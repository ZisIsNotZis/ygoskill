---
name: salamangreat-experience
description: 转生炎兽 (Salamangreat) deck experience: re-link reinforce loop, one-card combo, extenders, halt points
---
# 转生炎兽 (Salamangreat) Deck Experience

- **Deck Identity**

- FIRE Cyberse archetype with setcode 281 (0x119), sourced from near-pure corpus lists 220611转生炎兽, 240727转生炎兽, and 210116转生炎兽
- Main engine: 羚羊 26889158 (dump from deck), 犰狳蜥 52277807 (self-revive), 灯火美洲豹 56003780 (GY recursion), 狐狸 94620082 (topdeck search), 猎鹰 20618081 (bounce and set), 蜃景雄马 87327776 (Rank 3, deck special), 炽焰转生炎兽小妖 11962031 (search)
- Core links: 烽火猞猁 14812471 (Link 1, searches the field spell), 日光狼 87871125 (Link 2, re-link target), 炽热多头狮 41463181 (Link 3, S/T shuffle), 火凤凰 31313405 and 烈火凤凰 57134592 (Link 4 finishers)
- Key spells: 圣域 1295111 (field spell enabling re-link), 炎阵 52155219 (searcher), 愤怒 14934922 (quick destroy), 复活 19027895 (GY revive); key traps: 咆哮 51339637 (counter), 意志 64178424 (mass revive)
- Non-archetype core: 调试瓢虫女郎 16188701, 帧缓存火牛 80794697, 并行超限龙 71278040, 转码语者 46947713, 访问码语者 86066372, 双穹之骑士 阿斯特拉姆 21887175
- Modern lists (240727) add 赐炎之咎姬 2772337, 世海龙 西兰提斯 45112597, 灼热之火灵使 希塔 48815792, 炎星侯-马信 74168099, 解码语者·炽热之魂 61245672, 飞溅闪屏法师 59859086
- Spliced variants: Flame Admin 炎上框架管理员 49847524 (Link 2, all your links gain 800 ATK) appears in 191221 and 200111 lists; a full @火灵天星 Cyberse package appears in 250125转生炎兽@火灵天星 (see splice section)

- **Core Mechanic: Re-Link Reinforce Loop**

- 圣域 1295111 ① lets you link summon a 转生炎兽 link monster using only 1 same-name 转生炎兽 link monster on your field as material, verified in script c1295111 as a granted extra link procedure on extra deck monsters
- Re-linking 日光狼 87871125 into itself via 圣域 makes its ② live: add 1 转生炎兽 spell or trap from GY to hand, because ② requires 日光狼 used as material, verified in c87871125 valcheck
- 日光狼 ① gives card advantage: when a monster is special summoned to a zone it points to, add 1 FIRE monster from GY to hand, but that monster and its namesakes cannot be summoned this turn
- 灯火美洲豹 56003780 ② is the reinforcement piece: in GY, shuffle 1 other 转生炎兽 monster from GY into the deck and special summon itself to a zone a 转生炎兽 link points to, which triggers 日光狼 ① for a free card
- The cycle: special 美洲豹 to 日光狼 zone, 日光狼 adds a FIRE monster, use 美洲豹 as link material, repeat every turn for permanent hand and link advantage
- 犰狳蜥 52277807 ② self-revives from GY while a face-up 转生炎兽 is on field, and 羚羊 26889158 ① self-revives from hand whenever another 转生炎兽 monster is sent to your GY
- 烽火猞猁 14812471 ① on link summon searches 圣域 1295111 from deck, and can banish itself from GY once to save a 转生炎兽 monster from destruction
- 圣域 ② is a battle trick: pay 1000 LP during your monster's damage calculation, target 1 link monster, its ATK becomes 0 and you gain LP equal to its original ATK

- **One-Card Combo: 羚羊**

