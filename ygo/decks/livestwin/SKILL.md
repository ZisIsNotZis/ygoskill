---
name: livestwin-experience
description: 直播☆双子 / 邪恶★双子 (Live☆Twin / Evil Twins) deck experience: mechanics, one-card combo, extenders, halt points
---
# 直播☆双子 / 邪恶★双子 (Live☆Twin / Evil Twins) Deck Experience

- **Deck Identity**

- Main deck twins: 直播☆双子 姬丝基勒 36326160 (LIGHT LV2) and 直播☆双子 璃拉 73810864 (DARK LV2), each 500 ATK, each special summons the other from deck or hand when it is Normal or Special Summoned with no other monsters on the field
- Extra deck: 邪恶★双子 姬丝基勒 9205573 and 邪恶★双子 璃拉 36609518 (Link-2 Fiends, 1100 ATK), 邪恶★双子克星 麻烦·桑妮 93672138 (Link-4 Fiend, 3300 ATK), 邪恶★双子星 姬丝基勒·璃拉 62098216 (Level 8 Fiend, 2200 ATK, special summoned by tributing 2 Link monsters)
- Spells: 直播☆双子麻烦桑 37582948 (continuous spell, searches a 直播☆双子 monster on activation and burns opponent when they summon while an Evil★Twin is on field), 直播☆双子频道 35487920 (field spell, attack negation and end phase recycling of twins), 直播☆双子入口页 8083925 (continuous spell, discard 1 to special summon a Ki-sikil or Lil-la from deck)
- Reference list: pure Live☆Twin build in deck/220611双子 plays 3x each little twin, 2x 姬丝基勒·霜精 54257392, 1x 璃拉·糖果 81078880, 3x 麻烦桑 37582948, 3x 频道 35487920, 1x 入口页 8083925, and a heavy hand trap package 灰流丽 14558127, 增殖的G 23434538, 无限泡影 10045474, 幽鬼兔 59438930, 墓穴的指名者 24224830
- Build quirk: the extra deck runs 2x of each Evil★Twin link because the ② recursion loop cycles both links, plus generic Link-4s 双穹之骑士 阿斯特拉姆 21887175, 闭锁世界的冥神 98127546 and I:P百变莱娜 65741786 for board presence

- **Core Mechanic: Twin Tag Loop**

- Start with either little twin Normal Summoned on an empty field, its ① special summons the other little twin from deck or hand because scripts check setcode 0x152 (Ki-sikil) or 0x153 (Lil-la) in LOCATION_HAND+LOCATION_DECK
- Link the two little twins into 邪恶★双子 姬丝基勒 9205573 whose link material must include a Ki-sikil monster, then use its ② quick effect to revive 璃拉 73810864 from the graveyard because ① of the Evil★Twin link only draws if a Lil-la is already face-up on the field
- Link the revived 璃拉 with 9205573 into 邪恶★双子 璃拉 36609518 whose material must include a Lil-la, then use its ② to revive 姬丝基勒 36326160 from the graveyard, ending on one Evil★Twin link plus one little twin
- Each Evil★Twin ② is a quick effect usable in either player's main phase and only when the matching little twin is absent from the field, so the loop recycles graveyard twins every turn
- ① effects: 邪恶★双子 姬丝基勒 9205573 draws 1 card if a 璃拉 is on the field when it is summoned; 邪恶★双子 璃拉 36609518 destroys 1 card if a 姬丝基勒 is on the field when it is summoned
- Critical lock: every Evil★Twin ② activation applies EFFECT_CANNOT_SPECIAL_SUMMON for the rest of the turn that only allows Fiend monsters from the extra deck, verified in scripts as splimit checking RACE_FIEND in LOCATION_EXTRA, so plan non-Fiend Link plays before using ②

- **One-Card Combo: 姬丝基勒 36326160**

