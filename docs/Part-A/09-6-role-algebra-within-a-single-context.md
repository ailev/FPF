## 6 · Role algebra **within a single Context** (meaning relations)

Role algebra relates **role types** inside **one** `U.BoundedContext`. It is **not** mereology.

### 6.1 Specialization (narrower assignment)

* **Notation:** `RoleS ≤ RoleG`
* **Semantics (normative):** For any `U.RoleAssignment` with `role = RoleS` in this Context, the holder **also satisfies** requirements for `RoleG` in this Context.
* **Use:** Stable expertise ladders, privilege inheritance.
* **CC‑ALG‑1.** Engines that check `requiredRoles` **MUST** treat `≤` as admissible substitution.

### 6.2 Incompatibility (conceptual role incompatibility)

* **Notation:** `RoleA ⊥ RoleB`
* **Semantics (normative):** A single holder **MUST NOT** have overlapping `window`s for assignments to both roles in this Context.
* * **CC‑ALG‑2.** Validation **MUST** reject overlapping assignments that violate `⊥`.

### 6.3 Bundles (conjunctive requirement)

* **Notation:** `RoleC := Role1 ⊗ Role2 ⊗ …`
* **Semantics:** `RoleC` is **satisfied iff** the holder has **simultaneous** valid assignments for each conjunct role (in this Context).
* **Use:** “On‑call Incident Commander” = *Engineer ⊗ Communicator ⊗ Decision‑Maker*.
* **CC‑ALG‑3.** Checking `requires: [RoleC]` **MUST** expand to conjunctive checks.

> **Didactic guardrails.**
> Use `≤` for lasting ladders, `⊥` for critical safety/governance, `⊗` for frequent conjunctions. Prefer listing multiple `requiredRoles` on Method steps to avoid ornate lattices.

---
