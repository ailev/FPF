## 13 · Integration with A.15 — Role–Method–Work alignment

> **One line.** A `U.MethodDescription` **names** the roles it needs; a `U.Work` **cites** the concrete `U.RoleAssignment` that enacted the step; the **RSG state + window** gates that enactment.

### 13.1 Design‑time Standard (inside `U.MethodDescription`)

For every **MethodStep**:

* **`requiredRoles`** — a list of `U.Role` **from the same Context as the step**.
  *Example.* In `Hospital.OR_2025`, step “Make incision” has `requires: [IncisionOperatorRole]`.
* **Role algebra in‑Context** applies: if the Context defines `IncisionOperatorRole ≤ SurgeonRole`, then `requires: [SurgeonRole]` also admits holders of `IncisionOperatorRole`.
* **Separation of concerns.** Capability checks (does the holder *can*?) belong to `U.Capability` and resource limits; **authorization** belongs to `U.RoleAssignment` + RSG.

### 13.2 Run‑time check (inside `U.Work`)

A `U.Work` record must carry:

* **`performedBy` =** a concrete **`U.RoleAssignment`** (not just a person/system name).
* **Window gate.** The Work timestamp falls inside the assignment’s `@Window`.
* **State gate.** At that timestamp, an **enactable** state for the assignment is proven by a **`StateAssertion`** (the checklist verdict for a named RSG state).
* **Role algebra gate.** The assignment’s `role` is either one of `requiredRoles` or a **specialization (`≤`)** thereof; bundles (`⊗`) expand to conjunctions; incompatibilities (`⊥`) forbid overlaps on the same holder.

### 13.3 Evaluation & acceptance (link to services & deontics)

* **Observation.** The Work produces `U.Observation`(s).
* **Evaluation.** A `U.Evaluation` compares Observations with **AcceptanceClause**(s) referenced by a **Service** or a **RequirementRole**.
* **SoD hook.** If the step or evaluation demands independence (e.g., “not performed by its reviewer”), enforce via `⊥` between `PerformerRole` and `ReviewerRole` **in the same Context**.

### 13.4 Planning & scheduling (design‑time “who will enact”)

* **`U.WorkDescription`** (renamed from “WorkPlan”) binds forthcoming steps to **candidate RoleAssignments** and time windows.
* **Checks before the fact.** Validate windows (no gaps/overlaps where disallowed), enforce `⊥`, ensure expected RSG state will be **enactable** at scheduled time (or flag a pre‑flight checklist).

> **Didactic cue.** Think **“Step asks for badges; Run cites a badge; Badge must be valid & green.”**
> (Badge = RoleAssignment; valid = window; green = RSG state with a fresh StateAssertion.)

---


---

## 9 · Capability thresholds on steps (how A.15 uses this concept)

A step in a **Method** may define **required roles** (assignment) and **capability thresholds** (ability). A Work passes the gate if:

1. **assignment check:** the Work’s `performedBy` points to a valid **Role assignment** that covers the step window and satisfies the role relation (including specialization `≤` inside the context).
2. **Ability check:** the **holder** of that Role assignment has a **capability** whose **WorkScope covers the step’s JobSlice** (i.e., declared superset) and whose **WorkMeasures** meet the step’s threshold(s) **within `Γ_time(W)` and while the capability’s **QualificationWindow** includes *W***.

**Idioms managers can reuse (plain text):**

* *“S1 requires `IncisionOperatorRole` and Precision ≤ 0.2 mm (OR\_2025 norms) **in window W**.”*
* *“S2 requires `PlannerRole`, **WorkScope ⊇ JobSlice\[W]**, and Optimality ≥ 0.90 on `JS_Schedule_v4`.”*

**What to avoid:**

* Putting “Precision ≤ 0.2 mm” into the Role name. Keep thresholds attached to the **step**; keep **ability** on the **holder**.

---


---

# A.3 Transformer Constitution (Quartet)  \[A]


---

## 5 · Solution — The Transformer Quartet

A.3 defines four anchors, tied together by **Role Assignment (`U.RoleAssignment`)** and aligned with **Temporal Duality**.

### 5.1 The four anchors (terms & types)

1. **Acting side:** a **system bearing TransformerRole** — the only holon kind allowed to enact transformations (behavioural role). *Canonical phrase:* **“system bearing TransformerRole”**. *Local shorthand:* after explicit binding in the **same subsection**, you MAY write **“Transformer”** to denote that same system; re‑bind on context change and **do not** use shorthand where the domain already has a conflicting “transformer” term.

