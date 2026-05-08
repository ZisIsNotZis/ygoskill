---
name: ygo-card-build
description: DIY card design with power calibration and cost-benefit balance
---
# DIY Card Design

- **Power Level Calibration**

Compare designed card to existing cards of similar function and categorize as limited or banned meaning too efficient with no restrictions, competitive staple meaning strong but has costs or restrictions, competitive playable meaning good in specific decks, casual playable meaning niche use with moderate efficiency, or unplayable meaning too slow or costly or narrow.

- **Cost-Benefit Balance**

- Unconditional negate requires discard plus send self to graveyard plus once per turn
- Conditional negate requires specific trigger plus once per turn
- Search any card requires discard plus once per turn
- Search restricted archetype requires no cost or minor cost
- Special summon self requires cost or condition
- Special summon from graveyard requires strong condition plus cost
- Mass destroy requires high cost or specific trigger
- Draw 2 or more requires significant cost or very narrow condition

- **Design Templates**

Hand Trap Negate: Monster Effect Level 3 to 4, ATK/DEF low around 0/1800, effect reads when opponent activates a card or effect meeting condition during Quick Effect send this card from hand to graveyard negate the activation and if you do destroy it, you can only use this effect once per turn, add specific restriction like type or attribute or race or effect category.

Archetype Searcher: Monster or Spell or Trap, effect reads you may condition then add one card with archetype name from deck to hand that meets restrictions, you can only use this effect once per turn, add narrow search target and specific condition.

Extra Deck Boss: Fusion or Synchro or Xyz or Link, material requirements listed, optional quick effect powerful effect once per turn, secondary effect triggered by specific condition once per turn, power level matched to material difficulty.

- **Wording Standards**

- You can means optional effects
- You must means mandatory effects
- Once per turn means hard once per turn globally
- You can only use this effect of Card Name once per turn means per-card once per turn allowing other copies to activate
- If means non-chainable condition
- When means chainable condition
- and if you do means sequential dependency second part only resolves if first completed
- also means simultaneous resolution
- then means sequential resolution

- **Design Workflow**

- Understand request: new support for existing archetype, completely new card, rebalance existing card, or fill a gap
- Research similar cards using script search for CATEGORY flags or database query by setcode
- Design card stats: name, 8-digit password for ID, type, subtype, level or rank, attribute, race, ATK/DEF, link rating and markers if Link, setcode
- Design effects: type, trigger or condition, cost, target, resolution, restriction
- Balance check: find 3 to 5 cards with similar effects, compare costs restrictions and power levels, ensure designed card is not strictly better than existing options
- If implementing as script follow script implementation guide using password as filename c<password>.lua

- **Red Flags**

Overpowered: no once per turn on powerful effects, unconditional negate without significant cost, searches any card without restriction, mass removal without cost or condition, draws cards without cost, special summons with no requirement.

Underpowered: costs exceed effect value, overly narrow conditions that rarely trigger, effects too slow for current meta, restrictions that make card unusable, stats too low for level or rank.
