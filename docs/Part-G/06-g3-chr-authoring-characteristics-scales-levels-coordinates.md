## G.3 — **CHR Authoring: Characteristics · Scales · Levels · Coordinates** \[A]

**Tag:** \[A] (publishes CHR; constrains CAL/LOG)
**Stage:** *design‑time* (authoring & publication; enables lawful run‑time use by G.4/G.5)
**Primary hooks:** G.1 CG‑Frame Card; G.2 SoTA Pack; **MM‑CHR discipline** (A.17–A.19/C.16); **Trust & Assurance** (B.3, Γ‑fold B.1); **Contexts & Bridges with CL** (F.1–F.3, F.9); **UTS & Naming** (F.17–F.18); **RoleAssignment** (F.4); **RSCR** (F.15); **No tool lock‑in** (E.5.1–E.5.3); **Lexical rules** (E.10); **Design–Run split** (A.4);
**Illumination/QD & Dispatch** (C.18 NQD‑CAL, C.19 E/E‑LOG, G.5 registry/selector).
**Pre‑flight (applies to G.0–G.5).** Any numeric comparison/aggregation **MUST** (i) cite a **CG‑Spec.characteristic id**, and (ii) prove **CSLC legality** (A.18/C.16: **Scale/Unit/Polarity**) **before numbers move**; minimal evidence recorded via CG‑Spec. Cross‑Context reuse requires **Bridge + CL** with penalties routed to **R_eff only** (never **F/G**). **Φ(CL)**/**Φ_plane** **MUST** be monotone and table‑backed (policy‑ids recorded). **ReferencePlane** **MUST** be surfaced for any definitional claim. **Freshness windows** are normative per Characteristic and enforced at **G.4 CAL.Acceptance** via `FRESHNESS_CHECK(·)`. Unknowns propagate as a tri‑state {**admit**|**degrade**|**abstain**} into **Acceptance**.

### 1) Intent

Provide a **notation‑independent authoring discipline** to turn SoTA plurality into a **lawful characterization layer (CHR)**: precisely typed **Characteristics**, **Scales**, **Levels**, and **Coordinates** with **guard‑rails** on what operations and aggregations are **legal**. The output is a **CHR Pack** consumable by CAL authoring (G.4) and dispatch (G.5), and publishable to **UTS**. CHR prioritizes **method‑centric generation** (increases the probability of producing acceptable results) over ex‑post governance; **thresholds live only in G.4**.

### 2) Problem frame

You have a **CG-FrameContext** (G.1) and a **SoTA Synthesis Pack** (G.2) with competing Traditions, object/operator inventories, twin‑labeled UTS drafts and Bridge/CL(+CL^plane) notes. Before any calculus (G.4) or run‑time dispatch (G.5), you must **stabilize measurement semantics**: name things, type them, and make illegal operations **impossible by construction**.

### 3) Problem

Teams repeatedly stumble on:

* **Meaning leaks** across Contexts (same word, different sense).
* **Illicit arithmetic** (e.g., averaging ordinals, mixing units).
* **Hidden normalizations** that silently change polarity or scale.
* **Unverifiable aggregation** (no proof obligations, no Γ‑fold hooks).
* **Unreusable outputs** (no UTS rows, no test surface, no scope).

### 4) Forces

* **Pluralism vs. uniformity.** Preserve Tradition‑specific semantics yet deliver a common **typing** substrate.
* **Expressiveness vs. parsimony.** Reuse existing U.Types (F.8) vs. mint new ones with justification.
* **Pedagogy vs. formalism.** Make authoring teachable (Name Cards, micro‑examples) without weakening the legality guards.
* **Local context vs. portability.** Keep CHR **Context‑local** while preparing **Bridges** with **CL** and explicit **loss notes**.

### 5) Solution — *CHR Authoring chassis* (S1–S8)

**S1 · Measurement Charter (scope anchor)**
**Inputs:** CG-FrameContext (G.1), SoTA Pack (G.2). CAL traces supporting SoTAPaletteDescription MUST identify KD‑CAL lanes used (TA / VA / LA) and expose any lane‑dependent tolerances. **Cross‑lane comparisons are forbidden**; lane purity is enforced in **CAL.EvidenceProfiles**. If a claim crosses **ReferencePlanes**, declare **Φ_plane** and route penalties to **R_eff only**; there is **no “Bridge” across lanes**.

**Ops:** declare **ObjectKinds** and **TaskKinds** in the home **Context**; state **USM ScopeSlice(G)**, invariants, **ReferencePlane**, and **freshness** needs; list contested terms that require Bridges.
**Outputs:** `KindMap@Context`, `MeasurementCharter` (design‑time stance).
**Guards:** A.4 split; F.1–F.3 Contexting; E.10 lexical hygiene; **E.11 ATS GateCrossing** recorded for any tier crossing (AT0..AT3) with **Bridge id**, **PathSliceId**, and **CL** captured (penalties → **R_eff** only).

**S2 · Term Minting & Reuse (UTS‑first)**
**Ops:** for each candidate term, attempt **reuse** (F.8) via UTS; if minting, draft **Name Card** (Unified + Plain), Context, MDS, twin labels, and **loss notes** for any Bridge.
**Outputs:** `UTS.Drafts{Characteristic,Scale,Level,Coordinate}` with ids.
**Guards:** No global claims; Bridges carry **CL** (F.9).

**S3 · Characteristic Cards (the core unit)**
**Template (normative fields):**
`CharacteristicCard := ⟨UTS.id, Context, ReferencePlane, ObjectKind, Intent, Definition (typed), **ObservableOf ⟨instrument/protocol, uncertainty model, validity window⟩**, EvidenceLanes (KD‑CAL), ScaleRef, Polarity ∈ {↑, ↓, ⊥}, Domain/Range, UnitSet, Freshness/Half‑life, Missingness semantics, Reliability/Stability notes, **QD.Role ∈ {Q, D, QD‑score, none}, DescriptorMapRef (Tech; d≥2, optional), DistanceDefRef (if QD.Role=D), DHCMethodRef.edition (if Q/QD‑score)**, Micro‑examples⟩`
**Rules:** Definition references **MM‑CHR**; **Polarity** explicit; **UnitSet** coherent; **Missingness** classified (MCAR / MAR / MNAR, or local equivalents with mapping).
**Outputs:** `CHR.Characteristic[]` (if used in any **CG‑Spec**, the **CG‑Spec.characteristics\[] id** MUST be referenced here).  If a Characteristic plays a role in **Illumination/QD**, publish **QD.Role** and the corresponding **DHCMethodRef.edition/DistanceDefRef** for reproducibility of fronts (visible to G.5/C.18).

**S4 · Scales & Levels (lawful measurement)**
**ScaleCard:** `⟨type ∈ {nominal, ordinal, interval, ratio, count, cyclic,…}, admissibleTransforms (group), unit(s), resolution, bounds, zero semantics⟩`.
**LevelCard (for nominal/ordinal):** `⟨enumeration, partial/total order, ties policy⟩`.
**Rules:**

* **Nominal:** only equality, counting by category; transforms = permutations.
* **Ordinal:** order‑preserving transforms only; **no** addition/subtraction; medians allowed; quantiles allowed.
* **Boolean:** treated as **nominal with two levels**; only equality and counts; transforms = permutations.
* **Count:** non‑negative integers; addition allowed; **do not** assume ratio‑scale unless exposure/time base is fixed and declared; declare rate conversions explicitly.
* **Interval:** positive affine transforms; differences meaningful; means allowed.
* **Ratio:** positive scalar transforms; ratios and products allowed.
* **Cyclic:** operations respect wrap‑around; define principal interval.
  **Outputs:** `CHR.Scale[]`, `CHR.Level[]`.

**S5 · Coordinates & Encodings (without hidden cardinalization; state preserved invariants and non‑entitlements per A.18 CSLC)**
When a numeric **Coordinate** is required (e.g., for ranking), publish `CoordinatePolicy` with: mapping, invariants preserved (order/ratio/etc.), **what operations remain illegal**, and **proof obligations** if stronger structure is claimed. **Coordinates do not authorize scalarization of partial orders**; for partial orders, consumers **MUST** return sets.
**Examples:** isotonic embeddings for ordinal (order‑only), log‑scale coordinates for ratio positives, circular coordinates for cyclic.
**Outputs:** `CHR.Coordinate[]` + legality annotations.
**Guards:** Coordinate **does not** upgrade scale type without evidence; illegal ops remain blocked.
**Note:** if a Characteristic participates in any **CG‑Spec** characteristic, reference the characteristic id in the card.

**S6 · Operation Legality & Guard Macros** (explicitly forbid mean/subtract on ordinal; fail unit mismatches)
Publish a **Legality Matrix** per Scale type and a set of **Guard Macros** for CAL/LOG:
`ORD_COMPARE_ONLY`, `INTERVAL_MEAN_ALLOWED`, `RATIO_PRODUCT_ALLOWED`, `UNIT_CHECK`, `CROSS_Context_CL_PENALTY`, `POLARITY_CHECK`, `CYCLIC_DIFF`, `FRESHNESS_CHECK`,
`CSLC_PROOF_REQUIRED(x)` — aggregation/comparison proceeds **only** after **CSLC legality** is proven for the participating Scales/Units (per A.18/C.16),
`UNKNOWN_TRI_STATE(x)` — on missingness/unknowns, emit **{admit\|degrade\|abstain}** branch for **Acceptance** (no silent coercions),
`PHI_CL_MONOTONE(policy_id)` — assert that **Φ(CL)**/**Φ_plane** used for penalties is **monotone**; record **policy_id** (visible to G.4/G.5 **SCR**).
`RETURN_NONDOMINATED_SET()` — for partial orders (e.g., Pareto), the comparator **must** return the explicit non‑dominated set; scalarization is forbidden unless CAL justifies a lawful order.
`METRIC_EDITION_REF(id)` — surface the **DHCMethodRef.edition/DistanceDefRef.edition** used for any Q/D/QD‑score‑based comparison (ties to G.5/C.18).

