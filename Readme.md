# First Principles Framework (FPF) - Core Conceptual Specification

> First Principles Framework (FPF) is a standards-style pattern language for turning difficult engineering, research, management, and mixed human and AI work into explicit, reviewable, improvable reasoning.

- **Author:** Anatoly Levenchuk, with AI-agent assistance
- **Version:** July 2026
- **Status:** Normative kernel, eternal alpha: already used in working projects and development programs, while still evolving.

FPF helps when a project has outgrown one clever conversation. It is useful when meanings, claims, options, evidence, architecture, work decisions, publication forms, and improvement criteria need to stay coherent across people, teams, tools, time, or AI agents.

Use FPF as a reference model and pattern language, not as a linear textbook. Start from the working question you bring from your project. Bring in internal FPF terms only after they help you keep the work precise.

This readme is a thin public practical-use rendering of FPF for engineers, researchers, managers, reviewers, and AI-assisted project workers deciding what FPF can help them do now. It foregrounds the project questions most likely to pay off and deliberately coarsens, omits, or defers the full pattern language, source publications, source-use history, and relation structure. When a claim becomes important, return to the Preface, Table of Contents, and governing pattern body rather than treating this readme as the specification.

Begin with the project object at stake and the current question about it. FPF often calls an object a holon when it is being treated as a whole with parts: a machine, product, organization-as-system, body of knowledge, publication system, work occurrence, discipline, AI-agent arrangement, method, or local framework admitted under part-whole treatment. Roles use their own role ontology. Once the object and question are named, ask which structure, claim, decision, evidence, description, work, or improvement relation is current.

## Decide Whether FPF Fits

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
- when an accepted `ProblemCard@Context` claim must remain usable while the project selects a method, prepares or performs work, interprets a result, branches, stops, or returns after a changed assumption, inspect `E.18.1 P2W Problem-to-Work Carry-Through`; it carries that claim into one next value or relation governed by its direct pattern rather than prescribing one universal workflow;
- when a route-like explanation has several candidate positions and proposed relations or constraints that may change which continuations remain admissible, use it as a `ProvisionalUnfoldingDemonstrationDescription@Context` while any A.22.CGUS admission coordinate remains unresolved; after the wider CGUS is admitted, a separate `DemonstrativeUnfoldingSlice@Context` may present one traversal, and when admitted positions organize bounded transformations inspect the `E.18.3` specialization;
- keep several options alive until the comparison is clear enough to choose;
- say what "better" means before optimizing or scoring;
- make trust depend on evidence, freshness, scope, and intended use;
- publish different views for different readers without changing the underlying claim;
- when explanation, reader-facing ordering, or narrative rendering of selected source structure is current, state what structure is preserved, deliberately coarsened, abstracted, omitted, or lost, and which named source basis or governing pattern receives the return when loss matters;
- use mathematics or formal models when they clarify what structure is preserved, what is lost, and what can be checked;
- build domain or local FPF-grounded frameworks as dependents of FPF Core, not as silent rewrites of the Core.

## Practical-Use Cards

Start with the current project question, not an ordinal route through FPF. The fifteen semantic keys below are stable identifiers, not steps. When several cards seem plausible, compare their situations, first-result differences, and stop or return conditions in the conversation. Then inspect the direct pattern's Problem frame, Problem, Forces, Solution, Consequences, and ordinary boundary. Materialize comparison or candidate records only when a named receiving use relies on them.

In each card, the conditional template list is one ordinary walkthrough: inspect only the branch whose stated condition is current, apply that direct pattern's Solution, obtain its exact result, and stop or return at the card boundary. It is not a `DemonstrativeUnfoldingSlice@Context` because the card does not assert one wider constraint-governed structure with typed positions and relations among every alternative. The list is not a project order or a claim that all branches will execute.

The cards are domain-neutral. A first useful result may be a physical or clinical state, a capability, an episteme, a relation, dated `U.Work`, or another exact subject-governed value. A generated note, measurement, dashboard, or plan does not stand for machining, treatment, organizational change, learning, or another downstream result.

### ARCHITECTURE - Shape architecture from problem pressure

