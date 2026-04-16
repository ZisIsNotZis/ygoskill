# Deck Research Workflow

- **When to Use**

Before building or reviewing a deck for a specific archetype.

- **Gather Local References**

Search YDK files by filename using glob with patterns like double-star slash asterisk name asterisk dot ydk, search YDK files by content using grep_search with known core card IDs, run consensus on found decks using ydkshow.py with deck file patterns, parse YDK filenames for information like year strategy environment and variant name because users encode strategy in filenames.

- **Gather Online References**

Search recent tournament results using web search with archetype plus top cut decklist plus year, search meta rankings using web search with archetype plus tier list meta, search community discussions on Reddit, Team APS, and Master Duel Meta, note regional differences between OCG for Japan, TCG for Western regions, and Master Duel for digital because ban lists and metas differ.

- **Classify Deck Type**

From gathered references classify the archetype playstyle as Control with continuous Spell/Trap at 3 or more, Traps at 4 or more, and impedance from field lockdown like Weather, Eldlich, or Diabellstar, as Combo/Expand with archetype monsters at 6 or more, extra monsters at 5 or more, and impedance from extra negates like Orcust or Swordsoul, or as OTK with long search chains of 3 or more, fixed end field, and hand trap escort like Kushaque or Tearlaments.

Pass criteria: deck type identified with 3 or more pieces of evidence.

- **Extract Core Cards**

From ydkshow consensus cards with mean at 2.0 or above and q90 at 3 are core, from online decklists cards appearing in 70 percent or more of lists are core, verify each core card belongs to target series by setcode match, non-series high-consensus cards are combo partners and should be noted separately not treated as core.

- **Analyze Meta Context**

Determine current tier placement, top matchup strengths and weaknesses, recent ban list impact on the archetype, and emerging tech cards or variants in the current environment.

- **Output**

Deck type classification with evidence, N core cards with X from setcode Y, meta position as tier and meta share percentage, list of key variants found, current meta hand trap configuration, and notable tech cards with rationale.
