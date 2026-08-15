---
name: darkworld-experience
description: 暗黑界 (Dark World) deck experience: discard-trigger engine, opponent-discard bonuses, Grapha recursion, fusion package
---
# 暗黑界 (Dark World) Deck Experience

- **Deck Identity**

- All 暗黑界 monsters are DARK Fiends whose effects fire when discarded from hand to graveyard by a card effect, verified in every script as bit.band(r,0x4040)==0x4040 meaning REASON_EFFECT plus REASON_DISCARD
- Core discard engine: 暗黑界的取引 74117290, 墓穴的同路人 16435215, 暗黑回廊 98696958, 手札抹杀 72892473, 暗黑界之门 33017655 all discard by effect so every dropped 暗黑界 monster triggers
- "被对方的效果丢弃" bonus: any effect that fires additionally when the discard source is the opponent, scripted as rp==1-tp and tp==e:GetLabel(), the strongest versions only resolve this bonus
- The only easy way to make your own discards count as opponent-discards is 墓穴的同路人 16435215, because each player discards from the opponent hand, so the opponent is the reason player
- Extra deck focus is fusion: 暗黑界的登极 65956182, 暗黑界的混沌王 卡勒莱斯 22723778, 暗黑界的龙神王 格拉法 39552584, plus Rank 8 Xyz and 天霆号 阿宙斯 90448279, no synchro lines at all

- **Core Mechanic: Discard-Trigger Chain**

- 暗黑界的术师 丝诺 60228941 on effect discard adds any 暗黑界 card from deck, opponent-discard bonus also special summons a monster from opponent graveyard to your field in defense
- 暗黑界的龙神 格拉法 34230233 on effect discard destroys one opponent card, opponent-discard bonus confirms one random opponent hand card and steals it if it is a monster
- 暗黑界的魔神王 雷恩 41406613 on effect discard searches any Level 5 or higher 暗黑界 monster from deck, opponent-discard bonus also special summons any Level 4 or lower 暗黑界 monster from deck or grave to either field
- 暗黑界的军神 希尔瓦 32619583, 暗黑界的鬼神 凯勒特 34968834, 暗黑界的尖兵 贝基 33731070, 暗黑界的武神 高尔德 78004197 special summon themselves when discarded by effect, 武神 destroys up to two cards and 鬼神 extends with a Fiend from deck on the opponent-discard bonus
- 暗黑界的狩人 布劳 79126789 draws one card when discarded, draws two on the opponent-discard bonus, pure advantage engine
- 暗黑界的魔神 雷恩 99458769 only triggers on opponent-effect discard, then destroys all opponent monsters or all opponent spells and traps, the finisher piece
- 暗黑界的导师 塞鲁利 07623640 on effect discard special summons itself to opponent field in defense, then when it is special summoned by a 暗黑界 effect the opponent discards one card, an old hand-lopping engine
- 暗黑界的文殿 76672730 draw two when any Fiend is discarded from your hand by a 暗黑界 card effect or by an opponent effect, once per turn, the modern advantage engine
- 暗黑界的登极 65956182 fusing a 暗黑界 monster may use hand monsters as material and discards them by effect, so every 丝诺, 布劳, 军神 or 格拉法 discarded as fusion material triggers mid-fusion

- **One-Card Combo: 暗黑回廊 98696958**

- Step 1: activate 暗黑回廊 98696958, add 暗黑界的术师 丝诺 60228941 from deck to hand
- Step 2: 暗黑回廊 resolution then discards one card from hand, discard the just-added 丝诺 60228941
- Step 3: 丝诺 trigger adds any 暗黑界 card from deck, prefer 暗黑界之门 33017655 or 暗黑界的取引 74117290 or 暗黑界的登极 65956182
- Step 4: play the searched card, 暗黑界之门 33017655 banishes the graveyard 丝诺 as cost to discard a Fiend and draw one, generating another trigger while 丝诺 stays revivable in the banished zone
- End state: one 暗黑界 card searched plus one draw for one card spent, 丝诺 60228941 in grave or banished ready for 龙神 格拉法 34230233 or 魔神王 41406613 recursion
- Alternative one-card line: 暗黑界的门番 真塔 77895328 discards itself from hand to add 暗黑界之门 33017655, then the gate banishes 真塔 as cost for discard plus draw

