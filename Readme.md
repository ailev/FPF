# First Principles Framework (FPF) - Core Conceptual Specification

> First Principles Framework (FPF) is a standards-style pattern language for turning difficult engineering, research, management, and mixed human/AI work into explicit, reviewable, improvable reasoning.

- **Author:** Anatoly Levenchuk, with AI-agent assistance
- **Version:** June 2026
- **Status:** Normative kernel, eternal alpha: already used in working projects and development programs, while still evolving.

FPF helps when a project has outgrown one clever conversation. It is useful when meanings, claims, options, evidence, architecture, work decisions, publication forms, and improvement criteria must stay coherent across people, teams, tools, time, or AI agents.

Use FPF as a reference model and pattern language, not as a linear textbook. Start from the working question you bring from your project. Bring in internal FPF terms only after they help you keep the work precise.

This readme is a thin first-entry rendering of FPF for engineers, researchers, managers, reviewers, and AI-assisted project workers deciding where FPF can help. It foregrounds the project questions most likely to pay off first and deliberately coarsens, omits, or defers the full pattern language, source history, and relation structure. When a claim becomes important, return to the Preface, Table of Content, and governing pattern body rather than treating this readme as the specification.

The plain starting move is: name the project thing at stake. FPF often calls it a holon when the thing is being treated as a whole with parts: a machine, product, organization, method, body of knowledge, publication system, AI-agent arrangement, or local framework. Once the thing is named, FPF asks what structure, claim, decision, evidence, description, work, or improvement question is actually live.

## Decide Whether FPF Fits

Use FPF when ordinary discussion is no longer enough to keep work coherent. Typical signs:

- several teams, experts, tools, or AI agents must reason about the same work;
- the real-world test is slow, expensive, noisy, risky, or politically hard to repeat;
- different readers need different reports, dashboards, explanations, or decisions about the same underlying work;
- names, roles, responsibilities, options, evidence, or quality criteria are starting to blur;
- the team needs a current view of possible approaches, not just one recommendation;
- a decision is small enough to make now but important enough to leave a durable reason.

FPF is probably too heavy when the task is small, feedback is fast and cheap, the vocabulary is already stable, the decision will not be reused or audited, and a quick answer is enough.

FPF is mainly useful for people who have to keep difficult work understandable across boundaries:

- engineers and systems engineers working with complex products or operations;
- researchers building claims that others must inspect or reuse;
- platform and AI teams coordinating humans, models, tools, and approvals;
- safety, assurance, compliance, and regulatory leads who need visible evidence and responsibility boundaries;
- managers and product leaders who must compare options, budgets, risks, and delivery promises without hiding trade-offs.

There are three common ways to use FPF:

1. Human-only: use it as a writing and review discipline for meetings, notes, decisions, and technical documents.
2. Mixed team: use it to keep specialists, managers, safety leads, and AI assistants aligned around the same work.
3. AI-assisted: attach or index the specification, ask for plain-language project help first, and use pattern names only when they make the answer easier to check.

Stronger AI does not remove the need for FPF. AI can generate fluent options quickly, but projects still need to decide what counts as evidence, which option is being compared, who may rely on an answer, when a claim is stale, what remains only a guess, and what work is actually authorized. FPF helps make those boundaries explicit before a confident answer becomes an expensive mistake.

Core ideas in plain language:

- first name the project thing under concern; when it is treated as a whole with parts, FPF calls it a holon;
- local teams may use local meanings, but translation must be explicit when work crosses a boundary;
- the thing itself, its description, a dashboard about it, a decision about it, and the work done to change it are not the same;
- architecture is structure of that thing in a context, not the diagram, document, approval, or plan about it;
- serious architecture work can move from problem pressure to candidate structures, selected structures, decisions, method and work, actual structures, and feedback;
- keep several options alive until the comparison is clear enough to choose;
- say what "better" means before optimizing or scoring;
- make trust depend on evidence, freshness, scope, and intended use;
- publish different views for different readers without changing the underlying claim;
- when source structure must become an explanation, route, or narrative for a reader, state what structure is preserved, deliberately coarsened, abstracted, omitted, or lost, and where source return happens;
- use mathematics or formal models when they clarify what structure is preserved, what is lost, and what can be checked;
- build domain or local FPF-grounded frameworks as dependents of FPF Core, not as silent rewrites of the Core.

