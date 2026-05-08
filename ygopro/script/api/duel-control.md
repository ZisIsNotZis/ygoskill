# Duel Control API

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

- **Must-Select and Adjustment [ACTION]**

- Duel.SetMustSelect(group) → void / GrabMustSelectCard() → void
- Duel.Readjust() → void / AdjustInstantly([card]) → void / AdjustAll() → void
