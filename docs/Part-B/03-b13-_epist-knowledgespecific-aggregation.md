## **B.1.3 Γ\_epist — Knowledge‑Specific Aggregation** \[A]

> **► decided‑by: A.14 Advanced Mereology**
**A.14 compliance —** Use **ConstituentOf** for semantic parts; **PortionOf** only for quantitative splits of texts/data with declared μ (token/byte, etc.); **PhaseOf** for versions/revisions of MethodDescription/documents; no **ComponentOf** here.

> **Plain‑English headline.**
> **Γ\_epist** composes **epistemic holons** (claims, models, datasets, arguments) into a **single episteme** while preserving **provenance**, applying **conservative trust bounds** (B.3 F/G/R), and penalizing **poor conceptual fit** via **congruence levels (CL)**. It is **not** a physical sum; it is a **semantic and evidential fold**.

### 1) Problem frame

* **Holonic foundation.** In the FPF, a `U.Episteme` is a holon whose identity is **knowledge‑bearing** (A.1). It can be a **statement/claim**, a **model**, a **theory**, a **specification**, a **dataset with semantics**, or a **compiled scholarly artifact**.
* **Strict Distinction (A.15).** We separate:
  **structure** (what the episteme comprises), **order** (argument flow), **time** (versioning/phases), **work** (what was spent to produce/validate it), and **values** (objectives/criteria). Γ\_epist stays in the **structure/semantics** lane and calls out to Γ\_ctx/Γ\_time/Γ\_work when needed.
* **Mereology (A.14).** For knowledge composition we primarily use **ConstituentOf** (logical/semantic parts), **UsageOf/ReferenceTo** (external reliance), and **MemberOf** for **collections** (anthologies, corpora). We do **not** use **ComponentOf** (physical) in Γ\_epist.
  `PhaseOf` handles temporal versions of the **same** episteme; **RoleBearerOf** is irrelevant here because knowledge **does not play a role**—it is **used** by a holon‑in‑role (Transformer) at run‑time (A.12).
* **Assurance (B.3).** Knowledge carries **F**, **G**, **R** (Formality, ClaimScope, Reliability). Integration edges carry **CL** (congruence level) that penalizes poor fit. Γ\_epist **must** preserve provenance and apply **conservative** bounds: no “truth averaging,” no silent context hops. **Obligations here are mode/assurance‑gated per C.2.1.**  # [M‑0]
* **Order/time flavours.** Argument sequences may need **Γ\_ctx** (non‑commutative ordering of premises to conclusion). Knowledge evolution uses **Γ\_time** (versioning, deprecation, update). When composition produces **new closure or supervision** (e.g., explanatory theory emerges), we declare **MHT** (B.2).

---

### 2) Problem

Naive aggregation of knowledge holons causes recurring failures:

1. **Trust inflation by averaging.** Averaging confidences of conflicting claims creates a falsely “reliable” whole; violates **WLNK** and **B.3** conservatism.
2. **Provenance erasure.** Merges that drop sources, methods, or links break **A.10 Evidence Graph Referring** and make results unauditable.
3. **Semantic drift.** Folding across mismatched concepts without explicit **mappings** (and their **CL**) yields incoherent composites that look formal but mean nothing.
4. **Order blindness.** Arguments with essential **dependency order** (premise ⇒ lemma ⇒ conclusion) are treated as sets; non‑commutativity is lost and results become non‑reproducible.
5. **Context chimeras.** Combining items across **bounded contexts** (different vocabularies/units/policies) without a **Context Reframe** (B.2) silently corrupts claims and inflates **R**.
6. **Category errors.** Importing **Γ\_sys** rules (e.g., “sum truth,” “avg formality”) into knowledge composition produces physically sounding but epistemically nonsensical models.

---

### 3) Forces

| Force                                      | Tension                                                                                                                      |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| **Conservatism vs. Synthesis**             | Keep **reliability** bounded by the weakest supported link ↔ allow genuine explanatory integration when it actually emerges. |
| **Universality vs. Domain nuance**         | One operator across math, science, engineering specs ↔ domain‑specific semantics and evidence patterns differ.               |
| **Provenance fidelity vs. Cognitive load** | Keep the **full trail** of sources and methods ↔ avoid overwhelming authors with bookkeeping.                                |
| **Order/time discipline vs. Flow**         | Respect argument **order** and version **time** ↔ keep composition usable for day‑to‑day synthesis.                          |
| **Parsimony vs. Fit**                      | Small rule set (A.11) ↔ explicit **congruence** penalties and **context** rebasing when needed.                              |

