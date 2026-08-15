---
name: rokket-experience
description: 弹丸 (Rokket) deck experience: mechanics, one-card combo, extenders, halt points
---
# 弹丸 (Rokket) Deck Experience

- **Deck Identity**

- DARK Dragon link-climbing deck: 弹丸 (Rokket) main monsters float from deck when destroyed and self-destruct for removal when targeted by Link monster effects; 枪管 (Borreload) Link bosses and the Synchro ace 装弹枪管狞猛龙 are the finishers
- Reference builds: 260124弹丸 (link-focused, 龙之灵庙 grave setup), 260320弹丸 (雨幕龙 + 欢聚友伴 flavor), 260320弹丸 sync variant (弹丸同调士 into 红莲魔 Synchros)
- Engine core: 速攻旋转 31443476, 旋转引导扇区 36668118, 弹丸曳光龙 68464358, 弹丸快装龙 25554552, 绝对路由龙 67748760, 主动撞针龙 73539069, 后膛枪管龙 90011273, 三重枪管旋转 89875646
- Main 弹丸 monsters: 银色弹丸龙 32476603, 马格努姆弹丸龙 26655293, 空尖弹丸龙 51548207, 麻醉弹丸龙 53266486, 自动手枪弹丸龙 80250185, 弹丸口径龙 67127799, 弹丸重填龙 05969957, 弹丸雨幕龙 53481938, 弹丸引爆龙 98937206
- Extra 枪管 ladder: 装弹枪管龙 31833038, 装弹枪管狞猛龙 27548199, 前托枪管龙 98630720, 套筒枪管龙 66452432, 装弹枪管解放龙 27096833, 刺刀枪管龙 85289965, 后膛枪管龙 90011273, 三枪管龙 03957130, 削短枪管龙 29296344, 德林加凶枪龙 23732205, 装弹枪管死焰龙 84464389, 装弹枪管狂怒龙 92892239
- 弹丸 setcode is 0x102, 枪管 is 0x10f, both verified from cards.cdb datas; 主动撞针龙, 绝对路由龙, 速攻旋转, 旋转引导扇区 belong to neither setcode but support the engine

- **Core Mechanic: Link-Target Self-Destruct + Float**

- Every standard 弹丸 main monster has two paired effects, verified in scripts like c32476603.lua (银色弹丸龙)
- ② float: when destroyed by battle or effect while on the field, at the End Phase of that turn special summon 1 弹丸 from deck (except itself), so any destruction of your own Rokkets is card advantage
- ① self-destruct: quick effect that fires when any Link monster's effect targets this face-up card (yours or the opponent's), destroys itself then applies a bonus: 银弹 banishes 1 from opponent extra deck, 马格努姆 sends 1 field monster to grave, 空尖 reveals up to 6 from opponent deck and banishes 1, 麻醉 negates a face-up monster's effects and stops it attacking, 自动手枪 sends 1 field spell/trap to grave
- 弹丸雨幕龙 53481938 has a special variant of ①: destroy itself then special summon up to 1 弹丸 from each of hand, deck, grave and banished
- 主动撞针龙 73539069 (Link-1, 1 Level-4-or-lower Dragon) runs the loop: on Link Summon it searches 旋转引导扇区 36668118; its ignition effect destroys 1 face-up monster you control and adds 1 弹丸 from grave to hand — the add only resolves if the destroy succeeded, so target Striker itself, never a Rokket
- 旋转引导扇区 36668118 ② once per turn: special summon up to 2 弹丸 from hand in defense (max 1 of each name), or if the opponent controls more monsters, special summon up to the difference from grave; it also gives +300 ATK/DEF to all 弹丸 including the opponent's
- 速攻旋转 31443476 (Quick-Play): special summon 1 弹丸 from deck; that monster cannot attack and is destroyed by effect at the End Phase — that destruction itself triggers the float ② for a free 弹丸 from deck

- **One-Card Combo: 速攻旋转 or 弹丸曳光龙**

