## G.4 — **CAL Authoring: Calculi · Acceptance · Evidence** \[A]

**Tag:** [A] (publishes CAL; consumes CHR; constrains LOG & G.5; binds **ATS/E.11**; exposes **ReferencePlane** and **Φ‑policy ids** to **SCR**)
**ATS conformance note.** Any **cross‑tier import** (AT0↔AT1↔AT2↔AT3) **MUST** pass **E.11 AH‑2/3/4** (Gate/Lane/Lexical); failure is **blocking** for CAL publication (register as **RSCR** defect).
**Stage:** *design‑time* (authoring & publication; enables lawful run‑time evaluation)
**Primary hooks:** G.1 CG-Frame Card; G.2 SoTA Synthesis Pack; **G.3 CHR Pack**; **G.5 Dispatcher** (MethodFamily & **GeneratorFamily** registry); **KD‑CAL F–G–R** (B.3, B.1 Γ‑fold); **MM‑CHR discipline** (A.17–A.19/C.16); **Contexts & Bridges + CL** (F.1–F.3, F.9); **UTS & naming** (F.17–F.18); **RoleAssignment** (F.4); **RSCR** (F.15); **E/E‑LOG** (C.19); **SoS‑LOG** (C.23); **ATS** harness **AH‑1..AH‑4** (E.11); **Lexical rules** (E.10); **Design–Run split** (A.4); **Telemetry/Refresh** (G.11).

### 1) Intent

Provide a **notation‑independent authoring discipline** to turn CHR‑typed measurement (from **G.3**) and SoTA plurality (from **G.2**) into a **lawful calculus layer (CAL)** that is **portfolio‑aware** (partial orders return **sets/archives**, not forced scalars) and **ATS‑ready**:

* **Operators** (transform, compare, aggregate, optimize, decide),
* **Acceptance Clauses** (typed predicates for *fit‑for‑purpose*), and
* **Evidence wiring** (F–G–R lanes, Γ‑fold integration, CL routing, **ReferencePlane** and **Φ‑policy id** publication),

so that run‑time **LOG** bundles and the **G.5** selector can execute choices **safely, auditably, and with scope/trust visible**.

### 2) Problem frame

You have a **CG-FrameContext** (G.1), a **SoTA Synthesis Pack** (G.2), and a **CHR Pack** (G.3) with Characteristics/Scales/Levels/Coordinates and **Guard Macros**. Before any method is dispatched (G.5), the **CAL layer** must specify *what operators exist*, *what they legally do over the CHR types*, and *what counts as acceptable outcomes under declared scope (G) and assurance (F–R)*. Where only **partial orders** are lawful, **G.5** will return **non‑dominated sets (Pareto/archives)** under **E/E‑LOG**; CAL must not impose scalarization.

### 3) Problem

Teams repeatedly face:

* **Illicit operations** (hidden cardinalization; unit laundering; ordinal arithmetic).
* **Opaque acceptance** (thresholds scattered; no typed predicates; no Γ‑fold).
* **Unstated assumptions** (regularity, noise, independence) that break comparability.
* **Evidence ambiguity** (what lane? how to aggregate? where do CL penalties land?).
* **Tool entanglement** (vendor flags baked into core logic).

### 4) Forces

* **Power vs. safety.** Expressive operators vs. strict legality under **MM‑CHR**.
* **Pluralism vs. unification.** Preserve Tradition‑specific calculi vs. a common **typed** substrate.
* **Pedagogy vs. proof burden.** Make acceptance teachable while binding **proof obligations**.
* **Locality vs. portability.** Keep Context‑local semantics yet prepare **Bridges** (with **CL** and loss notes).
* **Exploration vs. exploitation.** Enable **NQD/E/E‑LOG** probing without leaking un‑assured results.

### 5) Solution — *CAL Authoring chassis* (C1–C9)