## First Practical Entries

A first practical entry is the first useful way to enter FPF from a real working project. Choose it by the project question you are trying to settle, not by the order of patterns in the specification.

The entries below are not a required sequence. They are common places where FPF can start paying rent in a project.

### 1. Develop or review architecture

Use this when you need to design, explain, review, or improve the architecture of a product, organization, technical system, document system, AI-agent setup, research program, local practice, or other thing with important internal structure.

FPF helps you start from the thing being changed or described, not from the drawing. It asks which structures are unknown, candidate, selected, expected, or actual; which architecture characteristics are under pressure; which alternatives must remain alive; which decision is now binding; which method or work will realize the selected structures; and what operation, measurement, or feedback can reopen the architecture.

Typical first result: a short P2S flow card or architecture question note that names the described holon, bounded context, problem pressure, unknown or selected structures, architecture characteristics, candidate or decision owner, work or feedback owner, and what real selected structure is still not settled by the current architecture statement.

First inspect: `C.32.P2S`, `C.30`, `A.22`, `C.32`, `C.32.PAD`, `C.32.ADR`, `C.33`, `C.34`, `C.35`, `C.30.ASV`, `C.30.AD`, `C.31`, `C.32.CONWAY`, and `B.2` or `B.2.P` when the work may reidentify the whole being discussed.

### 2. Write rules, methods, and work-process documents

Use this when you need to write or review technical regulations, procedures, method descriptions, operating instructions, work-process descriptions, standards-like project documents, API documents, contracts, SLAs, protocols, permissions, or compliance wording.

FPF helps you keep the described method separate from the method itself, a plan separate from performed work, responsibility separate from permission, an interface contract separate from implementation, and a published document separate from actual execution. It can also describe chains of methods when the chain itself is the subject, while keeping actual work occurrences separate from the document that says how work should be done.

Typical first result: a cleaned method, regulation, or interface outline that names what is being governed, the method or interface being described, the roles and responsibilities involved, the expected work result, and any evidence, gate, permission, or compliance claim that the document does not yet justify.

First inspect: `A.6`, `A.6.B`, `A.6.C`, `A.15`, `A.15.1`, `A.15.2`, `A.15.3`, `A.15.4`, `E.18`, `E.18.1`, `E.8`, and `E.19`.

### 3. Compare alternatives and make a local choice

Use this when a team needs to compare technologies, vendors, designs, policies, research paths, implementation options, or architecture moves without jumping to one favorite too early.

FPF helps you state what is being compared, which characteristics matter, which candidates are still in play, what evidence is missing, when a local choice is justified, and how to publish a selected set without hiding the comparison logic.

Typical first result: a comparison note with declared characteristics, candidate set, evidence gaps, the present scope of the choice, and what a selected-set publication may and may not be used to decide.

First inspect: `A.19`, `A.19.ECS`, `C.11`, `C.18`, `C.19`, `G.0`, and `G.5`.

### 4. Turn a vague situation into a usable problem statement

Use this when a project has complaints, opportunities, risks, anomalies, or strategic pressure, but no clear problem yet.

FPF helps you preserve partly formed concerns without pretending they are already requirements, decisions, causes, evidence, or work items. It can turn a vague situation into a problem card or problem portfolio that later work can use without erasing uncertainty.

Typical first result: a problem card, problem portfolio, or problem note that records what has been accepted, what remains only a cue, which context is involved, and which first pattern family can use the problem statement.

First inspect: `C.22.2`, `C.2.2a`, `A.16`, `A.16.1`, `A.16.2`, `B.4.1`, and `B.5.2.0`.

