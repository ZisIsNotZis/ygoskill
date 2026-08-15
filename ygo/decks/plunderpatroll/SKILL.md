---
name: plunderpatroll-experience
description: 海造贼 (Plunder Patroll) deck experience: attribute tag-out mechanic, one-card combo, extenders, halt points
---
# 海造贼 (Plunder Patroll) Deck Experience

- **Deck Identity**

- WATER Fiend archetype of five Level 4 main-deck sailors that "tag out" into an extra-deck fleet of attribute-tagged ships, then tag back into sailors
- Main deck: 蓝胡子海技士 55349375, 红胡子航海士 68769900, 黑翼水先人 91642007, 白胡子机关士 31374201 (Tuner), 金头发训练生 81344070 (Tuner)
- Extra deck ships, one per attribute: 双翼之光照号 18832779 (Fusion, Level 8 LIGHT), 豪速之烈火号 94253655 (Synchro, Level 8 FIRE), 庄重之大地号 85969517 (Pendulum Synchro, Level 8 EARTH, Scale 1), 静寂之暗夜号 20248754 (Xyz, Rank 4 DARK), 黑胡子船长 67647362 (Link-2 WATER)
- Support: 进水式 44227727 (Fusion Spell), 据点 93031067 (Field), 象征 80621422 (Equip), 大航海 20426176 (Continuous Trap), 祝宴 43004235 (Normal Trap), 夸示 17016131 (Continuous Trap), 海造贼衍生物 85969518 (token)
- All cards share setcode 0x13f; the main monsters have no on-summon search, searching comes from 据点 93031067 and the ships' removal effects

- **Core Mechanic: Attribute Tag-Out**

- 红胡子航海士 68769900 and 白胡子机关士 31374201 have a quick effect, only during the opponent's turn, that reads the union of attributes of the opponent's face-up monsters and their GY monster cards
- The effect Special Summons 1 海造贼 ship from your extra deck whose attribute is in that union, then equips the activating sailor to the ship, so the opponent's attributes pick your ship for you
- The taggable ships cover FIRE 豪速之烈火号 94253655, DARK 静寂之暗夜号 20248754, LIGHT 双翼之光照号 18832779, EARTH 庄重之大地号 85969517, and the tag-out needs a free Spell/Trap Zone for the equip plus a free Extra Monster Zone or link arrow for the ship
- 黑胡子船长 67647362 (Link-2, 2 monsters including at least 1 海造贼) tags out as a quick effect on any turn: target 1 face-up Effect monster you control, Special Summon a matching ship, equip the target to it, draw 1
- 象征 80621422 (Equip Spell, +500 ATK, cannot be targeted by opponent effects) tags out with the reverse read: send itself to GY to Special Summon a ship whose attribute matches a face-up monster or GY monster on either side, then equips the monster it was equipped to
- An equipped sailor sits in the Spell/Trap Zone as an Equip Card and unlocks the ship's quick removal, which the same ship lacks while bare: 豪速之烈火号 94253655 discards 1 海造贼 to banish an opponent Spell/Trap then search a 海造贼 monster; 静寂之暗夜号 20248754 discards 1 海造贼 to banish an opponent face-up Effect monster then search a 海造贼 Spell/Trap; bare ships use the same effect as an ignition in your Main Phase only
- 静寂之暗夜号 20248754 additionally detaches 1 material to protect a face-up 海造贼 monster you control from destruction
- 双翼之光照号 18832779 tags back in the Main Phase: Special Summon 1 face-up 海造贼 monster from your Spell/Trap Zone or hand, and its other quick effect discards 1 海造贼 to negate and destroy an opponent's monster effect activation, then adds 1 海造贼 card from deck to hand if it is equipped
- 庄重之大地号 85969517 (Pendulum Scale 1) pendulum effect shuffles itself to the extra deck and creates 2 海造贼衍生物 85969518 tokens, one for each player, with an attribute you announce — the token you give the opponent is the attribute you tag into
- 庄重之大地号 85969517 monster effects: when the opponent Special Summons a monster, add 1 海造贼 card from deck to hand and, if it is equipped, also Special Summon 1 海造贼 monster from deck; its ignition adds 1 海造贼 card from GY to hand and moves itself to the Pendulum Zone
- 大航海 20426176 (Continuous Trap) quick effect changes one opponent monster's attribute to an announced one and revives 1 海造贼 monster from your GY, the deck's attribute fixer

