## **B.1.5 Γ\_method — Order‑Sensitive Method Composition & Instantiation** \[D]
+> **► decided‑by: A.14 Advanced Mereology**
+**A.14 compliance —** Methods compose over **SerialStepOf/ParallelFactorOf** on **MethodDescription/Method** graphs (order, not parthood); stuff‑like inputs are modelled via **PortionOf** on resources and accounted in **Γ_work**; method/version history uses **PhaseOf**; mapping quality is handled via **CL** (B.3).
 
> **Plain‑English headline.**
> **Γ\_method** turns **ordered step‑methods** into a **single composite Method** (run‑time) and, dually, turns **ordered step specifications** into a **single MethodDescription** (design‑time). It reuses **Γ\_ctx** for order, keeps **work/cost in Γ\_work**, and makes **pre/post‑conditions and capability typing** explicit so models stay physically and logically sound.

### 1) Problem frame

* **Strict Distinction (A.15)** separates **what a holon is** (structure), **how steps are ordered** (order), **how it unfolds** (time), **what it spends** (work/resources), and **what it values** (objectives).
* **Method vs MethodDescription.**

  * **Method** is the **run‑time enactment** (a holon‑in‑role executing a concrete sequence of transformations).
  * **MethodDescription** is the **design‑time description** of that sequence (steps, order, pre/post‑conditions, required capabilities).
    Calling the sequence a “process” is common in some domains, but in FPF we use **Method/MethodDescription** to avoid conflating behaviour with work.
* **A.15 (Role–Method–Work Alignment)** supplies the **typed ordered relations** we need: **SerialStepOf** (strict precedence) and **ParallelFactorOf** (order‑concurrent branches with a join).
* **B.1.4 (Γ\_ctx/Γ\_time)** already handles **non‑commutativity** (order matters) and **temporal slicing**; **B.1.6 (Γ\_work)** handles **resource spending** and **efficiency**.
  **Γ\_method** sits **between** them: it composes methods **by order and capability** and **delegates** resource accounting to **Γ\_work**.

### 2) Problem

Without a dedicated, order‑aware method operator:

1. **Design/run conflation.** Authors mix **MethodDescription** (blueprint) and **Method** (enactment), producing “methods” that have both planned and executed attributes.
2. **Order erasure.** Sequences with crucial **pre/post‑conditions** get collapsed into sets; reordering breaks correctness while still “passing” naive aggregation.
3. **Capability mismatches.** Step outputs do not match the next step’s required inputs, but this is hidden in untyped edges; composite methods become non‑executable.
4. **Work leakage.** Costs and resource flows are **inlined** into method definitions; later models double‑count or violate conservation (Γ\_work was created to prevent this).
5. **Synergy by arithmetic.** Throughput or quality jumps caused by **proper joins** or **coordination** are misreported as simple sums or averages—violating WLNK and obscuring when a **Meta‑Holon Transition (B.2)** should be declared.

### 3) Forces

| Force                                    | Tension                                                                                                 |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Order fidelity vs. simplicity**        | Keep the **true sequence** (non‑commutative) ↔ Provide a **small** operator set.                        |
| **Type safety vs. flexibility**          | Enforce **capability typing** and **pre/post** checks ↔ Allow modular reuse of steps across contexts.   |
| **Design vs. run**                       | Compose **MethodDescription** for planning ↔ Instantiate **Method** for execution without mixing them.         |
| **Parallelism vs. correctness**          | Maximise concurrency on **independent branches** ↔ Guarantee **sound joins** and reproducible outcomes. |
| **Parsimony vs. separation of concerns** | Keep Γ small ↔ Keep **work** and **assurance** in their own lanes (Γ\_work, B.3).                       |

### 4) Solution

#### 4.1 Terms (didactic recap)

* **U.MethodDescription** — a design‑time description: ordered steps, **SerialStepOf/ParallelFactorOf**, step **capability types**, **pre/post‑conditions**, and required **external interactions**.
* **U.Method** — a run‑time enactment by a **U.TransformerRole** (A.12): the same ordered pattern realised on concrete carriers, satisfying step pre‑conditions and producing post‑conditions.
* **U.StepSpec / U.StepMethod** — step‑level counterparts of the above.
* **Capability type** — the **state/action signature** a step requires and produces (not to be confused with resources; those belong to Γ\_work).
* **Method Interface Standard (MIC)** — the **order‑aware** analogue of BIC: a short, declarative statement of what **external interactions** of the steps are **Promoted / Forwarded / Encapsulated** at the composite method boundary.

