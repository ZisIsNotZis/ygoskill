---
name: ghostrick-experience
description: 鬼计 (Ghostrick) deck experience: flip control engine, one-card play, extenders, halt points
---
# 鬼计 (Ghostrick) Deck Experience

- **Deck Identity**

- 鬼计 (Ghostrick) is a DARK flip-control deck: every main-deck monster is Level 1-3 DARK with low ATK (highest is 鬼计科学怪人 16279989 at 1600), built to sit face-down, flip for effects, and flip back down
- All main-deck Ghostrick monsters share two rules, verified in scripts such as c27491571.lua: they cannot be face-up Normal Summoned unless you control a face-up Ghostrick, and once per turn they can change themselves to face-down Defense
- The shared setcode is 0x8d in scripts (IsSetCard(0x8d)), so 鬼计节 35871958 and all Xyz count as Ghostrick for summon conditions and effects
- The three 三灾 field spells are 鬼计之馆 99795159, 鬼计游行 29400787, 鬼计博物馆 7617062: all forbid attacking face-down monsters and allow direct attacks when the opponent controls only face-down monsters
- Xyz lineup: 鬼计妖魔·阿鲁卡德 75367227 (Rank 3, pops set cards), 鬼计无头骑士 46895036 (Rank 1, quick ATK halve), 鬼计女夜魔 32224143 (Rank 2, destroy plus zone lock), 鬼计惰天使 53334641 (Rank 4, alternate win); the Link-1 鬼计节 35871958 is the modern engine card
- Trap core: 鬼计之夜 85827713, 鬼计匿影 50527144, 鬼计惊魂 86516889, 鬼计装修 61818176, 鬼计天旋地转 37055344, 鬼计心碎 80802524, 不给糖就搞鬼计 27170599
- Note on naming: there is no 鬼计的大洞, 鬼计·魔王, or 妖魔剑 in this card database; the fields are 鬼计之馆 99795159 / 鬼计游行 29400787 / 鬼计博物馆 7617062 and the top Xyz is 鬼计妖魔·阿鲁卡德 75367227
- Build quirk: the newest pure build (deck/250726鬼计) is a 60-card main with 鬼计节 35871958 x3, 鬼计惰天使 53334641 x2, 鬼计装修 61818176 x3, 鬼计曲线球 69809989 x3 and a 15-card extra; an older control build (deck/200808鬼计) runs 王家长眠之谷 47355498 and 熔岩魔神 102380 instead

- **Core Mechanic: Flip Control**

- Normal Set any Ghostrick face-down with no prerequisite (the summon limit only blocks face-up Normal Summon), then flip it on your own terms
- The 三灾 fields make face-down monsters safe: neither player can attack a face-down monster, and both players can direct attack when the opponent controls only face-down monsters
- Flip effects fire through your own position changes, not battle: 鬼计惊魂 86516889 flips your sets face-up Defense, 鬼计天旋地转 37055344 flips them face-up Attack during battle, 鬼计曲线球 69809989 flips one face-up Attack
- Flip payoff monsters: 鬼计僵尸 80885284 searches a Ghostrick whose Level is at most your Ghostrick count, 鬼计骷髅 51196805 banishes the opponent deck face-down, 鬼计妖精 36239585 recurs a Ghostrick from the GY, 鬼计狼人 72913666 burns for each set card, 鬼计人偶 46925518 flips the whole field face-down then extends
- 鬼计魔女 27491571 flips one opponent monster face-down each turn; 鬼计猫娘 24101897 flips any Level 4+ monster face-down the moment it is summoned while another Ghostrick is on your field
- 鬼计之夜 85827713 stops the opponent from flip summoning while you control a Ghostrick, and if the opponent destroys it they cannot attack that turn

- **One-Card Combo: 鬼计节 35871958**