**Outputs:** `CHR.Guards`, `CHR.LegalityMatrix`.
**Guards:** Enforce at authoring time + RSCR; route cross‑Context penalties to **R_eff** (never to **F/G**).
**Freshness windows** MUST be published per Characteristic (Context‑local; stale ⇒ {degrade|abstain} at Acceptance) and enforced via `FRESHNESS_CHECK(x)` in **CAL.Acceptance**.

**S7 · Aggregation & Comparison Patterns (safe by construction)**
Provide **typed aggregation templates** (e.g., lexicographic min, Pareto dominance — **return the explicit non‑dominated set** for partial orders; medoid/median for ordinal; **t‑norms only on ratio‑scale quantities in [0,1]**; **for interval: means allowed; for ratio: sums/products allowed after unit alignment**). Any comparator/aggregator used **across candidates** MUST cite a **CG‑Spec** characteristic id (A.19.D1) and, if based on **Q/D/QD‑score**, its **DHCMethodRef.edition/DistanceDefRef**; otherwise degrade to order‑only or abstain. **Record the chosen Γ‑fold contributor policy (default = weakest‑link) with an edition id; silent changes are forbidden.** Scalarization of partial orders is **forbidden**; selection is delegated to **G.5** which returns **sets/archives** under lawful orders.
**Outputs:** `CHR.AggregationSpecs` with legality proofs/links.

