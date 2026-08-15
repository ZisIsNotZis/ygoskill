---
name: mikanko-experience
description: 御巫 (Mikanko) deck experience: equip-and-reflect battle engine, one-card setup combo, extenders, halt points
---
# 御巫 (Mikanko) Deck Experience

- **Deck Identity**

- Verified from the near-pure build /home/z/ygo/deck/260124御巫/d3924caa2214dbaa.ydk: 60-card main, 15-card extra; every Mikanko card carries archetype setcode 0x18d (397, verified in cards.cdb)
- Level 3 0/0 main deck monsters with mixed attributes and races, so the common "LIGHT Warrior" label is inaccurate for this database: 剑之御巫 波礼 18377261 FIRE Warrior, 珠之御巫 狐理 6327734 WIND Psychic, 镜之御巫 迩迩 54862960 WATER Spellcaster, 御巫奉 佐那伎 11161666 EARTH Illusion
- Ritual boss 大日女之御巫 81260679 is LIGHT Fairy Level 6, and the Extra Deck Xyz 贵日女之御巫 57566760 is LIGHT Fairy Rank 3 (2× Level 3 Mikanko), both 0/0
- Equip Spells are Continuous Spells: 御巫的水舞蹈 43527730, 御巫的火丛舞 80044027, 御巫的诱轮舞 79912449, 御巫舞踊-迷惑鸟 57736667, 御巫的祓舞 16433136; Traps 御巫之契 42705243 and 御巫神较 78199891; Quick-Plays 传承的大御巫 44649322 and 天御巫之阖 17255673 — 传承的大御巫 is a Quick-Play, not a Field Spell, and this database has no Mikanko Field Spell
- OTK package: 脆刃之剑 41927278, 愚钝之斧 19578592, 武器洞 52105192, Kaiju 雷击坏兽 雷鸣龙王 48770333 / 坏星坏兽 席兹奇埃鲁 63941210, 熔岩魔神 102380
- Generic shell: 仪式的准备 96729612, 三战之号 35269904, 神之密告 78114463, 禁忌的圣冠 98829635, 天子的指轮 40678060, 强欲而金满之壶 49238328, 金满而谦虚之壶 84211599, hand traps 灰流丽 14558127 / 增殖的G 23434538 / 屋敷童 73642296 / 朔夜时雨 52038441 / 效果遮蒙者 97268402 / 无限泡影 10045474
- Build quirk: no 御巫神乐 16310544 ritual Spell in the main deck; Ohime 81260679 is searched by 仪式的准备 96729612 and cheated onto the field by the 御巫神舞-二贵子 84550369 grave effect

- **Core Mechanic: Equip and Reflect**

- Equipped Mikanko monsters are indestructible by battle and reflect all battle damage to the opponent; unequipped Level 3s take zero battle damage but stay battle-destructible, verified as EFFECT_INDESTRUCTABLE_BATTLE / EFFECT_REFLECT_BATTLE_DAMAGE / EFFECT_AVOID_BATTLE_DAMAGE in the scripts
- Ohime 81260679 and Xyz 贵日女之御巫 57566760 reflect unconditionally; 波礼 18377261 / 狐理 6327734 / 迩迩 54862960 reflect only while equipped
- One-turn kill: give the opponent a big monster (Kaiju 48770333 / 63941210 or 熔岩魔神 102380), equip 脆刃之剑 41927278 to it (+2000 ATK, battle damage suffered by both players), then 天御巫之阖 17255673 forces every attackable monster to attack your equipped Mikanko
- Damage math verified in ocgcore/processor.cpp: EFFECT_BOTH_BATTLE_DAMAGE copies the damage to both players and EFFECT_REFLECT_BATTLE_DAMAGE then adds your copy onto the opponent, so 熔岩魔神 102380 with 脆刃之剑 41927278 reflects 10000 and a 3300 ATK Kaiju reflects 10600, lethal from 8000
- Equip-swap engine: 御巫的水舞蹈 43527730 equips to a monster, then its ignition Special Summons a different-name Mikanko from hand or deck, re-equips itself to it, and returns the old monster to hand, firing every when-equipped trigger
- Equip-trigger toolbox: 波礼 18377261 adds a Mikanko Equip Spell, 狐理 6327734 adds a Mikanko Trap, 佐那伎 11161666 Special Summons a non-Illusion Mikanko from deck and locks your Extra Deck to Mikanko only for the turn
- 狐理 6327734 second effect: while any Equip Card is face-up on your field, all your Mikanko cards cannot be targeted by opponent effects
- Ritual side: 御巫神乐 16310544 ritual summons Ohime 81260679 and can then destroy up to N opponent cards, N being the number of distinct Equip Spell codes in your GY, and burns 1000 per destroyed card; this build skips the ritual Spell and relies on 二贵子 84550369 to cheat Ohime out

