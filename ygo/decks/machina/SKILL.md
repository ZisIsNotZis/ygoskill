---
name: machina-experience
description: 机甲 (Machina) deck experience: mechanics, one-card combo, extenders, halt points
---
# 机甲 (Machina) Deck Experience

- **Deck Identity**

- 机甲 (Machina) is an EARTH Machine mid-range grind deck built around the 机甲要塞 recursion loop, every card below verified as setcode 0x36
- Core main deck: 机甲要塞 5556499, 机甲机械骨架 42940404, 机甲未分类备用兵 45674286, 机甲部队·超大变形 51617185, 机甲放射兵 50863093, 机甲空袭兵 23469398, 机甲破坏预备兵 54563536, 机甲魔化仓库兵 85136114, 机甲上校 87074380, 机甲部队·毁灭武装力量 46033517, 机甲部队的再编制 86852702, 机甲部队的超临界 59741415, 机甲部队的防卫圈 13247801
- No in-archetype Fusion or Xyz exists, the deck summons generic Machines instead: 齿轮齿巨人 X 28912357 and 重装甲列车 铁狼 49121795 from Level 4s, 宵星之机神 丁吉尔苏 93854893 from Level 8s, 天霆号 阿宙斯 90448279 stacked on any Xyz after it battles
- The only fusion-style boss is 机甲部队·武装力量 58054262, summonable solely by 督战官 科文顿 22666164, it pays 1000 LP per attack and trades itself for 机甲士兵 60999392, 机甲狙击兵 23782705 and 机甲卫兵 96384007, not played in current lists
- 机甲大炮 39284521 special summons itself by sending any number of other Machines from hand to grave, gaining 800 attack per card sent, it fuels grave setup and is a Level 8 body for 丁吉尔苏
- Repo builds splash train packages: 紧急行车时间表 25274141, 弹丸特急 子弹快车 52481437, 超重型炮塔列车 古斯塔夫最大炮 56910167, 超重型炮塔列车 破天巨爱 26096328 and 兽带斗神“王者”轩辕十四 10604644 for Level 8 bodies, treat the Machina engine as the identity and the trains as the finisher

- **Core Mechanic: 机甲要塞 recursion**

- 机甲要塞 5556499 special summons itself from hand or grave by sending Machine monsters from hand to grave as cost whose levels total at least 8, the summoned Fortress itself may join the discard pile, so Fortress plus one Machine makes Fortress from hand and Fortress in grave revives by pitching one Level 8 such as 机甲放射兵 50863093
- While face up, when the opponent activates an effect targeting Fortress, reveal their hand and discard one chosen card, a mandatory chain-solve discard that punishes targeted removal
- When Fortress is destroyed by battle it destroys one opponent card, mandatory and targeting
- 机甲部队·超大变形 51617185 closes the loop: when Fortress is sent from your field to your grave, banish that Fortress as cost and special summon Megaform from grave, then Megaform tributes itself to special summon any other 机甲 monster from hand or deck, every Fortress death cycles into a fresh Machina
- Megaform's two effects share one count limit, only one total use per turn

- **One-Card Combo: 机甲机械骨架**

- Starter: 机甲机械骨架 42940404 in hand, normal summon it, nothing else needed
- Step 1: its search triggers only on normal summon, add 机甲未分类备用兵 45674286 from deck
- Step 2: 45674286 special summons itself because it was added to hand by an effect and not drawn, afterwards you can only special summon Machine monsters until end of turn
- Step 3: 45674286 sends 机甲部队·超大变形 51617185 or 机甲要塞 5556499 from deck to grave
- Step 4: overlay the two Level 4s into 齿轮齿巨人 X 28912357, detach one material to add any Level 4 or lower Machine from deck or grave, typically 机甲破坏预备兵 54563536 or 机甲魔化仓库兵 85136114
- End result: 齿轮齿巨人 X 28912357 with one material plus Megaform or Fortress in grave ready for the recursion loop, the Machine lock expires at end of turn

- **End Field**

- Grind board: 机甲要塞 5556499 plus 齿轮齿巨人 X 28912357, set 机甲部队的防卫圈 13247801 or 机甲部队的超临界 59741415, 机甲部队·毁灭武装力量 46033517 waiting in grave
- 机甲部队·毁灭武装力量 46033517 is the boss: it special summons itself from grave by banishing Machines from your grave with total levels at least 12, during the battle phase pays half your LP to negate an opponent effect and halve their LP, and when destroyed summons up to three 机甲 monsters from banished with total levels at most 12
- Rank 8 route: overlay 机甲空袭兵 23469398, 机甲放射兵 50863093, 机甲部队·超大变形 51617185 or 兽带斗神“王者”轩辕十四 10604644 into 宵星之机神 丁吉尔苏 93854893, its summon effect sends one opponent card to the grave without targeting and it replaces destruction by detaching material
- Rank 4 route: 重装甲列车 铁狼 49121795 detaches to make one Machine attack directly, or 齿轮齿巨人 X 28912357 keeps searching
- After any Xyz monster battles, stack 天霆号 阿宙斯 90448279 on top and detach two materials to send the rest of the field to the grave

