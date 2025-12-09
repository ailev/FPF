# **Part E · FPF Constitution and Authoring Cluster**

### Section E‑I · The FPF Constitution

#### Pattern E.1 — Vision & Mission: “Operating System for Thought”  \[A]

##### Problem frame
Modern engineering, science, and strategy all suffer from **conceptual overload**: dozens of domain tools, drifting vocabularies, and disconnected “best practices” splinter ideas as they travel from napkin sketch to certified deliverable. Stakeholders—*Engineers, Researchers, Learners*—lack a single, evolvable scaffold that can carry an insight across that span.

##### Problem
Absent such a scaffold, every discipline re‑invents epistemology and systems thinking, spawning silos, steep learning curves, and brittle life‑cycle models. Previous attempts either froze agility in rigid hierarchies or dissolved rigour in tool‑centric jargon.

##### Forces

| Force                           | Tension                                                                 |
| ------------------------------- | ----------------------------------------------------------------------- |
| **Conceptual Unity**            | Freedom to evolve ↔ invariant principles that prevent vocabulary drift. |
| **Rigor vs Agility**            | Formal verifiability ↔ rapid, iterative exploration.                    |
| **Universality vs Specificity** | Domain‑agnostic kernel ↔ problem‑specific leverage.                     |
| **Didactic Clarity**            | Human comprehension ↔ abstract purity and density.                      |
| **Physical Grounding**          | Abstract constructs ↔ a *material Transformer* that proves feasibility.     |

**Mission Statement**

> *Enable any motivated system/actor/agent/transformer — human or AI — to transform a raw idea into a reproducible, auditable change in the physical world through incremental, falsifiable cycles.*

**Vision Statement**

> *Reliable reasoning should be as accessible as version control: clone the conceptual kernel, extend it with domain plugins, and commit decisions that remain traceable across time, scale, and discipline.*

##### Solution — *FPF as an Operating System for Thought*
FPF delivers a **generative scaffold** realised as:

1. a **micro‑kernel** of non‑derivable, cross‑domain **first principles**;
2. pluggable **architheories**—Systemic Calculus, Knowledge Dynamics, etc.—that instantiate those principles;
3. a **pattern language** (*Architectural* ► why/ how; *Definitional* ► what) with embedded **Conformance Checklist (CC)**;
4. **Design Rationale Records (DRRs)** that govern safe, auditable evolution;
5. three **core invariants** that every artefact must honour

   * **Evolvability** — change is expected and governed;
   * **Cross‑Scale Coherence** — the same algebra binds parts to wholes at any level;
   * **Didactic Transparency** — each element exposes its own reasoning path.

** Conformance Checklist**

| ID              | Requirement                                                                                                                                          | Rationale                                       |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| **CC‑Vision.1** | Every composite artefact **MUST** cite a *material Transformer* that can, in principle, perform the aggregation (`Γ(D,C)`) that produced it.             | Ensures physical feasibility and auditability.  |
| **CC‑Vision.2** | Every normative rule **MUST** demonstrably support at least one core invariant (*Evolvability, Cross‑Scale Coherence, Didactic Transparency*).       | Keeps the Canon lean and purpose‑driven.        |
| **CC‑Vision.3** | Conceptual text **MUST NOT** contain tokens black‑listed by the **DevOps Lexical Firewall** (`yaml`, `docker`, …).                                   | Preserves layer purity and tool‑agnostic core.  |
| **CC‑Vision.4** | A conformant artefact **MUST** state a measurable benefit for at least one of the three roles (*Engineer, Researcher, Learner*) or justify omission. | Aligns success with stakeholder trajectories.   |

##### Consequences

*Positive* — Unified language accelerates cross‑disciplinary discovery; regulators can audit claim lineages; learners acquire concepts through the spec itself.
*Trade‑offs* — Authors face an initial learning curve and must trace every rule to an invariant; disciplined traceability is required to prevent variant sprawl.

##### Relations & Precedence
Pattern E.1 governs **E.2 Eleven Pillars** and the Guard‑Rail set **A.5–A.8**; any later pattern that conflicts with E.1 **MUST** be revised via a DRR before entering the Canon.

*“Purpose without a scaffold is wishful thinking; a scaffold without purpose is cargo‑cult—FPF welds the two into disciplined imagination.”*


---

## E.11 — Authoring‑Tier Scheme (ATS) \[A]

*Tech token:* `AuthoringTierScheme` (**ATS**).

**Object‑of‑talk.** `AuthoringTierScheme` — an **Episteme (Scheme, kind‑anchored)** that classifies **Authoring Work** into four **AuthoringTier** levels and governs **gate‑crossings**, **evidence lanes**, and **normative separation** between the levels.

**Register & scope.** Kernel pattern in Part E, applicable across FPF and reusable by Part G (architheory authoring) and Part C (discipline patterns), with guards per **E.10 (LEX‑BUNDLE)** and **C.20 §D.DISC**.

### 1) Intent

Provide a **uniform, testable classification Scheme** for acts of authoring in this project, preventing **normative token leakage** between layers of work, and requiring **explicit publication carriers** (`UTS` rows, `BridgeCard`) for any crossing. The scheme aligns with **USM** by treating each tier as a distinct **Work** class and with **E.10** by enforcing head‑anchored naming and I/D/S morphology.

**Wiring.** ATS is explicitly wired to **A.4 (Temporal Duality & Open‑Ended Evolution Principle)** and **B.4 (Observe→Refine→Deploy)**; the cognitive engine for authoring acts is **B.5/B.5.1 (Explore→Shape→Evidence→Operate)**. Keep **Working‑Model first (Tell–Show–Show)** to avoid gratuitous formalism (per **E.8**). **Telemetry/refresh is consumed by G.11 (PathSlice, decay, edition) via H2–H4/H7/H11 hooks.**

### 2) Problem

Without a disciplined tiering of authoring work:

* **Kinds blur** (execution vs design vs architheory vs meta‑authoring).
* **Tokens leak** (a result minted at one tier is used as if normative at another).
* **Evidence lanes** become non‑comparable; **CL (cross‑context loss)** is unmanaged.
* **“Domain” labels** are mistaken for governance, and job‑title language creeps into kernel tokens.

### 3) Forces

* **Separation of concerns.** Translation from applied problems to transdiscipline tasks must be distinct from architheory authoring and from meta‑authoring.
* **Evidence comparability.** Evidence must run in **lanes** with **CL penalties** recorded and routed.
* **Publication accountability.** Cross‑tier reuse must be visible on **UTS** with **Bridge** entries.
* **Lexical hygiene.** Head‑anchoring, I/D/S morphology, and Role/Holder/Carrier separation must hold across all tiers.
* **Discipline vs Domain.** `U.Discipline` governs comparability **via CG‑Spec**, while **Domain** is catalog‑only and stitched to **D.CTX + UTS**.

### 4) Solution — the Scheme

#### 4.1 The four **AuthoringTier** levels (Tech heads; Plain twins in italics)

**AT0 — `AppliedWork`** *(Plain twin: “Applied‑run”)*

* **Work kind.** Execution of applied methods on situated problems, **outside** FPF’s transdiscipline scope.
* **Typical outputs.** `RunObservation` *(run artefact; cf. `Observation`)*, `WorkLogCarrier`, optional `RunbookMethodDescription`.
* **Normative status inside FPF.** **Non‑normative** to higher tiers; may **inform** AT1 through a **`BridgeCard`** with CL notes.

* **Roles.** `ExecutorRole`, `OperatorRole`; **Holders** are concrete holons (teams/systems).
* **Conformance note.** AT0 tokens **MUST NOT** assert norms for AT1–AT3; **`Work` stays execution‑only**, plans/logs/recipes are modeled as `WorkPlan`/Carriers/`MethodDescription`.

**AT1 — `TransdisciplineDesignWork`** *(Plain twin: “Transdiscipline‑design work”)*

* **Work kind.** Translation of applied problems into **Tasks** and **SoTA‑about‑methods**: methods **about** applied methods.
* **Typical outputs.** `TaskPack`, `TranslationMethodDescription`, `DesignRationaleDescription`.
* **Normative status.** Normative **within AT1**; AT1 tokens **MAY** cite AT0 only through **BridgeCard** with CL captured.
* **Roles.** `DesignerRole`, `TranslatorRole`; **Holders** typed to a `U.BoundedContext`.
* **Scope relation to C.20.** When AT1 uses a discipline, name it as `U.Discipline` (Holon) and place comparison rules in its **CG‑Spec**; **no norms on Domain labels** (stitch Domain mentions to **D.CTX + UTS**).

**AT2 — `ArchitheoryAuthoringWork`** *(Plain twin: “Architheory‑authoring”)*

* **Work kind.** Production of the **SoTA Architheory Pack** used in Part G authoring.
* **Typical outputs.** `ArchitheoryPack`, `GaugeSpec`, `InvariantSetDescription`, `BridgeCard` (AT1↔AT2).
* **Normative status.** AT2 defines the **architheory norm set** (CAL/CHR/LOG) that **feeds** F/G reasoning; it **does not mutate Kernel types** and respects **unidirectional meaning** (Kernel → Architheory → Context → Instance).
* **Portfolio‑aware constraint.** AT2 **MUST** treat **“one signature → many specialisations”** as the norm: do **not** embed **global thresholds** or **forced scalarisations** inside architheory text; selection remains **set‑valued** (Pareto/Archive) under **G.5**, with dominance governed by **CAL** policies. Any maturity floors **SHALL** be expressed via **`CAL.AcceptanceClause`** (clause id cited), not inside LOG.
* **Roles.** `AuthorRole`, `AssessorRole` (review within AT2), `StewardRole` (pack upkeep).
* **Cross‑tier references.** Cite AT1 only through a `BridgeCard` with CL captured **and a matching UTS row**.
* **Evidence.** Publishes **UTS rows** for visibility and **BridgeCard** for any cross‑tier references.

**AT3 — `MetaAuthoringWork`** *(Plain twin: “Meta‑authoring”)*

* **Work kind.** Organisation and governance of AT2 work (e.g., editorial coordination).
* **Typical outputs.** `CoordinationFlowDescription`, `AuthoringPolicySpec`, `PublicationPlanDescription`.
* **Normative status.** AT3 **organises** but **does not overrule** AT2 invariants; under **KD‑CAL/B.3**, AT3 **MUST NOT** alter AT2 **F/G invariants** nor introduce cross‑lane mutations; it sets **how** AT2 is executed, not **what** architheory is true.
* **Roles.** `CoordinatorRole`, `EditorRole`, `DisciplineStewardRole` (if a `U.Discipline` is orchestrated).
* **Evidence.** Publishes **UTS rows** for visibility and **BridgeCard** for any cross‑tier references.

> **USM alignment.** Each AT\* is a **Work** class (USM *act*). Tokens produced at a tier are **typed** to that tier’s Work class and **obey E.10** lexical governance.

