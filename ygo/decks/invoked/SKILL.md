---
name: invoked-experience
description: 召唤师·阿莱斯特 (Invoked / 召唤魔术) deck experience: attribute fusion engine, one-card combo, extenders, halt points
---
# 召唤师·阿莱斯特 (Invoked) Deck Experience

- **Deck Identity**

- 阿莱斯特 (1880 deck folders) is the 召唤师·阿莱斯特 / 召唤魔术 engine, a tech splash in most folders but a coherent near-pure build here, anchored on the modern 2026-era support wave
- Strongest near-pure build in the repo: 260425召唤 folder (deck/260425召唤/c80e9f2cd20ce0db.ydk), running 召唤师 阿莱斯特 86120751 x3, 追忆的阿莱斯特 57294268 x3, 法之神灵 艾华斯 84288367 x3, 神灵剑 艾华斯 63926180 x3, 人工神灵 维拉卡姆 10673071 x3, 暴走魔法阵 47679935 x3, 召唤魔术 74063034 x2, 召唤魔术-「剑」 37432075 x2, 法之圣典 458748 x2, 魔法名-「新世界之始」 86319972, 暴走召唤师 阿莱斯特 97973962
- Extra deck: 超越召唤兽 纪元 33166263 x2 plus 索拉特 43989315, 普尔加托里奥 12307878, 巴巴伦 70383419, 大贤者兽 38423248, 埃律西昂 11270236, 光体 97300502, 俄刻阿诺斯 6772168, 雷电 49513164, and links 代理F魔术师 12450071, 转生炎兽 独角兔 60303245, 闪刀姬-阿泽莉娅 98462037, 至爱英雄 闪光火焰翼侠 87758525
- Draw engine and staples: 欢聚友伴·茸茸长尾山雀 42141493 x3, 灰流丽 14558127, 增殖的G 23434538, 次元吸引者 91800273, 屋敷童 73642296, 小丑与锁鸟 94145021, 墓穴的指名者 24224830, 无限泡影 10045474, 朔夜时雨 52038441, 星球改造 73628505
- The user-hypothesized fusions 圣魔美女莉丝梅 / 召唤兽·梅莉丝 / 召唤兽·索尔莱德 do not exist in cards.cdb; the real new fusions are 索拉特 43989315, 巴巴伦 70383419, 俄刻阿诺斯 6772168, 迪·阿尼玛 80635735, 大贤者兽 38423248, 纪元 33166263
- Setcodes verified in scripts: 0x1e1 (481) 阿莱斯特 monsters (86120751, 57294268, 97973962), 0xf4 (244) 召唤兽 fusion monsters, all fusion searches and 追忆's cost filter use these

- **Core Mechanic: Attribute Fusion Loop**

- 召唤师 阿莱斯特 86120751 on Normal Summon or Flip searches 召唤魔术 74063034 from deck, and as a quick effect discards itself from hand to give a Fusion monster you control 1000 ATK and DEF until end of turn
- 召唤魔术 74063034 fuses from the HAND only for generic fusions; for 召唤兽 fusions it may also use your field and BOTH players' graveyards, hand materials go to the graveyard while field and graveyard materials are banished
- The classic 8 fusions require the exact code 召唤师 阿莱斯特 86120751 plus one attribute monster: 普尔加托里奥 12307878 FIRE, 梅尔卡巴 75286621 LIGHT, 卡利古拉 13529466 DARK, 雷电 49513164 WIND, 科库托斯 85908279 WATER, 墨瓦腊泥加 48791583 EARTH, 光体 97300502 any Fusion monster, 大贤者兽 38423248 any Fusion/Synchro/Xyz/Link monster
- The new 0x1e1-setcode fusions accept any 阿莱斯特 monster instead of the exact code: 索拉特 43989315 plus FIRE or WIND, 巴巴伦 70383419 plus LIGHT or EARTH, 俄刻阿诺斯 6772168 plus WATER or DARK, 迪·阿尼玛 80635735 plus any Extra Deck summoned monster
- Recursion loop verified in scripts: 召唤魔术 74063034 in graveyard shuffles itself into the deck to add one BANISHED 召唤师 阿莱斯特 86120751 to hand, so use a field or graveyard Aleister as material to keep the loop alive
- 召唤魔术-「剑」 37432075 fuses from your FIELD monsters and for 召唤兽 may also use BANISHED monsters from both sides as material returning them to the graveyard, and its graveyard effect shuffles itself back to add a 0x1e1 monster or 召唤魔术 74063034 from the graveyard
- 暴走魔法阵 47679935 (field spell) searches 召唤师 阿莱斯特 86120751 on activation, makes your fusion-summon effects unnegatable, and stops the opponent responding after your Fusion Summon succeeds