### 5. Define what "better" means and run improvement

Use this when you need to improve a product, process, architecture, document, pattern, regulation, research program, or organization, but the improvement criteria are vague or competing.

FPF helps you define characteristics for evaluation, evaluate what is being improved, generate a portfolio of improvement proposals, choose changes that really improve the situation, and repeat the cycle without reducing quality to one score.

Typical first result: a quality-and-improvement note with evaluation characteristics, one evaluation of the object under improvement, a portfolio of proposed changes, and a condition for stopping or reopening the cycle.

First inspect: `A.19.ECS`, `E.22`, `E.23`, `C.16`, `C.25`, `E.21`, `E.9.DA`, and `E.2.DA` when the object is an FPF artifact.

### 6. Prepare evidence, assurance, or gate decisions before commitment

Use this when a project cannot responsibly act yet because evidence, assurance, constraints, gate validity, or decision permission is unclear.

FPF helps you separate what is being claimed from the evidence path, assurance argument, internal constraint validity, gate decision, local choice, and performed work. That separation matters when the cost of acting too early is high.

Typical first result: a commitment-readiness note that lists the claim, the evidence or assurance still needed, the gate or decision condition, and the work that remains blocked until those checks exist.

First inspect: `A.10`, `B.3`, `A.20`, `A.21`, `C.11`, `C.28`, and the relevant work or architecture pattern if the claim is about planned or performed work.

### 7. Check timing, freshness, rhythm, and action windows

Use this when a project depends on timing: freshness, latency, rate, cadence, action window, synchronization, inertia, aging, or rhythm.

FPF helps you separate timing information from evidence, permission, work completion, or vague urgency. It can say what timestamp, interval, cadence, freshness limit, action window, or rhythm claim is being used, and when that claim is no longer current enough for action.

Typical first result: a timing note that names what the timing is about, the relevant time relation or rhythm, the freshness or action-window limit, and the action that remains blocked when the timing claim is stale or underspecified.

First inspect: `C.27`, `A.10`, `A.20`, `A.21`, `C.11`, and the pattern that governs the thing whose timing matters.

### 8. Use causal explanations, interventions, responsibility, and model outputs safely

Use this when a project says that one thing causes another, a model output justifies an action, a change will produce an effect, or a role is responsible for an outcome.

FPF helps you separate causal use, counterfactual use, intervention claims, responsibility claims, model-output reliance, evidence, and decisions. It keeps a plausible explanation, prediction, or dashboard output from becoming permission to act.

Typical first result: a causal-use or model-output-use note that names the claim, the intervention or counterfactual being considered, the evidence or validation still needed, the responsibility limit, and the decision or work that remains blocked.

First inspect: `C.28`, `A.10`, `B.3`, `A.20`, `A.21`, `C.11`, and the domain pattern that governs the affected thing.

### 9. Compare descriptions, dashboards, explanations, and views of the same thing

Use this when a project has several descriptions, dashboards, explanations, renderings, model slices, or views and needs to know whether they are about the same thing, serve the same concern, or can be relied on in the same way.

FPF helps you keep the thing being described separate from its description, publication form, rendering, viewpoint, and same-thing claim. It can keep a diagram, dashboard, generated explanation, or view from silently becoming the thing itself, evidence, assurance, or decision.

Typical first result: a description-use note that names what is being described, which description or view is being used, how it is published or rendered, whether the same thing is really being addressed, and what the publication may and may not be used to claim.

First inspect: `E.17`, `E.17.0`, `E.17.EFP`, `A.15.4`, `A.7`, `C.30.AD`, and the pattern that governs the described thing.

### 10. Give things better names

Use this when project terms are misleading, overloaded, politically convenient, too broad, too local, or hard to translate between teams.

FPF helps you name products, roles, work processes, architecture elements, standards, document types, claims, characteristics, and project objects without treating a catchy label as ontology.

