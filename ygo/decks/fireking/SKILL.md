---
name: fireking-experience
description: 炎王 (Fire King) deck experience: destroy-and-revive engine, one-card baseline, two-card full line, extenders, halt points, mirror
---
# 炎王 (Fire King) Deck Experience

- **Deck Identity**

- FIRE Beast / Beast-Warrior / Winged-Beast (鸟兽族) archetype, setcode 0x81, with the 炎王兽 sub-archetype at setcode 0x1081; every 炎王 monster is FIRE attribute
- Modern pure build (reference deck/240727炎王): 3x 炎王妃 火神不死鸟 44455560, 3x 真炎王 凤凰不死鸟 90681088, 3x 圣炎王 大鹏不死鸟 66431519, 1-3x 炎王神兽 麒麟 2526224, 1-3x 炎王兽 甘尼许 18621798, 1-3x 炎王兽 巴隆 69000994, 1x 炎王神兽 大鹏不死鸟 23015896
- Spell engine: field spells 炎王的孤岛 57554544 and 炎王的圣域 65305978, quick-play 炎王神天烧 91703676 and 炎王炎环 59388357, normal spell 炎王的急袭 22993208, trap 炎王的结袭 38798785
- Extra deck core: 炎王神 大鹏不死鸟·永炎 64182380, 赐炎之咎姬 2772337, 灼热之火灵使 希塔 48815792, 转生炎兽 日光狼 87871125, 转生炎兽 烈火凤凰 57134592, 登陆群舰 游走巨鲸 20665527, S：P小夜骑士 29301450, 灾厄之星 提·丰 93039339, 天霆号 阿宙斯 90448279, I：P百变莱娜 65741786, 解码语者·炽热之魂 61245672
- Staple handtraps in the build: 灰流丽 14558127, 增殖的G 23434538, 墓穴的指名者 24224830, 抹杀之指名者 65681983, 无限泡影 10045474, 效果遮蒙者 97268402, 原始生命态 尼比鲁 27204311, 三战之才 25311006, 欢聚友伴·茸茸长尾山雀 42141493
- Card name map: 火神不死鸟 = Ulcanix, 凤凰不死鸟 = Ponix, 圣炎王 = Sacred Fire King Garunix, 炎王神兽 麒麟 = High Avatar Kirin, 永炎 = Garunix Eternity, 甘尼许 = Arvata, 巴隆 = Barong, 游走巨鲸 = Amblowhale, 天烧 = Sky Burn

- **Core Mechanic: The Destroy-and-Revive Engine**

- The deck wins by destroying its own original-FIRE monsters by effect and converting every destruction into summons, searches and field wipes
- Hand floaters: when a face-up 炎王 you control is destroyed by effect, 炎王兽 巴隆 69000994, 炎王兽 大鹏不死鸟 54149433, 炎王兽 麒麟 96594609, 炎王兽 夜叉 66413481 and 炎王兽 哈奴曼 38910263 each special summon themselves from hand, so multiple copies of the same floater can all appear off one destruction
- Hand-or-field floaters: 真炎王 凤凰不死鸟 90681088 and 圣炎王 大鹏不死鸟 66431519 also trigger when the destroyed FIRE monster came from the hand, verified in c90681088.lua and c66431519.lua filters accepting previous location hand or monster zone
- Destroyed-monster grave floats: 炎王妃 火神不死鸟 44455560 revives 炎王神兽 大鹏不死鸟 23015896 from deck, 炎王兽 甘尼许 18621798 revives a Beast/Beast-Warrior/Winged-Beast FIRE from grave (negated, destroyed end phase), 炎王神兽 麒麟 2526224 revives any 炎王 from hand or grave then pops one card, 炎王兽 麒麟 96594609 mills one FIRE from deck
- The wipe layer: 炎王神兽 大鹏不死鸟 23015896 destroyed by effect revives at the next standby and destroys all other monsters, 炎王神 大鹏不死鸟·永炎 64182380 destroys all other monsters on Xyz summon, and 炎王神天烧 91703676 destroys equal numbers of your 炎王 and opponent cards as a quick-play
- 炎王的孤岛 57554544 ① destroys one monster from hand or field to search any 炎王 monster, ② special summons a FIRE Winged-Beast from hand when your field is empty, ③ destroys all your monsters if the face-up field spell is sent to grave or banished
- 炎王的圣域 65305978 ① places 炎王的孤岛 57554544 from deck at activation, ② replaces destruction of your field-zone card with destroying one face-up FIRE from hand or field (which itself feeds the float engine), ③ quick Xyz summons a FIRE Xyz monster using only your 炎王 monsters when the opponent special summons
- 炎王神天烧 91703676 banishes itself from grave as a replacement when a face-up 炎王 would be destroyed by effect, a one-shot destruction shield

- **One-Card Combo: 真炎王 凤凰不死鸟 90681088**

