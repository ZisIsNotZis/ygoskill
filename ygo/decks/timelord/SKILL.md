---
name: timelord-experience
description: 时械神 (Timelord) deck experience: mechanics, one-card combo, extenders, halt points
---
# 时械神 (Timelord) Deck Experience

- **Deck Identity**

- Main engine: 时械神 monsters, all Level 10 Fairy with 0 ATK, cannot be destroyed by battle or card effects, take no battle damage from their battles, and shuffle themselves into the Deck at your Standby Phase
- Modern near-pure build from deck/260124时械神: 时械神 加百利恩 6616912 x3, 时械神 桑达伊恩 33015627 x3, 时械神 拉法恩 60222213 x3, 时械神 拉结恩 92435533 x3, 究极时械神 赛菲隆 8967776 x1, 时械巫女 27107590 x3
- Trap ladder: 虚无械 9409625 x3, 无限械 36894320 x2, 无限光 72883039 x1, plus 王宫的通告 51452091 x3 and 神之宣告 41420027 x1
- Spell support: 撕裂时间的魔瞳 19403423 x2, 拥抱过咎的魔瞳 61822419 x1, 三战之号 35269904 x2
- Extra deck toolbox: 超重型炮塔列车 古斯塔夫最大炮 56910167, No.35 极饿捕鸟蛛 90162951, No.84 增痛蛛 26556950, No.77 七罪蛛 62541668, 天霆号 阿宙斯 90448279, 灾厄之星 提·丰 93039339, 终戒超兽-武尔德拉斯 70636044, 拓扑逻辑轰炸龙 5821478, 拓扑零日衔尾蛇 66403530, 梦幻崩影·凤凰 2857636, 梦幻崩影·狮鹫 65330383, 虚光之宣告者 46935289, 神书的使者 拉哈穆 53904087
- This cardpool has no 时械神界 field spell, no 时械神 半神, and no Sarcophagus-style support; 影光的圣选士 23912837 and 神数的圣选士 98076754 exist but are 影依/神数 support (setcodes 0x9d/0xc4), not Timelord cards, never include them
- The 时械神 ladder top is 究极时械神 赛菲隆 8967776 (self-summon with 10+ monsters in grave) and 时械神祖 武加大 67508932 (Synchro, banishes opponent monsters when it battles) though the pure list runs no Tuner so 武加大 is usually unreachable
- The deck is a near no-spell-trap beatdown: every turn tribute-free normal summon an unkillable Timelord, trigger its battle-phase burn, recycle it, and close with the Rank 10 Xyz line

- **Core Mechanic: Tribute-Free Timelord Loop**

- Every 时械神 in the script pool has an EFFECT_SUMMON_PROC: if your field is empty and you have a free monster zone, normal summon it without tribute (Level 10)
- 时械神 桑达伊恩 33015627 additionally requires the opponent to control a monster for its tribute-free summon; it is also unique on field, one copy only
- Every 时械神 has an unconditional cannot-be-special-summoned-while-in-Deck condition (EFFECT_SPSUMMON_CONDITION at Deck location, cannot be disabled), so ordinary revival from Deck fails; summoning from hand or grave works normally
- Shared immunity: EFFECT_INDESTRUCTABLE_BATTLE and EFFECT_INDESTRUCTABLE_EFFECT make them immune to battle and effect destruction, and EFFECT_AVOID_BATTLE_DAMAGE makes their controller take no battle damage
- Battle-phase payoff triggers at the end of the Battle Phase, once per turn, only if the Timelord battled: 时械神 桑达伊恩 33015627 burns 2000, 时械神 米奇恩 7733560 halves opponent LP, 时械神 拉法恩 60222213 burns equal to one battled monster's ATK
- Other payoffs: 时械神 加百利恩 6616912 shuffles all opponent on-field cards into the Deck and the opponent draws for each, 时械神 拉结恩 92435533 shuffles the entire opponent grave into the Deck and burns 1000 once per turn whenever the opponent draws
- Mandatory Standby Phase effect: each 时械神 shuffles itself into the Deck at your Standby, so the loop is summon-battle-burn-recycle each turn, and the Deck never empties
- 时械巫女 27107590 is the searcher: it can special summon itself from hand when your field is empty, and while on field it can release itself as cost to add any 时械神 with 0 ATK from Deck to hand, leaving the field empty for the tribute-free summon
- 时械巫女 27107590 grave effect special summons a 时械神 from Deck ignoring summoning conditions, but only as your first special summon of the turn and it locks all further special summons that turn

