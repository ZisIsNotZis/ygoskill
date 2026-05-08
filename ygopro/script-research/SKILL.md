---
name: ygopro-script-research
description: Script research workflow for analyzing existing YGOPro Lua scripts
---
# Script Research Workflow

- **Goal**

Research an existing YGOPro Lua script to understand how a card effect is implemented.

- **Steps**

- Identify the card by ID or name using ydkshow.py or sqlite3 on cards.cdb
- Locate the script file at script/c<card_id>.lua (card_id is 8-digit zero-padded password)
- Read the script file and identify: effect types registered, event codes used, callback functions (condition, cost, target, operation), helper functions from procedure.lua or utility.lua
- Cross-reference API functions against [api/](api/SKILL.md) documentation
- If the script uses unfamiliar constants, look them up in [api/constants.md](api/constants.md) or [api/consteffect.md](api/consteffect.md)
- If the script uses procedure helpers (AddSynchroProcedure, AddFusionProcMix, etc.), look them up in [api/procedure.md](api/procedure.md)
- Summarize: what effects the card has, how each effect works step by step, what API functions and constants are used

- **Key Reference Files**

- script/constant.lua -- all constant definitions
- script/utility.lua -- commonly used helper functions (aux namespace)
- script/procedure.lua -- summoning procedure helpers
- script/c*.lua -- individual card scripts

- **Common Patterns to Look For**

- Card scripts follow the pattern: local card ID variable, initial_effect function, effect registration with SetCode/SetType/SetRange/SetCondition/SetCost/SetTarget/SetOperation
- Filter functions typically named cXXXXX.filter, condition functions cXXXXX.condition, target functions cXXXXX.target, operation functions cXXXXX.activate
- aux namespace (not Auxiliary) is the standard alias for utility functions

- **Output Format**

  Card: {name} (ID: {id})
  Effects:
    - Effect 1: type={EFFECT_TYPE_*}, event={EVENT_*}, callbacks={condition/cost/target/operation}
    - Effect 2: ...
  API functions used: {list}
  Constants used: {list}
  Procedure helpers: {list}
