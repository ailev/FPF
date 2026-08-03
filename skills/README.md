# FPF Skills

This directory contains portable AI-agent skill packages for bounded use of the First Principles Framework.

Review and applicability:

- `fpf-applicability-scan.skill` identifies the smallest relevant set of FPF patterns for one question.
- `fpf-design-challenge.skill` challenges a proposed or not-yet-implemented design with bounded FPF evidence.
- `fpf-alignment-audit.skill` audits implemented or accepted work against relevant FPF patterns.

Generative and operational use:

- `fpf-options-explore.skill` generates diverse NQD-guided candidates and optionally compares method families through a pinned parity contract.
- `fpf-sota-harvest.skill` builds a reconstructible, plural SoTA synthesis pack without silently fusing rival traditions.
- `fpf-decision-synthesize.skill` records a recoverable project decision after candidate synthesis, then projects it into an audience-specific ADR.
- `fpf-quality-improve.skill` runs a bounded improvement loop that requires both a target-version change and demonstrated result change in declared quality coordinates.

Each package contains its complete `SKILL.md` contract and `agents/openai.yaml` interface metadata. The skills discover an accessible FPF edition at runtime and do not assume this repository path, a specific operating system, or a particular workspace layout.
