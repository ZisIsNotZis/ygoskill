from torch.nn import *
try:
    import flash_attn
except ModuleNotFoundError:
    flash_attn = None
import torch
import numpy as np
import functools
import typing
import pyarrow.parquet
import multiprocessing
import os
import glob
import sqlite3
import tqdm
from torch import Tensor
from typing import Callable, Iterable, Self, cast, IO

torch.set_float32_matmul_precision('medium')


def ostr(x) -> str:
    if isinstance(x, Tensor):
        return f"tensor({','.join(map(str, x.shape))},dtype={x.dtype},device='{x.device}')"
    if isinstance(x, np.ndarray):
        return f"array({','.join(map(str, x.shape))},dtype={x.dtype},device='{x.device}')"
    if isinstance(x, tuple):
        return '('+','.join(map(ostr, x))+')'
    if isinstance(x, list):
        return '['+','.join(map(ostr, x))+']'
    if isinstance(x, (set, frozenset)):
        return '{'+','.join(map(ostr, x))+'}'
    if isinstance(x, dict):
        return '{'+','.join(f"'{i}'={ostr(j)})"for i, j in x.items())+'}'
    return getattr(x, '__name__', '') or repr(x).strip()


def argstr(*arg, **kwarg) -> str:
    return ', '.join((*map(ostr, arg), *(f'{i}={ostr(j)}'for i, j in kwarg.items())))


def fstr(f: Callable, *arg, **kwarg) -> str:
    return f'{ostr(f)}({argstr(*arg, **kwarg)})'


def printed[T](x: T) -> T:
    print(ostr(x))
    return x


def Try[T](f: Callable[[], T], default: T = None) -> T:
    try:
        return f()
    except FileNotFoundError:
        return default


@functools.lru_cache
def parquet(f: str) -> pyarrow.parquet.ParquetFile:
    return pyarrow.parquet.ParquetFile(f, memory_map=True)


def parquetsrand(f: list[str], m: int = 4) -> list[Tensor]:
    a = parquet(f[np.random.randint(len(f))])
    return [torch.from_numpy(np.frombuffer(i[j], 'B'))for i in [a.read_row_group(np.random.randint(a.num_row_groups), ['text'])[0]]for j in np.random.randint(0, len(i), m)]


def parquetsrands(f: list[str], n: int = 1, m: int = 4, *arg, **kwarg) -> Iterable[Tensor]:
    q: multiprocessing.Queue[list[Tensor]] = multiprocessing.Queue(n*(os.cpu_count() or 4))
    for _ in range(os.cpu_count() or 4):
        multiprocessing.Process(target=lambda: sum(iter(lambda: q.put(parquetsrand(f, m)) or 0, 1))).start()
    return iter(lambda: collate(sum((q.get()for _ in range(n)), []), *arg, **kwarg), None)


class Lend[T]:
    def __init__(self, a: Iterable[T], l: int = 65536):
        self.a = a
        self.l = l

    def __iter__(self) -> Iterable[T]:
        return iter(self.a)

    def __len__(self) -> int:
        return self.l


type Fn[T] = Callable[[T], T | None] | T | None


def fn[T](f: Fn[T], x: T | None) -> T | None:
    return x if f is None or x is None else f(x) if isinstance(f, Callable) else f


class Dimd:
    dim = 0

    def dim_(self, dim: int) -> Self:
        self.dim = dim
        return self


class Reprd(Module):
    name = ''

    def __init__(self, *arg, **kwarg):
        super().__init__()
        self.arg = arg
        self.kwarg = kwarg

    def extra_repr(self):
        return argstr(*self.arg, **self.kwarg)

    def name_(self, name: str) -> Self:
        self.name = name
        return self

    def _get_name(self):
        return self.name or self.__class__.__name__


class Unpak(Module):
    def __init__(self, f: Callable):
        super().__init__()
        self.f = f

    def forward(self, x, *arg, **kwarg):
        return self.f(*x, *arg, **kwarg)


