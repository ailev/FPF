## **B.1.6 Γ\_work — Work as Spent Resource** \[D]

+> **► decided‑by: A.14 Advanced Mereology**
+**A.14 compliance —** Only **Work** carries resource deltas; quantitative splits/consumption use **PortionOf** against pre‑consumption stocks; run histories use **PhaseOf** on Work; `MemberOf` MUST NOT be used for resource mereology; SCR/RSCR stay outside (use EPV‑DAG anchors).
 
### Problem frame

FPF distinguishes **what is done** from **what it costs** to do it.

* **Method / Process (design‑time vs run‑time):**
  A **MethodDescription** is a design‑time description of how a transformation is to be performed. At run‑time, a **Method** is the execution of that MethodDescription by a **Transformer** (A.12, A.15).
  In Cluster B, sequencing and coordination of methods are handled by **Γ\_method** (B.1.5).

* **Work (this pattern):**
  **Work** is the **spent resource** caused by executing a Method. It is not “a process.” It is the **resource delta** we can account for across a holon boundary while a Method runs. Γ\_work defines how such deltas compose.

This separation makes models auditable and prevents category errors: **Γ\_method** composes *actions*; **Γ\_work** composes the *resource expenditure* of those actions.

---

### Problem

Without a dedicated algebra for spent resources, models drift into four errors:

1. **Process–Work conflation:** Time‑ordered steps and resource spending are mixed, producing ambiguous or double‑counted totals.
2. **Conservation violations:** Totals appear that exceed inputs or create “free” resource, contradicting physical and informational conservation.
3. **Boundary blindness:** Spending is reported without specifying the boundary across which it is measured, making numbers non‑comparable.
4. **Category errors in mereology:** Collection membership (MemberOf) is misused as if it were parthood for resource stocks, polluting Γ proofs (B.1).

---

### Forces

| Force                                               | Tension                                                                                                                        |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Conservation vs. Abstraction**                    | Totals must obey material/energy/information conservation ↔ models must stay simple and readable.                              |
| **Run‑time measurability vs. Design‑time planning** | We need measurable deltas at run‑time ↔ we also need ex‑ante yields from MethodDescription to plan.                                   |
| **Heterogeneous units vs. Unified sums**            | Resources come in different units (joules, kg, bits) ↔ we still need composite statements (vectors, typed sums).               |
| **Safety vs. Synergy**                              | Weakest‑link bounds must cap availability ↔ redundancy or substitution can improve feasibility but belongs to emergence (B.2). |

---

### Terminology guard‑rails (A.15 — Strict Distinction)

> These rules are normative in this pattern; they exist to prevent the recurring confusion noted in prior drafts.

* **MethodDescription** — design‑time description of a transformation (parameters, intended yield η).
* **Method** — the run‑time execution of that MethodDescription by a **Transformer**; it exists only while it runs.
* **Process** — a method seen as an ordered structure of steps; composed by **Γ\_method**.
* **Work** — **spent resource** (a measurable delta across a declared boundary) caused by executing a Method; composed by **Γ\_work**.
* **Transformer (T)** — a **U.System** playing a role that executes a Method (A.12).
* **Mereology for resources (A.14):** use `PortionOf` for **quantitative splits** and `PhaseOf` for **time‑slices**; **do not** use `MemberOf` for resource stocks.

---

### Solution — The Γ\_work Operator 
#### Part 1 — Operator & Basic Definitions

**Intent.** Provide a universal, conservative way to compose resource spending across parts and steps, without talking about control‑flow (that is Γ\_method’s job).

##### 1) Operator signature

```
Γ_work : (R : ResourceGraph, M_spec : U.MethodDescription?, T : U.TransformerRole) → W_tot : U.Work
```

* **R — ResourceGraph.** An acyclic graph whose nodes are **U.Resource** holons with typed, extensive quantities (e.g., energy, mass, information). Edges are **`consumes`**, **`produces`**, **`transfers`** and are tied to explicit **U.Boundary** declarations (A.14). Where a stock is subdivided, the split uses `PortionOf`; where a run is time‑sliced, the slices use `PhaseOf`.

