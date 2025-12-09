## E.10.D2 — Intension–Description–Specification Discipline (I/D/S) \[D]

*Definitional pattern — normative, notation‑agnostic*

> **One‑sentence summary.** For every intensional FPF object (e.g., `U.Role`, `U.Method`, `U.System`, `U.Work`, `U.Service`), clearly distinguish the **thing itself** (*Intension*), its **context‑bound Description** (KU), and its **formal Specification** (KU). Use **–Spec** only when strict, testable invariants and an acceptance harness exist; otherwise use **–Description**. This keeps semantics clean, didactic, and testable across all architheories.

**Status.** Definitional [D], architheory‑agnostic.
**Builds on:** A.7 **Strict Distinction (Clarity Lattice)**; E.10.D1 **D.CTX (Context ≡ U.BoundedContext)**; C.2.1 **U.EpistemeSlotGraph (DescriptionContext, IDS‑13)**; C.2.3 **Unified Formality Characteristic (F)**.
**Coordinates with.** F.4 **Role Description**; F.5 **Naming Discipline**; F.10 **Evaluation**; F.15 **SCR/RSCR Harness**.
**Non‑goals.** No editors, workflows, registries, or storage formats. No tooling commitments.

### 1 · Problem frame

**Intent.** Prevent perennial confusions such as “the role contains the checklist” or “the method is the document.” Establish a universal discipline so that:

* **Intensions** (e.g., `U.Role`, `U.Method`) remain I/D/S layer‑pure and context‑agnostic entities in the kernel.
* **Descriptions** (KUs) capture human‑readable, **Context‑local** semantics (labels, glosses, characterisations, state graphs, checklists).
* **Specifications** (KUs) exist **only** when there are verifiable invariants, an acceptance harness, **and a declared Formality F adequate for checkability (C.2.3; default F ≥ F4)**, making claims testable.

**Applicability.** Whenever an FPF text introduces or uses an intensional `U.Type` (e.g., `U.Role`, `U.Method`, `U.Service`, `U.System`, `U.Work`, `U.RCS`, `U.RSG`, `U.RoleEnactment`) in any part (A–H).

### 2 · Problem 

1. **Plane/layer mixing.** Intensions are routinely conflated with their documents and with runtime facts.
2. **Name drift.** “Spec” gets used for any write‑up; “status” drifts between states of a role and epistemic/deontic statuses over knowledge units.
3. **Didactic friction.** Inconsistent naming raises cognitive load and impedes reuse across architheories.
4. **Unverifiable claims.** Without a clear gate to **–Spec**, normative wording appears without testability.

### 3 · Forces

| Force                        | Tension to resolve                                                                |
| ---------------------------- | --------------------------------------------------------------------------------- |
| **Simplicity vs rigour**     | Easy‑to‑learn naming vs the need for machine‑checkable invariants.                |
| **Universality vs locality** | Kernel intensions must be universal; language and criteria are **Context‑local**. |
| **Stability vs evolution**   | Names should be stable; artefacts must mature via **ΔF** along the **F** ladder cleanly. |

### 4 · Solution — the I/D/S layer + a formal Spec‑gate

#### 4.1 The triad (applies to **any** intensional `U.T`)

**Terminology discipline (normative).** Say **I/D/S layers** when you mean the **stratified order with a Spec‑gate**; say **I/D/S triad** only to note **three‑ness without order or dependency**. **Do not call I/D/S a “plane”.** Reserve **plane** for uses explicitly defined elsewhere (e.g., **`CHR:ReferencePlane`** and status families).
**Layer semantics (clarity).** **I‑layer** = **kernel/intensional type** (non‑epistemic; **not** a episteme) . **D‑layer** and **S‑layer** = **epistemic Knowledge Units** (KUs). The **Spec‑gate** upgrades a Description to a Specification only under declared checkability and harness conditions (unchanged).

For every intensional type `U.T`:

* **Intension — `U.T`.**
  The thing itself (e.g., `U.Role`, `U.Method`, `U.Service`, `U.System`, `U.Work`, `U.RCS`, `U.RSG`).
  *It does **not** contain documents, checklists, or carriers; it is not a runtime event or a file.*

* **Description episteme — `U.TDescription(@Context)`**
  A **Context‑local** knowledge unit that **characterises** `U.T` with labels (Tech/Plain), glosses, and, when applicable, **Role Characterisation Space (`U.RCS`)**, **Role State Graph (`U.RSG`)**, and **state conformance checklists**.
  *Readable, precise, didactic; may reference evaluation criteria but does not assert testable “shall”s by itself.*