2. **MethodDescription (design‑time description):** protocol / algorithm / SOP / script — all are **idioms of MethodDescription**; they live in **Tᴰ** and are **epistemes** with carriers (SCR/RSCR).

3. **Method (design‑time capability):** order‑sensitive composition the system *can* enact at run‑time (Γ\_method); it is **not** an occurrence.

4. **Work (run‑time occurrence):** dated execution producing state change and consuming resources (Γ\_work); every Work **isExecutionOf** exactly one MethodDescription version and is **performedBy** exactly one performer (possibly a collective system).

> **Safe memory line:** *MethodDescription → (describes) Method → (executed as) Work.*
> Roles are **masks** (A.2/A.7); methods/work are **behaviour**.

### 5.2 Contextual Role Assignmnent (`U.RoleAssignment`) for transformations

Use the universal assignment to state **who plays which role where and when**:

```
U.RoleAssignment(
  holder  : U.System,          -- the acting system (bearer)
  role    : U.TransformerRole, -- behavioural role
  context : U.BoundedContext,  -- semantic boundary
  timespan?: Interval          -- optional validity window
)
```

* A role is **local to context** and **time‑indexed**.
* The same system may bear multiple roles **if** the context allows compatibility.
* For epistemes, the target of change is their **symbol carriers**; the acting side is still a **system**.

### 5.3 Boundary & externality

Every transformation is modelled with **two sides** and an explicit **U.Interaction** boundary: **acting** (system bearing TransformerRole) and **target** (system being transformed, or the **carrier** of an episteme). There is **no self‑doing**; “self‑like” stories are handled by the **reflexive split** (regulator vs regulated subsystems) or by promoting a meta‑holon and keeping evidence external (A.12).

### 5.4 Temporal alignment (A.4 bridge)

* **MethodDescription** lives in **Tᴰ**;
* **Method** is defined at design-time and **executed as `U.Work` at run-time by a `U.System` with a valid `U.RoleAssignment` (window-aligned) and a live **StateAssertion** for an **enactable** RSG state**;
* **Work** lives in **Tᴿ**;
* transitions **Tᴰ → Tᴿ** and **Tᴿ → Tᴰ** are **grounded** by executions of appropriate methods by an **external** transformer (e.g., fabrication or observation).

### 5.5 Evidence Graph Referring

Each Work anchors to **carriers** and to the **MethodDescription** it instantiates; evidencing transformers are **external** (no self‑evidence). This sits in the **EPV‑DAG** and never in mereology.

### 5.6 Didactic dictionary (safe mappings)

* “Process / Workflow / SOP / Algorithm” ⇒ **MethodDescription** (design‑time description).
* “Operation / Job / Run / Performance” ⇒ **Work** (run‑time occurrence).
* “Function (equipment spec)” ⇒ **Method** (or MethodDescription if purely textual).
* “Creator” (legacy) ⇒ **Transformer** (shorthand for **system bearing TransformerRole** after local binding).


---

# A.3.1 — U.Method  \[D]


---

# A.3.2 — U.MethodDescription  \[D]



---

## A.3.3 · `U.Dynamics` \[D]

### 1 · Context

Teams need one place to say **how a thing changes**. Physicists call this “dynamics” (equations of motion, state‑transition maps). In IT and enterprise change, we often talk about **evolution of characteristics** (latency, cost, reliability, compliance, architectural fitness) across time. In knowledge work, **KD‑CAL** (knowledge dynamics) reasons about how the **status of claims** shifts as evidence arrives. All these are *the same modeling need*: a context‑local description of **state space** and **allowed transitions**.

FPF already separates:

* **what a holon is** (structure, PBS/SBS),
* **how we act** (Method/MethodDescription, Work),
* **what we promise** (Service).

What is missing without `U.Dynamics` is the **law of change**—the model that tells us how states evolve **with or without** our interventions.

> Intuition: **Method** tells an agent what to do; **Dynamics** tells everyone how the world (or a model of it) changes when something happens (or even when nothing happens).

**Lexical note.** Terms like *process* and *thermodynamic process* are mapped by **L‑PROC**:

* the **recipe** is `U.Method/MethodDescription`,
* the **dated run** is `U.Work`,
* the **law/trajectory model** is `U.Dynamics`.

---

### 2 · Problem

Without a first‑class `U.Dynamics`, models suffer predictable failures:

