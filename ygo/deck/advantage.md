---
name: advantage
description: Game advantage and tempo reference: advantage types and trades, summon resources, hidden zones, interaction timing, win axes, and the clock
---
# Game Advantage and Tempo

- **Advantage Kinds and How Cards Trade**

- Card advantage is raw card-count parity: searches, draws and recursion are +1 plays, so the deck docs' halt points center on the searcher (机壳工具 丑恶 65518099, 骷髅杂技小丑 40318957, 时械巫女 27107590); negating the search with 灰流丽 14558127 denies the plus (交闪 63166095, 特莱恩 91812341)
- Board advantage is not the same: one monster outweighs a whole field, 香格里拉茧 73542331 zone locks beat three beaters, 米德拉什 94977269 caps both players to one summon, so removal priority is by effect value not ATK (negate effects first, stall effects second, beaters last)
- Tempo is who reaches their plan with fewer actions: 深海歌后 78868119 turns one normal summon into two bodies, the Yosenju Kama chain 65247798/92246806/28630501 turns one normal summon into four attacks and nets hand +2 when they bounce home
- Life-point pressure converts cards into a clock: 限制解除 23171610 doubles the four Numeron gates 15232745/42230449/78625448/4019153 to 8000 direct, Tenpai stacks 1500+2600+1500+3000 for lethal, Mikanko reflects 10600 off a Kaiju 63941210 with 脆刃之剑 41927278, so OTK decks buy LP with board breakers
- A removal trades by what it removes: a 1-for-1 is card-neutral but tempo-positive when it kills the engine piece (无限泡影 10045474 on 塞拉 73639099 or 内燃 8633261), while 黄金卿 95440946 effect 1 trades 2 cards for 1 and is only right against a must-kill target
- Destruction that floats turns removal into advantage: 破械 replaces every destroyed card from deck (阿罗汉 26236560, 娑罗摩 31588572), trap holes 31548215/69599136 are 1-for-1 but 塞拉 73639099 re-sets and re-summons them into a loop, so a card's value is its recursion, not its activation

- **The Five Summon-Resource Categories**

- Normal summon is the scarcest per-turn resource: decks multiply it (Yosenju Kama chain, 沙龙 71348837 extra Madolche summon, 法之神灵 84288367 extra Spellcaster summon) or bypass it (True Draco tribute summons via continuous spells 75425320/49430782, Monarch squire 95457011 grants extra tribute summons)
- Tribute is a counted budget: True Draco pays continuous spells as tribute (EFFECT_ADD_EXTRA_TRIBUTE) so backrow is the fuel, Monarch pays monsters for the lock payoff 84171830/48716527, Qliphort counts 机壳的冻结 20447641 as 3 tributes and 机壳的牲祭 17639150 as 2, and negating a big tribute wastes the whole investment
- Extra deck slots are a 15-card budget: Link-1 ladders spend one slot to start engines (零衣 26077387, 塞拉 73639099, 马克斯 71791814), overlay-on-top Xyz keep material piles (Zoodiac 龙枪 48905153, Kashtira 香格里拉茧 73542331 into 阿莱斯哈特 48626373), and locks tax extra-deck freedom (Swordsoul token lock, Spright Level-2 lock 15443125/54498517, Qliphort pend-lock)
- Pendulum scales are a two-zone investment that refunds itself: destroyed pendulums go face-up to the extra deck, so a 1-8 scale pair (Pendulum Magician 94415058/20409757) re-summons the swarm every turn, and every scale pair carries a restriction (Qliphort 0xaa lock, 骷髅杂技小丑 40318957 scale limit)
- Tokens and LP costs are the fifth category: LP pays for engines (Dinomorphia half-LP costs into 狂飙霸王龙 92798873, Qliphort Tool 800 per search 65518099, 启辉器 15443125 pays attack as LP), tokens are free material that also count for 增殖的G 23434538 and 尼比鲁 27204311 (Swordsoul 相剑衍生物, Sky Striker 大黄蜂 52340444), and skipping the battle phase is a cost too (every Runick quick-play)

