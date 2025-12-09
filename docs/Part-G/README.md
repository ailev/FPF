# Part G – Discipline SoTA Architheory Kit

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
## 7) Conformance Checklist (normative)

1. **Context declared.** `CG‑Spec` is published **in** a `U.BoundedContext`; no global claims.
2. **Comparator set explicit.** Every permitted comparison/aggregation is named and typed; anything else **abstains by default**.
3. **CHR‑bound.** All compared quantities reference **CHR.Characteristic ids** with declared **Scale/Unit/Polarity**; guard macros attached.
4. **Minimal evidence published.** Per characteristic: **KD‑CAL lanes**, carriers, freshness, Bridge/CL allowances, and **failure behavior** are declared.
5. **Γ‑fold stated.** Default **weakest‑link**, or an alternative with proof obligations (monotonicity, boundary).
6. **CL penalties** routed to R_eff only; F is invariant; **publish Φ(CL)/Φ_plane policy‑ids in SCR** for any penalised claim.
7. **No illegal ops.** Ordinal **SHALL NOT** be averaged/subtracted; unit mismatches **SHALL** fail fast (MM‑CHR).
8. **Design/run split.** **AcceptanceStubs** provide templates in **G.0**; all **context‑local thresholds live only in CAL.Acceptance (G.4)**; nothing is hidden in CHR or code paths; manifests are externally inspectable.
9. **UTS‑ready.** Name Cards minted/reused with twin labels; Bridges carry **CL** and loss notes.
10. **RSCR wired.** Tests exist for refusal paths, unit/scale checks, threshold semantics, and CL→R_eff routing.
11. **Lifecycle set.** Refresh cadence and decay policy declared; deprecations follow **F.13–F.14** with lexical continuity notes.
12. **describedEntity present.** `GroundingHolon`, `ReferencePlane`, and a minimal `referenceMap` are recorded.
13. **Pre‑flight numeric gates.** Any numeric comparison/aggregation **MUST** cite a `CG‑Spec` entry with lawful **SCP/Γ‑fold** and **MinimalEvidence** satisfied; cross‑Context reuse requires **Bridge + CL** with penalties routed to **R_eff only** (never F).
14. **Partial‑order stance.** `ComparatorSet` SHALL NOT force total orders where only partial orders are lawful; **no scalarisation of partial orders**. Use Pareto/Lexicographic/medoid/median as lawful.
15. **Illumination discipline.** If Illumination is used, publish `ArchiveRef`, `InsertionPolicy`, and `Edition`; **exclude from dominance by default**; any promotion into dominance **MUST** cite a named lens/policy‑id and be recorded in provenance.
16. **Freshness/PathSlice.** Freshness windows are published and enforced; PathSlice identifiers are recorded in SCR when freshness gates influence gating/selection.
17. **ATS harness exposure.** Exports **MUST** provide inputs for **AH‑1..AH‑4** (tier/gate/lane/lexical checks per E.11) over EvidenceGraph paths and crossings; any failure is **blocking** for publication.

**Guards as in C.20:**
* **CC‑G0‑Φ.** **Φ(CL)** (and **Φ\_plane**, if used) **MUST** be **monotone, bounded, table‑backed**; publish policy ids; **R\_eff ≥ 0** by construction.
* **CC‑G0‑Unknowns.** **Unknowns propagate tri‑state** {pass|degrade|abstain} to **Acceptance**; **no silent coercions**.
* **CC‑G0‑CSLC.** **Scale/Unit/Polarity legality** MUST be proven (MM‑CHR/CSLC) **before** any aggregation; **no mean on ordinals; no unit mixing**.
**Registry hooks.** Every CG‑Spec entry declares Lifecycle/DRR and **RSCR triggers for Φ‑table, SCP, Γ‑fold, Bridge edits** (parity re‑runs required).

### 8) Consequences (informative)

* **Lawful comparability.** Teams know *exactly* what can be compared/aggregated and under which evidence minima.
* **Auditable trust.** Γ‑fold and CL routing make **R_eff** computation transparent to selectors and reviewers.
* **Frictionless downstream.** G.1–G.5 consume a single spec; CHR/CAL avoid hidden thresholds; dispatch is explainable.
* **Local first, portable later.** Context‑local semantics are primary; Bridges make portability deliberate and costed.

### 9) Worked micro‑example (indicative)

CG‑Frame: R&D Portfolio Decisions
Scope: ObjectKinds={Project}, TaskKinds={SelectPortfolio}
describedEntity: ⟨GroundingHolon=R&D, ReferencePlane=world⟩

ComparatorSet = {
  ParetoDominance,
  LexicographicMin(SafetyClass),
  AffineSum(CostUSD_2025)
}

Characteristics = \[
  SafetyClass : scale=ordinal,  polarity=↑, levels={D,C,B,A,AA},
  CostUSD_2025 : scale=ratio,   polarity=↓, unit=USD_2025,
  Readiness : scale=nominal,    polarity="="
]

 SCP:
  SafetyClass   → ORD_COMPARE_ONLY; aggregator=LexiMin; coordinate=Isotonic(order‑only) // no means
  CostUSD_2025  → UNIT_CHECK; aggregator=Sum; unit_alignment=USD_2025; polarity=↓
  Readiness     → equality_only; aggregator=None; ordering via Bridge only (CL≥2 with loss note)

MinimalEvidence:
  SafetyClass  → lanes={LA}, carriers={test_reports}, freshness≤18mo,
                  failure={abstain if lanes/carriers missing; refuse if mean() attempted}
   CostUSD_2025 → lanes={LA,VA}, carriers={ERP,audit}, freshness≤12mo,
                  failure={refuse if unit misaligned; sandbox if carrier missing}

  Readiness    → lanes={VA}, carriers={process_docs}, freshness≤12mo,
                  failure={abstain for ordering unless Bridge(CL≥2)}

Γ‑fold := weakest‑link across lanes
CL‑Routing: CL=2 (Marketing→Engineering) → multiplicative penalty on R_eff; F invariant

AcceptanceStubs:
  AC_SafetyGate: SafetyClass ≥ B
  AC_Budget: Σ CostUSD_2025 ≤ Envelope

RSCR:
* refuse mean(SafetyClass)
* fail on (USD + Readiness)
* verify AC_Budget on worked examples

## 10) Relations (wiring)

**Builds on:** A.4, A.10; **B.1/B.3/B.4**; **A.17–A.19/C.16**; **C.17–C.19**; **F.1–F.3/F.7–F.9/F.13–F.15/F.17–F.18**; **E.5.1–E.5.3** (no tool lock‑in); **E.10**.
**Publishes to:** G.1 (generator guards), G.2 (harvesting policy & CL), G.3 (required CHR), G.4 (acceptance/evidence), G.5 (eligibility gates).
**Constrains:** any LOG implementation via CAL/CHR legality and evidence minima.

### 11) Author’s quick checklist

1. Write the **Frame Charter** (Context, USM scope, describedEntity).
2. Enumerate the **ComparatorSet**; bind **SCP** with guard macros and AggregationSpecs.
3. Bind **Characteristics\[]** to **CHR** ids; ensure Scale/Unit/Polarity are declared (reuse or mint in UTS).
4. Publish **MinimalEvidence** per characteristic (KD‑CAL lanes, carriers, freshness, Bridge/CL allowances, failure behavior).
5. State Γ‑fold and CL‑Routing; **default Γ‑fold = weakest‑link**; if overriding, attach CAL proofs (monotonicity, boundary behavior). Record **Φ(CL)/Φ_plane** **policy ids**; penalties → **R_eff only**.
6. Publish to **UTS** with Name Cards, twin labels, Bridges (+loss notes); register **RSCR** tests.
7. Set **refresh/decay**; log changes to **DRR/SCR**; maintain lexical continuity on deprecations.

## G.1 — **CG-Frame‑Ready Generator** \[A]

**Stage:** *design‑time* (produces design‑time architheories & assets; enables run‑time use by target architheories)
**Working‑Model first:** prefer working models and didactic micro‑examples; escalate to formal harnesses only where risk warrants (per E.8).
**Primary hooks:** see **§11 Relations** for wiring. **Pre‑flight (via G.0/G.3/G.4):** lawful CHR typing + CG‑Spec for any comparison/aggregation; publish **ReferencePlane** on claims; on plane mismatch compute and publish **CL^plane** with **Φ_plane** (policy‑id); **Φ(CL)**/**Φ_plane** are **monotone, bounded, table‑backed** (policy‑ids recorded); **unknowns tri‑state** propagate as {pass|degrade|abstain} (no `unknown→0`); **CL penalties → R only** (F/G invariants); **fail‑fast on CSLC/scale mismatches** with **RSCR wiring**. See **§8 (Conformance), items 7 and 17–19**.
**Minimal publication unit:** the **six M1–M6 cards** (Context, SoTA‑set, VariantPool+EmitterTrace, Shortlist+DRR/SCR, F‑bindings, Refresh plan) are published as a **complete, reusable package** for the CG‑Frame.

### 1) Intent

Provide a **repeatable generator scaffold** that **targets goldilocks slots (feasible‑but‑hard)** and records **abductive provenance** for candidate variants for a declared **CG‑Frame**, (a) assembles a **local SoTA set**, (b) **emits** well‑typed **variant candidates** for private cases, and (c) **selects & packages** the winners into the **F‑suite** (RoleDescription templates, Concept‑Sets, UTS rows, names) with explicit trust and scope.
**Outputs (design‑time):** `AT1 TaskPack` + `VariantPool` + provenance (**A.10** anchors, **EmitterPolicyRef**) **+ per‑candidate SCR‑preview** (fields: **Φ(CL)/Φ_plane policy‑ids**, CL notes, ReferencePlane, UnknownHandling branch) **+ an ε‑Pareto front and an IlluminationSummary (pre‑thinning)** with **DescriptorMapRef**, **DHCMethodRef.edition/DistanceDef**, and archive **InsertionPolicy (incl. K‑capacity/dedup)** recorded, ready for G.2/G.5.

### 2) Problem frame (Design‑time vs Run‑time roles)

* **G‑pattern (this):** defines the *authoring choreography*.
* **Design‑time architheories of a CG-Frame:** CAL/LOG/CHR bundles produced by G.1 into a **library for this CG-Frame** (e.g., “Creativity theories”, “Decision theories”). ; method artefacts publish as **MethodDescription** by default and become **MethodSpec** only when a falsifiable harness exists (E.10.D2/D3; I/D/S discipline).
* **Run‑time target architheories:** the deployed theories/methods that users run to generate ideas or make decisions (gated by B.3; separated by A.4).
* **Local glossary:** *DRR* = Decision Rationale Record; *SCR* = Selection Confidence Report (fields: chosen family, eligibility verdicts, Γ‑fold contributors, CL penalties, R_eff); **MDS** = UTS metadata stub (Name Card + twin labels).

**Terminology hook (ATS stance & governance).**
— **AT0 (Applied‑run).** Execution outside FPF’s transdiscipline scope; AT0 imports into AT1 only via **BridgeCard + UTS** with **CL** loss notes. AT0 tokens do not assert norms upstream (E.11 AH‑2).  
— **AT1 (Transdiscipline‑design).** Translation of applied problems into **TaskPack** and **methods‑about‑methods**; **comparability lives in a `U.Discipline` CG‑Spec** (not on Domain labels). Domain is catalog‑only, stitched to **D.CTX + UTS** (C.20; E.11 §6).  
— **AT2 (Architheory authoring).** Publishes CHR/CAL/LOG packs; **CL/CL^k/CL^plane penalties route to `R_eff` only**; F/G invariants unchanged (KD‑CAL; E.11 AH‑3).  
— **AT3 (Meta‑authoring).** Organises AT2; **cannot override AT2 F/G** (E.11 table).  
— **Strategy/policy.** Do **not** mint a new kernel head “Strategy”: strategy is a **composition inside G.5** under **E/E‑LOG**; keep “strategy” only in the Plain register where pedagogically useful (C.22 bias‑annotation).

### 3) Problem (recurring pains the pattern solves)

* SoTA is scattered; no **local, scoped** set for a CG-Frame.
* Variant generation is ad‑hoc; **private cases** lack a principled emitter.
* Selection is taste‑driven; **trust & comparability** are opaque.
* Output doesn’t land in **F‑artifacts** (RoleAssignments/UTS/names), so it can’t be reused.

### 4) Forces (tensions to balance)

* **Breadth vs depth** (cover SoTA yet stay actionable).
* **Generativity vs assurance** (novel variants vs safety/trace).
* **Local meaning vs portability** (Context‑local semantics vs Bridges/CL).
* **Expressiveness vs parsimony** (new types vs reuse per F.8).

### 5) Solution — **Six‑module generator chassis**

*(Each module is a slot with explicit inputs/outputs and guard‑rails; minimal, substrate‑neutral.)*

**M1 · CG-Frame Card (scope anchor)**

 **Inputs:** CG-Frame name; purpose; audience; boundary; **USM scope claims (G) + SenseCells (F.3)**; **comparability/CL policy**;  **describedEntity:** GroundingHolon(X); **ReferencePlane ∈ {world, concept, episteme}**;   **referenceMap:** observable cues → CHR candidates (instrument/protocol/uncertainty)
**Outputs:**` CG-FrameContext := U.BoundedContext `+ **USM.ScopeSlice(G) + MDS** + **describedEntity block** + **Bridge policy** (CL thresholds) + **Γ‑fold** hints (B.1) + **UTS row id** (⟨CG‑FrameDescription | CG‑Spec⟩)`

**M2 · SoTA Harvester (scoped set)**

**Inputs:** discovery queries, canonical sources (**post‑2015 Science‑of‑Science surveys & field studies**), inclusion/exclusion criteria
**Ops:** normalise terms (F.2), cluster senses (F.3), draft Concept‑Set rows (F.7), **apply G.2 harvesting discipline** (discovery → claim sheets → bridge matrix)
**Outputs:** `SoTA_Set@CG-Frame` with provenance (A.10) + preliminary **UTS stubs** (F.17) **incl. twin labels + loss notes for bridged terms**
**Guards:** Evidence Graph Ref; CL for cross‑Context reuse (F.9); **lawful measurement (A.17–A.19/C.16)**; Trust baseline (B.3).

**M3 · Variant Emitter (illumination search)**

* **Inputs:** SoTA_Set; private constraints; resource envelopes
* **Ops:** open‑ended emitters (**NQD‑CAL**, **d≥2 DescriptorMap**); policy governor (E/E‑LOG); **abductive trace** (B.5.2) with A.10 anchors per lane and **ReferencePlane** on claims. **Optional OEE branch:** register a **Task/Environment GeneratorFamily (POET‑class)** with `EnvironmentValidityRegion` and `TransferRules`; bind SoS‑LOG/Acceptance branches for environment evolution; **telemetry must record edition‑aware Illumination increases with policy‑id**.
* **Scoring:** Creativity‑CHR characteristics (Novelty, Surprise, ConstraintFit, **Diversity**), **QD‑triad {Q, D, QD‑score}** per C.18; 
* **Outputs:** `VariantPool` with **EmitterTrace** (who/why/where) **+ SCR‑per‑candidate preview** (constraints/gates consulted; CL notes; **Φ policy‑ids**; ReferencePlane; **UnknownHandling={pass|degrade|abstain}** recorded) **+ IlluminationSummary (DescriptorMapRef, DHCMethodRef.edition, grid/binning)**.
* **Guards:** explore↔exploit policy (C.19); SoD (A.2 `⊥`); no category leaks (A.7); **metric legality/typing per MM‑CHR (A.17–A.19/C.16)**; **unknowns are tri‑state with explicit failure policy {degrade|abstain|sandbox} recorded in the EmitterTrace/SCR‑preview**; if a score/aggregation implies cross‑candidate comparison, cite a registered **CG‑Spec.characteristic**; otherwise degrade to lawful orders (median/medoid/lexi) or **abstain**.

CharacteristicSpace includes a **domain‑family coordinate** (grid or CVT / Centroidal Voronoi Tessellation centroids) per F1‑Card. **Archive InsertionPolicy** and **DistanceDefRef** editions MUST be recorded. Pre‑front thinning MAY use DPP or submodular Max‑min under the **Heterogeneity‑first** lens. Record in provenance: sampler class & seed, family‑quota vector (incl. k), subFamilyDef id (if used), and **δ_family/DistanceDefRef.edition** (via DescriptorMapRef).

**M4 · Selector & Assurer (fit‑for‑purpose)**

* **Inputs:** VariantPool; acceptance clauses; risk constraints
* **Ops:** evaluation & evidence (CAL hooks); **apply ConstraintFit=pass as an eligibility filter before any front computation**; compute an **ε‑Pareto front** (and/or archive under lawful partial orders) with **no forced scalarisation**; **Γ‑fold** aggregation (B.1); F–G–R roll‑up (B.3) with **CL→R only**; enforce **CG‑Spec.MinimalEvidence** for any characteristic used in evaluation; **keep thresholds in `G.4 CAL.Acceptance` (no thresholds in CHR/LOG)**; gate Γ‑fold contributors accordingly; when only ordinal semantics are lawful, avoid weighted sums and use lexicographic/median/medoid comparators; **surface Φ(CL)**/**Φ_plane** policy‑ids in SCR (per Pre‑flight); record **ε** and **DHCMethodRef.edition** used for any front computation.
* **Outputs:** `Shortlist` (**ε‑Pareto/Archive set**, not a singleton) with **Assurance tuples** ⟨F,G,**R_eff**⟩ + decision rationale (E.9 **DRR + SCR**, including **Φ(CL)/Φ_plane policy‑ids** and ReferencePlane on any penalised claim)
* **Guards:** CL penalties for cross‑Context imports; ageing/decay (B.3.4); **SoD for approval; minimum‑R gates**.

**M5 · F‑Binding (publication surface)**

* **Inputs:** Shortlist; local senses
* **Ops:** mint/ reuse (F.8), create RoleDesc (F.4), finalise Concept‑Set rows (F.7), write UTS entries (F.17), propose names (F.18), **register RSCR tests (F.15) and Worked‑Examples**; carry the **describedEntity block** (GroundingHolon, ReferencePlane, referenceMap summary) into UTS Name Cards/rows; ensure **CharacteristicRef**s point to **CG‑Spec.characteristics\[] ids**.

* **Outputs:** `CG-FrameLibrary` (CAL/LOG/CHR bundles) + **UTS entries with twin labels + loss/bridge notes** + Name Cards **+ RSCR ids**
* **Guards:** **No tool lock‑in (E.5.1–E.5.3)**; lexical rules (E.10); measurement discipline (A.17–A.19/C.16).
 
**M6 · Packaging & Refresh (evolution loop)**

* **Inputs:** DRR changes; telemetry (**PathSlice**, **IlluminationSummary (edition‑aware)**, coverage/regret); evidence refresh cadence; adoption feedback; policy‑ids (Φ).
* **Ops:** version sign‑off; bias audit (D.5); refresh NQD emitters; retire/merge per F.13–F.14; **refresh RSCR/Worked‑Examples; maintain lexical continuity; record refresh/decay signals from telemetry**.
* **Outputs:** `CG‑Kit@CG‑Frame` (versioned), with refresh policy & refresh hooks **+ deprecation notices (F.13)** and **telemetry hooks** (PathSliceId, policy‑ids, coverage/regret)
* **Guards:** A.4 temporal duality; evidence decay; change‑impact trace (B.4/E.9).

