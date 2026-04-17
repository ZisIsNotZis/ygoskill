# ygo-skills

Structured knowledge base for Yu-Gi-Oh! and YGOPro, organized as a skill tree for AI-assisted deck building, card research, combo design, and script implementation.

## Structure

```
ygo-skills/
├── SKILL.md                    # Root — skill tree index
├── ygo/                        # Yu-Gi-Oh! game knowledge
│   ├── card/                   # Card research, catalogs, DIY design
│   └── deck/                   # Deck building, combos, engines, metrics
├── ygopro/                     # YGOPro implementation knowledge
│   ├── database.md             # Card database schema and queries
│   ├── ydk.md                  # YDK file format and tools
│   ├── banlist.md              # Ban list structure
│   ├── ranking.md              # Meta tier analysis
│   ├── script/                 # Lua script research and implementation
│   └── tools/                  # Tool scripts documentation
└── self-evolve/                # Meta skills — maintenance and evolution
```

## Usage

Read `SKILL.md` and follow the tree. Each sub-skill has its own `SKILL.md` with a focused workflow. The core principle is strict skill adherence: follow the workflow, and if the result is wrong, update the skill.

## Key Workflows

- **Deck Building** — `ygo/deck/build/SKILL.md`: 5-step workflow from research to verification
- **Combo Design** — `ygo/deck/combo/SKILL.md`: 6-step workflow for discovering and validating combos
- **Card Research** — `ygo/card/research/SKILL.md`: Database queries, script reading, online research
- **Script Implementation** — `ygopro/script/build/SKILL.md`: Lua script creation for card effects

## Tools

- `ydkshow.py` — Card lookup and deck consensus analysis
- `ydkcheck.py` — Deck validation with quality scoring
- See `ygopro/tools/SKILL.md` for the full tool catalog

## License

MIT
