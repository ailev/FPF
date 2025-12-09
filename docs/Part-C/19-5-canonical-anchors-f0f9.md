## 5 · Canonical Anchors **F0…F9** (normative)

> **How to read this section.** Each anchor defines *what is minimally true* of an episteme to be rated at that level — across disciplines. The anchors are **ordinal**: F7 is strictly more formal than F6, etc. Levels are **about expression**, not truth; Reliability (R) and ClaimScope (G) are separate.

For every anchor we state **Definition**, **Inclusion criteria**, **Non‑examples** (to prevent over‑rating), and **Indicative artifacts** (cross‑disciplinary, post‑2015).

---

### 5.1 · **F0 — Unstructured Prose**

**Definition.** Free natural language; ambiguous; unstated assumptions; no required sections; meaning depends on reader context.
**Inclusion criteria.** Narrative exists but lacks stable structure; terms may shift meaning; no explicit acceptance/denial conditions.
**Non‑examples.** Any document with a consistent outline and stable vocabulary is at least F1.
**Indicative artifacts.** Whiteboard photos; impromptu email threads; notes from a hallway discussion; an ad‑hoc wiki page with mixed jargon.

---

### 5.2 · **F1 — Scoped Notes**

**Definition.** Informal narrative with a **consistent scope** and **stable terms**; some headings; the central claim/problem is bounded.
**Inclusion criteria.** Key terms are used consistently; scope is named (e.g., “for single‑node scheduling”); still no explicit criteria.
**Non‑examples.** If each requirement already names a check or scenario, that is F2+.
**Indicative artifacts.** A design note that consistently uses the same nouns/verbs and states “this applies to v2 of the service”; a lab memo defining a focus population.

---

### 5.3 · **F2 — Structured Outline**

**Definition.** A **complete template** (Context/Problem/Forces/Solution/…) is populated; content is coherent end‑to‑end; criteria are mostly placeholders.
**Inclusion criteria.** All expected sections exist; cross‑references are consistent; open items are marked (e.g., “TBD acceptance”).
**Non‑examples.** If acceptance criteria are explicit per claim, that is F3+.
**Indicative artifacts.** A draft pattern/spec with fully populated sections but qualitative language; an experiment plan with all slots filled yet non‑operational metrics.

---

### 5.4 · **F3 — Controlled Narrative**

**Definition.** Narrative remains human‑readable but uses **constrained phrasing**; each claim has a **clear, singular interpretation**.
**Inclusion criteria.** Use of controlled NL or disciplined templates (e.g., “shall/if/then”); per‑claim **acceptance statements** exist in prose.
**Non‑examples.** If properties are encoded as logical constraints or typeable Standards, that is F4+.
**Indicative artifacts.** Requirements written in Attempto‑style controlled English; decision rules with explicit pre‑/post‑conditions phrased in a fixed schema.

---

### 5.5 · **F4 — First‑Order Constraints**

**Definition.** Key claims are expressible at **≈ first‑order logic** (FOL) granularity; invariants/constraints are **explicit and checkable in principle**.
**Inclusion criteria.** Each critical statement can be rendered as a predicate over well‑typed variables; conflict/consistency checks are conceivable.
**Non‑examples.** Bare unit tests or executable code without stated invariants is not automatically F4.
**Indicative artifacts.** TLA+ or OCL constraints on a model; an API spec where pre/postconditions and invariants are written as logic‑like rules; well‑typed schema constraints with quantification over entities.

---

### 5.6 · **F5 — Executable Math / Algorithmics**

**Definition.** Content has **precise execution semantics**; results can be checked by **running** (simulation or computation).
**Inclusion criteria.** A model is encoded so that outcomes are deterministic (modulo declared randomness); simulations/tests demonstrate the claims’ executable shape.
**Non‑examples.** “It runs” without a statement of what is guaranteed is not enough; opaque notebooks with side effects but no declared semantics stay F3–F4.
**Indicative artifacts.** Differential‑equation models in code; a reference implementation with clear Standard comments linked to tests; an ML training recipe where the algorithmic pipeline and metrics are fully explicit (yet not proven).

---

### 5.7 · **F6 — Hybrid Formalism**

**Definition.** Combination of **discrete and continuous** reasoning or multiple formal layers; **model‑checking obligations** or equivalent are identified and traceable.
**Inclusion criteria.** Hybrid claims (e.g., controller + plant) are spelled out with both sides’ formalisms and the glue; property checks are specified.
**Non‑examples.** A prose description of cyber‑physical behavior without model obligations is ≤F5.
**Indicative artifacts.** Safety envelopes for autonomous motion expressed as state‑space invariants plus controller logic; hybrid automata with stated safety properties; Standards linking simulation to discrete decisions.

---

### 5.8 · **F7 — Higher‑Order Verified**

**Definition.** Core claims are encoded in a **higher‑order logic (HOL)** or equivalent, and **machine‑checked**; proof scripts or structured proofs exist.
**Inclusion criteria.** The kernel/tool verifies each inference step; failing changes break proofs.
**Non‑examples.** A hand proof attached to F4 constraints without machine checking remains F4–F5.
**Indicative artifacts.** A theorem in Isabelle/HOL or HOL‑Light proving a protocol invariant; a verified algebraic property of a cryptographic scheme.

---

### 5.9 · **F8 — Dependent / Constructive Proofs**

**Definition.** **Programs‑as‑proofs** (Curry–Howard) or **dependent type** artifacts; proof terms are part of the artifact; compilation/type‑check is verification.
**Inclusion criteria.** Types capture the property; changing the property changes the type and breaks the build.
**Non‑examples.** A typed program whose types do not encode the critical property is ≤F5.
**Indicative artifacts.** A Coq/Lean implementation whose type encodes sortedness/safety; a certified compiler pass with proof objects maintained by the build.

---

### 5.10 · **F9 — Univalent / Higher Foundations**

**Definition.** Frontier‑grade **higher foundations** (e.g., homotopy type theory / univalence); equality is treated as **structure**; proofs live at that level.
**Inclusion criteria.** Equivalences are recognized as identities by construction; properties rely on higher equalities.
**Non‑examples.** Any proof that does not hinge on higher‑dimensional equality is ≤F8.
**Indicative artifacts.** Formal developments where isomorphic structures are path‑equal by univalence; higher‑inductive types used to encode core invariants.

---

### 5.11 · Cross‑anchor cautions (normative)

* **Execution ≠ Proof.** Running code/examples (F5) is not a proof (F7+) unless proof obligations are explicitly encoded and checked.
* **Schema ≠ Semantics.** Parseable schemas (F2) are not logical constraints (F4) without semantic predicates.
* **Labels ≠ Levels.** “Approved,” “Final,” or “Published” are **status labels** and have no bearing on F unless they explicitly bind to these anchors.

---
