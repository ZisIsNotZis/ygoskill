---
name: mermail-atlantean-experience
description: 海皇水精鳞深海 (Mermail/Atlantean/Deep Sea) deck experience: discard-to-grave trigger engine, one-card combo, extenders, halt points
---
# 海皇水精鳞深海 (Mermail/Atlantean/Deep Sea) Deck Experience

- **Deck Identity**

- 海皇 (Atlantean) setcode 0x77: 海皇的狙击兵 706925, 海皇的重装兵 37104630, 海皇的龙骑队 74311226, 海皇的突击兵 8078366, 真海皇 特里冬 28754338, 海皇的咆哮 73199638
- 水精鳞 (Mermail) setcode 0x74: 水精鳞-邓氏深渊鱼 22446869, 水精鳞-深渊雀鳝兵 58471134, 水精鳞-萨拉深渊后 23545031, 水精鳞-深渊琳德 23899727
- 2025 support shares 深渊 setcode 0x75: 海皇子 尼普深渊王 21565445, 海皇精 深渊莱茵 17080584, 海皇精 深渊特里忒 9453320, 海皇龙神 波塞德拉·深渊 60517697, 轰海皇 波塞德拉 99193444, 水精鳞的深影队 53085623, 皇者水精鳞-尼普深渊王 69385019, 水精鳞-撼地深渊王 74371660
- 深海 (Deep Sea) engine: 深海歌后 78868119, 深海吟游诗人 71978434, 深海姬 首席女歌手 50793215, 深海艺术指导 33467872, 超古深海王 空棘鱼 88307361
- Modern coherent build is 海皇水精鳞深海 going 2nd, from deck folders 241026海皇水精鳞深海, 250927海皇水精鳞深海, 251220海皇水精鳞深海, 251220海皇水精鳞: board-break bounce plus OTK, not a going-1st combo deck
- Legacy cards 水精鳞-大蓝深渊鲸 75180828 and 绝海之马雷 31259606 are NOT in the modern build, they only appear in old 2018-2021 Mermail and Tearlaments decks; no card named 朗格 exists in this card DB

- **Core Mechanic: Discard-to-Grave Trigger Engine**

- Every classic 海皇 monster triggers when it is sent to the graveyard as cost for an activated WATER monster effect, verified in scripts as IsReason(REASON_COST) with an activated monster effect whose handler is WATER, for example c37104630.lua and c74311226.lua
- The trigger fires no matter where the card was sent from, hand, field, or deck, so deck-to-grave dumps count as long as they are cost, not effect
- Trigger payoffs: 重装兵 37104630 destroys 1 face-up opponent card, 龙骑队 74311226 adds 1 Sea Serpent from deck, 狙击兵 706925 destroys 1 set card, 尼普深渊王 21565445 second effect revives 1 海皇 monster from graveyard, 深影队 53085623 second effect special summons 1 level 4 or lower 海皇 or 水精鳞 from deck
- Effects that discard or send WATER as cost are the fuel: 邓氏深渊鱼 22446869 first effect, 深渊雀鳝兵 58471134, 轰海皇 99193444 both effects, 深渊莱茵 17080584 first effect release, 波塞德拉·深渊 60517697 first effect, 深影队 53085623 first effect, 饼蛙 90809975 negate (requires Aqua specifically)
- Effects that mill without cost do NOT trigger the engine: 深海吟游诗人 71978434 second effect mills 3 as effect, so it only sets up graveyard count, never pops or searches
- Level fixer: 深影队 53085623 first effect discards 1 card and makes all face-up WATER monsters on YOUR field level 7 until end of turn, enabling Rank 7 Xyz
- WATER locks: 深渊莱茵 17080584 first effect and 深影队 53085623 second effect forbid non-WATER extra deck special summons until end of turn, harmless for this all-WATER extra but it bans 共命之翼 迦楼罗 11765832 fusions
- Going 2nd the deck aims for exactly 5 WATER in graveyard to drop 冰灵神 穆兰格雷斯 13959634, whose summon discards 2 random cards from the opponent hand

- **One-Card Combo: 海皇子 尼普深渊王 21565445**