- **Situation and question.** Architecture-relevant problem pressure and competing characteristics are present, but the project needs to carry them toward candidate, selected, expected, or actual structures. Ask: which architecturing flow or description-use result is needed first?
- **Optional obstacle.** Candidate structures, architecture characteristics, or the relation between problem pressure and structure are not yet reviewable.
- **Template A.** `C.32.P2S Solution -> ProblemToStructureArchitecturingFlowCard@Project`. Select when the connected problem-to-structure flow is current. Local basis adds architecture-relevant pressure refs and current architecture-characteristic refs when available.
- **Template B.** `C.30.AD Solution -> ArchitectureDescriptionUseCard@Project`. Select when an existing architecture description or view is already the object being used and its admissible-use boundary is current.
- **Boundaries.** Stop when the selected first card makes the receiving architecture work reviewable. Return when problem pressure, EntityOfConcern, characteristics, description edition, or actual-structure feedback changes. Wrong-turn recovery sends a diagram-as-architecture claim to C.30 and C.33. Stronger neighbors are C.32 synthesis, C.32.PAD decision, A.15 work, E.23 improvement, or G.11 currentness according to the next claim.
- **Public coarsening.** "Architecture working card" restores to one of the two exact project cards; it does not denote architecture itself.

### WORKING-DOCUMENTS - Create a document another participant can use

- **Situation and question.** A participant asks for a regulation, procedure, plan, interface description, permission text, evidence note, gate record, publication, or AI tool-use plan. Ask first which use is current for the text: preserve meaning and boundary claims, prepare enactment, support reliance or a gate, or publish already governed content. The reader inspects only the branch selected by that question.

**Branch A: preserve meaning and boundary claims.**

- `A.6 Solution -> Claim Register` or an equivalent small claim set classified as L, A, D, and E when one text mixes definitions, admissibility, commitments, and evidence claims.
- `A.3.2 Solution -> U.MethodDescription` when the result describes a reusable semantic way of doing under conditions.
- `A.2.8 Solution -> U.Commitment` when an accountable subject's obligation, permission, or prohibition, scope, validity window, and referents are the actual result.
- If `interface` still hides whether the current claim concerns a signature, slot, module interface, functional port, protocol, service relation, or publication, use A.6.RSIR only to select the direct governing pattern, retain a reduced-use source label, or return a blocker. RSIR does not produce the downstream interface result. Once the direct claim is recovered, use its pattern and exact result; use A.6.M directly only for a recovered module-interface relation.

**Branch B: prepare enactment.**

- `A.15.2 Solution -> U.WorkPlan` when stating intended dated work, PlanItems, assignments, resources, windows, or sequencing constraints is current.
- `C.24 Solution -> CallPlan | CheckpointReturn` when tool-call enactment is current: use `CallPlan` after routes and budgeted execution are fixed enough, or `CheckpointReturn` while bounded probing remains the honest result.
- `A.15.5 Solution -> WorkEntryReadiness@Context` only when intended work already exists and readiness to cross its work boundary is current.

**Branch C: support reliance or a gate.**

- `A.10 Solution -> claim-bound evidence-provenance graph relation` when a named receiving use relies on recovering the basis for one claim or effect through evidence-producing or interpreting work, trace, time window, and bounded use.
- `B.3 Solution -> Assurance(H, C | K, S)` or an explicit no-assurance-claim disposition when the text is expected to carry a named assurance claim rather than merely point to evidence.
- `A.21 Solution -> OperationalGate(profile) use with GateProfile, effective GateCheckRefs, aggregated CV status, GateDecision, and DecisionLogRef` when exposing an actual gate decision is current. A readable checklist is not that decision.

**Branch D: publish governed content.**

- `E.17 Solution -> source-pinned publication face` when readable, exchangeable, or citable publication of an already governed episteme or relation is current without changing the underlying claim.

- **Boundaries.** Stop when the selected branch yields the exact result needed by its receiving use. Return to branch selection when the expected use changes. A single document may cite results from several branches, but page proximity does not merge their kinds or transfer their claims to a different governing pattern. RSIR stops at pattern selection, reduced-use source labeling, or a blocker; it never certifies that an interface relation now exists.
- **Public coarsening.** "Working document" is only a recognizable situation label. The expansion restores the selected branch, direct pattern, exact result, and receiving use.

