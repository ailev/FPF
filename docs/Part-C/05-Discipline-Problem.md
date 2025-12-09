## 2 · Problem

Teams routinely entangle **programs, specifications, proofs, and datasets**; a “proof” is treated as a tested routine, a “program” is cited as if it entailed a theorem. **Trust decays** because justification and evidence freshness are not explicit. Epistemes are anthropomorphised as actors (“the standard enforces…”), producing **category errors at execution**. Without a shared composition and equivalence calculus, aggregates hide weakest links and analogies harden into overclaims. KD‑CAL must stop these failure modes with a **single constitution and scale‑set**.

---


---

## 2 · Problem

Absent a unified **F**:

1. **Rigor whiplash.** Either everything is forced into premature formalism (blocking exploration), or informal artifacts drift into high‑assurance use (creating silent risks).
2. **Incomparability.** Each Context’s labels mean different things. Reviewers, integrators, and auditors cannot align expectations or compute trustworthy composites.
3. **Lost continuity.** Moving from sketch to proof often becomes a **rewrite**, severing provenance; the same idea looks like different artifacts at each “mode,” inviting translation errors.
4. **Confused roles.** Status (e.g., “accepted here”) gets conflated with rigor (“precise enough”), undermining governance and the KD‑CAL trust math.

---


---

## 3 · Problem  \[I]

1. **Scope–type conflation.** Authors try to widen **G** by “abstracting the wording,” yielding claims that *sound* general but are only supported on a thin slice.
2. **Silent drift across Contexts.** A “vehicle” here is not the same as a “transport unit” there; reuse proceeds without a declared mapping or risk accounting.
3. **Wasteful planning.** Without a signal about the *kind‑level*, teams either over‑formalize single‑slice decisions or under‑test class‑level claims (no variant coverage along subkinds).
4. **Unsafe composition.** Claims about incompatible “things” get composed because the describedEntity was implicit in prose.

---


---

## 3 · Problem

1. **Scope–Type conflation.** Teams broaden G by “abstracting” prose, not by adding supported slices.
2. **Unsafe composition.** Claims are joined though they talk about different “things.”
3. **Cross‑context drift.** Without an explicit core notion of kind, bridges blur describedEntity vs applicability.

---


---

## 3 · Problem

1. **Ambiguous membership.** Membership depends on tacit “latest” states or unwritten defaults.
2. **Signature opacity.** A kind’s definition is scattered; no single place to declare rigor (**F**) or assumptions.
3. **Order violations.** Subkind hierarchies do not guarantee subset behavior in practice.
4. **Scope leakage.** Teams smuggle applicability (G) into kind definitions, recreating G‑ladders by another name.

---


---

## 3 · Problem

1. **Semantic drift.** Moving a claim into a target‑context with a different taxonomy changes “what counts” without anyone noticing.
2. **Hidden order breaks.** Subkind relationships invert or vanish; downstream proofs/tests are misapplied.
3. **Entangled channels.** Teams conflate “scope mapping” with “kind mapping,” making it impossible to assign penalties coherently.
4. **Incomputable guards.** “We map it somehow” yields non‑deterministic classification at guard time.

---


---

## 3 · Problem

1. **Kind sprawl.** Teams mint near‑duplicate kinds (“Account\_PCI”, “Account\_Ledger”), and alignment decays.
2. **Hidden constraints.** Informal “we only accept …” statements leak into prose; guards can’t check them deterministically.
3. **Scope conflation.** Contextual requirements (jurisdiction, API version) get smuggled into “type” talk, blurring Scope vs Kind.
4. **Cross‑context fragility.** Masks don’t travel unless their constraints are mapped; teams reuse names and hope.

---


---

## 2 · Context & Problem

Projects often:

* treat **“more abstract wording”** as wider **G**,
* glue claims with incompatible **describedEntity** (kinds),
* move typed content across Contexts without **declared bridges**,
* or bake **AT** (abstraction vibe) into decision logic.

**C.3.A** fixes this by supplying guard macros that:
— **separate** typed compatibility (kinds) from **Scope** coverage (USM),
— require **both** bridges where needed,
— push congruence penalties to **R** only, and
— forbid **AT** in guards.

---


---

## 3 · Problem & Context (Informative)

### 3.1 The problem C.16 solves

Across architheories, people say “score”, “metric”, “rating”, “property”. Without a shared substrate, numbers drift: *42 of what? on which scale? comparable to whom?* C.16 eliminates drift by requiring every metric notion to **bind** to **one** Characteristic and **one** Scale, and by **separating** intensional anchors from descriptions and gauges. The result is **portable meaning**: a measure is always readable as a **Coordinate on a declared Scale of a named Characteristic**, with a principled path to evidence. 

### 3.2 Context and prior art

* **Kernel canon.** A.17 makes **Characteristic** the sole canonical anchor for measurability; A.18 fixes **CSLC** as the minimal sufficiency for interpretability. C.16 relies on both.
* **Cross‑domain alignment.** The MM‑CHR family already maps FPF U.Types to **ISO 80000‑1 (Quantity)**, **ISO/IEC 25024 (Data‑quality Characteristic)**, **QUDT (QuantityKind/QuantityValue)**, **W3C SOSA/SSN (Observable/Observed/Result)**, and domain “feature/metric” usage (Verspoor, TF Metrics). C.16 uses these rows **as Bridges** (Part F), preserving local senses and documenting losses.  
* **Open‑ended evolution.** FPF replaces “lifecycle” with **Reachable‑States Graph (RSG)**: movement is along **certified states** with checklists; measurement work adopts the same open‑endedness (re‑entry allowed when distinctions change). C.16 uses RSG to frame **readiness** and **revision** of metric notions conceptually (no processes implied).

---


---

## C.20 · **Discipline‑CAL — Composition of `U.Discipline`**  \[A]  *(Architheory: CAL)*

**Builds on.** **C.2 KD‑CAL** (F–G–R & CL routing), **A.19/G.0 CG‑Spec** (comparability), **F.9 Bridges** (cross‑Context alignment), **E.10 LEX** (registers & twin labels). **Coordinates with.** **C.21** (Discipline‑CHR, field health), **C.23** (Method‑SoS‑LOG), **F.17–F.18** (UTS). 

### 1 · Problem Frame
Disciplines persist as *knowledge canons* (epistemes), *codified practices & standards*, and *institutional carriers* (journals, bodies, curricula). FPF needs a typed, provenance‑preserving way to **compose** these into a reusable **holon of talk** that travels across contexts *lawfully*. Composition must honour KD‑CAL lanes and the CG‑Spec Standard so that any numeric comparison or aggregation remains auditable and legal.

### 2 · Problem
Without a **composition calculus** for disciplines:
* fields degenerate into labels; editions and rival **Traditions/Lineages** blur;  
* cross‑Context reuse silently drops meaning (no Bridge/CL), or performs illegal aggregations (means on ordinals; unit mixing);  
* selectors (Part G) cannot lawfully gate methods because maturity/evidence are not tied to a field’s canon and carriers.

### 3 · Forces
| Force | Tension |
|---|---|
| **Pluralism vs Cohesion** | Rival traditions must co‑exist ↔ a discipline holon must present a coherent public surface. |
| **Locality vs Federation** | Meaning is context‑local (rooms) ↔ reuse needs Bridges with CL and recorded loss notes. |
| **Rigor vs Agility** | CG‑Spec legality, KD‑CAL lanes ↔ practical authoring and edition flow (UTS/DRR). |
| **Didactic surface vs Assurance depth** | Human‑readable Discipline Card ↔ auditable F–G–R & provenance. |

### 4 · Solution — the **Discipline holon** and Γ_disc

#### 4.1 U.Types (minting & registers)
* **`U.Discipline`** — a **Holon** that composes an **EpistemeCanon**, **Standards/Practices**, and **Organisational Carriers** into a durable **unit of talk** (R‑core name; twin labels).  
* **`U.AppliedDiscipline`**, **`U.Transdiscipline`** — subtypes of `U.Discipline`.  (**Kernel U‑types; LEX‑governed**).
* **`U.Tradition`**, **`U.Lineage`** — auxiliary holons that organise variants/editions within a `U.Discipline`.  

**Placement/LEX.** `U.Discipline` and its subtypes are **Kernel U‑types** introduced under the **Open‑Ended Kernel** & **Ontological Parsimony** guards (**A.5**, **A.11**) and registered per **E.10/F.17**. This CAL **uses** them, it does not redefine them. If not yet present in A‑cluster, mark as **“provisionally minted”** and open a DRR to finalize placement (E.10 V‑ladder). 

All are **UTS‑published** with **twin labels**; minting follows **E.10** registers/prefix policy and **A.11** parsimony.

#### 4.2 What a `U.Discipline` is / is not
* A `U.Discipline` is **not** a `U.BoundedContext` and **not** a **Domain**. **Domain** remains a *catalog label* (stitched to D.CTX + UTS): **Discipline ≠ Domain** is enforceable via **E.10 LexicalCheck**; any cross‑Domain/Context reuse **MUST** cite a **Bridge (F.9) + CL + loss notes**; penalties to **R** only; **F/G invariant** (USM/KD‑CAL). 
* **Comparability** of a discipline flows **only through** the discipline’s **CG‑Spec** entries (no ad‑hoc formulas).  
* Cross‑Context/Tradition reuse **MUST** use **Bridge(s)** with **CL** and loss notes; **CL penalties route to R** (KD‑CAL/B.3); **F/G remain invariant**.  
* Public naming surfaces obey **LEX** (I/D/S; twin labels; banned heads); “discipline column” is **didactic only** and **carries no semantics** (enforced by LexicalCheck).

#### 4.3 Constructor **Γ_disc** (CAL export)
*Signature.*  
`Γ_disc : ⟨EpistemeCanon, StandardsSet, OrgCarriers, {Bridges}, Policy⟩ → U.Discipline`  
*Intent.* Fold the three constituents into a `U.Discipline`, **preserving provenance**, publishing UTS cards, and enabling lawful comparability via referenced **CG‑Spec** rows.  
*Obligations.*  
1) **Provenance & lanes.** Each imported episteme/standard declares **A.10 anchors** and lane tags **{TA, VA, LA}**; freshness windows are recorded.  
2) **Assurance fold.** Use KD‑CAL weakest‑link on R with **Φ(CL)** (and, where applicable, **Φ_plane** for ReferencePlane crossings) **table‑backed and monotone**; publish policy ids. For any justification **path P**, compute **`R_eff(P) = max(0, min_i R_i − Φ(CL_min(P)))`**; for parallel independent lines to the *same* claim take **`R(Γ) = max_P R_eff(P)`**; **`F(Γ)=min`** along used paths. No thresholds inside CHR/CAL (Acceptance‑only). Unknowns propagate as {pass|degrade|abstain} to Acceptance. 
3) **CG‑Spec guard.** Any numeric comparison/aggregation in Discipline reports **MUST** cite the discipline’s **CG‑Spec** with lawful **Gauge/Γ‑fold** and **MinimalEvidence**; units/scale/polarity legality via **MM‑CHR/CSLC** precedes aggregation.  
4) **Scale/Unit/Polarity legality.** Before any comparison/aggregation, **prove legality via MM‑CHR/CSLC** and cite **CG‑Spec characteristic ids** used in the fold (A.17–A.19).
5) **ReferencePlane guard.** When crossings touch `world|concept|episteme`, apply **CL_meta** and route penalties to **R** only; record **plane** on the UTS row.
6) **Edition discipline.** Changes to canons/standards that alter computed ⟨F,G,R⟩ **create a new edition**; DRR captures the rationale; UTS lifecycle records transitions.  
7) **No stealth globalisation.** Cross‑Context mappings are **by Bridge only**; “by‑name reuse” is forbidden** even with similar labels.

#### 4.4 Discipline ESG (state graph, informative surface)

Export a **Discipline.ESG** with named states and guarded transitions (e.g., *Emerging → Consolidating → Codified → Fragmenting*), where **guards reference C.21 metrics** (CHR‑typed; **Scale/Unit/Polarity + freshness windows**) and cite **CG‑Spec ids**; **all thresholds live only in AcceptanceClauses** (G.4). ESG is **descriptive**; all gating remains in CHR/CAL/LOG packs.

### 5 · Archetypal Grounding *(Tell–Show–Show)*

| Slot | **System** (safety code in a factory) | **Episteme** (discipline canon across editions) |
|---|---|---|
| **Object** | Production line with hazardous operations | “Safety engineering” as *describedEntity target* (accident models, tolerable risk) |
| **Concept** | Acceptance clauses & evaluation templates bound to rigs/windows | Canon texts: causality models, design rules, proofs/benchmarks (e.g., **formal knowledge bases**, **proof artefacts**, **concept schemas**) |
| **Symbol** | Local SOP/notation sets for checklists | Notation packages (CLIF, RDF/TriG, proof scripts) |
| **Γ_disc assembly** | Fold {line‑specific standard, plant procedures, certifying unit} into **`Discipline: Safety‑Plant‑A`** | Fold {canon papers, formal models, journals/committee} into **`Discipline: Safety‑Engineering`** with **Traditions** (e.g., system safety vs resilience engineering) |
| **Evidence lanes** | LA test campaigns (freshness windows), VA design proofs, TA tool quals | VA proofs over kinds, LA replications/meta‑analyses; TA for checkers |

