#!/usr/bin/env python3
"""
Card Catalog Validator for ygo-skills
Validates catalog entries (handtrap, generic support, etc.) against cards.cdb
"""

import os
import re
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Import sqlite3 and Path for database operations
import sqlite3
from pathlib import Path

def load_db(db_path="cards.cdb"):
    """
    Load cards.cdb database from project root or specified path

    Args:
        db_path: Path to cards.cdb. Default is "cards.cdb" in combo directory.

    Returns:
        sqlite3.Connection object
    """
    # Try to find cards.cdb
    if Path(db_path).is_absolute():
        db_file = Path(db_path)
    else:
        # Start from combo directory
        db_file = Path("/home/z/ygo/ygo-skills/ygo/card/combo") / db_path

    if not db_file.exists():
        raise FileNotFoundError(f"Database file not found: {db_file}")

    return sqlite3.connect(str(db_file.absolute()))


def get_card_info(conn, card_id):
    """
    Get card information from database

    Args:
        conn: sqlite3.Connection object
        card_id: Integer card ID (8 digits)

    Returns:
        Dictionary with card info or None if not found
    """
    cursor = conn.cursor()
    cursor.execute("""
        SELECT d.type, d.atk, d.def, d.level, d.attribute, d.race, t.name
        FROM datas d
        JOIN texts t ON d.id = t.id
        WHERE d.id = ?
    """, (card_id,))

    result = cursor.fetchone()
    return {
        'id': result[0] if result else None,
        'type': result[1] if result else None,
        'atk': result[2] if result else None,
        'def': result[3] if result else None,
        'level': result[4] if result else None,
        'attribute': result[5] if result else None,
        'race': result[6] if result else None,
        'name': result[7] if result else None
    }


