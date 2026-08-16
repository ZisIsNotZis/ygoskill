---
name: mcp-client-overview
description: Choose and wire an MCP duel client for agent-driven YGOPro play
---
# MCP Duel Client Overview

- **Two Clients**

- ygopromcp is the full fluorohydride/ygopro fork with a GUI and an MCP side channel; use it for agent-vs-agent duels
- ygomcp is a fresh lightweight headless implementation at vendor/ygocli; deprecated for duels but still handy for solo tests

- **Prefer ygopromcp When**

- Running self-duels to evolve deck experience files under ygo/decks
- Connecting two agents to the same srvpro room for competitive play-test
- You need the most complete gframe protocol compatibility

- **Prefer ygomcp When**

- Running a quick solo in-process duel with `ygo_solo`
- Loading a single puzzle or replay without building the full YGOPro binary
- Spinning up a lightweight local server for a one-off test

- **Common Wiring**

- Start srvpro from vendor/srvpro with `node ygopro-server.js` on port 7911
- Launch two YGOPro or ygomcp processes with the same room name and password
- Spawn the opponent subagent before the second `ygo_connect` so both clients join simultaneously
- Disable reasoning for both drivers or raise server timeouts to avoid AFK kicks

- **Details**

- See [mcp-ygopromcp.md](mcp-ygopromcp.md) for the ygopromcp fork, build flags, and tools
- See [mcp-ygomcp.md](mcp-ygomcp.md) for the lightweight ygomcp modes, tools, and deprecation note