> **Julia‑inspired specialisation note (design‑time only):** within M3–M4, **parametric specialisation** and **trait‑like dispatch** are allowed as a *notation‑free* idea: variants are emitted/selectable by **type‑parameters** (capability envelopes, scale, constraint traits) rather than ad‑hoc flags. No tool lock‑in; semantics live in CAL/CHR.

### 6) Interfaces — minimal I/O Standard

| Module | Consumes                       | Produces                                              |
| ------ | ------------------------------ | ----------------------------------------------------- |
| M1     | CG-Frame brief                    | `CG-FrameContext` (+ CL policy, Γ‑fold)                  |
| M2     | sources, criteria              | `SoTA_Set@CG-Frame`, UTS stubs                           |
| M3     | SoTA_Set, private constraints | `VariantPool` (+ Creativity‑CHR scores, QD‑triad, IlluminationSummary, EmitterTrace, DescriptorMapRef/DHCMethodRef.edition/DistanceDefRef) |
| M4     | VariantPool, acceptance        | `Shortlist` (**ε‑Pareto/Archive set**; + ⟨F,G,R_eff⟩, DRR + SCR, **ε**, **DHCMethodRef.edition/DistanceDefRef**) |
| M5     | Shortlist                      | RoleDesc templates, Concept‑Set rows, UTS rows, Name Cards |
| M6     | DRR deltas, **telemetry (PathSlice, coverage/regret, policy‑ids Φ)** | Versioned `CG‑Kit@CG‑Frame`, refresh plan + **telemetry hooks** |

### 7) Archetypal Grounding (Tell–Show–Show)
**Tell.** The generator targets **goldilocks** problems (feasible‑but‑hard), assembling a local SoTA set, a `VariantPool`, and (when needed) an `AT1 TaskPack`, under **E/E‑LOG** policy with lawful CHR typing and CG‑Spec bindings.
**Show A (Software R&D).** Context: R&D multi‑criteria decisions. M2 harvests outranking/value/portfolio fronts; M3 emits variants under budget/risk; M4 selects with acceptance clauses; M5 publishes RoleDesc/Concept‑Sets/UTS; M6 versions the `CG‑Kit` with quarterly refresh.
**Show B (Clinical ops).** Context: dose‑adjustment design. M2 harvests SoTA dosage models and safety invariants; M3 emits policy‑constrained variants; M4 gates by safety acceptance; M5 publishes `Safety‑Invariants` and Name Cards; M6 maintains refresh & deprecations.

### 8) Conformance Checklist (normative, terse)

1. **Context declared.** Every artifact is spoken **in** `CG-FrameContext` (U.BoundedContext); no global claims.
2. **describedEntity present.** Every …Description published in G.1 carries `describe: GroundingHolon`, `ReferencePlane`, and a minimal `referenceMap`.
3. **CG‑Spec required for comparisons.** Any numeric comparison/aggregation cites a **CG‑Spec** (characteristics, gauge, Γ‑fold); cross‑Context/Tradition use via **Bridge + CL** with penalties to **R_eff** only (never to F).
4. **Evidence anchored.** All SoTA imports and evaluations link to carriers (A.10); no self‑evidence.
5. **Design/run split.** Generators & selections are **design‑time**; operational runs are **Work** (A.4/A.15).
6. **Emitter governed.** NQD emitters operate under an explicit **E/E‑LOG** policy; portfolio coverage is recorded (C.18–C.19).
7. **Trust visible.** Each shortlist item carries ⟨F,G,**R_eff**⟩ with CL penalties (B.3; F.9).
8. **F‑surface complete.** Winners are published as **RoleAssignment/Concept‑Set/UTS** with local naming (F.4/F.7/F.17–F.18).
9. **Parsimony.** Prefer *reuse* over minting new U.Types (F.8); justify new ones via C.1 universality.
10. **Measurement typed.** All metrics use **CHR typing (Characteristic/Scale/Level/Coordinate)**; forbid illegal ops (A.17–A.19/C.16).
11. **SoD enforced.** Exploration authors ≠ selection approvers where required (A.2 `⊥`).
12. **Refresh set.** A cadence for evidence/variants is declared; stale items accrue **Epistemic Debt** (B.3.4).
13. **DRR/SCR emitted.** Every selection emits **DRR + SCR**; **R_eff** computed via **Γ‑fold** with CL penalties.
14. **UTS twin labels.** Published winners include **twin labels** and **loss notes** for any bridge.
15. **No tool lock‑in.** Core artifacts are notation‑independent; **no vendor/tool keywords in Core**; implementations live under **E.5.\***.
16. **RSCR wired.** Regression tests are registered for each published artifact (F.15).
17. **Φ‑policies surfaced.** Wherever CL/CL^plane penalties are used, **Φ** policies are **monotone, bounded, table‑backed**, with **policy‑ids** in SCR; **R_eff ≥ 0** by construction (per Pre‑flight/G.0).
18. **Unknowns are tri‑state.** Unknowns **propagate as {pass|degrade|abstain}** to Acceptance/Eligibility; **no `unknown→0/false` coercion**; behavior recorded in SCR.
19. **ATS harness pass.** Published crossings pass **E.11 AH‑1..AH‑4** (TierClassifier, GateCheck, LaneCheck incl. **CL→R only** and **CL^plane** if planes differ, LexicalCheck).
20. **Three‑family breadth (domains).** `SoTA_Set@CG‑Frame` spans **≥3 domain‑families** per A.8 (Exact/Natural/Eng&Tech/Formal/Social&Behavioural), with Bridge hygiene for any crossings. AND MinInterFamilyDistance ≥ δ_family (from F1‑Card); publish {FamilyCoverage, MinInterFamilyDistance, Diversity_P, IlluminationSummary} with explicit F1‑Card reference and **DistanceDefRef.edition**.
21. **QD‑triad evidence.** The generator **records** `Diversity_P` and **IlluminationSummary** for the triad used to motivate any “universal” UTS row or Core candidate; provenance includes `DescriptorMapRef`, **DHCMethodRef.edition**, and grid/binning; **archive InsertionPolicy (K‑capacity/dedup)** is visible.
22. **Emitter trace includes coverage.** `EmitterTrace` (M3) **MUST** log triad coverage (IlluminationSummary) alongside ⟨F,G,R_eff⟩ and CL notes; promotion of illumination to dominance remains **forbidden by default** (policy‑opt‑in per C.19).
23. **Variant Emitter.** CharacteristicSpace MUST include a domain‑family coordinate when available from F1‑Card; use HET‑FIRST lens (C.19) before exploit lenses.
24. **ε‑front recorded.** Any front computation **records ε and DHCMethodRef.edition**, and **returns sets** (Pareto/Archive) under lawful partial orders; **no forced scalarisation**.
25. **OEE branch legality.** When a **Task/Environment GeneratorFamily (POET‑class)** is used, publish `EnvironmentValidityRegion`, `TransferRules`, and the dedicated **SoS‑LOG/Acceptance** branches; **telemetry logs edition‑aware Illumination increases with Φ policy‑id**.
26. **MOO (method of obtaining output) surfaced (generator).** Any emission of a **VariantPool** or shortlist **set** **MUST** name its **generation mechanism**: cite **EmitterPolicyRef** (and, where applicable, **InsertionPolicyRef/DHCMethodRef**) and record the active **E/E‑LOG policy‑id** in **SCR** and telemetry. (No file formats mandated; Core remains notationally independent.)

### 9) Consequences (informative)

* **Generativity with guard‑rails:** wide variant search **and** computable trust.
* **Local first, portable later:** clear Context‑local semantics with **explicit Bridges** (CL) for crossing.
* **Direct line to F:** outputs are *immediately usable* in F.17 UTS & F.18 naming; no translation pass.

### 10) Worked micro‑sketch 

**CG-Frame:** Multi‑criteria Decisions in R\&D

* **M1:** `CG-FrameContext=R&D_Decisions_2026` (Γ‑fold default = weakest‑link for safety; mean for cost where interval/ratio scales allow; CL≥2 for cross‑Context reuse).
* **M2:** Harvest outranking, value models, portfolio fronts → SoTA_Set + UTS stubs.
* **M3:** Emit variants under constraints (budget, risk, hiring cap) via **NQD (d≥2)**; record **IlluminationSummary** and **DescriptorMapRef/DHCMethodRef.edition**; score by Creativity‑CHR and QD‑triad.
* **M4:** Select with acceptance clauses (must meet safety reqs; cost within envelope) using an **ε‑Pareto/Archive** set (no scalarisation) + ⟨F,G,**R_eff**⟩; **emit DRR + SCR** with **ε/DHCMethodRef.edition**.
* **M5:** Publish RoleDesc templates (`DecisionRole`, `EvaluatorRole`), Concept‑Set rows for “Alternative/Option”, and UTS rows with **local names**.
* **M6:** Version `VEK‑Pkg@R&D` with refresh every quarter; decay old evidence after 12 months.

### 11) Relations (wiring map)

* **Builds on:* A.4 (time split), A.10 (evidence), B.3 (assurance), B.5.2.1 (creative abduction), F.1–F.3 (Contexts/lexicon), F.7/F.8 (Concept‑Sets; mint/reuse).
* **Imports:** C.17 (Creativity‑CHR), C.18 (NQD‑CAL), C.19 (E/E‑LOG), C.16 (MM‑CHR).
* **Publishes to:* F.4 (RoleAssignment), **F.15 (RSCR)**, F.17 (UTS), F.18 (naming), optional Bridges (F.9).

### 12) Author’s checklist (how to use the skeleton)

* Fill **M1–M6 slots** with the minimal cards (one page each).
* Keep **names local**; propose cross‑Context Bridges only after the local UTS is stable.
* Treat **Julia‑style specialisation** as a *design idiom* (parametric variant families), not as tooling; keep lenses/policies recorded (EmitterPolicyRef; lens id).
* Commit every major decision into a **DRR** entry; wire outputs to **F‑artifacts** immediately.

## G.2 — **SoTA Harvester & Synthesis**   \[A]

> **Purpose.** Provide a rigorous, repeatable way to **discover**, **triage**, and **synthesize** state‑of‑the‑art (SoTA) across competing Traditions before we mint any CHR/CAL/LOG for a CG-Frame. The output is a **SoTA Synthesis Pack** that feeds naming (UTS), formalisation (CHR/CAL), and the algorithmic dispatcher (G.5).
> **Also outputs:** (i) **SoS‑indicator families** (as MethodFamily variants, not single metrics), and (ii) candidate **GeneratorFamily** bundles for open‑ended task/environment generation (QD/OEE class).
> **Form.** Architectural pattern with a conformance checklist, aligned to FPF’s pattern grammar and publication Standard.
> **Guardrail.** No forced scalarisation: downstream selectors (G.5) operate with partial orders and may return Pareto sets/archives, not single winners.

### 1) Problem frame

Teams are extending FPF into a new **CG-Frame** (e.g., creativity, decision theory, evolutionary/hyper‑holonic architecture). The literature is **plural and contested** (ordinal vs cardinal utility; evidential vs causal decision theories; active inference vs classical control; quantum‑like cognition, etc.). We need a **discipline** that captures this plurality without collapsing meaning across Contexts, and that yields artifacts other G‑patterns can consume. **In all normative text below, “Tradition” refers to the Tech token `Tradition` (Plain “Tradition” allowed only as a 1:1 synonym).**

### 2) Problem

How to **systematically** assemble a *complete‑enough* SoTA view that:

* respects **bounded contexts** and **bridges** (no global meaning leaks);
* records **evidence & trust** attributes suitable for later calculus;
* identifies **incompatible commitments** and **points of translation loss**;
* produces **actionable payloads** (names, claims, operators, exemplars) ready for CHR/CAL/LOG authoring and later **multi‑method dispatch** (G.5).

### 3) Forces (tensions you must balance)

* **Pluralism vs. comparability.** Rival Traditions speak different dialects; we must compare **without** flattening their semantics (use Bridges with CL and loss notes).
* **Breadth vs. depth.** Coverage must be wide across sub‑fields yet deep on the load‑bearing claims.
* **Recency vs. stability.** Post‑2015 advances matter, but we need durable claims and exemplars (record freshness windows; edition every distance/metric).
* **Exploration vs. exploitation.** Illumination/QD (diversity‑seeking) vs. best‑response optimisation; keep policies separate and publish which stance a synthesis adopts.
* **Formalism vs. pedagogy.** Early outputs must be teachable and auditable (UTS + Name Cards).
* **Design‑time vs. run‑time.** Keep modeling commitments separate from operational policies and proofs; record the DesignRunTag explicitly.

### 4) Solution (the harvesting & synthesis loop)

#### 4.1 Discovery funnel (iterate until saturation)

* **Seed → Expand → Prune.** Start with canonical surveys & top venues (post‑2015); expand via forward/backward citation and method keywords; prune with *CG-Frame‑fit* and *load‑bearing* tests (does this claim change how we would model/decide?). Maintain a **PRISMA‑style flow** (identification→screening→eligibility→included) in the pack’s provenance.
* **Contexting.** Assign each artifact to a **home Context** (Bounded Context + edition). If cross‑Context reuse is needed, draft a **Bridge** and a **CL** with a human‑legible *loss/fit* note.

Gate@M2‑exit: if FamilyCoverage < k (default k=3 for triad/“universal” claims; otherwise per lens policy and recorded in provenance) or MinInterFamilyDistance < δ_family (per F1‑Card edition) → expand search window/policies and rerun harvesting. **MUST record** `k`, the **F1‑Card id+edition**, and the `DistanceDefRef.edition` in `SoTA_Set` provenance.

**SoS‑indicators.** Where the literature offers Science-of-Science disciplinary indicators (replication, standardisation, disruptive balance, alignment) treat each as a **MethodFamily** with variants (calculation windows/constraints), not as a single scalar; record Acceptance branches for each variant.

#### 4.2 Claim distillation (per lineage/`Tradition`)
* For each Tradition, extract a **Claim Sheet** (minimal, typed statements) with **F‑ratings**, **G‑scope cues**, and **R‑Evidence Graph Ref** **tagged with KD‑CAL lanes (TA/VA/LA)**, plus **describedEntity** (`GroundingHolon`) and **ReferencePlane ∈ {world, concept, episteme}**; **Domain mentions stitched to D.CTX + UTS** (catalog‑only); include a stub **referenceMap** (observable cues → prospective CHR). Record **freshness windows** and the **edition** of any metric/distance used.

#### 4.3 Operator & object inventory