**C1 · CAL Charter (scope anchor)**
**Inputs:** CG-FrameContext (G.1), SoTA Pack (G.2), CHR Pack (G.3). CAL traces supporting SoTAPaletteDescription MUST identify KD‑CAL lanes used (TA / LA / VA) and expose any lane‑dependent tolerances. Cross‑lane comparisons are forbidden unless an explicit **Bridge** with declared **CL** and loss notes is provided; penalties route to **R_eff** only.
**Ops:** declare **TaskKinds** and **ObjectKinds** *in the home Context*; state **assumption envelopes** (data shape, noise, independence, stationarity), **USM ScopeSlice(G)**, and **evidence lanes** intended per KD‑CAL (e.g., TA/LA/VA);  enumerate intended **CG‑Spec.characteristic ids** **iff** any numeric comparison/aggregation will be performed in this CAL pack; declare **ReferencePlane** for any cross‑plane readings and the **freshness_window**/**Γ_time** policy to be used by EvidenceProfiles.
**Outputs:** `CAL.Charter@Context` (design‑time stance) + `TaskMap`.
**Guards:** A.4 split; F.1–F.3 Contexting; E.10 lexical hygiene; **E.11 ATS** (GateCrossing recorded with **Bridge id**, **PathSliceId**, **CL**; non‑conformance blocks publication).

Any cross‑Tradition or cross‑lane reduction MUST declare a CL bridge with explicit loss notes. Such reductions contribute a penalty term to Γ‑fold and are ineligible for “universal” aggregation.

**C2 · Operator Cards (typed & lawful)**
Define **OperatorCard** as the core unit:

```
OperatorCard :=
⟨ UTS.id, Context, Lineage/Tradition, Intent,
  Signature: X → Y over CHR types,
  Preconditions (typed; Guard Macros),
  Postconditions (typed; invariants),
  Evidence lanes used (KD‑CAL),
  Complexity/Cost cues,
  Failure modes & safe degradations,
  Micro‑examples, Bridges (+CL, loss notes) if any ⟩
  CG‑Spec refs: ids of CG‑Spec.characteristics used for any numeric comparison/aggregation; ReferencePlane note (if non‑home); policy‑ids Φ(CL), Φ_plane to be cited by LOG/SCR.
```

*Signatures* reference **CHR** types (Characteristics/Scales/Units/Coordinates).
**Guards:** `UNIT_CHECK`, `ORD_COMPARE_ONLY`, `POLARITY_CHECK`, `CYCLIC_DIFF`, `FRESHNESS_CHECK`, `PLANE_NOTE`, `PHI_CL_MONOTONE(policy_id)`.
**Outputs:** `CAL.Operator[]` (versioned; UTS‑published with twin labels).

**C3 · Acceptance Clauses (typed predicates)**
Craft **AcceptanceClause** as a minimal, typed grammar:

```
AcceptanceClause :=
⟨ ClauseId (UTS), applies_to: {TaskKind|OperatorId},
  CharacteristicRefs: CHR.Characteristic[],      // explicit binding to CHR ids
  CGSpecRefs?: CG‑Spec.characteristic[],         // REQUIRED iff Pred induces any numeric comparison/aggregation
  EvidenceProfileRefs?: CAL.EvidenceProfile[],   // provenance hooks for SCR/LOG (C5)
  Pred := boolean formula over CHR‑typed observables
          + CAL outcomes + Scope(G) + Resource envelope,
  Thresholds declared (Context‑local),
  Freshness: `freshness_window` and `Γ_time` selector (lane‑aware),
  UnknownHandling: {pass|degrade|abstain}, // tri‑state per G.0; "sandbox" is a LOG‑level degrade mode
  Dependence on evidence lanes (KD‑CAL) and ReferencePlane,
  Failure policy (degrade/abstain/escalate) ⟩
```

*Thresholds live here*, **not** inside CHR. Clauses are **design‑time** artifacts that run at selection/evaluation time.
**Outputs:** `CAL.Acceptance[]` (publish to UTS).
**Guards:** **No global thresholds**; cross‑Context reuse via **Bridge + CL** only.
"**Rule:** thresholds **live only in AcceptanceClauses**; if a clause induces comparison/aggregation, cite the CG‑Spec characteristic id; otherwise degrade to order‑only or **abstain**."
**Idiom (MaturityFloor).** Contexts MAY author `AC_MaturityFloor(MethodFamilyId, rung≥Lk)` as a typed predicate over the published `MaturityCard@Context` (C.23). The selector/SoS‑LOG MUST reference this clause by id; no maturity thresholds are embedded in LOG.
**UnknownHandling:** predicates MUST define behavior for `unknown` (tri‑state from **TaskSignature/CHR Missingness** and **ShiftClass**), recorded in SCR; default SHALL NOT coerce to numeric 0/−∞; when **ShiftClass=unknown|non‑iid**, families MAY **degrade** or **abstain** with scope notes (LOG‑executable branch ids). LOG‑level **sandbox/probe‑only** modes, if used, are expressed in **SoS‑LOG** branches, not as Acceptance outcomes. **Clauses SHALL expose stable `clauseId` for SoS‑LOG citation.**
**ATS hooks:** Acceptance must expose **GateCrossing ids** (E.11 AH‑1..AH‑4) for clause‑triggered gates; failures are *blocking* for publication.

**C4 · Aggregation & Comparison Flows (safe by construction)**
Compose operators via **FlowSpecs** with legality checks:

```
FlowSpec := DAG of OperatorIds
  + Admissible Aggregators (from CHR.AggregationSpecs)
  + Γ-fold hints for R-aggregation
  + Unit/scale checks at each edge
```

Provide **typed templates** (lexicographic, Pareto with explicit **non‑dominated set** output, ε‑Pareto thinning, t‑norms, medoid/median, affine sums for interval/ratio only with unit alignment). **If only a partial order is lawful, the Flow returns a set (portfolio/archive), never a forced scalarization.** Record **ReferencePlane** for every numeric edge.

**Outputs:** `CAL.Flow[]` + legality proofs/links.
**Guards:** Ordinal **MUST NOT** be averaged/subtracted; unit mismatches **fail fast**.

**C5 · Evidence Wiring & Γ‑fold (R aggregation)** (declare **TA/LA/VA lanes + describedEntity‑E0 fields readable to SCR; Γ = weakest‑link unless proven otherwise; **Φ‑policies must be monotone and bounded**)
For each Operator/Flow, define **EvidenceProfile**:

```
EvidenceProfile :=
⟨ lanes ∈ KD‑CAL[], anchors (A.10 carriers),
  contribution to R via Γ-fold,
  CL penalties routing (to R_eff; never to F),
    ageing/decay policy (B.3.4),
  freshness_window (Γ_time selector),
  edition semantics for illumination/archives (see C6) ⟩
```

Ship a **default Γ‑fold = weakest‑link**, overridable with proof of monotonicity & boundary behavior.
**Outputs:** `CAL.EvidenceProfiles` + **SCR** fields to be emitted at run‑time.

Record **ReferencePlane** on each EvidenceProfile row and publish **Φ(CL)**/**Φ_plane** **policy‑ids** (table‑backed) for every predicate branch; **No self‑evidence** (A.10); unknowns escalate to {degrade|abstain} at Acceptance, with any **sandbox/probe‑only** handling modeled as a **SoS‑LOG** branch; penalties route to **R_eff only** (never F/G).

