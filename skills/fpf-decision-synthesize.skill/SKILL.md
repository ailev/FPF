---
name: fpf-decision-synthesize
description: Turn evaluated alternatives into a recoverable project decision and an audience-appropriate ADR projection using bounded First Principles Framework (FPF) evidence without reading the full methodology. Locate FPF without assuming the user's storage, tools, operating system, repository layout, or setup. Use when the user asks to choose among evaluated options, document accepted losses and reopen triggers, create an ADR or trade-study record, or separate a decision from its publication and implementation.
---

# FPF Decision Synthesize

Produce a **Decision Package** in two ordered stages: the project decision relation, then its ADR-like publication projection. Do not let the record impersonate the decision or its authority.

## Resolve scope and FPF source

1. Resolve the decision question, Entity of Concern, evaluated candidates, decision owner, authority, evidence, criteria, constraints, affected structures, receiving work, and publication audience.
2. Resolve an accessible FPF edition from a user-supplied path, URI, attachment, corpus, connected item, optional runtime hint, or bounded search of accessible task-relevant roots. Verify candidates by FPF identity and navigable direct patterns, not container names.
3. Locate `Project Architecture Decision After Candidate Synthesis` and `Architecture Decision Record Projection` by title and content. Inspect each pattern's Problem frame, Problem, Forces, Solution, Consequences, and ordinary boundary.
4. Never load the full methodology or an oversized source wholesale. Use entry/index pages and targeted sections. Use six direct-pattern pages as the default ceiling; entry and index pages do not count.
5. Keep the source locator task-local and cite stable source/evidence locators. If candidate synthesis, comparison evidence, or project authority is missing, return `insufficient basis` and the exact prerequisite; never invent a decision.

## Stage 1: decision relation

1. Confirm that alternatives are materially distinct and recoverably evaluated. Route missing option generation or parity work to `fpf-options-explore`.
2. Record the selected configuration only when the project decision owner or authoritative evidence supplies the selection.
3. Record the decision question, considered options, governing criteria, evidence, rationale, accepted losses, affected structures, method/work consequences, dependencies, confirmation path, and explicit reopen trigger.
4. If selection is not yet authorized, produce a **Decision-Ready Proposal** and identify the remaining owner action; do not label it decided.

## Stage 2: ADR projection

1. Project the recoverable decision relation for the named audience and receiving use.
2. Include question, context, options, outcome, rationale, accepted trade-offs, consequences, confirmation path, source links, status, and supersession condition.
3. Preserve traceability back to the decision relation and evaluated candidates. Tailor presentation without changing decision meaning.

## Boundaries

- An ADR file is not the decision, architecture, candidate comparison, authority act, or implementation.
- Do not convert an FPF recommendation into project approval or claim that FPF selected the option.
- Do not create a false consensus when evidence or authority remains contested.
- Remain layer-agnostic and artifact-agnostic. Write or modify project records only when the user authorizes it.

## Subagent lifecycle

If this workflow delegates a bounded evidence, decision-analysis, or publication lane, retrieval, wait, elapsed-time, token, credit, cost, context, and turn budgets limit only scope, root-side polling, and new work. They never authorize `interrupt_agent`, cancellation, replacement, or duplicate execution of a running subagent. After allowed waits are exhausted, leave it running, continue only non-conflicting work, and consume its result when delivered. Report `still running; polling ended`, never that the lane was stopped. Interrupt only for explicit user cancellation or override, or a confirmed safety or protected-scope violation.

## Output

Return:

1. **Decision contract, authority, and resolved FPF source**
2. **Candidate and evidence readiness**
3. **Decision relation or Decision-Ready Proposal**
4. **ADR projection**, only when its source relation is recoverable
5. **Accepted losses, consequences, and reopen triggers**
6. **Unresolved authority/evidence and implementation handoff**

