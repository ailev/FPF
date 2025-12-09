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


---

## 17 · Didactic distillation (90‑second teaching script)

> “Before you name anything, **fix the context of meaning**. A *Context* is a **U.BoundedContext** tied to a specific canon—*BPMN 2.0*, *PROV‑O*, *ITIL 4*, *SOSA/SSN*, *IEC 61131‑3*, *OWL 2*. Words are **local to Contexts**: *process (BPMN)* is a workflow graph, *activity (PROV)* is a run‑time occurrence, *service (ITIL)* is a promise vocabulary. Cut the landscape so each unification line sees **at least three domain families**, with **one‑screen Cards** per Context (scope gist, time stance, trip‑wires). **Do not bridge** Contexts here—just write down the itch to bridge and defer it. Keep the cut **small enough to remember**. With Contexts fixed, harvesting (F.2), local clustering (F.3), role/status templates (F.4), and explicit Cross‑context bridges (F.9) become straightforward—and you avoid naming ghosts that come from words floating without walls.”


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


---

## 16 · Didactic distillation (60‑second script)

> “In F.2 you **harvest inside Contexts**. For each Context, pick the canon’s own phrasing, choose a **Local Normal Form** in that idiom, add **Tech** and **Plain** labels, and write a one‑sentence **Gloss** that matches how that Context talks. Stop there. No bridging, no behaviour, no equations. If the same string appears in another Context, treat it as a **different unit**. These units feed F.3, where you’ll sort senses **within** a Context, and F.9, where you’ll relate Contexts explicitly. This keeps meaning local, names faithful, and later reasoning clean.”


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


---

## 16 · Didactic distillation (60‑second teaching script)

> “A **Concept-Set row** shows **one idea across Contexts**—but only where explicit **Bridges** license it. Columns are Contexts; cells are **their own labels**. The row prints a **scope** (‘Naming-only’, ‘assignment/enactment-eligibility’, ‘Type-structure’, ‘KD-metric’) and the **weakest CL** that justifies reading across. A **one‑line rationale** says why sameness is safe **here**; a **counter‑example** warns where it breaks. Keep rows small (2–4 Contexts), typed (don’t mix senseFamilies), and temporally honest (design vs run stance). If Bridges don’t suffice, publish a **contrast row** instead. The table doesn’t invent meaning; it **summarises licensed sameness** so readers can cross disciplines without smuggling assumptions.”


---

# F.8 — Mint or Reuse? (U.Type vs Concept-Set vs Role Description vs Alias) \[A] 

**“Name only what thinking **requires**, and reuse everything else.”**

**Status.** Architectural pattern \[A], architheory‑agnostic.
**Depends on.** E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; A.7 **Strict Distinction**; A.11 **Ontological Parsimony**; A.8 **Universal Core**.
**Coordinates with.** F.1 **Contexts (Contexts)**; F.2 **Harvest**; F.3 **SenseCells**; F.4 **Role Description**; F.5 **Naming Discipline**; F.7 **Concept‑Set Table**; F.9 **Alignment & Bridge**.
**Aliases (informative).** *Mint‑vs‑Reuse gate*; *Naming governor*.

---


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


---

## 16 · Didactic distillation (90‑second teaching script)

> “When you feel like coining a new name, pause. **Which senseFamily** are you in—Role, Status, Measurement, Type‑structure, Method, or Execution? If a **single Context’s SenseCell** already says it, **reuse** that label. If you need an assignable Standard, **mint a Role Description** anchored to that SenseCell. If you must read **across Contexts**, reuse a **Concept‑Set row**—but only **at a stated scope** and only if its **CL meets the threshold** (τ). If it’s just a nicer wording, add an **Alias** (style only). Only in the rare case of a cross‑family, **irreducible** notion do you **mint a new U.Type**. Never let Naming‑only rows justify  **Assignment-eligibility** or structural inference, and never let identical strings force equivalence. This is not process—it’s **discipline of thought**: reuse what exists, declare scope when you bridge, and mint new primitives only when the kernel truly needs them.”



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


---

## 17 · Didactic distillation (90‑second script)

