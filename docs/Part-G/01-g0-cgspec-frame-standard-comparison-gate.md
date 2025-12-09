## G.0 — **CG‑Spec · Frame Standard & Comparison Gate** \[A]

**Tag:** \[A] (foundational Standard; constrains G.1–G.5)
**Stage:** *design‑time* (establishes comparison legality & evidence minima; governs run‑time gates)
**Primary hooks:** **USM / Scope (G)** (A.2.6), **Design–Run split** (A.4), **Evidence carriers** (A.10), **Assurance F–G–R with Γ‑fold** (B.1, B.3), **Change rationale** (B.4), **MM‑CHR discipline** (A.17–A.19/C.16), **Creativity‑CHR** (C.17), **NQD‑CAL** (C.18), **E/E‑LOG** (C.19), **Method‑SoS‑LOG** (C.23), **Bounded Contexts & Bridges + CL** (F.1–F.3, F.9), **Concept‑Sets** (F.7), **Mint/Reuse** (F.8), **RSCR** (F.15), **Lifecycle/Deprecations** (F.13–F.14), **UTS & Naming** (F.17–F.18), **No tool lock‑in** (E.5.1–E.5.3), **Lexical rules** (E.10), **ATS Harness AH‑1…AH‑4** (E.11).

### 1) Intent (informative)

Provide a **single, normative Standard** for a **CG‑Frame** that (a) names *what may be compared or aggregated*, (b) defines **lawful ScaleComplianceProfile (SCP) and aggregators** over CHR‑typed data, and (c) sets **minimal evidence** and **trust folding** rules so that all downstream generation (G.1), harvesting (G.2), measurement authoring (G.3), calculus (G.4), and dispatch/selection (G.5) operate **safely, comparably, and in‑scope**.

### 2) Problem frame (informative)

A team is extending FPF with a **CG‑Frame** (e.g., *Creativity*, *Decision*, *Architecture trade‑offs*). G.1–G.5 reference **CG‑Spec** for lawful comparison, but absent a clear Standard, projects drift into hidden cardinalization, ad‑hoc thresholds, and opaque evidence minima. **G.0** authors and publishes that Standard.

### 3) Problem (informative)

Recurring pains without a frame‑level spec:

* **Undefined comparison set.** Teams compare quantities without a declared **Characteristic/SCP** basis.
* **Illicit arithmetic.** Ordinals get averaged; units are mixed; polarity flips are implicit.
* **Opaque evidence minima.** Numeric gates run on *whatever is at hand*, not on declared **KD‑CAL lanes** or carriers.
* **Trust blur.** Cross‑Context reuse lacks **CL penalties** and Γ‑fold rules; selection **R_eff** is not auditable.
* **Inconsistent scope.** Global claims leak; boundaries and *describedEntity* are not attached to names.

### 4) Forces (informative)

* **Pluralism vs. comparability.** Rival Traditions must co‑exist while enabling lawful comparison.
* **Expressiveness vs. safety.** Rich **SCP profiles** and aggregators vs. **MM‑CHR** legality.
* **Locality vs. portability.** Context‑local semantics with explicit **Bridges + CL** when crossing.
* **Assurance vs. agility.** Minimal evidence gates that are strong enough to matter, light enough to adopt.
* **Design‑time vs. run‑time.** Keep Standards and thresholds **design‑time**; run‑time only *uses* them.

### 5) Solution — **The CG‑Spec Standard**

A **notation‑independent** object, published to **UTS**, that fixes *what is comparable, how, and under which evidence and trust minima*.

For top‑level disciplines, CG‑Spec is restricted to comparability, tolerances, and aggregation surfaces where sufficient basis exists (KD‑CAL lanes, Worked Examples, Γ‑fold reliability). CG‑Spec MUST NOT introduce “universal” cross‑Tradition scoring; run‑time choice belongs to the G.5 selector under CHR/CAL legality.

#### 5.1 CG‑Spec · Data Model (normative)