- Starter: any single Ghostrick monster in hand, no field setup needed
- Step 1: Normal Set that Ghostrick face-down (always legal)
- Step 2: Link Summon 鬼计节 35871958 using the face-down monster, because its link procedure explicitly allows face-down Ghostrick materials (EFFECT_FLAG_SET_AVAILABLE)
- Step 3: 鬼计节 35871958 is itself a Ghostrick, so face-up Normal Summons of hand Ghostricks become legal this turn
- Step 4: with any 三灾 field spell in the field zone, 鬼计节 35871958 grants all your Ghostrick monsters direct attack
- Step 5: on the opponent attack declaration, tribute 鬼计节 35871958 to Special Summon any Ghostrick from deck face-down, keeping the engine live

- **End Field One-Card**

- 鬼计节 35871958 plus a set 鬼计僵尸 80885284 or 鬼计妖精 36239585, ready to flip on the opponent turn
- Direct attack threat through the field spell, plus the deck face-down Special Summon from 鬼计节 35871958 as a defensive float
- Halt point: the floating Special Summon is from deck, so Ash Blossom on 鬼计节 35871958 ends the value; the line itself does not search

- **Extender: 鬼计惰天使 53334641 Win Line**

- Alternative Xyz Summon: 鬼计惰天使 53334641 can be stacked onto any other face-up Ghostrick Xyz (e.g. 鬼计无头骑士 46895036 from 鬼计南瓜灯 54512827 plus 鬼计霜精 61318483, or 鬼计女夜魔 32224143 from two Level 2s), inheriting all materials
- Effect one: detach one material to add any Ghostrick spell or trap from deck to hand, typically 鬼计装修 61818176 or 鬼计曲线球 69809989
- Effect two: once per turn, attach one Ghostrick card from hand as material
- 鬼计曲线球 69809989 GY effect: banish itself and attach one Ghostrick card from the GY to a Ghostrick Xyz
- 鬼计装修 61818176 GY effect: banish itself and overlay a differently-named Ghostrick Xyz from the extra deck onto yours, transferring every material
- When 鬼计惰天使 53334641 accumulates exactly 10 materials you win the duel immediately, checked by the script on every event, so cycle Xyz and recycle 惰天使 with 鬼计曲线球 69809989 to stack repeatedly

- **Extender: 鬼计妖精 36239585**

- On flip: set one Ghostrick card from your GY, monster face-down or spell/trap face-down, then optionally flip up to [the number of your face-down cards] opponent face-up monsters face-down
- The set card is banished if it leaves the field, so it is one-shot recursion, not reusable loop fodder
- Pair with 鬼计惊魂 86516889 to flip 鬼计妖精 36239585 and 鬼计魔女 27491571 on the same turn for mass flip-down

- **Extender: 鬼计木乃伊 97584500 and 鬼计海妖 64804316**

- 鬼计木乃伊 97584500: while face-up it gives one extra Ghostrick Normal Summon per turn, but it locks you out of Special Summoning non-DARK monsters
- 鬼计海妖 64804316: on summon or flip, mill two cards, and if a Ghostrick was among them add a Ghostrick spell or trap from deck or flip one opponent effect monster face-down; the only Level 4 main-deck Ghostrick, so two copies make 鬼计惰天使 53334641 directly

- **Extender: Non-archetype Techs**

- 瘴烟之死灵术师 69176851 (Link-2): send one spell or trap from hand or field to the GY for an extra Spellcaster Normal Summon, which covers the Level 2 Ghostrick spellcasters like 鬼计魔女 27491571; its level 5+ spellcaster revive is dead in a pure build
- S：P小夜骑士 29301450 (Link-2): generic banish removal, beware 鬼计博物馆 7617062 stops its attacks
- 无光之影 阿-宝·阿·库 4731783 (Link-4): discard one card in either main phase to pop a card or banish itself and revive a LIGHT or DARK monster from the GY, useful with all-DARK Ghostricks
- 不给糖就搞鬼计 27170599: with a Ghostrick field spell or 鬼计节 35871958 on your side, target one opponent monster, who either pays 2000 LP (the trap re-sets itself) or loses attack, effects, and gets flipped face-down at the end phase; that end-phase flip ignores immunity

