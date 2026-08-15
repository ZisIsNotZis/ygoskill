---
name: assaultmode-experience
description: 爆裂模式 (Assault Mode) deck experience: mechanics, one-card combo, extenders, halt points
---
# 爆裂模式 (Assault Mode) Deck Experience

- **Deck Identity**

- TRUE identity: Assault Mode (アサルトモード, 爆裂模式), NOT Burst Blader 破戒 — zero 破戒 deck folders exist and every 爆裂/爆裂模式 folder runs the 0x104f setcode Assault Mode cards
- The deck releases (tributes) a Synchro monster and summons its 「/爆裂体」 Assault Mode form from the deck via the trap 爆裂模式 80280737
- Modern 2025 support build (e.g. deck folder 251025爆裂) is far stronger than the 2008 classic and is the coherent build to play
- Main engine: 念动力反射者 74644400 (Level 1 Psychic tuner), 爆裂兽 3431737, 爆裂狙击手 39015, 爆裂巫妖 86098176, 爆裂音速战士 18711696
- Key spells and traps: 爆裂模式 80280737, 爆裂模式零型 88332693, 决斗进化-爆裂区域 91002901, 爆裂再起 74431740, 爆裂反击 76407432, 爆裂斩 40012727, 爆裂爆发 93469007, 爆裂瞬间移动 29863101, 再爆裂 56252810
- Extra deck boss forms (/爆裂体): 星尘龙/爆裂体 61257789, 深红剑士/爆裂体 50604072, 红莲魔龙/爆裂体 77336644, 真红莲新星龙/爆裂体 82323997, 科技属 戟炮手/爆裂体 47027714, 黑蔷薇龙/爆裂体 46985799
- Generic extra support: 黑翼的祭司 79519259, 加速同调星尘龙 30983281, 鲜花女男爵 84815190, S：P小夜骑士 29301450, 灾厄之星 提·丰 93039339, PSY骨架王·Ω 74586817, 星风狼 沃尔夫拉叶狼 3322931

- **Core Mechanic: Assault Mode Release**

- 爆裂模式 80280737 (trap): release 1 Synchro you control (or, after 决斗进化-爆裂区域 91002901 ③, 1 from the Extra Deck) as cost, then special summon 1 「/爆裂体」 monster from the DECK attack position
- The released Synchro and the summoned form are name-matched by a hardcoded assault_name in each script: 星尘龙 44508094 ↔ 星尘龙/爆裂体 61257789, 深红剑士 80321197 ↔ 深红剑士/爆裂体 50604072, 红莲魔龙 70902743 ↔ 红莲魔龙/爆裂体 77336644, 真红莲新星龙 97489701 ↔ 真红莲新星龙/爆裂体 82323997, 科技属 戟炮手 97836203 ↔ 科技属 戟炮手/爆裂体 47027714, 黑蔷薇龙 73580471 ↔ 黑蔷薇龙/爆裂体 46985799
- Activation is illegal with Synchros that have no /爆裂体 form: 黑翼的祭司 79519259, 加速同调星尘龙 30983281, 鲜花女男爵 84815190 can never be released for it
- /爆裂体 monsters are Synchro-type Effect monsters (Level 9-12) with a summon restriction: only 爆裂模式 80280737, 爆裂模式零型 88332693 (counts as an Assault Mode summon), 爆裂再起 74431740 and 再爆裂 56252810 (ignore conditions) or their own effects can summon them
- 念动力反射者 74644400: ① on Normal/Special Summon add 爆裂模式 80280737 or any card listing it (爆裂兽 3431737, 深红剑士/爆裂体 50604072, etc.) from deck; ② reveal 爆裂模式 in hand to special summon 1 monster listing 爆裂模式 from your grave (except itself) and raise its Level by 1-4
- 爆裂兽 3431737: discard itself from hand to add 爆裂模式 80280737 from deck, then becomes the revive target that 念动力反射者 74644400 ② turns into Synchro material (Level 4, raise +3 = 7)
- 黑翼的祭司 79519259 (Level 8 Synchro, generic tuner + 1+ non-tuner): ① on Special Summon set 爆裂模式 80280737 from hand/deck/grave, activable the same turn it is set — the key to same-turn combos; ② discard 1 to add or special summon 1 monster listing 爆裂模式 from deck, then only Synchro from the Extra Deck this turn
- 决斗进化-爆裂区域 91002901 (field): ① on activation add 1 monster listing 爆裂模式 from deck/grave; ② /爆裂体 special summoned this turn are indestructible by battle or opponent effects; ③ pay 2000 LP, once per turn, to allow releasing the Synchro for 爆裂模式 from the Extra Deck — this lets 星尘龙 44508094 in the Extra Deck pay for 星尘龙/爆裂体 61257789 without ever summoning it
- 爆裂狙击手 39015: ① release itself to special summon 1 monster listing 爆裂模式 from hand/deck, then only Synchro from the Extra Deck this turn; ② change a monster's Type and Attribute to match a revealed Extra Deck Synchro (fixes Synchro material race/attribute requirements)
- 爆裂模式 80280737 summons only from the DECK: the boss copy must stay in deck; 深红剑士/爆裂体 50604072 (reveal in hand → search → return itself to deck) and 爆裂再起 74431740 ② (shuffle grave copies back) keep it accessible