**S8 · Publication, Tests, and Evolution**
Publish all artifacts to **UTS** (with twin labels and Bridges); register **RSCR** tests: unit coherence, guard coverage, polarity invariants, illegal‑op refusal. Provide **Worked‑Examples** and a **Refresh Plan** (ageing/decay → B.3.4). Surface **policy‑ids Φ(CL), Φ_plane**, and, where applicable, **DHCMethodRef.edition/DistanceDefRef** for Q/D/QD‑score. Record **PathId/PathSliceId** for refresh/decay telemetry.
**Outputs:** versioned `CHR Pack@CG-Frame` + RSCR ids + deprecation notices (F.13) + provenance fields (Φ‑policies, PathSlice).
**Guards:** E.5.\* no tool lock‑in; lexical continuity (F.13–F.14).

### 6) Archetypal Grounding (informative; two CHR examples from distinct fields)

**AG‑1 (ML fairness, post‑2015 practice).**  
Characteristic: `DemographicParityGap` — **interval** (symmetric bounds around 0), Unit: percentage points, Polarity: **target‑band** with center at 0.  
Legality: **no cross‑ordinal scalarisation**; comparisons use intervals; **UNIT_CHECK** and **ORD_COMPARE_ONLY** guarding when gap is disclosed alongside ordinal labels; **CSLC_PROOF_REQUIRED** before any aggregation across cohorts; stale evidence ⇒ **UNKNOWN_TRI_STATE → {degrade|abstain}**.  
Bridge: when imported from an external auditing Tradition, require **Bridge + CL**; penalties via **PHI_CL_MONOTONE** → **R_eff** only.

