---
name: nekroz-experience
description: 影灵衣 (Nekroz) deck experience: ritual engine and cycle loop, one-card starters, extenders, halt points
---
# 影灵衣 (Nekroz) Deck Experience

- **Deck Identity**

- WATER ritual archetype, setcode 180 (0xb4), races mix Warrior/Spellcaster/Dragon/Wyrm
- Every ritual monster can only be special summoned by a ritual summon (aux.ritlimit in scripts), most with extra material restrictions, so they cannot be revived or cheated out
- Engine splits into four ritual spells, discard-searcher ritual monsters, and small monsters that search when released
- Extra Deck is ritual fodder, not monsters: 虹光之宣告者 79606837 and 旧神努茨 80532587 are sent to the GY by 万华镜 51124303
- Repo decks: 141115影灵衣/141220影灵衣 classic 千手神-Diva build, 220716影灵衣/241123影灵衣 modern 阿旺斯/艾米莉娅 build

- **Core Mechanic: 手牌仪式与轮回镜循环**

- Ritual summon is hand-based: 降魔镜 14735698 and 万华镜 51124303 summon from hand, 返魂术 97211663 from hand or GY, 神魔镜 50596425 from hand or the banished zone
- 降魔镜 14735698: tribute hand/field monsters OR banish Nekroz monsters from your GY as substitute, levels must sum EXACTLY to the ritual monster's level
- 万华镜 51124303: exactly 1 material, either 1 hand/field monster or 1 Extra Deck monster (level over 0, Xyz/Link not allowed) sent to the GY; then ritual summon ANY number of Nekroz rituals from hand whose total levels equal the material's level
- 神魔镜 50596425: Main Phase only, tribute sum may EXCEED the level, may send Nekroz monsters from the Extra Deck as substitute, summons from hand or banishment
- 返魂术 97211663: summons from hand or GRAVE, hand/field tribute only, exact level
- 轮回 loop: every ritual spell's GY effect banishes itself plus 1 Nekroz monster from GY to add 1 Nekroz spell from deck; 降魔镜/万华镜/返魂术 require YOUR field empty, 神魔镜 does not (empty-field condition verified in scripts)
- Discard engine: 光枪龙之影灵衣 26674724 discards to add any Nekroz monster, 辉剑鸟之影灵衣 99185129 discards to add any Nekroz spell/trap, 尤尼科之影灵衣 89463537 discards to recycle any Nekroz card from GY
- Full-tribute: 施里特 90307777, 阿旺斯 51618973 and 艾米莉娅 87003671 count as the entire needed level, implemented as a packed ritual level the core splits into high/low 16 bits (verified in ocgcore get_sum_params)
- Small monsters trigger when released by an effect, and ritual tribute counts as effect release, so tributing them during a summon chains their searches
- Floodgate presence: 尤尼科 89463537 negates effects of all face-up Extra-Deck-special-summoned monsters on both fields, 舞姬 52738610 stops the opponent chaining to your ritual spell activations and targeting your rituals, 索菲娅之影灵衣 21105106 locks Extra Deck summons during Main Phase 1

- **One-Card Starter: 千手神 23401839 / 万手神 95492061**

- No pure Nekroz one-card line reaches a ritual summon: a ritual spell AND a ritual monster must both be in hand and one search chain can only produce one of them
- Normal 千手神/万手神 → add 光枪龙之影灵衣 26674724 → discard it → add 辉剑鸟之影灵衣 99185129 or 施里特 90307777 → hand plus two, still needs a ritual spell as the second card
- 阿旺斯 51618973 one-card: normal summon → special summon 艾米莉娅 87003671 from deck → she adds a ritual monster or ritual spell → hand plus two, no summon
- Classic 深海歌后 78868119 one-card: normal summon → special summon 海皇的重装兵 37104630 from deck → Synchro into 虹光之宣告者 79606837, hold Herald as its negate and its GY search for later

- **Two-Card Ritual Baseline**

