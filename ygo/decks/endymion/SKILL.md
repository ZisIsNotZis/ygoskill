---
name: endymion-experience
description: 恩底弥翁 (Endymion) deck experience: spell-counter pendulum engine, openers, extenders, halt points
---
# 恩底弥翁 (Endymion) Deck Experience

- **Deck Identity**

- Pendulum Spell Counter hybrid: no fixed combo, an accumulator deck that banks Spell Counters from Spell activations and spends them through pendulum monsters into a board of negates and Link bosses
- Reference builds analyzed from the deck folder: the classic 恩底弥翁魔导兽 (Endymion + Mythical Beast) lists and the 2025-26 support build
- Bosses: 创圣魔导王 恩底弥翁 3611830 (pendulum scale 8, Level 7) and the older 神圣魔导王 恩底弥翁 40732515
- Pendulum core: 恩底弥翁的仆从 92559258 (scale 2), 恩底弥翁的统领 66104644 (scale 8), 恩底弥翁的皇后 39000945 (scale 2)
- Spell counter engine: 魔法都市 恩底弥翁 39910367 (the field spell the player called 恩底弥翁的圣殿), 魔力统辖 38943357, 魔力到达 39123673, 魔力掌握 75014062, 魔导加速 38325384, 魔法都市的实验设施 65342096
- Mythical Beast (魔导兽) counter engine: 刻耳柏洛斯尊主 53842431, 胡狼王 27354732, 胡狼 91182675, 迦楼罗 28570310, field spell 魔导研究所 94599451
- 2025-26 support engine: field spell 恩底弥翁皇国 34041788, 圣月之皇太子 雷古勒斯 96228804, Link-2 圣月之魔导士 恩底弥翁 20714553, maids 恩底弥翁的侍女 杰妮 7656689 and 玻璃 22623509 (also count as 魔女术), 圣魔 裁决之雷 59080 (counts as 大贤者 and 恩底弥翁)
- Extra deck core: 神圣魔皇后 塞勒涅 45819647, 刚炼装勇士·银金公主 24094258, 访问码语者 86066372, 异色眼风雷龙 53262004, 轨迹之魔术师 22125101
- Note: no card named 霸风之帝国 恩底弥翁 exists in cards.cdb, checked by name, by the 恩底弥翁 setcode 298, and by cards whose text mentions 恩底弥翁; treat that name as unverified and play the verified finishes above

- **Core Mechanic: Spell Counter Accumulation**

- Every Spell Card activation, yours or the opponent's, banks counters: +1 on 仆从 92559258, 统领 66104644 and 皇后 39000945 in the Pendulum Zone, +1 on 魔法都市 恩底弥翁 39910367 and 魔法都市的实验设施 65342096, +2 on Mythical Beasts 刻耳柏洛斯尊主 53842431 and 胡狼王 27354732, +1 on 胡狼 91182675 and 迦楼罗 28570310, verified in scripts c92559258, c39910367 and c65342096
- 魔法都市 恩底弥翁 39910367 is the counter bank: counters of destroyed counter-bearing cards move to it, once per turn it pays counter costs for your other cards, and it survives destruction by spending 1 counter
- Pendulum scale setup: 仆从 92559258 and 皇后 39000945 are scale 2, 统领 66104644 and 创圣魔导王 3611830 are scale 8, so a 2/8 pair pendulum summons levels 3 to 7
- Counter dump effects: 仆从 pays 3 counters to special summon itself from the Pendulum Zone plus a counter-capable monster with ATK 1000 or more from deck; 统领 pays 3 to special summon itself plus a face-up counter-capable pendulum from the Extra deck, which needs a free Extra Monster Zone; 皇后 pays 3 to special summon itself plus a counter-capable monster from hand; 创圣魔导王 pays 6 to special summon itself and destroy up to your number of counter-capable cards, gaining counters equal to the destructions
- 魔力统辖 38943357 searches any 恩底弥翁 card from deck, then places up to your face-up or graveyard count of 魔力统辖 plus 魔力掌握 75014062 copies of counters, one at a time
- 魔力掌握 75014062 places 1 counter on a counter-capable card then searches another 魔力掌握, chaining itself into a counter battery
- 魔力到达 39123673 adds any card whose text mentions 魔力指示物 (Spell Counter) from deck or grave; with a Level 7 or higher 恩底弥翁 monster on field it removes any number of counters to negate and destroy that many opponent face-up cards
- 魔导加速 38325384 mills 2 and places up to 2 counters, and if the opponent destroys it, it special summons a counter-capable monster from deck with up to 2 counters

- **One-Card Combo**

- No true one-card combo exists: the deck is an accumulator, its plays need 2-3 cards and Spell activations to bank counters
- Closest solo starter: activate 恩底弥翁皇国 34041788 to add 圣月之皇太子 雷古勒斯 96228804 from deck; if the opponent controls a monster, also special summon 1 Spellcaster from hand, and 雷古勒斯 then searches another 恩底弥翁皇国, giving the field spell its destroy replacement (destroy a 雷古勒斯 from hand or field instead)
- Standard opener: 恩底弥翁皇国 34041788 plus any Spellcaster in hand, reveal the Spellcaster to special summon 雷古勒斯 96228804 from hand, pay revealed level x 300 LP, then search the second 恩底弥翁皇国
- Alternative opener: 魔力统辖 38943357 searches 仆从 92559258 or 统领 66104644, then 魔力掌握 75014062 and other Spells bank counters until the 2/8 pendulum scales are live
- Mid-game engine loop: pendulum summon 仆从 and 统领, dump 3 counters each to extend, link into 银金公主 24094258 (adds a pendulum from deck face-up to the Extra deck, destroys a card to recover a face-up pendulum, draws when a Pendulum Zone card leaves), then 塞勒涅 45819647, whose counters equal all Spells in both fields and graves, revives Spellcasters each turn

