---
name: tribrigade-experience
description: 铁兽战线 (Tri-Brigade) deck experience: banish-link engine, one-card combo, extenders, halt points
---
# 铁兽战线 (Tri-Brigade) Deck Experience

- **Deck Identity**

- Beast/Beast-Warrior/Winged-Beast link deck, EARTH/WIND/DARK attributes, a graveyard-recursion engine that climbs links by banishing its own monsters
- Main monsters: 纳贝尔 14816857 (WIND Winged Beast Lv1, searches a 铁兽 monster when sent to the graveyard), 姬特 56196385 (EARTH Beast Lv2, mills a 铁兽 card when sent to the graveyard), 克拉斯 50810455 (EARTH Beast-Warrior Lv2, self special summons by discarding a Beast), 弗拉克杜尔 87209160 (EARTH Beast-Warrior Lv4, sends a Level 3 or lower Beast from the deck to the graveyard), 铁兽鸟 墨丘利信使 19096726 (DARK Winged Beast Lv4 handtrap, searches 阿不思的落胤 or Albaz-listing monsters when banished)
- Link monsters: 徒花之费莉吉特 26847978, 银弹之卢加鲁 52331012, 块击之蓝辉熊 47163170, 铁兽式击灭兵装“捕鼠猫” 33781156 (Link-2), 凶鸟之施莱格 99726621 (Link-4 boss), 铁兽式强袭机动兵装改“牛头伯劳2” 10019086 (Link-4 lock)
- Spells and traps: 铁兽的凶袭 51097887, 铁兽的击铁 92269002, 铁兽的咆哮 10793085 (quick-plays), 铁兽的邂逅 96378317 (continuous spell), 铁兽的抗战 40975243, 铁兽的血盟 86379342 (traps)
- Near-pure builds (deck/230114铁兽) run the four main monsters with 救援猫 14878871 and 迅捷河狸 68353324 as extra bodies, 炎舞-天玑 57103969 and 愚蠢的埋葬 81439173 as searchers
- Build quirks: the 201031 builds add the Simorgh lock (王神鸟 斯摩夫 72330894 + 霞之谷的巨神鸟 29587993), the 250726 builds go 迅捷/Spright hybrid with 迅捷鮟鱇 88686573, 卫星闪灵迅妖龙炮 72329844 and 天霆号 阿宙斯 90448279, and some splash 黑衣龙 白界龙 25451383 plus 烙印之剑 81767888

- **Core Mechanic: Banish-Link Engine**

- All four main deck 铁兽 monsters (纳贝尔 14816857, 姬特 56196385, 克拉斯 50810455, 弗拉克杜尔 87209160) share effect ①: banish any number of Beast/Beast-Warrior/Winged-Beast monsters from the graveyard, then special summon from the extra deck 1 Beast/Beast-Warrior/Winged-Beast Link monster whose Link Rating equals the number banished
- Verified in c14816857.lua: an ignition effect on the field monster that special summons the Link directly with no field materials, so the monster must be on the field and you need free zones, and “when Link Summoned” triggers (捕鼠猫 33781156 effect ①, 战华盟将-双龙 65711558 effect ①) do not fire from this engine
- The engine summons respect summoning conditions but need no materials, so it can summon any matching Link: 莱特哈特 53776969 (Link-1 Beast-Warrior) for 1 banish, 费莉吉特 26847978 / 卢加鲁 52331012 / 蓝辉熊 47163170 / 双龙 65711558 for 2, 施莱格 99726621 or 牛头伯劳2 10019086 for 4
- After an engine effect resolves, until the end of the turn you can only use Beast/Beast-Warrior/Winged-Beast monsters as Link Material (field effect in the scripts), so generic links like 阿波罗萨 4280258 and 访问码语者 86066372 must be made before the engine
- Graveyard triggers fuel the loop: 纳贝尔 14816857 adds a 铁兽 monster from the deck, 姬特 56196385 mills a 铁兽 card from the deck, each once per turn when sent to the graveyard, so the deck dumps then banishes the same monsters repeatedly
- 铁兽的抗战 40975243 special summons any number of banished Beast/Beast-Warrior/Winged-Beast monsters with negated effects and immediately link summons a 铁兽 Link using exactly those monsters (Duel.LinkSummon in c40975243.lua), a proper link summon so 捕鼠猫 33781156 effect ① triggers
- 铁兽的击铁 92269002 effect ② banishes 铁兽 cards from the graveyard and special summons a 铁兽 Link with matching Link Rating ignoring summoning conditions, the alternate engine that bypasses 牛头伯劳2 10019086 restrictions

- **One-Card Combo: 弗拉克杜尔 87209160**

