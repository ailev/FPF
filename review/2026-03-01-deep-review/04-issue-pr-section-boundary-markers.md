# Issue + PR: Section Boundary Marker Corruption

## Problem
At least two section end markers point to wrong IDs.

## Evidence
- `C.25` closes as `C.23:End` at line 32109.
- `E.13` closes as `E.10:End` at line 35239.

## Fix plan
- Correct markers to `C.25:End` and `E.13:End`.
- Add a lightweight heading↔end consistency lint script.
