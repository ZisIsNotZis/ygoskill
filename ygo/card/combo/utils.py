#!/usr/bin/env python3
"""
Utility functions for ygo card database operations
"""

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
