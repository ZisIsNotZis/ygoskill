---
name: altergeist-experience
description: 幻变骚灵 (Altergeist) deck experience: trap-control link engine, trap recursion, combo lines, halt points
---
# 幻变骚灵 (Altergeist) Deck Experience

- **Deck Identity**

- Control deck built on trap activations that chain into link monsters, all Light Spellcaster monsters with setcode 259 (0x103)
- Main engine monsters: 多功能诈骗者 42790071, 网络傀儡师 53143898, 寻道梅露辛 25533642, 泛在羽衣精 89538537, 恶意软件鬼火 27132400, 查询普卡 59185998
- Support monsters: 查询昆提兰那克 52927340, 渗透佩里 54126514, 像素妖精 57769391, 延迟菲芬尼拉 12977245, 警报食人水妖 85673903
- Core traps: 幻变骚灵协议 27541563, 幻变骚灵物化 35146019, 幻变骚灵复苏 22024279, 幻变骚灵伪装 80143954, 幻变骚灵的故障转移 98753320, 幻变骚灵的闹鬼死锁 2547033, 幻变骚灵·模拟精灵 86885905
- Extra deck links: 十六巫赫斯提 1508649 (Link 2), 隐私王班西 93503294 (Link 3), 管理提泰妮娅 61470213 (Link 4), 存储姬摩莉甘 23790299 (Link 4), 击键录杜尔迦 76685519 (Link 2)
- Generic tech: 个人欺骗攻击 53936268, 金满而谦虚之壶 84211599, 一对一 2295440, 访问码语者 86066372, 神圣魔皇后 塞勒涅 45819647
- Playstyle is reactive: set traps, pass, then convert every opponent move into Altergeist summons

- **Core Mechanic: Trap-Activation Engine**

- 多功能诈骗者 42790071 special summons itself from hand after any trap card you activate resolves, verified in script as EVENT_CHAIN_SOLVED with rp equals you and an ACTIVATE trap
- When 多功能诈骗者 special summons, it summons one other Altergeist from deck in defense, and the turn then locks you to Altergeist-only special summons in both directions: no non-Altergeist summon before the effect, none after
- 网络傀儡师 53143898 sets any Altergeist trap directly from deck when normal summoned, giving every turn a free trap
- 网络傀儡师 second effect trades one face-up Altergeist card sent to graveyard for one Altergeist monster revived from graveyard
- Traps revive from graveyard and recycle themselves: 幻变骚灵物化 35146019 revives a monster and later banishes itself from grave to add a trap, 幻变骚灵复苏 22024279 revives an Altergeist link and later banishes itself to perform one Altergeist summon
- Link monsters trigger on leaving the field, so the deck climbs links while searching: 十六巫赫斯提 1508649 adds any Altergeist card from deck when sent to grave, 隐私王班西 93503294 adds any Altergeist card from grave when sent to grave
- 幻变骚灵协议 27541563 is the floodgate: your Altergeist card effects cannot be negated while it is face-up, and it negates and destroys any opponent monster effect by sending one other face-up Altergeist card to grave

- **One-Card Combo: 网络傀儡师 setup**

- Starter: 网络傀儡师 53143898 alone in hand, no other cards needed
- Step 1: normal summon 网络傀儡师, effect one sets 幻变骚灵物化 35146019 or 幻变骚灵协议 27541563 from deck face-down
- Step 2: pass with one Altergeist monster and one set trap, which is the full control position
- Step 3: on the opponent turn, activating any trap triggers 多功能诈骗者 42790071 from hand if drawn, converting into the full engine
- Halt point: 灰流丽 14558127 on the set effect stops the trap; the deck has no other one-card starter

- **Two-Card Combo: Trap plus 多功能诈骗者**

- Starter: any trap card you can activate plus 多功能诈骗者 42790071 in hand
- Step 1: activate a trap, after it resolves 多功能诈骗者 special summons itself from hand
- Step 2: 多功能诈骗者 effect summons 网络傀儡师 53143898 from deck in defense, which sets a second trap from deck, usually 幻变骚灵物化 35146019
- Step 3: link the two into 十六巫赫斯提 1508649, or leave 网络傀儡师 for its graveyard revive next turn
- Step 4: 十六巫赫斯提 gains attack from linked Altergeist and negates a spell or trap activation by tributing a linked Altergeist, which then triggers its own grave search
- Halt point: 灰流丽 on the deck summon stops step 2, 无限泡影 10045474 or 效果遮蒙者 97268402 on 多功能诈骗者 stops the engine

- **End Field**

- 十六巫赫斯提 1508649 plus 网络傀儡师 53143898 plus two set traps, typically 幻变骚灵物化 35146019 and 幻变骚灵协议 27541563
- 幻变骚灵协议 makes all Altergeist effects unnegatable and negates one opponent monster effect per turn, 十六巫赫斯提 negates one spell or trap activation
- 恶意软件鬼火 27132400 revived from grave adds one more body for next turn link plays
- Stronger end board: climb to 管理提泰妮娅 61470213 which sets a trap from deck on link summon and steals an opponent effect monster in the main phase
- Finisher: 访问码语者 86066372 climbed over 神圣魔皇后 塞勒涅 45819647 to clear backrow and push for game

- **Extender: 个人欺骗攻击 engine**