- Step 1: normal summon 尼普深渊王, activate first effect, cost sends 重装兵 37104630 from deck to graveyard which triggers and destroys 1 face-up opponent card, then search 海皇精 深渊莱茵 17080584 from deck
- Step 2: activate 深渊莱茵 17080584 first effect, release it from hand plus 尼普深渊王 from field, special summon 轰海皇 波塞德拉 99193444 from deck, or add it if no zone
- Step 3: 尼普深渊王 second effect is a mandatory trigger because it was released as cost for a WATER monster effect, special summon 重装兵 37104630 back from graveyard, and the released 重装兵 triggers again to destroy a second face-up card
- Step 4: 轰海皇 99193444 second effect on summon, cost sends 水精鳞的深影队 53085623 from deck which triggers and special summons 深渊雀鳝兵 58471134 from deck, then 雀鳝兵 discards 1 WATER and adds 深海吟游诗人 71978434 or 蝶泳鱼 58288565, and 轰海皇 bounces 1 opponent card to hand
- Step 5: 深影队 53085623 first effect discards 1 card, all own face-up WATER become level 7, Xyz 海皇精 深渊特里忒 9453320 with 轰海皇 and 雀鳝兵, its first effect revives 重装兵 from graveyard, its third effect detaches 1 and sets a 深渊 trap from deck, 深渊蒸集队 63941169 or 深渊唤雨 34707034
- Step 6: overlay 特里忒 into 海皇龙神 波塞德拉·深渊 60517697, the overlay method is once per turn on any 海皇 or 水精鳞 Xyz, detach 2 materials and send 1 WATER from hand or deck to graveyard, bounce up to 3 opponent cards to hand, and the sent WATER triggers its own 海皇 effect again if it is a 重装兵 or 龙骑队
- Net result from one card: destroy 2 face-up cards, bounce 4 cards, field a 3000 ATK Xyz, set a trap, and a graveyard stocked for 穆兰格雷斯 and 波塞德拉·深渊 graveyard revival
- 灰流丽 14558127 on step 1 kills the search but the 重装兵 dump cost still resolves, so the pop still lands

- **End Field**

- Going 2nd push: 波塞德拉·深渊 60517697 at 3000 ATK with bounce up to 3, 轰海皇 99193444 at 2800 ATK with its own bounce, 冰灵神 穆兰格雷斯 13959634 hand strip, plus direct attacks because 龙骑队 74311226 lets level 3 or lower Sea Serpents attack directly
- Going 1st fallback: 特里忒 9453320 at 2100 plus 300 per material with graveyard revive and trap set, 撼地深渊王 74371660 which stops level 5 or higher monsters from attacking and quick-negates opponent monsters below 2800 ATK, 皇者水精鳞-尼普深渊王 69385019 which protects linked WATER monsters from targeting and fetches 深渊刺器-三叉戟 81878201
- Synchro options: 冰结界之龙 三叉龙 52687916 banishes 1 each from opponent hand, field and graveyard, 冰灵山的龙祖 矛枪龙 96402918 summons 冰结界 monsters when the opponent special summons, 相剑大公-承影 96633955 banishes 1 field and 1 graveyard card, 魔救之奇迹-巨龙晶石 9464441 negates spell and trap activations, 白斗气一角 63731062 revives a Fish on summon, 瑚之龙 42566602 pops a card and draws on graveyard, 深海姬 首席女歌手 50793215 steals a banished opponent card and searches a level 4 or lower WATER
- Utility: 海善龙 33113958 is a Rank 3 that adds 善德激流弹 80534031 and recycles materials, 龙神鲨 440556 detaches to summon a Rank 3 or lower WATER Xyz from the extra deck, 深渊刺器-三叉戟 81878201 equips by reviving a 海皇 or 水精鳞 from hand or graveyard and later returns 3 Fish, Sea Serpent or Aqua to deck
- Floodgate: 豪雨之结界像 10963799 in some mains, both players may only special summon WATER monsters, effectively one-sided for this deck

- **Extenders**

- 深渊莱茵 17080584 second effect: on the opponent turn, banish it from graveyard and discard 1 card to draw 1, a free card every turn the engine fed the graveyard
- 邓氏深渊鱼 22446869: discard 1 other WATER from hand, special summon itself, then search any level 4 or lower 水精鳞 such as 雀鳝兵 or 深影队
- 深渊雀鳝兵 58471134: on normal or special summon discard 1 WATER to add any level 3 WATER from deck, 深影队, 吟游诗人, 蝶泳鱼 or 狙击兵
- 深海歌后 78868119: on normal summon special summon any level 3 or lower Sea Serpent from deck, 吟游诗人, 尼普深渊王 or 重装兵, the classic Deep Sea opener
- 深海吟游诗人 71978434: on special summon mills 3 for graveyard setup and returns a level 4 or lower WATER from graveyard to deck
- 超古深海王 空棘鱼 88307361: discard 1 card to special summon as many level 4 or lower Fish from deck as possible, negated and unable to attack, pure Xyz material generation
- 冰水帝 霓石精·海女神 18494511: discard 1 WATER to special summon itself plus a 冰水 token, WATER locked from the extra deck while the token lives
- 一对一 2295440 searches a level 1 WATER such as 尼普深渊王, 金满而谦虚之壶 84211599 digs while banning extra deck cards, 雪花之光 24940422 is a free draw for spell and trap only hands
- 善德激流弹 80534031 destroys 1 own Fish, Sea Serpent or Aqua and 2 opponent cards, and from graveyard it makes a monster WATER or protects a WATER monster once from effect destruction
- 海皇的咆哮 73199638: trap that revives 3 level 3 or lower Sea Serpents from graveyard but forbids ALL special summons the turn it activates, so only on the opponent turn or as a final push