1. **Recipe = Law.** Teams put the *procedure* (Method/MethodDescription) where the *state law* should be, so simulations and predictions become impossible to compare with reality.
2. **Run = Law.** Logs of Work are mistaken for dynamics; past events are treated as if they defined what *must* happen.
3. **No state space.** Discussions jump between metrics (latency! throughput!) without an explicit **characteristic space** or invariants, so “improvements” cannot be reasoned about.
4. **Domain lock‑in.** “Dynamics” is left to domain vocabularies (physics, control, finance), losing a trans‑disciplinary way to speak about change in a single kernel.

---

### 3 · Forces

| Force                                  | Tension                                                                                                                 |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Universality vs. richness**          | One kernel notion must cover ODE/PDE, Markov chains, queues, discrete events, and enterprise “fitness characteristics”. |
| **Model vs. reality**                  | A law must be **design‑time** (an `Episteme`), yet judged by **run‑time** evidence (Work).                              |
| **Continuous vs. discrete vs. hybrid** | Different time bases and update rules must coexist.                                                                     |
| **Open vs. closed systems**            | Exogenous inputs (control/disturbances) may be explicit or implicit.                                                    |
| **Predictive use vs. diagnostic use**  | The same dynamics can guide planning or explain incidents; interfaces must support both.                                |

---

### 4 · Solution — The unified concept `U.Dynamics`

**Definition (normative).**
Within a `U.BoundedContext`, **`U.Dynamics`** is an **`U.Episteme` that specifies a state space and a state‑transition law** (deterministic or stochastic, continuous/discrete/hybrid) for one or more holons, possibly under exogenous inputs and constraints. It **does not** prescribe what an agent should do (that is `U.Method/MethodDescription`) and **is not** the dated evolution itself (that is `U.Work` evidence).

* **Type:** `U.Episteme` (design‑time model/law on a carrier).
* **Orientation:** descriptive/predictive about **how states evolve**; can be used by Methods but remains separate from them.
* **Judged by:** conformance of observed **Work‑derived traces** to the law and invariants.

#### 4.1 · Core structure (minimal fields)

```
U.Dynamics {
  context        : U.BoundedContext,     // where the model’s meaning and units are defined
  stateSpace     : CharacteristicSpace,  // explicit characteristics & units; may include topology/geometry
  transitionLaw  : Episteme,             // equations/relations/kernels/transition matrices/rules
  timeBase       : {continuous|discrete|hybrid},
  stochasticity? : {deterministic|stochastic}, // incl. noise/likelihood model if stochastic
  inputs?        : P(Characteristic),    // control/disturbances/environmental drivers
  observation?   : Episteme,             // measurement/observation map from state to observables
  constraints?   : Episteme,             // invariants/safety envelopes/guards
  validity?      : Conditions,           // operating region, approximations, version, timespan
  calibration?   : Episteme              // parameter identification / priors
}
```

* **`stateSpace`** uses FPF **characteristics** (not “characteristics”) so we can talk about **architecture fitness** (e.g., latency, MTBF, cost) just like temperature/pressure/volume in physics.
* **`transitionLaw`** is paradigm‑agnostic: ODE/PDE, finite‑state relation, Petri net firing, queueing kernel, Bayesian update, etc.
* **`observation`** separates what exists from what we *measure* (key for monitoring/assurance).

#### 4.2 · What `U.Dynamics` is **not**

* **Not a Method/MethodDescription:** no imperative steps or prescriptions.
* **Not Work:** no timestamps/resources attached; evidence lives on `U.Work`.
* **Not a Service:** no consumer promise; dynamics may underpin service SLOs but does not define the promise.
* **Not PBS/SBS:** do not place dynamics inside structural BoMs.

---

### 5 · Where `U.Dynamics` sits in enactment

* **Design‑time:**
  Methods may *reference* Dynamics for planning/control (e.g., MPC uses a plant model).
  Services may *derive* acceptance targets from Dynamics (e.g., queueing predictions → SLO).

* **Run‑time:**
  Work produces **state samples/telemetry**; applying the **observation** map yields traces.
  Conformance/violation is decided by comparing traces with **constraints** and predictions from the transition law.
  Updates to model parameters flow via **calibration** (design‑time again).

> Memory hook: **Method decides**, **Dynamics predicts**, **Work reveals**.

### Prediction Use In Gating (normative)

