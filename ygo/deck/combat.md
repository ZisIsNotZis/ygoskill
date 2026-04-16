# Go-First and Go-Second Strategy

- **Turn Definitions**

- T0 means you go first and make an end field on turn 1
- T1 means opponent went first and you break through plus expand on your turn 1
- T2 means opponent already set up end field and you act on turn 2
- T0 optimal means multi-negate end field that opponent struggles to break
- T1 acceptable means break opponent field plus counter-expand
- T2 suboptimal means opponent is prepared and may have hand trap ready

- **Start Rate Requirements**

- T1 cumulative rate T0 plus T1 at 80 percent or above: acceptable baseline, verify with ydkcheck.py section start
- T0 rate at 50 percent or above: competitive standard
- T2 rate less than 20 percent: acceptable ceiling
- Below baseline means deck bricks too often, optimize starter axis

- **Go-First Making End Field**

- Goal: 2 or more negate end field
- Full expand: from 1 to 2 cards make 2 or more negate end field
- Escort expand: set counter trap first then start combo
- Ideal end fields include 3 to 4 negates like Self-Playing with Dingirsu plus S:P plus Spirit Level, 2 negates like Labrynth with Galatea recycle plus Dingirsu, or 2 negates like Albaz with Balerdrake plus Herrsche
- Negate sources come from extra deck negates, field continuous effects, set traps, and reserved hand traps

- **Go-Second Breaking Through**

- Goal: break opponent end field plus counter-expand
- Removal priority: Lightning Storm, Dark Hole, or Feather Duster first, then Pointer cards, then specific denial
- Removal timing: clear own field first if using Lightning Storm, then use removal, save 1 or more hand traps for opponent counter
- Multi-negate field: solve most threatening first which is negate effects, then stall effects, then standing monsters
- Resources needed: removal 2 to 4 cards, hand traps 9 to 12 cards, generic negate 1 to 2 cards

- **Taking Maxx C Compromise**

- Trigger: opponent activates Maxx C, you must resolve under its effect
- Principle: minimize special summon count to reduce opponent draw benefit
- Compromise plays: normal summon core monster to make 1 negate, set counter or trap, use graveyard resources
- Compromise standard: 1 negate or stall plus 1 standing monster
- Do not force full combo because opponent draw benefit may win the game
- Compromise options: normal summon core monster with no special summon, set 1 or 2 counter or traps, use existing graveyard resources for 1 negate, save normal summon for压制 monster

- **Removal Priority Order**

- First priority: negate effects like Divine Warning, S:P, or Dingirsu, solve first
- Second priority: stall effects like Skill Drain or Unicorn, solve second
- Third priority: standing monsters with high ATK or legacy effects, solve last
- After removal: save 1 or more hand traps for opponent counter, do not over-commit

- **Hand Trap Timing**

- Ash Blossom: when opponent activates search/mill/special summon effect, discard from hand to chain
- Maxx C: before opponent expands, set on go-first or activate on go-second
- Indexer: activate before own combo to protect from Ash Blossom, Maxx C, or Imperm
- Infinite Imperm: go-second breakthrough when own field is empty to hand activate, or go-first escort when empty field to set
- Effect Veiler: own main phase from hand send to grave, negate opponent monster effect, own turn only
