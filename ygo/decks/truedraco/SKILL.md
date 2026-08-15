---
name: truedraco-experience
description: 真龙 (True Draco) deck experience: continuous spell/trap tribute engine, reactive searches, floodgate lock
---
# 真龙 (True Draco) Deck Experience

- **Deck Identity**

- Control deck that tribute summons Level 5-8 真龙 monsters by tributing its own continuous spells and traps instead of monsters, then locks the opponent out with continuous floodgates
- Standard build (deck 250726真龙) runs 39 cards with an empty extra deck, which is a hard requirement for 帝王的熔击 48716527 and 真帝王领域 84171830
- Boss: 真龙剑皇 卓辉星·拼图 21377582, Level 8 2950/2950, quick destruction plus immunity based on what was tributed
- Tribute searchers: 真龙导士 威风凛·少女 95004025 (adds any 真龙 monster), 真龙战士 点火烈·炽热 22499034 (adds or activates a 真龙 continuous spell), 真龙拳士 雾动轰·铁拳 58984738 (adds or activates a 真龙 continuous trap), each triggers once per turn when the opponent activates any card effect but only while tribute summoned
- Continuous engine cards: 真龙凰的使徒 75425320, 真龙的继承 49430782 (spells), 真龙的默示录 61529473, 真龙皇的复活 35125879 (traps)
- Starters: 龙神阵·略图 13035077 (field spell, searches any 真龙 card), 龙呼双搏 66092596 (adds a 真龙 monster on activation)
- Floodgates: 次元的裂缝 81674782, 帝王的熔击 48716527, 休息一回 24348804, 技能抽取 82732705, 群雄割据 90846359, side options 虚无空间 5851097, 千查万别 24207889, 魔封的芳香 58921041, 王宫的敕命 61740673, 卡组封锁 1149109, 能力吸收石 67234805
- Draw and utility: 强欲而贪欲之壶 35261759, 增殖的G 23434538, 神之宣告 41420027, 迷彩光书签 52296675, side tech 列王诗篇 58053438

- **Core Mechanic: Continuous Spell/Trap Tribute Engine**

- Every 真龙 tribute monster is scripted with EFFECT_ADD_EXTRA_TRIBUTE: any continuous spell or trap on your own spell/trap zone is a legal tribute material instead of a monster, verified in scripts as targeting own LOCATION_SZONE continuous cards
- Tribute counts stay standard by level: Level 5-6 monsters need 1 tribute, 真龙剑皇 卓辉星·拼图 21377582 (Level 8) needs 2, 真龙机兵 十二炼机圣 57761191 needs 3
- 真龙凰的使徒 75425320 and 真龙的继承 49430782 have an ignition effect that tribute summons a 真龙 monster from hand without consuming your normal summon, tribute is still paid from your continuous cards
- 真龙的默示录 61529473 and 真龙皇的复活 35125879 have the same extra tribute summon as quick effects but only during the opponent's main phase, so the deck tribute summons on the opponent's turn
- 真龙的继承 49430782 draws cards equal to the number of different 真龙 card types (monster, spell, trap) sent from the field to the grave this turn, counting both players, implemented as a global type counter
- 真龙凰的使徒 75425320 shuffles 3 真龙 cards from your grave into the deck to draw 1, recycling spent tribute materials
- All four engine cards float when sent from the spell/trap zone to the grave: 真龙的继承 49430782 and 真龙凰的使徒 75425320 destroy a spell or trap on the field, 真龙的默示录 61529473 and 真龙皇的复活 35125879 destroy a monster
- 龙呼双搏 66092596 places a face-up 真龙 monster destroyed by battle or effect into your spell/trap zone as a continuous spell, recycling the monster into future tribute material
- 真龙剑皇 卓辉星·拼图 21377582 is unaffected by effects whose original card type matches the cards tributed for it, and its quick effect banishes 1 continuous card from your grave to destroy any other card on the field, once per turn on either turn

- **One-Card Combo: 龙呼双搏 66092596**

