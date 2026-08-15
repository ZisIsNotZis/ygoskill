---
name: evileye-experience
description: 咒眼 (Evil Eye) deck experience: mechanics, one-card combo, extenders, halt points
---
# 咒眼 (Evil Eye) Deck Experience

- **Deck Identity**

- DARK Fiend archetype (setcode 0x129) built around the equip lock 太阴之咒眼 44133040 and two Link monsters: 咒眼之王 泽拉凯尔 17739335 (Link-3, 2600 ATK, arrows top-left/top-right/bottom-right, materials 2 or more 咒眼 monsters only) and 咒眼之女王 戈耳戈涅 29357687 (Link-2, 1900 ATK, arrows top/bottom-right, materials 2 monsters including at least one 咒眼 monster)
- Main deck monsters: 咒眼之死徒 沙利叶 82466274 (Lv4 1600/1400, deck searcher), 咒眼之死徒 美杜莎 18551923 (Lv4 1400/1600, graveyard recycler), self-summoning familiars 咒眼之眷属 巴西利乌斯 81344637 (Lv3 400/2000), 咒眼之眷属 巴西利科克 65351555 (Lv3 1000/2000), 咒眼之眷属 卡托布莱帕斯 45955628 (Lv3 600/1900), plus the token 咒眼之眷属衍生物 7610395
- Spells and traps: equips 太阴之咒眼 44133040 and 蛇发之咒眼 28957126, field 咒眼领阈-错视之城- 70122149, normal spells 眷现之咒眼 7610394, 灾诞之咒眼 8775395, 唤忌之咒眼 17616743, quick-play spell 惨祸之咒眼 43011492, continuous spell 静冠之咒眼 79400597, normal trap 妒绝之咒眼 6494106, continuous trap 死配之咒眼 42899204, counter trap 断罪之咒眼 79383919
- Build quirks from the repo decks: pure builds play 3 copies of every archetype card with 15 to 18 archetype spells and traps, no one-card link combo, so they grind for card advantage; control variants add floodgates 千查万别, 群雄割据, 技能抽取, 召唤限制器, 王家长眠之谷 plus 金满而谦虚之壶; some variants splash 冥王结界波, 超融合, or 海龟坏兽 as removal that also answers the mirror lock

- **Core Mechanic: 太阴 Equip Lock**

- 太阴之咒眼 44133040 equips only 咒眼 monsters and makes the equipped monster unable to be destroyed by battle or opponent effects and unable to be targeted by opponent effects, which is the deck protection layer
- Every 咒眼 quick effect is gated on being equipped with 太阴之咒眼 44133040: 沙利叶 82466274 destroys one opponent special-summoned monster, 美杜莎 18551923 banishes one opponent graveyard monster, 泽拉凯尔 17739335 destroys one opponent card on field, 戈耳戈涅 29357687 negates one opponent effect monster until end of turn, all usable during the opponent turn once per turn
- 蛇发之咒眼 28957126 is treated as 太阴之咒眼 44133040 while face-up in the spell and trap zone, so equipping it satisfies every gated quick effect, but it does NOT grant the destruction and targeting protection, keep a real 太阴 on the monster for defense
- 太阴之咒眼 44133040 triggers whenever you activate the equipped monster's effect or any other 咒眼 spell or trap: the equipped monster gains 500 ATK and you lose 500 life points, so playing spells drains your life and the drain is converted into attack power by 蛇发之咒眼 28957126 which gives the equipped monster attack equal to the life point difference while you are behind
- 太阴之咒眼 44133040 recurs from the graveyard: pay 1000 life points and banish another 咒眼 spell or trap from your graveyard to set itself, which is the main grind loop along with 唤忌之咒眼 17616743 reviving monsters
- Life point sharing: 咒眼领阈-错视之城- 70122149 makes battle damage you take from an attack against your 咒眼 monster also hit the opponent while 太阴之咒眼 44133040 is face-up in your spell and trap zone

- **One-Card Combo: 沙利叶 82466274**