### 6 · Bias‑Annotation
**Lenses:** Governance (naming/UTS), Architecture (CAL+CHR split), Onto/Epist (discipline ≠ domain; triangle fidelity), Pragmatic (authoring/editions), Didactic (twin labels; System/Episteme scenes). **Scope:** context‑local; no “global discipline”.

### 7 · Conformance Checklist (normative)
| ID | Requirement | Purpose |
|---|---|---|
| **CC‑C20‑1 (CG‑Spec linkage).** | A `U.Discipline` **SHALL** declare the **CG‑Spec** ids and **CHR characteristic ids** behind any comparison/aggregation; thresholds live only in **Acceptance** clauses referenced by those CG‑Specs. | Auditable comparability; no illegal ops. |
| **CC‑C20‑2 (Bridge‑only reuse).** | Any cross‑Context/Tradition use **SHALL** cite **Bridge id + CL + loss notes**; penalties **route to R only**; **F/G invariant**. | Prevent silent globalisation; align with KD‑CAL. |
| **CC‑C20‑3 (ReferencePlane).** For any crossing touching `world|concept|episteme`, **publish plane** and apply **Φ(CL)** (and **Φ_plane**, where applicable) — both **MUST** be **monotone, bounded, table‑backed**; **unknowns** propagate as **{pass|degrade|abstain}** into **Acceptance** with **SCR note**; **no silent `unknown→0`**. |
| **CC‑C20‑4 (Γ_disc integrity).** | `Γ_disc` **MUST** record lane tags and freshness windows for all imported evidence; **Φ(CL)** **MUST** be monotone and table‑backed per policy. | Deterministic assurance; hygiene of penalties. |
| **CC‑C20‑5 (Edition & DRR).** | Discipline editions **SHALL** be recorded via **UTS lifecycle** with DRR links; no silent rewrites or renames. | Traceable evolution. |
| **CC‑C20‑6 (LEX/I‑D‑S).** | `U.Discipline` names **SHALL** follow **LEX** (twin labels; registers; banned heads). **Domain** mentions are catalog‑only. | Register hygiene; avoid “Domain = Discipline”. |
| **CC‑C20‑7 (ATS hooks).** | Any **Tier‑crossing reference** in Discipline materials **SHALL** pass **AH‑2 GateCheck**/**AH‑3 LaneCheck**/**AH‑4 LexicalCheck** (E.11/G.13) and publish a **UTS row** for the crossing (_no implicit crossings_). |
| **CC‑C20‑8 (Discipline column is didactic).** | Any use of a “discipline column” in tables is **didactic only**; semantics are carried by **UTS rows + Bridges**; **Domain** remains a catalog stitch (**E.10/F.17**). |  |
| **CC‑C20‑9 (Lexical firewall).** | Normative sections remain **notation/tool‑neutral**; vendor/tool tokens are avoided (see **E.5.1**). |  |

#### 7.1 Canonical rewrites (anti‑ambiguity)
* “TDD discipline” → **`Tradition: Test‑Driven`** *(Plain twin keeps “Tradition”)*.  
* “Safety Discipline Owner” → **`Holder#DisciplineStewardRole:Safety‑Context`**.  
* “ClinicalSafetyDomain Governance” → **`DisciplineSpec: Clinical‑Safety`** with comparability in **CG‑Spec**; the **Domain** mention remains a **D.CTX + UTS** catalog stitch.

### 8 · Consequences
**Benefits.** Auditable field composition; lawful federation across traditions; selector‑ready maturity/evidence linkage; didactic surface for stewardship.  
+**Trade‑offs.** Discipline authoring requires CG‑Spec literacy and Bridge hygiene; paid back by safe reuse and clearer governance.

### 9 · Rationale
The calculus keeps **describedEntity local**, **comparability lawful**, and **assurance explicit**. It aligns with KD‑CAL’s weak‑link folds and CL routing, with CG‑Spec’s gauge/Γ‑fold Standard, and with LEX twin‑label governance. It avoids “phlogiston disciplines” by tying fields to measurable CHRs (C.21) and evidence lanes.

### 10 · Relations
**Builds on.** KD‑CAL (C.2); CG‑Spec (A.19/G.0); Bridges (F.9); LEX (E.10).  
**Coordinates with.** C.21 (field‑health CHRs), C.22 (Problem‑CHR), C.23 (Method‑SoS‑LOG).  
**Constrains.** G.2 **MUST** publish **TraditionCards**/**BridgeMatrix** sufficient for `Γ_disc` to assemble **≥2 Traditions** and **≥3 `U.BoundedContext`** per SoTA synthesis to avoid monoculture. G.5 selector **SHALL** cite Discipline **CG‑Spec ids** and **EvidenceGraph** rows when admitting families.


---

## C.21 — **Discipline-CHR · Field Health & Structure**  \[A] 

> *Purpose.* Give FPF a **typed, auditable** way to speak about the *health, maturity, and structure* of a scientific/engineering **discipline**, without collapsing into taste, anecdotes, or single-number scores. The pattern defines a **portable set of Characteristics** and guards (legality, freshness, scope) that any Context can specialize.

*This pattern supplies the CHR “vocabulary of health” for disciplines. C.20 composes the discipline; C.21 measures its health; Part G (G.2, G.12) harvests SoTA and operationalizes dashboards; Bridges keep meaning honest; penalties touch **R** only.*

 **Status & placement.** Part C (Architheory Specifications) → Cluster C.I (Core CHRs/CALs). 
  **Depends on:** **MM-CHR** (C.16), **KD-CAL** (C.2), **USM/Scope** (A.2.6), **Trust & Assurance** (B.3), **E.10 (LEX‑BUNDLE)**. 
  **Coordinates with:** **C.20 Discipline‑CAL** (what a `U.Discipline` is), **G.2** (SoTA palette), **G.12** (dashboard), **G.0** (CG‑Spec registry).

### 1 · Problem Frame

FPF treats *disciplines* as first-class holons (see **C.20**): they aggregate epistemes, practices, standards, institutions, and observed Work. Teams routinely say “the field is fragmented,” “standards are converging,” or “replication is improving,” but these claims are rarely **typed** (scale/unit/polarity) or **auditable** (evidence lanes, freshness, scope). C.21 supplies the CHR layer—named Characteristics with CSLC typing—so disciplines can be compared lawfully (CG‑Spec) and monitored through time (G.12).  Each published value MUST declare ReferencePlane ∈ {world|concept|episteme} and DisciplineId (U.Discipline@UTS); cross‑plane use applies CL^plane in Assurance (penalty to R_eff only). 

### 2 · Problem

Narrative health claims cause three recurrent failure modes:

1. **Illegality.** Averaging ordinals, mixing units, or comparing incommensurate Contexts ⇒ nonsense roll-ups.
2. **Staleness.** Health “scores” rarely declare **freshness windows** or evidence lanes (TA/VA/LA).
3. **Scope slippage.** “The field” is left implicit; cross-Context reuse lacks **Bridges & CL**, leading to silent semantic loss. Any numeric comparison/aggregation MUST cite a **CG‑Spec** row (characteristics, lawful gauge/Γ‑fold, MinimalEvidence) before computation.

### 3 · Forces

| Force                            | Tension                                                                                                                    |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Comparability vs nuance**      | Need global pictures without erasing local meaning (Context, traditions, cohorts).                                         |
| **Ordinal vs interval/ratio**    | Powerful stats tempt illegal ops on ranks and categories.                                                                  |
| **Local evidence vs federation** | Health must be computed *in room* (Context slice) yet projectable across rooms via Bridges & CL (penalties to **R** only). |
| **Recency vs stability**         | Health evolves; dashboards must reflect **freshness**, not just cumulative history.                                        |

### 4 · Solution — **Discipline Health Characterisation (DHC)**

#### 4.0 · Ontology quick sheet (normative, clarifying)
**What “DHC” is.** DHC is a **CHR vocabulary pack** (intensional) that defines **Characteristics** + **Scales/Units/Polarity** for discipline health; it is not a document or a run.
**Artifacts.**
• **`U.DHCPack`** (I‑layer name; published as an episteme): the **slot set** (Characteristic/Scale declarations) for a Context.  
• **`U.DHCMethodSpec`** (S‑layer): the **computational specification(s)** for deriving each DHC slot (e.g., replication‑window definition, CD‑index class), table‑backed; multiple per slot allowed, editioned separately.  
• **`U.DHCSeries`** (episteme w/ `EditionSeries`): a **time‑indexed publication** of computed DHC readings for a Discipline×Context, each value bound to `…Ref.edition` for every referenced method/metric/distance.
**Edition subjects.**  
(i) **DHCPack.edition** — when the **slot semantics** (Characteristic/Scale) change.  
(ii) **DHCMethodSpecRef.edition** — when a **computation method** (formula/class/policy) changes.  
(iii) **DHCSeries.edition** — when the **published series** changes its content (not carriers).  
**Publication.** Releases are **Work** on Carriers; **no** edition change unless content changes per `U.EditionSeries`.  
**Ref discipline.** All bindings to packs/methods/distances **SHALL** use `…Ref.edition` (dot on the Ref).

Define a **portable minimal set** of CHR **slots**. Each slot is **CHR-typed** (Characteristic, Scale/Unit/Polarity per **A.17–A.18**), **Context-local**, and guarded by **USM** (Claim scope **G**), **freshness windows**, and **evidence lanes** (TA/VA/LA).  Contexts MAY extend the set; MUST NOT alter scale types illegally. 

**“Health” is a vector** of CHR‑typed coordinates; **no single scalar** is implied. Lawful scalarization lives in **Acceptance** (G.4) with an explicit gauge/Γ‑fold and is never embedded in CHR.

#### 4.1 Core Characteristics (kernel-portable names)

1. **ReproducibilityRate** *(ratio ∈ [0,1]; polarity ↑; ReferencePlane=episteme; CG‑Spec‑bound)*
   Fraction of tested claims/benchmarks that independent teams **replicate** under a declared **ContextSlice** and **Γ\_time** window. **Lane tags:** LA (validation) with TA (typing) for protocols.

2. **StandardisationLevel** *(ordinal; polarity ↑; ReferencePlane=episteme)*
   {none, *emerging*, *de facto*, *de jure*}. **No mean.** Use medoid/mode; legal comparisons are ≤/=/> only. Tracks convergence on vocabularies, interfaces, or procedures.

3. **AlignmentDensity** *(ratio; polarity ↑; ReferencePlane=episteme; CG‑Spec‑bound)*  
   Density of **Substitution Bridges** (same **senseFamily**, CL≥2) between major `U.Tradition`s **per 100 DHC‑SenseCells** (G.2 F‑hooks) in the SoTA palette.  Substitution rule:  free substitution permitted at **CL=3**; at **CL=2** substitute only with extra‑guard (count in reporting, but this is not «free substitution») Units: `bridges_per_100_cells`. Cross‑Context use requires Bridge+CL; penalties → **R_eff** only.

 4. **DisruptionBalance** *(interval; polarity = target band; ReferencePlane=episteme; CG‑Spec‑bound)*  
  Relative share of **disruptive vs consolidating** works within **Γ_time** using a **registered CD‑index class** (editioned; cite **method id** in UTS). **Default plane:** *episteme*. Publish the **target band** via **Acceptance (G.4)**; not in CHR.
   
  5. **EvidenceGranularity** *(Context-declared: ordinal|ratio; polarity ↑; ReferencePlane=episteme)*  
   If ratio: units = `claims_per_artifact` or `anchors_per_claim` (declare). If ordinal: publish level names and **ORD_COMPARE_ONLY**.
   Fineness of evidential units and declared envelopes (experiment cards, benchmark tasks, audit granules). Encourages *smaller, well-scoped* claims over monoliths.

  6. **MetaDiversity** *(portfolio dispersion; polarity ↑ to band; ReferencePlane=episteme; CG‑Spec‑bound)*  
  Use entropy/HHI **over MethodFamily/Tradition shares** (method edition id в UTS); publish **guard‑band** as **Acceptance** binding; cross‑ordinal scalarisation is forbidden.
  Entropy/Herfindahl-type dispersion across `U.Tradition`s, method families, or data regimes, bounded by a **Context-declared guard-band** (too low ⇒ monoculture; too high ⇒ incoherence).

> **Typing & legality.** Each slot **MUST** declare **Scale/Unit/Polarity**; illegal ops (e.g., mean on ordinals; unit mixing) are **fail-fast** per **A.18/MM-CHR**.

#### 4.2 Guard Macros (normative)

* **ORD\_COMPARE\_ONLY(x)** — for **StandardisationLevel** (ordinal).
* **UNIT\_CHECK(x)** — forbid cross-unit aggregation (AlignmentDensity, ReproducibilityRate).
* **POLARITY_CHECK(x)** — enforce declared polarity (↑/↓/target-band) per MM‑CHR.
* **FRESHNESS(x; window)** — ensure values come from evidence within declared **Γ_time**; record **valid_until**; stale ⇒ {degrade|abstain} at Acceptance.
* **PLANE_NOTE(x)** — record **ReferencePlane**; compute **CL^plane** on crossings; penalties → **R_eff** only.
* **LANE\_TAGS(x; {TA|VA|LA})** — annotate contribution lanes.
* **SCOPE\_COVERS(x; TargetSlice)** — enforce **USM** coverage of the computation.
* **BRIDGE_CL(x; id, CL≥k)** — on cross‑Context roll‑ups, require **Bridge** with **CL**; penalties route to **R** only. If planes differ, apply **CL^plane** and cite **Φ_plane** policy id. **Hint:** for **AlignmentDensity** reporting, set **k=2** (CL≥2); **CL=3** counts as *free substitution*.

#### 4.3 Legality Matrix (extract)

| Operation     | ReproducibilityRate (ratio) | StandardisationLevel (ordinal) | AlignmentDensity (ratio) | DisruptionBalance (interval) |
| ------------- | --------------------------: | -----------------------------: | -----------------------: | ---------------------------: |
| mean          |                      **OK** |                     **FORBID** |                   **OK** |                       **OK** |
| median        |                          OK |                         **OK** |                       OK |                           OK |
| compare (<,>) |                          OK |                         **OK** |                       OK |                           OK |
| unit mix      |                  **FORBID** |                            n/a |               **FORBID** |                          n/a |

*Note:* For **MetaDiversity/EvidenceGranularity (ordinal)** use **median/mode**; forbid affine ops; unit mix always fails.

### 5 · Interfaces & Data Paths

* **Inputs.** `U.Discipline` from **C.20** (composition), SoTA **Palette**/**BridgeMatrix** from **G.2** (**DHC‑SenseCells** included), EvidenceProfiles from **G.4/G.6**.
* **Outputs.** Per‑Context **DHC rows** (these six slots), **UTS** Name Cards with twin labels (E.5/F.17–F.18), **Registry/RSCR hooks** on method edition changes; feeds **G.12** (time‑series).
* **Cross-Context reuse.** Only via **F.9 Bridges** with **CL** and **loss notes**; **Φ(CL)** penalties applied to **R** (never F/G).