---

### 4) Solution — **Terms, operator family, invariant Standard, core rules**

#### 4.1 Terms (didactic recap)

* **U.Episteme** — a knowledge holon. Internally we use a didactic triangle:
  **Object** (what it is about), **Concept** (theory/model/claim structure), **Symbol** (SCR carriers: text, code, figures, datasets).
* **Evidence/Provenance Graph** — edges like **evidences**, **derivesFrom**, **usesMethod**, **isMeasuredBy** with anchors (A.10).
* **Mapping edge** — a typed relation between conceptual vocabularies (e.g., ontology alignment, unit conversion) with a **CL** score (0…3/4 per A.15/B.3 convention).
* **SCR** — a `U.SCR` that lists all symbol carriers included in the aggregate; **never dropped**.
* **Bounded context** — a modelling Standard (vocabulary/units/policy). Crossing it requires **Context Reframe** (B.2) or explicit mappings with CL.

> **Didactic reminders.**
> • Knowledge does **not** “act.” Transformers (A.12) **use** knowledge.
> • **MemberOf** creates **collections**; it is not a semantic argument link. Use **ConstituentOf** for logical/evidential composition.
> • **PhaseOf** is for **versions** of the same episteme; if identity, boundary, or context re‑anchor, declare **MHT**.

---

#### 4.2 The operator family (companion flavours)

To keep **design vs run** clean (A.15), Γ\_epist has two companion flavours that share the same algebra but serve different moments:

1. **Synthesis (design‑time)** — fold epistemes into a **draft aggregate**

```
Γ_epist^synth : ( D_know : DependencyGraph< U.Episteme >,
                  T      : U.TransformerRole ) → U.Episteme
```

* **Domain.** `D_know` uses **ConstituentOf**, **UsageOf/ReferenceTo**, **evidences/derivesFrom**, optional **MemberOf** for collections.
 * **Result.** A **composite episteme** whose Object/Concept/Symbol components are assembled; **provenance and SCR are preserved**; F/G/R/CL are provisionally computed for later assurance.   **Gating:** at **M‑mode** only tuple placeholders are required; numeric scoring may be omitted (**\[M‑0/M‑1]**). At **F‑mode** the tuple **MUST** be computable in‑Context (**\[F‑*,L1+]**).  # [M/F]

2. **Compile (run‑time)** — produce the **released artifact** in a bounded context

```
Γ_epist^compile : ( E_synth : U.Episteme,
                    Ctx     : BoundedContext,
                    T       : U.TransformerRole ) → U.Episteme
```

* **Domain.** A synthesized episteme and a **target context** (journal, standard, program spec).
* **Result.** A **context‑anchored** episteme (e.g., published paper/spec) whose **mappings to the context vocabulary** are explicit and carry **CL**; assurance will reference this context baseline (B.3).

**Relationship to Γ\_ctx / Γ\_time.**
If the knowledge fold explicitly depends on **argument order** (e.g., derivation), the internal fold uses **Γ\_ctx** for the sequence. If a **temporal storyline** (updates, retractions) is important, use **Γ\_time** to slice versions; **Γ\_epist** then composes the **current slice**. If composition yields **new explanatory closure** beyond WLNK/CL, declare **MHT** (B.2).

---

#### 4.3 Invariant Standard (how the Quintet applies; **math by level**)

* **IDEM (Idempotence).** Folding a single episteme returns itself; no accidental “upgrade.”
* **COMM/LOC (Local commutativity / locality).** For **independent** subgraphs (no logical/evidential dependency), fold order/location is irrelevant; when dependencies exist, **Γ\_ctx** controls order explicitly.
* **WLNK (Weakest‑link bound).** Aggregate **Reliability (R)** is bounded by the **weakest supported link** along any justification path, **after** considering the **lowest CL** on mappings used by that path.
* **MONO (Monotonicity).** Strengthening a part (raising **R** with valid evidence or raising **CL** on a needed mapping) cannot lower aggregate **R**. Adding **contradictory** evidence is **not** an improvement; it triggers conflict handling (below), not MONO.

