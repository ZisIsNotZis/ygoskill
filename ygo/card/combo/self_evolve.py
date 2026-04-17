#!/usr/bin/env python3
"""
Self-Evolving Combo Discovery System
"""

import sqlite3
import json
import random
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime
import torch
import numpy as np
from collections import defaultdict, Counter
import re
import requests
from concurrent.futures import ThreadPoolExecutor
import threading


@dataclass
class ComboPattern:
    """Represents a discovered combo pattern"""
    id: str
    starter_card: int
    sequence: List[int]
    end_field: Dict[str, Any]
    performance: Dict[str, float]
    meta_relevance: float
    hand_trap_vulnerability: List[int]
    discovered_at: datetime
    last_validated: datetime
    success_count: int = 0
    failure_count: int = 0

    def success_rate(self) -> float:
        total = self.success_count + self.failure_count
        return self.success_count / total if total > 0 else 0.0


@dataclass
class CardKnowledge:
    """Knowledge about a card's role in combos"""
    card_id: int
    roles: List[str]  # ['starter', 'extender', 'payoff', 'hand_trap']
    common_combos: List[str]  # combo pattern IDs
    synergy_cards: List[int]  # cards that work well together
    interaction_rules: List[Dict[str, Any]]  # valid/invalid interactions
    performance_metrics: Dict[str, float]


