# Future Work / Roadmap Issue

## Topic
Planned-but-not-yet-written section IDs are referenced in the spec for forward-compatible reasoning support.

## Intent
Keep references, but mark them explicitly as roadmap placeholders to avoid false conformance expectations.

## Missing section IDs (sample)
- `A.22`..`A.45` family references (including `A.27`) used by A.20/A.21/E.18 and G.* surfaces.
- `C.1`, `C.4`..`C.7`, `C.9`..`C.12`, `C.14`, `C.15` listed/used but not fully implemented as `##` sections.
- `D.1`..`D.4.2`, `D.5.1`, `D.5.2` listed but not implemented as full sections.

## Evidence
- `FPF-Spec.md` lines: 100, 101, 155-168, 186-200, 20531, 20917, 30107, 30759, 31202, 31923, 32239, 32396, 37476, 37562, 37744, 48869, 49714, 50862.

## Proposed handling
- Add explicit roadmap marker policy in spec (e.g., `PlannedPlaceholder: yes`).
- Keep IDs for LLM context, but remove normative dependency semantics unless section body exists.
- Optionally add minimal `##` placeholder sections with status `Planned` and explicit non-normative disclaimer.