* **M\_spec — optional.** If present, it provides *ex‑ante* yield/efficiency (η) for planning; if absent, Γ\_work composes purely from measured deltas.

* **T — TransformerRole.** The external system that executes or validates the resource accounting for the run; T is not a node of R (A.12).

* **Result W\_tot — U.Work.** A typed **Work vector** (possibly sparse) with the same basis as the resources in R. It is accompanied by a **Boundary Ledger** (see §3).

> **Do not confuse:** Γ\_work neither schedules nor orders steps; it composes **deltas**. If you need order, use Γ\_method and then apply Γ\_work per step and fold the resulting Work vectors (see Relations in Part 2).

##### 2) What counts as “Work”

Work is defined **with respect to a declared boundary** of the holon being transformed or assembled:

* **Boundary‑relative delta (conservative form):**
  For any resource type *q* measured on boundary *B* during a run,

  ```
  Work_B(q) = Inflow_B(q) − Outflow_B(q) − ΔStock_inside(q)
  ```

  where **ΔStock\_inside(q)** is the change of internal stock over the run (positive when the stock grows).

* **Embodiment split:**
  Work can be split into **Dissipation** (lost to environment) and **Embodied** (retained in produced holons as state). Both are part of the same Work vector; the split is a reporting choice, not a second algebra.

* **Heterogeneous vectors:**
  Γ\_work treats different resource types as a **typed vector space** (no implicit conversion). Equivalences (e.g., joules↔bits via a declared model) are allowed only if **declared in M\_spec** or in a domain CAL; otherwise vectors remain multi‑dimensional.

##### 3) Boundary Ledger (normative output metadata)

Every Γ\_work result **MUST** include a **Boundary Ledger**:

* **(i) Boundary scope:** which `U.Boundary` was used (source holon, ports).
* **(ii) Time window:** start/stop or `PhaseOf` slice identifiers.
* **(iii) Basis:** the ordered list of resource types and units.
* **(iv) Method context:** reference to `M_spec` (if any) and run identifier of the Method.
* **(v) Transformer:** identity of **T** (system playing the executing or auditing role).

This ledger is what makes cross‑model Work totals comparable and auditable (A.10).

##### 4) The invariant quintet instantiated (overview)

Γ\_work preserves B.1 invariants; the detailed proofs and corner cases are in Part 2.

* **IDEM (idempotence):** Work over a graph with a single resource node and no consumption edges is the zero vector.
* **COMM / LOC (local commutativity / locality):** For **independent** subgraphs, composed Work is additive and independent of local fold order.
* **WLNK (weakest‑link bound):** Effective Work is capped by the scarcest **critical** input on the boundary (no Work can exceed available supply).
* **MONO (monotonicity):** Increasing an available resource cannot decrease Work (for the same boundary and time window); decreasing dissipation or improving η cannot reduce feasibility.

##### 5) How Γ\_work relates to Methods (and to Γ\_method)

* **Design‑time:** `M_spec` may declare an intended yield **η** and admissible equivalences between resource types (e.g., heat→mechanical), but these are **assumptions** until a Method runs.
* **Run‑time:** A Method instance (executed by **T**) produces actual deltas. Γ\_work composes those deltas; it does not speculate.
* **Sequencing:** If multiple Methods are ordered, use **Γ\_method** to compose the order, then apply Γ\_work per step and sum the Work vectors (independent branches sum; synchronized branches take max on **time**, not on **Work**).

> **Didactic tip:** Think of **Γ\_method** as the **story of what happened**, and **Γ\_work** as the **receipt of what it cost**, both anchored to the same boundary and time window.

##### 6) Fold rules (how Γ\_work composes)

**6.1 Boundary partition (across parts of a whole)**
Let the system‑level boundary **B** be covered by a finite family of pairwise‑disjoint sub‑boundaries **{Bᵢ}** (ports, surfaces, interfaces) that together exhaust **B**. For any resource type *q* in the basis:

* **Partition additivity (normative):**

  ```
  Work_B(q) = Σ_i Work_Bi(q)
  ```

  Preconditions: (i) `Bi` are disjoint except for measure‑zero interfaces, (ii) meters are aligned (same units, same time window), (iii) internal stock changes ΔStock\_inside(q) are measured for the *same* closed region bounded by B.
  *Why it matters:* this is the cross‑scale rule that lets part‑level Work totals roll up to the whole without double counting.

**6.2 Time slicing (serial runs / phases)**
Let the run be split by a set of non‑overlapping intervals **{τⱼ}** that cover the window **τ** (use `PhaseOf` to tag the slices). Then:

```
Work_B(q, τ) = Σ_j Work_B(q, τ_j)
```

This is the **temporal additivity** of Work. It is the Γ\_work analogue of Γ\_time’s coverage rule: we never “smear” or reorder; we sum non‑overlapping slices.

**6.3 Concurrent branches (parallel activity)**
When two independent sub‑boundaries **B₁**, **B₂** are active over overlapping time, total Work still **adds**:

```
Work_B(q) = Work_B1(q) + Work_B2(q)
```

Independence here means: no shared port, no shared stock variable, no hidden transfer between B₁ and B₂ that bypasses the declared meters. If a shared internal stock exists, it must be accounted in ΔStock\_inside(q) for **B** to keep conservation exact.

> **Didactic contrast:** Γ\_method handles **duration** (Σ for serial, max for parallel). Γ\_work handles **resource** (Σ in both serial and parallel), because resource spending composes additively across disjoint boundary parts and disjoint time slices.

**6.4 Multi‑resource vectors and declared equivalences**
Γ\_work never implicitly converts units. If a planning model needs an exchange (e.g., heat→mechanical, memory→compute), it must be **declared** in `M_spec` (or a domain CAL) as an **equivalence map** `E` applied **before** folding, yielding a new typed basis **E(basis)**. Absent such declaration, vectors remain multi‑dimensional and are added component‑wise.

**6.5 Availability gates (weakest‑link discipline)**
Many runs require **critical** inputs (a subset **Q\*** of the basis) to be present at or above a threshold. Let `Avail_B(q*)` be the measurable availability for `q* ∈ Q*` on boundary B during τ. Then feasibility is constrained by:

```
Work_B(q*) ≤ Avail_B(q*),  for all q* ∈ Q*
```

If any inequality is violated, the fold **must fail** or the modeller must declare a **Meta‑Holon Transition (B.2)** that introduces redundancy/substitution as a new structural capability (changing Q\* or the equivalence map). This is WLNK in resource form.

##### 7) Embodiment and dissipation (reporting scheme)

Every Work vector **MAY** be split into two projections, both defined on the **same basis** and the **same boundary/time window**:

* **Embodied\_B(q)** — the part of Work retained **inside** B as *state change* of produced holons (e.g., latent heat stored, material incorporated, committed data).
* **Dissipated\_B(q)** — the part of Work irreversibly exported beyond B (e.g., heat loss, scrap, discarded packets).

By norm:

```
Work_B(q) = Embodied_B(q) + Dissipated_B(q)
```

This split is **informative**, not a second algebra: Γ\_work always folds the **total** Work; the split is attached in the **Boundary Ledger** for transparency.

---

##### 8) Invariants — edge cases and proof sketches

**8.1 IDEM (idempotence)**
If `R` has one resource node, no `consumes/produces/transfers` edges, and ΔStock\_inside(q)=0, then

```
Work_B(q) = 0  (the zero vector)
```

Trivial by definition: no measured delta across B implies zero Work.

**8.2 COMM/LOC (local commutativity / locality)**
Let `R` factor into independent subgraphs `{Rᵢ}` whose boundary partitions `{Bᵢ}` are disjoint and cover **B** (6.1). Since each `Work_Bi` is evaluated with its own meters and time slices (6.2), and vector addition is commutative/associative, any local fold order yields the same `Σ_i Work_Bi`. Hence Γ\_work inherits commutativity/locality **under independence**.
*Note:* If subgraphs share a stock variable, independence fails and the modeller must either (i) refactor boundaries to restore independence, or (ii) model the shared stock explicitly in ΔStock\_inside(q) for the **parent** B.

