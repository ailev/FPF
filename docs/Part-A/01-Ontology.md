## **A.0 — Onboarding Glossary (NQD & E/E‑LOG)**  \[A]
**One‑screen purpose (manager‑first).** This pattern gives newcomers a plain‑language starter kit for FPF’s *generative* engine so they can run a lawful **problem‑solving / search loop** on day one. It explains the few terms you must publish when you **generate, select, and ship portfolios** (not single “winners”), and points to the formal anchors you’ll use later. *(OEE is a Pillar; NQD/E/E‑LOG are the engine parts.)*

**Builds on.** E.2 (**P‑10 Open‑Ended Evolution; P‑2 Didactic Primacy**), A.5, C.17–C.19 · **Coordinates with.** E.7, E.8, E.10; F.17 (UTS); G.5, G.9–G.12 · **Constrains.** Any pattern/UTS row that **describes a generator, selector, or portfolio**.

**Keywords & queries.** *novelty, quality‑diversity (NQD), explore/exploit (E/E‑LOG), **portfolio (set)**, illumination map *(gauge)*, parity run, comparability, ReferencePlane, CL^plane, **ParetoOnly** default*

### 1) Problem frame

Engineer‑managers meeting FPF for the first time need a **plain, on‑ramp vocabulary** for the framework’s *generative* engine so they can run an informed **problem‑solving/search loop** on day one—*before* formal architheories. Without that, Part G and Part F read as assurance/alignment only, and teams default to single “best” options. This **undercuts P‑10 Open‑Ended Evolution** and weakens adoption. 

### 2) Problem

In current practice:

* **Single‑winner bias.** Teams look for “the best” option and publish a leaderboard, suppressing **coverage & diversity** signals essential to search.
* **Metric confusion.** “Novelty” and “quality” are used informally; units/scales are omitted; ordinal values are averaged, breaking comparability.
* **Hidden policies.** Explore/exploit budgets and governor rules are implicit; results are irreproducible and **refresh‑unsafe** (no edition/policy pins).
* **Tool lock‑in.** Implementation terms (pipelines, file formats) leak into the Core, violating Guard‑Rails.

FPF needs a **short, normative glossary** that names the generative primitives in **Plain** register and ties each to its **formal anchor**—so portfolios, not single scores, become the default publication. 

### 3) Forces

| Force                         | Tension                                                                         |
| ----------------------------- | ------------------------------------------------------------------------------- |
| **Readability vs Rigor**      | One‑liners for managers ↔ lawful definitions with editions and scale types.     |
| **Creativity vs Assurance**   | Open‑ended search (OEE/QD) ↔ conformance, parity, and publication discipline.   |
| **Comparability vs Locality** | Shared N‑U‑C‑D terms ↔ context‑local CG‑frames and bridges with CL.             |
| **Tool‑agnostic Core**        | Conceptual publication in UTS ↔ engineering teams’ urge to cite specific tools. |

### 4) Solution — **Normative onboarding glossary and publication hooks**

#### 4.1 Plain one‑liners (normative on‑ramp; formal anchors in C.17–C.19)

| Term                      | Plain definition (on‑ramp)                                                                                                                                   | See        |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| **Novelty (N)**           | *How unlike the known set in your declared **CharacteristicSpace***. **Compute lawfully** (declared `DescriptorMapRef` + `DistanceDefRef`; no ad‑hoc normalisation). | C.17, C.18 |
| **Use‑Value (U / ValueGain)** | *What it helps you achieve now under your **CG‑Frame***; tie to acceptance/tests; **publish units, scale kind, polarity, ReferencePlane**.                   | C.17, C.18 |
| **Constraint‑Fit (C)**    | *Satisfies must‑constraints (Resource/Risk/Ethics)*; legality via **CG‑Spec**; **unknowns propagate** (never coerce to zero).                                | C.18, G.4  |
| **Diversity_P (portfolio)** | *Adds a new niche to the **portfolio***; measured against the **active archive/grid**, not a single list; declare **ReferencePlane** for each head.          | C.17, C.18 |
| **E/E‑LOG**               | *Named, versioned **explore↔exploit** policy*; governs when to widen space vs refine candidates; **policy‑id is published**.                                   | C.19       |
| **ReferencePlane**        | *Where a value lives:* **world** (system), **concept** (definition), **episteme** (about a claim). **Plane‑crossings add CL^plane** (penalties to **R only**); cite policy‑id. | F.9, G.6   |
| **Scale Variables (S)**  | *The **monotone knobs** along which improvement is expected* (e.g., parameterisation breadth, data exposure, iteration budget, resolution). **Declare S** for any generator/selector claimed to scale. | C.18.1       |
| **Scale Elasticity (χ)** | *Qualitative class of improvement when moving along S* (e.g., **rising**, **knee**, **flat** in the declared window). Used as a **selection lens**; numeric laws live in domain contexts.              | C.18.1       |
| **BLP (Bitter‑Lesson Preference)**  | *Default policy that **prefers general, scale‑amenable methods** over domain‑specific heuristics, unless forbidden by deontics or overturned by a scale‑probe.*                                        | C.19.1, C.24 |
| **Iso‑Scale Parity**  | *Fair comparison across candidates at equalised **scale budgets** along S*; may also include **scale‑probes** (two points) to test elasticity.                                                         | G.9, C.18.1  |

*(Registers & forbidden forms per **LEX‑BUNDLE**; avoid “axis/dimension/validity/process” for measurement and scope.)*  

#### 4.2 Publication & telemetry duties (where these terms **show up**)

1. **UTS surface (Part F).** When a **UTS row describes a generator, selector, or portfolio**, it **MUST** surface **N, U, C, Diversity_P, E/E‑LOG `policy‑id`, `ReferencePlane`**, with **units/scale/polarity** typed under **MM‑CHR / CG‑Spec**, and lawful references to `DescriptorMapRef`/`DistanceDefRef`. *(Row schema: F.17; shipping via G.10.)*  
2. **Parity & edition pins (Part G).** When QD/OEE is in scope, **pin** `DescriptorMapRef.edition` and `DistanceDefRef.edition` (and, where applicable, `CharacteristicSpaceRef.edition`, `TransferRulesRef.edition`) and record `policy‑id` + `PathSliceId`. Treat **illumination/coverage as gauges**; publish an **Illumination Map** where G‑kit mandates parity artefacts. **Declare S** (Scale Variables) and run at least one **scale‑probe** (two points along S) when claiming **scale‑amenability**. **Dominance policy defaults to `ParetoOnly`;** including illumination in dominance **MUST** cite a CAL policy‑id.
3. **Tell‑Show‑Show (E.7/E.8).** Any \[A] pattern that claims generative behaviour **MUST** embed **both** a **U.System** and a **U.Episteme** illustration using this glossary (manager‑first didactics). 

#### 4.3 Minimal recipe (run this on day one)
1) Declare **CG‑Frame** (what “quality” means; lawful units/scales) and **ReferencePlane**.  
2) Pick 2–4 **Q components** + a simple **DescriptorMap** (≥2 dims) for N/D; publish **editions**.  
3) Choose an **E/E‑LOG policy** (explore↔exploit budget); record **policy‑id**.  
4) Call the selector under **G.5** with parity pins; **return a set** (Pareto/Archive), not a single score.  
5) **Publish to UTS** + **PathIds/PathSliceId**; **Illumination Map** is a **gauge** by default.

### 5) Archetypal Grounding
*Informative; manager‑first (E.7/E.8 Tell‑Show‑Show).*  <!-- exact heading per CC‑AG.1 -->

**Show‑A · SRE capacity plan (selector returns a set).**
*Frame.* We must raise service headroom for Q4 without breaking latency SLOs.
*Portfolio.* `{cache‑expansion, read‑replicas, query‑shaping, circuit‑breaker tuning, schema‑denorm}`.
*Glossary in action.* `U = latency@p95 & error‑rate`, `C = budget ≤ $X, risk ≤ R`, `N = dissimilarity to current playbook`, `Diversity_P = adds a previously empty niche in our archive (e.g., “shifts load to edge”)`. E/E‑LOG starts **Explore‑heavy**, flips **Exploit‑heavy** once ≥ K distinct niches are lit. *(Publish UTS row + parity pins; illumination stays a gauge.)*  

**Show‑B · Policy search with QD archive (MAP‑Elites‑class).**
*Frame.* Robotics team explores gaits that trade stability vs energy use.
*Glossary in action.* `CharacteristicSpace = {step‑frequency, lateral‑stability}`, `ArchiveConfig = CVT grid`, `N` from descriptor distance, `U` = task reward, `Diversity_P` = coverage gain; **PortfolioMode=Archive**. Families include **MAP‑Elites (2015)**, **CMA‑ME/MAE (2020–)**, **Differentiable QD/MEGA (2022–)**, **QDax (2024)**; publish editions and policy‑ids; treat illumination as a **gauge**.  

*(Optional)* **Show‑C · OEE parity (POET/Enhanced‑POET).**
Co‑evolve `{environment, method}` portfolios; publish **coverage/regret** as gauges; pin `TransferRulesRef.edition`; return *sets*, not a single winner. 
  
**Show‑Epi · Evidence synthesis (U.Episteme).**
*Frame.* A living review compares rival **causal identification** methods (e.g., IV vs. DiD vs. RCT‑adjacent surrogates) across policy domains.
*Glossary in action.* `U = external‑validity gain @ F/G‑declared lanes`, `C = ethics & data‑licence constraints`, `N = dissimilarity in **ClaimGraph** transformations`, `D_P = coverage of identification niches in the archive`. `ReferencePlane = episteme`. Illumination/coverage stays a **gauge**; selection returns a **portfolio** of methods per niche. *(Publish UTS rows; cite Bridges + CL for cross‑domain reuse; edition‑pin Descriptor/Distance defs where QD applies.)*

### 6) Bias‑Annotation

**Scope.** Trans‑disciplinary; glossary applies to both **System** and **Episteme** work.
**Known risks & mitigations.**
*Over‑aggregation:* forbid mixed‑scale sums; use **CG‑frame** and **MM‑CHR**.
*Terminology drift:* enforce **LEX‑BUNDLE** registers; ban tool jargon in Core.
*Optimization monoculture:* require **portfolio** publication where G‑kit mandates parity; illumination stays a **gauge** unless CAL authorises otherwise.   

### 7) Conformance Checklist (SCR/RSCR stubs)

| ID          | Requirement                                                                                                                                                                               | Purpose                                                                         |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **CC‑A0‑1** | If a pattern/UTS row **describes a generator, selector, or portfolio**, it **MUST** surface **N, U, C, Diversity_P, `ReferencePlane`, and E/E‑LOG `policy‑id`**; **units/scale/polarity** **MUST** be declared. | Makes generative claims comparable and auditable (UTS as publication surface).  |
| **CC‑A0‑2** | When QD/OEE is in scope, **pin** editions: `DescriptorMapRef.edition`, `DistanceDefRef.edition` (and, where applicable, `CharacteristicSpaceRef.edition`, `TransferRulesRef.edition`); log `PathSliceId` and policy‑ids. | Enables lawful *parity/refresh*; edition‑aware telemetry.                       |
| **CC‑A0‑3** | **No mixed‑scale roll‑ups**; ordinal data **SHALL NOT** be averaged; any roll‑up **MUST** live under a declared **CG‑frame**.                                                             | Prevents illegal scoring; keeps comparisons lawful.                             |
| **CC‑A0‑4** | Where the G‑kit requires parity, **publish an Illumination Map** (coverage per niche); **single‑number leaderboards are non‑conformant** on the Core surface when a ParityReport is required. | Portfolio‑first publication; avoids single‑winner bias.                         |
| **CC‑A0‑5** | Keep **illumination/coverage** as **gauges**; **dominance policy defaults to `ParetoOnly`**; any change is CAL‑authorised and cited by policy‑id.                                          | Separates fit from exploration; preserves auditability.                         |
| **CC‑A0‑6** | Apply **E.7/E.8**: include a **U.System** and a **U.Episteme** illustration when claiming generative behaviour; obey **E.10** register hygiene; use the exact subsection title **“Archetypal Grounding.”** | Locks didactic primacy; prevents jargon drift.                                  |
| **CC‑A0‑7** | **ReferencePlane declared** for every N/U/C/Diversity_P head and **CL^plane** penalties **route to R only**; **Φ_plane** policy‑id published when planes differ.                            | Prevents plane/stance category errors; aligns with Bridge/ATS guards.           |
| **CC‑A0‑8** | **Diversity_P ≠ Illumination.** Diversity_P may enter dominance; **Illumination** remains a **gauge** unless explicitly promoted by CAL policy‑id.                                         | Matches QD triad semantics and parity defaults.                                 |
| **CC‑A0‑9** | If a generator/selector is claimed **scale‑amenable**, **declare S (Scale Variables)** and an **E/E‑LOG scale policy‑id**; otherwise mark **S = N/A**.                                      | Makes scale assumptions explicit and comparable across contexts.                 |
| **CC‑A0‑10** | For scale‑amenable claims, execute a **scale‑probe** (≥ 2 points along S) and report a **Scale Elasticity class** (*rising/knee/flat*) in the UTS row.                                      | Forces early strategy‑relevant evidence without over‑specifying numerics.        |
| **CC‑A0‑11** | Apply **Iso‑Scale Parity** in parity runs when S is declared; where infeasible, state the **loss notes** and treat results as **non‑parity** with an explicit penalty in **R**.             | Keeps comparisons fair and auditable under scale constraints.                    |
| **CC‑A0‑12** | **BLP default.** If a domain‑specific heuristic is selected over a general, scale‑amenable method, record a **BLP‑waiver** reason: *deontic*, *scale‑probe overturn*, or *context‑specific*. | Prevents silent violations of the Bitter Lesson; improves selector transparency. |

### 8) Consequences

**Benefits.**
• **Immediate usability** for engineer‑managers (plain one‑liners) with **formal anchors** for auditors.
• **Portfolio‑first** culture (sets & illumination) instead of brittle leaderboards.
• **Edition‑aware comparability**; parity/refresh is routine, not ad‑hoc.

**Trade‑offs & mitigations.**
• Slightly longer UTS rows → mitigated by consistent schema and copy‑paste snippets.
• Requires discipline on units/scales → mitigated by CG‑frame templates.

### 9) Rationale

This pattern **instantiates P‑10 Open‑Ended Evolution** by making *generation‑selection‑publication* **operational** at the on‑ramp: readers get just enough shared vocabulary to run *search as standard practice*. It aligns with **Didactic Primacy (P‑2)** and **LEX‑BUNDLE (E.10)** by keeping definitions *plain‑first* and scale‑lawful, and with **Plug‑in Layering (P‑5)** by pointing to C.17–C.19 for formal anchors without tool lock‑in. The post‑2015 line (MAP‑Elites → CMA‑ME/MAE → Differentiable QD/MEGA → QDax; POET/Enhanced‑POET/Darwinian Goedel Machine) normalised **quality‑diversity** and **open‑endedness** as first‑class search objectives; this glossary surfaces those ideas as **publication standards**, not tool recipes.  

### 10) Relations

**Builds on.** **E.2 Pillars** (P‑10, P‑2, P‑6), **A.5** (Open‑Ended Kernel), **B.5/B.5.2.1** (Abductive loops + NQD binding), **C.17–C.19** (Creativity‑CHR, NQD‑CAL, E/E‑LOG).    

**Coordinates with.** **E.7/E.8** (Archetypal Grounding; Authoring template), **E.10** (LEX‑BUNDLE), **F.17** (UTS), **G.5/G.9–G.12** (set‑returning selectors, **iso‑scale** parity, shipping & refresh).
**Constrains.** Any generator/selector/portfolio publication on the Core surface: **N‑U‑C‑Diversity_P + policy‑ids; S/Scale‑probe where applicable; parity pins; lawful scales; portfolio‑first where mandated**. (Ties into UTS rows and parity artefacts.)
**Editor’s cross‑reference.** For agentic orchestration of scalable tool‑calls under **BLP**/**SLL**, see **C.24 (Agent‑Tools‑CAL)**.

### Editor’s note (implementation hint)

This pattern is an **on‑ramp**: it **does not replace** C.17–C.19. It binds Plain definitions to **publication/telemetry** expectations so newcomers can *use* NQD/E/E‑LOG immediately while experts follow the formal trails. 



---

## A.1 Holonic Foundation: Entity → Holon  \[A] 

> *“Name the thing without smuggling in its parts.”*

### 1 · Context

The first epistemic act in any discipline is to **point**: “that thing, not the background.” Physics calls the pointed object a *system*, biology an *organism*, information science an *artifact*, philosophy an *entity*. Reusing any one of these across domains drags hidden assumptions and yields nonsense like *“What is the mass of a system of equations?”* or *“Where is the network interface of a moral theory?”*
FPF therefore starts from a **minimal, domain‑agnostic root** that makes such category errors impossible **by construction** and gives engineers and managers a clean, uniform handle for composition, boundaries and interfaces.

### 2 · Problem

If FPF treats **system** as the universal root, two recurrent failure modes appear:

1. **Category Error** — physical affordances get projected onto abstract artifacts (ports on theories; kilogram‑mass of paradigms).
2. **Mereological Over‑reach** — part–whole calculus is applied to genuinely atomic entities (prime numbers, elementary charges), producing meaningless “sub‑parts.”

A robust kernel must **separate identity from structure**: first say *what can be singled out*, then say *what has parts*.

### 3 · Forces

| Force                         | Tension                                                                                                    |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **Universality vs Intuition** | Precision of a new root term (*Holon*) ↔ practitioner expectation of familiar words (*System*, *Theory*).  |
| **Purity vs Pragmatism**      | Clean formalism ↔ immediate usability for engineers, scientists, managers.                                 |
| **Structure vs Identity**     | Need to talk about atoms with zero parts ↔ need full mereology for composites.                             |

### 4 · Solution — A three‑tier root (Entity ⊃ Holon ⊃ {System, Episteme})

FPF adopts a **three‑tier root ontology** refining Koestler’s “holon,” with crisp boundaries and safe composition. The presentation follows the \[A]‑template and style mandates (Context → Problem → Forces → Solution → …; mandatory *Archetypal Grounding*).

**4.1  `U.Entity` — Primitive of Distinction**
Anything that can be individuated and referenced. **No structural assumptions.** Use when you must name “a something” without committing to having parts.

**4.2  `U.Holon` — Unit of Composition**
A `U.Entity` that is *simultaneously* **(a)** a whole composed of parts and **(b)** a part within a larger whole. Formally, `U.Holon ⊑ U.Entity`.
Operational requirements:

* A holon has **exactly one** `U.Boundary` that separates it from its environment.
* The universal aggregation operator **Γ** is **only** defined on sets of `U.Holon` (never on bare `U.Entity`).
  These constraints make composition rules uniform across domains and prevent Γ from being misapplied.

**4.3  Interface primitives: `U.Boundary` & `U.Interaction`**
Every holon is defined by **how** it is separated and **what** crosses the separation.

* **`U.Boundary`** — physical or conceptual surface delimiting the holon’s scope.
* **`U.Interaction`** — any flow of matter, energy, or information that crosses a boundary.
  **Canonical boundary kinds (with twin archetypes):**

| Kind          | Permitted exchanges             | `U.System` archetype               | `U.Episteme` archetype                                        |
| ------------- | ------------------------------- | ---------------------------------- | ------------------------------------------------------------- |
| **Open**      | Matter, energy, information     | Microservice exposing a public API | Public wiki editable by anyone                                |
| **Closed**    | Energy, information (no matter) | Sealed cooling loop in a server    | Version‑locked theory accepting new evidence but fixed axioms |
| **Permeable** | User‑filtered subset            | Cell membrane regulating ions      | Legal code allowing specific amendment classes only           |

This pair (`Boundary`, `Interaction`) makes interfaces explicit, reviewable, and testable across domains.

**4.4  Inside/Outside decision procedure**
To decide whether an entity **E** is *inside* a holon **H**, apply:

1. **Dependency test:** removing **E** breaks a core invariant of **H**.
2. **Interaction test:** **E** participates in causal loops wholly within **H**’s boundary.
3. **Emergence test:** **E** contributes to a novel collective property warranting **H** as a single unit.
   Fail all three → **E** is *outside*. This practical triage prevents “scope creep” and forces explicit modeling of environment vs interior.

**4.5  Archetypal sub‑holons**
FPF fixes two **archetypal** specializations to ground cross‑domain universality:

| Subtype                    | Essence                                                | Home architheory |
| -------------------------- | ------------------------------------------------------ | ---------------- |
| **`U.System ⊑ U.Holon`**   | Physical, operational holon obeying conservation laws. | **Sys‑CAL**      |
| **`U.Episteme ⊑ U.Holon`** | Knowledge holon (axioms, evidence, argument graph).    | **KD‑CAL**       |

*Naming guideline:* keep “**System**” and “**Episteme**” for practitioner comfort; reserve **Holon** for meta‑level discourse and formal signatures.

### 5 · Archetypal Grounding (System / Episteme)

| Holonic slot | **`U.System` — Water‑pump**            | **`U.Episteme` — Scientific theory**            |
| ------------ | -------------------------------------- | ----------------------------------------------- |
| **Identity** | Pump #37 stamped on the name‑plate     | “Newtonian Gravitation”, 1726 edition           |
| **Boundary** | Cast‑iron casing; inlet/outlet flanges | Axiomatic scope and vocabulary                  |
| **Parts**    | Motor, impeller, seals, housing        | Axioms, definitions, theorems, datasets         |
| **Whole**    | Operable assembly that moves fluid     | Coherent body of knowledge predicting phenomena |

Showing the **same structural slots** filled by a machine and a theory demonstrates the **substrate‑independent universality** of `U.Holon`. This is the didactic “Tell–Show–Show” anchor required by the Style‑Guide for \[A]‑patterns. 

---

### 6 · Common Modelling Anti‑Patterns (manager’s quick checks)

1. **“Ports on a theory.”** Treating a proof corpus as if it had physical connectors. *Fix:* model `U.Interaction` only across **boundaries**; for epistemes, interactions are **symbolic flows** via carriers and citations (see A.10), not power or mass.
2. **“Document edited itself.”** Assigning actions to an episteme. *Fix:* actions are executed by a **system bearing a role** (A.12/A.15); epistemes are transformed **via external transformers** acting on their **symbol carriers**.
3. **“Parts everywhere.”** Forcing a part–whole onto atomic entities (e.g., prime numbers). *Fix:* if no meaningful parts exist, stay at `U.Entity`; apply Γ only to `U.Holon`.
4. **“Scope ≡ section.”** Using “scope” as a text region rather than a modeled boundary. *Fix:* define a `U.Boundary` and state what crosses it (`U.Interaction`).

> **When in doubt:** first decide **what is a holon**, then state **its boundary**, then list **what crosses**. Roles and methods come *after* (see A.2 and A.15).

### 7 · Conformance Checklist (normative)

| ID          | Requirement                                                                                                                                                                    | Purpose / Notes                                                                                                        |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| **CC‑A1.1** | Any modelled object that exhibits a part–whole structure **MUST** be typed as `U.Holon` or its subtype.                                                                        | Prevents applying Γ to atomic entities; makes aggregation well‑typed.                                                  |
| **CC‑A1.2** | Each `U.Holon` **MUST** reference exactly one `U.Boundary` and declare its boundary kind (*open / closed / permeable*).                                                        | Enables boundary inheritance and environmental Standards; aligns with the canonical boundary kinds introduced in A.1.  |
| **CC‑A1.3** | Domain architheories **MUST** explicitly subtype their root concept (`U.System`, `U.Episteme`, …) from `U.Holon`.                                                              | Ensures cross‑domain compatibility of aggregation and emergence patterns.                                              |
| **CC‑A1.4** | Inside/Outside decisions for any candidate part **SHALL** be justified by the three‑step test (Dependency → Interaction → Emergence) and recorded with the boundary reference. | Makes holon membership auditable and repeatable; uses A.1’s decision procedure.                                        |
| **CC‑A1.5** | Behavioural roles (**including** `TransformerRole`) **SHALL** attach only to `U.System` (the bearer), not to `U.Holon` in general and not to `U.Episteme`.                     | Preserves Strict Distinction and prevents category errors; episteme roles are classificatory only.                     |
| **CC‑A1.6** | Do **not** model acting groups as sets. If a grouping is expected to **act**, it **SHALL** be modelled as a **collective system** (with boundary, role, Method/Work).          | Distinguishes `MemberOf` (collection) from mereology; prepares for A.14 Portions/Phases.                               |
| **CC‑A1.7** | The universal aggregation operator **Γ** **SHALL** be applied **only** to sets of `U.Holon` within a single declared temporal scope (design **or** run) and context.           | Prevents “chimera” graphs; routes order/time to Γ\_ctx / Γ\_time (B.1.4).                                              |
| **CC‑A1.8** | Prose and diagrams **SHALL** follow the naming guideline: use **Holon** for meta‑level discourse; prefer **System / Episteme** in practitioner‑level statements.               | Reduces jargon friction; keeps signatures precise and text readable.                                                   |

> *Audit tip.* CC‑A1.5 is frequently violated when authors write “holon bearing TransformerRole”. Rewrite to “**system** bearing TransformerRole” or provide the explicit `U.RoleAssignment`. See A.2/A.15 for role mechanics.

---

### 8 · Consequences (informative)

| Benefits                                                                                                                                                         | Trade‑offs / Mitigations                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Eliminates category errors** across physical and abstract realms by cleanly separating identity (Entity), structure (Holon), and behaviour (Role/Method/Work). | Introduces the unfamiliar term **Holon**; mitigated by Tell‑Show‑Show pedagogy and dual archetypal examples (System/Episteme).  |
| **Unifies aggregation**: a single algebra Γ composes pumps, proofs, genomes, and teams under one roof.                                                           | Requires refactoring legacy “System‑only” language; addressed by A.2/A.3 role calculus and the Γ‑family in B.1.                 |
| **Predictable extension point**: CAL/LOG/CHR architheories add constraints without touching the core types.                                                      | Imposes discipline on boundary declarations; mitigated by boundary kinds and the Inside/Outside test.                           |

---

### 9 · Rationale with cross‑domain corroboration (post‑2015, informative)

The separation **Entity → Holon → {System, Episteme}** is not only ontologically clean; it is **empirically validated across domains since 2015**:

* **Compositional open systems.** Category‑theoretic treatments show that *boundaried* components compose safely (decorated cospans, open systems). This mirrors Γ’s reliance on declared boundaries. *(Fong & Spivak, 2019; Baez & Courser, 2017)*
* **Microservices & bounded contexts.** Modern software architecture stresses strong service boundaries and local reasoning as the route to evolvability—our `U.Boundary` and Inside/Outside test encode the same discipline. *(Newman, 2021; Vernon, 2022)*
* **FAIR & provenance.** Data/knowledge communities require explicit distinction between **content** and **carrier**, and auditable provenance—precisely the System/Episteme + SCR split used in A.1/A.10. *(Wilkinson et al., 2016; Boeckhout et al., 2018)*
* **Digital Twin / Thread.** Engineering practice since late‑2010s emphasises the run↔design seam and boundary‑consistent aggregation of subsystems—formalised in our Γ‑family and boundary inheritance rules. *(Grieves & Vickers, 2017; NIST DT/Thread reports 2019‑2021)*
* **Layered control of CPS.** Standard‑based, multi‑rate architectures justify explicit holon boundaries and scale transitions—feeding directly into B.2 Meta‑Holon Transition. *(Matni et al., 2024)*

These streams converge on one point: **make boundaries and composition first‑class** and separate **what a thing is** from **what it is doing here‑and‑now**—the heart of A.1/A.2.

---

### 10 · Relations

* **Builds / Grounds:**

  * **A.2 Role Taxonomy** — A.1 provides the substantial characteristic (`Holon`), A.2 introduces the functional characteristic (`Role` and `U.RoleAssignment`). Together they prevent role/type explosion and keep agency contextual.
  * **A.7 Strict Distinction (Clarity Lattice)** — A.1 supplies the *slots* (Entity/Holon/System/Episteme); A.7 guards their separation in prose and models, stopping Object ≠ Description ≠ Carrier conflations.
  * **A.14 Advanced Mereology: Portions & Phases** — A.1’s holon substrate is the target of A.14’s edge discipline (`ComponentOf`, `ConstituentOf`, `PortionOf`, `PhaseOf`); only mereological subtypes build holarchies.

* **Interacts with the Γ‑family (B‑cluster):**

  * **B.1 Universal Algebra of Aggregation** — Γ is defined **on holons** and respects CC‑A1.\*; Γ\_ctx/Γ\_time carry order and temporal composition, Γ\_work handles resource ledgers.
  * **B.2 Meta‑Holon Transition (MHT)** — uses A.1’s boundary and Inside/Outside rules to decide when aggregation yields a **new** whole with novel properties.
  * **B.3 Trust & Assurance Calculus** — evidence attaches to carriers (SCR/RSCR) of epistemes; assurance levels depend on A.1/A.10 alignment.
  * **B.4 Canonical Evolution Loop** — operationalises the **design↔run** seam at holon boundaries; observation itself is an external transformation across a boundary.

* **Specialised by architheories:** `U.System` (Sys‑CAL) and `U.Episteme` (KD‑CAL) are archetypal sub‑holons that supply domain‑specific invariants while inheriting A.1’s boundary and aggregation duties. 

---

*Without the holon, parts drift; without the role, purpose evaporates.* (Carry this epigraph with A.1 to cue the A.2 hand‑off.)


### Pattern A.1.1 — `U.BoundedContext`: The Semantic Frame \[D]

#### 1 · Term & Definition

*   **Term:** `U.BoundedContext`
*   **Definition:** A **`U.BoundedContext`** is a `U.Holon` that serves as an explicit **semantic frame of reference**. It defines a boundary within which a specific set of models, roles, rules, and language is self-consistent and authoritative. It is the FPF's formal mechanism for localizing meaning and managing complexity by partitioning a larger conceptual space into smaller, coherent, and independently governable domains.

#### 2 · Forces

### 2.1 · Prophylactic clarification — Context vs Domain
To prevent a common category error, **Domain** and **U.BoundedContext** are **not synonyms** in FPF.

| Characteristic | **Domain** (e.g., Physics, Law, Automotive Engineering) | **U.BoundedContext** (e.g., `AirTrafficControl_2025`, `Theory:QuantumMechanics`) |
| :--- | :--- | :--- |
| **Nature** | An **external field** of practice/knowledge that exists independently of any model. | An **internal FPF holon**: a named semantic “Context” with its own vocabulary and rules about a slice of a domain. |
| **Role in FPF** | Provides **grounding** for applicability and cross‑domain universality of the kernel. | Provides **local meaning and separation**: a semantic firewall where words and rules are coherent and unambiguous. |
| **Relationship** | One domain can have **many** valid perspectives. | A bounded context **hosts** one such perspective (Glossary, Invariants, local Role taxonomy, Bridges). |

**Normative anchor (didactic form):**  
The `context` field in any `U.RoleAssignment` **MUST** reference a **U.BoundedContext**, **never** a broad domain label.  
*Think “specific room” (e.g., `Hospital.OR_2025`), not “the whole building” (e.g., “Healthcare”).*

**Manager’s one‑liner:** A **Domain** is the *territory*; a **Bounded Context** is a *purpose‑made map* of that territory.

The concept of a `U.BoundedContext`, inspired by Domain-Driven Design (DDD) but elevated to a universal first principle, is essential for several reasons:

1.  **To Manage Complexity:** Real-world systems are too complex to be described by a single, monolithic model. A `U.BoundedContext` allows us to break down this complexity into manageable parts. Inside a context (e.g., "Air Traffic Control"), the term "flight" has a precise, unambiguous meaning. Outside, it could mean many things.
2.  **To Enable Pluralism:** Different teams, disciplines, or even historical eras have different models of reality. A `U.BoundedContext` allows these different worldviews to coexist without contradiction. As demonstrated in A.2, Pluto can be a `PlanetRole` in the context of `Early20thCenturyAstronomy` and a `DwarfPlanetRole` in the context of `IAU_2006_Definition`. The context is what resolves the apparent paradox.
3.  **To Make Roles Meaningful:** As established in A.2.1 `U.RoleAssignment`, a `U.Role` is only meaningful *inside* a context. The role of "Lead Engineer" is defined by the rules and expectations of "Project Phoenix," not by some universal law of engineering. The context provides the "stage" upon which the role is performed.

In short, a `U.BoundedContext` is not just a "scope" or a "namespace." It is a **holon of meaning**, a self-contained universe of discourse with its own local truth.

#### 3 · Core Components & Attributes

A `U.BoundedContext` is a composite holon defined by the following key components, which collectively constitute its model:

*   **`Glossary` (Local Lexicon):** A set of `U.Lexeme` entries (from Lang-CHR) that defines the specific vocabulary used within this context. It maps local terms to canonical FPF `U.Types` and clarifies any domain-specific jargon. This is where a context declares, "Inside here, the word 'ticket' means a `U.WorkItem`, not a `U.TravelPermit`."

*   **`Invariants` (Local Rules):** A set of machine- and human-readable rules (`U.ConstraintRule` from Norm-CAL) that must hold for any artifact or process within this context. This is the most powerful component, as it defines the "local physics" of the context.
    *   **Example Invariant (Role Compatibility):** *"Within this context, a `holder` cannot simultaneously play the `AuditorRole` and the `DeveloperRole`."*
    *   **Example Invariant (State Transition):** *"A `U.WorkItem` in this context can only transition from 'In Progress' to 'In Review', never directly to 'Done'."*

*   **`Roles` (Local Taxonomy):** A partial order of `U.Role`s that are defined and valid *only* within this context. It specifies the "job titles" available on this "stage."

*   **`Bridges` (Optional Mappings):** A set of explicit mappings (`U.Alignment`) to other `U.BoundedContext`s. A bridge defines how concepts and terms are translated when information flows from one context to another. This is the formal mechanism for inter-context communication.
    *   **Example Bridge:** A mapping that states, *"The `UserStory` concept in the `AgileDevelopment` context is functionally congruent (CL=1) to the `Requirement` concept in the `FormalEngineering` context."*

#### 4 · Relations to Other FPF Concepts

*   **As a `U.Holon`:** A `U.BoundedContext` is itself a holon. It has a **boundary** (the semantic line between what's inside and outside its model), **parts** (its `Glossary`, `Invariants`, etc.), and can be part of a larger whole (a context can be nested within another, more general context).

*   **As the Anchor for `U.RoleAssignment`:** The `context` field of a `U.RoleAssignment` **MUST** reference a valid `U.BoundedContext`. This ensures that every role assignment is explicitly anchored to a well-defined semantic frame.

*   **As the Scope for `U.Objective`:** A `U.Objective` (from Norm-CAL) is often defined relative to a context. The goal of "maximize velocity" is meaningful within the context of an `AgileSprint`, but might be meaningless or even counterproductive in a `ResearchDiscovery` context.

*   **As a Target for `U.Transformer`:** A `U.BoundedContext` can be changed. The evolution of a team's process, a scientific theory, or a project's rules is modeled as a `Transformer` acting on the `U.BoundedContext` holon itself (e.g., by adding a new invariant or deprecating a role).

#### 5 · Archetypal Grounding

The concept of a `U.BoundedContext` is universal and applies to both physical/operational domains and purely abstract/epistemic ones. Understanding these two archetypes clarifies its role as a fundamental FPF primitive.

| Archetype | Holder of the Context | `U.BoundedContext` Example | Core Components Illustrated |
| :--- | :--- | :--- | :--- |
| **`U.System` Archetype** | A modern software engineering team | **`AgileProject:Phoenix`** | **`Glossary`**: Defines "Story Point," "Sprint," "Velocity." <br> **`Invariants`**: "Daily stand-up must not exceed 15 minutes." "A Story cannot move to 'Done' without a linked Test Case." <br> **`Roles`**: `ProductOwnerRole`, `ScrumMasterRole`, `DeveloperRole`. <br> **`Bridges`**: Maps `Velocity` metric to the `FinanceDept` context's `CostCenter:BudgetBurnRate`. |
| **`U.Episteme` Archetype** | A scientific community | **`Theory:SpecialRelativity`** | **`Glossary`**: Defines "Inertial Frame," "Lorentz Transformation," "Proper Time." <br> **`Invariants`**: "The speed of light in a vacuum is constant for all observers." "The laws of physics are the same in all inertial frames." <br> **`Roles`**: `Postulate#AxiomaticCoreRole`, `Experiment#EvidenceRole`. <br> **`Bridges`**: Maps its concept of "Spacetime" to the `GeneralRelativity` context's more complex concept of "Curved Spacetime." |

**Key takeaway from grounding:**
This illustrates that a `U.BoundedContext` is not an abstract container but a **holon with tangible content**. For the engineering team, it's their project's "operating system." For the scientific theory, it's the "intellectual constitution." In both cases, the context defines what is true, what is possible, and what words mean *locally*.

#### 6 · Conformance Checklist

To ensure `U.BoundedContext` is used consistently and rigorously, the following normative checks apply.

| ID | Requirement (Normative Predicate) | Purpose / Rationale |
| :--- | :--- | :--- |
| **CC-A1.1.1 (Holon Nature)** | A `U.BoundedContext` **MUST** be modeled as a `U.Holon` with a defined `U.Boundary`. | Reinforces that contexts are well-defined entities, not vague groupings. Enables reasoning about contexts themselves as systems. |
| **CC-A1.1.2 (Role Localization)**| Every `U.Role` **MUST** be defined within the `Roles` taxonomy of at least one `U.BoundedContext`. A "global" role is forbidden. | Ensures that roles are never context-free. Prevents ambiguity by forcing every role to be anchored to a specific semantic frame. |
| **CC-A1.1.3 (Invariant Scope)** | An `Invariant` defined within a context **MUST** only apply to holons and processes operating *within* that context. | Prevents the leakage of local rules into the global space, which is critical for modularity and managing complexity. |
| **CC-A1.1.4 (Bridge Explicitness)** | Any interaction or mapping between two `U.BoundedContext`s **MUST** be modeled as an explicit `Bridge` artifact. | Forbids "backdoor" or implicit communication between contexts. Makes all inter-context dependencies visible and auditable. |
| **CC-A1.1.5 (RoleAssignment Context Anchor)** | Every `U.RoleAssignment` **MUST** reference exactly one `U.BoundedContext` in its `context` field. | Guarantees that every role assignment is unambiguous and its meaning is fully determined by a single, authoritative context. |

#### 7 · Consequences

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Enables True Modularity:** By encapsulating models, FPF can support large, complex systems where different teams can work on their own bounded contexts in parallel with minimal interference. | **Modeling Overhead:** Requires architects to explicitly think about and define the boundaries of their models, which can feel like extra work initially. *Mitigation:* This upfront effort is a strategic investment that prevents the much higher cost of integration chaos and semantic ambiguity later in the project. |
| **Resolves Ambiguity and Paradox:** Provides a formal mechanism to manage synonyms, homonyms, and conflicting models (like the Pluto example). It transforms "it depends" into a precise, queryable structure. | **Bridge Maintenance:** As contexts evolve, the bridges between them must be maintained. *Mitigation:* FPF tooling should support "link integrity" checks to automatically flag broken or outdated bridges. |
| **Makes Rules Explicit:** The `Invariants` component of a context makes the local rules and invariants for a project or theory explicit, documented, and auditable. | - |
| **Foundation for Scalable Autonomy:** In multi-agent systems, each agent can operate within its own bounded context, communicating with others through well-defined bridges. This is a prerequisite for building robust, decentralized systems. | - |

#### 8 · Rationale

**Lineage and fit with Domain‑Driven Design (DDD).**  
FPF generalizes the proven DDD idea of a **Bounded Context** from software into a universal modeling primitive:

| DDD concept | FPF counterpart | Generalization in FPF |
| :--- | :--- | :--- |
| Bounded Context | **U.BoundedContext** (a holon) | Used for systems **and** knowledge; first‑class object with explicit Glossary, Invariants, local Roles, Bridges. |
| Ubiquitous Language | **Glossary** of the context | The shared vocabulary is an explicit component, not just narrative. |
| Context Map | **Bridges/Alignment** between contexts | Cross‑context relations are modeled explicitly rather than assumed globally. |

**Why this matters here.**  
`U.BoundedContext` gives `U.RoleAssignment` (A.2.1) its footing: role meanings are **local by design**, conflicts are checked **inside** the same context, and differences **across** contexts are handled by *explicit bridges** instead of “global truth.”

The introduction of `U.BoundedContext` as a first-class holon is a direct implementation of several core FPF principles and is strongly supported by contemporary practice.

*   **Philosophical Grounding:** The idea that meaning is always local and context-dependent is a cornerstone of late 20th-century philosophy of language (e.g., Wittgenstein's "language-games"). FPF operationalizes this insight.
*   **Domain-Driven Design (DDD):** The concept is a direct borrowing and generalization from Eric Evans' seminal work on DDD, where the Bounded Context is the central strategic pattern for managing complexity in large-scale software. Its success over the past two decades in the software industry provides powerful empirical validation for its utility. FPF elevates it from a software design pattern to a universal ontological primitive.
*   **Architectural Necessity:** For FPF to fulfill its promise of being an "operating system for thought," it needs a mechanism analogous to an OS's "process separation." A `U.BoundedContext` is precisely that: a protected "memory space" for a model, preventing different models from corrupting each other.
*   **Enabler for Key Patterns:** The `Contextual Role Assignment` pattern (A.2.1) would be incoherent without a formal definition of "Context." This pattern provides that necessary foundation, making the entire role-based architecture sound.

In essence, `U.BoundedContext` is the architectural pattern that allows FPF to be both **universal** in its core principles and **specific** and **pluralistic** in its applications. It is the mechanism that tames complexity and makes large-scale, multi-paradigm modeling possible.

#### 9 · Relations

*   **Constitutes:** The foundational "semantic space" for patterns like `A.2 Role Taxonomy` and `A.13 The Agential Role`.
*   **Builds on:** `A.1 Holonic Foundation`, as a `U.BoundedContext` is itself a `U.Holon`.
*   **Interacts with:**
    *   `Norm-CAL`: A context's `Invariants` are typically expressed as `U.ConstraintRule`s.
    *   `Lang-CHR`: A context's `Glossary` is a collection of `U.Lexeme`s.
    *   `Decsn-CAL`: Decisions and objectives are often scoped to a specific context.
*   **Enables:** The resolution of conflicts as modeled in `D.3 Holonic Conflict Topology`, by showing that many conflicts are context-dependent.


---

## A.2 Role Taxonomy  \[A] 

*A holon’s essence tells us **what it is**; its roles tell us **what it is being, here and now**.*

### Problem frame

Pattern A.1 established the **substantial** characteristic of the core (`Entity → Holon → {System, Episteme, …}`), cleanly separating identity from structure and aggregation. The present pattern introduces the **functional** characteristic: how a holon participates in purposes **within a bounded context** and for some interval. This extends the early sketch of A.2 and tightens its alignment with A.7 (Strict Distinction): roles are *not* parts and *not* behaviours; they are contextual **masks** that a holon wears while behaviours are handled by **Method**/**Work**. 

