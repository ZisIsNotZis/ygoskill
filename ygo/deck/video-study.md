---
name: video-study
description: Learn from master players by downloading Bilibili videos and watching them with the watch skill
---
# Video Study from Bilibili Masters

- **Purpose**

- Improve understanding of a deck or matchup by watching high-level players explain or pilot it
- Extract combo sequencing, tech choices, side-deck plans, and timing decisions that written lists cannot show
- Cross-check deck experience files under ygo/decks against real master play

- **Tooling**

- BBDown downloads Bilibili videos; local install path varies, for example ~/.local/bin/BBDown
- Make sure BBDown is in PATH or invoke it by absolute path
- The watch skill at [.agents/skills/watch](../../../watch/SKILL.md) consumes the downloaded video and returns frames plus a transcript

- **Download Workflow**

- Find the Bilibili URL, BV number, av number, ep number, or ss number for the master video
- Create a clean work directory and run `BBDown <url>` from inside it
- BBDown writes the video file locally, often named after the title and page number
- For member-only or high-resolution videos, supply a cookie file or use the TV or app API flags as needed

- **Watch Workflow**

- Invoke the watch skill with the local video file and a focused question
- Example question: what is the opening combo line in this video
- Example question: which hand trap does the player keep and why
- Example question: how does the deck play through Ash Blossom
- For long videos, use the watch skill's --start and --end flags to focus on a single duel or turn
- If the video has no native captions and no Whisper key is available, use `--no-whisper` to get frames only and read the board state directly

- **Information to Extract**

- One-card and two-card combo lines with exact card order
- Extender choices when the primary combo is interrupted
- Board end fields and which cards the player prioritizes
- Hand-trap timing and which choke points the master respects
- Side-deck swaps for specific matchups
- Common mistakes or misplays the commentator warns against

- **Apply to Deck Experience**

- Compare the observed lines with the current ygo/decks/<deck>/SKILL.md file
- Update or add the one-card combo baseline if the master uses a different line
- Add named extender entries for any flexible piece the master highlights
- Record halt points discovered in the video, such as when the combo loses to a specific hand trap
- Add matchup notes when the master plays against a deck already in the corpus

- **Transcription Fallbacks**

- If `/watch` cannot transcribe because captions are missing and no Groq/OpenAI key is configured, try local whisper.cpp with all CPU cores (`-t $(nproc)`) and a fast model such as `ggml-large-v3-turbo-q5_0.bin`
- If local transcription is too slow for a long video, download viewer danmaku with `BBDown --danmaku-only` to collect timestamps and community notes
- For tutorial videos that display spreadsheets or slide decks, use `ffmpeg -ss <timestamp> -i <video> -vframes 1` to extract high-resolution crops and read them directly

- **Card Lookup**

- Convert captured card names into card IDs with `ydkshow.py <keyword>` so every line in the deck experience file has a verified ID
- When a card name is ambiguous, query `cards.cdb` directly or check the in-game card text from the video frame

- **Verification**

- After updating the deck experience file, replay the same lines in ygopromcp self-duels using playtest-evolution.md
- Do not treat a single video as gospel; cross-check with corpus consensus and ydkshow.py output
- Mark any line copied from a video as video-sourced until it is confirmed by script or self-duel