class CatalogValidator:
    """Validates catalog entries against cards.cdb"""

    def __init__(self, card_db_path="cards.cdb"):
        self.card_db_path = card_db_path
        self.conn = None

    def _connect_db(self):
        """Connect to cards.cdb"""
        self.conn = load_db(self.card_db_path)

    def _close_db(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()

    def validate_catalog(self, catalog_path, card_db_path="cards.cdb"):
        """
        Validate a single catalog file

        Args:
            catalog_path: Path to catalog .md file
            card_db_path: Optional path to cards.cdb (default is combo directory relative path)

        Returns:
            Tuple of (errors, warnings) lists
        """
        errors = []
        warnings = []

        # Resolve database path
        if card_db_path == "cards.cdb":
            db_path = Path("/home/z/ygo/ygo-skills/ygo/card/combo") / "cards.cdb"
        else:
            db_path = Path(card_db_path).absolute()
            # Ensure db_path is within project
            project_root = Path("/home/z/ygo/ygo-skills")
            if not str(db_path).startswith(str(project_root)):
                errors.append(f"Database path outside project: {db_path}")
                db_path = project_root / "cards.cdb"

        if not db_path.exists():
            errors.append(f"Database file not found: {db_path}")

        self.conn = load_db(str(db_path.absolute()))

        with open(catalog_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')

        current_card_id = None
        in_effect_block = False
        card_ids_seen = set()

        for i, line in enumerate(lines, 1):
            line = line.strip()
            if not line:
                continue

            # Check for card ID pattern
            card_match = re.match(r'^(\d{8})\s+', line)
            if card_match:
                card_id = card_match.group(1)
                current_card_id = card_id

                # Check if card ID exists in database
                card_info = get_card_info(self.conn, card_id)

                if card_info is None:
                    errors.append(f"Line {i}: Card ID {card_id} does not exist in database")
                else:
                    card_ids_seen.add(card_id)

                    # Check for alias field
                    if 'alias' in line:
                        # Verify alias exists
                        alias_match = re.search(r'alias\s*[:\s*(\d{8})\s*', line)
                        if alias_match:
                            alias_id = alias_match.group(1)
                            if get_card_info(self.conn, alias_id) is None:
                                errors.append(f"Line {i}: Alias ID {alias_id} does not exist in database")
            else:
                # If no card ID match, just continue
                continue

            # Check for hand trap criteria
            if 'hand trap criteria' in line.lower():
                self._validate_hand_trap(line, i, errors, warnings, content)

            # Check for generic support criteria
            if 'generic support criteria' in line.lower():
                self._validate_generic_support(line, i, errors, warnings, content)

        # Check for duplicate card entries
        duplicate_card_ids = [cid for cid in card_ids_seen if list(card_ids_seen).count(cid) > 1]
        if duplicate_card_ids:
            for cid in duplicate_card_ids:
                errors.append(f"Card ID {cid} appears more than once (likely duplicate entry)")

        # Return results
        self._close_db()
        return errors, warnings

    def _validate_hand_trap(self, line, line_num, errors, warnings, content):
        """Validate hand trap entry follows as 3-condition requirement"""
        # Extracts criteria from the line
        match = re.search(r'criteria:\s*(.+)', line, re.IGNORECASE)

        if not match:
            errors.append(f"Line {line_num}: 'hand trap criteria' without criteria specification")
            return

        criteria_text = match.group(1).strip()
        conditions = [c.strip() for c in criteria_text.split(',')]

        # Must have exactly 3 conditions
        if len(conditions) != 3:
            errors.append(f"Line {line_num}: Hand trap must have exactly 3 conditions, found {len(conditions)}")

        # Check each condition is valid
        # Valid keywords: hand activation + opponent interaction + interference keyword
        valid_keywords = [
            r'从手卡', '手卡', '从手牌',
            r'对方', '对方',
            r'干扰', '干扰',
            r'无效', '无效化',
            r'破坏', '破坏',
            r'除外', '除外'
        ]

        for condition in conditions:
            condition_lower = condition.lower()

            # Check for negation
            if any(neg in condition_lower for neg in ['不', '无', '非']):
                errors.append(f"Line {line_num}: Condition contains negation: '{condition}'")

            # Check if it references opponent interaction
            has_opponent = any(kw in condition_lower for kw in ['对方', '对方', 'opponent'])
            has_hand = any(kw in condition_lower for kw in ['手', '手', 'hand'])
            has_interference = any(kw in condition_lower for kw in ['干扰', '干扰'])

            if has_opponent and has_hand:
                # Must also have interference to be a hand trap
                if not has_interference:
                    warnings.append(f"Line {line_num}: Opponent+hand but no interference keyword")

            # Check for effect verification
            if not (has_opponent or has_interference):
                errors.append(f"Line {line_num}: Missing opponent interaction check")

    def _validate_generic_support(self, line, line_num, errors, warnings, content):
        """Validate generic support entry doesn't have archetype restrictions"""
        # Extracts criteria from the line
        match = re.search(r'criteria:\s*(.+)', line, re.IGNORECASE)

        if not match:
            errors.append(f"Line {line_num}: 'generic support criteria' without criteria specification")
            return

        criteria_text = match.group(1).strip()

        # Generic support should NOT have archetype restrictions
        archetype_patterns = [
            r'系列|series',
            r'字段|field',
            r'只|only.*特定|specific'
        ]

        for pattern in archetype_patterns:
            if re.search(pattern, criteria_text, re.IGNORECASE):
                errors.append(f"Line {line_num}: Generic support contains archetype restriction: '{pattern}'")


def main():
    # Get directory to check
    if len(sys.argv) > 1:
        catalog_dir = Path(sys.argv[1])
    else:
        catalog_dir = Path("/home/z/ygo/ygo-skills/ygo/card/catalog")

    # Find all catalog .md files
    catalog_files = list(catalog_dir.glob("*.md"))

    if not catalog_files:
        print(f"No catalog files found in: {catalog_dir}")
        sys.exit(0)

    total_errors = 0
    total_warnings = 0

    print(f"Validating {len(catalog_files)} catalog file(s)...\n")

    validator = CatalogValidator()

    for catalog_file in catalog_files:
        errors, warnings = validator.validate_catalog(catalog_file)
        total_errors += len(errors)
        total_warnings += len(warnings)

        if errors or warnings:
            rel_path = catalog_file.relative_to(catalog_dir)
            print(f"\n{rel_path}:")
            for error in errors:
                print(f"  [ERROR] {error}")
            for warning in warnings:
                print(f"  [WARN] {warning}")

    # Summary
    print(f"\n=== SUMMARY ===")
    print(f"Total errors: {total_errors}")
    print(f"Total warnings: {total_warnings}")

    # Exit code: 0 = all pass, 1 = errors found
    sys.exit(1 if total_errors > 0 else 0)


if __name__ == "__main__":
    main()
