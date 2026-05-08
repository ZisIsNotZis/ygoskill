# Card API — Physical Properties

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

- **Position/Location/Sequence**

- card:GetPosition() / GetPreviousPosition() / GetBattlePosition() → integer
- card:GetLocation() / GetPreviousLocation() / GetSequence() / GetPreviousSequence() → integer
- card:IsPosition(pos) / IsPrePosition(pos) / IsControler(player) / IsPreControler(player) / IsOnField() / IsLocation(loc) / IsPreLocation(loc) → boolean