### Problem

Without an explicit role calculus:

1. **Type explosion & conflation.** Each new purpose breeds a new “subtype” (`PumpAsCoolingLoop`, `PumpAsFuelLoop`, …), violating parsimony and fusing substance with function.
2. **Agency opacity.** It becomes unclear whether *any* system may act as a transformer/agent, or only pre-declared special kinds.
3. **Epistemic blindness.** Knowledge artefacts (papers, proofs) cannot be given roles, blocking modelling of citation, evidence, or design-time justification.

### Forces

| Force                                | Tension                                                              |   |
| ------------------------------------ | -------------------------------------------------------------------- | - |
| **Identity vs Function**             | A holon’s make‑up ↔ its transient, contextual purpose.               |   |
| **Static vs Dynamic classification** | Fixed type lattice ↔ late‑binding of new roles.                      |   |
| **Universality vs Familiarity**      | One mechanism for pumps **and** papers ↔ domain‑specific role names. |   |
| **Simplicity vs Expressiveness**     | Minimal primitives ↔ multi‑role, multi‑holder scenarios.             |   |

---

### Solution 

We elevate **Role** to a first‑class, *context‑indexed* concept and make the **binding** between a holon and a role explicit.

#### S‑level definitions (normative)

* **`U.Role`** — a **context-bound** capability/obligation schema that a holon **may bear (play)** for a time interval. A role has **no parts** and **no resource deltas** of its own. *(A7 guard)*
* **`U.RoleAssignment`** — a first-class object recording that a holon **bears (plays)** a role **in** a bounded context, optionally with authority, justification, and provenance:

```
U.RoleAssignment {
  holder        : U.Holon,
  role          : U.Role,
  context       : U.BoundedContext,
  timespan?     : Interval,
  justification?: U.Episteme,  // why (standard, SOP, evidence)
  provenance?   : U.Method     // how assignment/verification was done
}
```

Short form (readable): `Holon#Role:Context [@Interval]`.

> **Why a first‑class binding?** It keeps identity (holon), function (role), context (semantics), and time (run‑window) separate yet linked, preventing the substance/function conflation identified above. The early `playsRoleOf(Holon, Role, span)` relation in the draft is subsumed by `U.RoleAssignment` and extended with **Context** (and optional governance fields).

#### Temporal & behavioural alignment

* **Method** exists **only while** some **Work** is underway; **MethodDescription** persists as Episteme. A Role **binds** to Method (design‑time), and Work **performs** Method under that Role (run‑time). This preserves the *role ≠ behaviour* split and the *design ↔ run* duality.
* Only **Work** carries resource deltas (feeds Γ\_work); a Role never does.

---

### Invariants (must‑hold, concept‑level)

1. **Locality.** `role ∈ Roles(context)`. Outside its context, a role’s meaning is undefined.
2. **Non‑mereological.** No Role (nor Method/MethodDescription) may appear in any `partOf` chain; holarchies are for substantial holons only.
3. **Multiplicity.** A holder may **bear** multiple roles concurrently; a role may be **borne** by many holders—subject to each context’s compatibility rules.
4. **Time anchoring.** `timespan` (if present) is non‑empty and finite for run‑time claims; design‑time bindings are timeless but versioned via `MethodDescription` identity.
5. **Behavioural coherence.** During a Work interval, the performer **shall** play the Role that binds the executed Method. *(No hidden role swaps.)*

---

### Taxonomic frame (within a context)

Within each `U.BoundedContext`, role names are organised as a **partial order** (refinements) plus an **incompatibility** relation (mutually exclusive roles). Typical **substrate‑neutral** anchors:

| Kernel Role       | Intent                                | System archetype              | Episteme archetype                       |   |
| ----------------- | ------------------------------------- | ----------------------------- | ---------------------------------------- | - |
| `TransformerRole` | Changes other holons via Method/Work. | Robot arm assembling casings. | Prover constructing a new lemma.         |   |
| `ObserverRole`    | Collects evidence / metrics.          | Sensor array on a test‑rig.   | Reviewer annotating an article.          |   |
| `SupervisorRole`  | Governs subordinate holons.           | PLC orchestrating a line.     | Meta‑analysis curator combining studies. |   |

> Domains refine these anchors: e.g., `CoolingCirculatorRole`, `CitationSourceRole`, `LemmaRole`.

---

### Running examples (design ↔ run on one page)

**System case — Cooling loop**
`PumpUnit#3#HydraulicPump:Plant‑A`
`HydraulicPump ↦binds↦ ChannelFluid` (design)
`run‑2025‑08‑08 isExecutionOf centrifugal_pump_curve.ld` and `performedBy PumpUnit#3` (run)
*(All behavioural/resource facts live in Work; the Role is the mask.)*

**Episteme case — Standard in design**
`RFC‑9110.pdf#ProtocolStandard:WorldWideWeb` justifies `MethodDescription` selection; the **system** bearing `TransformerRole` is the design service that executed the selection work. The episteme did **not** act.

**Collective vs set (safety pitfall)**
A **set** `{Alice, Bob, 3.14}` has no behaviour; a **team** is a **system** with boundary, coordination **Method**, and supervision **Work**; only the latter can bear agentic roles.

---

### Anti‑patterns (with safe rewrites)

1. **“Transformer as system subtype.”**
   ✗ *“`U.TransformerSystem` builds pumps.”*
   ✓ *“`RobotArm R‑45#Transformer:Plant‑A` executed Work W.”* (Role is a mask; behaviour is Method/Work.)

2. **“Role as part.”**
   ✗ *“The pump’s role is one of its components.”*
   ✓ Roles are **never** parts; components are substantial. Keep all `partOf` chains role‑free.

3. **“Episteme acts by itself.”**
   ✗ *“The PDF enforced the SOP.”*
   ✓ An **episteme** can hold roles like `ProtocolStandard` **in context**, but only a **system** performs the Method/Work that uses it.

4. **“Context leakage.”**
   ✗ *“Pluto is Planet and DwarfPlanet.”* (in one tacit space)
   ✓ *“`Pluto#Planet:Early20thCenturyAstronomy`; `Pluto#DwarfPlanet:IAU_2006_Definition`.”* No contradiction—different bounded contexts. (Illustrative of `U.RoleAssignment` semantics carried forward from the A.2.1.)

### Authoring guidance (for engineers and leads)

* **Name roles for intent, not mechanics.** Prefer `CoolingCirculatorRole` over `ChannelFluidWithCentrifugalProfile`.
* **Pin the context early.** If two teams disagree, split contexts and (optionally) define an alignment bridge; do not over‑generalise the role.
* **Document the binding chain.** For any operational claim, be ready to point to: `RoleAssigning → Method ↔ MethodDescription → Work`. (Readers’ dictionary: *BPMN workflow → MethodDescription; operation/job → Work.*)

### Conformance Checklist (CC‑A2.\*)

|                      ID | Requirement                                                                                                                                                                                                                                                                          | Practical test (manager‑oriented)                                                                                                                                                             |
| ----------------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|             **CC‑A2.1** | A **Role** SHALL NOT be a mereological part of any holon; roles are never constituents of holarchies.                                                                                                                                                                                | If a diagram shows `Role →(part‑of)→ Holon`, the model **fails**. Replace the edge with `playsRoleOf(Holon, Role, span)` (A.14 governs parts).                                                |
|             **CC‑A2.2** | Only a **System** can bear **behavioural** roles (e.g., `TransformerRole`, `AgentialRole`) and thus bind **Method**/**Work**; an **Episteme** MAY bear **non‑behavioural** roles (e.g., `ReferenceRole`, `ConstraintSourceRole`) only.                                               | Lint the model: any `U.Episteme` that `bindsMethod` or is a `performedBy` target **fails**; move behaviour to a system bearing the role and act on episteme **carriers** (A.7, A.12, A.15).   |
|             **CC‑A2.3** | Every **non‑abstract Role** SHALL `bindsMethod ≥ 1`; roles with no bound method are **abstract** and non‑executable.                                                                                                                                                                 | If a role participates in `Work` without some `Method ⟷ MethodDescription` chain, flag “unbound role” and add a binding (A.15).                                                                      |
|             **CC‑A2.4** | Every **role reference** in normative text SHALL be **context‑indexed** by a declared **Bounded Context** (local to the pattern or glossary). Local shorthand **“Transformer”** is permitted only if the pattern’s Glossary **re‑binds** it to “**System bearing TransformerRole**”. | If prose says “Transformer updates the spec”, the pattern MUST define the local alias and its target; otherwise rewrite to the canonical long form (E.10, A.7).                               |
|             **CC‑A2.5** | Each `playsRoleOf` relation SHALL declare a **TimeInterval** (`span`); open intervals are allowed but must be explicit.                                                                                                                                                              | Search for `playsRoleOf` without a span; add `@t₀..t₁` or an open bound. This prevents ambiguous overlaps (A.2 Solution).                                                                     |
|             **CC‑A2.6** | If two roles are declared **incompatible inside the same context**, a bearer SHALL NOT hold them over **overlapping** spans.                                                                                                                                                         | Check the context’s role‑compatibility grid; if overlaps exist, either split the Work by `PhaseOf` or change staffing (A.14; B.1.4/Γ\_time).                                                  |
|             **CC‑A2.7** | For any **Work** item, the `performedBy` system MUST be the bearer of the executing role **throughout the Work’s timespan**.                                                                                                                                                         | Join `performedBy(Work, Holon)` with `playsRoleOf(Holon, Role, span)` and assert `span ⊇ timespan(Work)`. Split Work if the bearer changes (A.15 §8.1).                                       |
|             **CC‑A2.8** | Every **Method** bound to a role SHALL be `isDescribedBy ≥ 1` **MethodDescription** (`U.Episteme`) and every **Work** SHALL be `isExecutionOf` exactly one **MethodDescription** version.                                                                                                          | If a Work lacks `isExecutionOf`, or a Method lacks `MethodDescription`, the audit fails (A.15; A.10 evidencing hook).                                                                                |
|             **CC‑A2.9** | **Evidence** for claims about roles and execution MUST anchor to **symbol carriers** (SCR/RSCR); self‑evidence is forbidden.                                                                                                                                                         | A role effectiveness claim without SCR/RSCR or with cyclic provenance fails (A.10).                                                                                                           |
|            **CC‑A2.10** | When a Role assignment implies **order** or **temporal** structure, the pattern SHALL defer to **Γ\_ctx**/**Γ\_time** rather than overloading role edges.                                                                                                                               | If argument order matters, use Γ\_ctx folds and record OrderSpec; version/evolution goes via Γ\_time (B.1.3 §4.5).                                                                            |
|            **CC‑A2.11** | Use of legacy nouns “creator/actor/agent” in Core text is prohibited unless they are explicitly typed as **roles** with bearers; the term **“Transformer”** is a local alias, **not** a type.                                                                                        | Scan for bare nouns; replace with “system bearing TransformerRole” or define an alias in the Glossary (A.7 canonical rewrites; E.10 registers).                                               |
| **CC‑A2.12 (advisory)** | A reified **RoleAssigning** object SHOULD capture `context`, `timespan`, optional `authority`, `justification (U.Episteme)`, and `provenance (U.Method)`.                                                                                                                              | Recommended for governance‑heavy domains; it improves explainability without changing Core semantics (ties to A.10; B.3 Trust).                                                               |

> **Note.** CC‑A2.2 aligns with **A.7 Role‑domain guards** (“behavioural roles’ domain = system; epistemes bear non‑behavioural roles only”).

---

### Consequences

| Benefit                     | Why it matters                                                                                                       | Trade‑off / Mitigation                                                                       |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **Category‑error immunity** | Clear firewall between **identity** (holarchies) and **function** (roles) prevents mixing “parts” with “masks”.      | Slight modelling overhead; templates provide checklists (A.7, A.14).                         |
| **Operational clarity**     | Who does what, when, and under which mask becomes audit‑ready (`performedBy ⊆ playsRoleOf`).                         | Requires spans on Role assignments; mitigated by default “open‑ended” spans in drafts.          |
| **Epistemic hygiene**       | Knowledge holons contribute as **evidence** or **constraints**, never as doers.                                      | Authors must rewrite anthropomorphic prose; canonical rewrites help.                         |
| **Cross‑context pluralism** | Same bearer can hold different roles across contexts without contradiction; differences are explicit in the binding. | Requires declaring the **bounded context**; E.10 eases the ceremony with registers/aliases.  |
| **Γ‑coherence**             | Order/time/aggregation stay in Γ‑operators, not overloaded into “role" edges.                                        | Authors learn when to call Γ\_ctx/Γ\_time; the Part B on‑ramp is short.                      |

---

### Rationale (post‑2015 cross‑domain corroboration)

*Why insist on roles as contextual masks and externalised transformers?*

1. **Constructor Theory (2015–2022).** Post‑2015 work by Deutsch & Marletto re‑centres physics on **possible tasks and constructors** rather than objects, mirroring FPF’s **TransformerRole**: behaviour is attached to “who can realise a task,” not to substance per se. Our separation of **SubstantialHolon** vs **Role** and the insistence on **external** transformers directly echo this shift. *(Conceptual alignment noted in A.2 Solution and A.12 intent.)* 
2. **Layered Control Architectures (Matni–Ames–Doyle, 2024).** The modern control stack cleanly **externalises** regulators and planners relative to plants. FPF’s obligatory “system bearing TransformerRole” (A.7, A.12) is isomorphic to that separation, keeping supervision and actuation **outside** the controlled holon. 
3. **Active‑Inference / Agency spectrum (2017–2023).** Contemporary models treat agency as **graded** and **contextual** (percept‑act loops tuned by free‑energy bounds). A.13 adopts exactly this: **AgentialRole** is a role worn by a holon, with graded measurements via **Agency‑CHR**, not a static type.
4. **Basal Cognition & multi‑scale organisation (2019–2024).** Fields & Levin argue for **cross‑scale** control and information flows; FPF encodes this via Γ‑flavours and the **Meta‑Holon Transition** triggers, ensuring Role assignments compose across scales without collapsing identity into function.
5. **Knowledge ecosystems & safety cases (2018–2025).** Modern assurance relies on **traceable evidence** and conservative integration (no “truth averaging”): our A.10 anchors (SCR/RSCR) and Γ\_epist’s **weakest‑link** fold implement that discipline and forbid self‑evidence. 

> Summing up: post‑2015 science and engineering converge on **roles as contextual capabilities**, **externalised control**, and **traceable evidence**. A.2 codifies these insights in a substrate‑neutral way, keeping the Core small yet powerful.

---

### Relations

* **Builds on:**
  **A.1 Holonic Foundation** (role/mereology split), **A.7 Strict Distinction** (role ≠ behaviour; episteme ≠ carrier), **A.14 Advanced Mereology** (no roles in holarchies).  
* **Specialises / Coordinates with:**
  **A.13 Agential Role & Agency Spectrum** (behavioural roles over systems; graded agency), **A.15 Role–Method–Work Alignment** (bindsMethod / isExecutionOf discipline). 
* **Constrains / Used by B‑cluster:**
  **B.1 Universal Algebra of Aggregation (Γ)** (keep order/time in Γ\_ctx/Γ\_time; keep provenance in Γ\_epist), **B.2 Meta‑Holon Transition** (promotion when supervision/closure appears), **B.3 Trust & Assurance** (evidence & congruence).  
* **Interlocks with E‑cluster (governance & language):**
  **E.10 Lexical Discipline** (registers, tier disambiguation, local aliases like “Transformer”), **E.5.1 DevOps Lexical Firewall** (ban tooling tokens in Core patterns). 
* **Reinforces:**
  **A.10 Evidence Graph Referring** (external transformer; SCR/RSCR), **A.12 External Transformer Principle** (agent externalisation). 
  
  # A.2.1 — U.RoleAssignment: Contextual Role Assignment \[D]

*with `Role Performance View`, `U.RoleStateGraph (RSG)`, and `Role Characterisation Space (RCS)` hooks*

**Status.** Definitional pattern \[D], kernel‑level.
**Builds on:** A.1 **Holonic Foundation**, A.1.1 **`U.BoundedContext`**, A.2 **Role Taxonomy**.
**Coordinates with.** A.13 **Agential Role & Agency Spectrum**, A.15 **Role–Method–Work Alignment**, E.10.D1 **D.CTX (Context discipline)**, E.10.D2 **Strict Distinction**.
**Lexical discipline.** *Context* ≡ `U.BoundedContext` (E.10.D1). *Appointment* is **colloquial only** and **MUST NOT** appear in normative clauses. Canonical term: **Role Assignment**.

---


---

## 13 · Integration with A.15 — Role–Method–Work alignment

> **One line.** A `U.MethodDescription` **names** the roles it needs; a `U.Work` **cites** the concrete `U.RoleAssignment` that enacted the step; the **RSG state + window** gates that enactment.

### 13.1 Design‑time Standard (inside `U.MethodDescription`)

For every **MethodStep**:

* **`requiredRoles`** — a list of `U.Role` **from the same Context as the step**.
  *Example.* In `Hospital.OR_2025`, step “Make incision” has `requires: [IncisionOperatorRole]`.
* **Role algebra in‑Context** applies: if the Context defines `IncisionOperatorRole ≤ SurgeonRole`, then `requires: [SurgeonRole]` also admits holders of `IncisionOperatorRole`.
* **Separation of concerns.** Capability checks (does the holder *can*?) belong to `U.Capability` and resource limits; **authorization** belongs to `U.RoleAssignment` + RSG.

### 13.2 Run‑time check (inside `U.Work`)

A `U.Work` record must carry:

* **`performedBy` =** a concrete **`U.RoleAssignment`** (not just a person/system name).
* **Window gate.** The Work timestamp falls inside the assignment’s `@Window`.
* **State gate.** At that timestamp, an **enactable** state for the assignment is proven by a **`StateAssertion`** (the checklist verdict for a named RSG state).
* **Role algebra gate.** The assignment’s `role` is either one of `requiredRoles` or a **specialization (`≤`)** thereof; bundles (`⊗`) expand to conjunctions; incompatibilities (`⊥`) forbid overlaps on the same holder.

### 13.3 Evaluation & acceptance (link to services & deontics)

* **Observation.** The Work produces `U.Observation`(s).
* **Evaluation.** A `U.Evaluation` compares Observations with **AcceptanceClause**(s) referenced by a **Service** or a **RequirementRole**.
* **SoD hook.** If the step or evaluation demands independence (e.g., “not performed by its reviewer”), enforce via `⊥` between `PerformerRole` and `ReviewerRole` **in the same Context**.

### 13.4 Planning & scheduling (design‑time “who will enact”)

* **`U.WorkDescription`** (renamed from “WorkPlan”) binds forthcoming steps to **candidate RoleAssignments** and time windows.
* **Checks before the fact.** Validate windows (no gaps/overlaps where disallowed), enforce `⊥`, ensure expected RSG state will be **enactable** at scheduled time (or flag a pre‑flight checklist).

> **Didactic cue.** Think **“Step asks for badges; Run cites a badge; Badge must be valid & green.”**
> (Badge = RoleAssignment; valid = window; green = RSG state with a fresh StateAssertion.)

---


---

## 9 · Capability thresholds on steps (how A.15 uses this concept)

A step in a **Method** may define **required roles** (assignment) and **capability thresholds** (ability). A Work passes the gate if:

1. **assignment check:** the Work’s `performedBy` points to a valid **Role assignment** that covers the step window and satisfies the role relation (including specialization `≤` inside the context).
2. **Ability check:** the **holder** of that Role assignment has a **capability** whose **WorkScope covers the step’s JobSlice** (i.e., declared superset) and whose **WorkMeasures** meet the step’s threshold(s) **within `Γ_time(W)` and while the capability’s **QualificationWindow** includes *W***.

**Idioms managers can reuse (plain text):**

