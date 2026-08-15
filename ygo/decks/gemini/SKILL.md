---
name: gemini-experience
description: 二重 (Gemini) deck experience: Chemicritter engine, 再1次召唤 dual-summon mechanic, 碳素蟹 combo, halt points
---
# 二重 (Gemini) Deck Experience

- **Deck Identity**

- True identity: the Gemini monster-type engine (TYPE_DUAL), not 二重身 (Doppelwarrior 53855409) and not 沉默剑士 (Silent Swordsman 15180041) — no 二重 deck in this collection plays either; the coherent build is the 化合 (Chemicritter, setcode 0xeb) + 真化护法 (Evoltextor) + 凤凰剑圣 (Gearfried) engine
- Core monsters: 化合兽 碳素蟹 81599449, 化合兽 氧素牛 18993198, 化合兽 氢素鹰 55100740, 进化合兽 二氧鬼神 44088292, 进化合兽 水蛇龙 80476891, 真化护法 主教 16146511, 真化护法 骑士 96872283, 重起士道-金骑士 72305034, 凤凰剑圣 基亚·弗里德 69488544, 暗黑暴风龙 57662975
- Bosses: 超化合兽 甲醇双面兽 38026562 (Rank 8 Xyz), 神威凤凰剑圣 基亚·弗里德 22091647
- Support: 化合电界 65959844, 超二重召唤 95750695 (this DB's name for 再战 Supervise), 二重烧蚀 80758812, 二量合成 90965652, 完全燃烧 25669282, 二重召唤 43422537 (Double Summon), 抵价购物 38120068, 增援 32807846, 墓穴的指名者 24224830
- 2025 hybrid builds (250426 folders) add a 魔瞳 OTK package (撕裂时间的魔瞳 19403423, 讴歌死亡的魔瞳 81756619, 瞳之魔女 梦根娜 29439831), the Primite 原石 engine (原石龙 帝王黄玉龙 81418467, 原石的皇脉 56506740, 原石融合 99161253 to 始祖之龙王 53466722), and Horus Level 8 bodies (荷鲁斯的荣光-伊姆塞特 84941194, 王之棺 16528181)

- **Core Mechanic: 再1次召唤 (Gemini Summon)**

- A Gemini monster is a Normal monster while face-up on the field or in the Graveyard (aux.EnableDualAttribute adds TYPE_NORMAL in MZONE+GRAVE and removes TYPE_EFFECT); the second Normal Summon of the same copy is the 再1次召唤 that turns it into a DualState effect monster
- DualState is a card state, not a lingering effect: it is lost whenever the monster leaves the field, so a bounced or re-summoned Gemini must be re-summoned again
- The normal-summon budget is the whole engine's choke point: one normal summon plus one extra Gemini summon from 化合电界 65959844, or the summon limit of 2 from 二重召唤 43422537 (this card's text does not mention 二重怪兽, so 金骑士 72305034 cannot search it)
- 化合电界 65959844 (Field Spell) does three jobs: no tribute for Level 5+ Gemini summons, one extra Gemini summon per turn, and an ignition that banishes your own DualState Gemini until the opponent's End Phase to destroy one opponent card
- 超二重召唤 95750695 (Equip Spell) grants DualState for free without a summon (EFFECT_DUAL_STATUS) and revives one Normal monster from your Graveyard when the equip itself leaves the field face-up — since Geminis are Normal in the Graveyard, it recurs your own engine
- 二重烧蚀 80758812 (Continuous Trap) and 完全燃烧 25669282 skip the second summon entirely: they Special Summon Geminis already in DualState
- 进化合兽 二氧鬼神 44088292 in DualState gives every Gemini summon EFFECT_CANNOT_DISABLE_SUMMON — resolve it first and the whole summon line cannot be negated

- **One-Card Combo: 碳素蟹 81599449**

- One card 碳素蟹 81599449 plus one summon-enabler 化合电界 65959844 or 二重召唤 43422537 (2 cards total; 碳素蟹 cannot re-summon itself on turn one)
- Step 1: normal summon 碳素蟹 81599449 as a Normal monster
- Step 2: use the extra Gemini summon to 再1次召唤 it into DualState
- Step 3: activate its effect: send 进化合兽 二氧鬼神 44088292 from deck to Graveyard, then add 真化护法 主教 16146511 from deck to hand
- Step 4: with 二重召唤 43422537's second summon, gemini-summon 主教 16146511; its summon trigger revives the milled 二氧鬼神 44088292 from the Graveyard
- Result: 主教 16146511 plus 二氧鬼神 44088292 on board, Graveyard loaded, hand plus one — the full 甲醇双面兽 38026562 setup for next turn
- Two-card full combo: DualState 氧素牛 18993198, then its effect Special Summons 凤凰剑圣 基亚·弗里德 69488544 from hand and makes every face-up Gemini Level 8, overlay both into 超化合兽 甲醇双面兽 38026562, which revives a Gemini from the Graveyard on summon

- **End Field**

- 超化合兽 甲醇双面兽 38026562: while it has material the opponent cannot target or attack your Gemini monsters, and every Gemini normal summon by either player detaches one material to make the opponent send one card from hand or field to the Graveyard
- 进化合兽 二氧鬼神 44088292 (2800 ATK) or 真化护法 主教 16146511 as a second body; 主教 16146511 loops revivals every time it is summoned
- Backrow: set 二重烧蚀 80758812 or 神之宣告 41420027, 超二重召唤 95750695 equipped to a monster, 超自然警戒区域 16165939
- Finisher: 神威凤凰剑圣 基亚·弗里德 22091647 (Special Summons itself by banishing an Equip Spell, negates monster effect activations by sending an equip, equips monsters to itself for 500 ATK), or 二量合成 90965652 from the Graveyard to zero one of your monsters and pump 甲醇双面兽 38026562 past 3000
- Link toolbox in the 210717 build: 圣骑士的追想 伊索德 59934749, I：P百变莱娜 65741786, 访问码语者 86066372, 宵星之机神 丁吉尔苏 93854893, 闭锁世界的冥神 98127546

