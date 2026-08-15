---
name: numeron-experience
description: 源数 (Numeron) deck experience: one-card OTK engine, gate doubling, extenders, halt points
---
# 源数 (Numeron) Deck Experience

- **Deck Identity**

- Pure go-second OTK deck, archetype setcode 0x14a, wins in the Battle Phase of turn two or not at all
- Core cards: field spell 源数网络 41418852, its copy target 源数直系 77402960, four Rank 1 Xyz gates No.1 源数之门-壹 15232745, No.2 源数之门-贰 42230449, No.3 源数之门-叁 78625448, No.4 源数之门-肆 4019153
- Finisher enabler 限制解除 23171610 makes the gates 2000 ATK each for a clean 8000 direct-attack OTK
- Backup beatdown: 时械神 桑达伊恩 33015627 can Normal Summon without tribute when only the opponent has monsters, is indestructible, and burns 2000 after battling
- Typical pure build runs 3 源数网络 41418852, 2 to 3 源数直系 77402960, 2 to 3 of each gate, 3 限制解除 23171610, 3 惑星探查车 97526666, plus board breakers 黑洞 53129443, 雷击 12580477, 闪电风暴 14532163, 颉颃胜负 15693423, 禁忌的一滴 24299458 and hand traps 增殖的G 23434538, 灰流丽 14558127, 原始生命态 尼比鲁 27204311

- **Core Mechanic: 源数网络 Copy + Gate Doubling**

- 源数网络 41418852 effect one, once per turn: send 1 「源数」Normal Spell from deck to GY and apply that spell's activation effect, so one field spell becomes the whole engine
- The normal copy target is 源数直系 77402960: if 源数网络 41418852 is face-up in the Field Zone and you control no monsters, special summon up to 4 源数之门 Xyz from the Extra Deck, max 1 of each name
- Gates summoned this way have zero Xyz materials, so the doubling effects depend on 源数网络 41418852 effect two: 源数 Xyz monsters may activate their detach-a-material effects without detaching
- Each gate (15232745, 42230449, 78625448, 4019153) is battle-indestructible and, at the end of the Damage Step after battling an opponent's monster, doubles the ATK of all face-up 源数 monsters you control
- The doubling stacks across gates: 1000 to 2000 to 4000 to 8000, so attack order determines total damage and direct attacks never trigger the doubling
- 源数直系 77402960 banishes the gates at the End Phase and restricts you to one more Summon or Special Summon after it resolves, so the deck has no follow-up field

- **One-Card Combo: 源数网络 41418852**

- Starter: only 源数网络 41418852 in hand
- Step 1: activate 源数网络 41418852, effect one sends 源数直系 77402960 from deck to GY and copies its effect
- Step 2: copy effect special summons No.1 源数之门-壹 15232745, No.2 源数之门-贰 42230449, No.3 源数之门-叁 78625448, No.4 源数之门-肆 4019153 from the Extra Deck, all 1000 ATK with no materials
- Step 3: activate 限制解除 23171610, all Machine monsters double to 2000 ATK until the End Phase, the gates being Machine
- Step 4: attack directly with all four gates for 2000 each, total 8000, game over before the End Phase destruction of 限制解除 23171610 or the banish of 源数直系 77402960 matters
- Without 限制解除 23171610 the same four gates only deal 4000 direct, so the OTK needs either the Limiter or a monster to battle into

- **End Field**

- After a successful kill there is no field: 源数直系 77402960 banishes the gates at the End Phase, so the game ends in the same Battle Phase
- If the opponent survives, you pass with an empty field and likely lose next turn, the deck wins or dies on the spot
- Stall fallbacks when the kill fails: 时械神 桑达伊恩 33015627 as an indestructible 4000 ATK blocker that returns to deck at your Standby Phase, 试胆竞速 67616300 reducing all damage to 0 for the player with fewer LP, 源数之壁 42352091 special summoning itself after battle damage and ending the Battle Phase

- **Extenders: Battle Doubling and Rank-Up**

