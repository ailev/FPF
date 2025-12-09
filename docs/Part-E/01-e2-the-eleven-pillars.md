## E.2 — The Eleven Pillars \[A] 

### Problem frame 
Pattern E.1 set the FPF mission as an **operating system for thought**. To turn that mission into a durable architecture, FPF needs a small, explicit constitution—principles that remain stable while everything built on top of them can evolve. Without such invariants, domain silos, vocabulary drift, and tool‑centric shortcuts quickly erode coherence and reproducibility across disciplines.

### Problem
Frameworks without binding first principles wobble between two extremes: rigid dogmas that kill adaptation and amorphous guidelines that invite cognitive chaos. In either case, reasoning fragments, auditability collapses, and physical impact suffers.

##### Forces
| Force                          | Tension                                                |
| ------------------------------ | ------------------------------------------------------ |
| **Foundational Stability**     | Immutable core ↔ perpetual adaptation to new knowledge |
| **Cognitive Load**             | Minimal elegance ↔ comprehensive coverage              |
| **Rigor vs Accessibility**     | Formal soundness ↔ intuitive entry for non‑specialists |
| **Universality vs Modularity** | Domain‑agnostic scope ↔ plug‑in extensibility          |
| **Pragmatic Grounding**        | Abstract invariants ↔ measurable, falsifiable outcomes |

### Solution
FPF rests on **eleven non‑negotiable pillars**. Each pillar is a binding constraint that every artefact, pattern, and design‑rationale record (DRR) **must** honour. Together they form the load‑bearing structure that guarantees evolvability, cross‑scale coherence, and didactic clarity.

| ID       | Pillar                         | Essence                                                                                                                   |
| -------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| **P‑1**  | **Cognitive Elegance**         | Highlight decisive structure, eliminate ornamental formalism; separate data governance from thinking.                     |
| **P‑2**  | **Didactic Primacy**           | Human comprehension outranks theoretical or tooling purity.                                                               |
| **P‑3**  | **Scalable Formality**         | A single artefact can mature step‑by‑step from informal guess to formally assured state without forks or rewrites.        |
| **P‑4**  | **Open‑Ended Kernel**          | The micro‑kernel contains only meta‑concepts; all domain knowledge lives in external architheories.                       |
| **P‑5**  | **Plug‑in Layering**           | Architheories are modular, declarative extensions that can be added, replaced, or removed without destabilising the core. |
| **P‑6**  | **Lexical Stratification**     | Every core concept is expressible in four registers: plain name, technical term, formal U.Type, and mathematical symbol.  |
| **P‑7**  | **Pragmatic Utility**          | Proofs, metrics, and models exist to achieve real‑world objectives; falsification is rewarded over confirmation.          |
| **P‑8**  | **Cross‑Scale Consistency**    | Composition algebras (aggregation, boundary, emergence) are invariant across material systems, knowledge, and methods.    |
| **P‑9**  | **State Explicitness**         | Every artefact declares its state (`design‑time`, `run‑time`, etc.); transitions are cheap, traceable, auditable.         |
| **P‑10** | **Open‑Ended Evolution**       | Every entity is expected to evolve indefinitely; cycles must remain cheap, safe, and cognitively rewarding.               |
| **P‑11** | **State‑of‑the‑Art Alignment** | The kernel and architheories track reliable contemporary knowledge and update when the SoTA advances.                     |

> Any DRR that contradicts a pillar must first amend this constitutional pattern.

### Conformance Checklist

| ID         | Requirement                                                                                                                       | Purpose                               |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| **CC‑P‑1** | Every architectural pattern **must** list which pillar(s) it instantiates or refines.                                             | Guarantees constitutional grounding.  |
| **CC‑P‑2** | Every DRR proposing a normative change **must** include a “Pillar Impact Analysis.”                                               | Makes constitutional review explicit. |
| **CC‑P‑3** | Tooling and pedagogical artefacts **should** document which pillar(s) shape their design.                                         | Upholds P‑2 (Didactic Primacy).       |
| **CC‑P‑4** | An architheory is conformant only if its invariants reference **≥ 3** pillars, demonstrating cross‑scale and pragmatic alignment. | Prevents narrow, siloed extensions.   |
| **CC‑P‑5** | When two lawful approaches exist, authors **SHOULD** prefer methods whose **empirical capability slope** is **non‑negative** over the **audited scale window** (data, compute, **freedom‑of‑action**) and **MUST** justify any exception **via** a **BLP Scale‑Audit** (**BLP‑1**) with **declared tolerances** *(α = budget; δ = assurance; units specified)*. | Embeds Bitter‑Lesson preference; curbs heuristic debt. |
 
