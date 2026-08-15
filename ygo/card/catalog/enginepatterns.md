---
name: engine-patterns
description: Recurring engine shapes across archetypes: core loop, one-card minimum, end field, weak point
---
# Engine Patterns

- Cross-archetype study of the per-deck experience corpus, 40+ archetype documents read; decks with different names and different card text repeat the same engine geometry
- An engine shape is the fixed resource loop, the zone traffic it runs on (hand, field, grave, banished, deck, equip zone), its one-card entry point, the board it converges on, and the choke point where one interruption kills the whole line
- Every anchor is a real 8-digit card code verified in this codebase; a deck can run two shapes at once, the primary shape predicts the combo and the secondary shape fills the break plan

- **Token + Tuner Synchro Ladder**
  - **Core loop**: a normal summon makes a Tuner token (or recovers a Tuner) next to a non-Tuner, then the deck repeatedly Synchro Summons with fixed level math, each boss's effect summoning or recovering the next material until the Level 8-10 negate bosses land
  - **One-card minimum**: 相剑 莫邪 20001443 reveals any 相剑/Wyrm card to make the Level 4 Wyrm token 20001444 and Synchro 4+4 into 赤霄 69248256; 天杯龙 白龙 39931513 searches 灿幻开门 66730191 and Synchros during the Battle Phase into 灿幻升龙 82570174 then 灿幻超龙 18969888; 龙骑兵团 军事官 81962318 equips the Tuner 方阵龙 59755122 and re-summons it to climb
  - **End field**: 赤霄 69248256 negate plus 承影 96633955 banish engine and 鲜花女男爵 84815190; tenpai ends on the 灿幻超龙 18969888 Battle-Phase lock with lethal damage; dragunity ends on 始枪龙骑士 11969228 plus 龙之溪谷 62265044
  - **Weak point**: Ash the token-maker or the searcher (莫邪 summon effect, 龙相剑现 56465981, 灿幻开门 66730191), Veiler/Imperm the non-Tuner before the token appears, Nibiru around the fifth summon, and the token's own lock forbids Xyz/Link plays while it is on field
  - **Decks**: 相剑 swordsoul 莫邪 20001443, 天杯龙 tenpai 白龙 39931513, 龙骑兵团 dragunity 军事官 81962318

- **Dump-to-Grave Grave-Fusion Engine**
  - **Core loop**: a normal summon or spell mills a monster from deck to grave, the grave monster's trigger Fusion Summons using materials from hand, field and grave, and the fusion's own grave effects keep milling to chain further fusions in one activation
  - **One-card minimum**: 珠泪哀歌族 雷诺哈特 73956664 dumps 梅洛人鱼 74078255 and its grave trigger fuses 水仙女人鱼 92731385; 影依融合 44394295 fuses from the deck when the opponent controls an extra-deck summon and every material's grave effect fires; 暗黑界的登极 65956182 fuses with discarded materials so each discarded 暗黑界 triggers mid-fusion
  - **End field**: tearlaments ends on 鲁莎卡人鱼 84330567 negate plus 卡雷多哈特 28226490 spin with 壹世坏-珍珠世界 77103950 destroying on every recycle; shaddoll ends on 神影依·米德拉什 94977269 one-summon floodgate plus 影依的伪典 21011044; darkworld ends on 混沌王 22723778 or 龙神王 39552584
  - **Weak point**: Ash the dump or the search, 墓穴的指名者 24224830 or D.D.乌鸦 on the key grave monster before its trigger, 深渊的潜伏者 21044178 blanks all grave triggers, 次元吸引者 91800273 sends to banish instead of grave; shaddoll specifically dies to Ash on 影依融合 44394295 because the whole trigger chain is negated
  - **Decks**: 珠泪哀歌族 tearlaments 雷诺哈特 73956664, 影依 shaddoll 影依融合 44394295, 暗黑界 darkworld 暗黑界的登极 65956182

