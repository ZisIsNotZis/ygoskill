---
name: skystriker-experience
description: 闪刀姬 (Sky Striker) deck experience: spell-loop engine, one-card combo, extenders, halt points
---
# 闪刀姬 (Sky Striker) Deck Experience

- **Deck Identity**

- Spell-control grind archetype that runs almost no main-deck monsters, the only main-deck monsters are 闪刀姬-零衣 (26077387, Raye) and 闪刀姬-露世 (37351133, Roze), both Level 4 Warriors with 1500/1500
- Every Ace monster is Sky Striker Ace (set 0x1115), every spell is Sky Striker (set 0x115), the set check drives every searcher and the 3-spells-in-grave bonus system
- Extra deck is a ladder of link monsters, 闪刀姬-燎里 (63288573, Kagari) and 闪刀姬-雫空 (90673288, Shizuku) are the engine, 闪刀姬-飒天 (8491308, Hayate) and 闪刀姬-魁奈 (12421694, Kaina) are the utility link-1s, 闪刀姬-泽克 (75147529, Zeke) is the default link-2 end board
- Other extra options, 闪刀姬-阿泽莉娅 (98462037, Azalea), 闪刀姬-卡米丽娅 (63013339, Camellia), 闪刀姬=零露 (76072561, Zero), 闪刀姬-阿泽莉娅·节制 (56741506, Azalea Restriction), 试号闪刀姬-天津 (25072579, Amatsu)
- Sample near-pure list deck/220000闪刀/19da613d3d881bca.ydk holds 3 零衣, 3 露世, 1 交闪, 1 大黄蜂, 3 of most spells, 2-3 of each link, the format's limits decide 交闪 count
- Current lflist (2026.7) puts 闪刀起动-交闪 (63166095) at 2 and 闪刀机-大黄蜂浮游单元 (52340444) at 1, older formats limited 交闪 to 1 or banned it, always check the active format

- **Core Mechanic: Main-Zone Lock and the Spell Loop**

- Every 闪刀 spell requires no monsters in your Main Monster Zones (scripts check GetSequence()<5), monsters in the Extra Monster Zones do not block them, so links live in the EMZ while the spell row runs free
- 闪刀姬-零衣 (26077387) is the whole engine, her quick effect on either turn releases herself and link summons any Sky Striker Ace link from the extra deck to an EMZ, her grave effect revives her when a face-up Sky Striker Ace link leaves the field by battle or an opponent effect
- The link-1 ladder, summon 闪刀姬-雫空 (90673288, non-WATER material) or 闪刀姬-飒天 (8491308, non-WIND) or 闪刀姬-魁奈 (12421694, non-EARTH) from 零衣, then ladder those into 闪刀姬-燎里 (63288573, non-FIRE material)
- 闪刀姬-燎里 (63288573) adds any 闪刀 spell from grave to hand when summoned, recycling 闪刀起动-交闪 (63166095) every turn, this recursion is the spell loop the deck is named for
- 闪刀姬-雫空 (90673288) searches a 闪刀 spell from deck at the end phase of the turn it was summoned, its name must not already be in your grave, she also drops every opponent monster by 100 ATK/DEF per spell in your grave
- 闪刀姬-飒天 (8491308) attacks directly and sends a 闪刀 spell from deck to grave when it battles, feeding the 燎里 recycle, 闪刀姬-魁奈 (12421694) makes one opponent monster unable to attack and gains 100 LP per 闪刀 spell activation
- The 3-spell threshold, with 3+ spells of any kind in your grave every 闪刀 spell gains its bonus effect, reaching this count on turn 1 is the deck's main goal
- 闪刀起动-交闪 (63166095) adds any 闪刀 card from deck except itself, so it can grab the monster 闪刀机-正义刀剑 (61151074) too, and draws 1 after it resolves once 3+ spells are in your grave
- 闪刀姬-泽克 (75147529) is a link-2 of any 2 monsters including 1 Sky Striker link, it banishes a face-up monster until the end phase on link summon and can send 1 card you control to gain 1000 ATK

- **One-Card Combo: 闪刀姬-零衣 (26077387)**

