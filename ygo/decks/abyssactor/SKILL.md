---
name: abyssactor-experience
description: 魔界剧团 (Abyss Actor) deck experience: pendulum + 魔界台本 script engine, one-card combo, 奇幻剧场 script lock, halt points
---
# 魔界剧团 (Abyss Actor) Deck Experience

- **Deck Identity**

- All main monsters are DARK Fiend Pendulum monsters (race Fiend, attribute DARK); the deck is a pendulum deck whose real engine is the 魔界台本 continuous spell set
- Engine monsters: 狂放新秀 51391183 (scale 2, searches on destroy), 启幕人 44179224 (scale 7, self-summon + script mill), 大明星 25629622 (scale 3, level 7 boss), 临时演员 88412339 (scale 3, scale-setter), 圆熟女主演 78310590 (scale 0, level 7 recursion), 高超导演 2368215 (Link-1), 超级制作人 47404795 (Link-2)
- Scripts (魔界台本 spells): 魔王的降临 13662809, 戏剧性故事 33503878, 开幕式 23784496, 浪漫的告白者 41803903, 魔界的宴咜女 70564929, 幻想魔法 87390798, 火龙的住处 50179591
- Support: 奇幻剧场 77297908 (field spell, the lock), 谢幕 4682617 (mass recursion), 进入后台 59057953 (stock extra deck), 逃命马车 86578200 (protection)
- Role monsters: 恶魔反派 52240819 (level 8, 3000 ATK beater), 闪烁小明星 7279373 (scale 9, triple attack), 插科打诨角色 15308295 (control swap), 自由剧作家 65477143 (script setter), 可爱女主角 24907044, 莽撞新人 51028231, 花花配角 39024589, 时髦笑星 99634927
- Repo build families: pure toolbox (200418魔界剧团), 勇者 token + 超融合 (210828魔界剧团勇者衍生物融合), 刻魔 Fiendsmith + 破械 Unchained (240427魔界剧团刻魔破械, 241026魔界剧团刻魔)

- **Core Mechanic: Pendulum + 台本 Script Engine**

- Set two scales and pendulum summon every turn; 狂放新秀 51391183 pendulum effect changes the other 魔界剧团 scale to 9, opening levels 3-8 for 大明星 25629622 and 圆熟女主演 78310590; 圆熟女主演 scale 0 pairs with the 8-scales (自由剧作家 65477143, 插科打诨角色 15308295, 花花配角 39024589, 时髦笑星 99634927) for levels 1-7
- Destroyed pendulum monsters go face-up to the extra deck; recursion lives on that stock: 启幕人 44179224 sends a 魔界台本 from deck to grave then adds a face-up 魔界剧团 pendulum from extra to hand (its pendulum effect special summons itself from the PZ once per duel when your field is empty)
- 高超导演 2368215 (Link-1, material 1 魔界剧团 pendulum): special summons 1 card from your PZ, then places a different 魔界剧团 pendulum from deck or face-up extra into the freed PZ; afterwards only 魔界剧团 can be summoned or special summoned until end of turn
- 超级制作人 47404795 (Link-2, needs a Fiend among materials): quick effect in a main phase destroys 1 face-up card you control, then sets 奇幻剧场 77297908 from deck to the field zone or places a 魔界剧团 pendulum from deck into your PZ
- 大明星 25629622: on summon the opponent cannot activate spell/trap effects for the rest of that chain (script chain limit, monster effects still allowed); its ignition effect sets 1 魔界台本 spell from deck (auto-destroyed at end phase); its pendulum effect tributes a 魔界剧团 to recycle a script from grave
- Every 魔界台本 floats: destroyed while SET by an OPPONENT's card effect (script checks opponent as the destroyer, previous position face-down) with a face-up 魔界剧团 pendulum in your extra deck triggers the ② effect: search / bounce / draw / set more scripts / special summon pendulums / banish extra
- 圆熟女主演 78310590: on EVERY script effect activation including the floats it special summons a level 4 or lower 魔界剧团 pendulum from deck (returns to hand at end phase); ATK +100 per script in grave; special summons itself from hand when your pendulum monster is battle-destroyed
- 谢幕 4682617 (needs a 魔界台本 effect activated this turn, verified per-turn activity counter) adds up to your script count in grave face-up pendulums from extra to hand, then special summons up to that many from hand with different names; 进入后台 59057953 adds 2 different 魔界剧团 pendulums from deck to the face-up extra when 2 魔界剧团 cards are in your PZ

