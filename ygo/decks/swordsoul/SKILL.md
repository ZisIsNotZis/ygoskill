---
name: swordsoul-experience
description: 相剑 (Swordsoul) deck experience: Wyrm token-synchro engine, one-card combo, extenders, halt points
---
# 相剑 (Swordsoul) Deck Experience

- **Deck Identity**

- Engine monsters: 相剑师-莫邪 20001443, 相剑师-泰阿 56495147, 相剑军师-龙渊 93490856, non-Tuner Wyrm monsters that create Level 4 Wyrm Tuner tokens and Synchro into the Wyrm bosses
- Attributes differ per monster, 莫邪 20001443 is WATER Level 4, 泰阿 56495147 is WIND Level 4, 龙渊 93490856 is FIRE Level 6, the tokens are WATER, the deck is not DARK
- The Tuner is always the 相剑衍生物 token, not the main deck monsters, so the engine math is fixed at 4+4 equals Level 8 and 6+4 equals Level 10
- Searcher: 龙相剑现 56465981 adds 1 相剑 monster from deck to hand, or 1 Wyrm monster instead when you control a Synchro
- Extender: 白之圣女 艾克莉西娅 55273560 special summons itself when the opponent controls more monsters, then tributes itself to special summon a 相剑 monster from deck or hand
- Bosses: 相剑大师-赤霄 69248256, 相剑大公-承影 96633955, 相剑大邪-七星龙渊 47710198, plus generic 鲜花女男爵 84815190 and 深红剑士 80321197
- All 相剑 cards share setcode 0x16b in this codebase; tokens are 相剑衍生物 Wyrm WATER Level 4 ATK 0 DEF 0 Tuner, token codes 20001444, 56495148, 93490857, 14821891, 78836196, 99137267
- Modern support: 相剑瑞兽-纯钧 29884951, 妖眼之相剑师 62849088, 三英之相剑师 74405783, 轩辕之相剑师 82489470, 深渊之相剑龙 5141117, 赫圣之相剑 83308376, plus 阿不思的落胤 68468459 adjacency in fusion variants

- **Core Mechanic: Wyrm Token Synchro Engine**

- 莫邪 20001443 on Normal or Special Summon reveals 1 Swordsoul card or Wyrm monster from hand as cost and summons a token 20001444, and draws 1 card when used as Synchro material
- 泰阿 56495147 ignition banishes 1 Swordsoul card or Wyrm monster from graveyard as cost and summons a token 56495148, and sends 1 Swordsoul or Wyrm monster from deck to graveyard when used as Synchro material
- 龙渊 93490856 from hand discards 1 other Swordsoul or Wyrm monster as cost, special summons itself, optionally summons a token 93490857, and deals 1200 damage when used as Synchro material
- Every token locks the player out of non-Synchro Extra Deck summons while it is on the field, so Xyz and Link plays must happen before any token or not at all
- 龙相剑现 56465981 searches the starter and when banished raises or lowers a Swordsoul or Wyrm monster level by 1 until the end of the turn
- 大灵峰相剑门 93850690 revives a Swordsoul monster from graveyard, any Wyrm monster instead if you control a Synchro, and when banished changes a level by 1
- 相剑暗转 14821890 trap destroys 1 Wyrm you control plus 2 opponent cards, and when banished summons a token 14821891, making it the usual 赤霄 search-and-banish target
- 忆念之相剑 99137266 continuous trap banishes a Swordsoul card or Wyrm Synchro whenever any card is banished, and when banished summons a token 99137267
- 瑞相剑究 78836195 battle trick banishes up to 5 Swordsoul or Wyrm monsters from graveyard for 300 attack each, and when banished summons a token 78836196
- 承影 96633955 and 七星龙渊 47710198 both feed on banishing, so 大宇宙 30241314 floodgate, 天威之龙鬼神 5041348 banish-negation, and 忆念之相剑 99137266 form a banish engine

- **One-Card Combo: 相剑师-莫邪**

