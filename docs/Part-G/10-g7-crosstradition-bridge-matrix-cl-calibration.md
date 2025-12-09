## G.7 — **Cross‑Tradition Bridge Matrix & CL Calibration** \[A]

**Tag:** \[A] **Stage:** design‑time
**Hooks:** **G.2** (SoTA Bridge Matrix), **F.9** (Bridges/CL & CL^k/Ψ), **G.5** (eligibility & selection across bridges), **C.23** (SoS‑LOG rules), **G.4** (CAL/Acceptance routes), **C.18/C.19** (NQD/QD spaces & governor), **G.6 hooks H1, H3–H7, H9–H10** (UTS, RSCR, LOG path citation, gate‑crossings, SCR/ProofLedger), **E.11 (ATS: AH‑1..AH‑4)**
**Publishes to:** **UTS**; registers **Bridge Sentinels** for **G.11** refresh; emits **Telemetry(PathSlice)** with policy‑ids and **edition markers** (`DescriptorMapRef.edition`, `DistanceDefRef.edition`, and — when QD archives are implicated — `InsertionPolicyRef`) where relevant.

### 1 · Intent

Turn the **SoTA Bridge Matrix** produced in **G.2** into **formal Bridges** with **Congruence Levels (CL)**, **loss notes**, and **ReferencePlane** penalties where applicable; calibrate **CL/CL^k** and (where relevant) **CL^plane** using a small, auditable procedure; maintain a **Bridge Calibration Table (BCT)** with **sentinel‑sets** and **regression tests** to guard stability of CL/CL^k/CL^plane over time; register sentinels so any change to CL or Φ‑policies triggers **path‑local** RSCR re‑checks rather than whole‑pack reruns. Cross‑Tradition reuse **without** a Bridge is **forbidden**.  

### 2 · Problem Frame

**G.2** exports a **Bridge Matrix** (Tradition×Tradition) alongside Claim Sheets and Operator/Object inventories. Those rows already carry preliminary CL and loss notes; **G.7** hardens them into **F.9 Bridges** that can be consumed by **G.3/G.4/G.5** and surfaced on **UTS**. Maintain a **BCT** per Tradition‑pair with freshness windows and regression assets. +**AlignmentDensity** (C.21 DHC) counts only **CL ≥ 2** bridges; interpret **CL = 3** as *free substitution* and **CL = 2** as *guarded* (loss attached), with declared units for the series.  (counts & units per C.21/DHC)

### 3 · Problem

1. **Rival Traditions** must be compared **without** semantic flattening; 2) cross‑plane talk (world|concept|episteme) introduces **CL^plane** penalties; 3) penalty routing must stay **assurance‑only (R)**, leaving **F/G** invariant; 4) changes to Bridges need **targeted** refresh, not a full re‑weave of evidence; 5) when Bridges touch **DescriptorMap** used by illumination/QD, their **DescriptorMapRef.edition** and **DistanceDefRef.edition** must be tracked to avoid silent drift.

### 4 · Forces

| Force                                | Tension                                                                                              |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| **Comparability vs Local Authority** | Compare Traditions but never override Context‑local meaning; reuse is **Bridge‑only**.               |
| **Didactic Simplicity vs Fidelity**  | Managers need compact tables, yet **Row CL(min)** and explicit losses bound where sameness is safe.  |
| **Auditability vs Throughput**       | Calibration must be light‑weight but **UTS‑visible** and **AH‑1..AH‑4** runnable.                    |
| **Refresh Cost vs Safety**           | Move from pack‑wide reruns to **path‑local** triggers on **Bridge** edits.                           |
| **QD comparability vs Metric drift** | QD/illumination comparisons require **stable DescriptorMap and Degree‑of‑difference (DistanceDef)** definitions.     |

### 5 · Solution — **From Matrix to Bridges, with CL/CL^k Calibration, BCT & Sentinels**

**S0 · Prepare a Bridge Calibration Table (BCT) & Regression Set.**
Per Tradition‑pair, materialize a **BCT** capturing: `TradPairId`, `ComparableConstruct`, `FreshnessWindow`, `SentinelSetId`, `RegressionSetId`, and **declared units** (per C.21). Include **stability checks** for CL/CL^k/CL^plane across editions; record **edition ids** for `DescriptorMapRef.edition` and **DistanceDefRef.edition** (C.18) and — when applicable — `InsertionPolicyRef` to ensure edition‑aware auditing.

