---
name: ygo-skills
description: Comprehensive Yu-Gi-Oh! and YGOPro expertise. Reorganized skill tree. Read self-evolve/markdown-maintenance.md before editing any markdown.
---

# Yu-Gi-Oh! Skills

- **Skill Tree**

- **[ygo/](ygo/SKILL.md)** — Yu-Gi-Oh! game knowledge, no implementation details
  - **[card/](ygo/card/SKILL.md)** — Card research, design, comparison
    - **[catalog/](ygo/card/catalog/SKILL.md)** — Card catalogs by function
    - **[research/](ygo/card-research/SKILL.md)** — Card research workflow
    - **[build/](ygo/card-build/SKILL.md)** — DIY card design
    - **[compare/](ygo/card-compare/SKILL.md)** — Card comparison
    - **[self-evolve/](ygo/card-self-evolve/SKILL.md)** — Card skill evolution
  - **[deck/](ygo/deck/SKILL.md)** — Deck research, building, comparison
    - **[research/](ygo/deck-research/SKILL.md)** — Deck research workflow
    - **[build/](ygo/deck-build/SKILL.md)** — 5-step deck building
    - **[compare/](ygo/deck-compare/SKILL.md)** — Deck comparison
    - **[self-evolve/](ygo/deck-self-evolve/SKILL.md)** — Deck skill evolution
- **[ygopro/](ygopro/SKILL.md)** — YGOPro implementation knowledge
  - **[script/](ygopro/script/SKILL.md)** — Script research, implementation
    - **[research/](ygopro/script-research/SKILL.md)** — Script research
    - **[build/](ygopro/script-build/SKILL.md)** — Script implementation
    - **[compare/](ygopro/script-compare/SKILL.md)** — Script comparison
    - **[self-evolve/](ygopro/script-self-evolve/SKILL.md)** — Script skill evolution
  - **[tools/](ygopro/tools/)** — Common tool scripts
- **[self-evolve/](meta-self-evolve/SKILL.md)** — Meta skills
  - **[markdown-maintenance.md](self-evolve/markdown-maintenance.md)** — Markdown maintenance guidelines
  - **[skill-evolution.md](self-evolve/skill-evolution.md)** — Skill evolution process
  - **[mdcheck.py](self-evolve/mdcheck.py)** — Markdown validation script
  - **[catalogcheck.py](self-evolve/catalogcheck.py)** — Catalog validation script
  - **[combocheck.py](self-evolve/combocheck.py)** — Combo validation script

- **Strict Skill Adherence (Non-Negotiable)**

- Do EVERYTHING strictly adhering to the relevant skill/workflow, no improvisation, no shortcuts, no "I know better"
- If no skill/workflow exists for what you need, research, plan, and CREATE one first, then follow it
- If you strictly followed a skill/workflow and the result is wrong or the user is unhappy, the skill is wrong, not you — update the root-cause skill immediately
- Never "auto-adapt" or work around a skill without updating the skill itself — fix the skill, not the symptom
- Never do things beyond existing sub-skills without first creating the appropriate sub-skill
- This cycle is fully automatic and unattended: follow skill → if wrong → update skill → re-follow
- Run validation scripts before committing: mdcheck.py, catalogcheck.py, combocheck.py
- All validation scripts must pass with zero errors
- Read [self-evolve/markdown-maintenance.md](self-evolve/markdown-maintenance.md) before editing any markdown