* Enumerate **characterisation candidates** (Characteristics, Scales, Levels, Coordinates) and **operators** the Tradition needs. Park all measurement terms under **MM‑CHR** discipline (no ordinal arithmetic; declare polarity; unit coherence).
* Identify **decision objects** (options, lotteries, policies), **evidence objects** (observations, proofs), and **search objects** (frontiers, VOI heuristics) to be handed to CHR/CAL/LOG later.
* Compile **MethodFamily candidates** (common signature → multiple implementations) with `ValidityRegion`, `CostModel`, `Guarantees`, `KnownFailures`.
* If the Tradition includes task/environment generation, compile **GeneratorFamily candidates** (OEE/QD class; **POET/Enhanced‑POET‑like**) with `EnvironmentValidityRegion`, `TransferRules`, and **SoS‑LOG**/**Acceptance** branches to govern when transfers/migrations are legal.

#### 4.4 Alignment & divergence map

* Build a **Bridge Matrix**: `Tradition`×`Tradition` with where alignment is possible, **CL** and explicit **loss**; **note that CL penalties route to R_eff only (F and G invariant)**. Publish the **`DistanceDefRef.edition`** used to compute inter‑family distances.

#### 4.5 Didactic micro‑grounding & describedEntity anchoring

*For every load‑bearing claim, attach two micro‑examples …* **and link each micro‑example to carriers (A.10)** to serve as minimal anchors for future **CG‑Frame** characteristics and CHR cards.

#### 4.6 Publication surface (SoTA Synthesis Pack)

* **UTS delta.** Proposed **Name Cards** (Unified Tech / Plain) **with twin labels** (per F.17–F.18), Context, MDS, sense anchor, alignment/Bridges, lifecycle = *Draft*; **no new conceptual prefix without E.10 (LEX) and a DRR citation**; **use registered Γ‑fold family** (do not re‑use Γ for gauges).
* **ReferencePlane** is published per row; on any crossing compute and record **CL^plane**; penalties **route to R_eff only** (never F/G).
* **SoTA Tables.** Side‑by‑side claim sheets, operator lists, exemplar pointers, and **SoS‑indicator families** per Tradition/Context.
**NQD/Illumination annex (if applicable).** For any QD‑style family, publish **Q/D/QD‑score** definitions, the **IlluminationSummary** (as a gauge over Diversity_P), its **edition id**, and the **policies** used: `DescriptorMapRef.edition`, **`DHCMethodRef.edition`**, **`DistanceDefRef.edition`**, `EmitterPolicyRef`, and **`InsertionPolicyRef`** (archive dedup/elite replacement/`K`‑capacity). By default, **Illumination** does **not** enter dominance unless enabled by an explicit **CAL.Acceptance** policy.

* **Risk & trust notes.** Where translation exists, log **CL penalties** and evidence fragility for later **R** aggregation; on any plane crossing publish the **Φ_plane policy‑id** alongside `CL^plane`.

Required artifact for top‑level disciplines: **SoTAPaletteDescription (D)**, accompanied by CHR evidence (G.3) and CAL traces (G.4). The SoTA Synthesis Pack MUST include: (i) claim sheets, (ii) operator & object inventory, (iii) bridge matrix (CL with loss notes), (iv) worked micro‑examples, (v) UTS drafts, **(vi) PRISMA‑style flow record, (vii) SoS‑indicator families, and (viii) where relevant, QD/OEE annex with Illumination/Policy fields**. This Description precedes any CG‑Spec normalization.

 **G.2‑F (Γ_epist Synthesis Step).** For any cross‑source consolidation, produce a **`Γ_epist^synth`** with:
(i) **Provenance union** (no source loss),
(ii) **Object alignment** (LCA or **`CompositeEntity`** with explicit mappings),
(iii) **Assurance tuple = WLNK(…; Φ(CL), Φ_plane)** with **monotone, bounded, table‑backed** Φ‑policies; **publish policy‑ids in SCR** (including any **Illumination‑policy id**) and document them in **CG‑Spec**, (iv) **Conflict handling**: **no averaging** across rival planes/scales; preserve disjoint claims with Bridges + **loss notes**,
(v) **ReferencePlane per row**; **compute CL^plane** on crossings; **penalties → R_eff only**; **emit SCR** for each synthesis result.

 **G.2‑G (DHC hooks, C.21).** For each Tradition×Context, emit **DHC‑SenseCells** (UTS ids) and declare units for
**AlignmentDensity = `bridges_per_100_DHC_SenseCells`**; count only Bridges with **CL ≥ 2**; interpret **CL=3** as *free substitution*, **CL=2** as *guarded* (loss notes attached). Publish **freshness windows** and the **edition** of all DHC series, including the **DistanceDefRef.edition** wherever distances are used.

 Head‑anchoring + I/D/S; Plain twins present; tier crossings recorded (**Bridge + UTS** with **CL/CL^plane**); Domain mentions stitched to **D.CTX + UTS**.
**See §7 Conformance for the normative guard set (pluralism floor; Bridge+CL with loss notes; lane tags; RSCR hooks; ReferencePlane & CL^plane; penalties → R only).** This avoids duplication and drift.

### 5) Payload (what this pattern *exports*)

1. **SoTA Synthesis Pack** for the CG-Frame (folder):
* **G.2a** *Corpus Ledger*: bib entries + Context/edition + quick verdict (keep/park/retire).
* **G.2b** *Claim Sheets* (per Tradition) with F/G/R annotations and freshness windows.
* **G.2c** *Operator & Object Inventory* (candidate CHR terms; CAL hooks).
* **G.2d** *Bridge Matrix* with CL & loss notes.
* **G.2e** *Micro‑examples* (1‑pagers).
* **G.2f** *UTS Proposals* (Name Cards + proposed rows/aliases).
* **G.2g** *describedEntity Map*: per Tradition, a table `{term → GroundingHolon, ReferencePlane, referenceMap stubs}`.
* **G.2h** *PRISMA Flow Record* (identification→screening→eligibility→included).
* **G.2i** *SoS‑Indicator Families* (variants, constraints, Acceptance branches).
* **G.2j** *MethodFamily Cards* (signature, ValidityRegion, CostModel, Guarantees, KnownFailures, EvidenceRefs).
* **G.2k** *GeneratorFamily Cards* (OEE/QD class; EnvironmentValidityRegion; TransferRules; SoS‑LOG/Acceptance hooks).
* **G.2l** *(If applicable) NQD Annex*: Q/D/QD‑score definitions; **IlluminationSummary** (+ **edition id**); `EmitterPolicyRef`; `InsertionPolicyRef`; `DistanceDefRef.edition`.

1. **Hand‑off manifests** to:
* **G.3/G.4** (CHR authoring and CAL scoping) with the operator/object inventory;
* **G.5** (Dispatcher) with a **Method Family Index** per Tradition (candidate LOG bundles) **aligned to the Registry fields (Eligibility predicates, Assurance profile, CL notes)**, plus (where relevant) **GeneratorFamily** entries and **Illumination/Policy metadata** for QD families.

### 6) Interfaces & dependencies

* **Consumes:** CG-Frame Charter (G.1), naming rules & UTS protocol (F.17), measurement discipline (A.17–A.19), **Bridges & CL (F.9) with Trust (B.3)** + CAL evidence hooks.
* **(May also consume)** **G.13 `ClaimSheet@Context`/`SoSFeatureSet@Context`/`InteropSurface@Context`** when external scholarly indexes are mapped via conceptual interop; Core semantics unchanged.
* **Produces:** Draft **\[D]** terms for **G.2 → G.3**; operator stubs for **CAL** in **G.4**; initial **LOG** families for **G.5**; **SoS‑indicator families**; and, where applicable, **GeneratorFamily** bundles and **NQD/Illumination** metadata.

### 7) Conformance Checklist (author must be able to tick “yes”)

* **Pluralism floor.** ≥ 2 `Tradition` and ≥ 3 `U.BoundedContext` present.
* **Contexts declared.** Every artifact has a **home Context**; cross‑Context reuse uses a **Bridge** with **CL** and a **loss note**.  **ReferencePlane on crossings; CL→R only** with loss notes.
* **Rival Traditions kept disjoint.** No fused claims without an explicit alignment proof or Bridge. 
* **Measurement lawful.** All proposed characteristics/scales honour MM‑CHR guards (no illegal ordinal arithmetic; unit coherence; declared polarity). 
* **Hand‑offs produced.** CHR/CAL/LOG manifests exist and reference the SoTA pack components. 
* **describedEntity declared.** Each Claim Sheet states `GroundingHolon` and `ReferencePlane`; micro‑examples cite carriers (A.10).
* **Didactic grounding.** Each load‑bearing claim has **two worked micro‑examples** (heterogeneous substrates) and **A.10 anchors** with lane tags (**TA/VA/LA**).
* **UTS‑ready.** Each candidate term has a **Name Card** draft **with twin labels** (F.17–F.18), Context, MDS, concept‑set linkage (or rationale for “not applicable”).
* **DHC hooks present.** DHC‑SenseCells are emitted; **AlignmentDensity** units declared; **freshness windows + edition** stated (C.21).
* **PRISMA present.** The SoTA pack includes a PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) style flow record.
* **SoS‑indicators as families.** Indicators are represented as MethodFamily variants with Acceptance branches; no single unqualified scalar.
* **QD/OEE readiness (if applicable).** NQD annex includes Q/D/QD‑score defs, **IlluminationSummary** (edition), `EmitterPolicyRef`, `InsertionPolicyRef`, and **policy‑id**; dominance does not include Illumination unless enabled by E/E‑LOG.

* **DomainDiversity Guarantee.** If FamilyCoverage < k OR MinInterFamilyDistance < δ_family (F1‑Card), expand search radius under E/E‑LOG and re‑harvest; log policy id in SCR.

### 8) Anti‑patterns & rewrites (what to avoid, what to do instead)

* **“Global definition” temptation.** *Don’t:* collapse causal, evidential, and thermodynamic decision theories into one utility function. *Do:* keep **parallel claim sheets** and map **where** and **why** they diverge; attach **Bridges** with CL.
* **Ordinal arithmetic creep.** *Don’t:* average Likert‑style scores across studies. *Do:* treat as ordinal; use order‑safe summaries, or justify interval mapping via MM‑CHR evidence.
* **Design/run blur.** *Don’t:* treat policy heuristics as proven laws. *Do:* DesignRunTagtance, and route proofs/policies to the proper lanes.

### 9) Consequences

* **Comparable plurality.** Teams can hold multiple Traditions in view, compare them **safely**, and trace translation risk via CL.
* **Frictionless downstream work.** CHR/CAL/LOG authors receive **well‑shaped inputs**; UTS publication stays disciplined.
* **Pedagogical leverage.** Micro‑examples and Name Cards make the synthesis teachable and auditable.

### 10) Worked micro‑example (1 paragraph, indicative only)

*CG-Frame:* Decision theory. *Traditions:* (i) **Classical expected‑utility** (ordinal vs cardinal utility variants); (ii) **Causal decision theory**; (iii) **Quantum‑like cognitive models**; (iv) **Active‑inference thermodynamic stance**.
*Moves:* Each Tradition gets a **Claim Sheet** (e.g., choice rule, independence/separability, belief update), **Operator Inventory** (e.g., utility/likelihood/variational free energy), **Bridge Matrix** entries (*e.g.*, CDT ↔ EDT misalign on counterfactual conditioning; CL=2; *loss:* evidential dependence), two **micro‑examples** (manufacturing escalation vs human‑choice vignette), and **UTS proposals** for contested terms (`U.DecisionPolicy`, `U.PreferenceOrder`, `U.FreeEnergyBound`). If illumination is relevant (e.g., exploring diverse policy classes), include an **NQD annex** (Q/D/QD‑score defs, IlluminationSummary w/ edition, Emitter/Insertion policies). (Downstream: G.3 authors CHR for *Decision Object/Profile/Policy*; G.4 authors CAL variants; G.5 registers **MethodFamily/GeneratorFamily** entries.)

### 11) Editorial template (1‑page “SoTA Sheet” per Tradition)

* **Context & edition** · **Core claims** (typed; intended **F**) · **Objects & operators** · **Measurement stance** (MM‑CHR notes) · **Evidence stance** (what counts; typical *R* anchors; freshness window) · **Micro‑examples** · **Known bridges** (targets; CL; loss notes) · **Citations (≥2015)** · **UTS candidates** (Name Card ids) · *(if relevant)* **SoS‑indicator family variants** · *(if relevant)* **NQD fields** (Q/D/QD‑score defs; IlluminationSummary edition; Emitter/Insertion policy refs).

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

## G.8 — **SoS‑LOG Bundles & Maturity Ladders** \[A]

**Stage:** *design‑time packaging* (authoring & publication) with a *run‑time* consumer facade for **G.5** (selector/registry).
**Primary hooks:** **C.23** (Method‑SoS‑LOG), **G.4** (Acceptance & EvidenceProfiles), **G.6** (EvidenceGraph & PathId/PathSlice), **G.5** (Registry/Selector), **C.22** (TaskSignature S2), **C.18** (NQD‑CAL), **C.19** (E/E‑LOG), **F.9** (Bridges & CL), **G.7** (Bridge Matrix & CL calibration), **E.11** (ATS AH‑1..AH‑4), **E.5.2** (Notational Independence), **E.10** (LEX twin registers).
**Why this exists.** Families of methods compete inside a CG‑Frame; the selector must *admit, degrade,* or *abstain* per family without illicit scalarisation and with auditable provenance. This pattern **packages** the rule sets and maturity description defined elsewhere, so G.5 can lawfully dispatch portfolios/archives while keeping thresholds in **Acceptance** and justifications in **EvidenceGraph** paths. **It does not redefine SoS‑LOG semantics** (see **C.23**).
**Modularity note.** The bundle cleanly separates **LOG decisions** (C.23) from **Acceptance thresholds** (G.4), **evidence wiring** (G.6), **selection semantics** (G.5), and **refresh/decay** (G.11); each module evolves independently under **E.11** harness gates. 

### 1) Intent

Bind **C.23 SoS‑LOG** rule sets and a **maturity ladder (ordinal poset)** into a selector‑facing, **notation‑independent** bundle that: (i) **exposes** the decisions produced by C.23 rules, (ii) wires **EvidenceGraph** citations and ATS hooks, and (iii) exports edition‑aware telemetry for **Illumination (QD)** and **Open‑Ended** generator families—without embedding thresholds inside LOG (thresholds live only in **G.4 AcceptanceClauses**).

### 2) Problem frame

Unstructured readiness stories and prose‑only gates cannot be executed by **G.5**; cross‑Context reuse often lacks Bridges/CL and plane penalties, and QD/OEE signals are mixed into dominance unlawfully. We need a **bundle** that a) keeps **maturity** visible but **non‑scalar**, b) cites lawful paths in **EvidenceGraph** for every LOG decision, and c) exports **DominanceRegime**/**PortfolioMode** so the selector can **return sets** (Pareto/Archive) rather than forcing scalarisation.   

### 3) Forces

* **Pluralism vs. dispatchability.** Competing Traditions must be comparable without semantic flattening. 
* **Assurance vs. results.** Assurance lanes (TA/VA/LA) must not crowd out **method generation**; *degrade* branches should enable safe exploration under **E/E‑LOG** budgets. 
* **No‑Free‑Lunch.** Selection must return **sets** under partial orders; **Illumination** is a **gauge** by default.  
* **Edition‑awareness.** QD/OEE surfaces require pinned **`…Ref.edition`** and **policy‑id** for refresh/RSCR. 

### 4) Solution — *Bundle the LOG; publish the Ladder; keep thresholds in Acceptance*

#### 4.1 Objects (LEX heads; twin‑register discipline)

