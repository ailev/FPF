## Pattern E.3 — **Principle Taxonomy & Precedence Model** \[A] 

### Problem frame
Pattern E.2 supplies eleven immutable pillars, yet experience shows that a **flat list of principles invites ambiguity**: reviewers cannot decide which pillar overrules another  and “dead‑letter” rules accumulate. 

### Problem

When two pillars or derived principles pull in opposite directions, architectural decisions stall—or worse, drift toward the loudest voice. Without an explicit **taxonomy and precedence cascade**, FPF risks devolving into subjective debate, breaking its claim to be a rigorously *auditable* “operating system for thought.”

### Forces
| Force                                 | Tension                                                            |
| ------------------------------------- | ------------------------------------------------------------------ |
| **Categorical Clarity**               | Coherent grouping ↔ preservation of individual nuance              |
| **Deterministic Conflict Resolution** | Predictable hierarchy ↔ flexibility for context‑specific overrides |
| **Evolutionary Stability**            | Durable core ↔ adaptability to new knowledge                       |

### Solution
1. **Principle Taxonomy**
   Every principle is an instance of `U.Principle` assigned **exactly one** class ∈ { `Gov`, `Arch`, `Epist`, `Prag`, `Did` }.

   | Class                                    | Scope & Purpose                           | Example Pillars                                   |   |
   | ---------------------------------------- | ----------------------------------------- | ------------------------------------------------- | - |
   | **Gov** (Governance)                     | Change process, community decision‑making | P‑10 Open‑Ended Evolution · P‑11 SoTA             |   |
   | **Arch** (Architectural)                 | Macro‑structure & invariants              | P‑1 Cognitive Elegance · P‑4 Kernel               |   |
   | **Epist** (Epistemological and Ontological) | Semantics, evidence, trust                | P‑3 Scalable Formality · P‑8 Consistency          |   |
   | **Prag** (Pragmatic)                     | Real‑world value & cost/benefit           | P‑7 Pragmatic Utility                             |   |
   | **Did** (Didactic)                       | Cognition & learnability                  | P‑2 Didactic Primacy · P‑6 Lexical Stratification |   |

   *Epistemological* sub‑concerns (reasoning, falsifiability) reside inside **Onto**, avoiding category sprawl yet keeping semantics and trust in one bucket.

 2. **Precedence Stack**

   | Level | Governing Artefact                    | Overrides        |
   | ----- | ------------------------------------- | ---------------- |
   | 0     | **Vision & Mission** (E.1)            | everything       |
   | 1     | **Eleven Pillars** (E.2)              | all below        |
   | 2     | **Principles** (this pattern)         | patterns & DRRs  |
   | 3     | Architectural / Definitional patterns | local rules      |
   | 4     | Tooling & Pedagogy                    | informative only |

**Within Level 2 of precedence stack** the default order is:
`Gov ≫ Arch ≫ Epist ≫ Prag ≫ Did`

 **Graph Rule** — The precedence graph MUST be acyclic; any new edge that would form a cycle is **rejected**.
 
Governance principle vs Architectural principle clash: e.g. Core release schedule (Gov) outranks performance‑tuning (Prag)

### Conformance Checklist

| ID          | Requirement                                                                                                          | Purpose                          |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| **CC‑PT.1** | Every principle record **MUST** state `class` and may list `precedence_over[]`.                                      | Enables deterministic overrides. |
| **CC‑PT.2** | Precedence graph **MUST** be acyclic.    | Prevents circular law.           |
| **CC‑PT.3** | Any DRR introducing/modifying a principle **MUST** include a *Pillar Impact Analysis* and proposed precedence edges impact on each affected Pillar (P‑1… P‑11)| Aligns evolution with Pillars.   |

### Illustrative Conflict Resolution

1. **The Conflict**  
   * **P‑1 Cognitive Elegance** (`Arch`) demands an unambiguous term for “part–whole” entities, pushing us toward **Holon**.  
   * **P‑2 Didactic Primacy** (`Did`) values immediate practitioner familiarity, pushing us to retain **System**.

2. **Risk of Stalemate**  
   Without a precedence cascade, the discussion would collapse into subjective argument: *“purity beats clarity!”* vs *“clarity beats purity!”*.

3. **Applying the Precedence Model**  
   * Default order: **Gov ≫ Arch ≫ Epist ≫ Prag ≫ Did**.  
   * `Arch` outranks `Did`; therefore **P‑1** takes formal precedence over **P‑2**.

4. **Principled Decision**  
   We adopted **Holon** to satisfy the higher‑priority principle and mitigated the didactic cost by:  
   * declaring `System ≡ U.System ⊑ U.Holon`,  
   * providing aliases and an “On‑Ramp” tutorial.

> *The precedence rule did not merely name a winner; it compelled a solution that honoured both principles in proportion to their rank.*

**Precedence (high → low).** Law & Regulation → **E.5 Guard‑Rails** → **B.3 Trust & Assurance** → **E.3 governance decisions** → **E/E‑LOG policies** (editioned) → **BLP (E.2)** → Product Policies → Implementation Tactics.