### 6 · Archetypal Grounding (three fields)

#### 6.1 Computer Vision (Benchmarks 2015→)
* **ReproducibilityRate.** Ratio of independently reproduced results on ImageNet-style tasks within **rolling 24 mo** (LA lane).
* **StandardisationLevel.** *de facto* for dataset specs and metrics in *Vision\_2024*; *emerging* for robustness protocols.
* **DisruptionBalance.** Use an editioned CD‑index class (e.g., Wu‑style disruption family) with method id; publish target band via Acceptance; annotate ReferencePlane=episteme.
* **AlignmentDensity.** Bridges with **CL≥2** across sub-traditions (supervised vs self-supervised).
* **MetaDiversity.** Entropy across method families (CNN/ViT/Hybrid) kept within guard-band to avoid monoculture.

#### 6.2 Biomedicine (Gene–Disease Associations)
* **ReproducibilityRate.** Fraction of associations replicated in independent cohorts within **Γ\_time(36 mo)**; LA lane with TA (typing of protocols).
* **StandardisationLevel.** *de jure* for certain reporting guidelines; *emerging* for pre-registration norms.
* **EvidenceGranularity.** Move from “paper-level” to *claim-level* units (Context raises the score).
* **DisruptionBalance.** Target band discourages sustained “novelty spikes” unbacked by replication.

#### 6.3 Software Performance Engineering (SPE)
* **StandardisationLevel.** *emerging* → *de facto* for SLO taxonomies and trace schemas across vendors.
* **AlignmentDensity.** CL-rated Bridges between tracing ecosystems.
* **ReproducibilityRate.** Share of publicly replicable perf claims in rolling windows.
* **MetaDiversity.** Balance across load models, failure modes, and toolchains.

#### 6.4 Decision‑Making (2015→)
• ReproducibilityRate — share of causal effect estimates replicated across independent datasets within Γ_time; LA lane.
• StandardisationLevel — *emerging* for identification checklists; *de facto* for SCM notation in leading stacks (ordinal; no means).
• AlignmentDensity — CL‑rated Bridges between SCM/DoWhy‑style and RL/BO traditions per 100 DHC‑SenseCells.
• MetaDiversity — dispersion across method families (SCM/RL/BO/DT) within guard‑band; entropy/HHI (units declared in CG‑Spec).

#### 6.5 Evolutionary Architecture (software)
• ReproducibilityRate — fraction of architecture fitness results reproduced on independent workloads (rolling 18–24 mo; LA lane).
• StandardisationLevel — *de facto* for ADR/ATAM patterns; *emerging* for continuous fitness protocols.
• AlignmentDensity — Bridges across ATAM/SAAM/ADR style guides (CL≥2) normalised per 100 DHC‑SenseCells.
• MetaDiversity — portfolio dispersion across patterns (microservices, event‑driven, layered) with guard‑bands; no ordinal arithmetic.

### 7 · Measurement & Publication Procedure (authoring harness)

1. **Declare Context & TargetSlice.** (USM) Name editions, Standards, env params, `Γ_time`.
2. **Collect evidence.** Bind sources via **G.6 EvidenceGraph**; tag lanes and freshness.
3. **Compute DHC slots.** Enforce **Legality Matrix** and Guard Macros.
4. **Bridge (if needed).** Map via **F.9**; attach **CL** and **loss notes**; apply **R** penalties.
5. **Publish to UTS.** Name Cards (Tech/Plain), twin labels; **bind `DHCMethodSpecRef.edition`**, `DistanceDefRef.edition`, and, where templates are used, `DHCMethodRef.edition`; register RSCR triggers (method change, gauge edits).
6. **Dashboard.** Feed G.12 with time-series and guard-bands (disruption, diversity).

### 8 · Bias-Annotation (E-cluster lenses)

* **Didactic.** Plain names + twin labels; one-screen tables for managers.
* **Architectural.** No ordinals averaged; all cross-Context movement goes through Bridges+CL; penalties never touch F/G.
* **Pragmatic.** Freshness-aware; unknowns tri-state; values are decision-support, not trophies.
* **Epistemic.** Evidence lanes explicit; reproducibility is LA, typing is TA; validation distinct from verification in dashboards.

### 9 · Conformance Checklist (normative)

**CC-C.21-1 (CHR typing).** Every DHC slot **MUST** declare **Characteristic + Scale/Unit/Polarity**, with CSLC legality proved before any aggregation.
**CC-C.21-2 (Freshness).** Published values MUST carry Γ_time selector and freshness window; stale rows escalate to {degrade|abstain} in **G.4 Acceptance**.
**CC-C.21-3 (Plane).** ReferencePlane declared; cross‑plane re‑use publishes **CL^plane** (policy id) alongside CL; both penalties route to **R_eff**.
**CC‑C.21‑4 (DesignRunTag).** Every DHC row SHALL declare **DesignRunTag ∈ {design, run}**; design‑ и run‑characteristics **not mixing** in one value/aggregate.
**CC-C.21-5 (Lane tags).** Each value **MUST** tag **TA/VA/LA** lanes of contributing evidence.
**CC-C.21-6 (Ordinal discipline).** **StandardisationLevel** is ordinal; **no means**, **no z-scores**.
**CC-C.21-7 (Scope).** All computations declare **TargetSlice**; **USM** membership is decidable and deterministic.
**CC-C.21-8 (Bridges).** Cross-Context comparisons/publishers **MUST** cite **Bridge id + CL**; penalties route to **R\_eff**, never to F/G.
**CC-C.21-9 (UTS).** Publish DHC rows as **UTS Name Cards** with **twin labels** (Tech/Plain).
**CC‑C.21‑10 (Registry).** DHC methods are table-backed; silent method changes are forbidden (**bump `DHCMethodSpecRef.edition` + RSCR trigger**). 
**CC-C.21-11 (Unknowns).** Unknown inputs propagate tri-state {pass|degrade|abstain} to Acceptance; **no `unknown→0` coercion**.
**CC-C.21-12 (No tool/vendor tokens).** Core narrative follows **E.5.1** (Lexical Firewall).
**CC-C.21-13 (CG‑Spec citation).** Any numeric operation (comparison/aggregation) in DHC **MUST** refer to **CG‑Spec** (characteristics, gauge/Γ‑fold, MinimalEvidence).
**CC-C.21-14 (Φ‑policies).** **Φ(CL)** и **Φ_plane** — **monotone** and **table‑backed**; published by policy id.
**CC‑C.21‑15 (Ref discipline).** Any edition pinning **SHALL** appear as `…Ref.edition` on the relevant reference field (DHCPack/MethodSpec/DistanceDef/DHCMethodRef); bare `…Edition` fields are non‑conformant.
**CC‑C.21‑16 (Role kit, informative).** Use standard roles from F.4: `DisciplineStewardRole` (governs DHCPack), `DHCMethodAuthorRole`, `DHCSeriesPublisherRole`. Roles are **design‑time**; values are **run‑ or design‑stance** per slot and must declare **ReferencePlane**.

### 10 · Consequences

**Benefits.** Lawful comparisons; freshness-aware governance; explicit cross-tradition alignment; dashboards that don’t lie by averaging ranks.
**Costs.** Some ceremony (scales, windows, lanes, bridges), offset by template macros and UTS automation.
**Risks avoided.** “Phlogiston disciplines” (charisma-driven fields) fail DHC audits; **No-Free-Lunch** preserved by G.5 (selector returns sets, not universal scalars).

### 11 · Rationale (post-2015 signals & practice)

* **Replication & credibility (2015→).** Field-level health in SciSci emphasizes **replicability**, *fresh* evidence windows, and claim-level units—captured by **ReproducibilityRate** and **EvidenceGranularity**.
* **Disruption vs consolidation (2019→).** Empirical “disruption indices” distinguish papers that open new lines from those that refine—hence **DisruptionBalance** with *target bands*, not monotone “more is better.”
* **Standardization waves (2016→).** Package/ecosystem norms show ordinal trajectories (none→emerging→de facto→de jure); **ordinal typing** prevents illegal arithmetic.
* **Plural traditions (ongoing).** Mature fields maintain **bridges** with explicit **loss notes**; **AlignmentDensity** rewards CL-rated bridges without semantic collapse.

*(Names are illustrative of contemporary practice; the CHR is notation-agnostic and tool-neutral.)*

### 12 · Relations

* **Builds on:** **A.17–A.18** (Characteristic/CSLC), **A.2.6** (USM scopes), **B.3** (assurance lanes), **C.16** (MM-CHR templates).
* **Coordinates with:** **C.20** (what a `U.Discipline` *is*), **G.2** (SoTA palette and BridgeMatrix), **G.12** (Dashboard operationalization), **G.9** (parity harness for fair comparisons).
* **Constrains:** **G.10** (pack ships DHC rows + method ids), **G.11** (refresh windows/decay), **G.5** (selector may reference DHC only via admissible predicates; no cross‑ordinal scalarisation). **Coordinates:** **F.9** (Bridges for cross‑Tradition comparisons).

### 13 · Annex — Author’s quick template (copy-paste)

```
C.21.DHC(Context: <name/edition>; TargetSlice: <tuple>; Γ_time: <policy>)
  ReproducibilityRate:
    value: <0..1>   lane: LA   window: <…>   scope: <…>
  StandardisationLevel:
    value: {none|emerging|de_facto|de_jure}   compare_only: true
  AlignmentDensity:
    value: <ratio>   units: bridges_per_100_DHC_SenseCells   CL_min: 2   scope: <…>
  DisruptionBalance:
    value: <−1..1>   method: <CD-index class / edition>   target_band: [l,u]
  EvidenceGranularity:
    value: <ordinal|ratio per Context>   notes: <…>
  MetaDiversity:
    value: <entropy/HHI>   target_band: [l,u]
Guards: ORD_COMPARE_ONLY(StandardisationLevel), UNIT_CHECK(*), FRESHNESS(*), LANE_TAGS, SCOPE_COVERS, BRIDGE_CL(if x-Context)
Publish: UTS twin labels; RSCR triggers on method edition change.
```

---

## C.22 — **Problem‑CHR · Problem Typing & TaskSignature Binding**  \[A] 

**Purpose.** Give FPF a **lawful, minimal, and portable** way to speak about “the problem we face” so that the **selector** (G.5) can legally admit/abstain without prose or guesswork. We do this by (i) **typing problems** with CHR‑grounded traits and (ii) **binding** them to a **TaskSignature (S2)** that downstream architheories can consume. The Standard is **Context‑local**, evidence‑anchored, tri‑state‑aware, and bridge‑savvy. TaskSignature is *minimal* but sufficient for **eligibility**, **acceptance**, and **policy‑governed** choice. 

**Status & placement.** Part C (Architheory Specifications) → Cluster C.I (Core CHRs/CALs).
**Depends on:** **C.16 MM‑CHR** (measurement legality), **G.5** (selector S2/S3), **G.0** (CG‑Spec invariants).
**Coordinates with:** **G.4** (Acceptance/Evidence profiles), **C.23** (MethodFamily admissibility & maturity), **C.18 NQD‑CAL** (QD/illumination), **C.19 E/E‑LOG** (emitters/policies), **E.10** (LEX).

### 1) Intent

Operationalise No‑Free‑Lunch discipline in selection by ensuring every run‑time decision sees a **typed TaskSignature (S2)**, not a paragraph, and that **“problem”** (method unknown) is cleanly separated from **“task”** (method known; signature bound). The signature is the **smallest CHR‑typed set** sufficient to drive **Eligibility → Acceptance → policy‑governed selection** without illegal arithmetic or silent coercions; crossings are auditable (Bridge+CL → **R_eff only**).

### 2) Problem Frame (design/run split; ATS‑aware)

