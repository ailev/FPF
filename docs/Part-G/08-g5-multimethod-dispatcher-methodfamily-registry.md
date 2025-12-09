## G.5 — **Multi‑Method Dispatcher & MethodFamily Registry** \[A]

**Tag:** \[A] (uses CHR/CAL/LOG)
**Stage:** *design‑time* (authoring & registration) with a *run‑time* selector facade (policy‑governed; edition‑aware)
**Primary hooks:** G.1 CG-Frame Card, G.2 SoTA Synthesis Pack, G.3 CHR authoring, G.4 CAL variants, **KD‑CAL** (C.2), **Trust & Assurance** (B.3), **Formality F** (C.2.3), **USM / Scope (G)** (A.2.6), **Bounded Contexts & Bridges with CL** (Part F + B‑patterns), **SCR/RSCR** (F.15), **NQD‑CAL** (C.18), **E/E‑LOG** (C.19), **SoS‑LOG** (C.23), **ATS (E.11)** (AH‑1..AH‑4; GateCrossings), **G.6 Evidence Graph (PathId)**, **UTS & Naming** (F.17–F.18), **Guard‑Rails E.5.1–E.5.3** (no tool lock‑in, unidirectional dependency), **CSLC** (A.18).

### 1) Intent

Provide a **notation‑independent** architecture to register **families of methods** (LOG bundles) and to **select, combine, or fall back** among them for a concrete problem instance—*given typed characteristics (CHR), admissible calculi (CAL), and trust constraints (F–G–R).* The pattern embraces **No‑Free‑Lunch** realities: *there is no universal best method*, so selection is **trait‑ and evidence‑aware**, under explicit **explore↔exploit** policy. The selector returns a **Pareto set** and explicit **abstain/degrade** outcomes under **No‑Free‑Lunch**, governed by the **E/E‑LOG** policy lens. Optionally, the selector operates in **Quality‑Diversity (Illumination)** and **Open‑Ended Family** modes that (co‑)evolve solver families and, when registered, their task/environments; both modes remain **notation‑independent** and policy‑governed.

### 2) Problem frame

You have executed **G.1** (CG-Frame Card) and **G.2** (SoTA Synthesis Pack), which surfaced **rival Traditions and operator palettes**. **G.3/G.4** produced *candidate* CHR/CAL content. You now need a **registry and dispatcher** that:
(a) keeps Traditions **disjoint** yet comparable; (b) chooses a **method family** at run time from typed evidence **without collapsing semantics** across Contexts; (c) publishes names and obligations to **UTS**. 

### 3) Problem

How to design a **general, auditable selector** that:

* prefers **well‑matched** methods for a task instance (shape, noise, constraints) *without* hard‑coding an algorithmic dogma;
* respects **Bounded Contexts**, using **Bridges + CL** only when crossing (with penalties routed to **R**, never **F**);
* explains *why* a choice was made and **how much trust** it buys (F–G–R) with a **SCR**;
* remains free of **tooling jargon** and **implementation bias** at the Core level.   

### 4) Forces

* **Pluralism vs. dispatchability.** Competing Traditions expose different invariants; the selector must compare **without semantic flattening**.
* **Evidence vs. formality.** **F** shapes expression rigor; **R** tracks support; **G** is scope—**orthogonal** yet interacting under composition. 
* **Local semantics vs. reuse.** Cross‑Context reuse requires **Bridges** with **CL** and **loss notes**; penalties hit **R_eff**, not F. 
* **Exploration vs. exploitation.** Run‑time must sometimes **probe alternatives** (NQD/E‑E), but within declared **risk envelopes**.

### 5) Solution — *Dispatcher & Registry chassis*

**Selection kernel.** Apply **lawful orders only**; for partial orders **return a set** governed by **`PortfolioMode ∈ {Pareto | Archive}`** (default **Pareto**; **Archive** when QD is active), no forced scalarisation; **unit/scale mismatches fail fast**. **Default `DominanceRegime = ParetoOnly`; inclusion of Illumination in dominance requires an explicit `CAL.Acceptance` policy and its policy‑id recorded in SCR.** Eligibility/Acceptance are **tri‑state**; unknowns behave per MethodFamily policy (**pass**/**degrade**/**abstain**) and are logged in **SCR** **together with MinimalEvidence verdicts for each referenced characteristic**; **gate additionally by CG‑Spec.minimal_evidence** (by Characteristic id) before applying orders. **SoS‑LOG rule sets (C.23) are the executable shells consumed here**; any **maturity floors** are enforced via **CAL.AcceptanceClause** (not by LOG). **Maturity is an ordinal poset; no global scalarisation is permitted in Core.**