- **End Field**

- 暗黑界的龙神王 格拉法 39552584, fused by 暗黑界的登极 65956182 using 暗黑界的龙神 格拉法 34230233 from field or grave plus any DARK monster discarded from hand, 3200 ATK and a quick effect that turns any opponent monster effect or normal spell or trap activation into an opponent discard
- 暗黑界的混沌王 卡勒莱斯 22723778, fused by 暗黑界的登极 65956182 using 暗黑界的魔神 雷恩 99458769 plus two or more Fiends, destroys all opponent cards on fusion and its attack becomes material count times 1000, quick effect discards one to protect a face-up card from targeting for the turn
- 暗黑界的文殿 76672730 face-up so every subsequent 暗黑界 or opponent discard chain draws two cards, plus 暗黑界之门 33017655 for the 300 attack boost and the discard-draw loop
- One set 暗黑界的惩罚 03167439 to negate and destroy a summon by discarding a Fiend, while 暗黑界的龙神 格拉法 34230233 stays in grave to re-summon itself by bouncing a 暗黑界 monster
- 魔界特派员 死亡主播 71607202 protects any of your monsters from destruction by tributing one Fiend instead, and revives a Fiend from grave by discarding one card, a Fiend-only link that cannot be used as link material the turn it is summoned

- **Extenders**

- 暗黑界的取引 74117290 lets each player draw one and discard one, an unconditional discard-trigger outlet but it also fuels the opponent
- 墓穴的同路人 16435215 makes the opponent discard one card from your hand by their own effect, granting every 暗黑界 monster its full opponent-discard bonus, then both draw one, the premium extender
- 暗黑界的登极 65956182 is a fusion spell that also recycles itself from grave by returning to hand and discarding one 暗黑界 monster, repeatable fusion pressure
- 暗黑界的援军 85325774 revives any Level 4 or lower Fiend from grave then discards a Fiend from hand, two triggers for one card
- 连接暗黑界的结界通路 93431518 revives any 暗黑界 monster from grave but locks you out of all other summons for the turn, a finishing extender only
- 暗黑界的傀儡 30284022 banishes up to three monsters from both graves then discards a Fiend, and later banishes itself to return a banished Fiend to hand
- 暗黑界的洗脑 10131855 with three or more cards in hand bounces a 暗黑界 monster and turns an opponent monster effect into an opponent random discard, a defensive extender that grants opponent-discard bonuses
- 暗黑界的隐者 珀尔 03289027 when discarded revives a 暗黑界 monster from grave to either field, opponent-discard bonus extends into any Fiend from hand, grave or banished zone
- 超融合 48130397 discards one and fuses using both fields, can make 大气吸收者 28143384 from two Fiends of the same attribute when the opponent plays Fiends

- **Halt Points**

- 灰流丽 14558127 negates 暗黑界的术师 丝诺 60228941 search, 暗黑回廊 98696958, and 暗黑界的门番 真塔 77895328 search because all add from deck
- 增殖的G 23434538 turns every discard-trigger special summon of 军神 32619583, 鬼神 34968834, 魔神 99458769 or 魔神王 41406613 into an opponent draw, stop extending once it resolves
- 次元吸引者 or 次元裂缝 banishes discarded monsters instead of sending them to grave, so every 暗黑界 discard trigger never fires, the harshest counter
- 墓穴指名者 stops 暗黑界的龙神 格拉法 34230233 and 魔神王 41406613 grave recursion, and 王宫的敕命 negates every discard spell
- 王家的谷 (Necrovalley) blocks the graveyard special summons of 龙神 格拉法 34230233 and 魔神王 41406613 because both scripts check EFFECT_NECRO_VALLEY
- 暗黑界的惩罚 03167439 only negates a summon when you have a Fiend in hand to discard afterward, empty hand makes it dead

- **Mirror Match: 暗黑界 vs 暗黑界**