- Starter: 龙呼双搏 66092596 in hand, no other cards required
- Step 1: activate 龙呼双搏, its activation effect adds 真龙导士 威风凛·少女 95004025 from the deck to hand, a Level 5 monster needing only 1 tribute
- Step 2: tribute summon 威风凛·少女 with your normal summon, tributing the face-up 龙呼双搏 itself as the continuous spell tribute
- Step 3: pass, the moment the opponent activates any spell, trap, or monster effect, chain 威风凛·少女 to add any 真龙 monster from the deck, including 真龙剑皇 卓辉星·拼图 21377582
- End field: 真龙导士 威风凛·少女 95004025 with a reactive search armed, no other cards invested
- Two-card upgrade: open 真龙凰的使徒 75425320 or 真龙的继承 49430782 as well, use its extra tribute summon instead of the normal summon to put out 威风凛·少女, and with a second engine card chain another extra tribute summon to bring out 真龙剑皇 卓辉星·拼图 21377582 with 2 continuous tributes, ending on two tribute monsters
- 龙神阵·略图 13035077 line: destroy 1 card from hand or field (except itself) to search any 真龙 card, search 龙呼双搏 66092596 to start the same engine

- **End Field**

- 真龙剑皇 卓辉星·拼图 21377582 spell/trap-immune when tributed with 2 continuous cards, with one ready quick pop per turn fueled by banishing continuous cards from the grave
- A second tribute monster such as 真龙导士 威风凛·少女 95004025 keeping its reactive search armed for the opponent's turn
- One face-up engine card, 真龙凰的使徒 75425320 or 真龙的继承 49430782 for another tribute summon next turn, or 真龙的默示录 61529473 or 真龙皇的复活 35125879 activated face up during your turn so their quick tribute summons are live in the opponent's main phase
- Floodgate layer: 次元的裂缝 81674782, 帝王的熔击 48716527, 技能抽取 82732705, 群雄割据 90846359, set 神之宣告 41420027
- Grave stacked with continuous spells and traps as banish fuel for 真龙剑皇 21377582 pops and 真龙凰的使徒 75425320 recycle draws
- 龙神阵·略图 13035077 grants 300 ATK/DEF and one battle-destruction immunity per turn to each tribute summoned 真龙 monster while it stays face up

- **Extenders**

- 真龙导士 威风凛·少女 95004025 adds any 真龙 monster on opponent activation, the main route to 真龙剑皇 卓辉星·拼图 21377582 in mid-game
- 真龙战士 点火烈·炽热 22499034 adds or directly activates a 真龙 continuous spell mid-chain, grabbing 真龙凰的使徒 75425320 or 真龙的继承 49430782 without using your activation
- 真龙拳士 雾动轰·铁拳 58984738 adds or directly activates a 真龙 continuous trap mid-chain, grabbing 真龙的默示录 61529473 or 真龙皇的复活 35125879
- 真龙的继承 49430782 draw scales with 真龙 cards sent from the field this turn, so pop and float before drawing
- 真龙皇的复活 35125879 revives a 真龙 monster from your grave in defense, but locks you out of special summons until the end of the turn
- 真龙的默示录 61529473 destroys 1 other face-up 真龙 card you control to halve the attack and defense of every face-up monster the opponent controls, a tempo swing that also self-pops for float effects
- 真龙骑将 得律阿斯3世 94982447 (side option) makes your other 真龙 monsters untargetable and indestructible by opponent effects while face up, and summons a 真龙 from the deck when it leaves the field
- 迷彩光书签 52296675 (tech) draws a card by destroying itself from the pendulum zone, then special summons itself from the face-up extra deck as free tribute material, banishing itself when it leaves the field
- 帝王的熔击 48716527 keeps your tribute summoned monsters working while negating every non-tribute-summoned face-up monster, it requires an empty extra deck to activate and self-destroys at the end phase if no tribute summoned monster is on your field

- **Halt Points**

