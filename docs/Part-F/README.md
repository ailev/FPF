# **Part F — The Unification Suite (U‑Suite): Concept‑Sets, SenseCells & Contextual Role Assignment**

# Cluster F.I — context of meaning & Raw Material

# **F.0.1 — Contextual Lexicon Principles** \[A]

> **One‑sentence summary.** All meanings in FPF are **local to a `U.BoundedContext`** (“Context of meaning”); terms are **spoken with their Context**, and any relation **across Contexts** exists **only** as an explicit **Alignment Bridge** with stated loss/fit.

**Status.** Architectural pattern \[A], architheory‑agnostic.
**Builds on:** A.1.1 `U.BoundedContext` (formal frame); A.7 *Strict Distinction* (C‑6); A.8 *Universal Core* (C‑1); A.11 *Ontological Parsimony* (C‑5); A.4 *Temporal Duality* (C‑7); **E.10.D1 D.CTX** (lexical discipline for “Context”).
**Coordinates with.** **F.1** (Context Map via Context Cards), **F.2** (local term capture), **F.3** (intra‑Context clustering), **F.7** (Concept‑Set Table), **F.9** (Alignment & Bridge), **B.3** (Trust & Assurance; CL penalties).

> **Didactic note.** In the Tech register, **Context ≡ `U.BoundedContext`** (per E.10.D1). We use “Context of meaning” as a **metaphor only**; *Context* remains the normative short form for `U.BoundedContext`. The word **anchor** is not used in FPF.

> **Didactic note.** In the Tech register, **Context ≡ `U.BoundedContext`** (per E.10.D1). We use “Context of meaning” as a **metaphor only**; *Context* remains the normative short form for `U.BoundedContext`. The word **anchor** is not used in FPF. The word *plane* is reserved to **CHR:ReferencePlane** only.

**Terminology guard (normative, Part F).** The **row classifier** is **senseFamily**: {Role | Status | Measurement | Type‑structure | Method | Execution}. **Characteristic** (MM‑CHR) names measurable aspects only (A.17–A.19) and MUST NOT be used for row typing in Part F. Avoid the generic word **facet** in Part F; when unavoidable, reference **C.3.5 KindAT (informative facet)** or **Compose‑CAL `U.Facet`** explicitly. Only **CHR:ReferencePlane** is permitted (no bare “plane”); use **I/D/S layer** for intension/description/specification; use **stance** for design vs run.

## 1 · Problem Frame

Trans‑disciplinary modelling fails without an explicit discipline for **where words mean what**.

* **Semantic drift.** The same string (“process”, “role”, “service”) slides between domains and editions.
* **Homonym collisions.** One label carries incompatible senses across fields.
* **Hidden synonymy.** Different labels point to the same local sense, but the identity is unstated.
* **Implicit globalism.** Meaning is treated as universal; integration silently re‑writes models.

FPF resolves this by **localising** meaning first, then **explicitly translating** across locales.

---

## 2 · The Three Principles (normative)

### P‑S · **Source Localisation Principle** — *Speak with the Context.*

**Rule.** Every term in a normative FPF artefact **MUST** be bound to a **specific `U.BoundedContext`** (its “Context of meaning”). The binding is explicit in text, notation, or table headers (e.g., **process (BPMN 2.0)**).

**Implications.**

* No free‑floating “global terms”.
* A finite **Context Map** (see **F.1**) is chosen **before** naming work starts.
* If a source intrinsically fixes time stance, the **design/run tag** is carried by the Context (C‑7).

**Reasoning move (conceptual).**
`Context(C) ∧ says(C, term t) ⊢ usable(t@C)`

**Illustration (Enactment line).**
`activity @ PROV‑O (run)` vs `task @ IEC 61131‑3 (run)` vs `process @ BPMN 2.0 (design)`.

---

### P‑L · **Local Meaning Principle** — *Meaning lives inside the Context.*

**Rule.** The **intended sense** of a term is established **inside its Context** as a **SenseCell**: a small, reconstructible unit of local meaning with **Tech/Plain labels** and a concise gloss. SenseCells are **lexical only** (C‑6): no behaviours, no deontics, no equations.

**Implications.**

* SenseCells are **Context‑scoped**; they do **not** cross Contexts.
* Minimal generality (G‑1) and contextual specification (G‑2) govern naming inside the Context.
* **Intra‑Context clustering** of raw mentions precedes any Cross‑context act (see **F.3**).

**Reasoning move (conceptual).**
`usable(t@C) ∧ fits(gloss, C) ⊢ SenseCell⟨t@C⟩`

**Illustration (KD‑CAL).**
`observation @ SOSA/SSN`: Tech “observation”, Plain “measurement act”; gloss “Result‑bearing act applying a Procedure…”.

---

### P‑B · **Explicit Bridge Principle** — *across Contexts, only with a bridge.*

**Rule.** Any relation between terms from **different** Contexts **MUST** be stated as an **Alignment Bridge** (see **F.9**): a named mapping between **SenseCell⟨·⟩** items with a declared **relation kind** (e.g., *overlaps*, *broader‑than*, *near‑equivalent*) and a **Congruence Level (CL)** for trust calculus (B.3).

**Implications.**

* No by‑name identity across Contexts; **string equality ≠ sense equality**.
* Bridges carry **loss/fit notes** and are auditable; they can be revised by edition.
* Concept‑Sets (F.7) are built **from bridged cells**, not from surface strings.

**Reasoning move (conceptual).**
`SenseCell⟨x@A⟩ ↔⟨rel, CL⟩ SenseCell⟨y@B⟩ ⊢ translatable(x@A, y@B, rel, CL)`

**Illustration (Sys‑CAL × Enactment).**
`actuation @ CTRL‑Text` ↔⟨near‑equiv, CL=2⟩ `control‑output @ IEC 61131‑3`.

---

## 3 · Minimal Artefacts (conceptual, notationally neutral)

> These artefacts are **thought‑objects**; they specify **what must exist conceptually**, not how it is stored.

### 3.1 **Context Card** (for each `U.BoundedContext`)

A terse descriptor used in the **Context Map** (F.1):

* `id` (stable local handle) · `title` · `edition/year`
* `family` (discipline family; informal) · `scope gist`
* `timeStance?` (`design` / `run`, if inherent)
* `trip‑wires` (few lexical caveats that often mislead, e.g., “*process*≠thermo process”)

### 3.2 **SenseCell** (unit of local meaning, inside one context)

* `label.tech` / `label.plain` (two registers)
* `gloss` (minimal generality, Context‑true)
* `notes?` (warnings, edition shifts)
* **No** behaviour/deontics/equations (C‑6)

> **Where it comes from.** F.2 describes how SenseCells can be *derived* from local term evidence; F.0.1 only **requires** that local meaning be expressible as a SenseCell.

### 3.3 **Alignment Bridge** (between SenseCells from different Contexts)

* `left: SenseCell⟨·@A⟩`, `right: SenseCell⟨·@B⟩`
* `relation` (e.g., *equivalent‑under‑assumptions*, *overlaps*, *broader‑than*)
* `CL` (Congruence Level; feeds B.3 Trust & Assurance)
* `loss/fit` (explicit statement of what is lost or assumed)

---

## 4 · Invariants (normative)

1. **I‑1 · Context‑qualified usage.** Every normative use of a term is **Context‑qualified** (directly or via table/section headers).
2. **I‑2 · Local‑only cells.** A SenseCell belongs to **exactly one** Context.
3. **I‑3 · senseFamily hygiene.** SenseCells are **lexical**; behaviour, deontics, measurements, proof steps live in their respective architheories (C‑6). 
4. **I‑4 · Time stance fidelity.** If a source fixes `design/run`, the Context Card **carries** it and SenseCells **inherit** it.
5. **I‑5 · No implicit Cross‑context identity.** Cross‑context relations exist **only** as F.9 Bridges with `relation` and `CL`.
6. **I‑6 · Parsimony & heterogeneity hook.** The Context Map is **finite**, **heterogeneous** (≥ 3 families per unification line), and **parsimonious** (F.1).

---

## 5 · Reasoning Primitives (judgement schemata; pure, side‑effect‑free)

*These capture **allowable mental moves**; they do not prescribe storage, APIs, or workflow.*

* **Context qualification**
  `Context(C) ∧ mentions(C, s) ⊢ uses(s@C)`
  *Reading:* If a string *s* is used under Context *C*, we treat it as the local term *s\@C*.

* **Local sense formation**
  `uses(t@C) ∧ gloss_C(t) ⊢ SenseCell⟨t@C⟩`
  *Reading:* A Context‑true gloss yields a SenseCell for *t* inside *C*.

* **Admissible Cross‑context relation**
  `SenseCell⟨x@A⟩ ∧ SenseCell⟨y@B⟩ ∧ declare(rel, CL) ⊢ Bridge(x@A, y@B, rel, CL)`
  *Reading:* Only an explicit declaration generates a Bridge; no name‑matching inferences.

* **Bridge‑to‑Concept‑Set hint** *(for F.7)*
  `Bridge(x@A, y@B, rel≈equiv, CL≥k) ⊢ candidate_same_row(x, y)`
  *Reading:* Strong, near‑equivalence bridges can *nominate* cells for one Concept‑Set row (final decision in F.7).

---

## 6 · Didactic Metaphor (informative)

* **Contexts.** Each `U.BoundedContext` is a **Context**; its **Context Card** is a sign on the door (name, edition, time stance, trip‑wires).
* **Words in a Context.** A **SenseCell** is a dictionary entry pinned to that Context’s wall.
* **Door‑to‑door links.** An **Alignment Bridge** is a labelled passage connecting two Contexts; a **CL** placard says how trustworthy that passage is.

> *We first speak inside Contexts; only then decide which doors to connect—and with what warnings.*

---

## 7 · Placement & Flow

**F.0.1** is the **front door** of Part F. It enables:
**F.1** (choosing Contexts with Context Cards) → **F.2** (deriving SenseCells inside each Context) → **F.3** (stabilising local senses) → **F.7** (building Concept‑Set rows) → **F.9** (stating Bridges).

## 8 · Anti‑patterns & remedies

| #       | Anti‑pattern (what goes wrong)   | Symptom in models                                          | Why harmful (conceptual)                            | Remedy (this pattern’s clause)                                                            |
| ------- | -------------------------------- | ---------------------------------------------------------- | --------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **A1**  | **Global term** (Contextless usage) | “process”, “service”, “role” used without a Context mark      | Meaning drifts; integration silently rewrites sense | **P‑S**: Always speak **term\@context**; qualify via section/table headers if repeated       |
| **A2**  | **String‑match identity**        | Equating *service* (ITIL) with *service* (web‑API) by name | String equality ≠ sense equality                    | **P‑B**: Cross‑context relations exist only as **Bridges** with `relation`+`CL`              |
| **A3**  | **senseFamily mixing in SenseCell**    | Local glosses include behaviours, deontics, equations      | Violates **Strict Distinction** (C‑6); blocks reuse | **P‑L**: SenseCell is **lexical only**; behaviour/deontic math belongs to architheories   |
| **A4**  | **Edition blur**                 | Citing “BPMN” or “ITIL” without edition                    | Underspecified Context; un‑auditable sense shift       | **Context Card** carries `edition/year`; treat materially changed editions as distinct Contexts |
| **A5**  | **Context as type**              | Declaring “PROV‑O is‑a BPMN”                               | Implies inherited meanings between Contexts            | Contexts aren’t types; **no is‑a on Contexts** (E.10.D1). Use Bridges only                       |
| **A6**  | **Bridge without loss/fit**      | Bridge declared as “equivalent” with no assumptions        | Users infer total identity; trust calculus blind    | **P‑B**: Bridge must state `relation` and `CL`, plus a brief **loss/fit** note            |
| **A7**  | **Row from strings**             | Concept‑Set rows built from surface forms                  | Homonyms/synonyms contaminate rows                  | Build rows from **SenseCells**; add only cells connected by acceptable Bridges (F.7)      |
| **A8**  | **Transitivity overreach**       | Chaining weak near‑equivalences as if exact                | Inflates sameness; hides mismatch                   | **Bridge composition** (Sec. 10): compose with **min‑CL** and keep relation weakening     |
| **A9**  | **Domain ≡ Context**                | “Domain” name used as if it were a `U.BoundedContext`      | Domain families are informal; Contexts are formal      | Keep **Domain family** informative on Context Cards; meanings bind to **Contexts** only         |
| **A10** | **Time‑stance confusion**        | Treating `design` and `run` senses as identical            | Crosses senseFamilies; erases execution/spec split         | Carry **time stance** on Context Cards; prefer `design‑spec‑of` / `run‑trace‑of` Bridges     |

---

## 9 · Compact worked examples (multi‑architheory)

> *Each vignette shows (1) two Context Cards (abridged), (2) SenseCells inside Contexts, (3) the Bridge with relation & CL, and (4) a Concept‑Set hint (if any).*

### 9.1 Enactment × Provenance — *process* vs *activity*

* **Context A**: `BPMN_2_0` · *Business Process Model and Notation v2.0 (2011)* · *design*
  **SenseCell⟨process\@BPMN⟩**: Tech “process”; Plain “workflow process”; Gloss “graph of flow nodes/events executed by participants.”

* **Context B**: `PROV_O_2013` · *W3C PROV‑O (2013)* · *run*
  **SenseCell⟨activity\@PROV⟩**: Tech “activity”; Plain “provenance activity”; Gloss “time‑bounded occurrence using/generating entities.”

* **Bridge**: ⟨process\@BPMN⟩ ↔⟨`design‑spec‑of`, **CL=2**, loss: “no concurrency semantics in trace”; fit: “maps to execution plan”⟩ ⟨activity\@PROV⟩

* **Concept‑Set hint**: *No* same‑row nomination (relation ≠ near‑equiv); instead, record a **design↔run** linkage.

---

### 9.2 Control × PLC runtime — *actuation* vs *control output*

* **Context A**: `CTRL_Text_Classic` · *control theory primers* · *design*
  **SenseCell⟨actuation\@CTRL⟩**: Tech “actuation”; Plain “control output”; Gloss “signal applied to plant actuators.”

* **Context B**: `IEC_61131_3` · *PLC languages* · *run*
  **SenseCell⟨q‑output\@IEC⟩**: Tech “control‑output”; Plain “PLC output”; Gloss “program‑produced output variable to field I/O.”

* **Bridge**: ⟨actuation\@CTRL⟩ ↔⟨`near‑equivalent`, **CL=2**, loss: “hardware/scan‑cycle specifics absent in CTRL”; fit: “semantics align under linear regime”⟩ ⟨q‑output\@IEC⟩

* **Concept‑Set hint**: *Candidate same‑row* (F.7) with note: “merge permitted at **CL≥2** threshold.”

---

### 9.3 Measurement × Service — *observation* vs *service metric*

* **Context A**: `SOSA_SSN_2017` · *sensing/observations* · *run*
  **SenseCell⟨observation\@SOSA⟩**: Tech “observation”; Plain “measurement act”.

* **Context B**: `ITIL4_2020` · *services* · *(mixed)*
  **SenseCell⟨slo‑metric\@ITIL⟩**: Tech “service‑level metric”; Plain “service measure”; Gloss “quantity used to evaluate SLOs.”

* **Bridge**: ⟨observation\@SOSA⟩ ↔⟨`provides‑value‑for`, **CL=2**, loss: “organizational context not in SOSA”; fit: “metric results are measurement results.”⟩ ⟨slo‑metric\@ITIL⟩

* **Concept‑Set hint**: Not a same‑row case; this is a **role‑in‑use** relation (measurement feeds status evaluation).

---

### 9.4 Type reasoning — *subclass‑of* (OWL) vs *is‑a (plain)*

* **Context A**: `OWL2_Profiles` · *description logics*
  **SenseCell⟨subclass\@OWL⟩**: Tech “subclass‑of”; Plain “is‑a”.

* **Context B**: `ENG_Glossary` · *engineering plain usage compendium*
  **SenseCell⟨is‑a\@ENG⟩**: Tech “is‑a (engineering)”; Plain “kind‑of”; Gloss “informal subsumption in specs.”

* **Bridge**: ⟨subclass\@OWL⟩ ↔⟨`near‑equivalent`, **CL=1**, loss: “OWL formal constraints absent in ENG”; fit: “intended subsumption semantics.”⟩ ⟨is‑a\@ENG⟩

* **Concept‑Set hint**: Keep separate rows unless the consuming artefact demands **formal** semantics.

---

### 9.5 Deontics × Access — *permission* vs *role (RBAC)*

* **Context A**: `ODRL_2_2` · *policy/deontics*
  **SenseCell⟨permission\@ODRL⟩**: Tech “permission”; Plain “allowed action”.

* **Context B**: `NIST_RBAC_2004` · *access control*
  **SenseCell⟨role\@RBAC⟩**: Tech “access‑role”; Plain “permission set”.

* **Bridge**: ⟨permission\@ODRL⟩ ↔⟨`member‑of‑set‑in`, **CL=2**, loss: “contextual obligations not preserved”; fit: “RBAC roles aggregate permissions.”⟩ ⟨role\@RBAC⟩

* **Concept‑Set hint**: Not same row (different **kinds**); useful linkage for Enactment when binding duties to sessions.

---

## 10 · Extended reasoning moves (pure judgement schemata)

> *Judgements are conceptual entailments over Contexts, SenseCells, and Bridges. They carry no storage, workflow, or governance semantics.*

### 10.1 Context‑qualified use

`Context(C) ∧ mentions(C, s) ⊢ uses(s@C)`
*If s is used under Context C, we treat it as the local term s\@C.*

### 10.2 Sense formation (local)

`uses(t@C) ∧ gloss_C(t) ⊢ SenseCell⟨t@C⟩`
*A Context‑true gloss yields a SenseCell inside C.*

### 10.3 Admissible Bridge (creation predicate)

`SenseCell⟨x@A⟩ ∧ SenseCell⟨y@B⟩ ∧ A≠B ∧ rel∈R ∧ cl∈{0,1,2} ⊢ Bridge(x@A,y@B,rel,cl)`
*Only explicit relation `rel` with Congruence Level `cl` constitutes a Bridge.*

**Canonical relation set `R` (didactic catalogue):**
`equivalent‑under‑assumptions` · `near‑equivalent` · `overlaps` · `broader‑than` · `narrower‑than` · `design‑spec‑of` · `run‑trace‑of` · `representation‑of` · `member‑of‑set‑in` · `provides‑value‑for`.

### 10.4 Bridge composition (attenuating)

`Bridge(a,b,rel₁,cl₁) ∧ Bridge(b,c,rel₂,cl₂) ⊢ Bridge*(a,c,rel*,cl*)`

* `cl* := min(cl₁, cl₂)` (do **not** inflate confidence)
* `rel* := weaken(rel₁, rel₂)` (e.g., near‑equiv ∘ overlaps → overlaps)

*Reading:* Chained passages degrade to the weakest link.

### 10.5 Non‑identity by stance

`SenseCell⟨x@A(design)⟩ ∧ SenseCell⟨y@B(run)⟩ ∧ ¬declared(Bridge(x,y,near‑equiv,_)) ⊢ ¬same‑row(x,y)`
*Different time stances forbid same‑row unless an explicit near‑equiv Bridge exists.*

### 10.6 Row viability (Concept‑Set candidacy)

`Cells = {c₁…cₙ} ⊢ row‑viable(Cells) ⇔ connected(Cells, Bridges_{rel∈{equiv,near‑equiv}, cl≥k}) ∧ ¬contradiction(Cells)`

*Reading:* A row is viable if its cells form a connected subgraph via sufficiently strong Bridges and contain no mutually exclusive links.

### 10.7 Contradiction sieve

`Bridge(a,b,broader) ∧ Bridge(a,b,narrower) ⊢ contradiction(a,b)`
*Incompatible relations across the same pair flag a contradiction for review (conceptually).*

### 10.8 Non‑bridge implication ban

`name(x) = name(y) ∧ A≠B ⊢ ¬Bridge(x@A, y@B, _, _)`
*String equality across Contexts never implies a Bridge.*

---

## 11 · SCR/RSCR acceptance checks (conceptual)

> *These checks are **content‑oriented**; they validate that a manuscript/model respects Part F principles. No process/tool assumptions are implied.*

### 11.1 SCR — Static conformance

* **SCR‑F01 (Context‑qualified).** Every normative term is Context‑qualified (directly, or via a scoped header that unambiguously fixes the Context).
* **SCR‑F02 (Local cells).** Each SenseCell belongs to **exactly one** Context; no cell aggregates Cross‑context **senses**.
* **SCR‑F03 (senseFamily hygiene).** SenseCell glosses contain no behaviours/deontics/equations; those appear only in their architheories.
* **SCR‑F04 (Bridges explicit).** Every Cross‑context relation appears as a Bridge with `relation` and `CL` and a short **loss/fit** note.
* **SCR‑F05 (No string identity).** There is no use of string equality to stand in for Cross‑context identity.
* **SCR‑F06 (Time stance fidelity).** Where a Context fixes `design/run`, the SenseCells and any Bridges reflect that stance explicitly.
* **SCR‑F07 (Row viability).** Any Concept‑Set row shown is supported by a connected subgraph of Bridges with **CL ≥ threshold** and no contradictions.

### 11.2 RSCR — Regression & evolution

* **RSCR‑F01 (Edition split).** When a source edition changes materially, SenseCells tied to the old edition remain; new cells bind to the new Context; Bridges are re‑assessed.
* **RSCR‑F02 (Bridge stability).** If any Bridge endpoint changes gloss/stance, downgrade or retire the Bridge, documenting the **loss/fit** change.
* **RSCR‑F03 (Composition guard).** When composing Bridges in a chain, the resulting `CL` never exceeds the minimal link; relation weakens monotonically.
* **RSCR‑F04 (Heterogeneity + QD guard):** requires ≥3 domain‑families AND MinInterFamilyDistance ≥ δ_family (per the active F1‑Card edition), with QD‑triad evidence (publish Diversity_P and IlluminationSummary on the declared grid/kernel). Near‑alias pairs (per dSig rule) SHALL be flagged and excluded or merged before the guard is evaluated. Record the F1‑Card edition id.

### 11.3 Publish‑ready summary

An artefact is **ready** with respect to F.0.1 when:

1. **SCR‑F01…F07** hold for all terms, cells, rows, and bridges it presents;
2. **RSCR‑F01…F04** hold under simulated edition/stance changes;
3. Every Cross‑context statement can be read as a **Bridge** or as a composition of Bridges with stated attenuation.

---

## 12 · Quick reference (didactic)

* **Context** = a `U.BoundedContext` with edition, scope, and (if inherent) time stance.
* **SenseCell** = the minimal, lexical unit of meaning inside a Context (Tech/Plain labels + gloss).
* **Bridge** = the only Cross‑context relation, labelled with `relation` and **CL**, plus a short loss/fit note.
* **Concept‑Set row** = a didactic table row collecting **SenseCells** that are sufficiently the‑same‑thing under declared Bridges.

> **Mental checklist:** *Name the Context → speak in the Context → connect Contexts only by labelled bridges → build rows from bridged cells.*


# F.1 — Domain‑Family Landscape Survey \[A]

**“Fix the context of meaning before you name anything.”**
**Status.** Architectural pattern \[A], architheory‑agnostic.
**Depends on.** E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; **F.0.1 Contextual Lexicon Principles**; A.7 **Strict Distinction (Clarity Lattice)**; A.11 **Ontological Parsimony**.
**Coordinates with.** F.2 **Term Harvesting & Normalisation**; F.3 **Intra‑Context Sense Clustering**; F.4 **Role Description**; F.9 **Alignment & Bridge Across Contexts**; **G.0–G.1** *(Scope/describedEntity handoff)*.  *(Bridges live only in F.9.)*

**Aliases (informative).** *Contexts‑first survey*; *Context cut*.

## 1 · Intent & applicability

**Intent.** Establish a **finite set of U.BoundedContext** (“**context of meaning**”), each tied to an authoritative source or canon within a **domain family**, so that all later moves (term harvesting, clustering, role naming, cross‑context bridges) operate on **local meanings** rather than on drifting, globalised words.

**Applicability.** Use **at the start** of any unification effort for **any architheory** (Enactment (`U.RoleAssignment` + `U.RoleEnactment`), Sys-CAL, KD-CAL, Kind-CAL, LCA-CAL…) and **whenever** a discipline canon materially changes (new edition, re-framing, seminal result).

**Non‑goals.** No tooling, workflow, or editorial roles. No global ontology. No cross‑context equations. This pattern describes **how to think**, not how to store.

## 2 · Problem frame

Without explicit context of meaning:

1. **Word‑drift.** Common words (*process*, *role*, *service*, *model*) silently change sense across disciplines.
2. **Scope mirages.** One influential standard is mistaken for *the* domain.
3. **Retro‑lock.** Old editions become the implicit truth simply because they were “there first”.
4. **Category bleed.** Behavioural roles, epistemic statuses, deontic permissions mix because their contexts were never fixed.
5. **Name inflation.** New U.Types appear just to “stabilise” unstable words.

---

## 3 · Forces

| Force                        | Tension to resolve                                                                |
| ---------------------------- | --------------------------------------------------------------------------------- |
| **Universality vs locality** | We want cross‑domain unification, but **meaning is local** to a U.BoundedContext. |
| **Breadth vs parsimony**     | Wide coverage prevents bias; too many Contexts defeats understanding.                |
| **Recency vs continuity**    | New editions matter; but working knowledge often trails by years.                 |
| **Didactics vs fidelity**    | Pedagogically simple summaries must remain faithful to the source.                |

---

## 4 · Core idea (didactic)

**Think in Contexts, not in words.**
A *Context of meaning* is a **U.BoundedContext** (per D.CTX) that encloses a coherent vocabulary and its rules from a **specific, citable canon** (standard, BoK, seminal paper, textbook tradition). You **name and reason** *inside the Context*. When you must step between Contexts, you will **declare a bridge later** (F.9) with explicit losses or mismatches.

---

## 5 · Minimal vocabulary (this pattern only)

* **U.BoundedContext** (short: **Context** in Tech register). The formal *Context of meaning*.
* **Context** (Tech register alias for **U.BoundedContext**). Use **Context** for pedagogy, **U.BoundedContext** for formal references.
* **Domain family.** An **informative** shelf‑label grouping related Contexts (e.g., *workflow & provenance*; *services & deontics*; *sensing & measurement*; *types & taxonomies*; *control & actuation*). **No semantics** attach; Domain ≠ Context.
* **Context Card.** A **one‑screen** conceptual sketch of a Context (see §7.2).
* **SenseCell** *(appears downstream)*. A **(Context × Local‑Sense)** address; F.3 will mint these after clustering. Mentioned here only to keep the destination in view.

---

## 6 · Solution — the Contexts‑first survey (conceptual, notation‑free)

**Step 1 — Declare your unification line(s).**
State which architheory threads are in play (e.g., *Enactment + KD‑CAL sensing + Sys‑CAL execution*). This keeps the cut purposeful.

**Step 2 — Cut the landscape by domain families.**
For each line, **select at least three distinct domain families** (heterogeneity guard). Examples:

* *Workflow & provenance* (BPMN 2.0; W3C PROV‑O)
* *Services & deontics* (ITIL 4; ODRL 2.2)
* *Sensing & measurement* (SOSA/SSN; ISO 80000‑1)
* *Types & taxonomies* (OWL 2; FCA corpus)
* *Control & actuation* (state‑space control texts; IEC 61131‑3)

**Step 3 — For each family, sketch 1–3 Context Cards.**
Prefer canonical, widely cited canons. If a field is fragmented, choose one **exemplar** and one **counter‑voice** to surface heterogeneity.

**Step 4 — Make **locality** explicit.**
Treat words as **context‑local**. *Process (BPMN)* ≠ *process (thermodynamics)* ≠ *process (PROV)*. Do not reconcile. Do not average. **Just fix the Contexts.**

**Step 5 — Bound the set.**
Small enough to hold in working memory. As a rule of thumb:

* per unification line: **≥ 3 families**;
* per family: **1–3 Contexts**.
  More only if a missing Context hides a known sense‑split you will certainly need.

**Step 6 — Postpone bridges.**
If two Contexts seem “close”, **resist** collapsing. Note the tension and defer to **F.9 Alignment & Bridge**.

## 7 · What to record (conceptual, not clerical)

**7.1 The two‑minute memory.**
Everything you need to *think correctly later* fits on an eight‑line card. No registries, no workflows, no storage choices.

**7.2 The Context Card (one‑screen sketch).**
*(Each bullet is a thought, not a field.)*

* **Name & edition.** *“BPMN 2.0 (2011)”* • *“W3C PROV‑O (2013)”* • *“ITIL 4 (2020)”*.
* **Domain family.** *workflow* / *provenance* / *services* / *deontics* / *sensing* / *types* / *control* … *(informative only; never used to infer meaning).*
* **Scope gist** *(didactic; ≠ `USM.ScopeSlice(G)`)*. One line that marks the **inside/outside** (“workflow **graphs & participants**”, “provenance **entities/activities/agents**”).
* **Time stance** *(if inherent)*. Does the canon speak **design** (specifications, models) or **run** (occurrences, acts)?
* **Lexical trip‑wires.** Known homonyms or false friends in this Context (*“process ≠ thermodynamic process”*, *“role (RBAC) ≠ behavioural role”*).
* **Neighbour Contexts** *(informative)*. Close cousins that people often conflate (*BPMN ↔ PROV‑O*, *ITIL ↔ ODRL*).
* **Recency note.** *Current* / *superseded* / *candidate* (only as a reminder to yourself which text you mean).
* **Why this Context matters here.** One sentence linking to your unification line (“we will name Executions later; PROV‑O keeps them run‑time”).
* **Diversity signature (dSig).** A 5‑characteristics discrete signature for `U.BoundedContext`: **[Sector, Function, Archetype, Regime, MetricFamily]**. Authors SHOULD pick from local discipline taxonomies. **Publish a `dSigSource` list (five refs/URIs, one per axis) on every Card**, falling back to free‑text only where no canonical term exists. Two Contexts are flagged as **Near‑Duplicate** when ≥3 characteristics match. Publish `dSig` and `dSigSource` on every Card.

> *If your Card spills beyond a screen, you are collecting facts, not fixing meaning.*

F1‑Card (normative artefact): { taxonomyRef, embeddingRef, DistanceDef, δ_family, confidenceBand, calibrationSet, edition, subFamilyDef? }. subFamilyDef (optional): declares the stable partitioning below a domain‑family (e.g., taxonomic sub‑fields or CVT clusters with parent family anchors).  When HET‑FIRST quotas refer to “sub‑family”, they MUST use this declared subFamilyDef.
Declare **DomainDistance** policy (cosine or transport) and δ_family threshold; version as part of DescriptorMapRef. Publish `confidenceBand` (e.g., CI90%) for the calibrated `δ_family`; treat numbers in examples as illustrative, not normative.

## 8 · Invariants (normative, lightweight)

1. **Context ≡ U.BoundedContext.** In this pattern, *Context* always means **U.BoundedContext** (per E.10.D1).
2. **Locality.** Words are **local to their Context**; no global meaning is implied or imported.
3. **Heterogeneity.** Each unification line considers **≥ 3 distinct Domain families** (labels are informative only).
4. **Parsimony.** Prefer few, canonical Contexts per family (1–3) that jointly expose the key sense splits.
5. **No bridging here.** No equivalence or mapping is asserted between Contexts in F.1. (Bridges live in **F.9**.)
6. **Design/run honesty.** If a canon fixes a DesignRunTag, note it. Do not reinterpret.
7. **Didactic primacy.** Each Context Card must be readable by a thoughtful engineer in **under two minutes**.
8. **Domain‑family neutrality.** Domain families **carry no semantics**; they SHALL NOT be used for inheritance, inference, or bridge implication.
9. **Scope naming separation.** `Scope gist` on Cards is **didactic only**; formal *Scope/describedEntity* (=`USM.ScopeSlice(G)` ⊕ `describedEntity(GroundingHolon, ReferencePlane)`) is declared **in G.0–G.1**, not in F.1.
10. **Diversity signature present.** Each Context Card PUBLISHES a `dSig` in the 5‑characteristics form.
11. **Collision rule.** If any pair of Cards has `dSig` matching on ≥3 characteristics, mark **Near‑Duplicate** and either merge  into one slot or replace one by a Context from a different domain‑family. Record action in SCR.

## 9 · Self‑checks (mental, not procedural)

* **The mirror test.** Can you explain *why each Context is inside* your cut **in one breath**? If not, you are surveying for comfort, not for meaning.
* **The homonym ping.** For each frequent word (*process*, *role*, *service*, *model*, *execution*), can you immediately list **the Contexts where it differs**? If not, add the missing Context.
* **The bridge itch.** Feel a strong urge to say “these are the same”? Good. **Write the itch down** and refuse to scratch it here. That’s F.9’s job.
* **The memory rule.** If your entire survey cannot be recalled **without opening a document**, it is too large.

---

## 10 · Micro‑examples (illustrative only)

*One unification line: Enactment (`U.RoleAssignment` + `U.RoleEnactment`) with sensing and execution.*

* **BPMN 2.0 (2011)** — *workflow family*.
  *Scope gist:* flow nodes, sequence flows, participants (design‑time).
  *Trip‑wires:* “process” here is a **graph**; not a run.
* **W3C PROV‑O (2013)** — *provenance family*.
  *Scope gist:* **Activity** that uses/generates entities (run‑time).
  *Trip‑wires:* “activity/process” here is a **temporal occurrence**.
* **ITIL 4 (2020)** — *services family*.
  *Scope gist:* service as value co‑creation; SLO/SLA (deontic talk nearby).
  *Trip‑wires:* “incident/problem/practice” don’t equal workflow tasks.
* **ODRL 2.2** — *deontics family*.
  *Scope gist:* permissions, prohibitions, duties (design).
  *Trip‑wires:* “duty/obligation” ≠ service guarantee mechanics.
* **SOSA/SSN (2017)** — *sensing family*.
  *Scope gist:* Observation as an act yielding a Result for a property.
  *Trip‑wires:* “observation” ≠ “state”; it’s an **act** with a **procedure**.
* **IEC 61131‑3** — *control languages family*.
  *Scope gist:* tasks that **execute** programs (run‑time).
  *Trip‑wires:* “task/execution” ≠ “workflow process”.

> With only these Contexts fixed, later steps become almost mechanical: F.2 harvests terms **inside** each Context; F.3 clusters **within** each Context; F.4 names roles/statuses pointing to **SenseCells**; F.9 draws the bridges you refused to draw here.

## 11 · Anti‑patterns & remedies

| #       | Anti‑pattern               | Symptom in practice                                                                  | Why it harms thinking                                          | Remedy (conceptual move)                                                                                                |
| ------- | -------------------------- | ------------------------------------------------------------------------------------ | -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **A1**  | **“One‑Book Domain”**      | Everything is justified from a single canon (“X is the domain”).                     | Projectionism; blinds heterogeneity; brittle to new editions.  | Enforce **heterogeneity**: pick **≥ 3 distinct domain families** per unification line (§6 Step 2, §8‑3).                |
| **A2**  | **Context‑less talking**   | Words like *process*, *role*, *service* used without naming a Context.                  | Global words drift; later steps must guess meaning.            | Always **prefix with the Context** in thought and prose: *process (BPMN)*, *activity (PROV)*, *service (ITIL)* (§4, §7.2). |
| **A3**  | **Edition blur**           | “BPMN” or “ITIL” cited with no year or profile.                                      | Inadvertent sense shifts; debates about “what the book says.”  | Cards keep **name + edition** on the first line; think with the exact edition (§7.2).                                   |
| **A4**  | **Phonebook survey**       | Dozens of Contexts; no one can recall the cut.                                          | Violates didactic primacy; people default to global talk.      | **Parsimony rule**: 1–3 Contexts per family, just enough to reveal key sense‑splits (§6 Step 5, §8‑4, §9 “memory rule”).   |
| **A5**  | **Bridge‑by‑stealth**      | Phrases like “these are basically the same” inside the survey.                       | Hides losses; imports meaning across Contexts without scrutiny.   | **No bridging here**; write the *itch to bridge* down and defer to **F.9** (§6 Step 6, §8‑5).                           |
| **A6**  | **Role/status conflation** | *Role (RBAC)* treated as behavioural mask; *duty (ODRL)* treated as service runtime. | Category bleed across families.                                | Cards carry **lexical trip‑wires** (“RBAC role ≠ behavioural role”; “duty ≠ runtime guarantee”) (§7.2).                 |
| **A7**  | **Temporal fudge**         | *Activity* or *execution* discussed without run/design stance.                       | Misplaced assertions; design artefacts treated as occurrences. | Cards note **time stance** when inherent (design vs run) (§7.2, §8‑6).                                                  |
| **A8**  | **Domain = Context**       | A “domain” label used as if it were a Context (e.g., “control” == one context).         | Shelf label mistaken for a canon; sense becomes fuzzy.         | **Domain family is informative only**; Contexts are **U.BoundedContext** tied to specific canons (§5, §7.2).               |
| **A9**  | **Context inheritance**    | Arranging Contexts in is‑a hierarchies (“PROV is‑a BPMN”).                              | Suggests meaning flows by inheritance; erases locality.        | **No is‑a among Contexts**; relations between Contexts live in **F.9 bridges** (§8‑5).                                        |
| **A10** | **Didactic bloat**         | Context Card spills into pages of notes.                                             | Teaching burden overwhelms the core idea.                      | **One‑screen Card**; everything else belongs to later patterns (§7.1–§7.2).                                             |
| **A11** | **Family‑based inference** | Treating Domain‑family membership as implying similarity/equivalence. | Smuggles semantics via shelf labels; breaks locality. | **Domain family is informative only**; locality and any Cross‑context relation must be explicit (F.9). |

## 12 · Worked examples (multi‑architheory cuts)

> Each example shows **the cut** (the Contexts you keep in view) and the **thinking pay‑off** you get *before* any harvesting, clustering, or bridging.

### 12.1 Enactment (`U.RoleAssignment` + `U.RoleEnactment`) with sensing & execution (service acceptance)

**Unification line.** Enactment + KD‑CAL (sensing) + Sys‑CAL (execution).

**Contexts (six Cards).**

1. **BPMN 2.0 (2011)** — workflow family; **design**; *graph of flow nodes, participants*.
2. **PROV‑O (2013)** — provenance family; **run**; *Activity uses/generates Entities; Agents*.
3. **ITIL 4 (2020)** — services family; **design**; *service, SLO/SLA vocabulary*.
4. **ODRL 2.2** — deontics family; **design**; *permission / prohibition / duty*.
5. **SOSA/SSN (2017)** — sensing family; **run**; *Observation as act with Result*.
6. **IEC 61131‑3** — control languages; **run**; *tasks execute control programs*.

**Thinking pay‑off (examples).**

* You stop saying “*process uptime*” and think **Execution (IEC)** measured by **Observation (SOSA)** compared against **SLO (ITIL)**—three Contexts, three senses.
* You mark a trip‑wire: **RBAC role** (not in this cut) is *not* a **behavioural role (BPMN participant)**.
* You resist equating **PROV Activity** with **BPMN workflow**; later **F.9** may relate them with explicit loss.

---

### 12.2 Method quartet with types & measurement (model state graph)

**Unification line.** Method‑CAL + Kind-CAL + KD‑CAL.

**Contexts (five Cards).**

1. **SPEM 2.0 / ISO 24744** — methods family; **design**; *Method / MethodDescription language*.
2. **OWL 2 (profiles)** — types family; **design**; *class, subclass, equivalent class*.
3. **FCA corpus** — types family; **design**; *concept lattices*.
4. **SOSA/SSN (2017)** — sensing family; **run**; *Observation / Procedure*.
5. **ISO 80000‑1 (2022)** — metrology family; **design**; *quantity kinds, units*.

**Thinking pay‑off.**

* You keep **Method** (abstract how‑to) separate from **MethodDescription** (epistemic recipe) and **Execution** (run) because the Contexts already split design vs run.
* You avoid treating **FCA “concept”** as a **U.Type**; later F.9 can bridge OWL classes to FCA concepts with cautions.

---

### 12.3 Control & actuation with services (operational SLOs in plants)

**Unification line.** Sys‑CAL + LCA‑CAL (planned) + services/deontics.

**Contexts (five Cards).**

1. **State‑space control texts** — control family; **design**; *controller/plant, feedback*.
2. **IEC 61131‑3** — control languages; **run**; *task, program execution*.
3. **ISA‑95** — integration family; **design**; *levelled layers, interfaces*.
4. **ITIL 4 (2020)** — services family; **design**; *SLO/SLA*.
5. **SOSA/SSN (2017)** — sensing family; **run**; *Observation*.

**Thinking pay‑off.**

* “**Actuation**” is recognised as **control output** (Sys‑CAL), not a *service promise*.
* “**Incident**” (ITIL) is not a plant *fault* (Sys‑CAL); Contexts deter category errors.

---

## 13 · Reasoning primitives (judgement schemas, notation‑free)

> These are **mental moves**, not queries. They read “given these thoughts, this conclusion is safe to hold (conceptually).”

1. **Context set for a line**
   `line L declared ⊢ Contexts(L) = {C₁,…,Cₙ}`
   *Reading:* For a unification line **L**, the Contexts you deliberately keep in view are `{C₁,…,Cₙ}` (from your Cards).

2. **Heterogeneity check**
   `families(L) = F ⊢ heterogeneous(L) ≡ (|distinct(F)| ≥ 3)`
   *Reading:* Your cut is heterogeneous if it spans at least three **domain families**.

3. **Parsimony check**
   `Contexts(L)=R, families(L)=F ⊢ parsimonious(L) ≡ (∀f∈F: 1≤|R∩f|≤3)`
   *Reading:* Each family contributes a few Contexts, not a phonebook.

4. **Locality assertion**
   `term w, C∈Contexts(L) ⊢ meaning(w)@C is local`
   *Reading:* A word’s sense is **context‑local**; no global meaning is implied.

5. **Time‑stance guard**
   `C has stance s∈{design,run} ⊢ claims@C must respect s`
   *Reading:* If a Context is design‑time, do not make run‑time claims in it (and vice versa).

6. **Trip‑wire recall**
   `C lists tripWires T ⊢ for any w∈T, require Context‑prefix when speaking`
   *Reading:* Words on the trip‑wire list must be spoken with the Context name.

7. **Bridge embargo**
   `C₁≠C₂ ⊢ no‑equivalence(C₁,C₂) within F.1`
   *Reading:* F.1 never asserts equivalence across Contexts; postponement is principled, not procrastination.

8. **Context sufficiency probe**
   `common‑word w used in L ∧ w not covered by any trip‑wire ⊢ consider adding a Context that makes w differ`
   *Reading:* If a frequent word has no deliberate sense‑split in your cut, you may be missing a Context.

9. **Memory rule**
   `|Contexts(L)| too large ⊢ reduce until a careful mind can recite them unaided`
   *Reading:* The survey should live in memory, not in a registry.

## F1‑Card example (informative)
```
F1-Card v2025‑Q3:
  taxonomyRef: OpenAlex topics/fields (snapshot 2025‑08)
  embeddingRef: SPECTER2(2023) fine‑tuned@OA‑2025‑08
  DistanceDef: cosine on centroid embeddings (window 36 mo)
  δ_family: 0.35 (calibrated on control set; CI90% [0.33,0.37])
  calibrationSet: 120 labeled pairs (same vs different families)
  edition: 2025‑Q3
```
## 14 · Relations (with other patterns)

**Builds on:**
E.10.D1 **Lexical Discipline for “Context” (D.CTX)** — ensures *Context* ≡ *U.BoundedContext* and reserves “Problem Frame” for narrative use.
A.7 **Strict Distinction** — guards object/description/carrier and design/run splits while you cut Contexts.
A.11 **Ontological Parsimony** — motivates the small cut.

**Constrains:**
**F.2** (Term Harvesting): harvest **inside** Contexts named here; every occurrence carries a Context name.
**F.3** (Intra‑Context Sense Clustering): cluster **per Context**; no Cross‑context sense claims.
**F.4** (Role Descriptions): any role/status template must cite a **SenseCell** that lives in a Context from this cut.
**F.9** (Alignment & Bridge): only F.9 may relate Contexts; never F.1–F.4.

**Used by.**
Architheories in Part C (Sys‑CAL, KD‑CAL, Kind-CAL, Method‑CAL, LCA‑CAL) as the *lexical starting grid* for their examples and definitions.

---

## 15 · Migration notes (conceptual)

1. **New edition appears.** Keep the old Card; add a new Card with the new edition. If the sense shifts, treat it as a **new Context**; if it is strictly editorial, mark recency but keep one context.
2. **New family emerges.** If a missing family explains recurrent confusion in your line, admit it with **one exemplar** Context; remove a less informative Context to keep parsimony.
3. **Language variants.** Treat language editions as **separate Contexts** unless the canon itself declares a single normative bilingual mapping.
4. **Trip‑wire growth.** When you notice a recurring confusion, add a crisp trip‑wire to the relevant Card (one line; no essays).
5. **Bridges discovered later.** Do not back‑port bridges into F.1; leave the Cards untouched and record the mapping in **F.9**.
6. **Dormant Contexts.** If a Context no longer contributes to any active line, move it to a *parking shelf* (informative note on the Card) rather than deleting it.

---

## 16 · Acceptance tests (SCR/RSCR — concept‑level)

### 16.1 Static conformance checks (SCR)

* **SCR‑F1‑S01 (Heterogeneity).** For each unification line, the set of Cards spans **≥ 3 distinct domain families**.
* **SCR‑F1‑S02 (One‑screen Cards).** Each Card fits on one screen: name+edition; family; scope gist; time stance (if inherent); 1–3 trip‑wires; neighbour Contexts (optional); recency note.
* **SCR‑F1‑S03 (Locality pledge).** Nowhere in F.1 are Cross‑context equivalences or merges asserted.
* **SCR‑F1‑S04 (Parsimony).** In every family, **1–3** Contexts are kept; if more, a clear sentence justifies each extra Context’s unique sense contribution.
* **SCR‑F1‑S05 (Context discipline).** “Context” is used only as a synonym of **U.BoundedContext**; “domain” appears only as an informative family label.
* **SCR‑F1‑S06 (Temporal honesty).** If a canon fixes DesignRunTag, the Card states it.
* **SCR‑F1‑S07 (Family neutrality).** No claim, classification, or relation in F.1 relies on Domain‑family membership; families appear only as shelf labels on cards.
* **SCR‑F1‑S08 (dSig present).** Every Context Card has a 5‑characteristics `dSig`.
* **SCR‑F1‑S09 (Collision policy).** Any pair with `dSig` match on ≥3 characteristics is either merged or replaced; SCR records the action.

### 16.2 Regression checks (RSCR)

* **RSCR‑F1‑E01 (Edition churn).** When a new edition is added, prior Cards remain; no silent replacement.
* **RSCR‑F1‑E02 (Family balance).** Adding/removing Cards does not drop any line below **three families**.
* **RSCR‑F1‑E03 (Trip‑wire coverage).** After introducing a new Context, the trip‑wire lists of neighbouring Contexts are reconsidered and updated if needed.
* **RSCR‑F1‑E04 (No creep).** Periodically apply the **memory rule**: if the cut no longer fits in working memory, shrink it.

---

## 17 · Didactic distillation (90‑second teaching script)

> “Before you name anything, **fix the context of meaning**. A *Context* is a **U.BoundedContext** tied to a specific canon—*BPMN 2.0*, *PROV‑O*, *ITIL 4*, *SOSA/SSN*, *IEC 61131‑3*, *OWL 2*. Words are **local to Contexts**: *process (BPMN)* is a workflow graph, *activity (PROV)* is a run‑time occurrence, *service (ITIL)* is a promise vocabulary. Cut the landscape so each unification line sees **at least three domain families**, with **one‑screen Cards** per Context (scope gist, time stance, trip‑wires). **Do not bridge** Contexts here—just write down the itch to bridge and defer it. Keep the cut **small enough to remember**. With Contexts fixed, harvesting (F.2), local clustering (F.3), role/status templates (F.4), and explicit Cross‑context bridges (F.9) become straightforward—and you avoid naming ghosts that come from words floating without walls.”

# F.2 — Term Harvesting & Normalisation \[A] 

**“Harvest words *inside Contexts*, name them in the Context’s own idiom, and stop there.”**
**Status.** Architectural pattern \[A], architheory‑agnostic.
**Depends on.** E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; **F.0.1 Contextual Lexicon Principles** (Source · Local Meaning · Bridge‑Only Crossing); A.7 **Strict Distinction**; A.11 **Ontological Parsimony**.
**Coordinates with.** F.1 **Context Map via Context Cards**; F.3 **Intra‑Context Sense Clustering**; F.4 **Role Description**; F.9 **Alignment & Bridge Across Contexts**.
**Aliases (informative).** *context‑local harvesting*; *Local normalisation*.

---

## 1 · Intent & applicability

**Intent.** Provide a **conceptual** (notation‑free) discipline for turning *Context‑internal usage* into **context‑local lexical units** ready for later reasoning—without Cross‑context merging and without slipping into governance or tooling. The result is a **small, auditable set of context‑local names and glosses** that faithfully reflect how the canon speaks.

**Applicability.** Use whenever a unification line (from F.1) needs **actual words** to be referenced by patterns in Part C (architheories) or by Role Descriptions (F.4). Re‑enter F.2 when a canon/edition changes or when a new Context is admitted in F.1.

**Non‑goals.** No global labels; no Cross‑context equivalence; no workflow or role descriptions; no storage/API talk. F.2 specifies **how to think**, not how to “run a pipeline”.

---

## 2 · Problem Frame

Even with Contexts fixed (F.1), three mistakes recur:

1. **Word‑centrism.** Treating a string as if it carried its meaning across Contexts (*process*, *role*, *service*).
2. **Over‑normalisation.** Forcing one spelling/morphology across different canons, erasing Context‑specific cues.
3. **Premature structure.** Smuggling behaviour, deontics, or type structures into what should remain **lexical**.

F.2 prevents these by **localising** meaning and **naming** strictly **inside** each Context.

---

## 3 · Forces

| Force                      | Tension to resolve                                                               |
| -------------------------- | -------------------------------------------------------------------------------- |
| **Uniformity vs locality** | Desire for consistent names vs Context‑specific idioms that must be preserved.      |
| **Parsimony vs recall**    | Keep the harvested set small vs keep rare but pivotal terms that unlock bridges. |
| **Didactics vs fidelity**  | Two‑register labels (tech/plain) vs fidelity to the canon’s own phraseology.     |
| **Speed vs safety**        | Move fast to enable F.3/F.4 vs avoid any Cross‑context conclusion in F.2.           |

---

## 4 · Core idea (didactic)

**Harvest *inside* each Context; name *in that Context’s idiom*; do not cross Contexts.**
For every Context (a **U.BoundedContext** from F.1), you gather **attested phrases** as *thought‑cues*, choose a **Local Normal Form (LNF)** that matches the Context’s idiom, attach a **two‑register label** (Tech/Plain), and write a **one‑sentence gloss**. That’s all. You do **not** claim sameness with any other Context; you do **not** embed behaviour or deontics; you do **not** mint U.Types here. These *local lexical units* will become **Local‑Senses** in F.3 and later addressable **SenseCells** (Context × Local‑Sense).

---

## 5 · Minimal vocabulary (this pattern only)

* **Context** — Tech‑register alias for **U.BoundedContext** (per E.10.D1).
* **Attested phrase** — A short, verbatim cue from the canon that shows how a word is used **in this Context** (citation idea, not a record format).
* **Local Normal Form (LNF)** — The Context‑specific canonical surface you will use when referring to the term in this Context (minimal editing: spelling/hyphenation/casing per the canon).
* **Two‑register label** — **Tech** (engineer‑facing) and **Plain** (pedagogic) forms for the same Context‑local meaning.
* **Gloss (one‑sentence)** — A **Context‑faithful** description of how the canon uses the term, at **minimal generality**.
* **Local lexical unit** — The quintet *(Context, LNF, Tech, Plain, Gloss)*. This is F.2’s only outcome.
* **Homonymy (signal)** — Awareness that the **same string** has **different local lexical units** across Contexts (no relation asserted).
* **SenseCell** *(appears downstream)* — Address **(Context × Local‑Sense)** minted in F.3; mentioned here so you know what you’re preparing.

> *Everything above is a way of thinking. None of it implies a database, statuses, or roles.*

---

## 6 · Solution — three mental moves (notation‑free)

### Move A — **Localise the word**

**Question to ask.** *“In which Context am I hearing this word?”*
**Action (mental).** Point to a specific **Context** (from F.1). Grab 1–2 **attested phrases** that are representative **in this Context**.
**Outcome.** You stop thinking “global word” and start thinking “context‑local usage”.

*Micro‑cue.* If you cannot name the Context, do not harvest the word.

---

### Move B — **Name it in the Context’s idiom**

**Question to ask.** *“How would this Context itself write it?”*
**Action (mental).** Choose the **LNF** (Context‑conformant spelling/hyphenation). Then write the **two‑register label** and a **one‑sentence gloss** that says **what the canon means here**—nothing more.
**Outcome.** You have a **local lexical unit** *(Context, LNF, Tech, Plain, Gloss)*.

*Micro‑cues.*
• Prefer the canon’s head noun; keep canonical hyphens; avoid invented compounds.
• The **Plain** label should help a non‑specialist; the **Tech** label should match engineers’ eyes.
• The **Gloss** must fit on a single line; defer details to F.3.

---

### Move C — **Fence it off**

**Question to ask.** *“What must I refuse to conclude here?”*
**Action (mental).** Explicitly **refuse** to: (1) compare across Contexts, (2) fold morphology that the canon treats as meaningful, (3) embed behaviour, deontics, or type structure.
**Outcome.** A clean, **context‑local** lexical unit that will be safe to cluster in F.3 and safe to bridge (or not) in F.9.

---

## 7 · Guard‑rails (normative, lightweight)

1. **context‑locality.** Every local lexical unit **MUST** cite a Context (U.BoundedContext from F.1).
2. **Context‑idiom normalisation.** LNF **MUST** respect the Context’s idiom (spelling/hyphenation/casing) and use **minimal edits**.
3. **Two registers.** Each unit **SHOULD** carry both **Tech** and **Plain** labels for didactics; if one is missing, justify.
4. **Minimal generality (G‑1).** The gloss **MUST** be as specific as the Context’s canon requires—no broader.
5. **I/D/S layer hygiene (A.7).** **MUST NOT** include behaviour equations, deontic rules, measurement math, or type axioms; those belong to architheories.
6. **No Cross‑context claims.** **MUST NOT** assert equivalence, subsumption, or similarity with terms in other Contexts (F.9 only).
7. **Edition honesty.** If the Context’s canon has multiple editions with shifting usage, treat them as distinct Contexts in F.1 before harvesting.
8. **Parsimony.** Prefer **few, telling** lexical units over long tails; keep head terms that will power F.3/F.4/F.9.

---

## 8 · Micro‑examples (illustrative, context‑local)

> Each line is *one* local lexical unit. No relations are implied across lines.

* **Context:** *BPMN 2.0 (2011)* — **LNF:** `process`
  **Tech:** `process` · **Plain:** `workflow process`
  **Gloss:** “Directed graph of flow nodes and sequence flows enacted by participants.”

* **Context:** *PROV‑O (2013)* — **LNF:** `activity`
  **Tech:** `activity` · **Plain:** `temporal occurrence`
  **Gloss:** “Time‑bounded occurrence that uses and generates entities and is linked to agents.”

* **Context:** *ITIL 4 (2020)* — **LNF:** `service‑level‑objective`
  **Tech:** `service‑level‑objective` · **Plain:** `service target`
  **Gloss:** “Target value for a service characteristic within a service promise vocabulary.”

* **Context:** *NIST RBAC (2004)* — **LNF:** `role`
  **Tech:** `access‑role` · **Plain:** `permission role`
  **Gloss:** “Named grouping of permissions assignable via sessions.”

* **Context:** *SOSA/SSN (2017)* — **LNF:** `observation`
  **Tech:** `observation` · **Plain:** `measurement act`
  **Gloss:** “Act applying a procedure to a feature of interest to produce a result.”

* **Context:** *IEC 61131‑3* — **LNF:** `task`
  **Tech:** `task` · **Plain:** `runtime program execution`
  **Gloss:** “Cyclic or event‑driven execution unit for control programs.”

---

## 9 · Didactic heuristics (informative)

* **Keep the Context prefix in your inner speech.** Say “*process (BPMN)*”, “*activity (PROV)*”.
* **Prefer head nouns.** If the canon says “service‑level objective”, do not shorten it to “objective”.
* **Resist elegance that erases signal.** Hyphens and case often carry the Context’s culture; keep them.
* **Gloss from use, not from opinion.** Quote in your mind, then compress; avoid importing definitions from neighbouring Contexts.

## 10 · Anti‑patterns & remedies

| #       | Anti‑pattern                 | Symptom (in thought or prose)                                        | Why harmful                                                  | Remedy (conceptual move)                                                                                |
| ------- | ---------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| **A1**  | **Global normal form**       | One “canonical” label reused across Contexts.                           | Erases local meaning; invites stealth bridges.               | Keep **LNF per Context**; any Cross‑context relation belongs to **F.9** only.                                 |
| **A2**  | **String = meaning**         | Assuming identical strings denote one concept across Contexts.          | Homonym collision (*process*, *role*, *service*).            | Always prefix mentally with the **Context**; treat same string in different Contexts as **different units**.  |
| **A3**  | **Over‑normalisation**       | Folding hyphens/case/morphology “for consistency”.                   | Loses the canon’s idiom; breaks citations.                   | **Minimal edits** toward the Context’s idiom; never toward a global house‑style.                           |
| **A4**  | **Headless multiword**       | Truncating to a head (“objective” for “service‑level objective”).    | Ambiguity; collapses scope.                                  | Preserve canonical **head‑modifier** as LNF when meaningful.                                            |
| **A5**  | **Premature structure**      | Embedding behaviour, deontics, units, or type axioms into the gloss. | I/D/S layer mixing (violates A.7); biases later patterns.          | Gloss **usage**, not calculus; structural content belongs to architheories in Part C.                   |
| **A6**  | **Cross‑context folding**       | “BPMN workflow ≈ PROV activity” written inside F.2.                   | Hidden bridge; unpriced losses.                              | No Cross‑context claims in F.2; write the **itch to bridge** for **F.9**.                                  |
| **A7**  | **Edition blur**             | “BPMN” without year/profile; mixing excerpts across editions.        | Silent sense shift; unrepeatable reasoning.                  | Treat distinct editions as **distinct Contexts** in F.1, then harvest.                                     |
| **A8**  | **Vendor‑dialect elevation** | Treating a DSL/keyword list as “the domain”.                         | Projectionism; narrow idiom dominates.                       | If needed, model the DSL as **one context among others**; keep heterogeneity from F.1.                     |
| **A9**  | **Tail chasing**             | Harvesting hundreds of rare terms.                                   | Cognitive overload; dilutes signal.                          | Keep **head terms** that feed F.3/F.4/F.9; justify rare units by their bridging value.                  |
| **A10** | **Fake symmetry**            | Tech and Plain labels are identical jargon.                          | Didactic failure.                                            | Make **Plain** genuinely explanatory; keep **Tech** faithful to the canon.                              |
| **A11** | **Temporal fudge**           | Using run‑time words in design Contexts (or vice versa).                | Category drift; later contradictions.                        | Respect the Context’s **DesignRunTag** from its Card (F.1 §7.2).                                      |
| **A12** | **Cross‑language collapse**  | Merging bilingual terms as one unit.                                 | Erases idiom‑specific signals; hides normative mapping gaps. | Treat each language edition as its **own Context** unless the canon declares a normative mapping.          |
| **A13** | **Alias inflation**          | Inventing new local names “for clarity”.                             | Strays from the canon; hinders bridging.                     | Prefer the canon’s idiom; keep invented phrasings to the **Plain** register only.                       |
| **A14** | **Role/status conflation**   | RBAC “role” glossed as behavioural role.                             | Cross‑family bleed; wrong assignment later.                         | Call out the Context in the label: **access‑role (RBAC)** vs **participant (BPMN)**; keep senses disjoint. |

---

## 11 · Worked examples (multi‑architheory, context‑local only)

> Each line is a **local lexical unit** *(Context, LNF, Tech, Plain, Gloss)*.
> No Cross‑context relation is implied. Later clustering (F.3) and bridges (F.9) may connect them.

### 11.1 Enactment + sensing

* **Context:** *BPMN 2.0 (2011)* — **LNF:** `process`
  **Tech:** `process` · **Plain:** `workflow process`
  **Gloss:** “Directed graph of flow nodes and sequence flows enacted by participants.”

* **Context:** *PROV‑O (2013)* — **LNF:** `activity`
  **Tech:** `activity` · **Plain:** `temporal occurrence`
  **Gloss:** “Time‑bounded occurrence that uses and generates entities and links to agents.”

* **Context:** *SOSA/SSN (2017)* — **LNF:** `observation`
  **Tech:** `observation` · **Plain:** `measurement act`
  **Gloss:** “Act applying a procedure to a feature of interest to produce a result.”

* **Context:** *ITIL 4 (2020)* — **LNF:** `service‑level‑objective`
  **Tech:** `service‑level‑objective` · **Plain:** `service target`
  **Gloss:** “Target value for a service characteristic within a service promise vocabulary.”

*Thinking pay‑off:* you can phrase “compare **observation** to **service‑level‑objective**” without importing workflow or provenance semantics.

---

### 11.2 Sys‑CAL / LCA‑CAL + services

* **Context:** *State‑space control texts* — **LNF:** `actuation`
  **Tech:** `actuation` · **Plain:** `control output`
  **Gloss:** “Signal applied to the plant to influence state/output.”

* **Context:** *IEC 61131‑3* — **LNF:** `task`
  **Tech:** `task` · **Plain:** `runtime program execution`
  **Gloss:** “Cyclic or event‑driven execution unit for control programs.”

* **Context:** *ITIL 4 (2020)* — **LNF:** `incident`
  **Tech:** `incident` · **Plain:** `reported disruption`
  **Gloss:** “Unplanned interruption or reduction in the quality of a service.”

*Thinking pay‑off:* avoids calling a plant fault an “incident” unless you **cross Contexts later** with an explicit bridge.

---

### 11.3 Kind-CAL + Method‑CAL + KD‑CAL

* **Context:** *OWL 2 (profiles)* — **LNF:** `subclass‑of`
  **Tech:** `subclass‑of` · **Plain:** `is‑a (type hierarchy)`
  **Gloss:** “C ⊑ D: every instance of C is an instance of D.”

* **Context:** *FCA corpus* — **LNF:** `formal‑concept`
  **Tech:** `formal‑concept` · **Plain:** `extent–intent node`
  **Gloss:** “Maximal (objects, attributes) pair under a Galois connection.”

* **Context:** *SPEM 2.0 / ISO 24744* — **LNF:** `method`
  **Tech:** `method` · **Plain:** `abstract way of doing`
  **Gloss:** “Abstract how‑to independent of specification or execution.”

* **Context:** *SOSA/SSN (2017)* — **LNF:** `procedure`
  **Tech:** `procedure` · **Plain:** `measurement recipe`
  **Gloss:** “Specification guiding how an observation is produced.”

*Thinking pay‑off:* discourages treating an FCA “concept” as a `U.Type`, or a **procedure** as a **method** without later proof.

---

## 12 · Reasoning primitives (judgement schemas, notation‑free)

> Read each as a **permitted mental move** over the outcomes of F.2.
> Symbols: `R` = Context (U.BoundedContext), `u` = local lexical unit, `s` = surface string.

1. **Localisation**
   `heard(s) ∧ R chosen ⊢ localize(s,R)`
   *You decide to hear `s` only **in** Context `R`.*

2. **Context‑idiom normalisation**
   `localize(s,R) ⊢ LNF_R(s) = ℓ`
   *Within `R`, the **Local Normal Form** for `s` is `ℓ`.*

3. **Unit formation**
   `LNF_R(s)=ℓ ∧ labelTech=t ∧ labelPlain=p ∧ gloss=g ⊢ unit(u) = ⟨R,ℓ,t,p,g⟩`
   *A **local lexical unit** is formed (quintet).*

4. **Lexical‑only guard**
   `unit(u) ⊢ lexicalOnly(u)`
   *No behavioural/deontic/type math is attached to the gloss.*

5. **Homonymy signal (Cross‑context)**
   `LNF_Ra(s)=ℓa ∧ LNF_Rb(s)=ℓb ∧ Ra≠Rb ⊢ homonymy(s) ⊇ {Ra,Rb}`
   *Same string across Contexts is flagged as **different** by default.*

6. **Minimal generality check**
   `unit(u) ⊢ minimal(u) ⇔ gloss(u) says no more than the Context’s usage requires`
   *The gloss fits the Context; broader claims are withheld.*

7. **Two‑register adequacy**
   `unit(u) ⊢ didactic(u) ⇔ (tech(u) faithful) ∧ (plain(u) explanatory)`
   *Tech stays canonical; Plain helps non‑specialists.*

8. **No Cross‑context conclusion**
   `unit(u@Ra), unit(v@Rb), Ra≠Rb ⊢ ¬(u ≡ v) (within F.2)`
   *F.2 never asserts Cross‑context equivalence.*

9. **Ready‑for‑F.3 signal**
   `lexicalOnly(u) ∧ minimal(u) ∧ didactic(u) ⊢ readyF3(u)`
   *A unit is suitable input for **intra‑Context clustering** in F.3.*

---

## 13 · Relations

**Builds on:**
**F.1** (Contexts fixed; heterogeneity/parsimony in place).
**E.10.D1 D.CTX** (Context ≡ U.BoundedContext; “Problem Frame” reserved for narrative).
**F.0.1** (Source · Local Meaning · Bridge‑Only Crossing).

**Constrains:**
**F.3** (Intra‑Context Sense Clustering): operates **only** on units **from one Context**; produces Local‑Senses and addressable **SenseCells**.
**F.4** (Role Description Definition): may **cite SenseCells**, not raw strings.
**F.9** (Alignment & Bridge): consumes **homonymy signals**; declares explicit Cross‑context mappings with loss policies.

**Used by.**
Architheories in Part C when referencing domain idioms (labels stay **context‑local**).

---

## 14 · Migration notes (conceptual)

1. **New edition appears.** Add a Context in F.1; harvest afresh in F.2 using that Context; do not overwrite earlier units.
2. **Idiomatic update discovered.** If your LNF fought the canon’s idiom, **re‑LNF** within the same context; keep labels/glosses steady unless the canon itself differs.
3. **Ambiguity inside a Context.** If use splits, **mint two units** with distinct glosses; F.3 will sort their relation (same/different Local‑Sense).
4. **Language split.** Treat each language canon as its **own Context**; resist cross‑language merges in F.2.
5. **Tail pruning.** If units accumulate without feeding F.3/F.4/F.9, drop them from the working set; keep head terms that carry bridges.
6. **DSL quarantine.** If a tool dialect is unavoidable, keep it as one context among others; never let it define the idiom for other Contexts.

---

## 15 · Acceptance tests (SCR/RSCR — concept‑level)

### 15.1 Static conformance (SCR)

* **SCR‑F2‑S01 (context‑locality).** Every unit cites a Context from F.1.
* **SCR‑F2‑S02 (Idiomatic LNF).** Each LNF reflects the Context’s spelling/hyphenation/casing with **minimal edits**.
* **SCR‑F2‑S03 (Two registers).** Each unit carries both **Tech** and **Plain** labels; if not, a reason exists tied to didactics.
* **SCR‑F2‑S04 (Lexical‑only).** No gloss contains behaviour, deontics, measurement math, or type axioms.
* **SCR‑F2‑S05 (No Cross‑context claims).** Nowhere does F.2 assert equivalence/similarity/subsumption across Contexts.
* **SCR‑F2‑S06 (Minimal generality).** Glosses match the Context’s use; no globalisation.
* **SCR‑F2‑S07 (Temporal honesty).** For Contexts with fixed DesignRunTag, units and glosses respect it.

### 15.2 Regression (RSCR)

* **RSCR‑F2‑E01 (Edition split).** Introducing a new edition yields new units under a new Context; earlier units persist unchanged.
* **RSCR‑F2‑E02 (Normaliser stability).** Adjusting an LNF does not silently widen/narrow the gloss.
* **RSCR‑F2‑E03 (Language split).** Adding a second language yields a second Context; no bilingual collapse in F.2.
* **RSCR‑F2‑E04 (No stealth bridges).** After updates, F.2 still contains **zero** Cross‑context identity claims; any mapping appears only in F.9.
* **RSCR‑F2‑E05 (Head‑term focus).** Periodic check shows the unit set remains small and oriented to F.3/F.4/F.9 needs.

---

## 16 · Didactic distillation (60‑second script)

> “In F.2 you **harvest inside Contexts**. For each Context, pick the canon’s own phrasing, choose a **Local Normal Form** in that idiom, add **Tech** and **Plain** labels, and write a one‑sentence **Gloss** that matches how that Context talks. Stop there. No bridging, no behaviour, no equations. If the same string appears in another Context, treat it as a **different unit**. These units feed F.3, where you’ll sort senses **within** a Context, and F.9, where you’ll relate Contexts explicitly. This keeps meaning local, names faithful, and later reasoning clean.”

# F.3 — Intra‑Context Sense Clustering \[A] 

**“Within one context, decide what ‘the same sense’ really is—before you ever cross Contexts.”**
**Status.** Architectural pattern \[A], architheory‑agnostic.
**Depends on.** F.1 **Domain‑Family Landscape Survey**; F.2 **Term Harvesting & Normalisation**; E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; A.7 **Strict Distinction**; A.11 **Ontological Parsimony**.
**Coordinates with.** F.4 **Role Description**; F.7 **Concept‑Set Table**; F.8 **Mint or Reuse Decision**; F.9 **Alignment & Bridge Across Contexts**.
**Aliases (informative).** *context‑local clustering*; *Sense consolidation*.

---

## 1 · Intent & applicability

**Intent.** Consolidate the **context‑local lexical units** from F.2 into a **small set of Local‑Senses** that actually operate in that **one context (U.BoundedContext)**. Each Local‑Sense receives a crisp, didactic label pair (Tech/Plain) and a short sense statement. The result is an **addressable basis** for later uses (Role Assignment, tables, bridges) that is **still strictly context‑local**.

**Applicability.** Apply **after** F.2 for any Context that will feed naming (F.4/F.5), decision gates (F.8), Cross‑context bridges (F.9), or exemplars in Part C. Use again whenever the canon (edition) **shifts usage** enough to split or merge senses **within the same context**.

**Non‑goals.** No Cross‑context comparison or merging. No behaviour/deontics/type mathematics. No storage schemas or workflows. This is **pure sense‑making** inside one context.

---

## 2 · Problem Frame

context‑local units (LNF + labels + gloss) from F.2 often **over‑ or under‑differentiate** meaning:

1. **Over‑split:** superficial variants (*service‑level‑objective* vs *SLO*) treated as different “things”.
2. **Under‑split:** one gloss covering **two selectional frames** or incompatible use‑cases.
3. **Drift within a canon:** multi‑chapter texts use the same head differently unless the reader **consolidates** the intended sense.
4. **Didactic mismatch:** engineer‑friendly label and plain label drift apart when units remain too granular.

F.3 repairs this **inside the Context** by clustering “same sense” and distinguishing “different sense”, with **parsimony**.

---

## 3 · Forces

| Force                     | Tension to resolve                                                                                               |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Parsimony vs fidelity** | Few Local‑Senses ease teaching; too few dilute real distinctions the canon relies on.                            |
| **Usage vs definition**   | Glosses should reflect **how the canon uses the word**, not an imported dictionary definition.                   |
| **Labels vs idiom**       | Tech label must stay in the canon’s idiom; Plain label must help newcomers—without inventing a new sense.        |
| **Stability vs openness** | Consolidated senses must be stable enough for Role Descriptions and tables, yet revisable when the canon’s use clearly splits. |

## 4 · Core idea (didactic)

**Cluster by usage, not by string.**
Inside one context:

* **Same sense** → **Local‑Sense**: a small, coherent usage‑region the canon treats as one idea (even if it has aliases or minor surface variation).
* **Different sense** → **two Local‑Senses**: incompatible selectional frames, entailments, or role in the canon’s own statements.

Each Local‑Sense becomes **addressable** when paired with its Context: **SenseCell = (Context × Local‑Sense)**. SenseCells are **context‑local coordinates**; they do not pre‑judge any Cross‑context mapping.

---

## 5 · Minimal vocabulary (this pattern only)

* **Context** — short for `U.BoundedContext` (per D.CTX).
* **Unit** — a context‑local lexical unit from F.2 (LNF + Tech/Plain + gloss).
* **Local‑Sense** — the **conceptual cluster** of Units deemed “same sense” **within that Context**.
* **SenseCell** — the **address** for a Local‑Sense: *(Context, Local‑Sense)*. This is what later patterns will **cite**.
* **Counter‑example** — a short, canonical sentence or use that **must not** be covered by the Local‑Sense; it sharpens the boundary.
* **Usage cue** *(informative)* — a clue from usage (collocational patterns, paraphrases, entailments in the canon) that **suggests** merge or split. Cues **do not decide**; the canon’s intent does.

---

## 6 · Solution — how to think the clustering (notation‑free)

> What follows are **mental moves**, not steps for a team. Use them as probes until the Context’s usage partitions itself naturally.

**6.1 Consolidate aliases into one Local‑Sense.**
If Units differ only by **orthography, abbreviation, or canon‑blessed synonymy** and are **used interchangeably** in the Context’s own sentences, treat them as **one Local‑Sense**.
*Example (ITIL):* *service‑level‑objective* and *SLO* → one Local‑Sense.

**6.2 Split on incompatible selectional frames.**
If the same head pairs with **different kinds of arguments** or plays **different roles** in the canon’s statements (and those roles cannot both be true at once), split.
*Example (BPMN):* *event* as **node type** vs as **occurrence narrative** in a tutorial → two Local‑Senses; adopt the **node type** sense if that is the normative layer.

**6.3 Split on entailments that pull apart.**
If paraphrases lead to **different entailments** (e.g., one implies temporality, another structural position), you have two senses.
*Example (PROV):* *activity* implies **time‑bounded use/generate**; it cannot be the same sense as a **static capability**.

**6.4 Prefer sense minimality.**
If two candidate Local‑Senses never lead to **different conclusions** in the Context’s own use, merge them. If they sometimes do, split them—and record a **counter‑example** to keep the boundary crisp.

**6.5 Keep Tech label idiomatic; Plain label helpful.**
Tech label stays as the canon speaks; Plain label conveys the **function** of the sense to a careful newcomer. Neither label may **broaden** the sense beyond usage.

**6.6 Name only as much as you will use.**
If a fine-grained split has **no downstream consequence** (Role Descriptions, tables, bridges), prefer the coarser Local-Sense.

---

## 7 · Outputs (conceptual, not clerical)

F.3 yields, **per Context**:

1. A **small set of Local‑Senses**, each with:

   * **Label pair**: *Tech* (idiomatic) · *Plain* (didactic).
   * **Sense line**: one‑sentence usage statement, in the Context’s voice.
   * **Inside list** (informative): which Units from F.2 it consolidates.
   * **Counter‑example** (optional but powerful): a short use that must **not** be included.
1. A **SenseCell address** for each Local‑Sense: *(Context, Local‑Sense)*.

These are **thinking reference points** (cognitive only), not records or files. Later patterns **cite SenseCells by name**; nothing about storage is implied.

---

## 8 · Invariants (normative, lightweight)

1. **context‑locality.** Every Local‑Sense belongs to **exactly one context**. No Cross‑context clustering.
2. **Parsimony.** Local‑Senses are **few**; prefer the coarsest partition that preserves the canon’s distinctions.
3. **Idiomatic Tech.** The Tech label **must** stay in the Context’s idiom; no house‑style overrides.
4. **Didactic Plain.** The Plain label **must** aid comprehension **without adding scope**.
5. **Usage‑first.** Sense lines reflect the **canon’s usage**, not imported taxonomies or external theories.
6. **Counter‑examples rule.** If a counter‑example exists that the sense would wrongly include, **split**.
7. **No behaviour math.** Sense lines contain **no** behavioural, deontic, metrological, or type calculus; those live in Part C.
8. **Temporal honesty.** If the Context fixes **DesignRunTag**, the sense line respects it (e.g., PROV *activity* is **run‑time**).

---

## 9 · Self‑checks (mental probes)

* **Same‑conclusion test.** Do two candidate senses ever lead to **different conclusions** in the canon? If not, merge.
* **Argument‑slot probe.** Replace arguments in canonical sentences; do both candidates still read true? If one fails, split.
* **Label inversion.** Read the Plain label alone: does it tempt you to over‑generalise? If yes, tighten it.
* **Counter‑example ping.** Can you state a **ten‑word** use that the sense must exclude? If you can, write it; if you cannot, your sense may be too broad.
* **Memory rule.** Can you recall the Context’s Local‑Senses **without notes**? If not, you split too finely.

## 10 · Anti‑patterns & remedies

| #       | Anti‑pattern               | Symptom in thought                                                            | Why it harms                                            | Remedy (conceptual move)                                                                                          |
| ------- | -------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **A1**  | **String = Sense**         | Treating surface identity (*service*, *SLO*) as sameness of meaning.          | Collapses distinct uses; hides selectional differences. | Compare **selectional frames** and entailments inside the Context; merge only if conclusions never diverge.          |
| **A2**  | **Cross‑context creep**       | Folding BPMN *process* with PROV *activity* while clustering **inside** BPMN. | Imports foreign usage; violates locality.               | Constrain attention to **one context**; postpone Cross‑context talk to F.9.                                             |
| **A3**  | **Over‑granulation**       | Splitting minor orthographic variants (*service‑level‑objective* vs *SLO*).   | Adds friction; no conceptual gain.                      | Consolidate **canon‑blessed aliases** into one Local‑Sense.                                                       |
| **A4**  | **Under‑granulation**      | One sense for incompatible roles (*event* as node‑type vs occurrence).        | Causes contradictory inferences later.                  | Split on **role/entailment** conflict; add a **counter‑example** to sharpen the cut.                              |
| **A5**  | **Imported definitions**   | Borrowing dictionary glosses not used in the canon.                           | Drifts from the Context’s idiom; confuses labels.          | Ground every sense line in **statements the canon actually makes**.                                               |
| **A6**  | **Label drift**            | Tech label in canon idiom; Plain label broadens scope.                        | Teaches the wrong thing; leaks meaning.                 | Keep **Tech** idiomatic; make **Plain** helpful yet strictly **within** the same usage.                           |
| **A7**  | **Behaviour/math leakage** | Sense lines include runtime metrics, deontic rules, type axioms.              | Mixes I/D/S layers; duplicates Part C work.                   | Sense lines are **usage‑only**; no equations, no policies.                                                        |
| **A8**  | **Edition blend**          | Mixing 2011 and 2020 usage under one Local‑Sense.                             | Hidden shifts; brittle bridges later.                   | If usage changed with edition, treat as **different Contexts** (F.1) or distinct Local‑Senses with **edition note**. |
| **A9**  | **Collocate worship**      | Declaring sameness solely from similar nearby words.                          | Correlates ≠ causes; misses entailments.                | Use collocates as **cues**, then decide by **entailment/role** checks.                                            |
| **A10** | **Temporal fudge**         | Treating a design‑time sense as if it were run‑time (or vice versa).          | Category errors at enactment.                           | Respect the Context’s **time stance**; keep senses aligned to *design* or *run* as declared in F.1.                  |

---

## 11 · Local‑Sense Cards (one‑glance form)

> A **Local‑Sense Card** is a **one‑glance** sketch per sense in a Context. It teaches faster than prose lists and keeps senses crisp.

**Fields (thought‑items, not fields to fill):**

* **Context** (U.BoundedContext, edition)
* **Label pair** — **Tech** (idiomatic) · **Plain** (didactic)
* **Sense line** — one sentence in the Context’s voice
* **Inside** — which F.2 Units it consolidates (names only)
* **Counter‑example** — a short use that must **not** be included

---

## 12 · Worked examples (multi‑architheory, all **intra‑Context**)

### 12.1 BPMN 2.0 (workflow Context)

**Card A — “process (graph)”**

* **Label**: Tech **process** · Plain **workflow graph**
* **Sense line**: A BPMN **graph of flow nodes and sequence flows** **specifying orchestration among participants** *(design‑time)*.
* **Inside**: *process*, *process model*, *business process* (when used as diagram).
* **Counter‑example**: *“This process took 5 minutes”* ← **runtime** occurrence, **not** this sense.

**Card B — “event (node‑type)”**

* **Label**: Tech **event (node)** · Plain **event symbol**
* **Sense line**: A **node‑type** that marks starts, ends, and intermediates; typed by trigger/result.
* **Inside**: *start event*, *message event*, *end event*.
* **Counter‑example**: *“The outage event happened at 13:05”* ← narrative occurrence, **not** the node‑type.

> **Outcome:** “Process uptime” is rejected as a BPMN sense; Execution belongs to another Context.

---

### 12.2 PROV‑O (provenance Context)

**Card C — “activity (run)”**

* **Label**: Tech **activity** · Plain **time‑bounded execution**
* **Sense line**: An **occurrence** that **uses** and **generates** entities; linked to agents; has start/end.
* **Inside**: *activity*, *execution* (when PROV authors use it).
* **Counter‑example**: *“Sorting algorithm”* ← capability/method, **not** an occurrence.

**Card D — “agent (provenance)”**

* **Label**: Tech **agent** · Plain **provenance actor**
* **Sense line**: Thing that bears **responsibility** for an activity’s effects (person, org, software).
* **Inside**: *agent*.
* **Counter‑example**: *“RBAC role”* ← access status, **not** a PROV agent.

---

### 12.3 ITIL 4 (services Context)

**Card E — “service‑level objective”**

* **Label**: Tech **SLO** · Plain **service target**
* **Sense line**: A **target value/range** for a **service characteristic** used to define acceptable service.
* **Inside**: *service‑level objective*, *SLO*.
* **Counter‑example**: *“Actual availability 99.5%”* ← observation, **not** the target.

**Card F — “incident”**

* **Label**: Tech **incident** · Plain **service disruption**
* **Sense line**: An **unplanned interruption** or reduction in quality of a service.
* **Inside**: *incident*.
* **Counter‑example**: *“Fault in plant sensor”* ← Sys‑CAL fault; different Context.

---

### 12.4 SOSA/SSN (sensing Context)

**Card G — “observation (act)”**

* **Label**: Tech **observation** · Plain **measurement act**
* **Sense line**: An **act** applying a **Procedure** to a **FeatureOfInterest** to yield a **Result** for a property.
* **Inside**: *observation*.
* **Counter‑example**: *“Temperature is 20 °C”* ← **result value**, not the act.

---

### 12.5 OWL 2 (types Context)

**Card H — “subclass‑of”**

* **Label**: Tech **subclass‑of** (⊑) · Plain **is‑a (class)**
* **Sense line**: A **class inclusion**: every instance of **C** is an instance of **D**.
* **Inside**: *SubClassOf*, *is‑a* (when authors use it for classes).
* **Counter‑example**: *rdf\:type* (instance‑of) — not class inclusion.

**Card I — “equivalent‑class”**

* **Label**: Tech **equivalent‑class** · Plain **same class extension**
* **Sense line**: Mutual class identity by extension; two labels for **the same** set of instances.
* **Inside**: *EquivalentClasses*.
* **Counter‑example**: *owl\:sameAs* (individual identity), different predicate.

---

### 12.6 IEC 61131‑3 (control‑runtime Context)

**Card J — “task (runtime)”**

* **Label**: Tech **task** · Plain **program runner**
* **Sense line**: A **cyclic or event‑driven** execution unit that **invokes programs** on schedule or trigger.
* **Inside**: *task*.
* **Counter‑example**: *“Control algorithm”* ← design/method, not the runtime task.

---

## 13 · Reasoning primitives (judgement schemas, notation‑free)

> Each schema captures a **safe mental move**. It implies no storage, API, or workflow.

1. **Alias‑to‑sense consolidation**
   `Context C ⊢ interchangeable(U₁,…,Uₖ) ⇒ Local‑Sense σ`
   *Reading:* If Units are used interchangeably **by the canon** in **C**, consolidate them into one Local‑Sense **σ**.

2. **Selectional‑frame split**
   `C ⊢ frames(U) = F, frames(V) = G, F ∩ G = ∅ ⇒ split(U,V)`
   *Reading:* In **C**, if the argument/role patterns do not overlap, treat as **different senses**.

3. **Entailment divergence**
   `C ⊢ entail(U) ≠ entail(V) on canonical paraphrases ⇒ split(U,V)`
   *Reading:* If paraphrases lead to **different conclusions** in the canon, split.

4. **Parsimony merge**
   `C ⊢ no‑test distinguishes {U₁,…,Uₖ} ⇒ merge(U₁,…,Uₖ)`
   *Reading:* If no canonical test yields a difference, merge into one sense.

5. **Counter‑example trigger**
   `C ⊢ ∃e: e should not be covered by σ ⇒ refine(σ)`
   *Reading:* A crisp counter‑example forces a narrower sense (split or relabel).

6. **Idiomatic Tech, faithful Plain**
   `C ⊢ labelTech(σ) in idiom(C) ∧ labelPlain(σ) ⊆ usage(σ)`
   *Reading:* Tech label speaks the canon; Plain label does not widen the sense.

7. **SenseCell address**
   `C ⊢ σ ⇒ SenseCell ⟨C,σ⟩`
   *Reading:* Pair each Local‑Sense with its Context to form an address used downstream.

8. **Temporal guard**
   `stance(C)=design ⇒ forbid(run‑claims in σ)` (and symmetrically)
   *Reading:* Sense lines must not cross the Context’s DesignRunTag.

9. **Edition guard**
   `C≠C′ (different editions with usage shift) ⇒ no‑merge(σ@C, τ@C′)`
   *Reading:* Do not merge senses across Contexts when editions shift usage.

10. **Completeness ping (optional)**
    `frequent head w in C ∧ no Local‑Sense on w ⇒ consider(sense for w)`
    *Reading:* If a common head lacks a sense, you may be missing a useful consolidation (within C).

---

## 14 · Relations

**Builds on:**
F.1 **Domain‑Family Landscape Survey** (Contexts fixed); F.2 **Term Harvesting** (Units ready); E.10.D1 **D.CTX** (Context discipline); A.7 **Strict Distinction**.

**Constrains:**

* **F.4 Role Description.** Role Descriptions **cite SenseCells**; they do **not** invent senses.
* **F.7 Concept‑Set Table.** Rows are built from **SenseCells** (later Cross‑context assembly); intra‑Context clarity here prevents row bloat.
* **F.8 Mint or Reuse Decision.** Decisions compare proposed names to **existing SenseCells** to avoid type inflation.
* **F.9 Alignment & Bridge.** Bridges connect **SenseCell ↔ SenseCell** across Contexts; F.3 provides the stable endpoints.

**Is used by.**
Part C architheories to ground examples and invariants in **Context‑true** language.

---

## 15 · Migration notes (conceptual)

1. **Usage clarifies → merge.** If two Local‑Senses never lead to different conclusions in the Context’s canon, **merge** and keep the narrower sense line.
2. **Usage diverges → split.** If new reading reveals incompatible roles/entailments, **split** and attach a counter‑example to each side.
3. **Edition change → new Context.** When a new edition **reframes** usage, treat it as a **separate Context** (F.1) and re‑cluster there.
4. **Label upkeep.** If the Plain label tempts broadening, tighten it; if the Tech label drifts from idiom, restore the canon term.
5. **Dormant sense.** If a Local‑Sense ceases to matter for any active line, leave it listed but mark it **low‑use** in your own notes; do not fold it into another unless rule 1 holds.
6. **Bridge temptation.** Record tensions to bridge **elsewhere**; F.3 never resolves Cross‑context relations.

---

## 16 · Acceptance tests (SCR/RSCR — concept‑level)

### 16.1 Static conformance (SCR)

* **SCR‑F3‑S01 (context‑locality).** Every Local‑Sense is paired with **exactly one context**; no Cross‑context clustering appears.
* **SCR‑F3‑S02 (Label pair).** Each Local‑Sense has **Tech** (idiomatic) and **Plain** (didactic) labels; neither widens usage beyond the sense line.
* **SCR‑F3‑S03 (Sense line fidelity).** Each sense line is **grounded in canonical statements** of the Context; no behaviour/deontic/math content.
* **SCR‑F3‑S04 (Parsimony).** The set of Local‑Senses per Context is small enough to **recall unaided** by a careful mind.
* **SCR‑F3‑S05 (Counter‑example presence).** For any ambiguous head, at least one **counter‑example** is recorded to guard the boundary.
* **SCR‑F3‑S06 (Temporal honesty).** Where the Context has a declared stance, sense lines **respect design/run**.

### 16.2 Regression (RSCR)

* **RSCR‑F3‑E01 (Merge soundness).** Every merge is justified by a **failed distinction test** (no selectional or entailment difference).
* **RSCR‑F3‑E02 (Split necessity).** Every split cites a **role/entailment conflict** or a concrete **counter‑example**.
* **RSCR‑F3‑E03 (Edition guard).** No Local‑Sense spans Contexts that differ by edition **with usage shift**.
* **RSCR‑F3‑E04 (Label stability).** Changes to labels do **not** change sense; if they do, the change is treated as a split/merge per E01/E02.
* **RSCR‑F3‑E05 (Downstream continuity).** After splits/merges, **SenseCell** references in F.4/F.7/F.9 remain **referentially clear** (new addresses are explicit; no silent aliasing).

---

## 17 · Didactic close (60‑second recap)

> **Within one context,** collect how the canon actually **uses** a head, not how we wish it did. **Merge** aliases that never lead to different conclusions; **split** uses that do. Give each consolidated use a crisp **Tech** label in the Context’s idiom and a faithful **Plain** label. The pair *(Context, Local-Sense)* is your **SenseCell**—the address later cited by Role Descriptions, tables, and bridges. No Cross‑context mergers here; that job belongs to F.9. Keep senses few, boundaries sharp, and labels honest.

## F.4 — Role Description (RCS + RoleStateGraph + Checklists) \[A] 

**“Name the mask or the badge — and say what it commits to — but only inside a Context.”**
**Status.** Architectural pattern \[A], architheory‑agnostic.
**Depends on.** E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; **E.10.D2 Intension–Description–Specification Discipline**; F.1 **Domain‑Family Landscape Survey**; F.2 **Term Harvesting**; F.3 **Intra‑Context Sense Clustering**; A.2.1 **`U.RoleAssignment`**; A.7 **Strict Distinction**; A.11 **Ontological Parsimony**.
**Coordinates with.** F.5 **Naming Discipline for U.Types & Roles**; F.7 **Concept‑Set Table**; F.9 **Alignment & Bridge Across Contexts**; B.3 **Trust & Assurance Calculus** (for later status evaluation).
**Aliases (informative).** *Mask/Badge card*; *role card* (plain only).

### 1 · Intent & applicability

**Intent.** Provide a **conceptual template** for two kinds of assignables:

* **Role Template** — a **behavioural mask** that a holder can wear **in a specific Context** (U.BoundedContext), shaping how it **acts** (via Method/Execution relations).
* **Status Template** — an **epistemic or deontic badge** that a holder (or artefact, event, claim) can **bear** inside a Context, shaping how it is **treated** (evaluation, permission, standing).

Each template is **grounded in a SenseCell** `⟨Context, Local‑Sense⟩` from F.3 and declares **minimal invariants** that later **assignments** must satisfy. No Cross‑context meaning is imported here.

**Applicability.** Whenever you need to **speak precisely** about what it means to be *a Participant (BPMN)*, *hold an access‑role (RBAC)*, *be an Incident (ITIL)*, or *carry a Verified status (evidence line)*, before minting U.Types or drawing Cross‑context bridges.

**Non‑goals.** No workflows, no storage, no editors. No equations for assurance or control; those live in Part B/C. This pattern describes **how to think and speak** about assignables — not how to manage files.

### 2 · Problem frame

Without explicit Role Descriptions:

1. **Role/status conflation.** Access **role** (RBAC) treated as behavioural **mask** (BPMN participant); deontic **duty** treated as runtime **effect**.
2. **Context drift.** A “role” quietly starts meaning different things across canons; later assignments contradict each other.
3. **Hidden commitments.** We name a role/status but never state what **must hold** when it is assigned; downstream reasoning becomes arbitrary.
4. **Premature unification.** A single template tries to straddle several Contexts; losses remain implicit.

### 3 · Forces

| Force                         | Tension to resolve                                                                                                           |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Behaviour vs knowledge**    | A role changes how the holder **acts**; a status changes how the holder is **treated/assessed**. Keep **I/D/S layers** separate (E.10.D2; A.7). |
| **Locality vs reuse**         | We want reusable templates, yet meanings are **context‑local** (E.10.D1, F.1).                                                   |
| **Minimality vs sufficiency** | Invariants must be **few** and **decisive**; too many become pseudo‑procedures.                                              |
| **Didactics vs fidelity**     | A one‑screen card must be **teachable** without betraying the canon.                                                         |

---

### 4 · Minimal vocabulary (this pattern only)

* **Context** — **U.BoundedContext** (per E.10.D1).
* **Local‑Sense** — a consolidated sense in a Context (F.3).
* **SenseCell** — the address `⟨Context, Local‑Sense⟩`.
* **Role Template** — behavioural mask defined **in** a Context, later bound by **`U.RoleAssignment`**.
* **Status Template** — epistemic/deontic badge defined **in** a Context, later asserted as a **claim** about a holder/artefact.
* **Holder** — the thing that may wear a mask or carry a badge (e.g., a **U.System**, **U.MethodDescription**, **U.Work**, **U.Episteme**).

### 5 · Core idea (didactic)

**A Role Description is a small card that says:**
**(i)** *which Context’s sense it relies on* (**SenseCell**),
**(ii)** *what label we use to speak about it* (Tech & Plain), and
**(iii)** *what must hold* when someone **wears** the mask (Role) or **bears** the badge (Status).

It is **not** a definition by prose alone; it is a **pledge of invariants** — minimal, Context‑true, and later checkable.

### 6 · The Role Description Card (one‑screen sketch)

> Each bullet is a **thought‑item**, not a file field.

**Header**

* **Template kind:** **Role** | **Status**
* **Label pair:** **Tech** (idiomatic) · **Plain** (didactic)  *(naming discipline in F.5)*
* **SenseCell:** `⟨ContextId, Local‑Sense label⟩`

**Applicability**

* **Holder scope:** what can wear/bear it (e.g., *U.System*, *U.Work*, *U.MethodDescription*, *U.Episteme*).
* **Time stance:** **design** / **run** aligned to the Context (F.1).
* **Preconditions (Context‑true):** crisp conditions that must already be true in the Context’s idiom.

**Invariants (minimal)**

* **Behavioural invariants (Role)** *or* **Evaluation invariants (Status)** — 2–5 short lines stating what **must** hold after assignment/assertion, using the Context’s vocabulary and SenseCells where needed.
* **Separation guard:** a one‑line reminder of what this template **does not** imply (prevents senseFamily mixing).

**Consequences (informative)**

* **Typical interactions:** which **Method/Execution/Observation** constructs (by SenseCell) this template usually touches — *names only*.
* **Common misreads (trip‑wire):** 1–2 bullets to prevent known confusions.

> **Memory rule:** If your card can’t be read in **under two minutes**, you are writing a manual, not a template.

**Autonomy hooks (when Role may act autonomously)**
* **RCS additions (illustrative):** `AgencyLevel ∈ {None, Assisted, Delegated, Autonomous}`, `SafetyCriticality ∈ {SC0..SC3}`.
* **RSG gate:** mark which **states are enactable under autonomy** (cf. A.2.5); link to `AutonomyBudgetDeclRef`.
* **References:** If autonomy is claimed for this Role, the Role Description **MUST** reference: `AutonomyBudgetDeclRef` (id, version), `Aut-Guard policy-id`, `OverrideProtocolRef`.
* **Checklist:** include a **pre‑enactment** checklist item “Autonomy Green‑Gate passed” (guard verdicts present).

### 7 · Normative invariants (template discipline)

1. **context‑local grounding.** Every Role Description **MUST** cite exactly one **SenseCell** as its semantic locus.
2. **I/D/S layer separation.**
   * A **Role Template** **MUST NOT** encode deontic, access, or measurement rules.
   * A **Status Template** **MUST NOT** encode behaviour or control flow.
1. **Time honesty.** The card’s stance (**design/run**) **MUST** match the Context’s stance (F.1).
2. **Minimality.** Invariants **SHOULD** be the **fewest that decide** the assignment; avoid procedural sequences.
3. **No Cross‑context smuggling.** A single card **MUST NOT** import foreign semantics; if two Contexts are needed, the relation is handled later in **F.9**.
4. **Label fidelity.** **Tech** label **MUST** be idiomatic to the Context; **Plain** label **MUST** not widen the sense (F.3).
5. **Binding Standard (roles).** A **Role Template** is the **design‑time mask**; at run‑time, a **`U.RoleAssignment`** creates **System‑in‑Role** instances that are subject to the card’s invariants.
6. **Assertion Standard (statuses).** A **Status Template** is a **badge**; asserting it **commits** to the card’s evaluation invariants and to the Context’s way of checking them (later anchored via SenseCells, not formulas here).

### 8 · Reasoning primitives (judgement schemas, notation‑free)

> Conceptual moves only; no APIs, no data stores.

1. **Template grounding**
   `Template T cites SenseCell ⟨C,σ⟩ ⊢ meaning(T) is local to C`
   *Reading:* The template’s meaning is **context‑local**.

2. **Role assignability**
   `holder h, RoleTemplate T, preconds_T(h) ⊢ assignable(h,T)`
   *Reading:* If the **preconditions** hold for **h**, it is **eligible** to wear the mask **T**.

3. **Role assignment obligation**
   `assignable(h,T) ∧ bind(h,T: C) ⊢ invariants_T(h) must hold`
   *Reading:* Once bound (via **`U.RoleAssignment`**), **h** must satisfy **T**’s behavioural invariants.

4. **Status assertability**
   `StatusTemplate S, evidence_in_C supports S for x ⊢ assertable(x,S)`
   *Reading:* If evidence **in the Context C** supports **S** for **x**, the badge is **assertable** (details of evidence logic live in Part B).

5. **Status consequence**
   `assertable(x,S) ∧ assert(x,S) ⊢ evaluation_invariants_S(x)`
   *Reading:* Once asserted, **S**’s evaluation invariants constrain how **x** is treated.

6. **Separation guard**
   `RoleTemplate T ⊢ not(deontic_implied(T))` · `StatusTemplate S ⊢ not(behaviour_implied(S))`
   *Reading:* Wearing a mask doesn’t grant permissions; carrying a badge doesn’t define behaviour.

7. **Bridge embargo**
   `T cites ⟨C,σ⟩ ∧ C≠C′ ⊢ no‑equivalence(T@C, −) inside F.4`
   *Reading:* No Cross‑context equivalence is asserted here; use **F.9** later.

### 9 · Worked examples (multi‑architheory, Context‑true)

> Illustrative cards only; names are **tech/plain labels**, not final U.Type IDs (F.5 will govern naming).

#### 9.1 **Role Template:** *participant (workflow actor)* — Context: **BPMN 2.0 (2011)**

* **Kind:** Role
* **Label:** Tech **participant** · Plain **workflow actor**
* **SenseCell:** `⟨BPMN_2_0, participant (actor in workflow)⟩`
* **Holder scope:** **U.System** (organisation, team, service)
* **Time stance:** **design**
* **Preconditions:** Holder is addressable as a **lane/pool** in the workflow model.
* **Behavioural invariants:**

  1. Activities **assigned to** the participant appear in its lane/pool.
  2. The participant **interacts** through message flows at its boundaries.
  3. The participant **does not** define run‑time occurrence; it **structures** the model.
* **Separation guard:** No permissions implied; no execution logs implied.
* **Typical interactions (informative):** BPMN **process (graph)**; message **event (node)**.
* **Common misreads:** ≠ **RBAC role**; ≠ **PROV Activity**.

#### 9.2 **Status Template:** *access‑role membership* — Context: **NIST RBAC (2004)**

* **Kind:** Status
* **Label:** Tech **access‑role** · Plain **permission role**
* **SenseCell:** `⟨NIST_RBAC_2004, role (permission grouping)⟩`
* **Holder scope:** **U.System** (user/session)
* **Time stance:** **run**
* **Preconditions:** A defined set of **permissions** exists for the role.
* **Evaluation invariants:**

  1. If **x** carries this badge, **x**’s session inherits exactly the role’s **permissions**.
  2. The badge **does not** describe behaviour in a workflow; it determines **access**.
* **Separation guard:** No commitment about BPMN assignment; no deontic duties.
* **Typical interactions (informative):** **permission**, **session** (RBAC).
* **Common misreads:** ≠ **participant (BPMN)**; ≠ **person** as an ontological type.

#### 9.3 **Status Template:** *incident (service disruption)* — Context: **ITIL 4 (2020)**

* **Kind:** Status
* **Label:** Tech **incident** · Plain **service disruption**
* **SenseCell:** `⟨ITIL4_2020, incident (service quality drop)⟩`
* **Holder scope:** **U.Work** (recorded occurrence affecting a service)
* **Time stance:** **run**
* **Preconditions:** A **service** exists with declared **SLOs/quality metrics**.
* **Evaluation invariants:**

  1. The occurrence **reduces** service quality below acceptable levels.
  2. It triggers **restoration activities** per service practice (names only).
* **Separation guard:** Not a plant **fault**; not a BPMN **event node**.
* **Typical interactions:** **SLO** (ITIL), **Observation** (SOSA) — names only.
* **Common misreads:** ≠ **problem** (root cause category).

#### 9.4 **Role Template:** *task runner (control runtime)* — Context: **IEC 61131‑3**

* **Kind:** Role
* **Label:** Tech **task** · Plain **program runner**
* **SenseCell:** `⟨IEC_61131_3, task (runtime execution unit)⟩`
* **Holder scope:** **U.System** (controller CPU/task scheduler)
* **Time stance:** **run**
* **Preconditions:** A program is **registered** for cyclic/event execution.
* **Behavioural invariants:**

  1. Invokes assigned program according to **cycle/trigger**.
  2. Provides **schedule constraints** (period/priority) to its program.
* **Separation guard:** No claim about **deontic** guarantees or **service** targets.
* **Typical interactions:** **Execution** (A.15 family), **Actuation** (Sys‑CAL).
* **Common misreads:** ≠ **workflow task**; ≠ **algorithm** (design).

### 10 · Anti‑patterns & remedies

| #       | Anti‑pattern            | Symptom (in a card)                                                       | Why it harms thinking                                    | Remedy (conceptual move)                                                                                        |
| ------- | ----------------------- | ------------------------------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **A1**  | **Role⇄Status blur**    | A Role card says “grants permission”; a Status card dictates behaviour.   | **senseFamily mixing (Role vs Status)**; incoherent assignments.              | Move permission talk to a **Status**; keep Role invariants purely behavioural. Add a **separation guard** line. |
| **A2**  | **Pan‑Context template**   | One card cites several canons implicitly (“BPMN/PROV process”).           | Imports meaning across Contexts; hides losses.              | Keep **one SenseCell per card**. If Cross‑context relation is needed, defer to **F.9 Bridge**.                     |
| **A3**  | **Silent time flip**    | Card defined in a **design** Context asserts run‑time facts (or vice versa). | Violates F.1 time stance; produces category errors.      | Align **Time stance** to the Context; relocate run‑facts to status/evidence lines or to another Context.              |
| **A4**  | **Procedural template** | Long “steps” instead of minimal invariants.                               | Becomes a method recipe, not an assignable mask/badge.   | Replace sequences with **decisive invariants** (2–5 lines) that must hold regardless of procedure.              |
| **A5**  | **Permission leakage**  | A BPMN Role claims access rights “by wearing the mask”.                   | Conflates access with behaviour; weakens RBAC semantics. | State explicitly: **no permissions implied**. Bind access via a **Status** in the RBAC Context.                    |
| **A6**  | **Evidence bake‑in**    | Status card encodes metrics/formulas.                                     | Smuggles Part B maths; reduces portability.              | Keep only **evaluation invariants** in Context language; actual checks live in Part B/C via SenseCells.            |
| **A7**  | **Global label**        | Tech label chosen for cross‑discipline appeal (“Actor”) not Context idiom.   | Loses local meaning; harms F.3 clustering.               | Use **Context‑idiomatic Tech label**; provide a Plain label for teaching (F.5 governs labels).                     |
| **A8**  | **Concept inflation**   | Multiple near‑duplicate cards for the same SenseCell.                     | Noise; brittle naming.                                   | Prefer **refinement** (see §11) or a single card with tighter invariants; avoid duplicates.                     |
| **A9**  | **Holder sprawl**       | Holder scope lists unrelated kinds (“U.System or U.Work or U.Episteme”).  | Ambiguity at binding time.                               | Shrink **Holder scope** to the real carriers; if truly different, split cards.                                  |
| **A10** | **Anchor relapse**      | Card talks about “anchors” or “global context.”                           | Re‑introduces banned jargon; confuses D.CTX.             | Replace with **Context** / **SenseCell**; never use “anchor”.                                                      |
| **A11** | **Tooling creep**       | Mentions manifests, pipelines, editors.                                   | Violates E.5 guard‑rails; notational dependency.         | Remove all process/tool talk; keep card **concept‑only**.                                                       |
| **A12** | **Bridge‑by‑label**     | Using identical labels to imply Cross‑context sameness.                      | Stealth equivalence; no loss policy.                     | Labels do not bridge. Any Cross‑context claim goes to **F.9** with a declared CL policy.                           |

### 11 · Concept‑level operators (refinement & compatibility)

> **Judgement schemas** — pure reasoning moves over cards. No APIs, no storage, no workflow.

Let **`sense(T)`** denote the **SenseCell** cited by template **T**.
Let **`inv(T)`** denote the set of **invariants** on T.
Let **`senseFamily(T)`** ∈ {**Role**, **Status**}.
Let **`stance(T)`** ∈ {**design**, **run**} (from the Context).

#### 11.1 Same‑Context equivalence

**Form.**
`sense(T₁) = sense(T₂) ∧ inv(T₁) ⇔ inv(T₂) ⊢ T₁ ≡ T₂`

**Reading.** Two cards in the **same Context** with logically equivalent invariants **co‑designate** the same assignable.

*Tech cue.* Use this to **merge duplicates** conceptually without changing labels.

#### 11.2 Refinement (strictness order)

**Form.**
`sense(T₁) = sense(T₂) ∧ inv(T₁) ⇒ inv(T₂) ⊢ T₁ ⪯ T₂`

**Reading.** **T₁** is a **refinement** of **T₂** if its invariants **imply** those of **T₂** (same Context).

*Effects.* Assigning **T₁** automatically satisfies **T₂**; the converse need not hold.

#### 11.3 Incompatibility (mutual exclusion)

**Form.**
`sense(T₁) = sense(T₂) ∧ (inv(T₁) ∧ inv(T₂) ⇒ ⊥) ⊢ incompatible(T₁,T₂)`

**Reading.** Two cards in the same Context are **mutually exclusive** if their invariants cannot co‑hold.

*Use.* A conceptual **Separation‑of‑Duty** signal without governance.

#### 11.4 Co‑wearability / co‑bearability

**Form.**
+`senseFamily(T₁)=senseFamily(T₂)=Role ∧ stance(T₁)=stance(T₂) ∧ ¬incompatible(T₁,T₂) ⊢ coWearable(T₁,T₂)`
+`senseFamily(T₁)=senseFamily(T₂)=Status ∧ ¬incompatible(T₁,T₂) ⊢ stackable(T₁,T₂)`

**Reading.** Within a Context, two Roles can be worn together (or two Statuses carried) when they **do not** conflict.

#### 11.5 Time‑stance alignment

**Form.**
`stance(T)=design ⊢ inv(T) may not assert run‑facts`
`stance(T)=run ⊢ inv(T) may not assert design‑commitments`

**Reading.** Invariants must **respect** the Context’s DesignRunTag (F.1).

#### 11.6 Binding/Assertion admissibility

**Form. (Roles)**
`holder h ∧ preconds_T(h) ⊢ assignable(h,T)`
`assignable(h,T) ∧ bind(h,T) ⊢ inv(T)(h)`

**Form. (Statuses)**
`evidence_in_Context(C) supports S for x ∧ sense(S)=⟨C,σ⟩ ⊢ assertable(x,S)`
`assertable(x,S) ∧ assert(x,S) ⊢ inv(S)(x)`

**Reading.** Preconditions and evidence **gate** the act of wearing a mask or bearing a badge; once done, **invariants apply**.

### 11.7 Cross‑context embargo (inside F.4)

**Form.**
`sense(T₁)=⟨C,−⟩, sense(T₂)=⟨C′,−⟩, C≠C′ ⊢ no‑relation(T₁,T₂) here`

**Reading.** **F.4** never asserts Cross‑context relations. If a relation is desired, it becomes a **Bridge** in **F.9**.

### 12 · Relations (where this card sits)

**Builds on:**
E.10.D1 **D.CTX** (Context ≡ U.BoundedContext); F.1 (Contexts cut); F.2 (harvested terms); F.3 (Local‑Sense → **SenseCell**); A.2.1 **`U.RoleAssignment`**; A.7 **Strict Distinction**.

**Constrains:**
**F.5** (Naming): pairs **Tech/Plain** must reflect the **Context idiom** and avoid Cross‑context overreach.
**F.7** (Concept-Set Table): rows reference **SenseCells**; Role Description cards **point to** those rows but never **create** cross-context identity.
**F.8** (Mint or Reuse?): prefer **refinement (⪯)** over new cards; split cards rather than mixing senseFamilies.
**F.9** (Alignment & Bridge): any relation across Contexts is **declared there**; Role Description cards remain context-local.

**Is used by.**
A.15 family (Role–Method–Work alignment) to interpret **System‑in‑Role** and **Work**; Part B evidence/status checks to interpret **evaluation invariants**.

### 13 · Migration notes (conceptual playbook)

1. **Context update (edition split).** If the Context’s Local‑Sense changes, **fork** the card per new SenseCell; keep the old card as historically valid.
2. **Family correction (Role/Status).** If a card mixes behaviour and deontics, **split** into one Role and one Status; move permission language to the Status.
3. **Tighten by refinement.** When practice reveals a stricter understanding, prefer **T′ ⪯ T** over replacing **T**; this preserves existing assignments conceptually.
4. **Rename safely (labels only).** If F.5 revises labels, change **Tech/Plain** wording; **SenseCell** and **invariants** remain untouched.
5. **Scope correction.** If Holder scope was too wide, split into **parallel cards** with disjoint Holder scopes; avoid complex conditional invariants.
6. **Bridge discovery.** Do **not** inject Cross‑context text into cards; record the relation as an **F.9 Bridge** (with CL policy), leaving the cards as they are.

### 14 · Acceptance tests (SCR/RSCR — concept‑level)

#### 14.1 Static conformance (SCR)

* **SCR‑F4‑S01 (Uni‑Context grounding).** Each card cites **exactly one SenseCell**.
* **SCR‑F4‑S02 (Family honesty).** `senseFamily(T)` is **either** Role **or** Status; invariants match the family; a **separation guard** line is present.
* **SCR‑F4‑S03 (Time honesty).** `stance(T)` matches the Context’s stance; no opposing‑stance claims appear.
* **SCR‑F4‑S04 (Minimality).** Card lists **2–5** invariants; none are procedural step lists.
* **SCR‑F4‑S05 (Label fidelity).** Tech label is **idiomatic to the Context**; Plain label does not widen meaning.
* **SCR‑F4‑S06 (No Cross‑context import).** Invariants reference only the Context’s idiom or other **SenseCells** by **name** (no identity claims).
* **SCR‑F4‑S07 (Holder clarity).** Holder scope is a **single coherent kind** (e.g., `U.System` or `U.Work`), not a grab‑bag.
* **SCR‑F4‑S08 (No tooling/governance).** Card contains **no** mentions of manifests, pipelines, editors, or workflows.

#### 14.2 Regression (RSCR)

* **RSCR‑F4‑E01 (Edition churn).** When a Context edition changes, existing cards are **not overwritten**; new cards are added per SenseCell.
* **RSCR‑F4‑E02 (Refinement safety).** If **T′ ⪯ T** is introduced, prior usages of **T** remain conceptually valid; no backward contradictions arise.
* **RSCR‑F4‑E03 (senseFamily integrity).** No card changes senseFamily across revisions (Role↔Status) without an explicit **split** noted.
* **RSCR-F4-E04 (Bridge discipline).** After adding an **F.9 Bridge**, Role Description cards remain **unchanged**; cross-context meanings do not seep back into cards.
* **RSCR‑F4‑E05 (Label updates).** Label changes per **F.5** preserve SenseCell and invariants; tests treat them as **renames**, not semantic edits.

### 15 · Didactic distillation (60‑second close)

> A Role Description card is a **Context-true** way to speak about an assignable: a **Role** (behavioural mask) or a **Status** (epistemic/deontic badge).
> Each card names **one SenseCell**, gives a **Tech/Plain** label, states **minimal invariants**, and declares what it **does not** imply.
> Cards never mix **Role/Status senseFamilies** and never cross **I/D/S layers**, never flip time stance, and never import other Contexts.
> Inside one context, you can compare cards by **equivalence** (≡), **refinement** (⪯), **incompatibility**, and **co‑wearability**.
> across Contexts, say nothing in the card; use a **Bridge** later.
> Keep cards **one‑screen simple**: enough to decide assignments; nothing procedural; no tools; just clear thought.


# F.5 — Naming Discipline for U.Types & Roles \[D] 

**Status.** Definitional pattern \[D], architheory‑agnostic.
**Depends on.** E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; **E.10.D2 Intension–Description–Specification (I/D/S)**; F.1 **Domain‑Family Landscape Survey**; F.2 **Term Harvesting & Normalisation**; F.3 **Intra‑Context Sense Clustering**; F.4 **Role Description Definition**; A.7 **Strict Distinction**; A.11 **Ontological Parsimony**; F.0.1 **context‑local Lexicon Principle (RLP)**.
**Coordinates with.** F.7 **Concept‑Set Table**; F.8 **Mint or Reuse?**; F.9 **Alignment & Bridge**; F.13 **Term Registry & Deprecation**.
**Aliases (informative).** *Context‑true naming*; *Two‑register labels*.

---

## 1 · Intent & applicability

**Intent.** Provide a **small, normative code of naming** so that **U.Types** (Cross‑context categories) and **Role Descriptions** (context‑local Roles/Statuses) are labelled **clearly, locally faithful, and globally stable**, without importing tooling, workflows, or editorial process. Names are **consequences of meaning** fixed earlier (F.1–F.4), not badges invented to “stabilise” drifting words.

**Applicability.** Use **whenever** you (a) mint or revise a **U.Type** name from a **Concept‑Set row** (F.7), or (b) assign labels to a **Role Description** (F.4). This pattern governs **what a good name must be**, not *how a team produces it*.

**Non‑goals.** No registries, reviews, or hand‑offs. No style‑police for punctuation beyond conceptual clarity. No bridging or synonym decisions across Contexts (F.9 does that).

---

## 2 · Problem frame

Naming errors cause structural errors:

1. **Context denial.** A label hides its Context, inviting Cross‑context misuse (*“process”* used for both BPMN and PROV senses).
2. **senseFamily blur.** Names conflate **Role** (behavioural mask) with **Status** (epistemic/deontic badge).
3. **Over‑reach.** U.Types inherit jargon from one canon and sound global while being parochial.
4. **Under-reach.** Role Description labels sound so generic that they pretend to be U.Types.
5. **Unstable synonyms.** Labels drift to placate readers rather than reflect meaning fixed in SenseCells.

This code resolves these by **Context fidelity**, **senseFamily‑aware morphology**, and **two‑register pedagogy**.

---

## 3 · Minimal vocabulary (this pattern only)

* **Tech label** — the **Context‑idiomatic** name engineers expect *inside that Context*.
* **Plain label** — a **teaching gloss** in simple English that does **not broaden** the sense.
* **Symbolic alias** *(optional)* — conventional symbol if the canon uses one (e.g., “≤”).
* **SenseCell** — the **(Context × Local-Sense)** address cited by a Role Description card (F.3–F.4).
* **Concept‑Set row** — the Cross‑context table row that supports minting a **U.Type** name (F.7).

---

## 4 · Core idea (didactic)

> **Name what the invariants already make true.**
>
> For Role Descriptions, **speak like the Context** (Tech), then **teach it** (Plain).
> For U.Types, **speak like nobody’s Context**: pick the **neutral, minimal‑generality** label that best fits the **intersection** shown by your Concept‑Set row.

---

## 5 · Normative rules — Role Descriptions (context‑local labels)

Let **T** be a Role Description in Context **C** with SenseCell `sense(T)=⟨C,σ⟩`.

**R‑RD‑1 (Two registers).** Provide **both**:
`Tech(T)` = the **Context‑idiomatic** phrase (exact canon wording if possible).
`Plain(T)` = a brief, neutral explanation *that does not broaden meaning*.
*Symbolic alias* is optional and purely informative.

**R‑RD‑2 (No Context tags in labels).** Do **not** embed the Context name in the label (avoid “(BPMN)” in the label itself). Context is already carried by the **SenseCell**; keep labels clean.

**R‑RD‑3 (senseFamily‑aware morphology).**
— **Role** names are **countable nouns** for masks (e.g., *Participant*, *Operator*, *Reviewer*). Avoid verbs and gerunds. Add the suffix **“Role”** **only** if the Context idiom risks confusion with a substance or a status (e.g., *“Reviewer Role”* in a Context that also has a *“Reviewer Status”*).
— **Status** names are **state nouns** or **adjectival‑noun collocations** (e.g., *Approved*, *Compliant*, *In‑Service*, *Access Role* (RBAC)). If a family of levels exists, encode the **level** (`Assurance L1`, `Readiness L2`) rather than inventing decorative adjectives.

**R‑RD‑4 (Local idiom first).** Prefer the **canon’s term of art** even if it sounds narrower than a cross‑discipline cliché. The Plain label handles pedagogy; the Tech label honours the Context.

**R‑RD‑5 (Minimal generality).** Choose the **narrowest label** whose invariants you actually assert. Do **not** “upgrade” *Task* to *Activity* or *Process* just to sound universal.

**R‑RD‑6 (No permissions by stealth).** Role labels **must not** imply entitlement (*“Privileged Operator”* is a Status+Role mashup). Keep deontics in **Status** names in the **deontics Context**.

**R‑RD‑7 (Edition‑neutral labels).** Do **not** bake edition/profile into labels. Edition lives in the **Context**; the card binds to a SenseCell that already encodes edition where needed.

**R‑RD‑8 (Short and stable).** Favour **1–3 words**. Avoid rhetorical adjectives (*“robust, optimal, best‑practice”*).

---

## 6 · Normative rules — U.Types (Cross‑context labels)

Let **U** be a U.Type minted from a **Concept‑Set row** (F.7) satisfying A.8 (≥3 domain families) AND MinInterFamilyDistance ≥ δ_family (from F1‑Card).

+**R‑UT‑1 (Witnessed neutrality).** The Tech label **must not** be a term owned by one context when alternatives exist. Prefer **discipline‑neutral head nouns** (*Result, Reading, Execution, Evidence, Requirement, State, Type Node*). **Use** *Characteristic/Scale/Value/Level/Coordinate/Score/Gauge* **only** when the U.Type denotes a **measurement‑sense** kind anchored in a declared **CharacteristicSpace**; otherwise avoid these measurement‑canon terms to prevent semantics bleed.

**R‑UT‑2 (Minimal generality).** Name the **least upper sense** that all row witnesses share. If *Observation* and *Measurement* disagree, perhaps the U.Type is **Result** or **Reading**, not **Observation**.

**R‑UT‑3 (No senseFamily mixing in names).** Do **not** name a U.Type with deontic or behavioural language (*“PermittedService”*, *“ResponsibleAgent”*). **Role/Status/Method/Execution** belong to **Role Descriptions (F.4)** or local senses; U.Types are *what‑it‑is* kinds, not *what‑it‑does* or *what‑is‑allowed*.

**R‑UT‑4 (Head–modifier discipline).** Prefer **head nouns** with **light modifiers** over stacked compounds.
Good: *Evidence Status*, *Requirement Status*, *Type Node*.
Risky: *Multi‑stage‑workflow‑execution‑record* (compresses a scenario into a name).

**R‑UT‑5 (No Context tags in names).** U.Types are **Context‑agnostic**; never append “(BPMN)”/“(PROV)”. Provenance for the row lives in F.7, not in the name.

**R‑UT‑6 (Alias only for pedagogy).** Allow **Plain aliases** for teaching; **Tech label** is unique and stable. Synonym management belongs to **F.13**; do not invent alternates ad hoc.

**R‑UT‑7 (Family coherence).** When minting a **family**, use **parallel shapes** (*… Status*, *… Level*, *… Characteristic* **only for measurement families with a declared CharacteristicSpace**) so related U.Types signal relation by form.

**R‑UT‑8 (Symbolic names sparingly).** Symbols may be listed as *aliases* for readers of formal sections; they are **never** the U.Type’s Tech label.

**R‑UT‑9 (No edition/version in name).** Versions live in the Concept‑Set evidence; the name denotes a **time‑robust kind**.


## 7 Twin rules

**Mandatory Tech name.** Every `U.Type`/Role **MUST** declare a Tech name; plain twin is optional.
**Role suffix invariant.** Role Tech names **MUST** end with `Role`; plain twin **MUST** keep “(role)” on first use.
**No head elision.** Head terms **MUST NOT** be dropped in a way that changes expected Kind (e.g., _“Approval”_ ≠ _“Approver (role)”_).
**One twin, one context.** At most one plain twin per Context; register in **E.10.P**.


## 8 · Invariants (normative, lightweight)

**INV-F5-1 (Pair).** Every Role Description card and every U.Type **MUST** carry **Tech** and **Plain** labels; symbol is optional and informative.

**INV-F5-2 (Context fidelity for Role Descriptions).** `Tech(T)` **MUST** be idiomatic for its Context; `Plain(T)` **MUST NOT** broaden `sense(T)`.

**INV‑F5‑3 (Neutrality for U.Types).** `Tech(U)` **MUST** be discipline‑neutral with respect to the witness Contexts in its Concept‑Set row.

**INV‑F5‑4 (senseFamily honesty).** Role Description **Role** labels are **behavioural masks**; Role Description **Status** labels are **states/badges**; neither sneaks in the other senseFamily.

**INV‑F5‑5 (Minimality).** Labels **MUST** reflect the **minimal generality** supported by invariants (F.4 for Role Description, F.7 for U.Types).

**INV-F5-6 (No Context tags).** Names **MUST NOT** embed Context/edition tags; that information resides in SenseCells (Role Description) and Concept-Set rows (U.Types).

---

## 9 · Reasoning primitives (judgement schemas, notation‑free)

> Pure mental checks; no tools implied.

1. **Context-idiom check (Role Description).**
   `T in Context C ⊢ idiomatic(Tech(T), C)`
   *Reading:* The Tech label reads like the Context’s own term of art.

2. **Plain‑safety check.**
   `sense(T)=⟨C,σ⟩ ⊢ ¬broadens(Plain(T), σ)`
   *Reading:* The Plain label explains without enlarging the sense.

3. **Neutral‑witness check (U.Type).**
   `witnessContexts(U)=R ⊢ neutral(Tech(U), R)`
   *Reading:* The Tech label doesn’t privilege one witness Context’s jargon.

4. **senseFamily form check (Role Description).**
  `senseFamily(T)=Role ⊢ nounMask(Tech(T))`
  `senseFamily(T)=Status ⊢ stateForm(Tech(T))`
   *Reading:* The morphology matches the senseFamily.

5. **Minimality proof.**
  `inv(T) ⇒ nameScope(Tech(T)) ⊆ senseScope(sense(T))` (Role Description)
   `rowWitnesses(U) ⇒ nameScope(Tech(U)) ⊆ intersectionScope(row)` (U.Type)
   *Reading:* The name’s scope is **no wider** than what the invariants/witnesses support.

6. **Collision ping.**
  `similar(Tech(X), Tech(Y)) ∧ senseFamily(X)≠senseFamily(Y) ⊢ requireDisambiguatorOrSplit`
  *Reading:* If two labels nearly coincide across senseFamilies, either add a **minimal** disambiguator (Role Description only, within Context idiom) or split concepts.

---

## 10 · Micro‑examples (illustrative)

**Role Description (BPMN Context).**
Tech: **Participant** · Plain: *actor in a workflow* · senseFamily: **Role**
(*No “BPMN” in label; behaviour mask, not entitlement.*)

**Role Description (RBAC Context).**
Tech: **Access Role** · Plain: *named permission set* · senseFamily: **Status**
(*Deontic badge; not a behavioural mask.*)

**Role Description (ITIL Context).**
Tech: **Service‑Level Objective** · Plain: *service target value* · senseFamily: **Status**
(*Levelable family: SLO \[target], SLI \[indicator] handled in F.10/F.12 semantics, not in the label.*)

**U.Type (from Concept‑Set row: SOSA Observation, PROV Activity (result‑bearing), ML Metric Reading).**
Tech: **Result** · Plain: *the produced value or record of a measurement/assessment*
(*Neutral head noun when “Observation” is too Context‑coloured.*)

**U.Type (from OWL class, FCA concept, taxonomy nodes).**
Tech: **Type Node** · Plain: *a node in a type hierarchy or lattice*
(*Neutral across DL and FCA.)*

## 11 · Anti‑patterns & remedies

| #       | Anti‑pattern                | Symptom in labels                                                  | Why it harms thinking                                              | Remedy (rule‑backref)                                                                                               |
| ------- | --------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| **A1**  | **Context tag leakage**        | `Participant (BPMN)`, `Activity (PROV)` baked into the label       | Labels pretend to carry provenance; duplicates appear across Contexts | **No Context tags in names.** Context is in the SenseCell / Concept‑Set, not the label. (R‑RD‑2, R‑UT‑5)                 |
| **A2**  | **Globalised jargon**       | U.Type named `Observation` because SOSA uses it                    | Privileges one context; misleads DL/FCA readers                       | Pick neutral **head noun** (e.g., `Result`, `Reading`) when witnesses diverge. (R‑UT‑1, R‑UT‑2)                     |
| **A3**  | **senseFamily mixing**      | `Privileged Operator`, `Compliant Reviewer Role`                   | Role + deontic Status fused; category error                        | Keep **Role** nouns for masks; put deontics in **Status** names, often in a deontics Context. (R‑RD‑3, R‑RD‑6)       |
| **A4**  | **Verbified roles**         | `Observing`, `Controlling`, `Approving` as Role names              | Action words hide mask semantics; temporal confusion               | Use **countable nouns** for Roles: `Observer`, `Controller`, `Approver`. (R‑RD‑3)                                  |
| **A5**  | **Edition coding**          | `SLO‑v4`, `Task‑IEC61131`                                          | Names fossilise an edition; brittle across time                    | Edition belongs to the **Context**; keep labels edition‑neutral. (R‑RD‑7, R‑UT‑9)                                     |
| **A6**  | **Over-reach**              | Role Description `Activity` for a BPMN task, U.Type `Process` for run-time acts | Label outruns invariants; invites cross-context misuse                | Choose **minimal generality** that the invariants actually support. (R-RD-5, R-UT-2, INV-F5-5)
| **A7**  | **Under‑reach / vagueness** | `Item`, `Thing`, `Record` for specific kins                        | No discriminative power; weak teaching                             | Prefer **discipline‑neutral yet informative** heads (`Type Node`, `Result`, `Requirement Status`). (R‑UT‑1, R‑UT‑4) |
| **A8**  | **Symbol as name**          | U.Type named `λ` or `≤`                                            | Unsearchable; Context‑coloured conventions                            | Keep symbols **only as aliases**; Tech label is words. (R‑UT‑8)                                                     |
| **A9**  | **Synonym spray**           | Multiple Tech labels for one U.Type                                | Fragmentation; alias drift                                         | One **Tech** label; further surface forms live in the **registry** (F.13). (R‑UT‑6, INV‑F5‑1)                       |
| **A10** | **Compound overgrowth**     | `multi‑stage‑workflow‑execution‑record`                            | Encodes scenario in a name; unreadable                             | Use **head + light modifier**: `Execution Record` (if that is the U.Type at all). (R‑UT‑4)                          |
| **A11** | **Context-idiom denial**       | Role Description in BPMN named `Actor` (imported from other Contexts) | Readers misapply foreign semantics                                 | Use the **Context’s term of art** in the Tech label; teach via Plain label. (R-RD-4)
| **A12** | **Status as event**         | `Approval` status labelled `Approve`                               | Morphology hides state vs act                                      | Status labels are **state nouns** / **adjectival‑noun collocations**: `Approved`, `In Service`. (R‑RD‑3)           |
| **A13** | **Bracketed twins**         | `Participant/Agent`, `Service/SLO` as single label                 | Two senses slipped into one card                                   | Pick **one** label per concept; the other lives as alias (F.13) or as a different card. (INV‑F5‑1, R‑UT‑6)          |
| **A14** | **Family drift**            | `Assurance Rank`, `Assurance Tier`, `Readiness Level` mixed        | Readers fail to see relatedness                                    | Keep **family shape** parallel: `… Level`, `… Status`. (R‑UT‑7)                                                     |
| **A15** | **Decorative adjectives**   | `Robust Process`, `Best‑practice Method`                           | Marketing words displace semantics                                 | Drop rhetoric; name the **kind**, not its quality. (R‑RD‑8)                                                        |

---

## 12 · Worked examples (multi‑architheory)

> Each example shows the **reasoning move** that leads to the label; no procedures, no tooling.

### 12.1 Role Description labels (context-local)

**(a) BPMN Context — behavioural mask vs node word**

* **SenseCell.** ⟨*BPMN 2.0*, local‑sense: lane/pool actor that enacts tasks⟩
* **Decision.** Tech = **Participant** (Context idiom); Plain = *actor in a workflow*
* **Why.** `Participant` is the mask; it is **not** the node (*Task*, *Event*). (R-RD-3, R-RD-4)

**(b) RBAC Context — deontic badge**

* **SenseCell.** ⟨*NIST RBAC*, local‑sense: named permission set assigned to sessions⟩
* **Decision.** Tech = **Access Role**; Plain = *named permission set*
* **Why.** It’s a **Status**, not a behavioural mask; deontic plane kept explicit. (R-RD-3, R-RD-6)

**(c) ITIL Context — service target**

* **SenseCell.** ⟨*ITIL 4*, local‑sense: target value for a service characteristic⟩
* **Decision.** Tech = **Service‑Level Objective**; Plain = *service target value*
* **Why.** Family will carry `… Level`, `… Indicator` in adjacent cards; avoids jargon drift. (R-RD-3, R-UT-7)

**(d) IEC 61131-3 Context — run-time execution notion as Role Description?**

* **SenseCell.** ⟨*IEC 61131‑3*, local‑sense: cyclic/event‑driven task unit⟩
* **Decision.** For a Role Description **Status** of a run, label **Completed**, **Failed**, **Skipped** (Context idiom); avoid naming the **Work** itself here.
* **Why.** The *record of work* is a **U.Type** elsewhere (A.15.1); Role Description in this Context carries **badges** of runs. (A.7 stance split; R-RD-3)

### 12.2 U.Type labels (from Concept‑Set rows)

**Row R₁ (measurement‑sense):**
SOSA: *Observation* • ML practice: *metric reading* • Metrology: *measurement result*

* **Witness Contexts.** sensing; ML metrics; metrology
* **Decision.** U.Type Tech = **Result**; Plain = *the produced value or record of a measurement/assessment*
* **Why.** Neutral head noun covering all witnesses; avoids privileging SOSA’s *Observation*. (R‑UT‑1, R‑UT‑2)

**Row R₂ (type‑structure):**
OWL: *class* / *subclass* • FCA: *formal concept* (node in concept lattice)

* **Witness Contexts.** DL; FCA
* **Decision.** U.Type Tech = **Type Node**; Plain = *a node in a type hierarchy or lattice*
* **Why.** Neutral over DL vs FCA; head‑modifier shape is stable. (R‑UT‑1, R‑UT‑4, R‑UT‑7)

**Row R₃ (status family):**
ITIL: *incident status* • Safety cert.: *assurance level* • QA: *readiness level*

* **Witness Contexts.** services; assurance; QA
* **Decision.** Two U.Types: **Assurance Level**, **Readiness Level** (family‑coherent), plus **Requirement Status** (for normative clauses)
* **Why.** Separates families; preserves level vs status distinction. (R‑UT‑7, R‑UT‑3)

---

### 12.3 Mixed scenario (service acceptance over execution traces)

**Contexts in play.** IEC 61131‑3 (run), SOSA/SSN (sensing), ITIL 4 (services).

1. **Role Description (ITIL)** — Tech: **Service-Level Objective**; Plain: *service target value*.
2. **U.Type (from R₁)** — Tech: **Result** (to host measured values).
3. **Role Description (IEC)** — Tech: **Completed** / **Failed** (Status on a run).
4. **Name discipline payoff.** The sentence “*Compare IEC run **Results** against the ITIL **Service‑Level Objective***” is Context‑true without tags, because each label encodes its **senseFamily** and neutrality.

---

## 13 · Migration notes (conceptual)

1. **When a Context changes edition.** Names stay; the **SenseCell** shifts to the new edition. Only change a label if the **sense** has changed; then **split** the card rather than mutate the name. (INV‑F5‑2, R‑RD‑7)

2. **When a Concept‑Set row gains a new witness Context.** Re‑ask neutrality: if the Tech label now privileges a Context, **refactor to a more neutral head** (e.g., `Observation` → `Result`). (R‑UT‑1, R‑UT‑2)

3. **Collision emergence.** If a **Role card** and a **Status card** converge phonetically (`Approver` vs `Approved`), keep both but add the **minimal morphological disambiguator** only where the Context idiom demands it (`Reviewer Role`). (R-RD-3)

4. **Family hygiene.** As families grow, keep **parallel shapes** (`… Level`, `… Status`). If a legacy label breaks shape, add a **Plain alias** for teaching; don’t rename the Tech label without Concept‑Set pressure. (R‑UT‑7, R‑UT‑6)

5. **Language variants.** Non-English canons keep **their own Tech labels** (idiomatic in that Context); the **Plain** label remains English in FPF unless the Part mandates localisation. (R-RD-4, INV-F5-1)

6. **Symbol addition.** You may add a **symbolic alias** later for readers of formal sections; never promote a symbol to the Tech label. (R‑UT‑8)

7. **De‑jargonising the Plain label.** If readers stumble, adjust **Plain** wording only; do **not** widen the sense. (Plain‑safety check)

8. **Deprecation path.** If a label must change, publish the **new Tech + Plain**, keep the old as an **alias** in the registry (F.13), and leave the reasoning trail in the Concept‑Set row that forced the rename. (R‑UT‑6, F.13 linkage)

## 14 · Acceptance tests (SCR/RSCR — concept‑level)

### 14.1 Static conformance (SCR)

* **SCR-F5-S01 (Two registers).** Every Role Description card and U.Type **has both** Tech and Plain labels; any symbol is marked **alias**.
* **SCR-F5-S02 (Context fidelity for Role Descriptions).** For any Role Description `T` in Context `C`, `Tech(T)` appears idiomatic **in C**; `Plain(T)` does **not** broaden `sense(T)`.
* **SCR‑F5‑S03 (Neutrality for U.Types).** For any U.Type `U`, its Tech label does **not** coincide with a witness Context’s proprietary term when alternatives exist.
* **SCR‑F5‑S04 (senseFamily morphology).** Role labels are **countable nouns**; Status labels are **state nouns** / adjectival‑noun forms.
* **SCR-F5-S05 (Minimal generality).** For each label, there exists a reading where the **name’s scope ⊆ invariant scope** (Role Description) or **⊆ row intersection** (U.Type).
* **SCR‑F5‑S06 (No Context tags).** No label embeds Context or edition strings.
* **SCR‑F5‑S07 (Family coherence).** Families that claim parity (e.g., Levels) show **parallel shapes** across members.

### 14.2 Regression checks (RSCR)

* **RSCR‑F5‑E01 (Witness drift).** When a Concept‑Set row gains/removes a witness Context, re‑evaluate **neutrality**; if violated, refactor the Tech label to a more neutral head.
* **RSCR-F5-E02 (Edition churn).** When a Context updates, Role Description labels remain stable unless the **sense** changed; if sense changed, **split** the card and keep aliases in F.13.
* **RSCR‑F5‑E03 (Collision guard).** If two labels become confusable across **senseFamilies**, either add the **minimal** disambiguator (Role Description only, Context‑idiom) or separate the concepts.
* **RSCR‑F5‑E04 (Rhetoric creep).** Periodic skim for decorative adjectives; remove them unless they encode formal levels or families.

## 15 · Didactic distillation (60‑second recap)

> **Name what is already true.**
> Role Description labels **speak like the Context** (Tech) and **teach without widening** (Plain).
> U.Type labels **speak like nobody’s Context**: neutral head nouns at **minimal generality**, shaped in **parallel families**.
> **Never** glue Context tags or editions into names. **Never** mix senseFamilies in morphology.
> If witnesses change, reconsider neutrality; if senses split, **split names**, don’t stretch them.
> The label is the **last step of understanding**, not the first.


## F.6 — Role Assignment & Enactment Cycle (Six-Step) \[A] 

**“Assign only what you can later justify by local meaning and observable facts.”**
**Status.** Architectural pattern \[A], architheory‑agnostic.
**Depends on.** E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; F.1 **Domain‑Family Landscape Survey**; F.2 **Term Harvesting & Normalisation**; F.3 **Intra‑Context Sense Clustering**; F.4 **Role Description**; F.5 **Naming Discipline**.
**Coordinates with.** F.7 **Concept‑Set Table**; F.8 **Mint or Reuse?**; F.9 **Alignment & Bridge**; F.10 **Epistemic Status Mapping**; A.2.1 **U.RoleAssignment**; A.15.\* **Role–Method–Work alignment**; KD‑CAL (observations, results).
**Aliases (informative).** *Assign-and-verify mental loop*; *six-step role cycle*.

### 1 · Intent & applicability

**Intent.** Provide a **minimal set of reasoning moves** that turn a **Role Description** (F.4), anchored in a **SenseCell**, into a **sound claim** about a concrete **holder**—either a **Role assignment** or a **Status assertion**—with **local meaning** (within one context) and a **clear path to evidence** (KD‑CAL). These are **mental moves**, not workflows or tools.

**Applicability.** Any time you (a) bind a system to a **Role** mask, or (b) assert a **Status** about a system/artefact, **inside one U.BoundedContext**. Use when drafting models, reconciling vocabularies, or reading external canons.

**Non‑goals.** No process charts, no registries, no governance roles. No Cross‑context equivalences (that is F.9). No operational runbooks—only conceptual judgements.

### 2 · Problem frame

Without disciplined Role Assignment & Enactment reasoning:

1. **Sense‑family slippage.** Behavioural **Roles** and deontic/epistemic **Statuses** get mixed (keep them on distinct **senseFamilies**, per F.0.1).
2. **Context drift.** A label is lifted from one canon and used as if universal.
3. **Evidence vacuum.** Assignments are asserted with no thought to what could **show** they hold.
4. **Time blur.** Design‑time masks are judged by run‑time traces (or vice versa).
5. **Name inflation.** New labels are minted to patch noisy assignments.

### 3 · Forces

| Force                       | Tension to resolve                                                                   |
| --------------------------- | ------------------------------------------------------------------------------------ |
| **Locality vs reuse**       | Keep meaning inside one context while still naming things once across examples.         |
| **Clarity vs completeness** | State enough to be checkable without burying the reader in conditions.               |
| **Design vs run**           | Keep **stance** coherent: design‑time bindings are judged by design artefacts; if you need run‑time verification, express it as a **run‑Status/Role** Template—without confusing **stances** (A.7). |
| **Fact vs promise**         | Evidence (KD‑CAL) vs deontic expectations (service, policy) must not collapse.       |

### 4 · Minimal vocabulary (this pattern only)

* **Context** — shorthand for **U.BoundedContext** (per E.10.D1).
* **SenseCell σ** — **address** **⟨Context C × Local‑Sense ℓ⟩** per F.3. (Informative: we write simply **σ**; it already contains **C**.)
* **Role Description** — a **Role** or **Status** card anchored in a SenseCell (F.4).
* **Holder** — the concrete system/artefact considered for a **Role** binding.
* **Subject** — the referent of a **Status** assertion; determined by the Template (may or may not be the Holder).
* **subject_of(τ, H)** — function yielding the **Subject** for Status assertions given Template **τ** (and, if needed, candidate **H**).
* **Eligibility** — conditions on the Holder that *must* hold to apply the Template (F.4 invariants).
* **Window** — the DesignRunTag or interval relevant to the claim (design/run; instant/period).
* **Evidence shape** — the **Observation/Result/Procedure/Feature** pattern (KD‑CAL) that could confirm/refute the claim in its Context.

### 5 · Pre‑conditions (lightweight)

1. The **Context** is in your F.1 cut; **Context ≡ U.BoundedContext**.
2. The **Template** references a **SenseCell** in that Context (F.4).
3. The **Holder** is identified (by type or instance) without relying on Cross‑context mappings.

### 6 · The six moves (judgement schemas, notation‑free)

Each move is a **thought you can justify**, expressed as `premises ⊢ conclusion`.
All moves are **context‑local** and **side‑effect free** (they assert knowledge; they do not modify artefacts).

#### M1 · Locate — *Fix the Context and the Template*

**Form.**
`Template τ anchored at SenseCell σ≡⟨C, ℓ⟩ ⊢ address(τ) = σ`

**Reading.** Name the Context and the exact SenseCell that gives **local meaning** to the Template.
**Note.** This forbids “floating” Roles/Statuses and prevents Context drift.

#### M2 · Stance — *Respect DesignRunTag*

**Form.**
`stance(C)=s ∧ stance(τ)∈{s, both} ⊢ compatible_stance(τ,C)`

**Reading.** The Template’s DesignRunTag is **compatible** with its Context’s stance (design vs run).
**Note.** Guards against judging a design‑mask by run‑traces or judging a run‑status by design artefacts.

#### M3 · Qualify — *Check Holder eligibility*

**Form.**
`Holder H ∧ eligibility(τ) holds in C ⊢ eligible(H, τ @ C)`

**Reading.** Given the Template’s eligibility predicates (F.4), the Holder qualifies to be bound/assessed **in this Context**.
**Note.** Typical predicates: **type membership**, **capability present**, **scope fit**; all context‑local.

#### M4 · Bind/Assert — *Make the Role Assignment / Status claim*

**Role assignment (behavioural mask).**
`eligible(H, τ @ C) ∧ window W ⊢ plays_role(H, τ : C) @ W`

**Status assertion (epistemic/deontic state).**
`eligible(H, τ @ C) ∧ window W ∧ S = subject_of(τ, H) ⊢ has_status(S, τ : C) @ W`

**Reading.** Assert either a **Role** binding or a **Status** about the appropriate subject (system, artefact, service), within a **Window**.
**Note.** The **subject** of a Status may differ from the Role holder (e.g., a *service* has SLO status; a *team* plays a Role).

#### M5 · Evidence — *Shape what would make it true/false*

**Form.**
`plays_role/has_status κ in C ⊢ evidence_shape(κ) = Σ(C)`

**Reading.** From the Context’s semantics, state the **Observation/Result** pattern (KD‑CAL) that would confirm or refute the claim (**what**, **where**, **when**).
**Note.** This is not an execution plan: it is a **conceptual test** tied to the Context’s vocabulary.

#### M6 · Conclude — *Issue a defensible verdict with confidence*

**Form.**
`evidence E fits Σ(C) ∧ invariants(τ) hold ⊢ holds(κ) with confidence γ ∈ [0,1]`

**Reading.** If observed facts match the expected evidence shape and Template invariants stand, the assignment/status claim **holds** with some confidence (cf. B.3).
**Note.** Confidence combines measurement adequacy (KD‑CAL) with any Context‑specific uncertainty; no Cross‑context boost is implied.

#### Autonomy admission (Green‑Gate) and ledger
* **Before enactment:** If the Method step lists `requiresAutonomyBudget`, the enacting `U.RoleAssignment` **MUST** pass the **Autonomy Green‑Gate**: (i) active/enactable RSG state, (ii) budget tokens/envelope remain in the declared **Γ_time** window, (iii) all guards `pass`.
* **On enactment:** Write an **AutonomyLedgerEntry** attached to the `U.Work`, with deltas and guard verdicts.
* **On depletion:** Block further autonomy‑gated steps; emit a **DepletionNotice** (SpeechAct) and follow the `OverrideProtocolRef`.
* **SoD:** Enforce `⊥` between autonomy consumer Role and override caller Role.

### 7 · Core invariants (normative)

1. **Locality.** Every judgement is **about one context**. No Cross‑context equivalence is presumed or implied (that is F.9’s remit).
2. **Strict splits.** (**a**) **senseFamily split:** **Role** ≠ **Status** (per F.0.1); (**b**) **stance split:** **design** ≠ **run** (A.7). Each judgement names its **senseFamily** and **stance**.
3. **Eligibility before claim.** No binding or status without **eligible(H, τ @ C)**.
4. **Window honesty.** Every claim states or inherits a **Window** consistent with `stance(τ)` and `stance(C)`.
5. **Evidence‑ability.** Every claim must admit at least one **evidence shape** Σ in its Context (KD‑CAL compatible).
6. **Name discipline.** Labels used in judgements follow F.5 (Tech/Plain registers; no Context tags inside names).

### 8 · Reasoning aides (didactic)

* **Context‑prefix speech.** Think and speak with the **Context prefix** when ambiguity lurks: *participant (BPMN)*, *role (RBAC)*, *activity (PROV)*.
* **Window templates.** Prefer short phrases: *“during release‑R3 cutover”*, *“for the Q3 service period”*, *“at 2025‑08‑12T14:30Z”*.
* **Evidence as shape words.** *Result of Observation of ⟨Characteristic⟩ on ⟨Feature⟩ by ⟨Procedure⟩ within W*—not a measurement script.  

**“Assign only what you can later justify by local meaning and observable facts.”**

### 9 · Anti‑patterns & remedies

| #         | Anti‑pattern                   | Symptom                                                                                     | Why it harms reasoning                                                     | Remedy (conceptual move)                                                                                                     |
| --------- | ------------------------------ | ------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **AP-1**  | **cross-context Binding**         | ... | ... | Re-formulate strictly in one context. If cross-context support is essential, defer to **F.9 Bridge** and keep the assignment/status claim local. |
| **AP‑2**  | **Role/Status Conflation**     | “Operator” modeled as a deontic grant; “SLO met” modeled as a Role.                         | Collapses **behavioural mask** and **epistemic/deontic state** (A.7).      | Re‑type the Template: **Role** for “can/does”, **Status** for “is/has (as a claim)”. Use **M4** accordingly.                 |
| **AP‑3**  | **Window‑less Claims**         | Binding/assertion with no time stance or interval.                                          | Uncheckable; invites retrospective reinterpretation.                       | Make **Window** explicit (§6 M4). Inherit stance from the Context/Template if fixed; otherwise state it.                        |
| **AP‑4**  | **Eligibility‑after‑the‑fact** | Declaring the claim, then back‑fitting eligibility to observed traces.                      | Confuses **necessary conditions** with **diagnostics**; risks circularity. | Perform **M3 Qualify** *before* **M4 Bind/Assert**; treat evidence only in **M5**/**M6**.                                    |
| **AP‑5**  | **Global Label Illusion**      | Using bare labels (“process”, “agent”, “role”) as if universal.                             | Hides the Context; fuels homonym errors.                                      | Always recover **M1 Locate**: `address(τ)=⟨Context, SenseCell⟩`. Use F.5 naming discipline (Tech/Plain registers).              |
| **AP‑6**  | **Evidence by Prestige**       | “Industry practice says …” offered instead of KD‑CAL‑shaped facts.                          | Replaces observable Results with authority talk.                           | State an **evidence shape Σ(Context)** in **M5**; later fill it with **Observation/Result** facts (KD‑CAL).                     |
| **AP‑7**  | **Design/Run Inversion**       | Verifying a design‑time mask by design documents; verifying a run‑status with design specs. | Violates DesignRunTag; yields non‑falsifiable claims.                   | Apply **M2 Stance**: the Template’s stance must be compatible with the Context. Evidence follows the stance.                    |
| **AP-8**  | **Premature Bridge**           | ... | ... | Keep the assignment/status claim local; if needed, create an **F.9 Bridge** with loss notes and CL penalty.                  |
| **AP‑9**  | **Token Proofs**               | Single anecdotal event taken as universal confirmation.                                     | Over‑generalises; ignores evidence windows and procedures.                 | In **M5**, include **Procedure** and **Window**; in **M6**, roll confidence γ from adequacy of sampling (KD‑CAL).            |
| **AP‑10** | **Role Explosion as Patch**    | New Role minted for every exception.                                                        | Name bloat; brittle semantics.                                             | Re‑examine **eligibility** and **Window**; consider a **Status** to mark exceptions instead of new Roles.                    |
| **AP‑11** | **Subject Drift**              | Status asserted on the wrong subject (team vs service; asset vs dataset).                   | Breaks referent clarity; evidence no longer matches.                       | Use **M4**’s split: **plays\_role(H, …)** vs **has\_status(subject(H), …)**; pick the correct subject kind.                  |
| **AP‑12** | **Spec‑in‑Name**               | Cramming constraints into the label (“24x7‑Operator‑With‑Pager”).                           | Names become brittle; invariants become invisible.                         | Keep the label minimal (F.5); move constraints into **eligibility**/**invariants**.                                          |
| **AP‑13** | **Non‑Local Evidence Shape**   | Evidence shape mentions constructs from another Context.                                       | Hidden Cross‑context import.                                                  | Rewrite Σ using only this Context’s vocabulary; if impossible, use **F.9** Bridge and keep Σ local.                             |

### 10 · Worked examples (multi‑architheory)

> Each example is a **context-local** assignment/status reasoning trace using **M1…M6**. cross-context relations, if any, are noted as *optional* bridges (F.9) but not relied upon.

#### 10.1 Service availability status (ITIL + KD‑CAL)

**Context.** *ITIL 4 (services family; design)*
**Template (Status).* `SLO:availability≥99.9%` anchored at **SenseCell** ⟨ITIL4, “SLO (availability)”⟩.

**M1 Locate.** `address(τ)=⟨ITIL4, SLO(availability)⟩`
**M2 Stance.** `stance(ITIL4)=design`, `stance(τ)=design` ⇒ `compatible_stance(τ, ITIL4)`
**M3 Qualify.** `eligible(Service S, τ@ITIL4)` if S is a published service with declared availability target.
**M4 Assert.** `has_status(S, τ:ITIL4) @ W` where `W = Q1‑2025` (the evaluation period).
**M5 Evidence shape Σ(ITIL4).** *Observation* of **availability characteristic** (MM‑CHR) for S, produced by a **Procedure** that samples uptime and computes the **Result** as ratio over `W`. (KD‑CAL/MM‑CHR terms only; no tool implied.)
**M6 Conclude.** If Results across `W` give ≥ 99.9 % with adequate sampling and declared exclusions applied, `holds( has_status(S, τ:ITIL4) @ W ) with γ≈0.9`.
*Optional bridge.* If uptime sensing vocabulary is expressed in **SOSA/SSN**, an **F.9 Bridge** may map ITIL’s “availability metric” to **ObservableProperty(availability)** with a declared CL penalty; the assignment/status claim itself remains ITIL-local.

#### 10.2 Behavioural operator role (IEC 61131‑3 + Enactment)

**Context.** *IEC 61131‑3 (control languages; run)*
\**Template (Role).* `Control‑Task‑Executor` anchored at **SenseCell** ⟨IEC61131‑3, “task executes program”⟩.

**M1 Locate.** `address(τ)=⟨IEC61131‑3, task‑execution⟩`
**M2 Stance.** `stance(IEC61131‑3)=run`, `stance(τ)=run` ⇒ compatible.
**M3 Qualify.** Holder `PLC_7` qualifies if it hosts program `P` and is scheduled by task `T`.
**M4 Bind.** `plays_role(PLC_7, τ:IEC) @ W` where `W = [08:00, 18:00] 2025‑06‑05`.
**M5 Evidence shape Σ(IEC).** **Observation** of task schedule and program invocation logs as **Results** for features `T`/`P` during `W`; presence of expected cyclic/event‑driven triggers.
**M6 Conclude.** If Results show the expected executions with no missed cycles beyond tolerance, `holds( plays_role(PLC_7, τ:IEC) @ W ) with γ≈0.8`.
*Trip-wire.* Do **not** restate this as “PROV Activity” without **F.9**; keep the assignment/status claim IEC-local.

#### 10.3 Dataset accuracy status (ISO/IEC 25024 + KD‑CAL)

**Context.** *ISO/IEC 25024 (data‑quality; design)*
\**Template (Status).* `accuracy≥0.98` anchored at **SenseCell** ⟨ISO25024, “data accuracy”⟩.

**M1 Locate.** `address(τ)=⟨ISO25024, data‑accuracy⟩`
**M2 Stance.** `stance(Context)=design`, `stance(τ)=design` ⇒ compatible.
**M3 Qualify.** Subject `Dataset D` has a defined **reference set** and sampling protocol.
**M4 Assert.** `has_status(D, τ:ISO25024) @ W` where `W = “snapshot v2025‑04”`.
**M5 Evidence shape Σ(ISO25024).** **Observation** of correctness of sampled records vs reference, **Procedure** per standard, **Result** as proportion correct with confidence interval.
**M6 Conclude.** If CI lower bound ≥ 0.98, `holds( has_status(D, τ) @ W ) with γ≈0.85`.

#### 10.4 Access vs behavioural: two claims, two Contexts

**Contexts.** *NIST RBAC (access; design)* and *BPMN 2.0 (workflow; design)*.
**Templates.** `DB‑Admin (RBAC status)` vs `Participant (BPMN role)`.

**RBAC claim (Status).**
M1…M6 yield `has_status(User U, RBAC:DB‑Admin) @ W_dir` with Σ(RBAC) = **Observation** of assignment state in the access model at time `W_dir`.

**BPMN claim (Role).**
M1…M6 yield `plays_role(Team T, BPMN:Participant) @ W_proc` with Σ(BPMN) = **Observation** that lanes/pools enact tasks during `W_proc`.

**Lesson.** Two separate **context-local** claims — one **Status assertion** and one **Role assignment**; **no** implication that holding RBAC status entails playing the BPMN Role.

### 11 · Relations (with other patterns)

**Builds on:**
F.1 **Domain‑Family Landscape Survey** (Contexts fixed); F.2 **Term Harvesting** (local terms); F.3 **Intra‑Context Clustering** (SenseCells); F.4 **Role Description** (invariants, stance); F.5 **Naming Discipline** (labels).

**Constrains:**
**F.7** (Concept-Set Table): rows reference **SenseCells**; Role Description cards **point to** those rows but never **create** cross-context identity.
**F.8 Mint or Reuse?** Uses outcomes of **Role/Status** claims to decide: a new **Role/Status** label only when existing Templates cannot express the claim with eligibility/Window adjustments.
**F.9** (Alignment & Bridge): any relation across Contexts is **declared there**; Role Description cards remain context-local.
**F.10 Epistemic Status Mapping.** Consumes **M6** confidences γ and Σ‑adequacy to roll up assurance.

**Coordinates with.** **MM‑CHR** (characteristics, scales) wherever *Characteristic/Scale* is used in evidence shapes.

**Used by.**
Architheories (Part C) to anchor their examples: Sys‑CAL (execution/actuation roles), KD‑CAL (measurement statuses), Method‑CAL (execution claims for Methods/MethodDescription), Kind-CAL (typing claims remain outside Role Assignment & Enactment, but may inform eligibility predicates).

### 12 · Migration notes (conceptual)

1. **Template refactor.** If a Template’s invariants change, **claims remain as‑is**; re‑evaluate **M6** on demand. Do not silently rewrite past claims.
2. **Edition updates.** When a Context’s canon updates, treat it as a **new Context** if sense shifts; Claims anchored to the old Context stay valid for their Window.
3. **Name revisions.** Renaming per F.5 does not alter **address(τ)=⟨Context, SenseCell⟩**; claims reference the address, not surface form.
4. **Bridge introduction.** Adding an **F.9 Bridge** never upgrades an existing Role/Status claim; at most it enables *separate* translations with declared loss.
5. **From exception to Status.** If recurring exceptions to a Role appear, prefer minting a **Status** Template that marks the exception rather than proliferating Roles.
6. **Window tightening.** If evidence shows drift, narrow future **Windows**; past claims remain tied to their original Windows.

### 13 · Acceptance tests (SCR/RSCR — concept‑level)

#### 13.1 Static conformance (SCR)

* **SCR-F6-S01 (Local address).** Every assignment/status claim states `address(τ)=σ` where `σ` is a **SenseCell** (per F.3); no bare labels.
* **SCR‑F6‑S02 (SenseFamily clarity).** Each claim is typed **Role** or **Status**, never both; subjects are of the correct kind. Claim records both **senseFamily** and **stance** explicitly or by inheritance.
* **SCR‑F6‑S03 (Stance compatibility).** `stance(Context)` and `stance(τ)` are compatible (design/run).
* **SCR‑F6‑S04 (Eligibility first).** For each claim, `eligible(H, τ@context)` is derivable prior to assertion.
* **SCR‑F6‑S05 (Window explicit).** Each claim has a Window (explicit or inherited) consistent with stance.
* **SCR‑F6‑S06 (Evidence‑ability).** For each claim, an **evidence shape Σ(Context)** is stated using only that Context’s vocabulary plus KD‑CAL/MM‑CHR primitives.
* **SCR‑F6‑S07 (Locality guard).** No Cross‑context terms appear inside a claim; any reference to other Contexts is flagged as **F.9 Bridge (informative)**, not used to justify the claim.

#### 13.2 Regression (RSCR)

* **RSCR‑F6‑E01 (Edition stability).** Adding a new edition/Context does not mutate existing claims’ Contexts or Windows.
* **RSCR‑F6‑E02 (Name stability).** Changing labels per F.5 leaves addresses and conclusions invariant.
* **RSCR‑F6‑E03 (Bridge neutrality).** Introducing or revising an **F.9 Bridge** does not auto‑flip claim truth values; at most it enables explicit translations with loss notes.
* **RSCR‑F6‑E04 (Evidence refresh).** When KD‑CAL procedures or **MM‑CHR characteristic scales** change, only **γ** is re‑evaluated; the claim’s semantics remain.

### 14 · Didactic distillation (60‑second recap)

> **Six moves.** (M1) *Locate* the Context & SenseCell; (M2) check **stance**; (M3) test **eligibility**; (M4) **bind/assert** with a **Window**; (M5) sketch the **evidence shape** in that Context; (M6) **conclude** with confidence γ.
> **Two iron rules.** Keep it **context‑local**; keep **Role** and **Status** on their senseFamily.
> **Pay-off.** Assignment/status claims become small, auditable thoughts: easy to teach, easy to check, and easy to relate—later—via explicit Bridges when you truly must step between Contexts.

# F.7 — Concept‑Set Table \[A]

**“Show one thing across Contexts—only where explicit bridges allow it.”**

**Status.** Architectural pattern \[A], architheory‑agnostic.
**Depends on.** E.10.D1 **Lexical Discipline for ‘Context’** (Context ≡ `U.BoundedContext`); **F.0.1 senseFamily (normative)**; F.1 **Domain‑Family Landscape Survey**; F.2 **Term Harvesting**; F.3 **Intra‑Context Sense Clustering** (SenseCells); F.5 **Naming Discipline**; F.9 **Alignment & Bridge Across Contexts**.
**Coordinates with.** F.4 **Role Description**; F.6 **Role Assignment & Enactment Cycle (Six-Step)**; Part C architheories (for examples), **MM‑CHR (for Characteristic)**.
**Aliases (informative).** *Concept‑Set table*, *comparison grid*.

---

## 1 · Intent & applicability

**Intent.** Provide a **single, didactic page** where each **row** presents **one Concept‑Set**—a *set of SenseCells from different Contexts that we are licensed (by explicit Bridges) to treat as “the same for a stated scope”*. Columns are **Contexts**; cells carry **local labels**. The table **does not invent equivalences**: it **summarises** already declared **F.9 Bridges**, exposing *scope, losses, and counter‑examples* at a glance.

**Applicability.** Use whenever cross-context reading is necessary (naming U.Types, teaching contrasts, assignment/enactment-adjacent terminology). It is a **reading lens**, not a data model: **notation-free**, **governance-free**, **Context-loyal**.

**Non‑goals.** No hidden merges. No “global terms”. No workflows or tool schemas. The table is a **conceptual display** of *licensed sameness* and *honest non‑sameness*.

---

## 2 · Problem frame

Without a disciplined Cross‑context view:

1. **Silent equivalence.** Readers assume sameness by name alone (e.g., *process*).
2. **Loss denial.** Mappings hide what is dropped (DesignRunTag, units, agency).
3. **Name inflation.** New U.Types are coined to avoid facing heterogeneity.
4. **Cognitive scatter.** Concepts drift across documents without one compact, teachable “where‑what‑how‑same” view.

---

## 3 · Forces

| Force                          | Tension to resolve                                                                                            |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| **Locality vs comparison**     | Meaning lives in Contexts; yet we must **compare** Contexts to reason across disciplines.                           |
| **Didactics vs fidelity**      | A compact row is easy to grasp; it must still show **scope and loss** honestly.                               |
| **Simplicity vs completeness** | A minimal grid aids memory; temptation to overload it with proofs and procedures must be resisted.            |
| **Sameness vs difference**     | Some families **cannot** be unified; the table must support **contrast rows** without pretending equivalence. |

---

## 4 · Core idea (didactic)

A **Concept‑Set** is a **finite set of addresses**

$$
\text{CS}=\{\langle \text{Context}_i,\ \text{SenseCell}_i\rangle\}_{i=1..n}
$$

that FPF **treats as one** *for a declared scope* because there exist **F.9 Bridges** connecting these SenseCells pairwise (directly or via a short chain) with **congruence level** $\text{CL}$ above a **threshold** suitable for that scope. The **table row** shows:

* **FPF Label** *(Tech/Plain)* — the *didactic, FPF‑level* name chosen per F.5.
* **Row Scope** — where “being one” is safe (e.g., *Naming-only*, *assignment/enactment-eligibility*, *KD-CAL metric*, *Type‑structure*).
* **Row CL(min)** — the **minimum CL** of the Bridges that justify the row.
* **Context columns** — each cell: the **local label** + (optional) short cue.
* **Rationale (one line)** — why sameness is warranted *for this scope*.
* **Counter‑examples (one line)** — where/why sameness **breaks**.

> **Memory hook.** *A Concept‑Set row is a promise:* “You may **read across** these Contexts **this far—and no farther**.”

---

## 5 · Minimal vocabulary (this pattern only)

* **Context** — shorthand for `U.BoundedContext` (per E.10.D1).
* **senseFamily** — **referenced from F.0.1**; not redefined here; used to **type** rows and to require **uniformity** within a row.
* **SenseCell** — a **(Context × Local‑Sense)** address from F.3.
* **Bridge (F.9)** — an explicit, declarative Cross‑context mapping with a **congruence level** **CL** and **loss note**.
* **Characteristic (MM‑CHR)** — measurable comparandum defined in **MM‑CHR**; may be referenced in **Measurement/KD‑metric** rows; **do not** use “axis” only as a euphemism.
* **Concept‑Set (row)** — a *licensed sameness* across Contexts, bounded by **Row Scope** and **Row CL(min)**.
* **Contrast row** — a *non‑sameness* row: same surface across Contexts with **no** sufficient Bridges; teaches **difference**, not unity.

---

## 6 · The table (conceptual layout)

> One page. Fixed column order by Context. Each row fits in **five lines** max.

```
FPF Label (Tech / Plain) | Row Scope | Row CL(min) | [Context A] local label | [Context B] local label | [Context C] local label | Rationale | Counter‑examples
```

**Reading rules (didactic):**

1. **Cells are local.** A cell is **not** a translation; it is the Context’s **own** label for its SenseCell.
2. **Scope is king.** The FPF label only licenses sameness **within its Row Scope**. Outside that scope, treat cells as **different**.
3. **Row CL(min) governs trust.** Lower CL ⇒ narrower applicability; **never** up‑scope a row without revisiting Bridges.
4. **Rationale & counter‑examples** are **obligatory one‑liners**; if you need paragraphs, you need an F.9 walkthrough, not a row.

**Didactic name rationale** “Giants' table’” that alludes to *standing on the shoulders of giants*: each row explicitly leans on authoritative context of meaning (**U.BoundedContext**) established by prior disciplines and not imagined. It does **not** mean a physically large table; the name signals epistemic humility and traceable reliance on those sources. "We are like dwarfs on the shoulders of giants, so that we can see more than they, and things at a greater distance, not by virtue of any sharpness of sight on our part, or any physical distinction, but because we are carried high and raised up by their giant size." by Bernard of Chartres , d. c.1130, French philosopher.

## 7 · Conceptual construction (thought moves, not workflow)

> The table is derived from earlier patterns; it **creates nothing new**.

* **Sourcing.** Candidate cells come **only** from **SenseCells** (F.3).
* **Licensing.** A row exists **iff** the relevant **Bridges (F.9)** already justify sameness at the chosen **Row Scope**.
* **Bounding.** Prefer **2–4 Contexts** per row (parsimony); add more only if each adds a *distinct necessity* for the sameness claim.
* **Typing.** A row is **typed by senseFamily**: Role, Status, Type‑structure, Measurement, etc. **Do not mix senseFamilies** in one row.
* **Temporal honesty.** A row’s cells must share **compatible DesignRunTag**; if not, either split into two rows or mark a **contrast row**.

---

## 8 · Invariants (normative)

1. **Context‑loyal cells.** Every non‑empty cell is a **SenseCell** address; no minted paraphrases.
2. **Bridge sufficiency.** For a *Concept‑Set* row, **every pair** of filled cells is connected by an **F.9 Bridge path** whose **bottleneck CL** ≥ **Row CL(min)** printed for the row.
3. **Scope declaration.** Each row **MUST** declare a **Row Scope** chosen from a small controlled set (e.g., *Naming-only*, *assignment/enactment-eligibility*, *KD-metric*, *Type-structure*).
4. **senseFamily uniformity.** All cells in a row belong to the **same senseFamily** (Role **or** Status **or** Type-structure **or** Measurement…).
5. **Temporal compatibility.** Either all cells share the **same stance**, or the row is a **contrast row** (no sameness claim).
6. **Loss disclosure.** If any Bridge in the row has a **loss note**, the row **MUST** include a **counter‑example** that illustrates that loss in one line.
7. **No stealth expansion.** Adding a new cell to a row **MUST NOT** lower the printed **Row CL(min)** without updating **Row Scope** or splitting the row.
8. **Parsimony.** A row with only one filled cell is **forbidden** (that would be local talk, not a Cross‑context concept).
9. **Didactic bound.** A row that cannot be read in **≤ 30 seconds** violates didactic primacy and must be split.

---

## 9 · Micro‑illustrations (safe patterns)

> Illustrative only; these presume corresponding **F.9 Bridges** exist with stated CL and losses.

**(a) Subtyping across type‑formalisms (Type‑structure row)**

| FPF Label                                  | Row Scope      | Row CL(min) | OWL 2             | Kind-CAL            | Rationale                                                        | Counter‑examples                                                         |
| ------------------------------------------ | -------------- | ----------- | ----------------- | ------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **is‑a (Tech)** / *type hierarchy* (Plain) | Type‑structure | CL = 3      | `rdfs:subClassOf` | `U.SubtypeRelation` | Both are partial‑order *class* subsumption used for inheritance. | FCA *concept* order is not a class subsumption; keep it out or CL drops. |

**(b) “Observation result value” (Measurement row)**

| FPF Label                           | Row Scope | Row CL(min) | SOSA/SSN                | ISO 80000‑1                    | ITIL 4                       | Rationale                                                                                           | Counter‑examples                                                |
| ----------------------------------- | --------- | ----------- | ----------------------- | ------------------------------ | ---------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **result‑value** / *measured value* | KD‑metric | CL = 2      | `sosa:Result` (literal) | `QuantityValue` (unit‑bearing) | *metric value* (service KPI) | Values can be read as numbers tied to a Characteristic; ITIL metric uses same notion when unitised. | ITIL “metric” may be composite indices (loss of unit fidelity). |

**(c) Contrast row: “process” (no sameness)**

| FPF Label              | Row Scope | Row CL(min) | BPMN 2.0              | PROV‑O                  | Thermodynamics           | Rationale                                                 | Counter‑examples                                                                   |
| ---------------------- | --------- | ----------- | --------------------- | ----------------------- | ------------------------ | --------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **process** (contrast) | —         | —           | *graph of flow nodes* | *time‑bounded activity* | *state‑space trajectory* | Same surface, **different** senses; no licensed sameness. | Any attempt to equate design‑graph with run‑occurrence fails stance compatibility. |


## 10 · Anti‑patterns & remedies

| #         | Anti‑pattern                | Symptom in a row                                                               | Why it breaks thinking                                               | Remedy (conceptual move)                                                                                          |
| --------- | --------------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **AP‑1**  | **Bridge‑free sameness**    | Cells listed as “same” because their labels look alike; no cited Bridges.      | Violates locality; imports meaning across Contexts by name.             | A row **exists only** if backed by **F.9 Bridges**. Otherwise produce a **contrast row**.                         |
| **AP-2**  | **Scope creep**             | Row labelled “Type-structure” but used to justify **assignment/enactment-eligibility** or KD metrics. | Scope licences are not transferable; inference leaks.                | Keep a **small controlled set of Row Scopes**. If use widens, **mint a new row** or **re-bridge** with higher CL. |
| **AP‑3**  | **senseFamily mixing**      | One row mixes Role, Status, Measurement, and Type‑structure cells.             | Conflates senseFamily (F.0.1); readers cannot tell “what kind of sameness”. | **Type each row.** If two senseFamilys are needed, **split** into two rows.                                             |
| **AP‑4**  | **Temporal blur**           | Cells with incompatible DesignRunTag declared “same”.                     | Design artefacts ≠ run occurrences; claims invert.                   | Either **harmonise stance** (choose only compatible cells) or publish a **contrast row**.                         |
| **AP‑5**  | **Loss denial**             | Bridges carry loss notes, but the row omits counter‑examples.                  | Readers over‑trust; misuse outside safe scope.                       | Add a **one‑line counter‑example** that illustrates the loss.                                                     |
| **AP‑6**  | **CL averaging**            | Row CL(min) computed as an average of heterogeneous Bridges.                   | The weakest link governs; averages overstate safety.                 | Row CL(min) is the **bottleneck** (minimum along connecting paths).                                               |
| **AP‑7**  | **Overwide rows**           | 6–8 Contexts in one row; hard to read; subtle mismatches hide.                    | Violates didactic primacy; invites hidden losses.                    | **Parsimony**: 2–4 Contexts per row unless each extra cell has a **distinct necessity** you can state in one line.   |
| **AP‑8**  | **Minted paraphrases**      | Cells reword a Context’s label instead of citing the SenseCell.                   | Hides locality; future drift becomes invisible.                      | **Cells are Context‑loyal.** Use the Context’s own SenseCell label.                                                     |
| **AP‑9**  | **Duplicate rows by style** | Two rows with the same cell set but different FPF labels.                      | Name inflation; readers assume two distinct concepts.                | Keep **one row** per Concept‑Set per scope. Alternative labels appear as **aliases** in F.5, not new rows.        |
| **AP‑10** | **Implied transitivity**    | A↔B and B↔C Bridges exist; row silently assumes A↔C at the same CL.            | Paths can reduce CL; semantics might not compose.                    | Compute CL for **A↔C via bottleneck**; if too low, either reduce **Row Scope** or **omit** the cell.              |

---

## 11 · Worked examples (multi‑architheory)

> Each example gives a **row** (compact), then a **reading** explaining scope and limits. All sameness claims presuppose suitable **F.9 Bridges** with the stated CL.

### 11.1 Behavioural actor across Contexts (naming‑only)

| FPF Label (Tech / Plain)              | Row Scope   | Row CL(min) | BPMN 2.0        | PROV‑O    | Rationale                                                                               | Counter‑examples                                                                                      |
| ------------------------------------- | ----------- | ----------- | --------------- | --------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **actor** / *party that participates* | Naming‑only | CL = 2      | **Participant** | **Agent** | Both denote a bearer that can be named as the party to which activities are attributed. | PROV **Agent** includes software agents; BPMN **Participant** is typically an organisation lane/pool. |

**Reading.** The row licenses a **glossary‑level sameness** for didactic prose (“the actor”). It does **not** license modelling **identity** or inference across Contexts.

---

### 11.2 Execution occurrence (assignment/enactment-eligibility)

| FPF Label                                       | Row Scope       | Row CL(min) | PROV‑O                                                           | IEC 61131‑3                                          | Rationale                                                                       | Counter‑examples                                                   |
| ----------------------------------------------- | --------------- | ----------- | ---------------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| **execution-occurrence** / *a run that happens* | assignment/enactment-eligibility | CL = 2      | **Activity** (time-bounded occurrence using/generating entities) | **Task execution** (cyclic/event-driven program run) | Both are **run-time** occurrences that can be referenced by `U.RoleEnactment` to ground **Work performed under an assignment**. | BPMN **Process** is a **design** graph; not an occurrence—exclude. |

**Reading.** Safe to use as the **run-time occurrence that `U.RoleEnactment` points to** when we say “this Work was performed under an assignment”. Not safe to equate **all** PROV Activities with **all** PLC task runs for analytics.

---

### 11.3 Result value as KD‑metric (measurement)

| FPF Label                           | Row Scope | Row CL(min) | SOSA/SSN             | ISO 80000‑1                      | ITIL 4           | Rationale                                                                                                | Counter‑examples                                               |
| ----------------------------------- | --------- | ----------- | -------------------- | -------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **result‑value** / *measured value* | KD‑metric | CL = 2      | **Result** (literal) | **QuantityValue** (unit‑bearing) | **metric value** | A number representing a **Characteristic** at observation time; can be unitised and compared to targets. | ITIL “metric” may be a composite index; units may be implicit. |

**Reading.** Licences **metric tables** that join observations to service targets; warns that composite KPIs may violate unit fidelity.

---

### 11.4 Subtype relation (type‑structure)

| FPF Label                   | Row Scope      | Row CL(min) | OWL 2             | Kind-CAL            | Rationale                                     | Counter‑examples                                                                 |
| --------------------------- | -------------- | ----------- | ----------------- | ------------------- | --------------------------------------------- | -------------------------------------------------------------------------------- |
| **is‑a** / *type hierarchy* | Type‑structure | CL = 3      | `rdfs:subClassOf` | `U.SubtypeRelation` | Both are partial orders used for inheritance. | FCA **concept order** is not a class subsumption—exclude or publish another row. |

---

### 11.5 Contrast: “role” (access vs behaviour)

| FPF Label           | Row Scope | Row CL(min) | NIST RBAC                 | BPMN 2.0                                 | Rationale                                                      | Counter‑examples                                                                   |
| ------------------- | --------- | ----------- | ------------------------- | ---------------------------------------- | -------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **role** (contrast) | —         | —           | **Role** (permission set) | **Participant/Actor** (behavioural mask) | Same surface; **different senseFamilys** (Status vs Role/behaviour). | Any attempt to unify collapses deontics into behaviour; stance and effects differ. |

**Reading.** This row **teaches difference**; it deliberately **does not** license sameness.

---

## 12 · Reasoning primitives (judgement schemas, notation‑free)

> All judgements are **pure** (no side effects). “Contexts” are `U.BoundedContext`. `SC(C)` denotes a SenseCell in Context `C`. `CL(X↔Y)` is the congruence level of the **best** Bridge path (F.9) between SenseCells `X` and `Y` (bottleneck along that path).

### 12.1 Row licensing

**Form.**
`S = {SC(C₁), …, SC(Cₙ)}, Scope = s, τ(s) = requiredCL ⊢ licensable(S,s) ⇔ (∀ i<j: CL(SC(Cᵢ)↔SC(Cⱼ)) ≥ requiredCL ∧ senseFamily (S) is uniform ∧ stance(S) compatible)`

**Reading.** A set of cells **licenses** a row of scope `s` iff every pair is bridged at or above the **required CL** for that scope, all cells sit in the **same senseFamily**, and **DesignRunTag** is compatible.

---

### 12.2 Bottleneck CL for a row

**Form.**
`RowCL(S) = min_{i<j} CL(SC(Cᵢ)↔SC(Cⱼ))`

**Reading.** The row’s CL is the **minimum** congruence level across all pairs (the weakest link).

---

### 12.3 Scope guard

**Form.**
`licensable(S,s) ∧ s ⊑ s' ⊢ licensable(S,s') only if RowCL(S) ≥ τ(s')`

**Reading.** You may **tighten scope** (use the row for a stronger purpose) only if the row’s CL meets the **higher threshold** for that scope.

---

### 12.4 Contrast decision

**Form.**
`(∃ i<j: CL(SC(Cᵢ)↔SC(Cⱼ)) < τ(Naming‑only)) ⊢ publish‑contrast(S)`

**Reading.** If even **Naming‑only** cannot be licensed, publish a **contrast row** instead of forcing sameness.

---

### 12.5 Row extension guard

**Form.**
`licensable(S,s) ∧ add SC(Cₖ) ⊢ licensable(S∪{SC(Cₖ)}, s) iff ∀ i: CL(SC(Cᵢ)↔SC(Cₖ)) ≥ τ(s)`

**Reading.** You may add a new cell only if it bridges to **every existing cell** at the row’s scope.

---

### 12.6 Loss disclosure obligation

**Form.**
`licensable(S,s) ∧ (∃ i<j: lossNote on Bridge(SC(Cᵢ),SC(Cⱼ))) ⊢ row must carry ≥1 counter‑example`

**Reading.** Any loss note on any supporting Bridge obliges the row to include a **counter‑example one‑liner**.

---

## 13 · Relations (with other patterns)

**Builds on:**
F.1 **Contexts fixed** → defines the column set; F.2 **Harvest** → supplies term material; F.3 **SenseCells** → provide cell addresses; F.5 **Naming Discipline** → provides the two‑register **FPF labels**; F.9 **Bridges** → legally justify each row.

**Constrains:**
F.4 **Role Description** — when a template cites an FPF label from the table, it **inherits the Row Scope**; no template may claim semantics beyond the row’s licence.
F.6 **Role Assignment & Enactment Cycle (Six-Step)** — Move M‑4 (“choose label”) must reference a row if it wants Cross‑context reading.

**Used by.**
Part C architheories for didactic alignment pages; Part B trust calculus (B.3) may consume **Row CL(min)** when computing translation penalties.

---

## 14 · Migration notes (conceptual)

1. **Bridge update.** If any supporting Bridge’s CL changes, recompute **Row CL(min)**. If it drops below the printed value, either **lower Row Scope**, **split** the row, or **retire** it.
2. **New Context appears.** Do **not** auto‑expand rows. Test with **12.5**; add only if it brings a **distinct necessity**.
3. **Sense revision inside a Context.** If a SenseCell splits (F.3), decide which child cell (if any) remains in the row; the rest may require **new rows** or a **contrast**.
4. **Scope promotion.** To use a row for a stronger purpose (e.g., from **Naming-only** to **assignment/enactment-eligibility**), first ensure **Row CL(min) ≥ τ(new scope)**; otherwise construct **new Bridges** or **decline** promotion.
5. **Deprecation.** If a row no longer meets its invariant, mark its FPF label as **retired** in F.5 and point to successor rows (if any).
6. **Edition churn.** When a Context is superseded (F.1), either keep the cell (if semantics stable) or treat the successor as a **new Context** and re‑evaluate licensability.

---

## 15 · Acceptance tests (SCR/RSCR — concept‑level)

### 15.1 Static conformance checks (SCR)

* **SCR‑F7‑S01 (Context‑loyal cells).** Every non‑empty cell references an existing **SenseCell** (F.3) in a declared Context (F.1).
* **SCR‑F7‑S02 (Closure & bottleneck).** For each Concept‑Set row, **every pair** of cells has a Bridge path with CL ≥ **Row CL(min)** printed; **Row CL(min)** equals the **minimum** pairwise CL.
* **SCR‑F7‑S03 (Typed & scoped).** Each row declares a **Row Scope** from the controlled set and is **senseFamily‑uniform** (Role **or** Status **or** Measurement **or** Type‑structure…).
* **SCR‑F7‑S04 (Temporal compatibility).** Non‑contrast rows have **compatible** DesignRunTag across cells.
* **SCR‑F7‑S05 (Loss disclosure).** If any supporting Bridge has a recorded loss, the row includes **≥1 counter‑example** line.
* **SCR‑F7‑S06 (Parsimony).** Rows contain **2–4 Contexts** unless a one‑line necessity is stated for each extra Context.

### 15.2 Regression checks (RSCR)

* **RSCR‑F7‑E01 (Bridge drift).** After any Bridge change (F.9), recompute **Row CL(min)**; flag rows whose scope is now overstated.
* **RSCR‑F7‑E02 (Sense split).** After a SenseCell splits (F.3), ensure rows referencing it either pick a child cell or retire.
* **RSCR‑F7‑E03 (Scope integrity).** No consumer pattern uses a row outside its declared **Row Scope**.
* **RSCR‑F7‑E04 (No stealth growth).** Additions of cells never lower **Row CL(min)** silently; if they do, either split the row or reduce scope.

---

## 16 · Didactic distillation (60‑second teaching script)

> “A **Concept-Set row** shows **one idea across Contexts**—but only where explicit **Bridges** license it. Columns are Contexts; cells are **their own labels**. The row prints a **scope** (‘Naming-only’, ‘assignment/enactment-eligibility’, ‘Type-structure’, ‘KD-metric’) and the **weakest CL** that justifies reading across. A **one‑line rationale** says why sameness is safe **here**; a **counter‑example** warns where it breaks. Keep rows small (2–4 Contexts), typed (don’t mix senseFamilies), and temporally honest (design vs run stance). If Bridges don’t suffice, publish a **contrast row** instead. The table doesn’t invent meaning; it **summarises licensed sameness** so readers can cross disciplines without smuggling assumptions.”

# F.8 — Mint or Reuse? (U.Type vs Concept-Set vs Role Description vs Alias) \[A] 

**“Name only what thinking **requires**, and reuse everything else.”**

**Status.** Architectural pattern \[A], architheory‑agnostic.
**Depends on.** E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; A.7 **Strict Distinction**; A.11 **Ontological Parsimony**; A.8 **Universal Core**.
**Coordinates with.** F.1 **Contexts (Contexts)**; F.2 **Harvest**; F.3 **SenseCells**; F.4 **Role Description**; F.5 **Naming Discipline**; F.7 **Concept‑Set Table**; F.9 **Alignment & Bridge**.
**Aliases (informative).** *Mint‑vs‑Reuse gate*; *Naming governor*.

---

## 1 · Intent & applicability

**Intent.** Provide a **minimal, conceptual decision lattice** that answers, for any modelling need:

> “Do I **reuse** an existing label, add an **alias**, reference a **Concept‑Set row**, define a **Role Description**, or mint a **new U.Type**?”

The lattice enforces **locality of meaning** (Contexts), **senseFamily separation** (A.7), and **parsimony** (A.11) while remaining didactically simple.

**Applicability.** Use whenever a new name seems “needed” in any architheory thread (**Role Assignment & Enactment**, Sys-CAL, KD-CAL, Kind-CAL, Method-CAL, LCA-CAL…).

**Non‑goals.** No workflows, no roles, no storage. This is **thinking discipline**, not process guidance.

---

## 2 · Problem frame

Modellers tend to **mint names** when they actually need **reuse**, **aliasing**, or **explicit Cross‑context reading**. Consequences:

1. **Name inflation.** Parallel labels for the same idea across Contexts.
2. **senseFamily mixing.** Behavioural **Role** names that smuggle in deontic **Status** or measurement talk.
3. **Hidden bridges.** Cross‑context sameness is implied by look‑alike words rather than declared (F.9).
4. **Kernel sprawl.** New **U.Types** appear to plaster over local vocabulary gaps.

---

## 3 · Forces

| Force                       | Tension to resolve                                                                            |
| --------------------------- | --------------------------------------------------------------------------------------------- |
| **Parsimony vs coverage**   | Avoid new names unless necessary, yet cover recurring Cross‑context readings.                    |
| **Locality vs unification** | Keep senses **in‑Context**; when reading across, do it **explicitly** and only as far as needed. |
| **Didactics vs fidelity**   | Give readers one label to hold, but never over‑state sameness (respect CL and scope).         |

---

## 4 · Minimal vocabulary (used in this pattern only)

* **Context** — `U.BoundedContext` (per D.CTX).
* **SenseCell** — address of a **local sense** produced by F.3 (one context × one clustered sense).
* **Concept‑Set row** — a **licensed Cross‑context reading** (F.7) of cells in one senseFamily with a declared **Row Scope** and **Row CL(min)**.
* **senseFamily** — as defined in **F.0.1**; here used as the **typed discriminator for rows** restricted to {Role | Status | Measurement | Type‑structure | Method | Execution}. 
* **Role Description** — a **Role/Status** template anchored to a **single SenseCell** (F.4).
* **Alias** — an **additional label** for an existing FPF label (within F.5), no new semantics.
* **CL threshold τ(scope)** — the **minimum congruence level** needed for a row’s scope (e.g., τ(Naming-only) < τ(Assignment-eligibility) < τ(Type-structure)).

---

## 5 · The decision lattice (conceptual, notation‑free)

> Read top‑to‑bottom; the **first satisfied** branch decides. At every step, **state the senseFamily** (Role / Status / Measurement / Type‑structure / Method / Execution) before you proceed.

### Q0 — What is the **senseFamily** of your need?

* If **uncertain**, return to F.1/F.3: stabilise the Context(s) and the local sense.
* If **mixed**, split the need: one decision **per senseFamily** (A.7).

### Q1 — Is there a **single Context** whose SenseCell already expresses it?

* **Yes →** **Reuse** the **SenseCell**’s label **inside that Context**.

  * If you need assignable behaviour or deontics on that sense: **define a Role Description** **anchored to that SenseCell** (F.4).
* **No →** go to Q2.

> *Example (engineer).* You want “**task execution**” in control software. In `IEC 61131‑3` there is a clear SenseCell for **task execution**. **Reuse** that label; if you need responsibilities (“who monitors runs”), define a **Role Description** anchored to this SenseCell.

### Q2 — Do you need to **read across Contexts** (same senseFamily)?

* **No →** stay within one context; if your desire is merely a nicer label, consider an **Alias** (Q3).
* **Yes →** check F.7 for a **Concept‑Set row** covering your cells **in this senseFamily** with adequate **Row Scope** and **Row CL(min)**.

  * **Found & sufficient →** **Reuse the row’s FPF label** at that scope.
  * **Not found or insufficient →** either (a) **publish a contrast** (teach difference), or (b) propose a **new row** but only after F.9 Bridges exist at **τ(scope)**.

> *Example (manager).* You want one label for the **actor** in workflow and provenance prose. F.7 has a **Naming‑only** row mapping *BPMN Participant* ↔ *PROV Agent* at CL = 2. **Reuse** “actor” **at Naming‑only** scope; do **not** infer identity in models.

### Q3 — Is this **only a wording preference** for an existing FPF label?

* **Yes →** add an **Alias** in F.5 (Tech register and/or Plain register), no semantics changed.
* **No →** go to Q4.

> *Example (researcher).* You prefer “**is‑a**” to “**subclass‑of**” in Type pages. That is an **Alias** for the same concept; no new row, no new U.Type.

### Q4 — Does your need recur across Contexts in a way **not captured** by current rows, **with Bridges** already available at the required CL?

* **Yes →** propose a **new Concept‑Set row** (F.7): small (2–4 Contexts), **one senseFamily**, declare **Row Scope** and **Row CL(min)**, include a **counter‑example** if any Bridge has loss notes.
* **No →** go to Q5.

> *Example (engineer).* You repeatedly compare **runtime occurrence** in PROV with **PLC task runs**. F.9 Bridges exist at CL = 2. Propose **row “execution-occurrence”** at **assignment/enactment-eligibility** scope (not Type-structure).

### Q5 — Are you describing a **kernel‑level notion** missing from the catalogue, **not** reducible to existing rows or Role Descriptions, and **present across ≥ 3 domain families** (A.8)?

* **Yes →** propose a **new U.Type** (rare). Supply:
  (i) the minimal **intensional definition**; (ii) cross‑family evidence (≥ 3 Contexts, **distinct families**); (iii) how it **doesn’t** duplicate an existing U.Type.
* **No →** you **do not mint** a new type. Re‑express the need in terms of **Context reuse**, **row reuse**, **Alias**, or a **Role Description**.

> *Example (researcher).* You think we need **U.InfluenceEdge** (causal tendency). If it appears as a stable, **senseFamily‑specific** notion across **control**, **epistemic inference**, and **methods** (≥ 3 families), and cannot be formed from existing `U.Relation` subtypes, it **may** qualify. Otherwise, treat it as a **pattern** or a **row**.

---

## 6 · Scope thresholds (default τ) — **how much sameness** you’re allowed to claim

| Row / Use Scope     | What it licenses                                                                              | Default τ (minimum CL) | Typical consumers                         |
| ------------------- | --------------------------------------------------------------------------------------------- | ---------------------: | ----------------------------------------- |
| **Naming‑only**     | Shared label in prose, diagrams, and primers; **no inference**.                               |                  **1** | Pedagogy, glossary, didactic figures.     |
| **Assignment-eligibility** | Safe to reference the row’s target as the **thing a `U.RoleAssignment` may point to** (e.g., a run, a value). | **2** | F.4 Role Description, acceptance narratives. |
| **KD‑metric**       | Treat cells as the **same measured outcome** (unit‑compatible, procedure‑compatible).         |                  **2** | Measurement summaries, SLO tables.        |
| **Type‑structure**  | Treat cells as the **same structural relation** (e.g., subtyping) with inheritance semantics. |                  **3** | Kind-CAL pages, structural proofs.        |

> **Guard.** You may **tighten** scope (e.g., from Naming-only → Assignment-eligibility) **only** if the **Row CL(min)** meets the **higher τ**.

---

## 7 · Micro‑examples (didactic triad)

### 7.1 For engineers — “Do we need a new **Execution** label?”

* **Need.** “We want to refer to **what actually happened** in both provenance logs and PLC runtime.”
* **senseFamily.** Execution · **stance.** run.
* **Contexts.** `PROV‑O` (Activity), `IEC 61131‑3` (task run).
* **Row?** F.7 has **execution-occurrence** at **assignment/enactment-eligibility**, CL = 2.
* **Decision.** **Reuse** that row’s label at **Assignment-eligibility**; **no** new U.Type; define Role Descriptions **anchored to each Context** as needed.

### 7.2 For managers — “Can we call them all **actors**?”

* **Need.** A single everyday word in the spec to denote “the responsible party”.
* **senseFamily.** Role (behavioural mask in prose).
* **Contexts.** `BPMN 2.0` (Participant), `PROV‑O` (Agent).
* **Row?** **Naming‑only** row “actor”, CL = 2.
* **Decision.** **Reuse** “actor” **in prose only**; keep Context‑loyal labels in formal sections. No Role Description minted unless tied to one context.

### 7.3 For researchers — “New **U.Type** for ‘Work Scope’?”

* **Need.** Kernel notion capturing **feasible performance region** across systems.
* **Test A.8.** Appears in **control** (reachable sets), **services** (operating envelope), **measurement** (confidence bands): **≥ 3 families?**
* **Reduction test.** Can it be expressed as a **row** + existing `U.Relation` + KD‑CAL constructs?
* **Decision.** If **not reducible** and **cross‑family stable**, propose **new U.Type** with minimal definition; otherwise, prefer a **row** or a **pattern**.

---

## 8 · Invariants (normative, lightweight)

1. **Context‑first.** Every decision cites at least one **Context**; no global senses.
2. **senseFamily purity.** A single decision covers **one senseFamily**. Mixed needs are split.
3. **Row honesty.** Any Cross‑context reuse occurs **via a Concept‑Set row** at or above **τ(scope)**; no stealth equivalence.
4. **Role Description anchoring.** Role Descriptions are **single-Context**, **single-cell** anchors (F.4).
5. **Alias modesty.** Aliases **never** change semantics and live under F.5.
6. **Kernel restraint.** New **U.Types** are **rare**; A.8 **(≥ 3 families)** is mandatory, and duplication with existing U.Types must be ruled out.

---

## 9 · Quick reference (one‑glance map)

| You feel you need…                          | Likely action                  | Why                                              |
| ------------------------------------------- | ------------------------------ | ------------------------------------------------ |
| A convenient everyday word across two Contexts | **Reuse a Naming‑only row**    | Keeps prose simple without smuggling inference.  |
| An assignable mask with invariants          | **Role Description (single Context)** | Roles/Statuses attach to **local** senses.       |
| The same measured outcome across Contexts      | **Reuse a KD‑metric row**      | Units/procedures aligned at CL ≥ 2.              |
| A unifying schema relation (e.g., is‑a)     | **Reuse a Type‑structure row** | Structural inference preserved at CL ≥ 3.        |
| A nicer label for the same FPF concept      | **Alias in F.5**               | Style only; zero semantics.                      |
| A brand‑new primitive concept               | **New U.Type (rare)**          | Only if cross‑family, irreducible, kernel‑level. |

## 10 · Anti‑patterns & remedies

| #         | Anti‑pattern               | Symptom                                                                            | Why it harms thinking                              | Remedy (conceptual move)                                                                                                                         |
| --------- | -------------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **AP‑1**  | **Row‑less sameness**      | Declaring “these mean the same” across Contexts without citing a **Concept‑Set row**. | Imports meaning implicitly; no CL guard.           | If Cross‑context reuse is desired, **reuse an existing row** at a declared **scope** (F.7), else **publish the contrast** and defer to F.9 Bridges. |
| **AP-2**  | **Scope creep**            | Using a **Naming-only** row to justify **Assignment-eligibility** or structural inferences. | Over-claims sameness; breaks τ(scope).             | Respect **scope thresholds** (τ). Upgrade only when **Row CL(min) ≥ τ(new scope)**; otherwise stay Naming-only.                                  |
| **AP‑3**  | **Alias with payload**     | Introducing an Alias that subtly changes intent or senseFamily.                          | Hides semantics behind wording; confuses senseFamilies.   | Aliases (F.5) are **style only**. If semantics change, choose **row reuse** or **Role Description** instead.                                         |
| **AP-4**  | **Role-Description-to-row anchoring** | Role Description points to a **row** rather than a **single SenseCell**.       | Masks locality; **assignments** become cross-context by stealth. | Role Descriptions **must anchor to one SenseCell** (F.4). Use rows only in prose or aggregated views.                                                |
| **AP‑5**  | **Kernel inflation**       | Proposing a new **U.Type** because a convenient label is missing.                  | Duplicates the kernel; violates parsimony.         | Apply A.8: require **≥ 3 domain families** and **irreducibility**; otherwise **Alias** or **row**.                                               |
| **AP‑6**  | **senseFamily mixing**           | One name that conflates Role, Status, Measurement, or Type‑structure.              | Collapses A.7 Strict Distinction.                  | **Split by senseFamily** first (Q0). Decide **per senseFamily**.                                                                                             |
| **AP‑7**  | **Bridge‑by‑string**       | Treating identical surface forms as equivalent senses across Contexts.                | Homonym trap; ignores local sense.                 | Equivalence only via **F.9 Bridge** + **row**; never by string.                                                                                  |
| **AP‑8**  | **Row without loss notes** | Publishing a row where Bridges indicate mismatches, but row text is silent.        | Readers assume full equivalence.                   | Include **counter‑example** and **loss sketch** in the row’s narrative (F.7).                                                                    |
| **AP‑9**  | **CL laundering**          | Citing a high‑scope row based on old high CL while Bridges have since weakened.    | Invalidates downstream claims.                     | When CL falls below τ(scope), **downgrade row scope** (e.g., to Naming‑only) or **split row**.                                                   |
| **AP‑10** | **Global normal form**     | Seeking one canonical wording across all Contexts **as if** meaning were global.      | Erases locality; fuels hidden merges.              | Keep normalisation **per Context** (F.2/F.3). Cross‑context sameness lives in **rows** with scope.                                                     |

---

## 11 · Reasoning primitives (judgement schemas, notation‑free)

> Each item states a **mental entailment**. No storage, no roles, no workflows. Symbols: `C` = Context, `σ` = SenseCell, `R` = Concept‑Set row, `SF` = senseFamily, `τ` = scope threshold, `CL` = congruence level.

1. **senseFamily split**
   `need(n) ∧ mixedSF(n) ⊢ split(n) into {n₁…nₖ} by senseFamily`
   *You cannot decide for mixed senseFamilies; decide per senseFamily.*

2. **Cell reuse**
   `∃ C,σ : expresses(n,SF)@σ ⊢ reuseLabel(σ) in C`
   *If a single Context’s SenseCell already says it, reuse it locally.*

3. **Assignment-eligibility**
   `reuseLabel(σ) ∧ needAssignable(SF ∈ {Role,Status}) ⊢ mintRoleDescription(σ)`
   *When you need assignable behaviour/deontics for a local sense, mint a Role Description anchored to that sense.*

4. **Row reuse**
   `crossContexts(n,SF) ∧ ∃ R: covers(R,SF) ∧ CL(R) ≥ τ(scope) ⊢ reuseRow(R,scope)`
   *For Cross‑context readings, reuse a row at a scope whose τ is met.*

5. **Alias suffices**
   `sameIntent(n,label₀) ∧ stylePreference(n,label₁) ⊢ alias(label₀,label₁)`
   *If it’s only wording, add an Alias; no semantics move.*

6. **Row proposal**
   `recurrentCross(n,SF) ∧ bridgesCL(cells(n)) ≥ τ(scope) ∧ ¬∃R ⊢ proposeRow(cells,scope)`
   *If the need recurs and Bridges support the scope, propose a new row.*

7. **Kernel minting (rare)**
   `kernelCandidate(n) ∧ crossFamily≥3 ∧ irreducible(n) ⊢ proposeUType(n)`
   *Only if the notion is cross‑family and cannot be reduced to cells+rows+existing U.Types.*

8. **Scope downgrade**
   `reuseRow(R,scope) ∧ CL(R)↓ < τ(scope) ⊢ downgradeScope(R)`
   *If CL falls, lower the row’s licensed scope.*

9. **Row rejection**
   `conflictEvidence(rowCells) ∧ lossUnbounded ⊢ rejectRow`
   *If bridges show open‑ended loss, do not publish a row; teach the contrast.*

---

## 12 · Extended worked examples (multi‑architheory)

### 12.1 **Execution, observation, and acceptance** (engineers)

**Need.** A reusable label for “what actually happened and how it was checked against the promise”.
**senseFamilies.** Execution (stance: run); Measurement (KD); Status (accept/reject).

**Contexts.**
`IEC 61131‑3` (task run), `PROV‑O` (Activity), `SOSA/SSN` (Observation), `ITIL 4` (SLO/SLA).

**Reasoning.**

* `Execution`: `IEC` SenseCell (task run) and `PROV` SenseCell (Activity). There exists a **row** *execution-occurrence* at **Assignment-eligibility** with CL = 2 → **reuse row** at **Assignment-eligible** scope; do not infer Type-structure.
* `Measurement`: `SOSA` Observation cell; no Cross‑context needed → **reuse cell**.
* `Status`: `ITIL` SLO/SLA cell; **Role Description** “SLO‑Target” anchored to ITIL cell.

**Outcome.** Prose may say: “This **execution-occurrence** (row\@assignment/enactment-eligibility) was **observed** (SOSA cell) and **evaluated against the SLO** (ITIL cell).” No new U.Type; no hidden merges.

---

### 12.2 **Actor across workflow and provenance** (managers)

**Need.** A single everyday label for “the responsible party” in diagrams.
**senseFamily.** Role (behavioural mask in prose/diagrams).

**Contexts.** `BPMN 2.0` (Participant), `PROV‑O` (Agent).

**Reasoning.** A **Naming‑only** row “actor” exists, CL = 2. **Reuse the row** at Naming‑only.
If assignable behaviour is needed in a model, **mint Role Description** anchored to **BPMN Participant** (not to the row).

**Outcome.** Diagrams show “actor”; formal sections reference `Participant` or `Agent` as appropriate.

---

### 12.3 **Accuracy across metrology and data quality** (researchers)

**Need.** Treat “accuracy” consistently across ISO 80000 (metrology) and ISO/IEC 25024 (data quality).
**senseFamily.** Measurement.

**Contexts.** `ISO 80000‑1` (quantity/units), `ISO/IEC 25024` (data quality).

**Reasoning.** Bridges indicate **related but not identical** definitions; procedures differ. Existing **KD‑metric** row “accuracy” has CL = 2 with **loss note**: *population vs instrument focus*. **Reuse row** at KD‑metric scope for dashboards; **do not** use the row to justify interchange of procedures.

**Outcome.** One label in reports; method sections still cite the context‑local procedure.

---

### 12.4 **Subtype relation across OWL and a curated taxonomy** (formalists)

**Need.** Present “is‑a” uniformly across OWL 2 classes and a domain taxonomy.
**senseFamily.** Type‑structure.

**Contexts.** `OWL 2` (SubClassOf), `Taxonomy_X` (curated “is‑a” edges).

**Reasoning.** F.7 row “subtype‑order” exists at **Type‑structure scope** with CL = 3 (only after verifying acyclicity & anti‑symmetry in `Taxonomy_X`). If the curated taxonomy contains cycles, **downgrade** to Naming‑only or reject the row.

**Outcome.** When CL≥3, you may **reuse row** for structural proofs; else teach differences.

---

## 13 · Relations (with other patterns)

* **Builds on:** E.10.D1 (D.CTX) **Context ≡ U.BoundedContext**; F.1 Contexts; F.2 Harvest; F.3 SenseCells.
* **Constrains:**

  * **F.4 Role Description:** **one SenseCell per Role Description**; no row anchoring.
  * **F.5 Naming:** Aliases are style‑only; no semantics movement.
  * **F.7 Concept‑Set:** rows must declare **Scope** & **Row CL(min)** and carry **loss notes**.
  * **F.9 Bridges:** any row proposal presupposes Bridges at or above τ(scope).
* **Used by.** All architheories (Part C) whenever new labels are contemplated.

---

## 14 · Migration notes (conceptual)

1. **Old “anchor” language.** Replace legacy “anchor” with: **SenseCell** (local sense) + **Role Description** (assignable Standard) + (optionally) **Concept‑Set row** (Cross‑context reading).
2. **Over-strong rows.** If a row was used for **assignment/enactment-eligibility** or **Type-structure** but **CL drops**, **downgrade row scope** to **Naming-only** in prose; adjust examples.
3. **Split rows.** If one row covers cells whose Bridges diverge, **split** into two narrower rows with explicit loss notes.
4. **Alias proliferation.** Collapse redundant Aliases under a single F.5 entry; keep both registers (Tech/Plain).
5. **Proto‑types.** Suspect kernel inflation? Attempt **reduction**: SenseCell + row + existing U.Type. Only if irreducible across ≥ 3 families, reopen as a U.Type candidate.

---

## 15 · Acceptance tests (SCR/RSCR — concept‑level)

### 15.1 Static conformance (SCR)

* **SCR‑F8‑S01 (senseFamily purity).** Every decision record names **one senseFamily**; mixed needs are split.
* **SCR‑F8‑S02 (Proper anchoring).** Every Role Description cites **one SenseCell**; **no row** is used as a assignment/enactment anchor.
* **SCR‑F8‑S03 (Row scope).** Whenever a row is reused, its **Scope** is stated and **Row CL(min) ≥ τ(scope)** holds.
* **SCR‑F8‑S04 (Alias modesty).** Aliases introduced in F.5 do **not** claim new semantics or change senseFamily.
* **SCR‑F8‑S05 (Kernel restraint).** Any new U.Type proposal includes **≥ 3 domain families** of evidence and an **irreducibility** note.

### 15.2 Regression (RSCR)

* **RSCR‑F8‑E01 (CL drift).** If any Bridge’s CL changes, re‑evaluate dependent rows; **downgrade or split** where τ(scope) is no longer met.
* **RSCR-F8-E02 (Row overuse).** Scan examples: no case uses **Naming-only** rows to justify **Assignment-eligibility** or **Type-structure** claims.
* **RSCR‑F8‑E03 (Alias creep).** Ensure no Alias has accreted senseFamily‑specific semantics; if it has, migrate to a **row** or **Role Description**.
* **RSCR‑F8‑E04 (Kernel hygiene).** New U.Type proposals are rejected if a **SenseCell + row** construction suffices.

---

## 16 · Didactic distillation (90‑second teaching script)

> “When you feel like coining a new name, pause. **Which senseFamily** are you in—Role, Status, Measurement, Type‑structure, Method, or Execution? If a **single Context’s SenseCell** already says it, **reuse** that label. If you need an assignable Standard, **mint a Role Description** anchored to that SenseCell. If you must read **across Contexts**, reuse a **Concept‑Set row**—but only **at a stated scope** and only if its **CL meets the threshold** (τ). If it’s just a nicer wording, add an **Alias** (style only). Only in the rare case of a cross‑family, **irreducible** notion do you **mint a new U.Type**. Never let Naming‑only rows justify  **Assignment-eligibility** or structural inference, and never let identical strings force equivalence. This is not process—it’s **discipline of thought**: reuse what exists, declare scope when you bridge, and mint new primitives only when the kernel truly needs them.”


# F.9 — Alignment & Bridge across Contexts \[A] 

**“Translate across Contexts; never collapse them.”**
**Status.** Architectural pattern \[A], architheory‑agnostic.
**Builds on:** E.10.D1 (Context discipline: Context ≡ U.BoundedContext); **F.0.1 (senseFamily & StatusModality guard; Bridge‑only crossing)**; F.1 (Contexts fixed); F.2/F.3 (Cells exist); F.7 (rows depend on Bridges); F.8 (thresholds τ).

**Coordinates with.** B.3 **Trust & Assurance Calculus** (uses CL penalties); **A.6.1 U.Mechanism** (Transport clause for cross‑context use; penalties route to **R/R_eff** only; **F/G** invariant); Part C architheories (apply Bridges in formal claims).
**Aliases (informative).** *Context‑to‑Context translator*; *Sense bridge*.

## 1 · Intent & applicability

**Intent.** Provide a **conceptual discipline** for relating **SenseCells** from **different Contexts (U.BoundedContext)**. A **Bridge** states *what kind* of relationship holds, *how far* it holds (via **CL: Congruence Level**), and *what is lost* during the translation. Bridges **permit carefully scoped reuse** (e.g., a Concept‑Set row) while **forbidding silent equivalence**.

**Applicability.** Use **whenever** an author needs to **read across Contexts**—to reuse a familiar label, to connect design‑time and run‑time notions, to compare two standards’ terms, or to justify a row in the Concept‑Set table. This pattern is **not** storage, workflow, or governance; it codifies **thinking moves**.

**Non‑goals.** No global meaning; no tool/API; no editor roles. Bridges are **semantic relations between local senses**, not pipelines, not processes.

---

## 2 · Problem frame

Cross‑context work fails in predictable ways:

1. **String‑equals fallacy.** Identical surfaces (“process”, “role”, “accuracy”) taken as identical meaning.
2. **Scope creep.** A naming convenience is stretched to assignment or structural claims.
3. **DesignRunTag jumping.** Design artefacts are substituted for run‑time occurrences (or vice‑versa).
4. **Direction amnesia.** Narrower/broader relations treated as symmetric.
5. **Loss blindness.** Differences (units, granularity, preconditions) are left unstated, contaminating downstream reasoning.

Bridges cure these by **making relation, direction, loss, and strength explicit**.

---

## 3 · Forces

| Force                           | Tension to resolve                                                                       |
| ------------------------------- | ---------------------------------------------------------------------------------------- |
| **Locality vs reuse**           | Senses are context‑local, yet people need a common label to talk across Contexts.              |
| **Simplicity vs fidelity**      | Few Bridge kinds are teachable; too few will hide real mismatches.                       |
| **Safety vs utility**           | Allow some substitution when safe; forbid it when loss is unbounded.                     |
| **senseFamily purity vs explanation** | Substitution must preserve **senseFamily**; explanation may span **senseFamilies** without implying sameness. |

---

## 4 · Core idea (didactic)

**A Bridge is a declared translator between two local senses.**
It always names **(a)** the two **SenseCells**, **(b)** a **Bridge‑kind** (what relation), **(c)** a **direction** (if non‑symmetric), **(d)** a **CL** (how strong), and **(e)** **Loss Notes** (what fails to carry). Some Bridges **permit substitution** in limited scopes; others **permit only explanation**.

---

## 5 · Minimal vocabulary (this pattern only)

* **Context** — shorthand for **U.BoundedContext** (per E.10.D1).
* **SenseCell** — the pair *(Context × Local‑Sense)* from F.3.
* **Bridge** — a conceptual relation between two SenseCells with kind, direction, CL, and loss notes.
* **CL (Congruence Level)** — ordinal strength (0…3) of a Bridge (see §7).
* **Scope** — the **licensed use** of a Cross‑context reading (as in F.7/F.8):

* **Naming‑only** (talk consistently),
* **Role Assignment & Enactment-eligibility** (assignable constraints/roles/status reuse),
* **Type‑structure** (safe structural inference).
* **senseFamily** — the semantic category (Role, Status, Measurement, Type‑structure, Method, Execution…) per F.0.1 (normative Part F guard).

---

## 6 · Bridge kinds (senseFamily‑aware)

> **Two families** of Bridges: **Substitution Bridges** (senseFamily‑preserving; can support Concept‑Set rows) and **Interpretation Bridges** (explanatory; **not** for substitution).

### 6.1 Substitution Bridges (sense‑preserving)

These relate **SenseCells of the same senseFamily** and may license **limited substitution**:

1. **Equivalence (≈)** — *near‑identity of sense*. Symmetric. Rare.
   *Use:* May support **Type‑structure** rows when CL=3 and invariants match.
   *Loss Notes:* usually “none” or “profiling differences”.

2. **Narrower‑than (⊑)** / **Broader‑than (⊒)** — *proper inclusion of sense*. Directional.
  *Use:* Safe to substitute **narrower → broader** in **Naming-only** and sometimes **Role Assignment & Enactment**; **broader → narrower** is unsafe.
   *Loss Notes:* “loses special cases X”.

3. **Partial‑overlap (⋂)** — *non‑empty intersection, neither includes the other*.
  *Use:* **Naming-only** at best. **Never** justifies Role Assignment & Enactment / Type-structure.
   *Loss Notes:* “A-only senseFamily”, “B-only senseFamily”.

4. **Disjoint (⊥)** — *explicit contrast*.
   *Use:* For **didactic warnings**; not a reuse license.
   *Loss Notes:* n/a (it asserts incompatibility).

### 6.2 Interpretation Bridges (cross‑senseFamily, explanatory)

These **do not allow substitution** but **explain connections** across senseFamilies:

5. **Design‑spec ↔ Run‑trace (⇄ᴅʀ)** — a design concept relates to its run‑time occurrence.
   *Example:* *BPMN\:Process* ⇄ᴅʀ *PROV\:Activity*.
   *Use:* Explain pipelines (design → execution → provenance). No Concept‑Set rows.
   *Loss Notes:* “graph vs event”, “control‑flow vs temporal extent”.

6. **Measure‑of / Evidence‑for (→ᴍᴇᵃ)** — a measurement SenseCell evidences or quantifies another **senseFamily** (e.g., a Requirement clause).
   *Example:* *SOSA\:Observation* →ᴍᴇᵃ *ITIL\:SLO fulfilment*.
   *Use:* Explain evaluation. No substitution.

7. **Policy‑implies / Obliges (→ᴅᵉᵒ)** — a deontic statement constrains another **senseFamily**.
   *Example:* *ODRL\:Duty* →ᴅᵉᵒ *Service behaviour*.
   *Use:* Explain constraint propagation.

> **Rule of thumb.** If you want **rows** or **substitution**, you need a **Substitution Bridge** on the **same senseFamily**. If you want to **explain** why artefacts relate without claiming sameness, use **Interpretation Bridges**.

---

## 7 · CL scale and scope thresholds

CL expresses how safely meaning carries over.

| CL    | Name              | Intuition                                            | Typical loss         | Row scope allowed (τ thresholds) |
| ----- | ----------------- | ---------------------------------------------------- | -------------------- | -------------------------------- |
| **0** | **Opposed**       | Intentionally contrastive or disjoint                | n/a                  | none                             |
| **1** | **Comparable**    | Talk under a shared label; senses differ materially  | material sense divergence | **Naming‑only** (τₙₐₘₑ=1)        |
| **2** | **Translatable**  | Bounded loss; consistent examples & counter-examples | small, stated losses | **Role Assignment & Enactment-eligibility** (τRAE=2)     |
| **3** | **Near‑identity** | Invariants match; no material counter‑example        | profile‑level only   | **Type‑structure** (τᵗʏᴘᴇ=3)     |

* **Thresholds (normative):**

  * Publishing a **Naming‑only** row requires **CL ≥ 1** across the row’s Cells.
 * Publishing a **Role Assignment & Enactment-eligible** row requires **CL ≥ 2** and **same senseFamily**, and **compatible stance**..
  * Publishing a **Type‑structure** row requires **CL = 3** **and** matched invariants (acyclicity, anti‑symmetry, units, etc.).

* **Penalty use (informative):** B.3 may convert **CL** into an assurance **penalty** when a Cross‑context claim is made.

---

## 8 · The Bridge Card (one‑screen sketch)

> A **thought‑format** (not a form). Every bullet can be said in a sentence.

* **Cells.** `σA@contextA` ↔ `σB@contextB`.
* **senseFamily.** *Role / Status / Measurement / Type‑structure / Method / Execution …*
* **Kind.** *≈ / ⊑ / ⊒ / ⋂ / ⊥ / ⇄ᴅʀ / →ᴍᴇᵃ / →ᴅᵉᵒ*.
* **Direction.** *A→B* (if non‑symmetric) or *A↔B*.
* **CL.** *0–3* with a short **why**.
* **Loss Notes (bullets).** What fails to carry (units, scope, granularity, preconditions, time stance).
* **Counter‑example.** The crispest case where substitution would mislead.
* **Allowed use.** *Naming-only / Role Assignment & Enactment-eligible / Type-structure / Explanation-only*.
* **Didactic hook.** The helpful sentence a careful engineer can remember.

*If your Bridge Card doesn’t fit on a screen, you’re describing the Contexts, not the Bridge.*

---

## 9 · Invariants (normative)

1. **Locality first.** A Bridge relates **SenseCells**, never Contexts or strings.
2. **senseFamily discipline.** **Substitution Bridges must be senseFamily‑preserving**. **Interpretation Bridges** may cross senseFamilies but **never** license substitution.
3. **Direction clarity.** If the kind is non‑symmetric (⊑/⊒), **state direction** explicitly.
4. **CL honesty.** Assign **CL** only if you can state at least one **counter‑example** (CL≤2) or explain its absence (CL=3).
5. **Loss visibility.** Every Bridge carries **Loss Notes** (even “none”).
6. **Row dependence.** A Concept‑Set row’s **scope** is **bounded by the weakest CL** among its participating Bridges (F.7/F.8).
7. **No senseFamily jump by stealth.** You **must not** use an Interpretation Bridge to justify a **row** or **substitution**.
8. **Time DesignRunTag honesty.** If a Context fixes **design/run**, the Bridge must respect or explicitly declare stance relations (e.g., ⇄ᴅʀ).
9. **Kernel restraint.** Bridges **cannot** be used to promote ad‑hoc sameness into a new **U.Type**; A.11 applies.
10. **Non‑inheritance of Contexts.** Bridges **do not** imply “is‑a” between Contexts (E.10.D1).

---

## 10 · Micro‑examples (illustrative, one‑liners)

1. **Participant vs Agent (workflow vs provenance)**
   *Cells:* `BPMN:Participant` ↔ `PROV:Agent` • *senseFamily:* Role • *Kind:* ⋂ (overlap) • *CL:* 2 • *Loss:* participation vs attribution scopes differ • *Use:* **Naming‑only** (“actor”).

2. **Process (design) vs Activity (run)**
   *Cells:* `BPMN:Process` ⇄ᴅʀ `PROV:Activity` • *senseFamily:* Method ↔ Execution • *Kind:* **Design‑spec ↔ Run‑trace** • *CL:* 2 • *Loss:* graph vs event; concurrency vs temporalization • *Use:* **Explanation‑only**.

3. **Observation vs SLO check**
   *Cells:* `SOSA:Observation` →ᴍᴇᵃ `ITIL:SLO‑fulfilment` • *senseFamily:* Measurement → Status • *Kind:* Measure‑of • *CL:* 2 • *Loss:* sampling window; target definition • *Use:* **Explanation‑only**.

4. **Subtype across OWL and curated taxonomy**
   *Cells:* `OWL:SubClassOf` ≈ `TaxonomyX:is‑a` • *senseFamily:* Type‑structure • *Kind:* ≈ • *CL:* 3 *(only if TaxonomyX is acyclic & anti‑symmetric)* • *Loss:* profile differences • *Use:* **Type‑structure** rows allowed.

5. **Accuracy (metrology vs data‑quality)**
   *Cells:* `ISO80000:accuracy` ⋂ `ISO25024:accuracy` • *senseFamily:* Measurement • *Kind:* overlap • *CL:* 2 • *Loss:* instrument vs dataset perspective • *Use:* **Naming‑only** row “accuracy”; methods stay context‑local.

## 11 · Anti‑patterns & remedies

| ID        | Anti‑pattern                     | Symptom                                                                           | Why it breaks thinking                              | Remedy (conceptual move)                                                                                    |
| --------- | -------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **AP‑1**  | **String‑equals ≡ sense‑equals** | Same surface used across Contexts with silent identity claims.                       | Violates locality; invites false substitution.      | Always state a **Bridge kind**; if unsure, default to **⋂ overlap** with **Naming‑only** scope.             |
| **AP-2**  | **Stealth substitution**         | “We’ll just treat A like B for now.”                                              | Hidden policy with unknown loss; leaks into Role Assignment & Enactment.    | Publish a **Bridge Card** with **Loss Notes** and **CL**; if CL<2, substitution remains **forbidden**.      |
| **AP‑3**  | **Stance jump by wording**        | “Activity (PROV) is a Process (BPMN).”                                            | Design ↔ run confusion; swaps graphs for events.    | Use **⇄ᴅʀ design↔run Interpretation Bridge**, **not** ≈/⊑; keep **Explanation‑only** scope.                 |
| **AP‑4**  | **Symmetry hallucination**       | Treating ⊑/⊒ as if they were symmetric.                                           | Narrows broadened, broadens narrowed; unsafe reuse. | Record **direction** explicitly; only **≈** is symmetric.                                                   |
| **AP-5**  | **Disjoint but reused**          | Declare ⊥ then still borrow labels or Role Description constraints (RCS/RSG).     | Contradiction between declaration and use.          | Either retract ⊥ or stop reuse; if a thin thread exists, rename as **contrastive explanation** (no row).    |
| **AP‑6**  | **CL without counter‑example**   | “These are CL=3” with no invariant check.                                         | Inflates trust; permits structural rows wrongly.    | For **CL=3**, cite the **matching invariants**; otherwise, demote to **CL=2** and add counter‑example.      |
| **AP‑7**  | **Bridge inflation**             | Dozens of nearly identical Bridges between the same Contexts.                        | Noise masks the few material alignments.            | Prefer **one Bridge per pair of Cells per senseFamily**; fold variants into **Loss Notes**.                       |
| **AP-8**  | **Row outruns Bridge**           | Concept-Set row claims Role Assignment & Enactment-eligibility where some participating Bridges are CL=1. | Row scope exceeds weakest link.                     | Apply **weakest-link rule** (F.7/F.8): row scope ≤ **min(CL)**; otherwise split the row.                    |
| **AP‑9**  | **Bridge as new U.Type**         | Using a Bridge to justify minting a new universal Type.                           | Re‑globalises meaning; breaks A.11 parsimony.       | Keep Types context‑local; where reuse is needed, use **rows** + Bridges, not new primitives.                   |
| **AP‑10** | **Silent unit/scale mismatch**   | Mapping measurements without unit/scale notes.                                    | Hidden dimensional error.                           | Record units/scales in **Loss Notes**; if units can’t be related, the kind is **⊥** or **⋂ (Naming‑only)**. |

---

## 12 · Worked cross‑architheory examples (didactic)

### 12.1 Service acceptance (design) vs executions & observations (run)

* **Cells & Contexts**
  `ITIL4:SLO` *(Status, design)* ← **→ᴍᴇᵃ** — `SOSA:Observation(availability)` *(Measurement, run)*
  `BPMN:Process` *(Method, design)* ⇄ᴅʀ — `IEC61131:Task‑Execution` *(Execution, run)*
* **Narrative**
  Availability SLOs are **evaluated** by observations of task executions. No substitution: SLO ≠ observation; process ≠ execution.
* **Bridge Cards (sketch)**
  *ITIL\:SLO ←→ᴍᴇᵃ SOSA\:Observation* • **CL=2** • Loss: sampling window, clock skew.
  *BPMN\:Process ⇄ᴅʀ IEC\:Execution* • **CL=2** • Loss: control‑flow vs temporalization, concurrency collapse.
* **Permitted use**
  Explanation‑only; Concept‑Set rows may be **Naming‑only** (“availability”) with **CL≥1** label coherence across Contexts.

---

### 12.2 Behavioural role vs access role

* **Cells & Contexts**
  `BPMN:Participant` *(Role)* ⋂ `NIST‑RBAC:Role` *(Status)*
* **Narrative**
  Both talk about “who acts”, but one is **behavioural mask** in a workflow, the other **permission grouping**.
* **Bridge**
  **Kind:** overlap (⋂), **CL=2**; Loss: assignment moment, enforcement locus, multiplicity.
* **Permitted use**
* **Naming-only** row “actor”; **no Role Assignment & Enactment reuse** across senseFamilies.

---

### 12.3 Equivalence of subtype notions for structural rows

* **Cells & Contexts**
  `OWL2:SubClassOf` *(Type‑structure)* ≈ `TaxX:is‑a` *(Type‑structure curated)*
* **Bridge**
  **Kind:** ≈, **CL=3** **iff** curated taxonomy is **acyclic & anti‑symmetric** and uses class‑level reasoning.
* **Permitted use**
  **Type‑structure** rows allowed (τᵗʏᴘᴇ); Loss: OWL profile limitations (RL/EL/QO).

---

### 12.4 Accuracy (metrology) vs accuracy (data‑quality)

* **Cells & Contexts**
  `ISO80000:measurement‑accuracy` *(Measurement)* ⋂ `ISO25024:data‑accuracy` *(Measurement)*
* **Bridge**
  **Kind:** overlap, **CL=2**; Loss: “true value” notion differs (instrument vs dataset), scale transformations.
* **Permitted use**
  **Naming‑only** row “accuracy” used for reports; no shared methods.

---

### 12.5 Setpoint (control) vs target (service)

* **Cells & Contexts**
  `CTRL:text:setpoint` *(Status/Control)* ⊥ `ITIL:target` *(Status/Service)*
* **Bridge**
  **Kind:** disjoint (⊥) • Rationale: physical reference value vs business objective; different target kinds (control parameters vs requirement clause).
* **Permitted use**
  Didactic contrast only; prevents accidental substitution in SLO calculus.

---

## 13 · Reasoning primitives (judgement schemas)

> **All judgements are conceptual.** They license or forbid specific *thinking moves*—not API calls, not workflows.

### 13.1 Bridge declaration

`⊢ Bridge(σA@RA, σB@RB) : ⟨senseFamily, kind, dir, CL, Loss, scope⟩`

*Reading:* There exists a declared Bridge between SenseCells `σA` and `σB` with stated attributes.

---

### 13.2 Substitution licence (senseFamily‑preserving)

`Bridge(σA,σB): ⟨senseFamily f, kind∈{≈,⊑,⊒}, dir A→B, CL≥2, Loss L⟩ ⊢ A↠B @f (Role Assignment & Enactment-eligible)`

*Reading:* A **Substitution Bridge** on the same senseFamily with **CL≥2** licenses **Role-Assignment/Enactment-level** substitution **in the stated direction**. (Type-structure requires **CL=3**.)

---

### 13.3 Naming‑only licence

`Bridge(σA,σB): ⟨kind∈{≈,⊑,⊒,⋂}, CL≥1⟩ ⊢ A⇝B (Naming‑only)`

*Reading:* A Bridge with **CL≥1** supports using a shared label in prose or Concept-Set **Naming-only** rows, without structural or Role Assignment & Enactment commitments.

---

### 13.4 Prohibition by kind

`Bridge(σA,σB): ⟨kind=⊥⟩ ⊢ ¬(A↠B) ∧ ¬(row(A,B))`

*Reading:* **Disjoint** forbids substitution and rows; only contrastive teaching is allowed.

---

### 13.5 Interpretation embargo

`Bridge(σA,σB): ⟨kind∈{⇄ᴅʀ,→ᴍᴇᵃ,→ᴅᵉᵒ}⟩ ⊢ Explanation‑only`

*Reading:* **Interpretation Bridges** never license substitution or rows.

---

### 13.6 Weakest‑link rule for rows

`row R uses {Bridge_i} ⊢ scope(R) = min_i(scopeAllowed(Bridge_i)) ∧ CL(R)=min_i(CL_i)`

*Reading:* The **row scope** and **row CL** are bounded by the weakest participating Bridge.

---

### 13.7 Direction guard

`Bridge kind=⊑ with dir A→B ⊢ ¬(B↠A)`

*Reading:* Narrower→Broader does **not** invert; only A may substitute into B under the stated scope.

---

### 13.8 SenseFamily purity

`Bridge scope=Role Assignment & Enactment-eligible ⊢ senseFamily(A)=senseFamily(B) ∧ stance(A)=stance(B)`

*Reading:* Role Assignment & Enactment-level substitution requires **same senseFamily** and same stance (run-time or design time).

---

### 13.9 Loss accumulation

`A↠B with Loss L₁ ∧ B↠C with Loss L₂ ⊢ A↠C allowed only if same senseFamily ∧ CL=min(CL₁,CL₂) ∧ Loss ⊇ (L₁∪L₂)`

*Reading:* Chained substitution is rarer; if used, **accumulate Loss** and respect the **minimum CL**. When in doubt, avoid chaining across Contexts.

---

## 14 · Relations

**Builds on:** E.10.D1 (Context discipline: Context ≡ U.BoundedContext); **F.0.1 (senseFamily guard; Bridge‑only crossing)**; F.1 (Contexts fixed); F.2/F.3 (Cells exist); F.7 (rows depend on Bridges); F.8 (thresholds τ).

**Constrains:**

* **F.7 Concept‑Set Table:** each Cross‑context row must name supporting **Bridges**; row scope ≤ weakest Bridge.
* **F.8 Mint or Reuse?:** reuse choices reference **CL** and **kind**; no reuse without a Bridge.
* **Part C architheories:** formal claims that span Contexts cite Bridges and respect senseFamily/StatusModality & CL constraints.
* **B.3 Trust & Assurance Calculus:** may interpret **CL** as a penalty factor in Cross‑context reasoning.

---

## 15 · Migration notes (conceptual)

1. **Edition shift in a Context.** Re‑read affected **Cells**; if sense moved, split the Bridge or **lower CL**; keep the older Bridge for historical claims.
2. **New evidence of mismatch.** Add a **counter‑example**; **decrease CL** or change **kind** (e.g., from ≈ to ⊑ or ⋂).
3. **Convergence over time.** When invariants demonstrably match, and counter‑examples evaporate, **raise CL** cautiously; for **CL=3**, cite invariants.
4. **senseFamily refactor.** If a Cell’s senseFamily was mis‑typed, fix the senseFamily first in F.3, then revisit Bridges; **Interpretation** is safer than forced substitution.
5. **Row under‑protected.** If a row’s scope exceeds the weakest Bridge, either **split the row** by Context or **downgrade scope** to Naming‑only.
6. **Bridge sprawl.** Consolidate near‑duplicates into one Bridge with richer **Loss Notes**; retire the rest.

---

## 16 · Acceptance tests (SCR/RSCR — concept‑level)

### 16.1 Static conformance (SCR)

* **SCR‑F9‑S01 (Well‑typed).** Every Bridge names **two SenseCells**, each bound to a **Context** from F.1, and states **senseFamily**, **kind**, **dir** (if needed), **CL**, **Loss**, **scope**.
* **SCR‑F9‑S02 (senseFamily discipline).** Any Bridge that licenses **Role/Enactment-eligible** substitution is **senseFamily‑preserving** and **kind ∈ {≈,⊑,⊒}**.
* **SCR‑F9‑S03 (Loss visibility).** Every Bridge has **non‑empty Loss Notes** (the word “none” is allowed only with **CL=3** and stated invariants).
* **SCR‑F9‑S04 (Counter‑example hygiene).** Bridges with **CL≤2** carry at least one **counter‑example**; Bridges with **CL=3** cite **matching invariants**.
* **SCR‑F9‑S05 (Row compliance).** Every Concept‑Set row shows a **scope** no greater than the **minimum CL** across its supporting Bridges; no row relies on **Interpretation** Bridges.

### 16.2 Regression (RSCR)

* **RSCR‑F9‑E01 (Edition churn).** When a Context’s edition changes, re‑validate all Bridges touching it; **flag CL drift** and update rows’ scopes if needed.
* **RSCR‑F9‑E02 (Counter‑example drift).** New counter‑examples lower **CL**; deletions do not automatically raise **CL**.
* **RSCR‑F9‑E03 (senseFamily drift).** If a Cell’s senseFamily is corrected, all Bridges crossing that Cell are re‑typed; any substitution that would now cross senseFamilies is **invalidated**.
* **RSCR‑F9‑E04 (Weakest‑link enforcement).** Adding a low‑CL Bridge to a row **reduces** the row’s scope; if the row’s published scope would exceed the new minimum, **split** or **downgrade** the row.

---

## 17 · Didactic distillation (90‑second script)

> “A **Bridge** translates between **local senses** from different **Contexts**. It always declares **what relation** (≈, ⊑, ⋂, ⊥, or an **interpretation** like design↔run), **how strong** (CL 0–3), **which way** (for ⊑/⊒), and **what is lost**. **Substitution** is allowed only on the **same senseFamily** and only with **CL≥2**; **Type‑structure** needs **CL=3**. **Interpretation Bridges** explain, never substitute. Rows in the Concept‑Set table obey the **weakest‑link**: their scope cannot exceed the lowest CL among their Bridges. When editions change or counter‑examples surface, **lower CL** or change **kind**; if two senses truly converge and invariants match, raise to **CL=3**—rarely, and with reasons. Translate across Contexts; never collapse them.”

# F.10 — Status Families Mapping (Evidence • Standard • Requirement) \[A] 

**“Keep statuses in their native modality; translate between Contexts explicitly.”**
**Status.** Architectural pattern \[A], architheory‑agnostic.
**Builds on:** E.10.D1 **D.CTX** (Context ≡ `U.BoundedContext`); F.1 (Contexts), F.2 (Seeds), F.3 (Local‑Senses → SenseCells), F.4 (Role Description **Status** templates), F.9 (Bridges).
**Coordinates with.** B.3 **Trust & Assurance Calculus** (interprets CL penalties); Part C architheories: **KD‑CAL** (measurement semantics), **Norm‑CAL** (deontic logic), **Method‑CAL** (DesignRunTag).

---

## 1 · Intent & applicability

**Intent.** Provide a **simple, Context‑first way** to express and compare **status meanings** across disciplines **without collapsing modalities** (*epistemic* vs *deontic*). We focus on three pervasive **status families**:

1. **EvidenceStatus** (what the world **shows**) — epistemic modality.
2. **StandardStatus** (what a canon **sanctions**) — deontic (curatorial) modality.
3. **RequirementStatus** (what an obligation is **doing**) — deontic (compliance) modality.

Each status meaning is **local to a Context** (`U.BoundedContext`). Cross‑context relationships appear **only** via **Bridges** (F.9) with a declared **kind** and **CL** (congruence level).

**Applicability.** Whenever models mix observations, standards, and obligations: service acceptance from uptime measurements; safety proofs against normative checklists; ML model “validated” vs “approved for use”.

**Non‑goals.** No workflows, no tool states, no editorial lifecycles. This pattern defines **conceptual meaning and safe reasoning moves**, not procedures.

---

## 2 · Problem frame

Without a modality‑aware mapping of statuses:

* **Homonym traps.** *Validated* in metrology ≠ *validated* in software QA; *approved* in a standard ≠ *compliant* to a requirement.
* **Design/run bleed.** Design‑time “approved method” is used as if it proved run‑time “meets SLO”.
* **False substitution.** *Observed availability 99.95%* is silently treated as *SLO satisfied* without declaring the translation.
* **Name inflation.** New U.Types minted to stabilise drifting status words instead of fixing Contexts and Bridges.

---

## 3 · Forces

| Force                                     | Tension to resolve                                                                             |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Local fidelity vs Cross‑context reuse**    | Keep native Context meanings, yet enable explanation and (sometimes) substitution.                |
| **Didactic simplicity vs status variety** | Many status schemes exist; we need a **small spine** that admits Context synonyms.                |
| **Design vs run**                         | Standards speak design; evidence speaks run; requirements span both; do not swap them.         |
| **Safety vs utility**                     | Substitution is powerful but risky; explanation is safer but weaker. Make the choice explicit. |

---

## 4 · Core idea (didactic)

**Three families, two modalities, one habit.**
Treat every status word as a **SenseCell with a declared StatusModality** and **inside one Context**. When you must relate statuses across Contexts, **declare a Bridge** (F.9) that says *what kind of relation*, *how strong (CL)*, *which way (if narrower/broader)*, and *what is lost*. Prefer **explanation** Bridges; permit **substitution** only when kind/CL allow it.

**Reading an Episteme.** For every `U.Episteme`, read _Object_ (what it is about), _Concept_ (model/postulates), _Symbol_ (carriers). **Statuses classify the Episteme;** enactment remains with `U.System` and `U.Work`. (Formal identity rules: see **KD‑CAL**.)

## 5 · Minimal vocabulary (this pattern only)

* **StatusFamily.** Sub‑typing inside **senseFamily=Status**: one of **EvidenceStatus**, **StandardStatus**, **RequirementStatus**.
* **StatusCell.** A **SenseCell** whose meaning is a status with a declared **StatusModality ∈ {epistemic, deontic}**
* **StatusModality.** The mode of a StatusCell: **epistemic** or **deontic**. Use this term instead of the bare word *modality* per E.10 LEX rules.
* **Polarity.** The orientation of a status relative to a claim/obligation: **Positive** (supports/satisfies), **Negative** (contradicts/violates), **Neutral/Undetermined**.
* **Window.** The **applicability span** of a status (temporal or conditional), e.g., “Q3‑2025”, “under load ≥ 70%”.
* **Target.** What the status is **about**: a **claim** (epistemic), an **artefact or method** (standard), a **clause** (requirement).
* **Bridge (F.9).** The only legal way to relate StatusCells across Contexts; declares **kind** (≈, ⊑, ⊒, ⋂, ⊥, or an Interpretation arrow), **CL**, and **Loss**; **substitution is modality‑preserving**.

> **StatusModality guard.** EvidenceStatus is **epistemic**; StandardStatus & RequirementStatus are **deontic**. **Role Description Status** templates (F.4) bind to these **StatusModalities**; **no mixing**. The bare token *modality* is against E.10/LEX); this pattern uses **StatusModality**.

---

## 6 · The spine: three local ladders (Context‑native, small and renameable)

> The following ladders are **didactic spines**. Each Context may rename levels or insert thin sub‑levels, but Bridges must state how they align to this spine (kind & CL). Names appear in **Tech** / **Plain** register.

 -   **Episteme‑as‑actor (forbidden).** Never attribute **Work** to an Episteme; only Systems act.
    
-   **Requirement vs Hypothesis.** “Desired property/goal” is **not** `Requirement` status; use hypothesis/target + evaluation.
    
-   **Mereology ≠ Provenance.** Part‑whole edges never justify claims; use EPV‑DAG with carriers.


### 6.1 EvidenceStatus (epistemic statusModality)

**Levels (from weaker to stronger):**

1. **Observed** / *Seen once.*
2. **Measured** / *Quantified under a declared procedure.*
3. **Corroborated** / *Seen independently (≥ 2 distinct sources/procedures).*
4. **Replicated** / *Repeated by others under varied conditions.*
5. **Refuted** *(negative polarity)* / *Counter‑evidence overrides prior levels.*
6. **Inconclusive** *(neutral)* / *Insufficient signal.*

**Context alignment examples (illustrative):**
`SOSA/SSN:Observation` ↦ **Observed/Measured**; `GxP validation datapack` may map to **Replicated** (if protocol diversity holds) with **CL stated**.

**Invariants (context‑local):**
*Replicated ⇒ Corroborated ⇒ Measured ⇒ Observed.* Negative (**Refuted**) cancels positives **within the same Window**.

---

### 6.2 StandardStatus (deontic/curatorial statusModality)

**Levels (design‑time stance):**

1. **Candidate** / *Proposed, under review.*
2. **Draft** / *Working text, not normative.*
3. **Approved** / *Normative in this Context/edition.*
4. **Deprecated** *(negative)* / *Discouraged; may be removed.*
5. **Superseded** *(negative)* / *Replaced by a newer edition/profile.*

**Context alignment examples:**
`ISO profile: Published International Standard` ↦ **Approved**; `IETF RFC (Proposed Standard)` ↦ **Draft/Approved** depending on local policy; **CL must be declared** on the Bridge.

**Invariants:**
At most one positive stance at a time **per Context & edition**; **Superseded** implies **Approved** held in a prior Window.

---

### 6.3 RequirementStatus (deontic/compliance statusModality)

**Levels (run‑aware stance toward an obligation):**

1. **Applicable** / *The clause binds in this Window.*
2. **Inapplicable** / *Clause does not bind under stated conditions.*
3. **Satisfied** *(positive)* / *Met within Window.*
4. **Violated** *(negative)* / *Not met within Window.*
5. **Waived** *(neutral/administrative)* / *Binding suspended with justification.*
6. **Pending** *(neutral)* / *Awaiting evaluation or evidence.*

**Context alignment examples:**
`ITIL4:SLO achieved` ↦ **Satisfied**; `ODRL:Duty fulfilled` ↦ **Satisfied**; `ODRL:Prohibition breached` ↦ **Violated**.

**Invariants:**
For the **same clause and Window**, **Satisfied** and **Violated** are **mutually exclusive**. **Applicable** is a **precondition** for either; **Waived** switches off the precondition temporarily.

### 6.4 Contextual Citation Operators (pointer)

**Citation operators (context‑scoped).** Authors MAY use the **typed edges** `supports`, `refutes`, `dependsOn`, `supersedes` **inside a single Context** when expressing how an `Evidence`/`Standard` status applies. **Formal semantics live in B.3.2 (Evidence & Validation Logic).** Cross‑Context use requires a declared **Bridge** (F.9) and carries CL/Loss penalties.


## 7 · Solution — how meanings connect (conceptual, notation‑free)

**S‑1. Anchor status meanings per Context.**
Every status word (*validated*, *approved*, *compliant*) is treated as a **StatusCell** inside a specific Context. The **ladder position** is determined **locally** (e.g., “validated (metrology)” aligns to **Replicated** with CL stated; “validated (software)” may align to **Corroborated**).

**S‑2. Attach statuses to the right Targets.**
*EvidenceStatus → Claim or Quantity; StandardStatus → Method/Artefact; RequirementStatus → Clause.*
This prevents swapping “how we measure” with “what we promise”.

**S‑3. Translate via Bridges, not by name.**
Example: **Measured availability (SOSA)** →ᴍᴇᵃ **SLO clause (ITIL)** with **CL=2**, Loss: sampling window & clock skew. This supports **explanation**; **substitution** (“Satisfied”) requires **same StatusModality**, a stricter Bridge kind (F.9) **and** a declared evaluation rule (from the Service pattern), not from F.10.

**S‑4. Keep design/run honest.**
**StandardStatus** is design‑stance; **EvidenceStatus** is run‑signal; **RequirementStatus** spans both. Use **Interpretation Bridges** (F.9) for design↔run readings, not equivalence.

**S‑5. Prefer explanation over substitution.**
If a Bridge cannot reach **CL≥2** on the **same senseFamily**, do **not** substitute. Use **Naming‑only** rows or **explanations**; keep Role Descriptions (F.4) out of harm’s way.

---

## 8 · Invariants (normative, lightweight)

1. **Modality purity.** A StatusCell’s **StatusModality** is explicit and **must not change** during reasoning; cross‑modality claims require an **Interpretation Bridge** (F.9).
2. **Target typing.** A status **must name its Target kind** (claim / artefact / clause). Inferences that ignore the Target kind are invalid.
3. **Window discipline.** Every positive/negative status **names a Window**; contradictions are detected **within the same Window** only.
4. **Local monotonicity.** Within one context, **stronger** EvidenceStatus implies all **weaker** positives for the same Target & Window.
5. **Mutual exclusivity (requirement).** For a given clause & Window: **not** (Satisfied ∧ Violated).
6. **No free promotion.** **StandardStatus** (Approved) **does not** entail **RequirementStatus** (Applicable or Satisfied).
7. **Bridge gate.** Any Cross‑context comparison or reuse of a status **must cite a Bridge** (kind, CL, Loss); otherwise only **context‑local** reading is permitted.
8. **Weakest‑link propagation.** When multiple Bridges contribute to a Cross‑context interpretation, the **effective CL** is the **minimum** (cf. F.7/F.9).
9. **Naming restraint.** Status labels used across Contexts **without** a Bridge are **Naming-only** and **non-operative** for Role Assignment & Enactment decisions.

## 9 · Micro‑illustrations (snapshots, not procedures)

* **Metrology → Service.**
  *Observed uptime (SOSA)* with Window “July” plus Bridge **→ᴍᴇᵃ** to *SLO clause (ITIL)* yields: **we can explain** why “Satisfied” might hold **if** the Service pattern’s evaluation rule says so. F.10 itself **does not** declare “Satisfied”.

* **QA vs GxP “validation”.**
  *Validated (software QA Context)* aligns to **Corroborated** (CL=1–2).
  *Validated (GxP Context)* aligns to **Replicated** (CL=2–3) with Loss: environment diversity.
  Equating them needs **≈** with **CL stated** or they remain separate.

* **“Approved model” ≠ “Compliant outcome”.**
  **StandardStatus: Approved** for a **MethodDescription** does **not** imply **RequirementStatus: Satisfied** for a production clause. It only permits use; evidence must still speak.

## 10 · Anti‑patterns & remedies

| #         | Anti‑pattern                                 | Symptom                                                                        | Why it harms reasoning                                                               | Remedy (conceptual move)                                                                                                                                                                                                                       |
| --------- | -------------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **AP‑1**  | **“Validated ⇒ Approved ⇒ Compliant” chain** | A single word *validated* is treated as proving approval and compliance.       | Collapses **statusModalities** (epistemic → deontic); ignores Targets & Windows.               | Keep **EvidenceStatus** about **claims**, **StandardStatus** about **artefacts/methods**, **RequirementStatus** about **clauses**. Use **two Bridges** (evidence→requirement via interpretation + standard→requirement via policy), never one. |
| **AP‑2**  | **Run‑time proves design‑time**              | A month of logs is cited as “therefore the method is approved.”                | Directional fallacy; design‑time approval is curatorial, not measured.               | Separate **design vs run**. Evidence may justify a **proposal** Bridge to *Approved* only in Contexts where such promotion exists; otherwise keep **explanation‑only**.                                                                           |
| **AP‑3**  | **“Approved model” ⇒ “SLO satisfied”**       | Governance stamp is cast as automatic service compliance.                      | **StandardStatus** does not entail **RequirementStatus**; the latter needs evidence. | Require **EvidenceStatus** on the clause’s **Window**, then apply the **evaluation rule** (Service pattern).                                                                                                                                   |
| **AP‑4**  | **Synonym drift of status labels**           | *Verified/validated/approved* used interchangeably across Contexts.               | Homonymy across Contexts; weakens claims.                                               | Treat each status word as a **StatusCell** tied to its Context; relate only via **Bridge(kind, CL, Loss)**.                                                                                                                                       |
| **AP‑5**  | **No Window**                                | Status claimed without time/condition (“Compliant.”).                          | Unfalsifiable; blocks conflict detection.                                            | Every positive/negative status **names a Window**; contradictions checked per Window.                                                                                                                                                          |
| **AP‑6**  | **Double truth**                             | *Satisfied* and *Violated* asserted for same clause silently.                  | Violates mutual exclusivity; hides differing Windows.                                | Force **Window discipline**; if Windows coincide, at least one assertion must retract.                                                                                                                                                         |
| **AP‑7**  | **Substitute by name**                       | “SOSA Observation = ITIL SLO check”.                                           | Cross‑context equality without Loss accounting.                                         | Prefer **explanation Bridges**; allow **substitution** only when **same statusModality**, **kind ∈ {≈,⊑,⊒}**, **CL≥project threshold**, **Windows aligned**.                                                                                            |
| **AP‑8**  | **Evidence escalation without diversity**    | One lab repeats itself and calls it “replicated”.                              | Confuses **repetition** with **independent replication**.                            | In EvidenceStatus, **Replicated** demands **independent** settings/sources; else keep at **Corroborated**.                                                                                                                                     |
| **AP‑9**  | **Clause‑less compliance**                   | “Compliant” with no clause named.                                              | Target missing; cannot evaluate.                                                     | Every RequirementStatus **points to a clause** (Target).                                                                                                                                                                                       |
| **AP‑10** | **Negative erased by summary**               | A later summary lists *Satisfied* but omits earlier *Violated* in same Window. | Cherry‑picks; breaks auditability.                                                   | Apply **Weakest‑link**: within a Window, **negative outranks** prior positives for the same clause.                                                                                                                                            |
| **AP‑11** | **Bridge‑free roll‑up**                      | Cross‑context dashboards aggregate statuses as if native.                         | Hidden Cross‑context semantics; CL unknown.                                             | Each Cross‑context line **must cite Bridges**; roll‑up shows the **effective CL (min)**.                                                                                                                                                          |
| **AP‑12** | **Status explosion**                         | New bespoke statuses minted to match every tool state.                         | Pollutes lexicon; blurs statusModalities.                                                      | Map tool states to the **nearest ladder level** in the local context; keep tool terms as **Naming‑only** where needed.                                                                                                                            |

## 11 · Worked examples (multi‑architheory)

> Each example names **Contexts**, shows **StatusCells** on their native ladders, and draws **only the Bridges that F.10 allows**.

### 11.1 Service acceptance from run‑time evidence

**Contexts.** *SOSA/SSN (2017)* — sensing; *ITIL 4 (2020)* — services; *ODRL 2.2* — deontics (optional).

**Local statuses.**

* `SOSA:Observation(uptime)` → **EvidenceStatus: Measured**, Window **July**.
* `ITIL:SLO("99.9% monthly")` → **RequirementStatus** Target = clause *SLO‑99.9*, Window **July**.
* `ITIL:Practice("Monitoring pipeline")` → **StandardStatus: Approved** (design‑time).

**Bridges.**

* **Interpretation**: `Measured(uptime@July)` **→ᴍᴇᵃ** `SLO‑99.9` (kind = ⊑, CL = 2, Loss: sampling bias, clock skew).
* **Evaluation rule** (Service pattern, local to ITIL Context): returns **Satisfied** iff *mean uptime ≥ threshold* across Window.

**Result.** We may **explain** the **Satisfied** conclusion for *SLO‑99.9\@July*; we **do not** assert StandardStatus⇒RequirementStatus. If logs later show outages, a **Violated\@July** replaces **Satisfied\@July** (mutual exclusivity + Window discipline).

---

### 11.2 Safety controller: design approval vs run‑time duty

**Contexts.** *State‑space control texts* — design; *IEC 61131‑3* — run; *Norm‑CAL profile (safety layer)* — deontics.

**Local statuses.**

* `ControllerSpec(v3)` — **StandardStatus: Approved** in the **Norm‑CAL** Context.
* `PLC:Task(log@Q3)` — **EvidenceStatus: Corroborated** for *response time ≤ 50 ms*, Window **Q3**.
* `Duty("Emergency stop ≤ 100 ms")` — **RequirementStatus** clause in Norm‑CAL.

**Bridges.**

* **Interpretation**: `Corroborated(response@Q3)` **→** `Duty` check (kind = ⊑, CL = 2, Loss: sensor latency).

**Result.** The **duty** may be **Satisfied\@Q3** with explanation. *Approved spec* **alone** never yields *Satisfied*; it authorises deployment but does not prove compliance.

---

### 11.3 ML model: validation vs fairness requirement

**Contexts.** *ML validation canon* — design/run hybrid; *Policy Context (fairness charter)* — deontics; *SOSA/metrics* — sensing.

**Local statuses.**

* `Model v12: cross‑val AUC=0.92` → **EvidenceStatus: Corroborated** (Windows: CV folds).
* `Policy: “Demographic parity Δ ≤ 0.1”` → **RequirementStatus** clause.
* `“Validation SOP v5”` → **StandardStatus: Approved** (governance method).

**Bridges.**

* `Measured(Δ@Aug)` **→ᴍᴇᵃ** `Policy clause` (⊑, CL = 2, Loss: sampling variance).

**Result.** **Satisfied\@Aug** (if Δ≤ 0.1 in production Window) is justifiable. Cross‑val AUC does **not** decide fairness; only **production Δ** does.

---

### 11.4 Medical device log: refutation

**Contexts.** *SOSA/clinical observations*; *Regulatory profile*.

**Local statuses.**

* `Observation: adverse event` → **EvidenceStatus: Observed\@Week 34**.
* `Requirement: “No AE in first 30 days”` → **RequirementStatus** clause.

**Bridge & outcome.**

* Observation **→ Interpretation Bridge** to clause check (**kind: Interpretation**, **CL=3**).
* **Violated\@Week 34** overrides any earlier **Satisfied\@Week 34** (Weakest‑link; same Window).

---

## 12 · Reasoning primitives (judgement schemas, notation‑free)

> **Premises ⊢ conclusion.** No side effects. All moves are **mental** and **Context‑aware**.

1. **StatusModality classification**
   `σ is a StatusCell ⊢ statusModality(σ) ∈ {epistemic, deontic}`
   *Reading:* Every status sits on exactly one statusModality.

2. **Target typing**
   `σ ⊢ targetKind(σ) ∈ {claim, artefact/method, clause}`
   *Reading:* Evidence→claim; Standard→artefact/method; Requirement→clause.

3. **Window requirement**
   `σ has polarity ∈ {positive, negative} ⊢ window(σ) ≠ ∅`
   *Reading:* Pos/neg statuses must name a Window.

4. **Local ladder monotonicity (evidence)**
   `Replicated(τ,W) ⊢ Corroborated(τ,W) ⊢ Measured(τ,W) ⊢ Observed(τ,W)`
   *Reading:* Stronger implies weaker within the same Window.

5. **Requirement exclusivity**
   `clause κ, window W ⊢ ¬(Satisfied(κ,W) ∧ Violated(κ,W))`
   *Reading:* A clause cannot be both satisfied and violated in one Window.

6. **Windowed refutation**
   `Refuted(τ,W) ⊢ cancels {Observed,Measured,Corroborated,Replicated}(τ,W)`
   *Reading:* Negative evidence cancels positives only in the same Window.

7. **Explanation Bridge**
   `σ@C, τ@D, Bridge(C,D, kind∈{≈,⊑,⊒,⋂}, CL, Loss), sameStatusModality ⊢ explains(σ ⇒ τ) with ⟨CL,Loss⟩`
   *Reading:* Cross‑context explanation is permitted when statusModalities match.

8. **Substitution permission (guarded)**
   `explains(σ ⇒ τ) ∧ kind∈{≈,⊑,⊒} ∧ CL≥θ ∧ windowsAligned ⊢ maySubstitute(σ→τ)`
   *Reading:* Substitution is allowed only above a **project‑declared threshold θ** (see F.7) and aligned Windows.

9. **Cross‑statusModality embargo**
   `statusModality(σ) ≠ statusModality(τ) ⊢ explains(σ ⇒ τ) requires Interpretation kind`
   *Reading:* Crossing statusModalities is **interpretation** only; no direct substitution.

10. **Observation→Requirement clause (SOSA, Work outcomes)**
   `SOSA:Observation about Work outcomes ⊢ may interpret(RequirementClause κ) via Bridge(kind=Interpretation, CL, Loss); produces Evaluation(κ, Window); substitution forbidden`
   *Reading:* Observations inform clause evaluation within a Window; they never become RequirementStatus. Use F.12 for the verdict pipeline.

11. **Weakest‑link CL**
   `{explains(σᵢ ⇒ τ) with CLᵢ} ⊢ effectiveCL(⋀ᵢ σᵢ ⇒ τ) = minᵢ(CLᵢ)`
   *Reading:* Multiple Bridges compose by the minimum CL.

12. **Naming‑only safeguard**
   `noBridge(C,D) ⊢ crossContextUse(σ@C ⇒ τ@D) = namingOnly`
   *Reading:* Without a Bridge, only **explanatory prose** is allowed—no status inferences.

13. **DesignRunTag honesty**
   `statusModality=deontic ∧ targetKind=artefact/method ∧ window=W ⊢ doesNotDecide(clause κ @ W)`
   *Reading:* Approval of a method never decides a clause’s satisfaction for a run‑time Window.

## 13 · Relations

**Builds on:**
E.10.D1 **D.CTX** (Context discipline); F.1 (Contexts in view); F.2–F.3 (Seeds→Local‑Senses→SenseCells); F.4 (Role Description **Status** template with statusModality/target/window slots); F.7 (Bridge taxonomy & CL semantics); F.9 (Bridge artefact).

**Constrains:**

* **F.4 (Role Description Status):** a Role Description Status **must** select a **StatusFamily**, **StatusModality**, **target kind**, and **Window**.
* **F.8 (Naming):** status labels reused across Contexts **must** be marked as **Context‑scoped**; global synonyms forbidden.
* **Part C architheories:** KD‑CAL provides measurement semantics for EvidenceStatus; Norm‑CAL provides clause logic for RequirementStatus; Method‑CAL frames DesignRunTag for StandardStatus.

**Used by.**
Service Acceptance (F.12), Assurance roll‑ups (B.3), any cross‑domain conformance narrative.

---

## 14 · Migration notes (conceptual)

1. **New status word appears.** Treat it as a **StatusCell** in its Context; place it on the local ladder; only then consider Bridges.
2. **Edition changes.** If a Context redefines a status, **fork the StatusCell** (new SenseCell) and relate old↔new via a **Bridge** (often ⊑/⊒ with Loss).
3. **Threshold tuning.** The project sets **θ** (minimum CL for substitution). Lowering θ widens reuse but increases risk; document the choice in F.7 terms.
4. **Clause redesign.** If a requirement clause changes, keep old **Windows** intact; new clause starts a new Target; do **not** rewrite history.
5. **Explode→compress.** When many bespoke tool statuses pile up, **map** them to the nearest ladder level in their Contexts; keep tool labels as **Naming‑only**.
6. **Bridge hardening.** If explanation Bridges are used frequently, reconsider experiments that could raise **CL** enough to permit substitution—or accept explanation as sufficient and stop short of substitution.

---

## 15 · Acceptance tests (SCR/RSCR — concept‑level)

### 15.1 Static conformance (SCR)

* **SCR‑F10‑S01 (Modality & Target).** Every StatusCell declares **StatusModality** and **target kind**; none cross modalities.
* **SCR‑F10‑S02 (Windowed polarity).** Every positive/negative StatusCell instance bears a **Window**.
* **SCR‑F10‑S03 (Local order).** EvidenceStatus instances satisfy **monotonicity**; RequirementStatus enforces **mutual exclusivity** per clause+Window.
* **SCR‑F10‑S04 (Bridge citation).** Any Cross‑context comparison cites a **Bridge(kind, CL, Loss)**; absent that, mark as **naming‑only**.
* **SCR‑F10‑S05 (Substitution guard).** Any substitution claim checks **same StatusModality**, **kind ∈ {≈,⊑,⊒}**, **CL≥θ**, **Windows aligned**.
* **SCR‑F10‑S06 (Weakest‑link).** Where multiple Bridges feed one conclusion, the displayed **effective CL** is the **minimum**.

### 15.2 Regression (RSCR)

* **RSCR‑F10‑E01 (Edition churn).** Adding a new edition of a Context **does not** retro‑change past status conclusions; only new Windows see new meanings.
* **RSCR‑F10‑E02 (Threshold change).** If θ changes, re‑evaluate only **substitution** conclusions; **explanations** remain valid.
* **RSCR‑F10‑E03 (Bridge drift).** When a Bridge’s CL/Loss changes, recompute affected **effective CL**; substitution conclusions below θ revert to **explanation**.
* **RSCR‑F10‑E04 (Contradiction catch).** Adding a negative status within a Window **cancels** prior positives for the same clause (or raises a flagged contradiction if both persist).

---

## 16 · Didactic distillation (90‑second script)

> **Three families, two modalities.** *Evidence* tells us what the world **shows** (Observed→Measured→Corroborated→Replicated; Refuted cancels) — **epistemic**; *Standard* tells us what a canon **sanctions** (Candidate→Draft→Approved→Deprecated→Superseded) — **deontic**; *Requirement* tells us what an obligation is **doing** (Applicable/Inapplicable; Satisfied/Violated; Waived/Pending) — **deontic**.
> Every status is a **StatusCell inside one Context** with exactly one **StatusModality**, a **Target**, and a **Window**.
> When you must relate status meanings across Contexts, **draw a Bridge** that states the **kind** (≈, ⊑/⊒, ⋂, ⊥ or Interpretation), the **CL** (strength), and the **Loss** (what you ignore). Prefer **explanation**; allow **substitution** only when statusModalities match, kind permits, **CL≥θ**, and Windows align.
> Keep **design vs run** stance honest: approval is **design‑time**, evidence is **run‑time**, requirements **span both**. With this habit, “validated”, “approved” and “compliant” stop being a muddle of synonyms and become **precise, local meanings** you can compare **safely** and **audibly**.


# F.11 — Method Quartet Harmonisation \[A] 

**“Keep the *how* (Method), the *recipe* (MethodDescription), the *happening* (Work/Execution), and the *control push* (Actuation) in their own Contexts—then relate them explicitly.”**

**Status.** Architectural pattern \[A], architheory‑agnostic.
**Builds on:** E.10.D1 **D.CTX** (Context discipline); A.3/**A.3.1**/**A.3.2** (Transformer Constitution; `U.Method`, `U.MethodDescription`); A.15/**A.15.1** (`U.Work` as record of occurrence); Sys‑CAL (control/actuation semantics); KD‑CAL (observation).
**Coordinates with.** F.1–F.3 (Contexts, Seeds → SenseCells), F.4 (Role Description), F.5 (Naming), F.6 (Role Assignment & Enactment Cycle (Six-Step)), F.7/F.9 (Bridges), F.10 (Status families & Windows).
**Aliases (informative).** *Method/Spec/Work/Actuation split*; *design/run harmonisation*.

---

## 1 · Intent & applicability

**Intent.** Provide a **notation‑free, Context‑aware map** that keeps four notions distinct and connectable:

* **`U.Method`** — the abstract **way of doing** (design‑time concept).
* **`U.MethodDescription`** — the **recipe** that describes a Method (epistemic artefact).
* **`U.Work`** (informal: *Execution*) — the **run‑time occurrence** of doing (recorded event).
* **`U.Actuation`** — the **control output** applied to a plant (domain‑specific Work in Sys‑CAL).

The pattern makes the split **usable across architheories** (Role Assignment & Enactment, Sys-CAL, KD-CAL, Kind-CAL, planned LCA-CAL) and **legible across Contexts** (SPEM/BPMN for design; PROV-O/SOSA for run; IEC 61131-3/state-space for control).

**Applicability.** Any time a discussion risks **mixing designs with executions**, **recipes with runs**, or **workflow with control signals**; whenever you need to **name** or **reason** about “how we do X”, “the SOP/script/model”, “the actual run”, or “the actuator push”.

**Non‑goals.** No team workflow, no editors, no tools. No prescriptive file formats. **Only** conceptual distinctions and safe reasoning moves.

---

## 2 · Problem frame

When Method, MethodDescription, Work, and Actuation **collapse into one another**, models drift:

1. **Design/run blur.** A BPMN *process* (design graph) is cited as if it had *happened*.
2. **Recipe/approval fallacy.** An *approved* SOP (MethodDescription) is treated as proof that the service met its SLO.
3. **Execution ≟ control.** PLC *task execution* logs are conflated with *control outputs* (actuation), hiding stability issues.
4. **Cross‑context homonymy.** *Activity, task, execution, process, command* change sense across Contexts; inferences quietly break.

---

## 3 · Forces

| Force                        | Tension to resolve                                                                                             |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Fidelity vs didactics**    | We must honour domain nuance yet teach a split that fits in working memory.                                    |
| **Universality vs locality** | Quartet must be reusable across architheories, while meanings stay **context‑local**.                             |
| **Evidence vs approval**     | Evidence (run‑time) should support decisions, but must **not** be mistaken for deontic approval (design‑time). |
| **Action vs signal**         | Executing a method is not the same as emitting a control signal; both can co‑occur in one scenario.            |

---

## 4 · Core idea (didactic)

**Four boxes, four arrows, zero leakage.**

* **Box 1 — Method (design).** The **idea** of how to achieve an effect (algorithm, clinical pathway, welding technique).
* **Box 2 — MethodDescription (design, epistemic).** The **written/encoded recipe** that *describes* a Method (SOP, code, BPMN/SPEM model, theorem‑prover script).
* **Box 3 — Work (run).** The **occurrence** where a System‑in‑Role enacts (some version of) the Method. *`U.Work` is the record of this event.*
* **Box 4 — Actuation (run, Sys‑CAL).** The **control output** (setpoint/command) issued to influence a plant during Work.

**Arrows (conceptual relations).**

* `MethodDescription ↦ Method` (**describes**) — design stance.
* `Work ↦ MethodDescription` (**followedRecipe?** yes/no/variant) — run stance referencing design.
* `Work ↦ Method` (**enacts**) — run stance referencing the abstract way.
* `Actuation ↦ Work` (**part‑of / occurs‑during**) — control output inside execution.

Each box/arrow is **context‑local** (SPEM, PROV‑O, IEC…). **Cross‑context relations use Bridges** (F.7/F.9) with CL/Loss.

---

## 5 · Minimal vocabulary (this pattern only)

* **Context** = `U.BoundedContext` (per D.CTX).
* **Local‑Sense** → **SenseCell** (F.3): the address *(Context × sense)* for a term like *process*, *task*, *activity*, *command*.
* **Concept‑Set** (F.7/F.8): row aligning multiple SenseCells as “what we regard as the same” (after Bridges & losses are declared).
* **Window** (F.10): temporal/conditional envelope (e.g., *July*, *during test run T42*, *under load ≥ 70%*).
* **StatusCell** (F.10): laddered status **about** methods/specs/works (e.g., *Approved (spec)*; *Observed/Measured (work)*).

---

## 6 · Solution — the quartet lens (notation‑free)

> *Not steps for a team—**lenses for a thinker**. Use them to sanity‑check any statement about “how”, “script”, “run”, or “signal”.*

### 6.1 The **stance split** (design vs run)

* If the claim is about **what should be done** or **how it is described**, you are on the **design stance** (Method/MethodDescription).
* If the claim is about **what happened** or **what was emitted**, you are on the **run stance** (Work/Actuation).
* **Guard rule.** Never let a conclusion cross stances without (a) an explicit Bridge kind (*interpretation* vs *substitution*), and (b) an acceptable CL (F.7/F.9, F.10).

### 6.2 The **recipe/idea split**

* **Method** is the **idea**; **MethodDescription** is the **recipe** describing that idea.
* Different recipes may describe the **same** method (profiles, languages, levels of detail); one recipe may encode **several** methods (composite SOP).
* **Naming guard.** Keep labels distinct: *compressive‑strength test* (Method) vs *ASTM C39‑18* (MethodDescription).

### 6.3 The **happening** (Work) with **signal** (Actuation)

* **Work** is the **occurrence** (a PROV *Activity*, an IEC *Task* executing a program, a lab run).
* **Actuation** is the **control output** (setpoint, PWM command, valve open %) emitted **during** Work.
* You can have Work **without** Actuation (analysis job), or Actuation **without** a complex Method (manual push). Many scenarios have **both**.

### 6.4 The **Role Assignment & Enactment touch-points**

* **Roles** (F.4) bind **who enacts** the Method at run‑time (behavioural masks), **not** what permissions they hold (RBAC is a different Context).
* **Statuses** (F.10) bind to the right box: *Approved* → MethodDescription; *Measured/Observed* → Work; *Satisfied/Violated* → Requirement clause about the Work’s outcomes within a **Window**.

---

## 7 · Harmonisation map (Context‑first)

> Examples of **local SenseCells** and **safe Bridges**. *You may keep the exact Contexts from your F.1 cut.*

**Design (ideas & recipes).**

* *SPEM/ISO 24744 Context*: `SenseCell{Method}` = *Activity Definition / Task Definition*; `SenseCell{MethodDescription}` = *Process Description / WorkProduct* (as recipe).
* *BPMN 2.0 Context*: `SenseCell{MethodDescription}` = *Process (diagram)* as **design‑time** recipe (do not confuse with run).
* *OWL/Kind-CAL Context*: labels for Method kinds (type taxonomies) when needed (naming, not behaviour).

**Run (occurrences & outputs).**

* *PROV‑O Context*: `SenseCell{Work}` = *Activity* (time‑bounded occurrence).
* *SOSA/SSN Context*: Observations **about** Work results (feeds EvidenceStatus).
* *IEC 61131‑3 Context*: `SenseCell{Work}` = *Task executes Program* (runtime); `SenseCell{Actuation}` = *Output command / setpoint* emitted by the program.

**Typical Bridges (with intent).**

* `BPMN:Process (design)` **≈** `SPEM:Process Definition` (design↔design; CL depends on modelling profile; Loss: expressiveness gaps).
* `IEC:Task execution` **⊑** `PROV:Activity` (run↔run; Loss: control‑specific timing semantics, scan cycles).
* `Actuation (IEC)` **⋂** `Activity (PROV)` (intersection: the *sub‑intervals* where outputs are emitted).
* `SOSA:Observation` **interprets** `Requirement clause` (F.10) about **Work outcomes** (**cross‑StatusModality: epistemic→deontic; never substitution**; declare **Bridge(kind=Interpretation, CL, Loss)**).

---

## 8 · Invariants (normative)

1. **DesignRunTag honesty.** Statements about **Method/MethodDescription** (design) **MUST NOT** be used as if they were statements about **Work/Actuation** (run) without an explicit Bridge and Window.
2. **Box discipline.** Every claim about “how”, “recipe”, “run”, or “control output” **MUST** point to the correct box in the quartet.
3. **Context locality.** Terms (*process*, *activity*, *task*, *command*) **MUST** be read as **SenseCells** in their Contexts (F.3); Cross‑context equivalence is a matter for F.7/F.9 Bridges.
4. **Status placement.** *Approved* attaches to MethodDescription; *Observed/Measured* attach to Work; *Satisfied/Violated* attach to clauses about Work outcomes within a **Window** (F.10).
5. **Actuation as Work‑part.** Actuation **MUST** be modelled as **occurring within** (or as a specialised form of) Work on the run stance; it does **not** replace Work.
6. **Naming clarity.** Technical/Plain labels for the quartet **SHOULD** be distinct (F.5); avoid homonymous single‑word labels when Contexts collide.
7. **Bridge guard.** Cross‑context moves **MUST** declare **kind** (≈, ⊑, ⊒, ⋂, ⊥, Interpretation), **CL**, and **Loss** (F.7/F.9).

---

## 9 · Micro‑examples (didactic, cross‑architheory)

1. **Data pipeline deploy (software).**
   *Method*: “Delta‑load transform”. *MethodDescription*: `etl_delta.py@v3`. *Work*: nightly run 2025‑07‑14. *Actuation*: none.
   *Statuses*: Spec **Approved** (governance Context); Work **Measured** (rows processed) → Evidence for SLO (F.10).

2. **Valve control (industrial).**
   *Method*: PID tuning heuristic. *MethodDescription*: SOP sheet + IEC program. *Work*: PLC task cycle 18:00–18:30. *Actuation*: PWM duty sequence.
   *Bridge*: `IEC:Task` ⊑ `PROV:Activity` (CL=2). Observed setpoint tracking **interprets** requirement “settling time ≤ 5 s”.

3. **Clinical assay (lab).**
   *Method*: ELISA. *MethodDescription*: Kit IFU v7. *Work*: run batch #B217. *Actuation*: pipetting robot commands.
   *Statuses*: Spec **Approved** ≠ batch **Satisfied** (requires evidence at batch Window).

## 10 · Anti‑patterns & remedies

| #       | Anti‑pattern                   | Symptom in prose/models                                               | Why it harms thinking                                                       | Remedy (conceptual move)                                                                                                                                                                                             |
| ------- | ------------------------------ | --------------------------------------------------------------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **A1**  | **Design→Run Substitution**    | “The process **achieved** X” while pointing to a design diagram.      | Treats a **MethodDescription** as if it were **Work**; collapses stances.           | Apply the **stance split**: restate as “The **diagram describes** how X **should** be achieved.” To claim it **happened**, reference a **Work** SenseCell in a run‑time Context and, if needed, add a **Window** (F.10). |
| **A2**  | **Approval = Evidence**        | “Approved SOP ⇒ requirement satisfied.”                               | A **StatusCell** about a **MethodDescription** does not entail a run‑time outcome. | Keep **Approved** on Spec; place **Satisfied/Violated** on clauses **about Work** within a **Window**; require Observation/Evidence (KD‑CAL) for the run side.                                                       |
| **A3**  | **Execution = Actuation**      | PLC log of setpoints recorded as the whole execution history.         | Loses non‑signal aspects (delays, conditions, context); weakens reasoning.  | Model **Actuation** as **within** **Work**. Keep both SenseCells: *Task execution* (Work) and *Command/Setpoint* (Actuation).                                                                                        |
| **A4**  | **BPMN‑as‑Run**                | BPMN *Process* treated as “the thing that ran.”                       | BPMN’s meaning is context‑local and design‑time.                               | Use a **Bridge** (F.7/F.9) from *BPMN\:Process (design)* → *PROV\:Activity (run)* with kind **Interpretation**, CL/Loss declared.                                                                                    |
| **A5**  | **Spec Drift Retroactivity**   | Update to a recipe is assumed to modify past executions.              | Violates temporal honesty; breaks auditability.                             | Past **Work** remains as‑was. New **MethodDescription** versions describe future **Work** only; record variant relations if a run deviated.                                                                                 |
| **A6**  | **Homonym Collapse**           | *Task*, *activity*, *process* used interchangeably across Contexts.      | Imports meaning implicitly; masks losses.                                   | Prefix with **Context** and use **SenseCells**: e.g., *task (IEC)*, *activity (PROV)*, *process (BPMN)*. Any relation uses **Bridges** with CL/Loss.                                                                    |
| **A7**  | **Signal‑Only Compliance**     | SLO judged solely from actuator traces.                               | Ignores measured outcomes; risks false positives.                           | Tie **SLO** clauses to **Observations** (KD‑CAL) **about Work outcomes**; treat Actuation as an input, not proof.                                                                                                    |
| **A8**  | **Recipe-as-Role**             | “The Spec assigns responsibility” (mixes MethodDescription with Role constructs — `U.RoleDescription`/`U.RoleAssignment`).  | Conflates epistemic artefact with behavioural masks.                        | Use **F.4 Role Description; let **MethodDescription** only **describe** a Method.                                                                              |
| **A9**  | **One‑Context Scope**        | A single Context (e.g., BPMN) used as if it covered control/measurement. | Scope mirage; silent cross‑domain generalisation.                           | Re‑cut Contexts (F.1) to include control and sensing. Re‑express statements with the quartet across those Contexts.                                                                                                        |
| **A10** | **Lossless Bridge Assumption** | Claiming “equivalent” across Contexts without Loss.                      | Hides mismatches; unsafe transfer of inferences.                            | In **F.7/F.9** declare Bridge **kind**, **CL**, and explicit **Loss** notes.                                                                                                                                         |
| **A11** | **Recipe‑as‑Type**             | Treating a MethodDescription vocabulary as a type taxonomy.                  | Category error; misuses Kind-CAL.                                           | If a stable hierarchy of **kinds** of Methods is needed, mint **U.Type** nodes in Kind-CAL; keep MethodDescription as *description* only.                                                                                   |
| **A12** | **Actuation Outside Work**     | Commands modeled without enclosing Work.                              | Severs signal from enactment context; breaks traceability.                  | Embed **Actuation** **within** **Work** intervals; relate to the enacting Role and Method/MethodDescription references.                                                                                                     |

---

## 11 · Worked examples (extended, multi‑architheory)

> Each scenario names Contexts (from your F.1 cut), identifies the quartet boxes, and shows safe Cross‑context moves.

### 11.1 ML service rollout (software + services + sensing)

* **Contexts:** *SPEM/ISO 24744* (design), *PROV‑O* (run), *SOSA/SSN* (sensing), *ITIL 4* (services).
* **Quartet:**

  * **Method:** *Canary deployment strategy*.
  * **MethodDescription:** *Canary plan document with traffic slices and rollback rules* (design Context).
  * **Work:** *Two canary runs 2025‑08‑02 10:00–12:00* (PROV‑Activities).
  * **Actuation:** *Traffic‑shifting commands* (if modeled, they are outputs inside Work; optional in pure software).
* **Statuses (F.10):** *Spec Approved*; *Work Observed* (latency/err‑rate via SOSA Observations); *SLO clause Satisfied* in Window if measured ≤ thresholds.
* **Bridge(s):** *BPMN (if used) Process (design)* → *PROV Activity (run)* **Interpretation**, CL=2, **Loss:** path vs time granularity.

**Pay‑off:** No one infers SLO satisfaction from a plan. Evidence is about **Work**; the plan stays design‑time.

---

### 11.2 Industrial furnace control (control + sensing + services)

* **Contexts:** *State‑space control texts* (design), *IEC 61131‑3* (run), *PROV‑O* (run), *SOSA/SSN* (sensing), *ITIL 4* (services).
* **Quartet:**

  * **Method:** *PID with feed‑forward*.
  * **MethodDescription:** *Controller tuning sheet + program description*.
  * **Work:** *PLC task cycles 14:00–14:30* (IEC *Task executes Program*), **Bridged** as **PROV Activity**.
  * **Actuation:** *Setpoint & valve duty cycle outputs* emitted during Work.
* **Statuses:** *Spec Approved*; *Work Observed* (temperature curve); requirement *settling time ≤ 5 s* **Satisfied** if the observation within Window meets it.
* **Bridge(s):** `IEC:Task` ⊑ `PROV:Activity` (CL=2, **Loss:** scan‑cycle semantics). `SOSA:Observation` **interprets** requirement clause (CL=3).

**Pay‑off:** Separates **doing** from **pushing**, and both from **measuring**; compliance judged where it belongs.

---

### 11.3 Clinical assay

* **Contexts:** *SPEM/ISO 24744* (design), *Lab assay canon* (design/run split as per discipline), *PROV‑O* (run), *SOSA/SSN* (sensing).
* **Quartet:**

  * **Method:** *ELISA*.
  * **MethodDescription:** *Kit IFU v7 (instructions for use)*.
  * **Work:** *Batch B217 performed 2025‑06‑21* (PROV Activity).
  * **Actuation:** *Pipetting robot commands* (optional detail).
* **Statuses:** *Spec Approved*; *Work Observed* (absorbance readings); *Quality gate Satisfied* within batch Window.
* **Bridge(s):** IFU (design) **interprets** Activity (run) for acceptance (CL=2, **Loss:** deviations allowed per kit tolerances).

**Pay‑off:** A clean line from recipe → run → measurement → decision, without role/status conflation.

---

### 11.4 Incident response (services + enactment)

* **Contexts:** *ITIL 4* (services/design), *BPMN 2.0* (design), *PROV‑O* (run).
* **Quartet:**

  * **Method:** *Triage‑first incident handling*.
  * **MethodDescription:** *Incident workflow diagram + playbook*.
  * **Work:** *Handling INC‑3421, 09:10–10:02* (PROV Activity).
  * **Actuation:** none (unless modeling command invocations as outputs).
* **Statuses:** *Spec Approved*; *Work Observed* (timestamps, response time); *SLO “MTTR ≤ 60 min”* **Satisfied** within the incident Window.
* **Bridge(s):** BPMN (design) → PROV (run) **Interpretation**, CL=2, **Loss:** gateways vs real‑time branching.

**Pay‑off:** MTTR claims are tied to **Work**, not to the playbook.

---

## 12 · Reasoning primitives (judgement schemas)

> Pure **mental moves**; no storage or workflow is implied.

1. **Box classifier**
   `statement s, Contexts fixed ⊢ box(s) ∈ {Method, MethodDescription, Work, Actuation}`
   *Reading:* Classify any claim by its **box** (design idea, design recipe, run occurrence, control output).

2. **Stance firewall**
   `box(s) ∈ {Method,MethodDescription} ⊢ s ∉ {claims about Work outcomes}`
   *Reading:* A design‑time (stance) statement does **not** assert a run‑time (stance) outcome.

3. **Followed‑recipe judgement**
   `Work w, MethodDescription m ⊢ follows(w,m) ∈ {exact, variant, none}`
   *Reading:* A Work may follow a recipe **exactly**, with a **variant**, or **not at all**; later inferences must respect this value.

4. **Enactment link**
   `Work w, Method h ⊢ enacts(w,h)`
   *Reading:* The occurrence enacts the abstract Method (even if several specs describe it).

5. **Actuation inclusion**
   `Actuation a, Work w ⊢ occursWithin(a,w)`
   *Reading:* Control outputs are **within** (or are parts of) a Work interval.

6. **Observation binding** (KD‑CAL handshake)
   `Observation o about outcome(x) during Window W of Work w ⊢ evidenceFor(w, clause(x,W))`
   *Reading:* Measurements about a Work outcome within a Window serve as evidence for clauses **about that Work**.

7. **Clause evaluation** (F.10 handshake)
   `evidenceFor(w,clause) ⊢ status(clause,w) ∈ {Satisfied, Violated, Inconclusive}`
   *Reading:* A clause about Work yields a status via the observation set.

8. **Context locality**
   `term t, Context C ⊢ meaning(t)@C is local`
   *Reading:* A term’s sense is **local** to its Context; Cross‑context claims require Bridges.

9. **Bridge application** (F.7/F.9)
   `Bridge B: (X@A) ~kind,CL,Loss~ (Y@B); fact about X ⊢ transferableTo(Y) with penalty(CL,Loss)`
   *Reading:* Facts may transfer across Contexts only along a declared Bridge, with the stated penalty.

10. **Version non‑retroactivity**
    `MethodDescription m updated → m' ⊢ ∀ past Work w: follows(w,m')=none (unless w references m')`
    *Reading:* New recipes don’t rewrite history.

11. **Composite reasoning**
    `MethodDescription m = m1 ; m2, Work w executes steps w1,w2 ⊢ enacts(w1,m1) ∧ enacts(w2,m2)`
    *Reading:* Composition on design does not force composition on run, but when it aligns you may relate sub‑runs to sub‑methods.

12. **SLO locus guard**
    `SLO clause about service outcome ⊢ attachesTo(Work-window), not MethodDescription`
    *Reading:* Service obligations concern **what happened** within a Window, not the existence of a plan.

---

## 13 · Relations

**Builds on:**
E.10.D1 **D.CTX** (Context ≡ `U.BoundedContext`); A.3/**A.3.1**/**A.3.2**/**A.15** (Method/Spec/Work foundations); Sys‑CAL (Actuation semantics); KD‑CAL (Observation); F.1–F.3 (Contexts → SenseCells); F.10 (Status families & Windows).

**Constrains:**

* **F.4 Role Description:** Roles/Statuses **must** point to the right box (e.g., *Approved* → MethodDescription; *Observed* → Work).
* **F.5 Naming:** Enforce distinct Tech/Plain labels for Method/Spec/Work/Actuation where homonyms threaten.
* **F.7/F.9 Bridges:** All Cross‑context assertions among quartet terms **must** go through explicit Bridges with **kind/CL/Loss**.

**Used by.**
Part C architheories (Sys‑CAL, KD‑CAL, Method‑CAL, Kind-CAL, LCA‑CAL) when describing examples, proofs, and cross‑disciplinary mappings.

---

## 14 · Migration notes (conceptual)

1. **Split conflated “process”.** Where a single “process” node stands for both plan and run, refactor into **MethodDescription** (design) and **Work** (run); add a Bridge if the prose relied on identity.
2. **Re‑home statuses.** Move any *Approval*‑like statuses from Work to MethodDescription; move *Satisfied/Violated* from Spec to clauses about Work within **Windows**.
3. **Expose actuation.** If control outputs are buried in “execution logs,” mint **Actuation** SenseCells and relate them **within** Work.
4. **Version fences.** Past Works keep references to the **version** of MethodDescription they attempted to follow; don’t update those links retroactively.
5. **Name collisions.** Where *task/activity/process* appear with mixed meanings, prefix with Contexts and relabel per **F.5** (Tech/Plain).
6. **Backfill Bridges.** If earlier text implied Cross‑context equivalence, add explicit Bridges (F.7/F.9) declaring **kind/CL/Loss**.

---

## 15 · Acceptance tests (SCR/RSCR — concept level)

### 15.1 Static conformance checks (SCR)

* **SCR‑F11‑S01 (DesignRunTag honesty).** Every normative claim about outcomes is attached to **Work** (with Window), not to **Method/MethodDescription**.
* **SCR‑F11‑S02 (Box placement).** Labels and statuses appear on the correct box (e.g., *Approved* on MethodDescription only).
* **SCR‑F11‑S03 (Actuation inclusion).** All Actuation statements are modeled as **within** a Work interval.
* **SCR‑F11‑S04 (Context discipline).** Each quartet term is expressed as a **SenseCell** with its Context; no Cross‑context identity is asserted here.
* **SCR‑F11‑S05 (Bridge guard).** Any Cross‑context reasoning among quartet terms references an explicit **Bridge** with **kind/CL/Loss**.

### 15.2 Regression checks (RSCR)

* **RSCR‑F11‑E01 (Spec update).** When a MethodDescription changes, previous Works remain valid and unchanged; their statuses don’t shift unless re‑evaluated with explicit rationale.
* **RSCR‑F11‑E02 (Bridge drift).** If a Context updates, revisit Bridges that touch quartet terms; adjust **CL/Loss** only via F.7/F.9.
* **RSCR‑F11‑E03 (Status drift).** Adding new statuses does not move them across boxes (e.g., no new “Work‑Approved”).
* **RSCR‑F11‑E04 (Signal creep).** Introducing new Actuation details does not erase or replace Work context.

---

## 16 · Didactic distillation (90‑second script)

> “When you talk about *how something is done*, decide which of the **four boxes** you mean.
> **Method** is the **idea** (the way). **MethodDescription** is the **recipe** (the description). **Work** is the **happening** (what actually occurred). **Actuation** is the **control push** (signals emitted during Work).
> Keep **design** and **run** as distinct **stances**. Plans and approvals live in the **design stance**; measurements and obligations live in the **run stance** within **Windows**.
> Words like *process*, *task*, *activity*, *command* are **context‑local**—say *process (BPMN)*, *activity (PROV)*, *task (IEC)*. If you must relate them, draw a **Bridge** and declare its **kind**, **CL**, and **Loss**.
> For compliance, don’t point at the plan—point at **Work**, show **Observations**, and judge clauses in **F.10**.
> Hold this quartet in your head and you’ll stop mixing plans with facts, signals with outcomes, and names across Contexts. + Everything else—naming (F.5), `U.RoleDescription` (F.4) and `U.RoleAssignment`/`U.RoleEnactment` (A.2.1/F.6), Bridges (F.7/F.9)—falls into place.

# F.12 — Service Acceptance Binding \[A] 

**“Judge promises on what happened, not on what was planned.”**
**Status.** Architectural pattern \[A], architheory‑agnostic.
**Builds on:** F.1 **context of meaning (U.BoundedContext)**; F.2 **Term Harvesting**; F.3 **Intra‑Context Sense Clustering**; F.5 **Naming Discipline**; F.7/F.9 **Bridges & CL**; F.10 **Status Families & Windows**; F.11 **Method Quartet Harmonisation**; A.2.3 **U.Service**.
**Coordinates with.** KD‑CAL (Observation/Characteristic/Scale); Sys‑CAL (Work/Actuation contexts).
**Non‑goals.** No team workflows, no tooling, no editorial procedures. This pattern specifies **how to think** about acceptance, not how to store or operate systems.

---

## 1 · Intent & applicability

**Intent.** Provide a **conceptual binding** that turns a *service promise* (SLO/SLA clause) into a **clear, local, time‑bounded judgement** about **actual Work**, using **Observations** as evidence and **explicit Bridges** where Cross‑context notions must meet. The result is a **Status** (Satisfied/Violated/Inconclusive) that attaches to the **clause‑about‑that‑Work‑in‑that‑Window**.

**Applicability.** Any situation where a service is promised (availability, latency, safety margin, response time, quality gate, compliance duty) and its fulfilment must be decided from what occurred. Works across digital services, industrial control, laboratory processes, clinical pathways, logistics, etc.

---

## 2 · Problem frame

1. **Plan ≠ proof.** Diagrams and playbooks are treated as if they demonstrated fulfilment.
2. **Signal ≠ outcome.** Control signals (Actuation) are mistaken for the service outcome experienced by the consumer.
3. **Global meanings.** *Availability*, *incident*, *latency* are used as if universal, ignoring context‑local senses.
4. **Unstated translation.** Metrics from one canon are mapped to clauses from another without declaring losses.
5. **Timeless verdicts.** Judgements are asserted with no explicit Window (day, month, batch).

---

## 3 · Forces

| Force                                | Tension to resolve                                                                                        |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| **Promise vs. occurrence**           | Service is defined as an external **promise** (A.2.3), yet acceptance must reference **Work** (run‑time). |
| **Locality vs. integration**         | Meanings are **context‑local**; still we must compare across services, plants, and monitors.                 |
| **Parsimony vs. realism**            | We want a small binding scheme, yet domains differ (percentiles, downtime minutes, control margins).      |
| **Evidence vs. privacy/feasibility** | Observations prove outcomes; sometimes only proxies exist.                                                |

---

## 4 · Core idea (didactic)

**Bind promises to runs with measurements in time.**
Acceptance is a **quadruple of anchors** (all context‑local):

1. **ClauseCell** — a deontic/Standardual **SenseCell** stating the promise (*availability ≥ 99.9%*, *MTTR ≤ 60 min*, *temperature within band*).
2. **WorkCell** — a **SenseCell** for the **Work** that enacted the service in the relevant situation.
3. **MeasureCell** — a **SenseCell** for the **Observation/Characteristic** used as evidence (KD‑CAL).
4. **Window** — the explicit period in which the judgement is made (F.10).

A **Predicate** compares the **Measure** against the **Clause** within the **Window**.
The **Status** (Satisfied/Violated/Inconclusive) attaches to **ClauseCell\@Window about WorkCell**, never to a plan.

---

## 5 · Minimal vocabulary (this pattern only)

* **ClauseCell.** A context‑local deontic/Standardual concept (*SLO*, *obligation*, *target*), typically from *services/deontics* Contexts (e.g., **ITIL 4**, **ODRL**).
* **WorkCell.** A context‑local run‑time occurrence (PROV **Activity**, IEC **Task Execution**, etc.).
* **MeasureCell.** A context‑local observation concept (KD‑CAL **Observation** over a **Characteristic** with a **Scale/Unit**).
* **Window.** A time envelope (calendar month, batch, incident interval, shift) per F.10.
* **Predicate.** A clause‑shape: threshold, percentile, count‑within‑limit, band‑conformance, etc.
* **Bridge.** An explicit Cross‑context relation with **kind/CL/Loss** (F.7/F.9).

> **Context discipline.** Terms like *availability*, *activity*, *task*, *observation* are always read as **context‑local**. Cross‑use requires a **Bridge**.

---

## 6 · The binding, as five mental rules (notation‑free)

**R1 — Locus rule.**
A service verdict **attaches to the Clause**, scoped by a **Window**, **about a specific Work**:
`status(ClauseCell, WorkCell, Window) ∈ {Satisfied, Violated, Inconclusive}`.
*Reading:* We do not place “Satisfied” on the plan or on the whole service concept.

**R2 — Evidence rule.**
Only **Observations** (MeasureCell) that **refer to the outcome of the same Work** and **lie within the Window** may support the verdict.
*Reading:* Control commands and approvals are not evidence of outcome.

**R3 — Predicate rule.**
Every ClauseCell is read with a **Predicate** schema that defines how Measures decide:

* **Threshold:** `value ≥/≤ target`.
* **Percentile:** `Pₚ(value) ≤ target`.
* **Ratio/Share:** `good_time / total_time ≥ target`.
* **Count‑within‑limit:** `count(events of type E) ≤ target`.
* **Band:** `min(value) ≥ L ∧ max(value) ≤ U`.

**R4 — Bridge rule.**
If Clause, Work, and Measure live in **different Contexts**, apply declared **Bridges** with **kind**, **CL**, and **Loss** notes.
*Reading:* Without a Bridge, do not presume transferability of meanings.

**R5 — Window rule.**
Every verdict is **time‑bounded**. Changing the Window can change the result; **no retroactivity** from new clauses or specs (cf. F.10).

---

## 7 · Clause templates (conceptual schemata)

> These are **shapes of meaning**, not data fields.

1. **Availability (share‑of‑time)**

* **ClauseCell:** *service availability ≥ 99.9% monthly* (services Context).
* **MeasureCell:** *uptime indicator* over **Work** (KD‑CAL).
* **Predicate:** `good_time/total_time ≥ 0.999`.
* **Window:** calendar month.
* **Bridge:** from monitor semantics → consumer‑perceived availability (**kind:** proxy; **CL:** 2; **Loss:** blind to partial degradations).

2. **Latency (percentile)**

* **ClauseCell:** *p95 latency ≤ 120 ms during incidents* (services Context).
* **MeasureCell:** *response time observation* for the same **Work episode** (KD‑CAL).
* **Predicate:** `P95(latency) ≤ 120ms`.
* **Window:** incident interval.
* **Bridge:** from request‑level telemetry → service‑level promise (**kind:** aggregation; **CL:** 2; **Loss:** sampling bias).

3. **Safety margin (band)**

* **ClauseCell:** *temperature ∈ \[L,U] during batch* (deontics/quality Context).
* **MeasureCell:** *process temperature observation* (KD‑CAL).
* **Predicate:** `min ≥ L ∧ max ≤ U`.
* **Window:** batch run interval (Work).
* **Bridge:** not needed if Measure and Clause are in the same Context; otherwise declare.

4. **MTTR (count‑within‑limit + duration)**

* **ClauseCell:** *MTTR ≤ 60 min per incident*.
* **MeasureCell:** *timestamps of Work phases* (start fix → restore).
* **Predicate:** `restore_time − start_fix ≤ 60 min`.
* **Window:** each incident’s **Work** interval.
* **Bridge:** BPMN design steps → PROV Work **Interpretation** (CL=2; **Loss:** gateways ≠ real branching).

---

## 8 · Invariants (normative)

1. **Design/run split.** Clauses live on the **design stance**; judgements live on the **run stance** about **Work** (F.11).
2. **Context locality.** All terms are **context‑local**; Cross‑context meaning flows **only** across declared **Bridges**.
3. **Observation‑only evidence.** Verdicts require **Observations** that **about‑refer** to Work outcomes; **Actuation** and **Approvals** are not sufficient.
4. **Window explicitness.** Every verdict carries a **Window**; no timeless acceptance.
5. **Predicate declared.** The Clause’s **Predicate** is explicit; no hidden aggregation or default percentile.
6. **Non‑retroactivity.** Updating clauses or specs does not alter past verdicts; re‑evaluation must be explicit.
7. **One‑Work focus.** A verdict references a **specific Work** (or a defined population of Works) matched to the Clause’s scope.
8. **Loss honesty.** Each Bridge states **kind/CL/Loss**; stronger claims require stronger Bridges or same‑Context alignment.

---

## 9 · Micro‑examples (didactic, multi‑domain)

### 9.1 SaaS uptime (services + sensing)

* **Contexts:** *ITIL 4* (Clause), *PROV‑O* (Work), *SOSA/SSN* (Measure).
* **ClauseCell:** *availability ≥ 99.9% monthly*.
* **WorkCell:** *service provision* Activities during June.
* **MeasureCell:** *uptime observation* from synthetic probes.
* **Predicate:** share‑of‑time ≥ 0.999.
* **Bridge:** probe result → user availability (**kind:** proxy; **CL:** 2; **Loss:** regional gaps).
* **Verdict:** *Satisfied (June)* if the ratio holds; **attaches to Clause\@June about those Works**.

### 9.2 Furnace band (industrial control)

* **Contexts:** *quality/deontics canon* (Clause), *IEC 61131‑3/PROV* (Work), *KD‑CAL* (Measure).
* **ClauseCell:** *product temperature within \[720,740] °C during soak*.
* **WorkCell:** *soak phase* Work interval.
* **MeasureCell:** thermocouple Observations (KD‑CAL).
* **Predicate:** band conformance.
* **Bridge:** IEC task interval → PROV Activity (**Interpretation**, CL=2).
* **Verdict:** *Violated* if any measured value exits the band.

### 9.3 Incident MTTR (services + enactment)

* **Contexts:** *ITIL 4* (Clause), *PROV‑O* (Work).
* **ClauseCell:** *MTTR ≤ 60 min per incident*.
* **WorkCell:** each incident’s handling Activity.
* **MeasureCell:** timestamps (Observed facts) of start‑fix and restore events.
* **Predicate:** duration ≤ 60 min.
* **Bridge:** BPMN steps → PROV Activity (**Interpretation**, CL=2).
* **Verdict:** *Satisfied* if the measured interval meets the target.

## 10 · Anti‑patterns & remedies

| #       | Anti‑pattern                    | Symptom in practice                                                                          | Why it breaks thinking                          | Remedy (conceptual move)                                                                                                                                 |
| ------- | ------------------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **A1**  | **Plan‑as‑proof**               | A BPMN or runbook is cited as if it proved the SLO was met.                                  | Design artefacts are **not** occurrences.       | Apply **R1 locus** + **R2 evidence**: attach the verdict to **ClauseCell\@Window about WorkCell** and require **Observations** of outcomes.              |
| **A2**  | **Signal‑as‑outcome**           | Control **Actuation** (setpoint writes, approvals) treated as evidence of delivered service. | Commands are intentions, not results.           | Accept only **MeasureCell** that **about‑refer** to the **same Work**; if a control signal is used as proxy, declare a **Bridge(kind=proxy, CL, Loss)**. |
| **A3**  | **Windowless verdict**          | “We met the SLA” with no stated period or scope.                                             | Unfalsifiable; mixes populations.               | Enforce **R5 Window**: every verdict names a **Window** (month, batch, incident interval).                                                               |
| **A4**  | **Global words**                | *Availability*, *latency* used without a Context.                                               | Collides senses across disciplines.             | Speak with **Context prefixes** (F.1). Cross‑context reuse demands a **Bridge** (F.9).                                                                         |
| **A5**  | **Percentile mirage**           | p95 computed on a pooled year while the clause is monthly.                                   | Predicate and Window misaligned.                | **R3 Predicate** + **R5 Window**: compute the statistic **per Clause’s Window**.                                                                         |
| **A6**  | **Proxy blindness**             | Synthetic probes stand in for user experience with no limitations stated.                    | Proxies miss geography, jitter, or pathologies. | Declare **Bridge(kind=proxy, CL, Loss)**. If proxy coverage is too weak, the verdict is **Inconclusive**.                                                |
| **A7**  | **Scope drift (Work mismatch)** | Measured another product’s or region’s traffic but judged the whole service.                 | Evidence is about the wrong **Work**.           | Tie **MeasureCell** to the **same WorkCell** (or a stated population‑of‑Works) as the Clause scopes.                                                     |
| **A8**  | **Retroactive renorm**          | A new clause or recalibrated monitor silently rewrites past verdicts.                        | Violates temporal honesty.                      | Enforce **Non‑retroactivity** (Inv‑6): past verdicts stand; new rules apply forward.                                                                     |
| **A9**  | **Silent units**                | “Latency ≤ 120” with no unit or scale.                                                       | Ambiguous thresholds.                           | **KD‑CAL discipline**: state **Characteristic, Scale, Unit** on **MeasureCell**.                                                                         |
| **A10** | **Hidden aggregation**          | “Global availability” but only a subset of regions/slices was covered.                       | Over‑claims evidence.                           | State the **aggregation scope** explicitly or confine the verdict to the observed subset; otherwise **Inconclusive**.                                    |
| **A11** | **Status on the service**       | Tagging the abstract service as “Satisfied”.                                                 | Loses the describedEntity of the judgement.           | Attach to **ClauseCell\@Window about WorkCell**; the service concept remains a promise vocabulary (A.2.3).                                               |
| **A12** | **Bridge‑by‑name**              | Equating *Activity* ≡ *Process* because both say “process”.                                  | Assumes global meaning.                         | Use **F.9 Bridge** with **kind/CL/Loss**; or keep them distinct.                                                                                         |

---

## 11 · Extended worked examples (multi‑architheory)

> Each example identifies **Contexts**, the **quadruple** ⟨ClauseCell, WorkCell, MeasureCell, Window⟩, any **Bridge(s)**, and the **Predicate**. The verdict attaches to *ClauseCell\@Window about WorkCell*.

### 11.1 CDN latency across regions (services + sensing + types)

* **Contexts.** *ITIL 4* (Clause), *PROV‑O* (Work), *SOSA/SSN* (Measure), *OWL 2* (type labels).
* **ClauseCell.** *p95 end‑user latency ≤ 200 ms per region per month*.
* **WorkCell.** *delivery Activities* per region during the month (PROV).
* **MeasureCell.** *response‑time Observations* tagged by region and path (SOSA/SSN).
* **Predicate.** For each region in the Window, `P95(latency) ≤ 200 ms`.
* **Bridges.** *probe→user* (**kind**: proxy; **CL** 2; **Loss**: last‑mile bias).
* **Verdict.** Region‑wise statuses; a global “all‑regions met” is the **logical AND** of region statuses (declare this aggregation explicitly).
* **Manager cue.** “Green map ≠ one green verdict”; acceptance is **per Clause per Window per Work population**.

### 11.2 Stroke care: door‑to‑needle (method + enactment + status)

* **Contexts.** *clinical guideline canon* (Clause), *PROV‑O* (Work), *SOSA/SSN* (Measure), *F.10* (status windows).
* **ClauseCell.** *90% of ischemic‑stroke episodes achieve door‑to‑needle ≤ 30 min per quarter*.
* **WorkCell.** Population of **patient‑episode Activities** started in the quarter.
* **MeasureCell.** Timestamps **Observation** of *door* and *needle* events (KD‑CAL).
* **Predicate.** `|{episodes with (needle−door ≤ 30)}| / |{episodes}| ≥ 0.9`.
* **Bridges.** *EHR event semantics → PROV Activity* (**Interpretation**, **CL** 2; **Loss**: missing triage tags).
* **Verdict.** If data gaps exceed a declared tolerance, status is **Inconclusive** rather than “Satisfied by assumption”.

### 11.3 Cold‑chain warehouse (control + sensing + deontics)

* **Contexts.** *quality/deontics canon* (Clause), *IEC 61131‑3/PROV* (Work), *SOSA/SSN + ISO 80000‑1* (Measure).
* **ClauseCell.** *temperature ∈ \[2,8] °C for ≥ 99.5% of each day*.
* **WorkCell.** The warehouse’s **daily storage Activity**.
* **MeasureCell.** Thermistor **Observations** with calibrated units (KD‑CAL/ISO 80000‑1).
* **Predicate.** `(good_time / 24h) ≥ 0.995`.
* **Bridges.** *sensor position → product exposure* (**kind**: proxy; **CL** 2; **Loss**: stratification).
* **Verdict.** *Violated* if any day fails; annotate **Loss** to communicate assurance limits.

### 11.4 SaaS incident MTTR (services + enactment)

* **Contexts.** *ITIL 4* (Clause), *PROV‑O* (Work).
* **ClauseCell.** *MTTR ≤ 60 min per incident*.
* **WorkCell.** Each incident’s handling **Activity**.
* **MeasureCell.** **Observations** of start‑fix and restore timestamps.
* **Predicate.** `(restore − start_fix) ≤ 60 min`.
* **Verdict.** Per incident; a quarter’s report is an explicit aggregation of incident‑scoped verdicts.

---

## 12 · Reasoning primitives (judgement schemas, notation‑free)

> These are **mental inferences**; they neither read nor write artefacts. Each reads “if these thoughts hold, you may safely conclude …”.

1. **Clause–Work match**
   `covers(ClauseCell, WorkCell) ⊢ admissible(ClauseCell, WorkCell)`
   *Reading:* The Clause speaks **about** the kind of Work under judgement (scope alignment).

2. **Window adequacy**
   `Window is explicit ∧ Window intersects WorkCell-occurrence ⊢ admissible(Window)`
   *Reading:* There is a concrete time envelope; the Work actually occurred within it.

3. **Evidence sufficiency**
   `Observations E about WorkCell within Window ⊢ sufficient(E)`
   *Reading:* There exists a non‑empty set of outcome **Observations** relevant to the Work and Window.

4. **Evidence insufficiency → Inconclusive**
   `¬sufficient(E) ⊢ status = Inconclusive(ClauseCell, WorkCell, Window)`
   *Reading:* Absent admissible evidence, do not guess; mark **Inconclusive**.

5. **Predicate evaluation**
   `sufficient(E) ∧ eval(Predicate, E) = true ⊢ status = Satisfied(ClauseCell, WorkCell, Window)`
   `sufficient(E) ∧ eval(Predicate, E) = false ⊢ status = Violated(ClauseCell, WorkCell, Window)`
   *Reading:* The **Predicate** (threshold/percentile/share/band/…) decides directly from E.

6. **Bridge discipline**
   `usesCrossContexts(ClauseCell, WorkCell, MeasureCell) ∧ Bridges B declared ⊢ admissible(B)`
   `usesCrossContexts … ∧ ¬admissible(B) ⊢ status = Inconclusive`
   *Reading:* Cross‑context comparisons require explicit **Bridges**; without them, **Inconclusive**.

7. **CL aggregation (assurance hint)**
   `Bridges B = {b₁…bₖ} ⊢ effectiveCL = min(CL(bᵢ))`
   *Reading:* The weakest Bridge governs the assurance level communicated with the verdict (advisory to B.3 calculus).

8. **Population clauses**
   `Clause quantifies over population W = {w₁…wₙ} ⊢ status = agg({status(Clause, wᵢ, Window)})`
   *Reading:* For “≥ p%”‑style clauses, compute per‑Work verdicts, then apply the Clause’s quantifier.

9. **Non‑retroactivity**
   `newClause or newMonitor after Window ⊢ doesNotAlter(status@Window)`
   *Reading:* Later changes do not rewrite past verdicts.

10. **Conflict exposure**
    `two admissible Bridge sets ⇒ conflicting statuses ⊢ escalate as Inconclusive, expose Loss notes`
    *Reading:* If equally defensible translations disagree, the honest outcome is **Inconclusive** plus an explanation.

---

## 13 · Relations (with other patterns)

* **Builds on:**
  **F.1** (Contexts): keeps all meanings **local**.
  **F.2–F.3**: provide the **SenseCells** that become Clause/Work/Measure anchors.
  **F.5**: ensures labels for Clause/Work/Measure and Windows are didactically clear.
  **F.7–F.9**: supply **Bridge** kinds / **CL** and loss semantics.
  **F.10**: defines **Status** families and **Window** constructs.
  **F.11**: protects **Method / MethodDescription / Work / Actuation** distinctions.

* **Uses (Part C architheories).**
  **KD‑CAL** (Observation/Characteristic/Scale/Unit).
  **Sys‑CAL** (Work/Actuation Contexts).
  **Kind-CAL** (type labels for populations or cohort selection).

* **Constrains:**
  Later reporting and assurance rules (B.3) must **not** collapse CL/Loss; they report them alongside status.

---

## 14 · Migration notes (conceptual)

1. **Clause revisions.** Introduce a **new ClauseCell**; keep old verdicts intact (Non‑retroactivity).
2. **Monitor changes.** Update or replace **Bridges** (kind/CL/Loss). Future verdicts use the new Bridge; past ones are annotated, not rewritten.
3. **Scope corrections.** If evidence was about the wrong **Work**, retire the verdict and restate the quadruple; do **not** patch by redefining the Clause.
4. **Unit harmonisation.** When scales/units change, apply **KD‑CAL** conversions inside the Measure’s Context; if Cross‑context mapping is needed, declare a **Bridge**.
5. **Population refinement.** If a Clause’s quantifier is refined (e.g., per‑region → per‑AZ), treat each as a new ClauseCell or a new Window partition; avoid hidden re‑baselining.
6. **Proxy retirement.** When direct Observations become available, prefer them; keep earlier proxy‑based verdicts with their CL/Loss notes.

---

## 15 · Acceptance tests (SCR/RSCR — concept‑level)

### 15.1 Static conformance (SCR)

* **SCR‑F12‑S01 (Quadruple present).** Every acceptance statement names **ClauseCell**, **WorkCell**, **MeasureCell**, and **Window**.
* **SCR‑F12‑S02 (context‑locality).** Each of the three Cells cites a **Context** (U.BoundedContext).
* **SCR‑F12‑S03 (Evidence admissibility).** The **Observation(s)** are **about** the **same Work** and lie within the **Window**.
* **SCR‑F12‑S04 (Predicate explicit).** The **Predicate** shape is stated (threshold/percentile/share/band/…) with any needed aggregation scope.
* **SCR‑F12‑S05 (Bridge discipline).** Any Cross‑context use declares **Bridge(kind, CL, Loss)**.
* **SCR‑F12‑S06 (Status trichotomy).** The verdict is exactly one of **{Satisfied, Violated, Inconclusive}** and attaches to **ClauseCell\@Window about WorkCell**.
* **SCR‑F12‑S07 (Unit honesty).** MeasureCell specifies **Characteristic, Scale, Unit** (KD‑CAL).
* **SCR‑F12‑S08 (Temporal honesty).** No verdict is asserted without a **Window**; no clause retroactively changes past verdicts.

### 15.2 Regression checks (RSCR)

* **RSCR‑F12‑E01 (Bridge update).** When a **Bridge CL** changes, past verdicts stand; future verdicts **reference the new CL**; reports surface the difference.
* **RSCR‑F12‑E02 (Edition churn).** When a Context’s canon updates, Cells reference the **edition**; old verdicts remain bound to their original editions.
* **RSCR‑F12‑E03 (Scope drift guard).** If the Work population definition changes, verdicts are not silently re‑interpreted; new verdicts cite the new population.
* **RSCR‑F12‑E04 (Window partition).** Changing from monthly to weekly windows creates **new** verdicts; monthly summaries are expressed as explicit aggregations of weekly statuses.
* **RSCR‑F12‑E05 (Proxy retirement).** When direct Observations replace proxies, the status computation is re‑run **forward‑only**; past proxy‑based verdicts retain their CL/Loss annotations.

---

### 15.3 Didactic distillation (60‑second recap)

> **Bind promises to runs with measurements in time.**
> Name the **Clause**, the **Work** it talks about, the **Measure** of what actually happened, and the **Window**. Evaluate the Clause’s **Predicate** on Observations **about that Work in that Window**. If any concept crosses Contexts, declare a **Bridge** with **kind/CL/Loss**. The verdict (**Satisfied/Violated/Inconclusive**) attaches to **Clause\@Window about Work**, never to a plan or to the abstract service.

# F.13 — Lexical Continuity & Deprecation \[A] 

**“Change names without changing history.”**
**Status.** Architectural pattern \[A], architheory‑agnostic.
**Builds on:** F.1 **context of meaning**; F.2 **Term Harvesting**; F.3 **Intra‑Context Clustering (SenseCell)**; F.5 **Naming Discipline**; F.7 **Concept‑Set (row) construction**; F.8 **Mint‑or‑Reuse decision**; F.9 **Bridges**; F.10 **Status windows**.
**Coordinates with.** Part C CALs when canon editions change (Sys/KD/Type/Method/LCA).
**Non‑goals.** No registries, workflows, editors, or storage formats. No by‑name Cross‑context equivalence. No silent rewrites of old texts.

---

## 1 · Intent & applicability

**Intent.** Provide a **conceptual discipline** for evolving labels (for **SenseCells**, **Concept‑Set rows**, and **Role Description names**) so that:

* new names **clarify** without erasing what earlier texts meant;
* aliases remain **local to Contexts**;
* genuine sense changes cause **explicit splits/merges** (F.7/F.9), not cosmetic renames.

**Applicability.** Whenever you consider **renaming**, **aliasing**, **deprecating**, or **retiring** any label in FPF: a SenseCell label in a Context, a Concept‑Set row label, or a Role Description name.

---

## 2 · Problem frame

Unification efforts rot when names drift faster than senses or, worse, when senses change under a constant name.

* **Silent relabeling.** A new label is introduced as if nothing changed; readers cannot connect past to present.
* **Alias bloat.** Synonyms accumulate without discipline; reading becomes guesswork.
* **Cross‑context aliasing.** A single alias is made to stand for different Contexts (“global slang”), defeating locality.
* **Retroactive edits.** Old texts are silently rewritten to today’s names, corrupting provenance.

---

## 3 · Forces

| Force                          | Tension to resolve                                                                           |
| ------------------------------ | -------------------------------------------------------------------------------------------- |
| **Continuity vs truthfulness** | Preserve readers’ continuity yet surface real sense changes (no paint‑over).                 |
| **Locality vs convenience**    | Keep aliases **inside Contexts** even when a catchy global name tempts reuse.                   |
| **Simplicity vs coverage**     | Avoid giant synonym lists while still catching the one or two legacy names people will meet. |
| **Didactics vs formality**     | Make the mapping teachable without inventing new low‑level artefacts or processes.           |

---

## 4 · Core idea (didactic)

**Treat names as lenses, not objects.**
The **thing that persists** is the *sense* (a **SenseCell** inside a Context, or the *Cross‑context alignment* embodied by a **Concept‑Set row**, or a **Role Description** that points to such sense). Names are **lenses** we look through. When the lens improves, we **record a continuity relation** between lenses; when the underlying sense changes, we **split/merge the thing**, then name accordingly.

> **Contexts keep names local.**
> A label (including aliases) always belongs to **one context** or to **one Concept‑Set row**. Cross‑context similarity is handled by **Bridges** (F.9), never by shared names.

---

## 5 · Minimal vocabulary (this pattern only)

* **Legacy label** — a previously used label in the same Context (or same Concept‑Set row / Role Description).
* **Preferred label** — the current **F.5‑conformant** label for that item.
* **Alias** *(context‑local)* — a **read‑path** from a legacy label to the preferred one **inside the same Context** (or the same row/template). For writing, prefer the current label.
* **Continuity relation** — a small set of **relations over labels** (below) that capture whether a change is *just wording* or a *real sense change*.
* **Epoch note** — an **informative** time marker (“used before 2024‑07”) attached to a legacy label to help readers of old texts. (No storage format implied.)

---

## 6 · Solution — Continuity, not “registries”

Rather than maintain a tool or workflow, **think with five continuity relations**. Use the *least strong* relation that tells the truth.

### 6.1 Continuity relations (normative meanings)

1. **`renames(label_old → label_new)`** — *wording improved, sense unchanged*.
   *Use when:* Same **SenseCell** / same **Concept‑Set row** / same **Role Description**; only the surface form changed to satisfy F.5 (morphology, disambiguation, plain/tech harmony).
   *Effect:* `label_old` becomes a **context‑local alias** of `label_new`; both resolve to the **same thing**. Past texts remain valid.

2. **`aliases(label_legacy ↔ label_pref)`** — *legacy synonym kept for reading*.
   *Use when:* A common historical synonym exists **in the same Context** for the **same SenseCell**.
   *Effect:* Two‑way **read‑path** only; **writing uses `label_pref`**. Keep at most **one** legacy alias per register to avoid bloat.

3. **`splits(label_old ⇒ {label_A, label_B})`** — *one label covered multiple senses; now separated*.
   *Use when:* Your **SenseCell** was really two local senses; F.3 has **split** them; or a **Concept‑Set row** is refactored into two rows.
   *Effect:* `label_old` is **deprecated** (read‑path allowed to a **disambiguation note**); new writing uses `label_A`/`label_B`. No claim that either *continues* the old label wholesale.

4. **`merges({label_A, label_B} ⇒ label_new)`** — *two labels now recognized as one sense*.
   *Use when:* F.3 shows **same SenseCell**; or two Concept‑Set rows collapse after F.9 raised CL sufficiently.
   *Effect:* `label_A` and `label_B` become **aliases** of `label_new`. Keep one **epoch note** on each legacy label.

5. **`retires(label_old)`** — *name withdrawn without successor*.
   *Use when:* The label proved misleading and **no single successor** exists (e.g., it spanned different Contexts, or it was metaphorical).
   *Effect:* Only a **read‑warning** remains (“avoid in new writing; see Contexts X/Y”). Readers are pointed to **Bridges** or to multiple rows.

> **Important:** All five relations are **context‑local** (SenseCell level) or **row‑local** (Concept‑Set). **Never** use them to “alias” across Contexts. If a change crosses Contexts, it is not a rename; it requires a **Bridge** (F.9) and often a **split/merge of rows** (F.7).

---

## 7 · Invariants (normative)

1. **Locality of alias.** `aliases(·)` and `renames(·)` operate **within one context** (SenseCell) or **within one Concept‑Set row / Role Description**.
2. **Truth over comfort.** If the **sense changed**, use `splits`/`merges` (and possibly adjust rows/Bridges), **not** `renames`.
3. **Non‑retroactivity.** Past texts remain phrased as written; continuity only **adds read‑paths**, never rewrites.
4. **Alias parsimony.** per Context and per row, keep **≤ 1** legacy alias per register (Tech/Plain); prefer the one readers will most likely encounter.
5. **Prefer present for writing.** In normative writing, use the **current preferred label** (F.5). Aliases are for **reading comprehension**.
6. **Bridge discipline.** If a label shift would require crossing Contexts to “explain”, it is **not a rename**; use **F.9 Bridge** and, if needed, refactor the **Concept‑Set row(s)**.
7. **Epoch honesty.** When declaring continuity, attach a **succinct epoch note** (“pre‑2023 usage”) if it aids readers.

---

## 8 · Self‑checks (mental, not procedural)

* **Same‑sense test.** Can you point to the **same SenseCell** (or same row) before and after? If yes → `renames`/`aliases`. If no → `splits`/`merges`.
* **Context test.** Does the change stay **inside one context**? If it needs two Contexts to explain, it’s a **Bridge**, not a rename.
* **Reader test.** What two legacy strings would a newcomer actually meet in old texts? Keep **those two** as aliases; drop the rest.
* **History test.** Does your “continuity” require editing old claims? If yes, you’re attempting a **retroactive rewrite**—stop.
* **Didactic test.** Can you explain the continuity relation in **one sentence**? If not, you are hiding a sense change.

---

## 9 · Micro‑examples (illustrative)

### 9.1 Pure rename inside a Context (ITIL → clearer plain label)

*Context:* **ITIL 4 (services)**.
Old: **“SLO” (plain: *service target*)** → New: **“service‑level objective” (plain unchanged)**.
**Relation:** `renames("SLO" → "service‑level objective")`.
**Why:** F.5 morphology & expansion; SenseCell unchanged (same clause semantics).
**Effect:** Old guidance remains readable; new writing spells out the term.

### 9.2 Alias for a common legacy synonym (Sys‑CAL)

*Context:* **state‑space control (design)**.
Preferred: **“actuation”**. Legacy: **“control output”**.
**Relation:** `aliases("control output" ↔ "actuation")`.
**Why:** Same SenseCell; legacy term appears in older textbooks.
**Effect:** Readers resolve to the SenseCell; new texts use “actuation”.

### 9.3 Split of a muddled local sense (Enactment)

*Context:* **BPMN 2.0**.
Legacy label **“process”** was used to mean both **“collaboration”** and **“executable process”** in a team’s prose.
**Relation:** `splits("process" ⇒ {"collaboration","executable‑process"})`.
**Effect:** The single Concept‑Set row becomes two; old label is deprecated with a disambiguation note.

### 9.4 Merge after clustering raised confidence (Kind-CAL row)

Two Concept‑Set rows **{“DBaaS”, “Database‑Service”}** converge after F.3 within the same context profile and F.9 raised CL.
**Relation:** `merges({"DBaaS","Database‑Service"} ⇒ "Database‑Service")`.
**Effect:** “DBaaS” becomes a legacy alias with an epoch note.

### 9.5 Not a rename: Cross‑context temptation (forbidden)

*Contexts:* **BPMN (design graph)** vs **PROV‑O (run activity)**.
Temptation: “Let’s rename *process* to *activity*.”
**Diagnosis:** Cross‑context; **different SenseCells**.
**Action:** **No continuity relation.** Keep labels; if needed, declare a **Bridge** (F.9) explaining design→run mapping with CL/Loss.

## 10 · Anti‑patterns & remedies

| #       | Anti‑pattern               | Symptom in texts                                                      | Why it harms thinking                                          | Remedy (conceptual move)                                                                                                         |
| ------- | -------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **A1**  | **Cross‑context rename**      | “Let’s rename *process (BPMN)* to *activity (PROV)*.”                 | Erases Context boundaries; hides loss; violates locality.         | **Do not rename across Contexts.** Keep both labels; if you must relate them, declare a **Bridge** (F.9) with CL/loss.              |
| **A2**  | **Retroactive rewrite**    | Old passages silently updated to new names.                           | Breaks provenance; misleads readers about what was meant then. | **Non‑retroactivity.** Past texts stand; add **read‑paths** via `renames/aliases`; attach **epoch notes** when helpful.          |
| **A3**  | **Alias flood**            | Long lists of synonyms for comfort.                                   | Raises ambiguity; dilutes teaching signals.                    | **Alias parsimony.** Keep ≤ 1 legacy alias per register (Tech/Plain) **inside the same Context or row**.                            |
| **A4**  | **Paint‑over rename**      | Rename used where sense actually changed.                             | Confuses continuity with revision; hides splits.               | Use **`splits`** (or **`merges`**), not `renames`. If Contexts diverge, adjust **rows** (F.7) and **Bridges** (F.9).                |
| **A5**  | **Global alias**           | One catchy word reused as alias in several Contexts.                     | Creates a pseudo‑global dictionary; invites category errors.   | **Local aliases only.** If a word appears in many Contexts, treat it as **homonymous**; keep Context‑prefixed speech.                  |
| **A6**  | **Euphemism treadmill**    | Frequent cosmetic renames (“modernising” labels) with no gain.        | Cognitive noise; readers lose confidence in names.             | Apply the **Same‑sense test**. If gain is marginal, **do nothing**; if clarity improves materially, one **`renames`** is enough. |
| **A7**  | **Grandfather everything** | Never deprecate confusing legacy labels.                              | Drags ambiguity forward; blocks sharper distinctions.          | When a label truly misleads and has no single successor, **`retires`** with a short **pointer note** to Contexts/rows.              |
| **A8**  | **Row drift via rename**   | Concept‑Set row is relabeled while its membership silently changes.   | Hides that the set changed; breaks Cross‑context alignment.       | First **split/merge rows** (F.7) as needed; only then `renames` the row **if** its intension stayed.                             |
| **A9**  | **Bridge‑by‑alias**        | Using an alias to hint two Contexts are “the same.”                      | Smuggles translation without CL/loss.                          | **No Cross‑context aliasing.** If similarity matters, **Bridge** explicitly (F.9) and keep labels separate.                         |
| **A10** | **Acronym absolutism**     | Treating acronyms as preferred labels everywhere (“SLO” in any Context). | Obscures Context‑specific senses; hurts didactics.                | Prefer **expanded** labels as preferred (F.5); keep acronym as context‑local **alias** only where historically dominant.            |
| **A11** | **Temporal fudge**         | Rename used to imply design↔run shift (“execution ≈ process”).        | Conflates time stances; erases important dualities.            | Keep **design/run** explicit on labels or glosses; if mapping is needed, do so in **F.9**.                                       |
| **A12** | **Over‑canonicalisation**  | Forcing a single “perfect” label across all rows/Contexts.               | Centralises language; breaks heterogeneity guard.              | Let each Context/row keep its **own preferred label**; put unification pressure only into **rows** and **Bridges**.                 |

---

## 11 · Extended examples (multi‑architheory)

### 11.1 KD‑CAL × Services — *metric target* labels over time

* **Contexts:** *ITIL 4 (services, design)*; *SOSA/SSN (sensing, run)*.
* **Before:** Role Description used **“SLO”** (plain “target”) and readers often saw **“service target”**.
* **Move:** `renames("SLO" → "service‑level objective")` (Context: ITIL). Keep `aliases("service target" ↔ "service‑level objective")`.
* **Why:** Same local sense; clearer morphology for F.5; SOSA/SSN labels untouched.
* **Pay‑off:** Runtime **Observations** (SOSA) are later compared to **service‑level objective** clauses (ITIL) without Cross‑context aliasing.

### 11.2 Sys‑CAL × LCA‑CAL — separating *execution* vs *actuation*

* **Contexts:** *IEC 61131‑3 (run)*; *state‑space control texts (design)*.
* **Temptation:** Rename **“task execution”** to **“actuation”** “to sound control‑ish”.
* **Diagnosis:** Different Contexts; different SenseCells (program run vs control output).
* **Move:** **No rename.** Keep labels; later add **Bridge** “`execution (IEC)` *produces* signals that realise `actuation (control)`” with CL stating partial coverage.
* **Pay‑off:** Plant narratives stop calling programs “actuators”; runtime vs control semantics stay crisp.

### 11.3 Kind-CAL × Method‑CAL — false merge avoided

* **Contexts:** *OWL 2 (types, design)*; *SPEM 2.0 (methods, design)*.
* **Issue:** A row labeled **“Class”** tried to absorb **“WorkProductKind”** by a `renames`.
* **Diagnosis:** Not same sense; different calculi (type vs artefact category).
* **Move:** **Split the row**: `splits("class" ⇒ {"type‑class","work‑product‑category"})`.
* **Pay‑off:** Downstream Role Descriptions can point to the correct **SenseCell** without redefining ontological commitments.

### 11.4 Enactment × KD‑CAL — retiring a misleading metaphor

* **Context:** *BPMN 2.0 (design)*.
* **Legacy:** Team jargon **“heartbeat”** used for a **timer event**. Newcomers confuse it with **sensor heartbeats** (KD‑CAL).
* **Move:** `retires("heartbeat")` in BPMN Context with note “use **timer event**; ‘heartbeat’ refers to sensor liveness in KD‑CAL”.
* **Pay‑off:** Two different ecosystems stop colliding on the same catchy word.

### 11.5 Concept‑Set row refactor after rising CL

* **Rows:** `{“DBaaS”, “Database‑Service”}` representing service notions across several Contexts.
* **F.3 + F.9 outcome:** High CL; evidence of same Cross‑context alignment.
* **Move:** `merges({"DBaaS","Database‑Service"} ⇒ "Database‑Service")` at **row level**. Both legacy labels become row‑local aliases with epoch notes.
* **Pay‑off:** One clearer row label; old articles still understandable.

---

## 12 · Reasoning primitives (judgement schemas, notation‑free)

> Each judgement is a **pure thought**: premises ⇒ safe conclusion. No storage, no workflow, no roles.

Let **`ContextOf(ℓ)`** be the Context of label **ℓ** (when ℓ names a SenseCell); **`rowOf(ℓ)`** the Concept‑Set row (when ℓ names a row); **`senseOf(ℓ)`** the SenseCell it denotes (if local); **`pref(thing)`** the current preferred label of a SenseCell / row / Role Description.

### 12.1 Same‑sense & same‑place

`ContextOf(ℓ₁)=ContextOf(ℓ₂) ∧ senseOf(ℓ₁)=senseOf(ℓ₂) ⊢ mayRename(ℓ₁→ℓ₂)`
*Reading:* If two labels denote **the same SenseCell in the same Context**, a rename is legitimate.

### 12.2 Local alias

`ContextOf(ℓ₁)=ContextOf(ℓ₂) ∧ senseOf(ℓ₁)=senseOf(ℓ₂) ⊢ aliases(ℓ₁↔ℓ₂)`
*Reading:* Legacy synonym can be kept **as a read‑path**; writing uses `pref`.

### 12.3 Split detection

`coversMultipleLocalSenses(ℓ) ⊢ splits(ℓ ⇒ {ℓA,ℓB,...})`
*Reading:* If one label straddles several local senses, declare a split and prefer the new precise labels.

### 12.4 Merge admission

`ContextOf(ℓA)=ContextOf(ℓB) ∧ senseOf(ℓA)=senseOf(ℓB) ⊢ merges({ℓA,ℓB} ⇒ ℓN)`
*Reading:* Once F.3 shows identity of sense **within** a Context, merging labels into one preferred label is safe.

### 12.5 Retirement

`misleading(ℓ) ∧ ¬∃ℓ' sameSense(ℓ,ℓ') ⊢ retires(ℓ)`
*Reading:* If a label misleads and has **no single** successor, retire it and point readers to relevant Contexts/rows.

### 12.6 Cross‑context guard

`ContextOf(ℓ₁) ≠ ContextOf(ℓ₂) ⊢ ¬mayRename(ℓ₁→ℓ₂)`
*Reading:* Different Contexts forbid rename/alias; any relation goes to **Bridge** (F.9).

### 12.7 Writing discipline

`thing t ⊢ writeWithPreferred(t) = pref(t)`
*Reading:* Normative prose uses the **current** preferred label; aliases are for reading.

### 12.8 Reading resolution

`legacyLabel ℓ ⊢ readResolve(ℓ) = ⟨thing, pref(thing), epoch?⟩`
*Reading:* A reader can mentally resolve a legacy label to the **thing** and its present name, with epoch hint if needed.

### 12.9 Alias budget

`aliasesFor(thing, register=r) = A ⊢ |A| ≤ 1`
*Reading:* Keep at most one legacy alias per register (Tech/Plain) for any one thing.

### 12.10 Row‑level continuity

`rowOf(ℓA)=rowOf(ℓB)=R ∧ intension(R) stable ⊢ mayRenameRow(R,ℓB)`
*Reading:* A row label can change if the **row’s membership/intension** did not change; otherwise refactor rows first (F.7).

---

## 13 · Relations

**Builds on:**
F.1 **context of meaning** (keeps locality), F.2 **Harvesting** (provides attested strings), F.3 **Clustering** (establishes SenseCells), F.5 **Naming Discipline** (supplies preferred labels), F.7 **Concept‑Set rows**, F.8 **Mint‑or‑Reuse**, F.9 **Bridges**, F.10 **Status windows**, F.11 **Method harmonisation**, F.12 **Service acceptance**.

**Constrains:**

* **F.5 (Naming):** may select preferred labels **only** after applying these continuity relations.
* **F.7 (Rows):** row relabels require row **intension** stability; otherwise use **split/merge rows**.
* **F.9 (Bridges):** Cross‑context changes must **not** be expressed as renames/aliases.

**Used by.**
All Part C architheories when editions shift; all examples and tutorials when teaching with legacy terminology.

---

## 14 · Migration notes (conceptual playbook)

1. **Ask the same‑sense question first.** If the underlying **SenseCell/row** is unchanged, prefer `renames`; else reach for `splits/merges`.
2. **Keep it inside the Context.** If your explanation crosses Contexts, stop—this is **Bridge** territory (F.9), not a rename.
3. **Prefer clarity over fashion.** Rename only when the new label **removes a real ambiguity** (F.5 criteria), not to chase style.
4. **Limit nostalgia.** Admit **one** legacy alias in each register that readers will most likely meet; leave the rest to footnotes in examples.
5. **Deprecate with kindness.** When retiring a label, add a one‑line **pointer note** (e.g., “see `timer event` in BPMN; ‘heartbeat’ in KD‑CAL means sensor liveness”).
6. **Rows before names.** If a rename request coincides with a shift in what the row covers, **refactor rows** (F.7) first, then choose labels.
7. **Edition bumps.** When a canon updates, check labels used in that Context: if definitions shift, it’s a **split/merge**; if not, you may `renames` for style/uniformity.
8. **Teach the delta.** In primers, show a **mini table** with legacy → preferred pairs only where readers will encounter both.

---

## 15 · Acceptance tests (SCR/RSCR — concept‑level)

### 15.1 Static conformance (SCR)

* **SCR-F13-S01 (context-local continuity).** Every `renames/aliases` relates labels **within the same context** or the **same row/Role Description**; none cross Contexts.
* **SCR‑F13‑S02 (Truthfulness).** For each `renames`, there exists an unchanged **SenseCell/row**; otherwise the move is rejected.
* **SCR‑F13‑S03 (Alias budget).** For any one thing and register, the number of legacy aliases is **≤ 1**.
* **SCR‑F13‑S04 (Non‑retroactivity).** No requirement or suggestion to rewrite past texts is present; continuity is expressed as **read‑paths**.
* **SCR‑F13‑S05 (Row integrity).** A row rename occurs only when the row’s **intension** is stable; if membership changed, a **row split/merge** is documented (F.7).
* **SCR‑F13‑S06 (Bridge discipline).** No alias/rename is used to imply Cross‑context sameness; any such relation is deferred to **F.9**.

### 15.2 Regression (RSCR)

* **RSCR‑F13‑E01 (Edition drift audit).** When a canon edition changes, all labels from that Context are checked against definitions; moves are `renames` if senses stable, else `splits/merges`.
* **RSCR‑F13‑E02 (Alias creep check).** Periodically ensure alias budgets remain within **≤ 1 per register**; surplus aliases are pruned.
* **RSCR‑F13‑E03 (Bridge leak check).** Scan continuity notes for Cross‑context hints; any such case is converted into a **Bridge** or deleted.
* **RSCR‑F13‑E04 (Didactic continuity).** Sampling of examples shows that readers can **resolve** legacy labels to current ones without confusion (via the continuity notes).

---

## 16 · Didactic distillation (60‑second script)

> **Names are lenses.** The *thing* that persists is the **sense** (a SenseCell in a Context, a Concept‑Set row, a Role Description). When you improve a lens, use **`renames`** or **`aliases`** **inside that same place**. When the *thing* changes, say so with **`splits/merges`**—and adjust rows/Bridges accordingly. **Never rename across Contexts.** Keep at most **one** legacy alias per register. Do **not** rewrite history; give readers **read‑paths** and brief epoch notes. With this discipline, you can clarify language without erasing meaning, and your models keep both **continuity** and **truth**.

# F.14 — Anti‑Explosion Control (Roles & Statuses) \[A] 

**“Name less, express more.”**

**Status.** Architectural pattern \[A], architheory‑agnostic.
**Depends on.** F.1 **context of meaning**; F.2 **Harvesting**; F.3 **Local Sense Clustering**; F.4 **Role Description**; F.5 **Naming Discipline**; F.7 **Concept‑Set Table**; F.8 **Mint‑or‑Reuse**.
**Coordinates with.** F.10 **Status Windows & Mapping**; F.11 **Method Quartet Harmonisation**; F.12 **Service Acceptance Binding**; F.13 **Lexical Continuity**.
**Aliases (informative).** *Role/Status economy*; *Explosion guard*.

---

## 1 · Intent & applicability

**Intent.** Prevent the uncontrolled growth of **Roles** and **Statuses** by privileging **reuse**, **bundling**, **explicit separation‑of‑duties (SoD)**, and **applicability windows** over minting new names. Keep the vocabulary **small, crisp, and composable** while remaining faithful to local meanings fixed by Contexts (F.1) and SenseCells (F.3).

**Applicability.** Whenever a new Role/Status is proposed, a team merges two lines of work, or a domain shifts its jargon. Use this pattern before adding rows to the Concept‑Set Table (F.7) or new Role Descriptions (F.4).

**Non‑goals.** No org charts, no RBAC policies, no process roles. This pattern describes **mental moves** for architectural naming, not governance machinery.

---

## 2 · Problem frame

Left unchecked, Role/Status vocabularies tend to **diverge**:

1. **Synonym stacks.** *Reviewer*, *Approver*, *Validator*, *Verifier* minted separately despite overlapping responsibilities.
2. **Modifier creep.** *Night‑Operator*, *Shift‑Operator*, *Remote‑Operator* proliferate where one Role plus a window would suffice.
3. **SoD leakage.** New names invented to **evade** an intended separation (*Requestor‑Approver* as one Role).
4. **Status paintjobs.** *Compliant*, *At‑Risk*, *Grace*, *Waived*, *Temporarily‑Breached*—labels multiply where a **single Status × window** model would be clearer.
5. **Context blending.** A control‑Context *Actuator* gets treated as an Enactment *Execution* Role; a deontic *Duty* becomes a runtime *Status*.

Explosion harms didactics and increases alignment cost (F.9).

---

## 3 · Forces

| Force                           | Tension to resolve                                                                                     |
| ------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Expressiveness vs parsimony** | We must name real distinctions, but each new name increases cognitive load.                            |
| **Locality vs uniformity**      | Roles/Statuses are **context‑local**; yet we need a stable Cross‑context story through Concept‑Set rows.     |
| **Safety vs convenience**       | SoD constraints protect systems, but people seek convenience through composite roles.                  |
| **Temporal honesty**            | Many “new” Statuses are actually the **same** Status seen in different **windows** (design/run/grace). |

---

## 4 · Minimal vocabulary (this pattern only)

* **Role Description** (F.4): a **Role** (behavioural mask) or **Status** (epistemic/deontic standing) tied to a **SenseCell**.
* **Concept‑Set row** (F.7): a Cross‑context **intent** (“what we count as one thing”) aligned by SenseCells.
* **Bundle** (this pattern): a **named composition** of Role Descriptions that are meant to be used together by design (e.g., {Requester, Approver} for change control). A Bundle is a **concept**, not a package.
* **SoD Constraint** (this pattern): a **conceptual rule** stating that two Roles **must not** be played by the same Holder in the **same window**.
* **Window** (F.10): an **claim scope** (time stance, holon level, run segment) that delimits when a Role/Status holds.

---

## 5 · Core idea (didactic)

**Use four levers before minting a name:**

1. **Reuse the row.** If the intent matches an existing Concept‑Set row and the local SenseCell is already present, **use it**.
2. **Bundle, don’t blur.** When two Roles must travel together, **name the Bundle**, not a new hybrid Role.
3. **Declare SoD, don’t fuse.** When Roles must stay apart, **state the SoD** instead of minting a “super‑role.”
4. **Window, don’t multiply.** When a Status looks different across time/scale, keep **one Status** with **explicit windows**.

---

## 6 · Solution — the control cabinet (conceptual, notation‑free)

### 6.1 Reuse by row (first lever)

* **Move.** If a proposal matches the **intension** of an existing row (F.7), adopt its Role Description or add a local SenseCell **inside that row**.
* **Pay‑off.** Names don’t proliferate; Cross‑context tables stay thin.

**Example (services).** *Service‑availability‑compliance* already exists as a row. New labels *SLO‑Met* / *Uptime‑OK* **reuse** that row; SOSA/SSN Observations later feed it (F.12).

---

### 6.2 Bundle instead of hybrid (second lever)

* **Move.** When practice always pairs two Roles, define a **Bundle** `{RoleA, RoleB}`.
* **Not a hybrid.** Do **not** coin *RoleAB*; you’ll erase SoD options and obscure responsibilities.

**Example (enactment).** `{Requester, Approver}` is a Bundle. *Request‑Approver* (one Role) is **not** allowed; it contradicts intended checks.

---

### 6.3 Separate by SoD, don’t evade (third lever)

* **Move.** Record **SoD constraints** where separation matters (“Requester ⟂ Approver in run window”).
* **Why here.** SoD belongs to **semantics**, not org policy; it protects structure across Contexts and times.

**Example (methods).** `{Author ⟂ Reviewer}` in the **review window**. A proposal *Senior‑Reviewer* to “do both” is rejected; the **Bundle** remains `{Author, Reviewer}` with SoD.

---

### 6.4 Window the Status (fourth lever)

* **Move.** Keep a single Status and attach **windows** for *grace*, *evaluation*, *active*, *archival*.
* **Avoid.** *Compliant*, *At‑Risk*, *Grace* as separate Status types.

**Example (acceptance).** **Compliance** Status has readings per window:

* *evaluation window:* “pending check”,
* *active window:* “met / breached”,
* *grace window:* “temporarily tolerated breach”.
  One Status; clear windows.

---

### 6.5 Factor modifiers as facets, not names

* **Move.** Treat qualifiers (shift, locality, domain) as **facets** of the same Role/Status or as **windows**, not new types.

**Example (operations).** *Operator* with **window facet** `timeOfDay = night`—not a new Role *Night‑Operator*.

---

## 7 · Invariants (normative)

1. **context‑locality.** Each Role Description remains tied to a **SenseCell** in a **single Context** (F.3, F.4).
2. **Row preference.** New Role Descriptions **SHOULD** map to an existing row; new rows (F.7) require F.8 justification.
3. **No hybrid Roles.** If two Roles are conceptually distinct, they **must not** be fused into one to bypass SoD. Use **Bundle + SoD**.
4. **Windowed statuses.** Status proliferation across time/scale **MUST** be expressed as **windows** of a single Status family (F.10).
5. **Bundle clarity.** A Bundle **names only composition**; it does not inherit or redefine member semantics.
6. **Minimal modifier naming.** Adding a modifier to a label **MUST** pass F.5 tests; prefer facets/windows over new Role/Status names.
7. **Concept‑first.** No invariant relies on organization charts or access policies; **semantics precede governance**.

---

## 8 · Reasoning primitives (judgement schemas)

> Pure mental moves; no tools, no workflows.

Let **`rowOf(τ)`** be the Concept‑Set row of template **τ**, **`senseOf(τ)`** its SenseCell, **`win(τ)`** its window set.

1. **Row reuse admissibility**
   `intent(τₙ) ≡ intent(row r) ∧ ∃σ: senseOf(σ) in r ⊢ reuseRow(τₙ → r)`
   *Reading:* If the proposed template’s intent matches an existing row with a local SenseCell, reuse the row.

2. **Bundle recommendation**
   `alwaysTogether{α,β} ∧ distinct(α,β) ⊢ bundle({α,β})`
   *Reading:* If two distinct Roles occur together by design, name the Bundle.

3. **SoD necessity**
   `conflictRisk{α,β} ∧ sameHolder ∧ sameWindow ⊢ SoD(α ⟂ β)`
   *Reading:* If the same Holder in the same window would create a conflict, require SoD.

4. **Hybrid rejection**
   `SoD(α ⟂ β) ⊢ forbid(hybrid(α,β))`
   *Reading:* A SoD pair cannot be fused into one Role.

5. **Windowing over multiplication**
   `status σ showsVariantsAcross(w₁,…,wₖ) ⊢ keepOneStatus(σ) ∧ win(σ)={w₁,…,wₖ}`
   *Reading:* Variants across time/scale become windows, not new Status names.

6. **Facet over rename**
   `modifier m changes circumstance ¬ essence ⊢ preferFacet(τ,m)`
   *Reading:* If a modifier alters circumstances only, represent it as a facet/window.

---

## 9 · Micro‑examples (engineer / manager / researcher lenses)

### 9.1 Enactment (change control)

* **Proposal.** *Requester‑Approver* as a single Role “to move faster.”
* **Moves.** SoD(`Requester ⟂ Approver`) + **Bundle** `{Requester, Approver}`.
* **Result.** Same throughput, preserved checks, no hybrid Role.

### 9.2 Services (SLO evaluation)

* **Proposal.** New Status *At‑Risk*.
* **Moves.** Keep **Compliance** Status; add **grace window** and a **forecast facet** (informative) if needed.
* **Result.** One Status with windows; fewer names, clearer timelines.

### 9.3 KD‑CAL (evidence)

* **Proposal.** *Pre‑validated* between *Verified* and *Validated*.
* **Moves.** Use **Status chain** within one family: `Verified → Validated`; represent uncertainty as **confidence** (F.10), not another Status.
* **Result.** Clean ladder; no extra label.

### 9.4 Sys‑CAL (plant ops)

* **Proposal.** *Night‑Operator*, *Remote‑Operator*.
* **Moves.** **Role:** Operator; **facets/windows:** `timeOfDay`, `presenceMode`.
* **Result.** One Role, portable qualifiers.

### 9.5 Method quartet (reviews)

* **Proposal.** *Senior‑Reviewer* to bypass `{Author ⟂ Reviewer}`.
* **Moves.** Keep SoD; if seniority matters, introduce **Assurance Level** facet (F.10) on the **review decision**, not a new Role.
* **Result.** Separation preserved; trust expressed as a Status property, not a Role type.

## 10 · Anti‑patterns & remedies

| #       | Anti‑pattern                             | Symptom in models                                                                            | Why it harms thinking                                             | Remedy (conceptual move)                                                                                                          |
| ------- | ---------------------------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **A1**  | **Hybrid Role minting**                  | *Request‑Approver*, *Dev‑Ops‑Engineer* as one Role.                                          | Erases intended checks; conceals distinct responsibilities.       | **Bundle** `{Requester, Approver}` + **SoD** (`Requester ⟂ Approver`). Keep Roles distinct; name the cooperation, not the fusion. |
| **A2**  | **Modifier‑as‑type**                     | *Night‑Operator*, *Remote‑Operator*, *On‑call‑Reviewer*.                                     | Name proliferation for circumstantial qualifiers.                 | Keep **Role = Operator/Reviewer**; express *night/remote/on‑call* as **facets or windows** (F.10).                                |
| **A3**  | **Window‑as‑type**                       | *Compliant*, *At‑Risk*, *Grace*, *Breached* as separate Status types.                        | Paints temporal phases as different essences; breaks comparisons. | One **Status family** (e.g., **Compliance**) with **windows**: *evaluation / active / grace / archival* (F.10).                   |
| **A4**  | **Row drift**                            | New Concept‑Set row for *Uptime‑OK* when **Service‑Availability‑Compliance** already exists. | Splits one intent across rows; Cross‑context tables get wide.        | **Reuse the row** (F.7) if intent matches; add local **SenseCell** if needed.                                                     |
| **A5**  | **SoD evasion via “trusted” super‑role** | *Senior‑Reviewer* allowed to both author and review.                                         | Conflicts of interest reintroduced under prestige.                | Keep **SoD(Author ⟂ Reviewer)**; if trust matters, attach **Assurance Level** to the *decision* (Status facet), not a new Role.   |
| **A6**  | **cross-context fusion**                    | One Role Description mixes *Execution (IEC)* with *Duty (ODRL)* semantics.                       | Violates locality; meanings leak across Contexts.                    | Keep each **Role Description** tied to a **SenseCell** (F.4). cross-context reasoning uses **Bridge** (F.9).         |
| **A7**  | **Synonym carousel**                     | *Validator* vs *Verifier* vs *Checker* minted separately in the same Context.                   | Cognitive noise; ambiguous separation.                            | Choose **one label** via F.5; keep others as **aliases** in **Lexical Continuity** (F.13), not new templates.                     |
| **A8**  | **Org-chart mirroring**                  | Roles cloned from a company chart (*Squad-Lead*, *Tribe-Lead*) as generic **Role Descriptions**. | Organisation-specific names masquerade as semantics.              | Map local titles to **Bundles** of generic Roles (e.g., `{Planner, Coordinator}`), or treat as **aliases** (F.13). |
| **A9**  | **KPI‑as‑Status inflation**              | *Latency‑Good*, *Latency‑Bad*, *Latency‑Poor* as Status types.                               | Encodes numeric thresholds as separate essences; brittle.         | One **Quality Status** with **metric threshold** in its window definition (F.10/F.12); keep adjectives out of type names.         |
| **A10** | **Traffic‑light mania**                  | *Red/Amber/Green* Status types reused across unrelated families.                             | False unification across different intents; color ≠ meaning.      | Keep canonical **Status name** (e.g., **Compliance**); use **presentation** as a separate concern; colors are not types.          |
| **A11** | **Bundle masquerading as Role**          | *Change‑Manager* invented to hide `{Requester, Approver, Implementer}`.                      | Collapses structure; SoD becomes optional.                        | Name the **Bundle** and its **SoD** explicitly; keep Roles atomic.                                                                |
| **A12** | **State‑as‑Status sprawl**           | *Pre‑validated*, *Validated*, *Re‑validated*, *De‑validated*.                                | States are temporal positions on one ladder.                      | Define one **Validation Status** with **state ladder** and **windows**; use **Assurance Level** as a facet if needed.             |
| **A13** | **Contextless Role Description**            | Role Description without a SenseCell anchor.                                                     | Floating meaning; later bridges cannot be made explicit.          | Tie every **Role Description** to a **SenseCell** (F.4). If none fits, use F.8 to decide: **new row** or **rename/reuse**.        |
| **A14** | **Profile‑driven clones**                | *API‑Approver*, *Data‑Approver*, *Model‑Approver* as different Roles.                        | Scales by surface area; loses the shared essence.                 | One **Approver** Role with a **scope facet** (`objectType=API/Data/Model`).                                                       |

---

## 11 · Worked examples (multi‑architheory)

### 11.1 Enactment + Services + KD‑CAL — “SLO compliance without label sprawl”

**Contexts.** ITIL 4 (services), SOSA/SSN (sensing), PROV‑O (run).
**Intent.** Track SLO compliance with minimal Status vocabulary.

* **Naïve proposal.** Statuses: *Compliant*, *At‑Risk*, *Breached*, *Grace*, *Waived*.
* **Moves (F.14).** Keep **Compliance** as one **Status family**; define **windows**: *evaluation* (prediction against forecast), *active* (actuals vs target), *grace* (tolerated breach). **Waiver** becomes a **deontic Status** in ODRL Context, not part of Compliance.
* **Outcome.** One Status + windows; observations (SOSA) and provenance (PROV) feed the *active* window; service policy (ITIL/ODRL) defines *grace*.

### 11.2 Method‑CAL + Enactment — “Reviews with SoD and Bundle”

**Contexts.** SPEM/ISO 24744 (methods), Enactment lexicon.
**Intent.** Prevent authors reviewing their own work while keeping names lean.

* **Naïve proposal.** Roles: *Author*, *Self‑Reviewer*, *Peer‑Reviewer*, *Senior‑Reviewer*.
* **Moves.** Roles **Author**, **Reviewer** only; **SoD(Author ⟂ Reviewer)** in the **review window**. If practice needs two reviewers, mint **Bundle** `{Reviewer, Reviewer₂}`; express **seniority** as a **facet** on the *decision* (Assurance Level), not a new Role.
* **Outcome.** Two Roles, one Bundle, one SoD; no hybrid Role; assurance is visible as a property of the review result.

### 11.3 Sys‑CAL + LCA‑CAL + Services — “Operations without role fragments”

**Contexts.** IEC 61131‑3 (execution), state‑space control texts (actuation), ITIL 4 (services).
**Intent.** Staff coverage across shifts and locations without ten operator types.

* **Naïve proposal.** *Night‑Operator*, *Remote‑Operator*, *Local‑Operator*, *Shift‑Lead*, *On‑call‑Operator*.
* **Moves.** **Role** = **Operator**; add **facets/windows**: `timeOfDay`, `presenceMode`, `dutyCycle`. If coordination is distinct, mint **Coordinator** Role; when both occur together, **Bundle** `{Operator, Coordinator}`; keep **SoD** where needed (e.g., `Operator ⟂ Approver` for production change).
* **Outcome.** One Role + small facet set + Bundle; clean hooks to execution and actuation semantics.

### 11.4 KD‑CAL + Kind-CAL — “Evidence ladder without new labels”

**Contexts.** KD‑CAL (evidence), OWL 2/FCA (types).
**Intent.** Express proof maturity without inflating Status names.

* **Naïve proposal.** *Candidate‑Evidence*, *Preliminary‑Evidence*, *Verified‑Evidence*, *Validated‑Evidence*.
* **Moves.** Keep one **Evidence Status** ladder (`Collected → Verified → Validated`); use **Assurance Level** facet (numeric or ordinal) and **windows** for in‑review vs active. Align *types* in a **row**; do not mint new Status names for granularity.
* **Outcome.** Short vocabulary, clear ladder, quantitative facet where nuance is needed.

---

## 12 · Relations (with other patterns)

* **Builds on:** F.1 (Contexts), F.2 (Harvesting), F.3 (Local Clustering), F.4 (Role Description), F.5 (Naming).
* **Constrains:**

  * **F.7 (Concept‑Set Table):** prefer **row reuse**; new rows require F.8 justification.
  * **F.8 (Mint‑or‑Reuse):** apply **four levers** (reuse, bundle, SoD, window) before minting.
  * **F.10 (Status Windows & Mapping):** encode temporal/scale variation as **windows**, not new Status types.
  * **F.12 (Service Acceptance Binding):** bind acceptance to the **Compliance** Status family; avoid ad‑hoc status labels.
  * **F.13 (Lexical Continuity):** prior names become **aliases**; do not carry forward inflated vocabularies as new types.
* **Used by.** Architheory examples across Part C to keep Role/Status vocabularies tight.

---

## 13 · Migration notes (conceptual playbook)

1. **Map to rows.** For each existing Role/Status, identify its **Concept‑Set row**; if two names share an intent, **collapse** to one row (keep other names as **aliases**, F.13).
2. **Extract SoD.** Replace “super‑roles” with **Bundles** plus explicit **SoD**; where conflict exists, SoD is **normative**, not cultural.
3. **Demote modifiers.** Convert adjectival Role types into **U.Facet** (per Compose‑CAL) or **windows** on the base Role.
4. **Window statuses.** Merge Status families split by time/scale into **one Status + windows**; move waived/exempt notions to the **deontic Context** if applicable.
5. **Re‑use before minting.** When encountering a gap, scan rows for a near‑match; only if intent genuinely differs, open a **new row** (F.8).
6. **Preserve continuity.** Keep historic labels as **aliases** under the consolidated template (F.13); do not rewrite past texts.
7. **Rehearse the cut.** After consolidation, you should be able to recite the entire Role/Status vocabulary **from memory**; if not, reduce again.

---

## 14 · Acceptance tests (SCR/RSCR — concept‑level)

### 14.1 SCR — Static conformance

* **SCR‑F14‑S01 (Row reuse).** Every newly proposed Role Description either **references an existing row** or includes a clear **F.8 justification** for a new row.
* **SCR‑F14‑S02 (No hybrids).** No Role Description’s label or definition **conflates** two Roles that stand in a declared **SoD** relation.
* **SCR‑F14‑S03 (Windowed statuses).** Each Status family that shows temporal/scale variation is expressed as **one Status + windows** (not multiple Status types).
* **SCR‑F14‑S04 (Facet over modifier).** Role names do not encode circumstantial modifiers; such modifiers appear only as **facets/windows**.
* **SCR‑F14‑S05 (Context locality).** Every Role Description is anchored to **exactly one SenseCell**; no Cross‑context semantics inside a single template.
* **SCR‑F14‑S06 (Bundles are pure).** Every **Bundle** is a **set of templates** with **no additional semantics** beyond membership and referenced **SoD**.

### 14.2 RSCR — Regression (evolution)

* **RSCR‑F14‑E01 (Vocabulary slope).** Over a given interval, the count of distinct Role/Status templates **does not increase** unless matched by **row justifications** (F.8).
* **RSCR‑F14‑E02 (SoD integrity).** Adding templates does not introduce a label that **circumvents** any existing **SoD** relation.
* **RSCR‑F14‑E03 (Window integrity).** When windows are refined, **Status type count** remains constant; only window definitions change.
* **RSCR‑F14‑E04 (Alias discipline).** When labels change, prior names are recorded as **aliases** (F.13); no silent type multiplication.

---

## 15 · Didactic distillation (90‑second script)

> **Name less, express more.** Before minting a new Role or Status, try **four levers**:
> **(1) Reuse the row** — if the intent already exists, adopt it and add your local SenseCell.
> **(2) Bundle, don’t blur** — when two Roles travel together, **Bundle** them; keep **SoD** if they must stay apart.
> **(3) Declare SoD, don’t fuse** — conflicts of interest are solved with **SoD**, not with “trusted” super‑roles.
> **(4) Window, don’t multiply** — one **Status** can wear different **windows** (evaluation/active/grace); that’s not four Status types.
> Keep modifiers as **facets**, not names; keep every Role Description **context‑local** via its SenseCell. If your vocabulary no longer fits in a thoughtful mind, you have an **explosion**—return to the levers and reduce.

# F.15 — SCR/RSCR Harness for Unification \[A] 

**“Prove locality and parsimony first; only then prove composition.”**
**Status.** Architectural pattern \[A], architheory‑agnostic.
**Builds on:** E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; F.0.1 **Foundational Principles**; F.1–F.14.
**Coordinates with.** B.3 **Trust & Assurance Calculus** (for CL use on Bridges).

---

## 1 · Intent & applicability

**Intent.** Provide a **minimal, notation‑free harness of conceptual checks** that tells you whether a unification slice is **sound**: Contexts are fixed and diverse (F.1), terms are harvested and clustered **inside** Contexts (F.2–F.3), Role Descriptions **point to one SenseCell** (F.4), names obey discipline (F.5), rows are reused instead of multiplied (F.7–F.8), bridges are **explicit and penalised** (F.9), statuses vary by **windows** not type proliferation (F.10), and cross‑line bindings (F.11–F.12) respect locality.
**Applicability.** Use whenever you declare or revise any of: Context cards, Local‑Senses, SenseCells, Concept‑Set rows, Role Descriptions, Bridges, Status windows.
**Non‑goals.** No registries, workflows, or storage formats. No team roles. No metrics dashboards. This is **thinking discipline**, not governance.

---

## 2 · Problem frame

Without a unification harness:

1. **Locality leaks.** Cross‑context equivalence creeps in “by name”.
2. **Row sprawl.** Concept‑Set tables grow laterally with near‑duplicates.
3. **Role/Status inflation.** Adjectival or temporal variants become new types.
4. **Silent rewrites.** New editions overwrite old meanings without a trace.
5. **Unstable bridges.** Cross‑context relations harden into dogma without CL or loss statements.

---

## 3 · Forces

| Force                      | Tension to resolve                                                    |
| -------------------------- | --------------------------------------------------------------------- |
| **Parsimony vs coverage**  | Keep vocabularies small yet expressive across multiple Contexts.         |
| **Locality vs reuse**      | Preserve context‑local meaning while enabling Cross‑context comparison.     |
| **Stability vs evolution** | Allow new editions and rows without erasing prior sense.              |
| **Clarity vs formality**   | Checks must be teachable in minutes yet strong enough to catch drift. |

---

## 4 · Core idea (didactic)

The harness is a **two‑tier net of assertions**:

* **SCR — Static Conformance Rules.** context‑local and cross‑artefact checks that must hold **now**.
* **RSCR — Regression & Stability Rules.** Checks that must hold **across changes** (editions, rows, names).

All checks are expressed as **judgement schemas** (premises ⊢ conclusion). They **never** prescribe artefact formats, roles, or workflows.

---

## 5 · Minimal vocabulary (this pattern only)

* **Unification line (L).** The thematic cut you are pursuing (e.g., Enactment + Sensing + Execution).
* **Check.** A content‑level assertion about Contexts, senses, rows, Role Descriptions, bridges, or windows.
* **Witness.** A **thoughtful minimal example** that makes a check concrete (e.g., one seed, one bridge pair).
* **Slice.** The small set of objects under scrutiny together (Contexts in view, the row you’re adding, the Role Description that uses it, and any bridge it needs).

---

## 6 · Objects under check

1. **Contexts** — `U.BoundedContext` cards (F.1).
2. **Local‑Sense** — clustered sense inside one context (F.3).
3. **SenseCell** — *(Context × Local‑Sense)* address (F.3/F.4).
4. **Concept‑Set row** — a cross‑projection hypothesis of “the same thing” (F.7).
5. **Role Description** — Role/Status definition pointing to **one** SenseCell (F.4).
6. **Bridge** — explicit Cross‑context relation with CL and loss notes (F.9).
7. **Windows** — temporal/scale views for a Status family (F.10).
8. **Aliases** — name continuity commitments (F.13).
9. **Bundles & SoD** — reuse levers that replace hybrid roles (F.14).

---

## 7 · Solution overview — the harness as a lattice of checks

The harness arranges checks in three clusters:

* **S‑Local.** context‑local sanity (anchoring, clustering, two‑register labels).
* **S-Cross.** Cross-artefact coherence (row reuse, single-cell **Role Description**, bridge discipline, window honesty).
* **R‑Evo.** Evolution continuity (no silent rewrites, no vocabulary creep, bridge re‑validation).

This Part 1 enumerates **SCR** (S‑Local and S‑Cross). Part 2 covers **RSCR**, anti‑patterns, worked “dry runs”, and acceptance summaries.

---

## 8 · SCR — Static conformance rules (S‑Local)

> All S‑Local rules are **Context‑internal** and derive only from F.1–F.5.

**SCR‑F15‑S1 (Anchored term).**
`Seed σ has context C ⊢ C ∈ Contexts(L)`
*Reading:* Every harvested seed lives in a Context that is **deliberately in view** for your line (F.1, F.2).

**SCR‑F15‑S2 (Edition trace).**
`Occurrence ω supports σ ⊢ ω carries edition+location`
*Reading:* A Local‑Sense can be mentally reconstructed from attestations (F.2).

**SCR‑F15‑S3 (Intra‑Context clustering).**
`Local‑Sense λ clusters {σᵢ} ⊢ ∀i: context(σᵢ)=context(λ)`
*Reading:* No Cross‑context items inside a Local‑Sense (F.3).

**SCR‑F15‑S4 (Two registers).**
`Local‑Sense λ ⊢ label(λ)=⟨tech,plain, symbol?⟩ ∧ plain≠∅ ∧ tech≠∅`
*Reading:* Both engineering and plain labels exist; symbol (if any) is purely informative (F.2/F.3/F.5).

**SCR‑F15‑S5 (Minimal gloss).**
`gloss(λ) framed at minimal necessary generality`
*Reading:* The gloss neither smuggles behaviour/deontics nor globalises the sense (F.2/F.5).

**SCR‑F15‑S6 (Context‑local normal form).**
`normalize_C(surface)=n ⊢ n used only within C`
*Reading:* No global normal form at this stage (F.2).

---

## 9 · SCR — Static conformance rules (S‑Cross)

> S‑Cross rules tie Contexts, rows, Role Descriptions, bridges, and windows together **without** breaking locality.

**SCR-F15-S7 (Single-cell Role Description).**
`Role Description τ ⊢ anchor(τ)=one SenseCell ⟨C,λ⟩`
*Reading:* Every Role Description points to exactly **one** SenseCell; no mixed semantics (F.4).

**SCR-F15-S8 (Name discipline).**
`Role Description τ ⊢ name(τ) obeys F.5`
*Reading:* Labels follow the agreed morphology, register pairing, and minimal generality (F.5).

**SCR‑F15‑S9 (Row sufficiency).**
`Row ρ lists cells {⟨Cᵢ,λᵢ⟩} ⊢ |distinct(Cᵢ)| ≥ 2`
*Reading:* A row is meaningful only if it spans **at least two Contexts** (F.7).

**SCR‑F15‑S10 (Row purity).**
`Row ρ ⊢ no cell contains Cross‑context clustering`
*Reading:* Each cell is a **single** SenseCell, not a pre‑merged bundle (F.7).

**SCR‑F15‑S11 (Reuse before mint).**
`Proposed row ρ' overlaps intent(ρ) ⊢ prefer reuse(ρ) ∨ document F.8 decision`
*Reading:* Rows are reused by default; new rows require a mint‑or‑reuse rationale (F.7–F.8).

**SCR‑F15‑S12 (Bridge is explicit).**
`C₁≠C₂ ∧ relation asserted between λ₁,λ₂ ⊢ Bridge β: ⟨⟨C₁,λ₁⟩ ↔ ⟨C₂,λ₂⟩, kind, CL, loss⟩`
*Reading:* Cross‑context relations appear **only** as Bridges with declared kind (≡, ⊑, ⊒, ⟂), Congruence Level, and loss notes (F.9; B.3 for CL semantics).

**SCR‑F15‑S13 (Bridge locality).**
`Bridge β ⊢ cells belong to different Contexts`
*Reading:* You never bridge **within** a Context; that’s clustering (F.3/F.9).

**SCR‑F15‑S14 (Window honesty).**
`Status family Σ varies by time/scale ⊢ windows(Σ) define variation; no new Status types introduced`
*Reading:* Temporal and scale variation appears as **windows**, not as new types (F.10).

**SCR-F15-S15 (SoD preservation).**
`Bundle B = {τ₁,τ₂,…} with SoD(τᵢ ⟂ τⱼ) ⊢ no single **Role Description** fuses τᵢ,τⱼ`
*Reading:* Separation‑of‑Duties is a **normative constraint**, not a label tweak (F.14).

**SCR‑F15‑S16 (Binding coherence).**
`Service‑Acceptance binding references Status Σ and Execution E ⊢ Σ anchored; E anchored; comparison defined via Bridge(s) if Cross‑context`
*Reading:* Acceptance compares **anchored** executions and statuses, with any Cross‑context step made explicit (F.12 + F.9).

> **SCR/RSCR “Twin Harness” tests**

**SCR‑TWIN‑01 · Head term check.** Plain twin preserves/declares the head per **CC‑TWIN‑3**.  
**SCR‑TWIN‑02 · Kind check.** Plain twin maps to the same **Kind** as the Tech name (C.3).  
**SCR‑TWIN‑03 · SenseCell check.** Twin and Tech resolve to the same **SenseCell**; record counter‑example(s).  
**SCR‑TWIN‑04 · Stop‑list check.** If the base noun is in the **Ambiguity stop‑list**, require bracketed head + gloss or **fail**.  
**SCR‑TWIN‑05 · Normative surface check.** No plain twins in CC blocks, signatures, or acceptance clauses.  
**RSCR‑TWIN‑06 · Drift audit.** On Context or glossary edits, re‑run twin harness; degrade or deprecate if SenseFidelity falls.  
**RSCR‑TWIN‑07 · Bridge audit.** If a twin is copied across Contexts, ensure a **Bridge** exists; record **CL** and loss notes.

 > **Examples & Anti‑examples**

**Good (role with head):**
* Tech: `TransformerRole` → Plain: **“Transformer (role)”** — passes Head & Kind checks.
*  Tech: `IncidentCommanderRole` → Plain: **“Incident commander (role)”**.

**Good (episteme status with head):**
* Tech: `U.EvidenceRole` → Plain: **“Evidence (status)”** — first mention includes head.

**Borderline (allowed with gloss):**
* Tech: `U.Episteme` → Plain: **“Tradition (episteme)”** — **only** with first‑use gloss, e.g., _“Tradition (episteme) \[U.Episteme\] — a body of knowledge within IAU\_2006”_. (Without the head/gloss this is **forbidden** due to ambiguity.) 

**Forbidden:**
* Tech: `U.Episteme` → Plain: **“Tradition”** (bare) — fails **CC‑TWIN‑4/5**.
* Tech: `U.Service` → Plain: **“API”** — fails Kind and head checks (API is an access **method**, not the **promise**).
* Tech: `U.RoleAssignment` → Plain: **“Appointment”** — banned term; conflates governance speech‑act with the binding object.

> **Migration guidance (lightweight)**
1.  **Inventory.** List current plain twins per Context.
2.  **Score.** Assign **SenseFidelity** (0–3) and add counter‑examples; demote or deprecate any with score <2.
3.  **Head & gloss.** Add bracketed heads and first‑use glosses for all surviving twins.
4.  **Register.** Create/update entries in **E.10.P**; link a **DRR** for each change.
5.  **Lint.** Enable the **Twin Harness** in CI to block new ambiguous twins.

## 10 · Judgement schemas (core moves)

> Representative mental moves; each “fires” one cluster of SCRs.

1. **Anchoring**
   `Seed σ : context C, C ∈ Contexts(L) ⊢ anchored(σ)`  *(S1)*

2. **Local clustering**
   `∀σ∈Σ: context(σ)=C ⊢ cluster_C(Σ) = Local‑Sense λ`  *(S3)*

3. **Role-Description anchoring**
   `Role Description τ names ⟨C,λ⟩ ⊢ singleCell(τ)`  *(S7)*

4. **Row reuse**
   `intent(ρ') ≈ intent(ρ) ⊢ reuse(ρ) ∨ justify_mint(ρ')`  *(S11)*

5. **Bridge assertion**
   `C₁≠C₂ ∧ compare(⟨C₁,λ₁⟩,⟨C₂,λ₂⟩) ⊢ Bridge(CL,kind,loss)`  *(S12–S13)*

6. **Windowing**
   `Status Σ exhibits temporal/scale variance ⊢ define windows(Σ); forbid Σ‑splitting`  *(S14)*

7. **SoD guard**
  `SoD(τᵢ ⟂ τⱼ) ⊢ ¬exists Role Description υ that conflates {τᵢ,τⱼ}`  *(S15)*

---

## 11 · Micro‑witnesses (illustrative)

**11.1 Activity vs Task (PROV‑O ↔ IEC 61131‑3).**
Contexts: `PROV‑O (run)`, `IEC 61131‑3 (run)`.
Local‑Senses: *activity(prov)*, *task(iec)*.
*Fire:* S7 (**Role Description** “Execution” points to **one SenseCell**), S12 (Bridge: **overlap**, CL=2, loss: *IEC task may be cyclic; PROV activity need not be periodic*), S13 (Contexts differ), S14 (Status windows for compliance later, not new types).

**11.2 Service Acceptance (ITIL 4 ↔ SOSA/SSN).**
Contexts: `ITIL 4 (design)`, `SOSA/SSN (run)`.
Row: **Service‑Availability** with cells ⟨ITIL\:SLO availability⟩, ⟨SOSA\:observation of uptime⟩.
*Fire:* S9 (row spans ≥2 Contexts), S12 (Bridge kind: *measure-for-target*, CL=3, loss: *sampling bias*), S16 (binding coherence), **S-RoleDesc-SingleCell**.


## 12 · Relations (with other patterns)

**Builds on:** E.10.D1 (Context semantics), F.1–F.14.
**Constrains:** Any addition to F.1–F.14 is **publish‑ready** only if all relevant **SCR** here evaluate **true** on its slice.
**Feed:** B.3 may use Bridge CL and loss notes to adjust assurance.

## 13 · RSCR — Regression & Stability Rules (R‑Evo)

> These rules speak about **changes over time**. They are expressed as **judgement schemas** that compare two conceptual snapshots: `@t0` and `@t1`. No storage, no workflows—just content assertions.

**Notation.**
`X@t0` — object X before change • `X@t1` — after change • `Δ(X)=⟨…⟩` — described difference • `same(…) / new(…) / retired(…)` — conceptual status.

---

### 13.1 Contexts & editions

**RSCR‑F15‑E1 (No silent replacement).**
`Context C@t0 : edition e0, C@t1 : edition e1, e1≠e0 ⊢ either newContext(C,e1) ∨ explicitRecency(C,e1)`
*Reading:* A new edition becomes a **new Context** if sense shifts; otherwise keep one context and mark recency. Never overwrite meaning.

**RSCR‑F15‑E2 (Trip‑wire carry‑over).**
`C@t1 derives from C@t0 ⊢ tripWires(C@t1) ⊇ review(tripWires(C@t0))`
*Reading:* Known confusions are re‑checked and re‑stated (or explicitly dropped with a sentence why).

---

### 13.2 Local‑Senses & SenseCells

**RSCR‑F15‑E3 (Reconstitutable seeds).**
`Local‑Sense λ@t0, Δ(occurrences) → λ@t1 ⊢ λ@t1 still reconstructible from attestations@t1`
*Reading:* After changes in attestations, the Local‑Sense remains **auditably rebuildable**.

**RSCR‑F15‑E4 (No Cross‑context creep).**
`SenseCell ⟨C,λ⟩@t0 → @t1 ⊢ context(λ@t1)=C`
*Reading:* A SenseCell never migrates across Contexts through edits.

---

### 13.3 Concept‑Set rows

**RSCR‑F15‑E5 (Row identity).**
`Row ρ@t0 with cells {⟨Cᵢ,λᵢ⟩} → ρ@t1 with {⟨Cᵢ,λᵢ'⟩} ⊢ ρ “same” iff intent(λᵢ')≈intent(λᵢ) ∀i`
*Reading:* A row is the **same** row only if each cell still means *the same thing* in its Context. Otherwise, mint a **new row** and retire the old (F.7–F.8).

**RSCR‑F15‑E6 (Row shrink‑before‑split).**
`ρ@t1 loses a cell due to edition split ⊢ prefer keep ρ@t0 + add new row ρ' rather than mutating ρ silently`
*Reading:* When a Context splits meaning, preserve history: **add** instead of rewriting.

---

### 13.4 Role Descriptions (Role/Status)

**RSCR-F15-E7 (Single-cell continuity).**
`Role Description τ@t0 → τ@t1 ⊢ anchor(τ@t1)=one SenseCell ∧ (sameCell ∨ justifiedSwitch)`
*Reading:* A **Role Description** keeps pointing to **one** SenseCell; switching cells requires a **one-sentence** rationale tied to the row you reuse (F.4, F.8).

**RSCR-F15-E8 (Alias-then-rename).**
`name(τ@t0) → name(τ@t1) ⊢ create alias(name@t0→name@t1) unless semantics changed`
*Reading:* If only the **name** improves, create an **Alias** (F.13). If semantics change, **mint a new Role Description** instead.

---

### 13.5 Bridges

**RSCR‑F15‑E9 (Re‑validate on movement).**
`Bridge β: ⟨⟨C₁,λ₁⟩ ↔ ⟨C₂,λ₂⟩, CL, loss⟩ @t0; any λᵢ mutates @t1 ⊢ β re‑examined; CL may drop; loss updated`
*Reading:* Any end‑cell change **forces** a fresh look; default is **more caution** (CL non‑increasing unless newly justified).

**RSCR‑F15‑E10 (No bridge drift to identity).**
`series of edits turns β(kind≠≡) → β(kind=≡) ⊢ require new witness set`
*Reading:* Equivalence (≡) is special: it needs a **fresh witness**; you cannot slide into ≡ by minor edits.

---

### 13.6 Status windows & SoD

**RSCR‑F15‑E11 (Window stability).**
`Status family Σ windows@t0 → @t1 ⊢ window set changes only if variance‑of‑meaning is shown`
*Reading:* Add or remove windows **only** when meaning genuinely varies across time/scale—never for convenience (F.10).

**RSCR‑F15‑E12 (SoD invariance).**
`SoD(τᵢ ⟂ τⱼ) @t0 → @t1 ⊢ SoD preserved; no new Role Description conflates τᵢ,τⱼ`
*Reading:* Separation‑of‑Duties remains in force through changes (F.14).

---

## 14 · Anti‑patterns the harness catches (and the fix)

| Code   | Anti‑pattern            | Symptom                                  | Why it breaks                         | Harness catch → Fix                                                                              |
| ------ | ----------------------- | ---------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **H1** | **Row‑of‑one**          | Row spans a single Context                  | No cross‑projection; fake unification | **S9** fails → either add the second cell or drop the row                                        |
| **H2** | **Bridge‑by‑name**      | “Same name” assumed across Contexts         | Imports meaning; hides loss           | **S12** missing → assert an explicit Bridge with CL+loss or withdraw the claim                   |
| **H3** | **Silent edition swap** | “BPMN” changed to 2.0 → 2.1 without note | Retcons past statements               | **E1** fails → mint a new Context or mark recency; never overwrite                                  |
| **H4** | **Locality blur**       | Local‑Sense mixes two Contexts              | Cross‑context clustering                 | **S3/S6** fail → split back by Context; keep per‑Context normal forms                                  |
| **H5** | **Window‑as‑type**      | New Status type for weekend vs weekday   | Type inflation; hides time stance     | **S14/E11** fail → represent as windows, not types                                               |
| **H6** | **SoD bypass**          | Bundle fuses mutually exclusive roles    | Hidden duty conflict                  | **S15/E12** fail → keep roles separate; use Bundle only as reuse map                             |
| **H7** | **Alias-as-merge**      | Alias used to smuggle semantic change    | Loses history; misleads readers       | **E8** fails → if semantics changed, mint new Role Description; keep old with alias note only for pure rename |
| **H8** | **CL optimism**         | Most Bridges set to high CL by default   | Over‑trust; brittle reuse             | **E9/E10** → demand witnesses; prefer conservative CL                                            |

---

## 15 · Worked “dry‑runs” (composite slices)

> Each dry‑run shows **how the checks fire** when something evolves. These are **thinking rehearsals**, not procedures.

### 15.1 New edition of ITIL (services) arrives

**Slice.** Contexts: ITIL 4(2020)@t0 → ITIL 4(2024)@t1; Row: *Service-Availability*; **Role Description**: `AvailabilityStatus`; Bridges: to SOSA/SSN observations.

**Fire.**
E1 (**no silent replacement**): decide **new Context** ITIL 4(2024) because SLO definitions narrowed.
E5 (**row identity**): row *Service‑Availability*@t1 **new** (cells now ⟨ITIL2024\:SLO⟩ + ⟨SOSA\:obs⟩). Retire old row with note.
E9 (**bridge re‑validate**): sampling assumptions changed → **lower CL** by one and update loss note (*new calc window*).
E7 (**single-cell Role Description**): `AvailabilityStatus` still points to exactly one cell (ITIL2024\:SLO). Name unchanged → **no alias** needed.

**Pay‑off.** History is preserved; reuse remains safe; acceptance bindings (F.12) still compare anchored things.

---

### 15.2 Rename a Role Description without changing meaning

**Slice.** **Role Description** `IncidentStatus`@t0 → `ServiceIncidentStatus`@t1; same SenseCell.

**Fire.**
E8 (**alias‑then‑rename**): create **Alias** `IncidentStatus → ServiceIncidentStatus` (F.13).
S8 (**name discipline**): new name fits the suffix rules (F.5).

**Pay‑off.** Readers find both names; semantics untouched.

---

### 15.3 Tighten a Bridge (weak overlap → equivalence)

**Slice.** Bridge β between ⟨OWL\:subclass⟩ and ⟨FCA\:order‑edge⟩ was *overlap, CL=2*. New formal result proves equivalence in the covered fragment.

**Fire.**
E10 (**no drift to identity**): to move from overlap→≡, present a **new witness set** (fragment constraints).
S12 (**bridge explicit**): update β(kind=≡, CL=3) with precise scope/loss (“only within acyclic concept lattices with…”)

**Pay‑off.** Equivalence is **scoped and auditable**, not hand‑waved.

---

### 15.4 Window misuse detected

**Slice.** Team proposes *PeakHoursAvailabilityStatus* as a new Status type.

**Fire.**
S14/E11 (**window honesty**): reject new type; define a **window** for *peak hours* on `AvailabilityStatus`.

**Pay‑off.** No type explosion; the evaluation logic in F.12 stays uniform.

---

## 16 · Migration cues (conceptual)

1. **When in doubt, fork—not overwrite.** New edition? **Add a Context** unless you can argue sense identity in one sentence.
2. **Name pain → aliases, not merges.** If a label confuses, **rename with an alias**; if meaning changed, **mint new**.
3. **Rows age gracefully.** Never retrofit a row; **retire and re‑row** when any cell’s sense shifts.
4. **Bridges get colder over time.** Prefer to **lower CL** when editions drift; raising CL needs fresh witnesses.
5. **Windows absorb variation.** Resist splitting Status types; **window** by time/scale/phase.
6. **Guard SoD early.** When binding composite responsibilities (F.14), check SoD before naming.
7. **Teach the delta.** When things evolve, write one‑breath deltas (“what changed, why it matters”) as part of the example narrative—no registries implied.

---

## 17 · Acceptance summary (“Harness green”)

A unification slice is **publish‑ready** when:

1. **All SCR (S‑Local & S‑Cross) hold** for the current snapshot (Contexts, Local‑Senses, SenseCells, rows, Role Descriptions, Bridges, windows).
2. **All RSCR (R‑Evo) hold** against the previous snapshot: no silent replacements; rows either unchanged or retired+reborn; Bridges re‑validated with CL non‑inflated without witnesses; windows adjusted only for real variance; SoD intact.
3. **One micro‑witness per moving part** exists in the text (tiny example showing the check in action).
4. **Memory rule still holds**: the active Context set for the line fits in a careful mind without external aids (F.1).

---

## 18 · Didactic distillation (90‑second teaching script)

> “Use the harness to **think like a safety net**. First, the **SCR** threads: everything is **local** to a Context; **Role Descriptions** point to **one** SenseCell; rows actually **cross** Contexts; Bridges are explicit with CL and a loss note; windows capture variation without spawning new types. Then, the **RSCR** knots: never overwrite an edition—**fork the Context** or mark recency; keep rows stable by **retiring and re-rowing**; Bridges get **re-validated** (CL goes down unless you bring proof); renames become **aliases** unless meaning changes; **windows** absorb time/scale shifts; **SoD** stays intact. If you can pass these thoughts on a small slice—and explain each pass in **one breath**—your unification is green. No tooling, no roles, no dashboards. Just clean Contexts, honest rows, cautious bridges, and names that help minds meet.”

# F.16 — Worked‑Example Template (Cross‑Domain) \[A] 

**“Show the thought, not the tooling.”**
**Status.** Architectural pattern \[A], architheory‑agnostic.
**Builds on:** E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; F.1–F.15.
**Coordinates with.** B.3 **Trust & Assurance Calculus** (CL on Bridges); Part C architheories (Sys‑CAL, KD‑CAL, Kind-CAL, Method‑CAL).

---

## 1 · Intent & applicability

**Intent.** Provide a **single, didactic page template** for cross‑domain worked examples that makes every claim **local to a Context** (Context), every Cross‑context step **explicit via a Bridge**, and every named role/status **traceably tied** to one **SenseCell**. The template is **notation‑free** and **tool‑agnostic**; it captures **how to think** the example so others can replay it.

**Applicability.** Use whenever you illustrate **any** FPF construct that spans more than one Context: **Role Assignment & Enactment** bindings, acceptance checks, measurement-driven claims, type alignment, control/actuation stories, etc.

**Non‑goals.** No registries, workflows, editors, or storage formats; no step‑by‑step “team procedures.” This pattern shapes **the page a reader sees**, not how it was produced.

---

## 2 · Problem frame

Cross‑domain examples often fail in four predictable ways:

1. **Global words.** *Process*, *role*, *service*, *execution* used without the Context, inviting drift.
2. **Hidden bridges.** “It’s basically the same” across disciplines, with losses left implicit.
3. **Name without sense.** A **Role Description** name appears with no visible tie to a SenseCell.
4. **List without structure.** Facts line up but never meet in a single **Concept‑Set row**.

The template counters these by forcing **Contexts → senses → row → bridges**, in that order.

---

## 3 · Core idea (didactic)

A robust worked example is a **compact theatre**:

* **Stage** = a declared **unification line** (which threads of Part C are in play).
* **Backdrop** = **Context set** (Contexts from F.1), each with a one‑line Card.
* **Actors** = **SenseCells** (⟨Context, Local‑Sense⟩) you will actually use.
* **Plot** = **one Concept‑Set row** where those cells stand as “the same thing” for this example.
* **Cues** = **Role Descriptions** that reference exactly one SenseCell each.
* **Cross‑talk** = **Bridges** across Contexts (with kind, CL, and loss).
* **Timing** = **Windows** (if status varies across time/scale) and **SoD** (if duties must remain separate).
* **Moral** = a handful of **harness checks** (F.15) that the reader can verify mentally.

---

## 4 · Minimal vocabulary (this pattern only)

* **Context / Context** — always **U.BoundedContext** (E.10.D1).
* **Local‑Sense** — a sense clustered within one context (F.3).
* **SenseCell** — address `⟨Context, Local‑Sense⟩`.
* **Concept‑Set row (ρ)** — a Cross‑context alignment for “what we treat as one” in this example (F.7/F.8).
* **Role Description (τ)** — a Role or Status that **points to one SenseCell** (F.4–F.6).
* **Bridge (β)** — explicit Cross‑context relation with **kind** (≡ / overlaps / broader‑than / narrower‑than), **CL**, and **loss note** (F.9).
* **Window** — a bounded interval (time/scale/phase) tied to a Status (F.10).
* **SoD** — Separation-of-Duties constraint among **Roles** (F.14).

---

## 5 · The one‑page **Worked‑Example Canvas**

> Each bullet is a **thought you make visible**, not a form field.

1. **Title & claim.** A short name + one‑sentence claim you will demonstrate.
   *Example:* *“Service Uptime as Evaluated by Runtime Executions”* — “We compare **Execution (IEC)** observations to **SLO (ITIL)** within a declared window.”

2. **Unification line.** Which Part C threads are active.
   *Example:* *Enactment + KD‑CAL (sensing) + Sys‑CAL (execution).*

3. **Context set (compact Cards).** 3–6 Contexts from F.1 with one‑line scope and, if inherent, **design vs run** stance.
   *Example:* *BPMN 2.0 (design: workflow graph); PROV‑O (run: Activity uses/generates); ITIL 4 (design: SLO/SLA); SOSA/SSN (run: Observation); IEC 61131‑3 (run: task executes).*

4. **SenseCells in play.** List exactly the **Local‑Senses** you will use, each prefixed by its Context.
   *Example:* ⟨**ITIL**: service‑level‑objective⟩, ⟨**SOSA**: observation⟩, ⟨**IEC**: execution‑task⟩, ⟨**PROV**: activity⟩.

5. **The Concept‑Set row (ρ).** A **single line** that places the cells you treat as “the same” for the claim, with a one‑breath justification.
   *Example row ρ:* { ⟨ITIL\:SLO⟩ ↔ ⟨SOSA\:observed‑availability⟩ } — *We treat “target availability” and “observed availability” as comparable magnitudes in a specific window.*

6. **Bridges (β).** For any Cross‑context relation **not captured by ρ** (or that requires nuance), state **kind, CL, loss**.
   *Example β₁:* ⟨**IEC\:execution‑task**⟩ **overlaps** ⟨**PROV\:activity**⟩, **CL=2**, *loss:* PROV lacks cyclic scheduling semantics.
   *Example β₂:* ⟨**SOSA\:observation**⟩ **narrower‑than** ⟨**ITIL\:measurement**⟩, **CL=2**, *loss:* ITIL omits procedure metadata.

7. **Role-Description hooks.** Name the Role/Status templates and the **one SenseCell** each references.
   *Example:* `AvailabilityStatus` → ⟨ITIL\:SLO⟩; `Execution` → ⟨IEC\:execution‑task⟩; `EvidenceObservation` → ⟨SOSA\:observation⟩.

8. **Windows & SoD (if relevant).** Spell any **status windows** and any **SoD** you rely on.
   *Example:* Window: *monthly, business‑hours*; SoD: *Operator* ⟂ *SLO‑Owner*.

9. **Micro‑narrative (5–7 lines).** Walk the reader through the claim using **Context‑prefixed words** and the row/bridges above.
   *Example (abridged):* “A **task (IEC)** runs the control program. Its **observations (SOSA)** yield availability over the *monthly* window. We compare those to the **SLO (ITIL)** in the same window. Where we refer to **activity (PROV)** we do so via **β₁** (overlap, CL=2). The row ρ is the locus of comparison; the Bridge **β₂** explains why ‘measurement’ in ITIL is broader than ‘observation’ in SOSA.”

**Harness pings (F.15).** *S-Row-Cross*, **S-RoleDesc-SingleCell**, *E-NoSilentEdition*.
    *Example:* *S‑Row‑Cross*, *S‑RoleDescription‑SingleCell*, *E‑NoSilentEdition*.

> **Memory rule.** If your Canvas cannot fit on a single page (or one slide), the example is teaching the wrong thing.

---

## 6 · Invariants (normative)

1. **Locality of meaning.** Every term in the narrative appears **with its Context** at first mention (*process (BPMN)*, *activity (PROV)*, …).
2. **At least one row.** The example **MUST** include ≥ 1 **Concept‑Set row** spanning ≥ 2 Contexts.
3. **Single-cell Role Description.** Every **Role Description** in the example **MUST** point to **one** SenseCell.
4. **Explicit bridges.** Any Cross‑context step **not explained by the row** **MUST** appear as a **Bridge** with kind, CL, and loss.
5. **Temporal honesty.** If a Context fixes **design vs run**, the narrative respects it.
6. **Window discipline.** If comparison depends on time/scale/phase, a **window** is stated rather than minting a new Status type.
7. **SoD integrity.** If duties are involved, **SoD** is explicit and unbroken.
8. **Didactic parsimony.** One page, one claim, one row (or a tiny bundle of closely related rows).

---

## 7 · The row panel (how to show it without notation)

Show the row as a **compact two‑to‑five‑column list**:

* **Column header** = Context.
* **Cell** = `Local‑Sense label` (tech register; optional plain label on next line).
* **Footline** (one line) = “row reason”—why these cells count as “the same thing **for this claim**.”

*Example visual (linear text):*
**ITIL 4:** *service‑level‑objective* | **SOSA/SSN:** *observed‑availability* → **Row reason:** *both quantify availability for the same window; units harmonised by KD‑CAL; procedural metadata differs (captured in loss of β₂).*

---

## 8 · Worked micro‑example (didactic)

> **Title.** *Alarms Should Not Satisfy Uptime*
> **Claim.** An **alarm‑only Execution (IEC)** cannot satisfy the **SLO (ITIL)** because **observation (SOSA)** windows exclude time in “alarm state.”

**Contexts.** IEC 61131‑3 (run), SOSA/SSN (run), ITIL 4 (design).
**SenseCells.** ⟨IEC\:execution‑task⟩, ⟨SOSA\:observation⟩, ⟨ITIL\:SLO⟩.
**Row ρ.** { ⟨ITIL\:uptime‑SLO⟩ ↔ ⟨SOSA\:observed‑availability⟩ } — comparable magnitudes in the *calendar‑month* window.
**Bridge β.** ⟨IEC\:alarm‑state⟩ **narrower‑than** ⟨SOSA\:observation‑qualifier⟩, **CL=2**, *loss:* SOSA does not prescribe plant‑specific alarm semantics.
**Role-Description hooks.** `AvailabilityStatus` → ⟨ITIL\:SLO⟩; `EvidenceObservation` → ⟨SOSA\:observation⟩.
**Window.** *Calendar month, business‑hours*, exclusion: *alarm‑state intervals*.
**Micro‑narrative (4 lines).** A **task (IEC)** runs; when the plant is in **alarm state**, **observations (SOSA)** are flagged and **excluded** from the availability window. We then compare the remaining interval to the **SLO (ITIL)** via row ρ. The Bridge β clarifies why the flag is a **qualifier** in SOSA, not a Status type in ITIL.
**Harness pings.** *S‑Row‑Cross*, *S‑RoleDescr‑SingleCell*, *S‑Window*, *S‑TemporalHonesty*.

---

## 9 · Relations (with other patterns)

**Builds on:**
F.1 (Contexts), F.2–F.3 (terms & senses), F.4–F.6 (roles), F.7–F.8 (rows), F.9 (bridges), F.10 (windows), F.14 (SoD), F.15 (harness).

**Constrains:**
Any example placed in Part C or Part B **must** render its claim through this canvas (or a faithful reduction), so readers can run F.15 mentally.

---

## 10 · Didactic distillation (60‑second script)

> “A good cross‑domain example fits on **one page**. First, name the **claim**. Then show the **Contexts** you’re using. List the **SenseCells** you will actually touch. Draw **one row** that makes them the same **for this claim**. Every Cross‑context nuance you can’t justify in that row becomes a **Bridge** with a **kind**, a **CL**, and a **loss** sentence. Point each **Role Description** to **one** cell. If time/scale matters, state the **window**; if duties matter, state **SoD**. Finish with two or three **harness pings** from F.15. That’s it—no tooling, no long procedures. The reader can now replay your thought and agree (or disagree) at the right place.”

## 11 · Anti‑patterns & remedies

| #         | Anti‑pattern               | Symptom in the page                                            | Why it breaks thinking                                         | Remedy (point to this template & sibling patterns)                        |
| --------- | -------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **AP‑1**  | **Row‑less tour**          | A list of facts from many Contexts with no **Concept‑Set row**.   | Reader cannot see *what is treated as the same* for the claim. | Include **≥ 1 row ρ** spanning ≥ 2 Contexts (§5‑5, §6‑2).                    |
| **AP‑2**  | **Stealth bridging**       | Phrases like “basically the same” with no Bridge.              | Imports meaning Cross‑context; hides losses.                      | State a **Bridge β** with **kind, CL, loss** (§5‑6, F.9).                 |
| **AP-3**  | **Role-Description vagueness**          | A Role/Status named without a SenseCell.                       | Why it breaks thinking                                         | Remedy (point to this template & sibling patterns)                        |
| **AP‑4**  | **Global words**           | *process, role, service* appear unprefixed.                    | Context‑less words drift mid‑example.                             | Prefix first mention with the **Context** (*process (BPMN)*) (§6‑1, E.10.D1). |
| **AP‑5**  | **Window‑free comparison** | Numbers/targets compared with no stated window.                | Apples‑to‑oranges across time/scale.                           | Declare a **Window** for the Status (§5‑8, F.10).                         |
| **AP‑6**  | **SoD leakage**            | Duties named but the same actor implicitly holds both.         | Violates Separation‑of‑Duties intent.                          | State **SoD** and keep duties disjoint (§5‑8, F.14).                      |
| **AP‑7**  | **Design/run blur**        | A design‑time notion used as if it were a run‑time occurrence. | Category error; wrong Context claims.                             | Mark Context stance and keep claims in‑stance (§5‑3, §6‑5).                  |
| **AP‑8**  | **Edition haze**           | “BPMN”, “ITIL” without edition/profile.                        | Debates about “what the book says”.                            | Put **name + edition** on each Card (§5‑3).                               |
| **AP‑9**  | **CL silence**             | Bridge kind given, no CL or loss note.                         | Reader cannot gauge translation risk.                          | Add **CL** and **loss** in every Bridge (§5‑6, B.3).                      |
| **AP‑10** | **Over‑row**               | Ten cells glued into one row “for convenience”.                | Collapses distinct senses; unreadable.                         | Prefer **one tight row**; split into **two rows** if needed (§5‑5, §8).   |

---

## 12 · Extended worked micro‑examples

> Each example fits the **one‑page canvas** (§5) and makes the **row** and **bridges** do the work.

### 12.1 Type alignment: OWL class vs FCA concept (design‑time only)

**Title & claim.** *“Two Lenses on *Pump*: OWL class and FCA concept align for catalogue reasoning.”*
**Unification line.** Kind-CAL (design) + FCA (design).
**Contexts.** **OWL 2 (profiles)** — classes, `subClassOf` (design). **FCA corpus** — formal concepts, lattice order (design).
**SenseCells.** ⟨OWL\:class ‘Pump’⟩, ⟨FCA\:formal‑concept ‘Pump’⟩.
**Row ρ.** { ⟨OWL\:Pump⟩ ↔ ⟨FCA\:Pump⟩ } — *same practical extension in this product catalogue*.
**Bridge β.** ⟨FCA\:lattice‑order⟩ **overlaps** ⟨OWL\:subclass‑order⟩, **CL=2**, *loss:* FCA intents may include context attributes not modeled in OWL restrictions.
**Role-Description hooks.** `TypeLabel` → ⟨OWL\:class⟩ (for naming), no runtime **Role Assignment/Enactment**.
**Micro‑narrative (3 lines).** For catalogue queries, the **instances** covered by OWL class *Pump* match those of the FCA concept created from the same attributes; we treat them as one row. The **orderings** diverge in nuance (β), but not for membership in this example.
**Harness pings.** *S‑Row‑Cross*, *S‑TemporalHonesty* (design only), *S‑Bridge‑Kind‑CL*.

---

### 12.2 Role vs permission: SoD in enactment vs access control

**Title & claim.** *“Behavioral role (BPMN) is disjoint from access role (RBAC); keep duties separate.”*
**Unification line.** Role Assignmnent and Enactment (design & run) + access/deontics (design).
**Contexts.** **BPMN 2.0** — participant/lanes (design). **NIST RBAC (2004)** — roles/permissions (design).
**SenseCells.** ⟨BPMN\:participant⟩, ⟨RBAC\:role⟩.
**Row ρ.** — *(intentionally none)* — we do **not** treat them as the same.
**Bridge β.** ⟨BPMN\:participant⟩ **disjoint** ⟨RBAC\:role⟩, **CL=3**, *loss:* none—*different dimensions* (behavioral mask vs permission grouping).
**Role-Description hooks.** `Operator` → ⟨BPMN\:participant⟩; `AccessRole` → ⟨RBAC\:role⟩. **SoD:** `Operator` ⟂ `AccessRole‑Admin`.
**Window.** Not applicable.
**Micro‑narrative (3 lines).** We show SoD by prohibiting the same actor from holding **Operator** and **AccessRole‑Admin**. The disjoint **β** prevents leakage between behavioral masks and permission bundles.
**Harness pings.** *S‑RoleDescr‑SingleCell*, *S‑SoD*, *S‑Bridge‑Disjoint*.

---

### 12.3 Method quartet: from MethodDescription to Work with observations

**Title & claim.** *“Behavioral role (BPMN) is disjoint from access role (RBAC); keep duties separate.”*
**Unification line.** **Role Assignment & Enactment** (design & run) + access/deontics (design).
**Contexts.** **SPEM 2.0** (design: Method/MethodDescription), **PROV‑O** (run: Activity), **SOSA/SSN** (run: Observation), **ITIL 4** (design: SLO).
**SenseCells.** ⟨SPEM\:MethodDescription⟩, ⟨PROV\:activity⟩, ⟨SOSA\:observation⟩, ⟨ITIL\:SLO⟩.
**Row ρ.** { ⟨ITIL\:SLO\:build‑time⟩ ↔ ⟨SOSA\:observed‑build‑duration⟩ } — *compare promised vs observed duration on the same window*.
**Bridges.** β₁: ⟨SPEM\:MethodDescription⟩ **narrower‑than** ⟨PROV\:activity‑plan⟩, **CL=2**, *loss:* PROV lacks prescriptive structure; β₂: ⟨SOSA\:observation⟩ **narrower‑than** ⟨ITIL\:measurement⟩, **CL=2**, *loss:* ITIL abstracts from procedure.
**Role-Description hooks.** `Operator` → ⟨BPMN\:participant⟩; `AccessRole` → ⟨RBAC\:role⟩. **SoD:** `Operator` ⟂ `AccessRole-Admin`.
**Window.** *Release window: calendar week*.
**Micro‑narrative (4 lines).** The **MethodDescription (SPEM)** implies a target **build‑time**; **Work (PROV activity)** occurs; **observations (SOSA)** provide actuals; we compare against the **SLO (ITIL)** via row ρ over the *calendar week* window. Bridges β₁–β₂ explain why plan/measure semantics do not collapse.
**Harness pings.** *S‑Row‑Cross*, *S‑Window*, *S‑RoleDesc‑SingleCell*, *S‑TemporalHonesty*.

---

## 13 · Reasoning primitives (judgement schemas)

> These are **mental checks** you can perform on any example page.

1. **Row validity**
   `cells(ρ) = {⟨Cᵢ,Sᵢ⟩} with |Contexts(ρ)| ≥ 2 ⊢ validRow(ρ)`
   *Reading:* A row is valid only if it spans at least two Contexts and all entries are legitimate **SenseCells** (from F.3).

2. **Bridge coverage**
   `coRef(Ca,Cb) ∧ ¬sameRow(Ca,Cb) ⊢ requires β(Ca↔Cb)`
   *Reading:* If two Contexts are co‑referenced in the narrative but their senses are not placed in the same row, an explicit **Bridge** is needed.

3. **Role-Description single-cell**
   `Role Description τ used ⊢ ∃!⟨C,S⟩ : ref(τ)=⟨C,S⟩`

4. **Window sufficiency**
   `compare(qᵢ@Cᵢ, qⱼ@Cⱼ) ⊢ windowDeclared`
   *Reading:* Any Cross‑context quantitative comparison calls for a stated **Window**.

5. **Temporal honesty**
   `C has stance s ∈ {design, run} ⊢ claims@C must respect s`
   *Reading:* Do not assert run‑facts in a design‑only Context, or vice versa.

6. **SoD integrity**
   `SoD(D₁ ⟂ D₂) ∧ assign(actor, D₁) ∧ assign(actor, D₂) ⊢ violation`
   *Reading:* A declared SoD cannot be violated inside the example.

7. **Bridge clarity**
   `β given ⊢ kind(β) ∧ CL(β) ∧ loss(β)`
   *Reading:* Every Bridge shows **kind**, **CL**, and a **one‑line loss**.

8. **Edition clarity**
   `card(C) ⊢ has(name, edition)`
   *Reading:* Each Context Card specifies name + edition/profile.

9. **Harness ping mapping**
   `ping ∈ {S‑*, E‑*} ⊢ ping ⇒ subset of judgements above`
   *Reading:* Each named harness check (F.15) has a clear reading in these judgements.

---

## 14 · Acceptance tests (SCR/RSCR)

### 14.1 Static conformance (SCR)

* **SCR‑F16‑S01 (Row present).** The page contains **≥ 1** Concept‑Set row spanning **≥ 2 Contexts**.
* **SCR‑F16‑S02 (Bridge explicit).** Every Cross‑context assertion not justified by a row is shown as a **Bridge** with **kind, CL, loss**.
* **SCR-F16-S03 (Role-Description anchoring).** Each **Role Description** appearing in the page references **exactly one SenseCell**.
* **SCR‑F16‑S04 (Context prefixes).** First mention of each ambiguous term is **Context‑prefixed**.
* **SCR‑F16‑S05 (Window discipline).** Any numeric comparison across Contexts names a **Window**.
* **SCR‑F16‑S06 (DesignRunTag).** Claims respect each Context’s **design/run** stance.
* **SCR‑F16‑S07 (SoD).** If duties are named and SoD is relevant, **SoD is stated** and unviolated.
* **SCR‑F16‑S08 (One‑page parsimony).** The example fits the **one‑page canvas**; if extended, each sub‑page still respects §6 invariants.

### 14.2 Regression (RSCR)

* **RSCR‑F16‑E01 (Edition drift).** When a Context’s edition changes, the example either (a) is unaffected or (b) adds a note adjusting **β** or the **row**; no silent rewrites.
* **RSCR‑F16‑E02 (Bridge re‑score).** If an upstream **CL** definition changes (B.3), affected Bridges on the page show the new CL and, if needed, an updated **loss** sentence.
* **RSCR‑F16‑E03 (Row resilience).** If a SenseCell is split in F.3 (sense refinement), the example either keeps the same row using one child sense, or splits into two rows with a short justification.
* **RSCR‑F16‑E04 (Window clarity).** If organisational cadence changes (e.g., from monthly to weekly), windows on the page are updated explicitly.

---

## 15 · Migration notes (conceptual)

1. **Refactor long tutorials.** Extract the **claim**; pick **3–6 Contexts** (Cards); list the **SenseCells** you actually use; craft **one tight row**; surface any cross‑talk as **Bridges** with loss notes; delete everything else.
2. **Split crowded rows.** If a row tries to carry more than \~4 cells, split into two rows and write a **one‑line purpose** for each.
3. **Stabilise vocabulary.** If you find yourself rewriting terms mid‑page, you likely forgot a Context; return to F.1 and add a Card.
4. **Teach the bridge itch.** Leave “*these are the same*” feelings ungratified until you can articulate **kind, CL, loss** in one sentence.
5. **DesignRunTag respect.** If a design‑only Context tempts you into runtime talk, move that part of the narrative into a **run‑Context** and Bridge as needed.
6. **Keep the page living.** When upstream rows/bridges evolve (F.7–F.9), adjust the page *minimally* and call out the change in a margin note (conceptual, not procedural).

---

## 16 · Teaching variants (all obey §6 invariants)

* **Two‑Context equivalence.** Smallest case: 1 row, 2 Contexts, **β (≡, CL=3)** to explain why they’re truly the same *for this claim*.
* **Triangulation.** 1 row, 3 Contexts; typical for *measurement ↔ service ↔ execution*.
* **Disjointness lesson.** No row; one **β (disjoint)** plus a short SoD story.
* **Window primer.** Same sense across Contexts but different default windows; the page is about the **window choice**, not the term.

---

## 17 · Didactic checklist (author’s quick scan)

* One sentence **claim**?
* **Contexts** (with editions) visible?
* **SenseCells** named (tech & plain labels acceptable)?
* **Exactly one** tight **row** (or two, each justified)?
* All Cross‑context steps shown as **β(kind, CL, loss)**?
* **Role Description → one SenseCell** each?
* **Window** present where numbers meet?
* **SoD** stated where duties appear?
* Page fits a **single view**?

---

## 18 · Closing distillation (30‑second echo)

> A strong worked example is a **one‑page alignment**: claim → Contexts → cells → **one row** → explicit **bridges** → Role-Description hooks → window/SoD if needed. No tooling, no process charts—just **visible thinking** that any careful reader can replay and critique at the right place.


## F.17 — Unified Term Sheet (UTS) \[A]

**“One table that a careful mind can hold.”**
**Status.** Architectural pattern \[A], architheory‑agnostic.
**Builds on:** F.1–F.3 (Contexts → seeds → local senses), F.4 (Role Characterisation), F.5 (Naming), F.7 (Concept‑Set table), F.8 (Mint/Reuse decision), F.9 (Bridges), F.10–F.12 (Status & method/service bindings), F.15 (SCR/RSCR).
**Coordinates with:** A.1.1 `U.BoundedContext`, A.7 **Strict Distinction**, A.8 **Heterogeneity**, A.11 **Ontological Parsimony**, A.15 **Role–Method–Work Alignment**.
**Non‑goals.** No registries, workflows, editors, or storage formats. No by‑name Cross‑context equivalence. No “data pipeline.” This pattern prescribes **what a UTS is** and **how to judge it**, not how to generate files.

### 1 · Intent & Applicability

**Intent.** Provide a **single, normative table**—the **Unified Term Sheet (UTS)**—that distils the output of F.1–F.12 into **human‑readable rows**. Each row expresses **one Concept‑Set** unified into **one FPF U.Type** with its **Tech/Plain names** and **cross‑context senses**. The UTS is the *front‑door view* that authors, engineers, and managers use; it replaces scattered notes and eliminates guesswork.

**Applicability.** Produce a UTS **per architheory thread** (e.g., *Role Assignment & Enactment*, *Method quartet*, *Trust & Evidence*). Use it:

* to **name** U.Types and their **Tech/Plain** labels (F.5),
* to **teach** the mapping from familiar canons to unified concepts,
* to **audit** coverage and heterogeneity (A.8), and
* to **feed** examples in Parts A/C without re‑explaining terminology.

**Why now.** Earlier F‑patterns define *how to think*. **F.17** defines *what you publish* so others can think with you.

### 2 · Problem Frame

Without a single sheet:

1. **Locality is lost.** Mappings hide in prose; readers re‑globalise words.
2. **Naming drifts.** Teams adopt ad‑hoc labels that collide later.
3. **Coverage is opaque.** No quick check that coverage spans **≥ 3 domain families** across the sheet (A.8).
4. **Didactic load spikes.** Each section re‑teaches the same terms.

**UTS** fixes this by putting the **unification decision** and the **cross‑context evidence** on **one line** per concept.

---

### 3 · Forces

| Force                             | Constraint in UTS                                                                                                   |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Didactic primacy vs. fidelity** | UTS keeps **two names** (Tech/Plain) and **one‑line rationale**, but never misstates a source meaning.              |
| **Parsimony vs. recall**          | Each row is one concept; the UTS as a whole demonstrates heterogeneity across ≥ 3 domain families (A.8). Rows may cite fewer Contexts when the concept truly appears in fewer.                   |
| **Locality vs. comparability**    | Senses are **Context‑scoped** (E.10.D1). Cross‑context relations are shown only as **explicit bridges** (F.9) with **CL**. |
| **General usability**             | Sheet must be **legible on paper** and **memorisable** (block structure, stable row order).                         |

---

### 4 · Core Idea

**A UTS is a Concept‑Set table with names.**
Each **row** = one **Concept‑Set** unified into one **FPF U.Type** (the “what we mean”).
Each **column family** shows **how this concept appears** in the chosen **contexts of meaning** (F.1).

Two **canonical layouts** are allowed (pick one or publish both):

* **Layout A — Kernel‑first**: rows keyed by **FPF U.Type**; **Bounded‑Context Columns (BCC)**.
* **Layout B — Base‑concept**: rows keyed by **Base concept** (EN/RU) of a discipline, then unified to **U.Type**; **Discipline Columns (DC)**.

Both layouts are normative; choose based on audience. In Layout A, comparability is by **BCC** (*Bounded‑Context Column*); in Layout B, comparability is by **DC** (*Discipline Column*); never conflate the two.

### 5 · Minimal Vocabulary (for this pattern)

* **UTS (Unified Term Sheet).** The published, human‑readable table per thread.
* **Context.** Alias in Tech register for **`U.BoundedContext`** (E.10.D1). Normative unit of meaning; every SenseCell is scoped to a Context _(name + edition)._  
* **Bounded‑Context Column (BCC).** A didactic column used **only in Layout A**; one column per **Context (`U.BoundedContext`)** from the F.1 cut; **not a model element**; the **header includes the Context name + edition**.  
* **Discipline Column (DC).** A _discipline vantage_ used **only in Layout B** (e.g., _Operational Management_, _IT/Software_, _Physics_). A DC is **not** a **Bounded‑Context Column** and does not carry editions.  
* **Concept‑Set (CSR).** One unified concept with pointers to its SenseCells.  
* **SenseCell.** _(Context × Local‑Sense)_ address—how a Context “says that thing”.  
* **Bridge / CL.** Explicit cross‑context mapping (F.9) with Congruence Level and Loss note.
* **Plain Twin (LEX).** The LEX record pairing the **Unified Tech name** with its **Unified Plain name** for a U.Type; governed by **PTG** and referenced by `Twin‑Map Id (LEX)` (E.10 LEX‑BUNDLE).
* **Block Plan.** Didactic grouping of rows to keep the sheet memorizable.  
* **Unified Tech name / Unified Plain name.** Dual‑register names chosen per F.5; the **Tech name is the neutral, unified term** for the U.Type, not a borrowed Context name.

> **Discipline.** “Context” always means **`U.BoundedContext`** (E.10.D1). No global words.

### 6 · Row Schema (normative)

Every UTS row **MUST** carry the following fields (verbatim headings recommended):

| Field                     | Purpose                                                                                               |
| ------------------------- | ----------------------------------------------------------------------------------------------------- |
| **# / Block**             | Stable id and didactic block (see §7).                                                                |
| **FPF U.Type**            | Canonical kernel type (e.g., `U.Work`).                                                               |
| **Unified Tech name**     | Short technical name used in spec prose (F.5).                                                        |
| **Unified Plain name**    | Everyday name for non‑specialists (F.5).                                                              |
| **Plain‑Twin Governance (PTG) (optional)** | Stance for the Unified Plain twin: {**Strict**, **Guarded**, **Provisional**}; use when additional discipline of the Plain twin is required (E.10 LEX‑BUNDLE). |
| **Twin‑Map Id (LEX) (optional)** | Identifier of the Tech↔Plain twin record in the LEX‑BUNDLE; cite when `PTG ≠ Strict` or when multiple candidate twins exist. |
| **FPF Description**       | One‑line definitional gist (no examples).                                                             |
| **SenseCells (by context)** | Per selected Context: the local term(s) or construct that best realises the concept (one cell per Context). |
| **Bridges (CL/Loss)**     | For any cross‑context relation, record the F.9 Bridge with **CL** and a 2–6‑word loss note; if identity, mark **CL=3 (identity)**. |
| **Unification Rationale** | One sentence: why these senses are the same *conceptually*.                                           |
| **Notes (optional)**      | Brief DesignRunTag or trip‑wire hints (e.g., “design vs run”).                                     |

**Constraint.** “SenseCells (by **Context**)” **MUST** cite **at least three** distinct **Contexts** overall across the sheet for the thread (A.8). A single row may show fewer if the concept truly appears in fewer contexts; coverage is a property of the whole UTS.

**Discipline:** Every SenseCell **must** cite the **Context name + edition** (e.g., _“BPMN 2.0 (2011): Activity instance”_).

#### 6.1 · NQD Fields (normative; when applicable)

If a UTS row **describes** a **Generator/Selector/Portfolio** (design‑time or run‑time artefact), it **MUST** add the following fields. These are *publication* fields, not tooling‑specific formats.

| Field | Purpose |
| --- | --- |
| **N (Novelty)** | Lawful novelty claim tied to `CharacteristicSpaceRef` + `DistanceDefRef` (declare metric/pseudometric & invariances; cite edition ids). |
| **U (Use‑Value)** | Declared acceptance/test value under the active **CG‑Frame** (units & scale typed per MM‑CHR). |
| **C (ConstraintFit)** | Feasibility against **ResourceEnvelope/RiskEnvelope** (and relevant deontic/ethics clauses); no `unknown→0` coercion. |
| **D\_P (Portfolio Diversity)** | Diversity contribution relative to the **current PortfolioPack** (`ArchiveConfig`, grid/binning, K‑capacity, dedup). |
| **E/E‑LOG policy‑id** | Edition id of the explore/exploit governor policy that governed generation/selection budgets. |

**Note.** These fields *extend* the Row Schema; they do not change SenseCells/Bridges/Names. Rows that are *purely definitional* (no generator/selector/portfolio semantics) do not carry §6.1.

#### 6.2 · Autonomy fields (when applicable)
Add the following columns (nullable; **required** when autonomy is claimed by the row’s subject):
* `AutonomyBudgetDeclRef` (id, version)
* `Aut-Guard policy-id`
* `OverrideProtocolRef`
* `Scope (G)` (autonomy scope)
* `Γ_time` (admission window selector)
* *(optional)* `ScaleLensPolicyRef`
* *(optional)* `ScaleLensOptIn ∈ {OptedIn, Neutral, OptedOut}`
**Note.** These fields are required for UTS rows that describe a **Role**, **Method**, **Service**, or **Selector** with autonomy claims; optional fields make **Bitter‑Lesson/Scale‑Lens** an explicit **opt‑in** with published criteria.

### 7 · Block Plan (didactic grouping)

A UTS **MUST** declare a **Block Plan**—the sequence of blocks that group rows. Blocks are **thread‑specific**. Example **Block Plan** for *Role Assignment & Enactment* (matches your earlier tables):

* **Block A · Context & Roles** — `U.BoundedContext`, `U.Role`, `U.RoleAssignment`, `U.Capability`.
* **Block B · Method & Description** — `U.Method`, `U.MethodDescription`, Access/Acceptance descriptions (fields of `U.Service`).
* **Block C · Execution & Schedule** — `U.Work`, `U.WorkDescription`, `U.Observation`.
* **Block D · Service & Deontics** — `U.Service`, `U.SpeechAct`, `U.Commitment`, `U.ServiceClause`, `U.ServiceEvaluation`.
* **Block E · Carriers & Bridges** — `U.Carrier`, *Alignment (Bridge entry)*.
* **Block R · Knowledge Units & Statuses** — `U.Episteme`, `U.EvidenceRole`, `U.StandardStatus`, `U.RequirementStatus`, `U.DefinitionRole`, `U.AxiomaticCoreRole`.

> **Rule.** Block names are **didactic**, not ontological. Do **not** infer mereology or subtyping from blocks.

### 8 · Column Families (two canonical layouts)

#### 8.1 Layout A — Kernel‑first (U.Type as rows)

**Columns:**

* `FPF U.Type · Unified Tech name · Unified Plain name · Plain‑Twin Governance (PTG) · Twin‑Map Id (LEX) · FPF Description` *(left rail; `PTG`/`LEX` are optional)*
* **Bounded‑Context Columns (BCC)** — one column per **Context (`U.BoundedContext`)** from the F.1 cut; each header shows _name + edition_: e.g., **OMG BPMN 2.0**, **W3C PROV‑O**, **ITIL 4**, **NIST RBAC**, **W3C SOSA/SSN**, **OMG Essence (Language)**, **DEMO/DEMO‑EO**, **PMBOK 7**, **CM/BPM (CMMN/BPMN)**, **IEC 61131‑3**, **ODRL 2.2**, **ISO 80000‑1 / Metrology** … *(your chosen 12 Contexts)*
* `Bridges (CL/Loss)`
* `Unification Rationale`
* `Notes`
  
Do not mix **Discipline Columns (DC)** in Layout A. Columns here are only **Bounded‑Context Columns (BCC)**.

#### 8.2 Layout B — Base‑concept pivot (discipline columns)

**Columns:** Base concept · Scale‑map · Unified Tech name · **Unified Plain name** · Plain‑Twin Governance (PTG) · Twin‑Map Id (LEX) · Formal U.Type · **Discipline Columns (DC)** (e.g., Operational Management / IT/Software / Physics / …) · Rationale · Notes.

* `Base concept (EN / RU)`
* `Scale‑map (Σ / Π / μ)` *(optional; see §9.4)*
* `Unified Tech name`
* `Unified Plain name`
* `Plain‑Twin Governance (PTG)` *(optional)*
* `Twin‑Map Id (LEX)` *(optional)*
* `Formal U.Type`

* **Discipline Columns (DC)** (choose 3–5): e.g., **Operational Management**, **IT/Software**, **Physics**, **Science/Theory**, **Math/Proof**, **Literature**, **Religion** *(or other discipline columns suited to the thread)*
 * `Unification Rationale`
* `Notes`
 
> **Guidance.** Publish **Layout A** for kernel users and spec authors; publish **Layout B** for cross‑disciplinary onboarding and teaching.
> **Clarification — Plain vs Base concept.** In Layout B the `Base concept (EN/RU)` is a **discipline vantage** aid and **does not substitute** for the single **Unified Plain name** in the left rail. Do not mint alternative unified‑plain synonyms inside DC cells; flag homonym risks with ⚡ in `Notes`.

### 9 · Invariants (normative constraints)

1. **Locality.** Every SenseCell is **Context‑scoped** (E.10.D1). No global synonyms.
2. **Bridges only via F.9.** Cross‑context equivalence appears **only** as an explicit Bridge with **CL**. Any row citing > 1 **Context** must state at least one Bridge.
3. **Heterogeneity.** Across the UTS, coverage must involve **≥ 3 domain families** (F.1 Step 2; A.8).
4. **Scale‑map tags (optional but disciplined).** If used in Layout B:
   * **Σ (Summative):** concept’s quantitative properties aggregate across a population of executions/holders.
   * **Π (Conjunctive/Compositional):** concept composes by required conjunction (all‑of), not by averaging.
   * **μ (Micro/Atomic):** concept is inherently micro‑level (per single execution/holder).
     *(Tags aid teaching; they do not change semantics.)*
5. **Strict Distinction.** Use `U.Method` vs `U.MethodDescription`, `U.Work` vs `U.WorkDescription`, `U.Role` vs `U.RoleCharacterisation` correctly; do **not** collapse intensional objects with their descriptions.
6. **Dual register.** Every row has **Tech** and **Plain** labels per F.5.
7. **One‑breath rationale.** The `Unification Rationale` is a **single sentence** explaining the conceptual sameness despite local wording.
8. **Unified naming neutrality.** The **Unified Tech name** is the neutral FPF choice per F.5; it is **not** lifted wholesale from any single Context unless the Concept‑Set justification (F.7) shows identity.  
9. **Column discipline.** Layout A uses **Bounded‑Context Columns (BCC)** only; Layout B uses **Discipline Columns (DC)** only. Mixing is non‑conformant.
10. **Plain‑twin discipline.** The single **Unified Plain name** lives in the left rail; BCC/DC cells carry senses only. Any additional Plain aliases are managed in LEX (tv:*) and never minted per column.


### 10 · How to Compile (conceptual moves, not a workflow)

**M1 · Fix contexts (F.1).** Declare the **12 (±)** contexts for this thread.
**M2 · Harvest & cluster (F.2–F.3).** Identify candidate senses per Context; cluster *within* Contexts; mint **SenseCells**.
**M3 · Form Concept‑Sets (F.7).** For each “the‑same‑thing” across Contexts, create one **CSR**; attach SenseCells.
**M4 · Name (F.5).** Choose **Tech/Plain** labels; assert the **FPF U.Type** (or propose a new one via F.8).
**M5 · Bridge (F.9).** Where Cross‑context relations are not exact, assert Bridges with **CL** and a short **Loss** note.
**M6 · Place rows into blocks (§7).** Keep the sheet memorisable.
**M7 · Write one‑line `FPF Description` and the `Rationale`.**
**M8 · Run acceptance harness (F.15).** Apply the UTS checks in §11.

> **Note.** These are **thought moves**. No tooling is implied or required.

### 11 · Acceptance Harness (SCR/RSCR) for a UTS

#### 11.1 Static Conformance Rules (SCR‑UTS)

* **SCR‑UTS‑01 (Row completeness).** Each row contains: `U.Type`, `Tech`, `Plain`, `FPF Description`, `SenseCells (≥ 1)`, `Rationale`.
* **SCR‑UTS‑02 (Dual register).** Each row has both Tech and Plain labels; Tech is used in spec prose, Plain in didactics.
* **SCR‑UTS‑03 (Locality discipline).** Every SenseCell is cited **with its Context name & edition**.
* **SCR‑UTS‑04 (Heterogeneity).** Across the sheet, the set of referenced Context spans **≥ 3 domain families**.
* **SCR‑UTS‑05 (Bridge honesty).** All cross‑context sameness claims are expressed via an F.9 **Bridge** with a **CL** score; if identity, mark **CL=3** and note “identity/no loss” rather than omitting the bridge.
* **SCR‑UTS‑06 (One‑breath rationale).** The rationale is ≤ 35 words and states the **conceptual invariant** that unifies the row.
* **SCR‑UTS‑07 (Block parsimony).** Block Plan uses **≤ 7 blocks**; each block’s rows can be recited from memory by a careful reader.
* **SCR‑UTS‑08 (Strict Distinction).** No row description conflates Method↔MethodDescription, Work↔WorkDescription, Role↔RoleCharacterisation.
* **SCR‑UTS‑09 (Unified naming).** Each row’s **Unified Tech name** complies with F.5 rules (dual register, minimal generality, morphology); it is not a mere alias of one Context unless justified by an F.9 Bridge with **CL=3**.
* **SCR‑UTS‑10 (Column discipline).** **Layout A:** all non‑left‑rail columns are **Contexts** with editions. **Layout B:** all non‑left‑rail columns are **discipline columns**. No cross‑use.
* **SCR‑UTS‑11 (Plain‑twin hygiene).** The **Unified Plain name** appears **once** in the **left rail** (**tv:primary**). Neither BCC (Layout A) nor DC (Layout B) cells may introduce alternative **unified** Plain synonyms; use the ⚡ marker in `Notes` to flag homonym risk where needed.

#### 11.2 Regression Rules (RSCR‑UTS)

* **RSCR‑UTS‑A (Edition churn).** When a Context’s edition changes, old SenseCells remain addressable; new cells are added; **no silent rewrites**.
* **RSCR‑UTS‑B (Name stability).** Tech labels change only with a documented F.5 decision; Plain labels may evolve didactically if the Tech name stays.
* **RSCR‑UTS‑C (Coverage drift).** Adding/removing rows **must not** reduce family heterogeneity below §9.3.
* **RSCR‑UTS‑D (Loss drift).** If new evidence changes a Bridge’s CL/Loss, the row updates both the CL and the 2–6 word loss note.
* **RSCR‑UTS‑E (Plain discipline).** No per‑column Plain text appears in BCC/DC columns; any additional Plain aliases are tracked in Annex with **tv:** entries and counted against the alias budget (F.13). 

### 12 · Canonical Heading Templates (fill with your Contexts/Discipline columns)

**Layout A — Kernel‑first**

```
# | Block | FPF U.Type | Unified Tech name | Unified Plain name | Plain‑Twin Governance (PTG) | Twin‑Map Id (LEX) | FPF Description
  | BCC‑1 (Context name, edition) | BCC‑2 (Context name, edition) | BCC‑3 (Context name, edition) | … (more BCCs from the F.1 cut)
  | Bridges (CL/Loss) | Unification Rationale | Notes
```

**Example headers (illustrative, not canonical):**  
`OMG BPMN 2.0 (2011) | W3C PROV‑O (2013) | ITIL 4 (2020) | W3C SOSA/SSN (2017) | OMG Essence (Language, 2023)`  
_(Use the actual Contexts from your F.1 cut; always include the edition.)_

**Layout B — Base‑concept pivot**
_(Plain twin discipline identical: only one **Unified Plain name (tv:primary)** in the left rail; DCs carry senses, not Plain.)_

```
# | Block | Base concept (EN / RU) | Scale‑map (Σ/Π/μ)
  | Unified Tech name | Unified Plain name | Plain‑Twin Governance (PTG) | Twin‑Map Id (LEX) | Formal U.Type
  | DisciplineColumn‑1 (discipline) | DisciplineColumn-2 (discipline) | DisciplineColumn‑3 (discipline) | DisciplineColumn‑4 (discipline) | DisciplineColumn‑5 (discipline)
  | Unification Rationale | Notes
```

**Examples of Discipline Columns (illustrative):** Operational Management · IT/Software · Physics · Science/Theory · Mathematics · Literature · Religion.  
_(Choose 3–5 that fit the thread; do not place Contexts here.)_

### 13 · Didactic Aids

* **Trip‑wire column (optional).** A ⚡ marker in `Notes` for known homonyms (e.g., *process (BPMN) ≠ process (thermo)*).
* **DesignRunTag tag (optional).** `design` / `run` hint for concepts whose senses split by time.

### 14 · Micro Examples (one line each, illustrative)

*(These illustrate Layout A headings; swap Contexts to match your cut.)*

**Row: `U.Work` (Execution)**
`Tech=Execution · Plain=run` — “Dated, resource‑consuming occurrence realising a MethodDescription.”
**BPMN 2.0 (2011)**: *Activity instance* · **PROV‑O (2013)**: `prov:Activity` · **ITIL 4**: *change/incident record (run)* · **SOSA/SSN**: *(context: producer of Observation)* · **Essence (Language)**: *Activity occurrence* · **Bridges**: CL=3 (BPMN≍PROV) · **Rationale**: *All cells denote the concrete happening, not the recipe nor the capability.*

**Row: `U.MethodDescription` (Recipe)**
`Tech=MethodDescription · Plain=recipe` — “Recorded specification guiding executions.”
**BPMN 2.0 (2011)**: *Process model* · **PROV‑O (2013)**: `prov:Plan` · **ITIL 4**: *SOP / Work instruction* · **Essence (Language)**: *Activity space/Practice description* · **Bridges**: CL=2 (loss: control‑flow vs intent) · **Rationale**: *All cells denote the codified ‘how’, distinct from both the performer and the run.*

> These rows are examples only; your UTS MUST be compiled from your chosen **Contexts** (Layout A) or **Discipline Columns (DC)** (Layout B) and SenseCells.

### 15 · Relations

* **Builds on:** F.1–F.3 (contexts & local senses), F.7 (Concept‑Set), F.5 (names), F.9 (Bridges).
* **Feed:** Part A and Part C definitions/examples (row ids used as cross‑refs); teaching bundles (F.16).
* **Constrained by.** A.7 **Strict Distinction**, A.11 **Parsimony**, **E.10 §6 Twin‑Register Discipline** (Tech/Plain), **E.10.P (prefix registry: tv: / ut:)**, E.10.D1 **Context discipline**.

### 16 · Migration Notes

* **Re‑blocking.** If the Block Plan changes, keep row ids stable; move rows between blocks rather than renumbering.
* **Context growth.** When adding a new Context, populate SenseCells progressively; do not claim coverage until ≥ 1 row per block cites it.
* **Name evolution.** Update **Plain** labels freely for pedagogy; change **Tech** labels only via F.5 with clear S‑rules.


### 17 · FAQ (authoring hygiene)

**Q1. Is the UTS a registry?**
*A.* No. It is a **didactic publication artifact**. No CRUD semantics, no workflows.

**Q2. Can we collapse two Contexts if their terms look identical?**
*A.* Only via **F.9 Bridge** with **CL=3**. Identity must be argued, not assumed by spelling.

**Q3. Where do state‑graphs (A.2.5) show up?**
*A.* In `Notes` or as a dedicated row if the stateful nature of a Role family is central to the thread.

**Q4. How do we show deontic approvals?**
*A.* The concept rows (`U.SpeechAct`, `U.Commitment`, `U.ServiceClause`, `U.ServiceEvaluation`) make the communicative/epistemic pieces visible; enactment appears in examples, not as sheet mechanics.

### 18 · 90‑Second Teaching Script

> “To make our language usable, we publish a **Unified Term Sheet** for each thread. Each **row** is one **unified concept** (a Concept‑Set) named with a **Tech** and a **Plain** label and tied to concrete senses in our chosen **context of meaning**. If two contexts differ, we show an explicit **Bridge** with a **CL score** and a short **loss note**. The rows are grouped into 5–7 **didactic blocks** so the whole sheet fits in working memory. This is not a database; it’s the **one table** a careful mind can hold. From this sheet, everyone—engineers, managers, researchers—can talk precisely about **the same things** across disciplines.”

## **F.18 — Local‑First Unification Naming Protocol** \[A]
*Status: normative (Part F, Unification Suite). Audience: engineer‑managers, lead architects, editors of FPF artefacts. 

### 1. Context

Names must carry enough signal for everyday use, yet never smuggle in Cross‑context identities, hidden assumptions, or role/metric clutter. F.18 supplies that naming discipline and weaves it through F.1–F.17: Term Harvesting, Sense Clustering, Role Descriptions, Concept‑Sets, Bridges, Lexical Continuity, Anti‑Explosion control, and the Unified Term Sheet (UTS).

**Scope.** This protocol applies to naming of **any concepts** authored in Part F (U.Types and **local concepts** alike: kinds, roles, services, methods, works, relations, characteristics, states/statuses, etc.). The **U.Types** norms in this section are a **specialization**, not a restriction of scope.

**Purpose of this pattern.** Provide a **human‑legible, context‑anchored naming protocol** that:
* keeps *local meaning first* and prevents Cross‑context conflation;
* makes the **kind** of thing explicit (System, Episteme, Role, Service, Method, Work, Decision, Requirement, etc.);
* integrates smoothly with **Concept-Sets**, **`U.RoleDescription`**, and **Bridges** without requiring any special notation or tooling;
* supports lifecycle actions (mint, reuse, align, deprecate, split/merge) with a paper trail that managers can audit.

### 2. Problem

Without a shared naming protocol inside Part F, the same recurrent failures appear:

1. **Global‑name illusion.** A short label travels from one context to another and is *assumed* to mean the same thing; later, contradictions surface during acceptance or assurance.
2. **Context drift.** A label gradually changes inside its Context (edition, scope, envelope) without leaving a clean trace; readers argue over “what we meant.”
3. **Kind confusion.** Names hide *what sort of thing* is being named (System vs Episteme vs Role vs Service, etc.), leading to category errors and brittle integration.
4. **Threshold‑in‑the‑name.** Numeric limits, duty segregation, or state qualifiers get baked into names (“Critical‑Reviewer‑0.2 mm”), which cannot age or compose.
5. **Stealth renames.** Quiet label swaps, steered by fashion or politics, sever continuity with earlier evidence, plans, and bridges.
6. **Explosion by synonyms.** Teams mint many near‑synonyms instead of reusing a Concept‑Set row or creating an explicit Bridge with loss notes.

These failures erode trust, block reuse, and make Part F machinery (Concept-Sets, `U.RoleDescription`, Bridges) harder to apply.

### 3. Forces

| Force                                      | Tension to balance                                                                                                            |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| **Local truth vs Cross‑context portability**  | The name must “belong” inside one context while remaining referenceable from other contexts through explicit bridges.               |
| **Human ergonomics vs conceptual clarity** | Short, natural labels help teams move; explicit kind and Context cues keep reasoning sound.                                          |
| **Stability vs evolution**                 | Names should be durable, yet easy to deprecate or refine without breaking links to past evidence and work.                    |
| **Brevity vs auditability**                | A compact “badge” for everyday speech, plus an authoritative **Name Card** that records meaning, scope, edition, and lineage. |
| **Parsimony vs inclusivity**               | Reuse existing Concept‑Set rows where possible; mint new names only when indispensable in the local context.                     |

### 4. Solution — The Local‑First Naming Protocol

F.18 defines **eight rules** (R‑rules) and **six practices** (P‑practices). Together they produce **Name Cards** that any reader can interpret **ontologically** without guessing, and that slot cleanly into the rest of Part F.

**Path Card (subset of Name Card).** A **Name Card** whose **object‑of‑talk/entity-of-interest** is an **EvidenceGraph Path**: it cites a **PathId** (or **PathSliceId**), **Context**, **ReferencePlane**, **Γ_time**, and any **Bridge id(s) + CL/CL^plane** (with loss notes). Used by **G.6** and **G.10** to make justifications portable on UTS.

#### 4.1 The Eight R‑rules (normative)

**R1 — Speak every name *with its Context*.**
A name is **never** context‑free. When you introduce or use a name, **pair it with the Bounded Context** where it lives (the “Context of meaning”), and with the **edition** of that Context if relevant. In everyday speech: “X, *in* Y.” Cross‑context use requires a Bridge; labels alone do not travel. 

**R2 — State the ontological *Kind* on the Card.**
Every Name Card **must** state the **Kind** (System, Episteme, Role, Service, Method, Work, Objective, Requirement, Decision, Characteristic, etc.). This prevents category errors and keeps Role–Method–Work alignment clean. *Clarification:* this is a **Card requirement**, not a demand that the label string begin with the Kind.

**R3 — Declare the *Purpose / use‑domain* on the Card.**
In addition to **Kind**, the Name Card **must** state the intended **Purpose / use‑domain** that situates the concept in practice and signals **which families of contexts** are expected to use it (e.g., mathematical formalism, engineering practice, computer science, systems management). This enables reconstruction of usage from the lexicon and reduces unintended scope drift. *Clarification:* this is a **Card field**; it does **not** require the label string to carry the purpose qualifier.

**R4 — Resolve the name to a *Local‑Sense*.**
A minted name must resolve to a Local-Sense inside its Context (the result of F.2–F.3). If a name points to a Role Description, state that template and its sense basis. Avoid heavily overloaded surface terms: when needed, prefer concise two-word Tech labels that hint at the intended sense.

**R5 — Use *Twin Registers* (Unified Tech + Plain).**
Provide two human‑oriented labels on the Name Card, per **E.10** register discipline:
* a **Unified Tech** label (short, morphology‑stable, neutral in wording);
* a **Plain** label (reader‑friendly phrasing for managers and subject‑matter experts).

The **Unified Tech** label is the only one used in **Core** normative prose; **Plain** is for teaching and examples. Both remain **context‑local**; neither establishes Cross‑context identity (that is the job of the **UTS row** and **Bridges**).



+The **Unified Tech** label is the only one used in **Core** normative prose; **Plain** is for teaching and examples. Both remain **context‑local**; neither establishes Cross‑context identity (that is the job of the **UTS row** and **Bridges**).


**R6 — Keep thresholds and states *out of the name*.**
Do not encode numeric limits, separation‑of‑duties, or readiness states in the label. Put thresholds on **Method steps** (capability/acceptance), states in **Role State Graphs**, and SoD via **incompatibility** relations. Names carry *what this is* and *which Context claims it*—not *when and how it may act*.

**R7 — Cross‑context only by *Bridge* with loss notes.**
When another Context needs to reference a name, use an **Alignment Bridge** that states the relation (equivalent, narrower, broader, analogous) and its **Congruence Level** with explicit **loss/fit** annotations. Never equate two names by label alone.

**R8 — Make renames and merges *first‑class events*.**
When a label changes, or two labels consolidate or split, record it on the Name Card as a lifecycle action (rename, merge, split, retire) with rationale and dates. Past uses *remain valid as historical facts*; continuity comes from lineage, not silent edits.

#### 4.2 The Six P‑practices (normative process)

**P1 — Candidate set (*NQD-front* of seed-words).**
Do **not** pick a label “in one shot”. Build a **small, non-dominated candidate set** (an *NQD-front*, typically 5–10 items) by seeding and varying along:
**Traditions** — mathematics, physics, engineering, computer science, systems thinking, management, etc. with their typical contexts and situations; use maximum diversity here;
 **Novelty/Familiarity** — from careful **reuse** of established terms to sharper **neologisms** from recent SoTA traditions;  
 **Lexical form** — distinct **head terms** and morpheme families, readability/pronounceability, inflection/declension, transparency.
Use the **Novelty–Quality–Diversity** discipline from **Part G** to maintain only **non-dominated** candidates; when appropriate, you may implement this via **Γ_nqd.generate (G.18)**. Record the **seeds** and the short rationale in the Card’s notes. Choose final **Unified Tech**/**Plain** labels **from this frontier**; if a strong candidate is discarded, briefly note why.

For the purposes of **Diversity_P**, group candidates into **head-term families** (same base noun/verb + minor prepositions or case endings). Variants such as *“Reference plane”*, *“Plane of reference”* and *“Referred plane”* **count as one family**, not three distinct candidates. An NQD-front with multiple near-clones from one family **does not** satisfy the diversity requirement. Aim for **≥ 3 distinct head-term families** in the CandidateSet; if the front ends up with fewer families (e.g. due to a very narrow domain or strong AliasRisk on other heads), the Name Card **MUST** record a brief rationale in the NQD-front notes.

**Lexical Q‑axes for the NQD‑front**
When P1 uses **NQD‑CAL (C.18)**, treat the **Quality vector** over candidates as part of the same archive as C.18’s **NQD‑frontier**. Recommended axes (all **ordinal; no arithmetic means**):

 * **SemanticFidelity (P — Ontological precision).**
  *Question.* Does the label verify against the **Minimal Definitional Statement (MDS)** and Concept‑Set row without adding or losing core invariants?
  *Scale (ordinal; ↑ better).* `{Misleading, Vague, Precise, Exact}` with `Exact ≻ Precise ≻ Vague ≻ Misleading`.  
  *Link to P2.* When **P2** is run, derive the SemanticFidelity rating from the per‑sense‑seed judgements: candidates with any **core** sense‑seeds classified as `wrong‑prototype` **MUST** be rated **Misleading**; candidates rated **SemanticFidelity ≥ Precise** **SHOULD** have at least a configurable fraction `θ_P` (default `θ_P = 0.7`) of sense‑seeds in `on‑target` and **NONE** in `wrong‑prototype`. Discard candidates that remain **Misleading** after revision.

* **CognitiveErgonomics (S — Sociolinguistic admissibility).**  
  *Question.* Can the target **RoleEnactors** (engineers, managers) read, pronounce, and recall the label without specialist training?  
  *Scale (ordinal; ↑ better).* `{Alienating, Jargon, Acceptable, Natural}` with `Natural ≻ Acceptable ≻ Jargon ≻ Alienating`. Prefer labels **≥ Acceptable** in the home Context.

* **OperationalAffordance (O — Morphological/action alignment).**
  *Question.* Does the morphology of the label hint at its role in **methods/morphisms** (object vs process vs result) and support the required derivational family (noun/verb/participial forms)?
  *Scale (ordinal; ↑ better).* `{Opaque, Role‑hinting, Action‑aligned}`. Action‑aligned labels make it obvious whether we are naming an **actor**, an **activity**, or an **artifact** (e.g., *Author* vs *Authoring* vs *AuthoredArtifact*).  
  *Kind‑sensitive cues.* When the **Kind** on the Card is a **Role**, prefer agentive/holder morphology (*…Role*, *…er*, *…or* or local equivalents); when the Kind is **Method/MethodDescription**, prefer verbal or gerundive forms; when the Kind is **Holon**, prefer result nouns, when **Work**, prefer verb. Misaligned morphology (e.g., a Role named with a pure process noun) should be treated as a **penalty on OperationalAffordance** and, if retained for legacy or regulatory reasons, called out explicitly in **Card notes**. See F.5/F.11/F.12 and **LEX‑BUNDLE §8**.

* **AliasRisk (A — Lexical overload).**  
  *Question.* How likely is a careful reader to import a **wrong sense** from neighbouring FPF artefacts or external canons when they see this string?  
  *Scale (ordinal; ↓ better).* `{Safe, Context‑dependent, High‑Risk, Overloaded}` with `Safe ≻ Context‑dependent ≻ High‑Risk ≻ Overloaded`. Avoid adopting **Overloaded** labels unless required by legacy and called out explicitly in notes. When C.18’s **DomainDiversitySignature** is available, AliasRisk MAY be refined into a CHR‑typed characteristic with the same polarity.

Use these axes for **Pareto comparison only** (per **C.16** ordinal discipline). Do **not** collapse them into a single scalar score; the NQD‑front is computed over the **vector of lexical Q‑components** together with **Novelty** and **Diversity_P**.

**P2 — Semantic read‑through against archetypal situations.**  
Alongside the NQD‑front of label candidates, maintain a **small set of 5–10 archetypal situations** (“**sense‑seeds**”) that instantiate the intended use (purpose) across different traditions. For **each** candidate label and each sense‑seed, perform a **read‑through test**:  
– write **1–2 short example sentences per sense‑seed** (e.g., “In case X, we perform \<Label\>”);  
– classify the outcome, for a careful reader in the home Context, as one of `{too‑narrow, on‑target, too‑wide, wrong‑prototype}`.  
Maintain, on the Name Card, a small tally per candidate of how many sense‑seeds fall into each class. Use these tallies both to **prune candidates** and to instantiate **SemanticFidelity** (P‑axis): labels with a sustained pattern of `wrong‑prototype` hits on core sense‑seeds **SHALL** be removed from the NQD‑front (or kept only as deprecated aliases with an explicit warning). Candidates rated **SemanticFidelity ≥ Precise** **SHOULD** satisfy the `θ_P` constraint from the SemanticFidelity definition (fraction of `on‑target` seeds) and have no `wrong‑prototype` counts.  
Record **rejected candidates** and their **mismatch patterns** in the Name Card’s **NQD‑front notes**.

**P3 — Mint‑or‑Reuse gate (F.8).**
Before minting, search your Context’s **Concept‑Set table**. If a row already covers your sense, reuse it and only add a **local label**. If not, propose a **new row** and capture the decision in a brief rationale.

**P4 — Concept‑Set linkage (F.7).**
Every Name Card **must** indicate its Concept‑Set row (or record “not applicable” for intentionally Context‑unique names). This is the handle for alignment and anti‑explosion control.

**P5 — UTS registration (F.17).**
Publish each Name Card to the **Unified Term Sheet** with Context, kind, twin labels, sense anchor, edition, and lifecycle status. Keep the UTS the single, human‑readable table of record.

**P6 — Lifecycle hygiene (F.13).**
Apply the same discipline to renames, splits/merges, and retirements; leave a forward/backward pointer so readers can trace continuity at a glance.

### 5. The Name Card (authoring template, representation-agnostic)

#### 5.1 Card purpose & mode guard (normative)

To prevent “post-hoc justification” of intuitively chosen labels, every **Name Card** SHALL declare its
**CardMode ∈ {MintNew, DocumentLegacy}**:

* **MintNew.** The Card is the **output of an NQD-style lexical search** over a **candidate label set** generated inside
  the home Context(s), using the lexical Q-tuple `{SemanticFidelity, CognitiveErgonomics, OperationalAffordance,
  AliasRisk}` together with **Novelty (N)** and **Diversity_P** (per A.0 / C.17–C.18 / B.5.2.1).  
  – The Card SHALL record:  
    – a minimal **CandidateSet** (the labels actually evaluated), with **head-term family** tags for each candidate;  
    – the resulting **NQD-front** of **non-dominated candidates** over ⟨Q-tuple, N, Diversity_P⟩;  
    – a short **selection note** explaining why the chosen Tech/Plain pair was picked from that front
      (e.g., “better CognitiveErgonomics at equal SemanticFidelity”).  
 
  – A single-element NQD-front is permitted only if the Card records a brief rationale why **no alternative candidate
    survived** the lexical and NQD filters (e.g., legacy constraints, strong AliasRisk on all other options).

* **DocumentLegacy.** The Card documents an **externally imposed legacy label** (e.g., a regulatory or de facto Standard)
  and its mapping to FPF structures. In this mode the Card MAY omit a full NQD-front, but SHALL:  
  – state the **legacy source / provenance**;  
  – either (i) provide at least a **sketched NQD-comparison** of viable internal variants against the legacy label, or  
    (ii) record a short **out-of-scope rationale** (e.g., “name frozen by law; see cited Standard”) explaining why NQD
    search is not being used for selection.

For all **Core-surface naming of U.Types and other canonical FPF concepts**, **MintNew** is the **default** CardMode; using
DocumentLegacy for such names requires an explicit justification on the Card.

A **Name Card** is the authoritative, human‑readable record of a name inside its Context. It has these fields; teams may add local notes.

1. **Row ID** — the stable, opaque **UTS row identifier** (the identity anchor).
2. **Twin labels** — **Unified Tech** and **Plain** (per E.10).
3. **Context of meaning** — the Bounded Context and, if relevant, its edition.
4. **Kind** — what sort of thing this is (System, Episteme, Role, Service, Method, Work, Objective, Requirement, Decision, Characteristic, etc.). This is an **ontological category**, not a surface‑string prefix. 
5. **Purpose / use‑domain** — the intended area(s) of use (which families of contexts are expected to use it).
6. **Minimal Definitional Statement (MDS)** — one‑paragraph intended sense in the home context (no tool/process slang).
7. **Didactic subtitle** — ≤ 12 words that signal pragmatic use.
8. **Sense reference** — a Local‑Sense reference (how F.2–F.3 clustered it).
9. **Concept‑Set linkage** — Concept‑Set reference or “not applicable” (with rationale).
10. **Alignment note** — if a Bridge exists to other Contexts, cite it and record **loss/fit** in plain words (no formulas required on the Card).
11. **Relation kind** — if the name is for a relation, declare **structural** vs **epistemic** and `validationMode ∈ {axiomatic, inferential, postulate}`. For **structural** relations, provide **Constructive** grounding (`tv:groundedBy → Γₘ.sum|set|slice`). If the name is not for a relation with arity ≥ 2, set this field to “n/a”.
12. **Manager’s clip** — one‑line “use/avoid” guidance for everyday communication.
13. **Archetypal situations (sense‑seeds)** — **5-10 short “X‑case” lines** used by **P2** for the semantic read‑through; keep them **edition‑aware** and **context‑local**.
14. **NQD‑front seeds** — brief rationale for discarded candidates (**include mismatch patterns from P2 and any lexical Q‑scores used in P1**).
15. **SemanticFidelity/CognitiveErgonomics/OperationalAffordance/AliasRisk** scores for the NQD-front labels.
16. **Version**  — current status and history of editions.
17. **Card notes** — optional free text with comments about the name (e.g., recommended translations, etymology, pronunciation). 

**Manager’s reading habit.** When two names collide in a meeting, ask for their **Context**, **Kind**, **Purpose/use‑domain**, and **Sense anchor**. If any of those differ, you are comparing different things; switch to **Bridge** talk, not label talk.

### 6. What *belongs* in the label—and what does not

**Belongs (keeps the label clean and durable):**

* The **core head word** that names the thing *(the **Kind** is recorded on the Card; the string need not encode it)* (e.g., “Pump”, “Standard”, “Requirement”, “Surgeon”, “Cooling”).
* A **purpose qualifier** if it is essential to the local sense and stable across editions (e.g., “Cooling” vs “Fuel”).
* A **scope qualifier** only if it is part of the *meaning* rather than the current plan (“Surgical Ward” rather than dates or batch numbers).

**Does not belong (move elsewhere):**

* **Numbers and thresholds** (put on steps, capabilities, acceptance clauses).
* **States** (use Role State Graphs and checklists).
* **Temporal windows** (work plans and history).
* **Organisational authorisations** (speech acts and assignments).
* **Imported acronyms** from other Contexts (use Bridges with loss notes instead).

**Quick litmus for authors.** If removing a number, date, or state *does not* change the *meaning* of the thing, it should **not** be in the label.

### 7. Worked triad (three short, context‑local examples)

*(Names below are illustrative; the same words in other Contexts may mean something else. The point is how the Name Card keeps them clear.)*

#### 7.1 Industrial operations Context: “Thermal Management · 2026”

* **Kind:** Service
* **Purpose / use‑domain:** industrial thermal utilities; line‑level planning and operations
* **Unified Tech label:** Cooling Supply
* **Plain label:** Chilled water for line B
* **Sense anchor:** supply of water at defined temperature/flow to boundary B
* **Concept‑Set:** “Utility service” row; local variant recorded
* **Alignment note:** Bridge to “Plant Utilities · 2026” notes that “Cooling Supply” there bundles filtration; *loss:* filtration is not guaranteed in this Context
* **Version:** 20 Feb 2024
* **NQD‑front (seed candidates):** *Cooling Supply*, *Chilled Water Service*, *Process Cooling*, *Cooling Utility*. **Chosen:** *Cooling Supply* (neutral, morphology‑stable).

**Why it’s good.** The label doesn’t encode temperature or flow limits (those live in acceptance). It names a Service; nobody will confuse it with a pump System or a Method.

#### 7.2 Clinical Context: “Hospital OR · 2026”

* **Kind:** Role
* **Purpose / use‑domain:** OR governance and staffing; credentialing and checklists
* **Unified Tech label:** Surgeon Role
* **Plain label:** Operating surgeon
* **Sense anchor:** person who is authorised to perform surgical steps under defined checks
* **Concept‑Set:** “Clinical roles” row
* **Alignment note:** Bridge to “Training & Credentialing · 2026” shows partial overlap; *loss:* that Context’s “Senior Surgeon” carries teaching duties that do not apply here
* **Version:** Feb 2025; renamed‑from “Lead Surgeon” (2025) with rationale: avoided “lead” vs “operating” ambiguity
* **NQD‑front (seed candidates):** *Surgeon Role*, *Operating Surgeon*, *Primary Surgeon*, *Operating Physician*. **Chosen:** *Surgeon Role* (Kind‑neutral string; Plain clarifies).
*Lexical Q snapshot (PSOA‑style, informative).*  

| Candidate | SF | CE | OA | A‑Risk | Comment |
| --- | --- | --- | --- | --- | --- |
| Surgeon Role | Precise | Acceptable | Role‑hinting | Safe | Neutral head noun; morphology matches **Role** Kind; works across departments. |
| Operating Surgeon | Precise | Natural | Role‑hinting | Context‑dependent | Reads well, but “operating” competes with “operating theatre/room”; kept as Plain label only. |
| Primary Surgeon | Vague | Natural | Role‑hinting | Context‑dependent | “Primary” ambiguous (training vs shift); rejected for governance vocabulary. |
| Operating Physician | Vague | Jargon | Role‑hinting | High‑Risk | Collides with non‑surgical physician roles; rejected despite familiarity in some hospitals. |
 
**Why it’s good.** No fatigue thresholds or readiness states in the name; those live in the Role’s state graph and checklists.

#### 7.3 Public service Context: “Civic Services · 2026”

* **Kind:** Requirement
* **Purpose / use‑domain:** service performance management; public service SLAs
* **Unified Tech label:** Passport Lead‑Time
* **Plain label:** Time to issue a passport
* **Sense anchor:** elapsed time from complete application to issuance
* **Concept‑Set:** “Service quality requirements” row
* **Alignment note:** Bridge to “Legal Framework · 2026” records that legal “deadline” has different remedies; *loss:* legal exemptions not carried into this Context
* **Version:** current
* **NQD‑front (seed candidates):** *Passport Lead‑Time*, *Issuance Time*, *Service Turnaround*, *Time to Issue Passport*. **Chosen:** *Passport Lead‑Time* (neutral; Plain remains didactic).

**Why it’s good.** Target values (e.g., ≤ 20 days) are not in the label; they live in acceptance clauses.

---

### 8. Conformance Checklist (editor aid) — *Part I: naming & cards* (**non‑normative**)

**CCE‑F18.1 (Context pairing).**
Every name used in normative text **must** be paired with its **Context of meaning**. If you cannot name the Context, you do not have a valid name.

**CCE‑F18.2 (Kind clarity).**
Every Name Card **must** state the **kind** (System, Episteme, Role, Service, Method, Work, Objective, Requirement, Decision, Characteristic, …). Using labels that hide kind is non‑conformant.

**CCE‑F18.2a (Purpose declared).**
Every Name Card **must** state the **Purpose / use‑domain** (families of contexts where the concept is expected to be used). Omitting Purpose is non‑conformant.

**CCE‑F18.3 (Sense anchoring).**
A minted name **must** resolve to a **Local‑Sense** in its Context. If a sense cannot be stated, label minting is deferred.

**CCE‑F18.4 (Twin registers).**
Each Name Card carries a **Unified Tech** and a **Plain** label (E.10). Tech appears in **Core** prose; Plain in teaching/examples.

**CCE‑F18.5 (No thresholds/states in labels).**
Numeric limits, readiness states, and separation‑of‑duties **must not** appear in labels. Put them on steps, checklists, and role algebra.

**CCE‑F18.6 (Bridge‑only travel).**
Cross‑context reuse of a name **must** go through an **Alignment Bridge** with an explicit relation and **loss/fit** notes. Label matching alone is forbidden.

**CCE‑F18.7 (Lifecycle visibility).**
Renames, splits/merges, and retirements **must** be recorded on the Name Card with dates and rationale. Past occurrences remain valid as historical facts.

**CCE‑F18.8 (Mint‑or‑Reuse gate).**
Before minting, authors **must** check the Context’s Concept‑Set table; if a row exists, **reuse** it with a local label unless a documented reason compels a new row.

**CCE‑F18.9 (UTS entry).**
Names used in normative artefacts **must** appear on the **Unified Term Sheet** with the specified **Name‑Card fields**; include Notes when present).

**CCE‑F18.10 (No cross‑kind labels).**
Do not reuse the same **Unified Tech label** for different kinds inside one context (e.g., “Cooling” as a Service and as a Method). If unavoidable, add a stable qualifier to disambiguate and record the decision on both Name Cards.

**CCE‑F18.11 (Manager’s clip).**
Each Name Card **should** carry a one‑line “use/avoid” note to guide everyday speech. Where omitted, editors add it during review.

**CCE‑F18.12 (Anti‑explosion check).**
If three or more near‑synonyms for the same Local‑Sense appear in drafts, authors **must** either consolidate to one label or record an intentional synonym pair with use/avoid notes and a plan to converge.

### 9. Normative Standard (what must be true)

> This section is binding. It specifies the publication Standard for unification‑oriented names in the Unification Suite (Part F), with **local‑first authority**, **bounded context clarity**, and **one‑way unification** upwards along the ladder. It complements, and does not replace, the structural and epistemic Standards elsewhere in FPF.

**9.1 Local authority & home.**
Every unification name has a **single home**: exactly one *Bounded Context* that authors and stewards it. The home is responsible for the definition, examples, and lifecycle of the name. Cross‑context reuse happens by **bridges**, not by relocating the home.

**9.2 Minimum definitional payload.**
A published name MUST ship with a human‑readable **Minimal Definitional Statement (MDS)** that states the intended sense in the home context, and a **Didactic Subtitle** (≤ 12 words) that signals its pragmatic use. The MDS must be free of process slang and implementation jargon.

**9.3 Row ID + label surfaces.**
For each adopted name, the home supplies:
* a **Row ID** (the opaque UTS identifier — the **identity anchor**), and
* two **label surfaces**: a **Unified Tech** label (for Core prose) and a **Plain** label (for teaching).
  Both labels refer to the same underlying sense; **Plain** may simplify terms, not premises.

**9.4 One‑way dependencies.**
Each rung on the ladder depends only **downwards**: a name at rung *n* can rely on names ratified at rungs ≤ *n*, never sideways or upwards. Cycles are prohibited. If a dependency is not yet ratified at the required rung, the new name remains Draft or Pilot.

**9.5 Local‑first before reuse.**
Teams MUST first **identify and stabilize the local sense** (within their Bounded Context). **Within the home**, reuse existing **Concept‑Set rows** where they fit (§4.2 **P1**). **Across contexts**, reuse occurs via **Alignment Bridges** that map the local sense to an existing sense elsewhere—without collapsing the local home.

**9.6 Sense, not string.**
Publication concerns **sense** (intended meaning in context), not the literal string. Synonyms are allowed as **Plain** labels or **aliases** only if they point to the same **Row ID** and pass the conformance checks in §15 (“CC‑F18”). Strings must not be treated as identity.

**9.7 Relation-kind discipline (structural vs epistemic).**
If the public name surfaces a **structural relation**, its intended sense **MUST** be backed by *exactly one Constructive trace* in the structural calculus (Compose-CAL) and **SHALL** declare `validationMode=axiomatic` (see E.14). If the name surfaces an **epistemic relation**, Constructive backing is optional; **declare** `validationMode ∈ {inferential, postulate}` and use **Logical/Mapping** and/or **Empirical Validation** as appropriate. **Do not mix relation kinds** inside a single name. *(Do not use “Tier-1/2”; formality is expressed via F per C.2.3.)*

**9.8 Member vs Component.**
Names that describe collection membership MUST NOT be used to imply part‑whole structure, and vice versa. If both aspects are needed, publish two names with their own MDS and an explicit bridge.

**9.9 Lifecycle states.**
A name travels through **Idea → Draft → Pilot → Ratified → Deprecated**. Transitions require explicit human review gates. Ratified names carry a clear stewardship contact and date.

**9.10 Anti‑duplication duty.**
Before ratification, the home MUST perform a **near‑neighbor review**: identify adjacent names, record the decision to align, merge, or keep separate, and publish the rationale in the name’s record.

**9.11 Local clarity over global neatness.**
When in doubt, prefer **local intelligibility** for practitioners over global symmetry. Global neatness can be achieved later via bridges; loss of local sense is hard to repair.

**9.12 No imported tool terms in Core names.**
Names and their MDS must not carry terms whose only meaning is tied to operating tools or pipelines. If such terms are unavoidable in pedagogy, confine them to Working-Names and examples with disclaimers.

**9.13 Human‑only conformance.**
Conformance for this protocol is judged by trained human reviewers using the author/reviewer checklists in §14 and the conformance criteria in §15 (“CC‑F18”). Automated heuristics, if any exist in an organization, have no standing in the Core.

### 10. Rationale (why this exists and why these rules)

**10.1 Local‑first unlocks velocity without lexical debt.**
Centralized naming regimes seem tidy but slow learning and create brittle compromises. Local‑first minting lets teams speak clearly **now**; unification comes from disciplined bridges and one‑way dependencies, not from premature centralization.

**10.2 One home lowers ambiguity.**
Names with “many owners” drift. A **single home** concentrates accountability for sense, examples, and lifecycle, while still enabling broad reuse via alignment bridges.

**10.3 Unified Tech + Plain serve two audiences.**
Engineers need **precise** wording; managers and stakeholders need **approachable** wording. Splitting the surfaces keeps the same sense while protecting accuracy and pedagogy; both are anchored by the **Row ID**.

**10.4 One‑way ladder prevents conceptual knots.**
Acyclic dependencies cut off circular definitions and policy deadlocks. The ladder provides a simple mental model: *build on what is already firm*.

**10.5 Relation-kind discipline prevents category errors.**
Part-whole claims **(structural)** must rest on **Constructive** grounds (`tv:groundedBy → Γₘ.sum|set|slice`, `validationMode=axiomatic`). Experience-based or evaluative relations **(epistemic)** follow assurance rules (**Logical/Mapping**, and **Empirical Validation** when *postulate*), with an explicit `validationMode ∈ {inferential, postulate}`. Mixing relation kinds inside a single name confuses review and invites hidden assumptions. 

**10.6 Sense over string reduces false conflicts.**
Disputes often orbit the string (“we hate that word”). By separating **sense** (what we mean) from **string** (how we say it), the protocol enables peaceful coexistence: keep the **Row ID** constant; use one **Plain** label and, where helpful, a budgeted **alias** per register.


### 11. Application Guidance (how to apply, step by step)

**11.1 Prepare (30–60 min).**

* Clarify **your Bounded Context** and audience.
* Collect 2–3 typical user stories that require the name.
* Scan near‑neighbors in adjacent contexts (see §14.2 Reviewer checklist).

**11.2 Mint locally.**

* Write the **MDS** in plain language, one paragraph.
* Draft a **Didactic Subtitle** (≤ 12 words): “what this name buys you.”
* Decide whether the intended **relation kind** is **structural** or **epistemic** (do not mix), and declare `validationMode`.

**11.3 Choose surfaces.**

* **Unified Tech label**: concise, morphology‑stable, neutral; avoid metaphor.
* **Plain label**: approachable phrasing for non‑specialists.
* **How to choose**: pick both **from a small NQD‑frontier** (see §4.2 P1 (candidate set), P2(read-through)): diversify by tradition, novelty/familiarity, and lexical form; record discarded contenders and rationale on the Card.

**11.4 Place on the ladder.**

* Verify all dependencies are at the same rung or below.
* If a dependency is still Draft/Pilot, keep this name at most Pilot.

**11.5 Align, don’t erase.**

* Where overlap exists with another context, propose an **alignment bridge**.
* Keep your home; record the mapping and any known divergence in reading.

**11.6 Publish and steward.**

* Publish the name with MDS, subtitle, rung, home contact, examples.
* Schedule a **first refresh**: when should the home examine usage and drift?

**11.7 Deprecate gracefully.**

* If the sense is superseded, publish **Deprecation Notes**: what to use instead, and why. Keep old Working-Names visible long enough to allow safe migration.

**11.8 The “Friday test.”**

* On a busy Friday, could a competent colleague apply the name correctly using only the MDS, subtitle, and two examples? If not, refine before ratification: it too overloaded with meanings to be helpful.

### 12. Examples (worked mini‑cases for engineer‑managers)

> These examples are deliberately simple. They show how local‑first minting, one‑way unification, and tier discipline operate together.

**12.1 “Module” vs “Component” (engineering structure).**

* *Home A (Platform)* mints **Component** with MDS: “A physically or logically integrated part whose removal would alter the integrity of the whole.” **Structural**.
* *Home B (App Team)* mints **Module** with MDS: “A deployable bundle of functionality maintained as a unit.” **Epistemic** (usage practice), not a structural claim.
* **Unification:** An alignment bridge states: “In Platform, every Component may host one or more Modules; Modules are not Parts.” Dependencies are one‑way: *Module* depends on *Component*; *Component* does not depend on *Module*. No synonymy asserted. Both names remain in their homes.

**12.2 “Incident” vs “Event” (operational sense).**

* *Home C (Operations)* mints **Incident** with MDS: “An unplanned interruption or reduction in the quality of a service.” **Epistemic**.
* *Home D (Monitoring)* mints **Event** with MDS: “A recorded observation of a state change in a system.” **Epistemic**.
* **Unification:** Bridge notes: “Some Events are Incidents when they degrade service; not all Events are Incidents.” **Plain** labels (and at most one alias per register) may vary (e.g., “Outage” as an alias for **Incident**), but the **Row IDs** stay distinct. No part‑whole claims are implied.

**12.3 “Customer” vs “Account Holder” (business roles).**

* *Home E (Sales)* mints **Customer**: “A party that receives value from an offering in exchange for consideration.” **Epistemic**.
* *Home F (Finance)* mints **Account Holder**: “A party legally responsible for an account.” **Epistemic**.
* **Unification:** Bridge states overlaps and divergence: “A Customer can be an Account Holder; an Account Holder may not be a Customer (e.g., trustee).” The homes retain stewardship; a shared Working-Name “Client” may be used in executive materials with a clear note: **Working-Name only; see Concept-IDs for decisions**.

**12.4 “Batch” vs “Lot” (collection vs integration).**

* *Home G (Manufacturing)* mints **Batch**: “A collection of items produced under shared conditions.” **Epistemic membership**.
* *Home H (Quality)* mints **Lot**: “An integrated whole packaged and tracked as one item.” **Structural whole**.
* **Unification:** Bridge notes: “A **Lot** may originate from a single **Batch** or a slice of a Batch; not every Batch yields a single Lot.” Relation mapping: **MemberOf** (Batch membership) vs **ComponentOf**/**Whole** (Lot integration). *Loss note:* membership evidence does **not** imply part‑whole structure; part‑whole structure does **not** imply shared production conditions.

### 13. Anti‑Patterns & Failure Modes (what to avoid)

**13.1 “Global name first.”**
Trying to coin a single global string before local understanding is mature. **Fix:** mint locally, publish MDS, then align.

**13.2 “Synonym storm.”**
Collecting many strings without stabilizing the Concept-ID. **Fix:** one Concept-ID per sense; multiple Working-Names only if they truly help didactics.

**13.3 “Process leakage into names.”**
Burying workflow or tool steps inside the MDS. **Fix:** keep process in method descriptions; keep names about sense, not procedure.

**13.4 “Member‑implies‑part.”**
Letting collection names induce part‑whole claims. **Fix:** separate names, separate MDS; don’t smuggle structure into membership.

**13.5 “Sideways dependency.”**
Defining a name by appealing to another Draft at the same rung or higher. **Fix:** depend only downward or postpone ratification.

**13.6 “Alias/Plain drift.”**
Letting a Plain label or alias accumulate extra meanings absent in the underlying row. **Fix:** periodic label review; prune metaphors that start bending sense; respect the alias budget.

### 14. Assurance & Conformance (human‑only checks)

**14.1 Author checklist (before requesting review).**

* [ ] I identified the **home Bounded Context** and audience.
* [ ] I wrote a clear **MDS** (≤ 1 paragraph) and a **Didactic Subtitle** (≤ 12 words).
* [ ] I declared the **relation kind** (structural vs epistemic) and the **validationMode**; no mixing.
* [ ] If **structural**, I can point to **exactly one Constructive trace** that backs the structural claim.
* [ ] I surveyed near‑neighbors and recorded my decision to align, merge, or keep separate.
* [ ] I produced both **Unified Tech** and **Plain** labels (per E.10), with the same sense and pointing to the same **Row ID**.
* [ ] Dependencies point **only downward**; no sideways or upward pulls.
* [ ] I scheduled a **refresh date** and listed 2–3 usage examples.

**14.2 Reviewer checklist (at the gate).**

* [ ] One home is declared; stewardship contact is clear.
* [ ] The MDS is free from process jargon and implementation slang.
* [ ] The declared **relation kind** is justified; **structural** claims are constructively grounded; **epistemic** claims declare `validationMode` and evidential posture.
* [ ] Member vs Component is respected where relevant.
* [ ] Alignment bridges are proposed where overlap exists, with explicit reading of convergence/divergence.
* [ ] The ladder discipline holds: acyclic, downward‑only dependencies.
* [ ] The **Plain** label does not smuggle extra commitments; **Unified Tech** and **Plain** remain co‑referential and point to the same **Row ID**.
* [ ] Lifecycle state is accurate (Idea/Draft/Pilot/Ratified/Deprecated) and dated.

**14.3 Lightweight outcomes.**

* **Ratify** (meets all checks).
* **Pilot** (publish with explicit questions and a refresh date).
* **Revise** (return to author with targeted gaps).
* **Merge** (replace with an alignment to an existing name).
* **Deprecate** (publish successor guidance and sunset plan).

## 15 · Conformance Criteria (normative “CC‑F18”)

> These are **language‑level** obligations for authors and reviewers. They ensure every unified name is **local‑first**, **bridge‑aware**, and **teachable**.

**CC‑F18‑1 (Context first).** Every unified name **SHALL** be grounded in **local senses** that were harvested and clustered **inside named Contexts** (“context of meaning”) prior to unification. No name may be minted from free‑floating glosses or Cross‑context intuition. Use F.1–F.3 first.

**CC‑F18‑2 (Bridge‑only sameness).** Claims of sameness across Contexts **SHALL** be expressed only via explicit **Bridges** with a stated congruence and loss note. Mere spelling similarity never licenses a unified name. Use F.9.

**CC‑F18‑3 (Twin‑register naming).** Each unified concept **SHALL** carry **two labels**—a **Unified Tech** label (used in Core prose) and a **Plain** label (used for teaching). Labels are chosen per the naming discipline of F.5 and the register rules of **E.10**.

**CC‑F18‑4 (Neutrality of the Tech label).** The **Unified Tech** label **SHALL NOT** be borrowed wholesale from any single source Context where that borrowing would re‑import that Context’s private distinctions. Prefer a **neutral** term; **Cross‑context reuse occurs only via the UTS row and explicit Bridges**. (See F.5 “allowed/forbidden forms”.)

**CC‑F18‑5 (One concept per row, one Tech label per row).** A unified concept **SHALL** be captured as **one Concept‑Set row** in the **UTS**. Exactly **one Unified Tech label** is normative for that row; additional legacy strings are aliases in Annex (budgeted). Use F.7 with F.17.

**CC‑F18‑6 (SenseCell citations).** For each unified name, the **SenseCells** (Context × Local‑Sense) that justify it **SHALL** be cited in the UTS row with **Context name + edition**. Omit edition only if the Context has a single stable edition. See F.17 §6.

**CC‑F18‑7 (Sheet‑level coverage).** Within a thread’s UTS, the **set of rows** carrying unified names **SHALL** collectively cite **≥ 3 distinct Contexts**, ensuring breadth of evidence. Coverage is a property of the **sheet**, not of every single row. See F.17 §6 constraint.

**CC‑F18‑8 (No global words).** In Core text, **“Context” always means `U.BoundedContext`**; **discipline columns** may be used in teaching layouts but **is not** a bearer of meaning. Do not write context‑free claims of sameness. See E.10 and F.17 §5.

**CC‑F18‑9 (Didactic primacy).** A unified name **SHALL** be teachable on **one page**: its **UTS row** + a short narrative that a careful reader can replay (F.16 template). If it cannot be taught concisely, the naming attempt is premature.

**CC‑F18‑10 (No lifecycle connotations).** Names **SHALL NOT** encode imagined “maturity stages” or time‑ordering unless those are part of the concept’s intension. Stages belong in **state‑space** and dynamics narratives, not in names. (See A‑series CHR patterns.)

**CC‑F18‑11 (Strict distinction guard).** Names **SHALL** respect **A.7 Strict Distinction**: do not collapse **Role ↔ Method ↔ Work** or **Status ↔ Description** into one word. Align with F.11/F.12 where relevant.

**CC‑F18‑12 (Change control via F.13).** Renames, splits, merges, and retirements **SHALL** follow F.13’s lexical continuity rules; the UTS remains the canonical public surface for these changes.

**CC‑F18‑13 (Lexical Pareto discipline).** When a Name Card uses **NQD‑CAL (C.18)** to score label candidates, the **chosen Unified Tech label** **SHALL** lie on the **Pareto frontier** of the lexical Q‑tuple `{SemanticFidelity, CognitiveErgonomics, OperationalAffordance, AliasRisk}` (per **C.16** ordinal discipline and P1’s NQD‑front definition), unless an explicit exception is recorded. If authors deliberately select a dominated candidate (e.g., to honour legacy regulation or user muscle memory), the Name Card’s notes **MUST** state the reason for stepping off the frontier.

**CC-F18-13 (NQD-front surfaced, with honest diversity).**  
When a Name Card is in **MintNew** mode, the **candidate label set** and the resulting **NQD-front of non-dominated label candidates** over the lexical Q-tuple `{SemanticFidelity, CognitiveErgonomics, OperationalAffordance, AliasRisk}` **SHALL** be explicitly recorded on the Card (at least as a small table or list), together with the NQD evidence hooks (`DescriptorMapRef`, `DistanceDefRef`, and a brief `Diversity_P` / coverage summary).  
Each candidate **SHALL** carry a **head-term family** tag; morphological or prepositional variants built on the same head (e.g. “X plane”, “plane of X”, “planar X”) **MAY NOT** be counted as distinct for Diversity_P. The Card **SHALL** indicate how many distinct head-term families are represented on the NQD-front.  
An NQD-front with fewer than **three** head-term families is permitted **only** if the Card records why no lexically more diverse alternatives survived the SemanticFidelity / AliasRisk filters (e.g., very narrow domain, frozen legacy idiom).

**CC-F18-14 (Selection from the front only).**  
The **Unified Tech** and **Plain** labels published on the UTS row for a unified concept **SHALL** be drawn from the currently recorded **NQD-front** on the Name Card. Publishing a Tech/Plain pair that is **not** on that front (or that is dominated with respect to the declared lexical Q-axes plus NQD) is **non-conformant**, except in explicit **DocumentLegacy** mode as defined in §5.1.

**CC-F18-15 (Mode declaration).**  
Every Name Card **SHALL** declare its `CardMode ∈ {MintNew, DocumentLegacy}`. For Core-surface naming of **U.Types** and other canonical FPF concepts, **MintNew** is the default; **DocumentLegacy** is permitted only when recording pre-existing external names and MUST (i) cite the legacy source, and (ii) either attach an NQD-front over viable FPF variants or record a short rationale why NQD search is out-of-scope.

## 16 · Anti‑patterns & safe rewrites (normative)

> Each item names a **speaking error** and a **local‑first repair**. Use this as an author’s lint pass before proposing a unified name.

| #  | Anti‑pattern (do **not** say)                           | Why it fails                                                    | Safe rewrite (how to speak)                                                                                         |
| -- | ------------------------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| A1 | “These terms are the same **because they look alike**.” | Cross‑context **spelling** is not evidence of conceptual identity. | “We assert sameness **via a Bridge**; the loss note explains what survives across Contexts.” (F.9)                     |
| A2 | “Use the BPMN word as our Tech label.”                  | Imports BPMN’s local commitments into the unified term.         | “Choose a **neutral** Unified Tech label; cite BPMN as a **SenseCell** in the row.” (F.5, F.17 §6)                  |
| A3 | “Merge *process* (recipe) with *process* (execution).”  | Collapses **MethodDescription** with **Work**.                  | “Split the concepts: one row for **MethodDescription**, another for **Work**; align them in examples.” (F.11/F.16)  |
| A4 | “Our name encodes the lifecycle stage.”                 | Lifecycle phrasing sneaks in time.                              | “Name the **concept**; show **state‑space** changes in examples, not in the label.” (A‑series CHR rationale)        |
| A5 | “Contextless glossary.”                                 | Violates local‑first; readers re‑globalise.                     | “Publish a **UTS** per thread; each row lists **Contexts** (Contexts+editions).” (F.17)                                |
| A6 | “We’ll fix synonyms later.”                             | Synonym sprawl grows costs.                                     | “Apply **E.10** rules now: one Tech, one Plain; retire extras via **F.13**.”                                        |
| A7 | “One mega‑row for everything service‑like.”             | Bundles distinct concepts; harms teachability.                  | “One **Concept‑Set per idea**; group with a **Block Plan** for pedagogy.” (F.17 §7)                                 |

---

## 17 · Migration notes (renames, splits, merges, retirements)

**M1 — Start from Contexts, not from the old global word.** When inheriting legacy names, first **re‑harvest** terms inside the chosen Contexts (F.2–F.3). Only then decide whether to **reuse** or **mint** (F.8).

**M2 — Preserve reader muscle memory without duplicating meaning.** Keep the **Plain** label close to familiar speech, but make the **Tech** label precise. If a legacy term is overloaded, publish it as a **deprecated alias** in Annexes, not as a second Tech label. (F.13; Part H “Deprecated Aliases”.)

**M3 — Prefer split‑then‑bridge over vague merges.** If one legacy word covers two distinct concepts, **split** into two rows and add a short **relation note** between them (e.g., “recipe vs run”). Do **not** hide the split under a wide new name. (F.7; F.16.)

**M4 — Keep identifiers stable; move rows between blocks.** When the **Block Plan** evolves, move rows rather than renumbering; record the move in the row’s **Notes** field. (F.17 §16.)

**M5 — Upgrade rationale quality with worked examples.** Every rename or split should be accompanied by a **one‑page example** that shows the new row in action across at least **two Contexts**. (F.16; “tell‑show‑show”.)

---

## 18 · Worked examples (compact)

> Each example shows **how the Protocol steers naming** so engineers and managers can communicate without hidden Cross‑context leaks.  
> **Card hygiene shown explicitly:** each example **states the Kind and the Purpose/use‑domain** and **chooses Tech/Plain labels from a small NQD‑frontier** (seed set diversified by traditions, novelty/familiarity, and lexical form; see Part G (G.18)).
> **Head-term diversity:** each example **MUST** also state the **distinct head-term families** represented in its NQD candidate set (lexical “roots” such as *Recipe*, *Run*, *Episode*, not prepositional/morphological variants). This prevents faking Diversity_P with near-clones of one head.

### Example 1 — *MethodDescription* vs *Work* (recipe vs run)

* **Context harvest:**
  *BPMN 2.0 (2011):* “Process model” (recipe) and “Activity instance” (run).
  *PROV‑O (2013):* `prov:Plan` vs `prov:Activity`.
  *ITIL:* “Work instruction” vs “Change implementation record.”
* **Kind:** `U.MethodDescription` (design‑time artifact) **and** `U.Work` (run‑time occurrence).
* **Purpose / use‑domain:** planning/scheduling vocabulary across BPMN, PROV‑O, ITIL; separates *design recipe* from *execution episode* for governance and telemetry.
* **NQD‑front (seed candidates):**  
  *design‑time:* *Procedure*, *ProcessModel*, *MethodSpec*, *WorkflowDefinition*, *Recipe*, *MethodScript*  
  *run‑time:* *Run*, *Execution*, *Enactment*, *ActivityInstance*, *Job*, *Episode*
* **Head-term families used (design/run):**  
  *design-time heads:* {Procedure, ProcessModel, MethodSpec, WorkflowDefinition, Recipe, MethodScript}  
  *run-time heads:* {Run, Execution, Enactment, ActivityInstance, Job, Episode}
* **Chosen from frontier (Unified Tech / Plain):**  
  `U.MethodDescription` / “recipe”; `U.Work` / “run”.  
  *Discarded highlights:* **Procedure** (collides with governance “procedure/policy”); **Execution** (overloaded in CS/security); 
* **Anti-pattern (for illustration only, non-conformant).**  
 > *Bad CandidateSet (lexically narrow):* {“Reference plane”, “Plane of reference”, “Planar reference”, “Ref. plane v2”}.  
 > All four are one **head-term family** (*plane*). Even if Diversity_P over raw strings looks high (four labels), **head-term diversity is 1**, so this set **fails** the F.18 diversity intent. A conformant Card would either: (a) add labels with other heads (e.g., *Layer*, *Track*, *Band*), or (b) explicitly record why other heads are rejected (AliasRisk, domain idiom) and accept low lexical Diversity_P with a rationale.
* **Enactment** (speech‑act nuance).
* **Bridges:** recipe↔run **related**, not identical; loss note “control‑flow vs. execution.”
* **Why it matters:** Managers can schedule **Work** while authors improve the **MethodDescription**—no category errors. The NQD‑front preserves tradition‑diverse, lexically stable options until a reasoned choice is made. (F.11/F.16; F.17 rows.)

### Example 2 — *Service* (promise) vs *SpeechAct* (utterance) vs *Commitment* (deontic)

* **Context harvest:**
  *IT service canon:* “SLA/OLA clause”, “ticket approved”.
  *Speech‑act theory:* “performative utterance”.
  *Org governance:* “approval signature”.
* **Kind:** `U.Service` (promise), `U.SpeechAct` (utterance), `U.Commitment` (deontic bond).
* **Purpose / use‑domain:** ops/governance vocabulary connecting ITSM, organizational policy, and pragmatics; separates saying, binding, and promising.
* **NQD‑front (seed candidates):**  
  *promise:* *Service*, *Offering*, *Provision*, *CapabilityOffer*  
  *utterance:* *SpeechAct*, *Performative*, *Utterance*, *Declaration*  
  *deontic bond:* *Commitment*, *Obligation*, *Binding*, *Duty*
* **Chosen from frontier (Unified Tech / Plain):**  
  `U.Service` / “service (promise)”; `U.SpeechAct` / “utterance”; `U.Commitment` / “commitment”.  
  *Discarded highlights:* **Offering** (business‑model connotations); **Declaration** (too narrow for performatives); **Obligation** (legalese; narrower than commitment envelope).
* **Bridges:** utterance **institutes** commitment; commitment **binds** service clause; no synonymy claimed.
* **Why it matters:** Status tracking becomes intelligible without pretending that a “service” acts; the NQD‑front yields neutral, cross‑tradition readable labels. (F.12; F.17 blocks D/R.)

### Example 3 — *Characteristic* names without lifecycle bias

* **Context harvest:**
  *Quality canon:* “maturity level”; *Performance canon:* “throughput”.
 **Kind:** `U.Characteristic` (measurement names).
* **Purpose / use‑domain:** CHR‑compatible measurements for planning and performance; bridgeable across engineering and management.
* **NQD‑front (seed candidates):**  
  *readiness (ordinal):* *MaturityLevel*, *ReadinessLevel*, *PhaseReadiness*, *TRL*, *ReadinessScore*  
  *throughput (ratio):* *Throughput*, *Rate*, *ProcessingRate*, *OpsPerSecond*, *FlowRate*
* **Chosen from frontier (Unified Tech / Plain):**  
  `U.ReadinessLevel` / “readiness level” (ordinal); `U.Throughput` / “throughput” (ratio).  
  *Discarded highlights:* **TRL** (tied to a specific scale/tradition); **Rate/OpsPerSecond** (over‑specific units baked in).
* **Narrative:** Dynamics are shown as **movement in state‑space**, not via lifecycle‑laden names such as “pre‑production process”.
* **Why it matters:** Prevents lifecycle/time from leaking into labels; the NQD‑front ensures neutrality and recognizability. (A‑series CHR rationale; F.17 §4–§6.)

### 19 · FAQ (authoring hygiene)

**Q1. How many Contexts must a naming proposal cite?**
**A.** The **sheet** for a thread should cite **≥ 3** distinct Contexts overall; an individual row may cite fewer if the concept appears in fewer Contexts. The point is breadth at the **UTS** level, not token‑stuffing rows. (F.17 §6 constraint.)

**Q2. Can a Source Context’s term ever become the Tech label?**
**A.** Only if its form is **already neutral** and does **not** smuggle in that Context’s private commitments. When in doubt, pick a fresh neutral Tech label and keep the Source term in **SenseCells**. (F.5.)

**Q3. Where do we put discipline‑vantage views like “Operations” vs “Research”?**
**A.** Use the **discipline columns** in a teaching layout if helpful, but remember: **discipline columns are not Context columns** and carry no editions. (F.17 §5.)

**Q4. How do we keep names stable while the story evolves?**
**A.** Keep **row ids** stable; evolve placement via the **Block Plan** and record moves in **Notes**. Use F.13 for renames/splits/merges. (F.17 §16; F.13.)

**Q5. What if two teams insist on different Tech labels for the same concept?**
**A.** Publish **one** Tech label; treat the other as a **deprecated alias** (Annex). Bridge their local senses on the row. (F.13; Part H.)

---

### 20 · 90‑second teaching script (for engineer‑managers)

> “**Local‑first** means we start in **context of meaning**—we harvest terms **inside** each Context and only then unify. A unified name is a **teachable promise**: one **Tech** label for precision, one **Plain** label for outreach. Its **row** in the **UTS** shows where the idea lives in real disciplines (the **SenseCells**) and how those Contexts connect (explicit **Bridges** with a brief loss note). We never equate terms by spelling; we argue sameness with a **bridge**. We also never bake stages or actors into names—those belong to **dynamics** and **roles**, not labels. When the story changes, we evolve names with **lexical continuity** rather than re‑inventing words. The result is a vocabulary managers and engineers can **hold on one page** and use the same way across projects.”

### 21 · Acceptance Harness (SCR/RSCR) for F.18

**Purpose.** Provide auditable, notation‑independent checks that a proposed unified name (and its publication on a UTS line) satisfies the **local‑first** unification discipline. The harness extends the general unification checks in **F.15** with **naming‑specific** obligations.

#### 21.1 Static Conformance Rules (SCR‑UNIFY)

| ID                                                                                                                                                                                                       | Requirement (normative “SHALL/SHALL NOT”)                   | Why this exists (conceptual)                                 | Where this is reflected |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------ | ----------------------- |
| **SCR‑U‑01 (Row‑first).** A unified Tech/Plain name **SHALL** be published **only** on a **Concept‑Set row** whose cells are SenseCells drawn from declared Contexts. No free‑floating names.               | Names are *lenses* onto a defended **row**, not vice‑versa. | **F.7** row‑as‑unit; **F.17** UTS row discipline.            | §F.7; §F.17             |
| **SCR‑U‑02 (Bridge‑only equivalence).** Cross‑context sameness **SHALL** be claimed **only** via an explicit **Bridge** with a relation kind and **CL** + loss/fit note.                                    | Prevents “string‑match identity”.                           | **F.9** Bridges; **F.0.1** principles.                       | §F.9                    |
| **SCR‑U‑03 (Neutral Tech).** The **Unified Tech** label **SHALL** be **neutral**—not lifted wholesale from any single Context **unless** the row’s Concept‑Set shows exact identity.                        | Avoids importing a local worldview as global.               | **F.5** naming neutrality; **F.17** 9.8 naming neutrality.   | §F.5; §F.17             |
| **SCR‑U‑04 (Twin registers).** Each row **SHALL** carry **Tech** and **Plain** names with the Part E register discipline; Plain is teacher‑friendly, Tech is morphology‑stable.                          | Satisfies didactic primacy without jargon creep.            | **E.10** registers; **F.5** naming rules.                    | §E.10; §F.5             |
| **SCR‑U‑05 (No window‑in‑name).** Variations by **time/phase/scale** **SHALL** be handled by **applicability windows** on **Statuses** (or examples), **NOT** by baking modifiers into the unified name. | Prevents type/status explosion by adjectives.               | **F.10/F.12** windows; **F.14** explosion guard.             | §F.10; §F.12; §F.14     |
| **SCR‑U‑06 (Heterogeneity).** A UTS block **SHALL** demonstrate **≥ 3** independent domain families across its rows, or an explicit Bias‑Annotation shall scope the claim.                               | Enforces trans‑disciplinary reach or honest scope.          | **F.17** invariants 3; **E.8** Bias‑Annotation.              | §F.17; §E.8             |
| **SCR‑U‑07 (Member≠Component sanity).** Names **SHALL NOT** imply holarchic composition when the row unifies **collections**; keep **MemberOf** distinct from **ComponentOf**.                           | Stops structural category errors.                           | Part F principles / anti‑patterns.                           | §9.8; §13               |
| **SCR‑U‑08 (One‑breath rationale).** Each row **SHALL** include a **single‑sentence** Unification Rationale that states **why** the cells denote the same thing despite wording differences.             | Keeps the argument visible and auditable.                   | **F.17** invariant 7.                                        | §F.17                   |
| **SCR‑U‑09 (Alias budget).** Per register, legacy aliases on a unified name **SHALL** be **≤ 1**; additional legacy labels go to Annex/Glossary.                                                         | Controls lexical drift while preserving continuity.         | **F.13** alias budget rule.                                  | §F.13                   |
| **SCR‑U‑10 (No Cross‑context rename).** A rename **SHALL** occur **within** the same Context or same row; Cross‑context “renames” are **prohibited**—use Bridges.                                                 | Keeps locality intact; forbids silent conflation.           | **F.13** continuity; **F.9** Bridges.                        | §F.13; §F.9             |
| **SCR‑U‑11 (Semantic read‑through).** A unified Tech/Plain name **SHALL** pass a **semantic read‑through**: the Name Card lists **5–10 diverse NQD archetypal situations** and the **NQD‑front notes** record rejected candidate and their **mismatch patterns**. | Prevents labels that mislead across the intended situations; ties lexical choice to demonstrated use. | §F.18 §4.2; §F.18 §5. | §F.18 |

#### 21.2 Regression Rules (RSCR‑UNIFY)

| ID                                                                                                                                                                       | Regression duty across editions                                        | Effect |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- | ------ |
| **RSCR‑U‑E01 (Edition drift).** When a source Context updates, re‑validate the row: stable sense ⇒ **rename/alias**; changed sense ⇒ **split/merge** rows; never overwrite. | Preserves truthfulness without erasing history. **F.13** RSCR.         |        |
| **RSCR‑U‑E02 (CL honesty).** Bridges **SHALL NOT** increase their CL (claiming stronger sameness) without new witnesses; **SHOULD** reduce CL when editions diverge.     | Guards against optimism bias in equivalence. **F.17** migration cues.  |        |
| **RSCR‑U‑E03 (Alias creep).** Periodically prune aliases to the **≤ 1** budget per register.                                                                             | Maintains narratively crisp UTS. **F.13** RSCR‑Alias.                  |        |
| **RSCR‑U‑E04 (Name neutrality check).** If the Unified Tech label is traceable to one context’s idiom, re‑justify neutrality or retitle the row.                            | Keeps the name “ours,” not “theirs.” **F.17** 9.7–9.8.                 |        |
| **RSCR‑U‑E05 (Window misuse).** Reject newly proposed types that are really **windows** on an existing Status/Role.                                                      | Prevents explosion by adjectives. **F.14** S14/E11 patterns.           |        |

### 21 · Migration & Deprecation Notes (informative, naming‑specific)

1. **Start from rows, not strings.** When consolidating legacy labels, **build or revisit the Concept‑Set row** first; only then pick the **Unified Tech/Plain** names. This keeps **meaning** primary. **(F.7, F.17)** 
2. **Prefer alias over merge.** If the *sense* is stable but the label misleads, **rename and retain one alias**; if the sense changed, **mint a new row** (no retrofits). **(F.13)**
3. **Resist modifier types.** New adjectives (e.g., *Peak*, *Remote*, *Night*) usually belong to **windows** or **examples**, not to the unified name. **(F.10/F.12/F.14)** 
4. **Keep neutrality visible.** If stakeholders push a brand‑coloured label, document why the chosen **Unified Tech** is **neutral** and include the brand as an **alias** in Glossary/Annex. **(F.5, F.17)** 
5. **Don’t globalise a Context.** Never move a Context label into the unified name as if it were universal. Use **Bridges** to relate Contexts, with an explicit **loss note**. **(F.0.1, F.9)** 

### 22 · FAQ (authoring hygiene for engineer‑managers)

**Q1. Can we reuse a dominant industry term as the Unified Tech name?**
**A.** Only if the row’s Concept‑Set shows **exact identity** across Contexts; otherwise pick a **neutral** Unified Tech and list the industry label as an **alias** in the Glossary. **(F.5, F.17)** 

**Q2. Two terms look identical across Contexts—may we skip Bridges?**
**A.** No. **Sameness is argued, not spelled.** Publish a **Bridge** with relation kind and **CL** plus a short **loss/fit** note. **(F.9, F.0.1)** 

**Q3. When do we mint a new U.Type vs. add a new row vs. add an alias?**
**A.** Use **F.8 Mint‑or‑Reuse**: if the *intension* changes, **new U.Type**; if the *same thing* spans new Context, **new row**; if only the label misleads, **alias/rename**.

**Q4. Our team keeps proposing “qualified roles” (e.g., *Night‑Operator*). What do we do?**
**A.** Keep the **Role** unified and express qualifiers as **windows** on **Statuses** or as **example context**. This follows **F.14** and **F.12**.

**Q5. Can we compress two near‑equivalent rows into one to “simplify the sheet”?**
**A.** Only if the **one‑breath rationale** remains true after review and the Bridges support equivalence with the same or stronger CL; otherwise keep **two rows** with explicit differences. **(F.17, F.9)** 

### 23 · Didactic distillation (90‑second script)

> **“Name on a row, never on a whim.”** In FPF we **speak on rows, not on vibes**: a **Name Card** ties each Tech/Plain pair to a concrete Context, Concept‑Set row, and SenseCells, with a small **NQD‑front** of rejected alternatives. This gives you **bridged precision** without losing **local comfort**. **Your UTS is the one page a careful mind can hold.**

### 24 · SoTA‑Echoing (post‑2015 practice alignment)

* **Neural WSD & sense evaluation (2015→).** P2’s sense‑seed read‑through is a human‑scale analogue of modern **word‑sense disambiguation** evaluation, where models are scored by the fraction of examples assigned the correct sense and by error profiles across sense inventories. Post‑2015 neural WSD benchmarks (e.g., multi‑domain evaluations reported in ACL venues) motivate the explicit `{too‑narrow, on‑target, too‑wide, wrong‑prototype}` labelling and the `θ_P` threshold for **SemanticFidelity**.
* **Quality‑Diversity & multi‑objective search (MAP‑Elites, NSGA‑II families, 2015→).** P1’s NQD‑front and **CC‑F18‑13** follow the same discipline as QD/NSGA‑style archives in optimisation: maintain a **set of non‑dominated candidates** over a vector of objectives rather than a single scalar score. The lexical Q‑tuple `{SemanticFidelity, CognitiveErgonomics, OperationalAffordance, AliasRisk}` is deliberately small so that human authors can inspect a Pareto frontier in the same way QD methods expose illumination archives.
* **Design‑space exploration & idea ranking (mechanical/industrial design, 2018→).** The PSOA‑style Name‑Card tables echo contemporary **design‑space ranking** practice, where candidate concepts are compared on diversity and quality rather than on a single “score”. Explicitly surfacing *why* one candidate dominates another improves auditability and supports teaching, mirroring recent work on ranking ideas for both diversity and quality in engineering design.
* **Semantic transparency & morphology in interfaces and code (HCI and PL practice, 2015→).** The strengthened **OperationalAffordance** guidance aligns with empirical results on **semantic transparency** of labels and identifier names: morphology that cues “actor vs activity vs artifact” improves comprehension and reduces error rates in both UIs and source code. F.18 turns these findings into a simple naming discipline (agentive forms for Roles, verbal forms for Methods, result nouns for Work/Artifacts) that can be enforced on Name Cards.

### 25 · Relations

**Builds on:**
**F.0.1** Contextual Lexicon Principles (local meaning; bridge‑only Cross‑context claims). **F.1–F.3** Contexts → term harvesting → local sense clustering. **F.5** Naming discipline. **F.7** Concept‑Set construction. **F.8** Mint‑or‑Reuse decision lattice. **F.13** Lexical continuity (renames/aliases/splits/merges). **F.14** Anti‑explosion controls (bundles, SoD, windows). **F.15** SCR/RSCR harness. **F.17** UTS as the publication surface.  

**Constrains:** 
All patterns that propose or consume unified names and rows in Part F; any Part A/C pattern that cites U.Types on UTS rows inherits these naming duties (through the UTS linkage), while keeping **structural/epistemic/temporal** aspects distinct per Part E authoring rules.

**Coordinates with.**
**A.17/A.18** for measurement lexicon when rows concern measurable notions (Characteristic/Scale/Level/Coordinate vocabulary), ensuring neutral naming aligns with canonical terms and eases external alignment via Bridges.  
