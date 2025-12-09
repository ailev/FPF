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
