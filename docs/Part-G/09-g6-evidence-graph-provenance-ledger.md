## G.6 — Evidence Graph & Provenance Ledger \[A]

**Tag:** \[A] **Stage:** design‑time (assembly) + run‑time (telemetry ingestion)
**Builds on:** A.10 (Evidence Graph Referring), B.3 (Assurance), G.4 (CAL.ProofLedger & EvidenceProfiles), F.9 (Bridges/CL), **C.18 (NQD‑CAL)**, **C.19 (E/E‑LOG & policies)**, **E.11 (ATS)**, E.8 (template), E.10 (LEX), C.23 (**Science‑of‑Science LOG**, SoS‑LOG hooks)
**Publishes to:** **Unified Term Sheet (UTS)** (twin‑label **Name Card**s), RSCR, G.5 selector (by PathId citation), **G.11 Telemetry/Refresh**
**Guards respected:** Notational independence (E.5.2), lexical discipline (E.10), lane separation (TA/VA/LA), CL→R routing only, Γ‑fold = WLNK unless proven otherwise

### 1) Problem frame

SoTA claims and operators are admitted (or rejected) by **assurance** signals derived from diverse artefacts. FPF already mandates **Evidence Graph Referring** (A.10) and lane discipline (TA/VA/LA) and defines how **F–G–R** is computed (B.3). What is missing as a **first‑class object** is the **typed, citable path** from a claim to its anchors, with declared scope/plane and penalties, so selectors, audits, and **maturity transitions** can cite *exactly what* justified a decision, *when*, and *under which plane/bridge penalties*. This pattern introduces that missing object and its surface.
**Why here (not in G.4)?** G.4 defines **CAL artefacts** (EvidenceProfiles, ProofLedger) and legality/aggregation rules; **G.6** packages the **cross‑artefact provenance** as a graph and **mints path identities** that downstream LOG and UTS can cite without copying evidence tables.

### 2) Problem

1. Readers cannot **audit CL penalties and decay** on SoTA claims without chasing many tables. 2) Cross‑Context reuse must prove penalties hit **R only** (not F/G) and expose the **lowest‑link** path; today this is implicit. 3) **Maturity** decisions (C.23) need a stable **PathId** to re‑check later or in other Contexts.

### 3) Forces

| Force                        | Tension                                                                                                                                                                                     |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Provenance vs agility**    | Fine‑grained audit trails ↔ friction for authors.                                                                                                                                           |
| **Lane purity vs synthesis** | Keep TA/VA/LA separable ↔ Publish a single *why* for admission.                                                                                                                             |
| **Notation independence**    | Define semantics in prose/math ↔ teams want diagrams/tables (kept informative only).                                                                                                        |
| **Design vs run**            | Evidence at design‑time vs telemetry at run‑time must not be conflated.                         |
| **Plane mixing**             | World↔Concept↔Episteme crossings must be penalised only in **R** and be table‑backed Φ‑policies. |

### 4) Solution — **EvidenceGraph** (notation‑independent; lane‑aware; path‑addressable)

**4.1 Definition (object).**
An **EvidenceGraph** is a **typed DAG** whose nodes are the **A.10 anchors/carriers and evidencing roles** and whose edges are minimal, normative provenance relations. Each node/edge carries attributes sufficient for the B.3 trust calculus and E.10 lexical discipline; edges never build mereology (A.10 firewall).

