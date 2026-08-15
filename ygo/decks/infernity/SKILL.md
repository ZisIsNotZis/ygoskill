---
name: infernity-experience
description: 永火 (Infernity) deck experience: zero-hand engine, launcher loop, ritual splash, halt points
---
# 永火 (Infernity) Deck Experience

- **Deck Identity**

- The deck folder 260425巳剑荷鲁斯魔的永火 is a custom rework: a small Infernity zero-hand package inside a 巳剑 ritual shell with 荷鲁斯 and 刻魔 (Fiendsmith) engines
- Newest build 260425 main deck runs a thin Infernity package: 永火恶魔 99177923, 永火死灵师 56209279, 永火贤者 46435376, 永火炮 66957584, 归来的死神 04599182
- Variant 260320永火荷鲁斯刻魔 runs the fuller Infernity core, adding 永火幻象 86197239, 永火主教 54320860, 永火咒法师 48144778, 永火压制 12541409, 无之炼狱 93946239
- 巳剑 ritual engine: 巳剑降临 81560239, 天羽羽斩之巳剑 13332685, 天丛云之巳剑 19899073, 布都御魂之巳剑 55397172, 巳剑之尊 麁正 40543231, 巳剑之尊 草那艺 82782870, 巳剑之尊 佐士 18176525, 夜刀蛇巳 20295753, 巳剑劝请 45171524, 巳剑之神镜 49721684, 巳剑大祓 17954937, 朽坏的祭仪要录 24461358, 仪式的事前准备 13048472
- 荷鲁斯 engine: 荷鲁斯的荣光-伊姆塞特 84941194, 荷鲁斯的先导-哈碧 47330808, 王之棺 16528181, 王墓的石壁 26984177
- 刻魔 engine: 刻印群魔的刻魔锻冶师 60764609, 刻魔的咏圣 98567237, 刻魔的赞圣 35552985, 刻魔的大圣棺 49867899, 红泪之魔 落泪 28803166
- Support: 毁灭之黑魔术师 59400890, 黑魔导的幕帘 41350417, 诡计恶魔 66540884, 恶魔的篡夺 82997779, 恶魔的谐谑 87985506, 手札抹杀 72892473
- Two cards in this deck have NO script file in this checkout: 归来的死神 04599182 and 刻魔的镇魂棺 02463794, they will not function when played

- **Core Mechanic: Zero-Hand**

- All Infernity monsters trigger only while your hand is exactly 0, verified in scripts as Duel.GetFieldGroupCount(tp,LOCATION_HAND,0)==0, both at activation and resolution
- 永火炮 66957584 effect one discards 1 Infernity monster from hand toward reaching zero, effect two sends face-up Launcher from S/T zone to GY to special summon up to 2 Infernity monsters from GY, only while hand is 0
- 永火恶魔 99177923 effect one special summons itself when drawn while hand is 0, effect two searches any Infernity card from deck on special summon while hand is 0
- 永火贤者 46435376 effect one discards your entire hand to reach zero, effect two mills an Infernity monster from deck when it is sent to GY while hand is 0
- 永火死灵师 56209279 effect two special summons 1 Infernity monster from GY once per turn while hand is 0, the fuller variant adds 永火幻象 86197239 which tributes itself to special summon 2 Infernity monsters from GY while hand is 0
- 永火主教 54320860 special summons itself from hand when it is the only card in hand, 永火咒法师 48144778 special summons itself from GY while hand is 0 and cuts opponent monster ATK by 800, both only in the fuller variant
- The zero-hand loop: 永火炮 66957584 special summons 永火恶魔 99177923 plus 永火死灵师 56209279 from GY, 永火恶魔 searches another Infernity card, 永火死灵师 revives 永火恶魔 again, repeat the search and revive cycle for infinite advantage

- **One-Card Combo: 巳剑降临 ritual line**

- Starter: 天羽羽斩之巳剑 13332685 in hand, no other cards needed
- Step 1: reveal 天羽羽斩之巳剑 in hand, special summon 巳剑之尊 麁正 40543231 from deck, then release 麁正 to trigger its search for 天丛云之巳剑 19899073
- Step 2: activate 巳剑降临 81560239 effect two, release 天羽羽斩之巳剑 from hand as the level 8 ritual material to ritual summon 天丛云之巳剑 19899073 from hand
- Step 3: 天丛云之巳剑 destroys all opponent monsters on special summon, 天羽羽斩之巳剑 release effect searches another 巳剑 card and special summons itself back
- Step 4: end field is 天丛云之巳剑 19899073 with board wipe plus quick negate, 天羽羽斩之巳剑 13332685 with its attack debuff, and one searched 巳剑 card in hand

- **End Field**

