---
name: witchcrafter-experience
description: 魔女术 (Witchcrafter) deck experience: mechanics, one-card combo, extenders, halt points
---
# 魔女术 (Witchcrafter) Deck Experience

- **Deck Identity**

- Spellcaster fusion-control deck: bosses 玻璃女巫 21522601 and 服装女巫 84523092 backed by an end-phase spell recursion engine and fusion monsters 代理师傅 9603252, 学童组合 69964858, 桑德里永 33475154
- All archetype cards carry setcode 296 (0x128), verified in every script as c:IsSetCard(0x128); 结晶魔术 光之泪 73664385 and 恩底弥翁的侍女 玻璃 22623509 / 杰妮 07656689 also count as 魔女术 by rules (verified in datas setcode)
- Main monsters are all Spellcasters: 商标女巫 6071005 L6 DARK 2500/0, 玻璃女巫 21522601 L8 LIGHT 1000/2800, 服装女巫 84523092 L7 DARK 2400/1000, 锻造女巫 21744288 L4 FIRE 1800/600, 绘画女巫 95245544 L3 WIND, 万能杰妮 64756282 L1 WATER, 赤陶偶 70686400 and 陶器女巫 59851535 L2 EARTH, 宝石女巫 58139997 L5 LIGHT, 种子女巫 59106048 L4 WATER, 阿鲁鲁女神 71074418 L8 LIGHT 2800/0
- Key spells: 创造 57916305 monster search, 混乱融合 35098357 fusion, 庆祝会 6958567 destroy or fusion from grave, 演示 70226289 special summon from hand, 合作 10805153 double attack, 小巷 83289866 and 书卷 19673561 cost substitutes, 歪曲 69748261 counter trap, 圣夜行 32353566 field spell engine
- 光之泪 73664385 quick-play treated as 魔女术: each option once per turn, mill a Spellcaster or a Spell from deck, or when the opponent activates an effect special summon a 魔女术/大贤者 from hand or deck
- Extra deck: fusion 代理师傅 9603252 (2700/2800), 学童组合 69964858 (1800/2100), 桑德里永 33475154 (3800/2800), generic targets for 超融合 48130397 like 超魔导龙骑士 37818794 and 泥龙王 54757758; link options 塞勒涅 45819647, S:P 小夜骑士 29301450, I:P 百变莱娜 65741786
- 魔力统辖 38943357 searches any 恩底弥翁 card, which includes 恩底弥翁的侍女 玻璃 22623509 and 杰妮 07656689 (they carry both setcodes), making it an indirect 魔女术 searcher

- **Core Mechanic: Discard-a-Spell Costs and End-Phase Recursion**

- Every monster effect costs a Spell discard, verified in the shared costfilter of every script: discard a Spell from hand, or substitute it by sending face-up 小巷 83289866 or 书卷 19673561 from your S/T zone (once per turn each), or during your own turn send any other 魔女术 spell/trap from the DECK via 圣夜行 32353566
- Monsters with this cost: 服装女巫 84523092 pops a face-up card, 玻璃女巫 21522601 negates all opponent face-up monster effects until end of turn, 宝石女巫 58139997 special summons a 魔女术 from hand, and 锻造女巫 21744288 / 绘画女巫 95245544 / 陶器女巫 59851535 / 万能杰妮 64756282 release themselves plus the discard to special summon a 魔女术 from deck
- The four release-summon monsters are main-phase only (script spcon checks PHASE_MAIN1 or PHASE_MAIN2); 宝石女巫 58139997 has no phase lock
- The grind engine: at YOUR end phase, if you control a face-up 魔女术 monster, spells in the grave return to hand — 创造 57916305, 混乱融合 35098357, 演示 70226289, 合作 10805153, 裁剪 56894757, 怠工 83301414, 庆祝会 6958567 add themselves to hand, while 小巷 83289866 and 书卷 19673561 set themselves to your S/T zone (all scripts verified, EVENT_PHASE+PHASE_END, GetTurnPlayer==tp)
- Discarding and milling spells is setup, not card loss — the grave reloads every turn and the deck wins long games by out-recursing; banishment is the only thing that breaks the loop

- **One-Card Combo: 魔女的圣夜行 32353566**

