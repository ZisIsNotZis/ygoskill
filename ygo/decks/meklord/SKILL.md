---
name: meklord-experience
description: 机皇 (Meklord) deck experience: anti-synchro steal engine, one-card combo, extenders, halt points
---
# 机皇 (Meklord) Deck Experience

- **Deck Identity**

- Machine archetype, identity is anti-Synchro: 机皇帝 Emperors special summon themselves when your face-up monster is destroyed by effect, then equip opponent Synchro monsters as Equip Spells and add their ATK
- Archetype set codes verified in scripts: 0x13 = 机皇 umbrella, 0x3013 = 机皇帝, 0x5013 = 机皇神, 0x6013 = 机皇兵, and 0x6013/0x5013/0x3013 all satisfy 0x13 checks, so every 机皇 searcher reaches the whole archetype
- Core members: 机皇帝 神智∞ 68140974 (spell negate), 机皇帝 神空∞ 31930787 (direct attack), 机皇帝 神陆∞ 4545683 (ATK = half your LP, steal-back), 机皇帝 神智∞-同调吸收 30221870 (opponent-turn hand trap version)
- Modern support makes it a Machine swarm: 机皇创出 39109382 (searcher plus self-destroy engine), 机皇兵厂 助奏 3715284 (two bodies from deck), 机皇枢 无限核 77710579 (S/T search plus 机皇帝 revive), 根绝机皇神 2992036 (grave revive plus Synchro burn)
- Bosses: 机皇神 机录∞ 63468625 (4000 ATK, standby burn), 机皇神龙 三曲枝 4837861 (steal from extra deck, triple attack), 机皇神龙 星标 38522377 (ATK = sent monsters total, Synchro burn)
- Deck folder shows about 70 机皇 builds, mostly casual legacy decks such as 200530机皇, 200808机皇, 210717机皇, while modern builds are Machine hybrids like 250926奏悦机组机皇 with 反叛曲机器人 and 兽带斗神
- Build quirk: legacy .ydk files place extra deck monsters in the main deck section with no !extra marker, for example 200808机皇 lists 天霆号 阿宙斯 90448279, 连接栗子球 41999284, 梦幻崩影·凤凰 2857636, 梦幻崩影·独角兽 38342335 as main deck cards, so re-section the file before loading

- **Core Mechanic: 机皇帝 anti-Synchro trigger**

- All three Emperors cannot be Normal Summoned and special summon themselves from hand when a face-up monster you control is destroyed by effect and sent to grave, script check is REASON_EFFECT plus REASON_DESTROY with previous location MZONE face-up and your control, so self-destruction is the engine
- Battle destruction, tribute such as 原始生命态 尼比鲁 27204311, and banishment do not trigger the Emperors
- Once per turn ignition effect: target 1 opponent Synchro monster, equip it by control change and gain its ATK, while 机皇帝 神智∞ 68140974 or 神空∞ 31930787 is face-up your other monsters cannot attack
- 机皇帝 神智∞ 68140974 negates and destroys one opponent SPELL card activation per turn, it cannot negate trap or monster activations
- 机皇帝 神空∞ 31930787 sends 1 equipped monster to grave as cost to gain direct attack for the turn
- 机皇帝 神陆∞ 4545683 gains ATK and DEF equal to half your current LP and can special summon an equipped monster to your field in defense, stealing the Synchro as a real body
- 机皇帝 神智∞-同调吸收 30221870 during the opponent turn sends 1 face-up 机皇 monster you control to grave to special summon itself from hand, on summon makes one monster unable to attack, and can tribute itself to negate and destroy a destruction effect
- Deliberate self-destroy enablers: 机皇创出 39109382 effect two discards 1 and destroys 1 own monster, 机限爆弹 41475424 destroys 1 own 机皇 plus 1 opponent card, 混沌无限 4081825 destroys the monster it summoned at end phase
- 机皇枢 无限核 77710579 effect three and 根绝机皇神 2992036 effect one special summon 机皇帝 ignoring summoning conditions, the 无视召唤条件 trick, the only ways to summon an Emperor without the trigger
- Emperors and 机皇神 机录∞ 63468625 carry special summon condition value 0, so generic revival such as 死者苏生 83764718 or 混沌无限 4081825 cannot summon them, while 机皇神龙 三曲枝 4837861 and 星标 38522377 have only a revive limit and can be revived after proper summon

