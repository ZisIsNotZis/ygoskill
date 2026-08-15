---
name: rikka-experience
description: 六花 (Rikka) deck experience: tribute engine, 圣种 Sunseed line, one-card combo, extenders, halt points
---
# 六花 (Rikka) Deck Experience

- **Deck Identity**

- Reference build: deck dir `260124六花圣种之原石的蕾祸`, a modern near-pure Rikka tribute deck (Rikka + 圣种/Sunseed + 原石/Primite + 蕾祸/Ragnaraika bodies)
- Rikka monsters: 六花精 雪花莲 33491462, 六花精 樱草 08129306, 六花精 叶牡丹 71002019, 六花的白姬 00132308, 六花的一瓣 71734607
- Xyz bosses: 六花圣 泪滴花束雪花莲 33779875 (Rank 8), 六花圣 力量女神花圈 03828844 (Rank 4), 六花圣 花簪剑菊 06284176 (Rank 6), 神树兽 许珀利冬 09349094 (Rank 9)
- Engine: 圣种之地灵 27520594, 圣天树之幼精 93896655, 圣蔓的播种 53286626, 圣蔓之治愈者 65563871, 芳香炽天使-茉莉 21200905
- Support: 蕾祸之毬首 99153051, 蕾祸之矢筈天牛 26548709, 蕾祸缭乱狂咲 04841383, 蕾祸之武者髑髅 43129357, 血树龙姬 龙血树鬼 79966218
- Primite package: 原石的皇脉 56506740, 原石的穿光 29095457, 原石的鸣狞 92501449
- Server quirk, verified in cards.cdb: levels differ from official OCG, 六花精 雪花莲 is Level 8 here (OCG Level 4), 六花的白姬 is Level 4 (OCG Level 8), 六花精 仙客来 34614910 is Level 4 (OCG Level 1); plan every Xyz line around the server levels

- **Core Mechanic: The Tribute Engine**

- Every payoff runs on tributing Plants; one tribute can trigger a whole wave: 樱草 ① special summons itself from hand, 欧石楠 07407724 ② revives from grave, 仙客来 34614910 ② revives at the end phase of the turn it was tributed, 六花的风花 96162588 ① forces the opponent to tribute a monster, 泪滴花束雪花莲 ② gains ATK per tribute, 花簪剑菊 ① revives a monster from either grave; 欧石楠 and 仙客来 are archetype members not in the reference list but keep the same wave when sided in
- 六花来来 76869711 (field spell) ②: once per turn, when a 六花 card effect would tribute your Plant as a cost, tribute 1 face-up opponent monster instead; verified as EFFECT_EXTRA_RELEASE_NONSUM on the opponent field in every cost filter (雪花莲 ①, 叶牡丹 ①, 绚烂, 薄冰, 深深, 白姬 ②, 铁筷子 60880471)
- 泪滴花束雪花莲 33779875 ①: detach 1 material, tribute 1 monster on either field; only an ignition effect while it has no Plant material, but a quick effect usable on the opponent turn while it has Plant material; always Xyz it with a Plant material so it is the opponent-turn interrupt
- 来来 ② only redirects tribute COSTS, never 泪滴's tribute which is an effect, and only once per turn
- The tribute-lock: strip the opponent board by tributing their monsters (泪滴 quick tribute, 薄冰 control steal, 风花 mirror tribute, 来来 cost redirect) instead of destroying, dodging destruction protection and negated-effect boards
- 六花的薄冰 68941332: negate one face-up monster's field-activated effects for the turn; the tribute version also steals control until the end phase and makes it Plant

- **Core Mechanic: the 圣种 (Sunseed) Engine**

- 圣种之地灵 27520594 (Level 1 Normal Plant) is the engine access; link it into 圣天树之幼精 93896655 which searches 圣蔓的播种 53286626 when summoned with 圣种之地灵 in the extra monster zone
- 播种 53286626: special summon one 圣种 monster from deck and take 1000 damage; only 圣种之地灵 unless you control a 圣天树 link; after activation you may only special summon Plants from the extra deck this turn
- 幼精 ③ heals the damage and special summons 圣蔓之治愈者 65563871 from the extra deck; 治愈者 ② heals 300 per link marker of a 圣天树 link it points to
- Link 幼精 and 圣种之地灵 into 芳香炽天使-茉莉 21200905; 茉莉 ② tributes a monster in its linked zone to special summon any Plant from deck; 茉莉 ③ adds a Plant from deck whenever you gain LP
- Everything the engine summons is Plant, so it respects every Plant-only lock the deck applies