**AG‑2 (Clinical diagnostics).**  
Characteristic: `Sensitivity` — **ratio** (dimensionless in \[0,1]), Unit: none; Polarity: **↑**.  
Legality: means allowed on ratio; **t‑norms only on \[0,1]**; no mixing with **ordinal** labelling of test difficulty; **CSLC_PROOF_REQUIRED** on any rate→rate transformations (e.g., pooled sensitivity under varying prevalence).  
Evidence lanes: declare **TA/VA/LA** per protocol and trials; freshness window declared.

**AG‑note (Illumination/QD, post‑2015 practice).**  
When a Characteristic serves as **Diversity** or **Quality** in QD/Illumination (e.g., MAP‑Elites‑class methods), set `QD.Role` and publish **DHCMethodRef.edition/DistanceDefRef**; comparisons **return sets** under partial orders and do **not** introduce scalarisation in CHR.

### 7) Interfaces — minimal I/O Standard

| Interface                | Consumes                            | Produces                                                              |
| ------------------------ | ----------------------------------- | --------------------------------------------------------------------- |
| **G.3‑1 Charter**        | CG-FrameContext (G.1), SoTA Pack (G.2) | `KindMap@Context`, `MeasurementCharter`                                  |
| **G.3‑2 MintOrReuse**    | SoTA terms, UTS registry            | `Characteristic/Scale/Level/Coordinate` Name Cards (UTS ids)          |
| **G.3‑3 DefineScale**    | CharacteristicCard                  | `ScaleCard`, `LevelCard`                                              |
| **G.3‑4 Coordinate**     | ScaleCard, use‑cases                | `CoordinatePolicy` + legality annotations                             |
| **G.3‑5 Guards**         | Scale/Level/Coordinate specs        | `LegalityMatrix`, `GuardMacros` (for CAL/LOG)                         |
| **G.3‑6 AggregateSpecs** | CHR set, acceptance clauses         | `AggregationSpecs` (typed, with proofs/obligations; **DHCMethodRef.edition/DistanceDefRef.edition** if Q/D/QD‑score) |
| **G.3‑7 Publish**        | All above                           | Versioned `CHR Pack@CG-Frame`, RSCR tests, Worked‑Examples, deprecations, Φ‑policies, PathSlice |

### 8) Payload (what G.3 exports)