- Starter: 弗拉克杜尔 87209160 in hand plus any one Beast/Beast-Warrior/Winged-Beast monster in hand as discard fodder for 克拉斯 50810455, no other specific cards needed
- Step 1: activate 弗拉克杜尔 87209160 effect ①, send it from hand to the graveyard, mill 纳贝尔 14816857 from the deck
- Step 2: 纳贝尔 14816857 effect ② triggers, add 克拉斯 50810455 from the deck to hand
- Step 3: activate 克拉斯 50810455 effect ①, discard the fodder monster, special summon 克拉斯 50810455 from hand
- Step 4: activate 克拉斯 50810455 effect ②, banish 弗拉克杜尔 87209160 and 纳贝尔 14816857 from the graveyard, special summon 蓝辉熊 47163170 (Link-2) from the extra deck
- Step 5: activate 蓝辉熊 47163170 effect ①, discard 2 cards, special summon the banished 纳贝尔 14816857 back to the field
- Step 6: link summon 施莱格 99726621 using 克拉斯 50810455, 蓝辉熊 47163170 and 纳贝尔 14816857 (Link Rating 4), 施莱格 99726621 effect ① banishes 1 card on the field
- Step 7: 蓝辉熊 47163170 effect ② triggers in the graveyard, add 铁兽的抗战 40975243 from the deck to hand, then return 1 hand card to the bottom of the deck
- Step 8: set 铁兽的抗战 40975243, the 蓝辉熊 47163170 effect ② lock limits further special summons to 铁兽 monsters only until the end of the turn
- Halt point: 灰流丽 14558127 on step 1 or step 2 stops the line cold, 增殖的G 23434538 sees 5 summons
- Older variant without 蓝辉熊 47163170 (201031 builds): banish 2 into 费莉吉特 26847978, its effect ① special summons from hand, then climb to 施莱格 99726621 with no 抗战 40975243

- **End Field**

- 施莱格 99726621 (Link-4, 3000 ATK): effect ① banishes 1 card on the field whenever it is special summoned or another Beast/Beast-Warrior/Winged-Beast is special summoned while it is on the field, a repeatable quick removal on your opponent turn
- One set 铁兽的抗战 40975243: on the opponent turn, special summon the banished engine monsters (弗拉克杜尔 87209160, 纳贝尔 14816857, fodder) and link summon 施莱格 99726621 again for another banish, or 捕鼠猫 33781156 to mill 2 more 铁兽 cards
- Backrow options: 铁兽的咆哮 10793085 (mills a 铁兽 card type from deck or extra deck as cost, then ATK 0 / effect negate / bounce the target), 铁兽的凶袭 51097887 (deck extension), 铁兽的邂逅 96378317 (co-linked pump plus graveyard destruction protection)
- 牛头伯劳2 10019086 variant: locks the opponent out of responding to your special summons and on attack declaration banishes itself and all opponent cards, but needs 3+ 铁兽 spells/traps in the graveyard when special summoned by the engine
- Simorgh lock variant: 王神鸟 斯摩夫 72330894 special summons 霞之谷的巨神鸟 29587993 at the end phase, which negates effects by bouncing itself, plus 烈风之结界像 wind floodgate, a hard lock but vulnerable to board breakers
- Halt point: the deck has no play under 次元吸引者, both the engine and 铁兽的抗战 40975243 need the graveyard and banished zone intact

- **Extenders**

- 救援猫 14878871: send itself to the graveyard, special summon 姬特 56196385 and 迅捷河狸 68353324 from the deck as two Beast link materials, effects negated and destroyed at the end phase
- 迅捷河狸 68353324: on normal summon, special summon 1 Level 3 or lower 迅捷 monster from the deck or graveyard, usually 迅捷鮟鱇 88686573 whose own trigger (sent from hand or deck to the graveyard) pops 2 more 迅捷 monsters
- 炎舞-天玑 57103969: on activation add 1 Level 4 or lower Beast-Warrior from the deck, usually 弗拉克杜尔 87209160 or 克拉斯 50810455, also pumps Beast-Warriors by 100 ATK
- 愚蠢的埋葬 81439173: send 姬特 56196385, 迅捷鮟鱇 88686573 or 纳贝尔 14816857 from the deck to start the graveyard engine
- 铁兽的凶袭 51097887: quick-play, target 1 Beast/Beast-Warrior/Winged-Beast you control and special summon a different-race one from the deck with equal or lower ATK in defense, effects negated, one extra body plus engine fuel, locks extra deck summons to Link monsters after
- 铁兽的击铁 92269002: effect ① searches any 铁兽 spell or trap, effect ② banishes 铁兽 cards from the graveyard to special summon a 铁兽 Link ignoring summoning conditions, the main route to 牛头伯劳2 10019086
- 银弹之卢加鲁 52331012: on the opponent main phase, special summon 1 Level 4 or lower Beast/Beast-Warrior/Winged-Beast from hand or graveyard with negated effects that returns to hand at the end phase, extra disruption plus a body
- 块击之蓝辉熊 47163170: discard 2 to recycle a banished Level 4 or lower monster, and its graveyard effect searches any 铁兽 spell or trap, the combo extender and S/T tutor in one
- 铁兽鸟 墨丘利信使 19096726: when banished by the engine it adds 阿不思的落胤 or a monster listing it (黑衣龙 白界龙 25451383) from the deck to hand, the Branded splash entry point

