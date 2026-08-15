---
name: icebarrier-experience
description: 冰结界 (Ice Barrier) deck experience: WATER-lock synchro engine, Trishula-line bosses, one-card combo, extenders, halt points
---
# 冰结界 (Ice Barrier) Deck Experience

- **Deck Identity**

- WATER Aqua/Spellcaster/Warrior Synchro midrange: ladder into 冰结界之龙 三叉龙 52687916 and 冰结界的还零龙 三叉龙 70980824, back it with battle-phase and spell floodgates
- Archetype setcode is 0x2f in cards.cdb; every main monster is WATER, races split across Aqua tuners, Spellcaster searchers, Warrior 虎将 bodies, and Dragon/Sea Serpent/Wyrm synchros
- Reference near-pure list: deck/210717冰结界/bd206c889478c637.ydk (40 of 54 cards are 冰结界); current hybrids deck/241221冰结界 and deck/260124冰结界 add the generic WATER synchro toolbox (魔救之奇迹-巨龙晶石 9464441, 白斗气白鲸 5614808, 相剑大公-承影 96633955)
- Searchers: 冰结界的纹章 84206435 adds any 冰结界 monster, 冰结界的虎将 韦恩 81825063 self-summons then adds any 冰结界 spell or trap, 抵达冰结界的晴岚 17197110 tributes 冰结界 to summon 4-or-lower 冰结界 from deck
- Battle-phase floodgate: 冰结界 34293667 drops the attacking monster to 0 ATK and negates it; its grave effect mills a 5-or-higher WATER and recycles a WATER monster at the cost of a WATER special-summon lock
- 冰结界之镜 10691144 is a Quick-Play anti-banish mirror, not a field spell; the task-guessed 冰结界之龙 三戟龙 and 冰结界等重 do not exist in this DB
- Rebalance quirk: Xyz and Link monsters are reworked into main-deck Level/Pendulum bodies, for example 龙神鲨 440556, 饼蛙 90809975, 天霆号 阿宙斯 90448279, 海晶少女 奶嘴海葵 79130389, so the extra-deck lock rules apply only to Synchro

- **Core Mechanic: WATER Lock into Trishula**

- 冰结界的照魔师 18319762 discards 1 card to special summon any 冰结界 tuner from deck, then locks you to WATER special summons for the turn; its grave self allows discarding 冰结界 costs by banishing a grave copy of itself instead
- 冰结界的镜魔师 9396662 tributes another effect monster to summon up to 3 冰结界衍生物 9396663 and raises its own level by that many, then locks the extra deck to WATER Synchro only; when sent to grave it adds any 冰结界 card from deck or banishment
- 冰结界的霜精 70703416 mills a 3-or-lower 冰结界 from deck and copies its level until end of turn, the level-fixing tuner that makes Trishula math work
- 冰结界的依巫 44308317 special summons itself free while any 冰结界 is on field; its grave effect makes a 冰结界衍生物 44308318
- 冰结界的传道师 50088247 self-summons from hand while a 冰结界 is on field but then forbids 5-or-higher special summons that turn, so revive it via 晴岚 or its own tribute effect instead of the self-summon before the big play
- 冰结界的虎将 神兵 9056100 grants an extra normal summon of a 冰结界 monster; 冰结界的虎将 健陀罗 53921056 revives one 冰结界 from grave each end phase

- **One-Card Combo: 冰结界的纹章 84206435**

- Starter: 冰结界的纹章 84206435 in hand, nothing else required
- Step 1: activate 纹章 to add 冰结界的照魔师 18319762
- Step 2: normal summon 照魔师, discard 1 card to special summon 冰结界的镜魔师 9396662 from deck, now WATER-locked for the turn
- Step 3: 镜魔师 tributes 照魔师, summons 3 冰结界衍生物 9396663, and becomes level 5, extra deck now WATER-Synchro-locked
- Step 4: synchro 镜魔师 (level 5 tuner) with 2 tokens (level 1 each) into 深海姫首席女歌手 50793215 (level 7 Synchro Tuner, WATER)
- Step 5: 深海姫 returns 1 banished opponent card to hand and special summons 冰结界的依巫 44308317 (level 4) from deck
- Step 6: 镜魔师 in grave adds 抵达冰结界的晴岚 17197110 or 冰结界的三方阵 64990807 from deck or banishment
- End field one-card: 深海姫 50793215, 依巫 44308317, 1 token, plus the searched spell in hand