- **One-Card Combo: 圣种之地灵 Engine Access**

- One card gets the engine going: normal summon 圣种之地灵 27520594, or fetch it with 一对一 02295440, 孤火花 48686504, 圣蔓的播种 53286626, or 原石的皇脉 56506740 ③ (declaring 圣种之地灵 is free because a Normal monster has no effects to lock)
- Step 1: normal summon 圣种之地灵 27520594, link into 圣天树之幼精 93896655 in the extra monster zone, ① adds 圣蔓的播种 53286626
- Step 2: activate 播种, special summon 圣种之地灵 second copy from deck, take 1000 damage, 幼精 ③ heals it back and special summons 圣蔓之治愈者 65563871
- Step 3: link 幼精 and 圣种之地灵 into 芳香炽天使-茉莉 21200905
- Step 4: 茉莉 ② tributes 治愈者, special summons 六花精 雪花莲 33491462 from deck in defense
- Baseline end of a pure one-card line: 茉莉 plus 雪花莲 (Level 8 on this server) with no Xyz yet; 雪花莲 ② can make every Plant Level 8 but needs a second body on field to Xyz with
- The full endboard needs one more Plant body, and the standard partner is 樱草 08129306 or 白姬 00132308 in hand, see the two-card line below

- **Two-Card Line: 圣种之地灵 + 樱草/白姬/毬首**

- 樱草 08129306 is the free partner: it special summons itself from hand whenever any of your monsters is tributed, so it lands for free off the 治愈者 tribute in step 4
- With 樱草 on field, 雪花莲 ② targets itself (Level 8 on this server) and makes all your Plants Level 8, then Xyz 雪花莲 plus 樱草 into 泪滴花束雪花莲 33779875 with Plant material
- 白姬 00132308 works the same way from hand via its ① self special summon, and stays available in hand or grave for its ② monster-effect negate
- 蕾祸之毬首 99153051 works as the body: discard a Plant to special summon it, then ② adds two 蕾祸 cards from deck; it becomes Xyz material for 泪滴 after 雪花莲 ②
- Alternative Jasmine 21200905 target: 叶牡丹 71002019 instead of 雪花莲 when the Rank 8 cannot be finished (e.g., under 增殖的G 23434538); 叶牡丹 ② adds 六花绚烂 69164989 or 六花来来 76869711 to keep the follow-up live

- **End Field**

- 茉莉 21200905 plus 泪滴花束雪花莲 33779875 with Plant material, ready to quick-tribute one opponent monster per turn
- 六花来来 76869711 active with a set 六花的薄冰 68941332 or 六花深深 32557233 from deck, and 六花的一瓣 71734607 in grave reviving at the opponent end phase for a free next-turn body
- 白姬 00132308 in hand or grave: pay a Plant tribute plus return itself to deck to negate an opponent monster effect
- Upgrade path: Xyz 力量女神花圈 03828844 from two Level 4 monsters, then tribute it while it has material (雪花莲 ① cost, 叶牡丹 ① cost, or 孤火花) to trigger ② and special summon 神树兽 许珀利冬 09349094, which negates and destroys an opponent effect on their turn by detaching a matching-type material
- Halt point: the line needs 播种, 幼精 search, and 茉莉 ② to all resolve; Ash Blossom 14558127 on any of them caps the board at 茉莉 or earlier

- **Extenders**