#### 4.2 Tiering for autonomy budgets & guards
* **AT0/AT1** (application/bridge authors): may **use** existing `AutonomyBudgetDecl` and `Aut-Guard policy-id` and populate UTS fields; **MUST NOT** create new guard policies.
* **AT2** (architheory users): may **author** context‑local `AutonomyBudgetDecl` that instantiates an existing `Aut-Guard` policy and `OverrideProtocolRef`.
* **AT3** (architheory maintainers): may **mint/modify** `Aut-Guard` policies and **register** `OverrideProtocolRef` speech‑act schemas.
**Gate.** Any UTS row referencing a **new** `Aut-Guard policy-id` without AT3 provenance **fails** ATS checks.

### 5) Gate‑crossings & Evidence lanes

#### 5.1 Gate‑crossing requirement

A **GateCrossing** between tiers (e.g., AT0→AT1, AT1→AT2, AT2→AT3) **MUST** be recorded as:

1. a **`BridgeCard`** linking source tokens to target tokens (with **BridgeId** and **CL** loss notes), and
2. a **UTS row** listing: SourceTier, TargetTier, `ContextId` (from **D.CTX**), **BridgeId**, **bridgeChannel ∈ {Scope, Kind}**, **CL** (and **CL^k** if a **KindBridge** is used) with loss notes, **ReferencePlane** (source/target), **CL^plane** (if planes differ), steward Holder, and twin labels.

**ReferencePlane guard.** When a GateCrossing touches differing planes `{world|concept|episteme}`, compute and publish **CL^plane** (policy‑id + loss note) alongside CL.
* **Evidence.** Publishes **UTS rows** for visibility and **BridgeCard** for any cross‑tier references.

#### 5.2 Evidence lanes & CL routing

**Lane taxonomy (normative).**  
  — **F‑lane (Form):** mechanism‑internal laws (units/coherence, law‑set invariants, type/domain/range). Aggregation default: **min**; unaffected by CL penalties.  
  — **G‑lane (Grounding):** scope coverage and applicability to the declared `PublicationScope`. Aggregation: **intersection along a path; SpanUnion across independent lines**.  
  — **R‑lane (Assurance):** residual risk/assurance accounting; receives **Φ(CL)**/**Ψ(`CL^k`)**/**Φ_plane** penalties (all **monotone, bounded, table‑backed**) that **do not** mutate F/G.  
Materialisation: **SCR/RSCR** carry lane‑split; **UTS rows** cite policy‑ids and `CrossingRef`s; **VALATA** tables provide value annotations; carriers stay referenced via SCR/RSCR.

* **Lane separation.** Keep **Form (F)**, **Grounding (G)**, **Assurance (R)** evidence **disentangled** across all tiers (publish lanes explicitly).
* **CL routing.** Under **KD‑CAL**, **CL/CL^k/CL^plane penalties route to R only** and **MUST NOT** mutate F/G invariants. When planes differ, apply **CL^plane** in the assurance penalty; **Φ(CL)**/**Ψ(CL^k)**/**Φ_plane** MUST be **monotone** and **table‑backed**; publish **policy‑ids** in SCR **and cite them on the UTS row**.
* **Lane provenance.** Each evidence item carries: `LaneId`, `SourceTier`, `ContextId`, `BridgeId` (if imported), **ReferencePlane**, and (if applicable) **CL^plane**.

#### 5.3 Telemetry & Refresh hooks (normative)

* **Sentinel registration.** Every GateCrossing **MUST** register the **BridgeId** on a **PathSlice watch‑list**; edits to **CL/CL^k/CL^plane** or relevant **Φ/Ψ policy‑ids** **MUST** trigger **path‑local RSCR** and schedule **PathSlice** refresh (Γ_time × plane), not pack‑wide reruns.
* **Edition awareness.** Where Bridges reference **`U.DescriptorMapRef`**, **`DistanceDefRef`**, or **`InsertionPolicyRef`** (for archives), any **edition change** **MUST** be published to Telemetry and **MUST** trigger the same path‑local refresh.
* **Dominance policy.** **Illumination/QD signals do not alter dominance by default**; `DominanceRegime` **defaults to `ParetoOnly`**. Participation of illumination in dominance **MUST** be authorised by a **CAL policy** and **MUST** be cited by policy‑id in SCR.
* **Open‑Ended (GeneratorFamily) crossings.** Where a GateCrossing imports evidence from **`GeneratorFamily`** flows (POET‑class) — e.g., **`EnvironmentValidityRegion`** or **`TransferRulesRef`** — **register the BridgeId on the PathSlice watch‑list**; any **`…Ref.edition`** change **MUST** be published to Telemetry and **MUST** trigger a **path‑local RSCR/refresh**. Report **`IlluminationSummary`** as a **gauge**; dominance remains unaffected unless a **CAL** policy promotes it (policy‑id cited).

### 6) Interfaces to **C.20 §D.DISC** and **D.CTX / UTS**

* **Discipline usage.** When referencing a field (e.g., “Transdiscipline”), name it as **`U.Discipline` (Holon)**. Put comparability/aggregation in its **CG‑Spec**; do **not** attach norms to a **Domain** label.
* **Domain as catalog mark.** If “Domain” appears, **stitch** it to an **enumerated set of `U.BoundedContext` ids** (per **D.CTX**) and publish **UTS twins**. **Domain carries zero governance.** **Do not attach TaskSignature governance to Domain**; attach comparability/aggregation norms to the **CG‑Spec of U.Discipline**. C.22 **KindSet** supplies describedEntity; **USM** supplies Scope.
* **Traditions vs “Traditions.”** Sub‑disciplinary “Traditions” appear as **`Tradition`** tokens (Tech). Keep “Tradition” only as a **Plain twin** with a twin‑label.

### 7) Roles, Holders, and Carriers (holonic separation)

* **Role tokens.** `DesignerRole`, `TranslatorRole`, `AuthorRole`, `AssessorRole`, `ReviewerRole`, `CoordinatorRole`, `EditorRole`, `DisciplineStewardRole`.
* **Holders.** Use **`Holder#…Role:ContextId`** to type a role assumption, e.g., `Team‑Alpha is Holder#AuthorRole:Architheory‑Lab‑G`.
* **Carriers.** Use **Carrier** for systems that **bear epistemes**: `ArchitheoryPackCarrier`, `UTSRegisterCarrier`, `BridgeRegisterCarrier`.
* **Canonical rewrites.** Legacy `…CarrierRole` → **`Holder#…Role:Context`** (SCR‑LEX).

### 8) I/D/S morphology (applied here)

* **Intension.** `AuthoringTierScheme` (the Scheme itself).
* **Description.** `AuthoringTierSchemeDescription` (this pattern text).
* **Spec (optional, testable).** `AuthoringTierSchemeSpec` — when acceptance criteria and harnesses per **E.10.D2** are published. See §9.

### 9) Conformance (normative)

**C1 — Head‑anchoring.** All tokens minted under this Scheme **MUST** use explicit heads (`Work`, `MethodDescription`, `Pack`, `Spec`, `FlowDescription`, `BridgeCard`, `…Role`, `…Carrier`) and declare **`LEX.TokenClass`**. Figurative heads (e.g., “Ladder”) are **Plain only** with a 1:1 twin to the Tech token.

**C2 — I/D/S.** Use `…Description` for descriptive texts and `…Spec` only when acceptance criteria + harnesses are declared and executable (per **E.10.D2**).

**C3 — Role/Holon separation.** Use `…Role` for playable intentions; **Holders** assume roles via `Holder#…Role:ContextId`. Keep **Carrier** for systems that bear epistemes. Avoid job titles as kernel heads.

**C4 — Tier containment.**

* **C4.1.** Tokens minted at AT0–AT3 are **scoped** to their tier; **normative content MUST NOT leak** to another tier **without** a `BridgeCard` and **UTS row**.
* **C4.2.** AT3 (MetaAuthoring) **MUST NOT** override AT2 invariants; it may only constrain execution/coordination.

**C5 — Evidence lanes.** Publish F/G/R lanes; **route CL→R only**, record **Φ(CL)** and (if applicable) **Φ_plane**; **no F/G mutation**. Provenance includes **ReferencePlane** on crossings.

**C6 — Domain/Discipline governance.**

* **C6.1.** `U.Discipline` is a **Holon**; comparability rules live in **CG‑Spec**.
* **C6.2.** Any **Domain** mention must include the D.CTX projection and **UTS twins**; **no norms on Domain**.

**C7 — Gate‑crossings.** Every cross‑tier reuse **MUST** provide: `BridgeCard` + `UTS` row (with **ReferencePlane**, **bridgeChannel**, **CL**, **CL^k** *if* `bridgeChannel=Kind`, and **CL^plane** where applicable). No implied crossings.

**C8 — Minimal publication set.**

* AT0↔AT1: `BridgeCard`, `TaskPack` (AT1), CL notes, UTS row.
* AT1↔AT2: `BridgeCard`, `ArchitheoryPack` (AT2), lane mapping, UTS row.
* AT2↔AT3: `BridgeCard`, `CoordinationFlowDescription` (AT3), `AuthoringPolicySpec` (if present), UTS row.

**C9 — ATS harness is blocking.** Failures of **AH‑1..AH‑4** *(Classifier, Gate, Lane, Lexical)* **SHALL** block publication under this Scheme; a non‑conformant crossing **MUST NOT** be consumable by **G.4/G.5**. Record the failure as an **SCR** defect with a remediation note.

**Acceptance harness skeleton (for `AuthoringTierSchemeSpec`).**

* **AH‑1 (Classifier).** A deterministic classifier that maps a candidate **Work** record to {AT0|AT1|AT2|AT3} based on its **object‑of‑talk**, outputs, lane types, and declared Roles.
* **AH‑2 (Gate check).** Given a citation across tiers, verifier **MUST** find a `BridgeCard` and matching **UTS row**; **if `bridgeChannel=Kind`, `CL^k` MUST be present** and **Ψ‑policy id** is visible in SCR.
* **AH‑3 (Lane check).** Verifier **MUST** observe **CL/CL^k/CL^plane → R only**, **F/G invariants unchanged**, and — where planes differ — **CL^plane** presence with **Φ_plane** monotone/bounded and table‑backed; SCR shows **R_eff** as a function of Φ/Ψ terms. **When QD/OEE surfaces are present, edition pins MUST be visible**: `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `CharacteristicSpaceRef.edition` *(if present)*, and (for OEE) `TransferRulesRef.edition`.
* **AH‑4 (Lexical check).** Head‑anchoring + I/D/S + Role/Holon separation checks (SCR‑LEX).

### 10) Structure (informative)

### 10.1 Typing table

| Tier    | Work head (Tech)            | Typical outputs (Tech heads)                                                       | Evidence lane policy                        | Crossing rule                               |
| ------- | --------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| **AT0** | `AppliedWork`               | `RunObservation`, `WorkLogCarrier`, `RunbookMethodDescription`                     | Non‑normative to higher tiers               | `BridgeCard` + UTS for import to AT1        |
| **AT1** | `TransdisciplineDesignWork` | `TaskPack`, `TranslationMethodDescription`, `DesignRationaleDescription`           | CL from AT0 import → **R**                  | `BridgeCard` + UTS for import to AT2        |
| **AT2** | `ArchitheoryAuthoringWork`  | `ArchitheoryPack`, `GaugeSpec`, `InvariantSetDescription`                          | CL from AT1 import → **R**                  | `BridgeCard` + UTS for AT3 use              |
| **AT3** | `MetaAuthoringWork`         | `CoordinationFlowDescription`, `AuthoringPolicySpec`, `PublicationPlanDescription` | Publishes lanes; **does not** alter AT2 F/G | Records UTS; cannot change AT2 invariants   |

#### 10.2 Role map (examples)

* `Holder#DesignerRole:Context‑X` (AT1), `Holder#AuthorRole:Architheory‑Lab` (AT2), `Holder#CoordinatorRole:Program‑G` (AT3).
* `Holder` is always typed to a `U.BoundedContext`.
* Avoid **titles** as kernel types; keep them in the **Plain** register with twin labels.