* *“S1 requires `IncisionOperatorRole` and Precision ≤ 0.2 mm (OR\_2025 norms) **in window W**.”*
* *“S2 requires `PlannerRole`, **WorkScope ⊇ JobSlice\[W]**, and Optimality ≥ 0.90 on `JS_Schedule_v4`.”*

**What to avoid:**

* Putting “Precision ≤ 0.2 mm” into the Role name. Keep thresholds attached to the **step**; keep **ability** on the **holder**.

---


---

## A.13 The Agential Role & Agency Spectrum \[A]

> *“Agency is not a kind of thing; it is a way some systems operate.”*

### 1 · Intent & Context

The concept of "agency"—the capacity of an entity to act purposefully—is central to engineering, biology, and AI, yet it remains one of the most overloaded and ambiguous terms. Without a precise, falsifiable, and substrate-neutral definition, models of autonomous systems risk descending into "self-magic," where actions have no clear cause and accountability is lost.

This pattern builds directly upon the foundations laid in the FPF Kernel to provide that definition. A.1 established that only a **`U.System`** can be the bearer (`holder`) of behavioral roles.  A.2.1 defined the universal `U.RoleAssignment` (`Holder#Role:Context`) as the canonical way to assign roles. A.3 and A.12 defined the `TransformerRole` and the principle of the external agent.

The intent of this pattern is to:
1.  Formally define **agency** not as an intrinsic *type* of holon, but as a **contextual Role Assignment**.
2.  Introduce a measurable, multi-dimensional **spectrum of agency** via a dedicated Characterization (`Agency-CHR`), moving beyond a simple binary "agent/not-agent" switch.
3.  Provide a clear, **didactic grading system** that allows engineers and managers to assess and communicate the level of autonomy of any system in a consistent, evidence-backed manner.

### 2 · Problem

If agency is treated as a monolithic, intrinsic property or a mere label, four critical failure modes emerge, undermining the rigor of FPF:

1.  **Episteme-as-Actor:** Models might incorrectly assign agency to knowledge artifacts (`U.Episteme`), leading to nonsensical claims like "the specification decided to update the system." This is a direct violation of **Strict Distinction (A.7)**.
2.  **Type Inflation:** Introducing a `U.Agent` as a new base type alongside `U.System` and `U.Episteme` would violate **Ontological Parsimony (C-5)** and create conflicts with the dynamic nature of roles. A system might act as an agent in one context and a passive component in another; a static type cannot capture this.
3.  **Unfalsifiable Claims:** Without a measurable basis, "agency" becomes a subjective label. A team might call their system an "agent" for marketing purposes, but this claim has no verifiable meaning and cannot be audited, violating **Evidence Graph Referring (A.10)**.
4.  **The Binary Trap:** A simple "agent/not-agent" classification is too coarse. It fails to distinguish between a simple thermostat, a predictive cruise control system, and a strategic, self-learning robotic swarm, even though their cognitive capabilities differ by orders of magnitude.

### 3 · Forces

| Force | Tension |
| :--- | :--- |
| **Scientific Fidelity vs. Simplicity** | Contemporary science (e.g., Active Inference) models agency as a continuous, scale-free spectrum. FPF needs to honor this rigor while providing a simple, teachable model for practitioners. |
| **Role vs. Type** | The intuition is to think of an "Agent" as a *type* of thing. FPF's architecture demands that it be modeled as a *role* to preserve dynamism and ontological hygiene. |
| **Measurement vs. Label** | Engineers and managers need a quick, intuitive label (e.g., "this is a Level 3 agent"), while formal assurance requires a detailed, multi-dimensional, evidence-backed measurement. |
| **System-only Action vs. Collective Action**| How does agency apply to groups like teams or swarms? This requires a clear link to the rule from A.1 that any *acting group* must be modeled as a `U.System`. |

### 4 · Solution

FPF's solution is threefold: it defines an Agent via `U.RoleAssignment` (A.2.1), makes agency measurable with a dedicated Characterization, and provides a didactic summary via a graded scale.

#### 4.1 The Core Definition: Agent as a Contextual Role Assignment

An **"Agent"** in FPF is not a fundamental type. It is a convenience term (a Register 1 / Register 2 label) for a specific kind of **Contextual Role Assignment (`U.RoleAssignment`)**:

> `Agent ≍ U.RoleAssignment(holder: U.System, role: U.AgentialRole, context: U.BoundedContext)`

This means an Agent is simply a **`U.System`** that is currently playing an **`AgentialRole`** within a specific **`U.BoundedContext`**.

*   **No `U.Agent` Type:** To be clear, there is **no `U.Agent` base type** in the FPF Kernel. This avoids type inflation and preserves the dynamic nature of roles.
*   **Epistemes Cannot Be Agents:** As the `holder` must be a `U.System`, this definition constitutionally forbids `U.Episteme`s from being agents, preventing the "episteme-as-actor" category error.
*   **Canonical Syntax:** The technical notation for an agent is `System#AgentialRole:Context`.

#### 4.2 The `AgentialRole` and its Specializations

*   **`U.AgentialRole`:** This is the abstract `U.Role` that grants a `U.System` the capacity for goal-directed action within a context. It is the "license to act."
*   **Specialized Roles:** More specific behavioral roles like `TransformerRole` and `ObserverRole` are considered **specializations or sub-roles** of `AgentialRole`. They describe *what kind* of agential action is being performed at a given moment.
    *   A system playing `TransformerRole` is an Agent *that is currently modifying another holon*.
    *   A system playing `ObserverRole` is an Agent *that is currently gathering information*.
    This creates a clean hierarchy: a `Transformer` is always an `Agent`, but an `Agent` is not always a `Transformer` (it could be observing, planning, or idle).

#### 4.3 Measuring Agency: The `Agency-CHR` and the Spectrum

Agency is not a binary switch; it is a multi-dimensional spectrum of capabilities. FPF models this using a dedicated architheory, **`Agency-CHR` (C.9)**, which is a **Characterization** that attaches a set of measurable properties to a `U.RoleAssignment`.

The `Agency-CHR` profile is grounded in contemporary research (e.g., Active Inference, Basal Cognition) and includes the following key characteristics. Each is measured for a specific agent in a specific context and must be backed by evidence (A.10).

1.  **Boundary Maintenance Capacity (BMC):** The ability of the system to maintain its structural and functional integrity against perturbations. *(How robust is it?)*
2.  **Predictive Horizon (PH):** The temporal or causal depth of the agent's internal model. *(How far ahead can it "see"?)*
3.  **Model Plasticity (MP):** The rate at which the agent can update its internal model (`U.GenerativeModel`) in response to prediction errors (`U.Error`). *(How quickly can it learn?)*
4.  **Policy Enactment Reliability (PER):** The probability that the agent will successfully execute its chosen `U.Method` under operational conditions. *(How reliably does it do what it decides to do?)*
5.  **Objective Complexity (OC):** A measure of the complexity of the `U.Objective` the agent can pursue, from simple set-points to abstract, multi-scale goals.

#### 4.4 The Agency Grade (Didactic Layer)

While the multi-dimensional `Agency-CHR` profile is essential for formal assurance, engineers and managers need a simpler, at-a-glance summary. The **Agency Grade** is a **non-normative, didactic** scale from 0 to 4 that synthesizes the CHR profile into an intuitive level of autonomy.

| Grade | Label | Typical `Agency-CHR` Profile (Conservative Lower Bound) | Archetypal Example |
| :--- | :--- | :--- | :--- |
| **0** | **Non-Agential** | `BMC ≈ 0`, `PH ≈ 0`, `MP ≈ 0` | A rock, a document, a passive structural component. |
| **1** | **Reactive** | `BMC > 0`, `PH ≈ 0`, `MP ≈ 0` | A thermostat; a simple feedback controller. Follows fixed rules. |
| **2** | **Predictive** | `BMC > 0`, `PH > 0`, `MP ≈ 0` | A model-predictive controller with a fixed model; a chess engine that plans moves but doesn't learn new strategies. |
| **3** | **Adaptive** | `BMC > 0`, `PH > 0`, `MP > 0` | A self-calibrating sensor system; a machine learning agent that updates its model with new data. |
| **4** | **Reflective/Strategic** | High `BMC`, `PH`, `MP`, `PER`, and `OC`. Capable of meta-cognition (reasoning about its own reasoning) and pursuing abstract goals. | An autonomous R&D system; a cohesive, self-organizing DevOps team. |

**Crucial Distinction:** The `Agency-CHR` profile is the **normative evidence**. The Grade is a **pedagogical shortcut**. An artifact cannot claim a grade without having a corresponding, auditable CHR profile to back it up.

#### 5 · Archetypal Grounding

The universal pattern of agency, defined as a `Contextual Role Assignment` and measured by the `Agency-CHR`, manifests across all domains. The following table demonstrates its application to the FPF's two primary archetypes: a `U.System` and a collective `U.System` (a team), while explicitly showing why a `U.Episteme` cannot be an agent.

| Archetype | Holder (`U.System`) | Role & Context (`#Role:Context`) | `Agency-CHR` Profile Sketch | Resulting Agency Grade |
| :--- | :--- | :--- | :--- | :--- |
| **Simple Controller** | `Thermostat_Model_T800` | `#AgentialRole:HomeHeatingSystem` | `BMC`: High (maintains temp). <br> `PH`: Zero (no prediction). <br> `MP`: Zero (fixed logic). <br> `PER`: Very High. <br> `OC`: Low (single set-point). | **Grade 1 (Reactive)** |
| **Advanced Controller** | `PredictiveCruiseControl_v3` | `#AgentialRole:VehicleDynamics` | `BMC`: High. <br> `PH`: High (predicts traffic flow). <br> `MP`: Zero (fixed model). <br> `PER`: High. <br> `OC`: Medium (optimization). | **Grade 2 (Predictive)** |
| **Learning System** | `SelfCalibratingSensorArray` | `#AgentialRole:IndustrialProcess` | `BMC`: High. <br> `PH`: High. <br> `MP`: Medium (learns drift). <br> `PER`: High. <br> `OC`: Medium. | **Grade 3 (Adaptive)** |
| **Collective Agent** | `DevOpsTeam_Phoenix` (a collective `U.System`) | `#AgentialRole:ProjectPhoenix` | `BMC`: High (maintains velocity). <br> `PH`: High (sprint planning). <br> `MP`: High (retrospectives). <br> `PER`: Medium-High. <br> `OC`: High (abstract business goals). | **Grade 4 (Reflective/Strategic)** |
| **Knowledge Artifact** | `ISO_26262_Standard.pdf` (`U.Episteme`) | **N/A** (Cannot be a holder of an `AgentialRole`) | N/A | **Grade 0 (Non-Agential)** |

**Key takeaway from grounding:**
This table makes the abstract model concrete. It shows that the FPF agency model can precisely differentiate between simple controllers and complex learning systems. It also reinforces the **Strict Distinction** principle: the ISO standard (`U.Episteme`) is a crucial **justification (`justification?`)** for the actions of an agent (like the DevOps team), but it is never an agent itself.

#### 6 · Conformance Checklist

To ensure the agency model is applied rigorously and consistently, all FPF artifacts must adhere to the following normative checks.

| ID | Requirement (Normative Predicate) | Purpose / Rationale |
| :--- | :--- | :--- |
| **CC-A13.1 (Holder Type)** | The `holder` of a `U.RoleAssignment` with `role: U.AgentialRole` **MUST** be a `U.System`. | Prevents the "episteme-as-actor" category error. Enforces **Strict Distinction (A.7)**. |
| **CC-A13.2 (RoleAssignment Mandate)** | Any claim of agency **MUST** be represented by a complete `U.RoleAssignment` instance, including an explicit `holder`, `role`, and `context`. | Ensures that agency is always modeled as contextual and bound to a specific bearer, not as a free-floating property. |
| **CC-A13.3 (CHR Evidence)** | Any claim about an Agent's grade or level of autonomy **MUST** be substantiated by an auditable `Agency-CHR` profile with Evidence Graph Ref (A.10). | Makes claims of agency falsifiable and prevents "agency by marketing." |
| **CC-A13.4 (Grade is Didactic)**| The **Agency Grade (0-4)** **SHALL NOT** be used as a normative input for formal reasoning. It is a didactic summary of the `Agency-CHR` profile. | Prevents oversimplification in formal models. The detailed profile, not the summary grade, must be used for assurance cases. |
| **CC-A13.5 (Collective as System)** | To claim agency for a collective (e.g., a team, a swarm), the collective **MUST** first be modeled as a `U.System` with a defined `U.Boundary` and a coordination `U.Method`. | Prevents the error of assigning agency to a mere set or collection (`MemberOf`). Aligns with **A.1** and **A.14**. |
| **CC-A13.6 (MHT for Emergent Agency)** | If a collection of systems, previously non-agential or at a lower grade, develops a new supervisory structure and crosses a documented `Agency-CHR` threshold, a **Meta-Holon Transition (MHT, B.2)** **MUST** be declared. | Makes the emergence of collective agency an explicit, auditable event, preventing "magic" emergence. |

#### 7 · Consequences

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Category Safety & Clarity:** The pattern provides a clear, unambiguous definition of agency that prevents common modeling errors and is consistent across all of FPF. | **Increased Modeling Granularity:** Requires modelers to think in terms of Role-assignments and contexts, which is slightly more complex than just labeling something an "Agent." *Mitigation:* The `Holon#Role:Context` syntax and tooling support make this manageable in practice. |
| **Falsifiable & Measurable Agency:** By grounding agency in the `Agency-CHR`, the framework transforms a vague philosophical concept into a set of concrete, evidence-backed engineering properties. | **Measurement Effort:** Populating the `Agency-CHR` profile requires real work (testing, analysis, data gathering). *Mitigation:* The profile can be built iteratively. An initial estimate can be used, with the understanding that its `Reliability (R)` score is low until backed by evidence. |
| **Scalable Autonomy Model:** The graded scale provides a sophisticated language for describing and comparing different levels of autonomy, from simple automation to strategic intelligence. | **Risk of Misinterpreting Grades:** The simple 0-4 scale could be misused as a simplistic marketing label. *Mitigation:* The normative requirement (**CC-A13.4**) to always link a grade to its underlying CHR profile acts as a guardrail against this. |
| **Elegant Handling of Collectives:** The pattern provides a clean way to model the agency of teams, swarms, and organizations without violating ontological principles. | - |

#### 8 · Rationale

This pattern's strength comes from its synthesis of contemporary, post-2015 research into a single, operational model.

*   **Grounded in Science:** The move away from a binary, type-based view of agency towards a **graded, spectrum-based model** is directly aligned with modern research in Active Inference (Friston et al.), Basal Cognition (Fields, Levin), and evolutionary cybernetics. The `Agency-CHR` provides a direct, practical implementation of these ideas.
*   **Ontologically Sound:** By defining an Agent as a **Contextual Role Assignment**, the pattern avoids the ontological pitfalls of creating a new base type. It fully embraces the FPF's core architectural principle of separating **substance (`holder`)** from **function (`role`)** within a **context**. This aligns with best practices from foundational ontologies (like UFO) and the principles of **Strict Distinction (A.7)**.
*   **Pragmatic and Actionable:** The pattern is designed for engineers and managers. The `Agency Grade` provides a quick communication tool, while the underlying `Agency-CHR` provides the detailed, auditable data needed for formal assurance and risk management. This duality satisfies both **Didactic Primacy (P-2)** and **Pragmatic Utility (P-7)**.

In essence, this pattern does not *invent* a new theory of agency. It **distills and operationalizes** the emerging scientific consensus, packaging it into a rigorous, falsifiable, and practical tool for the FPF ecosystem.

#### 9 · Relations

*   **Builds on:**
    *   `A.1 Holonic Foundation`: Establishes that only `U.System`s can be bearers of behavioral roles.
    *   `A.2 Role Taxonomy`: Provides the universal  Contextual Role Assignment (`U.RoleAssignment`) mechanism.
    *   `A.12 External Transformer`: The actions of an Agent are modeled using the external transformer principle.
*   **Coordinates with:**
    *   `B.2 Meta-Holon Transition (MHT)`: A significant jump in the `Agency-CHR` of a collective can trigger an MHT.
    *   `B.3 Trust & Assurance Calculus`: The `Agency-CHR` profile provides crucial inputs for assessing the reliability and safety of an autonomous system.
    *   `D.2 Multi-Scale Ethics Framework`: The Agency Grade is used to determine the level of moral responsibility and accountability assigned to a system.
*   **Instantiates:**
    *   The `Agency-CHR` (C.9) architheory, which provides the formal definitions for the characteristics (BMC, PH, etc.).


---

# A.14 — Advanced Mereology: Components, Portions, Aspects & Phases  \[A]


#### 1 · Context — why an advanced mereology?

FPF’s holonic world is built from **part–whole** relations. Early drafts distinguished structural vs. conceptual parthood (e.g., **ComponentOf**, **ConstituentOf**) but practical modelling kept hitting two recurrent gaps:

1. **Quantities vs. parts.** Engineers routinely need “some of the fuel”, “the first 10 pages”, “a 30% subset of data”. This is not a component; it is a **portion** of a stuff‑like whole, governed by measures and conservation.

2. **Change vs. replacement.** Authors need to say “the prototype **before calibration**”, “v2 of the spec”, “shift 1 vs. shift 2 of the same run”. That is not a new whole; it is a **phase** of the same carrier across time.

This section introduces two **normative** sub‑relations of `partOf` that close those gaps and lock them to the rest of the kernel:

* **PortionOf** — metrical, measure‑preserving parthood of stuffs and other measurables.
* **PhaseOf** — temporal parthood of the *same* carrier across an interval.

It also restates guard‑rails that keep **roles** and **recipes** outside mereology (A.15), and clarifies how **MemberOf** fits (preview: **collections** are grounded constructively in **C.13 Compose‑CAL** via `Γ_m.set`; **collective agency** is handled outside mereology in **A.15 Role–Method–Work**).

**Publication note (Working‑Model first).** Read A.14 together with **E.14 Human‑Centric Working‑Model** and **B.3.5 CT2R‑LOG**: publish relations on the **Working‑Model** surface; when assurance is sought, **ground downward**. For structural claims that require extensional identity, use the **Constructive** shoulder via **Compose‑CAL Γ_m (sum | set | slice)**; order/time stay outside mereology (Γ_time / Γ_method).

#### 2 · Problem — what breaks without these distinctions?

If we only have “generic partOf” (plus Component/Constituent), four classes of errors appear:

1. **Conservation errors.** Treating “20 L of fuel from Tank A” as a component leads to nonsense: adding and removing such “components” does not respect quantities; Γ\_sys proofs violate Σ‑balance.

2. **Temporal smearing.** Flattening “before/after”, or “v1/v2” into one timeless whole collapses history; Γ\_time and Γ\_method cannot justify order‑sensitive properties; audits cannot reproduce conditions.

3. **Identity confusion.** Modelling “new version” as “new component” either breaks identity (it is still the *same* holon evolving) or hides a **Meta‑Holon Transition** when identity really changes.

4. **Role leakage.** Functional/organisational roles sneak into part trees (“the PumpRole is part of the plant”), violating A.15 and making structural reasoning brittle.

---

#### 3 · Forces

| Force                              | Tension                                                                                                         |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Expressiveness vs. Parsimony**   | We need new relations (Portion, Phase) ↔ we must keep the catalogue minimal and orthogonal.                     |
| **Universality vs. Domain nuance** | One set of rules must serve physical systems and epistemes ↔ measurement and time behave differently by domain. |
| **Identity vs. Change**            | Preserve “the same carrier through change” ↔ allow explicit re‑identification when invariants fail.             |
| **Static structure vs. Histories** | Part trees should be simple ↔ real work requires phased histories and measured slices.                          |

#### 4 · Solution — extend the mereology catalogue, keep it clean

**A.14 defines two additional sub‑relations of `partOf`** and **re‑affirms the firewall** between mereology and the role/recipe layer:

1. **PortionOf** — for *measured* parts of a whole (stuffs and other extensives).
2. **PhaseOf** — for *temporal* parts of the same carrier.
3. **No roles/recipes in mereology.** `U.Role`, `U.Method`, `U.MethodDescription` are **never** parts (A.15).
4. **MemberOf stays, but constructive aggregation and agency live elsewhere.** `MemberOf` remains available to state collections and collectives; **their collection‑as‑whole may be constructed via Γ\_m.set (Compose‑CAL, C.13)**, while **composition and agency are handled in B.1.7 Γ\_collective** (not in A.14).

The classical pair **ComponentOf** (structural, discrete) and **ConstituentOf** (conceptual, logical/epistemic) remain as in the kernel; A.14 only clarifies **how to tell them apart from Portion/Phase** (§ 6).

#### 5 · Formal cores (normative semantics)

##### 5.1 PortionOf — metrical part of a measurable whole

**Intent.** Capture “some of the same stuff/extent”, governed by a measure that adds up.

**Applicability.** Any `U.Holon` that carries an **extensive** measure μ on the chosen scope
(examples: mass, volume, length‑of‑text, byte size, wall‑time budget).

**Primitive.** `PortionOf(x, y)` means: *x is the same kind of stuff/content as y, but less*.

**Axioms (A14‑POR‑\*)**

* **POR‑1 (Partial order).** PortionOf is reflexive, antisymmetric, transitive on its domain.
* **POR‑2 (Metrical dominance).** If `x ProperPortionOf y` then `0 < μ(x) < μ(y)` for the agreed μ.
* **POR‑3 (Additivity on disjoint portions).** If `x ⟂ y` (no overlap) and both PortionOf y, then `μ(x ⊔ y) = μ(x)+μ(y)` and `x ⊔ y PortionOf y`.
* **POR‑4 (Kind integrity).** x and y must share the same **measure kind** and **unit** (or a declared conversion).
* **POR‑5 (Boundary compatibility).** For physical wholes, the whole’s boundary encloses the union of its portions; cross‑boundary “leaks” are interactions, not portions.

**Didactic tests.**
✔ “5 kg from a 20 kg billet” — PortionOf.
✔ “Pages 1–10 of the report” — PortionOf (μ = page or token count).
✘ “The pump module of the plant” — **ComponentOf**, not PortionOf.
✘ “The Methods section of the paper” — **ConstituentOf**, not PortionOf.


##### 5.2 PhaseOf — temporal part of the same carrier

**Intent.** Capture “the same holon during a sub‑interval”, preserving identity through change.

**Applicability.** Any `U.Holon` that persists across time with a recognised **carrier identity**.

**Primitive.** `PhaseOf(x, y)` means: *x is y restricted to a proper time interval*.

**Axioms (A14‑PHA‑\*)**

* **PHA‑1 (Partial order).** PhaseOf is reflexive, antisymmetric, transitive (on the same carrier).
* **PHA‑2 (Coverage).** The whole is the union of its maximal, non‑overlapping phases over its lifetime interval.
* **PHA‑3 (No paradoxical overlap).** Phases of the **same carrier** do not overlap in time; overlapping variants require `PhaseOf` on *aspects* or different carriers.
* **PHA‑4 (Identity through change).** Properties may vary between phases, but the carrier’s identity criteria hold continuously (e.g., same serial number, same legal identity, same theorem statement).
* **PHA‑5 (Escalation to MHT).** If identity criteria break (e.g., metamorphosis with new objectives), **declare a Meta‑Holon Transition (B.2)** rather than a PhaseOf.

**Didactic tests.**
✔ “PumpUnit#3 **before** calibration” — PhaseOf(Pump#3\_pre, Pump#3).
✔ “Spec v2” — PhaseOf(Spec\_v2, Spec), on the **MethodDescription** artefact.
✔ “Shift 1 of the same batch run” — PhaseOf(Work\_shift1, Work).
✘ “Prototype vs. production unit” — likely **different carriers**; use ComponentOf/ConstituentOf or MHT per criteria.

##### 5.3 CT2R‑LOG & Compose‑CAL handshake *(normative link)*

* **Structural claims** published on the Working-Model surface **SHALL** be justified, when assurance is required, by a **Constructive** grounding narrative using **Γ_m.sum | Γ_m.set | Γ_m.slice** and **linked with `tv:groundedBy`** (see **B.3.5**; **C.13**).  
* **PhaseOf** is **temporal parthood**; it **SHALL NOT** be grounded via Γ\_m. Its assurance follows identity‑through‑time criteria (CC‑PHA‑1..3) and Γ\_time ordering (B.1.4).  
* **MemberOf** remains **non‑mereological** (CC‑MEM‑2). When modelling a collection‑as‑whole for assurance purposes, the constructive basis is **Γ\_m.set**; no **ComponentOf** inferences follow from **MemberOf**.

#### 6 · Choosing the right relation (decision table)

| You want to say…                                             | Use                  | Why                                                                                |
| ------------------------------------------------------------ | -------------------- | ---------------------------------------------------------------------------------- |
| “This is a *piece* of the same stuff (lower amount/extent).” | **PortionOf**        | Governed by a measure μ and conservation (Σ‑additive).                             |
| “This is a *discrete part* that sits *inside* the whole.”    | **ComponentOf**      | Structural parthood; boundary‑respecting, not measured by μ.                       |
| “This is a *logical part* in a conceptual whole.”            | **ConstituentOf**    | Sections, lemmas, clauses, conceptual assembly.                                    |
| “This is the *same thing* during a *sub‑interval*.”          | **PhaseOf**          | Temporal slicing with identity continuity.                                         |
| “This *item belongs to that collection/collective*.”         | **MemberOf**         | Not a building block of the whole; composition handled in **B.1.7 Γ\_collective**. |
| “This system *plays a Role or position*.”          | **playsRole** (A.15) | Roles are contextual masks, never parts.                                           |

> **Firewall reminder.** If your sentence contains “role”, “policy”, “process/workflow/SOP/script”, you are likely talking about **A.15** (roles/recipes/runs), **not** A.14.

---

#### 7 · Archetypal grounding (System / Episteme)

| Relation                       | `U.System` example                                     | `U.Episteme` example                                        |
| ------------------------------ | ------------------------------------------------------ | ----------------------------------------------------------- |
| **PortionOf**                  | 50 L from a 200 L fuel tank (μ = volume).              | Pages 1–10 from a 120‑page report (μ = page/token count).   |
| **ComponentOf**                | Impeller **ComponentOf** PumpUnit.                     | Figure 2 **ComponentOf** Poster Layout (physical artefact). |
| **ConstituentOf**              | Control law **ConstituentOf** Controller Design.       | Lemma A **ConstituentOf** Theorem Proof.                    |
| **PhaseOf**                    | PumpUnit#3 *before*/*after* calibration (same serial). | Spec v1 → v2 (same document lineage).                       |
| MemberOf (for reference) | “is an element of a collection/collective”; use when a grouping is explicitly treated as a whole set, without implying component integration. Not a building block of the whole; **constructive aggregation** is handled in **C.13 Compose‑CAL** (`Γ_m.set`). If the grouping is expected to **act**, model a **collective system** (A.15). |

#### 8 · Conformance Checklist & type guards (normative)

##### **8.1 Global firewall and scope**

| ID            | Requirement                                                                                 | Purpose                                                 |
| ------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **CC‑A14‑0**  | No `U.Role`, `U.Method`, or `U.MethodDescription` **MAY** occur as a node in any `partOf` chain.   | Keeps parthood purely structural/conceptual (see A.15). |
| **CC‑A14‑0b** | `MemberOf` **MUST NOT** imply, entail, or be auto‑rewritten into any `partOf` sub‑relation. | Separates collections/collectives from parthood.        |
| **CC‑A14‑0c** | `SerialStepOf` / `ParallelFactorOf` **MUST NOT** appear in any `partOf` chain or table in A.14; model order via **A.15** (**Γ_ctx/Γ_method**). | Prevents the “order‑as‑structure” category error.       |

##### **8.2 PortionOf guards**

| ID                                 | Requirement                                                                                                                                                               | Purpose                                 |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| **CC‑POR‑1 (Domain)**              | `PortionOf(x,y)` is valid only if the modelling scope declares at least one **extensive measure** μ for y (mass, volume, token count, byte size, wall‑time budget, etc.). | Prevents “portion” without a measure.   |
| **CC‑POR‑2 (Kind)**                | x and y **SHALL** share the same μ‑kind and compatible units (or an explicit conversion).                                                                                 | Prevents apples‑to‑oranges addition.    |
| **CC‑POR‑3 (Monotone additivity)** | For disjoint portions `x ⟂ z` with `PortionOf(·,y)`: μ(x ⊔ z) = μ(x)+μ(z).                                                                                                | Secures Σ‑reasoning and Γ\_sys proofs. |
| **CC‑POR‑4 (Boundary)**            | For physical systems, the whole’s boundary encloses the union of portions; cross‑boundary flows are **not** portions.                                                     | Distinguishes stock vs flow.            |
| **CC‑POR‑5 (Non‑replacement)**     | “Replacing 20% of y by v” **MUST** be modelled as **PortionOf** removal + **Component/Constituent** insertion, not as a single PortionOf rewrite.                         | Avoids silent identity change.          |

##### **8.3 PhaseOf guards**

| ID                                    | Requirement                                                                                                                                                      | Purpose                                |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| **CC‑PHA‑1 (Carrier identity)**       | `PhaseOf(x,y)` requires an explicit **identity criterion** for y valid over the union of phases (e.g., serial number, legal identity, theorem statement).        | Prevents re‑identification by stealth. |
| **CC‑PHA‑2 (Coverage & non‑overlap)** | The lifetime of y equals the union of its maximal, non‑overlapping phases (on the same aspect).                                                                  | Enables Γ\_time composition and audit. |
| **CC‑PHA‑3 (Aspect clarity)**         | If two temporal slices of y overlap, they **MUST** be phases of **different aspects** (e.g., mechanical‑state vs software‑state), or else be different carriers. | Avoids paradoxical overlaps.           |
| **CC‑PHA‑4 (Escalation)**             | If identity criteria fail during change, declare a **Meta‑Holon Transition** (B.2) instead of PhaseOf.                                                           | Makes re‑identification explicit.      |
| **CC‑PHA‑5 (MethodDescription & Work)**      | Versions of **MethodDescription** and slices of **Work** **SHALL** use `PhaseOf` (A.15); PhaseOf never applies to `U.Role`.                                             | Aligns with A.15 bindings.             |

##### **8.4 Anchoring & validation (normative)**

| ID              | Requirement                                                                                                      | Purpose                                           |
| ----------------| ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| **CC‑ANCH‑1**   | Every `ut:StructPartOf` edge **MUST** carry a `tv:groundedBy` link to a valid `Γ_m` constructor trace (Compose‑CAL). | Makes A.10 executable; ensures extensional identity. |
| **CC-ANCH-2**   | For **epistemic** edges (`ut:EpiPartOf` and its sub-types), `tv:groundedBy` is **OPTIONAL**; instead supply **`ev:evidence`** and set **`validationMode ∈ {axiomatic, postulate, inferential}`**. | Harmonises evidence treatment for epistemic edges. |
| **CC‑ANCH‑3**   | The public query Standard remains `?x ut:PartOf+ ?y`; internally it is realised via CT2R‑aliases grounded by `Γ_m` traces. | Preserves the “one query” UX while tightening semantics. |

*Note.* Property names and trace semantics are defined in the CT2R‑LOG / Compose‑CAL architheories.

##### **8.5 MemberOf minimal semantics (non‑mereological)**