- **Halt Points**

- 灰流丽 14558127: on 弗拉克杜尔 87209160 effect ① dump, on the 纳贝尔 14816857 search, or on the engine activation, each kills or cripples the line
- 墓穴的指名者 24224830 and 抹杀之指名者 65681983: the deck's own answers to 灰流丽 14558127 and 增殖的G 23434538, protect the dump and the engine with them
- D.D.乌鸦 24508238 and 屋敷童 73642296: banish or block the 纳贝尔 14816857 and 姬特 56196385 graveyard triggers before the engine consumes them
- 增殖的G 23434538: the full combo special summons 5 times, under it stop at 费莉吉特 26847978 or 施莱格 99726621 only and pass with backrow
- 尼比鲁 27204311: the fifth summon is 施莱格 99726621, so the line is Nibiru-able, hold a 指名者 or end in fewer summons
- 次元吸引者 and 次元裂缝: banishing all graveyard monsters kills both the engine and 铁兽的抗战 40975243, the deck has no play under them
- 无限泡影 10045474 and 禁忌的一滴 on the field monster that would use the engine stop the climb, sequence the 抗战 40975243 set or 指名者 protection first

- **Mirror Match**

- The mirror is a race of 铁兽的抗战 40975243: whoever resolves the set Revolt on the opponent turn removes their board, every special summon under 施莱格 99726621 banishes 1 card
- Chain 施莱格 99726621 effect ① carefully, it is optional, in the mirror remove the opponent 施莱格 99726621 or 蓝辉熊 47163170 before their search resolves
- Keep 3+ 铁兽 spells/traps in the graveyard so your 牛头伯劳2 10019086 can be summoned and the opponent 牛头伯劳2 10019086 cannot
- 铁兽的咆哮 10793085 wins monster trades in the mirror: mill a Spell for effect negation or a Monster for ATK 0 against the opponent 施莱格 99726621
- Do not overextend into 增殖的G 23434538 in the mirror, the opponent 抗战 40975243 converts your summons into their banishes
- Watch 铁兽的邂逅 96378317 pumps on co-linked monsters and break the co-link before battle

- **Common Mistakes**

- Do not use an engine effect before generic link summons, the end-of-turn restriction only allows Beast/Beast-Warrior/Winged-Beast Link Materials, so 阿波罗萨 4280258, 访问码语者 86066372 and I：P百变莱娜 65741786 must be made first
- 捕鼠猫 33781156 effect ① and 铁兽的击铁 92269002 effect ② lock extra deck summons to Beast/Beast-Warrior/Winged-Beast for the turn, plan 访问码语者 86066372 accordingly
- 牛头伯劳2 10019086 cannot be engine-summoned with 2 or fewer 铁兽 spells/traps in the graveyard, mill 铁兽的咆哮 10793085 or 铁兽的抗战 40975243 first, only 击铁 92269002 effect ② ignores this condition
- 铁兽的咆哮 10793085 mills a 铁兽 card from the deck or extra deck as cost, dumping 施莱格 99726621 from the extra for the Monster effect is legitimate and good for graveyard fuel
- 克拉斯 50810455 effect ① needs a discard and the discard must be another Beast/Beast-Warrior/Winged-Beast, never activate it with an empty hand
- 铁兽的抗战 40975243 special summons are negated and the link summon uses exactly those monsters, no mixing in field monsters
- 块击之蓝辉熊 47163170 effect ② locks special summons to 铁兽 monsters after the search, sequence 施莱格 99726621 before activating the search
- 姬特 56196385 effect ② mills a 铁兽 card to the graveyard, it does not add to hand, and 纳贝尔 14816857 cannot search another 纳贝尔 14816857
- 铁兽的邂逅 96378317 only pumps co-linked monsters, activating it without a co-link wastes it
- Do not banish every Beast/Beast-Warrior/Winged-Beast from the graveyard, keep fuel for 铁兽的抗战 40975243 and 铁兽的击铁 92269002
- 铁兽鸟 墨丘利信使 19096726 effect ② searches only 阿不思的落胤 or Albaz-listing monsters, not a 铁兽 card, keep it out of 抗战 40975243 banishes unless the Branded splash is in the deck
- The monster special summoned by 铁兽的凶袭 51097887 has negated effects and cannot use the banish-link engine, use it as link material only
- 铁兽的血盟 86379342 effect ② needs one Beast, one Beast-Warrior and one Winged-Beast on the field at once, hard to satisfy in the pure build, prefer it only in hybrid builds
