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
