## **B.1.4 Contextual & Temporal Aggregation (Γ\_ctx & Γ\_time)** \[A]

> **► decided‑by: A.14 Advanced Mereology**
**A.14 compliance —** **Γ\_ctx** relies on **SerialStepOf/ParallelFactorOf** (order semantics); **Γ\_time** composes **PhaseOf** slices of the *same* carrier with coverage/no‑overlap; **PortionOf** is orthogonal (quantities within steps), mappings are not parthood.

> **Plain‑English headline.**
> Use **Γ\_ctx** when *the order of steps changes meaning*.
> Use **Γ\_time** when *we are aggregating the same carrier across a timeline*.

### 1) Problem frame

The universal algebra **Γ** (B.1) assumes local commutativity and locality for most structures. But many real‑world compositions are **not** order‑indifferent (recipes, proofs that unfold by steps, manufacturing routes), and many composites are **nothing but** a history (asset lifecycle, model revisions, experiment runs). For these cases FPF offers two universal flavours:


* **Γ\_ctx** — **procedural composition** (where SerialStepOf / ParallelFactorOf edges are present; see B.1.5 Γ_method for typing and joins; A.14 governs only mereological edges such as PortionOf/PhaseOf).
**Γ\_time** — *temporal* aggregation for **phase composition of the same carrier** (where `PhaseOf` edges from **A.14** are present).

Both flavours **inherit WLNK and MONO** from the Quintet (B.1) and remain compatible with **A.12** (Transformer Principle) and **A.15** (Strict Distinction): they do *order* and *time*, not structure, mapping, or cost.

---

### 2) Problem

Forcing sequential or temporal phenomena through the default, order‑indifferent Γ leads to recurring failures:

1. **Semantic erasure:** Treating `SerialStepOf` as if it were structural parthood flattens workflows; swapping steps silently changes meaning.
2. **Causal paradoxes:** Aggregating time slices as if they were unordered parts lets effects precede causes, or hides missing epochs.
3. **Locality violations:** Hidden shared state between “parallel” branches breaks reproducibility; independent branches were not actually independent.
4. **Design/run conflation:** Mixing design‑time plans and run‑time histories in one fold produces “chimeras” that neither simulate nor audit reality.

---

### 3) Forces

| Force                                 | Tension                                                                                                          |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Order fidelity vs. Simplicity**     | Preserve step order (non‑COMM) ↔ Keep reasoning lightweight and composable.                                      |
| **Temporal coverage vs. Flexibility** | Ensure gap/overlap discipline across phases ↔ Allow rolling windows and partial histories.                       |
| **Locality vs. Concurrency**          | Keep branches deterministic and independent ↔ Exploit parallelism where it is safe.                              |
| **Universality vs. Fit**              | One pattern for systems and epistemes ↔ Different edge types (`SerialStepOf`, `PhaseOf`) and different carriers. |

---

### 4) Solution — **Part 1: What these flavours are, and when to use them**

#### 4.1 Two flavours at a glance (edge discipline)

| Flavour                                      | You use it when…                                                      | Edge kinds in `D`                                         | Typical carrier                                                            |
| -------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Γ\_ctx** *(Contextual / order‑sensitive)*  | The **sequence** of steps changes the outcome or meaning.             | `SerialStepOf`, `ParallelFactorOf` (no structural substitution) | `U.Method` (procedures, work processes), also order‑bound argument chains in `U.Episteme` |
| **Γ\_time** *(Temporal / phase aggregation)* | You reconstruct a **timeline** of the **same** holon (phases/slices). | `PhaseOf` of a single carrier (non‑overlapping)                 | Any `U.Holon` with identity across time (systems or epistemes)             |

> **Strict Distinction (A.15) reminder.**
> • Structural inclusion → **Γ\_sys** (ComponentOf / ConstituentOf).
> • Order of actions → **Γ\_ctx** (and its specialisation **Γ\_method**).
> • History of the same thing → **Γ\_time** (PhaseOf).
> • Resource spending → **Γ\_work**.
> • Mappings / representations → value‑level links or `U.Interaction`, not parthood.

---

#### 4.2 Operator signatures (normative)

**Γ\_ctx — Contextual / Order‑Sensitive Aggregation**