Typical first result: a naming card or term sheet that says what is being named, which local contexts use the name, which candidate names were rejected, which plain and technical names are allowed, and which alternate names are risky.

First inspect: `F.17`, `F.18`, `F.19`, `E.10`, `E.10.ARCH`, and the subject pattern that governs the thing being named.

### 11. Repair wording in technical documents before it changes action

Use this when standards, specifications, contracts, policies, dashboards, model cards, explanations, or working documents use words that may quietly change what can be claimed or done.

FPF helps you repair wording by first recovering the ontology: what thing, relation, value, evidence path, publication use, gate, decision, work, or architecture claim is actually being made. The repair is not word-policing; it succeeds only when the repaired text still tells someone what can now be used, checked, or named, or which related pattern to apply.

Typical first result: a repaired paragraph, claim register, term sheet row, or non-use decision that says what the text may now be used for and what claim or action remains blocked.

First inspect: `E.10`, `E.10.ARCH`, `F.18`, `F.19`, `A.6.P`, `C.2.P`, `C.16.P`, `C.16.Q`, `C.30.P`, `A.6.F`, and `A.6.M`.

### 12. Decide whether mathematics or formal modeling would help

Use this when intuition is not enough and a mathematical model, formal declaration, invariant, or explicit structure could make the work easier to review, compare, or improve.

FPF helps with two opposite mistakes: missing useful mathematics, and using mathematics without saying what structure it preserves and what it loses. It keeps mathematical-lens use, formal declarations of the assumed substrate, mechanism import or realization, and first-principles-to-work carry-through as different claims that may need different patterns.

Typical first result: a short modeling note that names what is being modeled, the candidate mathematical lens, any formal declaration that is needed, preserved and lost structure, payoff, validation limit, and next project action.

First inspect: `C.29`, `A.6.0`, `A.6.1`, `E.18.1`, `C.16`, `C.27`, `C.30.LCA`, `C.30.ILC`, and the domain pattern that governs the modeled claim.

### 13. Build a state-of-the-art or option portfolio

Use this when the project needs the current field of possible solutions, schools of thought, research lines, technologies, or design options, rather than one recommendation.

FPF helps you harvest alternatives, keep novelty and diversity visible, define comparison characteristics, avoid early collapse to one winner, and refresh the portfolio as the field changes.

Typical first result: a SoTA pack, option portfolio, candidate set, archive, or selector-ready publication with declared scope, comparison characteristics, and refresh condition.

First inspect: `G.0`, `G.1`, `G.2`, `G.5`, `G.10`, `G.11`, `C.18`, `C.19`, `A.19`, and `A.19.ECS`.

### 14. Build a domain or local FPF-grounded framework

Use this when a team needs its own FPF-grounded guide for a domain, organization, role context, or local practice, such as a hydroponic-cucumber framework, neural-network architecture framework, enterprise architecture-review framework, or Codex-process framework.

FPF helps you keep the FPF Core, domain principle framework, local practice framework, source pack, selected pattern set, relation records, edition dependencies, publication/access carriers, quality loop, and refresh route from collapsing into one all-in-one carrier, one callable route, or one useful checklist. This is the normal adoption path when a group wants FPF for its own field without turning local policy into a Core rule.

Typical first result: a family-and-structure map or principle-framework architecture decision that names the framework edition, bounded context, FPF Core dependency, selected first patterns, relation and publication carriers, source pack, quality route, and refresh route.

In the first hour, write the context note, source-pack stub, first PFAD question, provisional name route, one to three pattern candidates, relation rows, first-entry carrier, quality route, and refresh trigger. Then open `E.4.DPF` for the full authoring spine.

First inspect: `E.4`, `E.4.FPF` when the form of FPF itself is live, `E.4.PFAD`, `E.4.DPF`, `E.4.DPF.DA`, `E.4.PFR`, `G.2`, `E.8`, `E.11`, `E.17`, `F.18`, and `G.11`.

## One-Minute Example

