## 12 · Migration Notes (conceptual playbook)

1. **Rename headings.** Replace any “Context” section title with **Problem Frame**.
2. **Delete “anchor”.** Replace with **SenseCell** or **Concept‑Set** references.
3. **Split domain vs context.** Where “domain context” appears, rewrite as **Domain family** + explicit list of `U.BoundedContext`s.
4. **Audit references.** Ensure every semantic reference is `ContextId:LocalLabel` or `SenseCell(ContextId, …)` or Concept‑Set column.
5. **Flatten contexts.** Remove any inheritance among contexts; move relations to **E.10.U9**.
6. **Tag time.** Replace “design/runtime context” with **TimeScope tags**.
7. **Language/edition pass.** Split or merge Contexts per **D‑CTX‑7**; document rationale.

---