- Battle-doubling line against one monster: give the opponent a Kaiju like 海龟坏兽 加美西耶勒 55063751 or 怪粉坏兽 加达拉 36956512, or 熔岩魔神 102380, then gates attack into it, each gate doubling all gates, reaching 8000 plus with the last direct attacks
- 所有者的刻印 9720537 returns the Kaiju to your field, which can clear the opponent's monster for direct attacks, but remember 源数直系 77402960 needs your field empty when it resolves
- 升阶魔法-源数之力 48333324 ranks No.1 源数之门-壹 15232745 into 混沌No.1 混沌源数门-空 79747096 and negates all other face-up cards on the field, while the CNo.1's own Xyz Summon trigger banishes every monster on the field
- 混沌No.1 混沌源数门-空 79747096, if banished, special summons itself next Standby and burns the opponent the total ATK of banished Xyz monsters while 源数网络 41418852 is face-up
- 源数混沌仪式 41850466, if your face-up 混沌No.1 混沌源数门-空 79747096 was destroyed by a monster effect that turn, summons 混沌No.1000 梦幻虚神 原数天灵 89477759 at 10000 ATK using 1 源数网络 41418852 and 4 「No.」 Xyz as material
- 源数风暴 20936251, while 混沌No.1000 梦幻虚神 原数天灵 89477759 is on field, destroys all opponent Spell and Trap cards and burns 1000
- No.100 源数龙 57314798 Xyz summons on two same-name same-rank 「No.」 Xyz and gains ATK equal to the total ranks of all Xyz on the field times 1000, and revives from GY on a direct attack if your hand and field are empty
- Searchers for the engine: 惑星探查车 97526666 tributes itself to add any Field Spell, 星球改造 73628505 adds any Field Spell, 皮里·雷斯地图 33907039 adds a 0 ATK monster namely 源数之壁 42352091, 试胆竞速 67616300 and 舞台旋转 73468603 dig into field spells
- 源数之壁 42352091 effect one, a Quick Effect usable on the opponent's turn while you control no other cards, sends itself to GY to activate 源数网络 41418852 from hand or deck
- 希望之记忆 84731222 draws one card for each 「No.」 Xyz monster type you control, up to four after 源数直系 77402960 resolves
- 团结之力 56747793 equips +800 per face-up monster, pushing an equipped gate to 4200 when the four gates are on field

- **Halt Points**

- Destroy or negate 源数网络 41418852 before the Battle Phase: without its effect two the material-less gates cannot activate their doubling, and without it face-up 源数直系 77402960 cannot even resolve
- Ghost Ogre style field-spell removal in response to 源数网络 41418852 effect one, and generic field spell hate like 双龙卷 43898403 or 舞台旋转 73468603, stops the entire engine
- 增殖的G 23434538 punishes the four simultaneous special summons of 源数直系 77402960 with four draws, answer it with 墓穴的指名者 24224830, 抹杀之指名者 65681983, or 次元吸引者 91800273
- 原始生命态 尼比鲁 27204311 triggers on the fifth special summon, live only when the combo added extra summons such as a Kaiju before the four gates, and wipes the board before the attack
- 无限泡影 10045474 or 效果遮蒙者 97268402 negating a gate stops its doubling contribution, and 王宫的敕命 style spell locks kill the deck entirely
- 源数直系 77402960 requires both 源数网络 41418852 face-up in the Field Zone and zero monsters you control, so any monster you keep blocks the OTK

- **Mirror Match: 源数 vs 源数**

- Whoever resolves 源数直系 77402960 with 限制解除 23171610 first wins, since gates are battle-indestructible and direct attacks deal the full 8000
- Hand trap wars decide it: 灰流丽 14558127 does not stop the 源数网络 41418852 copy because the deck send is a cost and the copy summons from the Extra Deck, but 增殖的G 23434538 and 原始生命态 尼比鲁 27204311 punish the summon burst
- 墓穴的指名者 24224830 and 抹杀之指名者 65681983 are the key disruptors to protect your own 源数直系 77402960 line from the opponent's hand traps
- 混沌No.1 混沌源数门-空 79747096 banish-all is the board answer in the mirror, clearing both sides' gates before the kill turn

- **Common Mistakes**

- Do not summon any monster before 源数直系 77402960, its activation condition requires your field to be monster-free
- Do not activate 源数直系 77402960 without 源数网络 41418852 face-up in the Field Zone, and do not let 源数网络 41418852 leave the field mid-combo or the material-less gates lose their doubling
- Do not attack with all gates directly when the opponent has a monster: battle into it first to double every gate, then direct attack with the boosted remainder
- Attack order matters because each battle doubles all gates, order the weakest attacks first so the doubling chain reaches 4000 to 8000 before the last gate swings
- Remember 源数直系 77402960 leaves only one Summon or Special Summon afterwards, so do not plan a second summon line in the same turn
- Remember the gates are banished at the End Phase by 源数直系 77402960, never keep them for defense and never expect them next turn
- 限制解除 23171610 destroys the Machines at the End Phase, irrelevant after the kill but do not rely on the gates surviving the turn without the kill
- 试胆竞速 67616300 protects only the player with fewer LP, so it shields the opponent when you are ahead, activate it only when behind or use it to draw
- 皮里·雷斯地图 33907039 halves your LP and locks the searched monster's effects unless you summon it, plan the 源数之壁 42352091 search carefully
- Kaiju tribute effects must resolve before 源数直系 77402960, giving the opponent exactly one monster to battle into for the doubling chain
