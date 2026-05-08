---
name: ygopro-script-self-evolve
description: Script skill self-evolution based on comparison and debugging feedback
---
# Script Skill Evolution

See [../../meta-self-evolve/adherence.md](../../meta-self-evolve/adherence.md) for strict adherence rules.
- **Loop Template**: See [../../meta-self-evolve/self-evaluate-template.md](../../meta-self-evolve/self-evaluate-template.md) for the shared SMART loop. Override steps 1 and 6 with domain-specific details.

- **Goal**

Improve script implementation skills based on feedback from comparison and debugging results. When a skill is strictly followed but produces wrong results, the skill is wrong -- update it immediately.

- **Triggers**

- Script comparison reveals systematic errors in a category (event codes, effect types, helper usage, scoping)
- Comparison reveals a made-up function or constant -- critical failure, the build skill must be updated
- Debugging session reveals an API function or pattern not documented in [api/](../api/SKILL.md)
- User reports a script implementation that does not match real card behavior
- Multi-effect card was implemented as single merged effect -- build skill gap
- Targeting effects missing EFFECT_FLAG_CARD_TARGET or chkc check -- build skill gap

- **Evolution Actions**

- If API documentation gap found: add the missing function or pattern to the appropriate api/ file
- If common mistake pattern found: add it to Common Mistakes in [build/SKILL.md](../script-build/SKILL.md) or Common Discrepancies in [compare/SKILL.md](../script-compare/SKILL.md)
- If procedure helper misunderstanding found: update [api/procedure.md](../api/procedure.md) with clarification
- If constant usage error found: update [api/constants.md](../api/constants.md) or [api/consteffect.md](../api/consteffect.md) with usage notes
- If made-up function/constant found: add explicit prohibition to [build/SKILL.md](../script-build/SKILL.md) Absolute Prohibitions section

- **Verification**

- After updating skill files, verify they are under 200 lines
- Verify all updated files are linked from their parent SKILL.md
- Re-run the comparison that triggered the evolution to confirm the gap is addressed

- **Output Format**

  Action: {update api / update build / update compare / update constants / update procedure}
  File: {path}
  Change: {1-line summary}
  Evidence: {comparison result before/after}