```
CG‑Spec :=
⟨ UTS.id, Edition, Context, Purpose, Audience,
  Scope := USM.ScopeSlice(G) ⊕ Boundary{TaskKinds, ObjectKinds},
  describedEntity := ⟨GroundingHolon, ReferencePlane ∈ {world|concept|episteme}⟩,
  WorldRegime? ∈ {prep|live}, // refines ReferencePlane=world; affects acceptance/telemetry; introduces no new planes
  ReferenceMap := minimal map{term/id → UTS|CHR|G.2} (stabilizes naming & describedEntity),

  ComparatorSet := [ComparatorSpec…],                 // finite, explicit
    // MUST NOT encode illegal scalarisation of partial orders;
    // lawful forms include: ParetoDominance, Lexicographic over typed traits,
    // medoid/median on ordinals; WeightedSum only on interval/ratio with unit alignment (CSLC‑proven)
  Characteristics := [CHR.Characteristic.id…],        // must exist in G.3 pack

  SCP := map Characteristic.id → ⟨
    ScaleTypes, Polarity ∈ {↑|↓|=}, Unit alignment rules,
    CoordinatePolicy?, GuardMacros ⊇ {UNIT_CHECK, ORD_COMPARE_ONLY, FRESHNESS_CHECK, PLANE_NOTE, PHI_CL_MONOTONE(policy_id), METRIC_EDITION_REF(id)?},
    AggregationSpecs
  ⟩,

  MinimalEvidence := map Characteristic.id → ⟨
    KD‑CAL lanes ⊆ {TA,LA,VA}, Carriers ⊆ A.10,
    Sample/Replication minima, Freshness/HalfLife (PathSlice window), ReferencePlane,
    Bridge allowances (CL thresholds, CL^plane policy id), I/D/S layer exposed to SCR fields,
    FailureBehavior ∈ {abstain | degrade.order | sandbox},
    UnknownHandling := tri‑state {pass|degrade|abstain} with explicit binding to Acceptance (no silent `unknown→0` coercion)
  ⟩,

  Γ‑fold := ⟨default:=weakest‑link | override(proof_refs, monotonicity, boundary)⟩,
  CL‑Routing := map Bridge.CL → penalty on R_eff only (F invariant),
  Φ := ⟨ Φ(CL) MUST be monotone, bounded (R_eff ≥ 0), and table‑backed; optional Φ_plane for {world|concept|episteme} crossings (unaffected by WorldRegime) ⟩,
  AcceptanceStubs := [AcceptanceClause template…],    // templates only; **context‑local thresholds live in CAL.Acceptance (G.4)**
  
  E/E‑LOG Guard := ⟨explore↔exploit budgets, probe accounting, NQD constraints⟩,
  Illumination := ⟨
    Q_refs ⊆ Characteristics, D_refs ⊆ Characteristics,
    QD_score := definition (typed), ArchiveRef := U.DescriptorMapRef (Tech; d≥2),
    InsertionPolicy, Edition := ⟨DHCMethodRef.edition, DistanceDefRef.edition⟩,
    DominanceDefault := exclude, PromotionPolicy? := lens/policy‑id
  ⟩, // Illumination gauges Diversity_P and informs exploration; not part of dominance unless PromotionPolicy is named

 RSCR := testset{
    illegal_op_refusals,
    unit/scale checks,
    freshness windows,
    partial‑order scalarisation refusals,
    threshold semantics,
    CL→R_eff routing,
    refuse degrade.order on unit mismatches (MM‑CHR)
 },

  Naming := UTS Name Cards (required fields per F.17/F.18) with **Unified Tech** and **Plain** labels, Concept‑Set linkage, Bridge loss/fit notes, and lifecycle,
  Lifecycle := ⟨owner, DRR link, refresh cadence, decay/aging, deprecation + lexical continuity⟩,
  Provenance := ⟨carrier types, SoTA pack refs (G.2), DRR/SCR linkage⟩
⟩
```

**Notes:**
* `Characteristics[]` are pointers—no measurement semantics live here; those are authored in **G.3**.
* `SCP` binds **what** aggregations/comparisons are lawful **for this Frame** over those characteristics (using **G.3 AggregationSpecs**).
* `MinimalEvidence` is the **gate** consumed by G.1/M4 and G.5: if not met, numeric comparisons **degrade** to safe forms or **abstain** (see **§7.13**).
* `Γ‑fold` must state monotonicity and boundary behavior if not weakest‑link; proofs/anchors go to **CAL.ProofLedger** (G.4); legality constraints summarized in **§7.5–§7.7**.
* **Legality proof.** Units/scale/polarity legality **MUST** be proven via **MM‑CHR/CSLC** before any aggregation; **no silent `unknown→0` coercion**; thresholds live **only** in Acceptance (G.4) — see **§7.7** and **§7.8**.
* `CL‑Routing` sends penalties to **R_eff only**; **F** is invariant under Bridging.
* **Illumination default.** Illumination is a gauge over **Diversity_P** (coverage/QD‑score). It informs exploration/refresh and tie‑breaks; it is **not** in the dominance set unless a **PromotionPolicy (lens/policy‑id)** is named.
* **Partial orders.** Where only a partial order is lawful, **do not force total orders** in `ComparatorSet`; downstream (G.5) returns explicit non‑dominated sets.
* **Guard macros.** Recommended set includes: `UNIT_CHECK`, `ORD_COMPARE_ONLY`, `FRESHNESS_CHECK`, `PLANE_NOTE`, `PHI_CL_MONOTONE(policy_id)`.

