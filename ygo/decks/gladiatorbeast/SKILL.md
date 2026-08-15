---
name: gladiatorbeast-experience
description: 剑斗兽 (Gladiator Beast) deck experience: battle-phase tag-out engine, contact fusion loop, extenders, halt points
---
# 剑斗兽 (Gladiator Beast) Deck Experience

- **Deck Identity**

- Beast / Beast-Warrior / Divine-Beast main deck monsters with a battle-phase swap engine; fusions are contact fusions from the field, no 融合 spell needed
- Main deck core: 师斗 26582143, 女斗 52502677, 骑斗 57731460, 枪斗 41470137, 教斗 2067935, 马斗 25924653, 绳斗 78868776, 双斗 31247589, 罪斗 67385964, 鱼斗 5975022, 奥古斯都 7573135, 维斯帕西亚努斯 88996322
- Extra deck fusions: 凯撒 48156348, 希拉克略 27346636, 尼禄 29357956, 主斗 30864377, 多米提安努斯 33652635, 克劳狄乌斯 48958757, 车斗 73285669, 乔治 90957527, 盲斗 3779662
- Extra deck links: 奴隶豹 66863374, 骏斗 72246674, 德拉伽塞斯 62000467; main deck support: 奴隶虎 92373006
- Key spells and traps: 剑斗训练所 35224440, 剑斗兽的斗技场-弗拉维圆形斗技场 5063379, 再起的剑斗兽 20201255, 团结的剑斗兽 66290900, 剑斗排斥波 93684009, 剑斗兽的战车 96216229, 剑斗海战 52394047, 休息的剑斗兽 98891840, 剑斗归还 24285858
- Near-pure build quirk: 救援猫 14878871 + 师斗 26582143 is the modern starter (救援猫 summons 2 师斗 as link material), with 失X-剑士 招来者 4423206 as a bridge; older builds run 救援兔 85138716, 奴隶虎 92373006, 奴隶豹 66863374

- **Core Mechanic: Battle-Phase Tag-Out**

- Every main deck Gladiator Beast has a trigger at end of battle phase, verified in scripts as EVENT_PHASE+PHASE_BATTLE with GetBattledGroupCount()>0, that shuffles itself into the deck as cost and special summons 1 different Gladiator Beast from deck
- The tag-out is optional and resolves only if the monster actually battled this turn; a monster summoned by a tag-out at end of battle phase cannot attack or tag out again that turn
- Fusions tag out to the EXTRA deck instead of the main deck: 凯撒 48156348 tags out for 2 from deck excluding 枪斗 41470137, 尼禄 29357956 for 2, 多米提安努斯 33652635 for 1, 主斗 30864377 for 1
- On-summon triggers fire only for monsters special summoned by a Gladiator Beast effect, verified in scripts as Auxiliary.gbspcon checking SUMMON_VALUE_GLADIATOR or IsSpecialSummonSetCard 0x1019
- gbspcon fires for tag-out summons, 奴隶虎 92373006 and 奴隶豹 66863374 swaps, 师斗 26582143 self-summon, 再起的剑斗兽 20201255, and 斗技场 5063379 summons, but NOT for 排斥波 93684009 (0x19 setcode, no trigger)
- On-summon effects: 枪斗 41470137 destroys 1 Spell/Trap, 鱼斗 5975022 destroys 1 face-up monster, 骑斗 57731460 adds a Gladiator Beast from grave, 教斗 2067935 banishes 1 from grave and copies its name, 罪斗 67385964 mills 1 from deck, 双斗 31247589 attacks twice, 绳斗 78868776 becomes 2100 ATK, 奥古斯都 7573135 summons 1 from hand in defense that returns to deck at end phase, 维斯帕西亚努斯 88996322 grants +500 ATK to your monsters while it was itself summoned by a Gladiator Beast effect
- Contact fusion: return listed field monsters to deck or extra deck as cost to summon the fusion, verified as aux.AddContactFusionProcedure with ContactFusionSendToDeck
- 团结的剑斗兽 66290900 is the in-battle-phase fusion spell: shuffle materials from hand, field, or grave into the deck, summon 1 Gladiator Beast fusion ignoring conditions, but this turn only Gladiator Beasts may attack