> “A **Bridge** translates between **local senses** from different **Contexts**. It always declares **what relation** (≈, ⊑, ⋂, ⊥, or an **interpretation** like design↔run), **how strong** (CL 0–3), **which way** (for ⊑/⊒), and **what is lost**. **Substitution** is allowed only on the **same senseFamily** and only with **CL≥2**; **Type‑structure** needs **CL=3**. **Interpretation Bridges** explain, never substitute. Rows in the Concept‑Set table obey the **weakest‑link**: their scope cannot exceed the lowest CL among their Bridges. When editions change or counter‑examples surface, **lower CL** or change **kind**; if two senses truly converge and invariants match, raise to **CL=3**—rarely, and with reasons. Translate across Contexts; never collapse them.”


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


---

## 16 · Didactic distillation (90‑second script)

> **Three families, two modalities.** *Evidence* tells us what the world **shows** (Observed→Measured→Corroborated→Replicated; Refuted cancels) — **epistemic**; *Standard* tells us what a canon **sanctions** (Candidate→Draft→Approved→Deprecated→Superseded) — **deontic**; *Requirement* tells us what an obligation is **doing** (Applicable/Inapplicable; Satisfied/Violated; Waived/Pending) — **deontic**.
> Every status is a **StatusCell inside one Context** with exactly one **StatusModality**, a **Target**, and a **Window**.
> When you must relate status meanings across Contexts, **draw a Bridge** that states the **kind** (≈, ⊑/⊒, ⋂, ⊥ or Interpretation), the **CL** (strength), and the **Loss** (what you ignore). Prefer **explanation**; allow **substitution** only when statusModalities match, kind permits, **CL≥θ**, and Windows align.
> Keep **design vs run** stance honest: approval is **design‑time**, evidence is **run‑time**, requirements **span both**. With this habit, “validated”, “approved” and “compliant” stop being a muddle of synonyms and become **precise, local meanings** you can compare **safely** and **audibly**.



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


---

## 16 · Didactic distillation (90‑second script)

> “When you talk about *how something is done*, decide which of the **four boxes** you mean.
> **Method** is the **idea** (the way). **MethodDescription** is the **recipe** (the description). **Work** is the **happening** (what actually occurred). **Actuation** is the **control push** (signals emitted during Work).
> Keep **design** and **run** as distinct **stances**. Plans and approvals live in the **design stance**; measurements and obligations live in the **run stance** within **Windows**.
> Words like *process*, *task*, *activity*, *command* are **context‑local**—say *process (BPMN)*, *activity (PROV)*, *task (IEC)*. If you must relate them, draw a **Bridge** and declare its **kind**, **CL**, and **Loss**.
> For compliance, don’t point at the plan—point at **Work**, show **Observations**, and judge clauses in **F.10**.
> Hold this quartet in your head and you’ll stop mixing plans with facts, signals with outcomes, and names across Contexts. + Everything else—naming (F.5), `U.RoleDescription` (F.4) and `U.RoleAssignment`/`U.RoleEnactment` (A.2.1/F.6), Bridges (F.7/F.9)—falls into place.


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


---

# F.13 — Lexical Continuity & Deprecation \[A] 

**“Change names without changing history.”**
**Status.** Architectural pattern \[A], architheory‑agnostic.
**Builds on:** F.1 **context of meaning**; F.2 **Term Harvesting**; F.3 **Intra‑Context Clustering (SenseCell)**; F.5 **Naming Discipline**; F.7 **Concept‑Set (row) construction**; F.8 **Mint‑or‑Reuse decision**; F.9 **Bridges**; F.10 **Status windows**.
**Coordinates with.** Part C CALs when canon editions change (Sys/KD/Type/Method/LCA).
**Non‑goals.** No registries, workflows, editors, or storage formats. No by‑name Cross‑context equivalence. No silent rewrites of old texts.

---


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


---

## 16 · Didactic distillation (60‑second script)

> **Names are lenses.** The *thing* that persists is the **sense** (a SenseCell in a Context, a Concept‑Set row, a Role Description). When you improve a lens, use **`renames`** or **`aliases`** **inside that same place**. When the *thing* changes, say so with **`splits/merges`**—and adjust rows/Bridges accordingly. **Never rename across Contexts.** Keep at most **one** legacy alias per register. Do **not** rewrite history; give readers **read‑paths** and brief epoch notes. With this discipline, you can clarify language without erasing meaning, and your models keep both **continuity** and **truth**.