- **End Field**

- 创圣魔导王 恩底弥翁 3611830 with counters: one Spell/Trap activation negate per copy per turn by returning a counter-bearing card you control to hand, with its counters moving onto the boss; untargetable and effect-indestructible while it holds counters; battle-destroyed with counters it adds any Normal Spell from deck
- 胡狼王 27354732 negates one monster effect per turn for 2 counters; 刻耳柏洛斯尊主 53842431 banishes an opponent monster for 4 counters and absorbs its ATK
- 神圣魔皇后 塞勒涅 45819647 revives a Spellcaster from hand or grave each turn for 3 counters and cannot be attacked while any 恩底弥翁 card is on field
- 异色眼风雷龙 53262004 (Fusion of an Odd-Eyes monster plus a pendulum monster) bounces an attack-position monster on summon and negates any effect for 1 face-up pendulum from the Extra deck
- 魔法族之里 68462976 locks the opponent out of Spell activations while you control a Spellcaster, so the deck must keep one on field at all times
- Optional stun cards from the classic build: 天岩户 32181268 blocks monster effect activations while face-up, 电光-雪花- 13974207 blocks setting and activating Set Spell/Trap cards

- **Extenders**

- 魔力到达 39123673 recurs any counter-mentioning card from the grave, re-fueling the engine
- 魔法都市的实验设施 65342096 acts as a second 魔法都市 恩底弥翁 39910367, its name becomes the Citadel, and after your Spellcaster dies in battle it removes 6 counters to special summon a Level 7 or higher Spellcaster from deck
- 圣月之魔导士 恩底弥翁 20714553, a Link-2 needing a Level 4 Spellcaster, equips a Spellcaster from grave or banished zone to a 大贤者 monster on summon and bounces an equipped Spellcaster to hand as a quick effect
- Maids: 玻璃 22623509 special summons itself after a Spell activation and searches any 魔女术 Spell/Trap or 次元魔法; 杰妮 7656689 special summons itself while you control a Spellcaster and tags out to another 魔女术 monster
- 圣魔 裁决之雷 59080 pays a face-up 大贤者 card or 2 counters to special summon a Spellcaster from hand, face-up Extra deck, or grave, or to banish one other card
- 魔导研究所 94599451 banks 2 counters whenever your Mythical Beast pendulum is destroyed and trades any number of counters for a same-level counter-capable monster from deck or face-up Extra
- 宙读之魔术士 76794549, 刻读之魔术士 12289247 and 星读之魔术师-星占之魔术士 1186447 fix scales and recover when your cards are destroyed; 灵摆宝藏 26237713 adds any pendulum from deck face-up to the Extra deck

- **Halt Points**

- Ash Blossom on 魔力统辖 38943357, on 恩底弥翁皇国 34041788, or on 雷古勒斯 96228804 stops the search plus the counter placement
- Removing or banishing 魔法都市 恩底弥翁 39910367 deletes the counter bank and the once-per-turn cost payer
- 王家长眠之谷 47355498, which the deck itself mains, blocks the grave half of 魔力到达 39123673 and 塞勒涅 45819647 targets, so it can work against you
- 天岩户 32181268 also blocks your own monster effect activations while face-up, including 塞勒涅 and Mythical Beast disruption
- Handtraps that stop the first Spell activation or the pendulum summon, 灰流丽 14558127 and 增殖的G 23434538, starve the counter economy before it starts

- **Mirror Match**

- Every Spell activation feeds both players' counter engines, so the mirror is a race to resolve 魔力统辖 38943357 and 恩底弥翁皇国 34041788 first
- Keep 创圣魔导王 3611830 negate for the opponent's 魔力统辖 search, their 恩底弥翁皇国 activation, or their boss summon
- 魔法族之里 68462976 decides the mirror if resolved first: its controller keeps casting Spells while the opponent cannot
- Do not fire chain Spells into the opponent's 仆从 92559258 or 统领 66104644 in the Pendulum Zone, every activation banks them a counter
- 异色眼风雷龙 53262004 negates the opponent's 创圣魔导王 summon line or Mythical Beast disruption

- **Common Mistakes**

- Forgetting that your own Spell activations give the opponent's pendulum 仆从 92559258, 统领 66104644 and 皇后 39000945 counters too, and their activations give you counters, so sequence cheap Spells first
- Paying counter costs from the pendulum monsters instead of 魔法都市 恩底弥翁 39910367, which can pay once per turn as the bank
- 统领 66104644 Extra deck summon requires a free Extra Monster Zone, so it is dead without a Link monster or an empty Extra zone first
- 仆从 92559258 deck fetch needs ATK 1000 or more, so it cannot fetch itself (ATK 900) but can fetch 统领 66104644, 皇后 39000945 and the Mythical Beasts
- 魔力到达 39123673 negation needs a Level 7 or higher 恩底弥翁 monster on field, and 王家长眠之谷 47355498 blocks its grave search
- Returning the wrong card to hand for the 创圣魔导王 3611830 negate: bounce a card you can afford to lose, like a Mythical Beast or a pendulum, so its counters transfer to the boss
- 轨迹之魔术师 22125101 locks the turn: pay 1200 LP and you must pendulum summon this turn or your monster effects and Pendulum Zone effects are dead
- 魔法族之里 68462976 locks you out of Spells the moment you control no Spellcaster, including after a board wipe
- The deck has no one-card combo, so do not overextend on a partial hand, one survived turn restarts the counter economy
