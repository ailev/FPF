# Issue Only (No Fix Yet): B.4 Subsections + Section-8 Systemic Template Drift

## Problem A
`B.4.1/B.4.2/B.4.3` are marked Stable in ToC but not implemented as canonical `##` sections.

### Evidence
- ToC: lines 127-129.
- Body has `B.4-1/2/3` bullets only: lines 24493, 24501, 24509.

## Problem B
Canonical section-8 template requirement is violated systemically.

### Evidence
- Requirement: line 33305.
- Violations sample: lines 5422, 21060, 24007, 24798.

## Requested handling
Track as separate issue for design decision first; no direct patch in this wave.