- **Halt Points**

- Ash Blossom answers: 鬼计惰天使 53334641 search, 鬼计节 35871958 floating Special Summon, 鬼计妖精 36239585 GY set, 鬼计曲线球 69809989 revive, 鬼计海妖 64804316 mill-add
- Effect negation on 鬼计魔女 27491571 and 鬼计惰天使 53334641 stalls the flip and search engine; negating 鬼计猫娘 24101897 blanks the Level 4+ flip
- Backrow removal like 雷击 and 羽扫 clears 鬼计之夜 85827713 and 鬼计装修 61818176; hold 鬼计匿影 50527144, which grants one turn of targeting and destruction immunity to all your Ghostrick cards and face-down monsters
- 王家长眠之谷 47355498 and 次元吸引者 91800273 cut the GY recursion used by 鬼计曲线球 69809989, 鬼计装修 61818176, 鬼计妖精 36239585 and 鬼计无头骑士 46895036
- Unaffected monsters (e.g. 俱舍怒威族, 荷鲁斯) cannot be flipped by 鬼计魔女 27491571 or 鬼计惊魂 86516889; out them with 鬼计女夜魔 32224143 destroy, bounded by your total Ghostrick ATK, or let 不给糖就搞鬼计 27170599 end-phase flip-down resolve
- 增殖的G: the 鬼计惰天使 53334641 line Special Summons repeatedly; under G, set monsters and pass on traps instead of extending

- **Mirror Match: 鬼计 vs 鬼计**

- The 三灾 fields are symmetric, so direct attack and who resolves 鬼计之夜 85827713 first decide the game
- 鬼计天旋地转 37055344 is the mirror breaker: flip your own set face-up Attack then flip their face-up monster face-down, or flip their set face-up Attack so it becomes attackable
- 鬼计妖魔·阿鲁卡德 75367227 is the only in-archetype out to the opponent set monsters, popping face-down cards
- Keep 鬼计南瓜灯 54512827 and 鬼计霜精 61318483 in hand as battle answers; they Special Summon themselves face-down and stop the direct attack
- Whoever leaves a face-up Xyz standing first loses it to 鬼计女夜魔 32224143 or 鬼计天旋地转 37055344; prefer ending on face-downs

- **Common Mistakes**

- Trying to face-up Normal Summon without a Ghostrick already on the field is illegal; Normal Set is always legal instead
- Attacking face-down monsters under your own 三灾 field, because the field blocks your attacks too; pop sets with 鬼计妖魔·阿鲁卡德 75367227 or flip them with 鬼计天旋地转 37055344 first
- Forgetting 鬼计游行 29400787 zeroes all damage the opponent takes, so it is a search engine, not a beatdown field
- 鬼计博物馆 7617062 locks your non-Ghostrick monsters out of attacking, so S：P小夜骑士 29301450 and 无光之影 阿-宝·阿·库 4731783 cannot attack under it
- Summoning non-DARK monsters while 鬼计木乃伊 97584500 is face-up violates its Special Summon lock, including LIGHT S：P小夜骑士 29301450
- Detaching 鬼计惰天使 53334641 materials carelessly, because each detach moves the count away from the 10-material win
- 鬼计装修 61818176 GY rank-up needs a face-up Ghostrick Xyz and a differently-named Ghostrick Xyz in the extra deck, and the target must not be unaffected
- Treating 鬼计妖精 36239585 set recursion as reusable, when the set card is banished on leaving the field
- 不给糖就搞鬼计 27170599 re-sets itself if the opponent pays 2000 LP, so do not expect that copy in the GY, and it cannot activate without a Ghostrick field spell or 鬼计节 35871958
- 鬼计心碎 80802524 revives two Ghostricks with names different from the destroyed monster, so choose revival targets that are not the destroyed name
- Ending turns with face-up monsters only; face-downs dodge targeting, 鬼计之夜 85827713, 鬼计匿影 50527144 and 鬼计心碎 80802524 all reward staying face-down