* **Specification episteme — `U.TSpec(@Context)`**
  A **Context‑local** knowledge unit that states **testable invariants** for `U.T` and is **bound to an acceptance harness**.
  *Normative, verifiable, suitable for SCR/RSCR (F.15).*

> **Key phrasing discipline.** Intensions are **characterised by** (not “contain”) RCS/RSG/checklists, which **live in** the Description/Spec.
> **Terminology guard.** To avoid collisions with **ReferencePlane** and other semantic planes, the I/D/S triad is referred to as **I/D/S Layers** (Intension Layer · Description Layer · Specification Layer). The word **plane** is reserved for **semantic planes** (Role/Status/Measurement/Type‑structure/Method/Work, etc.) and for the **ReferencePlane** field used in describedEntity/assurance.

#### 4.2 The Spec‑gate (when “–Spec” is allowed)

Use the **–Spec** suffix **only if all** of the following hold:

1. **Formality F (C.2.3):** the artefact declares **F ≥ F4** (or a context-defined higher threshold) so predicates are checkable.
2. **Verifiability:** invariants are stated as checkable predicates or thresholds.
3. **Harness bound:** there is a linked **acceptance harness** (SCR/RSCR matrices per F.15).
4. **Context anchoring:** all wording is explicitly local to a named `U.BoundedContext` (E.10.D1).

If any condition is missing, the artefact **must be** a `…Description`.

#### 4.3 Where RCS/RSG and evaluations sit

* **`U.RCS` (Role Characterisation Space)** and **`U.RSG` (Role State Graph)** are **intensional** types that structure the space of role characteristics and permissible state transitions.
* Their **human presentation** (characteristics, dimensions, node labels, admissible transitions) lives in the **RoleDescription**, and becomes part of **RoleSpec** only when the transitions and state predicates are made **testable** and harness‑bound.
* **`U.Evaluation`** operates on **evidence** against the conformance checklist (from the Description/Spec) to produce a **state attestation** (“X is in state S @Context within window W”).
* **Epistemic/deontic statuses** (e.g., *Evidence*, *Requirement*, *Standard*) are **roles over Epistemes** (not states of the role). They are governed elsewhere (F‑R family) and must not be conflated with `U.RSG` state names.

#### 4.4 Plain‑language memory hook

> *Thing vs words vs rules.*
> **The thing** (`U.Role`, `U.Method`) is clean and abstract.
> **The words** (labels, glosses, RCS/RSG pictures, checklists) live in the **Description**.
> **The rules** (testable “shall”s with harness) live in the **Specification**.
> If you can’t test it, don’t call it **Spec**.

### 5 · Minimal vocabulary & naming discipline (this pattern only)

**Core trio (per intensional `U.T`).**

* **`U.T` — the Intension.**
  Kernel object (e.g., `U.Role`, `U.Method`, `U.Service`, `U.System`, `U.Work`, `U.RCS`, `U.RSG`).
  *Never* a document, *never* an event, *never* a file.

* **`U.TDescription(@Context)` — the Description Episteme.**
  Context‑local characterisation of `U.T`: Tech/Plain labels, gloss, notes; for roles, may **characterise** with an `U.RCS` (characteristics/traits), an `U.RSG` (states/transitions), and **state conformance checklists** (per state). *Readable; precise; not yet a set of testable “shall”s.*

* **`U.TSpec(@Context)` — the Specification Episteme.**
  Context‑local, **testable** invariant set for `U.T`, explicitly **bound to an acceptance harness** (SCR/RSCR matrices per F.15). Use **–Spec** only through the Spec‑gate (Sec. 4.2).

**Suffix rules.**

* Use **`…Description`** by default (M‑mode or F‑mode without harness).
* Use **`…Spec`** *only* when **all** Spec‑gate conditions (Sec. 4.2) hold.
* No alternative suffixes (“Profile”, “Definition”, “Guide”) inside the Core; such epistemes live in pedagogy/tooling layers, not in the I/D/S discipline.

**Naming morphology (recap of F.5 as it applies here).**

* Two registers: **Tech** and **Plain** labels on every Description/Spec.
* Roles use **count nouns** (e.g., *Operator*); states use **state nouns** (e.g., *Approved*).
* Statuses over knowledge (e.g., Evidence/Requirement) are **not** role states; they name **roles over Epistemes** (F‑R family), not nodes in `U.RSG`.

**Context anchoring.**
Every Description/Spec is **local to** a `U.BoundedContext` (E.10.D1). Phrases in the episteme must read correctly once prefixed by the Context name (e.g., “(ITIL4) Acceptance criteria …”).

**Carriers.**
`U.Carrier` holds **encodings** of a Description/Spec; the Episteme’s identity is **not** the file. *Never* say “the role contains the checklist in the PDF”; say “the **RoleDescription** characterises the role with checklists; this **carrier** encodes them.”

