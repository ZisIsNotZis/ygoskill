#!/usr/bin/env python3
"""
Combo Step Validator for ygo-skills
Validates combo steps against combo validation rules and cards.cdb
Enforces material accounting, card source verification, phase restrictions, and resolution order
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple, Dict, Optional

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


class ComboStepValidator:
    """Validates combo steps against combo validation rules and cards.cdb"""

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

    def validate_combo_file(self, combo_file_path: Path) -> Tuple[List[str], List[str]]:
        """
        Validate a single combo file against validation rules

        Args:
            combo_file_path: Path to combo .md file

        Returns:
            Tuple of (errors, warnings) lists
        """
        errors = []
        warnings = []

        # Resolve database path
        db_path = Path("/home/z/ygo/ygo-skills/ygo/card/combo") / "cards.cdb"
        if not db_path.exists():
            errors.append(f"Database file not found: {db_path}")
            return errors, warnings

        self.conn = load_db(str(db_path.absolute()))

        with open(combo_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')

        # Parse combo steps
        steps = self._parse_combo_steps(lines)
        if not steps:
            errors.append("No valid combo steps found in file")
            return errors, warnings

        # Validate each step
        for i, step in enumerate(steps, 1):
            step_errors, step_warnings = self._validate_step(step, i, steps)
            errors.extend(step_errors)
            warnings.extend(step_warnings)

        # Validate material accounting
        material_errors = self._validate_material_accounting(steps)
        errors.extend(material_errors)

        # Validate resolution order
        resolution_errors = self._validate_resolution_order(steps)
        errors.extend(resolution_errors)

        self._close_db()
        return errors, warnings

    def _parse_combo_steps(self, lines: List[str]) -> List[Dict]:
        """Parse combo steps from file content"""
        steps = []
        current_step = None
        step_number = 0

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Check for step number pattern (e.g., "1.", "2.", "1.2.")
            step_match = re.match(r'^(\d+)\.\s+(.+)', line)
            if step_match:
                step_number = int(step_match.group(1))
                step_content = step_match.group(2).strip()

                # Save previous step if exists
                if current_step:
                    steps.append(current_step)

                current_step = {
                    'number': step_number,
                    'content': step_content,
                    'cards': [],
                    'phases': [],
                    'sources': []
                }
            elif current_step and line.startswith('- '):
                # Parse bullet points within step
                bullet_content = line[2:].strip()
                current_step['content'] += f" {bullet_content}"

                # Extract card IDs from bullet points
                card_match = re.search(r'(\d{8})', bullet_content)
                if card_match:
                    card_id = card_match.group(1)
                    current_step['cards'].append(card_id)

                    # Extract phase information
                    phase_match = re.search(r'(Main|Battle|End|Draw|Standby|Main2|Battle2|End2)', bullet_content)
                    if phase_match:
                        current_step['phases'].append(phase_match.group(1))

                    # Extract source information
                    source_match = re.search(r'(Hand|Deck|GY|Extra|Field|Banished)', bullet_content)
                    if source_match:
                        current_step['sources'].append(source_match.group(1))

        # Add last step
        if current_step:
            steps.append(current_step)

        return steps

    def _validate_step(self, step: Dict, step_index: int, all_steps: List[Dict]) -> Tuple[List[str], List[str]]:
        """Validate individual combo step"""
        errors = []
        warnings = []

        step_num = step['number']
        step_content = step['content']
        cards = step['cards']

        # Check card existence
        for card_id in cards:
            card_info = get_card_info(self.conn, card_id)
            if card_info is None:
                errors.append(f"Step {step_num}: Card ID {card_id} does not exist in database")
            elif card_info['type'] not in ['Monster', 'Spell', 'Trap']:
                warnings.append(f"Step {step_num}: Card ID {card_id} is not a monster, spell, or trap card")

        # Check phase restrictions
        phases = step['phases']
        if phases:
            # Main phase should not contain battle phase actions
            if 'Main' in phases and any(phase in ['Battle', 'Battle2'] for phase in phases):
                errors.append(f"Step {step_num}: Main phase cannot contain battle phase actions")

            # End phase should not contain summoning or setting
            if 'End' in phases and any(phase in ['Main', 'Main2'] for phase in phases):
                warnings.append(f"Step {step_num}: End phase should not contain summoning or setting actions")

        # Check source restrictions
        sources = step['sources']
        if sources:
            # Deck draws should be in Draw phase
            if 'Deck' in sources and 'Draw' not in phases:
                warnings.append(f"Step {step_num}: Deck draw should be in Draw phase")

            # Extra deck summons should be in Main phase
            if 'Extra' in sources and 'Main' not in phases and 'Main2' not in phases:
                warnings.append(f"Step {step_num}: Extra deck summon should be in Main phase")

        # Check for duplicate cards in same step
        if len(cards) != len(set(cards)):
            duplicate_cards = [card for card in cards if cards.count(card) > 1]
            for card_id in set(duplicate_cards):
                errors.append(f"Step {step_num}: Duplicate card ID {card_id} in same step")

        return errors, warnings

    def _validate_material_accounting(self, steps: List[Dict]) -> List[str]:
        """Validate material accounting across all steps"""
        errors = []
        card_counts = {}
        total_materials = 0

        for step in steps:
            for card_id in step['cards']:
                card_counts[card_id] = card_counts.get(card_id, 0) + 1

        # Check for excessive material usage
        for card_id, count in card_counts.items():
            if count > 3:  # Maximum 3 copies of any card
                errors.append(f"Card ID {card_id} used {count} times (maximum 3 allowed)")

        # Check total material count
        total_materials = sum(len(step['cards']) for step in steps)
        if total_materials > 15:  # Maximum 15 materials per combo
            errors.append(f"Total materials ({total_materials}) exceed maximum of 15")

        return errors

    def _validate_resolution_order(self, steps: List[Dict]) -> List[str]:
        """Validate resolution order of combo steps"""
        errors = []

        # Check step numbering
        expected_numbers = list(range(1, len(steps) + 1))
        actual_numbers = [step['number'] for step in steps]

        if actual_numbers != expected_numbers:
            errors.append(f"Step numbering is incorrect. Expected: {expected_numbers}, Got: {actual_numbers}")

        # Check phase sequence
        for i in range(len(steps) - 1):
            current_phases = steps[i]['phases']
            next_phases = steps[i + 1]['phases']

            # Main phase should be followed by Main, Battle, or End phase
            if 'Main' in current_phases and 'Main' not in next_phases and 'Battle' not in next_phases and 'End' not in next_phases:
                errors.append(f"Step {steps[i]['number']} to {steps[i+1]['number']}: Invalid phase transition from Main")

            # Battle phase should be followed by Battle2 or End phase
            if 'Battle' in current_phases and 'Battle2' not in next_phases and 'End' not in next_phases:
                errors.append(f"Step {steps[i]['number']} to {steps[i+1]['number']}: Invalid phase transition from Battle")

            # End phase should be followed by End2 or Main2 phase
            if 'End' in current_phases and 'End2' not in next_phases and 'Main2' not in next_phases:
                errors.append(f"Step {steps[i]['number']} to {steps[i+1]['number']}: Invalid phase transition from End")

        return errors


def main():
    # Get file to check
    if len(sys.argv) > 1:
        combo_file = Path(sys.argv[1])
    else:
        combo_file = Path("/home/z/ygo/ygo-skills/ygo/card/combo/validate/SKILL.md")

    if not combo_file.exists():
        print(f"Combo file not found: {combo_file}")
        sys.exit(1)

    validator = ComboStepValidator()
    errors, warnings = validator.validate_combo_file(combo_file)

    if errors or warnings:
        print(f"\nValidating {combo_file.name}:")
        for error in errors:
            print(f"  [ERROR] {error}")
        for warning in warnings:
            print(f"  [WARN] {warning}")

    # Summary
    print(f"\n=== SUMMARY ===")
    print(f"Total errors: {len(errors)}")
    print(f"Total warnings: {len(warnings)}")

    # Exit code: 0 = all pass, 1 = errors found
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()