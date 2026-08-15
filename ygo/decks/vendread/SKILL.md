---
name: vendread-experience
description: 复仇死者 (Vendread) deck experience: ritual-zombie engine, ritual-lock, one-card engine, combo lines, extenders, halt points
---
# 复仇死者 (Vendread) Deck Experience

- **Deck Identity**

- DARK Zombie ritual deck; archetype tag 复仇死者 (setcode 0x106); every monster is DARK Zombie and every ritual spell summons 复仇死者 ritual monsters from hand or GY
- Main-deck monsters: 噬腐复仇死者 1855886 (LV6, the engine), 复仇死者·归来者 31772684 (LV4), 复仇死者·斯特里克斯 49477180 (LV2), 复仇死者·地狱犬 67267333 (LV3), 复仇死者·阿尼玛 70491682 (LV1), 复仇死者之核 49394035 (LV1)
- Ritual monsters: 归魂复仇死者·屠魔侠 4388680 (LV6 2400), 复仇死者·混骸鬼 3909436 (LV7 2700), 归魂复仇死者·诛邪侠 34093683 (LV8 3000), 复仇死者·噬腐鬼 29348048 (LV8 2800), 复仇死者·奇美拉 13482075 (LV5 2300)
- Ritual spells: 归魂复仇死者的爆诞 7986397, 归魂复仇死者的诞生 94666032, 极饿复仇死者 13386407
- Spells and traps: 复仇死者之夜 76871889 (field), 复仇死者的突击 76798740 (quick-play), 复仇死者的黑夜梦魇 33971095 (continuous), 复仇死者的移魂再诞 2287848, 复仇死者的续魂再结 2266498, 复仇死者的还魂再生 30650147, 复仇死者的白昼黎明 60375194 (traps)
- Link monster: 降灵复仇死者·救世侠 91420202 (2 Zombies, 1600, name treated as 屠魔侠)
- Reference build (deck/220423复仇死者): 屠魔侠 4388680 x3, 爆诞 7986397 x3, 诞生 94666032 x3, 仪式的事前准备 13048472 x3, 极饿复仇死者 13386407 x2, full main-deck Vendread set, Zombie engine 齐唱僵尸 49959355 x3, 马头鬼 92826944 x2, 不死世界 4064256, 尸界的班西 66570171, 吸血鬼吸食者 37129797, extra 救世侠 91420202 x2, 冰结界之龙 三叉龙 52687916, 召命之神弓-阿波罗萨 4280258, 卫星闪灵·淘气精灵 27381364
- 2025-support builds (deck/251220复仇死者, deck/260228活死人的呼声复仇死者) add 大尸教 21960890 x3, 灵道士 僵尸 76352503, 破灭与终焉之支配者 3739500, and the 秘仪之力21-世界 23846921 + 光之结界 73206827 skip-turn lock fetched by 电子化天使-弁天- 77235086

- **Core Mechanic: Ritual-Zombie Engine**

- 归魂复仇死者的爆诞 7986397: ritual summon with levels EXACTLY equal, tributing hand/field monsters or replacing one tribute by sending 1 复仇死者 monster from deck to GY; the summoned monster is destroyed at the end of the NEXT turn
- 归魂复仇死者的诞生 94666032: ritual summon with levels GREATER-or-equal, tributing hand/field monsters or banishing Zombies from GY as substitutes; its GY effect replaces the destruction of 屠魔侠 4388680
- 极饿复仇死者 13386407: special summon 1 复仇死者 monster (never 噬腐鬼 29348048) face-down from hand/deck/GY, then ritual summon using field monsters including it with levels greater-or-equal
- 爆诞's deck-send puts 噬腐复仇死者 1855886 or 斯特里克斯 49477180 into the GY mid-ritual so their GY triggers resolve in the same chain
- Ritual-summoned 屠魔侠 4388680 and 混骸鬼 3909436, when sent from the field to the GY, search (a ritual spell / a ritual monster) and dump a 复仇死者 monster from deck — this is the recursion loop
- Tributing 之核 49394035, 归来者 31772684, 地狱犬 67267333, 斯特里克斯 49477180 or 阿尼玛 70491682 FROM THE FIELD as ritual material grants the ritual monster a bonus effect: untargetable, quick-banish a special-summoned monster, quick-banish a spell/trap, draw-1 after battle, banish-on-battle-destroy
- 噬腐复仇死者 1855886 is the engine card: ① sent to GY by any means → add 1 复仇死者 spell/trap from deck; ② while in GY, when a monster on the field is released → banish 1 Zombie from GY → special summon itself, but while that copy is face-up only 复仇死者 monsters can be special summoned (the ritual-lock)
- 诛邪侠 34093683 and 救世侠 91420202 treat their name as 屠魔侠 4388680, which satisfies 噬腐鬼 29348048's GY revival condition and name-based plays
- Trap recursion: 移魂再诞 2287848 discards to revive a 复仇死者 monster and recover a ritual spell; 续魂再结 2266498 reveals a ritual monster in hand, special summons banished 复仇死者 monsters face-down with levels summing exactly, releases them, then ritual summons from hand; 移魂再诞's GY effect shuffles exactly 5 banished Zombies into the deck to draw 1

