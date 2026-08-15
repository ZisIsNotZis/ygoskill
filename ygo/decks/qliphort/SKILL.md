---
name: qliphort-experience
description: 机壳 (Qliphort) deck experience: pendulum tribute engine, pend-lock floodgate, extenders, halt points
---
# 机壳 (Qliphort) Deck Experience

- **Deck Identity**

- 机壳 is the Qliphort archetype in this codebase: Machine-type EARTH Effect Pendulum monsters, all sharing setcode 0xaa; note this DB runs them as EARTH, not the real-world LIGHT
- Naming note: 机壳工具 丑恶 65518099 is the deck searcher (Scout role), 机壳别名 愚钝 13073850 is the tribute-summon bounce (Monolith role), 机壳的牲祭 17639150 is the equip (Saqlifice), 机壳的要塞 43034264 is the field spell, and the Apoqliphort bosses are 隐藏的机壳内核 无神论 40061558 and 隐藏的机壳杀手 物质主义 27279764
- Non-monster support: field 机壳的要塞 43034264, equip 机壳的牲祭 17639150, traps 机壳的再星 20426907 / 机壳的冻结 20447641 / 起动的机壳 30845999 / 隐藏的机壳 04450854, link 机壳守护神 路径灵 22423493
- Deck type: control/stun hybrid — tribute-summoned bosses beat down behind summon-negation floodgates, not a long combo deck
- Build quirk: the pend-lock forbids special summoning non-机壳 monsters, so the only practical extra-deck monster is 机壳守护神 路径灵 22423493; any non-机壳 link or fusion must be made before scales are set
- Build quirk: 2014-era lists run 技能抽取 82732705 with stun traps; 2026 lists keep the same engine and add floodgates 技能抽取 82732705 and 群雄割据 90846359 (all 机壳 are Machine, so Rivalry never hurts you)

- **Core Mechanic: Pendulum Tribute Engine and the Pend-Lock**

- Every 机壳 Pendulum scale carries the lock "you cannot Special Summon monsters except 机壳", cannot be negated (EFFECT_CANNOT_SPECIAL_SUMMON, player-targeted, setcode 0xaa filter)
- Every 机壳 Pendulum monster can be Normal Summoned without tribute; a no-tribute Normal Summon or any Special Summon makes it Level 4 with 1800 ATK and no protection
- A tribute summon that tributed at least one 机壳 monster keeps its printed Level and ATK and becomes immune to activated monster effects from monsters with lower original Level or Rank (aux.qlifilter)
- The immunity never blocks Link monster effects, so link-based removal always works against tribute-summoned Qliphorts
- Tribute fodder is the engine: tributed pendulums go face-up to the Extra Deck, then Pendulum Summon back between any scale 1 and scale 9 as Level 4 1800 bodies, or return to hand via 隐藏的机壳 04450854
- Scales come in 1 and 9: scale 1 is 机壳磁盘 无感动 64496451 / 机壳别名 愚钝 13073850 / 机壳档案 色欲 91907707 / 机壳汇编器 不安定 51194046, scale 9 is 机壳工具 丑恶 65518099 / 机壳基因组 贪欲 37991342 / 机壳壳层 拒绝 90885155 / 机壳存取 残酷 87588741
- The floodgate is 机壳的再星 20426907: negates the effects of Level 4 or lower Normal and Flip Summons, negates and banishes Level 5 or higher Special Summons when they leave the field, and destroys itself if no other face-up 机壳 card is on your field
- 技能抽取 82732705 pairs with the Apoqliphort bosses: the bosses are Spell/Trap immune so they keep their effects under Skill Drain while every other face-up monster is negated

- **One-Card Combo: 机壳工具 丑恶 opener**

