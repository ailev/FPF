---
type: "fpf-knowledge-page"
context:
  - "FPF"
page_type: "fpf-knowledge-page"
mode: "canonical-generated"
title: "Decide Whether FPF Fits"
part: "[[00_Hubs/FPF - First Principles Framework (FPF) Readme]]"
parents:
  - "[[00_Hubs/FPF - First Principles Framework (FPF) Readme]]"
source_file: "FPF-Spec.md"
source_lines:
  - 412
  - 460
status: "generated"
generated_on: "2026-08-02"
generated: true
---


Use FPF when ordinary discussion is no longer enough to keep work coherent. Typical signs:

- several teams, experts, tools, or AI agents share reasoning about the same work;
- the real-world test is slow, expensive, noisy, risky, or politically hard to repeat;
- different readers need different reports, dashboards, explanations, or decisions about the same underlying work;
- names, roles, responsibilities, options, evidence, or quality criteria are starting to blur;
- the team needs a current view of possible approaches, not just one recommendation;
- a decision is small enough to make now but important enough to leave a durable reason.

FPF is probably too heavy when the task is small, feedback is fast and cheap, the vocabulary is already stable, the decision will not be reused or audited, and a quick answer is enough.

FPF is mainly useful for people who have to keep difficult work understandable across boundaries:

- engineers and systems engineers working with complex products or operations;
- researchers building claims for inspection or reuse by others;
- platform and AI teams coordinating humans, models, tools, and approvals;
- safety, assurance, compliance, and regulatory leads who need visible evidence and responsibility boundaries;
- managers and product leaders comparing options, budgets, risks, and delivery promises without hiding trade-offs.

There are three common ways to use FPF:

1. Human-only: use it as a writing and review discipline for meetings, notes, decisions, and technical documents.
2. Mixed team: use it to keep specialists, managers, safety leads, and AI assistants aligned around the same work.
3. AI-assisted: attach or index the specification, ask for plain-language project help first, and use pattern names only when they make the answer easier to check.

Stronger AI does not remove the need for FPF. AI can generate fluent options quickly, but projects still need to decide what counts as evidence, which option is being compared, who may rely on an answer, when a claim is stale, what remains only a guess, and what work is actually authorized. FPF helps make those boundaries explicit before a confident answer becomes an expensive mistake.

Core ideas in plain language:

- first name the project object under concern; when it is treated as a whole with parts, FPF calls it a holon;
- local teams may use local meanings; boundary-crossing work makes the translation relation explicit;
- the project object itself, its description, a dashboard about it, a decision about it, and the work done to change it are not the same;
- architecture is structure of that holon or project object in a context, not the diagram, document, approval, or plan about it;
- serious architecture work can move from problem pressure to candidate structures, selected structures, decisions, method and work, actual structures, and feedback;
- when the current question is which reusable way of doing changes, produces, derives, selects, controls, or preserves the project object under stated conditions, inspect `A.3.1 U.Method`; a strategy name, procedure text, program, plan, dated run, mechanism, or evidence record does not answer that method question by its label or form;
- when one already-selected direct-kind method, model, formalism, assurance technique, ontology, or other apparatus is current and its setup/application cost must earn one declared use, inspect [[C_Kernel Extension Specifications/07_19_Explore-Exploit Live-Pool Governor/02_C.19.02 - Use-Bounded Apparatus Application|C.19.2]]; it governs one bounded application to a separately governed problem-facing result and guarantee. Open [[C_Kernel Extension Specifications/06_18_Open-Ended Search Archive and Front Stewardship/00_C.18 - Open-Ended Search Archive and Front Stewardship|C.18]] only when an adequate candidate must be generated or reframed, and [[C_Kernel Extension Specifications/02_11_Decision Theory (Decsn-CAL)/00_C.11 - Decision Theory (Decsn-CAL)|C.11]] only when two or more eligible alternatives make a real local choice current;
- when a clear engineering claim produces a wrong action, identity, dependence, obtaining, responsibility, or projection consequence, inspect [[A_Kernel Architecture Cluster/07_Strict Distinction (Clarity Lattice)/01_A.07.01 - Consequence-Guided Ontological Problem Solving|A.7.1]]; when current FPF uses produce incompatible consequences for the same receiving claim and scope, inspect [[A_Kernel Architecture Cluster/07_Strict Distinction (Clarity Lattice)/02_A.07.02 - FPF Ontology-Premise Reconciliation|A.7.2]]. In either route, keep the method episteme, admitted performer, dated work, returned direct-owner result, and one result episteme distinct: the local disposition is a value in that result, not its kind, and [[A_Kernel Architecture Cluster/07_Strict Distinction (Clarity Lattice)/02_A.07.02 - FPF Ontology-Premise Reconciliation|A.7.2]] need not converge;
- when an accepted [[C_Kernel Extension Specifications/10_22_Task Typing and TaskSignature Assignment (Problem-CHR)/03_C.22.02 - ProblemCard|C.22.2]] `ProblemCard` episteme must remain usable while the project selects a method, prepares or performs work, interprets a result, branches, stops, or returns after a changed assumption, inspect `E.18.1 P2W Problem-to-Work Carry-Through`; it carries the accepted problem-side distinctions into one next value or relation governed by its direct pattern rather than prescribing one universal workflow;
- when a route-like explanation has several candidate positions and proposed relations or constraints that may change which continuations remain admissible, use it as a `ProvisionalUnfoldingDemonstrationDescription@Context` while any [[A_Kernel Architecture Cluster/22_Structure and Structural Views (STRUCT-CAL)/01_A.22.CGUS - Constraint-Governed Unfolding Structure|A.22.CGUS]] admission coordinate remains unresolved; after the wider CGUS is admitted, a separate `DemonstrativeUnfoldingSlice@Context` may present one traversal, and when admitted positions organize bounded transformations inspect the [[E_The FPF Constitution and Authoring Guides/17_18_Transformation Flow Structure/03_E.18.03 - Constraint-Governed Transformation-Flow Unfolding Structure|E.18.3]] specialization;
- keep several options alive until the comparison is clear enough to choose;
- say what "better" means before optimizing or scoring;
- make trust depend on evidence, freshness, scope, and intended use;
- publish different views for different readers without changing the underlying claim;
- when explanation, reader-facing ordering, or narrative rendering of selected source structure is current, state what structure is preserved, deliberately coarsened, abstracted, omitted, or lost, and which named source basis or governing pattern receives the return when loss matters;
- use mathematics or formal models when they clarify what structure is preserved, what is lost, and what can be checked;
- build domain or local FPF-grounded frameworks as dependents of FPF Core, not as silent rewrites of the Core.