### OPTION-COMPARISON - Compare alternatives and select the current result kind

- **Situation and question.** Several possibilities are present, but the current need may be to define comparison, retain diversity, govern a live pool, publish a selected set, or make one local choice. Ask which of those relations is current.
- **Template A.** `A.19.ECS Solution -> EvaluationCharacteristicSpaceSpec`. Select when coordinates, scales, evidence rules, and protected trade-offs are not adequate for comparison.
- **Template B.** `C.18 Solution -> ExplorationArchiveRecord@Context | FrontRecord@Context`. Select the archive result when later use relies on retained variants and their lineage or diversity; select the front result when later use relies on inspectable non-dominance and its comparator basis.
- **Template C.** `C.19 Solution -> PoolPolicyResult`. Select when a still-live pool needs one explicit `widen`, `keep frontier`, `narrow to subset`, or `sunset line` treatment and a change trigger.
- **Template D.** `G.5 Solution -> Shortlist | RankedShortlist | SpecialistHandoff | abstain or escalation outcome`. Select when selector-facing publication of a set or narrowed handoff is current; use a ranked result only when order materially belongs to the published result.
- **Template E.** `C.11 Solution -> ChoiceResult`. Select when an OptionSet and comparison basis exist and one local choose, reject, probe, or reroute result is current.
- **Boundaries.** Stop at the result answering the current option question. Return when candidate membership, archive policy, dominance basis, pool policy, selector publication, comparison basis, preference order, or probe value changes. An archive is not a live pool, narrowing a pool does not publish a shortlist, and a shortlist is not a local choice.
- **Public coarsening.** "Option comparison" is the recognizable situation; the expansion restores evaluation specification, archive, front, pool-policy result, selected-set publication, or local choice under its exact condition.

### PROBLEM-SHAPING - Turn early pressure into an honest problem-side result

- **Situation and question.** Something matters, but it may still be an early cue, a set of possible inquiry routes, an abductive question, or a problem ready for acceptance. Ask how far articulation has actually progressed.
- **Template A.** `A.16.1 Solution -> U.PreArticulationCuePack`. Select when a cue nucleus and its witness or anchor should be preserved before a route or problem claim is stable.
- **Template B.** `B.4.1 Solution -> RoutedCueSet`. Select when cue content is stable enough to publish route plurality or one selected route with explicit rationale, while no later endpoint is yet warranted.
- **Template C.** `B.5.2.0 Solution -> U.AbductivePrompt`. Select when prompt species, open question, scope, and cue provenance are stable enough to seed abductive search.
- **Template D.** `C.22.2 Solution -> ProblemCard@Context`. Select when the affected EntityOfConcern, constraints, unresolved relations, distinctions to preserve, and acceptance basis can be stated without smuggling in a selected solution.
- **Conditional continuation.** When an accepted problem-side record must become usable by later eligibility, acceptance, or method-family selection, inspect `C.22 Solution -> TaskSignature`. The TaskSignature types only the current problem traits and receiving use; it does not select a method, issue a selector verdict, plan work, or prove that work occurred.
- **Boundaries.** Stop at the earliest result that is both truthful and useful. Return or back off when the cue anchor, route rationale, prompt contrast, affected EntityOfConcern, constraint, or acceptance basis changes. Do not force a cue into a ProblemCard merely to make the work look started.
- **Public coarsening.** "Problem shaping" restores to the exact cue pack, routed cue set, abductive prompt, or accepted ProblemCard under its articulation condition.

### IMPROVEMENT - Define evaluation before repeating improvement

