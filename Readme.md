# FPF Obsidianized

An Obsidian-ready and LLM-friendly presentation of the original [First Principles Framework (FPF)](https://github.com/ailev/FPF).

## What this repository is

This repository is only a usability and presentation fork of the original FPF. It does not redefine FPF, publish a competing methodology, or claim authority over its content. The canonical source, its meaning, and its evolution remain in [ailev/FPF](https://github.com/ailev/FPF).

FPF was created by **Anatoly Levenchuk, with AI-agent assistance**. It is a standards-style pattern language for making difficult engineering, research, management, governance, and mixed human/AI work explicit, reviewable, and improvable. Among other things, it helps distinguish the entity being discussed from its descriptions, evidence, decisions, plans, and performed work; keep claims scoped to their context and intended use; and recover the direct patterns governing a current question.

The normative FPF text is not rewritten in this fork. The upstream monolithic source is preserved byte-for-byte under a deliberately Obsidian-hidden filename, while scripts generate a navigable projection made of smaller Markdown notes, hubs, indexes, links, and frontmatter.

## Why an Obsidian-ready version

The current FPF specification is a multi-megabyte Markdown document—roughly 12 MB in the current edition. Loading the whole file for every question is inconvenient for people and costly for LLM context: it consumes many tokens, makes retrieval less selective, and forces each tool to rediscover the document structure.

This fork makes the same content easier to use:

- **Bounded LLM retrieval:** load the relevant pattern pages and their neighbors instead of repeatedly loading the entire specification.
- **Lower context cost:** spend tokens on the current question and direct evidence rather than unrelated parts of the corpus.
- **Obsidian navigation:** browse hubs, wiki-links, backlinks, folders, frontmatter, and the local graph.
- **Obsidian CLI access:** search for and read individual generated notes from scripts, agents, and terminal workflows without opening the monolith.
- **Searchable indexes:** use generated pattern, relation, and term indexes to locate direct sources quickly.
- **Recoverable citations:** generated notes retain source-line metadata and the original source filename.
- **Incremental review:** Git shows which generated pages changed after an upstream update instead of presenting one opaque giant-file diff.
- **Shared human/agent structure:** people and LLMs can navigate the same stable page and hub layout.
- **Automatic checks:** every rebuild produces a validation report covering page counts, unresolved source relations, and broken wiki-links.

## Repository layout

- [`FPF-Spec-original/FPF-Spec.md.breaks.my.obsidian.bak`](FPF-Spec-original/FPF-Spec.md.breaks.my.obsidian.bak) — the untouched upstream monolithic source under a filename Obsidian will not treat as a normal Markdown note.
- [`FPF-Spec/`](FPF-Spec/) — the generated Obsidian graph: direct pages, hubs, indexes, links, and validation output.
- [`scripts/build_fpf_obsidian_graph.py`](scripts/build_fpf_obsidian_graph.py) — the deterministic generator.
- [`skills/`](skills/) — portable FPF review skills for AI agents.
- [`FPF-Spec/00_Index/FPF - Validation Report.json`](FPF-Spec/00_Index/FPF%20-%20Validation%20Report.json) — the current mechanical build report.

## Included FPF skills

The skills use a bounded set of direct FPF patterns and discover an accessible FPF edition at runtime. They do not assume this repository path, Obsidian, Git, a particular operating system, or a project layer.

| Skill | Use it when | What it returns |
|---|---|---|
| [`fpf-applicability-scan`](skills/fpf-applicability-scan.skill/SKILL.md) | You have one question and want to know whether FPF is useful or which patterns apply. | The smallest relevant pattern set, its applicability basis, expected first useful result, receiving use, and stop/return boundary. |
| [`fpf-design-challenge`](skills/fpf-design-challenge.skill/SKILL.md) | You have a proposal, design, taxonomy, policy, workflow, model, or decision that has not yet been treated as implemented authority. | A bounded challenge finding: a concern, no concern found within scope, FPF not decisive, or insufficient basis—plus evidence and possible corrections where supported. |
| [`fpf-alignment-audit`](skills/fpf-alignment-audit.skill/SKILL.md) | Work has been implemented or accepted and you want to check whether the intended FPF distinctions actually landed. | A replayable per-claim audit separating semantic findings from mechanical checks, with a boundedly supported, unsupported, or insufficient-basis verdict. |

All three skills are read-only by default. They keep FPF evidence separate from project authority: an FPF finding does not approve a design, authorize work, provide assurance, or make a gate decision.

## Using the graph with an LLM

Start from the practical-use pages, hubs, or indexes under [`FPF-Spec/`](FPF-Spec/), then retrieve only the direct patterns relevant to the current question. For repeatable review contracts, invoke one of the bundled skills instead of asking an agent to read and summarize the entire source.

A useful request is:

```text
Use the FPF Obsidian graph and inspect only the direct patterns needed for this question:
[your bounded project question]

Separate direct FPF claims, project evidence, reviewer inference, and project decisions.
```

## Updating from upstream

The large upstream `FPF-Spec.md` must not appear at the root of a checkout linked into an active Obsidian vault. Fetch and merge upstream in a temporary worktree, preserve the resulting source as `FPF-Spec-original/FPF-Spec.md.breaks.my.obsidian.bak`, and verify that its Git blob matches upstream before updating the vault-visible checkout.

Regenerate the Obsidian graph from the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/build_fpf_obsidian_graph.py --clean
```

Then inspect [`FPF-Spec/00_Index/FPF - Validation Report.json`](FPF-Spec/00_Index/FPF%20-%20Validation%20Report.json), confirm that `broken_links_count` is zero, and review the Git diff before committing the generated projection.

## Canonical source and citation

- Original repository: [github.com/ailev/FPF](https://github.com/ailev/FPF)
- Original author: Anatoly Levenchuk, with AI-agent assistance

When citing FPF, cite the original project rather than this usability fork:

```text
Levenchuk, Anatoly. First Principles Framework (FPF).
GitHub repository: https://github.com/ailev/FPF
```
