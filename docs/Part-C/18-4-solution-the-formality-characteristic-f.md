## 4 · Solution — The **Formality Characteristic F**

### 4.1 · Identity and Type (MM‑CHR)

* **Name:** `U.Formality` (nicknamed **F** in F–G–R).
* **Type:** `U.Characteristic`.
* **Scale:** **ordinal** (no arithmetic; comparisons and thresholds only).
* **Polarity:** **up** (higher ⇒ more strictly and unambiguously expressed).
* **Unit:** **formality step** (qualitative anchor).
* **Value domain:** default anchors **F0…F9** (see §4.4).
* **Carrier:** any `U.Episteme` (claim/theory/spec/model/policy/etc.).
* **Notation‑agnostic:** the same F semantics apply regardless of symbol system; bridges between notations do **not** change F (they may affect R via CL, see C.2.2).

**Normative reading.** “F = k” states *how strictly the content is expressed*, not whether it is true (R) nor how broadly it applies (G).

---

### 4.2 · Relationship to KD‑CAL (F–G–R)

* **F in the triple.** F is the **Formality coordinate** in the F–G–R assurance space. It influences trust **indirectly**: higher F reduces ambiguity, enabling stronger evidence and safer composition, but **does not** substitute for evidence (R) or scope (G).
* **Composition invariant (weakest‑link).** For any composite episteme,
  **F\_composite = min(F\_parts on support paths)**.
  *Rationale:* the formal rigor of a whole cannot exceed its least‑formal essential part.
* **Orthogonality.** Changing **G** (envelope/scope) or **R** (evidence) does not, by itself, change **F**; conversely, raising **F** does not imply broader G or higher R.

---

### 4.3 · Extensibility and Local Anchors

FPF provides **default anchors F0…F9** (next subsection). **Contexts MAY**:

* introduce **intermediate anchors** (e.g., F6.5) or **named sub‑anchors** (e.g., “F4‑OCL” vs “F4‑TLA‑constraints”),
* publish **domain exemplars** for anchors,
* define **thresholds** (e.g., “claims of type X must be F≥7”).

**Constraints (normative):**

* **Monotonic order is preserved.** New anchors **MUST NOT** invert or blur the ordering.
* **Anchor meaning is conserved.** Local elaborations **SHALL** map to the nearest global anchor without shifting global semantics (e.g., anything called “F8.x” remains **proof‑grade**).
* **No proxy scales.** Do **not** invent alternative “formality modes/tiers” as surrogates; use **F** explicitly.

---

### 4.4 · Default **F0…F9** Anchors (overview)

> *Full anchor definitions with cross‑disciplinary examples appear in §5 (next part). Below is the overview for orientation.*

* **F0 — Unstructured prose.** Free narrative; ambiguous; human interpretation only.
* **F1 — Scoped notes.** Informal but term‑consistent scope; clearer than F0.
* **F2 — Structured outline.** Template present; coherent sections; criteria mostly “TBD”.
* **F3 — Controlled narrative.** Complete template; constraints sketched in constrained NL or pseudo‑formal phrasing.
* **F4 — First‑order constraints.** Explicit invariants/properties expressible at ≈FOL level (checkable conditions exist).
* **F5 — Executable math/algorithmics.** Precisely defined computational semantics; outcomes checkable by execution/simulation.
* **F6 — Hybrid formalism.** Mixed discrete/continuous methods; model‑checking or equivalent obligations identified.
* **F7 — Higher‑order verified.** Core claims encoded and checked in HOL‑style systems.
* **F8 — Dependent/constructive proofs.** Proof‑carrying content (programs‑as‑proofs).
* **F9 — Univalent/higher foundations.** Equality‑as‑structure; frontier‑grade formal foundations.

**Intent of anchors.** They form a **gentle gradient** from “thinker‑friendly” (F0–F3) through “formalizable” (F4–F6) to **proof‑grade** (F7–F9), allowing the **same artifact** to climb without renaming or forking.

---

### 4.5 · Usage Obligations (declaration, not governance)

* **Declare F.** Every normative episteme **SHALL** declare its **F** (one value) in its context. There is **no default**.
* **Use F in reasoning.** Any comparison, composition, or alignment that depends on rigor **SHOULD** reference **F** explicitly rather than implicit labels like “draft/final.”
* **Do not conflate F with status.** Status systems (ESG/RSG) may **refer** to F in their guards, but **F ≠ status**. This pattern defines **what** rigor is, not **when** a Context should require it.

---
