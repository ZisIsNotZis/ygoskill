# Card API — Getters and Checks

Source: ocgcore/scriptlib.h, ocgcore/libcard.cpp (3671 lines, 233 functions). All functions called on a Card object: card:function_name(...). Parameter types: CARD (0x04), EFFECT (0x10), GROUP (0x08), INT (0x01), BOOLEAN (0x40), FUNCTION (0x20)

- **Code**

- card:GetCode() → integer [, integer] — card code; may return secondary code
- card:GetOriginCode() → integer — original code from card data
- card:GetOriginCodeRule() → integer [, integer] — pendulum rule codes
- card:GetFusionCode() → integer... — current code + EFFECT_ADD_FUSION_CODE codes
- card:GetLinkCode() → integer... — current code + EFFECT_ADD_LINK_CODE codes
- card:IsCode(code1, code2, ...) → boolean — matches any given code (vararg)
- card:IsFusionCode(code1, code2, ...) → boolean — fusion code membership (vararg)
- card:IsLinkCode(code1, code2, ...) → boolean — link code membership (vararg)
- card:IsOriginCodeRule(code1, code2, ...) → boolean — original code rule (vararg)

- **Set**

- card:IsSetCard(setcode1, setcode2, ...) → boolean — current set membership (vararg)
- card:IsOriginSetCard(setcode1, setcode2, ...) → boolean — original set membership (vararg)
- card:IsPreSetCard(setcode1, setcode2, ...) → boolean — previous set membership (vararg)
- card:IsFusionSetCard(setcode1, setcode2, ...) → boolean — fusion set membership (vararg)
- card:IsLinkSetCard(setcode1, setcode2, ...) → boolean — link set membership (vararg)
- card:IsSpecialSummonSetCard(setcode1, setcode2, ...) → boolean — special summon set (vararg)

- **Type**

- card:GetType() → integer — current type with effects applied
- card:GetOriginType() → integer — original type from card data
- card:GetFusionType() / GetSynchroType() / GetXyzType() / GetLinkType() → integer — adjusted types
- card:IsType(type) → boolean — any type bits match (bitwise AND)
- card:IsAllTypes(type) → boolean — ALL type bits match (exact subset)
- card:IsFusionType(type) / IsSynchroType(type) / IsXyzType(type) / IsLinkType(type) → boolean

- **Level/Rank/Link**

- card:GetLevel() / GetRank() / GetLink() → integer — current values
- card:GetSynchroLevel(scard) / GetRitualLevel(scard) → integer — level for summon vs another card (requires CARD)
- card:GetOriginLevel() → integer — original level (0 for XYZ/LINK)
- card:GetOriginRank() → integer — original rank (0 for non-XYZ)
- card:IsXyzLevel(xyzcard, level) → boolean — XYZ level check (requires CARD + INT)
- card:IsLevel(lvl1, lvl2, ...) / IsRank(r1, r2, ...) / IsLink(l1, l2, ...) → boolean — matches any value (vararg)
- card:IsLevelBelow(level) / IsLevelAbove(level) / IsRankBelow / IsRankAbove / IsLinkBelow / IsLinkAbove → boolean
- card:IsHasLevel() → boolean — has valid level
- card:IsHasDefense() → boolean — has defense

- **Scale**

- card:GetLScale() / GetOriginLScale() / GetRScale() / GetOriginRScale() / GetCurrentScale() → integer

- **Link Markers and Linked Cards**

- card:IsLinkMarker(direction) → boolean — has link marker direction (requires INT)
- card:GetLinkedGroup() → Group — cards linked by this card
- card:GetLinkedGroupCount() → integer — count of linked cards
- card:GetLinkedZone([controler]) → integer — linked zone bitmask (optional INT controler)
- card:GetMutualLinkedGroup() / GetMutualLinkedGroupCount() / GetMutualLinkedZone([controler]) → Group/integer
- card:IsLinkState() / IsExtraLinkState() → boolean

- **Column**

- card:GetColumnGroup() → Group / GetColumnGroupCount() → integer / GetColumnZone(location [, controler]) → integer / IsAllColumn() → boolean

- **Attribute**

- card:GetAttribute() / GetOriginAttribute() → integer — current/original attribute
- card:GetFusionAttribute([playerid]) / GetLinkAttribute([playerid]) / GetAttributeInGrave([playerid]) → integer — optional INT playerid
- card:IsAttribute(attr) / IsFusionAttribute(attr [, playerid]) / IsLinkAttribute(attr [, playerid]) → boolean — bitwise AND
- card:IsNonAttribute(attr) → boolean — has attribute OTHER than given

- **Race**

- card:GetRace() / GetOriginRace() / GetLinkRace([playerid]) / GetRaceInGrave([playerid]) → integer
- card:IsRace(race) / IsLinkRace(race [, playerid]) → boolean — bitwise AND

- **ATK/DEF**

- card:GetAttack() / GetOriginAttack() / GetTextAttack() / GetDefense() / GetOriginDefense() / GetTextDefense() → integer — negative treated as 0; Text versions from card data
- card:IsAttack(atk1, atk2, ...) / IsDefense(def1, def2, ...) → boolean — matches any value (vararg)
- card:IsAttackBelow(atk) / IsAttackAbove(atk) / IsDefenseBelow(def) / IsDefenseAbove(def) → boolean

- **Previous State (on field)**

- card:GetPreviousCodeOnField() → integer [, integer] / GetPreviousTypeOnField / GetPreviousLevelOnField / GetPreviousRankOnField / GetPreviousAttributeOnField / GetPreviousRaceOnField / GetPreviousAttackOnField / GetPreviousDefenseOnField / GetPreviousOverlayCountOnField → integer

- **Owner/Controller/Reason**

- card:GetOwner() / GetControler() / GetPreviousControler() → integer — player ID (0 or 1)
- card:SetReason(reason) → void — sets current reason (requires INT)
- card:GetReason() → integer / GetReasonCard() → Card / GetReasonPlayer() → integer / GetReasonEffect() → Effect
- card:IsReason(reason) → boolean — checks reason bits (any flag) / IsAllReasons(reason) → boolean — ALL reason flags

- **Position/Location/Sequence**

- card:GetPosition() / GetPreviousPosition() / GetBattlePosition() → integer
- card:GetLocation() / GetPreviousLocation() / GetSequence() / GetPreviousSequence() → integer
- card:IsPosition(pos) / IsPrePosition(pos) / IsControler(player) / IsPreControler(player) / IsOnField() / IsLocation(loc) / IsPreLocation(loc) → boolean

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
