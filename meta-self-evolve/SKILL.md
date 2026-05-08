---
name: meta-self-evolve
description: Self-evolution for the entire YGO skill tree
---
# Self-Evolve Skills

- **Purpose**

- This skill ensures the entire skill tree stays organized, consistent, and strictly followed
- It does NOT care about domain knowledge itself -- that is each sub-skill's self-evolve responsibility
- Focus: tree structure, file quality, strict adherence enforcement, gap detection

- **Organizational Self-Evolution Workflow**

- Check the file tree: enumerate all markdowns under ygo-skills/
- Scan file content: verify each file follows markdown-maintenance guidelines, is linked from a parent SKILL.md, is under 200 lines, uses bullet points only
- Find problems: orphaned files, missing links, content violations, structural gaps, missing sub-skills for uncovered workflows
- Fix each problem: update files, create missing sub-skills, reorganize as needed
- Check/scan again: repeat until everything is well-organized and all problems are resolved
- This loop runs automatically whenever self-evolve is invoked, no user intervention needed

- **Sub-Skills**

- **[adherence.md](adherence.md)** -- Strict skill adherence rules (shared by all self-evolve skills)
- **[self-evaluate-template.md](self-evaluate-template.md)** -- Shared SMART loop template for all self-evolve skills (referenced by card-self-evolve, deck-self-evolve, script-self-evolve)
- **[markdown-maintenance.md](markdown-maintenance.md)** -- Guidelines for organizing and maintaining all markdown files
- **[skill-evolution.md](skill-evolution.md)** -- How skills evolve during use and background loops