- **One-Card Combo: 魔界剧团的彩排**

- 彩排 6004133 must be the FIRST activation of Main Phase 1 (script condition: main phase 1 with no phase activity yet): add 1 魔界剧团 card plus 1 魔界台本 spell from deck; its restriction only blocks non-魔界剧团 PENDULUM summons (script checks the pendulum summon type), so generic special summons stay legal
- Starter line: 彩排 6004133 → 狂放新秀 51391183 + 戏剧性故事 33503878; normal summon 狂放新秀, activate 戏剧性故事 targeting it → special summon 大明星 25629622 from deck, then destroy 狂放新秀 (or move it to the PZ) → 狂放新秀's destroy trigger adds 启幕人 44179224 from deck
- Link 高超导演 2368215 off 大明星, place 启幕人 into the PZ, 高超导演 effect special summons 启幕人 and places 圆熟女主演 78310590 from deck into the PZ; 启幕人 effect mills 开幕式 23784496 and adds the destroyed 狂放新秀 back from the face-up extra deck
- Link 超级制作人 47404795, pay 1000 LP with 圆熟女主演's pendulum effect to add 自由剧作家 65477143, then pendulum summon 大明星 + 狂放新秀 + 启幕人 from hand or face-up extra (scales: 圆熟女主演 0 + 自由剧作家 8)
- 大明星 sets 魔界的宴咜女 70564929 from deck, activate it tributing 启幕人 to set 开幕式 23784496 from grave, then 超级制作人 quick effect destroys 宴咜女 to set 奇幻剧场 77297908 from deck
- Honest note: 彩排 6004133 alone only nets one monster plus one script; the full line needs follow-up pieces (启幕人 44179224, 狂放新秀 51391183, 大明星 25629622, 高超导演 2368215), so treat 彩排 as the seed and extend from whatever the hand offers
- Alternative documented starter: 启幕人 44179224 + 彩排 6004133 — 启幕人 self-summons, mills a script and recycles 狂放新秀; 戏剧性故事 33503878 pops 狂放新秀 to summon 大明星, and the engine repeats into 超级制作人 + 奇幻剧场

- **End Field: 奇幻剧场 Script Lock**

- 奇幻剧场 77297908 active with at least one PENDULUM-SUMMONED 魔界剧团 pendulum on your field: every opponent monster effect activation is replaced at resolution with "destroy 1 face-down spell/trap on your own field" (script swaps the chain operation, once per turn), so their monsters cannot remove your board and self-destruct their own set cards
- The replaced destruction does not trigger their script floats because the destroying effect belongs to the opponent themselves, so the lock is safe even in the mirror
- Keep several SET 魔界台本 as payoff threats: 开幕式 23784496 (draw until 5 in hand), 戏剧性故事 33503878 (bounce up to 2 cards), 魔王的降临 13662809 (search up to 2), 浪漫的告白者 41803903 (set more scripts from deck), 幻想魔法 87390798 (put 1 opponent card on top of deck), 魔界的宴咜女 70564929 (special summon pendulums from deck), 火龙的住处 50179591 (banish 3 from opponent extra after battle destroy)
- Bodies on board: 大明星 25629622 (set one script every turn), 圆熟女主演 78310590 (chain special summon off every script activation), 恶魔反派 52240819 (3000 ATK, summon drops an opponent monster ATK by 1000 x your 魔界剧团 count), 闪烁小明星 7279373 (triple attack finisher)
- 魔王的降临 13662809 breaks boards: destroy up to the number of different attack-position 魔界剧团 names you control face-up cards, and with a level 7+ 魔界剧团 on field the opponent cannot respond to its activation at all