1. **CHR Pack\@CG-Frame** (folder):

   * `CHR.Characteristic[]` (Cards)
   * `CHR.Scale[]`, `CHR.Level[]`
  * `CHR.Coordinate[]` (with legality notes)
   * `CHR.Guards`, `CHR.LegalityMatrix`
   * `CHR.AggregationSpecs` (**Γ‑fold contributor policy + edition id**, **DHCMethodRef.edition/DistanceDefRef.edition** if applicable; visible to G.4/G.5 **SCR**)
   * **UTS Entries** (Name Cards + twin labels + Bridge CL & loss notes)
   * **RSCR** tests + **Worked‑Examples** (**Archetypal Grounding included**)
   * **Provenance fields**: **ReferencePlane**, **Φ(CL)**/**Φ_plane** policy‑ids, **PathId/PathSliceId**

1. **Hand‑off manifests** to G.4 (admissible CAL operators; unit/scale constraints; freshness routing) and to G.5 (TaskSignature trait inferences; eligibility predicates; QD roles/editions for lawful archives).

### 9) Conformance Checklist (normative)

1. **Context declared.** Every CHR artifact has a **home Context**; cross‑Context reuse uses a **Bridge** with **CL** and **loss note**.
2. **Scale typed.** Each Characteristic declares **Scale type**, **Polarity**, **UnitSet**, **Bounds**, **Zero semantics**, **Freshness**.
3. **ReferencePlane surfaced.** Any definitional claim carries an explicit **ReferencePlane**.
4. **ObservableOf filled.** Each CharacteristicCard declares `ObservableOf` with instrument/protocol and uncertainty.
5. **CG‑Spec link.** If a Characteristic is used as a **CG‑Spec** characteristic, the characteristic id is referenced.
6. **Legality explicit.** A **Legality Matrix** and **Guard Macros** exist and are referenced by all downstream operators.
7. **No scalarization of partial orders.** Partial orders **MUST** return sets (archives) at selection time; scalarization is forbidden in CHR.
8. **No illegal ops.** Ordinal **SHALL NOT** be averaged/subtracted; unit mismatches **SHALL** fail fast (A.17–A.19/C.16).
9. **Coordinates honest.** Numeric encodings **SHALL** state what invariants they preserve and **SHALL NOT** silently upgrade measurement structure.
10. **Aggregation proven.** Published aggregation specs come with **proof obligations** (monotonicity, idempotence, boundary) or a rationale for weaker claims.
11. **UTS‑ready.** Names minted or reused; **twin labels** present; **loss notes** attached where bridged (F.17–F.18, F.9).
12. **Evidence wired.** Each Characteristic links to **R‑anchors** (KD‑CAL lanes) and **Worked‑Examples**.
13. **RSCR passing.** Tests enforce guards (ordinal arithmetic refusal, unit coherence, polarity checks, cyclic wrap rules).
14. **Design/run split.** Authoring is **design‑time**; run‑time policies live in CAL/LOG (A.4).
15. **Φ/planes surfaced in provenance.** Where a CHR card depends on cross‑Context/plane import, provenance **MUST** cite Bridge id and record **CL/CL^plane** policy‑ids visible to **G.4/G.5 SCR**; include **PathSliceId** for refresh.
16. **Lifecycle set.** Refresh/decay declared; deprecations follow **F.13–F.14** with **Lexical Continuity** notes.
17. **No thresholds in CHR.** All thresholds/guard‑bands live **only** in **AcceptanceClauses** (G.4); CHR **MUST NOT** embed policy cut‑offs (cf. C.21 practice).
18. **Φ(CL) monotone & recorded.** If CL penalties apply, **Φ(CL)**/**Φ_plane** **MUST** be monotone, table‑backed, and recorded with **policy id**; penalties route to **R_eff** only (never **F/G**).
19. **QD roles reproducible.** If a Characteristic participates in QD/Illumination, **QD.Role** and **DHCMethodRef.edition/DistanceDefRef.edition** are published (fronts reproducible across runs).
20. **Unknowns are tri‑state.** Missingness/unknowns propagate as **{admit\|degrade\|abstain}** into **Acceptance**; silent coercions forbidden.
21. **Archetypal Grounding present.** Two cross‑domain CHR examples are included (per E.8) to teach lawful CHR authoring without weakening legality guards; add a QD note if any Characteristic is used for Illumination.

### 10) Anti‑patterns & rewrites