**8.3 WLNK (weakest‑link)**
Let **Q\*** be the critical input set with availability caps `Avail_B(q*)`. Since the delta definition measures **net** consumption across B (inflow–outflow–Δstock), and no external creation is allowed, each `Work_B(q*)` cannot exceed `Avail_B(q*)`. If the plan suggests more, you have either (a) a measurement error, (b) a missing equivalence declaration in `M_spec`, or (c) a true emergent synergy that must be modelled as **MHT** (new redundancy/substitution capability).

**8.4 MONO (monotonicity)**
Monotonicity is interpreted along three characteristics; in all cases “improvement” never makes the whole **worse** (i.e., never increases required Work nor decreases feasibility):

* **Availability monotonicity:** Increasing `Avail_B(q)` for any non‑critical q leaves `Work_B(q)` unchanged (availability is not auto‑consumed); increasing it for a critical q cannot increase `Work_B(q)` and weakly increases feasibility.
* **Yield monotonicity (η):** For a fixed output target, increasing declared or measured **η** weakly **decreases** the required `Work_B(q)` in the inputs, never increases it.
* **Loss monotonicity:** Decreasing dissipation (better insulation, better compression) weakly **decreases** `Dissipated_B(q)`; total Work cannot go up as a result.

**8.5 Compatibility with Γ\_method**
Let a process be composed by Γ\_method from steps `{S_k}`, each with its own boundary partition `{B_k}` and time slice `{τ_k}`. If independence holds between steps at the resource boundary level (no hidden cross‑leaks), the summed Work

```
Σ_k Work_Bk(q, τ_k)
```

is invariant to any topological sort consistent with Γ\_method’s order (Γ\_method may change *when* costs are incurred; Γ\_work adds *how much* is spent).

**Manager note.** When reviewing a plan, inspect **Γ\_method** (is the order/capability sound?). When reviewing results, inspect **Γ\_work** (do the boundary‑relative deltas and units make sense?). Use **PhaseOf** to align both views over time.

#### 9) Archetypal grounding (System / Episteme)

| Facet                       | **U.System — Assembling a heat‑treated frame**                                                                      | **U.Episteme — Training and publishing a model**                                                                                     |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Boundary**                | The enclosure boundary of the frame workstation; ports for electricity, gas, material in/out.                       | The boundary of the knowledge artefact: data ingress, model artefact egress, compute energy ingress.                                 |
| **Work definition**         | Electricity and fuel inflows minus outflows minus Δstock of materials and thermal content retained in the frame.    | Energy spent (compute) + data‑read deltas; Embodied work includes the stored parameters (as committed bytes) and archived SCRs. |
| **Embodied vs Dissipated**  | Embodied: material incorporated, latent heat retained; Dissipated: heat loss, scrap.                                | Embodied: parameter file written, proof artefacts; Dissipated: energy to heat, discarded intermediate data.                          |
| **Additivity across parts** | Ports on furnace, press, conveyor are `Bᵢ`; total frame‑level Work is Σ over `Bᵢ`.                                  | Data‑read over dataset shards are `Bᵢ`; total training Work adds per‑shard deltas.                                                   |
| **Time slicing**            | Heat → dwell → quench phases are `PhaseOf`; Work adds: Σ over phases.                                               | Epochs are `PhaseOf`; Work adds across epochs.                                                                                       |
| **WLNK**                    | Gas supply cap limits feasible heat cycles (critical input); if redundancy is added (dual supply), model it as MHT. | Storage bandwidth caps data‑read; adding a cache hierarchy is MHT (new structural capability), not “free” efficiency.                |

---

#### 10) Conformance Checklist (complete)

