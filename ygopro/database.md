# Card Database

- **Table Structure**

The cards.cdb file is a SQLite database with two tables. The datas table contains id which is the card password, alias for alt-art handling, setcode for archetype affiliation, type bitmask, level for monsters, race bitmask, attribute bitmask, ATK for monsters, and DEF for monsters. The texts table contains id linking to datas and name for card name and desc for raw effect text.

- **Type Bitmasks**

TYPE_MONSTER is 0x1, TYPE_SPELL is 0x2, TYPE_TRAP is 0x4, TYPE_EFFECT is 0x20, TYPE_FLIP is 0x400, TYPE_TUNER is 0x1000, TYPE_FUSION is 0x40, TYPE_SYNCHRO is 0x2000, TYPE_XYZ is 0x800000, TYPE_LINK is 0x4000000. Extra deck monster check: type bitwise AND 0x4802040 greater than 0.

- **Setcode**

64-bit integer with 4 fields of 16 bits each. Extract: shift right by N times 16 then AND 0xFFFF for N equals 0, 1, 2, 3. Common: Labrynth 1154, Swordsoul 1254, Self-Playing 1168, Albaz 1234, Tearlaments 1232. Card belongs to series if any field matches. Card can belong to multiple series.

- **Common Queries**

By name: SELECT d.id, t.name, d.type, d.level, d.atk, d.def, d.race, d.attribute, d.setcode FROM datas d JOIN texts t ON d.id=t.id WHERE t.name equals CardName.

By setcode checking all 4 fields: SELECT d.id, t.name, d.type FROM datas d JOIN texts t ON d.id=t.id WHERE any of the 4 shifted fields equals the target code.

Extra deck monsters: SELECT d.id, t.name FROM datas d JOIN texts t ON d.id=t.id WHERE d.type AND 0x4802040 greater than 0.

Monsters of specific race: SELECT d.id, t.name FROM datas d JOIN texts t ON d.id=t.id WHERE d.race AND race_bitmask greater than 0.

Card password equals id, used as filename for scripts: c<ID>.lua.
