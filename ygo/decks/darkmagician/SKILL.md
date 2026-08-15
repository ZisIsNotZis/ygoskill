---
name: darkmagician-experience
description: 黑魔术师 (Dark Magician) deck experience: mechanics, one-card combo, extenders, halt points
---
# 黑魔术师 (Dark Magician) Deck Experience

- **Deck Identity**

- Centerpiece: 黑魔术师 46986414, a Level 7 DARK Spellcaster Normal Monster with no script, 2500 ATK, the name every support card lists
- 黑魔术少女 38033121, Level 6 DARK Spellcaster, gains 300 ATK per 黑魔术师 46986414 or 黑混沌之魔术师 30208479 in either GY
- Modern main deck (260228黑魔术师 build): 魔术师之杖 7084129 x3, 王之仆人-黑魔术师 88570003 x3, 魔术师双魂 97631303, 混沌之幻想魔术师 12266229 x2, 黑魔导阵 47222536 x3, 魂之仆人 23020408 x3
- Modern extra deck: 超魔导龙骑士-真红眼龙骑士 37818794, 毁灭之黑魔术师 59400890 x2, 超魔导战士-混沌制驭者 85059922, 鲜花女男爵 84815190, 共命之翼 迦楼罗 11765832, S:P小夜骑士 29301450, I:P百变莱娜 65741786
- 260228黑魔 build adds the link climb: 神圣魔皇后 塞勒涅 45819647, 访问码语者 86066372, 闭锁世界的冥神 98127546, 天霆号 阿宙斯 90448279
- Alternate builds (260320黑魔术师融合): 超融合 48130397 x2 plus 星尘龙 44508094, 异色眼灵摆龙 16178681, 凶饿毒融合龙 41209827 as fusion-food for 毁灭之黑魔术师
- Legacy hybrid (140000黑魔魔导书): 魔导书士 巴特尔 14824019, 奥义之魔导书 89739383, 创造之魔导书 56981417, 魔导书的神判 46448938, 魔导书院 拉迈松 33981008

- **Core Mechanic: Name-Linked Search and Fusion**

- Nearly every spell and trap lists 黑魔术师 46986414 in its text, and all searches filter by "lists 黑魔术师", so any one search reaches any support card
- 魔术师之杖 7084129 normal summon searches any spell or trap that lists 黑魔术师, making it the engine's key searcher
- 黑魔术的继承 41735184 banishes two spells from GY to add one 黑魔术师-listing spell or trap from deck, a second search outlet that fuels itself off spell-heavy play
- 混沌之幻想魔术师 12266229 reveals itself in hand to add any non-ritual monster that lists 黑魔术师, then shuffles one hand card to deck top
- Fusion lines use 黑魔术的秘仪 59514116 and 蒂迈欧之眼光 22283204, both of which special summon the fusion themselves instead of needing a Polymerization-type spell
- 黑魔术的秘仪 59514116 can perform a fusion summon using any fusion monster whose materials include 黑魔术师 46986414 or 黑魔术少女 38033121, or a ritual summon releasing either as material
- 蒂迈欧之眼光 22283204 targets one 黑魔术师 or 黑魔术少女 on field or GY, returns it to deck, and fusion summons a fusion monster listing that card, but that fusion is banished at the next End Phase (script: turn count plus one)
- 黑魔导阵 47222536 (field spell in official data, coded as a continuous spell in this cards.cdb) excavates top three on activation and adds one 黑魔术师 or a spell or trap that lists it
- 黑魔导阵 47222536 second effect: when 黑魔术师 is normal or special summoned, banish one card your opponent controls, a constant removal trigger on every DM summon

- **One-Card Combo: 魔术师之杖**

- Starter: 魔术师之杖 7084129 in hand, no other cards needed
- Step 1: normal summon 魔术师之杖, activate its summon effect, add any 黑魔术师-listing spell or trap from deck, prefer 黑魔导阵 47222536 or 魂之仆人 23020408
- Step 2: activate 黑魔导阵, excavate the top three cards, add one 黑魔术师 46986414 or a spell or trap that lists it to hand
- Step 3: play 魂之仆人 23020408, place 黑魔术师 46986414 from hand on top of deck, the upcoming draw is now a 2500 body
- Step 4: normal or special summon 黑魔术师 next turn to trigger 黑魔导阵's banish on every summon
- Halt point: 灰流丽 14558127 on 魔术师之杖's search or 黑魔导阵's excavation leaves you with a 1600 ATK body and no engine

- **End Field**

