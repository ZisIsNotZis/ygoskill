---
name: millennium-experience
description: 千年 (Millennium) deck experience: Exodia fusion artifacts, 千年十字 line, one-card combo, extenders, halt points
---
# 千年 (Millennium) Deck Experience

- **Deck Identity**

- Archetype 千年 (setcode 0x1ae): Egyptian artifact monsters that set themselves as continuous spells in the spell/trap zone and cheat out the Exodia fusion boss 幻之召唤神 艾克佐迪亚 83257450
- Supporting columns: 被封印 (setcode 0x40, the five Exodia pieces), 艾克佐迪亚 (setcode 0xde), and the 艾格佐德 spells 魔神火炎炮 64043465, 愤怒之业火 魔神火炎炮 23617756, 魔神火焰炮 402416 (setcode 0x1af)
- Win routes: 幻之召唤神 艾克佐迪亚 83257450 beatdown, the alternate win of gathering all five 被封印 pieces in hand (被封印的艾克佐迪亚 33396948), or 召唤神 艾克佐迪亚 58604027 beatdown
- Engine monsters: 千年王朝之盾 1164211 (searches 千年十字 37613663), 从千年长眠中觉醒的原人 38775407 (searches a 千年 monster), 守护千年珍宝的石人 74169516 (searches 石版神殿 63017368), plus defensive 千年月少女 37552929, 千年绝对鸟 63947968, 千年的血族 5130393 and vanilla 千年原人 76232340, 千年石人 47986555
- Strongest build (deck/250927千年刻魔被封印闪刀欢聚友伴): full Millennium engine plus 宿心的青眼龙 54475145 with 刻魔/闪刀/欢聚友伴 shells; pure engine build (deck/240427被封印千年) adds the link toolbox 纳祭之魔·阿尼玛 94259633, S：P小夜骑士 29301450, 访问码语者 86066372

- **Core Mechanic: Spell-Place Engine into 千年十字**

- Every 千年 effect monster has ①: from the hand, place itself face-up as a continuous spell in the spell/trap zone (needs a free zone)
- While placed as a spell each has ②: pay 2000 LP or reveal 千年十字 37613663 from hand, then special summon itself and search — 千年王朝之盾 1164211 → 千年十字 37613663, 从千年长眠中觉醒的原人 38775407 → a 千年 monster, 守护千年珍宝的石人 74169516 → 石版神殿 63017368; ② is once per turn per card
- 千年十字 37613663: reveal exactly five 被封印 monsters (被封印的艾克佐迪亚 33396948, 被封印者的左腕 7902349, 被封印者的右腕 70903634, 被封印者的左足 44519536, 被封印者的右足 8124921) from hand/deck/face-up field, special summon 幻之召唤神 艾克佐迪亚 83257450 from the extra deck, shuffle every other face-up monster you control into the deck, then lock all your summoning for the turn
- The revealed pieces are only confirmed and stay where they were, so the combo is repeatable and the Exodia win stays live
- 千年十字 37613663 returns to the deck after resolving instead of going to the graveyard
- 幻之召唤神 艾克佐迪亚 83257450: Level 10, ① immune to opponent effect destruction, ② quick effect at damage calculation adds your current LP to its ATK, ③ once per turn negates a spell/trap activation, ④ at any end phase sets one 艾格佐德 spell (setcode 0x1af) from the deck, ⑤ standby phase you lose 1000 LP

- **One-Card Combo: 千年王朝之盾 1164211**

- Hand: 千年王朝之盾 1164211 only, all five 被封印 pieces still in the deck
- Step 1: activate ① to place 千年王朝之盾 1164211 as a continuous spell in the spell/trap zone
- Step 2: activate ② paying 2000 LP, special summon 千年王朝之盾 1164211 and search 千年十字 37613663 from the deck
- Step 3: activate 千年十字 37613663 revealing the five 被封印 pieces 33396948, 7902349, 70903634, 44519536, 8124921 from the deck, special summon 幻之召唤神 艾克佐迪亚 83257450
- Step 4: 千年十字 37613663 shuffles itself into the deck, the summon lock applies, 千年王朝之盾 1164211 stays on field because it is setcode 0x1ae
- End phase: 幻之召唤神 艾克佐迪亚 83257450 ④ sets 魔神火炎炮 64043465 or 愤怒之业火 魔神火炎炮 23617756 face-down from the deck

- **End Field**

- 幻之召唤神 艾克佐迪亚 83257450 (immune to effect destruction, negates one spell/trap per turn, adds LP to ATK in battle) plus 千年王朝之盾 1164211 (0/3000 wall, immune to spell/trap destruction)
- One face-down 艾格佐德 spell set by 幻之召唤神 艾克佐迪亚 83257450, all five 被封印 pieces still available for next turn
- 守护千年珍宝的石人 74169516 on field makes your 千年十字 37613663 activations unnegatable, keep it out when possible
- 愤怒之业火 魔神火炎炮 23617756 ① wipes the opponent board while 幻之召唤神 艾克佐迪亚 83257450 (Level 10 艾克佐迪亚 archetype) is on field
- Own standby phase 幻之召唤神 艾克佐迪亚 83257450 ⑤ costs 1000 LP, close the game before the drain matters

- **Extenders**

