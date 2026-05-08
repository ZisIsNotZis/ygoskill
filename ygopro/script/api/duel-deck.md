# Duel Deck and Materials API

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

- **Player Capability Checks**

- Duel.IsPlayerAffectedByEffect(player, code) → bool
- Duel.IsPlayerCanDraw(player) / IsPlayerCanDiscardDeck(player) / IsPlayerCanDiscardDeckAsCost(player) → bool
- Duel.IsPlayerCanSummon(player) / IsPlayerCanMSet(player) / IsPlayerCanSSet(player) → bool
- Duel.IsPlayerCanSPSummon(player) / IsPlayerCanFlipSummon(player) → bool
