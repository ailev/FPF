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
