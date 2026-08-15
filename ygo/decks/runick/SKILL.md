---
name: runick-experience
description: 神碑 (Runick) deck experience: Fountain quick-play engine, deck-out win condition, stun pieces
---
# 神碑 (Runick) Deck Experience

- **Deck Identity**

- Main deck is almost all spells: eight different Runick quick-play spells plus the field spell 神碑之泉 92107604 and the continuous spell 神碑的欺诳 29595202, supported by generic floodgates and draw spells
- All Runick monsters are FUSION-type monsters living only in the Extra Deck, the deck runs zero main-deck Runick monsters, verified as type 97 with setcode 383 (0x17f) in cards.cdb
- Win condition is deck-out: every quick-play activation banishes 1 to 4 cards from the top of the opponent deck while floodgates stop the opponent from playing
- The deck never attacks: every quick-play activation makes YOU skip your next Battle Phase, verified as EFFECT_SKIP_BP with player target set to yourself in every quick-play script
- Pure stun build seen in 240928神碑 and 250726神碑 lists: 神碑之泉 92107604, 神碑的欺诳 29595202, all eight quick-plays, plus 神碑之翼 胡基 55990317 / 神碑之翼 穆宁 92385016 / 神碑之牙 格利 28373620 / 神碑之牙 弗利基 47219274 / 神碑之鬣 史莱普尼尔 74659582 in the Extra Deck

- **Core Mechanic: Fountain Quick-Play Engine**

- 神碑之泉 92107604 effect 1: while face-up in the field zone, you can activate Runick quick-play spells from hand during the opponent turn, the signature mechanic that turns every Runick spell into a hand trap
- 神碑之泉 92107604 effect 2: once per turn, when you activate a Runick quick-play (either of its two effects), target up to 3 Runick quick-plays in your GY, return them to the bottom of the deck in any order, then draw cards equal to the number returned, verified in script c92107604.lua as a chain trigger on EVENT_CHAINING
- The just-activated quick-play is still on the field when the Fountain trigger fires, so the recycled targets must be quick-plays already in the GY from earlier activations, sequence activations accordingly
- Every Runick quick-play has two activation effects sharing one once-per-turn oath limit: option A is a disruption effect that also banishes the opponent deck top, option B special summons 1 Runick monster from the Extra Deck to the Extra Monster Zone
- Option B needs a free Extra Monster Zone or a zone a Link monster points to, so typically only one Runick monster is on the field at a time, verified via GetLocationCountFromEx with the extra zone flag in every quick-play script
- 神碑的欺诳 29595202: forced trigger that banishes 1 card from the opponent deck top whenever ANY player activates a quick-play, including your own Runick plays and the opponent quick-plays, verified in c29595202.lua with no player check

- **One-Card Combo: 神碑的锋芒**

- Starter: 神碑的锋芒 31562086 in hand, no other cards needed
- Step 1: activate 神碑的锋芒 31562086 with option B, special summon 神碑之翼 胡基 55990317 from the Extra Deck to the Extra Monster Zone
- Step 2: 胡基 55990317 trigger on being summoned from the Extra Deck, discard 1 card as cost, add 神碑之泉 92107604 from deck to hand
- Step 3: activate 神碑之泉 92107604, the engine is now live for the opponent turn
- Step 4: every additional Runick quick-play in hand becomes chainable disruption plus 1 to 4 deck banishes, and the Fountain recycles and draws once per turn
- Halt point: Ash Blossom on the 神碑的锋芒 search or on 胡基 search stops the line, no discardable card in hand blocks 胡基 effect
- Alternative opener: 星球改造 73628505 alone adds 神碑之泉 92107604 directly, but leaves no monster on the field

- **End Field One-Card**

- 神碑之泉 92107604 face up plus 神碑之翼 胡基 55990317 in the Extra Monster Zone
- 胡基 55990317 protection: banishes itself to prevent any other card you control from being destroyed by card effect, making it the Fountain guardian
- The skipped Battle Phase means no attacks, the board holds via floodgates while the quick-plays mill on the opponent turn
- Halt point: 神碑之泉 destroyed without backup means no hand quick-play activations on the opponent turn, the whole engine halves

- **Extender: 星球改造 73628505**

- Adds any field spell from the deck, that is 神碑之泉 92107604, the fastest way to put the engine online without spending a quick-play activation

- **Extender: 神碑之翼 穆宁 92385016**

- On being summoned from the Extra Deck, discard 1 card to add 神碑的欺诳 29595202 from deck to hand
- 神碑的欺诳 29595202 mills 1 extra card whenever anyone activates a quick-play, stacking with every Runick spell you chain
- 穆宁 92385016 quick effect: banishes itself to negate and destroy any opponent effect that targets your Runick card or face-down card, end phase recovers 1000 LP

