# Debug API Reference

Source: ocgcore/scriptlib.h, ocgcore/libdebug.cpp. Debug functions exposed via Debug.* in Lua for testing, AI development, and field setup.

- **Debug Output**

- Debug.Message(message) → void — prints debug message to duel's string buffer; message converted via tostring
- Debug.ShowHint(message) → void — sends hint message over network buffer via MSG_SHOW_HINT; message truncated to SIZE_HINT_MSG-1
- Debug.SetAIName(name) → void — sends AI name over network buffer via MSG_AI_NAME; name truncated to SIZE_AI_NAME-1

- **Card Creation and Placement**

- Debug.AddCard(code, owner, playerid, location, sequence, position [, proc_complete]) → Card|nil — creates new card and places it at specified location; supports normal placement, P-zone placement, and XYZ overlay attachment; if location is on-field and face-up, enables field effects and adjusts; returns nil if location is not usable and not valid XYZ attach (6 INTs; optional BOOLEAN defaults to false)

- **Player Information**

- Debug.SetPlayerInfo(playerid, lp, startcount, drawcount) → void — sets life points, starting hand count, and draw count; playerid must be 0 or 1 (4 INTs)

- **Pre-Relationship Setup (simulate state without normal mechanics)**

- Debug.PreSummon(card, summon_type [, summon_location]) → void — pre-sets card's summon_info to simulate summon having already occurred; summon location packed into upper 16 bits (CARD, INT; optional INT defaults to 0)
- Debug.PreEquip(equip_card, target) → boolean — establishes equip relationship without normal game mechanics; also links effect target relationships; returns true if equip succeeded, false if conditions not met (equip not in SZONE, target not in MZONE, or target face-down) (2 CARDs)
- Debug.PreSetTarget(t_card, target) → void — directly adds target relationship between two cards via add_card_target; simulates targeting without triggering effects (2 CARDs)
- Debug.PreAddCounter(card, countertype [, count]) → void — directly adds counters to card's counter map without effect resolution (CARD, INT; optional INT defaults to 1)

- **Field Reload (for testing setup)**

- Debug.ReloadFieldBegin(flag [, rule]) → void — clears duel state and begins field reload with specified duel options and rule version; if rule is 0 and flag has DUEL_OBSOLETE_RULING, uses rule 1; otherwise uses CURRENT_RULE; Master Rule 3 expands SZONE to 8 slots (INT; optional INT defaults based on flag)
- Debug.ReloadFieldEnd() → void — finalizes field reload by disabling shuffle checks for hand and deck, then calls reload_field_info to rebuild field state (no params)

- **Typical AI Script Usage Pattern**

- Start with Debug.ReloadFieldBegin(flag) to clear state
- Use Debug.AddCard() calls to set up the field
- Configure player info with Debug.SetPlayerInfo()
- Pre-establish relationships if needed: Debug.PreEquip(), Debug.PreSetTarget(), Debug.PreSummon()
- Finalize with Debug.ReloadFieldEnd()
- Use Debug.Message() for logging decisions
- Use Debug.ShowHint() to display AI reasoning to user