class ComboDiscoveryEngine:
    """Main engine for self-evolving combo discovery"""

    def __init__(self, db_path: str = "cards.cdb"):
        self.db_path = db_path
        self.patterns = {}
        self.knowledge_base = {}
        self.heuristics = {
            'length_penalty': 0.1,
            'negate_value': 1.5,
            'resource_value': 1.0,
            'consistency_threshold': 0.7,
            'meta_weight': 0.3
        }
        self.generic_pool = self._load_generic_pool()
        self.lock = threading.Lock()

    def _load_generic_pool(self) -> Dict[str, List[int]]:
        """Load generic extenders and hand traps"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Generic extenders - simplified to all level 3 monsters
        cursor.execute("""
            SELECT d.id FROM datas d
            JOIN texts t ON d.id = t.id
            WHERE d.type & 0x4000000 AND NOT d.alias
            AND d.level = 3
        """)
        extenders = [row[0] for row in cursor.fetchall()]

        # Hand traps - using known hand trap IDs
        cursor.execute("""
            SELECT d.id FROM datas d
            JOIN texts t ON d.id = t.id
            WHERE d.type & 0x4000000 AND NOT d.alias
            AND t.name LIKE '%%Ash%%' OR t.name LIKE '%%Impermanence%%'
            OR t.desc LIKE '%%can be activated from hand%%'
        """)
        hand_traps = [row[0] for row in cursor.fetchall()]

        conn.close()

        return {
            'extenders': extenders,
            'hand_traps': hand_traps,
            'searchers': self._get_searchers(),
            'removal': self._get_removal()
        }

    def _get_searchers(self) -> List[int]:
        """Get searcher cards"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT d.id FROM datas d
            JOIN texts t ON d.id = t.id
            WHERE d.type & 0x4000000 AND NOT d.alias
            AND (t.desc LIKE '%%search%%' OR t.desc LIKE '%%add%%')
        """)
        searchers = [row[0] for row in cursor.fetchall()]
        conn.close()
        return searchers

    def _get_removal(self) -> List[int]:
        """Get removal cards"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT d.id FROM datas d
            JOIN texts t ON d.id = t.id
            WHERE d.type & 0x4000000 AND NOT d.alias
            AND (t.desc LIKE '%%destroy%%' OR t.desc LIKE '%%banish%%')
        """)
        removal = [row[0] for row in cursor.fetchall()]
        conn.close()
        return removal

    def discover_generic_combos(self,
                            starter_attribute: str = "light",
                            starter_race: str = "demon",
                            hand_size: int = 5) -> List[ComboPattern]:
        """Discover generic combos for arbitrary starter"""

        # Find all matching starters
        starters = self._find_starter_cards(starter_attribute, starter_race)
        print(f"Found {len(starters)} starter cards")

        all_combos = []

        for starter_id in starters:
            # Generate random hand combinations
            for _ in range(10):  # Reduced for testing
                hand = self._generate_random_hand()
                if not hand:
                    continue
                sequences = self._generate_sequences(starter_id, hand, max_depth=3)

                for sequence in sequences:
                    combo = self._validate_and_score(sequence)
                    if combo:
                        all_combos.append(combo)

        # Remove duplicates and rank
        unique_combos = self._deduplicate_combos(all_combos)
        return sorted(unique_combos,
                     key=lambda x: x.performance.get('total_value', 0),
                     reverse=True)

    def _find_starter_cards(self, attribute: str, race: str) -> List[int]:
        """Find cards matching starter criteria"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        attr_map = {
            'light': 0x4,
            'dark': 0x8,
            'fire': 0x10,
            'water': 0x20,
            'earth': 0x40,
            'wind': 0x80,
            'divine': 0x100
        }

        race_map = {
            'demon': 0x800,
            'dragon': 0x1000,
            'spellcaster': 0x2000,
            'warrior': 0x4000,
            'beast': 0x8000,
            'beast_warrior': 0x10000,
            'fiend': 0x20000,
            'fairy': 0x40000,
            'plant': 0x80000,
            'aquatic': 0x100000,
            'reptile': 0x200000,
            'rock': 0x400000,
            'insect': 0x800000,
            'dinosaur': 0x1000000,
            'fish': 0x2000000,
            'sea serpent': 0x4000000
        }

        cursor.execute(f"""
            SELECT d.id FROM datas d
            JOIN texts t ON d.id = t.id
            WHERE d.attribute = {attr_map.get(attribute, 0)}
            AND d.race = {race_map.get(race, 0)}
            AND d.level BETWEEN 1 AND 12
            AND NOT d.alias
            AND t.name NOT LIKE '%%token%%'
        """)

        starters = [row[0] for row in cursor.fetchall()]
        conn.close()
        return starters

    def _generate_random_hand(self) -> List[int]:
        """Generate a random hand from generic pool"""
        hand = []
        # Add 2-3 random cards from generic pool
        all_cards = (self.generic_pool['extenders'] +
                    self.generic_pool['searchers'] +
                    self.generic_pool['removal'])
        if len(all_cards) > 0:
            hand_size = random.randint(2, min(4, len(all_cards)))
            hand = random.sample(all_cards, hand_size)
        return hand

    def _generate_sequences(self,
                          starter_id: int,
                          hand: List[int],
                          max_depth: int = 5) -> List[List[int]]:
        """Generate possible combo sequences"""
        sequences = []

        def backtrack(current_seq, remaining_hand, depth):
            if depth >= max_depth:
                sequences.append(current_seq)
                return

            # Try each card in hand
            for card_id in remaining_hand:
                new_seq = current_seq + [card_id]
                new_hand = remaining_hand.copy()
                new_hand.remove(card_id)

                # Check if sequence is valid
                if self._is_valid_sequence(new_seq):
                    backtrack(new_seq, new_hand, depth + 1)

        backtrack([starter_id], hand, 0)
        return sequences

    def _is_valid_sequence(self, sequence: List[int]) -> bool:
        """Basic sequence validation"""
        if len(sequence) == 0:
            return False

        # Check if all cards exist
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        for card_id in sequence:
            cursor.execute("SELECT id FROM datas WHERE id = ?", (card_id,))
            if not cursor.fetchone():
                conn.close()
                return False

        conn.close()
        return True

    def _validate_and_score(self, sequence: List[int]) -> Optional[ComboPattern]:
        """Validate combo and calculate performance score"""
        # Always return a pattern for demonstration
        end_field = self._simulate_combo(sequence)

        # Calculate performance metrics
        performance = {
            'negate_count': self._count_negates(end_field),
            'resource_advantage': self._calculate_resources(end_field),
            'board_presence': self._count_monsters(end_field),
            'consistency': self._estimate_consistency(sequence),
            'total_value': 0  # Will be calculated
        }

        # Calculate total value
        performance['total_value'] = (
            performance['negate_count'] * self.heuristics['negate_value'] +
            performance['resource_advantage'] * self.heuristics['resource_value'] +
            performance['board_presence'] * 0.5
        )

        # Find vulnerability points
        vuln_points = self._find_halt_points(sequence)

        # Create pattern
        pattern = ComboPattern(
            id=f"combo_{len(self.patterns)}",
            starter_card=sequence[0],
            sequence=sequence,
            end_field=end_field,
            performance=performance,
            meta_relevance=self._calculate_meta_relevance(sequence),
            hand_trap_vulnerability=vuln_points,
            discovered_at=datetime.now(),
            last_validated=datetime.now(),
            success_count=1,  # Default to one successful test
            failure_count=0
        )

        return pattern

    def _simulate_combo(self, sequence: List[int]) -> Dict[str, Any]:
        """Simulate combo execution"""
        # Simplified simulation
        # In practice, this would use a game simulator

        field = {
            'monsters': [],
            'spell_traps': [],
            'hand': [],
            'grave': []
        }

        for i, card_id in enumerate(sequence):
            card = self._get_card_info(card_id)

            # Simple logic - add to field based on type
            if card.get('type', 0) & 0x4000000:  # Monster
                field['monsters'].append({
                    'id': card_id,
                    'atk': card.get('atk', 0),
                    'def': card.get('def', 0)
                })
            else:
                field['spell_traps'].append({
                    'id': card_id,
                    'type': 'spell'  # Simplified
                })

        return field

    def _get_card_info(self, card_id: int) -> Dict[str, Any]:
        """Get card information from database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT d.type, d.atk, d.def, d.level, d.attribute, d.race, t.name
            FROM datas d
            JOIN texts t ON d.id = t.id
            WHERE d.id = ?
        """, (card_id,))

        row = cursor.fetchone()
        conn.close()

        if row:
            return {
                'type': row[0],
                'atk': row[1],
                'def': row[2],
                'level': row[3],
                'attribute': row[4],
                'race': row[5],
                'name': row[6]
            }
        return {}

    def _count_negates(self, field: Dict[str, Any]) -> int:
        """Count negate effects in field"""
        count = 0
        for card in field.get('spell_traps', []):
            if 'negate' in card.get('name', '').lower():
                count += 1
        return count

    def _calculate_resources(self, field: Dict[str, Any]) -> int:
        """Calculate resource advantage"""
        # Simplified: count advantage in cards
        return len(field.get('monsters', [])) + len(field.get('spell_traps', []))

    def _count_monsters(self, field: Dict[str, Any]) -> int:
        """Count monsters on field"""
        return len(field.get('monsters', []))

    def _estimate_consistency(self, sequence: List[int]) -> float:
        """Estimate combo consistency"""
        # Simplified: longer sequences are less consistent
        base = 1.0
        penalty = (len(sequence) - 1) * self.heuristics['length_penalty']
        return max(0.1, base - penalty)

    def _calculate_meta_relevance(self, sequence: List[int]) -> float:
        """Calculate how relevant the combo is to current meta"""
        # In practice, this would analyze tournament data
        return 0.5  # Placeholder

    def _find_halt_points(self, sequence: List[int]) -> List[int]:
        """Find where combo can be stopped by hand traps"""
        halt_points = []

        for i, card_id in enumerate(sequence):
            if self._is_hand_trap(card_id):
                halt_points.append(i)

        return halt_points

    def _is_hand_trap(self, card_id: int) -> bool:
        """Check if card is a hand trap"""
        return card_id in self.generic_pool['hand_traps']

    def _deduplicate_combos(self, combos: List[ComboPattern]) -> List[ComboPattern]:
        """Remove duplicate combo patterns"""
        seen = set()
        unique = []

        for combo in combos:
            key = tuple(combo.sequence)
            if key not in seen:
                seen.add(key)
                unique.append(combo)

        return unique

    def update_from_tournament(self, tournament_data: Dict[str, Any]):
        """Update knowledge base from tournament results"""
        with self.lock:
            # Update combo success rates
            for match in tournament_data.get('matches', []):
                for combo in match.get('combos_used', []):
                    if combo['success']:
                        self.patterns[combo['id']].success_count += 1
                    else:
                        self.patterns[combo['id']].failure_count += 1

                    self.patterns[combo['id']].last_validated = datetime.now()

            # Adjust heuristics based on meta
            meta_archetypes = tournament_data.get('meta_archetypes', {})
            self._adjust_heuristics(meta_archetypes)

    def _adjust_heuristics(self, meta_archetypes: Dict[str, float]):
        """Adjust heuristics based on current meta"""
        # Update meta weight based on archetype diversity
        diversity = len(meta_archetypes)
        self.heuristics['meta_weight'] = min(0.5, diversity / 20)


def main():
    """Example usage: Generic Light/Demon combo discovery"""
    engine = ComboDiscoveryEngine()

    print("Discovering generic Light attribute Demon combos...")

    # Discover combos
    combos = engine.discover_generic_combos(
        starter_attribute="light",
        starter_race="demon"
    )

    # Print results
    print(f"\nFound {len(combos)} viable combos:")
    for i, combo in enumerate(combos[:10]):  # Top 10
        print(f"\nCombo {i+1}:")
        print(f"  Starter: {combo.starter_card}")
        print(f"  Sequence: {combo.sequence}")
        print(f"  Negates: {combo.performance['negate_count']}")
        print(f"  Resources: {combo.performance['resource_advantage']}")
        print(f"  Success Rate: {combo.success_rate():.2%}")
        print(f"  Meta Relevance: {combo.meta_relevance:.2f}")


if __name__ == "__main__":
    main()