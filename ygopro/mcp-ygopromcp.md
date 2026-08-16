---
name: ygopromcp-client
description: ygopromcp MCP client forked from fluorohydride/ygopro for agent duel control
---
# ygopromcp MCP Client

- **What It Is**

- ygopromcp is a fork of fluorohydride/ygopro that adds a Model Context Protocol side channel to the GUI game
- The MCP bridge lives in the YGOPro binary, so the same build can run as a normal GUI client or be driven by an agent
- The source tree is the project root at ~/ygo, with MCP code in gframe/mcp.cpp and gframe/mcp.h
- MCP is initialized at startup and speaks newline-delimited JSON-RPC 2.0 over stdio
- No special flag is required to enable MCP; any binary built from this tree exposes it

- **Build**

- Use the existing YGOPro build system; a typical debug binary is ~/ygo/bin/debug/YGOPro
- A release binary is ~/ygo/bin/release/YGOPro
- The symlink ~/ygo/ygopro points at bin/debug/YGOPro
- Any YGOPro binary built from this tree exposes the same MCP tools

- **Headless Launch Flags**

- The binary accepts the normal gframe CLI flags for automatic room entry
- `-n <nick>` sets the nickname shown in the room
- `-h <host>` sets the server host, usually 127.0.0.1
- `-p <port>` sets the server port, srvpro default is 7911
- `-w <password>` sets the room password
- `-d <deckfile>` loads a deck file
- `-j` clicks the join-host button automatically
- `-k` keeps the process alive after a duel ends instead of exiting
- Example: `~/ygo/bin/debug/YGOPro -n Alpha -h 127.0.0.1 -p 7911 -w TestRoom -d deck/example.ydk -j -k`

- **MCP Tools**

- `ygo_connect` joins a room, uploads the deck, readies, and blocks until the first decision point or failure
- `ygo_choose` answers the pending prompt and blocks until the next decision point
- `ygo_card` explains a card by name substring or numeric code
- `ygo_chat` sends a chat message to the room
- `ygo_surrender` concedes the current game and blocks for the server response
- `ygo_disconnect` leaves the room and returns to the disconnected state

- **Dual-Client Connection Flow**

- Two independent YGOPro processes act as the two players in one room on a single srvpro server
- Spawn the opponent subagent and start its client before calling `ygo_connect` on the second client so both connect near-simultaneously
- A second `ygo_connect` while one is already in flight returns already connecting; wait for the pending prompt instead of retrying
- The first decision is Rock-Paper-Scissors with options 0 rock, 1 paper, 2 scissors, then the winner picks first or second turn
- Both clients must use the exact same room name and matching password; mismatches cause the pair to never meet

- **Reading Prompts**

- Each response shows game state, a short log, card explanations for relevant cards, then a line with options min to max of total
- `1 to 1 of 12` means pick exactly one option, `2 to 2 of 2` means pick both, `0 to 1 of 2` means pick zero or one
- Prompts with exactly one legal answer are auto-answered and never reach the agent
- Zone choices use my MZone index or my SZone index; position choices follow every monster placement
- Chain windows offer decline or chain with a specific card; material selection lists Xyz materials often requiring a list of ids

- **Server and Time Limits**

- Start the server from vendor/srvpro with `node ygopro-server.js`; the default port is 7911
- Server configuration lives at vendor/srvpro/config/config.json
- `random_duel.hang_timeout` ejects idle players; default was 90 but the current config uses 600
- `hostinfo.time_limit` is the per-turn seconds budget; current config uses 600
- Edit config.json and restart the server to apply timeout changes

- **Deck Research Play-Test**

- Corpus decks under ~/ygo/deck contain bare card codes without #main / #extra / !side headers
- Convert a corpus deck into proper YDK section format before play; see [ydk.md](ydk.md) for the section layout
- Create a room whose rule string contains NOCHECK or NC so srvpro skips banlist validation for non-legal test decks
- Match both clients reasoning effort for fair real-time play; a slow driver times out and loses
- Disable reasoning for both sides with reasoningEffort off to avoid AFK kicks during long self-duels
- A debug YGOPro client may segfault with rc=-11 after a timeout; raise timeouts and use fast drivers to reduce the risk
