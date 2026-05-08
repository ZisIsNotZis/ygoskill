---
name: self-evaluate-template
description: Shared self-evaluation loop template for all self-evolve skills
---
# Self-Evaluation-Evolve Loop Template

This template is referenced by all self-evolve skills. Each skill overrides only the triggers and evolution actions.

- **SMART Loop (Non-Negotiable)**

- Step 1: Execute the domain task strictly following the relevant build/research workflow
- Step 2: Run validation scripts -- dedicated non-skippable verification, every error must be resolved
- Step 3: Compare with reference material following the compare workflow -- write down ALL differences unconditionally
- Step 4: For each failure or systematic difference, analyze: which step caused it? Is a threshold wrong? Were you strictly following the guideline? If yes and result is wrong, how should the guideline change?
- Step 5: Update the root-cause skill file -- build, compare, catalog, or other relevant file
- Step 6: Re-execute the task from scratch following the updated workflow, repeat steps 2-5 until all checks pass

- **Output Format**

  Action: {update build / update catalog / update compare / update other}
  File: {path}
  Change: {1-line summary}
  Evidence: {validation result before/after}
