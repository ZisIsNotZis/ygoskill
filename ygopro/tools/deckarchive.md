# Deck Archive (deck.7z)

- **Purpose**

Compressed archive containing Yu-Gi-Oh! deck lists for research purposes. Serves as a dataset for:
- Deck consensus analysis
- Meta tier research
- Archetype identification
- Trend analysis
- Competitive deck reference

- **Contents**

Typical contents include:
- Tournament winning decks
- Regional event decks
- Top meta decks across different formats
- Experimental and rogue decks
- Various archetype variants

- **Usage with Tools**

1. **For ydkshow.py analysis**:
   ```bash
   # Extract archive
   7z x deck.7z -o/decks
   
   # Analyze consensus
   python tools/ydkshow.py /decks/*.ydk
   ```

2. **For ydkcheck.py validation**:
   ```bash
   python tools/ydkcheck.py /decks/your_deck.ydk
   ```

3. **For deck research workflow**:
   - Search by filename patterns to identify archetypes
   - Use consensus data to determine core cards
   - Compare against local builds

- **Integration Skills**

Used primarily in:
- `ygo/deck/research/SKILL.md` — For meta analysis and archetype identification
- `ygo/deck/compare/SKILL.md` — For deck comparison and evaluation
- `ygopro/ranking.md` — For tier list creation and validation

- **Best Practices**

- Regular updates to capture meta shifts
- Organize by year and format for historical analysis
- Include sideboard options where available
- Note source tournament/event for context
- Filter by competitive format (OCG, TCG, Master Duel)
- Include regional variations if available

- **Alternatives**

When deck.7z is not available, use:
- Online deck databases (YGOPRODeck, etc.)
- Tournament result websites
- Community deck sharing platforms
- Local tournament collections