- 万华镜 51124303 + 尤尼科之影灵衣 89463537: send 虹光之宣告者 79606837 (Lv4) from Extra Deck → ritual summon 尤尼科 → Herald GY search adds 光枪龙 26674724 → discard it → 辉剑鸟 99185129 → discard it → 降魔镜 14735698, 尤尼科 floodgate is live
- 降魔镜 14735698 + 施里特 90307777: 施里特 counts as the full Lv9 tribute → ritual summon 三叉龙之影灵衣 52068432 → banish 1 card each from opponent hand (random), field and GY → 施里特 release search adds 光枪龙 26674724 → discard chain continues
- 阿旺斯 51618973 + 神魔镜 50596425: 阿旺斯 summons 艾米莉娅 87003671 → she searches 尤尼科 89463537 → 神魔镜 in Main Phase tributes 阿旺斯 and 艾米莉娅 as full tribute → 尤尼科 on field
- 深海歌后 78868119 into 虹光之宣告者 79606837 plus any ritual spell in hand: tribute Herald for 尤尼科, Herald's GY search adds the next ritual monster

- **End Field**

- 尤尼科之影灵衣 89463537 with 天枪龙之影灵衣 74122412 (quick destroy plus destruction immunity) and 舞姬 52738610, hand holding 瓦尔基鲁斯 25857246 or 三叉龙 52068432 as interrupts
- 索菲娅之影灵衣 21105106 board: ritual summoned from hand with 3 of your field monsters of different types → banish all cards on field and in GY except itself, plus the Main Phase 1 Extra Deck lock
- Modern board: 分体论聚合员 9940036 (Rank 9) made with 三叉龙 52068432 and a level-adjusted 巫女艾莉娅儿 56827051, on Xyz summon dumps 1 Extra Deck card to trigger 虹光之宣告者 79606837, negates a face-up card when it goes to the GY
- 瓦尔基鲁斯 25857246 in hand: negate an attack and end the battle phase by discarding itself plus banishing 1 Nekroz from GY, or tribute up to 2 hand/field monsters to draw that many
- 千查万别 24207889 floodgate fits the board while rituals stay mostly Warrior/Spellcaster; beware 灾亡虫 52846880 (Dragon) and 炼机圣 13408726 (Wyrm)

- **Extender: 增援 32807846 / 仪式的准备 96729612**

- 增援 32807846 adds any Lv4-or-lower Warrior: 阿旺斯 51618973, 艾米莉娅 87003671, 施里特 90307777, 舞姬 52738610
- 仪式的准备 96729612 adds a Lv7-or-lower ritual monster (光枪龙 26674724, 尤尼科 89463537, 辉剑鸟 99185129, 天枪龙 74122412, 瓦尔基鲁斯 25857246) then optionally a ritual spell from your GY

- **Extender: 影灵衣 monsters on release**

- 施里特 90307777: add any Warrior Nekroz ritual, covers 光枪龙 26674724, 三叉龙 52068432, 决战兵器 88240999, 毒枪龙骑士 39468724, 辉剑鸟 99185129
- 巫女艾莉娅儿 56827051: reveal any number of Nekroz cards to change her level by that count (enables Rank 9 and Lv9 万华镜 fodder), then add any non-ritual Nekroz on release
- 舞姬 52738610: add any face-up banished Nekroz monster on release, feeding the 神魔镜 50596425 banish-zone engine
- 阿旺斯 51618973: once per duel, return any number of banished Nekroz cards to hand on release
- 大魔道士 27796375: on release add a Spellcaster Nekroz ritual (瓦尔基鲁斯 25857246, 天枪龙 74122412, 尤尼科 89463537, 索菲娅 21105106), on banish send 1 Nekroz monster from deck to GY
- 战士艾可萨龙 53180020: on release add the Dragon ritual 灾亡虫之影灵衣 52846880, on banish special summon 1 banished Nekroz monster
- 艾米莉娅 87003671: special summon herself from hand if a Warrior Nekroz is on your field or in your GY

- **Extender: 万华镜 51124303 fodder**

