---
name: redeyes-experience
description: 真红眼 (Red-Eyes) deck experience: fusion engine, one-card combo, extenders, halt points
---
# 真红眼 (Red-Eyes) Deck Experience

- **Deck Identity**

- DARK Dragon deck built around the Normal monster 真红眼黑龙 74677422 and its fusion toolbox, all fusion targets name a 真红眼 monster as material
- Key main deck monsters: 真红眼黑炎龙 30079770, 真红眼亚黑龙 18491580, 真红眼幼龙 58257569, 真红眼飞龙 67300516, 传说的黑石 66574418, 黑钢龙 93969023, 真红眼铁骑士-基亚·弗里德 85651167, 真红眼凶雷皇-邪性恶魔 39357122, 真红眼的凶星龙-流星之龙 17871506
- Fusion monsters: 真红眼黑刃龙 21140872, 恶魔龙 暗黑魔龙 45349196, 流星龙 流星黑龙 30086349, 真红眼黑星龙 27657173, 真红眼黑龙剑 19747827
- Xyz boss: 真红眼钢炎龙 44405066; ritual boss: 真红王 19025379 via 真红眼转生 45410988; hybrid metal boss: 真红眼黑重钢龙 80870883 via 金属化·强化反射装甲 89812483
- Key spells: 真红眼融合 06172122, 真红眼看破 92353449, 真红眼之魂 44397496, 红玉之宝札 32566831, 黑炎弹 52684508; key traps: 真红眼的铠旋 39387565, 真红眼烧灭 71782404, 附锁链的真红眼牙 57135971, 暗龙族之爪 76076738
- Near-pure reference deck: /home/z/ygo/deck/220115真红眼/8dd6619eb94bc69b.ydk, and 230114真红眼/240727真红眼 variants; the deck list format carries no main/extra section markers

- **Core Mechanic: 真红眼融合 Lock**

- 真红眼融合 06172122 fuses using hand, deck, and field monsters, so a single copy in hand is a full fusion play with zero other setup
- Its activation cost forbids any Normal or Special Summon this turn before it, and after it resolves the player cannot summon or special summon except by that card's own effect, verified in script as ACTIVITY_SUMMON and ACTIVITY_SPSUMMON checks plus an oath lock
- The summoned fusion monster's name becomes 真红眼黑龙 74677422, which matters for name-based effects like 黑炎弹 52684508 and 真红之魂's burn
- Fusion material setcode is 0x3b, so any 真红眼 fusion is legal, and the deck can also fuse 6星「恶魔」通常怪兽 with 真红眼通常怪兽 into 恶魔龙 暗黑魔龙 45349196 using 恶魔召唤 70781052
- Gemini monsters 真红眼黑炎龙 30079770 and 真红眼凶雷皇 39357122 are treated as Normal on field and in grave, so they qualify as Normal targets for 真红眼钢炎龙's revival and as fusion material from the field, but not from hand or deck

- **One-Card Combo: 真红眼融合**

- Starter: 真红眼融合 06172122 in hand, no other cards needed
- Step 1: activate 真红眼融合, fuse 真红眼黑龙 74677422 from deck plus 恶魔召唤 70781052 from deck into 恶魔龙 暗黑魔龙 45349196, a 3200 ATK battle floodgate
- Step 2: 恶魔龙 暗黑魔龙's battle shuts off opponent effects until damage step end, and at battle phase end it burns 2400 (真红眼黑龙's original ATK) and recycles 真红眼黑龙 to deck
- Alternative line: fuse 真红眼黑龙 74677422 plus a 6星龙族 monster into 流星龙 流星黑龙 30086349, which dumps a 真红眼 monster from hand or deck for half-ATK burn and revives a Normal on leaving field
- Alternative line: fuse 真红眼黑龙 74677422 plus 真红眼铁骑士-基亚·弗里德 85651167 into 真红眼黑刃龙 21140872, a 2800 ATK negate-and-equip wall
- The fusion lock ends the turn's summoning, so the play is a single 真红眼融合 then pass

- **End Field One-Card**

- 真红眼黑刃龙 21140872 (or 恶魔龙 暗黑魔龙 45349196, 流星龙 流星黑龙 30086349) plus grave setup of 真红眼黑龙 74677422 for 真红眼之魂 44397496 or 真红眼的铠旋 39387565 recursion next turn
- 真红眼黑刃龙 21140872 negates any effect targeting your cards by sending one equip to grave, and equips a warrior from grave on a 真红眼 attack
- 真红眼钢炎龙 44405066 as an additional Xyz: 2 level-7 monsters, burns 500 per opponent effect activation while it has material, is effect-indestructible with material, and detaches to revive a 真红眼 Normal from grave in either turn
- Halt point: Ash Blossom 14558127 on 真红眼融合 kills the whole line because the fusion is the entire turn and the lock still applies

- **Extender: 传说的黑石 66574418**

- Tribute it to special summon any 7-star-or-below 真红眼 monster from deck, then in grave shuffle a 真红眼 monster back to deck to add itself to hand, a self-recycling loop
- Feeds 真红眼黑龙 74677422 onto the field for a following 真红眼融合 fusion, and its grave effect works with 真红眼黑星龙 27657173 or 真红眼看破 92353449 dumps

- **Extender: 黑钢龙 93969023**

