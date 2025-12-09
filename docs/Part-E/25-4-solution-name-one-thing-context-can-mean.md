## 4 · Solution — **Name one thing “Context” can mean**

**D‑CTX‑1 (Canonical meaning).** In all FPF materials, **Context** denotes the formal primitive **`U.BoundedContext`** only. The short form **Context** is permitted in the *Tech* register strictly as an alias of `U.BoundedContext`.

**D‑CTX‑2 (Remove “anchor”).** The term **anchor** is **prohibited**. When you need “the place where a meaning lives”, use:

* **`SenseCell := (U.BoundedContext, Local‑Sense)`** — the *cell of meaning* inside a specific Context; or
* a **`ConceptSet.Row`** + column reference (see E.10.U7).

**D‑CTX‑3 (Domain is informative).** **Domain** (workflow, provenance, services, access, sensing, …) is **not** a U.Type. It is an **informative family label** grouping several `U.BoundedContext`s. There is no “domain context”.

**D‑CTX‑4 (Narrative is Problem Frame).** Use **Problem Frame** (or **Frame**) for situational narrative in patterns. Do **not** use “context” for narrative sections.

**D‑CTX‑5 (Time is a tag, not a context).** `design` / `run` are **TimeScope tags** (C‑7) on artefacts or sources; they do **not** create separate contexts.

**D‑CTX‑6 (No context inheritance).** `U.BoundedContext`s have **no is‑a** or containment relations. Any cross‑context relationship appears **only** via E.10.U9 *Alignment/Bridge* with explicit loss policies.

**D‑CTX‑7 (Language/edition discipline).** Different languages or editions may be **distinct `U.BoundedContext`s** when meaning or usage can diverge. Where an official source binds multilingual labels to the **same** semantics, record them as **labels** of the **same** Context.

**D‑CTX‑8 (Reference forms).** Use **one of the following** when pointing to meaning:

* **`ContextId:LocalLabel`** (e.g., `BPMN_2_0:process`), or
* **`SenseCell(ContextId, Local‑SenseId)`**, or
* **ConceptSet(RowId).Column(ContextId)** (E.10.U7).

---