- **One-Card Combo: 神灵剑 艾华斯**

- Step 1: activate 神灵剑 艾华斯 63926180 option one, special summon 法之神灵 艾华斯 84288367 from deck, note the turn's attack restriction to Fusion monsters only
- Step 2: 法之神灵 艾华斯 84288367 ignition effect from the field banishes itself, searches 追忆的阿莱斯特 57294268 from deck and grants an extra normal summon of a Spellcaster
- Step 3: normal summon 追忆的阿莱斯特 57294268, its summon trigger costs banishing 召唤兽 索拉特 43989315 from the Extra Deck and searches 召唤魔术-「剑」 37432075 or 召唤魔术 74063034
- Step 4: activate 召唤魔术-「剑」 37432075, fuse field 追忆 57294268 plus banished 索拉特 43989315 into 召唤兽 巴巴伦 70383419, 追忆 goes to the graveyard
- Step 5: 巴巴伦 70383419 searches 人工神灵 维拉卡姆 10673071 or 魔法名-「新世界之始」 86319972 and may banish one graveyard monster
- Step 6: 维拉卡姆 10673071 special summons itself from hand while 追忆 57294268 sits in the graveyard, then sets 召唤魔术 74063034 or 召唤魔术-「剑」 37432075 from deck
- Result: 巴巴伦 70383419 on field, set 召唤魔术, 维拉卡姆 10673071 or 新世界之始 86319972 in hand, 追忆 57294268 in graveyard for the next 召唤魔术 fusion
- Two-card engine baseline: normal summon 阿莱斯特 86120751 search 召唤魔术 74063034, 追忆 57294268 special summons itself targeting the Spellcaster, search a second 召唤魔术 or 剑, then fuse 阿莱斯特 plus 追忆 into 俄刻阿诺斯 6772168 or 卡利古拉 13529466

- **End Field**

- 埃律西昂 11270236 (3200/4000) with its quick effect banishing a 召唤兽 and all opponent monsters of the same attribute, made by 召唤魔术 74063034 or 剑 37432075 from one 召唤兽 plus one Extra Deck summoned monster such as 暴走召唤师 阿莱斯特 97973962 or a second fusion
- 俄刻阿诺斯 6772168 (3000/3000) in the Extra Monster Zone redirects opponent monsters headed to the graveyard into the banished zone, in a main monster zone it forces the opponent to attack only it
- 纪元 33166263 (3800) made from two Fusion monsters with different attributes, on summon banishes field and graveyard cards up to its material count and with 3 or more materials peeks at and banishes up to 3 opponent Extra Deck cards
- 迪·阿尼玛 80635735 destroys all opponent Extra Deck summoned monsters or all their spells and traps on summon, and chains to opponent graveyard effects by banishing itself to summon an 阿莱斯特 from deck and negate
- 梅尔卡巴 75286621 is the omni-negate discarding a card of the same type, 光体 97300502 destroys an opponent monster on their summon and grows by banishing fusion monsters, 卡利古拉 13529466 floodgates to one monster effect and one attack per turn
- 巴巴伦 70383419's graveyard effect banishes itself to make all opponent monsters lose attack equal to a target Fusion's attack, wiping 3800 from their field behind 纪元 33166263
- Follow-up comes from the hand loop: 召唤魔术 74063034 adds back the banished 召唤师 阿莱斯特 86120751, and 法之圣典 458748 tributes a 召唤兽 to summon a different-attribute 召唤兽 as a Fusion Summon on the next turn

