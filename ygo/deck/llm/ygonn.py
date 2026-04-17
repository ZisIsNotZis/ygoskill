from nn import *


@functools.cache
def sets() -> dict[int, str]:
    return {int(i, 16): j for i in open('strings.conf').read().split('setname ')[1:]for i, j in [i.split()[:2]]}


@functools.cache
def lfs() -> dict[int, int]:
    return {i: j for i in open('lflist.conf').read().split('\n\n')[0].split('\n')if i[0]not in '#!'for i, j in [map(int, i.split()[:2])]}


@functools.cache
def cards(bind=False) -> dict[int, int]:
    if bind:
        try:
            return {x: i for i, x in enumerate(fromfile('binds.i').tolist(), 1)}
        except FileNotFoundError as _:
            print(_)
    x = sum(sqlite3.connect('cards.cdb').execute('select id from datas where not alias order by id'), ())
    if bind:
        tofile('binds', torch.tensor(x, dtype=torch.int))
    return {x: i for i, x in enumerate(x, 1)}


@functools.cache
def aliases() -> dict[int, int]:
    return dict(sqlite3.connect('cards.cdb').execute('select id,alias from datas where alias'))


@functools.cache
def extras() -> tuple[int, ...]:
    return sum(sqlite3.connect('cards.cdb').execute('select id from datas where type&0x4802040 and not alias'), ())


@functools.cache
def decks(dev='cpu', bind=False) -> list[torch.Tensor]:
    return [torch.tensor([i for i in open(i).read().split('!')[0].split()if i.isdigit()for i in [cards(bind).get(aliases().get(int(i), int(i)), 0)]if i], dtype=torch.short, device=dev)for i in glob.glob('deck/*/*')]


@functools.cache
def cntdecks(dev='cpu', bind=False) -> list[torch.Tensor]:
    return [torch.stack((i, j.to(i.dtype)), 1)for i in decks(dev, bind)for i, j in [torch.unique(i, return_counts=True)]]


class Cardsfeat(typing.NamedTuple):
    lvAtkDefPNameDescSet: torch.Tensor  # 1113/794
    race: torch.Tensor  # 1+26
    att: torch.Tensor  # 1+7
    catTypeP: tuple[torch.Tensor, torch.Tensor]  # 32+32(27)+8/20+8

    def to(self, dev: torch.device | str | None = None, type: torch.dtype | None = None):
        return Cardsfeat(self.lvAtkDefPNameDescSet.to(dev, type), self.race.to(dev), self.att.to(dev), (self.catTypeP[0].to(dev), self.catTypeP[1].to(dev)))


@functools.cache
def cardsfeat(dev='cpu', dtype=torch.half, cdev='cuda', ctype=torch.half, model='', feat=.95) -> Cardsfeat:
    cards = list(zip((torch.zeros(4100, device=dev, dtype=dtype), 0, 0, torch.zeros(0, dtype=torch.int, device=dev)), *[(
        torch.cat([
            torch.tensor([level & 15, max(atk, 0), not type & 0x4000000 and max(Def, 0), level >> 24], device=dev, dtype=dtype),
            emb(name, model, dev, dtype, cdev, ctype),
            emb(desc.replace('\r', '').replace('\n', '').strip(), model, dev, dtype, cdev, ctype),
            emb(Try(lambda: open(f'script/c{i}.lua').read().replace('\r', '').replace('\n', r'\n').strip(), ''), model, dev, dtype, cdev, ctype),
            sum((emb(sets()[setcode >> i & 0xffff], model, dev, dtype, cdev, ctype)for i in range(0, 64, 16)if setcode >> i), torch.zeros(1024, device=dev, dtype=dtype)),
        ]),
        race.bit_length(),
        attribute.bit_length(),
        torch.tensor(np.unpackbits(np.array((category % 0x100000000, type, type & 0x4000000 and (Def >> 1 & 0xf0) | (Def & 0xf)), 'I').view('B')).nonzero()[0], device=dev, dtype=torch.int),
    )for i, setcode, type, atk, Def, level, race, attribute, category, name, desc in sqlite3.connect('cards.cdb').execute('select datas.id,setcode,type,atk,def,level,race,attribute,category,name,desc from datas join texts on datas.id=texts.id where not alias')]))
    embm.cache_clear()
    return Cardsfeat(
        pca(torch.stack(cards[0]), feat, 'cardsfeatpca'),
        torch.tensor(cards[1], device=dev, dtype=torch.int),
        torch.tensor(cards[2], device=dev, dtype=torch.int),
        (torch.cat(cards[3]), torch.tensor([0, *map(len, cards[3])], device=dev, dtype=torch.int)[:-1].cumsum_(0)),
    )


@functools.cache
def cardsfeatmin(dev='cpu', dtype=torch.half, cdev='cuda', ctype=torch.half, model='', feat=.95) -> Cardsfeat:
    cards = list(zip((torch.zeros(2051, device=dev, dtype=dtype), 0, 0, torch.zeros(0, dtype=torch.int, device=dev)), *[(
        torch.cat([
            torch.tensor([level & 15, max(atk, 0), not type & 0x4000000 and max(Def, 0)], device=dev, dtype=dtype),
            emb(name+''.join(i for i in range(0, 64, 16)for i in [sets().get(setcode >> i & 0xffff, '')]if i not in name), model, dev, dtype, cdev, ctype),
            emb(''.join(desc.split()), model, dev, dtype, cdev, ctype),
        ]),
        race.bit_length(),
        attribute.bit_length(),
        torch.as_tensor(np.unpackbits(np.array((type, type & 0x4000000 and Def), '>I').view('B')).reshape(-1, 32)[:, ::-1].flat[[1, 2, 4, 6, 7, 9, 10, 11, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 32, 33, 34, 35, 37, 38, 39, 40]], dtype=torch.int, device=dev),
    )for setcode, type, atk, Def, level, race, attribute, name, desc in sqlite3.connect('cards.cdb').execute('select setcode,type,atk,def,level,race,attribute,name,desc from datas join texts on datas.id=texts.id where not alias order by datas.id')]))
    embm.cache_clear()
    return Cardsfeat(
        pca(torch.stack(cards[0]), feat, 'cardsfeatminpca'),
        torch.tensor(cards[1], device=dev, dtype=torch.int),
        torch.tensor(cards[2], device=dev, dtype=torch.int),
        (torch.cat(cards[3]), torch.tensor([0, *map(len, cards[3])], device=dev, dtype=torch.int)[:-1].cumsum_(0)),
    )


if __name__ == '__main__':
    # cardsfeat()
    cardsfeatmin()
    # print(ent(torch.cat(decks('cpu'))))
