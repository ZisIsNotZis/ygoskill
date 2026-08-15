---
name: spellbook-experience
description: 魔导书 (Spellbook) deck experience: spell recursion engine, searchers, one-card combo, extenders, halt points
---
# 魔导书 (Spellbook) Deck Experience

- **Deck Identity**

- Spellcaster monsters plus the 魔导书 spell family, a slow grind-control deck that loops spells between hand, deck, graveyard, and the banished zone instead of one-shot combo lines
- Core searcher: 魔导书士 巴特尔 14824019 (Level 2 WATER, mandatory search on Normal or Flip Summon), recursion spells 奥义之魔导书 89739383, 创造之魔导书 56981417, 蜡板之魔导书 61592395, field spell 魔导书院 拉迈松 33981008
- Draw and removal: 冰火之魔导书 23314220 (pitch a Spellcaster or Spellbook, draw 2), 恶灵之魔导书 97997309 (Quick-Play, banishes 1-3 Spellbooks from grave for bounce, flip, or banish), 律法之魔导书 88616795 (Quick-Play, temporary spell or trap immunity), 水卜之魔导书 25123082 (1000 ATK buff plus battle search)
- Bosses: 魔导法士 朱诺 86585274 (2500, self-special from hand by revealing 3 Spellbooks, pop one card by banishing a Spellbook), 魔导法皇 海隆 92918648 (Rank 7, detach to destroy up to grave Spellbook count opponent backrow), 魔导皇士 安普尔 53136004 (steals a monster by banishing a Spellcaster plus a Spellbook), 魔导天士 杜勒蒙德 29146185 (field wipe by revealing 4 different Spellbooks after grave recursion)
- Monsters are mixed LIGHT and DARK (朱诺, 杜勒蒙德 LIGHT; 海隆, 安普尔, 迪亚勒 DARK), not a pure DARK deck, and the Level 5-plus LIGHT or DARK Spellcaster searches (朱丝蒂 26732909, 坦佩尔 87608852, 马特 63175639 end phase) can pick either attribute
- Build quirk: the current format in this codebase lflist.conf is 2026.7 and 魔导书的神判 46448938 is not listed, so the OCG-banned end-phase engine is fully legal here at 3 copies
- Naming note: this database uses 之-suffix names, the alternate 魔导书·刻印 / 魔导书·禁域 / 魔导书·星书 / 魔导书·圣光 forms are the same cards as 恶灵 / 律法 / 冰火 / 水卜, 创世魔导 refers to 创造之魔导书 56981417, 魔导王 安普拉莉 maps to 魔导皇士 安普尔 53136004, and 魔导化士 胡斯托普 does not exist in this database, the only 魔导化士 here is 马特 63175639

- **Core Mechanic: Spell Recursion Loop**

- 巴特尔 14824019 on Normal or Flip Summon adds any 魔导书 spell from deck to hand as a mandatory trigger, it always resolves if any Spellbook spell remains in deck
- 奥义之魔导书 89739383 searches any 魔导书 card except itself, including the 魔导书 monsters, once per turn
- 创造之魔导书 56981417 requires a face-up Spellcaster on field, reveals another 魔导书 card from hand as cost, then copies the activation effect of one 魔导书 Normal Spell in the grave, re-using 奥义 searches, 蜡板 recovery, or 水卜 buffs from the graveyard
- 创造 only copies Normal Spells, it cannot copy the Quick-Plays 律法 88616795, 恶灵 97997309, 神判 46448938, the field spell 魔导书院 拉迈松 33981008, or the Equip 死灵之魔导书 52628687
- 蜡板之魔导书 61592395 adds one face-up banished 魔导书 spell back to hand, which is why the deck deliberately banishes spells through 恶灵, 朱诺 86585274, and 白雪 55623480 costs
- 魔导书院 拉迈松 33981008 in Standby Phase, with a Spellcaster on field or grave, moves one 魔导书 spell from grave to deck bottom and draws one, and when destroyed by the opponent special summons a Spellcaster of level equal to or below the number of 魔导书 spells in the grave from hand or deck
- 冰火之魔导书 23314220 sends one other 魔导书 card from hand or face-up field, or one face-up Spellcaster from field, to the grave to draw 2, the standard way to turn 巴特尔 or a dead Spellbook into cards
- The loop: 奥义 searches from deck, its grave copy is reused by 创造, banished copies return via 蜡板, and 书院 cycles grave copies back to the deck for the next 巴特尔 or 奥义