**Publication hook for LOG.** EvidenceProfiles **SHALL** expose `profileId` and record **ReferencePlane**; these ids are **citable** from SoS‑LOG rules (C.23).

**C6 · NQD Operators & Explore↔Exploit Policy Surface (QD & OEE‑ready)**
Where the CG-Frame needs search/generation, define **NQD‑class** operators with explicit:

* **Portfolio coverage** obligations (C.18) and **QD‑metric triad**: *Quality (Q)*, *Diversity (D)*, *QD‑score*.
* **Risk budgets** and **probe accounting** under **E/E‑LOG**.
* **Illumination mode:** declare **Descriptor space** as `U.DescriptorMap (Tech; d≥2)` with its **CharacteristicSpace (Plain)** twin (E.10); provide `ArchiveRef`, **InsertionPolicyRef** (from G.5), and **IlluminationSummary := gauge over Diversity_P**; record **Edition := {DHCMethodRef.edition, DistanceDefRef.edition}** on `DescriptorMapRef/ArchiveRef`. By default **Illumination does not enter dominance** unless an explicit policy id (Φ) says otherwise.
* **OEE/GeneratorFamily support:** where tasks/environments are co‑evolved, register **GeneratorFamily (POET‑class)** with `EnvironmentValidityRegion` and `TransferRules`; author **Acceptance/SoS‑LOG branches** for {environment, method} pairs.
* **Emission trace** schema (who/why/where → VariantPool metadata for G.1/M3), including **edition** bumps for archives/descriptors and the active **policy‑id**.

+**Outputs:** `CAL.NQD[]` + policy knobs the **G.5 selector** can read (**EmitterPolicyRef**, **ArchiveRef**, **DescriptorMapRef** with **Edition{DHCMethodRef.edition, DistanceDefRef.edition}**, **IlluminationSummary**, **Q/D/QD‑score**).

**Guards:** Probes **MUST** respect AcceptanceClauses; unsafe probes **MUST** abstain or sandbox.