- **One-Card Combo: 噬腐复仇死者**

- 噬腐复仇死者 1855886 is the one-card engine: any send-to-GY (突击 76798740 cost, 齐唱僵尸 49959355 ② dump, 灵道士 僵尸 76352503 ①, 救世侠 91420202 ③, 爆诞 7986397 deck-send) triggers ① to search any 复仇死者 spell/trap
- Standard line with 噬腐复仇死者 1855886 + 归魂复仇死者的爆诞 7986397 + 屠魔侠 4388680 in hand: 爆诞 tributes 噬腐复仇死者 from hand (LV6 = exact level) and ritual summons 屠魔侠
- 噬腐复仇死者 ① then adds 复仇死者的突击 76798740 or 复仇死者的移魂再诞 2287848 from deck
- End of next turn 爆诞 destroys 屠魔侠 → ② adds 诞生 94666032 and dumps 斯特里克斯 49477180 from deck → 斯特里克斯 ① reveals a 复仇死者 card and special summons itself
- Next turn 诞生 94666032 ritual summons 屠魔侠 4388680 back from the GY by banishing Zombie substitutes
- One-card ritual line: 极饿复仇死者 13386407 alone special summons 之核 49394035 or 噬腐复仇死者 1855886 face-down from deck, then rituals from hand/GY with levels greater-or-equal; tributing the face-down 之核 grants untargetable, tributing 噬腐复仇死者 triggers its ① search
- 仪式的事前准备 13048472 alone fetches 诞生 94666032 + 屠魔侠 4388680, two pieces that still need Zombie levels in GY or on field to resolve

- **End Field**

- Typical turn one: 混骸鬼 3909436 (declare Trap or Monster) or 屠魔侠 4388680 holding granted effects (untargetable from 之核 49394035, quick-banish from 归来者 31772684 or 地狱犬 67267333) plus 复仇死者之夜 76871889, 1-2 set 复仇死者 traps (移魂再诞 2287848 / 还魂再生 30650147 / 白昼黎明 60375194), 噬腐复仇死者 1855886 in GY, and 马头鬼 92826944 or 救世侠 91420202 on board
- 复仇死者之夜 76871889 ② lets any 复仇死者 monster that destroys by battle chain a second attack (banish 1 复仇死者 monster from GY, no direct attacks)
- Boss swing: 诛邪侠 34093683 (3000 ATK, your other cards untargetable while ritual-summoned) plus 噬腐鬼 29348048 (release 1 Zombie in a main phase → gains its original ATK; revives from GY while 屠魔侠 name is present)
- 复仇死者·奇美拉 13482075 is the defensive ritual: banishes 1 Zombie from GY to negate and destroy a destruction effect, and drops opponent monsters by 500 ATK/DEF when released or banished for a ritual

- **Extenders**

- 复仇死者的突击 76798740 (quick-play): send 1 Zombie from hand or face-up field to GY → special summon any 复仇死者 monster from deck, even a ritual monster like 屠魔侠 4388680 as a plain body
- 复仇死者之夜 76871889 ①: discard 1 card → add any 复仇死者 monster from deck, including a ritual monster
- 复仇死者·斯特里克斯 49477180: sent to GY → reveal 1 复仇死者 card in hand → special summon itself
- 复仇死者之核 49394035: banish 1 Zombie from GY → special summon itself; LV1 ritual fodder
- 复仇死者·地狱犬 67267333: discard 1 复仇死者 card → special summon from GY; 0/2100 wall
- 复仇死者·阿尼玛 70491682: banish itself from GY → special summon 1 banished 复仇死者 monster, then only Zombies may be special summoned this turn
- 复仇死者·归来者 31772684: special summons itself when destroyed by the opponent
- 马头鬼 92826944: banish itself from GY → special summon 1 Zombie from GY (non-复仇死者, mind the locks)
- 齐唱僵尸 49959355: ① discard a card → +1 level on a face-up monster; ② send 1 Zombie from deck to GY → +1 level (the dump feeds 噬腐复仇死者 1855886)
- 降灵复仇死者·救世侠 91420202: ② add 1 复仇死者 card from GY to hand; ③ at damage calculation send 1 Zombie from deck to GY → opponent monster loses level x 200 ATK (send 噬腐复仇死者 for the search)
- 大尸教 21960890 (2025 builds): on summon → send 1 Fiend/Zombie ritual monster from deck to GY, then add 1 ritual spell from deck; ② special summons a banished LV4-or-lower Fiend/Zombie
- 复仇死者的移魂再诞 2287848 (trap): discard 1 card → special summon 1 复仇死者 monster from GY in defense + add 1 ritual spell from GY to hand
- 复仇死者的续魂再结 2266498 (trap): reveal a 复仇死者 ritual monster in hand → special summon banished 复仇死者 monsters face-down (levels exactly equal, one of each name) → release them → ritual summon from hand
- 复仇死者的黑夜梦魇 33971095 (continuous): release any number of 复仇死者 monsters → target gains that many levels; +1000 ATK to a ritual monster after it destroys by battle
- 不死世界 4064256 makes all monsters Zombie, so 噬腐鬼 29348048 can release anything and 突击 76798740 can send anything; 尸界的班西 66570171 protects and searches it

