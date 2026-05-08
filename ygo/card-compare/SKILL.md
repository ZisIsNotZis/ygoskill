---
name: ygo-card-compare
description: Card comparison for power level calibration of custom card designs
---
# Card Comparison

Compare a custom card design against existing cards of similar function to calibrate power level.

- **Method**

- Identify the card primary function: negate, search, destroy, special summon, or draw
- Find 3 to 5 existing cards with similar function using script search via grep_search with CATEGORY flags or database query
- For each comparison card note: effect power (what it does, scope, conditions), cost (discard, tribute, LP, once per turn), restrictions (archetype lock, timing, target limitations), stats (level, ATK/DEF, race, attribute)
- Position the designed card relative to comparisons: strictly better (too strong -- add cost/restriction), strictly worse (too weak -- reduce cost/increase power), comparable (balanced -- justified by niche or trade-off)

- **Output Format**

  Designed card: {name}
  Comparison: {card_name} -- {balanced/overpowered/underpowered}
  Verdict: {reason}