- Starter: 直播☆双子 姬丝基勒 36326160 in hand, no other cards needed
- Step 1: Normal Summon 姬丝基勒 on an empty field, its ① special summons 直播☆双子 璃拉 73810864 from the deck
- Step 2: Link both into 邪恶★双子 姬丝基勒 9205573, no draw trigger because no Lil-la remains on the field
- Step 3: activate 9205573 ② quick effect to special summon 璃拉 73810864 from the graveyard, now locked to Fiend-only extra deck summons this turn
- Step 4: Link 璃拉 and 9205573 into 邪恶★双子 璃拉 36609518, then use its ② to special summon 姬丝基勒 36326160 from the graveyard
- Step 5: end field is 36609518 plus 姬丝基勒 36326160 with both Evil★Twin ② recursion effects live for the next turn and 直播☆双子频道 35487920 ready to negate attacks and recycle twins at end phase

- **End Field**

- One-card end: 邪恶★双子 璃拉 36609518 plus 直播☆双子 姬丝基勒 36326160, 直播☆双子频道 35487920 face up for attack negation and end phase recycling, and full hand trap backup
- With an extender 姬丝基勒·霜精 54257392 or 璃拉·糖果 81078880 the end field becomes both Evil★Twin links 9205573 and 36609518 on the field, and 36609518 ① destroys one card because 9205573 carries the 0x152 Ki-sikil setcode
- Boss option: tribute both Evil★Twin links to special summon 邪恶★双子星 姬丝基勒·璃拉 62098216 from hand or graveyard, its ① forces the opponent to send field cards down to two if they control three or more, and it gains 2200 ATK and DEF if both a Ki-sikil and a Lil-la are in the graveyard for a 4400 beater
- 邪恶★双子克星 麻烦·桑妮 93672138 is a quick-effect link that can tribute itself to revive up to one Ki-sikil and one Lil-la from the graveyard, and from the graveyard can banish itself plus send an Evil★Twin from hand, deck, or field to the graveyard to send one field card to the graveyard
- Generic finishers: 双穹之骑士 阿斯特拉姆 21887175, 闭锁世界的冥神 98127546, 天霆号 阿宙斯 90448279 and the 同盟运输车 83152482 plus 破坏剑-龙破坏之剑 76218313 lock that stops the opponent from special summoning from the extra deck

- **Extenders**

- 姬丝基勒·霜精 54257392 special summons itself from the hand while a 璃拉 is on the field, and its graveyard effect banishes itself to draw 1 card whenever the opponent adds a card from the deck to hand while an Evil★Twin is on the field
- 璃拉·糖果 81078880 special summons itself from the hand while a 姬丝基勒 is on the field, and its graveyard effect lowers an opponent monster's ATK by battle damage dealt by an Evil★Twin
- 直播☆双子麻烦桑 37582948 searches any 直播☆双子 monster from the deck on activation, which grabs a second little twin or the 霜精 54257392 extender
- 直播☆双子入口页 8083925 discards 1 card to special summon a Ki-sikil or Lil-la from the deck but locks extra deck summons to Evil★Twin monsters only for the rest of the turn
- 直播☆双子频道 35487920 during the end phase returns a Ki-sikil or Lil-la from the graveyard to the deck, or to the hand instead if you control no monsters
- Newer support from later lists: 秘密口令句 61976639 searches a Live☆Twin or Evil★Twin spell or trap, 邪恶★双子挑战 98360333 revives a Ki-sikil or Lil-la and then performs one Evil★Twin link summon, 邪恶★双子礼物 60759087 swaps control of a twin with an opponent monster or returns a set spell or trap to the deck
- 直播☆双子 璃拉·甜蜜 82699999 is a hand trap that discards itself to negate the opponent's chain against a Live☆Twin effect and revives itself from the graveyard while a Ki-sikil is on the field

- **Halt Points**

