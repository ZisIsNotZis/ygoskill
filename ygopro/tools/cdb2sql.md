# CDB to SQL Converter (cdb2.sql)

- **Purpose**

Convert YGOPro SQLite database (cards.cdb) into human-readable SQL format with named string values instead of raw bitmasks. Creates a temporary table with readable data before converting back to bitmask format.

- **Requirements**

Separate installation at `~/my/ygo/cdb2.sql` (included in local directory). Requires sqlite3.

- **Usage**

```bash
sqlite3 cards.cdb < ~/my/ygo/cdb2.sql
```

- **Output**

Creates two identical tables:
1. Human-readable temporary table with string values
2. Standard datas/texts tables with bitmask values

- **Data Transformation**

- **Type Conversion**: 
  - Raw bitmasks → "怪兽魔法 陷阱 通常 效果 融合..." strings
  - Example: TYPE_EFFECT + TYPE_MONSTER → "怪兽效果"

- **Race Conversion**:
  - Bitmasks → single character codes: "战魔天恶死机水炎..."
  - Example: RACE_WARRIOR + RACE_SPELLCASTER → "战魔"

- **Attribute Conversion**:
  - Bitmasks → single character codes: "地水炎风光暗"
  - Example: ATTR_FIRE + ATTR_WATER → "炎水"

- **Link Arrows**:
  - Appended to "连接" type: "连接↙↓" for bottom-left + bottom arrows

- **Applications**

- Database debugging and verification
- Custom card data creation
- Converting between formats for different tools
- Human-readable database inspection
- Learning bitmask values by seeing converted results
- Preprocessing for ypicgen.sh card image generation

- **Relation to cards.sql**

- cdb2.sql converts existing cdb to readable format
- cards.sql is for creating new DIY data in readable format
- Both use the same string-to-bitmap mapping
- cards.sql is more flexible for adding new cards
- cdb2.sql is for converting existing data