> **Separation reminder.**
> Method composition ≠ resource spending. Keep **resource budgets, yields, dissipation** in **Γ\_work**; **Γ\_method** only checks and composes **order and capability**.

---

#### 4.2 The operator family (two companion flavours)

To respect the design/run split, **Γ\_method** is presented as two companion operators sharing the same semantics but acting at different scopes.

1. **Planning (design‑time) — compose specifications**

   ```
   Γ_method^plan : ( D_spec : OrderedDependencyGraph< U.StepSpec >,
                     σ       : OrderSpec,
                     MIC_in  : optional boundary hints )
                   → U.MethodDescription
   ```

   * **Domain.** `D_spec` contains step specifications linked by **SerialStepOf** / **ParallelFactorOf** (**A.15**).
   * **Result.** A single **U.MethodDescription** whose **MIC** is computed from step interfaces using the **Promote / Forward / Encapsulate** quartet (cf. BIC in B.1.2).

2. **Enactment (run‑time) — instantiate methods**

   ```
   Γ_method^run  : ( M_spec : U.MethodDescription,
                     T      : U.TransformerRole,
                     Bind   : carrier & parameter bindings )
                   → U.Method
   ```

   * **Domain.** A previously composed **MethodDescription**, a **Transformer** that plays the method, and concrete **bindings** (carriers, parameters).
   * **Result.** A **U.Method** (the real execution) provided that **capability checks** and **pre/post‑conditions** hold.

**Relationship to Γ\_ctx.**
Both flavours **reuse Γ\_ctx** invariants for order (non‑commutative composition with **NC‑1..3** reproducibility). **Γ\_method** specialises the **typing and boundary rules** for methods and introduces **MIC**.

---

#### 4.3 Core aggregation rules (design‑time composition)

When computing **Γ\_method^plan(D\_spec, σ)**:

1. **Order preservation.**
   Respect the **OrderSpec σ**; independent branches may be folded in any **topological sort** (Γ\_ctx NC‑3). **SerialStepOf** enforces strict precedence; **ParallelFactorOf** allows concurrency with a **join**.

2. **Capability continuity (typed joins).**
   Every join must be **type‑sound**: the **post‑condition / output signature** of each incoming branch must **meet** the next step’s **pre‑conditions** (logical entailment or declared **adapter** steps). Missing adapters are **defects**, not assumptions.

3. **MIC synthesis (boundary behaviour).**
   For each external interaction of a step, decide **Promote / Forward / Encapsulate** into the composite **MIC**. This inherits the clarity of BIC (B.1.2) for methods.

   * *Promote*: becomes a direct composite interaction (e.g., top‑level “start/stop”).
   * *Forward*: remains step‑local but exposed under the composite boundary (namespaced).
   * *Encapsulate*: becomes internal; callers cannot rely on it.

4. **Assurance hooks (without computing assurance).**
   Record where **B.3 assurance** will later hang: (i) the **cutset** steps that bound reliability/quality, (ii) the **integration edges** whose **CL** will penalise poor fit (mappings, fragile joins), and (iii) the **envelope** (G) intended for the method’s validity.

5. **No costs here.**
   If a step lists resources/yields, **do not** aggregate them here. Instead, add a pointer to the corresponding **Γ\_work** composition to be executed with the same order/joins at run‑time.

---

#### 4.4 Core aggregation rules (run‑time instantiation)

When executing **Γ\_method^run(M\_spec, T, Bind)**:

1. **Pre/post enforcement.**
   Before each step, verify **pre‑conditions** against **Bind** and the evolving carrier state; after, check **post‑conditions** hold. Failing these means the **Method** cannot be enacted as specified.

2. **Typed state flow.**
   The **state/action types** produced by a step must make the next step **well‑typed**; if not, an **adapter method** (itself with a MethodDescription) must be present in the graph.