- **Situation and question.** A named object version should improve, but evaluation purpose, quality family, scales, proposal effect, or repeated-loop need may still be unsettled. Ask which prerequisite for improvement is missing now.
- **Template A.** `E.22 Solution -> QualityEvaluationQuestionFrame`. Select first when evaluation purpose, floor or improvement aim, protected trade-offs, expected evidence basis, or expected result form is not yet agreed.
- **Template B.** `C.25 Solution -> Q-Bundle`. Select when a composite engineering quality family needs a bearer, components, measures, scope, mechanisms, status, and evidence relation.
- **Template C.** `A.19.ECS Solution -> EvaluationCharacteristicSpaceSpec`. Select when the object-specific coordinates, scales, comparators, and evidence rules needed for evaluation do not yet exist.
- **Template D.** `E.23 Solution -> QualityImprovementLoopRecord`. Select only when the object version and evaluation basis exist and repeated proposal, change, coordinate-qualified re-evaluation, and loop decision are current.
- **Boundaries.** Stop at the smallest missing frame, Q-Bundle, evaluation specification, or completed local loop record. Return when object version, evaluation purpose, Q components, scale, comparison set, evidence basis, expected result change, or protected trade-offs change. "Repeat until better" is not a loop method until better is evaluable on declared coordinates.
- **Public coarsening.** "Improvement frame" restores to the exact result under its prerequisite condition.

### COSTLY-ACTION - Prepare an expensive or hard-to-reverse action

- **Situation and question.** A proposed action is expensive, externally committing, safety-relevant, or hard to reverse. Ask which unresolved uncertainty or governing relation currently prevents responsible commitment, gate use, intended work, or performed work.
- **Template A.** `A.10 Solution -> claim-bound evidence-provenance graph relation`. Select when the support basis for one claim or effect is not recoverable.
- **Template B.** `B.3 Solution -> Assurance(H, C | K, S)` or an explicit no-assurance-claim disposition. Select when the action depends on a named assurance claim and its limitations and decay condition.
- **Template C.** `A.20 Solution -> path-slice-local CV result with step, CV class, CV.Status, and witness or refusal`. Select when constraint validity is the current question; this result does not itself pass a gate.
- **Template D.** `A.21 Solution -> OperationalGate(profile) use with GateProfile, GateCheckRefs, aggregated CV status, GateDecision, and DecisionLogRef`. Select when a real gate decision is current.
- **Template E.** `C.28 Solution -> CausalUseTriageRecord`. Select when expected effects, intervention, counterfactual, or policy claims carry the action rationale and their supported-rung boundary is current.
- **Template F.** `C.11 Solution -> ChoiceResult`. Select when several actions remain live and the current result is choose, reject, probe, or reroute.
- **Template G.** `A.15.5 Solution -> WorkEntryReadiness@Context`. Select only after intended work exists and readiness to enter its work boundary is the current relation.
- **Boundaries.** Stop at the first result that decides the present uncertainty; do not force every costly action through all templates. Return when the claim, evidence path, assurance context, constraint definition, gate profile, causal-use basis, option set, intended work, resource state, cost, or reversibility changes. Planning or readiness does not authorize or perform work, and a gate display does not replace `GateDecision`.
- **Public coarsening.** "Costly action" restores to the exact evidence, assurance, constraint-validity, gate, causal-use, choice, or readiness result under its selection condition.

### TIME - Use timing and currentness claims responsibly

- **Situation and question.** A claim about rate, rhythm, delay, effort, inertia, recovery, currentness, or validity window is being used for action. Ask whether temporal-claim adequacy or source currentness orchestration is current.
- **Optional obstacle.** A snapshot is used as a trend, a trend as a control law, or an old edition as current.
- **Template A.** `C.27 Solution -> Dyn2TemporalClaimAdequacyCard`. Select when a local temporal claim changes supported use.
- **Template B.** `G.11 Solution -> RefreshCurrentnessLine@Context`. Select when freshness, edition, telemetry, decay, or currentness is the live claim.
- **Boundaries.** Stop at the smallest supported temporal card or currentness line. Return when window, bearer, evidence relation, model assumption, source edition, or telemetry changes. Wrong-turn recovery downgrades unsupported rate or currentness claims. Stronger neighbors are C.16 for measurement, C.28 for causal use, A.15 for work, and the direct source or publication governing patterns.
- **Public coarsening.** "Time check" restores to the C.27 card or G.11 line.

### CAUSAL-USE - Bound causal language before using it for action

