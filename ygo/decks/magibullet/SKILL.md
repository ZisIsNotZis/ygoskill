---
name: magibullet-experience
description: 魔弹 (Magibullet) deck experience: mechanics, one-card combo, extenders, halt points
---
# 魔弹 (Magibullet) Deck Experience

- **Deck Identity**

- 16-card archetype verified from cards.cdb and script/: 9 monsters 卡斯帕 32841045, 小子 5230799, 医生 68246154, 斯塔尔 31629407, 灾星 68024506, 狂野 94418111, 萨米尔 30907810, 马克斯 71791814, 恶魔卡斯帕 3287359 plus 7 spells/traps 亡命之徒 20745268, 死者连发 29628180, 交叉统治者 93356623, 无尽内啡肽 67901914, 舞动之针 66149377, 血色之冠 47810543, 恶魔交易 92534075
- Main deck monsters are LIGHT Fiend level 3-4 with weak stats (1200-1700 ATK); 萨米尔 30907810 is a level 8 2500/2500 boss; the two links are 马克斯 71791814 (Link-1, 1000 ATK) and 恶魔卡斯帕 3287359 (Link-2, 2000 ATK)
- No archetype monster special summons itself from hand: bodies come from the normal summon, the column triggers, 马克斯 71791814, 同胞的牵绊 40450317 and 血色之冠 47810543
- Control and grind deck: disrupt during the opponent turn with hand-activateable archetype spells/traps, then out-grind with recursion from 医生 68246154, 灾星 68024506 and 狂野 94418111
- Two build families in deck/: pure trap-control without archetype links (e.g. 180414魔弹, Instant Fusion 1845204 + 千眼 package), and link-value with 马克斯 71791814 x3 plus a generic link package and DDD 蜘蛛 finisher (e.g. 220716魔弹, 230114魔弹)
- Build quirk: the deck .ydk files in deck/ carry no main/extra separator line, all zones export as one block; filter by card type when resolving them

- **Core Mechanic: Hand-Spell Firing**

- ① every face-up 魔弹 monster (main monsters, both links, 萨米尔 30907810) grants hand activation of 魔弹 spells/traps on both players' turns: quick-plays via EFFECT_QP_ACT_IN_NTPHAND and traps via EFFECT_TRAP_ACT_IN_HAND, verified in ocgcore effect.cpp which applies it to counter traps too, so 死者连发 29628180 is hand-activateable
- ② each main monster has a once-per-turn quick trigger on EVENT_CHAINING when any Spell/Trap is activated in its column; scripts verify re:IsHasType(EFFECT_TYPE_ACTIVATE) and the monster's GetColumnGroup contains the activated card, so the activation can be from hand or field and by either player
- Column placement is the core skill: the activated card must be placed into the Spell/Trap zone sharing the monster's column (same zone sequence), otherwise the trigger never fires
- Any Spell/Trap activation in the column counts, not just archetype ones; generic spells such as 成金哥布林 70368879 and 强欲而贪欲之壶 35261759 are cheap trigger fodder
- 卡斯帕 32841045 ② searches any 魔弹 card from deck except the activated card's name; 医生 68246154 ② adds any 魔弹 card from GY except the activated card's name
- 小子 5230799 ② discards one 魔弹 card from hand as cost then draws 2; 斯塔尔 31629407 ② special summons one level 4 or lower 魔弹 monster from deck in face-up defense except itself
- 灾星 68024506 ② special summons one 魔弹 monster from GY in face-up defense; 狂野 94418111 ② shuffles exactly 3 魔弹 cards from GY into deck and draws 1
- 马克斯 71791814 is Link-1 with material 1 魔弹 monster of level or link rating 8 or lower; IsLinkSetCard(0x108) equals IsSetCard in this core so any main-deck 魔弹 works as material, not only link monsters
- 恶魔卡斯帕 3287359 is Link-2 with 2 monsters including 1 LIGHT Fiend; on link summon it picks 2 魔弹 cards from hand or deck including at least 1 monster, special summons one monster to your field and sets the other face-down on the opponent field (monster face-down defense, spell/trap face-down)
- 萨米尔 30907810 can be tribute summoned with 1 tribute of any face-up 魔弹 monster from either field, and ② draws at the opponent end phase equal to the number of 魔弹 spells/traps you activated since your draw phase while it was face-up (script counts globally, negated activations subtract)

