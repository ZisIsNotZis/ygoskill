---
name: shaddoll-experience
description: 影依 (Shaddoll) deck experience: flip engine, fusion from deck, one-card baseline, extenders, halt points
---
# 影依 (Shaddoll) Deck Experience

- **Deck Identity**

- Main deck is a flip-monster engine: every 影依 monster is a DARK Spellcaster flip monster (exceptions noted) that generates advantage both when flipped face-up and when sent to the graveyard by a card effect
- Core main monsters: 影依兽 3717252, 影依刺猬 4939890, 影依蜥蜴 30328508, 影依龙 77723643, 影依猎鹰 37445295, 影依猎犬 52551211, 影依巫女 艾莉娅儿 97518132, 影依的原核 4904633, 影灵之翼 文蒂 51023024
- Modern additions: 影依的炎核 虚梦狱 92079625, 影雄之烬 神子晶 95072744, and the searcher spell 炼狱的乖放 61345801
- Fusion spells and traps: 影依融合 44394295, 与神之假身的接触 6417578, 冻结之心映照的神影 34950192, 影依的伪典 21011044, 影光的圣选士 23912837
- Extra deck is attribute-specific El Shaddoll fusions: 神影依·拿非利 20366274, 神影依·米德拉什 94977269, 神影依·舍金纳迦 74822425, 神影依·神子晶 48424886, 神影依·七贤巨鲲魔 50907446, 神影依·异花莉莉丝 19261966, 神影依·文迪戈 74009824, 影灵翼骑 影文蒂 8852158, 神影依·米沙赫雷恶 32467459, plus the Link 影依·拿非利 86938484
- Partner engines in repo decks: 机怪虫 flip monsters feed the Link 影依·拿非利 86938484 (Link-2 requiring 2 flip monsters), 珠泪哀歌族/阿不思 builds splash 影依 fusion for the deck-material unlock

- **Core Mechanic: Flip and Grave Trigger Pair**

- Every main deck 影依 flip monster has two effects that share one count limit per copy per turn: the FLIP effect (when flipped face-up, e.g. by attack or by 影光的圣选士) and the grave effect (when sent to the graveyard by a card effect)
- Sent as fusion material by 影依融合 or 与神之假身的接触 counts as sent by card effect, so fusion summons chain a burst of grave effects; sent as Xyz material or by battle does not trigger them
- 影依兽 3717252: flip draw 2 then discard 1, grave draw 1
- 影依刺猬 4939890: flip add 1 影依 spell or trap from deck, grave add 1 影依 monster from deck (not itself)
- 影依蜥蜴 30328508: flip destroy 1 monster on the field, grave send 1 影依 card from deck to grave
- 影依龙 77723643: flip return 1 opponent card on the field to hand, grave destroy 1 spell or trap on the field
- 影依猎鹰 37445295: flip special summon 1 影依 monster from grave in face-down defense (not itself), grave special summon itself in face-down defense
- 影依猎犬 52551211: flip add 1 影依 card from grave to hand, grave change 1 monster's battle position and non-影依 flip effects do not activate
- 影依巫女 艾莉娅儿 97518132: flip special summon 1 banished 影依 monster in defense, grave banish up to 3 cards from either graveyard
- 影灵之翼 文蒂 51023024: flip special summon 1 影依 monster from deck in face-up or face-down defense, grave special summon 1 影依 monster from deck in face-down defense
- 影依的原核 4904633 is a continuous trap that summons itself as a Level 9 DARK Spellcaster 1450/1950 monster, counts as the listed attribute material for El Shaddoll fusion, and recurs a 影依 spell or trap from grave when sent by effect

- **Core Mechanic: Fusion from Deck**

