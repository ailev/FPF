---
name: fpf-options-explore
description: Generate and compare diverse candidate options with bounded First Principles Framework (FPF) evidence without reading the full methodology. Locate FPF without assuming the user's storage, tools, operating system, repository layout, or setup. Use when the user asks for non-obvious or interesting solutions, NQD exploration, OEE/QD parity, alternative generation before a decision or ADR, or comparison of method families without prematurely selecting one winner.
---

# FPF Options Explore

Produce a read-only **Candidate Exploration Pack**. Generate and compare options; do not make the receiving project decision.

## Resolve scope and FPF source

1. Resolve the question, Entity of Concern, bounded context, receiving use, evaluator, and decision owner from the request and accessible evidence.
2. Resolve an accessible FPF edition from a user-supplied path, URI, attachment, corpus, connected item, optional runtime hint, or bounded search of accessible task-relevant roots. Verify candidates by FPF identity and navigable direct patterns, not container names.
3. Locate direct patterns by title and content. Inspect `Creative Abduction with NQD`; inspect `Parity and Benchmark Harness` only when method-family or OEE/QD comparison is required. Read their Problem frame, Problem, Forces, Solution, Consequences, and ordinary boundary.
4. Never load the full methodology or an oversized source wholesale. Use entry/index pages and targeted sections. Use six direct-pattern pages as the default ceiling; entry and index pages do not count.
5. Keep the source locator task-local. Cite it with the most stable available file, URI, attachment, corpus, or connected-item locator. If no edition can be verified, return `insufficient basis` and state what source is required.

## Define the exploration contract

Before generating options, record:

- the question, scope, baseline, and receiving use;
- what counts as interesting, for whom, and relative to which familiar options;
- declared quality measures and protected constraints;
- novelty and diversity axes, admissible risk, cost, reversibility, and time horizon;
- evidence inputs, exploration budget, policy pins, and stop criteria.

If “interesting” remains undefined, ask for the missing distinctions or return `insufficient basis`; do not substitute an internet-average preference.

## Workflow

1. Generate a provenance-bearing `CandidateSet` using NQD-guided creative abduction. Keep hypotheses explicitly abductive.
2. Evaluate candidates only in the declared quality coordinates. Preserve useful diversity, archive state, and the applicable decision/reasoning record.
3. Treat novelty, diversity, illumination, coverage, and regret as telemetry unless the exploration contract explicitly promotes one into a decision criterion.
4. When comparison is requested, pin the baseline, comparator edition, freshness window, normalization or bridge rules, and policy. Produce `ParityPlan@Context` before `ParityReport@Context`.
5. Return the candidate set, Pareto front when justified, retained alternatives, evidence gaps, and handoff requirements. Do not silently collapse several measures into one opaque score.

## Boundaries

- Do not claim that a novel candidate is superior, selected, approved, or implementable.
- Do not manufacture diversity through cosmetic wording; distinguish candidates by declared mechanisms, structures, or trade-offs.
- Route an actual selection and ADR request to `fpf-decision-synthesize` after candidates have recoverable evaluation evidence.
- Remain layer-agnostic and artifact-agnostic. Remain read-only unless the user separately authorizes implementation or file writes.

## Subagent lifecycle

If this workflow delegates a bounded evidence or exploration lane, retrieval, wait, elapsed-time, token, credit, cost, context, and turn budgets limit only scope, root-side polling, and new work. They never authorize `interrupt_agent`, cancellation, replacement, or duplicate execution of a running subagent. After allowed waits are exhausted, leave it running, continue only non-conflicting work, and consume its result when delivered. Report `still running; polling ended`, never that the lane was stopped. Interrupt only for explicit user cancellation or override, or a confirmed safety or protected-scope violation.

## Output

Return:

1. **Exploration contract and resolved FPF source**
2. **CandidateSet and provenance**
3. **Declared-coordinate evaluation and diversity map**
4. **Parity plan/report**, when applicable
5. **Retained options, exclusions, and evidence gaps**
6. **Stop condition and decision handoff**

