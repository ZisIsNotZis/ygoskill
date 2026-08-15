---
name: maliss-experience
description: 码丽丝 (M∀LICE/Maliss) deck experience: banish recursion engine, one-card combo, extenders, halt points
---
# 码丽丝 (M∀LICE / Maliss) Deck Experience

- **Deck Identity**

- Archetype 码丽丝 (M∀LICE / Maliss), OCG 2024 Supreme Darkness era, a LIGHT Cyberse Link combo deck built on banishing its own cards and summoning them back, setcode 447 (0x1BF)
- Main deck monsters are the four 码丽丝<兵卒> (Pawn) monsters, Level 3 LIGHT Cyberse with 300 DEF: 白兔 69272449 (1200 ATK), 睡鼠 32061192 (900 ATK), 柴郡猫 96676583 (1500 ATK), 三月兔 20938824 (600 ATK)
- Continuous Trap engine, the three 码丽丝<代码> cards: GWC-06 20726052, TB-11 57111661, MTP-07 94722358, each usable the turn it is Set by banishing 1 face-up 码丽丝 monster you control
- Extra deck bosses, the three 码丽丝<王后> Link monsters: 红心加密 21848500 (Link-3 boss, 2500 ATK), 白棋捆绑 95454996 (Link-3, 2300 ATK), 红棋勒索 68059897 (Link-3, 2300 ATK)
- Spells: field spell 梦游地下界 68337209 and Quick-Play 镜中奇像 93453053
- Near-pure build verified from deck/240928码丽丝, deck/241026码丽丝, deck/250125码丽丝: 睡鼠 x3, 白兔 x3, 柴郡猫 x2-3, 三月兔 x3 (later lists), 梦游地下界 x3, 封印之黄金柜 75500286 x2-3, one copy of each trap, plus handtraps, 次元吸引者 91800273, Bystials, and the Cyberse toolbox

- **Core Mechanic: Banish-Recursion Engine**

- Every Pawn has a once-per-turn trigger that fires when it is banished, verified in scripts as EVENT_REMOVE: 白兔/睡鼠/柴郡猫 pay 300 LP and Special Summon themselves, 三月兔 instead pays 300 LP and adds 1 banished 码丽丝 monster to hand
- The self-Summon from 白兔/睡鼠/柴郡猫 applies a lock for the rest of the turn: no Extra Deck Special Summons except Link monsters, so sequence all Fusion/Xyz/Synchro plays before starting the loop
- 三月兔 is the exception with no lock: its hand Quick Effect banishes 1 other 码丽丝 card from hand or grave during either Main Phase and Special Summons itself, its banish effect recycles
- Any card that banishes your cards feeds the loop: 睡鼠① banishes a 码丽丝 monster from deck and gives 码丽丝 monsters +600 ATK, 柴郡猫① banishes a 码丽丝 card from hand and draws 2, 梦游地下界① banishes from hand/deck/grave, 封印之黄金柜 75500286 banishes from deck
- 白兔 on Normal or Special Summon Sets 1 码丽丝 Trap from deck whose name is not in your grave, once per turn, the trap engine of the deck
- The three traps all carry the set-quick clause, scripted as EFFECT_TRAP_ACT_IN_SET_TURN with a banish-a-face-up-码丽丝 cost, so a trap Set this turn by 白兔 resolves immediately
- 红棋勒索 on Link Summon adds any 码丽丝 Spell, 白棋捆绑 on Link Summon banishes up to 3 cards from both graves, 红心加密's Quick Effect returns 1 banished 码丽丝 card to deck to banish 1 card on field, unnegatable while it points to a monster
- 梦游地下界② gives 码丽丝 Link monsters +3000 ATK while 3 or more different 码丽丝 Traps are banished, ③ forces opponent monsters to attack 码丽丝 Links, the power ceiling of the deck

- **One-Card Combo: 睡鼠 32061192 Opener**

