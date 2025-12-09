## 12.4 · Metric templates (normative kernels + manager‑ready variants)

 **Template syntax (MM‑CHR):**
`U.DHCMethod { name, context, carrierKind, definition, unit?, scale, EvidencePin, acceptanceHook? }`
*Note:* Data instances carry `DHCMethodRef` pointing to this template.

### 12.4.1 · Templates (kernel definitions)

1. **`MT.Novelty@context`**

* **carrierKind:** Artifact|WorkOutput.
* **definition:** `1 − max_sim(encode(x), encode(y))` over y in **ReferenceSet**@Context.
* **scale:** ratio \[0..1].
* **EvidencePin:** `{ReferenceSetId, EncoderId, Version}`; frozen by `A.10`.
* **notes:** Publish encoder & corpus drift in RSCR.

2. **`MT.Use‑Value`**

* **carrierKind:** Work (fulfillment) → artifact (decision memo).
* **definition:** Evaluation of an outcome against a declared **objective/criterion** for the current context (or predicted value with explicit model & error).
* **scale:** ordinal {Fail, Partial, Pass} or scalar KPI.
* **EvidencePin:** links to `U.Work` that **fulfilsService\`**; cite acceptanceSpec edition.

3. **`MT.ConstraintFit`**

* **carrierKind:** Work / Artifact.
* **definition:** `|{c∈C_must : pass(c)}| / |C_must|` within the **MethodDescription** scope; optional weighting by criticality allowed if declared.
* **scale:** ratio \[0..1].
* **EvidencePin:** constraint list from **Norm‑CAL**; checks from Work telemetry.

4. **`MT.ReframeDelta`**

* **carrierKind:** Episteme pair (ProblemStatement v0→v1).
* **definition:** Categorise frame change as {None, Local, BoundaryShift, Systemic}; **justify** with a Scope diff (`A.2.6 U.ContextSlice` delta) and causal map simplification.
* **scale:** ordinal 0–3.
* **EvidencePin:** diff artifact + Bridge notes if Cross‑context.

5. **`MT.DiversityOfSearch`**

* **carrierKind:** Work set (episode).
* **definition:** Count of **distinct approach classes** tried (domain‑local typology) / time.
* **scale:** count; derived rate.
* **EvidencePin:** tagged Work items; typology lives in the Context glossary.

6. **`MT.Compositionality`**

* **carrierKind:** Artifact.
* **definition:** set aggregator (Compose‑CAL) of reused components ≥ K and presence of novel relation among ≥ 2 parts.
* **scale:** boolean + secondary “structure score” (e.g., depth or edge novelty).
* **EvidencePin:** component graph + provenance of parts.

7. **`MT.Transferability@X`**

* **carrierKind:** Artifact.
* **definition:** Applicability in target **Context X** via a **Bridge**; report **CL** and residual scope slice.
* **scale:** ordinal {not portable, portable with loss, near‑iso}; record CL (0–3).
* **EvidencePin:** Bridge id + pilot Work in X.

8. **`MT.Time‑to‑First‑Viable`**

* **carrierKind:** Work episode.
* **definition:** elapsed wall‑clock to first `UsefulnessEvidence = Pass`.
* **scale:** duration.
* **EvidencePin:** first passing `U.Work` id.

9. **`MT.Risk‑BudgetedExperimentation`**

* **carrierKind:** WorkPlan vs Work.
* **definition:** `(Planned exploratory spend) / (Allowed risk budget)` and realised counterpart; flag **overrun**.
* **scale:** ratio + policy gate (pass/fail).
* **EvidencePin:** WorkPlan ledger vs `WorkLedger`.

### 12.4.2 · Manager’s quick checks (plain‑language adapters)

* **Novelty** without a **frozen corpus** is **storytelling**—freeze corpus, fix encoder, then score.
* **Use‑Value** without a **consumer‑facing acceptance** is a **proxy**—bind to a **Service** or explicit Objective.
* **Diversity** counts **approach classes**, not color‑swap variants—publish your typology.