- **One-Card Combo: 御巫神舞-二贵子**

- Honest note: there is no true one-card full board; the engine needs a body plus an equip. 二贵子 84550369 is the one-card setup starter (played ×3), completed by 御巫之契 42705243 plus 御巫的水舞蹈 43527730
- Step 1: activate 二贵子 84550369, send 御巫的水舞蹈 43527730 from deck to GY, then set 御巫之契 42705243 from deck; this locks your Extra Deck to Mikanko only until end of turn
- Step 2: flip 御巫之契 42705243, Special Summon 剑之御巫 波礼 18377261 from deck, then equip it with 御巫的水舞蹈 43527730 from the GY
- Step 3: 波礼 18377261 equip-trigger adds 御巫的火丛舞 80044027 from deck (or a second 水舞蹈 43527730)
- Step 4: activate 御巫的火丛舞 80044027, Special Summon 御巫奉 佐那伎 11161666 or 镜之御巫 迩迩 54862960 from hand or GY and equip it; if 佐那伎 11161666 is summoned, its trigger Special Summons 珠之御巫 狐理 6327734 from deck
- Step 5: Xyz two of the Level 3s into 贵日女之御巫 57566760, whose summon effect adds any Equip Spell from deck or GY, normally 脆刃之剑 41927278 for the next-turn kill
- Step 6: hold 天御巫之阖 17255673 and set the searched trap (御巫神较 78199891) for the kill turn; the 水舞蹈 43527730 swap returns its old monster to hand, so bounce a monster you no longer need for the Xyz
- Two-card engine baseline: any Mikanko monster plus 御巫的水舞蹈 43527730 in hand makes the same board; the body can come from 传承的大御巫 44649322, 御巫的火丛舞 80044027, or a normal summon

- **End Field**

- 贵日女之御巫 57566760 holding an equip, with one Xyz material left for a post-battle chain attack; 0 ATK, indestructible, and reflect make it the kill turn defender
- An equipped 珠之御巫 狐理 6327734 for the global untargetable protection plus a set Trap (御巫神较 78199891 or 御巫之契 42705243) waiting for next turn
- 天御巫之阖 17255673 kept as a Quick-Play, with 禁忌的圣冠 98829635 and 神之密告 78114463 in hand for interaction
- The real end field is a threat, not a wall: 脆刃之剑 41927278 on a Kaiju 48770333 / 63941210 or 熔岩魔神 102380 plus 天御巫之阖 17255673 is a one-hit reflect kill from full LP
- Alternate control end field: equipped 镜之御巫 迩迩 54862960 steals one monster each opponent turn, and 御巫的祓舞 16433136 bounces one monster per side whenever the opponent Special Summons
- Optional Synchro toolbox when the Extra Deck lock is avoided: 金云兽-马龙 93125329 (self-adjusting Level 6 Synchro Tuner) into 鲜花女男爵 84815190, PSY骨架王·Ω 74586817, or 谜式密码大师·紧缩位压缩员 72444406

- **Extenders**