- Starter: 机壳工具 丑恶 65518099 in hand; set it in a Pendulum Zone, pay 800 LP, add any 机壳 card from deck to hand, preferably 机壳磁盘 无感动 64496451, 机壳的要塞 43034264 or 机壳的牲祭 17639150
- The deck has no true one-card boss: Tool alone ends on one scale 9 plus one searched card; every boss line needs a second card
- Two-card line to a boss: Tool search plus a 机壳 body, no-tribute Normal Summon the body as Level 4 1800, tribute it for 机壳磁盘 无感动 64496451, whose tribute-summon effect special summons 2 机壳 from deck (destroyed at End Phase)
- With 机壳的要塞 43034264 active, its extra Qliphort Normal Summon lets you tribute the 2 Disk bodies plus one more 机壳 for the Apoqliphort boss in the same turn
- Two-card Freeze line: set and activate 机壳的冻结 20447641 to special summon itself as a Level 4 1800 Machine, then tribute it alone (it counts as 3 tributes) for 隐藏的机壳内核 无神论 40061558 or 隐藏的机壳杀手 物质主义 27279764
- Saqlifice math: 机壳的牲祭 17639150 makes its equipped monster count as 2 tributes, so one equipped 机壳 plus one body tribute summons 机壳磁盘 无感动 64496451, and the equip searches another 机壳 monster when it is sent to the grave

- **End Field**

- Ideal going-first board: 隐藏的机壳内核 无神论 40061558 (tribute 3 机壳, Spell/Trap immune, once per turn take control of 1 opponent monster until End Phase) or 隐藏的机壳杀手 物质主义 27279764 (Spell/Trap immune, all special-summoned monsters lose 500 ATK/DEF, once per turn force the opponent to send 1 monster from hand or field to grave)
- Set 机壳的再星 20426907, plus 技能抽取 82732705, plus a face-up scale or 机壳的要塞 43034264 so 机壳的再星 does not destroy itself
- Fallback board: tribute-summoned 机壳壳层 拒绝 90885155 (double attack, piercing) or 机壳磁盘 无感动 64496451 with 机壳的再星 20426907 and set traps

- **Extenders**

- 机壳的要塞 43034264: extra Qliphort Normal Summon each turn, Qliphort summons cannot be negated, and it keeps 机壳的再星 20426907 alive
- 机壳的冻结 20447641: special summons itself as a monster, protects your 机壳 spells and traps from destruction that turn, and counts as 3 tributes for the Apoqliphort bosses
- 机壳的牲祭 17639150: +300 ATK, cannot be destroyed by battle, doubles the equipped monster as tribute for 机壳 tribute summons, searches a 机壳 monster when sent to the grave from the field
- 隐藏的机壳 04450854: once per turn, add up to 3 face-up 机壳 Pendulum monsters from your Extra Deck to your hand — recursion after tribute chains
- 机壳基因组 贪欲 37991342: when tributed, destroy 1 Spell or Trap on the field — tribute it to clear the opponent 机壳的再星 20426907 or 技能抽取 82732705
- 机壳档案 色欲 91907707: when tributed, return 1 monster on the field to the hand — its bounce beats any monster whose Level is not lower than its own, including the Level 9 boss
- 机壳汇编器 不安定 51194046: during the End Phase of a turn you tribute-summoned, draw 1 card for each 机壳 tributed that turn — tribute 3 for the boss and draw 3
- 机壳壳层 拒绝 90885155: tribute summon it for double attack and piercing damage that turn
- 机壳存取 残酷 87588741: on tribute summon, gain LP and deal damage equal to the grave-count difference
- 机壳守护神 路径灵 22423493: Link-2 of 2 Machines, unaffected by Spell/Trap effects and by opponent Link monster effects, once per turn negates 1 face-up card you control and 1 the opponent controls, and when 2 monsters are special summoned simultaneously to its linked zones (机壳磁盘 无感动 64496451 effect) searches any Level 5 or higher Machine from deck
- 起动的机壳 30845999: give a normal-summoned 机壳 +300 ATK and immunity to the opponent Spell/Trap effects for the turn (its own effects get negated, so use it as a protected beater)