- 影依融合 44394295 is a normal spell, once per turn: fusion summon a 影依 fusion using hand and field monsters; if the opponent controls a monster special summoned from the extra deck, monsters from your deck may also be used as material
- The deck-material unlock is the deck's signature play: two 影依 cards in deck become a fusion monster plus multiple grave triggers in one activation
- 影依的伪典 21011044 is a continuous trap, once per turn quick effect during either player's main phase: fusion summon using your field and grave monsters as material by banishing them, then send 1 opponent face-up monster with the same attribute as the fusion monster to the grave; the fusion monster cannot attack directly
- 与神之假身的接触 6417578 is a quick-play spell, once per turn: fusion summon using hand and field monsters only
- 冻结之心映照的神影 34950192 is a continuous spell: on activation send 1 fusion monster from your extra deck to the grave, then once per turn tribute a fusion monster on your field to special summon a 影依 fusion with a different attribute from the extra deck as a fusion summon with 0 ATK; both effects lock you to only special summoning 影依 from the extra deck that turn
- Fusion material formula, verified in procedure.lua: each El Shaddoll fusion needs exactly 1 影依 monster plus 1 monster of the listed attribute (拿非利 light, 米德拉什 dark, 舍金纳迦 earth, 神子晶 fire, 异花莉莉丝 water, 文迪戈 wind); 七贤巨鲲魔 50907446 needs 2 影依 monsters with different attributes; 米沙赫雷恶 32467459 needs 影依 plus dark plus earth
- 影依的原核 4904633 as a fusion material substitutes for the attribute requirement, which is why it is the glue that makes any 影依 fusion live

- **One-Card Combo: 影依融合 44394295**

- Honest baseline: 影依 has no unconditional one-card starter; this combo needs one extra card in deck as the attribute material and an opponent monster special summoned from the extra deck to unlock deck materials
- Starter: 影依融合 44394295 in hand, opponent controls any extra-deck-summoned monster
- Step 1: activate 影依融合, choose 影依刺猬 4939890 and 赫之圣女 卡尔特西娅 95515789 (light) from the deck as material, fusion summon 神影依·拿非利 20366274
- Step 2: 影依刺猬 sent as material triggers its grave effect, add 1 影依 monster from deck to hand, for example 影依兽 3717252 or 影依蜥蜴 30328508 for the next fusion
- Step 3: 神影依·拿非利 special summon effect sends 1 影依 card from deck to grave, mill 影依蜥蜴 30328508
- Step 4: 影依蜥蜴 grave effect sends another 影依 card from deck to grave, mill 影依猎鹰 37445295
- Step 5: 影依猎鹰 grave effect special summons itself in face-down defense, a flip threat for next turn
- End state: 神影依·拿非利 2800 ATK on field, 1 影依 monster added to hand, 1 影依 in hand from 刺猬 search, 2 影依 monsters in grave, 影依猎鹰 set face-down
- Variant material 影依兽 3717252 instead of 刺猬 draws a card and drops one hand card when it hits the grave
- Halt point: 灰流丽 14558127 chained to 影依融合 negates the whole line including every grave trigger, the single most effective interruption against the deck

- **End Field**

- 神影依·米德拉什 94977269 is the classic floodgate: while on field both players can only special summon once per turn, and it cannot be destroyed by opponent card effects
- 影依的伪典 21011044 set behind 米德拉什 is the opponent-turn threat: fuse 米德拉什 plus a grave 影依 into a second fusion during the opponent's main phase and send an opponent monster to the grave
- Graveyard setup with 影依刺猬, 影依蜥蜴, 影依猎鹰 and one 影依 spell or trap ready for 神影依·拿非利 recursion gives follow-up on every turn
- Modern tower end field: 神影依·米沙赫雷恶 32467459 immune to opponent activated spells and traps and to effects of monsters with lower level or rank, with an 800 LP search for a 影依 or 炼狱 spell or trap each turn
- 神影依·异花莉莉丝 19261966 as a floodgate alternative blocks both players from special summoning from hand or grave by spell or trap effects, shutting down 影光的圣选士 and most revival plays

- **Extenders**

