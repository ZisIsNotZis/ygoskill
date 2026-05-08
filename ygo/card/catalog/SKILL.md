---
name: card-catalogs
description: Card catalog definitions and file structure
---
# Card Catalogs

- **Catalog Definitions**

- **Hand Trap**: a card that activates from HAND during OPPONENT'S TURN to INTERFERE with the opponent, all three conditions must be met, interference includes negate, destroy, banish, stop summons, or apply resource pressure, excludes cards that only self-summon from hand or only search without disrupting the opponent, excludes cards that require a monster on the field to activate from hand as those are field-dependent not pure hand traps
- **Generic Support**: cards for your own resource management including search, mill, draw, or special summon, generic means no specific series restriction or the restriction is wide enough that multiple archetypes can use it, excludes cards that interfere with the opponent, excludes archetype-specific support
- **Generic Trap**: trap cards from the field that interfere with the opponent, excludes counter traps which have their own catalog, excludes cards whose primary function is self-benefit such as recursion or search
- **Counter**: counter traps or quick-play spells that negate or counter opponent actions, counter traps have spell speed 2 and can chain to spell speed 1 or 2 effects, quick-play counters are used on your own turn to protect combos or on opponent's turn to break through
- **NHT**: Non-Handtrap Interference, main deck monsters that interfere from the field, excludes hand traps, excludes extra deck monsters which have their own catalog, excludes pure searchers or extenders with no disruption
- **Generic Extra**: extra deck monsters with non-specific summon conditions that any deck can use, generic means the summon condition only requires broad types like effect monsters, tuners, same-level monsters, or different-named monsters, excludes archetype-specific extra deck monsters

- **Catalog Files**

- **[handtrap.md](handtrap.md)** — Hand trap cards
- **[support.md](support.md)** — Generic support cards
- **[gentrap.md](gentrap.md)** — Generic trap cards
- **[countertrap.md](countertrap.md)** — Counter cards
- **[nht.md](nht.md)** — Non-Handtrap Interference monsters
- **[genericextra.md](genericextra.md)** — Generic extra deck monsters