```
Γ\_ctx : (D_ctx : DependencyGraph, σ : OrderSpec, T : U.TransformerRole) → H′ : U.Holon
```

* **D\_ctx:** a DAG whose **edges are only** `SerialStepOf` / `ParallelFactorOf`.
* **σ (OrderSpec):** an explicit **partial order** (or total order) compatible with `D_ctx` that disambiguates how branches compose and where joins occur.
* **T:** the transformer that performs the material act of sequencing/combining steps (A.12).
* **Output H′:** typically a `U.Method` holon, but may be any holon whose identity is defined by stepwise construction.

**Γ\_time — Temporal / Phase Aggregation**

```
Γ\_time : (D_time : DependencyGraph, τ : TimeWindow, T : U.TransformerRole) → H′ : U.Holon
```

* **D\_time:** a DAG whose **edges are only** `PhaseOf`, all phases referring to the **same carrier** identity.
* **τ:** the declared time window to be covered by the aggregation.
* **T:** the transformer that composes the timeline (A.12).
* **Output H′:** the holon reconstructed over τ (system lifecycle, theory revision history, dataset growth, etc.).

---

#### 4.3 Adapted invariants (what replaces COMM/LOC)

Both flavours **keep** IDEM, WLNK, MONO from B.1. They **replace** COMM/LOC by discipline specific to order and time.

**For Γ\_ctx (NC‑invariants):**

* **NC‑1 — Determinism under σ.** Given the same `D_ctx` and `σ`, the fold yields the same result.
* **NC‑2 — Context identifier.** The result **SHALL** record an unambiguous identifier of `σ` (e.g., a canonical text or digest) as part of the aggregation record.
* **NC‑3 — Partial‑Order Soundness.** Any topological sort consistent with `σ` and with declared independence (below) yields the same result; independent branches may fold in parallel.

**For Γ\_time (T‑invariants):**

* **T‑1 — Temporal Idempotence.** A single phase/slice folds to itself.
* **T‑2 — Chronological Discipline.** Phases must be composed in non‑decreasing time consistent with carrier identity; reversing adjacent slices is forbidden.
* **T‑3 — Coverage.** The union of phase intervals equals the declared `τ`, with **no overlaps** and **no unexplained gaps**. Gaps/overlaps require explicit justification (e.g., measurement resolution or MHT).

> **Why we keep WLNK and MONO.**
> Even with order/time, the whole cannot be safer or more reliable than the bottleneck step/phase (WLNK), and improving a step/phase on declared monotone characteristics cannot make the whole worse (MONO).

---

#### 4.4 Guards that make the folds provable

**For Γ\_ctx**

1. **Edge discipline:** only `SerialStepOf` / `ParallelFactorOf`.
2. **OrderSpec σ:** explicit partial order; joins must have well‑typed inputs/outputs (see B.1.5 for join soundness).
3. **Independence declaration:** if you claim parallel folds commute locally, declare **which branches are independent** (no hidden shared state or side‑effects).
4. **Scope:** single `DesignRunTag` (design *or* run) for all nodes; do not mix plans with histories.
5. **Boundary note:** if steps cross holon boundaries, record the relevant `U.Interaction`—do not recast it as parthood.

**For Γ\_time**

1. **Same carrier:** all phases are `PhaseOf` the **same** holon identity; identity change implies a Transformer producing a *new* holon.
2. **Non‑overlap / coverage:** phase intervals are disjoint and cover `τ`; if not, specify how resolution limits or business rules justify the pattern.
3. **Scope:** single `DesignRunTag`; design‑time hypothetical timelines and run‑time actual logs are kept separate.
4. **Boundary note:** if Work across boundaries is reported for phases, route resource statements to **Γ\_work**; Γ\_time itself does not invent costs.

---

#### 4.5 Selection checklist (didactic quick guide)

* **Does swapping two steps change meaning or safety?** → **Γ\_ctx**.
* **Is this the same entity evolving over time?** → **Γ\_time**.
* **Is it a physical assembly or conceptual inclusion?** → **Γ\_sys**.
* **Is it a “who belongs to this collective” question?** → **MemberOf** + (future) **Γ\_collective**.
* **Do you need durations, critical paths, and joins?** → **Γ\_method** (specialisation of **Γ\_ctx**).
* **Do you need resource spending across a boundary?** → **Γ\_work** (orthogonal; can be used together with Γ\_ctx/Γ\_time).