| ID           | Requirement                                                                                       | Purpose                               |
| ------------ | ------------------------------------------------------------------------------------------------- | ------------------------------------- |
| **CC‑MEM‑1** | `MemberOf` domain/range are open: any `U.Holon` may be a member of a collection/collective holon. | Allows mixed collections when needed. |
| **CC‑MEM‑2** | From `MemberOf(x,C)` it is **forbidden** to infer any property of C to x via parthood rules.      | Prevents “set‑as‑whole” errors.       |
| **CC‑MEM‑3** | **Constructive aggregation of collections** is provided by **C.13 Compose‑CAL** (`Γ_m.set`); **agency of collectives** is specified outside A.14 (see **A.15 Role–Method–Work**). | Keeps A.14 narrow and clean.          |


##### **8.5 CT2R‑LOG handshake (Working‑Model → Assurance)**

| ID                 | Requirement                                                                                                                                                              | Purpose                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| **CC-A14-10**      | For **structural** edges on the Working-Model surface, authors **SHALL** set `validationMode=axiomatic` and attach **`tv:groundedBy → Γ_m.sum|set|slice`**.      | Aligns A.14 with CT2R-LOG (**B.3.5**) and Compose-CAL (**C.13**); ensures extensional identity. |
| **CC‑A14‑11**      | **PhaseOf** edges **SHALL NOT** use Γ\_m for grounding. Authors **SHALL** provide identity criteria and non‑overlap per **CC‑PHA‑1..3** and reference **Γ\_time** when ordering matters. | Keeps temporal parthood distinct from construction; preserves the plane firewall.       |

#### 9 · Validation patterns (author’s decision procedure)

**Step 0 — Firewall check.**
If your sentence contains *role*, *policy*, *process/workflow/SOP/script*, or *execution/run/job*, you are **not** in mereology; go to **A.15** (Role–Method–Work).

**Step 1 — Is it measured stuff?**
If yes, pick **PortionOf**. Confirm μ is declared (CC‑POR‑1/2). Test additivity on a toy split (CC‑POR‑3). If flows cross a boundary, remodel as interactions, not portions (CC‑POR‑4).

**Step 2 — Is it a discrete inside part?**
If yes, pick **ComponentOf** (physical) or **ConstituentOf** (conceptual). Do **not** use PortionOf here.

**Step 3 — Is it the same carrier at a time slice?**
If yes, pick **PhaseOf**. Verify identity criteria and non‑overlap (CC‑PHA‑1/2/3). If criteria break, escalate to **B.2** (CC‑PHA‑4).

**Step 4 — Is it a membership statement?**
Use **MemberOf** only; avoid any part‑inferences (CC‑MEM‑2). If you need a **collection as a whole**, use **C.13** (`Γ_m.set`) for constructive grounding. If you need **collective action**, defer to **A.15**.

**Quick spot‑tests (repair kit).**

| Smell                          | Likely error                      | Fix                                                                                                                          |
| ------------------------------ | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| “20% of the chassis”           | Treating structure as stuff       | Use **ComponentOf**; if truly laminar material, PortionOf applies to **material stock**, not the assembled chassis.          |
| “Chapter 2 is 15% of the book” | Mixing measures and constituents  | Use **ConstituentOf**; the 15% is **length‑of‑text** as a separate statement.                                                |
| “Spec v2 overlaps v1”          | Overlapping phases on same aspect | Use `PhaseOf(Spec_v2, Spec)` with non‑overlap; represent drafting as **Work** episodes (A.15) rather than overlapping specs. |
| “Team is part of the project”  | Member vs part confusion          | Use **MemberOf(Team, ProjectCollective)**, not partOf.                                                                       |

---

#### 10 · Interplay with Γ‑flavours (how these relations behave under aggregation)

| Γ‑flavour                    | Mereological hooks (what A.14 supplies)                                                                                                                | Key effect                                                                                    |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| **Γ\_sys (B.1.2)**          | Treat **PortionOf** as Σ‑additive stocks; **ComponentOf** must respect boundary integration; **PhaseOf** is not aggregated here.                       | Conserves extensive measures and keeps structural WLNK (weakest‑link) on components.          |
| **Γ\_epist (B.1.3)**         | **PortionOf** of texts/data uses μ = token/byte count; **ConstituentOf** composes arguments/sections; **PhaseOf** versions MethodDescriptions/documents.      | Preserves provenance and avoids trust inflation by keeping constituents vs portions distinct. |
| **Γ\_ctx / Γ\_time (B.1.4)** | **PhaseOf** provides the legal slicing for time and order; **PortionOf** is orthogonal (quantities inside steps).                                      | Ensures chronological consistency and monotone coverage.                                      |
| **Γ\_method (B.1.5)**          | Recipes are **MethodDescription** graphs (not parthood). When a recipe refers to stuff‑like inputs, those are **PortionOf** statements on resources.          | Separates recipe composition from structure.                                                  |
| **Γ\_work (B.1.6)**          | Only **Work** carries resource deltas; when logging “consumed 5 kg from Tank A”, model it as **PortionOf** relation to the stock prior to consumption. | Makes Σ‑balance explicit; aligns with CC‑POR‑3/4.                                             |

#### 11 · Consequences

**Benefits**

* **Predictable composition.** Σ‑additivity for portions and identity‑through‑time for phases make Γ‑proofs straightforward.
* **History without confusion.** Temporal slicing is explicit and audit‑ready; no paradoxical overlaps.
* **Cleaner integration with roles and recipes.** The firewall prevents “functional object” creep into structure.
* **Compatibility with engineering practice.** Mirrors *product breakdown* (components) vs *functional breakdown* (roles) vs *material stocks* (portions) vs *versioning* (phases).

**Trade‑offs / mitigations**

* **Modelling energy.** Authors must pick μ and declare units; provide a short μ‑catalog per project.
* **More relation names.** Two extra sub‑relations increase vocabulary; mitigated by the decision table (§ 6) and spot‑tests (§ 9).
* **Escalation discipline.** Deciding PhaseOf vs MHT requires judgement; A.14 provides criteria, and B.2 captures true re‑identification.

#### 12 · Pedagogy aids (non‑normative)

**Two‑minute checklist for reviewers**

1. Do I see “process/workflow/policy/script”? — then **A.15**, not mereology.
2. Does every PortionOf have a declared μ and unit?
3. Do phases cover a lifetime without overlap for the same aspect?
4. Are any roles/recipes appearing as parts? If yes, stop and refactor.

#### 13 · Patch map (where to touch in the working file)

1. **Kernel · Holonic Mereology (§ A.1 → A.14)**
   *Add* sub‑sections “PortionOf” and “PhaseOf” with axioms (POR‑1..5, PHA‑1..5).
   *Move* MemberOf note to a minimal semantics paragraph (no composition here).

2. **A.15 (Role–Method–Work)**
   *Cross‑link* firewall (CC‑A14‑0/0b) and reinforce that versioning uses **PhaseOf** only on MethodDescription/Work.

3. **B.1.2 Γ\_sys / B.1.3 Γ\_epist / B.1.4 Γ\_ctx/Γ\_time / B.1.5 Γ\_method / B.1.6 Γ\_work**
   *Insert* a one‑line “A.14 compliance” note: which A.14 sub‑relations each flavour relies on, as in § 10.

4. **Examples & Annexes**
   *Refactor* any “percentage as part” examples into PortionOf with declared μ;
   *Split* any overlapping histories into PhaseOf sequences.

Each edited heading should carry the badge **“► decided‑by: A.14 Advanced Mereology”**.

#### 14 · Rationale (state‑of‑the‑art alignment, post‑2015)

* **Metrical mereology** advances (e.g., recent work on quantity‑based parthood and additivity) motivate **PortionOf** with explicit μ and Σ‑laws, preventing the classic “stuff as components” fallacy.
* **Temporal parts & identity through change** (renewed treatments in analytic metaphysics and formal ontology) motivate **PhaseOf** with coverage/non‑overlap and escalation when identity criteria fail.
* **Engineering ontologies (BORO lineage, Core Constructional practice, ISO 15926 family)** keep a strict separation between **functional breakdowns** (our Roles) and **product breakdowns** (our Components), with **stock/consumable** modelling (our Portions) handled by quantities, not by component trees.
* **Knowledge artefact lifecycles** in contemporary MBSE and open‑science workflows use explicit versioning (our PhaseOf) and provenance‑preserving composition (our ConstituentOf).
* The net effect is a **minimal‑sufficient** catalogue: two added sub‑relations close real modelling gaps while preserving **parsimony**, **didactic clarity**, and **Γ‑compatibility** across domains.

### A.15 Role–Method–Work Alignment (Contextual Enactment)  \[A]

#### 1 · Intent & Context

In any complex system, from a software project to a biological cell, there is a fundamental distinction between **what something is** (its structure), **what it is supposed to do** (its role and specified capability), and **what it actually does** (its work). Confusing these layers is a primary source of design flaws, budget overruns, and failed projects. Teams argue about a "process" without clarifying if they mean the documented procedure, the team's ability to execute it, or a specific execution that happened last Tuesday.

This pattern provides the canonical alignment for modeling contextual enactment in FPF, serving as the ultimate implementation of the **Strict Distinction Principle (A.7)**. It weaves together several foundational concepts into a single, coherent model of how intention becomes action:
*   **A.2 (Contextual Role Assignment):** Provides the `Holder#Role:Context` structure for assigning roles.
*   **A.4 (Temporal Duality):** Provides the strict separation between `design-time` and `run-time`.
*   **A.12 (External Transformer):** Ensures that all actions are attributed to an external agent.

The intent of this pattern is to establish a normative, unambiguous vocabulary and set of relations for describing the entire evolution of an action, from the specification of a capability to its concrete, resource-consuming execution.

To keep plan–run separation explicit, this pattern references **A.15.2 `U.WorkPlan`** for **schedules/calendars** and **A.15.1 `U.Work`** for **dated execution**. Ambiguous terms like “process / workflow / schedule” are constrained by **L‑PROC / L‑FUNC / L‑SCHED** (E‑cluster): a _workflow_ is a **Method/MethodDescription**, a _schedule_ is a **WorkPlan**, and what _happened_ is **Work**.

**Terminology note (L‑ACT).** The words _action/activity_ are **not normative** in the kernel. When a generic “doing” is needed, we use the didactic term **enactment** (not a type). Normative references must be to **`U.Method` / `U.MethodDescription` / `U.Work` / `U.WorkPlan`**. See lexical rules **L‑PROC / L‑FUNC / L‑SCHED / L‑ACT**

#### 2 · Problem

Without this formal framework, models suffer from a cascade of category errors:

1.  **Role-as-Part:** A Role (e.g., `AuditorRole`) is incorrectly placed inside a structural bill-of-materials (`ComponentOf`), making the system's architecture brittle and nonsensical.
2.  **Specification-as-Execution:** A `MethodDescription` (the "recipe") is treated as evidence that the work was done. This leads to "paper compliance," where a system is considered complete simply because its documentation exists.
3.  **Capability-as-Work:** A team's *ability* to perform a task (`Capability`) is conflated with the *actual performance* of that task (`Work`). This obscures the reality of resource consumption and actual outcomes.
4.  **Work-without-Context:** An instance of work is logged without a clear link back to the role, capability, and specification that governed it, making the work unauditable and its results impossible to reproduce.
5.  **Ambiguous "Process/Activity":** The overloaded term "process" is used indiscriminately to refer to all of the above, creating a fog of miscommunication that paralyzes decision-making. Activity/action terms must be resolved via L‑ACT to Method/MethodDescription (recipe), WorkPlan (schedule), or Work (run).

#### 3 · Forces

| Force | Tension |
| :--- | :--- |
| **Structure vs. Function** | The need to model the stable, physical structure of a system (`mereology`) vs. the need to model its dynamic, functional behavior (`roles` and `actions`). |
| **Design vs. Run** | The need for a timeless, reusable description of a capability (`design-time`) vs. the need for a specific, dated record of its execution (`run-time`). |
| **Clarity vs. Jargon** | The need for a precise, formal vocabulary to prevent ambiguity vs. the reality that teams use informal, domain-specific jargon like "process" or "workflow." |
| **Accountability vs. Complexity** | The need for a complete, end-to-end audit trail for every action vs. the desire to keep models simple and avoid excessive documentation. |

#### 4 · Solution
The solution is a stratified alignment that cleanly separates the `design-time` and `run-time` for contextual **enactment**. The bridge between these worlds is the **`U.RoleAssignment`**.

#### 4.1 The Core Entities: A Strict Distinction

FPF mandates the use of the following distinct, non-overlapping entities to model action. Using them interchangeably is a conformance violation.

**A) Design-Time Entities (The World of Potential):**

*   **`U.Role`:** A contextual "mask" or "job title" (e.g., `TesterRole`). It specifies a function but is not the function itself.
*  **`U.Method`:** The **abstract way‑of‑doing** inside a context (paradigm‑agnostic; may be imperative, functional, logical, or hybrid).
*  **`U.MethodDescription`:** A **`U.Episteme` describing a `U.Method`** (the SOP/algorithm/proof/recipe on a carrier).
*   **`U.Capability`:** An **attribute** of a `U.System` that represents its **ability** to perform the actions described in a `MethodDescription`. This is the "skill" or "know-how."
* **`U.WorkPlan`:** An **`U.Episteme`** declaring **intended `U.Work` occurrences** (windows, dependencies, intended performers as role kinds, budgets) — see **A.15.2**.
* 
**B) The Bridge Entity:**
*   **`U.RoleAssignment`:** The formal assertion `Holder#Role:Context` that links a specific `U.Holon` to a `U.Role` within a `U.BoundedContext`. This binding is what "activates" the requirements associated with a role.

**C) Run-Time Entity (The World of Actuality):**

*   **`U.Work`:** An **occurrence** or **event**. It is the concrete, dated, resource-consuming **execution of a `U.MethodDescription`** by a `Holder` acting under a `U.RoleAssignment`; capability checks are evaluated at run time against the holder. This is the only entity that has a start and end time and consumes resources.

**Kinds of Work and the primary target**
Every `U.Work` SHALL declare a `primaryTarget: U.Holon` and a `kind`.
Kinds:
* Operational — transforms a `U.System` or its environment.
* Communicative (SpeechAct) — transforms a deontic/organizational frame (e.g., commitments, permissions, approvals).
* Epistemic — transforms a `U.Episteme` (e.g., curating a dataset).
The `primaryTarget` disambiguates enactment: what is being acted upon. Example: an approval is `kind=Communicative`, `primaryTarget = Commitment(change=4711)`. A deployment is `kind=Operational`, `primaryTarget = ServiceInstance(prod-us-eu-1)`.

**Didactic Note for Managers: The "Chef" Analogy**

This model can be easily understood using the analogy of a chef in a restaurant.

*   **`ChefRole`** is the **Role**. It's a job title with certain expectations.
*   A **Cookbook (`U.MethodDescription`)** contains the **recipe** for a Soufflé. It's a piece of knowledge.
*   The chef's **skill** in making soufflés is their **`U.Capability`**. They have this skill even when they are not cooking.
*   The restaurant's rulebook (`U.BoundedContext`) states that anyone in the `ChefRole` *must* have the `Capability` to follow the recipes in the cookbook.
*   The actual act of **making a soufflé** on Tuesday evening—using eggs and butter, taking 25 minutes, and consuming gas—is the **`U.Work`**.

Confusing these is like mistaking the cookbook for the soufflé. FPF's framework simply makes these common-sense distinctions formal and mandatory.

#### 4.2 The Canonical Relations: Connecting the Layers

The entities are connected by a set of precise, normative relations that form an unbreakable causal chain. The following diagram illustrates this flow from the abstract context down to the concrete execution.

```mermaid
graph TD
    subgraph Design-Time Scope (Tᴰ)
        A[U.BoundedContext] -- defines --> B(U.Role)
        M[U.Method] -- isDescribedBy --> D[U.MethodDescription]
        Cap[U.Capability] -- supports --> M
        H(U.System as Holder) --> RB(U.RoleAssignment)
        B -- is the role in --> RB
        A -- is the context for --> RB
        A -- bindsCapability(Role,Capability) --> Cap
    end

    subgraph Run-Time Scope (Tᴿ)
        W[U.Work]
    end

    RB -- performedBy --> W
    W  -- isExecutionOf --> D

    style A fill:#e6f3ff,stroke:#36c,stroke-width:2px
    style B fill:#fff2cc,stroke:#d6b656,stroke-width:2px
    style Cap fill:#d5e8d4,stroke:#82b366,stroke-width:2px
    style M fill:#d5e8d4,stroke:#82b366,stroke-width:2px
    style D fill:#f8cecc,stroke:#b85450,stroke-width:2px
    style H fill:#e1d5e7,stroke:#9673a6,stroke-width:2px
    style RB fill:#dae8fc,stroke:#6c8ebf,stroke-width:3px,stroke-dasharray: 5 5
    style W fill:#ffe6cc,stroke:#d79b00,stroke-width:2px,font-weight:bold
```

*   **`bindsCapability(Role, Capability)`:** A `U.BoundedContext` asserts that a given `Role` requires a specific `Capability`. This is a `design-time` rule.
*  **`isDescribedBy(Method, MethodDescription)`:** A `Capability` is formally described by one or more `MethodDescription`s. This links the skill to the recipe.
*   **`isExecutionOf(Work, MethodDescription)`:** A specific `U.Work` is a `run-time` instance of a `design-time` `Capability`.
*   **`performedBy(Work, RoleAssigning)`:** A `U.Work` is always performed by a specific `Agent` (a RoleAssignment). This links the action to the actor-in-context.

_At run time, capability thresholds declared by the context/spec are **checked** against the holder; Work outcomes provide **evidence** for capability conformance._

This chain provides complete traceability: a specific instance of `Work` can be traced back through its `Capability` to its `MethodDescription`, and to the `Agent` (`Holder` + `Role` + `Context`) that was authorized and responsible for its execution.

#### 5 · Archetypal Grounding

The Contextual Action Framework is universal. It applies identically to the modeling of physical engineering processes, knowledge work, and socio-technical systems.

| Archetype | **`U.System` Archetype (Manufacturing)** | **`U.Episteme` Archetype (Scientific Peer Review)** |
| :--- | :--- | :--- |
| **`BoundedContext`** | `FactoryFloor:ProductionLine_B` | `Journal:PhysicsLetters_A` |
| **`Role`** | `WeldingRobotRole` | `ReviewerRole` |
| **`Holder`** | `ABB_Robot_Model_IRB_6700` (`U.System`) | `Dr_Alice_Smith` (modeled as a `U.System`) |
| **`U.RoleAssignment`** | `ABB_Robot#WeldingRobotRole:Line_B` | `Dr_Smith#ReviewerRole:PhysicsLetters_A` |
| **`MethodDescription` (`U.Episteme`)**| `Welding_Procedure_WP-28A.pdf` (SOP) | `Peer_Review_Guidelines_v3.docx` |
| **`Capability` (Attribute of Holder)** | `executeWeldingSeam(Type: 3F)` | `evaluateManuscript(Field: QuantumOptics)` |
| **`Work` (`Occurrence`)** | Manufacturing Work: `Weld_Job_#78345` (15:32-15:34 UTC, consumed 1.2 kWh, 5g Argon) — **isExecutionOf** `Welding_Procedure_WP‑28A.pdf` | Peer‑review Work: `Review_of_Manuscript_#PL-2025-018` (Completed 2025-08-15, took 4 hours) — **isExecutionOf** `Peer_Review_Guidelines_v3.docx` |

**Key takeaway from grounding:**
This side-by-side comparison reveals the power of the framework. A seemingly different activity like welding a car chassis and reviewing a scientific paper are shown to have the **exact same underlying causal structure**. Both involve a `Holder` (a system) acting in a `Role` within a `Context`, using a `Capability` described by a `MethodDescription` to produce a specific, auditable instance of `Work`. This universality is what allows FPF to bridge disparate domains.

#### 6 · Conformance Checklist

To ensure the integrity of action modeling, all FPF-compliant models must adhere to the following normative checks.

| ID | Requirement (Normative Predicate) | Purpose / Rationale |
| :--- | :--- | :--- |
| **CC-A15-1 (Entity Distinction)** | The entities `U.Role`, **`U.Method`**, **`U.MethodDescription`**, `U.Capability`, **`U.WorkPlan`**, and `U.Work` **MUST** be modeled as distinct, non‑overlapping types. | This is the core enforcement of **Strict Distinction (A.7)**. It prevents the category errors outlined in the "Problem" section. |
| **CC-A15-2 (Temporal Scope)** | `U.Method`/`U.MethodDescription`/`U.WorkPlan` exist in **design‑time**; `U.Work` exists in **run‑time**. Design artifacts are not mutated by operational events. | Enforces **Temporal Duality (A.4)**. Blueprints cannot be mutated by operational events. |
| **CC-A15-3 (RoleAssignment Mandate)**| Every `U.Work` **MUST** be linked via `performedBy` to a valid `U.RoleAssignment`. | Guarantees that every action has a clearly identified, context-bound actor, ensuring accountability. |
| **CC-A15-4 (Traceability Chain)**| For every `U.Work`, an unbroken chain **MUST** exist: `Work —performedBy→ RoleAssigning` and `Work —isExecutionOf→ MethodDescription —describes→ Method`. Capability checks are evaluated against the holder at run time. | Ensures end-to-end auditability from a specific action back to the "recipe" that governed it. |
| **CC-A15-5 (No Roles in Mereology)** | A `U.Role` or `U.Capability` **SHALL NOT** be part of a mereological (`partOf`) hierarchy. | The "Role-as-Part" anti-pattern is a violation. Roles and capabilities are functional, not structural. Enforces **A.14**. |
| **CC-A15-6 (Resource Honesty)** | Resource consumption (`U.Resource`) **MUST** only be associated with `U.Work`, never with `U.MethodDescription` or `U.Capability`. | Enforces that costs are tied to actual events, not to plans or potential. Aligns with **Resrc-CAL (C.5)**. |
| **CC‑A15‑7 (Plan/Run Split)** | Schedules/calendars **MUST** be represented as `U.WorkPlan` (A.15.2). A WorkPlan SHALL NOT be used as evidence of execution; only `U.Work` carries actuals. | |
| **CC‑A15‑8 (Lexical Sanity)** | Unqualified “process/workflow/schedule” **MUST** be interpreted per **L‑PROC/L‑FUNC/L‑SCHED**: workflow ⇒ `Method/MethodDescription`; schedule ⇒ `WorkPlan`; what happened ⇒ `Work`. | |
| **CC-A15-9 (Realisation)** | A valid `U.Work` realises a `U.MethodDescription` under a `U.RoleAssignment`. Spontaneous physical evolution without a MethodDescription is modeled as `U.Dynamics`, not as `U.Work`. | |
| **CC-A15-10 (GateSplit)** | A SpeechAct that changes a Role’s state (e.g., “Approve”, “Authorize”) MUST be modeled as a distinct `U.Work` step (kind=Communicative). It may open the Green‑Gate for a subsequent operational step, but it SHALL NOT be conflated with that step. | |
| **CC-A15-11 (KindFit)** The `U.Role` named in the `performedBy` assignment SHALL be appropriate for the Work kind (e.g., ApproverRole for Communicative approvals; DeployerRole for Operational deployments). | |

#### 7 · Consequences

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Unambiguous Communication:** Provides a shared, precise vocabulary for teams to discuss roles, processes, and results, eliminating the ambiguity of terms like "process." | **Initial Learning Curve:** Requires teams to learn and internalize the distinctions between the core entities. *Mitigation:* The "Chef" analogy and clear archetypes serve as powerful didactic tools. FPF tooling should guide users with templates. |
| **End-to-End Auditability:** The framework creates a "digital thread" that links every operational event (`Work`) back to its authorizing role, context, and specification. This is critical for regulated industries and for root cause analysis. | **Increased Formality:** Requires more explicit modeling than informal approaches. *Mitigation:* This is a strategic investment. The upfront cost of formal modeling is offset by massive savings in debugging, re-work, and compliance efforts later. |
| **Enables True Modularity:** By separating capability from execution, the framework allows for easier substitution. A `MethodDescription` can be updated without invalidating past `Work` records. A `Holder` can be replaced with another, as long as it possesses the same `Capability`. | - |
| **Foundation for Governance:** The model makes it possible to build powerful governance rules. For example: "Only an `Agent` with `AuditorRole` can execute `Work` that instantiates the `ApproveRelease` capability." | - |

#### 8 · Rationale

This pattern solves a problem that has plagued systems modeling for decades: the conflation of what a system *is* with what it *does*. Its rigor is not arbitrary but is grounded in several key intellectual traditions.

*   **Ontology Engineering:** The pattern is a direct application of best practices from foundational ontologies (like UFO), which have long insisted on the distinction between *endurants* (objects like a `U.System`) and *perdurants* (events/processes like `U.Work`), and between intrinsic properties and relational roles. FPF makes these powerful distinctions accessible to practicing engineers.
*   **Process Theory:** Formalisms like the Pi-calculus or Petri Nets model processes as dynamic interactions. The FPF Contextual Action Framework provides a higher-level, more semantically rich layer on top of such formalisms. The `U.Work` entity can be seen as an instance of a process, but FPF adds the crucial context of the `Role`, `Capability`, and `MethodDescription` that govern it.
*   **Pragmatism and Practice:** The framework is deeply pragmatic. The distinctions it makes (e.g., between a `MethodDescription` and `Work`) are precisely the ones that matter in the real world of project management, compliance, and debugging. When a failure occurs, a manager needs to know: was the recipe wrong (`MethodDescription`), did the chef lack the skill (`Capability`), or did they just make a mistake this one time (`Work`)? This framework provides the vocabulary to ask and answer that question precisely.

By creating this clean, stratified alignment for enactment, FPF provides a stable and scalable foundation for all of its more advanced architheories, from resource management (`Resrc-CAL`) and decision theory (`Decsn-CAL`) to ethics (`Norm-CAL`).

#### 9 · Relations

*   **Directly Implements:** `A.7 Strict Distinction`.
*   **Builds Upon:** `A.2 (U.Role)`, `A.2.1 (U.RoleAssignment)`, `A.4 (Temporal Duality)`, `A.12 (External Transformer)`.
*   **Is Used By / Provides Foundation For:**
    *   `C.4 Method-CAL`: Provides the formal definition of `U.MethodDescription` and the `Γ_method` operator for composing them.
    *   `C.5 Resrc-CAL`: Provides the `U.Work` entity to which resource consumption is attached.
    *   `B.1.6 Γ_work`: The aggregation operator for `U.Work`.
    *   `B.4 Canonical Evolution Loop`: The entire loop is a sequence of `Work` instances that modify `MethodDescription`s.
    *   `A.15.2 U.WorkPlan`: plan–run split, baselines and variance against `U.Work`.
* **Constrains:** Any architheory that models actions or processes must use this framework to be conformant. It serves as the canonical alignment for **contextual enactment** in the FPF ecosystem.
* **Coordinates with** L‑PROC / L‑FUNC / L‑SCHED (E‑cluster) for lexical disambiguation of _process / workflow / schedule_.


---

# A.15.1 — U.Work  \[D]


---

# A.15.2 — U.WorkPlan  \[D]



---

## A.17 (A.CHR‑NORM) — Canonical “Characteristic” `[A]`

### 1. Context

Every FPF architheory needs to **measure** various aspects of systems or knowledge artifacts. A dedicated measurement backbone (see **C.MM‑CHR**, Measurement & Metrics Characterization) already exists, prescribing the **CSLC discipline** – i.e. define a **Characteristic**, choose a **Scale** (with a **Unit** if applicable), record a **Level/Value**, and thus obtain a **Coordinate** on that scale, optionally mapping to a **Score** via a **ScoringMethod (USCM)**. However, historically multiple near-synonyms (“axis”, “dimension”, “property”, “feature”, "metric") have been used interchangeably for “what is being measured,” and often the _aspect itself_ gets conflated with _how it is expressed_ (units, ranges, labels). This pattern enters the FPF **Kernel lexicon** to **canonize a single term** for the measured aspect and enforce a clear separation between **what** is measured and **how** it is measured.

### 2. Problem

When measurement concepts are not kept rigorously distinct, several issues arise:

-   **Polysemy at the anchor.** Teams say “dimension” or “feature” but mean slightly different things, so the very trait being measured is ambiguous.
    
-   **Arity mistakes.** A relational quality (e.g. similarity between two items) might be treated as if it were an intrinsic property of one item, or vice versa, leading to logical errors.
    
-   **Expression conflation.** The aspect being measured is often mixed up with its expression – for example, using “scale” or “axis” to mean both the quality _and_ its unit or range. This leads to **unsafe arithmetic** (averaging ordinal ranks, comparing raw numbers from incompatible scales, etc.) because values get interpreted out of context.
    

In summary, projects lacking a canonical terminology for metrics risk miscommunication and pseudo-quantitative operations. Measurements of physical quantities, architectural attributes, or performance scores end up on **incommensurate rails** due to inconsistent naming and handling.

### 3. Forces

-   **F1 – Single anchor of meaning.** Any numeric value is meaningless unless one can ask “value of _what_?”. The measurement’s meaning must be anchored in a single clearly named aspect.
    
-   **F2 – Arity clarity.** Some characteristics apply to a single entity (e.g. its mass or length), while others inherently relate multiple entities (e.g. distance between two points, coupling between modules, agreement between judges). If arity isn’t explicit, claims and calculations become corrupted.
    
-   **F3 – Scale integrity.** Different kinds of scales permit different operations – e.g. you can average temperatures (ratio scale) but not ranks or grades (ordinal scale) without losing meaning. If one mixes values without regard to scale type or units, the result is nonsense (**pseudo-arithmetic**).
    
-   **F4 – Composition discipline.** In complex evaluations, multiple measurements may need to be combined. Without a disciplined approach, people might perform ad-hoc math on apples and oranges (adding scores from unrelated characteristics, etc.). A proper pattern must require any combination to go through a defined monotonic **ScoringMethod** (e.g. a weighted formula) instead of arbitrary aggregation.
    
-   **F5 – Transdisciplinarity.** The measurement framework should work for **any domain**. The same conceptual scaffold must serve physical science (e.g. lab temperature readings), software engineering (e.g. module cohesion ratings), and even subjective assessments (e.g. figure-skating scores) without bias. One vocabulary, many CG‑frames.
    
-   **F6 – Open-endedness.** As systems evolve, their performance or quality metrics also evolve. Rigid life-cycle stage labels (“Phase 1, Phase 2…”) don’t capture iterative improvement. The pattern should favor an **open-ended state-space** view (revisiting states via checklists, as in an RSG – **RoleStateGraph** with re-entry) over any fixed lifecycle with “terminal” stages.
    
### 4. Solution

**Establish “Characteristic” as the one canonical construct for “what is measured.”** In every FPF context, the _aspect or trait_ being measured MUST be referred to as a **Characteristic**. This term replaces “axis” or “dimension” in normative usage (those may appear _only_ as explanatory aliases in Plain register). By fixing a single name and schema, we cleanly separate a **Characteristic** from its **Scale** (and **Unit**), and from any observed **Value/Level** on that scale. The solution also differentiates single-entity vs multi-entity cases and binds all measurements to the standard CSLC sequence.

To enforce this solution, the following rules apply:

-   **A17-R1 (Canonical term).** In all normative models and specifications, the measured aspect **SHALL** be referred to as a **Characteristic**. (Legacy terms “Axis” or “Dimension” are retired from technical vocabulary – see Part J Lexicon Update.)
    
-   **A17-R2 (Entity vs. relation subtype).** Each Characteristic **MUST** declare its intended _arity_. An **Entity-Characteristic** applies to exactly one bearer (e.g. _Temperature_ of a reactor, _Evolvability_ of a software module), whereas a **Relation-Characteristic** applies to an ordered tuple of two or more bearers (e.g. _Distance_ between two sensors, _Coupling_ between modules, _Agreement_ among reviewers). The arity is part of the definition and **must be explicit** wherever it’s not obvious from naming.
    
