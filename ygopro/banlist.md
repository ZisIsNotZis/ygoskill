# Ban List (Forbidden and Limited)

- **lflist.conf Format**

Location: project root lflist.conf. First line is a header listing all available ban list names in brackets like [2026.4] [2025.10 TCG]. Each ban list starts with !name on its own line. Under each list there are three sections: #forbidden, #limited, #semi-limited. Each entry is card_id limit --comment where limit is always 0 for forbidden, 1 for limited, 2 for semi-limited. The comment after -- is the Japanese card name.

- **Limit Values**

- 0 = Forbidden: card cannot be included in any deck under this ban list
- 1 = Limited: maximum 1 copy per deck
- 2 = Semi-Limited: maximum 2 copies per deck
- No entry = Unlimited: maximum 3 copies per deck (subject to the same-name rule)

- **OCG vs TCG Ban Lists**

OCG (Official Card Game) lists use format YYYY.M like 2026.4. TCG (Trading Card Game) lists use YYYY.M TCG like 2025.10 TCG. OCG and TCG have different forbidden and limited cards. Always verify which format applies before building or validating a deck.

- **Checking Ban List Compliance**

Using ydkcheck.py:
```bash
python tools/ydkcheck.py deck.ydk section lflist
```

This reads lflist.conf, matches the first listed ban list, and checks every card. For cards with alias set (alternate artwork), the alias is checked instead of the card ID. Output lists all restricted cards in the deck with their limit status and copy count. If lflist.conf is missing the check is skipped with a warning.

Using ydkshow.py:
```bash
python tools/ydkshow.py <card_id_or_keyword>
```

The lim column in output shows the card's current limit status under the active ban list.

- **Manual Query**

```bash
sqlite3 cards.cdb "SELECT d.id, t.name, d.alias FROM datas d JOIN texts t ON d.id=t.id WHERE d.id IN (SELECT id FROM lflist WHERE limit_val < 3)"
```

Note: lflist.conf is a text file not a database table. For manual lookup grep the file:
```bash
grep -A9999 '!2026.4' lflist.conf | grep <card_id>
```
