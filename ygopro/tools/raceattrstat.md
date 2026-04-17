# raceattrstat.py

- **Purpose**

Calculate statistical distribution of Yu-Gi-Oh! card attributes and races from the cards.cdb database. Outputs YAML format for easy parsing and analysis.

- **Requirements**

Separate installation at `~/my/ygo/raceattrstat.py` (included in local directory). Requires Python with yaml module.

- **Usage**

```bash
python ~/my/ygo/raceattrstat.py
```

Queries cards.cdb and outputs YAML with four sections:
1. Race distribution (most to least common)
2. Attribute distribution (most to least common) 
3. Race x attribute matrix (attribute distribution per race)
4. Attribute x race matrix (race distribution per attribute)

- **Output Format**

```yaml
# Race counts sorted by frequency
战士: 1234
魔法使: 567
...

# Attribute counts sorted by frequency
地: 234
水: 456
...

# For each race, attribute percentages sorted by frequency (higher is more common)
战士:
  炎: 45.2%
  光: 30.1%
  ...
  
# For each attribute, race percentages sorted by frequency
地:
  战士: 34.5%
  机械: 28.9%
  ...
```

- **Data Source**

- Queries `datas` table: race, attribute fields (bitmasks)
- Maps bitmasks to readable names using defined arrays
- RACE = '战士 魔法师 天使 恶魔 不死 机械 水 炎 岩石 鸟兽 植物 昆虫 雷 龙 兽 兽战士 恐龙 鱼 海龙 爬虫类 念动力 幻神兽 创造神 幻龙 电子界 幻想魔'
- ATTRIBUTE = '地水炎风光暗神'

- **Applications**

- Meta analysis: Understanding card distribution across attributes/races
- Deck building: Identifying common archetypes by race/attribute
- Balance analysis: Comparing distribution across game eras
- Data validation: Spotting data import errors
- Tournament preparation: Preparing for regional meta trends
