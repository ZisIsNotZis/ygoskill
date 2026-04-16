# Duel API Reference

Source: ocgcore/scriptlib.h, ocgcore/libduel.cpp. Duel.* is the global game controller. [ACTION] marks functions that yield to the engine.

- **Player and Game State**

- Duel.EnableGlobalFlag(flag) → void — enable global game flag (INT)
- Duel.GetLP(player) / SetLP(player, lp) → int/void — life points (INT player 0/1)
- Duel.IsTurnPlayer(player) → bool / GetTurnPlayer() → int — current turn player
- Duel.GetTurnCount([player]) → int — optional INT for per-player count
- Duel.GetDrawCount(player) → int — draw count for player

- **Card Movement [ACTION]**

- Duel.Destroy(target, reason [, dest, reason_player]) → void — destroy card(s) (CARD or GROUP, INT reason [, INT dest, INT reason_player])
- Duel.Remove(target, position, reason [, reason_player]) → void — banish (CARD/GROUP, INT pos, INT reason [, INT rp])
- Duel.SendtoGrave(target, reason [, reason_player]) → void — send to GY (CARD/GROUP, INT reason [, INT rp])
- Duel.SendtoHand(target, player, reason [, reason_player]) → void — send to hand (CARD/GROUP, INT player, INT reason [, INT rp])
- Duel.SendtoDeck(target, player, seq, reason [, reason_player, send_activating]) → void — send to deck (CARD/GROUP, INT player, INT seq, INT reason [, INT rp, BOOLEAN])
- Duel.SendtoExtra(target, player, reason) → void — send to extra deck (CARD/GROUP, INT player, INT reason)
- Duel.Release(target, reason [, reason_player]) → void — release/tribute (CARD/GROUP, INT reason [, INT rp])
- Duel.MoveToField(target, player, loc, pos, enable) → void — move to field position (CARD, INT player, INT loc, INT pos, BOOLEAN)
- Duel.ReturnToField(target) → void — return card to field (CARD)
- Duel.MoveSequence(loc, seq1, seq2) / SwapSequence(loc1, loc2, seq1, seq2) → void
- Duel.ChangeForm(target, pos) → void — change battle position (CARD/GROUP, INT pos)

- **Summoning [ACTION]**

- Duel.Summon(player, card, ignore_count, peffect [, min_tribute, zone]) → void — normal summon
- Duel.SpecialSummonRule(player, card [, sumtype]) → void — special summon by rule
- Duel.SynchroSummon(player, card [, tuner, mg, minc, maxc]) → void — synchro summon
- Duel.XyzSummon(player, card [, materials, minc, maxc]) → void — xyz summon
- Duel.LinkSummon(player, card [, materials, lcard, minc, maxc]) → void — link summon
- Duel.SpecialSummon(target, sumtype, sumplayer, player, nocheck, nolimit, pos [, zone]) → void — generic special summon (CARD/GROUP)
- Duel.SpecialSummonStep(card, sumtype, sumplayer, player, nocheck, nolimit, pos [, zone]) → bool — step mode
- Duel.SpecialSummonComplete() → void — complete batch
- Duel.SetM(player, card, ignore_count, peffect [, min_tribute, zone]) → void — set monster
- Duel.SetS(target, player [, toplayer, confirm]) → void — set spell/trap
- Duel.CreateToken(player, code) → Card — create token
- Duel.IsSummonCancelable() → bool / CheckSummonCount([card]) → bool / IncreaseSummonCount([card]) → void

- **Equip and Control [ACTION]**

- Duel.Equip(player, equip_card, target [, update_only, step]) → bool / EquipComplete() → void
- Duel.GetControl(target, player [, reset_phase, reset_count, zone]) → void — change control
- Duel.SwapControl(target1, target2 [, reset_phase, reset_count]) → void — swap control

- **Counters**

- Duel.IsCanAddCounter(player [, type, count, card]) → bool / RemoveCounter(reason_player, s, o, type, count, reason) → void
- Duel.IsCanRemoveCounter(player, type, count, reason [, check]) → bool / GetCounter(player, loc, seq, type) → int

- **Chain and Effects [ACTION]**

