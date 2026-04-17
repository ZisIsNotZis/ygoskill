#!/bin/env python
from ygonn import *
import lightning as L


class Model(L.LightningModule):
    def __init__(self):
        super().__init__()
        layer = 8
        expe = exp = 8  # expansion for embedding and model
        head, headlin = 16, 2  # head for self attention (hard wired/weighted) and linear path (hard wired/weighted)
        ent = 10.6756  # token log2 entropy
        comp = round(head**.5*ent/4)*4  # compressed size (layer boundary, nonlinear uncompress)
        uncomp = round(head**.75*ent/4)*4  # uncompressed size (in layer, linear compress)
        self.emb = Seq(
            ZipAdd(
                Linear(794, 2*max(expe*comp, uncomp//2)+comp),
                Embedding(27, 2*max(expe*comp, uncomp//2)+comp, 0, scale_grad_by_freq=True),
                Embedding(8, 2*max(expe*comp, uncomp//2)+comp, 0, scale_grad_by_freq=True),
                Unpak(EmbeddingBag(28, 2*max(expe*comp, uncomp//2)+comp, mode='sum', scale_grad_by_freq=True)),
            ),
            F(torch.split, (2*max(expe*comp, uncomp//2), comp), -1),
            ZipAdd(
                Seq(
                    F(swiglu),
                    Linear(max(expe*comp, uncomp//2), comp, False),
                ),
                Identity(),
            ),
        )
        self.m = SeqStack(Seq(
            RMSNorm(comp),
            Linear(comp, 2*max(exp*comp, uncomp//2)+3*head*round(ent)+headlin*uncomp),
            F(torch.split, (2*max(exp*comp, uncomp//2), 3*head*round(ent)+headlin*uncomp), -1),
            ZipAdd(
                Seq(
                    F(swiglu),
                    Linear(max(exp*comp, uncomp//2), 3*head*round(ent)+headlin*uncomp, False),
                ),
                Identity(),
            ),
            F(torch.split, (3*head*round(ent), headlin*uncomp), -1),
            ZipCat(
                Seq(
                    Unflatten(-1, (3, head, -1)),
                    F(at),
                    Einsum('...hd,hcd->...hc', (head, uncomp, round(ent)), bias=(head, uncomp)),
                ),
                Unflatten(-1, (-1, uncomp)),
            ).dim_(-2),
            MapRes(Linear(uncomp, uncomp)),
            F(softmaxglu),
            Linear(uncomp, comp),
        )for _ in range(layer))
        print(self.emb, self.m)
        self.emb, self.m = (torch.compile(i, dynamic=False, fullgraph=True, options={'triton.cudagraphs': True, 'shape_padding': True})for i in (self.emb, self.m))

    def forward(self, x):
        return self.m((_ := self.emb(X))[x])@_.T

    def training_step(self, x, _):
        y = self.forward(x[:, :-1])
        t = settarget(x, y.size(-1), remain=True)
        l = crossentropy(y, t)+log(t.ravel())@t.ravel()/t.shape[:-1].numel()
        self.log_dict({f'los{i}': l for i, l in enumerate(l)})
        return l.mean()

    def configure_optimizers(self) -> torch.optim.Adam:
        return torch.optim.Adam(self.parameters(), 1e-4)


X = cardsfeatmin().to('cuda')
L.Trainer(precision=16, gradient_clip_val=1).fit(
    Model(),
    torch.utils.data.DataLoader(decks(), shuffle=True, batch_size=16, collate_fn=functools.partial(setcollate, mi=75, ma=75))
)