**`SoS‑LOG.Rule`** — executable rule schema `{Admit | Degrade(mode) | Abstain}` for `(TaskSignature, MethodFamily)`; authored per **C.23** (this pattern does not redefine rule semantics).
* **`MethodFamily.MaturityCardDescription@Context`** — an **ordinal** (closed enum) ladder with declared **ReferencePlane**; *no thresholds inside*. 
* **`SoS‑LOGBundle@Context`** — the **selector‑facing** package defined in §4.2.
* **Naming discipline.** Do **not** alias **Spaces** and **Maps**. **Tech = `U.DescriptorMapRef` (d≥2); Plain‑twin = `CharacteristicSpaceRef`** (per CC‑G5.22). Editions live on **Refs** (e.g., `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `CharacteristicSpaceRef.edition` when pinning a historical Space phase).
* **Twin registers.** Tech labels are normative; Plain twins are didactic only and must not cross Kinds.

#### 4.2 Bundle schema (conceptual; notationally independent)

```
SoS-LOGBundle@Context :=
⟨ BundleId (UTS), MethodFamilyId, HomeContext,
  RuleIds[],                      // C.23 rules (Admit/Degrade/Abstain)
  MaturityCardDescription,        // closed enum; ordinal; ReferencePlane declared
  ClosedEnums: {DegradeModeEnum, MaturityRungs}, // UTS-registered
  DominanceRegime, PortfolioMode, // default DominanceRegime=ParetoOnly
  BridgeIds[], ΦPolicyIds[],      // CL/CL^plane policies cited by id
  A10EvidenceGraphRef?[],          // OPTIONAL at packaging time: A.10 carriers (lanes + freshness windows) for G.6 resolution
  EvidenceGraphPathIds?[],        // MAY be included when stable PathIds exist (e.g., rung justifications);
                                  // branch‑specific PathIds are recorded at run‑time in SCR per C.23/H4
  // Acceptance thresholds live in G.4; selector cites clause ids from CAL at run‑time (no duplication here)

  QD/OEE: {CharacteristicSpaceRef, CharacteristicSpaceRef.edition?,
           DescriptorMapRef.edition,
           DistanceDefRef.edition, EmitterPolicyRef, InsertionPolicyRef}?,
  OEE?: {EnvironmentValidityRegion, TransferRulesRef.edition}?,
  AuthoringMethodDescriptionRefs?[], // OPTIONAL: cite MethodDescription/Spec ids (with editions) of methods that materially shaped rules/ladder (SoTA-of-description traceability across ATS tiers)
  Edition, Notes ⟩
```

*Default.* `DominanceRegime = ParetoOnly`; **Illumination/coverage** are gauges that **do not** affect dominance unless an explicit **CAL** policy states otherwise (*policy‑id appears in SCR*). **Ψ(CL^k)**, where used for kind‑bridges, is cited by id alongside Φ.

#### 4.3 Admissibility Ledger (selector‑facing export)

Publish an **`AdmissibilityLedger@Context`** with rows
`(MethodFamilyId, RuleId, MaturityRung, BranchIds, BridgeIds, ΦPolicyIds, EvidenceGraphPathIds?, DominanceRegime, PortfolioMode, Edition)` — **UTS‑registered** and consumed by **G.5**. The selector **cites** Acceptance clause/rung ids from CAL/C.23 and does **not** recompute thresholds.

#### 4.4 Binding obligations (packaging‑only; refer to **C.23 R0–R8** for rule semantics)

* **B1 — Evidence wiring.** At packaging time, provide **A.10 Evidence Graph Ref** (lanes + freshness windows) that back the C.23 rules; where already minted, **MAY** include stable **`EvidenceGraph PathId`(s)** (e.g., rung justifications). **Branch‑specific PathIds are recorded at run‑time in SCR** per **C.23/H4**.
* **B2 — CL/plane routing.** Cross‑Context/plane reuse in the bundle **MUST** cite **Bridge ids** and the applicable **Φ(CL)**/**Φ_plane** policy‑ids; penalties route to **`R_eff` only**; **F/G invariant**.
* **B3 — QD portfolio fields.** If `PortfolioMode=Archive`, the bundle **MUST** pin `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `EmitterPolicyRef`, and `InsertionPolicyRef`; **IlluminationSummary** is a **gauge** and is excluded from dominance unless CAL promotes it (policy‑id recorded).
* **B4 — Open‑ended fields.** If `GeneratorIntent` applies, the bundle **MUST** carry `EnvironmentValidityRegion` and `TransferRulesRef.edition`; selector outputs are `{environment, method}` portfolios; coverage/regret are **gauges**.
* **B5 — Telemetry hooks.** On any illumination increase/archive change, telemetry **SHALL** log `PathSliceId`, the active **policy‑id**, and the editions of `DescriptorMapRef`/`DistanceDefRef`; in OEE also `TransferRulesRef.edition`. (Feeds **G.11** refresh; aligns with **C.23 R8**.)

#### 4.5 Maturity ladder (poset, not a scalar; Description, not Spec)

Publish **`MethodFamily.MaturityCardDescription@Context`** (UTS twin labels; **Scale kind=ordinal**; **ReferencePlane declared**). Do **not** embed thresholds. **Rung semantics live in C.23**; this pattern only **binds** the card into the bundle and requires UTS publication and **EvidenceGraph** justification for rung transitions.

### 5) Interfaces — minimal I/O standard (conceptual)

| Interface                               | Consumes                                                                               | Produces                                                             |
| --------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **G.8‑1 `Publish_LOGBundle`**           | `MethodFamily`, C.23 rules, G.4 Acceptance, Bridges/Φ policies, (optional) QD/OEE refs | `SoS‑LOGBundle@Context` (UTS row)                                    |
| **G.8‑2 `Publish_AdmissibilityLedger`** | Bundle + per‑rule branch records (with A.10 anchors; PathIds if available)            | `AdmissibilityLedger@Context` (UTS row)                              |
| **G.8‑3 `Publish_MaturityCard`**        | Ladder description + EvidenceGraph PathIds for rung justification                      | `MaturityCardDescription@Context` (UTS row; editioned)               |
| **G.8‑4 `Expose_TelemetryHooks`**       | Archive/illumination/OEE signals                                                       | `PathSliceId`, `…Ref.edition`, **policy‑id** for RSCR/refresh (G.11) |

*Note.* Surfaces are **conceptual only** per **E.5.2**; actual serializations (e.g., RO‑Crate) belong in **G.10 / Annex**. 

### 6) Conformance Checklist (CC‑G8)

* **CC‑G8‑1 (No thresholds in LOG).** Any maturity floor or numeric gate **SHALL** be authored as a **G.4 AcceptanceClause** and cited by id from the LOG; **LOG never embeds thresholds**. 
* **CC‑G8‑2 (Tri‑state discipline).** Unknowns **MUST** map to an explicit LOG branch (`Degrade` or `Abstain`); `sandbox/probe‑only` is a **LOG branch** with an **E/E‑LOG policy‑id**. 
* **CC‑G8‑3 (Path citation).** Every `Admit/Degrade/Abstain` **MUST** cite **EvidenceGraph PathId(s)** at run‑time when G.6 is present (per C.23/H4). **At packaging time**, the Bundle/Ledger **SHALL** provide **A.10 Evidence Graph Ref** and **MAY** include stable **PathId(s)** where available.* **CC‑G8‑4 (Bridge & plane penalties).** Crossings **MUST** cite **Bridge ids** and **Φ(CL)**/**Φ_plane** policy‑ids; **penalties reduce `R_eff` only**; **F/G invariant**. 
* **CC‑G8‑5 (Dominance defaults).** **Default** `DominanceRegime = ParetoOnly`; inclusion of **Illumination** in dominance **requires** an explicit CAL policy with **policy‑id recorded in SCR**. 
* **CC‑G8‑6 (QD/OEE edition discipline).** When QD/OEE are active, bundles **MUST** pin **`U.DescriptorMapRef.edition`**, `DistanceDefRef.edition`, `EmitterPolicyRef`/`InsertionPolicyRef`, and (for OEE) `TransferRulesRef.edition`. **`CharacteristicSpaceRef.edition` SHALL be pinned whenever grid/cell boundaries or de‑duplication rules affect parity/selection;** otherwise it MAY be omitted from packaging, but **telemetry MUST still record it when QD is in scope**. Any illumination increase **MUST** log `PathSliceId` + **policy‑id**. `CharacteristicSpaceRef.edition` **MUST NOT** be used as a substitute for `DescriptorMapRef.edition`.
* **CC‑G8‑7 (Maturity = ordinal).** Ladders **SHALL** declare **Scale kind=ordinal** and closed rungs; rung transitions **MUST** be justified by EvidenceGraph paths and published to UTS. 
* **CC‑G8‑8 (Spaces ≠ Maps).** Do not alias `CharacteristicSpace` and `DescriptorMap`; use **Tech** heads with editions on **Refs** only; obey twin‑register rules. 
* **CC‑G8‑9 (Notational independence).** Bundles **SHALL** remain tool/format‑neutral (Core semantics only). 
* **CC‑G8‑10 (MOO cross‑reference).** Method of obtaining outputs: when the LOG bundle is consumed to emit selector **sets**, the producing step **SHALL** surface the **generation/parity mechanism** id (e.g., **ParityHarnessId** under G.9) and the controlling **policy‑id** in **SCR** and telemetry. (Packaging remains conceptual per **E.5.2**.)
* **CC‑G8‑11 (SoTA‑of‑description trace).** If any authoring methods (e.g., discovery, clustering, summarisation) materially influenced rule text or ladder rungs, **cite their `AuthoringMethodDescriptionRefs` with editions**. This supports ATS‑tier SoTA tracking of the *methods that describe methods* without adding tool lock‑in (E.5.2).

### 7) Archetypal grounding (informative, SoTA‑oriented)

**Show‑A · Decision‑making (selector returns a set).**
*S2 excerpt.* `TaskKind=multi‑criteria; Orders=partial; PortfolioMode=Pareto`.
*Families.* Outranking/MCDA, Causal (SCM), Offline‑RL/Decision‑Transformer, Bayesian Optimisation (risk‑aware).
*Bundle.* `SoS‑LOG` cites **PathIds** for replication/legality; **MaturityFloor** enforced via **AcceptanceClause** `AC_MaturityFloor(≥L2)`; selector returns a **Pareto set**, no cross‑ordinal averaging.  

**Show‑B · QD archive (policy search, MAP‑Elites‑class).**
*S2 excerpt.* `PortfolioMode=Archive; CharacteristicSpaceRef(d=2); ArchiveConfig(K=1, CVT, DistanceDefRef.edition=v2); EmitterPolicyRef=v3; DominanceRegime=ParetoOnly`.
*Bundle.* `Admit` returns an **archive**; **IlluminationSummary** (Q/D/QD‑score) is reported; editions and **policy‑id** are pinned for refresh. Contemporary QD families include **MAP‑Elites (2015)**, **CMA‑ME/MAE (2020–)**, **Differentiable QD/MEGA (2022–)**, **QDax (2024)**. 

**Show‑C · Open‑ended generators (POET‑class; environments + methods).**
*S2 excerpt.* `GeneratorIntent; EnvironmentValidityRegion=EVR‑A; TransferRulesRef=TR‑A`.
*Bundle.* Admits portfolios over `{environment, method}`; unknown `TransferRules` ⇒ `Degrade(scope‑narrow)`; telemetry logs **coverage/regret** and **edition bumps**; SoTA includes **POET (2019)**, **Enhanced‑POET (2020)**, and **Darwin Gödel Machine (2025)**‑class approaches.

> *Didactic note.* These examples reflect the **“single call, many solvers”** idiom and portfolio‑first selection (akin to **DifferentialEquations.jl** and **JuMP** ecosystems), which the **G.5** registry expects. 

### 8) Relations

**Builds on:** **C.23** (SoS‑LOG), **G.4** (Acceptance), **G.6** (EvidenceGraph, PathId), **C.22** (TaskSignature S2), **F.9** (Bridges & CL), **G.7** (Bridge Matrix & CL calibration), **C.18/C.19** (QD/E‑E), **E.11** (ATS harness).
**Publishes to:** **G.5** (selector/registry), **UTS** (bundle, ladder, ledger), **G.11** (refresh via PathSlice & editions).  
**Constrains:** Any LOG implementation that claims FPF conformance; **default dominance** and **tri‑state** behavior must match **G.5** semantics. 

### 9) Bias‑Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**.
Scope: **Core‑wide**; ordinal scales are never averaged; **Illumination** stays a gauge unless explicitly promoted by policy (id cited).  

### 10) Author’s quick checklist

1. Compile **RuleIds[]** with tri‑state handling and **PathId** citations; run AH‑1..AH‑4. 
2. Describe the **MaturityCard** (ordinal; closed enum; ReferencePlane declared); **do not** embed thresholds. 
3. Register **Φ(CL)**/**Φ_plane** policies (ids only); ensure penalties route to **R_eff** only. 
4. If QD/OEE is active, pin **editions** (`DescriptorMapRef`/`DistanceDefRef`/`TransferRulesRef`) and expose **PathSliceId** for refresh. 
5. Publish **SoS‑LOGBundle** and **AdmissibilityLedger** to **UTS** (twin labels; editioned). 
6. Declare `DominanceRegime`/`PortfolioMode`; **default = ParetoOnly**; if Illumination is promoted into dominance, cite the **CAL policy id**.

## G.9 — **Parity / Benchmark Harness** \[A]

**Tag:** [A] **Stage:** design‑time planning **+** run‑time execution (selector‑adjacent)
**Primary hooks:** **G.5** (selector & portfolios), **G.6** (EvidenceGraph, PathId/PathSlice), **G.4** (Acceptance & CAL predicates), **C.23** (SoS‑LOG branches & maturity), **C.22** (TaskSignature S2), **C.18/C.19** (QD & E/E‑LOG policies), **G.7** (Bridge Matrix & CL calibration, BCT/Sentinels), **F.15** (RSCR parity/regression), **F.9** (Bridges & CL), **E.11** (ATS AH‑1..AH‑4), **E.5.2** (Notation‑independence).
**Why this exists.** Rival **MethodFamilies/Traditions** are often “benchmarked” under different freshness windows, editions, or via illegal scalarisations; results cannot be lawfully compared or reproduced. **G.9** provides a *method of obtaining outputs*: a **parity plan + execution harness** that produces a **ParityReport@Context** consumable by **G.5**, with apples‑to‑apples baselines, lawful orders (often partial), and **PathId‑cited** provenance. Illumination/coverage and regret are exposed as **gauges** and **excluded from dominance by default**; any promotion into dominance must be explicit in CAL policy and cited by id. Parity pins are **edition‑aware** and **bridge/plane‑aware** by construction.
**Modularity note.** G.9 does **not** redefine SoS‑LOG or Acceptance; it **binds** them into a parity plan, calls the **G.5** selector in set‑returning mode, and **publishes** evidence per **G.6** with ATS visibility. Thresholds remain in **G.4**; LOG semantics remain in **C.23**.  

### 1) Intent

Provide a **notation‑independent** harness that designs and executes **lawful, edition‑aware** parity runs **across families/traditions**—with equal **freshness windows**, **editions**, **budgets**, and **Bridge/CL/CL^plane routing**—so that **G.5** can select **sets** (Pareto/Archive) without illicit scalarisation. Parity outputs are published as **`ParityReport@Context`** with **EvidenceGraph PathIds** and **CAL policy‑ids** for any non‑default dominance behaviour.

When Characteristics live on different scales/units or spaces, parity **MUST** use **gauge‑based comparability** (“map, then compare”) before any numeric comparison, per the CG‑Spec/MM‑CHR legality.

### 2) Problem frame

Benchmarks routinely compare unlike with unlike: different dataset editions, metric definitions, or QD grids; ordinal measures get averaged; illumination is mixed into dominance. Cross‑Context reuse skips **Bridges** and **CL penalties**. G.9 cures this by fixing a **BaselineSet**, **FreshnessWindows**, and a **ComparatorSet** bound to **CG‑Spec** characteristics and editions, then **driving** the selector to return **sets** under admissible orders and **publishing** legally interpretable results.  

### 3) Forces

* **Pluralism vs comparability.** Rival traditions must be comparable **without** semantic collapse; comparisons cross **Bridges**, incur **CL→R** penalties only. 
* **Partial orders vs totals.** Many targets remain **partially ordered**; the harness must not force totals; **return sets**. 
* **Edition‑awareness.** QD/OEE outcomes depend on **`DescriptorMapRef.edition`**, **`DistanceDefRef.edition`**, **Emitter/Insertion** policies; parity must *pin* them. 
* **Gauges vs objectives.** **Illumination/coverage & regret** inform health but are **gauges by default**; dominance may only change via CAL policy id. 
* **ATS visibility.** Crossings/gates must be visible to AH‑1..AH‑4; failures block publication. 

### 4) Solution — *Plan parity; execute once; publish sets with path‑cited evidence*

#### 4.1 Objects (LEX heads; twin‑register discipline)

* **`ParityPlan@Context`** — design‑time object that fixes comparison terms:
  `⟨PlanId(UTS), CG‑FrameId, HomeContext, BaselineSet, FreshnessWindows, ComparatorSet(id), Budgeting, ε, BridgeIds[], ΦPolicyIds[], EvidenceGraphRef(A.10), EditionPins, PortfolioMode, DominanceRegime, Notes⟩`.

* **`EditionPins`** (when QD/OEE):
  `⟨DescriptorMapRef.edition, DistanceDefRef.edition, DHCMethodRef.edition, DHCMethodSpecRef.edition, CharacteristicSpaceRef.edition?, EmitterPolicyRef, InsertionPolicyRef, (OEE) TransferRulesRef.edition⟩`.

* **`ComparatorSet`** — a set of **CG‑Spec‑bound** characteristics with declared **Scale kind, units, polarity**, lawful order (≤, ≽, lexicographic, Pareto), **ReferencePlane**, and the **editions used by any measures** (`DHCMethodRef.edition`/**`DHCMethodSpecRef.edition`**, `DistanceDefRef.edition`). **Ordinal averages are forbidden.** Where spaces/scales differ, parity **MUST** declare the **gauge mapping** used to lawfully embed one coordinate space into the other prior to comparison. Any numeric comparison/aggregation **must** be CSLC‑lawful and cite the corresponding CG‑Spec entry.

* **`ParityReport@Context`** — run‑time publication object (below §5).

**Naming discipline.** Heads reuse existing U‑types and LEX rules; **no new “Strategy” U.Type** is minted (policies live in **E/E‑LOG**). Tech/Plain twins follow **E.10**. 

#### 4.2 Parity planning (design‑time; notation‑independent)

1. **Fix the BaselineSet.** Choose **MethodFamilies** (and, if present, **GeneratorFamilies**) to compare; cite **SoS‑LOG bundle ids** and **MaturityCard** rungs for context; thresholds stay in **Acceptance**. Where cross‑Tradition reuse occurs, ensure corresponding **G.7 BridgeCards** and **Calibration Ledger/BCT** entries exist and are referenced by id.
2. **Equalise FreshnessWindows.** Declare **identical** evidence windows for all baselines; record **lanes** (TA/VA/LA) and carriers in **A.10**. 
3. **Pin editions.** Freeze **`DHCMethodRef.edition`/`DHCMethodSpecRef.edition`/`DistanceDefRef.edition`**, `DescriptorMapRef.edition`, and (if applicable) **`CharacteristicSpaceRef.edition`**; pin `EmitterPolicyRef` and `InsertionPolicyRef`; in OEE also **`TransferRulesRef.edition`**. 
4. **Bind ComparatorSet to CG‑Spec.** For every numeric operation, cite **CG‑Spec.Characteristics** and prove **CSLC** legality; attach **ReferencePlane**. Where scales/units/spaces differ, declare the **gauge mapping** used (“map, then compare”) and its lawful scope.
5. **Declare order & portfolio semantics.** **Default** `DominanceRegime = ParetoOnly`; **Illumination** is a **gauge** (report‑only) unless CAL declares `ParetoPlusIllumination` by id; choose `PortfolioMode ∈ {Pareto|Archive}`. If ε‑front thinning is used, declare **`EpsilonDominance (ε≥0)`** explicitly and cite policy/edition where relevant.
6. **Route crossings.** Where Traditions/planes or Kinds differ, require **Bridge ids** and publish **Φ(CL)**/**Φ_plane** (and, where used, **Ψ(CL^k)**) policy‑ids; penalties **reduce R_eff only**; **F/G invariant**. 

#### 4.3 Execution protocol (run‑time; selector‑adjacent)

* **E1 · Gate on legality.** Run **Eligibility → Acceptance** on the shared **S2 TaskSignature**; refuse illegal CHR ops (e.g., ordinal means). 
* **E2 · Call G.5 with parity pins.** Execute **G.5.Select** under the parity **ComparatorSet**/**EditionPins**; **return a set** (Pareto/Archive) when order is non‑total; record **Bridge/Φ/Φ_plane** (and **Ψ**, if kind‑bridges apply) policy‑ids and compute **R_eff** with penalties *to R only*. If gauge mappings were declared, record their ids/notes in SCR and cite the applicable PathIds.
* **E3 · Report gauges.** Publish **IlluminationSummary** (Q/D/QD‑score) and **coverage/regret** **as gauges**; dominance unaffected unless CAL policy id authorises otherwise. 
* **E4 · Cite paths.** Every inclusion/exclusion decision **cites EvidenceGraph PathId(s)**; path‑local **PathSliceId** is emitted for editioned QD/OEE events. 
* **E5 · Telemetry for refresh.** On illumination increase or archive change, log **policy‑id** and **editions** (`DescriptorMapRef`/`DistanceDefRef`/`CharacteristicSpaceRef`/`DHCMethodSpecRef`/`TransferRulesRef`), enabling **G.11** refresh and **F.15 RSCR** triggers. 

#### 4.4 QD & OEE parity (specialisations)

* **QD parity.** Require identical **CharacteristicSpace** resolution/topology and **`CharacteristicSpaceRef.edition`**, plus **`DescriptorMapRef.edition`**, **`DistanceDefRef.edition`**, **InsertionPolicyRef**, **EmitterPolicyRef** across families during comparison; **Illumination** remains a gauge unless CAL promotes. 
* **OEE parity (POET/Enhanced‑POET/DGM‑class).** Declare a shared **`EnvironmentValidityRegion`** and **`TransferRulesRef.edition`**; outputs are **{environment, method}** portfolios; **coverage/regret** are gauges. 

### 5) Interfaces — minimal I/O (conceptual; Core‑only)

| Interface                          | Consumes                                                                                                  | Produces                                                                                                                                                                                                                    |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **G.9‑1 `Plan_Parity`**            | BaselineSet; FreshnessWindows; **CG‑Spec** ids; **SoS‑LOG bundles**; Bridges/Φ; EditionPins; Budgeting; ε | **`ParityPlan@Context`** (UTS row; editioned)                                                                                                                                                                               |
| **G.9‑2 `Run_Parity`**             | `ParityPlan@Context`; `TaskSignature (S2)`; **G.5.Select**                                                | Selector outputs (**set** per `PortfolioMode`), DRR+SCR with **PathIds/PathSliceId**, Portfolio Pack                                                                                                                        |
| **G.9‑3 `Publish_ParityReport`**   | Run artefacts; Telemetry                                                                                  | **`ParityReport@Context`**: `⟨BaselineSet, FreshnessWindows, ComparatorSet(id), EpsilonDominance ε?, PathIds[], AbstainReasons[], Portfolio, Gauges{Illumination, coverage, regret}, DHCMethodRef.edition/DHCMethodSpecRef.edition/DistanceDefRef.edition/CharacteristicSpaceRef.edition?, EditionPins, CalibrationLedgerId?/BCT.id?, RSCRRefs[]⟩` |
| **G.9‑4 `Expose_ParityTelemetry`** | Archive/regret signals; illumination deltas                                                               | Telemetry events (`PathSliceId`, **policy‑id**, editions) for **G.11** refresh/**F.15** RSCR                                                                                                                                |

*Surfaces are **conceptual**; serialisations belong to **G.10 Annex/Interop** (no tool lock‑in). *

### 6) Conformance Checklist (CC‑G9)

1. **Equal windows & editions.** All baselines **SHALL** use **identical FreshnessWindows** and **pinned editions** for **`DHCMethodRef`** and **`DistanceDefRef`**; QD pins include `DescriptorMapRef.edition`, `CharacteristicSpaceRef.edition` (if applicable), `DistanceDefRef.edition`, and `Emitter/Insertion` policies. 
2.  **Spec‑level pin.** Where DHC methods are used, parity **SHALL** also pin **`DHCMethodSpecRef.edition`** to forbid silent spec drift and to enable RSCR triggers.
3. **Lawful orders; no scalarisation.** The harness **MUST NOT** force a total order where only partial orders are lawful; return **Pareto/Archive** and tie‑notes; **no ordinal averages**. 
4. **Gauge discipline.** If Characteristics differ by unit/scale/space, parity **MUST** declare a lawful **gauge mapping** and compare only after mapping (“map, then compare”).
5. **Default dominance.** `DominanceRegime` **SHALL** default to **`ParetoOnly`**; any inclusion of illumination into dominance **MUST** be a CAL policy with **policy‑id** cited in SCR. 
6. **Bridge routing.** Cross‑Context/plane/Kind use **MUST** cite **Bridge ids** and **Φ(CL)**/**Φ_plane** (and **Ψ(CL^k)** where used); penalties **→ R_eff only**; **F/G invariant**. 
7. **Path citation.** Every parity decision **MUST** cite **EvidenceGraph PathId(s)** (and **A.10** anchors); refusal paths included. 
8. **Telemetry for illumination/OEE.** Any illumination increase or OEE transfer **MUST** log `PathSliceId`, **policy‑id**, and active editions (incl. **`CharacteristicSpaceRef.edition`** and **`TransferRulesRef.edition`**). 
9. **RSCR parity tests.** Publish RSCR tests covering **negative/refusal paths** (illegal CHR, missing Bridges/Φ tables, edition drift). 
10. **ATS visibility.** AH‑1..AH‑4 **MUST** pass on crossings and lexical duty (UTS/twin labels). 
11. **Tech‑register discipline.** Do not use the noun *metric* as a Tech primitive; cite **`DHCMethodRef`**/**`U.Measure`** and **`DistanceDefRef`** editions.
12. **MOO surfaced (parity).** Method-of-obtaining-output: `Run_Parity` **MUST** record the **ParityHarnessId** and any active **EmitterPolicyRef/InsertionPolicyRef** (where QD applies), together with the **CAL policy‑id** for any non‑default dominance. These ids **SHALL** appear in **SCR** and parity telemetry (PathSlice‑keyed). (No scalarisation is introduced by this reporting.)



### 7) Anti‑patterns & remedies

* **AP‑1 Hidden edition drift.** *Remedy:* Pin editions in `EditionPins`; re‑run RSCR on any change. 
* **AP‑2 Averaging ordinals.** *Remedy:* CG‑Spec guards + CSLC proofs; report as **ordinal compare‑only**. 
* **AP‑3 Illumination in dominance by default.** *Remedy:* Keep as **gauge**; promote only via CAL policy id. 
* **AP‑4 Bridge‑free crossings.** *Remedy:* Require **Bridge** with **CL** and **loss note**; penalties to **R**. 
* **AP‑5 “Metric” as a primitive in Tech.** *Remedy:* Use **`DHCMethodRef`**/**`U.Measure`** and **`DistanceDefRef`** with editions; in Plain register *metric* may appear only as a didactic synonym with an explicit pointer to canonical terms.
* **AP‑6 Hidden spec drift.** *Remedy:* Pin **`DHCMethodSpecRef.edition`** and register RSCR tests for spec changes; refuse parity reuse on unpinned spec editions.

### 8) Archetypal grounding (informative, SoTA‑oriented)

**Show‑A · Decision‑making multi‑Tradition parity (EU/MCDA vs Causal vs Offline‑RL/DT vs BO).**
*Plan.* Equal **freshness** (e.g., rolling 24 mo); ComparatorSet uses **ordinal** preference and **ratio** risk (CVaR). *Execution:* selector returns a **Pareto set**; **no cross‑ordinal weighting**; **regret** reported as a **gauge** in telemetry (report‑only).  

**Show‑B · QD parity (MAP‑Elites / CMA‑ME / DQD / QDax‑class).**
*Plan.* `PortfolioMode=Archive`, fixed grid (or CVT), **CharacteristicSpaceRef.edition=v1**, **DescriptorMapRef.edition=v2**, **DistanceDefRef.edition=v2**, `EmitterPolicyRef=v3`, `InsertionPolicyRef=elite‑replace`. *Execution:* **Archive** is the returned set; **IlluminationSummary (Q/D/QD‑score)** reported; **dominance = ParetoOnly** unless CAL says otherwise.  

**Show‑C · OEE parity (POET/Enhanced‑POET/DGM‑class).**
*Plan.* Shared **`EnvironmentValidityRegion`** and **`TransferRulesRef.edition`**; ComparatorSet ties coverage to **gauge** semantics; selector returns **{environment, method}** portfolios. *Execution:* **coverage/regret** recorded as **gauges**; edition & **policy‑id** bumps logged with **PathSliceId**; where QD is active, also log **`CharacteristicSpaceRef.edition`**.

> *Didactic note.* These examples follow **“single call, many solvers”** and **portfolio‑first** selection idioms (akin to **DifferentialEquations.jl**/**JuMP**) that **G.5** expects; G.9 supplies the *parity scaffolding* around those calls. 

### 9) Payload — what this pattern *exports*

**`ParityReport@Context`** (UTS row; editioned):
`⟨BaselineSet, FreshnessWindows, ComparatorSet(id), EpsilonDominance ε?, Portfolio(Set | Archive), Gauges{Illumination, coverage, regret}, PathIds[], PathSliceId?, BridgeIds[], ΦPolicyIds[]/Φ_plane?/Ψ(CL^k)?, DHCMethodRef.edition/DHCMethodSpecRef.edition/DistanceDefRef.edition/CharacteristicSpaceRef.edition?, EditionPins, CalibrationLedgerId?/BCT.id?, AbstainReasons[], RSCRRefs[]⟩`.


**Plus:** DRR+SCR bundle; **Portfolio Pack**; **Run‑safe Plan**; Telemetry events for **G.11** refresh. 

### 10) Relations

**Builds on:** **G.5** (set‑returning selector), **G.6** (PathIds, PathSlice), **G.4** (Acceptance thresholds), **C.23** (SoS‑LOG duties), **C.22** (S2 typing), **C.18/C.19** (QD/E‑E), **F.15** (RSCR harness), **F.9** (Bridges/CL).  
**Publishes to:** **UTS** (plans/reports; twin labels), **G.11** (refresh signals), **G.10** (shipping surface, Annex mappings). 
**Constrains:** **G.5** callers to cite **policy‑ids & editions** in portfolios; **G.12** dashboards to treat parity gauges lawfully. 

### 11) Author’s quick checklist

1. **Plan**: fix BaselineSet (≥2 traditions), equal FreshnessWindows, **ComparatorSet** bound to **CG‑Spec** (CSLC proofs attached; gauge mappings declared where needed). 
2. **Pin** editions (`DescriptorMapRef`/`DistanceDefRef`/`DHCMethodRef`/**`DHCMethodSpecRef`**/`Emitter`/`Insertion`/`TransferRulesRef` if OEE). 
3. **Declare** `PortfolioMode` and **default** `DominanceRegime=ParetoOnly`; if changing, cite CAL **policy‑id**. 
4. **Route** crossings via Bridges; publish **Φ(CL)**/**Φ_plane**; penalties → **R_eff only**. Reference **G.7** **Calibration Ledger/BCT** ids for the crossings used.
5. **Execute** G.5; **return a set**; record DRR+SCR with **PathIds**/**PathSliceId**.  
6. **Publish** `ParityReport@Context`; attach RSCR parity tests (refusal paths; edition drift). 

## G.10 — **SoTA Pack Shipping (Core Publication Surface)**  \[A]

**Tag:** [A] (conceptual, notation‑independent; Core surface only)
**Stage:** *release‑time* composition of discipline packs, consumable by selectors and audits; edition‑aware; ATS‑gated
**Builds on:** **G.1–G.8** (generator → harvester → CHR/CAL → dispatcher → evidence/bridges/log bundle), **F.17–F.18** (UTS & naming), **B.3** (trust calculus), **E.5.2** (notational independence), **E.11** (ATS; AH‑1..AH‑4), **C.18/C.19/C.23** (NQD/QD‑telemetry; E/E‑LOG; SoS‑LOG)
**Publishes to:** **UTS** (twin‑label Name Cards), **G.5** (selector parity pins & portfolios), **SCR/RSCR**, **G.11** (telemetry/refresh)
**Optional inputs:** **G.13 `InteropSurface@Context`** (if present) MAY be cited to declare which external‑index editions and gauge/plane embeddings informed the shipped pack; Core remains notation‑independent (Annex handles concrete crosswalks).

### 1) Intent

Provide a **single, normative shipping surface**—the **SoTA‑Pack(Core)**—that turns the outputs of G.1–G.8 into a **release‑quality, selector‑ready, edition‑aware portfolio** without mandating any file formats. The pack **exposes what was decided, why, and under which policies/editions**, so that **G.5 may return sets (Pareto or Archive)** and audits can cite **stable EvidenceGraph paths**. Illumination/coverage (**QD**) and OEE signals are exported as **gauges**, not forced into dominance unless a declared policy says so. (All order/illumination defaults are **inherited** from **G.5/G.6/G.8**.)

**Why this matters.** Earlier G‑patterns emphasised legality and assurance; **G.10** completes the generative loop by defining **how SoTA outputs are *shipped***—with parity pins, PathSlice anchoring, ATS harness hooks, and telemetry stubs—so the next author or selector can **use** them immediately, not just verify them.

**Editorial – Close the generative loop.** For each CG‑Frame, drive **G.1 Generator → G.2 SoTA Harvester → G.3–G.4 authoring → G.5 Selector (set‑returning)**, then publish a **SoTA‑Pack(Core)** (this pattern) with parity pins & PathIds, and register **G.11** refresh on illumination increases (QD/OEE). *(No additional file formats; Core remains notation‑independent.)*

### 2) Problem frame

Teams can already generate variants (G.1), harvest SoTA (G.2), author CHR/CAL/LOG (G.3–G.4), register families (G.5), mint paths (G.6), calibrate bridges (G.7), and bundle SoS‑LOG (G.8). What is **missing** is a **Core, notation‑independent shipping object** that *packages* these moving parts with:

* **UTS‑visible identities and twin labels** (so people can talk about the pack); **no tool lock‑in** in Core.
* **Selector parity** (ComparatorSet and EditionPins) so G.5 can compute **sets** lawfully; **Illumination** stays a **gauge** by default. 
* **PathIds/PathSliceIds** and **policy‑ids** so **C.23 decisions** and maturity changes cite **exact evidence paths**.
* **Telemetry stubs** so **edition‑aware refresh** can be triggered on **illumination increases** or bridge edits. 

### 3) Solution — *Ship a SoTA‑Pack(Core); keep file formats in Annex*

A **SoTA‑Pack(Core)** is a **conceptual object** (published to **UTS** and surfaces) with **no mandated serialisation** in Core; mapping to external crates/registries (e.g., RO‑Crate, ORKG, OpenAlex) lives in **Annex/Interop**. Core prescribes **fields and obligations**, not files or schemas. **Cards/tables are conceptual only**; machine checks and linters belong to Tooling. (Per **E.5.2**, formats are out‑of‑scope for Core.)

#### 3.1 Data model (normative; notation‑independent)

```
SoTA‑Pack(Core) :=
⟨ PackId (UTS), Edition, HomeContext,
  CG‑FrameRef, describedEntity := ⟨GroundingHolon, ReferencePlane⟩,
  ComparatorSetRef (CG‑Spec) + Γ‑fold notes,            // legality & folding
  ParityPins := { EditionPins, ΦPolicyIds },             // edition/policy anchors (ids only)
  Families := { MethodFamilyIds[], GeneratorFamilyIds?[] },
  SoS‑LOGBundleRef?, MaturityCardRef?,                   // G.8 outputs
  AdmissibilityLedgerRef?,                               // selector-facing rows
  Portfolio := { DominanceRegime, PortfolioMode, ε? },   // default: ParetoOnly
  Bridges := { BridgeIds[], ΦPolicyIds[], Φ_plane?, Ψ(CL^k)?[] },
  Evidence := { A10EvidenceGraphRef?[], EvidenceGraphPathIds?[] }, // path-justified slots
  QD := { CharacteristicSpaceRef,
          CharacteristicSpaceRef.edition?,
          DescriptorMapRef.edition,
          DistanceDefRef.edition,
          DHCMethodRef.edition?,        // optional: guards gauge computations when CHR-provided
          DHCMethodSpecRef.edition?,    // optional: prevents silent spec drift (parity alignment)
          EmitterPolicyRef?, InsertionPolicyRef?, 
          IlluminationSummary? },       // gauges; report-only by default
  OEE? := { EnvironmentValidityRegion, TransferRulesRef.edition }, // generator families
  PathSlices := { PathSliceId?[] },                      // pins Γ_time & plane
  SCR/DRR := { SelectionReports[], RationaleEntries[] },
  Notes ⟩
```

**Defaults & invariants.** Inherit order/illumination and measurement legality from **CC‑G5/CC‑G6/CC‑G8**. Locally for shipping: (i) **ParityPins** MUST include `EditionPins` for any QD/OEE surfaces (`DescriptorMapRef.edition`, `DistanceDefRef.edition`, and, where applicable, `CharacteristicSpaceRef.edition`, `TransferRulesRef.edition`). (ii) **PathSliceId** MUST be recorded whenever QD/OEE pins exist (for path‑local refresh). (iii) **CL/CL^plane** penalties **reduce `R_eff` only** (F/G invariant).

> *Rationale.* This structure gives **G.5** everything it needs: admissible order, portfolio semantics, **parity pins** and **policy ids**, and (when present) **QD/OEE gauges** and **PathIds** for explainability, without binding to any vendor notation.

### 4) Shipping choreography (normative steps; SoTA method for release)

**S‑1 · Pin parity (ComparatorSet & Editions).**  
Attach the **CG‑Spec ComparatorSet** (characteristics, **ScaleComplianceProfile (SCP)**, Γ‑fold) and **EditionPins** for QD/OEE (`DescriptorMapRef.edition`, `DistanceDefRef.edition`, `TransferRulesRef.edition`), and, when relevant to reproduction of partitioning, `CharacteristicSpaceRef.edition`. 
For **QD archive semantics**, also **pin `EmitterPolicyRef` and `InsertionPolicyRef`** (replacement/K‑capacity semantics). 
This ensures **lawful comparison** and **replayable fronts**; **IlluminationSummary** is exported as a **gauge**.

**S‑2 · Publish selector semantics.**  
Declare `DominanceRegime` and `PortfolioMode ∈ {Pareto|Archive}` (and `ε` if used). **Return sets** (non‑dominated or archive) by default; do **not** force scalarisation.

**S‑3 · Bind crossings to penalties (R‑only).**  
For every cross‑Context/plane or kind crossing, cite **Bridge ids** and **ΦPolicyIds**/**Φ_plane** (and **Ψ(CL^k)** where applicable). **Penalties are monotone, bounded, table‑backed** and **route to `R_eff` only**; **F/G invariant**. Publish **loss notes** in UTS/Notes.

**S‑4 · Anchor evidence.**
Provide **A.10 anchors** (lanes + freshness windows) and, where already minted, **PathIds**/**PathSliceIds** for rung changes and LOG decisions; missing anchors **forbid** maturity advance. **Lane tags** remain separable into **TA/VA/LA** and visible in **SCR**.

**S‑5 · Expose ATS harness hooks (AH‑1..AH‑4).**
The pack exports identifiers so **TierClassifier, GateCheck, LaneCheck, LexicalCheck** can run; publication **fails** if a crossing lacks **UTS+Bridge**, if lane purity is violated, or if **Φ/Ψ** are absent.

**S‑6 · Wire telemetry for refresh.**  
Whenever **illumination increases** or archive editions change, emit telemetry with **PathSliceId**, the active **policy‑id**, and editions of `DescriptorMapRef`/`DistanceDefRef` (and `TransferRulesRef.edition` for OEE). 
Also log **`EmitterPolicyRef` and `InsertionPolicyRef`** in telemetry for QD runs. 
When QD partitioning depends on the Space phase, include `CharacteristicSpaceRef.edition`. 
These feed **G.11** refresh/decay and **path‑local RSCR** (Bridge sentinels).

**S‑7 · Publish to UTS (twin labels; local‑first).**
Mint a **UTS Name Card** for the pack and its major items (e.g., `SoS‑LOGBundle@Context`, `AdmissibilityLedger`, `MaturityCardDescription`), with **Tech/Plain twins** under the local Context; **identity travels only via Bridges** with CL and loss notes.

> **Design note.** The choreography is **methodic generation**, not a post‑hoc checklist: parity pinning, path anchoring, ATS gating, and telemetry stubs are **produced** during shipping to increase the chance that downstream selections and updates remain lawful and reproducible. (This rebalances FPF from “assurance‑only” toward **result‑oriented generation**.)

### 5) Interfaces & hooks (selector‑ and audit‑facing)

| ID         | Interface (conceptual)     | Consumes                                                          | Produces                                                |
| ---------- | -------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------- |
| **G.10‑1** | `Compose_SoTA_Pack`        | G.1–G.8 outputs, ComparatorSet, Bridges, editions, SCR/DRR deltas | `SoTA‑Pack(Core)` (UTS row + surfaces)                  |
| **G.10‑2** | `Publish_PortfolioSurface` | Portfolio semantics, parity pins, ε?                              | Selector‑readable parity surface (no formats mandated)  |
| **G.10‑3** | `Expose_AH_Hooks`          | GateCrossings, lanes, Φ/Ψ policy‑ids                              | AH‑1..AH‑4‑ready ids; **fail** on missing hooks         |
| **G.10‑4** | `Emit_TelemetryPins`       | Illumination/archive/OEE events                                   | PathSlice‑keyed telemetry: `policy‑id`, `…Ref.edition`  |
| **G.10‑5** | `Publish_PathCitations`    | A.10 anchors, PathIds                                             | PathId/PathSlice citations for C.23/H4 & rung changes   |
| **G.10‑6** | `Ingest_InteropSurface?`   | (optional) **G.13 `InteropSurface@Context`**                       | Annotated pack notes citing external‑index editions      |

*Surfaces remain **conceptual** per **E.5.2**; RO‑Crate/ORKG/OpenAlex mappings belong to **Annex/Interop** and do not affect Core conformance.*

### 6) Conformance checklist (CC‑G10)

This pattern **inherits** order/illumination, evidence, and bridge/penalty legality from **CC‑G5**, **CC‑G6**, **CC‑G8**. Shipping‑specific requirements:

1. **CC‑G10.1 (Notation‑independent).** The pack **MUST NOT** rely on any specific file syntax; **cards/tables are conceptual**; tool serialisations are informative only.
2. **CC‑G10.2 (Pack parity pins).** If QD/OEE fields are present, **pin** `DescriptorMapRef.edition`, `DistanceDefRef.edition`, (OEE) `TransferRulesRef.edition`; include `CharacteristicSpaceRef.edition` where it affects partitioning reproducibility; for **QD archive semantics** also **pin `EmitterPolicyRef` and `InsertionPolicyRef`**. *(Informative alias: **ArchiveConfig** := {`CharacteristicSpaceRef`?, `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `EmitterPolicyRef`, `InsertionPolicyRef`}.)*
3. **CC‑G10.3 (Telemetry discipline).** Any **illumination increase** or archive edit **SHALL** log **PathSliceId**, active **policy‑id**, the active editions of the pinned `…Ref` fields (including OEE `TransferRulesRef.edition`), **and** the active **`EmitterPolicyRef`/`InsertionPolicyRef`**.
4. **CC‑G10.4 (UTS publication & twins).** All shipped heads appear on **UTS** with **Tech/Plain twins**; cross‑Context identity travels **only by Bridges** with CL and loss notes.
5. **CC‑G10.5 (MOO surfaced in shipping).** Method-of-obtaining-output surfacing: for every **Portfolio set** or **Archive** published, the pack **SHALL** list the applicable **generation/parity mechanism** ids
+   (**EmitterPolicyRef/InsertionPolicyRef** for QD archives; **ParityHarnessId** for parity; **DHCMethodRef** where method definitions are generators) and the active **policy‑id(s)** in **SCR** and **telemetry pins**. (Core remains notationally independent.)

### 7) Relations

**Builds on:** G.1 (generator), **G.2** (SoTA Synthesis), **G.3–G.4** (CHR/CAL legality & acceptance), **G.5** (registry/selection), **G.6** (EvidenceGraph paths & PathSlice), **G.7** (Bridge/CL calibration), **G.8** (SoS‑LOG bundle & maturity ladder).
**Publishes to:** **UTS**, **G.5** (parity surface), **SCR/RSCR**, **G.11** (refresh on telemetry).
**Constrains:** any Tooling export; formats exist only in **Annex/Interop** (non‑normative).

### 8) Worked micro‑sketch (informative; post‑2015 SoTA families)

**CG‑Frame:** *Decision‑making under constraints* (multi‑method portfolio).
*Families registered:* Outranking/MCDA; Causal/SCM; BO; RL/Policy‑search; **QD‑RL** (*e.g.,* MAP‑Elites/CMA‑ME‑class); **OEE** task generator (POET‑class).
**Shipping highlights.**
(1) **Parity pins**: ComparatorSet cites `SafetyClass(ord)`, `CostUSD_2025(ratio)`, …; Γ‑fold = WLNK for assurance.
(2) **Portfolio**: `DominanceRegime=ParetoOnly`, `PortfolioMode=Archive`, `ε=0.01`.
(3) **QD**: `DescriptorMapRef.edition=DM‑v5`, `DistanceDefRef.edition=Δ‑Hamming‑v2`, `CharacteristicSpaceRef.edition=CS‑v3?`, 
    `EmitterPolicyRef=E/E‑LOG:budgeted‑explore`, `InsertionPolicyRef=replace_if_better@K=2`, 
    (`DHCMethodRef.edition?`, `DHCMethodSpecRef.edition?` when CHR‑based gauges apply); 
    **IlluminationSummary** reported (triad Q/D/QD‑score), **not** used for dominance. 
(4) **OEE**: `EnvironmentValidityRegion=R&D‑bench v1`, `TransferRulesRef.edition=TFR‑v3`.
(5) **Crossings**: `Bridge{Marketing→Engineering, CL=2}` with **loss note**; **Φ(CL)** and **Φ_plane** ids shown; **R‑only** penalty routing.
(6) **Paths**: Shortlist decisions cite **PathIds**; rung upgrades attach PathIds; **PathSliceId** carried for the QD edition snapshot.
(7) **Telemetry**: when coverage ↑ in archive cell (QD‑RL run), emit `Telemetry(PathSlice)` with **policy‑id** + editions; **G.11** schedules path‑local refresh. 

### 9) Author’s quick checklist

1. **Pin parity.** Attach `ComparatorSetRef` + Γ‑fold; freeze `…Ref.edition` (QD/OEE).
2. **Declare portfolio.** Set `DominanceRegime`/`PortfolioMode`/`ε`.
3. **Route crossings.** List Bridges + **Φ/Ψ** policy‑ids; put loss notes on UTS.
4. **Cite evidence.** Include A.10 anchors and any stable **PathIds**; ensure lanes and freshness windows are visible to **SCR**.
5. **ATS hooks.** Expose ids for **AH‑1..AH‑4**; shipping blocks on missing hooks.
6. **Telemetry stubs.** Log **PathSliceId** + **policy‑id** + **edition** fields for QD/OEE **and** the active **`EmitterPolicyRef`/`InsertionPolicyRef`**.
7. **UTS & twins.** Publish Name Cards (Tech/Plain); keep **local‑first**; Bridges carry identity across.

### 10) Didactic distillation (90‑second script)

> *Ship thinking, not files.* A **SoTA‑Pack(Core)** is the **one place** where a discipline’s generated methods and portfolios are **ready to use**: parity‑pinned, path‑anchored, ATS‑gated, and telemetry‑aware. It tells selectors **what order to use** and **which set to return**, auditors **which paths to cite**, and authors **which editions/policies** to repeat. Formats come later (Annex); **Core stays semantic and universal**.

**Annex/Interop pointer (informative).** Serialisation recipes (e.g., RO‑Crate 1.2 profiles for UTS rows, PathSlice pins, Φ‑policy ids; ORKG/OpenAlex cross‑walks) live in **Part I** and are **non‑normative**. Core conformance is judged on **conceptual fields** and **obligations** alone.

## G.11 — **Telemetry‑Driven Refresh & Decay Orchestrator** [A]

**Tag.** [A] (architectural, notation‑independent; Core)
**Stage.** *run‑time & maintenance‑time* (drives selective re‑computation and republication)
**Primary hooks.** **G.6** (EvidenceGraph & Path/PathSlice ids), **G.7** (Bridge Sentinels, CL/Φ/plane), **G.5** (set‑returning selector), **G.8** (SoS‑LOGBundle; maturity ladder; QD/OEE pins), **G.10** (SoTA Pack shipping ↦ telemetry pins), **C.18/C.19** (QD/illumination; E/E‑LOG emitters), **C.23** (Method‑SoS‑LOG duties), **B.3.4** (evidence decay/epistemic debt), **E.11** (ATS AH‑1..AH‑4).       

**Why this exists.** Earlier G‑patterns made SoTA packs lawful and selector‑ready; this pattern closes the loop by **turning telemetry and decay into concrete refresh actions** that (i) keep SoTA packs current without pack‑wide reruns, (ii) preserve lawful orders (set‑returning selection; no forced scalarisation), and (iii) make QD/OEE exploration **operational** (edition‑aware, policy‑tracked) rather than merely auditable.  

**Refresh triggers (normative)**
Treat the following as **refresh causes** (Path‑local where possible) and run **targeted RSCR** before republication:
* **Illumination/archive deltas (QD).** Telemetry events carrying `PathSliceId`, active `policy‑id`, and editions of `DescriptorMapRef`/`DistanceDefRef` (**plus** `CharacteristicSpaceRef` when domain‑family coordinates are used).
* **OEE transfer deltas.** Edition change in `TransferRulesRef` or update to `EnvironmentValidityRegion`.
* **Legality surface edits.** Changes to **Γ‑fold** definitions, **gauge** mappings, or **Φ** tables/policies.
* **Bridge calibration edits.** Bridge/BCT changes that affect **CL** or plane penalties.
* **Dominance policy changes.** CAL policy‑id changes that promote gauges into dominance.

**Modularity note.** G.11 is **purely conceptual** (E.5.2): it prescribes identifiers, triggers, and obligations—not file formats or tools. Any serialisation lives in Annex/Interop; Core conformance is judged on semantics only. 

### 1) Intent

Given **PathSlice‑keyed telemetry** and **evidence freshness windows**, produce a **`RefreshPlan@Context`** that (a) identifies the **minimal set of paths and portfolios** that must be recomputed or re‑published, (b) executes **edition‑aware** QD/OEE reruns **under the same laws** (dominance defaults, gauge semantics), and (c) emits **DeprecationNotices** and **EditionBumpLog** while keeping **F/G invariants** and routing Bridge penalties to **R_eff only**.   

### 2) Problem frame

Blind “full rebuilds” and audit‑only workflows either waste compute or let **epistemic debt** accumulate. QD/OEE runs shift archives and coverage, but without **edition‑pinned** descriptors and policy ids, selectors and dashboards drift silently. Cross‑Context reuse changes (Bridges, CL, Φ/plane) are often handled ad hoc rather than as **sentinel‑driven, path‑local RSCR**. We need an orchestrator that **turns signals into scoped refresh**, maintaining lawful orders and ATS visibility.   


### 3) Forces

* **No‑Free‑Lunch vs. stability.** The selector must **return sets** under partial orders; refresh must **not** smuggle in scalarisation. **Default `DominanceRegime = ParetoOnly`.** 
* **Gauge vs. order.** **IlluminationSummary (Q/D/QD‑score)** informs exploration and dashboards as a **gauge**; it **does not** enter dominance unless CAL says so (policy‑id cited). 
* **Edition‑awareness.** QD/OEE parity requires pinned **`DescriptorMapRef.edition`**, **`DistanceDefRef.edition`**, **`InsertionPolicyRef`**, **`EmitterPolicyRef`**, and (for OEE) **`TransferRulesRef.edition`**.  
* **Bridge hygiene.** CL/CL^k/CL^plane changes must trigger **path‑local** refresh; penalties route to **R_eff**; **ReferencePlane** is always declared. 
* **ATS gates.** Crossings must remain visible to **AH‑1..AH‑4** (Tier/Gate/Lane/Lexical). 

### 4) Solution — **From telemetry to targeted recomputation**

#### 4.1 Signals (what G.11 consumes)

1. **PathSlice Telemetry.** Emitted by G.10/G.9/G.8: `⟨PathSliceId, policy‑id, DescriptorMapRef.edition, DistanceDefRef.edition, CharacteristicSpaceRef.edition?, EmitterPolicyRef?, InsertionPolicyRef?, TransferRulesRef.edition? (OEE), timeWindow⟩`.   
2. **Bridge Sentinels.** Registered for each GateCrossing; any edit to **CL/CL^k/CL^plane** or Φ/Ψ policy ids raises a **path‑local** refresh event. 
3. **Freshness Windows & Decay.** KD‑CAL lanes carry **freshness**; when windows expire, **epistemic debt** rises and triggers **Refresh/Deprecate/Waive** governance. 

#### 4.2 Trigger catalogue (normative)

* **T0 — Policy change (generation/parity).** A change in the active **policy‑id** for **Emitter/Insertion** (E/E‑LOG) or parity harness under fixed editions ⇒ schedule **slice‑scoped** recomputation for the affected portfolios/archives; do **not** alter dominance defaults.
* **T1 — Illumination increase.** Δcoverage>0 or ΔQD‑score>0 under the active archive & grid. ⇒ schedule archive‑scoped recomputation; **do not** change dominance unless CAL policy promotes illumination (policy‑id cited to SCR).  
* **T2 — Edition bump (QD).** Change in `DescriptorMapRef.edition` and/or `DistanceDefRef.edition` (and, when partition depends on Space phase, `CharacteristicSpaceRef.edition`). ⇒ recompute the **same** QD metrics under new editions; publish **EditionBumpLog**. 
* **T3 — Edition bump (OEE).** Change in `TransferRulesRef.edition` or `EnvironmentValidityRegion`. ⇒ re‑evaluate `{environment, method}` portfolios; **coverage/regret remain gauges**. 
* **T4 — Bridge change.** Any update to CL/CL^k/CL^plane or Φ/Ψ policy ids on a crossing. ⇒ **path‑local RSCR** + refresh of affected selections; penalties route to **R_eff only**. 
* **T5 — Freshness expiry.** Any A.10 carrier behind a LOG decision or Acceptance gate passes `valid_until`. ⇒ schedule refresh per lane; may issue **DeprecationNotice** if budget exceeded. 
* **T6 — Maturity rung change.** A **C.23** rung justification (PathId) is upgraded/downgraded. ⇒ Rebind **AdmissibilityLedger** rows; update SoS‑LOGBundle edition; cite PathIds. 
* **T7 — Policy change.** CAL policy altering dominance set (e.g., illumination promotion) or Γ‑fold. ⇒ Re‑execute selection under new policy; record policy‑id in SCR; update the **Portfolio Pack** (per G.10), not a new surface term.

#### 4.3 Planner (conceptual algorithm; minimal recomputation)

```
Given: Telemetry events E, Bridge edits B, Freshness expiries F, Policy changes P
1) Partition events by PathSliceId; compute dependency closure over EvidenceGraph (ancestors that change legality/lanes).
2) For each slice S:
   a) Enforce legality: CG‑Spec checks; refuse illegal ops; compute ReferencePlane/Φ_plane.
   b) If S involves QD: pin editions; schedule Γ_nqd.{updateArchive,illuminate,selectFront}.
   c) If S involves OEE: schedule portfolio recomputation over {environment, method} with GeneratorFamily parity.
   d) If Bridges changed: run path‑local RSCR; recompute R_eff (F/G invariant).
   e) If freshness expired: sample per-lane refresh; if budget limited, raise DeprecationNotice.
