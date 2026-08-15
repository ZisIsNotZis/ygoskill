---
name: thunderdragon-experience
description: 雷龙 (Thunder Dragon) deck experience: thunder hand-discard engine, one-card combo, fusion bosses, halt points, mirror
---
# 雷龙 (Thunder Dragon) Deck Experience

- **Deck Identity**

- Near-pure 雷龙 builds analyzed from `deck/190000雷龙` and `deck/190112雷龙`, core engine at 3x: 雷龙 31786629, 雷兽龙-雷龙 29596581, 雷电龙-雷龙 56713174, 雷源龙-雷龙 20318029, 雷鸟龙-雷龙 83107873
- Boss fusions: 超雷龙-雷龙 15291624 (3x, search-floodgate lock), 雷神龙-雷龙 41685633 (2-3x, quick destruction), vanilla 双头雷龙 54752875
- Engine spells: 雷龙融合 95238394 (3x), 雷龙放电 18444733 (trap), 封印之黄金柜 75500286 (3x), 百雷之雷龙 82045034 (other 雷龙 builds)
- Extra deck link toolbox: 刺刀枪管龙 85289965, 装弹枪管龙 31833038, 梦幻崩影·凤凰 2857636, 梦幻崩影·独角兽 38342335, 常夏的避暑雷神 38406364, 拓扑三叶双头蛇 72529749, 连接栗子球 41999284, 安全龙 99111753, 纳祭之魔·阿尼玛 94259633
- Support: 太阳电池人 44586426, 雷劫龙-雷龙 55591586, 幻创龙 奇幻龙人神 78661338, 混源龙 巨涡始祖神 55878038, 超融合 48130397, 精神操作 37520316, 强欲而贪欲之壶 35261759
- Hand traps / answers: 灰流丽 14558127, 增殖的G 23434538, 墓穴的指名者 24224830, 抹杀之指名者 65681983, 效果遮蒙者 97268402, 无限泡影 10045474, 鹰身女妖的羽毛扫 18144506, 颉颃胜负 15693423
- 190000雷龙 variant packs a floodgate package: 虚无空间 5851097, 王宫的通告 51452091, 技能抽取 82732705, 神之宣告 41420027, 红色重启 23002292, 激流葬 53582587, 心灵崩坏 15800838
- Uncertainty note: 雷龙格斗 and 雷霆之翼龙 do NOT exist in this cards.cdb (searched all texts); the fusion engine is 雷龙融合 95238394 and the real bosses are 超雷龙-雷龙 15291624 / 雷神龙-雷龙 41685633 / 双头雷龙 54752875 — never try to play cards under those missing names

- **Core Mechanic: Thunder Hand-Discard Engine**

- Every main deck member discards itself from hand as cost for a search / recycle / special summon / ATK effect, and floats when removed or sent from field to grave
- 雷龙 31786629: main-phase discard → add up to 2 copies of 雷龙 itself from deck, script filter IsCode(31786629) so it NEVER searches other members
- 雷电龙-雷龙 56713174: quick discard on either player's turn → add 1 copy of itself from deck; when removed or sent from field to grave → add 1 non-self 雷龙 card from deck
- 雷兽龙-雷龙 29596581: discard → add 1 non-self 雷龙 card from grave or banished zone; when removed or sent from field to grave → special summon 1 雷龙 monster from deck in defense, it returns to hand at end phase
- 雷鸟龙-雷龙 83107873: discard → special summon 1 non-self 雷龙 monster from grave or banished zone; when removed or from field to grave → shuffle any number of hand cards to deck, then draw the same number
- 雷源龙-雷龙 20318029: quick discard on either turn → target a thunder monster, +500 ATK; when removed or from field to grave → add another 雷源龙 from deck, a self-looping booster
- Script-verified float rule: the second effects trigger on EVENT_REMOVE from any location (hand, field, deck) but the EVENT_TO_GRAVE trigger requires previous location on field — banishing a member from hand or deck fires it, plain hand-discards do not
- 雷兽龙 ① and ② share one once-per-turn lock, same for every member, so using one effect in a turn blocks the other copy of the card's other effect
- 雷鸟龙 ① can revive a properly fusion-summoned 超雷龙-雷龙 15291624 or 雷神龙-雷龙 41685633 from grave because the archetype filter accepts fusion monsters