- **Situation and question.** Causal, intervention, effect, policy, or counterfactual language is being used to support a decision or action. Ask: what causal-use rung and support basis are actually available?
- **Optional obstacle.** Association, intervention, and counterfactual claims are being treated as interchangeable.
- **Template A.** `C.28 Solution -> CausalUseTriageRecord`. This is the initial template; local basis adds the live causal wording, target use, candidate rung, comparator or counterfactual, and support-basis refs.
- **Boundaries.** Stop at the triage record when it honestly bounds supported and unsupported use. Return when intervention, comparator, target population, evidence, or causal-use purpose changes. Wrong-turn recovery downgrades causal laundering to the supported claim. Stronger neighbors are CausalUseEvidenceDesignRecord or CausalUseSupportVerdict inside C.28, C.11 for choice, and direct evidence or work patterns.
- **Public coarsening.** "Causal check" restores to `CausalUseTriageRecord`.

### DESCRIPTION-USE - Create or use a description without losing its subject

- **Situation and question.** A description, view, dashboard, explanation, model, report, or publication is to be created, compared, transformed, or relied on. Ask which unresolved EntityOfConcern, viewpoint, representation change, lost structure, source set, or architecture use blocks the current use.
- **Template A.** `E.17.0 Solution -> DescriptionContext`. Select for the generic describing case: name `EntityOfConcernRef`, `BoundedContextRef`, `ViewpointRef`, resulting view or view family, and any correspondence relation needed for the current comparison.
- **Template B.** `A.6.3.RT Solution -> RepresentationSchemeTransitionRelation@Context`. Select when the same EntityOfConcern is being re-represented and a named receiving use relies on recovering the source representation, receiving representation, preserved claim or commitment, source-relation chain, representation-scheme delta, loss or recoverability, admissible use, and non-admissible downstream use. The relation records the concrete case; `RepresentationSchemeTransition` remains the method-pattern name.
- **Template C.** `C.33 Solution -> StructuralInformationAdequacyNote@Context`. Select when the current question concerns what structure a description or view captured, lost, hid, and which wider source structure receives return for the declared architecture use.
- **Template D.** `E.17.ID.CR Solution -> ComparativeReviewUnit`. Select only for bounded comparison over already available source epistemes or publications. It is not the generic description result.
- **Template E.** `C.30.AD Solution -> ArchitectureDescriptionUseCard@Project`. Select when the subject is specifically an architecture description or view and its admissible architecture-use boundary is current.
- **Boundaries.** Stop at the smallest result answering the current description-use question. Return when EntityOfConcern, context, viewpoint, representation scheme, captured structure, source edition, comparison basis, or intended use changes. A publication carrier does not become its subject, and a readable view does not become evidence, assurance, permission, decision, architecture, or work without the corresponding governed relation.
- **Public coarsening.** "Description use" restores to `DescriptionContext`, `RepresentationSchemeTransitionRelation@Context`, `StructuralInformationAdequacyNote@Context`, `ComparativeReviewUnit`, or `ArchitectureDescriptionUseCard@Project` under the stated condition.

### NAMING - Name a governed value for its readers

- **Situation and question.** A governed value needs a stable Tech or Plain label across a bounded context. Ask: which name lets readers recover the value without changing its kind or scope?
- **Optional obstacle.** Candidate labels carry conflicting senses, hidden kinds, or misleading morphology.
- **Template A.** `F.18 Solution -> NameCard`. Local basis adds governed value, governing pattern, bounded context, candidate set, rejected candidates, rationale, bridges, lineage, and refresh condition.
- **Boundaries.** Stop at a complete NameCard when no public term publication is current. Return when governed value, context, candidate evidence, reader interpretation, or bridge changes. Wrong-turn recovery restores the governed value before selecting a label. F.17 becomes the stronger neighbor only when actual term-row publication is current.
- **Public coarsening.** "Naming card" restores to `NameCard`.

### WORDING - Repair wording without changing the kind by accident

