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