-   **A17-R3 (Characteristic space).** Any set of defined Characteristics spans a multi-dimensional **CharacteristicSpace**. Movement or evolution is then described as trajectories through this space (with states revisited or refined over time), rather than as a linear lifecycle through preset phases. This ensures measurements feed into open-ended state modeling rather than locking into “end states.”
    
-   **A17-R4 (Lexical guardrails).** Normative text **SHALL** use only the canonical measurement terms: **Characteristic, Scale, Level, Value, Coordinate, Score, Normalization, Unit**. Synonyms like _axis_, _dimension_, _metric_, _grade_, _property_, etc., are **forbidden in formal usage**. (They may appear in narrative explanations or user-facing documentation _only if_ clearly defined as aliases for the canonical terms.) Authors **MUST** not use deprecated terms in identifiers or formal statements, and any didactic alias should be introduced with an explicit mapping to the official term. These lexical rules uphold clarity and are further detailed in **E.10 LEX‑BUNDLE**. 

- **A17-R5 (Symbol policy).** **Γ** reserved for holonic composition; **𝒢 : Coordinate→Score** for metric‑level ScoreMethod; **MUST NOT** be conflated; documents **SHALL NOT** reuse Γ for ScoreMethod. **If an ordered Scale is declared, polarity SHALL be fixed; 𝒢 MUST be monotone** w.r.t. that polarity.

- **A17-R6 (Declared polarity).** Every ordered Scale **SHALL** declare one of: **↑‑better**, **↓‑better**, or **non‑applicable** (for purely nominal scales). For interval/ratio scales, polarity fixes the intended order of comparison.

- **A17-R7 (Monotonicity against polarity).** If a template declares an **ordering polarity** on its Scale (↑ better / ↓ better), then **𝒢 MUST be monotone** w\.r.t. that polarity: higher‑is‑better (resp. lower‑is‑better) in coordinates **implies** ≥ (resp. ≤) in scores.

- **A17-R8 (Arity declaration).** Authors **SHALL** mark a Characteristic as **`U.EntityCharacteristic`** (applies to exactly one bearer) or **`U.RelationCharacteristic`** (applies to a relation of cardinality ≥ 2). Examples: *Cohesion* → entity‑level; *Coupling* → relation‑level.

- **A17-R9 (Relational scale anchors).** For relation‑level cases, the Scale’s admissible values **SHALL** be defined over the **tuple** domain (e.g., distances, similarities, inter‑role latencies). Ambiguity that re‑reads a relational Characteristic as unary is **forbidden**.

- **A17-R10 (Intension vs Description).** The **Characteristic** remains the **intensional object**; any rubric, catalogue of levels, or examples are **descriptions**. Keep the intensional Characteristic distinct from its descriptive episteme (cf. `U.Episteme` roles: Object–Concept–Symbol).

#### 4.1 CharacteristicSpace & Change Reasoning *(Normative/Clarifying)*

**R17 — CharacteristicSpace declaration.** When an architheory reasons about **change**, it **SHALL** name the **CharacteristicSpace** (the set of Characteristics, with Scales, units, and topology assumptions) in which motion is considered.

**R18 — RSG framing, not lifecycle.** Change narratives **SHALL** be framed as movement on a **reachable‑states graph (RSG)** with **checklists** that certify state acquisition; **“lifecycle”** staging is **deprecated**. *(A.17 conforms to the open‑ended evolution stance of the Kernel.)*

**I7 — Vector interpretation.** A **U.Coordinate** vector may collect multiple coordinates for multi‑Characteristic reasoning; composition into a single Score, if desired, is an **explicit new 𝒢** on that vector.

### 5. Archetypal Grounding (System & Episteme Examples)

**In a physical system (`U.System`):** Consider a **Distance** Characteristic defined for a pair of physical objects. For example, two machines in a factory have a Distance of 3.5 meters between them. Here _Distance_ is a Relation-Characteristic (applies to the pair), with an associated Scale (e.g. a ratio scale in meters), and the measured 3.5 m is a **Coordinate** on that scale. If we instead look at an **Engine Temperature** Characteristic (unary), a particular engine might have a Temperature of 350 K at some moment – _Temperature_ (the Characteristic) is clearly separated from how it’s measured (Scale in Kelvin) and the reading (350, a Coordinate on that scale).

**In an epistemic context (`U.Episteme`):** Consider a **Formality** Characteristic to rate a documentation artifact’s rigor. We might define an ordinal Scale with named Levels such as _Informal_, _Semi-formal_, _Formal_. A given specification document can then be said to have _High Formality_ – meaning it occupies the “Formal” **Level** on the Formality Scale. Here _Formality_ (Characteristic) captures _what_ we measure about the document, while the tiered Scale (with qualitative levels) expresses _how_ we categorize it. Because we use an ordinal scale, we can rank documents by Formality, but we would not average “Semi-formal” and “Formal” (avoiding meaningless arithmetic on an ordinal metric). In another knowledge context example, one could define a Characteristic **Reliability** for a knowledge source with a percentage Scale from 0 to 100%. An article’s reliability might be 85% – which is only interpretable by knowing it refers to “Reliability” on a 0–100% Scale (i.e. a specific Coordinate on that Characteristic’s scale).

### 6. Bias-Annotation

This pattern is deliberately **domain-neutral** and introduces no bias toward any particular discipline or measurement type. By enforcing a uniform lexicon, A.17 actually mitigates bias: it prevents **disciplinary jargon** from creeping into core definitions (ensuring, for instance, that a software metric isn’t given a vague custom term when it’s fundamentally a Characteristic). The **Didactic lens** is strongly served: using one precise name per concept improves clarity for all audiences. There is a slight initial cost in re-labeling legacy terms (e.g. renaming “dimensions” to Characteristics), but this is offset by the long-term **Cognitive Elegance (P‑1)** – the framework becomes easier to learn and less prone to misinterpretation. No single domain’s terminology dominates, and the pattern explicitly supports both quantitative (physics-like) and qualitative (judgment-based) measurements, reflecting **Pragmatic neutrality**. The requirement of open-ended state-space thinking aligns with **P‑10 (Open-Ended Evolution)**, ensuring we don’t bake in lifecycle biases that assume development must terminate at a final stage. In summary, A.17 imposes a disciplined vocabulary that is broad enough for all fields and free of hidden assumptions, thereby avoiding subtle ontological or cultural biases in the measurement model.

### 7. Conformance Checklist

When authoring or reviewing FPF-compliant metrics, use the following checklist to ensure **Characteristic normalization** is applied:

1.  **Declared Characteristic:** Have you explicitly named a **Characteristic** for each aspect being measured, instead of using generic terms? (e.g. use _“Reliability”_ as a Characteristic name rather than saying “this dimension”).
    
2.  **Arity Explicit:** Is it clear whether the Characteristic is unary or relational? If a metric involves a relationship, are the participating entities (pair, tuple, etc.) identified in its definition?
    
3.  **Separate Scale/Unit:** For each Characteristic, have you defined the **Scale** (and **Unit**, if applicable) separately, rather than embedding units or ordinal terms in the name of the Characteristic? (e.g. _“Length (m)”_ should be captured as Characteristic = _Length_, Unit = _meter_).
    
4.  **Scale-appropriate operations:** Are you only performing comparisons or calculations that make sense for the declared scale type? (No averaging of ranks, no mixing of units – ensure **ordinal** Characteristics aren’t treated like numbers, and **interval/ratio** values respect zero and units.)
    
5.  **No implicit aggregation:** If multiple measurement readings are combined, is there a defined **ScoredMethod** (with monotonic logic) that produces a **Score**? Avoid any ad-hoc “overall score” that simply adds or averages raw values from different Characteristics.
    
6.  **Canonical terminology in use:** Are you using the terms _Characteristic_, _Scale_, _Level/Value_, _Coordinate_, _Score_, _Gauge_, _Unit_ in all formal descriptions? Confirm that no deprecated synonyms (axis, dimension, etc.) appear in technical content or identifiers (they can appear in Plain explanations only with proper reference to the canonical term).
    
7.  **Open-ended progression:** (If applicable) When modeling progress or change using metrics, have you considered using a state-space of Characteristics rather than a fixed sequence of phases? This check is to encourage leveraging the open-ended nature of CharacteristicSpaces, especially in evolutionary or iterative processes.
    
_(Failure to satisfy the above indicates a violation of this pattern’s intent. The **LEX-BUNDLE** rules in E.10 provide automated checks for term usage, and MM-CHR templates enforce explicit Characteristic/Scale definitions.)_

### 8. Consequences

By instituting **Characteristic** as the single term and enforcing the CSLC structure, this pattern yields several positive outcomes:

-   **Unambiguous metrics:** Every measurement has a single, well-defined anchor of meaning – the Characteristic – eliminating guesswork about “what is this number about?”.
    
-   **Separation of concerns:** We cleanly separate _what_ is measured from _how_ it’s represented. The Characteristic names the quality of interest, while the Scale/Unit defines the expression. A raw value now **means nothing by itself** – it must be read as “X units on the Y scale of Z Characteristic,” which greatly reduces misinterpretation.
    
-   **Unary vs. relational clarity:** The explicit distinction between Entity-Characteristic and Relation-Characteristic ensures that relational properties (like “distance between A and B” or “consistency among experts”) aren’t mistakenly treated as inherent properties of a single object. This guards against logical errors and data modeling mistakes.
    
-   **Cross-domain comparability:** All measurements, regardless of domain, follow the same **CSLC** rails. This means a temperature in Kelvin and a reliability score in percent can each be traced through Characteristic → Scale → Coordinate. They can’t be directly compared unless designed to be, which is _good_: any composite scoring must be done via an explicit **SCP** mapping to a common **Score** scale. The pattern thus enables interoperability (through well-defined Score bridges) while preventing illegitimate comparisons.
    
-   **Consistent evolution framing:** By retiring the idea of a bespoke “lifecycle” for every process and instead viewing changes as movement in a CharacteristicSpace, the pattern aligns metric thinking with state-based reasoning (e.g. as used in dynamic models). There is no artificial “final state” for improvement – a system can always evolve to a new coordinate without violating a lifecycle Standard. This open-ended view encourages continuous improvement and refinement, echoing FPF’s emphasis on evolutionary development.
    

There are few downsides. One consequence is that modelers must learn the canonical terms and possibly refactor existing documentation (a short-term effort). Also, enforcing scale integrity means quick-and-dirty aggregate scores are not allowed unless justified via a SCP – this introduces a healthy “pause” to ensure composite metrics are well-founded. Overall, the benefits in clarity and correctness far outweigh the overhead. Teams gain a _lingua franca_ for metrics, and the risk of metric abuse (mixing apples and oranges) is significantly reduced.

### 9. Rationale

The Canonical Characteristic pattern is a direct response to recurring measurement pitfalls. By insisting on “one precise name per concept”, it upholds **Strict Distinction (A.7)**, ensuring that the framework never treats two different ideas as one. For instance, earlier practice might label both a requirement category and its score as “dimension,” causing confusion; with A.17, the _aspect_ is a Characteristic and its _score_ is separate, so each idea has its place. This clarity is pedagogically vital (**P‑2 Didactic Primacy**): readers and contributors immediately know what a term means and how to interpret any value associated with it.

The solution also draws on fundamentals of measurement theory (Stevens’ levels of measurement) to prevent misuse. By encoding scale types and unit handling into our patterns, we avoid the “pseudo-quantitative” fallacies – no more averaging things like _risk levels_ or adding up _grades_ as if they were true numbers. In effect, A.17 puts a safeguard around **P‑1 Cognitive Elegance and P‑7 Ontological Parsimony**: we use a minimal, universal set of measurement constructs, and we avoid bloating the conceptual space with domain-specific or redundant terms. One canonical set of terms also makes the framework more teachable and **composable across contexts**, since architheories and projects aren’t inventing new synonyms that others must decipher.

Importantly, distinguishing Entity vs Relation Characteristics future-proofs the reasoning model. It enforces a modeling rigor seen in domains like physics (where properties vs. relations are carefully distinguished) and brings it to architecture and knowledge domains. This rigor supports advanced reasoning in FPF – for example, **A.3.3 (Dynamics)** can treat system state variables as a well-defined set of Characteristics, and assurance patterns can trace **evidence metrics** unambiguously to the exact aspect measured. It also means any attempt to compare or combine metrics has to be explicit (via Gauges), which inherently improves **transparency and auditability** (a key FPF goal).

Finally, retiring the “lifecycle” vocabulary in favor of state-space trajectories aligns with FPF’s **open-ended evolution** principle. It acknowledges that improvement is not a predefined path but a navigable space. This shift in mindset (from lifecycle stages to checklisted state transitions) removes an implicit bias that systems _ought_ to reach a “final” maturity stage – instead, it keeps the door open for perpetual refinement, which is philosophically aligned with continuous learning and adaptation.

In summary, A.17 is the linchpin that turns a loose collection of measurement practices into a **coherent, principle-driven system**. It rationalizes the language, thereby rationalizing thought: by speaking in one clear voice about measurements, FPF ensures that every number in the system can be trusted to answer “value of what, on what scale, relative to what context.” This rationale is reflected in improved model integrity and cross-domain trust in the meaning of metrics.

### 10. Relations

-   **Builds on / Elaborates:** _FPF Core Measurement Schema_ (as outlined in C.16). A.17 lifts the metric template concepts from C.16 into a kernel-level rule. It also reinforces **A.7 Strict Distinction**, by giving each measurement concept a unique name and forbidding overloaded terms.
    
-   **Constrains:** All other patterns and architheories that define or use metrics. For example, **A.3.3 `U.Dynamics`** (system dynamics) must name its state variables as Characteristics with proper scales (it cannot refer to them loosely as “KPIs” without context). Similarly, any **Service-level agreements (A.2.3 `U.Service`)** or **assurance calculations (B.3, D.3 patterns)** that involve measurements are governed by this canonical terminology (no unwarranted synonyms or unit confusion per ISO/IEC 80000, ISO/IEC 25024, QUDT, SOSA/SSN best practices). The pattern’s lexical rules are part of the **LEX-BUNDLE** (E.10) – any FPF-conformant context must adhere to these naming conventions.
    
-   **Coordinates with:** **A.18 (CSLC-KERNEL)**, which defines the minimal **Characteristic/Scale/Level/Coordinate** Standard in detail. A.17 provides the vocabulary and basic distinctions (what is a Characteristic, and its arity), while A.18 applies this to ensure each measurement template is well-formed. Also coordinates with **C.KD-CAL** and **C.CHR-CAL** (Knowledge Dynamics Calculus, Characterization Calculus) – those architheories use the Characteristic/Scale constructs to build domain-specific metrics (e.g. knowledge quality scores) and rely on A.17’s canon for consistency.
    
-   **Anticipates:** **E.10 Lexical Discipline** rules – A.17’s enforcement of a single term and controlled aliases is a concrete instance of the lexical uniformity mandated in E.10. It also paves the way for **F.7 Concept-Set Bridges** in Unification patterns, since external ontologies for quantities (ISO 80000, QUDT, etc.) can be mapped cleanly onto FPF Characteristics now that the term is fixed. In short, A.17 is a foundational lexicon pattern that a) ensures internal consistency and b) simplifies alignment with external standards for measurable properties.
    


---

## A.18 (A.CSLC‑KERNEL) — Minimal CSLC in Kernel (Characteristic ⟷ Scale ⟷ Level ⟷ Coordinate) `[A]`

**Aliases (for narrative use only):** _“Axis”_ (≈ Characteristic), _“Point”_ (≈ Coordinate). _(These colloquial aliases may be used in Plain language **explanations**, but never in formal identifiers or normative text.)_

### 1\. Context

We often need to **characterize some aspect** of a subject (be it a single artefact or a relationship between artefacts) in a rigorous way. Whether it’s recording a physical quantity, an architectural property, or a performance rating, the characterization must:

-   remain _domain-neutral_ (work for engineering metrics, subjective scores, etc.),
    
-   ensure that two measurements are **comparable if and only if** they share the same defined aspect and scale, and
    
-   accommodate both **ordered tiers** (qualitative levels like Low/Medium/High) and **numeric magnitudes** (continuous or interval values) without mixing them up.
    

In FPF’s kernel, the **CSLC pattern** (CG‑frame–Scale–Level–Coordinate) provides the minimal vocabulary and constraints to achieve this. It defines how one **Characteristic** ties to one **Scale**, and how any measured **value** can be treated as a **Coordinate** on that scale (with an optional named **Level** if the scale is discrete or tiered). The context here is the need for a _unified Standard_ so that every single measurement in any architheory can be interpreted and compared on common grounds.

### 2\. Problem

**Uninterpretable values.** A raw number or label means nothing without knowing **what aspect it measures** and **how it is measured**. The string “4”, the label “High”, or the real number 9.81 convey no insight unless we know **which Characteristic** they pertain to and the **Scale** that gives them meaning. In cross-disciplinary work this ambiguity is magnified: a “5” could be a risk rank (ordinal), a length in meters (ratio), or a satisfaction score (perhaps interval). Common failure modes include:

-   In **ordinal settings** (e.g. expertise levels _Novice < Skilled < Expert_), one can **rank** values but not meaningfully add or average them. Treating ordinal labels like numbers (e.g. averaging _Novice=1, Expert=3_) produces invalid results.
    
-   In **cardinal settings** (e.g. seconds, meters, degrees Kelvin), arithmetic operations do make sense – but only if units are respected and zero is meaningful (for ratio scales). If we strip away units or mix scales (seconds vs. minutes), we again get nonsense.
    

Without a strict Standard, one team might treat “High” and “Medium” as having a numeric gap, another might average **4** (on a 5-star scale) with **4** (as 4 seconds) because both are “4”. **Inconsistent practices make cross-domain reasoning impossible.** We need a kernel-level solution that _fixes_: (a) the **aspect being measured**, (b) the **scheme by which it’s measured**, and (c) the **type of scale structure** (ordinal vs. metric), _and_ that ensures each reported value is bound to that scheme. At the same time, the Standard should _not_ force artificial numeric detail where it isn’t applicable (e.g. we shouldn’t assign meaningless numbers to purely qualitative tiers just to satisfy a structure).

### 3\. Forces

-   **F1 – Transdisciplinarity.** The pattern must uniformly handle measurements in _physical domains_ (e.g. length, time, temperature), _system attributes_ (e.g. a module’s coupling or reliability), and _human judgments_ (e.g. user satisfaction scores). It needs to be neither overly quantitative (alienating softer domains) nor overly qualitative (lacking precision for hard science).
    
-   **F2 – Comparability vs. freedom.** We want to compare “like with like” – e.g. two readings of the same Characteristic on the same Scale – with absolute confidence. At the same time, the system should allow **different Scales for the same Characteristic** when necessary (for example, one project might measure Quality on a 0–5 star scale, another on a 0–100 percentage scale). The pattern must permit such flexibility _without_ letting those differing scales be conflated.
    
-   **F3 – Ordinal vs. cardinal integrity.** The Standard should preserve the nature of the data: **order-only vs order+distance**. If something is ordinal (ranks, grades), the framework should prevent unwarranted numeric operations on it. If it’s cardinal (real-valued with units), the framework should enable arithmetic but still keep track of units and zero. In essence, it must protect ordinal data from “leaking” into interval arithmetic.
    
-   **F4 – Named tiers vs. continuous magnitudes.** In many domains, **named Levels** (tiers or grades) are useful – e.g. Technology Readiness Levels or bond credit ratings – whereas in others, a continuous scale is needed. The pattern should support **optional Level labels** (for tiered scales) _without forcing_ every scale to have such labels. In other words, Levels are an add-on for discrete/tiered scales, not a requirement for truly continuous measures.
    
-   **F5 – Method agnosticism.** The kernel Standard should say _what_ must be defined (Characteristic, Scale, etc.) but **not prescribe how measurements are obtained**. Whether a value comes from a sensor reading, a simulation, or an expert judgment is up to the respective architheory (e.g. Sys-CAL vs. KD-CAL). The pattern must not bake in any process or scoring methodology; it only ensures that once a measurement exists, it’s well-formed and comparable. This avoids locking in any particular assessment method.
    

### 4\. Solution

**Adopt a minimal “one characteristic – one scale – one coordinate (value)” Standard for all measurements.** In the FPF kernel, any metric must bind **exactly one Characteristic to exactly one Scale**, and any observation produces **one Coordinate (value)** on that Scale (with an optional **Level** name if the scale has discrete tiers). We nickname this the **CSLC clause**:

> **Exactly one Characteristic + exactly one Scale ⇒ one Coordinate (value), with an optional Level.**

Concretely, the parts of this clause are defined as follows:

-   **Characteristic:** the aspect or feature being measured (the “CG‑frame” along which comparison is made). It answers “_What are we measuring?_” – e.g. _Distance, Temperature, Quality, Reliability_.
    
-   **Scale:** the organized set of possible values that the Characteristic can take, including the type of scale (_ordinal_, _interval_, or _ratio_), the measurement **Unit** (if applicable), and any bounds or structure. The Scale defines “_How do we measure it?_” – e.g. “meters on a linear scale from 0 up to 1000” or “ratings 1 through 5 with ordering only”.
    
-   **Coordinate:** a concrete measured value that locates the subject on the chosen scale. This could be a number (for a numeric scale) or a category label (for an ordinal scale). It answers “_What is the result?_” – e.g. 7.4 (meters), or _Expert_ (level).
    
-   **Level (optional):** a named **tier or category** on the scale, used only if the scale is tiered or discretized. For example, an ordinal scale might have Levels _Low, Medium, High_. A Level is essentially a human-friendly label for certain coordinates or ranges. On purely continuous scales, **Level** is not used.
    

Using this **CSLC structure**, every measurement is unambiguous and self-contained: the Characteristic tells us the context, the Scale tells us how to interpret the value, and the Coordinate is the outcome on that scale (with a Level label if appropriate). Notably, this pattern _forbids bundling multiple characteristics into one metric_ – each metric template is one-characteristic-per-template to keep semantics crisp. If something needs to assess multiple factors, it should be modeled as multiple CSLC metrics or a higher-level composite (see §8 below). This one-aspect-one-scale rule is what allows unambiguous comparison and prevents hidden complexity.

Finally, the solution ensures **tier optionality**: If a domain uses named Levels, we include them; if not, we don’t force it. For example, one can have a _Bug Severity_ Characteristic with Levels {Minor, Major, Critical} on an ordinal scale, whereas a _Length_ Characteristic would have a continuous scale (no predefined levels, just units). Both fit the pattern.

### 5\. Archetypal Grounding (System & Episteme Examples)

**In a physical scenario (`U.System`):** Consider an athlete’s long jump. We define a Characteristic **Jump Distance** with a Scale “meters (m)” ranging from 0 upward (ratio scale with meters as the unit). When the athlete jumps and lands at 7.45 m, we record a **Coordinate** of _7.45 m_ for the Jump Distance Characteristic. Here, Jump Distance is the Characteristic, the meter-scale is the declared Scale, and _7.45 m_ is the value (Coordinate). Because this is a cardinal measurement, we can meaningfully say one jump is 1.5 m longer than another, etc. Now consider another metric in the system: **Battery Health** of a device, which might be categorized qualitatively. We could define an ordinal Scale with Levels like _Good, Fair, Poor_ for the Battery Health Characteristic. If a particular device is rated “Poor”, that is a Coordinate on the Battery Health scale (with _Poor_ as the Level name). No arithmetic is done on these labels, but we can order devices by health (Good > Fair > Poor). Both examples illustrate the one-characteristic-one-scale rule: the jump’s distance is not combined with any other aspect; the battery’s health is evaluated on its own defined scale.

**In a knowledge context (`U.Episteme`):** Consider measuring an author’s expertise in a certain domain. We introduce a Characteristic **Expertise Level** for a person, with an ordinal Scale defining tiers such as _Novice, Competent, Expert_. Alice might be assessed at _Expert_ level in software engineering – that’s a **Coordinate** on the Expertise Level scale for the Characteristic “Software Engineering Expertise”. Bob might be at _Competent_. We cannot average Alice’s and Bob’s levels, but we can say the scale is ordered (_Expert_ > _Competent_ > _Novice_). For a more quantitative episteme example, consider a Characteristic **Hypothesis Confidence** for a scientific claim, with a Scale 0–1 (or 0–100%) representing probability or confidence level (ratio scale). One hypothesis might have a confidence of 0.95, another 0.7; these are Coordinates on the Confidence scale. We can compare them numerically (0.95 is higher than 0.7, and 0.95 _implies_ a stronger belief), and we could even combine multiple confidence values through Bayesian formulas (if justified) – but crucially, we would only do so in a way that respects their scale (probabilities combined properly, not treated as arbitrary scores). The Expertise Level and Hypothesis Confidence examples show how the CSLC pattern accommodates both an ordinal qualitative measure and a continuous quantitative measure in the knowledge domain, each with one Characteristic and one defined Scale.

### 6\. Bias-Annotation

The CSLC-Kernel pattern is crafted to be **maximally inclusive of different measurement types** while imposing just enough structure to ensure consistency. It does not privilege any particular domain or modality of measurement: a subjective 5-star rating is treated with the same formal rigor as a physical length in meters. In terms of the FPF principle lenses, this pattern consciously balances the **Architectural/Ontological** needs (clear structure for data) with the **Pragmatic/Didactic** needs (flexibility and clarity for users). There is little risk of cross-domain bias here because the pattern explicitly supports both extremes (ordinal and ratio, qualitative and quantitative). By remaining **method-agnostic**, it avoids bias toward certain validation techniques – e.g. it doesn’t assume every measurement comes from an instrument (it could come from expert judgment just as well). One might argue the pattern enforces a somewhat formal approach to what could be informal measures (forcing definition of scale and characteristic), but this formalism is lightweight and is precisely what makes the metric interpretable. In summary, A.18 embodies **neutrality**: it’s a container that fits any content as long as that content is well-labeled. It reinforces **P‑2 (Didactic Primacy)** by making all metrics self-explanatory in terms of what and how, and respects **P‑1 (Cognitive Elegance)** by using a minimal, uniform scheme. No cultural or disciplinary assumptions are baked in – an anthropologist’s “Cultural Significance” scale can live alongside an engineer’s “Voltage” scale with equal status. The pattern’s requirement for declaring polarity (“higher is better” vs “lower is better” vs target range) further avoids bias in interpretation – it prevents the assumption that “more is always better,” which might be untrue in many contexts (e.g. for error rates, lower is better). All these considerations ensure that A.18 introduces no hidden skew; it merely provides a fair playing field for all metrics.

### 7\. Conformance Checklist

When defining a new metric template or using measurements, practitioners **SHALL** verify the following:

1.  **One characteristic, one scale:** Each metric **template** binds exactly **one Characteristic** to exactly **one Scale**. If you find a metric trying to cover multiple things at once, split it into separate metrics.
    
2.  **Polarity declared:** For any **ordered** Scale (ordinal/interval/ratio), the **polarity** (“higher‑is‑better”, “lower‑is‑better”, “targeted optimum (symmetric or asymmetric around a declared target)”) **SHALL** be declared at the **template** that binds a Characteristic to a Scale. State whether higher values are better, lower are better, or if an optimal range/target exists. (For example: \*“higher is better” for a performance score, \*“lower is better” for error count, or _“target 37 °C” for body temperature where deviation in either direction is worse_.) This ensures that anyone comparing two values knows which way is “up.”
    
3.  **Unit and level clarity:** If the Scale is quantitative, specify the **Unit** (e.g. _seconds, meters, %_) and make sure all values include or assume that unit. If the Scale has named Levels, list them clearly and use them consistently. Do **not** use the same label to mean different things on different scales, and avoid using unit terms in Characteristic names (the unit belongs with the scale).
    
4.  **Scale-appropriate operations only:** Only perform those comparisons or calculations that are valid for the given scale type. For a nominal scale, you can check equality but not order. For an ordinal scale, you can order or rank values but not do math like “A minus B.” For interval scales, addition/subtraction is OK (with unit conversion if needed), but ratio comparisons (A is twice B) might not make sense without a true zero. For ratio scales, all arithmetic operations are allowed _with proper attention to units_. This check prevents logical errors (e.g. averaging “High” (3) and “Medium” (2) and getting 2.5 — which is meaningless).
    
5.  **No bare numbers:** Never present a raw number or value without its context of Characteristic and Scale. If someone sees “42” in your output, they should _also_ see or know “42 of what, measured how.” A reader who is not aware of the metric’s template should not be left guessing what a given value signifies. In practice, this means labeling reports and data with the metric name or identifier so that values can be traced back to their meaning.
    
6.  **Template bridges for cross-metric comparison:** If you intend to compare or aggregate measurements from **different templates** (different Characteristics/Scales), ensure an explicit **ScoreMethod** or conversion is defined. For example, if you need to combine a “usability score” (0–5 stars) with a “security score” (0–100%), you might define a new **Score** that maps both onto a common 0–10 scale via monotonic functions. Without such a bridge, do not directly mix metrics – keep them separate in analysis. This guarantees that any cross-metric reading has a well-founded basis.
    
7.  **Level optionality respected:** If your Characteristic doesn’t naturally have tiers, don’t force it to have **Level** names (you can leave the Level concept unused). Conversely, if your Characteristic is commonly described in categories, it’s fine to define Levels for clarity. The key is to use the Level field intentionally: either not at all (for truly continuous measures) or in a fixed, **non-overlapping** way (for discrete categories). Do not use “Level” for something that behaves like a continuous value (it would be confusing to assign a label where a number would do, or vice versa).
8. **Comparability test:** Two Coordinates are comparable iff same Characteristic+Scale (incl. unit, polarity). Otherwise — Score‑level only after a declared SCP to a bounded range.

_(The above serve as normative checkpoints. Many of these are automatically supported by using the standard metric templates in software: e.g. the system will enforce one Characteristic per template, require a unit for ratio scales, etc. The **Lexical rules** from A.17/E.10 are assumed: use canonical names and notations for all parts of the metric.)_

### 8. Consequences

Adopting the minimal CSLC Standard in the kernel yields a number of benefits:

-   **Universal interpretability:** Every measurement is intrinsically self-describing. One cannot have a “mystery number” floating around; by design you must know it’s _X (Coordinate) on Y Scale of Z Characteristic_. This dramatically reduces miscommunication in reports and data exchange. An engineer and an analyst can share a metric knowing they interpret it the same way, because the context travels with the value. Level is optional when scale is tiered or discreet. 
    
-   **Safe comparison and aggregation:** Values can only be compared when they belong to the same Characteristic and Scale (or when an authorized SCP converts them). This prevents the common error of comparing apples to oranges. When cross-comparison is needed, the pattern funnels us into creating a proper normalization, which improves the soundness of composite scores. Essentially, it’s now impossible to accidentally average an uptime percentage with a user satisfaction rating, for example, without explicitly defining how to map one to the other.
    
-   **Flexibility across domains:** The pattern is **transdisciplinary**. It doesn’t matter if the measurement is temperature in Kelvin, length in inches, code complexity in “abstract points,” or user satisfaction on a five-level Likert scale – all are handled uniformly. This makes it easier to plug new architheories or domains into FPF, since they don’t need special rules for their metrics; they just instantiate the CSLC template in their context.
    
