---
name: combo-validate
description: Combo validation rules and common pitfalls
---
# Combo Validation

- **Per-Step Validation Rules**

  - Verify summon legality: materials on field, correct count, correct attribute/race/type
  - Verify effect activation conditions: timing, cost, once-per-turn, hard once-per-turn
  - Verify card source: deck cards ≠ extra deck cards; grave effects require card in grave first
  - Verify effect resolution order: effects in same chain resolve in reverse order; triggered effects queue
  - Verify phase restrictions: some effects only in Main Phase, opponent's turn, battle phase, etc.
  - Verify resource accounting: each card can only be used once per step; materials leave the field on Link/Fusion/Xyz summon

- **Common Pitfalls**

  - Assuming grave contents that were never sent there
  - Assuming a card is in hand when it's only in deck or grave
  - Assuming Main Phase 2 exists on T1 (no battle phase = no MP2)
  - Assuming a monster was normal summoned (needed for some tribute/eff conditions)
  - Using extra deck monsters as if they exist in main deck
  - Miscalculating Link material values (Link-5 needs 5 link value, not 1 monster)
  - Activating graveyard effects without meeting their specific conditions (e.g., "other" monster in grave)
  - Stopping the combo prematurely when further valid steps exist
  - Skipping effect reads and guessing what a card does
