# **Part C — Architheory Specifications**

| §                                            | Architheory                        | Tag | Scope & Exports                                                      |
| -------------------------------------------- | ---------------------------------- | --- | -------------------------------------------------------------------- |
| **Cluster C.I – Core CALs / LOGs / CHRs**    |                                    |     |                                                                      |
| C.1                                          | **Sys‑CAL**                        | CAL | Physical holon composition; conservation invariants; resource hooks. |

# C.2 · **KD‑CAL** — *Epistemic holon composition* \[A]  *(Architheory: CAL)*

**Scope & exports.** A substrate‑neutral calculus for composing **epistemic holons** (`U.Episteme`) and reasoning about their motion and equivalence. Exports: (i) three **point‑characteristics**—**Formality F**, **ClaimScope G**, **Reliability R**—that locate a single episteme; (ii) a **pairwise ladder** of **Congruence Levels (CL 0…3)**; (iii) four **Δ‑moves** (*Formalise, Generalise/Specialise, Calibrate/Validate, Congrue*); (iv) **composition rules** (Γ_epist) for aggregates; (v) propagation laws for CL through mappings and notation bridges. KD‑CAL sits on the `U.Episteme` *semantic triangle* (Symbol–Concept–Object) and never confuses **notation** with **carrier**. All F–G–R computations are **context‑local**; Cross‑context traversals **require** an explicit **Bridge** with **CL** and apply the **B.3** congruence penalty **Φ(CL)** to **R**.  // Contexts ≡ U.BoundedContext; substitution is plane‑preserving only.

**Formality F** is the rigor characteristic defined **normatively in C.2.3**. All KD‑CAL computations and guards **SHALL** use `U.Formality` (F0…F9) as specified there; **no parallel “mode” ladders** are allowed.

## 1 · Context

FPF fixes two archetypal sub‑holons: **`U.System`** (physical/operational) and **`U.Episteme`** (knowledge holon). KD‑CAL is the **home architheory** of `U.Episteme`, giving engineers a compact, testable way to say (a) how strictly an episteme is written (**F**), (b) how much structure it manages (**G**), (c) how well it is warranted by evidence or severe tests (**R**), and (d) how closely **two** epistemes coincide (**CL**). KD‑CAL is built atop **C.2.1 U.Episteme — Semantic Triangle via Components**, which reifies every episteme as **Concept** (claim‑graph), **Object** (describedEntity & evaluation rules), and **Symbol** (notation)—*not the file itself*; **carriers** and **work/executions** remain outside and are linked via `isCarriedBy` / `producedBy(U.Work)`.

## 2 · Problem

Teams routinely entangle **programs, specifications, proofs, and datasets**; a “proof” is treated as a tested routine, a “program” is cited as if it entailed a theorem. **Trust decays** because justification and evidence freshness are not explicit. Epistemes are anthropomorphised as actors (“the standard enforces…”), producing **category errors at execution**. Without a shared composition and equivalence calculus, aggregates hide weakest links and analogies harden into overclaims. KD‑CAL must stop these failure modes with a **single constitution and scale‑set**.

---

## 3 · Forces

* **Universality vs domain idioms.** One calculus must host physics theories, legal codes, safety specs, algorithms, and formal proofs without flattening their differences.
* **Meaning vs materiality.** Meaning must be independent of carrier, yet accountable to it historically.
* **Deductive vs empirical.** Axiomatic certainty and empirical trust have different lifecycles; both must compose.
* **Abstraction vs enactment.** Epistemes constrain action; **systems** act. The calculus must keep the roles distinct.

---

## 4 · Solution

### 4.1 · Coordinates and the triangle

**KD‑CAL characteristics (single‑episteme, point‑values).**

* **Formality F.** From free prose to **machine‑checkable proof/specification**. Litmus: *would a machine reject it if wrong?*
* **Claim scope (G), a set‑valued applicability over `U.ContextSlice`, with ∩/SpanUnion/translate algebra; CL penalties apply to R, not to F/G.** Litmus: *how wide is the declared scope, and under what minimal assumptions does the claim hold?*
* **Reliability R.** From untested idea to **continuously validated claim**. Litmus: *where is the last successful severe test?* **R‑claims MUST bind to evidence and declare relevance windows; stale bindings degrade R or require waiver per ESG policy.**

 **Congruence Level (CL), pairwise ladder.**
 `CL‑0` **Opposed/Disjoint** (contrastive; no substitution); `CL‑1` **Comparable / Naming‑only** (label similarity; no substitution); `CL‑2` **Translatable / RoleAssignment‑eligible** (structure‑preserving mapping in a declared fragment with **stated loss**; theorems may transport); `CL‑3` **Near‑identity / Type‑structure‑safe** (invariants match; type‑structure substitution allowed). *CL is a characteristic of a relation between two epistemes; it is not a fourth charachteristic of epistemic characteristic space.* **Norm:** *substitution is permitted only if plane‑preserving and **CL ≥ 2**; substituting **type‑structure** requires **CL = 3***.

**Triangle link.** The characteristics live on the **Concept↔Object** side: *F* by the internal claim‑graph structure; *G* by the **ClaimScope** (scope & assumptions); *R* by evaluation templates and evidence bindings. The **Symbol** vertex hosts notation; **carriers are outside** the episteme and link via `isCarriedBy`. Multiple notations are allowed under a **single Symbol component**; authors SHOULD register `NotationBridge(n₁,n₂)` with an associated **CL** to make conversion loss explicit.

### 4.2 · Four Δ‑moves (epistemic motion)

* ***ΔF — Formalise.** Rewrite for stricter calculi/grammars; raise proof obligations.
* ***ΔG — Generalise / Specialise.** Widen or narrow the **claim scope** (assumptions & scope). Changes to decomposition granularity are an **orthogonal view** and do not change **G** unless they alter the envelope.
* **ΔR — Calibrate / Validate.** Strengthen severe tests or add live monitoring; update evidence bindings.
* **ΔCL — Congrue.** Establish and record the sameness relation between **two** epistemes (ladder 0→3).
  Moves compose into **paths**; CL along a path is the **minimum** of its links.

### 4.3 · Composition (Γ\_epist) and propagation

Let **Γ\_epist** combine epistemes `{Eᵢ}` into a composite episteme **Γ** that makes a joint claim (*AND‑style*) or exposes an interface (*series composition*). KD‑CAL imposes **safe defaults**:

* **R (Reliability).** Along any justification **path** `P`, compute **`R_eff(P) = max(0, min_i R_i − Φ(CL_min(P)))`** (weakest‑link with congruence penalty). For **series** composition (claims needed conjunctively), the path‑wise weakest‑link applies; for **parallel** support (independent lines to the *same* claim), use **`R(Γ) = max_P R_eff(P)`** (annotate independence); never exceed the best attested line. Cross‑context steps and **NotationBridge** traversals contribute to `CL_min(P)`.

* **F (Formality).** `F(Γ) = minᵢ F(Eᵢ)` (monotone non‑increasing along used paths). To raise **F**, apply **ΔF** to the weakest parts.
* **G (ClaimScope).** On any dependency **path**, take the **intersection** of claim scopes (the **narrowest overlapping scope**). Across **independent support paths to the same claim**, set **`G(Γ) = SpanUnion({G_path})` constrained by support** (drop unsupported regions). Widening/narrowing the scope is an explicit **ΔG±** operation.
* **CL (Congruence).** For a chain of mappings `E₀ ~ E₁ ~ … ~ Eₖ`, the **path congruence** is `min CL(Eⱼ,Eⱼ₊₁)`. Passing through a **NotationBridge** sets CL to the bridge’s declared level; the **Φ(CL)** penalty is applied in the **R** fold for any path that traverses it.

These rules keep Γ aligned with the **holonic kernel**: Γ is only defined on holons and respects identity/boundary discipline from the core. 

### 4.4 · What **must not** be conflated (normative guards)

* **Symbol ≠ carrier.** Files, PDFs, or repositories are **carriers** outside the episteme; they never count as parts of `U.Episteme` (**see C.2.1 EP‑1; CC‑EPI‑2/3**).
* **Epistemes do not act.** Only **systems** perform work; epistemes constrain/evaluate via **Object** and **Concept** (**per Core A.15 / CC‑EPI‑3**).
* **CL is not a score.** It is a **qualitative ladder** of preservation strength; do not average it. 

---

## 5 · ✱ Archetypal Grounding (Tell–Show–Show)

**Universal rule (tell).** *Compose knowledge by Γ\_epist with weakest‑link R, monotone F, and explicit CL on every bridge; keep Symbol–Concept–Object separate and never turn a carrier into a part.*

**System (show, Sys‑CAL lens).** Consider a **battery‑pack thermal subsystem** integrating a physics model of heat flow and an operating envelope for fast‑charge. As a **system**, it composes pumps, sensors, and controllers by physical Γ with conservation constraints (Sys‑CAL). The assurance story depends on epistemes about the model and envelope; the system **acts**, epistemes constrain. (Archetypes and boundary discipline per core.)

**Episteme (show, KD‑CAL lens).** Consider a **CMIP‑class climate projection episteme** (post‑2015 generation): its **Concept** is a claim‑graph over PDEs and parameterisations; its **Object** defines an claim scope (historical forcings, resolution); its **Symbol** may include two notations (domain equations vs. tabular schema) linked by a **NotationBridge** with an explicit CL. Compose sub‑epistemes for radiation, clouds, and ocean mixing: `R = min` across the critical path; an independent hindcast line can raise `R` only up to its own level; `F` is bounded by the least‑formal sub‑claim unless the composition adds formal invariants.

---

## 6 · Bias‑Annotation

* **Metric worship.** Treating `[F,G,R]` as ends rather than means; mitigation: require **evidence bindings** and narrative of limits in the Object envelope.
* **Category slip.** Equating a notation or its carrier with the Concept; mitigation: Symbol–carrier separation and EP‑1 triangle cardinality.
* **Analogy inflation.** Presenting CL‑0/1 as identity; mitigation: always name the **CL rung** for cross‑mappings.

---

## 7 · Conformance Checklist

1. **C2‑1 (Triangle).** Every `U.Episteme` **MUST** occupy exactly one slot per {Symbol, Concept, Object}; carriers link via `isCarriedBy` and are never parts.
2. **C2‑2 (Coordinates).** Each episteme **SHALL** declare `[F,G,R]` with a brief rationale; **F** is `U.Formality ∈ {F0…F9}` per **C.2.3**, **exactly one episteme‑level F** computed as the **min over essential parts**. CL is declared for **pairs only**. Sub‑anchors: ** Contexts **MAY** mint named sub‑anchors (e.g., `F4[OCL]`, `F7[HOL]`), which **MUST** preserve the global order and **map to their parent anchor** from C.2.3.
3. **C2‑3 (Composition).** Authors **SHALL** choose Γ_mode (**series** vs **parallel**). For any justification **path** use **`R_eff(P) = max(0, min_i R_i − Φ(CL_min(P)))`**; for **parallel** independent lines to the *same claim*, take **`R(Γ) = max_P R_eff(P)`** (never exceeding the strongest line). Compute `F(Γ) = min` along the used paths. For **G**, use **path‑wise intersections** and then **SpanUnion({G_path}) constrained by support**. Cross‑context traversals **MUST** use a Bridge with **CL** and apply **Φ(CL)** to `R`.
4. **C2‑4 (NotationBridge).** Multi‑notation Symbol components **SHOULD** register `NotationBridge` edges with CL and loss note; any cross‑notation reasoning **MUST** cite the bridge’s CL.
5. **C2‑5 (No action).** Epistemes **MUST NOT** be assigned actions; work is executed by systems in role.

---

## 8 · Consequences

**Benefits.** A single, compact **map** for all knowledge artefacts; fast detection of weakest‑link **R** in aggregates; disciplined reuse across domains with explicit **CL**; consistent separation of **meaning** from **material carriers**.
**Trade‑offs.** Authors must learn to declare Γ‑mode and CL explicitly; multi‑notation work requires bridge bookkeeping; *mitigation:* the triangle and ladder keep the discipline brief and repeatable.

---

## 9 · Rationale

KD‑CAL externalises a long‑standing semiotic insight (Sign–Meaning–Referent) into a **holonic composition** where syntax/structure (**F,G**), pragmatics/evidence (**R**), and cross‑mapping strength (**CL**) are visible and composable. The explicit triangle (C.2.1) prevents carrier confusion; the characteristic provide a **manager‑readable** yet **formalisation‑ready** scale (with **G** grounded in **scope/envelope**, not part‑count); the CL ladder replaces overloaded “alignment” with a graded sameness notion.

---

## 10 · Relations

* **Depends on:** `U.Episteme — Semantic Triangle via Components` (C.2.1): identity invariants EP‑1, Symbol–Concept–Object definitions, evidence bindings.
* **Peers:** **Sys‑CAL** (C.1), which composes **systems**; KD‑CAL composes **epistemes** and feeds assurance lenses in Part B.
* **Constrained by authoring:** `[A]` patterns must include Tell–Show–Show with **Archetypal Grounding** (this section).

---

## 11 · Worked mini‑examples (post‑2015 flavours)

* **Formal lift (ΔF).** Recasting a 2019 **variational free‑energy** narrative into a typed calculus raises **F**, clarifies scope, and enables CL‑2 bridges between biological and ML formulations—*without* claiming empirical gain (**R** unchanged).
* **Parallel evidence (R, max).** Two independent **hindcast** lines (circa CMIP6, 2019) supporting the same forecast allow `R(Γ)=max(R₁,R₂)`; if one line drifts, the composite is bounded by the stronger line until series constraints apply.
* **Notation bridge (CL drop).** A 2021 **type‑theoretic specification** rendered in a semi‑formal DSL requires a `NotationBridge` with a CL<3 note; any theorem transported across must respect the bridge’s declared preservation.

*(No tooling is implied; these are conceptual moves within the calculus.)*

## C.2.1 · **U.Episteme — Epistemes and their slot graph** \[A]

> **One-line summary.** `U.Episteme` is the holon type for epistemes; its internal ontology is given by `U.EpistemeSlotGraph`, which replaces the legacy **semantic triangle** with a typed graph n-ary relation over `DescribedEntity`, `GroundingHolon`, `ClaimGraph`, `Viewpoint`, `View`, and `ReferenceScheme`, aligned with `U.RelationSlotDiscipline` and ready for both symbolic and distributed representations.

### 1 · Context

FPF’s kernel recognises two archetypal sub‑holons: **System** and **Episteme**. Systems are operational wholes; **epistemes** are **knowledge holons**—theories, models, specifications, standards, algorithms, proofs—whose reason for being is to **say something defeasible or deductive about something** and to be **held to account** by justification. 

**Readers.** Engineering managers and lead designers who need a uniform way to reason about **theories, specifications, algorithms, proofs**—from charter memos up to formal axiomatics—without collapsing into tooling or discipline‑specific notations.

KD‑CAL (C.2) needs a precise notion of **what an episteme is** and **how it mediates** between:

* the thing(s) it is about,
* the contexts and systems that ground and test it, and
* the representational machinery (notations, carriers, operations) we use to work with it.

Contemporary work on **formal languages as cognitive artifacts** (Dutilh Novaes), **operational iconicity** of notations (Krӓmer), **material engagement** (Malafouris), **distributed representations** and **latent‑space communication** in ML, and **tool‑augmented reasoning** (ReAct‑style agent loops) shows that:
* the relation between an episteme and its **DescribedEntitySlot** is not a single “Object-vertex”: it involves explicit **slots and morphisms** (described-entity mapping, grounding, evaluation) typed by SlotKinds and contexts;
* **representations** come in heterogeneous forms (symbolic, diagrammatic, latent, interactive), with very different **operational affordances**;
* **inference** is often **mixed‑mode**: symbolic reasoning plus calls to tools, solvers, and learned models.

FPF therefore needs a **more modular, graph‑shaped ontology** for epistemes which:
* keeps **KD‑CAL** and I/D/S discipline intact,
* is compatible with **A.6.0/A.6.5** signatures (`SlotKind`/`ValueKind`/`RefKind`),
* can be used uniformly by A.6.2–A.6.4 (epistemic morphisms) and E.17.* (views & publication),
* and demotes the old non-SoTA **semanit triangle** to a **didactic projection**, not the normative ontology.

In this pattern:+
* `U.Episteme` is the **holon genus** for epistemes (C.2), with components and identity governed by A.1/A.6/A.7.
* `U.EpistemeSlotGraph` names the **internal ontology graph** of `U.Episteme`: the small, typed n-ary relation over episteme positions (`DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ViewSlot`, `ReferenceSchemeSlot`) on which KD-CAL, A.6.2–A.6.4 and E.17.* rely.
* Species such as `U.EpistemeCard`, `U.EpistemeView`, `U.EpistemePublication` are holonic realisations of `U.Episteme` whose component structure is constrained to be compatible with `U.EpistemeSlotGraph`.

### 2 · Problem

Without a shared **episteme constitution**, teams fall into recurring failure modes:

1. **Object–Description–Carrier soup.** Diagrams and files are treated as *the theory itself*. Changes to a PDF are confused with theoretical change.
2. **DescribedObject blur.** A spec seems to describe “everything in general”. The **GroundingHolon**—*what exactly this knowledge is about*—is implicit and drifts.
3. **Proof vs program confusion.** Algorithms, specifications, and proofs are mixed: a “proof” is used as if it were a tested routine; a “program” is cited as if it entailed a theorem (Curry–Howard misunderstood).
4. **Unanchored trust.** Claims accumulate with no explicit **justification graph** or **evidence freshness**, so assurance degrades invisibly.
5. **Category errors at execution.** Epistemes appear as *actors* (“the standard enforces…”) instead of **systems** acting *with* or *on* epistemes such as data sets or algorithms.

The legacy non-SoTA “Semantic Triangle” treated an episteme as a holon with three components: **Concept** (ClaimGraph), **Object** (Reference Map), and **Symbol** (notation).

This worked well for:
* separating **meaning** (Concept) from **carriers**, and
* integrating KD‑CAL’s **F–G–R** characteristics (Formality, ClaimScope, Reliability).

But for current use‑cases it has structural blind spots:

1. **No explicit DescribedEntity slot.**
   The “Object vertex” bundles together *what the episteme is about* with *how we interpret and test it*. There is no explicit **slot** for the entity‑of‑interest (`U.Entity`) and no clear separation between:
   * the **thing described**, and
   * the **ReferenceScheme** used to read claims as statements about that thing.

2. **Grounding collapses into Object.**
   Material and organisational contexts (labs, infrastructures, organisations) that **ground** an episteme (in Malafouris’ sense) are hidden in the Object/Reference Map. KD‑CAL and Bridges need explicit **GroundingHolon** positions.

3. **Viewpoints are not first‑class.**
   ISO‑style **viewpoints** (families of stakeholders, concerns, conformance rules) and their induced **views** appear only indirectly, via KD‑CAL or MVPK. There is no explicit `U.Viewpoint` / `U.View` pair at the episteme core, which makes it hard to:

   * connect to I/D/S **DescriptionContext**,
   * organize multi‑view descriptions (E.17.0), or
   * align publication viewpoints with engineering viewpoints.

4. **Representations and operations are compressed into “Symbol”.**
   Very different representational regimes are flattened into one Symbol vertex:

   * purely denotational notations (no internal inference calculus),
   * fully operational calculi (e.g., proof assistants),
   * interactive visualisations,
   * latent vectors and prompt‑programs for LLMs.
     There is no place to say “this representation admits **syntactic inference** of such‑and‑such kind” vs “this is just a **passive label**”.

5. **No explicit signature discipline.**
   The triangle speaks of “Object/Concept/Symbol” but not of **slots** and **references** in the sense of A.6.5 `U.RelationSlotDiscipline`. In episteme this leads to:
   * names where **slot, value and ref** are conflated (`DescribedEntityRef` used as if it were a slot),
   * ambiguity between “epistemic object” (what is talked about) and “episteme” (the description),
   * fragile interoperability with signatures for roles, methods, services.

Thus we have problems of:
* **DescribedEntity drift.**
 Specifications and models accumulate without a stable notion of **which DescribedEntity they talk about**; fields like `SubjectRef` are overloaded and resist safe refactoring.
* **Viewpoint confusion.**
  Engineering, publication and governance views are mixed, making it hard to maintain consistency across surfaces or to reason about conformity of descriptions under different viewpoints.
* **Representation mismatches.**
  Trade‑offs between neural vs symbolic, diagrammatic vs textual, or interactive vs batch representations cannot be expressed at the episteme level; they leak into ad‑hoc tool descriptions.
* **Broken modularity.**
  As soon as we add KD‑CAL, LOG‑CAL, MVPK, and E.TGA, multiple **implicit triangles** appear, each with slightly different semantics, instead of a single shared `U.EpistemeSlotGraph`.

We need a replacement for the triangle that keeps its **didactic clarity** but matches the **graph‑ and morphism‑centric** reality of contemporary epistemic work.

### 3 · Forces

| Force                                          | Tension we must resolve                                                                                                                |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **Geometry vs. operations**                    | Simple geometric pictures (triangles) are memorable; real epistemic work is **operational and graph‑shaped** (many nodes, many edges). |
| **Universality vs. representation regimes**    | One ontology must accommodate symbolic calculi, diagrams, DSLs, interactive notebooks, and latent vectors.                             |
| **Intension vs. description vs. spec (I/D/S)** | Intensional objects (I) are not epistemes; descriptions (D) and specifications (S) are. The core must honour Strict Distinction.       |
| **Viewpoint locality vs. reuse**               | Viewpoints should be **local** to families of descriptions, yet we want reusable **viewpoint bundles** across domains (E.17.1/E.17.2). |
| **Slot discipline vs. usability**              | A clean `SlotKind`/`ValueKind`/`RefKind` discipline is vital for reasoning, but must not render engineering episteme unreadable.             |
| **Stability vs. SoTA evolution**               | The core must remain stable while integrating evolving practices: LLM tool‑use, ReAct‑style loops, structured cospans, optics, etc.    |

### 4 · Solution — from outdated semantic triangle to `U.EpistemeSlotGraph`

#### 4.0 Overview

For `U.Episteme`, the legacy semantic triangle is replaced by `U.EpistemeSlotGraph` that is a **small, typed ontology graph** and an **n-ary relation view** over the core episteme positions:

 **Nodes / positions / slots.**
  Minimal **kernel SlotKinds** (with their ValueKinds) that every episteme can refer to, following A.6.5:
  * `DescribedEntitySlot`  (ValueKind `U.Entity` or a declared subkind) → *“what this episteme is about”*;
  * `GroundingHolonSlot`   (ValueKind `U.Holon`) → *“where/how this is grounded”*;
  * `ClaimGraphSlot`       (ValueKind `U.ClaimGraph`) → *“what is being said (intensional content)”*;
  * `ReferenceSchemeSlot`  (ValueKind `U.ReferenceScheme`) → *“how we read claims as statements about entities”*;
  * `ViewpointSlot`        (ValueKind `U.Viewpoint`) → *“under which viewpoint we read/validate this episteme”*;
  * `ViewSlot`             (ValueKind `U.View`) → *“a view‑episteme produced under a viewpoint”*.

* **Slots and signatures.**
  These positions are realised as **SlotKinds** with associated **ValueKinds** and **RefKinds** under `U.RelationSlotDiscipline` (A.6.5). An **episteme kind** (`U.EpistemeKind`) is a **signature** over these slots.

* **Episteme as n‑ary relation and as holon.**
  Each concrete episteme instance can be seen both as:

  * a **tuple** filling these slots (`U.EpistemeTuple`), and
  * a **holon with components** (`U.EpistemeCard`, `U.EpistemeView`, `U.EpistemePublication`) whose fields correspond to those slots.

`U.Episteme` is thus the holon type whose components are *disciplined* by the `U.EpistemeSlotGraph`; C.2.1 fixes that discipline.

* **Morphisms.**
  Simple **epistemic morphisms** (described-entity mapping, grounding, encoding, evaluation) are expressed as ordinary relations/functions between these positions. A.6.2–A.6.4 then specify general laws for effect-free morphisms over `U.Episteme`.

* **Legacy triangle as didactic projection.**
  The classic Symbol–Concept–Object triangle becomes a **didactic view** of this graph, not the normative ontology; it is simply the projection to:

  * `Symbol` ≈ a subset of `U.RepresentationScheme`/`U.RepresentationToken`,
  * `Concept` ≈ `U.ClaimGraph`,
  * `Object` ≈ `{DescribedEntity, ReferenceScheme}`.

The rest of this pattern fixes the **minimal core** needed by KD‑CAL, A.6.2–A.6.4 and E.17.*. The representational nodes (`U.RepresentationScheme`, `U.RepresentationToken`, `U.PresentationCarrier`, `U.RepresentationOperation`) are introduced as an **extension C.2.1+**, preserving the interface defined here.

#### 4.1 Minimal epistemic positions (nodes & slots)

This section defines the **minimal node set** for `U.EpistemeSlotGraph` and the associated **SlotKinds**. These are the positions that A.6.2–A.6.4 and E.17.* can rely on.

##### 4.1.1 `DescribedEntitySlot` — “what this episteme is about”

**Tech:** `DescribedEntitySlot` (SlotKind), `describedEntityRef : U.EntityRef` (Ref slot in tuples/cards).
**Plain:** *described entity*, *entity‑of‑interest*, *object‑of‑talk*.

**Intent.** Provide a **single, explicit slot** for the entity (or entities) that an episteme is about, avoiding the former conflation of Object/Reference/Context.

**Normative definition.**

1. `DescribedEntitySlot` is a **SlotKind** in the sense of A.6.5 `U.RelationSlotDiscipline`.

   * Its **ValueKind** is `U.Entity`.
   * Its **RefKind** is `U.EntityRef` (or a species thereof) and **MUST** be realised in data as a field named `describedEntityRef : U.EntityRef` (E.10 discipline).
1. Species of `U.EpistemeKind` **MAY** constrain the ValueKind to a subtype `EoIClass ⊑ U.Entity` (for example, “EoI is always a `U.Holon` and, more specifically, a `U.System` or `U.Episteme`”). The subtype **MUST NOT** be named `U.DescribedEntity`; “described entity” remains a **role name**, not a kernel type.
2. Wherever episteme previously used `U.EpistemicObject` as a separate type, it is re‑interpreted as **“`U.Entity` in the role of filling `DescribedEntitySlot`”** and is marked as **legacy alias** in LEX‑BUNDLE.

**Didactic cue.**
“Ask: *What, exactly, is this description about?* That is the DescribedEntity.”

##### 4.1.2 `GroundingHolonSlot` — “where / in what holon this is grounded”

**Tech:** `GroundingHolonSlot` (SlotKind), `groundingHolonRef : U.HolonRef?`.
**Plain:** *grounding holon*, *holon‑of‑grounding*, *engagement context*.

**Intent.** Capture the **material–social holon** (system, lab, infrastructure, organisation, runtime environment) with respect to which an episteme’s claims are **tested, calibrated or validated**.

**Normative definition.**

1. `GroundingHolonSlot` is a **SlotKind** with:

   * **ValueKind** `U.Holon`,
   * **RefKind** `U.HolonRef` (or a species thereof),
   * and recommended field name `groundingHolonRef? : U.HolonRef` in episteme cards/views.
2. `GroundingHolonSlot` is **optional** at the minimal core: an episteme may be **un‑grounded** at M‑mode (e.g., purely mathematical), but any episteme used for **empirical evaluation or assurance** under KD‑CAL **SHALL** either:

   * populate `groundingHolonRef`, or
   * declare explicitly that no such grounding is possible (e.g., counterfactuals, abstract logics), with consequences reflected in KD‑CAL `R`.
3. The phrase *“grounding holon”* is **plain‑register**; there is no kernel type `U.GroundingHolon`. It always means “the holon currently filling `GroundingHolonSlot` for this episteme.”

**Didactic cue.**
“Ask: *In which lab/organisation/world‑slice do we test or observe this?* That is the GroundingHolon.”

##### 4.1.3 `U.ClaimGraph` and `ClaimGraphSlot` — intensional content

**Tech:** `U.ClaimGraph` (kernel type), `ClaimGraphSlot` (SlotKind).
**Plain:** *claim graph*, *intensional content*.

**Intent.** Reuse the existing KD‑CAL notion of **ClaimGraph** as the episteme’s **intensional body**, but make its role as a **slot value** explicit.

**Normative definition.**

1. `U.ClaimGraph` is the **ValueKind** for `ClaimGraphSlot`:

   * nodes: typed claims (definitions, axioms, theorems, requirements, properties, assumptions);
   * edges: logical/derivational/refinement relations, as already defined in C.2.
2. `ClaimGraphSlot` is a **SlotKind** whose instances are always **stored by value** in core patterns:

   * `content : U.ClaimGraph` is the normative field in `U.EpistemeCard` / `U.EpistemeView`;
   * C.2.1 **MUST NOT** introduce `U.ClaimGraphRef` as a ValueKind. Any reference type for ClaimGraphs, if needed, is a **RefKind** defined by discipline packs on top of `U.ClaimGraph`.
3. `ClaimGraphSlot` is **mandatory**: every `U.EpistemeKind` that uses C.2.1 **SHALL** have exactly one `ClaimGraphSlot`.

**Didactic cue.**
“Ask: *What is actually being claimed, defined, required, proved?* That is the ClaimGraph.”

##### 4.1.4 `U.Viewpoint` and `ViewpointSlot` — perspective of concerns and validators

**Tech:** `U.Viewpoint` (kernel type), `ViewpointSlot` (SlotKind), `viewpointRef : U.ViewpointRef?`.
**Plain:** *viewpoint*, *perspective*, *stakeholder perspective*.

**Intent.** Provide a **first‑class home** for ISO‑style viewpoints and their generalisations, as used by E.17.0 `U.MultiViewDescribing`, MVPK, and TEVB.

**Normative definition.**

1. `U.Viewpoint` is the type of **intensional viewpoint specifications**:

   * families of **RoleEnactors/stakeholder groups** the viewpoint speaks for,
   * their **concerns**,
   * allowed **kinds of descriptions/specifications**,
   * and **conformance rules** for views under this viewpoint.
     (The internal structure of `U.Viewpoint` is fixed in E.17.0, not here.)
2. `ViewpointSlot` is a **SlotKind** with:

   * **ValueKind** `U.Viewpoint`,
   * **RefKind** `U.ViewpointRef`,
   * normative field name `viewpointRef? : U.ViewpointRef` on episteme cards/views.
3. For **I/D/S descriptions/specs** (E.10.D2), `viewpointRef` is a **mandatory part of `DescriptionContext`**; C.2.1 treats that as a **species‑level constraint**, not as a universal requirement for all epistemes.
4. `ViewpointSlot` may be unset in purely internal, pre‑viewpoint epistemes (e.g., raw formal developments), but any episteme that participates in **MultiViewDescribing** (E.17.0) **MUST** set it or be deterministically associated to it via a `ViewpointBundle`.

**Didactic cue.**
“Ask: *Who is this for, and what do they need to see to accept it?* That is the Viewpoint.”

##### 4.1.5 `U.EpistemeView` / `U.View` and `ViewSlot` — episteme‑level views

**Tech:** `U.EpistemeView` (kernel species of `U.Episteme`), alias `U.View`; `ViewSlot` (SlotKind); `viewRef : U.ViewRef`.
**Plain:** *view*, *epistemic view*.

**Intent.** Distinguish **view‑epistemes** (views **of** descriptions/specifications) from both:

* the underlying descriptions/specifications themselves, and
* the **PublicationSurface** carriers on which they are rendered (E.17, L‑SURF).

**Normative definition.**

1. `U.EpistemeView` is a **species of `U.Episteme`** whose episteme kind includes, at minimum:

   * one `ClaimGraphSlot` (typically a **sliced or projected ClaimGraph**),
   * one `DescribedEntitySlot`,
   * one `ViewpointSlot`,
   * and appropriate `ReferenceSchemeSlot`.
2. `U.View` is an **alias** for `U.EpistemeView` in E‑cluster patterns (especially E.17.*), used where the word “view” is conventional.
3. `ViewSlot` is a **SlotKind** whose:

   * **ValueKind** is `U.View`,
   * **RefKind** is `U.ViewRef` (or `U.EpistemeViewRef` species),
   * intended usage is **in meta‑structures** such as `U.MultiViewDescribing` families and MVPK.
4. `ViewSlot` **MUST NOT** be confused with carrier slots: Surfaces and faces are **not** values of `ViewSlot`; they are `U.Surface` artefacts in L‑SURF, related to views by MVPK.

**Didactic cue.**
“Ask: *Which particular slice of the description under this viewpoint are we talking about?* That is the View.”

##### 4.1.6 `U.ReferenceScheme` and `ReferenceSchemeSlot` — reading ClaimGraph as claims about entities

**Tech:** `U.ReferenceScheme` (kernel type), `ReferenceSchemeSlot` (SlotKind); `referenceScheme? : U.ReferenceScheme`.
**Plain:** *reference scheme*, *interpretation scheme*, *description scheme*.

**Intent.** Separate **what is being said** (ClaimGraph) from **how claims are read as statements about entities and contexts** (designation, measurement, evaluation envelopes), without reifying the referents themselves as a vertex.

**Normative definition.**

1. `U.ReferenceScheme` is a **component type of epistemes**, not an external object:

   * it determines how nodes of `U.ClaimGraph` are mapped to **properties/relations** over values of `DescribedEntitySlot`,
   * it specifies **measurement/evaluation templates** (how to test claims on `GroundingHolon`),
   * it fixes **claim scope envelopes** over characteristic spaces.
2. `ReferenceSchemeSlot` is a **SlotKind** with:

   * **ValueKind** `U.ReferenceScheme`,
   * **no RefKind in the minimal core** (ReferenceSchemes are stored by value as `referenceScheme? : U.ReferenceScheme` fields on episteme cards/views).
     Discipline packs **may** introduce `U.ReferenceSchemeRef` as a **RefKind**, but **must not** repurpose it as a new ValueKind.
3. `ReferenceScheme` is the place where the legacy “Object‑vertex” semantics now live:

   * it does **not** “contain” the real‑world object,
   * it hosts the **rules** that tie claims to entities and groundings.

**Didactic cue.**
“Ask: *Given this ClaimGraph, how exactly do we treat it as talking about these entities in these contexts, and how do we test it?* That is the ReferenceScheme.”

##### 4.1.7 Minimal node set and extension C.2.1+

The **minimal `U.EpistemeSlotGraph` core** for C.2.1 consists of positions (the episteme core SlotKinds of A.6.5 CC‑A.6.5‑5):
* `DescribedEntitySlot` (ValueKind `U.Entity`),
* `GroundingHolonSlot` (ValueKind `U.Holon`),
* `ClaimGraphSlot` (ValueKind `U.ClaimGraph`),
* `ViewpointSlot` (ValueKind `U.Viewpoint`),
* `ViewSlot` (ValueKind `U.View`),
* `ReferenceSchemeSlot` (ValueKind `U.ReferenceScheme`).

This pattern **only fixes these positions**.
The **extension C.2.1+** (second step of the refactor) adds:
* `U.RepresentationScheme` and `RepresentationSchemeSlot`,
* `U.RepresentationToken` and `RepresentationTokenSlot`,
* `U.PresentationCarrier` and `PresentationCarrierSlot`,
* `U.RepresentationOperation` and `RepresentationOperationSlot` (with inference regime annotations),

without changing:
* the definition of `U.EpistemeKind`,
* the minimal `U.EpistemeCard` interface,
* or the assumptions A.6.2–A.6.4 / E.17.* make about episteme components.

In C.2.1+ carriers remain **structural publication artefacts**, not semantic parts of the episteme:
`U.PresentationCarrier` values are linked to `U.Episteme` / `U.View` via MVPK / L‑SURF relations (e.g. `isCarriedBy` / faces) and **MUST NOT** be counted as components when reasoning about episteme identity, DescribedEntity/grounding, or KD‑CAL morphisms. Changing carriers or surfaces alone **never** changes the `U.Episteme` instance determined by C.2.1; it only produces new `U.Work` / publication events.

##### 4.1.8 Attached epistemic structures (non-slot components)

`U.EpistemeSlotGraph` deliberately does **not** reify every epistemic artefact as a node. Several key structures remain **attached, non-slot components** of `U.Episteme`:
* **`JustificationGraph`** — the argument/evidence graph for nodes of `U.ClaimGraph` (A.10/B.3).
* **`EvidenceBindings`** — per-claim `U.EvidenceRole` assignments that connect claims to external `U.Work` and carriers.
* **`EditionSeries`** — the `PhaseOf` chain of episteme editions (A.14) with change-class annotations (symbol-only vs ClaimGraph vs ReferenceScheme changes).
* **`ScopeCard` / `U.ClaimScope`** — USM scope objects (A.2.6) describing where the episteme’s claims hold.

These attached structures are **not extra positions** of `U.EpistemeSlotGraph`; they hang off the `U.ClaimGraph`/`U.ReferenceScheme` pair and are governed by KD-CAL (C.2), A.10 and B.3. C.2.1 only requires that an episteme which participates in KD-CAL exposes them in a way that keeps **ClaimGraph / ReferenceScheme / Evidence / EditionSeries / `ClaimScope`** clearly distinguishable.

#### 4.2 Episteme as n‑ary relation and as holon

To prevent confusion between **objects‑of‑talk**, their **descriptions**, and the **places they occupy in an episteme**, C.2.1 explicitly treats epistemes both as:

1. **n‑ary relations with a signature** (slots & values), and
2. **holons with components** (fields & parts).

##### 4.2.1 `U.EpistemeKind` — episteme as a typed n‑ary relation

**Tech:** `U.EpistemeKind` (kernel type).

**Intent.** Provide a **signature‑level** description of an episteme as an n‑ary relation whose arguments are governed by `SlotKind`/`ValueKind`/`RefKind` triples per A.6.5.

**Normative definition.**

1. Every episteme that participates in KD‑CAL **belongs to some `U.EpistemeKind`**.
   The kind determines:

   * which **SlotKinds** appear (`DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ViewSlot`, `ReferenceSchemeSlot`, …),
   * the **ValueKind** for each slot (always a subtype of `U.Type`),
   * the **RefKind** used to store it in episteme (when applicable).
1. `U.EpistemeKind` is a **special case** of `U.Signature` (A.6.0), with its slots governed by `U.RelationSlotDiscipline` (A.6.5). C.2.1 **MUST NOT** define an alternative slot discipline.
2. For the minimal core, every `U.EpistemeKind` **MUST** include:
   * exactly one `ClaimGraphSlot`,
   * at least one `DescribedEntitySlot`,
   * and at least one `ReferenceSchemeSlot`.
     Inclusion of `GroundingHolonSlot`, `ViewpointSlot`, `ViewSlot` **MAY** be species‑level constraints (mandatory for D/S‑epistemes, optional for others).

**Didactic cue.**
“An `EpistemeKind` is the *type* of episteme: which positions it has and what can go into them.”

##### 4.2.2 `U.EpistemeTuple` — episteme as filled n‑ary relation

**Tech:** `U.EpistemeTuple` (kernel species).

**Intent.** Model **filled instances** of an episteme’s signature, separating the n‑ary relation from any particular holonic packaging or publication.

**Normative definition.**

1. `U.EpistemeTuple` is a species whose instances are **pure value tuples**:
   * for each SlotKind in the associated `U.EpistemeKind`, a value of the slot’s **ValueKind** (or a reference value of **RefKind**, if the kind is configured as such).
2. `U.EpistemeTuple` is **notation‑agnostic** and **carrier‑agnostic**: it does not know about files, formats, or surfaces.
   It exists to give A.6.2–A.6.4 a minimal notion of “episteme as a point in Ep”.
3. In episteme, `U.EpistemeTuple` rarely appears directly; it is typically **induced** by `U.EpistemeCard` and `U.EpistemeView` (which add component structure and meta‑information).

**Didactic cue.**
“An `EpistemeTuple` is the abstract record of *what fills which slots* — nothing more.”

##### 4.2.3 `U.EpistemeCard`, `U.EpistemePublication`, `U.EpistemeView` — holonic realisations

**Tech:** `U.EpistemeCard`, `U.EpistemePublication`, `U.EpistemeView` (species of `U.Episteme`).

**Intent.** Provide **holon‑level structures** that engineers can work with (components, mereology, provenance), while keeping them aligned with `U.EpistemeKind` and `U.EpistemeTuple`.

**Normative definition.**

1. **`U.EpistemeCard`.**
   A species of `U.Episteme` whose components correspond one‑to‑one to slots of some `U.EpistemeKind`:
   * `content : U.ClaimGraph` (for `ClaimGraphSlot`),
   * `describedEntityRef : U.EntityRef` (for `DescribedEntitySlot`),
   * `groundingHolonRef? : U.HolonRef` (for `GroundingHolonSlot`),
   * `viewpointRef? : U.ViewpointRef` (for `ViewpointSlot`),
   * `referenceScheme? : U.ReferenceScheme` (for `ReferenceSchemeSlot`),
   * optionally `representationSchemeRef? : U.RepresentationSchemeRef` (C.2.1+),
   * `meta : Edition/Provenance/Status…`.
     Minimal episteme identity is the pair `⟨content, describedEntityRef⟩` within a `U.BoundedContext`; all other fields are optional at the genus level but may be mandatory in species. Changes that alter `content` or the effective `referenceScheme` (or that intentionally re‑identify `describedEntityRef`) **SHALL** be realised as new phases in an `U.EditionSeries` (PhaseOf chain) under A.14/A.7. Changes confined to `U.PresentationCarrier` / surfaces or other publication artefacts **do not** create a new episteme; they are captured as `U.Work` / publication events over the same `U.Episteme`.
2. **`U.EpistemePublication`.**
   A species representing **epistemes that have been published** onto surfaces (MVPK). It:
   * has at least the components of `U.EpistemeCard`,
   * plus references to `U.Surface` / `U.Face` artefacts (E.17, L‑SURF),
   * but **does not** re‑interpret these surfaces as parts of the episteme; carriers remain external.
3. **`U.EpistemeView`.**
   As defined in §4.1.5, a species of `U.Episteme` representing a **view** under a specific `U.Viewpoint`.
   Its components are a specialisation of `U.EpistemeCard`:
   * ClaimGraph often restricted/projection of a base description/specification,
   * Viewpoint fixed,
   * ReferenceScheme tailored to that viewpoint.

**Alignment requirement.**
For any of these species, the pattern **MUST** state explicitly:
* which `U.EpistemeKind` it realises, and
* how each component maps to a SlotKind/RefKind under `U.RelationSlotDiscipline`.

This ensures that A.6.2–A.6.4 can treat any `U.Episteme*` uniformly as both:
* an object in the category **Ep**, and
* a structured holon with components.

##### 4.2.4 SlotKind / ValueKind / RefKind discipline for DescribedEntity & GroundingHolon

C.2.1 adopts **A.6.5 `U.RelationSlotDiscipline`** wholesale. For the two key positions:
1. **DescribedEntitySlot.**
   * `SlotKind = DescribedEntitySlot`;
   * `ValueKind = U.Entity` (species may constrain to `EoIClass ⊑ U.Entity`);
   * `RefKind = U.EntityRef` (or a species thereof);
   * normative field name in episteme cards: `describedEntityRef : U.EntityRef`.
     No kernel type named `U.DescribedEntity` is introduced; the phrase “described entity” always means “an instance of `U.Entity` in the role filling `DescribedEntitySlot`”.
1. **GroundingHolonSlot.**
   * `SlotKind = GroundingHolonSlot`;
   * `ValueKind = U.Holon`;
   * `RefKind = U.HolonRef`;
   * normative field name: `groundingHolonRef? : U.HolonRef`.
     There is no kernel type `U.GroundingHolon`; “grounding holon” is a **slot occupant name**.
Any episteme that previously mixed slot/value/ref concepts (e.g., using `DescribedEntityRef` as if it were a type) **MUST** be migrated to this discipline over time; C.2.1 provides the normative anchor, and F.18 / discipline packs provide the migration guide.

#### 4.3 Minimal epistemic morphisms (informal schema)

> **Note.** The full mathematical treatment (categories Ep and Ref, describedEntity functor `α : Ep → Ref`, and effect‑free morphisms) lives in A.6.2–A.6.4. Here we fix only the **object‑level relations** that C.2.1 expects to exist between its positions.

At the level of `U.EpistemeCard` components and SlotKinds, we assume the following **primitive relations** (not all are functions):

1. **`describedEntitySet : U.Episteme → P(U.Entity)`**
   *derivable from `DescribedEntitySlot` and `ReferenceScheme`*
   * For an episteme `E`, `describedEntitySet(E)` is (at least) the singleton containing the entity referenced by `describedEntityRef(E)`; in more complex cases, it may be a finite set or bundle of entities, determined by `ReferenceScheme`.
   * The **functorial DescribedEntity mapping** `δ_E : Ep → Ref` used in A.6.2–A.6.4 is the categorical lift of this relation: it forgets episteme internals and keeps only the object in the ReferencePlane determined by the pair `<DescribedEntitySlot, GroundingHolonSlot>`.

2. **`grounds : (U.Entity, U.Holon) ⇝ GroundingRelation`**
   *relates described entities to grounding holons*
   * Captures how values of `DescribedEntitySlot` are **situated** in holons that make evaluation possible (labs, infrastructures, organisations).
   * Need not be total or functional; an entity may admit multiple grounding holons, or none.

3. **`designates : (U.ReferenceScheme, U.ClaimGraph, U.Entity, U.Holon) ⇝ DesignationProfile`**
   *how claims are read as statements about entities in contexts*
   * Specifies, for each claim in `content` and each `<describedEntityRef, groundingHolonRef>`, what property/relation it purports to state, and under what conditions.

4. **`satisfies / evaluatesTo : (U.ClaimGraph, U.ReferenceScheme, U.Holon) → TruthProfile/SuccessProfile`**
   *evaluation of claims under a reference scheme and grounding*
   * Forms the bridge to KD‑CAL’s `F, G, R` evaluation; details are given in C.2 and B.3.

5. **View-related morphisms** (to be connected with A.6.3):
   * `viewProject : (U.Episteme, U.Viewpoint) → U.View`
     — effect-free, **DescribedEntity-preserving** projection that slices `ClaimGraph` and specialises `ReferenceScheme` under a given viewpoint.
   * `viewEmbed : U.View → U.Episteme`
     — embedding of a view back into the wider episteme, typically as a reference with correspondence proofs.

5. **Reflexive describedEntity guard.**
   When `DescribedEntitySlot` or `ReferenceScheme` picks out an episteme or claim that includes the referring claim itself (**ReferencePlane = episteme**), publishers **SHALL** ensure that the induced justification/evaluation structure is **acyclic per evaluation chain**: reflexive describedEntities may exist as literature handles, but they MUST NOT form a minimal support cycle for acceptance or KD‑CAL assurance. Self‑reference is allowed as a citation pattern, not as a way to close justification loops.

These are **not yet laws**; they are the **hooks** that A.6.2–A.6.4 will formalise into:
* `U.EffectFreeEpistemicMorphing` (Ep→Ep morphisms over this structure),
* `U.EpistemicViewing` (describedEntity‑preserving Ep→Ep),
* `U.EpistemicRetargeting` (describedEntity‑retargeting Ep→Ep).

### 5 · Legacy semantic triangle as didactic view  *(informative)*

**Position.** The classical semiotic or semantic triangle (“Symbol–Concept–Object”, Ogden–Richards/Frege–Carnap style) is **not** the normative ontology for epistemes in FPF. For `U.Episteme`, it is treated as a **didactic projection** of the richer hypergraph `U.EpistemeSlotGraph`:
* **“Symbol” corner** ≈ {`U.RepresentationToken`, `U.RepresentationScheme`, `U.PresentationCarrier`} when C.2.1+ is in use; in the minimal core this is collapsed into whichever external artefact happens to carry `U.ClaimGraph`.
* **“Concept” corner** ≈ `U.ClaimGraph` + `U.ReferenceScheme` under a chosen `U.Viewpoint`. This is the intensional content plus its interpretation recipe.
* **“Object” corner** ≈ the occupant of `DescribedEntitySlot` (ValueKind `U.Entity`) plus the occupant of `GroundingHolonSlot` (ValueKind `U.Holon`) and the grounding relation between them.

Under this reading the triangle is a **three‑node quotient** of the `U.EpistemeSlotGraph`:
```
(Symbol)      = RepresentationToken + Scheme + Carrier
(Concept)     = ClaimGraph + ReferenceScheme (+ Viewpoint)
(Object)      = DescribedEntity + GroundingHolon
```

All **viewpoints, operations, carriers and reference planes** are suppressed in the classical diagram. The cost of this suppression is precisely the confusion that motivates C.2.1:
* describing becomes an single unlabeled arrow,
* inference regimes disappear,
* measurement and grounding are invisible.

**Didactic use.** C.2.1 allows the triangle **only** in the following cases:
1. As an **introductory picture** in guidance material (“this is the coarse triangle; the actual pattern is the episteme slot graph”).
2. As a **quotient diagram**: an explicit note that “this figure ignores viewpoint, grounding, carrier, and operationality; see C.2.1 for the full structure”.
3. As a **legacy alignment aid** when mapping to standards or literature that speak only in triangle terms.

**Guard.** Any pattern or documentation page that uses a “semantic triangle” diagram **MUST** either:
* explicitly state “this is a didactic projection of C.2.1 `U.EpistemeSlotGraph`”, or
* treat it as a legacy reference when aligning with external standards.

The triangle **MUST NOT** be used as a kernel‑level ontology or as a basis for morphism laws. All normative reasoning about epistemes proceeds via the slots and components of `U.EpistemeSlotGraph`.

### 6 · Interaction with I/D/S and DescriptionContext  *(normative)*

C.2.1 is the **episteme‑layer carrier** that I/D/S discipline (A.7, E.10.D2) relies on. The link is made via `DescriptionContext`.

#### 6.1 · DescriptionContext over C.2.1 components

For any episteme that is a **Description** or a **Specification** in the sense of E.10.D2, the field `subjectRef : U.SubjectRef` is interpreted as a **DescriptionContext triple**:
```
DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩
```

where:
* `DescribedEntityRef : U.EntityRef` — occupies `DescribedEntitySlot` (ValueKind `U.Entity`, species often constrained via EoIClass ⊑ `U.Entity`).
* `BoundedContextRef : U.BoundedContextRef` — points to the context that fixes vocabulary, units, and legal inferences for this description (E.10.D1).
* `ViewpointRef : U.ViewpointRef` — occupies `ViewpointSlot` (ValueKind `U.Viewpoint`) and determines which concerns, role‑enactor families, and conformance rules apply.

**Normative requirement (IDS‑13).**
For every `…Description` / `…Spec` episteme:
1. `subjectRef` **SHALL** be decodable to a well‑formed DescriptionContext triple.
2. `DescribedEntityRef` from that triple **SHALL** be identical to the field `describedEntityRef` that fills `DescribedEntitySlot` in the corresponding `U.EpistemeCard`/`U.EpistemeView`.
3. `ViewpointRef` in DescriptionContext **SHALL** agree with `viewpointRef` in the episteme card or be uniquely derivable from a `U.ViewpointBundle` in E.17.1 (with the derivation rule documented).

Intensions (I‑layer) such as `U.System`, `U.Method`, `U.Role` **do not** inhabit C.2.1 directly; they are the *targets* of I→D operations (`Describe_ID`) and appear as values of `DescribedEntitySlot` in resulting descriptions/specs.

#### 6.2 · I→D and D→S morphisms over C.2.1

* **Describing (`Describe_ID : I → D`).**
  Produces an episteme whose:
  * `content : U.ClaimGraph` encodes the descriptive claims about the intension,
  * `describedEntityRef` points to the intension’s entity,
  * `groundingHolonRef` (if present) fixes where the description is evaluated or tested,
  * `viewpointRef` selects the describing viewpoint.

  `Describe_ID` is **conformant** to A.6.2 but not an Ep→Ep morphism (domain is Intension, codomain is Episteme). C.2.1 provides the **codomain schema** and ensures that the resulting Description has a valid DescriptionContext.

* **Specifying/Formalising (`Specify_DS/Formalize_DS : D → S`).**
  Takes a Description episteme and returns a Specification episteme with:
  * the same `describedEntityRef`,
  * the same `BoundedContextRef` and `ViewpointRef` (hence same DescriptionContext),
  * a `content : U.ClaimGraph` that raises formality F (F≥4) and adds test harness hooks, but is conservative with respect to the underlying intension.

  As an Ep→Ep morphism, `Specify_DS` is a **species of A.6.2** and must obey the invariants over the C.2.1 slots (DescribedEntityChangeMode = preserve; no change to DescribedEntity; ClaimGraph refinement only).

C.2.1 does **not** define I/D/S; it only insists that any `…Description`/`…Spec` species that claims to respect I/D/S discipline must:
* implement `U.EpistemeCard` or `U.EpistemeView` **with** `content`, `describedEntityRef`, `groundingHolonRef?`, `viewpointRef?`, and `referenceScheme?` fields, and
* wire these fields into `subjectRef` as DescriptionContext.

### 7 · Alignment with A.6.2–A.6.4 (episteme morphisms)  *(normative)*
`U.EpistemeSlotGraph` is the **object‑level substrate** for the episteme morphism patterns:
* A.6.2 `U.EffectFreeEpistemicMorphing`
* A.6.3 `U.EpistemicViewing`
* A.6.4 `U.EpistemicRetargeting`

#### 7.1 · Effect‑free episteme morphisms (A.6.2) over C.2.1
For any `f : X → Y` that is an instance of `U.EffectFreeEpistemicMorphing`:
* **Typed objects.**
  X and Y are `U.Episteme` instances realised as `U.EpistemeCard` / `U.EpistemeView` with at least the minimal core components:

  ```
  content            : U.ClaimGraph
  describedEntityRef : U.EntityRef      // DescribedEntitySlot
  groundingHolonRef? : U.HolonRef       // GroundingHolonSlot
  viewpointRef?      : U.ViewpointRef   // ViewpointSlot
  referenceScheme?   : U.ReferenceScheme// ReferenceSchemeSlot (ByValue)
  ```

  Any additional C.2.1+ components (RepresentationScheme, Tokens, Carriers, Operations) are visible to A.6.2 only through their declared SlotKinds (A.6.5).
* **DescribedEntityChangeMode characteristic.**
  `f` **MUST** declare a **`describedEntityChangeMode ∈ {preserve, retarget}`**:
  * `preserve` — `describedEntityRef(Y) = describedEntityRef(X)` and any change to `groundingHolonRef`/`viewpointRef` must be justified by Bridges/CorrespondenceModel, without changing the DescribedEntitySlot value;
  * `retarget` — permitted only for A.6.4 species; see below; in this case the characteristic records an intentional change in the pair `<describedEntityRef, groundingHolonRef>` under a declared `KindBridge` in the appropriate ReferencePlane.

  This **DescribedEntityChangeMode** is a CHR-style *characteristic* (A.17) on episteme morphisms, which points directly to `DescribedEntitySlot`. Avoid introducing a separate “describedEntity” term alongside `DescribedEntity`. 
  
* **Component discipline.**
  P0–P5 from A.6.2 are read **directly** in terms of C.2.1 components:
  * purity ⇒ only C.2.1 components of Y may change; no Work/Mechanism side‑effects;
  * conservativity ⇒ claims in `content_Y` read via `referenceScheme_Y` about the new `<DescribedEntity, GroundingHolon>` do not go beyond what already follows from `content_X` via `referenceScheme_X` under the declared DescribedEntityChangeMode and Bridges;
  * functoriality ⇒ composition of such transformations respects the slot structure and ReferenceSchemes.

Any Ep→Ep pattern that operates on `U.Episteme` **MUST** state which C.2.1 slots it reads and which it may write, in terms of SlotKinds/ValueKinds/RefKinds (A.6.5), and then declare itself a species of A.6.2/3/4 as appropriate.

#### 7.2 · EpistemicViewing (A.6.3) as describedEntity‑preserving projections

`U.EpistemicViewing` is the **DescribedEntity-preserving** species of A.6.2. Over C.2.1 this means:
* `describedEntityRef(Y) = describedEntityRef(X)` — the same value in `DescribedEntitySlot`.
* `groundingHolonRef` is preserved, or changed only within a fixed grounding context (e.g. normalising identifiers for the same lab or runtime).
* `viewpointRef` is either:
  * preserved (internal normalisation under the same viewpoint), or
  * replaced by another `U.ViewpointRef` *within* a `U.MultiViewDescribing` family (E.17.0), with invariants enforced by a CorrespondenceModel.
* `content` and `referenceScheme` are transformed **conservatively**: no new intensional claims about the same DescribedEntity are introduced.

Typical examples:
* filtering or aggregating `U.ClaimGraph` to a view relevant for a stakeholder group;
* rendering a behavioural specification into a tabular or diagrammatic episteme under a publication viewpoint;
* normalising a logic‑heavy episteme into a more operational one, while keeping the same described system and context.

In terms of SoTA, EpistemicViewing behaves like a **lens** or **optic** over C.2.1: a focus (SlotKinds for content/representation) is manipulated while the DescribedEntity is fixed.

#### 7.3 · EpistemicRetargeting (A.6.4) as DescribedEntity-bundle retargeting on episteme morphisms

`U.EpistemicRetargeting` is the species of A.6.2 where **`describedEntityChangeMode = retarget`**.
It is always a **morphism between epistemes** (`f : X → Y` in `U.Episteme`), but the adjective “retargeting” refers **not** to the fact that an episteme is mapped to another episteme (this is true for all A.6.2 species), and **not** to a separate describedEntity, but specifically to the **change in the DescribedEntity-bundle** selected by C.2.1:
* `describedEntityRef(Y) ≠ describedEntityRef(X)` — the value stored for `DescribedEntitySlot` changes;
* a `KindBridge` must relate `Kind(describedEntityRef(X))` and `Kind(describedEntityRef(Y))`;
* `groundingHolonRef` may remain the same (e.g. same plant, different subsystem) or be transformed along a Bridge in the same ReferencePlane.

In practice, many retargetings operate on the **target bundle** `<DescribedEntitySlot, GroundingHolonSlot>` (for example, when an episteme about a physical module is re-interpreted as an episteme about a function-holon realised in a different environment). The characteristic `describedEntityChangeMode` still classifies such morphisms by whether this bundle is preserved or intentionally re-identified under a `KindBridge` and reference-plane policy; the episteme on the codomain side is just the usual A.6.2 target object.


Over C.2.1 this is used for:
* **functional vs structural reinterpretation** (e.g. an episteme about a physical module retargeted to an episteme about the function it realises; StructuralReinterpretation in E.TGA becomes a species of A.6.4);
* **signal vs spectrum** transitions (Fourier‑style moves where the object‑of‑talk changes from time‑domain signal to frequency‑domain representation but an invariant, such as energy, is preserved);
* **data vs model** transitions (e.g. retargeting an episteme about raw observations to an episteme about a learnt model, with an invariant such as likelihood or sufficient statistics).

C.2.1 ensures that these retargetings have a **clear source and target** at the DescribedEntitySlot and that any such move is expressed as a morphism over well‑typed slots, not as an unstructured rewrite of “subject” or “object” labels.

### 8 · Alignment with E.17.* (Multi‑View Describing & Publication)  *(normative)*

`U.EpistemeSlotGraph` underpins the E.17 cluster:
* E.17.0 `U.MultiViewDescribing`
* E.17.1 `U.ViewpointBundleLibrary`
* E.17.2 `TEVB — Typical Engineering Viewpoints Bundle`
* E.17 `MVPK — Multi‑View Publication Kit`

#### 8.1 · Multi‑View Describing (E.17.0)

`U.MultiViewDescribing` organises **families of descriptions/specifications** over a shared entity‑of‑interest:
* The **EoIClass** parameter of E.17.0 is a species constraint on the ValueKind of `DescribedEntitySlot` (`EoIClass ⊑ U.Entity`).
* Each member of a multi‑view family is a `…Description`/`…Spec` episteme with:
  * `describedEntityRef` into that EoIClass,
  * `viewpointRef` drawn from a `U.ViewpointBundle`,
  * `subjectRef` decoding to DescriptionContext.

Within this pattern:
* `U.Viewpoint` is **exactly** the ValueKind of `ViewpointSlot` in C.2.1.
* `U.View` is `U.EpistemeView`, a species of `U.Episteme` whose `content` is already restricted to a particular `U.Viewpoint` and often also to a particular `U.RepresentationScheme`.

C.2.1 thus supplies the **per‑episteme** structure that E.17.0 rearranges into multi‑view families.

#### 8.2 · Viewpoint bundles (E.17.1/E.17.2)

`U.ViewpointBundleLibrary` and TEVB specialise the `U.Viewpoint` node:
* A ViewpointBundle is a **set of `U.Viewpoint` instances** tailored to a class of DescribedEntities (e.g., holons in engineering contexts).
* TEVB fixes `EoIClass = U.Holon` (typically `U.System` or `U.Episteme`) and provides canonical engineering viewpoints: functional, structural, role‑enactor, interface‑oriented, etc.

From the C.2.1 perspective:

* these bundles populate the ValueKind of `ViewpointSlot`;
* engineering episteme species that want to be “TEVB‑aligned” must restrict `viewpointRef` to TEVB’s `EngineeringVPId` set, while keeping the same DescribedEntitySlot discipline.

#### 8.3 · MVPK (E.17) as publication over C.2.1 views

MVPK treats `U.View` (i.e. `U.EpistemeView`) as its primary input:
* it uses `U.EpistemicViewing` species (A.6.3) to generate publication‑oriented views from engineering or logical views;
* it then packages these `U.View` epistemes into `U.Surface` artefacts via publication viewpoints and faces.

C.2.1’s distinction between:

* `U.Viewpoint` (intensional, epistemic perspective) and
* `U.PresentationCarrier` (surface in C.2.1+ and L‑SURF)

keeps **epistemic perspective and physical medium separate**:
* MVPK operates only on epistemes (Views) and then on carriers;
* the same View can be realised on multiple carriers without changing its describedEntity or ClaimGraph.

Any MVPK species that claims to be C.2.1‑conformant **MUST**:
* treat `U.View` as a `U.EpistemeView` with a valid C.2.1 core,
* document which C.2.1 slots it reads/writes (typically only representation/carrier‑related ones, leaving `DescribedEntitySlot` and `GroundingHolonSlot` untouched),
* refrain from introducing new claims about the described entity beyond what is in the source `U.View`’s ClaimGraph.

### 9 · Bias‑annotation  *(informative)*

**Episteme‑first and pragmatics‑first.**
The pattern assumes that *nothing is a meaningful episteme* unless it is **about something for someone under some perspective**. This follows the pragmatic turn in semantics: describedEntity and concerns are not afterthoughts but part of the core structure. The graph is therefore built around slots for DescribedEntity, GroundingHolon, Viewpoint and ClaimGraph, not around abstract “propositions in the void”.

**Operational/representational bias.**
C.2.1+ anticipates that certain RepresentationSchemes are **operational** in Novaes’ sense (supporting direct syntactic inference, like pen‑and‑paper arithmetic or proof states) while others are **purely notational**. The pattern remains neutral on which schemes are used but bakes in a place for operations and carriers so that:

* symbol‑manipulating tools (SAT/SMT, proof assistants, classical programming languages),
* distributed/latent representations (LLM embeddings, latent protocols like “DroidSpeak”, “Coconut”‑style communication),
* hybrid ReAct‑style agent loops

can all be treated as different species operating over the same `U.EpistemeSlotGraph`. There is a bias towards making these operational differences **explicit** instead of hiding them behind “the model”.

**Viewpoint and stakeholder bias.**
The pattern leans on the ISO‑style idea that viewpoints encode **stakeholder concerns and role‑families**, but it generalises this beyond architecture. `U.Viewpoint` is intentionally intensional and not bound to any single discipline; still, the examples are skewed toward engineering and epistemic use‑cases.

**Didactic bias.**
The pattern is written to be teachable: semantic triangles are kept as didactic projections; examples like stools on lab rigs, services and SLAs, and model‑evaluation epistemes are deliberately simple. This may under‑represent more exotic epistemes (e.g. artistic, legal, or socio‑technical ones), but the intention is that these use the same slots with different species‑level constraints.

### 10 · Conformance checklist  *(normative)*

**CC‑C.2.1‑1 · Minimal core components for episteme species.**
Any species of `U.Episteme` that participates in I/D/S discipline or in E.17 multi‑view/publishing **MUST** be representable as `U.EpistemeCard`/`U.EpistemeView` with at least:

```
content            : U.ClaimGraph
describedEntityRef : U.EntityRef
groundingHolonRef? : U.HolonRef
viewpointRef?      : U.ViewpointRef
referenceScheme?   : U.ReferenceScheme      // ByValue
meta               : …                      // edition, provenance, status (A.7/F.15)
```

and corresponding SlotSpecs consistent with A.6.5 (`DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ReferenceSchemeSlot`).

**CC‑C.2.1‑2 · No kernel type for “DescribedEntity” or “GroundingHolon”.**
Patterns **MUST NOT** introduce kernel types `U.DescribedEntity` or `U.GroundingHolon`:
* DescribedEntitySlot has ValueKind `U.Entity` ( species‑constrained via EoIClass if needed),
* GroundingHolonSlot has ValueKind `U.Holon`.

Plain terms “described entity” and “grounding holon” are allowed only as **role descriptions** of slot occupants.

**CC‑C.2.1‑3 · SlotKind/ValueKind/RefKind discipline.**
All episteme‑related slots, including `DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ViewSlot`, `ReferenceSchemeSlot` (and any extensions in C.2.1+), **MUST**:
* follow the naming discipline of A.6.5 (`*Slot` for SlotKinds, `*Ref` only for RefKinds/fields),
* declare a ValueKind and refMode (`ByValue` or a RefKind),
* be used consistently across patterns that refer to the same conceptual position.

**CC‑C.2.1‑4 · DescriptionContext wiring.**
Any episteme species whose name or pattern claims to be a `…Description` or `…Spec` in the sense of E.10.D2 **MUST**:
* expose `subjectRef : U.SubjectRef`,
* provide a decoding to `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩`,
* ensure that `DescribedEntityRef` matches `describedEntityRef` (DescribedEntitySlot), and
* ensure that `ViewpointRef` matches `viewpointRef` or is derivable from a `U.ViewpointBundle` under documented rules.

**CC‑C.2.1‑5 · Morphism declarations over slots.**
Any pattern in A.6.2–A.6.4, E.17, E.TGA, or discipline packs that defines morphisms between epistemes **SHALL**:
* state whether it is a species of `U.EffectFreeEpistemicMorphing`, `U.EpistemicViewing`, or `U.EpistemicRetargeting`,
* declare its `describedEntityChangeMode` (preserve/retarget),
* name which SlotKinds it reads and writes,
* state its behaviour on `describedEntityRef`, `groundingHolonRef`, `viewpointRef`, and `referenceScheme`.

**CC‑C.2.1‑6 · Semantic‑triangle usage guard.**
If a semantic triangle or parallelogram diagram appears in a pattern or tutorial, there must be an explicit note that:
* it is a didactic projection of `U.EpistemeSlotGraph`, and
* normative laws are stated in terms of C.2.1 nodes and morphisms, not in terms of triangle corners.

**CC‑C.2.1‑7 · KD‑CAL / ReferencePlane alignment.**
Any pattern that evaluates or compares epistemes (KD‑CAL/LOG‑CAL, CHR, CG‑Spec, etc.) **MUST** point out:
* how `U.ClaimGraph` is interpreted in a ReferencePlane,
* how `GroundingHolonSlot` figures into measurement or validation,

**CC‑C.2.1‑8 · Context locality and Bridges.**
Any `U.Episteme` species that is consumed by KD‑CAL / LOG‑CAL / CHR‑based patterns **SHALL** declare a `U.BoundedContextRef`; all F–G–R computations and C.2.1 slot interpretations are **context‑local**.  Cross‑context use **MUST** proceed via an explicit Bridge with CL / Φ‑policy (F.9/B.3), with penalties routed to R‑lanes only; F and the slot structure from C.2.1 remain unchanged.

**CC‑C.2.1‑9 · Carriers and Work outside episteme content.**
C.2.1 **inherits** A.7/A.12’s separation obligations: `U.PresentationCarrier` / `U.Surface` artefacts and `U.Work` instances **MUST NOT** be treated as parts of `U.Episteme` or as values of any SlotKind in `U.EpistemeSlotGraph`. Episteme content stays in `U.ClaimGraph` and `U.ReferenceScheme`; evidence enters only via `U.EvidenceRole` bindings that point to external `U.Work` / carriers (A.10/B.3). Changing carriers or re‑publishing work alone does **not** change the episteme determined by ⟨content, describedEntityRef, referenceScheme⟩ in its `U.BoundedContext`.

**CC‑C.2.1‑10 · Reflexive describedEntity guard.**
When an episteme uses C.2.1 to speak **about** another episteme (ReferencePlane = episteme), or about itself (self‑describing or meta‑specification cases), patterns **SHALL** ensure that the resulting JustificationGraph / evaluation chains are **acyclic** along support paths. Reflexive `describe` / citation edges may exist as literature anchors, but they MUST NOT form minimal support cycles for acceptance or KD‑CAL assurance decisions; the trust calculus MUST always bottom out in external evidence (`U.Work` with `U.EvidenceRole`) rather than in purely self‑referential claims.

### 11 · Consequences  *(informative)*

**Benefits**
* **Single, extensible episteme core.**
  C.2.1 gives a small, stable set of positions (DescribedEntity, GroundingHolon, ClaimGraph, Viewpoint, View, ReferenceScheme) and components (`U.EpistemeCard`, `U.EpistemeView`, `U.EpistemePublication`) on which all higher‑level patterns depend. This avoids the proliferation of “epistemic objects” and “facets” with overlapping semantics.
**Transparent DescribedEntity & grounding discipline.**
  The pair (`DescribedEntitySlot`, `GroundingHolonSlot`) is no longer hidden inside ad-hoc “SubjectRef” fields or semantic triangles: both are explicit, typed slots. This makes retargeting, viewing and correspondence laws (A.6.2–A.6.4, E.17.0) easier to state and check.
* **Better fit for contemporary representation practice.**
  By distinguishing ClaimGraph, RepresentationScheme, Tokens, Carriers and Operations (in C.2.1+), the pattern matches contemporary SoTA views of notation and formalism:
  * formal languages as cognitive artefacts and de‑semanticisation tools (Novaes),
  * operational iconicity and medium‑sensitive reasoning (Krämer, Malafouris),
  * hybrid symbolic–neural workflows (e.g. ReAct, tool‑augmented LLMs, latent protocols).
  FPF can model both symbol‑heavy and latent‑heavy workflows without privileging either.
* **Uniform substrate for multi‑view description and publication.**
  MultiViewDescribing, viewpoint bundles (TEVB), and MVPK all land on the same episteme core. This avoids the current “views vs viewpoints vs faces” confusion and leaves “architecture” as a domain‑specific specialisation rather than a competing meta‑ontology.
* **Tooling alignment.**
  Slot discipline plus explicit episteme components map cleanly to implementation types (records, row‑typed schemas, effectful handlers). Tools can generate code, schemas or telemetry from episteme species without guessing what “subject”, “context” or “object” mean.

**Trade‑offs / costs**
* **More explicit structure.**
  Authors must declare slots, ValueKinds and references explicitly, and keep DescriptionContext consistent. This is more upfront work than writing ad‑hoc “Subject/Object” fields, but it pays off in substitution safety and cross‑pattern reuse.
* **Migration effort.**
  Legacy uses of “EpistemicObject”, “Facet”, “Subject”/“Object”, and raw `…Ref` fields will need refactoring into C.2.1 slots + A.6.5 SlotSpecs. Migration notes and aliasing can ease the transition, but mechanical cleanup will still be required.
* **Exposure of representation biases.**
  Being explicit about RepresentationSchemes and Operations may surface disagreements about which representations are “primary” in a team or discipline. C.2.1 does not resolve these disagreements; it only makes them visible and therefore debatable.

#### 12 · Relations  *(overview)*

**Builds on**
* A.1 `U.Holon` — for treating episteme as a holon with components.
* A.6.0 `U.Signature` — for interpreting episteme kinds as n‑ary relations over slots.
* A.6.5 `U.RelationSlotDiscipline` — for SlotKind/ValueKind/RefKind discipline over episteme slots.
* A.7, E.10.D2 — for I/D/S discipline and the Interpretation of `subjectRef` as DescriptionContext.
* C.2 (KD‑CAL, LOG‑CAL) — for ClaimGraph semantics, ReferencePlanes, and Bridges.
* E.8, E.10 — for pattern authoring discipline and lexical guards.

* **Constrains**
* A.6.2–A.6.4 — by fixing the minimal episteme component set those morphisms operate on and by requiring an explicit **DescribedEntityChangeMode characteristic** (`describedEntityChangeMode ∈ {preserve, retarget}`) over `DescribedEntitySlot`/`GroundingHolonSlot`.
* E.17.0–E.17.2 — by specifying how `DescribedEntity`, `Viewpoint`, `View` and ReferenceSchemes are represented at episteme level.
* E.17 (MVPK) — by separating `U.View` (episteme) from `U.PresentationCarrier` (surface), and by requiring that publication morphisms be `U.EpistemicViewing` species over C.2.1‑conformant views.
* F.18 (LEX‑BUNDLE) — by providing the episteme‑specific name cards and guards for DescribedEntity/GroundingHolon/Viewpoint/View/ReferenceScheme and their SlotKinds.

**Used by**
* A.6.2 `U.EffectFreeEpistemicMorphing` — as the default episteme object structure for episteme‑to‑episteme transforms.
* A.6.3 `U.EpistemicViewing` — as the substrate for describedEntity‑preserving projections (views).
* A.6.4 `U.EpistemicRetargeting` — as the substrate for DescribedEntity-bundle retargeting transforms between epistemes (Ep→Ep with `describedEntityChangeMode = retarget`).
* E.17.0 `U.MultiViewDescribing`, E.17.1, E.17.2 — to organise families of D/S‑epistemes under Viewpoints and EoI classes.
* E.17 (MVPK) — to publish episteme views as surfaces.
* E.TGA — to interpret StructuralReinterpretation and other engineering projections as episteme morphisms over a well‑typed `U.EpistemeSlotGraph`.

Together, these relations make `U.EpistemeSlotGraph` the **single normative core** for thinking about epistemes, their DescribedEntity mapping, their representations, and their transformations across FPF.

# C.2.3 · **Unified Formality Characteristic F**  \[A]

> **One‑line summary.** Defines **Formality (F)** as a single, ordinal **Characteristic** (`U.Formality`) with **polarity “up”**, anchored by a **default ladder F0…F9** from **free prose** to **proof‑grade foundations**. This unifies how rigor is declared and compared across all epistemes and contexts, and supplies the **F‑coordinate** in the F–G–R assurance space.

---

### 0 · Status & Scope

**Status.** Normative pattern in **KD‑CAL / Part C.2**. It **replaces** the legacy “modes/tiers” language and any parallel “formality ladders.” The letter **F** hereafter denotes the **Formality** characteristic in the **F–G–R** triple.

**Scope.** Conceptual only. The pattern **does not** prescribe workflows, toolchains, or team procedures. It specifies *what Formality is and how to measure/declare it*, so that any team, discipline, or architheory can think and communicate rigor with the same yardstick.

**Non‑goals.**
– Not a publication process, not a governance gate.
– Not a reliability metric (R) and not a scope/abstraction metric (G).
– Not tied to any notation, repository layout, or CI/CD practice.

---

## 1 · Context

Transdisciplinary work (physics, software, systems, policy, data) needs a **shared notion of rigor** that travels across context of meaning. A controller invariant stated in a theorem prover, a research hypothesis framed in constrained English, and a managerial decision rule written as acceptance criteria must be **comparable**—not by their domain lore, but by **how strictly they are expressed**.

Historically, FPF texts carried **multiple signals of rigor** (narrative “modes,” editorial tiers, ad‑hoc “formal vs. informal” talk). These signals mixed with status labels (e.g., “Draft/Effective”), obscuring whether an “approved” artifact was **actually precise** or merely **organizationally accepted**. To reason soundly in KD‑CAL and to compose artifacts safely, we standardize a **single Formality characteristic F**:

* **Portable:** works for math, code, models, requirements, policies.
* **Ordinal & minimal:** few clear anchors from “sketch” to “foundations.”
* **Composable:** participates in the F–G–R calculus and weak‑link invariants.
* **Context‑extensible:** Contexts may introduce **intermediate anchors** without breaking comparability.

---

## 2 · Problem

Absent a unified **F**:

1. **Rigor whiplash.** Either everything is forced into premature formalism (blocking exploration), or informal artifacts drift into high‑assurance use (creating silent risks).
2. **Incomparability.** Each Context’s labels mean different things. Reviewers, integrators, and auditors cannot align expectations or compute trustworthy composites.
3. **Lost continuity.** Moving from sketch to proof often becomes a **rewrite**, severing provenance; the same idea looks like different artifacts at each “mode,” inviting translation errors.
4. **Confused roles.** Status (e.g., “accepted here”) gets conflated with rigor (“precise enough”), undermining governance and the KD‑CAL trust math.

---

## 3 · Forces

| Force                                             | Tension to resolve                                                                                                                             |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Human ↔ Formal system**                         | Natural language is fast and legible; formal systems are unambiguous and checkable. We need a spectrum, not a cliff.                           |
| **Local freedom ↔ Global comparability**          | Contexts must be free to set thresholds; cross‑context reasoning requires a shared scale and anchors.                                          |
| **Readability ↔ Precision**                       | Rich narrative aids understanding; tight syntax prevents misinterpretation. The characteristic must not force one at the expense of the other. |
| **Open‑world thinking ↔ Closed‑world guarantees** | Exploration benefits from openness; certification needs explicit closure. F must support gradual “closing” without renaming the artifact.      |

---

## 4 · Solution — The **Formality Characteristic F**

### 4.1 · Identity and Type (MM‑CHR)

* **Name:** `U.Formality` (nicknamed **F** in F–G–R).
* **Type:** `U.Characteristic`.
* **Scale:** **ordinal** (no arithmetic; comparisons and thresholds only).
* **Polarity:** **up** (higher ⇒ more strictly and unambiguously expressed).
* **Unit:** **formality step** (qualitative anchor).
* **Value domain:** default anchors **F0…F9** (see §4.4).
* **Carrier:** any `U.Episteme` (claim/theory/spec/model/policy/etc.).
* **Notation‑agnostic:** the same F semantics apply regardless of symbol system; bridges between notations do **not** change F (they may affect R via CL, see C.2.2).

**Normative reading.** “F = k” states *how strictly the content is expressed*, not whether it is true (R) nor how broadly it applies (G).

---

### 4.2 · Relationship to KD‑CAL (F–G–R)

* **F in the triple.** F is the **Formality coordinate** in the F–G–R assurance space. It influences trust **indirectly**: higher F reduces ambiguity, enabling stronger evidence and safer composition, but **does not** substitute for evidence (R) or scope (G).
* **Composition invariant (weakest‑link).** For any composite episteme,
  **F\_composite = min(F\_parts on support paths)**.
  *Rationale:* the formal rigor of a whole cannot exceed its least‑formal essential part.
* **Orthogonality.** Changing **G** (envelope/scope) or **R** (evidence) does not, by itself, change **F**; conversely, raising **F** does not imply broader G or higher R.

---

### 4.3 · Extensibility and Local Anchors

FPF provides **default anchors F0…F9** (next subsection). **Contexts MAY**:

* introduce **intermediate anchors** (e.g., F6.5) or **named sub‑anchors** (e.g., “F4‑OCL” vs “F4‑TLA‑constraints”),
* publish **domain exemplars** for anchors,
* define **thresholds** (e.g., “claims of type X must be F≥7”).

**Constraints (normative):**

* **Monotonic order is preserved.** New anchors **MUST NOT** invert or blur the ordering.
* **Anchor meaning is conserved.** Local elaborations **SHALL** map to the nearest global anchor without shifting global semantics (e.g., anything called “F8.x” remains **proof‑grade**).
* **No proxy scales.** Do **not** invent alternative “formality modes/tiers” as surrogates; use **F** explicitly.

---

### 4.4 · Default **F0…F9** Anchors (overview)

> *Full anchor definitions with cross‑disciplinary examples appear in §5 (next part). Below is the overview for orientation.*

* **F0 — Unstructured prose.** Free narrative; ambiguous; human interpretation only.
* **F1 — Scoped notes.** Informal but term‑consistent scope; clearer than F0.
* **F2 — Structured outline.** Template present; coherent sections; criteria mostly “TBD”.
* **F3 — Controlled narrative.** Complete template; constraints sketched in constrained NL or pseudo‑formal phrasing.
* **F4 — First‑order constraints.** Explicit invariants/properties expressible at ≈FOL level (checkable conditions exist).
* **F5 — Executable math/algorithmics.** Precisely defined computational semantics; outcomes checkable by execution/simulation.
* **F6 — Hybrid formalism.** Mixed discrete/continuous methods; model‑checking or equivalent obligations identified.
* **F7 — Higher‑order verified.** Core claims encoded and checked in HOL‑style systems.
* **F8 — Dependent/constructive proofs.** Proof‑carrying content (programs‑as‑proofs).
* **F9 — Univalent/higher foundations.** Equality‑as‑structure; frontier‑grade formal foundations.

**Intent of anchors.** They form a **gentle gradient** from “thinker‑friendly” (F0–F3) through “formalizable” (F4–F6) to **proof‑grade** (F7–F9), allowing the **same artifact** to climb without renaming or forking.

---

### 4.5 · Usage Obligations (declaration, not governance)

* **Declare F.** Every normative episteme **SHALL** declare its **F** (one value) in its context. There is **no default**.
* **Use F in reasoning.** Any comparison, composition, or alignment that depends on rigor **SHOULD** reference **F** explicitly rather than implicit labels like “draft/final.”
* **Do not conflate F with status.** Status systems (ESG/RSG) may **refer** to F in their guards, but **F ≠ status**. This pattern defines **what** rigor is, not **when** a Context should require it.

---

## 5 · Canonical Anchors **F0…F9** (normative)

> **How to read this section.** Each anchor defines *what is minimally true* of an episteme to be rated at that level — across disciplines. The anchors are **ordinal**: F7 is strictly more formal than F6, etc. Levels are **about expression**, not truth; Reliability (R) and ClaimScope (G) are separate.

For every anchor we state **Definition**, **Inclusion criteria**, **Non‑examples** (to prevent over‑rating), and **Indicative artifacts** (cross‑disciplinary, post‑2015).

---

### 5.1 · **F0 — Unstructured Prose**

**Definition.** Free natural language; ambiguous; unstated assumptions; no required sections; meaning depends on reader context.
**Inclusion criteria.** Narrative exists but lacks stable structure; terms may shift meaning; no explicit acceptance/denial conditions.
**Non‑examples.** Any document with a consistent outline and stable vocabulary is at least F1.
**Indicative artifacts.** Whiteboard photos; impromptu email threads; notes from a hallway discussion; an ad‑hoc wiki page with mixed jargon.

---

### 5.2 · **F1 — Scoped Notes**

**Definition.** Informal narrative with a **consistent scope** and **stable terms**; some headings; the central claim/problem is bounded.
**Inclusion criteria.** Key terms are used consistently; scope is named (e.g., “for single‑node scheduling”); still no explicit criteria.
**Non‑examples.** If each requirement already names a check or scenario, that is F2+.
**Indicative artifacts.** A design note that consistently uses the same nouns/verbs and states “this applies to v2 of the service”; a lab memo defining a focus population.

---

### 5.3 · **F2 — Structured Outline**

**Definition.** A **complete template** (Context/Problem/Forces/Solution/…) is populated; content is coherent end‑to‑end; criteria are mostly placeholders.
**Inclusion criteria.** All expected sections exist; cross‑references are consistent; open items are marked (e.g., “TBD acceptance”).
**Non‑examples.** If acceptance criteria are explicit per claim, that is F3+.
**Indicative artifacts.** A draft pattern/spec with fully populated sections but qualitative language; an experiment plan with all slots filled yet non‑operational metrics.

---

### 5.4 · **F3 — Controlled Narrative**

**Definition.** Narrative remains human‑readable but uses **constrained phrasing**; each claim has a **clear, singular interpretation**.
**Inclusion criteria.** Use of controlled NL or disciplined templates (e.g., “shall/if/then”); per‑claim **acceptance statements** exist in prose.
**Non‑examples.** If properties are encoded as logical constraints or typeable Standards, that is F4+.
**Indicative artifacts.** Requirements written in Attempto‑style controlled English; decision rules with explicit pre‑/post‑conditions phrased in a fixed schema.

---

### 5.5 · **F4 — First‑Order Constraints**

**Definition.** Key claims are expressible at **≈ first‑order logic** (FOL) granularity; invariants/constraints are **explicit and checkable in principle**.
**Inclusion criteria.** Each critical statement can be rendered as a predicate over well‑typed variables; conflict/consistency checks are conceivable.
**Non‑examples.** Bare unit tests or executable code without stated invariants is not automatically F4.
**Indicative artifacts.** TLA+ or OCL constraints on a model; an API spec where pre/postconditions and invariants are written as logic‑like rules; well‑typed schema constraints with quantification over entities.

---

### 5.6 · **F5 — Executable Math / Algorithmics**

**Definition.** Content has **precise execution semantics**; results can be checked by **running** (simulation or computation).
**Inclusion criteria.** A model is encoded so that outcomes are deterministic (modulo declared randomness); simulations/tests demonstrate the claims’ executable shape.
**Non‑examples.** “It runs” without a statement of what is guaranteed is not enough; opaque notebooks with side effects but no declared semantics stay F3–F4.
**Indicative artifacts.** Differential‑equation models in code; a reference implementation with clear Standard comments linked to tests; an ML training recipe where the algorithmic pipeline and metrics are fully explicit (yet not proven).

---

### 5.7 · **F6 — Hybrid Formalism**

**Definition.** Combination of **discrete and continuous** reasoning or multiple formal layers; **model‑checking obligations** or equivalent are identified and traceable.
**Inclusion criteria.** Hybrid claims (e.g., controller + plant) are spelled out with both sides’ formalisms and the glue; property checks are specified.
**Non‑examples.** A prose description of cyber‑physical behavior without model obligations is ≤F5.
**Indicative artifacts.** Safety envelopes for autonomous motion expressed as state‑space invariants plus controller logic; hybrid automata with stated safety properties; Standards linking simulation to discrete decisions.

---

### 5.8 · **F7 — Higher‑Order Verified**

**Definition.** Core claims are encoded in a **higher‑order logic (HOL)** or equivalent, and **machine‑checked**; proof scripts or structured proofs exist.
**Inclusion criteria.** The kernel/tool verifies each inference step; failing changes break proofs.
**Non‑examples.** A hand proof attached to F4 constraints without machine checking remains F4–F5.
**Indicative artifacts.** A theorem in Isabelle/HOL or HOL‑Light proving a protocol invariant; a verified algebraic property of a cryptographic scheme.

---

### 5.9 · **F8 — Dependent / Constructive Proofs**

**Definition.** **Programs‑as‑proofs** (Curry–Howard) or **dependent type** artifacts; proof terms are part of the artifact; compilation/type‑check is verification.
**Inclusion criteria.** Types capture the property; changing the property changes the type and breaks the build.
**Non‑examples.** A typed program whose types do not encode the critical property is ≤F5.
**Indicative artifacts.** A Coq/Lean implementation whose type encodes sortedness/safety; a certified compiler pass with proof objects maintained by the build.

---

### 5.10 · **F9 — Univalent / Higher Foundations**

**Definition.** Frontier‑grade **higher foundations** (e.g., homotopy type theory / univalence); equality is treated as **structure**; proofs live at that level.
**Inclusion criteria.** Equivalences are recognized as identities by construction; properties rely on higher equalities.
**Non‑examples.** Any proof that does not hinge on higher‑dimensional equality is ≤F8.
**Indicative artifacts.** Formal developments where isomorphic structures are path‑equal by univalence; higher‑inductive types used to encode core invariants.

---

### 5.11 · Cross‑anchor cautions (normative)

* **Execution ≠ Proof.** Running code/examples (F5) is not a proof (F7+) unless proof obligations are explicitly encoded and checked.
* **Schema ≠ Semantics.** Parseable schemas (F2) are not logical constraints (F4) without semantic predicates.
* **Labels ≠ Levels.** “Approved,” “Final,” or “Published” are **status labels** and have no bearing on F unless they explicitly bind to these anchors.

---

## 6 · Assigning **F** in Practice (guidance)

This section is **informative**. It offers practical heuristics so engineers‑managers can triage artifacts quickly and consistently.

### 6.1 · Three questions to place a first guess

1. **Can a competent reader misread the claim?**
   If yes, you are likely ≤F2. If no (unique reading by construction), you are ≥F3.
2. **Are constraints stated as predicates over typed things?**
   If yes, you are around **F4**; if they are only executable tests without predicates, you’re **F5**.
3. **Would a tool *reject* an incorrect change?**
   If “only by rerunning examples,” that’s **F5**; if “because the logic kernel/type checker refuses it,” that’s **F7–F8**.

### 6.2 · Decision steps (quick rubric)

* **Has complete template?** If not, **F0–F1**. If yes →
* **Are per‑claim acceptances written (even informal)?** If not, **F2**. If yes →
* **Are they predicate‑like (quantifiers, implies, forall/exists)?** If yes, **F4**; if no, **F3**.
* **Is there an executable model with declared semantics?** If yes, **F5–F6** (hybrid if both discrete/continuous).
* **Are core properties machine‑proved?** If yes, **F7**; if types carry the property, **F8**; if higher equivalence is essential, **F9**.

### 6.3 · Litmus tests (do/don’t)

* **Do** point to the **lowest** rigor segment that is essential to the artifact; **F is capped by the weakest required part**.
* **Do** keep **F** independent from **R** and **G**: a well‑verified but informal hypothesis is **low F, high R**; a formal theorem without empirical content is **high F, R=N/A or VA‑lane only**.
* **Don’t** “average” levels: a long F8 appendix does not make an F3 body F8; F sticks to the **claim** or the **episteme**, not to page counts.
* **Don’t** upgrade F just because a tool was used; tooling matters only if the **content** reaches the anchor’s semantics.

### 6.4 · Anti‑patterns

* **Terminology inflation.** Calling acceptance criteria a “specification” without predicates → F3 at most.
* **Notebook mirage.** Treating an executable notebook with hidden state as formal proof → remains F5 without explicit obligations.
* **Schema worship.** Equating JSON Schema validity with logical safety → F2/F3, not F4.
* **Proof‑by‑CI.** “The pipeline is green” is not a logic kernel; without proofs or dependent types, F≤F6.

### 6.5 · Edge cases and how to rate them

* **Generated docs from formal sources.** Rate **by the source**, not the rendered prose. If the source is F7 proofs, the generated PDF remains **F7** as long as it is a faithful view.
* **Natural‑language with embedded formulas.** If formulas are illustrative only, keep **F3**; if they define obligations and are checkable, move **F4–F6** accordingly.
* **Standards in code comments.** If they constrain behavior and are enforced (e.g., via runtime/type checks), consider **F4–F5**; otherwise **F3**.
* **Hybrid ML systems.** The training procedure (executable) suggests **F5**; safety guards as formal constraints can raise parts to **F4/F6**; certified components may reach **F7/F8**.

### 6.6 · Raising **F** (ΔF moves, informative)

Typical **ΔF** steps (see KD‑CAL motion primitives):

* **F2→F3:** Introduce controlled phrasing; per‑claim acceptances.
* **F3→F4:** Recast acceptances as typed predicates/invariants.
* **F4→F5:** Provide executable semantics with declared Standards.
* **F5→F7:** Encode properties in a proof‑capable logic; prove core invariants.
* **F7→F8/9:** Migrate property into types / adopt higher‑equality foundations.

> **Note.** ΔF does not require changing **G** or **R**. Many projects raise F while holding scope and evidence constant, then tackle R (validation) separately.

## 7 · Conformance (normative)

This section defines what it means to **use F correctly** in KD‑CAL. All “**SHALL**/**MUST**/**SHOULD**/**MAY**” statements here are normative.

### 7.1 · Declaration & Semantics

* **CC‑F‑1 (Declaration).** Every normative `U.Episteme` **SHALL** declare exactly one value for `U.Formality` (**F ∈ {F0…F9}**, or a context‑defined sub‑anchor that maps to one of these).
* **CC‑F‑2 (Ordinality).** F is an **ordinal Characteristic**: implementations **MUST NOT** perform arithmetic on F; only comparisons and thresholds are valid.
* **CC‑F‑3 (Polarity).** The polarity of F is **up**: a larger F value denotes **strictly greater or equal** expressive rigor than a smaller one.
* **CC‑F‑4 (No proxies).** Contexts **MUST NOT** introduce alternative “formality modes/tiers” as surrogates for F. If additional labels are desired, they **SHALL** be published as named **sub‑anchors** of F (see §4.3).

### 7.2 · Locality, Extensibility, and Anchors

* **CC‑F‑5 (Local extensibility).** A bounded context **MAY** introduce intermediate anchors (e.g., F6.5) and domain‑named anchors (e.g., “F4‑OCL”), **provided that** (a) the global F0…F9 order is preserved, and (b) each sub‑anchor is explicitly mapped to a parent anchor.
* **CC‑F‑6 (Anchor conservation).** Sub‑anchors **SHALL NOT** redefine the global meaning of their parent anchor (e.g., anything under F8 remains **proof‑grade**).

### 7.3 · Composition & Granularity

* **CC‑F‑7 (Weakest‑link fold).** For any composite episteme (theory, spec, model), the effective Formality **F\_composite** along any essential support path **SHALL** be computed as the **minimum** F of its essential parts on that path.
* **CC‑F‑8 (Granularity rule).** If different parts of an episteme carry different F values, the **episteme‑level F** is the **minimum** over all **essential** parts (non‑essential/illustrative parts are excluded).
* **CC‑F‑9 (No averaging).** Implementations **MUST NOT** average or otherwise combine F values numerically; the min rule suffices.

### 7.4 · Orthogonality & Non‑Interference

* **CC‑F‑10 (Orthogonality to G/R).** Changes in scope/envelope (G) or evidence (R) **SHALL NOT** alter F unless the **expression form** of the claims changes. Conversely, raising F **SHALL NOT** be interpreted as raising R or broadening G.
* **CC‑F‑11 (Notation‑agnostic).** Changing notations or carriers (Symbol side) **does not** change F if the claim graph and its formal content are preserved. Any translation loss is accounted for by **CL** penalties in R, not by altering F.

### 7.5 · Bridges & Cross‑Context Use

* **CC‑F‑12 (Bridges keep F stable).** When a claim is used across bounded contexts via a Bridge, the original F value **SHALL** be preserved in attribution. If the receiving context requires a different expression form, it **MUST** produce a **new episteme** (with its own F).
* **CC‑F‑13 (CL is for trust, not F).** Any mismatch across contexts **SHALL** be handled via Congruence Level (CL) and its effect on R; CL **MUST NOT** be used to down‑rate F.

### 7.6 · Traceability & Change

* **CC‑F‑14 (Observable basis).** An assigned F **SHALL** be justifiable by observable content (e.g., presence of predicates/invariants for F4; mechanized proofs for F7+).
* **CC‑F‑15 (ΔF disclosure).** A **ΔF** move (raising or, if justified by discovered error, lowering F) **SHALL** be recorded as a content change to the episteme. Whether a context versions that change is outside this pattern’s scope.

---

## 8 · Composition & Interaction (normative + informative notes)

### 8.1 · Inside one episteme (normative)

* **Essential paths.** Identify essential parts/claims that are required for the episteme’s truth. Apply **min‑F** along each support path; the **episteme‑level F** is the min over essential paths (CC‑F‑7, CC‑F‑8).
* **Episteme‑about (ReferencePlane=episteme).** Descriptions about other claims/epistemes carry their **own** F and do **not** raise the target’s F; any cross‑plane penalty flows via **CL^plane → R**.

> **Note (informative).** A long formal appendix (F8) attached to a largely narrative body (F3) does **not** make the whole F8; the episteme remains **F3** unless the core claims move into the formal appendix.

### 8.2 · Relation to **G** (scope/envelope) (normative)

* F concerns the **expression form** of the claim; G concerns its **claim scope**. Tightening the envelope without changing how the claim is expressed does not change F; re‑expressing the claim in a stricter form (e.g., predicates) can raise F without changing G.

> **Caution (informative).** Raising F often **reveals** hidden assumptions, which may lead to a **ΔG** (narrower envelope). Treat this as a **separate** change: update G explicitly rather than smuggling scope changes under F.

### 8.3 · Relation to **R** (evidence/assurance) (normative)

* **F ≠ R.** Proof‑grade expression (F7+) still requires binding to appropriate assurance lanes (VA/LA/TA) in the trust calculus; empirical claims may have high R with low F if they remain informal.
* **Decay independence.** F **does not decay** with time; R may decay (empirical freshness) or shift due to CL. Tool assurance (TA) is tracked independently of F.

> **Note (informative).** Higher F typically **enables** stronger R (easier to test or prove), but no automatic relationship is assumed.

### 8.4 · CL & Bridges (normative)

* **CL effects.** Using content across context boundaries requires a Bridge with a CL rating. CL affects **R** (penalties) and **never** changes **F** (CC‑F‑12/13).
* **Semantic change ⇒ new episteme.** If a cross‑context mapping **alters** the claim (e.g., coarsens predicates, drops obligations), treat it as a **new episteme** with its own F rather than “the same F with lower CL.”

### 8.5 · Motion primitives (informative)

* **ΔF** raises or (rarely) lowers the rigor of expression. Plan ΔF moves independently of **ΔG**/**ΔR**: projects often alternate “raise F” (make the claim checkable) with “raise R” (gather proof/validation) at a fixed G.
* **Cost signals.** Typical costs: authoring overhead (F3→F4), model encoding (F4→F5/6), proof engineering (F6→F7/8). The benefit is reduced ambiguity and safer composition.

### 8.6 · Gaps & thresholds (informative)

* **F‑gap** = ordinal difference between two F anchors (no arithmetic). Large gaps signal translation risk: an F8‑level component will not accept informal inputs (F2) except via additional formalization (ΔF) or robust alignment (CL‑guarded).

---

## 9 · Worked Examples (informative)

> Each mini‑case states the artifact, assigns **F**, and notes interactions with **G/R**. Examples are deliberately cross‑disciplinary to stress transdisciplinary comparability.

### 9.1 · Research hypothesis (physics)

**Artifact.** Short note proposing a new scaling law; clear vocabulary; scope “low‑Reynolds flows in microchannels.”
**F.** **F3** (controlled narrative with per‑claim acceptance in prose).
**G/R.** G is a narrow physical envelope; R is initially low (hypothesis).
**Next ΔF.** Recast acceptance as predicates over variables → **F4**; encode a simple simulation harness → **F5**.

### 9.2 · API specification (software)

**Artifact.** REST API doc with request/response schemas and explicit pre/postconditions; invariants like “idempotent under retry.”
**F.** **F4** (first‑order constraints).
**G/R.** G = stated resource model; R improves via conformance tests (independent).
**Next ΔF.** Reference implementation and executable test suite with declared Standards → **F5**; model‑check idempotence under failure injection → **F6**.

### 9.3 · Safety controller (cyber‑physical)

**Artifact.** Controller with plant model; safety distance invariant and braking envelope defined and verified in a hybrid model checker.
**F.** **F6** (hybrid formalism with obligations checked).
**G/R.** G = operating envelope (speed ranges, road conditions); R increases via track tests and simulation coverage.
**Next ΔF.** Encode key invariants in HOL and prove monotonicity → **F7**; migrate safety property into dependent types in the control kernel → **F8**.

### 9.4 · Decision policy (management)

**Artifact.** Escalation policy: if risk score ≥ θ and budget slack ≤ β, escalate to committee; otherwise defer.
**F.** **F3→F4** depending on phrasing. If the thresholds and variables are typed and the rule is predicate‑like, rate **F4**.
**G/R.** G = organizational scope (which portfolios, time windows); R entails retrospective calibration (did escalations match outcomes?).

### 9.5 · Verified algorithm (theory/software)

**Artifact.** Sorting function implemented with a dependent type ensuring output is ordered and a permutation of input; proof included.
**F.** **F8** (dependent/constructive proof).
**G/R.** G = data types and preconditions; R (empirical) is irrelevant; VA lane suffices (proof stands).

### 9.6 · ML classifier (data/ML)

**Artifact.** Training pipeline fully specified; metrics defined; OOD detection configured; no formal invariants.
**F.** **F5** (executable algorithmic semantics).
**G/R.** G = data distributions and deployment envelope; R grows with validation/monitoring.
**Next ΔF.** Add formal constraints for safety (e.g., monotonicity in features) → **F4/F6** for those aspects; certified post‑processing may achieve **F7** for a slice.

### 9.7 · Meta‑specification (method description)

**Artifact.** A guideline on how to review specs; it includes checklists and litmus tests.
**F.** **F3–F4** depending on whether checks are predicates.
**Interaction.** Its F does **not** lift the F of the reviewed artifacts; it only affects **R** via better CL (clearer alignments and fewer losses).

## 10 · Authoring & Review Guidance (informative)

This section helps engineering managers, architects, and researchers **assign F consistently**, plan **ΔF moves**, and **review** claims without slipping into status/process language.

### 10.1 · For authors — placing and raising **F**

* **Start honest.** If you’re drafting ideas in plain prose, declare **F0–F1**. You are not “behind”; you’re **appropriately early**.
* **Stabilize vocabulary first.** Move to **F2–F3** by making terms stable and acceptance statements unambiguous (controlled phrasing).
* **Name predicates next.** When acceptance can be written as **typed predicates** (“for all …, if … then …”), you have reached **F4**.
* **Give semantics to execution.** When readers can **run** a model/algorithm with *declared* semantics and see outcomes aligned with the predicates, you are in **F5** (hybrid + obligations → **F6**).
* **Prove what matters.** When the **logic kernel/type system** will **reject** incorrect changes to core claims, you are at **F7–F8**; if equality as structure is essential, **F9**.
* **Keep identity.** Prefer **ΔF** on the *same* episteme (raising rigor stepwise) over creating new documents; this keeps provenance and reduces translation error.

**Typical ΔF plan:** *Sketch (F1) → Controlled narrative (F3) → Predicates (F4) → Executable semantics (F5/6) → Machine‑checked core (F7/8).* Scope (G) and evidence (R) can remain fixed while F rises.

### 10.2 · For reviewers — verifying the declared **F**

Use **observable checks**:

* **F2?** Template is complete; terms don’t drift; “TBD” acceptance is explicitly marked.
* **F3?** Every claim has a **single reading** via constrained phrasing; hidden ambiguity is flagged.
* **F4?** Each critical claim is **predicate‑like** (typed variables, quantifiers/implication allowed); conflicts are **checkable in principle**.
* **F5?** Executable **semantics are declared**; runs/tests are not ad‑hoc but trace back to claims.
* **F6?** Hybrid obligations are **identified and linked** (discrete + continuous, or layered formalisms).
* **F7/8?** Incorrect edits to core claims are **rejected by the kernel/type system**; proof/scripts or proof‑objects exist and are traceable.
* **F9?** Higher equalities are **first‑class** (e.g., univalence), and core results rely on them.

**Failure modes to watch:** “green CI” as proof; schema validation treated as semantics; notebooks without declared semantics; long formal appendix while the main claim stays informal (rate by the **weakest essential part**).

### 10.3 · For integrators & architects — using **F** in composition

* **Plan around the minimum.** In any composition, **F\_composite = min F\_parts** along essential paths. Identify the **bottleneck F** first; your ΔF effort goes there.
* **Mind the F‑gaps.** Large ordinal gaps (e.g., F7 vs F2) imply translation risks and alignment costs. Either **raise** the low‑F part or insert **bridges** with explicit scope and confidence impacts (handled in **R** via **CL**).
* **Don’t upgrade by proximity.** An F8 component does not “elevate” an F3 neighbor. Keep F independent and visible.

### 10.4 · For assurance leads — relating **F** to **G/R** without conflation

* **F enables, R assures.** Raising **F** makes evidence easier to formulate and check; it does not **create** evidence. Rate R separately (calibration/validation/monitoring vs proof lanes).
* **G is separate.** Tightening **G** (scope/envelope) may accompany ΔF (as assumptions become explicit) — treat this as a **ΔG** move, not a side effect.
* **Use thresholds explicitly.** If a context expects “formalized before use,” write guard conditions as **`F ≥ k`**, not as status labels.

### 10.5 · Common pitfalls & remedies

| Pitfall                                   | Remedy                                                                                          |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Calling structured prose a “formal spec.” | If acceptance isn’t predicate‑like, rate **≤F3** and plan **ΔF: prose → predicates (F4)**.      |
| Treating runnable code as proof.          | Declare **F5**; add **stated obligations** and property checks to progress **F6–F7**.           |
| Averaging F across parts.                 | Use **min over essential parts**; if unsure which parts are essential, audit the support graph. |
| Letting status leak into F.               | Keep **status** (e.g., “accepted here”) separate; **F** is about expression only.               |

---

## 11 · Glossary & Notation (normative where noted)

**Formality (F).** `U.Formality` — an **ordinal Characteristic** with polarity **up**; default anchors **F0…F9** (§5). *(Normative)*

**Anchor (F‑anchor).** A named qualitative milestone on the F scale (e.g., F4 “first‑order constraints”). Sub‑anchors are context‑local refinements that **preserve order**. *(Normative)*

**ΔF.** A change to the expression form that alters F (usually **up**). Record as an episteme content change. *(Normative)*

**Essential part/path.** A part or claim without which the episteme’s central assertion does not hold. Composition applies **min‑F** along essential support paths. *(Normative)*

**Predicate / Invariant.** A typed, checkable statement about objects/states; at **F4** and above, critical claims are expressed as such.

**Machine‑checked / Proof‑carrying.** Content for which a logic kernel/type system rejects incorrect changes (F7+) or where programs and proofs are the same artifact (F8).

**Higher equality / Univalence.** Treatment of equivalence as identity in higher foundations relevant at **F9**.

**Notation & examples.**

* Declare as `F = Fk` (e.g., `F = F4`).
* Sub‑anchor: `F = F4[OCL]` or `F = F7[HOL]`.
* Thresholds in prose: “requires **F ≥ F6** for core claims.”
* Mixed parts: list per part if useful (e.g., “Body F3; Appendix proofs F7 — **episteme F3**”).

---

## 12 · Change Log & Patch Notes (normative migration)

**12.1 Supersession.**
This pattern **supersedes** the legacy “modes/tiers” language. Any references to “M‑mode/F‑mode”, “publication tiers”, or parallel “formality ladders” are **deprecated**. From now on, **Formality** is expressed **only** as **F** with default anchors **F0…F9** (and optional sub‑anchors per §4.3).

**12.2 Impacted cross‑references.**

* **C.2.2 (F–G–R).** Replace any generic “F‑ladder” description with a normative reference to **C.2.3** and treat **F** in the triple as defined here (including **min‑F** composition).
* **ESG/RSG text.** Where guards previously referenced “modes/tiers,” rewrite guards as **`F ≥ Fk`** conditions.
* **Meta‑descriptions.** Ensure meta‑artifacts carry **their own F** and do not “lift” a target artifact’s F; use **CL→R** for cross‑context penalties, not F changes.

**12.3 Transitional guidance.**

* **Legacy artifacts without F.** Assign an initial F by applying the rubric in **§6**; record the assignment as a content attribution (not as a status change).
* **Legacy labels in prose.** Replace them with explicit **F** declarations. If prose implies mixed rigor, rate by the **weakest essential** segment (see §7.3).
* **No dual systems.** Do not keep “modes” alongside F; remove proxies and speak **F directly**.

**12.4 Backward compatibility (non‑normative note).**
During editorial refresh, it is acceptable to annotate historical records with both the **new F** and the legacy note for provenance. Forward‑looking reasoning and composition, however, **SHALL** use **F only**.

**12.5 Versioning & edits.**
Raising or (exceptionally) lowering **F** constitutes a **content change** (ΔF). Whether such a change triggers a new edition in a given Context is **outside this pattern**; respect the Context’s edition policy while keeping **F** accurate.

# C.3 · **Kind‑CAL — Kinds, Intent/Extent, and Typed Reasoning**  \[A]

> **One‑line summary.** Establishes **`U.Kind`** as the **minimal, context‑local intensional carrier** of “what a statement is about,” separates **intent** (KindSignature + its own **F**) from **extent** (*which* instances belong to the kind **in a given Context slice**), and situates **typed reasoning** alongside **USM Scope (G)** and **F–G–R** without conflation. Details of the core objects and operations live in **C.3.1–C.3.5**; guard shapes are standardized in **C.3.A**.

---

## 0 · Status, Placement, Dependencies & Sub‑pattern Map  \[A]

**Status.** Normative architheory in **Part C**. Identifier **C.3**. This pattern lays the **architectural invariant** and manager‑level guidance. The **mechanics** are defined by its child patterns.

**Readers.** Engineering managers, architects, and assurance leads who must reason about *typed claims* across Contexts without mixing up **describedEntity** (Kinds), **applicability** (**G**), and **assurance** (**R**).

**Depends on.**
— **A.2.6 USM** (Context slices & Scopes): **`U.ClaimScope` = G**, **`U.WorkScope`**, ∈/∩/**SpanUnion**/translate, **Γ\_time** policy, Bridges + **CL** (scope).
— **C.2.2 F–G–R**: weakest‑link composition; penalties to **R** for Cross‑context congruence (CL).
— **C.2.3 Unified Formality F**: F0…F9 as an **ordinal Characteristic** (expression rigor).

**Sub‑patterns (normative unless noted).**
— **C.3.1** · `U.Kind` & `U.SubkindOf` (partial order).
— **C.3.2** · `KindSignature` (**intent**, with **F**) & `Extension/MemberOf` (**extent** in a slice).
— **C.3.3** · **KindBridge** & **`CL^k`** (type‑congruence; penalties route to **R**).
— **C.3.4** · **RoleMask** (context‑local adaptation without cloning kinds).
— **C.3.5** · **KindAT** (K0…K3, **informative facet**, not a Characteristic).
— **C.3.A** · **Typed Guard Macros** (annex): admit/compose, masks, Cross‑context reuse; AT is **forbidden** in guards.

**Deprecations.**
— “**Generality ladder**” for **G**; **G is Scope** only (set‑valued over `U.ContextSlice`).
— Any “**Kind scope**” characteristic (Kinds carry **intent/extent**, not Scope).
— **Mark as legacy** any uses of **‘validity’ as a Characteristic** or **‘operation’ as a Scope‑like Characteristic**; **redirect** to **`U.ClaimScope`** / **`U.WorkScope`** (A.2.6) for applicability. Editors SHOULD add glossary redirects in Part E.

**Editorial note (cut‑over).** Content formerly in C.3 that defined guard shapes, decision trees, and macro anti‑patterns now resides in **C.3.A**. Membership **evaluation obligations** live in **C.3.2** with `MemberOf`.

---

## 1 · Purpose & Rationale  \[A/I]

**What you get.**

1. A **neutral typed layer**: name *what* a claim quantifies over (**Kinds**) without binding to any particular “type technology” (OWL, PL types, shapes…).
2. A clean **split of characteristics**:
   – **Scope (G)** = *where* a claim holds (USM, set‑valued over **Context slices**).
   – **Kind extent** = *which instances* belong to a kind **inside** a given slice.
   – **F** = *how strictly* content is expressed (C.2.3).
   – **R** = *how well supported* (evidence & congruence penalties).
3. **Typed reuse across Contexts**: a dedicated **KindBridge** with **`CL^k`** (type‑congruence), so you can predict risk **without** touching F or G.
4. **Manager‑oriented maps**: when to invest in **formalization** (F), when to expand/narrow **Scope** (ΔG), when to test across **subkinds** (R), and what kind of **bridge** you should expect.

**Why it helps.**
Teams routinely overspend on proofs for **instance‑level** questions and underspecify scope for **class‑level** claims. By naming the **Kind**, you plan **ΔF/ΔR** correctly and keep **G honest**. Typed checks also block unsafe compositions (“we were talking about different things”).

---

## 2 · Context  \[I]

Cross‑disciplinary work mixes artifacts that *look like “types”* but behave differently: ontology classes, schema “shapes,” programming types, BORO super/sub categories, ad‑hoc labels. At the same time, **USM** made “scope” precise. What was missing was a *small, neutral* notion of **describedEntity** that (a) **does not** re‑invent a global “type system,” (b) composes with USM and F–G–R, and (c) lets Contexts keep their idioms—**with bridges** when crossing boundaries.

---

## 3 · Problem  \[I]

1. **Scope–type conflation.** Authors try to widen **G** by “abstracting the wording,” yielding claims that *sound* general but are only supported on a thin slice.
2. **Silent drift across Contexts.** A “vehicle” here is not the same as a “transport unit” there; reuse proceeds without a declared mapping or risk accounting.
3. **Wasteful planning.** Without a signal about the *kind‑level*, teams either over‑formalize single‑slice decisions or under‑test class‑level claims (no variant coverage along subkinds).
4. **Unsafe composition.** Claims about incompatible “things” get composed because the describedEntity was implicit in prose.

---

## 4 · Forces  \[I]

| Force                             | Tension to resolve                                                                                 |
| --------------------------------- | -------------------------------------------------------------------------------------------------- |
| **Local freedom vs global sense** | Contexts need their own vocabularies; Cross‑context work needs a common skeleton for **describedEntity**.      |
| **Minimality vs utility**         | The notion of kind must be tiny yet powerful enough to guide ΔF/ΔR/bridges/composition.            |
| **Intent vs extent**              | Kinds come with a **definition** and a **population in place**; both are needed and must not mix.  |
| **Typed discipline vs F–G–R**     | Typed safety must not distort **G** (Scope) nor introduce a parallel “assurance math.”             |
| **Abstraction vs applicability**  | “Higher abstraction” is **not** “wider applicability”; the framework must make this split obvious. |

---

## 5 · Solution — Architectural Decisions (overview)  \[A]

**C.3‑D1 — `U.Kind` is intensional and context‑local.**
Kinds name *what a claim quantifies over*. They form a partial order **`⊑`** (**SubkindOf**). *(See C.3.1.)*

**C.3‑D2 — Separate **intent** and **extent**.**
— **KindSignature(k)**: the intensional content (predicates/invariants/Standards). It carries its **own F** (C.2.3).
— **Extension(k, slice)**/**MemberOf**: which instances belong to `k` **in a given `U.ContextSlice`**. *(See C.3.2.)*

**C.3‑D3 — Kinds do **not** carry Scope.**
**Scope** lives with **claims/capabilities** (USM): a set of **Context slices** where the statement holds. Kinds carry **intent/extent** only. *(USM A.2.6 + C.3.2.)*

**C.3‑D4 — Typed reuse across Contexts is explicit.**
Use a **KindBridge** with **`CL^k`** (type‑congruence) and loss notes. Its effect is **only via R** penalties; **F/G remain unchanged**. *(See C.3.3.)*

**C.3‑D5 — Local adaptation without cloning.**
Use a **RoleMask** to bind a kind to Context‑specific constraints/aliases; promote to a **subkind** if the mask becomes stable and widely reused. *(See C.3.4.)*

**C.3‑D6 — An **informative** “abstraction tier” exists for Kinds (AT: K0…K3).**
A facet (not a Characteristic) that helps plan **ΔF/ΔR** and forecast bridge style; **AT never appears in guards**. *(See C.3.5.)*

**C.3‑D7 — Guard shapes are standardized and fail‑closed.**
Typed compatibility first (same‑Context **`⊑`** or **KindBridge**), then **Scope coverage** (USM), then **R** penalties and freshness. *(See C.3.A.)*

> **Manager’s picture — Two characteristics (keep them separate).**
> – **characteristic 1 (USM, G):** *Where* the claim holds → set of **Context slices**; composed by ∈ (membership) / ∩ (intersection) / **SpanUnion** (union across independent lines) / translate (scope mapping).
> – **characteristic 2 (Kind extent):** *Which instances* in a **given slice** belong to the kind → `MemberOf(e, k, slice)`.
> **Never “widen G” by abstract wording; widen only by ΔG with support.**

---

## 6 · Core Concepts (informative summary; authoritative norms live in C.3.1–C.3.5)  \[I]


> This section fixes the **Standard** of terms used in C.3 and points to the sub‑patterns for complete mechanics. All “**SHALL/MUST**” statements here are normative.

**Editorial note.** This section is **informative**. It restates manager‑level takeaways and **points to** the canonical, normative rules in **C.3.1–C.3.5**. Where this section summarizes a rule, treat the cited sub‑pattern (and rule ID) as the **source of truth**.


### 6.1 · `U.Kind` & `U.SubkindOf (⊑)`  \[A]

**Definition.** `U.Kind` is a **context‑local intensional object** naming a “kind of thing” that claims may quantify over.
**Order.** `U.SubkindOf (⊑)` is a **partial order** (reflexive, transitive, antisymmetric). We write `k₁ ⊑ k₂`.

**Summary of norms** *(authoritative text: **C.3.1 K‑01–K‑02**)*.
— Contexts treat `⊑` as a partial order and document any computed meets/joins if they provide them.
— Kinds do not carry Scope; Scope remains on claims/capabilities (USM).

> *Full treatment:* **C.3.1** (definitions, invariants, examples).

---

### 6.2 · **KindSignature** (intent) & **F**  \[A]

**Definition.** `KindSignature(k)` is the **intent**: predicates/invariants/Standards that define the kind in the Context. Its expression rigor has an explicit **`U.Formality`** (C.2.3).

**Summary of norms** *(authoritative text: **C.3.2 K‑03–K‑04**)*.
— `KindSignature(k)` declares its F (C.2.3). Claim‑level F does **not** auto‑inherit; weakest‑link applies on the claim’s own support paths.
— If a signature change alters membership, treat it as a content change (Contexts may version kinds).

> *Full treatment:* **C.3.2** (signature/intent with F; relation to claims).

---

### 6.3 · **Extension** & **MemberOf** (extent in a slice)  \[A]

**Definition.** `Extension(k, slice) ⊆ EntitySet(slice)` = set of instances that belong to `k` **in the given `U.ContextSlice`**. `MemberOf(e, k, slice)` is the membership predicate: `e ∈ Extension(k, slice)`.

**Summary of norms** *(authoritative text: **C.3.2 K‑05–K‑08**)*.
— Membership is deterministic for a fixed `(k, slice)` (no hidden “latest”).
— If `k₁ ⊑ k₂`, then `Extension(k₁,slice) ⊆ Extension(k₂,slice)` for all slices.
— Definedness may be bounded; outside it, guards fail closed.
— Keep **Scope (G)** and **MemberOf** as distinct guard predicates.

> *Full treatment:* **C.3.2** (extent semantics, examples, authoring hints).

---

### 6.4 · **KindBridge** & **`CL^k`** (type‑congruence)  \[A]

**Summary of norms** *(authoritative text: **C.3.3 KB‑01–KB‑12**)*.
— A KindBridge states Contexts/versions, kind mapping/rules, preserved order links, **`CL^k`** anchors, loss notes, and definedness.
— No inversions of preserved subkind links; collapses must be declared.
— When classification depends on a KindBridge, apply a monotone penalty **Ψ(`CL^k`)** to **R** (scope‑bridge **Φ(CL)** applies separately). **F** and **G** remain unchanged.
— Chaining uses weakest‑link on **`CL^k`**.

> *Full treatment:* **C.3.3** (bridge shape, anchors, examples).

---

### 6.5 · **RoleMask** (adaptation without cloning)  \[A]

**Definition.** `U.RoleMask(kind, Context)` is a **named binding** that carries constraints (optional **narrowing** of membership), vocabulary/notation aliases, and intended use for local procedures—**without** creating a new Kind.

**Summary of norms** *(authoritative text: **C.3.4 RM‑01–RM‑08**)*.
— Masks are registered/versioned; constraints are observable/deterministic at guard time.
— Do not treat masks as kind synonyms; promote frequently reused constraint masks to explicit subkinds (`⊑`).


> *Full treatment:* **C.3.4** (mask taxonomy, guard discipline, promotion rule).

---

### 6.6 · **KindAT (K0…K3)** — *informative facet*  \[I]

**Status.** A **facet** attached to `U.Kind`, not a Characteristic: no algebra, **never** used in guards or composition.

**Anchors (intentional view).**
**K0** Instance; **K1** Behavioral pattern; **K2** Formal kind/class; **K3** Up‑to‑Iso.

**Use.** Helps plan **ΔF/ΔR** and forecast bridge style (e.g., K3↔K3 suggests up‑to‑iso mapping). Do **not** conflate AT with **G** or **R**.

> *Full treatment:* **C.3.5** (manager heuristics, anti‑misuse).

---

### 6.7 · Quick examples (two‑characteristic awareness)  \[I]

**E‑Sketch 1 — Policy over `Vehicle`.**
Claim: “For all `x ∈ Vehicle`: brakeDistance(x) ≤ 50 m (dry), ≤ 40 m (wet).”
– **describedEntity:** `Vehicle` (Kind, typically K2) — *what* we quantify over.
– **Scope (G):** `{surface∈{dry,wet}, speed≤50, rig=v3, Γ_time=rolling 180d}` — *where* the claim holds.
– **Extent in slice:** which instances the lab currently classifies as `Vehicle` (via `MemberOf`).
Typed checks happen **before** Scope intersection; **G** is not widened by “abstract wording.”

**E‑Sketch 2 — API rule over `AuthenticatedRequest`.**
Producer A emits `Request`; consumer B expects `AuthenticatedRequest`.
– If `Request ⊑ AuthenticatedRequest` **does not** hold, add an **adapter** or adopt a **subkind**; do **not** force fit by widening **G**.
– Scope remains independent (API version, Γ\_time policy); evidence/freshness sits in **R**.

## 7 · How to use typed reasoning \[A/I]

## 7.1 How typed reasoning plugs into **F–G–R & USM**

### 7.1.1 · The basic shape of a typed claim (manager view)  \[I]

A typed claim has two independent parts:

1. **describedEntity (Kind).** *Which things the statement talks about.*
   “For every item of kind **k** in the **target context** (the selected **TargetSlice**) …”.
   — The **definition** of kind **k** lives in **KindSignature(k)** (with its **F**, C.3.2).
   — **Which items count as “k”** is evaluated in the **TargetSlice** (C.3.2) by a deterministic membership check.

2. **Applicability (Scope, G).** *Where the statement holds.*
   `U.ClaimScope(Claim)` is the **collection of contexts** where the claim is valid (USM A.2.6). Guards test: “Scope **covers** the TargetSlice”.

**Discipline.** The guard first checks **typed compatibility** (in the same Context: “is‑a / subkind‑of”; across Contexts: a **KindBridge**, C.3.3), then **Scope coverage** (USM), then **R** freshness and any bridge congruence penalties. See **C.3.A Guard\_TypedClaim**.

---

### 7.1.2 · Composition of typed claims  \[A]

**Rule C‑T‑1 (typed pre‑check).** To compose a **producer claim** with a **consumer claim**, where the producer quantifies over kind **k (source)** and the consumer expects kind **k (expected)**:

* **same Context:** require **“is‑a / subkind‑of”** to hold (the source kind is a subkind of the expected kind) (C.3.1).
* **Cross‑context:** require a **KindBridge** that maps the source kind to a **local kind that is a subkind of the expected kind** in the target Context (C.3.3). If neither holds, the composition is **unsafe**; introduce a subkind, add an adapter (or a RoleMask), or decline.

* **Role‑aware option (same Context):** if the consumer expects a **RoleMask** over the expected kind, you may satisfy the mask’s explicit constraints (C.3.4) instead of changing kinds, provided those constraints are observable at gate time.

**Rule C‑T‑2 (scope after type).** After typed compatibility is satisfied, compute Scope as in USM:

* **Serial path:** take the **intersection** of the contributors’ claim scopes.
* **Parallel independent lines:** use **SpanUnion** of the serial scopes (only if independence is justified).

**Rule C‑T‑3 (no type‑by‑scope).** A kind mismatch **MUST NOT** be “fixed” by widening **G**. Changes in describedEntity require **subkind introduction**, **signature edits**, or a **KindBridge**—not a scope change.

**Manager hint.** First confirm the **port shape** matches (kinds line up), then check the **operating area** (scope), and finally look at **confidence** (evidence freshness plus any bridge congruence penalties).

---

### 7.1.3 · F–G–R with typed claims (what changes, what doesn’t)  \[A/I]

* **F (Formality).**
  – **Claim‑level F** follows C.2.3 (weakest‑link along the claim’s support paths).
  – **KindSignature F** is declared **on the kind** (C.3.2) and influences claims **only** if the claim essentially depends on those predicates (weakest‑link again).
  – **Raising F** can *reveal* hidden assumptions (which may trigger ΔG in the claim), but **does not change G** by itself.

* **G (Scope).**
  – Always **set‑valued over Context slices** (USM A.2.6).
  – Typed reasoning does not alter G’s algebra (∈/∩/SpanUnion/translate).
  – Never infer Scope from “how general the wording sounds.”

* **R (Reliability).**
  – Evidence freshness/decay (validation windows) remains separate from Scope coverage.
  – **Cross‑context penalties** split cleanly: a **scope‑bridge penalty** (USM) and a **kind‑bridge penalty** (C.3.3). Both **reduce R only**; neither changes **F** or **G**.

**Manager rule of thumb.**
Start with the reliability from your support; then **apply the scope‑bridge penalty**; then **apply the kind‑bridge penalty**. Each step can only reduce reliability.  
You never add or average **F/G**: you **compose scope** per USM rules and apply **weakest‑link** for F/R along support paths.

---

### 7.1.4 · ESG gating with typed claims  \[A]

* **Gate on F**, if your Context requires rigor before use (e.g., `U.Formality(Claim) ≥ F4`).
* **Gate on Scope coverage** (USM) and an explicit **time selector** (Γ_time) policy.
* **Gate on R freshness** and **minimum congruence** for bridges (e.g., `CL ≥ 2`, `CL^k ≥ 2`).
* **Do not** gate on **AT** (C.3.5); it is an informative facet only.
* Use **C.3.A guard macros** to keep guards short and auditable.

### 7.2 · How typed reasoning plugs into the CAL chain (Lang‑CHR → Role‑CAL)  \[A/I]

> **Intent.** Show a clear, end‑to‑end path a manager can follow to take a typed claim from words to safe reuse across Contexts—without any tool or data‑governance assumptions. Each stage says **what it supplies**, **what it needs**, and **what it hands off** to the next stage.

---

#### 7.2.1 **Lang‑CHR** — stable words first  \[A/I]

**What it supplies.** A disciplined vocabulary and controlled phrasing so that terms like *Vehicle*, *AuthenticatedRequest*, *AdultPatient* have **one meaning** in the Context.

**What it requires.** Authors use controlled narrative (C.2.3 **F3**) at minimum: single‑meaning terms, explicit “shall / if / then”, and no drifting synonyms.

**Hand‑off.** A small, curated lexicon entry for each candidate *Kind‑word*; these become **`U.Kind` names** in the next step.

> *Manager hint.* If two teams cannot agree on the noun, you are not ready to type the claim. Resolve the noun in Lang‑CHR before introducing a Kind.

---

#### 7.2.2 **Kind‑CAL** (this Part) — name the *describedEntity*  \[A]

**What it supplies.**
• **`U.Kind`** objects for those nouns; a partial order **`⊑`** (subkind‑of).
• **KindSignature(k)** (intent), with declared **F**.
• **Extension(k, slice)** and **`MemberOf(e,k,slice)`** (extent).
• (Optional) **AT (K0…K3)** as an **informative facet**.

**What it requires.**
• Deterministic membership (no “latest” defaults) and a clear rule for where membership is defined in each context.
• No “Kind scope”: Scope remains with claims/capabilities (USM).

> *Manager hint.* Use the kind’s **AT tag** only as a planning signal (where to invest rigor and tests). AT never gates decisions and never widens scope.

**Hand‑off.** Typed quantifier sites for claims: “∀ x ∈ **Extension(k, slice)** …”, plus a visible **`⊑`** lattice for compatibility checks down the line. Typed claim sites written in Plain language: “for every item of kind **k** in the **target context** …”, plus a visible **subkind‑of** lattice for compatibility checks down the line.

> *Manager hint.* Decide early whether your Kind is K0 (instance‑ish) or K2 (formal class). It sets your **ΔF/ΔR** budget expectations.

---

#### 7.2.3 **Structure‑CAL** — give Kinds usable shape  \[A/I]

**What it supplies.** Structural building blocks **on Kinds**:
• **combinations** (“and”),
• **alternatives** (“either/or”),
• **records** (named fields),
• **functions** (inputs to outputs),
plus relations like **has‑attribute** and **part‑kind**, and the minimal invariants those structures must respect.

**What it requires.**
• Do not hide Scope inside structure.
• Put structural rules into the **KindSignature** as checkable statements (ideally **F4+**).

**Hand‑off.** Typed *ports and shapes* of claims/specifications (“this policy expects `PassengerCar × ControllerConfig`”), making compatibility checks crisp before any Scope math.

> *Manager hint.* If two claims expect different shapes (for example, one needs “Vehicle with ABS”, the other just “Vehicle”), plan a **subkind** or an **adapter**. Do not “solve” it by rewording the claim.

**Note (informative).** If a Context declares structural constructors on kinds (e.g., product/sum/record/function), editors SHOULD document the corresponding **Extension** inclusion laws for those constructors. Keep Scope in USM; do not hide it in structure.

---

#### 7.2.4 **Compose‑CAL** — compose with typed pre‑checks  \[A]

**What it supplies.** The **order of checks** you must follow for safe composition:

1. **Typed compatibility**: in the same Context, the producer’s kind **is a subkind of** the consumer’s kind; across Contexts, a **KindBridge** maps the producer’s kind to a local kind that fits, with an acceptable **kind‑bridge congruence level** (C.3.3).
2. **Scope checks** (USM): along dependency paths, take the **intersection** of scopes; use **SpanUnion** only when support lines are truly independent.
3. **Assurance wiring**: apply the **scope‑bridge penalty** and the **kind‑bridge penalty** to **R**; check evidence freshness separately.

**What it requires.** Independence justification for **SpanUnion**; no “type‑by‑scope” fixes.

**Hand‑off.** A typed, scope‑checked composition that survives audit because each risk is accounted for in **R**.

> *Manager hint.* Run the **typed pre‑check** first. It is the cheapest failure to catch and prevents “scope gymnastics” that mask a type mismatch.

---

#### 7.2.5 **CT2R‑LOG** — speak the logic, keep the math honest  \[A/I]

**What it supplies.**
• A clear logical reading of your typed claim: “for every item of kind **K**, condition **φ** holds” (or “there exists an item …”).
• Rules for refinement and substitution that respect the **subkind‑of** relation.
• When appropriate (K3), reasoning that treats structures as **equivalent up to isomorphism** (useful where exact identity is the wrong notion).

**What it requires.**
• Pick a logic that matches the **Formality** you declare (e.g., machine‑checked logic for higher **F**).
• When the logic travels across Contexts, use a **KindBridge** to keep meaning aligned; any mismatch is reflected as a **kind‑bridge penalty** in **R**.

**Hand‑off.** Proof obligations or reasoning templates that are consistent with your Kind/Structure setup and do not alter **G**.  **Shall‑note CT2R‑1.** Transferring typed formulas that depend on `MemberOf` across Contexts **uses a KindBridge**; any mismatch is accounted as **Ψ(`CL^k`)** in **R**. **F** and **G** remain unchanged. For **up‑to‑iso** situations, see **C.3.5 (AT)** for when K3 is appropriate.

> *Manager hint.* If your proof keeps failing when you move between Contexts, add a **bridge at the Kind level**; do not try to “fix” it by changing scope.

---

#### 7.2.6 **Role‑CAL** — adapt without cloning  \[A]

**What it supplies.** **RoleMask(kind, Context)**: a named, registered adaptation (extra constraints or local aliases, with optional narrowing) that reuses the **same** kind instead of creating a new one.

**What it requires.**
• Constraints must be testable at gate time and give deterministic answers.
• If a constraint mask is reused often, **promote it to a subkind**.

**Hand‑off.** Context‑specific views that keep identity intact and make typed guards practical (“use `PaymentAccount@PCI` mask in these steps”).

> *Manager hint.* If the same mask appears in several guards, **promote** it to a subkind. This reduces future bridge and audit effort.

---

#### 7.2.7 Mini end‑to‑end example (manager‑oriented)

> **Scenario.** A risk gate for API requests must be reused by another program across Contexts.

**Lang‑CHR.** Settle on *Request*, *AuthenticatedRequest*, *RiskScore*, *BudgetSlack*; write them in controlled phrases (F3).

**Kind‑CAL.**
• Define `Kind Request` (K2) and a **subkind** `AuthenticatedRequest ⊑ Request`;  publish a **KindBridge** for the PCI taxonomy with **kind‑bridge congruence level 2** (loss note: token class is collapsed).
• Membership `MemberOf(e, AuthenticatedRequest, slice)` is deterministic under API v2.3 and Γ\_time policy.

**Structure‑CAL.**
• `AuthenticatedRequest` is a **record kind** with fields (headers, tokenProof, body); invariants relate tokenProof to headers.

**Compose‑CAL.**
• Policy P says in Plain terms: “for every **AuthenticatedRequest** in the **target context**, deny the call when **riskScore** is at or above the set **risk threshold** and **budgetSlack** is at or below the set **budget limit**.”
• Another service S expects `PCIRequest`. Typed pre‑check: does `AuthenticatedRequest ⊑ PCIRequest`? No.
• Remedy: adapter A proves `AuthenticatedRequest → PCIRequest` in this Context; if reusing across Contexts, publish a **KindBridge** for the PCI taxonomy with **`CL^k=2`** (loss: token class collapsed).

**CT2R‑LOG.**
• State P in a state P in a proof‑checked logic (where appropriate for F7+), so that changes to token rules break proofs. Proofs rely on the **AuthenticatedRequest** definition, not on the consumer’s scope.

**Role‑CAL.**
• Register a **RoleMask** over `PCIRequest` for the consuming team; guards must be able to test the mask’s constraints at gate time.

**Outcome.**
• **Typed guard** approves only when: (i) the type pre‑check passes (same‑Context subkind‑of or a KindBridge with an acceptable congruence level), (ii) **Scope** covers the target context (API v2.3, explicit time selector), and (iii) **R** reflects the **scope‑bridge** and **kind‑bridge** penalties and evidence is fresh.
• No one widened Scope to hide a type mismatch; the adapter + bridge made the semantics explicit and auditable.

---

> **Takeaway.** If you keep these six hand‑offs in view—words → kinds → structure → composition → logic → roles—you get **predictable reviews**, **clean risk accounting**, and **reusable claims** that travel across Contexts without silent meaning drift.

### 7.3 · Compliance & Regulatory Alignment — profile  \[A/I]

Treat regulatory categories as **Kinds**, carry their **intent** in `KindSignature` with declared **F**, move them across Contexts with a **KindBridge** (type‑congruence **`CL^k`** + loss notes), and express applicability as **Claim scope** over `U.ContextSlice` (with explicit **Γ_time**). Any Cross‑context uncertainty is routed to **R** via **Ψ(`CL^k`)** (kind) and **Φ(CL)** (scope); **F** and **G** remain unchanged.

> **Authoritative obligations and guard macros** (C‑REG‑1…8, Guard_RegAdopt / Guard_RegChange / Guard_RegXContextUse) and worked scenarios live in **C.3.A, Annex A (Regulatory adoption profile)**.


### 7.4 · How typed reasoning plugs into **Assurance Lanes (VA/LA/TA) & Evidence design**  \[A/I]

**Intent (manager’s view).** Typed reasoning turns “prove/test/qualify” into a **repeatable plan** by making *what the rule talks about* explicit (named **Kinds**, their **subkinds**, optional **RoleMasks**) and keeping **Scope (G)** over `U.ContextSlice` separate from **membership** inside the slice. Cross‑context uncertainty (Scope Bridge **CL**, KindBridge **`CL^k`**) always routes to **R** as penalties **Φ/Ψ**; it never changes **F** or **G**.

**Evidence matrix (sketch).**

| Row set                       | Column set                                                   | Cell content                                                                                                           |
| ----------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| **Kinds** (subkinds or masks) | **Context slices** (Standard versions, env ranges, `Γ_time`) | **Evidence unit** (proof fragment, test batch, monitoring window), with **Scope** and **MemberOf** predicates attached |

*Tip.* For formal kinds and “up‑to‑iso” kinds (AT K2/K3), expect **more rows** (variants). For instance‑like kinds (AT K0), expect **fewer rows** and **tighter columns** (narrow slices, stricter freshness).

> **Authoritative evidence obligations and guard macros** (planning/attachment, VA/LA/TA duties, anti‑patterns) are in **C.3.A, Annex B**.

### 7.5 · How typed reasoning plugs into **ESG and Method–Work gating**  \[A]

> Intent. Make state changes and work admissions deterministic, auditable, and safe by separating (1) **typed compatibility** (what the statement or capability is about) from (2) **scope coverage** (where it holds or can run). Any Cross‑context uncertainty is routed to **R** (reliability) only—never to **F** (form) or **G** (scope).

---

#### 7.5.1 · Scope & fit

This subsection defines **normative guard obligations** for:

* **ESG** (Episteme State Graph) transitions whose assertions **quantify over kinds**, and
* **Method–Work** admissions where a **capability** expects inputs/outputs of specified kinds.

It reuses:

* **USM** (A.2.6): `U.ClaimScope` (G) and `U.WorkScope` coverage + `Γ_time`,
* **Kind‑CAL core** (C.3.1–C.3.2): `U.Kind`, `MemberOf(e,k,slice)`, `⊑`,
* **KindBridge** (C.3.3) with **`CL^k`** and loss notes,
* **Scope Bridge** (Part B) with **CL** and loss notes,
* **RoleMask** (C.3.4) when local adaptations of a kind are used,
* **Formality F** (C.2.3) when transitions gate on rigor,
* **Assurance R** (C.2.2) for evidence freshness and penalties Φ/Ψ.

**Guard macros.** The **normative guard shapes** for ESG and Method–Work (**Guard_TypedClaim**, **Guard_TypedJoin**, **Guard_MaskedUse**, **Guard_XContext_Typed**) are specified in **Annex C.3.A С**. Use those shapes; the present section is a manager‑level overview only.

#### 7.5.2 · Inputs & roles (at guard time)

* **TargetSlice** — the specific context you are deciding for: Context, versioned Standards, environment parameters, and an explicit **time selector (Γ_time)**.
* **Typed carriers**

  * **ESG:** the **Claim** quantifies over one or more **Kinds** (e.g., “for all vehicles in the target context …”).
  * **Method–Work:** the **Capability** declares expected input/output kinds (and possibly RoleMasks).
* **Thresholds** (context‑local policy):

  * Minimum **F** level for the Claim (if the Context gates on rigor),
  * Minimum **congruence** for **scope bridges**,
  * Minimum **type‑congruence** for **KindBridges**,
  * Evidence **freshness windows** (R‑lane).
* **Evidence bundle** (if the transition implies trust): references, dates, windows.

---
#### 7.5.3 · Manager’s 7‑step checklist (operational)

1. **Name the slice.** Write the full `TargetSlice`/`JobSlice` tuple including **`Γ_time`**.
2. **Check coverage.** Claim/Work scope **covers** the slice (USM).
3. **Check typed definedness.** A deterministic membership check is available in this context for every kind you use (and any masks are registered).
4. **Check typed compatibility.** same Context: `⊑` (or mask constraints met). Cross‑context: **KindBridge** with **`CL^k ≥ c`**.
5. **Bridge scope if needed.** Scope Bridge with **CL ≥ c** for Cross‑context scope.
6. **Apply penalties to R.** Apply the **scope‑bridge penalty** and the **kind‑bridge penalty**; then check evidence **freshness** windows.
7. **(If gated) Check F.** Enforce `Formality ≥ F_k` for the transition.

> **Remember:** **F** and **G** never change because of bridges; only **R** is penalized. AT (K0…K3) is informative and **not** used in guards.

---

#### 7.5.4 · Cross‑references

* **USM / A.2.6:** Scope coverage, `Γ_time`, serial **∩**, **SpanUnion**, Bridge+CL.
* **Kind‑CAL / C.3.1–C.3.4:** `U.Kind`, `⊑`, `MemberOf`, RoleMask, KindBridge + **`CL^k`**.
* **Formality / C.2.3:** `U.Formality` thresholds (when ESG gates on rigor).
* **Assurance / C.2.2:** Freshness windows; **Φ(CL)** and **Ψ(`CL^k`)** penalties to **R** (weakest‑link on paths).

This subsection is **normative** for guards in ESG and Method–Work that **use kinds**.

## 8 · Cross‑context typed reuse & assurance accounting  \[A/I]

### 8.1 · The **two‑bridge rule** (mandatory)  \[A]

When any part of the use crosses Contexts:

1. **Scope Bridge** (USM/Part B) with **CL** → penalty **Φ(CL)** to **R**.
2. **KindBridge** (C.3.3) with **`CL^k`** → penalty **Ψ(`CL^k`)** to **R**.

Both bridges carry **loss notes**; neither changes **F** or **G**. See **C.3.A Guard\_XContext\_Typed**.

---

### 8.2 · Narrowing after mapping (best practice)  \[I]

If a bridge’s loss notes indicate material mismatch (dropped invariants, collapsed subkinds):

* **Narrow the mapped Scope** to areas where those losses are benign.
* **Or** introduce an **adapter** (plus evidence) that restores the needed properties in the target Context.
* Document the decision; the penalties still land in **R**.

---

### 8.3 · Typical Cross‑context patterns (manager’s catalog)  \[I]

* **Name‑level overlap only (low `CL^k`).**
  Expect significant Ψ penalty. Limit quantification, add local checks, or refuse reuse until the kind mapping is improved.

* **Up‑to‑iso mapping (high `CL^k`).**
  Often seen for K3 kinds. Ψ penalty is small; treat as “shape‑preserving” transfer. Still apply the appropriate **Φ(CL)** for Scope.

* **Mask‑to‑subkind evolution.**
  If receivers repeatedly use the same **RoleMask** to make a transfer safe, promote it to an explicit **subkind** and update the bridge to preserve that link.

---

### 8.4 · Decision pattern (fast path)  \[I]

1. **Typed pre‑check:** `k_A ⊑ k_B` (same Context) **or** `KindBridge(k_A → k′_B)` with acceptable **`CL^k`**.
2. **Scope coverage:** `translate(Scope_A)` covers `TargetSlice_B`.
3. **Apply penalties:** **Φ(CL\_scope)** and **Ψ(`CL^k`)** to **R**.
4. **Freshness:** windows/decay for all bound evidence.
5. **Publish:** a short “Bridge and Loss Notes” box; include any **narrowing** or **adapters** used.

---

## 9 · Authoring guidance (engineers‑managers)  \[I]

### 9.1 · When to mint a `U.Kind`  \[I]

Create a Kind when:

* multiple claims refer to the **same “describedEntity”** using unstable labels;
* you need **subkinds** (refinement) or repeated **RoleMasks**;
* different Contexts must **map** this “describedEntity” via bridges;
* you need to **quantify** over a population (and plan variant coverage) instead of over a single exemplar.

Avoid creating a Kind for **one‑off** instance references—prefer a clear **K0** facet or just a literal exemplar in the claim.

---

### 9.2 · Writing a **KindSignature** (and picking **F**)  \[I]

* Start with a concise **intent**: the invariants/constraints that make membership meaningful.
* Aim for **F4** (predicate‑like) if the kind is intended for reuse; rise to **F7+** only where proof‑grade is justified.
* Use **observable** terms (no “latest”); if a Standard matters, **name its version**.
* If defining a Kind reveals systematic **narrowings** in use, introduce explicit **subkinds** (`⊑`) rather than accumulating opaque masks.

> **Example (sketch).**
> `Kind Vehicle` — intent: “has VIN; has brake system; has propulsion {ICE, EV, Hybrid}; …” (F4 predicates).
> Subkind: `PassengerCar ⊑ Vehicle`.
> RoleMask: `Vehicle@ABSRequired` for processes that demand ABS (deterministic constraints; candidates for promotion to subkind if widely reused).

---

### 9.3 · Setting the **AT** facet (K0…K3)  \[I]

Use **AT** to **aim effort**, not to gate:

* **K0**: instance/cohort — focus **R** on the TargetSlice; don’t over‑formalize.
* **K1**: behavioral pattern — clarify Standards; plan ΔF (F3→F4).
* **K2**: formal class — invest in F4–F7; plan **variant coverage** across subkinds in **R**.
* **K3**: up‑to‑iso — expect high‑quality bridges; consider F7–F9 for critical invariants.

Never treat **AT** as “wider/narrower” **G**.

---

### 9.4 · Writing a typed claim (with USM blocks)  \[I]

**Skeleton.**

* **Kinds used:** `Vehicle` (K2), subkinds `PassengerCar`.
* **Claim scope (G):** `surface∈{dry,wet}; speed≤50; rig=v3; Γ_time=rolling 180d`.
* **Statement:** `∀ x ∈ Extension(Vehicle, TargetSlice) …`
* **Guards:** use **C.3.A Guard\_TypedClaim**; if Cross‑context, add **Guard\_XContext\_Typed** (two‑bridge rule).

**Tip.** Keep **Scope**, **MemberOf definedness**, **F thresholds**, and **freshness** as **separate** guard predicates—the auditor should be able to tick each box independently.

---

### 9.5 · Minimal “Kind card” contents (Context catalog)  \[I]

* **Name** and **intent summary** (KindSignature snippet + **F**).
* **`⊑` links** (parents/children).
* **Examples of `MemberOf@slice`** (what membership looks like in practice).
* **Known RoleMasks** (type, constraints, determinism).
* **Known KindBridges** (source/target Contexts, **`CL^k`**, loss notes, definedness).
* *(Optional)* **AT** facet with one‑line rationale.

---

## 10 · Review & integration guidance  \[I]

### 10.1 · Reviewer’s 8‑point checklist

1. **Named describedEntity.** Does the claim state **what** it quantifies over (`U.Kind`)?
2. **Scope explicit.** Is **G** declared (no “domain” placeholders, no implicit “latest”)?
3. **Typed compatibility.** For compositions, do we have `⊑` (same Context) or a **KindBridge**?
4. **RoleMasks.** If used, are they **registered**, **deterministic**, and not masquerading as kinds?
5. **Two‑bridge rule.** For Cross‑context use, do we have **both** Scope Bridge (**CL**) and **KindBridge** (**`CL^k`**)?
6. **Penalties.** Are **Φ(CL)** and **Ψ(`CL^k`)** applied to **R**, not smuggled into F/G?
7. **Freshness.** Are validation/monitoring windows separate from Scope coverage?
8. **Evidence fit.** For class‑level claims, does the test plan cover **subkinds/variants**?

---

### 10.2 · Integrator’s composition playbook (typed first, then scope)

* **Step 1:** Check `k_A ⊑ k_B` (or KindBridge).
* **Step 2:** Compute **Scope\_serial** = `Scope(A) ∩ Scope(B)` (USM).
* **Step 3:** If parallel supports exist, **SpanUnion** them (only where independent).
* **Step 4:** Apply **Φ**/**Ψ** penalties to **R**; enforce freshness.
* **Step 5:** If a **mask** is repeatedly required, consider promoting it to a **subkind**.

---

### 10.3 · Assurance lead: wiring penalties and windows

* Identify channels used: **Scope bridge? KindBridge?**
* Apply **Φ(CL)** and **Ψ(`CL^k`)** to **R** (monotone; higher congruence ⇒ smaller penalty).
* Verify **freshness windows** for all bound evidence (independent of bridges).
* Publish a **one‑box summary**: bridges, levels, loss notes, any narrowing/adapters, net impact on **R**.

---

### 10.4 · Red flags (stop‑the‑line)

* “**We widened G because we reworded the type.**” → **Reject**; redo as subkind/bridge or revise Scope honestly.
* “**Mask equals kind.**” → **Refactor**; register mask properly or promote to subkind.
* “**Cross‑context without KindBridge.**” → **Block**; demand mapping and **`CL^k`**.
* “**No Γ\_time.**” → **Block**; add explicit time policy (point/window/rolling).

---

## 11 · Worked examples (end‑to‑end)  \[I]

+> *Each example shows the typed pre‑check, Scope composition, penalties to **R**, and the managerial decision. Full guard clauses for these scenarios are in **Annex C.3.A**.*

### 11.1 · Cyber‑physical braking policy across labs and plants

**Claim (Lab Context).**
“∀ `x ∈ Vehicle`: brakingDistance(x) ≤ 50 m (dry), ≤ 40 m (wet).”
**Kinds.** `Vehicle` (K2, KindSignature F4); subkind `PassengerCar ⊑ Vehicle`.
**Scope (Lab).** `{surface∈{dry,wet}, speed≤50, rig=v3, Γ_time=rolling 180d}`.

**Reuse at Plant B.**
– **KindBridge:** `Vehicle ↦ TransportUnit` with **`CL^k=2`** (loss: EV subkind collapsed).
– **Scope Bridge:** `Lab → PlantB` with **CL=2** (rig bias ±2 %).
– **Narrowing:** loss notes indicate wet‑surface bias; Plant B **narrows** mapped Scope to temp/adhesion ranges with acceptable bias.

**Decision.**
Typed pre‑check: **OK** via KindBridge. Scope coverage after translate/narrow: **OK**.
Penalties: apply **Φ(2)** and **Ψ(2)** to **R**; freshness windows checked.
**Outcome:** Adopt with reduced **R**; action item: qualify rig v4 to raise CL in the future.

---

### 11.2 · API decision rule with adapter and subkind promotion

**Consumer claim.**
“∀ `x ∈ AuthenticatedRequest`: deny if riskScore(x) ≥ θ ∧ budgetSlack ≤ β.”

**Producer reality.**
Service A emits `Request` (no auth guarantee).
**Option A:** A proves it emits `AuthenticatedRequest` (introduce subkind or strengthen Standard).
**Option B:** Insert **adapter** that filters/annotates `Request → AuthenticatedRequest`.

**Typed check.**
Before: no `Request ⊑ AuthenticatedRequest`. After **Option B**: adapter supplies the guarantee; repeated use leads to promoting **mask** to **subkind**.

**Scope.**
API v2.3; Γ\_time = rolling 30 d.
**R.**
No Cross‑context reuse; no Φ/Ψ. Evidence: adapter correctness on the TargetSlice.

**Outcome.**
Adopt via Option B; open task: generalize producer to subkind and remove adapter later.

---

### 11.3 · Clinical dosage rule across jurisdictions (bridge + mask)

**Claim (Hospital X).**
“∀ `x ∈ AdultPatient`: dosage ≤ D per kg for drug M.”
**Kind.** `AdultPatient` (K2, F4).
**Mask.** `AdultPatient@ClinicMask` narrows to the clinic’s cohort (deterministic DOB policy).

**Reuse in Jurisdiction Y.**
– **KindBridge:** `AdultPatient ↦ AdultPerson_Y`, **`CL^k=1`** (18 vs 21 years boundary).
– **Scope Bridge:** coding systems differ (CL depends on mapping quality).
– **Narrowing:** restrict Scope to datasets where DOB granularity supports boundary reconciliation.

**Decision.**
Typed pre‑check via KindBridge: **OK**. Scope coverage after translate/narrow: **OK**.
Penalties: **Φ(CL\_scope)** and **Ψ(1)** applied to **R**.
**Outcome:** Adopt with strong **R** penalty; plan: negotiate a harmonized boundary to raise `CL^k`.

---

### 11.4 · ML fairness constraint with typed quantification

**Claim (Product Context).**
“∀ `x ∈ EligiblePerson`: TPR difference ≤ δ across groups `G`.”

**Kind.** `EligiblePerson` transitions from **K1→K2** as attributes and cohorts are formalized (KindSignature F4).
**Scope.** `{pipeline=P, features=F, Γ_time=rolling 180 d}`.

**Cross‑context use.**
Model team Context has `Resident` with different feature basis.
– **KindBridge:** `EligiblePerson ↦ Resident` with **`CL^k=1`** (feature loss).
– **Scope Bridge:** `pipeline P → P′`, **CL=2**.

**Decision.**
Typed pre‑check **OK** via bridges; mapped Scope **covers** the subset where features align.
Apply **Φ(2)** and **Ψ(1)** to **R**; restrict groups to mapped subset; require monitoring freshness.
**Outcome:** Adopt with reduced **R** and a mitigation note; action items: improve feature mapping and raise KindSignature F.

## 12 · Anti‑patterns & how to fix them  \[I/A]

> *Use this section as a “red flags” sheet in reviews. Each item links to a concrete remedy that preserves F–G–R & USM discipline (F/G/R separation, USM algebra, typed pre‑checks).*

| Anti‑pattern (what goes wrong)                                   | Why it’s wrong (conceptual fault)                                                               | The fix (normative/informative pointers)                                                                                                              |
| ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **“We widened G because we reworded the type.”**                 | Confuses **describedEntity** (kind) with **applicability** (scope). Abstract wording ≠ broader scope. | Keep typed pre‑check separate (C.3.1 `⊑` or C.3.3 KindBridge). Widen **G** only via **ΔG+** with support (USM A.2.6).                                 |
| **“Kind scope” block attached to a Kind.**                       | Kinds don’t carry Scope; they carry **intent/extent**.                                          | Remove the block. Scope stays on claims/capabilities (USM). If you meant classifier definedness, state it via **K‑07** (C.3.2).                       |
| **Inferring scope from extension size.**                         | **Scope ≠ Extension**; extension is “which instances in a slice,” not “where the claim holds.”  | Keep **G** set‑valued over `U.ContextSlice` (USM). Use `MemberOf` only inside the typed quantifier.                                                   |
| **Mask used as a hidden kind (“just call it the masked kind”).** | Opaque drift; reviewers can’t see constraints.                                                  | Register a **RoleMask** (C.3.4). If reused across guards, **promote to subkind** with `⊑`.                                                            |
| **Cross‑context reuse with only one bridge.**                       | Contexts differ on two characteristics: Scope **and** Kind.                                                   | Apply the **two‑bridge rule**: Scope Bridge (**CL** → Φ) **and** KindBridge (**`CL^k`** → Ψ). Both penalties land in **R**.                           |
| **Using AT (K0…K3) as a gate/threshold.**                        | AT is an **informative facet**, not a Characteristic; gating on AT recreates a G‑ladder.        | Remove AT from guards. Use it only to **aim ΔF/ΔR** and to set **bridge expectations** (C.3.5).                                                       |
| **“Automated execution success proves the type claim.”**                            | Execution success (F5/6) is not proof (F7+); also confuses **R** with **F**.                    | If you need proof‑grade properties, raise **F** for the claim/KindSignature (C.2.3) or restrict the claim. Keep **R** as evidence freshness/coverage. |
| **Hidden “latest” in membership or scope checks.**               | Non‑deterministic evaluation; unverifiable audit trail.                                         | Declare **Γ\_time** explicitly in Scope (USM). Membership must be **deterministic** (C.3.2 K‑05/K‑07).                                                |
| **Fixing type mismatch by “unioning scopes.”**                   | G‑union cannot repair **describedEntity** mismatches.                                                 | Introduce a **subkind**, add an **adapter** (+evidence), or define a **KindBridge**.                                                                  |
| **Collapsing subkinds silently in a bridge.**                    | Reviewers don’t see lost distinctions → false confidence.                                       | Record **loss notes** on the KindBridge (C.3.3 KB‑11); consider **narrowing** mapped Scope or adding an adapter.                                      |

---

## 13 · Governance & conformance pull‑ups  \[A]

> *Contexts adopt Kind‑CAL by meeting the **Context‑level** obligations below. They summarize, not duplicate, the formal requirements in **C.3.1–C.3.5** and **C.3.A**. Use this as an adoption checklist.*

### 13.1 · Context‑level obligations (must‑haves)

1. **Kinds & order.** Maintain a Context catalog of `U.Kind` with an explicit **partial order** `⊑`.
   – Conformance: **C.3.1** (K‑01/K‑02).

2. **Kind signatures (intent).** For each Kind, publish a **KindSignature** with declared **F** (C.2.3).
   – Conformance: **C.3.2** (K‑03/K‑04).

3. **Deterministic membership.** Ensure `MemberOf(e,k,slice)` is **deterministic**; declare any definedness domain.
   – Conformance: **C.3.2** (K‑05/K‑07).

4. **Typed guards.** When a claim quantifies over kinds, guards SHALL use the **typed guard macros** (or equivalents) from **C.3.A**; **Scope coverage** and **typed checks** are separate predicates.

5. **Role masks.** If a local projection is needed, register a **RoleMask** (type: constraint/vocabulary/composite); avoid cloning kinds.
   – Conformance: **C.3.4** (RM‑01…RM‑06).

6. **Two‑bridge rule for Cross‑context use.**
   – **Scope Bridge** (Part B) with **CL** → Φ(CL) to **R**.
   – **KindBridge** (C.3.3) with **`CL^k`** → Ψ(`CL^k`) to **R**.
   – Conformance: **C.3.3** (KB‑01…KB‑10).

7. **Decision records.** For each typed state change, record: **TargetSlice tuple**, typed compatibility outcome (`⊑` or KindBridge), **Scope coverage**, applied **Φ/Ψ** penalties to **R**, and **freshness** checks.

### 13.2 · ESG / Method‑Work template inserts (normative snippets)

* **Kinds used:** list `U.Kind` and any expected **subkinds** or **RoleMasks**.
* **Claim scope (G):** explicit predicates over `U.ContextSlice` inc. **Γ\_time**.
* **Typed guard lines:**
  – same Context: `k_A ⊑ k_B` *checked*.
  – Cross Context: `KindBridge(k_A → k′_B)`, `CL^k ≥ c_k` *checked*.
* **Scope bridge lines:** `Bridge(Context_A → Context_B)`, `CL ≥ c_s` *checked*.
* **Assurance lines:** `Φ(CL)`, `Ψ(CL^k)` applied to **R**; **freshness windows** hold.

### 13.3 · Audits & levels of adoption (informative)

* **USM‑Typed‑Ready.** Catalog exists; `⊑` declared; guard macros installed.
* **USM‑Typed‑Guarded.** All typed claims use **C.3.A** guard shapes; **Γ\_time** explicit; two‑bridge rule enforced.
* **USM‑Typed‑Auditable.** Decision records capture **TargetSlice**, typed checks, bridges, penalties, freshness.
* **USM‑Typed‑Composed.** Compositions use typed pre‑check before Scope algebra; independence justified for **SpanUnion**.

---

## 14 · Migration & editorial impact  \[A]

> *Apply these edits incrementally; you do not need to stop other work. The aim is to eliminate synonym drift, restore F/G/R separation, and make typed reasoning routine.*

### 14.1 · Inventory & refactor (steps)

1. **Inventory** claims that implicitly talk about “things” (vehicles, requests, accounts, cohorts…).
2. **Name kinds** for recurring “describedEntity”; start at **K1**; promote to **K2** as invariants stabilize.
3. **Extract KindSignature** (aim **F4**); declare **F**.
4. **Refactor claims** to typed quantification: `∀ x ∈ Extension(k, slice) …` plus **Scope (G)** predicates.
5. **Publish bridges** where reuse is Cross‑context: Scope Bridge (**CL**) and KindBridge (**`CL^k`**) with loss notes; wire penalties **Φ/Ψ** to **R**.
6. **Normalize masks**: register RoleMasks; if reused, promote to subkinds (`⊑`).

### 14.2 · Edits to other parts (normative redirects, no new math)

* **A.2.6 (USM).**
  – Add “no Scope on kinds” note.
  – In typed examples, show `MemberOf` definedness + Scope coverage.
  – Two‑bridge rule for Cross‑context typed reuse.

* **C.2.2 (F–G–R).**
  – Replace any “generality/abstraction” wording with **Claim scope (G)**.
  – Before scope composition, require typed pre‑check (`⊑` or KindBridge).
  – Distinguish penalties: **Φ(CL)** vs **Ψ(`CL^k`)** → both to **R**.

* **C.2.3 (F).**
  – Add note: **KindSignature** has its own **F**; claim‑level F remains by weakest‑link.

* **Part B (Bridges).**
 – Introduce **KindBridge** with **`CL^k`**, monotone order preservation, loss notes; determinism.
 – Chaining uses **min** of levels (weakest‑link) **for both** **CL** (Scope bridges) **and** **`CL^k`** (KindBridges).


* **Role‑CAL.**
  – Add **RoleMask** for kinds; determinism; promotion rule to subkind when reused.

* **Compose‑CAL.**
  – Add typed pre‑check before Scope algebra; forbid “type‑by‑scope”.

* **Part E (Lexicon).**
  – Add: `U.Kind`, `U.SubkindOf (⊑)`, `KindSignature`(+F), `Extension`, `MemberOf`, `U.RoleMask`, **KindBridge**, `CL^k`, **AT (kinds, facet)**.
  – Mark as **legacy aliases** (not characteristic names): *generality (as ladder), kind scope, validity (as characteristic), capability envelope*; redirect to **Claim/Work scope** or **Kind** entries.

### 14.3 · Backwards compatibility

* Historical prose may keep legacy words. **Guards, conformance text, and state assertions** MUST use the Kind‑CAL/USM vocabulary and guard shapes.
* When annotating older records, add a small “typed note” box: **Kinds**, **Scope**, **Bridges (CL/`CL^k`)**, **loss notes**, **penalties to R**.

---

## 15 · Extended rationale & design notes  \[I]

> *This section explains the design choices that keep Kind‑CAL compact and interoperable with F–G–R & USM without drifting into tooling or technology stacks.*

### 15.1 · Why **no Scope on kinds**

Scope answers **“where the claim holds”** (set of Context slices, USM); kinds answer **“what the claim is about”**. Putting Scope on kinds would either (a) duplicate claim Scope, or (b) smuggle applicability into a classifier. We prevent both by: **intent/extent on kinds** (C.3.2), **Scope on claims/capabilities** (USM).

### 15.2 · Why **two bridges** (Scope vs Kind)

Contexts diverge along **context** (Standards, parameters, time) and **classification** (what counts as a member). A single bridge hides which characteristic is mismatched. Two explicit bridges keep fixes targeted: **ΔG / narrowing** for context misfit; **subkind/adapter** for classification misfit. Both risks land in **R** as separate penalties (**Φ/Ψ**).

### 15.3 · Why **AT is a facet**

AT (K0…K3) improves **planning** (ΔF/ΔR, bridge style) and **navigation** without introducing new algebra. Making AT a Characteristic would recreate a “G‑ladder,” blur applicability with abstraction, and invite gating on AT. As a facet, AT remains helpful but **toothless in math**, which is precisely what we want.

### 15.4 · Why **RoleMask** and not “clone a kind”

Operational tweaks (extra constraints, local aliases) are real but temporary. Cloning kinds creates drift and duplicate bridges. **RoleMask** documents the tweak **without breaking identity**; promotion to subkind occurs when practice stabilizes. This keeps catalogs small and bridges honest.

### 15.5 · Fit with **Compose‑CAL** and **LOG‑CAL**

Typed pre‑checks (same‑Context `⊑` or KindBridge) act like **port compatibility** before any Scope arithmetic. LOG‑CAL benefits from explicit quantification `∀ x : Kind` with substitution rules aligned to `⊑`. Neither alters F/G/R algebra; they prevent category mistakes before we do trust math.

### 15.6 · CT2R lens (intuition)

A **KindBridge** behaves like a **functor** that (approximately) preserves structure between Contexts; **`CL^k`** is a practical knob for “how functorial” it is. At **K3** (up‑to‑iso), this is literal: we expect bridges to preserve equivalences, hence higher `CL^k` and smaller Ψ penalties.

## 15bis · Rationale (Part E form)  \[I]

**Problem.** (recap)
— Authors conflate *describedEntity* with *applicability*, widening G by abstract wording.
— Cross‑context reuse drifts semantically without declared mappings or risk accounting.
— Planning misfires: over‑formalization for instance claims; under‑testing for class claims.
— Unsafe compositions when describedEntity is implicit.

**Forces.** (recap)
— Local freedom vs global sense; minimality vs utility; intent vs extent; typed discipline vs F–G–R; abstraction vs applicability.

**Decision (C.3‑D1…D7).**
— D1: `U.Kind` is intensional and context‑local (`⊑` partial order).
— D2: Separate intent (KindSignature + F) and extent (Extension/MemberOf@slice).
— D3: No Scope on kinds (Scope lives with claims/capabilities via USM).
— D4: Typed reuse is explicit: KindBridge + `CL^k`, penalties route to **R** only.
— D5: Local adaptation via RoleMask; promote stable masks to subkinds.
— D6: AT (K0…K3) as **facet**, not a Characteristic; never used in guards.
— D7: Guard shapes: typed pre‑check → scope coverage → penalties/freshness.

**Consequences.**
(+) Predictable Cross‑context reuse: two‑bridge rule, separate penalties (Φ/Ψ) to **R**.  
(+) Manager‑friendly planning: AT guides ΔF/ΔR; typed pre‑check blocks category mistakes.  
(+) Clean F–G–R discipline: no “G‑ladder,” no hidden scope inside classifiers.  
(−) Editorial discipline required: no “Kind scope”; masks must be cataloged; promote when stable.  
(−) Initial bridge authoring cost; mitigated by loss‑notes and reuse.

**Alternatives considered.**
— *Global U.Type*: rejected as either too thin or too prescriptive across Contexts.  
— *“Kind scope” in USM*: rejected; duplicates/obscures Scope vs Extension split.

**Known uses.**
— §11.1 (cyber‑physical braking); §11.2 (API with adapter); §11.3 (clinical dosage); §11.4 (ML fairness).  
— ESG guard shapes in **C.3.A**; typed pre‑check in Compose‑CAL (§7.2.4).

**Related patterns.**
A.2.6 (USM), C.2.2 (F–G–R), C.2.3 (F), Part B (Bridges), Role‑CAL, Compose‑CAL, C.3.1–C.3.5, C.3.A.

## 16 · Quick reference for managers  \[I]

### 16.1 · 10‑minute start

1. Name the **Kind** your claim talks about.
2. Write **Scope (G)** as slice predicates (with **Γ\_time**).
3. If composing, check **`⊑`** or **KindBridge** first.
4. Use the **typed guard macro** (C.3.A).
5. Route bridge levels to **R** (Φ/Ψ); check freshness.

### 16.2 · 30‑day rollout plan

Week 1: Inventory & name Kinds (K1); adopt guard macros.
Week 2: Draft **KindSignature** for the top 5 Kinds (aim **F4**); register masks.
Week 3: Wire **two‑bridge rule** into ESG; add CL/`CL^k` lines to decision templates.
Week 4: Promote repeated masks to subkinds; publish first **KindBridge** records with loss notes.

---

## 17 · Local glossary (reading aid)  \[I]

> *Canonical definitions live in sub‑patterns; this list is for quick recall while reading C.3.*

* **`U.Kind`** — Minimal intensional “type/kind” object; carries **KindSignature** and **`⊑`** (C.3.1/C.3.2).
* **`U.SubkindOf (⊑)`** — Partial order on kinds (C.3.1).
* **KindSignature(k)** — Predicate‑like intent that defines the kind; has its own **F** (C.3.2).
* **Extension(k, slice)** — Set of instances of `k` **inside** a `U.ContextSlice` (C.3.2).
* **MemberOf(e, k, slice)** — Boolean membership predicate (C.3.2).
* **RoleMask(k, Context)** — Registered adaptation (constraints/aliases; optional narrowing), no new kind (C.3.4).
* **KindBridge** — Cross‑context mapping for kinds (intent/order) with **`CL^k`** and loss notes (C.3.3).
* **`CL^k`** — Kind‑congruence level; penalty **Ψ(`CL^k`)** goes to **R** (C.3.3).
* **AT (K0…K3)** — Informative facet of a Kind; aids planning/navigation; never used in guards (C.3.5).
* **Guard macros** — Typed guard shapes for ESG/composition (C.3.A).

> *End of C.3. See **C.3.1–C.3.5** and **C.3.A** for the referenced mechanics and guard macros.*

# C.3.1 · **U.Kind & SubkindOf (Core)**  \[A]

> **One‑line summary.** Defines **`U.Kind`** as a **minimal, context‑local intensional carrier** for “what a claim is about,” and **`U.SubkindOf (⊑)`** as a **partial order** over kinds. **Kinds do not carry Scope.** Scope remains on **claims/capabilities** (USM). This core pattern supplies only identity, locality, and ordering; **intent & membership** (`KindSignature`, `Extension/MemberOf`) are specified in **C.3.2**, bridges & congruence in **C.3.3**, masks in **C.3.4**, and the AT facet in **C.3.5**.

---

## ## 0 · Status, Placement & Dependencies

**Status.** Normative architheory in **Part C**. Identifier **C.3.1**.
**Audience.** Engineering managers, architects, assurance leads.

**Dependencies.**

* **A.2.6 USM (Unified Scope Mechanism).** *Scope* is a set‑valued **USM property** over `U.ContextSlice` on **claims/capabilities**; algebra: `∈` (membership), `∩` (intersection), `SpanUnion` (union across independent lines), `translate` (scope mapping).
* **C.2.2 F–G–R.** F = formality of expression; **G = Claim scope**; R = assurance/evidence; weakest‑link for F/R; CL penalties feed **R**, not **F/G**.
* **C.2.3 U.Formality (F).** Ordinal F0…F9; no arithmetic; applies to all content, including Kind signatures (defined in **C.3.2**).
* **Part B Bridges & CL.** Generic (scope) bridges and CL; **Kind bridges** are specialized in **C.3.3**.

**Non‑goals.**

* No data governance or repository/notation mandates.
* No membership or signature semantics here (defined in **C.3.2**).
* No Cross‑context mapping/congruence here (defined in **C.3.3**).
* No role/mask mechanics here (defined in **C.3.4**).
* No AT facet mechanics here (defined in **C.3.5**).

## 1 · Purpose & Audience

This pattern gives **one small, stable vocabulary** to say *what* a claim ranges over (its **describedEntity**) without entangling that with *where it applies* (Scope) or *how well it is supported* (R). For managers:

* It prevents the costly mistake “more abstract wording ⇒ wider scope.”
* It enables **typed composition** (you cannot combine claims about incompatible “things”).
* It keeps **Scope** and **Assurance** math unchanged and predictable.

---

## 2 · Context

across Contexts, “type” means OWL class, SHACL shape, code type, BORO category, etc. A **neutral, minimal** object is needed to name *the kind of entities* a claim quantifies over **without** importing a full type system or altering USM. **`U.Kind`** fills that role; **ordering** between kinds captures “is‑a/refines” relationships a Context relies on.

---

## 3 · Problem

1. **Scope–Type conflation.** Teams broaden G by “abstracting” prose, not by adding supported slices.
2. **Unsafe composition.** Claims are joined though they talk about different “things.”
3. **Cross‑context drift.** Without an explicit core notion of kind, bridges blur describedEntity vs applicability.

---

## 4 · Forces

| Force                          | Tension to resolve                                                        |
| ------------------------------ | ------------------------------------------------------------------------- |
| **Minimality vs utility**      | Keep the core tiny yet sufficient for composition and governance.         |
| **Locality vs reuse**          | Kinds are context‑local, but projects reuse claims across Contexts via bridges. |
| **describedEntity vs applicability** | Ordering should not leak into Scope; kinds must not carry G.              |
| **Neutrality vs specificity**  | Avoid committing to any particular type/ontology stack or notation.       |

---

## 5 · Solution — Core Objects (overview)

* **`U.Kind`** — a **context‑local intensional** object naming a “kind of thing” claims may quantify over.
* **`U.SubkindOf (⊑)`** — a **partial order** on kinds (reflexive, transitive, antisymmetric). `k₁ ⊑ k₂` reads “`k₁` refines `k₂`.”

> **No Scope on kinds.** Scope is for **claims/capabilities** (USM). Kinds supply **describedEntity only**; **membership** and **signature** live in **C.3.2**.

---

## 6 · Norms & Invariants (normative)

**C3.1‑K‑01 (Partial order).** `U.SubkindOf (⊑)` **SHALL** be a **partial order** on `U.Kind`: reflexive, transitive, antisymmetric. Editors **SHALL** document any Context‑specific meets/joins if they supply them (optional).

**C3.1‑K‑02 (No Scope on kinds).** A `U.Kind` **MUST NOT** carry a Scope value. Scope lives with **claims** (`U.ClaimScope` = **G**) and **capabilities** (`U.WorkScope`) per **A.2.6**.
*Rationale pointer:* see **C.3.2** for the **intent/extent vs Scope** split.

**C3.1‑K‑03 (Identity & locality).** A `U.Kind` is **context‑local**. Cross‑context mapping of kinds is handled by **KindBridge** (see **C.3.3**); such mapping **MUST NOT** be conflated with Scope bridging.

**C3.1‑K‑04 (Naming).** A Context **SHALL** assign stable identifiers to kinds and **SHOULD** catalog parent/child `⊑` links. Synonyms/aliases **SHALL** point to the canonical kind id.

**C3.1‑K‑05 (Separation of concerns).** This core **does not** define kind intent or membership; those are specified in **C.3.2** (`KindSignature` with its own F; `Extension/MemberOf` and determinism).

---

## 7 · Interactions (informative)

* **With USM (A.2.6).** Guards that quantify over a kind use **two** predicates: “Scope covers TargetSlice” (USM) **and** whatever **membership** predicate is defined for the kind (see **C.3.2**). Kinds themselves carry **no Scope**.
* **With F–G–R (C.2.2).** This pattern does not alter the triple; typed checks happen **before** scope algebra, preventing invalid compositions.
* **Order of checks reference.** See **Annex C.3.A §5 (E‑01)** for the normative evaluation order: typed compatibility first, then Scope coverage, then penalties to **R** and freshness.
* **With Formality (C.2.3).** A **KindSignature** (C.3.2) declares its **F**; claims retain their own F via weakest‑link.
* **With Bridges (Part B).** Use **KindBridge** (C.3.3) for describedEntity; use **Scope Bridge** (Part B) for applicability. Penalties land in **R** via different channels.

---

## 8 · Authoring & Review (informative)

**When to mint a kind.**
Mint a `U.Kind` when claims repeatedly quantify over “the same sort of thing” and you need: (i) safe composition, (ii) clear Cross‑context mapping, (iii) a place to collect invariants (in **C.3.2**).

**Don’t over‑mint.**
If a local constraint is temporary or purely procedural, prefer a **RoleMask** (C.3.4) over a new subkind.

**Review prompts.**

1. Does the draft introduce a new *describedEntity* concept? → consider a kind.
2. Does prose hint at “is‑a” relationships? → capture as `⊑`, not as scope widening.
3. Are authors trying to widen scope by abstracting wording? → stop; widen **G** only via **ΔG** (USM) with support.

---

## 9 · Examples (informative, technology‑neutral)

1. **Vehicle/PassengerCar.**
   Mint `Kind Vehicle`. Later add `PassengerCar ⊑ Vehicle`. Claims about **Vehicle** may be reused by narrowing to **PassengerCar** without touching **G**. Scope remains an independent predicate over `U.ContextSlice`.

2. **Request/AuthenticatedRequest.**
   If multiple policies speak about “authenticated requests,” declare `AuthenticatedRequest ⊑ Request`. Do **not** widen G to compensate for missing authentication; either change the producer’s kind or insert an adapter (C.3.2/C.3.4) while keeping G honest.

---

## 10 · Conformance checklist (normative)

| ID            | Requirement                                                                                             |
| ------------- | ------------------------------------------------------------------------------------------------------- |
| **C3.1‑K‑01** | `U.SubkindOf (⊑)` is a **partial order** (reflexive, transitive, antisymmetric).                        |
| **C3.1‑K‑02** | `U.Kind` **does not carry Scope**. Scope remains on claims/capabilities per **A.2.6**.                  |
| **C3.1‑K‑03** | Kinds are **context‑local**; Cross‑context mapping uses **KindBridge** (C.3.3), not Scope bridges.            |
| **C3.1‑K‑04** | Kinds have **stable ids**; synonyms redirect; Contexts catalog `⊑` links.                                  |
| **C3.1‑K‑05** | **No intent/membership** in this core; refer to **C.3.2** for `KindSignature` and `Extension/MemberOf`. |

---

## 11 · Rationale (informative)

**Why a tiny core?**
Contexts differ wildly in “type” practice. A large, prescriptive core would either (a) force one Tradition’s semantics on all, or (b) become an empty label. The **smallest powerful** core—identity + ordering—gives managers and integrators what they need (safe composition, predictable edits) and leaves intent/membership/bridges/masks to focused sub‑patterns.

**Why “no Scope on kinds”?**
**Scope** (USM) answers “**where** a claim/capability holds” over `U.ContextSlice`. Kinds answer “**what** the claim ranges over.” Blending them recreates the failure mode we are removing (“higher abstraction ⇒ wider scope”). The right split is:

* **Kind**: intensional name + order (`⊑`) *(this pattern)*; intent & membership *(C.3.2)*.
* **Scope**: set of context slices *(A.2.6)*.
* **Assurance**: evidence & penalties *(C.2.2 / Part B)*.

# C.3.2 · **KindSignature (+F) & Extension/MemberOf**  \[A]

> **One‑line summary.** Specifies the **intent and extent** of kinds: (**i**) a **`KindSignature(k)`** (the intensional definition of kind `k`) that **declares its own Formality F**; (**ii**) an **`Extension(k, slice) ⊆ U.EntitySet(slice)`** and the **membership predicate** `MemberOf(e, k, slice)` that are **deterministic per `U.ContextSlice`**; (**iii**) **monotonicity** of extension under `SubkindOf`; (**iv**) a **definedness policy** that fails **closed** outside its domain. **Kinds still carry no Scope** (that rule lives in C.3.1); Scope stays on **claims/capabilities** (USM). This pattern gives managers and reviewers the **observable basis** to check “what counts as a member here and now” without entangling applicability (G) or assurance (R).

---

## 0 · Status, Placement & Dependencies

**Status.** Normative architheory in **Part C**. Identifier **C.3.2**.
**Audience.** Engineering managers, architects, assurance leads, editors.

**Depends on.**

* **C.3.1** (*U.Kind & SubkindOf Core*): kinds are context‑local; `⊑` is a partial order; kinds carry **no Scope**.
* **A.2.6 USM** (*Context slices & Scopes*): Claim scope (G) and Work scope live on claims/capabilities; algebra `∈` (membership), `∩` (intersection), `SpanUnion` (union across independent lines), `translate` (scope mapping).
* **C.2.3 U.Formality (F)**: ordinal F0…F9; no arithmetic; weakest‑link composition applies to content that depends on the signature.
* **C.2.2 F–G–R**: assurance calculus; CL penalties feed **R**, not **F/G**.
* **Part B (Scope Bridges & CL).** CL (scope congruence) and scope translation live in Part B/USM; **kind‑congruence `CL^k`** and kind mapping live in **C.3.3** (KindBridge).

**Non‑goals.**

* No Scope semantics here (USM); no bridge semantics here (C.3.3).
* No repository/notation mandates; this is concept‑level, not tooling.

## 1 · Purpose & Audience

This pattern makes **describedEntity testable** in a Context:

* Authors get a place to write **what defines a kind** (`KindSignature`) and at **what rigor (F)**.
* Reviewers can ask **deterministic** questions: *“Given this `TargetSlice`, which entities are in `k`?”*
* Managers can plan **ΔF** (raise signature rigor) and **ΔR** (evidence over members) **without** changing **G** (applicability).

**No tooling assumption.** The pattern is **conceptual** and notation‑neutral (no OWL/SHACL/type‑system requirement); it specifies reviewer‑checkable obligations that managers can read in plain language.

## 2 · Context

Different Contexts encode “type” intent differently (predicates, schemas, ontologies, Standards). Regardless of notation, a team must be able to answer, reproducibly: **who belongs to the kind at this slice?** If this is not stable, claims quantified over the kind are unverifiable, bridges are opaque, and composition becomes unsafe.

---

## 3 · Problem

1. **Ambiguous membership.** Membership depends on tacit “latest” states or unwritten defaults.
2. **Signature opacity.** A kind’s definition is scattered; no single place to declare rigor (**F**) or assumptions.
3. **Order violations.** Subkind hierarchies do not guarantee subset behavior in practice.
4. **Scope leakage.** Teams smuggle applicability (G) into kind definitions, recreating G‑ladders by another name.

---

## 4 · Forces

| Force                              | Tension to resolve                                                                                   |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **Local freedom vs comparability** | Contexts need their own notations, but membership must be checkable in a common style.                  |
| **Expressivity vs determinism**    | Rich intent is welcome, but membership must be deterministic given `slice`.                          |
| **Intent vs applicability**        | Define “what counts” (intent/extent) without encoding “where valid” (G).                             |
| **Rigor vs cost**                  | Raising signature F has cost; the framework must support low‑F drafts and high‑F safety cores alike. |

---

## 5 · Solution — Objects & Standards (overview)

* **`KindSignature(k)`** — the **intensional** definition of kind `k` in the Context; it **declares `U.Formality`** per C.2.3.
* **`U.EntitySet(slice)`** — the set (or well‑defined universe) of **entities addressable in a given `U.ContextSlice`**.
* **`Extension(k, slice) ⊆ U.EntitySet(slice)`** — **which entities** belong to `k` **at** `slice`.
* **`MemberOf(e, k, slice)`** — membership predicate: `e ∈ Extension(k, slice)`.

**Design split.**

* **Intent** lives in **`KindSignature`** (with F).
* **Extent** is **computed per `slice`** via `MemberOf`.
* **Applicability** (where a **claim** holds) remains a **Scope** on the claim (USM) and **MUST NOT** be encoded into `KindSignature`.

---

## 6 · Norms & Invariants (normative)

> IDs **C3.2‑K‑03…K‑08** correspond to the rules announced in C.3; additional local rules use **C3.2‑S‑\***.

### 6.1 · Signature & Formality

**C3.2‑K‑03 (Signature F).** Every `KindSignature(k)` **SHALL declare `U.Formality`** per C.2.3 (F0…F9).
— *Note:* Raising signature F **does not** automatically raise claim‑level F; claims follow weakest‑link along their **own** support paths.

**C3.2‑K‑04 (Signature change = content change).** Any change to `KindSignature(k)` that **alters membership** (i.e., would change `Extension(k, slice)` for some `slice`) **SHALL** be recorded as a **content change** (Contexts may version kinds).

### 6.2 · Extension & Membership

**C3.2‑K‑05 (Deterministic membership).** For fixed `(k, slice)`, `MemberOf(e, k, slice)` **MUST** be deterministically evaluable **from observable content in `slice`**.
— Implication: **“latest” is forbidden**; `Γ_time` must be explicit on `slice` (A.2.6).
— If a classifier makes external assumptions, they **MUST** be named in `KindSignature`.

**C3.2‑K‑06 (Monotone in `⊑`).** If `k₁ ⊑ k₂`, then for **every** `slice`:
`Extension(k₁, slice) ⊆ Extension(k₂, slice)`.

**C3.2‑K‑07 (Definedness & fail‑closed).** Each Context **MAY** restrict the **domain of definedness** for `MemberOf(–, k, –)` (e.g., only when a Standard or dataset is present at a given version). Outside that domain, `MemberOf` **MUST** be treated as **not defined** for guard purposes, and guards **MUST fail closed** (deny). Implementations MAY internally return `False`, but there **MUST** be no path where undefined membership yields implicit success.

**C3.2‑K‑08 (Separation from G).** Guards **SHALL** keep **Scope coverage** (USM) and **membership** **as separate predicates**:
“`U.ClaimScope(Claim) covers TargetSlice` **AND** `MemberOf(?, k, TargetSlice)` is defined/used”.

### 6.3 · Entity set & time

**C3.2‑S‑01 (`U.EntitySet`).** A Context **SHALL** document what counts as `U.EntitySet(slice)` (e.g., “rows in dataset D at version v,” “live objects in service S at build b,” “ontology individuals at vocabulary v”). This documentation **MUST** be stable and addressable via the `slice` tuple.
**C3.2‑S‑02 (Time).** `slice` **SHALL** specify **`Γ_time`** (point/window/policy). Membership **MUST NOT** rely on implicit recency. 

`U.EntitySet(slice)` **MUST NOT** expand implicitly via external defaults or time; its extent is fixed by the `slice` tuple (see **C3.2‑S‑02**).

## 7 · Interactions & Placement (informative)

* **With C.3.1.** Kinds carry identity and `⊑`; **no Scope** on kinds. This pattern adds the **intent/extent** layer under those constraints.
* **With A.2.6 (USM).** A typed claim’s guard normally evaluates, in the order specified by **Annex C.3.A §5 (E‑01)**: (1) typed compatibility, (2) **Scope coverage** at `TargetSlice`, (3) **`MemberOf(?, k, TargetSlice)`** definedness and any instantiation, followed by penalties to **R** and freshness checks. Use **Guard_TypedClaim** / **Guard_TypedJoin** rather than ad‑hoc shapes.
* **With C.2.3 (F).** Signature F influences claims **only if** the claim **depends on** the signature content; weakest‑link min applies along the claim’s support path.
* **With C.3.3 (KindBridge).** When `MemberOf` is computed via a **kind mapping across Contexts**, kind‑congruence `CL^k` contributes a **monotone penalty to **R** only (Ψ(`CL^k`)); **F/G MUST NOT** be adjusted. 
* **With Role‑CAL (C.3.4).** A **RoleMask** may **narrow** membership (context‑local adaptation). Frequent masks that encode stable narrowing **SHOULD** be promoted to subkinds (`⊑`).

---

## 8 · Authoring & Review Guidance (informative)

### 8.1 · Authoring `KindSignature`

* **Be explicit and observable.** Prefer predicate‑like clauses over prose (“has VIN format …”; “axles ≥ 2”).
* **Bind to versions.** Name Standards/schemas by version; avoid “current.”
* **Declare F honestly.** F3 for controlled narrative is fine in early phases; aim F4+ for durable kinds; consider F7+ for safety‑critical cores.
* **Name assumptions.** If membership requires external conditions (e.g., calibrated rig), put them in the signature.

### 8.2 · Authoring membership

* **Define `U.EntitySet(slice)`.** Write it down once per Context, make it addressable via the `slice` tuple, and reuse.
* **Determinism first.** No hidden IO, no implicit time; membership must be recomputable from the slice.
* **Document definedness.** If `MemberOf` is undefined without a Standard, say so; guards will fail closed.
* **Respect `⊑`.** If you declare `k₁ ⊑ k₂`, verify subset behavior (C3.2‑K‑06).

### 8.3 · Review checklist (10 minutes)

1. Is **signature F** declared? Is the signature sufficient to evaluate membership?
2. Is **`U.EntitySet(slice)`** documented and addressable?
3. Is **membership deterministic** with explicit `Γ_time` (no “latest”)?
4. If `⊑` links exist, does **subset behavior** hold at sample slices?
5. Are **Scope** and **membership** kept **separate** in guards?
6. Any **Cross‑context** classification? If yes, is **KindBridge** referenced (C.3.3)?

---

## 9 · Worked Examples (informative)

### 9.1 · Vehicle (signature F4) and membership

**KindSignature(Vehicle)** *(F4)*:

* `hasVIN(x)` is true and parseable;
* `axles(x) ≥ 2`;
* `hasBrakeSystem(x)`;
* Standards: `registryAPI v1.4`; `Γ_time` policy: rolling 365 d for registry fields.

**`U.EntitySet(slice)`**: “records in `registryAPI v1.4` for plant `A` at build `b`, as of `Γ_time`.”
**`Extension(Vehicle, slice)`**: all records satisfying the predicates **in that `slice`**.
**Monotonicity:** `PassengerCar ⊑ Vehicle` ⇒ `Extension(PassengerCar, s) ⊆ Extension(Vehicle, s)`.

### 9.2 · AuthenticatedRequest (definedness & fail‑closed)

**KindSignature(AuthenticatedRequest)** *(F4)*:

* `Request` with `authHeader` present and `authSignature` valid according to `AuthStandard v2.3`;
* `Γ_time`: point in time for key validity check.

**Definedness:** `MemberOf(–, AuthenticatedRequest, slice)` is **undefined** if `AuthStandard v2.3` is **absent** in `slice` ⇒ guards **fail closed** (C3.2‑K‑07).

### 9.3 · Clinical cohort (low‑F signature; deterministic membership)

**KindSignature(AdultPatient)** *(F3→F4 as it hardens)*:

* `ageYears(x, Γ_time) ≥ N` (jurisdictional N varies; recorded in the Context’s signature note).
* `EntitySet(slice)`: EHR `ehr‑east v7.5` @ `Γ_time`;
* Membership deterministic if DOB present; undefined otherwise (fail closed).

---

## 10 · Anti‑patterns & Remedies (informative)

| Anti‑pattern                                         | Why it’s wrong                        | Remedy                                                              |
| ---------------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------- |
| Using “latest” implicitly in membership              | Non‑deterministic; unreproducible     | Require explicit `Γ_time`; treat freshness separately in **R**      |
| Encoding Scope (“only in EU plant”) in the signature | Confuses applicability with describedEntity | Move such conditions to **Claim scope (G)**; keep signature general |
| Declaring `k₁ ⊑ k₂` but not ensuring subset behavior | Breaks typed reasoning                | Tighten `KindSignature` or drop the `⊑` link                        |
| Treating RoleMask as a different kind                | Catalog sprawl; hidden semantics      | Keep mask as adaptation; promote to subkind if widely reused        |
| Membership relying on external, unnamed assumptions  | Hidden dependencies; review fatigue   | Name assumptions in the signature; point to Standards/versions      |

---

## 11 · Rationale (informative)

### 11.1 · Why give **F** to `KindSignature`?

Because rigor in the **definition of a kind** materially affects how safely teams can quantify over it. A signature at **F4** (predicate‑like) makes membership checkable in principle; **F7+** (machine‑checked) can support proof‑carrying development. Keeping this **separate from claim‑level F** prevents “signature formalization” from inflating unrelated claims.

### 11.2 · Why **Extension** is not **Scope**

* **Extension** answers: *“Which entities count as `k` **in this slice**?”*
* **Scope (G)** answers: *“In which slices does **this claim** hold?”*
  Blending the two recreates the old failure mode where “more abstract wording” was treated as “wider applicability.” USM already gives the set‑algebra for G; Kind‑CAL supplies the **typed universe** the claim quantifies over.

### 11.3 · Why **determinism** and **fail‑closed**?

Guards must be **reproducible** and **auditable**: same `slice` ⇒ same membership result. If inputs are missing (undefinedness), the safest default is **deny** (fail closed), prompting either a richer slice or a scope/claim change.

---

## 12 · Conformance checklist (normative)

| ID            | Requirement                                                                                     |
| ------------- | ----------------------------------------------------------------------------------------------- |
| **C3.2‑K‑03** | Every `KindSignature(k)` **declares `U.Formality`** (F0…F9).                                    |
| **C3.2‑K‑04** | Signature changes that alter membership are **content changes** (Contexts may version kinds).      |
| **C3.2‑K‑05** | `MemberOf(e, k, slice)` is **deterministic** for fixed `(k, slice)` (no “latest”).              |
| **C3.2‑K‑06** | **Monotonicity:** if `k₁ ⊑ k₂` then `Extension(k₁, s) ⊆ Extension(k₂, s)` for all `s`.          |
| **C3.2‑K‑07** | **Definedness:** outside domain, membership **fails closed**; guards deny use.                  |
| **C3.2‑K‑08** | **Separation:** guards keep **Scope coverage** (USM) and **membership** as distinct predicates. |
| **C3.2‑S‑01** | The Context **documents `U.EntitySet(slice)`** (stable, addressable via `slice`).                |
| **C3.2‑S‑02** | `slice` **specifies `Γ_time`**; membership **must not** rely on implicit recency.               |


# C.3.3 · **KindBridge & CL^k — Cross‑context Mapping of Kinds**  \[A]

> **One‑line summary.** Defines **`KindBridge`** as the normative mechanism for moving **kinds** (their **intent** and selected **subkind‑of** links) between bounded contexts (“Contexts”). A bridge declares **how a source kind maps to a target kind**, which parts of the **`⊑`** order are preserved or collapsed, and publishes a **type‑congruence level `CL^k`** with **loss notes** and a **definedness area**. **`CL^k` penalties apply only to Reliability (R)** when a claim depends on Cross‑context classification; **F** (formality) and **G** (Claim scope) remain unchanged. Scope translation continues to use the **USM Bridge + CL** channel; **KindBridge** is a **separate, parallel channel** for describedEntity.

---

## 0 · Status, Placement, Dependencies 

**Status.** Normative architheory in **Part C**. Identifier **C.3.3**.
**Audience.** Engineering managers, architects, assurance leads, editors.

**Depends on.**

* **C.3.1 — U.Kind & SubkindOf (Core):** kinds are context‑local intensional objects; `⊑` is a partial order; kinds **do not carry Scope**.
* **C.3.2 — KindSignature (+F) & Extension/MemberOf:** signature declares its own **F**; membership `MemberOf(e,k,slice)` is **deterministic** per `U.ContextSlice`.
* **A.2.6 — USM (Context slices & Scopes):** Claim scope (**G**) and Work scope live on claims/capabilities; scope bridging and **CL** penalties are defined there.
* **C.2.2 — F–G–R:** weakest‑link; penalties land in **R**, not **F/G**.
* **C.2.3 — U.Formality (F):** signature rigor.

**Non‑goals.**
— No repository/notation mandates; conceptual only.
— No Scope mapping here (that’s USM); **KindBridge** maps **kinds**, not scopes.
— No new arithmetic on `CL^k`; it reuses the **ordinal anchor semantics** of CL (Part B) but applies to kinds.

## 1 · Purpose & Audience

Cross‑context reuse fails in two **orthogonal** ways:

1. **Applicability** (G): *where* the claim holds (handled by USM Scope Bridge).
2. **describedEntity** (Kind): *what* the claim quantifies over (handled by **KindBridge**).

**C.3.3** gives managers an explicit, auditable channel for **(2)**, so a team can say, with evidence: *“`Vehicle` in Lab maps to `TransportUnit` in Plant with `CL^k=2`; the EV subkind collapses; here’s what we lost.”* Guards stay deterministic; assurance math stays clean (penalties in **R** only).

---

## 2 · Context

Contexts use different **classifications**: ontology classes vs shape Standards, regulatory cohorts vs app types, etc. Informal “same‑name” reuse silently mutates describedEntity. USM already made scope moves explicit. **KindBridge** does the same for kinds: **declare the mapping**, rate its **congruence**, and capture known **losses**.

---

## 3 · Problem

1. **Semantic drift.** Moving a claim into a target‑context with a different taxonomy changes “what counts” without anyone noticing.
2. **Hidden order breaks.** Subkind relationships invert or vanish; downstream proofs/tests are misapplied.
3. **Entangled channels.** Teams conflate “scope mapping” with “kind mapping,” making it impossible to assign penalties coherently.
4. **Incomputable guards.** “We map it somehow” yields non‑deterministic classification at guard time.

---

## 4 · Forces

| Force                                    | Tension to resolve                                                                              |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Minimal disclosure vs precision**      | Bridges must be light to write yet precise enough to avoid semantic drift.                      |
| **Local autonomy vs global reuse**       | Each target‑context keeps its vocabulary; reuse requires explicit, reviewable mappings.                   |
| **Typed safety vs agility**              | We need typed compatibility checks without blocking exploratory reuse.                          |
| **Separate channels vs operator burden** | Two channels (Scope & Kind) must be explicit, but guard writers shouldn’t drown in boilerplate. |

---

## 5 · Solution — The **KindBridge** object (overview)

A **KindBridge** connects **source** Context **A** and **target** Context **B** for a set of kinds. It declares:

1. **Mapping of kinds**: either to named target kinds or via **signature translation** rules.
2. **Order preservation**: which `⊑` links are preserved (monotone), which are **collapsed**, and which are **unknown** (not claimed).
3. **Type‑congruence `CL^k`**: reuses the **same anchors/labels** as **CL** (Part B) but applies to kind intent/order (not to Scope). *Gloss:* higher `CL^k` ⇒ closer preservation of kind intent and declared `⊑` links.
4. **Loss notes**: human‑readable list of invariants and subkinds **not preserved**.
5. **Definedness area**: the subset of `U.ContextSlice` characteristics where the mapping is **intended** to be used (e.g., certain Standards/versions).
6. **Determinism**: fixed versions + mapping rules ⇒ deterministic result (no “latest”).

**Effect on assurance.** When a **claim** in B depends on classification that goes through this bridge, **reduce R** by a monotone penalty **Ψ(`CL^k`)**. **Do not** change **F** or **G**.

---

## 6 · Norms & Invariants (normative)

> The following formalize the **KB‑01…KB‑12** rules announced in C.3.

### 6.1 · Subject & Scope of a KindBridge

**KB‑01 (Subject).** A KindBridge **maps**:

* one or more **KindSignature**(s) from source to target; and
* an **explicitly declared subset of `⊑` links** (which it claims to preserve or collapse).

**KB‑02 (No Scope).** A KindBridge **MUST NOT** map Claim/Work scope (**G**). Scope translation uses the **USM Bridge + CL** channel (A.2.6, Part B).

**No blended score.** Congruence for Scope (**CL**) and for Kind (**CL^k**) **MUST NOT** be aggregated into a single “interoperability” score in guards; each channel is assessed and penalized **separately**. See **Annex C.3.A §5 (E‑06)**.


### 6.2 · Declaration & Shape

**KB‑03 (Declaration).** A KindBridge record **SHALL** include:

1. source/target Contexts and vocabulary/Standard **versions**;
2. a **kind mapping** per source kind `k`: either a **named** target kind `k′` or a **signature translation rule** that constructs the **target‑context** `KindSignature(k′)` (the result is owned and versioned in the target Context);
3. an **order preservation claim** for any `k₁ ⊑ k₂` it covers: *preserved* / *collapsed* / *unknown*;
4. **`CL^k`** value (using the CL anchor ladder) labeled **“kind‑congruence”**;
5. **loss notes** (non‑preserved invariants, collapsed subkinds, equality quirks);
6. **definedness area** (constraints on `U.ContextSlice` dimensions where the bridge is meant to apply).

**KB‑04 (Determinism & local evaluation).** Given fixed Context versions and mapping rules, **translateₖ** **MUST** be deterministic (no implicit “latest”). After mapping to `k′`, **membership SHALL be evaluated using the target Context’s own `KindSignature(k′)` and `MemberOf(–, k′, –)`**; source‑context membership results **MUST NOT** be reused as truth in guards (they may be cited as evidence in **R**).

### 6.3 · Order & Monotonicity

**KB‑05 (Monotone order).** If the bridge claims to **preserve** `k₁ ⊑ k₂`, then in the target Context **`translateₖ(k₁) ⊑′ translateₖ(k₂)`** **MUST** hold.
**KB‑06 (No inversions).** The bridge **MUST NOT** assert preserved links that **invert** order. If real‑world constraints force reversal, the link **MUST** be marked **not preserved** with a **loss note**.
**KB‑07 (Collapse semantics).** Marking a link as **collapsed** is allowed (two subkinds mapped to one target kind), but the record **SHALL** list the merged subkinds and any properties thereby lost.

### 6.4 · Congruence & Assurance

**KB‑08 (Anchor reuse & AT neutrality).** **`CL^k`** reuses the **ordinal anchor semantics** of CL (Part B) but applies **to kinds**. Editors **SHALL** label it explicitly as **kind‑congruence** to avoid confusion with Scope CL. **KindBridge records MUST NOT compute or alter KindAT (C.3.5 AT‑04); AT is editorial and independent of `CL^k`.**
**KB‑09 (Effect on R only).** When a claim in the target Context depends on `MemberOf(–, translateₖ(k), TargetSlice)`, a **monotone penalty `Ψ(CL^k)`** **SHALL** reduce **R** (alongside any `Φ(CL)` penalty from the Scope Bridge). Implementations **MUST NOT** adjust **F or G** due to `CL^k`.
**KB‑10 (Chaining).** For a chain of bridges, **effective `CL^k` = min** of the links (weakest‑link).

### 6.5 · Loss Notes & Definedness

**KB‑11 (Loss notes).** Bridges **SHALL** publish human‑readable **loss notes**: which invariants of `KindSignature` are **not preserved**, which subkinds are **collapsed**, and any **higher‑equality** caveats (e.g., up‑to‑iso only).
**KB‑12 (Definedness & guard use).** The bridge’s **definedness area** **SHALL** be stated. Guards **MUST fail closed** outside it (i.e., if a classification relies on the bridge where it is not defined, the guard denies use).

---

## 7 · Interactions (informative)

### 7.1 · With USM Scope bridges (two channels)

When using a claim across Contexts, expect **two concurrent bridges**:

* **Scope Bridge (USM)**: maps **G**; publishes **CL**; penalty **Φ(CL)** to **R**.
* **KindBridge (this pattern)**: maps **kinds**; publishes **`CL^k`**; penalty **Ψ(`CL^k`)** to **R**.

**Discipline:** compute both; **do not** collapse them into one “interoperability score.”

 See **Annex C.3.A §5 (E‑01)** for the normative evaluation order in guards.

### 7.2 · With membership (C.3.2)

After mapping `k` to `k′ = translateₖ(k)`, the **target Context** evaluates membership **as usual**: `MemberOf(e, k′, TargetSlice)`. If the bridge provides a **signature translation**, that definition becomes the **local** `KindSignature(k′)` (versioned per target Context policy).

### 7.3 · With Role masks (C.3.4)

If a claim uses a **RoleMask(k)** across Contexts, you need:

* a **KindBridge** for `k` (`CL^k` + loss notes), and
* a documented **mask adapter** (how mask constraints translate).
  Penalties still land in **R**. If the mask’s effect is stable and widely reused, consider promoting it to a **subkind** on the target side.

### 7.4 · With guards (Annex C.3.A)

Use the **`Guard_XContext_Typed`** macro (Annex C.3.A), which requires **both bridges** and applies **both penalties** to **R**:

* find Scope bridge (CL≥threshold), translate **G**, check coverage;
* find KindBridge (`CL^k≥threshold`), translate **kind**, check **membership definedness**;
* apply **Φ(CL)** and **Ψ(`CL^k`)** to **R**; keep **F/G** untouched.

---

## 8 · Authoring, Review & Rating Guidance (informative)

### 8.1 · Authoring a KindBridge

* **Start narrow & honest.** Declare only the kinds and `⊑` links you **actually preserve**; mark the rest **unknown**.
* **Prefer named targets.** If the target already has a suitable kind, map to it; use **signature translation** only when necessary, and list what’s preserved vs weakened vs dropped.
* **Write loss notes in plain language.** Example: “EV vs ICE subkinds collapsed; battery‑health invariants dropped.”
* **Fix the definedness area.** Bind to target Standards/versions and any environment selectors essential to classification.
* **Assign `CL^k` from exemplars.** Calibrate on concrete counter‑examples and preserved properties; resist optimistic ratings.

### 8.2 · Review playbook (10 minutes)

1. **Two bridges present?** Scope Bridge **and** KindBridge?
2. **Order claims honest?** Any `⊑` inversions? Collapses disclosed?
3. **`CL^k` plausible?** Based on preserved properties, not name similarity?
4. **Loss notes present?** Will they force narrowing of Scope or extra tests?
5. **Definedness area clear?** Guard will **fail closed** outside it?
6. **Penalties wired to R?** No hidden tweaks to **F/G**?

### 8.3 · Rating `CL^k` (rules of thumb)

* **High `CL^k`**: signature equivalence or **up‑to‑iso**; `⊑` fragment preserved; only cosmetic losses.
* **Medium `CL^k`**: some invariants weakened; selected subkinds collapsed; order preserved on critical path.
* **Low `CL^k`**: name‑only correspondences; properties diverge; order not preserved. Expect significant **R** penalty and/or adapters.

---

## 9 · Worked Examples (informative)

### 9.1 · Vehicle → TransportUnit (manufacturing)

**Source kind:** `Vehicle` (K2, signature F4).
**target Context:** `PlantB`, kind `TransportUnit` exists.

**KindBridge:**

* `Vehicle ↦ TransportUnit`; **order**: preserves `PassengerCar ⊑ Vehicle`; **collapses** `EV ⊑ Vehicle` into `TransportUnit` (no EV subkind).
* **`CL^k=2`** (mid); **loss notes:** “battery‑health invariants not carried”; **definedness:** only for `registryAPI v1.4`, `Γ_time` in last 365 d.

**Use:** Claim quantified over `Vehicle` crosses to `PlantB`.
**Guards:** scope bridge CL=2 (rig bias); kind bridge `CL^k=2`; both penalties reduce **R**. **F/G** unchanged.

### 9.2 · AuthenticatedRequest across services (software)

**Source kind:** `AuthenticatedRequest` defined by `AuthStandard v2.3`.
**target Context:** `Frontend` with different auth header scheme.

**KindBridge:** signature translation (`authHeader` → `x‑auth`), preserves “signature valid” property; **`CL^k=3`** (high).
**Loss notes:** none; **definedness:** only where `AuthStandard v2.3` is in scope.

**Effect:** Rules quantified over `AuthenticatedRequest` can be reused; **R** penalty small (Ψ(3) near 1). Scope remains independent (API v2.3).

### 9.3 · AdultPatient across jurisdictions (clinical)

**Source kind:** `AdultPatient` (≥ 18 at `Γ_time`).
**target Context:** `JurisdictionY` uses ≥ 21.

**KindBridge:** `AdultPatient ↦ AdultPerson_Y` with boundary mismatch; **`CL^k=1`**.
**Loss notes:** “Boundary 18 vs 21; map narrows to ≥ 21”.
**Guard:** Require **mask adapter** or **narrow Scope** to cohorts where DOB is known and ≥ 21. **R** penalty strong; **F/G** remain as declared.

---

## 10 · Anti‑patterns & Remedies (informative)

| Anti‑pattern                                 | Why it’s wrong                         | Remedy                                                                              |
| -------------------------------------------- | -------------------------------------- | ----------------------------------------------------------------------------------- |
| One “interop score” for both kind & scope    | Blurs channels; corrupts penalties     | Use **two bridges**; apply **Φ(CL)** (Scope) and **Ψ(`CL^k`)** (Kind) **separately** |
| Claiming preserved `⊑` while inverting order | Makes typed reasoning unsound          | Mark as **not preserved**; add **loss note**; consider adapter or subkind redesign  |
| Hiding collapses                             | Overstates coverage                    | List collapsed subkinds explicitly; plan extra **R** for lost granularity           |
| “Latest mapping”                             | Non‑deterministic; non‑auditable       | Version bridges; bind to Standards/versions; **fail closed** outside definedness    |
| Using KindBridge to widen G                  | Conflates describedEntity with applicability | Keep Scope edits in **USM** (ΔG±); KindBridge never widens Scope                    |
| Adjusting F/G for poor `CL^k`                 | Violates F–G–R & USM separation             | Route consequences to **R** only; consider narrowing Scope or adding adapters       |

---

## 11 · Conformance Checklist (normative)

| ID        | Requirement                                                                                                                                          |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **KB‑01** | A KindBridge **maps** `KindSignature`(s) and an explicitly declared subset of `⊑` links.                                                             |
| **KB‑02** | A KindBridge **MUST NOT** map Scope; Scope uses USM Bridge (Part B).                                                                                 |
| **KB‑03** | Bridge records **SHALL** include Contexts/versions, kind mapping/rules, order‑preservation claims, **`CL^k`**, **loss notes**, and **definedness area**. |
| **KB‑04** | Mapping **MUST** be **deterministic** given fixed versions/rules (no “latest”).                                                                      |
| **KB‑05** | Preserved order links **MUST** stay **monotone**: `k₁ ⊑ k₂` ⇒ `translateₖ(k₁) ⊑′ translateₖ(k₂)`.                                                    |
| **KB‑06** | **No inversions**: preserved links cannot invert order; otherwise mark **not preserved** and add loss notes.                                         |
| **KB‑07** | **Collapses** are allowed but **MUST** list merged subkinds and lost properties.                                                                     |
| **KB‑08** | **`CL^k`** **SHALL** reuse CL anchors and be labeled **“kind‑congruence.”**                                                                           |
| **KB‑09** | **Penalties:** when classification uses KindBridge, apply **Ψ(`CL^k`)** to **R**; **MUST NOT** adjust **F/G**.                                        |
| **KB‑10** | **Chaining:** effective `CL^k` across a chain is **min** (weakest‑link).                                                                              |
| **KB‑11** | **Loss notes** **SHALL** enumerate non‑preserved invariants and collapsed subkinds.                                                                  |
| **KB‑12** | **Definedness:** bridge **SHALL** state its valid area; guards **fail closed** outside it.                                                           |

**Integration requirements with Part B (bridges):**

* **B‑P1.** Part B (Bridges) **SHALL** list **KindBridge** as a distinct bridge class alongside USM Scope bridges.
* **B‑P2.** Part B **SHALL** state that **`CL^k` penalties route to R** via a monotone **Ψ**, never to **F/G**.
* **B‑P3.** Part B **SHALL** define **chaining = min** for both **CL** and **`CL^k`** (weakest‑link).
* **Templates.** ESG/Method templates should expose fields for **Scope Bridge (CL)** and **KindBridge (`CL^k`)** with loss notes & definedness.


# C.3.4 · **RoleMask — Contextual Adaptation of Kinds (without cloning)**  \[A]

> **One‑line summary.** Defines **`U.RoleMask(kind, Context)`** as a **context‑local adaptation** of a `U.Kind` that (a) adds **constraints** and/or **vocabulary bindings**, and (b) may **narrow** membership **deterministically** within a `U.ContextSlice`, **without creating a new kind**. RoleMasks are catalogued, versioned, and guard‑addressable; frequent, stable constraint masks **SHOULD be promoted** to explicit **subkinds**. Cross‑context use of a RoleMask requires a **KindBridge** (for kinds) and, when needed, a **MaskAdapter** (for mask constraints). All penalties route to **R**; **F/G** remain unchanged.

---

## 0 · Status, Placement, Dependencies 

**Status.** Normative architheory in **Part C**. Identifier **C.3.4**.
**Audience.** Engineering managers, architects, reviewers, editors.

**Depends on.**

* **C.3.1 — U.Kind & SubkindOf (Core):** kinds are intensional; `⊑` is a partial order; kinds **carry no Scope**.
* **C.3.2 — KindSignature (+F) & Extension/MemberOf:** signature F; deterministic `MemberOf(e,k,slice)`; `EntitySet(slice)`.
* **C.3.3 — KindBridge & CL^k:** Cross‑context kind mapping; `CL^k` penalties → **R** only.
* **A.2.6 — USM (Context slices & Scopes):** Claim/Work scope (**G**) over `U.ContextSlice`; bridges and **CL** for scope.
* **C.2.2 — F–G–R; C.2.3 — U.Formality (F).**

**Non‑goals.**
— No repository/notation mandates; conceptual only.
— RoleMask is **not** a governance tier, data policy, or “mini‑type system.”
— RoleMask does **not** redefine Scope; context conditions belong to **USM**.

## 1 · Purpose (manager’s view)

Teams often need a **local projection** of a widely used kind:

* **Constraint:** “For our procedure, take `Vehicle` **with ABS** only.”
* **Vocabulary:** “Here, `AuthHeader` is called `X‑Auth`.”

If each team clones a fresh kind, catalogs fragment and bridges multiply. **RoleMask** is the disciplined alternative: **keep the kind identity**, apply **declared constraints and bindings**, and make the mask **first‑class** (registered, versioned, guard‑addressable). When a mask becomes stable “de‑facto subkind,” **promote** it to `⊑`.

**Benefits:** fewer near‑duplicates, cleaner Cross‑context reuse, deterministic guards, and auditable narrowing instead of hand‑wavy “this is the version we mean.”

---

## 2 · Context

Kinds (C.3.1/3.2) name **what** claims quantify over; USM (A.2.6) governs **where** claims hold. In practice, procedures need **local tailoring** of kinds for a role/process (compliance profile, product line, cohort). RoleMask gives that tailoring **without** mutating describedEntity (Kind) or applicability (Scope).

---

## 3 · Problem

1. **Kind sprawl.** Teams mint near‑duplicate kinds (“Account\_PCI”, “Account\_Ledger”), and alignment decays.
2. **Hidden constraints.** Informal “we only accept …” statements leak into prose; guards can’t check them deterministically.
3. **Scope conflation.** Contextual requirements (jurisdiction, API version) get smuggled into “type” talk, blurring Scope vs Kind.
4. **Cross‑context fragility.** Masks don’t travel unless their constraints are mapped; teams reuse names and hope.

---

## 4 · Forces

| Force                                   | Tension to resolve                                                                                           |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Local specialization vs common core** | Need Context‑specific tailoring **without forking** kinds.                                                      |
| **Expressivity vs determinism**         | Masks must express real constraints **and** be **deterministically checkable** at guard time.                |
| **Context vs entity constraints**       | Conditions over **ContextSlice** (Scope) vs conditions over **entities** (membership) must be split cleanly. |
| **Reuse vs proliferation**              | Encourage reuse and promotion to subkind when stable; avoid a mask zoo.                                      |

---

## 5 · Solution — **RoleMask** (overview)

A **RoleMask** is a **named, versioned binding** `U.RoleMask(kind, Context)` that:

1. **Adds constraints** (entity‑level predicates only),
2. **Binds vocabulary/notation** (aliases, field maps) for the Context/process,
3. **May declare context expectations** (selectors over `U.ContextSlice`, e.g., jurisdiction, API version). **These are enforced via USM Scope guards** (A.2.6) and **do not** change mask membership.
4. **May narrow membership**: `Extension_mask(k, s) ⊆ Extension(k, s)` (entity‑level narrowing only),
5. **Never creates a new kind**; identity stays with `k`.
6. **Is guard‑addressable** and **deterministic** (no “latest”).

**Mask types (declared):**

* **Constraint mask** — adds constraints; may narrow membership;
* **Vocabulary mask** — aliases only; no membership change;
* **Composite mask** — both.

**Separation discipline.**

* **Entity‑level predicates** (e.g., “hasABS(x)”) → **mask membership** (narrowing).
* **Context conditions** (e.g., “jurisdiction=EU”, “API=v2.3”) → **USM Scope** guards (intersection), **not** mask membership.
  Masks **may carry both kinds** of information, but guards must route them into the **right channel**.

---

## 6 · Norms & Invariants (normative)

> The following formalize and expand **RM‑01…RM‑08** referenced in C.3.

### 6.1 · Definition & Shape

**RM‑01 (Definition).** `U.RoleMask(kind, Context)` **SHALL** be a named, versioned record with:
(a) **intent** (what role/procedure the mask serves),
(b) **constraints** (entity‑level predicates; optional context requirements),
(c) **vocabulary/notation bindings**,
(d) **membership narrowing** definition (if any),
(e) **intended guard use**.

**RM‑02 (Not a new kind).** A RoleMask **MUST NOT** introduce a new `U.Kind`. If the domain needs a stable refinement, Contexts **SHALL** publish an explicit `SubkindOf` node (C.3.1).

**RM‑03 (Determinism).** Membership under a mask (if defined) **MUST** be **deterministic** given `slice` and published constraints; implicit “latest” is forbidden.

**RM‑04 (Mask taxonomy).** A mask **SHALL** declare its type: **constraint / vocabulary / composite**.
— **Vocabulary masks** MUST NOT change membership;
— **Constraint/composite masks** MAY narrow membership **only via entity‑level predicates**.

### 6.2 · Separation of channels

**RM‑05 (Context vs entity).**

* Predicates about **entities** (features, attributes) MAY narrow membership: `Extension_mask(k, s) ⊆ Extension(k, s)`.
* Predicates about **ContextSlice** (jurisdiction, Standards, Γ\_time) **SHALL** be enforced via **USM Scope** guards (A.2.6). Masks **MUST NOT** hide Scope requirements inside membership checks.

**Guard routing.** Enforce ContextSlice predicates via **USM Scope** (A.2.6) and entity predicates via **membership**; see **Annex C.3.A §4.3 (Guard_MaskedUse)** and **§5 (E‑01)** for the normative order of checks.

**RM‑06 (Guard use).** Guards **MAY** reference a RoleMask by name **only** if the mask is **registered, versioned, and its constraints are observable** at guard time. Mask names **MUST NOT** be treated as kind synonyms.

### 6.3 · Promotion & Catalog

**RM‑07 (Promotion rule).** A constraint mask reused broadly and stably **SHOULD** be promoted to an explicit **subkind** with a `⊑` link; retire the mask or keep it as a vocabulary wrapper. Editors **SHALL** track promotions in the catalog.

**RM‑08 (Catalog).** Contexts **SHALL** catalog masks (name, version, type, intent, constraints, bindings, examples, related subkinds, known bridges/adapters). Redundant masks **SHOULD** be consolidated.

### 6.4 · Cross‑context use

**RM‑09 (Bridges & adapters).** If a claim uses `MemberOf(–, RoleMask(k), TargetSlice)` across Contexts, the receiving Context **SHALL** require:
(a) a **KindBridge** for `k` (`CLᵏ`, loss notes), and
(b) a **MaskAdapter** — a documented, deterministic mapping of the mask’s **entity‑level constraints** and **vocabulary bindings** into the target Context — whenever those constraints/bindings differ.
Penalties **MUST** route to **R**: `Ψ(CLᵏ)` for kind, plus any **Φ(CL)** for scope bridge.

**RM‑10 (Definedness & fail‑closed).** Mask evaluation **SHALL** state its definedness area; outside it, guards **fail closed**.

---

## 7 · Invariants & Non‑goals (normative)

* **No Scope leakage.** RoleMasks **cannot** widen/narrow **Claim scope (G)**; any context conditions are enforced by USM guards.
* **Identity preservation.** The carrier kind remains `k`; RoleMask does not change describedEntity.
* **Weakest‑link unaffected.** RoleMasks do not alter weakest‑link rules on **F/R**; guards **route entity predicates to membership** and **context predicates to USM Scope**.

## 8 · Interactions (informative)

### 8.1 · With Kinds & Subkinds (C.3.1)

Use RoleMask for **procedural tailoring**. If the tailoring becomes **conceptual** and stable, **introduce a subkind** with `⊑` and update references.

### 8.2 · With Membership & Signature (C.3.2)

* **Entity‑level constraints** live in mask membership (deterministic).
* **Signature F** belongs to the kind; raising F in the signature does not auto‑change masks.

### 8.3 · With KindBridge (C.3.3)

A RoleMask crossing Contexts needs **two artifacts**: the KindBridge (`CL^k`, loss notes) and a **MaskAdapter** (how constraints/aliases translate). **R** gets both penalties; **F/G** stay intact. If the adapter systematically narrows membership in the target Context, consider **target‑side subkind**.

### 8.4 · With Guards (Annex C.3.A)

Use **`Guard_MaskedUse`** (Annex **C.3.A §4.3**). It requires:
— mask registration & determinism;
— Scope coverage (A.2.6), **Γ\_time** explicit;
— where Cross‑context: KindBridge (`CL^k`) + MaskAdapter + penalties → **R**.
— **Cross‑context combo.** When masks cross Contexts, use **`Guard_MaskedUse`** together with **`Guard_XContext_Typed`** (Annex **C.3.A §4.5**) so both bridges are checked and both penalties (**Φ(CL)** and **Ψ(CLᵏ)**) land in **R**.
— **Order of checks.** Follow **Annex C.3.A §5 (E‑01)**: typed compatibility first, then Scope coverage, then penalties to **R** and freshness.

## 9 · Anti‑patterns & Remedies (informative)

| Anti‑pattern                                      | Why it’s wrong                         | Remedy                                                                                |
| ------------------------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------- |
| Mask as “new type”                                | Duplicates kind; breaks alignment      | Keep the kind; if stable refinement → publish **subkind** (`⊑`).                      |
| Hiding Scope in mask membership                   | Conflates channels; non‑portable       | Move context conditions to **USM** guards; keep only entity predicates in membership. |
| Unregistered mask in guards                       | Non‑deterministic; un‑auditable        | Register & version the mask; fail closed otherwise.                                   |
| Cross‑context use without KindBridge/MaskAdapter     | Silent semantic drift                  | Require **KindBridge** + **MaskAdapter**; apply `Ψ(CL^k)` and any `Φ(CL)` to **R**.    |
| Mask proliferation (ten masks that mean the same) | Catalog entropy; inconsistent behavior | Consolidate; promote frequently used constraints to **subkinds**.                     |
| Treating mask name as kind synonym                | Hides constraints; invites misuse      | In prose, say “`RoleMask(k, name)`”; in guards, reference mask fields explicitly.     |

---

## 10 · Worked Examples (informative)

### 10.1 · `Vehicle@ABSOnly` (constraint mask)

**Kind.** `Vehicle` (K2, signature F4).
**Mask.** `Vehicle@ABSOnly` — entity‑level predicate `hasABS(x)=true`; type **constraint**.
**Guards.** `MemberOf(–, Vehicle@ABSOnly, TargetSlice)` defined & deterministic; **Scope** (surface/speed/rig/Γ\_time) checked separately.
**Promotion?** If ABS‑only becomes a conceptual category, publish `VehicleWithABS ⊑ Vehicle` and retire the mask.

### 10.2 · `AuthenticatedRequest@Frontend` (vocabulary mask)

**Kind.** `AuthenticatedRequest` defined by `AuthStandard v2.3`.
**Mask.** `@Frontend` binds `authHeader → X‑Auth` (aliases only); **no** narrowing; type **vocabulary**.
**Cross‑context.** If reused in another Context, require **KindBridge** for the kind; **no** MaskAdapter needed (aliases are local).
**R.** Only scope bridge penalties apply (if any).

### 10.3 · `AdultPatient@Clinic` (composite mask) across jurisdictions

**Kind.** `AdultPatient` (≥ 18 at `Γ_time`).
**Mask.** `@Clinic`: entity constraint “DOB present”; context hint “EHR system = X” (this part routes to Scope). Type **composite**.
**Cross‑context.** Jurisdiction Y uses ≥ 21 → **KindBridge** with `CL^k=1`; **MaskAdapter** maps DOB fields.
**Guards.** Scope bridge (coding system) + KindBridge + MaskAdapter; penalties **Ψ(1)** (kind) + **Φ(CL)** (scope) to **R**.
**Outcome.** Allowed with reduced R; consider target‑side subkind `AdultPerson_Y`.

---

## 11 · Authoring & Review Guidance (informative)

### 11.1 · Authoring a RoleMask card

**Fields (suggested).** `name`, `kind`, `type (constraint/vocabulary/composite)`, `intent`, `constraints (entity vs context split)`, `bindings`, `membership definition (if any)`, `definedness`, `examples`, `known bridges/adapters`, `promotion note`.
**Rules of thumb.**

* Keep entity predicates **small and testable**.
* Put **context** in Scope, not in membership.
* If ≥ 3 teams reuse the same constraint mask → **promotion** review.

### 11.2 · Reviewer 7‑point checklist

1. Mask **registered** and **versioned**?
2. **Type** declared correctly (constraint/vocabulary/composite)?
3. Entity vs context **split** respected?
4. **Determinism** (no “latest”) satisfied?
5. Guard **routes** context to **USM** and entity to **membership**?
6. Any Cross‑context use has **KindBridge** + **MaskAdapter** with penalties **to R**?
7. **Promotion** warranted (stable, reused) or consolidation needed?

---

## 12 · Conformance Checklist (normative)

| ID        | Requirement                                                                                                                                                |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **RM‑01** | RoleMask **SHALL** be a named, versioned record with intent, constraints, bindings, membership definition (if any), and intended guard use.                |
| **RM‑02** | RoleMask **MUST NOT** introduce a new `U.Kind`; stable refinements **SHALL** be modeled as subkinds (`⊑`).                                                 |
| **RM‑03** | Mask membership (when defined) **MUST** be deterministic given `slice` and mask fields; implicit “latest” forbidden.                                       |
| **RM‑04** | Mask **SHALL** declare its type: constraint / vocabulary / composite; vocabulary masks **MUST NOT** change membership.                                     |
| **RM‑05** | Context conditions **SHALL** be enforced via **USM Scope** guards; membership narrowing **MAY** use entity predicates only.                                |
| **RM‑06** | Guards **MAY** reference a mask only if it is **registered, versioned**, and its constraints are **observable**; mask names **MUST NOT** be kind synonyms. |
| **RM‑07** | Frequently reused constraint masks **SHOULD** be **promoted** to subkinds; editors **SHALL** track promotions.                                             |
| **RM‑08** | Contexts **SHALL** catalog masks; redundant masks **SHOULD** be consolidated.                                                                                 |
| **RM‑09** | Cross‑context masked use **SHALL** declare a **KindBridge** (`CL^k`) and any **MaskAdapter**; penalties **MUST** reduce **R** only.                            |
| **RM‑10** | Mask definedness **SHALL** be stated; guards **fail closed** outside the defined area.                                                                     |

# C.3.5 · **KindAT — Intentional Abstraction Facet for Kinds (K0…K3)**  \[I/A]

> **One‑line summary.** Defines **KindAT** as an **informative facet** attached to `U.Kind` that classifies the **intentional abstraction stance** of a kind—**K0 Instance**, **K1 Behavioral Pattern**, **K2 Formal Kind/Class**, **K3 Up‑to‑Iso**—to **guide ΔF/ΔR planning, bridge expectations, catalog/search, and refactoring**. **KindAT is not a Characteristic**: it has **no algebra**, **no thresholds**, and **MUST NOT** appear in guards or composition math. All assurance remains in **F–G–R**; typed semantics remain in **C.3.1–C.3.4**.

---

## 0 · Status, Placement, Dependencies 

**Status.** Mixed:
— **Informative** for the anchors, heuristics, examples, and guidance.
— **Normative** for the **usage rules** that forbid employing AT in guards/composition and constrain its placement.

**Placement.** Part C (Kinds), identifier **C.3.5**. Audience: engineering managers, architects, editors, assurance leads.

**Depends on.**
— **C.3.1** (`U.Kind`, `U.SubkindOf (⊑)`), **C.3.2** (`KindSignature` + F, `Extension/MemberOf`), **C.3.3** (KindBridge + `CL^k`), **C.3.4** (RoleMask).
— **A.2.6 USM** (Claim/Work scope over `U.ContextSlice`), **C.2.2 F–G–R**, **C.2.3 U.Formality (F)**.
— **MM‑CHR** distinction **Facet vs Characteristic** (editors).

**Non‑goals.**
— No numerical scale, no gating, no composition operators, no “quality” scoring.
— No effect on **F**, **G**, or **R** besides **planning hints**.

## 1 · Purpose (manager’s view)

Teams constantly decide **how far to formalize** and **how broadly to validate**:

* *Are we speaking about **this cohort** (instances), about **things that behave like X** (pattern), about a **formal class** with invariants, or about objects **up to isomorphism**?*
* *Given that stance, should we invest in **F4 predicates**, **F7 proofs**, or **R** across variants?*
* *What kind of **KindBridge** is realistic (coarse mapping vs up‑to‑iso), and what **`CL^k`** should we expect?*

**KindAT** answers these with a **small, shared vocabulary (K0…K3)** that is **safe to use** (cannot distort F/G/R) yet **actionable** for planning and catalog/search.

---

## 2 · Context & Rationale

### 2.1 · The orthogonality we preserve

* **G (Claim scope)** is **where** a claim holds (A.2.6).
* **Kinds** give **what** a claim is about (C.3.1/3.2).
* **R** is assurance (evidence, freshness, penalties).
* **F** is expression rigor (C.2.3).

Teams often **conflate abstraction with applicability** (“sounds general ⇒ applies broadly”) or **over‑engineer proofs** where **slice‑checks** suffice. AT separates these concerns.

### 2.2 · Why a facet, not a Characteristic

Per **MM‑CHR**, **Characteristics** (e.g., F, G) carry algebra and appear in guards/composition. **KindAT** is only a **tag** on `U.Kind`:

* **No algebra, no thresholds**, not used in guards.
* **Editorial placement** only: on kinds, not on claims.
* **Planning signal**: what ΔF and ΔR typically pay off; what bridge style to expect.

This keeps AT **useful** without risking a “second G” or back‑door quality scores.

### 2.3 · Design choice recap (moved from C.3 §15.2)

* Making AT a Characteristic would **duplicate** G’s role and encourage gating.
* As a **facet**, AT remains a **catalog/navigation and planning device**, not an assurance dimension.

---

## 3 · **Anchors K0…K3** (informative)

> **How to read.** Each anchor states the **intentional stance** of the kind, **inclusion cues**, **non‑examples** (to prevent misuse), and **planning hints** (ΔF/ΔR/bridge expectations). Anchors are **context‑local editorial tags** on `U.Kind`.

### 3.1 · **K0 — Instance‑level**

**Intent.** The kind denotes **exemplars** or a **tightly curated set**; often a named cohort or a concrete template.
**Cues.** Membership relies on listing or direct identity features; little to no general invariants.
**Non‑examples.** Any kind with stable, general invariants belongs in **K2**.
**Planning hints.** Focus **R on TargetSlice** (executable checks, F5/6); avoid premature proof engineering. Bridges are **instance‑maps**; expect **low `CL^k`** outside the Context.

### 3.2 · **K1 — Behavioral Pattern**

**Intent.** The kind is a **role/behavioral** pattern (“things that act like …”), typically stated via Standards or controlled NL, not a full type.
**Cues.** “Duck‑typing” flavor; Standards reference behavior/state transitions.
**Non‑examples.** If you can state global invariants as predicates, consider **K2**.
**Planning hints.** Invest in **F3→F4** (predicate‑like acceptances); **R** must test **behavioral diversity**; bridges are **pattern maps** with moderate `CL^k`.

### 3.3 · **K2 — Formal Kind/Class**

**Intent.** A **formal class** with explicit **invariants/relations** (ontology class, type with Standards).
**Cues.** Predicate‑like signature, subkind lattice, invariants reviewed.
**Non‑examples.** Pure examples/cohorts (K0); informal roles (K1).
**Planning hints.** Raise **KindSignature F** to **F4+**, consider **F7** for safety‑critical cores; **R** should cover **subkinds/variants**; bridges are **type‑maps**, `CL^k` often medium/high.

### 3.4 · **K3 — Up‑to‑Iso**

**Intent.** Defined **up to isomorphism/equivalence** (category‑theoretic flavor; “equal as structure,” not by identity); equality‑as‑structure matters.
**Cues.** Statements invariant under isomorphism; reasoning by equivalence classes.
**Non‑examples.** Classes where identity matters beyond structure.
**Planning hints.** Expect **up‑to‑iso** bridges; `CL^k` can be high where equivalence is respected. **F7–F9** likely for key properties; **R** focuses on **witnesses of equivalence** at interfaces.

## 4 · Manager Heuristics (informative)

| Decision area       | K0                               | K1                          | K2                                         | K3                                      |
| ------------------- | -------------------------------- | --------------------------- | ------------------------------------------ | --------------------------------------- |
| **ΔF investment**   | Prefer F5/6 executable semantics | F3→F4 acceptance predicates | F4→F7 (predicates/proofs)                  | F7→F9 (proof‑carrying, higher equality) |
| **ΔR design**       | Slice‑focused checks             | Behavioral diversity        | Variant/subkind coverage                   | Equivalence witnesses at boundaries     |
| **Bridge style**    | Instance map                     | Pattern map                 | Type map                                   | Up‑to‑iso / functorial                  |
| **Expected `CL^k`** | Low outside Context                 | Medium                      | Med/High                                   | High where iso holds                    |
| **Refactoring**     | Aggregate to K2 when stable      | Crystallize invariants → K2 | Maintain lattice; promote masks → subkinds | Keep iso constraints explicit           |

---

## 5 · Misuse & Antidotes (informative)

* **“Higher AT ⇒ wider G.”** *Wrong.* **G** changes only via **ΔG** (USM). AT does not alter scope.
* **“Gate on AT.”** *Wrong.* Use **F** thresholds and scope/evidence guards; AT is never a gate.
* **“Depth in `⊑` ⇒ AT.”** *Wrong.* AT is about **intentional stance**, not graph depth.
* **“AT on claims.”** *Wrong.* AT tags **`U.Kind` only**.
* **“AT as quality score.”** *Wrong.* Use **F** and **R** for rigor/reliability.

---

## 6 · **Usage Rules (normative)**

> These are the **only** normative constraints in this pattern. Everything else is guidance.

**AT‑01 (Facet, not Characteristic).** KindAT **SHALL** be treated as a **Facet** per MM‑CHR: it has **no algebra, no thresholds**, and **MUST NOT** appear in guards or composition math.

**AT‑02 (Placement).** If recorded, KindAT **SHALL** be attached to **`U.Kind`** (or its catalog card). It **MUST NOT** be attached to claims/capabilities or used as a proxy for **G**/**F**/**R**.

**AT‑03 (Editorial discipline).** Editors **SHALL NOT** write text implying “higher AT widens scope” or “higher AT increases rigor/reliability.” Any such text **MUST** be revised to reference **ΔG**/**F**/**R** explicitly.

**AT‑04 (Bridge neutrality).** **KindBridge** records **MUST NOT** compute or adjust AT; they may include *informative* remarks about likely anchor alignment. `CL^k` is independent of AT and is assessed from signature/order preservation.

**AT‑05 (Catalog).** Contexts that use AT **SHOULD** record it in **Kind catalog entries** alongside: signature snippet & **F**, subkinds, RoleMasks, KindBridges. Absence of AT implies **“not set”**, not K0.

---

## 7 · Authoring & Review Guidance (informative)

### 7.1 · How to tag (fast rubric)

* If the card lists **concrete items/cohorts**, tag **K0**.
* If the card defines **behavioral obligations** in prose/templates but few global invariants, tag **K1**.
* If the card states **predicates/invariants** and participates in a **subkind lattice**, tag **K2**.
* If the card explicitly reasons **up to isomorphism**, tag **K3**.

### 7.2 · Review checklist (5 minutes)

1. Is the **carrier** a **`U.Kind`** (not a claim)?
2. Does the **tag** match the **signature** (intent)?
3. Are **ΔF**/**ΔR** implications noted for planning (not gating)?
4. Any **RoleMasks** that should be promoted to subkinds (K2 hygiene)?
5. Any **Cross‑context reuse** that suggests **bridge style** (pattern/type/iso)?

---

## 8 · Integration Notes (informative)

* **With C.3.1/3.2 (Kinds, Signature, Extension).** AT guides *how* to evolve signature **F** and *what* R coverage is sensible; it **does not** change membership semantics.
* **With C.3.3 (KindBridge).** AT hints at likely **bridge style** (instance‑map / pattern‑map / type‑map / up‑to‑iso), but **`CL^k`** is still computed from signature/order preservation; penalties route to **R**.
* **With C.3.4 (RoleMask).** Persistent K1‑style masks often warrant **promotion to K2 subkinds**.
* **With A.2.6 (USM).** All scope decisions remain under **G**. AT text should never be used to infer coverage.
* **With C.2.3 (F).** AT does not raise/lower **F**; it **suggests** where raising F is cost‑effective.

---

## 9 · Worked Mini‑Examples (informative)

* **K0 (Instance).** `Account_US_GAAP_2025_Q1_Cohort`. Plan **R** slice checks; avoid type‑maps across Contexts.
* **K1 (Behavior).** `CacheableRequest` (“idempotent under retry; cache key well‑formed”). Raise **F3→F4**; design **R** for failure‑mode diversity; expect **pattern bridges**.
* **K2 (Formal).** `Account` with invariants (balance = debits−credits; posting rules). Raise **F4+**; plan **R** over `Asset`/`Liability` subkinds; bridge via **type maps**.
* **K3 (Up‑to‑Iso).** `UndirectedGraph` up to node relabeling. Expect **up‑to‑iso bridges**; proofs at **F7+**; **R** checks interface equivalence witnesses.

---

## 10 · Conformance Checklist (normative)

| ID        | Requirement                                                                                                   |
| --------- | ------------------------------------------------------------------------------------------------------------- |
| **AT‑01** | KindAT is treated as **Facet** (no algebra/thresholds); **MUST NOT** appear in guards/composition.            |
| **AT‑02** | AT **MUST** be attached to **`U.Kind`** only (if used); not to claims/capabilities.                           |
| **AT‑03** | Editorial text **MUST NOT** imply AT alters **F/G/R**; revise to name **ΔF/ΔG/ΔR** instead.                   |
| **AT‑04** | KindBridge **MUST NOT** compute/alter AT; `CL^k` is assessed independently.                                   |
| **AT‑05** | If a Context catalogs AT, it **SHOULD** include it in Kind cards with signature **F**, subkinds, masks, bridges. |


# C.3.A · **Typed Guard Macros for Kinds + USM (Annex)**  \[A/I]

> **One‑line summary.** Provides **normative guard macros** that combine **USM Scope** (A.2.6) with **Kind‑CAL** (C.3.x) so authors can gate state changes and compositions that **quantify over kinds** without conflating **describedEntity** (Kinds) with **applicability** (Scope **G**) or **assurance** (**R**). Includes **decision trees, anti‑patterns, and examples** (informative). **AT (KindAT)** is **never** used in guards.

---

## 0 · Status, Placement, Dependencies 

**Status.** Mixed:
— **Normative**: guard macro clauses, evaluation order, fail‑closed discipline, conformance checklist.
— **Informative**: ... decision trees, anti‑patterns, worked examples, macro skeletons.

**Placement.** Part C (Kinds), identifier **C.3.A** (Annex). Audience: engineering managers, editors, reviewers, assurance leads.

**Depends on.**
— **A.2.6 USM**: `U.ContextSlice`, `U.ClaimScope` (**G**), `U.WorkScope`, ∈/∩/**SpanUnion**/translate, **Γ\_time** policy, Bridge + **CL** (scope).
— **C.3.1**: `U.Kind`, `U.SubkindOf (⊑)`; **C.3.2**: `KindSignature` (with **F**) and `Extension/MemberOf`; **C.3.3**: **KindBridge** + `CL^k` (kind‑congruence) & loss notes; **C.3.4**: **RoleMask**.
— **C.3.5**: **KindAT** (facet) — **explicitly forbidden** in guards.
— **C.2.2 F–G–R**: weakest‑link, penalties to **R** only; **C.2.3 F**: F0…F9 (expression rigor).
— **Part B Bridges & CL**: scope bridge semantics and CL ladder.

## 1 · Purpose & Audience

**Purpose.** Give Contexts a **single set** of guard shapes to:
(a) **admit** typed claims safely,
(b) **compose** typed claims/specs,
(c) **use** RoleMasks properly, and
(d) **reuse across Contexts** via **both** scope and kind bridges—**without** inventing new scales or conflating **G**, **F**, and **R**.

**Audience.** Engineering managers and reviewers who must read/author guards that are **legible, deterministic, and auditable** in context.

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

## 3 · Solution Overview (what these guards do)

All guards in this Annex share three invariants:

1. **Fail‑closed.** If any required predicate is undefined/false, the guard **denies** the transition.
2. **Deterministic.** Given a fixed **TargetSlice** (with explicit **Γ\_time**) and published declarations, evaluation yields one outcome.
3. **Separation of concerns.**
   *Typed compatibility* (same‑Context `⊑` or **KindBridge**) is **not** Scope.
   *Scope coverage* is a USM set‑membership judgment over **Context slices**.
   *Assurance penalties* (**Φ(CL)** for scope bridges; **Ψ(`CL^k`)** for kind bridges) reduce **R** only.

---

## 4 · Normative Guard Macros

> **Notation.** “**SHALL**” clauses are normative obligations. “Notes” are informative reminders. Names like `Guard_TypedClaim` are editorial handles; Contexts may alias them, but **MUST** preserve semantics. Macro names (e.g., `Guard_TypedClaim`) are editorial handles; Contexts may alias them provided the logical obligations are preserved.


### 4.1 · **Guard\_TypedClaim** — admit a claim quantified over a kind

**Intent.** Approve a state transition that asserts Claim **C** which quantifies over `U.Kind` **k** at **TargetSlice**.

**Guard\_TypedClaim(C, k, TargetSlice, thresholds?)** — **SHALL** include, in this order:

1. **ScopeCoverage.** `U.ClaimScope(C) covers TargetSlice`. *(USM A.2.6)*
2. **Γ\_time declared.** TargetSlice **SHALL** specify **Γ\_time** (point/window/policy). No “latest”. *(A.2.6)*
3. **Kind definedness.** `MemberOf(?, k, TargetSlice)` is **defined and deterministic**. *(C.3.2 K‑05/K‑07)*
4. **Typed compatibility.**
   4.1 **same Context**: if C expects `k′`, require `k ⊑ k′`. *(C.3.1)*
   4.2 **Cross Context**: if Contexts differ, require a declared **KindBridge** that maps `k → k′` and publishes **`CL^k ≥ c`** with loss notes. *(C.3.3)*
5. **Assurance penalties (R only).** If step 4.2 used a KindBridge, the guard **SHALL** apply a monotone penalty **Ψ(`CL^k`)** to **R**. If a **Scope bridge** was used to move C’s Scope (USM), apply **Φ(CL)** to **R**. *(C.2.2 + C.3.3 + Part B)*
6. **Evidence freshness (if trust is implied).** Freshness windows and expiry checks **SHALL** be separate predicates (not Scope). *(C.2.2)*
7. **Formality threshold (if ESG mandates).** If the Context gates rigor, require `U.Formality(C) ≥ F_k`. *(C.2.3)*

**Prohibitions.**
— **AT forbidden.** KindAT **MUST NOT** appear in this guard. *(C.3.5 AT‑01/02)*
— **No “domain” placeholders.** Guards **SHALL** name an addressable **TargetSlice**, not a fuzzy “domain”.

---

### 4.2 · **Guard\_TypedJoin** — compose two typed claims/specs (A → B)

**Intent.** Permit composition where **A** produces facts over `k_A` and **B** consumes `k_B`.

**Guard\_TypedJoin(A, k\_A; B, k\_B; TargetSlice)** — **SHALL** include:

1. **TypedCompat.**
   1.1 **same Context**: require `k_A ⊑ k_B`.
   1.2 **Cross Context**: require **KindBridge** mapping `k_A → k′_B` with **`CL^k ≥ c`** and `k′_B ⊑ k_B`.
2. **ScopeSerial.** Compute `Scope_serial = ClaimScope(A) ∩ ClaimScope(B)`. Require `Scope_serial covers TargetSlice`. *(A.2.6)*
3. **Penalties (R only).** Apply **Ψ(`CL^k`)** if a KindBridge was used; apply **Φ(CL)** if a Scope bridge was used. *(C.2.2 / Part B / C.3.3)*
4. **Freshness.** Guard **SHALL** assert required freshness windows for evidence **along the serial path**.
5. **No type‑by‑scope.** The guard **MUST NOT** widen Scope to “fix” a type mismatch; remedies are subkind introduction, adapter, or bridge.

**Mask awareness.** If B expects a **RoleMask(k\_B)**: either show A’s outputs already satisfy mask constraints, or add a documented **mask adapter** (see 4.3) and treat any **contextual** constraints as part of **ScopeSerial**.

---

### 4.3 · **Guard\_MaskedUse** — use a RoleMask with a kind

**Intent.** Use `U.Kind` **k** under a **RoleMask** **m** in Context **R**.

**Guard\_MaskedUse(k, m, TargetSlice)** — **SHALL** include:

1. **MaskRegistered.** `RoleMask(k, m, version)` is **registered and versioned**. *(C.3.4 RM‑06)*
2. **MaskDeterminism.** All mask constraints are **observable** on TargetSlice; if the mask narrows membership, it **SHALL** be deterministic. *(RM‑03)*
3. **MaskType clarity.** Mask **SHALL** declare its type: constraint / vocabulary / composite. *(RM‑04)*
4. **Promotion cue.** If mask is reused widely as a de‑facto subkind, editors **SHOULD** promote it to an explicit `⊑` link. *(RM‑05)*
5. **Cross‑context use.** If `TargetSlice.Context ≠ owner(k).Context`, require:
   5.1 **KindBridge** with **`CL^k ≥ c`**;
   5.2 **MaskAdapter** (if constraints need translation), deterministic;
   5.3 Penalty **Ψ(`CL^k`)** to **R**. *(RM‑07 + C.3.3)*
6. **ScopeCoverage.** `U.ClaimScope(artifact) covers TargetSlice`. *(A.2.6)*

**Prohibitions.**
— **Mask ≠ Kind.** Guards **MUST NOT** treat the mask name as a synonym for the Kind. *(RM‑06)*

### 4.4 · **Guard\_SpanUnion\_Typed** — publish parallel coverage across independent support lines

**Intent.** Publish **SpanUnion** of scopes for **the same typed claim** supported by **independent** lines `L₁…Lₙ`.

**Guard\_SpanUnion\_Typed(C, k, {Lᵢ})** — **SHALL** include:

1. **Per‑line discipline.** For each line `Lᵢ`, first satisfy **Guard\_TypedClaim(C, k, Sliceᵢ)** (or its Cross‑context variant) at the relevant slices/supports.
2. **Independence justification.** Publisher **SHALL** include a partition or certificate showing that essential components of `Lᵢ` are **disjoint** from `Lⱼ` (no shared weakest link). *(A.2.6 §7.3)*
3. **Published scope.** `Scope_published = SpanUnion({Sᵢ})`, where each `Sᵢ` is the serial scope for line `Lᵢ`.
4. **No overreach.** The union **MUST NOT** include slices not covered by any `Sᵢ`.
5. **Typed consistency.** The **describedEntity** (kind **k**) is **the same** across lines; if not, normalize via subkinds or adapters before union.

**Note.** Independence and union rules are USM‑native; this macro ties them to typed claims without adding new algebra.

---

### 4.5 · **Guard\_XContext\_Typed** — Cross‑context typed reuse (both bridges)

**Intent.** Reuse **C** quantified over **k** in another Context’s **TargetSlice**.

**Guard\_XContext\_Typed(C, k, TargetSlice)** — **SHALL** include:

1. **Scope bridge.** There **exists** a Scope Bridge **b\_s** `(source = owner(C).Context, target = TargetSlice.Context)` with **CL ≥ c\_s**. *(Part B)*
2. **Kind bridge.** There **exists** a KindBridge **b\_k** `(source = owner(k).Context, target = TargetSlice.Context)` with **`CL^k ≥ c_k`**. *(C.3.3)*
3. **Mapped scope coverage.** `Scope′ = translate(b_s, ClaimScope(C))` and `Scope′ covers TargetSlice`.
4. **Mapped kind definedness.** `k′ = translate(b_k, k)` and `MemberOf(?, k′, TargetSlice)` is **defined**.
5. **Penalties (R only).** Apply **Φ(CL(b\_s))** and **Ψ(`CL^k(b_k)`)** to **R**.
6. **Loss notes.** Publisher **SHALL** attach loss notes from both bridges (rig bias, collapsed subkinds, etc.).

**Prohibitions.**
— **Do not** “merge” bridges; Scope and Kind are orthogonal channels.
— **Do not** alter **F** or **G** due to `CL`/`CL^k`; penalties land in **R** only.

---

## 5 · Evaluation Semantics & Order (normative)

**E‑01 (Order of checks).** Guards **SHALL** check **typed compatibility first** (same‑Context `⊑` or KindBridge), **then** Scope coverage (USM), **then** apply penalties to **R** and verify freshness.

**E‑02 (Determinism).** Given fixed inputs (slices, bridges, versions), evaluation **MUST** be deterministic. “Latest” time, unversioned Standards, or implicit mappings are disallowed.

**E‑03 (Fail‑closed).** Undefined membership (`MemberOf`) or missing bridge **MUST** cause guard failure.

**E‑04 (No AT in guards).** AT is an editorial facet and **MUST NOT** be referenced. *(C.3.5 AT‑01/02)*

**E‑05 (Weakest link on congruence).** For chained bridges, effective **CL** / **`CL^k`** is the **minimum** of links.

**E‑06 (Separation of predicates).** Scope coverage and evidence freshness **SHALL** be distinct predicates; do not fold freshness into Scope or kinds.

**Evaluation order.** Apply checks in the order defined in **§5 (E‑01)**: typed compatibility → Scope coverage → penalties to **R** → freshness.


## 6 · Conformance Checklist (normative)

| ID        | Requirement                                                                                                                              |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **GC‑01** | Guards that admit/compose typed claims **SHALL** use **Guard\_TypedClaim** or **Guard\_TypedJoin** (or proven‑equivalent Context aliases).  |
| **GC‑02** | Guards that use RoleMasks **SHALL** use **Guard\_MaskedUse** (or equivalent) and comply with RM‑01…RM‑07.                                |
| **GC‑03** | Cross‑context typed reuse **SHALL** use **Guard\_XContext\_Typed** with **both** bridges; penalties **MUST** route to **R** (Φ/Ψ), not to F/G. |
| **GC‑04** | All guards **SHALL** declare **Γ\_time** explicitly and **SHALL** fail closed on undefined membership or missing bridges.                |
| **GC‑05** | Guards **MUST NOT** reference **AT**; any such reference **MUST** be removed or replaced with ΔF/ΔG/ΔR predicates.                       |
| **GC‑06** | Scope union **MUST** follow USM **SpanUnion** rules (independence justification); typed union **MUST NOT** change describedEntity.             |

### 6.1 · What counts as “proven‑equivalent” (editorial rule)

A Context may adopt a different surface phrasing **iff** the Context’s guard contains **all** obligations listed in the relevant macro, in the same logical roles (typed compatibility, Scope coverage, R penalties, freshness).

### 6.2 · Where penalties land (assurance calculus hook)

**Norm.** **Φ(CL)** (scope congruence) and **Ψ(`CL^k`)** (kind congruence) are **monotone non‑increasing** functions into **R**. Contexts **SHALL** calibrate them per policy; this Annex does not prescribe numeric forms.

### 6.3 · Minimal conceptual formulas (informative)

* **R after bridges:** `R_final = R_base × Φ(CL_scope) × Ψ(CL_kind)` (concept only).
* **No arithmetic on F/G.** F is ordinal (thresholds only); G is set‑valued (membership only).

---

## 7 · Decision Trees (informative)

**D1 · Admitting a typed claim**

1. **same Context?** If **yes** → check `⊑` (`k ⊑ k′` if expected). If **no** → require **KindBridge**.
2. **Scope coverage?** Compute `covers(TargetSlice)`.
3. **Membership defined?** `MemberOf(?, k(′), TargetSlice)` defined? If **no** → deny.
4. **Bridges used?** Apply penalties **Φ/Ψ** to **R**.
5. **Freshness?** Check windows. **Optional**: `F ≥ F_k` if ESG mandates.

**D2 · Composing A → B**

1. Typed: `k_A ⊑ k_B` or **KindBridge** to `k′_B ⊑ k_B`.
2. Scope: `Scope(A) ∩ Scope(B)` covers TargetSlice.
3. Penalties: apply **Φ/Ψ** to **R**.
4. Freshness: along serial path.
5. If **mask** expected: either A implies it or add **mask adapter**.

**D3 · Union across lines**

1. Prove per‑line typed admission.
2. Provide independence partition.
3. Publish **SpanUnion**; no extrapolation.

---

## 8 · Guard Anti‑patterns & Remedies (informative)

| Anti‑pattern                                     | Why it’s wrong                         | Remedy                                                             |
| ------------------------------------------------ | -------------------------------------- | ------------------------------------------------------------------ |
| **Widening G** to “fit” a type mismatch          | Conflates describedEntity with applicability | Introduce subkind, adapter, or KindBridge; keep G honest           |
| **Using mask name as kind**                      | Hides constraints; breaks determinism  | Register mask; reference constraints; promote to subkind if stable |
| **Ignoring `CL^k`** in Cross‑context classification | Under‑counts risk; silent drift        | Require KindBridge; apply **Ψ(`CL^k`)** to **R**                   |
| **Inferring Scope from Extension size**          | Scope ≠ Extension                      | Keep Scope (where) distinct from Extension (which instances)       |
| **Implicit “latest”** time                       | Non‑deterministic; non‑auditable       | Declare **Γ\_time** policy explicitly                              |
| **Gating on AT**                                 | AT is a facet, not a Characteristic    | Replace with ΔF thresholds or Scope/Evidence predicates            |

---

## 9 · Worked Examples (informative, brief)

> Detailed scenarios remain in **C.3 §11**. This Annex sketches how the macros apply; cross‑reference as needed.

**E1 — Safety braking policy (same Context).**
Use **Guard\_TypedClaim**: `PassengerCar ⊑ Vehicle` passes; `ClaimScope` ∩ plant scopes covers TargetSlice; no bridges → no penalties; freshness checked.

**E2 — Cross‑plant reuse (both bridges).**
Use **Guard\_XContext\_Typed**: Scope bridge (CL=2) narrows temp; KindBridge (`CL^k=2`) collapses EV subkind. Apply **Φ(2)**×**Ψ(2)** to **R**; publish loss notes.

**E3 — API rule with adapter.**
Use **Guard\_TypedJoin**: producer `Request` → consumer expects `AuthenticatedRequest`. Either prove `⊑` or add adapter; Scope remains separate (API v2.3 with Γ\_time window).

**E4 — Masked clinic cohort across jurisdiction.**
Use **Guard\_MaskedUse** + **Guard\_XContext\_Typed**: registered mask, deterministic DOB constraint; KindBridge `CL^k=1`; Scope bridge CL depends on coding; penalties to **R**; Scope narrowed to overlap.

---

## 10 · Rationale (why an Annex) (informative)

* **Focus.** Keeps **guard mechanics** together, easing adoption in ESG/Method templates.
* **Separation.** Prevents leakage of AT/typed flavor into “Scope math”.
* **Auditability.** Standard shapes let reviewers check determinism, bridges, penalties, and freshness quickly.
* **Inter‑pattern glue.** Hooks **USM**, **Kind‑CAL**, **Bridges**, and **F–G–R** without inventing new scales.

### Annex A · How typed reasoning plugs into **Compliance & Regulatory Alignment**  \[A/I]

> **For managers.** This section shows how to make **regulatory adoption and reuse** precise, auditable, and portable using **Kinds**, **KindBridges** (with a kind‑bridge congruence level, noted as **CL^k** for editors), and **USM Scope**. It cleanly separates *what the law is about* from *where and when it applies*, and routes any cross‑jurisdiction uncertainty to **R** (assurance). It never changes **F** (form) or **G** (scope) to hide mismatches.

---

#### A.1 Purpose & fit

**What this solves.** Regulations and standards name classes of things (“**Adult person**,” “**Class II medical device**,” “**Personal data**,” “**Lease**”). In one context they are native; in another they are foreign. Without typed reasoning, teams either (a) hand‑translate terms (silently changing meaning), or (b) reduce everything to Context labels (“domain = EU”), which cannot be checked by guards.

**What we add.**

1. Model regulatory categories as **Kinds** (with `KindSignature` and `⊑`),
2. map them across Contexts with **KindBridges** and **type‑congruence `CL^k`**,
3. express **Claim scope (G)** over **Context slices** that explicitly list *jurisdiction, version, and a time selector (Γ_time)*, and
4. apply **R‑penalties** (`Ψ(CL^k)`and, if scope is bridged,`Φ(CL)`) while **keeping F and G unchanged**.

---

#### A.2 Normative obligations  \[A]

**C‑REG‑1 (Regulatory kinds).** Regulatory categories **SHALL** be represented as `U.Kind` in the authority’s Context (e.g., `AdultPerson@RegY`, `MedicalDeviceClassII@FDA`, `PersonalData@GDPR`, `Lease@IFRS`). Each such kind **SHALL** have a `KindSignature` with a declared **F** level (C.3.2).

**C‑REG‑2 (KindBridge).** Cross‑context reuse of a regulatory category **MUST** declare a **KindBridge** with a kind‑bridge congruence level (**CL^k**) and **loss notes** (C.3.3). The mapping **SHALL** preserve the “is‑a / subkind‑of” direction (no inversions).

**C‑REG‑3 (Scope is USM).** Regulatory **applicability** (jurisdiction, effective dates, product families, platforms) **SHALL** be expressed as **Claim scope (G)** over `U.ContextSlice`, with an explicit **time selector (Γ_time)**. Do **not** encode applicability into kinds.

**C‑REG‑4 (No synonym shortcuts).** Editors **MUST NOT** treat legal terms as synonyms of local kinds without a KindBridge. Any term alignment **SHALL** be documented (mapping + `CL^k` + loss notes).

**C‑REG‑5 (Determinism).** `MemberOf(e, k_reg, slice)` **MUST** be deterministically evaluable when used in guards (no “latest law” or unstated grace periods).

**C‑REG‑6 (Penalties land in R).** When a claim or guard relies on Cross‑context classification (membership decided via a KindBridge), the receiving Context **MUST** apply the **kind‑bridge penalty** (based on **CL^k**) to **R**; if the **Scope** is also bridged, apply the **scope‑bridge penalty** (based on **CL**) to **R** as well. **F** and **G** remain unchanged.

**C‑REG‑7 (Editioning).** Changes in law/regulator guidance that alter membership or applicability **SHALL** be recorded as content changes: update `KindSignature` (kinds) and/or update **Claim scope** (ΔG±). Using an implicit “latest” time is forbidden; guards must name a time selector (Γ_time).

**C‑REG‑8 (Masks, not clones).** Local process nuances (e.g., clinic‑specific cohort definitions) **SHALL** be captured with **RoleMasks** over the adopted kind; do **not** clone a new kind unless a stable **subkind** is warranted.

---

#### A.3 Guard macros (ready to use)  \[A]

**(a) `Guard_RegAdopt` — adopt a regulatory requirement into a Context (Plain: check scope, map the legal category, and account for penalties)**

Use when an internal policy is defined by reference to an authority’s category.

```
Inputs: Claim P (policy), RegKind k_reg in Context R_auth, TargetSlice S_local
Guard_RegAdopt(P, k_reg, S_local):
  1. ScopeCoverage:       U.ClaimScope(P) covers S_local                 // USM
  2. Γ_time:              S_local specifies Γ_time (no "latest")         // USM
  3. KindBridge:          a KindBridge exists that maps the legal category to a local kind, with **CL^k** at least the minimum policy level
  4. MemberOfDefined:     MemberOf(?, k_local, S_local) is defined       // determinism
  5. Penalties→R:         apply the **kind‑bridge penalty** (based on CL^k) to **R**
  6. ScopeBridge?         if the policy’s scope lives in the authority’s Context, translate it via a Scope Bridge; apply the **scope‑bridge penalty** (based on CL) to **R**
  7. EvidenceFreshness:   freshness windows for any bound evidence hold  // C.2.2
```

**(b) `Guard_RegChange` — react to a regulatory change (Plain: re‑issue the kind and/or scope and refresh penalties)**

```
Inputs: Reg change Δ (new edition, guidance), impacted kinds/claims
Guard_RegChange(Δ):
  1. Identify impact:      does Δ alter KindSignature (membership) or Scope predicates?
  2. If KindSignature:     version k_reg; update KindBridge; re-evaluate CL^k; update loss notes
  3. If Scope:             publish ΔG± (widen/narrow) to Claim scope; update guards
  4. Reassess penalties:   recompute Ψ(CL^k), Φ(CL) → R
  5. Γ_time discipline:    set sunrise/sunset; forbid implicit retroactivity in guards
```

**(c) `Guard_RegXContextUse` — cross‑jurisdiction use with both bridges (Plain: move scope and kind, then account for both penalties)**

```
Guard_RegXContextUse(P, k_reg@R_auth, S_local@R_local):
  1. Scope bridge:      a Scope Bridge from the authority Context to the local context exists with CL at least the policy minimum; the translated scope covers the local slice
  2. Kind bridge:       a KindBridge maps the legal category to a local kind with **CL^k** at least the policy minimum
  3. MemberOfDefined:   MemberOf(?, k_local, S_local) is defined
  4. Penalties→R:       apply the **scope‑bridge** and **kind‑bridge** penalties to **R**
  5. Loss-guided narrow: optionally narrow Scope' where known losses are material (best practice)
```

---

#### A.4 Worked examples  \[I]

**(1) Healthcare — “Adult” dosage rule across jurisdictions**

*Reg source.* Jurisdiction Y defines `AdultPerson@RegY` (AT around K2, F4) with **age at least 18**; your hospital Context uses `AdultPatient` (**age at least 21**).
*Claim.* “For all `x ∈ AdultPatient`: dosage ≤ D/kg for drug M.”
*Adoption.*

* **KindBridge.** Map `AdultPerson@RegY → AdultPatient`; **`CL^k = 1`**; **loss note:** boundary mismatch (18↔21).
* **Scope.** `{jurisdiction=Y, formulary=M, time selector (Γ_time)=from 2026‑01‑01}`.
* **Guard.** `Guard_RegAdopt` passes; **R** penalized by `Ψ(1)`. Policy narrows Scope to mapped cohort (age≥21) for in‑house use.
* **Change.** If Y changes adult to ≥19 (new edition), run `Guard_RegChange`: version the kind, refresh the bridge, re‑assess `CL^k`, update guards.

**(2) Privacy — GDPR↔CCPA PII across Contexts**

*Reg kinds.* `PersonalData@GDPR`, `PersonalInformation@CCPA`.
*Internal kind.* `PersonalData@Product` with masks per data store.
*Policy claim.* “No sharing of `SensitiveAttribute` outside processors.”
*Adoption.*

* **KindBridges.** `SensitiveAttribute@GDPR → SensitiveAttribute@Product` (**`CL^k=2`**); `SensitivePersonalInformation@CCPA → SensitiveAttribute@Product` (**`CL^k=1`**, loss: biometric nuance).
* **Scope.** Two policies with **SpanUnion** over `{jurisdiction=EU}` and `{jurisdiction=CA}`, each with its own **Γ\_time** windows and evidence freshness.
* **Guards.** For CA, apply stronger **R** penalty (`Ψ(1)`), and narrow to the mapped subset (exclude ambiguous fields).
* **Do not.** Do not rename GDPR terms to local labels **without a KindBridge**.

**(3) Export control — US EAR “600‑series” classification**

*Reg kind.* `EAR600SeriesItem@US` (AT≈K2, F3→F4 as predicates are formalized).
*Local kind.* `Product@Company`.
*Work scope.* `{destination=countries, end_use, time selector (Γ_time)=shipment date}` for the shipping capability.
*Adoption.*

* **KindBridge.** Map `EAR600SeriesItem@US → Product@Company`; `CL^k=2` (loss: component kit edge cases); loss notes recorded.
* **Capability guard (Method–Work).**

  * `U.WorkScope(Ship)` covers `JobSlice` (destination, end use, time).
  * `MemberOf(product, EAR600_mapped, JobSlice)` defined (classification present).
  * Apply `Ψ(2)` to **R** (classification uncertainty) and, if reusing US scope text, `Φ(CL_scope)` too.
* **Outcome.** Shipment admitted only for allowed destinations; higher **R** may require manual review.

**(4) Finance — IFRS vs US GAAP “Lease”**

*Reg kinds.* `Lease@IFRS`, `Lease@USGAAP`.
*Local kind.* `LeaseStandard@Corp` used in policy “recognize lease liabilities.”
*Adoption.*
* **KindBridge.** `Lease@IFRS → LeaseStandard@Corp` (**`CL^k=2`**; loss: short‑term exceptions differ).
* **Scope.** `{jurisdiction=IFRS, Γ_time=financial period, ledger=v7}`.
* **Evidence.** LA plans cover subkinds (operating vs finance) per your classification; the kind‑bridge congruence level (CL^k) drives extra testing near boundary cases.

---

#### A.5 Design guidance & pitfalls  \[I]

**Do this.**

* **Treat regulatory categories as Kinds.** Put the *definition* into `KindSignature` (aim for **F4** predicates where practical).
* **Make time explicit.** In guards, require a **time selector (Γ_time)** for effective dates and grace periods. Forbid “latest”.
* **Publish bridges with loss notes.** If two jurisdictions’ categories are “almost the same,” say *how*, rate **`CL^k`**, and note what is lost.
* **Split “where” from “what.”** Keep **Scope (G)** over `U.ContextSlice` (jurisdiction, plant, Standard versions) separate from **MemberOf** on the kind.
* **Route uncertainty to R.** Use `Ψ(CL^k)` and `Φ(CL)`; never modify **F/G** to hide ambiguity.

**Avoid this.**

* **Synonym games.** Don’t alias “Adult” to local `AdultPatient` in prose. Use a **KindBridge**.
* **Scope by labels.** “Domain = EU” is not a guard. Use explicit `U.ContextSlice` fields (jurisdiction, version, time selector) and **Scope** predicates.
* **Hiding time.** Never rely on “current law”; always fix **Γ\_time** (point/window/policy).
* **Widening G to compensate for type gaps.** If kinds don’t line up, introduce a **subkind**, add a **mask/adapter**, or **narrow**; don’t “make the scope bigger”.

---

#### A.6 Migration checklist  \[I]

1. **Inventory** regulatory references in policies/specs.
2. **Create Kind cards** for referenced legal categories (intent summary, `KindSignature` + **F**, known subkinds, AT tag if helpful).
3. **Publish KindBridges** to your local kinds with `CL^k` and loss notes.
4. **Rewrite guards** to use **Scope coverage** (USM) plus `MemberOf` on the mapped kind; add an explicit **time selector (Γ_time)**.
5. **Wire penalties**: `Ψ(CL^k)` and `Φ(CL)` lower **R**; refresh evidence windows.
6. **Catalog RoleMasks** for local nuances; promote frequently reused masks to **subkinds**.

---

#### A.7 Manager’s one‑page pattern  \[I]

* **Question 1 — Where does the rule apply?** → **Scope (G)** over **Context slices** (jurisdiction, plant, Standard, and a **time selector (Γ_time)**).
* **Question 2 — About what things?** → **Kind** (regulatory category) with a **KindBridge** if foreign.
* **Gate recipe.** **Scope covers the TargetSlice** and **membership for the mapped kind is defined**, and **both bridges are present where needed**; then **apply bridge penalties to R** and decide.
* **Change handling.** New law edition? Update `KindSignature`/Bridge (kinds) and/or **Scope** (ΔG); never rely on “latest.”
* **Accountability.** Keep **loss notes**, **CL/CL^k**, and **Γ\_time** in the decision record.


### Annex B · How typed reasoning plugs into **Assurance Lanes (VA/LA/TA) & Evidence design**  \[A/I]

**Intent (manager’s view).** Typed reasoning turns “prove/test/qualify” into a **repeatable plan**. By making *what the rule talks about* explicit (named **Kinds**, their **subkinds**, and optional **RoleMasks**), you can:

1. design **proof obligations** that actually quantify over the right things (VA),
2. build **test plans** that cover the **right variants/subkinds** in the **right context slices** (LA), and
3. isolate **tool risk** (TA) instead of letting it bleed into scope or type semantics.

**Invariant reminders.**
— **Scope (G)** is *where* a claim holds — expressed over `U.ContextSlice` (with an explicit time selector, **Γ_time**).
— **Kind membership** is *which things* the claim ranges over inside that slice — checked with `MemberOf(..., kind, slice)`.
— **Bridge penalties**: the **scope‑bridge penalty** (based on **CL**) and the **kind‑bridge penalty** (based on **CL^k**) both lower **R** (assurance). They never change **F** (form) or **G** (scope).

#### B.1 What you get with typed assurance  \[I]

* **Targeted proofs (VA).** If a policy says “for every **PassengerCar** …” (notation hint: ∀x:PassengerCar), the VA lane now has a clear target. You can prove obligations **once for the kind** (and its subkinds), instead of re‑proving per ad‑hoc label.
* **Subkind‑aware test plans (LA).** Test matrices are indexed by **subkinds** (and RoleMasks) × **context slices**; coverage stops being accidental.
* **Deterministic guards.** A test/proof either **applies** to the TargetSlice and Kind (`Scope covers & MemberOf defined`) or it doesn’t. No “latest,” no silent widening.
* **Clean tool boundaries (TA).** You qualify the **prover/model‑checker/classifier** once and route **tool confidence** to TA, not to “broadened” claims.

---

#### B.2 Normative obligations for evidence design  \[A]

**EA‑1 (Two checks).** Every VA/LA artifact that supports a typed claim **SHALL** bind **both**:

* **Scope predicate**: `U.ClaimScope(Claim) covers TargetSlice` (with explicit `Γ_time`), and
* **Kind predicate**: `MemberOf(?, k, TargetSlice)` is **defined** (deterministic).

**EA‑2 (Subkind coverage).** When a claim quantifies over `k`, target‑contexts **SHALL** justify LA coverage **per relevant subkind** of `k` (or **per RoleMask** if masks stand in for stable subkinds). “Representative set” **MUST** be stated explicitly.

**EA‑3 (Independence for unions).** If a published **SpanUnion** of evidence lines is used to enlarge covered area, **independence** of lines **SHALL** be documented (no shared weakest link).

**EA‑4 (Bridges accounted).** If a VA/LA artifact travels across Contexts:

* **Scope movement** **SHALL** use a Scope Bridge (Part B) with **CL** and apply the **scope‑bridge penalty** to **R**.
* **Kind movement** **SHALL** use a **KindBridge** (§ C.3.3) with **CL^k** and apply the **kind‑bridge penalty** to **R**.
  Neither movement **SHALL** alter **F** or **G**.

  Neither movement **SHALL** alter **F** nor **G**.

**EA‑5 (Freshness).** LA evidence **SHALL** declare freshness windows tied to `Γ_time` (no implicit “latest”). Expiry **MUST** fail guards closed until refreshed.

**EA‑6 (No scope‑by‑wording).** Editors **MUST NOT** widen **G** by rewriting a claim to sound “more general.” Widening **G** (ΔG+) is permitted **only** with new support that truly enlarges the set of slices.

**EA‑7 (TA separation).** Tool qualification (TA) **SHALL** be tracked independently. VA/LA guards **MUST NOT** substitute “tool is trusted” for content proof/coverage.

---

#### B.3 Designing the **evidence matrix**  \[I]

A practical way to plan LA/VA is a **matrix**:

| Row set                       | Column set                                                   | Cell content                                                                                                           |

| ----------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| **Kinds** (subkinds or masks) | **Context slices** (Standard versions, env ranges, `Γ_time`) | **Evidence unit** (proof fragment, test batch, monitoring window), with **Scope** and **MemberOf** predicates attached |

* **Choose rows.** Start with the kind and list **relevant subkinds** (notation hint: kᵢ is a subkind of k) or stable **RoleMasks**.
* **Choose columns.** Split your declared **Scope (G)** into **named slices** you intend to support (e.g., “dry, speed up to 50” and “wet, speed up to 40” with specific rigs and versioned Standards).
* **Fill cells.** Attach one or more **evidence units** per cell (proof obligations for VA; test campaigns/monitoring windows for LA). Mark **bridged** cells and their **CL/CL^k** penalties to **R**.

> **Tip.** For formal kinds and “up‑to‑iso” kinds (AT K2/K3), expect **more rows** (more variants to cover). For instance‑like kinds (AT K0), expect **fewer rows** and **tighter columns** (narrow slices, stricter freshness).

---

#### B.4 VA lane — proofs that match the kind  \[A/I]

**What VA contributes.** Proofs reduce ambiguity and eliminate many LA burdens when they **truly quantify over the intended kind** and **live in the declared Scope**.

**VA‑patterns (informative):**

* **Proof over the Kind (F7–F8).** “For every **PassengerCar**, the property holds” (notation hint: ∀x:PassengerCar). If the property depends on subkind‑specific rules, split lemmas per subkind.
* **Proof‑carrying components.** When the content is **F8** (dependent types), the build rejects violations; LA can shrink to **conformance smoke** within the slices.
* **Up‑to‑iso (AT K3).** Equational reasoning “up‑to‑iso” is acceptable **only** if the KindSignature works at that level and receivers accept **KindBridge** that preserves equivalences.

**VA‑obligations (normative):**

* **VA‑1.** A proof artifact **SHALL** cite the **Kind** it quantifies over and reference the **Claim scope** slices it assumes.
* **VA‑2.** Cross‑context acceptance of proofs **SHALL** use both bridges (Scope+Kind) and apply **Φ/Ψ** penalties to **R** (never to F/G).
* **VA‑3.** If the proof relies on **tool kernels**, their **TA** status **SHALL** be disclosed; weakening TA **MUST NOT** be “paid for” by silent scope widening.

**Mini‑example (VA).**
Policy P: “∀ x: PassengerCar. stoppingDistance(x) ≤ 50 m on dry at speed≤50.”
— **Kind**: `PassengerCar ⊑ Vehicle` (K2), signature F4 (predicates).
— **Scope**: `{surface=dry, speed≤50, rig=v3, Γ_time=rolling 180 d}`.
— **Proof**: a proof assistant lemma over `PassengerCar` (tool choice is context‑local).
— **Reuse** to Plant‑B: a Scope Bridge with **CL=2** (rig bias) and a KindBridge with **CL^k=3** (same classification). Apply the **scope‑bridge penalty** for CL=2 and the **kind‑bridge penalty** for CL^k=3 to **R**.

---

#### B.5 LA lane — tests & monitoring that cover the right variants  \[A/I]

**What LA contributes.** Empirical assurance for claims with executable semantics or physical interfaces; especially when F ≤ F6 or when stochastic/real‑world effects matter.

**LA‑patterns (informative):**

* **Cover by subkind.** Test at least one representative per subkind; add more where variability inside a subkind matters.
* **Boundary probing.** Concentrate tests near **KindSignature** and **Scope** boundaries (e.g., temp limits, speed caps).
* **Hybrid checks (F6).** When software controllers interact with physical systems, ensure **both sides** declare obligations; include their interaction cases in the matrix.
* **Monitoring windows.** For live systems, define **Γ\_time policies** (e.g., rolling 30 d) and tie alerts to **kind‑aware metrics** (“error rate per `ServiceInstance`”).

**LA‑obligations (normative):**

* **LA‑1.** Each test campaign **SHALL** specify **rows/columns** in the evidence matrix and attach **Scope/MemberOf** predicates to each run.
* **LA‑2.** Freshness windows **SHALL** be explicit and enforced in guards (no “latest”).
* ***LA‑3.** If a **KindBridge** merges subkinds, test plans **SHALL** be adjusted (more cells, stricter acceptance), and the **kind‑bridge penalty** (based on CL^k) applied to **R**.
* **LA‑4.** Publishing **SpanUnion** coverage requires the independence note (which support lines differ).

**Mini‑example (LA).**
Claim: “For all `x ∈ Vehicle`: brakeDistance ≤ 50 m on dry, ≤ 40 m on wet.”
— **Rows**: `{PassengerCar, LightTruck}`.
— **Columns**: `{dry, ≤50}`, `{wet, ≤40}` with rigs and versions.
— **Cells**: PC/dry covered by track tests; LT/wet by simulation + surrogate tests (independent lines → SpanUnion allowed).
— **Bridge** to jurisdiction Y collapses EV vs ICE ⇒ `CL^k=2`. Apply **Ψ(2)** to **R**; add extra wet tests to compensate.

---

#### B.6 TA lane — tool qualification where it belongs  \[A/I]

**What TA contributes.** Confidence in **provers, checkers, model‑checkers, data classifiers** and pipelines. TA is about the **machinery**, not the **claim** or **kind** semantics.

**TA‑patterns (informative):**

* **Prover kernels.** Audit/qualification of the kernel version used for VA proofs.
* **Automated Model‑checkers.** Qualification against seeded faults; document limits (precision, nondeterminism).
* **Classifiers used for `MemberOf`.** If membership uses ML or rules engines, qualify the **classifier** separately; any drift monitoring belongs to LA freshness.

**TA‑obligations (normative):**

* **TA‑1.** Tools critical to VA/LA **SHALL** declare their qualification status and version; guards **SHALL** reference these declarations when they matter.
**TA‑2.** Lower tool qualification **MUST NOT** be hidden by relaxing **F** or widening **G**. target‑contexts may offset it by demanding **more evidence** in **R** (for example, extra tests), per policy.

---

#### B.7 Guard macros for evidence planning & attachment  \[A]

**Guard\_EvidencePlan\_Typed** — approve a plan that is adequate for a typed claim.
*Plain reading.* The first macro checks that the plan names the rows (kinds or masks) and columns (slices), that scope and membership can be checked for each cell, that any Cross‑context moves declare bridges, and that penalties are budgeted in **R**.

```
1. MatrixDeclared:    Evidence matrix rows = {subkinds or masks of k}; columns = {TargetSlices within ClaimScope}
2. ScopeBound:        For each column, ClaimScope covers that slice with explicit Γ_time
3. KindBound:         MemberOf(?, k, slice) is defined (deterministic) for all planned slices
4. BridgeBudgeted:    If cross-context:
                        (a) Scope Bridge(s) declared with CL → attach the **scope‑bridge penalty** to the **R** budget
                        (b) KindBridge(s) declared with CL^k → attach the **kind‑bridge penalty** to the **R** budget
5. FreshnessPolicy:   LA freshness windows specified per slice; monitoring plan defined (if live)
6. IndependenceNote:  If SpanUnion is claimed, independence justification attached
7. TADecls:           Tools and their TA status listed; residual risk routed to R (not to F/G)
```

**Guard\_EvidenceAttach\_Typed** — attach concrete evidence to a state change.
*Plain reading.* The second macro checks that each attached evidence unit clearly states which row and column it covers, binds scope and membership in a reproducible way, applies bridge penalties to **R**, and respects freshness.

```
1. CellMatch:         Each evidence unit cites (subkind/mask, slice) it covers
2. PredicateBinding:  Evidence embeds Scope and MemberOf predicates (or references them verifiably)
3. BridgeApplied:     If evidence is bridged, apply the **scope‑bridge** and/or **kind‑bridge** penalties to **R**; record loss notes
4. FreshnessMet:      Evidence within declared freshness; else guard fails closed
5. VA/LA Mix:         If VA present, verify it matches the quantified Kind; if LA fills gaps, show matrix deltas
6. TAConsistent:      Tool versions match TA declarations used at planning time
```

---

#### B.8 Anti‑patterns & remedies  \[I]

| Anti‑pattern                       | Why it’s risky                                | Remedy                                                              |
| ---------------------------------- | --------------------------------------------- | ------------------------------------------------------------------- |
| “We tested one golden case.”       | Hides variant risk; ignores subkinds.         | Build a subkind‑indexed matrix; add boundary tests per column.      |
| “Latest data suffices.”            | Non‑deterministic; un‑auditable.              | Declare `Γ_time` windows; fail closed on expiry.                    |
| “Tool is trusted, so we’re done.”  | Confuses TA with VA/LA; misses content risk.  | Keep TA separate; add VA proofs or LA tests as needed.              |
| Bridging without penalties         | Understates risk; mapping gaps surface later  | Apply **scope‑bridge** and **kind‑bridge** penalties to **R**; publish loss notes. |
| Widening G to cover evidence gaps. | Conflates applicability with available tests. | Keep G honest; expand matrix or lower claim scope explicitly (ΔG−). |
| Inferring scope from how many items match    | Scope is not the same as membership      | Keep **Scope** (where it applies) distinct from **membership** (which items match in the slice). |


---

#### B.9 End‑to‑end example (manager’s cheat‑sheet)  \[I]

**Scenario.** You want to publish “∀ x: PassengerCar. brakeDistance ≤ 50 m dry; ≤ 40 m wet” across two plants.

1. **Kinds.** `PassengerCar ⊑ Vehicle` (K2, signature F4).
2. **Scope (G).** `{surface in {dry, wet}, speed limits, rig version, time selector (Γ_time)=rolling 180 days}` in Plant‑A.
3. **VA.** Prove the property for **PassengerCar** using a proof assistant, and cite the **Scope** slices it assumes.
4. **LA.** Build an evidence matrix with rows `{PassengerCar}` and columns `{dry, up to 50}` and `{wet, up to 40}`, including rig variants; add boundary tests near the limits.
5. **TA.** Qualify the prover kernel and the automated checker used for wet surrogates.
6. **Bridge.** To Plant‑B: a **Scope Bridge** with **CL=2** (rig bias) and a **KindBridge** with **CL^k=3** (same classification).
7. **Penalties.** Apply the **scope‑bridge penalty** for CL=2 and the **kind‑bridge penalty** for CL^k=3 to **R**. Per policy, add extra test cells in Plant‑B to compensate for rig bias.
8. **Guards.** Use `Guard_EvidenceAttach_Typed` on the state change; include freshness checks.

**Outcome.** A defensible, auditable publication: typed, scoped, with clear evidence coverage and explicit risk penalties — no conflation of abstraction with applicability, and no tool risk smuggled into content.

### Annex C. ESG guards

**Status note.** This profile restates the guard semantics from **§4** for ESG/Method contexts. It does **not** add obligations; where wording diverges, **§4 controls**.

#### C.1 **ESG** guard obligations (normative)

When a state transition publishes or affirms a claim that quantifies over kinds, the guard **SHALL**:

1. **Scope coverage (USM).**
   `U.ClaimScope(Claim) covers TargetSlice` (singleton or finite set) and TargetSlice **declares `Γ_time`** (no “latest”).

2. **Typed definedness.**
   A **deterministic membership check** is available for every kind used by the claim in the **TargetSlice**. If membership cannot be evaluated in that context, the guard **fails closed**.

3. **Typed compatibility (same Context).**
 If a downstream consumer expects a specific kind, then for each kind used by the claim either:
* the used kind is an **is‑a / subkind‑of** the expected kind, or
* a documented **RoleMask** for the expected kind is used and its constraints are **met and observable** in the **TargetSlice**.

3. **Typed compatibility (Cross‑context).**
  If any referenced kind is **used across Contexts**, a **KindBridge** **SHALL** be declared with a published **type‑congruence level** (minimum acceptable level per Context policy), order preserved (no inversions), and **loss notes**.  
The guard **SHALL** apply the **kind‑bridge penalty** to **R**.

4. **Scope translation (Cross‑context claim use).**
If the Claim’s scope originates in another target‑context, a **Scope Bridge** with a published **congruence level** is required; apply the **scope‑bridge penalty** to **R**.

6. **Formality threshold (if gated).**
   If the ESG state requires rigor, enforce `U.Formality(Claim) ≥ F_k` (C.2.3).
   (*Note:* Raising F does **not** widen G; do not substitute.)

7. **Evidence freshness (R).**
   Where the new state implies trust, assert freshness windows and confirm **no expired bindings**.

**Prohibitions (normative).**

* Do **not** widen **G** to “hide” a type mismatch. Fix typed compatibility (introduce a subkind, use a RoleMask, publish a KindBridge) or reject.
* Do **not** treat a **mask name** as a kind—masks must be **registered** and **deterministic**.
* Do **not** infer G from the size of a kind’s **Extension**; **Scope ≠ Extension**.

---

#### C.2 · **Method–Work** guard obligations (normative)

To admit a **capability** for a specific **Work** step at **JobSlice**, the guard **SHALL**:

1. **Work scope coverage (USM).**
   The capability’s **Work scope** covers the **JobSlice**, and the **JobSlice** includes an explicit **time selector (Γ_time)**.


2. **Measures & qualification.**
   **All** required `U.WorkMeasures` hold at JobSlice and the `U.QualificationWindow` is **valid at `Γ_time`**.

3. **Typed inputs (same Context).**
   For each declared input kind (or RoleMask), assert:
   * **Membership check available:** the system can deterministically decide whether the input belongs to the expected kind in this **JobSlice**.
   * **Compatibility:** the provided input kind is an **is‑a / subkind‑of** the expected kind, or the **RoleMask** constraints are satisfied and observable.

3. **Typed outputs / post‑conditions (if declared).**
   If the capability guarantees an output kind `k_out`, record the obligation to **demonstrate** `MemberOf(output, k_out, JobSlice)` (typically via conformance tests or audits).

4. **Cross‑context typed use.**
   If inputs/outputs are typed in a different target‑context than the capability or JobSlice:
   * **KindBridge(s)** are required with a published **type‑congruence level** and **loss notes**; apply the **kind‑bridge penalty** to **R**.
   * If the capability resides in another target‑context, a **Scope Bridge** with a published **congruence level** is required; apply the **scope‑bridge penalty** to **R**.

4. **No substitution by G.**
   Do not “fix” a typed mismatch by widening the **Work scope**. Use an **adapter** or a **RoleMask**, or reject.

---

#### C.3 · Guard macros (ready‑to‑use)

**ESG\_TypedGate(Claim, TargetSlice, Kinds, thresholds)**
*Manager view:* The following macros are for editors; target‑contexts may automate them if desired. Managers can read the comments on each step; the checks are the same ones described in Plain language above.

```
1  assert ClaimScope(Claim) covers TargetSlice                 // USM
2  assert Γ_time(TargetSlice) is explicit                  // no "latest"
3  for each kind k in Kinds used by Claim:
4      assert membership_defined(k, TargetSlice)               // C.3.2 K-07
5  if same-Context typed expectations exist:
6      assert is_subkind(k, k_expected) OR meets_mask_constraints(k_expected, TargetSlice)
7  if cross-context kinds:
8      assert KindBridge(k, k') with type_congruence ≥ c_kind and loss notes
9      apply_kind_bridge_penalty(type_congruence)
10 if cross-context scope:
11     assert ScopeBridge(Claim.Context, TargetSlice.Context) with congruence ≥ c_scope
12     apply_scope_bridge_penalty(congruence)
13 if F-threshold applies: assert Formality(Claim) ≥ F_k        // C.2.3
14 if trust implied: assert Fresh(evidence, window) AND NoExpiredBindings
```

**MethodWork\_TypedGate(Capability, JobSlice, Inputs/Outputs, thresholds)**

```
1  assert WorkScope(Capability) covers JobSlice                // USM
2  assert Γ_time(JobSlice) is explicit
3  assert WorkMeasures(JobSlice) satisfied AND QualificationWindow holds
4  for each expected input-kind k_in:
5      assert membership_defined(k_in, JobSlice)
6      assert is_subkind(k_input, k_in) OR meets_mask_constraints(k_in, JobSlice)
7  if declared output-kind k_out: record obligation to show MemberOf(output,k_out,JobSlice)
8  if cross-context kinds: assert KindBridge(...) with type_congruence ≥ c_kind; apply_kind_bridge_penalty(type_congruence)
9  if cross-context capability/scope: assert ScopeBridge(...) with congruence ≥ c_scope; apply_scope_bridge_penalty(congruence)
```

#### C.4 · Worked examples (manager‑focused)

**(A) ESG — Promote a braking policy to *Effective*.**
*Claim.* “For all **vehicles**: braking distance is **≤ 50 m** on dry and **≤ 40 m** on wet.”
*TargetSlice.* `{surface∈{dry,wet}, speed≤50 km/h, rig=v3, Γ_time=rolling 180 d}`
*Kinds.* `Vehicle` (K2, `KindSignature` at F4); the consumer subsystem expects `PassengerCar`.
**Guard.**

1. **Scope** covers TargetSlice (USM ✓).
2. **Definedness** of `MemberOf(?, Vehicle, TargetSlice)` ✓.
3. **Typed compatibility:** `PassengerCar ⊑ Vehicle` ✓.
4. **No bridges** → no penalties.
5. **F‑threshold:** `Formality(Claim) ≥ F4` ✓.
6. **Freshness:** evidence ≤ 180 days ✓.
   **Result:** Transition allowed. F/R apply weakest‑link on support paths; G remains the set declared.

---

**(B) Method–Work — Admit “RiskScore” step with typed input.**
*Capability.* `ComputeRiskScore` expects `AuthenticatedRequest`; promises SLOs (latency ≤ 50 ms, error ≤ 0.5 %).
*JobSlice.* `{api=v2.3, region=eu‑west, Γ_time=now, traffic_class=gold}`
*Inputs.* Producer emits `Request` (no auth guarantee).
**Guard.**

1. **Work scope** covers JobSlice; **Measures** & **QualificationWindow** ✓.
2. **Typed inputs:** `MemberOf(?, AuthenticatedRequest, JobSlice)` must hold. Not true for raw `Request`.
3. **Remedy:** insert an **adapter** that enforces/attests auth → yields `AuthenticatedRequest`.
4. **No Cross‑context** → no bridges.
   **Result:** Admitted **with adapter**; Scope unchanged; R relies on adapter evidence. Widening Work scope is **not** acceptable to bypass typed mismatch.

---

**(C) Cross‑context ESG — Adopt policy across plants.**
*Claim Context.* `SafetyLab@2026`. *target Context.* `PlantB@EU`.
*Kinds.* `Vehicle ↦ TransportUnit` via **KindBridge** with **`CL^k=2`** (EV/ICE collapsed); **Scope Bridge** from lab to plant with **CL=2** (rig bias ±2 %).
**Guard.**

1. Translate **Scope** and **cover** `TargetSlice_B`.
2. Translate **Kind** and ensure `MemberOf(?, TransportUnit, TargetSlice_B)` is **defined**.
3. Apply the **scope‑bridge penalty (level 2)** and the **kind‑bridge penalty (level 2)** to **R**; publish loss notes.
   **Result:** Transition allowed with reduced **R**; G is the **mapped** set; F unchanged.

---

#### C5 · Anti‑patterns & remedies (normative where noted)

| Anti‑pattern                                      | Why it’s wrong                                 | Remedy                                                                              |
| ------------------------------------------------- | ---------------------------------------------- | ----------------------------------------------------------------------------------- |
| Widening **G** to “make kinds match”              | Conflates **describedEntity** with **applicability** | Introduce **subkind**, **RoleMask**, or **KindBridge**; keep G honest.              |
| Using a **mask name** as a kind                   | Hides constraints; breaks determinism          | Register mask; ensure constraints are observable; promote to **subkind** if reused. |
| Ignoring **`CL^k`** when classifying across Contexts | Under‑counts risk                              | Require **KindBridge**; apply **Ψ(`CL^k`)** to **R**; record loss notes.            |
| Inferring **Scope** from the size of the **Extension** | Scope is not the same as Extension            | Keep **Scope** (where it applies) distinct from **Extension** (which items count in the slice). |
| Implicit “**latest**” time                        | Non‑deterministic guard                        | Require explicit **`Γ_time`** (point/window/policy).                                |

---

# **C.13 — Compose‑CAL (Constructional Mereology)**
*(architheory pattern; structural rung of the FPF ladder)*
**Status.** Normative architheory \[A]; notation‑agnostic; imports Kernel only.

### 1 Intent

Provide a single, generative calculus for part–whole structure so that **all** structural relations in FPF are *constructed* (not merely declared) from three primitives and thereby inherit extensional identity by design. The calculus is hidden from day‑to‑day users behind relation aliases; its artefacts are traces that witness how a whole arises from its parts.

Also known as *“Γₘ mereology”*, *“constructor‑based composition”*.

**Layer.** *calculus.*
**Depends on.** Kernel only (no upward imports).
**Consumed by.** CT2R‑LOG (B.3.5) Working‑Model alias logic and any architheory that needs part–whole semantics. Compose‑CAL does **not** import alias definitions; it merely emits traces that others may reference.

Compose‑CAL introduces a **single construction operator Γₘ** with exactly three constructors—**sum**, **set**, **slice**—sufficient to build structural wholes, collections‑as‑wholes, and aspects **without** extending the Kernel’s type set. No “parallel” or “temporal slice” constructor is added. Every construction yields a **trace** that serves as the witness for structure. Human‑facing relations such as *ComponentOf*, *MemberOf*, *AspectOf* are defined elsewhere as **Working‑Model aliases** and are *grounded* in these traces; Compose‑CAL itself remains purely generative and extensional.


### 2 Problem frame & Problem

FPF presents a unified structural backbone used across disciplines. Historically, sub‑relations like *ComponentOf* or *MemberOf* were **declared** directly. This maximised usability but provided no generative guarantee that a new subtype was extensionally well‑behaved or reducible to common mereology.

Declared lists of part‑of sub‑relations **scale poorly** and **lack identity guarantees**. Engineers ask for a *single dial* (“is x part of y?”), while ontologists need a principled foundation that (a) avoids Kernel bloat and (b) proves that wholes are nothing over and above their parts. Adding yet another bespoke relation (e.g., *PortionOf*) should not entail schema surgery or ad‑hoc rules.

### 3 Forces

* **Parsimony (C‑5).** Add no core types if composition suffices; keep the constructor set minimal.
* **Minimal Kernel (P‑1).** Generativity must live in a plug‑in calculus, not in Kernel axioms.
* **Cognitive asymmetry.** Everyday users want “one part‑of query”; specialists accept complexity backstage.
* **Trans‑disciplinary unification.** Every architheory that needs mereology should reuse one *generative* basis.
* **Green‑field strictness.** With no legacy to break, we can require grounding for new structural edges.

## 4 Solution

### 4.1 Solution sketch

**Compose‑CAL SHALL provide Γₘ with three and only three constructors:**
1. **`Γₘ.sum(parts:Set[U.Entity])`** — returns a whole *W* such that each *p* in *parts* stands in **KernelPartOf(p, W)**.
2. **`Γₘ.set(elems:Set[U.Entity])`** — returns a **collection** *C*; each *e* in *elems* stands in a calculus‑internal **mero:KernelPartOf(e, C)** under **member‑as‑part** semantics (publication alias: typically **`ut:MemberOf`**). **Counts/order** (e.g., parallel/serial factors) are **not carried here**; they live in method/time families adjacent to structure.  *Note:* although `mero:KernelPartOf` is transitive in the calculus, the **published** `MemberOf` alias remains **non‑transitive** by design (see A.14 guards). 
3. **`Γₘ.slice(entity:U.Entity, facet:U.Facet)`** — returns an **aspect** *S* such that **mero:KernelPartOf(S, entity)** and *S* carries the declared **facet**. Temporal facets are excluded here.
   
+**Note.** The calculus names an internal backbone **`mero:KernelPartOf`**; the Kernel’s public `ut:PartOf`/**A.14** catalogue remain unchanged. Publish only via Working‑Model aliases (CT2R‑LOG).

+The calculus emits a **trace** for every construction; Structural aliases **MUST** be *grounded by* exactly one such trace.

**Non‑goals (clarifications).**
* No extra constructors for “parallelism” or “time slices”; parallelism is modelled via **set** (with order handled in `Γ_method`), and temporal parts live in the appropriate temporal/system calculus. This preserves parsimony.
* Compose‑CAL does not define user‑visible relation names; those belong to the alias layer.

### 4.2 Normative Standard (high‑level)

* **C13‑N1.** *Extensional identity.* Two Γₘ results are identical iff they have the same parts under the same constructor and facet conditions.
* **C13-N2.** *Structural grounding stance.* Every **structural** edge **MUST** reference **exactly one** Γₘ trace as its grounding witness **and SHALL declare `validationMode = axiomatic`** (see B.3.5 / E.14). **Structural edges MUST NOT** be published in `postulate` or `inferential` stances.
* **C13‑N3.** *Algebraic laws.* `Γₘ.sum` and `Γₘ.set` are **commutative** and **idempotent** over their inputs; `Γₘ.slice` composes only by facet‑compatible refinement.
* **C13‑N4.** *Acyclicity & antisymmetry.* Structural part‑of induced by Γₘ is transitive, antisymmetric, and acyclic at the level of entities. *(Formal axioms appear later in this pattern.)*
* **C13‑N5.** *Separation of concerns.* Γₘ provides constructions and traces; naming, aliasing and human‑level relation taxonomies are defined outside Compose‑CAL (see B.3.5 for the CT2R‑LOG handshake).
* **C13‑N6.** *Member vs component.* `Γₘ.set` yields **collections** whose Working‑Model alias is **MemberOf**; authors **SHALL NOT** infer **ComponentOf** from **MemberOf** without a separate `Γₘ.sum` narrative.
* **C13‑N7.** *Domain guard.* Do **not** apply Compose‑CAL to roles, methods, or works (see A.12/A.15): these are outside mereology.

### 4.3 Scope, applicability, terms & notation

+Use Compose-CAL whenever a claim concerns **structural containment** of entities (assemblies, collections, aspects). Compose-CAL is *not* used for epistemic relations between knowledge artefacts; those are **epistemic** relations and may be justified by **Logical/Mapping** and/or **Empirical Validation** with an explicit `validationMode ∈ {inferential, postulate}`. Compose-CAL is neutral with respect to domain (mechanical, biological, software, etc.).

* **Γₘ** — the mereological construction operator of this calculus.
* **trace** — a minimal, inspectable witness that a constructor was applied to given inputs to yield a whole (or aspect).
* **structural part‑of** — the structural relation induced by Γₘ; user‑facing aliases (e.g., *ComponentOf*, *MemberOf*) are separate patterns that **must** point back to traces.
  
 **Alias readiness.** Typical CT2R mappings:  
* **ComponentOf** ⇢ `sum` narrative;  
* **MemberOf** ⇢ `set` narrative;  
* **AspectOf** ⇢ `slice` narrative;  
* **PortionOf** ⇢ `slice(entity, facet="material/spatial‑region")` **plus** metrical semantics (A.14);  
* **ConstituentOf** (logical/content) ⇢ `sum` narrative over conceptual parts. *(Material mixtures are **not** `ConstituentOf`; use `PortionOf` or `ComponentOf` per A.14.)*
 
### 5 · Archetypal Grounding *(System / Episteme duo)*

> **Tell–Show–Show.** Compose‑CAL is a thinking‑level calculus for building structural wholes from parts. We *show* it twice—first on a **System** (structural) and then on an **Episteme** case (where constructive grounding is *not* the primary mode).

#### 5.1 · **System** (structural; constructive grounding)

**Story.** A **Skid** is assembled from its **Pump**, **Motor**, **Baseframe**, and **Manifold**.

**Constructive grounding (Γ\_m).**
Narrate a *sum* of parts: “Skid = sum{Pump, Motor, Baseframe, Manifold}.” This uses **`Γ_m.sum`** to obtain a whole whose parts stand in **KernelPartOf**; the resulting Working‑Model relation engineers publish is **`ut:ComponentOf`** on each edge from part to whole. The mapping “*sum → ComponentOf*” reflects the intended aliasing between constructive traces and human‑facing mereology.

**Facets and collections.** 
Need the **inspection surface**? Narrate **`Γₘ.slice(Skid, "spatial")`** and publish **`ut:AspectOf`**. Need a group of **Transfer interactions**? Narrate **`Γₘ.set{…}`** and publish **`ut:MemberOf`**—this is a **collection-as-whole**, not a sub‑assembly; no component identity is implied without a separate **`Γₘ.sum`** narrative.

**Plane separation.**
Assembly **order** and **time** are *not* encoded here: parallel lines and schedules live in method/time families and are described adjacent to, not inside, the part‑tree.

#### 5.2 · **Episteme** (knowledge‑bearing; non‑constructive first)

**Story.** A **Mass‑Flow Representation** is used to stand for a measured flow in a plant dataset.

**Grounding choice.** 
Here the Working‑Model relation (e.g., **RepresentationOf**) is **epistemic**. Authors typically justify it by *inferential* or *postulate* stances (argument or calibration cues), not by a mereological construction; constructive traces remain optional. This preserves the firewall between structure and knowledge claims while keeping a clear path to stronger assurance if the team later reframes part of the representation structurally (e.g., sets of interactions as a **`Γ_m.set`** for a flow bundle).

#### 5.3 · Scope justification

* **Universality.** The trio **sum / set / slice** appears across mechanical assemblies, biological complexes, and organizational artifacts; aliasing to **ComponentOf / MemberOf / AspectOf** provides a stable Working‑Model surface for those domains.
* **Parsimony.** No “parallel” or “temporal slice” constructor is added; time slices belong in the temporal calculus, and parallelism is modelled as a **set** plus method metadata.

### 6 · Bias‑Annotation *(cognitive anti‑patterns and counter‑moves)*

| Bias (name)                       | Symptom                                                                                                         | Counter‑move (conceptual)                                                                                                    | Where to look                               |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| **Constructor‑centrism**          | Treating the trace as “the real thing” and the Working‑Model edge (e.g., **ComponentOf**) as merely decorative. | Re‑affirm **Working‑Model first** (publish in `ut:*Of`), then attach constructive narratives only when assurance demands it. | B.3.5 (Working‑Model relations & grounding) |
| **Collection ↔ Composition swap** | Using **MemberOf** to stand in for **PartOf**, then inferring structural identity.                              | Keep **set** outputs as *collections*; use **sum** for wholes with extensional identity.                                     | A.14 (Advanced Mereology)                   |
| **Temporal leakage**              | Smuggling sequence/phase into part‑trees.                                                                       | Route order/time to their planes; **no** “temporal slice” constructor in Compose‑CAL.                                        | B.1.\* (Γ\_method / Γ\_time)                |
| **Over‑slicing**                  | Multiplying aspects until identity becomes opaque.                                                              | Declare the **facet** explicitly; stop when aspects no longer aid recognition of the same whole.                             | A.14 (Aspect/Phase distinction)             |
| **Feature creep**                 | Proposing a new constructor for a special case.                                                                 | Reduce to **sum / set / slice**; if reduction fails across ≥ 3 domains, reconsider the modelling plane before adding power.  | C‑5 (Parsimony)                             |
| **Axiomatic inflation**           | Demanding constructive traces for epistemic links by default.                                                   | Use *inferential* / *postulate* where appropriate; reserve *axiomatic* for structural identity.                              | B.3.5 (validation modes)                    |

---

### 7 · Conformance Checklist *(normative, calculus‑level)*

The following regulate **how to think and write** when invoking Compose‑CAL. They are notation‑agnostic and conceptual.

| ID                                         | Requirement                                                                                                                                                                                    | Purpose                                                                 |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **CC‑C13‑1 (Three moves only).**           | Authors **SHALL** construct structural narratives using exactly **`Γ_m.sum`**, **`Γ_m.set`**, and **`Γ_m.slice`**. No additional constructors are introduced in this calculus.                 | Preserve **parsimony** and cross‑domain comparability.                  |
| **CC‑C13‑2 (Kernel invariants).**          | Constructive narratives **SHALL** respect **KernelPartOf** invariants (transitivity, antisymmetry, acyclicity) and yield extensional identity for wholes.                                      | Keep structural identity intelligible and replayable.                   |
| **CC‑C13‑3 (Algebraic laws).**        | `sum`/`set` are commutative & idempotent; `slice` composes only with facet‑compatible refinement. | Make traces **peer‑reconstructible** and easy to replay in thought. |
| **CC‑C13‑4 (No order/time in mereology).** | Authors **SHALL NOT** encode execution order, parallelism, or temporal coverage via constructors; such concerns belong to method/time planes and are stated adjacent to structure.             | Maintain the plane firewall.                                            |
| **CC‑C13‑5 (Narratability).**              | Each constructive trace **SHALL** be narratable in plain language **without introducing new primitives**.                                                                                      | Enforce human‑first clarity; uphold C‑5.                                |
| **CC‑C13‑6 (Alias alignment).**            | When Publishing Working‑Model relations for structural content, authors **SHOULD** align “sum→ComponentOf”, “set→MemberOf (or pattern‑specific)”, “slice→AspectOf” in their explanatory prose. | Keep alias semantics stable across Contexts.                               |
| **CC-C13-7 (CT2R-LOG handshake).**     | For every **structural** edge on the Working-Model, authors **SHALL** set `validationMode=axiomatic` and point **`tv:groundedBy`** to exactly **one** Γₘ trace (`sum|set|slice`). *Legacy “Tier-1” wording deprecated; express formality via **F** per C.2.3.* | Clean bridge to the Working-Model alias layer; decouples relation kind from legacy “tiers”. |
| **CC‑C13‑8 (Member ≠ Component).**         | A **set** output remains a *collection*; authors **SHALL NOT** infer **ComponentOf** from **MemberOf**. When an integrated assembly is intended, provide a separate **`Γ_m.sum`** narrative.   | Prevent membership→component conflation.                                 |
| **CC‑C13‑9 (Facet explicitness).**         | **Slice** narratives **SHALL** name the **facet** used; temporal facets are excluded (handled elsewhere).                                                                                      | Keep aspects precise and non‑temporal.                                  |
| **CC‑C13‑10 (No roles in mereology).** | Do not apply Γₘ to `U.Role`, `U.Method`, or `U.Work`; these are outside mereology (A.12/A.15). | Preserve the plane firewall. |
| **CC‑C13‑11 (Member non‑transitive).** | When publishing `MemberOf`, do not rely on transitive closure across collection‑of‑collections; surface semantics remain non‑transitive per A.14. | Prevent Member→Component drift. |

> **Author’s note.** Compose‑CAL is a calculus for **constructive** reasoning about structure. Publishing remains in the **Working‑Model** layer (see B.3.5); constructive narratives are attached when the team seeks stronger assurance, never as a substitute for clear human‑facing relations.

### 8 · Consequences

**Benefits**

 * **Extensional clarity.** Every structural claim is reconstructed from `Γ_m.sum | Γ_m.set | Γ_m.slice`: **sum** establishes component‑assembly identity; **set** establishes collection identity; **slice** yields aspects as parts—without expanding the Kernel.
* **Human–first publication, formal–on‑demand.** Teams keep publishing **Working‑Model** relations (e.g., `ut:ComponentOf`), while **assurance** is attached as needed via a constructive grounding narrative and `tv:groundedBy` (see B.3.5).
* **Separation of planes preserved.** Order/parallelism and temporal coverage remain in `Γ_method` / `Γ_time`; structure is never overloaded to carry them, avoiding recurrent category errors.
* **Uniformity across domains.** The same triad models mechanical assemblies, socio‑technical memberships, and informational wholes without domain‑specific constructors or ad‑hoc exceptions.
* **Didactic economy.** Authors learn one compact calculus; reviewers gain a predictable place to look for constructive justification when `validationMode = axiomatic` (B.3.5 alignment).
* **Compositional reuse.** Traces are reusable fragments of reasoning; complex wholes are narratable as sums of sub‑traces, with sets for concurrency and slices for aspect selection.

**Trade‑offs / Mitigations**

* **Discipline cost at higher assurance.** Writing a concise grounding narrative for axiomatic claims takes effort. *Mitigation:* reuse the micro‑templates in this pattern’s Grounding section and keep narratives notation‑free.
* **Over‑use risk.** Temptation to treat collections as integrated assemblies. *Mitigation:* keep **MemberOf** distinct from **ComponentOf**; both `set` and `sum` yield wholes, but only **`sum`** establishes **component** structure and assembly identity.
* **Temporal leakage risk.** Authors may try to smuggle time into structure via “temporal slices.” *Mitigation:* use `Γ_time` for temporal statements and `slice` only for intensional aspects, not for time windows.

> **One‑line takeaway.** Compose‑CAL gives a minimal, universal *how‑it‑was‑built* story for any structural edge, without disturbing the human‑first publication surface defined in B.3.5.

---

### 9 · Rationale (informative)

**Why exactly three moves?**
`sum`, `set`, and `slice` are jointly sufficient and minimally overlapping:

* **`sum`** creates an **integrated whole** from parts and thereby establishes **component** structure (assembly identity).
* **`set`** creates a **collection‑as‑whole**; members are **parts of the collection** under member‑as‑part semantics, but **no component integration** is implied.
* **`slice`** returns an **aspect as part** of its bearer (facet‑constrained, e.g., spatial/material); temporal facets are excluded here.

All three moves create new entities; **sum** is the only move that establishes **component** identity. Neither `set` nor `slice` changes the identity of their inputs, and `set` never upgrades membership to component status. Temporal coverage and workflow order are handled in their own planes.

This separation mirrors long‑standing distinctions between composition, collection, and aspect, while enforcing **parsimony**: no additional constructors are introduced into the Kernel (C‑5). The calculus remains **notation‑agnostic**: its meanings are given in prose and mathematics; any diagrams are illustrative only, in line with the Notational‑Independence guard‑rail (E.5).

**Why constructive grounding lives outside the publication surface.**
FPF privileges **Working‑Model** relations as the canonical form for communication and design. Compose‑CAL supplies the **constructive shoulder** of the **Assurance Layer**: when authors choose `validationMode = axiomatic`, they narrate the whole as a `sum` of parts (with optional `set` and `slice` scaffolding) and point to that narrative via `tv:groundedBy`. This keeps the text readable while preserving a path to stronger assurance (B.3 family, Authoring Template).

**Why order/time are out of scope.**
Correctness‑by‑sequence and temporal coverage are orthogonal to **parthood**. Encoding them as parts breeds contradictions (e.g., “phase‑as‑component”). Compose‑CAL deliberately refuses any “serial/parallel/temporal constructor,” delegating such concerns to `Γ_method` and `Γ_time` and aligning with B.1’s flavour separation.

---

### 10 · Relations

**Builds on**

* **A.14 Advanced Mereology.** Uses its structural catalogue (Component/Portion/Aspect vs Member) as the *target* of constructive narratives; never collapses Member into Part.
* **E.5 Guard‑Rails (Notational Independence).** Meanings are given in prose; diagrams are illustrative only.  
* **E.5 Guard‑Rails (Unidirectional Dependency).** Compose‑CAL depends **downward** only; it never imports alias layers or higher planes.
* **E.8 Authoring Conventions.** Conforms to the canonical pattern template (Grounding section for `[A]` patterns; CC placement).

**Coordinates with**
* **B.3.5 CT2R‑LOG.** `tv:groundedBy` refers (conceptually) to Compose‑CAL traces when `validationMode = axiomatic`; **Working‑Model** relations remain the publication interface.
* **B.1 flavours.** Keeps order (`Γ_method`) and time (`Γ_time`) outside structure; may co‑appear in narratives when relevant but never as constructors.
* **Kind-CAL / Lang‑CHR.** Provide the Mapping shoulder of assurance (labels, type alignment) that complements constructive narratives in this pattern.
* **KD‑CAL.** Provides the Logical shoulder when authors justify relations inferentially instead of constructively.
* **C.16 (Measurement substrate).** Supplies quantitative hooks when a constructive narrative benefits from explicit counts/ratios (e.g., cardinalities, coverage), while keeping metrics distinct from mereology.

**Constrains**
* Any architheory that **creates** or **reasons about** structural wholes SHOULD narrate them using only `sum | set | slice`.
* Structural publication MUST NOT encode order/time; such claims belong to their dedicated flavours.
* Introducing new structural constructors requires a separate parsimony argument and is discouraged unless the triad cannot narrate the case without ambiguity.

**Provides**
* A minimal generative basis (`Γ_m.sum | Γ_m.set | Γ_m.slice`) and the corresponding reading discipline for constructive narratives.
* A stable interface with CT2R‑LOG for `tv:groundedBy` links under `validationMode = axiomatic`.


# C.16 (MM‑CHR) — Measurement & Metrics Characterization (Architheory)  \[A]

## 1 · Intent (Normative)

**Name.** *Measurement & Metrics Characterization (MM‑CHR).* This is user-oriented name: in user‑facing narrative we say ‘metrics’; in Tech register we speak `U.DHCMethodRef`/`U.Measure`.
**Intent.** Provide a **transdisciplinary substrate for measurement** that any architheory can rely on: a small, stable set of intensional constructs and relations—**`U.DHCMethodRef`**, **`U.Measure`**, **`U.Unit`**, **`U.EvidenceStub`**—disciplined by **CSLC** (*Characteristic / Scale / Level / Coordinate*) so that every recorded value is **interpretable** and **comparable** across CG‑frames (physics lab time‑of‑flight, figure‑skating judging, architectural modularity, etc.). **C.16** does **not** re‑define **Characteristic** (A.17) nor the CSLC kernel Standard (A.18); instead, it **exports** the measurement substrate that *binds* an architheory’s metric notions to **one Characteristic and one Scale** and frames a **conceptual link to evidence**. This characterization is **notation‑neutral**, **tool‑agnostic**, and **open‑ended** (no “lifecycle” narrative; evolution proceeds via **RSG** moves with checklists). 

**Outcomes.**
(1) A uniform way for architheories to *declare* what is measured and *read* what has been measured; (2) explicit **Characteristic anchoring** and **Scale typing** per CSLC; (3) principled **comparability** and **polarity** (declared at the template level); (4) **traceability** via conceptual evidence stubs; (5) seamless alignment with cross‑domain quantity notions (ISO 80000, ISO/IEC 25024, QUDT, SOSA/SSN, Verspoor) through Unification rows (Part F). 

## 2 · Scope & Status (Normative)

**Scope.** **C.16** specifies the **measurement substrate** for FPF architheories: the roles of `U.DHCMethodRef`, `U.Measure`, `U.Unit`, `U.EvidenceStub`; their **CSLC discipline**; the notions of **Scale type**, **polarity**, **comparability**, and **evidence sufficiency** at the level of *conceptual conditions*. It **exports** these constructs for all architheories (KD‑CAL, Arch‑CAL, etc.) without prescribing domain formulae or procedures. 

**Status.** **Normative architheory.** C.16 **depends on** A.17 (canonical **Characteristic**) and A.18 (minimal **CSLC** in Kernel). Where C.16 cites external CG‑frames, the stance is through **Part F** rows and **Bridges** (with CL and loss notes), not by vocabulary import. 

**Out of scope.** No computational recipes, no workflow prescriptions, no governance/process guidance. C.16 concerns **objects of thought** (intensions) and their **validity conditions**, not records or tooling. (Implementation guidance, if any, belongs outside Part C.)

---

## 3 · Problem & Context (Informative)

### 3.1 The problem C.16 solves

Across architheories, people say “score”, “metric”, “rating”, “property”. Without a shared substrate, numbers drift: *42 of what? on which scale? comparable to whom?* C.16 eliminates drift by requiring every metric notion to **bind** to **one** Characteristic and **one** Scale, and by **separating** intensional anchors from descriptions and gauges. The result is **portable meaning**: a measure is always readable as a **Coordinate on a declared Scale of a named Characteristic**, with a principled path to evidence. 

### 3.2 Context and prior art

* **Kernel canon.** A.17 makes **Characteristic** the sole canonical anchor for measurability; A.18 fixes **CSLC** as the minimal sufficiency for interpretability. C.16 relies on both.
* **Cross‑domain alignment.** The MM‑CHR family already maps FPF U.Types to **ISO 80000‑1 (Quantity)**, **ISO/IEC 25024 (Data‑quality Characteristic)**, **QUDT (QuantityKind/QuantityValue)**, **W3C SOSA/SSN (Observable/Observed/Result)**, and domain “feature/metric” usage (Verspoor, TF Metrics). C.16 uses these rows **as Bridges** (Part F), preserving local senses and documenting losses.  
* **Open‑ended evolution.** FPF replaces “lifecycle” with **Reachable‑States Graph (RSG)**: movement is along **certified states** with checklists; measurement work adopts the same open‑endedness (re‑entry allowed when distinctions change). C.16 uses RSG to frame **readiness** and **revision** of metric notions conceptually (no processes implied).

---

## 4 · Forces (Informative)

**F1 — Interpretability first.** A value detached from its Characteristic/Scale is meaningless; CSLC supplies minimum context.
**F2 — Transdisciplinarity.** Physics, architecture, curation, sport judging—*one* substrate must cover all while respecting scale types and polarity.
**F3 — Intension vs description.** Confusing the **Characteristic** (intensional object) with its rubric or exemplar text (descriptions) corrupts claims; C.16 keeps them distinct.
**F4 — Comparability without coercion.** Ordinal ≠ interval; ratio admits unit change, ordinal does not; polarity matters for “better/worse”. C.16 encodes these **as conceptual constraints**, not formulas.
**F5 — Evidence sufficiency.** A measure should be *checkable in principle*; evidence is a **conceptual link** (not storage advice).
**F6 — Lexical discipline.** One canon in normative register; narrative labels are didactic only (Part E). C.16 reuses E.10’s **register mapping**.

---

## 5 · Solution Outline (Normative)

**S1 — Exported objects.** C.16 **exports** four intensional constructs to be used by any architheory:

1. **`U.DHCMethodRef`** — the *binding* of **one `U.Characteristic`** to **one Scale form**, with declared **polarity** and a conceptual **compatibility claim** (what counts as “same‑scale” for comparison). It is an *intensional specification*, not a record layout.
2. **`U.Measure`** — an *assertion* that a **subject** occupies a **Coordinate** (or **Level**, if discrete) on that Scale; the measure **references** its template and carries a **conceptual pointer to evidence** (`U.EvidenceStub`).
3. **`U.Unit`** — the *unit kind* associated with the Scale where applicable (physical quantities, normalized “points”, “stars”, “%”); unit coherence is part of comparability conditions.
4. **`U.EvidenceStub`** — a *conceptual locator* of grounds for the asserted value (type, identifier, brief summary, optional integrity notion); sufficiency criteria are **conceptual** (see §9, later).

**S2 — Comparability stance.** C.16 states **conceptual comparability** conditions: *same Characteristic*, *compatible Scale type and parameters*, *unit coherence* for interval/ratio; **no** forced coercions for nominal/ordinal; any score‑producing gauge **must be monotone** w\.r.t. template polarity. (Details: §7–§8 in later parts.)

**S3 — Evidence stance.** A measure that, by its template, **requires** evidence, is **inadmissible** without a meaningful `U.EvidenceStub`. C.16 defines **what it means conceptually** for evidence to “connect” the subject, the Characteristic, and its symbolic description; mechanisms are out of scope. (Details: §9 in later parts.)

**S4 — RSG framing (open‑endedness).** Readiness, calibration, and revision of metric notions are expressed as **RSG node moves with checklists** (e.g., “characteristic anchored”, “Scale typed”, “Unit coherent”, “Gauge declared”), allowing **re‑entry** when distinctions change; there is no terminal “lifecycle”. (Details: §10, later.)

---

### 5.1 · Lexical Discipline & Registers (Normative)

**L1 — Canon.** Use **Characteristic / Scale / Level / Coordinate / Score / Unit / Gauge** in **Tech** register; their `U.*` counterparts in **Formal**; narrative labels (e.g., *axis*, *points*, *stars*) are **didactic only** at first‑mention mapped to canon (E.10). 
**L1‑bis — “metric”.** The noun *metric* is **not** a Tech‑register canonical token for measurables; use **Characteristic / Scale / Coordinate / Score / Gauge**. It **may** appear in the architheory title and in the Formal names `U.DHCMethodRef` / `U.Measure`. Do not use *metric* as a synonym for **Characteristic** or **Score** in normative prose.
**L2 — Intension vs Description.** Keep **intensional objects** (`U.DHCMethodRef`, `U.Characteristic`) distinct from **descriptions** (rubrics, exemplars) and from **claims** (`U.Measure`). No collapsing of names across these layers.
**L3 — No synonym sprawl.** In normative clauses do **not** substitute *dimension/axis/property/feature* for **Characteristic**; A.17 governs canonicalization. (C.16 inherits A.17’s rename policy.)
**L4 — Bridge‑only unification.** Cross‑vocabulary sameness appears only via **F.9 Bridges** with **CL** and **loss notes**; C.16’s lexicon is the *source* side for measurement rows.
**L5 — “Metric” in registers.** In **Tech/Formal** avoid the noun *metric* as a primitive; use `U.DHCMethodRef` / `U.Measure` / **Score**. In **Plain** register *metric* MAY denote “a Template+Measure family” on first mention, with an explicit pointer to canonical terms.

## 5.2 · Relations (pointers; details later)

**To A.17 / A.18.** C.16 *uses* A.17’s canonical **Characteristic** and A.18’s **CSLC sufficiency**; it neither re‑states nor weakens them.
**To Part F.** C.16 is the **exporting architheory** behind measurement rows in UTS/Bridges (e.g., **result‑value** ↔ SOSA `Result`, ISO `QuantityValue`).
**To Arch‑CAL.** Architectural qualities (*Coupling, Cohesion, Evolvability*) become **Characteristics** measured via C.16 templates; architectural dynamics read as trajectories in **CharacteristicSpace** (A.17 context).

## 5.3 · Normative Core Model (types & Standards)

> **Position.** MM‑CHR does **not** redefine kernel terms; it **binds** them to an architheory‑level Standard that every metric must satisfy. Canonical vocabulary and CSLC duties are inherited from **A.17**/**A.18** and referenced here without duplication.
> 
> **Source of Truth** A.17/A.18 are the sole sources of truth for Canon and CSLC; C.16 **adopts by reference** and **forbids restatements** of their definitions. C.16 only **exports** `U.*` constructs, comparability stance, evidence semantics, and RSG touch‑points.

### 5.3.1 `U.DHCMethod` — the metric definition (normative)

**Role.** An intensional **Standard** that fixes *what is measured* and *how values must be read*—without producing any values itself. It is a *Definition*, not a Measure. **References to this template in data use `U.DHCMethodRef`.**

**R‑MT‑1 (CSLC anchor).** A DHCMethod **SHALL** bind to **exactly one** `U.Characteristic` and **exactly one** **Scale‑form** admissible for that Characteristic (cf. A.18). Level is **optional** (used when the scale is enumerated); otherwise values are given directly as Coordinates.

**R‑MT‑2 (Unit).** If the scale carries units (interval/ratio), the template **SHALL** designate a **Unit** of presentation. For ordinal/nominal scales, unit may be absent or a nominal label (e.g., “stars”). (Old MM‑CHR Annex A already listed these structural elements; here we fix the conceptual obligation. )

**R‑MT‑3 (Polarity).** For any ordered scale, the template **SHALL** declare polarity (*higher‑is‑better / lower‑is‑better / target‑is‑best*), used by downstream gauges and comparisons (see §6). A **targeted** Scale **SHALL** declare at the Template: (a) the **target value**, (b) the **tolerance semantics** (e.g., symmetric band ±δ, or asymmetric bands), and (c) the **monotone fall‑off** convention outside the band. Any 𝒢 derived from a targeted Scale **MUST** be piecewise‑monotone toward the target and respect the declared tolerance semantics.

**R‑MT‑4 (Applicability).** A template **SHALL** state the **applicability frame** (what kinds of subjects it meaningfully applies to) in conceptual terms; this is a property of the definition, not of any measure.

**R‑MT‑5 (Intension vs description).** The template is an **intensional object**. Any rubric, checklist, or prose that explains it is a **Description**; they are related but not identical (E.10 discipline).

**R‑MT‑6 (Cardinality hint).** A Template **MAY** declare its intended **cardinality semantics** for a subject within a **time stance** (e.g., *latest‑only*, *at‑most‑one‑per‑day*, *time series*).
Where declared, claims outside that semantics are **inadmissible conceptually** (they must be reframed or versioned). *Purpose:* prevent silent duplicates and mixed regimes without imposing storage logic.

 **R‑MT‑7 (MAY):** “`UncertaintyPolicy` — optional conceptual guidance on how uncertainty is expressed/read (e.g., band/CI/quantile), without prescribing methods/tools.
    

### 5.3.2 `U.Measure` — the recorded reading (normative)

**Role.** A **claim** that a subject occupies a **Coordinate** (or named **Level**) on the template’s scale, backed by a minimal pointer to its grounds.

**R‑ME‑1 (Template binding).** Every Measure **SHALL** reference exactly one DHCMethodRef; its **Value/Coordinate** must be **valid** for that template’s scale (type, range, category).

**R‑ME‑2 (Subject).** A Measure **SHALL** identify its **subject‑of‑measurement** (the bearer) unambiguously in the same Context of meaning as the template’s applicability frame.

**R‑ME‑3 (Evidence stub).** Where the template requires it, a Measure **SHALL** include an **EvidenceStub**—a conceptual pointer sufficient to support independent reasoning about the claim’s origin. (The old spec framed this as “traceability/provenance”; we keep only the **conceptual** role here. )

**R‑ME‑4 (Time stance).** A Measure **SHALL** carry a **time stance** (e.g., “as‑observed at T”, or “as‑aggregated over W”), expressed conceptually; it disambiguates the reading’s intended window without prescribing formats.

**R‑ME‑5 (Entity vs relation).** If the Characteristic is **relational**, the subject is a **tuple** (pair, k‑tuple); the wording of the claim reflects that arity and the template’s relation topology (cf. A.17).

R‑ME‑6 (MAY):** “`UncertaintyStub` — optional conceptual pointer to the adopted uncertainty estimation for this Measure, **if** required by the template.

> *Informative anchor.* The old Annex B example “Article Completeness” illustrates the split template/measure/evidence; **C.16** keeps the split but forbids storage‑level talk.

### 5.3.3 `U.Unit` — semantics of quantities (normative)

**Role.** A conceptual marker of **quantity kind** and admissible **conversions** within that kind; not every scale requires it.

**R‑UN‑1 (Quantity kind).** Where units apply, the template **SHALL** indicate the **quantity kind** (e.g., Time, Length, Dimensionless‑Score). Units are meaningful only **within** one kind.

**R‑UN‑2 (Convertibility).** Comparisons across different units are permitted **iff** they are **convertible** by kind‑preserving transformation (ratio/interval scales); for ordinal/nominal scales, no numeric conversions exist. (Old Annex A listed conversion hints; here we assert the conceptual boundary. )

**R‑UN‑3 (Canonical labels).** `%` denotes “fraction×100”; “points” denotes dimensionless magnitudes used for scores; “stars” denotes discrete ordinal marks. These are **labels** of representation, not new characteristics.

**R‑UN‑4 (Quantity‑kind bridge).** A Template on an interval/ratio Scale **SHOULD** name the underlying **quantity kind** (e.g., ISO 80000/QUDT category) to enable safe external bridges. This does **not** import external vocabularies; it declares an alignment point.

### 5.3.4 `U.EvidenceStub` — pointer to grounds (normative)

**Role.** A compact **tie** from a Measure to the grounds sufficient for **reasoned audit** (not a repository prescription).

**R‑EV‑1 (Minimal sufficiency).** An EvidenceStub **SHALL** carry, at minimum, a **type‑of‑ground** and an **identifier** sufficient to retrieve or reconstruct the grounds in the appropriate Context of meaning.

**R‑EV‑2 (Compositionality).** Multiple grounds may be **composed** as a finite set; composition is **commutative/associative/idempotent** at the level of stubs, enabling conceptual merge of corroborations.

**R‑EV‑3 (Soundness axiom).** A Measure **is admissible** only if at least one **auditable chain of grounds** can be stated from the bearer to the Characteristic via an appropriate Description (Object–Concept–Symbol triangle in the episteme). (The old text motivates “transparency/trust”; **C.16** states the conceptual admission rule. )

## 5.4 · Polarity, Comparability, and Gauges (normative)

> **Notation.** To avoid clashes with the kernel’s global aggregation symbol, this architheory denotes a gauge mapping by **𝒢** (calligraphic 𝒢).

**R‑POL‑1 (Declared polarity).** Every ordered scale **SHALL** declare polarity at the **template**. Any Gauge **𝒢** must be **monotone** with that polarity.

**R‑CMP‑1 (Comparability conditions).** Two readings are **directly comparable** when they share **Characteristic**, **scale type**, and **unit** (or unit is convertible within one quantity kind). Otherwise, comparability requires an explicitly declared **𝒢** on a common representation.

**R‑G𝒢‑1 (Gauge disclosure).** If a metric issues a **Score**, its Gauge **𝒢 : Coordinate → Score** **SHALL** be named with a **bounded codomain** and stated monotonicity. (The old text discussed “score ranges” and mapping; **C.16** keeps only the conceptual duty. )

**R‑G𝒢‑2 (Ordinal respect).** For ordinal inputs, **𝒢** must be **order‑preserving**; interval assumptions **MUST NOT** be smuggled in.


## 5.5 · Entity vs Relation bindings (normative clarifications)

**R‑ER‑1 (Arity preservation).** If the Characteristic is `U.EntityCharacteristic`, the subject is **one** bearer; if `U.RelationCharacteristic`, the subject is a **k‑tuple** (k ≥ 2). The Measure’s claim text **SHALL** reflect this arity.

**R‑ER‑2 (Relation scale).** Relation‑valued scales **SHALL** fix their symmetry/antisymmetry and directionality (e.g., distance symmetric; influence directional), at the **template** level.

**R‑ER‑3 (Bridge to CG‑frames).** In architectural CG‑frames, **Coupling/Cohesion** are Characteristics over **modules** (structure) or **roles** (function). Their measures are relational (**Coupling**) or unary (**Cohesion** within an element), but both live in the same MM‑CHR substrate. (Alignment hinted in the old mapping rows across contexts. )

---

## 5.6 · Acceptance (conceptual, RSG‑aware)

> Acceptance here is **thought‑level**. It uses the **Reachable‑States Graph (A.2.5)** pattern to organise mental checks—no “lifecycle” narratives.

**SCR‑C16‑A (Template sufficiency).** You can traverse **N1→N3** (Characteristic fixed → Scale typed → Unit coherent) for the template **without** invoking any implementation artifacts (cf. A.18 RSG alignment).

**SCR‑C16‑B (Reading sufficiency).** For a given subject, you can traverse **N4→N6** (Gauge named where needed → exemplar‑anchored sense → reading established) with polarity and arity explicit.

**SCR‑C16‑C (Comparability).** When two readings are placed side‑by‑side, you can state in one breath whether they are **comparable as‑is** or only **after 𝒢**, and **why**.

**SCR‑C16‑D (Evidence adequacy).** For any required EvidenceStub, you can sketch at least one **auditable chain of grounds** from the subject to the Characteristic via a Description in the right Context.

---

### 5.7 Cross‑references & anchors

* **A.17 (CHR‑NORM).** Canonical **Characteristic** and Entity/Relation split; lexical rules and alias sunset.
* **A.18 (CSLC‑KERNEL).** One Characteristic + one Scale per template; Level optional; operation guard by scale type.
* **Annex C (old MM‑CHR).** Cross‑domain alignment hints for Characteristics/Observations/Quantities across ISO 80000, ISO/IEC 25024, QUDT, SOSA/SSN (used here only as conceptual witnesses).

## 6  Permitted operations by scale type (with anti‑examples)

| Scale type   | Comparisons    | Location          | Differences        | Ratios                   | Admissible summaries                                  | Typical anti‑patterns (forbidden)                                   |
| ------------ | -------------- | ----------------- | ------------------ | ------------------------ | ----------------------------------------------------- | ------------------------------------------------------------------- |
| **Nominal**  | =, ≠           | mode, frequencies | —                  | —                        | counts, proportions                                   | averaging labels; ordering categories without a declared order      |
| **Ordinal**  | <, =, > (rank) | median, quantiles | **not meaningful** | —                        | order‑respecting summaries (median rank, percentiles) | arithmetic mean of ranks; variance on ranks; linear blends of ranks |
| **Interval** | <, =, >        | mean location     | Δ meaningful       | ratio **not** meaningful | mean, sd of **differences**, correlation              | ratio claims (“twice as hot” in °C); geometric mean                 |
| **Ratio**    | <, =, >        | mean location     | Δ meaningful       | ratios meaningful        | arithmetic/geometric means, cv, growth rates          | adding heterogeneous units; log on nonpositive values               |

**Guards.**
G‑1 (Order). On ordinal, any transform used inside 𝒢 **MUST** be **monotone**.
G‑2 (Differences). On interval/ratio, **Δ** is legitimate; on ordinal/nominal, it is **undefined**.
G‑3 (Ratios). Only ratio Scales admit **x/y** semantics; interval/ordinal/nominal do not.
G‑4 (Unit coherence). Interval/ratio arithmetic presumes compatible units (or declared conversion).
G‑5 (Target polarity). If polarity is “targeted”, comparison is via distance‑from‑target, not simple ↑/↓.

*(These rules line up with the MM‑CHR exposition of CSLC and term discipline; A.17 fixes the lexical side.)* 

## 7 · Evidence Semantics (Normative)

### 7.1  What an Evidence Stub is (and is not)

**Definition.** `U.EvidenceStub` is a **conceptual pointer** that ties a **measure** to the **grounds** sufficient for independent checking (observations, arguments, lawful transformations). It is not the run log, not the carrier, and not the intensional characteristic itself. This keeps **intension–description–specification** distinct per E.10.D2 and the Clarity Lattice.

**Rule Σ‑1.** Whether evidence is **required** is a **property of the metric template**; if required, each `U.Measure` **SHALL** include an `U.EvidenceStub`.
**Rule Σ‑2.** Evidence composition is **commutative, associative, idempotent** at the concept level (sets/multisets of grounds); combining grounds can never *reduce* what is knowable about the measure’s warrant.
**Rule Σ‑3.** *Soundness minimum:* there exists a conceptual chain linking **bearer → Characteristic → Scale/Unit → admissible method/episteme**. (No “free‑floating numbers”.)
**Rule Σ‑4.** Declared *agreement* constructs (e.g., dual readings, panels) **MUST** be appropriate to the scale type (rank concordance for ordinal; tolerances for interval/ratio).
*Anchors:* MM‑CHR units/evidence notion; Strict Distinction and the separation of objects from their descriptions/specs.

---

## 8 · Integration with RSG & Dynamics (Normative/Clarifying)

### 8.1  RSG (Role‑State Graph) touch‑points

MM‑CHR **supplies recognisers** used in **State Checklists**. A checklist criterion **may** refer to a measure (e.g., “Cohesion ≥ T on ordinal ladder”), but the **state itself remains intensional**; the checklist is its **description**, and a **StateAssertion** is an evidence‑backed verdict over a Window. No lifecycle language is implied; RSGs are open‑ended graphs with re‑entry edges.

**Rule RSG‑M1.** When a checklist cites a measure, it **SHALL** do so by **Characteristic + Scale semantics** (and unit if applicable), not by colloquial aliases; Tech/Formal registers apply. **Rule RSG‑M2.** Thresholds in checklists **MUST** respect the scale type (no ratio talk on interval scales; no arithmetic on ordinal ladders).

### 8.2  Dynamics & CharacteristicSpace

`U.Dynamics.stateSpace` is a **CharacteristicSpace**—a named set of Characteristics with units/topology. MM‑CHR provides the **measurement side** of that space; architheories specify the **transition law**. Architectural or epistemic **dynamics** are then *trajectories in the declared CharacteristicSpace*. **No** procedural or storage commitments are implied.

## 9 · Conformance Checklist (Normative)

> *Thought‑level acceptance conditions for authors and reviewers; they constrain meaning, not tooling.*

**CC‑MCHR‑1 · CSLC anchoring.** Each `U.DHCMethodRef` binds **exactly one** `U.Characteristic` and **exactly one** scale; each `U.Measure` carries a value valid for that scale (cf. A.18).
**CC‑MCHR‑2 · Polarity declared.** Every **ordered** scale in a template declares **polarity**; any **Score** via 𝒢 is monotone w\.r.t. that polarity.
**CC‑MCHR‑3 · Unit coherence.** Claims that compare or combine values are **grounded in unit coherence** (or declared conversions for interval/ratio).
**CC‑MCHR‑4 · Comparability honesty.** Ordered comparisons are asserted **only** when §7.2 holds; otherwise authors use qualitative/set‑level language.
**CC‑MCHR‑5 · Evidence sufficiency.** Where evidence is required by the template, the measure’s grounds are **conceptually sufficient** to retrace the claim; composition respects Σ‑laws (§8).
**CC‑MCHR‑6 · RSG alignment.** If a measure gates a **state** in an RSG, the checklist criteria **respect scale semantics** and the **intensional vs description** split. No lifecycle phrasing; use RSG open‑ended moves.
**CC‑MCHR‑7 · Dynamics awareness.** Where discussions involve change, the **CharacteristicSpace** is **named** (characteristics, units, topology) and separated from the **transition law** (architheory side).
**CC‑MCHR‑8 · Lexical guard‑rails.** Tech identifiers and headings use **Characteristic/Scale/Level/Value/Score/Unit/Gauge**; aliases (axis/dimension/points/stars) appear **only** in explanatory Plain register with a first‑mention mapping to the Tech canon.

### 10 · Invariants & Anti‑Patterns *(Normative unless marked “Informative”)*

#### 10.1 Invariants (N‑rules)

**N‑1 — One Characteristic + one Scale per template.**
Every `U.DHCMethodRef` binds *exactly one* **Characteristic** and *exactly one* **Scale** (its type + admissible range or level‑set). This is the CSLC sufficiency condition for interpretability.

**N‑2 — Value validity.**
A `U.Measure` holds a **Value** that is *admissible* for the template’s Scale (numeric range, categorical level); when a **Level** is used, it is among the named rungs declared for that Scale.

**N‑3 — Polarity is declared at the template.**
For ordered Scales, the template states the comparison direction (↑ better / ↓ better / target‑is‑best). Any **Gauge mapping** to **Score** preserves that monotonic ordering. *(Note: we use “Gauge mapping” instead of the Greek letter used elsewhere in FPF to avoid symbol conflicts.)*

**N‑4 — Unit coherence.**
Within one template there is one *primary* **Unit** of expression (or an explicit level‑set for non‑numeric Scales). Conversions are conceptually allowed only where the Scale supports meaningful arithmetic (interval/ratio); nominal/ordinal Scales are not subject to numeric conversions.

**N‑5 — Comparability guard.**
Two Measures are comparable *iff* they share the same template (hence, the same Characteristic + Scale + Unit) **or** stand in an explicit equivalence declared via the Unification suite (F‑cluster Bridges). Otherwise, comparability is not presumed.

**N‑6 — Evidence as conceptual anchoring.**
If a template requires it, each Measure includes an **EvidenceStub** that conceptually links the Value to its grounds; absence where required makes the Measure inadmissible for use. *(This is a conceptual obligation; no process mechanics are implied.)*

**N‑7 — Arity clarity.**
If the Characteristic is relational (applies to a pair/tuple), the subject of measurement is the relation itself; the reading must not be re‑described as a unary property of either participant.

**N‑8 — Open‑ended evolution; graph, not lifecycle.**
When MM‑CHR is used in change reasoning, movement happens in a **CharacteristicSpace** and along a reachable‑states graph (RSG). There is no lifecycle terminal; revisions may re‑enter earlier framing nodes as per A.17. *(Conceptual control structure only.)*

---

#### 10.2 Anti‑Patterns (A‑rules) — with cures

**A‑1 — Scale drift under the same template.**
*Smell:* the Scale meaning (bounds, categories) shifts while the template ID remains.
*Cure:* version the template; declare the relation in the Unification suite.

**A‑2 — Arithmetic on ordinal.**
*Smell:* averaging “stars” or ranking labels as if they were intervals.
*Cure:* either keep order‑respecting operations only, or introduce a Gauge mapping that defines a proper Score range.

**A‑3 — Unit soup.**
*Smell:* mixing milliseconds and seconds for the same template, or “%” and “points” for one Scale.
*Cure:* one primary Unit per template; conversions (when meaningful) are declared conceptually, not ad‑hoc.

**A‑4 — Alias leakage.**
*Smell:* “axis/dimension/point/ladder” in normative identifiers or headings.
*Cure:* use only canonical tokens in normative prose; narrative labels are allowed *solely* in Plain register with first‑mention mapping (A.17).

**A‑5 — Multi‑Characteristic stuffing.**
*Smell:* one template tries to carry a vector of Values for several Characteristics.
*Cure:* separate templates (one Characteristic each) and compose coordinates explicitly when needed.

**A‑6 — Evidence afterthought.**
*Smell:* Measures required to have grounds are introduced without an intelligible EvidenceStub.
*Cure:* treat the EvidenceStub as part of the measurement claim itself, not an accessory.

**A‑7 — Template mutation after Measures exist.**
*Smell:* retro‑editing Characteristic/Scale/Unit of an active template.
*Cure:* immutability of that triad post‑use; publish a successor template if the concept changes.

**A‑8 — Score‑of‑everything.**
*Smell:* collapsing heterogeneous Values into a single “points” Score without declared ScoreMethod and SCP.
*Cure:* retain the Value on its Scale; add an explicit ScoreMethod and SCP only when there is a justified need for a Score.

### 11 · Cross‑Domain Vignettes *(Informative, transdisciplinary)*

> *Each vignette shows an CSLC‑conformant template → measure, without duplicating the A.17/A.18 glossaries.*

**V‑A (Architecture — relational property).**
Characteristic: **Coupling** (relational) between modules; Scale: ordinal {Low, Med, High}; Unit: level‑labels; Polarity: ↓ better.
Reading: subsystem pair ⟨M₁, M₂⟩ gets **Med**; ScoringMethod (optional) maps levels monotonically to a bounded Score for comparative dashboards.

**V‑B (Physics — interval/ratio).**
Characteristic: **ResponseTime**; Scale: ratio with non‑negative reals; Unit: seconds; Polarity: ↓ better.
Reading: subject S has **0.237 s**; comparability holds with any template that declares the same Characteristic+Scale+Unit (or an explicit equivalence).

**V‑C (Performing arts — ordinal).**
Characteristic: **EdgeControlQuality**; Scale: ordinal levels 1…5; Unit: level‑labels; Polarity: ↑ better.
Reading: performance P gets **4**; any aggregation uses a declared ScaleComplianceProfile (SCP) that respects order.

**V‑D (AI ethics — ratio).**
Characteristic: **ParityGap** (difference of positive rates); Scale: interval with symmetric bounds; Unit: percentage points; Polarity: ↓ better (0 is target).
Reading: model M on cohort C shows **3.2 pp**; evidence points conceptually to the derivation rationale (inputs, reference cohorts).

### 12 · Relations & Placement *(Informative)*

**Kernel.** MM‑CHR *imports* the canonical Characteristic vocabulary and the CSLC discipline fixed by A.17 and A.18; it does not redefine them. CharacteristicSpace reasoning (for change) lives in the architheories that consume MM‑CHR readings.

**Using architheories.** KD‑CAL, Arch‑CAL and others *instantiate* templates and produce measures; MM‑CHR remains a neutral measurement substrate. Trade‑off analyses and architectural trajectories operate over coordinates that MM‑CHR makes available, not inside MM‑CHR.

**Unification (F‑cluster).** External standards (e.g., ISO 80000 quantity types; W3C SOSA/SSN observable properties; QUDT units/quantity kinds) are related via Concept‑Set rows and Bridges; MM‑CHR treats those alignments as context supplied by F‑patterns, not as local re‑definitions.

## C.17 — **Creativity‑CHR** — Characterising Generative Novelty & Value 

### 0 · Status, Placement & Exports

**Status.** Architheory specification (**CHR**) — normative where stated.
**Depends on.** A‑kernel (A.1–A.15), **CHR‑CAL** (C.7), **MM‑CHR** measurement infrastructure (C.16), **KD‑CAL** and **Sys‑CAL** for carriers and holons, **Decsn‑CAL** (utility), **Norm‑CAL** (constraints/ethics).
**Coordinates with.** **B.5.2.1 NQD** (abductive generator) for search instrumentation, **Agency-CHR** (C.9) for agential capacity, B-cluster trust/assurance (B.3), Canonical Evolution Loop (B.4), Role Assignment & Enactment Cycle (Six-Step) (F.6) and Naming Discipline for U.Types & Role Names (F.5).
**Guard‑rails.** Obeys E‑cluster authoring rules (Notational Independence; DevOps Lexical Firewall; Unidirectional Dependency).

**What this architheory provides (exports):**

This architheory exports **Characteristics** and measurement templates **only**. It **does not** export any Γ\_\* operators, portfolio composition rules, or selection/scalarization policies; those live in **C.18 NQD-CAL** and **C.19 E/E-LOG** (or **Decsn-CAL** for decision lenses). A Context _publishes_ the measurement space and admissible policies; a decision is taken by an _agent in role_ using a _named lens_ within that space.

* **`U.CreativitySpace`** — a **CharacteristicSpace** (CHR) with named **Characteristics** and scale metadata for evaluating creative work/outcomes **inside a `U.BoundedContext`**.
* **`U.CreativityProfile`** — a vector of coordinates in `U.CreativitySpace` attached by a **`U.Evaluation`** to a specific **Outcome** (usually an `U.Episteme` produced by `U.Work`).
* **Core Characteristics (kernel nucleus; Context‑extensible):**
1. **`Novelty@context`** — distance from a **`ReferenceBase`** in the current Context/time window; ∈ \[0, 1].
2. **`Use‑Value`** *(alias: `ValueGain`)* — measured or predicted improvement against a **declared objective**; interval/ratio scale per Context.
3. **`Surprise`** — negative log‑likelihood under a **GenerativePrior**; bits or nats.
4. **`ConstraintFit`** — degree of **must‑constraint** satisfaction (Norm‑CAL / Service acceptance); ∈ \[0, 1].
5. **Diversity_P (portfolio-level)** — coverage/dispersion (set-level). **Illumination** is a **report-metric over Diversity_P** (coverage/QD-score summaries). It is **report-only** and **never** part of the primary dominance test.
6. **`AttributionIntegrity`** — provenance/licensing discipline for lawful, transparent recombination; ∈ \[0, 1].
7. **`FamilyCoverage`** — (count, polarity ↑, scope=portfolio, unit=families, provenance: F1‑Card)
8. **`MinInterFamilyDistance`** — (ratio [0,1] or metric units, polarity ↑, scope=portfolio, DistanceDef@F1‑Card)
9. **`AliasRisk`** —  (ratio [0,1], polarity ↓, diagnostic; drop if dSig ≥3/5 characteristics collide)
10. **`U.DomainDiversitySignature (dSig)`** — 5‑tuple over discrete characteristics **[Sector, Function, Archetype, Regime, MetricFamily]**  attached to each `U.BoundedContext`. Used for **Near‑Duplicate** diagnostics and `AliasRisk`. Policy: flag as Near‑Duplicate when ≥3 characteristics match; see F.1 invariants and SCR‑F1‑S08..S09. 
11. **Note (AliasRisk binding).** `AliasRisk` MAY be computed using `dSig` collision diagnostics; a Context MUST declare the collision rule and policy id in DescriptorMap provenance when AliasRisk is reported.

* **Supporting types (linking points):**

  * **`U.ReferenceBase`** — the domain‑local corpus (by Context & time window) used to compute `Novelty@context`.
  * **`U.SimilarityKernel`** — a declared similarity metric class for the Context (text/image/design/code/etc.), with invariance notes.
  * **`U.GenerativePrior`** — a predictive model over the Context’s artifacts/behaviours used to compute `Surprise`.
  * **`U.CreativeEvaluation`** — a specialisation of `U.Evaluation` that yields a `U.CreativityProfile` and the Evidence Graph Ref.
  * **`EffortCost`** *(advisory)* — resource outlay to achieve the outcome; from WorkLedger (Resrc‑CAL). *(For normalization and planning; not itself “creativity.”)*


* **Operators (first tranche):** `composeProfiles` (set → portfolio), `dominates` (partial order in space), `frontier` (Pareto set), `normaliseByEffort`. *(Formal laws introduced in Quarter 2.)*
* **Relations (informative; not exported):** dominance relation (partial order in the space), frontier predicate (Pareto set), portfolio composition view. *C.17 exports no operators; these are mathematical relations only.*
* 
> **Scope note.** This architheory **does not** define who is “a creative person.” It characterises **creative outcomes and episodes** as **observed in Work** and **expressed as Epistemes**. Agency (capacity to originate) is measured in **Agency‑CHR (C.9)**; here we measure **what came out** and **how it scores** against stated goals and references.  A **Context publishes** the measurement space and admissible policies; a **decision is made by an agentic system in role**, using a named lens within that space. CHR exports **no Γ‑operators** and **no team workflow rules**.

### 1 · Motivation & Intent (manager’s read‑first)

**Problem we solve.** Teams talk past each other about “creativity”: some prize **novelty**, others **business value**, others **originality** or **risk‑managed invention**. Without a shared, context‑local measurement space, reviews derail, portfolios drift, and safety constraints are waived ad‑hoc.

**Intent.** Provide a **small, universal measurement kit** that turns “this is creative” into **checkable, context‑local statements** — grounded in **evidence**, aligned to **objectives**, and **composable** from individuals to portfolios.

**Manager’s one‑screen summary (what you can do with it):**

1. **Score** a design/code/theory change on **Novelty–Value–Surprise–ConstraintFit** with declared references and models.
2. **Compare** options in a **Pareto sense** (no single magic score forced).
3. **Consider** constraints as a **coordinate** in the space; compare options on **frontiers** while keeping Context for high‑novelty options
4. **Track** a portfolio’s **Diversity** to avoid local maxima and groupthink.
5. **Defend** decisions with an auditable **CreativeEvaluation** that cites **what was new relative to which base**, **how value was measured**, and **why this counts here**.

---

### 2 · Forces

| Force                                | Tension we must resolve                                                                                                                 |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Universality vs. domain detail**   | One kit must serve hardware design, software, policy, and science, yet let each Context pick similarity kernels, priors, and value models. |
| **Invention vs. constraint**         | Creative leaps are valuable; safety, ethics, and acceptance are non‑negotiable.                                                         |
| **Local truth vs. Cross‑context reuse** | Meaning is context‑local (A.1.1); yet we need Bridges to compare across organisations/disciplines.                                         |
| **Single score vs. frontier**        | Management wants a number; reality is multi‑objective.                                                                                  |
| **Randomness vs. intention**         | Random noise looks “novel” yet useless; planned recombination can be highly creative.                                                   |

**Design answer.** A **context‑local CreativitySpace** with a **small set of characteristics**, each with **clear measurement templates** and **Evidence Graph Ref**; composition uses **frontiers and partial orders**, not forced scalarisation.

---

### 3 · Solution Overview — The context‑local CreativitySpace

**Idea.** Creativity is **not a type**; it is a **profile** measured on an **outcome** (episteme) or **episode** (set of works) **inside a bounded context**. The context supplies the **ReferenceBase**, **SimilarityKernel**, **GenerativePrior**, **objective function(s)**, and **acceptance constraints**.

**Objects in play (A‑kernel alignment):**

* A **system** (person, team, service) performs **`U.Work`** under a role (A.2).
* That work yields a **carrier** (doc/model/design/code), i.e., an **`U.Episteme`**.
* We apply a **`U.CreativeEvaluation`** to that episteme (and linked work) to produce a **`U.CreativityProfile`** with evidence.

**Cre­ativitySpace (first‑class CHR):**
`U.CreativitySpace(Context) := 〈Novelty@context, ValueGain, Surprise, ConstraintFit, Diversity_P, AttributionIntegrity, EffortCost?〉`
with **scale**/**unit** metadata from **MM‑CHR** (C.16), and Context‑specific **measurement methods** bound by **MethodDescription**.

**Design/run split (A.4):**

* **Design‑time**: score **concepts** or **specs** against **surrogate value models** and **priors**; record **assumptions** (USM scopes; A.2.6).
* **Run‑time**: recompute **ValueGain** and **ConstraintFit** from Work evidence (service acceptance, KPIs) and refresh **Surprise** if priors update.

---

### 4 · Vocabulary (CHR terms & D‑stubs)

> Names are **context‑local**; below are kernel terms. Roles like “Designer/Reviewer” are contextual (A.2). **Documents don’t act** (A.7/A.12); they are **evaluated**.

1. **`U.ReferenceBase`** *(D).* A curated, versioned **set of artifacts** (epistemes) and/or behaviours that define “what exists already” **in this Context and time window**.
   **Conformance (RB‑1):** must declare **inclusion criteria**, **time span (`TimeWindow`)**, and **coverage notes**.

2. **`U.SimilarityKernel`** *(D).* A declared **metric family** with invariances (e.g., text: cosine over embeddings, image: LPIPS, code: AST graph edit).
   **Conformance (SK‑1):** must cite **MethodDescription** and **test corpus**; state **limits**.

3. **`U.GenerativePrior`** *(D).* A model that yields **likelihood** of artifacts given the Context’s history (n‑gram/LM, design grammar, trend model).
   **Conformance (GP‑1):** must publish **training slice**, **fit method**, **perplexity/fit metrics**, and **refresh policy**.

4. **`U.CreativeOutcome`** *(D).* Any **`U.Episteme`** put forward for creative evaluation (e.g., new design, algorithm, spec, policy draft).
   **Note.** If the outcome is a **system change** without a single carrier, attach the evaluation to a **bundle** (set) of carriers referenced from Work.

5. **`U.CreativeEvaluation`** *(D).* A **`U.Evaluation`** that outputs a **`U.CreativityProfile`** and anchors to **ReferenceBase**, **Kernel/Prior**, **objective(s)**, **acceptance tests**, and **Work evidence**.

6. **`U.CreativityProfile`** *(D).* The **coordinate tuple** in `U.CreativitySpace` with provenance to the above inputs and **USM scopes**.
   **Conformance (CP‑1):** profile **must** include **scales/units**, **scopes**, **confidence bands** (B.3), and the **edition** of space definitions.

---

### 5 · The Core Characteristics (kernel nucleus)

Each characteristic is specified per **MM‑CHR (C.16)** with: **name**, **intent**, **carrier**, **polarity**, **scale type**, **measurement template**, **evidence**, **scope (USM)**, and **didactic cues**. *Context profiles MAY add characteristics; kernel characteristics MAY NOT be removed without a Bridge.*

#### 5.1 · `Novelty@context` — “How unlike the known set is this?”

* **Intent.** Quantify **distinctness** of the outcome relative to **`U.ReferenceBase`** (global or targeted slice).
* **Carrier.** `U.Episteme` (the outcome).
* **Polarity.** Higher is “more novel.”
* **Scale.** **\[0, 1]**; ratio (0 = duplicate under kernel; 1 = maximally distant).
* **Measurement template (normative pattern):**

  1. Declare **ReferenceBase** `B` and **TimeWindow** window.
  2. Declare **SimilarityKernel** `σ` and its invariances.
  3. Compute **`Novelty@context := 1 − max_{b∈B} sim_σ(outcome, b)`**, or a robust variant (top‑k mean).
  4. Publish **sensitivity note** (how results shift with kernel/`B`).
* **Evidence.** Kernel/version id; top‑k neighbours with distances; ablation on invariances.
* **Scope hooks (USM).** `B` **must** be a declared **slice**; Cross‑context use needs a **Bridge** with **CL** and **loss notes**.
* **Didactic cues.**

  * **Not** “randomness.” Noise has high novelty, low value.
  * **Local, not global.** Novelty is **to this Context now**, not timeless originality.

#### 5.2 · `Use‑Value` *(alias: `ValueGain`)* — “What good did this add under our objective?”

* **Intent.** Quantify **benefit** vs a baseline objective (Decsn‑CAL utility, Service acceptance, KPI).
* **Carrier.** Outcome (episteme) with **Work** evidence.
* **Polarity.** Higher is better.
* **Scale.** Interval/ratio, unit **declared by the Context** (e.g., ΔSNR, % defects, profit/period).
* **Measurement templates (pick one):**

  * **Measured:** `ValueGain := metric_after − metric_before` (declare counterfactual method).
  * **Predicted:** `E[ValueGain | model]` with error bars; update post‑run.
  * **Evidence.**  Declared **objective/criterion**; measurements or credible predictions; counterfactual method (A/B, back‑test, causal inference).
  * **Scope.** State the **context window** used for the objective; claims outside that window are **informative only**.
  * **Didactic cues.**

  * Value is **relative to stated objective**; if the objective is wrong, the value reflects it.
  * Keep **counterfactual discipline**; otherwise “gain” is storytelling.

#### 5.3 · `Surprise` — “How improbable under our learned world?”

* **Intent.** Capture **unexpectedness** given **`U.GenerativePrior`**.
* **Carrier.** Outcome.
* **Polarity.** Higher surprise = more unexpected.
* **Scale.** **bits** or **nats**: `Surprise := −log p_prior(outcome)`.
* **Measurement template:**

  1. Declare **GenerativePrior** (training slice, model class).
  2. Encode outcome for the prior; compute likelihood proxy.
  3. Publish calibration curve (reliability diagram / PIT histogram).
* **Evidence.** Model cards; fit metrics; OOD diagnostics; refresh policy.
* **Scope.** Training slice declared as **ContextSlice**; Bridges penalise **R** (trust), not the value itself (A.2.6).
* **Didactic cues.**

  * **Novelty vs Surprise:** high novelty under one kernel may be low surprise under a broad prior; publish both.

#### 5.4 · `ConstraintFit` — “Did it honour the non‑negotiables?”

* **Intent.** Ensure **mandatory constraints** (safety, ethics, standards, SLOs) are satisfied.
* **Carrier.** Outcome + Work evidence.
* **Polarity.** Higher is **better** (1 = all mandatory satisfied).
* **Scale.** **\[0, 1]**, ratio or pass/fail.
* **Measurement template:** declare **set `C_must`** (Norm‑CAL / Service acceptance), compute **`ConstraintFit := |{c∈C_must : pass(c)}| / |C_must|`**; optionally weight per criticality.
* **Evidence.** Checklists, tests, audits; Who/Role performed the **SpeechActs** (approvals/waivers).
* **Scope.** Constraints are **context‑local**; Cross‑context requires **Bridge**; waivers are **SpeechAct Work** with RSG gates (A.2.5).
* **Interpretation note.** Low `ConstraintFit` signals tension with declared **must‑constraints** and warrants reframing or redesign; **this pattern does not prescribe go/no‑go rules**.

#### 5.5 · `Diversity_P` *(portfolio‑level)* — “Are we exploring the space?”

* **Intent.** At the **set** level, avoid myopic exploitation; promote **coverage**.
* **Carrier.** A **set** of outcomes.
* **Polarity.** Higher means **broader coverage** (not “better” per se).
* **Scale.** Set‑functional; Context defines metric (e.g., **average pairwise distance**, **k‑cover** over features).
* **Template.** Declare **kernel** and **covering policy**; compute score and **coverage map (illumination)**; relate to **USM ClaimScopes**.
* **Alignment note.** The **illumination/coverage** view corresponds to *IlluminationScore* used by **B.5.2.1 NQD‑Generate**; no separate characteristic is introduced here—measure it as part of `Diversity_P`.
* **Evidence.** Distance matrix/cover plots; sensitivity to kernel.
* **Didactic cue.** Use **Diversity\_P** to **shape portfolios**, not to pick single winners.
* **Marginal gain (for generators)** — normative. For a candidate h and current set S, ΔDiversity_P(h | S) := Diversity_P(S ∪ {h}) − Diversity_P(S). Contexts using NQD SHALL compute D as this marginal and publish the Diversity_P definition alongside the CharacteristicSpace/kernel and TimeWindow.

**Heterogeneity Characterisation**
* FamilyCoverage  (polarity ↑) — count of distinct domain‑families covered by a portfolio/triad; unit: families; window: declared.
* MinInterFamilyDistance (polarity ↑) — min distance between selected families in DescriptorMap; unit: per DistanceDef; window: declared.
* AliasRisk (polarity ↓) — collinearity/near‑duplicate risk indicator for contextual signatures; unit: score (0–1) with policy id.


**Lexical special case (F.18 naming).**  
For **lexical CandidateSets** used by Name Cards (F.18), **Diversity_P SHALL be computed over head-term families, not over raw strings**. Variants that share the same lexical head (e.g., “Reference plane”, “Plane of reference”, “Planar reference”) **MUST** be treated as one family for coverage and distance; only candidates with distinct heads contribute to lexical Diversity_P. This aligns lexical use of Diversity_P with `FamilyCoverage` / `AliasRisk` and prevents inflating diversity by near-synonyms of a single head.


#### 5.6 · `AttributionIntegrity` — “Did we credit sources and licences correctly?”

* **Intent.** Discourage “novelty theft”; ensure **recombination** is **lawful and transparent**.
* **Carrier.** Outcome + provenance graph.
* **Polarity.** Higher is better.
* **Scale.** **\[0, 1]**; fraction of **required attributions/licence duties** satisfied.
* **Template.** Trace graph coverage against Context policy; licence constraints as **Norm‑CAL** rules.
* **Evidence.** PROV‑style links; licence scans; acknowledgements.
* **Didactic cue.** High `AttributionIntegrity` signals lawful and transparent recombination; low values indicate unacceptable practice in most Contexts.  
* **Default role.** `AttributionIntegrity` is **measurable but non‑dominant**. It MAY serve as a **policy filter/tie‑break** (C.19). If certain attribution duties are **must‑constraints**, they belong to **ConstraintFit** (Norm‑CAL) and act as **eligibility gates**. It is **not** part of the default dominance set.
* **Dominance & gating note (normative).** `AttributionIntegrity` is a measurable **Characteristic**; it is **not** in the default dominance set. Contexts MAY use it as a **filter** or **tie‑break** via policy (C.19). Legal/ethical **must‑fit** checks live in **ConstraintFit** (Norm‑CAL); failing those blocks eligibility **before** dominance.

#### 5.7 · `EffortCost` *(advisory)* — “What did it take?”

* **Intent.** Normalise comparisons by cost; not part of “creativity” per se.
* **Carrier.** WorkLedger.
* **Polarity.** Lower is better when used as denominator.
* **Scale.** Resource units (hours, energy, \$).
* **Template.** Sum cost categories over Work that produced the outcome.
* **Evidence.** Time/resource logs; BOM deltas.
* **Didactic cue.** Use **`CreativityPerCost := f(Novelty@context, ValueGain, Surprise)/EffortCost`** for operations planning, not for excellence awards.

---

### 6 · Conformance Checklist (first tranche)

| ID                                        | Requirement (normative)                                                                                                                                                                  | Purpose / audit hint                                          |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **CC‑CR‑1 (context‑locality)**               | Every **CreativityProfile** **MUST** name the **`U.BoundedContext`** and the **edition** of `U.CreativitySpace`.                                                                         | Prevents Cross‑context slippage.                                 |
| **CC‑CR‑2 (Declared bases)**              | **Novelty@context** claims **MUST** declare `ReferenceBase`, `SimilarityKernel`, and `TimeWindow`; **Surprise** claims **MUST** declare `GenerativePrior` and its training slice.                 | Makes “new to whom?” and “unexpected under what?” explicit.   |
| **CC‑CR‑3 (Objective anchor)**            | **ValueGain** **MUST** reference the **objective** (KPI/utility) and **counterfactual method** (if predicted, the model).                                                                | Stops free‑form value stories.                                |
| **CC‑CR‑4 (Must‑fit)**                    | If **must** constraints exist, **ConstraintFit** **MUST** be present; enactment decisions **SHALL** treat `ConstraintFit<1` as **fail**, unless an explicit **waiver SpeechAct** exists. | Keeps safety & ethics non‑negotiable.                         |
| **CC‑CR‑5 (Evidence)**                    | Each coordinate **MUST** have Evidence Graph Ref (neighbours, tests, logs, model cards).                                                                                                   | Enables audit & replication.                                  |
| **CC‑CR‑6 (Scopes)**                      | Profiles **MUST** include **USM scopes** (ClaimScope/WorkScope) relevant to measurement; off‑scope claims are advisory.                                                                  | Ties numbers to where they hold.                              |
| **CC‑CR‑7 (No scalarisation by default)** | The architheory **SHALL NOT** force a single scalar “creativity score.” If a Context defines one, it **MUST** publish the weighting and its drift policy.                                   | Keeps decisions on a Pareto frontier unless a policy opts‑in. |
| **CC‑CR‑8 (Bridge discipline)**           | Cross‑context comparisons **MUST** use a **Bridge** with **CL** and recorded **losses**; any mapped coordinate **MUST** note penalties in the **R** lane, not silently alter the value.     | Honest portability.                                           |

---

### 7 · Manager’s Quick‑Start (apply in 5 steps)

1. **Name the Context** *(context + edition)*.
2. **Pick measurement defaults** *(kernel, prior, objective, constraints)* from the Context’s handbook.
3. **Score outcome** → `Novelty@context`, `Use‑Value`, `Surprise`, `ConstraintFit`.
4. **Decide by frontier**: shortlist **non‑dominated** options; use **ConstraintFit** as a gate; apply **policy** if a scalar is approved.
5. **Record a CreativeEvaluation** with evidence; if crossing Contexts, attach the **Bridge id**.

> **Mental check.** *New to our base? Helpful to our objective? Unexpected under our model? Safe & licenced?*
> If any answer is “unknown,” you are **not done measuring**.

---

### 8 · Archetypal Grounding (three domains)

**(a) Manufacturing design change)**
*Outcome.* New impeller geometry for Pump‑37.
*Context.* `PlantHydraulics_2026`.
*Novelty@context* 0.42 (shape‑descriptor kernel vs last 5 years).
*ValueGain.* +6.8% flow @ same power (bench Work).
*Surprise.* 1.3 bits (within evolutionary trend prior).
*ConstraintFit.* 1.0 (materials, safety, noise).
*Decision.* **Frontier winner**: modest novelty, clear value, safe. Portfolio keeps **Diversity\_P** by also funding one high‑surprise concept for exploration.

**(b) Software architecture refactor)**
*Outcome.* New concurrency model for ETL.
*Context.* `DataPlatform_2026`.
*Novelty\_G.* 0.27 (AST/edit kernel vs internal corpus).
*ValueGain.* −20% latency, −35% p95 stalls (A/B Work).
*Surprise.* 0.5 bits (trend prior expected co‑routines).
*ConstraintFit.* 0.83 (fails SoD—same author as reviewer).
*Decision.* Return for **SoD fix**; then likely adopt. Creativity is **not** a waiver over governance.

**(c) Scientific hypothesis)**
*Outcome.* A new scaling law claim.
*Context.* `GraphDynamics_2026`.
*Novelty\_G.* 0.66 (formula kernel vs literature base).
*ValueGain.* Predicted: explains 12 prior anomalies (model check).
*Surprise.* 3.7 bits (strongly unexpected under prior).
*ConstraintFit.* 1.0 (ethics N/A; evidence roles bound with decay windows).
*Decision.* Fund **replication Work**; track **R** decay per policy.

---

### 9 · Anti‑Patterns (fast fixes)

| Anti‑pattern                   | Why it fails                                                                  | Fix with this architheory                                                        |
| ------------------------------ | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **“Creativity = randomness.”** | Noise yields high `Novelty@context`, low `ValueGain` and often low `ConstraintFit`. | Evaluate **all four** characteristics; require ConstraintFit=1 for musts.                   |
| **Global originality claims.** | Ignores context‑local meaning and current corpus.                                | Declare **Context & ReferenceBase**; cross Contexts only via **Bridge**.               |
| **One magic score.**           | Hides trade‑offs; fragile under drift.                                        | Decide on **Pareto frontier**; publish scalar only with explicit weights/policy. |
| **Hand‑wavy value.**           | No objective → no audit.                                                      | Tie to **Service/KPI** or **utility**; state **counterfactual**.                 |
| **Silent borrowing.**          | Legal/ethical risk; reputational damage.                                      | Track **AttributionIntegrity**; licence scans in evidence.                       |

---

### 10 · Relations (where this plugs in)

* **A.2 Role & A.15 Run‑alignment.** Creative **Work** is performed by **systems in roles**; outcomes are **epistemes**. Creativity is **measured by `U.Evaluation`**, not “done by a document.”
* **B.3 Trust/Assurance.** Coordinates carry **confidence bands**; Bridges lower **R** by **CL**. Evidence roles (A.2.4) bind datasets/benchmarks used in measurements.
* **C.9 Agency‑CHR.** Agency measures **capacity to originate**; a high‑agency system may still output low‑creativity outcomes (and vice versa with strong scaffolding).
* **A.2.6 USM (Scope).** All measurements sit on **ContextSlices**; `G‑ladder` is explicitly **not** used (C.17 follows A.2.6’s set‑valued scopes).
* **D‑cluster ethics.** **ConstraintFit** is where **must** constraints, ethics, and safety bind the evaluation; waivers are explicit **SpeechActs**.

---

### 11 · Authoring Aids (didactic cards)

* **Write the Context.** Context + edition on every profile.
* **Name the base & kernel.** Without them, `Novelty@context` is undefined.
* **State the objective.** Value without a KPI is a story.
* **Publish priors.** Surprise needs a trained model with cards.
* **Gate by musts.** `ConstraintFit` < 1 blocks enactment unless waived.
* **Prefer frontiers.** Shortlist non‑dominated options; let governance decide trade‑offs.
* **Bridge explicitly.** Cross‑context talk needs CL and loss notes.

## 12 · CSLC recap and the Creativity CharacteristicSpace

**Purpose.** Ground “creativity” as a **measurable family of characteristics** (CHR) rather than a role, capability, or virtue. Each characteristic is scoped to a **`U.BoundedContext`**, evaluated on **`U.Work`** (episodes), **artifacts** (epistemes, e.g., design sketches, models), or **holders** (systems/teams) via **MM‑CHR** exports (`U.DHCMethodRef`, `U.Measure`, `U.Unit`, `U.EvidenceStub`), using the **CSLC** discipline (*Characteristic / Scale / Level / Coordinate*).

> **Strict Distinction (A.7) reminders.**
> *Creativity is not a Role* (no one “plays CreativityRole”). It’s a **characterisation** of outcomes/process.
> *Creativity is not Work* (no resource deltas). Work **produces** artifacts we later characterise.
> *Creativity is not a Service* (no external promise). Services are judged from Work; creativity may correlate with value.

### 12.1 · The Creativity CharacteristicSpace (CHR‑SPACE)

The core **characteristics** below are **kernel‑portable** names; Contexts **specialise** them (rename if needed, but keep semantics). Each characteristic declares: **what we measure**, **on what carrier**, **typical scale**, and **where it lives** in FPF.

| Characteristics (kernel name)       | What it captures (intuitive)                                 | Measured on           | Typical scale (CSLC)                               | Lives with / checked by              |
| ------------------------ | ------------------------------------------------------------ | --------------------- | -------------------------------------------------- | ------------------------------------ |
| **Novelty\@context**        | Distance from known ideas **in this Context**                   | Artifact / Work set   | Ratio or bounded \[0..1] via *similarity→distance* | `KD‑CAL` corpus + `U.BoundedContext` |
| **Use‑Value**            | Benefit vs a **declared objective**                          | Artifact / Evaluation | Ordinal (Fail/Partial/Pass) or scalar KPI          | `B.3` Evidence & `U.Evaluation`      |
| **Surprise**             | Unexpectedness under the Context’s **GenerativePrior**          | Artifact              | bits or nats (−log‑likelihood)                     | Prior cards & calibration            |
| **ConstraintFit**        | Degree of **must‑constraints** satisfied while exploring     | Work / Artifact       | % satisfied (0–100)                                | `Norm‑CAL` + step guards             |
| **Diversity_P**          | Portfolio **coverage/dispersion** (incl. coverage map view)  | Set of artifacts      | Set‑functional; coverage index                     | `Γ_ctx` fold + USM ClaimScopes       |
| **AttributionIntegrity** | Lawful & transparent **provenance/licensing**                | Artifact + provenance | \[0,1]                                              | PROV + Norm‑CAL                      |

> **Locality.** **Every characteristic is context‑local** (e.g., **Novelty\@context**). Cross‑context claims **must** use a **Bridge** and record **CL** penalties (B.3). No global novelty.

#### 12.2 · Context extensions & policy‑level characteristics (non‑kernel)

The following **context‑local** characteristics remain available but are **not** part of the kernel nucleus; use them as **derived** or **policy** measures:

* **ReframeDelta** — change in the **problem frame** that improves solvability (episteme‑pair; ordinal).
* **Compositionality** — degree of **re‑use and new relations** among parts (artifact; boolean + structure score).
* **Transferability\@X** — portability to **Context X** via a Bridge (artifact; ordinal + CL penalty).
* **DiversityOfSearch** — breadth of **approach classes tried** (work set; count/rate).
* **Time‑to‑First‑Viable** — elapsed time to first **Use‑Value = Pass** (work; duration).
* **Risk‑BudgetedExperimentation** — planned vs realized exploration share (workplan vs work; ratio; policy gate).

> **Compatibility note.** This split removes duplicate “core lists” and aligns C.17 with **B.5.2.1 NQD** and **C.16/A.17–A.18**: the **kernel nucleus** captures creativity *qualities*; the items above instrument **process/policy** or **portfolio shaping**.

### 12.3 · Scale choices (CSLC discipline)

For each characteristic, **declare the scale** explicitly (nominal / ordinal / interval / ratio). **Do not** average ordinal scores; fold with medians or distributional summaries. Choose **units** (when applicable) and **coordinate** semantics (e.g., what “distance” means).

* *Novelty\@context.*
  Coordinate = `1 − max_similarity(candidate, corpus)` with a declared encoder (text, graph, CAD). Unitless in \[0..1]. Document encoder & corpus freeze (`A.10` Evidence Graph Ref).
* *Use‑Value.*
  `Pass` iff **acceptanceSpec** (from `U.Service` or Decision KPI) is met from **Work** evidence; else `Partial`/`Fail`. For scalar KPIs, publish mean ± CI and the acceptance threshold; predicted values carry error bars and are updated post‑run.
* *ConstraintFit.*
  Ratio = satisfied / declared **must** constraints. Constraints are `Norm‑CAL` rules; **count only declared** ones (no unspoken “norms”).


## 12.4 · Metric templates (normative kernels + manager‑ready variants)

 **Template syntax (MM‑CHR):**
`U.DHCMethod { name, context, carrierKind, definition, unit?, scale, EvidencePin, acceptanceHook? }`
*Note:* Data instances carry `DHCMethodRef` pointing to this template.

### 12.4.1 · Templates (kernel definitions)

1. **`MT.Novelty@context`**

* **carrierKind:** Artifact|WorkOutput.
* **definition:** `1 − max_sim(encode(x), encode(y))` over y in **ReferenceSet**@Context.
* **scale:** ratio \[0..1].
* **EvidencePin:** `{ReferenceSetId, EncoderId, Version}`; frozen by `A.10`.
* **notes:** Publish encoder & corpus drift in RSCR.

2. **`MT.Use‑Value`**

* **carrierKind:** Work (fulfillment) → artifact (decision memo).
* **definition:** Evaluation of an outcome against a declared **objective/criterion** for the current context (or predicted value with explicit model & error).
* **scale:** ordinal {Fail, Partial, Pass} or scalar KPI.
* **EvidencePin:** links to `U.Work` that **fulfilsService\`**; cite acceptanceSpec edition.

3. **`MT.ConstraintFit`**

* **carrierKind:** Work / Artifact.
* **definition:** `|{c∈C_must : pass(c)}| / |C_must|` within the **MethodDescription** scope; optional weighting by criticality allowed if declared.
* **scale:** ratio \[0..1].
* **EvidencePin:** constraint list from **Norm‑CAL**; checks from Work telemetry.

4. **`MT.ReframeDelta`**

* **carrierKind:** Episteme pair (ProblemStatement v0→v1).
* **definition:** Categorise frame change as {None, Local, BoundaryShift, Systemic}; **justify** with a Scope diff (`A.2.6 U.ContextSlice` delta) and causal map simplification.
* **scale:** ordinal 0–3.
* **EvidencePin:** diff artifact + Bridge notes if Cross‑context.

5. **`MT.DiversityOfSearch`**

* **carrierKind:** Work set (episode).
* **definition:** Count of **distinct approach classes** tried (domain‑local typology) / time.
* **scale:** count; derived rate.
* **EvidencePin:** tagged Work items; typology lives in the Context glossary.

6. **`MT.Compositionality`**

* **carrierKind:** Artifact.
* **definition:** set aggregator (Compose‑CAL) of reused components ≥ K and presence of novel relation among ≥ 2 parts.
* **scale:** boolean + secondary “structure score” (e.g., depth or edge novelty).
* **EvidencePin:** component graph + provenance of parts.

7. **`MT.Transferability@X`**

* **carrierKind:** Artifact.
* **definition:** Applicability in target **Context X** via a **Bridge**; report **CL** and residual scope slice.
* **scale:** ordinal {not portable, portable with loss, near‑iso}; record CL (0–3).
* **EvidencePin:** Bridge id + pilot Work in X.

8. **`MT.Time‑to‑First‑Viable`**

* **carrierKind:** Work episode.
* **definition:** elapsed wall‑clock to first `UsefulnessEvidence = Pass`.
* **scale:** duration.
* **EvidencePin:** first passing `U.Work` id.

9. **`MT.Risk‑BudgetedExperimentation`**

* **carrierKind:** WorkPlan vs Work.
* **definition:** `(Planned exploratory spend) / (Allowed risk budget)` and realised counterpart; flag **overrun**.
* **scale:** ratio + policy gate (pass/fail).
* **EvidencePin:** WorkPlan ledger vs `WorkLedger`.

### 12.4.2 · Manager’s quick checks (plain‑language adapters)

* **Novelty** without a **frozen corpus** is **storytelling**—freeze corpus, fix encoder, then score.
* **Use‑Value** without a **consumer‑facing acceptance** is a **proxy**—bind to a **Service** or explicit Objective.
* **Diversity** counts **approach classes**, not color‑swap variants—publish your typology.

## 13 · Novelty & transfer are **context‑local** (Bridges mandatory)

**Rule N‑1 (Locality).** `Novelty@context` is defined **only** within its `U.BoundedContext`. **Never** compare scores across Contexts without an **Alignment Bridge** (F.9).

**Rule N‑2 (Directional mapping).** A Bridge may assert a **directional** substitution (e.g., *Novelty\@DesignLab → Novelty\@Manufacturing* with CL = 2, **loss:** aesthetics encoder absent). Reverse mapping is **not** implied.

**Rule N‑3 (Penalty to R, not to G).** Cross‑context novelty **does not** change scope **G**; it **reduces R** (reliability) by the **CL penalty** (B.3), unless validated by pilot Work in the target Context.

**Practical pattern.** Publish novelty **with its Context tag** and—when reused—attach the **Bridge id** and target‑context **pilot** outcomes.

---

## 14 · Anti‑Goodhart guard (use creativity metrics safely)

> **Goodhart’s Law:** “When a measure becomes a target, it ceases to be a good measure.” — We bake in **guards** so creativity scoring **improves** outcomes instead of gaming them.

### 14.1 · Guard‑rails (normative)

* **G‑1 Paired appraisal.** **Never** assess **Novelty** in isolation; pair it with **Use‑Value** or **ConstraintFit** to avoid proxy myopia
* **G‑2 Frozen references.** Novelty requires **frozen corpus + encoder**; changes create a **new edition** and **RSCR** rerun. Portfolio/selection heuristics are **policy-level** (see **C.19**); do not “reward” Illumination beyond its role as a report-metric.
* **G‑3 Time‑lag sanity.** Include a **post‑fact check** (e.g., 30–90‑day retention or cost‑to‑serve delta) before celebrating “creative wins.”
* **G‑4 Exploration budget.** Tie **DiversityOfSearch** to **Risk‑BudgetedExperimentation**; flag overspend.
* **G‑5 No ordinal averaging.** Do not average **ordinal** scales; use distributions/medians or convert only under declared models.

### 14.2 · Conformance Checklist — **CC‑C17‑M (metrics & guards)**

| ID             | Requirement                                                                                                                            | Practical test                                                              |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **CC‑C17‑M.1** | Each metric instance **MUST** cite its **Context**, **edition**, and **evidence hooks** (corpus/encoder, acceptanceSpec, constraint set). | Scorecard lists `ContextId`, `Edition`, and hook ids resolvable via `A.10`. |
| **CC‑C17‑M.2** | **Novelty** scores **MUST NOT** be used to approve Work without a **paired gate** (**Use‑Value** **or** **ConstraintFit**).               | Find decisions referencing novelty; check co‑gate present.                  |
| **CC‑C17‑M.3** | Cross‑context reuse **MUST** cite a **Bridge** and record **CL**; **R** is penalised accordingly.                                         | Scorecards with foreign Context tag lacking Bridge → **fail**.                 |
| **CC‑C17‑M.4** | Ordinal metrics **MUST** be summarised with medians/distributions, not means, unless a declared model justifies numeric treatment.     | Reports using a mean on ordinal without model → **fail**.                   |
| **CC‑C17‑M.5** | Metric templates **MUST** be versioned; changing encoder, reference set, or acceptanceSpec **creates a new edition**.                  | Diff shows changed hooks without edition bump → **fail**.                   |

---

## 15 · Worked mini‑cases (engineer‑manager focus)

> **All names are context‑local; bridges and editions are explicit.**
> We show **(a)** what is measured, **(b)** who acts, **(c)** what is accepted, and **(d)** how evidence flows.

### Case A — Hardware ideation sprint (manufacturing design)

* **Context.** `DesignLab_2026`.
* **Objective.** Reduce fastener count by ≥ 30 % without tooling changes.
* **MethodDescription.** “Morphological matrix ideation v2.”
* **Work.** 1‑day sprint, 6 sessions.
* **Metrics.** `Novelty@context` (encoder: CAD‑graph v1; ReferenceSet: in‑house assemblies), `ConstraintFit` (no‑tooling‑change), `Use‑Value` (acceptance: Pass if sim shows ≤ +5 % assembly time).
* **Roles.** Performers = design cell (#TransformerRole); Observer = methods coach (#ObserverRole ⊥).
* **Outcome.** 22 candidates; 4 **Pass** usefulness; best `Novelty`=0.41 with **100 %** constraints respected; `Time‑to‑First‑Viable` = 3 h 40 m.
* **Evidence.** Scorecard episteme holds metrics; links to Work ids; acceptance tied to internal **Service** “Design‑for‑Assembly Simulation”.

**Manager’s read.** “We didn’t just produce ‘novel’ shapes; 4 passed the sim and respected constraints, within the day.”

---

### Case B — Data‑science hypothesis generation (health analytics)

* **Context.** `Cardio_2026`.
* **Objective.** Find a new risk factor candidate for readmission (< 30 days).
* **MethodDescription.** “Causal discovery v3 + clinician review.”
* **Metrics.** `DiversityOfSearch` (approach classes: feature ablation, IVs, DAG‑learners), `Novelty@context` (text encoder over prior hypotheses), `Use‑Value` (AUROC uplift ≥ 0.03 on hold‑out), `Transferability@Hospital_B` (Bridge CL=2).
* **Roles.** SRE pipeline (#ObserverRole) computes metrics; clinicians (#ReviewerRole) set acceptance; data squad (#TransformerRole) performs experiments.
* **Outcome.** Two candidates; one meets AUROC uplift; **Transferability** requires follow‑up (CL penalty).
* **Evidence.** Episteme bundle: model cards, hold‑out plots, Bridge note.

**Manager’s read.** “One candidate works **here**; plan a pilot at Hospital B (we recorded CL=2).”

---

### Case C — Product squad reframing (software UX)

* **Context.** `SaaS_Onboarding_2026`.
* **Objective.** Reduce time‑to‑value (TTV) by 20 %.
* **MethodDescription.** “JTBD interviews + onboarding flow experiments.”
* **Metrics.** `ReframeDelta` (BoundaryShift: split onboarding into ‘job setup’ and ‘first result’), `Use‑Value` (TTV ‑22 % on A/B), `Risk‑BudgetedExperimentation` (within cap), `Compositionality` (reuse of existing workflow widgets).
* **Roles.** UX researcher (#ObserverRole), squad (#TransformerRole), product ops (#ReviewerRole).
* **Outcome.** Frame changed; TTV target passed; experiments within budget.
* **Evidence.** Reframing episteme with Scope diff + A/B report.

**Manager’s read.** “We changed the problem frame and proved the value drop—within risk limits.”

---

### What these cases illustrate (tie‑backs)

* **Locality.** All novelty/usefulness claims are **Context‑tagged**; Cross‑context steps use **Bridges** with **CL**.
* **Dual‑gate.** Novelty never acts alone; usefulness/constraints co‑gate decisions.
* **SoD & Evidence.** Observers are **separate** from performers; metrics live on **epistemes** with **frozen hooks**; Work proves fulfillment.


## 16. Working examples

#### 16.1 · Software (algorithmic/architectural ideation)

**Kernel characteristics (↑/↓/gate).**
Novelty↑ (algorithmic / compositional), Use‑Value↑ (targeted user/job metric), ConstraintFit=gate (resource/latency envelope), Cost‑to‑Probe↓ (hours to runnable spike), Evidence‑Level↑ (tests/benchmarks confidence), Option‑Value↑ (paths unlocked), RegretRisk↓ (blast radius if wrong).

**Priors.**

* Novelty prior **skeptical** beyond nearest known family (discount by conceptual distance).
* Evidence prior at **L0** (B.3) until benchmarks exist; regression tests act as **ObserverRole** evidence.

**Context card (one screen).**

* Γ\_bundle: Cost = sum; ConstraintFit = AND; Novelty = subadditive; Evidence = min (chain) / SpanUnion (indep).

#### 16.2 · Hardware (mechanical/electro‑mechanical concepting)**

**Kernel characteristics.**
Novelty↑ (principle/material), Use‑Value↑ (performance delta), ConstraintFit=gate (manufacturability window), Time‑to‑Probe↓ (bench jig), Cost‑to‑Probe↓, SafetyRisk↓ (hazard), Evidence‑Level↑ (bench data), Option‑Value↑ (platform reuse).

**Priors.**

* SafetyRisk has **WLNK** priority (R must cover hazard chain).
* ConstraintFit must pass **manufacturing gate** before frontier inclusion.

**Context card.**
* Γ\_bundle: Hazard = max; ConstraintFit = AND; Cost = sum+coupling; Evidence = min on chain; Scope via **WorkScope** (A.2.6).

#### 16.3 · Policy design (rules/standards/programs)

**Kernel characteristics.**
Novelty↑ (institutional), Use‑Value↑ (measurable social/operational effect), ConstraintFit=gate (legal/operational), Cost‑to‑Probe↓ (pilot), Evidence‑Level↑ (triangulated), EthicalRisk↓ (D‑cluster), Option‑Value↑ (coalitions/pathways), Scope (ClaimScope G) explicit.

**Priors.**
* EthicalRisk uses **status‑only** eligibility conditions; Evidence aging (decay) is **fast**; cross‑context Bridges carry **CL** penalties.

**Context card.**
* Γ\_bundle: EthicalRisk = max; ConstraintFit = AND (legal & operational); Cost = sum; Evidence = min/SpanUnion; Scope = ClaimScope (A.2.6).

## 17 Consequences & fit (for engineer‑managers)

* You can **reason on paper** about creativity: compare with **dominance**, pick along a **frontier**, and steer exploration with a few **policy characteristics**.
* Changes to the space (**scales, eligibility conditions, operators**) are handled by **RSCR**, so decisions are **explainable over time**.
* The **Context handbooks** are a **thinking OS**: one screen to start ideating without importing tool stacks or management playbooks.

## 18 Relations

* **Builds on**: B.1 Γ‑algebra (WLNK/COMM/IDEM/MONO), B.3 Trust & Assurance (F–G–R, CL), A.2.6 USM (Claim/Work scopes), A.10 Evidence Graph Referring.
* **Coordinates with**: A.2 Role suite (Observer/Evidence roles for probes), A.15 (Work & plans for probes), C.16 MM‑CHR (scale polarity & units). **C.18 NQD-CAL** (generation/illumination operators Γ_nqd.*) and **C.19 E/E-LOG** (policies, selection, and portfolio rules). This CHR remains measurement-only.
* **Defers to**: F.9 Bridges for Cross‑context transfers; D‑cluster for ethical/speech‑act gates.

## 19 Quick reference cards (tear‑out)

* **Dominance test**: apply **signs** + **eligibility conditions** + **trust**; then partial order.
* **Frontier use**: **show frontier** + **name the lens** that picked your choice.
* **Portfolio policy**: keep `ExploreShare` and `WildBetQuota`; set `BackstopConfidence`; rebalance on cadence.

## 20 · Conformance Checklist (pattern‑level, normative)

> *Pass these and your CS modelling remains a thinking architecture, not a team‑management manual.*

**CC‑C17‑1 (context‑local CS).**
Every **CreativitySpace** (the characteristic set where ideation and selection are measured) **MUST** be defined *inside one* `U.BoundedContext`; all characteristics and their scales are local to that Context. (Bridges with CL penalties are required across Contexts; see §C.17.16.)

**CC‑C17‑2 (Characteristics, not “characteristics”).**
Each CS dimension **SHALL** be a named **Characteristic** per **MM‑CHR**, with kind (`qualitative`, `ordinal`, `interval`, `ratio`, or `set‑valued`), unit/scale, polarity, and admissible operations. No free‑floating coordinates. (A.CHR‑NORM / A.CSLC‑Kernel.)

**CC‑C17‑3 (Profile ≠ plan).**
A **Profile** is a *state description over characteristics* (what the option *is* in CS); a **Plan** or **Method** is *how you will act*. Never encode choices or schedules into the profile.

**CC‑C17‑4 (Portfolio = set + rule).**
A **Portfolio** is a set of candidate profiles **plus** a selection rule (objective + constraints) declared *in the same Context*. Presenting only a scatterplot is non‑conformant.

**CC‑C17‑5 (Dominance operator well‑typed).**
A dominance claim **MUST** name the **characteristic subset and polarity** under which it is evaluated. Dominance on incomparable scales (or mixed polarities without explicit transformation) is invalid.

**CC‑C17‑6 (Frontier from rule, not from taste).**
A **Frontier** (Pareto or constraint‑bound) **SHALL** be computed from the declared selection rule; drawing a “nice hull” by eye fails conformance.

**CC‑C17‑7 (Search–Exploit as **dynamics**, not policy dogma).**
Exploration/exploitation **MUST** be expressed as a **dynamics on the portfolio measure(s)** (e.g., exploration share as a function of marginal value of information), *not* as a prescriptive budget recipe. (Design‑time statements belong to Decsn‑CAL; see §C.17.16.)

**CC‑C17‑8 (Evidence Graph Referring for scores).**
Any numeric score in a profile **MUST** cite its **MeasurementTemplate** (MM‑CHR) and the **observation/evaluation** that yielded it. No anonymous numbers.

**CC‑C17‑9 (Separable uncertainty lanes).**
Keep **aleatory** vs **epistemic** uncertainty separate on characteristics; their combination rule **MUST** be stated (e.g., interval arithmetic, conservative bound).

**CC‑C17‑10 (Time is explicit).**
Comparisons across iterations **MUST** state `TimeWindow` (snapshot window) and whether *drift* or *refit* occurred (§C.17.14). “Latest” is not a time selector.

**CC‑C17‑11 (No proxy collapse).**
If a composite “creativity index” is used, its **aggregation algebra** (weights, monotone transforms) **MUST** be declared; the primitive characteristics remain queryable.

**CC‑C17‑12 (Work stays on Work).**
Resource/time actuals and run logs live on `U.Work`; CS never carries actuals. We reason **about** profiles/portfolios; we do not audit operations here.


### 21 · Worked‑Context Handbooks (concept cards, not runbooks)

> *Each Context publishes one page per card. These are **thinking kernels**: priors, objectives, admissible characteristics, and example transforms. No staffing, no process charts.*

**(a) Kernel Card — “What is a creative win here?”**

* **Context:** `<Context/Edition>`
* **Purpose Characteristic(s):** what “win” means (e.g., *Novelty*, *Usefulness*, *Adoptability*), with polarity and admissible ops.
* **Constraint Characteristics:** *Risk*, *Cost of change*, *Time to learn*, etc.
* **Objective** *(Decsn‑CAL pointer)*: Maximise `<purpose>` subject to declared constraints.
* **Frontier Rule:** Pareto over `{purpose ↑, risk ↓, cost ↓, time ↓}`.
* **Evidence Hooks:** which observations/evaluations populate each characteristic.

**(b) Priors Card — “What we believe before seeing data.”**

* **Default priors** on uncertainty for each characteristic (e.g., Beta for adoption probability).
* **Bridge policy:** minimal CL acceptable for imported profiles.
* **Exploration prior:** initial exploration share as a function of prior entropy.

**(c) Objective Variants Card — “Admissible objective shapes.”**

* Catalog the *few* objective forms this Context allows (lexicographic tie‑break, ε‑constraint, max‑min fairness), with **didactic pictures** of their frontiers.
* State when to switch objective (e.g., during bootstrapping vs exploitation).

**(d) Ready‑to‑use transforms** *(MM‑CHR aligned)*

* Monotone maps (e.g., log utility), normalizations, ordinal→interval “do & don’t” (only with evidence of order‑to‑interval validity).
* **Forbidden transforms** list (e.g., averaging ordinal ranks).

These cards are *conceptual fixtures*; **Tooling** may implement them, **Pedagogy** may teach them, but **C.17** only standardises their content as **thinking affordances**.

### 22 · Placement sanity‑check across the pattern language** *(avoid scope creep)

* **MM‑CHR (C.16):** defines **Characteristic/Scale/Unit/Measure** and the *characterisation discipline*. **All** CS dimensions live there; C.17 **uses** them, never re‑defines scales.
* **A.CHR‑SPACE (A.19):** exports **CharacteristicSpace & Dynamics hooks**; C.17 is a **Contexted specialisation** for creative reasoning (profiles/portfolios/selection).
* **Decsn‑CAL (C.11):** hosts **objective functions, constraints, preference orders, utility proofs**, and the **search–exploit dynamics** as decision policies. C.17 only **names** the hooks (objective, rule), keeps policy math out.
* **KD‑CAL (C.2) & B.3 (Trust):** carry **evidence provenance**, **assurance** and **congruence penalties (CL)** for Cross‑context reuse. C.17 requires anchors; it does not invent confidence calculus.
* **Compose‑CAL (C.13):** governs **set/union/slice** aggregation; the portfolio set is a **Γ\_m.set** over profiles; frontier is derived **without** ad‑hoc geometry.
* **B.4 Canonical Evolution Loop:** where *Run→Observe→Refine→Deploy* sits. C.17 supplies the **view** in which refinement is judged.

**Out of scope here:** team staffing, budgeting workflows, data‑governance procedures, ticket states, any “how to manage people”. This pattern organises **thought**, not **teams**.

### 23 · Anti‑patterns & canonical rewrites (conceptual hygiene)

1. **characteristic‑speak.** “Along the novelty characteristic…” → **Rewrite:** “Along the **Novelty characteristic** (ordinal; higher is better)…”.
2. **Pretty hulls.** Drawing a convex hull and calling it a frontier → **Rewrite:** compute Pareto under declared characteristic polarities.
3. **Ordinal arithmetic.** Averaging ranks or Likert values → **Rewrite:** either treat as **ordinal** and use **order‑safe** operators, or justify an interval mapping via MM‑CHR evidence.
4. **Proxy tyranny.** Single composite index driving choice unseen → **Rewrite:** publish **primitive characteristics**, index formula, and sensitivity.
5. **Policy‑as‑math.** “10% wild bets” as a rule → **Rewrite:** declare an **exploration dynamics** tied to value‑of‑information; if keeping a heuristic, label it as such.
6. **Global meaning.** Porting a profile from another Context by name → **Rewrite:** attach a **Bridge** with CL and loss notes; adjust trust, not scales.
7. **Plan‑profile blur.** Putting milestones into profiles → **Rewrite:** move schedules to `U.WorkPlan`; keep CS for *how options compare*, not *how to execute*.

### 24 · Minimal didactic cards (one screen each)

**(1) Profile Card**

* **Option id & Context**
* **Characteristics table** (value, unit/scale, uncertainty split)
* **Evidence Graph Ref** (Observation/Evaluation ids)
* **Notes** (bridges used, CL penalties)

**(2) Portfolio‑with‑Rule Card**

* **Set of candidate profiles (refs)**
* **Objective & constraints** (Decsn‑CAL pointer)
* **Dominance subset** & **Frontier snapshot** (with TimeWindow)
* **Delta vs previous** (entered/exited/moved)

**(3) Search–Exploit Card** *(conceptual)*

* **Exploration share** as function of **marginal VOI** (symbolic)
* **Update cadence** (TimeWindow policy)
* **Stop conditions** (e.g., VOI below threshold; risk bound reached)

**(4) RSCR Summary Card**

* **What changed?** (refit/Δ±)
* **Sentinels status**
* **Frontier churn**
* **Bridge CL drift**

These cards are **thinking scaffolds**; they do not prescribe org process.

### 25 · Consequences (informative)

| Benefit                    | Why it matters                                                                                                                    |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **context‑local rigour**      | Creative comparison is made decidable *where meaning lives*; Cross‑context reuse is explicit and penalised only in trust, not scale. |
| **Frontier honesty**       | Decisions rest on declared characteristics and polarities; frontiers follow rules, not taste.                                     |
| **Temporal comparability** | RSCR prevents silent drift; “better/worse” claims retain meaning over iterations.                                                 |
| **Method independence**    | Any tooling can implement the cards; C.17 remains a conceptual API for thought.                                                   |

**Trade‑offs:** upfront ceremony (declare characteristics, polarity, TimeWindow) and disciplined bridges. The payoff is comparability and explainability.

### 26· Open questions (non‑normative, research hooks)**

* **Information geometry of CS:** can certain Contexts justify canonical distance metrics across characteristics without violating MM‑CHR parsimony?
* **Multi‑agent exploration:** how to couple individual CS frontiers into a *co‑exploration* equilibrium without importing team governance?
* **Learning‑to‑rank vs measurement:** what minimal evidence suffices to treat an ordinal characteristic as interval for the purpose of frontier estimation?


## C.18 — NQD‑CAL — Open‑Ended Search Calculus \[A]

**Status.** Architheory specification (**CAL**). Exports `Γ_nqd.*` operators for open‑ended, illumination‑style generation. **ΔKernel = 0** (no kernel primitives added). *Minting note:* this CAL **does not mint** new U‑types; it defines **CAL‑records** that MAY alias to registered U‑types where present via **E.10/UTS**.

**Depends on.** A‑kernel (A.1–A.15), **MM‑CHR** (C.16) for measurements, **KD‑CAL** for similarity/corpora, **Sys‑CAL** for carriers, **Decsn‑CAL** (objectives; advisory), **Compose‑CAL** (set aggregation; advisory).

**Coordinates with.** **B.5.2.1** (binding), **C.17 Creativity‑CHR** (characteristics & scales), **C.19 E/E‑LOG** (policies: emitter selection, explore/exploit).

**Exports (CAL; no U‑type minting here).**
 - Records: `NQD.DescriptorMap` (alias of `U.DescriptorMap` if minted), `NQD.NQDArchive` (alias of `U.NQDArchive`), `NQD.Niche`, `NQD.ArchiveCell`, `NQD.EmissionSeed?`, `U.EmitterPolicyRef`, `U.InsertionPolicyRef`, `U.IlluminationSummary`, and `NQD.CandidateSet` (alias of `Set<U.Hypothesis>`).

### Problem frame
Open‑ended search (NQD) equips FPF with illumination‑style generation and Pareto/portfolio selection in multi‑criteria, partially ordered spaces; it feeds G.5 without scalarising ordinal or mixed‑scale characteristics.

### Problem
Without a disciplined NQD calculus, contexts (a) conflate illumination gauges with dominance, (b) lose reproducibility due to undeclared DescriptorMap/DistanceDefRef.editions, and (c) perform illegal aggregations across scales.

### Forces
• Posets vs. scalarisation — selectors must return sets (Pareto/archive) rather than illegal weighted sums across mixed scales.
• Exploration vs. exploitation — emitters must adapt while preserving provenance and editioning.
• Gauge vs. objective — Illumination (coverage/QD‑score) informs health but is not a dominance characteristic by default.
• Reproducibility vs. adaptivity — budgets, ε, K, and InsertionPolicy must be edition‑tracked.

### Solution
Provide Γ_nqd.* operators and U.Types for DescriptorMap, Archive/Niche, policies, and illumination gauges; bind measurement legality to MM‑CHR and policy control to E/E‑LOG. (Exports/Type notes/Operator specs below are normative parts of this Solution.)

- Operators (Γ):
  - `Γ_nqd.generate(seed?, EmitterPolicyRef, Budget, DescriptorMapRef, QualityMeasuresRef, NoveltyMetricRef, CoverageGrid, CellCapacity K=1, EpsilonDominance ε=0, DedupThreshold?, InsertionPolicyRef?) → CandidateSet<U.Hypothesis>`
  - `Γ_nqd.updateArchive(Archive, CandidateSet, InsertionPolicyRef?) → Archive'`
  - `Γ_nqd.illuminate(Archive) → IlluminationSummary{coverage, QD-score, occupancyEntropy, filledCells}` (reporting gauge only; not a dominance characteristic unless a policy explicitly promotes it).
  - `Γ_nqd.selectFront(Archive|CandidateSet, characteristics={Q components, Novelty@context, ΔDiversity_P, …}) → ParetoFront`

**Type notes.**
- `U.DescriptorMap (Tech; twin‑labelled Plain) : Hypothesis → ℝ^d` (declares encoder, invariances, version, **CharacteristicSpaceRef**). Publish Tech/Plain per **E.10**; declare `DescriptorMapRef.edition` and `DistanceDefRef.edition`. **Dimensionality rule.** **Require `d≥2` only when QD/illumination surfaces are active**; for non‑QD contexts `d≥1` is lawful.
- `NQD.CandidateSet` ≡ `Set<U.Hypothesis>` with attached per‑item vectors `{Q_i, N_i, D_i:=ΔDiversity_P, S_i?, provenance_i}`.
- `U.NQDArchive` holds per‑cell elites and genealogy refs; context‑local.
- `U.Niche` is a region in CharacteristicSpace (grid bucket / CVT centroid / cluster).
- `U.EmitterPolicyRef` points to a named policy in **C.19 E/E‑LOG**.
- `U.InsertionPolicyRef` — named archive‑update policy (e.g., `replace_if_better | replace_worst | bounded_age | bounded_regret`); versioned.
- `U.IlluminationSummary` is a **gauge** over `Diversity_P` (see C.17), not a dominance characteristic.

**Operator specs (normative).**
- `Γ_nqd.generate(...)` SHALL:
  (a) respect **Budget**,  
  (b) compute `{Q_i}` (vector), `N_i` (Novelty@context), `D_i := ΔDiversity_P(h_i | Pool)` under the same CharacteristicSpace & TimeWindow as the Pool, and optional `S_i` (Surprise),
  (c) deduplicate by `DedupThreshold` in CharacteristicSpace,  
  (d) record `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `EmitterPolicyRef`, `ε`, `K`, `Seeds`, and genealogy references (parent/seed ids) to enable replay and selection auditing.
- `Γ_nqd.updateArchive` SHALL apply local competition per cell (keep up to K elites), preserve genealogy, and **enact the declared `InsertionPolicyRef`**; default is `replace_if_better` with deterministic tie‑breakers.
- `Γ_nqd.illuminate` SHALL return coverage and QD‑score computed against the declared grid and archive edition.
- `Γ_nqd.selectFront` SHALL compute the (ε‑)Pareto front over the declared characteristics; **Illumination** is excluded by default (report‑only).  

**Pipeline:** apply **Eligibility (ConstraintFit=pass)** → **Dominance (default set from C.19; by default `{Q components}` only)** → **Tie‑breakers (`Novelty@context`, `ΔDiversity_P`, `Surprise`; `Illumination` gauge)**.
**Pure academic QD-mode:** Contexts MAY elect a _pure‑QD_ mode (dominance on `Q` only; `N/ΔD` used via archive occupancy and tie‑breakers). Any deviation SHALL be declared by policy id and recorded in provenance.

**Reproducibility & editions.** Each call SHALL emit provenance sufficient for replay: `{DHCMethodRef.edition, DescriptorMapRef.edition, EmitterPolicyRef (params), **InsertionPolicyRef**, DedupThreshold?, ε, K, Seeds, TimeWindow}`.
Telemetry hook: whenever IlluminationSummary increases (Δcoverage>0 or ΔQD‑score>0), the Context SHALL emit a Telemetry(PathSlice) record that cites {EmitterPolicyRef, DescriptorMapRef.edition, DistanceDefRef.edition, InsertionPolicyRef?, TimeWindow}. (Aligns with G.6/G.7/G.11 portfolio/edition constraints.)

**Measurement alignment.** `Novelty@context`, `Use‑Value (ValueGain)`, `Surprise`, `Diversity_P` SHALL be measured per **C.17** (MM‑CHR templates). **IlluminationSummary** is a gauge over `Diversity_P` (coverage/QD‑score); when CharacteristicSpace includes domain‑family cells, publish grid id and FamilyCoverage, plus **DescriptorMapRef.edition/DistanceDefRef.edition**.
.

### Conformance Checklist
- **C18‑1** Declare `DescriptorMap` (encoder, invariances, corpus edition) before generation.
- **C18‑1b** When used in F/G triads, DescriptorMap SHALL declare a domain‑family coordinate (grid/cells) and reference an F1‑Card::DistanceDefRef & δ_family.
- **C18‑1c**  When a domain‑family coordinate is declared, the Context SHALL compute and publish **AliasRisk** for each front/portfolio emission, together with the dSig collision rule and the policy id. AliasRisk is computed against `U.DomainDiversitySignature (dSig)`; **the DescriptorMap SHALL publish**: (i) `collisionRuleId` (near‑duplicate threshold, e.g. “≥3 characteristics equal”),  (ii) `dSigSource` pointers used for coding the five characteristics. The collision rule and formula **MUST** be part of `DescriptorMap` provenance (see **Creativity‑CHR**, Heterogeneity Characterisation).
- **C18‑2** Record `EmitterPolicyRef` (policy id from C.19) and parameter set.
- **C18‑3** Compute `D = ΔDiversity_P(h | Pool)` under the same DescriptorMap & TimeWindow as the Pool (see C.17).
- **C18‑4** Exclude Illumination from dominance unless policy explicitly promotes it.
- **C18‑5** Keep `Use‑Value` separate from assurance scores; do not alter `F/G/R` semantics (see B.3, C.17 §Use‑Value).
- **C18‑6** Emit full provenance; thinning after front computation MUST be recorded.
- **C18‑7** Before computing any front, apply **ConstraintFit = pass** as a hard eligibility filter.

**Defaults.** Normative defaults **live in C.19 (EmitterPolicy)** and are **not restated** here. Minimum provenance remains: `DescriptorMapRef.edition` and `DistanceDefRef.edition`, `DHCMethodRef.edition`, `EmitterPolicyRef`, `InsertionPolicyRef`, `TimeWindow`, `Seeds`, `DedupThreshold?`; also record `FamilyCoverage/MinInterFamilyDistance`.

**Didactic quickstart (Context).**
1) Pick 2–4 Quality coordinates and a simple DescriptorMap (2–4 dims).  
2) Set defaults: `K=1`, `ε=0`, a conservative `EmitterPolicy`.  
3) Run `Γ_nqd.generate` to fixed Budget; inspect the front; log coverage (IlluminationSummary).  
4) Apply abductive plausibility filters; promote prime hypothesis to L0.

### Archetypal Grounding
**System.** Legged‑robot gait exploration: Q = forward speed & energy efficiency (ratio), D = morphology/coordination descriptors (ℝ^d); Archive = CVT grid; Illumination gauges coverage without entering dominance.
"**Episteme.** SoTA palette synthesis: Q = Use‑Value proxies per C.17 (ratio/interval as legal), D = method‑family niches; publish DescriptorMapRef.edition and DistanceDefRef.edition for reproducible fronts.

### Bias‑Annotation
Lexical firewall and notation independence apply; no vendor/tool tokens; ordinal characteristics never averaged; illumination treated as gauge unless a policy promotes it. (E.5.1, E.5.2, C.16)

### Consequences
• Portfolio honesty (no forced scalarisation). • Reproducible exploration (editioned maps/policies). • Healthy diversity signals via gauges.

### Rationale
Post‑2015 Quality‑Diversity (MAP‑Elites & successors) demonstrates illumination efficacy; NQD‑CAL captures these ideas while preserving MM‑CHR legality and LOG governance.

### Relations
Builds on: C.16, C.2. Coordinates with: B.5.2.1 (binding), C.17, C.19, G.5, G.6, G.11.

### C.18.1 — **SLL — Scaling‑Law Lens (binding)** \[A]

**One‑screen purpose (manager‑first).**
Make **generation/selection** scale‑savvy: at the level of **conceptual descriptors**, declare (a) **which monotone knobs** we would scale, (b) the **ScaleWindow** over which we claim behaviour, and (c) the **elasticity class** we observed—**without** imposing numeric fits or vendor tools at Core level. This surfaces knees early and keeps comparisons lawful and fair across families. (Parity is handled by **G.9**; illumination remains a **gauge** unless promoted by policy.)  

**Builds on.** C.16 (MM‑CHR), C.17 (Creativity‑CHR), C.18 (NQD‑CAL); advisory: C.5 (Resrc‑CAL).
**Coordinates with.** C.19 (E/E‑LOG), G.5 (Selector & Registry), G.9 (Parity Harness), G.10 (Shipping), G.11 (Refresh‑Telemetry), C.24 (Agent‑Tools‑CAL).
**Keywords.** scaling law; **Scale Variables (S)**; ScaleWindow; knee; diminishing returns; **iso‑scale parity**; **gauge mapping**; **scale‑probe**; **DoE** (design‑of‑experiments); segmented regression; knee detection.

#### 1) Problem frame

Teams often say a method “**scales**” without disclosing **which resources**, **across what window**, and **how** outcomes respond (convex rise → knee → plateau). Without that, parity is skewed (unequal budgets, unmatched windows), coverage/illumination report-metrics leak into dominance, and “knees” are found late. SLL supplies a notation‑independent **lens** to make scale behaviour explicit and comparable. 

#### 2) Problem

Omitting **Scale Variables** and the comparison window causes: (i) **unfair parity** (compute/data/FoA mismatched), (ii) **illumination/coverage report-metric  creep** into dominance by default, (iii) late detection of knees and budget waste. **G.9** already forbids scalarising mixed scales and mandates equal **FreshnessWindows**/**pinned editions**; SLL complements this with **ScaleWindow** & elasticity. 

#### 3) Forces

Notation independence vs useful scaling heuristics; local context vs cross‑context generality; **gauges vs objectives** (illumination stays a gauge unless policy promotes it); early exploration vs reproducible policy.

#### 4) Solution — *binding lens for generator/selector profiles* (normative)

**4.1 Types (aliases; ΔKernel = 0).**
`SLL.Profile` is an **annotation** on a `MethodFamily/Generator` or a `Selector` profile; **no new U.Types** are minted (LEX discipline). 

**4.2 Fields (conceptual descriptors).**

* **S — Scale Variables.** Minimal set of **monotone knobs** for the Context: `compute` (steps/tokens/FLOPs/time/energy), `data` (size/quality), `model capacity` (params/branches), `iteration budget`, **`freedom‑of‑action (FoA)`**/**environment richness**, etc. Declare **units** via **Resrc‑CAL** and bind to a **ScaleWindow**. Where training/inference trade, **name the phase** the claim concerns.
* **ScaleWindow.** Declared range of `S` values for which behaviour claims hold (editioned). This is **distinct from** **FreshnessWindow** used by parity. 
* **Scale‑Probe.** At least **two** (preferably **≥ 3**) **parity‑respecting** points in `S` within the ScaleWindow, recorded with **replicates/seeds** and **CI/error bars** to support elasticity classification. Pick points via a **small factorial or Latin‑hypercube** when multiple knobs vary.
* **ElasticityClass** `χ ∈ {rising, knee, flat, declining}` — a **qualitative** class; numeric exponents/fits live in domain annexes, not Core.
* **ParityNotes.** `iso‑scale parity?` flag (and **loss notes** if not achieved), plus **Bridge/Φ/Ψ** IDs when crossing contexts (penalties **route to R only**). 

**4.3 Norms (SLL).**

* **SLL‑1 (Declaration).** Any profile **claiming scale behaviour SHALL** declare `S` and a **ScaleWindow** for the Context.
* **SLL‑2 (Probe).** Early investigation **SHALL** include a **scale‑probe** (≥ 2 points in `S`, with replicates/CI) and record **χ**. Multi‑knob probes **SHALL** hold unspecified knobs fixed or pinned, and disclose invariants.
* **SLL‑3 (Parity).** Where `S` is declared, comparisons **SHALL** ensure **iso‑scale parity** and lawful **gauge mapping** across heterogeneous knobs (e.g., FLOPs↔tokens) **before** comparing outcomes; **FreshnessWindows/editions** must be equal/pinned per **G.9**. Record **seeds/replicates**, ComparatorSet, and policy‑ids in telemetry/SCR. 
* **SLL‑4 (Selection lens).** Within the **same Context and ScaleWindow**, if other heads (N/U/C) are tied, selectors **MAY** use **χ** as a **policy‑level tie‑breaker** under **E/E‑LOG**; illumination remains a **gauge** unless a CAL policy promotes it.
* **SLL‑5 (Knee test).** A **knee** is **claimed** only where a monotone rise is followed by a **statistically significant** slope drop across adjacent probe points within the ScaleWindow; thresholds (e.g., Δslope & CI level) are **policy‑defined** (E/E‑LOG) and must be cited. Absent such evidence, classify as **rising**.
* **SLL‑6 (Telemetry invariants).** Probes **SHALL** export seeds/replicates, edition pins, policy‑ids, and Resrc‑CAL units to **G.11**.

**4.4 Method — minimal SoTA probe recipe (notation‑agnostic; informative).**
1) **Choose knobs** `S` that are plausibly monotone in the Context (compute/data/capacity/FoA).  
2) **Pick 3–5 probe points** per active knob (edge/mid/edge) under iso‑scale parity; use a **fractional factorial** if >2 knobs.  
3) **Run replicates** (≥ 3 preferred) and **bootstrap** 95% CI on the primary objective(s); log seeds.  
4) **Estimate local slopes** on a log‑log grid; apply **piecewise/segmented regression** or a **knee detector** (e.g., L‑curve/Kneedle) to support `χ`.  
5) **Record invariants** (pinned knobs, safety envelope) and publish **SLL.Card@Context**.  
6) **If χ changes** across the window, split the ScaleWindow and re‑classify per segment.

#### 5) Interfaces — minimal I/O (conceptual)

**G.9 Plan/Run Parity** consumes `S`/ScaleWindow to align budgets, **pin editions**, and perform **gauge mapping**; **G.11** carries **policy‑id**, **PathSliceId**, seeds/replicates, CI level, and edition pins per parity CC. 

#### 6) Conformance Checklist (CC‑SLL)

1. `S` declared **or** `S = N/A` with rationale.
2. **Scale‑probe** performed; **χ** recorded with **replicates/CI**; invariants disclosed.
3. **iso‑scale parity** or **loss notes** + penalties **→ R only**; editions/seeds pinned; ComparatorSet cited.
4. If used as tie‑breaker, the selector cites **χ** and **lens id** in **E/E‑LOG** provenance.
5. Knee claims cite the **policy threshold** and CI level used.

#### 7) Anti‑patterns & remedies

Hidden budget mismatches; averaging ordinals across families; **illumination in dominance by default**; unpinned editions; slope claims without **replicates/CI**; training/inference phase mixing → **cure** with **G.9** parity (equal windows/editions; normalize‑then‑compare; return sets), phase‑label the claim, and record slope uncertainty per Scale‑Audit discipline.  

#### 8) Archetypal grounding (post‑2015; informative)

* **LLM scaling.** Kaplan‑style & **Chinchilla‑optimal** regimes; **Mixture‑of‑Experts** and **retrieval‑augmented** families shift effective capacity with different inference budgets; prompt‑policies often transfer better than narrow pipelines.
* **RL/Planning.** Model‑based optimization & general agents vs hand‑tuned controllers; slopes reported wrt budget/FoA under safety envelopes.
* **QD/OEE.** MAP‑Elites, **CMA‑ME**, **DQD**, **QDax**; **POET/Enhanced‑POET** families: coverage/illumination as gauges; parity uses fixed grids/spaces and edition pins.  

#### 9) Payload — exports

`SLL.Card@Context` (UTS row; editioned):
`⟨S{knobs, units, phase}, ScaleWindow, Scale‑Probe{points≥2, design=one‑liner, seeds, CI}, ElasticityClass χ, ParityNotes{iso‑scale?|loss, invariants}, BridgeIds?/Φ/Ψ, PolicyIds? (E/E‑LOG), PathSliceId?⟩`.

**UTS row template (conceptual; pencil‑ready).**
`SLL.Card@Context := S=(COMPUTE|DATA|CAPACITY|FOA; units=…; phase=TRAIN|INFER), ScaleWindow=[LOW…HIGH], Probe=(points=…, design=factorial|LHD, seeds=…, CI=…), χ=rising|knee|flat|declining, ParityNotes=(iso=true|false; invariants=…), Bridge/Φ/Ψ=(…), PolicyIds=(…), PathSliceId=(…)`.

#### 10) Relations

**Builds on:** C.16/17/18. **Coordinates with:** C.19 (lenses/policies), **G.5** (set‑returning selector), **G.9** (parity; **ParetoOnly** default; gauge‑mapping), **G.10** (shipping). 

> *Pedagogical cue.* **Say what you would scale, probe it twice, and use the slope‑class to steer.**

## C.19 — E/E‑LOG — Explore–Exploit Governor \[A]

**Status.** Architheory specification (**LOG**). Defines exploration/exploitation policies and selection lenses. **No Γ operators** are exported; policies parameterize calls in **C.18 NQD‑CAL**.

### Problem frame
The E/E governor provides named, versioned policies and lenses that steer NQD generation/selection under lawful dominance and provenance constraints.

### Problem
Ad‑hoc exploration mixes ordinal and interval folds, silently scalarises posets, and loses lens/policy provenance—undermining legality and reproducibility.

### Forces
• Trust gates vs. discovery — graduation requires backstop confidence while maintaining explore_share.
• Heterogeneity vs. focus — fairness quotas by family vs. depth on proven lines.
• Lens expressiveness vs. audit — scalarised choices must not be called 'the frontier' and MUST record lens ids.

### Solution
Define EmitterPolicy (class, params, ε, K, insertion/dedup) and selection lenses with a fixed pipeline (Eligibility → Dominance → Tie‑breakers); bind provenance (policy id, lens id) and guard promotions of Surprise/Illumination to dominance to explicit policy declarations.

**Agency note.** Decisions are taken by a **system in role**. **Contexts publish** measurement spaces and admissible policies as **semantic frames**; LOG profiles lenses and policies but does **not** enact choices.
**Depends on.** **C.18 NQD‑CAL** (generators), **C.17 Creativity‑CHR** (measurements), **Decsn‑CAL** (objectives/constraints, scalarization lenses), **B.3** (trust adjustments), **Compose‑CAL** (set aggregation; advisory).

**EmitterPolicy (named profile).** A context‑local, versioned policy with fields:
`{ name, class ∈ {UCB, Thompson, BO‑EI, GP‑UCB, PES, …}, params, explore_share∈[0,1], temperature τ≥0, rebalance_period, wild_bet_quota≥0, backstop_confidence (assurance level), epsilon_dominance ε, cell_capacity K, **insertion_policy**, **dedup_threshold** }`.
Policies are referenced as `U.EmitterPolicyRef` by NQD generator call (C.18) and are conceptual lenses, not staffing/budget instructions.

**Defaults (if policy is unspecified):**  
• **Dominance:** `{Q components}` with `ConstraintFit=pass` as **eligibility gate**.  
• **Tie‑breakers:** `Novelty@context`, `ΔDiversity_P`, `Surprise`; `Illumination` (gauge over Diversity_P) MAY be used as a tie‑breaker but is **not** in the dominance set.  
• **Archive:** `K=1`, `ε=0`, deduplication in `CharacteristicSpace`.  
• **Policy:** UCB‑class with moderate temperature; `explore_share ≈ 0.3–0.5`.  
• **Provenance (minimum):** record `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `DHCMethodRef.edition`, `EmitterPolicyRef`, `InsertionPolicyRef`, `dedup_threshold?`, `TimeWindow`, `Seeds`.

**Scalarization lenses (policy‑level).** A lens `J_ℓ` declares: (a) hard eligibility conditions (e.g., ConstraintFit=pass), (b) soft aggregation (weights/curves), (c) trust policy (how assurance/CL discounts enter).  
**Conformance.** A Context MUST name the lens used to pick from a frontier; scalarized rankings MUST NOT be presented as “the frontier”; the **`lens id MUST be recorded in provenance of each selection`**.

**Promotion rules (policy).**  
- **Tie‑breaks.**  `Surprise` and `Illumination` MAY act as tie‑breakers; **promotion into the dominance set MUST be declared by lens or policy id** and captured in provenance.
- **Graduation.** Profiles graduate from Explore→Exploit when **backstop_confidence** (B.3 level) and eligibility conditions are met.  
- **Sunset/Pivot.** Profiles failing VOI/backstop thresholds are sunset or pivoted at `rebalance_period`.

**Explore/Exploit loop (per rebalance_period).**
1) Recompute frontier with trust discounts.  
2) Enforce `explore_share` (minimum attention on high‑Novelty, not‑yet‑proven profiles).  
3) Update generator `temperature τ` / emitter mix.  
4) Apply `backstop_confidence` to graduate; sunset stale probes.  
5) Satisfy `wild_bet_quota` by seeding fresh high‑Novelty candidates.
6) HET‑FIRST — apply group‑fairness quotas by domain‑family and/or DPP/Max‑min repulsion before exploit lenses; log quotas and sampler policy id.

**Named lenses (heuristics; policy‑level, not norms)**
The following **lens profiles** are **illustrative heuristics**. Contexts MAY reuse/modify them; they are **not** normative.
• **Frontier‑sweeper** — maintain attention on the full front; promote only when `backstop_confidence` holds.  
• **Barbell** — enforce `explore_share ≥ θ` with a `wild_bet_quota`; otherwise exploit top‑trust region.  
• **Spike‑first** — pick highest **Use‑Value** subject to `ConstraintFit=pass` and a small **Cost‑to‑Probe** cap.  
• **Safety‑first** — minimize **SafetyRisk** subject to `Use‑Value ≥ θ` and `ConstraintFit=pass`.  
• **Platform‑option** — maximize **Option‑Value** under probe cost bounds.  
• **Pilot‑then‑scale** — optimize **Use‑Value** on pilot scope with `BackstopConfidence ≥ L1`; widen `G` once **R** holds.  
• **Heterogeneity‑first (policy id).** Eligibility → Dominance → Tie‑breakers; Hard gate: FamilyCoverage ≥ k, MinInterFamilyDistance ≥ δ_family; Fairness quotas: ≤1 candidate per sub‑family at pre‑front sampling; DPP/Max‑min sampler allowed.
**Conformance (lens recording).** A decision that uses any lens **MUST** record its **lens id** alongside `EmitterPolicyRef`. (This restates and localizes C19‑3.)

### Conformance Checklist
- **C19‑1** Each NQD generator call (C.18) **SHALL** cite `U.EmitterPolicyRef` (policy id + params) **and the active `InsertionPolicyRef`/`dedup_threshold` when not inherited**.
- **C19‑2** The characteristic set & signs used for dominance **MUST** be declared; eligibility conditions applied first. *(References to C.18 generator operators are descriptive only; LOG exports no Γ.)*
- **C19‑3** If a lens is used, its id MUST be recorded; do not label scalarized top‑1 as “frontier”.  
- **C19‑4** Promotion of Surprise/Illumination into dominance MUST be explicit in policy.  
- **C19‑5** USM/RSG gate applies: policy actions SHALL operate within the Context’s scope and enactable RSG states.
- **C19‑6** Each selection lens **MUST** implement and document the pipeline` Eligibility (ConstraintFit=pass) → Dominance (declared set) → Tie‑breakers (declared)`. Any **promotion** of Surprise/Illumination into the dominance set **MUST** be named by lens/policy id and recorded in provenance.
- **C19‑7 (LEX‑AUTH trigger).** Any change to `EmitterPolicy` defaults that affects domain‑family quotas/samplers (HET‑FIRST), or any change to `DescriptorMap` family coordinates, `DistanceDef`, or the `δ_family` threshold MUST be authored via **E.15 LEX‑AUTH** with a published **LAT**; the DRR SHALL carry the LAT pointer (see **CC‑DRR.6**). Record policy/card ids in SCR.
- **C19‑8**  When the Heterogeneity‑first lens is used, provenance MUST include: (i) the family‑quota vector (including the default triad quota k), (ii) the subFamilyDef id (from F1‑Card) if sub‑family quotas apply, (iii) the sampler class, seed, and policy id.

**Illumination & Diversity_P.** Illumination is a **gauge over Diversity_P** (coverage/QD‑score). It informs exploration health and tie‑breaks; it is **not** a dominance characteristic by default.

When **Name Cards** (F.18) use NQD-CAL for lexical search, the underlying `DescriptorMap` and `Diversity_P` **MUST** follow the **head-term family** discipline:  
– group label candidates into families by lexical head (base noun/verb, ignoring minor prepositions and inflection);  
– compute Diversity_P and any illumination/coverage gauges over these families (cf. `FamilyCoverage`, `AliasRisk`), not over individual string variants.  
This requirement prevents treating small morphological tweaks of one head as a “diverse” frontier and keeps lexical NQD-fronts honest.

**Baseline profile (informative, context‑local template).**
`EmitterPolicy#NQD-Default-2025`:
    class=`UCB`, explore_share=`0.3–0.5`, temperature `τ=moderate`,
    rebalance_period=`Context default`, wild_bet_quota=`≥0`,
    backstop_confidence=`policy L1`, epsilon_dominance=`ε=0`,
    cell_capacity=`K=1`.
Contexts MAY clone/adjust; if used, record its id in provenance.

**Didactic quickstart (Context).**
- Start with policy class = `UCB` or `Thompson`; set `explore_share≈0.3–0.5`, `τ` moderate.  
- Name the dominance set: `{Q components, Novelty@context, ΔDiversity_P}` with `ConstraintFit=pass` as gate.  
  *(Use‑Value / Cost‑to‑Probe may appear in **lenses** or **constraints**; they are **not** in the default dominance set.)*
- Pick a lens for the final choice (or stick to frontier if undecided); record the lens id in the decision memo.

### Archetypal Grounding
**System.** Policy‑driven A/B of architectural variants: Eligibility = constraint‑fit; Dominance = {Q components, Novelty@context, ΔDiversity_P}; lens = 'Frontier‑sweeper' vs 'Barbell'.
**Episteme.** Method‑family portfolio in SoTA pack: fairness quotas across traditions; lens id recorded; Illumination used as tie‑breaker only unless promoted.

### Bias‑Annotation
No global scalarisation of partial orders; ordinal scales excluded from arithmetic; all selections record lens id and policy id; notation/tool neutrality.

### Consequences
• Transparent exploration budgets. • Repeatable lens‑based selections. • Heterogeneity preserved without illegal aggregates.

### Rationale
Post‑2015 exploration practice (bandits/BO/RL with QD) shows policies must be explicit, auditable, and editioned; LOG provides that governance.

### Relations
Builds on: Decsn‑CAL, B.3. Coordinates with: C.18, C.17, G.5, G.9.

### C.19.1 — **BLP — Bitter‑Lesson Preference (policy)** \[A]

**One‑screen purpose (manager‑first).**
Establish, at **governing policy** level, the empirical **Bitter Lesson**: **prefer general, scale‑amenable methods**—those that improve with **more data/compute/capacity and greater freedom‑of‑action**—over narrow hand‑crafted heuristics **when safety and legality are equal**. Exceptions require a transparent **Scale‑Audit** under the parity harness. 

**Builds on.** C.19 (E/E‑LOG), C.24 (Agent‑Tools‑CAL; **ATC‑2**), B.3 (Assurance), E.3 (Precedence), E.5 (Guard‑Rails).
**Coordinates with.** G.5 (Selector), G.8 (SoS‑LOG Bundles), G.9 (Parity), G.11 (Refresh‑Telemetry), A.0 (On‑Ramp).
**Keywords.** general‑method preference; scale‑amenability; **BLP‑waiver**; iso‑scale parity; **Scale‑Audit**; slope vector; **α/δ tolerances**.

#### 1) Problem frame

Bespoke heuristics can win locally but **do not scale**; general methods (search/learning/planning) **improve with scale** and transfer across bridges/planes. Without a standing policy, selectors drift toward hand‑craft and single‑winner leaderboards, violating parity and lawful orders. 

#### 2) Policy clauses (normative; synchronized with Core)

**BLP‑1 — Scale‑Audit requirement.**
Any DRR that selects a **narrower/hand‑engineered** method over a **general/scalable** alternative **MUST** include a **Scale‑Audit**:
(a) **Parity harness**: equal **FreshnessWindows**, a common **ComparatorSet**, **replicates/seeds**, **portfolio‑first** evaluation; **Dominance = ParetoOnly** unless a CAL policy says otherwise (policy‑id cited).  
(b) **Budget sweeps**: vary **compute**, **data**, and **FoA** within a fixed safety envelope; **pin** any unsweepable knob and record the invariant. 
(c) **Slopes & uncertainty**: report ∂quality/∂compute, ∂quality/∂data, and (where applicable) ∂coverage/∂FoA, with **CI/error bars** and **edition/policy pins** in telemetry. Use **bootstrapped CIs** or repeated‑seed estimates; disclose heteroscedasticity handling.
(d) **Resources**: publish **Resrc‑CAL** accounts (time/energy/FLOPs) and assurance deltas (B.3). 
(e) **Objective vector**: list **Q/Risk/Cost** and—**only if policy promotes them**—illumination/coverage gauges. 
(f) **DoE recipe**: for ≥2 active knobs, apply a **fractional factorial** or **Latin‑hypercube** with ≥ 3 levels per knob to avoid aliasing; justify any lower design.  
(g) **Knee & regret tests**: if claiming a heuristic wins, show either (i) a **knee** inside the audited window for the general method (per SLL‑5 policy thresholds) or (ii) **budget‑constrained regret** over the sweep where the heuristic dominates within CI.

**BLP‑2 — Preference rule (with α/δ tolerances).**
Among admissible options with comparable assurance (within **δ**) and budget (within **α**), prefer the method whose **slope vector** **Pareto‑dominates** over the audited range; if no dominance within error bounds, prefer the **more general** method; else resolve by the **E/E‑LOG** tie‑breakers declared in policy. (Agentic contexts implement this as **ATC‑2**; **BLP_delta_α/δ** live in **ATC.Policy**.)  

> **BLP‑2.1 — Valid waiver grounds (override transparency).**
> Overrides of BLP‑2 are allowed **only** when:
> • **Deontic override:** regulation/ethics make the general method inapplicable (E.5/E.3).
> • **Scale‑probe overturn:** under **iso‑scale parity** in the declared **ScaleWindow**, the heuristic **sustainedly outperforms** with uncertainty accounted for.
> • **Complementary bias:** the heuristic is an **inductive bias** that **improves** the general method **without blocking scale** (graceful degradation as `S` grows).
> All overrides record a **BLP‑waiver** with rationale, owner, and expiry/review in the DRR. 

**BLP‑3 — Minimal‑prescription default.**
Author **rules‑as‑prohibitions** (negative constraints) instead of stepwise scripts; encode limits in **Φ policy tables** (and **Φ_plane**) and allow agents to **sequence autonomously** within those constraints. Scripts are permissible only when mandated by safety/regulation or with compelling DRR evidence reviewed under E.3/E.5. 

**BLP‑4 — Heuristic‑Debt register (mandatory).**
Any admitted heuristic is recorded as **Heuristic Debt** with scope, owner, expiry/review window, and a de‑hardening plan; track in **CalibrationLedger/BCT** and cite in SCR. 

**BLP‑5 — Continuous‑learning posture.**
Where product policy allows, enable **feedback‑driven adaptation** (preference learning, critique loops) within Guard‑Rails and privacy controls; disabling adaptation requires DRR justification and review date. 

**BLP‑6 — Precedence & safeguards.**
BLP is constitutional (instantiates **P‑10/P‑11/P‑7/P‑1**), but **does not supersede Guard‑Rails (E.5) or precedence rulings (E.3)**. Where **NQD/E/E‑LOG** promotes illumination into dominance, **BLP adopts that lens** for the audited window.  

**BLP‑7 — Publication discipline.**
Scale‑Audit artefacts **SHALL** be exported to **G.11** with edition pins, CI level, α/δ, ComparatorSet, and **BLP.Policy@Context** reference so downstream selectors can reuse evidence without re‑running audits.

#### 3) Conformance Checklist (CC‑BLP)

1. **α/δ tolerances** declared in DRR or via policy profile (and CI level stated).
2. DRR includes a **Scale‑Audit** (BLP‑1a–g) with slopes, **CI**, edition/policy pins, and Resrc‑CAL.
3. Selection cites **BLP‑2** and precedence checks.
4. Any heuristic is logged as **Heuristic‑Debt** with expiry and de‑hardening plan.
5. Authoring defaults to **rules‑as‑prohibitions**; deviations are DRR‑justified and safety‑anchored.
6. **Resrc‑CAL** accounts and assurance deltas reported.
7. **Replicate counts/seeds** and **confidence intervals** recorded for slope estimates; heteroscedasticity handling disclosed.
8. Audit artefacts exported to **G.11** with **BLP.Policy@Context** id.

#### 4) Anti‑patterns & remedies

Single‑winner leaderboards; hidden budget mixing; promoting illumination into dominance **without policy**; missing edition pins; heuristics without expiry; slope estimates without CI or with aliased designs → **remedy** with G.9 parity + edition pins, explicit **policy‑ids**, DRR publication, **Heuristic‑Debt** entries, and BLP‑1f DoE discipline. 

#### 5) Archetypal grounding (post‑2015; informative)

* **LLMs:** prompt‑programs, **retrieval‑augmented** and **MoE** policies vs narrow task‑specific pipelines; portfolio‑first selection across editions/budgets.
* **RL & planning:** model‑based optimization/general agents vs hand‑coded controllers (subject to α/δ and safety).
* **Preference learning:** **RLHF ↔ DPO** families.
* **QD/OEE:** MAP‑Elites/**CMA‑ME**/**DQD**/**QDax**; **POET/Enhanced‑POET**; illumination remains a **gauge** unless policy promotes it. 

#### 6) Payload — exports

`BLP.Policy@Context` (UTS row; editioned):
`⟨PreferenceDefault, α/δ tolerances + CI, Scale‑Audit recipe (G.9 link; DoE), WaiverRegister{reason, owner, expiry}, E/E‑LOG lens policy‑ids, ATC.PolicyRef? (agentic), G.11.TelemetryPins⟩`.

**UTS row template (conceptual; pencil‑ready).**
`BLP.Policy@Context := PreferenceDefault=(prefer‑general|neutral), α/δ=(α=…, δ=…, CI=…), Scale‑Audit=(parity=G.9; sweep=S={…}; DoE=factorial|LHD; kneeTest=policy‑τ), WaiverRegister=[{reason=…, owner=…, expiry=…}], E/E‑LOG=(policyIds=…), ATC.PolicyRef=(…), TelemetryPins=(edition=…, seeds=…, comparatorSet=…)`.

#### 7) Relations

**Depends on:** **G.5/G.9** (selector/parity), **G.11** (refresh telemetry), **C.5** (Resrc‑CAL), **C.18** (NQD‑CAL), **C.19** (E/E‑LOG), **F.7/F.9** (Bridges, CL/Φ/Ψ). **Constrained by:** **E.5** Guard‑Rails and **E.3** precedence. 

> *Memory hook.* **Prefer what scales; explain when you don’t.**

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