- **One-Card Combo: 紧急瞬间移动 67723438**

- Activate 紧急瞬间移动 67723438 (quick-play) to special summon 念动力反射者 74644400 from the deck (Level 1 Psychic), then its ① adds 爆裂模式 80280737
- One-card output is the tuner on field plus the trap in hand; the full board needs one more card (爆裂兽 3431737 or a discard outlet to seed the grave)
- Full two-card line: with 爆裂兽 3431737 also in hand, discard it to search a second 爆裂模式, then 念动力反射者 ② reveals 爆裂模式 and revives 爆裂兽 from the grave at Level +3 = 7
- Synchro: 念动力反射者 74644400 (1) + 爆裂兽 3431737 (7) = 黑翼的祭司 79519259 (8)
- 黑翼的祭司 ① sets 爆裂模式 80280737 from deck, activable same turn; ② discards 1 to add 星尘龙/爆裂体 61257789 to hand (or special summon 爆裂狙击手 39015)
- 决斗进化-爆裂区域 91002901 (via 星球改造 73628505 or its own activation) ③ pays 2000
- Activate the set 爆裂模式 80280737, release 星尘龙 44508094 from the Extra Deck, special summon 星尘龙/爆裂体 61257789 (3000 ATK, protected this turn by the field)

- **End Field**

- 星尘龙/爆裂体 61257789: omni-negate — release itself to negate and destroy any monster effect, spell or trap activation, then special summons itself back from the grave in the End Phase; when destroyed on field it revives 星尘龙 44508094 from grave
- 黑翼的祭司 79519259 (2500) as the second body and search engine; 决斗进化-爆裂区域 91002901 face-up for protection and next-turn ③
- Hand pieces: 深红剑士/爆裂体 50604072 (recursive hand search) or 爆裂反击 76407432; set 爆裂再起 74431740, 爆裂斩 40012727 or a second 爆裂模式 80280737
- Boss swap options on the opponent turn: 深红剑士/爆裂体 50604072 (3300, opponent cannot activate effects of Level 5+ monsters special summoned from the Extra Deck — note deck-special-summoned /爆裂体 are NOT hit), 科技属 戟炮手/爆裂体 47027714 (4500, negates monster summons and banishes all opponent special summoned monsters), 真红莲新星龙/爆裂体 82323997 (4000, chain-banishes opponent cards up to the tuner count and negates attacks), 红莲魔龙/爆裂体 77336644 (3500, destroys all other monsters after it attacks)
- 爆裂再起 74431740 pivot: release 星尘龙/爆裂体 61257789 to summon 深红剑士/爆裂体 50604072 from deck in defense for the Extra Deck lock — or keep the omni-negate instead, do not pivot blindly
- 加速同调星尘龙 30983281 alternative route: release it in the Main Phase to special summon 星尘龙 44508094 from the Extra Deck as a Synchro summon, then Synchro summon again, giving a field 星尘龙 to release for 爆裂模式 80280737

