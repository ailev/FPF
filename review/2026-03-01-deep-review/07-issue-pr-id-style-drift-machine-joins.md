# Issue + PR: ID Style Drift Breaking Machine Joins

## Problem
Equivalent references use incompatible ID forms.

## Evidence
- `B.4.1` vs `B.4-1`: lines 127 and 24493.
- `G.5.Select` vs `G.5-3 Select`: lines 49623 and 47866.
- `G.6:H8` vs canonical `G.6:7.5.8`: lines 41158 and 48394.

## Fix plan
- Normalize tokens to canonical form in current spec.
- Preserve readability labels separately from machine IDs.