- Duel.RegisterEffect(effect, player) → void / ActivateEffect(effect) → void
- Duel.SetChainLimit(func) / SetChainLimitP(func) → void — chain limit filter functions
- Duel.GetChainMaterial(player) → Card / GetCurrentChain() → Group / GetReadyChain() → Group
- Duel.GetChainInfo(index, flags) → various — info about a chain link
- Duel.GetChainEvent() → Group / GetFirstTarget() → Card / GetTargetsRelateToChain() → Group
- Duel.BreakEffect() → void — break current effect resolution
- Duel.ChangeEffect(player, value) → void / NegateActivation(ev) → void / NegateEffect(ev) → void
- Duel.NegateRelatedChain(target, code) → void / DisableSummon(sumtype [, card, group, reason_effect, reason_player, sumplayer]) → void

- **Events [ACTION]**

- Duel.CheckEvent(code [, check]) → bool / RaiseEvent(eg, code, re, r, rp, ep, ev) → void
- Duel.RaiseSingleEvent(card, code, re, r, rp, ep, ev) → void / CheckTiming(code) → bool

- **LP and Damage [ACTION]**

- Duel.Win(player, reason) → void / Draw(player, count, reason) → void
- Duel.Damage(player, amount, reason [, is_step]) → void / Recover(player, amount, reason [, is_step]) → void / RDComplete() → void
- Duel.CheckLPCost(player, cost) → bool / PayLPCost(player, cost [, must_pay]) → void
- Duel.CalculateDamage(attack_card, target_card [, new_attack]) → void
- Duel.GetBattleDamage(player) → int / ChangeBattleDamage(value) → void

- **Battle**

- Duel.ChangeAttacker(card [, ignore_count]) → void / ChangeAttackTarget([card]) → bool
- Duel.ChangeTarget(chain_index, card) → void / ChangeTargetPlayer(chain_index, player) → void / ChangeTargetParam(chain_index, param) → void
- Duel.GetAttacker() → Card / GetAttackTarget() → Card / GetBattleMonster(player) → Card
- Duel.DisableAttack() → void / ChainAttack([card]) → void / GetBattledCount(player) → int / IsDamageCalculated() → bool

- **Phase and Environment**

- Duel.IsEnvironment(code) → bool / IsPhase(phase) → bool / IsMainPhase() → bool / IsBattlePhase() → bool
- Duel.GetCurrentPhase() → int / SkipPhase(player, phase, count, reset, reset_count) → void

- **Deck/Hand/Extra [ACTION]**

- Duel.DiscardDeck(player, count [, reason]) → void / DiscardHand(player, filter, min, max, reason [, exception, extraargs...]) → void
- Duel.DisableShuffleCheck([disable]) → void / DisableSelfDestroyCheck([disable]) → void / RevealSelectDeckSequence([reveal]) → void
- Duel.ShuffleDeck(player) / ShuffleExtra(player) / ShuffleHand(player) / ShuffleSetCard(group) → void
- Duel.ConfirmDecktop(player, count) / ConfirmExtratop(player, count) / ConfirmCards(player, group) → void
- Duel.SortDecktop(player, sort_player, count) → void

- **Field Queries**

- Duel.GetLocationCount(player, loc [, uplayer, reason, zone]) → int, int — available locations and bitfield
- Duel.GetMZoneCount(player [, card_or_group, uplayer, reason, zone]) → int, int / GetSZoneCount(...) → int, int
- Duel.GetLocationCountFromEx(player [, uplayer, card_or_group, type]) → int, int
- Duel.GetUsableMZoneCount(player [, uplayer, reason, zone]) → int, int
- Duel.GetLinkedGroup(player) → Group / GetLinkedGroupCount(player) → int / GetLinkedZone(player) → int
- Duel.GetFieldCard(player, loc, seq) → Card / CheckLocation(player, loc, seq) → bool
- Duel.GetFieldGroup(player, loc1, loc2) → Group / GetFieldGroupCount(player, loc1, loc2) → int
- Duel.GetDecktopGroup(player, count) → Group / GetExtratopGroup(player, count) → Group

- **Field Group Queries (filtering)**

- Duel.GetMatchingGroup(filter, player, loc1, loc2, exception [, extraargs...]) → Group
- Duel.GetMatchingCount(filter, player, loc1, loc2, exception [, extraargs...]) → int
- Duel.GetFirstMatchingCard(filter, player, loc1, loc2, exception [, extraargs...]) → Card
- Duel.IsExistingMatchingCard(filter, player, loc1, loc2, count, exception [, extraargs...]) → bool
- Duel.SelectMatchingCards(filter, player, loc1, loc2, min, max, exception [, extraargs...]) → Group [ACTION]

- **Release and Tribute [ACTION]**