- **Extenders**

- 爆裂狙击手 39015: release itself to special summon 爆裂兽 3431737 or 念动力反射者 74644400 from the deck; resolve before any Xyz/Link play because of the Synchro-only lock
- 爆裂模式零型 88332693 (quick-play): ① release 1 Synchro on field to special summon the matching /爆裂体 from the HAND as an Assault Mode summon — search the boss to hand first; ② in grave, banish it to set 爆裂模式 80280737 from hand/deck, activable same turn (trap recycling)
- 爆裂再起 74431740: ① release 1 /爆裂体 to special summon a different /爆裂体 from deck in defense, ignoring conditions; ② quick effect from grave, banish, to shuffle any number of 爆裂模式 / listing cards from grave back to deck
- 爆裂巫妖 86098176: ① on Normal/Special Summon revives 1 monster listing 爆裂模式 or a Level 4 or lower Zombie from grave (revives 爆裂兽 3431737 or 爆裂狙击手 39015); ② is a non-tuner while on field; ③ when sent to grave as Synchro material adds 爆裂斩 40012727 or 爆裂反击 76407432 from deck
- 爆裂音速战士 18711696: special summons itself while 废品战士 60800381, 爆裂模式 80280737 or a listing card is on field; on Normal/Special Summon adds 1 同调士 monster or 爆裂模式 from deck (Junk/同调士 bridge)
- 一对一 2295440: discard 1 monster, special summon 念动力反射者 74644400 (Level 1) from deck
- 爆裂瞬间移动 29863101: return 1 /爆裂体 from hand to deck, draw 2 (filters hand, refills the deck with the boss 爆裂模式 80280737 needs)
- 深红剑士/爆裂体 50604072 in hand: reveal it, add 爆裂模式 80280737 or a listing card from deck, then return itself to deck — repeatable search that also keeps the deck stocked
- 再爆裂 56252810: banish 爆裂模式 80280737 from grave to destroy all your monsters and special summon 1 /爆裂体 from grave ignoring conditions (its effects are negated, it cannot be released, banished when it leaves the field) — emergency recovery, not a main line

- **Halt Points**

- 灰流丽 14558127 stops 念动力反射者 74644400 ① and 爆裂兽 3431737 searches, 黑翼的祭司 79519259 ②, and 爆裂狙击手 39015 ① deck special summons
- 增殖的G 23434538: the full line special summons five or more times, hand the opponent the draws or stop early
- 原始生命态尼比鲁 27204311: five summons triggers the wipe, stop before the fifth summon or sequence the field-spell ③ after Nibiru has resolved
- 效果遮蒙者 or 无限泡影 on 念动力反射者 74644400 ② or on 黑翼的祭司 79519259 ① removes the same-turn 爆裂模式 80280737 access
- 墓穴指名者 24224830 and 抹杀指名者 65681983 answer hand traps and the grave recursion of 爆裂再起 74431740 ② and 爆裂模式零型 88332693 ②
- 小丑与锁鸟 94145021 blocks the deck-adds of 黑翼的祭司 79519259 ② and 决斗进化-爆裂区域 91002901 ①
- Respect your own Synchro-only lock: resolve Xyz/Link first (S：P小夜骑士 29301450, 灾厄之星 提·丰 93039339), then use 爆裂狙击手 39015 ① or 黑翼的祭司 79519259 ②

- **Mirror Match**