**method‑first stance**
In FPF a **Problem** exists when a Holder or external **Transformer** cannot cite a known **Method** (or specialisation thereof) that satisfies the current **TaskSignature** under the declared **ScopeSlice(G)**. Problem‑solving therefore entails **strategizing** (selecting or synthesising a method). The resulting **strategy/policy** is a composition under **G.5/E/E‑LOG** and **is not** a new kernel type.  
**Unknown‑first discipline.** Author S2 with `unknown` traits rather than coercions; **SoS‑LOG** branches MUST specify `{admit|degrade|abstain|sandbox}` handling for `unknown` via closed enums registered at UTS.

Un‑typed “problems” collapse into **informal prose**; selectors cannot **filter/abstain** lawfully; thresholds leak into scoring; cross‑Context reuse is by name, not Bridge. We need a Context‑local descriptor that (i) obeys **MM‑CHR legality** (Scale/Unit/Polarity proven before any aggregation), (ii) records **Assurance lanes (TA/VA/LA)** per **A.10** and **ReferencePlane**, (iii) carries **tri‑state unknowns** explicitly, and (iv) **publishes ATS crossings** (Bridge + UTS) with **Φ(CL)/Φ_plane policy ids**.

### 3) Problem

Without typed descriptors, **Eligibility/Acceptance** degenerate into prose; **illegal ops** creep in (ordinal means; unit mixing); **cross‑plane comparisons** lose **CL/Φ** routing (**penalties to R_eff only**). 

### 4) Forces

| Force                        | Tension                                                                                                                           |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Parsimony vs sufficiency** | Fewer fields to avoid ceremony **vs** enough to drive lawful gating.                                                              |
| **Unknowns**                 | Many traits are **unknown** at intake → tri‑state semantics must propagate to Acceptance without silent coercions.                |
| **CHR legality**             | **No mean on ordinals; no unit mixing**; polarity & scale type must be declared *before* aggregation.                             |
| **Locality vs portability**  | Problem is **in‑room**; still must cross **via Bridges**, with **CL** and (if planes differ) **CL^plane** penalties → **R** only. |

---

### 5) Solution — **Problem‑CHR** (fields) + **TaskSignature (S2) binding** *(normative)*

#### 5.1 Minimal CHR fields (tri‑state aware).
Each field is **CHR‑typed** (Characteristic/Scale/Unit/Polarity; MM‑CHR discipline). Every predicate admits `unknown` (tri‑state). Unknowns must propagate to {degrade|abstain|sandbox} per Acceptance/EvidenceProfile policy (recorded in SCR). (G.4/G.6 alignment)

