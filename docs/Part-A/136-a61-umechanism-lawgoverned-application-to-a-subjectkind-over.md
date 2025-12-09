## **A.6.1 — U.Mechanism · Law‑governed application to a SubjectKind over a BaseType** \[A]

**One‑line summary.** A `U.Mechanism` is a **Signature with laws** applied to a declared **SubjectKind** over a **BaseType**, with explicit **operations**, **invariants/guards**, and a named **Transport** clause for cross‑context use. Transport is **Bridge‑only** (per **F.9**) with penalties routed to **R**/**R_eff** only (per **B.3**); **F/G** remain invariant; **CL^plane** follows **C.2.1 CHR:ReferencePlane**. Realizations **MAY** be published under **A.6** (Signature→Realization; **one Γ only if `classification=CAL`**; acyclic imports; opacity).

**Status.** Normative \[A\] in **Part A (Kernel)**.  

**Placement.** Immediately **after A.6** as **A.6.1**. **USM (A.2.6)** and **UNM (A.19/C.16)** become **instances conforming to A.6.1** (no semantic change to either).

### 1 · Problem frame

Give FPF **one uniform kernel shape** for things like **USM** (set‑algebra on context slices) and **UNM** (classes of admissible normalizations with ≡_UNM) so authors can **define, compare, refine, compose, and port** mechanisms **without re‑inventing the meta‑language**; all cross‑context use is **Bridge‑only** with **CL penalties to R/R_eff**, never to **F/G**.

### 2 · Problem 

Without a kernel abstraction, scope/normalization/comparison constructs proliferate with incompatible algebras and guard surfaces; cross‑context reuse lacks visible **Bridge/CL routing**; comparability drifts into **illegal scalarisation** (e.g., ordinal means). FPF already curbs this via **A.6** (Signature discipline), **USM** (scope algebra & Γ_time), **UNM** (normalize‑then‑compare), and **CG‑Spec** (lawful comparators/ScoringMethods)—but lacks a **common meta‑slot** for “mechanism.”

### 3 · Forces 

**Locality vs transport.** Semantics are **context‑local**; crossing contexts is **Bridge‑only** (Part F/B.3); penalties hit **R/R_eff**; **F/G** invariant.

**Expressivity vs legality.** Rich operators vs **CHR legality** and **CG‑Spec** (no ordinal averages; lawful unit alignment).

**Time determinacy.** Explicit **Γ_time**; no implicit *latest*. (Required in USM’s `ContextSlice`.)

**Signature hygiene.** Obey **A.6** (exactly one Γ from CAL, LOG/CHR export none; imports acyclic; realizations opaque).

### 4 · Solution

#### 4.1 **Mechanism Intension** 

A `U.Mechanism` **publishes**  
        `U.Mechanism.Intension := ⟨IntensionHeader, Imports,
                SubjectBlock := ⟨SubjectKind, BaseType, SliceSet, ExtentRule, ResultKind?⟩,
                ParamKinds, OperatorAlgebra, LawSet, AdmissibilityConditions, Applicability, Transport, Γ_timePolicy, PlaneRegime, Audit⟩`  
and admits Realizations (kernel‑level or architheory‑level) that respect it. The shape is **notation‑independent** and **conceptual** (no tooling, storage, or CI metadata).

* **IntensionHeader.** `id` (PascalCase), `version` (SemVer), `status` (draft/review/stable/deprecated).  
  If realized as an **Architheory**, add the **A.6** header with `classification ∈ {CAL|LOG|CHR}` and `imports/provides`; **only CAL may export exactly one Γ**; **LOG/CHR export none**. For **Kernel‑level** realizations, do **not** mint an A.6 header.

* **Imports.** Architheory Signatures / `U.Types` this mechanism requires (notation‑independent; **acyclic**). When realized as an Architheory, **LOG/CHR may import CAL; CAL may import CAL** (A.6 layering).
* **BaseType.** A `U.Type` the mechanism ranges over. CHR spaces (e.g., a `U.CharacteristicSpace`/chart family) appear here **as types**; outside CHR, use set‑typed `U.Type`s. **Do not mint** a new core type; **reference existing `U.Type`s**. If planes differ, state the **ReferencePlane** policy (see *PlaneRegime*).
* **SubjectKind / SliceSet / ExtentRule / ResultKind? / ParamKinds.**
  • **SubjectKind.** The intensional kind acted upon (C.3.1/3.2), separate from quantification.
  • **SliceSet.** The addressable set of Context slices (USM: **ContextSliceSet**).
  • **ExtentRule.** A rule yielding `Extension(SubjectKind, slice)` (C.3.2), used as the quantifier’s domain.
  • **ResultKind?** Optional intensional kind for outputs of `OperatorAlgebra`.
  • **ParamKinds.** A name→Kind map for multi‑ary operators (inputs); avoids overloading “Role”.
* **OperatorAlgebra.** Named operations with types; examples:  
  • **USM:** `∈, ⊆, ∩, SpanUnion, translate, widen, narrow, refit`.  
  • **UNM:** `apply(method)`, `compose`, `quotient(≡_UNM)`; **normalize‑then‑compare**.

* **LawSet.** Equations/invariants (no proofs here). **Admissions/eligibility tests belong under AdmissibilityConditions, not here.** Laws **MUST** be compatible with CHR legality where numeric comparison/aggregation is induced. Examples:
  • **USM:** serial **intersection**; **SpanUnion** only where a **named independence assumption** is satisfied (state features/axes, validity window, evidence class); `translate` uses declared Bridges; **Γ_time** is mandatory.  
  • **UNM:** **scale‑appropriate** transforms — ratio→positive‑scalar; interval→affine; ordinal→monotone; nominal→categorical; `tabular:LUT(+uncertainty)`.  
  *(Do not mint a new Kernel token for “certificate”; if such a type is later required, it **MUST** follow DRR/LEX minting.)*

* **AdmissibilityConditions.** Deterministic, **context‑local** predicates that **fail closed** (e.g., “Scope covers TargetSlice” with named **Γ_time**; “NormalizationMethod class + validity window named”). Unknowns **→ {degrade | abstain}**; never coerce to 0/false.

* **Applicability.** Binding to a **`U.BoundedContext`** with stance/plane/time notes and any **CG‑Spec/MM‑CHR** legality claims; cross‑context use is declared via **Transport** only.

* **Transport.** **Bridge‑only** semantics for cross‑context / cross‑plane use: name the Bridge and channel (`Scope|Kind`) per **F.9**, and record **ReferencePlane**(src,tgt) per **C.2.1**. Do **not** restate CL ladders, **CL^plane**, or Φ/Ψ tables here; penalties **route to R/R_eff only** and **never** mutate F/G (per **B.3**). Crossings are explicit; **no implicit crossings**. Where **USM** or **KindBridge** are used together, apply the **two‑bridge rule** (scope CL and kind `CL^k` penalties handled **separately** to R).

* **Γ_timePolicy.** Point/window/policy; **no implicit “latest.”** Validity windows are **named**; **required** whenever guards reference time.
* **PlaneRegime.** Declare `ReferencePlane` on values/paths; when planes differ, name **CL^plane** and apply a **Φ_plane** policy (Part F/B.3). Plane penalties **do not** change CL; route to **R/R_eff** only; **F/G** stay invariant.

* **Audit.** Conceptual audit surface only (no data/telemetry workflows): crossings are publishable on **UTS**; surface **policy‑ids** rather than tables. Edition pins and regression hooks (if any) are referenced by id; operational details remain out of scope.
* **SignatureBlock alignment (A.6).** When realized as an **Architheory**, map `U.Mechanism.Intension` to the **A.6 Signature Block** — `Imports`, **Derivations**, **Invariants**, **BelongsToAssurance** — and include the **A.6 header** with `classification/provides`. **CAL** Realizations MAY **provide exactly one Γ**; **LOG/CHR provide none**; **imports form a DAG**; internals **opaque**.

**Compatibility with A.6.** If realized as an **architheory** (CAL/LOG/CHR), obey A.6 (**one Γ for CAL only; acyclic imports; opacity**). Kernel‑level realizations remain notation‑independent and publish the same fields for auditability. LEX discipline applies to all minted tokens.

#### 4.2 U.MechMorph · Refinement, Extension, Equivalence & Composition

**Intent.** Provide structure‑preserving **relations & constructors** between mechanisms.  
**Definitions.**

* **Refinement** `M′ ⊑ M`: narrows **SliceSet/ExtentRule** or **strengthens laws** (safe substitution; Liskov‑style).
* **Extension** `M ⊑⁺ M″`: **adds operations** without weakening existing Laws; old programs remain valid (conservative extension).
* **Equivalence** `M ≡ M′`: there exists a bijective mapping between Subjects/ops preserving/reflecting **LawSet** (up‑to‑isomorphism on **BaseType** and **OperatorAlgebra**).
    
* **Quotient** `M/≈`: factor by a **congruence** (e.g., **≡_UNM** for charts).

* **Product** `M×N`: independent **BaseTypes**; ops are component‑wise; ensures **no illegal cross‑ops** (e.g., set‑algebra discipline for `SpanUnion`). Where independence is claimed, **name and justify** the assumption (do not mint new Kernel types here).

**Transport** `Bridge⋅M`: lifts across Contexts/planes; names **CL/CL^k/CL^plane** regimes; penalties → **`R_eff` only**; **UTS row** recommended for publication; **ReferencePlane(src,tgt)** recorded. If mapping losses are material, **narrow** the mapped set or publish an **adapter** (best practice).

**Passing example.** `USM′ = USM + “publish named independence‑assumption evidence for SpanUnion”` ⇒ **Refinement** (strengthened law; substitution‑safe).
**Normalization quotient.** `UNM / ≡_UNM` exposes **compare‑on‑invariants** surfaces for UCPM/USCM (normalize‑then‑compare).

#### 4.3 U.MechAuthoring · Instantiation template

**MechanismDescription (E.8 Tell–Show–Show; I/D/S‑compliant):**
`Mechanism: U.<Name>`  *(Kernel conceptual description; no tooling fields)*
`Imports: <Signatures / U.Types>` · `SubjectBlock: <SubjectKind, BaseType, SliceSet, ExtentRule, ResultKind?>` · `ParamKinds: <name→Kind map>` · `OperatorAlgebra: <operators with types>` · `LawSet: <equations/invariants>` · `AdmissibilityConditions: <admission predicates; Γ_time>` · `Transport: <Bridge channels; CL/CL^k/CL^plane named; ReferencePlane(src,tgt)>` · `PlaneRegime: <world|concept|episteme rules>`

#### 4.4 MechFamilyDescription & MechInstanceDescription 

* **MechFamilyDescription**: `{Mechanism.Intension, Realizationα, Realizationβ, …}` — each Realization may **tighten** (never relax) Laws (Liskov‑style).

* **MechInstanceDescription**: `{Mechanism.Intension@Context, Windows, named Φ/Ψ/Φ_plane regimes, BridgeIds}` — a **conceptual instance**; operational telemetry/workflows are out of scope.

### 5 · Archetypal Grounding

#### 5.1 **U.System (Work) — USM as a U.Mechanism instance** (normative by reference)

* **Imports:** `U.ContextSliceSet`; Part F.9 **Bridge**; **C.2.1 ReferencePlane** (noted for crossings); **C.2.2 F–G–R**; **C.2.3 U.Formality**.
* **BaseType:** `U.ContextSliceSet`.
* **SliceSet:** `U.ContextSliceSet` (addressable `U.ContextSlice`s).
* **SubjectKind:** `U.Scope` with specializations `U.ClaimScope` (G) and `U.WorkScope`.
* **OperatorAlgebra:** `∈, ⊆, ∩, SpanUnion, translate, widen, narrow, refit`.
* **LawSet:** serial **intersection**; **SpanUnion** only where a **named independence assumption** is satisfied (state features/axes, validity window, evidence class); **translate** uses declared **Bridges**; **Γ_time** is **mandatory**.
* **AdmissibilityConditions:** deterministic **“Scope covers TargetSlice”**; **fail‑closed**; `unknown → {degrade|abstain}` (no implicit `unknown→0/false`).
* **Transport:** **Bridge‑only** with **CL**; penalties → **`R_eff`**; **F/G** invariant; publish UTS notes.
* **Γ_timePolicy:** `point | window | policy`; **no implicit “latest.”**
* **PlaneRegime:** *not applicable to scope sets* (scope is set‑valued over `ContextSlice`, no value‑plane); **CL^plane** N/A.

#### 5.2 **U.Episteme (Knowledge) — UNM as a U.Mechanism instance** (normative by reference)

* **Imports:** **A.17/A.18 (CSLC)**; **C.16 (MM‑CHR)**; `U.BoundedContext`; Part F.9 **Bridge**; **C.2.1 ReferencePlane**.
* **BaseType:** chart/`U.CharacteristicSpace` family in a CN‑frame (one `U.BoundedContext`).
* **SubjectKind:** **NormalizationMethod classes** with induced **≡_UNM** equivalence over charts.
* **OperatorAlgebra:** `apply(method)`, `compose`, `quotient(≡_UNM)`; **normalize‑then‑compare** (exposes compare‑on‑invariants surfaces to UCPM/USCM).
* **LawSet:** scale‑appropriate transforms — `ratio:scale / interval:affine / ordinal:monotone / nominal:categorical / tabular:LUT(+uncertainty)`; **validity windows** per edition.
* **AdmissibilityConditions:** `method ∈ declared class‑set` AND **validity window named**; **fail‑closed**; `unknown → {degrade|abstain}`.
* **Transport:** **Bridge‑only** on cross‑Context; when **describedEntity changes**, declare **KindBridge (CL^k)**; penalties → **`R_eff` only**.
* **Γ_timePolicy:** **named validity windows** for NormalizationMethod/instances (editioned).
* **PlaneRegime:** values live on **episteme ReferencePlane**; on plane crossings apply **CL^plane** policy; penalties → **`R_eff` only**.

*(No operational telemetry implied; publication remains conceptual.)*

### 6 · Defaults

* **Local‑first semantics.** All judgments are **context‑local**; crossings are **explicit** and **costed** (CL→R only).
* **Compliance‑first comparability.** Numeric comparison/aggregation requires **CG‑Spec** (lawful **SCP**, Γ‑fold, MinimalEvidence); **partial orders return sets**; **no ordinal means**.
* **Tri‑state discipline.** `unknown → {degrade|abstain}`; `sandbox/probe‑only` is a **LOG branch** with a policy‑id (no implicit `unknown→0/false`).
* **R‑only penalties.** **Φ/Ψ/Φ_plane** are **monotone and bounded**; penalties route to **`R_eff` only**; **F/G invariant**.

### 7 · Conformance Checklist (normative)

| ID | Requirement |
|----|-------------|
| **CC‑UM.1** | **Complete Mechanism.Intension** publishes: `Imports; SubjectBlock (SubjectKind, BaseType, SliceSet, ExtentRule, ResultKind?); ParamKinds; OperatorAlgebra; LawSet; AdmissibilityConditions; Applicability; Transport (Bridge named; ReferencePlane); Γ_timePolicy; PlaneRegime; Audit`. |
| **CC‑UM.2** | **A.6 alignment:** if realized as Architheory, use A.6 header; **one Γ only if CAL**; LOG/CHR none; **imports acyclic**; Realizations **opaque**; laws may be **tightened** (not relaxed). |
| **CC‑UM.3** | **Bridge‑only transport:** crossings **name** a **Bridge** (F.9); `ReferencePlane(src,tgt)` recorded (C.2.1); **CL^plane** named when planes differ; **no implicit crossings**. When typed reuse is involved, the **two‑bridge rule** applies (scope CL and kind `CL^k` penalties routed **separately** to **R**). |
| **CC‑UM.4** | **R‑only routing:** Φ/Ψ/Φ_plane regimes and CL ladders per **B.3**; penalties **reduce R/R_eff** only; **F/G invariant**. |
| **CC‑UM.5** | **CG‑Spec binding** for any numeric compare/aggregate: lawful **SCP** and Γ‑fold; **normalize‑then‑compare**; **partial orders return sets**; **no ordinal means**; interval/ratio arithmetic only with unit alignment (CSLC‑proven). |
| **CC‑UM.6** | **E.8/E.10 compliance:** Tell–Show–Show present under **“Archetypal Grounding”**; twin registers & I‑D‑S respected; any new `U.*` token requires a **DRR** and **LEX.TokenClass** entry; non‑spec surfaces end with **“…Description”**; **no tool/vendor tokens in Core**. |
| **CC‑UM.7** | **Unknowns tri‑state:** guards define `unknown → {degrade|abstain}`; sandbox/probe branches live in **SoS‑LOG** (not Acceptance).

### 8 · Born‑via‑A.6.1 sketches (informative)

**CPM — Unified Comparison Mechanism (parity‑grade orders)**  
**BaseType:** typed traits/charts in a CG‑Frame. **OperatorAlgebra:** lawful orders (≤, ≽, lexicographic) + **set‑returning** dominance (Pareto). **LawSet:** **no ordinal averaging**; **normalize‑then‑compare** when spaces/scales differ (UNM); editions pinned. **AdmissibilityConditions:** **CG‑Spec** bound; **ComparatorSet** explicit. **Transport:** Bridge+CL → **R/R_eff only**.  

**USCM — Unified Scoring Mechanism (SCP‑first)**  
**BaseType:** `U.Measure` (CHR‑typed slots). **OperatorAlgebra:** gauge embeddings + admissible aggregators; **WeightedSum** only on interval/ratio with unit alignment; partial orders return sets. **Guards:** **MinimalEvidence** \+ CG‑Spec legality. **Transport:** penalties → **R/R_eff**; UTS row.

**PTM — Publication & Telemetry Mechanism (informative)**
**BaseType:** `SoTA‑Pack(Core)`, `PathId/PathSliceId`, `PolicyId`. **OperatorAlgebra:** emit **selector‑ready** packs with parity pins and **telemetry stubs**; listen for edition/illumination bumps; trigger **slice‑scoped** refresh. 

**LawSet:** **no change of dominance defaults** unless CAL policy promotes; edition‑aware refresh. **Guards:** AH‑1..AH‑4 block missing pins. **Transport/Audit:** **G.10/G.11** publication & refresh semantics (CL routing to **R/R_eff**).

*Informative SoTA:* telemetry hooks align with post‑2015 quality‑diversity families (CMA‑ME/MAE, DQD/MEGA) and open‑ended methods (POET‑class) when gauged (illumination) rather than scored.

### **9 · SoTA-Echoing (post-2015 practice alignment)** *(informative)*

**Purpose.** To show how the FPF concept of a *Mechanism* (law-governed signature with guards and transport) aligns with, and improves upon, leading research and engineering practices after 2015.  
All comparisons are *informative*: they serve didactic continuity, not new normative force.

#### 9.1 Contemporary references (post-2015 sources)

1. **Algebraic effects and handlers** (Koka, Effekt, OCaml 5) — formalise “operation + lawful handler” semantics.
    
2. **Institution theory** (Goguen–Burstall; HETS evolutions) — defines translation between signatures, sentences, and models by typed morphisms.
    
3. **Policy-as-Code** (Rego/OPA, ISO 3450x ODD) — codifies admissibility and risk predicates for runtime enforcement.
    
4. **Session / Typestate types** (post-2017 multiparty protocols, linear usage) — constrain admissible operation sequences and states.
    
5. **Measurement-legality in machine learning** (2015 – 2025 monotone and calibrated learning, conformal prediction) — exemplifies the need for explicit scale compliance and monotonicity proofs (CSLC/CG-Spec echo).
    

Each source corresponds to a distinct *Tradition*: formal semantics, categorical algebra, compliance automation, protocol safety, and lawful AI.

#### 9.2 Alignment with A.6.1 fields and concepts

| External practice | Corresponding A.6.1 field / construct | FPF alignment and improvement |
| --- | --- | --- |
| Algebraic effects & handlers | **OperatorAlgebra + LawSet** | FPF generalises effect signatures into universal operator laws; adds Γ_time for temporal legality and explicit R-routing. |
| Institution morphisms | **U.MechMorph** (Refine/Extend/Quotient) | Mechanism morphisms reuse institutional structure but add ContextSlice & Bridge discipline; CL penalties route → R_eff. |
| Policy-as-Code / ODD | **AdmissibilityConditions + Γ_timePolicy** | Policies become first-class lawful guards; FPF forbids hidden context or “latest” defaults. |
| Session / Typestate protocols | **AdmissibilityConditions + set-valued USM Scopes** | Deterministic guards preserve state safety; composable across Contexts by Bridges. |
| Lawful measurement (ML) | **CG-Spec / MM-CHR** binding | Enforces CSLC proofs; forbids ordinal averaging; guarantees unit/scale alignment. |

#### 9.3 Adopt / Adapt / Reject summary

* **Adopt** formal, law-governed signatures (Institutions + Effects); explicit admissibility predicates.
    
* **Adapt** runtime policy execution into *static AdmissibilityConditions + Γ_time* (no embedded evaluators).
    
* **Reject** tool-bound semantics, automatic recency heuristics, or any cross-scale arithmetic without CSLC proof.

#### 9.4 Holonic repeatability

The same correspondence holds at **every holonic level**:  
a part-holon declares its own `OperatorAlgebra/LawSet/AdmissibilityConditions`; a whole-holon merges them via Bridges; a meta-holon re-binds mechanisms under a new Γ-closure. All penalties remain in **R / R_eff**, while **F / G** invariants propagate intact.

### 10 · 60‑second didactic script 

> *“To mint a mechanism, fill a **Mechanism.Intension**: declare **SubjectBlock** (**SubjectKind**, **BaseType**, **SliceSet**, **ExtentRule**, **ResultKind?**) and **ParamKinds**; then **OperatorAlgebra/Laws/AdmissibilityConditions** and **Γ_time**; define **Transport** (Bridge/CL with penalties to R only), and **Audit** (UTS + Path pins). Realize it as CAL/LOG/CHR under **A.6**. USM and UNM are already such mechanisms; the same template births comparison, scoring, and publication mechanisms—safely bound to **CG‑Spec**—without leaving the kernel grammar.”*

### 11 · Quick “builder’s” checklist (author‑facing)

1. Draft **AT0/AT1 charter**: why this Mechanism, which **guard surfaces** and **comparability** are in scope; is a **Γ_m (CAL)** builder needed?
    
* Fill **Mechanism.Intension** (**SubjectBlock**, **ParamKinds**, **OperatorAlgebra**, **LawSet**, **AdmissibilityConditions**, **Applicability**, **Transport**, **Γ_timePolicy**, **PlaneRegime**, **Audit**).
    
* Bind **CHR legality & CG‑Spec** when comparing/aggregating (ComparatorSet, ScaleComplianceProfile (SCP), MinimalEvidence, Γ‑fold).
    
Ship **UTS + G.10**; wire **G.11** telemetry (PathSlice‑keyed); ensure penalties **route to `R_eff` only**.

### 12 · Consequences (informative)

* **Uniform kernel shape.** Scope, normalization, comparison families can be authored and compared without lexical drift.
* **Auditable reuse.** GateCrossings are UTS‑visible; penalties are transparent (**R only**), with **AH‑1..AH‑4** harness coverage.
* **Scalarisation avoids illegality.** Partial orders remain set‑valued; cross‑scale arithmetic is blocked by **CG‑Spec/CSLC**.

### 13 · Rationale (informative)

Anchoring mechanisms in **A.6 Signature→Realization** provides a minimal, typed surface that preserves **USM** set‑algebra and **UNM** “normalize‑then‑compare” quotients while making **Part F (Bridges)** crossings explicit and costed on **R** (never **F/G**).

### 14 · Relations (quick pointers)

Builds on **A.6**; instantiates **A.2.6 USM** (ContextSlice, Γ_time, ∩/SpanUnion/translate) and **A.19/C.16 UNM** (classes, ≡\_UNM, validity windows); uses **Part B** (Bridges, CL/CL^k/CL^plane; **no implicit crossings**); binds **CG‑Spec** for any numeric comparison/aggregation; telemetry/publication via **G.10/G.11**.
