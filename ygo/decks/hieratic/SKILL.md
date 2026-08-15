---
name: hieratic-experience
description: 圣刻 (Hieratic) deck experience: dragon tribute engine, 泰芙龙 opener, 阿图姆 to 塞特龙 line, 九神龙 and 圣刻天龙 finish, extenders, halt points
---
# 圣刻 (Hieratic) Deck Experience

- **Deck Identity**

- 圣刻 (Hieratic, setcode 0x69) is a LIGHT Dragon tribute-engine deck: released 圣刻 dragons convert into free Dragon Normal monsters that become Xyz material
- Main monsters: 圣刻龙-泰芙龙 77901552, 圣刻龙-舒龙 3300267, 圣刻龙-奈芙龙 31516413, 圣刻龙-艾西龙 4022819, 圣刻龙-奥西龙 30794966, 圣刻龙-塞特龙 66789970, 圣刻龙-半龙努特 41639001, 圣刻龙-半龙盖布 78033100
- The engine's Normal monsters: 神龙之圣刻印 13140300 (Level 8) and 龙王之圣刻印 64514622 (Level 6 DUAL), plus generic 紫翠玉龙 43096270 (Level 4) and 拉长石龙 62514770 (Level 6 Tuner)
- Extra deck core: 圣刻龙王-阿图姆龙王 27337596 (Rank 6 tutor), 圣刻神龙-九神龙 64332231 (Rank 8 pop), 圣刻天龙-九神龙 3292267 (Rank 8 negate, custom to this DB), 天球之圣刻印 24361622 (Link-2)
- Spells and traps: 召集之圣刻印 25377819, 超力之圣刻印 51365514, 创造之圣刻印 39680372, 反射之圣刻印 47360060, 抹杀之圣刻印 11975962, 复活之圣刻印 53670497
- Build quirk: reference deck 201205圣刻 is a pure 2012 build with 无底的落穴 69599136 and 次元幽闭 70342110, extra only 2x 阿图姆 27337596 plus 2x 九神龙 64332231
- Build quirk: reference deck 210717圣刻 modernizes with 超再生能力 27770341, 战线复归 59919307, 塞特龙 66789970, 龙王之圣刻印 64514622, a Normal Dragon toolbox and a toolbox extra including 真红眼暗钢龙 88264978, 暗钢龙 暗钢 79266769, 龙魔人 龙骑士女王 90726340, 迅雷之骑士 盖亚龙骑士 91949988, 天霆号 阿宙斯 90448279, 混沌之战士 49202162 and synchros

- **Core Mechanic: Dragon Tribute Engine**

- Every 圣刻龙 (泰芙龙 77901552, 舒龙 3300267, 奈芙龙 31516413, 艾西龙 4022819, 盖布 78033100) has a mandatory EVENT_RELEASE trigger: when released, Special Summon 1 Dragon Normal Monster from hand, deck or GY with 0 ATK/DEF, verified in scripts as TRIGGER_F with location 0x13
- 舒龙 3300267 and 奈芙龙 31516413 are the tribute outlet: each Special Summons itself from hand by releasing 1 圣刻 monster you control, so releasing 泰芙龙 77901552 puts both the outlet and a free Normal on the board
- Pick the Normal deliberately: 龙王之圣刻印 64514622 (Level 6) feeds 阿图姆 27337596, 神龙之圣刻印 13140300 (Level 8) feeds 九神龙 64332231 or 圣刻天龙 3292267
- 泰芙龙 77901552 opens the engine: it Special Summons itself from hand when you control no monsters and the opponent controls at least one, but cannot attack that turn
- 艾西龙 4022819 can be Normal Summoned without tribute (base ATK becomes 1000), and its once-per-turn effect makes every face-up 圣刻 the same Level as a targeted face-up Dragon Normal — the Rank 8 enabler
- 塞特龙 66789970 (banish 3 Dragon Normals from GY to summon itself, then banish 1 Dragon from GY to destroy 1 card) and 奥西龙 30794966 (banish 1 LIGHT Dragon plus 1 Dragon Normal from GY, destruction-replacement tribute) recycle the engine from the GY
- 半龙努特 41639001 and 半龙盖布 78033100 are the Level 4 pair: 努特 Special Summons a Dragon Normal whenever any effect targets it, 盖布 summons one on battle destroy and its release trigger fetches a 圣刻 Normal specifically
- 龙王之圣刻印 64514622 is a DUAL monster: treated as Normal while on field, and after a second Normal Summon it can release itself to Special Summon any other 圣刻 from hand, deck or GY

