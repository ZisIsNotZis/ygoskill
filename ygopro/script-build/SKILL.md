---
name: ygopro-script-build
description: Script implementation workflow for YGOPro Lua card effects
---
# Script Build Workflow

- **Goal**

Implement a YGOPro Lua script for a card effect from scratch or from a specification. Strictly follow every rule below — no improvisation, no shortcuts, no making up functions or constants.

- **Script Structure (Non-Negotiable)**

- All Lua functions share one global namespace — unscoped function names WILL collide and override each other
- Old style: `function cXXXXX.initial_effect(c)` with callbacks named `cXXXXX.filter`, `cXXXXX.condition`, `cXXXXX.target`, `cXXXXX.activate`
- New style: `local s,id,o=GetID()` then `function s.initial_effect(c)` with callbacks `s.filter`, `s.condition`, `s.target`, `s.activate`
- Always use one of these two styles — NEVER use bare `function initial_effect(c)` or unscoped `function MyCondition(e,tp,eg,ep,ev,re,r,rp)`
- File naming: `c<card_id>.lua` where card_id is the actual 8-digit (or shorter) card password, NOT c1, c2, c3, etc.
- Normal monsters have NO script file at all — do not create one

- **Implementation Steps**

- Read the card text carefully, identify ALL effects, determine effect types and event codes from [api/consteffect.md](../api/consteffect.md)
- For each effect: choose the correct EFFECT_TYPE_* and EVENT_* code, create Effect.CreateEffect(c), set all required properties (Code, Type, Range, Property), then set callbacks (Condition, Cost, Target, Operation)
- For summoning procedures: use the appropriate Auxiliary.Add*Procedure function from [api/procedure.md](../api/procedure.md)
- Register the effect with c:RegisterEffect(e)
- When a card targets other cards: use EFFECT_FLAG_CARD_TARGET in SetProperty, and include `chkc` check in target function: `if chkc then return chkc:IsLocation(...) and chkc:Is...() end`
- For counter traps: use EFFECT_TYPE_ACTIVATE (NOT EFFECT_TYPE_QUICK_O), and use EVENT_FREE_CHAIN or the appropriate event
- For multi-effect cards (like Solemn Judgment): register EACH distinct use as a SEPARATE effect, do NOT merge multiple conditions into one operation
- LP cost "half": use `Duel.CheckLPCost(tp,Duel.GetLP(tp)//2)` and `Duel.PayLPCost(tp,Duel.GetLP(tp)//2)` — integer division, NOT a fixed number
- Test the script by placing it at script/c<card_id>.lua and running a test duel

- **Absolute Prohibitions**

- NEVER make up a function that does not exist in the API docs — if unsure, check [api/](../api/SKILL.md) or search script/utility.lua and script/procedure.lua
- NEVER make up a constant that does not exist in script/constant.lua — check [api/constants.md](../api/constants.md) or [api/consteffect.md](../api/consteffect.md)
- NEVER use mock, stub, placeholder, or ellipsis in implementation — every line must be real, correct, and complete
- NEVER skip an effect because it seems complicated — implement it fully using the real API
- NEVER imagine a helper function exists — all helpers live in aux (script/utility.lua) or script/procedure.lua, verify before using

- **Common Mistakes to Avoid**

- Using EVENT_ATTACK_DECLARE instead of EVENT_ATTACK_ANNOUNCE for attack response effects
- Using wrong effect type for traps: counter traps use EFFECT_TYPE_ACTIVATE, not EFFECT_TYPE_QUICK_O
- Missing EFFECT_FLAG_PLAYER_TARGET when an effect affects a player rather than a card
- Missing EFFECT_FLAG_CARD_TARGET when a card targets other cards
- Missing `chkc` check in target function for targeting effects
- Using NegateActivation vs NegateSummon incorrectly: NegateActivation for chain negation, NegateSummon for summon negation
- Missing CompleteProcedure for special summon monsters, BreakEffect for effect resolution interruption
- Forgetting that LP cost uses Duel.CheckLPCost/Duel.PayLPCost, not direct subtraction
- Using Aux instead of aux (lowercase) for utility namespace
- Merging multiple distinct effects into one effect with combined conditions — register each as separate effect
- SetTargetRange(0,0) is almost never correct — verify the intended target range

- **Script Template (New Style)**

```lua
local s,id,o=GetID()
function s.initial_effect(c)
  -- effect registration here
end
```

- **Script Template (Old Style)**

```lua
local id=XXXXX
local s=_G["c"..id]
if not s then return end
function s.initial_effect(c)
  -- effect registration here
end
```
