## 10 · Reasoning Primitives (conceptual judgements; notation‑agnostic)

> Pure **thinking moves**; no APIs, no storage, no governance.

* **(J1) Context expansion.** `⊢ Context ≡ U.BoundedContext`
  *Reading:* wherever “Context” appears in formal prose, it denotes `U.BoundedContext`.

* **(J2) Anchor ban.** `uses("anchor") ⊢ violation(D‑CTX‑2)`
  *Reading:* usage of “anchor” flags a discipline violation.

* **(J3) Sense reference.** `ref(ContextId, LocalLabel) ⊢ SenseCell(ContextId, Local‑Sense)`
  *Reading:* a well‑formed reference identifies a SenseCell.

* **(J4) Narrative frame.** `header("Context") ⊢ replaceWith("Problem Frame")`
  *Reading:* headings “Context” in patterns must become “Problem Frame”.

* **(J5) Domain family.** `label ∈ {workflow,…} ⊢ DomainFamily(label)`
  *Reading:* Domain labels are families, not contexts.

* **(J6) Time tag.** `stance ∈ {design, run} ⊢ TimeScopeTag(stance)`
  *Reading:* time is a tag, not a new context.

---