- Whoever resolves 爆裂模式 80280737 or 决斗进化-爆裂区域 91002901 ③ first wins the negate war; chain 星尘龙/爆裂体 61257789 to the opponent 爆裂模式 activation to negate and destroy it (it re-summons itself in the End Phase)
- 深红剑士/爆裂体 50604072 locks only Level 5+ monsters special summoned from the Extra Deck, so the opponent deck-special-summoned /爆裂体 bosses still work — strip their base Synchros and the field-spell ③ instead
- 爆裂反击 76407432 negates the opponent 爆裂模式 80280737 activation while you control a face-up /爆裂体 — hold it until their release is declared
- Remove the opponent engine pieces 念动力反射者 74644400 and 爆裂兽 3431737 before they convert; without them no 爆裂模式 80280737 is ever live
- 爆裂斩 40012727 (wipe, needs your own /爆裂体) and 灾厄之星 提·丰 93039339 (stops 科技属 戟炮手/爆裂体 47027714 and 真红莲新星龙/爆裂体 82323997 from activating) are the mirror sideboard answers

- **Common Mistakes**

- Releasing a Synchro without a /爆裂体 form (黑翼的祭司 79519259, 加速同调星尘龙 30983281, 鲜花女男爵 84815190) — 爆裂模式 80280737 cannot be activated, only 星尘龙 44508094, 深红剑士 80321197, 红莲魔龙 70902743, 真红莲新星龙 97489701, 科技属 戟炮手 97836203 and 黑蔷薇龙 73580471 have forms
- 爆裂模式 80280737 summons from the DECK: with all boss copies in hand or grave the activation fails — keep one in deck via 深红剑士/爆裂体 50604072 bounce, 爆裂再起 74431740 ② or 爆裂模式零型 88332693 ②
- /爆裂体 cannot be revived generically: 念动力反射者 74644400 ②, 黑翼的祭司 79519259 ② and 爆裂狙击手 39015 ① may only special summon listing monsters without summon restrictions (爆裂兽 3431737, 爆裂狙击手 39015, 爆裂巫妖 86098176, 爆裂音速战士 18711696)
- 爆裂模式 80280737 is a Trap: it needs to be set the previous turn or set-and-activated same turn via 黑翼的祭司 79519259 ① or 爆裂模式零型 88332693 ② — never try to play it straight from hand
- 念动力反射者 74644400 ② Level announcement: 爆裂兽 3431737 revives at Level 4, raise +3 for 黑翼的祭司 79519259 (Level 8); raising +4 makes Level 9 and needs a Level 9 target — check the Synchro target before announcing
- 决斗进化-爆裂区域 91002901 ③ is once per turn with a 2000 LP cost and its flag is consumed by the first Extra Deck release — a second 爆裂模式 80280737 that turn must release a Synchro from the field
- 爆裂模式零型 88332693 ① summons from the HAND: search the boss into hand (黑翼的祭司 79519259 ②, 决斗进化-爆裂区域 91002901 ①) before relying on it
- Sequence the locks: after 爆裂狙击手 39015 ① or 黑翼的祭司 79519259 ②, only Synchro may come from the Extra Deck — Xyz/Link first
- 爆裂爆发 93469007 burns BOTH players (Level ×200 per released /爆裂体): only a finisher with an LP lead
- 爆裂反击 76407432 needs a face-up /爆裂体 at activation — activate it before releasing that /爆裂体 for 爆裂模式 80280737 or 爆裂再起 74431740
- 星尘龙/爆裂体 61257789 ① releases itself as cost and only returns in the End Phase — after negating, it is not a field body for the rest of that turn, and ③ revives 星尘龙 44508094 only on destruction, not on release
- 深红剑士/爆裂体 50604072 lock hits only monsters special summoned from the Extra Deck — /爆裂体 special summoned by 爆裂模式 80280737 from the deck are unaffected
