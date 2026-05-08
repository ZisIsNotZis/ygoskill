---
name: ygo-deck-self-evolve
description: Deck skill self-evolution based on ydkcheck.py failures and comparison issues
---
# Deck Skill Self-Evolve

- See **[meta-self-evolve/adherence.md](../../meta-self-evolve/adherence.md)** for strict adherence rules.
- **Loop Template**: See **[meta-self-evolve/self-evaluate-template.md](../../meta-self-evolve/self-evaluate-template.md)** for the shared SMART loop. Override steps 1 and 6 with domain-specific details.

- **SMART Self-Evaluation-Evolve Loop (Non-Negotiable)**

- Step 1: Build a deck strictly following [build/SKILL.md](../deck-build/SKILL.md) 5-step workflow
- Step 2: Run ydkcheck.py with section all — this is a dedicated non-skippable verification step, every error must be resolved
- Step 3: Compare with reference decks following [compare/SKILL.md](../deck-compare/SKILL.md) — write down ALL differences unconditionally
- Step 4: For each failure or systematic difference, analyze: which step in the workflow caused it? Is the threshold in [metrics.md](../metrics.md) wrong? Is the card data in [catalog/](../../card/catalog/SKILL.md) incomplete? Is the engine info in [engines.md](../engines.md) missing? Were you strictly following the guideline? If yes and result is wrong, how should the guideline change?
- Step 5: Update the root-cause skill file — [build/SKILL.md](../deck-build/SKILL.md), [metrics.md](../metrics.md), [engines.md](../engines.md), [combat.md](../combat.md), [compare/SKILL.md](../deck-compare/SKILL.md), or catalog files
- Step 6: Re-build the deck from scratch following the updated workflow, repeat steps 2-5 until ydkcheck.py passes with 0 errors and match rate is 50 percent or above
- One-time pass means: ydkcheck.py 0 errors on first run after building, and match rate 50 percent or above on first comparison

- **Triggers**

- ydkcheck.py returns errors after strictly following deck-build/SKILL.md — build skill gap
- ydkcheck.py quality score below 60 after following deck-build/SKILL.md — metrics or build skill gap
- Start rate T1 cumulative below 80 percent — build skill gap in starter identification or ratio
- Comparison match rate below 50 percent — build skill gap in core identification or card selection
- Hand trap count below 9 — build skill gap in hand trap configuration step
- Extra deck has unsummonable cards — build skill gap in extra deck verification step
- Card catalog missing a key card — catalog data gap, update catalog files
- Engine not documented in engines.md — engines data gap, add engine entry
- Ban limit violation — build skill gap in lim column checking step
- Alias conflict missed — rules.md or build skill gap in same-name checking

- **Evolution Actions**

- If build workflow step is ambiguous or missing: add clarification or new step to [build/SKILL.md](../deck-build/SKILL.md)
- If metric threshold is wrong: update [metrics.md](../metrics.md) with corrected threshold and evidence
- If engine data is missing: add engine entry to [engines.md](../engines.md) with core cards, function, applications, and constraints
- If catalog card is missing: add to the appropriate catalog file under [card/catalog/](../../card/catalog/SKILL.md)
- If comparison workflow has gap: update [compare/SKILL.md](../deck-compare/SKILL.md)
- If combat strategy is wrong: update [combat.md](../combat.md) with corrected strategy and evidence

- **Verification**

- After updating skill files, verify they are under 200 lines per [self-evolve/markdown-maintenance.md](../../../meta-self-evolve/markdown-maintenance.md)
- Verify all updated files are linked from their parent SKILL.md
- Re-run ydkcheck.py on the deck that triggered the evolution to confirm the gap is addressed
- **Output Format**

  Action: {update build / update compare / update metrics / update engines / update catalog}
  File: {path}
  Change: {1-line summary}
  Evidence: {validation result before/after}
