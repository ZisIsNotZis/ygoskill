# Card Research Workflow

- **When to Use**

User asks what a card does, to find cards matching a description, to list all cards of an archetype, or to find cards with a specific function.

- **Identify Search Type**

- Exact card lookup, user provides card name
- Natural language search, user describes effect in plain language
- Archetype listing, user wants all cards of a series
- Function search, user wants cards with specific effect type like negate or search or special summon

- **Query Card Database**

Use cards.cdb which contains card data in the datas table and card text in the texts table, join on id.

By exact name:
```bash
sqlite3 cards.cdb "SELECT d.id,t.name,d.type,d.level,d.atk,d.def,d.race,d.attribute,d.setcode FROM datas d JOIN texts t ON d.id=t.id WHERE t.name='CardName'"
```

By partial name:
```bash
sqlite3 cards.cdb "SELECT d.id,t.name,d.type FROM datas d JOIN texts t ON d.id=t.id WHERE t.name LIKE '%keyword%'"
```

By setcode, check all 4 fields of the 64-bit setcode integer:
```bash
sqlite3 cards.cdb "SELECT d.id,t.name,d.type FROM datas d JOIN texts t ON d.id=t.id WHERE (d.setcode&0xFFFF=CODE OR (d.setcode>>16)&0xFFFF=CODE OR (d.setcode>>32)&0xFFFF=CODE OR (d.setcode>>48)&0xFFFF=CODE)"
```

By type bitmask, extra deck monsters use type AND 0x4802040 greater than 0, trap cards use type AND 0x4 greater than 0.

- **Quick Card Info via ydkshow**

Use [../../../ygopro/tools/](../../../ygopro/tools/) ydkshow.py which reads cards.cdb and displays full card info including effect text.

```bash
python ../../ygopro/tools/ydkshow.py <card_id>
python ../../ygopro/tools/ydkshow.py <keyword1> <keyword2>
```

Output format includes card name, series, id, alias, lim, date, type, level, attribute, race, ATK/DEF, and effect text.

- **Natural Language to Script Search**

Parse user request into activation location, trigger condition, effect type, target, and restrictions. Map to script search using grep_search against script/c*.lua files with CATEGORY flags like CATEGORY_NEGATE for negate, CATEGORY_TOHAND plus CATEGORY_SEARCH for search, CATEGORY_DESTROY for destroy, CATEGORY_SPECIAL_SUMMON for special summon.

- **Read Card Script**

Card scripts live in /home/z/ygo/script/c<ID>.lua. Read the file to understand the actual implementation beyond the database text. Identify effect types, trigger conditions, costs, targets, resolution, and restrictions like once per turn.

- **Online Research**

If card not in local database or recently printed, search yugioh wiki for card info, search community forums for competitive review, and search ruling databases for clarifications.

- **Output**

Card name, id, type, level or rank, attribute, race, ATK/DEF, archetype, full effect text, key function, strengths and weaknesses, and current meta relevance.
