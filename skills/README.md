# FPF Skills

This directory contains portable AI-agent skill packages for bounded use of the First Principles Framework:

- `fpf-applicability-scan.skill` identifies the smallest relevant set of FPF patterns for one question.
- `fpf-design-challenge.skill` challenges a proposed or not-yet-implemented design with bounded FPF evidence.
- `fpf-alignment-audit.skill` audits implemented or accepted work against relevant FPF patterns.

Each package contains its complete `SKILL.md` contract and `agents/openai.yaml` interface metadata. The skills discover an accessible FPF edition at runtime and do not assume this repository path, a specific operating system, or a particular workspace layout.