- **One-Card Combo**

- Hieratic has no true one-card line: the baseline opener is 泰芙龙 77901552 plus one partner, 舒龙 3300267 or 奈芙龙 31516413 in hand, or 召集之圣刻印 25377819 to search the partner
- Step 1: Special Summon 泰芙龙 77901552 from hand (your field empty, opponent controls a monster)
- Step 2: Special Summon 舒龙 3300267 from hand by releasing 泰芙龙, then 泰芙龙's trigger Special Summons 龙王之圣刻印 64514622 from the deck with 0 ATK/DEF
- Step 3: Xyz Summon 圣刻龙王-阿图姆龙王 27337596 with 舒龙 and 龙王之圣刻印 (two Level 6 Dragons)
- Step 4: 阿图姆 detaches 1 material to Special Summon 圣刻龙-塞特龙 66789970 from the deck with 0 ATK/DEF, and cannot attack this turn
- Step 5: end on 阿图姆 27337596 plus 塞特龙 66789970, with 塞特龙 able to banish a GY Dragon and destroy 1 card each turn
- The 奈芙龙 31516413 variant destroys monsters instead of backrow and stays Level 5, so it cannot make 阿图姆 directly — use 舒龙 3300267 when the plan is Rank 6

- **End Field**

- Standard end field: 阿图姆 27337596 (2400) plus 塞特龙 66789970 (2800), 5200 damage and one pop per turn from 塞特龙
- With 创造之圣刻印 39680372: overlay 阿图姆 27337596 into 圣刻神龙-九神龙 64332231, which releases any number of monsters from hand or field to destroy the same number of cards
- Or overlay 阿图姆 27337596 into 圣刻天龙-九神龙 3292267, which on the opponent's turn negates and destroys any targeting effect aimed at your field, GY or banished cards
- A second Rank 8: 塞特龙 66789970 plus 神龙之圣刻印 13140300, or 艾西龙 4022819's level-fix making 舒龙 3300267 and itself Level 8
- 天球之圣刻印 24361622 on field: during the opponent's turn, release a monster to return 1 face-up card to hand, then its own trigger Special Summons any Dragon from hand or deck with 0 ATK/DEF
- 真红眼暗钢龙 88264978: banishes 1 face-up Dragon to Special Summon itself, then revives 1 Dragon from hand or GY — a 2800 beater that extends into the next turn
- 天霆号 阿宙斯 90448279: Xyz onto an Xyz that battled this turn, then detach 2 to send every other card on the field to the GY
- Backrow: 反射之圣刻印 47360060 counter, 抹杀之圣刻印 11975962 quick-play banish, 复活之圣刻印 53670497 mill and revive

- **Extenders**

- 召集之圣刻印 25377819: add any 圣刻 monster from deck to hand
- 超力之圣刻印 51365514: Special Summon 1 圣刻 monster from hand
- 创造之圣刻印 39680372: effect one overlays a different 圣刻 Xyz onto a Dragon Xyz you control (阿图姆 27337596 into 九神龙 64332231 or 圣刻天龙 3292267), effect two banishes itself from the GY to Special Summon a 圣刻 from the GY in defense
- 真红眼暗钢龙 88264978: banishes a face-up Dragon to Special Summon itself, then revives 1 Dragon from hand or GY
- 天球之圣刻印 24361622: Link-2 from any 2 Dragons such as 泰芙龙 77901552 and 紫翠玉龙 43096270
- 龙魔人 龙骑士女王 90726340: Rank 4 from 半龙努特 41639001 and 半龙盖布 78033100, detach to revive a Level 5 or higher Dragon from the GY (negated, cannot attack)
- 迅雷之骑士 盖亚龙骑士 91949988: overlays onto a Rank 5 or 6 Xyz such as 阿图姆 27337596 for piercing 2600 ATK
- 复活之圣刻印 53670497: on the opponent's turn mills a 圣刻 to fuel 塞特龙 66789970 and 奥西龙 30794966, on your turn returns a banished 圣刻 to the GY, and when destroyed Special Summons a 圣刻 from the GY
- 超再生能力 27770341: activate alongside tribute plays to draw one card per Dragon released or discarded that turn at the End Phase
- 战线复归 59919307: revive any monster from your GY in defense position
- 暗钢龙 暗钢 79266769: Link monster needing 2+ effect monsters sharing race and attribute, once per turn revives a monster from your GY or banished zone to its linked zone (negated, bottom of deck when it leaves), and locks you out of Link Summons for the rest of the turn