**Time stance.**
Descriptions/Specs must declare DesignRunTag when inherent (e.g., RoleDescription is design‑time; state attestation via `U.Evaluation` is run‑time).

### 6 · Invariants (normative)

**IDS‑1 (Plane purity).**
An intensional `U.T` **MUST NOT** be conflated with its Description/Spec or with any `U.Carrier` or `U.Work`.

**IDS‑2 (Context locality).**
Every `…Description/…Spec` **MUST** name a `U.BoundedContext`. Wording inside is read **as‑local**; no global meaning is implied.

**IDS-3 (Spec-gate).**
A episteme **MUST NOT** use the **–Spec** suffix unless: *(a)* the artefact declares **`U.Formality = Fk` with k ≥ 4** per **C.2.3**, *(b)* invariants are testable predicates, *(c)* an acceptance harness is linked (F.15), *(d)* Context is explicit.

**IDS‑4 (Characterisation verbs).**
Texts **MUST** say: *“`U.Role` is **characterised by** `U.RCS`/`U.RSG` in the RoleDescription”*.
They **MUST NOT** say: *“the role **contains** the RCS/RSG”*.

**IDS‑5 (RCS/RSG scope).**
`U.RCS`/`U.RSG` are **intensional structures**. Their **presentations** (characteristics, state names, admissible transitions, checklists) live in the **RoleDescription**, and in **RoleSpec** only when transitions and state predicates are fully testable.

**IDS‑6 (Evaluation semantics).**
`U.Evaluation` **MUST** operate over evidence against conformance checklists from the Description/Spec and **MUST** produce a **state attestation** (who/what is in state *S* @Context within window *W*). Evaluation **does not** mutate the intensional object.

**IDS‑7 (Status separation).**
Epistemic/deontic statuses (Evidence/Requirement/Standard) are roles over **knowledge units**; they **MUST NOT** be used as state names in `U.RSG`.

**IDS‑8 (Register discipline).**
Every Description/Spec **SHOULD** include both **Tech** and **Plain** labels. Symbolic aliases are optional and informative.

**IDS‑9 (No stealth bridges).**
Descriptions/Specs **MUST NOT** import meanings from other Contexts by shared labels. Cross‑context relations exist only as **F.9 Bridges**.

**IDS‑10 (Window honesty).**
When an evaluation is time‑bounded, the **window** **MUST** be stated in the attestation.

**IDS‑11 (Ladder clarity).**
A Description may mature into a Spec by satisfying IDS‑3; the opposite move requires a rationale (loss of testability) and must drop the **–Spec** suffix.

**IDS‑12 (Didactic bound).**
A RoleDescription **SHOULD** fit on one screen per state graph plus one screen of notes; sprawling documents belong to pedagogy, not to the core Description.

### 7 · Reasoning primitives (judgement schemas, notation‑free)

> Judgements are **mental moves**—they assert what follows when premises hold. They do **not** imply queries, storage, or workflows.

1. **Description link (with DescriptionContext)**

   ```
   U.T, C, Vp ⊢ isDescriptionOf(TDesc, U.T, C, Vp)
   ```

   *Reading:* `TDesc` is the Context‑local Description of `U.T` in Context `C` under Viewpoint `Vp`. Its `subjectRef` decodes to `DescriptionContext = ⟨DescribedEntityRef(U.T), C, Vp⟩` (IDS‑13, C.2.1 §6.1).

2. **Spec link (Spec‑gate, viewpoint‑local)**

   ```
   isDescriptionOf(TDesc, U.T, C, Vp) ∧ U.Formality(TSpec) ≥ F4
      ∧ testableInvariants(TSpec) ∧ harnessBound(TSpec)
      ∧ sameDescriptionContext(TSpec, TDesc)
      ⊢ isSpecOf(TSpec, U.T, C, Vp)
   ```

   *Reading:* Only when F‑mode, testability, harness, and a matching `DescriptionContext` are present may we judge `TSpec` a Specification of `U.T` in `C` under Viewpoint `Vp`.

3. **Role characterisation**

  ```
   isDescriptionOf(RoleDesc, U.Role, C, Vp)
   ∧ characterises(RoleDesc, U.RCS) ∧ characterises(RoleDesc, U.RSG)
   ⊢ characterisedBy(U.Role, {U.RCS, U.RSG}) @C
  ```

   *Reading:* The role is *characterised by* the RCS/RSG as presented in the Description (which is pinned to `(C, Vp)`), not that it “contains” them.