- 灰流丽 14558127 (Ash Blossom) on 龙呼双搏 66092596 or 龙神阵·略图 13035077 stops the one-card line, the remaining continuous spell is only tribute fodder
- 增殖的G 23434538 is a minor threat because the engine tribute summons instead of special summoning, only 真龙皇的复活 35125879 special summons, so play the full line under G
- 王宫的敕命 61740673 negates all spell effects on the field, your continuous spells stop working but can still be tributed for tribute summons
- 魔封的芳香 58921041 forces you to set spells first, blocking 龙呼双搏 66092596 and the continuous spell engines for a turn while the traps 真龙的默示录 61529473 and 真龙皇的复活 35125879 stay playable
- 虚无空间 5851097 blocks 真龙皇的复活 35125879 and stays alive longer under 次元的裂缝 81674782 because monsters are banished instead of sent to the grave
- 次元的裂缝 81674782 is double-edged, it kills 真龙皇的复活 35125879 revive since monsters are banished, while 真龙剑皇 21377582 pop fuel and 真龙凰的使徒 75425320 recycle still work because continuous cards reach the grave

- **Mirror Match: 真龙 vs 真龙**

- Search triggers fire only on opponent activations, whoever acts first gifts the other a search, so resolve your continuous spell effects before developing tribute monsters or force the opponent to activate first
- 真龙剑皇 21377582 quick pop versus quick pop is decided by chain order because both are monster effects regardless of tribute types, hold your pop for their pop
- Tribute 真龙剑皇 卓辉星·拼图 21377582 with 2 continuous cards in the mirror for spell and trap immunity, dodging the opponent's 真龙的默示录 61529473 halving and trap float destruction
- 帝王的熔击 48716527 decides the board, your tribute summoned monsters keep effects while the opponent's special summoned monsters are negated
- 次元的裂缝 81674782 hurts both sides' revives, popping it first or keeping it off is a real tempo line
- Whoever keeps more continuous cards face up controls the tribute summon count, use 真龙的默示录 61529473 and 真龙皇的复活 35125879 tribute summons during the opponent's main phase to out-develop them

- **Common Mistakes**

- Tributing away every continuous card kills the engine, keep at least one face-up 真龙凰的使徒 75425320, 真龙的继承 49430782, 真龙的默示录 61529473 or 真龙皇的复活 35125879 alive
- Forgetting tribute counts: 威风凛·少女 95004025, 点火烈·炽热 22499034 and 雾动轰·铁拳 58984738 need 1 tribute, 真龙剑皇 卓辉星·拼图 21377582 needs 2, 真龙机兵 十二炼机圣 57761191 needs 3, tribute summons via continuous card effects still pay the same counts
- 真龙剑皇 21377582 immunity follows what was tributed, tribute continuous cards to dodge spell and trap effects, tribute monsters such as two 威风凛·少女 95004025 to dodge 技能抽取 82732705 style monster negates
- Monsters placed by 真龙皇的复活 35125879 are special summoned, not tribute summoned, so their search triggers never activate, and the card locks your special summons for the rest of the turn, sequence it last
- 龙神阵·略图 13035077 needs a card to destroy from hand or field to search, never activate it without a target, keep a disposable card such as an extra copy or 增殖的G 23434538
- 帝王的熔击 48716527 and 真帝王领域 84171830 require an empty extra deck, never put 真龙机兵 十二炼机圣 57761191 or any extra deck monster into the main build
- Do not activate 卡组封锁 1149109 before your searches, it locks your own 龙神阵·略图 13035077 and 龙呼双搏 66092596 deck additions
- 真龙的默示录 61529473 cannot use its destroy-and-halve effect and its tribute summon in the same chain, the shared per-chain cost flag blocks the second activation
- 技能抽取 82732705 negates your own tribute monsters too, only pair it with 帝王的熔击 48716527 when 真龙剑皇 卓辉星·拼图 21377582 was tribute summoned with monsters for monster-type immunity, otherwise the lock is symmetric