- **Extender: 神碑之牙 格利 28373620**

- On being summoned from the Extra Deck, add 1 non-quick-play Runick spell from your GY to hand, recycling 神碑之泉 92107604 or 神碑的欺诳 29595202
- Indestructible by card effects, on battle destruction destroys 1 card on the field

- **Extender: 神碑之牙 弗利基 47219274**

- While in the Extra Monster Zone, when it battles banish 2 cards from the opponent deck top, all battle damage from its battles becomes 0
- On being destroyed, add 1 Runick quick-play from GY to hand, the recovery half of the engine

- **Extender: 神碑之鬣 史莱普尼尔 74659582**

- Quick effect during your Main Phase or the opponent Battle Phase: banish 1 face-up opponent monster and itself until the End Phase, temporary removal that also frees the Extra Monster Zone
- When the opponent adds a card from the deck to hand, special summon a 神碑衍生物 74659583 token with 1500 ATK and DEF as a blocker

- **Floodgate Suite (no Runick trap exists in this card DB, the stun pieces are generic)**

- 技能抽取 82732705, 千查万别 24207889, 群雄割据 90846359, 御前试合 53334471, 召唤限制器 23516703, 次元的裂缝 81674782, 超古代生物的墓场 83266092, 灵魂抽取 73599290, 和平使者 44656491, 同调区域 60306277
- Monster floodgates: 天岩户 32181268, 冲浪检察官 15397015, 化石恐龙 肿头龙 42009836, they shut down the opponent while the mill engine runs

- **Halt Points**

- 神碑之泉 92107604 destroyed: no hand quick-plays on the opponent turn and no recycle draw, recover with 星球改造 73628505 or 多元宇宙 885016
- Ash Blossom on 神碑的锋芒 31562086 search, 胡基 55990317 search, or 星球改造 73628505 stops the opening line
- 技能抽取 82732705 negates your own Runick monster effects on the field, so Sleipnir banish and Hugin search stop working under your own floodgate while the spell engine is unaffected
- 次元吸引者 91800273 conflicts with the Fountain recycle, quick-plays get banished instead of reaching the GY, do not activate it on a turn you rely on Fountain effect 2
- 微睡的神碑 67835547 gives the target one indestructibility, do not target a monster you plan to destroy with 辉耀之炎的神碑 68957034
- 解咒的神碑 66712905 option A only triggers when the opponent adds from the deck to hand outside the Draw Phase, do not hold it expecting a free chain disruption
- Only one Runick monster fits the Extra Monster Zone, sequence your option B summons or use Sleipnir self-banish to free the zone

- **Mirror Match: 神碑 vs 神碑**

- The duel becomes a mill race, whoever keeps 神碑之泉 92107604 alive and mills faster wins
- 解咒的神碑 66712905 punishes opponent searches, chain it to their 神碑的锋芒 31562086 or 胡基 55990317 searches for a random hand discard
- 破坏的神碑 94445733 removes their 神碑之泉 92107604 or 神碑的欺诳 29595202, the fastest way to win the race
- 神碑的欺诳 29595202 mills the opponent on every quick-play activation by either side, an advantage that snowballs in the mirror
- 辉耀之炎的神碑 68957034 destroys their special summoned Runick monster, 冰冻诅咒的神碑 30430448 negates their monster, 微睡的神碑 67835547 stops their monster from attacking

- **Common Mistakes**

- Never attempt to attack, every quick-play activation skips your next Battle Phase, the deck wins by deck-out not damage
- Do not waste the once-per-turn activation on the wrong option, option B summons a monster, option A does the disruption and milling
- The just-activated quick-play cannot be recycled by the same Fountain trigger, order activations so the recycle happens after earlier quick-plays reach the GY
- 微睡的神碑 67835547 makes the target indestructible once, never target the monster you are about to destroy
- 解咒的神碑 66712905 is not a general purpose quick-play, its disruption effect only fires on opponent deck-to-hand adds
- 神碑的锋芒 31562086 can search any Runick card except itself, usually search 神碑之泉 92107604 first
- 金满而谦虚之壶 84211599 and 强欲而金满之壶 49238328 block card-effect draws for the turn, so Fountain effect 2 draw fails after them
- 削命的宝札 59750328 forbids special summons for the turn, which blocks option B monster summoning
- Under your own 技能抽取 82732705 the Runick monsters lose their effects, plan around Sleipnir and Hugin being dead while the floodgate is up
- 次元吸引者 91800273 kills your own Fountain recycling, only activate it when the GY loop does not matter this turn