**Strategizing escalation.** When no admissible `MethodFamily` exists for the declared `TaskSignature`, the selector **MUST NOT fail closed**; it **SHALL** return an **empty `CandidateSet`** together with a **`Run‑safe Plan`** that includes an **`ActionHint=strategize`** (C.23 branch‑id), and—where registered—a **`GeneratorFamily`** stub (`EnvironmentValidityRegion`, `TransferRulesRef`). This escalates to **method creation/selection** under **E/E‑LOG**, avoiding ad‑hoc execution.

**Telemetry & parity.** Open hooks for **G.11** (refresh) and **G.9** (parity/baselines). Route **CL penalties → R_eff only**; declare **ReferencePlane** for any claim; **record Φ(CL)/Φ_plane policy‑ids in SCR (Φ MUST be monotone and bounded)**; on plane/context crossings **cite Bridge ids**. When **Illumination** is active, compute and publish **Q (quality), D (diversity), and QD‑score** and the **Archive state**; **IlluminationSummary is a lawful gauge over `Diversity_P`** and **does not enter dominance** unless an explicit **CAL** policy states otherwise **and its policy‑id is recorded in SCR**. **Any increase of Illumination MUST log `PathSliceId`, the active policy‑id, and the active editions of `DescriptorMapRef` and `DistanceDefRef`.**

“Strategy” is a **composition** inside G.5 under **E/E‑LOG** governance; **no new U.Type ‘Strategy’** is minted (**Plain‑register only** per E.10).

**S1 · MethodFamily Registry (design‑time, per CG-Frame)**
Define a **registry row** per *MethodFamily* (e.g., *Outranking*, *CDT*, *Active‑Inference*, *Pareto‑front MOMAs*, *Gradient‑based optimizer*, *RL policy search*), each row comprising:

* **Identity:** local Context, lineage/Tradition, version, **UTS name card**;
* **SolverSignature:** I/O contracts and invariants (types, units, monotonicity), objective kinds, side‑effect constraints;
* **ValidityRegion:** declared TaskClass and tolerances (shape/conditioning/noise) for which guarantees apply; if applicable, **EnvironmentValidityRegion** (for co‑evolved tasks);
* **Eligibility Standard** (typed): required **Object/Task kinds**, **Data shape/regularity traits**, **Noise/uncertainty model**, **Resource envelope**, **Scope prerequisites** (USM claims), **Evidence lanes per KD‑CAL** (e.g., VA/LA/TA) it relies on; **predicates MUST support tri‑state {true|false|unknown} and define a failure policy for `unknown` (degrade/abstain)**. If a “sandbox/probe‑only” route is desired, it MUST be modeled as a distinct **SoS‑LOG** branch (C.23) with a branch‑id and not as a fourth Acceptance status;
* **Assurance profile:** **I/D/S** of the method artefact (e.g., `MethodDescription` vs `MethodSpec` per E.10.D2), **Formality F** anchored to **U.Formality** scale **F0…F9** (C.2.3), expected **R** lane(s), **CL** allowances for cross‑Context operation; **CL penalties SHALL route to R_eff only**;
* **Guarantees:** accuracy/robustness/regret bounds and their preconditions; **EvidenceRefs** to **EvidenceGraph** paths supporting claims;
* **CostModel** and **KnownFailures** (adversarial/degenerate cases);
* **PolicyHooks:** E/E‑LOG knobs (exploration quota, risk budget); optional **EmitterPolicyRef** (C.19) when Illumination is used;
* **BridgeUsage:** declared Bridges and **CL** allowances with loss notes for any cross‑Context transfer;
* **Twin‑naming (E.10):** **Tech:** `U.DescriptorMapRef`; **require `d≥2` only when QD/illumination surfaces are active** (otherwise `d≥1` is lawful); **Plain twin:** `CharacteristicSpaceRef`. **Aliases between them are forbidden** (distinct objects);
* When Illumination is used, declare `U.DescriptorMapRef.edition` and **pin all QD metrics to it**, together with **`DistanceDefRef.edition`** (diversity metric) and **`DHCMethodRef.edition`** to ensure reproducible fronts;
* **InsertionPolicyRef** for archives (elitist replacement, **K‑capacity**, dedup/tie rules);
* **Proof obligations** (what must be established before/after selection).
* **Artefacts:** list **MethodDescription** ids (UTS); where harnessed, also **MethodSpec** ids; cross‑Context reuse requires Bridges + CL.

  All fields are **Core‑level concepts**; concrete notations live in Tooling per **E.5.1–E.5.3**. Publish to **UTS** with twin labels and loss notes if bridged. 