- **Banish-Pile Recursion Engine**
  - **Core loop**: the banished zone is the deck's real hand — monsters trigger when banished, summon themselves back from banished, and pay banish costs to recur; the opponent has few tools against a zone they cannot touch, and some variants weaponize banishing to mill the opponent
  - **One-card minimum**: 码丽丝 睡鼠 32061192 banishes 三月兔 20938824 from deck, 三月兔 pays 300 LP to add itself back, and the loop feeds Link summons; 俱舍怒威族 芬里尔狼 32909498 empty-field self-summon searches 莱斯哈特 31149212 into 香格里拉茧 73542331; 自奏圣乐 吉尔苏 69811710 dumps 嬉游曲恶魔 57835716 which banishes itself to summon from deck under 通天塔 90351981
  - **End field**: maliss ends on 红心加密 21848500 plus 梦游地下界 68337209 (+3000 ATK with three banished traps); kashtira ends on 香格里拉茧 73542331 plus No.89 95474755 with zone locks; orcust ends on 丁吉尔苏 93854893 plus 之阶 703897
  - **Weak point**: 古遗物圣枪 34267821 locks banishing outright, D.D. Crow removes the key banished or grave piece, 墓穴の指名者 24224830 hits the grave half of the loop, and 次元吸引者 91800273 is asymmetric — it fuels maliss (which plays from banished) but starves orcust and kashtira grave plays
  - **Decks**: 码丽丝 maliss 睡鼠 32061192, 俱舍怒威族 kashtira 香格里拉茧 73542331, 自奏圣乐 orcust 嬉游曲恶魔 57835716

- **Link-Climb Re-Link Loop**
  - **Core loop**: link into an anchor monster, then re-link the same-name monster using only itself as material through a field-spell clause, re-firing the on-material effect every turn; a grave piece specials itself into the anchor's zone to trigger its card-gain effect, recycling the spent spell or trap
  - **One-card minimum**: 转生炎兽 羚羊 26889158 dumps 犰狳蜥 52277807, links 烽火猞猁 14812471 which searches 圣域 1295111, then re-links 日光狼 87871125; 码语者 调试瓢虫女郎 16188701 searches the starter and climbs 转码语者 46947713 into 访问码语者 86066372
  - **End field**: re-linked 日光狼 87871125 with set 愤怒 14934922 or 咆哮 51339637, modern lists add 赐炎之咎姬 2772337; codetalker and ignister end on 访问码语者 86066372 double-attack OTK
  - **Weak point**: Ash the dump or the search (羚羊 ②, 烽火猞猁 ①, 调试瓢虫女郎 16188701), 墓穴の指名者 24224830 on the grave recursion pieces 犰狳蜥 and 灯火美洲豹 56003780, Nibiru lands right at the re-link step, and any grave banish wrecks the loop
  - **Decks**: 转生炎兽 salamangreat 羚羊 26889158, 码语者 codetalker 调试瓢虫女郎 16188701, @火灵天星 ignister 辣辣妖@火灵天星 15808381

- **Xyz Overlay-On-Top Ladder**
  - **Core loop**: one monster grows into a boss by overlaying Xyz monsters on top of it; materials transfer up the stack, the top monster inherits the whole pile, and detaching the pile pays for the final wipes and negates
  - **One-card minimum**: 十二兽 鼠骑 78872731 dumps 马剑 77150143, overlays 狗环 41375811, detaches to summon a second 鼠骑, climbs 虎炮 11510448 and 龙枪 48905153 then 天霆号阿宙斯 90448279; 救祓少女 马尔法 37343995 overlays on the opponent's grave plays into 米迦埃莉丝 42741437 and 圣母颂歌 59242457; 圣骑士 断钢湖中剑 46008667 overlays 圣骑士王 阿托利斯 21223277 into 神圣骑士王 康尼厄斯 78876707; 魔偶甜点 皇后·后冠提拉米苏 37164373 overlays into 后冠草莓提拉米苏 49689480
  - **End field**: stacked 阿宙斯 90448279 field wipe or 未来龙皇 霍普 26973555 negate-steal, madolche quick bounce, exosister 圣母颂歌 59242457 double attack with a banish
  - **Weak point**: Ash the starter's dump or first search, Veiler/Imperm the ladder piece before it detaches, Nibiru after five summons, and removing the base monster kills the climb — exosister has no overlay without a main-deck monster on field
  - **Decks**: 十二兽 zoodiac 鼠骑 78872731, 魔偶甜点 madolche 皇后·后冠提拉米苏 37164373, 圣骑士 nobleknight 断钢湖中剑 46008667, 救祓少女 exosister 马尔法 37343995

