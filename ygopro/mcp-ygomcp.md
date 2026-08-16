---
name: ygomcp-client
description: ygomcp lightweight headless MCP duel client at vendor/ygocli
---
# ygomcp Lightweight MCP Client

- **What It Is**

- ygomcp is a freshly implemented headless MCP duel client that lives at vendor/ygocli
- It has no GUI, no gframe code, and no dependency on the fluorohydride/ygopro source tree
- The project was originally called ygocli but the CLI part was removed, so the correct name is ygomcp
- It is now deprecated in favor of ygopromcp for new agent duel workflows

- **Build**

- Run `make` in vendor/ygocli to build the `ygomcp` binary
- The build uses C++17 and links against sqlite3
- Data files must sit next to the binary: cards.cdb, strings.conf, script/, wiki/, single/, replay/

- **Running Modes**

- `ygomcp mcp` starts the MCP server on stdio for agent control
- `ygomcp server` starts a standalone duel server that other clients can join
- `ygomcp <deck0.ydk> <deck1.ydk> [--auto]` runs a solo in-process duel with god view
- `ygomcp interact` runs an interactive text session
- `ygomcp replay <file.yrp>` plays back a replay
- `ygomcp puzzle <puzzle>` loads a puzzle from single/<puzzle>/

- **MCP Tools**

- `ygo_solo` runs both players in-process from the same session
- `ygo_client` connects to a ygopro/gframe server such as srvpro
- `ygo_choose` answers a pending prompt by id or indices
- `ygo_card` searches the card database by name or code
- `ygo_wiki` greps bundled concept files under wiki/
- `ygo_exit` closes the current network connection
- `ygo_surrender` concedes while keeping the connection alive through match side exchange
- `ygo_observe` connects as a public-view observer that is never prompted
- `ygo_replay` narrates a saved replay
- `ygo_server` / `ygo_server_exit` launch or stop a built-in server child
- `ygo_windbot` / `ygo_windbot_exit` launch or stop a WindBot AI client
- `ygo_puzzle` plays a puzzle with optional setup.lua scripting

- **Network Notes**

- Implements the gframe wire protocol version 0x1362
- Supports optional room passwords set by the host and matched on join
- Best-of-3 matches exchange side decks automatically after each game
- Observers sit in seats 2 through 7 and see only public information
- Client-to-srvpro compatibility is the primary target; server-to-gframe is best-effort

- **When to Use**

- Use ygomcp for lightweight solo validation, puzzles, or replays when the full YGOPro build is not needed
- Use ygomcp as a local server to pair with a ygopromcp client for quick tests
- Prefer ygopromcp for competitive agent-vs-agent duels and for updating deck experience files