4. **State conformance predicate**

   ```
   checklistFor(RoleDesc, state S) = χ
   ∧ evidence E within window W
   ⊢ conformsToState(E, χ, W) ⇒ attestation(subject ∈ S @C, W)
   ```

   *Reading:* Evidence satisfies the checklist for state `S`, yielding a state attestation.

5. **Transition admissibility**

   ```
   U.RSG allows (S → S') @C
   ∧ attestation(subject ∈ S @C, W)
   ∧ conformsToState(E', checklistFor(S'), W')
   ⊢ admissibleTransition(subject : S → S' @C)
   ```

   *Reading:* A move from `S` to `S'` is admissible when RSG permits it and `S'` is satisfied.

6. **Status / state separation guard**

   ```
   statusOverKU(KU, σ) ∧ stateInRSG(ρ)
   ⊢ σ ≠ ρ  (distinct planes)
   ```

   *Reading:* A status over a knowledge unit is not a role‑state.

7. **No Cross‑context import**

   ```
   isDescriptionOf(TDescA, U.T, CA, VpA) ∧ isDescriptionOf(TDescB, U.T, CB, VpB) ∧ CA≠CB
   ⊢ ¬equateByLabel(TDescA, TDescB)  (bridges required in F.9)
   ```

   *Reading:* Identical wording across Contexts (and Viewpoints) does not grant equivalence; only Bridges may relate them.

### 8 · Anti‑patterns & remedies

| ID   | Anti‑pattern                | Symptom                                                              | Why it harms thinking                     | Remedy (concept move)                                                                          |
| ---- | --------------------------- | -------------------------------------------------------------------- | ----------------------------------------- | ---------------------------------------------------------------------------------------------- |
| A‑1  | **Spec‑by‑name**            | Every write‑up is titled “Spec”.                                     | Inflates normativity; untestable claims.  | Apply **Spec‑gate** (IDS‑3). If any condition fails, rename to `…Description`.                 |
| A‑2  | **Role contains RSG**       | “The role contains a state graph.”                                   | Plane mixing; mereological confusion.     | Use **characterised by** phrasing (IDS‑4); RSG presentation lives in RoleDescription/RoleSpec. |
| A‑3  | **Status ≡ state**          | *Approved* (status over episteme)  appears as a node in the role graph.     | Cross‑plane conflation; logic errors.     | Keep **statuses** (over Epistemes) separate from **role states** (IDS‑7).                            |
| A‑4  | **Stealth bridge**          | Copying state names across Contexts to imply sameness.                  | Hidden cross‑context import.              | Declare an **F.9 Bridge** or accept divergence (IDS‑9).                                        |
| A‑5  | **Checklist = process**     | Treating conformance checklist as an execution workflow.             | Category error (design vs run).           | Checklists are **criteria** used by `U.Evaluation`; executions live under `U.Work`.            |
| A‑6  | **Carrier identity**        | File path/version treated as “the spec itself.”                      | Identity drift; archival brittleness.     | Identity is the **KU**; `U.Carrier` is only an encoding (Sec. 5).                              |
| A‑7  | **Windowless verdict**      | Attestations omit time window.                                       | Unreproducible results; stale judgements. | Require **window** in attestation (IDS‑10).                                                    |
| A‑8  | **Over‑formal Description** | Description bloats into a standard; unreadable.                      | Violates didactics; blocks adoption.      | Enforce **one‑screen** discipline (IDS‑12); move exegesis to pedagogy.                         |
| A‑9  | **Spec without harness**    | “Shall” statements with no linked acceptance matrices.               | Unverifiable normativity.                 | Bind to **SCR/RSCR harness** (F.15) or downgrade to Description (IDS‑3).                       |
| A‑10 | **Global language leakage** | Description reads as universal definition rather than Context‑local. | Breaks locality; fuels conflicts.         | Prefix mentally with the Context; rewrite locally (IDS‑2).                                        |

### 9 · Worked examples (multi‑architheory, didactic)

> Each vignette shows **intension ↔ Description/Spec ↔ Evaluation** with **context‑local** wording. No workflows; only thinking moves.

#### 9.1 Enactment (Role Assignment & Enactment line) — *Change Authority* role (ITIL 4 Context)

**Contexts.** `ITIL4_2020` (services/deontics), `PROV_O_2013` (run‑time traces).
**Intension.** `U.Role :: ChangeAuthority` — a behavioural mask that may be worn by a system (person/team/tool) to **authorise** a change.

**RoleDescription\@ITIL4.**