- **One-Card Combo: 魔导书士 巴特尔**

- Step 1: Normal Summon 巴特尔 14824019, its mandatory effect adds 奥义之魔导书 89739383 from deck
- Step 2: activate 奥义, add 魔导书院 拉迈松 33981008 (grind), 蜡板之魔导书 61592395 (recovery), or 创造之魔导书 56981417 (recursion) depending on hand
- Step 3: with a second 魔导书 in hand, activate 创造 revealing it, copy 奥义 from the grave, and add another Spellbook such as 恶灵 97997309 or 水卜 25123082
- Step 4: activate 冰火 23314220 sending 巴特尔 to the grave, draw 2, then 蜡板 61592395 recovers any Spellbook banished by 恶灵 or 朱诺 86585274 costs
- 巴特尔 alone ends on 巴特尔 plus one Spellbook in hand, the full loop needs a second Spellbook or 神判 46448938 to truly extend

- **One-Card Combo: 魔导书的神判**

- Activate 神判 46448938 first in a spell chain, every spell activated by either player after it adds one to the end-phase count, negated activations subtract one
- Chain 巴特尔 search, 奥义, 创造, 冰火, 水卜, or 科瑞森 40230018 after it, at end phase add up to the count of 魔导书 spells from deck, then optionally special summon one Spellcaster of level equal to or below the number added from deck, 朱诺 86585274 needs seven, 沉默魔术师 41175645 or 巴特尔 need less
- 神判 is a Quick-Play, it can be chained to opponent spell activations on their turn and still resolves at that turn end phase

- **End Field**

- Typical control end field: 巴特尔 14824019, 沉默魔术师 41175645, or 朱诺 86585274, 魔导书院 拉迈松 33981008 face-up, one set 恶灵之魔导书 97997309 for the opponent turn, and 律法之魔导书 88616795 ready to grant immunity
- With the 神判 46448938 line the end field adds several Spellbook spells in hand and one Spellcaster from deck, hand advantage is the real end board
- Rank 4 options from Level 4 monsters 白雪 55623480, 辉夜 86937530, 沉默魔术师 41175645: 鸟铳士 卡斯泰尔 82633039, No.39 希望皇 霍普 84013237 into 闪光No.39 希望皇 霍普·电光皇 56832966
- Rank 7 boss 魔导法皇 海隆 92918648 over two 朱诺 86585274 detaches to destroy up to the number of 魔导书 spells in the grave opponent spells and traps
- 魔导天士 杜勒蒙德 29146185 special summoned by 马特 63175639 or 坦佩尔 87608852 adds two 魔导书 from the grave, then reveals four different 魔导书 in hand to destroy all other cards on the field

- **Extenders**

- 魔导书库 科瑞森 40230018 searches when no 魔导书 spell is in the grave, the opponent picks one of three revealed, and it locks all non-魔导书 spells for the turn, play it before any Spellbook reaches the grave
- 魔导书库 苏雷 20822520 with five or more 魔导书 in the grave reveals the top 2 and adds all 魔导书 among them, with the same non-Spellbook spell lock for the turn
- 魔导杂货商人 32362575 is a flip monster, on flip it mills from the deck until a spell or trap, adds that card and sends the rest to the grave, classic graveyard fuel and Spellbook hit
- 魔导化士 马特 63175639 mills one 魔导书 each turn, and if five or more Spellbook spell types are in the grave at end phase it tributes itself to special summon a Level 5 or higher DARK Spellcaster from deck
- 魔导教士 朱丝蒂 26732909 and 魔导召唤士 坦佩尔 87608852 trade a Level 3 EARTH body for one Level 5 or higher LIGHT or DARK Spellcaster plus one Spellbook, 朱丝蒂 at end phase, 坦佩尔 immediately with a Level 5-plus summon lock
- 魔导鬼士 迪亚勒 56174248 revives itself from the grave by banishing three 魔导书 spells, feeding the 蜡板 61592395 loop
- 妖精传姬-白雪 55623480 special summons itself from the grave by banishing seven cards from hand, field, and grave, dumping Spellbooks into the banished zone for 蜡板 recovery, and flips a monster face-down on summon
- 妖精传姬-辉夜 86937530 searches a 1850 ATK Spellcaster such as 魔导老士 艾尔米特 90743290 on summon, 艾尔米特 gains 300 ATK and two levels per Spellbook activation, and 辉夜 bounces a monster as a quick effect
- 死灵之魔导书 52628687 revives a Spellcaster from the grave as an Equip with level gain, at the cost of banishing another Spellcaster and revealing a Spellbook from hand