-   **Ordinal and cardinal handled with equal rigor:** By explicitly classifying scales, the pattern gives ordinal data the respect it deserves (no pretending it’s numeric) and gives ratio data the formal context it needs (units, zero, etc.). This balance means both qualitative assessments and quantitative measurements live side by side, each with their constraints respected. Domains that lean heavily on categorical ratings benefit from the **Level** concept (with no pressure to assign fake numbers), and domains that use real measurements benefit from unit enforcement and type-aware computations.
    
-   **Clarity in multi-factor scoring:** The prohibition of implicit multi-characteristic measures means that any “overall” score or index has to be constructed out of known pieces. This tends to improve the transparency of complex scoring schemes. If an organization wants to create a single index from 5 different metrics, A.18 forces them to introduce a defined ScoringMethod function that combines those 5 Coordinates into one Score, with declared monotonicity and bounds. The consequence is that composite metrics become auditable and debatable (you can examine the weighting or formula) rather than opaque sums.
    
-   **Methodological neutrality (and innovation):** Because the kernel imposes no method for obtaining the values – only how to frame them once obtained – architheories and tool builders are free to innovate in how they measure things. The Standard just ensures that once they do, everyone else can understand and use the results correctly. This separation of concerns (what vs. how) accelerates multi-disciplinary collaboration: a social scientist’s observational scale can feed into a systems model without any confusion, as long as it’s couched in the CSLC terms.
    

On the downside, **users must do a bit more upfront work** to define their metrics. The pattern’s requirements (declare Characteristic, define Scale, etc.) mean one cannot simply say “we’ll track a risk score” without further detail. In practice, this is a _desirable_ trade-off: the extra effort (perhaps a few minutes to set up a metric template) prevents far greater confusion down the line. Another possible trade-off is **multiplicity of scales** – the pattern allows the same Characteristic to have multiple scales (in different contexts or versions), which might fragment data if not managed (e.g. two teams measuring “Performance” on different scales). However, it also provides the remedy: make the difference explicit and, if needed, build a conversion Gauge. This explicitness is actually beneficial, as it highlights when “Performance (0–5)” is not directly comparable to “Performance (Percentage)”. In short, any fragmentation is out in the open and can be dealt with via alignment or bridging.

Overall, A.18’s consequences are overwhelmingly positive: **measurements become first-class, well-understood citizens of the model.** The cost is a slight increase in definition effort and discipline, which is a small price for coherence. Once this pattern is in place, higher-level patterns (in Parts B, C, D) that reason about metrics can rely on it. For example, trust calculations (Part D) can assume that any metric they consume has a known scale and meaning, and knowledge dynamics algorithms (Part B or C) can safely combine evidence knowing the comparisons are valid. The minimal CSLC Standard is thus a foundational enabler for robust, cross-domain assurance in FPF.

### 9\. Rationale

The rationale behind A.18 is to enforce _semantic clarity_ at the data level, thereby solving a host of downstream problems. Without this pattern, one must constantly ask, “What does this number mean? Can I combine these two values?” – questions that have led to many project errors. By building the answers into the framework (“every number knows its unit, scale, and aspect”), we front-load the work and eliminate ambiguity. The solution directly addresses each force:

-   **Transdisciplinarity:** We include both ordinal and cardinal mechanisms so that no discipline’s metrics are left out. This was informed by observing multi-disciplinary teams: e.g., in a single project, a human factors specialist might rate usability (ordinal) while an engineer measures throughput (ratio). A.18 gives them a common language and prevents one from misusing the other’s data. It embodies the idea that _universal structure enables local freedom_: everyone’s metric can plug in, as long as they specify it properly.
    
-   **Comparability vs. freedom:** The pattern strikes a balance by tying comparability to explicit commonality. If two metrics truly measure the same thing in the same way, then of course you can compare them – they’ll share Characteristic and Scale. If they differ, the framework doesn’t stop you from defining them (freedom), but it does stop you from _conflating_ them inadvertently. The introduction of **polarity** declarations is a direct response to this tension: it adds a tiny burden (must declare “higher is better” etc.) but yields big pay-off in avoiding mis-ordered interpretations and enabling safe composite scoring (monotonic Gauges).
    
-   **Ordinal vs. cardinal separation:** The rationale here is guided by measurement theory: we want to preserve information content. Treating ordinal data with only order operations preserves all its information; doing more (like adding them) injects false information. The pattern’s strictness on scale types forces modelers to be honest about what their data can and cannot do. This not only prevents errors but also encourages **best practices** (e.g. if you find you desperately want to average an ordinal score, perhaps you should refine it into an interval scale in your methodology). The outcome is a framework that respects both the **qualitative** and **quantitative** realms appropriately, aligning with **FPF’s Pillar of Pragmatism** – use formalism where it’s justified, but not beyond its limits.
    
-   **Optional Levels:** Requiring Levels in every case would have been too rigid (not everything has named tiers), but not supporting them would fail domains that rely on them (like maturity models or grading systems). The rationale for making Level _optional_ is to accommodate both. We saw in practice that many metrics naturally form tiers (e.g. technology readiness levels TRL 1–9) and giving them a slot in the model (instead of burying them in definitions) makes those metrics much easier to work with and integrate. Meanwhile, continuous metrics carry no baggage of unused fields. This design was checked against existing standards (like ISO 25024 for quality measures) to ensure we aren’t deviating from industry expectations: indeed, separating the concept (Characteristic) from the scheme (Scale) aligns well with standards, and including an optional categorization aligns with common practice in capability maturity models, etc.
    
-   **Method neutrality:** The decision to _not_ include any measuring procedures in A.18 (no specific formulas, no mandated evidence type) comes from the principle of separation of concerns. The kernel should provide the _what_ and _how (structurally)_, while architheories provide the _how (procedurally)_. This keeps the kernel lean (**P‑1 Cognitive Elegance**) and allows domain experts to implement whatever method is appropriate, merely committing to wrap their results in the CSLC form. By doing so, we avoid any bias toward empirical vs analytical, or manual vs automated measurements – FPF welcomes all, as long as they conform to the schema. This was rationalized by examining case studies: e.g., some reliability metrics come from formal proofs (analysis), others from testing (empirical) – the kernel can host both results identically, requiring only that each result says what it measured and on what scale.
    

In essence, A.18 is the _infrastructure of meaning_ for metrics. It may appear as a simple template, but it’s profoundly enabling. It forces clarity at creation time, so we don’t have to infer or debate meaning at usage time. The pattern’s strength lies in preventing errors that _don’t have to happen_. It encodes lessons from both metrology (the science of measurement) and everyday data science (where unit errors and mis-comparisons are infamous issues). The rationale is backed by these lessons: **fix the interpretation rules in the design, and you eliminate entire classes of confusion and mistakes.** By having this in the kernel, every architheory – from knowledge scoring to system performance – benefits immediately, and their results become interoperable to a degree that would be impossible without a common structure.

### 10\. Relations

-   **Extends/Uses:** **A.17 (CHR-NORM)** – A.18 explicitly builds on the canonical terminology established in A.17. It uses the term **Characteristic** as defined there (and no other synonyms) and carries forward the edict that “axis/dimension” be treated as mere narrative aliases. It also leverages the Entity-vs-Relation Characteristic distinction from A.17: Section 7.4 of this pattern references tests for disambiguating relational metrics. Essentially, A.17 provides the **lexical and conceptual groundwork** (what a Characteristic is, and the basic vocabulary), while A.18 provides the **structural and normative rules** for linking Characteristics to measurements.
    
-   **Core foundation for metrics:** This pattern underpins the **Measurement & Metrics Characterization spec (C.MM‑CHR)** – the architheory that implements metric storage and computation. In MM-CHR, every `U.DHCMethodRef` and `U.Measure` follows the CSLC format defined by A.18. By lifting CSLC rules to the kernel, we ensure all architheories (like **KD-CAL** for knowledge dynamics, **Sys-CAL** for systems, or any custom CAL/CHR) share a common approach to metrics. A.18 also informs the design of **CHR-CAL (Characterisation Calculus)**, which generalizes measurable property templates: CHR-CAL relies on the one-Characteristic-per-metric assumption and the comparability rules set here to compose higher-level characterizations.
    
-   **Enables dynamic reasoning:** A.18’s insistence on well-defined Scales allows patterns like **A.3.3 `U.Dynamics`** (system dynamics models) to incorporate measurement dimensions as state variables without ambiguity. For example, a `stateSpace` in a dynamics model can be explicitly defined as a set of Characteristics (each with units and ranges), making simulations and traces dimensionally consistent. If A.18 were not in place, one model might treat “performance” as a 1–5 score and another as a probability – combining them would be incoherent. With A.18, such differences must be reconciled via a Gauge or kept separate, preserving coherence in multi-model analyses.
    
-   **Coordinates with assurance patterns:** Many patterns in Part B and D (for trust, assurance, and ethics) involve **scores** and **metrics**. For instance, **B.3** (Assurance Levels) computes overall assurance from evidence scores; A.18 ensures those input scores are well-defined and comparable (e.g. all are 0–1 or all are percentages, with polarity noted). **D.4** (Trust-Aware Calculus) might combine trust metrics across domains – again, A.18 provides the common ground so that a “trust score” coming from an operational metric and one coming from a social rating can be normalized and compared meaningfully. In summary, any pattern that aggregates or uses measurements is constrained (in a positive way) by A.18’s rules. They “plug into” this framework.
    
-   **Constrained by lexical rules:** This pattern’s content is part of the formal lexicon governance. It works within **E.10 LEX-BUNDLE**, which means the terms _Characteristic, Scale, Coordinate, Level,_ etc., are controlled vocabulary. A.18 localizes some generic requirements from A.17 (for example, A.17 mandates polarity in principle; A.18 requires it be declared per template in practice). It also aligns with external standards: by having explicit scale types and units, it dovetails with ISO/IEC measurement terminology and allows straightforward mapping to frameworks like **ISO 80000 (quantities and units)** and **Stevens’s scale types**. This relation to standards is deliberate – it eases **F.9 (Alignment Bridge)** construction to external ontologies by having a clean internal schema (A.18 provides that schema). In effect, A.18 is where FPF’s internal consistency meets external compatibility, ensuring our measurement semantics can relate to those outside FPF when needed.


---

## A.19 (A.CHR‑SPACE) — CharacteristicSpace & Dynamics Hook `[A]`

**Non‑duplication note.** This pattern reuses the canonical measurement concepts (`U.Characteristic`, **CSLC** terms) from **A.17/A.18** and relies on **C.16 (MM‑CHR)** for **normalization evidence**. It **does not redefine** units or normalization semantics. **UNM** *names admissible re‑parameterizations within one `U.BoundedContext`* and thereby **induces a context‑local congruence** over charts, written **≡_UNM**, which is a **specialization of the framework’s congruence notion** used in **B.3** (and instantiated for epistemes in **B.1.3**). A **NormalizationFix** selects a canonical representative of an **≡_UNM** class. Timebases and laws remain out of scope (see **A.3.3**).
**Locality & governance.** A **UNM** is *context‑local*: it is declared within a single `U.BoundedContext` for a given CharacteristicSpace (or family of charts) and **enumerates** (a) the **admissible classes of NormalizationMethod**, (b) the **invariants** they must preserve, (c) **closure** under composition (and inverses where defined), and (d) **validity/versioning rules** (editions, windows). Semantics and evidence backing remain under **C.16**; A.19 constrains how UNM artifacts are *named and used* in state/comparability logic. **Cross‑context reuse** of a UNM **MUST** be declared via **A.6.1 Transport**; when the *describedEntity* changes, declare a **KindBridge (CL^k)**. Any **CL^plane** penalties **route to R/R_eff only**.

### 0 · Terminology update (Normalization) — replaces legacy “gauge/map/κ”
**UNM — Unified Normalization Mechanism.** A mechanism that packages admissible re‑parameterizations for a CharacteristicSpace so that values can be normalized for safe comparison **within one `U.BoundedContext`**.
**NormalizationMethod.** A concrete method within UNM (intensional definition of how to normalize a slot or a vector of slots). **Method classes SHALL be scale‑appropriate:** ratio → positive‑scalar conversion; interval → affine transform; ordinal → order‑preserving monotone map; nominal → categorical re‑map; lookup table (**LUT**) with uncertainty annotations (where declared). These classes are **named consistently** across the spec as: `ratio:scale`, `interval:affine`, `ordinal:monotone`, `nominal:categorical`, `tabular:LUT(+uncertainty)`.
**NormalizationMethodDescription.** The **epistemic** description of a NormalizationMethod (documentation/spec with bounds, validity window, Evidence Graph Ref).
**NCV — NormalizedCharacteristicValue.** The **result** of applying a NormalizationMethod to a **coordinate value** (or vector) in a CharacteristicSpace. *Note:* **Characteristics** themselves are **not** normalized; **values** (coordinates) are.
**NormalizationMethodInstance.** A concrete, editioned **use** of a NormalizationMethod in a CN‑frame or embedding (binds method → slot(s), edition, validity window). Use this term when referring to stored/ID’d artifacts (e.g., in logs), to avoid overloading **map**.
**UNM‑congruence (≡_UNM).** Context‑local equivalence relation over **charts** generated by the admissible **NormalizationMethods** declared in the UNM; two charts are **≡_UNM** iff they are related by a chain of admissible, **scale‑appropriate** transformations that preserve the declared invariants.
**IndicatorChoicePolicy.** Principles/rules for selecting which Characteristics (or their NCVs) become Indicators for decisions.
**Indicator.** The result of applying an IndicatorChoicePolicy to a set of Characteristics/NCVs; an Indicator is **not** a target value by itself and **not** any normalized value by default.
**Indicatorization (policy step).** Selecting Indicators is a **separate**, policy‑governed step; producing NCVs alone **does not** yield Indicators.
**Removal of κ‑notation.** The previous κ symbol and derived phrases (e.g., “κ‑operator”) **for normalization** are retired in favor of explicit names: *Normalization, NormalizationMethod, NCV, UNM*. This retirement does **not** affect unrelated uses of κ as a generic metavariable in logic or requirements schemas elsewhere in the spec.
**Lexical note (map vs Map).** In this document, lowercase **map** denotes a mathematical function only. Capitalized **Map** (e.g., `DescriptorMap`) retains its Part‑G meaning as a **method type** that encodes subjects into a declared Space; it is **disjoint** from **NormalizationMethod/UNM**. Do **not** use “map/Map” as a synonym for **NormalizationMethod**, **NormalizationMethodInstance**, or **NCV**.

### 1 · Intent & Scope (Normative)

**Intent.** Establish a **kernel‑level state‑space type**—`U.CharacteristicSpace`—so that any holon’s **state changes** (e.g., a system’s condition or a role’s readiness) can be formalized as **trajectories in a space of declared Characteristics with chosen Scales**. For **epistemes**, state is governed by **ESG**; **F–G–R** are **assurance coordinates**, not a state space. This gives every `U.Dynamics` model a well‑typed `stateSpace` and enables formal state certification (using RoleStateGraph checklists) instead of narrative stage transitions.

**Scope.** Pattern A.19 **defines**:

-   the **type** `U.CharacteristicSpace` as a finite product of **slot value sets** (per A.18),
-   the **slot** construct for each factor (a pairing of a **Characteristic** with a chosen **Scale**),
    
-   minimal **structural overlays** (optional **order**, **topology**, **metric** hooks) that downstream architheories _may_ attach to a space, and
    
-   the **hook** `U.Dynamics.stateSpace : CharacteristicSpace` – i.e. the requirement that any dynamics model declare a CharacteristicSpace for its state space (typing only).
    

A.19 **does not** introduce any new measurement aspects, composite metrics, or **normalization semantics** (those are provided by **C.16 (MM‑CHR)** under **UNM**), and it does not define how dynamics evolve over time or any predictive laws (see **A.3.3** for dynamics semantics). The focus here is purely on the _structure of state spaces_ and their comparability.

**Lexical guard (“map”).** In normative text, lowercase **map** refers only to a mathematical function; it MUST NOT be used as a synonym for **NormalizationMethod**, **NCV**, or **UNM**. Capitalized **Map** keeps its suffix‑family meaning (e.g., `DescriptorMap`) and is unrelated to normalization. Use **NormalizationMethod** for the transform and **NCV** for its output.

