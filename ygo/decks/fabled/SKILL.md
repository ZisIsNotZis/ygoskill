---
name: fabled-experience
description: 魔轰神 (Fabled) deck experience: discard-trigger engine, Rescue Cat combo, end fields, extenders, halt points
---
# 魔轰神 (Fabled) Deck Experience

- **Deck Identity**

- The 魔轰神 decks in this corpus are the Duel Terminal archetype Fabled (TCG name); 魔轰神 (Fiend) and 魔轰神兽 (Beast) sub-groups share setcode 0x35, verified in scripts such as c19439119.lua and c22555834.lua
- This is NOT Morphtronic 变形斗士 (a separate 34-card archetype in cards.cdb) and NOT Dark World 暗黑界 (separate setcode); the folder's real identity is Fabled
- Corpus builds: pure Fabled synchro decks (deck folders 110000魔轰神, 180113魔轰神, 210717魔轰神) and modern Fabled+刻魔 Fiendsmith builds (241123魔轰神刻魔, 251025魔轰神刻魔阿不思的落胤)
- Discard-engine main monsters: 克露丝 19439119, 葛琳萝 24040093, 雷文 47217354, 库沙诺 97439806, 索尔基乌斯 72328962, 路里 97651498, 甘纳许 18282103, 凯希 56399890, 刻耳柏拉 82888408, 佳娃 29905795, 野槌 55277252, 阿凡克 83039608, 马可西亚 57630503, 贝希尔摩斯 68897338
- Synchro bosses: 雷吉恩 47395382, 尤尼科 44155002, 件 89194103, 瓦尔基鲁斯 54048462, 利威坦 39477584, 安德剌斯 9061682, 加麦基 94292987, 利威西卜魔 21281085
- Fabled support: 魔轰神界之阶 22555834, 魔轰神界的复活 57775790, 弑逆的魔轰神 55766177

- **Core Mechanic: Discard-Trigger Engine**

- Every main monster triggers on being discarded from hand to grave with REASON_DISCARD (verified in script c19439119.lua); 克露丝 19439119 revives a Lv4-or-below Fabled, 甘纳许 18282103 and 刻耳柏拉 82888408 and 路里 97651498 special summon themselves, 凯希 56399890 destroys a face-up card, 马可西亚 57630503 searches a Fabled spell or trap
- Discard outlets are the engine: 雷文 47217354 discards any number to gain levels and 400 ATK each, 佳娃 29905795 and 野槌 55277252 discard a Fabled to special summon themselves, 索尔基乌斯 72328962 revives from grave for two discards, 库沙诺 97439806 loops back to hand by discarding another Fabled
- 葛琳萝 24040093 sends itself as REASON_COST, which is NOT a discard, so it does not trigger 克露丝 or 凯希 even though the card leaves the hand
- The deck plays around hand count: 尤尼科 44155002 negates all opponent monster, spell, and trap effects while both players hold the same number of cards, and 件 89194103 is indestructible while you hold zero cards
- 魔轰神界之阶 22555834 field spell mills a Fabled on activation and returns one from grave to hand for a two-card discard, and its ATK boost applies only when your hand is smaller

- **One-Card Combo: 救援猫 14878871**

- Activate 救援猫 14878871 to special summon 甘纳许 18282103 and 刻耳柏拉 82888408 from deck; both are Lv3-or-below Beasts so the summon is legal
- Synchro 刻耳柏拉 (Lv2 Tuner) plus 甘纳许 (Lv3) into 雷吉恩 47395382, whose synchro summon draws until your hand has exactly two cards
- Continue from 雷吉恩 47395382 with a tuner in hand: 佳娃 29905795 discards a Fabled to special summon itself, then 雷吉恩 plus 佳娃 makes 光枪龙 50321796 to bounce a card, or 雷吉恩 plus 克露丝 19439119 makes 月华龙 黑蔷薇 33698022
- The discarded 克露丝 19439119 revives 甘纳许 18282103 from grave, which becomes the next material, and 凯希 56399890 discarded anywhere in the chain pops a face-up card
- Modern build upgrade: extend 雷吉恩 47395382 plus a tuner into 安德剌斯 9061682 (draw 2 then discard 1) and stack 加麦基 94292987 which special summons any Fabled from hand or deck on synchro summon

- **End Field**

