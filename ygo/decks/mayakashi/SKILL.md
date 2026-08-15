---
name: mayakashi-experience
description: 魔妖 (Mayakashi) deck experience: synchro ladder, revival chain, link tops, extra-deck locks, halt points
---
# 魔妖 (Mayakashi) Deck Experience

- **Deck Identity**

- Zombie synchro-ladder deck in this codebase's custom rework: ladder synchro levels are 3/5/7/9/11 and the ladder is topped by three custom link monsters, a grind/recursion style where the extra deck never stays dead
- Main-deck members: 冰之魔妖-雪娘 72700231 (Level 1 tuner), 丽之魔妖-妲姬 42542842 (Level 2 tuner), 翼之魔妖-波旬 41729254 (Level 1), 辙之魔妖-车夫 78936551 (Level 3), 骸之魔妖-夜叉 77714963 (Level 5), 毒之魔妖-束胫 5325155 (Level 2)
- Ladder synchros: 辙之魔妖-胧车 30607616 (Level 3) → 毒之魔妖-土蜘蛛 77092311 (Level 5) → 翼之魔妖-天狗 4103668 (Level 7) → 丽之魔妖-妖狐 3486020 (Level 9) → 骸之魔妖-饿者髑髅 39475024 (Level 11)
- Link tops: 冰之魔妖-雪女 66870733 (LINK-2, exactly 2 魔妖), 垂冰之魔妖-雪女 36114945 (LINK-3, 2+ Zombies), 零冰之魔妖-雪女 2645637 (LINK-4, 2+ Zombies)
- Spell support: 魔妖回天 2364438 (search or mill), 魔妖变生 39753577 (revive), 逢华妖丽谭-魔妖不知火语 62219643 (turn lock), 逢华妖丽谭-魔妖语 83266006 (attribute revive); traps 魔妖坏劫 51225407, 魔妖游行 41867019
- Generic Zombie package: 马头鬼 92826944, 牛头鬼 52467217, 齐唱僵尸 49959355, 巨食尸鬼 魔杰拉 45154513, 一对一 2295440, 愚蠢的埋葬 81439173
- Hand traps seen in the pure build: 灰流丽 14558127, 增殖的G 23434538, 屋敷童 73642296, 欢聚友伴·茸茸长尾山雀 42141493, 小丑与锁鸟 94145021, 无限泡影 10045474, 恐龙摔跤手·潘克拉辛角龙 82385847, 墓穴的指名者 24224830
- Build quirk: 魔妖仙兽 (setcode 0xb3) pendulums such as 魔妖仙兽 独眼群主 21364070 and 魔妖仙兽 大刃祸是 93368494 are a separate archetype in this codebase; their effects and locks do not work with 魔妖 (setcode 0x121) cards
- Build variants: pure ladder (e.g. 240727), Zombie-mill with 名推理 58577036 and 吸收精气的骨塔 63012333, and a Horus rank-8 hybrid (荷鲁斯的荣光-伊姆塞特 84941194, 王之棺 16528181) with 真血公 吸血鬼 73082255 and No.38 希望魁龙 银河巨神 63767246

- **Core Mechanic: Synchro Ladder and Revival Chain**