- **One-Card Combo: 机皇枢 无限核 77710579**

- Step 1: normal summon 机皇枢 无限核 77710579, effect one searches a 机皇 S/T from deck, take 机皇创出 39109382
- Step 2: activate 机皇创出 39109382, effect two discards 1 card and destroys 机皇枢 77710579
- Step 3: 机皇枢 77710579 effect three triggers on effect destruction and special summons 1 机皇帝 from hand or deck ignoring summoning conditions, with an attribute restriction so no face-up monster of the same attribute sits on your field, 神智∞ 68140974 is DARK, 神空∞ 31930787 is WIND, 神陆∞ 4545683 is EARTH
- Step 4: 机皇帝 神智∞ 68140974 ignition equips 1 opponent Synchro if present and gains its ATK, a 2500 body with a spell negate
- Step 5: 机皇创出 39109382 effect three triggers from 机皇枢's destruction and destroys 1 other face-up S/T on the field, ideally opponent backrow
- Step 6: 机皇创出 39109382 effect one on activation can first add a second 机皇 monster such as 机皇兵厂 助奏 3715284 or another 机皇帝
- Net result: one card into 机皇帝 plus spell negate plus S/T pop plus an extra monster in hand
- Alternative one-card line: 机皇兵厂 助奏 3715284 effect one destroys itself and special summons 2 机皇兵 from deck in defense with a Machine-only summon lock, then overlay into 我我我枪手 12014404 or 重装甲列车 铁狼 49121795

- **End Field**

- Standard end board: 机皇帝 神智∞ 68140974 equipped with an opponent Synchro, 机皇创出 39109382 face-up, one 机皇兵 body for the next turn, set 机限爆弹 41475424 or 混沌无限 4081825 or 根绝机皇神 2992036, and 机皇帝 神智∞-同调吸收 30221870 held in hand as the opponent-turn hand trap
- Turbo line from the 210717机皇 build: 名推理 58577036, 怪兽之门 43040603, 愚蠢的埋葬 81439173 and 左腕的代偿 86541496 dump 机皇 monsters, then 机皇神 机录∞ 63468625 special summons itself from hand by sending 3 机皇 from hand, a 4000 ATK body with Synchro steal and standby burn, and 根绝机皇神 2992036 effect one revives it from grave ignoring conditions
- Swarm line: 机皇兵厂 助奏 3715284 plus 机皇兵 field makes 3 plus 机皇 monsters, enabling 机皇神龙 星标 38522377 whose ATK becomes the total original ATK of the monsters it sends, for example 2500 plus 1800 plus 1600, with a 1000 burn on every Synchro summon
- 机皇城 67328336 field spell stops 机皇帝 from being targeted by Synchro monster effects and searches any 机皇帝 when destroyed

- **Extenders**

- 机皇兵厂 助奏 3715284: self-destroy to special summon 2 机皇兵 from deck in defense with a Machine-only lock, plus an end phase burn of 100 times your 机皇 count
- 机动要塞 极强音 86997073: field spell that special summons 1 机皇兵 from hand
- 机皇枢 无限核 77710579: searches a 机皇 S/T on summon, survives one battle destruction, and revives a 机皇帝 ignoring conditions when destroyed by effect, also acts as the third 机皇 body for 机皇神龙 星标 38522377
- 混沌无限 4081825: flips all defense monsters on both fields to attack, special summons 1 机皇 monster from deck or grave with negated effects, then destroys it at end phase, and that end phase destruction triggers a 机皇帝 from hand
- 根绝机皇神 2992036: effect one targets 3 机皇 in grave with different names and either adds all to hand or special summons all ignoring conditions with a Machine lock after, effect two banishes itself from grave while a 机皇神 is on field to destroy 1 opponent Synchro and burn its original ATK
- 再机动 85775486: shuffle 1 机皇 from hand into deck to add 1 机皇 from grave to hand
- 机皇兵 神空一型 75733063: when destroyed by battle, special summons 1 机皇兵 from deck
- 机皇帝的赐与 12986778: draw 2 when exactly 2 face-up monsters exist and both are 机皇, skipping the battle phase
- 钢铁抽卡 34559295: draw 2 when exactly 2 Machine effect monsters are on your field, after activation only 1 more special summon this turn so use it last
- Generic Machine tech seen in the deck folder: 同胞的牵绊 40450317, 一对一 2295440, 汪分之一机会！？ 51405049, 小世界现象 89558743, 强欲而金满之壶 49238328