- Standard opener is 1 Pawn starter plus 1 discard, every Pawn works as the starter; the published canonical line starts from 睡鼠, verified step by step against scripts and the deck's card pool
- Step 1: Normal Summon 睡鼠, activate ① banishing 三月兔 20938824 from deck (码丽丝 gain 600 ATK)
- Step 2: 三月兔③ pays 300 LP, adds banished 三月兔 to hand
- Step 3: Link 睡鼠 into 连接解码员 30342076 (Link-1, one Level 4 or lower Cyberse)
- Step 4: 三月兔① Quick Effect banishes 睡鼠 from grave and Special Summons itself, then 睡鼠③ pays 300 LP and Special Summons itself back, applying the Link-only lock
- Step 5: Link Summon 红棋勒索 68059897 using 解码员 plus 三月兔 plus 睡鼠 (3 materials including a 码丽丝, Link-3 in this cdb), 红棋勒索① adds 梦游地下界 68337209, 解码员① Special Summons itself back because it was material for a 2300+ ATK Cyberse Link
- Step 6: activate 梦游地下界, its ① banishes 白兔 69272449 from deck
- Step 7: 白兔③ pays 300 LP, Special Summons itself, 白兔① Sets MTP-07 94722358 from deck
- Step 8: activate Set MTP-07 by banishing 白兔 as cost, MTP-07① adds 柴郡猫 96676583 from deck, optional banish of 1 field card because a 码丽丝 Link is present
- Finish with the remaining bodies: 柴郡猫① banishes a 码丽丝 card from hand to draw 2 (the banished Pawn Summons itself), then use 点阵图跳离士 18789533, 模板弹涂鱼 24521325, 飞溅闪屏法师 59859086 or a Bystial as extra material to Link 红心加密 21848500 (exactly 3 monsters including 码丽丝), then 白棋捆绑 95454996 (3+ monsters including 码丽丝) whose ① banishes your used traps from grave to turn on the +3000 ATK, then S:P 小夜骑士 29301450
- Exact finish is draw-dependent, the skeleton is fixed: the loop always generates 睡鼠 + 三月兔 + 白兔 + a Set trap plus whatever the discard and draws provide

- **End Field**

- Standard end board: 红心加密 21848500 plus S:P 小夜骑士 29301450 plus 梦游地下界 68337209 face-up with 3 different 码丽丝 Traps banished, making 红心加密 5500 ATK with a once-per-turn unnegatable quick banish
- 白棋捆绑 95454996 is the preferred second Link when bodies allow, its grave-wipe banishes the used GWC-06 20726052 / TB-11 57111661 / MTP-07 94722358 to enable the field spell boost
- One 码丽丝 Trap left Set (usually GWC-06) extends next turn, 连接栗子球 41999284 and 连环栗仔球 24842059 in grave answer attacks and trap activations
- Alternative builds finish on 召命之神弓-阿波罗萨 4280258 plus 访问码语者 86066372 with GWC-06 Set and 三月兔 20938824 recycled in hand
- Grind builds climb into 防火龙 5043010 or 防火龙·暗流体 64211118 (Link-5) to bounce or stack ATK

- **Extenders**

- 封印之黄金柜 75500286 banishes a Pawn from deck, its banish trigger Summons it, a two-for-one starter alongside any Pawn
- 梦游地下界 68337209① banishes from hand/deck/grave on activation, same trigger value as 黄金柜
- 三月兔 20938824 is the fastest extender: hand Quick Effect needs any other 码丽丝 in hand or grave
- 镜中奇像 93453053 negates an opponent monster by banishing a 码丽丝 from hand or face-up field, and if itself banished swaps a grave 码丽丝 for a same-type 码丽丝 from deck
- 点阵图跳离士 18789533 Special Summons itself when sent to grave or banished, a free Link material
- 模板弹涂鱼 24521325 Special Summons itself into a zone a Cyberse Link points to, and for one Link Summon can count as the same name as a banished Cyberse
- 飞溅闪屏法师 59859086 revives a Cyberse from grave in Defense (negated, Cyberse-only after), and 盛悴之致命毒蜥 9763474 is the generic Link-2 ladder
- Bystials 德鲁伊鳞虫 6637331, 玛格巨龙 33854624, 巴尔德鸟龙兽 72656408 Summon themselves by banishing a LIGHT/DARK from either grave, your LIGHT Pawns are fuel
- 电脑网挖矿 57160136 searches any Level 4 or lower Cyberse for a discard, 星球改造 73628505 searches the field spell
- TB-11 57111661 Special Summons a 码丽丝 monster from deck, or a 码丽丝 Link from the Extra Deck if the opponent controls 3 or more cards, the turn-2 push tool
- 炽魂代码人 74652966 in some lists is a free body with a 码丽丝 Link on field and later banishes itself from grave on the opponent's turn for a Link-3+ Cyberse Summon

- **Halt Points**