| ID            | Requirement                                                                                                                                     | Purpose                                               |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| **CC‑B1.6.1** | Every Γ\_work result SHALL include a **Boundary Ledger**: boundary, time window, basis, method context, transformer identity.                   | Make Work statements comparable and auditable (A.10). |
| **CC‑B1.6.2** | Resource vectors SHALL be **typed**; no implicit unit conversions. Any equivalence MUST be declared in `M_spec` (or a domain architheory).      | Prevent silent inflation/deflation.                   |
| **CC‑B1.6.3** | Resource stocks SHALL be structured with `PortionOf` and `PhaseOf`; `MemberOf` MUST NOT be used for resource mereology.                         | Align with A.14 and prevent category errors.          |
| **CC‑B1.6.4** | For partitioned boundaries `{Bᵢ}` the fold MUST satisfy partition additivity and document the partition.                                        | Enable cross‑scale roll‑ups.                          |
| **CC‑B1.6.5** | For time slicing `{τⱼ}` the fold MUST satisfy temporal additivity with non‑overlapping slices (Γ\_time‑compatible).                             | Keep history coherent.                                |
| **CC‑B1.6.6** | Critical inputs **Q\*** and their availability caps MUST be explicit; any violation SHALL cause the fold to fail or require an MHT declaration. | Enforce WLNK conservatism.                            |
| **CC‑B1.6.7** | If a shared internal stock exists between sub‑boundaries, it MUST be modelled in ΔStock\_inside(q) at the **parent** boundary level.            | Preserve conservation and COMM/LOC preconditions.     |
| **CC‑B1.6.8** | When `M_spec` declares a yield η, the report SHALL separate **planned** (ex‑ante) and **measured** (ex‑post) Work.                              | Keep planning distinct from accounting (A.15).        |
| **CC‑B1.6.9** | Γ\_work SHALL provide proofs of the invariant quintet under the independence assumptions used, or explicitly state where MHT is required.       | Maintain B.1 guarantees.                              |

---

#### 11) Consequences

**Benefits**

* **Audit‑ready costing:** A single definition of Work makes multi‑scale totals consistent and comparable.
* **Separation of concerns:** Control‑flow (Γ\_method) never contaminates cost accounting (Γ\_work).
* **Cross‑scale reliability:** Partition/time additivity gives predictable roll‑ups from parts and phases.
* **Safety by design:** WLNK gates reveal feasibility limits early; emergence is explicit via MHT.

**Trade‑offs / mitigations**

* **Boundary modelling effort:** Requires explicit ports and stock deltas. *Mitigation:* use A.14 templates for common boundary patterns.
* **Vector heterogeneity:** Mixed units can be hard to read. *Mitigation:* keep vectors typed; add equivalence maps only when justified in `M_spec`.
* **Independence discipline:** Shared stocks complicate additivity. *Mitigation:* elevate stock accounting to the parent boundary per CC‑B1.6.7.

---

#### 12) Rationale (informative)

Γ\_work is a conservative algebra of **spent resources**. It respects physical conservation (mass/energy), supports information‑centric resources without conflation, and keeps the **design‑time** (MethodDescription) separate from **run‑time** (Method) facts (A.15). Additivity over disjoint boundaries and non‑overlapping phases is the minimal set of rules that yields stable cross‑scale accounting while remaining faithful to the universal invariants of B.1. Emergent efficiency (redundancy, substitution) is not “free”: it is made structural via **Meta‑Holon Transition** (B.2), after which the same algebra applies at the new level.

---

#### 13) Relations

* **Builds on:** A.12 **Transformer Principle**; A.14 **Mereology Extension** (PortionOf, PhaseOf); A.15 **Strict Distinction** (MethodDescription / Method / Work).
* **Coordinates with:** B.1.5 **Γ\_method** (order and concurrency), B.1.4 **Γ\_time** (temporal coverage), B.1.2 **Γ\_sys** (system assembly).
* **Triggers:** B.2 **Meta‑Holon Transition (MHT): Recognizing Emergence and Re‑identifying Wholes** when feasibility constraints (WLNK) are beaten by structural redundancy/substitution.
* **Feeds:** B.3 **Trust & Assurance Calculus (F–G–R with Congruence)** (cost‑aware confidence overlays) — informative only, without altering Γ\_work’s conservation semantics.

> **Summary for practitioners.**
> Use **Γ\_method** to say **what happens and in which order**.
> Use **Γ\_work** to say **what it costs across a boundary**.
> Keep boundaries, time windows, units, yields, and transformers explicit.
> When apparent “free gains” appear, declare the structural change (MHT) and apply the same algebra one level up.