3. **Order determinism (Γ\_ctx).**
   Respect `σ`. Parallel branches may execute independently **only if** they share no state that would break **NC‑1..3**; otherwise they must synchronise at the declared join.

4. **MIC honouring.**
   Interactions exposed by **MIC** are the **only** external commitments the composite method makes. Any additional ad‑hoc external interaction is a **model violation** (or requires updating the MIC and re‑planning).

5. **Γ\_work hand‑off.**
   Invoke **Γ\_work** to compute **spent resources, yields, dissipation** along the same order/join structure. The resulting work products **annotate** the Method but are **not** part of Γ\_method’s aggregation.

> **Invariant intuition.**
>
> * **IDEM:** a single step‑method composed alone yields the same method.
> * **COMM/LOC:** replaced by Γ\_ctx **NC‑1..3** (determinism given `σ`, context hash of `σ`, and partial‑order soundness).
> * **WLNK:** quality/throughput of the composite is bounded by the **critical path** steps (identified for later B.3 assurance).
> * **MONO:** strengthening a step (better pre/post, stronger type, improved adapter) **cannot** make the composite worse.

---

#### 4.5 Didactic contrasts (to prevent common confusions)

* **Method vs Work.**
  Method = **what** ordered transformations are enacted; **Work** = **resources spent / yields / dissipation** when enacting them (Γ\_work). Keep them distinct.

* **Method vs Structure.**
  Method composes **ordered steps**; structure composes **parts** (Γ\_sys). Do not use **ComponentOf** where **SerialStepOf/ParallelFactorOf** are intended.

* **Method vs Phase.**
  Method composition is **order**; **PhaseOf** (Γ\_time) is **temporal progression** of the **same carrier**. If a phase boundary also introduces **closure/supervision/context rebase**, that is **MHT** (B.2), not mere phasing.

* **MethodDescription vs Method.**
  Keep **planning** artefacts (MethodDescription) separate from **enactment** (Method). Γ\_method provides operators for both but never fuses them.

### 5) Archetypal grounding (worked, didactic)

#### 5.1 System archetype — **Assemble‑Paint‑Test** as one Method

* **Design‑time (Γ\_method^plan).**
  `D_spec` contains `StepSpec`s: `AssembleChassis`, `InstallPowertrain`, `PaintBody`, `RunFunctionalTest`.
  Relations: `AssembleChassis → InstallPowertrain` (**SerialStepOf**), `PaintBody ∥ RunFunctionalTest` after a structural seal (**ParallelFactorOf**).
  Capability typing:

  * Output of `InstallPowertrain` **meets** input of `RunFunctionalTest` (functional harness attached).
  * `PaintBody` requires sealed surfaces from `InstallPowertrain` (pre‑condition).
    MIC outcome:
  * **Promote:** `Start()`, `Abort()`, `CertificationReport`.
  * **Forward:** `RunFunctionalTest.Diagnostics` (namespaced).
  * **Encapsulate:** `PrimerMixingPort`, internal seal checks.

* **Run‑time (Γ\_method^run).**
  `T` enacts the `MethodDescription` on concrete carriers. Pre/post checks gate each step; parallel branches run after pre‑conditions met; a join waits for both to finish.

* **Assurance hooks (B.3).**
  Cutset steps for WLNK: `InstallPowertrain` (torque tolerances) and `RunFunctionalTest` pass/fail; integration edges carry **CL** for harness mapping and paint/seal specification.
  **Γ\_work** is invoked to compute energy/material spend and dissipation; Γ\_method does not tally costs itself.

#### 5.2 Episteme archetype — **Evidence‑Synthesis‑Publish** as one Method

* **Design‑time (Γ\_method^plan).**
  Steps: `CollectDatasets`, `NormalizeSchemas`, `EstimateModel`, `CrossValidate`, `DraftManuscript`.
  Ordering: `CollectDatasets → NormalizeSchemas → EstimateModel → CrossValidate → DraftManuscript`.
  Capability typing: `NormalizeSchemas` outputs a typed feature space that **entails** `EstimateModel`’s input; adapters specified for legacy datasets.
  MIC outcome:

  * **Promote:** `Submit()`, `ReleaseArtifacts()`.
  * **Forward:** `CrossValidate.Folds(k)`.
  * **Encapsulate:** ad‑hoc scrubbing utilities.

