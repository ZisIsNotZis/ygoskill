---
name: tenpai-deck-experience
description: 天杯龙 (Tenpai) deck experience: battle-phase synchro OTK engine, one-card combo, extenders, halt points
---
# 天杯龙 (Tenpai) Deck Experience

- **Deck Identity**

- Going-second Battle Phase Synchro OTK deck, top-tier in 2024-25, that wins by resolving a battle-phase synchro swarm on its own turn instead of building a turn-one board, 40 main / 15 extra
- Main deck engine monsters are all FIRE Dragon with 天杯龙 setcode 0x1aa: 天杯龙 白龙 39931513, 天杯龙 中龙 91810826, 天杯龙 发龙 65326118, 幻禄之天杯龙 23657016 (this client cards.cdb is a July-2024 pool, the later OCG 林鸟/辉光 prints are absent, use the four names above)
- Extra deck Tenpai synchros have 灿幻 setcode 0x1a9: 灿幻升龙 双叉戟龙军王 82570174, 灿幻超龙 三超戟龙军王 18969888, plus the generic 三叉戟龙军王 39402797
- Spells and traps: 灿幻开门 66730191 three copies, 杯满的灿幻庄 30336082, 星球改造 73628505, 金满而谦虚之壶 84211599; 灿幻开花 25388971 and 灿幻封炉 55484152 are archetype options not played in this build
- Searchers and bodies: 龙宝龙 11590299, 深渊之兽 玛格巨龙 33854624
- Hand traps and interaction: 灰流丽 14558127, 增殖的G 23434538, 幽鬼兔 59438930, 效果遮蒙者 97268402, 尼比鲁 27204311, 次元吸引者 91800273, 欢聚友伴·茸茸长尾山雀 42141493, 灵王的波动 40366667, 无限泡影 10045474
- 主动撞针龙 73539069 in the extra list searches 旋转引导扇区 and needs 弹丸 monsters the main deck does not play, treat it only as an emergency Link-1 climb material

- **Core Mechanic: Battle-Phase Synchro Engine**

- Every main deck Tenpai monster has a once-per-turn Quick Effect, activatable during either player's Battle Phase, that Synchro Summons using itself plus your other monsters, verified in scripts as phase between battle start and battle end, with a per-card counter so several monsters can each synchro once per turn
- 天杯龙 中龙 91810826 is a Level 4 Tuner: it Special Summons itself from hand while you control a FIRE Dragon, and when an attack is declared it Special Summons a Level 4 or lower FIRE Dragon from deck, never another 中龙, making it the deck-Summon generator
- 天杯龙 发龙 65326118 revives a Level 4 or lower FIRE Dragon from your graveyard on its own summon or at an attack declaration, and while on field your FIRE Dragons cannot be destroyed by battle
- 天杯龙 白龙 39931513 adds a 灿幻 Spell or Trap from deck to hand or sets it on summon, makes your FIRE Dragons deal no battle damage to you, and its battle-phase synchro starts the climb
- 幻禄之天杯龙 23657016 Special Summons itself as a Tuner when an effect adds it to hand not by drawing, optionally raising its Level by 1, and can tribute itself as a Quick Effect to Special Summon another 天杯龙 from deck, after which you can only Special Summon Dragons until end of turn
- 灿幻开门 66730191 is a Quick-Play, once per turn: outside the Battle Phase choose one mode, add a Level 4 or lower FIRE Dragon from deck to hand or Special Summon a FIRE Dragon from hand, inside the Battle Phase both modes resolve
- The engine attacks first to trigger battle-start effects, then re-synchros with the generated monsters every Battle Phase and finishes under 灿幻超龙 which locks the opponent out of Battle Phase effects

- **One-Card Combo: 天杯龙 白龙**

- Starter: 天杯龙 白龙 39931513 alone in hand against any opponent field
- Step 1: Normal Summon 白龙, its effect searches 灿幻开门 66730191 and adds it to hand, never sets it
- Step 2: enter Battle Phase and activate 灿幻开门, both modes apply: add 天杯龙 中龙 91810826 from deck to hand, then Special Summon it from hand
- Step 3: declare an attack with 中龙, at battle start its effect Special Summons 天杯龙 发龙 65326118 from deck, the 1500 attack resolves
- Step 4: 中龙 battle-phase synchro using itself and 发龙 into 灿幻升龙 双叉戟龙军王 82570174
- Step 5: 灿幻升龙 revives 中龙 from graveyard and locks you to Dragon-only Special Summons for the rest of the turn
- Step 6: attack with 灿幻升龙 for 2600, then with the revived 中龙 for 1500, reaching three attack declarations this turn
- Step 7: 白龙 battle-phase synchro using itself and 灿幻升龙, a Level 7 Tuner, into 灿幻超龙 三超戟龙军王 18969888: all monsters change to Attack Position, opponent monsters must attack, and the opponent cannot activate effects during the Battle Phase
- Step 8: attack with 灿幻超龙 for 3000, total 1500 plus 2600 plus 1500 plus 3000 equals 8600, lethal

