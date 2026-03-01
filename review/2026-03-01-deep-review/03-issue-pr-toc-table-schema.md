# Issue + PR: ToC/Table Schema Parser Breakage

## Problem
ToC/table markdown structure is parser-breaking.

## Evidence
- Missing row terminator: `FPF-Spec.md` line 61.
- Unescaped `|` in table cells: lines 94-99, 229, 279.

## Fix plan
- Close malformed row.
- Escape literal pipes in table cells.
- Keep content unchanged semantically.