When **predicted** coordinates (from a dynamics model) are used for **comparison or gating**, one of the following **MUST** hold:
1) a **fresh observation** is available for the gate’s window; or
2) the applied flow/map `Φ_{Δt}` is proven **non‑expansive** (Lipschitz ≤ 1) under the declared distance overlay (see § 5.1.7), **and** it **commutes** with the invariantization step (§ 5.1.6) — i.e., `Quot/Fix_g ∘ Φ_{Δt} = Φ_{Δt} ∘ Quot/Fix_g` on the domain of use.

If neither condition is satisfied, using prediction for gating is **forbidden**; the system **MUST** fall back to observation. Any use of `Φ_{Δt}` **SHALL** declare its validity window (range, Δt).

### 6 · Archetypal grounding (engineer‑manager friendly)

| Domain                        | Holon & State Space                     | Transition Law Example               | Observation                 | Typical Questions                                                 |
| ----------------------------- | --------------------------------------- | ------------------------------------ | --------------------------- | ----------------------------------------------------------------- |
| **Process control**           | Reactor: {Temperature, Concentration}   | Non‑linear ODE with disturbance term | Thermocouples, analyzers    | Will we overshoot? What control horizon keeps safety constraints? |
| **Reliability/ops**           | Service platform: {MTBF, MTTR, Backlog} | Birth–death/queueing model           | Incident logs, uptime pings | Given load, what SLO is feasible?                                 |
| **Evolutionary architecture** | System: {Latency, Cost, Coupling}       | Discrete‑time map per release        | Perf tests, bills           | If we change X, how does latency trend next 3 sprints?            |
| **KD‑CAL (knowledge)**        | Claim: {Belief, Support}                | Bayesian update rule                 | Evidence artifacts          | How does confidence evolve as studies arrive?                     |

**Key takeaway:** one kernel object captures **trajectories in a characteristic space**, from thermodynamics to software quality and knowledge confidence.


---

# A.15.1 — U.Work  \[D]


---

## 4 · Solution — define `U.Work` as the accountable, dated occurrence

### 4.1 Definition

**`U.Work`** is a **4D occurrence holon**: a **dated run‑time enactment** of a `U.MethodDescription` by a performer designated through a `U.RoleAssignment`, **executed within a concrete `U.System/SubSystem`**, inside a `U.BoundedContext`, that binds concrete parameters, consumes/produces resources, and leaves an auditable trace. 
Each `U.Work` is a **morphism** `Δ` on a declared **state‑plane** (`StatePlaneRef`), mapping ⟨**pre‑state**, **inputs**⟩ to ⟨**post‑state**, **outputs**⟩ for one or more **affected referents**.

> **Memory aid:** *Work = “how it went this time”* (dated, resourced, accountable).

### 4.2 Core anchors (conceptual descriptors; not a data schema)

When you describe a Work instance in a review, answer these prompts:

1. **Window** — start/end timestamps (and, where relevant, location/asset).
2. **Spec** — `isExecutionOf → U.MethodDescription` (the description actually followed; **edition pinned** if applicable).
3. **Performer** — `performedBy → U.RoleAssignment` (which **holder#role\:context** acted).
4. **Parameters** — concrete values bound for this run (from the **MethodDescription** parameter declarations).
5. **Inputs/Outputs** — material/information artifacts read/written, products/services delivered.
6. **Resources** — energy, materials, machine time, money (the **only** place we book them).
7. **Outcome** — success/failure classes, quality measures, acceptance verdicts (**map‑then‑compare** per **ComparatorSet** under **CG‑Spec**; pin editions).
8. **Links** — predecessor/successor/overlap relations to other Work, and step/run nesting (if part of a bigger operation).
9. **Context** — the bounded context(s) under which this run is judged (normally inherited from the MethodDescription and RoleAssigning; see A.15 for cross‑checks).
10. **Effect (Δ)** — `affected → {referent(s)}` + **pre‑state anchor** and **post‑state anchor** (or a declared **Δ‑predicate** evaluated on evidence) on the declared state‑plane (**StatePlaneRef**).
11. **System** — `executedWithin → U.System` (the operational system/sub‑system accountable for the occurrence; **mandatory**).
12. **Evidence & Telemetry (optional)** — if the run feeds **G.11** refresh or QD/OEE archives, cite **PathId/PathSliceId** and active **policy‑id** used for illumination; do not elevate gauges into dominance without CAL policy.

### 4.3 Clear distinctions (the four‑slot grammar in action)

| You are pointing at…                          | The right FPF concept  | Litmus                                                          |
| --------------------------------------------- | ---------------------- | --------------------------------------------------------------- |
| The **recipe/code/diagram**                   | **MethodDescription**         | Is it knowledge on a carrier?                                   |
| The **semantic “way of doing”**               | **Method**             | Same Standard across notations?                                 |
| The **assignment** (“who is being what”)     | **Role → RoleAssigning** | Can be reassigned without changing the system?                  |
| The **ability** (“can do within bounds”)      | **Capability**         | Would remain even if not assigned?                             |
| The **dated occurrence** with logs, resources | **Work**               | Did it happen at (t₀, t₁), consume resources, produce outcomes? |
| The **state change caused this time**         | **Work.Δ**             | Did the referent move from pre→post on the declared state‑plane? |

### 4.4 Publication (MVPK guard‑rails for `U.Work`) — *normative*
Publication of `U.Work` across MVPK faces **must** be a typed projection that does **not** mutate intensional semantics (A.7; E.17). Concretely:
1. **No new claims.** Faces (**PlainView / TechCard / InteropCard / AssuranceLane**) **SHALL NOT** introduce properties beyond the `U.Work` intensional arrow; they **project** presence‑pins only (time window, performer, spec, parameter‑binding occurrence, resource ledger presence, acceptance verdict presence). Numeric/comparable content appears **only** with pins (see 4.4‑4.5 below); **“signature”** is banned on faces.
2. **No Γ‑leakage.** Faces **MUST NOT** smuggle Γ semantics (union/hull/overlap policy, budget algebra) into prose; whenever aggregation is shown, the face **cites** the Γ‑operator and policy‑id used. Compute totals outside the face per B.1; faces carry **references**, not implied Γ rules.
3. **No I/O re‑listing.** Per MVPK, faces **do not duplicate** intensional I/O lists. They show **presence‑pins** and **anchors** to carriers/lanes/editions only (E.17 §5.4).
4. **Lawful orders (sets).** Where a `U.Work` face presents any **comparison or ranking across runs** (e.g., acceptance classes, parity/benchmark inserts), the face **must**: (i) compare **after mapping** via a declared **ComparatorSet**; (ii) **return sets** (Pareto/Archive) when order is partial; (iii) **forbid** hidden scalarization/ordinal means (cf. G.9).
5. **Comparator/Transport edition pins.** Any numeric/comparable statement on a `U.Work` face **MUST** pin the **CG‑Spec**/**ComparatorSet** edition(s) and, where scale/plane conversion occurs, the **UNM.TransportRegistry** edition (**Φ**/**Φ^plane** policy‑ids). Cross‑context/plane crossings **route penalties to R‑lane only** (Bridge id + Φ) (cf. E.17; G.9).
6. **Cross‑tier citations.** Any citation of AT1/AT2 artefacts on a `U.Work` face **MUST** carry **BridgeCard + UTS row** (with plane notes and CL routing).
7. **No surrogate‑run creation.** Faces **MUST NOT** synthesize “virtual runs” from reconstructed records alone; a face may reference only `U.Work` instances that meet Δ‑anchoring in §4.2/§8.

### 4.5 ATS profile & crossings (tier discipline) — *normative*
* **Tier.** `U.Work` is **AT0**. Any face that cites AT1/AT2 artefacts (e.g., ComparatorSet, CG‑Spec editions) **MUST** include **BridgeCard + UTS row** and record **Φ(CL)/Φ^plane** policy‑ids; **penalties reduce `R_eff` only**.
* **Binding discipline.** **Launch values bind only here** (occurrence). Plan‑time proposals remain proposals; do not back‑fill plan faces with run‑time bindings. **Pre/post state anchors bind here** (pre at start; post at completion or at declared checkpoints).


---

# A.15.2 — U.WorkPlan  \[D]



---

## 4 · Solution — the `U.WorkPlan` as the time‑bound intention to execute Work

### 4.1 Definition

**`U.WorkPlan`** is an **`U.Episteme`** that **declares intended `U.Work` occurrences** over a horizon, with **planned windows**, **dependencies**, **intended performers** (as **role kinds** or **proposed RoleAssignings**), **resource budgets/reservations**, and **acceptance targets**—**within a `U.BoundedContext`**.

> **Strict distinction (memory aid):**
> **Method** = *how in principle*. **MethodDescription** = *how it is written*.
> **WorkPlan** = *when, by whom in intent, under which constraints*.
> **Work** = *how it went this time*.