- **End Field**

- Full two-card setup (晴岚 17197110 in hand): after 镜魔师 9396662 reaches level 5 with tokens, activate 晴岚 to tribute 2 tokens and summon 冰结界的传道师 50088247 and 冰结界的依巫 44308317 from deck, then 镜魔师 (5) + 传道师 (2) + 依巫 (4) equals 冰结界的还零龙 三叉龙 70980824, banishing up to 3 opponent cards on summon
- 还零龙 floats when destroyed by the opponent: revives 冰结界之龙 三叉龙 52687916 with 3300 ATK and halves and negates their monsters
- Alternative level 9: 霜精 70703416 copies 冰结界的守护阵 82498947 (level 3), plus 依巫 44308317 (4) plus 冰偶 97476032 (2) makes 冰结界之龙 三叉龙 52687916, banishing 1 card each from opponent hand, field, and grave
- Backrow anchors: 抵达冰结界的晶域 35380371 stops the opponent chaining to your 冰结界 effects and bounces a 冰结界 while tucking a card to deck bottom; 冰结界的晶壁 43582229 revives a 4-or-lower 冰结界 and, with 3 monsters out, makes your 冰结界 immune to effects of extra-deck-summoned monsters
- Removal synchros: 冰结界之龙 光枪龙 50321796 bounces by discarding (grave 照魔师 18319762 can pay), 冰结界之龙 天枪龙 65749035 destroys up to 2, 冰结界的虎王 雪虎 70583986 bounces your own cards for +500 ATK each
- Toolbox in hybrids: 魔救之奇迹-巨龙晶石 9464441 negates and destroys a spell or trap, 白斗气白鲸 5614808 destroys all opponent attack-position monsters on summon, 冰灵山的龙祖 矛枪龙 96402918 summons a 冰结界 from deck when the opponent summons from extra

- **Extenders**

- 抵达冰结界的晴岚 17197110: tribute 1 or 2 冰结界 to summon the same count of 4-or-lower 冰结界 with different names from deck, then in grave banishes itself to add back a 冰结界 monster; the main multi-body extender
- 冰结界的三方阵 64990807: reveal 3 different-named 冰结界 in hand, destroy 1 opponent card and special summon a 冰结界 from hand
- 冰结界的虎将 韦恩 81825063: special summons itself while the opponent has a monster and you have a 冰结界, then searches any 冰结界 spell or trap, and banishes the opponent's spells and traps sent from field
- 冰结界的依巫 44308317: free self-summon plus a grave token to feed 镜魔师 9396662 or synchro fodder
- 冰结界的随身 43256007: tributes itself to drop a 5-or-higher 冰结界 from hand, then revives itself from grave by lowering a 3-or-higher WATER monster by 2 levels for laddering
- 冰结界的传道师 50088247: tribute it to revive any 冰结界 from grave, a second body after the 晴岚 summon
- 冰结界的军师 50032342: discard 1 冰结界 to draw 1, cheap grave and hand setup
- 冰结界的净玻璃 53535814: returns up to 2 of your grave 冰结界 and up to 2 opponent grave cards to the decks, and banishes itself to force a monster to defense
- Generic WATER extenders seen in builds: 鬼青蛙 9126351, 冰水帝 霓石精·海女神 18494511, 寂静鮟鱇 90303176, 次世代水精灵 4904812, 冰偶镜 65569724 with 冰偶 97476032

- **Halt Points**

