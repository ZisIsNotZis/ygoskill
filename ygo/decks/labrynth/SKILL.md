---
name: labrynth-experience
description: 拉比林斯迷宫 (Labrynth) deck experience: Normal Trap engine, welcome recursion, setup lines, halt points
---
# 拉比林斯迷宫 (Labrynth) Deck Experience

- **Deck Identity**

- This codebase translates the archetype as 白银之城 (Silver Castle) / 迷宫城; the trap names use 拉比林斯迷宫, all are the same archetype
- Trap-control grind deck: DARK Fiend monsters plus Normal Trap recursion, wins by out-grinding with 2900/3000 beatsticks and repeated trap value
- No in-archetype extra deck; extra slots are generic removal/answers such as 混沌之双翼 22850702, 灾厄之星 提·丰 93039339, 旧神 努茨 80532587, 闭锁世界的冥神 98127546, 访问码语者 86066372
- The newer support names used in other guides (超兽灰姑娘, 贵妇布朗尼可, 惨眩骇触拉比林斯) do not exist in this build; the full family here is 白银之城的召使 阿里安娜 1225009, 白银之城的召使 阿里亚娜 75730490, 白银之城的执事 阿里亚斯 73602965, 白银之城的火吹炉 74018812, 白银之城的龙饰灯 37629703, 白银之城的狂时钟 2511, 白银之城的魔神像 48745395, 白银之城的拉比林斯 2347656, 迷宫城的白银姬 81497285, 白银之迷宫城 33407125, 拉比林斯迷宫欢迎 5380979, 拉比林斯迷宫欢迎欢迎大欢迎 92714517, 拉比林斯迷宫欢迎欢送 32785578, 拉比林斯迷宫连环阵 68779682, 拉比林斯迷宫布置 69895264

- **Core Mechanic: Normal Trap Engine**

- Nearly all recursion triggers on "your Normal Trap effect makes a monster leave the field", verified in scripts as previous location MZONE plus reason effect, no owner restriction, so the opponent's monsters you destroy also trigger it
- 阿里安娜 1225009 ②: draw 1, then optionally special summon 1 Fiend from hand or set 1 card from hand
- 阿里亚娜 75730490 ②: same draw-plus-set/summon pattern
- 白银之城的拉比林斯 2347656 ③: destroy 1 card in the opponent's hand (random) or 1 card they control
- 拉比林斯迷宫欢迎 5380979 ②: set itself from GY, once per turn, not usable the turn it was sent to GY
- 白银之城的火吹炉 74018812 ② revives itself, 白银之城的龙饰灯 37629703 ② returns itself to hand, 白银之城的狂时钟 2511 ② returns to hand or revives

- **Engine: Welcome Trap Recursion**

- 欢迎 5380979 ①: special summon 1 Labrynth monster from deck, then until the end of the next turn you can only special summon Fiends from deck or extra
- 大欢迎 92714517 ①: special summon 1 Labrynth from hand, deck or GY, then return 1 monster you control to hand; the bounce is itself a "leave the field" event that re-fires the recursion
- 大欢迎 92714517 ②: banish itself from GY to return 1 Fiend you control to hand, or an opponent's card instead while you control a face-up Level 8 or higher Fiend
- Standard loop: 欢迎 summons 白银之城的拉比林斯 2347656, 大欢迎 bounces it, which fires 阿里安娜's draw, the 2347656 ③ destroy, 欢迎 ② set-from-GY and 火吹炉 74018812 revival all at once, repeatable every turn
- 拉比林斯迷宫连环阵 68779682 chained to a set 欢迎 copies its effect so the summon resolves twice

- **One-Card Setup (trap engine instead of a combo)**

- 阿里安娜 1225009: normal summon, search any Labrynth card (欢迎, 大欢迎, 连环阵, 白银之城的拉比林斯, 白银之迷宫城, 布置), set it if the searched card is a trap
- 火吹炉 74018812 or 龙饰灯 37629703 from hand: send itself plus discard 1 as cost, set 1 Labrynth spell or trap from hand or deck, usually 欢迎 5380979; the effect is quick so it also works on the opponent's turn
- 阿里亚娜 75730490: send 1 Normal Trap from hand or face-down field to GY as cost, special summon 1 Level 4 or lower Fiend from deck in defense (火吹炉, 龙饰灯, 狂时钟 or another 阿里安娜), then that monster sets or searches
- 阿里亚斯 73602965: in either main phase, send itself from hand or field to GY, special summon 1 Labrynth from hand or set 1 Normal Trap from hand that can be activated the same turn; in GY it revives when the opponent chains to your Labrynth card or trap

- **End Field**

- Turn 1 typical: one small Fiend plus 2-3 set traps (欢迎 5380979, 大欢迎 92714517, 次元障壁 83326048, 教导的惩罚 82956214, 蛊惑谋陷 80101899, 事务回滚 6351147, 欢迎欢送 32785578) plus hand traps 灰流丽 14558127, 增殖的G 23434538, 无限泡影 10045474
- 迷宫城的白银姬 81497285 waiting in hand: on either player's turn, when a Normal Trap or Labrynth card effect activates, special summon it in defense; while you control a face-down card it cannot be targeted or destroyed by opponent effects; ③ once per turn sets a different Normal Trap from deck when a Normal Trap activates
- 白银之城的拉比林斯 2347656 on field: opponent cannot chain monster effects to your Normal Trap activations, so 灰流丽 14558127 and 无限泡影 10045474 cannot stop your 欢迎; ② once per turn sets 1 Normal Trap from GY, but that trap cannot activate without a face-up Fiend on your field
- With 白银之迷宫城 33407125: activating a set 欢迎-family trap (script setcode 4478) optionally destroys 1 card on the field, once per turn; activating any non-Labrynth Normal Trap special summons 1 Fiend from hand or GY