- 石版神殿 63017368: ① places a monster from hand as a continuous spell, then places one 千年 monster from the deck as a continuous spell — that deck-placed monster can immediately use its ② to special summon itself and search; ② a destroyed 千年 monster becomes a continuous spell instead of going to the graveyard
- 宿心的青眼龙 54475145: ① discard it to search 千年十字 37613663 (free second starter), ③ while in the graveyard when the opponent summons a Level 8 or higher or 3000 or more ATK monster, send those monsters to the graveyard and special summon itself, once per duel and only in a duel where you activated 千年十字 37613663
- 从千年长眠中觉醒的原人 38775407: as a spell, special summons itself (2750/2500) and searches another 千年 monster; on the field it cannot be destroyed by monster effects
- 守护千年珍宝的石人 74169516: as a spell, special summons itself and searches 石版神殿 63017368
- 千年的启示 41044418: ① discard a Divine-Beast such as 千年原人 76232340 or 从千年长眠中觉醒的原人 38775407 to add 死者苏生 83764718 from deck or graveyard, ② sends itself from the spell/trap zone to the graveyard so this turn 死者苏生 83764718 can special summon 太阳神之翼神龙 10000010 ignoring summon conditions (that 翼神龙 goes to the graveyard at the end phase)
- 千年月少女 37552929: as a spell, chains to an opponent effect activation to special summon itself, this turn the opponent cannot target your Level 5 or higher 幻想魔族/魔法师族 monsters with effects, and both battle monsters survive that battle; 千年绝对鸟 63947968 chains the same way and gains LP
- 千年的血族 5130393: special summons itself from hand when you take 1000 or more damage, ② steals a monster from the opponent graveyard
- 魔神火炎炮 64043465: ① bounces any field monster by sending a 被封印/艾克佐迪亚 card from hand or deck to the graveyard (also feeds 召唤神 艾克佐迪亚 58604027 ATK), ② when it leaves the spell/trap zone to the graveyard adds a 被封印/艾克佐迪亚 card from the graveyard
- 愤怒之业火 魔神火炎炮 23617756: ① destroys all opponent cards while a Level 10 or higher 艾克佐迪亚 monster is on your field, ② banishes itself from the graveyard to add one 被封印 monster from deck/graveyard or return up to five 被封印 monsters from graveyard/banished to the deck (reloads the 千年十字 37613663 piece count)

- **Halt Points**

- Ash 灰流丽 14558127 on 千年王朝之盾 1164211, 从千年长眠中觉醒的原人 38775407 or 宿心的青眼龙 54475145 search stops access to 千年十字 37613663
- G·B·猎人 4130270 face-up blocks 千年十字 37613663 activation entirely because cards on the field cannot return to the deck
- 增殖的G 23434538: the pure 千年十字 37613663 line is one special summon so it is G-resistant, but 石版神殿 63017368 plus the 原人/盾/石人 ② extensions stack summons and hand the opponent draws
- 幻之召唤神 艾克佐迪亚 83257450 has no monster-effect protection: 熔岩魔神 102380 or 海龟坏兽 加美西耶勒 55063751 tribute it, 效果遮蒙者 97268402 negates it, ③ only stops spell/trap activations
- If the special summon of 幻之召唤神 艾克佐迪亚 83257450 is negated (for example 神之宣告 41420027), the summon lock still applies and you end the turn with nothing summonable
- Fewer than five 被封印 pieces in hand/deck/field (banished or stuck in the graveyard) makes 千年十字 37613663 unplayable; pieces in the graveyard only feed 召唤神 艾克佐迪亚 58604027 ATK
- 幻之召唤神 艾克佐迪亚 83257450 is not properly fusion summoned by 千年十字 37613663, so 死者苏生 83764718 cannot revive it

- **Mirror Match**

- First player to resolve 千年十字 37613663 controls the duel: 幻之召唤神 艾克佐迪亚 83257450 ③ negates the opponent 千年十字 37613663 activation
- 守护千年珍宝的石人 74169516 ③ makes your 千年十字 37613663 unnegatable, keep it on the field in the mirror
- 幻之召唤神 艾克佐迪亚 83257450 ② uses your LP as ATK, preserve LP instead of freely paying 2000 LP costs, and the 1000 LP standby drain decides damage races
- Do not summon non-千年 monsters or links before 千年十字 37613663, they get shuffled into the deck by its resolution
- 千年的血族 5130393 steals opponent graveyard 被封印 pieces in the mirror, and 魔神火炎炮 64043465 bounces 幻之召唤神 艾克佐迪亚 83257450 because it is only destruction-immune, not bounce-immune

- **Common Mistakes**

- Activating 千年十字 37613663 after making link monsters shuffles them into the deck, resolve it first or keep only 千年 (setcode 0x1ae) monsters on field
- Summoning anything after 千年十字 37613663 is impossible for the rest of the turn, do all summons before it
- Paying 2000 LP for ② costs while holding a 千年十字 37613663 in hand, reveal it instead to save LP
- Using 被封印 pieces as fusion material or 魔神火炎炮 64043465 dump moves them out of the hand/deck/field pool and can strand the combo
- Forgetting 幻之召唤神 艾克佐迪亚 83257450 ⑤ drains 1000 LP every standby, a stalled board with it out is a loss timer
- The Exodia win (被封印的艾克佐迪亚 33396948) only checks when a card is added to hand, assemble the fifth piece with 愤怒之业火 魔神火炎炮 23617756 ② or the 召唤神 艾克佐迪亚 58604027 end phase effect so the check fires
- 召唤神 艾克佐迪亚 58604027 needs a 被封印 monster to tribute, do not spend the last accessible piece without a recovery plan
- 千年的启示 41044418 ① needs a Divine-Beast in hand, keep 千年原人 76232340 or 从千年长眠中觉醒的原人 38775407 available when running the 死者苏生 83764718 line