**Lexical guard (“carrier”).** In kernel prose, **Carrier** (capitalized) names `U.Carrier` (a **symbol bearer**). Do **not** use “carrier” for set‑theoretic supports; prefer **ValueSet**/**underlying set**. A.19 therefore uses **ValueSet(slot)** for the set that supplies values to a slot.

### 2 · Context (Informative)

FPF’s kernel already standardizes **what** is measured (a **Characteristic**, per A.17) and **how** it is measured (a **Scale** with units, via the **CSLC** Standard in A.18). We also have a measurement substrate (`U.DHCMethodRef`, `U.Measure`) to handle individual observations. What has been missing for modeling **dynamics** is a canonical “Context” in which **multiple Characteristics** can co-exist so that complex **states** (with many aspects) and their **trajectories** are well-typed and comparable. Without a formal CharacteristicSpace, teams either hard-code ad-hoc vectors (often with inconsistent assumptions) or fall back to informal lifecycle stories (“phases” or stages) that contradict the kernel’s open-ended, non-linear evolution paradigm. The Architectural patterns (A-cluster) expect that `U.Dynamics.stateSpace` will be a set of **declared Characteristics each with a declared Scale**. Pattern A.19 delivers exactly this capability, leveraging the CSLC measurement discipline without reinventing any arithmetic or unit-handling logic.

### 3 · Problem (Informative)

-   **P1 — “Feature vector” drift.** In practice, teams often assemble state vectors or “feature” lists with implicit or mismatched units and scales. Without a formal space, one coordinate’s value can’t safely be compared or combined with another’s (e.g. mixing degrees Celsius with percentages). **CSLC** guarantees consistency **per Characteristic**, but a bundle of multiple “characteristics” remains under-specified if we lack a unified space definition.
    
-   **P2 — Lifecycle bias.** Absent a formal state space, system change tends to be described in terms of fixed **stages or phases** (design phases, maturity levels, etc.). This conflicts with FPF’s **open-ended** stance: in FPF a role’s state model (RSG) allows re-entry and refinement of states rather than one-way lifecycle stages with an “end.” We need a space model that treats evolution as continuous movement, not a one-directional sequence.
    
-   **P3 — Incoherence across CN‑frames.** Different modeling “CN‑frames” (architecture vs. epistemic vs. operational) often choose different sets of qualities to measure (different sets of characteristics). Later, however, we may need to **compose** these models or **project** one into another. Without a kernel notion of how one state space can be a **subspace** of or **embedded** in another, any integration of models will be ad hoc and error-prone.
    
-   **P4 — Relational measurements.** Some Characteristics are inherently **relational** (e.g. a _Coupling_ between two components, or _Distance_ between points). Naïvely forcing such traits into a single-object feature vector loses critical information (arity, symmetry). The kernel already distinguishes single-entity vs multi-entity Characteristics (A.17); we must preserve that distinction in the state space so that a relational metric isn’t treated as an intrinsic one by mistake.
    
-   **P5 — The geometry temptation.** When defining a state space, it’s tempting to assume or inject additional structure (ordering of states, topologies for continuity, metrics for distance) as if inherent. But the kernel must remain minimal and domain-neutral: it should not **smuggle in** analysis methods or domain-specific norms under the guise of geometry. Any such structure should be added explicitly by specialized architheories, not baked into the core definition of a space.
    

### 4 · Forces (Informative)

-   **F1 – CSLC integrity at scale.** When combining multiple measurements into a state, we must uphold the **CSLC discipline** for each component: each coordinate has a defined Characteristic, Scale type, unit, and (if applicable) polarity. We need to do this without redefining or duplicating that single-characteristic integrity – the multi-dimensional space should simply enforce CSLC per slot.
    
-   **F2 – Transdisciplinarity & lexical clarity.** The state space framework must work for **quantitative physical metrics** (ratio scales, continuous units), **qualitative assessments** (ordinal scales, tiers), and mixtures thereof. It must not be biased toward one domain’s notion of measurement. At the same time, to avoid confusion, the **lexicon must remain canonical**: we use _Characteristic_ (not “axis/dimension”) as the formal term for a measured aspect, regardless of domain, per A.17’s naming convention.
    
-   **F3 – Arity and semantics.** Lifting various Characteristics into a unified space should not obscure their nature. If a Characteristic is defined as a relation (multi-entity property), the state space must represent it appropriately (e.g. as a coordinate that is a tuple or a symmetric relation) rather than flattening it into an unrelated scalar. Entity-specific vs relational properties must remain clear in the space’s structure.
    
-   **F4 – Minimal core, extensible further.** The kernel should provide only the **bare essentials**: a carrier for state with proper typing. It should be possible to impose additional structure like order, topology, or metrics _if and when needed_ by downstream theories, but these must be **optional overlays**. The core space definition should be minimalistic to allow broad use, yet capable of extension for advanced needs.
    
-   **F5 – Composability of spaces.** We need well-defined operations to **project** a state space to a subspace (dropping some Characteristics), **embed** one space into a larger space (mapping coordinates from one context to another), and take **products** of spaces (combining different state spaces into a joint space). These operations are crucial for composing sub-models, comparing alternatives, or aligning different “CN‑frames” (for example, linking an architectural model’s state space with a metrics model’s space). The approach must support such composition in a principled way.
    
-   **F6 – Alignment with RSG (state machines).** In FPF, formal **state certification** is done via checklists on RoleStateGraphs (A.2.5). Our state space concept must complement that: i.e. the **state** of a holon remains an **intensional** concept (defined by criteria), but those criteria are evaluated against the measurable **coordinates** in a CharacteristicSpace. The design must allow checklists to map observed coordinates to named states and enable re-certification as states evolve, rather than locking states into a static progression.
    

### 5 · Solution

#### 5.1 `U.CharacteristicSpace`

##### 5.1.1 Type signature

Let **I** be a finite index set labeling a collection of **slots**. Each **slot** _i_ (for _i ∈ I_) is defined as a pair:

> **`slot_i = (Characteristic_i, Scale_i)`**,

where:

-   `Characteristic_i` is a `U.Characteristic` (with an explicit arity, i.e. either an entity-Characteristic or a relation-Characteristic as defined in A.17), and
    
-   `Scale_i` is a chosen **Scale** for that Characteristic (with a specified scale type and unit, per A.18 and the MM‑CHR rules).
    
Then a **CharacteristicSpace** (CS) is formally the Cartesian product of all slot **value sets**:

$$\mathbf{CS} = \prod_{i \in I} \mathrm{ValueSet}(\mathrm{slot}_i)\,.$$

In other words, a point (state) in the space consists of one coordinate value for each slot. A **state** _x_ in CS can be seen as a total function _x(i)_ that picks a value from each slot’s **ValueSet** (for every _i ∈ I_, _x(i) ∈ ValueSet(slot\_i)_). By kernel mandate, any `U.Dynamics.stateSpace` **SHALL** be bound to some instance of `CharacteristicSpace`, and all states or trajectories described by that dynamics model **MUST** lie within that space’s **value set**. (The actual dynamic **laws** and time progression are handled in A.3.3; A.19 only defines the state‑space container and its properties.)

##### 5.1.2 Slot discipline (invariants)

To ensure consistency and comparability, a CharacteristicSpace must obey the following invariants:

-   **A19-CS-1 (Exactly one per slot).** Each slot **binds exactly one** Characteristic to **exactly one** Scale (including a specific Unit or kind, if applicable). This mirrors the CSLC clause of “one aspect – one scale”: there are no ambiguous or compound mappings in a single slot. (If a Characteristic can be measured on multiple scales, only one is chosen for a given space; others would require separate slots or a different space.)
    
-   **A19-CS-2 (Named basis).** A CharacteristicSpace **SHALL** publish an ordered list of its slots as its **basis**. Each slot in the basis has a stable identifier (or key) that can be used in data structures or APIs. These basis names should be treated as technical identifiers (machine-readable tokens); any human-friendly alias or description for a slot should be provided only in the Plain register as a non-normative aid (per E.10). In short, the identity and order of slots in the space are explicit and stable.
    
-   **A19-CS-3 (Immutability of meaning).** Once a space is in use, the meaning of each slot is fixed. A slot’s `(Characteristic, Scale)` pair **MUST NOT** be retroactively altered. If requirements change (e.g. a different scale or a revised definition of the Characteristic), one **MUST** define a new version of the space (or a new slot) rather than silently changing the existing one. When a space is versioned or a slot replaced, an explicit **embedding** (mapping from the old space to the new space) should be published to relate historical states to the new coordinates. This ensures past data remains interpretable and prevents semantic drift.
    
-   **A19-CS-4 (Arity preservation).** If a `Characteristic_i` is defined as a **relation** (multi-entity characteristic), then slot _i_ represents a relationship among multiple entities. The coordinate value at such a slot is a **tuple** (with the appropriate entity types) rather than a simple scalar. The slot’s declaration **SHALL** indicate the relation’s symmetry or directionality as part of its meaning (this should align with how the Characteristic was originally defined in its template). In essence, relational Characteristics retain their arity in the space, so that we don’t confuse, say, “Coupling between X and Y” with an intrinsic property of X or Y alone.
 
-  **A19-CS-5 (No hidden normalizations or aggregations).** A CharacteristicSpace itself carries **no implicit normalizations or formulas** for aggregating coordinates. It is a _descriptive_ structure, not a scoring mechanism. Any computation that combines or transforms coordinates (e.g. producing an overall “score” or weighted sum) must be defined outside the core space – typically in an architheory that leverages the measurement framework (see C.16’s **UNM/NormalizationMethod** registry). In particular, any handling of **polarity** (which way “better” is) or weighting of different **slots** happens in those external formulas, not inside the space definition. The space provides the raw coordinates; the logic to interpret or aggregate them is added by domain‑specific layers with explicit disclosure of how it’s done.

 - **A19-CS-6 (Slot meta completeness).** Where applicable, each slot **SHALL** declare `admissible_domain` and **missingness semantics** (e.g., codes for *missing*, *censored*, *not-applicable*), consistent with the Characteristic’s Scale and with MM‑CHR. This prevents silent domain drift and clarifies how absent values participate in predicates and comparisons.

##### 5.1.3 Minimal structure hooks (optional overlays)

By default, a CharacteristicSpace has no assumed ordering or metric structure – it is just a Cartesian product of value sets. However, a space **MAY** declare certain structural attributes _as opt-in metadata_ (i.e. informative annotations that architheories can rely on, but not enforced by the kernel). These optional **overlays** include:

-   **Product topology.** A **topology** on the space, typically the product topology when slots that are quantitative (interval or ratio scales) need continuity considerations. Declaring a topology is useful if continuity or convergence arguments are relevant (e.g. to say a sequence of states approaches a limit state). By default, without declaration, no topological structure is assumed on the space.
    
_Lexical note:_ Here **“distance metric”** strictly means a mathematical distance function (or a generalized distance such as a **pseudometric** or **quasi‑metric**) on the state space. This is **not** to be confused with *metrics* as performance measures in MM‑CHR. In the **Tech** register, avoid the noun **metric**; refer to **`U.DHCMethod`/`U.DHCMethodRef`** for measurement templates (see **C.16**). Any distance overlay on a CharacteristicSpace must not conflict with scale semantics; it is an additional analysis structure, not a redefinition of measurement meaning.

These overlays are entirely **optional** and have no effect on the core meaning of the space – they exist only to support particular needs (like making **dominance**, **continuity**, or **distance** reasoning possible) in models that require them. If needed, they should be added deliberately by an architectural theory rather than assumed. This way, any ordering or metric properties of states are made **explicit** instead of relying on hidden or default arithmetic. _(Rationale:_ The CSLC and MM‑CHR rules already govern what operations are allowed on each scale; A.19’s approach is to let higher-level theories layer on an order, topology, or metric when appropriate, so nothing is taken for granted tacitly in multi-dimensional arithmetic._)_

##### 5.1.4 Dynamics hook (typing only)

Any model of change or dynamics in FPF must declare the state space it operates over. Formally, `U.Dynamics.stateSpace` **SHALL** be specified as a reference to a `CharacteristicSpace`. This creates a typing obligation: the dynamic model can only produce states (and trajectories of states) that lie in the given space. All predicates or predictions in such a dynamics model are understood to **quantify over** sequences of points in that CharacteristicSpace (with time semantics governed by A.3.3’s time base and laws). **Note:** A.19 defines only the structure of the state space; it deliberately **does not** fix any time axis or dynamic law. Those remain the responsibility of the dynamics pattern (A.3.3). A.19 simply ensures there is a well-defined space in which states live, so that dynamics are decoupled from any narrative “stage” and instead treat evolution as movement through this space.

##### 5.1.5 Lexical discipline (Normative)

In all **normative references, definitions, and identifiers** related to this pattern, the specification uses the canonical measurement terminology: **Characteristic**, **Scale**, **Level**, **Coordinate**, **CharacteristicSpace**, **slot**, **basis**. Legacy terms like “axis”, “dimension”, or “point” are **forbidden** in Technical/Formal registers of the spec (per A.17’s lexical rules). They may appear _at most once_ in explanatory **Plain** language as mapped aliases to aid understanding (and if used, must be explicitly identified as equivalent to the official terms). In this pattern, we consistently use “slot” or “basis element” (never “axis”) to refer to a component of a space, and “Characteristic” (never “dimension”) to refer to the measured aspect. This lexical discipline ensures clarity and consistency across the framework (see A.17 and C.16 L-rules for the formal policy on terminology).

##### 5.1.6 Quotients & NormalizationFix (Normative)

**Design rule — read invariants, not labels.** Eligibility, comparability and acceptance **SHALL** be decided on **quotients by ≡_UNM** (or on explicitly **Normalization‑fixed** charts), not on raw labels.

*Minimal obligations:*
1) **Name the quotient or fix.** If a checklist predicates over a **normalization‑variant** property, it **MUST** name the **NormalizationFix** (which **UNM.NormalizationMethod(s)** and chart are assumed) and thus the **≡_UNM** class.
2) **Declare NormalizationMethod class.** Every normalization used **MUST** name its **NormalizationMethod** class (affine / order‑preserving / LUT with uncertainty) and validity window.
3) **Join/equality only on invariants.** Equality checks and joins across spaces **MUST** target invariant forms (the **≡_UNM** quotient or a declared **Normalization‑fixed** representation), never raw un‑fixed coordinates.

##### 5.1.7 Metric discipline & calibration (Normative)

Use the **weakest safe structure** required by the argument (pre‑order → semi‑metric → metric). 
* **If a distance overlay is declared**, any acceptance predicate or KPI defined over a CharacteristicSpace **SHALL be non‑expansive** (Lipschitz ≤ 1) w.r.t. the published `d` on the **declared domain** (raw coordinates or NCVs, as specified), or else state an explicit margin that absorbs any expansion.
* **If only an order overlay is declared**, any acceptance predicate/KPI **SHALL be isotone** w.r.t. the declared product order.

*Minimal obligations:*
1) **Publish the metric (if used).** If a distance overlay is used, the space **MUST** publish the distance function `d` (including any weights/parameters) and its declared domain of applicability.
2) **Bound expansion.** Any acceptance predicate/KPI that relies on `d` **MUST** be shown **non‑expansive** (Lipschitz ≤ 1); otherwise an explicit **expansion bound** and compensating **margin** **MUST** be stated.
3) **State error & commutation.** If a metric is used together with **NormalizationFix**, the specification **MUST** state (a) the maximum tolerated measurement/calibration error and (b) whether `d` **commutes** with the **NormalizationFix** (or provide a disclaimer and additional guard if it does not).

#### 5.2 State Spaces & Comparability

> **Memory hook:** _We compare **only what lies in the same space** (or is translated into a common space via a declared mapping), and we only certify a holon’s **state** based on **observable coordinates** in that space (using a defined checklist). Anything else is just storytelling._

To make state-space reasoning practical across different contexts and models, this section provides the key **operators and criteria** related to CharacteristicSpaces:

1.  **Space operations** – how to derive a **Subspace**, establish an **Embedding**, or form a **Product** of spaces. These enable us to restrict a space to fewer slots, to map one space into another (with unit conversions, etc.), or to combine spaces (e.g. for composite models).
    
2.  **Comparability regimes** – two allowable ways to compare states: (a) **coordinatewise**, which requires strict sameness of space and units; or (b) **normalization-based**, which uses declared transformations to reconcile differences. We define when each applies and how to apply it properly.
    
3.  **RSG integration** – how formal **state certification** (via checklists in a Role’s state graph) ties into the CharacteristicSpace: ensuring that whenever we declare a system “Ready” or “Degraded”, it’s based on snapshot coordinates in a space. We also outline how to push or pull state definitions along space embeddings (so different contexts can translate states).
    
4.  **Archetypal examples** – “worked mini-schemas” illustrating typical usage in complementary CN‑frames (Operational, Assurance, Alignment). These examples show minimal models mixing entity and relational slots, how data might be structured, and how cross-context alignment works in practice.
    

> **Terminology note:** We often denote a CharacteristicSpace abstractly as **CS**. Formally, one can describe a CS as a tuple `⟨I, basis⟩` where _I_ is the index set of slots and _basis_ is the set (or ordered list) of `slot_i` pairs. When a CharacteristicSpace is attached to a specific **Role** in a specific **Context** (see A.2, A.2.5), we may call it an **RCS** (Role CharacteristicSpace) – essentially the state space for that role’s state machine within that bounded context. Individual **states** of a role live in an RSG (RoleStateGraph, A.2.5), and a **StateAssertion** is a certified claim that at a given time window, the holon’s RCS coordinates satisfy the checklist for a particular state.

##### 5.2.1 · CS Operators (notation-neutral, context-local)

To support model composition, we define operations on CharacteristicSpaces in a notation-independent way (so these can be implemented in any tooling or notation). All these operations are assumed to occur **within a single context** (within one `U.BoundedContext`) unless otherwise noted:

**5.2.1.1 Subspace –** **Projection** `π_S : CS → CS|_S`.  
Given a CharacteristicSpace CS with basis _I_ (slots) and a chosen subset of slot indices $S \subseteq I$, one can form the **subspace** $CS|_S$ which includes only the slots in _S_ and omits all others. The projection map `π_S` takes any state _x_ in the original space and **projects** it onto the coordinates indexed by _S_, effectively discarding the other coordinates. This operation is straightforward: if $S = \{i_1, i_2, ...\}$, then $CS|_S$ has those slots, and any state in $CS|_S$ corresponds to a state in CS with the other coordinates ignored. 
**Properties:** Projection is **idempotent** (`π_S ∘ π_S = π_S`) and, if an order or other structure is defined solely on the subspace’s slots, `π_S` preserves that structure (e.g. it will reflect any order that depends only on slots in _S_).

**5.2.1.2 Embedding –** **Injection** `ι : CS₁ ↪ CS₂`.  
An **embedding** is a structure-preserving **injection** from one space CS₁ into another space CS₂. It consists of two parts: (a) a mapping of slots from CS₁ to slots of CS₂, and (b) for each such slot, a **NormalizationMethod** (function that translates coordinates from CS₁’s scale into CS₂’s scale when the scales or units differ). Formally, let CS₁ have basis _I₁_ and CS₂ have _I₂_. An embedding defines an injective function _m: I₁ → I₂_ that identifies each slot of CS₁ with a corresponding slot in CS₂. For each slot _i ∈ I₁_, where its scale or unit differs from the target _m(i)_ in CS₂, we provide a **NormalizationMethod** function $n_i: Dom(slot_i) → Dom(m(i))$ that yields an **NCV** in the target domain, is **monotone** and respects the scale types (e.g., converting degrees Fahrenheit to degrees Celsius, or mapping one ordinal ranking to another). Intuitively, an embedding says: “Any coordinate tuple from CS₁ can be interpreted as a coordinate tuple in CS₂, possibly after converting units or re‑scaling, and without losing any information except what the declared **NormalizationMethods** intentionally **coarse‑grain**.” If there is no loss at all (**NormalizationMethods** are identity or strict conversions), the embedding is essentially an inclusion of one space into a larger one; if there is some information loss (e.g., converting a fine‑grained scale to a coarse one), that loss is explicit in the **NormalizationMethodDescription**. **Locality:** Embeddings are defined **within a single `U.BoundedContext`** (i.e., both CS₁ and CS₂ are in the same context). Using an embedding across contexts requires an **Alignment Bridge** (see F.9) with an associated congruence‑loss policy.  **Normalization declaration duties (MUST):** Each NormalizationMethod **MUST** (i) state **monotonicity** w.r.t. the slot’s polarity; (ii) publish a **validity window** (value range and time applicability); and (iii) identify its NormalizationMethod class (ratio:scale / interval:affine / ordinal:monotone / nominal:categorical / tabular:LUT(+uncertainty)). **NormalizationMethods** used in enactment gates **MUST** be current; expired editions require renewal or an explicit Waiver (see C.16). In other words, you cannot assume one context’s space fits into another’s without an explicit Bridge; any attempt to do so must treat it as a cross‑context alignment with potential loss.

**Method‑class note.** For **ratio** scales use positive‑scalar conversions; for **interval** scales use **affine** transforms; for **ordinal** scales use **order‑preserving** monotone maps; for **nominal** scales use **categorical** re‑maps; LUT with uncertainty may be used where declared with evidence.

**5.2.1.3 Product –** **Combination** `CS₁ ⊗ CS₂ = CS⊗`.  
The **product** of two spaces CS₁ and CS₂ is a new space **CS⊗** that effectively contains all slots of CS₁ and all slots of CS₂. If CS₁ has index set _I₁_ and basis slots {slot₁…} and CS₂ has _I₂_, then $CS⊗$ has index set $I\_⊗ = I₁ ⊎ I₂$ (disjoint union) with each slot’s definition carried over from its original space. In practical terms, any state in the product space is a pair _(x₁, x₂)_ where _x₁_ is a state of CS₁ and _x₂_ is a state of CS₂ (assuming the two spaces pertain to possibly different aspects or roles). **Use cases:** Product spaces allow modeling **multi-role scenarios** or bundling an entity’s state with some environmental or contextual state. For example, one might take a space of internal capability metrics and ⊗ with a space of external conditions to form a combined space for “readiness under conditions.” **Note:** When combining scores or coordinates from a product space, one must be mindful of scale incommensurability. Cross‑slot aggregation **SHALL** proceed only via a declared **Γ‑fold** (B.1) and, where needed, explicitly declared **NormalizationMethods**; naïve arithmetic is forbidden. The product operation itself doesn’t perform any aggregation; it only sets the stage.

##### 5.2.2 · Comparability of **States** (two admissible regimes)

A **state label** like "Ready", "Authorized", "Degraded", etc., in an RSG is an intensional category (defined by a checklist of conditions – see A.2.5). Determining whether the **states of two holons** are comparable (e.g. whether one is “better” or “worse” than the other in some multi-criteria sense) depends on **where** their state coordinates live and **how** we map those coordinates to a common basis. There are two admissible comparability regimes in FPF:

###### 5.2.2.1 Coordinatewise comparability (`≼_coord`)

Two states can be compared **coordinatewise** only under strict conditions. Essentially, we require the states to be expressed in the **same measurement space**, with the **same units and scales**, and using the **same state definitions**. Formally, coordinatewise comparison is allowed **only if all of the following hold**:

-   **Same space.** The two holders’ state snapshots lie in the **exact same CharacteristicSpace** (and, if relevant, the same RCS attached to a Role in a given Context). It’s not enough that they have similarly named characteristics; they must share the actual defined space (same slots with same definitions).
    
-   **Scale congruence.** For each slot being compared, the scale type, unit, and polarity orientation are **identical**. For example, if comparing temperature readings, both must be on the same scale (say, °C on a ratio scale with “higher = hotter” orientation). No unit mismatches or differing interpretations can be present.
    
-   **State-definition congruence.** The states or status labels themselves must be defined in terms of the **same checklist criteria applied in the same space**. In other words, if we are comparing whether one system is “Ready” and another is “Ready”, both instances of “Ready” must derive from the same formal definition (same thresholds, same checklist logic) over those coordinates. If one context’s "Ready" means something different, you cannot assume they correspond.
    
When these conditions are met, one can define a **coordinatewise preorder** over states. Common patterns include:

- **Dominance:** For a given set of “higher is better” slots, we say state *x* **≼<sub>coord</sub>** state *y* if and only if for *every relevant slot a*, the coordinate $a(x) \le a(y)$ (**after orienting all slots to the declared polarity for that slot**). In other words, *y* is as good or better on all enforced criteria. This defines a Pareto-like ordering (often partial, not total).

-   **Threshold band inclusion:** If states are defined by meeting certain thresholds (e.g. State _Y_ means all metrics above specific levels), then we might say _x_ **≼<sub>coord</sub>** _y_ if _x_ meets every threshold that defines _y_’s state. For instance, if state _y_ = “High Performance” requires speed > 100 and accuracy > 90%, then _x_ is “no less than y” if _x_ also exceeds those thresholds.
    
By default, **no comparability** is assumed unless proven. If any of the above congruence conditions fails, one must **not** fall back to ad-hoc comparisons (like matching by name or normalizing without declaration). Either switch to a **normalization-based regime** or declare the states **incomparable**.

###### 5.2.2.2 Normalization‑based comparability (`≼_normalization`)

When two state vectors do not meet the strict conditions for coordinatewise comparison (e.g. they come from different spaces, or same conceptual Characteristics but measured on different scales/units, or defined in different contexts), the only sanctioned way to compare them is via a **NormalizationMethod‑based mapping under UNM** into a common space. The idea is: **normalize, then compare**. Specifically:

If we have state _x_ in space CS₁ and state _y_ in space CS₂ (possibly the same space, possibly not), and if direct coordinatewise comparison is not valid, we must introduce a set of **per‑slot NormalizationMethods** to translate one state’s coordinates into the frame of the other. A **NormalizationMethod** `m_a: Dom(a_src) → Dom(a_tgt)` is a monotonic transformation (non‑decreasing w.r.t. the declared polarity) that converts values from the source slot’s domain to the target slot’s domain and yields an **NCV** in the target domain. Each method is tailored to its Characteristic/Scale pair and respects the scale types (e.g., **positive‑scalar** conversion for ratio scales, **affine** conversion for interval scales, an **order‑preserving** mapping for ordinal scales, or a **categorical** re‑mapping for nominal scales). Collectively, a set of methods {m_a} for all slots forms a **vector‑level normalization function** `N: CS₁ → CS₂` that lands **within the same ≡_UNM class** of charts in the target Context.

**Comparability rule (normalize‑then‑compare).** We say _x_ **≼<sub>normalization</sub>** _y_ if, after applying the normalization **function** `N` to _x_ to translate it into space CS₂, the resulting point **N(x)** (a vector of **NCVs**) is **≼<sub>coord</sub>** _y_ in the target space. In other words, we don’t compare _x_ and _y_ directly; we compare **N(x)** to _y_, where both are now expressed in the **same** space (CS₂) with the same units and definitions. Normalization‑based comparison thus reduces to the coordinatewise case _after_ a transformation.

If the normalization crosses context boundaries (i.e., CS₁ and CS₂ are in different bounded contexts), then by FPF policy this mapping must be treated as a formal **Bridge** alignment with an associated **congruence‑loss (CL)** level. In such cases, any conclusions drawn carry an **assurance penalty**: the confidence in comparability is discounted according to the worst-case loss of meaning along the mapping. (See also B.3’s `Φ(CL)` rule for how a CL penalty factors into trustworthiness scores.)

**Auditability.** Each NormalizationMethod should be fully specified and transparent. At minimum, one should document the functional form or mapping table being used and the intended domain of validity (**NormalizationMethodDescription**). In the measurement architheory (C.16), normalization comes with calibration evidence/rationale and a note of its valid range or conditions. (For example, a method translating lab scores to field scores might note it’s valid only for a certain operating range.) While A.19 does not require recording these details, it assumes that such **evidence and bounds** are handled by the measurement framework (MM‑CHR) outside the core space definition. The key here is that **no comparison is magic** – if values differ in scale or context, a declared monotonic transformation must bridge them, and its limitations should be known.

> **Mnemonic:** _“Never compare before you **land** both points in the **same** well-typed space.”_ In other words, always map measurements to a common basis (same CharacteristicSpace and units) before attempting to say one state is ≥ or ≤ another. Directly comparing raw numbers from different scales or contexts is not allowed.

##### 5.2.3 · RSG touch-points — **State certification via CS**

To connect the abstract concept of a **space of metrics** with the operational concept of **states** (like “Ready” or “Degraded”) in a Role’s lifecycle, we introduce a **certifier** function that evaluates state predicates against coordinates: 

certify(Role, Context): Snapshot( RCS[Role,Context], Window )  ──→  {StateAssertion}

This is a conceptual sketch: given a **snapshot** of all relevant coordinates for a Role (in its RCS) over some time window, the certifier produces a set of **StateAssertions** that are deemed true in that window. Each StateAssertion claims that the holder is in a particular state (e.g. “Ready”) during the window, backed by evidence.

**5.2.3.1 From CS snapshot to StateAssertion (design → run).** Each possible state _s_ in a Role’s RSG has an associated **Checklist** _(s)_ – a design-time artifact (see A.2.5 §8.1) which is a predicate defined over the RCS’s coordinates (and possibly other contextual observables). For example, a state “Degraded” might have a checklist like “\[temperature < 50 °C\] AND \[pressure > 5 bar\] for 10 minutes”. When the system is running, we take an **Observation** of the current coordinates (a snapshot of the RCS at a given time or over a time window) and evaluate the checklist. A **StateAssertion**(holder, _s_, Window) is then a record that the checklist for state _s_ has been satisfied by the observed data in that interval. In other words, it’s a certified evaluation that “state _s_ holds true for this holon at this time.” Only observable, measurable facts go into these predicates (no subjective judgments), and each assertion is traceable to the specific evidence (observations) that support it. The Role’s **Green-Gate Law** (A.2.5 §8.4) then says that a Role can proceed with an enactment (e.g. performing work) if and only if there is a **StateAssertion** showing the holon to be in an **enactable** state at that time. This connects measurement to action: you can only act if you have evidence you’re in the right state to act. 
**Evidence kind & window.** Every StateAssertion **SHALL** record `evidence_kind ∈ {observation, prediction}`, the **window** `[t_from, t_to]`, and, if `prediction`, the **horizon Δt** relative to the observation base. Use of `prediction` in enactment gates is permitted **only** under the DYN/TIME constraints captured in **CC‑A19.17–A19.18**; otherwise a **fresh observation** is required.

**5.2.3.2 Translating state definitions across embeddings.** If we have an **embedding** ι: RCS₁ ↪ RCS₂ (for example, RCS₁ is a subspace or a different version of RCS₂), we might want to reuse or compare state definitions between the two. There are two directions to consider:
* **Pulling a checklist** (reuse state criteria from a larger space in a smaller space): Given a checklist defined on RCS₂ (the larger or target space), we can **pull it back** via the normalization map **N** of the embedding to get a predicate on RCS₁. This derived checklist (**Checklist₂ ∘ N**) lets us apply the RCS₂’s state definition to a holon that only has RCS₁ measurements. This is useful when a consumer context wants to evaluate whether a producer (with fewer characteristics or different units) meets the consumer’s state definitions. Essentially, the consumer asks: “If I map the producer’s metrics into my space, does it satisfy my state criteria _s_?”
 * **Pushing an assertion** (honor a producer’s certified state in a larger space): If a holon has a StateAssertion for state s’ in RCS₁, can we treat it as evidence for state s in RCS₂? This is only valid under a strict condition: the checklist for state s in the larger space, when composed with the normalization mapping **N**, must logically imply the checklist s’ in the smaller space (or vice versa, depending on which state corresponds to which). In practice, this often requires a proof of refinement: that meeting state s (in big space) guarantees state s’ (in small space), or that state s’ (in small) is sufficient for state s (in big space) given the normalization translations. If that condition is met (or a policy waiver is granted in lieu of proof), then an assertion in the smaller space can be **pushed up** to count as an assertion in the larger space. This mechanism allows, for example, a component’s certified state to satisfy a system-level state requirement, provided the relationship is formally established.
  
**5.2.3.3 Certification interface (pointer).** Operational interface examples and minimal data stubs are **informative** and live in **A.19.D1** (“Certification Interface Example”). Pattern A.19 only constrains **conceptual** obligations; no storage/ID scheme is mandated here.
  
_(In summary, embeddings not only allow numeric comparability, but also allow **state definitions** and **certifications** to be systematically translated between contexts, ensuring consistency in how we interpret “Ready”, “Failed”, etc., across different models.)_

##### 5.2.4 · Cross-context comparability & assurance hooks

When comparing states or metrics **across different bounded contexts** (different “context of meaning”), additional rules apply to maintain semantic integrity:

-   **5.2.4.1 Direction & loss (Bridges).** Suppose we want to claim that “Holon X in Context B is in state _Ready_ as defined in Context A.” This requires an explicit **Alignment Bridge** declaration that maps the RCS of _(Role, Context B)_ to the RCS of _(Role, Context A)_ (or maps State B to State A). Such a Bridge (see F.9) will specify the correspondence of Characteristics (and the necessary **NormalizationMethods under UNM**) and a **congruence‑loss (CL)** level indicating how much fidelity is lost in translation. Critically, these Bridges are **one-directional** mappings unless explicitly made bidirectional. Just because we can interpret B’s state as an A-state does not mean we can go the other way without another mapping. The Bridge makes the mapping and any loss explicit. Without a declared Bridge, cross-context state comparisons or substitutions are not valid – there is no implicit global state space. The statement above, for instance, would only hold if we have something like “Bridge B→A (with defined NormalizationMethods) such that X@B can be viewed in A’s terms.” The **direction matters**: “B satisfies A’s Ready” does **not** imply the converse unless another bridge (A→B) is defined.
    
-   **5.2.4.2 Confidence penalties for mapped comparisons.** Whenever a **normalization-based comparison** crosses Contexts (via a Bridge), assurance **MUST** apply the penalty **Φ(CL)** as **defined in B.3** (CL is **ordinal** there). For episteme‑specific compositions, **B.1.3** instantiates the same policy. This pattern does **not** restate the scale or Φ; it defers to **B.3**. For example, a safety argument that relies on a cross-context comparison might need to downgrade its certainty or include an extra safety margin.  This penalty **MUST** be declared as part of the assurance argument for the comparison (stating the Bridge used and its CL), so that the Φ(CL) discount can be reasoned and applied. No implementation‑level storage format or identifier is mandated by this pattern.
    
-   **5.2.4.3 Declare “incomparable” when appropriate.** If for some critical Characteristic there is **no valid NormalizationMethod** to translate measurements between two contexts (e.g. the scale types are fundamentally different, or the measurement’s meaning doesn’t carry over), then the framework insists that we declare the states or metrics **incomparable** rather than attempting any fudge. No comparison should ever default to “close enough by name” or other heuristics. For instance, if one context measures “User Satisfaction” qualitatively and another quantitatively, and no monotonic mapping can be justified, one must simply say a user satisfaction state in context A cannot be compared to one in context B. Mark it incomparable and avoid any misleading conclusions. This rule guards against the natural temptation to compare things just because they have the same label or general intent, when in fact their measurement basis is different.

##### 5.2.5 Certification pipeline (Minimal, Normative)

Canonical evaluation chain (notation‑neutral):

`raw coords → Normalize (UNM.NormalizationMethod) → Quotient / NormalizationFix → (optional) Indicatorization (via IndicatorChoicePolicy) → (optional) Order/Distance overlay → Evaluate Checklist → StateAssertion → Green‑Gate`

**Strict distinction.** Steps may be **co‑implemented**, but are **logically distinct** and **MUST** be referenceable in assertions (**NormalizationMethod/UNM** name or formula, overlay kind). A gate is **invalid** if any required step lacks a current, valid referent (e.g., expired **NormalizationMethod** edition).

### 5.3 Operator library (notation‑neutral)

**Spaces:** `Sub` (projection), `Emb` (embedding), `Prod` (product), `Quot` (quotient by declared equivalence), `NormalizationFix` (fix to a named chart/edition).

**States/criteria transport:** `Pull` (pull checklist via embedding/NormalizationMethod), `Push` (push assertion along embedding with proof/waiver), `Indicatorize` (apply **IndicatorChoicePolicy** to select Indicators), `Align_B` (cross‑context alignment via Bridge with CL), `Fold_Γ` (admissible aggregation/accumulation per B.1, with WLNK/MONO constraints).

**OP‑1 (Normative).** If `Align_B` is used in **gating**, the **Bridge used** and its **CL** **MUST** be declared in the assurance argument; the corresponding Φ(CL) penalty is applied per B.3. Silent cross‑context reuse is forbidden. (A.19 does not mandate any storage/ID scheme.)

### 6 · Conformance Checklist (normative) — **CC‑A19**

**Formality anchors & operational segregation (normative).** A.19 aligns with **C.2.3 Unified Formality Characteristic (F)**. The legacy tier labels **T0/T1/T2 are deprecated**; speak **F** directly and treat operations separately (see **E.10** for registers).
— **F-Surface (recommended F ≥ F3).** Obligations are **declarability** and **arguability**: the author can **name** the CharacteristicSpace (basis/slots as *(Characteristic, Scale)* pairs), **state** the comparability regime (coordinatewise or normalization-based), and **express** a state’s checklist in observable coordinates. No storage formats, IDs, or operational provenance are required.
— **F-Predicates (F ≥ F4 when predicate-like).** As above, plus **explicit slot/NormalizationMethod names** and **stated overlays** (order/metric). When acceptance conditions are written as **typed predicates over coordinates**, declare **F ≥ F4**. Remains **notation-neutral** and **storage-agnostic**.
— **Operational bindings (not part of F).** When automatic checking/assurance is required, use **A.19.D1 / C.16 / B.3** for IDs, validity windows, waivers, and logs. These raise **R/TA** in the trust calculus and **do not change F** unless the **expression form** changes (see C.2.3 orthogonality).

The following checklist summarizes the normative requirements introduced by Pattern A.19. An implementation or model **conforms** to A.19 if and only if all these conditions are met:

**Spaces & mappings**  
**CC‑A19.1.** Any defined **Subspace**, **Embedding**, or **Product** of CharacteristicSpaces **MUST** explicitly list the involved slots and their metadata (scale type, unit, polarity). No comparability or merging is allowed purely by matching names or assuming correspondence – it must be declared.  
**CC‑A19.2.** Every **Embedding** `ι: CS₁ ↦ CS₂` **MUST** provide a well‑defined **NormalizationMethod** for each slot where `CS₁`’s slot differs in scale/unit from `CS₂`’s. Each method **MUST** (a) be **monotonic** w.r.t. the declared polarity and scale type; (b) publish a **validity window** (value range and time applicability); and (c) name its method class (affine / order‑preserving / LUT). (Identity suffices where scales are identical.)
**CC‑A19.2a.** **Scale‑class guard.** Ratio conversions **SHALL** be positive‑scalar; interval conversions **SHALL** be affine; ordinal conversions **SHALL** be order‑preserving; nominal conversions **SHALL** be categorical re‑maps; LUT with uncertainty **MAY** be used where declared with evidence.

**Comparability**  
**CC‑A19.3.** **Coordinatewise comparability** (`≼_coord`) is **permitted only** when the states being compared share the **same CharacteristicSpace**, with **identical scale metadata** on each compared slot, and using the **same state definition criteria**. If these conditions aren’t fully satisfied, an implementation **MUST NOT** attempt direct coordinatewise comparison; it should either apply a **normalization‑based** method or report the items as **incomparable**.
**CC‑A19.3a.** Use of **Indicators** in any checklist/assertion **MUST** cite an **IndicatorChoicePolicy** (edition). Treating any **NCV** as an Indicator **without** a declared policy is **forbidden**.

**CC‑A19.4.** **Normalization‑based comparability** (`≼_normalization`) **MUST** be done by first normalizing all relevant coordinates of the source state into the target state’s space via the declared **NormalizationMethods**, and **only then** comparing in that common space. In other words, two states can be compared under `≼_normalization` only by producing an image of one in the other’s space (`G(x)`) and using `≼_coord` on the result. Each NormalizationMethod **MUST** be explicitly defined (no implicit or “on the fly” conversions).  
**CC‑A19.5.** Any cross-context state comparison or substitution **MUST** cite a corresponding **Alignment Bridge** (F.9) with an explicit **CL (congruence-loss) level**. If such a Bridge is used in an assurance or decision-making context, the model **MUST** apply the appropriate confidence reduction (`Φ(CL)` penalty per B.3) to reflect the loss. Cross-context comparisons without a Bridge (i.e. assuming equivalence by name or convention) are **forbidden**.

**Certification & enactment**  
**CC‑A19.6.** Every **StateAssertion** **MUST** identify at least: the specific **state** being asserted (by name), the associated **checklist** or criteria set (by name), and the observation **window**. Furthermore, if the evaluation involved cross‑space mapping, it **MUST** **declare** which **NormalizationMethod(s)** or **Bridge** were applied. This ensures the decision can be examined in review; A.19 does not mandate any storage/ID scheme.

**CC‑A19.7.** The **Green-Gate enactment rule** (A.2.5) **SHALL** be enforced: a transformative action (`U.Work`) by a RoleAssignment is only allowed if there exists a **contemporaneous** StateAssertion showing the holon in a state that is marked **enactable**. If a StateAssertion has been translated from another context or space, it is valid for gating **only** if it was obtained through declared Embeddings/Bridges (no untracked inferences). This ensures no work is done under an unverified or mis-mapped state condition.  
**CC‑A19.8.** All **Checklist** definitions for states **MUST** be formulated in terms of **observable predicates** on the RCS (and known context events) – no hidden workflows or implicit time sequencing inside a checklist. A checklist should read like a static predicate (even if it’s about a duration of some condition). If temporal order or multi-step processes are involved in achieving a state, those must be modeled via explicit **Methods/Work** or via an aggregation logic (e.g., using the Γ (Gamma) patterns in B.1 for process sequencing), rather than being baked into the state’s definition. **Use of Indicators in any checklist MUST cite an IndicatorChoicePolicy edition; treating any NCV as an Indicator without policy is forbidden.**

**Anti‑drift**  
**CC‑A19.9.** If a **NormalizationMethod/UNM** or a **state checklist** is updated or calibrated differently in a new version, previous StateAssertions **MUST NOT** be retroactively modified. One must close out or mark the old assertions with their valid time window and start issuing new assertions under the updated definitions. In other words, historical records remain as they were (tied to the definitions at that time), and any change in criteria results in a _new context or version_ for future assertions. This prevents retroactive truth-changing and maintains integrity of historical data.  
**CC‑A19.10.** If any **critical slot** in a comparison lacks a defensible monotonic **NormalizationMethod** (meaning you cannot find any reasonable way to translate that characteristic between two spaces without excessive loss or ambiguity), then the comparison **MUST** be reported as **incomparable**. The system should not attempt any unofficial workaround (like simply comparing whatever is available or ignoring that dimension). This rule applies even if all other slots have gauges – one missing or irreconcilable aspect is enough to force an “incomparable” verdict, unless the decision-makers explicitly accept a loss via a Bridge with stated limitations.

**Quotients & Normalization‑fix (QNT)**
**CC‑A19.11.** Equality checks and joins across spaces **MUST** target invariant forms (on a **quotient** or declared **NormalizationFixed** chart), not raw coordinates.
**CC‑A19.12.** If a checklist predicates on a normalization‑variant property, it **MUST** name the **NormalizationFix** (which UNM.NormalizationMethod or chart is assumed).
**CC‑A19.13.** All used **NormalizationMethod** classes (affine / monotone / LUT…) **MUST** be named in the bounded context’s glossary.

**Metric discipline & calibration (MET)**
**CC‑A19.14.** If a distance overlay is used, acceptance predicates/KPIs over a CS **SHALL** be **non‑expansive** (Lipschitz ≤ 1) w.r.t. the published `d` on the declared domain (raw coordinates or NCVs), or declare a compensating margin; otherwise they **SHALL** be isotone w.r.t. the declared product order.
**CC‑A19.15.** Any distance used in state/acceptance checks **MUST** carry max tolerated error and, where claimed, a **Lipschitz bound** for the **NormalizationMethod** composition in use.
**CC‑A19.16.** Cross‑CN‑frame inputs **SHALL** name the **normalization transform** and its **validity window**; expired transforms are invalid for gating unless waived explicitly.

**Dynamics & time (DYN/TIME)**
**CC‑A19.17.** Every temporal guard **MUST** specify the window `[t_from, t_to]` and `evidence_kind ∈ {observation, prediction}`; if `prediction` is used for gating, the conditions in **§ 5.2.3.1 (Evidence kind & window)** **MUST** hold.
**CC‑A19.18.** Any dynamics map `Φ_{Δt}` used in comparison/gating **MUST** be **non‑expansive** (Lipschitz ≤ 1) under the declared distance overlay **and** commute with **NormalizationFix**; otherwise **observation** is required.

**Certification (CERT)**
**CC‑A19.19.** StateAssertions **MUST** **state** the current **NormalizationMethod/UNM** and overlay artifacts used (by name or formula) and the `evidence_kind`; assertions relying on **expired** NormalizationMethod/UNM are **invalid** for gating unless an explicit **Waiver SpeechAct** is **declared** per policy. (A.19 imposes no requirement on IDs or storage.)
**CC‑A19.20.** The certification pipeline steps (**Normalize (UNM.NormalizationMethod); Quot/Fix_normalization; overlay; evaluate; assert**) are **logically distinct** and **MUST** be reconstructable in argument/review; collapsing steps without clearly stated referents violates A.19. (No specific persistence format is implied.)

**Operators (OP)**
**CC‑A19.21.** Use of `Align_B` in gating **MUST** **declare** the **Bridge** used and propagate **CL** into assurance (B.3). Cross‑context comparison without a Bridge is **forbidden**. (No requirement to store an ID is imposed by A.19.)

### 7 · Anti‑patterns → safe rewrites

_The following are common modeling mistakes (“anti-patterns”) related to measurement spaces, and how to correct them:_

-   **“Same label ⇒ comparable.”**  
    ✗ _Assuming_ **Ready@contextA ≥ Ready@contextB** _just because both states are called "Ready"._  
	✓ **Explicitly normalize and bridge contexts:** Define an Alignment **Bridge (B→A)** and appropriate **NormalizationMethods** for the underlying metrics. Then compare by first translating one state’s coordinates (compute **N(x)** as NCVs in the target space) and using `≼_coord` on the result.
    
-   **“Compare before landing.”**  
    ✗ Comparing values directly across different scales, e.g. _Drift\_A = 5°C vs Drift\_B = 5°F_ as if they were the same.  
	✓ **Normalize to common units first:** e.g., apply the Fahrenheit‑to‑Celsius **NormalizationMethod** _m_(T_F) = (T_F − 32) × 5/9 to convert all data to °C, **then** compare the drift values. Always **normalize into one space** before comparing magnitudes.
    
-   **“Checklist = workflow.”**  
    ✗ Defining a state’s checklist with an implied sequence: _“State ‘Ready’ requires doing Step 1 then Step 2…”_  
    ✓ **Keep checklists declarative:** A **Checklist** should represent a state of the system (a condition) – essentially **state evidence** – not a sequence of actions. If order or process matters, model that explicitly via a **MethodDescription** or by using a **Γ** (Gamma) aggregator for process logic. In other words, state = “Ready” might require conditions A and B to be true (regardless of how you got there), whereas the procedure to get ready (do Step1 then Step2) should be a separate method or playbook.
    
-   **“Retro-fix past assertions.”**  
    ✗ Going back to edit or reinterpret old StateAssertions after changing a threshold or gauge (e.g. “We updated the criteria, let’s ‘fix’ last quarter’s records to match”).  
    ✓ **Never alter historical assertions:** **Leave history as‑is.** If criteria change, issue new assertions under the new criteria going forward, and if needed, explicitly **version** the **NormalizationMethod/UNM** or checklist. Past assertions remain valid for the old version and their time; new ones apply henceforth. This ensures auditability and avoids erasing or rewriting what was true under earlier standards.


---

## A.19.D1 — CN‑frame (comparability & normalization) \[D]

> **Scope.** This CN‑frame Algebra & Normalization Discipline **extends A.19** by fixing the **governance Standard** for CN‑frames, defining a **conformance checklist** and **regression harness**, and providing **didactic one‑pagers** and **anti‑patterns** so teams can introduce CN‑frames without tool lock‑in. The mandatory pattern structure and authoring discipline from **Part E** (Style Guide, Tell‑Show‑Show, checklists, DRR, guard‑rails) are applied throughout.

### 1 · Context

A.19 established a substrate‑neutral picture:

* a **CN‑frame** = *(Context‑local)* **CharacteristicSpace (CS)** + **chart** (coordinate patch + units) + **UNM/Normalization** (admissible re‑parameterizations that preserve meaning and generate **≡_UNM** over charts);
* **operators** (subspace, product, pullback/pushforward) and **comparability** (coordinatewise vs **normalization‑based (normalize‑then‑compare)**);
* **RSG touch‑points**: role readiness (**RSG** states) are **certified** against CS via **checklists** over observable characteristics;
* **entity/relational mixtures** across CN‑frames via minimal schemas and bridges.

**Terminology guard.** *CN‑frame* is the **lens** (I); *CN‑Spec* is the **governance card** (S) that fixes admissible charts/**normalizations**/comparability/Γ‑fold for that lens **in one `U.BoundedContext`**; *CN‑Description* is the didactic surface (D) with worked examples and anti‑patterns.

