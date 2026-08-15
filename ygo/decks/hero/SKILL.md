---
name: hero-experience
description: 英雄 (HERO) deck experience: V-HERO engine, fusion spells, Masked HERO, Favorite Contact line, extenders, halt points
---
# 英雄 (HERO) Deck Experience

- **Deck Identity**

- Modern HERO is a multi-archetype hybrid under the shared HERO setcode 0x8: Elemental HERO 元素英雄, Destiny HERO 命运英雄, Vision HERO 幻影英雄, Masked HERO 假面英雄, Xtra HERO 特异英雄 links, and the Favorite 至爱 fusions
- Engine core: 幻影英雄 独善人 18094166, 幻影英雄 增量人 22865492, 幻影英雄 仿生人 27780618, 元素英雄 影雾女郎 50720316, 元素英雄 天空侠 40044918, 元素英雄 液态侠 59392529
- D-HERO package: 命运英雄 魔性人 9411399, 命运英雄 否定人 16605586, 命运英雄 血魔-D 83965310, 融合命运 52947044 into 命运英雄 毁灭凤凰人 60461804
- Fusion spells: 融合 24094653, 奇迹融合 45906428, 置换融合 74335036, 融合命运 52947044, 至爱接触 75047173, 超融合 48130397
- Masked HERO quick access: 假面变化 21143940 into 假面英雄 暗爪 58481572, 假面英雄 酸水 29095552, 假面英雄 原子火 85672957, 假面英雄 宝钻 62624486; main-deck Masked HERO 假面英雄 炉火 58288218, 假面英雄 暮鸦 10808715, 假面英雄 泉水 66206748
- Neos splash for Favorite/contact lines: 元素英雄 新宇侠 89943723, 新空间侠·水波海豚 17955766, 奇迹除外士 30875635, EN切换 10186633
- Xtra HERO links: 特异英雄 十字人 58004362, 特异英雄 地狱裂魔 19324993, 特异英雄 神杖先驱 1948619

- **Core Mechanic: V-HERO Engine into Fusion**

- 独善人 18094166 in hand discards 1 HERO as cost to special summon itself, then on summon places 1 V-HERO monster from deck to your Spell/Trap zone as a Continuous Trap, and for the rest of the turn you cannot special summon non-HERO monsters from the extra deck
- 增量人 22865492 from the S/T zone, during a Main Phase, releases 1 HERO you control to special summon itself, and when it was special summoned from the S/T zone it special summons 1 Level 4 or lower V-HERO from deck, typically 仿生人 27780618
- 仿生人 27780618 on summon sends 1 HERO from deck to GY, typically 影雾女郎 50720316, then as an ignition effect banishes 1 HERO from your GY to add 融合 24094653 from deck to hand
- 影雾女郎 50720316 searches a HERO Quick-Play spell from deck when special summoned, typically 假面变化 21143940, and searches a HERO monster from deck when it is sent to the GY
- 天空侠 40044918 on summon or special summon either adds 1 HERO monster from deck to hand or, if you control other HERO monsters, destroys that many Spell/Trap cards on the field
- 液态侠 59392529 on normal summon special summons 1 Level 4 or lower HERO from your GY, and when used as fusion material for a HERO fusion summon draws 2 cards then discards 1
- Fusion materials come from hand, field, deck (融合命运 only), and GY (奇迹融合 only), and each fusion spell carries its own extra-deck summon lock, so sequencing the fusion spells in the right order is the whole deck

- **One-Card Combo: 独善人**

