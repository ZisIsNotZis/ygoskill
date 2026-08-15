---
name: sunavalon-experience
description: 圣天树 (Sunavalon) deck experience: plant link engine, one-card combo, end field lock, extenders, halt points
---
# 圣天树 (Sunavalon) Deck Experience

- **Deck Identity**

- Sunavalon is a Plant link engine that climbs from 圣天树之幼精 93896655 to the Link-4 boss 圣天树之大母神 92770064 using 圣种 (Sunseed) Normal monsters and 圣蔓 (Sunvine) links, then wins with the 圣天树的开花 54340229 negate-all lock and a boosted 圣蔓之剑士 91557476 OTK
- Main deck monsters: 圣种之地灵 27520594 (the Level 1 Normal Plant seed), 圣种之影芽 30013902, 圣种之天双芽 66407907, 圣蔓之少女 53618293 (hand trap)
- Extra deck: 圣天树 links 幼精 93896655, 月桂精 7984540, 精灵 39880350, 灰树精 44478599, 大精灵 65285459, 大母神 92770064 plus 圣蔓 links 剑士 91557476, 治愈者 65563871, 守护者 28168762
- Key spells and traps: 圣蔓的播种 53286626 (starter), 圣蔓的交配 70473293 (revive), 圣蔓之社 27946124 (recursion), 圣天树的开花 54340229 (lock finisher, a continuous TRAP not a field spell)
- Setcodes in scripts: 圣天树 0x2158, 圣蔓 0x1158, 圣种 0x4158, every search and special summon filter uses these
- Repo decks live under deck folders dated YYMMDD; pure engine builds are 201205/201228/210717 圣天树, hybrids add 六花 (Rikka), 王战, 芳香, 兽带斗神, and 2024-25 builds add 蕾祸 (Rayho) and 原石 (Primite)

- **Core Mechanic: Plant Link Engine**

- Starter spells put 圣种之地灵 27520594 on the field: 粗人预料 911883 needs an empty field, 救援兔 85138716 special summons two, 圣蔓的播种 53286626 special summons one from deck for 1000 LP
- 幼精 93896655 is a Link 1 (material 1 Plant Level 4 or lower) that searches a 圣蔓 spell or trap only when summoned with 圣种之地灵 as material into the Extra Monster Zone, verified in script c93896655
- The damage loop: 播种 53286626's 1000 LP cost triggers the damage effects of 幼精 (once per turn), 精灵 (up to 2 per turn), 大精灵 (up to 3 per turn) which each recover that LP and special summon a 圣蔓 link from the Extra Deck for free
- Link climb with verified materials: 幼精 (1) to 精灵 39880350 (2 Plants incl a 圣天树 link) to 灰树精 44478599 (2-3 Plants incl a link monster, revives 地灵 from GY on summon) to 大精灵 65285459 (2+ Plants) to 大母神 92770064 (2+ link monsters)
- 剑士 91557476 and 治愈者 65563871 are Link 1s made from exactly 1 Plant Normal monster, so every recycled 地灵 27520594 becomes a Sunvine body
- All 圣天树 links cannot be targeted for attacks, so the opponent must remove them by effect while 剑士 91557476 and 守护者 28168762 are the only real attackers and the defense line
- 治愈者 65563871 gains LP equal to link rating times 300 when summoned and 600 per battle damage dealt by a Plant link, making LP a reusable resource
- 大母神 92770064 is Link 4 with 0 ATK, indestructible by opponent card effects, untargetable for attacks, and once per turn tributes a link monster in its own linked zones to destroy up to that monster's link rating opponent cards

- **One-Card Combo: 粗人预料**

- Step 1: activate 粗人预料 911883 on an empty field to special summon 圣种之地灵 27520594 from deck
- Step 2: link summon 圣天树之幼精 93896655 into the Extra Monster Zone using 地灵 as the sole material, search 圣蔓的播种 53286626 from deck
- Step 3: activate 播种, special summon a second 圣种之地灵 from deck and pay 1000 LP, the damage triggers 幼精's effect to recover 1000 LP and special summon 圣蔓之治愈者 65563871 from the Extra Deck
- Step 4: link summon 圣天树之精灵 39880350 in the Extra Monster Zone using 幼精 and 治愈者, replacing them as the damage trigger source
- Step 5: link summon 圣天树之灰树精 44478599 using 精灵 and the second 地灵, its summon effect revives 圣种之地灵 from the graveyard
- Step 6: link summon 圣蔓之剑士 91557476 using the revived 地灵, its summon effect raises its ATK by 800 times 灰树精's link rating to 3200
- Step 7: link summon 圣天树之大母神 92770064 using 灰树精 and 剑士, its summon effect searches 圣天树的开花 54340229, then activate 开花 while 大母神 is on field to negate every face-up monster the opponent controls
- Ash Blossom on step 1, 2, or 3 ends the whole line and leaves only a lone 幼精

- **End Field**

- 大母神 92770064 in the Extra Monster Zone plus 圣天树的开花 54340229 face up is the lock: opponent monsters negated on activation, 大母神 indestructible and popping up to 4 cards per turn
- 开花 54340229 also has a quick effect at damage calculation that makes a battling Plant link gain the combined ATK of its linked zone monsters
- Full OTK field adds 圣蔓之剑士 91557476 linked under the boss at 4000 ATK, plus 灰树精 44478599 kept alive to grant 剑士 attacks up to the number of 圣天树 links you control, usually two for 8000 damage
- To keep 灰树精 for the OTK, make 大母神 from 大精灵 65285459 plus a second 治愈者 65563871 instead of consuming 灰树精, which needs one extra body from 圣蔓之社 27946124 or 圣种之天双芽 66407907
- Grind setup: 圣蔓之社 27946124 recurs a continuous trap from the graveyard every opponent end phase, so 开花 54340229 or 魔封的芳香 58921041 comes back each turn
- Modern 2024-25 hybrids add 原石的皇脉 56506740 and 神树兽 许珀利冬 9349094 or 小仙人掌封闭者 31615285 to the end board

