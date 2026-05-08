---
name: ygo-deck-build
description: Deck building 5-step workflow with quantitative verification
---
# Deck Building 5-Step Workflow

- **Pre-Build Checklist (Non-Negotiable)**

Before writing any card ID into the YDK file, verify ALL of the following for each card:

- Check lim value using ydkshow.py or sqlite3 -- lim 0 means forbidden (do not include anywhere), lim 1 means maximum 1 copy total (including extra deck), lim 2 means maximum 2 copies total (including extra deck)
- Check card type -- Fusion, Synchro, Xyz, Pendulum, and Link monsters go in extra deck ONLY, never in main deck
- Verify every card ID exists by running ydkshow.py card <id> -- if it returns empty or error the ID is invalid, do not use it
- Check alias field -- if alias is not 0 and differs from ID by 10 or less, the card shares the 3-copy limit with the alias card, count both together
- Count main deck cards as you write -- must reach 40 to 44 before finalizing
- Count extra deck cards -- must be 12 to 15
- Verify no card appears more than 3 times total across main and extra combined (including alias variants)

- **Step 0: Identify Deck Type and Gather References**

Search local YDK files by filename and content, search online for tournament results and meta rankings, classify deck as Control, Combo/Expand, or OTK using criteria in [../deck-research/SKILL.md](../deck-research/SKILL.md). Pass: deck type identified with 3 or more pieces of evidence. Pitfall: single reference may be a minority variant, always verify with multiple references from local and online sources.

- **Step 1: Determine Core**

Query card database by setcode, run ydkshow consensus on local decks if available.

- Verify each card with mean >= 1.0 belongs to target series (non-series high-mean cards are combo partners, not core)
- Check alias: alias != 0 and diff from ID > 10 means same name different effect, evaluate separately
- Confirm at least 1 extra deck summon point exists
- Pass: 4+ distinct series cards with mean >= 2.0 and q90 >= 3, all series cards listed then filtered, 1+ extra deck summon point confirmed
- Pitfall: new card with low mean may be a new engine, not personal preference -- study newest data first
- Pitfall: do not treat combo partners as core

- **Step 2: Build Main Deck 40 to 44 Cards**

Ratio: core archetype 12-18, hand traps 9-12, generic support 3-6, generic removal 2-4.

- Hand trap minimum: Ash Blossom 3 + Maxx C 2 + Indexer 1 = 6 (not recommended), aim for 9-12 with 3+ types
- Check lim column: lim 0 = forbidden, lim 1 = limited to 1, lim 2 = limited to 2
- Validate usability: cost/material requirements satisfiable, no conflicts (Dimension Shifter vs Foolish Burial)
- Same-name limit is 3 copies respecting alias rules
- Pass: main 40-44 cards, same-name at most 3, hand traps at 9+, core at 12+, no cards without strategic justification
- Pitfall: do not skip non-archetype support cards, composite decks may have multiple axes, archetype continuous Spell/Trap must be included even if mean < 1.0 (engine pieces)

- **Step 3: Build Extra Deck 12 to 15 Cards**

Ratio: Fusion/Synchro/Xyz 5-8, Link-1/Link-2 boards 3-5, Link-3+ finishers 2-4, generic removal 1-2.

- Every extra monster must be summonable by main deck -- verify summon conditions for each
- At least 1 Link-1 or Link-2 board required, at least 2 boss monsters required
- Pass: extra 12-15 cards, every monster summonable, at least 1 Link-1/Link-2, at least 2 bosses
- Pitfall: treat extra deck as resources to understand, not slots to fill. Boss monsters with restrictive triggers are not reliable. Reference running < 15 means understand why -- but minimum is 12. Do not add unnecessary cards to fill slots.

- **Step 4: Quantitative Verification**

Run ydkcheck.py with section all. Must pass with 0 errors:

- Basic checks: main 40-60, extra 0-15
- Duplicates: same-name at most 3
- Lflist: all cards respect ban limits
- Start T1 cumulative rate >= 80%
- Quality score >= 60
- Allowed warnings with explanation: types, extra, usability. Fix each error and re-run until clean.
- Pitfall: ydkcheck.py provides rough checking only. Fine checking requires reading card effect text manually. Do not assume card effects work as expected -- read full effect text especially for boss monsters and fusion cards like Simple Fusion (destroys at End Phase).

- **Step 5: Compare with References**

Open 5-10 reference variants from local and online sources, calculate match rate as common unique cards / total unique cards * 100%, 50%+ is acceptable.

- For every difference ask why the reference chose card A and why you chose card B and which is better for current environment
- Reference has but you do not: check ydkshow mean, check online meta carry rate, check effect text for function, decide to add or stay with reason
- You have but reference does not: check ydkshow mean, check online discussion, check effect text for unique function, decide to keep with strategic reason or delete
- Pass: match rate >= 50% with explanations for all differences, or different variant type with justification
- Pitfall: listing differences without analysis is insufficient. Single deck reference has randomness and personal preference -- find consensus. Study decks by year (newest first). Low overlap may indicate different variant, not error -- always check current top cuts.

- **Output Format**

  Deck name: {name}
  Type: {Control/Combo/OTK}
  Main (40-44): {card list}
  Extra (12-15): {card list}
  Hand traps: {count} cards ({types})
  Core series: {count} cards ({series})
  Match rate: {percent}% vs references
  Key differences: {summary}
