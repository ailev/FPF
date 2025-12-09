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