- **Extenders**

- 圣种之天双芽 66407907: on summon with a 圣天树 link on field revives a Level 4 or lower Plant Normal, its grave effect banishes itself plus a link monster to re-summon a same-name Plant link, the repeat source of 地灵 and 剑士 bodies
- 圣种之影芽 30013902: special summons itself from hand while a Plant Normal is on field, its grave effect banishes itself to re-summon a linked 圣天树 or 圣蔓 link of rating 2 or less from the Extra Deck
- 圣蔓之社 27946124: discard 1 card to activate while a 圣天树 link is on field, revives a Plant Normal once per turn, and its end phase effect re-sets a continuous trap from the graveyard, the grind engine for 开花 54340229 and 魔封的芳香 58921041
- 圣蔓的交配 70473293: once per turn tributes a link monster to special summon a Plant from the graveyard with negated effects, best used for link material because revived 剑士 91557476 loses its ATK boost trigger
- 圣天树之月桂精 7984540: once per turn tributes a monster to return 2 Plant links from the graveyard to the Extra Deck, the recycling tool for the next turn's climb
- 救援兔 85138716 and 一对一 2295440 and 孤火花 48686504 are alternate one-card starters that put 圣种之地灵 27520594 on the field
- 蔷薇少女 29177818 special summons itself when a face-up Plant is sent to the graveyard and returns itself from grave, extra link fodder
- 超营养太阳 28529976 tributes a Level 2 or lower Plant to summon a bigger Plant from deck, a pure-build side tool
- 芳香炽天使-茉莉 21200905 is a generic Link 2 Plant that special summons a Plant from deck and searches one whenever you gain LP, the modern hybrid bridge

- **Halt Points**

- 灰流丽 14558127 on 粗人预料 911883, on 幼精's search, or on 播种 53286626 stops the engine cold because 地灵 27520594 bodies stop flowing
- 增殖的G 23434538 draws a card for every one of the roughly nine special summons in the full line, play a shortened lock-only line under it
- 原始生命态 尼比鲁 27204311 wipes the board on the fifth special summon, leave 播种's grave effect or 天双芽 66407907 to rebuild
- 效果遮蒙者 97268402 and 无限泡影 10045474 chain to 灰树精's 地灵 recursion or to 大母神's search and pop, so resolve those triggers before committing more summons
- 屋敷童 73642296 negates grave-activated effects like 天双芽's second effect, but not field-activated recursion like 灰树精's summon effect
- 小丑与锁鸟 94145021 limits the searches from 幼精, 大母神, 圣蔓之社, 蕾祸, and 六花 engines in the same turn
- An opponent 小仙人掌封闭者 31615285 blocks all special summons outright while they control another Plant, and 魔封的芳香 58921041 forces you to set spells first

- **Mirror Match**

- Every 圣天树 link cannot be attacked, so the mirror is decided by effects and the 剑士 91557476 OTK, never by normal battle
- The first player to resolve 大母神 92770064 plus 圣天树的开花 54340229 wins, because 开花 negates the opponent's whole board while 大母神 keeps popping up to 4 cards
- Counter the opponent's 开花 activation with 神之宣告 41420027 or 花粉症 91078716 tributing a Plant, and activate your own 开花 before theirs
- Use 大母神's pop to strip the opponent's 剑士 91557476 and 治愈者 65563871 so their OTK and LP engine die first
- 圣蔓之少女 53618293 negates the opponent's targeting effects aimed at your Extra Deck summoned Plants, which answers 泡影 and 遮蒙者 in the mirror
- The opening exchange is the 粗人预料 race, 灰流丽 and 锁鸟 on the starter decide the game, whoever keeps the 圣种之地灵 27520594 climb wins

- **Common Mistakes**

- 幼精 93896655 searches only when summoned with 圣种之地灵 as material inside the Extra Monster Zone, any other summon gives no search
- 粗人预料 911883 requires an empty field, never normal summon first
- 播种 53286626 locks your Extra Deck summons to Plants for the turn, and without a face-up 圣天树 link it can only special summon 圣种之地灵
- Order 播种's 1000 LP payment before other plays so the damage triggers of 幼精, 精灵, or 大精灵 fire and pay out free Sunvines
- Summon 剑士 91557476 while 大母神 92770064 is already on field for the full 4000 ATK, a 1600 剑士 boosted by a Link 1 does not OTK
- 灰树精 44478599's multi-attack targets a 圣蔓 link in its own linked zones and the attack count equals your 圣天树 link count, zone placement decides the OTK
- 大母神's pop tributes a link monster inside 大母神's own arrow zones, so link 剑士 or 治愈者 under it before relying on the removal
- 开花 54340229 checks for a Link 4 or higher Plant link at resolution, summon 大母神 first then activate, and a set trap cannot activate the turn it is set
- 圣蔓之少女 53618293 negates only opponent targeting effects, it does nothing against 灰流丽 or 增殖的G
- 圣蔓的交配 70473293 revives with negated effects, the revived 剑士 loses its boost and 治愈者 loses its LP gain, use it for material instead
- 月桂精 7984540's recycle tributes a monster, do not strip your field bare in a losing position
- 圣蔓之社 27946124's end phase recursion needs a continuous trap already in the graveyard, send 开花 or 魔封的芳香 there before the opponent's end phase
- 播种 53286626's grave effect can banish itself to replace the destruction of a Plant link, keep it in the graveyard as protection
- 大母神 92770064 is Link 4 not Link 5, the common misremembering changes which lock pieces you can build with it
