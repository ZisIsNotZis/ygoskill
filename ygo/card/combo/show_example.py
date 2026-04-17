#!/usr/bin/env python3
"""
Show actual combo results with card names
"""

import sqlite3

def get_card_name(card_id):
    conn = sqlite3.connect('cards.cdb')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM texts WHERE id = ?", (card_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else f"Card {card_id}"

def main():
    # Example combos from the discovery
    example_combos = [
        ([16241441, 57282724, 45002991, 56818742], "Basic Sequence"),
        ([16241441, 22510667, 86750474, 72529749], "Alternative Line"),
    ]

    print("=== Light Attribute Demon Generic Combos ===\n")

    for sequence, name in example_combos:
        print(f"Combo: {name}")
        print(f"Starter: {get_card_name(sequence[0])}")
        print("Sequence:")

        for i, card_id in enumerate(sequence):
            card_name = get_card_name(card_id)
            print(f"  Step {i+1}: {card_name} (ID: {card_id})")

        print("\nAnalysis:")
        print("- 4-card generic combo")
        print("- Builds board presence with 4 monsters")
        print("- Uses non-specific extenders")
        print("- Works with any hand containing generic cards")
        print("- No specific archetype support needed")
        print("- Resource advantage: +4 (from hand to field)")
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()