- Starter: 速攻旋转 31443476 in hand with no other cards (or normal summon 弹丸曳光龙 68464358 alone; the lines are identical from step 2)
- Step 1: activate 速攻旋转, special summon 弹丸曳光龙 68464358 from deck (Level 4 Tuner)
- Step 2: link 曳光龙 into 主动撞针龙 73539069, Striker searches 旋转引导扇区 36668118
- Step 3: activate 旋转引导扇区, then activate Striker ② targeting Striker itself and 曳光龙 in grave, destroy Striker and add 曳光龙 to hand
- Step 4: activate 旋转引导扇区 ②, special summon 曳光龙 from hand in defense
- Step 5: activate 曳光龙 quick effect, destroy 旋转引导扇区 (any face-up card you control), special summon 银色弹丸龙 32476603 from deck, this locks you to DARK extra deck summons for the turn
- Step 6: Synchro 曳光龙 (Level 4 Tuner) + 银色弹丸龙 (Level 4) into 装弹枪管狞猛龙 27548199, equip Striker from grave as its gun barrel, gaining 1 枪管指示物 and +600 ATK (half of Striker's 1200)
- Line verified step by step against c31443476, c73539069, c36668118, c68464358, c27548199; the 枪管指示物 count equals the equipped Link's rating, so this one-card line ends on 1 counter only

- **End Field One-Card**

- 装弹枪管狞猛龙 27548199 at 3600 ATK with 1 枪管指示物, one negation of an opponent effect activation per counter (the negate only answers opponent effects and spends a counter)
- No backrow beyond the searches already used; the line is small but honest, 弹丸's real end boards need a second card
- Two-card end boards (second 弹丸 or a second starter): 狞猛龙 with 2-3 counters (equip a 后膛枪管龙 90011273 or 三枪管龙 03957130 instead of Striker) plus a Link-4 boss: 前托枪管龙 98630720 (quick negate an effect monster and revive a 弹丸 from grave, attacks all monsters, indestructible, untargetable) or 套筒枪管龙 66452432 (negate a face-up card, destroy your 弹丸 for its float, at battle phase start special summon a Link-4-or-lower 枪管 from extra deck such as 装弹枪管龙 31833038)
- 枪管重启 87607094 in hand (pay half LP, negate an opponent spell/trap activation and set it face-down) and 灵王的波动 40366667 back up the board

- **Extender: 弹丸快装龙 25554552**

- On Normal or Special Summon adds 1 Level 7 DARK Dragon from deck, then locks you to DARK extra deck summons for the turn
- Search targets: 亡龙之战栗-死欲龙 05560911 (pay half LP, target a Level 6-or-lower monster you control, special summon itself with level reduced by that monster's level) in the 260320 builds, 弹丸引爆龙 98937206 in the 260124 build
- 亡龙之战栗-死欲龙 05560911 is also the Synchro variant enabler: 弹丸同调士 48355999 normal summon revives a Level 5-or-higher DARK Dragon from grave (negated, destroyed at End Phase) for Level 8 红莲魔龙·右红痕 80666118 or 装弹枪管狞猛龙, up to Level 12 真红莲新星龙-燃烧之魂 65541655 and Level 9 琰魔龙 红莲魔·渊 09753964

- **Extender: 弹丸雨幕龙 53481938 and 绝对路由龙 67748760**

- 弹丸雨幕龙 ignition from hand: send 1 non-Level-5 DARK Dragon from deck to grave as cost, special summon itself, DARK lock for the turn
- The standard dump is 绝对路由龙 67748760, whose grave effect (any send, including costs) adds 1 弹丸 from deck to hand — 雨幕龙 is a one-card Absorouter search plus a body
- 绝对路由龙 also special summons itself from hand while a face-up 弹丸 is on field; the 260124 build dumps it with 龙之灵庙 41620959 and 愚蠢的埋葬 81439173 instead
- 弹丸引爆龙 98937206: special summon itself while a DARK Dragon Link is on field, ignition to special summon a DARK Dragon monster card from your spell/trap zone (negated, cannot attack) — turns equipped cards from 枪管上膛 06556178 or the 狞猛龙 equipped Link into bodies

- **Extender: 后膛枪管龙 90011273 and 三重枪管旋转 89875646**

- 后膛 (Link-2, 2 DARK Dragons including a 弹丸): on Link Summon adds a 枪管 spell/trap (枪管上膛 06556178, 枪管重启 87607094, 三重枪管旋转 89875646); quick effect gives +500 ATK to a DARK monster you control, and if the target left the field it special summons a 弹丸 from deck in defense instead
- 后膛 ② targeting your own 弹丸 is an engine trick: the 弹丸 can chain its ① self-destruct, then 后膛 summons a 弹丸 from deck
- 三重枪管旋转 mode 1: return 1 Dragon from grave to deck, special summon a different-name 弹丸 from deck; mode 2: return 2 Dragons, add a field spell from grave; mode 3: return 3 Dragons, shuffle up to 3 opponent grave cards back
- 三枪管龙 03957130 (Link-3): on Link Summon adds 速射扳机 67526112 or 双式扳机 38129297 or 重型扳机 20071842; its ignition destroys a face-up card you control to recycle a DARK Dragon from grave to hand
- 装弹枪管死焰龙 84464389 (fusion, DARK Link + DARK monster) searches a 弹丸 on fusion, equips a DARK Link from grave or banished for +500 ATK, and pops a card when used as Link material; 装弹枪管狂怒龙 92892239 (2 DARK Dragons) quick-destroys one of your monsters and one opponent card, and banishes itself from grave to revive a DARK Link

- **Extender: 德林加凶枪龙 23732205 and 削短枪管龙 29296344**

- 德林加 (Link-2, 2 DARK Dragons): each time a face-up 弹丸 you control is special summoned it revives itself from grave (banished when it leaves the field); at the opponent's End Phase it destroys an attack-position monster that did not attack and burns its ATK
- 削短 (Link-2, 2 Dragons including a 弹丸): discard 1, destroy 1 face-up monster; if it was a Link monster, special summon up to its Link rating 弹丸 from hand and grave; after resolution you cannot special summon Link-2-or-lower from the extra deck for the rest of the turn
- 弹丸重填龙 05969957: from hand or field, when a face-up DARK monster you control that was summoned from the extra deck is destroyed, send this to grave and special summon a different-name DARK monster from grave — hand-trap protection for your Borreload bosses

- **Halt Points**

- 灰流丽 14558127 on 速攻旋转 or on 曳光龙's deck special summon kills the one-card line; 墓穴的指名者 24224830 and 抹杀之指名者 65681983 answer it
- 增殖的G 23434538 and 欢聚友伴·茸茸长尾山雀 42141493 punish the roughly five special summons of the line; under them stop after Striker plus the 旋转引导扇区 search and pass, or end on 狞猛龙 alone
- 效果遮蒙者 97268402 and 无限泡影 10045474 on 曳光龙 stop the deck special summon; 屋敷童 73642296 hits the 绝对路由龙 grave search
- 灵王的波动 40366667 (activatable from hand while the opponent controls a card, negates an effect that would special summon and destroys it if a trap is in your grave) and 枪管重启 87607094 answer enemy starters, but 灵王的波动 from hand locks your LIGHT/EARTH/WIND monster effects for the whole duel
- Effects that declare Synchro, such as 次元障壁 83326048, kill the 狞猛龙 line; the deck has no meaningful backup without its extra deck summons

- **Mirror Match: 弹丸 vs 弹丸**

- Every 弹丸 ① fires when any Link monster's effect targets it, so never target the opponent's 弹丸 with your Striker, 削短, 后膛 or 套筒 effects — their ① chains for free value (银弹 banishes your extra deck boss, 马格努姆 sends a field monster to grave)
- Expect the same in reverse: your 弹丸 can chain ① to the opponent's Link targeting, so bait with 后膛 ② or force the targeting on a card you want destroyed
- 银色弹丸龙 32476603 self-destruct is the strongest mirror weapon: strip 前托枪管龙, 套筒枪管龙 and 狞猛龙 from their extra deck before they link into them
- 削短 destroying an opponent's Link special summons up to its rating in 弹丸 from hand and grave; 德林加's End Phase burn punishes monsters that did not attack
- 旋转引导扇区 36668118's +300 applies to both players' 弹丸; 枪管重启 87607094 negates their 速攻旋转 31443476 and 旋转引导扇区 activations
- Whoever resolves 速攻旋转 plus 曳光龙 into 狞猛龙 first usually wins the grind; keep 墓穴的指名者 for their 绝对路由龙 search

- **Common Mistakes**

- 弹丸曳光龙 68464358 and 弹丸口径龙 67127799 are both Tuners, so Tracer plus Caliber cannot Synchro; the non-Tuner for the Level 8 must be 银色弹丸龙, 马格努姆弹丸龙 or 弹丸快装龙
- Striker ② targeting a 弹丸 makes that 弹丸 chain its ① self-destruct, Striker's destroy then fails and the add-to-hand does not resolve; target Striker itself or a non-Rokket
- Do not treat 速攻旋转's End Phase destruction as a loss — the destroyed 弹丸 floats into another 弹丸 from deck at the same End Phase
- 削短枪管龙's Link-2-or-lower lock applies even when nothing was destroyed, so make 后膛 or other Link-2s first and save 削短 for last
- Respect the DARK-only extra deck locks of 曳光龙, 快装龙, 雨幕龙, 引爆龙 and 同调士 — no S：P小夜骑士 29301450 or 灾厄之星 提·丰 93039339 plays after those effects resolve
- 装弹枪管狞猛龙's negate only answers opponent activations and spends a 枪管指示物, so the one-card line's single counter must be saved for a real threat
- 套筒枪管龙 ②: chain the targeted 弹丸's ① self-destruct before resolution for double value, the 弹丸 still floats at the End Phase
- 枪管上膛 06556178 banishes the equipped monster when the equip card leaves the field, so do not destroy your own equip casually
- 装弹枪管死焰龙's pop triggers only when used as Link material; 装弹枪管狂怒龙's grave revival summons a DARK Link whose effects are negated for that turn
- 装弹枪管解放龙 27096833 revives from grave by destroying one of your own monsters, once per chain — do not forget the sacrifice
