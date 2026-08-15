---
name: zombie-experience
description: 不死 (Zombie) deck experience: Zombie World floodgate engine, Doomking control, one-card lines, extenders, halt points
---
# 不死 (Zombie) Deck Experience

- **Deck Identity**

- 不死 is a Zombie type (不死族) control pile, not a setcode archetype: 不死世界 4064256, 齐唱僵尸 49959355, 尸界的班西 66570171 and 死灵王 恶眼 39185163 all have setcode 0, the deck is defined by type plus the field spell
- Representative build from deck 191123不死世界: 3x 不死世界 4064256, 3x 齐唱僵尸 49959355, 3x 尸界的班西 66570171, 2x 死灵王 恶眼 39185163, 2x 马头鬼 92826944, 3x 不知火的隐者 94801854, 1x 吸血鬼吸食者 37129797, 1x 成长的花朵 92964816, staples and a synchro-fusion toolbox
- Other Zombie sub-archetypes are separate setcodes that only splash: 不知火 217, 吸血鬼 142, 魔妖 289, 复仇死者 262, 黄金国巫妖 4418
- The engine is 齐唱僵尸 49959355 as starter, 死灵王 恶眼 39185163 as boss, 尸界的班西 66570171 as the 不死世界 enabler

- **Core Mechanic: 不死世界 floodgate engine**

- 不死世界 4064256: all face-up monsters and all grave monsters become Zombie, and neither player can Tribute Summon except with Zombie tributes, verified in script c4064256.lua
- Making every field and grave monster a Zombie turns every opponent monster-effect activation from field or grave into a Zombie effect trigger for 死灵王 恶眼 39185163, and every grave revival into a draw for 吸血鬼吸食者 37129797
- 尸界的班西 66570171: quick effect, banish itself from field or grave, activate 不死世界 4064256 from hand or deck, once per turn on either turn, verified in script c66570171.lua, note it cannot activate from hand
- 尸界的班西 66570171 while on field: 不死世界 4064256 cannot be destroyed by card effects and cannot be targeted by card effects
- 死灵王 恶眼 39185163: when a Zombie monster effect activates, once per chain, either negate that effect or banish 1 monster from any field or grave, each option usable once per own turn, verified in script c39185163.lua
- 死灵王 恶眼 39185163: during either standby phase, if any field zone holds a face-up card, special summon itself from grave in defense position, once per turn
- 吸血鬼吸食者 37129797: link-2, draw 1 whenever a Zombie is special summoned from either player's grave, and may Tribute opponent Zombies for a Tribute Summon
- Game plan: 不死世界 4064256 locks the opponent into Zombies, 死灵王 39185163 negates or banishes each Zombie activation, 吸血鬼吸食者 37129797 converts every grave revival into card advantage

- **One-Card Combo: 愚蠢的埋葬 81439173**

- Step 1: activate 愚蠢的埋葬 81439173, send 尸界的班西 66570171 from deck to grave
- Step 2: chain 班西 quick effect, banish itself from grave, activate 不死世界 4064256 from deck, one card puts the floodgate engine online
- Alternative one-card: 一对一 2295440, discard 1, special summon 成长的花朵 92964816 from deck, link it into 连接栗子球 41999284, banish 成长的花朵 to add 死灵王 恶眼 39185163 from deck, or special summon it directly if 不死世界 4064256 is up
- 齐唱僵尸 49959355 alone is the one-card grave setup: effect 2 mills 1 Zombie from deck and raises any face-up monster level by 1, effect 1 discards 1 to raise a level, it needs one more card to convert the mill into a full field

- **End Field**

- Standard two-card line 齐唱僵尸 49959355 + 尸界的班西 66570171: discard 班西 with effect 1, 班西 activates 不死世界 4064256 from deck, effect 2 mills 成长的花朵 92964816, 成长的花朵 banishes itself and special summons 死灵王 恶眼 39185163 from deck because 不死世界 is up
- Full end field: 不死世界 4064256, 死灵王 恶眼 39185163, 吸血鬼吸食者 37129797, backrow 大逮捕 36975314 or 墓穴的指名者 24224830, hand 灰流丽 14558127 or 屋敷童 73642296
- 死灵王 39185163 recurs every standby while any field spell is face up, the end field rebuilds itself each turn
- Halt points on the line: 灰流丽 14558127 on the 齐唱僵尸 mill or on the 不死世界 activation, 屋敷童 73642296 on the 死灵王 standby revival, 墓穴的指名者 24224830 banishing 死灵王 or 马头鬼 92826944

- **Extenders**

