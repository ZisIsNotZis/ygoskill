# Group API Reference

Source: ocgcore/scriptlib.h, ocgcore/libgroup.cpp. Groups are sets of cards. Created via Group.CreateGroup() or returned by many Duel.* and card:* functions.

- **Creation and Lifecycle**

- Group.CreateGroup() → Group — new empty group
- Group.FromCards(card1, card2, ...) → Group — nil values skipped (vararg CARDs)
- group:Clone() → Group — shallow copy with same cards
- group:DeleteGroup() → void — marks for GC; only if is_readonly == GTYPE_KEEP_ALIVE
- group:KeepAlive() → void — persists across yields/coroutines
- group:Clear() → void — removes all cards; non-read-only only

- **Mutation**

- group:AddCard(card) / RemoveCard(card) → void — non-read-only only
- group:Remove(filter_func [, exception, ...]) → void — removes matching cards; exception not removed; extra args to filter
- group:Merge(other_group) / Sub(other_group) → void — add/remove all cards from other group; non-read-only only

- **Iteration and Query**

- group:GetFirst() → Card|nil — resets iterator, returns first card; nil if empty
- group:GetNext() → Card|nil — next card; nil at end; errors if GetFirst not called first
- group:GetCount() → integer — also bound to __len metamethod
- group:IsContains(card) → boolean / Equal(other_group) → boolean — same cards same order
- group:SearchCard(filter_func [, ...]) → Card|nothing — first matching card; extra args to filter

- **Filtering**

- group:Filter(filter_func [, exception, ...]) → Group — new group with cards that pass filter; exception excluded
- group:FilterCount(filter_func [, exception, ...]) → integer — count of passing cards
- group:IsExists(filter_func, min_count [, exception, ...]) → boolean — at least min_count cards satisfy filter

- **Selection (Player-Facing, YIELD)**

- group:Select(playerid, min, max [, exception]) → Group|nil — prompts player to select min-max cards; yields; nil if canceled
- group:FilterSelect(playerid, filter_func, min, max [, exception, ...]) → Group — filter first, then select; yields
- group:SelectUnselect(unselect_group [, playerid, finishable, cancelable, min, max]) → Card|nil — select from group or unselect_group; yields
- group:RandomSelect(playerid, count) → Group — random selection; does NOT yield
- group:CancelableSelect(playerid, min, max [, exception]) → Group|nil — like Select but cancelable; yields

- **Sum Operations**

- group:GetSum(filter_func [, ...]) → integer — sums filter return values for all cards
- group:CheckWithSumEqual(filter_func, target_sum, min_count, max_count [, ...]) → boolean — subset sums exactly to target_sum with cardinality min-max
- group:SelectWithSumEqual(playerid, filter_func, target_sum, min_count, max_count [, ...]) → Group — player selects cards summing exactly; yields
- group:CheckWithSumGreater(filter_func, min_sum [, ...]) → boolean — subset sums to at least min_sum
- group:SelectWithSumGreater(playerid, filter_func, min_sum [, ...]) → Group — player selects cards summing at least min_sum; yields

- **Min/Max and Class Count**

- group:GetMinGroup(filter_func [, ...]) → Group, integer — all cards sharing minimum filter value + the value
- group:GetMaxGroup(filter_func [, ...]) → Group, integer — all cards sharing maximum filter value + the value
- group:GetClassCount(filter_func [, ...]) → integer — count of unique filter return values
- group:GetBinClassCount(filter_func [, ...]) → integer — OR all filter values, count 1-bits (population count)

- **Operators (Metamethods)**

- group1 + group2 or group1 | group2 → Group — union
- group1 - group2 → Group — difference
- group1 & group2 → Group — intersection
- group1 ~ group2 → Group — symmetric difference (XOR)
- #group → integer — count, equivalent to group:GetCount()
