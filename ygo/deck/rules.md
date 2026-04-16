# Deck Construction Rules

- **Deck Sizes**

- Main deck: 40 to 60 cards, 40 is most consistent, 40 to 44 recommended
- Extra deck: 0 to 15 cards, 0 means pure main deck build confirm intentional, 12 to 15 recommended for full resource utilization
- Side deck: 0 to 15 cards, optional used for post-game swapping not checked by ydkcheck.py

- **Card Limits**

- Same name card limited to 3 copies per deck, determined by card name not card ID
- alias equals 0 means normal card count by own ID
- alias not 0 and difference from ID is 10 or less means alt-art or same effect, count as same name
- alias not 0 and difference from ID is greater than 10 means same name different effect, share the 3 copy limit with the alias card

- **Ban List**

- Forbidden means lim equals 0, zero copies allowed
- Limited means lim equals 1, maximum 1 copy
- Semi-limited means lim equals 2, maximum 2 copies
- Unlimited means no entry in lflist.conf, maximum 3 copies default
- Check alias lim first then own ID lim
- Examples: Crystron Halqifibrax is lim 0, Maxx C is lim 1

- **Type Bitmasks**

- TYPE_MONSTER is 0x1, TYPE_SPELL is 0x2, TYPE_TRAP is 0x4
- TYPE_EFFECT is 0x20, TYPE_FLIP is 0x400, TYPE_TUNER is 0x1000
- TYPE_FUSION is 0x40, TYPE_SYNCHRO is 0x2000, TYPE_XYZ is 0x800000, TYPE_LINK is 0x4000000
- Extra deck monster: type bitwise AND 0x4802040 greater than 0

- **Setcode Rules**

- Setcode is a 64-bit integer containing 4 fields of 16 bits each
- Extract each field: shift setcode right by N times 16 bits then bitwise AND 0xFFFF for N equals 0, 1, 2, or 3
- A card belongs to a series if any of the 4 fields match the target code
- A card can belong to multiple series simultaneously
- Common series: Labrynth equals 1154, Swordsoul equals 1254, Self-Playing equals 1168, Albaz equals 1234, Tearlaments equals 1232