* **Nodes (informative types)**: `U.EvidenceRole` (holder = `U.Episteme`), `SymbolCarrier`, `TransformerRole` (external), `MethodDescription` (design), `Observation` (dated result); all resolvable to **SCR/RSCR** rows. **When QD/illumination or portfolio selection is involved (C.18/C.19), nodes MAY carry:** `U.DescriptorMapRef` **(with** `edition` **and** `DistanceDef` **ids)**, `ArchiveCellRef`, `EmitterPolicyRef`, and `InsertionPolicyRef` (K‑capacity & replacement semantics) **as attributes**.
* **Edges (normative vocabulary, minimal):** `verifiedBy` (formal line), `validatedBy` (empirical line), `fromWorkSet` (run‑time provenance), `happenedBefore` (temporal), `derivedFrom`.  
* **Informative only:** `usedCarrier`, `interpretedBy` MAY appear in SCR narratives but are not part of the normative edge set. **No mereology** here; structural relations publish via CT2R‑LOG.
* **Lane tags:** every binding is typed with **assuranceUse ∈ {TA, VA, LA}** and kept separable through to the assurance tuple and SCR display.
* **Context & Plane:** nodes and claims declare `U.BoundedContext` and **ReferencePlane**; any crossing uses a **Bridge** with **CL / CL^k / CL^plane** and **loss notes**, and **penalises only R** via published, table‑backed **Φ/Ψ** policies.
* **Freshness/decay:** empirical bindings declare **time windows**; on expiry they incur **Epistemic Debt** that must be resolved via refresh/deprecate/waive; proofs may fence to a **TheoryVersion** (no decay). **Editioned telemetry** MUST cite `PathSliceId` and any `U.DescriptorMapRef.edition` used to compute Illumination/QD metrics.
* **No self‑evidence:** evidencing `TransformerRole` is **external** to the evaluated holon.

**4.2 PathId (address for justifications)**.
A **PathId** is a **stable identifier** minted for a **claim‑local, lane‑typed path** in an EvidenceGraph under a declared **TargetSlice** (Scope G with Γ\_time selector) and **ReferencePlane**. PathIds are **editioned**; they denote a **proof spine** from the claim to carriers and include: the **lane split**, the **lowest CL on the path**, the **Γ‑fold in effect** (default = WLNK), **policy‑ids** **Φ(CL)** **and, if applicable,** **Φ\_plane**, and **valid‑until** (freshness) for empirical legs. PathIds are **citable from SoS‑LOG** and **UTS**; missing or stale PathIds **forbid maturity rung advance**.

**4.3 PathSliceId (time‑ & plane‑lifted slice).**
A **PathSliceId := PathId × Γ_time window × ReferencePlane**. It keys **release‑quality snapshots** and enables **path‑granular refresh** (G.11) when freshness or bridges change. **If QD/illumination is present, the PathSliceId MUST also pin** `U.DescriptorMapRef.edition` **and** `DistanceDefRef.edition` **to make front/coverage snapshots reproducible.** A PathSliceId MUST declare its Γ_time selector and plane; crossings require Bridge + CL^plane and route penalties to R only.

**4.4 Computation hooks (reusing B.3 & G.4, not redefining).**

