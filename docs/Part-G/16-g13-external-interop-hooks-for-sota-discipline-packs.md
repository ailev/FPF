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