**C7 · Proof Obligations & Soundness Ledger**
For each Operator/Flow/Acceptance, attach **obligations**:
* **Measurement legality** (scale/unit/polarity),
* **Monotonicity / idempotence / stability** of aggregators,
* **Assumption checks** (e.g., independence, convexity),
* **Φ‑policy monotonicity/boundedness** (Φ(CL), Φ_plane) per published policy id (explicit link to EvidenceProfile rows),
* **Degradation conditions** (when to drop to ordinal or abstain) and **tie‑handling rules** for partial orders (why a set is returned).

* Log proofs or references; if empirical, bind to KD‑CAL lanes and A.10 carriers.
* AcceptanceClause.Sketch: if CGSpecRefs ≠ ∅ then attach ProofRef: CAL.ProofLedger.Id (**A.18 CSLC** check)

**Outputs:** `CAL.ProofLedger` (linked from UTS).
**Guards:** Missing proofs **MUST** be visible in **SCR** (severity affects **R**, not **F**).

**C8 · Publication, RSCR, and Bridges**
Publish all CAL artifacts to **UTS** (with twin labels; Context noted; Bridges + CL + loss notes). Register **RSCR** tests:

* Refuse illegal ops (e.g., `mean(ordinal)`),
* Enforce **Guard Macros**,
* Check Flow unit/scale coherence,
* Verify **AcceptanceClause** semantics on Worked‑Examples; verify **ε‑Pareto** non‑scalarizing behavior; verify **freshness_window** enforcement.

**Outputs:** `CAL Pack@CG-Frame` + RSCR ids + Worked‑Examples + deprecation notices (F.13).
**Guards:** E.5.\* (no tool lock‑in); lexical continuity (F.12/F.14).