**S1′ · GeneratorFamily Registry (design‑time, Open‑Ended mode)**
Register **GeneratorFamily** (POET/Enhanced‑POET‑class) entries that (co‑)evolve **tasks/environments** and solvers. Each row declares:
* **GeneratorSignature** (I/O, state, budget semantics), **EnvironmentValidityRegion**, **TransferRules** (when/what to transfer across environments) with **`TransferRulesRef.edition` (mandatory in OEE mode)**, **CoEvoCouplers** (which MethodFamilies co‑evolve), **Stop/Refresh** conditions;
* **SoS‑LOG/Acceptance hooks** (discipline‑level gates for validity of generated tasks); any thresholds live in CAL.Acceptance (not LOG);
* **Publication shape:** the selector returns portfolios of pairs `{Environment, MethodFamily}` with their **Eligibility/Assurance** and **PortfolioMode**; telemetry records **coverage/regret** and **IlluminationSummary** (**edition‑aware**, pinned to `DescriptorMapRef.edition` and `DistanceDefRef.edition`).

**S2 · TaskSignature & Trait Inference (design‑time + run‑time)**
A **TaskSignature** is a *minimal typed record* the dispatcher consumes:
`⟨Context, TaskKind, KindSet:U.Kind[], DataShape, NoiseModel, ObjectiveProfile, Constraints{incl. ResourceEnvelope}, ScopeSlice(G), EvidenceGraphRef, Size/Scale, Freshness, Missingness, PortfolioMode⟩`. Values are **CHR‑typed** (Characteristics/Scales/Levels/Coordinates per MM‑CHR discipline) with provenance. Traits may be **inferred** from CHR/CAL bindings (e.g., *convexity known? differentiable? ordinal vs interval scales?*) and from **USM** scope metadata. **When Illumination is active**, extend with `QualityDiversity: {DescriptorMapRef (Tech; d≥2), CharacteristicSpaceRef (Plain twin)}`, `ArchiveConfig (grid/CVT cells)`, `EmitterPolicyRef`, `InsertionPolicyRef`, `DistanceDefRef.edition`, `Q‑budget/D‑budget`. Descriptor and space are distinct objects (no aliases) and must be provided as twins.
**Design/Run hygiene.** No mixed‑stance signatures; Tier crossings publish Bridge+UTS and record **Φ(CL)/Φ_plane** ids.
**UnknownHandling:** all fields admit `unknown` (tri‑state {true|false|unknown}); **Missingness semantics MUST align with CHR.Missingness** (MCAR/MAR/MNAR or mapped equivalents) and be honored by Acceptance/Flows.

**S3 · Selection Kernel (run‑time, policy‑governed)**
**No‑Free‑Lunch is enforced**: choose Tradition/Operator sets from the SoTAPaletteDescription conditioned on task/object/CHR preconditions, rather than by “universal” cross‑Tradition formulas in CG‑Spec. Selector decisions MUST cite palette entries and CHR/CAL constraints used. **CG‑Spec MUST NOT override this with one‑size‑fits‑all formulas.**

The selector MUST:

(1) read SoTAPaletteDescription,
(2) filter Traditions by CHR preconditions and KD‑CAL lane fit,
(3) pick operators consistent with declared scales and taboos,
(4) emit a rationale with links to palette entries and Worked Examples.

