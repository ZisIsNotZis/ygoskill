# Meta Ranking and Tournament Data

- **Information Sources**

- Web search is the primary method for current meta data, no local database contains tournament results
- Search patterns: `<archetype> top cut decklist YYYY`, `<archetype> tier list meta YYYY`, `<archetype> ocg meta`, `<archetype> tcg meta`
- OCG and TCG have separate meta environments and separate ban lists, always specify which format
- Top-cut decklists from recent tournaments are the most reliable consensus source for card choices
- Community discussions and tier lists reveal meta trends but are less authoritative than tournament results

- **Tier System**

- Tier 1: highest meta share, most represented in top cuts, most consistent results
- Tier 2: competitive and capable of topping but less consistent or less represented
- Tier 3: rogue or niche strategies that can win but are underrepresented
- Meta share percentage: proportion of top-cut placements held by an archetype across recent tournaments
- Tier placement shifts with every new product release and ban list update

- **Using Meta Data in Deck Workflows**

- Research phase: determine current tier placement and meta share before committing to an archetype
- Build phase: cross-verify local consensus data (ydkshow.py) against online top-cut lists, current meta may differ from old local data
- Compare phase: compare your build against 3 to 5 online top-cut decklists for the same archetype
- Meta shifts: hand-trap configurations, extra deck choices, and tech cards all change with the meta, old data can be misleading

- **Key Warnings**

- Online meta is more reliable than old local data for current environment
- Not checking current top cuts before concluding may result in outdated configurations
- Regional differences: OCG and TCG ban lists and meta may differ significantly
- Meta evolves with every product release and ban list update, always verify recency of sources