- Equips itself from hand or field to a 真红眼 monster for 600 ATK, and when it leaves the field searches any 真红眼 card from deck, including 真红眼融合 06172122
- Standard loop: equip 黑钢龙 to 真红眼黑龙 74677422, use it as fusion material or send it to grave, then search 真红眼融合 for the next turn
- 真红眼幼龙 58257569 battle-destroyed special summons a 7-star-or-below 真红眼 from deck and equips itself for 300 ATK, then adds a level-1 Dragon like 黑钢龙 from deck or grave when the equip leaves the field

- **Extender: 真红眼黑星龙 27657173**

- From hand it sends a level-5-or-higher Normal monster from hand or deck to grave, special summons itself, and becomes level 7, enabling 真红眼钢炎龙 44405066 with a second level 7
- In grave it banishes itself to add 真红眼融合 06172122 from deck or grave, but only on a later turn, verified by aux.exccon condition
- Combines with 红玉之宝札 32566831 which dumps a 7-star 真红眼 monster to draw 2 then optionally dumps another

- **Extender: 真红眼暗钢龙 88264978**

- Special summons itself by banishing a face-up Dragon on field, then revives any Dragon from hand or grave once per turn, the generic Dragon extender of the 龙族 hybrid
- Banishing 真红眼黑龙 74677422 or a token enables 真红眼钢炎龙 44405066 plays and 流星龙 流星黑龙 30086349 fusion from hand

- **Extender: 真红眼之魂 44397496 and 真红眼的铠旋 39387565**

- 真红眼之魂 special summons any 真红眼 monster from grave, the simplest recursion
- 真红眼的铠旋 as a continuous trap revives a Normal monster from grave as a quick effect while you control a 真红眼, and if destroyed by opponent effect it revives a 真红眼 monster from grave

- **Extender: 真红眼亚黑龙 18491580**

- Special summons itself by tributing a 真红眼 monster from hand or field, and when destroyed by battle or opponent effect revives a 7-star-or-below 真红眼 from grave with doubled original ATK if it is 真红眼黑龙 74677422

- **Extender: 真红之魂 06556909**

- Its name is treated as 真红眼黑龙 74677422 on field and in grave, so it satisfies name-based fusion and 黑炎弹 52684508 targets
- When the opponent special summons, send it to grave to special summon a 真红眼 monster from hand or deck, and once per duel it can burn the original ATK of a 真红眼黑龙 on the field in either turn

- **Halt Points**

- 真红眼融合 06172122 cannot be activated after any summon or special summon that turn, so never normal summon first
- After 真红眼融合 resolves no other summon is legal that turn, so extenders like 传说的黑石 66574418 or 真红眼黑星龙 27657173 must be used on a different turn or before fusion when possible
- 真红眼看破 92353449 requires discarding a 真红眼 monster from hand or deck as cost, so an empty 真红眼 pool in deck stops it
- 真红眼黑星龙 27657173's grave add is banned the same turn it was sent to grave, and 真红眼亚黑龙 18491580's revival needs a 7-star-or-below 真红眼 target in grave
- 真红眼钢炎龙 44405066 loses effect-indestructibility and the 500 burn once its last material is detached

- **Mirror Match: 真红眼 vs 真红眼**

- Whichever player resolves 真红眼融合 06172122 first establishes the bigger fusion because the lock prevents the mirror from answering with a fusion of their own
- 真红眼黑刃龙 21140872's negation answers effects that target your cards, so chain it to 真红眼之魂 44397496 or 真红眼的铠旋 39387565 revival effects
- 恶魔龙 暗黑魔龙 45349196's battle floodgate decides combat, so avoid attacking into it without removal
- 真红眼钢炎龙 44405066 burns 500 per opponent activation, so minimize effect activations while it has materials
- 真红眼烧灭 71782404 punishes both players, so a destroyed 真红眼 can burn the opponent out but also hurts you

- **Common Mistakes**

- Do not activate 真红眼融合 06172122 after a normal summon or any special summon that turn, the cost check makes it illegal
- Do not try to special summon after 真红眼融合 resolves, the oath lock forbids it
- Do not forget the fused monster's name becomes 真红眼黑龙 74677422, which enables 黑炎弹 52684508 (2400 burn) and 真红之魂 06556909 burn but also means 黑炎弹 blocks that monster from attacking
- 真红眼黑星龙 27657173 needs a level-5-or-higher Normal monster to dump, so keep 真红眼黑龙 74677422 or 恶魔召唤 70781052 in deck and never empty the normal pool
- 真红眼幼龙 58257569 special summons from deck only when destroyed by battle, so do not waste its effect window
- 真红眼暗钢龙 88264978 banishes a face-up Dragon as cost, so never banish the only material you need for the fusion
- 真红眼黑刃龙 21140872 equips only warrior monsters from grave, so its equipped monster pool is built from 真红眼铁骑士-基亚·弗里德 85651167 and other warriors
- 真红眼钢炎龙 44405066 requires 2 level-7 monsters as material, so use 真红眼黑炎龙 30079770, 真红眼亚黑龙 18491580, 真红之魂 06556909, or 真红眼黑星龙 27657173 after its level-up
- 真红眼转生 45410988 needs level total 8 or more and can banish 真红眼 monsters from grave as tribute substitute, so check grave count before declaring the ritual
