# **Part F — The Unification Suite (U‑Suite): Concept‑Sets, SenseCells & Contextual Role Assignment**


---

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



---

# F.5 — Naming Discipline for U.Types & Roles \[D] 

**Status.** Definitional pattern \[D], architheory‑agnostic.
**Depends on.** E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; **E.10.D2 Intension–Description–Specification (I/D/S)**; F.1 **Domain‑Family Landscape Survey**; F.2 **Term Harvesting & Normalisation**; F.3 **Intra‑Context Sense Clustering**; F.4 **Role Description Definition**; A.7 **Strict Distinction**; A.11 **Ontological Parsimony**; F.0.1 **context‑local Lexicon Principle (RLP)**.
**Coordinates with.** F.7 **Concept‑Set Table**; F.8 **Mint or Reuse?**; F.9 **Alignment & Bridge**; F.13 **Term Registry & Deprecation**.
**Aliases (informative).** *Context‑true naming*; *Two‑register labels*.

---


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


---

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


---

# F.8 — Mint or Reuse? (U.Type vs Concept-Set vs Role Description vs Alias) \[A] 

**“Name only what thinking **requires**, and reuse everything else.”**

**Status.** Architectural pattern \[A], architheory‑agnostic.
**Depends on.** E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; A.7 **Strict Distinction**; A.11 **Ontological Parsimony**; A.8 **Universal Core**.
**Coordinates with.** F.1 **Contexts (Contexts)**; F.2 **Harvest**; F.3 **SenseCells**; F.4 **Role Description**; F.5 **Naming Discipline**; F.7 **Concept‑Set Table**; F.9 **Alignment & Bridge**.
**Aliases (informative).** *Mint‑vs‑Reuse gate*; *Naming governor*.

---


---

# F.14 — Anti‑Explosion Control (Roles & Statuses) \[A] 

**“Name less, express more.”**

**Status.** Architectural pattern \[A], architheory‑agnostic.
**Depends on.** F.1 **context of meaning**; F.2 **Harvesting**; F.3 **Local Sense Clustering**; F.4 **Role Description**; F.5 **Naming Discipline**; F.7 **Concept‑Set Table**; F.8 **Mint‑or‑Reuse**.
**Coordinates with.** F.10 **Status Windows & Mapping**; F.11 **Method Quartet Harmonisation**; F.12 **Service Acceptance Binding**; F.13 **Lexical Continuity**.
**Aliases (informative).** *Role/Status economy*; *Explosion guard*.

---


---

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
