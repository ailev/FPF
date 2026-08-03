# Levenchuk’s FPF Knowledge Graph Toolkit

An Obsidian-ready, LLM-friendly usability fork of the original [First Principles Framework (FPF)](https://github.com/ailev/FPF).

## About this fork and FPF

This repository does not redefine FPF or claim authority over it. The canonical source and its evolution remain in [ailev/FPF](https://github.com/ailev/FPF).

This build uses upstream FPF revision [`9a9a42e`](https://github.com/ailev/FPF/commit/9a9a42e4d154021ca3f7415e0009a4214832f65f), dated **2026-08-02**.

FPF was created by **Anatoly Levenchuk, with AI-agent assistance**. It is a pattern language for making difficult engineering, research, management, governance, and human/AI work explicit and reviewable. It separates entities from descriptions, evidence, decisions, plans, and performed work; scopes claims to their intended use; and identifies the direct patterns governing a question.

The normative content is not rewritten. A script generates smaller linked notes, hubs, indexes, and frontmatter from the upstream source; the monolithic source itself is not stored in this repository.

## Why this version

The current specification is roughly 12 MB. Loading it for every question consumes many LLM tokens and weakens retrieval focus. This fork provides:

- bounded LLM retrieval of relevant patterns, with lower context cost;
- Obsidian hubs, links, backlinks, folders, frontmatter, and graph navigation;
- Obsidian CLI access for scripts and agents to search or read individual notes;
- pattern, relation, and term indexes with source-line metadata;
- shared human/agent navigation, incremental Git diffs, and automatic link validation.

## Repository layout

- [`FPF-Spec/`](FPF-Spec/) — generated graph and validation output.
- [`scripts/build_fpf_obsidian_graph.py`](scripts/build_fpf_obsidian_graph.py) — generator.
- [`skills/`](skills/) — portable agent skills.

## Included skills

The skills discover FPF at runtime and assume no repository path, tool, operating system, or project layer.

| Skill | Use case | Result |
|---|---|---|
| [`fpf-applicability-scan`](skills/fpf-applicability-scan.skill/SKILL.md) | Decide whether FPF is useful and which patterns apply. | Smallest relevant set, basis, first result, use, and stop boundary. |
| [`fpf-design-challenge`](skills/fpf-design-challenge.skill/SKILL.md) | Challenge a proposal or not-yet-implemented decision. | Bounded finding with evidence and supported corrections. |
| [`fpf-alignment-audit`](skills/fpf-alignment-audit.skill/SKILL.md) | Check implemented or accepted work. | Per-claim semantic/mechanical audit with a bounded verdict. |

All are read-only by default. Findings do not approve designs, authorize work, provide assurance, or make gate decisions.

## Updating from upstream

Fetch or check out upstream `FPF-Spec.md` outside the active Obsidian vault, then pass its path explicitly to the generator.

Regenerate from the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/build_fpf_obsidian_graph.py --source /path/to/FPF-Spec.md --clean
```

Check the [`validation report`](FPF-Spec/00_Index/FPF%20-%20Validation%20Report.json) for zero broken links, then review the diff.

## Citation

Cite the original: `Levenchuk, Anatoly. First Principles Framework (FPF). https://github.com/ailev/FPF`
