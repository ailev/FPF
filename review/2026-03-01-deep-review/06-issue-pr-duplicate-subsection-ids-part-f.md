# Issue + PR: Duplicate Subsection IDs in Part F

## Problem
Duplicate subsection IDs create anchor collisions.

## Evidence
- `F.2:6.2` appears at lines 39192 and 39204.
- `F.18:21` appears at lines 45047 and 45077.

## Fix plan
- Renumber the second occurrence in each pair.
- Update any direct references if present.