- 墓穴的同路人 16435215 is double-edged in the mirror, your discard of an opponent 暗黑界 monster grants them their full opponent-discard bonuses, so only use it when your own chain resolves better
- 暗黑界的取引 74117290 hands the opponent a draw and a discard, in the mirror that fuels their engine too, weigh the advantage before activating
- 暗黑界的龙神王 格拉法 39552584 conversion makes the opponent discard their own card, which their own 文殿 76672730 draw-two still triggers, so the conversion trades like a targeted discard against their advantage engine
- Keep 暗黑界的术师 丝诺 60228941 alive to deny their search and banish graveyard 龙神 格拉法 34230233 copies to break their recursion loop
- 暗黑界的文殿 76672730 draw-two fires on every opponent-effect discard, so a player who chains discards first floods their hand while the other cascades triggers for them

- **Common Mistakes**

- 暗黑界的门番 真塔 77895328 discard is a cost, not an effect discard, so it never triggers 暗黑界的文殿 76672730 or any other 暗黑界 discard trigger
- 手札抹杀 72892473 and 暗黑界的取引 74117290 discards are your own effect, so they grant no opponent-discard bonus, only 墓穴的同路人 16435215 and 暗黑界的洗脑 10131855 grant the bonus reliably
- Do not sequence 暗黑界的登极 65956182 fusion without planning which hand monsters become discarded materials, every discarded 暗黑界 monster triggers mid-fusion and can flood the board before 混沌王 22723778 resolves
- 暗黑界的混沌王 卡勒莱斯 22723778 requires exactly 暗黑界的魔神 雷恩 99458769 plus two Fiends, and 魔神 雷恩 only triggers on opponent discards, so protect it and never discard it without the bonus
- 暗黑界的龙神 格拉法 34230233 special summons itself from grave by bouncing a face-up 暗黑界 monster, never bounce the monster you need for an Xyz or fusion that turn
- 魔神王 41406613 can only bounce a Level 7 or lower 暗黑界 monster, while 龙神 格拉法 34230233 can bounce any, misreading the level restriction wastes the recursion
- 连接暗黑界的结界通路 93431518 locks out all summons for the turn, do not activate it then expect to extend, play it only as the final move
- 暗黑界的文殿 76672730 draw-two triggers during damage step too, keep it face-up before any big discard chain and sequence the discards to maximize its once per turn draw
- Under 技能抽取 82732705 field monster effects are negated but 暗黑界的龙神 格拉法 34230233 and 魔神王 41406613 still special summon from grave because that summon is not a field effect, a deliberate synergy
- 天霆号 阿宙斯 90448279 needs an Xyz monster that battled this turn, so attack with No.1 感染蝇王 10666000 first, then overlay 阿宙斯 on top of it to wipe the board

- **Build Quirks**

- The reference pure build 250927暗黑界 runs three 暗黑界的龙神 格拉法 34230233, three 魔神王 41406613, three 术师 丝诺 60228941, three 门番 真塔 77895328 and three 狩人 布劳 79126789 as the engine core
- It plays three 暗黑界的取引 74117290, three 墓穴的同路人 16435215, three 暗黑界的登极 65956182 and two 暗黑界之门 33017655 as the discard outlets, with one 手札抹杀 72892473, one 暗黑回廊 98696958 and one 暗黑界的文殿 76672730
- Singles of 暗黑界的军神 32619583, 暗黑界的鬼神 34968834, 暗黑界的魔神 99458769 and 暗黑界的隐者 03289027 cover the fusion material and recursion roles without bloating the discard pool
- The extra deck holds two 暗黑界的混沌王 卡勒莱斯 22723778, two 暗黑界的龙神王 格拉法 39552584, one 大气吸收者 28143384, one No.1 感染蝇王 10666000, one 天霆号 阿宙斯 90448279, one 灾厄之星 提·丰 93039339, one 破械双王神 来迎 29479265 and one 魔界特派员 死亡主播 71607202
- 灾厄之星 提·丰 93039339 is a hand-trap Xyz that overlays on the opponent attack-position monster after they special summon two or more from the extra deck, negating all 3000 or higher attack monster effects
- 技能抽取 82732705, 鹰身女妖的羽毛扫 18144506 and 超融合 48130397 fill the generic slots, 超融合 discards one card so it is also a discard outlet
