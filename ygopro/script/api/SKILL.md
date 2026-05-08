---
name: lua-api-reference
description: YGOPro Lua API reference for Card, Effect, Group, Duel, and related objects
---
# Lua API Reference

Source: ocgcore/scriptlib.h, ocgcore/libcard.cpp, ocgcore/libeffect.cpp, ocgcore/libgroup.cpp, ocgcore/libduel.cpp, ocgcore/libdebug.cpp, script/procedure.lua, script/constant.lua

- **[card.md](card.md)** — Card object API (getters, checks, actions)
- **[cardaction.md](cardaction.md)** — Card object API (movement, summon, materials, counters, immunity)
- **[card-identity.md](card-identity.md)** — Code, set, type, level/rank/link, scale
- **[card-physical.md](card-physical.md)** — Link markers, column, attribute, race, ATK/DEF, position
- **[card-state.md](card-state.md)** — Previous state, owner, reason, summon info, status, battle stats
- **[card-effect.md](card-effect.md)** — Effect management, flag effects, relations, card targets
- **[effect.md](effect.md)** — Effect object API (creation, setters, getters, checkers, types, callbacks)
- **[group.md](group.md)** — Group object API (creation, mutation, iteration, filtering, selection, operations)
- **[duel.md](duel.md)** — Duel global API (state, movement, summon, chain, battle, phase, queries, prompts)
- **[duel-state.md](duel-state.md)** — Player state, card movement, summoning
- **[duel-control.md](duel-control.md)** — Control, counters, chain/effects, events, must-select
- **[duel-damage.md](duel-damage.md)** — Damage, battle, phase, prompts, announcements
- **[duel-deck.md](duel-deck.md)** — Deck/hand, field queries, filtering, materials, targets, overlay
- **[debug.md](debug.md)** — Debug API (output, card creation, field setup)
- **[procedure.md](procedure.md)** — Procedure helpers (Synchro, Xyz, Fusion, Ritual, Link, Pendulum, Gemini)
- **[constants.md](constants.md)** — Core constants (locations, positions, types, attributes, races, reasons, summon types, phases)
- **[consteffect.md](consteffect.md)** — Effect-related constants (effect types, flags, codes, events, categories, resets)