- **Discard or Mill-Pile Float-Search Engine**
  - **Core loop**: monsters trigger when discarded or milled by an effect, turning every discard outlet into search plus special summon; the pile from hand or deck into grave IS the resource, and the searched piece is the next discard
  - **One-card minimum**: 暗黑界 暗黑回廊 98696958 adds 术师 丝诺 60228941 then discards it to search; 雷龙 封印之黄金柜 75500286 banishes 雷兽龙 29596581 whose float special summons from deck; 永火 永火炮 66957584 plus 永火恶魔 99177923 run the zero-hand search loop; 不死 愚蠢的埋葬 81439173 mills 尸界的班西 66570171 which activates 不死世界 4064256 from deck
  - **End field**: thunderdragon ends on 超雷龙 15291624 search floodgate plus 雷神龙 41685633 quick destruction; infernity loops searches into a boss; zombie ends on 死灵王 恶眼 39185163 negate-standby plus 吸血鬼吸食者 37129797 draw engine
  - **Weak point**: Ash the search triggers, 屋敷童 73642296 on the grave triggers, 次元吸引者 91800273 sends discards to banish so the triggers never fire, 小丑与锁鸟 94145021 blocks the whole search chain, and any forced draw breaks infernity's zero-hand state
  - **Decks**: 暗黑界 darkworld 暗黑回廊 98696958, 雷龙 thunderdragon 封印之黄金柜 75500286, 永火 infernity 永火炮 66957584, 不死 zombie 愚蠢的埋葬 81439173

- **Control Trap Recursion**
  - **Core loop**: recursion lives in set traps — a normal summon searches and sets a trap, the trap's resolution summons a monster whose effect sets the next trap from deck or grave, and the backrow re-fills every turn; traps also carry grave effects that re-set themselves
  - **One-card minimum**: 白银之城 阿里安娜 1225009 searches 欢迎 5380979 and sets it; 虫惑魔 特莱恩 91812341 searches 墓穴洞 31548215 and links into 塞拉 73639099; 幻变骚灵 网络傀儡师 53143898 sets 物化 35146019 and trap activations summon 多功能诈骗者 42790071; 恐啡肽狂龙 镰刀龙 92133240 sets 激昂 78420796 for an opponent-turn fusion into 狂飙霸王龙 92798873; 黄金国巫妖 黑化觉醒之黄金国永生药 68829754 summons 黄金卿 95440946 and sets a 黄金乡 trap
  - **End field**: labrynth 白银之城的拉比林斯 2347656 with two to three set traps; traptrix 塞拉 73639099 plus 蒂奥 45803070 plus two traps; altergeist 十六巫赫斯提 1508649; dinomorphia 狂飙霸王龙 92798873 LP floodgate; eldlich trap monsters under 技能抽取 82732705
  - **Weak point**: Veiler/Imperm the searcher or the engine monster (塞拉 73639099 immunity covers traps only), backrow removal and trap negation (王宫的敕命 61740673, 魔封的芳香 58921041), and 次元吸引者 91800273 kills the grave re-set recursion that every loop depends on
  - **Decks**: 白银之城 labrynth 欢迎 5380979, 虫惑魔 traptrix 塞拉 73639099, 幻变骚灵 altergeist 多功能诈骗者 42790071, 恐啡肽狂龙 dinomorphia 镰刀龙 92133240, 黄金国巫妖 eldlich 黑化觉醒之黄金国永生药 68829754