* **Run‑time (Γ\_method^run).**
  The same order executes; **Γ\_work** accounts for compute/storage spend.
  Assurance hooks: cutset at `CrossValidate`; integration **CL** for schema mappings; post‑condition for `DraftManuscript` includes provenance SCR.

---

### 6) Method Interface Standard (MIC) — template & examples

#### 6.1 MIC template (normative content)

```
Method Interface Standard (MIC)
  name:                human-readable identifier
  version:             semantic label of this MIC
  orderSpecHash:       hash(OrderSpec σ + step signatures)
  externalInteractions:
    - id:              external op name
      mode:            {Promote | Forward | Encapsulate}
      signature:       state/action types (typed interface)
      preconditions:   predicates that must hold at call
      postconditions:  predicates guaranteed on return
      qosEnvelope:     optional envelope (throughput, latency, quality)
  invariants:
    - textual/logical invariants preserved by the method
  notes:
    - rationale for Promote/Forward/Encapsulate choices
```

#### 6.2 MIC excerpts (didactic)

* **Manufacturing method MIC excerpt**

  ```
  externalInteractions:
    - id: Start
      mode: Promote
      signature: Start(): Promise<BatchId>
      preconditions: LineReady & MaterialsAvailable
      postconditions: BatchId issued
    - id: PrimerMixingPort
      mode: Encapsulate
  invariants:
    - FunctionalTest.Pass implies TorqueTolerance ≤ δ
  ```

* **Evidence method MIC excerpt**

  ```
  externalInteractions:
    - id: Submit
      mode: Promote
      signature: Submit(): Promise<SubmissionId>
      preconditions: ManuscriptReady & SCRComplete
      postconditions: DOI assigned on accept
    - id: CrossValidate.Folds
      mode: Forward
      signature: Folds(k: Int): Report
  invariants:
    - Report.metrics computed on held-out data only
  ```

---

### 7) Proof obligations (normative)

**At planning time (Γ\_method^plan):**

1. **PO‑PLAN‑ORDER.** Provide `OrderSpec σ`; produce `orderSpecHash`.
2. **PO‑PLAN‑TYPE.** For every edge, show **capability continuity**: `OutType(step_i) ⊢ InType(step_j)` or provide a typed **adapter StepSpec**.
3. **PO‑PLAN‑MIC.** For each step interaction, decide **Promote/Forward/Encapsulate** and justify in MIC.
4. **PO‑PLAN‑CL‑POINTS.** Identify integration edges whose **CL** will matter for B.3; record intended sources of mapping evidence.
5. **PO‑PLAN‑NO‑WORK.** Confirm that costs/resources are **not** aggregated here; point to the planned **Γ\_work** composition (by reference).

**At run time (Γ\_method^run):**

1. **PO‑RUN‑PRE/POST.** Demonstrate that pre‑conditions hold before each step; check post‑conditions after.
2. **PO‑RUN‑NC.** Show compliance with Γ\_ctx **NC‑1..3** (determinism with σ, context hash, partial‑order soundness).
3. **PO‑RUN‑MIC‑HONOUR.** Record that only MIC‑declared external interactions occurred.
4. **PO‑RUN‑WORK.** Attach the **Γ\_work** result (spent resources, yields, dissipation) aligned with the same order/join structure.
5. **PO‑RUN‑ASSURANCE.** Provide the observed values for the cutset steps and the actual **CL** of integration mappings to feed B.3 assurance.

---

### 8) Conformance Checklist (normative)

