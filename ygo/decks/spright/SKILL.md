---
name: spright-deck-experience
description: 卫星闪灵 (Spright) deck experience: Level-2 swarm engine, one-card combo, extenders, halt points
---
# 卫星闪灵 (Spright) Deck Experience

- **Deck Identity**

- Level-2 swarm combo deck, all main deck Spright monsters are Level 2 Thunder (setcode 0x180), 卫星闪灵·蓝色喷流灵 76145933, 卫星闪灵·喷流灵 13533678, 卫星闪灵·红色精灵 75922381, 卫星闪灵·萝卜精灵 2311090, 卫星闪灵·皮克精队 49928686
- Extra deck ladder, Link-2 卫星闪灵·淘气精灵 27381364 and Link-2 卫星闪灵迅妖龙炮 72329844, Rank-2 Xyz 巨大喷流卫星闪灵 54498517, plus the 青蛙 engine finisher 饼蛙 90809975
- Spells, 卫星闪灵启辉器 15443125 is the one-card starter, 卫星闪灵粉碎者群集 88836438 and 卫星闪灵双人交叉金臂勾 68250822 are the quick-play interaction, 卫星闪灵伽马暴 42431833 is the OTK pump
- This client cards.cdb has exactly 12 卫星闪灵 cards, the task-named 卫星闪灵·极光, 卫星闪灵·闪耀, 卫星闪灵·纳尔佩 and 流星/辉光 supports do not exist in this codebase, use the 12 names above
- Typical build pairs Spright with the 青蛙 engine (粹蛙 1357146, 鬼青蛙 9126351, 魔知青蛙 46239604) and the 迅捷 engine (迅捷河狸 68353324, 迅捷鮟鱇 88686573), plus 深海歌后 78868119 as a normal-summon extender, sample list in deck/260320卫星闪灵青蛙迅捷

- **Core Mechanic: Level-2 Lock and the Swarm**

- Every main deck Spright monster can special summon itself from hand while you control a face-up Level 2, Rank 2 or Link 2 monster, the exact requirement differs per card so read the scripts before extending
- 卫星闪灵·蓝色喷流灵 76145933 needs a Level 2 or Rank 2 on field, on special summon it adds any other 卫星闪灵 monster from deck to hand, this is the deck's main searcher
- 卫星闪灵·喷流灵 13533678 also needs a Level 2 or Rank 2, on special summon it adds any 卫星闪灵 spell or trap from deck to hand, usually 卫星闪灵启辉器 15443125 or 卫星闪灵粉碎者群集 88836438
- 卫星闪灵·红色精灵 75922381 and 卫星闪灵·萝卜精灵 2311090 need a Level 2 or Link 2 on field, both are hand-trap negates that tribute another Level 2, Rank 2 or Link 2 monster, 红色精灵 negates monster effects and 萝卜精灵 negates spell and trap effects, tributing a Rank 2 or Link 2 adds destruction
- 卫星闪灵·皮克精队 49928686 needs a Level 2 or Rank 2, its battle trick sends itself from hand or field to grave to give another Level 2, Rank 2 or Link 2 the opponent monster's attack during damage calculation
- 卫星闪灵启辉器 15443125 special summons any 卫星闪灵 monster from deck and pays life points equal to its original attack, then locks you to Level 2, Rank 2 or Link 2 special summons until the end of the turn, verify the lock before making non-Level-2 plays
- 卫星闪灵迅妖龙炮 72329844 on link summon sends a Level 2 monster from deck to grave, and while on field whenever another monster is special summoned it can detach one Xyz material you control to return one monster on field to hand, use the detach on 巨大喷流卫星闪灵 54498517 after it gained materials
- 卫星闪灵·淘气精灵 27381364 stops the opponent targeting monsters in its linked zones, and during either main phase can special summon a Level 2 from your grave, if the opponent controls a monster it can instead summon a Rank 2 or Link 2, this is the end-board protection piece
- 巨大喷流卫星闪灵 54498517 is a Rank 2 Xyz that also accepts Link 2 monsters as material, its attack doubles to 3200 if it has a fusion, synchro, xyz or link monster as material, its ignition effect detaches one material to special summon a Level 2 from deck then locks both players to Level 2, Rank 2 or Link 2 until end of turn

- **One-Card Combo: 卫星闪灵启辉器 15443125**