---

# F.14 — Anti‑Explosion Control (Roles & Statuses) \[A] 

**“Name less, express more.”**

**Status.** Architectural pattern \[A], architheory‑agnostic.
**Depends on.** F.1 **context of meaning**; F.2 **Harvesting**; F.3 **Local Sense Clustering**; F.4 **Role Description**; F.5 **Naming Discipline**; F.7 **Concept‑Set Table**; F.8 **Mint‑or‑Reuse**.
**Coordinates with.** F.10 **Status Windows & Mapping**; F.11 **Method Quartet Harmonisation**; F.12 **Service Acceptance Binding**; F.13 **Lexical Continuity**.
**Aliases (informative).** *Role/Status economy*; *Explosion guard*.

---


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


---

## 15 · Didactic distillation (90‑second script)

> **Name less, express more.** Before minting a new Role or Status, try **four levers**:
> **(1) Reuse the row** — if the intent already exists, adopt it and add your local SenseCell.
> **(2) Bundle, don’t blur** — when two Roles travel together, **Bundle** them; keep **SoD** if they must stay apart.
> **(3) Declare SoD, don’t fuse** — conflicts of interest are solved with **SoD**, not with “trusted” super‑roles.
> **(4) Window, don’t multiply** — one **Status** can wear different **windows** (evaluation/active/grace); that’s not four Status types.
> Keep modifiers as **facets**, not names; keep every Role Description **context‑local** via its SenseCell. If your vocabulary no longer fits in a thoughtful mind, you have an **explosion**—return to the levers and reduce.


---

# F.15 — SCR/RSCR Harness for Unification \[A] 

**“Prove locality and parsimony first; only then prove composition.”**
**Status.** Architectural pattern \[A], architheory‑agnostic.
**Builds on:** E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; F.0.1 **Foundational Principles**; F.1–F.14.
**Coordinates with.** B.3 **Trust & Assurance Calculus** (for CL use on Bridges).

---


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


---

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


---

## 18 · Didactic distillation (90‑second teaching script)

> “Use the harness to **think like a safety net**. First, the **SCR** threads: everything is **local** to a Context; **Role Descriptions** point to **one** SenseCell; rows actually **cross** Contexts; Bridges are explicit with CL and a loss note; windows capture variation without spawning new types. Then, the **RSCR** knots: never overwrite an edition—**fork the Context** or mark recency; keep rows stable by **retiring and re-rowing**; Bridges get **re-validated** (CL goes down unless you bring proof); renames become **aliases** unless meaning changes; **windows** absorb time/scale shifts; **SoD** stays intact. If you can pass these thoughts on a small slice—and explain each pass in **one breath**—your unification is green. No tooling, no roles, no dashboards. Just clean Contexts, honest rows, cautious bridges, and names that help minds meet.”


---

# F.16 — Worked‑Example Template (Cross‑Domain) \[A] 

**“Show the thought, not the tooling.”**
**Status.** Architectural pattern \[A], architheory‑agnostic.
**Builds on:** E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; F.1–F.15.
**Coordinates with.** B.3 **Trust & Assurance Calculus** (CL on Bridges); Part C architheories (Sys‑CAL, KD‑CAL, Kind-CAL, Method‑CAL).

---


---

## 10 · Didactic distillation (60‑second script)

> “A good cross‑domain example fits on **one page**. First, name the **claim**. Then show the **Contexts** you’re using. List the **SenseCells** you will actually touch. Draw **one row** that makes them the same **for this claim**. Every Cross‑context nuance you can’t justify in that row becomes a **Bridge** with a **kind**, a **CL**, and a **loss** sentence. Point each **Role Description** to **one** cell. If time/scale matters, state the **window**; if duties matter, state **SoD**. Finish with two or three **harness pings** from F.15. That’s it—no tooling, no long procedures. The reader can now replay your thought and agree (or disagree) at the right place.”


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


---

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