- **Extenders**

- 连环阵 68779682: chain to your own SET Normal Trap activation and copy its effect, then your effect damage to the opponent becomes 0 until the end of the next turn
- 事务回滚 6351147: pay half LP and copy a Normal Trap's activation effect from the opponent's GY (①) or your own GY (②, banishing itself), re-resolving 欢迎, 大欢迎 or a copied 次元障壁 83326048
- 蛊惑谋陷 80101899: banish 1 Normal Trap from deck, set its same-name copy from deck activatable the same turn, but afterwards you can only activate 1 trap this turn
- 沉迷陷溺 22377092: destroy your own spell or trap, set 1 Normal Trap from deck activatable the same turn while 3 or more traps are in your GY
- 布置 69895264: shuffle 2 Labrynth spells or traps from GY and banished into deck, then if you control a Fiend set the same number of different non-Labrynth Normal Traps from deck; note it is registered as a Continuous Spell in the database though its effect is one-shot, so it stays face-up
- 狂时钟 2511: discard it so that this turn, while you control a Labrynth monster, you can activate 1 set Normal Trap the turn it was set; it recurs when you pay hand cards as costs for Labrynth effects or trap activations
- 魔神像 48745395: special summons itself from hand when any trap activates, on summon sets a battle trap (attack-declaration only) from deck, gains 400 ATK per distinct trap type in GY and forces the opponent to attack it instead of other Fiends
- 欢迎欢送 32785578: negate an attack, destroy 1 card, then set 1 non-Labrynth Normal Trap from hand or deck
- Hand-trap negation line: 灵王的波动 40366667, 列王诗篇 58053438, 霆王的闪光 6325660, 异次元竞技场 31849106, all hand-activatable only under their printed conditions and each locks attributes afterwards

- **Halt Points**

- 灰流丽 14558127 on 阿里安娜 1225009 search kills the plus one but leaves the 1600 body, the turn still functions with 火吹炉 74018812 or 龙饰灯 37629703 in hand
- 无限泡影 10045474 or 效果遮蒙者 97268402 on 火吹炉, 龙饰灯 or 阿里亚娜 stop their set or summon effects; 灰流丽 cannot stop 火吹炉's set from deck because setting is outside Ash's scope
- Remove 白银之城的拉比林斯 2347656 first (Imperm its column, 闭锁世界的冥神 98127546, 超融合 48130397, 月女神之镞 2263869) and the traps become chainable by monster effects again
- 迷宫城的白银姬 81497285 loses both protections while you control no face-down card, so keep at least one trap set
- Trap-negation and anti-trap cards shut the whole engine; 次元吸引者 91800273-style GY banning kills the recursion (欢迎 GY set, 布置, 大欢迎 ②)
- Under 增殖的G 23434538 play minimal, the deck naturally special summons 1-3 monsters per turn, settle for set traps plus one summon

- **Mirror Match**

- The player who resolves 白银之城的拉比林斯 2347656's trap protection first keeps trap priority, whoever ③-destroys the opponent's Level 8 first wins the grind
- Destroying the opponent's monsters with your traps also triggers your own recursion (no owner restriction on the leave-field trigger), so ③ destroy and 教导的惩罚 82956214 keep your 欢迎 and 阿里安娜 loop running in the mirror
- 白银姬 vs 白银姬: keep a face-down so your boss stays untargetable, and use its ③ to set 次元障壁 83326048 or 教导的惩罚 82956214
- Destroying opponent monsters also feeds their 大欢迎 92714517 GY targets, weigh the recursion you gain against the GY fuel you give them
- 魔神像 48745395 enters on any trap activation in the mirror and points attacks at itself

- **Common Mistakes**

- After activating 欢迎 5380979 only Fiends can be special summoned from deck or extra until the end of the next turn, do not plan non-Fiend extra plays like 访问码语者 86066372 behind it
- 欢迎 ② cannot set itself from GY on the turn it was sent there
- 白银之城的拉比林斯 ② recycles a trap that cannot activate without a face-up Fiend, check the board before setting from GY
- 阿里亚娜 75730490 sends a trap as cost and only summons Level 4 or lower Fiends, never 阿里亚斯 73602965 or the Level 8 monsters
- 连环阵 68779682 must chain to a set trap you activated, not one activated from hand, and afterwards your effect damage to the opponent is zero
- 布置 69895264 shuffles exactly two Labrynth spells or traps and sets the same count of different non-Labrynth traps, do not shuffle away recursion you still need
- 大欢迎 ② banishes itself from GY, spend it on the bounce or the removal, not both
- The recursion triggers need a monster to leave the field by a trap effect, bouncing via 大欢迎 counts but destroying your own set trap does not
- 白银姬 81497285 protection needs a face-down card, and 魔神像 48745395 must be on field before trap resolution to use its ① special summon
