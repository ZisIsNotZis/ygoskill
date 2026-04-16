# Script Comparison and Debugging

- **Goal**

Compare a script implementation against the real reference script. This is a mandatory, non-skippable step after every implementation. The comparison must be exhaustive and lead to skill updates when systematic issues are found.

- **Comparison Loop (Non-Negotiable)**

- Step 1: Implement the card strictly following [build/SKILL.md](../build/SKILL.md)
- Step 2: Double-check your implementation — this is a dedicated non-skippable step, pay special attention to all caveats
- Step 3: Compare with the real script at script/c<card_id>.lua — write down ALL differences unconditionally, no matter how small
- Step 4: For each difference, analyze: why is it different? Is it functionality, style, or helper usage? Is your way even correct? Why didn't you write like the reference? Were you strictly following the guideline? If yes and your way is problematic, how should the guideline change? If no, why didn't you follow it?
- Step 5: Update [build/SKILL.md](../build/SKILL.md) or other skill markdowns if the comparison revealed a guideline gap
- Step 6: Re-implement the card from scratch, strictly following the (possibly updated) guideline. Repeat steps 2-5 until no differences remain, or remaining differences are acceptable (old/new style equivalent, etc.)
- The final file left must be 100% correct and verifiable. Leave inline comments for every edit made during the loop for audit trail.

- **What to Compare**

- Effect registrations: same EFFECT_TYPE_*, same EVENT_* codes, same SetRange values
- Callback functions: same filter logic, same condition checks, same target selection, same operation logic
- Helper function calls: same aux.* functions, same Duel.* functions, no made-up helpers
- Property flags: EFFECT_FLAG_PLAYER_TARGET, EFFECT_FLAG_CARD_TARGET, EFFECT_FLAG_DELAY, etc.
- Target function structure: `chkc` check present when EFFECT_FLAG_CARD_TARGET is set
- LP cost calculations: half-LP is `Duel.GetLP(tp)//2`, not a fixed number
- Counter trap handling: EFFECT_TYPE_ACTIVATE, not EFFECT_TYPE_QUICK_O
- Multi-effect cards: each distinct use registered as separate effect, not merged
- SetTargetRange values: 0,0 is almost never correct
- Script structure: scoped function names (cXXXXX. or s.), not bare globals

- **Common Discrepancies**

- Event code errors: ING suffix (EVENT_SUMMONING) vs ED suffix (EVENT_SUMMONED) — ING before action completes, ED after
- Missing helpers: aux.NegateSummonCondition, Duel.GetChainMaterial, Duel.SelectFusionMaterial, Duel.NegateActivation
- Missing flags: EFFECT_FLAG_PLAYER_TARGET for player-affecting effects, EFFECT_FLAG_CARD_TARGET for targeting effects
- Fusion complexity: oversimplified fusion missing Chain Material support, CompleteProcedure, BreakEffect
- LP cost: half-LP calculation is Duel.GetLP(tp)//2 not Duel.GetLP(tp)/2 (integer division)
- Case conventions: aux not Aux, cXXXXX.filter/condition/target/activate naming pattern
- Merged effects: multiple distinct activations merged into one effect instead of separate registrations