A **pure selector** computes a **CandidateSet** with an **admissible (possibly partial) order** (no illegal cross‑scale scoring) and constrained by an *AssuranceGate*:

1. **Eligibility filter:** `MethodFamily` passes iff all **Eligibility Standard** predicates hold **and** all **CG‑Spec.MinimalEvidence** gates for referenced characteristics are met; **if CG‑Frame uses NQD, enforce `ConstraintFit=pass` before front selection**; otherwise **abstain**. Where a “sandbox/probe‑only” route is intended, express it via a dedicated **SoS‑LOG** branch (C.23) with a branch‑id; Acceptance remains tri‑state {pass|degrade|abstain}.
2. **CG‑Spec gate:** require all **CHR characteristics** referenced by Acceptance/Flows to meet the **CG‑Spec.minimal\_evidence** in the current Context; otherwise **abstain** under E/E‑LOG. If a probe‑only path is needed, route via a dedicated **SoS‑LOG** branch (C.23).
3. **Admissible preference:** apply **lexicographic** precedence over lawful traits (e.g., *assumption fit* ≻ *evidence alignment* ≻ *resource/cost*). **Weighted sums across mixed scale types (ordinal vs interval/ratio) are forbidden**; prefer lexicographic/medoid/median where lawful; **any unit/scale conversions MUST be proven legal via CSLC (A.18) before aggregation**.
4. **F–G–R aware gating:** compute **R_eff** with **Γ‑fold** (default = weakest‑link; **override only if CAL/EvidenceProfile supplies an alternative with proofs of monotonicity & boundary behavior**) and apply **CL** penalties (R_eff only; F and G invariant); block candidates failing *minimum R*; **record Γ‑fold contributors explicitly in SCR**. **F** is read from method formalisation level; **G** from **USM** slice; penalties **never alter F**. 
5. **Partial‑order handling:** if after gating the order is not total, **return a Pareto (non‑dominated) set** and explain tie‑criteria in DRR/SCR; do not force a total order via illegal scalarization.
6. **Explore↔Exploit policy:** under **E/E‑LOG**, admit a quota of **NQD‑emitted** alternatives (guarded by risk budgets) to avoid local optima; log probes and outcomes for **refresh**. In **Illumination** mode, selection produces/updates an **Archive** (cells/niches) and computes **Q/D/QD‑score** per edition; ordering within a niche remains lawful (lexicographic/median), never cross‑scale weighted sums.

**S4 · Composition & Fallbacks (design‑time templates)**
Provide templates for **composed strategies**: (i) *pre‑conditioners* (e.g., rescale/denoise), (ii) *meta‑selectors* (e.g., *small‑n* vs *large‑n* switch), (iii) *cascade fallbacks* on **Assurance failure** (e.g., degrade objective from cardinal to ordinal when CHR forbids interval arithmetic). Guard with **CSLC (A.18)** for **unit/scale legality**; **disallow illegal ordinal arithmetic**.
Add a **Verifier stage**: on run‑time preconditions failing or **evidence freshness** expiring, trigger the next lawful fallback; emit DRR/SCR deltas.

**S5 · Publication & Telemetry**
Each selection produces a **Decision Rationale Record (DRR)** + **SCR**, citing chosen family, **why**, **CG‑Spec ids and characteristics consulted with MinimalEvidence verdicts (per characteristic & lane)**, **Γ‑fold contributors**, **ReferencePlane & CL^plane usage**, **CL penalties**, expected **R_eff**, and any **explore** probes. Register the family and selection policy to **UTS** **with twin labels and loss notes where bridged**; provide **RSCR** parity/regression tests as conformance artefacts. **Record on‑policy outcomes and off‑policy regret signals via telemetry (G.11)** to support registry refresh.  

**If Illumination is active,** also publish **IlluminationSummary** (Q/D/QD‑score, Archive snapshot, coverage/regret) and `DescriptorMapRef.edition` with `DistanceDefRef.edition`/`DHCMethodRef.edition`; in **Open‑Ended** mode publish `{Environment, MethodFamily}` portfolios with their coverage **and record `TransferRulesRef.edition`**. **Exports also include:** a **Dispatcher Report** (candidates and reasons in/out), a **Portfolio Pack** (_Pareto set_ + tie‑break notes), and a **Run‑safe Plan** (flows + legality proofs).