### 11) Examples (cross‑arena, MG·DA compliant)

1. **Software engineering.** AT0: `RunObservation: CI‑Run‑4711`. AT1: `TaskPack: Refactoring‑Targets`. AT2: `ArchitheoryPack: Modularity‑Gauges` + `GaugeSpec: Coupling/Coherence`. AT3: `AuthoringPolicySpec: Pack‑Update‑Cadence`. Crossings logged with `BridgeCard` and UTS; CL from AT1→AT2 routed to **R**.

2. **Clinical operations.** AT0: `RunLogCarrier: MedicationAdministrationWork`. AT1: `TranslationMethodDescription: Dose‑Adjustment‑Design`. AT2: `ArchitheoryPack: Safety‑Invariants`. AT3: `CoordinationFlowDescription: Evidence‑Intake‑Board`. Domain mentions stitched to D.CTX + UTS; discipline governance via **CG‑Spec**.

3. **Operations research.** AT0: `RunResultDescription: Route‑Plan‑Day‑7`. AT1: `TaskPack: Routing‑Abstractions`. AT2: `GaugeSpec: Cost‑Elasticity`. AT3: `AuthoringPolicySpec: Evidence‑Lane‑Publishing`. All imports bridged; CL→R only.

### 12) Anti‑patterns & canonical rewrites

* **“Process ladder”** → Use **Work** heads: `AppliedWork`, `TransdisciplineDesignWork`, etc.
* **“Domain governance”** → Move rules into a **`Discipline CG‑Spec`**; keep Domain as catalog mark with D.CTX + UTS stitching.
* **`Reviewer` (type)** → `ReviewerRole` with `Holder#ReviewerRole:Context`.
* **`…CarrierRole` (legacy)** → `Holder#…Role:Context`.
* **“Tradition”** → `Tradition` (Tech); keep “Tradition” only as Plain twin with twin‑label to the `Tradition`.

### 13) Quality hooks & metrics (informative)

* **Q1. Tier purity.** Share of tokens whose **SourceTier == TargetTier** (no crossing).
* **Q2. Crossing completeness.** % of cross‑tier citations with `BridgeCard` + UTS.
* **Q3. CL hygiene.** % of imported evidence with CL routed to **R** and explicit loss notes.
* **Q4. Lexical conformance.** % tokens passing **SCR‑LEX** (head‑anchoring, I/D/S, Role/Holon separation).
* **Q5. Publication latency.** Median time between citation and UTS row publication.

### 14) Implementation notes

* **Classifier aid.** A simple rule of thumb:

  * Mentions **real‑world outcomes** → candidate `AppliedWork` (AT0).
  * Mentions **methods‑about‑methods** and **Task packs** → AT1.
  * Mints **gauges/invariants/packs** for reuse → AT2.
  * Sets **policies/coordination** for authoring → AT3.
    Always confirm via **object‑of‑talk** and **output heads**.

**Publication discipline.** Keep a **`BridgeRegisterCarrier`** and a **`UTSRegisterCarrier`** controlled by `Holder#StewardRole:Program‑X`.
 Record twin labels on UTS rows.

### 15) Related patterns

* **A.4** — Temporal Duality & Open‑Ended Evolution Principle (time‑split of design/run).
* **B.4** — Canonical Evolution Loop (Observe→Refine→Deploy) governs ATS change/refresh cadence.
* **B.5/B.5.1** — Canonical Reasoning Cycle (Explore→Shape→Evidence→Operate) as cognitive engine for AT‑work.
* **E.10 (LEX‑BUNDLE)** … **F.17** — UTS publication. **C.20 §D.DISC** … **D.CTX** — Context enumeration and stitching.
* **E.10.D2** — I/D/S acceptance harness (for `…Spec`).
* **F.4** — Role Description (RCS/RSG) for `…Role` tokens.
* **F.11** — Method Quartet Harmonisation (algorithm ↔ method description ↔ spec).
* **F.17** — UTS publication.
* **C.20 §D.DISC** — Discipline CAL lexical guard (Holon, CG‑Spec, Domain stitching).
* **D.CTX** — Context enumeration and stitching.

### 16) Glossary (tokens minted or stabilised here)

* `AuthoringTierScheme` · `AuthoringTierSchemeDescription` · `AuthoringTierSchemeSpec`
* `AppliedWork` (AT0) · `TransdisciplineDesignWork` (AT1) · `ArchitheoryAuthoringWork` (AT2) · `MetaAuthoringWork` (AT3)
* `TaskPack` · `ArchitheoryPack` · `GaugeSpec` · `InvariantSetDescription`
* `BridgeCard` · `UTS row` (PublicationCarrier entry) · `BridgeRegisterCarrier` · `UTSRegisterCarrier`
* Roles: `DesignerRole`, `TranslatorRole`, `AuthorRole`, `AssessorRole`, `ReviewerRole`, `CoordinatorRole`, `EditorRole`, `DisciplineStewardRole`
* Lane markers: `F‑lane`, `G‑lane`, `R‑lane` · `CL` (conformance loss) with **CL→R only**

### 17) Lexical/Conformance checklist (quick use)

* **Head‑anchoring:** All heads signal kind (System/Holon/Work/Method/Pack/Spec/Description/Role/Carrier).
* **I/D/S morphology:** `…Description` vs `…Spec` used correctly; acceptance harness only for `…Spec`.
* **Role vs Holder vs Carrier:** `Holder#…Role:ContextId`; Carriers bear epistemes; no `…CarrierRole`.
* **Object‑of‑talk stated** in first line for every new token.
* **Domain = catalog mark only;** stitched to D.CTX + UTS; comparability in **CG‑Spec** of a `U.Discipline`.
* **Gate‑crossings published:** `BridgeCard` + **UTS row** always present.
* **Evidence lanes:** F/G/R separated; **CL→R only**; provenance recorded.
* **Plain twins:** Figurative heads (e.g., “Ladder”, job titles, “Tradition”) also corrected by a twin plane lexical discipline.
* **No minted `U.Type` “Strategy”.** Treat **strategy/policy** as compositions/lenses in **G.5** under **E/E‑LOG**; keep “strategy” in the **Plain** register only.

### 18) Minimal worked “publish set” (ready‑to‑use)

1. **Mint** `AuthoringTierSchemeDescription` (this pattern).
2. **Optionally mint** `AuthoringTierSchemeSpec` with AH‑1…AH‑4 harnesses (per E.10.D2).
3. **Set up carriers:** `BridgeRegisterCarrier`, `UTSRegisterCarrier`.
4. **Start registering crossings:** whenever AT0 informs AT1, AT1 informs AT2, or AT3 organises AT2, publish a **`BridgeCard`** with CL notes and a **UTS row**; register the Bridge on the **PathSlice sentinel watch‑list**.

### **Pattern E.12 — Didactic Primacy & Cognitive Ergonomics \[A] 

**Context**

The FPF is designed as an "Operating System for Thought," a tool intended to augment and clarify human (and artificial) reasoning. This mission places a unique demand on its architecture: the framework's internal elegance and formal power are secondary to its primary function of being understandable and usable. A perfectly consistent but incomprehensible system fails in its didactic purpose. As formal mechanisms like `Assurance Levels` and epistemic scores are introduced, there is a significant risk that the pursuit of these metrics becomes an end in itself, overshadowing the ultimate goal of fostering clearer thought.

**Problem**

If the framework's design prioritizes theoretical purity or formal completeness over cognitive ergonomics, it becomes vulnerable to two critical failure modes:

1.  **Goodhart's Law:** When a measure (like `AssuranceLevel:L2`) becomes the primary target, it ceases to be a good measure of genuine understanding. Teams may start "gaming the metrics," producing artifacts that are formally perfect but conceptually shallow or pragmatically useless.
2.  **Cognitive Overload & Rejection:** The framework becomes so dense, jargon-laden, and procedurally complex that its users—the very agents it is meant to serve—either burn out or abandon it in favor of simpler, albeit less rigorous, methods. The "Operating System for Thought" devolves into a bureaucratic machine for certification.

**Forces**

| Force | Tension |
| :--- | :--- |
| **Formal Rigor vs. Human Usability** | How to build a system that is both formally sound and cognitively accessible, without sacrificing one for the other. |
| **Intrinsic Complexity vs. Incidental Complexity**| How to distinguish the necessary cognitive load inherent in solving a difficult problem from the unnecessary friction imposed by a poorly designed framework. |
| **Means vs. Ends** | How to ensure that the production of high-quality artifacts (the means) always serves the ultimate goal of enhancing an agent's cognitive capabilities (the end). |

**Solution**

FPF elevates **Didactic Primacy (Pillar P-2)** to a normative architectural principle, operationalized through two conceptual mechanisms designed to act as a permanent counterbalance to excessive formalism.

**1. The Principle of Didactic Primacy (Expanded Definition)**

The primary purpose of the FPF is to enhance the cognitive capabilities (`U.Capability`/`Mastery`) of an Agent (`U.Agent`) in service of its Objectives (`U.Objective`). The creation of artifacts with high assurance levels and epistemic scores is a *means to that end, not the end itself*. Any architectural decision that increases formal rigor at the cost of clarity or usability must be explicitly justified by a demonstrable gain in the agent's ability to reason effectively.

**2. Mechanism 1: The Rationale Mandate**

Every key assurance artifact (such as a `U.AssuranceCase` or `Proof`) **MUST** contain a mandatory, human-readable **`rationale`** component.

*   **Nature:** The `rationale` is not a technical description but a narrative explanation.
*   **Content:** It **MUST** answer the question: *"How does achieving this level of formal assurance tangibly help the agent better understand the problem or make a more reliable decision?"*
*   **Purpose:** This mandate forces a moment of reflection, formally linking the act of formalization back to its pragmatic, cognitive purpose. An empty or perfunctory rationale indicates that the assurance work may be an exercise in formalism for its own sake.

> **Didactic Note for Managers: The "So What?" Test**
>
> The Rationale Mandate is FPF's built-in "So What?" test. When your team presents a complex, formally verified artifact (`AssuranceLevel:L2`), the `rationale` is where they answer your fundamental question: "This is impressive, but *so what*? How does this help us ship a better product, make a smarter investment, or avoid a critical risk?" If the answer isn't clear and compelling in the `rationale`, the formal work may have been a waste of resources. It keeps your most brilliant minds focused on creating value, not just elegant proofs.