- **One-Card Combo: 救援猫 14878871**

- Step 1: activate 救援猫 14878871, send itself to grave, special summon 2× 师斗 26582143 from deck (Beast Level 3, effects negated, destroyed at end phase)
- Step 2: Xyz summon 失X-剑士 招来者 4423206 on the 2 师斗, detach 1 material to special summon 女斗 52502677 from deck in defense (Beast-Warrior EARTH Level 4)
- Step 3: link summon 奴隶豹 66863374 using 招来者 and 女斗, its first effect adds any 剑斗兽 card from deck such as 团结的剑斗兽 66290900, 剑斗兽的斗技场-弗拉维圆形斗技场 5063379, or 再起的剑斗兽 20201255
- Step 4: 奴隶豹 66863374 second effect returns 女斗 52502677 to the deck and special summons 枪斗 41470137 from deck as a GB-effect summon, 枪斗 destroys 1 Spell/Trap
- Step 5: battle with 枪斗 41470137, at end of battle phase tag it out for 1 Gladiator Beast from deck such as 马斗 25924653 or 骑斗 57731460
- Step 6: in a later battle phase use 团结的剑斗兽 66290900 to contact fuse 凯撒 48156348 with 枪斗 41470137 plus 1 Gladiator Beast from field, hand, or grave, 凯撒 destroys up to 2 cards, attacks, and tags out for 2 Gladiator Beasts from deck excluding 枪斗
- Alternative with 剑斗训练所 35224440: search 师斗 26582143, reveal it plus 1 Gladiator Beast from hand to summon both, then 师斗 searches a 剑斗 spell or trap, then link into 奴隶豹 66863374

- **End Field**

- 凯撒 48156348 on board plus a set 剑斗兽的战车 96216229 from 斗技场 5063379 end phase setup
- 主斗 30864377 with 2 Level 5 or higher Gladiator Beasts as material, first effect can summon any Gladiator Beast fusion ignoring conditions once per turn
- 多米提安努斯 33652635 with 维斯帕西亚努斯 88996322 plus 2 Gladiator Beasts, negate 1 monster effect per turn and redirect opponent attacks to itself
- 克劳狄乌斯 48958757 with 5 Gladiator Beasts from field or grave, next battle phase twice, and its second effect responds to opponent monster effects
- 排斥波 93684009 face up protects your Gladiator Beasts from targeting outside the battle phase, 剑斗兽的战车 96216229 negates monster effects, 剑斗海战 52394047 forces opponent attacks

- **Extenders**

- 剑斗训练所 35224440: add any Level 4 or lower Gladiator Beast from deck, the primary searcher for 师斗 26582143 or 枪斗 41470137
- 再起的剑斗兽 20201255: special summon 1 Gladiator Beast from hand or grave whose race is not already on your field, with battle protection
- 剑斗兽的斗技场-弗拉维圆形斗技场 5063379: discard 1 to search any Gladiator Beast, summons 1 from deck on opponent attack declaration with battle immunity, and at end phase sets a 剑斗 trap from deck if a Gladiator Beast was summoned from deck this turn
- 教斗 2067935: banishes a Gladiator Beast from grave and copies its name until end phase, enables named-material fusions like 多米提安努斯 33652635 needing 维斯帕西亚努斯 88996322
- 女斗 52502677: sends 1 Gladiator Beast from deck or extra to grave as cost and copies its name and level, makes Level 5 or higher material for 主斗 30864377 or copies 维斯帕西亚努斯 88996322
- 奴隶虎 92373006: special summons itself while a Gladiator Beast is on field, tribute it to swap a Gladiator Beast on field for 1 from deck as a GB-effect summon
- 奴隶豹 66863374: link 2 requiring a Gladiator Beast material, first effect searches any 剑斗兽 card, second effect swaps a field Gladiator Beast for a different one from deck
- 骏斗 72246674: on link summon brings 1 Level 4 or lower Gladiator Beast from hand or grave, or from deck if opponent controls a monster, then locks link materials to Gladiator Beasts
- 维斯帕西亚努斯 88996322: special summons itself from hand at battle start when your Gladiator Beast battles, gives your monsters +500 ATK while it is on field
- 剑斗归还 24285858: return 3 Gladiator Beast cards from grave to deck and draw 1, recursion fuel after tag-outs
- 休息的剑斗兽 98891840: return 2 Gladiator Beast cards from hand to deck and draw 3

