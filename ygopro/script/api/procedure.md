# Procedure API Reference

Source: script/procedure.lua (2331 lines). Summoning procedure helpers registered on cards via Auxiliary.Add*Procedure functions.

- **Synchro Summon Procedures**

- Auxiliary.AddSynchroProcedure(c, f1, f2, minc [, maxc]) → void — 1 tuner (f1) + minc to maxc non-tuner (f2); registers EFFECT_SPSUMMON_PROC with SUMMON_TYPE_SYNCHRO; maxc defaults to c:GetLevel()-1
- Auxiliary.AddSynchroProcedure2(c, f1, f2) → void — backwards-compat: calls AddSynchroProcedure with minc=1, maxc=1
- Auxiliary.AddSynchroMixProcedure(c, f1, f2, f3, f4, minc, maxc [, gc]) → void — up to 3 specific named monsters (f1/f2/f3 each take 1) + f4 for 0 to maxc additional; gc optional goal-check callback
- Auxiliary.Tuner(f [, ...]) → function — factory: returns filter checking target:IsTuner(syncard) AND optionally f; used as f1
- Auxiliary.NonTuner(f [, ...]) → function — factory: returns filter checking target:IsNotTuner(syncard) AND optionally f; used as f2

- **Xyz Summon Procedures**

- Auxiliary.AddXyzProcedure(c, f, lv, ct [, alterf, alterdesc, maxct, alterop]) → void — ct monsters of rank lv; alterf/alterdesc/alterop support overlay-from-overlay alternative; registers EFFECT_SPSUMMON_PROC with SUMMON_TYPE_XYZ
- Auxiliary.AddXyzProcedureLevelFree(c, f [, gf, minc, maxc, alterf, alterdesc, alterop]) → void — Xyz with no level restriction; gf optional group-level validation

- **Fusion Summon Procedures**

### Core Mix Procedures

- Auxiliary.AddFusionProcMix(fcard, sub, insf, ...) → void — foundation for all Fusion procedures; each vararg element is specific material (code number), filter function, or table of codes/functions; sub enables substitute; insf enables Instant Fusion; registers EFFECT_FUSION_MATERIAL
- Auxiliary.AddFusionProcMixRep(fcard, sub, insf, fun1, minc, maxc, ...) → void — like Mix but fun1 repeated minc to maxc times

### Convenience Wrappers

- AddFusionProcCode2(c, code1, code2, sub, insf) — 2 specific named materials
- AddFusionProcCode3(c, code1, code2, code3, sub, insf) — 3 specific named materials
- AddFusionProcCode4(c, code1, code2, code3, code4, sub, insf) — 4 specific named materials
- AddFusionProcCodeRep(c, code1, cc, sub, insf) — code1 repeated cc times
- AddFusionProcCodeRep2(c, code1, minc, maxc, sub, insf) — code1 repeated minc to maxc times
- AddFusionProcCodeFun(c, code1, f, cc, sub, insf) — code1 + f repeated cc times
- AddFusionProcFun2(c, f1, f2, insf) — 2 filter-based materials (no substitute)
- AddFusionProcFunRep(c, f, cc, insf) — filter f repeated cc times
- AddFusionProcFunRep2(c, f, minc, maxc, insf) — filter f repeated minc to maxc times
- AddFusionProcFunFun(c, f1, f2, cc, insf) — f1 + f2 repeated cc times
- AddFusionProcFunFunRep(c, f1, f2, minc, maxc, insf) — f1 + f2 repeated minc to maxc times
- AddFusionProcCodeFunRep(c, code1, f, minc, maxc, sub, insf) — code1 + f repeated minc to maxc times
- AddFusionProcCode2FunRep(c, code1, code2, f, minc, maxc, sub, insf) — code1 + code2 + f repeated minc to maxc times

### Specialized Fusion