* **Γ‑fold & penalties.** Unless justified otherwise in **CAL.ProofLedger**, **R** aggregates by **weakest‑link**, then applies **Φ(CL_min)**, any applicable **Ψ(`CL^k`)** (where a **KindBridge** is traversed), and **Φ_plane** (all **bounded, monotone**), and is **clipped**: `R_eff := max(0, …)`. **F = min**. **G** composes as **intersection along a path**; **SpanUnion** across **independent** lines only (see CC‑G6‑10/12). Penalties **never** modify F/G. **All numeric operations MUST be lawful per CG‑Spec (declared characteristic, unit/scale, Γ‑fold); illegal mixes trigger fail‑fast and RSCR.**
* **Lane separation.** Evidence lanes remain **separable** through to the assurance surface and SCR; no averaging across lanes.
* **Exposure to SCR.** Every path resolves to **SCR/RSCR** entries; the **Assurance SCR** displays node/edge values, describedEntity and plane, **TA/VA/LA table**, **valid‑until/decay**, and **Epistemic‑Debt**. **Mandatory fields:** lane‑split, **Γ‑fold contributors** (with ids), **Φ(CL)**/**Φ\_plane policy‑ids**, **PathId/PathSliceId**, and, when QD/illumination is involved, `U.DescriptorMapRef.edition` and `DistanceDefRef.edition` ids.
* **Reuse across Contexts.** Any cross‑Context/plane reuse must cite **Bridge ids + loss notes**; penalties route to **R\_eff only**; **policy‑ids** for Φ/Ψ are published in the SCR and CG‑Spec.

**4.5 Conceptual API (notation‑independent surface).**

* `Explain(pathId)` → returns lane‑split, **min R\_i**, **CL\_min**, applied **Φ/Ψ** policy‑ids, **valid‑until**, and the **contributing EvidenceProfile ids**.
* `PathsFor(claim, TargetSlice, plane)` → enumerates admissible paths, ordered by WLNK cutset; returns **PathId\[]**.
* `Snapshot(pathId | pathSliceId)` → emits an **RSCR‑grade** snapshot (for release, UTS) with **twin labels**; when a **PathSliceId** is provided, the snapshot is **time‑local** (no reweave).
  (These are **conceptual shapes**, not APIs; per E.5 they stay tool‑neutral.)

**4.6 RSCR triggers (conceptual).**
Edits that change **gauges/acceptance**, **Φ/Ψ policies**, **Bridge CL**, or **Γ‑fold** for a path **trigger RSCR**; **QD/OEE‑related edits** (e.g., `U.DescriptorMapRef.edition`/`DistanceDef`, `EmitterPolicyRef`, `InsertionPolicyRef`) **also trigger RSCR**. Selectors in G.5 must **re‑cite** PathIds on re‑run, or degrade/abstain per LOG duties.

> **Aphorism.** *“If you can’t point to a path, you don’t have provenance—only a story.”*

### 5) Archetypal Grounding (System / Episteme)

**System (Γ\_sys):** *Autonomous brake envelope claim*.
Claim: “Stop within 50 m from 100 km/h.” EvidenceGraph nodes: `verifiedBy` static‑analysis proof; `validatedBy` instrumented track tests; calibration carriers; external test lab as `TransformerRole`. **PathId** combines VA+LA legs; **R\_eff** = min(R\_i) − Φ(CL\_min); **G** is the **operational envelope** covered by tests; **F** limited by least‑formal leg. Freshness windows and decay are shown in SCR; any cross‑plant reuse applies **Scope Bridge** penalties to **R only**.

**Episteme (Γ\_epist):** *Vision benchmark SoTA (2015→) replication path*.
Claim: “Method family M attains parity on ImageNet‑style tasks.” EvidenceGraph nodes: replicated studies (LA), proof obligations for metric legality (VA), tool‑qualification declarations (TA). RSCR adapts vocabularies/units per Context; **Bridge** entries across sub‑traditions carry **loss notes** and **CL**. The **PathId** cited by SoS‑LOG at admission includes **ReferencePlane**, **Φ(CL)** policy ids, and **valid‑until** on rolling 24 mo windows.

### 6) Bias‑Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**.
Scope: **Universal** within the Conceptual Core; numerical policies (Φ/Ψ tables) remain **Context‑local** and are **cited by id**, not embedded, preserving independence and avoiding tool lock‑in.

### 7) Conformance Checklist (CC‑G6)

| ID                                     | Requirement                                                                                                                                              | Purpose                                                                                                                                                                                                                                 |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CC‑G6‑1 (Anchor & lanes)**           | Every path **MUST** resolve to A.10 anchors (SCR/RSCR) and declare **lane tags TA/VA/LA** on bindings.                                                   | Enforces evidential reality and lane separation. |
| **CC‑G6‑2 (No self‑evidence)**         | The evidencing `TransformerRole` is **external**; reflexive cases model a meta‑holon.                                                                    | Prevents circular proof.                                                                                                                     |
| **CC‑G6‑3 (Plane & Context declared)** | Each path **SHALL** declare `U.BoundedContext`, **ReferencePlane**, and (if crossing) the **Bridge id + loss notes**.                                    | Makes penalties auditable.                                                                                                                   |
| **CC‑G6‑4 (CL routing)**               | **Φ(CL)**, **Ψ(`CL^k`)** (when a **KindBridge** is used), and, if applicable, **Φ\_plane** penalties **reduce R\_eff only**; **F/G invariant**.          | Preserves scale/plane safety.                                                                                                                |
| **CC‑G6‑5 (Γ‑fold discipline)**        | **Declare Γ‑fold**; default is **weakest‑link**. Overrides **MUST** cite CAL.ProofLedger ids for monotonicity/boundary behaviour.                        | Legal aggregation without redefining B.3.                                                                                                   |
| **CC‑G6‑6 (Time & decay)**             | Empirical legs **MUST** expose **freshness windows** and **valid‑until**; expiry incurs **Epistemic Debt** with managed resolution.                      | Stops “latest” drift.                                                                                                                        |
| **CC‑G6‑7 (Design/run split)**         | EvidenceGraph **SHALL NOT** mix design‑time MethodDescription with run‑time Work traces in one node; use explicit instantiation bridges.                 | Avoids stance chimeras.                                                                                                                     |
| **CC‑G6‑8 (SCR surface)**              | For any **PathId**, the **Assurance SCR** **SHALL** list node/edge F,G,R, CL, describedEntity, plane, TA/VA/LA table, decay, and Epistemic‑Debt.               | Complete audit surface.                                                                                                                     |
| **CC‑G6‑9 (Citable PathIds)**          | **SoS‑LOG** decisions (admit/degrade/abstain) and **Maturity rung transitions** **MUST** cite **EvidenceGraph PathId(s)**. Absence forbids rung advance. | Stable justifications per C.23.                                                                                                              |
| **CC‑G6‑10 (Independence note)**       | If a **SpanUnion** of evidence lines is claimed, publish the **independence justification**.                                                             | Lawful enlargement of G.                                                                                                                     |
| **CC‑G6‑11 (UTS hooks)**               | Evidence artefacts and PathIds **MUST** be **UTS‑citable** with twin labels (Tech/Plain).                                                                | Publication discipline.                                                                                                                     |
| **CC‑G6‑12 (IndependenceCertificate)** | Independence for any **SpanUnion** MUST be carried by a **USM (`A.2.6 §7.3`) IndependenceCertificate** (partition of essential components; reference id in SCR). | Makes SpanUnion auditable and machine‑checkable. |
| **CC‑G6‑13 (Mandatory SCR/DRR fields)** | SCR/DRR for any cited path **MUST** expose: lane‑split, **Γ‑fold contributors (ids)**, **Φ(CL)**/**Φ\_plane** policy‑ids, **PathId/PathSliceId**; with QD/illumination also expose `U.DescriptorMapRef.edition` and `DistanceDefRef.**edition**` ids. | Ensures lawful, reproducible audits and refresh. |
| **CC‑G6‑14 (Legality of numeric ops)** | Any numeric comparison/aggregation in paths **MUST** cite **CG‑Spec** (characteristic id, unit/scale, Γ‑fold). **Fail‑fast** on CSLC violations; no ordinal→cardinal promotion. | Prevents illegal arithmetic and hidden assumptions. |
| **CC‑G6‑15 (Editioned QD/OEE telemetry)** | Ingested QD/illumination or OEE events **SHALL** record `U.DescriptorMapRef.edition`, `EmitterPolicyRef`, `InsertionPolicyRef`, and (for OEE) `EnvironmentValidityRegion`/`TransferRules` refs. | Reproducible fronts/coverage and environment lineage. |

