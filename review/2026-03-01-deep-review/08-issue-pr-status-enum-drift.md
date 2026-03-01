# Issue + PR: Status Enum Drift and Contradictions

## Problem
Status values and status assignments are inconsistent.

## Evidence
- `A.2.7` status mismatch: line 46 (`New`) vs line 4599 (`Stable`).
- enum case drift: line 228 (`stable`), line 315 (`stub`).

## Fix plan
- Normalize status vocabulary (`Stable`, `Draft`, `Stub`, etc.).
- Align ToC and section status for `A.2.7`.