- Starter, 卫星闪灵启辉器 15443125 in hand, no other cards needed
- Step 1, activate 启辉器, special summon 卫星闪灵·蓝色喷流灵 76145933 from deck and pay 1100 life, the Level 2 lock applies for the rest of the turn
- Step 2, 蓝色喷流灵 on summon adds 卫星闪灵·喷流灵 13533678 from deck to hand
- Step 3, special summon 喷流灵 from hand because 蓝色喷流灵 is a Level 2, on summon it adds 卫星闪灵粉碎者群集 88836438 or 卫星闪灵双人交叉金臂勾 68250822 from deck
- Step 4, link both Level 2 monsters into 卫星闪灵迅妖龙炮 72329844, its link summon effect sends 迅捷鮟鱇 88686573 from deck to grave
- Step 5, 迅捷鮟鱇 in grave triggers and special summons up to 2 迅捷河狸 68353324 from deck
- Step 6, overlay 迅妖龙炮 as a Link 2 material plus one 迅捷河狸 into 巨大喷流卫星闪灵 54498517, its attack doubles to 3200 because a link monster is material, detach one to special summon 粹蛙 1357146 or 魔知青蛙 46239604 from deck, both players now locked to Level 2, Rank 2 or Link 2
- Step 7, link the remaining 迅捷河狸 and the summoned 粹蛙 or 魔知青蛙 into 卫星闪灵·淘气精灵 27381364, use its quick effect to revive a Level 2 from grave into its linked zone, usually the spent 蓝色喷流灵 or 喷流灵

- **End Field**

- One-card line, 巨大喷流卫星闪灵 54498517 at 3200 attack with one material left plus 卫星闪灵·淘气精灵 27381364 protecting it from targeting plus one revived Level 2 in the linked zone, hand keeps 卫星闪灵粉碎者群集 88836438 or 卫星闪灵双人交叉金臂勾 68250822 and any 红色精灵 75922381 or 萝卜精灵 2311090
- Two-card frog line, 鬼青蛙 9126351 plus any water discard special summons 鬼青蛙, its summon sends 粹蛙 1357146 from deck to grave, 粹蛙 banishes a frog from grave to special summon itself, both overlay into 饼蛙 90809975 which negates one monster effect or spell trap activation per turn by sending an aqua from hand or field to grave
- 饼蛙 90809975 on resolution also special summons the negated monster face-down to your field when it was a monster, turning one negate into a steal, and when it leaves the field it adds one water from grave to hand
- 卫星闪灵伽马暴 42431833 pushes 1400 attack and defense onto every Level 2, Rank 2 or Link 2 on the field, use it after the lock resolves for the damage push, its grave effect can give one monster 1400 attack until the opponent's end phase
- 天霆号 阿宙斯 90448279 can overlay onto a 巨大喷流 that attacked this turn and wipe the field with two detaches, and 扫兴书呆魔术师 72167543 can overlay onto a Rank 3 or lower Xyz in main phase 2

- **Extenders**

- 卫星闪灵·蓝色喷流灵 76145933 is the main extender, any board with a Level 2 or Rank 2 lets it summon itself and search a new Spright monster, keep one in hand off the 启辉器 line
- 卫星闪灵·喷流灵 13533678 extends the same way and fetches spells, a second 启辉器 found by 喷流灵 can restart the full line from an empty field
- 迅捷河狸 68353324 on normal summon special summons another 迅捷 engine monster from deck or grave, and 迅捷鮟鱇 88686573 special summons up to 2 迅捷 engine monsters when sent from hand or deck to grave, these are the extra bodies that make the second Link 2 possible
- 深海歌后 78868119 on normal summon special summons a Level 3 or lower sea serpent from deck, two Level 2 bodies from one normal summon into 迅妖龙炮 72329844 or 淘气精灵 27381364
- 鬼青蛙 9126351 can discard a water monster to special summon itself, its summon sends a Level 2 or lower water aqua from deck to grave, and it can bounce one monster you control for an extra frog normal summon, 粹蛙 1357146 banishes a frog from grave to special summon itself from grave, 魔知青蛙 46239604 adds a frog from deck or grave to hand when sent from field to grave and forces attacks onto itself while on field
- 卫星闪灵粉碎者群集 88836438 is a quick-play that banishes a 护宝炮妖, 兽带斗神 or 卫星闪灵 card from hand or grave as cost then either special summons a 护宝炮妖 from deck, special summons a 兽带斗神 from grave, or banishes one of your Level 2, Rank 2 or Link 2 monsters plus one opponent card, the removal mode is the main use
- 卫星闪灵双人交叉金臂勾 68250822 is a quick-play with three modes, attach a monster from either field or grave to your Rank 2 Xyz as material, take control of an opponent monster into a zone your Link 2 points to, or special summon a grave monster into a zone your Link 2 points to, the steal and attach modes break mirrors
- 卫星闪灵·红色精灵 75922381 and 卫星闪灵·萝卜精灵 2311090 in hand are the reactive extenders, they summon themselves on the opponent's turn as long as a Level 2 or Link 2 sits on your field and then negate, do not tribute your only interaction piece to negate
- 神鸣 89753095 searches any thunder monster from deck, which includes every Spright monster, but the searched monster cannot be normal summoned until the end of the next turn, use it to grab a hand special summoner like 蓝色喷流灵 or 喷流灵

- **Halt Points**