3) Compose a **RefreshPlan@Context** with ordered actions and expected deltas; publish to UTS; execute and update **SCR/RSCR** only (DRR applies to normative edits, not run‑time refresh).
```

*Lawful orders.* The planner **never** forces total orders; **G.5** returns sets (Pareto/Archive). **Illumination** remains a **gauge** unless promoted via CAL policy.  

#### 4.4 Outputs (selector‑ and audit‑facing)

* **`RefreshPlan@Context` (UTS row; editioned).**
  `⟨PlanId, PathSliceIds[], Triggers{T1..T7}, Actions{RecomputeSelection | UpdateArchive | RebindBridge | Re‑publishBundle | RebuildPortfolioSurface}, EditionPins{…Ref.edition}, PolicyPins{Φ/Ψ ids}, ExpectedGauges{Illumination, coverage, regret}, AffectedPortfolios{set|archive}, RSCRRefs[], Notes⟩`.
*Execution results appear in* **`RefreshReport@Context`** (PathIds, **SCR/RSCR deltas**, EditionBumpLog ids). 
* **`EditionBumpLog`** and **`DeprecationNotice[]`** (UTS rows; contextual, lane‑aware). 
* **Telemetry echo.** Every illumination increase or OEE transfer records `PathSliceId`, **policy‑id**, and active editions (incl. `CharacteristicSpaceRef.edition` and `TransferRulesRef.edition`). For PathSlice‑pinned QD/OEE, surface `U.DescriptorMapRef.edition` / `U.DistanceDefRef.edition` to align with PathCard.

### 5) Interfaces — minimal I/O (conceptual; Core‑only)

| ID                                 | Interface                                                                   | Consumes                                                                                                            | Produces |
| ---------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | -------- |
| **G.11‑1 `Ingest_Telemetry`**      | PathSlice telemetry; Bridge Sentinel events; freshness expiries             | `RefreshQueue` (slice‑keyed), annotated with Trigger kinds                                                          |          |
| **G.11‑2 note**                    | Use **Portfolio Pack** / shipping artefacts from G.10; do not introduce new surface names.                         |                                                                                                                      |          |
| **G.11‑3 `Execute_RefreshPlan`**   | `RefreshPlan@Context`                                                       | Updated portfolios (sets/archives), **SCR** deltas (policy‑id + PathIds), **EditionBumpLog**, **DeprecationNotice** |          |
| **G.11‑4 `Publish_RefreshReport`** | Execution artefacts                                                         | `RefreshReport@Context` (UTS row) + PathId citations for C.23/H4                                                    |          |

*ATS harness.* All crossings exposed for **AH‑1..AH‑4** remain visible; publication **fails** if UTS+Bridge are missing or lanes are impure. 

### 6) Conformance Checklist (CC‑G11)

1. **CC‑G11.1 (Scoped by PathSlice).** Every refresh is **slice‑scoped**; pack‑wide reruns are prohibited unless the dependency closure spans all slices (record rationale). 
2. **CC‑G11.2 (Edition discipline).** When QD/OEE are active, **pin** and **echo**: `DescriptorMapRef.edition`, `DistanceDefRef.edition`, **`CharacteristicSpaceRef.edition` whenever a domain‑family coordinate is declared per C18‑1b**, `EmitterPolicyRef`, `InsertionPolicyRef`, `TransferRulesRef.edition` (OEE). **`.edition` SHALL apply only on `…Ref`**. **Fail** if any required pin is missing.  
3. **CC‑G11.3 (Gauge legality).** Publish **Q/D/QD‑score** and **IlluminationSummary** as gauges; **exclude from dominance** unless a CAL policy promotes them; record the **policy‑id** in SCR. 
4. **CC‑G11.4 (Bridge penalties).** CL/CL^k/CL^plane penalties **route to R_eff only**; **F/G invariant**; publish **Φ/Ψ ids** with loss notes. 
5. **CC‑G11.5 (Selector invariants).** **G.5** is called with the same lawful **ComparatorSet** and returns **sets** (Pareto/Archive); no scalarisation is introduced by refresh. 
6. **CC‑G11.6 (ATS visibility).** AH‑1..AH‑4 **MUST** pass for all refreshed crossings; missing hooks block publication. 
7. **CC‑G11.7 (Decay governance).** Freshness expiry triggers **Refresh/Deprecate/Waive** with budget notes; decisions appear in **DeprecationNotice** and SCR. 

### 7) Anti‑patterns & remedies

* **Full‑rerun mania.** Rebuilding everything on minor Bridge edits. → **PathSlice‑scoped** RSCR + refresh; document slice closure. 
* **Editionless QD.** Comparing QD outcomes across space/distance changes without editions. → **Pin editions**; re‑illuminate; log **EditionBump**. 
* **Gauge scalarisation.** Using illumination to alter dominance by default. → Keep as **gauge**; require **CAL policy id** to promote. 
* **Bridge blindness.** Ignoring CL^plane at world↔concept↔episteme crossings. → Compute **Φ_plane**; penalties to **R_eff**; cite ids. 
* **Telemetry gaps.** Emitting coverage gain without policy‑id/editions. → Refuse; **G.11‑2** MUST fail the plan until telemetry is complete. 

### 8) Consequences

* **Selective, edition‑aware upkeep.** Minimal recomputation with **auditable** triggers and **policy‑pinned** context. 
* **Operational QD/OEE.** Illumination and open‑ended exploration inform **refresh**, not dominance, unless explicitly authorised. 
* **Downstream cleanliness.** Selectors and dashboards consume **updated sets** with lawful orders and **Φ** ids; DHC metrics can be charted with declared windows/units. 

### 9) Worked micro‑sketches (informative; SoTA‑oriented)

* **QD Portfolio (MAP‑Elites / CMA‑ME / DQD / QDax‑class).** A run increases coverage in several cells. Telemetry logs `PathSliceId`, `EmitterPolicyRef`, `InsertionPolicyRef`, editions for `DescriptorMapRef`/`DistanceDefRef`. **G.11** plans an **Archive** refresh only for affected slices; selector returns the **archive set**; **IlluminationSummary** is reported (Q/D/QD‑score) and **excluded from dominance** (default). 
* **OEE Portfolio (POET/Enhanced‑POET/DGM‑class).** `TransferRulesRef.edition` bumps; telemetry cites `EnvironmentValidityRegion`. **G.11** schedules recomputation of `{environment, method}` portfolios; **coverage/regret** reported as gauges; selector returns a **set of pairs**; CAL policies unchanged. 

### 10) Relations

**Builds on:** **G.6** (PathId/PathSlice), **G.7** (Bridge Sentinels & calibration), **G.8** (bundles; maturity), **G.9** (parity scaffolding & edition pins), **C.18/C.19** (QD & E/E‑LOG), **C.23** (SoS‑LOG), **B.3.4** (decay), **E.11** (ATS).
**Consumes:** Telemetry pins from **G.10/G.9**; Edition pins and policy ids from **G.5/G.8**.
**Publishes to:** **UTS** (RefreshPlan/Report; EditionBumpLog; DeprecationNotice), **SCR/RSCR** (path‑local checks), **G.12** (discipline dashboards).  

### 11) Author’s quick checklist

1. **Collect pins.** Ensure telemetry includes `PathSliceId`, **policy‑id**, and all required `…Ref.edition` fields (QD/OEE). For PathSlice‑pinned QD/OEE, expose `U.DescriptorMapRef.edition` / `U.DistanceDefRef.edition` in line with PathCard.
2. **Scope to slices.** Build the **minimal** dependency closure over EvidenceGraph; avoid pack‑wide reruns. 
3. **Re‑select lawfully.** Call **G.5** with unchanged ComparatorSet; **return sets** (Pareto/Archive). 
4. **Respect gauges.** Publish **Q/D/QD‑score** and any coverage/regret as **gauges**; do **not** alter dominance unless CAL policy id promotes. 
5. **Bridge routing.** If CL/plane changed, re‑compute **R_eff**; **F/G invariant**; cite **Φ/Ψ ids**. 
6. **Decay actions.** When freshness expires, choose **Refresh/Deprecate/Waive**; publish notices; update SCR/DRR. 
7. **ATS pass.** Keep AH‑1..AH‑4 hooks visible; block publication on missing UTS+Bridge. Do not emit DRR from run‑time refresh; use DRR only for normative Core edits (E.9).

### 12) Didactic distillation (60‑second script)

> *Refresh thinking, not just files.* **G.11** listens to **telemetry** and **decay**, finds the **smallest PathSlices** that matter, and **re‑runs only those**—with **editions and policies pinned** so parity holds. It never changes your order defaults: the selector still **returns sets**, and illumination remains a **gauge** unless you *explicitly* promote it. The result is SoTA that **stays SoTA**—auditable, edition‑aware, and cost‑aware.  

## G.12 — **DHC Dashboards · Discipline‑Health Time‑Series (lawful gauges, generation‑first)** [A]

**Stage.** *design‑time authoring* → *run‑time computation & publication* (dashboard series)
**Primary hooks.** **C.21 Discipline‑CHR** (what to measure), **G.2** (SoTA palette & **DHC‑SenseCells**), **G.5** (selector; set‑returning portfolios), **G.6** (EvidenceGraph & PathId/PathSlice), **G.8** (SoS‑LOG bundle & maturity ladders), **G.10** (SoTA‑Pack shipping & telemetry stubs), **G.11** (telemetry‑driven refresh/decay), **C.18/C.19** (Illumination/QD; E/E‑LOG), **C.23** (SoS‑LOG duties), **F.17/F.18** (UTS & twin labels), **E.5.2** (notation independence).
**Why this exists.** **C.21** defines lawful *slots* for discipline health (DHC) but not a SoTA method to *produce* dashboard time‑series. **G.12** provides that method: a disciplined, edition‑aware pipeline that computes DHC values from evidence paths, selector outputs, and QD/OEE gauges—without illicit scalarisation, without averaging ordinals, and with telemetry that keeps dashboards fresh via **G.11**. This operationalizes the “coordinates with G.12” promise in **C.21**. 
**Modularity note.** G.12 consumes CHR/CAL/LOG artefacts and emits UTS‑published dashboard rows; formats (e.g., RO‑Crate/ORKG/OpenAlex) remain Annex/Interop and do **not** affect Core conformance (per **G.10**, **E.5.2**). 

### 1) Intent

Turn **discipline‑health definitions** (C.21) into a **lawful, reproducible, refresh‑aware dashboard series** that:
(i) reads **evidence** by **PathId/PathSlice** (C.21↔G.6), (ii) folds values only where **CG‑Spec** allows (units/scale/polarity proved), (iii) exposes **freshness windows** and **ReferencePlane** explicitly, (iv) uses **selector outputs** as *sets* (Pareto/Archive) rather than forcing total orders, and (v) treats **Illumination/QD** as **gauges** (not in dominance unless CAL policy promotes).  

### 2) Problem frame

Teams publish “field health” numbers with mixed scales, hidden re‑parameterisations, and cross‑Context roll‑ups that violate Γ‑fold/Bridge discipline. Ordinal quantities (e.g., standardisation stages) get averaged; QD/coverage signals are smuggled into dominance. No one pins **editions** of descriptor spaces or distances, so dashboards silently drift. We need a **generation‑first** pattern that computes DHC time‑series **legally** and **refreshes selectively** when telemetry indicates illumination/edition changes or decay.  

### 3) Forces

* **Assurance vs. results.** Dashboards must *increase the chance of good results*, not only audit them; legality remains visible. 
* **No‑Free‑Lunch.** Selection returns **sets** under partial orders; dashboards must respect this and never coerce to totals. 
* **Gauge vs. order.** **IlluminationSummary** (*Q/D/QD‑score*) informs exploration as a **gauge**; dominance changes only via named CAL policy‑id. 
* **Edition‑awareness.** QD/OEE parity requires **`.edition` on …Ref** for spaces/distances/transfer rules; telemetry must carry **policy‑id** and **PathSliceId** so G.11 can refresh slices, not packs.  
* **Bridge hygiene & planes.** Cross‑Context/plane comparisons cite **Bridge id + CL** and **Φ/Φ_plane**; penalties reduce **R_eff** only. 

### 4) Solution — *Author C.21 once; compute & publish DHC series lawfully and refresh‑aware*

#### 4.1 Objects (LEX heads; twin‑register discipline)

* **`DHCSeries@Context`** — the UTS‑published time‑series object for a discipline’s dashboard (editioned).
* **`DHCSlot`** — a typed slot authored via **C.21** (`Characteristic`, `Scale/Unit/Polarity`, `ReferencePlane`, `Γ_time`, lane tags). **No arithmetic** is permitted until CSLC legality is proved. 
* **`DHCMethodRef` / `DHCMethodSpecRef`** — edition‑pinned references to the method/definition used to compute a slot value (table‑backed registry). 
* **`EditionPins`** — `{ DHCMethodRef.edition, DHCMethodSpecRef.edition, DistanceDefRef.edition, DescriptorMapRef.edition?, CharacteristicSpaceRef.edition?, TransferRulesRef.edition? }` captured per row. 
* **Naming discipline.** Tech register uses **`U.DescriptorMapRef (d≥2)`** for QD spaces; Plain twin is **`CharacteristicSpaceRef`**; **aliasing is forbidden** and **`.edition` SHALL appear only on `…Ref`** per **E.10 §6.2** (see also G.9/G.7 twin‑naming notes). 

#### 4.2 Method‑of‑Obtaining (SoTA, generation‑first; design‑time → run‑time)

**Stage A — Author & Bind (design‑time)**
A1. **Author slots via C.21.** For each DHC slot (e.g., *ReproducibilityRate*, *StandardisationLevel*, *AlignmentDensity*, *DisruptionBalance*, *EvidenceGranularity*, *MetaDiversity*), bind CHR characteristics, scales/units, lanes, `Γ_time`, and **ReferencePlane**; declare **TargetSlice (USM)** and scope; record **compare‑only** for ordinals. 
A2. **Attach CG‑Spec and Proof stubs.** Cite **CG‑Spec** ids for any numeric comparisons/aggregations; prove CSLC legality/compliance and declare Γ‑fold (WLNK unless justified). **Where Bridges/planes are involved, the penalty policies `Φ(CL)`, `Φ_plane` (and `Ψ` for Kind‑bridges) MUST be *monotone, bounded, and table‑backed* (record policy‑ids).**
A3. **Pin methods.** Register `DHCMethodSpecRef` and its `DHCMethodRef` for each slot; edition‑pin both for parity & RSCR. 
A4. **Declare QD/OEE hooks (if used).** Name `DescriptorMapRef`/`DistanceDefRef` (+ editions), `EmitterPolicyRef`, `InsertionPolicyRef`; for OEE, register `GeneratorFamily` with `EnvironmentValidityRegion` and `TransferRulesRef.edition`. **Illumination remains a gauge by default** (see **DominanceRegime ∈ {ParetoOnly, ParetoPlusIllumination}**).

**Stage B — Compute (run‑time, lawful gauges)**
B1. **Harvest evidence** by **PathId/PathSlice**, preserving lanes (TA/VA/LA) and freshness windows (Γ_time). 
B2. **Compute per‑slot values** using the *edition‑pinned* `DHCMethodRef` and, where relevant, `DistanceDefRef`. per‑slot values** using the *edition‑pinned* `DHCMethodRef` and, where relevant, `DistanceDefRef`.
 • *ReproducibilityRate (LA lane).* Ratio under declared Γ_time with minimal evidence; abstain/degrade on missingness.
 • *StandardisationLevel (ordinal).* Publish **compare‑only**; forbid means/z‑scores.
 • *AlignmentDensity.* Count Bridges with **CL≥2** per **100 DHC‑SenseCells**; units = `bridges_per_100_DHC_SenseCells`; treat **CL=3** as *free substitution*, **CL=2** as *guarded* (counted with loss notes). Cite Bridge ids + policy‑ids; penalties → **R_eff** only.
 • *DisruptionBalance.* Compute with a **registered CD‑index class** (edition‑pinned) and publish *target bands*; **not** monotone “more is better.”
 • *EvidenceGranularity*/*MetaDiversity.* Compute as declared (entropy/HHI); record units and windows.
All numeric ops must cite **CG‑Spec**; cross‑Context values move only via Bridges with CL and loss notes. 
B3. **Integrate selector outputs (sets).** When a DHC slot depends on method performance trade‑offs (e.g., portfolio coverage), call **G.5.Select** and **return sets** (Pareto/Archive); never force totals. Publish **`DominanceRegime ∈ {ParetoOnly, ParetoPlusIllumination}`** and **`PortfolioMode ∈ {Pareto|Archive}`** (defaults: `ParetoOnly`, `Pareto`). 
B4. **Treat QD/OEE as gauges.** If illumination is active, publish **IlluminationSummary (Q/D/QD‑score)** and **Archive** snapshot; if OEE is active, publish coverage/regret per `{Environment, MethodFamily}`; **exclude from dominance** unless a CAL policy (id) promotes. Echo **edition pins** and **policy‑id** in SCR.  

**Stage C — Publish & Wire for refresh (run‑time, publication)**
C1. **Publish DHC rows to UTS** with **twin labels** (Tech/Plain), slots’ *ReferencePlane*, lane tags, windows, and **EditionPins**. 
C2. **Cite paths.** Each row lists contributing **EvidenceGraph PathId(s)**/**PathSliceId**; Bridge ids and **Φ(CL)**/**Φ_plane** (and **Ψ** if Kind‑Bridge) appear in SCR with loss notes; penalties route to **R_eff only**; **Φ/Ψ policies are *monotone, bounded, table‑backed***. 
C3. **Emit telemetry for G.11.** On any **illumination increase** or edition bump (space/distance/transfer‑rules), record `PathSliceId` + **policy‑id** + active editions so **G.11** plans **slice‑scoped** refresh.  

> **SoTA note (informative).** Typical QD/OEE families include **MAP‑Elites/CVT‑ME, CMA‑ME/MAE, DQD/MEGA, QDax (JMLR 2024)** for illumination and **POET/Enhanced‑POET** with **Darwin Gödel Machine (2025)**‑class variants for open‑ended generation. These are registered as `MethodFamily`/`GeneratorFamily` entries and consumed via **G.5**/**C.23** with **IlluminationSummary** reported as gauges. (Default: *not in dominance*.) 

### 5) Interfaces — minimal I/O (conceptual; Core‑only)

| ID                                     | Interface                                                                                                  | Consumes                                                                                                 | Produces                                                                                    |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **G.12‑1 `Build_DHCSeries`**           | C.21 slot specs, CG‑Spec ids, `DHCMethod*Ref`, windows, ScopeSlice                                         | `DHCSeries@Context` (UTS row; editioned; lanes/windows/planes surfaced)                                  |                                                                                             |
| **G.12‑2 `Compute_DHCRow`**            | EvidenceGraph **PathId/PathSlice**, Bridges(+CL/Φ/plane), `DistanceDefRef.edition`, `DHCMethodRef.edition` | `(slot_id, value, compare‑only?, units/scale, stance, window, PathIds[], BridgeIds[], Φ/Φ_plane ids, EditionPins)` |
| **G.12‑3 `Integrate_PortfolioGauges`** | `SoTA‑Pack(Core)` parity pins, G.5 outputs, QD/OEE telemetry                                               | `IlluminationSummary`, Archive snapshot, `{Environment,MethodFamily}` coverage/regret gauges (SCR‑cited) |                                                                                             |
| **G.12‑4 `Publish_DashboardSlice`**    | Rows from G.12‑2/‑3                                                                                        | UTS Name Cards (Tech/Plain twins); SCR notes (policy‑ids; planes; penalties→R_eff)                       |                                                                                             |
| **G.12‑5 `Emit_TelemetryPins`**        | Illumination increase, edition bump, transfer events                                                       | PathSlice‑keyed telemetry (`policy‑id`, `…Ref.edition`) for **G.11** refresh plan                        |                                                                                             |

(*Do not introduce file formats; surfaces are conceptual. Serialisation recipes live in Annex/Interop.*) 

### 6) Conformance Checklist (CC‑G12, normative)

1. **C.21 compliance.** Every dashboard row traces to a **C.21‑authored DHC slot** with **Characteristic + Scale/Unit/Polarity**, lane tags, **Γ_time**, stance, and **ReferencePlane** declared. **No arithmetic** proceeds without CSLC legality. 
2. **Ordinal discipline.** Ordinal slots (e.g., *StandardisationLevel*) are **compare‑only**; **no means/z‑scores**. 
3. **CG‑Spec citation.** All numeric operations cite **CG‑Spec** characteristics, gauge/Γ‑fold, and MinimalEvidence; gauge mappings are explicit (“map, then compare”). 
4. **Set‑returning selection.** When invoking **G.5**, **return sets** (Pareto/Archive); **default `DominanceRegime = ParetoOnly`**; any promotion of Illumination into dominance **MUST** cite CAL **policy‑id** in SCR.  
5. **Edition discipline.** Pin `DHCMethodRef.edition`, `DHCMethodSpecRef.edition`, `DistanceDefRef.edition`, and—if QD/OEE—`DescriptorMapRef.edition` / `CharacteristicSpaceRef.edition?` / `EmitterPolicyRef` / `InsertionPolicyRef` / `TransferRulesRef.edition`. **`.edition` SHALL appear only on `…Ref`.**  
6. **Bridge routing & planes.** Cross‑Context/plane rows **MUST** cite **Bridge id + CL** and **Φ(CL)**/**Φ_plane**; penalties route to **R_eff** only; **F/G invariant**; **Φ/Ψ policies SHALL be monotone, bounded, and table‑backed** (ids recorded). 
7. **Telemetry sufficiency.** Any illumination increase or OEE transfer **MUST** log `PathSliceId`, **policy‑id**, and active editions; missing pins **block publication** until remedied. 
8. **UTS publication & twins.** Publish dashboard rows as **UTS Name Cards** with **Tech/Plain twins**; identity travels via Bridges with loss notes. 

### 7) Bias‑Annotation (E‑cluster lenses)

* **Didactic.** One‑screen tables; plain names + twin labels.
* **Architectural.** No ordinals averaged; penalties never touch F/G; planes explicit. 
* **Pragmatic.** Freshness‑aware; unknowns tri‑state; telemetry‑driven refresh. 
* **Epistemic.** Evidence lanes & PathIds explicit; maturity rungs ordinal; illumination is a gauge. 

### 8) Consequences

* **Generation‑first dashboards.** Authors publish *how values are produced* (methods, editions, paths), not just thresholds; selectors and dashboards stay lawful by construction. 
* **Selective, edition‑aware upkeep.** Telemetry makes **G.11** refresh **slice‑scoped**, preventing drift without pack‑wide reruns. 
* **Plurality preserved.** Set‑returning selection + Bridge hygiene avoids phlogiston‑like “trans‑disciplines” and illicit scalarisation. 

### 9) Relations

**Builds on:** **C.21** (DHC), **G.6** (PathId/PathSlice), **G.8** (SoS‑LOGBundle), **G.10** (SoTA‑Pack shipping), **G.11** (refresh), **C.18/C.19** (QD/E‑E), **C.23** (SoS‑LOG). **Coordinates with:** **G.5** (selector returns sets; parity pins), **F.17/F.18** (UTS/twins). **Constrains:** dashboard consumers: illumination is a **gauge** by default; cross‑Context use must publish **Φ** ids; planes explicit.   

### 10) Author’s quick checklist

1. Bind each slot via **C.21** (CHR + CG‑Spec + Γ_time + ReferencePlane + stance + lanes). 
2. Register and **pin** `DHCMethodSpecRef`/`DHCMethodRef` and any `DistanceDefRef`. 
3. If QD/OEE active, declare `DescriptorMapRef`/`CharacteristicSpaceRef?`/`Emitter`/`Insertion`/(OEE) `TransferRulesRef` editions; **IlluminationSummary** stays a gauge. 
4. Harvest **PathIds/PathSliceIds** and compute values; forbid ordinal means; cite Bridges + **Φ/Φ_plane**; penalties→**R_eff**. 
5. Publish to **UTS** (twins), attach SCR notes (policy‑ids, planes, edition pins). 
6. Emit telemetry on illumination increase/edition bumps for **G.11**. 

### 11) Worked micro‑examples (informative; SoTA‑oriented)

**(A) Decision‑making discipline (multi‑tradition).**
Slots: *ReproducibilityRate* (LA, Γ_time=3y), *StandardisationLevel* (ordinal), *AlignmentDensity* (Bridges CL≥2 across EU/MCDA, SCM/DoWhy, RL/Decision‑Transformer), *DisruptionBalance* (DI‑class, target band), *MetaDiversity* (HHI of operator families). QD annex: Descriptor space = `U.DescriptorMapRef (d≥2)`, Archive (MAP‑Elites/CMA‑ME/DQD), **IlluminationSummary** reported with `{DescriptorMapRef.edition, DistanceDefRef.edition}`; OEE annex: POET‑class `GeneratorFamily` with `EnvironmentValidityRegion` and `TransferRulesRef.edition`. Illumination and coverage/regret are **gauges**; selection returns **Pareto/Archive** sets.  

**(B) Evolutionary software architecture.**
Slots: *ReproducibilityRate* (LA, Γ_time=3y), *StandardisationLevel* (ordinal), *AlignmentDensity* (Bridges CL≥2 across EU/MCDA, SCM/DoWhy, RL/Decision‑Transformer; units `bridges_per_100_DHC_SenseCells`), *DisruptionBalance* (**CD‑index class**, target band), *MetaDiversity* (HHI of operator families). QD annex: Descriptor space = `U.DescriptorMapRef (d≥2)`, Archive (MAP‑Elites/CMA‑ME/DQD), **IlluminationSummary** reported with `{DescriptorMapRef.edition, DistanceDefRef.edition}`; OEE annex: POET‑class `GeneratorFamily` with `EnvironmentValidityRegion` and `TransferRulesRef.edition`. Illumination and coverage/regret are **gauges**; selection returns **Pareto/Archive** sets.  

## G.13 — **External Interop Hooks for SoTA Discipline Packs (conceptual)** \[INF]

**Tag.** \[INF] (informative, conceptual hooks; no file formats mandated)
**Stage.** *design‑time mapping* → *run‑time ingestion & refresh*
**Primary hooks.** **G.2** (SoTA harvester), **G.5** (set‑returning selector & registries), **G.6** (EvidenceGraph & PathId/PathSlice), **G.7** (Bridge Matrix & CL/planes), **G.8** (SoS‑LOG bundles), **G.9** (parity harness), **G.10** (SoTA‑Pack shipping), **G.11** (telemetry‑driven refresh), **G.12** (DHC dashboards), **C.21** (Discipline‑CHR), **C.23** (Method‑SoS‑LOG), **E.5.2** (notation independence), **E.11** (ATS gates AH‑1..AH‑4).   

### 1) Problem frame

FPF already defines how to **compose lawful characteristics, evidence, and selectors**; it also packages SoS‑LOG rule sets and returns **sets** (Pareto/archives) rather than smuggling scalarisations. But authors still spend effort *hand‑harvesting* SoTA material from external scholarly indexes (OpenAlex, ORKG, Crossref, discipline repositories), creating ad‑hoc pipelines with inconsistent **editions, freshness windows, planes, and gauges**. The absence of a **conceptual interop layer** slows the creation of SoTA architheories and makes parity/refresh brittle. **G.13** supplies the missing layer: *conceptual* mappers and telemetry hooks that let external index data be **lawfully mapped**, edition‑pinned, and wired into **G.2→G.5→G.9→G.10→G.11→G.12** without specifying file formats (Annex/Interop owns serialisations). By construction, **Illumination** and coverage remain **gauges** unless a CAL policy promotes them; dominance defaults to **ParetoOnly**.  

### 2) Problem

External indexes publish **claim‑adjacent signals** (citations, disruption, replication, dataset links, task taxonomies). These signals are valuable for SoTA **generation** (not only audit), but:

* **Comparability risk.** Units/scales vary; ordinal signals are routinely averaged; plane crossings (world↔concept↔episteme) are implicit. (FPF forbids ordinal averages; penalties from plane or context crossings must route to **R_eff** only.)  
* **Edition drift.** Index snapshots change, silently breaking QD/OEE parity and dashboards unless **editions** and **policy‑ids** are pinned in telemetry. 
* **Assurance overreach.** Without a method to *produce* outputs, teams over‑invest in checks. FPF needs **generation‑first** interop that feeds selector portfolios, SoS‑LOG maturity, and DHC gauges. 

### 3) Forces

| Force                     | Tension                                                                                                                       |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Notation independence** | Helpful serialisations (RO‑Crate, ORKG, OpenAlex) vs **Core conceptual** surfaces only.                                       |
| **Pluralism vs parity**   | Diverse scholarly traditions vs lawful, edition‑aware comparison; **return sets** under partial orders.                       |
| **Gauge vs dominance**    | Illumination/coverage inform exploration but **do not** change dominance unless CAL policy says so.                           |
| **Planes & bridges**      | Cross‑plane/context reuse must publish **Φ(CL)** and **Φ_plane** ids; losses touch **R** only.                                |
| **OEE/QD parity**         | Generator families (POET‑class, DGM‑class) require **TransferRulesRef.edition**, environment validity, and coverage gauges.   |

### 4) Solution — *Conceptual mappers + telemetry that drive generation, not just audit*

#### 4.1 Objects (LEX heads; twin‑register discipline)

* **`ExternalIndexCard@Context`** — conceptual registration of an external index/snapshot:
  `⟨IndexId, ProviderName, Edition (date/commit), CoverageScope, Licence, describedEntity := ⟨GroundingHolon, ReferencePlane⟩, FreshnessWindow, Notes⟩`.
  *Edition lives on the **Card**, and is cited by downstream mappers and telemetry.*

* **`ClaimMapperCard@Context`** — executable *conceptual* mapping (no file syntax) from index entities to FPF artefacts:
  `⟨MapperId, Source[IndexId], Targets{ClaimSheet|BridgeHints|SoS-LOG hints}, PlaneMap(world|concept|episteme), GaugeMap (for scale/unit/space embeddings), EvidenceGraphRef(A.10), CSLC Proof Stubs, Edition⟩`.
  *PlaneMap and GaugeMap define lawful embeddings; Bridge generation is **not** automatic — crossings publish **Φ**/**Ψ** policy‑ids and **CL/CL^k** as applicable (monotone, bounded, table‑backed).*  

* **`SoSFeatureTransform@Context`** — turns mapped claims into **CHR‑typed** SoS features (e.g., disruption, replication coverage, standardisation rate), each bound to **CG‑Spec** characteristics with declared **Scale kind, units, polarity, ReferencePlane**. 

*Any numeric operation **MUST** be CSLC‑legal; ordinal measures are compare‑only; units are aligned per CG‑Spec; no ordinal→cardinal promotion.*

* **`IndexTelemetryPin`** — edition bump or policy change signal (notation‑independent):
  `⟨IndexId, Edition, PathSliceId?, policy‑id?, When⟩` routed to **G.11** for slice‑scoped refresh. 

*Edition fields **SHALL** appear **only** on `…Ref` objects when references are present (cf. CC‑G10/CC‑G12); parity pins echo active editions and policy‑ids.*

* **`InteropSurface@Context`** — selector‑ and dashboard‑facing summary: what has been mapped, from which index edition, with which gauge/plane embeddings (published on UTS; twins Tech/Plain). 

#### 4.2 Generation‑first interop flow (notation‑independent)

1. **Register sources.** Author **ExternalIndexCard**(s) with editions & freshness windows; declare describedEntityPlane. 
2. **Map claims.** Run **ClaimMapperCard** to produce **ClaimSheets** (e.g., problem/task taxonomies, method assertions, dataset links) and **BridgeHints** (candidate context crossings with loss notes). Plane crossings publish **Φ_plane** alongside **Φ(CL)**; penalties route to **R_eff** only. 
3. **Type as SoS features.** Apply **SoSFeatureTransform** to bind mapped signals to **CG‑Spec** characteristics (scale legality via CSLC proofs), producing lawful SoS inputs for **C.21** DHC slots and **C.23** maturity rules.  
4. **Feed generation.**

   * **G.2** harvests *competing Traditions* plus mapped SoS features to build SoTA palettes and **Bridge Matrices**;
   * **G.5** registers **MethodFamily/GeneratorFamily** entries and, on selection, **returns sets (Pareto/Archive)** with **DRR+SCR** and portfolios, never forcing totals;
   * **G.9** executes parity under equal windows/editions; illumination & coverage are **gauges**.  
5. **Publish & ship.** **G.8** bundles SoS‑LOG rules and **MaturityCard** (ordinal; thresholds stay in Acceptance), and **G.10** composes SoTA Packs with telemetry pins — still **conceptual** surfaces (Annex handles RO‑Crate/ORKG/OpenAlex).  
6. **Refresh by telemetry.** Index edition bumps emit **IndexTelemetryPin**. **G.11** plans **slice‑scoped** refresh, respecting **DominanceRegime = ParetoOnly** and keeping illumination as a **gauge** unless CAL promotes it (policy‑id in SCR). **Φ/Ψ policies are monotone, bounded, table‑backed; penalties route to `R_eff` only (F/G invariant).**  

#### 4.3 Interop specialisations (worked patterns; all conceptual)

* **OpenAlex‑class mapper.** Works/Authors/Concepts → `ClaimSheet`(Problem/Method/Result) + SoS features (e.g., growth, disruption, collaboration breadth); Concept graph crossings publish **Bridge ids** with **Φ** penalties to **R_eff**.
* **ORKG‑class mapper (claim‑level).** ResearchProblem/Contribution/Comparison → `ClaimSheet` + **SoS‑LOG** rule hints (admit/degrade/abstain branches tied to evidence lanes and maturity rungs). Thresholds remain in **G.4 Acceptance**. 
* **PRISMA‑class artefacts.** Systematic‑review metadata mapped to **EvidenceGraph** anchors (A.10 lanes, freshness windows) to back **C.23** decisions; PathIds cited at run‑time in SCR. 

> **OEE/QD parity.** When interop powers **GeneratorFamily** work (e.g., importing environment families or transfer rules from external corpora), **pin `TransferRulesRef.edition`** and publish coverage/regret as **gauges**; selection returns **{environment, method}** portfolios. 

### 5) Interfaces — minimal I/O standard (conceptual; Core‑only)

| ID                                  | Interface                                                  | Consumes                                                     | Produces                                                                 |
| ----------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------ |
| **G.13‑1 `Register_ExternalIndex`** | `ExternalIndexCard` fields                                 | Provider metadata, scope, **Edition**, freshness             | `ExternalIndexCard@Context` (UTS row; twin labels)                       |
| **G.13‑2 `Map_ClaimsToFPF`**        | `ExternalIndexCard`, Mapper/Gauge/Plane maps, A.10 anchors | Claim entities, taxonomies                                   | `ClaimSheet@Context`, `BridgeHints`, PathId anchors (conceptual)         |
| **G.13‑3 `Derive_SoSFeatures`**     | ClaimSheets, CG‑Spec ids, CSLC stubs                       | typed SoS features                                           | `SoSFeatureSet@Context` (CHR‑typed; planes & units declared; **ordinal → compare‑only**) |
| **G.13‑4 `Publish_InteropSurface`** | G.13‑2/‑3 outputs                                          | parity pins (windows, **editions**), planes, bridges, gauges | `InteropSurface@Context` (UTS row; selector/dashboard‑readable)          |
| **G.13‑5 `Emit_IndexTelemetryPin`** | Edition bump / policy change                               | Index & edition, PathSlice?, policy‑id?                      | Telemetry to **G.11** (`PathSliceId`, **policy‑id**, active editions; **editions appear only on `…Ref`**)    |
| **G.13‑6 `Wire_To_SoTA_Pack`**      | InteropSurface + G.1–G.8 outputs                           | SoTA shipping data                                           | **G.10** pack hooks (conceptual surfaces; Annex maps to ORKG/OpenAlex).  |

### 6) Archetypal Grounding (informative; SoTA‑oriented)

**System.** *Software architecture portfolio design.* Import OpenAlex “software architecture” concept neighbourhood; map to ClaimSheets of architectural tactics. Feed **G.5** to select a **Pareto set** of tactics under cost/performance/reliability; publish **Bridge/Φ** ids for any cross‑context reuse; **IlluminationSummary** remains a **gauge**.  

**Episteme.** *Science‑of‑science discipline dashboard.* Use ORKG comparison graphs to derive SoS features (replication coverage, standardisation rate, disruption balance) as **CHR‑typed** characteristics for **C.21** DHC slots; publish on UTS with twins; **G.11** refreshes slices when index **Edition** changes. 

**OEE/QD.** *Open‑ended environment generation.* Import external environment taxonomies; register a **GeneratorFamily** with `EnvironmentValidityRegion` and **`TransferRulesRef.edition`**; selector returns **{environment, method}** portfolios; coverage/regret are **gauges**. 

### 7) Bias‑Annotation

* **Didactic lens.** Tech/Plain twins at publication; no vendor/tool tokens. 
* **Architectural lens.** **No forced scalarisation**; dominance defaults to **ParetoOnly**; illumination & coverage are **gauges** unless CAL promotes.  
* **Epistemic lens.** Plane crossings publish **Φ(CL)**/**Φ_plane** ids; penalties reduce **R_eff** only; **F/G invariant**. 

### 8) Conformance Checklist (CC‑G13, conceptual; applies when G.13 surfaces are used)

1. **Notation‑independence.** Interop surfaces are **conceptual**; any serialisation lives in **Annex/Interop**; Core conformance is judged on semantics only. 
2. **CHR legality.** Every numeric SoS feature **MUST** bind to **CG‑Spec** with declared **Scale kind, units, polarity, ReferencePlane** and **CSLC** legality; ordinal measures are **never** averaged/subtracted. 
3. **Bridges & planes.** Cross‑context/plane reuse **MUST** cite **Bridge ids** and **Φ(CL)**/**Φ_plane** (and **Ψ(CL^k)** when a KindBridge is involved) **policy‑ids**; **Φ/Ψ policies SHALL be monotone, bounded, table‑backed**; penalties route to **`R_eff` only**; **F/G invariant**. 
4. **Edition discipline.** Interop outputs **SHALL** pin index **Edition** and echo it in parity pins; QD/OEE interop also pins `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and (OEE) **`TransferRulesRef.edition`**. **Edition fields SHALL appear only on `…Ref` objects.**  
5. **Gauge defaults.** **IlluminationSummary** and any coverage/regret **SHALL** be treated as **gauges** and **excluded from dominance** unless a CAL policy promotes them (policy‑id appears in **SCR**). 
6. **Selector invariants.** Any selection spawned from interop **MUST** use **G.5** and **return sets** (Pareto/Archive) under lawful orders; no scalarisation is introduced by interop. 
7. **ATS visibility.** All crossings must expose AH‑1..AH‑4 hooks; missing UTS+Bridge or impure lanes **blocks publication**. 

