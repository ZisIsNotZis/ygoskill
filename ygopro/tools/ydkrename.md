# ydkrename.py

- **Purpose**

Batch rename YDK files based on archetype and date. Generates descriptive filenames like "2024闘獣_1234abcd..." that encode archetype name and release date in alphabetical order.

- **Requirements**

Separate installation at `~/my/ygo/ydkrename.py` (included in local directory). Requires Python with sqlite3.

- **Usage**

```bash
python ~/my/ygo/ydkrename.py <deck.ydk>
```

Processes one YDK file or all files in a directory.

- **Algorithm**

1. Parse YDK to extract all card IDs
2. Look up setcodes and card names for all cards
3. Find the most prominent shared setcode (archetype)
4. Extract release date from card setcode using pack metadata
5. Build filename as: YYYY archetype idhash

Date determination:
- Check `pack/` directory for release dates
- Use the maximum date among all cards in the deck
- Format: YYMM (e.g., 2401 for January 2024)

Archetype determination:
- Gram splitting: For each card, split name by `[- ·/]` and generate all substrings (grams)
- Find the most frequent gram across all cards in the deck
- Require at least CNT occurrences (default 5) to be considered the archetype

- **Examples**

`test.ydk` containing Uria, Lord of Searing Flames cards:
- Input: `test.ydk`
- Output: `2004冥闘獣_...` (2004 year + 冥闘獣 archetype)
- Renamed to: `2004冥闘獾_1234abcd...ydk`

- **Design Notes**

- Uses xxhash64_hexdigest for consistent ID hashing
- Preserves original files by creating hard links
- mkdir_ handles recursive directory creation safely
- Text processing removes special characters and splits text into grams
- Works with multi-language card names
