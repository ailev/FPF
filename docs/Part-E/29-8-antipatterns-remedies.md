## 8 · Anti‑patterns & Remedies

| Anti‑pattern                  | Symptom                                                           | Why harmful                          | Remedy (normative)                                                           |
| ----------------------------- | ----------------------------------------------------------------- | ------------------------------------ | ---------------------------------------------------------------------------- |
| **A1 Context-as-situation**   | “Context” used for narrative sections                             | Ambiguity                            | Use **Problem Frame**; reserve Context for `U.BoundedContext` (D‑CTX‑4).     |
| **A2 Anchor-speak**           | “role anchor”, “ontology anchor”                                   | Redundant token; hides locality      | Replace with **SenseCell** or **ConceptSet(Row).Column** (D-CTX-2, D-CTX-8). |
| **A3 Domain context**         | “Workflow domain context”, etc.                                   | Family ≠ formal context              | Use **Domain family** + explicit list of Context ids (D‑CTX‑3).              |
| **A4 Context hierarchy**      | Context A “is‑a” Context B                                        | Leaks meanings; blocks loss policies | Remove hierarchy; use **E.10.U9 Bridge** with loss policy (D‑CTX‑6).         |
| **A5 Time‑as‑context**        | “Runtime context” vs “Design context”                             | Multiplies Contexts incorrectly         | Use **TimeScope tags** (C‑7); keep one Context (D‑CTX‑5).                    |
| **A6 Cross‑lingual blending** | Mixing language labels as one context despite divergent semantics | Hidden drift                         | Split Contexts per **D‑CTX‑7** or document shared semantics if truly bound.  |

---