- 六花的一瓣 71734607 is a monster, not a spell: ① adds or mills one 六花 monster from deck (Plant-only lock after), ② revives itself from grave at the opponent end phase while your field is empty or all Plant
- 六花绚烂 69164989: add one 六花 monster; the tribute version (pay one Plant) also adds a different-name Plant of the same original level, so 雪花莲 33491462 grabs 铁筷子 60880471 (both Level 8 on this server) or 叶牡丹 71002019 grabs 欧石楠 07407724 (both Level 6)
- 六花深深 32557233: revive one 六花 monster from grave, and with a Plant tribute also revive another Plant
- 蕾祸之毬首 99153051: discard one Insect/Plant/Reptile to special summon itself, then search up to two 蕾祸 cards from deck or banished and banish one hand card; locks you to Insect/Plant/Reptile special summons
- 蕾祸之矢筈天牛 26548709: special summons itself by returning a banished Insect/Plant/Reptile to the bottom of the deck, and revives a Level 4 or lower Insect/Plant/Reptile when used as 蕾祸 link material
- 蕾祸缭乱狂咲 04841383 (continuous spell): 300 ATK/DEF to Insect/Plant/Reptile and minus 300 to everything else; ② searches a 蕾祸 monster or special summons one from hand, grave, or banished
- 蕾祸之武者髑髅 43129357: link-2 revives a 蕾祸 from grave; in grave it returns an Insect/Plant/Reptile to deck to special summon itself; using either locks you to Insect/Plant/Reptile
- 血树龙姬 龙血树鬼 79966218: mill a Level 4 or lower Plant from deck as cost, special summon itself with the milled monster level, Dragon/Plant-only special summon lock after; its ② Dragon revive is dead in this build because there are no Dragons
- 圣种之影芽 30013902: in grave, banish itself and target a linked 圣天树/圣蔓 link-2 or lower to special summon the same-name card from the extra deck with negated effects, Plant-only lock after
- 森罗的舞蹈娘 先锋葡萄 21903613: on link summon excavate up to three cards, special summon up to two Plants among them, send the rest to grave; those special summoned monsters cannot be used as link material
- 原石的穿光 29095457: quick-play, reveal a 原石 card or a Normal monster from hand to negate and banish any face-up card; no reveal needed while you control a Normal monster
- 原石的皇脉 56506740 ③: declare 圣种之地灵 and special summon it from deck, grave, or hand in defense, free because a Normal monster cannot activate effects

- **Playing Under 增殖的G and 欢聚友伴**

- The full line special summons six or more times, so while 增殖的G 23434538 or 欢聚友伴·茸茸长尾山雀 42141493 is active, stop at 茉莉 21200905 plus one body and set 薄冰 68941332 or 来来 76869711
- The deck carries 墓穴的指名者 24224830 and 抹杀之指名者 65681983 to answer 增殖的G or 灰流丽 14558127 mid-combo, chain them before extending
- 尼比鲁 27204311 hits around the fifth summon, right before 泪滴; hold 抹杀之指名者 or end the line one step early rather than losing the whole board

- **Mirror Match: 六花 vs 六花**

- The mirror is a tribute race: whoever lands 泪滴花束雪花莲 33779875 first with Plant material dictates the game with quick tributes
- Kill the engine first: negate 播种 53286626, 幼精 93896655 search, or 茉莉 21200905 ② with 灰流丽 14558127, or stop 雪花莲 ② with 无限泡影 10045474 before the Rank 8 forms
- 六花的薄冰 68941332 negates the opponent 雪花莲 or 茉莉, and the tribute version steals control of one monster until the end phase
- 六花的风花 96162588 forces the opponent to tribute a monster every time your 六花 is tributed, but it also feeds their 樱草 08129306 hand triggers, so sequence tributes carefully
- 来来 76869711 ② redirects your tribute costs to the opponent monster, so tribute their 雪花莲 or 白姬 as cost instead of your own Plants

- **Common Mistakes**

- Plan Xyz around the server levels, not OCG: 雪花莲 33491462 is Level 8 and 白姬 00132308 is Level 4 on this server, so Rank 4 (力量女神花圈 03828844), Rank 6 (花簪剑菊 06284176), and Rank 8 (泪滴花束雪花莲 33779875) all come from different material pairs than the official combos
- 六花的一瓣 71734607 is a Level 1 monster, not a spell, and its ① only works from the field, so it needs a summon first
- Respect the locks: after 毬首 ②, 雪花莲 ①, 一瓣 ①, 来来 ①, 影芽 ②, 播种, or 血树龙姬 ① you cannot special summon non-Plants (or non-Insect/Plant/Reptile), so 灰流丽 14558127, 屋敷童 73642296, 小丑与锁鸟 94145021, 尼比鲁 27204311, and 欢聚友伴 42141493 become unsummonable mid-line
- 播种 53286626 locks extra deck special summons to Plants for the turn; every extra deck monster in the build is Plant so this is safe only if you never go into non-Plant extras
- Never Xyz 泪滴 without a Plant material or you lose its quick effect on the opponent turn
- 风花 96162588 destroys itself at the opponent end phase while a non-Plant monster is face-up on your field
- 先锋葡萄 21903613 excavated monsters cannot be link material, so do not plan a second link climb on them
- 影芽 30013902 resurrects the target link with negated effects, so a resurrected 幼精 or 治愈者 does not search or heal
- 来来 ② is once per turn and only covers cost releases of 六花 effects; 泪滴's tribute is an effect and is not redirected
- 血树龙姬 ② is dead without a Dragon, and 原石的鸣狞 92501449 ② needs a Normal monster with higher ATK than the target, which 圣种之地灵 27520594 (0 ATK) rarely provides