- **Extenders**

- 机甲部队的再编制 86852702 is the searcher: discard any one card to add two 机甲 monsters, or discard one 机甲 card to add two 机甲 cards, at most one copy of each name, once per turn by oath
- 机甲未分类备用兵 45674286 self-special summons whenever added to hand by any non-draw effect and then mills one 机甲 monster from deck, the Machine lock makes it the glue between searches and grave setup
- 机甲放射兵 50863093 discards another 机甲 from hand to special summon itself, then destroys a Machine you control to special summon a different-named 机甲 from grave whose level does not exceed the destroyed monster
- 机甲空袭兵 23469398 discards another 机甲 to special summon itself, and during the opponent turn destroys a Machine you control to special summon a different-named 机甲 from deck, targeting itself with its own Level 8 can deck out a 机甲要塞 5556499
- 机甲魔化仓库兵 85136114 on summon special summons a 机甲 from grave in defense with its effects negated that turn, then bounces one own 机甲 monster and one opponent spell or trap to hand
- 机甲破坏预备兵 54563536 sends itself from hand or field to grave to give a 机甲 monster plus 1200 attack as a quick effect even during the damage step, and returns itself to hand after any own 机甲 battle destruction
- 机甲部队的超临界 59741415 is a trap: destroy a Machine you control to special summon a different-named 机甲 from hand or deck, and from grave banishes itself to shuffle three Machines from grave or banished into the deck and draw one

- **Halt Points**

- Ash Blossom on 机甲机械骨架 42940404 search stops the one-card line at a single 1800 attacker
- 机甲部队的再编制 86852702 denies two cards if interrupted, it is the preferred hand trap target over a single search
- Negating 机甲未分类备用兵 45674286 loses the grave setup and the board leaves nothing but 齿轮齿巨人 X 28912357
- 机甲部队·毁灭武装力量 46033517 needs twelve levels of Machines in grave, emptying the grave stops both its summon and its death revival
- 机甲空袭兵 23469398 and 机甲放射兵 50863093 destroy their own Machine as part of resolution, negating the special summon leaves you down a monster with no replacement

- **Mirror Match: 机甲 vs 机甲**

- Both sides run the same recursion, the first player to resolve 机甲部队·毁灭武装力量 46033517 and halve the opponent's LP usually wins
- 机甲空袭兵 23469398 on the opponent's turn flips the board: destroy your own Level 8 to summon a 机甲要塞 5556499 from deck
- Bounce beats destroy: 机甲魔化仓库兵 85136114 returns an opposing Fortress to hand, dodging its battle-destroy pop and resetting its field presence
- Hold 机甲破坏预备兵 54563536 for battle, pumping Fortress past 3700 attack breaks the mirror's 2500 wall
- 嵌合要塞龙 79229522 with 电子龙 70095154 eats the opponent's Machines from their field as fusion material, the ultimate mirror removal
- Keep a Fortress in hand to rebuild after the opponent's 天霆号 阿宙斯 90448279 board wipe

- **Common Mistakes**

- 机甲机械骨架 42940404 searches only on normal summon, never on special summon
- After 机甲未分类备用兵 45674286 special summons itself you may only special summon Machine monsters until end of turn, sequence every non-Machine play before it
- 机甲金属抓手兵 69838761 summons without tribute only while you control no face-up cards at all, face-up spells, traps and monsters all block it, and it becomes 1800 attack instead of 2800 while the added card is random from three revealed, so it can whiff
- 机甲部队的超临界 59741415 is a trap that must be set a turn in advance, it cannot be activated from hand
- 机甲魔化仓库兵 85136114 revival negates the revived monster's effects, do not expect its summon trigger
- 机甲上校 87074380 destroys its own target too, its wipe removes one of your Machines alongside every opponent monster with attack at most the target's
- 机甲部队·毁灭武装力量 46033517 summons from grave only, its death revival needs the banished Machines so plan the banish targets
- 机甲部队的再编制 86852702 allows at most one copy per turn by oath and at most one copy of each name per add
- 齿轮齿巨人 X 28912357 searches only Level 4 or lower Machines, it cannot grab 机甲要塞 5556499
- 弹丸特急 子弹快车 52481437 sends two of your own cards to grave at attack declaration, only attack when the trade is worth it
- 机甲部队的防卫圈 13247801 protects only Level 6 and lower Machines, Fortress and the Level 8s stay vulnerable
