---
name: interruption-tactics
description: How to hold interaction against any opponent deck — read the engine early, pick the right choke, and sequence your hand traps by the engine shape
---
# Interruption Tactics: Reading and Breaking Any Deck

- Compiled from the Halt Points of the 110+ archetype docs in ygo/decks; the per-deck stop logic distilled into reusable rules
- The goal is not one "best Ash target" but a method: identify the engine shape in the first one or two activations, then apply the shape's choke logic (see [../card/catalog/enginepatterns.md](../card/catalog/enginepatterns.md) and [../card/catalog/summongeometries.md](../card/catalog/summongeometries.md) for the shapes)

- **Read the Engine Before You Interrupt**

- Watch the first one or two activations, name the zone traffic: is it dumping to grave, banishing itself, setting traps, making a token, equipping, or paying a discard cost?
- The one-card minimum is the choke every time: negate that exact activation and the whole line stalls, so hold your best interrupt for the known starter of the opponent's shape
- Distinguish search that CANNOT be negated from search that can: deck-banishes like 睡鼠① or 影依融合 44394295 deck-materials and 锻造女巫 forms are not Ash-able, while explicit "add to hand" searches are
- Note the lock the deck pays: token-locks (相剑/spright to Lv2), DARK-locks (orcust/phantomknights), Dragon-only-locks (tenpai), Fiend-locks (fiendsmith), Spellcaster-only-locks (mikanko) — if you force them past the lock they cannot recover, but they also cannot be stopped on those lines

- **Choose the Matrix: Which Choke Matches the Shape**

- Grave-engine (dump-to-grave fusion, orcust, tearlaments, thunderdragon): 墓穴的指名者 24224830 / D.D. 乌鸦 24508238 / 屋敷童 73642296 on the key grave piece before its trigger, 深渊的潜伏者 21044178 blanks every grave trigger, 次元吸引者 91800273 sends to banish
- Banish-engine (maliss, kashtira, some orcust lines): 古遗物圣枪 34267821 locks banishing outright, but 次元吸引者 91800273 is ASYMMETRIC — it fuels a maliss-style deck, use it only against grave-decks
- Trap-loop (labrynth, traptrix, altergeist, dinomorphia, eldlich): 王宫的敕命 61740673 / 魔封的芳香 58921041 shut the engine, backrow removal hits the searcher (塞拉 73639099, 白银之城的拉比林斯 2347656), and the grave re-set recursion dies to 次元吸引者 91800273
- Summon-count ladder (most combo decks): 原始生命态 尼比鲁 27204311 at the fifth summon, 增殖的G 23434538 taxing every step — as the combo-player, keep the summons under the Nibiru threshold when it is live
- Search-heavy (swordsoul, labrynth, most searchers): 小丑与锁鸟 94145021, 灰流丽 14558127 on the searcher
- Ritual/one-tribute (nekroz, voicelessvoice, monarch, drytron, rikka): stop the search chain (千手神 23401839, 万手神 95492061, 仪式的事前准备 13048472, 理 25801745) or the searcher-summoner, and hit the grave recycle with 墓穴的指名者 24224830
- Float-on-destruction (unchained, fireking): use tribute/absorb/banish removal (尼比鲁 27204311, 超融合 48130397, or absorb effects) so the float never triggers — destroying their cards feeds the chain
- Equip-engine (mikanko, nobleknight, dragunity): remove the EQUIPPED monster, not the equip — destroying the equip (水舞蹈, 圣剑) just re-equips or re-bounces; strip the monster or negate it so the equip has no carrier
- Xyz-overlay (zoodiac, madolche, exosister, galaxyeyes): kill the base monster before battle or negate the attack to deny the 阿宙斯 overlay; every material is a future negate/wipe charge
- Pendulum (qliphort, endymion, abyssactor, pendulummagician): 宇宙旋风 8267140 / 双龙卷 43898403 on the scales kills the summon range; endymion dies when its counter-bank field spell is removed
- Battle-Phase OTK (tenpai): the whole deck is a going-second swarm, so hand-trap the starters (灰流丽 14558127 on 灿幻开门 66730191, 灵王的波动 40366667 on the battle-phase synchro effects) and land 灿幻超龙 18969888-style locks BEFORE your own fifth summon
- Control/floodgate (skill drain, 神影依·米德拉什 94977269, 未来龙皇 霍普-style negate-stall, kashtira zone-locks, 御巫 reflect): the lock is the board, so the answer is removal that bypasses the immunity (non-targeting, tribute, absorb) or not letting the floodgate resolve in the first place

- **Sequence Your Interaction**

- Resolve your un-respondable plays first, then force the opponent into the window you control (see [engine-mechanics.md](engine-mechanics.md) spell speeds)
- Chain 灰流丽 to the activated effect, and 效果遮蒙者 97268402 / 无限泡影 10045474 to a monster already face-up — match the timing to the nature of the effect (activation vs on-field effect vs grave trigger)
- Save targeted removal (禁忌的一滴 24299458, or non-targeting tools) for the piece your hand traps cannot reach, and keep the 墓穴的指名者 24224830 / D.D.乌鸦 24508238 for the grave piece if both a search and a grave effect exist in the line
- When the opponent's engine is maxed (full combo), a single negate rarely wins; prioritize the floodgate or tower that must come down, then the engine, then the beaters

- **Under Increase-G Compromise**

- When 增殖的G 23434538 resolves against you, minimize special summons: make the one-card end (1 negate or 1 stall plus 1 standing monster) instead of the full line
- Some decks are naturally G-resistant: the 天杯龙 灿幻开门 66730191 line and 魔女术 圣夜行 32353566 line are one special summon; play them fully and only skip the extenders
- When it is YOUR 增殖的G 23434538, sequence so the opponent pays maximum draws for minimal chance to win — resolve it early and make them choose between stopping and handing you the game

- **Rule of Thumb: The Mirror Is the Shape Test**

- The mirror sections of the deck docs are shape-versus-shape strategies: two decks sharing an engine shape share the mirror rules, so mastering one engine pattern teaches the mirror of every deck that uses it (see [../card/catalog/enginepatterns.md](../card/catalog/enginepatterns.md))
- Vs an unknown deck, assume the most common shape for its archetype family (link ladder for Cyberse, grave-fusion for Fusion-pile, trap-loop for trap decks) and apply that choke until the line reveals a different shape

- **Hand-Trap Budget**

- Near-pure combo metas: 灰流丽 14558127 / 增殖的G 23434538 / 原始生命态 尼比鲁 27204311 / 小丑与锁鸟 94145021 front-loaded, 9 to 12 total
- Control metas: keep 效果遮蒙者 97268402 / 无限泡影 10045474 and backrow removal over 灰流丽
- Dedicated sideboard answers: 古遗物-圣枪 34267821 (banish), 王宫的敕命 61740673 (trap), 魔封的芳香 58921041 (spell lock), 次元障壁 83326048 (one summon type), 御前试合 53334471 / 群雄割据 90846359 in the current format
