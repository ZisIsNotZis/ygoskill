---
name: genex-experience
description: 次世代 (Genex) deck experience: searcher ladder, Level 10 synchro boss, attribute-lock, extenders, halt points
---
# 次世代 (Genex) Deck Experience

- **Deck Identity**

- Archetype family: 次世代 setcode 0x2, 真次世代 (Real Genex) setcode 0x1002, 盟军·次世代 (Ally Genex) setcode 0x2002, every IsSetCard 0x2 filter matches all three, so 真次世代 and 盟军·次世代 cards count as 次世代 for every search and effect
- Modern builds are WIND and DARK Machine Synchro midrange: the 真次世代 searcher ladder sets up the Level 10 boss 次世代兵器 还零 61775475, one negate plus a backrow wipe
- Legacy build is a WIND engine on 霞之谷的神风 15854426 with 次世代鼓风人 24432029 and 盟军·次世代鸟人兵 64034255, ending on the attribute-locked synchros
- Tuner pool: 次世代控制员 68505803 (Level 3 WIND Machine Normal Tuner, the classic material), 次世代再生品 51827737 (Level 1 DARK Machine), 真次世代预言机 10178757 (Level 1 DARK), 真次世代协调员 32744558 (Level 2 DARK), 真次世代图灵机 61052897 (Level 2 DARK), 盟军·次世代鸟人兵 64034255 (Level 3 DARK), 次世代鼓风人 24432029 (Level 4 WIND Spellcaster)
- Near-pure reference decks: 230722次世代 and 231125次世代 folders in the deck corpus, 40 main plus 15 extra, 兽带斗神“王者”轩辕十四 10604644 and 半魔导带域 71650854 are optional control packages

- **Core Mechanic: Searcher Ladder**

- 真次世代锅炉人 1533292 on normal summon adds a Level 2 真次世代 from deck, targets 真次世代破碎机 65149697, 真次世代图灵机 61052897, or 真次世代协调员 32744558
- 真次世代破碎机 65149697 on normal summon adds a Level 4 真次世代, targets 真次世代涡轮人 6256844, 真次世代加速器 73783043, 真次世代水精灵 34568783, or 真次世代终极人 46572756
- 真次世代涡轮人 6256844 on normal summon adds a Level 1 次世代, targets 次世代再生品 51827737, 次世代节能员 30399511, or 真次世代预言机 10178757
- 次世代节能员 30399511 on normal summon adds a Level 3 effect 次世代, targets 次世代水精灵 4904812, 盟军·次世代鸟人兵 64034255, 次世代后备品 16828633, or 次世代工作员 93882364, never 次世代控制员 68505803 because it is a Normal monster
- 次世代水精灵 4904812 on normal summon sends 1 WATER from deck to graveyard as cost, then adds 次世代控制员 68505803, dump 真次世代水精灵 34568783 to fuel its graveyard plays
- Every ladder rung is a normal-summon trigger, so without extra summons one turn plays only one rung
- 修复次世代控制员 8173184 is the extra-summon engine: Link-1 on any Level 4 or lower 次世代, on Link summon it recycles a 次世代 from graveyard to hand, and whenever a 次世代 card is added to your hand by an effect it normal summons 1 次世代 from hand, once per chain
- 修复次世代控制员 8173184 script is marked not fully implemented and its card text carries a cannot be used normally warning, treat the one-turn ladder as unreliable in this codebase until verified

- **Core Mechanic: Attribute-Lock Synchros**

- The four classic synchros hard-lock their materials: exactly 次世代控制员 68505803 as tuner plus non-tuners of one fixed attribute
- 次世代风能人 43925870 is Level 7 WIND Machine, needs 次世代控制员 68505803 plus WIND non-tuners like 真次世代涡轮人 6256844, gains 300 attack per set card on the field and discards 1 to destroy a face-down card
- 次世代地热能人 33972299 is Level 6 EARTH, needs 次世代控制员 68505803 plus EARTH non-tuners like 次世代地矿人 89333528, swaps its 1800 attack with 2800 defense while a Level 4 or lower 次世代 is on field
- 次世代水能人 47421985 is Level 6 WATER, needs 次世代控制员 68505803 plus WATER non-tuners like 次世代水精灵 4904812, gains life points equal to the attack of monsters it destroys in battle
- 次世代热能人 6588580 is Level 8 FIRE, needs 次世代控制员 68505803 plus FIRE non-tuners like 次世代热炉人 53944920, gains 200 attack per FIRE in graveyard and burns 200 per 次世代 in graveyard when it destroys a monster
- 次世代再生品 51827737 copies the name of any 次世代 in graveyard until end phase, 次世代后备品 16828633 copies 次世代控制员 68505803 directly, both fill the controller tuner slot from a non-controller body
- 真次世代水精灵 34568783 banishes 1 次世代 from graveyard to adopt its attribute and optionally becomes a tuner until end phase, the flexible piece that satisfies any attribute-lock requirement
- 真次世代风筝 73483491 skips the controller lock, needs any 次世代 tuner plus WIND non-tuners, cannot be attacked while another monster is on field and searches any 次世代 when it destroys a monster