**S1 · Forge Bridges from Matrix rows.**
For each comparable construct in the G.2 Bridge Matrix, mint an F.9 BridgeCard **anchored at SenseCell granularity** (F.3/F.7); **never whole Contexts**. If tokens other than SenseCells are used, **declare their SenseCell anchors**. State `bridgeChannel ∈ {Scope, Kind}`, `kind` (≡/⊑/⋈/≈/… as supported), `CL ∈ {3,2,1,0}` with loss notes (Scope) and, where a KindBridge is used, `CL^k ∈ {3,2,1,0}` with loss notes. Record direction if non‑symmetric and the validity region. **CL ≥ 2** (and **CL^k ≥ 2**) is permitted; **= 1** requires a **Waiver**; **= 0** is forbidden. Publish a **UTS row** for every GateCrossing. **No implicit crossings.**

**S2 · Calibrate CL with a minimal, auditable procedure.**
Per Bridge:

1. Plane check. Record `ReferencePlane`(source,target). If planes differ, compute **CL^plane** and attach **Φ_plane** (policy‑id + loss note). **Plane penalties SHALL NOT mutate `CL`**; they **only reduce `R_eff` via Φ_plane**. Crossing **≥ 2 planes MAY be policy‑blocked** (Φ_plane = block) unless a documented Waiver is cited. **F/G remain invariant.**
2. **Counter‑example duty.** Assign **CL/CL^k** only if you can state at least one **counter‑example** for ≤ 2, or explain its absence for 3 (**honesty rule**).
3. Penalty policies. Reference **Φ(CL)** (Scope) and, where applicable, **Ψ(CL^k)** (Kind), and **Φ_plane** — all **monotone, bounded, table‑backed** — used by your CG‑Frame. **Route penalties to `R_eff` only; F/G invariant.**
4. Row scope (by reference). For Concept‑Set rows supported by Bridges, apply **F.7** row rules: **Row CL(min) = bottleneck** (no averages) and include a counter‑example when any cell carries a loss note. (Do not restate them here.)
5. Stability check. Run the **BCT Regression Set**; if CL/CL^k/CL^plane changes, attach the regression delta, update **SentinelSet**, and emit **Telemetry(PathSlice)** with `policy‑id`(s) and any affected **DescriptorMapRef.edition** or **DistanceDefRef.edition**.

**S3 · Publish crossings to UTS & Evidence surfaces.**
Every GateCrossing emits a UTS row listing `SourceTier→TargetTier`, `Context ids`, `Bridge id`, `bridgeChannel`, `CL` (and `CL^k` if KindBridge), `ReferencePlane(s)`, and `CL^plane` (if planes differ). **SCR shows the policy‑ids for Φ(CL), Ψ(CL^k) (if used), and Φ_plane** and cites the **BCT id** and **RegressionSet id**. (No implicit crossings.)

**S4 · Register Bridge Sentinels (watch‑list).**
All **Bridge ids** referenced by live **EvidenceGraph `PathId`/`PathSliceId`** are **watch‑listed**. On any change in **CL/CL^k/CL^plane** or **Φ/Ψ policy‑id**, emit **path‑local RSCR** triggers (per **H3/H4**) and schedule refresh **per PathSlice** (Γ_time × plane), not per pack. Where Bridges reference **DescriptorMapRef** or **DistanceDef**, any **edition change** also triggers sentinels and publishes an edition note to Telemetry.

**S5 · Dispatcher & DHC hooks.**
G.5 may only compare across Traditions when a Bridge exists; selection uses admissible orders, **bans cross‑ordinal scalarisation**, and applies **CL/CL^k/CL^plane penalties to R only**. **SoS‑LOG (C.23) gates** accompany any cross‑Tradition choice; **Acceptance (G.4)** holds thresholds/unknowns. For illumination/QD comparisons, G.5 must cite the **DescriptorMapRef.edition** and the **DistanceDefRef.edition** exposed by **G.7**. G.12 reports AlignmentDensity using Bridges with **CL ≥ 2** (units declared).

### 6 · Structure (conceptual surfaces)

