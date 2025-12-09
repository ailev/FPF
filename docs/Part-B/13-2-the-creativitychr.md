## 2 · The **Creativity‑CHR** (references only; no re‑definitions here)

This binding **references** the context‑local **Creativity‑CHR** (see **C.17**) and **does not** restate measurement templates. The primary coordinates are:
• **`Novelty@context`** (C.17 §5.1), • **`ΔDiversity_P`** (marginal; C.17 §5.5), and • **`Q` components** (per A.18).  
**`Surprise`** and **`Illumination`** are **secondary**: Illumination is a **gauge over Diversity_P**; both act as **tie‑breakers** unless explicitly promoted by policy (C.19).  
**`Use‑Value`** (*alias:* `ValueGain`) is **informative for decision lenses** (Decsn‑CAL) and **MUST NOT** enter NQD dominance by default (see C.17 §5.2).

All listed **Characteristics** are **context‑local** with explicit units/ranges and **polarity↑**. They are *measurements*, not eligibility conditions; eligibility conditions are supplied by **USM/RSG**. (Complies with **A.18** measurement discipline; does not overload assurance semantics.)

> **Lexical discipline.** The items above are **Characteristics** in the sense of **A.17/A.18**; avoid reserved names such as “validity” or “operation.”
> **Normalization note.** If a **QualityVector** has heterogeneous units, Contexts SHALL normalize or nondimensionalize each component before Pareto analysis (see CC‑B.5.2.1‑7).
> **D vs I (normative).** **D = ΔDiversity_P** (marginal gain) and is eligible for the primary dominance test. **I** is _portfolio illumination_ (report/visual); it **SHALL NOT** be part of the primary dominance test and is usable **only** as an explicit tie-break per policy.
> **Measurement invariants.** Distances, grids, and transforms MUST be declared once per run, versioned, and referenced from provenance (§3, §5).