- 天丛云之巳剑 19899073 as the boss, 3200 ATK, destroys all opponent monsters on summon, quick effect makes opponent discard 1 card or negate their effect
- 天羽羽斩之巳剑 13332685 plus 布都御魂之巳剑 55397172 as grind bodies, both recur from GY via their release search effects
- 毁灭之黑魔术师 59400890 as an alternative finisher, special summons itself by banishing a 6 star or higher Spellcaster from field after a spell is activated and searches 黑魔术师 46986414 or a card listing it
- Backrow: 巳剑大祓 17954937 negate trap, 恶魔的篡夺 82997779 ritual summon or trap set, 王墓的石壁 26984177 field spell, 永火压制 12541409 negate plus burn in the fuller variant
- Link toolbox: 刻魔的大圣棺 49867899, 刻魔的神圣棺 32991300, 世海龙 西兰提斯 45112597, 真血公 吸血鬼 73082255

- **Extenders**

- 巳剑劝请 45171524 searches a 巳剑 monster, or takes 800 damage to special summon a 巳剑 monster from hand or GY, releasing a Reptile applies both
- 朽坏的祭仪要录 24461358 adds a ritual spell from deck and its named ritual monster, 仪式的事前准备 13048472 searches 巳剑降临 81560239 plus 天丛云之巳剑 19899073
- 巳剑之神镜 49721684 ritual summons a Reptile ritual monster from hand or GY, 夜刀蛇巳 20295753 special summons itself when sent to GY by effect
- 荷鲁斯的荣光-伊姆塞特 84941194 special summons itself from GY while 王之棺 16528181 is on field and discards to search 王之棺 then draws
- 刻印群魔的刻魔锻冶师 60764609 discards itself to search any 刻魔 spell or trap, 刻魔的咏圣 98567237 adds a Fiend Light monster and fusion summons
- 黑魔导的幕帘 41350417 special summons 黑魔术师 46986414 from deck for both players and searches a spell or trap listing 黑魔术师, feeding 毁灭之黑魔术师 59400890
- 手札抹杀 72892473 and 永火贤者 46435376 dump the hand to reach the zero-hand state for the Infernity loop

- **Halt Points**

- 灰流丽 14558127 stops the 天羽羽斩之巳剑 13332685 reveal summon, 巳剑降临 81560239 ritual, and 永火贤者 46435376 mill
- 增殖的G 23434538 punishes the ritual summon chains and the 永火炮 66957584 special summons
- 墓穴的指名者 24224830 and 抹杀之指名者 65681983 stop 天丛云之巳剑 19899073 and 布都御魂之巳剑 55397172 release recursion and the 永火死灵师 56209279 revive
- 禁忌的一滴 24299458 and 冥王结界波 54693926 blank the negates on 天丛云之巳剑 19899073 and 毁灭之黑魔术师 59400890
- Nibiru style cards punish the chain of special summons before the 巳剑 boss hits the board
- The zero-hand condition is fragile, any forced draw or search that lands a card in hand before 永火炮 66957584 or 永火恶魔 99177923 resolves kills the Infernity line

- **Mirror Match: 永火 vs 永火**

- Whichever player reaches zero-hand first and resolves 永火炮 66957584 gets the search engine rolling, so dump the hand early
- 天丛云之巳剑 19899073 is the trump, both sides race to ritual summon it first, its board wipe decides the game
- 布都御魂之巳剑 55397172 special summons a Reptile from GY when the opponent special summons, use it to answer their 巳剑 boss
- 巳剑大祓 17954937 negates the opponent ritual summon effect, time it against 天丛云之巳剑 19899073
- Do not play 归来的死神 04599182 or 刻魔的镇魂棺 02463794 in the mirror, they have no script in this build and are dead draws

- **Common Mistakes**

- Do not activate 永火炮 66957584 effect two with cards still in hand, the resolution check fails and the special summon fizzles
- 永火恶魔 99177923 searches only while hand is 0 at resolution, search after using the searched card or it wastes the search
- 永火贤者 46435376 mills only while hand is 0, discard everything first then send it to GY
- 巳剑降临 81560239 effect one ritual summons from deck using hand and field monsters, effect two ritual summons from hand using up to two deck monsters, read which side you are on
- 天羽羽斩之巳剑 13332685 reveal effect is once per duel, do not waste it on a low value 巳剑 monster
- 毁灭之黑魔术师 59400890 alternate summon needs a 6 star or higher Spellcaster banished from your field and a spell effect activated that turn, do not summon it without the setup
- 黑魔导的幕帘 41350417 negates the effects of the monsters it special summons this turn, 黑魔术师 46986414 itself cannot activate
- 诡计恶魔 66540884 searches 恶魔 of the trap variety, use it to grab 恶魔的篡夺 82997779 or 恶魔的谐谑 87985506 rather than a random monster
- 巳剑劝请 45171524 special summoned monsters cannot attack directly, plan the damage line around that restriction