**Notes.**
* BLP is a constitutional policy (see E.2 / “BLP”), but **does not supersede** E.5 Guard‑Rails nor B.3 assurance floors; it **does govern** ties among lawful, comparable‑assurance options.
* Wherever **NQD/E/E‑LOG** promotes illumination gauges to dominance, **BLP adopts that lens** rather than overriding it (see E.2 BLP‑6).
* Any exception to policy **MUST** include a DRR with rationale and expiry.
* **BLP Override (Waiver).** When a narrower hand‑engineered method is selected over a general/scalable alternative **within declared tolerances** (α = budget, δ = assurance), the DRR **MUST** include:
  - a **BLP Scale‑Audit** (see E.2 **BLP‑1**) covering compute/data/**freedom‑of‑action** sweeps and slope/uncertainty reporting,
  - the **tolerances** α/δ and objective vector used (E.2 **BLP‑1e**),
  - a **Heuristic‑Debt** entry (owner, scope, expiry/review, de‑hardening plan) per E.2 **BLP‑4**,
  - an **Oversight Level** (see **E.3‑ABL**) and the approving authority (see **Approval matrix** below).
**Portfolio‑first parity.** All precedence decisions that compare methods **MUST** use the G.5/G.9 parity harness and **Pareto** dominance; scalarisation across mixed scales/units is **prohibited** (B.3).

**BLP — Bitter‑Lesson Hooks into Precedence**
1) **Tie‑breaking.** If two lawful options are **within δ** assurance and **within α** budget, prefer the option whose **slope vector Pareto‑dominates** over the audited window; if no dominance, prefer the **more general** method. (E.2 **BLP‑2**.)
2) **Script‑vs‑Search conflicts.** For conflicts between **procedural scripts** and **general search/learning**, scripts prevail **only** when mandated by E.5 or regulation, or when a DRR records a **BLP‑waiver** with expiry and hazard rationale (E.2 **BLP‑3/6**).
3) **Publication.** Precedence rulings that reference BLP **MUST** publish editioned policy‑IDs, edition pins, and **Resrc‑CAL** accounts to the SCR (E.2 **BLP‑1d**; G.11).

**ABL — Autonomy‑Budget & Oversight Levels**
This section defines **graduated levels of agent autonomy** (level taxonomy), the **budget envelopes** they operate under, and the **review/approval** gates. Levels apply to any **Agentic Tool‑Use & Call‑Planning** context (see **C.Agent‑Tools‑CAL**).

| Level | Name                         | Freedom‑of‑Action (FoA)                  | Explore‑Share (default) | Typical Use                                     | Oversight Gate |
|------:|------------------------------|------------------------------------------|-------------------------|-------------------------------------------------|----------------|
| **L0** | Scripted Execution           | **Whitelist only**; fixed scripts        | 0                       | Compliance‑critical, deterministic procedures   | Engineer‑of‑Record (EoR) |
| **L1** | Constrained Sequencing       | Negative constraints; **single‑tool**    | ≤ 0.10                  | Low‑risk automation with bounded novelty        | EoR + Peer Review |
| **L2** | Supervised Autonomy          | Multi‑tool plans; bounded replanning     | 0.20 (±0.10)            | Ambiguous tasks; moderate budget                | Team Lead + Safety |
| **L3** | Auditable Autonomy           | Multi‑step, self‑replanning; adaptive    | 0.30 (±0.10)            | Production agents with learning under guard‑rails | Product + Safety + Legal |
| **L4** | Open‑Ended / Research Mode   | Broad FoA within sandbox & rails         | 0.40–0.50               | Illumination‑first exploration, sandboxes only  | Governance Board (Gov‑CAL) |

**Normative requirements by level.**
* **Budgets.** Each level **MUST** declare ceilings for **time / compute / cost / risk** and a FoA descriptor; units must be explicit (Resrc‑CAL). Budgets are **hard gates** at run‑time (C.Agent‑Tools‑CAL **ATC‑3**).
* **Assurance floors.** **B.3** WLNK minima on **F** and **R** apply at all levels; **CL penalties** for integration **increase** with level (B.3.3). Pre‑deployment **assurance deltas** MUST be recorded for L2+.
* **Exploration discipline.** `explore_share` MUST be explicit in the **CallPlan** (C.Agent‑Tools‑CAL **ATC‑4**). Deviations from defaults require DRR justification.
* **Provenance.** L1+ MUST emit a **CallGraph** with Service/Method editions, EmitterPolicyRef, budget deltas, and observation hooks (C.Agent‑Tools‑CAL **ATC‑5/6**).
* **BLP conformance.** For L2+, selection MUST apply **BLP** (E.2 **BLP‑2**) with **α/δ** tolerances declared in the plan policy. Any admitted heuristic requires a **Heuristic‑Debt** entry (E.2 **BLP‑4**).
* **Learning/Adaptation.** L3–L4 MAY enable **feedback‑driven adaptation** within E.5 Guard‑Rails and privacy controls; L0–L2 default **off** unless a DRR documents mitigation (E.2 **BLP‑5**).
* **Human‑in‑the‑Loop (HITL).** L0–L1 require **pre‑approval** of plans; L2 requires **sentinel‑triggered pausing** for review; L3 requires **periodic** review windows; L4 requires **continuous** telemetry review and **sandboxing**.

**Approval matrix (who can approve what).**
* **L0:** EoR or appointed maintainer.
* **L1:** EoR **and** peer reviewer (two‑person rule).
* **L2:** Team Lead **and** Safety representative.
* **L3:** Product Owner **and** Safety **and** Legal/Privacy.
* **L4:** **Gov‑CAL Board** (multi‑disciplinary) with documented scope, time‑boxed **trial budget**, and rollback criteria.

**Escalation / de‑escalation triggers.**
* **Escalate** level when repeated **BLP‑consistent** results show stable assurance within δ and budget adherence within α for ≥ **N_policy** runs (declare **N_policy** in the active profile); DRR **MUST** include slope evidence (E.2 **BLP‑1c**).
* **De‑escalate** level when: (i) sentinel breaches risk or budget, (ii) assurance drops below floors, (iii) policy changes, or (iv) a significant **heuristic‑debt** item expires without replacement.

**Conformance Checklist — E.3 ↔ BLP Interop**

| ID          | Requirement                                                                                                          | Purpose                          |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| **CC‑E3.10** | Precedence list includes **BLP** explicitly **below** E/E‑LOG and **above** product tactics; conflicts handled via **BLP‑waiver** discipline. | Makes BLP’s standing auditable. |
| **CC‑E3.11** | Every DRR that overrides BLP **MUST** include a **Scale‑Audit** (E.2 **BLP‑1**) and a **Heuristic‑Debt** entry (E.2 **BLP‑4**). | Prevents silent heuristic drift. |
| **CC‑E3.12** | Each agentic plan declares an **Oversight Level** (L0–L4) with explicit budgets, `explore_share`, and **E/E‑LOG EmitterPolicyRef**. | Aligns autonomy with assurance. |
| **CC‑E3.13** | L1+ executions emit **CallGraphs** with editioned policy/method ids and budget deltas; L3+ include adaptation status. | Ensures replayability & audit. |
| **CC‑E3.14** | Level changes follow **escalation/de‑escalation** triggers and are recorded with edition pins in the SCR. | Keeps autonomy under control. |

##### Consequences
*Positive* — Turns subjective debate into objective, traceable decisions; high‑impact conflicts surface early.

##### Rationale
The chosen taxonomy mirrors FPF’s layered dependency: **Governance** rules how change occurs; **Architecture** shapes what can exist; **Epistemology** secures meaning and trust; **Pragmatics** and **Didactics** ensure usefulness and learnability. Explicit override edges supply the flexibility experts need, while the default hierarchy keeps day‑to‑day design deterministic—a “living constitution” that remains both human‑intelligible and machine‑enforceable.

##### Relations
* **Depends on:** `pat:constitutional/vision`, `pat:constitutional/pillars`
* **Governs:** All subsequent patterns and DRRs; Guard‑Rail patterns reference CC‑PT.\

> *“A taxonomy sorts principles; precedence gives them order—together they convert debate into design.”*

### **E.4 — FPF Artefact Architecture \[A]**

##### Problem frame

The FPF ecosystem produces a wide range of artifacts, from timeless, normative principles to rapidly evolving pedagogical materials and executable tools. If these different types of artifacts are mingled without a clear architectural separation, the ecosystem becomes difficult to navigate, govern, and maintain. Users cannot easily distinguish binding rules from helpful advice, and the entire framework's release cycle becomes coupled to its most volatile component.

##### Problem

How can we structure the FPF ecosystem to ensure a clean separation of concerns between normative concepts, didactic materials, and executable tooling? A formal architecture is required to maintain conceptual purity, enable independent evolution of components, and provide a clear map for all stakeholders.

##### Forces

| Force | Tension |
| :--- | :--- |
| **Stability vs. Agility** | The conceptual core must evolve slowly and deliberately ↔ tools and tutorials must iterate quickly to keep pace with technology and user needs. |
| **Authority vs. Accessibility** | Users need to know which rules are normative and binding ↔ they also need accessible, non-normative guides to help them learn. |
| **Modularity vs. Cohesion** | The different artifact families must be able to evolve independently ↔ they must remain part of a single, coherent FPF ecosystem. |

##### Solution

The FPF ecosystem is formally stratified into three canonical **artefact families**. Each family has a distinct purpose and is governed by different rules, ensuring a clear separation of concerns. The interaction between these families is governed by the **Unidirectional Dependency Principle** (see Guard-Rail E.5.3).

1.  **The Conceptual Core (The Canon):** This family contains the **normative** pattern language of FPF. It is the single source of truth for all universal concepts, rules, and invariants. It is defined to be tool-agnostic and notation-independent. This family represents the timeless "law" of FPF.

2.  **The Tooling Reference:** This family contains **executable artifacts** that implement or verify the normative rules of the Core. This includes reference linters, simulators, and data schemas. This family is the "instrument" that makes the law of the Core operational.

3.  **The Pedagogical Companion:** This family contains **non-normative, didactic materials** designed to help humans learn and apply FPF. This includes tutorials, worked examples, and playbooks. This family is the "textbook" that explains both the law and the instruments.

##### Archetypal Grounding (System / Episteme)

*   **For a `U.System`:**
    *   **Conceptual Core:** Defines the universal pattern `U.System`.
    *   **Tooling Reference:** Provides a modeling language profile or a serialization schema for modeling systems.
    *   **Pedagogical Companion:** Provides a tutorial on how to model a water pump using that profile.

*   **For an `U.Episteme`:**
    *   **Conceptual Core:** Defines `U.Episteme` and the F-G-R characteristics.
    *   **Tooling Reference:** Provides the reference linting tool to automatically score epistemes.
    *   **Pedagogical Companion:** Provides a case study on how a scientific theory's R-score evolves over time.

##### Conformance Checklist

| ID | Requirement |
| :--- | :--- |
| **CC-E.4.1** | Every artifact in the FPF ecosystem **MUST** declare which of the three families (Core, Tooling, Pedagogy) it belongs to. |
| **CC-E.4.2** | The content of each artifact **MUST** be consistent with the defined purpose of its family (e.g., no normative rules in the Pedagogical Companion). |
| **CC‑E.4.3** | Artefacts in the Tooling or Pedagogy families SHALL NOT be imported by artefacts in the Conceptual Core. |

##### Consequences

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Clear Separation of Concerns:** Users and contributors can immediately identify the nature and authority of any given artifact. | **Requires Discipline:** Authors must be careful to place new content in the correct artifact family. |
| **Decoupled Release Cycles:** The Core can maintain a stable, slow release cadence, while the Tooling and Pedagogy artifact family can evolve rapidly. | - |
| **Architectural Clarity:** Provides a simple, powerful mental model for navigating the entire FPF ecosystem. | - |

##### Rationale

This pattern establishes the macro-architecture of the entire FPF ecosystem. By separating the timeless "why" and "what" (the Conceptual Core) from the practical "how" (Tooling) and the educational "how-to-learn" (Pedagogy), it creates a system that is simultaneously stable, agile, and accessible. This layered architecture is a proven pattern in large-scale systems, from the OSI model in networking to the structure of modern operating systems, and it is essential for FPF's long-term health and scalability.

##### Relations

*   **Instantiates:** **P-5 (Plugin Layering)** at a macro-level.
*   **Is Constrained by:** **E.5.3 (Unidirectional Dependency)**.
*   **Is Foundation For:** The entire authoring and governance model, as it defines the "territories" where different rules apply.

> *“A canon without a rationale is scripture; a rationale without a canon is gossip. FPF keeps both, fused in patterns.”*

###  E.5 · Four Guard‑Rails of FPF         \[A]

#### Problem frame  
FPF positions itself as a **timeless, universal “operating system for
thought.”**  Collaborative projects of this scope face four predictable
entropic pulls:

1. **Implementation gravity** – concept prose accretes tool jargon.  
2. **Notation lock‑in** – one diagram style becomes “the language.”  
3. **Convenience cycles** – quick fixes create reverse dependencies.  
4. **Disciplinary monoculture** – implicit bias colours “universal” rules.

Left unchecked, these forces erode Pillars **P‑1 Cognitive Elegance**,
**P‑4 Open‑Ended Kernel** and **P‑5 Plug‑in Layering**.

#### Problem  
Without explicit, non‑negotiable protectors the Conceptual Core would
slowly:

* entangle with transient technology terms,  
* hard‑freeze into a single dialect,  
* devolve into a tightly coupled “big ball of mud”,  
* betray its trans‑disciplinary promise.

#### Forces  

| Force | Tension |
|-------|---------|
| **Purity vs Pragmatism** | Preserve pristine concepts ↔ need real examples. |
| **Universality vs Convention** | Rules valid across domains ↔ convenience of one familiar notation. |
| **Modularity vs Integration** | Independent layers ↔ temptation to cross‑link for speed. |
| **Objectivity vs Perspective** | Neutral framework ↔ Transformers’ unavoidable cultural lens. |

#### Solution — the Four Guard‑Rails  
FPF establishes **four architecturally enforced guard‑rails** that every Core, Tooling, and Pedagogy artefact must obey.  They function as an “immune system” resisting each entropic pull.
**Scope note (conceptual, not lint).** These guard‑rails regulate the **architecture of thought**—concepts, claims, and their relations. They **do not** mandate tools, file formats, notations, or workflows; any linting or automation lives outside the Core and is optional, provided it preserves these conceptual constraints.


| # | Guard‑Rail | Protects against |
|---|------------|------------------|
| **GR‑1** | **DevOps Lexical Firewall** | Implementation, governance, automatisation and DevOps concerns gravity |
| **GR‑2** | **Notational Independence** | Notation lock‑in |
| **GR‑3** | **Unidirectional Dependency** | Convenience cycles |
| **GR‑4** | **Cross‑Disciplinary Bias Audit** | Disciplinary monoculture |

Concrete rules for each rail live in patterns **E.5.1 – E.5.4**.

#### Archetypal Grounding (System / Episteme)

| Guard‑Rail | `U.System` example | `U.Episteme` example |
|------------|-------------------|----------------------|
| GR‑1 | Definition of `U.System` never cites file formats or build scripts. | Definition of `U.Episteme` avoids naming specific proof engines. |
| GR‑2 | Pump boundary invariant is true in plain text or any diagram. | F‑G‑R semantics hold in algebraic or graph notation alike. |
| GR‑3 | A sizing helper imports Core invariants; Core never imports helper tutorials. | Learning guide cites R‑score; Core never cites guide. |
| GR‑4 | Bias audit removes thermo‑mechanical jargon from a “universal” pattern. | Audit replaces physics‑centric metaphors in a trust pattern. |

#### Conformance Checklist

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC‑GR.1** | Every new Core pattern **SHALL** cite, in its *Relations* section, the guard‑rail(s) it relies on or may affect. | Ensures traceability and deliberate rule interaction. |
| **CC‑GR.2** | Artefacts classified as Tooling or Pedagogy **MUST NOT** violate any rule in GR‑1 through GR‑4. | Keeps entropic forces outside the Conceptual Core. |
| **CC‑GR.3** | A revision to any guard‑rail pattern **REQUIRES** a Design‑Rationale Record that (a) states the reason, and (b) includes a Pillar‑impact analysis per E.3 precedence model. | Aligns evolution with higher‑level principles. |
| **CC‑GR.4** | The aggregate of guard‑rail rules **MUST** remain internally consistent and acyclic; no guard‑rail may override another without explicit precedence edges. | Preserves deterministic governance. |
| **CC‑GR.5** | Every Core pattern **MUST** anchor its primary subject with a declared **ReferencePlane** (`world | concept | episteme`) at first mention. | Keeps Core about “life” objects (extensional/intensional) rather than their paperwork, and aligns with CHR:ReferencePlane. |
*All CC‑GR duties are **conceptual**. Any automated checks are **informative only** and live in Tooling/Pedagogy.*

#### Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| **Long‑term integrity** – stops slow drift of the Core toward jargon, notation lock‑in, and hidden cycles. | Authors must run a guard‑rail checklist before submission. *Mitigation:* template auto‑inserts the checklist. |
| **Stable yet evolvable ecosystem** – Core stays timeless while Tooling & Pedagogy can iterate rapidly. | Early stage contributions may feel constrained; examples in the Pedagogical Companion show compliant paths. |
| **Trust & auditability** – stakeholders can verify the framework’s purity independently. | Adds overhead to governance; justified by safety and longevity. |

#### Rationale  
A constitution without enforcement degrades into *dead‑letter rules*.  
The four guard‑rails translate abstract Pillars into **concrete, testable
constraints**.  Grouping them under one umbrella pattern:

* gives newcomers a single “safety index” to consult,  
* makes compliance binary (*pass / amend*),  
* provides a stable anchor for future automated conformance tools—without
  mentioning any specific engine, thus honouring GR‑1 itself.

They collectively instantiate Pillars **P‑1**, **P‑2**, **P‑4**, **P‑5**
and reinforce the precedence order defined in **E.3**.

#### Relations

* **Comprises:**  
  * `pat:guard/devops‑firewall` (E.5.1) – GR‑1  
  * `pat:guard/notational‑independence` (E.5.2) – GR‑2  
  * `pat:guard/unidirectional‑dependency` (E.5.3) – GR‑3  
  * `pat:guard/bias‑audit` (E.5.4) – GR‑4
* **Depends on:**  
  * `pat:constitution/pillars` (E.2)  
  * `pat:constitution/principle‑taxonomy` (E.3)
* **Constrains:** every Core, Tooling, and Pedagogy artefact; all DRRs.

####  E.5.1 · DevOps Lexical Firewall \[D]

##### Problem frame  
The FPF Core is meant to remain valid across decades and technology
generations.  Implementation details—file formats, build pipelines,
runtime flags—evolve rapidly and differ between domains.  When such
terms invade normative prose, the Core ages as quickly as the tools it
mentions.

##### Problem  
*Conceptual erosion*: a rule that cites a transient technology becomes
obsolete when that technology fades, forcing unnecessary Core revisions
and fragmenting historical audits.

##### Forces  

| Force | Tension |
|-------|---------|
| **Timelessness** | Concepts must survive tool turnover. |
| **Pedagogic clarity** | Examples need concreteness ↔ too much concreteness hard‑codes technology. |
| **Cross‑domain reach** | Physical‑system engineers and knowledge‑theorists use different stacks. |

##### Solution  
Establish a **Lexical Firewall** around the **Conceptual Core** *(conceptual constraint; not a build‑time linter)*:

1. **Forbidden lexicon**  
   Normative patterns **SHALL NOT** contain tool‑or file‑specific words
   (e.g. protocol keywords, file extensions, IDE commands).  
   Permissible wording: “a reference parser”, “a serialisation schema”.

2. **Indirection rule**  
   When a Core concept needs an executable illustration, the pattern
   cites the **Tooling Reference family** artefact by *conceptual name*,
   never by concrete path or syntax.

3. **Glossary pointer**  
   If an unavoidable technical term appears, it is defined in a *Tooling Glossary* outside the Core and referenced by conceptual alias—not embedded.
*Non‑normative automation.* Machine checks **MAY** exist in Tooling; they are advisory and **MUST NOT** be imported into the Core.

##### Archetypal Grounding (System / Episteme)

| Scenario | `U.System` example | `U.Episteme` example |
|----------|-------------------|----------------------|
| **Normative text** | “A system boundary must expose at least one conserved‑quantity flow.” (No mention of modelling language.) | “An episteme records its F–G–R coordinates.” (No mention of proof syntax.) |
| **Illustrative link** | A modelling profile resides in the Tooling family; Core cites it as “the reference system‑profile”. | A linting routine lives in Tooling; Core cites it as “the reference episteme‑checker”. |

##### Conformance Checklist

| ID | Requirement |
|----|-------------|
| **CC‑LFW.1** | A Core pattern **SHALL** fail review if it contains implementation‑specific tokens. |
| **CC‑LFW.2** | References to executable artefacts **MUST** use conceptual names, not file paths or command strings. |
| **CC‑LFW.3** | Pedagogical examples inside Core **MAY** describe behaviour, but **MUST NOT** embed code snippets. |

##### Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| Core stays evergreen and cross‑domain. | Authors must relocate concrete examples to Tooling or Pedagogy. |
| Reviewers can machine‑scan for banned tokens. | Requires a small vocabulary allow‑list; maintained in Tooling Guide. |

##### Rationale  
Language shapes thought.  By firewalling transient jargon, we uphold
**P‑1 Cognitive Elegance** (clarity), **P‑2 Didactic Primacy** (domain‑neutral
exposition) and **P‑5 Plug‑in Layering** (clean separation between Core
and Tooling).  The rule is content‑agnostic and thus itself immune to the
very decay it prevents.

##### Relations  
* **Parent umbrella:** `pat:constitution/guard‑rails` (E.5)  
* **Constrains:** every pattern in Conceptual Core  
* **Instantiates pillars:** P‑1, P‑2, P‑5
  
  ####  E.5.2 · Notational Independence \[D]

##### Problem frame  
FPF concepts must travel across academic disciplines, modelling tools,
and future notations we cannot yet foresee. If a normative pattern binds
its *meaning* to one diagram style, file syntax, or markup dialect, the
concept ages as soon as the notation does.

##### Problem  
*Semantic lock‑in*: when a definition relies on a particular glyph set or
diagram grammar, alternative communities either translate it—risking
drift—or ignore FPF altogether.

##### Forces  

| Force | Tension |
|-------|---------|
| **Expressiveness** | Diagrams and formal grammars aid precision ↔ they should never become the definition itself. |
| **Longevity** | A 20‑year horizon ↔ notation life‑cycles of 3‑5 years. |
| **Cross‑discipline adoption** | Mathematicians prefer algebraic syntax; engineers prefer schematics. |

##### Solution — Notational Independence Guard‑Rail *(conceptual; semantics over syntax; not a notation mandate)*

1. **Semantics primacy**  
   Normative content **SHALL** define concepts in linguistic form first
   (plain English + mathematics if needed). Visual or syntax examples
   are secondary illustrations.

2. **Equivalence clause**  
   When an official alternate notation exists, the pattern must state:
   *“Representation A and Representation B are semantically equivalent
   under mapping M.”*

3. **Reference indirection**  
   If the Core cites a diagram, it does so by *conceptual role*
   (“reference boundary schematic”) rather than by file or syntax name.

4. **Conceptual prefix neutrality**  
   FPF **conceptual prefixes** (e.g., `U.`, `Γ_`, `ut:`, `tv:`, `ev:`, `mero:`) are  **cognitive namespaces**, not syntax tokens. Core patterns **MUST NOT**  tie their meaning to any concrete serialisation or URI scheme for these prefixes; any expansions are **illustrative only** and live in Tooling or Pedagogy.

5. **Cards and other "forms"**
Cards, tables and other "forms" exist in FPF core only as conceptual model, not as data model, thus no need to data-related notation or notation for lint. Comformance checklist and quards is also conceptual, argumentation like "this will ease machine check" is forbidden, no machine checking is intended in core; machine checks and linters live only in Tooling.

##### Archetypal Grounding (System / Episteme)

| Scenario | `U.System` example | `U.Episteme` example |
|----------|-------------------|----------------------|
| Definition | Boundary of a pump is expressed in prose plus set notation; a diagram is illustrative. | F‑G‑R characteristics defined textually; a triple‑store serialisation is illustrative. |
| Alternate rendering | Same pump semantics rendered in a lattice diagram or a tabular sheet remain valid. | R‑scores plotted in a heatmap or listed in CSV remain equivalent. |

##### Conformance Checklist

| ID | Requirement |
|----|-------------|
| **CC‑NI.1** | A Core pattern **MUST NOT** embed semantics that hinge on one specific notation. |
| **CC‑NI.2** | Illustrative renderings **SHALL** be marked “informative”. |
| **CC‑NI.3** | When multiple official renderings exist, the pattern **MUST** declare the semantic mapping between them. |
| **CC‑NI.4** | If a **conceptual prefix** appears in Core, its expansion (if shown) **SHALL** be marked *informative* and **MUST NOT** be required to interpret the semantics. |

##### Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| Ensures FPF survives notation turnover. | Authors invest time describing mappings; mitigated by reusable mapping templates. |
| Lowers entry barrier for domains using different diagram traditions. | Excessive illustrations can bloat pages; guidance in Pedagogical Companion limits scope. |

##### Rationale  
Language and diagrams are tools, not truths. By elevating semantics over
syntax, FPF maintains **P‑1 Cognitive Elegance** and **P‑2 Didactic
Primacy** while safeguarding **P‑5 Plug‑in Layering**: tooling layers can
add new renderers without Core edits.

##### Relations  
* **Parent umbrella:** `pat:constitution/guard‑rails` (E.5)  
* **Constrains:** every normative Core pattern and official alternate rendering  
* **Instantiates pillars:** P‑1, P‑2, P‑5

####  E.5.3 · Unidirectional Dependency \[D]

##### Problem frame  
FPF separates artefacts into stable **Conceptual Core**, executable
**Tooling Reference**, and fast‑evolving **Pedagogical Companion** (see
E.4 Artefact Architecture).  If dependencies can point *both* ways,
volatile layers will eventually drag the Core into rapid revision
cycles or introduce domain‑specific bias.

##### Problem  
*Architectural gravity*: a tutorial or helper script adds a new feature,
Core patterns import it “temporarily,” and within months the supposedly
timeless layer depends on transient assets—breaking Pillar **P‑5
Plug‑in Layering**.

##### Forces  

| Force | Tension |
|-------|---------|
| **Agility vs Stability** | Tooling must iterate quickly ↔ Core must remain slow and deliberate. |
| **Reuse vs Isolation** | Authors want to reuse helper concepts ↔ Core cannot depend on volatile code. |
| **Simplicity** | Rule must be testable and unambiguous ↔ must allow legitimate upward imports. |

##### Solution — One‑Way, Acyclic Imports  
Define a strict **partial order** over artefact families **and guard meaning flow** (see **E.10 V‑1**): imports point only **upward** in stability, and **no Core semantics** may derive from Tooling/Pedagogy. No linters or machine checking in Conceptual Core.

Pedagogical Companion  ⟶  Tooling Reference  ⟶  Conceptual Core

1. **Allowed edges**  
   Dependencies **MAY** point **only upward** (toward greater semantic
   stability). No cycle is ever permitted.

2. **No downward import**  
   Core artefacts **SHALL NOT** import Tooling or Pedagogy artefacts.
   Tooling artefacts **SHALL NOT** import Pedagogy artefacts.

3. **Future layers**  
   Any new family is inserted below an existing one or becomes part of
   the Tooling or Pedagogy strata; the ordering extends accordingly.

##### Archetypal Grounding (System / Episteme)

| Layer | `U.System` illustration | `U.Episteme` illustration |
|-------|------------------------|---------------------------|
| Core | Definition of `U.System` and boundary invariant. | Definition of F‑G‑R characteristics. |
| Tooling | “Reference system‑profile” that checks boundary flow; *imports* Core invariants. | “Episteme‑scoring routine” that calculates R‑score; *imports* Core characteristics. |
| Pedagogy | Tutorial using the system‑profile to model a pump; *imports* profile and Core term. | Case study explaining R‑score evolution; *imports* scoring routine and Core term. |
| **Forbidden** | Core pattern importing measurement script. | Core pattern importing R‑score web dashboard. |

##### Conformance Checklist

| ID | Requirement |
|----|-------------|
| **CC‑UD.1** | Dependency graph among all artefacts **MUST** be acyclic. |
| **CC‑UD.2** | An artefact **SHALL** import only from its own family or any family above it in the order. |
| **CC‑UD.3** | A DRR that introduces a downward edge **SHALL** be automatically rejected. |

##### Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| Core stays free of tool churn and tutorial bias. | Authors must create abstraction layers in Tooling instead of inserting hooks into Core. |
| Release cadence decoupled: Core (slow), Tooling (medium), Pedagogy (fast). | Slight duplication when multiple tools target same concept; mitigated by shared Core definitions. |

##### Rationale  
One‑way import graphs are a proven safeguard in operating systems
(kernel vs user land) and layered protocols. Here the rule operationalises
Pillars **P‑4 Open‑Ended Kernel** and **P‑5 Plug‑in Layering**, ensuring
that innovation happens “below” without contaminating the timeless Core.

##### Relations  
* **Parent umbrella:** `pat:constitution/guard‑rails` (E.5)  
* **References layer definition:** `pat:constitution/artefact‑architecture` (E.4)  
* **Instantiates pillars:** P‑4, P‑5  
* **Constrains:** All artefact imports recorded in DRRs or SCRs

#### E.5.4 — Cross‑Disciplinary Bias Audit** \[D]

##### Problem frame  
FPF calls itself trans‑disciplinary, but every author carries implicit
metaphors from a home domain. If those metaphors leak into “universal”
patterns, practitioners from other fields disengage or mis‑interpret the
rules.

##### Problem  
Unrecognised bias hides in wording, examples, unit choices or principle
weighting. Once embedded in normative language, such bias is hard to
remove and contradicts Pillars **P‑2 Didactic Primacy** and **P‑8
Cross‑Scale Consistency**.

##### Forces  

| Force | Tension |
|-------|---------|
| **Neutrality** | One voice for all disciplines ↔ need for relatable examples. |
| **Conciseness** | Audit guidance must be brief ↔ must cover multiple bias types. |
| **Longevity** | Guidance must survive emergence of new domains. |

##### Solution — Principle‑Taxonomy‑Guided Bias Audit  

1. **Bias‑Lens set**  
   Every normative pattern is assessed through **five lenses** that match the
   Principle classes from **E.3**:  
   `Gov`, `Arch`, `Onto/Epist`, `Prag`, `Did`.

2. **Equilibrium question**  
   For each lens ask:  
   *“Does the pattern over‑privilege this class or silence it?”*  
   *Examples:*  
   *   Over‑reliance on `Onto/Epist` precision may ignore `Prag` cost.  
   *   Dominant `Arch` metaphors may alienate `Did` audiences.

3. **Scope‑or‑Balance rule**  
   * If imbalance is found and universality is intended, re‑phrase to
     restore balance.  
   * If imbalance is intentional (domain‑specific pattern), mark the
     scope explicitly: *“Applies primarily to thermodynamic systems.”*

4. **Audit trace**  
   The pattern carries a short **Bias‑Annotation** paragraph recording
   which lenses were tested and any scoping statement. No workflow checklists or
   reviewer metadata or other data and data format and data governance tips is stored in the Core.

##### Archetypal Grounding (System / Episteme)

| Bias lens | Example imbalance | Conceptual correction |
|-----------|------------------|-----------------------|
| `Arch` vs `Did` | Pump pattern uses abstract category theory terms. | Add plain‑language boundary narrative or move abstraction to appendix. |
| `Onto/Epist` vs `Prag` | Episteme trust score defined with complex logic but no guidance on empirical cost. | Add pragmatic note on evidence collection burden or scope the pattern. |

##### Conformance Checklist

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC‑BA.1** | Each Core pattern **SHALL** include a *Bias‑Annotation* listing the five lenses and any declared scope limitation. | Ensures explicit reflection on bias. |
| **CC‑BA.2** | A pattern labelled “universal” **MUST NOT** privilege a single lens without justification or scoping note. | Preserves trans‑disciplinary integrity. |
| **CC‑BA.3** | If scope is declared, the pattern **SHALL** reference the mapping or rationale that enables cross‑domain translation. | Keeps pathways open for other calculi. |
| **CC‑BA.4 (QD‑triad evidence for “universal”).** | Any pattern that labels itself **“universal”** SHALL cite **A.8 CC‑UC 1 + CC‑UC 2** and attach the **QD evidence** (Diversity_P + IlluminationSummary, with edition and binning) or else **scope** the claim to its home Context. | preserves domain quality diversity |

##### Consequences  

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| Neutral, inclusive language attracts wider adoption. | Authors spend a few extra lines on Bias‑Annotation; mitigated by template snippet. |
| Bias is surfaced at writing time, not after publication. | — |

##### Rationale  
Coupling the audit directly to the Principle Taxonomy keeps the guard‑rail
**concept‑driven**, not workflow‑driven. No mention of review boards,
CI‑jobs, or checklists appears in the Core; such mechanics belong in the
Tooling Guide. This guard‑rail therefore satisfies **GR‑1** (Firewall)
while securing Pillars **P‑2, P‑7 Pragmatic Utility, P‑8**.

##### Relations  
* **Parent umbrella:** `pat:constitution/guard‑rails` (E.5)  
* **Depends on:** `pat:constitution/principle‑taxonomy` (E.3)  
* **Constrains:** All normative patterns claiming universality
  
### E.6 · Didactic Architecture of the Specification \[D]

#### Problem frame  
FPF addresses readers from at least two characteristics of diversity:

* **Disciplinary** – systems engineers, knowledge scientists, ethicists.  
* **Experience** – newcomers need intuition; experts need rigour.

Past drafts mixed governance mandates with domain examples, producing a
steep learning curve and repeated “forward‑reference” detours.

#### Problem  
If core ideas are buried under formalism or scattered across parts,
readers either give up or misuse the framework. We need a **fixed
narrative scaffold** that guides cognitive load from low to high while
keeping normative sections discoverable.

#### Forces  

| Force | Tension |
|-------|---------|
| **Cognitive Load** | Early clarity ↔ eventual formal depth. |
| **Conceptual Integrity** | Foregoing examples risks abstraction ↔ too many examples delay axioms. |
| **Uniform Flow** | Single, predictable roadmap ↔ flexibility for future parts. |

#### Solution — “On‑Ramp to Archetypes first, Authoring last” sequence  

The "On-Ramp First" Macro-Structure: The specification is ordered to create a smooth cognitive ramp:
* It begins with an informal, non-normative Preface (The On-Ramp), which uses storytelling and concrete examples (System and Episteme) to build intuition.
* It then proceeds through the normative Parts (A-D), moving from the foundational kernel to the rich patterns of trans-disciplinary reasoning.
* It concludes with the authoring rules (Part E) and appendices, ensuring that this "meta" content does not obstruct the primary learning path.

1. **Preface (On‑Ramp)**  
   Informal tour; introduces `U.System` and `U.Episteme` via concrete
   stories before any normative language appears.

2. **Part A Kernel**  
   Minimal holonic ontology and the Transformer principle give readers
   the essential vocabulary.

3. **Part B Trans‑disciplinary Reasoning**  
   Tell‑Show‑Show pedagogy: universal rule → Sys‑CAL example →
   KD‑CAL example.

4. **Part C Architheories**  
   Domain‑specific calculi expand on the examples already seen.

5. **Part D Ethics & Conflict Optimisation**  
   Shows reflective patterns only after readers grasp holonic reasoning.

6. **Part E Authoring**  
   Constitution, guard‑rails, and contributor rules come last; novices
   can postpone reading.

7. **Appendices (Annexes)**  
   Tutorials, tooling guides, and migration scripts live here.

#### Archetypal Grounding (System / Episteme)

| Narrative layer | First sight of `U.System` | First sight of `U.Episteme` |
|-----------------|---------------------------|-----------------------------|
| Preface | Coffee‑machine story (pump as system). | Meta‑analysis story (study bundle as episteme). |
| Part A | Formal definition inherits boundary invariant. | Formal definition inherits F‑G‑R coordinates. |
| Part B Tell‑Show‑Show | Γ\_sys example: assemble pump. | Γ_epist example: merge study bundle. |

#### Conformance Checklist

| ID | Requirement |
|----|-------------|
| **CC‑DA.1** | Each Part **SHALL** open with a one‑paragraph situational “hook” before formal text. |
| **CC‑DA.2** | Every `[A]` pattern **MUST** implement Tell‑Show‑Show: universal rule plus System & Episteme illustrations. |
| **CC‑DA.3** | Governance patterns (**Part E**) **SHALL NOT** appear before the Kernel in the main document flow. |

#### Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| Smooth learning curve; readers can stop at their needed depth. | Template discipline required; mitigated by authoring guide (E.8). |
| Reduces forward‑reference clutter; each concept is primed before formal use. | Preface evolves when new archetypes added; handled via On‑Ramp revision DRR. |

#### Rationale  
Educational research shows retention improves when abstract rules are
immediately paired with contrasting illustrations. By fixing the reading
order and mandating Tell‑Show‑Show inside every `[A]` pattern, FPF
embeds pedagogy into its architecture, realising Pillars **P‑2 Didactic
Primacy** and **P‑1 Cognitive Elegance** without weakening rigour.

#### Relations  
* **Depends on:** `pat:constitution/guard‑rails` (GR‑1 ensures example jargon stays outside Core).  
* **Constrains:** Placement of all Parts, patterns, and appendices.  
* **Instantiates pillars:** P‑1, P‑2
  
###  E.7 · Archetypal Grounding Principle \[D]

#### Problem frame  
Universal rules are powerful only when readers can grasp them. In FPF the
Conceptual Core speaks in substrate‑agnostic language: `U.Holon`,
Γ‑aggregation, MHT emergence. Practitioners need to “see” those rules in
familiar matter—physical hardware or bodies of knowledge—before they can
reuse them.

#### Problem  
A purely abstract statement risks two failures:

1. **Didactic failure** – readers dismiss the pattern as “too meta,”
   violating Pillar **P‑2 Didactic Primacy**.  
2. **Unproven universality** – without cross‑domain instantiation the rule
   remains an untested claim.

#### Forces  

| Force | Tension |
|-------|---------|
| **Universality vs Concreteness** | Abstract law ↔ concrete example. |
| **Brevity vs Clarity** | Spec should stay concise ↔ dual examples add length. |
| **Rigour vs Accessibility** | Formal semantics ↔ intuitive narrative. |

#### Solution — mandatory *Archetypal Grounding* subsection  

Every architectural pattern (`[A]`) **SHALL** include a dedicated
section, titled exactly **“Archetypal Grounding,”** that *shows* how the
abstract law SCRs in FPF’s two canonical holon flavours:

1. **`U.System`** – the archetype of a **physical, operational holon**.  
2. **`U.Episteme`** – the archetype of an **abstract, epistemic holon**.

This enforces a repeatable **Tell‑Show‑Show** rhythm:

| Stage | Content |
|-------|---------|
| **Tell** | `Solution` section states the universal rule. |
| **Show #1** | `Archetypal Grounding` – concrete `U.System` example. |
| **Show #2** | Same section – parallel `U.Episteme` example. |

#### Archetypal Grounding (of this pattern itself)

| Universal rule | `U.System` instantiation | `U.Episteme` instantiation |
|----------------|--------------------------|----------------------------|
| “Every `[A]` pattern requires grounding.” | Pattern *D.1 Algebra of Aggregation* illustrates Γ\_sys on assembling a water pump. | The same pattern illustrates Γ_epist on merging a meta‑analysis. |

#### Conformance Checklist

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC‑AG.1** | Every architectural (`[A]`) pattern in Parts A, B, C, D, E **SHALL** contain a subsection headed exactly *“Archetypal Grounding”*. | Guarantees consistent Tell‑Show‑Show rhythm. |
| **CC‑AG.2** | The Archetypal Grounding subsection **MUST** illustrate the rule with both `U.System` *and* `U.Episteme`. | Demonstrates trans‑disciplinary reach. |
| **CC‑AG.3** | If a rule intentionally applies to only one substrate, the subsection **SHALL** state the scope limitation and justify it against the five Principle‑Taxonomy lenses (`Gov`, `Arch`, `Onto/Epist`, `Prag`, `Did`). | Prevents silent bias; links to Bias‑Audit guard‑rail. |
| **CC‑AG.4** | Patterns lacking a compliant Archetypal Grounding subsection **MAY NOT** progress to “Accepted” status. | Enforces discipline without referring to workflow mechanics. |

#### Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| **Immediate clarity** – readers see abstract laws in action. | Patterns grow by one short table; mitigated by consistent template snippet. |
| **Proof of universality** – every rule is self‑documenting across substrates. | Authors must think cross‑domain; fosters richer patterns. |
| **Narrative cohesion** – recurring System/Episteme protagonists create a memorable storyline. | — |
|Built-in Proof of Universality: The specification consistently demonstrates its trans-disciplinary claims, building trust and credibility. | — |

#### Rationale  
Tell‑Show‑Show is a proven pedagogical sequence. By making it normative,
FPF hard‑codes **P‑2 Didactic Primacy** into the fabric of every `[A]`
pattern while still honouring **P‑1 Cognitive Elegance**—the grounding
section replaces brittle ad‑hoc anecdotes with a disciplined dual
example. Linking scope‑justification to the five Principle lenses ties the
pattern to the **Taxonomy‑Guided Bias Audit** and keeps governance
language out of the Core.

#### Relations  

* **Implements macro flow:** `pat:authoring/didactic‑architecture` (E.6)  
* **References base types:** `pat:kernel/holon` (A.1) (`U.System`, `U.Episteme`)  
* **Interacts with bias guard‑rail:** `pat:guard/bias‑audit` (E.5.4) via CC‑AG.3  
* **Constrains:** Authoring template in `pat:authoring/pattern‑template` (E.8)

###  E.8 · FPF Authoring Conventions & Style Guide   \[A]

#### Problem frame  
FPF grows through the addition of patterns written by authors from many
disciplines.  Without a shared structure *and* voice the framework would
fracture, violating Pillars **P‑1 Cognitive Elegance** and
**P‑2 Didactic Primacy**.

#### Problem  
*Structural drift* and *stylistic fragmentation* threaten three qualities:

1. **Comparability** – readers cannot align patterns lacking common
   headings.  
2. **Narrative cohesion** – prose swings from dry jargon to informal
   blog style.  
3. **Auditability** – missing sections hide safety checks
   (Archetypal Grounding, Bias‑Annotation).

#### Forces  

| Force | Tension |
|-------|---------|
| **Uniformity vs Expressiveness** | Consistent template ↔ freedom for diverse domains. |
| **Rigor vs Readability** | Formal precision ↔ engaging prose. |
| **Brevity vs Completeness** | Concise patterns ↔ mandated safety subsections. |

#### Solution — One template, enriched by style principles  

##### 1 · Canonical Pattern Template  
All patterns **SHALL** follow this section order (headings verbatim).
Sections marked ✱ are **mandatory for `[A]`**, optional for `[D]`.

1. Header block (ID, Type, Status)
2. Problem frame
3. Problem
4. Forces
5. Solution
6. ✱ Archetypal Grounding (mandatory `[A]`; optional `[D]`)
7. Bias‑Annotation
8. Conformance Checklist
9. Consequences
10. Rationale
11. SoTA‑Echoing (post‑2015 practice alignment)
12. Relations
13. Footer marker

*Unification note:* historic A‑ and D‑templates differed only by the Grounding and SoTA Echoing heading; optionality preserves clarity without duplication.
Problem frame in alexandrian pattern canon historically called "context", FPF do not use this label due to overloading with Context a Plain label of a U.BoundedContext.

##### 2 · Stylistic Principles (S‑0 ... S‑13)

| # | Principle | Guideline |
|---|-----------|-----------|
| S‑0 | Narrative Seven-Step Heuristic | Authors are encouraged to structure major paragraphs or subsections using the seven‑step mnemonic |
| S‑1 | Density without Jargon | Short declarative sentences; tool names belong in Pedagogy/Tooling. |
| S‑2 | Internal Cohesion | Inline references to Pillars and related patterns. |
| S‑3 | Embedded Mini‑Definitions | Gloss a new term in parentheses on first appearance. |
| S‑4 | Contextualisation | Brief historical or disciplinary lineage anchors. |
| S‑5 | Prophylactic Clarification | Pre‑empt common misreadings inside the prose. |
| S‑6 | Quotable Closers | Finish Solution or Consequences with a memorable aphorism. |
| S‑7 | Generative over Prescriptive | Present rules as enabling constraints, not bureaucracy. |
| S‑8 | Trans‑disciplinary Tie‑ins | Illustrate using at least two distinct fields. |
| S‑9 | Physical Grounding Reference | Link abstractions to a `Transformer` or physical process. |
| S‑10 | Punchy Blocks | ≤ 5 sentences per paragraph; lists for clarity. |
| S‑11 | Narrative Flow | Ensure sections read as a continuous story, not bullet soup. |
| S‑12 | Full sentences over tags | Avoid “keyword soup”. Each list item MUST contain a subject and a verb; prefer 2–4 sentence micro‑paragraphs to bare tag lists. |
| S‑13 | SoTA‑Echo craft | In the SoTA‑Echoing section, present: **claim → practice → source → alignment → adoption status (adopt/adapt/reject)**; cite Bridges & CL when crossing Contexts/planes. |

Authors use the principles as a *scaffold*, not a straitjacket: the goal
is coherent, engaging insight.

** S-0 (Narrative Flow Heuristic) explanation**
Narrative flow recommended follow these steps: **Hook → Frame → Weave → Anchor → Bridge → Flow → Close**.

Brief explanations: 
| Step       | Purpose in a paragraph/section                             |
| ---------- | ---------------------------------------------------------- |
| **Hook**   | Grab attention with a vivid image or paradox.              |
| **Frame**  | State the specific question or problem space.              |
| **Weave**  | Connect to earlier patterns or Pillars.                    |
| **Anchor** | Tie to a concrete System/Episteme or physical process.     |
| **Bridge** | Show the implication for the upcoming claim or rule.       |
| **Flow**   | Deliver the formal content or argument.                    |
| **Close**  | End with a quotable line or payoff that reinforces memory. |

Narrative Flow Heuristic also operationalises S‑1 (Density w/o Jargon), S‑2 (Internal Cohesion), S‑4 (Contextualisation), and S‑6 (Quotable Closers).

##### Autonomy authoring stub (mandatory when autonomy is claimed)
If a pattern or example claims **autonomy** for any Role/Method/Service:
1) Add a subsection **“Autonomy (RoC‑E.16)”** that lists:
   * `AutonomyBudgetDeclRef` (id, version, Scope (G), Γ_time),
   * `Aut-Guard policy-id`,
   * `OverrideProtocolRef` (SpeechAct names, SoD),
   * pointer to where **Green‑Gate** applies in the Method steps,
   * where **AutonomyLedgerEntry** is recorded on `U.Work`.
2) Include one **Tell‑Show‑Show** vignette that demonstrates **depletion** and **override** handling.
3) Use **LEX‑BUNDLE** terms (Scope (G), Γ_time, Role/Method/Work). Avoid “validity”, “process”, “actor” unless mapped to kernel types.

#### Archetypal Grounding (System / Episteme)

| Template element | `U.System` illustration | `U.Episteme` illustration |
|------------------|------------------------|---------------------------|
| Section order | Pump‑assembly pattern follows 1‑to‑11 headings. | Meta‑analysis pattern follows same headings. |
| S‑1 Density w/o Jargon | “The pump boundary is the sealing plane.” | “An episteme’s F‑score captures falsifiability.” |
| Hook‑Weave‑Anchor | Opens with field anecdote → links Γ‑core → anchors to motor torque. | Opens with historical paradox → links MHT → anchors to peer‑review data. |

#### SoTA‑Echoing  *(normative; lineage & deltas to contemporary State‑of‑the‑Art)*

**Purpose.** Make each pattern’s relationship to contemporary practice explicit and comparable without importing tooling or data governance. This section is prose‑first and notation‑independent.

**Minimum contents (obligations).**
1) **Sources (post‑2015).** Cite ≥ 3 primary SoTA sources (standards, seminal papers, widely‑used frameworks), at least **two independent Traditions** (per G‑cluster).  
2) **Practice alignment.** For each cited item, state **what is adopted, adapted, or rejected**, and **why** (in 2–4 sentences).  
3) **Scale legality.** If numeric operations are implied, **bind** them to **CG‑Spec** (Characteristic ids, Scale/Unit/Polarity, SCP/Γ‑fold) and declare partial‑order stance; **no scalarisation of partial orders**.  
4) **Cross‑Context reuse.** Any reuse across `U.BoundedContext` **SHALL** cite **Bridge id + CL** with loss notes; penalties route to **R_eff only** (F/G invariant). For plane crossings, publish **Φ(CL)**/**Φ_plane** policy‑ids.  
5) **Lexical hygiene.** Do **not** use the verb/noun “mapping” outside E.10’s reserved sense; prefer **alignment**/**Bridge**/**relation** language.