- **Equip-and-Recur Equip Engine**
  - **Core loop**: Equip Spells are the engine pieces — equipping flips a dormant monster live, the equip trigger searches or summons, and the equip's grave or third effect re-equips itself to the replacement monster, refunding the destroy cost
  - **One-card minimum**: 御巫 水舞蹈 43527730 equips, summons a different-name Mikanko, re-equips and bounces, with 脆刃之剑 41927278 as the reflect kill; 圣骑士 莫德雷德 59057152 plus 加拉廷 14745409 self-destroy and re-equip; 龙骑兵团 方阵龙 59755122 equips itself as a Tuner and re-summons to keep synchroing; 海造贼 象征 80621422 tags out by opponent attribute
  - **End field**: mikanko 贵日女之御巫 57566760 reflect wall with untargetable protection; nobleknight 神圣骑士王 康尼厄斯 78876707 loaded with 圣剑; dragunity 始枪龙骑士 11969228 plus 龙之溪谷 62265044
  - **Weak point**: remove the equipped monster, not the equip — destroying a 圣剑 just triggers its re-equip, mikanko loses its reflect when the monster is negated or the equip is removed, and 次元吸引者 91800273 breaks every grave-equip recursion line
  - **Decks**: 御巫 mikanko 水舞蹈 43527730, 圣骑士 nobleknight 加拉廷 14745409, 龙骑兵团 dragunity 方阵龙 59755122, 海造贼 plunderpatroll 象征 80621422

- **Destruction-Trigger Float Chain**
  - **Core loop**: the deck destroys its own cards by effect and every destruction converts into a summon or search; the floated replacement destroys another of your cards, so one self-destroy triggers a whole chain, and set traps float when destroyed too
  - **One-card minimum**: 破械 娑罗摩 31588572 sets 破械唱导 53417695 then destroys it, 阿罗汉 26236560 floats from deck and the pair links into 阎摩 24269961; 炎王 凤凰不死鸟 90681088 searches 圣域 65305978, places 孤岛 57554544 and destroys Ponix to search 甘尼许 18621798 while Ponix recurs next standby
  - **End field**: unchained ends on 罗寂刹 67680512 plus 阎摩 24269961 plus set traps, 双极之破械神 1966438 re-summons itself on every destruction; fireking ends on 永炎 64182380 board wipe plus both field spells and 甘尼许 18621798 negate
  - **Weak point**: banish, tribute and absorb never trigger floats — 尼比鲁 27204311 tributes the field, 罗寂刹 67680512 consumes without destroying, 屋敷童 73642296 stops the grave loops, and destroying your own cards carelessly backfires (炎王的孤岛 57554544 wipes your board when it leaves the field)
  - **Decks**: 破械 unchained 娑罗摩 31588572, 炎王 fireking 凤凰不死鸟 90681088

- **Ritual Tribute-Total Engine**
  - **Core loop**: ritual spells convert hand, field, grave and banished monsters into tribute levels, a full-tribute piece counts as the entire needed level, and release triggers chain searches while the ritual spell's grave effect recycles itself for next turn
  - **One-card minimum**: no pure ritual deck has a true one-card line — the baseline is a ritual spell plus a monster, or one full-tribute piece (影灵衣 施里特 90307777, 肃声 理 25801745 covers the whole L7 requirement); 万华镜 51124303 sends 虹光之宣告者 79606837 from the extra deck as exactly-one material
  - **End field**: nekroz 尤尼科 89463537 extra-deck floodgate plus 天枪龙 74122412 and 舞姬 52738610; voicelessvoice 法理守护者 10774240 plus 结界 98477480 attack-and-target lock with 理 reviving from grave every ritual summon
  - **Weak point**: Ash the search chain (千手神 23401839, 万手神 95492061, 阿旺斯 51618973, 理 25801745), 墓穴の指名者 24224830 on the grave recycle loop, 次元吸引者 91800273 starves the banish-zone ritual spell, and 小丑与锁鸟 94145021 blocks the discard-searchers
  - **Decks**: 影灵衣 nekroz 万华镜 51124303, 肃声 voicelessvoice 理 25801745, 巳剑 (巳剑降临 81560239, documented as an infernity splash)