- Step 1: activate 圣夜行 32353566 as the field spell
- Step 2: 圣夜行 ① adds 锻造女巫 21744288 from deck, then you discard 1 card from hand (a 魔女术 spell is best, it recurs at end phase)
- Step 3: normal summon 锻造女巫 21744288
- Step 4: main phase, 锻造女巫 ①: release it and pay the discard cost from the deck via 圣夜行 ② (send 创造 57916305 or 混乱融合 35098357 from deck to grave, never 圣夜行 itself), special summon 玻璃女巫 21522601 from deck
- Step 5: end phase the milled spell returns to hand because 玻璃女巫 21522601 is face-up
- Total special summons is one, so the line is nearly immune to 增殖的G 23434538
- Alternative search targets: 万能杰妮 64756282 (its grave effect ② banishes itself plus one 魔女术 spell and applies that spell's activation effect, so 混乱融合 35098357 or 创造 57916305 play from the grave), or 赤陶偶 70686400 (① from hand adds a 魔女术 from grave to hand and special summons itself, then ② is a built-in fusion summon)
- Two-card extension: 圣夜行 plus any 魔女术 card in hand — search 赤陶偶 70686400, discard a 魔女术 monster, 赤陶偶 ① recovers it and special summons itself, ② fuses it with the recovered monster into 学童组合 69964858, whose ① searches any 魔女术 spell
- Two-card starter: 创造 57916305 searches a monster, pair with any discardable spell to run the same release-summon line without 圣夜行

- **End Field One-Card**

- 玻璃女巫 21522601 plus 圣夜行 32353566 face-up plus one recurring spell in grave
- 玻璃女巫 21522601 ②: discard a spell (free from deck on your turn while 圣夜行 is up) to negate all opponent face-up monster effects until end of turn; ①: at damage calculation reveal any number of differently-named spells, the battling Spellcaster gains 1000 ATK/DEF each, so 合作 10805153 on it swings twice for big damage
- With the two-card extension the board adds 学童组合 69964858 (quick search or spell-copy on either turn) or 代理师傅 9603252, whose three quick options — destroy a card, special summon a level 6 or lower 魔女术 from hand or deck, recover a 魔女术 spell or trap from grave — each have their own once-per-turn limit and can be used whenever a non-fusion Spellcaster monster or Spell card effect activates, including the opponent's
- Backrow of choice: 歪曲 69748261 counter trap (negate and destroy, needs a face-up level 5 or higher 魔女术), 小巷 83289866 (protects each 魔女术 from destruction once per turn and acts as a cost substitute), 光之泪 73664385 ready to special summon from deck when the opponent activates an effect

- **Halt Points**

- 灰流丽 14558127 on 圣夜行 32353566 ① stops the one-card line cold, and on 锻造女巫 21744288 ① or 光之泪 73664385 stops the deck summons
- 墓穴的指名者 24224830 on the milled spell kills the end-phase recursion; on 万能杰妮 64756282 or 绘画女巫 95245544 in grave kills their grave effects
- 无限泡影 10045474 on 锻造女巫 21744288 before it releases, or on 玻璃女巫 21522601 before it negates, breaks the end board
- Destroying 圣夜行 32353566 (e.g. 宇宙旋风 8267140) forces every discard cost back to the hand and halves the engine
- Banish-heavy hate (次元吸引者 91800273, D.D. 乌鸦 24508238) empties the grave toolbox; 学童组合 69964858 ② and 守护圣者 94553671 ② are the recovery answers

- **Extender: 商标女巫 6071005**

- Ignition from hand or field: release itself, add 1 魔女术 field or continuous spell from deck — 圣夜行 32353566, 小巷 83289866, or 书卷 19673561
- Float: when your face-up 魔女术 monster leaves the field by the opponent's effect, special summon this card from grave and release 1 monster the opponent controls (script verifies rp equals opponent and REASON_EFFECT); if it leaves the field afterwards it is banished

- **Extender: 恩底弥翁的侍女 玻璃 22623509 / 杰妮 07656689**

- 玻璃 22623509: during your main phase of a turn a Spell card effect was activated, special summon it from hand; when special summoned, add 1 魔女术 spell or trap or 次元魔法 28553439 from deck
- 杰妮 07656689: if you control a Spellcaster, special summon it from hand; quick effect during either main phase: banish 1 Spellcaster you control, special summon a different 魔女术 from deck
- Both are searchable by 魔力统辖 38943357, and 杰妮 07656689's banishment feeds 守护圣者 94553671 ① and 庆祝会 6958567 option 2 (fusion using Spellcasters from grave or banishment, shuffled into the deck)

- **Extender: 守护圣者 94553671 continuous trap**

- Face-up quick effect: shuffle 1 Spellcaster from your grave or banishment into the deck, add 1 魔女术 spell from deck
- From the grave (not the turn it was sent): banish itself, add any number of your face-up banished 魔女术 spells (at most one of each name) to hand

- **Mirror Match: 魔女术 vs 魔女术**

- Both players run the same recursion engine, so the mirror is decided by who breaks the other's 圣夜行 32353566 first — 服装女巫 84523092 and 代理师傅 9603252 destroy it, and without it every discard cost must come from hand
- 玻璃女巫 21522601 ② is not targeting and hits the opponent's face-up monsters too; chain it to their 玻璃女巫 ② or to their 锻造女巫 21744288 release to stop the extension
- 服装女巫 84523092 protects your other Spellcasters from targeting but not itself — target the opponent's 玻璃女巫 21522601 directly, or 超融合 48130397 their monsters into 代理师傅 9603252 or 共命之翼 迦楼罗 11765832 (cannot be responded to)
- 歪曲 69748261 negates and destroys any activation including the opponent's 歪曲, so counter-trap chains decide who keeps the board
- The grind war favors whoever keeps spells in the grave instead of banishing them; 学童组合 69964858 ② and 守护圣者 94553671 ② punish the opponent's banish lines

- **Playing Under 增殖的G 23434538**

- The deck is naturally G-resistant: the 圣夜行 32353566 line is one special summon, and even the full release-summon extension is two or three
- Play the standard line under G and only skip the 赤陶偶 70686400 fusion extension, which pushes the summon count up
- 超融合 48130397 cannot be responded to at all, so the opponent cannot chain 增殖的G to its activation; if G is already face-up the fusion summon still draws, but the removal may still be worth one card

- **Common Mistakes**

- Do not banish spells from the grave carelessly: the entire recursion needs spells in the grave, and only 庆祝会 6958567 and 守护圣者 94553671 bring cards back from banishment
- 圣夜行 32353566 ② works only during your own turn, only while 圣夜行 stays face-up, and cannot send 圣夜行 itself — keep other 魔女术 spells in the deck to mill, or the costs revert to hand
- The four release-summon monsters 锻造女巫 21744288 / 绘画女巫 95245544 / 陶器女巫 59851535 / 万能杰妮 64756282 activate only in main phases — do not pass into battle phase expecting to extend
- 玻璃女巫 21522601 ② negates only the monsters that are face-up at resolution; monsters summoned or flipped afterwards keep their effects, so fire it in response to their plays, not at the start of a chain you cannot see
- 歪曲 69748261 needs a face-up level 5 or higher 魔女术: 玻璃女巫 21522601, 服装女巫 84523092, 商标女巫 6071005, 桑德里永 33475154 and 学童组合 69964858 qualify, 锻造女巫 21744288 and the other small monsters do not
- 桑德里永 33475154 ① locks you to fusion extra-deck summons for the turn and 赤陶偶 70686400 ① locks you to 魔女术 extra-deck summons — resolve link plays like 塞勒涅 45819647 or S:P 小夜骑士 29301450 before these
- 代理师傅 9603252 ① triggers on any non-fusion Spellcaster monster or Spell activation, including your own — pace your own activations so its three options are saved for the opponent's turn
- 绘画女巫 95245544 ② draws 1 then must send a 魔女术 from hand to grave, otherwise it banishes your whole hand face-up — only activate it with a 魔女术 in hand
- 演示 70226289's no-response protection covers your Spellcaster monster effect activations only, not your spell activations
- 大魔女 桑德里永 33475154 ② revives itself from grave during your end phase by revealing a Spell in hand — keep one spell in hand, or the 3800 body stays dead