**BridgeCard (core fields).**
`⟨BridgeId, Source⟨Context, SenseCell⟩, Target⟨Context, SenseCell⟩, bridgeChannel∈{Scope, Kind}, kind, CL, CL^k?, lossNotes, validityRegion, ReferencePlane(src,tgt), CL^plane?, Φ(CL) policy‑id, Ψ(CL^k) policy‑id?, Φ_plane policy‑id?, DescriptorMapRef?, DescriptorMapRef.edition?, DistanceDefRef?, DistanceDefRef.edition?, InsertionPolicyRef?, Evidence lanes, UTS.rowId, BCT.id, RegressionSet.id, SenseCellAnchorRefs?⟩`
(“SenseCell‑only; never Contexts.”)

**Calibration Ledger (per Tradition pair).**
`⟨TradPairId, ComparableConstruct, Bridges[], RowScope, RowCL(min), Counter‑example link, Freshness window, SentinelSet.id, RegressionSet.id, DescriptorMapRef?, DescriptorMapRef.edition?, DistanceDefRef?, DistanceDefRef.edition?, InsertionPolicyRef?, Steward⟩`
(Attach to **SoTA Synthesis Pack** and cite from **G.5**.)

This is pure conceptual, notation-independent.

### 7 · Interfaces & Dependencies

* **Consumes:** G.2 Bridge Matrix; E.10 LEX/I‑D‑S; E.11 ATS crossings; B.3 Φ‑policies; C.21 metrics schema; **C.18/C.19** QD descriptors & policies (when relevant); **C.23** SoS‑LOG clauses; **G.4** Acceptance thresholds.    
* **Produces:** F.9‑conformant **BridgeCards**; **UTS** crossing rows; **PathSlice** sentinel registrations; CL policy ids for **SCR**; DHC‑visible bridge counts; **Telemetry(PathSlice)** entries with policy‑ids and, where applicable, **DescriptorMapRef.edition** and **DistanceDefRef.edition** and **InsertionPolicyRef**.

### 8 · Conformance Checklist (normative)

1. **Bridge‑only reuse.** Any Cross‑Tradition or Cross‑Context reuse **MUST** cite a **Bridge** with **CL** (and **CL^k** if KindBridge) and **loss notes**; **mentions without Bridge+UTS row are non‑conformant**.
2. **CL regimes.** **CL, CL^k ∈ {3,2,1,0}**; **≥ 2** permitted; **= 1** only with **Waiver**; **= 0** forbidden. **Honesty rule** holds (counter‑example for ≤ 2 or stated absence for 3).
3. Plane guard. On plane mismatch, compute **CL^plane** and publish **Φ_plane** policy‑id. **Plane penalties SHALL NOT change `CL`; penalties reduce `R_eff` only.** Blocking is a **Φ_plane** policy outcome (not a CL edit).
4. R‑only routing. **Φ(CL)**/**Ψ(CL^k)**/**Φ_plane** are **monotone, bounded, table‑backed**; **penalties reduce `R_eff` only**; **F/G invariant**.
5. Row bottleneck (by reference). Apply **F.7** row rules: **Row CL(min)=bottleneck** (no averages) and include a counter‑example when any cell has a loss note.
6. **UTS publication.** Each GateCrossing publishes a **UTS row** with **ReferencePlane**(s) and **CL^plane** (if any); cites **BCT.id/RegressionSet.id**; **no implicit crossings**.
7. **ATS harness.** **AH‑1..AH‑4** pass on published crossings and lanes; **fail** on missing Bridge/UTS or lane impurity.
8. **Sentinel wiring.** Bridges cited by live **PathId/PathSliceId** are **watch‑listed**; edits to **CL/CL^k/CL^plane** or **Φ/Ψ** trigger **path‑local RSCR** per **H3/H4**; **DescriptorMapRef.edition / DistanceDefRef.edition changes** trigger the same.
9. **ReferencePlane on transfer.** Any **inter‑Context** or **inter‑plane** transfer **MUST** explicitly declare `ReferencePlane(src,tgt)` and publish **Φ_plane** (if planes differ); absence is **fail‑fast**.
10. **DHC accounts.** **AlignmentDensity** counts only **CL ≥ 2**; **CL=3** is free substitution, **CL=2** guarded (loss published).
11. SenseCell anchoring. BridgeCards **MUST** anchor to **SenseCells**; if other tokens are used, **declare SenseCell anchors**.
12. **BCT presence.** A **BCT** with **freshness window**, **SentinelSet**, and **RegressionSet** MUST exist for any Tradition‑pair with Bridges; **stability checks** must be runnable via AH‑harness.

