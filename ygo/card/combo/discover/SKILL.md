---
name: combo-discover
description: Combo discovery workflow with constraint checking and search strategies
---
# Combo Discovery

- **Workflow**

  - Define constraints explicitly before searching (grave state, turn, phase, available resources)
  - Query cards.cdb for all cards matching starter criteria (attribute, race, level)
  - For each candidate card, read its full effect text before using it in any sequence
  - Trace resource flow: where does each card come from (deck/hand/grave/extra) and is that source valid
  - Build sequences step-by-step, validating each step's legality before proceeding
  - Continue until no further valid moves exist, not until an arbitrary step count
  - Rank discovered combos by end-field strength and consistency

- **Constraint Checklist**

  - Graveyard starts empty unless explicitly stated otherwise
  - Turn is unspecified -> assume worst case (T1, no Main Phase 2, no battle phase)
  - Never assume a monster's summon method (normal/special/tuned) unless stated
  - Never assume specific cards in hand or grave -> combos must work with arbitrary cards
  - One-card combos are the baseline, two-card combos are named extensions, never the primary line
  - Trace every summon source: a summon from hand requires the card already in hand, a search that adds to hand still needs a summon effect before the body lands
  - Verify every search target can act this turn: traps cannot activate the turn they are set or searched, so prefer quick-play, continuous, or monster searches mid combo
  - Link-N requires exactly N link value from materials; each monster counts as 1 or its own link rating
  - Extra deck monsters (fusion/synchro/xyz/link) do not exist in main deck
  - Cards with archetype restrictions can only access their own archetype unless stated

- **Search Strategies**

  - Start from material-compatible Link monsters that share the starter's attribute/race
  - Prioritize cards with graveyard effects that self-trigger on send (recursive loops)
  - Prefer sequences that generate additional resources (search, draw, special summon from deck)
  - Look for fusion/ritual/synchro endpoints that maximize board impact per resource spent

- **Output Format**

  Combo name: {descriptive label}
  Starter: {card name} ({id}), {N} additional card(s) needed
  Type: {one-card/two-card/full-archetype}
  Steps:
    - Step {N}: {Card Name} — {action}
      Cost: {resources paid}
      Gain: {resources received}
      State: {hand: N, field: N, grave: N}
  End field: {monsters with effects, negate count, resources}
  Halt points:
    - Step {N}: {hand trap} stops combo -> {compromise field}
  Validation: {pass/fail} — {reason}