A platform team asks:

> Should we buy, fine-tune, or build an agent stack for our product?

Without FPF, the conversation often mixes architecture, vendor comparison, safety, evidence, budget responsibility, user value, and implementation planning. The loudest option can win before the team knows what is being compared.

With FPF, the first pass can become a small set of explicit project objects:

- holons in play: the product, the agent stack, and the team or toolchain that will change it are not the same thing;
- architecture flow: what problem pressure should become which candidate, selected, expected, and actual structures;
- comparison frame: which alternatives are in the candidate set;
- evaluation characteristics: cost, latency, controllability, safety, maintainability, time to first use, and other project-specific characteristics;
- evidence gaps: what must be tested before commitment;
- current decision state: whether the team is choosing now, keeping a selected set, making a project architecture decision, or doing more discovery;
- work and feedback: what method, readiness, and performed-work records must later show that the selected structures were actually realized;
- reader reliance: what engineering, management, and assurance readers may responsibly rely on.

That same shape can be used for a factory modernization, laboratory protocol, construction design change, supply-chain decision, safety case, or research program. The point is not the AI topic; the point is one body of reasoning that can be reviewed, improved, and published without changing meaning on the way.

## What FPF Is

FPF is a pattern language for disciplined thinking in projects where ordinary prose, local expert judgment, or one-off AI output is not enough.

It helps teams:

- keep meanings stable when work crosses teams, tools, documents, and time;
- separate the thing being discussed from diagrams, dashboards, explanations, promises, decisions, and actual work;
- state what a claim can responsibly be used for before people rely on it;
- compare options without collapsing too early to one favorite;
- define quality criteria before improvement starts;
- keep evidence, assurance, decisions, and implementation work visible as different questions;
- carry architecture work from problem pressure to real structures and feedback instead of stopping at diagrams or decision prose;
- grow domain or local frameworks from FPF Core without silently changing Core meaning;
- repair confusing wording by first asking what the wording is doing in the project, not by swapping synonyms;
- leave each pass with one useful next result: a clearer question, a better name, a comparison note, an evidence gap, a safer document, or a reason to inspect a specific pattern.

## What FPF Is Not

FPF is not:

- a shrink-wrapped project methodology;
- a checklist bureaucracy;
- a quick-answer cheat sheet;
- a replacement for domain expertise;
- a demand to study the whole specification before useful work begins;
- a promise that every project needs every pattern.

FPF is most useful when the cost of semantic drift, premature convergence, hidden evidence gaps, weak architecture, vague quality, or unreviewable work is higher than the cost of using a disciplined pattern language.

## How to Use This Repository

Start with the first practical entry that matches your project question. Then inspect the named pattern family and apply its Problem frame, Solution, examples, and checklist.

Use the `Preface` for the cross-cutting ideas behind the pattern language. Use the Table of Content when you already know the pattern family or need a search-oriented overview. Use extended cases only when the compact first entry is not enough.

If you use an AI assistant, attach or index `FPF-Spec.md` and ask for plain-language project help first. Let internal pattern names enter the conversation only when they make the reasoning more precise.

A good first prompt is:

```text
You have the FPF specification as a file.
Help me structure this project:
[short project description]

Use plain language for engineer-managers.
Propose the first useful FPF entry:
architecture, rules and methods, API or interface wording, permission or compliance wording, comparison and choice,
problem shaping, quality improvement, evidence and assurance,
temporal claims, causal or model-output use, publication or view use,
naming, technical-text precision, mathematical modeling,
current options and state of the art,
or a domain/local FPF-grounded framework.
For the selected entry, give:
1. the main project thing or claim at stake,
2. the first useful written result,
3. the first FPF patterns to inspect,
4. what still cannot be decided, trusted, or used responsibly.
```

## Citation

If you use FPF, please cite:

```text
Levenchuk, Anatoly. First Principles Framework (FPF).
GitHub repository: https://github.com/ailev/FPF
```