- **One-Card Combo: 小子 or 卡斯帕 into 马克斯**

- Starter: 小子 5230799 or 卡斯帕 32841045 alone; the payoff scales with the opponent field
- Step 1: normal summon the starter monster
- Step 2: link summon 马克斯 71791814 using it as the single material
- Step 3: resolve 马克斯 71791814 ① with the option that fits the opponent field: if they control at least 1 monster, add up to that many 魔弹 spells/traps from deck to hand with each name once; if they control at least 1 spell/trap, special summon up to that many 魔弹 monsters from deck with each name once
- Step 4: the added spells/traps are already hand-activateable for the rest of the game while any 魔弹 monster is face-up; the add line typically takes 交叉统治者 93356623, 亡命之徒 20745268 and 死者连发 29628180
- Halt point: 马克斯 71791814 ① does nothing against an empty opponent field, open instead with the column-search micro-line below
- Micro-line (the real engine, 2 cards): normal summon 卡斯帕 32841045, activate any spell from hand into its column such as 成金哥布林 70368879, 卡斯帕 ② searches any 魔弹 card from deck; the searched card chains into more column activations or extends with 斯塔尔 31629407

- **End Field**

- Typical control end board: 马克斯 71791814 plus one main monster such as 小子 5230799 or 卡斯帕 32841045, with 血色之冠 47810543 and 恶魔交易 92534075 set, and a hand full of 魔弹 spells/traps
- On the opponent turn, activate 魔弹 spells/traps from hand into the monster columns: each activation fires the ② engine again, so 卡斯帕 32841045 re-searches, 小子 5230799 draws 2, 医生 68246154 recurs, 斯塔尔 31629407 summons blockers
- Interaction set while monsters are up: 死者连发 29628180 negates and destroys their spell/trap activation, 交叉统治者 93356623 sets one face-up monster to 0 ATK/DEF and negates it, 亡命之徒 20745268 destroys one face-up card, 舞动之针 66149377 banishes up to 3 cards from either or both graveyards
- 血色之冠 47810543 quick effect in either main phase special summons one 魔弹 from hand and locks the opponent mirror monster zone while unused; 恶魔交易 92534075 makes 魔弹 monsters indestructible by card effects and searches one 魔弹 from deck or GY when sent by an opponent effect
- 无尽内啡肽 67901914 doubles one 魔弹 monster's ATK and DEF for the turn with no direct attack allowed, turning 萨米尔 30907810 into a 5000 beater for monster clearing
- Link builds finish with the DDD 蜘蛛 package: 赦俿王 46593546 or 磐石王 51497409 into No.84 增痛蛛 26556950 into No.77 七罪蛛 62541668 to banish all opponent special summoned monsters

- **Extenders**

- 同胞的牵绊 40450317 at 3 in every pure build: pay 2000 LP, target one level 4 or lower monster, special summon 2 different 魔弹 monsters from deck with the same type, attribute and level, which every level 3-4 main monster satisfies; it locks all special summons for the rest of the turn and skips the battle phase, so sequence it last
- 血色之冠 47810543 is a one-of that extends bodies and locks a zone during either main phase
- 灾星 68024506 revives any 魔弹 monster from GY on its column trigger, enabling link climbs again
- 医生 68246154 recurs any 魔弹 card from GY on its column trigger, keeping interaction density high
- 狂野 94418111 recycles 3 spent 魔弹 cards into the deck for a draw, refueling the search pool
- 斯塔尔 31629407 summons level 4 or lower 魔弹 from deck on its column trigger, a free body for 马克斯 71791814 material
- Instant Fusion 1845204 into 千眼纳祭神 63519819 or 千年眼纳祭神 41578483 gives instant bodies and hand-trap protection; 旧神 努茨 80532587 pairs with 禁忌的一滴 24299458 by being sent as cost to destroy a card
- 进入境智网 28827503 special summons a hand monster negated and immediately link summons it with a link summon that cannot be negated and no response window
- Generic spells as trigger fodder double as extenders: 成金哥布林 70368879, 强欲而贪欲之壶 35261759, 雷击 12580477