- **Extenders**

- 追忆的阿莱斯特 57294268: special summons itself from hand targeting any face-up Spellcaster or Fusion monster including the opponent's, then its summon trigger searches 召唤魔术 74063034 or 召唤魔术-「剑」 37432075 at the cost of banishing one 召唤兽 from the Extra Deck
- 法之神灵 艾华斯 84288367: banishes itself from hand to search any 阿莱斯特 monster, from the field it additionally grants an extra Spellcaster normal summon, and in the graveyard it revives when your Fusion monster dies to a non-battle effect and fuses again from hand and field
- 人工神灵 维拉卡姆 10673071: special summons itself while an 阿莱斯特 monster is on field or in graveyard, sets 召唤魔术 74063034 or 剑 37432075 from deck, and chains to an opponent response against your Fusion effect by banishing itself to negate and banish that response
- 暴走召唤师 阿莱斯特 97973962: Link 2 of monsters with different races AND different attributes, its name becomes 召唤师 阿莱斯特, and every Fusion Summon while it is on field lets you discard one to add 召唤魔术 74063034 or 法之圣典 458748, the repeat value engine
- 召唤魔术-「杯」 76334960: while any 阿莱斯特 monster is on field, in graveyard, or banished, it fuses one of your hand or field monsters plus one monster from your DECK, or one of your monsters plus one opponent face-up monster, all materials banished
- 法之圣典 458748: tributes a 召唤兽 you control as cost and special summons a different-original-attribute 召唤兽 as a Fusion Summon, a card-neutral attribute swap that also triggers 暴走召唤师 97973962's search
- 魔法名-「新世界之始」 86319972: banishes an 阿莱斯特 or Fusion monster from the graveyard to special summon any 召唤兽 ignoring conditions for the turn, and from the graveyard revives a banished 召唤兽 whenever a monster is banished face-up
- 召唤兽 索拉特 43989315: quick effect revives any level 6 or lower monster from either graveyard with negated effects, and its graveyard effect fuses itself with your field and graveyard monsters into 纪元 33166263 or 埃律西昂 11270236
- 大贤者兽 38423248: on summon banishes a Fusion/Synchro/Xyz/Link from your graveyard plus one field monster, and when Fusion Summoned and destroyed special summons a level 4 Spellcaster from deck and equips itself to it
- 多层融合 58570206 and 超融合 48130397 appear in variant builds as generic fusion tools, 多层融合 can use up to the opponent's monster count of your Extra Deck monsters as material, the direct path to 纪元 33166263

- **Halt Points**

- 灰流丽 14558127 on 阿莱斯特's normal summon search, on 追忆 57294268's summon-trigger search after its Extra Deck cost, or on 维拉卡姆 10673071's set stops the engine because the search chain 艾华斯-to-追忆-to-剑 collapses
- 增殖的G 23434538 draws for every 追忆 57294268, 维拉卡姆 10673071, and Fusion Summon, play a shortened single-fusion line under it
- 无限泡影 10045474 and 效果遮蒙者 97268402 hit 追忆 57294268's summon-trigger search or 埃律西昂 11270236's quick banish, they cannot hit 追忆's hand ignition effect
- 墓穴的指名者 24224830 and 屋敷童 73642296 stop the graveyard recursion of 召唤魔术 74063034, 剑 37432075, and 索拉特 43989315, leaving the engine without fuel
- 小丑与锁鸟 94145021 limits the multiple searches per turn, and 次元吸引者 91800273 banishes instead of sending to graveyard, cutting 索拉特 43989315, 新世界之始 86319972, and both 召唤魔术 graveyard effects while the banished-pool cards still function
- 原始生命态 尼比鲁 27204311 wipes the board around the fourth or fifth special summon, keep 新世界之始 86319972 or 索拉特 43989315 to rebuild from the graveyard

- **Mirror Match: 召唤 vs 召唤**

