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
