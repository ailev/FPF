---
name: fpf-alignment-audit
description: Audit implemented or accepted work against relevant First Principles Framework (FPF) patterns with bounded, replayable evidence. Locate and use an accessible FPF source without assuming its path, storage, operating system, tools, repository layout, or user setup. Use when the user asks for a final FPF review, whether decisions were applied, whether a target is FPF-aligned, whether contradictions, gaps, leftovers, dead routes, or regressions remain, or whether an implemented document, policy, workflow, model, system, or change set is coherent after revision.
---

# FPF Alignment Audit

Produce a read-only **Bounded Alignment Finding**. Do not turn an audit report into project assurance, authorization, or a gate decision.

## Resolve scope and sources

1. Resolve the implemented target, accepted claims, current authority, affected dependencies, and requested receiving use from the request and accessible context. Do not assume named layers, a repository layout, Git, a fixed artifact schema, or software-only evidence.
2. Resolve an accessible FPF edition in this order: a source named in the request; a path, URI, attachment, corpus, or connected item already in context; an optional environment or workspace hint; then a bounded search of accessible workspace or storage roots. Treat configuration hints as optional, never required.
3. Verify candidates by content, not container name. A usable source must identify itself as FPF and expose navigable direct patterns with the relevant Problem frame, Problem, Forces, Solution, and Consequences; practical-use cards, usage guidance, hubs, contents, and indexes are supporting landmarks.
4. Do not require a particular environment variable, directory or repository name, application, version-control system, home-directory layout, shell, local filesystem, or operating system. Use the discovery and retrieval capabilities available in the current runtime.
5. Search only accessible, task-relevant roots or providers; never scan an entire device, account, or network. If several editions remain plausible and the choice affects the finding, ask the user which is authoritative. If none can be verified, report what was checked and request a path, URI, attachment, corpus, or connected source.
6. Never load a monolithic or explicitly unsafe/oversized FPF source wholesale. Use split or indexed pages or targeted section retrieval. If the runtime can only load the entire oversized source, request another accessible representation. Keep the resolved source locator task-local; never persist a discovered user-specific location into this reusable skill.
7. If only an unimplemented proposal exists, stop and recommend `fpf-design-challenge` instead.

## Define the audit contract

Before reviewing, enumerate:

- project claims whose alignment is being tested;
- target carriers or observed states;
- authority and evidence available for each claim;
- affected dependencies, projections, interfaces, or receiving uses;
- explicit exclusions and acceptance/refusal conditions.

Do not silently turn “review everything” into an unbounded repository or methodology read. State the chosen boundary and why it is sufficient or insufficient.

## Audit workflow

1. Route each claim from the relevant practical-use card to its direct governing FPF pattern. Inspect the pattern's Problem frame, Problem, Forces, Solution, Consequences, and ordinary boundary.
2. Use six direct-pattern pages as the default retrieval budget. Entry pages and index searches do not count. A budget exhaustion produces `insufficient basis`, never a semantic pass; name the exact additional pages or project evidence needed.
3. Inspect the implemented target and only the dependencies or projections required by the enumerated claims. Mark every unavailable or uninspected dependency explicitly.
4. Separate semantic findings from structural or mechanical verification. Parsing, link resolution, tests, or clean diffs do not by themselves prove semantic alignment.
5. Apply only claim-relevant lenses. These may include identity and revision meaning, evidence versus provenance, lifecycle transitions, authority, compatibility, projection faithfulness, unresolved blockers, or recursive impact. Do not run them as a universal layer checklist.
6. Stop at the smallest bounded finding supported by recoverable FPF and project evidence. Return when the claim, context, source edition, evidence, implementation state, governing pattern, or receiving use changes.

## Subagent lifecycle

If the review delegates a bounded evidence or reviewer lane, retrieval, wait, elapsed-time, token, credit, cost, context, and turn budgets limit only review scope, root-side polling, and new work. They never authorize `interrupt_agent`, cancellation, replacement, or duplicate execution of a running subagent. After allowed waits are exhausted, leave it running, continue only non-conflicting work, and consume its result when delivered. Report `still running; polling ended`, never that the lane was stopped. Interrupt only for explicit user cancellation or override, or a confirmed safety or protected-scope violation.

## Per-claim replay record

For every audited claim, record:

- claim and Entity of Concern;
- bounded context and receiving use;
- implemented carrier or observed state;
- direct FPF pattern, source edition, stable locator, and inspected Solution;
- project evidence and source status;
- expected and observed result;
- semantic and mechanical findings, kept separate;
- reviewer inference, explicitly labeled;
- inspected and uninspected dependencies;
- stop/return condition and exact next source when needed.

Use stable citations appropriate to the source, such as file-and-line, URI-and-section, attachment, corpus, or connected-item locators. A citation is a pointer, not a substitute for the replay record.

## Verdict states

Use only:

- `boundedly supported` — all enumerated claims have recoverable FPF and project evidence, and no semantic blocker was found within the stated scope;
- `unsupported` — a checked claim conflicts with its governing basis or the observed target;
- `insufficient basis` — required FPF source, project authority, evidence, dependency, or observation is missing or non-recoverable.

Never upgrade an unchecked claim through reviewer consensus. Reviewers using one evidence packet are reasoning-independent, not retrieval-independent; include coverage dissent and exact source requests when relevant.

## Authority and layer boundaries

- Return assurance, gate, release, authorization, or acceptance claims to their direct project governor.
- Distinguish direct FPF claims, project evidence, mechanical verification, reviewer inference, and operator decisions.
- Remain layer-agnostic: discover the requested scope at runtime and audit a single layer, several layers, or a layerless target by the same contract.
- Remain read-only unless the user separately authorizes corrections.

## Output

Return:

1. **Audit contract, resolved FPF source, and inspected scope**
2. **Per-claim alignment matrix**
3. **Semantic blockers**
4. **Structural or mechanical failures**
5. **Residual gaps and optional improvements**
6. **Excluded or uninspected claims**
7. **Bounded verdict and stop/return condition**

Do not use an unqualified “FPF-aligned,” “all good,” or “passed” verdict.