- 马头鬼 92826944: banish from grave to special summon any Zombie from grave, the universal recursion
- 牛头鬼 52467217: main phase mill 1 Zombie from deck, when sent to grave banish another Zombie in grave to special summon a Zombie from hand
- 不知火的隐者 94801854: Tribute a Zombie on field to special summon a defense 0 Zombie tuner from deck, namely 齐唱僵尸 49959355 or 尸忍 90020780
- 尸忍 90020780: on field, draw 1 then discard 1 whenever another Zombie is special summoned from your grave, and special summons itself when banished from grave
- 成长的花朵 92964816: when sent to grave, banish itself to add any level 5+ Zombie from deck, special summons it instead while 不死世界 4064256 is up, locks you into Zombie summons for the turn
- 流星登龙 68431965: on synchro summon mill a lower level monster and reduce own level, mills 成长的花朵 92964816 or 马头鬼 92826944, a level 7 tuner into 天威之龙鬼神 5041348 or PSY骨架王·Ω 74586817
- 超融合 48130397: with 不死世界 4064256 up, fuse 2 opponent Zombies into 冥界龙 龙亡 8198620, or 凶饿毒融合龙 41209827 or 沼地的泥龙王 54757758
- 吸血鬼千金 6039967: special summons itself from hand on any attack declaration and pumps a Zombie in battle, 暗之卡组破坏病毒 54974237 Tributes 死灵王 39185163 to destroy opponent spells and traps

- **Halt Points**

- 灰流丽 14558127: chain to 齐唱僵尸 49959355 effect 2 mill, to the 尸界的班西 66570171 不死世界 activation, or to 牛头鬼 52467217 mill
- 屋敷童 73642296: negates the 死灵王 39185163 standby revival, the 马头鬼 92826944 revival, and the 牛头鬼 52467217 grave effect, every grave special summon
- 墓穴的指名者 24224830: banishes 死灵王 39185163 or 马头鬼 92826944 from grave and negates them, breaking the recursion engine
- Removing 不死世界 4064256 while 尸界的班西 66570171 is not on field stops 死灵王 39185163 standby revival because it needs any face-up field spell
- Opponent 大逮捕 36975314 steals 死灵王 39185163 or 吸血鬼吸食者 37129797, and non-targeting removal like 梦幻崩影·凤凰 2857636 bypasses the 班西 protection

- **Mirror Match: 不死 vs 不死**

- The player whose 不死世界 4064256 sticks wins the Doomking race, chain your 死灵王 39185163 to theirs and negate the activation or banish it from grave
- 死灵王 39185163 negate and banish options each lock once per own turn, use the banish option on the opponent 死灵王 and the negate on their mill activations
- 墓穴的指名者 24224830 and 屋敷童 73642296 are the mirror weapons, hit the opponent 死灵王 39185163 before standby
- 超融合 48130397 under 不死世界 4064256 fuses both 死灵王 into 冥界龙 龙亡 8198620, the cleanest mirror out
- 吸血鬼吸食者 37129797 draws for both players whenever either revives from grave, pace your grave plays and expect theirs
- The first 尸界的班西 66570171 protects 不死世界 4064256 from destruction and targeting, deny the opponent 班西 with 墓穴的指名者 24224830

- **Common Mistakes**

- 尸界的班西 66570171 activates from field or grave only, never from hand, do not hold it in hand expecting a quick 不死世界
- Do not use 齐唱僵尸 49959355 effect 2 then attack with non-Zombie monsters, they cannot attack that turn unless 不死世界 4064256 makes them Zombie
- 死灵王 39185163 standby revival needs any face-up field spell, if 不死世界 4064256 is removed and no other field spell exists the engine is dead, keep 尸界的班西 66570171 or another field spell as backup
- 死灵王 39185163 negate and banish options are each once per own turn, resolving two Zombie effects does not give two negates
- 死灵王 39185163 also triggers on your own Zombie activations, it is optional so do not accidentally negate your own 齐唱僵尸 49959355 or 马头鬼 92826944 plays
- 成长的花朵 92964816 locks you into Zombie summons after resolving, do not extend into non-Zombie links afterwards
- 不死世界 4064256 also makes your own field and grave monsters Zombie, 灰流丽 14558127 and 屋敷童 73642296 become Zombie triggers for the opponent 死灵王 while on field
- 冥界龙 龙亡 8198620 must be Fusion Summoned, it cannot be special summoned from grave or extra deck
- Do not Tribute Summon non-Zombies while 不死世界 4064256 is up, only Zombies can be Tribute Summoned by either player
- 吸血鬼吸食者 37129797 revives an opponent grave monster onto their field as a defense Zombie, it can swing back or become tribute fodder, banish it with 死灵王 39185163 instead