- Starter: 独善人 18094166 in hand plus any other HERO card to discard
- Step 1: activate 独善人, discard 1 HERO as cost, special summon it
- Step 2: 独善人 effect places 增量人 22865492 from deck to the S/T zone as a Continuous Trap
- Step 3: activate 增量人 in the S/T zone, release 独善人, special summon 增量人, then its own effect special summons 仿生人 27780618 from deck
- Step 4: 仿生人 effect sends 影雾女郎 50720316 from deck to GY; 影雾女郎 in GY adds 液态侠 59392529 or 天空侠 40044918 from deck to hand
- Step 5: 仿生人 ignition effect banishes 影雾女郎 from GY and adds 融合 24094653 from deck to hand
- Step 6: link 2 with 增量人 and 仿生人 into 特异英雄 十字人 58004362, which on link summon special summons 1 D-HERO from GY (the discarded 否定人 16605586 if it was the cost), then releases a D-HERO to add 1 HERO monster from deck, typically 天空侠 40044918
- Step 7: normal summon 天空侠, add another HERO or destroy backrow, then 融合 液态侠 and 天空侠 into 元素英雄 日出侠 22908820; 日出侠 adds 奇迹融合 45906428, and 液态侠 as material draws 2 discard 1
- Step 8: 奇迹融合 banishes 日出侠 plus another HERO from field or GY into 至爱英雄 闪光火焰翼侠 87758525, which shuffles 5 GY monsters into deck, draws 2, and gains 1000 ATK
- Step 9: 假面变化 21143940 on a DARK HERO such as 影雾女郎 special summons 假面英雄 暗爪 58481572 from the extra deck
- Verify exact material order against the chosen extra deck; the engine steps are script-verified, the finisher targets vary by build

- **End Field One-Card**

- 假面英雄 暗爪 58481572 with opponent deck-to-GY banished instead and one random opponent hand card banished when they add from deck to hand outside the Draw Phase
- 至爱英雄 闪光火焰翼侠 87758525 with the 1000 ATK buff and battle-destroy burn, plus 特异英雄 十字人 58004362 link and the 奇迹融合/假面变化 set up
- DPE variant instead of or alongside: 融合命运 52947044 with 魔性人 9411399 from deck plus a hand HERO into 命运英雄 毁灭凤凰人 60461804, which destroys 1 card you control and 1 card on the field each turn and revives itself from GY at the next Standby Phase
- 至爱接触 75047173 line: shuffle fusion materials from hand, field, GY, and banished zone to deck bottom, then special summon 1 fusion monster that lists a HERO as material, ignoring summoning conditions; if 新宇侠 89943723 was shuffled, that monster cannot be returned to the extra deck
- Halt point: Ash Blossom on 独善人 activation or 仿生人 mill stops the engine, 增殖的G punishes the special summon count, and any negation of 假面变化 or the first fusion leaves a reduced board

- **Extender: 液态侠 59392529 and 天空侠 40044918**

- 液态侠 normal summon revives any Level 4 or lower HERO from GY, turning one extra normal summon into a second body for links or fusion material
- 液态侠 as HERO fusion material draws 2 discard 1, netting one card while fueling the grave for 奇迹融合 45906428 or 仿生人 27780618 banish cost
- 天空侠 as a second normal summon target searches the missing combo piece, and its destroy effect clears backrow when another HERO is already on field

- **Extender: Masked HERO package**

- 假面变化 21143940 is a Quick-Play that sends 1 face-up HERO you control to GY and special summons 1 Masked HERO of the same attribute from the extra deck, so 影雾女郎 50720316 DARK becomes 假面英雄 暗爪 58481572, WATER 液态侠 becomes 假面英雄 酸水 29095552, FIRE becomes 假面英雄 原子火 85672957
- 假面英雄 炉火 58288218 in hand reveals itself to add 假面变化 21143940 or 融合 24094653 from deck, then discards 1, and special summons itself when a HERO fusion is special summoned, then banishes itself when it leaves the field
- 假面英雄 暮鸦 10808715 banishes 1 HERO from your GY as cost to special summon itself from hand, then searches any Masked HERO from deck or GY
- 假面英雄 泉水 66206748 reveals itself in hand to special summon 1 HERO from hand in Defense, and when sent to GY as cost or by effect sets 假面变化 21143940 from deck or GY
- 对极英雄 混沌侠 23204029, fusion of 2 Masked HERO and treated as a LIGHT monster, negates 1 face-up card's effects until end of turn as a quick effect

- **Extender: Xtra HERO links and Favorite fusions**

