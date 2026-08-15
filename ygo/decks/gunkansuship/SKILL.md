---
name: gunkansuship-experience
description: 军贯 (Gunkan Suship) deck experience: mechanics, one-card combo, extenders, halt points
---
# 军贯 (Gunkan Suship) Deck Experience

- **Deck Identity**

- 军贯 (OCG 軍貫, TCG Gunkan Suship, 简中 舍利军贯): WATER Aqua sushi-battleship Xyz archetype that plays Rank 4 and Rank 5 ships, all 11 cards share setcode 0x166 in cards.cdb and scripts
- Main deck monsters: 舍利军贯 24639891 (Level 4 Normal, 2000 ATK, the "rice" key), 赤舍利军贯 63748694, 银鱼军贯 78362751, 鲑鱼子军贯 61027400, 海胆军贯 42377643
- Extra deck ships: 空母军贯-银鱼级特务舰 21293424 (Rank 4), 无畏军贯-鲑鱼子级一号舰 75215744 (Rank 4), 超无畏军贯-海胆级二号舰 94798725 (Rank 5)
- Spell and Trap support: 军贯处『海栈』 62200831 (Field Spell), 推荐捏军贯 83008724 (Continuous Spell), 随兴捏军贯 24393683 (Normal Trap)
- 舍利军贯 24639891 is the engine: a strong 2000 ATK Normal Summon that every fish monster special summons itself off of, and ships pay out when 舍利军贯 is among their materials
- Modern builds use 军贯 as a Rank 4/5 toolbox, verified in the deckbase (deck/241026舍利军贯雷火沸动原石的斩机): 斩机 Mathmech, 雷火沸动 Goblin Biker, 原石 Primite, 天霆号阿宙斯 90448279, 未来No.0 未来皇 霍普 ladder

- **Core Mechanic: 舍利军贯 Material Bonuses**

- Each ship triggers on its Xyz Summon and applies effects based on which named monsters were used as materials, verified as EFFECT_MATERIAL_CHECK plus a summon trigger in the scripts
- 空母军贯-银鱼级特务舰 21293424: 舍利军贯 material draws 1, 银鱼军贯 material searches any 军贯 Spell or Trap from deck
- 无畏军贯-鲑鱼子级一号舰 75215744: 舍利军贯 material draws 1, 鲑鱼子军贯 material grants one extra attack this Battle Phase
- 超无畏军贯-海胆级二号舰 94798725: 舍利军贯 material draws 1, 海胆军贯 material grants direct attack
- 赤舍利军贯 63748694 is treated as 舍利军贯 only in hand, deck, field and grave; once it becomes Xyz material its name change stops applying, confirmed by official ruling ygocdb.com/faq/23958 and by the script IsCode checks
- Consequence: ships made with 赤舍利军贯 as material gain no draw, extra attack or direct attack bonus, and 银鱼军贯 78362751's ① cannot activate off a ship whose only 舍利军贯 material is 赤舍利军贯
- 空母's ② protects the whole fleet: while any face-up card exists in a field zone, all your 军贯 monsters summoned from the Extra Deck cannot be destroyed by opponent's effects and gain ATK equal to their original DEF
- The protection comes from 空母 being face-up, not from the field spell itself, and any face-up Field Spell on either side of the field satisfies the condition
- 超无畏's ② is a Quick Effect once per turn, in your Main Phase or the opponent's Battle Phase, negating the effects of up to N face-up cards the opponent controls where N equals your face-up 军贯 Xyz monsters
- Each ship's ① is once per turn per name, shared across copies, and the overlay-style summons from 赤舍利军贯 63748694 and the field spell count as Xyz Summons so they also trigger the ships

- **One-Card Combo: 赤舍利军贯 Engine Line**

- There is no true one-card starter: every line needs 舍利军贯 24639891 (or a 赤舍利军贯 63748694, whose name is 舍利军贯 in hand) plus one fish
- Starter: 赤舍利军贯 63748694 and any card treated as 舍利军贯 24639891 in hand, a second 赤舍利军贯 also works as the key
- Step 1: reveal the 舍利军贯 to activate 赤舍利军贯's ②, the reveal is the cost and the card stays in hand
- Step 2: 赤舍利军贯 special summons itself from hand
- Step 3: special summon 银鱼军贯 78362751 from deck with its effects negated
- Step 4: Xyz Summon 空母军贯-银鱼级特务舰 21293424 over 赤舍利军贯 and 银鱼军贯
- Step 5: 空母's ① resolves, the 银鱼军贯 material searches a 军贯 Spell or Trap and the 赤舍利军贯 material grants no draw
- Step 6: search 军贯处『海栈』 62200831 or 推荐捏军贯 83008724 and activate it to establish the board
- Aggro variant: special summon 鲑鱼子军贯 61027400 from deck instead and Xyz Summon 无畏军贯-鲑鱼子级一号舰 75215744, which attacks twice
- Halt point: 灰流丽 14558127 on 赤舍利军贯's ② negates the whole line because the deck special summon happens in the same chain