### 9) Consequences

* **Generation‑first interop.** External indexes become **inputs to method generation** (palettes, portfolios, OEE seeds), not just audit decorations.
* **Edition‑aware parity & refresh.** Index updates trigger **slice‑scoped** recomputation via **G.11**; parity pins stay lawful; dashboards remain stable. 
* **Trans‑disciplinary hygiene.** Bridge/plane publication prevents “phlogiston‑like” pseudo‑disciplines from entering Core without loss notes and penalties to **R** only. 

### 10) Rationale

**FPF is a creativity framework, not an audit checklist.** By making **claim‑level interop** a first‑class conceptual layer, **G.13** routes SoS signals into the **generation loop** (G.2→G.5→G.9) while preserving Core invariants: notation independence, lawful orders, gauge semantics, and plane‑aware penalties. The result is faster, safer SoTA authoring that remains **auditable, edition‑aware, and modular**.

### 11) Relations

**Builds on:** **G.2**, **G.5**, **G.6**, **G.7**, **G.8**, **G.9**, **G.10**, **G.11**, **G.12**, **C.21**, **C.23**, **E.5.2**, **E.11**. 
**Publishes to:** **UTS** (twin labels) and **G.10** shipping surfaces; **G.11** via telemetry pins.  
**Constrains:** Any interop consumer that claims FPF conformance **must** respect gauge/dominance defaults, parity pins, and plane/bridge publication.