- **One-Card Combo: 封印之黄金柜 75500286**

- Step 1: activate 封印之黄金柜, banish 雷兽龙-雷龙 29596581 from deck, its removal trigger fires and special summons 1 雷龙 monster from deck in defense (pick 雷电龙-雷龙 56713174), that body returns to hand at end phase
- Step 2: the banished 雷兽龙 comes back to hand during your second standby phase after activation, script RESET_SELF_TURN 2, a delayed recycle
- Step 3: discard the special summoned 雷电龙 (quick) to add another copy, discard 雷龙 31786629 to add 2 more 雷龙, the hand fills with members
- Step 4: activate 雷龙融合 95238394, shuffle the field / grave / banished thunder materials back to deck and fusion summon 超雷龙-雷龙 15291624 (雷龙 + any thunder) — the opponent search lock is up
- Step 5: leave 雷龙融合 in grave, its second effect banishes itself to add 1 thunder from deck on later turns, but it cannot be used the turn it was sent to grave
- Alternative one-card starter 孤高除兽 92998610: normal summon it, banish 雷兽龙 from hand as cost and banish another 雷兽龙 from deck, two removal triggers special summon 2 雷龙 monsters from deck, 3 bodies total
- From the 3 bodies link into 刺刀枪管龙 85289965 or 装弹枪管龙 31833038, or discard 雷源龙 / 雷电龙 first to enable 超雷龙 tribute special summon (tribute 1 non-fusion thunder effect monster)

- **End Field**

- 超雷龙-雷龙 15291624 (opponent cannot add cards from deck to hand except by draw, their searches die) plus 雷神龙-雷龙 41685633 (quick destruction of 1 card when any thunder monster hand effect activates, damage step allowed)
- 雷龙融合 95238394 in grave as a permanent +1 thunder per turn, hand of 雷龙 members ready for next turn discards
- 雷龙放电 18444733 face up: your thunder effect activations cannot be negated and 1/turn a summoned 雷龙 monster lets you banish a thunder from deck to destroy a spell or trap
- Floodgate variant adds 虚无空间 5851097 / 王宫的通告 51452091 / 技能抽取 82732705 / 神之宣告 41420027 / 红色重启 23002292 as set backrow
- OTK line: 刺刀枪管龙 85289965 double attack with attack halving, or two level 10 雷神龙 into 超重型炮塔列车 古斯塔夫最大炮 56910167 for 2000 burn

- **Extenders**

- 太阳电池人 44586426: normal summon mills 1 thunder from deck to grave feeding 雷龙融合 and 雷劫龙, and makes 电池人衍生物 tokens whenever a thunder is summoned for link material
- 常夏的避暑雷神 38406364: link 2 thunder, on the opponent's turn discard 1 to revive a thunder from grave into its linked zone, a defensive grinder
- 雷劫龙-雷龙 55591586: special summon by banishing 1 Light and 1 Dark from grave, Light from the 雷龙 family and Dark from 幻创龙 78661338; 2800 beater that searches a thunder after battle destruction and recycles a banished card at end phase
- 幻创龙 78661338: hand-trap that special summons itself when the opponent links and draws cards, the only Dark monster source for 暗之诱惑 1475311 and 雷劫龙's summon condition
- 百雷之雷龙 82045034: revive a thunder from grave plus all same-name copies, monsters leave the field are banished, played in several other 雷龙 builds in this codebase
- 超融合 48130397: fuse using both players' monsters, the opponent's thunder monsters are fuel for 超雷龙 / 雷神龙 / 双头雷龙 54752875
- 精神操作 37520316 steals an opponent monster as an extra body or link material, the only realistic way to make 水晶机巧-继承玻纤 50588353 without a tuner in some builds
- 强欲而贪欲之壶 35261759 draw 2 at the cost of 10 face-down banished cards, played in the 190112雷龙 build