* **Tech/Plain.** *ChangeAuthority* / “change approver”.
* **RCS (characteristics).** CredentialLevel ∈ {L1,L2}; Scope ∈ {Service, Platform}; SeparationOfDuty ∈ {Clean, Violates}.
* **RSG (states).** `Proposed → Designated → Authorized → Active → Suspended → Revoked`.
* **State checklists (sketch).**

  * *Authorized:* { valid nomination, SoD=Clean, credential ≥ required, mandate window set }.
  * *Active:* *Authorized* ∧ { current shift/roster entry ∧ no conflicting active duty }.

**Evaluations.**
`U.Evaluation@ITIL4` over evidence (roster entries, mandate doc, SoD list, PROV Activities of approvals) yields **attestations**:

* `subject=Team‑X ∈ Authorized@ITIL4 in ⟨2025‑08‑01, 2025‑12‑31⟩`.
* Later, `subject=Team‑X ∈ Active@ITIL4 at 2025‑09‑14T10:05Z`.

**Didactic hooks.**

* The **role** is *characterised by* RCS/RSG in the **RoleDescription**; it **does not contain** them.
* The **attestation** is a statement about state‑in‑window; it does **not** mutate the role.

#### 9.2 Method (Essence‑language Context) — *Backlog Refinement* method

**Contexts.** `OMG_Essence_Language_2023` (method language), `PROV_O_2013` (runtime).
**Intension.** `U.Method :: BacklogRefinement`.

**MethodDescription\@Essence.**

* **Tech/Plain.** *BacklogRefinement* / “tidy backlog”.
* **Inputs/Outputs (informative).** Work items (ideas) → clarified items (ready/not‑ready tags).
* **RCS (characteristics).** Cadence ∈ {weekly, continuous}; CollaborationMode ∈ {sync, async}.
* **RSG (states).** `Sketched → Defined → Adopted`.
* **State checklist (Adopted).** { team agreed practice note exists, cadence set, entry/exit criteria published }.

**Spec‑gate outcome.**
No acceptance harness yet → remains **MethodDescription**, **not** MethodSpec.

**Run‑time echo.**
`U.Work` instances (calendar sessions, chat threads) are traced in PROV; **Evaluation** can check whether an *Adopted* practice is being followed in window W without ever reifying the method as a workflow.

#### 9.3 Service (SLO/SLA) — *Calibration Service* (ITIL 4 + SOSA/SSN Contexts)

**Contexts.** `ITIL4_2020` (service), `SOSA_SSN_2017` (observation), `ISO_80000_1_2022` (units).
**Intension.** `U.Service :: CalibrationService`.

**ServiceDescription\@ITIL4.**

* **Tech/Plain.** *CalibrationService* / “we calibrate your sensor”.
* **Acceptance facet (informative).** *SLO: error ≤ 0.5% FS under ISO 80000 units*; **formal criteria live in** ServiceSpec only if harness exists.

**Evaluation\@ITIL4+SOSA.**
Observations (SOSA) from test runs compared with thresholds → **ServiceEvaluation** attests *Met/Not‑Met* in a stated window.
No Cross‑context import: ISO units cited **as context‑local** references.

#### 9.4 Epistemic (KD‑line) — *Evidence status vs role state*

**Contexts.** `PROV_O_2013` (provenance), `FPF_Evidence_Status` (status family).
**Intensions.** `U.KnowledgeUnit :: Report_42`; `U.EvidenceStatus :: SupportsClaim`.

**Separation.**

* `SupportsClaim@C` is a **status over a Episteme** (classifies the report).
* It is **not** a node of any role’s `U.RSG`.
* `U.Evaluation` produces `attestation(Report_42 has EvidenceStatus=SupportsClaim@C, W)`.

**Didactic point.**
State names in *role* graphs do not duplicate **statuses**; planes stay disjoint.

#### 9.5 Control (Sys‑CAL line) — *Control‑Operator* role (IEC 61131‑3 Context)

**Contexts.** `IEC_61131_3` (control languages), `ISA_95` (integration).
**Intension.** `U.Role :: ControlOperator`.

**RoleDescription\@IEC61131‑3.**

* **RCS.** StationLevel ∈ {Cell, Line}; TaskMode ∈ {Cyclic, Event}; AlarmPrivileges ∈ {Ack, Ack+Shelve}.
* **RSG.** `Onboarded → Authorized → ConsoleActive → Paused → Suspended`.
* **Checklists (ConsoleActive).** { Authorized ∧ current console login ∧ task watchlist loaded }.

**Attestation (run‑time).**
`subject=Operator‑A ∈ ConsoleActive@IEC at 2025‑09‑14T08:00Z` based on log evidence.
No “workflow” required in the Description.

### 10 · Relations (with other patterns)

**Builds on:**