---

#### 4.6 Didactic contrasts (one‑liners)

* **Γ\_sys vs Γ\_ctx:** Γ\_sys composes *what the whole is*; Γ\_ctx composes *how it is done*.
* **Γ\_ctx vs Γ\_method:** Γ\_method is Γ\_ctx **plus** step‑specific rules (durations, joins, capability typing).
* **Γ\_time vs Γ\_ctx:** Γ\_time composes *phases of the same carrier*; Γ\_ctx composes *different steps that realise a procedure*.
* **Γ\_time vs Γ\_work:** Γ\_time composes *history*; Γ\_work accounts *costs across a boundary* for each phase.

### 5) Proof Kit (ready‑to‑reuse obligations for Γ\_ctx / Γ\_time)

This Proof Kit instantiates the generic obligations from **B.1.1 §6** for the order/time flavours. Attach these items whenever you call Γ\_ctx or Γ\_time on a `DependencyGraph D`.

#### 5.1 Γ\_ctx obligations

* **CTX‑IND (Independence & Joins).**
  Declare **which branches are independent** (no hidden shared state, no side‑effects that leak across branches). For every **join**, state a **join‑soundness condition** (compatible input/output types and pre/postconditions).
  *Claim:* Under CTX‑IND, parallel folds of independent branches commute locally; any topological sort consistent with `σ` yields the same result (NC‑3).

* **CTX‑ORD (OrderSpec).**
  Provide the **OrderSpec `σ`** as a partial order (or total order) text, including where joins occur.
  *Claim:* Given `D_ctx` and `σ`, the fold is deterministic (NC‑1) and carries a stable **context identifier** (NC‑2).

* **CTX‑WLNK (Critical Path).**
  Identify the **critical path** (or a cutset) whose weakest step caps the property of the whole: throughput, safety, assurance, etc.
  *Claim:* The whole is bounded by the weakest element along the critical path (WLNK).

* **CTX‑MONO (Monotone characteristics).**
  List the characteristics that cannot degrade the whole when improved: e.g., ↓ step duration, ↓ error rate, ↑ step reliability, ↑ join soundness.
  *Claim:* Improving only monotone characteristics cannot make the aggregated process worse (MONO).

* **CTX‑IDEM (Singleton).**
  Provide the one‑step singleton witness: Γ\_ctx of a single `SerialStepOf`‑free node returns that step unchanged (IDEM).

* **CTX‑SCOPE/BOUND.**
  Affirm a **single DesignRunTag** (`design` or `run`) and list any **U.Interaction** that crosses a holon boundary (do not recast it as parthood).

#### 5.2 Γ\_time obligations

* **TIME‑CARR (Carrier Identity).**
  State explicitly the **carrier holon** whose history is being reconstructed.
  *Claim:* All `PhaseOf` arcs refer to the same carrier; if identity changes, model a Transformer producing a new holon (A.12), not another phase.

* **TIME‑COV (Coverage & Non‑overlap).**
  Provide the target **TimeWindow τ** and the list of phases with intervals; justify any gaps or overlaps (resolution limits, business rules).
  *Claim:* Phases cover τ without overlap; otherwise the fold is not admissible (T‑3).

* **TIME‑ORD (Chronological Discipline).**
  Assert that fold order is non‑decreasing in time; reversing adjacent slices is forbidden.
  *Claim:* Temporal idempotence holds on a single slice, and chronological composition preserves consistency (T‑1, T‑2).

* **TIME‑WLNK (Temporal Weakest‑Link).**
  Identify time‑critical constraints: missing essential phases, minimal sampling resolution, minimal integrity of a crucial epoch.
  *Claim:* The property of the whole (over τ) is capped by the weakest phase/epoch.

* **TIME‑MONO (Monotone characteristics).**
  List monotone improvements: ↑ coverage, ↑ timestamp precision, ↑ measurement accuracy, ↑ calibration quality.
  *Claim:* Such improvements cannot degrade the aggregate.

* **TIME‑SCOPE/BOUND.**
  Keep design‑time hypothetical timelines and run‑time actual logs separate; route resource statements for phases to **Γ\_work** (not Γ\_time).

---

### 6) Archetypal grounding (worked micro‑examples)

Use these as templates; each fits on a page and references the obligations above.