- **One-Card Combo: 真次世代锅炉人 1533292 into 次世代兵器 还零 61775475**

- Assumes 修复次世代控制员 8173184 works, without it the line stalls after the first search and the deck plays as midrange
- Step 1: normal summon 真次世代锅炉人 1533292, add 真次世代破碎机 65149697 from deck to hand
- Step 2: Link summon 修复次世代控制员 8173184 using 真次世代锅炉人 1533292, its Link summon effect adds 真次世代锅炉人 1533292 back from graveyard to hand
- Step 3: 修复次世代控制员 8173184 trigger on the added card grants a free normal summon, summon 真次世代锅炉人 1533292 again, its search adds 真次世代破碎机 65149697 which re-triggers the free summon
- Step 4: free normal summon 真次世代破碎机 65149697, its search adds 真次世代涡轮人 6256844 which re-triggers the free summon
- Step 5: free normal summon 真次世代涡轮人 6256844, its search adds 次世代再生品 51827737 which re-triggers the free summon
- Step 6: free normal summon 次世代再生品 51827737, field is 真次世代锅炉人 1533292, 真次世代破碎机 65149697, 真次世代涡轮人 6256844, 次世代再生品 51827737, and 修复次世代控制员 8173184
- Step 7: synchro 次世代兵器 还零 61775475 with 次世代再生品 51827737 as the DARK tuner plus the Level 3, 2, and 4 non-tuners, total 10
- Step 8: after 修复次世代控制员 8173184 summon effect resolves you may only special summon Synchro monsters from the extra deck and non-次世代 tuners cannot be synchro material, so stop after the synchro

- **End Field**

- One-card end field is 次世代兵器 还零 61775475 plus 修复次世代控制员 8173184, the ladder searches net one extra 次世代 in hand for next turn
- 次世代兵器 还零 61775475 quick effect negates and destroys any opponent monster effect by banishing 1 same-attribute card from graveyard as cost, then that attribute cannot be banished by this card again this turn
- 次世代兵器 还零 61775475 ignition once per turn shuffles 1 to 6 face-up 次世代 from graveyard or banished into deck, then destroys up to that many spell and trap cards on the field, clears both sides
- 真次世代黑机车人 38354937 is Level 9 and takes control of the opponent highest-level monster on synchro summon, but needs all DARK non-tuners so the pure build rarely reaches it
- 盟军·次世代加速人 66165755 is Level 8, discards 1 to revive a Level 4 or lower Machine from graveyard with doubled attack, banished at your end phase, the backup ladder payoff
- Generic synchro options from the same material pool: 加速同调星尘龙 30983281, 鲜花女男爵 84815190, PSY骨架王·Ω 74586817, 古代妖精龙 25862681, 冰结界的虎王 雪虎 70583986, 冰结界之龙 三叉龙 52687916, 念力终结处刑者 60465049, 天威之龙鬼神 5041348, 魔救之奇迹-巨龙晶石 9464441, 方程式运动员 电光赛道名将 33158448
- 加速同调星尘龙 30983281 revives a Level 2 or lower tuner from graveyard on synchro summon and re-synchros during the main phase to climb into 念力终结处刑者 60465049
- Utility extras: 暗次元的战士 109401 banishes a hand card to revive a banished DARK monster and burns 100 per set card each end phase, 灾厄之星 提·丰 93039339 answers link monsters, 欢快童话动物家族 81019803 and 虹光之宣告者 79606837 are Level 4 synchro speed bumps

- **Extenders**