- The only true one-card starter in the deck: 凤凰不死鸟 (Ponix) alone ends on the negate plus the full field-spell engine
- Step 1: normal summon 真炎王 凤凰不死鸟 90681088, activate its ② to add 炎王的圣域 65305978 from deck to hand
- Step 2: activate 炎王的圣域 65305978, its ① places 炎王的孤岛 57554544 from deck face-up, a placement that 灰流丽 14558127 cannot negate because it is not an add-to-hand, summon or mill
- Step 3: activate 炎王的孤岛 57554544 ① to destroy 凤凰不死鸟 on the field, search 炎王兽 甘尼许 18621798; the destroyed 凤凰不死鸟 ③ re-adds itself from grave at your next standby, starting the recursion loop
- Step 4: normal summon 炎王兽 甘尼许 18621798, its ① stands ready to negate a monster effect by destroying one other face-up FIRE from hand or field
- End field one card: 甘尼许 18621798 negate plus 炎王的圣域 65305978 plus 炎王的孤岛 57554544 plus 凤凰不死鸟 recursion next standby
- Halt point: 灰流丽 14558127 on the 凤凰不死鸟 search or on the 孤岛 search stops the engine at one card, 无限泡影 10045474 or 效果遮蒙者 97268402 on the normal summon leaves an empty board

- **Standard Two-Card Combo: 炎王妃 火神不死鸟 44455560 + any FIRE**

- The full line needs a second FIRE to destroy, any hand FIRE such as 炎王兽 麒麟 96594609, 灰流丽 14558127 or another 炎王 works
- Step 1: normal summon 炎王妃 火神不死鸟 44455560, activate ① to destroy the second FIRE from hand and search 真炎王 凤凰不死鸟 90681088 from deck
- Step 2: the destroyed 炎王兽 麒麟 96594609 mills 圣炎王 大鹏不死鸟 66431519 from deck to grave, 凤凰不死鸟 90681088 special summons itself from hand and searches 炎王的圣域 65305978
- Step 3: activate 炎王的圣域 65305978 to place 炎王的孤岛 57554544, then 孤岛 ① destroys 火神不死鸟 on the field to search 圣炎王 大鹏不死鸟 66431519
- Step 4: the destroyed 火神不死鸟 ② revives 炎王神兽 大鹏不死鸟 23015896 from deck in defense, and 圣炎王 66431519 special summons itself from hand
- Step 5: 圣炎王 66431519 ② destroys 炎王神兽 麒麟 2526224 from deck to gain 1200 ATK, then 麒麟 ② revives 火神不死鸟 44455560 from grave and can pop one card
- Step 6: overlay 圣炎王 66431519 and 炎王神兽 大鹏不死鸟 23015896 (both Level 8) into 炎王神 大鹏不死鸟·永炎 64182380, its ① destroys all other monsters, and a destroyed 火神不死鸟 44455560 can float another 大鹏不死鸟 23015896 from deck when a second copy is still in the deck
- Alternative finish: link 火神不死鸟 44455560 with the spare body into 赐炎之咎姬 2772337, revive a FIRE from grave, then climb to 登陆群舰 游走巨鲸 20665527 for the Amblowhale endboard, a line verified against the Master Duel Meta Fire King combo guide
- This full line special summons five or more times, 原始生命态 尼比鲁 27204311 is live against it, prefer the short line when Nibiru is a threat

- **End Field**

- 炎王神 大鹏不死鸟·永炎 64182380 with materials: 3000 ATK, board wipe on Xyz summon, detach one material to destroy one spell or trap and gain 500 ATK, and if destroyed while holding materials revives up to that many 炎王 monsters from grave
- Second body: 圣炎王 大鹏不死鸟 66431519 as a 2700+ beater or 炎王神兽 大鹏不死鸟 23015896 as a defense wall threatening the standby wipe
- Both 炎王的圣域 65305978 and 炎王的孤岛 57554544 face-up, 圣域 ② protects the field spell through the float engine and 圣域 ③ quick Xyz summons 永炎 64182380 on the opponent turn when they special summon
- One set 炎王神天烧 91703676 as the quick-play wipe plus its grave destruction shield
- 炎王兽 甘尼许 18621798 on field as the monster-effect negate
- Amblowhale variant endboard: 登陆群舰 游走巨鲸 20665527 (attack grows with the link monsters in both graves) plus 炎王的圣域 65305978 and 炎王的孤岛 57554544, with 炎王神兽 麒麟 2526224 kept in hand for its quick effect on the opponent turn
- 赐炎之咎姬 2772337 in grave is a defensive extender: when the opponent special summons it destroys one face-up FIRE you control and one opponent monster, then revives itself

- **Extenders**