**Lexical guard (map/Map).** Lowercase **map** is a mathematical function; capitalized **Map** (e.g., `DescriptorMap`) is a Part‑G method type (encoder) and is **not** a NormalizationMethod or NormalizationMethodInstance.

A.19.D1 makes this *operational and auditable*.

### 2 · Problem

Absent a governance layer, four failure modes recur:

1. **Chartless numbers.** Measures move between teams without units, reference states, or declared normalization → **illusory comparability**.
2. **Hidden normalization flips.** Re‑parameterisations (e.g., normalising by batch size) silently alter meaning; trend lines lie.
3. **CN‑frame sprawl.** Every initiative mints a new “dashboard dimension”; semantics diverge; assurance collapses.
4. **Un‑bridgeable reports.** Cross‑team roll‑ups average **incongruent** CN‑frames, violating the **weakest‑link (WLNK)** discipline from Γ and B.3.

### 3 · Forces

| Force                         | Tension we must balance                                                              |
| ----------------------------- | ------------------------------------------------------------------------------------ |
| **Universality vs nuance**    | One Standard for robotics, safety, finance — yet leave each context’s idioms intact. |
| **Speed vs audit**            | Light ceremony for on‑ramp; hard guarantees for assurance and SoD.                   |
| **Local truth vs federation** | Keep CN‑frames meaning‑local; still enable **explicit** bridging across Contexts.          |
| **Minimalism vs safety**      | Few mandatory slots; enough structure to forbid silent gauge drift.                  |

---

### 4 · Solution — **The CN‑Spec** (CN‑Spec) + **Registry** + **Bridges**

#### 4.1 The **CN‑Spec** (comparability & normalization specification per CN‑frame, in one `U.BoundedContext`)

A **CN‑frame** is governed by a compact, notation‑free card:

```
CN‑Spec {
  name              : CN‑frameName                  // local to Context
  context           : U.BoundedContext              // edition/version included
  cs_basis          : [{
    slot_id         : <tech-token>,                 // stable slot id (basis name)
    characteristic  : <U.Characteristic>,          // per A.17 / A.18
    scale           : { type: nominal|ordinal|interval|ratio, unit?: <U.Unit>, bounds?: <...> },
    polarity        : up|down|target-range,        // comparison orientation
    // if needed: missingness?, admissible_domain? (MM‑CHR‑consistent metadata)
  }]
  chart             : { reference_state, coordinate_patch, measurement_protocol_ref }
  normalization     : { UNM_id?, methods: [NormalizationMethodId], instances?: [NormalizationMethodInstanceId], invariants, admissible_reparameterizations, method_descriptions: [NormalizationMethodDescriptionRef], fix?: <NormalizationFixSpec> }
  comparability     : { mode ∈ {coordinatewise, normalization-based}, minimal_evidence }
  indicator_policy? : { IndicatorChoicePolicyRef, scope, edition }
  acceptance        : { checklist_for_admission, window, evidence_anchors } // gates RSG state checks
  aggregation       : { Γ_fold, WLNK/COMM/LOC/MONO choices, time_policy }   // safe roll-up recipe
  alignment?        : { bridges_to_other_contexts, CL_levels, loss_notes }  // optional
  lifecycle         : { owner_role, DRR_links, deprecation_plan }
}
```

**Reading:** *A CN‑frame is a context‑local lens with declared characteristics, units, a chart to read them, a **UNM/Normalization** that states what “doesn’t matter,” explicit rules for when a datum counts and how many can be safely folded, and (optionally) an **IndicatorChoicePolicy** to select Indicators. Not every Characteristic (even with an NCV) is an Indicator; Indicators arise from policy.*

`NormalizationKinds`, `MetricSpec` and `QuotientSpec` are **CN‑frame‑level** governance metadata; per **A19‑CS‑5** the kernel `CharacteristicSpace` carries **no NormalizationMethods** or composition; normalization lives in **MM‑CHR**.

**L‑CN‑Spec‑NORM‑IDs**: where stored artifacts are referenced (e.g., in assurance logs), use **NormalizationMethodId**/**NormalizationMethodInstanceId**; avoid generic “map”/“gauge” nouns.

#### 4.2 **CN‑frame Registry** (per Context)

Each `U.BoundedContext` keeps a **CN‑frame Registry** (VR):

* **canonical names** and **editions**;
* **SoD hooks** (who can edit CN‑Spec, who can certify admission);
* **deprecation map** (what replaces what, when).

#### 4.3 **Bridges** (across contexts)

Cross‑context reuse occurs **only** via explicit **Alignment Bridges** (F.9) between CN‑Specs:

```
Bridge CN‑frameA@Context1  →  CN‑frameB@Context2
  CL: {3|2|1|0}
  kept_characteristics: [...]
  lost_characteristics: [...]
  transform: {pullback | pushforward | re-scaling | re-binning}
  extra_guards: {additional evidence / reviewer role / waiver speech-act}
```

**CL policy (reference).** **CL levels and the penalty Φ(CL) are defined in B.3** (CL is **ordinal**; do not average). **Mechanism authors SHALL declare crossings in the `Transport` clause of A.6.1 U.Mechanism; penalties from scope/kind/plane **route to `R/R_eff` only** (never to **F/G**). This CN‑Spec may **add operational guards** per level (e.g., “extra reviewer at CL=1”, “waiver at CL=2”), but it **does not redefine** the scale or Φ. For episteme‑specific frames, see also **B.1.3**.

### 5 · Conformance Checklist (normative)

> **Pass these and your CN‑frames are fit for assurance and cross‑team composition.**

**CC‑A19.D1‑1 (Local scope).** Every CN‑frame **MUST** live inside a declared `U.BoundedContext` (with edition). Names are **local**; same label in another Context ≠ same CN‑frame.

**CC‑A19.D1‑2 (Units & polarity).** Each characteristic in `cs_basis` **MUST** declare **unit/scale** and **polarity** (↑ better / ↓ better / target range). No unlabeled magnitudes.

**CC‑A19.D1‑3 (Chart).** `chart` **MUST** name the **reference state**, **coordinate patch** and **measurement protocol** (`U.MethodDescription`) to make numbers reproducible.

**CC‑A19.D1‑4 (Normalization).** `normalization` **MUST** list the **admissible transforms** (e.g., affine rescale, monotone map) **and** the **invariants** they preserve (what comparability means).

**CC‑A19.D1‑5 (Comparability mode).** `comparability.mode` **MUST** be either **coordinatewise** (same chart & units) or **normalization‑based** (after normalization by the declared **UNM** into the **same ≡_UNM class**). Mixed/implicit modes are prohibited.

**CC‑A19.D1‑6 (Admission checklist).** `acceptance.checklist_for_admission` **MUST** be observable and time‑bounded; each datum admitted to the CN‑frame **SHALL** cite a **StateAssertion** or equivalent `U.Evaluation`.

**CC‑A19.D1‑7 (Aggregation discipline).** `aggregation.Γ_fold` **MUST** specify WLNK/COMM/LOC/MONO choices and the **time policy** (e.g., average of rates vs integral of counts). **No free‑hand averages.**

**CC‑A19.D1‑8 (Bridge‑only reuse).** Cross‑context consumption **MUST** cite a **Bridge** with CL and **loss notes**; coordinate‑by‑name without a Bridge **fails**. If the data participate in **gating/assurance**, apply **Φ(CL) per B.3**; this CN‑Spec does not restate Φ.

**CC‑A19.D1‑9 (SoD & roles).** Editing CN‑Spec and admitting data **MUST** be performed by **different** roles (⊥ enforced): `CN‑frameStewardRole ⊥ CN‑frameCertifierRole` inside the same context.

**CC‑A19.D1‑10 (Lifecycle & DRR).** Every CN‑Spec **MUST** carry an **owner role**, a **deprecation plan**, and links to **DRR** entries for rationale and changes (Part E.9).

**CC‑A19.D1‑11 (Anchors & lanes for comparability).** Any **admission** into a CN‑frame that is later **used for comparison/aggregation** **SHALL** cite the corresponding **A.10 EvidenceRole** anchors for each characteristic, with **assuranceUse lane** tags {TA, VA, LA} and **validity windows** (where applicable), so that the **SCR** can report lane‑separated contributions and freshness (B.3). Absence of anchors for a required characteristic renders items **incomparable**.

**CC‑A19.D1‑12 (Notation independence).** CN‑Spec content **MUST NOT** depend on a tool or file format; semantics precede notation (E.5.2 Notational Independence).

**CC‑A19.D1‑13 (Lexical guard‑rails).** characteristic names and role labels **MUST** follow the Part E lexical discipline (registers, twin labels; no overloaded “process/service/function”).

### 6 · Consequences (informative)

| Benefit                           | Why it matters                                                                                                        |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Auditable comparability**       | Chart + declared normalization (UNM + NormalizationMethods) make “same number” meaningful; silent re‑basings become explicit, reviewable choices.                   |
| **Safe roll‑ups**                 | Γ‑folds with WLNK/COMM/LOC/MONO stop optimistic averaging and preserve invariants.                                    |
| **Pluralism without incoherence** | Bridges with CL and loss notes allow federation without pretending to global sameness.                                |
| **RSG‑ready**                     | Admission checklists let **RSG** states reference **CN‑frame‑backed** facts (e.g., *Ready* requires characteristics within bounds). |

### 7 · Rationale (informative)

The CN‑Spec aligns A.19.D1 with **Part E**: it packages Tell‑Show‑Show, Conformance Checklists, and DRR‑backed change, while honouring **DevOps Lexical Firewall**, **Unidirectional Dependency**, and **Notational Independence** so that semantics never depend on tooling.  It also operationalises B.3 **Trust & Assurance** by making CL penalties and WLNK folds first‑class.

---

### 8 · Archetypal Grounding *(Tell‑Show‑Show)*

> **Same slots, three arenas; no tooling implied.**

#### 8.1 **Industrial line** — *Weld‑quality CN‑frame* (`AssemblyLine_2026`)

* `cs_basis`: *BeadWidth\[mm] (target 6.0±0.2)*, *Porosity\[ppm] (↓)*, *SeamRate\[1/min] (↑ until limit)*
* `chart`: reference jig, fixture ID, torch type; `MethodDescription#Weld_MIG_v3`
* `normalization`: affine rescale on gray‑level calibration → invariant = physical porosity
* `comparability`: **normalization‑based (UNM)** (calibration tables applied)
* `aggregation`: WLNK on quality (min‑bound), COMM on counts, time = per‑shift histograms
* **RSG hook**: `WelderRole.Ready` requires *Porosity ≤ 500 ppm* & *BeadWidth within ±0.2 mm* admitted by this CN‑frame.

#### 8.2 **Software/SRE line** — *Latency CN‑frame* (`SRE_Prod_Cluster_EU_2026`)

* `cs_basis`: *P50Latency\[ms] (↓)*, *P99Latency\[ms] (↓)*, *Load\[req/s]*
* `chart`: client vantage, trace sampler v4; `MethodDescription#HTTP_probe_v4`
* `normalization`: monotone time‑warp compensation for collector skew; invariant = percentile order
* `comparability`: **normalization‑based (UNM)** with declared normalization
* `aggregation`: MONO on latency (max of mins), WLNK across services
* **RSG hook**: `DeployerRole.Active` gated if **P99** < declared SLO over the admission window.

#### 8.3 **Clinical/episteme line** — *Trial‑outcome CN‑frame* (`Cardio_2026`)

* cs_basis:
  - slot_id: ΔBP
    characteristic: BloodPressureChange
    scale: { type: ratio, unit: mmHg }
    polarity: down
  - slot_id: AdverseRate
    characteristic: AdverseEventRate
    scale: { type: ratio, unit: "%" }
    polarity: down
  - slot_id: Age
    characteristic: Age
    scale: { type: ratio, unit: years }
    polarity: neutral
* `chart`: cohort definition; `MethodDescription#TrialProtocol_v5`
* `normalization`: case‑mix adjustment (propensity score); invariant = adjusted ΔBP
* `comparability`: **normalization‑based (UNM)** (post‑adjustment)
* `aggregation`: LOC on subcohorts; WLNK on safety outcomes
* **RSG hook**: `EvidenceRole.Validated` admission requires CN‑frame acceptance; **Assurance** pulls CL from any Bridge used.

#### 8.4 Worked mini-schemas (entity/relational mixtures across CN‑frames, informative)

To illustrate how CharacteristicSpace is used in practice, below are simplified schema snippets for three typical **CN‑frames**: an **Operations** view (run-time state and action gating), an **Assurance** view (evidence and cross-context comparison), and an **Alignment** view (design-time consistency across contexts). These examples mix entity-based and relational Characteristics and demonstrate how state spaces, gauges, and bridges appear in a model. (The notation is mix of a graph/entity diagram and a relational table outline for clarity. **PK** = primary key, **FK** = foreign key.)

**8.4.1 Operations CN‑frame — Run-time gating & enactment**

_Entity graph view:_

Holder (System) ── playsRoleOf ──> Role@Context ── has ──> RCS (slots…)
RSG (Role@Context) ── owns ──> State (◉ status)
Checklist (of State) ── testedBy ──> Evaluation ── yields ──> StateAssertion
Work ── performedBy ──> RoleAssignment
Work ── isExecutionOf ──> MethodDescription

In the above, a **Holder** (a system instance) plays a **Role** in some Context, which has an attached **RCS** (a set of slots defining its characteristic space). That Role’s **RSG** owns various possible **State** entries (each state could be, e.g., Ready, Waiting, Degraded, etc.). Each State has a **Checklist** which is **tested by** an Evaluation process, resulting in a **StateAssertion** (pass/fail) at runtime. Meanwhile, **Work** instances (concrete operations) are performed by the RoleAssignment and correspond to some MethodDescription (procedure). The “gate” for Work is that a StateAssertion for an enactable state must exist.

_Relational stub:_ (illustrating how data might be stored)

| Table | Key Columns (essential) |
| --- | --- |
| **ROLE\_ASSIGNMENT** | `RA_ID` (PK); `HOLDER_ID`; `ROLE_ID`; `CONTEXT_ID`; `WINDOW_FROM`, `WINDOW_TO` |
| **RCS\_SNAPSHOT** | `SNAP_ID` (PK); `RA_ID` (FK to ROLE\_ASSIGNMENT); `WINDOW_FROM`, `WINDOW_TO`; `CHAR_ID`; `VALUE`; `UNIT`; `SCALE_TYPE` |
| **RSG\_STATE** | `STATE_ID` (PK); `ROLE_ID`; `CONTEXT_ID`; `NAME`; `ENACTABLE` (bool) |
| **CHECKLIST** | `CHK_ID` (PK); `STATE_ID` (FK to RSG\_STATE); `PREDICATE_TYPE`; `PREDICATE_SPEC` |
| **STATE\_ASSERTION** | `SA_ID` (PK); `RA_ID` (FK); `STATE_ID` (FK); `CHK_ID` (FK); `WINDOW_FROM`, `WINDOW_TO`; `VERDICT` (pass/fail); `NORMALIZATION_ID`?; `BRIDGE_ID`? |
| **WORK** | `WORK_ID` (PK); `RA_ID` (FK); `METHODDESC_ID` (FK to MethodDescription); `WINDOW_FROM`, `WINDOW_TO`; _(other fields like results or references)_ |

In this schema: an RCS snapshot table might log individual coordinate values (`VALUE`) for each Characteristic (`CHAR_ID`) in a given RoleAssignment, with their units and scale type noted (to ensure we know what the number means). The StateAssertion ties a RoleAssignment to a state checklist and says whether it passed, including references to any gauge or bridge if cross-context or scaled comparisons were involved. The gate logic for enactment can then be a query like: “Is Work W admissible now?” – which joins through ROLE\_ASSIGNMENT to find the latest StateAssertion for that RA where `ENACTABLE=true` and `VERDICT=pass`.

**8.4.2 Assurance CN‑frame — Evidence freshness & mapped comparisons**

_Entity graph view:_

NormalizationMethodInstance ── appliesTo ──> Characteristic   (each instance is a scale‑appropriate, monotone transform within UNM)
Bridge (ContextB → ContextA)   (Alignment Bridge between contexts, with CL and loss notes)
StateAssertion ── uses ──> {NormalizationMethodInstance, Bridge}   (if a state comparison crossed contexts)

This view highlights that in the assurance context, we keep track of how we mapped or compared states:

* A **NormalizationMethodInstance** represents a monotone, scale‑appropriate mapping from one Characteristic’s scale to another’s under **UNM** (editioned, with validity window).
* A **Bridge** between Context B and Context A (for corresponding roles or states) carries a CL rating and possibly notes on what is “lost in translation.”
* A **StateAssertion** may **use** a NormalizationMethodInstance or a Bridge, meaning that assertion was reached by translating data via that instance or comparing across that bridge.

_Relational stub:_

| Table                | Key Columns (essential)                                                                                                               |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **NORMALIZATION\_METHOD** | `NORMALIZATION_METHOD_ID` (PK); `CLASS` (ratio:scale | interval:affine | ordinal:monotone | nominal:categorical | tabular:LUT); `DESCRIPTION_REF` |
| **NORMALIZATION\_INSTANCE** | `NORMALIZATION_INSTANCE_ID` (PK); `NORMALIZATION_METHOD_ID` (FK); `SRC_CHAR_ID`; `TGT_CHAR_ID`; `FORMULA_SPEC|LUT_REF`; `MONOTONE` (bool); `VALIDITY_WINDOW`; `EVIDENCE_REF` |
| **BRIDGE**           | `BRIDGE_ID` (PK); `FROM_ROLE@CTX`; `TO_ROLE@CTX`; `CL` (congruence-loss level, e.g. 0–3); `NOTES` (description of losses/adjustments) |
| **ASSURANCE\_EVENT** | `AE_ID` (PK); `SA_ID` (FK to StateAssertion); `EFFECT` (enum: penalty\_applied, evidence\_refreshed, etc.); `DETAILS`                 |

In this stub, **NORMALIZATION\_MAP** defines each cross-scale mapping that has to be accounted for (with `FORMULA_SPEC` describing how to compute the target value from the source). The Bridge table enumerates official Bridges between contexts (for example, bridging a “Ready” state in an engineering context to “Ready” in an operations context, with CL indicating how fully comparable they are). An ASSURANCE\_EVENT log could record when a penalty was applied due to a low-CL Bridge or when an assertion was refreshed or invalidated due to new evidence or time lapse. (For instance, policy might say if a critical state assertion uses a Bridge with CL < 2 in a safety context, a special waiver or secondary approval is needed – that could be represented as an event requiring a **Waiver** action.)

**8.4.3 Alignment CN‑frame — Design-time reuse of states across Contexts**

_Entity graph view:_

Checklist(ContextA.State)   ← pull(N) —   Checklist’(ContextB.State’)   (pull a checklist via **NormalizationMethodInstance** N)
Refinement π : RSG(Role' ≤ Role)   (RSG refinement mapping, e.g. Role' is a subtype of Role)

This view covers how _design-time_ alignment happens:

-   A **Checklist’** for a state in Context B can be **pulled** via a **NormalizationMethodInstance** into Context A to become a derived Checklist for a state in Context A. This is effectively what we described in the pull operation: using another context’s criteria in your own space.
    
-   A **Refinement π** is shown between RSGs indicating Role’ is a specialized role of Role (e.g. a sub-role or a scenario-specific role) and how their states relate (Role’ might have extra states or more granular distinctions). This refinement should maintain that for each state in Role’ that maps to a state in Role, the entails/implication relation holds for enactability.
    

_Relational stub:_

| Table               | Key Columns                                                                                                                                                                                       |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **RSG\_REFINEMENT** | `MAP_ID` (PK); `ROLEPRIME_ID` (FK to Role' in Context B); `ROLE_ID` (FK to Role in Context A); `STATEPRIME_ID` (FK to state in Role' RSG); `STATE_ID` (FK to state in Role RSG); `ENTAILS` (bool) |
| **CHECKLIST\_PULL** | `PULL_ID` (PK); `SRC_STATE_ID`; `TGT_STATE_ID`; `NORMALIZATION_INSTANCE_ID` (FK to NormalizationMethodInstance used); `VERSION`? /\* and perhaps timestamp \*/                                     |

In this stub, RSG\_REFINEMENT maps states of a sub-role to states of a super-role, with an `ENTAILS` flag indicating if being in the sub-state guarantees being in the super-state. **Every refinement mapping should ensure at least one enactable state in the sub-role corresponds to an enactable state in the super-role** (or else the sub-role would allow something the super-role doesn’t – that’s an alignment lint check). The CHECKLIST\_PULL table records that a state from one context has had its checklist pulled into another context via a gauge (identified by GAUGE\_ID). This is a design artifact saying “State X in context A is defined by applying gauge G to State Y in context B’s criteria.” A version or validity field might ensure we know which edition of the checklist or gauge was used.

### 9 · Anti‑patterns (and the fix)

| Anti‑pattern            | Symptom                                   | Why it hurts                 | Fix (CN‑Spec slot)                           |
| ----------------------- | ----------------------------------------- | ---------------------------- | --------------------------------------- |
| **Chartless number**    | “Latency = 120”                           | No unit/vantage → untestable | Fill `cs_basis` + `chart`                          |
| **Normalization smuggling**     | Quiet “per‑unit” normalisation mid‑stream | Trend reversal               | Declare `NormalizationMethod`/**NormalizationMethodInstance** + keep invariant        |
| **Bridge‑by‑name**      | Reusing labels across Contexts               | False comparability          | Author **Bridge** with CL + loss        |
| **Free‑hand averaging** | Arithmetic mean on bounded risks          | Violates WLNK                | Declare `Γ_fold` with WLNK              |
| **CN‑frame sprawl**        | Ten nearly‑identical CN‑frames               | Cognitive debt               | Use Registry + DRR; prefer reuse        |
| **Role conflation**     | Same person edits CN‑Spec & certifies data     | SoD breach                   | Enforce `CN‑frameSteward ⊥ CN‑frameCertifier` |

### 10 · Didactic quick cards (one‑liners teams reuse)

1. **Numbers travel with their Context.** Always cite `Context@Edition`.
2. **If the normalization is not declared, the trend is fiction.**
3. **WLNK beats wishful means.** Use weakest‑link folds for safety.
4. **Admit → Assert → Act.** (CN‑frame admission → RSG StateAssertion → Method step).
5. **Bridge or bust.** Cross‑context = Bridge with CL and loss notes.
6. **Steward writes, Certifier admits.** (SoD by design.)
7. **Charts are recipes.** Name the `MethodDescription` that made the number.
8. **Deprecate in the open.** CN‑frame cards carry DRR & retirement plans.
9. **Keep characteristics few, meanings sharp.** Prefer ≤ 7 characteristics per CN‑frame.
10. **No tooling names in Core.** Semantics first; notation later.
11. **Use method/instance IDs, not “gauge/map”.** Prefer `NormalizationMethodId`/`NormalizationMethodInstanceId`.

### 11 · SCR / RSCR Harness (acceptance & regression)

> **These are concept‑level checks; notation‑agnostic.**

#### 11.1 **SCR — Acceptance (first introduction)**

* **SCR‑A19.4‑S01 (Completeness).** **CN‑Spec has **all** mandatory slots; `cs_basis` include **unit/scale/polarity**; `chart` references a `MethodDescription`.
* **SCR‑A19.4‑S02 (Normalization clarity).** `normalization` lists UNM/NormalizationMethod(s) with validity windows, method descriptions, **and** named invariants.
* **SCR‑A19.4‑S03 (Comparability test).** Provide one worked example showing **coordinatewise** or **normalization‑based** comparison end‑to‑end (with Evidence Graph Ref).
* **SCR‑A19.4‑S04 (Γ‑fold audit).** Aggregation rule spells out WLNK/COMM/LOC/MONO choices; reviewer reconstructs result on a toy set.
* **SCR‑A19.4‑S05 (SoD).** Distinct `RoleAssignments` for `CN‑frameStewardRole` and `CN‑frameCertifierRole` exist; windows do not overlap.
* **SCR‑A19.4‑S06 (describedEntity & anchors surfaced).** For each CN‑Spec characteristic used in the worked example, cite the corresponding CHR Characteristic name and the evidence anchor(s) (A.10) that make the reading observable in this Context.

#### 11.2 **RSCR — Regression (on change)**

* **RSCR‑A19.4‑R01 (UNM edit).** On changing `normalization` (UNM/NormalizationMethod), flag **all** downstream Bridges for CL re‑assessment; re‑run example comparisons.
* **RSCR‑A19.4‑R02 (Slot surgery/Basis surgery).** Adding/removing/renaming slot/basis requires a **new edition**; old data remain valid **for their edition**.
* **RSCR‑A19.4‑R03 (Chart drift).** Updating measurement protocol bumps edition; **historic Work** keeps old edition link.
* **RSCR‑A19.4‑R04 (Fold change).** Any change to `Γ_fold` invalidates cached roll‑ups; re‑compute or mark as superseded.
* **RSCR‑A19.4‑R05 (Bridge health).** After either side’s edition change, **re‑validate** Bridge CL and loss notes before accepting Cross‑context data.
* **RSCR‑A19.4‑R06 (Deprecation rule).** On deprecating a CN‑frame, Registry lists its successor; bridges re‑targeted or retired.

### 12 · Interaction summary (wiring to the rest of the kernel)

* **A.2 / A.2.5 (Roles / RSG).** RSG **checklists** quote **CN‑Spec.acceptance**; enactment gates rely on **admitted** CN‑frame data.
* **B.1 (Γ‑algebra).** CN‑Spec’s `Γ_fold` instantiates Γ\_ctx/Γ\_time/WLNK/MONO choices explicitly.
* **B.3 (Assurance).** Bridge CL enters the **R** term; WLNK protects safety roll‑ups.
* **C.6 / C.7 (LOG‑CAL / CHR‑CAL).** Units, scales, and measurement templates come from CHR; proofs about folds live in LOG‑CAL.

### 13 · Minimal CN‑Spec template (copy/paste, informational)

```
CN‑frame: <Name>      Context: <Context/Edition>
characteristics:
  - <CharacteristicName> : <Unit/Scale>  [Polarity: up|down|target-range]
Chart:
  reference_state: <text>
  coordinate_patch: <domain/subset>
  measurement_protocol_ref: <MethodDescriptionId>
Normalization:
  UNM: <UNMId?>
  methods: [<NormalizationMethodId>...]
  method_descriptions: [<NormalizationMethodDescriptionRef>...]
  invariants: [<property>...]           # what ≡_UNM preserves
  fix?: <NormalizationFixSpec>          # canonical representative of the ≡_UNM class
Indicators (optional):
  policy_ref: <IndicatorChoicePolicyRef>
  resulting_indicators: [<IndicatorId>...] // selection is policy‑defined; NCVs alone do not make an Indicator
Comparability:
  mode: coordinatewise | normalization-based
  minimal_evidence: <what must be observed to compare>
Aggregation:
  fold: <Γ_fold expr>   time_policy: <window, statistic>
  WLNK/COMM/LOC/MONO: <declared choices>
Acceptance:
  checklist: [<observable criterion>...]
  window: <ISO 8601 interval>
  evidence_anchors: [<Observation/Evaluation ids>...]
Alignment (optional):
  bridges: [<BridgeId, CL, kept/lost characteristics, extra guards>...]
Lifecycle:
  owner_role: <Role>
  DRR_links: [<DRR ids>...]
  deprecation_plan: <short note>
```

** Certification data Standard (minimal).** (For implementation completeness, not a user-facing concern.) At minimum, any state certification function should take as input: a specific holon (holder) in a given Role and Context and a time window, and it should have access to a **snapshot** of all relevant RCS coordinates for that Role (plus any other needed observations or speech‑act logs in that window). It should output a **StateAssertion** object that includes: the target state’s identifier, the checklist (or checklist ID) used, the verdict (pass/fail); `evidence_kind ∈ {observation, prediction}`; the **window** `[t_from, t_to]`; for `prediction` also the **horizon Δt** and the **normalization** snapshot used; and references to the supporting observations. If any **NormalizationMethods** or cross‑context Bridges were used, those **MUST** be referenced (IDs) so that any **CL** penalty (B.3) can be applied deterministically. This is to ensure traceability and to apply any assurance penalties. Invariants for this process include: no “secret” criteria (all checklist conditions must be based on observable data, not insider knowledge), versioning of checklists (if a checklist changes version, new assertions are tagged to the new version; old assertions aren’t retroactively modified), and immutability of past assertions (once recorded, a StateAssertion isn’t edited after the fact – if it was wrong or conditions changed, a new assertion is issued instead of altering history).

### Close

A.19.D1 gives A.19 some **teeth**: a *CN‑Spec* you can put on one page, a **Registry** that stops sprawl, **Bridges** that carry explicit loss, and a **checklist + harness** that make comparability **auditable**. It obeys the **mandatory pattern structure** of Part E (style, checklists, DRR, guard‑rails) while remaining tool‑agnostic and context‑local.
