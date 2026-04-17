# cards.sql Template

- **Purpose**

Human-readable SQL format for DIY card data. Replaces raw bitmask values with named strings for readability. Used by expansions/cards.sql for custom card definitions. Newer than cdb2.sql and preferred for new DIY work.

- **Format**

The file is a self-contained SQL script that creates a temporary table with human-readable column values, inserts card data, then converts back to bitmasks and inserts into the real datas and texts tables.

Template structure (**apply on expansions/cards.cdb, not main one!**):
```sql
delete from texts;
delete from datas;
create table _ as select _.column1 id,_.column2 name,_.column3 type,_.column4 level,_.column5 race,_.column6 attribute,_.column7 atk,_.column8 def,_.column9 desc from(values
-- One row per card:
-- (id, 'name', 'type_string', level, 'race_string', 'attribute_string', atk, def, 'effect_text')
(20000,'Card Name','怪兽效果',3,'魔法师','炎',1500,1500,'Effect text here'),
-- More cards...
)_;
insert into datas(id,type,level,race,attribute,atk,def,setcode,ot,alias,category)select id,(type like'%怪兽%')*0x1|(type like'%魔法%')*0x2|(type like'%陷阱%')*0x4|(type like'%通常%')*0x11|(type like'%效果%')*0x21|(type like'%融合%')*0x41|(type like'%仪式%')*0x80|(type like'%灵魂%')*0x221|(type like'%同盟%')*0x421|(type like'%二重%')*0x821|(type like'%调整%')*0x1001|(type like'%同调%')*0x2001|(type like'%速攻%')*0x10002|(type like'%永续%')*0x20000|(type like'%装备%')*0x40002|(type like'%场地%')*0x80002|(type like'%反击%')*0x100004|(type like'%翻转%')*0x200021|(type like'%卡通%')*0x400021|(type like'%超量%')*0x800001|(type like'%灵摆%')*0x1000000|(type like'%特殊%')*0x2000021|(type like'%连接%')*0x4000001,level+(type like'%灵摆%')*0xd0000,(race like'%战%')*0x1|(race like'%魔%')*0x2|(race like'%天%')*0x4|(race like'%恶%')*0x8|(race like'%死%')*0x10|(race like'%机%')*0x20|(race like'%水%')*0x40|(race like'%炎%')*0x80|(race like'%岩%')*0x100|(race like'%鸟%')*0x200|(race like'%植%')*0x400|(race like'%昆%')*0x800|(race like'%雷%')*0x1000|(race like'%龙%')*0x2000|(race like'%兽%')*0x4000|(race like'%士%')*0x8000|(race like'%恐%')*0x10000|(race like'%鱼%')*0x20000|(race like'%海%')*0x40000|(race like'%爬%')*0x80000|(race like'%念%')*0x100000|(race like'%神%')*0x200000|(race like'%创%')*0x400000|(race like'%幻%')*0x800000|(race like'%电%')*0x1000000|(race like'%想%')*0x2000000,(attribute like'%地%')*0x01|(attribute like'%水%')*0x02|(attribute like'%炎%')*0x04|(attribute like'%风%')*0x08|(attribute like'%光%')*0x10|(attribute like'%暗%')*0x20|(attribute like'%神%')*0x40,atk,def|(type like'%↙%')*0x1|(type like'%↓%')*0x2|(type like'%↘%')*0x4|(type like'%←%')*0x8|(type like'%→%')*0x20|(type like'%↖%')*0x40|(type like'%↑%')*0x80|(type like'%↗%')*0x100,(1-(type like'%无%'))*0x1e0,0,0,0 from _;
insert into texts(id,name,desc) select id,name,desc from _;
drop table _;
```

- **Type Strings**

Monster types are concatenated: 怪兽 魔法 陷阱 通常 效果 融合 仪式 灵魂 同盟 二重 调整 同调 速攻 永续 装备 场地 反击 反转 卡通 超量 灵摆 特招 连接. Example: 怪兽效果 for Effect Monster, 怪兽效果融合 for Fusion, 怪兽效果连接↙↓ for Link-2 with bottom-left and bottom arrows.

- **Race Strings**

Single character per race: 战魔天恶死机水炎岩鸟植昆雷龙兽士恐鱼海爬念神创幻电想. Example: 战 for Warrior, 龙 for Dragon.

- **Attribute Strings**

Single character per attribute: 地水炎风光暗神. Example: 炎 for FIRE, 光 for LIGHT.

- **Link Arrows**

Appended to 连接 type: ↙↓↘← →↖↑↗ for the 8 link arrow positions. Example: 连接↙↓ means Link with bottom-left and bottom arrows.

- **Usage**

```bash
sqlite3 cards.cdb < cards.sql
```

This replaces all existing data. To add cards without replacing, remove the delete statements and adjust the insert to use INSERT OR REPLACE.