- 增殖的G 23434538 and 欢聚友伴·茸茸长尾山雀 42141493: the full combo Special Summons over ten times, stop at 红棋勒索 68059897 plus field spell plus one Set trap, or resolve 次元吸引者 91800273 first to blank both draws and grave synergy
- 小丑与锁鸟 94145021 stops the add-to-hand searches, sequence MTP-07 94722358 and the 红棋勒索 search before starting the Summon loop if Droll is live
- 原始生命态尼比鲁 27204311: keep Summons below five before the board has a negate, the Link-only lock makes non-Link recovery impossible after a Pawn self-Summon
- 灰流丽 14558127 hits MTP-07 (deck add) and TB-11 57111661 (deck Summon), but 睡鼠① deck banish, 白兔① deck Set and the GWC-06 20726052 grave Summon are not Ash-able
- 古遗物圣枪 34267821 locks banishing and hurts the whole engine, opponent Bystials and 墓穴的指名者 24224830 remove grave Pawns that GWC-06 wants to recover
- 次元障壁 83326048 is your own side-deck answer to other Link strategies, 灵王的波动 40366667 is the main-deck trap handtrap that stops Special Summon effects

- **Mirror Match: 码丽丝 vs 码丽丝**

- The player who resolves the engine first wins, 白棋捆绑 95454996① banishing both graves strips the opponent's used traps and their +3000 ATK boost
- 镜中奇像 93453053 negates the opponent's 白兔 69272449 or 红心加密 21848500 by banishing your own Pawn, which then Summons itself back, a free negate
- 梦游地下界 68337209③ forces attacks into your Links, keep Pawns in pointed zones for the protective clauses: 白兔 no battle damage, 睡鼠 32061192 effect-indestructible, 柴郡猫 96676583 battle-banish, 三月兔 20938824 target protection
- 次元吸引者 91800273 is asymmetric in your favor because the engine plays from banished, the mirror often comes down to resolving it first
- Do not give away banished 码丽丝 Traps without need, the field spell boost needs three different ones and 红心加密 21848500 needs a banished 码丽丝 card to recycle for its Quick Effect

- **Common Mistakes**

- Activate 柴郡猫① with no 码丽丝 card in hand, the effect does nothing and the Pawn can only Summon itself when it is the banished card
- Start non-Link Extra Deck plays after a Pawn self-Summon, the Link-only lock then blocks 电子界无效亚龙 92422871 (Fusion), 分体论聚合员 9940036 (Rank 9 Xyz) and 谜式密码大师 72444406 (Synchro) techs
- Expect 白兔① to Set a second trap from a re-Summoned 白兔, its trap-Set is once per turn and cannot Set a trap name already in your grave
- Plan around TB-11 57111661's Summoned monster, it cannot attack and its effects are negated, it is a body only
- Forget that 白棋捆绑① is how the used traps reach banished, without three different banished 码丽丝 Traps 梦游地下界 68337209 gives no +3000 ATK
- Use 红心加密① with no banished 码丽丝 card available, the return-to-deck is the cost of the banish
- Leave 红心加密 with no monster in its pointed zone, its Quick Effect becomes negatable
- Over-extend into 增殖的G 23434538 or 原始生命态尼比鲁 27204311, the deck can stop at 红棋勒索 68059897 plus field spell plus a Set trap
- Banish 三月兔 20938824 expecting a body, it recycles to hand instead and only Summons itself through its hand Quick Effect
- Set MTP-07 94722358 as the one trap and never Set GWC-06 20726052 or TB-11 57111661, each has a different recovery role in the next turn

- **Build Quirks (this cdb)**

- Chinese naming is 码丽丝, not 玛尔丽丝, setcode 447 (0x1BF), card names use 码丽丝<兵卒>/<代码>/<王后> brackets
- Duplicate unscripted cdb entries exist for 梦游地下界 68337210 and 白兔 69272450 with identical text, always play the scripted 68337209 and 69272449
- In this cdb 红棋勒索 68059897 and 白棋捆绑 95454996 have Link rating 3 in datas despite printing 2+ monsters as materials, so the engine demands 3+ monsters, official TCG/OCG prints of these two are Link-2, expect divergence outside this cdb
- 红心加密 21848500 needs exactly 3 monsters including a 码丽丝, matching both cdb and official text
- No Wicckid or Backup Ignister exists in this cdb, substitute 盛悴之致命毒蜥 9763474 and 飞溅闪屏法师 59859086 in the ladder
- Early lists play 睡鼠 x3, 白兔 x3, 柴郡猫 x2, 封印之黄金柜 75500286 x2-3 without 三月兔 20938824, 三月兔 x3 arrives in later lists
- 次元吸引者 91800273 is main-decked at two in early lists, 灵王的波动 40366667 is the trap handtrap, 次元障壁 83326048 sits in the side
- Custom-server variants like 260228码丽丝巳剑@火灵天星 use cards not present in this cdb and are out of scope for this experience file