- **Hidden Advantage: GY, Banish and Hand as Zones**

- The graveyard is a second hand for most engines: Labrynth 欢迎 5380979 re-sets itself from GY, Eldlich runs the whole loop from grave (95440946, 68829754, 56984514), Shaddoll monsters are two cards each (flip effect plus grave trigger on 3717252/4939890), Tearlaments fuses from GY (74078255, 92731385), 影依的原核 4904633 substitutes any attribute from grave
- Banish is a third zone: Maliss plays entirely from banished (32061192, 21848500, 95454996), Swordsoul 承影 96633955 scales off the banished count under 大宇宙 30241314, Invoked 召唤魔术 74063034 banishes materials to recover 阿莱斯特 86120751, and 次元吸引者 91800273 flips the game to banishment (asymmetric for Maliss, fatal to Tenpai grave recursion 65326118 and Dark World discard triggers)
- The hand is hidden card advantage: hand traps (14558127, 23434538, 10045474, 40366667) answer from nowhere, Plunder tag-out 68769900/31374201 reads the opponent's field and GY attributes, and 墓穴的同路人 16435215 turns discards into opponent-effect triggers for Dark World 76672730
- Zone denial is how you cut recursion: 墓穴的指名者 24224830 on the key GY piece (梅洛人鱼 74078255, 雷诺哈特 73956664, 娑罗摩 31588572), 深渊的潜伏者 21044178 shutting off all GY triggers, 香格里拉茧 73542331 locking monster zones, and Runick milling the deck top as inverse card advantage (92107604, 29595202)
- Zone-aware play: count every zone before acting — Sky Striker spells fail with a monster in a main zone (63166095), 无限光 72883039 needs an empty field, 源数直系 77402960 needs zero monsters, and a full backrow blocks Plunder tag-out equips

- **Interaction Timing and Sequencing**