- Starter: 咒眼之死徒 沙利叶 82466274 in hand, no other cards needed
- Step 1: normal summon 沙利叶, its trigger effect one adds any 咒眼 card from deck to hand except itself, add 太阴之咒眼 44133040
- Step 2: activate 太阴之咒眼 44133040 and equip it to 沙利叶, the monster becomes indestructible by battle and effects and untargetable by opponent effects
- Step 3: 沙利叶 effect two is now live, destroy one opponent special-summoned monster as a quick effect on either turn, once per turn
- End field for one card: one protected 1600 attack body with one removal per turn, the set-up for the next turn's grind rather than a link board
- Full board line with two more cards: special summon 巴西利乌斯 81344637 from hand (needs a 咒眼 monster on field) and dump 灾诞之咒眼 8775395 from deck to graveyard, link 沙利叶 and 巴西利乌斯 into 戈耳戈涅 29357687, then special summon 巴西利科克 65351555 from hand or graveyard and link into 泽拉凯尔 17739335, 灾诞's graveyard effect then equips 太阴之咒眼 44133040 from graveyard onto 泽拉凯尔

- **End Field Full Board**

- 咒眼之王 泽拉凯尔 17739335 equipped with 太阴之咒眼 44133040 as the boss: 2600 attack, indestructible and untargetable, one quick destroy of any opponent card per turn on both turns, and two attacks per battle phase if it was link summoned using a material with 2600 or more attack
- 咒眼之女王 戈耳戈涅 29357687 placed in 泽拉凯尔's bottom-right arrow zone: attack grows by 100 for each distinct 咒眼 card name in your graveyard, one quick negate of an opponent effect monster per turn on both turns
- One set trap, usually 断罪之咒眼 79383919 counter trap or 妒绝之咒眼 6494106 bounce, plus 咒眼领阈-错视之城- 70122149 in the field zone for the search and shared battle damage
- Halt points: Ash Blossom on 沙利叶's search or on 灾诞之咒眼's activation denies the combo, 无限泡影 or 效果遮蒙者 on the normal summon stops the search, 小丑与锁鸟 after the first deck to hand search stops 灾诞 and 蛇发 searches, 浮幽樱 banishes 泽拉凯尔 from the extra deck, Nibiru lands around the fifth summon, and a Kaiju or 冥王结界波 is the classic out to the equip lock

- **Extender: 巴西利乌斯 81344637**

- Inherent special summon from hand while you control a face-up 咒眼 monster, once per turn by this method, then effect two sends any 咒眼 spell or trap from deck to graveyard
- The dump feeds every graveyard tool: 灾诞之咒眼 8775395 effect two equips from graveyard, 太阴之咒眼 44133040 effect three sets itself from graveyard, 蛇发之咒眼 28957126 effect three searches from graveyard, 静冠之咒眼 79400597 effect one uses a graveyard card as draw cost

- **Extender: 灾诞之咒眼 8775395**

- Cost sends one 咒眼 monster and one 咒眼 spell or trap from deck to graveyard, then adds one 咒眼 equip spell from deck to hand, usually 太阴之咒眼 44133040 or 蛇发之咒眼 28957126
- After the cost both a monster and 太阴 are in graveyard, so the link climb triggers effect two of 灾诞 which equips one 咒眼 equip from graveyard onto the freshly link summoned 咒眼 link monster
- Tax: for the rest of the turn every effect you activate from a non 咒眼 card costs 500 life points, so do not activate hand traps, 指名者, or generic draw spells after 灾诞 in the same turn

- **Extender: 眷现之咒眼 7610394**

- Special summons one 咒眼之眷属衍生物 7610395 token, or two tokens while 太阴之咒眼 44133040 is face-up in your spell and trap zone, giving cheap link material toward 泽拉凯尔 17739335
- Locks you into Fiend only summons for the rest of the turn, so activate it only after any non-Fiend plays are done
- Graveyard effect banishes itself to make your 咒眼 spells and traps untargetable by opponent effects for the turn

- **Extender: 唤忌之咒眼 17616743**

- Special summons one 咒眼 monster from hand or graveyard, and from the deck as well while 太阴之咒眼 44133040 is face-up in your spell and trap zone
- The deck summon option turns 唤忌 into a one-card link climb once the 太阴 lock is up, and the graveyard option revives spent 沙利叶 82466274 or 美杜莎 18551923 for their quick effects again

- **Extender: 巴西利科克 65351555**

