# Card Comparison

Compare a custom card design against existing cards of similar function to calibrate power level.

- **Method**

- Identify the card primary function: negate, search, destroy, special summon, or draw
- Find 3 to 5 existing cards with similar function using script search via grep_search with CATEGORY flags or database query
- For each comparison card note effect power describing what it does its scope and conditions, cost describing what you pay like discard tribute life points or once per turn, restrictions like archetype lock timing or target limitations, and stats like level ATK/DEF race or attribute
- Position the designed card relative to comparisons: strictly better means too strong so add cost or restriction, strictly worse means too weak so reduce cost or increase power, comparable means balanced and justified by niche or trade-off

- **Output**

Designed card name versus each comparison card with verdict on whether it is balanced, overpowered, or underpowered based on the comparison of power, cost, and restrictions.
