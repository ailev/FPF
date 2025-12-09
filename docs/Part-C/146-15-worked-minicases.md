## 15 · Worked mini‑cases (engineer‑manager focus)

> **All names are context‑local; bridges and editions are explicit.**
> We show **(a)** what is measured, **(b)** who acts, **(c)** what is accepted, and **(d)** how evidence flows.

### Case A — Hardware ideation sprint (manufacturing design)

* **Context.** `DesignLab_2026`.
* **Objective.** Reduce fastener count by ≥ 30 % without tooling changes.
* **MethodDescription.** “Morphological matrix ideation v2.”
* **Work.** 1‑day sprint, 6 sessions.
* **Metrics.** `Novelty@context` (encoder: CAD‑graph v1; ReferenceSet: in‑house assemblies), `ConstraintFit` (no‑tooling‑change), `Use‑Value` (acceptance: Pass if sim shows ≤ +5 % assembly time).
* **Roles.** Performers = design cell (#TransformerRole); Observer = methods coach (#ObserverRole ⊥).
* **Outcome.** 22 candidates; 4 **Pass** usefulness; best `Novelty`=0.41 with **100 %** constraints respected; `Time‑to‑First‑Viable` = 3 h 40 m.
* **Evidence.** Scorecard episteme holds metrics; links to Work ids; acceptance tied to internal **Service** “Design‑for‑Assembly Simulation”.

**Manager’s read.** “We didn’t just produce ‘novel’ shapes; 4 passed the sim and respected constraints, within the day.”

---

### Case B — Data‑science hypothesis generation (health analytics)

* **Context.** `Cardio_2026`.
* **Objective.** Find a new risk factor candidate for readmission (< 30 days).
* **MethodDescription.** “Causal discovery v3 + clinician review.”
* **Metrics.** `DiversityOfSearch` (approach classes: feature ablation, IVs, DAG‑learners), `Novelty@context` (text encoder over prior hypotheses), `Use‑Value` (AUROC uplift ≥ 0.03 on hold‑out), `Transferability@Hospital_B` (Bridge CL=2).
* **Roles.** SRE pipeline (#ObserverRole) computes metrics; clinicians (#ReviewerRole) set acceptance; data squad (#TransformerRole) performs experiments.
* **Outcome.** Two candidates; one meets AUROC uplift; **Transferability** requires follow‑up (CL penalty).
* **Evidence.** Episteme bundle: model cards, hold‑out plots, Bridge note.

**Manager’s read.** “One candidate works **here**; plan a pilot at Hospital B (we recorded CL=2).”

---

### Case C — Product squad reframing (software UX)

* **Context.** `SaaS_Onboarding_2026`.
* **Objective.** Reduce time‑to‑value (TTV) by 20 %.
* **MethodDescription.** “JTBD interviews + onboarding flow experiments.”
* **Metrics.** `ReframeDelta` (BoundaryShift: split onboarding into ‘job setup’ and ‘first result’), `Use‑Value` (TTV ‑22 % on A/B), `Risk‑BudgetedExperimentation` (within cap), `Compositionality` (reuse of existing workflow widgets).
* **Roles.** UX researcher (#ObserverRole), squad (#TransformerRole), product ops (#ReviewerRole).
* **Outcome.** Frame changed; TTV target passed; experiments within budget.
* **Evidence.** Reframing episteme with Scope diff + A/B report.

**Manager’s read.** “We changed the problem frame and proved the value drop—within risk limits.”

---

### What these cases illustrate (tie‑backs)

* **Locality.** All novelty/usefulness claims are **Context‑tagged**; Cross‑context steps use **Bridges** with **CL**.
* **Dual‑gate.** Novelty never acts alone; usefulness/constraints co‑gate decisions.
* **SoD & Evidence.** Observers are **separate** from performers; metrics live on **epistemes** with **frozen hooks**; Work proves fulfillment.