- **Halt Points**

- 灰流丽 14558127 on 噬腐复仇死者 1855886 ①, 复仇死者之夜 76871889 ①, or 仪式的事前准备 13048472 stops the search line
- 墓穴的指名者 24224830 on 噬腐复仇死者 in the GY cuts the recurring body, the ① search, and 爆诞 7986397's deck-send value
- 增殖的G 23434538: the deck specials 5+ times (噬腐复仇死者, 斯特里克斯, 之核, ritual monster, 马头鬼) — under G play 突击 76798740 for one summon or a single 诞生 94666032 ritual and pass
- 次元吸引者 91800273 and GY hate hurt the engine, but 续魂再结 2266498, 阿尼玛 70491682 and 移魂再诞 2287848 ② make the deck banish-resilient
- 原始生命态 尼比鲁 27204311 arrives after 5 summons — the ritual line plus 斯特里克斯 49477180 self-special often crosses it; keep the summon count at 4 unless 诛邪侠 34093683 or a set trap answers it
- Negating 爆诞 7986397, 诞生 94666032 or 事前准备 13048472 stops the ritual; the normal-summon starters 齐唱僵尸 49959355 fold to 无限泡影 10045474 and 幽鬼兔 59438930
- The locks: with 噬腐复仇死者 1855886 face-up via ②, or with the 还魂再生 30650147 token out, every normal and special summon must be 复仇死者 — 马头鬼 92826944, 齐唱僵尸 49959355, 吸血鬼吸食者 37129797 and generic links are unusable until the lock piece leaves the field

- **Mirror Match**

- 还魂再生 30650147 is the best mirror answer: it releases the opponent's face-up ritual monster (their boss) and replaces it with a 0-ATK token on your side
- 续魂再结 2266498 ritual summons on the opponent's turn — summon 混骸鬼 3909436 and declare Trap to block their 移魂再诞 2287848 recursion, or declare Monster to block their granted quick effects
- 之核 49394035-granted untargetable beats 归来者 31772684's quick-banish targeting, and 诛邪侠 34093683 makes your other cards untargetable
- The first player to ritual a boss with 复仇死者之夜 76871889 double attack usually wins the race; 白昼黎明 60375194 is the comeback wipe when behind on card count
- 噬腐鬼 29348048's ② revival needs 屠魔侠 4388680 name on your field — 诛邪侠 34093683 or 救世侠 91420202 satisfy it through name treatment

- **Common Mistakes**

- 爆诞 7986397 destroys the ritual monster at the end of the NEXT turn regardless of immunity — keep 诞生 94666032 in the GY to replace it; the replace checks the exact card 屠魔侠 4388680 and does NOT protect 诛邪侠 34093683 or 救世侠 91420202 even though their name is 屠魔侠
- 仪式的事前准备 13048472 only pairs with 诞生 94666032 (the only Vendread ritual spell listing a monster name); it cannot search with 爆诞 7986397, and pairing 极饿复仇死者 13386407 would only find 噬腐鬼 29348048, which 极饿 cannot summon
- 极饿复仇死者 13386407 cannot special summon 噬腐鬼 29348048 (explicitly excluded by its text)
- Granted effects need the material released FROM THE FIELD — discarding 之核 49394035, 归来者 31772684 or 地狱犬 67267333 from hand, or using 爆诞's deck-send, grants nothing
- 噬腐复仇死者 1855886 ② does not trigger when it itself is the released monster, only when another monster is released
- Do not resolve 噬腐复仇死者 ② before your non-复仇死者 plays (马头鬼 92826944, 齐唱僵尸 49959355, links like 召命之神弓-阿波罗萨 4280258) — the lock closes behind it
- The 还魂再生 30650147 token locks normal AND special summons to 复仇死者 while it is out and is 0-ATK ritual fodder; the released opponent monster's own release effects still trigger
- 移魂再诞 2287848 ② requires exactly 5 face-up banished Zombies to shuffle and draw 1
- 白昼黎明 60375194 needs the opponent to control more cards than you, and the surviving ritual monster cannot attack directly
- 复仇死者之夜 76871889 ② chain attack only hits monsters (the attacker gains a no-direct-attack clause)
- 阿尼玛 70491682 ① locks special summons to Zombies for the rest of the turn
- 归来者 31772684 ① triggers only when destroyed by the OPPONENT
- 噬腐鬼 29348048's ② revival is banished if it ever leaves the field
- Do not activate 混骸鬼 3909436 ① with an empty GY — it banishes a 复仇死者 card as cost
- 大尸教 21960890 ② only recovers banished LV4-or-lower Fiend/Zombie monsters — 屠魔侠 4388680 (LV6) is not a valid target
