## 5.4 · Polarity, Comparability, and Gauges (normative)

> **Notation.** To avoid clashes with the kernel’s global aggregation symbol, this architheory denotes a gauge mapping by **𝒢** (calligraphic 𝒢).

**R‑POL‑1 (Declared polarity).** Every ordered scale **SHALL** declare polarity at the **template**. Any Gauge **𝒢** must be **monotone** with that polarity.

**R‑CMP‑1 (Comparability conditions).** Two readings are **directly comparable** when they share **Characteristic**, **scale type**, and **unit** (or unit is convertible within one quantity kind). Otherwise, comparability requires an explicitly declared **𝒢** on a common representation.

**R‑G𝒢‑1 (Gauge disclosure).** If a metric issues a **Score**, its Gauge **𝒢 : Coordinate → Score** **SHALL** be named with a **bounded codomain** and stated monotonicity. (The old text discussed “score ranges” and mapping; **C.16** keeps only the conceptual duty. )

**R‑G𝒢‑2 (Ordinal respect).** For ordinal inputs, **𝒢** must be **order‑preserving**; interval assumptions **MUST NOT** be smuggled in.