### 8) Interfaces & Hooks (normative)

Each hook below defines: **Trigger → Obligation → Publishes/Consumes → Invariants**.

#### **H1 — UTS Name Card for Evidence Artefacts**

* **Trigger.** A new **EvidenceGraph node** is minted (an **A.10 anchor/carrier** classifying evidence for a claim).
* **Obligation.** Mint a **UTS Name Card** with **twin labels** for the artefact (Tech/Plain), citing the **home `U.BoundedContext`** (per D.CTX) and edition; do **not** borrow a Context‑local Tech label as a “global” name. 
* **Publishes/Consumes.** **Publishes:** UTS row; **Consumes:** A.10 anchor metadata.
* **Invariants.** Cross‑Context sameness is **Bridge‑only**; the UTS row lists Bridges with **CL** and a short **loss note**.

#### **H2 — UTS PathCard (PathId/PathSliceId)**

**Trigger.** A new **PathId** (or **PathSliceId**) is minted for a claim.  
**Obligation.** Publish a **UTS Name Card** with twin labels for the Path (or PathSlice), listing **Context, ReferencePlane, Γ_time**, and cited **Bridge ids + CL/CL^plane** (with loss notes). **If present, include** `U.DescriptorMapRef.edition` **and** `DistanceDefRef.edition` **ids.**  
* **Invariants.** **F/G invariants never mutate** due to CL penalties; penalties reduce **R only**. **Illumination/QD signals do not alter dominance unless a selection policy (C.19) explicitly declares it; such policy ids MUST be cited.**