- 灰流丽 14558127 negates 冰结界的纹章 84206435 search, 照魔师 18319762 deck summon, 晴岚 17197110 deck summon, and 深海姫首席女歌手 50793215 deck summon, which stops the line at one body
- 无限泡影 10045474 on 照魔师 18319762 or 镜魔师 9396662 kills the token line, on 还零龙 70980824 or 三叉龙 52687916 kills the banish
- 增殖的G 23434538: the full combo is 4 to 6 special summons, so stop early at 深海姫 50793215 or 魔救之奇迹-巨龙晶石 9464441 and keep a token to tribute
- 屋敷童 73642296 negates 镜魔师 9396662 grave search, 晴岚 17197110 grave add, and 冰结界 34293667 grave mill; 小丑与锁鸟 94145021 stops 纹章 84206435 and 晴岚 searches
- 原始生命态 尼比鲁 27204311 drops on the fifth summon, so pace the ladder if no 墓穴的指名者 24224830 is available
- 墓穴的指名者 24224830 and 抹杀之指名者 65681983 answer hand traps and also strip the opponent's grave 照魔师 18319762 discard substitute in the mirror

- **Mirror Match: 冰结界 vs 冰结界**

- Both players WATER-lock after 照魔师 18319762 and 镜魔师 9396662, so the duel is won by whoever resolves 冰结界的还零龙 三叉龙 70980824 or 冰结界之龙 三叉龙 52687916 first and banishes the opponent's engine pieces
- 冰结界的虎将 莱蓬 81275309 is the mirror-breaker: the opponent's on-field monster effects need a discard or are negated, taxing their 照魔师 and 镜魔师 plays
- 冰结界的净玻璃 53535814 returns their grave 照魔师 18319762 and 镜魔师 9396662 to deck, removing the discard substitute and the recursion before they can ladder
- 冰结界的虎将 韦恩 81825063 banishes the opponent's spells and traps sent from field, which kills their grave 冰结界 34293667 and 晴岚 17197110 plays
- 冰结界之镜 10691144 answers the opponent's 三叉龙 52687916 banish by removing matching cards from their hand, field, and grave in kind
- 冰结界的守护阵 82498947 and 冰结界的术者 23950192 shut down attacks while a second 冰结界 is out, and 冰结界的封魔团 73061465 locks their spells with one discard

- **Common Mistakes**

- Do not normal summon before activating 照魔师 18319762 when 冰结界的纹章 84206435 starts, the line needs the normal summon for 照魔师
- Never self-summon 冰结界的传道师 50088247 before the big synchro, its 5-or-higher special-summon lock forbids 还零龙 70980824 and 三叉龙 52687916; bring it out through 晴岚 17197110 instead
- The 照魔师 18319762 and 镜魔师 9396662 locks are WATER-only, so non-WATER extra monsters like 鲜花女男爵 84815190 or 装弹枪管狞猛龙 27548199 must come out before the engine or not at all
- 抵达冰结界的晶域 35380371 destroys itself at end phase unless you reveal 3 different 冰结界 extra-deck monsters, so keep 三叉龙 52687916, 还零龙 70980824, 天枪龙 65749035, and 光枪龙 50321796 in the extra deck
- 冰结界 34293667 grave effect locks you to WATER until the end of your next turn, so do not plan a non-WATER monster after milling with it
- 霜精 70703416 copies the milled monster level only until end of turn, choose 冰结界的守护阵 82498947 (level 3) for 三叉龙 math instead of 传道师 50088247 (level 2) when the sum must be exactly 9
- 冰结界的三方阵 64990807 needs 3 different-named 冰结界 in hand, confirm the names differ before revealing with 照魔师 18319762 and 镜魔师 9396662 in hand
- 纹章 84206435 is a one-shot search, so grab the missing piece: 照魔师 18319762 for the full line, 镜魔师 9396662 when 照魔师 is already held, 霜精 70703416 for the Trishula route
- 冰结界的依巫 44308317 grave token and 冰结界的镜魔师 9396662 tokens are both named 冰结界衍生物 with setcode 0x2f (codes 44308318 and 9396663), so 晴岚 17197110 can tribute them, but do not over-sacrifice bodies needed as synchro material