- Every ladder synchro is 1 tuner + 1 or more non-tuners; the intended climber is 丽之魔妖-妲姬 42542842, a Level 2 tuner, because ladder synchro (odd level) + 妲姬 = next tier: 3→5→7→9→11
- 妲姬 42542842 grave trigger: when any 魔妖 monster is special summoned from the extra deck, revive this card from the grave (each copy once per turn); the turn it revives, you can only special summon 魔妖 monsters from the extra deck
- 波旬 41729254 on normal or special summon: special summon any other 魔妖 monster from the deck (usually 妲姬 to start the climb)
- 车夫 78936551 on normal or special summon: revive any other 魔妖 from your grave in defense with negated effects — a free 妲姬 revival that does not spend 妲姬's own once-per-turn trigger, and the revived tuner still works as synchro material
- Revival chain: each synchro revives itself from the grave by banishing 1 other Zombie from your grave when your next-tier synchro is destroyed by battle or the opponent's effect — 胧车 30607616 reacts to Level 5 (土蜘蛛), 土蜘蛛 77092311 to Level 7 (天狗), 天狗 4103668 to Level 9 (妖狐), 妖狐 3486020 to Level 11 (饿者髑髅)
- 饿者髑髅 39475024 instead revives when your LINK monster is destroyed by battle or the opponent's effect, tying the synchro ladder to the link tops; destroying the board cascades the whole ladder back up from the grave
- On-revive payoffs (trigger only when special summoned from the grave, not from the extra deck): 胧车 30607616 makes your monsters indestructible by battle this turn; 土蜘蛛 77092311 mills 3 cards from each player's deck; 天狗 4103668 destroys 1 opponent spell or trap; 妖狐 3486020 destroys 1 opponent monster; 饿者髑髅 39475024 becomes unaffected by other card effects until the end phase
- 束胫 5325155 grave trigger: when your 魔妖 monster (other than itself) is destroyed by battle or the opponent's effect, revive itself, with the 魔妖-only extra deck lock for that turn
- Archetype floodgate: while 雪娘 72700231, 波旬 41729254, 车夫 78936551 or 夜叉 77714963 is on the field, you cannot special summon non-魔妖 monsters from the extra deck — this applies to you too
- 雪娘 72700231 ignition from hand or grave: revive itself when any face-up 魔妖 (other than itself) is on the field, then send 1 Zombie from deck to grave, setting up 妲姬, 马头鬼 92826944 or 魔杰拉 45154513

- **One-Card Combo: 魔妖回天**

- Activate 魔妖回天 2364438 and add 波旬 41729254 to hand (the send-to-grave mode is for dumping 妲姬 or 马头鬼 92826944 in setup turns)
- Normal summon 波旬, its effect special summons 妲姬 42542842 from the deck
- Synchro 辙之魔妖-胧车 30607616 with 波旬 (Level 1) + 妲姬 (Level 2); 妲姬 in the grave triggers on the extra-deck summon and revives itself
- Synchro 毒之魔妖-土蜘蛛 77092311 with 胧车 (Level 3) + 妲姬 (Level 2)
- End field: 土蜘蛛 plus 妲姬, ladder armed — if 土蜘蛛 is destroyed by battle or opponent effect, 胧车 revives from the grave (banishing 1 Zombie) and grants battle indestructibility
- Full climb needs more revivals: each 妲姬 copy revives once per turn, so dump extra copies with 魔妖回天 2364438, 雪娘 72700231, 牛头鬼 52467217 or 愚蠢的埋葬 81439173, and extend with 车夫 78936551 or 魔妖变生 39753577
- With revivals: 土蜘蛛 + 妲姬 → 天狗 4103668 (Level 7); 天狗 + 妲姬 → 妖狐 3486020 (Level 9); 妖狐 + 妲姬 → 饿者髑髅 39475024 (Level 11)
- Link climb on top with leftover Zombie bodies: 冰之魔妖-雪女 66870733 (exactly 2 魔妖, e.g. 饿者髑髅 + 妲姬), then 垂冰之魔妖-雪女 36114945 (link rating 3), then 零冰之魔妖-雪女 2645637 (link rating 4); 魔杰拉 45154513 and 马头鬼 92826944 supply extra bodies
- Alternative tuning: 齐唱僵尸 49959355 (Level 3 tuner) raises a monster's level by 1 with a discard, or mills a Zombie from deck and raises by 1, hitting the odd ladder levels from other tuner/non-tuner combos
- Under 增殖的G 23434538 or 欢聚友伴·茸茸长尾山雀 42141493, stop after 波旬 + 妲姬, or at 胧车, and pass with the floodgate up

- **End Field**