- 影依的伪典 21011044: the opponent-turn fusion engine, also a removal tool through the same-attribute send
- 影光的圣选士 23912837: normal trap, effect one revives a 影依 from grave in defense, grave effect banishes itself plus 1 影依 from grave to flip one of your face-down monsters face-up or set one of your face-up monsters face-down
- 影灵翼骑 影文蒂 8852158: quick effect flips all face-down monsters on the field face-up, triggering every 影依 flip effect, then may set that many other face-up monsters face-down as disruption
- 影灵之翼 文蒂 51023024: chains a deck special summon from both its flip and grave effects, flooding the field for the Link 影依·拿非利 86938484
- 数学家 41386308: normal summon sends any Level 4 or lower monster from deck to grave, triggering 影依刺猬, 影依蜥蜴, 影依猎鹰 or 影灵之翼 文蒂 on summon
- 愚蠢的埋葬 81439173: mills 影依猎鹰 37445295 from deck for a free face-down revival
- 影雄之烬 神子晶 95072744: flip copies a non-rock 影依 monster's flip effect from grave, and when sent to the grave by an effect fuses using your hand, field and grave monsters as banished material
- 炼狱的乖放 61345801: reveal 1 影依 card from hand to add 2 影依 cards of different card types from deck, then discard 1
- 与神之假身的接触 6417578: quick-play fusion for reaction plays on the opponent's turn without the extra deck unlock

- **Halt Points**

- 灰流丽 14558127 on 影依融合 44394295 negates the activation and every chained grave effect
- 灰流丽 on 数学家 41386308 or on 影依刺猬 4939890 grave search cuts the resource engine
- 墓穴的指名者 24224830 or 屋敷童 73642296 on the grave trigger chain stops 影依猎鹰 37445295 revival and 影依兽 3717252 draw
- 无限泡影 10045474 on 影依·拿非利 86938484 ignition fusion or on 影雄之烬 神子晶 95072744 before its grave effect resolves
- Graveyard disruption like banishing 影依 monsters cuts 影依的伪典 21011044 materials and 影光的圣选士 23912837 costs
- Destroying face-down 影依 monsters with card effects avoids their flip effects, though their grave effects still fire because they were sent by a card effect
- 神之宣告 41420027 on 影依的原核 4904633 activation stops the attribute-substitute monster, and 神之密告 78114463 or 红色重启 23002292 stop 影依的伪典

- **Mirror Match: 影依 vs 影依**

- Whoever resolves 影依融合 44394295 first chains more grave triggers and wins the value race, so 灰流丽 14558127 is the mirror's decisive card
- 神影依·米德拉什 94977269 locks both players to one special summon, so whoever lands it first freezes the opponent's follow-up fusions
- 影依猎犬 52551211 grave effect flips an opponent's face-down 影依 face-up and triggers its flip effect for the opponent, so use it on your own set monsters or to force position changes, never as a free gift in the mirror
- 神影依·异花莉莉丝 19261966 blocks spell and trap revival including 影光的圣选士 23912837, but not 影依·拿非利 86938484 which revives itself by its own monster effect
- 影依的原核 4904633 decides which fusions are live through its attribute substitute, so removing the opponent's 原核 from play or grave is priority
- 神影依·米沙赫雷恶 32467459 is the mirror's tower, only removable by battle or by a higher-level monster effect

- **Common Mistakes**

- Setting 影依 monsters face-down without a flip enabler and passing, handing the opponent a free turn to remove them
- Forgetting 影依融合 44394295 deck materials need an opponent extra-deck-summoned monster, activating it with only hand and field materials when you could wait or use 与神之假身的接触 6417578 instead
- Making 神影依·米德拉什 94977269 and then continuing to special summon, since 米德拉什 limits both players to one special summon per turn
- Activating 影依的伪典 21011044 on your own turn when you need to attack, the fusion monster it summons cannot attack directly
- Searching traps like 影依的伪典 21011044 or 影光的圣选士 23912837 with 影依刺猬 4939890 and trying to use them the same turn, traps cannot activate the turn they are set
- Using 冻结之心映照的神影 34950192 and then planning link or other extra deck plays, the 影依-only-from-extra restriction applies the whole turn
- Using 影光的圣选士 23912837 grave effect and banishing 影依的原核 4904633 that is still needed as the attribute substitute material
- Forgetting 神影依·拿非利 20366274 destroys any special-summoned monster it battles, attack into special-summoned beaters instead of avoiding them
- Forgetting the shared count limit, each 影依 flip monster can use only one of its two effects per copy per turn
- Activating 影依兽 3717252 flip effect without enough deck to draw two cards, or 神影依·七贤巨鲲魔 50907446 grave search with a full hand, both force a discard or fizzle