- Starter, 零衣 in hand with no other cards needed
- Step 1, normal summon 零衣 to a main zone and link summon 闪刀姬-雫空 (90673288) using her to an EMZ, main zones are empty again
- Step 2, end phase 雫空 searches 闪刀起动-交闪 (63166095) from deck because its name is not yet in your grave
- End field, 雫空 in the EMZ plus 交闪 in hand, nothing else, this is the standard one-card pass and the full engine is ready next turn
- Two-card line with 交闪, 交闪 adds 闪刀机-大黄蜂浮游单元 (52340444), 大黄蜂 summons the 闪刀姬衍生物 token (52340445), 零衣 ladders into 雫空 then into 燎里 (63288573), 燎里 recycles 交闪, 燎里 plus token link into 闪刀姬-泽克 (75147529), 交闪 again adds 闪刀机-黑寡妇抓锚 (98338152)
- The 交闪 draw and most bonus effects only trigger once 3+ spells sit in grave, count your grave before expecting the draw, a 飒天 (8491308) dump or 闪刀空域-零区 (50005218) excavate is the usual way to reach the count

- **End Field**

- One-card, 闪刀姬-雫空 (90673288) in the EMZ plus 闪刀起动-交闪 (63166095) in hand with no other field presence
- Two-card, 闪刀姬-泽克 (75147529) in the EMZ, 闪刀机-黑寡妇抓锚 (98338152) set, one spell still in hand, 泽克's summon already banished one face-up monster until the end phase
- 泽克's ignition can send 闪刀空域-零区 (50005218) or a spent spell to grave as setup, the banished monster returns at the end phase so plan the attack order
- Halt points, 灰流丽 (14558127) on 交闪 or on 雫空's search, 增殖的G (23434538) making the full ladder give many draws, effect negation on 零衣's link-summon quick effect stopping the ladder before it starts

- **Extenders**

- 闪刀姬-露世 (37351133) special summons herself from hand when another Sky Striker Ace is normal or special summoned, adding a second body for link-2 plays, her grave effect revives her when an opponent EMZ monster leaves the field by battle or your effect and then negates a face-up opponent monster
- 闪刀起动-连刀 (9726840) sends 1 card you control to grave and then special summons a Sky Striker Ace link from extra to an EMZ, +1000 ATK if you have both LIGHT and DARK Sky Striker Aces on field or in grave (零衣 is DARK, 露世 is LIGHT), it locks all non-Sky Striker extra summons for the turn
- 闪刀空域-零区 (50005218) field spell sends 1 other card you control, excavates 3 and adds a 闪刀 spell among them, when sent from the field zone to grave by an effect it special summons 零衣 from deck, pair it with 多任务战刀机 or 大力神基地
- 闪刀机关-多任务战刀机 (24010609) sends 1 other card you control and then only you may respond to your own spell activations, its end phase effect sets 闪刀 spells from grave up to the number of 闪刀 spells activated that turn, those sets are banished if they leave the field
- 闪刀机构-大力神基地 (97616504) equips a monster so it attacks twice and draws when it destroys by battle with 3+ spells, when sent from field to grave by an effect it shuffles up to 3 闪刀 spells from grave back to deck, recycling 交闪 (63166095)
- 闪刀术式-剪斗交刃 (46271408) returns a Level 4 Sky Striker Ace from grave to hand or special summons it with 3+ spells, bringing back 零衣 or 露世 for another ladder
- 闪刀机-虎鲨加农炮 (51227866) banishes an opponent grave monster or special summons it to your field without attack with 3+ spells
- 闪刀姬=零露 (76072561) is a link-2 of two Sky Striker links that adds a 闪刀 spell from deck or grave on summon and releases itself to special summon both 零衣 and 露世 from deck or grave plus destroy 1 card
- 闪刀机-正义刀剑 (61151074) is a hand monster that discards itself for +1500 ATK on a 闪刀 monster during the battle phase and equips itself from grave to a Sky Striker link for +1500 ATK
- 闪刀亚式-双纽闪门 (34433770) shuffles 闪刀 spells and Ace monsters from grave back to deck and bounces 1 field card per 3 shuffled, in grave it banishes itself to link summon a Sky Striker Ace link when a 闪刀 monster is special summoned

- **Halt Points**

