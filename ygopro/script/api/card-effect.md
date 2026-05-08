# Card API — Effects and Targets

- **Card Targets**

- card:SetCardTarget(target) → void / GetCardTarget() → Group / GetFirstCardTarget() → Card|nil / GetCardTargetCount() → integer
- card:IsHasCardTarget(target) → boolean / CancelCardTarget(target) → void (requires CARD)
- card:GetOwnerTarget() → Group / GetOwnerTargetCount() → integer

- **Effect Management**

- card:GetActivateEffect() → Effect... — all activatable effects on field
- card:CheckActivateEffect(ignore_con, ignore_cost, copy_info) → Effect + event info (requires 3 BOOLEANs, returns 0-7 values)
- card:RegisterEffect(effect [, forced]) → integer — registers effect; returns effect ID (requires EFFECT, optional BOOLEAN)
- card:IsHasEffect(code [, check_player]) → Effect... — finds effects by code (requires INT, optional INT)
- card:ResetEffect(code, type) → void / GetEffectCount(code) → integer / CopyEffect(code, reset [, count]) → integer / ReplaceEffect(code, reset [, count]) → integer
- card:EnableReviveLimit() → void / CompleteProcedure() → void

- **Flag Effects and Relations**

- card:RegisterFlagEffect(code, reset, flags, count [, label, desc]) → Effect (5 required INTs, 2 optional)
- card:GetFlagEffect(code) → integer / ResetFlagEffect(code) → void / SetFlagEffectLabel(code, label) → boolean / GetFlagEffectLabel(code) → integer...
- card:CreateRelation(target_card, reset) → void / ReleaseRelation(target_card) → void / CreateEffectRelation(effect) → void / ReleaseEffectRelation(effect) → void / ClearEffectRelation() → void
- card:IsRelateToEffect(effect) → boolean / IsRelateToChain([chain_index]) → boolean / IsRelateToCard(target_card) → boolean / IsRelateToBattle() → boolean