- **One-Card Combo: 金头发训练生 81344070**

- Step 1: activate 金头发训练生 81344070 from hand, send 白胡子机关士 31374201 from hand to GY as cost, Special Summon 金头发 (Level 4 Tuner)
- Step 2: 白胡子机关士 31374201 GY trigger Special Summons 红胡子航海士 68769900 from deck, then locks you to 海造贼-only Special Summons until the End Phase
- Step 3: Synchro 金头发 + 红胡子 into 豪速之烈火号 94253655 (Level 8 FIRE)
- Step 4: 烈火号 ignition, discard 1 海造贼 card such as 蓝胡子海技士 55349375 as cost, banish 1 opponent Spell/Trap, then add 1 海造贼 monster from deck to hand such as 黑翼水先人 91642007
- Step 5: 蓝胡子海技士 55349375 discarded from hand triggers to discard 1 more card and draw 1
- Result: 烈火号 94253655 on board, one opponent backrow banished, one 海造贼 monster searched, one extra draw

- **End Field**

- One-card: 豪速之烈火号 94253655 plus one banished backrow, one search, one draw — a removal-plus-resource board, not a negate board
- Two-card 金头发训练生 81344070 + 黑翼水先人 91642007: 黑翼 summons itself and recycles a 海造贼 from GY, Xyz 红胡子航海士 68769900 + 黑翼 into 静寂之暗夜号 20248754 keeping 金头发 as Tuner, then 暗夜号 ignition banishes an opponent face-up Effect monster and searches a 海造贼 Spell/Trap such as 象征 80621422 or 大航海 20426176
- Two-card 金头发训练生 81344070 + 据点 93031067: 据点 discards 1 and searches 蓝胡子海技士 55349375, ending on 烈火号 94253655 plus 蓝胡子 and one search
- Full board with setup: 黑胡子船长 67647362 with an equipped ship such as 静寂之暗夜号 20248754, 据点 93031067 active, 大航海 20426176 or 祝宴 43004235 or 夸示 17016131 set — attribute-responsive interruption plus draw value

- **Extenders**

- 据点 93031067 (Field Spell) is the searcher: discard 1, add any 海造贼 card except itself from deck; every face-up 海造贼 card in your Spell/Trap Zone (equipped sailors and face-up 海造贼 traps included) gives your monsters +500 ATK; its GY effect bounces a face-up 海造贼 card from your Spell/Trap Zone to hand and Sets itself from GY, recycling equipped sailors
- 蓝胡子海技士 55349375 Special Summons itself from hand while another face-up 海造贼 monster is on field and draws on discard
- 黑翼水先人 91642007 from hand: Special Summon itself and add 1 海造贼 monster from GY to hand, then lock to 海造贼-only summons; when sent to GY from hand or field it Special Summons 1 海造贼 monster from your Spell/Trap Zone in Defense
- 金头发训练生 81344070 from GY: discard 1, Special Summon itself, then lock to 海造贼-only summons
- 进水式 44227727 Fusion Summons 双翼之光照号 18832779 from exactly 2 海造贼 monsters on the field, and its GY effect banishes itself to equip 1 海造贼 monster or 象征 80621422 from deck to a face-up 海造贼 monster
- 祝宴 43004235 draws 1 plus 1 per face-up Equip Card you control (equipped sailors count as Equip Cards) then shuffles that many back from hand; in GY it equips itself to a 海造贼 you Special Summon from the extra deck for +500 ATK
- 夸示 17016131 draws 1 when a face-up 海造贼 monster destroys by battle, and its quick effect sends itself to GY to make the opponent draw 1 then discard a monster, or send 1 card from their extra deck to GY
- 刻魔 engine in recent builds (刻魔的镇魂棺 2463794, 刻魔的大圣棺 49867899, 刻印群魔的刻魔锻冶师 60764609, 刻魔 落泪之日 46640168, 刻魔 震怒之日 82135803, 刻魔的赞圣 35552985) supplies LIGHT Fiend bodies that feed 象征 80621422 tag attributes and 烈火号 94253655's Fiend ATK boost
- 耀圣 engine (耀圣之花诗 卢西娜 13597785 FIRE, 耀圣之波诗 狄娜 59581480 WATER, 耀圣之月诗 福尔图娜 85976588 LIGHT, 耀圣诗之狱神精 12375297) supplies FIRE and LIGHT bodies for tag-outs
- 勇者 engine (阿拉弥赛亚之仪 3285551, 圣殿的水遣 30680659, 命运之旅路 39568067, 流离的狮鹫骑手 2563463) supplies a WIND negate and free bodies for 黑胡子船长 67647362