- There is no strict one-card starter, 莫邪's reveal, 泰阿's banish, and 龙渊's discard each need a second Swordsoul or Wyrm card, so the line opens with 莫邪 20001443 plus any Swordsoul or Wyrm card in hand
- Opening: activate 龙相剑现 56465981 to add 莫邪 20001443, normal summon it, reveal any Swordsoul or Wyrm card, even a spell such as 龙相剑现 itself, and summon token 20001444
- Step 1: Synchro 莫邪 plus token into 相剑大师-赤霄 69248256, its summon effect adds 1 Swordsoul card from deck to hand or banishes it face-up
- Step 2: banish 相剑暗转 14821890 from deck with 赤霄 instead of adding it, its banished effect summons token 14821891, and 莫邪's material effect draws 1 card
- Step 3: extend with 泰阿 56495147, banish 莫邪 from graveyard to make a token, then Synchro into a second 赤霄, 深红剑士 80321197, or 辉龙星-蚣蝮 83755611
- Step 4: drop 龙渊 93490856 from hand by discarding a Swordsoul or Wyrm card, make a token, and Synchro into 相剑大公-承影 96633955 or 鲜花女男爵 84815190, both Level 10 from 6 plus 4
- Step 5: 泰阿's material effect dumps 龙相剑现 56465981 or 相剑暗转 14821890 from deck to graveyard to set up their banished effects
- 白之圣女 艾克莉西娅 55273560 covers the missing second monster, tribute her to special summon 泰阿 from deck when the opening hand is short

- **End Field**

- Standard board: 相剑大师-赤霄 69248256 search plus negation, 相剑大公-承影 96633955 banish engine, and 鲜花女男爵 84815190 negate-and-destroy or 深红剑士 80321197 Level 5 and higher summon lock
- 相剑大邪-七星龙渊 47710198 Level 10 alternative: draws when you Synchro a Wyrm, banishes one opponent summon with 1200 burn, and banishes an opponent spell or trap activation with 1200 burn
- Set 相剑暗转 14821890 for a three-card destroy and 忆念之相剑 99137266 to convert every banish into more Swordsoul banishes, fueling 承影's attack
- Floodgates: 群雄割据 90846359 locks the opponent to one monster race, 大宇宙 30241314 sends everything to the banished zone, both protect a Wyrm-only board
- 天威之龙鬼神 5041348 Level 8 Wyrm Synchro tech banishes an opponent monster whose effect activates and gains attack in battle, and its banish triggers feed 承影
- 妖眼之相剑师 62849088 plus a token makes 蛇眼断罪龙 79415624 Level 12, and 灾厄之星 提·丰 93039339 ranks up on your strongest monster to stop 3000 or higher attack effects, but only when no token is on the field

- **Extenders**

- 白之圣女 艾克莉西娅 55273560: free special summon when the opponent has more monsters, tribute it to bring 莫邪, 泰阿, or 龙渊 from deck or hand, adding a summon mid-combo
- 龙渊 93490856 from hand: the discard cost accepts any Swordsoul or Wyrm card, so spent spells such as 龙相剑现 56465981 or 相剑暗转 14821890 are valid fuel
- 泰阿 56495147: ignition recycles graveyard Swordsoul or Wyrm cards, including spent spells, into tokens, and its material effect dumps the next extender
- 大灵峰相剑门 93850690: revives a spent 莫邪 or 泰阿 from graveyard to restart the token engine, and its banished effect adjusts levels for off-math Synchros
- 相剑瑞兽-纯钧 29884951: quick effect in either main phase tributes a monster to summon itself, destroys both itself and an opponent extra-deck summon in battle, and banishes a card on field or in either graveyard as Synchro material
- 妖眼之相剑师 62849088: quick effect special summons itself from hand while a negated effect monster is on the field, and when the opponent special summons, chooses special summon from your hand, draw 2, or destroy one of their extra-deck summons
- 轩辕之相剑师 82489470: negates an attack and summons itself from hand, and when a monster is banished face-up it banishes itself from field or graveyard to special summon a Light Spellcaster with equal ATK and DEF, namely 妖眼之相剑师 62849088
- 三英之相剑师 74405783: Level 8 Spellcaster Synchro from a Level 4 Tuner plus non-tuners, searches 妖眼之相剑师 62849088 from deck or graveyard, and negates a face-up card, destroying it too if 艾克莉西娅 or 阿不思的落胤 68468459 is in the graveyard
- 深渊之相剑龙 5141117: special summons itself from hand or graveyard when a monster is banished face-up by a card effect, banishing one field zone card and one opponent monster from field or graveyard, but only a Wyrm monster effect may summon it, so 大灵峰相剑门 93850690 cannot
- 赫圣之相剑 83308376: banishes any card on the field or in either graveyard while you control a Synchro, and recurs itself from graveyard by banishing a Synchro while the opponent controls an extra-deck monster