### Policy — Bitter‑Lesson Preference (BLP)

**Intent.** Favor **general, computation‑leveraged**, and **freedom‑of‑action** methods over hand‑tuned, brittle heuristics *when safety and legality are held constant*. This codifies the empirical trend that methods which scale with **data, compute, and search breadth** outpace bespoke rule‑engineering. **Applicability:** beyond ML, this policy covers **search/optimization**, **control**, **simulation‑based inference**, and other computational sciences where capability improves with scale and exploration. When **NQD/E/E‑LOG** promotes **novelty/coverage (illumination)** to **dominance**, these gauges are included in BLP comparisons for the audited window.

**BLP‑1 — Scale‑Audit Requirement.** Any DRR that selects a more specialized/hand‑engineered method over a general/scalable alternative **MUST** include a **Scale‑Audit**:
* (a) **Parity harness**: same **ComparatorSet**, **freshness window**, and **evaluation seeds/replicates**; portfolio‑first evaluation (see **G.5/G.9**). Dominance criterion: **Pareto‑only** by default across the declared objective vector; any alternative requires a documented waiver by **Gov‑CAL** under **E.3** precedence.
* (b) **Budgets**: sweep **compute** (**steps/tokens/params/time/energy**, as applicable), **data** (size/quality), and **freedom‑of‑action** (from script‑like instructions → minimal prohibitions) **under a fixed risk/safety envelope**. If any parameter cannot be swept, **pin** it and record the invariant.
* (c) **Slopes & uncertainty**: report ∂quality/∂compute, ∂quality/∂data, and (where applicable) ∂coverage/∂**freedom‑of‑action** and **∂novelty/∂budget**; include **error bars/CI** from multi‑seed trials; publish edition pins and policy‑IDs in SCR/telemetry (**G.11**).
* (d) **Resources**: publish **Resrc‑CAL** accounts (time/energy/FLOPs) and assurance deltas (B.3).  
* (e) **Objective declaration**: list the **objective vector** (quality, risk, cost, **and any illumination gauges** per NQD/E/E‑LOG) used for Pareto comparison.

**BLP‑2 — Preference Rule.** Given lawfulness and comparable assurance (within δ) and budget (within α), prefer the method whose **slope vector** is **Pareto‑dominant** over the audited range (per **BLP‑1c/1e**). If no dominance holds within error bounds, prefer the **more general** method (fewer domain‑specific heuristics, greater transfer via Bridges Φ/Ψ); otherwise resolve via **E/E‑LOG** tie‑breakers declared in policy.

**BLP‑3 — Minimal‑Prescription Default.** Author **rules‑as‑prohibitions** (negative constraints) over step‑by‑step scripts. Encode limits in **Φ policy tables** (and **Φ_plane** where applicable) instead of procedural checklists; allow the agent/system to sequence functions autonomously under those constraints (SoS‑LOG). **Pre/post‑conditions and test harnesses remain permitted**; **scripts** are permissible only when mandated by safety/regulation, or with compelling evidence recorded in the DRR **and reviewed under E.3 precedence / E.5 Guard‑Rails**.

**BLP‑4 — Heuristic‑Debt Register.** Any hand‑tuned rule admitted for pragmatic reasons **MUST** be registered as **Heuristic Debt** with: scope, owner, expiry/review window, measurable replacement target under BLP‑2, and a de‑hardening/sunset plan. Track in **CalibrationLedger/BCT (Baseline Change Tracker)** and cite in SCR.

**BLP‑5 — Continuous‑Learning Posture.** Where product policy allows, enable **feedback‑driven adaptation** (e.g., preference learning, critique loops) within Guard‑Rails (**E.5**) and privacy/regulatory controls, with appropriate opt‑outs where required. Disabling adaptation requires DRR justification and a review date.

**BLP‑6 — Precedence & Safeguards.** BLP is a **Gov/Arch** policy instantiated by Pillars **P‑10 (Open‑Ended Evolution)**, **P‑11 (SoTA Alignment)**, **P‑7 (Pragmatic Utility)**, and **P‑1 (Cognitive Elegance)**. It does **not** override safety/ethics (**E.5**) **nor** E.3 precedence rulings; where BLP conflicts with Guard‑Rails, **Guard‑Rails prevail**. When **NQD/E/E‑LOG** elevates illumination to dominance for exploration mandates, BLP **adopts that lens** rather than overriding it.