- **Halt Points**

- 灰流丽 14558127 hits 金头发训练生 81344070, 据点 93031067's search, and 白胡子机关士 31374201's GY deck summon, which is the second activation in the one-card line
- 墓穴的指名者 24224830 on 白胡子机关士 31374201 in GY kills the one-card line; 屋敷童 73642296 covers the other GY effects and 小丑与锁鸟 94145021 covers 据点 93031067
- 增殖的G 23434538 punishes every tag-out and ship summon; 原始生命态 尼比鲁 27204311 clears the whole tag-out board
- Structural halt: tag-out needs a matching attribute among the opponent's face-up monsters or GY monsters, so an empty or single-attribute board with no ship attribute stalls the engine
- Tag-out also needs a free Spell/Trap Zone for the equip and a free Extra Monster Zone or link arrow for the ship
- 大航海 20426176 destroys itself in the End Phase if you control no face-up 海造贼 monster
- 三战之才 25311006 and 禁忌的一滴 24299458 answer the ships' quick removals

- **Mirror Match**

- Both sides' tag-outs read the OPPONENT's attributes, so the mirror is an attribute war: exposing LIGHT/FIRE/DARK/EARTH cards hands the other player the same tag keys
- The WATER sailors alone grant no ship attribute, so a board of only sailors cannot be tagged into; 庄重之大地号 85969517 tokens and engine bodies (刻魔 LIGHT, 耀圣 FIRE/LIGHT) open the tag axis for both players
- 庄重之大地号 85969517's pendulum effect is double-edged: the token it gives the opponent is exactly the attribute they need to tag into your ships
- 大航海 20426176 decides the mirror: changing an opponent monster to FIRE/DARK/LIGHT/EARTH lets you tag the matching ship, and both players can do it to each other
- 黑翼水先人 91642007 recycling 海造贼 from GY matters because GY monster attributes count for tag-outs — recycle to keep your attribute pool and strip theirs
- Whoever resolves 黑胡子船长 67647362 first gains a tag, an equip, and a draw, so fight for the first Link-2
- 夸示 17016131's hand dump can strip the opponent's second 白胡子机关士 31374201 before its GY summon can fire

- **Common Mistakes**

- 红胡子航海士 68769900 and 白胡子机关士 31374201 tag-outs work only during the opponent's turn — on your own turn use 黑胡子船长 67647362 or 象征 80621422
- Forgetting the tag-out also reads the opponent's GY: GY monster cards count, face-down monsters and Spell/Traps contribute no attribute
- 豪速之烈火号 94253655 and 静寂之暗夜号 20248754 removal is quick only while equipped with a face-up 海造贼 card; a bare ship is an ignition-only Main Phase play
- 象征 80621422 matches attributes on either side's field or GY, so a lone WATER board cannot activate it — include LIGHT/FIRE/DARK/EARTH bodies or 庄重之大地号 85969517 tokens
- 黑翼水先人 91642007, 白胡子机关士 31374201 and 金头发训练生 81344070 GY effects lock you to 海造贼-only Special Summons for the turn, so resolve non-archetype summons first
- 大航海 20426176 cannot revive a ship that was tag-out summoned without its proper Synchro/Xyz/Fusion procedure — such a ship can only be shuffled back to the extra deck
- 进水式 44227727 needs exactly 2 海造贼 monsters on the field to fuse 双翼之光照号 18832779, so do not activate it on an empty board
- Equipped sailors' "sent to GY" effects fire only from the hand or Monster Zone — a sailor destroyed while equipped in the Spell/Trap Zone does NOT trigger 蓝胡子海技士 55349375's draw or 白胡子机关士 31374201's deck summon
- 祝宴 43004235 shuffles back as many cards as it drew extra, so check hand size before activating
- 双翼之光照号 18832779 tag-back is Main Phase only, and its negate discards a 海造贼 card as cost
- Tag-out needs a free Spell/Trap Zone for the equip, so a full backrow locks the mechanic
- Protect 白胡子机关士 31374201 and 金头发训练生 81344070, the only Tuners, or the Level 8 Synchros 豪速之烈火号 94253655 and 庄重之大地号 85969517 become unreachable