* **`DataShape`** — data regime & admissible transforms (e.g., tabular, sequence, graph; density; stationarity claims).
* **`NoiseModel`** — uncertainty class / robustness envelope (e.g., iid Gaussian; heavy‑tailed; adversarial budget).
* **`ObjectiveProfile`** — objective heads (**Scale/Unit/Polarity** and **ReferencePlane** declared), polarity, and **lawful orders** (lexicographic, Pareto, medoid/median where legal). **Weighted sums across mixed scale types are forbidden**; ordinal heads use order‑only guards. For QD tasks, explicitly enumerate **Q (quality)**, **D (diversity)**, and **QD‑score** heads; see **DominanceRegime** below.
* `RegularityTraits` — method‑relevant structure (**convexity/differentiability/separability/monotonicity**) as CHR‑typed predicates with guard‑macros (e.g., `ORD_COMPARE_ONLY`, `UNIT_CHECK`, `POLARITY_CHECK`). Include `ConditionClass` (e.g., stiffness/κ‑proxies) where applicable.
* **`Constraints`** — explicit hard/soft constraint classes (feasibility predicates; **ResourceEnvelope**/**RiskEnvelope**). **Thresholds live in Acceptance (G.4) only; never inside CHR or code paths.**
* **`ShiftClass/Stationarity`** — CHR‑typed claims about regime stability (iid | covariate‑shift | concept‑drift | adversarial). Default=`unknown`. Acceptance/Flows MUST honor this in gating or abstain.
* `EvidenceGraphRef (A.10)` — carriers & **lane tags (TA/VA/LA)** with **freshness windows**; **no self‑evidence**; default Γ‑fold = **weakest‑link** unless CAL proves an alternative.
* `ScopeSlice(G)` — **USM** slice of **describedEntity/scope** to bound claims (discipline governance in **CG‑Spec**; Domain is a catalog mark only).
* `Size/Scale` — size/condition proxies (**n, m, κ, sparsity**) with **declared units**; unit mismatch ⇒ {sandbox|refuse}.
* **`Freshness`** — validity window for descriptors.
* `Missingness` — **MCAR/MAR/MNAR** (or mapped equivalents) per **CHR.Missingness**; MUST be honoured by Acceptance/Flows.
* `KindSet` — **`U.Kind[]`** of objects‑of‑talk addressed by the TaskKind; separates **describedEntity (Kind)** from **Scope (USM)**.

**QD / Illumination extensions (normative; ties to C.18/C.19).**
* **`CharacteristicSpaceRef`** — reference to **`U.CharacteristicSpace`**, with declared **d≥2**; **characteristics are CHR‑typed**; **ReferencePlane** per characteristic; pin edition via **`CharacteristicSpaceRef.edition`**.
* **`ArchiveConfig`** — archive **topology** (grid/CVT/graph), **resolution** (bins/centroids), **K‑capacity**, **`InsertionPolicyRef`** (elite replacement/dedup/novelty), and **`DistanceDefRef.edition`** (declare **metric/pseudometric** status and invariances; any normalisation **MUST** cite lawful scale transforms in **CG‑Spec**); legality follows CG‑Spec.
* **`EmitterPolicyRef`** — pointer to emitter/governor policy (C.19) applicable to this TaskSignature; **edition id** recorded.
* **`DominanceRegime`** — `{ParetoOnly | ParetoPlusIllumination}`. **Default = `ParetoOnly`** (illumination remains a gauge unless CAL explicitly authorises `ParetoPlusIllumination`, policy‑id cited).
* **`IlluminationSummary`** — a **gauge over `Diversity_P`**; **published** by default; excluded from dominance unless a CAL enables `ParetoPlusIllumination` (policy‑id cited).
* **`IlluminationMap`** *(parity‑run)* — required **publication artefact** (grid/CVT/graph per `ArchiveConfig`) recording coverage per niche/cell with `DescriptorMapRef`/`DistanceDefRef.edition`. **Leaderboards as single‑score lists are forbidden**; comparisons **MUST** be under CG‑frames.
* **`PortfolioMode`** — `{Pareto | Archive}`. **Default = `Archive`**: selectors **publish portfolios** (QD archives) rather than a single “best” set; ε‑fronts remain admissible for local decisions under CG‑Spec.
* **`Budgeting`** — evaluation/time/batch **budgets**, including **E/E‑LOG exploration budget** id; units declared (CG‑Spec).
* **`TelemetryHooks`** — **PathSliceId**, **decay/refresh policy ids**, and **edition counters** to record **U.DescriptorMap** and **policy‑id** updates upon illumination gains.
* **`GeneratorIntent`** (OEE) — optional intent to invoke a **`GeneratorFamily`** (G.5) with pointers to **`EnvironmentValidityRegion`**, **`TransferRulesRef`**, and **coverage/regret** reporting expectations.

**Legality.** Before any numeric comparison/aggregation, **prove CSLC legality** (Scale/Unit/Polarity) and **cite CG‑Spec.Characteristics**; publish **ReferencePlane**. **Unknowns** propagate as {degrade|abstain|sandbox}; **no `unknown→0/false` coercions**.

#### 5.2 TaskSignature (S2) — binding definition (design‑time + run‑time).
A TaskSignature is a minimal typed record the selector consumes:
`⟨Context, TaskKind, KindSet:U.Kind[], DataShape, NoiseModel, ObjectiveProfile, Constraints{incl. Resource/Risk Envelopes}, ScopeSlice(G), EvidenceGraphRef, Size/Scale, Freshness, Missingness, ShiftClass?, BehaviorSpaceRef?, ArchiveConfig?, EmitterPolicyRef?, DominanceRegime?, PortfolioMode?, Budgeting?, TelemetryHooks?, GeneratorIntent?⟩`


**Minimality rule.** S2 carries only fields required for **Eligibility→Acceptance→lawful selection**; any additional traits derived at design‑time are published as provenance (UTS) but **do not expand S2**. 

Values are **CHR‑typed** with **provenance**; traits may be **inferred** from CHR/CAL bindings (e.g., *convexity known? differentiable? ordinal vs interval scales?*) and from **USM** scope metadata. Unknowns are tri‑state; **Missingness semantics MUST align with CHR.Missingness** and be honored by Acceptance/Flows. 

**Design/Run hygiene.** Do not mix DesignRunTag in one signature; **publish ATS crossings** (Bridge + UTS) when importing design‑time traits into run‑time.

#### 5.3 Provenance & planes.
Record **Context**, **ReferencePlane** for each value; on any cross‑Context/plane reuse, attach BridgeDescription + UTS row, apply **CL** (and, if planes differ, **CL^plane**) penalties to **R_eff only**; both **Φ(CL)** and (if used) **Φ_plane** MUST be **monotone, bounded, and table‑backed**; **no “distance” language; penalties never mutate F/G.** Publish policy‑ids in SCR and cite Bridge ids on crossings.

#### 5.4 Binding & use.

* **Eligibility** gates read TaskSignature against each **MethodFamily.Eligibility** (C.23) and **CG‑Spec.MinimalEvidence** for referenced characteristics.
* **Acceptance** clauses (G.4) use these fields for **threshold predicates** (thresholds live in Acceptance only).
* **Selection kernel** (G.5.S3) applies a **lawful order** (often partial); **weighted sums across mixed scale types are forbidden**. If only a partial order remains, **return a Pareto (non‑dominated) set** with tie notes. If `PortfolioMode=Archive`, the selector **may** return a **QD archive** (per `ArchiveConfig`) **in addition to** or **instead of** a Pareto set. **Illumination** enters dominance **only** if `DominanceRegime=ParetoPlusIllumination` is **enabled by CAL** (policy id cited); otherwise, QD metrics are **reported** but **excluded** from dominance.
* When `GeneratorIntent` is present, G.5 may dispatch to a registered **`GeneratorFamily`** (POET‑class); the selection surface becomes **pairs** `{environment, method}`, with Environment guarded by **`EnvironmentValidityRegion`** and **`TransferRulesRef`** (C.23 wiring). Report **`IlluminationSummary`** as a **gauge over `Diversity_P`** in telemetry; dominance remains unaffected unless policy changes as above.

#### 5.5 Unknowns.
Every field supports `unknown`; downstream **degrade/abstain/sandbox** behavior is explicit per Acceptance/EvidenceProfile; no implicit coercions. 

#### 5.6 Publication.
Emit a **ProblemProfile** (…Description) that carries the bound TaskSignature, **UTS** Name Cards for any minted values (twin labels), and SCR‑visible provenance (A.10 anchors, lane tags, freshness, **ReferencePlane**). **Mark any vendor/tool examples as Plain‑register only (LEX V‑4); they are non‑normative.**

#### 5.7 Open‑Ended tasks (GeneratorFamily) *(normative)*.
If the problem requires **open‑ended generation** of tasks/environments, S2 **SHALL** include `GeneratorIntent` with pointers to **`EnvironmentValidityRegion`** (lawful support of generated environments), **`TransferRulesRef`** (cross‑environment transfer constraints), and **coverage/regret** telemetry expectations. Selector outputs are then portfolios over **{environment, method}**; **coverage** and **IlluminationSummary** are **gauges** (reported) unless **CAL** authorises their participation in dominance (see `DominanceRegime`). Edition increments of **CharacteristicSpaceRef.edition**/**DistanceDefRef.edition** and the **policy‑id** that caused illumination increases **SHALL** be recorded in SCR.


### 6) Archetypal Grounding (Tell–Show–Show)

*Tell–Show–Show hook (per E.8):* label examples as **Show‑1 (continuous ODE)** and **Show‑2 (MIP)** and cite CHR guard‑macros in‑line so engineers can see **which field drove which gate**.  **Explicitly annotate which S2 fields triggered each Eligibility/Acceptance decision** (e.g., `service_level@ordinal → ORD_COMPARE_ONLY`, `budget@ratio → unit alignment check`).

**A. Differential equations (continuous systems, solver choice).**
*ProblemProfile.* `DataShape=ODE, stiff?=unknown, Size/Scale={n≈10^3}, ObjectiveProfile={↓error@ratio, ↑throughput@ratio}, Constraints={budget≤X, safety_gate@ordinal}, RegularityTraits={Lipschitz known?=unknown, Jacobian sparsity=high}, Missingness=MAR`.
*Binding.* Selector reads TaskSignature; **eligibility** filters MethodFamilies that require known stiffness or differentiability (unknown ⇒ **degrade/abstain** per family); **Acceptance** enforces `safety_gate` as **ordinal predicate**, not averaged (ORD\_COMPARE\_ONLY), and budgets with **unit‑aligned sums** (ratio). The selector returns a **Pareto set**; no cross‑ordinal weighting.

**B. Mixed‑integer optimisation (planning/scheduling).**
*ProblemProfile.* `DataShape=MIP, NoiseModel=deterministic, ObjectiveProfile={↓cost@ratio, ↑service_level@ordinal}, Constraints={SLA hard, workforce soft}, RegularityTraits={convex_relaxation=available}, Size/Scale={vars~10^5}, Missingness=MCAR`.
*Binding.* **CG‑Spec** forbids means over **service\_level** (ordinal); **Acceptance** holds thresholds; **Eligibility** checks convex‑relaxation availability; **Selection** applies **lexicographic** guard (assumption‑fit ≻ evidence‑fit ≻ resource), compute **R\_eff** with Γ‑fold, route **CL** to **R** only; if partial order remains, return a **Pareto set**.

> *Contemporary anchors (informative):* modern **Julia** ecosystems illustrate the “**general call outside, specialised implementations inside**” ethos (e.g., DifferentialEquations.jl, JuMP), aligning with C.22→G.5 multi‑method dispatch under NFL.

**C. Quality‑Diversity portfolio (illumination).**
*ProblemProfile.* `DataShape=policy‑search; ObjectiveProfile={↑reward@ratio, ↑coverage@ratio (report‑only)}, DominanceRegime=ParetoOnly, PortfolioMode=Archive, CharacteristicSpaceRef(d=3, characteristics=CHR‑typed), ArchiveConfig(grid, res=32×32×16, K=1, InsertionPolicyRef=elite‑replace, DistanceDefRef.edition=v1), EmitterPolicyRef=v2, Budgeting{eval=1e6}, TelemetryHooks{PathSliceId=…}`.
*Binding.* Selector may return an **archive**; **coverage/illumination** are **reported** but **excluded** from dominance (default). Any change of `DistanceDefRef.edition`/Emitter policy is **editioned** and logged in SCR.

**D. Open‑ended environment generation (POET‑class).**
*ProblemProfile.* `GeneratorIntent{GeneratorFamilyRef=…, EnvironmentValidityRegion=… (CHR‑typed), TransferRulesRef=…, CoverageMetric=…}`, `PortfolioMode=Archive`.
*Binding.* Selector outputs **{environment, method}** pairs that pass Eligibility; **TransferRules** govern cross‑environment policy reuse; telemetry reports **coverage/regret** and **IlluminationSummary** with **edition/policy‑id** when improved.

### 7) Bias‑Annotation (LEX/discipline guards)

* **No minted “Strategy” head.** “Strategy/policy” are *roles/lenses* inside G.5; do **not** introduce a new `U.Type` “Strategy”.
* **No minted `U.Type` “Strategy”.** Strategy/policy are roles/lenses inside G.5 Compose under E/E‑LOG; keep “strategy” as Plain where pedagogically needed.
* **Transdiscipline vs domain.** Comparability flows through **`U.Discipline` CG‑Spec**; “Domain” is a catalog mark stitched to D.CTX + UTS; do **not** attach norms to Domain labels.
* **Plain twins & head‑anchoring.** Use Description/Spec morphology correctly (I/D/S; E.10.D2). 

### 8) Anti‑patterns (normative):
* **AP‑1** Pre‑binding a Method into S2 (“problem as if task”); **Remedy:** keep S2 method‑agnostic; bind only lawful traits.
* **AP‑2** Silent `unknown→false/0` in Eligibility/Acceptance.  
* **AP‑3** Cross‑ordinal averaging / ordinal–interval scalar mixes.  
* **AP‑4** **Design/run chimera** signatures (mixing stances).  
* **AP‑5** **Domain** treated as governance (attach governance to **U.Discipline/CG‑Spec**, not Domain).  
* **AP‑6** Implicit handling of data‑shift (assume iid); **Remedy:** declare `ShiftClass` (or `unknown`) and gate via Acceptance.
* **AP‑7** Tool/vendor tokens in normative text; **Remedy:** move to Plain‑register note; keep Tech anchors on CHR/CAL ids (LEX V‑4).

**Remedies:** tri‑state predicates; lawful orders (lexi/Pareto/median/medoid); ATS crossing with Bridge+CL; Domain stitched to **D.CTX + UTS** only.

### 9) Conformance Checklist (normative)

0. **Minimal S2.** S2 contains only fields necessary for Eligibility/Acceptance/selection; any extra derived traits remain provenance.
1. **TaskSignature present (S2).** All TaskKinds **publish** a TaskSignature with all fields declared and **CHR‑typed**; `unknown` supported for each.
2. **CHR legality proven.** Any numeric comparison/aggregation **cites CG‑Spec** by **Characteristic id** and proves **CSLC legality**; **no mean on ordinals; no unit mixing**.
3. **Unknowns propagate.** Unknowns **must** map to {pass|degrade|abstain} in **Acceptance**/**Eligibility**; no implicit coercions; behavior recorded in **SCR**.
4. **Evidence lanes.** **A.10 anchors** + **Assurance lanes (TA/VA/LA)** + **freshness windows** recorded; **Γ‑fold** default=weakest‑link unless proved otherwise.
5. **ReferencePlane guarded.**  ReferencePlane noted **per value and per ObjectiveProfile head**; on crossings apply **CL** (and **CL^plane** if planes differ); **Φ(CL)/Φ_plane** are **monotone, bounded, table‑backed and documented in the `CG‑Spec`**; penalties → **R_eff only** (F/G invariant).
6. **Acceptance thresholds live in CAL.** No thresholds in CHR or code paths; only in **G.4 AcceptanceClauses**. 
7. **Selector legality.** Selection uses **admissible (possibly partial) orders**; **weighted sums across mixed scale types are forbidden**; return a **Pareto set** when appropriate. 
8. **ATS crossings published.** Any AT0↔AT1↔AT2 reuse emits **BridgeDescription + UTS row** with CL notes and planes. 
9. **UTS twin labels.** All exported cards publish **Name Cards** with twin labels; Bridges carry loss notes. 
10. **ATS harness.** **AH‑1..AH‑4** (E.11) checks pass for: TierClassifier, GateCheck, LaneCheck, LexicalCheck on the published TaskSignature and crossings.
11. **QD fields (when QD is in scope).** If `PortfolioMode=Archive` or QD heads are present, **CharacteristicSpaceRef** (d≥2), **ArchiveConfig** (topology, resolution, K, `InsertionPolicyRef`, `DistanceDefRef.edition`), and **EmitterPolicyRef** **SHALL** be present and CHR‑typed; characteristics declare **ReferencePlane**.
12. **DominanceRegime default.** `DominanceRegime` **defaults to `ParetoOnly`**; inclusion of illumination in dominance **MUST** be enabled by a **CAL.Acceptance policy**; the policy id **SHALL** be published in SCR.
13. **Telemetry.** **PathSliceId**, **refresh/decay policies**, and **edition counters** for **CharacteristicSpaceRef**/**DistanceDefRef**/**EmitterPolicyRef** **SHALL** be recorded; any illumination increase **SHALL** log the **policy‑id** that triggered it.
14. **GeneratorIntent (when OEE is in scope).** `GeneratorIntent` **SHALL** cite **`EnvironmentValidityRegion`** and **`TransferRulesRef`** (ids resolvable in G.5/C.23); absence ⇒ `Abstain` for OEE dispatch.
15. **Budgets.** `Budgeting` (eval/time/batch) **SHALL** declare units and E/E‑LOG exploration budget id when used.
16. **Archive legality.** `DistanceDefRef.edition` and any novelty measures **SHALL** be CSLC‑lawful and **editioned**; illegal ops ⇒ **Abstain**.
17. **Planes.** **ReferencePlane** **SHALL** be declared for all QD heads/axes; plane crossings apply **Φ\_plane** (penalty to **R** only).
18. **Unknowns.** Unknown QD fields **map** to `{degrade|abstain|sandbox}`; no coercions.

### 10) Interfaces & Data Paths

+*Inputs.* `ProblemProfile` (…Description), CG‑Spec ids, Evidence Graph Ref (A.10), D.CTX; (if QD) CharacteristicSpaceRef/ArchiveConfig/EmitterPolicyRef configs; (if OEE) GeneratorIntent.
 *Produces.* `TaskSignature@Context` (S2) with provenance; **SCR‑visible** fields; UTS Name Cards for any minted traits; (if QD/OEE) archive/portfolio semantics and telemetry hooks declared.
 *Consumed by.* **G.5** (Eligibility/Selection kernel), **G.4** (Acceptance/Evidence), **C.23** (admit/degrade/abstain rules; maturity ladder).

### 11) Consequences (informative)

* **Lawful selection.** Dispatch is **explainable** and **audit‑ready**; every reason in/out cites TaskSignature fields, CG‑Spec rows, and Γ‑fold contributors. 
* **Local first, portable later.** Context‑local semantics are primary; Bridges make portability **deliberate and costed** (penalties to **R** only). 
* **Frictionless downstream.** G.1–G.5 consume a **single, typed** Standard; thresholds are cleanly separated into **Acceptance**; unknowns are not guessed.
* **QD/OEE‑ready.** Typed QD and GeneratorIntent fields make **portfolio** and **open‑ended** workflows **first‑class**, with lawful dominance, editioned distances, and policy‑aware illumination.

### 12) Relations

**Builds on:** **C.16 MM‑CHR**, **G.0 CG‑Spec**. **Coordinates with:** **G.4 Acceptance**, **G.5 Selector**, **C.18 NQD‑CAL**, **C.19 E/E‑LOG**, **C.23 Method‑SoS‑LOG**. **Constrained by:** **E.10 (LEX/I/D/S)**, **E.11 (ATS)**.

### 13) Author’s quick checklist

1. **Write the ProblemProfile.** Context, TaskKind, ObjectKinds, USM **ScopeSlice(G)**, describedEntity (GroundingHolon, ReferencePlane). 
2. **Fill TaskSignature (S2).** Populate all fields; mark `unknown` explicitly; align **Missingness** with CHR semantics. 
3. **Bind CG‑Spec ids.** For any numeric comparison/aggregation you expect downstream, cite **CG‑Spec.Characteristics** and prove **CSLC** legality. 
4. **Attach Evidence Graph Ref.** Lanes (TA/VA/LA), carriers, freshness windows; set **Γ‑fold** default; no self‑evidence. 
5. **Publish crossings.** If importing from other tiers/Contexts, mint **BridgeDescription + UTS row**; record **CL/CL^plane**; penalties **→ R only**. 
6. **Keep thresholds in Acceptance.** Move any thresholds (gate numbers) into **G.4**;  wire **RSCR** refusal tests (illegal ops; unit/scale checks; **tri‑state unknowns**; CL→R routing; **Φ tables present**).
7. **Run AH‑1..AH‑4** (ATS harness) on the signature and crossings; attach **UTS Name Cards** with twin labels.
8. **Bias audit.** Check E.5.4 and C.21 hooks if the problem lives *inside* a discipline dashboard or SoTA pack.

### 14) Goldilocks hook (design‑time)

When generating candidate solutions for a **TaskKind**, target **“goldilocks”** slots (feasible‑but‑hard) so that the TaskSignature is informative (neither trivial nor impossible); this aligns with **G.1** (target goldilocks, abductive provenance) and ensures the **TaskSignature is informative** (neither trivial nor impossible) for **G.5** selection.


---

## C.23 — **Method‑SoS‑LOG — MethodFamily Evidence & Maturity**  \[A]

*Architheory: LOG (deductive shells for admissibility)*
*First use expansion:* **SoS‑LOG = Science‑of‑Science LOG** (LEX short‑form discipline applied).

**HomeContext.** For this pattern, *HomeContext* means the `U.BoundedContext` where a `MethodFamily` is registered (LEX D.CTX).

**Builds on.** **G.5** (MethodFamily registry/selector), **G.4** (Acceptance & EvidenceProfiles), **C.22** (TaskSignature S2), **C.18 NQD‑CAL** (QD/illumination), **C.19 E/E‑LOG** (emitters/policies), **B.3** (Assurance lanes & `R_eff`), **A.10** (Evidence Graph Ref), **E.10** (LEX), **E.11** (ATS). **Coordinates with.** **G.6** (EvidenceGraph), **G.8** (LOG bundling), **G.9** (Parity), **G.11** (Refresh).     

### 1) Problem frame

Families of methods compete inside a CG‑Frame. The selector (G.5) must **admit, degrade, or abstain** per family **without** universal scores, using **typed** problem descriptors and **auditable** evidence. Maturity of a family (how far it has travelled from “clever idea” to “run‑safe”) must be **visible to LOG** rules yet **separate from thresholds** (which live only in **AcceptanceClauses**, G.4). 

### 2) Problem

Unstructured “readiness” stories and undisciplined evidence lead to:

* (i) **Illicit scalarisation** across mixed scale types,
* (ii) **Prose‑only** gating that a dispatcher cannot execute,
* (iii) Cross‑Context reuse without Bridges/CL, and
* (iv) Immature families leaking into production.
  We need a **notation‑independent LOG layer** that turns **TaskSignature (S2)** + **EvidenceProfiles** into **executable rules** for *admit / degrade / abstain*, **routing any CL penalties to `R_eff` only** (never mutating **F/G**). 

### 3) Forces

* **Pluralism vs. dispatchability.** Competing Traditions expose different invariants; selection must compare **without semantic flattening**.
* **Maturity vs. opportunity.** Open‑ended exploration (E/E‑LOG) must coexist with **run‑safe** exploitation; *immature ≠ forbidden* → provide safe **degrade** paths.
* **Unknowns (tri‑state).** Missing or `unknown` S2 fields must propagate **explicitly** to *degrade/abstain/sandbox*; no silent coercions.
* **Lexical discipline.** Head‑anchoring, I/D/S separation, Bridge hygiene; **no tool names in Core**.

---

### 4) Solution — **Method‑SoS‑LOG**: deductive shells over Eligibility & Evidence

#### 4.1 Objects & heads (LEX/I‑D‑S)

*Tech heads; Plain twins are published via UTS.*
**`MethodFamily`** (registered in G.5) carries **Eligibility** and artefact identity; **`MaturityCard`** (this pattern) carries evidence‑aware maturity; **`SoS‑LOG.Rule`** (this pattern) is an executable rule schema that returns one of `{Admit | Degrade(mode) | Abstain}` for a `(TaskSignature, MethodFamily)` pair. Descriptions live as `…Description`; when harnessed they become `…Spec`. 

#### 4.2 Rule schema (normative)

For each `MethodFamily` **f**, author an **executable** rule set:

```
LOG.Deduce_f(TaskSignature S2) → {Admit | Degrade(mode) | Abstain}
```

with the following **branch obligations**:

**R0 — CG‑Spec gate (precondition, HomeContext).** Before R1–R3, verify **CG‑Spec.MinimalEvidence** for every CHR characteristic referenced by *f*’s Acceptance/Flows **in the home Context**; failure ⇒ `Abstain` with reasons (no silent sandbox). Publish the **CG‑Spec ids** consulted. 
*Rationale:* selector legality requires the CG‑Spec gate to be explicit, not implicit in prose. Publish associated **ReferencePlane** notes alongside the consulted ids.

**R0.QD — QD/OEE pre‑gates (if applicable).** If S2 declares **BehaviorSpaceRef/ArchiveConfig/EmitterPolicyRef** or `PortfolioMode=Archive`, verify:
(i) **CharacteristicSpaceRef** characteristics are CHR‑typed, d≥2, **ReferencePlane** per characteristic declared;
(ii) **ArchiveConfig** is lawful (topology, resolution, **K**>0, `InsertionPolicyRef`, `DistanceDef` with **edition id** and declared metric/pseudometric status);
(iii) **EmitterPolicyRef** present (with **edition id**);
 (iv) **DominanceRegime** present; if absent, **default= ParetoOnly**.
 Failure of any ⇒ `Abstain` with reasons.

**R1 — Admit.** `Admit` **IFF**
(a) S2 satisfies **Eligibility** predicates of *f* (tri‑state aware),
(b) **EvidenceProfile minima** referenced by Acceptance/Flows for *f* are met (lanes/anchors/freshness) **in the home Context** (post R0),
(c) all relevant **CAL.AcceptanceClauses** (G.4) evaluate to true under lawful CHR comparisons,
(d) any **maturity gating** (e.g., a floor on Maturity rungs) is expressed as an **AcceptanceClause** and referenced here by id (no thresholds inside LOG).
*LOG never sets thresholds; it only executes and cites Acceptance verdicts.*

**R2 — Degrade.** If (a) holds but (b) or (c) is **partially** satisfied or **unknown**, return `Degrade(mode)` where `mode ∈ {scope‑narrow | sandbox | probe‑only}` and **emit scope notes** (USM Scope(G), Γ_time). Record which S2 unknowns or Evidence minima caused the degrade. **LOG‑Degrade** never changes **CHR scales or planes**; it **narrows Scope (G)** or **execution mode**. 
**Note (CAL vs LOG).** CAL‑level **`degrade.order`** (fall‑back to order‑only comparisons) is governed by **G.4**/**CG‑Spec** and is **not** a LOG mode. **SoS‑LOG never overrides CAL outcomes**; a LOG branch **only narrows** `Scope(G)` or **execution mode** (e.g., `sandbox`, `probe‑only`), it **does not** alter CHR scales or admissible orders.
`probe‑only` MUST cite an **E/E‑LOG policy id** (exploration budget) and Acceptance‑bound guards.

**R3 — Abstain.** If S2 violates **Eligibility** *or* **R0** fails, return `Abstain` (with reasons). **Abstain** is mandatory on **illegal CHR operations** (e.g., ordinal means) and when **Bridge/CL** requirements are unmet. 

**R4 — CL routing.** Any cross‑Context/plane reuse must cite **Bridge ids** (with loss notes). Apply **Φ(CL)** and (if planes differ) **Φ_plane** that are **monotone, bounded, table‑backed**; **publish policy‑ids** in the SCR; **penalties reduce `R_eff` only**; **F/G must remain invariant**.

**R5 — Proof hooks.** Every branch **MUST** cite **Evidence Graph Ref** (A.10), lane tags (TA/VA/LA), freshness windows, and (if bridged) **Bridge ids + loss notes**; the decision is **SCR‑visible**. When **G.6 EvidenceGraph** is present, also **publish EvidenceGraph path id(s)** for the branch (admit/degrade/abstain). **No self‑evidence**.

**R6 — QD portfolio semantics (if applicable).** If `PortfolioMode=Archive`, `Admit` may return a **QD archive** (per `ArchiveConfig`) instead of only a Pareto set. Unless **CAL** authorises `DominanceRegime=ParetoPlusIllumination`, **illumination/coverage** act as **gauges** (reported in telemetry) and **do not** affect dominance.

**R7 — GeneratorFamily branches (open‑ended).** If S2 includes `GeneratorIntent`, SoS‑LOG **MUST**:
 (i) verify **`EnvironmentValidityRegion`** is declared and lawful;
 (ii) verify **`TransferRulesRef`** exists; if `unknown` ⇒ `Degrade(scope‑narrow)` or `Abstain` per family policy;
 (iii) treat the selection surface as **pairs `{environment, method}`**; publish **coverage/regret** and **IlluminationSummary** as gauges (dominance participation per **R6**).

**R8 — Telemetry & Refresh hooks.** On any illumination increase or archive change, publish **edition increments** for **CharacteristicSpaceRef**/**DistanceDefRef** and the **policy‑id** (Emitter/Acceptance) that caused the change; expose **PathSliceId** for refresh/decay in SCR.

> *Aphorism.* **“Admit on lawfulness and sufficiency; degrade on uncertainty; abstain on illegality.”**

#### 4.3 Maturity ladder (poset, not a scalar; Description, not Spec)

Publish a **`MethodFamily.MaturityCardDescription@Context`** (UTS enum ids; **Scale kind = ordinal**; **ReferencePlane declared**). Do **not** embed thresholds here; any **maturity floors** used for admission are authored as **G.4 AcceptanceClause** and referenced by id from R1.

* **L0 — Anecdotal.** Claims exist; lanes sparse; examples ad‑hoc.
* **L1 — Worked‑Examples.** Multiple **worked examples** with lane tags and **Scope slices** declared; *no replication yet*.
* **L2 — Replicated.** Independent replication(s) in distinct Context slices (publish D.CTX + UTS rows), lane separation observed, decay windows explicit.
* **L3 — Benchmark‑Severe.** Repeated wins or parity on **community baselines** or **severe tests**; cross‑Tradition bridges declared with **loss notes**.

*Optional rung (for QD/OEE‑heavy families; ordinal, closed enum):*
* **L4 — QD‑Hardened.** Archive stability under declared **InsertionPolicy/DistanceDef** editions; reproducible **IlluminationSummary** improvements under controlled budgets; OEE generators pass **EnvironmentValidityRegion** severe tests.

**Norms.**
**M1.** The ladder is **lane‑aware** (TA/VA/LA) and **freshness‑aware**; it is **not** a global numeric score. Declare **Scale kind=ordinal** and the **closed enumeration** of rungs; register the enum at **UTS** (twin labels; editioned).
**M2.** Transitions **MUST** be justified by **EvidenceGraph** paths (once G.6 is available) and UTS publication; missing anchors ⇒ no advance.
**M3.** Any **maturity floor** used for admission (e.g., “run‑critical Context requires ≥L2”) **MUST** be authored as a **CAL.AcceptanceClause** and referenced by id from R1; SoS‑LOG does **not** embed thresholds.
**M4.** Declare **ReferencePlane** for the MaturityCard; on ReferencePlane crossings apply published **Φ_plane** policy (penalty to **R_eff only**), with Bridge id and loss notes.

> *Rationale note.* Treating maturity as a **poset** aligns with B.3’s lane calculus and avoids **scalarisation across ordinal/ratio** scales; assurance penalties remain on **R**, never **F/G**.

#### 4.4 Unknowns & Shift classes (tri‑state discipline)

**U1. (LEX/ATS).** Enumerations for `Degrade(mode)` and Maturity rungs **MUST** be declared as **closed value sets** and **registered at UTS** (twin labels). AH‑4 (LexicalCheck) **applies**.
**U2.** Every S2 field is tri‑state; `unknown` **MUST** map to a branch (`Degrade` or `Abstain`) declared on the **family** (no coercions). Each branch publishes a **branch‑id** and (where used) a `mode` from a **closed enum** registered at **UTS** (LEX enum clarity).
**U3.** `ShiftClass` semantics follow **C.22**. If `ShiftClass ∈ {covariate‑shift, concept‑drift, adversarial}` or `unknown`, default outcome is `Degrade(scope‑narrow)` unless a CAL.AcceptanceClause explicitly guards the regime.

#### 4.5 Publication & wiring

**W1.** Each family publishes a **`MaturityCardDescription@Context`** (UTS twin labels; ReferencePlane declared) and **registers SoS‑LOG rule ids**; editions are versioned and **RSCR‑tested for branch‑coverage** (Admit/Degrade/Abstain, unknown paths). **Φ(CL)/Φ_plane policy‑ids** must be present in SCR where applicable.
**W2. Admissibility Ledger.** Publish an **`AdmissibilityLedger@Context`**: rows = `(MethodFamilyId, RuleId, MaturityRung, BranchIds, BridgeIds, ΦPolicyIds, EvidenceGraphPathIds?, DominanceRegime, PortfolioMode, Edition)`, UTS‑registered; this ledger is the **selector‑facing** export.
**W3. Strategy token.** Do **not** mint a `U.Type` “Strategy”; strategy remains a **composition** inside G.5 (`Compose`) under **E/E‑LOG**.
**W4.** Selector (G.5) **consumes** these rules; results appear in the **Dispatcher Report** with reasons in/out and cited anchors/bridges.

### 5) Archetypal Grounding (Tell–Show–Show)

*(Plain register for pedagogy; Core remains notation‑independent per E.10/E.8.)*

**Show‑1 · Continuous dynamics (ODE task).**
*S2 excerpt.* `DataShape=ODE; stiff?=unknown; Size≈10^3; Objective={↓error@ratio, ↑throughput@ratio}; Constraints={safety_gate@ordinal}; Jacobian_sparsity=high; Missingness=MAR`.
*Families.* `Implicit‑BDF` vs `Explicit‑RK` vs `Symplectic`.
*Rules.*
— `Implicit‑BDF`: **Eligibility** tolerates `stiff?=unknown` if `Jacobian_sparsity=high` (guarded precondition); **MaturityCard**=`L3` (replicated & benchmarked). Outcome: `Admit`.
— `Explicit‑RK`: requires `stiff?=false`; with `unknown` ⇒ `Degrade(sandbox)` (probe).
— `Symplectic`: eligible only when `Hamiltonian=true`; here ⇒ `Abstain`.
*Didactic anchor.* This mirrors C.22’s typed‑signature discipline and CHR legality (no ordinal means; unit alignment for **ratio**).

> Contemporary ecosystem examples of these families (post‑2015) are organised in **DifferentialEquations.jl**, which exposes multiple solver **families** under one call surface—precisely the pattern G.5 expects. ([Journal of Open Research Software][1])

**Show‑2 · Planning/scheduling (MIP task).**
*S2 excerpt.* `DataShape=MIP; NoiseModel=deterministic; Objective={↓cost@ratio, ↑service_level@ordinal}; Size≈10^5 vars; convex_relaxation=available`.
*Families.* `MILP (branch‑and‑bound)`, `Constraint‑Programming`, `Heuristic meta‑search`.
*Rules.*
— `MILP`: **Eligibility** requires `convex_relaxation=available`; **MaturityCard**=`L3` in the home Context ⇒ `Admit`.
— `Constraint‑Programming`: **MaturityCard**=`L2`; Acceptance demands `service_level≥B` (ordinal predicate). With `B` met but baseline parity unknown ⇒ `Degrade(scope‑narrow)`.
— `Heuristic meta‑search`: **MaturityCard**=`L1` ⇒ `Degrade(sandbox)` or `Abstain` depending on RSCR parity policy.
*Didactic anchor.* Selector returns a **Pareto set** (no cross‑ordinal weighting), as required by G.5.

> Contemporary “single call / many solvers” packaging that motivates MethodFamily rows is exemplified by **JuMP** (2017–2022), which cleanly separates **model description** from solver choice. ([Miles Lubin][2])

— *DifferentialEquations.jl* illustrates **family‑based** solver packaging (multi‑method under one interface), 2017–2024 ecosystem. ([Journal of Open Research Software][1])
— *JuMP* illustrates **model/solver separation** and registry‑like selection (2021–2022 papers, site). ([Miles Lubin][2])
— *Science of Science* review (2018) supports the emphasis on replication/benchmarks in maturity assessment. ([Science][3])

**Show‑3 · QD archive (policy search).**
*S2 excerpt.* `PortfolioMode=Archive; CharacteristicSpaceRef(d=2); ArchiveConfig(CVT, res=1k cells, K=1, DistanceDefRef.edition=v2, InsertionPolicyRef=dyn‑elite); EmitterPolicyRef=v3; DominanceRegime=ParetoOnly`.
*Rules.* `Admit` returns an **archive**; illumination **reported**; changes to `DistanceDef`/Emitter **editioned** in SCR; dominance remains **ParetoOnly**.

**Show‑4 · Open‑ended GeneratorFamily (POET‑class).**
*S2 excerpt.* `GeneratorIntent{GeneratorFamilyRef=GF‑01, EnvironmentValidityRegion=EVR‑A, TransferRulesRef=TR‑A, CoverageMetric=…}; PortfolioMode=Archive`.
*Rules.* `Admit` yields portfolios over `{environment, method}`; `Degrade(scope‑narrow)` if `TransferRules`=`unknown`; telemetry publishes **coverage/regret** and **IlluminationSummary** with **edition/policy‑id** on improvements.

[1]: https://openresearchsoftware.metajnl.com/articles/10.5334/jors.151?utm_source=chatgpt.com "DifferentialEquations.jl – A Performant and Feature-Rich ..."
[2]: https://mlubin.github.io/pdf/jump-sirev.pdf?utm_source=chatgpt.com "JuMP: A Modeling Language for Mathematical Optimization"
[3]: https://www.science.org/doi/10.1126/science.aao0185?utm_source=chatgpt.com "Science of science"

### 6) Bias‑Annotation

**Principle‑taxonomy lenses.** *Universality* (trans‑discipline), *Didactic primacy* (Tell–Show–Show), *Open‑ended evolution* (refresh‑ready), *Lexical firewall* (no tool names in Core), *Notation independence*. Limits: Worked examples reference widely‑used ecosystems **in Plain register** only. 

### 7) Conformance Checklist (normative)

| ID           | Requirement                                                                                                                                                                                | Purpose                                       |                                                                    |                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------- | ------------------------------------------------------------------ | ---------------------- |
| **CC‑C23.1** | Each `MethodFamily` **SHALL** publish a `MaturityCard` with rung justification via **A.10** anchors (lanes, freshness windows) and (if bridged) **Bridge ids** with **CL** and loss notes. | Makes maturity **auditable** and lane‑typed.  |                                                                    |                        |
| **CC‑C23.2** | `SoS‑LOG` rules **MUST** be **executable** (no prose‑only) and cite: Eligibility test result; CG‑Spec gate verdict; EvidenceProfile minima; Acceptance verdict; Γ‑fold contributors; **EvidenceGraph PathId/PathSliceId**; CL/Φ policy‑ids. |
| **CC‑C23.3** | Enumerations used by the rules (**Degrade(mode)**; Maturity rungs) **SHALL** be **closed** and **UTS‑registered** (twin labels). |
| **CC‑C23.4** | **Unknowns** in S2 **SHALL** map to `{degrade | abstain | sandbox}` with explicit **branch‑ids**; no `unknown→0/false` coercions.                                                          | Tri‑state discipline.                          |                                                                    |                        |
| **CC‑C23.5** | Cross‑Context/plane use **MUST** cite a **Bridge**; **Φ(CL)**/**Φ\_plane** **MUST** be monotone, bounded, table‑backed; penalties **→ `R_eff` only**.                                      | Keeps F/G invariant; legal CL routing.        |                                                                    |                        |
| **CC‑C23.6** | **No thresholds** in CHR or Maturity; thresholds **live only** in **AcceptanceClauses** (G.4).                                                                                             | Separation of concerns.                       |                                                                    |                        |
| **CC‑C23.7** | `MaturityCard` **SHALL NOT** be turned into a global scalar; treat as **poset**; any ordering **MUST** be lawful over CHR types.                                                           | Forbids cross‑scale scalarisation.            |                                                                    |                        |
| **CC‑C23.8** | Publish to **UTS** with twin labels; run **ATS AH‑1..AH‑4** on crossings (TierClassifier, GateCheck, LaneCheck, LexicalCheck).                                                             | Publication & ATS hygiene.                    |                                                                    |                        |
| **CC‑C23.9** | All enumerations (e.g., `Degrade(mode)`, Maturity rungs) **SHALL** declare a **closed value set** and **Scale kind**, and be registered at UTS (LEX enum clarity).                          | Avoids lexical drift; lawful typing.          |                                                                    |                        |
| **CC‑C23.10** | **RSCR tests** cover negative/refusal paths (illegal CHR ops; CG‑Spec gate fail; Bridge missing; **Φ table/policy‑id missing**; **AH‑4 lexical violations**); ensure **branch coverage** (Admit/Degrade/Abstain, unknown). |
| **CC‑C23.11** | If QD fields are in scope, **R0.QD** **MUST** pass: lawful **CharacteristicSpaceRef** (d≥2, characteristics typed, planes declared per characteristic), **ArchiveConfig** (topology/resolution/K, `InsertionPolicyRef`, **editioned** `DistanceDef`), **EmitterPolicyRef** present. | QD legality gate. | |
| **CC‑C23.12** | **DominanceRegime** **SHALL** default to `ParetoOnly`; switching to `ParetoPlusIllumination` **MUST** be authorised by **CAL** and cited by id in SCR.                                    | Prevents implicit scalarisation.              |                                                                    |                        |
| **CC‑C23.13** | If `PortfolioMode=Archive`, LOG **MUST** allow archive outputs (R6) and publish **IlluminationSummary** as a gauge unless CAL opts‑in to dominance participation.                         | Lawful archive semantics.                     |                                                                    |                        |
| **CC‑C23.14** | If `GeneratorIntent` present, **R7** **MUST** verify **EnvironmentValidityRegion** and **TransferRulesRef**; outputs are **{environment, method}** portfolios; coverage/regret telemetry published. | OEE legality & telemetry. | |
| **CC‑C23.15** | On illumination increases/archive changes, **edition increments** (BehaviorSpace/DistanceDef/EmitterPolicy) and the **policy‑id** responsible **SHALL** be logged (R8).                   | Reproducibility & refresh.                    |                                                                    |                        |

### 8) Consequences

* **Explainable admission.** Every *Admit/Degrade/Abstain* is backed by **anchored** evidence and explicit unknown handling (selector reports are SCR‑linked).
* **Run‑safe pluralism.** Multiple families can co‑exist with **policy‑governed** exploration (E/E‑LOG) and maturity‑aware gating.
* **Portable governance.** Bridge hygiene and CL routing make cross‑Tradition reuse **deliberate and costed** (penalties to **R** only).

### 9) Rationale

The ladder and LOG shells align with FPF’s **Assurance calculus**: **F** (form) is governed by artefact kind, **G** (scope) by USM slices, and **R** (reliability) accumulates via WLNK then **Φ(CL)** penalties. Treating maturity as **evidence‑typed rungs**—rather than a “score”—avoids illegal arithmetic and lets **design/run** remain separate per ATS. This mirrors contemporary **science‑of‑science** insights: replication, benchmarking, and field health indicators are the **currency** of maturity, not anecdote.  ([Science][3])

### 10) Relations

**Builds on:** **G.5** (selector consumes these rules), **G.4** (Acceptance & EvidenceProfiles), **C.22** (S2 typing), **C.18 NQD‑CAL**, **C.19 E/E‑LOG**, **B.3** (Assurance tuple & WLNK).   
**Publishes to:** **UTS** (MaturityCards, rule ids), **SCR/RSCR** (branch coverage; parity hooks).
**Constrains:** **G.8** (LOG Bundling must cite MaturityCards), **G.9** (parity harness draws baselines per rung), **G.11** (refresh windows per rung & decay), **G.5** (Open‑Ended Family mode for GeneratorFamily).
**Outcome.** The pattern introduces **new content** (LOG shells + maturity poset + degrade modes + publication Standard) and **does not duplicate** CG‑Spec legality rules, CHR guard‑macros, or CAL acceptance mechanics; it *integrates* them into **admissibility logic** for MethodFamilies.


---

## C.24 — Agentic Tool‑Use & Call‑Planning (C.Agent‑Tools‑CAL)  \[A]

**Status.** Architheory specification (**CAL**). Defines the conceptual calculus for **agentic selection and sequencing of tool calls** under budgets, trust gates, and policy. **ΔKernel = 0** (no kernel primitives added). *Minting note:* this CAL **does not mint** new U‑types; it **aliases** canonical U‑types where appropriate via **E.10/UTS**.

**Instantiates / Refines Pillars.** E.2 P‑3 Scalable Formality, P‑7 Pragmatic Utility, P‑10 Open‑Ended Evolution, P‑11 SoTA Alignment, and the **Bitter‑Lesson Preference** (prefer scalable, general methods that benefit from more data/compute over fragile hand‑tuned heuristics when assurance/cost are comparable).

**Depends on.** A‑kernel (A.1–A.15) for holonic basics and **Role–Method–Work** separation; **B.3** Trust & Assurance (F–G–R with CL penalties); **E.3/E.5** (precedence & Guard‑Rails); **C.5** Resrc‑CAL; **C.18** NQD‑CAL (candidate generation/portfolio); **C.19** E/E‑LOG (explore–exploit policies); **optional** Compose‑CAL and KD‑CAL (knowledge dynamics) where available.

**Coordinates with.**
U.WorkPlan and U.Service bindings (acceptance gates), Working‑Model publication discipline (**per B.3**), Evidence/Provenance (G.6).

### 1) Problem frame

Modern systems increasingly rely on **agents** that can **choose tools** (services/methods) and **plan sequences** of calls to achieve objectives in uncertain contexts. Without a calculus:

* calls are scheduled by **ad‑hoc heuristics**,
* **budgets** (compute, cost, wall‑time) are implicit,
* **assurance** and **policy provenance** are lost, and
* agents either over‑constrain themselves with brittle scripts or wander without guard‑rails.

This CAL provides the **conceptual API for thought** that lets any implementation (LLM‑based, search‑based, code‑based, robotic) plan calls **lawfully**, **audibly**, and **scalably**. (Role–Method–Work alignment; didactic primacy.)  

### 2) Problem

We need a **tool‑agnostic** way to (i) identify **admissible tools**, (ii) **score** candidate call sequences, (iii) allocate an **explore/exploit** share, (iv) enforce **budget & harm** gates, and (v) **replan** on signals—**without** baking domain‑specific heuristics into the core and **without** violating B.3 assurance discipline. 

### 3) Forces

| Force                              | Tension                                                                                                        |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **General methods vs. hand‑craft** | Scalable, model‑centric search ↔ short‑term wins of bespoke scripts (guarded by **Bitter‑Lesson Preference**). |
| **Assurance vs. Autonomy**         | F‑G‑R gates & CL penalties ↔ agent freedom to sequence calls and learn online.                                 |
| **Exploration vs. Delivery**       | Exploration share for illumination ↔ delivery SLAs and cost ceilings (E/E‑LOG policy).                         |
| **Separation of concerns**         | Planning (MethodDescription) ↔ execution (Work) ↔ service promises (U.Service).                                |

### 4) Solution — Signature & Realization

**Types (aliases).**
*`ATC.CallSpec`* ≡ `U.MethodDescription` with `accessSpec` for a tool service;
*`ATC.CallPlan`* ≡ `U.WorkPlan` specialised for tool invocations;
*`ATC.CallGraph`* ≡ Evidence/Provenance graph over a `U.Work` ledger;
*`ATC.Policy`* references `U.EmitterPolicyRef` (E/E‑LOG) and local call gates **including BLP tolerances (α, δ)**.

**Roles.**
A **System in AgentialRole** composes a **Plan** (MethodDescription); upon enactment, a **Performer** executes **Work** (calls), and **Observers** record **Observations** with acceptance checks. (A.15 strict distinction.) 

**Operators (Γ_agent; CAL, conceptual):**

1. `Γ_agent.eligible(tool, TaskSignature, K_ctx) → {true|false, notes}`
   *Eligibility gate* based on capability fit, policy allow‑list/deny‑list, and context K (incl. safety constraints).

2. `Γ_agent.enumerate(TaskSignature, K_ctx) → CandidateSet<ATC.CallSpec>`
   Returns admissible calls. **MAY** delegate to **NQD‑CAL** for portfolio enumeration when families are heterogeneous and **MUST** apply the current **E/E‑LOG lens** (objectives & gauges) to tag candidates.

3. `Γ_agent.plan(Objective, CandidateSet, Budget, ATC.Policy) → ATC.CallPlan`
   Produces a **call plan** with steps `{pre, call, post}`, *explicit budgets* (compute, cost, time, risk), and **E/E policy** (explore_share, tie‑breakers, stop‑conditions). The plan is a MethodDescription, not Work.  

4. `Γ_agent.execute(ATC.CallPlan) → {ATC.CallGraph, Observations}`
   Executes with **hard gates** (budget, risk, constraint‑fit) and logs provenance suitable for B.3 assurance reporting (design/run separated). 

5. `Γ_agent.replan(Signals, ATC.CallPlan, Budget′) → ATC.CallPlan′`
   Triggered by sentinel breaches, assurance drops, or policy events; preserves **editioned** policy and context. (Design/run separation; Working‑Model handshake.) 

6. `Γ_agent.score(Plan or Step) → ⟨ValueProxies, Cost, Risk, FGR_floor⟩`
   Computes selection signals **without** illegal scalarisation across mixed scales; **uses Pareto comparison under the C.19 E/E‑LOG lens** and defers final dominance to declared policies. 

**Normative Laws (ATC‑Laws).**

* **ATC‑1 (Model‑the‑Call, not the App).** A tool call is a **Work** instance that enacts a referenced **MethodDescription** promised by a **Service**; plans schedule calls but are **not the calls**. (A.15.)
* **ATC‑2 (Bitter‑Lesson Preference).** When two admissible choices are within **δ (assurance)** and **α (budget)**, **prefer the more general, scale‑benefiting method** whose **slope vector Pareto‑dominates** under the declared E/E‑LOG objectives; any override **MUST** record a **BLP‑waiver** with expiry. (E.2; precedence governed by E.3.)
* **ATC‑3 (Budget & Harm Gates).** Plans **SHALL** declare ceilings on compute, cost, wall‑time, and risk; execution **MUST** abort or replan on breach. (Assurance ties to B.3; design/run kept separate.)
* **ATC‑4 (Explore‑Share Discipline).** Plans **MUST** declare `explore_share`; defaults **inherit from E/E‑LOG profiles**. **Informative defaults**: `0` for safety‑critical or deterministic tasks; `≈0.2–0.4` for ambiguous tasks with heterogeneous tool families. Promotion of illumination gauges into dominance **requires explicit policy**.
* **ATC‑5 (Provenance & Replay).** Every call **MUST** emit a **CallGraph** with: Service id, MethodDescription edition, inputs/outputs (redacted per privacy), **EmitterPolicyRef**, and budget deltas. (NQD/E/E provenance fields apply when used.)
* **ATC‑6 (Assurance‑First Decisions).** Selection **MUST** respect B.3: WLNK minima on F/R (weakest‑link floors), CL penalties on integration, and **no** chimera scores across design/run. Publish **⟨F,G,R⟩** for the *typed claim* “this plan is admissible under K,S”.
* **ATC‑7 (Notation/Vendor Independence).** Core pattern text **MUST NOT** encode vendor‑specific tokens; bindings occur in Context via Bridges/Profiles. (Lexical guard‑rails.)


### 5) Policy Block (normative, profile‑able)

**ATC‑Policy fields (conceptual):**
`{ backstop_confidence, explore_share, risk_bound, cost_ceiling, time_ceiling, tie_breakers, novelty_quota?, wild_bet_quota?, stop_conditions, BLP_delta_α, BLP_delta_δ }` — realized by referencing an **E/E‑LOG EmitterPolicy** and adding **BLP** clauses. Defaults inherit from E/E‑LOG; any deviation is editioned.

**BLP Precedence.** In conflicts with tactics that hard‑code narrow scripts, **BLP** applies **subject to E.3/E.5 precedence**. Where scripts encode **safety‑critical gating or regulatory compliance**, scripts **prevail** unless a DRR records: (i) **override rationale**, (ii) **expiry**, (iii) **measured hazard** avoided, and (iv) planned **re‑evaluation** window (P‑10 evolution duty).

### 6) Archetypal Grounding (informative; non‑binding)

1. **LLM Research Agent (knowledge work).**
   Task: answer a novel technical question. Candidate tools: retrieval, structured web search, code runner, table/plot generator.
   **Plan:** `enumerate → plan(explore_share≈0.4) → call(search→retrieve→synthesise→code‑check) → replan on sentinel (low R)`; **BLP** favours **general retrieval + prompting policies** over hand‑coded, per‑site scrapers unless assurance demands otherwise. (Echoes SoTA: *ReAct* (2022), *Self‑Ask* (2022), *Reflexion* (2023), *Tree‑of‑Thoughts* (2023), *Toolformer* (2023).)

2. **Program Repair Agent (systems/software).**
   Task: propose a patch against a failing test suite. Candidate tools: repo introspection, static analyzer, unit runner.
   **Plan:** prefer **search‑and‑learn loops** with test‑guided feedback over fixed “if error X then patch Y” tables; exploration quota enforces trials across patch families before exploitation. (Aligns with post‑2019 automated program repair lines and *SWE‑bench*‑style agent loops.)

3. **Lab Automation Agent (physical).**
   Task: adjust a wet‑lab protocol under drift. Candidate tools: planner, pipetting controller, spectrometer, Bayesian optimizer.
   **Plan:** **BLP** drives toward **model‑based optimization** under budgeted sample counts; heuristics remain as **policy‑documented** fallbacks with expiry. (Resonates with quality‑diversity and BO practice since 2015, mirrored by NQD/E/E policies.) 

### 7) Conformance Checklist (CC‑AT)

1. **CC‑ATC‑1 — Declared separation.** Plan is a `MethodDescription`; execution is `Work`; acceptance is via `U.Service`. No schedule inside specs; schedules live in `U.WorkPlan`.
2. **CC‑ATC‑2 — Budgets on record.** `time/compute/cost/risk` ceilings exist **ex ante**; stop conditions listed.
3. **CC‑ATC‑3 — E/E policy.** `EmitterPolicyRef` (or equivalent) and `explore_share` are editioned and logged.
4. **CC‑ATC‑4 — Assurance tuple.** Publish the **typed claim** “Plan admissible under K,S” with **⟨F,G,R⟩** and CL penalties traceable in the **CallGraph** SCR. Design/run never merged.
5. **CC‑ATC‑5 — BLP waiver discipline.** Any heuristic override against a general method includes **expiry** and **re‑evaluation** date.
6. **CC‑ATC‑6 — Provenance minimum.** Record `{ServiceRef, MethodDesc.edition, EmitterPolicyRef, DescriptorMapRef? (if NQD), DistanceDefRef? (if NQD), TimeWindow, Seeds?, Dedup?}`.
7. **CC‑ATC‑7 — Notation independence.** No vendor tokens in conceptual text; bindings via Bridges/Profiles only.
8. **CC‑ATC‑8 — BLP tolerances declared.** **α/δ** tolerances are present in `ATC.Policy` or referenced via the active E/E‑LOG profile.

### 8) Consequences

*Positive.* Portable agent patterns; **auditable autonomy**; lawful exploration; faster hypothesis cycles via BLP; replayable call graphs; decision‑grade Working‑Model surfaces.
*Trade‑offs.* Requires explicit budgets/policies; BLP may defer quick wins from bespoke scripts; stronger logging discipline.

### 9) Rationale (post‑2015 SoTA alignment, informative)

* **Scaling‑first methods** (language‑model and representation‑learning scaling laws; subsequent data/compute‑balanced scaling) empirically support **BLP**: general, learnable mechanisms tend to dominate as budgets rise—hence **ATC‑2**.
* **Tool‑use agents** in the literature (*ReAct*, *Self‑Ask*, *Reflexion*, *Toolformer*, *Tree‑of‑Thoughts*, open‑ended *Voyager*‑style skill acquisition) all benefit from **explicit planning + feedback**, exactly what CC‑AT‑2/3/6 encode.
* **Quality‑Diversity & BO** practice motivates the **explore_share** default and the distinction between **dominance vs. illumination gauges** (kept separate unless policy promotes).  

### 10) Relations

* **Builds on:** A.15 Role–Method–Work alignment (planning vs execution vs service), B.3 Trust & Assurance (F–G–R/CL), C.5 Resrc‑CAL, C.18 NQD‑CAL (candidate/portfolio), C.19 E/E‑LOG (policies).    
* **Constrains:** Any `U.Service` used as a “tool” MUST expose acceptance conditions and observation hooks sufficient for B.3 reporting. 
* **Enables:** Human‑centric Working‑Model surfaces with policy/assurance disclosures (design/run separated). 

### 11) Bias‑Annotation

*Lexical firewall* and *notation independence* apply; no vendor tokens; mixed‑scale characteristics are never averaged; illumination remains a **gauge** unless a policy promotes it into dominance.  

#### Didactic Quick Card (1‑screen crib)

**Agentic Call Plan (public):**
*Objective · Context(K) · Budget{time/compute/cost/risk} · PolicyRef (E/E‑LOG) · Explore‑share · Steps[ pre/ call /post ] · Stop‑conditions · **BLP tolerances (α,δ)** · BLP‑note (if any) · Assurance⟨F,G,R|K,S⟩ · Provenance ids.*


---

## C.25 — **Q‑Bundle: Authoring “‑ilities” as Structured Quality Bundles**  \[D]

**Status & placement.** Part C (measurement/comparability); **Definitional pattern \[D]** reusing Core patterns (**A.2.6 USM**; **A.6.1 Mechanism**; **C.16 MM‑CHR / A.18 CSLC**). Intended as a **lightweight authoring aid** for Contexts; it adds no new kernel types.  (A.6.1; A.2.6 § 6.2; C.16/A.18). 

### 1 · Problem frame
Provide a **minimal, uniform shape** for engineering “‑ilities” so authors either (a) declare a **single CHR characteristic** (when truly measurable on one scale), or (b) publish a **structured bundle** that keeps **measures** (CHR) distinct from **scope** (USM set) and **mechanism/status** slots. This prevents conflation of **set‑algebra** (scope) with **numeric measurement** (CHR) and keeps assurance math stable.  (A.2.6 § 6.2; C.16).

### 2 · Problem (recurring)
*‑ilities* are often treated as if they were **single metrics**, while in practice many are **composites** whose evaluation depends on (i) **declared context‑of‑use** (Scope), (ii) **one or more CHR measures** (SLIs/SLOs), and (iii) **supporting mechanisms/statuses**. Collapsing these into “one number” invites illegal arithmetic and breaks USM locality.  (A.2.6; C.16).

### 3 · Forces
**Locality vs comparability.** Scope must remain **context‑local** (USM) while measures remain **legally comparable** (CSLC). 
**Mechanism vs measure.** Presence of a mechanism (A.6.1) is not itself a measurement, yet may gate admissibility and influence **R**.  (A.6.1; C.16/A.18).

### 4 · Solution — Q‑Bundle normal form (Tell → Show → Show; E.8 order)
**Definition.**  
`Q‑Bundle := ⟨ Name, Carrier, ClaimScope?, WorkScope?, Measures[CHR], QualificationWindow?, Mechanisms?, Status?, Evidence? ⟩`

**Fields (conceptual; reuse existing types).**
* **Name.** The quality family label (e.g., *Availability*, *Resilience*).  
* **Carrier.** `U.System | U.Service | U.Episteme` (what bears the quality).  
* **ClaimScope / WorkScope.** **USM** set(s) over `U.ContextSlice` (where the claim holds / where the capability can deliver). **Set‑valued; not CHR.**  (A.2.6 § 6.2).  
* **Measures[CHR].** One or more **CHR Characteristics bound to one Scale each** (e.g., `AvailabilityRatio[%]`, `RTO[min]`). **These are the measurable slots.** (C.16/A.18).  
* **QualificationWindow.** Time policy used by guards (point/window/rolling).  
* **Mechanisms / Status.** References to **A.6.1 U.Mechanism** realizations (e.g., redundancy policy, audit/trace) or certification/status flags. **Not measurements.** (A.6.1).  
* **Evidence (optional).** Anchors/stubs per A.10 or C.16 to justify measures/mechanisms.

**Conformance (minimal).**
1) If a publisher intends to use an “‑ility” as a **single measurement axis**, they **MUST** bind it to a **named `U.Characteristic` + CSLC Scale** and cite that axis in guards/UTS; otherwise publish a **Q‑Bundle**. (C.16/A.18).  
2) **Scope** remains **USM set‑valued**; guards use **membership/coverage** (“Scope covers TargetSlice”), never ordinal/averaging on G. (A.2.6 § 6.2).  
3) **Mechanisms/Status** MAY gate admissibility but **MUST NOT** be conflated with **Measures**; penalties from Bridges/planes route to **R** only. (A.6.1; Part B).