class Base(ModuleList):
    def __init__(self, *arg: Module | Iterable[Module]):
        super().__init__(cast(list[Module], arg)if len(arg) != 1 or isinstance(arg[0], Module)else arg[0])

    def forward(self, x) -> list:
        return [x := self(x)for self in self]


class Seq(Base):
    def forward(self, x):
        return super().forward(x)[-1]


class SeqCat(Base, Dimd):
    def forward(self, x) -> Tensor:  # type: ignore
        return torch.cat(super().forward(x), self.dim)


class SeqStack(Base, Dimd):
    def forward(self, x) -> Tensor:  # type: ignore
        return torch.stack(super().forward(x), self.dim)


class Res(Seq):
    def forward(self, x: Tensor) -> Tensor:
        return super().forward(x)+x


class MapRes(Seq):
    def forward(self, x) -> tuple:
        return super().forward(x), x


class StackRes(Seq, Dimd):
    def forward(self, x: Tensor) -> Tensor:
        return torch.stack([super().forward(x), x], self.dim)


class CatRes(Seq, Dimd):
    def forward(self, x: Tensor) -> Tensor:
        return torch.cat([super().forward(x), x], self.dim)


class Zip(Base):
    def forward(self, x: Iterable) -> list:
        x = list(x)
        assert len(self) == len(x)
        return [self(x)for self, x in zip(self, x)]


class ZipAdd(Zip):
    def forward(self, x: Iterable) -> Tensor:  # type: ignore
        return functools.reduce(torch.add, super().forward(x))


class ZipMul(Zip):
    def forward(self, x: Iterable) -> Tensor:  # type: ignore
        return functools.reduce(torch.mul, super().forward(x))


class ZipCat(Zip, Dimd):
    def forward(self, x: Iterable) -> Tensor:  # type: ignore
        return torch.cat(super().forward(x), self.dim)


class ZipStack(Zip, Dimd):
    def forward(self, x: Iterable) -> Tensor:  # type: ignore
        return torch.stack(super().forward(x), self.dim)


class Map(Base):
    def forward(self, x) -> list:
        return [self(x)for self in self]


class Add(Map):
    def forward(self, x) -> Tensor:  # type: ignore
        return functools.reduce(torch.add, super().forward(x))


class Mul(Map):
    def forward(self, x) -> Tensor:  # type: ignore
        return functools.reduce(torch.mul, super().forward(x))


class Cat(Map, Dimd):
    def forward(self, x) -> Tensor:  # type: ignore
        return torch.cat(super().forward(x), self.dim)


class Stack(Map, Dimd):
    def forward(self, x) -> Tensor:  # type: ignore
        return torch.stack(super().forward(x), self.dim)


class F(Reprd):
    def __init__(self, f: Callable, *arg, **kwarg):
        super().__init__(f, *arg, **kwarg)
        self.f = f

    def forward(self, x):
        return self.f(x, *self.arg[1:], **self.kwarg)