* **E.10.D1 — Lexical Discipline for “Context” (D.CTX).** Provides the *Context* primitive and bans “anchor” talk.
* **A.7 — Strict Distinction (Clarity Lattice).** This pattern concretises SD for intension vs description/spec vs carrier vs work.
* **C.2.3 — Unified Formality Characteristic (F).** Supplies the **F** anchors and **ΔF** moves that gate `…Spec`.

**Constrains:**

* **F.1–F.3 (Contexts → seeds → local senses).** Descriptions **must** cite context‑local senses (SenseCells) rather than global words.
* **F.4–F.5 (role/service naming).** Tech/Plain labels on Descriptions obey F.5 morphology rules.
* **F.8 (Service Acceptance Binding).** Evaluations of services read acceptance **from Description/Spec**, compare against Observations.
* **F.9 (Alignment & Bridge).** No Description/Spec may imply Cross‑context equivalence; Bridges carry all Cross‑context semantics.
* **F.15 (SCR/RSCR Harness).** Any `…Spec` must link to its harness; RSCR re‑checks verdict stability across editions/windows.

**Is used by.**

* **Part C architheories.** Sys‑CAL, KD‑CAL, Kind-CAL, Method‑CAL cite `…Description/…Spec` epistemes explicitly and consume **state attestations** from `U.Evaluation`.
* **Part B trust calculus.** Uses the presence/absence of harnessed Specs and the windowed nature of attestations in confidence roll‑ups.

### 11 · Migration notes (conceptual refactor playbook)

> Goal: remove conflations and normalise names without changing underlying models.

1. **Rename by default.** Any `XSpec` lacking a bound acceptance harness becomes **`XDescription`**. Keep content intact; change suffix and preface with a “Description, not Spec” note.
2. **Promote selectively.** For epistemes that *are* testable and declare **F ≥ F4**, add harness links (F.15) and re-label as **`XSpec`** via the Spec-gate.
3. **Fix the verbs.** Rewrite “Role contains RSG/RCS” → “Role is **characterised by** RSG/RCS in RoleDescription”.
4. **Detach carriers.** Replace identity‑by‑file with **`U.Carrier` encodes …Description/Spec** wording.
5. **Add Contexts.** Where a Description drifts globally (“the backlog refinement is…”), prefix with the Context and adjust wording to be **local**.
6. **Split planes.** Move any Evidence/Requirement **statuses** out of role state lists; keep them as roles over **knowledge units**.
7. **Window‑ise verdicts.** Ensure every evaluation statement adds an explicit **window** (instant or interval).
8. **Document maturity.** **Declare each Description’s F** (C.2.3) and track **ΔF** promotions/demotions as part of change notes (no governance implied).

### 12 · Acceptance tests (SCR/RSCR — concept‑level)

#### 12.1 Static conformance checks (SCR)

* **SCR-D2-S01 (Suffix discipline).** Every episteme with suffix **–Spec** passes the **Spec-gate** (**F ≥ F4** ∧ testable invariants ∧ harness link ∧ Context named). Otherwise it bears **–Description**.
* **SCR‑D2‑S02 (Characterisation verbs).** Texts never say an intension “contains” RCS/RSG; they say it is **characterised by** them via the Description/Spec.
* **SCR‑D2‑S03 (Plane purity).** No episteme mixes role **states** and knowledge **statuses**; each appears only on its correct plane.
* **SCR‑D2‑S04 (context‑locality).** Every Description/Spec names its `U.BoundedContext`; wording reads correctly when prefixed by the Context.
* **SCR‑D2‑S05 (Two registers).** Tech **and** Plain labels present on all Descriptions/Specs.
* **SCR‑D2‑S06 (Carrier separation).** Identity statements refer to Epistemes; files are referenced only as `U.Carrier` encodings.
* **SCR‑D2‑S07 (Windowed evaluation).** All state attestations cite a window `W` (instant or interval).

#### 12.2 Regression checks (RSCR)

* **RSCR‑D2‑E01 (Spec demotion guard).** If a **–Spec** loses its harness or testability, it is demoted to **–Description**; diffs show no lingering “shall” claims.
* **RSCR‑D2‑E02 (Bridge drift).** If two Contexts begin to share identical labels, verify no Descriptions/Specs imply Cross‑context identity; add or revise **F.9 Bridges** instead.
* **RSCR‑D2‑E03 (Edition churn).** When a Context’s canon updates, previously valid attestations remain historical (windowed); new Specs/Descriptions cite the new edition.
* **RSCR‑D2‑E04 (Verb hygiene).** Automated grep over corpus finds “contains RSG/RCS” phrasing; none remain after refactor.
* **RSCR‑D2‑E05 (Status bleed).** Spot‑audit a random sample of role graphs to ensure no epistemic/deontic statuses appear as role states.