- Auxiliary.AddFusionProcShaddoll(c, attr) → void — 1 Shaddoll + 1 monster of attribute attr; may use Spellbook field counter as alternative
- Auxiliary.AddFusionEffectProcUltimate(c, params) → Effect — fusion via activated effect; params table controls filter, material location, operations, grave/removed/deck/extra filters
- Auxiliary.AddFusionEffectProc(c, filter, mat_location, mat_filter, mat_operation [, params]) → Effect — simplified wrapper for AddFusionEffectProcUltimate
- Auxiliary.AddContactFusionProcedure(c, filter, self_location, opponent_location, mat_operation, ...) → Effect — Contact Fusion: materials sent to GY via custom operation (not as cost)

- **Ritual Summon Procedures**

- Auxiliary.AddRitualProcUltimate(c, filter, level_function, greater_or_equal [, summon_location, grave_filter, mat_filter, pause, extra_operation, extra_target]) → Effect — base Ritual procedure; greater_or_equal is "Greater" or "Equal"
- Auxiliary.AddRitualProcGreater(c, filter [, ...]) → Effect — materials sum >= original level
- Auxiliary.AddRitualProcEqual(c, filter [, ...]) → Effect — materials sum == original level
- Auxiliary.AddRitualProcGreater2(c, filter [, ...]) → Effect — Greater using current Level (GetLevel)
- Auxiliary.AddRitualProcEqual2(c, filter [, ...]) → Effect — Equal using current Level (GetLevel)
- Code-based variants: AddRitualProcGreaterCode(c, code1, ...) / AddRitualProcEqualCode / AddRitualProcEqual2Code / AddRitualProcEqual2Code2 / AddRitualProcGreater2Code / AddRitualProcGreater2Code2

- **Link Summon Procedures**

- Auxiliary.AddLinkProcedure(c, f, min, max [, gf]) → Effect — min to max monsters matching filter f summing to c's Link Rating; gf optional group validation; registers EFFECT_SPSUMMON_PROC with SUMMON_TYPE_LINK

- **Pendulum Procedures**

- Auxiliary.EnablePendulumAttribute(c [, reg]) → void — enables Pendulum Summon from Pendulum Zone; also registers activate effect from hand (unless reg=false)
- Auxiliary.EnableReviveLimitPendulumSummonable(c, loc) → void — for monsters also pendulum-summonable from special locations

- **Gemini/Dual Procedures**

- Auxiliary.EnableDualAttribute(c) → void — enables Gemini second summon; registers EFFECT_DUAL_SUMMONABLE, EFFECT_ADD_TYPE (TYPE_NORMAL when faceup and not dual), EFFECT_REMOVE_TYPE (TYPE_EFFECT)
- Auxiliary.IsDualState(effect) / IsNotDualState(effect) → boolean — checks dual state
- Auxiliary.DualNormalCondition(effect) → boolean — faceup and not in dual state

- **Summon Condition Limiters**

- Auxiliary.fuslimit / ritlimit / synlimit / xyzlimit / penlimit / linklimit — effect conditions for EFFECT_CANNOT_SPECIAL_SUMMON restricting to specific summon type
- Auxiliary.AssaultModeLimit / MaskChangeLimit / DarkFusionLimit / FossilFusionLimit — archetype-specific summon limits

- **Material Check Helpers**

- Auxiliary.MustMaterialCheck(v, tp, code) → boolean — checks "must use X as material" requirements; code is EFFECT_MUST_BE_FMATERIAL/SMATERIAL/XMATERIAL/LMATERIAL

- **Global Callback Variables**

- Auxiliary.FCheckAdditional / FGoalCheckAdditional — extra check during Fusion material condition/goal
- Auxiliary.RCheckAdditional / RGCheckAdditional — extra check during Ritual material condition/group selection

- **Fusion Material Operation Helpers**

- Auxiliary.FMaterialToGrave — send materials to grave / FMaterialRemove — banish materials / FMaterialToDeck — return to deck
- Auxiliary.ContactFusionSendToDeck (aka Auxiliary.tdcfop) — Contact Fusion: send materials to deck

- **Ritual Check Helpers**

- Auxiliary.RitualCheckGreater / RitualCheckEqual / RitualCheck / RitualCheckAdditionalLevel / RitualCheckAdditional
