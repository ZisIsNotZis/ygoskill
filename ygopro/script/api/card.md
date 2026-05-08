# Card API — Getters and Checks

Source: ocgcore/scriptlib.h, ocgcore/libcard.cpp (3671 lines, 233 functions). All functions called on a Card object: card:function_name(...). Parameter types: CARD (0x04), EFFECT (0x10), GROUP (0x08), INT (0x01), BOOLEAN (0x40), FUNCTION (0x20)

**Split into focused sub-files (read only what you need):**

- **[card-identity.md](card-identity.md)** — Code, set, type, level/rank/link, scale
- **[card-physical.md](card-physical.md)** — Link markers, column, attribute, race, ATK/DEF, position
- **[card-state.md](card-state.md)** — Previous state, owner, reason, summon info, status, battle stats
- **[card-effect.md](card-effect.md)** — Effect management, flag effects, relations, card targets
