# Duel Damage and Battle API

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
