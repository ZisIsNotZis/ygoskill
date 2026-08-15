---
name: ryzeal-experience
description: 雷火沸动 (Ryzeal) deck experience: mechanics, one-card combo, extenders, halt points
---
# 雷火沸动 (Ryzeal) Deck Experience

- **Deck Identity**

- Main deck engine monsters are all Level 4: 内燃雷火沸动机 8633261, 外燃雷火沸动机 34022970, 剑式阴极雷火沸动机 35844557, 节式阳极雷火沸动机 72238166, 星式热气雷火沸动机 84433129, 掌式永磁雷火沸动机 61116514
- Attribute and race split into two search groups: 内燃/外燃/星式热气 are LIGHT Pyro, 剑式阴极/节式阳极/掌式永磁 are FIRE Thunder
- Xyz core: 雷火沸动油电双动机 7511613 (generic Rank 4, the mid-line search piece) and 雷火沸动死旋爆震机 34909328 (the 3000 ATK boss)
- Spell line: field spell 雷火沸动交界机 6798031, quick-play 雷火沸动机插电 60394026
- Trap line: 雷火沸动霍尔洞推进器 33787730, 雷火沸动质量驱动器 53276089
- Sample pure build plays 内燃×3 外燃×3 剑式阴极×3 节式阳极×1 plus 篝火 85106525 and 小世界现象 89558743 as consistency, does not main 星式热气 or 掌式永磁
- This server has no 极帝/始祖/迪乌阿/奥拓 cards in the database; the boss of record is 雷火沸动死旋爆震机 34909328

- **Core Mechanic: Level 4 spam into Rank 4 Xyz**

- Every main deck 雷火沸动 monster has a once-per-turn self special summon clause from hand, verified in scripts as EFFECT_SPSUMMON_PROC
- Each self-summon method costs something and then locks you to Rank 4 Xyz from the Extra Deck for the rest of the turn (EFFECT_CANNOT_SPECIAL_SUMMON non-Rank-4 Xyz), so all lines end on Rank 4 monsters
- 内燃 8633261 costs 1 card from hand or field to the graveyard; its second effect only triggers on Normal Summon and special summons any 雷火沸动 from deck except itself, making it the one-card starter
- 外燃 34022970 costs 1 Xyz from the Extra Deck to the graveyard, which sets up the graveyard for 插电 60394026 later
- 剑式阴极 35844557 costs nothing but needs a 雷火沸动 on field or in graveyard; its summon searches a LIGHT Pyro monster (the 内燃/外燃/星式热气 group)
- 节式阳极 72238166 needs an Xyz on field or in graveyard; its ignition effect sends 1 card to the graveyard to revive a 雷火沸动 from the graveyard in defense with effects negated
- 星式热气 84433129 costs 1 Xyz material detached from your field; its summon sets any 雷火沸动 spell or trap from deck
- 掌式永磁 61116514 cannot be normal summoned, returns a 雷火沸动 from hand or graveyard to deck or extra to summon itself, and keeps the Rank 4 Xyz lock while face-up on field
- 外燃 34022970 searches a Thunder FIRE monster when summoned, 剑式阴极 35844557 searches a LIGHT Pyro monster when summoned, so the two groups chain-search into each other

- **One-Card Combo: 内燃雷火沸动机 8633261**

- Step 1: normal summon 内燃 8633261, activate its second effect to special summon 外燃 34022970 from deck
- Step 2: 外燃 34022970 summon effect adds 剑式阴极 35844557 (Thunder FIRE) from deck to hand
- Step 3: Xyz both into 雷火沸动油电双动机 7511613, its summon effect attaches 1 雷火沸动 monster from the graveyard as material
- Step 4: activate 油电双动机 7511613 ignition effect, detach 2 materials to add 2 different 雷火沸动 cards from deck to hand, pick 星式热气 84433129 and 雷火沸动交界机 6798031 or 插电 60394026
- Step 5: special summon 剑式阴极 35844557 from hand, its summon effect adds another LIGHT Pyro 雷火沸动 (内燃 8633261 or 外燃 34022970) from deck
- Step 6: special summon 星式热气 84433129 by detaching 1 material from 油电双动机 7511613, its summon effect sets 雷火沸动交界机 6798031 or 插电 60394026 from deck
- Step 7: Xyz 剑式阴极 35844557 and 星式热气 84433129 into 雷火沸动死旋爆震机 34909328, its summon effect attaches 1 monster from the graveyard as material
- 篝火 85106525 is a one-card line by itself: it searches a Level 4 or lower Pyro monster, which is 内燃 8633261 or 外燃 34022970, then follow the same line

- **End Field One-Card**

- 雷火沸动死旋爆震机 34909328 at 3000 ATK with 2 to 3 materials, quick effect destroys any card on field when the opponent activates a card effect, and once per turn can detach 1 material to replace the destruction of your Xyz monsters
- 雷火沸动油电双动机 7511613 at 2500 ATK boosting your monsters by 100 ATK per material and dropping the opponent's by 100 per material
- One set 雷火沸动 spell or trap from 星式热气 84433129, and 3 to 4 extra cards in hand from the searches
- Halt point: Ash Blossom 14558127 on 内燃 8633261 second effect stops the whole line, Ash on 外燃 34022970 or 油电双动机 7511613 search cuts hand advantage but 死旋爆震机 34909328 is usually still reachable

- **Extenders**

