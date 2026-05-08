# Card API — Identity and Type

Source: ocgcore/scriptlib.h, ocgcore/libcard.cpp (3671 lines, 233 functions). All functions called on a Card object: card:function_name(...). Parameter types: CARD (0x04), EFFECT (0x10), GROUP (0x08), INT (0x01), BOOLEAN (0x40), FUNCTION (0x20)

- **Code**

- card:GetCode() → integer [, integer] — card code; may return secondary code
- card:GetOriginCode() → integer — original code from card data
- card:GetOriginCodeRule() → integer [, integer] — pendulum rule codes
- card:GetFusionCode() → integer... — current code + EFFECT_ADD_FUSION_CODE codes
- card:GetLinkCode() → integer... — current code + EFFECT_ADD_LINK_CODE codes
- card:IsCode(code1, code2, ...) → boolean — matches any given code (vararg)
- card:IsFusionCode(code1, code2, ...) → boolean — fusion code membership (vararg)
- card:IsLinkCode(code1, code2, ...) → boolean — link code membership (vararg)
- card:IsOriginCodeRule(code1, code2, ...) → boolean — original code rule (vararg)

- **Set**

- card:IsSetCard(setcode1, setcode2, ...) → boolean — current set membership (vararg)
- card:IsOriginSetCard(setcode1, setcode2, ...) → boolean — original set membership (vararg)
- card:IsPreSetCard(setcode1, setcode2, ...) → boolean — previous set membership (vararg)
- card:IsFusionSetCard(setcode1, setcode2, ...) → boolean — fusion set membership (vararg)
- card:IsLinkSetCard(setcode1, setcode2, ...) → boolean — link set membership (vararg)
- card:IsSpecialSummonSetCard(setcode1, setcode2, ...) → boolean — special summon set (vararg)

- **Type**

- card:GetType() → integer — current type with effects applied
- card:GetOriginType() → integer — original type from card data
- card:GetFusionType() / GetSynchroType() / GetXyzType() / GetLinkType() → integer — adjusted types
- card:IsType(type) → boolean — any type bits match (bitwise AND)
- card:IsAllTypes(type) → boolean — ALL type bits match (exact subset)
- card:IsFusionType(type) / IsSynchroType(type) / IsXyzType(type) / IsLinkType(type) → boolean

- **Level/Rank/Link**

- card:GetLevel() / GetRank() / GetLink() → integer — current values
- card:GetSynchroLevel(scard) / GetRitualLevel(scard) → integer — level for summon vs another card (requires CARD)
- card:GetOriginLevel() → integer — original level (0 for XYZ/LINK)
- card:GetOriginRank() → integer — original rank (0 for non-XYZ)
- card:IsXyzLevel(xyzcard, level) → boolean — XYZ level check (requires CARD + INT)
- card:IsLevel(lvl1, lvl2, ...) / IsRank(r1, r2, ...) / IsLink(l1, l2, ...) → boolean — matches any value (vararg)
- card:IsLevelBelow(level) / IsLevelAbove(level) / IsRankBelow / IsRankAbove / IsLinkBelow / IsLinkAbove → boolean
- card:IsHasLevel() → boolean — has valid level
- card:IsHasDefense() → boolean — has defense

- **Scale**

- card:GetLScale() / GetOriginLScale() / GetRScale() / GetOriginRScale() / GetCurrentScale() → integer