#### **H3 — RSCR Trigger on Evidence‑Impacting Edit (with Bridge Sentinels)**

* **Trigger.** Any edit in G.6 that can change **gauges, acceptance verdicts, Γ‑fold contributors, or `R_eff`**; examples: freshness/decay change; Bridge **CL/CL^k** or loss update; **Φ/Ψ** policy change; lane tag correction; ReferencePlane correction; **QD/OEE artefact updates** (`U.DescriptorMapRef.edition`/`DistanceDef`, `EmitterPolicyRef`, `InsertionPolicyRef`, archive K‑capacity).
* **Obligation.** Emit a **typed RSCR trigger**; the corresponding regression test must verify: (i) legality of CHR ops in affected flows, (ii) unit/scale checks, (iii) **CL→`R_eff` routing only**, (iv) presence of Φ policy‑ids in the SCR. 
* **Publishes/Consumes.** **Publishes:** RSCR test id(s); **Consumes:** CAL.EvidenceProfiles, CAL.Acceptance, Φ‑policies.
* **Invariants.** **F/G invariants never mutate** due to CL penalties; penalties reduce **R only**.

#### **H4 — SoS‑LOG Path Citation (Selector Explainability)**

* **Trigger.** A **C.23 SoS‑LOG** rule returns {**Admit | Degrade(mode) | Abstain**} for a `(TaskSignature, MethodFamily)` pair.
* **Bridge Sentinels.** All **Bridge ids** referenced by live **PathIds/PathSliceIds** are **watch‑listed**; any change to **CL/CL^plane** or **Φ policy id** triggers **path‑local RSCR** on the affected set of Paths/Slices only.
* **Obligation.** The LOG branch **MUST** cite **EvidenceGraph `PathId`(s)** that justify the decision, together with **lane tags (TA/VA/LA)**, freshness windows, **Bridge ids + loss notes** (if any), and Φ policy‑ids. **When the decision relies on QD/illumination or portfolio telemetry, the citation MUST include** `U.DescriptorMapRef.edition`, the relevant `EmitterPolicyRef`/`InsertionPolicyRef` **ids, and the** **lens id** *(per C.19)* **if a lens was used.**
* **Publishes/Consumes.** **Publishes:** SCR‑visible branch record with `PathId`; **Consumes:** EvidenceGraph API path query.
* **Invariants.** **No self‑evidence**; cross‑plane penalties **MUST** be monotone, bounded, and table‑backed.

#### **H5 — Maturity Rung Transition Justification**

* **Trigger.** A `MethodFamily.MaturityCard@Context` rung change is proposed.
* **Obligation.** The transition **MUST** be justified by one or more **EvidenceGraph paths** and then **published on UTS**; **missing anchors ⇒ no advance**.
* **Publishes/Consumes.** **Publishes:** updated UTS entry for the MaturityCard; **Consumes:** EvidenceGraph paths and A.10 anchors.
* **Invariants.** Maturity is an **ordinal poset**, not a global scalar; any gating thresholds live **only** in **AcceptanceClauses** and are cited by id from LOG (no thresholds inside LOG). 