- 炎王神兽 麒麟 2526224: quick effect during main phases, destroy one other face-up FIRE from hand or field to special summon itself as a Level 8 body for 炎王神 大鹏不死鸟·永炎 64182380
- 炎王炎环 59388357: quick-play, destroy one face-up FIRE you control to special summon one FIRE from grave, a cheap mid-chain floater trigger plus revival
- 炎王的急袭 22993208: normal spell, only while the opponent controls a monster and you control none, special summons one Beast/Beast-Warrior/Winged-Beast FIRE from deck (negated, destroyed end phase)
- 炎王的结袭 38798785: trap, special summons one monster each from hand, deck and grave with one of each of the three races, all negated and destroyed end phase, then banishes itself from grave to make your 炎王 summons unanswerable this turn
- 一对一 2295440: discard one monster to special summon 真炎王 凤凰不死鸟 90681088 from deck, the Level 1 Ponix is a valid target
- 炎王兽 巴隆 69000994: after being destroyed by effect it searches any 炎王 card at your next standby, a slow mid-game engine refill
- 炎王兽 夜叉 66413481: when destroyed it destroys one card in your own hand or field, a deliberate self-destruction tool to fire your own floaters
- 灼热之火灵使 希塔 48815792: link 2 that special summons a FIRE monster from the opponent grave to a zone it points to, and searches a FIRE monster with 1500 or less defense if destroyed
- 转生炎兽 日光狼 87871125: link 2 that adds one FIRE monster from grave to hand when a FIRE is summoned to its pointed zone, but locks that monster name from being summoned this turn
- 解码语者·炽热之魂 61245672: link 3 that draws on demand, an option to convert a safe board into hand advantage

- **Halt Points**

- 灰流丽 14558127 hits every deck search: 火神不死鸟 44455560 ①, 凤凰不死鸟 90681088 ②, 孤岛 57554544 ①, and the 麒麟 96594609 ② mill, stopping the engine at its first search
- 灰流丽 14558127 cannot negate 炎王的圣域 65305978 placing 炎王的孤岛 57554544 from deck, the placement is not an add-to-hand, summon or mill
- 无限泡影 10045474, 效果遮蒙者 97268402 and 灵王的波动 40366667 on 火神不死鸟 44455560 or 凤凰不死鸟 90681088 before their search resolves ends the line
- 原始生命态 尼比鲁 27204311 on the fifth summon, play the short line (Ponix only or 圣域 plus two Level 8s) when Nibiru is live
- 增殖的G 23434538: the deck special summons constantly, stop after two or three summons and pass on the 甘尼许 18621798 negate plus field spells instead of playing into it
- 墓穴的指名者 24224830 and 抹杀之指名者 65681983 answer 灰流丽 14558127 and 增殖的G 23434538 and are main-deck staples in the pure list
- Field spell chain: 炎王的孤岛 57554544 ③ destroys all your monsters when the face-up field spell leaves the field, trigger 炎王的圣域 65305978 ② first so the destruction feeds the floats instead of killing the board
- Graveyard disruption (深渊之兽 6637331 33854624, D.D.乌鸦 24508238) hurts the grave-revive lines, the main grave dependencies are 巴隆 69000994 standby search and 圣炎王 66431519 grave revival

- **Mirror Match: 炎王 vs 炎王**

- Both sides run the same floaters, never destroy a face-up 炎王 without a plan because the opponent converts every destruction into free summons
- Priority target is the opponent 炎王的圣域 65305978 and 炎王的孤岛 57554544, without the field spell engine the mirror turn halves, use 永炎 64182380 ② to pop the field spell before the wipe
- Watch the standby phase, 炎王神兽 大鹏不死鸟 23015896 revives and wipes, clear the opponent grave copies or hold 炎王神天烧 91703676 to dodge the wipe
- 炎王神天烧 91703676 targets equal numbers of your own 炎王 and opponent cards, in the mirror the self-destruction feeds your floaters so it is rarely a bad trade
- 赐炎之咎姬 2772337 in grave turns every opponent summon into a trade, check who controls the earlier 咎姬 engine before committing the summon chain

- **Common Mistakes**

- Do not destroy your own 炎王的孤岛 57554544 without 炎王的圣域 65305978 ② protection, the ③ wipe destroys the whole board
- 炎王的孤岛 57554544 ① and ② share one use per turn, do not spend ① and expect ② in the same turn
- 炎王神兽 麒麟 2526224 ① only works in main phases, not during the battle or end phase, and its ② optional pop resolves after the revival
- 炎王妃 火神不死鸟 44455560 destroys first then searches, and its ② revives 炎王神兽 大鹏不死鸟 23015896 from deck not grave, sequence the graveyard setup first
- 炎王兽 甘尼许 18621798 ② revives with negated effects and destroys itself at the end phase, treat it as a temporary body and re-destroy it for float value
- Hand floaters 巴隆 69000994, 大鹏不死鸟 54149433, 麒麟 96594609, 夜叉 66413481 and 哈奴曼 38910263 need the destroyed monster face-up on the field, only 凤凰不死鸟 90681088 and 圣炎王 66431519 trigger on hand destruction
- 转生炎兽 日光狼 87871125 locks the name it adds from being summoned this turn, do not return the monster you still need on board
- 炎王神天烧 91703676 grave shield is once per turn, do not plan around two protections
- 炎王的结袭 38798785 monsters are negated and destroyed at the end phase, use them as link or Xyz material immediately or let them die for the floats
- 炎王的圣域 65305978 ③ quick Xyz needs your 炎王 monsters on field and an opponent summon, sequence your turn so at least one 炎王 survives to the opponent turn