- **Situation and question.** A sentence sounds fluent but hides which object, relation, slot, use position, or claim kind is active. Ask: what was the pre-repair kind and which invariant is preserved after rewriting?
- **Optional obstacle.** A trigger word has been replaced while ontology, admissible use, or scope drifted.
- **Template A.** `E.10 Solution -> KindRestorationCheck`. Local basis adds the exact span, pre-repair kind, relation, position, use, and scope, post-repair settlement, governing-pattern ref, and disposition.
- **Boundaries.** Stop when the repaired wording preserves or explicitly changes the kind by accepted decision and remains understandable under MG-DA. Return when the sentence's EntityOfConcern, use, or scope changes. Wrong-turn recovery rejects lexical substitution without semantic check. Stronger neighbors are F.19 for phrase-level prose repair, F.18 for durable naming, or the direct domain pattern for ontology repair.
- **Public coarsening.** "Wording repair" restores to `KindRestorationCheck` plus the changed sentence.

### MATHEMATICAL-MODELING - Use a mathematical lens when it changes the next action

- **Situation and question.** A project question may benefit from a mathematical object or lens, but the next action and lost structure are not yet clear. Ask: can one cheap lens result change the next admissible action?
- **Optional obstacle.** A metaphor such as graph-like, field-like, or optimization-like is being treated as ontology or evidence.
- **Template A.** `C.29 Solution -> MathLensUse.LensCandidateNote`. Select when no adequate mathematical object has yet been named.
- **Template B.** `C.29 Solution -> MathLensUse.OneLine`. Select when candidate mathematical object, mapping, preserved structure, lost structure, payoff, next action, rival or fallback, and stop condition can be stated.
- **Boundaries.** Stop at `NoMathLensUseNeededNote`, candidate note, or one-line result according to C.29. Return when EntityOfConcern, mapping, observation, preserved structure, or intended use changes. Wrong-turn recovery removes lens-as-world or lens-as-evidence overread. Stronger neighbors are C.29 MiniCard or FullCard, C.16 measurement, C.28 causal use, and C.30 architecture use.
- **Public coarsening.** "Mathematical-modeling note" restores to the selected `MathLensUse.*` output.

### SOTA-PORTFOLIO - Build a plural current field of options and sources

- **Situation and question.** A project needs the current plural field of methods, theories, technologies, or design options rather than one favored source. Ask first what source and tradition synthesis is adequate, then which stewardship relation is current for the resulting candidates.
- **Template A.** `G.2 Solution -> SoTA Synthesis Pack@CG-Frame`. Select when the immediate need is a reconstructible `SoTA_Set@CG-Frame` and `SoTAPaletteDescription` with rival traditions, claim rows, evidence anchors, crossings, and source-use boundaries.
- **Conditional walkthrough.** If later use relies on retained generated or harvested variants, use `C.18 -> ExplorationArchiveRecord@Context`; if later use relies on exposed non-dominated variants, use `C.18 -> FrontRecord@Context`; if a still-live pool needs treatment, use `C.19 -> PoolPolicyResult`; if a selector-facing set is to be published, use `G.5 -> Shortlist | RankedShortlist | another declared selector outcome`. These are conditional continuations, not synonyms or serial stages.
- **Boundaries.** Stop at the pack when downstream stewardship is not current. Return when scope, traditions, source editions, evidence anchors, or harvest policy changes. Archive, front, live pool, and selected set keep different membership, policy, and publication meanings; no prose summary may collapse them.
- **Public coarsening.** "SoTA portfolio" restores to the G.2 pack and, only when current, the exact C.18, C.19, or G.5 continuation result.

### DPF-AUTHORING - Build a reusable FPF-grounded domain framework