#### **H6 — Bridge/CL Edge Annotation (Gate‑Crossings)**

* **Trigger.** An EvidenceGraph edge **crosses tiers or Contexts/planes** (ATS GateCrossing).
* **Obligation.** Record a **`BridgeCard`** and publish a **UTS row** with: SourceTier→TargetTier, Context ids (D.CTX), **Bridge id**, **bridgeChannel**, **CL** (and **CL^k** if KindBridge), **ReferencePlane**(s), and **CL^plane** (if planes differ). **No implicit crossings**.
* **Publishes/Consumes.** **Publishes:** UTS crossing row; **Consumes:** GateCrossing metadata.
* **Invariants.** CL/CL^plane penalties **route to R only**; lanes are **explicit**.

#### **H7 — ReferencePlane Penalty Publication**

* **Trigger.** A claim/evidence path spans different **ReferencePlanes** `{world|concept|episteme}`.
* **Obligation.** Compute and publish **Φ\_plane** (policy id + loss note) alongside **Φ(CL)**; both policies are **monotone, bounded, table‑backed**; report in SCR for any affected verdict. **Publish ids, not tables; values live in CAL.Acceptance/Φ‑policy registries.** 
* **Publishes/Consumes.** **Publishes:** SCR fields with Φ policy‑ids; **Consumes:** CAL.EvidenceProfiles row(s).
* **Invariants.** Penalties affect **`R_eff`** only; **F/G** remain invariant.

#### **H8 — ATS Harness Exposure (AH‑1..AH‑4)**

* **Trigger.** G.6 exports are bundled for release or consumed by selectors.
* **Obligation.** Provide inputs so that **AH‑1..AH‑4** (TierClassifier, GateCheck, LaneCheck, LexicalCheck) can run against **EvidenceGraph paths and crossings**; FAIL if any cross‑tier/Context reference lacks **UTS+Bridge** or if lane purity is violated. **Expose policy‑ids (Φ(CL), Φ\_plane) and Γ‑fold overrides so harness checks can verify monotonicity/bounds.**
* **Publishes/Consumes.** **Publishes:** harness‑readable identifiers (no formats mandated); **Consumes:** GateCrossing + lane tags.
* **Invariants.** LEX hygiene (head‑anchoring, I/D/S) holds for all exported tokens.

#### **H9 — SCR Surface for Assurance**

* **Trigger.** Selector reports or acceptance checks reference evidence.
* **Obligation.** Expose **lane‑split**, freshness windows, **Γ‑fold** contributors, **Φ(CL/plane)** policy‑ids, **IndependenceCertificate ids** (if SpanUnion), and (where present) **ProofLedger** references **as SCR‑visible fields**. 
* **Publishes/Consumes.** **Publishes:** SCR views; **Consumes:** CAL.Acceptance, CAL.ProofLedger, EvidenceGraph paths.
* **Invariants.** **WLNK default = weakest‑link** unless proved otherwise; any override cites monotonicity/boundary proofs.

#### **H10 — ProofLedger Linkage (CAL ↔ G.6)**

* **Trigger.** A formal proof obligation or evidence role is attached to a claim.
* **Obligation.** Link the EvidenceGraph node/edge to **CAL.ProofLedger** entries and **A.10 carriers** via `verifiedBy/validatedBy` relations; **SCR/RSCR anchors are mandatory** for all carriers. **No self‑evidence**. 
* **Publishes/Consumes.** **Publishes:** ProofRef ids in the path; **Consumes:** CAL.ProofLedger entries.
* **Invariants.** **TA/VA/LA** distinctions remain explicit; tool qualification belongs to **TA**.

#### **H11 — Telemetry Ingest (Selector & Probe Outcomes)**