- 篝火 85106525 searches 内燃 8633261, 外燃 34022970 or 星式热气 84433129 (Pyro only, it cannot grab the Thunder FIRE monsters)
- 小世界现象 89558743 bridges a hand monster into 内燃 8633261 or 外燃 34022970 by sharing exactly one stat line
- 三战之号 35269904 sets a normal spell or trap from deck, including 雷火沸动交界机 6798031, 插电 60394026 or 雷火沸动霍尔洞推进器 33787730, when the opponent activated a monster effect
- 插电 60394026 revives any 雷火沸动 or Xyz monster from the graveyard or banished zone and can attach 1 雷火沸动 from deck to a face-up Rank 4 Xyz, then locks your attacks to Rank 4 Xyz for the turn
- 节式阳极 72238166 revives a 雷火沸动 from the graveyard in defense negated, giving a second body for another Rank 4 Xyz
- 雷火沸动霍尔洞推进器 33787730 destroys up to as many face-up opponent cards as the number of 雷火沸动 Xyz you control, and from the graveyard banishes itself to Xyz summon using your monsters including a 雷火沸动
- 雷火沸动质量驱动器 53276089 gives your 雷火沸动 monsters 1000 ATK for the turn and attaches itself to a Rank 4 Xyz as material
- Extra deck toolbox for the Rank 4 slot: 重铠装-希望鳍条枪兵 1269512 (overlay finisher), 深渊的潜伏者 21044178, 鸟铳士 卡斯泰尔 82633039, No.41 泥睡魔兽 睡梦貘 90590303, 励辉士 入魔蝇王 46772449, No.60 刻不知之杜加雷斯 66011101, 龙卷龙 6983839
- 天霆号 阿宙斯 90448279 and 灾厄之星 提·丰 93039339 exist in the sample extra but cannot be summoned in the same turn as any of the self-summon methods because of the Rank 4 Xyz lock; overlay them on a later turn

- **Halt Points**

- Ash Blossom 14558127 on 内燃 8633261 deck special summon leaves you with only the normal summoned 内燃 and no engine
- Ash Blossom 14558127 on 外燃 34022970 search or 油电双动机 7511613 search stops the hand advantage engine
- 无限泡影 10045474 or 效果遮蒙者 97268402 on 内燃 8633261 before its summon trigger resolves kills the line
- 抹杀之指名者 65681983 or 墓穴的指名者 24224830 on 内燃 8633261 or 外燃 34022970 prevents the deck and extra deck summons
- 原始生命态 尼比鲁 27204311 hits after the fifth summon of the full combo, 增殖的G 23434538 draws the opponent a card per summon, 小丑与锁鸟 94145021 stops every search
- 次元障壁 83326048 declaring Xyz is a full stop, and the deck itself can side it

- **Mirror Match: 雷火沸动 vs 雷火沸动**

- Whoever resolves 内燃 8633261 into 死旋爆震机 34909328 first controls the duel because the boss quick destroys on any opponent activation
- 雷火沸动交界机 6798031 negate effect is once per turn, save the material detach for the opponent 内燃 8633261 summon trigger or 油电双动机 7511613 search
- 雷火沸动霍尔洞推进器 33787730 is a blowout in the mirror, it destroys one face-up opponent card per 雷火沸动 Xyz you control
- 深渊的潜伏者 21044178 shuts down the graveyard revival plays of 插电 60394026 and 节式阳极 72238166
- 雷火沸动交界机 6798031 first effect prevents Xyz summoning a monster with the same name as one already on your field, so no double 油电双动机 7511613 or double 死旋爆震机 34909328 while it is face-up

- **Playing Under 增殖的G and 欢聚友伴**

- Do not play the full combo while 增殖的G 23434538 or the opponent's 欢聚友伴·茸茸长尾山雀 42141493 is active, every special summon hands the opponent a draw
- Compromise line under G: normal summon 内燃 8633261, special summon 外燃 34022970, Xyz 油电双动机 7511613, detach 2 to search 2, end there at three summons
- If a 死旋爆震机 34909328 must come down, make it from 内燃 8633261 and 剑式阴极 35844557 only, keeping the summon count at four
- 墓穴的指名者 24224830 and 抹杀之指名者 65681983 answer the opponent hand traps before extending

- **Common Mistakes**

- Always normal summon 内燃 8633261, its deck special summon effect only triggers on normal summon, using its self-summon method wastes the starter
- The self-summon methods lock you to Rank 4 Xyz for the turn, never plan 天霆号 阿宙斯 90448279 or 灾厄之星 提·丰 93039339 in the same turn
- 油电双动机 7511613 search needs 2 materials detached, do not spend its materials on 星式热气 84433129 before searching
- 星式热气 84433129 sets a card from deck, a set trap cannot activate the same turn, prefer setting 雷火沸动交界机 6798031 or 插电 60394026 for later
- 外燃 34022970 search condition fails if any face-up non-Level-4 or non-Rank-4 monster exists on your field, do not summon a Link or higher-level monster first
- 篝火 85106525 searches Pyro monsters only, it can never grab 剑式阴极 35844557 or 节式阳极 72238166
- 剑式阴极 35844557 searches LIGHT Pyro and 外燃 34022970 searches Thunder FIRE, do not expect them to search each other's group directly
- 掌式永磁 61116514 keeps the Rank 4 Xyz lock active while face-up on the field, do not keep it around if a non-Rank-4 Xyz play is planned
- 雷火沸动质量驱动器 53276089 graveyard effect triggers when it is sent from outside the field, discarding it as cost banishes 1 opponent graveyard card