#### 6.1 **Γ\_ctx — U.System (manufacturing route)**

* **Graph:** `Prep SerialStepOf Weld SerialStepOf Paint`; `QC ParallelFactorOf Paint` with a join; scope=`run`.
* **CTX‑IND:** `QC` is independent of `Prep/Weld` state; join requires “painted & inspected” flags aligned.
* **CTX‑ORD:** `σ` is total: `Prep → Weld → Paint`; `QC` runs in parallel with `Paint`, joins at `Finish`.
* **CTX‑WLNK:** Slowest/least reliable step on the critical path caps throughput and assurance.
* **CTX‑MONO:** ↓ duration of `Weld`; ↑ join condition coverage → cannot reduce overall safety.
* **Routing:** Costs/energy are handled per step with **Γ\_work**; structure of subassemblies remains in **Γ\_sys**.

#### 6.2 **Γ\_ctx — U.Episteme (order‑bound argument)**

* **Graph:** `PremiseA SerialStepOf LemmaB SerialStepOf Conclusion`; `Background ParallelFactorOf PremiseA`.
* **CTX‑IND:** `Background` does not alter `LemmaB` assumptions; join checks entailment preconditions.
* **CTX‑WLNK:** Weakest premise on the entailment spine caps the argument’s reliability.
* **SCR:** Γ\_epist on the final `Conclusion` produces a SCR linking every source; Γ\_ctx assures the order.

#### 6.3 **Γ\_time — U.System (asset lifecycle)**

* **Carrier:** *This* turbine T‑17.
* **Phases:** `Install [t0,t1)`, `Operate v1 [t1,t2)`, `Overhaul [t2,t3)`, `Operate v2 [t3,t4)`.
* **TIME‑COV:** Intervals cover `[t0,t4)` with no overlap; a gap between `t2` and `t2+ε` is justified as clock resolution.
* **TIME‑WLNK:** The weakest reliability epoch caps lifetime MTTF claimed for `[t0,t4)`.
* **Routing:** Work/energy footprints per phase via **Γ\_work**; structural upgrades (new rotor) are Transformers (A.12), not phases, if identity changes.

#### 6.4 **Γ\_time — U.Episteme (paper revisions)**

* **Carrier:** *This* paper P.
* **Phases:** `Draft v1`, `Review v2`, `Camera‑ready v3`.
* **TIME‑ORD/COV:** Non‑overlapping versions covering the documented interval; v3 supersedes v2, not a parallel branch.
* **TIME‑WLNK:** If v2 violated a key citation, overall reliability over `[v1,v3]` is capped by that epoch unless the violation is explicitly retracted and corrected in v3 (documented change).
* **Routing:** Γ\_epist aggregates the conceptual whole at each version; Γ\_time composes the revision history.

---

### 7) Conformance Checklist (normative checklist)

| ID            | Requirement                                                                                                                                                                     | Purpose                                       |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **CC‑B1.4.1** | **Γ\_ctx** input `D_ctx` SHALL use **only** `SerialStepOf` / `ParallelFactorOf` edges; **Γ\_time** input `D_time` SHALL use **only** `PhaseOf` edges.                           | Keep flavours matched to A.14 edges.          |
| **CC‑B1.4.2** | **OrderSpec `σ`** (for Γ\_ctx) or **TimeWindow `τ`** (for Γ\_time) SHALL be explicitly declared.                                                                                | Determinism and auditability (NC‑1/2, T‑2/3). |
| **CC‑B1.4.3** | An **independence declaration** (Γ\_ctx) or **coverage declaration** (Γ\_time) SHALL be attached, with join‑soundness statements (Γ\_ctx) and non‑overlap proof (Γ\_time).      | Make replaced COMM/LOC discipline explicit.   |
| **CC‑B1.4.4** | **WLNK cutset** SHALL be identified (critical path for Γ\_ctx; critical epoch for Γ\_time).                                                                                     | Conservative bounds.                          |
| **CC‑B1.4.5** | **MONO characteristics** SHALL be listed and justified for the call.                                                                                                                       | Prevent hidden regress.                       |
| **CC‑B1.4.6** | All nodes SHALL share the same `DesignRunTag` (`design` or `run`) in a single fold.                                                                                            | Ban design/run chimeras.                      |
| **CC‑B1.4.7** | Structural inclusion, mappings, and resource spending SHALL NOT be encoded as order/time edges; route to **Γ\_sys / Γ\_epist**, value‑level links or **Γ\_work** respectively. | Enforce A.15 Strict Distinction.              |
| **CC‑B1.4.8** | If coverage breaks or identity changes, the modeller SHALL refactor the graph or declare a **Meta‑Holon Transition** (B.2).                                                     | Make emergence explicit.                      |