- 零冰之魔妖-雪女 2645637 (LINK-4): negates opponent monster effects that activate while banished; twice per turn, when a monster is special summoned from a grave or a grave monster effect activates, set one other face-up monster's attack to 0 and negate its effects
- 垂冰之魔妖-雪女 36114945: on summon negates 1 opponent effect monster; quick effect from the grave, also on the opponent turn, banishes itself to revive 1 Zombie synchro from the grave or banished zone
- Keep one ladder synchro alive, preferably 饿者髑髅 39475024 (effect immunity when revived from grave) or 妖狐 3486020 (monster destruction)
- 冰之魔妖-雪女 66870733: link it to a synchro so it cannot be battle targeted; when your synchro is destroyed by battle or opponent effect, halve one face-up monster's attack and defense
- Grave pieces: 妲姬 42542842 revives on any extra-deck 魔妖 summon, 束胫 5325155 revives on your 魔妖 destruction, 魔杰拉 45154513 replaces your Zombie's destruction, 马头鬼 92826944 banishes itself to revive any Zombie
- Play 逢华妖丽谭-魔妖不知火语 62219643 last: release 1 魔妖 or 不知火 synchro or link monster, then both players cannot special summon from hand, deck or extra deck this turn — your grave-based ladder revivals still work under it
- Set 魔妖坏劫 51225407: opponent monsters lose 100 attack and defense per different 魔妖 name in your grave, plus grave recursion (banish itself and 1 Zombie to revive a 魔妖)
- 魔妖游行 41867019: each time a Zombie synchro is summoned from somewhere other than the extra deck (ladder revivals), pick one of draw 1, set a 魔妖 spell or trap from deck, send opponent's lowest-attack monster to grave, or deal 800 damage, each option once per turn

- **Extenders**

- 一对一 2295440: discard 1 monster, special summon 雪娘 72700231 from the deck (Level 1 tuner)
- 魔妖变生 39753577: discard 1 card, revive 1 魔妖 from your grave or banished zone with target protection; locks extra deck summons to 魔妖 this turn
- 马头鬼 92826944: banish itself from the grave, revive any Zombie from your grave with no lock
- 牛头鬼 52467217: main phase, send 1 Zombie from deck to grave; when sent to grave, banish another Zombie from grave to special summon 1 Zombie from hand
- 夜叉 77714963: from hand, discard another 魔妖 monster to special summon itself as a Level 5 body (with 妲姬 42542842 that is 天狗 4103668)
- 束胫 5325155: board-wipe insurance — your 魔妖 destroyed by battle or opponent effect revives it from the grave
- 魔杰拉 45154513: from hand or grave, replaces your Zombie's destruction once per turn by banishing itself; when banished, for example as ladder revival fodder, revives itself in defense and may drop 1 level
- 垂冰之魔妖-雪女 36114945 grave quick effect revives Zombie synchros from grave or banished zone, giving the ladder a second life on the opponent turn
- 逢华妖丽谭-魔妖语 83266006: main phase, revive a Zombie from grave or banished zone with the same attribute as a Zombie synchro you control — the ladder covers WATER (雪娘 72700231, 雪女 66870733), FIRE (妲姬 42542842, 妖狐 3486020), WIND (波旬 41729254, 天狗 4103668), EARTH (车夫 78936551, 胧车 30607616, 土蜘蛛 77092311) and DARK (夜叉 77714963, 饿者髑髅 39475024); the revived monster is banished at end phase and non-Zombie summons are locked after activation
- 魔妖坏劫 51225407 grave effect: banish itself and 1 Zombie from grave, revive 1 魔妖 from grave

- **Halt Points**