- **Extenders**

- 高超导演 2368215 recursion turns any PZ pendulum into a body plus a fresh scale from deck; 超级制作人 47404795 turns any own face-up card into 奇幻剧场 77297908 or another scale
- 戏剧性故事 33503878 special summons any different-name 魔界剧团 from deck off any face-up pendulum, then moves or destroys the target to trigger its float
- 浪漫的告白者 41803903 bounces one pendulum to hand to special summon a different name from the face-up extra deck in defense; floats into multiple scripts from deck
- 魔界的宴咜女 70564929 tributes a 魔界剧团 to set any script from grave, twice per turn — the grave loop engine
- 自由剧作家 65477143 pendulum effect discards 1 card on an attack declaration to give the opponent a monster (enables 临时演员 88412339's self-summon condition); when special summoned from the PZ it reveals 3 scripts and the opponent sets 1 for you (destroyed at end phase); on destroy it recycles a script
- 谢幕 4682617 after a script activation: mass add from face-up extra then mass special summon from hand with different names, locked to 魔界剧团 pendulums afterwards
- 插科打诨角色 15308295 pendulum effect swaps control of an opponent monster with one of your 魔界剧团 pendulums (the Comedian itself is destroyed and stocks the extra deck); its monster form is a control-shift stall trick
- 莽撞新人 51028231 protects one 魔界剧团 per turn, special summons a level 4 or lower 魔界剧团 from deck when destroyed, and pops a level 4 or lower monster when destroyed in the PZ
- 可爱女主角 24907044 sets a 魔界台本 from deck when destroyed, and drops the attacker ATK by battle damage taken; 恶魔反派 52240819 sets a script from grave after battle destruction
- Modern engine extenders from the repo builds: 刻魔 engine (刻魔的咏圣 98567237, 刻魔的赞圣 35552985, 刻印群魔的刻魔锻冶师 60764609, 闭锁天之月 71818935, 召唤女巫 61665245) into 高超导演 and 超级制作人, 破械神王 阎摩 24269961, 勇者 engine (阿拉弥赛亚之仪 3285551, 圣殿的水遣 30680659, 流离的狮鹫骑手 2563463), 超融合 48130397, 小世界现象 89558743, and in pure builds the pendulum toolbox (刚炼装勇士·银金公主 24094258, 刻读之魔术士 12289247, 宙读之魔术士 76794549, 访问码语者 86066372)

- **Halt Points**

- 彩排 6004133: only at the very start of Main Phase 1 before any other action (script checks no phase activity)
- 狂放新秀 51391183 pendulum effect locks special summons to 魔界剧团 until end of turn — activate it only right before the pendulum summon, never before the 刻魔 or 勇者 engine
- 临时演员 88412339 tribute effect locks special summons to 魔界剧团 and locks its own pendulum effect — play it as the last extender
- 高超导演 2368215 effect locks normal and special summons to 魔界剧团 until end of turn — play every non-archetype extender first
- 圆熟女主演 78310590 pendulum search (pay 1000 LP) locks special summons to 魔界剧团 pendulums
- 谢幕 4682617 requires a 魔界台本 effect activation this turn (per-turn activity counter, script-verified) and locks special summons to 魔界剧团 pendulums — activate a script first
- 魔王的降临 13662809 cannot activate without an attack-position 魔界剧团 on your field, and its no-response clause needs a level 7+ 魔界剧团 (大明星 25629622 or 圆熟女主演 78310590)
- The 奇幻剧场 77297908 lock needs a PENDULUM-SUMMONED monster: special summons from 高超导演, 戏剧性故事 or 圆熟女主演 do not count (script checks the pendulum summon type), and the replacement only fires once per turn
- 大明星 25629622's spell/trap lock lasts only the current chain, not the whole turn — do not rely on it for later chains
- Script floats need the card destroyed while face-down by an OPPONENT effect plus a face-up 魔界剧团 pendulum in your extra deck — never self-destroy set scripts and keep the extra stocked
- 超级制作人 47404795 destroys one of YOUR OWN face-up cards — aim it at a script already used or a scale you are replacing

- **Mirror Match**

- Scripts float for the destroyed player: never destroy the opponent's SET 魔界台本 with your own effects, every pop feeds them a search or draw
- 魔王的降临 13662809 only hits face-up cards, so it is the clean mirror breaker — resolve it first with 大明星 25629622 (level 7+) on board so it cannot be responded to
- Whoever keeps 奇幻剧场 77297908 plus a pendulum-summoned monster first wins the monster game; under the lock the opponent's monster effects destroy their own face-down cards with no payoff
- 插科打诨角色 15308295 steals a pendulum-summoned monster and breaks the opponent's lock — hold it for their lock piece
- 大明星 25629622's summon stops the opponent chaining their set scripts — summon it before your own script activations to blank their responses
- The 谢幕 4682617 race is decided by scripts in grave and pendulums face-up in extra: mill with 启幕人 44179224 and keep destroyed pendulums in the extra deck instead of returning everything to hand

- **Common Mistakes**

- Activating 谢幕 4682617 before any 魔界台本 activation this turn — it fizzles (script-verified activity counter)
- Using 狂放新秀 51391183's scale change with nothing to pendulum summon, or before the 刻魔 / 勇者 engine summons
- Activating 彩排 6004133 after any other Main Phase 1 action — the activation is illegal
- Ending the turn with zero face-up 魔界剧团 pendulums in the extra deck — every script float, 启幕人 44179224, 谢幕 4682617 and 进入后台 59057953 dies
- Destroying your own set scripts with 魔王的降临 13662809 or 超级制作人 47404795 expecting floats — floats only trigger on opponent-effect destruction
- Forgetting 大明星 25629622's set script self-destroys at end phase — recycle it via 大明星's pendulum effect or 魔界的宴咜女 70564929
- 奇幻剧场 77297908 lock with only non-pendulum-summoned monsters on field (高超导演 / 戏剧性故事 / 圆熟女主演 summons do not count)
- Only 超级制作人 47404795 fetches 奇幻剧场 77297908 from deck (the field spell has no archetype setcode) — do not spend 超级制作人 carelessly
- Overextending under 增殖的G 23434538: pendulum summon plus 高超导演 plus 谢幕 chains many special summons — under G stop at 彩排 + one pendulum summon + set scripts
- Trading 恶魔反派 52240819 or 闪烁小明星 7279373 as link fodder when they are your lethal tools

- **Build Quirks (this codebase)**

- 圆熟女主演 78310590 is a MAIN-DECK pendulum monster here, not a Fusion (database type has no fusion bit and the script has no fusion materials) — play 3 copies, search and pendulum summon it freely; the real OCG card is a Fusion monster
- Setcodes: 魔界剧团 monsters 0x10ec, 魔界台本 spells 0x20ec; 奇幻剧场 77297908 and 逃命马车 86578200 have setcode 0 so generic archetype searchers miss them
- 逃命马车 86578200 is implemented as a Continuous Spell in this database: 魔界剧团 monsters survive battle once each turn, one target gains effect-protection until the opponent's end phase, and its float bounces all opponent cards when destroyed while set
- 彩排 6004133's restriction only constrains PENDULUM summons (script checks the summon type), so Fiendsmith and Brave engine special summons are safe after it
- Repo deck cores: 彩排 6004133 x3, 启幕人 44179224 x3, 高超导演 2368215 x3, 临时演员 88412339 x3, 超级制作人 47404795 x2-3, 狂放新秀 51391183 x2-3, 圆熟女主演 78310590 x2-3, 大明星 25629622 x1-3, plus 魔王的降临 13662809, 开幕式 23784496, 戏剧性故事 33503878, 魔界的宴咜女 70564929 and 奇幻剧场 77297908
- The repo .ydk files dump all cards into the main section without side-deck markers — read them as composition references, not legal deck structure