- **Halt Points**

- 灰流丽 14558127 stops 尼普深渊王 21565445 first effect search, 深渊莱茵 17080584 first effect special summon, 深影队 53085623 second effect deck summon and 深海歌后 78868119 deck summon
- 小丑与锁鸟 94145021 stops deck to hand adds, hit 尼普深渊王 21565445 first effect or 深渊雀鳝兵 58471134 search
- 无限泡影 10045474 on 尼普深渊王 21565445 kills the whole line because every branch starts from its first effect
- 灵王的波动 40366667 is a hand trap that negates any special summoning effect, hit 深渊莱茵 17080584 first effect or 深影队 53085623 second effect, note the graveyard dump cost still resolves
- Activating 灵王的波动 40366667 from the hand locks you out of LIGHT, EARTH and WIND monster effects for the rest of the duel, which kills your own 幽鬼兔 59438930, 小丑与锁鸟 94145021 and 朔夜时雨 52038441 for the game
- 墓穴的指名者 24224830 and 抹杀之指名者 65681983 pre-empt the graveyard triggers, banishing 重装兵 37104630 or 龙骑队 74311226 before they pop or search
- Under 增殖的G 23434538 or 欢聚友伴·茸茸长尾山雀 42141493 stop after 轰海皇 99193444 bounce, 深影队 53085623 second effect and the 特里忒 9453320 chain feed multiple draws, play only 尼普深渊王 21565445 into 轰海皇 99193444 under G
- 幽鬼兔 59438930 hits 特里忒 9453320 Xyz and 撼地深渊王 74371660, 朔夜时雨 52038441 is a common counter in the mirror, 小丑与锁鸟 94145021 cripples the search heavy engine

- **Mirror Match: 海皇水精鳞 vs 海皇水精鳞**

- The mirror is a graveyard race, the first player whose 重装兵 37104630 pop or 龙骑队 74311226 search resolves sets the tempo, pre-empt with 墓穴的指名者 24224830 on 尼普深渊王 21565445 second effect revive
- 撼地深渊王 74371660 negates only monsters below its own 2800 ATK, so the 3000 ATK 波塞德拉·深渊 60517697 ignores it while 特里忒 9453320 at 2100 plus material boosts usually gets negated
- Bounce order matters, remove 特里忒 9453320 and 撼地深渊王 74371660 before they detach, and never destroy 波塞德拉·深渊 60517697 with destruction because its graveyard effect revives 3 level 3 or lower Fish, Sea Serpent and Aqua
- 深渊刺器-三叉戟 81878201 recycling decides the grind, the player who recycles 重装兵 37104630 and 龙骑队 74311226 first wins the long game
- Respect 豪雨之结界像 10963799 if the opponent mains it, your WATER-locked extra deck cannot play around it with non-WATER fusions

- **Common Mistakes**

- Do not expect 海皇 graveyard triggers from effect mills, only REASON_COST sends fire 重装兵 37104630, 龙骑队 74311226, 尼普深渊王 21565445 and 深影队 53085623
- Do not waste 重装兵 37104630 as a search dump, every cost dump of it should be a deliberate free pop
- 深影队 53085623 first effect only changes YOUR own face-up WATER levels, the script scopes the target to your field, it cannot level-fix opponent monsters for Rank 7
- 深渊莱茵 17080584 first effect releases itself from the HAND, it cannot release itself from the field, and both releases are the cost, so negating it still loses both monsters
- The WATER lock from 深渊莱茵 17080584 and 深影队 53085623 forbids non-WATER extra deck summons, never plan 超融合 48130397 into 共命之翼 迦楼罗 11765832 or 沼地的泥龙王 54757758 in the same turn
- 轰海皇 99193444 second effect pays its deck dump as cost, so even when negated by 灵王的波动 40366667 the graveyard setup resolves
- 特里忒 9453320 third effect only sets 深渊 setcode traps such as 深渊蒸集队 63941169 and 深渊唤雨 34707034, the 深渊鳞甲 equips are handled by 皇者水精鳞-尼普深渊王 69385019 instead
- 波塞德拉·深渊 60517697 overlay summon is once per turn and needs an existing 海皇 or 水精鳞 Xyz, keep 特里忒 9453320 with materials so the 2 material detach bounce is available
- 冰灵神 穆兰格雷斯 13959634 needs exactly 5 WATER in graveyard and skips your next Battle Phase when it leaves the field, do not summon it going first and fail to close the game
- 海皇的咆哮 73199638 forbids all special summons for the whole turn, it is not a mid-combo extender
- 龙神鲨 440556 cannot attack the turn it uses its effect and only summons Rank 3 or lower WATER Xyz such as 海善龙 33113958