- 灰流丽 14558127 on 魔妖回天 2364438 search, on 波旬 41729254 deck summon, or on 雪娘 72700231 self-revival kills the starter line
- 灰流丽, 屋敷童 73642296 or 墓穴的指名者 24224830 on 妲姬 42542842 grave trigger stalls the ladder at the current tier
- Banishing 妲姬 or 马头鬼 92826944 from the grave removes the climb fuel
- 增殖的G 23434538 and 欢聚友伴·茸茸长尾山雀 42141493 punish the many special summons; play the one-to-two-summon 波旬 + 妲姬 line under them
- 原始生命态 尼比鲁 27204311 lands on the fifth special summon of a full climb; stop before five summons or hold 墓穴的指名者 24224830
- Grave-banishing effects (次元吸引者 91800273 style) kill the engine: 妲姬, 束胫 5325155, ladder revivals, 马头鬼, 垂冰之魔妖-雪女 36114945 and 魔妖变生 39753577 all need the grave, and every ladder revival cost banishes a Zombie
- The extra-deck floodgate: once 雪娘 72700231, 波旬 41729254, 车夫 78936551 or 夜叉 77714963 is on the field, generic extra monsters such as 鲜花女男爵 84815190, 真血公 吸血鬼 73082255, 访问码语者 86066372 and No.38 希望魁龙 银河巨神 63767246 cannot be summoned — in the Horus hybrid, make the rank-8s first, then the 魔妖
- 零冰之魔妖-雪女 2645637 needs another face-up monster as its target and allows only 2 activations per turn — do not rely on it alone

- **Mirror Match**

- First 零冰之魔妖-雪女 2645637 wins the grind: it negates grave monster effects (妲姬 42542842, 束胫 5325155, 马头鬼 92826944) and attack-zeroes monsters on grave plays
- Save 屋敷童 73642296 and 墓穴的指名者 24224830 for the opponent's 妲姬 rather than their searcher
- Destroy the opponent's ladder with YOUR effects: 妖狐 3486020 monster destruction and 天狗 4103668 spell or trap destruction do not trigger their 束胫 5325155, which needs opponent-caused destruction
- Whoever resolves 逢华妖丽谭-魔妖不知火语 62219643 with a board up first locks the other out of hand, deck and extra deck summons — the decisive play
- 魔杰拉 45154513 turns their 妖狐 or 天狗 removal into a free defense-position body for you
- Unique-on-field rules matter: 妲姬 42542842, 束胫 5325155 and every ladder synchro and link can only have one face-up copy — never stack two of the same name

- **Common Mistakes**

- Special summoning non-魔妖 extra monsters after a 魔妖 main monster is on the field — the archetype floodgate applies to you; sequence generic links and synchros first
- Wasting 妲姬 42542842 grave triggers (once per turn per copy) — do not revive her for one synchro when the climb needs her later
- 车夫 78936551 revives with negated effects: the revived 妲姬 is still a tuner, but her own grave trigger is a separate effect that remains available, so plan which copy does what
- 土蜘蛛 77092311 mills 3 from BOTH decks and only when revived from the grave, not on an extra-deck summon — it can fuel opponent grave engines, so do not mill into them needlessly
- 垂冰之魔妖-雪女 36114945 grave quick effect banishes itself, losing the negate body — only use it when the ladder revival matters more
- Activate 逢华妖丽谭-魔妖不知火语 62219643 last: it locks you too, so anything left unplayed from hand, deck or extra deck is dead that turn
- 零冰之魔妖-雪女 2645637 cannot target itself and is optional — against one big monster with no grave plays its negation may be unusable
- 魔妖坏劫 51225407 attack reduction counts different 魔妖 NAMES in the grave — milling duplicates does not stack it
- 雪娘 72700231 needs another face-up 魔妖 (not itself) to revive — do not open with it alone unless 波旬 41729254 or 魔妖回天 2364438 is available
- 魔妖游行 41867019 needs a non-extra-deck Zombie synchro summon, so it does nothing on your initial extra-deck ladder summons and only pays off on grave revivals
- 魔妖仙兽 (setcode 0xb3) cards are a different archetype — their pendulum effects and summon locks do not interact with 魔妖 (setcode 0x121) cards