- 超魔导龙骑士-真红眼龙骑士 37818794 fusion of 黑魔术师 plus 真红眼黑龙 74677422 or any Dragon Effect Monster, immune to targeting and destruction by card effects
- 超魔导龙骑士 quick effect discards one card to negate and destroy any card activation, and gains 1000 ATK when it does
- 超魔导龙骑士 ignition effect destroys one opponent monster and burns its ATK as damage, once per turn per normal monster used as material
- 超魔导战士-混沌制驭者 85059922 fusion of 黑魔术师 plus a Chaos ritual monster (setcode 0xcf, e.g. 黑色混沌之魔术师 黑混沌 44001993), revives a DARK or LIGHT from GY on fusion summon
- 超魔导战士-混沌制驭者 releases one LIGHT and one DARK to banish every monster your opponent controls, a second floodgate layer
- 毁灭之黑魔术师 59400890 fusion of 黑魔术师 plus any LIGHT or DARK monster, and is also summonable from the extra deck by banishing a Level 6 or higher DARK Spellcaster you control after any spell was activated
- 毁灭之黑魔术师 treated as 黑魔术师 46986414 on field and GY, and searches any 黑魔术师-listing card on summon, so it both extends and fuels 黑魔导阵
- 超魔导骑士-黑魔导骑兵 73452089 fusion of 黑魔术师 plus a Warrior, gains 100 ATK per spell or trap on field and GY, and discards to negate a targeting effect
- Ideal closing board: 超魔导龙骑士 37818794 plus 黑魔导阵 47222536 plus a hand 灰流丽 14558127, Dragoon's negate covering the turn, 黑魔导阵 banishing on any DM summon

- **Extender: 魔术师双魂**

- 魔术师双魂 97631303 from hand sends one Level 6 or higher Spellcaster from deck to GY as cost, then special summons itself
- The milled 黑魔术师 46986414 gives 黑魔导阵 47222536 a future summon to banish off of, makes 魂之仆人 23020408's GY draw count it, and enables 永远之魂 48680970 recursion
- Once on field, 魔术师双魂 sends up to two spells or traps from hand or field to GY to draw that many cards, a draw engine that converts dead spells into hand advantage
- 魔术师双魂 second mode sends itself to GY to special summon 黑魔术师 46986414 or 黑魔术少女 38033121 from GY

- **Extender: 王之仆人-黑魔术师**

- 王之仆人-黑魔术师 88570003 special summons itself from hand by revealing one spell from hand as cost, no discard
- It is treated as 黑魔术师 46986414 on field and GY, so it triggers 黑魔导阵 47222536 and counts for 黑魔术少女 38033121's ATK
- After summoning, it sets one 黑魔术师-listing spell or trap directly from deck, an extra engine piece for free
- Its quick effect discards one spell to destroy all spells and traps your opponent controls, a one-sided 羽毛扫 on the opponent's turn

- **Extender: 黑魔术的秘仪 59514116**