### 12) Author’s quick checklist

1. **Card the source.** Register `ExternalIndexCard` with **Edition**, Plane, and FreshnessWindow.
2. **Map claims with legality.** Write `ClaimMapperCard` including **GaugeMap** and **PlaneMap**; attach A.10 anchors; supply CSLC stubs. 
3. **Type SoS features.** Bind to **CG‑Spec** (units/scale/polarity/plane); forbid ordinal averages. 
4. **Pin parity.** Echo index **Edition**; if QD/OEE, also pin `DescriptorMapRef`/`DistanceDefRef`/(OEE) `TransferRulesRef`.  
5. **Feed generation.** Call **G.5** (set‑returning) via **G.9** parity; keep illumination/coverage as **gauges**. 
6. **Ship conceptually.** Publish `InteropSurface@Context` and pack via **G.10** (no file formats in Core). 
7. **Refresh on telemetry.** Emit `IndexTelemetryPin` on edition changes; let **G.11** plan **slice‑scoped** refresh; ensure AH‑1..AH‑4 pass.  

#### Informative SoTA anchors (post‑2015, for orientation)

* **Quality‑Diversity / Illumination.** MAP‑Elites and its successors (CVT‑MAP‑Elites, CMA‑ME/MAE, Differentiable QD incl. MEGA‑variants, QDax JMLR 2024, SAIL) — portfolio‑first exploration with **Q/D/QD‑score** gauges.
* **Open‑Ended Evolution.** POET / Enhanced‑POET and **Darwin Gödel Machine**‑class algorithms — `{environment, method}` portfolios with **coverage/regret** as gauges; **`TransferRulesRef.edition`** pinned. 


