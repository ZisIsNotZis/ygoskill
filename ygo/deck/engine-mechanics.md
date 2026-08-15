---
name: engine-fundamentals
description: How the YGOPro engine actually runs beneath the card text — zones, chains, summon procedures, timings — and what an expert duelist reads from it
---
# How the Engine Runs (Duelist's View)

- **Purpose**

- Bridge between the low-level Lua/script mechanics (see ygopro/script/api/) and real gameplay decisions
- A duelist who knows how the engine represents state can predict zones, chain links, and trigger windows that card text only hints at
- Everything here is cross-architecture: the same patterns repeat across all 100+ archetypes in ygo/decks/

- **The State Is Every Card In Every Zone**

- Every card exists somewhere: deck, hand, field (main monster 5 + spell/trap 5 + field + extra 2), graveyard, and banish (Plus the side/extra deck offline)
- Expert play treats GY and banish as live resources, not discard piles — many engines recur from the grave or banish zone, so removal (D.D. Crow, banishing traps) is asymmetric against those decks
- Knowing WHICH zones a combo needs (a token zone for pendulum, an EMZ for link, a grave for fusion) tells you where to break it

- **The Chain: Spell Speed and Priority**

- Spell speed 1 (Normal Spells/Traps, monster effects) — cannot chain to speed-2+
- Spell speed 2 (Quick-Plays, Traps, quick monster effects) — chains to 1 and 2
- Spell speed 3 (Counter Traps) — only Counter Traps chain to it; the top of interaction
- In the engine "cannot be responded to" (unnegatable/dodge-then-resolve) is a distinct property — decks like Fusion-from-hand or an archetype's anti-chain dodge win by resolving outside the window
- Practical rule: resolve your un-responsable plays first, then force the opponent to commit to the window you control

- **Trigger Windows and Mandatory/Optional Splits**

- The engine fires effects on event codes (destroyed, sent to grave, leaves field, summoned, activation, damage) with conditions (timing, resources, flags)
- Mandatory triggers queue even if bad; optional (if/あなた can) give the player the choice — knowing which is which tells you whether the opponent "must" extend
- "Can't activate during X phase" or "once per turn" checks are engine counters the card text states; decks exploit them by sequencing the once-per-turn in the turn where it matters

- **Summon Procedures Are the Core DSL of the Engine**

- Extra deck monsters enter by procedure: Fusion (materials sent to gy + "Contact" fuses from field only), Synchro (tuner + non-tuner exact/≥ level), Xyz (materials of a rank, stacked on top), Link (materials to a rating, requires EMZ/co-link), Pendulum (scale+scale, up to sum of scales from hand/face-up extra)
- Each procedure has its own "material economy": Fusion asks for specific names/attributes, Synchro asks for a tuner, Xyz asks for a rank pile you can stack, Link asks only for types/ratings
- Recognizing the procedure behind a deck's bosses tells you its real constraint: a Fusion deck is name-locked (can't generic-spam), a Synchro deck needs tuner routes, a Link deck needs zones

- **The Six Engine-Axis Templates (what 100+ decks reduce to)**

- Recur engine: mill/discard→grave→revive/fusion-from-grave (Orcust, Tearlaments, Shaddoll, Purelv) — key: GY recursion means "remove from GY/banish" kills the deck
- Float engine: destroyed→summon a replacement (Yang Zing, Unchained, Mayakashi ladder, Blue-Eyes floaters) — key: once-per-turn destruction limit or banish-replacement outs it
- Search engine: a normal summon/search that chains into the combo (Swordsoul Mo Ye, Rio, Sky Striker Raye, Mathmech) — key: Ashing the search head stops most single-summon lines
- Token/LP engine: spend a resource to gain bodies (Mikanko equips, Sacred Beasts/殉教者, Timelords) — key: deny the resource (LP or font of tokens)
- Lock/stun engine: an unbreakable field/backrow that denies actions (Qliphort floodgate, True Draco monsters, Eldlich traps, Kashtira zone-lock) — key: they win on denial not damage, break the lock piece not the damage
- OTK engine: commit everything early battle for lethal (Tenpai battle-phase, Numeron 4 direct attacks, Mikanko reflect) — key: they are glass cannons, deny the battle phase or the commit

- **The Advantage Clock**

- Expert play tracks the "clock": who is ahead in cards/summons/LP and which axis they win on (board lock, damage, grind)
- Hand traps + fast removal trade one-for-one but stop entire engine turns (a single Ash can cost the opponent their whole starter) — that is why stall/grind decks accumulate advent
- Every extra summon is one more piece the opponent can answer; overcommitting into 增殖的G or a board-wipe is a misexecution the docs flag as common mistakes

- **Reading the Board (5 questions a turn)**

- What zones are populated and which does the opponent still need (EMZ, S/T, a free main zone)?
- What is in their GY/banish that recurs if I pass?
- Which summon procedure are they one card away from?
- What is their "clock" and which of my interactive pieces (hand trap, removal, trap) actually stops their specific line?
- If I cannot break everything, what single piece (the engine head, the recursion, the lock) must die this turn?

- **Why This Matters Across Decks**

- The 100+ deck docs in ygo/decks/ each encode one instance of these templates
- A duelist who learns the templates + advantage clock can pilot an unfamiliar deck competently on first sight and, more importantly, identify and break the opponent's engine geometry on the fly