class Einsum(Reprd):
    def __init__(self, eq: str, *arg: tuple[int, ...] | Fn[Tensor], f: Fn[Tensor] = None, bias: tuple[int, ...] | Fn[Tensor] = None):
        eq, out = eq.split('->')
        In, eq = eq.split(',', 1)
        eqarg = [(i, j) for i, j in zip(eq.split(','), arg)if j is not None]
        eqs, arg = zip(*eqarg)
        eq = f'{In},{','.join(eqs)}->{out}'
        super().__init__(eq, *arg, _=f, bias=bias)
        self.eq = eq
        self.l = len(eqs)
        self.f = f
        eq = ''.join(i for i, j in eqarg if isinstance(j, tuple))
        for k, (i, j) in enumerate(eqarg):
            setattr(self, f'_{k}', Parameter(init.uniform_(torch.empty(j), k := -self.calculate_in(i, j, In, eq, out), -k))if isinstance(j, tuple)else j)
        self.bias = Parameter(init.uniform_(torch.empty(bias), k := -self.calculate_in(eq, sum((j for j in arg if isinstance(j, tuple)), ()), In, eq, out), -k))if isinstance(bias, (int, tuple))else bias

    def forward(self, x: Tensor) -> Tensor:
        match self.l:
            case 1: y = torch.einsum(self.eq, fn(self.f, x), fn(self._0, x))
            case 2: y = torch.einsum(self.eq, fn(self.f, x), fn(self._0, x), fn(self._1, x))
            case 3: y = torch.einsum(self.eq, fn(self.f, x), fn(self._0, x), fn(self._1, x), fn(self._2, x))
            case 4: y = torch.einsum(self.eq, fn(self.f, x), fn(self._0, x), fn(self._1, x), fn(self._2, x), fn(self._3, x))
            case 5: y = torch.einsum(self.eq, fn(self.f, x), fn(self._0, x), fn(self._1, x), fn(self._2, x), fn(self._3, x), fn(self._4, x))
            case 6: y = torch.einsum(self.eq, fn(self.f, x), fn(self._0, x), fn(self._1, x), fn(self._2, x), fn(self._3, x), fn(self._4, x), fn(self._5, x))
            case 7: y = torch.einsum(self.eq, fn(self.f, x), fn(self._0, x), fn(self._1, x), fn(self._2, x), fn(self._3, x), fn(self._4, x), fn(self._5, x), fn(self._6, x))
            case 8: y = torch.einsum(self.eq, fn(self.f, x), fn(self._0, x), fn(self._1, x), fn(self._2, x), fn(self._3, x), fn(self._4, x), fn(self._5, x), fn(self._6, x), fn(self._7, x))
            case 9: y = torch.einsum(self.eq, fn(self.f, x), fn(self._0, x), fn(self._1, x), fn(self._2, x), fn(self._3, x), fn(self._4, x), fn(self._5, x), fn(self._6, x), fn(self._7, x), fn(self._8, x))
            case _: y = torch.einsum(self.eq, fn(self.f, x), *(fn(getattr(self, f'_{i}'), x)for i in range(len(self.arg)-1)))
        return add(y, fn(self.bias, x))

    @staticmethod
    def calculate_in(eq: str, _: tuple[int, ...], In: str, eqs: str, out: str) -> float:
        return functools.reduce(float.__mul__, (float(i in out or i not in In) or j**(-.5/eqs.count(i))for i, j in zip(eq, _)))

    @staticmethod
    def calculate_gain(f: int | float | init._NonlinearityType | Callable[[Tensor], Tensor], _=1 << 16) -> float:
        return f if isinstance(f, (int, float)) else init.calculate_gain(cast(init._NonlinearityType, f)) if isinstance(f, str) else (2*_)**.5/torch.func.vjp(f, torch.randn(_))[0].norm()


def tiny(x: Tensor) -> Tensor:
    return x+torch.finfo(x.dtype).tiny*torch.finfo(x.dtype).eps


def crossentropy(y: Tensor, t: Tensor, logsoftmax=True) -> Tensor:
    if t.dtype == torch.long:
        t = t[..., None]
    l = (functional.cross_entropy if logsoftmax else functional.nll_loss)(y.permute(0, y.ndim-1, *range(1, y.ndim-1)), t.expand_as(y)[..., 0]if t.dtype == torch.long else t.expand_as(y).permute(0, y.ndim-1, *range(1, y.ndim-1)), reduction='none'if y.ndim > t.ndim else 'mean')
    return l.mean(list(range(1-t.ndim, 0)))if y.ndim > t.ndim else l


def tofile(f: str | IO, a: Tensor, type: torch.dtype | None = None) -> Tensor:
    (_ := a.data.to('cpu', type).contiguous().numpy()).tofile(f'{f}.{','.join(map(str, a.shape[1:]))}{_.dtype.char}'if isinstance(f, str) else f)
    return a


def fromfile(f: str, dev: torch.device | str = 'cpu', type: torch.dtype | None = None) -> Tensor:
    return torch.as_tensor(np.memmap(f, f.split('.')[-1]), device=dev, dtype=type)


