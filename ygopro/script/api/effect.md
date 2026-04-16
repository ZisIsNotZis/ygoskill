# Effect API Reference

Source: ocgcore/scriptlib.h, ocgcore/libeffect.cpp. Effects created with Effect.CreateEffect(card) and registered with card:RegisterEffect(effect [, forced]) or Duel.RegisterEffect(effect, player)

- **Creation**

- Effect.CreateEffect(handler_card) → Effect — creates new effect owned by handler card; owner player set to current reason_player (requires CARD)
- Effect.GlobalEffect() → Effect — creates global effect with no owner player (set to 0) and owner set to temp_card
- effect:Clone() → Effect — deep copy of this effect
- effect:Reset() → void — removes effect from owner/handler; no-op if owner or handler is null

- **Setters**

- effect:SetDescription(code) → void — description code (usually string ID from strings.conf)
- effect:SetCode(code) → void — effect code value (event or action this effect responds to)
- effect:SetRange(location) → void — location range where effect is active
- effect:SetTargetRange(self_range, opp_range) → void — target range for self and opponent; clears EFFECT_FLAG_ABSOLUTE_TARGET
- effect:SetAbsoluteRange(playerid, self_range, opp_range) → void — target range relative to specific player; if playerid=0 s->self/o->opp, if 1 swapped; sets EFFECT_FLAG_ABSOLUTE_TARGET
- effect:SetCountLimit(count [, code]) → void — per-chain/per-game usage limit; count==0 coerced to 1; code==EFFECT_COUNT_CODE_CHAIN adds SINGLE flag; sets EFFECT_FLAG_COUNT_LIMIT
- effect:SetReset(reset_flag [, reset_count]) → void — reset conditions; if reset_flag has RESET_PHASE but not RESET_SELF_TURN|RESET_OPPO_TURN, both are added; reset_count defaults to 0 then coerced to 1
- effect:SetType(type) → void — auto-configures: ACTIVATE types become FIELD+ACTIVATE with range set; FLIP types set code to EVENT_FLIP and become SINGLE; IGNITION/QUICK types get FIELD added
- effect:SetProperty(flag0 [, flag1]) → void — flag0 preserves INTERNAL_FLAGS; flag1 overwrites flag[1] entirely
- effect:SetLabel(label1, label2, ...) → void — clears existing label and sets to provided integer values (vararg INTs)
- effect:SetLabelObject(obj) → void — associates card/effect/group object with effect's label; nil clears it
- effect:SetCategory(category_bitmask) → void — e.g. CATEGORY_DESTROY, CATEGORY_DAMAGE
- effect:SetHintTiming(self_timing [, opp_timing]) → void — timing hints for activation; param 2 for effect owner, param 3 for opponent (defaults to param 2)
- effect:SetCondition(func) / SetTarget(func) / SetCost(func) / SetOperation(func) → void — callback functions; unrefs previous first; operation nil clears it
- effect:SetValue(func_or_value) → void — FUNCTION (sets EFFECT_FLAG_FUNC_VALUE), boolean, integer, or number
- effect:SetOwnerPlayer([playerid]) → void — 0 or 1; no-op if not 0 or 1
- effect:SetCostCheck(enabled) → void — whether effect cost has been checked/paid

- **Getters**

- effect:GetFieldID() / GetDescription() / GetCode() / GetType() / GetCategory() / GetRange() → integer
- effect:GetProperty() → integer, integer — both flag arrays (flag[0], flag[1]); returns 0,0 if nil
- effect:GetLabel() → integer... — all label integers; returns 1 integer (0) if empty
- effect:GetLabelObject() → Card | Effect | Group | nil — nil if not set or invalid
- effect:GetOwner() → Card / GetHandler() → Card — owning/handling card
- effect:GetOwnerPlayer() / GetHandlerPlayer() → integer — player ID (0 or 1)
- effect:GetCondition() / GetTarget() / GetCost() / GetOperation() → Function | nil
- effect:GetValue() → Function | integer — if EFFECT_FLAG_FUNC_VALUE set returns function, else stored integer
- effect:GetActiveType() / GetActivateLocation() / GetActivateSequence() → integer

- **Checkers**

- effect:IsActiveType(type_mask) / IsHasProperty(flag0 [, flag1]) / IsHasCategory(category_mask) / IsHasType(type_mask) / IsHasRange(range_mask) → boolean
- effect:IsActivatable(playerid [, neglect_loc, neglect_target]) → boolean — can be activated by player; optional params control whether location and target requirements are ignored
- effect:IsActivated() → boolean — type includes any chain-link type (EFFECT_TYPES_CHAIN_LINK)
- effect:IsCostChecked() → boolean — whether cost has been checked/paid
- effect:CheckCountLimit(playerid) → boolean — can still be used (has remaining count)
- effect:UseCountLimit(playerid [, count, oath_only]) → void — decrements usage count; oath_only true only decrements if OATH code; count defaults to 1

- **Effect Types**

- EFFECT_TYPE_TRIGGER_O — optional trigger / EFFECT_TYPE_TRIGGER_F — mandatory trigger
- EFFECT_TYPE_QUICK_O — optional quick effect / EFFECT_TYPE_QUICK_F — mandatory quick effect
- EFFECT_TYPE_ACTIVATE — spell/trap activation / EFFECT_TYPE_FLIP — flip effect / EFFECT_TYPE_IGNITION — ignition (main phase only)
- EFFECT_TYPE_SINGLE — affects self only / EFFECT_TYPE_FIELD — affects field/players / EFFECT_TYPE_EQUIP — equip effect
- EFFECT_TYPE_CONTINUOUS — non-chain continuous / EFFECT_TYPE_XMATERIAL — effect as XYZ material / EFFECT_TYPE_GRANT — grants effects / EFFECT_TYPE_TARGET — continuous targeting

- **Common Effect Properties**

- EFFECT_FLAG_CANNOT_DISABLE — cannot be negated / EFFECT_FLAG_CARD_TARGET — takes card targets / EFFECT_FLAG_PLAYER_TARGET — affects players
- EFFECT_FLAG_DAMAGE_STEP — can activate in damage step / EFFECT_FLAG_DAMAGE_CAL — can activate at damage calculation / EFFECT_FLAG_DELAY — delayed trigger (場合)
- EFFECT_FLAG_SINGLE_RANGE — only affects self / EFFECT_FLAG_UNCOPYABLE — cannot be copied / EFFECT_FLAG_OATH — oath effect
- EFFECT_FLAG_NO_TURN_RESET — once per field not per turn / EFFECT_FLAG_IMMEDIATELY_APPLY — apply immediately on activation / EFFECT_FLAG_CONTINUOUS_TARGET — continuous targeting

- **Callback Signatures**

All callbacks receive: e (effect), tp (controller 0/1), eg (event group), ep (event player), ev (event value), re (reason effect), r (reason flags), rp (reason player)

- Condition: function(e, tp, eg, ep, ev, re, r, rp) → boolean — false means cannot activate
- Cost: function(e, tp, eg, ep, ev, re, r, rp, chk) — chk==0 return boolean if cost can be paid; chk~=0 actually pay cost
- Target: function(e, tp, eg, ep, ev, re, r, rp, chk) — chk==0 set operation info via Duel.SetOperationInfo() and return boolean
- Operation: function(e, tp, eg, ep, ev, re, r, rp) — resolves the effect, no return value
