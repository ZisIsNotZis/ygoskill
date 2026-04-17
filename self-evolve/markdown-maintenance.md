# Markdown Maintenance Guidelines

- **Core Principles**

- All markdowns organize into topics → sub-topics → sub-sub-topics with unlimited nesting, each file focused and clean
- **Always use bullet points whenever possible**, no tables, no checkboxes, no numbered lists, no heading level nesting beyond a single # title
- Every item must be clear, specific, informative, and compact, no item may repeat or conflict with another, every item must be necessary
- **No file shall exceed 200 lines**, non-negotiable, first compact redundant items, then subdivide into more-focused sub-markdowns
- Assume the reader knows nothing about Yu-Gi-Oh! or YGOPro, explain acronyms, provide context, be helpful
- No markdown shall be logically unreachable, every file must be naturally encountered during a workflow, if a file is never reached during any workflow extract its information into the relevant workflow files
- The main SKILL.md at each level contains no domain knowledge, only a brief title and a tree of linked sub-topic markdowns
- Every single markdown file must exist somewhere in the tree rooted at the top-level SKILL.md, no orphaned files, if a file exists but is not linked either absorb it or add it to the tree at the logical position
- Before making edits to any markdown, read this file first, after editing verify the file is under 200 lines, linked from a parent SKILL.md, uses bullet points, has no duplicates, and is clear to a reader without YGO knowledge

- **Automated Validation Requirements**

- Run `python3 self-evolve/mdcheck.py` to validate markdown structure, formatting, and tree connectivity
- Run `python3 self-evolve/catalogcheck.py` to validate catalog entries against cards.cdb database
- Run `python3 self-evolve/combocheck.py` to validate combo steps with material accounting and phase restrictions
- All validation scripts must pass with zero errors before committing changes
- Fix all validation errors before proceeding with any markdown edits

- **Naming Conventions**

- research, build, compare, self-evolve are always folders containing a SKILL.md, not files
- Hyphens shall not appear in any filename except self-evolve
- Use spaces or camelCase for multi-word filenames