- **Situation and question.** A domain or local practice needs a reusable FPF-grounded framework edition rather than isolated advice. Ask whether the useful first result is a present organization-design proposal about an intended future framework, a settled framework-architecture decision, a post-claim architecture-description use, or a post-PFAD account of authoring dependencies.
- **Template A.** `E.4.DPF Solution -> FrameworkOrganizationDesignProposal@Context`. Select before PFAD when one current C.2.1 proposal episteme makes candidate organization claims reviewable. Its EntityOfConcern is a present intended-framework-result description whose EntityOfConcern is an A.15.2 `U.WorkPlan`; proposal and description share the description's exact A.1-admitted grounding holon. Its one ClaimGraph carries typed candidate claim nodes and proposed subject relation signatures. A relation-family coverage constraint node carries covered family ref-kind pairs, admitted use, and coverage criterion; a WorkPlan acceptance target remains separate basis. A materialized PUA expectation expects this proposal, not the later framework edition. Claim status carries proposedness; accountable obligation exits to A.2.8; a separate return points to E.4.PFAD when framework-architecture settlement is current. Optional proposal meta-structure never substitutes for proposed subject organization.
- **Template B.** `E.4.PFAD Solution -> PrincipleFrameworkArchitectureDecision@Context`. Select when framework family, Core dependency boundary, content boundary, pattern relation structure, publication architecture, or access architecture is the current decision question. The filled decision relation exists before any ADR-like publication of it.
- **Template C.** `C.30.AD Solution -> ArchitectureDescriptionUseCard@Project`. Select only after the framework entity, `ArchitectureOf@Context`, and selected architecture-relevant structures exist, and when admissible use of the corresponding architecture description is current.
- **Template D.** `E.4.DPF Solution -> FrameworkAuthoringDependencyDescription@Context`. Select only when PFAD exists and the immediate need is a minimal account of dependency availability and relevance for the next authoring use. This C.2.1 episteme concerns the current DPF-authoring `U.WorkPlan`, has one exact grounding holon, ClaimGraph, and ReferenceScheme, and contains at least the Core-edition, source-basis, and PFAD dependency positions. Core edition and PFAD are available with exact value-kind refs. Another missing dependency has an acquisition-condition description and no value ref; an available dependency has exact value and kind refs and no acquisition condition. Relevance remains independent in both branches. Future products need not exist; a missing PFAD returns to Template B.
- **Boundaries.** Stop at the proposal while its candidate organization ClaimGraph is the current result, at PFAD while framework-architecture settlement is current, at the C.30.AD use card while post-claim description use is current, or at the dependency description when it makes the next authoring work recoverable. Return when intended result kind, current intended-result description, proposal basis, design question, candidate relation signature, constraint, invariant, dependency direction, alternative, unresolved position, Core edition, source basis, architecture decision, publication or access use, quality result, or currentness changes. Neither a topic list nor an organized proposal document without proposed subject relations is a proposal result.
- **Public coarsening.** "DPF authoring" restores to `FrameworkOrganizationDesignProposal@Context`, `PrincipleFrameworkArchitectureDecision@Context`, `ArchitectureDescriptionUseCard@Project`, or `FrameworkAuthoringDependencyDescription@Context` under the stated condition.

### SYSTEM-IN-CONTEXT - Make the current system question explicit

- **Situation and question.** A candidate system is named, but the current system question is not yet explicit. Ask whether the needed first result concerns identity and environment, composition, participation and functioning, selected structures, intended creation or change, or creation or change that has already occurred.
- **Template A.** `A.1 Solution -> HolonDelimitationRelation@Context`. Select for identity rule, bounded context, included or excluded entities, environment relation, selected-structure boundary, or current boundary condition.
- **Template B.** `B.1.2 Solution -> SystemAggregationRelation@Context`. Select when aggregation depends on distinguishing admitted system parts from external crossing relations.
- **Template C.** `A.1 Solution -> SystemParticipationRelation@Context`. Select when the current question connects the acting system to functioning, functional elements, roles, capabilities, methods, mechanisms, work plans, work occurrences, transformations, evidence, assurance, or temporal and dynamics aspects. Each linked value keeps its direct governing pattern.
- **Template D.** `C.30 Solution -> ArchitectureQuestionCard@Project`. Select when the system is identified and selected structures or architecture relations are now current.
- **Template E.** `A.15.2 Solution -> U.WorkPlan`. Select when planning intended system creation or change is current.
- **Template F.** `A.15.1 Solution -> U.Work`. Select only when creation, change, maintenance, or another dated occurrence has happened and can be grounded through its performer, enacted method, affected referent, resources, outcome, time window, and evidence relation. The occurrence is the direct result; `ResultProducingWorkSlot[]` remains absent, while any planning, setup, authorization, or causal relation to other work returns to its direct governor.
- **Boundaries.** Stop at the smallest result that answers the current question. Return when system identity, context, parthood, participation, selected-structure question, intended work, or performed-work evidence changes. Wrong-turn recovery restores system, environment, part, participation, architecture, plan, performed work, and description as separately governed values. A diagram box is not a system boundary by shape, a functioning description is not the functioning system, and a work record is not a system part merely because it appears inside one project view.
- **Public coarsening.** "System in context" restores to the exact selected result under its selection condition.

