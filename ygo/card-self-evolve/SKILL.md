---
name: ygo-card-self-evolve
description: Card skill self-evolution based on validation failures and comparison issues
---
# Card Skill Self-Evolution

See [../../meta-self-evolve/adherence.md](../../meta-self-evolve/adherence.md) for strict adherence rules.
- **Loop Template**: See [../../meta-self-evolve/self-evaluate-template.md](../../meta-self-evolve/self-evaluate-template.md) for the shared SMART loop. Override steps 1 and 6 with domain-specific details.

- **SMART Self-Evaluation-Evolve Loop (Non-Negotiable)**

- Step 1: Build/review a card strictly following [build/SKILL.md](../card-build/SKILL.md) workflow
- Step 2: Run mdcheck.py, catalogcheck.py, combocheck.py -- dedicated non-skippable verification, every error must be resolved
- Step 3: Compare with reference cards following [compare/SKILL.md](../card-compare/SKILL.md) -- write down ALL differences unconditionally
- Step 4: For each failure or systematic difference, analyze: which step in the workflow caused it? Is the threshold in the catalog wrong? Were you strictly following the guideline? If yes and result is wrong, how should the guideline change?
- Step 5: Update the root-cause skill file -- [build/SKILL.md](../card-build/SKILL.md), [compare/SKILL.md](../card-compare/SKILL.md), or catalog files
- Step 6: Re-build the card from scratch following the updated workflow, repeat steps 2-5 until all checks pass and comparison match rate is acceptable

- **Triggers**

- mdcheck.py returns errors after strictly following card-build/SKILL.md -- build skill gap
- Validation score below threshold after following card-build/SKILL.md -- catalog or build skill gap
- Comparison match rate below 50 percent -- build skill gap in core identification or card selection
- Card catalog missing a key card -- catalog data gap, update catalog files
- Combo validation fails -- discover or validate skill gap
- Power level calibration wrong -- compare or build skill gap

- **Evolution Actions**

- If build workflow step is ambiguous or missing: add clarification to [build/SKILL.md](../card-build/SKILL.md)
- If catalog entry is missing or wrong: update the appropriate catalog file under [card/catalog/](../catalog/SKILL.md)
- If comparison workflow has gap: update [compare/SKILL.md](../card-compare/SKILL.md)
- If combo validation rules are wrong: update [validate/SKILL.md](../combo/validate/SKILL.md)

- **Verification**

- After updating skill files, verify they are under 200 lines per [markdown-maintenance.md](../../meta-self-evolve/markdown-maintenance.md)
- Verify all updated files are linked from their parent SKILL.md
- Re-run validation scripts on the card that triggered the evolution to confirm the gap is addressed

- **Output Format**

  Action: {update build / update catalog / update compare / update validate}
  File: {path}
  Change: {1-line summary}
  Evidence: {validation result before/after}
