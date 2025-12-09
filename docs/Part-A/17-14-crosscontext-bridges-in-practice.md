## 14 · Cross‑Context bridges in practice (with CL penalties)

> **Rule.** **No Cross‑context substitution by name.** If a step in **Context A** needs `Role_A`, and the performer only holds `Role_B` in **Context B**, you must use an explicit **Bridge** (F.9) that says how `Role_B@B` relates to `Role_A@A`, with a **Congruence Level (CL)** and **loss notes**.

### 14.1 Directional substitution

A Bridge may assert, *directionally*:

* **`substitutesFor(Role_B@B → Role_A@A)`** with a CL and a list of **kept** and **lost** RCS characteristics / RSG nuances.
* The reverse direction **does not** follow unless declared.

### 14.2 CL → gating policy (normative thresholds)

| **CL** | Meaning (intuitive)                     | **Permit** | **Guard**                                                                            | **Block** |
| :----: | --------------------------------------- | :--------: | ------------------------------------------------------------------------------------ | :-------: |
|  **3** | Near‑isomorphic sense; no material loss |     Yes    | None beyond ordinary RSG/Window gates                                                |     —     |
|  **2** | Close but with stated losses            |     Yes    | Require **extra evidence** (e.g., additional checklist item) **or** a named reviewer |     —     |
|  **1** | Distant analogy; risky                  |  Exception | Only by explicit **Waiver SpeechAct** naming the Bridge + loss rationale             |  Default  |
|  **0** | Incompatible                            |     No     | —                                                                                    |    Yes    |

*Normative hooks.* The **Trust & Assurance Calculus (B.3)** aggregates CL penalties into confidence scores; **D.2** may mandate CL≥2 for safety‑critical enactments.

### 14.3 Typical bridges (worked patterns)

* **BPMN Task ↔ PROV Activity.**
  `substitutesFor(Task@BPMN → Activity@PROV)` with **CL=2**; **lost:** BPMN control‑flow guards; **kept:** “bounded occurrence consuming/producing entities.”
  *Effect.* A Work logged as `Activity@PROV` may satisfy a step requiring a `Task@BPMN` **if** an extra guard enforces the BPMN pre‑/post‑conditions.

* **Essence Alpha‑State ↔ RoleStateGraph state.**
  `substitutesFor(“Alpha.State:Ready”@Essence → “Ready”@RSG)` with **CL=2**; **lost:** Alpha‑specific narrative criteria; **kept:** checklist‑based readiness.
  *Effect.* A team may reuse Essence states as labels in RSG, but still maintains local checklists as **StateAssertions**.

* **ITIL Service Owner ↔ RBAC Administrator.**
  Typically **CL=1** and **directional** (Administrator\@RBAC → ServiceOwner\@ITIL) **rejected** unless a policy Bridge enumerates compensating controls.
  *Effect.* Prevents “ops admin = service owner” conflations without an explicit waiver.

### 14.4 Bridge invariants

* **Local first.** Substitution never overrides in‑Context `⊥`, `⊗`, or `≤`.
* **Evidence trail.** Every Cross‑context enactment relying on a Bridge **shall** reference its Bridge id in the `U.Work` justification.
* **Loss visibility.** The Bridge **must** state which **RCS characteristics** are preserved vs dropped; if a dropped characteristic is required by the step, substitution is **invalid**, regardless of CL.

---
