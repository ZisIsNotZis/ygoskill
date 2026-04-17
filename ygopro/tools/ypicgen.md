# ypicgen.sh — Card Image Generator

- **Purpose**

Generate official-style Yu-Gi-Oh! card images from database and artwork. Converts raw card data into visually complete cards with proper layout, text, and images.

- **Requirements**

Works in the `expansions/` directory. Requires:
- bash
- sqlite3 (for card data)
- imagemagick (convert, mogrify, composite)
- Custom textures in `textures/` directory
- Card artwork in `pico/<id>.*` files

- **Dependencies**

- `cards.cdb` (SQLite database in parent directory)
- `textures/` — Template files and graphics
- `pico/` — Card artwork files (png, jpg, etc.)
- `pics/` — Output directory for generated cards

- **Usage**

```bash
cd expansions
./ypicgen.sh
```

- **Process**

For each card in cards.cdb:
1. Check if image already exists in `pics/` - skip if present
2. Read card data: name, type, level/attribute/race, ATK/DEF, effect
3. Generate card image using imagemagick:
   - Apply template based on card type (card_effect.webp, etc.)
   - Overlay card name with gold text effect
   - Add attribute icons from textures/att_*.webp
   - Insert monster portrait from pico/<id>*
   - Add effect text with word wrapping
   - Include level/rank stars
   - Set ATK/DEF values

- **Customization**

Environment variables:
- `NAMESZ`: Name font size (default 25, 15 for NAME2)
- `NAMEY`: Name vertical position (default 55, 44 for NAME2)

- **Design Notes**

- Uses hardcoded coordinates for element placement
- Requires accurate card data in correct format
- Monster portraits should be 300x300 minimum
- Effect text auto-wraps at 35 characters per line
- Chinese character support via WenquanYi-Micro-Hei font
- Creates official-looking cards with professional layout