| ID            | Requirement                                                                                                                                                   | Purpose                             |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **CC‑B1.5.1** | Γ\_method **SHALL** be used in two flavours only: `Γ_method^plan` for specifications, `Γ_method^run` for enactments.                                          | Enforce design/run separation.      |
| **CC‑B1.5.2** | Planning inputs **SHALL** use **SerialStepOf / ParallelFactorOf** edges with a declared **OrderSpec σ**.                                                      | Preserve order semantics.           |
| **CC‑B1.5.3** | All joins **SHALL** be **type‑sound** (capability continuity) or include explicit typed adapters.                                                             | Prevent non‑executable composites.  |
| **CC‑B1.5.4** | A **MIC** **SHALL** be produced for `Γ_method^plan` and **SHALL** be honoured by `Γ_method^run`.                                                              | Make external commitments explicit. |
| **CC‑B1.5.5** | Resource spending/yields **SHALL** be computed via **Γ\_work** and MUST NOT be inlined into Γ\_method aggregation.                                            | Maintain separation of concerns.    |
| **CC‑B1.5.6** | Γ\_ctx **NC‑1..3** invariants **SHALL** hold for both flavours (determinism under σ, hash, partial‑order soundness).                                          | Guard non‑commutative correctness.  |
| **CC‑B1.5.7** | If joining branches produces apparent super‑additivity beyond WLNK not explainable within Γ\_method, an **MHT** **SHALL** be considered and recorded per B.2. | Prevent “synergy by arithmetic”.    |

---

### 9) Anti‑patterns & repairs

| Anti‑pattern           | Symptom                                                       | Repair                                                                             |
| ---------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| **Design/Run Chimera** | Spec contains runtime measures; enactment adds planning edges | Split into `MethodDescription` vs `Method`; rerun Γ\_method per flavour.                  |
| **Orderless Set**      | Steps modelled as unordered; reordering breaks correctness    | Provide `OrderSpec σ` and recompose with Γ\_method/Γ\_ctx.                         |
| **Silent Adapter**     | A join assumes implicit conversion                            | Add explicit typed **adapter StepSpec/Method** and re‑prove capability continuity. |
| **Inline Costs**       | Method sums time/energy                                       | Move to **Γ\_work**; link the work composition to the same order.                  |
| **Boundary Fog**       | External calls occur ad‑hoc                                   | Define/Update **MIC**; Promote/Forward/Encapsulate explicitly.                     |
| **Emergence by Join**  | Throughput leaps past WLNK with no story                      | Either (i) prove within Γ\_method (cutset/CL/order) or (ii) declare **MHT** (B.2). |

---

### 10) Consequences

**Benefits**

* **Didactic clarity.** Readers see **what** is being composed (order & capability) vs **what** is spent (Γ\_work) vs **what** is assured (B.3).
* **Deterministic execution semantics.** Γ\_ctx‑backed order with explicit joins yields reproducible composites.
* **Robust interfaces.** MIC prevents accidental external dependencies and preserves modularity.
* **Cross‑scale fit.** Same pattern works for physical, organizational, and epistemic methods.

**Trade‑offs**

* **More explicitness up‑front.** Capability typing and MIC authorship require care; in return, later integration is safer.
* **Adapter discipline.** Modellers must create adapters rather than assuming conversions—this avoids hidden brittleness.

---

### 11) Rationale (informative)

* **Order is semantic.** Many failures stem from pretending that order does not matter; Γ\_method makes **non‑commutativity** explicit (via Γ\_ctx) while keeping the operator set small.
* **Strict Distinction.** The split between **Method/MethodDescription**, **Γ\_method/Γ\_work**, and **assurance** implements A.15, preventing category errors (behaviour vs spending vs claims).
* **Mereology alignment.** Using **SerialStepOf / ParallelFactorOf** (A.14) keeps method composition orthogonal to structural composition (**ComponentOf**) and temporal phasing (**PhaseOf**).
* **Assurance readiness.** Identifying cutsets and mapping CL points during planning makes B.3 application straightforward and auditable.

---

### 12) Relations

* **Builds on:** A.12 (Transformer Role), A.14 (Mereology Extension), A.15 (Strict Distinction); B.1.1 (Proof Kit), B.1.4 (Γ\_ctx/Γ\_time).
* **Coordinates with:** B.1.6 (Γ\_work) for resource accounting; B.3 (Assurance) for WLNK cutsets and CL penalties.
* **Triggers/Complements:** B.2 (MHT) when new closure/supervision or context re‑base appears at method level.
* **Used by:** Later domain architheories that define canonical methods in specific disciplines (without altering Γ\_method).

> **One‑sentence takeaway.**
> **Γ\_method** composes **ordered, typed steps** into a reliable method, keeps **interfaces explicit** (MIC), leaves **costs to Γ\_work**, and provides clean hooks for **assurance** and **emergence**.


