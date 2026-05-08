---
name: ygo-card-combo-self-evolve
description: Combo skill self-evolution based on validation failures and new patterns
---
# Combo Skill Self-Evolution

- **Evolution Triggers**

  - When a discovered combo is proven invalid → update validate rules
  - When a better combo path is found for an existing starter → update discover strategies
  - When a common pitfall is identified → add to validate pitfall list
  - When a new high-performance pattern emerges → record key observation in discover

- **Evolution Rules**

  - Record only key observations and rules, never specific combo examples
  - Each update must identify the root cause (missing rule vs wrong rule vs missing knowledge)
  - If a skill was followed but produced wrong results, the skill itself is wrong — fix the skill

- **Acceptance Criteria**

  - AC: Run mdcheck.py validation script with zero errors
  - AC: Run catalogcheck.py validation script with zero errors  
  - AC: Run combocheck.py validation script with zero errors
  - AC: All markdown files under 200 lines
  - AC: All files use bullet points only (no numbered lists, tables, or checkboxes)
  - AC: All files properly linked in tree structure
  - AC: No duplicate or conflicting content in any markdown file
  - AC: Combo steps follow material accounting rules (max 15 materials, max 3 copies per card)
  - AC: Combo steps follow phase restriction rules
  - AC: Combo steps follow resolution order rules
