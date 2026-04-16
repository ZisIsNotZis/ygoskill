# YDK File Format and Tools

- **YDK Format**

A YDK file is a plain text deck list with three sections. #main contains main deck card IDs one per line, #extra contains extra deck card IDs one per line, and #side contains side deck card IDs one per line. Each section ends at the next section header or end of file. Card IDs are 8-digit passwords matching the id field in cards.cdb. Comments start with ! or # outside section headers. Blank lines are ignored.

- **ydkshow.py**

Location: [tools/ydkshow.py](tools/ydkshow.py). Reads cards.cdb and displays card info.

Single card lookup:
```bash
python tools/ydkshow.py <card_id>
python tools/ydkshow.py <keyword1> <keyword2>
```

Deck consensus analysis:
```bash
python tools/ydkshow.py <deck_file_pattern>
```

Output includes card name, series, id, alias, lim, date, type, level, attribute, race, ATK/DEF, effect text. For deck consensus: count, mean, q25, q50, q75, q90, std across all matching YDK files.

- **ydkcheck.py**

Location: [tools/ydkcheck.py](tools/ydkcheck.py). Validates a deck list against rules.

```bash
python tools/ydkcheck.py <deck.ydk> section all
python tools/ydkcheck.py <deck.ydk> section start
python tools/ydkcheck.py <deck.ydk> section basic
python tools/ydkcheck.py <deck.ydk> section lflist
```

Sections: basic checks main 40 to 60 and extra 0 to 15, duplicates checks same-name at most 3, lflist checks all cards respect ban limits, start checks T0/T1/T2 rates with 500 samples, quality computes quality score, all runs every section.

- **sqlite3 Direct Queries**

For queries not covered by the tools:
```bash
sqlite3 cards.cdb "SELECT d.id, t.name FROM datas d JOIN texts t ON d.id=t.id WHERE t.name LIKE '%keyword%'"
```
