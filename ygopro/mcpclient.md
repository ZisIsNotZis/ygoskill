# MCP Duel Client

- **What It Is**

- The YGOPro binary exposes a Model Context Protocol server with direct tools ygo_connect, ygo_choose, ygo_chat, ygo_card, ygo_surrender, and ygo_disconnect
- Two independent server instances act as two players in one room against one srvpro server
- Wire the servers in the dsh profile patch at ~/.dsh/profiles/web/cordis.patch.yml using the dsh-mcp-client plugin, one instance per serverName
- Agent-facing tool names appear as mcp__serverName__toolName once the profile hot-reloads

- **Connect Flow**

- ygo_connect with host, port, deck path, and name joins the room, uploads the deck, readies, and blocks until the first decision point (Rock-Paper-Scissors, turn order, or prompt) or a failure
- Because connect blocks until game start, spawn the opponent client driver subagent before calling connect on the second client so both connect near-simultaneously
- A connect while one is in flight returns error already connecting — do not retry, the pending prompt will arrive
- The first decision is Rock-Paper-Scissors with option 0 rock, 1 paper, 2 scissors, then the winner picks go first or go second

- **Prompt Format**

- Every response shows game state, a log, card explanations for relevant cards, then a line with options min to max of total numbered choices
- The min to max range is how many options to select: 1 to 1 of 12 means pick exactly 1 of 12, 2 to 2 of 2 means pick both of 2, 0 to 1 of 2 means pick 0 or 1
- Single-answer prompts with exactly one legal choice are auto-answered and never reach the agent
- Each ygo_choose call answers the pending prompt and blocks until the next decision point, so every call advances exactly one prompt

- **Common Prompt Types**

- Zone choice asks where to place a summon or set, shown as my MZone index or my SZone index
- Position choice offers face-up attack, face-down defense, face-up defense, and face-down attack, appearing after every monster placement
- Chain window offers decline or chain with a specific card, deciding whether to respond to an effect activation
- Material selection lists Xyz materials, often requiring a list of ids when the range is 2 to 2
- Search and retrieval prompts list deck, hand, or graveyard candidates to pick from
- Yes or no prompts confirm optional effect triggers

- **Reading the State**

- self and oppo views are from your side, with oppo cards shown as question marks unless revealed
- The board grid row3 is monster zones, row4 is spell and trap zones, columns 0 to 4 plus the field zone
- Log lines use C1 and C2 for chain links, moved H to M0 for hand to monster zone 0, and solving and solved for chain resolution
- The card explain block gives full effect text of cards involved in the current prompt

- **Playing a Turn**

- Read the full option list on every prompt before choosing, because position prompts look identical across summons and cause repeated identical calls
- Answer chain windows deliberately, declining lets your own effect resolve while chaining interrupts the opponent play
- Use ygo_card to look up any card name or id before deciding
- Use ygo_chat for the room log, ygo_surrender to concede, and ygo_disconnect to leave after game over

- **Time and AFK Limits**

- srvpro config lives at ~/srvpro/config/config.json after the server was moved to the home directory, holding random_duel.hang_timeout default 90 which ejects idle players and hostinfo.time_limit default 180 which is the in-game time per turn
- The server ejects idle players after the timeout and may award the game to the opponent, so a slow-reasoning driver times out and loses
- Raise both values in config.json and restart the server to give slow drivers headroom, for example hang_timeout 600 and time_limit 600
- The server reads config at startup, edit config.json then restart node ygopro-server.js from ~/srvpro to apply
- Match both clients reasoning tier for fair real-time play, since a high-effort subagent thinks too long per prompt and gets AFK kicked while a fast client wins by default
- Disable reasoning for both sides by setting reasoningEffort to off in ~/.dsh/settings.yaml, watch for the web UI or a later save overwriting the file back to high

- **Deck Research Play-Test**

- The corpus under ~/ygo/deck holds tens of thousands of directories named date plus card-name concatenations, each containing ONE bare .ydk with a flat list of numeric card codes and NO main/extra section headers
- The MCP client loader deckManager.LoadCurrentDeck needs #main / #extra / !side headers, so a raw corpus deck must be converted before it can be play-tested
- Convert a corpus deck with the helper /home/z/ygo/deck2ydk.py SRC_DIR_or_file, which reads the numeric codes, splits them into main and extra using the TYPE_ bits from cards.cdb (extra = FUSION 0x40 or SYNCHRO 0x2000 or XYZ 0x800000 or LINK 0x4000000), and writes ./deck/example5.ydk with proper sections; codes unknown to cards.cdb are dropped and reported
- A deck whose main/extra must NOT be re-split (a hand-built example) should just be copied verbatim to an exampleN.ydk
- Many corpus decks are non-legal under the current banlist or export incomplete; do not fix the deck, instead create a room with a rule string that contains NOCHECK or NC — srvpro treats that substring in the room/rule as hostinfo.no_check_deck and skips deck validation entirely (ygopro-server.js:1844), no server config edit required
- The example decks currently in use: deck/example.ydk, example3.ydk, example4.ydk, example5.ydk (deck2ydk output)
- Start the local server from ~/srvpro with node ygopro-server.js (port 7911) before connecting MCP clients; rooms optionally use a name/password to pair the two client instances