* **Trigger.** Run‑time **selector** or **probe** outcomes (E/E‑LOG) return observations that bear on previously asserted claims; **this includes QD/illumination updates and OEE `GeneratorFamily` events** (environment edits/transfers).
* **Obligation.** Ingest as **external evidence lines** into the EvidenceGraph with proper **lane typing** (LA/VA/TA), **Context slice** and **Γ\_time**; record **edition‑aware fields** when applicable: `U.DescriptorMapRef.edition`, `DistanceDef`, `ArchiveCellRef`, `EmitterPolicyRef`, `InsertionPolicyRef`, the **policy‑id**, and the **lens id** *(per C.19)* used by the selector. For OEE events, capture `EnvironmentValidityRegion` and `TransferRules` references. Opening/closing of refresh windows produces **DRR/RSCR hooks** outside the Core text. *This hook wires G.6 to G.11 Telemetry/Refresh while keeping Core prose tool‑agnostic as required by E.5.*
* **Publishes/Consumes.** **Publishes:** new EvidenceGraph nodes/edges + UTS rows; **Consumes:** selector/probe attestation (as conceptual carriers) **and (when present) GeneratorFamily attestations**.
* **Invariants.** Separate **ΔR / ΔF** from **ΔG** in rationale (Assurance calculus discipline). **Illumination increments are logged as editioned deltas; they do not change dominance unless declared by policy (C.19).**

#### Minimal conformance (hooks)

1. **UTS publication (H1)** for every minted evidence artefact; Bridges carry **CL + loss note**.
2. **RSCR triggers (H3)** on any edit impacting gauges/acceptance/Γ‑fold or Φ penalties.
3. **LOG path citation (H4)** is mandatory for **all** Admit/Degrade/Abstain decisions; **no self‑evidence**. 
4. **Maturity rung transitions (H5)** **forbid** advancement without EvidenceGraph paths and UTS publication.
5. **Gate‑crossings (H6/H7)** publish **Bridge + CL/CL^plane** and route penalties to **R only**; **no implicit crossings**.
6. **ATS harness (H8)** passes **AH‑1..AH‑4** on crossings and lane purity.
7. **SCR surface (H9)** exposes lane split, Γ‑fold, Φ‑policies, ProofRefs; default **WLNK** unless proved otherwise.
8. **ProofLedger linkage (H10)** ties formal/empirical roles to **A.10 carriers**; **SCR/RSCR anchors** present.


### 9) Consequences

**Benefits.** Path‑addressable provenance; transparent **CL** and decay; clean **DesignRunTag**; selectors and auditors share the *same* object; **R** penalties become explainable deltas rather than folklore.
**Trade‑offs.** Authors must declare freshness and planes; mitigated by reusing G.4 **EvidenceProfiles** instead of duplicating fields.

### 10) Rationale

G.6 concretises the “**because‑graph**” already implicit in A.10 as a **typed, lane‑aware DAG** with **stable path addresses**. It relies on B.3’s **assurance skeleton**—WLNK for R, penalties by **Φ(CL\_min)**, **SpanUnion constrained by support** for G, and **F = min**—rather than inventing a new calculus. The **SCR/RSCR** obligations keep the graph grounded in carriers and external Transformers, matching post‑2015 provenance practice for reproducible knowledge and auditability.

### 11) Relations
**Builds on:** A.10 (anchors, SCR/RSCR, externality), B.3 (assurance lanes & Γ‑fold skeleton), G.4 (EvidenceProfiles & ProofLedger), F.9 (Bridges/CL), **C.18 (NQD‑CAL)**, **C.19 (E/E‑LOG & policies)**, **E.11 (ATS)**, E.8/E.10 (template & lexical rules).
**Publishes to:** **UTS** (Name Cards for evidence artefacts and PathIds) and **RSCR**; **G.5** selectors cite **PathId** in their **SoS‑LOG** branches (admit/degrade/abstain); **G.11** consumes editioned telemetry for refresh/decay.
**Constrains:** **G.5** (eligibility/selector must point to PathIds; **portfolio results MUST cite policy‑ids and, when QD present, DescriptorMap editions**), **G.9** (parity checks cite concrete paths), **G.11** (telemetry drives Path refresh & deprecation via evidence windows and edition changes).