*Informative SoTA contexts (post‑2015):* portfolio‑first selection across **LLM prompt‑programming vs fine‑tuned task models**; **preference‑learning families (RLHF ↔ DPO)**; **QD archives (MAP‑Elites/CMA‑ME/DQD/QDax)**; **open‑ended environment–method co‑evolution (POET‑class)**; **offline RL vs Decision Transformer parity**; and beyond ML, **optimization/control** (model‑based planning vs hand‑tuned controllers) and **simulation‑based inference** in the sciences. These are **illustrative only**; use the parity harness instead of single‑winner leaderboards.

#### Conformance Checklist — BLP

| ID            | Requirement                                                                                                     | Purpose                                       |
| ------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **CC‑BLP.1**  | Tolerances **α (budget)** and **δ (assurance)** are declared in the DRR or referenced via policy profile.      | Makes BLP decisions reproducible.             |
| **CC‑BLP.2**  | DRR includes a **Scale‑Audit** (BLP‑1a–e) with published slopes and pinned editions/policy‑IDs.               | Makes scale behavior auditable.               |
| **CC‑BLP.3**  | Selection decision cites **BLP‑2** and lists the governing pillars and precedence checks.                      | Ties choice to constitution.                  |
| **CC‑BLP.4**  | Any admitted heuristic is logged as **Heuristic Debt** with expiry/review and de‑hardening plan.               | Prevents silent drift toward brittle rules.   |
| **CC‑BLP.5**  | Default authoring uses **rules‑as‑prohibitions**; deviations are DRR‑justified and safety‑anchored.            | Preserves agent autonomy under constraints.   |
| **CC‑BLP.6**  | Resource accounts (time/energy/FLOPs) and assurance deltas are reported via **Resrc‑CAL** and B.3.             | Avoids “free heuristic” illusions.            |
| **CC‑BLP.7**  | **Replicate counts/seeds** and **confidence intervals** for slope estimates are recorded.                      | Prevents spurious slope inferences.           |

#### Relations
* **Instantiates pillars:** P‑10, P‑11, P‑7, P‑1.  
* **Depends on:** **G.5/G.9** (admission/comparator/selector & parity harness), **G.11** (refresh telemetry), **C.5** (Resrc‑CAL), **C.18** (NQD‑CAL), **C.19** (E/E‑LOG), **F.7/F.9** (Bridges, CL/Φ/Ψ).  
* **Constrained by:** **E.5** Guard‑Rails (DevOps Lexical Firewall; Notational Independence; Cross‑Disciplinary Bias Audit) and **E.3** precedence.

#### Definitions
**α (budget tolerance)** may be relative or absolute; declare units (e.g., % cost, wall‑time, energy). **δ (assurance tolerance)** is the permissible delta in assurance under **B.3**; declare measure and floor(s).

#### Consequences

*Positive*

* Provides an explicit “north star” for every contributor.
* Delivers a falsifiable checklist for evaluating proposals.
* Builds trust in high‑assurance domains through transparency.

*Trade‑offs*

* Constitutional review adds friction to rapid, informal changes.
* Amending the pillar set itself demands high‑bar governance.

### Rationale

The pillars are distilled from systems engineering, philosophy of science, software architecture, and ontology design. They interlock: *Cognitive Elegance* (P‑1) enables *Didactic Primacy* (P‑2); *Open‑Ended Kernel* (P‑4) and *Plug‑in Layering* (P‑5) make *Open‑Ended Evolution* (P‑10) and *SoTA alignment* (P‑11) feasible; *Cross‑Scale Consistency* (P‑8) provides the algebraic backbone for *Scalable Formality* (P‑3). This minimal yet sufficient set balances stability with change, rigor with accessibility, and abstraction with measurable impact.

### Relations
* **Depends on:** `pat:constitutional/vision` – pillars operationalise the mission.
* **Refined by:** All subsequent patterns in the Core Specification.
* **Governs:** Every DRR, tool, and pedagogical artefact linked to FPF.

*These pillars are not a cage but the load‑bearing columns of a workshop where ideas can be safely built, dismantled, and evolved.*