- One spell performs either the fusion or the ritual branch, chosen at activation, both require 黑魔术师 46986414 or 黑魔术少女 38033121 among the materials
- Fusion branch makes 超魔导龙骑士 37818794, 毁灭之黑魔术师 59400890, 超魔导骑士 73452089, or 超魔导师-黑魔术师徒 50237654 from field monsters
- Ritual branch releases 黑魔术师 or 黑魔术少女 (plus any other monsters to meet the ritual monster's level, which is 8 for both chaos magicians) to ritual summon 黑混沌之魔术师 30208479 or 黑色混沌之魔术师 黑混沌 44001993, which then serve as 超魔导战士-混沌制驭者 85059922 material
- 超魔导师-黑魔术师徒 50237654 fusion of 黑魔术师 or 黑魔术少女 plus a Spellcaster, draws one whenever a spell or trap activates and can set it, and revives both 黑魔术师 and 黑魔术少女 when destroyed

- **Extender: 蒂迈欧之眼光 22283204**

- One spell turns a single 黑魔术师 46986414 or 黑魔术少女 38033121 from field or GY into a fusion monster, no second material needed on field
- 龙骑士 黑魔术师 41721210 (黑魔术师 plus a Dragon) is the classic target, it protects your spells and traps from targeting and destruction
- The fusion summoned this way is banished at the next End Phase, so time the play to use the fusion's effect within one turn cycle

- **Extender: 魔术师的导门阵 7922915**

- Normal trap that special summons 黑魔术师 46986414 from hand plus one Level 7 or lower DARK Spellcaster from deck
- Works from the opponent's turn, and its GY effect banishes itself to negate a face-up spell or trap while 黑魔术师 is on field

- **Extender: 师徒的牵绊 60709218**

- Requires a face-up 黑魔术师 46986414 on field, then special summons 黑魔术少女 38033121 from hand, deck, or GY
- After summoning it sets one of 黑·魔·导 2314238, 黑·爆·裂·破·魔·导 75190122, 黑·魔·导·爆·裂·破 49702428, or 黑·魔·导·连·弹 70168345 from deck
- 黑·魔·导 2314238 destroys all opponent spells and traps while 黑魔术师 is face-up, 千把刀 63391643 destroys one opponent monster

- **Halt Points**

- 灰流丽 14558127 on 魔术师之杖 7084129's search, 混沌之幻想魔术师 12266229's search, or 黑魔术的继承 41735184 kills the first search and stalls the deck
- 灰流丽 on 黑魔术的秘仪 59514116 stops the fusion line entirely because the fusion itself is the spell's effect
- 效果遮蒙者 97268402 or 无限泡影 10045474 on 魔术师之杖 7084129 after normal summon blanks the search and leaves no engine
- 增殖的G 23434538 punishes the deck hard because the standard line makes several special summons, prefer ending on 黑魔导阵 plus one body under G
- 次元吸引者 91800273 style banish locks the deck out because most recursion depends on GY (黑魔术的继承 41735184, 永远之魂 48680970, 魔术师双魂 97631303 GY mode)
- 墓穴的指名者 24224830 on 魔术师之杖's GY effect, 黑魔术少女 38033121's count, or 龙骑士 黑魔术师 41721210 protection disrupts the mid game
- 技能抽取 82732705 and 千查万别 24207889 shut off the whole engine since every monster is an effect monster except the vanilla 黑魔术师 46986414

- **Mirror Match: 黑魔术师 vs 黑魔术师**

- First 黑魔导阵 47222536 to resolve wins the banish war because every subsequent DM summon removes a card
- 超魔导龙骑士 37818794 negates the opponent's 黑魔术的秘仪 59514116 or 蒂迈欧之眼光 22283204, whoever resolves Dragoon first negates the other's fusion line
- 超融合 48130397 can fuse using the opponent's 黑魔术师 46986414 as the DARK material for 毁灭之黑魔术师 59400890, so holding it changes how the opponent may commit monsters
- Keep 千把刀 63391643 for the opponent's 黑魔术少女 38033121, which otherwise outgrows everything as DMs fill both GYs
- 魔术师双魂 97631303 draws decide the mirror, whoever mills and draws into 黑魔术的秘仪 first establishes Dragoon

- **Common Mistakes**

- Do not search 黑魔导阵 47222536 with 魔术师之杖 7084129 when the deck is under 3 cards, the excavation requires at least 3 in deck
- Activate 黑魔导阵 47222536 before the DM summon, the banish trigger is on the summon event and only fires while the spell is face-up on field
- 蒂迈欧之眼光 22283204 banishes its fusion at the next End Phase, do not commit your only 黑魔术师 to a fusion that disappears before your next turn
- 黑魔术的秘仪 59514116 needs the 黑魔术师 or 黑魔术少女 among its actual materials, keep one in hand or field instead of milling every copy
- 永远之魂 48680970 (if played) destroys all your monsters when it leaves the field, protect it with 龙骑士 黑魔术师 41721210 or remove it only as a deliberate sacrifice
- 王之仆人-黑魔术师 88570003 effects ② and ③ share one use per turn, using the hand summon to set a spell on your turn locks out the discard quick destroy for that same turn
- Do not dump both 魔术师双魂 97631303 draw targets from hand, keep at least one spell to discard for 王之仆人-黑魔术师 88570003's quick destroy or 超魔导龙骑士 37818794's negate
- 魔术师之杖 7084129 has 1600 ATK and no battle protection, never leave it as your only field against attack lines
- 黑魔导阵's excavation reveals cards to your opponent, sequence searches so the revealed 黑魔导阵 or 魂之仆人 does not telegraph the whole plan

- **Environment Notes**

- 黑魔导阵 47222536 is stored as a continuous spell in this cards.cdb even though official data has it as a field spell, the script works identically from the spell zone
- 魂之仆人 23020408, 黑魔导的幕帘 41350417, 黑魔术的秘仪 59514116, and 蒂迈欧之眼光 22283204 are coded as quick-play spells in this cards.cdb, allowing opponent-turn activation, verify timing against official normal-spell rulings
- 超魔导龙骑士-真红眼龙骑士 37818794's once-per-turn destroy uses the number of Normal Monsters among its fusion materials (script counts TYPE_NORMAL), a DM plus a dragon effect monster yields one use
- 黑魔术师 46986414 and 黑魔术少女 38033121 have no script beyond stat lines, all interaction comes from the support cards that list them