* **Hidden cardinalization.** *Don’t:* treat ordinal encodings as interval; *Do:* publish an **isotonic** coordinate with clear limits.
* **Unit laundering.** *Don’t:* add cost (USD) to time (hours); *Do:* transform to lawful quantities or keep vector comparisons.
* **Global definitions.** *Don’t:* one “utility” for all Contexts; *Do:* Context‑local Characteristics with Bridges + CL.
* **Aggregation by convenience.** *Don’t:* “weighted averages” on ordinals; *Do:* medians, majority order, or lexicographic rules with proofs.
* **Design/run blur.** *Don’t:* bake policy thresholds into Scale definitions; *Do:* keep thresholds in CAL acceptance clauses.
* **Scalarizing partial orders.** *Don’t:* compress Pareto/poset outcomes into a single score; *Do:* return the **non‑dominated set** and defer selection to G.5 under lawful orders.

### 11) Consequences

* **Safety by construction.** Illegal operations are blocked at the **type/guard** level.
* **Comparable plurality.** Rival Traditions can co‑exist because CHR preserves **local meaning** and exposes **lawful** comparison.
* **Frictionless downstream.** CAL (G.4) and Dispatcher (G.5) receive **typed, UTS‑published** primitives with RSCR tests; QD/Illumination roles are reproducible (editions surfaced), and partial orders flow through as **sets/archives**.

### 12) Worked micro‑example (indicative)

*CG-Frame:* R\&D portfolio decisions.
**Objects:** `Project`. **Characteristics:**

1. `SafetyClass` — **ordinal**, Levels = {D,C,B,A,AA} (↑ better), admissible transforms = **order‑preserving**, **aggregation** default = **lexicographic min** across subsystems; **Coordinate** = isotonic map (order only).
2. `CostUSD_2025` — **ratio**, unit = USD (2025 real), admissible = positive scalar; allowed ops: +, × by scalar; **aggregation** = sum after **unit alignment**.
3. `Readiness` — **nominal**, Levels = {lab, pilot, field}; ops = equality, counts; no ordering unless a Bridge provides one with **CL** and loss note.
   **Guards:** `ORD_COMPARE_ONLY(SafetyClass)`, `UNIT_CHECK(CostUSD_2025)`, `RETURN_NONDOMINATED_SET()`.
   **UTS:** Name Cards minted; twin label “Safety rating” with loss note for marketing Context Bridge.
   **RSCR:** tests refuse `mean(SafetyClass)`; accept `median(SafetyClass)`; fail `CostUSD + Readiness`.
   **QD note:** if `SafetyClass` is used as a **D**‑characteristic (axis) in Illumination, publish `QD.Role=D` and `DistanceDef` (edition recorded).

### 13) Relations

**Builds on:** G.1, G.2; **MM‑CHR** (A.17–A.19/C.16); **F–G–R**; **Contexts/Bridges + CL**; **UTS**; **RoleAssignment**; **C.18 NQD‑CAL / C.19 E/E‑LOG**.
**Publishes to:** G.4 (CAL admissible operators, legality macros, freshness checks), G.5 (TaskSignature traits, QD roles/editions), **UTS**, RSCR, Worked‑Examples.
**Constrains:** any CAL/LOG implementation that consumes CHR.

### 14) Author’s quick checklist

1. Write the **Measurement Charter** and **KindMap** for the CG-Frame.
2. For each candidate Characteristic, **reuse** or **mint** in UTS with Name Card **+ twin labels**; cite **Bridge ids** where a CHR term is imported across Contexts, and surface **ReferencePlane** for any definitional claim.
3. Declare **Scale**, **Levels**, **Polarity**, **UnitSet**, **Bounds**, **Freshness**, **Evidence lanes**.
4. Publish any **Coordinate** with invariants preserved and explicit **non‑entitlements**.
5. Generate **Legality Matrix** + **Guard Macros** (`RETURN_NONDOMINATED_SET`, `METRIC_EDITION_REF` where applicable); wire **AggregationSpecs** with proofs.
6. Emit **RSCR** tests and **Worked‑Examples**; version the **CHR Pack**; set refresh/decay; surface **Φ‑policy ids** and, if QD is used, DHCMethodRef.edition/DistanceDefRef.edition.