*Didactic takeaway.*
Think in three layers: **Intension** (what the thing *is*), **Description/Spec** (how we *state* its character and, when mature, *test* it), and **Evaluation** (what we can *attest* about it in a **window**). Keep Contexts local, planes separate, and “contains” out of your vocabulary.

### 13 · Author’s pocket guide (carry‑in‑mind rules)

> **Use these as thinking cues, not as paperwork.** Each cue is a one‑breath test you can apply while writing.

1. **Name the Context.** Write “*Role (ITIL4)*”, “*Method (Essence‑language)*”, “*Execution (PROV)*”. Never speak global words.
2. **Pick the *object-of-talk*.** Am I talking about an **intension** (Role/Method/Service), a **Description/Spec**, an **Evaluation**, or a **Carrier**? Stay on one object-of-talk per sentence.
3. **Prefer –Description.** Use **`…Description`** by default. Switch to **`…Spec`** only after the **Spec‑gate** (testable invariants + harness + F‑mode).
4. **Characterised by…** Say *“Role is **characterised by** RCS/RSG recorded in RoleDescription”*, never *“Role **contains** its states”*.
5. **Window every verdict.** An Evaluation must read “*X ∈ State\@context **in** W*”. No naked, timeless verdicts.
6. **Status ≠ state.** Role **states** live in `U.RSG`; Evidence/Requirement **statuses** classify **knowledge units**. Do not mix.
7. **Bridge later.** If two Contexts “feel the same”, write the itch down and leave it for **F.9 Bridge**.
8. **Two registers.** Every Description/Spec has **Tech** and **Plain** labels; prefer the shortest tech term that matches the invariants.
9. **Carrier humility.** Files and records are **Carriers** of Descriptions/Specs; they don’t *equal* the thing you reason about.
10. **Spec = test.** If you can’t point to a harness that would falsify it, it isn’t a **Spec** yet.

### 14 · Phrasebook & pitfall table (say this, not that)

| Mistaken phrasing (avoid)              | Didactically correct phrasing (use)                                                                                  | Why                                                                                        |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| “The Role **contains** its states.”    | “The **Role** is **characterised by** RCS/RSG **recorded in** the RoleDescription.”                                  | Roles are intensions; state graphs live in their **Descriptions/Specs** (knowledge plane). |
| “MethodSpec (draft).”                  | “**MethodDescription** (Essence‑language Context); not a Spec yet.”                                                     | **–Spec** is reserved for testable artifacts that passed the Spec‑gate.                    |
| “We proved the service meets the SLO.” | “**Evaluation** attests *Service ∈ Met\@ITIL4 in W* based on observations and the **Acceptance harness**.”           | Evaluations produce **windowed attestations**, not timeless facts.                         |
| “Evidence status is a role state.”     | “**Evidence status** classifies a **KnowledgeUnit**; **Role states** live in RSG. Different planes.”                 | Prevents status/state conflation.                                                          |
| “The PDF is the Method.”               | “The PDF is a **Carrier** that **encodes** a **MethodDescription**.”                                                 | Carrier ≠ content.                                                                         |
| “BPMN workflow = PROV activity.”        | “Add a **Bridge (F.9)** if needed; in F.1/F.2/F.3 we treat them as **context‑local** senses.”                           | No Cross‑context identity outside Bridges.                                                    |
| “WorkSpec / WorkPlan (synonyms).”      | “**U.WorkPlan** (preferred). **WorkDescription** is an allowed alias; **WorkSpec** is deprecated.”                   | Aligns with the –Description/–Spec discipline.                                             |
| “RoleSpec is our template.”            | “**RoleDescription** is our template; promote to **RoleSpec** once the harness exists.”                              | Keeps the Spec word meaningful.                                                            |
| “Spec says the same in all Contexts.”     | “Each **Spec/Description** is **context‑local**; Cross‑context reuse requires an **Alignment Bridge** with CL/loss notes.” | Locality guard.                                                                            |

### 15 · Naming & alias policy (normative, notation‑free)

#### 15.1 Suffix discipline (recap).**

* **Preferred default:** **`…Description`** for Role/Method/Service/Work.
* **Reserved:** **`…Spec`** only if the item passed the **Spec‑gate** (F‑mode, testable invariants, harness id, Context named).
* **Banned:** Using **–Spec** as a synonym for “detailed description”.

#### 15.2 Canonical/alias map (current edition).**

