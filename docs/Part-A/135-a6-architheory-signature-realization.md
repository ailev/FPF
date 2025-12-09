## A.6 — Architheory Signature & Realization  \[A]

### 1. Problem frame

FPF’s architecture is a modular ecosystem of **architheories** (CAL/LOG/CHR) that extend a slim Kernel. To keep composition stable and comparable, each architheory **publishes a public Signature** (the Standard) and provides one or more **Realizations** (private implementations).  
**A.6 as a specialisation.** This pattern is the **architheory‑specific specialisation** of **A.6.0 `U.Signature`** and coordinates cross‑context use with **A.6.1 `U.Mechanism`** (Bridge/CL per **F.9**; penalties route to **R/R_eff** only per **B.3**; **F/G** invariant; **CL^plane** per **C.2.1 CHR:ReferencePlane**).


### 2.  Problem

When Signatures (interface) leak implementation, the ecosystem becomes brittle: (1) substitutability breaks, (2) imports entangle, (3) cross‑context use becomes implicit and unauditable.

### 3. Forces
| Force | Tension |
| --- | --- |
| **Stability vs. evolution** | Keep public promises stable while allowing private Realizations to evolve. |
| **Universality vs. fitness** | One Signature shape across CAL/LOG/CHR vs architheory‑specific vocabularies. |
| **Intension vs. specification** | Signatures state *what & laws*; Realizations carry *how/tests*. |
| **Locality vs. transport** | Context‑local semantics vs explicit, auditable Bridge‑only crossings (R‑only penalties). |
 
### 4. Solution

#### 4.1. `U.ArchitheorySignature` — *the public Standard*

A **Signature** states **what** an architheory offers—its vocabulary, laws, and applicability—**without** embedding implementation or build metadata. It is the stable unit that other architheories import.

#### 4.2. `U.ArchitheoryRealization` — *the private implementation*

A **Realization** satisfies the Signature while remaining opaque. Multiple Realizations may co‑exist; they **may tighten** (never relax) the Signature’s laws (Liskov‑style substitutability).

#### 4.3 · Signature Block — **A.6.0 alignment** and **Architheory View**

Every architheory **SHALL** publish **two adjacent views** of its public contract:
1) the **universal** A.6.0 `U.Signature` Block (*SubjectBlock; Vocabulary; Laws; Applicability*), and  
2) an **Architheory View** that preserves the pass interface used across Part C: **Imports / Derivations / Invariants / BelongsToAssurance**.
This ensures both cross‑family uniformity **and** compatibility with existing architheory architecture. The **universal Block remains the source‑of‑truth**; the **Architheory View is a projection** that MUST NOT introduce fields not derivable from the Block (e.g., no hidden AdmissibilityConditions; no Γ in LOG/CHR).

| `U.Signature` row (A.6.0)          | A.6 alias / where to author it                                           |
|------------------------------------|---------------------------------------------------------------------------|
| **SubjectBlock**            | One‑line declaration above the block (**SubjectKind + BaseType**; may be visually split into **Subject/Quantification**; avoid “governed” wording) |
| **Vocabulary**                     | **Derivations** (public types/relations/operators that the theory contributes) |
| **Laws (Invariants/Guards)**       | **Invariants** (law statements; proofs live in Realizations)             |
| **Applicability (Scope & Context)**| **BelongsToAssurance** + context note in the header; bind a `U.BoundedContext` where relevant; numeric comparability **binds** to **CG‑Spec/MM‑CHR** (normalize‑then‑compare; lawful units/scales). |

**Architheory View (mandatory alongside the universal view):**
* **Imports** — required `U.Type`s/relations already present or produced by earlier passes.  
* **Derivations** — new `U.Type`s/relations/operators the architheory contributes.  
* **Invariants** — law statements (proofs in Realizations).  
* **BelongsToAssurance** — {Typing | Verification | Validation}.
 
*Prohibition.* The Signature block is **conceptual**: no packaging/CI/tooling metadata (LEX firewall), no Γ‑builders (except as permitted below for CAL).

#### 4.4 · Γ‑export policy and layering

* A **CAL** architheory **SHALL** export **exactly one** aggregation/builder `Γ`. The **`Γ` identifier MUST be namespaced** under the architheory `id` (e.g., `ArchitheoryId.Γ`) to avoid collisions.
* **LOG** and **CHR** architheories **SHALL NOT** export `Γ`.  
* Import layering **SHALL** respect the holonic stack: **LOG/CHR may import CAL; CAL may import CAL**; import graphs are **acyclic** and respect **LEX‑BUNDLE** strata (Kernel → Architheory → Context → Instance); no cross‑bleed.

#### 4.5 · Signature header 

Each Signature begins with:  
`id` (PascalCase), `version` (SemVer), `status` (draft/review/stable/deprecated), `classification` (CAL/LOG/CHR), `imports` (list), `provides` (list, including Γ if CAL).  
If **SubjectBlock** are non‑trivial, add a one‑liner in the header (or immediately above the block).

### 5 · Transport & Cross‑Context Use (coordination with A.6.1)