- Ash Blossom 灰流丽 14558127 on the little twin ① activation stops the deck special summon and leaves only the Normal Summoned twin, ending the combo
- 无限泡影 10045474 or 效果遮蒙者 97268402 on the Evil★Twin ② recursion prevents the graveyard revival, breaking the loop
- The Fiend-only extra deck lock from any Evil★Twin ② forbids 双穹之骑士 阿斯特拉姆 21887175, I:P百变莱娜 65741786, and 天霆号 阿宙斯 90448279 for the rest of the turn, so climb those links before activating ②
- 增殖的G 23434538 taxes the whole line which performs four to six summons, stop after the first Evil★Twin link plus one little twin under G
- 姬丝基勒·霜精 54257392 graveyard draw requires an Evil★Twin on the field, so it is dead as a draw engine before the first link summon
- 邪恶★双子星 姬丝基勒·璃拉 62098216 requires exactly two Link monsters tributed from the field, do not attempt it with a little twin on the field
- 直播☆双子入口页 8083925 extra deck lock to Evil★Twin monsters prevents all generic links for the turn, use it only when ending on twins

- **Mirror Match: 直播☆双子 vs 直播☆双子**

- Both engines die to 无限泡影 10045474 or 效果遮蒙者 97268402 on the first little twin ① activation, whoever resolves the first Evil★Twin ② recursion first gets the graveyard advantage
- 邪恶★双子 璃拉 36609518 ① destruction resolves while a Ki-sikil is face-up, use it to remove the opponent's face-up little twin before they link
- 姬丝基勒·霜精 54257392 graveyard effect draws against the opponent's 直播☆双子麻烦桑 37582948 searches because it triggers on opponent deck additions while an Evil★Twin is on the field
- 墓穴的指名者 24224830 and 抹杀之指名者 65681983 banish the little twins or the ② recursion targets, use 抹杀之指名者 on the starter and 墓穴的指名者 on the graveyard revival
- 直播☆双子频道 35487920 attack negation and 邪恶★双子克星 麻烦·桑妮 93672138 graveyard spot removal decide the grind game, keep both available for the opponent's turn
- 邪恶★双子星 姬丝基勒·璃拉 62098216's forced send to two field cards is the biggest tempo swing, whoever lands it first usually wins the mirror

- **Common Mistakes**

- Do not Normal Summon a second monster before the little twin ①, its condition requires no other monsters on the field and scripts check Duel.GetFieldGroupCount tp LOCATION_MZONE equals 1
- Do not use an Evil★Twin ② before making generic non-Fiend links, the Fiend-only extra deck lock is permanent for the turn
- Do not expect 邪恶★双子 姬丝基勒 9205573 to draw or 邪恶★双子 璃拉 36609518 to destroy on the first loop, the ① triggers need the matching little twin face-up at summon time
- 邪恶★双子星 姬丝基勒·璃拉 62098216 cannot be Normal Summoned and must tribute two Link monsters, and its 2200 ATK boost needs both a Ki-sikil and a Lil-la in the graveyard
- 邪恶★双子克星 麻烦·桑妮 93672138 quick effect tribute is a cost, and its graveyard effect needs an Evil★Twin to send to the graveyard, do not banish the last Evil★Twin with 墓穴的指名者 24224830 first
- 直播☆双子频道 35487920 end phase effect targets a graveyard twin, choose the hand option only when you control no monsters
- The 同盟运输车 83152482 lock cannot use it as link material the turn it is summoned, and 破坏剑-龙破坏之剑 76218313 stops the opponent from special summoning from the extra deck while equipped
- 璃拉·糖果 81078880 attack reduction needs an Evil★Twin battle to have dealt damage first, do not fire it before combat

- **Build Quirks**

- The pure list carries 3x 直播☆双子麻烦桑 37582948 and 3x 直播☆双子频道 35487920 because the search spell fixes hands while the field spell protects the small board
- Later lists add 秘密口令句 61976639, 邪恶★双子挑战 98360333 and 邪恶★双子礼物 60759087 as trap based extenders, and the 2025 lists splice in Fiendsmith cards but the core 直播☆双子 engine stays identical
- The extra deck's 2x each Evil★Twin link is mandatory for the recursion loop, cutting to one copy breaks the second loop step
- Deck folder candidates 250927双子 and 260124双子 are 名推理 58577036 FTK-style shells with 天魔神 诺雷拉斯 48453776 and 刻魔 engines, not representative of the pure Live☆Twin experience, the clean reference list is deck/220611双子