---

### 8) Anti‑patterns and their fixes

| Anti‑pattern                         | Symptom                                                     | Fix                                                                                                                     |
| ------------------------------------ | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Structure‑as‑sequence**            | `StepB ComponentOf StepA` to force an order                 | Use `SerialStepOf` (Γ\_ctx) and an explicit `σ` with a join condition if needed.                                        |
| **History‑as‑structure**             | `v2 ComponentOf v1`                                         | Use `PhaseOf`; if identity actually changed, model a Transformer (A.12) producing a new holon.                          |
| **Parallelism without independence** | Declaring `ParallelFactorOf` but sharing hidden state       | Either declare the shared state as an interface and remove independence, or refactor so branches are truly independent. |
| **Overlapping phases**               | Two `PhaseOf` intervals for the same carrier overlap        | Split the intervals or justify overlap as measurement resolution; otherwise fold is invalid.                            |
| **Design/run chimera**               | Mixing run logs with design plan in one Γ\_ctx/Γ\_time fold | Split into two graphs by scope; relate through a Transformer or mapping at value level.                                 |
| **Cost in Γ\_time**                  | Trying to sum energy in Γ\_time                             | Route costs to Γ\_work per phase; Γ\_time composes history, not expenditure.                                            |

---

### 9) Consequences

**Benefits**

* **Semantic fidelity:** Order and history are first‑class; no more flattening sequential logic or erasing temporal causality.
* **Auditable determinism:** An explicit `σ`/`τ` and independence/coverage declarations make folds reproducible and reviewable.
* **Safe parallelism:** Partial‑order soundness preserves determinism while exploiting concurrency where it is actually safe.
* **Clean separation of concerns:** Structure (Γ\_sys/Γ\_epist), order (Γ\_ctx/Γ\_method), time (Γ\_time), and cost (Γ\_work) no longer interfere.

**Trade‑offs / mitigations**

* **Extra declarations:** Independence, joins, and coverage require up‑front articulation.
  *Mitigation:* reuse the Proof Kit forms; adopt the decision checklist from Part 1 §4.5.
* **Limited parallelism:** Where branches are not independent, concurrency must be curtailed.
  *Mitigation:* regroup steps; elevate shared state to explicit interfaces.

---

### 10) Rationale (informative)

This pattern implements **A.15’s ordered relations** (`SerialStepOf`, `ParallelFactorOf`) and leverages **A.14’s `PhaseOf`** for timeline; consistent with **Strict Distinction**: order and time are not structure, and costs are not history. The adapted invariants (NC‑1..3 and T‑1..3) give precise replacements for COMM/LOC where these do not hold, while retaining WLNK and MONO. The result is a small, stable interface that matches how engineers and researchers already argue about procedures and histories, without importing domain‑specific notations into the kernel.

---

### 11) Relations

* **Builds on:** B.1 (Universal Γ), B.1.1 (Dependency Graph & Proofs), A.12 (Transformer), A.14 (Mereology Extension), A.15 (Strict Distinction).
* **Specialises into:** **B.1.5 Γ\_method** (adds duration, capability typing, join soundness rules).
* **Works alongside:** **B.1.6 Γ\_work** (resource accounting per step/phase).
* **Triggers:** **B.2 Meta‑Holon Transition (MHT): Recognizing Emergence and Re‑identifying Wholes** when re‑ordering or re‑phasing produces genuinely new properties.
* **Feeds:** **B.4 Canonical Evolution Loop** (time‑aware cycles that carry explicit costs and order).

> **One‑page takeaway.**
> If **order changes meaning**, use **Γ\_ctx** with an explicit **OrderSpec** and independence/joins.
> If you are **composing the same carrier across time**, use **Γ\_time** with a **TimeWindow**, coverage, and identity.
> Keep structure, mapping, and cost in their places, and the invariants will do the rest.