Signatures **SHALL NOT** restate Bridge/CL mechanics. If cross‑context/plane use is intended, the Signature **names** the Bridge conceptually. Semantics are governed by **A.6.1 `U.Mechanism`**; **Bridges** are specified in **F.9**; **CL/CL^k** and **Φ/Ψ** penalty calculus live in **B.3**; **CL^plane** follows **C.2.1 CHR:ReferencePlane**. No implicit “latest”; time‑sensitive guards require an explicit **Γ_time** policy in the consuming mechanism.

### 6. Normative Relations

`implements(Realization, Signature)` (mandatory, one‑way) · `imports(Signatureᵢ, Signatureⱼ)` (DAG) · `provides(Signature, U.Type ∪ Operator)` (public namespace).

### 7 Archetypal Grounding

Provide a brief pair of examples (Work/System; Knowledge/Episteme) that name SubjectBlock, show Vocabulary and Laws, and state Applicability/Context. Keep proofs out of the Signature.

### 8 Conformance Checklist

| ID | Requirement |
|----|-------------|
| **CC‑A6.1** | Every architheory **MUST** declare exactly one `Signature`. |
| **CC‑A6.2** | Every architheory **MUST** provide ≥ 1 `Realization` consistent with its Signature. |
| **CC‑A6.3** | The global graph of `imports` **MUST** be acyclic. |
| **CC‑A6.4** | Realizations **MUST NOT** reference internals of other architheories; only their Signatures. |
| **CC‑A6.5** | A Signature’s `provides` **MUST NOT** redeclare `U.Type`s already exported by transitive `imports`. |
| **CC‑A6.6** | Realizations **MAY tighten** but **MUST NOT relax** Signature laws (Liskov‑style). |
| **CC‑A6.7** | If multiple Realizations exist, authors **SHOULD** provide a short trade‑off rationale. |
| **CC‑A6.8** | The Signature **MUST** include an explicit **A.6.0 alignment** mapping (table or one‑liners). |
| **CC‑A6.9** | Where numeric comparability is implied, **bind** legality to **CG‑Spec/MM‑CHR** (normalize‑then‑compare; lawful units/scales; no ordinal means). |
| **CC‑A6.10** | Any intended cross‑context/plane use **MUST** name the Bridge and defer semantics to **A.6.1**/**Part F**; penalties route to **R/R_eff** only. |  
| **CC‑A6.11** | If `classification = CAL` and a `Γ` is exported, its identifier **MUST** be namespaced under the architheory `id`. |
| **CC‑A6.12** | **Both views** of the Signature are present: the universal A.6.0 Block **and** the **Architheory View (Imports/Derivations/Invariants/BelongsToAssurance)** placed adjacently. |

**Author-facing:**
* [ ] The **two** Signature views are present (A.6.0 Block **and** Architheory View).  
* [ ] If `classification = CAL`, **exactly one** Γ is named.  
* [ ] Imports point **down** the layering and remain **acyclic**.  
* [ ] Any referenced artefacts are anchored by SCR/RSCR identifiers (A.10).  
* [ ] An **A.6.0 alignment note** is provided (table or one‑liners as above).

### 9 Consequences

* **Hard decoupling** — Kernel stability is preserved; swapping a Realization never breaks dependents.  
* **In‑framework competition** — Alternative logics, physics, economic models can co‑exist under the same interface.  
* **Machine‑checkable composition** — Because imports form a DAG and `provides` are explicit, automated loaders can detect conflicts early.

### 10 Didactic Addendum — Benefits & Trade‑offs (informative)

| Benefit | What you get | Trade‑off / Guard |
| --- | --- | --- |
| **Universal shape (A.6.0 alignment)** | One 4‑row block across architheories, mechanisms, methods, disciplines. | Maintain **Intension vs. Specification** separation; no Γ in Signatures except CAL per A.6. |
| **Substitutability** | Multiple Realizations behind one Signature; safe swaps; Liskov‑style tightening allowed. | Relaxing laws is forbidden; otherwise mint a refined Signature or use **U.MechMorph** (A.6.1). |
| **Transport discipline** | **Bridge‑only** crossing; CL penalties route to **R/R_eff**; **F/G invariant**. | Crossings are **named**; no implicit “latest”; **Γ_time** where relevant. |
| **Numeric comparability sanity** | **normalize‑then‑compare** via **CG‑Spec/MM‑CHR**; explicit unit/scale alignment. | **Partial orders return sets**; illegal scalarisation (e.g., ordinal means) is blocked. |
| **Layering predictability** | Exactly **one Γ** for **CAL**; **LOG/CHR** export none; **imports acyclic; no cross‑bleed across strata**. | Some constructs belong as **Mechanisms (A.6.1)**, not as architheories. |

### 11 Rationale

Why “Signature”? Familiar to engineers (function/type signatures) and to logicians (algebraic signatures). It is concise, neutral, and keeps the Kernel slim while enabling competing world‑views to co‑exist behind the same interface.

### 12 Relations

*Specialises / is specialised by*: **A.6.0 `U.Signature`**, **A.6.1 `U.Mechanism`**.  
*Constrained by*: LEX‑BUNDLE (registers/strata), D.CTX (Context), Part F (Bridges & cross‑context transport; naming).