2. **Reliability fold.** Along any support spine, **R\_raw = min\_i R\_i**; apply congruence penalty Φ(CL\_min) → **R\_eff = max(0, R\_raw − Φ(CL\_min))**.  *No averaging; weakest‑link.*  
   **Math by level:**  
   – **\[M‑0/M‑1]** allow **ordinal** comparisons only (no arithmetic on R); Φ may be stated qualitatively (“low/med/high”).  
   – **\[M‑2/L1]** require numeric Φ table (default in §4.4) and reproducibility tag on empirical edges.  
   – **\[F‑*,L1/L2]** require formal derivability of the fold rules from LOG‑CAL; constructive mode annotates `proof.kind=constructive`.  # [M/F]

#### 4.4 Core rules for epistemic aggregation (design‑time synthesis)

When computing **Γ\_epist^synth(D\_know, T)**:

1. **Provenance preservation.**
   The **provenance/evidence graph** is **unioned with de‑duplication**; every claim in the aggregate remains traceable to its sources and methods. No source, method, or dataset that supports a retained claim may be dropped.

2. **SCR construction.**
   Build a **U.SCR** that lists all symbol carriers (texts, code, figures, datasets) that materially participate in the aggregate. Provenance nodes must be mappable to SCR entries.

3. **Object alignment.**
   Determine a **common Object** via domain taxonomy (e.g., **least common ancestor**) or create a `U.CompositeEntity` with explicit **mappings**. Record **CL** for each mapping; **do not** silently merge homonyms.

4. **Concept integration with CL penalty.**
   Compute provisional **F/G/R** of the aggregate:

   * **F\_eff** = min(F\_i) (formality is as strong as the least formal constituent actually used).
   * **G\_eff** = function of coverage; typically **monotone** in included scope, capped by weakest definitional fit.
   * **R\_eff** = min over justification paths of { R\_i along the path } **penalized** by the lowest **CL** used by that path: `R_eff := max(0, min_path( min_claimR(path) − Φ(CL_min(path)) ))`, where **Φ** is the normative penalty function defined below.
      If a mapping with **CL < threshold** is essential to a path, mark the claim **provisional**.
 5. **Normative Penalty Function Φ (v1.0)**
The penalty function `Φ` quantifies the loss of reliability due to poor conceptual alignment between parts.

| Congruence Level `CL_min` | 0 | 1 | 2 | 3 |
| :--- | :--- | :--- | :--- | :--- |
| **Penalty Φ(CL_min)** | 1.5 | 1.0 | 0.5 | 0.0 |

+*A domain profile **MAY** provide an alternative table but **MUST** preserve monotonic decrease (a lower `CL` cannot have a smaller penalty). The default values are derived from empirical fits in KD-CAL Bench 0.3.*

 6. **Conflict detection (no averaging).**
    Detect contradictions (e.g., `p` and `¬p` with overlapping scope). Do **not** average. Either (i) **separate** by context or scope (bounded contexts; Γ\_time slices), (ii) mark **provisional** with explicit conflict edges, or (iii) if resolution yields **new closure**, consider **MHT**.

7. **Handling of Axiomatic vs. Postulative Epistemes**
   In alignment with ADR-028, the computation of `R_eff` depends on the episteme's declared `mode`.

*   For an input episteme `E_i` with **`mode: axiomatic`**, empirical `R` is N/A; take `R_i_eff = F_i`. **Tag:** `line=formal`.  # [F‑*]
*   For **`mode: postulative`**, use declared `R_i` with decay; **Tag:** `line=empirical`.  # [M‑1/M‑2/F]
*   The aggregate `E_eff` **MUST** also declare a mode. If all inputs are `axiomatic`, the output is `axiomatic`. If any input is `postulative`, the output **MUST** be `postulative`.
*   **Constructive note.** Under **F‑constructive**, equivalence claims use **isomorphism/equivalence** in the chosen UF library; **CL=2** means proof‑reconstructed alignment, not mere model‑theoretic appeal.  # [F‑constructive]
 
7. **Order‑aware arguments (optional).**
   If the argument requires premise ordering, embed a **Γ\_ctx** fold inside Γ\_epist; record the **OrderSpec** for reproducibility (NC‑1..3).
   **Gating:** OrderSpec is **recommended** at **M‑1** and **required** at **M‑2/F**.  # [M‑1→F]