- Duel.GetReleaseGroup(player) → Group / GetReleaseGroupCount(player) → int
- Duel.CheckReleaseGroup(player, filter, count [, exception, extraargs...]) → bool
- Duel.SelectReleaseGroup(player, min, max [, exception]) → Group
- Duel.CheckReleaseGroupEx(player, filter, count, s, o [, exception, extraargs...]) → bool
- Duel.SelectReleaseGroupEx(player, filter, min, max, s, o [, exception, extraargs...]) → Group
- Duel.GetTributeGroup(player, filter, min, max, card) → Group / GetTributeCount(player, filter, min, max, card) → int
- Duel.CheckTribute(player, filter, min, max, card) → bool / SelectTribute(player, min, max, card) → Group

- **Target Setting [ACTION]**

- Duel.GetTargetCount(filter, player, loc1, loc2, exception [, extraargs...]) → int
- Duel.IsExistingTarget(filter, player, loc1, loc2, count, exception [, extraargs...]) → bool
- Duel.SelectTarget(player, filter, loc1, loc2, min, max, exception [, extraargs...]) → Group
- Duel.SetTargetCard(card) → void / ClearTargetCard() → void / SetTargetPlayer(player) → void / SetTargetParam(param) → void

- **Material Selection [ACTION]**

- Duel.GetMustMaterial(player, code) → Group / CheckMustMaterial(player, code) → bool
- Duel.SelectFusionMaterial(player, card [, group, min, max]) → Group / SetFusionMaterial(player, card [, group]) → void / GetFusionMaterial(player) → Group
- Duel.SetSynchroMaterial(player, card [, group]) → void / GetSynchroMaterial(player) → Group
- Duel.SelectSynchroMaterial(player, card, filter1, filter2, min, max, smat, mg) → Group / CheckSynchroMaterial(...) → bool
- Duel.SelectTunerMaterial(player, card, tuner, filter1, filter2, min, max, mg) → Group / CheckTunerMaterial(...) → bool
- Duel.GetRitualMaterial(player) → Group / GetRitualMaterialEx(player) → Group / ReleaseRitualMaterial() → void
- Duel.CheckXyzMaterial(player, card, filter, level_reference, min, max, group) → bool / SelectXyzMaterial(...) → Group

- **Overlay [ACTION]**

- Duel.Overlay(card, group) → void / GetOverlayGroup(player, loc1, loc2) → Group / GetOverlayCount(player, loc1, loc2) → int
- Duel.CheckRemoveOverlayCard(player, loc, type, count, reason) → bool / RemoveOverlayCard(reason, player, s, o, min, max) → void

- **Must-Select and Adjustment [ACTION]**

- Duel.SetMustSelect(group) → void / GrabMustSelectCard() → void
- Duel.Readjust() → void / AdjustInstantly([card]) → void / AdjustAll() → void

- **Player Prompts [ACTION]**

- Duel.Hint(hinttype, player, hint) → void / GetLastSelectHint([player]) → int / HintSelection(group) → void
- Duel.SelectEffectYesNo(player, card [, desc]) → bool / SelectYesNo(player, desc) → bool / SelectOption(player, option1, option2, ...) → int
- Duel.SelectSequence(player, loc, seq) → int / SelectPosition(player, card, positions) → int
- Duel.SelectDisableField(player, count, loc1, loc2, filter) → int / SelectField(player, count, flag, filter [, cancelable]) → int

- **Announcements and Random [ACTION]**

- Duel.AnnounceRace(player, count, available) → int / AnnounceAttribute(player, count, available) → int
- Duel.AnnounceLevel(player [, min, max, exclude...]) → int, int / AnnounceCard(player [, filter...]) → int / AnnounceType(player) → int
- Duel.AnnounceNumber(player, number1, number2, ...) → int, int / AnnounceCoin(player) → int
- Duel.TossCoin(player, count) → int... / TossDice(player, count1 [, count2]) → int... / RockPaperScissors([repeat]) → int
- Duel.GetCoinResult() → int / GetDiceResult() → int / SetCoinResult(result) → void / SetDiceResult(result) → void

- **Player Capability Checks**

- Duel.IsPlayerAffectedByEffect(player, code) → bool
- Duel.IsPlayerCanDraw(player) / IsPlayerCanDiscardDeck(player) / IsPlayerCanDiscardDeckAsCost(player) → bool
- Duel.IsPlayerCanSummon(player) / IsPlayerCanMSet(player) / IsPlayerCanSSet(player) → bool
- Duel.IsPlayerCanSPSummon(player) / IsPlayerCanFlipSummon(player) → bool
