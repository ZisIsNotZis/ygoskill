# Duel State API

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
