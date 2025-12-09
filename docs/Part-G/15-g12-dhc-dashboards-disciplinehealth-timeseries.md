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