- 御巫之契 42705243: Trap that Special Summons a Mikanko from hand or deck and may equip one Equip Spell from hand or GY; that monster is banished whenever it leaves the field
- 御巫的火丛舞 80044027: Special Summons a Mikanko from hand or GY and equips itself, then may Special Summon one monster from the opponent's GY to their field with effects negated, giving the reflect an attackable body
- 传承的大御巫 44649322: Quick-Play that Special Summons a Mikanko from hand ignoring summoning conditions (returns to hand in the opponent's End Phase); its GY effect mills any Mikanko card from deck
- 御巫神较 78199891: Trap that equips any legal Equip Spell from the DECK to a face-up monster, the clean way to put 脆刃之剑 41927278 or 愚钝之斧 19578592 on the opponent's monster; its GY effect recycles an Equip Spell whenever one is sent to your GY
- 武器洞 52105192: mills 1 from the deck top and adds any Equip Spell from deck or GY, but you must not have normal summoned and cannot normal summon afterward, so activate it before summoning or skip the normal summon
- 贵日女之御巫 57566760 summon search is generic, grabbing 脆刃之剑 41927278, 愚钝之斧 19578592, 天子的指轮 40678060, or any Mikanko Equip Spell
- 仪式的准备 96729612: adds Ohime 81260679 from deck; her hand reveal then searches any Mikanko card at the cost of discarding one card
- 御巫神隐 53174748: equips an opponent monster to your Mikanko as an Equip Card and burns 500 per equip if a Ritual monster is on the field; its GY effect revives a Mikanko from hand or banishment
- 御巫舞踊-迷惑鸟 57736667: after your Mikanko battles, bounce any one card on the field; its GY effect revives a Mikanko, equips itself, and the revived monster is banished on leaving
- 御巫的诱轮舞 79912449: equips to an opponent monster and steals its control while you control a Mikanko; when it leaves the field the stolen monster is sent to the GY
- 天子的指轮 40678060: negates one Spell activation per turn while equipped to an already-equipped monster you control
- 三战之号 35269904: after the opponent activates a monster effect, set any Normal Spell or Trap from deck, but it cannot activate that turn

- **Halt Points**

- Ash Blossom 14558127 on 二贵子 84550369 kills the mill, the set, and the lock; on the 波礼 18377261 / 狐理 6327734 / 佐那伎 11161666 equip-triggers it stops the search or the Special Summon
- 增殖的G 23434538: the 水舞蹈 43527730 swap loop Special Summons once per activation, so stop at two to three summons; the kill turn itself needs few summons and can play through G
- Dimensional effects (次元吸引者, 裂缝, 大宇宙) kill the GY pieces: 火丛舞 80044027 revival, 迷惑鸟 57736667 revival, 二贵子 84550369 grave cheat, 神较 78199891 recycle, Ohime 81260679 grave equip
- Graveyard hate such as 屋敷童 73642296 and 朔夜时雨 52038441 hits the same pieces; this build carries 墓穴的指名者 24224830 and 抹杀之指名者 65681983 to answer them
- Negating your equipped Mikanko removes its reflect and battle protection, so 禁忌的圣冠 98829635 or 无限泡影 10045474 on your own monster is fatal; keep the equips live
- The Extra Deck lock after 佐那伎 11161666 or 二贵子 84550369 forbids 鲜花女男爵 84815190 / PSY骨架王·Ω 74586817 / S:P小夜骑士 29301450 that turn, so make Synchro and Link plays first
- 调和之天救龙 70088809 disables non-Synchro Extra Deck monster effects until your next End Phase, conflicting with 贵日女之御巫 57566760 — do not resolve it on a turn you need the Xyz

- **Mirror Match**

- Reflect is symmetric: the first player whose monster attacks an equipped Mikanko takes the full reflected damage, so the duel is decided by who resolves 天御巫之阖 17255673 or 禁忌的圣冠 98829635 first
- 禁忌的圣冠 98829635 selects without targeting, so it negates the opponent's equipped Mikanko through 狐理 6327734 protection and turns their reflect off
- 狐理 6327734 protection blocks every targeting play: 迩迩 54862960 steal, 御巫的诱轮舞 79912449, 御巫神隐 53174748, and equipping 脆刃之剑 41927278 to their monster — remove their equip first or use non-targeting answers
- 御巫的诱轮舞 79912449 steals the opponent's equipped beater; keep your own 贵日女之御巫 57566760 protected by 狐理 6327734
- 御巫神隐 53174748 burn (500 per equip while a Ritual is on field) and Ohime 81260679 hand-reveal searches decide hand parity in the grind
- Do not attack without 天御巫之阖 17255673 protection in the mirror; every swing you declare can be turned into your own reflect damage

- **Common Mistakes**

- Equipping 愚钝之斧 19578592 to your own Mikanko negates its effects and kills the reflect; it belongs on the opponent's monster as a +1000 ATK reflect amplifier plus a 500 standby burn to them
- 强欲而金满之壶 49238328 can only activate at the start of Main Phase 1 and randomly banishes 6 Extra Deck cards, so play it before any summon and accept the risk to the 贵日女之御巫 57566760 copies
- 金满而谦虚之壶 84211599 halves all damage the opponent takes that turn — never activate it on the reflect-kill turn, and it also banishes 3 or 6 face-down Extra Deck cards
- Using 武器洞 52105192 after the normal summon is illegal; sequence it before the summon and accept the no-normal-summon clause
- Triggering 佐那伎 11161666 or 二贵子 84550369 before Synchro or Link plays locks the Extra Deck; 贵日女之御巫 57566760 stays legal, Baronne 84815190 and the Links do not
- 调和之天救龙 70088809 turns off non-Synchro Extra Deck monster effects until your next End Phase — never use it on a turn you need 贵日女之御巫 57566760
- Monsters summoned by 御巫之契 42705243 and 迷惑鸟 57736667 are banished on leaving the field, so never bounce them with 水舞蹈 43527730 or Xyz them away expecting recovery
- 波礼 18377261 searches only when equipped; summoning it naked wastes its trigger, and traps added by 狐理 6327734 or set by 二贵子 84550369 cannot activate the turn they are set
- 天御巫之阖 17255673 extra attack sends one of your equips to the GY as cost and the monster cannot direct attack afterward; keep a spare equip on the field
- 脆刃之剑 41927278 sends itself to the GY when its controller takes 2000 or more battle damage — with your reflect that never happens, but only while your Mikanko stays equipped
- 神之密告 78114463 negates Spell and Trap activations only, do not hold it for monster effects
- The opponent monster gifted by 御巫的火丛舞 80044027 has negated effects but is still an attackable body, so it is a reflect target, not a defense
