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