- Starter: 羚羊 26889158 in hand, no other cards required
- Step 1: normal summon 羚羊, its ② sends 犰狳蜥 52277807 from deck to GY
- Step 2: 犰狳蜥 ② special summons itself from GY because 羚羊 is face-up on field
- Step 3: link 羚羊 into 烽火猞猁 14812471, its ① adds 圣域 1295111 from deck to hand
- Step 4: activate 圣域, then link 犰狳蜥 and 烽火猞猁 into 日光狼 87871125
- Step 5: 犰狳蜥 ② revives itself again from GY to 日光狼 linked zone, triggering 日光狼 ① to add a FIRE monster such as 羚羊 back to hand
- Step 6: use 圣域 ① to re-link 日光狼 with only itself as material, enabling 日光狼 ② to recycle 转生炎兽 spell or trap from GY, or link into 炽热多头狮 41463181 to shuffle an opponent S/T
- Step 7: on later turns 灯火美洲豹 56003780 from GY specials itself to the 日光狼 zone, triggering another 日光狼 ① card gain, keeping the reinforcement loop live each turn
- Variant with 蜃景雄马 87327776: Xyz 羚羊 and 犰狳蜥 into it, detach 1 to special 灯火美洲豹 from deck, then link both into 日光狼 so 美洲豹 lands in GY for the loop immediately and 蜃景雄马 ② bounces a monster
- End state: re-linked 日光狼 with set 愤怒 14934922 or 咆哮 51339637, 圣域 on field, plus a FIRE monster in hand from the loop

- **End Field**

- 日光狼 87871125 re-linked via 圣域 1295111 as the anchor, plus one set 转生炎兽 trap 咆哮 51339637 or 意志 64178424
- Classic pure end: 炽热多头狮 41463181 (shuffles opponent S/T on summon) over 日光狼, with 圣域 and 愤怒 14934922 ready
- 愤怒 14934922 ② uses a re-linked link to destroy up to its link rating number of opponent cards, and 咆哮 51339637 counters monster effects or activations while a 转生炎兽 link is face-up
- Modern 240727 end: 赐炎之咎姬 2772337 (revives FIRE from GY, self-revives and destroys on opponent special) plus 日光狼 and 圣域, or 世海龙 西兰提斯 45112597 to wipe and re-summon the board
- OTK line: 访问码语者 86066372 climbed over 转码语者 46947713 with 更新干扰员 88093706 for double attacks and non-responding destruction
- 烈火凤凰 57134592 is the ember recursion end: re-linked it searches any 转生炎兽 card, and in GY it revives itself whenever your FIRE monster is destroyed, gaining that monster's ATK

- **Extenders**

- 蜃景雄马 87327776: Rank 3 over two Level 3s, detach 1 to special any 转生炎兽 from deck in defense, and when an Xyz-summoned one is link material it bounces a monster on the field
- 猎鹰 20618081: in GY bounces a face-up 转生炎兽 you control to hand to special itself, and when sent to GY sets 1 转生炎兽 spell or trap from GY
- 狐狸 94620082: on normal summon reveals top 3 and adds 1 转生炎兽 card; in GY discards 1 转生炎兽 to revive itself and destroy 1 face-up S/T
- 炽焰转生炎兽小妖 11962031: on summon adds any Level 4 or lower 转生炎兽 from deck, but locks you to FIRE monsters only for the rest of the turn
- 帧缓存火牛 80794697: when face-up on field leaves, discard 1 Cyberse to draw 2, converting dead 转生炎兽 into gas
- 调试瓢虫女郎 16188701: on summon adds any Level 3 or lower Cyberse from deck, fetching 羚羊 or 犰狳蜥
- 并行超限龙 71278040: after any link summon specials itself from hand to the linked zone, then specials another from deck, making Level 4 bodies for Xyz or link climbs
- 转码语者 46947713: revives a Link 3 or lower Cyberse link from GY to its zone and gives 500 ATK plus target protection while co-linked
- 转生炎兽的超转生 54529134: quick-play that re-links one 转生炎兽 link into a same-name link without 圣域, one per turn
- 转生炎兽的炎虞 28534130: specials a 转生炎兽 from hand with effects negated and immediately link summons over it, and in GY returns a 转生炎兽 link from GY to extra deck
- 炽焰飞腾 66947913: with no monsters revives 1 FIRE from GY and equips itself for 500 ATK, and banishes a card when destroyed by opponent effect

- **Flame Admin and @火灵天星 Splice**