8. **No costs here.**
   Any compute/collection effort is **Γ\_work**; attach references but do not mix costs into epistemic aggregation.

#### 4.5 Core rules for compilation (run‑time context anchoring)

When computing **Γ\_epist^compile(E\_synth, Ctx, T)**:

1. **Context bindings.**  # [M‑1+]
   Map all operative concepts/units/claims into **Ctx**; record mappings and their **CL**. If the rebase changes boundary/objective of the episteme (e.g., from descriptive compendium to explanatory theory with commitments), **declare Context Reframe (MHT)** per B.2.

2. **Assurance baseline (gated).**  
   Recalculate the **assurance tuple** (B.3) **in Ctx**: F and R may change with formalization and mapping penalties; G is re‑expressed in Ctx’s scope.  
   **Gating:**  
* **\[M‑0]** narrative justification only;  
* **\[M‑1]** qualitative tuples allowed;  
* **\[M‑2/L1]** numeric tuple required;  
* **\[F‑*/L2]** tuple **and** proof obligations on weight/penalty model selection.  # [M/F]

3. **Release SCR.**
 Produce RSCR with carrier hashes; at **L2** require independent re‑hash verification.  # [M‑1/L2]

4. **Order/time hooks.**
   If the compiled artifact includes an internal derivation, carry the **OrderSpec**; if it codifies a specific **time slice** of evolving knowledge, link back to the **Γ\_time** slice used.

### 5) Archetypal grounding (worked, didactic)

#### 5.1 Episteme — **Meta‑analysis into a guidance statement**

* **Inputs (U.Episteme):**
  `E₁` randomized trial (R=0.84, F=3, G=medium), `E₂` observational study (R=0.55, F=2, G=wide), `E₃` mechanistic model (R=0.60, F=3, G=narrow).
  Mappings: dosage units (mg ↔ IU), outcome definitions (pain scale variants), each with declared **CL** (e.g., unit mapping CL=3, outcome alignment CL=2).