### **Part H – Glossary & Definitional Pattern Index**

| §   | ID & Title                     | Tag  | Concise reminder                                               |
| --- | ------------------------------ | ---- | -------------------------------------------------------------- |
| G.1 | Alphabetic Glossary            | INF  | Every `U.Type`, relation & operator with four‑register naming. |
| G.2 | Definitional Pattern Catalogue | \[D] | One‑page micro‑stubs of every `[D]` pattern for quick lookup.  |
| G.3 | Cross‑Reference Maps           | INF  | Bidirectional links: Part A ↔ Part C ↔ Part B terms.           |


### **Part I – Annexes & Extended Tutorials**

| §   | ID & Title                  | Tag | Concise reminder                                                |
| --- | --------------------------- | --- | --------------------------------------------------------------- |
| G.1 | Deprecated Aliases          | INF | Legacy names kept for backward compatibility.                   |
| G.2 | Detailed Walk‑throughs      | INF | Step‑by‑step modelling of a pump + proof + dev‑ops pipeline.    |
| G.3 | Change‑Log (auto‑generated) | INF | Version history keyed to DRR ids.                               |
| G.4 | External Standards Mappings | INF | Trace tables to ISO 15926, BORO, CCO, Constructor‑Theory terms. |

---

### **Part J – Indexes & Navigation Aids**

| §   | ID & Title               | Tag | Concise reminder                                        |
| --- | ------------------------ | --- | ------------------------------------------------------- |
| H.1 | Concept‑to‑Pattern Index | INF | Quick jump from idea (“boundary”) to pattern (§, id).   |
| H.2 | Pattern‑to‑Example Index | INF | Table listing every archetypal grounding vignette.      |
| H.3 | Principle‑Trace Index    | INF | Maps each Pillar / C‑rule / P‑rule to concrete clauses. |

### **Part K  – Lexical debt**
### Mandatory replacement map for measurement terms

> **Rule:** In all **normative** content (specifications, data schemas, etc.), the deprecated terms **“axis”** and **“dimension”** (and their plural or compound forms) **MUST NOT** be used to denote a measurable aspect. Use **Characteristic** in the Tech register instead. Other colloquial terms should be mapped to canonical terms as listed below. In **Plain** narrative, the legacy words may appear _only on first use_ and only if paired with their canonical equivalent for clarity.

| Legacy Term (context) | **Replace with** (Tech register) | Plain register allowance | Canonical Reference |
| --- | --- | --- | --- |
| axis (of measurement); dimension (of a system or quality) | **(disallowed in Core prose)** → use **Characteristic** | No parenthetical allowance in Core; use **Characteristic / Measure / Coordinate** only | A.17 (CHR-NORM) |
| point (on an axis); data point | **Coordinate** (on a Scale) | “point” _(in explanations only, e.g. “a point on the scale”)_ | A.18 (CSLC-KERNEL) |
| metric value; raw score | **Coordinate** (or **Value**) | “value” _(acceptable in plain usage when context is clear, but formally it’s a Coordinate tied to a Characteristic)_ | A.18, C.16 |
| score (composite or normalized) | **Score** (produced via a **Gauge**) | “score” _(if needed in narrative, ensure it’s explained as a result of a defined Gauge)_ | A.17/A.18 (Gauge/Score) |
| unit dimension; unit axis | **Unit** (of a Scale) | “unit” _(plain usage okay)_ | A.18 (Scale/Unit) |
| metric (as a noun) | **Avoid in Tech and as primitive** → use **`U.DHCMethodRef` / `U.Measure` / Score** | “metric” _(Plain only on first use, with pointer to canonical terms)_ | C.16 § 5.1 (L5), A.18 |

## Migration debt from A.2.6 (Scope, ClaimScope, WorkScope)

### Deprecations (normative)

The following terms **MUST NOT** name scope characteristics in normative text, guards, or conformance blocks:

* *applicability*, *envelope*, *generality*, *capability envelope*, *validity* (as a characteristic name).

Use instead:

* **`U.ClaimScope`** (*Claim scope*, nick **G**) for epistemes;
* **`U.WorkScope`** (*Work scope*) for capabilities;
* **`U.Scope`** only when explaining the abstract mechanism (not in guards).

### Affected locations and required edits (normative)

Editors SHALL apply the following replacements:

1. **Part C.2.2 (F–G–R).**

   * Replace any internal definition of “Generality” with a normative reference to **A.2.6 §6.3** (*Claim scope (G)*).
   * Where “abstraction level” is mentioned as G, replace with “Claim scope (where the claim holds)”; keep **AT** (AbstractionTier) only as optional didactics (non‑G).
   * Ensure composition examples use **intersection/SpanUnion** for G, not ordinal “more/less general”.

2. **Part C.2.3 (Formality F).**

   * No change to F itself.
   * Any example that implies “raising F widens G” MUST be rephrased: F changes expression form; G changes only via **ΔG**.

3. **Part A.2.2 (Capabilities).**

   * Replace “capability envelope/applicability” with **`U.WorkScope`**.
   * Method–Work gates MUST test **Work scope covers JobSlice**, with **measures** and **qualification windows** bound.

4. **Part B (Bridges & CL).**

   * Add a note: **CL penalties apply to R**, not to **F/G**; mapping MAY recommend **narrowing** the mapped scope (best practice).

5. **Part E (Lexicon).**

   * Add entries for **Claim scope (G)**, **Work scope**, **Scope** (mechanism).
   * Mark listed deprecated terms as **legacy aliases** allowed only in explanatory notes.

6. **ESG & Method–Work templates.**

   * Replace any “applicability”/“envelope” guard phrasing with **ScopeCoverage** (see §10).
   * Require explicit **`Γ_time`** selectors in all scope‑sensitive guards.

### Migration playbook (informative)

1. **Inventory** scope‑like phrases across your Context (search: applicability, envelope, generality, capability envelope, valid\*).
2. **Classify** each occurrence as **Claim scope** (episteme) or **Work scope** (capability); replace any “scope characteristic(s)” with “scope type” or “USM scope object” depending on sentence grammar.
3. **Rewrite** guards to use `Scope covers TargetSlice` + explicit **`Γ_time`**; remove “latest”.
4. **Publish** any required **Bridges** with **CL** for Cross‑context usage.
5. **Document** ΔG changes separately from evidence freshness (R).

### Backwards compatibility (informative)

Legacy artifacts MAY keep their historical phrasing in body prose. All **guards, conformance checklists, and state assertions** MUST be rewritten to the USM terms and semantics.


### Change Log (normative migration record)

* **A.2.6 introduced.** Defines `U.ContextSlice`, `U.Scope`, `U.ClaimScope (G)`, `U.WorkScope`; sets algebra and guard patterns.
* **Deprecated labels.** “applicability / envelope / generality / capability envelope / validity” as characteristic names.
* **Edits required.** C.2.2 (G = Claim scope), A.2.2 (Work scope for capabilities), Part B (CL→R note), Part E (Lexicon updates), ESG/Method–Work guard templates (ScopeCoverage + `Γ_time`).
* **No change.** C.2.3 (F) unchanged; its examples updated only for wording consistency.

 