- **Halt Points**

- 灰流丽 14558127 on 巴特尔 14824019 search, on 奥义 89739383, or on 科瑞森 40230018 stops the first search and usually the whole turn
- 灰流丽 can also negate 魔导书院 拉迈松 33981008 special summon from deck when the field spell is destroyed by the opponent
- 神判 46448938 end-phase resolution is not a card activation so 灰流丽 cannot negate it, stop it at activation with 神之宣告 41420027 or 神之通告 40605147, or block the end-phase deck adds with 小丑与锁鸟 94145021
- 增殖的G 23434538 is only mild, the deck special summons one monster per line, but the 神判 chain and 白雪 55623480 recursion give the opponent several draws
- 魔导书院 拉迈松 33981008 is the grind engine, removing it stops the free draw and the destruction summon, protect it or fall back to the 蜡板 61592395 and 创造 56981417 loop

- **Mirror Match: 魔导书 vs 魔导书**

- The 神判 46448938 player who chains more spells wins the end-phase advantage, save quick-plays 恶灵 97997309 and 律法 88616795 to chain under the opponent 神判 and add to its count too
- 恶灵 banishes three Spellbooks to banish the opponent 魔导书院 拉迈松 33981008, cutting their grind and their standby draw
- 律法 88616795 on your own monster blocks the opponent 恶灵 flip and blocks 冰火 23314220 which cannot send an immune Spellcaster
- Watch the banish zone, 蜡板 61592395 recovers banished Spellbooks, whoever feeds fewer banished cards keeps more 蜡板 targets, and 白雪 55623480 flips the opponent 巴特尔 14824019 face-down before it adds value while its own banish effect feeds your 蜡板
- Whoever 魔导书院 拉迈松 33981008 survives the exchange draws more cards and wins the grind

- **Common Mistakes**

- Do not pitch the only face-up Spellcaster with 冰火 23314220 before using 创造 56981417 or 恶灵 97997309, both need a face-up Spellcaster on the field
- 创造 56981417 cannot copy Quick-Plays, field, or Equip Spellbooks, only the Normal Spells 奥义 89739383, 蜡板 61592395, 水卜 25123082, 冰火 23314220, 科瑞森 40230018, 苏雷 20822520
- 蜡板 61592395 only retrieves face-up banished 魔导书, face-down banished cards and graveyard cards are not targets, and it is dead without an existing banished Spellbook
- Play 科瑞森 40230018 before any Spellbook reaches the grave, it is dead with a single 魔导书 in the grave, and its non-Spellbook spell lock punishes hybrid builds that want to follow with Sky Striker or other spells
- 巴特尔 14824019 search is mandatory, always search the highest value Spellbook, and it only triggers on Normal or Flip Summon, not on Special Summon
- 恶灵 97997309 costs Spellbooks from the grave, keep enough grave Spellbooks for 书院 33981008, 创造 56981417, and 苏雷 20822520 instead of banishing everything
- 水卜 25123082 requires a battle destroy to search, buff a monster that can actually kill something, do not waste it on a defensive 巴特尔
- 神判 46448938 counts only spells activated after it, activating it last in a chain wastes the count, and negated activations reduce it
