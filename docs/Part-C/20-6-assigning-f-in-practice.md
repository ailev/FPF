## 6 · Assigning **F** in Practice (guidance)

This section is **informative**. It offers practical heuristics so engineers‑managers can triage artifacts quickly and consistently.

### 6.1 · Three questions to place a first guess

1. **Can a competent reader misread the claim?**
   If yes, you are likely ≤F2. If no (unique reading by construction), you are ≥F3.
2. **Are constraints stated as predicates over typed things?**
   If yes, you are around **F4**; if they are only executable tests without predicates, you’re **F5**.
3. **Would a tool *reject* an incorrect change?**
   If “only by rerunning examples,” that’s **F5**; if “because the logic kernel/type checker refuses it,” that’s **F7–F8**.

### 6.2 · Decision steps (quick rubric)

* **Has complete template?** If not, **F0–F1**. If yes →
* **Are per‑claim acceptances written (even informal)?** If not, **F2**. If yes →
* **Are they predicate‑like (quantifiers, implies, forall/exists)?** If yes, **F4**; if no, **F3**.
* **Is there an executable model with declared semantics?** If yes, **F5–F6** (hybrid if both discrete/continuous).
* **Are core properties machine‑proved?** If yes, **F7**; if types carry the property, **F8**; if higher equivalence is essential, **F9**.

### 6.3 · Litmus tests (do/don’t)

* **Do** point to the **lowest** rigor segment that is essential to the artifact; **F is capped by the weakest required part**.
* **Do** keep **F** independent from **R** and **G**: a well‑verified but informal hypothesis is **low F, high R**; a formal theorem without empirical content is **high F, R=N/A or VA‑lane only**.
* **Don’t** “average” levels: a long F8 appendix does not make an F3 body F8; F sticks to the **claim** or the **episteme**, not to page counts.
* **Don’t** upgrade F just because a tool was used; tooling matters only if the **content** reaches the anchor’s semantics.

### 6.4 · Anti‑patterns

* **Terminology inflation.** Calling acceptance criteria a “specification” without predicates → F3 at most.
* **Notebook mirage.** Treating an executable notebook with hidden state as formal proof → remains F5 without explicit obligations.
* **Schema worship.** Equating JSON Schema validity with logical safety → F2/F3, not F4.
* **Proof‑by‑CI.** “The pipeline is green” is not a logic kernel; without proofs or dependent types, F≤F6.

### 6.5 · Edge cases and how to rate them

* **Generated docs from formal sources.** Rate **by the source**, not the rendered prose. If the source is F7 proofs, the generated PDF remains **F7** as long as it is a faithful view.
* **Natural‑language with embedded formulas.** If formulas are illustrative only, keep **F3**; if they define obligations and are checkable, move **F4–F6** accordingly.
* **Standards in code comments.** If they constrain behavior and are enforced (e.g., via runtime/type checks), consider **F4–F5**; otherwise **F3**.
* **Hybrid ML systems.** The training procedure (executable) suggests **F5**; safety guards as formal constraints can raise parts to **F4/F6**; certified components may reach **F7/F8**.

### 6.6 · Raising **F** (ΔF moves, informative)

Typical **ΔF** steps (see KD‑CAL motion primitives):

* **F2→F3:** Introduce controlled phrasing; per‑claim acceptances.
* **F3→F4:** Recast acceptances as typed predicates/invariants.
* **F4→F5:** Provide executable semantics with declared Standards.
* **F5→F7:** Encode properties in a proof‑capable logic; prove core invariants.
* **F7→F8/9:** Migrate property into types / adopt higher‑equality foundations.

> **Note.** ΔF does not require changing **G** or **R**. Many projects raise F while holding scope and evidence constant, then tackle R (validation) separately.
