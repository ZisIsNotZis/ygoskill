---
name: worldlegacy-experience
description: 星遗物 (World Legacy / World Chalice) deck experience: engine mechanics, one-card combo, extenders, halt points
---
# 星遗物 (World Legacy) Deck Experience

- **Deck Identity**

- True identity resolved by setcode: 星遗物 (World Legacy) is the archetype keyword, setcode 0xfe, confirmed in cards.cdb datas for every card named 星遗物
- The deck name 世界 is ambiguous in the collection: most *世界* folders are 不死世界 (Zombie World) field-spell decks or 世界末日/世界再生 Demise ritual decks, not this archetype; the true World Legacy decks pair 星遗物 with 星杯 (World Chalice, setcode 0xfd) and finish with 闭锁世界的冥神 98127546
- Core engine is the World Chalice link ladder: normal monsters 被星杯所选中者 22916281, 被星杯所劝诱者 58400390, 领取星杯的巫女 95511642, bridged by 星遗物-『星杯』 57288708 and 星杯的妖精莉丝 21893603
- Support spells carry the 星遗物 name and setcode 0xfe: 星遗物的继承者 99674361, 星遗物的醒存 31706048, 星遗物的加护 97648103, 星遗物的引导 21254443
- Optional splashes from the same story line: 机界骑士 (Mekk-Knight, setcode 0x10c) 苍穹之机界骑士 20537097, and 自奏圣乐 (Orcust, setcode 0x11b) 宵星之骑士吉尔苏 69811710

- **Core Mechanic: Normal-Monster Link Ladder**

- The ladder starts from Normal monsters, so 粗人预料 911883 special summons 被星杯所选中者 22916281 or 领取星杯的巫女 95511642 from deck for free when you control nothing
- 星杯龙伊姆杜克 31226177 is a link-1 over exactly one Normal monster, its continuous effect grants an extra Normal Summon of a 星杯 monster each turn
- 星遗物-『星杯』 57288708 is the payoff: if it was Normal Summoned face-up and leaves the field, it special summons 2 星杯 monsters from deck; in grave it banishes itself to add any 星遗物 card from deck
- Every 星杯 link monster triggers on leaving the field to special summon a 星杯 monster from hand, so the ladder replaces itself as you climb
- 星遗物的继承者 99674361 special summons any grave monster to a zone a Link monster points to, recycling ladder pieces for more climb
- 星遗物的醒存 31706048 excavates 5, adds one 机怪虫 or 星遗物 card and mills the rest, then locks you into Link-only extra deck summons for the turn

- **One-Card Combo: 粗人预料**

- Starter: 粗人预料 911883 in hand, empty field, any 星遗物-『星杯』 57288708 in deck
- Step 1: activate 粗人预料, special summon 被星杯所选中者 22916281 from deck
- Step 2: link it into 星杯龙伊姆杜克 31226177, use its extra Normal Summon for 星遗物-『星杯』 57288708
- Step 3: link 星遗物-『星杯』 into 星杯神乐夏娃 77610772, its leave-field effect summons 被星杯所劝诱者 58400390 and 领取星杯的巫女 95511642 from deck
- Step 4: link 夏娃 and one Normal into 星杯剑士奥拉姆 4709881, its effect tributes the linked 星杯 to revive a grave monster to its zone
- Step 5: link 奥拉姆 into 星键士利娃 39752820, set a 星遗物 spell or trap from deck, then activate 星遗物的继承者 99674361 to revive the tribute material
- Step 6: climb 利娃 plus material into 双穹之骑士阿斯特拉姆 21887175, or continue into 闭锁世界的冥神 98127546 using four monsters

- **End Field**

- 双穹之骑士阿斯特拉姆 21887175, untargetable by opponent effects, untargetable for attacks, and its battle boost beats any special summoned monster
- 闭锁世界的冥神 98127546 negates all opponent face-up monsters on link summon, is untargetable except by targeting effects, and negates one grave-special-summon effect per turn
- One set 星遗物 spell or trap from 星键士利娃 39752820, typically 星遗物的继承者 99674361 or 星遗物的引导 21254443
- 召命之神弓阿波罗萨 4280258 as an alternative end piece negating up to three monster effect activations, or 访问码语者 86066372 for the OTK push
- 双星神阿-维达 17469113 only if 8 or more distinct Link monsters exist across both fields and graves, its non-negatable shuffle resets the whole board

- **Extenders**