- Pure build: 尤尼科 44155002 hand-count negate plus 件 89194103 plus 雷吉恩 47395382 or 光枪龙 50321796, backrow of 雷破 4178474, 魔族之链 50078509, and 因果切断 71587526, with a hand kept equal to the opponent for 尤尼科
- Classic boss line: 雷文 47217354 discards 克露丝 19439119 and 甘纳许 18282103, both special summon, then 雷文 (Lv4) plus 甘纳许 makes 瓦尔基鲁斯 54048462 whose discard-a-Fiend draw keeps fuel flowing toward 利威坦 39477584
- Modern build: 安德剌斯 9061682 plus 利威西卜魔 21281085 (tribute Fabled monsters to steal the opponent monsters) protected by 魔轰神界的复活 57775790 which chain-blocks the opponent on every Fabled synchro summon and recurs a Fabled from grave or banishment
- 利威坦 39477584 returns up to three Fabled from grave to hand when destroyed, so recursion fights through removal
- Fiendsmith shell (刻魔, setcode 0x1b0): 刻印群魔的刻魔锻冶师 60764609 discards itself to search 刻魔 spell or trap and 刻魔的镇魂棺 2463794 special summons a 刻魔 from hand or deck as link-1 extension

- **Extenders**

- 佳娃 29905795 discards any Fabled to special summon itself, turning any dead Fabled card into a body; 野槌 55277252 does the same and then special summons a Lv2-or-below Fabled from hand
- 克露丝 19439119 as a discarded card revives any Lv4-or-below Fabled from grave, and 葛琳萝 24040093 searches any Fabled monster from deck, so a discard outlet plus these two extends the full line
- 贝希尔摩斯 68897338 discards two or more Fabled including itself to pseudo-synchro summon a Fabled synchro whose level equals the sum, and from grave it banishes itself to special summon a Fabled whenever a card leaves your hand
- 魔轰神界的复活 57775790 on activation sets any other Fabled spell or trap from deck, and its third effect discards a Fabled card to draw one or special summon a Fabled from grave or banishment
- 弑逆的魔轰神 55766177 special summons a Fabled from grave and destroys a face-up card on field at the cost of one discard, usable as an interruption or revival during the opponent turn
- 索尔基乌斯 72328962 revives itself from grave for two discards and 阿凡克 83039608 revives itself for one discard, both refueling tuner counts for 尤尼科 44155002

- **Halt Points**

- Ash Blossom on 救援猫 14878871 ends the pure line with no summon left; on 克露丝 19439119 revive it stops the follow-up, and 墓穴的指名者 on 克露丝 or 甘纳许 18282103 shuts down grave recursion
- Droll and Lock Bird punishes the draw chain of 雷吉恩 47395382 plus 科技属 超图书馆员 90953320, both of which appear in the corpus lists
- 增殖的G taxes the many special summons; stop after 雷吉恩 47395382 if the opponent resolves it, since the archetype cannot combo without summoning
- 尤尼科 44155002 only negates while hand counts match, so any forced draw or discard on your side turns it off mid-chain; never rely on it blindly
- 凯希 56399890 destroys face-up cards only and requires a discard, so it fails against set monsters and when your hand is empty
- 安德剌斯 9061682 gives the opponent the option to discard one card to negate its draw, so do not count on the plus two against a full opponent hand

- **Mirror Match: 魔轰神 vs 魔轰神**

- The player who discards first feeds the other: 安德剌斯 9061682 effect two steals any monster the opponent discards, so 佳娃 29905795 and 野槌 55277252 discards become your monsters
- 尤尼科 44155002 mirror is decided by hand count: whoever can hold exactly the same number of cards as the opponent keeps the negate online, so sequence draws and discards to match
- 凯希 56399890 trades one discard to pop the opponent tuner; killing 刻耳柏拉 82888408 before the synchro summon halts their level math
- 件 89194103 is indestructible at zero hand, so in the mirror keep your hand empty on their turn or remove it with 凯希 before it matters

- **Common Mistakes**

- Do not expect 葛琳萝 24040093's self-send to trigger the discard effects; the script marks it REASON_COST, so chain 雷文 47217354 or 佳娃 29905795 discards instead
- 甘纳许 18282103 is banished when it leaves the field after its own discard summon, so do not count on it returning to grave from the field for recursion
- 雷文 47217354 level and ATK gain lasts only until the end of turn, so all synchro math must happen in the same turn
- 库沙诺 97439806 needs another Fabled in hand to return itself, and 野槌 55277252 second effect only summons a Lv2-or-below Fabled, so check hand composition before activating
- 佳娃 29905795 and 野槌 55277252 discard as a cost, which resolves before their summon, so they cannot activate with an empty hand
- 安德剌斯 9061682 effect two triggers only when the OPPONENT discards, never on your own discards
- 加麦基 94292987's deck special summon happens on synchro summon and its draw-and-discard happens when sent to grave, so sequence it to avoid decking or hand-size misplays
- 魔轰神界的复活 57775790 chain-block applies only to your own Fabled synchro summons, and its one-per-turn discards must be Fabled cards
- 尤尼科 44155002 compares hand counts at effect resolution, so activating it while holding more cards than the opponent leaves the field open