- **Halt Points**

- 灰流丽 on 召集之圣刻印 25377819, 超力之圣刻印 51365514, the release-trigger Normal summons, or 阿图姆 27337596's deck tutor each ends the line
- 无限泡影 and 效果遮蒙者 on 阿图姆 27337596 stop the 塞特龙 66789970 tutor
- 增殖的G: the standard line Special Summons 4 to 6 times
- 尼比鲁: 5 summons are reachable in the standard opener
- Grave hate such as 次元吸引者 and 墓穴指名者 denies 塞特龙 66789970, 奥西龙 30794966 and 真红眼暗钢龙 88264978 their GY Dragon fuel
- Negating 复活之圣刻印 53670497's mill or 超再生能力 27770341's draw keeps the deck from re-fueling

- **Mirror Match**

- The race is 阿图姆 27337596 into 塞特龙 66789970: whoever resolves the tutor first usually wins
- 抹杀之圣刻印 11975962 banishes the opponent's 龙王之圣刻印 64514622 or 神龙之圣刻印 13140300 before they become Xyz material
- 反射之圣刻印 47360060 negates the opponent's 召集之圣刻印 25377819, 超力之圣刻印 51365514 or 创造之圣刻印 39680372 activations
- 圣刻天龙-九神龙 3292267 dominates the mirror: it negates targeting effects such as the opponent's 抹杀之圣刻印 11975962, 塞特龙 66789970 pop and 天球之圣刻印 24361622 bounce
- 创造之圣刻印 39680372 decides the mirror: the first player to overlay 阿图姆 27337596 into 圣刻天龙 3292267 or 九神龙 64332231 controls the board
- 艾西龙 4022819's level-fix changes every face-up 圣刻 on both fields, so it can accidentally hand the opponent the Level 8 they need
- 半龙努特 41639001 triggers on any targeting including the opponent's, so use non-targeting removal such as 九神龙 64332231 pops in the mirror

- **Common Mistakes**

- 泰芙龙 77901552 cannot attack the turn it Special Summons itself — do not count its damage
- 阿图姆 27337596 cannot attack after using its tutor effect — attack first or accept the lock
- Release-trigger summons are mandatory and need a free monster zone — a full field makes them fizzle
- Always pick the Normal the line needs: 龙王之圣刻印 64514622 for 阿图姆 27337596, 神龙之圣刻印 13140300 for Rank 8
- 龙王之圣刻印 64514622 is DUAL: on the field it is a Normal monster and its summoning effect requires the second Normal Summon
- 塞特龙 66789970 and 奥西龙 30794966 need Dragon Normal fuel in the GY — mill with 复活之圣刻印 53670497 on the opponent's turn first
- 创造之圣刻印 39680372 effect one targets only Dragon Xyz monsters, not 天球之圣刻印 24361622 or other Links, and effect two banishes itself so use effect one before treating it as GY fodder
- 天球之圣刻印 24361622's bounce works only during the opponent's turn and only from the Extra Monster Zone
- 暗钢龙 暗钢 79266769 locks you out of Link Summons after its effect — make your Links first
- 超再生能力 27770341 draws at the End Phase — activate it with your tribute plays, not after them
- 反射之圣刻印 47360060 is a Counter Trap with a tribute cost — keep a spare 圣刻 if the Xyz still needs material
- 舒龙 3300267 and 奈芙龙 31516413 removal can release a 圣刻 from the hand: 舒龙 on field plus 泰芙龙 77901552 in hand pops a backrow and still triggers 泰芙龙's summon
- 半龙努特 41639001's trigger has no controller check in the script, so your own targeting effects also trigger it — 天球之圣刻印 24361622 can bounce your own 努特 for a free Dragon Normal