- **Halt Points**

- 灰流丽 14558127 on 莫邪 20001443 summon effect leaves a vanilla 1700 body with no token and ends the line unless a second summon exists
- 灰流丽 on 龙相剑现 56465981 search, on 泰阿 56495147 ignition, or on 白之圣女 艾克莉西娅 55273560 tribute effect stops the combo at different depths
- 墓穴的指名者 24224830 or 抹杀之指名者 65681983 on 莫邪, 泰阿, or 龙渊 in the graveyard kills all the graveyard-fueled extenders
- 无限泡影 10045474 or 效果遮蒙者 97268402 on 莫邪 or 赤霄 69248256 removes the token or the search, so save targeted negation for the searcher
- 原始生命态 尼比鲁 27204311 lands around the fifth summon, monster, token, 赤霄, token, monster, before the Level 10 bosses appear, so watch the summon count
- The deck is soft to 增殖的G 23434538, the full combo summons many times and every token counts toward the draw trigger
- The token lock is a self-imposed halt point, any Xyz or Link plan after a token is made is illegal in this codebase

- **Mirror Match: 相剑 vs 相剑**

- Both sides run the same Wyrm engine, so the player who resolves 龙相剑现 56465981 plus 莫邪 20001443 first establishes 赤霄 69248256 plus 承影 96633955 and wins the tempo race
- 承影's attack scales with the total banished count, so the banish war decides the mirror, and 相剑暗转 14821890 plus 忆念之相剑 99137266 control who wins it
- 赤霄's negation is the best interaction, negate the opponent 莫邪 summon effect or 泰阿 56495147 ignition before a token appears
- Negating an opponent monster with 赤霄 enables their 妖眼之相剑师 62849088 to special summon itself from hand, so negate only when a Level 8 body is acceptable
- 相剑暗转 14821890 always destroys one of your own Wyrms, so target a token or an about-to-be-spent monster, never a key boss
- 深红剑士 80321197 locks the opponent out of Level 5 and higher summons next turn, cutting 龙渊 93490856 and all Level 10 lines
- 灾厄之星 提·丰 93039339 answers the opponent's established 承影 board by overlaying onto your strongest monster, but only after your tokens are gone

- **Common Mistakes**

- Opening 泰阿 56495147 into an empty graveyard wastes its ignition, the banish cost needs graveyard fuel, so summon 莫邪 20001443 or 龙渊 93490856 first
- Reveal, banish, and discard costs accept any Swordsoul card or Wyrm monster, not just Swordsoul monsters, so spent spells like 龙相剑现 56465981 are legal fuel for 泰阿 and 龙渊
- Do not forget the token lock, making a token forbids Xyz and Link summons from the extra deck while it is on the field, so sequence 灾厄之星 提·丰 93039339 and similar plays before tokens
- 赤霄 69248256 search is add or banish, banishing 相剑暗转 14821890 or 忆念之相剑 99137266 from deck triggers their token effects, adding them sets disruption, choose per board state
- 大宇宙 30241314 sends everything to the banished zone instead of the graveyard, which also kills your own 莫邪 draw, 泰阿 ignition, and 承影 96633955 protection, so set it only after the board is established
- 群雄割据 90846359 allows one monster race per side, but 白之圣女 艾克莉西娅 55273560 is Fairy and 妖眼之相剑师 62849088 is Spellcaster, so never leave mixed races on the field with it active
- 深渊之相剑龙 5141117 can only be special summoned by a Wyrm monster effect, so 大灵峰相剑门 93850690 cannot summon it, while 邪龙星-睚眦 43202238 deck revive can
- 承影 96633955 destruction protection banishes from your graveyard, so over-burying the graveyard with 泰阿 costs leaves 承影 unprotected
- Do not activate 相剑暗转 14821890 with only bosses on board, the destroy targets include your own Wyrm, so keep a token around as the self-target
