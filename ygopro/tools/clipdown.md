# clipdown.sh

- **Purpose**

Monitor clipboard content and automatically save YDK format text to timestamped files. Captures deck lists copied from any source (WeChat, Discord, etc.).

- **Requirements**

Separate installation at `~/my/ygo/clipdown.sh` (included in local directory). Requires:
- bash
- xclip (for clipboard access)
- clipnotify (for clipboard change monitoring)

- **Setup**

1. Install dependencies:
```bash
sudo apt install xclip clipnotify
```

2. Run the script in background:
```bash
nohup ~/my/ygo/clipdown.sh > clipdown.log 2>&1 &
```

- **Usage**

The script runs continuously:
- Monitors clipboard changes using clipnotify
- When clipboard content changes, saves it as `<timestamp>.ydk`
- Timestamp format: UNIX epoch in seconds

- **Example**

After copying a YDK from WeChat:
- Clipboard contains YDK content
- clipdown detects the change
- Saves to: `1234567890.ydk`

- **Notes**

- Designed for YDK crawler integration
- Creates file with every clipboard change - may create many files
- Use in combination with clipdown.sh for continuous monitoring
- Files are saved in current working directory
- To stop: `pkill -f clipdown.sh`
- Combine with tools/ydkrename.py to rename downloaded decks