| Concept (intension) | Preferred episteme name      | Allowed alias (equal scope)   | Deprecated alias | Notes                                                                                 |
| ------------------- | ---------------------- | ----------------------------- | ---------------- | ------------------------------------------------------------------------------------- |
| Role                | **RoleDescription**    | RoleCard *(Pedagogy only)*    | —                | *RoleCard* is informal (teaching layer), not a normative episteme name.                     |
| Role (F‑mode)       | **RoleSpec**           | —                             | —                | Only after Spec‑gate.                                                                 |
| Method              | **MethodDescription**  | —                             | **MethodSpec**   | Global rename complete; legacy references should be updated.                          |
| Method (F‑mode)     | **MethodSpec**         | —                             | —                | Now reserved for harnessed, testable methods.                                         |
| Work (schedule)     | **U.WorkPlan**         | **WorkDescription**           | **WorkSpec**     | *WorkSpec* alias removed; *WorkDescription* remains as didactic alias for *WorkPlan*. |
| Service             | **ServiceDescription** | ServiceCard *(Pedagogy only)* | —                | As above: Card is informal only.                                                      |
| Service (F‑mode)    | **ServiceSpec**        | —                             | —                | Requires acceptance harness id (F.15).                                                |

#### 15.3 Verb & morphology rules.**

* **Verbs.** Use *characterised by*, *recorded in*, *encoded by*; avoid *contains*, *is stored in*, *is implemented by* when speaking at the conceptual level.
* **Morphology.**

  * Roles name **masks** as **count nouns** (*Operator, ChangeAuthority*).
  * States as **state nouns/participles** (*Authorized, Active*).
  * Status names are **classifiers over knowledge** (*SupportsClaim, NormativeStandard*).
  * Descriptions/Specs use neutral nouns (*RoleDescription, MethodSpec*).

#### 15.4 Deprecations (effective now).**

* **MethodSpec** (as a general name) → **MethodDescription** unless Spec‑gate is met.
* **WorkSpec** (alias for WorkPlan) → **WorkDescription** (allowed alias), or **U.WorkPlan** (preferred).
* Texts must avoid “contains RSG/RCS” phrasing (see RSCR‑D2‑E04).

### 16 · Quick templates (fill‑in‑mind, not forms)

> Copy these **lines** into your prose as thinking scaffolds. They are not schemas, fields, or checklists to fill; they are didactic prompts.

### 16.1 Role (default).

* *Intension.* `U.Role :: <TechName> in <ContextId>`.
* *RoleDescription\@context.* Tech/Plain: **`<TechName> / <PlainName>`**.

* **RCS characteristics.** `<characteristic₁ ∈ {...}>; <characteristic₂ ∈ {...}>`.
* **RSG nodes (→).** `<S₀ → S₁ → ... → Sₙ>`.
* **State checklist (one node).** `<StateX : {criterion₁, …}>`.
* *Evaluation attestation.* `subject=<Holder> ∈ <StateX>@<ContextId> in <Window> (evidence: <cue₁,…>)`. 

#### 16.2 Method (Essence‑language Context).

* *Intension.* `U.Method :: <TechName>`.
* *MethodDescription\@context.* Inputs/Outputs (informative), **RCS/RSG** (if you track adoption).
* *Spec upgrade (optional).* “Becomes **MethodSpec** when harness `<id>` exists.”

#### 16.3 Service (acceptance‑bearing).**

* *ServiceDescription\@context.* Tech/Plain; **Acceptance facet** (informative until harnessed).
* *Evaluation.* `Service ∈ Met/Not‑Met@context in <Window>` based on observations and acceptance criteria.

#### 16.4 Alignment reminder.

* “No Cross‑context identity is implied; if needed, add **F.9 Bridge**: `<ContextA:TermA> ↔ <ContextB:TermB>` with CL/loss notes.”

### 17 · Didactic distillation (90‑second script)

> **“Three layers; one context; no leakage.”**

1. **Pick the Context.** Every word lives **inside** a `U.BoundedContext`.
2. **Pick the I/D/S layer.** Speak about the **Intension (I)**, or about its **Description/Spec (D/S)**—but never mix layers. If your sentence also asserts describedEntity or evidence, **name the `ReferencePlane`** (`world|concept|episteme`).
3. **Describe, then test.** Start with **Role/Method/ServiceDescription**. Only when you can **falsify** it with a harness do you call it a **Spec**.
4. **State is attested.** Role **states** are attested by **Evaluations** as *“X ∈ State\@context **in** W”*. Evidence/Requirement **statuses** classify **knowledge**, not roles.
5. **Carriers carry.** PDFs and repos are **Carriers** of the Description/Spec; they aren’t the thing itself.
6. **Bridges are explicit.** Cross‑context sameness is never assumed; you declare a **Bridge** with CL/loss.
   Follow these six lines and SD (*Strict Distinction*) stops being an abstraction—you feel it in every sentence you write.
   