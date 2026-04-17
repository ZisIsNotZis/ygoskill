# AutoKey Deck Crawler

- **Purpose**

AutoKey scripts that automate card data entry from the WeChat Mini Program "决斗者查卡器" (Duelist Card Checker). Simulates mouse clicks and keyboard input to extract deck lists from the mini program interface.

- **Prerequisites**

- AutoKey installed and running on Linux desktop
- WeChat desktop client with 决斗者查卡器 mini program open
- Screen resolution matching the click coordinates in the scripts

- **Scripts**

- **ygo.py** — Scans a list of cards by clicking through the mini program search results. Clicks each card in a 4-item column, extracts data from 3 detail screens per card, then scrolls. Runs in an infinite loop.
- **ygold.py** — Simpler variant that clicks through a single card repeatedly at a fixed position. Used for manual single-card extraction.
- **ygo.json** — AutoKey script configuration for ygo.py
- **folder.json** — AutoKey folder configuration

- **Usage**

1. Open WeChat desktop and navigate to 决斗者查卡器
2. Position the mini program window at the expected screen location
3. Start the AutoKey script
4. The script will auto-click through cards with 1 to 3.5 second delays
5. Results are captured via clipboard using clipdown.sh

- **Limitations**

- Click coordinates are hard-coded for a specific screen resolution
- Requires the mini program to be in a specific state before starting
- No error recovery if a click lands on the wrong element
- Timing is approximate and may need adjustment for slower systems