**Writing guidance (readability).**
*Write short paragraphs, not tag lists.* For each Tradition, provide (a) a one‑sentence capsule of the practice, (b) a one‑sentence comparison to the pattern’s Solution, (c) a one‑sentence adoption status with reason. Where helpful, add one **System** and one **Episteme** micro‑example (Tell–Show–Show).

**Format: human‑first.** A small table is allowed, but each row **MUST** be accompanied by 1–2 sentences as above. Vendor/tool tokens, file formats, or data schemas are out of scope.

##### Conformance Checklist  

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC‑SG.1** | Every new pattern **SHALL** follow the section order defined in the Canonical Template (Context → … → Relations). | Guarantees structural comparability and machine‑parsing. |
| **CC‑SG.2** | Architectural patterns (`[A]`) **MUST** include an *Archetypal Grounding* section; Definitional patterns (`[D]`) **MAY** omit it **only** if the Bias‑Annotation states a domain‑specific scope. | Enforces Tell‑Show‑Show unless formally limited. |
| **CC‑SG.3** | The *Bias‑Annotation* section **SHALL** cite the five Principle‑Taxonomy lenses and declare either “Universal” or an explicit scope limitation. | Keeps cross‑disciplinary neutrality explicit (ties to Guard‑Rail 4). |
| **CC‑SG.4** | Normative sentences **MUST** use keywords *SHALL*, *SHALL NOT*, *MUST*, *MAY* exactly as defined; synonyms are prohibited. | Prevents ambiguity for auditors and tooling. |
| **CC‑SG.5** | Pattern prose **SHOULD** demonstrate adherence to Style Principles **S‑0 … S‑13**; reviewers are empowered to request revision when clarity or didactic quality suffers. | Embeds common narrative voice without rigid policing. |
| **CC‑SG.6 (SoTA‑Echo required for `[A]`).** | Architectural patterns **SHALL** include a **SoTA‑Echoing** section as specified above; Definitional patterns **SHOULD** include it when cross‑disciplinary comparability is at issue. | Ensures contemporary situating of rules. |
| **CC‑SG.7 (Post‑2015, multi‑Tradition).** | SoTA‑Echoing **SHALL** cite ≥ 3 post‑2015 sources across ≥ 2 Traditions; each item **MUST** carry adoption status (adopt/adapt/reject) with reason. | Guards against monoculture; makes intent explicit. |
| **CC‑SG.8 (Bridge & CL on reuse).** | Any cross‑Context or plane reuse mentioned in SoTA‑Echoing **MUST** cite **Bridge id + CL** and (if planes differ) **Φ(CL)**/**Φ_plane** policy‑ids; penalties **→ R_eff** only. | Safe, auditable reuse. |
| **CC‑SG.9 (Lexical hygiene).** | The term **mapping** **SHALL NOT** appear in SoTA‑Echoing except in the precise E.10 sense; use **alignment/Bridge/relation** instead. | Avoids overloading reserved vocabulary. |
| **CC‑SG.10 (No keyword soup).** | SoTA‑Echoing items **MUST** be written as sentences (not bare noun phrases); bullet lists are acceptable only with complete clauses. | Improves didactic quality and comparability. |

##### Consequences  

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| **Predictable skeleton** – readers instantly know where to find context, forces, and criteria. | Limits author freedom in macro layout; mitigated by flexibility inside the Solution subsection. |
| **Cohesive voice** – S‑principles give FPF a recognisable style, aiding memorability. | Reviewers must read for style, not only semantics; checklists ease load. |
| **Embedded pedagogy** – Tell‑Show‑Show and Hook → Close heuristics turn the spec into a self‑teaching text. | Slightly longer patterns; justified by better comprehension and fewer clarifying DRRs. |

##### Rationale  
Structure and style function as FPF’s *grammar*. By unifying what were
once separate “template” and “style guide” patterns, authors face a
single reference point that satisfies:

* **P‑1 Cognitive Elegance** – uniform, minimal surprises.  
* **P‑2 Didactic Primacy** – narrative flow, dual archetype examples.  
* Guard‑Rails 1 & 2 – no tool jargon, no notation lock‑in inside prose.

Optionality for `[D]` patterns preserves efficiency: purely invariant
definitions need not carry dual examples, yet must still justify the
omission via Bias‑Annotation—keeping pedagogy and neutrality explicit.

Conformance checklist often has name conformance criteria in international and industry standards, FPF name it so to easier adopt by engineers and managers.

##### Relations  

* **Implements:** `pat:authoring/didactic‑architecture` (E 6) & `pat:authoring/archetypal‑grounding` (E 7)  
* **Constrained by:** Guard‑Rails E 5.1‑E 5.4 (lexical firewall, notation independence, etc.)  
* **Constrains:** All future `NORM`, `A`, `D`, and `GOV` patterns; DRR template references the same section order.  

###  E.9 · Design‑Rationale Record (DRR) Method \[D]

#### Problem frame  
FPF is engineered for Pillar **P‑10 Open‑Ended Evolution**: its normative
rules must adapt as new calculi and insights arrive. But change without a
record of *why* leads to conceptual erosion and undermines auditability.
Hence FPF requires an explicit **Design‑Rationale Record (DRR)**—a
durable *conceptual artefact* that precedes every normative change.

#### Problem  
Direct edits to the Core, absent a structured rationale, trigger three
systemic hazards:

1. **Lost provenance** – future authors cannot infer the reasoning behind
   a rule; intent decays.  
2. **Implicit assumptions** – discarded alternatives vanish from memory,
   so debates resurface and churn repeats.  
3. **Conceptual drift** – incremental tweaks slip past the Eleven Pillars
   and Principle Taxonomy lenses, blurring the framework’s foundations.

#### Forces  

| Force | Tension |
|-------|---------|
| **Agility vs Rigour** | Evolve swiftly ↔ demonstrate deliberate, Pillar‑aligned decisions. |
| **Transparency vs Efficiency** | Provide a public argument trail ↔ avoid bureaucratic drag on minor edits. |
| **Clarity vs Conciseness** | Capture full reasoning ↔ prevent meta‑text from bloating the Core itself. |

#### Solution — the DRR as a structured argument  
Any proposal to add, modify or deprecate a `NORM`, `A`, `D`, or `GOV`
rule **MUST** be accompanied by a **Design‑Rationale Record** containing
exactly four conceptual components:

| Component | Guiding question | Typical content |
|-----------|------------------|-----------------|
| **Problem frame** | *Why are we talking about this?* | Problem statement, triggering insight, or external change. |
| **Decision** | *What will we do?* | Precise normative text to enter the specification. |
| **Rationale** | *Why is this the right thing?* | Comparison of alternatives, Pillar check, taxonomy‑lens balance. |
| **Consequences** | *What happens next?* | Expected benefits, trade‑offs, impacted patterns, risk notes. |

The DRR lives **outside** the normative Core; only its *Decision* flows
into the specification upon acceptance, preserving Core brevity while
storing provenance.

#### Archetypal Grounding (System / Episteme)

| Holon flavour | DRR analogue | Four components illustrated |
|---------------|--------------|-----------------------------|
| **`U.System`** (physical) | Engineering Change Order for pump motor upgrade. | Context: inefficiency; Decision: switch to brushless DC; Rationale: energy gain vs cost; Consequences: new control schema + supplier change. |
| **`U.Episteme`** (knowledge) | Foundational theory revision paper. | Context: conflicting data; Decision: introduce new axiom; Rationale: explains legacy & new data, Pillar alignment; Consequences: fresh predictions, update to curricula. |

#### Conformance Checklist

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC‑DRR.1** | Any change to a `NORM`, `A`, `D`, or `GOV` pattern **SHALL** be preceded by an accepted DRR containing Context, Decision, Rationale, Consequences. | Prevents undocumented edits. |
| **CC‑DRR.2** | The *Rationale* element **MUST** assess the proposal against **all Eleven Pillars** and the five Principle‑Taxonomy lenses (`Gov`, `Arch`, `Onto/Epist`, `Prag`, `Did`). | Keeps evolution aligned and cross‑disciplinary. |
| **CC‑DRR.3** | The DRR **SHALL** list every pattern it supersedes, amends, or risks impacting. | Maintains explicit impact graph. |
| **CC‑DRR.4** | Once approved, only the *Decision* text is inserted into the Core; other DRR sections **SHALL NOT** migrate into normative prose. | Preserves Core brevity; provenance remains external. |
| **CC‑DRR.5** | Minor, non‑substantive edits (e.g., typos) **MAY** follow a lightweight DRR variant containing Context + Decision only, provided they do not alter semantics. | Allows efficiency without eroding rigour. |
| ^^CC‑DRR.6 (LAT pointer)** | For Δ‑2/Δ‑3 changes to part F or part G patterns, the DRR SHALL include a non‑normative pointer (id/URI) to a published LEX‑AUTH Trace (LAT) archived as U.Work; the LAT is evidence, not normative prose.

#### Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| **Complete audit trail** – every normative change carries a structured “why”. | Adds deliberate friction; mitigated by CC‑DRR.5 for trivial fixes. |
| **Higher decision quality** – Pillar & lens check surfaces hidden conflicts early. | Authors must learn taxonomy; template checklist shortens ramp‑up. |
| **Institutional memory** – prevents re‑litigation of rejected alternatives. | DRR archive grows; index stored in a non‑normative annex. |

#### Rationale  
A legal code evolves by amendments, not by editing the statute in place;
FPF adopts the same discipline. The DRR embodies **P‑10 Open‑Ended
Evolution** while protecting **P‑1 Cognitive Elegance**: the Core remains
succinct, yet its evolution is fully transparent. Coupling the argument
to the Pillars and taxonomy lenses aligns each change with FPF’s
constitution and Guard‑Rails, without prescribing tooling workflows.

#### Relations  

* **Instantiates:** P‑10 Open‑Ended Evolution, P‑2 Didactic Primacy  
* **Template governed by:** `pat:authoring/pattern‑template` (E 8)  
* **Interacts with:** `pat:guard/bias‑audit` (E 5.4) via lens check  
* **Complemented by:** `pat:authoring/code‑of‑conduct` (E 12) – etiquette for DRR debate  