#### 5.2 SoTAPalette

1. **SoTAPalette (I).** Intensional profile of a discipline’s Traditions and method‑families with intentions and tolerances:
* admissible TaskKinds/ObjectKinds,
* required CHR types,
* characteristic operators/proofs,
* typical CL bridges (with known loss).

2. **SoTAPaletteDescription (D).** Publication of the palette: 
* metadata of Traditions, 
* Operator & Object Inventory, 
* Bridge Matrix with CL/loss notes, 
* micro‑examples, 
* UTS drafts. 
 
This is the “SoTA Synthesis Pack” of G.2 and must be citable in G.5 decisions.

3. **SoTAPaletteSpec (S).** Minimal gates on completeness/quality of a palette: 
* coverage of Traditions/sub‑tasks, 
* minimum replications/carriers across KD‑CAL lanes (TA/LA/VA), 
* explicit CL penalties for reductions, and bans on illegal operations (e.g., ordinal ≠ mean). 
 
These gates are consumed by CG‑Spec.Acceptance and Γ‑fold where cross‑Tradition comparison/aggregation is attempted

#### 5.3 Tradition

* In this framework, **“scientific/engineering Tradition/lineage/tradition” is an epistemic kind**: **`Tradition`** (I) with its **`TraditionDescription`** (D) and **`TraditionSpec`** (S).
* The **community of people** behind a Tradition is modeled separately as an optional **`TraditionCarrier`** that _carries_ a `Tradition` but does **not** determine cross‑Tradition comparability rules.
* In the **SoTA‑palette**, entries are **`Tradition`** items (epistemic) with their D/S artifacts; the palette composes them and exposes bridges/limits. The Dispatcher (G.5) selects among these entries under CHR/CAL constraints; CG‑Spec (G.0) only governs comparability/Γ‑fold where justified.

Tradition (I): an epistemic formation (Tradition‑of‑thought, lineage) identified by its method family:
- operator set and admissible transformations,
- admissible TaskKinds/ObjectKinds,
- necessary CHR types and proof idioms,
- canonical CL bridges and stated limits,
- stance on measurement scales and allowed algebra.
(Notes: This is an epistemic kind, not a social group. See §TraditionCarrier for the social carrier.)

TraditionDescription (D): the documentary corpus of a Tradition:
- charter/lineage and key references,
- Operator & Object inventory with CHR preconditions,
- Bridge Matrix (CL) with loss and validity regions,
- Worked Examples with CHR annotations,
- UTS drafts for typical tasks,
- KD‑CAL lane coverage and replication notes,
- explicit anti‑operators / banned reductions (e.g., ordinal ≠ mean).

TraditionSpec (S): inclusion gates for a Tradition to be considered comparable/aggregable:
- minimum replication across KD‑CAL lanes (TA/LA/VA),
- declared CHR prerequisites and proof idioms,
- declared CL penalties/conditions for any cross‑Tradition bridge,
- Γ‑fold contribution rule (how evidence accumulates),
- prohibitions on illegal scale algebra.
These S‑level gates are referenced by CG‑Spec.acceptance only where aggregation/comparison is attempted; otherwise the Tradition remains descriptive.

TraditionCarrier (I): role of a social/organizational system (people, labs, consortia) that holds a Tradition. Carriers supply replication capacity and provenance but have no normative authority over cross‑Tradition aggregation rules.

Γ‑fold: an evidence/reliability fold that aggregates only along declared commensurate dimensions; includes penalties from CL bridges and lane‑mismatch factors. Γ‑fold parameters MUST be cited to KD‑CAL lanes and Worked Examples; when absent, aggregation is disallowed.

Default composition: weakest‑link; admissible overrides: {min‑k‑of‑n, harmonic, conservative Bayesian}; override requires CAL.ProofLedger refs

#### 5.4 Authoring Steps (S1–S6)