- Flame Admin 炎上框架管理员 49847524 boosts all your link monsters by 800 ATK while on field, turning 日光狼 into 2600 and 炽热多头狮 into 3100 for cheaper OTKs in 191221 and 200111 pure lists
- The @火灵天星 package in 250125 lists replaces the pure hand-trap shell with a Cyberse engine: 微码编码员 2347477 (hand link material for 码语者 and searches 电脑网 S/T), 辣辣妖@火灵天星 15808381, 闪闪妖@火灵天星 16020923, 备份员@火灵天星 30118811
- It adds 暗幼童@火灵天星 74567889 (searches 火灵天星“艾”心乐园岛 59054773), 暗骑士@火灵天星 97383507 (revives @火灵天星 to its zones), and 协心代码语者@火灵天星 39138610 (negate and banish on opponent effect)
- Finishers in the splice: 电子界小男巫 52698008 (destruction immunity), 防火龙·暗流体 64211118 (battle-phase negation and multi-attack), "艾"宝-搭档 91509824 (negate effects, revive banished Cyberse), 不期而遇-妨"艾"- 6552971 (search)
- The splice keeps the 转生炎兽 core of 羚羊, 犰狳蜥, 美洲豹, 日光狼 and 圣域 but adds a DARK Cyberse engine, so 圣域 ② and the re-link loop still drive the deck

- **Halt Points**

- 灰流丽 14558127 stops the opener: it negates 羚羊 ② deck-to-GY dump, 烽火猞猁 ① search, 调试瓢虫女郎 16188701 search, and 狐狸 94620082 topdeck search
- 增殖的G 23434538 punishes the whole line because 犰狳蜥, 美洲豹, and every link summon specials; stop after 日光狼 plus one set if 增殖的G resolves
- 原始生命态 尼比鲁 27204311 lands after five summons, right before or at the re-link step, tributing the field including the re-linked 日光狼
- 无限泡影 10045474 on 羚羊 ② or on the 日光狼 re-link stops the engine cold
- 墓穴的指名者 24224830 or 抹杀之指名者 65681983 on 犰狳蜥 or 灯火美洲豹 in GY kills the recursion loop, since both recycle from GY
- 次元吸引者 91800273 or any GY banish wrecks the deck because the whole loop depends on GY monsters
- 御前试合 53334471 and 群雄割据 90846359 lock pure lists out of non-FIRE 转码语者 and 访问码语者 climbs, but the splice is even more vulnerable since @火灵天星 monsters are mostly DARK

- **Mirror Match: 转生炎兽 vs 转生炎兽**

- Race to re-link 日光狼 87871125 first: the first player whose 日光狼 ② is live can recycle 愤怒 14934922 or 咆哮 51339637 each turn
- 圣域 1295111 ② wins damage races: pay 1000 to drop the opponent re-linked 日光狼 to 0 ATK and gain its 1800 LP during your attack
- 炽热多头狮 41463181 ① shuffles the opponent's S/T into the deck, removing their set 愤怒 or 咆哮 before it resolves
- 愤怒 14934922 ② on a re-linked 炽热多头狮 destroys up to three of the opponent's cards, and 咆哮 51339637 negates the opponent's monster effects
- Whichever player keeps more FIRE monsters in GY wins the 灯火美洲豹 56003780 recursion war, so 墓穴的指名者 24224830 is the highest-value mirror card
- 访问码语者 86066372 over 转码语者 46947713 with 更新干扰员 88093706 is the standard mirror finisher because both players play through the same engine

- **Common Mistakes**

- Do not normal summon before 羚羊 26889158 unless 犰狳蜥 52277807 or 帧缓存火牛 80794697 needs the extra body, the opener wants 羚羊's ② dump to resolve first
- 日光狼 87871125 ① lock applies to the added monster and its namesakes for the whole turn, never plan to summon the card 日光狼 just added
- 犰狳蜥 52277807 special summoned by its ② effect is banished when it leaves the field, so do not use it as Xyz material if you need it again
- 蜃景雄马 87327776 ① locks you out of non-FIRE monster effects for the turn, so use 转码语者 and 访问码语者 only after resolving it
- 炽焰转生炎兽小妖 11962031 locks you to FIRE-only special summons for the turn, so it cannot start the 转码语者 climb
- 炽焰狂怒 92345028 specials monsters with negated effects and limits you to one extra deck summon, use it as a combo fallback not mid-line
- 狐狸 94620082 only adds 1 转生炎兽 card from the revealed 3, and 羚羊's dump is a hard once per name per turn, sequence the searches before committing
- 圣域 1295111 ② pays 1000 LP during damage calculation and drops a link monster to 0 ATK, it is a life-gain battle trick, not removal
- Set 咆哮 51339637 or 意志 64178424 instead of holding them in hand, 猎鹰 20618081 and 日光狼 ② both recur traps from GY, while 咆哮 ② even re-sets itself from GY when a re-linked link appears
- 转生炎兽的意志 64178424 ② sends itself to GY as cost and specials up to the target link's rating of 转生炎兽 in defense, leaving the trap in GY for 日光狼 recursion