- 虹光之宣告者 79606837 (Lv4): sent by 万华镜 → search any ritual monster, and it doubles as a negate that releases itself
- 旧神努茨 80532587 (Lv4): sent by 万华镜 → destroy 1 card on the field
- 中生代化石骑士 骷髅骑士 59531356 / 超念导体 比蒙巨兽 15028680 (Lv6): sent by 万华镜 → summon 光枪龙之影灵衣 26674724
- 索菲娅之影灵衣 21105106: during your Main Phase 1 discard it plus 1 Nekroz spell → opponent cannot special summon from the Extra Deck that phase

- **Halt Points**

- 灰流丽 14558127 stops every search: 千手神/万手神 23401839/95492061, 阿旺斯 51618973, 艾米莉娅 87003671, 光枪龙 26674724, 辉剑鸟 99185129, 虹光之宣告者 79606837, 仪式的准备 96729612
- 墓穴的指名者 24224830 answers the 万华镜 51124303 fodder by negating the 虹光之宣告者 79606837 / 旧神努茨 80532587 GY triggers
- 增殖的G 23434538 punishes every search and ritual summon, stop at 尤尼科 89463537 when it resolves
- 效果遮蒙者 97268402 / 无限泡影 10045474 on 阿旺斯 51618973 or 艾米莉娅 87003671 ends the modern engine
- 小丑与锁鸟 94145021 blocks the discard-search chain, 次元吸引者 91800273 banishes everything headed to the GY and starves the engine
- Self-halt: 降魔镜/万华镜/返魂术 GY searches need YOUR field empty, 神魔镜 50596425 is the only GY search usable with monsters on your field

- **Mirror Match: 影灵衣 vs 影灵衣**

- 尤尼科 89463537 does NOT stop Nekroz rituals, they are summoned from the hand not the Extra Deck, it only hits the Herald/N'tss/分体论聚合员 plays
- First 万华镜 51124303 → 虹光之宣告者 79606837 → 尤尼科 chain wins the floodgate race, 天枪龙 74122412 answers the opponent's 尤尼科
- 三叉龙 52068432 randomly banishes the opponent's hand search pieces, 索菲娅 21105106 Main Phase 1 lock ends the duel
- 决战兵器 88240999 destroys and banishes the opponent's face-down cards, 瓦尔基鲁斯 25857246 negates attacks and ends the battle phase
- 舞姬 52738610 decides ritual spell fights, whoever activates the ritual spell with 舞姬 face-up resolves first

- **Common Mistakes**

- Do not activate the 降魔镜 14735698 / 万华镜 51124303 / 返魂术 97211663 GY search with monsters on your field, use 神魔镜 50596425 instead
- 神魔镜 50596425 is Main Phase only, never plan a 神魔镜 ritual summon on the opponent's turn, its GY search is fine anytime
- 万华镜 51124303 needs an exact level: Lv4 虹光之宣告者 79606837 can only summon Lv4 尤尼科 89463537, Lv3 辉剑鸟 99185129 needs Lv3 fodder, 光枪龙 26674724 needs Lv6
- 降魔镜/返魂术 need an EXACT level sum while 神魔镜 allows over-tribute, 施里特/阿旺斯/艾米莉娅 full-tribute in all three
- Respect material restrictions: no Lv8 material for 瓦尔基鲁斯 25857246, no same-name material for 光枪龙 26674724 and 灾亡虫 52846880, no Lv9 for 三叉龙 52068432 and 炼机圣 13408726, no Lv10 for 决战兵器 88240999 and 毒枪龙骑士 39468724
- 索菲娅 21105106 wipe removes YOUR field and GY too and locks your own summons for the turn, count both sides before activating
- 尤尼科 89463537 negates your own Extra Deck summons, do not Synchro 虹光之宣告者 or Xyz 分体论聚合员 9940036 under your own Unicore, send fodder with 万华镜 instead
- 光枪龙 26674724 bounce only hits Extra-Deck-special-summoned monsters, 三叉龙 52068432 hand banish is random
- Discards are costs that stock the GY on purpose, they feed 降魔镜 banishes, 返魂术 GY summons and 神魔镜 banish-zone summons, keep the grave alive
- 增援 32807846 cannot search 千手神/万手神, they are Fairy not Warrior
- Do not extend into 增殖的G 23434538, the ceiling is 尤尼科 plus one searched card