**3. Mechanism 2: The Human-Factor Loop (HF-Loop)**

To provide a continuous, self-correcting mechanism against cognitive overload, FPF introduces a conceptual feedback loop.

*   **Core Concept:** The HF-Loop is a formal method of inquiry designed to distinguish between the *essential complexity* of the problem being solved and the *incidental complexity* introduced by the FPF itself.
*   **Trigger Concept:** A review is triggered when the **subjective cognitive workload** associated with using the framework exceeds a conceptual threshold. This is not about performance metrics, but about the perceived mental effort required to use FPF's concepts and structures.
*   **Review Concept:** When triggered, a formal review is conducted by individuals in roles that specialize in human-centric perspectives, such as the **`Ethicist`** and **`UX Design Critic`**.
*   **Output Concept:** The review produces a set of proposed **conceptual simplifications** or **didactic improvements** to the framework's patterns or architheories. These are then submitted as formal change proposals (DRRs).

**Conformance Checklist**

*   **CC-E12.1 (Rationale Mandate):** Every `U.AssuranceCase` or `Proof` artifact at `AssuranceLevel:L2` **MUST** contain a non-empty `rationale` component that satisfies the "So What?" test.
*   **CC-E12.2 (HF-Loop Trigger Condition):** Each architheory that defines a significant workflow **SHOULD** specify a conceptual condition for triggering an HF-Loop review, based on the principle of managing cognitive load.
*   **CC-E12.3 (HF-Loop Review Mandate):** If a trigger condition is met, a review involving the designated human-centric roles **MUST** be initiated. Its outcome **MUST** be a documented set of conceptual refinement proposals.
*   **CC-E12.4 (Didactic Primacy in DRRs):** Any DRR proposing a change to a normative pattern **MUST** include a section analyzing its impact on cognitive ergonomics and didactic clarity.

**Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | Manager's View: What It Looks Like | How FPF Prevents It (Conceptually) |
| :--- | :--- | :--- |
| **The "Ivory Tower" Framework** | The FPF specification becomes a beautiful but impenetrable fortress of abstract logic that no practicing engineer can actually use. | The **HF-Loop** provides a formal channel for user feedback to drive conceptual simplification. The roles of `UX Design Critic` and `Ethicist` are constitutionally empowered to challenge complexity that does not serve a clear purpose. |
| **The "Meaningless Rationale"** | The `rationale` field is filled with boilerplate text like "To increase assurance," without any real connection to the problem. | The "So What?" test is part of the review process for L2 artifacts. A perfunctory `rationale` is grounds for rejecting the artifact's promotion to L2, forcing the author to articulate the *real* value of their formal work. |
| **Glorifying Complexity** | A culture emerges where the most complex and difficult-to-understand models are considered the "best," regardless of their utility. | The core principle of **Cognitive Elegance (P-1)** and the mechanisms in this pattern create a constant pressure towards simplicity and clarity. The framework formally values understanding over mere complexity. |

**Consequences**

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Guards FPF's Core Mission:** This pattern acts as an "immune system," protecting the framework from devolving into sterile formalism and ensuring it remains a tool for enhancing thought. | **Introduces "Softer" Concepts:** Cognitive load and rationale quality are less quantifiable than formal proofs. *Mitigation:* FPF operationalizes them through a formal method. The HF-Loop is a structured inquiry, not an informal chat. |
| **Empowers Human-Centric Roles:** It gives the `Ethicist` and `UX Design Critic` roles a concrete, constitutional function in the evolution of the framework. | - |
| **Prevents User Burnout and Rejection:** The HF-Loop is an early warning system that detects when the framework is becoming too cumbersome, allowing for course correction before users become frustrated and abandon it. | - |
| **Creates a Self-Simplifying System:** The pattern creates a formal pressure that forces FPF to evolve towards greater clarity and usability, balancing the drive for formal rigor. | - |

**Rationale**

This pattern operationalizes **Didactic Primacy (P-2)**, transforming it from a philosophical statement into an enforceable architectural Standard. The `Rationale Mandate` ensures that every act of formalization is tied to a clear purpose. The `Human-Factor Loop` ensures that the *cost* of using the framework is measured not just in resources, but in the most critical resource of all: the cognitive capacity of its users.

This pattern does not weaken the formal rigor established by other ADRs; it complements it. It guarantees that the powerful machinery of FPF is always directed towards a meaningful, human-relevant goal. It is the constitutional guarantee that FPF will remain, first and foremost, an "Operating System for Thought."

**Relations**

*   **Implements:** Pillar `P-2 Didactic Primacy`.
*   **Complements:** `E.13 Pragmatic Utility & Value Alignment` (which focuses on the relevance of the *problem*, while this pattern focuses on the usability of the *framework*).
*   **Is constrained by:** The overall governance process (DRRs), which is the vehicle for implementing the conceptual simplifications proposed by the HF-Loop.

### Pattern E.13 — Pragmatic Utility & Value Alignment \[A] 

**Context**

The FPF provides a powerful engine for constructing formally correct and highly reliable holons. This power, however, introduces a subtle but profound risk: a team can create a perfectly verified and validated artifact (`AssuranceLevel:L2`) that solves an irrelevant, misunderstood, or non-existent problem. The framework guarantees that the solution is *correct*, but it does not, by itself, guarantee that the solution is *useful*.

Furthermore, many of the most important system objectives—such as "safety," "usability," or "security"—are not directly measurable. They are assessed via **proxy characteristics** (e.g., "number of reported vulnerabilities" as a proxy for security). This practice is vulnerable to Goodhart's Law: when a proxy becomes the primary target, it often ceases to be a good measure of the original goal, as teams begin to optimize the proxy at the expense of the real objective.

**Problem**

Without a formal mechanism to keep the entire assurance apparatus tethered to real-world value, FPF risks enabling two critical failure modes:

1.  **Formalism for Formality's Sake:** Teams become preoccupied with achieving high epistemic scores, producing elegant but useless artifacts. The framework is used to build beautiful solutions to the wrong problems.
2.  **Proxy-Metric Distortion (Goodhart's Law):** Teams successfully optimize for a chosen proxy characteristic, but in doing so, they diverge from—or even actively undermine—the true, often qualitative, `U.Objective` that the proxy was intended to represent. The system becomes technically successful but pragmatically a failure.

**Forces**

| Force | Tension |
| :--- | :--- |
| **Measurability vs. Meaning** | How to use quantitative, measurable proxies for progress without losing sight of the qualitative, often un-measurable, goals that truly matter. |
| **Abstraction vs. Application** | How to build and reason with abstract models without them becoming disconnected from any concrete, practical application. |
| **Incremental Progress vs. Global Value** | How to ensure that local optimizations and incremental improvements are genuinely contributing to the overall value proposition of the holon. |

**Solution**

FPF elevates **Pragmatic Utility (Pillar P-7)** to a normative architectural principle, operationalized through two mandatory conceptual mechanisms.

**1. The Principle of Pragmatic Utility (Expanded Definition)**

Any artifact created within the FPF is an instrument for achieving a specific, pragmatic `U.Objective`. The value of an artifact is determined solely by its **utility** in achieving that objective, not by its epistemic scores in isolation.

**2. Mechanism 1: The Proxy-Audit Loop**

To formally manage the risk of Goodhart's Law, FPF introduces a conceptual feedback loop to periodically review the alignment between proxy characteristics and their intended goals.

*   **New Normative Relation:** A new relation, `isProxyFor: U.Characteristic → U.Objective`, is introduced. This relation **MUST** be used to explicitly declare when a measurable characteristic is serving as a proxy for a higher-level, often qualitative, goal.
*   **Conceptual Audit Process:** Any characteristic marked with the `isProxyFor` relation is subject to a **periodic conceptual audit**.
*   **Review Roles:** This audit is conceptually performed by the individual(s) in the **`Strategist`** role. They are tasked with answering the question: *"Is optimizing for this proxy still reliably driving progress toward the actual `U.Objective` it represents, or have we observed a divergence?"*
*   **Output Concept:** If a divergence is identified, a high-priority `U.Method` for revising or replacing the proxy **MUST** be proposed.

> **Didactic Note for Managers: Are You Climbing the Right Mountain?**
>
> The Proxy-Audit Loop is your compass. Your team's dashboards might show all green—metrics are improving, targets are being hit. But the audit loop forces a crucial question: "Are these the *right* metrics?"
>
> Imagine you are trying to improve "customer satisfaction" (`U.Objective`). You choose "average call handle time" as a proxy metric. Your team successfully drives this number down. But the Proxy-Audit reveals that customer satisfaction is actually *decreasing* because agents are rushing and providing poor service to meet the time target. The loop forces you to recognize this divergence and find a better proxy (e.g., "first-call resolution rate"). It ensures your team is not just climbing fast, but climbing the right mountain.

**3. Mechanism 2: The Minimally Viable Example (MVE) Mandate**

To enforce a pragmatic, value-first approach from the very beginning of a project, any new `U.System` or major system component **MUST** begin its development cycle with the creation of a **Minimally Viable Example (MVE)**.

*   **Definition:** An MVE is a simple, end-to-end, working instance of the holon that demonstrates the achievement of at least one core, user-facing objective, however trivial. It is the FPF equivalent of a "Hello, World" for a complex system.
*   **Assurance Requirement:** The MVE **MUST** achieve a minimum of **`AssuranceLevel:L1 (Substantiated)`**. This means the MVE cannot be a mere mock-up or a purely conceptual sketch; it must be supported by at least one piece of tangible evidence (e.g., a passing test case, a formal assertion), as defined in Pattern B.3.3.
*   **Stege transition Precedence:** The development of the full-scale holon cannot proceed to `AssuranceLevel:L2` until the MVE has been created and has met its L1 requirement.

**Conformance Checklist**

*   **CC-E13.1 (Proxy Declaration Mandate):** Any `U.Characteristic` used as a primary driver for an objective **MUST** be explicitly linked to that `U.Objective` via the `isProxyFor` relation.
*   **CC-E13.2 (Proxy-Audit Mandate):** A formal Proxy-Audit review **MUST** be conducted at regular conceptual intervals (e.g., before each major release). The outcome of this review **MUST** be a documented episteme.
*   **CC-E13.3 (MVE Mandate):** The development of any new `U.System` **MUST** be preceded by the creation of an MVE that satisfies the `AssuranceLevel:L1` requirement.
*   **CC-E13.4 (MVE Traceability):** The full-scale `U.System` **MUST** maintain a formal traceability link (`isEvolutionOf`) to its originating MVE.

**Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | Manager's View: What It Looks Like | How FPF Prevents It (Conceptually) |
| :--- | :--- | :--- |
| **The "Perfectly Engineered Irrelevance"** | The team delivers a technically brilliant system that is formally verified and validated, but no one wants to use it because it doesn't solve a real problem. | **CC-E13.3** forces the team to build a working, end-to-end slice of value (the MVE) *first*. This grounds the entire project in a demonstrated solution to a real user need from day one. |
| **The "Metric Myopia"** | The team becomes obsessed with improving a specific KPI, ignoring clear signs that this is not improving—and may even be harming—the overall user experience or business goal. | **CC-E13.2** mandates the Proxy-Audit Loop. This forces a periodic, strategic step-back, where the `Strategist` role is constitutionally required to ask, "Are we still measuring what matters?" |
| **The "Big Design Up Front" Trap** | The team spends months creating a vast, abstract, and highly detailed model of a system before ever building a single working component. | The **MVE Mandate** prevents this. It forces an iterative, pragmatic "build-to-learn" approach, ensuring that models are always grounded in a working reality. |

**Consequences**

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Defense Against Goodhart's Law:** The Proxy-Audit Loop is a concrete, operational defense against the common failure mode of optimizing for the wrong thing. It forces regular, strategic reflection on the meaning of metrics. | **Introduces Strategic Overhead:** The Proxy-Audit Loop and the creation of an MVE require dedicated time for strategic thinking and early implementation. *Mitigation:* This is not an expense but a strategic investment. This upfront effort is designed to prevent the far greater cost of developing the wrong system over months or years. |
| **Ensures Value-Driven Development:** The MVE Mandate guarantees that all major development efforts are grounded in a demonstrated, working solution to a real problem, however small. This prevents teams from investing significant resources in abstract models that have no proven path to practical application. | - |
| **Prevents "Analysis Paralysis":** By requiring an early, working example, this principle encourages an iterative, pragmatic development style. It forces teams to build and learn, rather than over-specifying in a vacuum. | - |
| **Positions FPF as an Engineering Discipline:** This pattern firmly anchors FPF as a tool for practical engineering, not just theoretical modeling. | - |

**Rationale**

This pattern operationalizes **Pragmatic Utility (P-7)**. While Pattern E.12 protects the *agent* from the cognitive overload of the framework, this pattern protects the *problem* from being lost in a sea of formal abstraction. It provides the necessary constitutional guardrails to keep the powerful formal methods of FPF focused on delivering tangible, real-world value.

The **MVE Mandate** ensures that every journey starts with a destination in sight. The **Proxy-Audit Loop** ensures that the compass used on that journey remains pointed in the right direction. Together, these mechanisms guarantee that knowledge generated within FPF is not only formally correct and epistemically reliable, but also meaningful, useful, and aligned with its intended purpose.

**Relations**

*   **Implements:** Pillar `P-7 Pragmatic Utility`.
*   **Complements:** `E.12 Didactic Primacy & Cognitive Ergonomics`.
*   **Provides context for:** The definition of `U.Objective` and `U.Characteristic` by establishing a formal link between them.


---

# **E.14 · Human‑Centric Working‑Model** \[A]

### 1  Intent

Establish a **single, human‑centric Working‑Model** that practitioners can read, discuss, and evolve **without exposure to formal machinery**.  
Each statement **declares a justification stance** (`validationMode`) and, when assurance is sought, attaches **appropriate grounding** via one or more assurance shoulders — **Mapping**, **Logical**, **Constructive** — and **may additionally attach Empirical Validation** (evidence) as defined by the Trust & Assurance calculus. Empirical Validation can accompany any stance; it is **required** when the stance is *postulate*. Assurance shoulders sit **beneath** the Working‑Model and **never define its vocabulary**.
 
+Put bluntly: *one model people work in; three assurance shoulders — plus empirical checks when the world is the judge.*

### 2  Problem & Context

+Teams need **one shared Working‑Model** to make decisions at speed. Historically this surface either:

* **drifts into jargon**—different terms for the same thing, slash‑labels, partial overlaps; or
* **calcifies into machinery**—too formal for day‑to‑day design and review.

Both failure modes create friction between two audiences:
(1) **working users** (engineers, programme managers, policy owners) who need a **small, stable surface**, and
(2) **assurance authors** (ontologists, methodologists, auditors) who need **proofs that the surface is sound**.

E.14 resolves the impasse by **separating concerns**:

* A **Working‑Model layer**: curated kinds and relations expressed in plain terms, governed by simple human rules.
* A **three‑rung Assurance stack** beneath it—**Mapping**, **Logical**, **Constructive**—that carries the heavy arguments (concept alignment, relational semantics, generative traces) and **never leaks back** into the Working‑Model narrative.

This pattern dovetails with the framework’s unification stance (**small Working‑Model surface, rigorous foundations**) and with our constructional mereology commitments (**sum/set/slice** provide extensional identity), while keeping the Kernel minimal and meta‑only.

### 3  Forces

1. **Cognitive economy vs. semantic precision.**
   Managers and engineers must navigate with a handful of names and relations; assurance authors must still certify that those names and relations **are unambiguous and extensional**.

2. **Speed of change vs. guarantees.**
   The Working‑Model must accommodate rapid iteration; the Assurance stack must **lag just enough** to check, without blocking practical progress.

3. **Parsimony vs. expressivity.**
   The Working‑Model should **not proliferate relation types or ad‑hoc categories**; fine‑grained distinctions live in the Assurance layers and are surfaced **only when they materially change a decision**.

4. **Downward grounding vs. upward contamination.**
   Grounding must always flow **down** (Working‑Model → Mapping → Logical → Constructive). No dependence **up** is allowed: proofs and traces never dictate wording or layout in the Working‑Model.

5. **Trans‑disciplinary unification vs. local dialects.**
   The Working‑Model must reconcile different disciplines’ habits **without erasing them**; Mapping captures dialects, while the Working‑Model exposes a **single usable choice**.

6. **Auditability vs. readability.**
   Every Working‑Model statement must be **auditable on request**, yet day‑to‑day views **hide the scaffolding** unless summoned.

---

### 4  Solution 

#### 4.1 Human-Centric principles

> **E.14‑P.1 – Working‑Model first, stance explicit.**  
> Operate one **Working‑Model** for all human‑facing discussion. For **each** assertion, the author **SHALL declare** a justification stance (`validationMode`) and choose the **appropriate assurance shoulder(s)**: **Mapping** (term↔kind alignment via **Lang‑CHR** / D‑Projection), **Logical** (CT2R alias semantics, scope/constraints), **Constructive** (Γₘ generative trace), and **Empirical Validation** (evidence via `U.EvidenceRole` in a declared `U.BoundedContext`).

> **E.14‑P.2 – Downward‑only dependency.**
> Information **may** flow from the Working‑Model down into any Assurance layer; **no Assurance layer may impose vocabulary or shape back upward** into the Working‑Model.
>
> **E.14‑P.3 – Small surface, big proof.**
> The Working‑Model exposes a **minimal set** of names (L‑1/L‑2 registers) and **a compact family of relations** used in everyday reasoning; precision and completeness are **proved below**.

> **E.14‑P.4 – Human registers first.**
> Terms in the Working‑Model are deliberately curated for **human legibility** (register‑badged, synonym‑aware). Synonym capture and language variance belong to Mapping; **only the chosen canonical label appears on the Working‑Model surface**.

> **E.14‑P.5 – Justification modes are explicit.**  
> Each Working‑Model relation **declares** `validationMode ∈ {axiomatic, inferential, postulate}`.  
> _axiomatic_ → **Constructive** grounding (Γₘ trace via `tv:groundedBy`); _inferential_ → **Logical** grounding (reasoned chain, often KD‑CAL‑backed for epistemic ties); _postulate_ → **Empirical Validation** (evidence bundle with scope and timespan). Empirical Validation (**LA**) may also accompany _inferential_ or _axiomatic_ claims as real‑world confirmation. **Mapping** contributes **TA**, **Logical/Constructive** contribute **VA**, and **Empirical** contributes **LA** (per the Trust & Assurance calculus; no calculus variables appear on the Working‑Model surface).

> **E.14‑P.6 – Parsimony at the surface.**
> No new Working‑Model relation types are introduced if the existing Logical aliases plus Constructive grounding suffice to capture the intended meaning.

> **E.14‑P.7 – Evidence is a first‑class support.**  
> When *postulate* is chosen, authors **SHALL** attach an **evidence pointer** (Empirical Validation) appropriate to the claim and context, governed by `U.EvidenceRole` within a declared `U.BoundedContext`.  
 
### 5  Layer Standard & Downward Flow (Working‑Model → Assurance)

This section defines **what each layer is for**, **what it guarantees**, and **how a single Working‑Model statement is carried down**.

#### 5.1  Working‑Model (what humans see)

**Purpose.** A small, curated graph of kinds and relations that a mixed team can read at a glance.

**Elements.**

* **Kinds** — one **chosen concept** per node (no slash‑labels).
* **Relations** — a short list intelligible to non‑specialists (e.g., *Component‑of*, *Member‑of*, *Aspect‑of*, plus a small number of cross‑disciplinary ties such as *Interface‑of* or *Constituent‑of*).
* **Language register badges** — terms appearing on the surface are L‑1 or L‑2; L‑3/L‑4 remain in Mapping as synonyms or symbols.

**Obligations.**

* Every Working‑Model edge and node is **grounded downward** (see below).
* The Working‑Model **does not display** constructor jargon, proof terminology, or evidence identifiers; those live in Assurance and are **callable on demand**.

#### 5.2  Assurance‑1: Mapping (from words to kinds)

**Role.** Consolidate human labels from varied sources and **bind them to the chosen kinds** used on the Working‑Model.

**Guarantee.** For any Working‑Model label, there exists a **stable alignment** to exactly one kind; synonyms, abbreviations, locales and registers are recorded here, **not** on the surface. Mapping primarily raises **Typing Assurance (TA)** by consolidating synonyms/registers and binding tokens/labels to **one chosen kind**; calculus‑level metrics live outside Part E.

**Deliverable.** A compact alignment table per scope that makes it obvious which **one label** the Working‑Model will show and which alternatives are tolerated in background sources.

*(Rationale: Working teams speak many dialects; the Working‑Model speaks one. Mapping is the interpreter.)*

#### 5.3  Assurance‑2: Logical (from Working‑Model relations to alias semantics)

**Role.** Give each Working‑Model relation **a precise alias meaning** and **its admissible use‑cases**, keeping the surface vocabulary small.

**Guarantee.** A Working‑Model edge such as *Component‑of* or *Aspect‑of* **carries one intended reading** (transitivity/antisymmetry expectations, scope notes), sufficient for auditors to assess whether the **use is legitimate** in a given context.

**Deliverable.** A short set of alias rules: “When an edge is labeled *Component‑of* at the surface, it intends the structural reading that is later verified by construction.” The Logical layer is **the Standard** that ties human labels to accepted meanings (CT2R alias rules); it primarily contributes **Verification Assurance (VA)**. Calculus‑level symbols are not used in E‑patterns.

*(Rationale: logical aliasing protects the small surface from relation proliferation while keeping meanings crisp.)*

#### 5.4  Assurance‑3: Constructive (from meanings to generative traces)

**Role.** Provide **extensional guarantees** by **constructing** the wholes, collections, and slices that Working‑Model relations speak about.

**Guarantee.** For structural edges, **there exists a constructional narrative** (e.g., *sum*, *set*, *slice*) that, if told, would recreate the whole from its parts or the aspect from its bearer; this makes identity and containment **trackable and testable** across scales.

**Deliverable.** A **single generative story** per structural link (axiomatic justification). For non-structural ties on the surface (e.g., epistemic links), Constructive may be absent; Logical/Empirical take the lead. Constructive contributes **VA** (extensional identity via Γₘ); for **structural** edges, `tv:groundedBy` **MUST** reference exactly one Γₘ trace.

*(Rationale: constructional grounding turns everyday part‑whole talk into statements whose identity conditions are not left to taste.)*

#### 5.5  Assurance‑4: Empirical Validation (from claims to observed world)

**Role.** Record when and where a Working‑Model claim meets reality.  
**Guarantee.** Every empirical binding names a **`U.BoundedContext`**, a **target claim/scope**, and a **timespan**; **staleness/refresh** are managed per context policy.  
**Deliverable.** A `U.EvidenceRole` binding (status‑only) anchored into the Evidence–Provenance chain. Empirical Validation contributes **LA** (raises empirical **R** and constrains **G** to its validated envelope).

#### 5.6  The downward grounding for a single surface statement

Consider a Working‑Model arrow **A –Component‑of→ B**:

1. **Mapping** shows that the words *A* and *B* are the chosen labels for their kinds; it retains tolerated synonyms and symbols in the background.
2. **Logical** confirms that **Component‑of** on the surface means the **structural reading** with its ordinary mereological expectations; if the surface used *Member‑of* instead, Logical would similarly certify the intended reading and its boundaries.
3. **Constructive** exhibits the **constructional narrative** (e.g., a _sum_ of parts resulting in **B** with **A** among them), which yields **axiomatic justification** for the structural edge, sets `validationMode=axiomatic`, and binds the edge via **`tv:groundedBy → Γₘ.sum|set|slice`**.
4. **Empirical Validation** records the **evidence pointer** and scope that make the claim auditable within its `U.BoundedContext` (required for *postulate*; optional reinforcement for other stances).

Together, these three **ground the human arrow without leaking their machinery upward**. The Working‑Model remains simple; the Assurance stack carries the proof.

### 6 · Archetypal Grounding *(System / Episteme)*

> **Tell–Show–Show.** The principle is stated once, then shown on a `U.System` case (structural) and on a `U.Episteme` case (knowledge‑bearing), in line with the authoring template.

**6.1 · `U.System` — Working‑Model first, Constructive grounding available**

* **Publication (Working‑Model).** Authors state structure using familiar relations (e.g., *Impeller* **ut\:ComponentOf** *Pump*; *Pump* **ut\:ComponentOf** *Skid*). Nothing else is required for readers to follow the design.
* **Assurance (downward grounding).** When stronger assurance is sought, the same author **narrates** the constructive story of the whole as a composition of parts and, where appropriate, attaches a downward grounding to that narrative (sum / set / slice). The narrative remains concept‑level and notation‑neutral; order and time stay out of structure and are expressed in their own planes.
* **Canonization move.** Readers continue to see Working‑Model relations as the primary surface; the constructive story is *supporting*, not *defining*.

**6.2 · `U.Episteme` — Working‑Model first; Logical/Mapping preferred; Empirical evidence as appropriate**

* **Publication (Working‑Model).** Authors connect meaning‑bearing artefacts using knowledge relations (e.g., **RepresentationOf**, **UsageOf**) in the same human‑oriented style.
* **Assurance (downward grounding).** Here assurance typically flows to the **Logical** or **Mapping** shoulders (reasoned argument; type/lexical alignment). **Empirical Validation** is used where observation is the right currency (status‑only roles on epistemes); Constructive grounding is optional and used only where a structural interpretation is genuinely intended.
* **Canonization move.** Again, Working‑Model text is the public form; assurance is attached deliberately and separately, without leaking method or time semantics into structure.

**6.3 · Pattern lesson (both cases)**
The **Working‑Model layer remains the canonical publication surface** for authors and reviewers; **assurance layers** (Mapping / Logical / Constructive) are **opt‑in** and used purposefully, with grounding flowing **downwards** from the Working‑Model to the appropriate shoulder. This presentation respects the authoring template’s *Archetypal Grounding* requirement and keeps notational choices illustrative rather than defining. 

---

### 7 · Bias‑Annotation *(what to watch for, and the counter‑moves)*

| Bias (name)                       | Symptom in drafts                                                                           | Conceptual counter‑move                                                                                                                        | Where this is governed                                               |
| --------------------------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Formalism capture**             | Treating a constructive narrative as “the real thing,” with **ut:\*Of** reduced to a label. | Re‑assert Working‑Model primacy: publish in **ut:\*Of**; attach assurance **downwards** only when needed.                                      | E.8 template; Notational‑Independence guard‑rail.                    |
| **Canonical inversion**           | Demanding constructive grounding for epistemic links by default.                            | Keep the **progressive** stance: prefer Logical/Mapping assurance for knowledge claims; raise to Constructive only when structure is at issue. | Authoring template; Working‑Model pattern family.                    |
| **Layer leakage (order/time)**    | Encoding sequence or phase as part–whole to “strengthen” claims.                            | Keep **order**/**time** in their planes; do not smuggle them into structure.                                                                   | Style/structure guidance in Part E; flavour separation in Γ‑family.  |
| **Collection ↔ Composition swap** | Using **MemberOf** as if it implied **ComponentOf** identity.                               | Keep collections (*set*) distinct from assemblies (*sum*); do not upgrade membership to component status.                                      | Working‑Model mereology guidance (Part B/C linkage).                 |
| **Notation lock‑in**              | Letting a diagram or syntax define meaning.                                                 | Apply **Notational Independence**: define semantics in prose (maths if needed); treat renderings as informative.                               | Notational‑Independence guard‑rail.                                  |
| **Backwards dependency**          | Letting an assurance artefact redefine public terms.                                        | Preserve **unidirectional dependence**: Working‑Model terms do not derive their meaning from assurance artefacts.                              | Part E guard‑rails (dependency discipline).                          |
| **Silent stance**                 | Publishing claims with no declared assurance stance.                                        | Declare the stance explicitly (e.g., working claim vs reasoned vs constructive).                                                               | Style/authoring discipline in Part E.                                |

> **Reading reminder.** Bias checks are *conceptual* reading aids; they never introduce notational or tooling mandates.

### 8 · Conformance Checklist *(normative; author‑facing duties for thought and prose)*

| ID                                         | Requirement                                                                                                                                                                      | Purpose                                                       |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **CC‑E14‑1 (Working‑Model primacy).**      | Authors **SHALL** publish claims in **Working‑Model** form (human‑oriented **ut:\*Of** relations or equivalent domain statements) as the canonical surface for readers.          | Preserve human‑first canon and didactic clarity.              |
|**CC‑E14‑2 (Downward grounding).** | When assurance is attached, grounding **SHALL** flow **downwards** from the Working‑Model to the appropriate assurance shoulder (**Mapping / Logical / Constructive / Empirical**) and **SHALL NOT** impose vocabulary back onto the Working‑Model. | Maintain plane separation and cognitive economy. |
| **CC‑E14‑3 (Stance declaration).**         | For any claim where assurance matters, the author **SHALL** declare `validationMode` (*postulate / inferential / axiomatic*).                                                    | Make assurance intent explicit and readable.                  |
| **CC‑E14‑4 (No order/time in structure).** | Authors **SHALL NOT** encode execution order, parallelism, or temporal coverage as part–whole; keep them adjacent in their own planes.                                           | Prevent layer leakage and category errors.                    |
| **CC‑E14‑5 (Collection ≠ Composition).**   | Authors **SHALL** keep **membership** claims distinct from **component** claims; no implicit upgrade from collection to assembly.                                                | Guard extensional identity and reader expectations.           |
| **CC‑E14‑6 (Notational independence).**    | Core meaning **MUST NOT** hinge on a specific diagram or syntax; any rendering present **SHALL** be marked informative.                                                          | Ensure longevity and cross‑discipline portability.            |  
| **CC‑E14‑7 (Layer direction).**            | Authors **SHALL** avoid back‑defining Working‑Model terms by their assurance artefacts; dependence is one‑way (Working‑Model → Assurance).                                       | Preserve unidirectional dependence of layers.                 |
| **CC‑E14‑8 (Template compliance).**        | Sections **SHALL** follow the canonical pattern order; *Archetypal Grounding* is mandatory for `[A]`.                                                                            | Keep patterns comparable and auditable by reading.            |  
| **CC‑E14‑9 (Progressive formality).**      | Authors **SHOULD** escalate assurance deliberately (from working claim to reasoned to constructive), and use **Empirical Validation** where observation is the right currency.    | Support the formality ladder without burdening early drafts.  |
|**CC-E14-10 (Structural grounding handshake).** | For **structural** edges on the Working-Model, authors **SHALL** set `validationMode=axiomatic` and provide **Constructive** grounding with `tv:groundedBy → Γₘ.sum|set|slice` (see **Compose-CAL** and **CT2R-LOG**). Exactly **one** Γₘ trace is permitted per edge (CI rule alignment). | Aligns E.14 with CT2R-LOG and Compose-CAL; ensures extensional identity. |
| **CC‑E14‑11 (Empirical bindings).**        | When `validationMode=postulate` (or when adding real‑world confirmation), authors **SHALL** bind evidence via `U.EvidenceRole` in a declared `U.BoundedContext` with an explicit **timespan** and provenance anchors. | Aligns with Evidence Graph Referring and empirical ageing policies. |
| **CC-E14-12 (F-declaration).**             | Normative Working-Model artefacts **SHALL** declare `U.Formality = Fk` per **C.2.3** (**recommended F ≥ F3** for readable surfaces). Assurance artefacts **MAY** carry higher F; **min-F** applies to composites. | Aligns E.14 with the unified Formality characteristic; avoids legacy “tiers/modes”. |

*All obligations above are **conceptual** and apply to thought and prose; they introduce no notational or data‑processing requirements.*

**E — Conceptual Examples (no notation, no data handling)**

1. **Assembly from parts → “Component Of”**
   A pump skid is agreed to be nothing over and above its pump, frame, reservoir, and valve set considered together. Because the whole is conceptually *constructed* from those parts, the team may safely speak of each part as *Component Of* the skid. The justification is the construction itself: if any listed part were removed, the very same skid would no longer exist as that whole. This keeps identity extensional and makes the engineer‑facing alias (“Component Of”) truthful rather than conventional.

2. **Parallel elements gathered → “Member Of”**
   A test rig has four identical cartridges used in parallel. The rig treats them as a conceptual *gathering*; membership is fixed by inclusion in that gathering, not by sequence or timing. Speaking of each cartridge as *Member Of* the rig’s cartridge bank is then licensed by the same gathering act. Engineers can keep saying “member,” while architects know the warrant is the underlying construction of the bank as a collection, not an accidental tagging.

3. **Focused facet carved → “Aspect Of”**
   When the team talks about the *thermal envelope* of a reactor, they are not multiplying entities; they are taking the already‑agreed reactor and conceptually *carving out* its thermal facet for focused reasoning. Calling that carve‑out an *Aspect Of* the reactor is justified because the aspect owes its identity to the parent and the chosen facet, and nothing else. This licenses disciplined talk about “boundary,” “interface,” or “envelope” without mistaking them for independent systems.

> **Notes across the examples**
> • Everyday aliases (*Component Of, Member Of, Aspect Of*) remain the only labels engineers need to see; their truth is anchored by prior constructional choices.  
> • Structural links draw on **Constructive** grounding; **epistemic links**—like “Representation Of” or “Usage Of”—may instead rely on **Empirical Validation** (evidence bundles) or **Logical** grounding appropriate to the claim.  

**F — Resulting Context (after you apply the pattern)**

**What improves**

* **Single dial for containment.** Teams can ask one plain question—“what is inside what?”—and trust that all structural talk reduces to shared constructional choices rather than ad‑hoc relation lists. Ontologists keep rigorous warrants without burdening day‑to‑day readers.
* **Extensional identity by default.** Wholes are the wholes they are because of the parts gathered; collections are the collections they are because of their members; aspects inherit identity from their parent and facet. This prevents silent drift when labels change.
* **Layer harmony.** Engineer‑facing aliases live at the same level as other relation names, while their warrants live one step below, keeping human language clean and the generative basis auditable.

**What to watch**

* **Discipline at the structural tier.** A structural link that lacks a constructional warrant is conceptually unsafe. Conversely, forcing epistemic links to pretend they are structural over‑physicalises knowledge claims; for those, evidence or argument is the right currency.
* **Author workload moves, not grows.** Day‑to‑day model authors stay with aliases; specification authors carry the burden of ensuring every structural statement really follows from a sum, a gathering, or a carve‑out. This is a conscious shift of complexity away from operations and into the pattern’s foundation.

**Invariants you must preserve**

* **Parsimony of constructors.** Build wholes by summing parts; build banks by gathering elements; focus facets by carving aspects. Do not invent extra generative acts for parallelism or time‑slicing; those concerns belong to other conceptual services.
* **Two‑tier justification.** Structural talk rides on construction; epistemic talk rides on evidence or proof. Keep the boundary sharp so that later reasoning (about reliability, compliance, or policy) remains clear.

**Known consequences**

* **Stable queries, fewer surprises.** Because aliases are backed by shared constructions, teams from different disciplines can interoperate without renegotiating meanings at hand‑off.
* **Audit trail without jargon.** Reviewers can trace every structural claim to a prior constructional choice, while everyday collaborators keep using familiar relation names.



---

# E.15 — Lexical Authoring & Evolution Protocol  (LEX‑AUTH) \[A]

> *Author patterns as evidence‑bearing epistemes, evolve them via governed open‑ended search, and publish an auditable trace that improves quality—not just compliance.*


---

## 4) Solution — A *governed evolutionary* authoring method with a publishable **LEX‑AUTH Trace (LAT)**

LEX‑AUTH defines **how** a pattern is **proposed, varied, selected, validated, and merged**, with artifacts and evidence fit to the FPF kernel.

### 4.1 Method (design‑time choreography)

**Stage A — Frame & Scope (Context, Objectives, Invariants)**

1. **Anchor** the work in a **`U.BoundedContext`** for the spec (e.g., `FPF/Core`), cite governing guard‑rails (**E.5.\***), and state **objectives** for the change (e.g., clarity ↑, universality ↑, assurance cost ↓).
2. **Declare the Delta‑Class** (see §4.3) and **impact radius** (dependent patterns, bridges, tests).
3. **Fix acceptance targets** (see §4.4 Quality & SoTA metrics).

**Stage B — Generate candidates (SoTA + NQD)**
4. **Harvest SoTA** inputs (standards, rival patterns, lived domain idioms) and **bind** them as *evidence* via `U.EvidenceRole` with **claim/claim‑scope/timespan** (empirical vs deductive lines).
5. **Generate candidate variants** using **NQD‑CAL** engines (Novelty/Quality/Diversity) with an **E/E policy** (explore↔exploit governor) to populate a **Pareto front** of pattern phrasings/structures. *(No single shot; multiple candidate clauses compete.)*

**Stage C — Shape & Align (Structure, Bridges, USM)**
6. **Shape** top candidates into the standard **\[A] template** (Context → Problem → Forces → Solution → CC → Consequences → Rationale), obeying **LEX‑BUNDLE** (no tooling jargon; twin registers allowed).
7. **Bridge across Contexts** explicitly (F.9): any imported definitions/claims declare **CL** and *loss notes*; propose scoped **narrowing** where needed.
8. **Type scopes** with **USM (A.2.6)**: keep **ClaimScope (G)** distinct from **WorkScope**; no “applicability/envelope” smuggling.

**Stage D — Validate & Decide (Assurance, Tests, DRR)**
9. **Run the harness**: update **SCR/RSCR** (F.15), lint lexical rules (E.10), run **Γ‑consistency** and **RSG/SoD** checks where relevant.
10. **Score** candidates on **Quality & SoTA metrics** (§4.4) and **assurance deltas** (Δ⟨F,G,R⟩).
11. Record a **DRR** (E.9) with *options considered*, *trade‑offs*, chosen candidate, *blast‑radius*.
12. **Merge** the winner; version pattern **SemVer** by Delta‑Class.

**Stage E — Publish & Monitor**
13. Publish the **LEX‑AUTH Trace (LAT)** (§4.2) with the pattern.
14. Schedule **evidence refresh** windows and an **evolution watchpoint** (B.4 loop): when metrics or SoTA inputs decay, reopen Stage B.

### 4.2 The **LEX‑AUTH Trace (LAT)** — what it is and why it matters

A LAT is **not** “we ran a script.” It is a **structured episteme** that lets others **reproduce quality gains** and **re‑run** the search when SoTA shifts.

**LAT minimal contents (publish with the pattern):**

1. **Context & version** (pattern id, context, SemVer, Delta‑Class).
2. **Objective vector** (what we tried to improve: clarity, universality, assurance cost, etc.).
3. **SoTA pack** (sources bound as `U.EvidenceRole` with claim/scope/time and polarity).
4. **NQD settings** (emitters/lenses, diversity characteristics) + **E/E policy** used.
5. **Candidate set** (top K variants with NQD scores + short deltas from baseline).
6. **Bridge ledger** (all cross‑context imports with **CL** and loss notes).
7. **Assurance delta** (Δ⟨F,G,R⟩ from baseline; penalties from CL applied).
8. **Harness results** (checks passed/failed, test diffs).
9. **DRR link** (decision rationale id).
10. **Refresh policy** (evidence decay windows and triggers).

**Uses of the LAT:**
*Reproducibility* (re‑run B‑stages as SoTA changes), *assurance* (explicit impact on F/G/R), *portfolio health* (diversity/coverage), *teaching* (didactic before/after), and *cross‑context safety* (no silent imports).
Publish the pattern with a DRR that carries a LAT pointer (id/URI). The LAT itself is a U.Work evidence pack (non‑normative), archived with edition and Γ_time.

**Example of a LAT‑stub**
```
LAT:
  context: FPF/Core, pattern: F.15, semver: x.y+1, delta-class: Δ‑2
  objectives: {clarity↑, universality↑, assurance-cost↓}
  SoTA-pack: {OpenAlex 2025‑Q3, SPECTER2‑23, DPP‑2019, MAP‑Elites‑2015+}
  NQD-settings: {CharacteristicSpace: domain‑family × …, grid: CVT@k=16}
  candidates: K=4 (wording of RSCR‑F04 & gates)
  bridge-ledger: none (intra‑canon refs only)
  assurance‑delta: ΔF=+, ΔG=+, ΔR=+ (after CL‑penalties=0)
  harness: LEX‑BUNDLE lint pass; F‑suite pass; Γ‑consistency ok
  DRR-id: DRR‑2025‑09‑DFCM‑roll‑in
  refresh: F1‑Card edition refresh window = 6 mo
```

### 4.3 What counts as “changed the pattern as a whole” — **Delta‑Classes & versioning**

Classify the intended change **before** work starts (declared in DRR & LAT):

* **Δ‑0 Lexical polish** — wording/ordering only; **no** change to CC or semantics. → *Patch* (x.y.**z**+1).
* **Δ‑1 Didactic restructure** — narrative/layout; **unchanged** Conformance Checklist (CC). → *Minor* (**x.y**+1.0).
* **Δ‑2 Normative refinement** — CC tightened/clarified; *semantics preserved* by test equivalence. → *Minor* (**x.y**+1.0) + **RSCR** required.
* **Δ‑3 Semantic change** — CC **adds/removes** requirements; downstream contracts shift. → *Major* (**x**+1.0.0) + **impact review** + **bridges refresh**.

> **Definition of “pattern changed as a whole”:** any **Δ‑2/Δ‑3** change (i.e., the **normative surface** or **semantics** changed) counts as a pattern change in the canonical corpus and triggers harness & bridge reviews.

### 4.4 Quality & SoTA metrics (selection lenses)

**Mandatory lenses** (declare in LAT; higher is better unless noted):

* **Clarity** (readability; plain‑register score from didactic rubric).
* **Universality** (C‑1): *≥3 heterogeneous domains* anchored in the Archetypal section.
* **Lexical discipline** (E.10): 0 violations (DevOps lexicon, process/function conflations).
* **Assurance delta**: ΔF (formality), ΔG (scope clarity), ΔR (reliability after CL penalties).
* **Bridge integrity**:  Bridge integrity (policy lens): declare minimum CL thresholds per Context policy; penalties route to R only (B.3/F.9); record policy‑id in LAT.
* **Test conformance**: F‑suite pass; RSCR clean.
* **Exploration health** (NQD): diversity coverage > threshold; no premature convergence.
* **Didactic economy**: length vs density ratio within band; “Tell‑Show‑Show” present.

**Optional lenses** (context‑specific): *Ethical/SoD guard strength; cross‑scale roll‑up integrity; aggregation proofs present;* etc.

---

## 8) Operators (authoring deltas you are allowed to apply)

* **Refine** (tighten CC without changing acceptance meaning).
* **Split/Merge** (factor patterns; preserve links; update Bridges).
* **Generalise/Constrain** (expand/restrict ClaimScope (G) with proofs or loss notes).
* **Rephrase** (clarify language; leave CC untouched).

Each operator carries a default **Delta‑Class** and test obligations.


---

## E.16 — RoC‑Autonomy: Budget & Enforcement \[A]

**Intent.** Make any claim of autonomous behavior testable and enforceable via a published **AutonomyBudgetDecl**, **Guarded enactment**, **Override SpeechActs with SoD**, and a **Work‑anchored AutonomyLedger**. 
**Rule (summary).** If a Role/Method/Service claims autonomy, authors **MUST**: (i) publish an `AutonomyBudgetDecl` with `AdmissibilityConditionsId` and `OverrideProtocolRef`; (ii) gate Method steps with `requiresAutonomyBudget`; (iii) write a `AutonomyLedgerEntry` on every admitted Work; (iv) block on depletion until a `ResumeAutonomy` SpeechAct passes SoD; (v) surface autonomy fields in UTS rows.

**Builds on:** A.2 / A.2.1 / A.2.5 / A.15; B.3; E.8; E.10; E.11; F.4; F.6; F.15; F.17.
**Coordinates with:** A.13 (Agential Role), C.9 (Agency‑CHR), C.24 (Agent‑Tools‑CAL) where applicable; G.4–G.5–G.8–G.9–G.10 (method authoring/selection/shipping).

### 1) Problem Frame

Autonomy‑claiming **performers** (*RoleAssignments* over services/robots/teams operating without continuous human direction) must **stay within declared limits** (safety, risk, resource, remit) and **yield** to governance when required. Without a uniform rule, “autonomy” drifts into tacit norms, cannot be benchmarked or audited, and undermines selection (Part G) and publication (Part F).

### 2) Problem

* **Opaque autonomy.** Patterns assert “autonomous” behavior with no **budget** or **enforcement**.
* **Un‑gated execution.** Methods can execute beyond authority or risk limits.
* **Ad‑hoc overrides.** No standard **SpeechAct** for pausing/de‑scoping; SoD is unclear.
* **Non‑portable publication.** **UTS (Unified Term Sheet)** rows cannot surface autonomy‑critical data for parity or selection.

### 3) Forces

| Force                          | Tension                                                                  |
| ------------------------------ | ------------------------------------------------------------------------ |
| **Creativity vs Safety**       | Exploration autonomy vs hard constraints and override duties             |
| **Locality vs Comparability**  | Context‑local rules vs cross‑context selection (G‑suite)                 |
| **Simplicity vs Auditability** | Lightweight authoring vs ledger‑grade evidence                           |
| **Autonomy vs SoD**            | Helpful self‑action vs separation‑of‑duties and human‑in‑the‑loop points |

### 4) Solution — **Rule‑of‑Constraints (RoC) for Autonomy**

This RoC **applies whenever** a Role/Method/Service **claims autonomous operation** (any phrasing that implies unsupervised decision or actuation).

**E.16‑S1 (Autonomy Budget — mandatory).**
Any autonomy claim **MUST** publish an **AutonomyBudgetDecl** as a *named, versioned* object in the **same `U.BoundedContext`**:

```
AutonomyBudgetDecl {
  id, version
  scope: ClaimScope (G)                              // where this budget applies
  budget: {                                          // all typed via MM‑CHR (C.16)
    action_tokens?     : Unitful quota / rate
    decision_tokens?   : Unitful quota / rate
    risk_envelope?     : CHR vector with acceptance bands
    resource_caps?     : set of unitful caps (Γ_work categories)
    time_window?       : Γ_time window & cadence
  }
  AdmissibilityConditionsId : policy-id                          // Aut-Guard policy naming gates & penalties
  overrideProtocolRef : Episteme                     // SpeechAct & SoD for pause/resume/escalate
  telemetrySpecRef? : Episteme                       // what to emit into AutonomyLedger
  editionPins : { RoleRef?, MethodDescRef?, CHR refs, ... } 
}
```

**E.16‑S2 (Guarded enactment — Green‑Gate).**
A **Method step** that *requires* autonomy **MUST** list `requires: [RoleX]` **and** `requiresAutonomyBudget: AutonomyBudgetDecl.id`. A **Work** instance is admissible *iff* at enactment time:

* the performer’s **RoleAssignment** is valid and in an **enactable** RSG state (A.2.5);
* the budget accounting for the **AutonomyBudgetDecl** indicates **tokens/limits remaining** for *this* budget in the declared **Γ_time** window (derived from the AutonomyLedger);
* all **guard checks** defined by `AdmissibilityConditionsId` evaluate to **pass** (e.g., risk ≤ band, resource ≤ cap).

Failing any gate **blocks** enactment (no “soft warnings” on Core surface).

**E.16‑S3 (Autonomy Ledger).**
All admissible Work **MUST** record **AutonomyLedger entries**:

```
AutonomyLedgerEntry {
  workId, performedBy: RoleAssignmentId
  budgetId, version, time
  deltas: { action_tokensΔ?, decision_tokensΔ?, riskΔ?, resourceΔ? }
  guardVerdicts: { name → pass|fail }
  pathIds: { PathId, PathSliceId }                  // for G‑suite parity/refresh
}
```

The ledger is **evidence**: attach to `U.Work` (A.15.1) and fold under **Γ_work** and **Γ_time** for reporting.

**E.16‑S4 (Overrides — SpeechActs & SoD).**
Every budget **MUST** reference an **OverrideProtocolRef** that defines canonical **SpeechActs**:

* **PauseAutonomy(budgetId)** — immediate stop of autonomy‑gated steps;
* **ResumeAutonomy(budgetId)** — resume after conditions;
* **NarrowAutonomy(budgetId, Δscope)** — apply stricter limits;
* **Escalate(budgetId)** — handover to a declared **SupervisorRole**.

**SoD:** The override caller **MUST NOT** be the same **RoleAssignment** that is consuming the budget (enforce `⊥` in the Context). All overrides are **Work** (SpeechActs) with **ledger entries** (zero or negative deltas as per policy).

**E.16‑S5 (Depletion behavior).**
When a budget **depletes** (no tokens / envelope exceeded / cap breached):

* **Block** further autonomy‑gated steps in the **same Γ_time window**;
* Emit **DepletionNotice** (SpeechAct), and either **Escalate** or **Park** per policy;
* Only a **ResumeAutonomy** SpeechAct from an admissible Role (per SoD) may reopen the gate.

**E.16‑S6 (Publication in UTS).**
UTS rows that describe a **Role**, **Method**, **Service**, or **Selector** with autonomy **MUST** include:

* `AutonomyBudgetDeclRef` (id & version);
* `Aut-Guard policy-id`;
* `OverrideProtocolRef`;
* declared **Scope (G)** and **Γ_time** window;
* edition pins for the referenced Role/Method/CHR.
* *(optional, if a scale preference is declared)* `ScaleLensPolicyRef` and `ScaleLensOptIn ∈ {OptedIn, Neutral, OptedOut}`.

**E.16‑S7 (Scale & selection — optional lens).**
When autonomy interacts with open‑ended search (C.18/C.19), **budget consumption** and **guard violations** are **selection lenses** in Part G (G.5/G.9). Applying a **Scale‑Lens / Bitter‑Lesson** preference is **OPTIONAL**. Authors **MAY** declare a **ScaleLensPolicy** for the autonomy claim; when declared, it **MUST** state:
* **Trigger criteria** — evidence that expected utility‑of‑scale is monotonic/non‑saturating on held‑out tasks, and a threshold at which scaling beats structured heuristics.
* **Budget fit** — compute/latency/cost targets **within** the declared `AutonomyBudgetDecl` (Γ_time, resource_caps).
* **Safety invariants** — guards and SoD remain **non‑weakened** under scaling; no policy may bypass E.16 gates.
* **Fallback** — a degrade‑gracefully plan if scaling fails to clear the trigger criteria within budget.
If no **ScaleLensPolicy** is declared, selection remains **neutral** with respect to Bitter‑Lesson; RoC does **not** authorize ignoring scale‑safety guards under any policy.

### 5) Archetypal grounding (Tell‑Show‑Show; human‑centric)

**Show‑A (U.System — mobile robot).**
`Robot_R7#NavigatorRole:Warehouse_2026` executes `Navigate_v3`.
`AutonomyBudgetDecl`: `action_tokens=10 k steps/day`, `risk_bands={maxSpeed ≤ 1.2 m/s, minDist ≥ 0.5 m}`, `resource_caps={battery ≥ 20%}`; `AdmissibilityConditionsId=Aut‑Guard‑R7‑v1`; override via `PAUSE`, `RESUME`, `ESCALATE` SpeechActs by `FloorSupervisorRole ⊥ NavigatorRole`. Ledger entries decrement `action_tokens`, track `minDist`. Depletion at 0 tokens halts autonomous moves and pages supervisor.

**Show‑B (U.Service — autonomous deploy).**
`DeployerRole` performs step “Promote to prod” under `AutonomyBudgetDecl` with `decision_tokens=3/day`, `risk_envelope={error‑budget burn ≤ 2% / day}`, guard “all pre‑deploy checks pass”. Overrides only by `CABChair#AuthorizerRole ⊥ DeployerRole`.
→ **Edit:** use `risk_bands` for consistency: `risk_bands={error‑budget burn ≤ 2% / day}`.

### 6) Conformance Checklist (SCR — E.16‑CC)

| ID            | Requirement                                                                                                                                                                 |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **E.16‑CC‑1** | Any autonomy claim **MUST** reference an **AutonomyBudgetDecl** in the same `U.BoundedContext`.                                                                             |
| **E.16‑CC‑2** | **Method steps** that depend on autonomy **MUST** name the `AutonomyBudgetDecl.id` and **MUST** be Green‑Gated by the budget’s guards at enactment.                         |
| **E.16‑CC‑3** | A **Work** admitted under autonomy **MUST** carry an **AutonomyLedgerEntry** with deltas and guard verdicts.                                                                |
| **E.16‑CC‑4** | **Overrides** are **SpeechActs** with SoD enforced (`⊥` between consumer and overrider roles); each override creates a ledger entry.                                        |
| **E.16‑CC‑5** | **Depletion** **MUST** block autonomy‑gated steps until a **ResumeAutonomy** SpeechAct passes SoD and guard checks.                                                         |
| **E.16‑CC‑6** | **UTS rows** for autonomy‑bearing Roles/Methods/Services **MUST** include `AutonomyBudgetDeclRef`, `Aut-Guard policy-id`, `OverrideProtocolRef`, `Scope (G)`, and `Γ_time`. |

### 7) Consequences

* **Testability.** Autonomy is measurable (tokens/envelopes), audit‑ready (ledger), and stoppable (SpeechActs).
* **Comparability.** UTS surfaces autonomy metadata for fair selection & parity.
* **Safety.** Guards are hard gates; depletion halts further autonomy‑gated Work.

### 8) Rationale & E‑/F‑/G‑links

* **E.8** — follows the pattern template (Context → Problem → Forces → Solution → Grounding → CC → Consequences).
* **E.10** — uses LEX‑BUNDLE: Scope via **ClaimScope (G)**, time via **Γ_time**, no “validity/process/actor/agent‑as‑noun” language; new lexical rule **L‑AUTO** added in edits below.
* **E.11 (ATS)** — authoring‑tier gates who may **mint** budgets/guards vs who may **use** them (diff below).
* **Part F** — integrates with **F.4** Role Description (RCS includes *AgencyLevel*; RSG gates), **F.6** Role Assignment & Enactment (Green‑Gate), **F.15** SCR/RSCR (harness includes depletion/override tests), **F.17** UTS (columns, incl. optional ScaleLens fields).
* **Part G** — **G.4/G.5**: method authors must declare budgets & guards; **G.9** parity includes autonomy consumption & violations; **G.10** shipping requires UTS autonomy fields.