- **End Field**

- OTK board is 灿幻超龙 18969888 at 3000 ATK with its must-attack and Battle Phase effect lock plus every surviving attacker, and after the third attack declaration 灿幻升龙 82570174 and 灿幻超龙 can each revive from the graveyard once per duel as extra attackers
- Damage stack: 灿幻升龙 82570174 2600, 灿幻超龙 18969888 3000, 三叉戟龙军王 39402797 3000 up to three attacks, 异色眼陨火龙 80696379 2500, 鬼动武者 40509732 2600, 电光赛道名将 33158448 2100 at Level 7, 月华龙 黑蔷薇 33698022 2400, 黑蔷薇龙 73580471 2400, 鲜花女男爵 84815190 3000
- Defensive board when the OTK is stopped: 灿幻超龙 18969888 plus 天球之圣刻印 24361622 which once per opponent turn tributes a monster to bounce a face-up card and then Special Summons a Dragon from deck with 0 ATK and DEF, plus 鲜花女男爵 84815190 for one omni-negate and the hand traps 灵王的波动 40366667 and 无限泡影 10045474
- 杯满的灿幻庄 30336082 protects your FIRE Dragons from opponent activated effects during your Main Phase 1 and doubles a Dragon Synchro's ATK if destroyed during the Battle Phase, combine it with 三叉戟龙军王 self-destroy for a 6000 ATK multi-attacker

- **Extenders**

- 天杯龙 中龙 91810826 battle-start deck Special Summon and 天杯龙 发龙 65326118 battle-start graveyard revival are the repeatable Battle Phase extenders, and each generated monster can still attack and synchro once that turn
- 幻禄之天杯龙 23657016 comes out for free as a Tuner when searched by 杯满的灿幻庄 30336082 or 灿幻开门 66730191, at Level 4 after its level-up it makes 灿幻升龙 with 白龙 or 发龙, and its tribute effect can fetch 中龙 from deck mid-Battle Phase
- 三叉戟龙军王 39402797 on Synchro Summon destroys up to two other cards you control and gains one extra attack per card destroyed, only Synchro Summonable and never revivable, destroying 杯满的灿幻庄 in the Battle Phase doubles its ATK
- 龙宝龙 11590299 on Normal Summon adds any Level 4 or lower FIRE Dragon from deck, an extra starter that does not consume 灿幻开门
- 灼热之火灵使 希塔 48815792 is a Link 2 that Special Summons a FIRE monster from the opponent graveyard to your zone it points to for link climbing
- 灿幻开花 25388971 as an option ends your Main Phase when the opponent controls more monsters and all yours are FIRE Dragon, fast-forwarding into the Battle Phase, and after three attacks its graveyard effect draws one card and Special Summons any number of 天杯龙 from hand
- 灿幻封炉 55484152 as an option revives monsters your FIRE Dragons destroy by battle in Defense Position and in the opponent End Phase pays 1000 LP to set a 灿幻 Spell or Trap from graveyard, cards set this way are banished if they leave the field

- **Halt Points**

- 灰流丽 14558127 stops the starter by negating 灿幻开门 66730191 activation, 天杯龙 白龙 39931513 search, or 天杯龙 中龙 91810826 self-Special Summon
- 效果遮蒙者 97268402 and 无限泡影 10045474 hit the on-field search, revival, and synchro effects, 杯满的灿幻庄 30336082 shields your FIRE Dragons only during your Main Phase 1 so Battle Phase plays are unprotected
- 幽鬼兔 59438930 destroys any monster whose effect activates on the field, 白龙 39931513 search, 中龙 91810826 battle-start Summon, 发龙 65326118 revival, the battle-phase synchro effects, or the 灿幻升龙 82570174 revival, and also any face-up Spell or Trap effect like the 杯满的灿幻庄 30336082 search
- 尼比鲁 27204311 arrives at the fifth Special Summon, make 灿幻超龙 before the fifth summon because its Battle Phase lock then forbids 尼比鲁 entirely
- 增殖的G 23434538 and 欢聚友伴·茸茸长尾山雀 42141493 tax every Special Summon, under either card keep the summon count minimal or lose the card advantage war
- 次元吸引者 91800273 from either side turns graveyard-bound cards into banished ones and kills 天杯龙 发龙 65326118 revival, 灿幻升龙 revival, and the three-attack graveyard recursion, switch to deck Summon lines from 中龙 instead
- 灵王的波动 40366667 negates any effect that includes a Special Summon, it answers 灿幻开门, 中龙 self-Summon, and the battle-phase synchro Quick Effects themselves, and also stops the opponent starters when you hold it
- 无限泡影 10045474 from hand and 效果遮蒙者 97268402 are the cheapest stops on the battle-phase synchro before 灿幻超龙 lands

