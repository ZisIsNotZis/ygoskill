# Card API — State and History

- **Previous State (on field)**

- card:GetPreviousCodeOnField() → integer [, integer] / GetPreviousTypeOnField / GetPreviousLevelOnField / GetPreviousRankOnField / GetPreviousAttributeOnField / GetPreviousRaceOnField / GetPreviousAttackOnField / GetPreviousDefenseOnField / GetPreviousOverlayCountOnField → integer

- **Owner/Controller/Reason**

- card:GetOwner() / GetControler() / GetPreviousControler() → integer — player ID (0 or 1)
- card:SetReason(reason) → void — sets current reason (requires INT)
- card:GetReason() → integer / GetReasonCard() → Card / GetReasonPlayer() → integer / GetReasonEffect() → Effect
- card:IsReason(reason) → boolean — checks reason bits (any flag) / IsAllReasons(reason) → boolean — ALL reason flags

- **Summon Info**

- card:GetSummonType() / GetSummonLocation() / GetSummonPlayer() → integer
- card:GetSpecialSummonInfo(flag1, flag2, ...) → values — spsummon fields by flag constants (vararg)
- card:IsSummonType(type) / IsSummonLocation(loc) / IsSummonPlayer(player) / IsStatus(status) → boolean
- card:SetStatus(status, enable) → void — sets/unsets status flag (requires INT, BOOLEAN)

- **Destination/Turn/Tuner/Effect Property**

- card:GetDestination() → integer — sendto_param.location / GetLeaveFieldDest() → integer — leave field redirect
- card:GetTurnID() / GetFieldID() / GetFieldIDR() → integer — unique IDs
- card:IsNotTuner(scard) / IsTuner(scard) → boolean — tuner check for synchro (requires CARD)
- card:IsOriginalEffectProperty(func) / IsEffectProperty(func) → boolean — effect property check (requires FUNCTION)

- **Status/Dual/Materials/Equipment**

- card:IsDualState() / EnableDualState() / SetTurnCounter(count) / GetTurnCounter() / IsDisabled() / IsExtraDeckMonster() → boolean/void/integer
- card:SetMaterial([group]) → void / GetMaterial() → Group / GetMaterialCount() → integer / GetTunerLimit() → Effect|Function|integer... / GetHandSynchro() → Effect|Function|integer...
- card:GetEquipGroup() → Group / GetEquipCount() → integer / GetEquipTarget() → Card / GetPreEquipTarget() → Card
- card:CheckEquipTarget(target) / CheckUnionTarget(target) → boolean (requires CARD) / GetUnionCount() → integer, integer

- **XYZ/Overlay**

- card:GetOverlayGroup() → Group / GetOverlayCount() → integer / GetOverlayTarget() → Card
- card:CheckRemoveOverlayCard(player, count, reason) → boolean (requires 3 INTs)
- card:RemoveOverlayCard(player, min, max, reason) → integer — removes XYZ materials (requires 4 INTs, YIELDS)

- **Battle Stats**

- card:GetAttackedGroup() → Group / GetAttackedGroupCount() → integer / GetAttackedCount() → integer
- card:GetBattledGroup() → Group / GetBattledGroupCount() → integer / GetAttackAnnouncedCount() → integer
- card:IsDirectAttacked() → boolean / GetBattleTarget() → Card|nil / GetAttackableTarget() → Group, boolean
- card:IsAttackable() → boolean / IsChainAttackable([atk_count, monster_only]) → boolean (optional INT, BOOLEAN)
- card:IsCanBeBattleTarget(attacker) → boolean (requires CARD)