- Spell speeds decide who can answer: quick effects and quick-plays (speed 2) chain to normal spells and traps (speed 1), counter traps (speed 3) beat everything except counter traps (永久辉煌的黄金乡 56984514, 神之宣告 41420027), and the window is the play
- "Cannot respond" clauses flip the window: 暴走魔法阵 47679935 blocks responses to your fusion summons, 灿幻超龙 18969888 locks the whole battle phase, 白银之城的拉比林斯 2347656 stops monster-effect chains to your traps, 幻变骚灵协议 27541563 makes your effects unnegatable, 王宫的通告 51452091 negates all traps
- Hand-trap windows are effect-class specific: Ash 14558127 only hits add/mill/summon-from-deck (it cannot stop 火吹炉 74018812's set-from-deck), 幽鬼兔 59438930 needs a field effect activation, 灵王的波动 40366667 only special-summon effects, 尼比鲁 27204311 only past the fifth summon, so sequence to dodge the live one
- Bait and commit: fire a cheap non-essential effect first to force the negate (Magibullet column trigger 32841045 with a generic spell, 炎舞-「天玑」 57103969 before the real search, Zoodiac 会局 46060017), then resolve the engine piece into the spent window
- Ordering within a turn is a resource: 灵摆呼唤 53208660 must come before scale effects, 强欲而金满之壶 49238328 only at the start of Main Phase 1, 武器洞 52105192 before the normal summon, 沙龙 71348837 before 券 60470713 on the Madolche return chain, Runick Fountain 92107604 recycles only cards already in GY
- Under 增殖的G 23434538 tempo flips: the full combo becomes a self-damaging draw engine, so the docs' compromise lines (stop at 红棋勒索 68059897, stop at 巨大喷流 54498517, Labrynth one trap plus one summon) are the correct clock decision

- **The Three Win Axes and Engine Shape**

- Field lock: small board plus denial that answers everything — Labrynth traps behind 2347656, Eldlich floodgates 82732705, True Draco 熔击 48716527 plus tribute immunity 21377582, Monarch 84171830, Qliphort 再星 20426907, Dinomorphia Rexterm 92798873, Kashtira zone lock, Runick floodgates behind 神碑之泉 92107604
- Damage/OTK: going-second shape — board breakers, few summon steps, a finisher that converts LP (Numeron gates 15232745 plus 限制解除 23171610, Tenpai battle-phase synchros 39931513/18969888, Mikanko reflect 41927278, Timelord burn 33015627/60222213) and little or no follow-up, so they win in one turn or lose the next
- Grind/fatigue: recursion density — every engine piece works twice (Eldlich hand-and-grave 95440946, Sky Striker spell loop 63288573/63166095, Altergeist trap revival 35146019/22024279, Unchained float, Magibullet hand-activation plus recursion 68246154/68024506, Dark World discard draws 76672730), so they win by out-drawing and out-recycling
- Reading the axis from engine shape: extra deck density and pump slots (OTK lists run 限制解除 23171610 or 脆刃之剑 41927278), recursion clauses in card text (set-from-GY, float, revive), floodgate count in the main, LP costs (Dinomorphia), battle-phase skipping (Runick = fatigue, Tenpai = damage), and summon count per turn (2-3 = control, 8+ = combo)

- **The Clock: Pushing, Holding and Setting Up**

- The clock is who wins in how many turns, independent of psychology: OTK decks threaten turn-2 lethal so every pass is a decision against the clock, combo decks have a fast clock but no recovery (Numeron 源数直系 77402960 banishes the gates at end phase), grind decks have a slow clock and can trade forever
- The deck docs' halt points are clock decisions: the moment you stop extending to deny the opponent's answer — end before the fifth summon (尼比鲁 27204311) unless a lock already prevents it (灿幻超龙 18969888 before Nibiru is live), stop the line under Maxx C 23434538, keep 香格里拉茧 73542331 alive because all locks vanish with it, keep a face-down for 白银姬 81497285 protection
- Push vs hold: attack with the weakest attacker first to trigger effects (中龙 91810826 deck summon, 镰贰太刀 92246806 battle-damage search, Zoodiac ladder into 天霆号 90448279 after battle), hold blockers when the opponent's clock is faster than yours (Timelord walls 33015627, Runick 史莱普尼尔 74659582 token)
- Set up vs pass: when the engine is one piece short, pass with recursion armed (真龙导士 95004025 reactive search, 塞拉 73639099 plus one set trap, 欢迎 5380979 set from GY) rather than force a partial play, because every turn the setup survives is a turn closer to your axis
- Track the differentials that define the clock: summon count (Nibiru/Maxx C), LP thresholds (Dinomorphia 2000 trap recursion and Rexterm 92798873 floodgate, 脆刃之剑 41927278 self-destruct at 2000 damage), banished/grave counts (承影 96633955 attack, Runick mill rate), and hand sizes (Dark World 文殿 76672730 draw-two, Yosenju +2 per turn)

- **Reading the Board**

- The 5 questions an expert asks each turn:
- 1. What axis is the opponent on — field lock, OTK, or grind — and what is their clock in turns, given their engine shape and what they have already committed?
- 2. What is the summon count and zone state: is 尼比鲁 27204311 or 增殖的G 23434538 live, which zones are locked or blocked, and how many summons can I afford?
- 3. Where does their recursion live (hand, GY, banish, face-up extra deck) and can I cut it this turn with 墓穴的指名者 24224830, 深渊的潜伏者 21044178, 次元吸引者 91800273, or a zone lock?
- 4. Which of their interactions answer my plan, which clauses matter (spell speed, "cannot respond", unnegatable), and what cheap play can I bait first to force the commit?
- 5. Is this a push turn, a hold turn, or a setup turn — do I convert to damage, hold blockers, or arm recursion, and what happens to my own clock if I pass?
