---
name: ygo-card-research
description: Card research workflow for querying card database and analyzing card effects
---
# Card Research Workflow

- **When to Use**

User asks what a card does, to find cards matching a description, to list all cards of an archetype, or to find cards with a specific function.

- **Identify Search Type**

- Exact card lookup -- user provides card name
- Natural language search -- user describes effect in plain language
- Archetype listing -- user wants all cards of a series
- Function search -- user wants cards with specific effect type (negate, search, special summon)

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

By type bitmask: extra deck monsters use type AND 0x4802040 > 0, trap cards use type AND 0x4 > 0.

- **Quick Card Info via ydkshow**

Use [../../../ygopro/tools/](../../../ygopro/tools/) ydkshow.py which reads cards.cdb and displays full card info including effect text.

```bash
python ../../ygopro/tools/ydkshow.py <card_id>
python ../../ygopro/tools/ydkshow.py <keyword1> <keyword2>
```

Output includes: card name, series, id, alias, lim, date, type, level, attribute, race, ATK/DEF, effect text.

- **Natural Language to Script Search**

Parse user request into activation location, trigger condition, effect type, target, and restrictions. Map to script search using grep_search against script/c*.lua files with CATEGORY flags (CATEGORY_NEGATE, CATEGORY_TOHAND+CATEGORY_SEARCH, CATEGORY_DESTROY, CATEGORY_SPECIAL_SUMMON).

- **Read Card Script**

Card scripts live in /home/z/ygo/script/c<ID>.lua. Read the file to understand the actual implementation beyond the database text. Identify effect types, trigger conditions, costs, targets, resolution, and restrictions (once per turn).

- **Online Research**

If card not in local database or recently printed: search yugioh wiki for card info, search community forums for competitive review, search ruling databases for clarifications.

- **Output Format**

  Card name: {name}
  ID: {id}
  Type: {Monster/Spell/Trap}
  Level/Rank: {value}
  Attribute/Race: {value}
  ATK/DEF: {value}/{value}
  Archetype: {series}
  Effect: {full effect text}
  Key function: {description}
  Strengths/weaknesses: {list}
  Meta relevance: {current/meta/stale}
