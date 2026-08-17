---
name: playtest-evolution
description: Evolve deck experience by having agent-driven ygopromcp clients duel each other
---
# Play-Test Driven Deck Evolution

- **Purpose**

- Turn raw deck lists into verified deck experience files under ygo/decks
- Discover real combo lines, choke points, halt points, and matchup mistakes by playing games instead of reading lists
- Iterate quickly with an agent driving one deck and a subagent driving the other

- **Prerequisites**

- A built ygopromcp binary from ~/ygo, see [ygopro/mcp-ygopromcp.md](../../ygopro/mcp-ygopromcp.md)
- srvpro running from vendor/srvpro, see [ygopro/mcp-ygopromcp.md](../../ygopro/mcp-ygopromcp.md) server notes
- Two YDK files: the target deck and a representative opponent deck
- The target deck's card codes split into #main, #extra, and !side sections per [ygopro/ydk.md](../../ygopro/ydk.md)

- **Research Phase**

- Run ydkshow.py on the target deck and on a corpus of similar decks to identify core cards, extenders, and ratios
- Run ydkcheck.py section all on the target deck to fix construction errors before play-test
- Read the relevant card scripts and ygopro database entries for any card whose timing is unclear
- Form a hypothesis for one-card combo, key extender lines, weak points, and common mistakes
- If a combo was learned from a video, treat it as a hypothesis until a self-duel reproduces the same end board and sequence

- **Duel Setup**

- Start srvpro with `node ygopro-server.js` from vendor/srvpro
- Create a room whose rule string contains NOCHECK or NC if either test deck is not legal under the current banlist
- Use the same room name and password for both clients
- Launch two ygopromcp processes from ~/ygo/bin/debug/YGOPro with matching host, port, room, and deck flags

- **Agent and Subagent Roles**

- The main agent drives the target deck and records observations
- Spawn a subagent to drive the opponent deck through its own MCP client
- Spawn the subagent and call ygo_connect there before calling ygo_connect on the target client
- Both agents must answer prompts with ygo_choose and look up cards with ygo_card when needed

- **During the Duel**

- Log every meaningful decision point, successful line, failed line, and hand-trap interaction
- Note which single card opens the full combo, which cards are dead draws, and where the engine halts
- Watch for chains, zones, and material choices that differ from the hypothesis
- Use ygo_surrender to end a lost game cleanly and move to the next game

- **After the Duel**

- Update the deck experience file under ygo/decks/<deck>/SKILL.md with verified findings
- Record the one-card combo baseline, named extenders, end fields, and halt points
- Add matchup notes if the opponent deck is a common meta choice
- Add common mistakes discovered during play
- Re-run ydkcheck.py to ensure the deck file still validates after any list changes

- **Iteration**

- Change one thing at a time in the deck list or in the combo sequencing
- Run another self-duel and compare the new results to the previous run
- Stop iterating when the deck consistently reaches its end field and the experience file captures all known lines

- **Performance Tips**

- Disable reasoning for both drivers or set reasoningEffort to off to avoid hitting the per-turn time limit
- Raise random_duel.hang_timeout and hostinfo.time_limit in vendor/srvpro/config/config.json if drivers are slow
- Keep both drivers at the same reasoning tier so one side does not win by timeout default
- A debug YGOPro client can crash after a timeout; prefer fast drivers and raised timeouts