- **One-Card Combo: 海胆军贯 Rank 5 Line**

- Starter: 海胆军贯 42377643 plus 舍利军贯 24639891 in hand
- Step 1: 海胆军贯's ① reveals the 舍利军贯, special summons itself as Level 5, then special summons the revealed 舍利军贯 as Level 4
- Step 2: 海胆军贯's ② targets the 舍利军贯, changes its Level to 5, then searches another 舍利军贯 24639891 from deck to hand
- Step 3: overlay both Level 5 monsters into 超无畏军贯-海胆级二号舰 94798725 (Rank 5, 2900 ATK)
- Step 4: 超无畏's ① resolves: the 舍利军贯 material draws 1 and the 海胆军贯 material grants direct attack
- Step 5: use 超无畏's ② in your Main Phase to negate one face-up opponent card
- Halt point: 灰流丽 14558127 on 海胆军贯's ①, or 效果遮蒙者 and 无限泡影 10045474 on the ② level change which kills the Rank 5

- **End Field**

- Engine card plus key: 空母军贯-银鱼级特务舰 21293424 with 军贯处『海栈』 62200831 face-up, one search spent and the deck stacked
- Full field: 超无畏军贯-海胆级二号舰 94798725 (2900, direct attack, negates up to two face-up cards with two ships out) plus 无畏军贯-鲑鱼子级一号舰 75215744 (2200, two attacks, destroys one card whenever any of your 军贯 Xyz deals battle damage)
- 无畏's destroy is cross-ship: 超无畏's direct attack also triggers it, so swing with the direct attacker first
- With 军贯处 or any face-up Field Spell the ships reach 2450 / 2500 / 3400 ATK, which is 2200+250, 2200+300 and 2900+500
- Under 增殖的G 23434538 settle for one ship only, 空母 is the value pick and 无畏 the damage pick

- **Extenders**

- 银鱼军贯 78362751: ① special summons itself when a 舍利军贯 is face-up on field or inside a ship's materials; ② special summons another 军贯 monster from hand, then stacks any number of 舍利军贯 24639891 from deck or grave on top of the deck in any order
- 银鱼's ② stacking can also use 赤舍利军贯 63748694 because its name is 舍利军贯 in deck and grave
- 鲑鱼子军贯 61027400: ① inherent special summon from hand while a 舍利军贯 is face-up on field, no chain and no hand cost; ② reveals the top 3 cards of the deck, adds or special summons one 舍利军贯 24639891 among them, shuffles the rest back
- 军贯处『海栈』 62200831: ① once per turn, when you Normal or Special Summon a 军贯 monster even during the Damage Step, place one 军贯 card from deck on top; ② when the opponent sends your 军贯 Xyz to the grave they pay LP equal to its DEF, then you may special summon 舍利军贯 24639891 from hand and overlay a 军贯 Xyz on top of it
- 随兴捏军贯 24393683 (Normal Trap): ① reveals 3 军贯 monsters from deck and the opponent picks one to add to your hand, but if a 舍利军贯 24639891 is among the three you pick instead; ② banishes itself from the grave to shuffle 3 军贯 monsters from grave into the deck and draw 1, not on the turn it went to the grave
- 推荐捏军贯 83008724 (Continuous Spell): once per turn reveal 舍利军贯 24639891 in hand, place a counter and reveal a 军贯 Xyz, then the opponent declares one of 鲑鱼子军贯 61027400, 银鱼军贯 78362751 or 海胆军贯 42377643 and you add it from deck, but if it is absent the spell returns to the deck
- The 推荐捏 search is soft: the script c83008724.lua lets the opponent name any of the three fish, unlike the OCG text which restricts to the fish listed on the revealed ship, so expect the opponent to pick the fish that does not fit your current plan
- 赤舍利军贯 63748694 doubles as a second 舍利军贯 in hand, so 赤舍利 plus 赤舍利 is a valid engine pair
- Rank 4 splash package from the deckbase: 斩机 圆武 36521307 and 斩机 径武 17946349 into 块斩机算子达朗贝尔 85692042 and 块斩机算子拉普拉斯 88021907, 天霆号阿宙斯 90448279 over spent Rank 4s, 未来No.0 未来皇 霍普 65305468 into 未来No.0 未来龙皇 26973555