**S1 · Frame Charter (Scope & describedEntity)**
Declare **Context**, **USM scope**, *describedEntity* (`GroundingHolon`, `ReferencePlane`), TaskKinds/ObjectKinds; record boundary examples and non‑examples.

**S2 · Comparator Set & Gauge Draft**
List **which** comparisons/aggregations the Frame intends (e.g., dominance, lexicographic, Pareto, affine sums on interval/ratio with unit alignment). Bind each comparator to **G.3/AggregationSpecs** and attach **GuardMacros**. **Do not** scalarise partial orders; for ordinals, use medoid/median; **WeightedSum is forbidden** on mixed scale types.

**S3 · Characteristics Binding**
For each comparison you intend to allow, bind the **CHR.Characteristic id** and required **Scale/Unit/Polarity**; if missing, author in **G.3** or reuse via UTS (F.8). For any numeric encoding of ordinals, publish **CoordinatePolicy** with non‑entitlements.

**S4 · Minimal Evidence Gates**
Per characteristic, declare **KD‑CAL lanes** (TA/LA/VA), required **carriers** (A.10), freshness/half‑life, and **Bridge/CL allowances**. Define **failure behavior**: **degrade to order‑only**, **sandbox**, or **abstain**.

For unit mismatches specify **sandbox (quarantine) or refuse**; **degrade.order is not permitted for unit mismatches under MM‑CHR**.

MinimalEvidence MUST name **CHR.Characteristics** used by Acceptance/Flows and the **TaskSignature fields** they constrain (by id), so **G.5** can gate **before** selection.

**S5 · Γ‑fold & CL Routing**
Set default **Γ‑fold** for trust aggregation and the **CL penalty** table. Document proofs or references if overriding weakest‑link.

**S6 · Publication & Tests**
Mint **UTS** Name Cards with twin labels; attach **loss notes** for Bridges. Register **RSCR** tests: (i) refuse illegal ops (e.g., mean on ordinal), (ii) enforce unit/scale checks, (iii) verify freshness/PathSlice handling, (iv) refuse illegal scalarisation of partial orders, (v) verify **CL → R_eff** routing and **Φ(policy‑id)** publication in SCR.
Acceptance depends on (a) presence of SoTAPaletteDescription (G.2) with attached CHR/CAL evidence (G.3–G.4), and (b) justification of any aggregation via Γ‑fold (reliability fold) with explicit CL loss accounting. Where evidence is insufficient, acceptance MUST fall back to per‑Tradition reporting without cross‑Tradition aggregation.

### 6) Interfaces — minimal I/O Standard (normative)

| Interface          | Consumes                                | Produces / Constrains                                                    |
| ------------------ | --------------------------------------- | ------------------------------------------------------------------------ |
| **G.0‑1 Charter**  | CG‑Frame brief, USM scope, SoTA signals | `CG‑Spec.Scope`, `describedEntity`, `ComparatorSet`                            |
| **G.0‑2 SCP**      | G.3 CHR Pack, AggregationSpecs          | `CG‑Spec.SCP` + guard bindings                                           |
| **G.0‑3 Evidence** | SoTA carriers (G.2), KD‑CAL norms       | `CG‑Spec.MinimalEvidence`, `Γ‑fold`, `CL‑Routing`                        |
| **G.0‑4 Publish**  | All above                               | Versioned `CG‑Spec@UTS` + Name Cards, RSCR ids, Lifecycle                |
| **→ G.1**          | `CG‑Spec`                               | M1/M4 guardrails; abstain/degrade paths wired; M3/M4 scoring legality; Characteristic refs bound (F invariant) |
| **→ G.2**          | `CG‑Spec`                               | Inclusion/exclusion & Bridge/CL policy for SoTA Synthesis                |
| **→ G.3**          | `CG‑Spec`                               | Which Characteristics/Scales must exist; legality macros to expose       |
| **→ G.4**          | `CG‑Spec`                               | Acceptance templates; evidence gates; Γ‑fold/CL routing Standards        |
| **→ G.5**          | `CG‑Spec`                               | Eligibility gates; minimum **R_eff** checks; degradation/abstain policies; Illumination hooks (ArchiveRef/U.DescriptorMapRef, InsertionPolicy, Edition), publication of **Φ(CL)/Φ_plane policy‑ids** in SCR |
| **→ G.6**          | `CG‑Spec`                               | EvidenceGraph guard fields (**Φ(CL)/Φ_plane policy‑ids**, freshness windows, **PathId/PathSliceId**) made citable; selectors/audits reference PathIds (no formats mandated) |