---
name: ygo-deck-compare
description: Deck comparison workflow for match rate calculation and difference analysis
---
# Deck Comparison Workflow

- **Pre-Comparison**

Ensure your deck passes ydkcheck.py with section all and 0 errors. Gather 5 to 10 local variants and 3 to 5 online top-cut decklists.

- **Match Rate Calculation**

Unique cards are non-core non-series cards meaning support, hand traps, and generic cards. Common unique cards are cards both you and reference have, matched by name with alias variants counting as the same. Total unique equals your unique plus reference unique minus 2 times common unique. Match rate equals common unique divided by total unique times 100 percent, 50 percent or above passes. Less than 50 percent likely means different variants, check step 0 type classification matches.

- **Per-Card Difference Analysis**

For cards reference has but you do not: check ydkshow mean where mean at 1.0 or above is consensus and skipping needs explanation, check current online meta carry rate, check effect text for function provided, check if your deck has a substitute, decide to add or stay with reason.

For cards you have but reference does not: check ydkshow mean where mean less than 0.5 is personal preference and keeping needs justification, check online meta for whether anyone runs this card, check effect text for unique function, decide to keep with strategic reason or delete.

- **Core Engine Comparison**

Compare core series cards by setcode, they should match between decks. Core difference greater than 3 cards means likely different variant or core identification error. Check if consensus combo partner which is non-series but mean at 2.0 or above was missed.

- **Extra Deck Comparison**

Compare card by card: what did reference run, can you summon it, what did you miss. Extra difference greater than 5 cards means check summon chain completeness. Reference running fewer than 15 means understand why but verify minimum 12. Common reasons for extra differences: variant difference like Synchro versus Link versus Xyz, TCG versus OCG ban list differences, or personal preference.

- **Hand Trap Configuration**

Compare types and counts between decks. Hand trap types fewer than 3 is warning because easily tech-d against. Total hand traps fewer than 9 is warning because insufficient escort and breakthrough.

- **Engine Comparison**

Identify both sides mini-engines from engines.md. For each engine note how many reference ran versus how many you ran and whether complete or partial. Partial engine means 1 or 2 of 2 to 3 cards, confirm intentional or incomplete. Multi-axis shows as standard deviation at 1.0 or above signal where different variants run different engines.

- **Output Format**

Common unique cards with count and match rate percentage. Reference has but you do not with card name, mean, q value, online carry rate, and decision to add or skip with reason. You have but reference does not with card name, online discussion, and decision to keep with reason or delete. Extra differences with list and decision to adjust or maintain. Final verdict: pass or needs revision with listed items.
