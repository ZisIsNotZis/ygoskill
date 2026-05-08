---
name: ygo-deck-compare
description: Deck comparison workflow for match rate calculation and difference analysis
---
# Deck Comparison Workflow

- **Pre-Comparison**

Ensure your deck passes ydkcheck.py with section all and 0 errors. Gather 5 to 10 local variants and 3 to 5 online top-cut decklists.

- **Match Rate Calculation**

Unique cards are non-core, non-series cards (support, hand traps, generic). Common unique cards are cards both you and reference have (matched by name, alias variants count as same). Total unique = your unique + reference unique - 2 * common unique. Match rate = common unique / total unique * 100%, 50% or above passes. Less than 50% likely means different variants -- check step 0 type classification matches.

- **Per-Card Difference Analysis**

For cards reference has but you do not: check ydkshow mean (mean >= 1.0 is consensus, skipping needs explanation), check current online meta carry rate, check effect text for function provided, check if your deck has a substitute, decide to add or stay with reason.

For cards you have but reference does not: check ydkshow mean (mean < 0.5 is personal preference, keeping needs justification), check online meta for whether anyone runs this card, check effect text for unique function, decide to keep with strategic reason or delete.

- **Core Engine Comparison**

Compare core series cards by setcode -- they should match between decks. Core difference > 3 cards means likely different variant or core identification error. Check if consensus combo partner (non-series but mean >= 2.0) was missed.

- **Extra Deck Comparison**

Compare card by card: what did reference run, can you summon it, what did you miss. Extra difference > 5 cards means check summon chain completeness. Reference running < 15 means understand why -- but verify minimum 12. Common reasons: variant difference (Synchro vs Link vs Xyz), TCG vs OCB ban list differences, personal preference.

- **Hand Trap Configuration**

Compare types and counts between decks. Hand trap types < 3 is warning (easily tech-'d against). Total hand traps < 9 is warning (insufficient escort and breakthrough).

- **Engine Comparison**

Identify both sides mini-engines from engines.md. For each engine note how many reference ran vs how many you ran and whether complete or partial. Partial engine = 1 or 2 of 2 to 3 cards -- confirm intentional or incomplete. Multi-axis shows as standard deviation >= 1.0 signal (different variants run different engines).

- **Output Format**

  Match rate: {percent}% ({common_unique} common unique / {total_unique} total unique)
  Reference has but you do not:
    - {card_name} (mean: {mean}, q: {q}, carry: {rate}) -> {add/skip}: {reason}
  You have but reference does not:
    - {card_name} (online: {discussion}) -> {keep/delete}: {reason}
  Extra differences: {list} -> {adjust/maintain}
  Final verdict: {pass/needs revision} -- {items}
