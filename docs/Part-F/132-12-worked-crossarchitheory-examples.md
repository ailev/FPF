## 12 · Worked cross‑architheory examples (didactic)

### 12.1 Service acceptance (design) vs executions & observations (run)

* **Cells & Contexts**
  `ITIL4:SLO` *(Status, design)* ← **→ᴍᴇᵃ** — `SOSA:Observation(availability)` *(Measurement, run)*
  `BPMN:Process` *(Method, design)* ⇄ᴅʀ — `IEC61131:Task‑Execution` *(Execution, run)*
* **Narrative**
  Availability SLOs are **evaluated** by observations of task executions. No substitution: SLO ≠ observation; process ≠ execution.
* **Bridge Cards (sketch)**
  *ITIL\:SLO ←→ᴍᴇᵃ SOSA\:Observation* • **CL=2** • Loss: sampling window, clock skew.
  *BPMN\:Process ⇄ᴅʀ IEC\:Execution* • **CL=2** • Loss: control‑flow vs temporalization, concurrency collapse.
* **Permitted use**
  Explanation‑only; Concept‑Set rows may be **Naming‑only** (“availability”) with **CL≥1** label coherence across Contexts.

---

### 12.2 Behavioural role vs access role

* **Cells & Contexts**
  `BPMN:Participant` *(Role)* ⋂ `NIST‑RBAC:Role` *(Status)*
* **Narrative**
  Both talk about “who acts”, but one is **behavioural mask** in a workflow, the other **permission grouping**.
* **Bridge**
  **Kind:** overlap (⋂), **CL=2**; Loss: assignment moment, enforcement locus, multiplicity.
* **Permitted use**
* **Naming-only** row “actor”; **no Role Assignment & Enactment reuse** across senseFamilies.

---

### 12.3 Equivalence of subtype notions for structural rows

* **Cells & Contexts**
  `OWL2:SubClassOf` *(Type‑structure)* ≈ `TaxX:is‑a` *(Type‑structure curated)*
* **Bridge**
  **Kind:** ≈, **CL=3** **iff** curated taxonomy is **acyclic & anti‑symmetric** and uses class‑level reasoning.
* **Permitted use**
  **Type‑structure** rows allowed (τᵗʏᴘᴇ); Loss: OWL profile limitations (RL/EL/QO).

---

### 12.4 Accuracy (metrology) vs accuracy (data‑quality)

* **Cells & Contexts**
  `ISO80000:measurement‑accuracy` *(Measurement)* ⋂ `ISO25024:data‑accuracy` *(Measurement)*
* **Bridge**
  **Kind:** overlap, **CL=2**; Loss: “true value” notion differs (instrument vs dataset), scale transformations.
* **Permitted use**
  **Naming‑only** row “accuracy” used for reports; no shared methods.

---

### 12.5 Setpoint (control) vs target (service)

* **Cells & Contexts**
  `CTRL:text:setpoint` *(Status/Control)* ⊥ `ITIL:target` *(Status/Service)*
* **Bridge**
  **Kind:** disjoint (⊥) • Rationale: physical reference value vs business objective; different target kinds (control parameters vs requirement clause).
* **Permitted use**
  Didactic contrast only; prevents accidental substitution in SLO calculus.

---