- **Halt Points**

- 灰流丽 14558127 is the primary answer, it negates 赤舍利军贯's ②, 海胆军贯's ①, 银鱼军贯's ②, 鲑鱼子军贯's ② and 随兴捏军贯's ① because all special summon or search within the same chain
- 增殖的G 23434538: both engine lines are three special summons, 赤舍利 plus deck fish plus Xyz or 海胆 plus 舍利 plus Xyz, so the opponent draws three if you play through it
- 效果遮蒙者 and 无限泡影 10045474 stop the field-based ignitions: 海胆军贯's ② level change kills the 超无畏 line and 银鱼军贯's ② loses its hand summon and deck stacking
- 尼比鲁 27204311: a two-ship full combo reaches six summons and is 尼比鲁-able after the fifth
- 次元吸引者 91800273 cuts 银鱼军贯's ② grave stacking and 随兴捏军贯's ② grave recursion
- Hand effects are hard to stop: 赤舍利军贯, 海胆军贯 and 银鱼军贯's ① activate from the hand, so 效果遮蒙者 and 无限泡影 cannot touch them and only 灰流丽, 抹杀之指名者 65681983 or 墓穴的指名者 24224830 answer them

- **Mirror Match**

- The 超无畏军贯-海胆级二号舰 94798725 negation war decides the mirror: the first player to resolve it negates the opponent's ships in their Main Phase, blanking 无畏's destroy-on-damage and 空母's fleet protection until the end of the turn
- The field spell destruction immunity protects both players' ships from each other's destruction, so 无畏军贯-鲑鱼子级一号舰 75215744's destroy effect cannot pop a protected 军贯 Xyz and answers must be 超无畏's negation, battle or non-destruction removal
- 空母军贯-银鱼级特务舰 21293424's search decides the grind, grab 随兴捏军贯 24393683 or 军贯处『海栈』 62200831 first
- 军贯处's ② punishes the opponent for sending your ships to the grave, they pay LP equal to the ship's DEF and you may re-overlay a ship from a 舍利军贯 24639891 in hand
- Whoever keeps 空母 face-up keeps their fleet protected, and whoever draws 随兴捏军贯 24393683 first wins the resource race because its reveal-search puts a 舍利军贯 in hand for the next engine activation
- Battle math: 超无畏 at 3400 with a Field Spell attacks directly and 无畏 attacks twice, so the player who resolves both first ends the damage race

- **Common Mistakes**

- Never count on the draw, extra attack or direct attack bonuses from a 赤舍利军贯 material, the name change does not apply while the card is Xyz material per ygocdb.com/faq/23958
- 银鱼军贯's ① cannot activate off a ship whose only 舍利军贯 material is 赤舍利军贯, keep a face-up 舍利军贯 or 赤舍利军贯 on the field instead
- 赤舍利军贯's ② can only build the Rank 4 ships 空母 and 无畏, never 超无畏, because the materials are Level 4 plus the Level 5 海胆军贯; the Rank 5 requires the 海胆 level-change line
- 超无畏's ② is once per turn total, usable in your Main Phase or the opponent's Battle Phase but not in both, and its target cap equals your face-up 军贯 Xyz count so extend the board before activating it
- 随兴捏军贯 is a Trap and must be set a turn ahead, and its ② grave effect cannot be used on the turn it is sent to the grave
- Always reveal 舍利军贯 24639891 when paying 海胆军贯's ① cost, revealing any other 军贯 card sends it to the bottom of the deck permanently
- Order the deck stacks from 军贯处's ① and 银鱼军贯's ② so a 舍利军贯 sits on top, guaranteeing the next 鲑鱼子军贯 mill or normal draw hits it
- 鲑鱼子军贯's ① is an inherent special summon that does not start a chain and cannot be Ashed, only its ② ignition effect can
- Do not assume the field spell alone protects anything: the immunity and ATK boost come from 空母's ②, so 空母 must stay face-up and some field zone card must stay face-up, even the opponent's
- 无畏军贯-鲑鱼子级一号舰's destroy-on-damage needs 无畏 face-up on the field and triggers off any 军贯 Xyz's battle damage, so use 超无畏's direct attack first to get the destroy off
- 推荐捏军贯 is a soft search in this codebase, do not rely on it to fetch a specific fish and do not reveal a ship you cannot or will not summon
