---
name: fpf-applicability-scan
description: Identify which First Principles Framework (FPF) patterns are relevant to one bounded question without reading the full methodology. Locate and use an accessible FPF source without assuming its path, storage, operating system, tools, repository layout, or user setup. Use when the user asks what FPF can contribute, which FPF ideas or patterns fit, what to borrow from FPF, or whether FPF is applicable to a proposal, document, policy, workflow, model, system, or other target.
---

# FPF Applicability Scan

Produce a read-only **Pattern Applicability Finding**. Stop at a bounded recommendation; do not redesign the target or authorize changes.

## Resolve sources

1. Resolve the target and its current authority from the user request and accessible context. Do not assume a repository, Git, an artifact schema, or named layers.
2. Resolve an accessible FPF edition in this order: a source named in the request; a path, URI, attachment, corpus, or connected item already in context; an optional environment or workspace hint; then a bounded search of accessible workspace or storage roots. Treat configuration hints as optional, never required.
3. Verify candidates by content, not container name. A usable source must identify itself as FPF and expose navigable direct patterns with the relevant Problem frame, Problem, Forces, Solution, and Consequences; practical-use cards, usage guidance, hubs, contents, and indexes are supporting landmarks.
4. Do not require a particular environment variable, directory or repository name, application, version-control system, home-directory layout, shell, local filesystem, or operating system. Use the discovery and retrieval capabilities available in the current runtime.
5. Search only accessible, task-relevant roots or providers; never scan an entire device, account, or network. If several editions remain plausible and the choice affects the finding, ask the user which is authoritative. If none can be verified, report what was checked and request a path, URI, attachment, corpus, or connected source.
6. Never load a monolithic or explicitly unsafe/oversized FPF source wholesale. Use split or indexed pages or targeted section retrieval. If the runtime can only load the entire oversized source, request another accessible representation. Keep the resolved source locator task-local; never persist a discovered user-specific location into this reusable skill.

## Scan workflow

1. State the current question, Entity of Concern, bounded context, and receiving use.
2. Route from the resolved edition's Practical-Use Cards entry point or its equivalent. Use its usage guide, table of contents, hubs, and term/relation indexes only to locate direct patterns.
3. Compare plausible cards by situation, exact first-result difference, and stop/return conditions. A card or pattern-family name alone is not a finding.
4. Inspect each selected direct pattern's Problem frame, Problem, Forces, Solution, Consequences, and ordinary boundary.
5. Use six direct-pattern pages as the default retrieval budget. Entry pages and index searches do not count. If the budget cannot support a claim, return `insufficient basis` and name the exact additional pages or project evidence needed; do not broaden silently.
6. Recommend only the smallest useful set of direct patterns. Do not create an ordered whole-project FPF program unless the receiving use requires one.

## Subagent lifecycle

If the review delegates a bounded evidence or reviewer lane, retrieval, wait, elapsed-time, token, credit, cost, context, and turn budgets limit only review scope, root-side polling, and new work. They never authorize `interrupt_agent`, cancellation, replacement, or duplicate execution of a running subagent. After allowed waits are exhausted, leave it running, continue only non-conflicting work, and consume its result when delivered. Report `still running; polling ended`, never that the lane was stopped. Interrupt only for explicit user cancellation or override, or a confirmed safety or protected-scope violation.

## Per-candidate record

For every candidate, record:

- project question and target claim;
- Entity of Concern and bounded context;
- selected practical-use card;
- direct pattern, source edition, stable locator, and inspected Solution;
- expected first useful result and receiving use;
- project evidence and direct FPF basis;
- reviewer inference, if any;
- applicability: `applicable`, `not applicable`, or `insufficient basis`;
- stop/return condition and exact next source when applicable.

Use stable citations appropriate to the source, such as file-and-line, URI-and-section, attachment, corpus, or connected-item locators. A citation is a pointer, not a substitute for the applicability record.

## Boundaries

- Keep FPF recommendation separate from project authority and operator decisions.
- Label direct FPF claims, project evidence, reviewer inference, and operator decisions distinctly.
- Apply only lenses selected by the current question; do not run ontological, assurance, lifecycle, or other checks as universal rituals.
- Remain layer-agnostic: discover the requested scope at runtime and treat a named layer, several layers, or a layerless target identically.
- Remain read-only unless the user separately authorizes implementation.

## Output

Return:

1. **Question, scope, and resolved FPF source**
2. **Pattern Applicability Findings**
3. **Recommended smallest set**
4. **Excluded or unchecked claims**
5. **Stop/return condition**

Do not claim that FPF made, approved, or authorized a project decision.