- 灰流丽 (14558127) on 闪刀起动-交闪 (63166095) or on 闪刀姬-雫空 (90673288) end phase search stops the card advantage engine
- 增殖的G (23434538) punishes every link summon and the 大黄蜂 token, play the minimal line, 雫空 plus a set 闪刀机-黑寡妇抓锚 (98338152) with no ladder
- Banishing the 闪刀 spell in grave or 墓穴的指名者 (24224830) on it kills the 燎里 (63288573) recycle and the 3-spell bonuses
- 次元吸引者 (91800273) and similar grave-exiling effects shut down 燎里, the 交闪 draw, 剪斗交刃, 虎鲨加农炮, 零衣 and 露世 revival and all 3-spell bonuses
- Negating 零衣's (26077387) link-summon quick effect leaves her stuck in a main zone with no spells usable, the most fragile point of the turn
- Any effect negation on the links removes their search, recycle, attack lock or banish, Sky Striker links are pure effect monsters with no protection
- Field-based monster negation disables 雫空's attack drop, 魁奈's attack lock and 泽克's banish

- **Mirror Match: 闪刀姬 vs 闪刀姬**

- The first player who needs a main-zone monster to resolve loses spell access, sequence the 零衣 (26077387) ladder so monsters only ever sit in the EMZ
- 闪刀姬-露世 (37351133) grave trigger fires when an opponent EMZ monster leaves the field by battle or your effect, so destroying or stealing their link with 黑寡妇抓锚 (98338152) or 烈火再燃 (99550630) revives their 露世 and negates one of your monsters
- 泽克's (75147529) temporary banish still counts as leaving the field, the opponent 露世 revives and negates, factor that into every removal choice
- Remove the opponent 零衣 and 露世 from grave or hand before they ladder again, 虎鲨加农炮 (51227866) and 次元吸引者 (91800273) shine here
- 试号闪刀姬-天津 (25072579) is the dedicated mirror card, it changes an opponent monster effect with 2000+ ATK into destruction of one of their Sky Striker links, and on its own attack destroys your Sky Striker monster plus one of their cards
- The 3-spell race decides the mirror, whoever reaches 3 spells in grave first gets 黑寡妇抓锚's steal and the 1500 token, dump via 飒天 (8491308) or 闪刀空域-零区 (50005218)
- Keep your 零衣 in grave with a live revival trigger so losing a link in battle does not cost the whole turn

- **Common Mistakes**

- Activating 闪刀 spells while a monster sits in a Main Monster Zone, everything from 交闪 (63166095) to 黑寡妇抓锚 (98338152) fails, link monsters off into the EMZ first
- 交闪 cannot search itself and 雫空 (90673288) cannot search a spell already in your grave, sequence searches before dumping that spell
- Playing 大黄蜂浮游单元 (52340444) before 3 spells in grave when the 1500 token is needed, the token is 0/0 without the threshold
- Leaving the 大黄蜂 token in a main zone, it blocks your own spells until it is linked away or used as material
- Using 黑寡妇抓锚 for the negate only when 3+ spells would steal the monster until the end phase, the steal is the payoff
- Forgetting 零衣's link-summon quick effect works on the opponent turn, link into 魁奈 (12421694) to stop an attack or 飒天 (8491308) for value
- Summoning 燎里 (63288573) before 飒天 (8491308) battles, the dump only triggers on battle and it is the usual way to put a spell in grave for the recycle
- Using 连刀 (9726840) in a turn that needs a non-Sky Striker extra summon, the lock lasts the whole turn
- 阿泽莉娅 (98462037) sends itself to grave if 3 or fewer spells are in grave when its destroy resolves, keep 4+ spells or accept losing it
- 阿泽莉娅·节制 (56741506) only equips monsters with 2500 or less ATK and banishes a spell from hand or grave as cost, do not burn the only 交闪
- 多任务战刀机 (24010609) sets spells from grave at the end phase and those sets are banished if they leave the field, do not expect to reuse them next turn
- Forgetting the 3-spell threshold per spell, count the grave before 交闪 for the draw, 烈火再燃 (99550630) for the extra destroy, 鹰式推进器 (25733157) for indestructible, 妨害波纹 (25955749) for the monster destroy and 爆风偏向 (21623008) for the EMZ bounce
