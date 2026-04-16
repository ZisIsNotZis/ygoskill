# Deck Metrics and Thresholds

- **ydkshow Interpretation**

- mean greater than or equal to 2.0 and q90 equals 3: cross-variant core, must include
- mean 1.5 to 2.0 and q90 equals 3: core, some variants run 2, almost must include
- mean 1.0 to 1.5 and q90 equals 2 to 3: important support, environment dependent
- mean 0.5 to 1.0 and q90 equals 1 to 2: optional support, understand before choosing
- mean less than 0.5 and q90 equals 0 to 1: personal preference, exclude unless justified
- standard deviation greater than or equal to 1.0: multi-axis coexistence signal
- q75 greater than or equal to 3 and mean less than 1.0: some variants run full but others run zero

- **Hand Trap Ratios**

- Recommended: Ash Blossom 3, Maxx C 2 to 3, Indexer 1 to 2, others 2 to 4, total 9 to 12 with 3 or more types
- Minimum: Ash Blossom 3, Maxx C 2, Indexer 1, total 6 not recommended

- **Main Deck Ratios**

- 40 cards most consistent to 44 cards, maximum 60
- Core archetype: 12 to 18 cards
- Hand traps: 9 to 12 cards
- Generic support: 3 to 6 cards
- Generic removal: 2 to 4 cards

- **Extra Deck Ratios**

- 12 to 15 cards, minimum 12
- Fusion/Synchro/Xyz: 5 to 8 cards
- Link-1/Link-2 boards: 3 to 5 cards
- Link-3 or higher finishers: 2 to 4 cards
- Generic removal: 1 to 2 cards

- **Quality Score Formula**

- Core completeness at 25 percent weight: 5 points for 15 or more core monsters, 3 points for 12 to 14, 1 point for less than 12
- Hand trap coverage at 20 percent weight: 5 points for 9 to 12 with 3 or more types, 3 points for 6 to 8 with 2 types, 1 point for less than 6
- Extra usability at 15 percent weight: 5 points for 12 to 15 all summonable, 3 points for 10 to 11, 1 point for less than 10 or unsummonable
- First turn impedance at 15 percent weight: 5 points for 3 or more negates, 3 points for 2, 1 point for 1 or less
- Compromise ability at 10 percent weight: 5 points for can make 1 negate on Maxx C, 3 points for no negate but stall, 1 point for surrender
- Second turn breakthrough at 10 percent weight: 5 points for 4 or more removal plus hand traps, 3 points for 2 to 3, 1 point for none
- Consensus match at 5 percent weight: 5 points for greater than 70 percent match, 3 points for 50 to 70 percent, 1 point for less than 50 percent
- Total score: 80 or above is master level, 60 to 79 is competitive, 40 to 59 is playable, less than 40 means rebuild

- **Start Rate Thresholds**

- T0 definition: 5 card hand has 2 or more starters, or 1 starter plus 1 hand trap, effective first turn action
- T1 definition: 5 card hand has 1 or more starters, partial first turn action
- T2 definition: 5 card hand has no starters, complete brick
- T0 rate 50 percent or above: excellent
- T1 cumulative rate T0 plus T1 at 80 percent or above: pass
- T1 cumulative 60 to 80 percent: warning, may brick frequently
- T1 cumulative less than 60 percent: fail, severe bricking
- T2 rate greater than 20 percent: warning, more than 1 in 5 chance of complete brick
- Verified with ydkcheck.py section start using 500 samples by default