- 一对一 2295440 discards 1 monster to special summon 次世代再生品 51827737, 次世代节能员 30399511, or 真次世代预言机 10178757 from deck, the best kickstart for the ladder
- 盟军·次世代鸟人兵 64034255 from hand returns 1 face-up monster you control to hand and special summons itself, gains 500 attack if the returned monster was WIND, banished when it leaves the field
- 真次世代协调员 32744558 on normal or special summon special summons 1 Level 3 or lower 次世代 from hand, extends any ladder rung
- 真次世代预言机 10178757 special summons itself whenever a 次世代 effect adds it from deck to hand, but can only be synchro material for 次世代 synchros
- 真次世代图灵机 61052897 special summons itself from hand during the opponent main phase and immediately synchro summons a 次世代 synchro, the only opponent-turn play, and counts as Level 3 when material for 次世代 synchros
- 次世代再生品 51827737 name-copy and 次世代后备品 16828633 name-copy open the attribute-locked synchros without 次世代控制员 68505803
- 真次世代水精灵 34568783 graveyard effect returns itself and 1 次世代 from graveyard to hand while a 次世代 synchro is on field, but for the rest of the turn cards you own banish instead of going to graveyard
- 真次世代加速器 73783043 special summons a 次世代 card added to your hand from deck, every search becomes an extra body while it is on field
- 暗次元的战士 109401 turns the banished pile left by 次世代兵器 还零 61775475 negates into revived DARK monsters
- Legacy WIND loop: 霞之谷的神风 15854426 special summons a Level 4 or lower WIND from deck when a WIND monster returns to hand, 盟军·次世代鸟人兵 64034255 bounces 次世代鼓风人 24432029 which then searches a DARK 次世代
- Staples: 墓穴的指名者 24224830 and 抹杀之指名者 65681983 protect the graveyard recursion, 贪欲之壶 67169062 recycles spent ladder pieces

- **Halt Points**

- 灰流丽 14558127 on any ladder search stops the chain, hitting 真次世代锅炉人 1533292 or 真次世代涡轮人 6256844 kills the one-card line
- 增殖的G 23434538 is live against the one-turn ladder because 修复次世代控制员 8173184 triggers five or more extra summons, stop at two summons when it resolves
- 原始生命态 尼比鲁 27204311 drops after the fifth summon of the ladder, the Repair line always crosses the five-summon threshold
- 效果遮蒙者 97268402 and 无限泡影 10045474 negate the summon triggers of the searchers, 真次世代水精灵 34568783 attribute change is an ignition and also vulnerable
- 墓穴的指名者 24224830 on 次世代再生品 51827737 or 真次世代水精灵 34568783 removes the tuner and the attribute flexibility
- 次世代水精灵 4904812 sends its WATER as cost, so the graveyard dump cannot be negated but the follow-up 次世代控制员 68505803 search can
- 重力崩坏 7811875 is a counter trap in the builds that sends your own face-up synchro to graveyard to negate a summon and locks the opponent out of summoning, play around it by keeping a spare tuner

- **Mirror Match**

- Both players race to 次世代兵器 还零 61775475, the first one who resolves the backrow wipe wins the backrow war
- Keep 墓穴的指名者 24224830 for 次世代再生品 51827737 and 真次世代水精灵 34568783, removing recursion wins the grind
- 半魔导带域 71650854 during your main phase 1 protects your synchro line from targeting and destruction, but blocks your own field spell activations
- 真次世代黑机车人 38354937 steals the opponent boss on summon, the pure builds trade it for the consistent Level 10
- 暗次元的战士 109401 burn is slow but the set-card count is usually high in the mirror, every set backrow is 100 damage per end phase

- **Common Mistakes**

- Do not plan the one-turn ladder around 修复次世代控制员 8173184, its script is marked not fully implemented and the card text warns it cannot be used normally, verify it works before committing the line
- After 修复次世代控制员 8173184 summon effect, only Synchro summons from the extra deck are allowed and non-次世代 tuners cannot be material, do not attempt Xyz or Link plays in that turn
- 次世代节能员 30399511 searches only Level 3 effect 次世代, never use it to fetch 次世代控制员 68505803, that is 次世代水精灵 4904812 job
- 真次世代锅炉人 1533292 searches only Level 2 真次世代 and 真次世代涡轮人 6256844 only Level 1 次世代, do not point them at the wrong rung
- 真次世代水精灵 34568783 graveyard recursion locks your own graveyard for the rest of the turn, sequence it after all graveyard milling is done
- 次世代兵器 还零 61775475 quick negate banishes a matching-attribute graveyard card and then forbids that attribute for the rest of the turn, do not waste the only card of the needed attribute
- 次世代兵器 还零 61775475 ignition shuffles your own 次世代 into deck, it removes graveyard fuel for 次世代热能人 6588580 and recursion, use it only when the destruction matters
- 盟军·次世代鸟人兵 64034255 is banished when it leaves the field, do not bounce it into 霞之谷的神风 15854426 loops expecting it back
- 真次世代预言机 10178757 can only be synchro material for 次世代 synchros, never feed it to generic ones
- 真次世代图灵机 61052897 counts as Level 3 for 次世代 synchros, level math changes when it is the tuner
- 真次世代黑机车人 38354937 requires all DARK non-tuners, the pure build has almost none, do not assume it is reachable
- 半魔导带域 71650854 forbids activating or setting field spells, 星球改造 73628505 and 圆盘斗技场 84792926 conflict with it on the same turn