- **One-Card Combo: 时械巫女**

- Starter: 时械巫女 27107590 alone in hand, no other cards needed
- Step 1: normal summon 时械巫女 (no tribute needed, field must be empty)
- Step 2: activate its field effect, release itself as cost, add a 时械神 from Deck to hand, your field is now empty
- Step 3: tribute-free normal summon 时械神 桑达伊恩 33015627 (opponent needs a monster) or 时械神 拉法恩 60222213 / 时械神 拉结恩 92435533
- Step 4: attack, end of Battle Phase trigger resolves (2000 burn for 桑达伊恩, ATK burn for 拉法恩, grave shuffle for 拉结恩)
- Step 5: Standby Phase next turn the Timelord shuffles into the Deck, repeat from step 1 with the next 时械巫女 or searched copy
- Alternative one-card line: 撕裂时间的魔瞳 19403423 alone, draw 2, then normal summon 时械巫女 and a 时械神 with the double normal summon, plus the turn's hand monster activations are locked
- Halt point: negating the 时械巫女 search (Ash-style hand trap) leaves no board, negating the 时械神 normal summon stops the whole loop for that turn

- **End Field**

- Ideal: 无限光 72883039 face-up with one or more 时械神 on field, 王宫的通告 51452091 set or flipped, one set trap from the ladder
- 无限光 72883039 protects: your 时械神 cannot be targeted by opponent effects and cannot be returned to the Deck, which cancels their mandatory Standby self-shuffle so they stay on field
- With 无限光 72883039 plus 时械神 桑达伊恩 33015627 and 时械神 拉结恩 92435533, every attack burns 2000 and every opponent draw burns 1000
- Rank 10 Xyz line from two Level 10 时械神: 超重型炮塔列车 古斯塔夫最大炮 56910167 (detach one, burn 2000) or No.35 极饿捕鸟蛛 90162951, climb into No.84 增痛蛛 26556950, then No.77 七罪蛛 62541668
- Overlay finishers: 天霆号 阿宙斯 90448279 can be Xyz Summoned over any Xyz monster you control, 灾厄之星 提·丰 93039339 can be Xyz Summoned over your highest-ATK monster such as a 4000 ATK 时械神 桑达伊恩 33015627
- 终戒超兽-武尔德拉斯 70636044 is a Rank 10 negate-and-destroy monster made directly from two 时械神, good under 王宫的通告 51452091
- 虚光之宣告者 46935289 negates any Spell/Trap activation by discarding a Fairy, and 时械神 in hand are Fairy discard fodder
- 神书的使者 拉哈穆 53904087 gives an extra normal summon for a Level 5+ monster and recycles hand monsters for draws at the end phase
- 究极时械神 赛菲隆 8967776 special summons itself from hand with 10+ monsters in grave and each turn can special summon one Level 8+ Fairy from hand or grave with negated effects and 4000 ATK as a beater

- **Extenders**

- 虚无械 9409625: quick effect to discard a Level 10 from hand and draw one, and while it is the only card in your Spell/Trap zones, quick effect to shuffle a 时械神 from grave into the Deck and set 无限械 36894320 from hand or Deck, it survives one opponent effect destruction per turn
- 无限械 36894320: activates by sending face-up 虚无械 9409625 to the grave, then once per turn either special summons a 时械神 from hand in a Main Phase or shuffles a 时械神 from grave into the Deck to set 无限光 72883039
- 无限光 72883039: activates by sending face-up 无限械 36894320 to the grave, then once per turn if your field is empty special summons up to three 时械神 from hand, Deck and grave, one from each location, ignoring summoning conditions
- 三战之号 35269904: if the opponent activated a Spell/Trap this turn, search any Spell or Trap from the Deck and either set it (it cannot trigger that turn) or add it to hand if the opponent controls a monster, this is how the deck finds the ladder
- 拥抱过咎的魔瞳 61822419: for the turn, every Level 5+ monster in your hand can be normal summoned without tribute, your Spell/Trap activations pay no LP cost, and from the grave it banishes itself to shuffle a 魔瞳 from hand into the Deck and draw one
- 撕裂时间的魔瞳 19403423: draw two and gain a second normal summon, and from the grave it can banish itself plus discard another copy so that after your next normal summon the opponent cannot activate monster effects for the rest of the chain
- 光神化 28890974: special summons a Fairy from hand with halved ATK that self-destructs at the end phase, used in variant builds to drop a 时械神 for one battle phase before turning it into Xyz material
- 十种神镜阵 50357013: variant-build draw card, send any face-up monsters from hand or field whose levels total exactly 10 to the grave and draw two, one Level 10 时械神 is the perfect cost and it feeds 赛菲隆's grave count