def tfilter[T](x: Iterable[T | None]) -> list[T]:
    return [x for x in x if isinstance(x, (np.ndarray, Tensor)) or x]


def add(*x: Tensor | None) -> Tensor:
    return functools.reduce(torch.add, tfilter(x))


def sub(*x: Tensor | None) -> Tensor:
    return functools.reduce(torch.sub, tfilter(x))


def mul(*x: Tensor | None) -> Tensor:
    return functools.reduce(torch.mul, tfilter(x))


def div(x: Tensor, *y: Tensor | None) -> Tensor:
    return x/tiny(functools.reduce(torch.mul, tfilter(y)))


def log(x: Tensor) -> Tensor:
    return tiny(x).log()


def log2(x: Tensor) -> Tensor:
    return tiny(x).log2()


def rope(q: Tensor, k: Tensor, l: int = 0, L: int = 0) -> list[Tensor]:
    cos = torch.arange(q.size(-3), dtype=q.dtype, device=q.device)[:, None, None]*torch.logspace(np.log10(np.pi/(l or 1)), np.log10(np.pi/(L or q.size(-3))), q.shape[-2:].numel()//2, dtype=q.dtype, device=q.device).reshape(-1, q.size(-2)).T
    cos, sin = cos.cos(), cos.sin()
    cos, sin = torch.cat([cos, sin], 2), torch.cat([-sin, cos], 2)
    return [cos*q+sin*q.roll(q.size(-1)//2, -1)for q in (q, k)]


def depe(q: Tensor, k: Tensor, l: int = 0, L: int = 0) -> tuple[Tensor, Tensor]:
    logw = torch.logspace(1/(l or 256), 1/(L or q.size(-3)), q.shape[-2:].numel(), device=q.device).reshape(-1, q.size(-2)).T**torch.arange(q.size(-3), device=q.device)[:, None, None]
    return q/logw.cumsum(-3), k*logw


def broadcasttensors(x: list[Tensor], ndim: tuple[int, ...] = ()) -> list[Tensor]:
    sz = [-1 if i in ndim else j for i, j in enumerate(torch.broadcast_shapes(*map(Tensor.size, x)))]
    return [x.expand(sz)for x in x]


def exactnd(x: list[Tensor], dim: tuple[int, ...], ndim: tuple[int, ...] = ()) -> tuple[list[Tensor], tuple[int, ...]]:
    x = broadcasttensors([functools.reduce(Tensor.unsqueeze_, dim[x.ndim:], x)for x in x], ndim)
    return [x.flatten(0, x.ndim-len(dim))for x in x], x[0].shape[:1-len(dim)]


def at(
    q: Tensor | None | tuple[Tensor, ...],
    k: Tensor | None = None,
    v: Tensor | None = None,
    pe: Callable[[Tensor, Tensor], tuple[Tensor, Tensor]] | None = None,
    causal: bool = True,
    **arg
) -> Tensor:
    if isinstance(q, tuple):
        q, k, v = (q+(None,)*2)[:3]
    assert q is not None
    if k is None:
        (q,), size = exactnd([q], (0, 1, 1, 0, 2))
        if not pe and q.device.type != 'cpu' and flash_attn:
            return flash_attn.flash_attn_qkvpacked_func(cudahalf(q).expand(-1, -1, 3, -1, -1), causal=causal, **arg).unflatten(0, size)
        q, k, v = q.permute(2, 0, 1, 3, 4)
    elif v is None:
        (q, k), size = exactnd([q, k], (0, 1, 1, 0, 2), (2, 3))
        q.squeeze_(2)
        if not pe and q.device.type != 'cpu' and flash_attn:
            return flash_attn.flash_attn_kvpacked_func(cudahalf(q), cudahalf(k).expand(-1, -1, 2, -1, -1), causal=causal, **arg).unflatten(0, size)
        k, v = k.permute(2, 0, 1, 3, 4)
    else:
        (q, k, v), size = exactnd([q, k, v], (0, 1, 1, 0), (2,))
    if pe:
        q, k = pe(q, k)
    if q.device.type != 'cpu' and flash_attn:
        return flash_attn.flash_attn_func(cudahalf(q), cudahalf(k), cudahalf(v).expand_as(k), causal=causal, **arg).unflatten(0, size)
    return functional.scaled_dot_product_attention(q.transpose(1, 2), k.transpose(1, 2), v.transpose(1, 2), is_causal=causal, **arg).transpose(1, 2).unflatten(0, size)


def swiglu(x: Tensor | tuple[Tensor, Tensor], dim: int = -1) -> Tensor:
    g, x = x.chunk(2, dim) if isinstance(x, Tensor) else x
    return functional.silu(g)*x


def softmaxglu(x: Tensor | tuple[Tensor, Tensor], dim: int = -1) -> Tensor:
    g, x = x.chunk(2, dim) if isinstance(x, Tensor) else x
    return torch.einsum('...hd,...hd->...d', g.softmax(-2), x)


def softmaxgate(x: Tensor) -> Tensor:
    return (x[0].mT.softmax(-1)[..., None, :]@x[1].mT[..., None])[..., 0, 0]


def cudahalf(x: Tensor) -> Tensor:
    return x.to('cuda', torch.bfloat16 if x.dtype == torch.bfloat16 else torch.half)


def cumsum(x: Tensor, *dim: int) -> Tensor:
    for i in dim or [-1]:
        x = x.cumsum(i)
    return x


def cummean(x: Tensor, *dim: int) -> Tensor:
    return cumsum(x, *dim)/functools.reduce(torch.mul, [torch.arange(1, 1+x.size(i), dtype=x.dtype, device=x.device)[:, *[None]*(-i-1)]for i in dim or [-1]])


def cumrmsnorm(x: Tensor, *dim: int) -> Tensor:
    return div(x, cummean(x.square(), *dim).sqrt())


def cumlayernorm(x: Tensor, *dim: int) -> Tensor:
    x = x-cummean(x, *dim)
    return div(x, cummean(x.square(), *dim).sqrt())


def collate(x: list[Tensor], l: float = 1, mi: int = 1, ma: int = 4096) -> Tensor:
    l = max(min(round(np.quantile(list(map(len, x)), l)), ma), mi)
    return torch.stack([functional.pad(x, (0, 0)*(x.ndim-1)+(0, l-len(x)))if len(x) < l else x[(_ := np.random.randint(len(x)-l+1)):_+l]for x in x]).long()


def setcnt(x: Tensor) -> Tensor:
    return torch.stack([i.to(x.dtype)for i in torch.unique(x, return_counts=True)], -1)


def setcollate(x: list[Tensor], *arg, **kwarg) -> Tensor:
    return collate([x[torch.randperm(len(x))]for x in x], *arg, **kwarg)


def settarget(x: Tensor, e: int, count: Tensor | None = None, remain: bool = False) -> Tensor:
    if count is None:
        count = torch.ones(1, dtype=torch.uint8, device=x.device).expand_as(x)
    y = torch.zeros(*x.shape, e, dtype=count.dtype, device=x.device).scatter_add_(-1, x[..., None], count[..., None])
    if remain:
        y = y.flip(-2).cumsum_(-2)[..., :-1, :].flip(-2)
        y[..., 0] = 1-y[..., 1:].any(-1)
    else:
        y = y.sum(-2, True)
    return (y.float()/y.sum(-1, True)).contiguous()


@functools.cache
def embs(m: str, dev='cpu', type=torch.half) -> dict[str, Tensor]:
    try:
        x = open(f'{m.split('/')[-1]}.txt').read().split('\n')[:-1]
        return dict(zip(x, fromfile(f'{m.split('/')[-1]}.e', dev, type).reshape(len(x), -1)))
    except FileNotFoundError as _:
        return {}


@functools.cache
def embm(m: str, dev='cuda', type=torch.half):
    import transformers
    return torch.compile(transformers.AutoModel.from_pretrained(m, attn_implementation='flash_attention_2', device_map=dev, dtype=type).requires_grad_(False).eval(), dynamic=True)


@functools.cache
def embt(m: str):
    import transformers
    return transformers.AutoTokenizer.from_pretrained(m)


def emb(x: str, m='', dev='cpu', type=torch.half, cdev='cuda', ctype=torch.half) -> Tensor:
    if not m:
        m = 'Qwen/Qwen3-Embedding-0.6B'
    if x not in embs(m, dev, type):
        embs(m)[x] = embm(m, cdev, ctype)(**embt(m)(printed(x), return_tensors='pt').to(cdev))[0][0, -1].to(dev, type)
        open(f'{m.split('/')[-1]}.txt', 'a').write(x+'\n')
        tofile(open(f'{m.split('/')[-1]}.e', 'ab'), embs(m)[x], torch.half)
    return embs(m)[x]


def pca(x: Tensor, n=0., f='pca') -> Tensor:
    if not n:
        n = .95
    x -= x.mean(0)
    x /= x.std(0)
    try:
        return x@fromfile(f'{f}.{x.size(1)}e', x.device, x.dtype).T
    except FileNotFoundError as _:
        u, s, v = torch.pca_lowrank(x.float(), min(x.shape)if isinstance(n, float)else n, False)
        v /= s
        if isinstance(n, float):
            s = torch.searchsorted(s.square_().cumsum_(0), s[-1]*n)
            v = v[:, :s]
            u = u[:, :s]
        tofile(f, v.T, torch.half)
        return u.to(x.dtype)


def ent(x: Tensor):
    c = torch.zeros(int(x.max())+1, dtype=torch.int, device=x.device).scatter_add_(0, x.int(), torch.ones(1, dtype=torch.int, device=x.device).expand(len(x)))/len(x)
    return c@log2(c)


def softbackpack(x: Tensor, n=2, tmp=.2) -> Tensor:
    '''backpack x(...l)->p(...nl) s.t. x@p is as uniform as possible'''
    s = x[..., :n].clone()  # force first n value always separate, s.t. p is not uniform everywhere
    p = torch.eye(n, device=x.device, dtype=x.dtype).expand(*x.shape[:-1], n, n).unbind(-2)
    for x in x[..., n:, None].unbind(-2):
        p += (((s+x)/-tmp).softmax(-1),)
        s += x*p[-1]
    return torch.stack(p, -1)


def autosa(x: Tensor, h=2, causal=True) -> Tensor:
    '''self attention x(...lc)->x(...hlc) w/o hard wired projection'''
    u = x - x.mean(list(range(x.ndim)))
    u = u/u.std(list(range(x.ndim)))
    u = u/u.norm(dim=-1, keepdim=True)
    try:
        u, s, _ = u.float().svd()
    except:
        tofile('autosa', u)
        raise
    u = u.to(x.dtype)
    s = s.to(x.dtype)
    u *= s[..., None, :]
    u = u[..., None, :, :]*softbackpack(s, h)[..., None, :]
    return torch.nn.functional.scaled_dot_product_attention(u, u, x[:, None], is_causal=causal).transpose(1, 2)


def sinkhornnll(y: Tensor, t: Tensor, tmp=.2, it=10, logsoftmax=False) -> Tensor:
    if logsoftmax:
        y = y.log_softmax(-1)
    y = y.take_along_dim(t.expand(y.shape[:-1])[..., None, :], -1)
    m = (y/tmp).exp_().clone()
    for _ in range(it):
        m /= m.sum(-1, True)
        m /= m.sum(-2, True)
    return y.mul_(m).sum(list(range(-1-t.ndim, 0)))/-y.shape[-1-t.ndim:-1].numel()


if __name__ == '__main__':
    y = torch.rand(2, 3, 4, 5, requires_grad=True).log_softmax(-1)
    t = torch.randint(5, [3, 4])
    l = crossentropy(y, t)
    L = sinkhornnll(y, t)
    print(l, L)
    l.mean().backward()
    L.mean().backward()
