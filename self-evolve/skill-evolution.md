# Skill Evolution

- **Core Principle: The Skill Is Always the Root Cause**

- If you strictly followed a skill/workflow and the result is wrong or the user is unhappy, the skill is wrong, not you
- Never silently adapt or work around a skill — always update the root-cause skill first
- Never do things beyond existing sub-skills without first creating the appropriate sub-skill
- If no skill exists for a task, research, plan, and create one before proceeding
- This is fully automatic and unattended: follow skill → detect failure → update skill → re-follow

- **Evolution Triggers**

- Skill strictly followed but result is wrong → update the skill immediately
- User asks for something not covered → create the sub-skill by research, then use it
- User reports missing information → add to the appropriate file in the tree
- Markdown maintenance violation detected → fix and update guidelines if needed
- New OCG engine update → update script implementation knowledge
- New set release or ban list change → update affected files
- New tool available → add to tools directory and update references

- **Evolution Process**

- Identify what needs updating and which file is the root cause
- Research the current state using online sources, local data, or official scripts
- Update the file following markdown-maintenance guidelines
- Verify the update is linked from the correct SKILL.md
- Verify file is under 200 lines after update
- If update requires new files, create them at the logical position in the tree
- If a new workflow is needed, create the sub-skill (research/, build/, compare/, self-evolve/) first

- **Sub-Skill Self-Evolution**

- Each domain (card, deck, script) has its own self-evolve/ sub-skill for domain-specific evolution
- Domain self-evolve handles: missing card knowledge, outdated meta data, script API changes, etc.
- Root self-evolve handles: tree structure, file quality, adherence enforcement, organizational gaps
- Domain self-evolve follows the same strict adherence rules: if the domain skill fails, update it

- **Skill Design Principles (SMART)**

- Specific: each skill has a clear, narrow purpose
- Measurable: use tool-based checking whenever possible, pyright for Python, lua checkers for Lua, ydkcheck.py for decks, ydkshow.py for card lookup
- Actionable: skills produce concrete outputs like deck lists, scripts, or analysis reports
- Relevant: skills cover actual use cases, not hypothetical ones
- Time-bounded: skills reference current meta state with dates or version info

- **Tool Preferences**

- Always prefer persistent tools over writing scripts from scratch
- Python: use pyright to check before reporting success
- Lua: use uv or available lua checkers
- Deck validation: always use ydkcheck.py
- Card lookup: always use ydkshow.py or sqlite3 against cards.cdb
