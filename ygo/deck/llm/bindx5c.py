#!/bin/env python
from ygonn import *
import lightning as L


class Model(L.LightningModule):
    def __init__(self):
        super().__init__()
        layer, exp, expo, h, hff, e, ent = 8, 8, 12, 16, 2, 1+len(cards()), 10.7
        c, d = (h**.5*ent/4).__ceil__()*4, (ent/4).__ceil__()*4
        self._ = Seq(
            Embedding(e, c, scale_grad_by_freq=True),
            SeqStack(Seq(
                Add(
                    Seq(
                        RMSNorm(c),
                        Linear(c, 2*exp*c),
                        F(swiglu),
                        Linear(exp*c, 3*h*d+hff*2*c, False),
                    ),
                    Linear(c, 3*h*d+hff*2*c),
                ),
                F(torch.split, (3*h*d, hff*2*c), -1),
                ZipCat(
                    Seq(
                        Unflatten(-1, (3, -1, d)),
                        F(at),
                        Einsum('...hd,hcd->...hc', (h, 2*c, d), bias=(h, 2*c)),
                    ),
                    Unflatten(-1, (-1, 2*c)),
                ).dim_(-2),
                F(softmaxglu),
            )for _ in range(layer)),
            Add(
                Seq(
                    Linear(c, 2*expo*c),
                    F(swiglu),
                    Linear(expo*c, e, False),
                ),
                Linear(c, e),
            ),
        )
        print(self._)
        self._ = torch.compile(self._, dynamic=False, fullgraph=True, options={'triton.cudagraphs': True, 'shape_padding': True})

    def forward(self, x):
        return self._(x)

    def training_step(self, x, _):
        y = self.forward(x)
        t = settarget(x, y.size(-1))
        l = crossentropy(y, t)+log(t.ravel())@t.ravel()/t.shape[:-1].numel()
        self.log_dict({f'los{i}': l for i, l in enumerate(l)})
        return l.mean()

    def configure_optimizers(self) -> torch.optim.Adam:
        return torch.optim.Adam(self.parameters(), 1e-4)


L.Trainer(precision=16, gradient_clip_val=1).fit(
    Model.load_from_checkpoint('lightning_logs/version_26/checkpoints/epoch=72-step=664300.ckpt'),
    torch.utils.data.DataLoader(decks(), shuffle=True, batch_size=16, collate_fn=functools.partial(setcollate, mi=75, ma=75))
)