- **Halt Points**

- 灰流丽 14558127 negates 卡斯帕 32841045 ② search, 马克斯 71791814 ① add or special summon, and 小子 5230799 ② draw
- 幽鬼兔 59438930 destroys any monster using its field ② trigger and 马克斯 71791814 when it resolves ①
- 无限泡影 10045474 or 禁忌的一滴 24299458 on 马克斯 71791814 or 萨米尔 30907810 removes the engine for the turn
- 墓穴的指名者 24224830 on 医生 68246154 or 灾星 68024506 in GY stops recursion; deck-special summons from 马克斯 71791814, 斯塔尔 31629407 and 同胞的牵绊 40450317 cannot be stopped by it
- 增殖的G 23434538 punishes 马克斯 71791814 ① mass special summon and 同胞的牵绊 40450317; fall back to the single-monster add line
- Exile effects starve the engine: 舞动之针 66149377 clears both graveyards, cutting 医生 68246154, 灾星 68024506 and 狂野 94418111 recursion
- The ① hand-activation effect only exists on face-up monsters in the monster zone: flipping 魔弹 monsters face-down or removing them halts all hand plays

- **Mirror Match**

- The column trigger fires on the opponent's activations too: never activate a spell/trap in the column of an enemy 魔弹 monster, it searches with 卡斯帕 32841045, draws 2 with 小子 5230799 or summons with 斯塔尔 31629407
- 萨米尔 30907810 can tribute any face-up 魔弹 monster from either field as material, so an opponent 萨米尔 can eat your face-up monsters
- 交叉统治者 93356623 is the engine killer in the mirror: zero and negate their 马克斯 71791814 or 卡斯帕 32841045 first
- 死者连发 29628180 answers their hand activations, so the player who activates first into a wrong column loses the exchange
- 恶魔交易 92534075 makes 亡命之徒 20745268 useless against their monsters, switch to 交叉统治者 93356623 for removal
- The face-down card gifted by 恶魔卡斯帕 3287359 sits on the opponent field and they can activate it or tribute it with their 萨米尔 30907810, only use it when the 马克斯 71791814 follow-up payoff outweighs the gift

- **Common Mistakes**

- Activating the trigger spell in the wrong column: the monster ② only fires when the activated card is placed in the same column, so check zone sequence before playing
- Assuming the column trigger needs a 魔弹 spell: any spell/trap activation in the column works, generic spells are free trigger fodder
- 同胞的牵绊 40450317 ordering: after it resolves you cannot special summon for the rest of the turn and you lose the battle phase, so resolve Instant Fusion 1845204 and link plays before it, or use it as the terminal play
- 无尽内啡肽 67901914 forbids direct attack on the target, so a doubled monster clears monsters but cannot close the game directly
- 狂野 94418111 requires exactly 3 魔弹 cards in GY as targets or the draw does not resolve
- 马克斯 71791814 ① is dead against an empty opponent field; do not link your only monster into it without checking
- 恶魔卡斯帕 3287359 gifts the opponent a face-down 魔弹 card that feeds their 萨米尔 30907810 tribute and their own hand activations
- 死者连发 29628180 only responds to the opponent spell/trap activations, it cannot negate monster effects
- 交叉统治者 93356623 targets any face-up monster including your own, verify the target before activating
- 舞动之针 66149377 banishes from both graveyards, resolve 医生 68246154 and 灾星 68024506 recursion before activating it, not after
- 萨米尔 30907810 ② only resolves at the opponent end phase while it is still face-up on the field and needs at least one counted activation, so summon it early in your turn
- Filling your own spell/trap zones with sets leaves no zone to place column activation fodder, keep one column zone open per trigger monster