- **Mirror Match**

- Both sides are the same going-second OTK so the duel is decided by hand-trap trading on the starters, 灰流丽 14558127 against 灿幻开门 66730191 and 天杯龙 白龙 39931513 searches, 灵王的波动 40366667 against 开门 and the battle-phase synchro effects
- 次元吸引者 91800273 is the strongest mirror card, the first player to resolve it with an empty graveyard shuts down the opponent 发龙 and 灿幻升龙 recursion, sequence discards so your own graveyard stays empty when needed
- Whoever lands 灿幻超龙 三超戟龙军王 18969888 in the Battle Phase first wins because its lock blocks the opponent 灵王的波动, 无限泡影, and monster hand traps for the rest of the Battle Phase and forces their monsters to attack into it
- 欢聚友伴·茸茸长尾山雀 42141493 needs an empty field to activate, in the mirror keep it for turn one and do not expect it after monsters are out
- Do not use 金满而谦虚之壶 84211599 on the OTK turn because it halves all damage the opponent takes that turn and turns lethal into non-lethal
- 幽鬼兔 59438930 destroys the opponent 杯满的灿幻庄 30336082 on its search activation and removes their Main Phase 1 protection before they extend safely, and also punishes any on-field monster effect they activate

- **Common Mistakes**

- 灿幻开门 66730191 is once per turn per name so the 白龙-searched second copy cannot activate the same turn, use the 白龙 39931513 search for 杯满的灿幻庄 30336082 or hold it
- Never set 灿幻开门 from 白龙 search, a Quick-Play set this turn cannot activate this turn, always add it to hand
- 杯满的灿幻庄 30336082 protection exists only during your Main Phase 1, your monsters are fully vulnerable during the Battle Phase OTK
- Do not plan on 灿幻升龙 and 灿幻超龙 three-attack graveyard revival under 次元吸引者 91800273, everything is banished instead
- 三叉戟龙军王 39402797 must be Synchro Summoned, never revived, and its extra attacks count only cards it actually destroyed, destroy two targets for the full three attacks
- The Dragon-only locks of 幻禄之天杯龙 23657016 tribute effect and 灿幻升龙 82570174 forbid non-Dragon Special Summons for the rest of the turn, make 天球之圣刻印 24361622, S：P小夜骑士 29301450, 鲜花女男爵 84815190, and 赐炎之咎姬 2772337 before triggering them or skip them
- 灵王的波动 40366667 activated from hand forbids your LIGHT, EARTH, and WIND monster effects for the whole duel, 鲜花女男爵 84815190, 月华龙 黑蔷薇 33698022, and 电光赛道名将 33158448 become dead, set it from the field when you expect to use those
- 赐炎之咎姬 2772337 locks you to FIRE-only Special Summons while on field and 次元吸引者 91800273 requires an empty graveyard, check both before extending
- Attack first with 天杯龙 中龙 91810826 to trigger its deck Special Summon, then synchro, the generated monster can still attack this Battle Phase
- Under 增殖的G 23434538 or 欢聚友伴·茸茸长尾山雀 42141493 stop at 白龙 39931513 plus attack or 白龙 into 灿幻升龙 only, the full combo hands the opponent five or more draws
- 欢聚友伴·茸茸长尾山雀 42141493 cannot activate unless your field is empty, do not hold it as a reactive card after summoning
- 电光赛道名将 33158448 negates only Spell and Trap activations, each negate costs two Levels, and at Level 3 it can no longer activate, at most two negates per turn
- 灿幻封炉 55484152 sets cards that are banished when they leave the field and traps cannot activate the turn they are set, prefer 开门 and 庄 searches mid-combo