**C9 · Packaging & Refresh**
Version the CAL pack; set **refresh cadence** (evidence decay, probe telemetry, SoTA deltas). Track change‑impact to AcceptanceClauses and Flows; emit **deprecation** and **lexical continuity** notes. Record **PathSliceId** for telemetry updates and **edition** changes for archives/descriptors.
**Outputs:** Versioned `CAL‑Pkg@CG-Frame` + refresh hooks.
**Guards:** A.4 temporal duality; B.4 change rationale logged in **DRR**/**SCR**.

### 6) Interfaces — minimal I/O Standard

| Interface             | Consumes                                 | Produces                                                                          |
| --------------------- | ---------------------------------------- | --------------------------------------------------------------------------------- |
| **G.4‑1 Charter**     | CG-FrameContext (G.1), SoTA Pack (G.2), CHR | `CAL.Charter@Context`, `TaskMap`                                                     |
| **G.4‑2 Operators**   | CHR types, SoTA operator inventory (G.2) | `CAL.Operator[]` (UTS ids; legality guards; EvidenceProfiles)                     |
| **G.4‑3 Acceptance**  | TaskMap, policy intents, CHR guards      | `CAL.Acceptance[]` (typed clauses; thresholds; failure policies)                  |
| **G.4‑4 Flows**       | Operators, CHR AggregationSpecs          | `CAL.Flow[]` (typed pipelines; Γ‑fold hints; legality proofs)                     |
| **G.4‑5 NQD Surface** | CHR types, E/E‑LOG policy                | `CAL.NQD[]` (emitters; risk budgets; telemetry schema)                            |
| **G.4‑6 Publish**     | All above                                | Versioned `CAL Pack@CG-Frame`, RSCR tests, Worked‑Examples, Bridges/CL, deprecations |

**Notes:** `CAL.NQD[]` SHALL expose `DescriptorMapRef`, `ArchiveRef`, **IlluminationSummary**, and publish **Q/D/QD‑score** fields; all Interfaces emitting numeric comparisons **MUST** cite **CG‑Spec.characteristic ids** and **ReferencePlane**.

### 7) Payload (what G.4 exports)

1. **CAL Pack\@CG-Frame** (folder):

   * `CAL.Operator[]` (cards, signatures, guards)
   * `CAL.Acceptance[]` (typed clauses)
   * `CAL.Flow[]` (composition with legality checks)
   * `CAL.EvidenceProfiles` + **Γ‑fold** annotations (with **ReferencePlane** & **Φ‑policy ids**)
   * `CAL.NQD[]` (if applicable; with `DescriptorMapRef`, `ArchiveRef`, **IlluminationSummary**, **Q/D/QD‑score**, **edition**)
   * `CAL.ProofLedger`
   * **UTS entries** (Name Cards, twin labels, Bridges + CL/loss notes)
   * **RSCR** tests + **Worked‑Examples**
1. **Hand‑off manifests** to **G.5** (Eligibility Standards derive from Operator/Flow preconditions; Acceptance as selector gates; Evidence to **SCR**).

### 8) Conformance Checklist (normative)

1. **Context declared.** Every CAL artifact has a **home Context**; cross‑Context reuse requires **Bridge + CL + loss note**.
2. **Typed throughout.** Signatures, predicates, and flows **MUST** use **CHR** types (Characteristics/Scales/Units/Coordinates).
3. **Legality enforced.** **Guard Macros** from **G.3** are attached and **RSCR‑tested**; ordinal arithmetic **MUST NOT** be performed.
4. **CG‑Spec & CSLC.** Any operator/flow/acceptance that induces **numeric** comparison/aggregation **MUST** cite the **CG‑Spec.characteristic id** and **prove CSLC legality**. In Acceptance, supply `CGSpecRefs` and a `ProofRef` to the **CAL.ProofLedger**; otherwise **degrade/abstain**. Where only a partial order is lawful, the Flow returns a **set (Pareto/archive)** with optional **ε‑thinning**; **no forced scalarization**.
5. **CHR binding in Acceptance**. `AcceptanceClause.CharacteristicRefs` SHALL enumerate CHR characteristics used by each threshold/comparison (machine‑checkable).
6. **Evidence link in Acceptance**. `AcceptanceClause.EvidenceProfileRefs` SHALL list EvidenceProfile ids consulted by the clause so SCR can surface Φ(CL)/Φ_plane policy‑ids per branch.
7. **C.21 guard‑bands live only in Acceptance** (no thresholds embedded in CHR); cross‑plane penalties recorded (**Φ_plane**) **with policy‑ids**; **no distance language**.
8. **Acceptance explicit.** All thresholds/policies live in **AcceptanceClauses**, not in CHR or Operator definitions.
9. **Evidence wired.** Each Operator/Flow declares lanes and anchors; **CL penalties** route to **R_eff** only (not **F**).
10. **Γ‑fold & freshness recorded.** R aggregation rule (default **weakest‑link**) is stated; **freshness windows** are declared; contributors appear in **SCR**; **Φ‑policies** are cited by id and shown to be monotone/bounded.
11. **Degradation safe.** When assumptions fail, flows **MUST** degrade (e.g., cardinal→ordinal) or **abstain**, never perform illegal ops.
12. **No tool lock‑in.** No vendor keywords in core fields; implementations live under **E.5.\***.
13. **Lifecycle set.** Refresh/decay declared; deprecations follow **F.13–F.14** with **Lexical Continuity** notes.
14. **UTS‑ready.** Names minted/reused; twin labels present; **Worked‑Examples** attached.
15. **Φ‑policies monotone.** **Φ(CL)** and **Φ_plane** **MUST** be **monotone** and published by **policy id**; penalties route to **R_eff only** (never **F/G**). **Illumination** enters dominance **only** if an explicit **CAL.Acceptance** policy authorises it (policy‑id recorded in SCR); Φ‑policies do **not** govern dominance.
16. **No self‑evidence (A.10).** EvidenceProfiles and Acceptance proofs **MUST NOT** rely on carriers produced by the same holon without an external **TransformerRole**; cyclic provenance fails acceptance.
17. **QD/OEE readiness.** If **NQD** or **GeneratorFamily** are present: (a) publish `DescriptorMapRef` (Tech; d≥2) and **CharacteristicSpace (Plain)**; (b) expose **Q/D/QD‑score** and **IlluminationSummary**; (c) record **edition** on archive updates; (d) declare `EnvironmentValidityRegion` and `TransferRules`; (e) Acceptance/SoS‑LOG branches exist for {environment, method}.
18. **No new U.Types for strategy/policy.** Strategies/policies are **compositions** governed by **E/E‑LOG** and registered via G.5, not minted as new core types.

### 9) Anti‑patterns & rewrites

* **Hidden thresholds.** *Don’t:* bake policy cut‑offs into CHR or code; *Do:* publish **AcceptanceClause** with Context‑local thresholds.
* **Operator without signature.** *Don’t:* “score(x)” with implicit units; *Do:* declare `Signature: Project × SafetyClass(ord) × CostUSD(ratio) → {ord, ratio,…}` and guards.
* **Globalized flows.** *Don’t:* reuse an optimization flow across Contexts without Bridge; *Do:* declare **Bridge + CL** and attach loss notes.
* **Evidence blur.** *Don’t:* cite “validated” without lane; *Do:* mark **KD‑CAL** lane(s) + anchors and Γ‑fold effect.
* **Design/run blur.** *Don’t:* trigger side effects inside selection; *Do:* keep selection pure (G.5), evaluation emits **DRR/SCR**.
* **Forced scalarization.** *Don’t:* collapse partial orders to a single score; *Do:* return **non‑dominated sets (Pareto/archives)** with optional ε‑thinning; let **G.5** dispatch portfolios.

### 10) Consequences

* **Safety by construction.** Illegal operations are blocked; acceptance becomes auditable.
* **Comparable plurality.** Rival calculi co‑exist as separate **Operator/Flow** families with explicit Bridges and **CL**.
* **Frictionless dispatch.** **G.5** reads typed **Eligibility** from CAL preconditions and gates by **AcceptanceClauses** with **SCR** ready.
* **Pedagogical clarity.** Operator/Acceptance cards + Worked‑Examples make the calculus teachable and inspectable; QD/OEE fields clarify illumination portfolios without over‑scalarization.

### 11) Worked micro‑example (indicative)

*CG-Frame:* **R\&D portfolio decisions** (same as G.1/G.3 for continuity).
**CHR recap:** `SafetyClass` (ordinal ↑), `CostUSD_2025` (ratio), `Readiness` (nominal).

**Operators:**

* `DominatesPareto : Project×Project → bool` over ⟨↓CostUSD, ↑SafetyClass⟩ with `ORD_COMPARE_ONLY(SafetyClass)` + `UNIT_CHECK(CostUSD)`; lane = **LA**.
* `BudgetFeasible : Portfolio → bool` with unit‑aligned sum; lane = **LA/VA**.
* `LexiMinSafety : Portfolio → SafetyClass` (aggregator = lexicographic min); lane = **LA**.

**AcceptanceClauses:**

* `AC_SafetyGate`: *must meet* `SafetyClass ≥ B` (ordinal predicate; Context‑local levels).
* `AC_Budget`: `TotalCostUSD_2025 ≤ Envelope`.
* `AC_Explain`: DRR must cite top‑3 trade‑offs; lane = **VA** for exemplars.

**Flows:**

* `Flow_SelectPareto`: filter by `AC_Budget ∧ AC_SafetyGate`, compute Pareto front via `DominatesPareto`; Γ‑fold = weakest‑link over **LA/VA**.
* `Flow_IlluminateAlternatives` (optional): run **NQD** over `U.DescriptorMap (Tech; d≥2)` with archive `ArchiveRef` and emitter `EmitterPolicyRef`; publish **IlluminationSummary** and **Q/D/QD‑score**; **does not enter dominance** unless Φ‑policy allows.

**Evidence:**

* CL penalty applied if `SafetyClass` is bridged from a *marketing* Context rating; penalty lowers **R_eff** only; **F** unchanged.
* EvidenceProfile rows cite **ReferencePlane** and **Φ‑policy ids**; telemetry records **edition** on any archive update.

Run‑time: **G.5** reads CAL preconditions/acceptance to form eligibility and gates; emits **DRR+SCR** citing Γ‑fold contributors.

### 12) Relations

**Builds on:** G.1, G.2, **G.3**; **MM‑CHR**; **F–G–R / KD‑CAL**; **Contexts/Bridges + CL**; **UTS**; **Role Assignment**.
**Publishes to:** **G.5** (eligibility, acceptance, evidence), **UTS**, **RSCR**, Worked‑Examples.
**Constrains:** any **LOG** implementation that executes these operators/flows; **SoS‑LOG** bundles MUST cite `clauseId`/`profileId` and honor portfolio/non‑scalarization contracts.

### 13) Author’s quick checklist

1. Write the **CAL Charter** and **TaskMap** for the CG-Frame.
2. For each SoTA operator candidate, author an **OperatorCard** with typed signature, guards, lanes, proofs/anchors.
3. Externalize all thresholds into **AcceptanceClauses**; define failure policies and safe degradations.
4. Assemble **Flows** using CHR‑approved aggregators; attach Γ‑fold hints and legality proofs.
5. Define **EvidenceProfiles** and **CL** routing; ensure **SCR** fields are computable.
6. Publish to **UTS** with twin labels and Bridges; register **RSCR** tests; ship **Worked‑Examples**.
7. Set **refresh/decay**; version the **CAL‑Pkg**; log change impact to **DRR/SCR**; wire **ATS gates (E.11)**; ensure **QD/OEE** fields (DescriptorMapRef, ArchiveRef, IlluminationSummary, Q/D/QD‑score, **edition**) are present when NQD is used.