- Ash Blossom 14558127 on 启辉器 15443125 stops the one-card line entirely, Ash on 蓝色喷流灵 76145933 search, 喷流灵 13533678 search or 迅捷鮟鱇 88686573 summon also breaks extension
- 增殖的G 23434538 punishes the swarm, the one-card line makes 6 to 7 special summons so under G stop at 巨大喷流 54498517 or earlier, chain 墓穴的指名者 24224830 or 抹杀之指名者 65681983 to protect the combo
- 欢聚友伴·茸茸长尾山雀 42141493 draws the opponent a card for each special summon from deck or extra deck, the Spright line special summons from deck repeatedly so stop the line or accept the draw count, 小丑与锁鸟 94145021 also shuts off the search and summon effects that follow
- 尼比鲁 27204311 triggers on the fifth special summon, count summons carefully, the 启辉器 line reaches five at 迅捷鮟鱇 88686573's summons, hold 墓穴的指名者 or stop before the fifth summon
- The Level 2 lock is the deck's own halt, after 启辉器 or 巨大喷流 resolves you cannot make non-Level-2 plays like 访问码语者 86066372 or a Link 3 or higher, sequence all Link 3 and higher summons before the lock
- 灵王的波动 40366667 from hand negates any effect that special summons when the opponent controls a card, it can answer 启辉器, 蓝色喷流灵 and 迅捷鮟鱇 all at once, the deck itself runs it as a defensive option

- **Mirror Match: 卫星闪灵 vs 卫星闪灵**

- The mirror is decided by who resolves 启辉器 15443125 first and who holds 红色精灵 75922381 or 萝卜精灵 2311090 in hand, the negate monsters trade one-for-one against the opponent's searches and summons
- 红色精灵 75922381 answers 蓝色喷流灵 76145933 and 喷流灵 13533678 searches and 巨大喷流 54498517 summons, 萝卜精灵 2311090 answers 启辉器 and 卫星闪灵粉碎者群集 88836438 activations
- 卫星闪灵双人交叉金臂勾 68250822 steals the opponent's 巨大喷流 54498517 by attaching it as Xyz material or taking control into your Link 2 zone, attach mode also removes their materials and sends them to grave
- 卫星闪灵粉碎者群集 88836438 banishes a Spright from hand or grave plus one opponent card, the removal is a clean answer to a fully built 巨大喷流 board because it does not target
- 饼蛙 90809975 negates and steals in the mirror, its negate sends an aqua from hand or field to grave and the stolen monster comes to your field face-down, keep an aqua in hand to fuel it
- Do not activate 巨大喷流 54498517's effect carelessly in the mirror, the lock applies to both players so resolving it freezes your own non-Level-2 plays too, use it only when the lock favors you

- **Common Mistakes**

- Forget the Level 2 lock and try to link into 访问码语者 86066372, W：P变幻舞夜 4993187 or any Link 3 or higher after 启辉器 15443125 or 巨大喷流 54498517 resolved, the restriction is hard and the summon fails
- Misread the self-summon requirement, 蓝色喷流灵 76145933 and 喷流灵 13533678 need a Level 2 or Rank 2 while 红色精灵 75922381 and 萝卜精灵 2311090 need a Level 2 or Link 2, a bare 巨大喷流 is Rank 2 so only the searchers can follow it
- Search 卫星闪灵粉碎者群集 88836438 with 喷流灵 13533678 and then find no 护宝炮妖, 兽带斗神 or 卫星闪灵 card in hand or grave to banish as cost, check the cost before searching
- Activate 卫星闪灵启辉器 15443125 when the extra deck and main deck cannot support the full line, the card is the only real starter so a second 启辉器 from 喷流灵 search is the recovery route
- Tribute the only other Level 2, Rank 2 or Link 2 monster to use 红色精灵 75922381 or 萝卜精灵 2311090, the negate leaves you empty and the tribute does not have to be a Spright but must exist
- Use 卫星闪灵迅妖龙炮 72329844's bounce effect before 巨大喷流 54498517 gains materials, the detach cost needs an Xyz material so sequence the detach after Gigantic absorbs materials
- Overlay 迅妖龙炮 72329844 or 淘气精灵 27381364 as link material on the same turn they were link summoned, both cards forbid being link material in the turn they link summoned
- Expect 深海歌后 78868119 to search, it only special summons a sea serpent from deck on normal summon, it cannot grab 卫星闪灵 cards
- Play 卫星闪灵伽马暴 42431833 expecting the attack boost to dodge the Level 2 lock, the card is fine after the lock but the lock still applies to all your summons
- Attack into 魔知青蛙 46239604 or 饼蛙 90809975 without accounting for the negate and steal, 饼蛙 can flip your monster face-down to its field

- **Playing Under 增殖的G and 欢聚友伴**

- Do not play the full line while 增殖的G 23434538 or 欢聚友伴·茸茸长尾山雀 42141493 is active, every deck or extra deck special summon gives the opponent a card
- Compromise line under G, 启辉器 15443125 into 蓝色喷流灵 76145933 and 喷流灵 13533678 then stop at 巨大喷流 54498517 with the searches in hand, keep special summons under four
- 墓穴的指名者 24224830 and 抹杀之指名者 65681983 answer G and Ash, 灵王的波动 40366667 covers summon effects, hold at least one answer before extending
- 迅捷鮟鱇 88686573 and 迅捷河狸 68353324 are the extra bodies that inflate the summon count, skip the 迅捷 engine portion when the opponent holds G