- 个人欺骗攻击 53936268 is a continuous spell with a quick effect: shuffle one Altergeist card from hand or face-up field to deck, add one Altergeist monster from deck to hand
- Search 恶意软件鬼火 27132400 with it: the monster is added to hand other than by draw, so it special summons itself, then revives another Altergeist from grave in defense
- The engine loops: 网络傀儡师 53143898 sends Altergeist cards to grave for revives, 寻道梅露辛 25533642 searches on being sent to grave, 查询普卡 59185998 returns to hand whenever an Altergeist link is summoned
- Build quirk: in this codebase 个人欺骗攻击 is a continuous spell with setcode 0, so it is not an Altergeist card and cannot be set by 网络傀儡师 nor searched by Altergeist searches; it must be drawn or found by 金满而谦虚之壶 84211599

- **Extender: 像素妖精 and 一对一**

- 一对一 2295440 special summons a level 1 monster from deck, and 像素妖精 57769391, 寻道梅露辛 25533642, 渗透佩里 54126514, 查询普卡 59185998 are all level 1
- 像素妖精 57769391 tributes itself to excavate three cards, add one Altergeist card to hand, mill the rest, which feeds the grave for 幻变骚灵物化 and 网络傀儡师 revives
- 恶意软件鬼火 27132400 normal summon revives a grave Altergeist in defense but that revived monster's effects cannot activate that turn, so it only provides a body or link material

- **Extender: 隐私王班西 and defensive pieces**

- 隐私王班西 93503294 is a link 3 that in the main phase releases one other Altergeist to summon any Altergeist from deck into a zone it points to, and searches any Altergeist from grave when it goes to grave
- 警报食人水妖 85673903 in hand special summons itself when you link summon an Altergeist link, into a zone pointed to by another link monster, and turns that link into an Altergeist for the turn
- 查询昆提兰那克 52927340 in hand negates an opponent attack by special summoning itself, then negates one opponent face-up card while it remains on field
- 延迟菲芬尼拉 12977245 makes your other Altergeist monsters untargetable and unattackable, 击键录杜尔迦 76685519 steals an opponent grave monster when your Altergeist deals battle damage

- **Halt Points**

- 灰流丽 14558127 hits 多功能诈骗者 deck summon, 网络傀儡师 trap set, 个人欺骗攻击 search, and 像素妖精 excavate
- 无限泡影 10045474 and 效果遮蒙者 97268402 negate 多功能诈骗者 on the field, which freezes the whole engine
- 增殖的 G 23434538 and 欢聚友伴·茸茸长尾山雀 42141493 punish every special summon, so limit plays to one 多功能诈骗者 plus one deck summon under them
- 墓穴的指名者 24224830 banishes the grave targets of 幻变骚灵物化 and 幻变骚灵复苏, cutting recursion
- 技能抽取 82732705 is played in some variants and hurts field-trigger effects, but the trap and grave recursion still works, so play the deck as pure trap control under it

- **Mirror Match: 幻变骚灵 vs 幻变骚灵**

- Whoever resolves 多功能诈骗者 42790071 first wins tempo, so hand traps and 无限泡影 10045474 should be saved for the opponent 多功能诈骗者
- 幻变骚灵的闹鬼死锁 2547033 negates an opponent trap activation by discarding an Altergeist monster, and it can activate the turn it was set if set by an Altergeist card effect, making it a mirror breaker
- Bounce the opponent equipped 幻变骚灵物化 35146019 with 泛在羽衣精 89538537: the trap leaving the field destroys the monster it revived
- 幻变骚灵协议 27541563 decides the negate war: the side with protocol face-up keeps its engine alive while the other side's monsters and traps get negated
- 墓穴的指名者 24224830 stops the opponent grave recursion of 幻变骚灵物化 and 幻变骚灵复苏, so fire it on the first revived monster
- Kill 网络傀儡师 53143898 first, it is the trap settler that the whole field relies on

- **Common Mistakes**

- Do not special summon any non-Altergeist monster in the same turn you use 多功能诈骗者 deck summon, the turn locks to Altergeist only in both directions
- 网络傀儡师 second effect sends a face-up Altergeist card to grave, so never send an equipped 幻变骚灵物化 35146019: the trap leaving field destroys the revived monster
- 幻变骚灵复苏 22024279 only revives Altergeist link monsters, not main deck monsters, and its grave effect performs a summon only, not a special summon
- 幻变骚灵物化 destroys its monster when the trap leaves the field, so 泛在羽衣精 89538537 bounce of your own equipped 物化 is a self-destruct, not a dodge
- 恶意软件鬼火 revived monster's effects cannot activate that turn, do not expect a revived 网络傀儡师 to set a trap
- 幻变骚灵的闹鬼死锁 is a normal trap, its set-turn activation only applies when an Altergeist card effect set it, such as 网络傀儡师 or 管理提泰妮娅
- 十六巫赫斯提 negation requires tributing a monster in its linked zone, position links so an Altergeist body sits under it before the opponent turn
- 查询普卡 59185998 is a link material from hand but only for Altergeist links and only with at least one other Altergeist material, do not discard it as a cost
- Do not play 访问码语者 86066372 during the 多功能诈骗者 turn, the Altergeist-only lock blocks non-Altergeist special summons