- **Halt Points**

- The 时械巫女 27107590 search is the engine, negating it or the follow-up tribute-free normal summon stops the turn with no board
- 虚无械 9409625 quick effects require it to be the only card in your Spell/Trap zones, so a set 王宫的通告 51452091 or any other backrow blocks the whole ladder
- 无限械 36894320 special summon only works in a Main Phase and only from the hand, 无限光 72883039 only works with an empty field, so a lingering monster or token blocks the flood summon
- Removing 无限光 72883039 lets every 时械神 shuffle itself into the Deck at your Standby, leaving you with no field for the next turn
- 时械神 桑达伊恩 33015627 cannot even be tribute-free summoned if the opponent's field is empty, and all battle payoffs require actually battling, so attack-locks or no valid attack stop the burn
- 王宫的通告 51452091 negates all other trap effects on the field, including your own 虚无械 9409625, 无限械 36894320 and 无限光 72883039, so it must be flipped after the ladder plays resolve

- **Mirror Match: 时械神 vs 时械神**

- Direct damage wins the mirror since no battle damage is ever dealt, whoever resolves 时械神 桑达伊恩 33015627 or 时械神 拉法恩 60222213 first takes the race
- 时械神 加百利恩 6616912 is the strongest mirror card, shuffling the opponent's whole field including their 时械神 into the Deck so they lose field presence and must rebuild
- 时械神 拉结恩 92435533 punishes the opponent's draw effects with 1000 damage per draw, both players run 撕裂时间的魔瞳 19403423 so the draw-burn applies
- Whoever lands 无限光 72883039 first keeps their 时械神 on field while the opponent's self-shuffle every Standby, permanent field advantage decides the game
- The 王宫的通告 51452091 fight matters, the side that flips it after the ladder resolves controls the trap engine, 神之宣告 41420027 negates the opponent's 时械巫女 27107590 summons or 无限械 36894320 activations
- 时械神 米奇恩 7733560 in variant builds halves the opponent's LP directly and is the fastest kill, beat it before it battles

- **Common Mistakes**

- Do not waste 时械巫女 27107590 grave effect after any special summon that turn, it requires being your first special summon and locks all later special summons
- Do not rely on normal revival to special summon 时械神 from the Deck, their cannot-be-summoned-from-Deck condition blocks it, use 时械巫女 27107590 or 无限光 72883039 which ignore summoning conditions
- Do not flip 王宫的通告 51452091 before resolving 虚无械 9409625, 无限械 36894320 and 无限光 72883039 plays, it negates your own trap ladder
- Do not leave a monster on field when planning 无限光 72883039, its three-monster flood summon requires an empty field
- Do not attack with 时械神 桑达伊恩 33015627 into an empty opponent field, no battle means no 2000 burn, and it also cannot be tribute-free summoned then
- 撕裂时间的魔瞳 19403423 and 拥抱过咎的魔瞳 61822419 lock your own hand monster activations for the turn, activate hand traps first or accept the lock
- 光神化 28890974 special summons a monster that self-destructs at the end phase, use its battle phase then Xyz or link it away before the end phase
- 究极时械神 赛菲隆 8967776 special summons with negated effects, the 4000 ATK beater does not keep the battle immunity or the burn trigger
- 时械神 加百利恩 6616912 lets the opponent draw for every card shuffled, do not shuffle into a hand that can out your 无限光 72883039 lock
- 时械神 拉结恩 92435533 grave shuffle is cancelled by NecroValley-style effects, check for the negation before expecting the grave wipe
- Do not run 影光的圣选士 23912837 or 神数的圣选士 98076754 for Timelord support, they belong to 影依 and 神数, the 时械神 setcode is 0x4a