For any **Illumination increase**, telemetry **MUST** record the **`PathSliceId`**, the **active policy‑id**, and the active **editions** of `DescriptorMapRef` and `DistanceDefRef`; **in Open‑Ended (GeneratorFamily) mode it MUST also record `TransferRulesRef.edition`**. These **MUST** be visible to **RSCR** triggers.

**S6 · Governance & Evolution**

* **Unidirectional dependency:** Registry and selector are Core patterns; implementations are Tooling; tutorials are Pedagogy.
* **Change control:** versioned entries; deprecations flow through **Lexical Continuity** and **Worked‑Examples** refresh.

> **Julia‑style specialisation (design idiom).** Use **trait‑like dispatch** and **parametric specialisation** *at the level of typed Standards*, not code, to keep selection semantics **portable** across languages and stacks. The Core remains **notation‑independent**.

### 6) Interfaces — minimal I/O Standard

| Interface                | Consumes                                                | Produces                                                                      |
| ------------------------ | ------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **G.5‑1 RegisterFamily** | SoTA row(s) from **G.2**, CHR/CAL stubs (G.3/G.4), Context | `MethodFamily` record (eligibility Standard, assurance profile, UTS entry id) |
| **G.5‑2 RegisterGeneratorFamily** | SoTA row(s) from **G.2**, Context | `GeneratorFamily` record (GeneratorSignature, EnvironmentValidityRegion, TransferRules **(+ TransferRulesRef.edition in OEE)**, CoEvoCouplers, Acceptance hooks) |
| **G.5‑3 Select**         | `TaskSignature`, policy (E/E‑LOG), **SoS‑LOG rules (C.23)**, acceptance clauses   | `CandidateSet` with admissible (possibly partial) order; **return a set per `PortfolioMode`** (Pareto or Archive) when the order is non‑total; chosen `MethodFamily`; **DRR + SCR** (F–G–R/CL, **ReferencePlane & Φ ids**); **Portfolio Pack** (return mode + tie‑break notes); **Run‑safe Plan** (flows + legality proofs); **if no candidate is admissible**, emit `ActionHint=strategize` (with responsible **C.23 branch‑id**) and **MAY** include a minimal `GeneratorFamily` stub (EVR + `TransferRulesRef.edition`) for lawful exploration under **E/E‑LOG**. |
| **G.5‑4 Compose**        | `CandidateSet`, composition template                    | Composite strategy spec (with legality checks)                                |
| **G.5‑5 Telemetry**      | Outcomes, probes                                        | Registry refresh cues; RSCR deltas; (if Illumination) Q/D/QD‑score + Archive deltas + `DescriptorMapRef.edition`/`DistanceDefRef.edition`/**`CharacteristicSpaceRef.edition` when a domain‑family coordinate is declared per C18‑1b**, **`PathSliceId`**, **policy‑id**; (if Open‑Ended) coverage/regret per `{Environment, MethodFamily}` |

### 7) Conformance Checklist (normative)

**CC‑G5.0** Core Standards **SHALL** remain notation‑independent; vendor/tool keywords are forbidden in eligibility or assurance fields (E.5.1–E.5.3).
**CC‑G5.1** Every `MethodFamily` **SHALL** declare an **Eligibility Standard** using CHR terms; Standards **SHALL NOT** rely on tool‑specific keywords.
**CC‑G5.2** Selection **SHALL** be a **pure function** of `TaskSignature` + policy; side effects limited to DRR/SCR emission.
**CC‑G5.3** Cross‑Context use **MUST** cite a **Bridge** with **CL**; penalties **MUST** flow to **R_eff**; **F** and **G** remain invariant; **attach a loss note**. 
**CC‑G5.4** The selector **MUST** **default** to the **weakest‑link** rule for **R_eff** and record contributors in **SCR**; it **MAY** use an alternative Γ‑fold **only** when provided by CAL with proof obligations satisfied (monotonicity, boundary behavior).
**CC‑G5.5** Ordinal scales **MUST NOT** be averaged/subtracted; unit/scale legality **MUST** be enforced by CHR guards.
**CC‑G5.6** Chosen families **SHALL** be published to **UTS** with twin labels and scope notes; deprecations follow F.13.
**CC‑G5.7** Exploration **MUST** be budgeted under **E/E‑LOG**; probe outcomes **MUST** feed refresh.
**CC‑G5.8** **CG‑Frame gate enforced.** Selection rejects candidates that do not meet **CG‑Spec.minimal_evidence** for the characteristics they use; **Maturity floors** (if present) are enforced via **AcceptanceClauses**.
**CC‑G5.9** **Admissible ordering.** Candidate ordering **MUST** be lexicographic or otherwise lawful over CHR‑typed traits; **weighted sums across ordinal/interval/ratio mixes are forbidden**. If only a partial order is available, **return a Pareto set**.
**CC‑G5.10** **SCR completeness.** SCR **MUST** enumerate Γ‑fold contributors, **CG‑Spec characteristics** used, and **MinimalEvidence gating verdicts** (by lane & carrier).
**CC‑G5.11** **Tri‑state eligibility.** Eligibility predicates **MUST** define behavior for `unknown` (**degrade/abstain**); **unknowns propagate into Acceptance decisions**; silent coercion to `false` is forbidden. Any “sandbox/probe‑only” handling MUST be modeled as a dedicated **SoS‑LOG** branch (C.23) with a branch‑id, not as a fourth Acceptance status.
**CC‑G5.12** **No “universal” cross‑Tradition scoring.** Cross‑Tradition selection **MUST NOT** rely on a single numeric formula not justified by CHR/CAL and CG‑Spec.  Enforce heterogeneity gate: FamilyCoverage ≥ 3 and MinInterFamilyDistance ≥ δ_family for triads/portfolios that claim universality; cite **Context Card id (F.1)** in DRR/SCR.
**CC‑G5.13** The selector **MUST NOT** recompute Acceptance thresholds or Maturity floors; it **consumes** `AdmissibilityLedger@Context` rows (C.23) and **cites** the referenced clause/rung ids in SCR.
**CC‑G5.14** **Φ(CL) and (where applicable) Φ_plane MUST be monotone and bounded, and published in CG‑Spec;** SCR **MUST** record the policy‑id in use.
**CC‑G5.15** **Units/scale legality MUST be proven via CSLC (A.18) before any aggregation or Γ‑fold;** unit/scale mismatches fail fast. *(Complements CC‑G5.5 on ordinal arithmetic.)*
**CC‑G5.16** **Hidden thresholds are forbidden.** All thresholds live in **AcceptanceClauses** (not in CHR, LOG, or code).
**CC‑G5.17** **ReferencePlane MUST be declared for any claim and noted in SCR,** including **CL^plane** usage for plane crossings.
**CC‑G5.18** **Numeric comparisons/aggregations MUST cite a lawful CG‑Spec SCP with declared Γ‑fold;** cross‑Context reuse **requires Bridge + CL**, with penalties routed to **R_eff** only (never **F**).
**CC‑G5.19** **Illumination triad.** When Illumination is active, **Q, D, and QD‑score MUST be computed and published** with Archive state; **Illumination is excluded from dominance unless explicitly enabled by policy.**
**CC‑G5.20** **Gauge semantics.** **IlluminationSummary SHALL be treated as a gauge over `Diversity_P`**; inclusion in dominance requires an explicit **CAL** policy with a recorded **policy‑id** in SCR.
**CC‑G5.21** **Archive reproducibility.** Any use of archives **MUST** declare **`InsertionPolicyRef`** (replacement, **K‑capacity**, dedup/tie rules) and record **`DistanceDefRef.edition`** and **`DHCMethodRef.edition`**; **`DescriptorMapRef.edition` MUST** be logged in telemetry; **all QD metrics SHALL be pinned to `DescriptorMapRef.edition`**.
**CC‑G5.22** **Twin‑naming (E.10).** Use **Tech** `U.DescriptorMapRef` (d≥2) with **Plain twin** `CharacteristicSpaceRef`; **aliases are forbidden** (they are distinct objects).
**CC‑G5.23** **Portfolio mode.** The selector **MUST** expose **`PortfolioMode ∈ {Pareto | Archive}`** (**default = Archive**) and echo it in DRR/SCR and the Portfolio Pack; ε‑fronts are allowed as *local* decision aids under CG‑Spec.
**CC‑G5.24** **Open‑Ended portfolios.** In Open‑Ended mode, the selector **MUST** return portfolios of `{Environment, MethodFamily}` pairs; **EnvironmentValidityRegion** and **TransferRules** **MUST** be declared; SoS‑LOG/Acceptance branches govern validity of generated tasks.
**CC‑G5.25** **Transfer rules edition (OEE).** In OEE mode, **`TransferRulesRef.edition` is mandatory** and **MUST** be visible to Telemetry and **RSCR** triggers.
**CC‑G5.26** **Lawful ordering in niches.** Within any archive niche/cell, ordering **MUST** be lawful (lexicographic/medoid/median over compatible scales); **weighted sums across mixed scale types are forbidden**.
**CC‑G5.27** **ATS visibility.** Tier/context crossings **MUST** be visible to ATS (E.11) (AH‑1..AH‑4); violations are fail‑fast defects of publication.
**CC‑G5.28** **Dominance policy default.** `DominanceRegime` **SHALL** default to `ParetoOnly`; inclusion of illumination in dominance **MUST** be explicitly authorised by **CAL.Acceptance** (`ParetoPlusIllumination`) with the policy‑id recorded in SCR; **parity‑run publication (CC‑G5.23a) remains mandatory** irrespective of dominance policy.
**CC‑G5.29** **Illumination increase logging.** Any **increase in Illumination** **MUST** log `PathSliceId`, **policy‑id**, and the active **`DescriptorMapRef.edition`/`DistanceDefRef.edition`** in telemetry and expose them to **RSCR** triggers; **in Open‑Ended (GeneratorFamily) mode, `TransferRulesRef.edition` MUST also be logged.**
**CC‑G5.30** **No Strategy minting (centralised).** “Strategy/policy” are **compositions** governed by **E/E‑LOG** and published via **G.5.Compose**; **no new `U.Type` “Strategy”** may be minted by other Part G patterns.
**CC‑G5.31 (Strategy hint on non‑admissible sets).** If selection yields **∅** under the active SoS‑LOG and Acceptance, the selector **SHALL** emit `ActionHint=strategize` with the responsible **C.23 branch‑id** and **MAY** include a `GeneratorFamily` stub (EVR + `TransferRulesRef.edition`) to guide exploration under **E/E‑LOG**.
**CC‑G5.32** **Parity‑run publication.** A selector/generator **MUST** publish an **Illumination Map** (archive topology + coverage per niche with `DescriptorMapRef`/`DistanceDefRef.edition`). **Single‑score leaderboards are forbidden**; any roll‑up **MUST** be lawful under **CG‑Spec** (no mixed‑scale sums).

### 8) Consequences

* **Auditable plurality.** Rivals co‑exist, selected with **explainable** trust and scope handling.
* **Safety by construction.** Illegal measurements and cross‑Context leaks are blocked by Standard and CL penalties. 
* **Evolvability.** Families can be **added/retired** without rewriting the selector; UTS provides a stable publication surface.

### 9) Worked micro‑examples (indicative)

**9.1 Decision Theory (multi‑Tradition)**
`TaskSignature:` *one‑shot, high‑stakes, observational dataset; causal graph partially known; counterfactuals needed; ordinal preference ordering only in some panels; strict risk constraint.*

* Eligibility filters admit **CDT** (needs counterfactuals), **EDT** (if evidential suffices), **Active‑Inference** (if a generative model with variational free energy is in scope), and **reject cardinal EU** where CHR shows *ordinal‑only* preferences.
* CL appears if a *psychological Context* Bridge is used for utility elicitation; selector applies **CL penalty** to **R_eff** only; **F** remains the method’s declared formalism level. **DRR** explains the choice (CDT) and logs an **NQD** probe of *Active‑Inference* under small budget. 

**9.2 Creativity (portfolio search)**
`TaskSignature:` *wide design space; resource cap; novelty emphasis; diversity quota.*

* Registry offers **Pareto‑front NQD** and **IPO‑style recombiners**; **E/E‑LOG** sets an explore‑heavy policy initially, then shifts to exploit on observed Use‑Value. **SCR** reports that Use‑Value evidence is **LA** lane while novelty scoring rests on **VA** heuristics. 

**9.3 Quality‑Diversity & Open‑Ended (GeneratorFamily portfolios)**  
`TaskSignature:` *co‑evolving task family; descriptor map d≥2; risk‑budgeted exploration; environment shifts allowed; strict ConstraintFit gate; freshness windows active.*

* **Registry (design‑time).** Register a **GeneratorFamily** of the **POET/Enhanced‑POET (and compatible DGM‑class)** with  
  `EnvironmentValidityRegion := {grid mazes with dynamic doors; hazard_intensity ≤ L2; size ≤ 50×50}`,  
 `TransferRules (+ TransferRulesRef.edition) := {transfer policy when ConstraintFit=pass; else abstain; reset if MinInterFamilyDistance < δ}`,  
  `CoEvoCouplers := {RL‑policy‑search, CMA‑ME planner}`; attach **SoS‑LOG/Acceptance** branches for validity of generated tasks (no lethal hazards; budget ≤ envelope). *CL penalties route to R_eff only; F/G stay invariant; ReferencePlane is recorded on every claim.*

* **Selection (run‑time).** The dispatcher reads the SoTA palette and CAL gates, applies **ConstraintFit=pass** as a hard eligibility filter, then produces a **portfolio of pairs** `{Environment, MethodFamily}`:  
 – a **Pareto/Archive** (per `PortfolioMode`) over niches (quality/diversity lawful order; no forced scalarization),  
  – ε‑Pareto thinning when applicable,  
  – ties broken by lawful lenses only. *Illumination does **not** enter dominance unless policy explicitly promotes it.*

* **Policy (E/E‑LOG).** Use a named **lens** `Barbell` with `explore_share ≈ 0.4`, `wild_bet_quota = 2`, `backstop_confidence = L1`; cite `EmitterPolicyRef` (UCB‑class, moderate τ). Record the **lens id** and **policy‑id Φ** in provenance.

* **Telemetry & publication.** Emit **DRR+SCR** with: CG‑Spec characteristics consulted and MinimalEvidence verdicts (by lane), Γ‑fold contributors, ReferencePlane/CL^plane usage, CL penalties→R_eff, selected `{Environment, MethodFamily}` portfolio, and probe logs. Publish **IlluminationSummary** with `Q/D/QD‑score`, Archive snapshot, and **DescriptorMap edition** (`{DHCMethodRef.edition, DistanceDef}`); for open‑ended mode also publish **coverage/regret per {Environment, MethodFamily}**. Register families and policies to **UTS** (twin labels; loss notes where bridged).


### 10) Relations

**Builds on:** G.1–G.4; **F–G–R / KD‑CAL**; **Formality F**; **USM**; **Bridges & CL**; **Guard‑Rails E.5.\***.    
**Publishes to:** **UTS**, Worked‑Examples, RSCR.
**Constrains:** any run‑time *selector implementations* (Tooling) via the Core Standards.

### 11) Editorial notes (authoring guidance)

* Keep **Standards minimal** and **typed**; resist adding tool‑level flags to the Core (route to Tooling Glossaries).
* Treat **composition patterns** as first‑class (preconditioner → solver → verifier); publish each as a **UTS row** with clear Contexts.
* When a selection *raises F* (e.g., recasting acceptance as predicates), record **ΔF** separately from **ΔG/ΔR**.

### 12) Quick author checklist

1. Register ≥ 3 **MethodFamilies** per competing Tradition with typed **Eligibility** and **Assurance**.
2. Define the **TaskSignature** schema for the CG-Frame; prove it is **minimal** but **sufficient** for dispatch.
3. Implement **Selection Kernel** as a pure Core algorithm; ensure **CL penalties** and **weakest‑link R** are computed and logged in **SCR**.
4. Publish families and selection policy to **UTS**; add one **Worked‑Example** per policy branch.
5. Provide **RSCR** parity/regression tests as conformance obligations; ensure telemetry hooks (G.11) are connected.