- **Halt Points**

- 灰流丽 14558127 stops 机皇创出 39109382 effect one search, 机皇枢 无限核 77710579 search, and 机皇兵厂 助奏 3715284 effect one deck special summons
- 无限泡影 10045474 or 效果遮蒙者 97268402 on 机皇枢 77710579 keeps its destruction trigger from firing
- 墓穴的指名者 24224830 and 抹杀之指名者 65681983 banish grave 机皇, starving 根绝机皇神 2992036 targets and the three-different-names banish cost of 机皇神龙 三曲枝 4837861
- 增殖的G 23434538 punishes the swarm, 机皇兵厂 助奏 3715284 makes 2 bodies, 无限核 into 机皇帝 adds a third, 根绝机皇神 2992036 can add up to 3 more
- 原始生命态 尼比鲁 27204311 clears the 助奏 swarm and because tribute is not destruction no 机皇帝 trigger fires in compensation
- 冥王结界波 54693926 and 禁忌的一滴 24299458 negate the Emperor equip and spell negate, leaving 2500 plain bodies
- 机皇帝 神智∞ 68140974 only negates spell activations, it cannot answer trap or monster starts

- **Mirror Match**

- Emperors trigger only on your own monsters destroyed by effect, so destroying your own 机皇 with 机皇创出 39109382 effect two or 机限爆弹 41475424 never gifts the opponent an Emperor
- The mirror is a race to the first 机皇帝, whoever resolves 机皇枢 无限核 77710579 or 机皇创出 39109382 first dictates the board
- Sequence 机皇创出 39109382 carefully because an opposing 机皇帝 神智∞ 68140974 negates spell activations, open with the monster 机皇枢 77710579 instead
- With no Synchro targets the Emperors are plain beaters, 机皇帝 神陆∞ 4545683 scales with half your LP, 神空∞ 31930787 direct attacks, and 机皇神 机录∞ 63468625 standby burn closes games
- 混沌无限 4081825 flips both players defense monsters to attack, do not flip your own 机皇神龙 星标 38522377 or low ATK 机皇兵 into open attacks
- 机皇神龙 星标 38522377 burns the player who special summons a Synchro, so if you must Synchro in the mirror you take the 1000 yourself

- **Common Mistakes**

- Do not try generic revival for 机皇帝 68140974 31930787 4545683 or 机皇神 机录∞ 63468625, their summon conditions reject it, only 无视召唤条件 effects like 机皇枢 77710579 effect three and 根绝机皇神 2992036 effect one work
- The Emperor trigger needs destroyed by effect, sent to grave, and face-up, battle destruction, 原始生命态 尼比鲁 27204311 tribute, and banishment do not fire it
- 机皇帝 神智∞ 68140974 and 神空∞ 31930787 forbid your other monsters from attacking while face-up, do not stack attackers beside them
- 机皇帝 神陆∞ 4545683 halves its own stats as your LP drops, summon it early or protect LP with 神之恩惠 35346968 or it becomes a wall instead of a beater
- 机皇神 机录∞ 63468625 standby burn skips your battle phase, use it as a finisher, and its 3 机皇 from hand cost is heavy so dump it to grave and revive with 根绝机皇神 2992036 instead
- 机皇神龙 星标 38522377 sets its ATK once at summon from the monsters sent, send high original ATK 机皇帝 and 机皇兵, and remember its 1000 burn can hit you
- 机皇神龙 三曲枝 4837861 needs 3 different-named 机皇 in grave to banish, equips any extra deck monster at attack declare for ATK, but triple attacks only while the equipped card is a Synchro
- 机皇兵厂 助奏 3715284 effect one locks you to Machine-only special summons for the turn and summons in defense, do not follow it with a non-Machine engine
- 混沌无限 4081825 summons a monster with negated effects that self-destructs at end phase, it is an Emperor-trigger enabler and body, not a threat
- 铁壁机皇兵 59371387 negates the effects of your attack-position 机皇兵, a stall trap rather than a combo piece
- Sequence draw spells before extending, 机皇帝的赐与 12986778 skips the battle phase and 钢铁抽卡 34559295 caps special summons for the turn