- **Halt Points**

- 机壳工具 丑恶 65518099 scale search is the only search; negate or destroy it and the deck loses a turn of advantage
- 机壳磁盘 无感动 64496451 tribute-summon effect is the engine; negating the summon or the effect costs the 2 bodies and the follow-up
- The tribute summons themselves: without 机壳的要塞 43034264, negating the Apoqliphort tribute summon (40061558/27279764) wastes all 3 tributes
- Removal that does not target monster effects (compulsory return, bottomless-type traps) is the premium answer because tribute-summoned Qliphorts are only immune to monster effects, not Spell/Traps
- 机壳的再星 20426907 self-destructs without another face-up 机壳 card, and 技能抽取 82732705 or 群雄割据 90846359 do not count, so destroy the scales and the field to kill the trap
- The deck special summons little, so draw-to-G-type cards give few draws, but each pendulum summon and Disk body still feeds them — under G, skip pendulum plays and end on one tribute summon
- Tool pays 800 LP per search; skip the search when the line does not need it and LP is low

- **Mirror Match: 机壳 vs 机壳**

- 机壳的再星 20426907 negates Level 4 or lower Normal Summons, which catches the opponent's no-tribute Level 4 1800 bodies, but never their tribute summons (Level 5 or higher but a Normal Summon, so the Level 5+ Special Summon clause misses them)
- The immunity is Level-relative: 隐藏的机壳内核 无神论 40061558 (Level 9) can steal control of another Kernel because equal Level is not protected, and the bounces of 机壳档案 色欲 91907707 and 机壳别名 愚钝 13073850 resolve against any monster of equal or higher Level
- 机壳基因组 贪欲 37991342 is the mirror answer: tribute it to destroy the opponent's 机壳的再星 20426907, 技能抽取 82732705 or 机壳的要塞 43034264
- Whoever tribute summons first usually wins — preserve 机壳的牲祭 17639150 equipped fodder (counts as 2 tributes) to guarantee the second tribute summon via 机壳的要塞 43034264
- Each pend-lock is player-targeted, so neither player's scale locks the other; the mirror is decided by tribute summons and Spell/Trap control, not by the lock

- **Common Mistakes**

- Do not set scales and then plan non-机壳 special summons (links, fusions, Xyz) — the pend-lock forbids every non-机壳 special summon while a 机壳 scale is up
- Do not expect the ④ effects from no-tribute Normal Summons: 机壳磁盘 无感动 64496451, 机壳别名 愚钝 13073850 and 机壳壳层 拒绝 90885155 only trigger on a tribute summon that tributed a 机壳 monster
- Tributed pendulums go face-up to the Extra Deck, so fodder never reaches the grave; recursion comes from 隐藏的机壳 04450854 and pendulum summons, and 机壳的牲祭 17639150 only searches when it is sent to the grave from the field
- 机壳磁盘 无感动 64496451 special-summoned monsters are destroyed at the End Phase — attack, tribute or link with them first
- Tribute-summoned Qliphorts are not Spell/Trap immune (only the Apoqliphort bosses and 机壳守护神 路径灵 22423493 are) — they still die to compulsory-return and bottomless-type cards
- Link monster effects bypass the Qliphort immunity entirely — never rely on it against link-based removal
- 机壳的再星 20426907 destroys itself without another face-up 机壳 card — keep a scale, the field spell or a monster up at all times
- Do not pendulum summon without a purpose: the summoned monsters arrive as Level 4 1800 vanillas and only serve as tribute fodder
- 技能抽取 82732705 also negates your own tribute-summoned Qliphort effects — resolve 机壳磁盘 无感动 64496451 before flipping Skill Drain, or play the Apoqliphort bosses that keep their effects
- The Apoqliphort bosses cannot be special summoned and need exactly 3 机壳 tributes (or 机壳的冻结 20447641 as 3) — they can never be pendulum summoned back from the Extra Deck
