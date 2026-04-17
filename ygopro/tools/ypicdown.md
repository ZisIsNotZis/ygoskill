# ypicdown.sh

- **Purpose**

Download missing Yu-Gi-Oh! card images from the CDN `cdn.233.momobako.com` using card IDs. Converts webp to jpg for better compatibility.

- **Requirements**

Separate installation at `~/my/ygo/ypicdown.sh` (included in local directory). Requires:
- bash
- sqlite3 (to query card IDs)
- curl (for downloading)
- imagemagick (for mogrify conversion)

- **Usage**

```bash
cd /home/z/ygo
bash ~/my/ygo/ypicdown.sh
```

- **Process**

1. Query all card IDs from `cards.cdb` that don't have corresponding images in `pics/`
2. For each missing ID, download from: `https://cdn.233.momobako.com/ygoimg/ygopro/<id>.webp`
3. Convert downloaded webp to jpg using mogrify
4. Delete original webp files

- **Example**

If card 12345.jpg is missing:
- Download: `https://cdn.233.momobako.com/ygoimg/ygopro/12345.webp`
- Convert: `mogrify -format jpg pics/12345.webp`
- Cleanup: `rm pics/12345.webp`

- **Notes**

- Only downloads cards that are completely missing (no .jpg, .png, .webp)
- Downloads are sequential - could be optimized with parallel downloading
- Requires internet connection
- CDN may have rate limits - script doesn't handle retries
- After download, run expansions/ypicgen.sh to generate card images
