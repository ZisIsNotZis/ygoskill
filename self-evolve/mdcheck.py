#!/usr/bin/env python3
"""
Markdown Linting and Tree Validation for ygo-skills
Enforces markdown-maintenance.md rules and tree structure
"""

import os
import re
import sys
from pathlib import Path

# Constants for markdown rules
MAX_LINES_PER_FILE = 200


class MarkdownLinter:
    """Check markdown files for compliance with markdown-maintenance.md rules"""

    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.errors = []
        self.warnings = []

    def _check_line_count(self):
        """Check if file exceeds 200 lines"""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if len(lines) > MAX_LINES_PER_FILE:
                self.errors.append(f"File exceeds {MAX_LINES_PER_FILE} lines: {len(lines)}")
                return False
        return True

    def _check_bullet_points_only(self):
        """Check if file uses bullet points, no numbered lists, no tables, no checkboxes"""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for numbered lists (e.g., "1.", "2.", "- [ ]")
        numbered_list_pattern = r'^\s{0,9}\.|\s{1,2}\)\s|^\s*-\s+\d+\s+\]'
        if re.search(numbered_list_pattern, content, re.MULTILINE):
            self.errors.append("Contains numbered list (1. or 2. or 1.2.)")
            return False

        # Check for checkboxes
        checkbox_pattern = r'- \[ \]'
        if re.search(checkbox_pattern, content, re.MULTILINE):
            self.errors.append("Contains checkbox format (- [ ])")
            return False

        # Check for tables
        table_pattern = r'^\|?---?\|?$'
        if re.search(table_pattern, content, re.MULTILINE):
            self.errors.append("Contains table format (--- or |)")
            return False

        # Check for heading nesting beyond single #
        heading_pattern = r'^(#{1,6})\s'
        lines = content.split('\n')
        current_heading_level = 0
        for i, line in enumerate(lines, 1):
            # Skip empty lines
            if not line.strip():
                continue
            if re.match(r'^(#{1,6})\s', line):
                if line.strip('#').count('#') > current_heading_level:
                    if current_heading_level > 1:
                        self.errors.append(f"Heading nesting beyond level {current_heading_level}: {line.strip()[:50]}")
                        return False
                    current_heading_level = line.strip('#').count('#')
        return True

    def _check_content_quality(self):
        """Check that every item is clear, specific, informative, compact, and necessary"""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')

        # Check for duplicates or conflicts
        paragraphs = self._extract_paragraphs(content)
        if len(paragraphs) > len(set(paragraphs)):
            self.warnings.append("Potential duplicate or conflicting content")

        # Check for vague statements
        vague_patterns = [r'\s*is important\s*', r'\s*useful\s*', r'\s*good\s*', r'\s*bad\s*']
        for pattern in vague_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                self.warnings.append(f"Contains vague statement pattern: {pattern}")

        return True

    def _extract_paragraphs(self, content):
        """Extract text blocks separated by blank lines"""
        return [p.strip() for p in content.split('\n\n') if p.strip()]


def check_tree_structure(root_dir):
    """
    Verify all SKILL.md files are properly linked from parent SKILL.md
    No orphaned files, all files reachable via links
    """
    errors = []

    root_skill_md = root_dir / "SKILL.md"
    if not root_skill_md.exists():
        errors.append(f"Root SKILL.md not found: {root_skill_md}")

    # Build a mapping of all markdown files
    md_files = {}
    for md_file in root_dir.rglob("**/*.md"):
        rel_path = md_file.relative_to(root_dir)
        md_files[str(rel_path)] = md_file

    # Check for orphaned files (files that exist but not linked)
    for md_file in root_dir.rglob("**/*.md"):
        # Skip root SKILL.md
        if md_file == root_skill_md:
            continue

        rel_path = md_file.relative_to(root_dir)
        # Find which SKILL.md should link to this file
        # Traverse up to find the nearest parent with SKILL.md
        expected_parent = None
        for parent in md_file.parents:
            if (parent / "SKILL.md").exists():
                expected_parent = parent
                break

        if expected_parent is None:
            # This is a top-level markdown (should be linked from root)
            if not (root_dir / "SKILL.md").read_text():
                errors.append(f"Orphaned file not linked: {md_file}")
        else:
            # This is a sub-skill markdown - check if linked from parent
            parent_content = expected_parent.read_text()
            if rel_path.as_posix() not in parent_content:
                errors.append(f"File not linked from parent: {md_file}")

    # Check naming convention: research, build, compare, self-evolve are folders
    naming_violations = []
    for md_file in root_dir.rglob("**/*.md"):
        name = md_file.name
        # Check if any of the standard sub-skill names are used as files (with hyphens)
        standard_subskills = ["research", "build", "compare", "self-evolve"]
        if name in standard_subskills:
            # Should be a directory
            if not md_file.is_dir():
                errors.append(f"Sub-skill is file not directory: {name}")
            # Should not contain hyphens
            else:
                naming_violations.append(f"Sub-skill file contains hyphens: {name}")

    return errors


def check_markdown_file(file_path, sections=None):
    """
    Check a single markdown file for compliance
    Returns (errors, warnings)
    """
    linter = MarkdownLinter(file_path)

    errors = []
    warnings = []

    # Run all checks
    if not linter._check_line_count():
        errors.extend(linter.errors)

    if not linter._check_bullet_points_only():
        errors.extend(linter.errors)

    if not linter._check_content_quality():
        warnings.extend(linter.warnings)

    return errors, warnings


def main():
    # Get root directory from first argument or default to ygo-skills
    if len(sys.argv) > 1:
        root_dir = Path(sys.argv[1])
    else:
        root_dir = Path("/home/z/ygo/ygo-skills")

    sections = None
    if len(sys.argv) > 2:
        sections = sys.argv[2:]

    # Check all markdown files
    all_md_files = list(root_dir.rglob("**/*.md"))
    total_errors = 0
    total_warnings = 0

    print(f"Checking markdown files in: {root_dir}")
    print(f"Found {len(all_md_files)} markdown files\n")

    # Run tree structure check
    tree_errors = check_tree_structure(root_dir)
    total_errors += len(tree_errors)
    for error in tree_errors:
        print(f"  [TREE] {error}")

    # Run markdown content checks
    for md_file in all_md_files:
        file_errors, file_warnings = check_markdown_file(md_file, sections)
        total_errors += len(file_errors)
        total_warnings += len(file_warnings)

        if file_errors or file_warnings:
            rel_path = md_file.relative_to(root_dir)
            print(f"\n{rel_path}:")
            for error in file_errors:
                print(f"  [ERROR] {error}")
            for warning in file_warnings:
                print(f"  [WARN]  {warning}")

    # Summary
    print(f"\n=== SUMMARY ===")
    print(f"Total errors: {total_errors}")
    print(f"Total warnings: {total_warnings}")

    # Exit code
    sys.exit(2 if total_errors > 0 else 0)


if __name__ == "__main__":
    main()