- **Pendulum Scale Engine**
  - **Core loop**: set two scales, pendulum summon a swarm, then convert the swarm into a boss by tribute or link; the pend-lock (no non-archetype special summons) is the price, and destroyed pendulums recur face-up in the extra deck as reusable fodder
  - **One-card minimum**: 机壳工具 丑恶 65518099 pays 800 LP to search any 机壳 and sits as scale 9; 魔界剧团 彩排 6004133 searches 狂放新秀 51391183 to summon 大明星 25629622; 恩底弥翁皇国 34041788 adds 雷古勒斯 96228804 and banks spell counters
  - **End field**: qliphort 无神论 40061558 Spell/Trap-immune boss plus 机壳的再星 20426907; endymion 创圣魔导王 3611830 negate with 银金公主 24094258; abyssactor 大明星 25629622 plus the 奇幻剧场 77297908 script lock
  - **Weak point**: 宇宙旋风 8267140 or 双龙卷 43898403 on the scales kills the summon range, Nibiru after the swarm, non-targeting removal bypasses the qliphort immunity (it blocks monster effects only), and endymion dies when the counter bank 魔法都市 39910367 is removed
  - **Decks**: 机壳 qliphort 机壳工具 丑恶 65518099, 恩底弥翁 endymion 恩底弥翁皇国 34041788, 魔界剧团 abyssactor 彩排 6004133

- **Tribute-Summon Engine**
  - **Core loop**: squires search or spawn tribute fodder, an extra-tribute-summon effect converts them into a tribute boss in one turn, the boss's tribute-summon effect dumps or searches the next boss, and a no-extra-deck lock is the payoff; some variants redirect the tribute cost onto the opponent's monsters
  - **One-card minimum**: 帝 天帝从骑 爱迪娅 95457011 summons 冥帝从骑 哀多斯 59463312, both are tributed into 天帝 埃忒耳 96570609; 六花 圣种之地灵 27520594 links 圣天树之幼精 93896655 into 茉莉 21200905 which tributes to summon 雪花莲 33491462
  - **End field**: monarch 天帝 96570609 plus 冥帝 厄瑞玻斯 23064604 with 真帝王领域 84171830 locking extra-deck summons; rikka 雪花莲 33779875 quick-tribute with 神树兽 许珀利冬 09349094 negate; floodgate fiends 虚无魔人 47084486 and 威光魔人 33746252 as one-tribute summons
  - **Weak point**: Ash the squire's summon or search, Veiler/Imperm the tribute summoner, remove the field-spell lock (真帝王领域 84171830, 来来 76869711), and 墓穴の指名者 24224830 on the grave squires cuts the second tribute
  - **Decks**: 帝 monarch 天帝从骑 爱迪娅 95457011, 六花 rikka 圣种之地灵 27520594

- **Using Engine Patterns**
  - Name the shape from the first one or two activations: which zones does the deck move cards between, does it re-link or overlay the same monster, does it float on destruction, does it run on set traps or equips or a single field spell
  - The shape predicts the combo: the one-card minimum is always the choke — negate that exact activation, hit the grave piece with 墓穴の指名者 24224830, and pick the zone-hate that matches the shape (次元吸引者 91800273 for pile decks, 古遗物圣枪 34267821 for banish decks, backrow removal for trap loops, Nibiru for summon-count ladders)
  - Each shape has a preferred kill: banish recursion fears 古遗物圣枪 34267821, float chains die to tribute or absorb removal, Xyz ladders die at the base monster, synchro ladders die at the token, and pendulum decks die at the scales
  - The mirror sections of the deck docs are really shape-versus-shape strategies: two decks sharing a shape share the same mirror rules, so learning one engine pattern teaches the mirror of every deck that uses it
