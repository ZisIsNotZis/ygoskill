# ygo-skills

Structured knowledge base for Yu-Gi-Oh! and YGOPro, organized as a skill tree for AI-assisted deck building, card research, combo design, and script implementation.

## Structure

```
ygo-skills/
├── LICENSE
├── README.md
├── SKILL.md
├── meta-self-evolve
│   ├── SKILL.md
│   ├── adherence.md
│   ├── catalogcheck.py
│   ├── combocheck.py
│   ├── markdown-maintenance.md
│   ├── mdcheck.py
│   ├── self-evaluate-template.md
│   └── skill-evolution.md
├── ygo
│   ├── SKILL.md
│   ├── card
│   │   ├── SKILL.md
│   │   ├── catalog
│   │   │   ├── SKILL.md
│   │   │   ├── countertrap.md
│   │   │   ├── genericextra.md
│   │   │   ├── gentrap.md
│   │   │   ├── handtrap.md
│   │   │   ├── nht.md
│   │   │   └── support.md
│   │   ├── combo
│   │   │   ├── SKILL.md
│   │   │   ├── comboformat.md
│   │   │   ├── discover
│   │   │   │   └── SKILL.md
│   │   │   ├── light_demon_demo.py
│   │   │   ├── self_evolve.py
│   │   │   ├── show_example.py
│   │   │   ├── utils.py
│   │   │   └── validate
│   │   │       └── SKILL.md
│   │   └── combo-self-evolve
│   │       └── SKILL.md
│   ├── card-build
│   │   └── SKILL.md
│   ├── card-compare
│   │   └── SKILL.md
│   ├── card-research
│   │   └── SKILL.md
│   ├── card-self-evolve
│   │   └── SKILL.md
│   ├── deck
│   │   ├── SKILL.md
│   │   ├── combat.md
│   │   ├── engines.md
│   │   ├── llm
│   │   │   ├── SKILL.md
│   │   │   ├── bindx5c.py
│   │   │   ├── nn.py
│   │   │   ├── open.py
│   │   │   └── ygonn.py
│   │   ├── metrics.md
│   │   └── rules.md
│   ├── deck-build
│   │   └── SKILL.md
│   ├── deck-compare
│   │   └── SKILL.md
│   ├── deck-research
│   │   └── SKILL.md
│   └── deck-self-evolve
│       └── SKILL.md
└── ygopro
    ├── SKILL.md
    ├── banlist.md
    ├── database.md
    ├── ranking.md
    ├── script
    │   ├── SKILL.md
    │   └── api
    │       ├── SKILL.md
    │       ├── card-effect.md
    │       ├── card-identity.md
    │       ├── card-physical.md
    │       ├── card-state.md
    │       ├── card.md
    │       ├── cardaction.md
    │       ├── constants.md
    │       ├── consteffect.md
    │       ├── debug.md
    │       ├── duel-control.md
    │       ├── duel-damage.md
    │       ├── duel-deck.md
    │       ├── duel-state.md
    │       ├── duel.md
    │       ├── effect.md
    │       ├── group.md
    │       └── procedure.md
    ├── script-build
    │   └── SKILL.md
    ├── script-compare
    │   └── SKILL.md
    ├── script-research
    │   └── SKILL.md
    ├── script-self-evolve
    │   └── SKILL.md
    ├── tools
    │   ├── SKILL.md
    │   ├── autokey
    │   │   ├── folder.json
    │   │   ├── ygo.json
    │   │   ├── ygo.py
    │   │   └── ygold.py
    │   ├── autokey.md
    │   ├── cardssql.md
    │   ├── cdb2sql.md
    │   ├── clipdown.md
    │   ├── clipdown.sh
    │   ├── deck.7z
    │   ├── deckarchive.md
    │   ├── raceattrstat.md
    │   ├── raceattrstat.py
    │   ├── ydkcheck.py
    │   ├── ydkrename.md
    │   ├── ydkrename.py
    │   ├── ydkshow.py
    │   ├── ypicdown.md
    │   ├── ypicdown.sh
    │   ├── ypicgen.md
    │   └── ypicgen.sh
    └── ydk.md
```

## Usage

Read `SKILL.md` and follow the tree. Each sub-skill has its own `SKILL.md` with a focused workflow. The core principle is strict skill adherence: follow the workflow, and if the result is wrong, update the skill.

## Key Workflows

- **Deck Building** — `ygo/deck-build/SKILL.md`: 5-step workflow from research to verification
- **Combo Design** — `ygo/deck/combo/SKILL.md`: 6-step workflow for discovering and validating combos
- **Card Research** — `ygo/card-research/SKILL.md`: Database queries, script reading, online research
- **Script Implementation** — `ygopro/script-build/SKILL.md`: Lua script creation for card effects

## Tools

- `ydkshow.py` — Card lookup and deck consensus analysis
- `ydkcheck.py` — Deck validation with quality scoring
- See `ygopro/tools/SKILL.md` for the full tool catalog

## License

MIT