- **Halt Points**

- 灰流丽 14558127 stops the hand discards (雷龙 31786629, 雷电龙 56713174, 雷兽龙 29596581, 雷鸟龙 83107873 first effects) and the 雷兽龙 float special summon from deck
- 墓穴的指名者 24224830 and 抹杀之指名者 65681983 on one member name negate every same-name copy for the turn, the deck runs 3x of each name so one 指名者 can kill a whole chain
- 增殖的G 23434538 taxes every special summon, but the discard engine itself summons nothing, play the hand loop under G and limit fusion / link summons to one
- 古遗物-圣枪 34267821 in the side deck stops all banishing for the turn, which kills the float triggers and 雷龙融合's banished-zone materials, a self-stun card
- 次元吸引者 91800273 style locks send discards to banish instead of grave, the float effects still fire but 雷龙融合 95238394 loses grave access, adapt by playing pure hand value
- Chain the discard effects correctly, 雷神龙-雷龙 41685633 pops on any thunder hand effect including your own, a sloppy first discard wastes the pop

- **Mirror Match: 雷龙 vs 雷龙**

- The first 超雷龙-雷龙 15291624 wins the search war, under the enemy lock 雷龙 31786629, 雷电龙 56713174 second effect and 雷龙融合 95238394 second effect all die
- Under the enemy 超雷龙 only 雷兽龙 ① grave recycle, 雷鸟龙 ① grave and banished-zone special summon, and your own 超雷龙 tribute special summon still function
- Remove the enemy 超雷龙 with 雷神龙-雷龙 41685633 quick pop or 雷龙放电 18444733, 超融合 48130397 is the mirror blowout because their thunder monsters are your fusion material
- 双头雷龙 54752875 is a vanilla fusion, only meaningful as a 超融合 target against their pure 雷龙 monsters or as 雷神龙 material
- 墓穴的指名者 24224830 trades decide the float chain, name 雷兽龙-雷龙 29596581 first because its float special summon is the engine
- 雷龙放电 18444733 resolves first to shield your hand effects from the mirror's 灰流丽 14558127
- Floodgate traps 技能抽取 82732705 and 虚无空间 5851097 are symmetric, the hand-discard engine ignores Skill Drain but 虚无空间 blocks your own fusion summons, commit it last

- **Common Mistakes**

- Do not discard 雷龙 31786629 expecting other members, it only adds copies of itself, use 雷电龙 56713174 second effect for non-self searches
- 雷龙融合 95238394 fuses from field, grave and banished zone only, never from hand, and its second effect is locked the turn it was sent to grave
- 雷兽龙 special summoned monsters return to hand at end phase, link, fuse or tribute them during the turn instead of leaving them as the only field presence
- 雷兽龙 ① and ② share a once-per-turn lock, using the discard effect blocks the float special summon that same turn
- 超雷龙 tribute special summon needs a thunder hand effect used that turn by either player and its lock hits only the opponent, your own searches keep working
- Sequence your 雷神龙 quick pop after deciding the target, every thunder hand discard including your own triggers it
- 雷神龙 alternate special summon banishes 1 thunder from hand plus 1 non-self thunder fusion from field and is a removal dodge, use it to escape destruction
- 双头雷龙 54752875 has no effect, never fusion summon it outside 超融合 against thunder monsters
- 技能抽取 82732705 negates your own 超雷龙 and 雷神龙 on-field effects, the floodgate variant closes the game with beaters and traps instead
- Aim 雷龙放电 18444733's deck banish at a 雷兽龙 to float special summon or a 雷电龙 to search, not at an arbitrary thunder
- 太阳电池人 44586426 third effect needs a 电池人 monster in field or grave, in these builds it is only the mill plus token maker
- 幻创龙 78661338 is your only Dark attribute monster, do not banish it for 暗之诱惑 1475311 if 雷劫龙-雷龙 55591586 still needs its Dark material