- Every Invoked body is Extra Deck summoned, so 迪·阿尼玛 80635735's board wipe destroys the entire opponent board and whoever resolves it first wins the monster zone
- 俄刻阿诺斯 6772168 in the Extra Monster Zone banishes the opponent's graveyard-bound monsters, killing their 索拉特 43989315 ladder and 新世界之始 86319972 recursion
- 纪元 33166263's attribute lock turns every face-up monster into one attribute, then 埃律西昂 11270236 targets a graveyard 召唤兽 and banishes all opponent monsters sharing that attribute for a one-sided board wipe
- 梅尔卡巴 75286621 negates the opponent's 追忆 57294268 search and 埃律西昂 11270236 banish, 卡利古拉 13529466 floodgates their fusion laddering to one monster effect per turn
- 神灵剑 艾华斯 63926180 option three rips three random face-down cards from the opponent Extra Deck, their 召唤兽 materials and 大贤者兽 38423248 fuel
- 追忆 57294268's summon can target the opponent's fusion monster, gaining board presence and 1000 attack while stealing a body position, and whoever resolves 暴走魔法阵 47679935 first fuses without any response window

- **Common Mistakes**

- 召唤师 阿莱斯特 86120751 searches ONLY 召唤魔术 74063034, never 暴走魔法阵 47679935, get the field spell from 星球改造 73628505 or by drawing it, and 追忆 57294268 cannot search it either
- 召唤魔术 74063034 uses hand materials only for non-召唤兽 fusions, never fuse a generic monster with field monsters using it, 剑 37432075 is the field-materials card
- Field and graveyard materials of 召唤魔术 74063034 are BANISHED while hand materials go to the graveyard, and only a banished 阿莱斯特 can be recovered by its graveyard effect, so banish the field or graveyard Aleister instead of discarding it from hand
- 追忆的阿莱斯特 57294268 is not 召唤师 阿莱斯特 for fusion materials, the classic attribute fusions 普尔加托里奥 12307878, 梅尔卡巴 75286621, 卡利古拉 13529466, 雷电 49513164, 科库托斯 85908279, 墨瓦腊泥加 48791583, 光体 97300502, 大贤者兽 38423248 all need the exact code 86120751, 追忆 only fuses into 索拉特 43989315, 巴巴伦 70383419, 俄刻阿诺斯 6772168, 迪·阿尼玛 80635735
- 暴走召唤师 阿莱斯特 97973962 needs two monsters with both different races and different attributes, 阿莱斯特 86120751 plus 追忆 57294268 are both Spellcaster DARK and cannot link into it
- 追忆 57294268's search costs banishing a 召唤兽 from the Extra Deck, never pay it when that fusion is the only remaining 召唤兽, keep 新世界之始 86319972 in the graveyard to reclaim the banished one
- 索拉特 43989315 revives monsters with NEGATED effects, treat the revived body as fusion material only, and its graveyard fusion needs 索拉特 itself plus field and graveyard monsters all banished
- 法之圣典 458748 requires a DIFFERENT original attribute than the tributed 召唤兽 and cannot summon the same attribute, and it is a cost tribute before the summon
- 新世界之始 86319972's condition-ignoring summon is banished at the End Phase, use it as an all-in finisher not as part of the end board, and its graveyard effect only triggers on face-up banishes
- 埃律西昂 11270236 can only be summoned by its listed fusion materials and 魔法名-「大兽」 47457347 cannot revive it, only 新世界之始 86319972 ignores its summoning condition
- 召唤魔术-「杯」 76334960 banishes every material including the deck monster, plan the banished pool for 剑 37432075 and 新世界之始 86319972 instead of burning the deck blindly
- 俄刻阿诺斯 6772168's zone decides its effect, Extra Monster Zone for the graveyard redirect and main monster zone for the attack taunt, the two effects never apply at once
- 暴走魔法阵 47679935's protection only covers your own fusion-summon effects and its search on activation is optional, keep it on the field and do not activate it at the end of the turn for no value
- 大贤者兽 38423248's summon banishment takes one Fusion/Synchro/Xyz/Link from YOUR graveyard, check that you can spare that recursion fuel before resolving it
- 追忆 57294268's hand effect can target an opponent Spellcaster or Fusion monster, remember the option in the mirror instead of passing when your own field is empty
