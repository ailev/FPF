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