### 9 · Micro‑examples (post‑2015 contexts; *indicative only*)

> **Scope note.** Examples illustrate **row scopes** and **loss notes**. They are not endorsements of equivalence beyond the stated scope. Penalties route to **R** only; **F/G** invariant.

1. “Preference‑learning objective” *(senseFamily=Method; **Row Scope: Naming‑only**)* ...
   *Cells:* `RLHF@Context‑A:policy‑gradient‑on‑reward‑model` ↔ `DPO@Context‑B:direct‑preference‑optimization` • *Row CL(min):* 2 • *Loss:* KL‑regularisation vs. implicit logistic form; sensitivity to label‑noise mix • *Use:* didactic (naming/expository); **no** substitution of acceptance thresholds. *(2017→2023 literature evolution; rival training programs with overlapping intent.)*

2. “Causal effect (ATE) reading” *(senseFamily=Method; **Row Scope: Naming‑only**)* …
   *Cells:* `SCM@Context‑C:do(x)` ↔ `Potential‑Outcomes@Context‑D:ATE` • *Row CL(min):* 2 • *Loss:* identifiability conditions differ (ignorability/positivity vs. graph‑based rules); estimator families diverge • *Use:* expository mapping in Claim Sheets; **no** estimator substitution across pipelines.

3. “Stiffness indicator for ODE suites” *(senseFamily=Measurement; **Row Scope: MM‑CHR metric (measurement comparandum)**)* …
   *Cells:* `Rosenbrock:stability‑region test` ↔ `IMEX:stiff‑ratio heuristic` • *Row CL(min):* 2 • *Loss:* test regimes differ; grid dependence; asymptotic constants • *Use:* **G.5** eligibility hints; acceptance thresholds live in **G.4**, not here.

4. “Illumination descriptor mapping” *(senseFamily=Measurement; **Row Scope: QD comparability (DescriptorMap-only)**)* …
  *Cells:* `MAP‑Elites:grid indices` ↔ `CVT‑MAP‑Elites:Voronoi centroids` • *Row CL(min):* 2 • *Loss:* binning vs. centroidal tessellation; drift when **DistanceDef** or centroid‑counts change • *Use:* lawful cross‑reporting of Q/D/QD‑scores; **DescriptorMapRef.edition** and **DistanceDefRef.edition** must be cited; thresholds remain in **G.4**.

*(All four rows presume extant F.9 Bridges; row bottlenecks and losses are printed as per F.7.)*

### 10 · Anti‑patterns & Remedies

* **Semantic flattening.** Treating rival definitions as synonyms without Bridges. → **Bridge first;** print **loss**; keep **Row Scope** tight.
* **CL averaging.** Computing Row CL as an average. → **Bottleneck min**; never averages.
* **SenseFamily jump.** Using an interpretation bridge to license substitution. → **Substitution requires senseFamily‑preserving bridges**.
* **Plane blindness.** Ignoring **CL^plane** when crossing world↔concept↔episteme. → Compute **CL^plane** and publish **Φ_plane id**.
* **Pack‑wide reruns.** Reweaving all evidence on a minor Bridge edit. → **Sentinels + PathSlice** for targeted RSCR. 
* **QD metric drift.** Comparing illumination/QD outcomes after **DescriptorMap** or **DistanceDef** changes without editioning. → **Record editions in BridgeCard/BCT**; publish to Telemetry; re‑run BCT regression checks.

### 11 · Consequences

* **Auditable plurality.** Teams can hold multiple Traditions in view and compare them **safely**; losses are visible; penalties touch **R** only.
* **Selective & edition‑aware refresh.** Bridge edits or **DescriptorMapRef.edition / DistanceDefRef.edition** changes trigger **path‑local** refresh (lower cost, higher reactivity).
* **Downstream cleanliness.** **G.5** selectors have lawful crossings and **Φ** ids; **G.12** can compute DHC signals with declared units and windows; illumination/QD comparisons carry **edition** context, preventing silent drift.

### 12 · Relations

**Builds on:** **G.2** (Matrix), **F.9** (Bridges/CL), **B.3** (Φ penalties), **E.10** (LEX), **E.11** (ATS), **C.18/C.19** (QD descriptors & governor), **C.23** (SoS‑LOG). **Prerequisite for:** **G.5** eligibility across bridges and edition‑aware QD parity; **G.11** responds to **Bridge Sentinels**.   