- Quick effect special summons itself from hand or graveyard while you control a face-up 咒眼 monster, usable on either turn, banished if it leaves the field
- Effect two on the opponent turn link summons a 咒眼 link monster using your monsters, and your 咒眼 equip spells in the spell and trap zone count as 咒眼 monsters for the materials, a defensive mid-combat climb into 戈耳戈涅 29357687 to negate or 泽拉凯尔 17739335 to destroy
- The equip spells used as material go to the graveyard, so the equipped monster loses the 太阴 protection when this line is used

- **Mirror Match: 咒眼 vs 咒眼**

- The player who lands 太阴之咒眼 44133040 on a monster first with a live quick effect controls the pace, so fight over 沙利叶 82466274's normal summon and search
- 妒绝之咒眼 6494106 bounces the equipped monster, which sends the equip to the graveyard, but the opponent re-sets 太阴 with its graveyard effect, expect a long grind war over graveyard recursion
- 惨祸之咒眼 43011492 destroys the opponent's 太阴 or 蛇发 in their spell and trap zone, and banishes it instead while your own 太阴 is up, strip their equip zone first
- 死配之咒眼 42899204 steals an opponent monster special summoned in attack position with lower attack than your 咒眼 monster, and the stolen monster counts as 咒眼 while 太阴 is up, so it can be used as material for 泽拉凯尔 17739335
- 戈耳戈涅 29357687's attack is large in the mirror because both graveyards hold many distinct 咒眼 names, and its negate on the opponent 泽拉凯尔 stops the quick destroy
- 蛇发之咒眼 28957126 decides attack races: the player behind on life points gains attack equal to the difference, so finishing swings and 咒眼领阈 shared battle damage matter more than life point total

- **Common Mistakes**

- Do not activate 眷现之咒眼 7610394 before non-Fiend plays, its Fiend only summon lock stops I：P百变莱娜, 超融合, and generic link monsters for the turn
- Do not chain hand traps or generic spells after 灾诞之咒眼 8775395 activates, each non 咒眼 activation costs 500 life points for the rest of that turn
- Remember the standby phase penalties after using the quick effects: 沙利叶 82466274 destroys one of your own cards, 美杜莎 18551923 banishes one of your own graveyard cards, 泽拉凯尔 17739335 negates one effect monster in its linked zone, and 戈耳戈涅 29357687 destroys one monster in its linked zone, which can be your own monster
- Dodge the standby penalty by using the monster as link material after its quick effect, the penalty effect disappears when the monster leaves the field
- 妒绝之咒眼 6494106 is a normal trap and 断罪之咒眼 79383919 is a counter trap, both must be set a turn before use, neither works from the hand
- 泽拉凯尔 17739335 requires every material to be a 咒眼 monster, build 戈耳戈涅 29357687 first with two monsters and then link up, a single non 咒眼 material is illegal
- 泽拉凯尔's double attack needs a material with 2600 or more attack, the pure way is another 泽拉凯尔 or a 2600 plus tech like 恐龙摔跤手·潘克拉辛角龙, do not waste the effect by using small materials
- 蛇发之咒眼 28957126 satisfies the equipped with 太阴 conditions but provides no protection, never rely on it alone against destruction and targeting effects
- Do not over-activate spells while 太阴之咒眼 44133040 is equipped, each 咒眼 spell or trap activation costs 500 life points and the drain can kill you before 蛇发 converts it into attack
- 唤忌之咒眼 17616743 summons from deck only while 太阴之咒眼 44133040 is face-up in your spell and trap zone at activation, do not waste it on a hand or graveyard summon when the deck summon would climb
- 灾诞之咒眼 8775395 needs one 咒眼 monster and one 咒眼 spell or trap in deck as cost and an equip spell to add, run at least six equips in the build so it does not fizzle late
- 美杜莎 18551923 adds from graveyard not from banishment, keep 静冠之咒眼 79400597 effect three in mind to return banished 咒眼 cards to the graveyard
- 死配之咒眼 42899204 self-destroys when the stolen monster leaves the field and needs your 咒眼 monster with higher attack at activation, steal only monsters you can protect or link away
- 巴西利科克 65351555 effect two works only on the opponent turn and consumes your equipped 太阴 or 蛇发 as material, dropping the protection on the target monster