## One-Minute Example

A platform team asks:

> Should we buy, fine-tune, or build an agent stack for our product?

Without FPF, the conversation often mixes architecture, vendor comparison, safety, evidence, budget responsibility, user value, and implementation planning. The loudest option can win before the team knows what is being compared.

With FPF, the first pass can become a small set of explicit project objects:

- holons in play: the product, the agent stack, and the team or toolchain that will change it are not the same holon;
- architecture flow: what problem pressure should become which candidate, selected, expected, and actual structures;
- comparison frame: which alternatives are in the candidate set;
- evaluation characteristics: cost, latency, controllability, safety, maintainability, time to first use, and other project-specific characteristics;
- evidence gaps: which test result makes commitment admissible;
- current decision state: whether the team is choosing now, keeping a selected set, making a project architecture decision, or doing more discovery;
- work and feedback: which method, readiness, and performed-work records establish that the selected structures were actually realized;
- reader reliance: what engineering, management, and assurance readers may responsibly rely on.

That same shape can be used for a factory modernization, laboratory protocol, construction design change, supply-chain decision, safety case, or research program. The point is not the AI topic; the point is one body of reasoning that can be reviewed, improved, and published without changing meaning on the way.

## What FPF Is

FPF is a pattern language for disciplined thinking in projects where ordinary prose, local expert judgment, or one-off AI output is not enough.

It helps teams:

- keep meanings stable when work crosses teams, tools, documents, and time;
- separate the project object being discussed from diagrams, dashboards, explanations, promises, decisions, and actual work;
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

Start with the practical-use card that recognizes the current project question. If several fit, compare their situations, first-result differences, and stop or return conditions before inspecting the selected direct pattern.

Use the `Preface` for the cross-cutting ideas and the repeated-use explanation. Use the Table of Contents when you already know the pattern family or need a search-oriented overview. Use the direct pattern body for the governed Solution. Once one direct pattern is current, use `E.11.PUA` to apply its Solution to the first exact result and its receiving use. Use `E.11.PUR` only when a named receiving use needs an addressable applicability finding, recommendation, coordination, or ordering relation. Use extended cases when the compact card and direct pattern are not enough.

If you use an AI assistant, attach or index `FPF-Spec.md` and ask for plain-language project help first. Let internal pattern names enter the conversation only when they make the reasoning more precise.

A good first prompt is:

```text
You have the FPF specification as a file.
Help me with this current project question:
[short project description and question]

Use plain language for engineer-managers.
Compare the relevant semantic practical-use cards when several fit:
ARCHITECTURE, WORKING-DOCUMENTS, OPTION-COMPARISON,
PROBLEM-SHAPING, IMPROVEMENT, COSTLY-ACTION, TIME,
CAUSAL-USE, DESCRIPTION-USE, NAMING, WORDING,
MATHEMATICAL-MODELING, SOTA-PORTFOLIO, DPF-AUTHORING,
or SYSTEM-IN-CONTEXT.

Then inspect the selected direct pattern and give:
- the current EntityOfConcern and practical question;
- the pattern and Solution selected under the current condition;
- the exact kind of first useful result;
- what that result lets us do next;
- where to stop or return when a stronger claim becomes current.

Keep comparison conversational unless a named receiving use relies on an addressable record.
Do not turn the card into a whole-project plan.
```

## Citation

If you use FPF, please cite:

```text
Levenchuk, Anatoly. First Principles Framework (FPF).
GitHub repository: https://github.com/ailev/FPF
```