- **Extenders**

- 真化护法 主教 16146511: on every Normal or Special summon while in DualState, revive one FIRE Warrior or Gemini from your Graveyard (not itself); searchable by 增援 32807846 (Level 4 Warrior)
- 重起士道-金骑士 72305034: on summon, add any Spell or Trap whose text mentions 二重怪兽 — 超二重召唤 95750695, 二重烧蚀 80758812, 二量合成 90965652, 完全燃烧 25669282 or 化合电界 65959844; it also becomes Machine and gains 500 ATK
- 真化护法 骑士 96872283: send one face-up Equip you control to the Graveyard to destroy one opponent card — removal that also feeds 超二重召唤 95750695 and the Gearfried bosses
- 氢素鹰 55100740: discard one card, revive one Gemini from the Graveyard in Defense — grave recursion on demand
- 二重烧蚀 80758812: quick effect in Main Phase, discard one: Special Summon any Gemini from deck as DualState, or tribute one Gemini to Special Summon one FIRE Warrior from hand or deck (destroy one card if the tribute was DualState) — this is how 凤凰剑圣 基亚·弗里德 69488544 and 神威凤凰剑圣 22091647 come out
- 二量合成 90965652: search 化合电界 65959844, or 完全燃烧 25669282 plus one 化合兽 monster; in the Graveyard, banish itself to make one of your monsters 0 ATK and give its base ATK to another (one of the two targets must be DualState)
- 完全燃烧 25669282: banish one face-up 化合兽 you control, Special Summon two different 化合兽 from deck; from the Graveyard during a direct attack, revive one of your banished Geminis as DualState
- 抵价购物 38120068: discard a Level 8 (二氧鬼神 44088292, 水蛇龙 80476891, 凤凰剑圣 69488544, 暗黑暴风龙 57662975) to draw two
- 凤凰剑圣 基亚·弗里德 69488544 (2800 ATK Level 8): while DualState, when the opponent activates a Spell, Special Summon one Gemini from your Graveyard; send an Equip to negate a Spell or Trap activation that targeted a monster

- **Halt Points**

- 灰流丽 14558127 on 碳素蟹 81599449's mill-search kills the hand engine, and on 完全燃烧 25669282's deck summons blocks the double Special Summon
- 效果遮蒙者 or 无限泡影 on 真化护法 主教 16146511's revival trigger stops recursion (the revive is from the Graveyard, so 灰流丽 14558127 cannot hit it)
- Negate 氧素牛 18993198 before its effect resolves and the level-sync fails, so no 甲醇双面兽 38026562
- 增殖的G 23434538: the deck Special Summons repeatedly (主教 16146511 revives, 氧素牛 18993198, 二重烧蚀 80758812 deck summon, 完全燃烧 25669282) — stop at 主教 when G is up, do not extend into the deck summons
- 墓穴的指名者 24224830 protects the 碳素蟹 81599449 mill and the 主教 16146511 and 甲醇双面兽 38026562 revivals; hold it for hand traps aimed at those plays
- The modern variant cannot activate hand monster effects while 撕裂时间的魔瞳 19403423 is active — 灰流丽 14558127 and 增殖的G 23434538 are dead in hand for that duel

- **Mirror Match: 二重 vs 二重**

- 超化合兽 甲醇双面兽 38026562's detach effect triggers on any Gemini normal summon, including the opponent's — their 再1次召唤 pays you a discard, so summoning your Geminis while their 甲醇双面兽 38026562 is up is a losing trade
- The first 化合电界 65959844 pop decides the board: it removes the opponent's DualState beater and their extra-summon engine at once
- 进化合兽 二氧鬼神 44088292 cancels summon-negation in both directions, so the duel becomes a race of who resolves 氧素牛 18993198's level-sync into 甲醇双面兽 38026562 first
- In the mirror, 二量合成 90965652 only affects your own monsters — never choose your own key piece for the 0 ATK side by accident; use it to push the OTK instead

- **Common Mistakes**

- Count the summon budget before the turn starts: 化合电界 65959844's extra Gemini summon and 二重召唤 43422537's limit of 2 are the only ways to 再1次召唤 more than one Gemini per turn
- 超二重召唤 95750695's revival triggers when the equip card leaves the field face-up, not when the equipped monster dies, and it revives a Normal monster — a Gemini is only a Normal monster in the field or Graveyard, never in hand or deck
- Do not banish your own DualState monster with 化合电界 65959844 if it is the material or protection you need this turn — the banish lasts until the opponent's End Phase
- 碳素蟹 81599449 needs a second Gemini in deck after the mill: send 二氧鬼神 44088292 first so 主教 16146511 can revive it the same turn
- 二量合成 90965652's Graveyard pump needs one DualState monster among the two targets and only touches your own field
- 氧素牛 18993198's level sync applies to all your face-up Geminis including itself — Special Summon the Level 8 before the overlay or the levels lock
- 增援 32807846 only searches Level 4 or lower Warriors (主教 16146511, 骑士 96872283, 金骑士 72305034) — it cannot search the Chemicritters (Aqua, Beast, Winged Beast, Fiend, Fish)
- 完全燃烧 25669282's Graveyard revival cannot be used the turn it was sent to the Graveyard
- 二重烧蚀 80758812 is a Trap: it cannot activate the turn it is set, and its hand-discard cost is paid before you know whether the summon succeeds
- A Gemini that leaves the field reverts to a Normal monster and loses DualState; it must be 再1次召唤 again to regain its effects