### 5 · Micro‑catalogue (worked mini‑sketches)
**Availability (often Q‑CHR).**  
*Scope:* observation window + region/tier (USM). *Measure:* `AvailabilityRatio[%]` (CHR). *Mechanisms:* redundancy/failover (A.6.1). **Guard:** Scope covers TargetSlice ∧ SLI/SLO satisfied.  

**Resilience (Q‑CMP).**  
*Scope:* disruption scenarios (USM). *Measures:* `MTTR`, `RTO`, `RPO` (CHR set). *Mechanisms:* drills/restore runbooks. **Guard:** scenario‑specific gates; **R** absorbs penalties from crossings.  

**Security (Q‑MECH/Q‑CMP).**  
*Scope:* trust zones/attack classes (USM). *Measures:* time‑to‑patch, coverage proportions (CHR). *Mechanisms/Status:* control sets, certs. **Guard:** policy/mechanism present ∧ measures thresholds ∧ Scope match.

### 6 · Relations
**Builds on.** **A.2.6** (USM scope algebra, set‑valued; no CSLC), **A.6.1** (mechanism intensions and guards), **C.16/A.18** (measurement legality: one Characteristic ↔ one Scale).  
**Coordinates with.** **B.3** (R/CL penalties only), **A.15** (Method–Work gates use Scope + Measures + Windows).

### 7 · Consequences (brief)
* **No category errors.** Authors cannot “average scope” or treat mechanisms as measurements.  
* **Portable comparisons.** Numbers compare on CHR Scales; scope composes by set algebra.  
* **Cleaner gates.** Admission checks become `Scope covers TargetSlice ∧ Measures met ∧ Window valid`.

### 8 · Quick authoring checklist (lintable)
* If the term is an **‑ility**, choose: **CHR axis** (bind to Characteristic+Scale) **or** **Q‑Bundle**.  
* Ensure any scope is **USM** (set over `U.ContextSlice`); no “G‑levels.”  
* Cite mechanisms/status separately; route crossings’ penalties to **R** only.