- **Halt Points**

- Ash Blossom on 剑斗训练所 35224440, 斗技场 5063379 search, 师斗 26582143 search, or 奴隶豹 66863374 search stops the first search
- 增殖的G punishes the many special summons in the combo, stop after 救援猫 14878871 and 奴隶豹 66863374 and do not loop tag-outs under it
- Negate the tag-out trigger at end of battle phase to strand the battle phase with no follow-up summon
- 维斯帕西亚努斯 88996322, 奥古斯都 7573135, and 罪斗 67385964 summon from hand during battle, play around 尼比鲁 by limiting summons before the battle phase
- Interrupt the battle phase itself: cards that end the battle phase or negate the attack break the tag-out loop before it starts
- 剑斗兽的战车 96216229 is a counter trap needing a Gladiator Beast on field, do not use it when the field is empty

- **Mirror Match: 剑斗兽 vs 剑斗兽**

- Whoever tags out first and forces the opponent to answer the first 凯撒 48156348 pop usually wins the trade
- 剑斗兽的战车 96216229 wins the mirror: first player to have a Gladiator Beast plus a set 战车 controls monster effects
- 排斥波 93684009 prevents targeting outside the battle phase, so mirror removal happens only during the battle phase, time 凯撒 48156348 or 鱼斗 5975022 destruction there
- 剑斗海战 52394047 forces attacks and 多米提安努斯 33652635 redirects them, combine to force bad trades
- Keep 维斯帕西亚努斯 88996322 material alive or copy its name with 教斗 2067935 or 女斗 52502677 to keep 多米提安努斯 33652635 access

- **Common Mistakes**

- Do not tag out a monster that did not battle this turn, the trigger requires GetBattledGroupCount()>0
- Do not summon 凯撒 48156348 expecting to tag out into 枪斗 41470137, 凯撒 explicitly excludes 枪斗 from its tag-out summons
- Do not tag out 马斗 25924653 carelessly, its revived monster returns to deck when 马斗 leaves the field
- Do not fuse 多米提安努斯 33652635 without 维斯帕西亚努斯 88996322 or a name copy, 教斗 2067935 and 女斗 52502677 name copies reset at end phase so fuse the same turn
- 排斥波 93684009 summons do NOT count as Gladiator Beast effect summons, summoned monsters get no on-summon trigger
- 奴隶豹 66863374 second effect needs a face-up Gladiator Beast on field to target, link it while a beast is still on board
- 再起的剑斗兽 20201255 cannot summon a Gladiator Beast whose race is already on your field, check Beast vs Beast-Warrior vs Divine-Beast
- 骏斗 72246674 locks your link materials to Gladiator Beasts for the turn, summon it after your non-Gladius links
- 团结的剑斗兽 66290900 only works during the battle phase and locks attacks to Gladiator Beasts that turn, do not activate it when you need non-Gladius attacks
- 奥古斯都 7573135 hand summons return to deck at end phase, do not plan around keeping them
- Do not summon 主斗 30864377 as a fusion material, it cannot be used as fusion material at all
- 克劳狄乌斯 48958757 grants double battle phase only when summoned by its own contact method, not when summoned by 主斗 30864377 or 团结的剑斗兽 66290900
