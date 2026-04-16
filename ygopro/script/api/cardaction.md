# Card API — Actions, Movement, and Summonability

- **Summonability Checks**

- card:IsDestructable([effect]) → boolean — can be destroyed (optional EFFECT)
- card:IsSummonable() → boolean — can be normal summoned
- card:IsSpecialSummonableCard() / IsFusionSummonableCard([summon_type]) → boolean
- card:IsMSetable(ignore, effect [, minc, zone]) → boolean — M-zone settable (requires BOOLEAN, EFFECT, optional 2 INTs)
- card:IsSSetable([ignore]) → boolean — S-zone settable (optional BOOLEAN)
- card:IsSpecialSummonable([sumtype]) → boolean
- card:IsSynchroSummonable(tuner [, materials, minc, maxc]) → boolean (requires CARD, optional GROUP, 2 INTs)
- card:IsXyzSummonable([materials, minc, maxc]) → boolean (optional GROUP, 2 INTs)
- card:IsLinkSummonable([materials, linkcard, minc, maxc]) → boolean (optional GROUP, CARD, 2 INTs)
- card:IsCanBeSummoned(ignore, effect [, minc, zone]) → boolean (requires BOOLEAN, EFFECT, optional 2 INTs)
- card:IsCanBeSpecialSummoned(effect, sumtype, sumplayer, nocheck, nolimit [, sumpos, toplayer, zone]) → boolean (requires EFFECT + 4 INTs + 2 BOOLEANs, optional 3 INTs)
- card:IsCanBePlacedOnField([toplayer, tolocation]) → boolean (optional 2 INTs)

- **Location Movement Checks**

- card:IsAbleToHand([player]) / IsAbleToGrave() / IsAbleToDeck([player]) / IsAbleToExtra([player]) / IsAbleToRemove([player, pos, reason]) → boolean
- card:IsAbleToHandAsCost() / IsAbleToGraveAsCost() / IsAbleToDeckAsCost() / IsAbleToExtraAsCost() / IsAbleToDeckOrExtraAsCost() / IsAbleToRemoveAsCost([pos]) → boolean
- card:IsReleasable([reason]) / IsReleasableByEffect() / IsDiscardable([reason]) → boolean

- **Position/Controller Change Ability**

- card:IsCanChangePosition() / IsCanTurnSet() / IsAbleToChangeControler() → boolean
- card:IsControlerCanBeChanged([ignore, zone]) → boolean (optional BOOLEAN, INT)

- **Counters**

- card:AddCounter(type, count [, singly]) → boolean (requires 2 INTs, optional BOOLEAN)
- card:RemoveCounter(player, type, count, reason) → boolean (requires 4 INTs, YIELDS)
- card:GetCounter(type) → integer — type=0 returns total (requires INT)
- card:EnableCounterPermit(type [, prange, condition]) → void (requires INT, optional INT, FUNCTION)
- card:SetCounterLimit(type, limit) → void (requires 2 INTs)
- card:IsCanAddCounter(type, count [, singly, location]) → boolean (requires 2 INTs, optional BOOLEAN, INT)
- card:IsCanRemoveCounter(player, type, count, reason) → boolean (requires 4 INTs)
- card:IsCanHaveCounter(type) → boolean (requires INT)

- **Material Checks**

- card:IsCanBeFusionMaterial([fcard, summon_type]) / IsCanBeSynchroMaterial([scard, tuner]) / IsCanBeRitualMaterial([scard]) / IsCanBeXyzMaterial([scard]) / IsCanBeLinkMaterial([scard]) → boolean
- card:CheckFusionMaterial([group, cg, chkf, not_material]) → boolean (optional GROUP, CARD, INT, BOOLEAN)
- card:CheckFusionSubstitute(fcard) → boolean (requires CARD)
- card:IsCanOverlay([player]) → boolean (optional INT)

- **Immunity/Targetability**

- card:IsImmuneToEffect(effect) → boolean (requires EFFECT)
- card:IsCanBeDisabledByEffect(effect [, is_monster_effect]) → boolean (requires EFFECT, optional BOOLEAN)
- card:IsCanBeEffectTarget([effect]) → boolean (optional EFFECT)

- **Misc/Transformation**

- card:AddMonsterAttribute(type [, attribute, race, level, atk, def]) → void — transforms trap into monster (requires INT, optional 5 INTs)
- card:CancelToGrave(cancel) → boolean — cancels/confirms GY destination (requires BOOLEAN)
- card:GetTributeRequirement() → integer, integer — min, max tribute requirements
- card:SetHint(type, value) → void — card hint for client display (requires 2 INTs)
- card:ReverseInDeck() → void / SetUniqueOnField(pos1, pos2, code [, location]) → void / CheckUniqueOnField(player [, location, ignore_card]) → boolean
- card:ResetNegateEffect(code1, code2, ...) → void — resets negate effects (vararg INTs)
- card:AssumeProperty(type, value) → void — assumes property for hidden cards (requires 2 INTs)
- card:SetSPSummonOnce(code) → void — limits special summon to once per code (requires INT)
