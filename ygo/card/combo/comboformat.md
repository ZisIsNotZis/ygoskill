# Combo Documentation Format

- **Combo Line Entry**

- Name: descriptive label like "Starter Name plus Extender to End Field"
- Starter: card name and ID, card count needed from hand
- Type: one card combo, two card combo, or full archetype combo
- Steps: ordered sequence, each step has card played, action, resources consumed, resources gained
- End field: list of monsters on field with effects active, negate count, other advantages
- Halt points: list of steps where a hand trap can stop the combo, which hand trap, and what the compromise field becomes
- Source: local reasoning, online guide with URL, or verified by script reading

- **Step Format**

- Step N: Card Name — action description
- Cost: resources paid
- Gain: resources received including searches, summons, mills
- State: hand count, field monsters, grave resources after this step

- **End Field Format**

- Board: Monster Name with effect description, one per line
- Negates: count and type like monster negate, spell negate, trap negate
- Protection: any protection effects active
- Resources: remaining cards in hand, recyclable cards in grave

- **Halt Point Format**

- Step N: hand trap name stops the combo
- If stopped here: compromise field description
- Play around: alternative line if this hand trap is anticipated

- **Example: Light Attribute Dragon Starter**

- Name: Light Dragon plus Wyverbuster to Crystal Wing plus negate board
- Starter: Light Dragon ID 14536032, needs 1 additional card
- Type: two card combo
- Steps:
  - Step 1: Light Dragon — normal summon, trigger effect to special summon Wyverbuster from hand
  - Cost: normal summon
  - Gain: 2 monsters on field
  - State: 4 in hand, 2 on field, 0 in grave
  - Step 2: Wyverbuster — trigger effect to search Dark Dragon
  - Cost: Wyverbuster on field
  - Gain: Dark Dragon added to hand
  - State: 5 in hand, 1 on field, 1 in grave
  - Step 3: Light Dragon and Dark Dragon — synchro summon Crystal Wing
  - Cost: both monsters on field
  - Gain: Crystal Wing Synchro Dragon on field
  - State: 4 in hand, 1 on field, 2 in grave
- End field: Crystal Wing Synchro Dragon with 1 monster negate per turn
- Halt points:
  - Step 1: Ash Blossom on Light Dragon search effect — compromise: pass with 1 monster on field
  - Step 2: Ash Blossom on Wyverbuster search — compromise: Crystal Wing still reachable but no follow-up

- **Combo Tree Visualization**

- Use indentation to show branches
- Starter leads to multiple paths based on extenders available
- Mark optimal path with asterisk
- Mark compromise paths with dash

```
Light Dragon
  + Wyverbuster → Crystal Wing (optimal)
    - Ash on Wyverbuster → 1 negate board (compromise)
  + No extender → pass turn (minimal)
```