### 4.2 Plan Items (what a `WorkPlan` is made of)

A `U.WorkPlan` **contains Plan Items** (think: scheduled tasks/ops), each of which typically states:

1. **Target Method/Spec** — the **Method** to be enacted and the **MethodDescription** intended for enactment.
2. **Planned window** — e.g., earliest start/latest finish, timebox, recurrence (cron‑like), blackout periods.
3. **Role requirements** — **role kinds** required (not people), optional **proposed RoleAssigning(s)** if pre‑assignment is allowed in the context.
4. **Capability thresholds** — minimal abilities required of the performer (checked at run time).
5. **Resource budgets/reservations** — planned energy/materials/machine slots/money; reservations on assets.
6. **Dependencies** — precedence/overlap permissions; gates/approvals.
7. **Acceptance targets** — quality windows/SLA targets to be judged when Work completes.
8. **Location/asset constraints** — where the run is expected to take place.
9. **Links to Service promises** (if any) — external commitments that this plan aims to satisfy.

> **Didactic guardrail:** **No logs or actuals** belong in a WorkPlan; **no step logic** or solver internals either—that’s the Method/Spec.

### 4.3 Clear distinctions (lexical sanity for “schedule/process/workflow”)

| If you say…                                 | In FPF it is…                                        | Why                                               |
| ------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------- |
| “The **schedule** for tomorrow’s surgeries” | **`U.WorkPlan`**                                     | Calendar of intended runs (who/when constraints). |
| “The **workflow** for appendectomy”         | **`U.MethodDescription`** (and `U.Method`)                  | Recipe and semantic way, not a calendar.          |
| “The **process** already ran at 10:00”      | **`U.Work`**                                         | A dated run with resources and outcomes.          |
| “The **thermodynamic process** path”        | **`U.Work`** (occurrence) + **`U.Dynamics`** (model) | A realized trajectory plus its model, not a plan. |
| “The **plan** assigns Dr. Lee”              | **WorkPlan** naming an **intended** RoleAssigning      | assignment is still validated at run time.       |
| “The **budget** for Shift‑B”                | **WorkPlan** (planned ledger)                        | Actual costs land on **Work**, not on the plan.   |

> **L‑SCHED (lexical rule).** In this document, words like **schedule**, **calendar**, **rota**, **Gantt**, **plan** point to **`U.WorkPlan`** unless explicitly redefined by a bounded context glossary.

### 4.4 Plan mereology (composition of plans ≠ composition of methods or runs)

Keep three separations crystal‑clear:

* **Method composition** (design‑time semantics) → produces **new Methods**.
* **Work composition** (run‑time occurrences) → produces **parent/child runs** with overlaps/episodes.
* **Plan mereology** (epistemic structure) → organizes **Plan Items** for coordination (phases, sprints, shifts), with **precedence** and **resource reservations**.

**Common relations among Plan Items:**

* **`Precedes_pl` / `DependsOn_pl`** — start/finish constraints and gates.
* **`MayOverlap_pl` / `MutuallyExclusive_pl`** — allowed overlaps vs exclusive windows.
* **`Refines_pl`** — a child plan item tightens windows/budgets of a parent.
* **`Alternative_pl`** — planned alternatives (e.g., backup rig, backup team).

**Didactic rule:** A Plan Item **does not force** an identical Work shape; mapping is via **fulfilment** and **variance** (see §6).

### 4.5 How `WorkPlan` meets `Work` (fulfilment & variance)

When reality happens, each `U.Work` may:

* **Fulfil** a Plan Item — link `plannedAs → PlanItem`.
* **Partially fulfil** — multiple Work instances share one Plan Item (e.g., split run), or one Work fulfils several Plan Items (e.g., consolidated batch).
* **Deviate** — execute with method/spec substitution, different window, different performer (still valid or policy‑exception).
* **Be unplanned** — Work with no Plan Item (emergency, ad‑hoc); must be labeled as such.

**Variance dimensions** the plan expects to report on:

* **Schedule variance (Δt):** early/late vs planned window.
* **Cost variance (Δc):** actual resource spend vs budget.
* **Scope variance:** different Method/Spec than planned (with justification).
* **Quality variance:** acceptance verdict vs target.
* **Assignment variance:** intended vs actual RoleAssigning.

> **Manager’s view:** A plan that cannot report variance is a calendar picture, not a management tool.

---