- 星杯的妖精莉丝 21893603 searches any 星杯 monster on summon, and in grave discards a hand or field monster to return to hand for repeat use
- 救援兔 85138716 special summons two same-name Normal monsters from deck, two 被星杯所选中者 22916281 become two 伊姆杜克 links
- 皮里·雷斯地图 33907039 searches any 0 ATK monster, which covers 领取星杯的巫女 95511642 and 星遗物-『星杯』 57288708, at half LP cost
- 星遗物的加护 97648103 adds two different 星杯 monsters from grave to hand, and in grave replaces a linked Link monster destroyed in battle
- 星遗物的引导 21254443 banishes a 星遗物 monster from hand or field to special summon two grave monsters, but they cannot attack this turn
- 星杯的守护龙 84899094 is a hand-trap negate for any effect targeting a linked monster, and in grave revives a Normal monster to a linked zone
- 宵星之骑士吉尔苏 69811710 mills a 自奏圣乐 or 星遗物 card on summon and makes tokens when alone, plus its column condition turns it into a tuner
- 通往星遗物的钥匙 2930675 recovers a banished 机界骑士 or 星遗物 card at activation
- 来自星遗物中的觉醒 12989604 is a trap that performs a Link Summon with your monsters on the opponent turn
- 沉眠于星遗物的深层 98935722 revives a level 5 or higher grave monster and negates opponent monster effects in its column while a 机界骑士 is out

- **Halt Points**

- 灰流丽 14558127 on 粗人预料 911883 leaves no field, on 星遗物的醒存 31706048 stops the excavation, on 星遗物-『星杯』 57288708 leave-field summon stops the ladder
- 增殖的G 23434538 punishes the whole ladder, every link step draws the opponent a card, stop after 伊姆杜克 if you must play
- 墓穴的指名者 24224830 and 抹杀之指名者 65681983 stop 星遗物-『星杯』 57288708 grave search and the revival effects
- 原始生命态尼比鲁 27204311 triggers on the fifth summon, keep a monster or the ladder past five summons in mind
- 无限泡影 10045474 on 星杯龙伊姆杜克 31226177 denies the extra Normal Summon, on 星杯的妖精莉丝 21893603 denies the search
- 效果遮蒙者 97268402 negates 粗人预料-target monsters that have on-field trigger effects, but 星遗物-『星杯』 leaves-field trigger still fires from grave
- 颉颃胜负 15693423 or 冥王结界波 54693926 clear the 阿斯特拉姆 end field since both bypass targeting protection

- **Mirror Match: 星遗物 vs 星遗物**

- The duel is won by the first 闭锁世界的冥神 98127546, its on-summon negation and targeting immunity outweighs any other piece
- Fight for 星遗物-『星杯』 57288708 first, the player who normal summons it and gets the 2-for-1 from deck has the material lead
- 星遗物的继承者 99674361 is the mirror breaker, revive 星遗物-『星杯』 from your own grave and let it leave again for another 2 monsters
- Use 星遗物-『星盾』 55787576 against mirror columns, its column makes your 星遗物 cards untargetable and undestroyable by opponent effects
- Keep 星键士利娃 39752820 set-card timing in mind, the set 星遗物 card cannot activate this turn unless a 星遗物 monster is already in your grave
- 双星神阿-维达 17469113 resets both engines at once, hold it for the turn you can end the game, since it locks your own summons that turn

- **Common Mistakes**

- Activating 星遗物的醒存 31706048 and then trying to summon a non-Link extra deck monster, the Link-only lock applies for the whole turn
- Special summoning 星遗物-『星杯』 57288708 from hand and expecting its 2-from-deck trigger, that trigger only fires if it was Normal Summoned
- Forgetting 星遗物的引导 21254443 summoned monsters cannot attack, plan the kill through 阿斯特拉姆 or 访问码语者 instead
- Using 星键士利娃 39752820 set effect with an empty grave, the set card is dead until a 星遗物 monster reaches your grave
- Forgetting 闭锁世界的冥神 98127546 can use one opponent monster as link material, it steals boss monsters on the way up
- Reviving 星遗物-『星盾』 55787576 from grave carelessly, its own effect lets the opponent special summon a monster from their hand or grave too
- 皮里·雷斯地图 33907039 halving LP then playing into 原始生命态尼比鲁 27204311, the Nibiru token plus half LP ends the game
- Overextending under 增殖的G 23434538, the archetype special summons more than any other deck of its size, always stop early against the handtrap