- 特异英雄 地狱裂魔 19324993 on link summon reveals 1 HERO fusion monster from the extra deck and adds up to 2 of the monsters listed as its material from deck, locking you to HERO extra deck summons that turn
- 特异英雄 神杖先驱 1948619 when a HERO is summoned to a zone it points to sets 1 融合 24094653 or 假面变化 21143940 from your GY, and when destroyed by battle or opponent effect special summons 1 HERO from hand
- 特异英雄 十字人 58004362 recycles a D-HERO from GY on link summon and searches any HERO monster by releasing a D-HERO
- 至爱英雄 火焰翼侠 13243124, fusion of 2 same-Type different-Attribute monsters and treated as Elemental HERO, gains 1000 ATK against 2200+ ATK monsters and, when a monster is destroyed by battle in either player's turn, quick-fusion summons using your hand and field monsters
- 元素英雄 日出侠 22908820 searches 奇迹融合 45906428 on fusion summon, and its on-field trigger destroys 1 card when another HERO attacks
- 奇迹除外士 30875635 in hand sends 1 Neo-Spacian from deck to GY to special summon itself, then on summon adds 1 Spell/Trap that lists an Elemental HERO monster, such as 至爱接触 75047173 or EN切换 10186633, and when sent to GY banishes 1 card from the opponent GY
- EN切换 10186633 shuffles 1 face-up Elemental HERO or Neo-Spacian you control into deck to special summon another from deck, and in GY banishes itself to shuffle HEROes back and draw 1
- 羽翼栗子球·萨巴希尔 LV10 40237839 reveals itself and pays half your LP to add 1 融合 spell from deck and shuffle itself back, locking you to HERO extra deck summons that turn, and on the opponent turn with 1000 LP or less special summons itself and burns

- **Halt Points**

- 灰流丽 14558127 negates 独善人 18094166 activation, 仿生人 27780618 mill, and 影雾女郎 50720316 search, each stopping a different stage of the line
- 增殖的G 23434538 forces the deck to stop after 2-3 summons or hand the opponent cards on every extra summon
- Negating 增量人 22865492's S/T zone activation or 仿生人's search leaves only two Level 3/4 bodies and no fusion
- 墓穴的指名者 24224830 and 抹杀之指名者 65681983 answer 影雾女郎 and 仿生人 GY effects; the deck has no built-in protection for its enablers
- 次元障壁 83326048, 大宇宙, or 次元吸引者 style floodgates cut off the GY-dependent engine and 奇迹融合 45906428
- 暗爪 58481572 is a one-shot floodgate but 2400 ATK dies to 禁忌的一滴 24299458, 无限泡影 10045474, and 三战之才 25311006

- **Mirror Match: 英雄 vs 英雄**

- The player who resolves 独善人 18094166 first usually wins the resource race, so hand traps and 禁忌的一滴 24299458 decide the game
- 暗爪 58481572 mirrors are deadly: with both players running GY-reliant engines, whoever controls 暗爪 first forces the opponent to play around banished mills and hand removal
- 超融合 48130397 is a blowout in the mirror, using the opponent's own HERO field as fusion material with a discard cost
- 三战之才 25311006 steals the opponent's 至爱英雄 闪光火焰翼侠 87758525 or 日出侠 22908820 after your monsters are destroyed
- 血魔-D 83965310 negates all opponent face-up monster effects and equips one of their monsters, shutting down the whole HERO board
- Do not over-extend into 增殖的G 23434538 in the mirror, the first player to run out of gas loses

- **Common Mistakes**

- Do not activate 独善人 18094166's deck-to-S/T effect before planning the turn's extra deck summons, the lock to HERO extra deck summons applies for the whole turn
- 融合命运 52947044 can only use hand and deck materials, never GY, and the fusion is destroyed at the end phase of the next turn, so use it for 毁灭凤凰人 60461804 which revives itself, not for long-term boards
- 奇迹融合 45906428 banishes its materials, so 影雾女郎 50720316 banished as material cannot trigger its GY search
- 假面变化 21143940 requires the exact same attribute, do not attempt to Mask Change a LIGHT or WIND HERO into 暗爪 58481572 or 酸水 29095552
- 至爱接触 75047173 shuffles materials back to deck bottom, verify the target fusion lists a HERO monster as material before activating, and if 新宇侠 89943723 is shuffled the summoned monster cannot be returned to the extra deck
- 液态侠 59392529 draws 2 then discards 1, leaving the discard card choice for a HERO the opponent can use, and its revive effect only works on a normal summon
- 十字人 58004362 and 地狱裂魔 19324993 both impose HERO-only extra deck summon locks, so summon non-HERO tools like 捕食植物 食虫粉衣凤梨森蚺 70369116 before activating them or not at all
- Do not release the wrong D-HERO for 十字人's search, the released monster's name cannot be the search target
- Normal summon 天空侠 40044918 first in the combo so its search can pick 液态侠 59392529 or 影雾女郎 50720316 that the rest of the line needs