* **Γ\_epist^synth:**

  * **Provenance preservation:** all study protocols, datasets, analysis scripts listed in the **SCR**.
  * **Object alignment:** “acute low‑back pain within 6 weeks” via taxonomy LCA; non‑aligned chronic cohorts excluded or mapped with low CL and flagged.
  * **Concept integration:** compute provisional `R_eff` along each justification path, penalized by \*\*Φ(CL\_min(path))`; aggregate `R\_eff\` = min over paths.
  * **Conflict handling:** `E₂` contradicts `E₁` in a subgroup; kept as **provisional** with explicit conflict edge and scope note (different baseline severity).

* **Γ\_epist^compile (journal context):**
  Map outcomes to journal’s required measure, recalc F/G/R with mapping penalties; produce release **SCR** (hashes, versions) and context baseline.
  Result: “Guidance Statement v1.0” with conservative `R`.

* **Why not averaging?**
  Averaging would inflate `R` and hide low‑CL outcome mappings; Γ\_epist enforces pathwise **min** + **CL** penalty.

---

#### 5.2 Episteme — **Safety case from heterogeneous evidence**

* **Inputs:** requirement spec (F=3, R=0.7), hazard analysis (F=2, R=0.6), test logs (F=1, R=0.8), formal proof of controller property (F=3, R=0.9).

* **Γ\_epist^synth:**

  * Provenance union; **SCR** includes requirements, proof artifact, test datasets.
  * Concept integration: controller proof applies only under assumptions A; test logs violate A in edge case → **CL** low for mapping “test scenario ≡ proof assumption.”
  * `R_eff` bounded by the weakest justification path after **Φ(CL\_min)**; claim on “system‑level safety” marked **provisional** until assumption alignment is demonstrated.

* **Γ\_epist^compile (certification context):**
  Context re‑base to regulatory vocabulary; if the re‑base changes objective/boundary (e.g., from internal assurance to public certification), consider **MHT (Context Reframe)** per B.2.

---

#### 5.3 Contrast (didactic)

| Aspect          | **Γ\_epist (Knowledge)**                                         | **Γ\_sys (Physical)**                       |
| --------------- | ---------------------------------------------------------------- | -------------------------------------------- |
| What is folded? | Claims, models, datasets, arguments                              | Components, materials, assemblies            |
| Conservatism    | **Pathwise min** of R + penalty **Φ(CL)**                        | WLNK via **weakest part** (strength, rating) |
| Fit             | **Mappings** with declared **CL**                                | **Interfaces/BIC** compatibility             |
| Order/time      | Optional **Γ\_ctx** for argument order; **Γ\_time** for versions | Γ\_ctx for workflows; Γ\_time for phases     |
| Work/cost       | External in **Γ\_work** (compute, curation)                      | External in **Γ\_work** (energy, labour)     |

---

### 6) Proof obligations (normative)

**At synthesis (Γ\_epist^synth):**

1. **PO‑SYN‑PROV.** The **provenance/evidence graph** MUST be preserved (union with de‑duplication); every retained claim is traceable to sources/methods in the **SCR**.
2. **PO‑SYN‑OBJ.** The **Object** MUST be identified (single subject via LCA or explicit `U.CompositeEntity`) with declared **mappings** and their **CL**.
3. **PO‑SYN‑CL.** All **mapping edges** that bridge semantics/units MUST carry **CL**; the chosen penalty **Φ** MUST be monotone in CL (lower CL ⇒ higher penalty). Thresholds for marking **provisional** MUST be stated.
4. **PO‑SYN‑R.** `R_eff` MUST be computed as **min over justification paths** of (claim reliabilities along the path **minus** `Φ(CL_min(path))`). No arithmetic mean is allowed for reliability.
5. **PO‑SYN‑CONFLICT.** Contradictions MUST be either (i) separated by context/scope, (ii) marked as **provisional** with explicit conflict edges, or (iii) escalated to **MHT** if resolution yields new explanatory closure.
6. **PO‑SYN‑ORDER.** If order matters, the **OrderSpec** MUST be recorded and Γ\_ctx **NC‑1..3** (determinism, context hash, partial‑order soundness) MUST hold.
7. **PO‑SYN‑NOWORK.** Resource spending, yields, and dissipation MUST NOT be computed here; instead, attach references to the aligned **Γ\_work** composition.

**At compilation (Γ\_epist^compile):**

1. **PO‑COMP‑CTX.** The target **bounded context** MUST be declared; all active concepts MUST be mapped with **CL**; context vocabulary/units recorded.
2. **PO‑COMP‑ASSUR.** The assurance tuple (F/G/R) MUST be recomputed **in the target context** with the applied **CL penalties**.
3. **PO‑COMP‑REL.** A **release‑grade SCR** (hashes, versions, dates) MUST be produced.
4. **PO‑COMP‑MHT.** If the compilation re‑anchors **boundary**, **objective**, or **identity** (e.g., from compendium to explanatory theory), an **MHT (Context Reframe)** MUST be declared with a Promotion Record (B.2).
5. **PO‑COMP‑ORDER/TIME.** If derivational order or a specific time slice is essential, the **OrderSpec** and the **Γ\_time** slice MUST be referenced.

---

### 7) Conformance Checklist (normative)

| ID            | Requirement                                                                                                                                                         | Purpose                        |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **CC‑B1.3.1** | Inputs to Γ\_epist MUST be `U.Episteme` holons; **ComponentOf** is forbidden; use **ConstituentOf / UsageOf / ReferenceTo**; **MemberOf** only for **collections**. | Prevent category errors.       |
| **CC‑B1.3.2** | Provenance and **SCR** MUST be preserved in the aggregate; dropping sources or methods is non‑conformant.                                                      | Enforce Evidence Graph Referring.    |
| **CC‑B1.3.3** | Aggregate **R** MUST follow the **pathwise min** rule with **Φ(CL\_min)** penalties; no averaging of reliability.                                                   | Guard conservatism (WLNK).     |
| **CC‑B1.3.4** | Contradictions MUST NOT be smoothed by arithmetic; handle by **scope separation**, **provisional** status, or **MHT**.                                              | Keep incoherence visible.      |
| **CC‑B1.3.5** | Every `U.Episteme` serving as an input to `Γ_epist` **MUST** declare its `mode` (`axiomatic` or `postulative`). An aggregate holon's mode **MUST** be `postulative` if any of its constituents is `postulative`. | Prevent category errors in reliability calculation. |
| **CC‑B1.3.6** | Crossing bounded contexts requires either **explicit mappings with CL** or an **MHT (Context Reframe)**.                                                            | Make context explicit.         |
| **CC‑B1.3.7** | If order matters, Γ\_ctx **NC‑1..3** MUST hold; if versions matter, the **Γ\_time** slice MUST be identified.                                                       | Preserve order/time integrity. |
| **CC‑B1.3.8** | Design‑time **synthesis** and run‑time **compilation** MUST NOT be conflated; use the appropriate flavour.                                                          | Maintain A.15 separation.      |

### 8) Anti‑patterns & repairs

| Anti‑pattern             | Symptom                                           | Repair                                                                                     |
| ------------------------ | ------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Truth‑averaging**      | Averaging confidence of conflicting claims        | Apply **pathwise min** with **CL** penalties; separate scopes or mark **provisional**.     |
| **Provenance amnesia**   | Sources/methods disappear in the aggregate        | Rebuild **SCR**; re‑run Γ\_epist with provenance union.                               |
| **Homonym merge**        | Different concepts with same name silently merged | Insert **mapping edges** with CL; if CL too low, split by context or mark **provisional**. |
| **Context hop**          | Mixed units/vocabularies without declaration      | Declare **bounded context** and mappings; if purpose changes, use **MHT**.                 |
| **Version soup**         | Mixed time slices without clarity                 | Use **Γ\_time** to slice; compose current slice only; link others explicitly.              |
| **Work stuffing**        | Compute/curation cost blended into reliability    | Move costs to **Γ\_work**; keep R based on evidence, not spend.                            |
| **Orderless proof**      | Derivation steps treated as a set                 | Add **OrderSpec**; compose with Γ\_ctx inside Γ\_epist.                                    |
| **Synergy by narrative** | “New theory” claimed without BOSC evidence        | If closure/supervision actually emerges, declare **MHT**; otherwise lower claims.          |

---

### 9) Consequences

**Benefits**

* **Auditability by construction.** Every retained claim remains tied to its sources; **SCR** guarantees reconstructability.
* **Safe synthesis.** **R** cannot be inflated; **CL penalties** make conceptual misfit explicit.
* **Context‑aware releases.** Compiled artifacts are aligned with a declared context; cross‑context reuse is principled.
* **Didactic clarity.** Separates **semantic folding** (Γ\_epist) from **order** (Γ\_ctx), **time** (Γ\_time), **spend** (Γ\_work), and **emergence** (B.2).

**Trade‑offs**

* **Mapping overhead.** Declaring mappings and **CL** costs time; it prevents silent incoherence.
* **Conservative stance.** Results may look pessimistic; this is deliberate (WLNK). Use **MHT** only for genuine explanatory closure.

---

### 10) Rationale (informative)

* **Epistemic composition is not physical addition.** Reliability must be bounded by the **weakest justified path**, not averaged; conceptual misalignment must **reduce** confidence, not be ignored.
* **Provenance is part of meaning.** Dropping sources/methods changes what the episteme **is**; Γ\_epist treats provenance and **SCR** as first‑class.
* **Context matters.** Bounded contexts structure practice; formal **Context Reframe (MHT)** prevents quiet re‑interpretations of claims.
* **Parsimony with power.** A small set of rules (provenance preservation, CL‑penalized pathwise min, order/time hooks, context discipline) is enough to model scientific and engineering knowledge without importing domain‑specific tool jargon.

---

### 11) Relations

* **Builds on:** A.12 (Transformer Role—compilers/editors enact), A.14 (Mereology Extension—ConstituentOf/MemberOf/PhaseOf usage), A.15 (Strict Distinction).
* **Coordinates with:** B.1.1 (Proof kit), B.1.4 (Γ\_ctx/Γ\_time inside knowledge folds), B.1.6 (Γ\_work for compute/collection spend).
* **Triggers/Complements:** B.2 (MHT) when explanatory closure or context re‑base creates a **new whole** (theory, standard).
* **Feeds:** B.3 (Assurance) — `F/G/R` and **CL** baselines computed here become inputs to trust calculations.

> **One‑sentence takeaway.**
> **Γ\_epist** preserves provenance, penalizes poor conceptual fit, forbids reliability averaging, and makes context explicit—so that knowledge aggregates are conservative, auditable, and genuinely coherent.
