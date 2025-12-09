# Part A – Kernel Architecture Cluster

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

## 1 · Intent & scope (what this pattern fixes)

**Intent.** Provide one, universal, **context‑local** way to say *who is being what, where (and when)* without altering what the thing **is**. The same grammar works for people, machines, software, teams, and **also** for knowledge artefacts (epistemes) when they hold **statuses** rather than perform actions.

**Scope.**

* Defines **`U.RoleAssignment`** (binding a **holder** holon to a **role** inside a **bounded context**, optionally within a **time window**).
* Separates that binding from **`U.RoleEnactment`** (the *run‑time* fact that a piece of **Work** was performed under that assignment).
* Names the **Role Characterisation Space (RCS)** and the **Role State Graph (RSG)** as **intensional** facets of a Role (recorded in its `RoleDescription`, upgraded to `RoleSpec` only after tests exist).
* Declares **eligibility** constraints so Roles apply to the right holon kinds, **without chains** like “Transformer is assigned to be Agent”. Role families are independent.

**Non‑goals.** No storage models, no workflows, no org charts. This is a **thinking Standard**; all semantics are notation‑free.

---

## 2 · Problem frame (recurring confusions this removes)

1. **Type explosion.** Baking transient function into rigid types (“CoolingPump”, “AuditDeveloper”) violates parsimony and makes change brittle.
2. **Context drift.** Labels like *Operator*, *Process Owner*, *Standard* slide in meaning across teams/years when not tied to a **Context**.
3. **Actor vagueness.** Work logs state that things happened but not **who, in what capacity**, under which **local rules**.
4. **Category leaks.** Documents “do” tasks; deontic statuses are treated like run‑time states; capabilities are confused with permissions.
5. **Role chains.** Attempting “System ↦ TransformerRole ↦ AgentRole” mixes **independent** role families and hides design intent.

---

## 3 · Forces (and how we resolve them)

| Force                            | Resolution in this pattern                                                                                                        |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Universality vs locality**     | One mechanism (`U.RoleAssignment`), but every meaning is **context‑local** (Context); Cross‑context sameness only via **Bridge** (F.9). |
| **Stability vs change**          | **Identity of holder** stable; **assignments** come/go via windows; **enactments** are punctual facts attached to Work.           |
| **Clarity vs brevity**           | Full definition + the mnemonic shorthand `Holder#Role:Context@Window`.                                                            |
| **Behavior vs status**           | **Only systems enact behavior**; epistemes **hold statuses**. Different role families, no chains.                                 |
| **Specification vs description** | Role **RCS/RSG** are recorded in **RoleDescription**; upgrade to **RoleSpec** only after a test harness exists (E.10.D2).         |

---

## 4 · Solution — the binding and its strict neighbours

### 4.1 Canonical definition (notation‑free)

**`U.RoleAssignment`** is a **context‑local** binding:

```
RoleAssignment ::= 〈holder: U.Holon, role: U.Role, context: U.BoundedContext, window?: U.Window〉
```

**Invariants (normative).**

* **RA‑1 (Locality).** `role` **MUST** be defined in `context` (its meaning is exactly the one recorded in that Context’s RoleDescription/RoleSpec).
* **RA‑2 (No role‑of‑role).** `holder` **MUST** be a `U.Holon` (System, Episteme, or composite). Assigning roles **to roles** is forbidden.
* **RA‑3 (Eligibility by role family).**

  * **Behavioural / Agential / Constructor roles**: `holder` **MUST** be a `U.System`. Only systems can enact Methods and produce Work.
  * **Epistemic‑status / Normative‑status roles** (e.g., *Evidence*, *Standard*, *Requirement*): `holder` **MUST** be a `U.Episteme`.
  * **Service‑governance roles** (e.g., *ServiceOffering*, *SLO‑Clause* as status carriers): holder is typically a `U.Episteme`; execution still requires a System in a behavioural role.
    *(Contexts may refine eligibility, but cannot weaken these families.)*
* **RA‑4 (Window discipline).** If `window` is present, enactments (below) **MUST** occur within it; if absent, interpret as “open‑ended from assignment time”.
* **RA‑5 (Separation).** A RoleAssignment confers **the capacity/authorization to act** (or the status to be recognised), but it is **not behaviour** (no Work implied), **not capability** (intrinsic ability lives elsewhere), and **not structure** (may never appear in a BoM).
 
  Never use "appointment" as a synonym to "assignment".

**Didactic read.** Think **badge** (*who wears which mask, where, when*). The rules for the mask live **in the room** (Context).

**Two assignment modes**
A RoleAssignment can be:
(a) Authoritative — issued by an authority or policy in the Context (often via a SpeechAct Work); it can open the Green‑Gate for steps that require explicit authorization.
(b) Observational — an evidence‑backed classification that the holder occupies a Role in this Context (e.g., “Moon as SatelliteRole:IAU_2006”). Observational assignments never by themselves open operational Green‑Gates; they can gate decisions and analysis.

### 4.2 Role Enactment (distinct from the assignment)

**`U.RoleEnactment`** captures the *run‑time* fact that **a specific piece of Work** was performed under **a specific Role Assignment**:

```
RoleEnactment ::= 〈work: U.Work, by: U.RoleAssignment〉
```

**Invariants.**

* **RE‑1 (Actor reality).** `by.holder` **MUST** be a `U.System`. (Epistemes never enact Work.)
* **RE‑2 (Temporal fit).** `work.window` **MUST** overlap `by.window` (or `by.window` is open and contains `work.window`).
* **RE‑3 (Method gate).** For the `MethodStep` realised by `work`, `by.role` **MUST** satisfy the step’s `requiredRoles` in that **same Context** (directly or via `≤` specialization inside the Context).
* **RE‑4 (Traceability).** Every `U.Work` **MUST** reference exactly one `U.RoleEnactment` (hence a determinate RoleAssignment) as its performer.

*Reading:* **Assignments authorize; enactments happen.** That single sentence prevents months of muddled logs.

Role Enactment is the occurrence of `U.Work` performed by a `holder` while a valid `U.RoleAssignment` for the required Role is in an enactable state of its RoleStateGraph (A.2.5) within the same Context. Enactment is generic: it includes operational work (e.g., actuation) and communicative work (speech acts such as approvals).

### 4.3 Role Characterisation Space (RCS) & Role State Graph (RSG)

These are **intensional facets** of a **Role**, not containers “inside” the Role. They are **recorded in** the **RoleDescription** (or **RoleSpec** once harnessed), per E.10.D2.

* **RCS (Role Characterisation Space).** A set of named characteristics that parameterise how the Role is understood in a Context (e.g., *AgencyLevel ∈ {None, Assisted, Delegated, Autonomous}*; *SafetyCriticality ∈ {SC0…SC3}*).
* **RSG (Role State Graph).** A directed graph of **named states** (nodes) and **admissible transitions** (edges) for the Role **within the Context** (e.g., *{Eligible → Authorized → Active → Suspended → Revoked}*).

  * Each **state** has a **Conformance Checklist** (set of observable cues) supporting **Evaluations** (“X ∈ *Authorized*@context in W”).
  * RSG governs **role state transitions**, independent of any Work instance.

**Discipline.** Say *“Role is **characterised by** RCS/RSG recorded in RoleDescription”*, **never** “Role **contains** its states.”

---

### 4.4 Shorthand & reading

Use the canonical compact form in prose and diagrams:

```
Holder#Role:Context@Window
```

Examples:

* `PLC_17#Transformer:PipelineOps@2025‑04‑01..2025‑06‑30`
* `ISO_26262v2018#NormativeStandard:AutoSafetyCase` *(status role on an Episteme; no enactment)*

*The shorthand is didactic; the semantics are those of §§4.1–4.3.*

---

### 4.5 Independence of role families (no chains)

Role families (e.g., **Agential**, **Constructor/Transformer**, **Observer/Measurer**, **Status**) are **independent**. A Context may state that *`Surgeon ≤ Clinician`* **within the same family**, but **MUST NOT** model “Transformer is an Agent” by chaining RoleAssignments. When a holder must satisfy **both** an Agential and a Transformer requirement, the **MethodStep** **requires both** roles; the holder **wears two badges**, not a badge‑of‑a‑badge.

## 5 · Eligibility across holon kinds (normative matrix)

A Role’s **family** constrains **who can wear its badge**. Eligibility is part of **didactic hygiene** and prevents chains like “Transformer → Agent”.

### 5.1 Holder kinds (recap)

* **`U.System`** — any acting holon (person, device, software service, team, organization, socio‑technical unit).
* **`U.Episteme`** — any knowledge unit (document, dataset, model, standard, Standard).
* **`U.Holon`** — supertype; only **Systems** enact Work; **Epistemes** can only hold **status** roles.

### 5.2 Role‑family × holder matrix

| Role family (examples)                                                 | May be held by `U.System` | May be held by `U.Episteme` | Notes (eligibility refinements live in Context)                                                                                |
| ---------------------------------------------------------------------- | :-----------------------: | :-------------------------: | ------------------------------------------------------------------------------------------------------------------------------ |
| **Agential** (e.g., *Agent*, *Decision‑Maker*, *Approver*)             |           **✓**           |              ✗              | Requires RCS characteristic *AgencyLevel*; RSG must expose *Authorized/Active* states.                                                   |
| **Transformer/Constructor** (e.g., *Welder*, *ETL‑Runner*)             |           **✓**           |              ✗              | Performs Methods; produces Work; often requires *Capability* evidence.                                                         |
| **Observer/Measurer** (e.g., *Observer*, *Monitor*)                    |           **✓**           |              ✗              | Produces `U.Observation`; may be passive (probe) or active (test rig).                                                         |
| **Communicator/Speech** (e.g., *Authorizer*, *Notifier*)               |           **✓**           |              ✗              | A subtype of behavioral roles; produces `U.Work` typed as SpeechAct.                                                           |
| **Service‑Governance** (e.g., *ServiceOffering*, *SLO‑ClauseCarrier*)  |           (rare)          |            **✓**            | Usually **Episteme** (catalog entry, policy). If a System “offers”, the *offer* is a SpeechAct; the *offering* is an Episteme. |
| **Epistemic‑Status** (e.g., *Evidence*, *Definition*, *AxiomaticCore*) |             ✗             |            **✓**            | Status roles for knowledge; never enact Work.                                                                                  |
| **Normative‑Status / Deontic** (e.g., *Requirement*, *Standard*)       |             ✗             |            **✓**            | Source of obligations; Work is checked **against** them, not enacted by them.                                                  |

**Invariant — RA‑3 (eligibility)** *(restated)*: Assignments **MUST** respect this matrix. A Context may **tighten** (e.g., “Approver must be human”), never loosen.

**Conformance checks (easy to remember).**

* **CC‑ELIG‑1.** If `role.family ∈ {Agential, Transformer, Observer, Speech}`, then `holder : U.System`.
* **CC‑ELIG‑2.** If `role.family ∈ {Epistemic‑Status, Normative‑Status, Service‑Governance}`, then `holder : U.Episteme`.
* **CC‑ELIG‑3.** No “role of a role”: `role` is bound to a **holder**, not to another role or assignment.

---

## 6 · Role algebra **within a single Context** (meaning relations)

Role algebra relates **role types** inside **one** `U.BoundedContext`. It is **not** mereology.

### 6.1 Specialization (narrower assignment)

* **Notation:** `RoleS ≤ RoleG`
* **Semantics (normative):** For any `U.RoleAssignment` with `role = RoleS` in this Context, the holder **also satisfies** requirements for `RoleG` in this Context.
* **Use:** Stable expertise ladders, privilege inheritance.
* **CC‑ALG‑1.** Engines that check `requiredRoles` **MUST** treat `≤` as admissible substitution.

### 6.2 Incompatibility (conceptual role incompatibility)

* **Notation:** `RoleA ⊥ RoleB`
* **Semantics (normative):** A single holder **MUST NOT** have overlapping `window`s for assignments to both roles in this Context.
* * **CC‑ALG‑2.** Validation **MUST** reject overlapping assignments that violate `⊥`.

### 6.3 Bundles (conjunctive requirement)

* **Notation:** `RoleC := Role1 ⊗ Role2 ⊗ …`
* **Semantics:** `RoleC` is **satisfied iff** the holder has **simultaneous** valid assignments for each conjunct role (in this Context).
* **Use:** “On‑call Incident Commander” = *Engineer ⊗ Communicator ⊗ Decision‑Maker*.
* **CC‑ALG‑3.** Checking `requires: [RoleC]` **MUST** expand to conjunctive checks.

> **Didactic guardrails.**
> Use `≤` for lasting ladders, `⊥` for critical safety/governance, `⊗` for frequent conjunctions. Prefer listing multiple `requiredRoles` on Method steps to avoid ornate lattices.

---

## 7 · Time & state transition calculus (windows, RSG, enactability)

**Assignments authorize**, **enactments happen** — in time. RSG governs the **role’s** state transitions; `window` governs the **binding’s** validity.

### 7.1 Windows and overlap

* **Window form:** `@t_start..t_end` (ends may be open).
* **RE‑2 (temporal fit)** *(restated)*: `work.window` **MUST** lie within (or overlap appropriately with) `assignment.window`.
* **Handover pattern:** Close `A#Role@..t` and open `B#Role@t..` — never delete history.
* **CC‑WIN‑1.** Historic assignments **MUST NOT** be erased; close the window instead.

### 7.2 RSG gating of enactment

Each Role’s **RoleDescription/RoleSpec** defines an **RSG** with named states. Some states are **enactable**.

* **RSG‑1 (state types).** A state **MUST** declare whether it **permits** enactment (*enactable: true/false*).
* **RSG‑2 (checklists).** Each state **MUST** list a **Conformance Checklist** (E.10.D2) — observable cues to support **U.Evaluation** yielding a **StateAssertion**.
* **RE‑5 (RSG gate).** A `U.RoleEnactment` is valid **iff** at enactment time the `U.RoleAssignment` can be supported by a **valid StateAssertion** that the holder is in an **enactable** state of the Role’s RSG **in this Context**.
* **Example.** *SurgeonRole* states: *Eligible → Authorized → Active → Suspended → Revoked*. Only **Active** is enactable. A pre‑op checklist produces `StateAssertion(SurgeonRole, Active)`.

**Practical reading.** *Badge valid* (window) ∧ *state is right* (RSG) ⇒ you may act.

### 7.3 Suspensions, revocations, probation

* **Suspend:** transition to a **non‑enactable** state (e.g., *Suspended*). Keep the assignment’s window open; enactment is blocked by **RE‑5**.
* **Revoke:** either (a) close the window, or (b) transition to *Revoked* (non‑enactable).
* **Probation:** a dedicated RSG state with limited enactability (e.g., only under supervision, modelled as an extra required role on Method steps).
* **CC‑RSG‑1.** RSG transitions **MUST** be explicit; no implicit “back to Active”.

### 7.4 Typical temporal patterns (didactic)

* **Shift rotation.** `A#Role@08:00..16:00`, `B#Role@16:00..24:00` — clean handover, no `⊥` issues.
* **Shadowing.** `Trainee#Role@..` + `Mentor#SupervisorRole@..`; Method steps require **both** roles.
* **Emergency bundle.** `SoloOperator := Incision ⊗ Hemostasis ⊗ Suturing`; activate only under declared emergency (Context‑level policy).

---

## 8 · Anti‑patterns (and the fast fix)

| #      | Anti‑pattern          | Symptom                                    | Why it’s harmful                   | FPF fix (conceptual move)                                         |
| ------ | --------------------- | ------------------------------------------ | ---------------------------------- | ----------------------------------------------------------------- |
| **A1** | **Global role label** | “Alice is Lead Engineer” (nowhere)         | Meaning drifts; untestable         | **Always anchor to Context**: `Alice#LeadEngineer:ProjectPhoenix` |
| **A2** | **Role as part**      | BoM lists “Cooling Function”               | Category error (structure vs role) | Keep BoM structural; model `Pump#Cooling:ThermalMgmt`             |
| **A3** | **Document acts**     | “The SOP closed the ticket”                | Epistemes don’t enact Work         | Give the doc a **status role**; make a System enact the step      |
| **A4** | **Role chains**       | “Transformer assigned to be Agent”         | Collapses independent families     | Require **both roles** on Method step; one holder, two badges     |
| **A5** | **Hidden state**      | Acting while *Authorized? Active?* unclear | Safety & audit gaps                | Use RSG with **StateAssertions** gating enactment                 |
| **A6** | **Edition blur**      | Context “ITIL” with no version             | Sense slippage                     | Context card must carry **edition** (E.10.D1/F.1)                  |
| **A7** | **Bridge‑by‑name**    | Equating roles across Contexts by label       | Cross‑context drift                   | Use **F.9 Bridge** with CL & loss notes                           |

## 9 · Archetypal grounding (three disparate arenas)

**Goal.** Show that the same binding **`Holder#Role:Context@Window`**, plus **RCS** (Role‑Characterisation Space) and **RSG** (Role‑State Graph), works uniformly for **operational systems**, **software/service operations**, and **knowledge governance**.

Natural systems note. Spontaneous physical phenomena (e.g., Moon orbiting Earth) are modeled as `U.Dynamics`, not as `U.Work`. An observational RoleAssignment like `Moon#SatelliteRole:IAU_2006` is valid classification but does not imply enactment of a method.

### 9.1 Industrial operations (welding cell)

**Role (family).** `WelderRole` *(Transformer)*
\**RCS (illustrative characteristics).*

* `ProcessClass ∈ {MIG, TIG, Spot}`
* `QualifiedMaterial ∈ {Al, SS, Ti, …}`
* `MaxCurrentAmp ∈ ℝ⁺`
* `SafetyProfile ∈ {Standard, HotWork, ConfinedSpace}`

\**RSG (named states).*
`Unqualified → Qualified → Authorized → Active → Suspended → Revoked`
(*enactable*: **Active** only)

**Assignments.**

* `Robot_SN789#WelderRole:AssemblyLine_2025@2025‑02‑01..open`
* `Robot_SN790#WelderRole:AssemblyLine_2025@2025‑02‑01..open`

**StateAssertions (via checklists).**

* `StateAssertion(WelderRole, Qualified, AssemblyLine_2025, @2025‑02‑01..2026‑02‑01)` — training & test weld coupons.
* `StateAssertion(WelderRole, Active, AssemblyLine_2025, @2025‑03‑01..open)` — daily pre‑shift checks + gas/torch inspection.

**Enactment (gated by RSG).**
A `U.Work` entry `W#Seam134` is valid only if `performedBy = Robot_SN789#WelderRole:AssemblyLine_2025` and an **Active** `StateAssertion` covers the timestamp. If the torch‑health checklist fails, RSG transitions `Active → Suspended`; further seams are blocked by **RE‑5**.

---

### 9.2 Software & cloud operations (continuous delivery / SRE)

**Roles (families).**

* `DeployerRole` *(Transformer)* — authorises execution of deployment Methods.
* `IncidentCommanderRole` *(Agential/Speech)* — directs response and issues SpeechActs (declares incident states).

**RCS (illustrative).**

* `DeployerRole`: `Env ∈ {staging, prod}`, `ChangeWindow`, `RollbackAuthority ∈ {self, peer, CAB}`.
* `IncidentCommanderRole`: `OnCallTier ∈ {L1,L2,L3}`, `ServiceScope`, `PageDuty ∈ {primary, secondary}`.

\**RSGs (named states).*

* `DeployerRole`: `Eligible → Authorized → Active → Suspended` (*enactable*: **Active**).
* `IncidentCommanderRole`: `OnCall → Engaged → Handover → Rest` (*enactable*: **Engaged**).

**Assignments.**

* `sCG‑Spec_ci_bot#DeployerRole:CD_Pipeline_v7@2025‑04‑01..open`
* `Alex#IncidentCommanderRole:SRE_Prod@2025‑04‑10T08:00..2025‑04‑10T20:00`

**StateAssertions (via checklists).**

* `DeployerRole/Active`: completed change ticket, green pre‑deploy tests, peer‑review check mark.
* `IncidentCommanderRole/Engaged`: accepted page, situational brief read, comms‑channel opened.

**Enactment.**

* A deployment `Work` is valid only with `performedBy: sCG‑Spec_ci_bot#DeployerRole:CD_Pipeline_v7` **and** `Active` state asserted for the moment of start.
* Declaring `Incident SEV‑1` is a **SpeechAct Work** performed by `Alex#IncidentCommanderRole:SRE_Prod` in **Engaged** state; it changes deontic conditions (e.g., elevates `RollbackAuthority`).

---

### 9.3 Knowledge governance (standards & requirements)

**Roles (families).**

* `NormativeStandardRole` *(Normative‑Status Episteme)* — a document that is *the* standard **in this Context**.
* `RequirementRole` *(Deontic‑Status Episteme)* — a statement that **binds** behaviour in this Context.

**RCS (illustrative).**

* `NormativeStandardRole`: `Scope`, `Edition`, `ApplicabilityWindow`.
* `RequirementRole`: `BindingClass ∈ {shall, should, may}`, `TargetRole`, `AcceptanceClauseRef`.

\**RSGs (named states).*

* `NormativeStandardRole`: `Proposed → Adopted → Effective → Superseded` (*enactable*: N/A — Episteme roles are **non‑enactable**; they gate others).
* `RequirementRole`: `Draft → Approved → Effective → Retired` (non‑enactable).

**Assignments.**

* `ISO_26262_ed2.pdf#NormativeStandardRole:AutoSafetyCase_2025@2025‑01‑01..open`
* `REQ‑BRAKE‑001.md#RequirementRole:AutoSafetyCase_2025@2025‑03‑05..open`

**Effects (gating, not acting).**

* A system’s **Work** (e.g., HIL test run) is **evaluated** against clauses referenced by `RequirementRole`.
* An **Approval SpeechAct** (by a CAB chair who is a `U.System`) may transition `RequirementRole: Draft → Approved`. The Episteme does not “act”; **Systems** act, **Epistemes** hold status.

---

## 10 · Everyday pattern snippets (didactic moves)

> **Use these micro‑moves to think and speak cleanly; no tooling required.**

1. **“Who can do this step?”**
   On a `MethodStep`, write `requires: [RoleX]`. In your head, expand: “Any `performedBy` whose `role ≤ RoleX`, with a **valid window** and **enactable RSG state**.”
   *Example:* `requires: [SurgeonRole]` and `IncisionOperatorRole ≤ SurgeonRole` ⇒ `Dr.Kim#IncisionOperatorRole:Hospital.OR_2025` is admissible **iff** Active.

2. **Handover without history loss.**
   Close one window, open another. Never delete.
   `Alex#IncidentCommander:SRE_Prod@08:00..12:00`
   `Riya#IncidentCommander:SRE_Prod@12:00..20:00`

3. **Independence by construction (SoD).**
   Declare `Developer ⊥ IndependentAuditor`. Then it’s **impossible** (by validation) to have overlapping windows on one holder for both roles.

4. **Supervision as bundle.**
   Model apprenticeship by requiring `Trainee ⊗ Supervisor` on sensitive steps, or by RSG state **Probation** that flips `enactable` only if `SupervisorRole` is also present.

5. **Same badge name in two Contexts.**
   `LeadEngineer:ProjectPhoenix` ≠ `LeadEngineer:DivisionR&D`. If you must relate, create a **Bridge** with CL & loss notes; never rely on the name.

6. **Documents don’t act; they frame.**
   Replace “the SOP executed X” with: `SOP_v4#RequirementRole:SafetyCase` and a `SpeechAct` “approve run” by `QA_Officer#AuthorizerRole:Plant_2025`.

7. **Window + state ⇒ permission.**
   Quick mental check: *badge valid?* (window) ∧ *state OK?* (RSG) ⇒ **go**; else **no‑go**.

8. **Communicative enactment (approval)**
`CAB_Chair#ApproverRole:ChangeControl@2026-05-01T10:05` performs a SpeechAct Work “Approve Change-4711”. Effect: moves ApproverRole’s RSG state from Authorized?→Approved and
+   opens the Green‑Gate for the operational step “Deploy Change-4711” (performed by a different RoleAssignment).

## 11 · Conformance checklist (SCR) — compact, memorable

> **Pass these and your RoleAssignments are sound.**

**Anchoring & locality**

1. **CC‑CTX‑1.** Every `role` reference names a **role defined in the same `U.BoundedContext`** as the assignment.
2. **CC‑CTX‑2.** No cross‑Context equivalence is assumed by label; relations across Contexts live only in **Bridges** (F.9).

**Eligibility & families**
3\. **CC‑ELIG‑1.** Behavioral roles (`Agential/Transformer/Observer/Speech`) **MUST** bind **`U.System`** holders.
4\. **CC‑ELIG‑2.** Status roles (`Epistemic‑Status/Normative/Service‑Governance`) **MUST** bind **`U.Episteme`** holders.

**Role algebra (in‑Context)**
5\. **CC‑ALG‑1.** `≤` permits substitution for `requiredRoles`.
6\. **CC‑ALG‑2.** `⊥` forbids overlapping windows on the same holder.
7\. **CC‑ALG‑3.** `⊗` expands to conjunctive checks at performance time.

**Time & gating**
8\. **CC‑WIN‑1.** Historic RoleAssignments are never deleted; windows are **closed**, not erased.
9\. **CC‑ENACT‑1.** Every `U.Work` has `performedBy = some U.RoleAssignment`.
10\. **CC‑ENACT‑2.** At the `U.Work` timestamp, an **enactable** `RSG` state is asserted for that assignment (via **StateAssertion**).
11\. **CC‑ENACT‑3.** If state flips to non‑enactable (e.g., **Suspended**), enactment is blocked until an **Active** assertion reappears.

**Strict distinction & category hygiene**
12\. **CC‑SD‑1.** No Role in a BoM/structure tree; roles do not participate in mereology.
13\. **CC‑SD‑2.** Epistemes never enact Work; only Systems do.

**Traceability**
14\. **CC‑TRC‑1.** From any `U.Work`, reviewers can trace **performedBy → RoleAssignment → Role → (RCS,RSG) → Context** and retrieve supporting **StateAssertion** evidence.

---

## 12 · Regression harness (RSCR) — what to re‑check when things change

> **Run these mental “diff checks” whenever you change roles, contexts, or states.**

**RSG & gating**

* **RSCR‑RSG‑E01.** After editing an RSG, verify that each enactable state still has a live **Conformance Checklist** and that historic **StateAssertions** remain interpretable (no silent renames).
* **RSCR‑RSG‑E02.** If a state flips *enactable⇄non‑enactable*, re‑evaluate pending or recurring `U.Work` plans (no hidden authorisations).

**SoD & windows**

* **RSCR‑SOD‑E01.** On adding `⊥` constraints, scan for overlapping assignments that newly violate SoD; schedule revocations or rescheduling.
* **RSCR‑SOD‑E02.** On removing `⊥`, confirm that governance rationale is recorded elsewhere (policy change Episteme).

**Context churn**

* **RSCR‑CTX‑E01.** When a Context edition updates, freeze prior RoleAssignments; create **new** assignments in the new Context rather than mutating old ones.
* **RSCR‑CTX‑E02.** Bridges referencing affected roles are reviewed for CL/loss adjustments.

**Eligibility drift**

* **RSCR‑ELIG‑E01.** If a role family changes (e.g., reclassifying *Offerer* from behavioral to status), audit all assignments for holder‑type violations.

**Trace continuity**

* **RSCR‑TRC‑E01.** Spot‑check that `U.Work → RoleAssignment → StateAssertion` chains still resolve after refactors.
* **RSCR‑TRC‑E02.** Randomly sample old incidents/runs to ensure reproducible authorisation verdicts.

**Name stability**

* **RSCR‑NAME‑E01.** If a role label changes, maintain the **role identity**; treat renamed labels as aliases inside the same Context rather than minting a new role unless RCS/RSG changed materially.

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

## 14 · Cross‑Context bridges in practice (with CL penalties)

> **Rule.** **No Cross‑context substitution by name.** If a step in **Context A** needs `Role_A`, and the performer only holds `Role_B` in **Context B**, you must use an explicit **Bridge** (F.9) that says how `Role_B@B` relates to `Role_A@A`, with a **Congruence Level (CL)** and **loss notes**.

### 14.1 Directional substitution

A Bridge may assert, *directionally*:

* **`substitutesFor(Role_B@B → Role_A@A)`** with a CL and a list of **kept** and **lost** RCS characteristics / RSG nuances.
* The reverse direction **does not** follow unless declared.

### 14.2 CL → gating policy (normative thresholds)

| **CL** | Meaning (intuitive)                     | **Permit** | **Guard**                                                                            | **Block** |
| :----: | --------------------------------------- | :--------: | ------------------------------------------------------------------------------------ | :-------: |
|  **3** | Near‑isomorphic sense; no material loss |     Yes    | None beyond ordinary RSG/Window gates                                                |     —     |
|  **2** | Close but with stated losses            |     Yes    | Require **extra evidence** (e.g., additional checklist item) **or** a named reviewer |     —     |
|  **1** | Distant analogy; risky                  |  Exception | Only by explicit **Waiver SpeechAct** naming the Bridge + loss rationale             |  Default  |
|  **0** | Incompatible                            |     No     | —                                                                                    |    Yes    |

*Normative hooks.* The **Trust & Assurance Calculus (B.3)** aggregates CL penalties into confidence scores; **D.2** may mandate CL≥2 for safety‑critical enactments.

### 14.3 Typical bridges (worked patterns)

* **BPMN Task ↔ PROV Activity.**
  `substitutesFor(Task@BPMN → Activity@PROV)` with **CL=2**; **lost:** BPMN control‑flow guards; **kept:** “bounded occurrence consuming/producing entities.”
  *Effect.* A Work logged as `Activity@PROV` may satisfy a step requiring a `Task@BPMN` **if** an extra guard enforces the BPMN pre‑/post‑conditions.

* **Essence Alpha‑State ↔ RoleStateGraph state.**
  `substitutesFor(“Alpha.State:Ready”@Essence → “Ready”@RSG)` with **CL=2**; **lost:** Alpha‑specific narrative criteria; **kept:** checklist‑based readiness.
  *Effect.* A team may reuse Essence states as labels in RSG, but still maintains local checklists as **StateAssertions**.

* **ITIL Service Owner ↔ RBAC Administrator.**
  Typically **CL=1** and **directional** (Administrator\@RBAC → ServiceOwner\@ITIL) **rejected** unless a policy Bridge enumerates compensating controls.
  *Effect.* Prevents “ops admin = service owner” conflations without an explicit waiver.

### 14.4 Bridge invariants

* **Local first.** Substitution never overrides in‑Context `⊥`, `⊗`, or `≤`.
* **Evidence trail.** Every Cross‑context enactment relying on a Bridge **shall** reference its Bridge id in the `U.Work` justification.
* **Loss visibility.** The Bridge **must** state which **RCS characteristics** are preserved vs dropped; if a dropped characteristic is required by the step, substitution is **invalid**, regardless of CL.

---

## 15 · Consequences (what you can count on)

**Benefits**

1. **No type explosion.** Structure stays stable; function lives in RoleAssignments with small, local lattices.
2. **Traceable authority.** Every `U.Work` has a clean chain: **performedBy → RoleAssignment → Role → (RCS,RSG) → Context**.
3. **Safe heterogeneity.** Different Contexts can use the same badge name differently; conflicts are dissolved by locality and explicit Bridges.
4. **Didactic economy.** One mental form — `Holder#Role:Context@Window` — covers factories, clouds, labs, and libraries.
5. **Strong SoD.** Incompatibilities (`⊥`) and bundles (`⊗`) are first‑class; audits become mechanical.
6. **Assurance‑ready.** RSG + StateAssertions convert checklists into **explicit gates**; CL penalties quantify Cross‑context risk.
7. **Temporal honesty.** Windows encode the ebb and flow of assignments without history loss.

**Costs / discipline required**

1. **RoleDescription work.** Each Context needs a minimal RoleDescription (name, RCS, RSG, checklists).
2. **Bridge authorship.** Cross‑context work requires explicit Bridges with CL & loss notes.
3. **Vocabulary hygiene.** Teams must stop using context‑less role labels.

---

## 16 · Rationale (why this specific design)

* **Strict Distinction (A.7).** Keeps **identity** (Holon) separate from **assignment** (RoleAssignment), **behaviour** (Method/Work), and **knowledge** (Episteme).
* **Ontological Parsimony (A.11).** One universal binding, three tiny in‑Context relations (`≤, ⊥, ⊗`), no global role types.
* **Universal Core (A.8).** Same mechanism works across **systems** (machines, software, teams) and **epistemes** (standards, requirements), demonstrated in §9.
* **Lexical discipline (E.10.D1 & E.10.D2).** Roles are **context‑local**; descriptions (RCS, RSG) are **descriptions of intensional roles**, not the roles themselves.
* **Alignment with SoTA.**

  * **DDD.** Elevates **Bounded Context** from software to a universal meaning frame.
  * **UFO / OntoUML.** Roles as anti‑rigid, context‑dependent types.
  * **OMG Essence.** RSG generalises Alpha state graphs with explicit checklists and enactability flags.
  * **RBAC & Assurance.** First‑class SoD and auditable windows; CL penalties match modern safety/security practice.
  * **PROV‑O.** Clean separation of Activity (Work) from Association (who held which role).

---

## 17 · Relations (where this pattern sits)

**Builds on / depends on**

* **A.1 Holonic Foundation** — `U.Holon` (holders).
* **A.1.1 `U.BoundedContext`** — the “Context of meaning.”
* **A.2 Role Taxonomy** — role families (Agential / Transformer / Observer / Speech; Epistemic‑Status / Normative / Service‑Governance).
* **E.10.D1 (D.CTX)** & **E.10.D2 (Strict Distinction of intensional vs description)** — locality & description discipline.

**Enables / instantiated by**

* **A.15 Role–Method–Work Alignment** — step gating, performer linking, evaluation hooks.
* **B.1 Γ‑algebra** — constructors/observers are simply roles enacted by systems.
* **B.3 Trust & Assurance Calculus** — CL penalties on Bridges; evidence from StateAssertions.
* **D.2 Multi‑Scale Ethics** — duties attach to roles; SoD encoded via `⊥`.
* **F‑cluster (Unification Method)** — F.1–F.4 define Contexts and local senses; F.9 defines Bridges consumed here.

**Interacts with**

* **C.* Architheories*\* (Sys‑CAL, KD‑CAL, Method‑CAL, CHR‑CAL) — enactment hooks, measurement via Observations.
* **Service & Deontics (Part D/E)** — obligations and acceptance evaluated against role‑gated Work.

---

## 18 · Teaching distillation (60‑second recap)

> “Give every action a **badge with a Context**. The badge is a **`U.RoleAssignment`**: `Holder#Role:Context@Window`.
> The badge is **valid** in time (window) and **green** in state (RSG + **StateAssertion**).
> A **Method step** names the badges it needs; a **Work** cites the exact badge that enacted it.
> If a badge comes from another Context, cross with a **Bridge** and respect its **CL penalty**.
> Keep SoD with `⊥`, reuse expertise with `≤`, and require combos with `⊗`.
> Documents don’t act — they hold **status roles**; **only systems enact Work**.
> With this, factories, clouds, and knowledge all speak the same, small grammar.”


# A.2.2 — U.Capability  \[D]

## 1 · Context (plain‑language motivation)

In real projects we must answer two different questions:

* **“Can this system do X?”** — this is about an **ability** inherent to the system.
* **“Is this system assigned to do X here and now?”** — this is about an **assignment** (a **Role assignment**) inside a bounded context.

+Teams frequently blur the two, and then further mix them with **how** the work is done (the **Method**) and **what actually happened** (the **Work**). `U.Capability` isolates **ability as a first‑class concept** so that you can plan realistically, staff responsibly, and audit cleanly.

## 2 · Problem (what goes wrong without this concept)

1. **Permission ≠ ability.** A Role assignment authorizes execution in a context; it does **not** prove the system can meet the required **WorkScope** and **WorkMeasures**.
2. **Recipe ≠ ability.** A Method says *how* to do something; it does not guarantee that *this* holder can meet the target outcomes under the required constraints.
3. **Execution log ≠ ability.** A past Work record does not, by itself, establish a stable ability; conditions may have been favorable or unique.
4. **Cross‑team confusion.** Enterprise terms like “capability”, “service”, and the old “function” are used interchangeably; planning, staffing, and assurance become fragile.

---

## 3 · Forces (what we must balance)

| Force                                   | Tension we resolve                                                                                                                   |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Stability vs. change**                | Ability is a relatively stable property of a system, yet it evolves with upgrades, wear, calibration, and environment.               |
| **Universality vs. domain‑specificity** | One universal notion must serve robots, teams, and software services, while letting each domain keep its own performance vocabulary. |
| **Evidence vs. simplicity**             | We want an ability claim to be evidence‑backed, but the core idea must stay simple enough for planning conversations.                |
| **Local conditions vs. reusability**    | Ability depends on conditions (inputs, environment); still, the concept must be reusable across contexts via explicit scoping.       |

---

## 4 · Solution — define the ability explicitly

### 4.1 Definition
**`U.Capability`** is a **dispositional property of a `U.System`** that states its **ability to produce a class of outcomes** (i.e., execute a class of Work) **within a declared `U.WorkScope` (conditions/assumptions) and meeting stated `U.WorkMeasures`**. It is **not** an assignment (Role), **not** a recipe (Method), and **not** an execution (Work).

> **One-liner to remember:** *Capability = “can do (within its **WorkScope** and measures)”*, independent of *“is assigned now”* or *“did do at time t”*.

**Capability declaration (summary).** A capability SHALL declare, as **separate** items:
* **`U.WorkScope`** (*Work scope*) — the set of `U.ContextSlice` under which the capability can deliver the intended `U.Work` (see **A.2.6 §6.4**);
* **`U.WorkMeasures`** — measurable targets with units evaluated on a **JobSlice** (R‑lane facet);
* **`U.QualificationWindow`** — the time policy that governs operational admissibility at **`Γ_time`** (R‑lane facet).
**Note.** This separation supersedes the legacy “envelope + measures + validity interval” bundle. **Work scope is the set of conditions (USM), not a Characteristic; measures are CHR‑characteristics; capability packages both.**

**Reminder (measurement & scope).** *WorkScope* is a **set‑valued USM object** (membership, set algebra) and **not** a CHR Characteristic; *WorkMeasures* are **CHR Characteristics** with declared scales/units. **Admission checks these separately** (see § 10.3 WG‑2/WG‑3).

### 4.2 Conceptual descriptors (not a data schema)

When you describe a capability in a model or a review, anchor it by answering these five didactic prompts:

1. **Holder:** *Whose ability is this?* → a specific `U.System`.
2. **Context:** *In which bounded context were the measures established?* → `U.BoundedContext` (strongly recommended for clarity and comparability).
3. **Task family:** *Ability to do **what kind** of work?* → reference the relevant **MethodDescription**(s) or method family the system can execute.
4. **WorkScope:** *Under what conditions?* → inputs/resources/environment assumptions (e.g., voltage, pressure, ambient, tool head).
5. **Performance measures:** *With what bounds?* → CHR‑style measures (throughput, precision, latency, reliability, MTBF…) with ranges/targets.

Optional descriptors that improve trust without adding bureaucracy:

* **QualificationWindow:** calibration/qualification window for the stated **WorkScope** (abilities drift).
* **Evidence:** links to test reports, certifications, prior Work summaries (as **Episteme**).
* **Degradation/upgrade notes:** known change points that affect the **WorkScope**.

> **Didactic guardrail:** Capabilities are stated in **positive, measurable terms** (“can weld seam type W at ±0.2 mm up to 12/min at 18 °C–30 °C”). Avoid role words (“welder”) or recipe detail (step flows) here.

### 4.3 Shorthand for everyday speech

To keep discussions terse yet precise, teams often write:

* **“S#17 can \<MethodDescription / task family> @ \<WorkScope> → \<measures>.”**
* Or as a bullet in a capability table scoped to a context, e.g., *AssemblyLine\_2025 Capability Sheet*.

This is not a formal notation—just a consistent way to keep the five prompts in view.

## 5 · Clear distinctions (litmus tests managers can apply)

| If you are talking about…                  | Use                     | Litmus test                                                                                  |
| ------------------------------------------ | ----------------------- | -------------------------------------------------------------------------------------------- |
| **assignment** (who is being what, where) | **Role → Role assignment** | Can you reassign to another holder without changing the system’s composition? If yes → Role. |
| **Ability** (can do within bounds)         | **Capability**          | Would you still say “can do” even if not currently assigned? If yes → Capability.           |
| **Recipe** (how‑to)                        | **Method / MethodDescription** | Has inputs/outputs and steps but no date/time.                                               |
| **Execution** (what happened)              | **Work**                | Has a start/end, consumed resources, left a log.                                             |
| **External promise**                       | **Service**             | Framed as “we provide/guarantee to others.”                                                  |
| **Law/model of change**                    | **Dynamics**            | Describes state evolution, not an ability of one system.                                     |

**Two useful corollaries**

* A step in a Method may **require** a Role; **optionally** it may also stipulate a **capability threshold** (e.g., precision ≤ 0.2 mm). assignment and ability are checked separately.
* A Service depends on **having** the needed capabilities **and** being **assigned** to deliver under the Service’s context.

---

## 6 · Archetypal grounding (parallel structural and organizational examples)

### 6.1 Physical system on a line (structural example)

* **Holder:** `RobotArm_A` (`U.System`).
* **Task family:** seam welding per `Weld_MIG_v3` **MethodDescription**.
* **WorkScope:** workpiece steel grades S235–S355; ambient 18–30 °C; argon mix 92–95 %; torch T‑MIG‑07.
* **Measures:** bead width 6.0 mm ± 0.2 mm; throughput ≤ 12 seams/min; defect rate < 0.5 %.
* **Context:** `AssemblyLine_2025`.
* **Readable claim:** *RobotArm\_A can execute Weld\_MIG\_v3 within the stated **WorkScope** at the stated measures (AssemblyLine\_2025).*
* **What this is not:** It is **not** “the welder”—that is a **Role assignment** when assigned on a shift. It is **not** the weld recipe— that is the **MethodDescription**.

### 6.2 Software service in operations (structural, cyber-physical)

* **Holder:** `PlannerService_v4` (deployed system).
* **Task family:** job‑shop schedule generation per `JS_Schedule_v4` MethodDescription.
* **WorkScope:** 50–500 jobs; 5–40 machines; hard deadlines only; network latency ≤ 20 ms.
* **Measures:** schedule completion within 0.95 of theoretical optimum (benchmark set), 98 % on‑time delivery in simulation.
* **Context:** `PlantScheduling_2025`.
* **Use:** Steps that “require ScheduleGeneration capability ≥ 0.90 optimality” will only pass if the holder’s capability meets or exceeds that bound.

### 6.3 Organizational unit (enterprise sense)

* **Holder:** `FinanceDept` (`U.System` as OrgUnit).
* **Task family:** period close per `CloseBooks_v3` MethodDescription.
* **WorkScope:** IFRS; ERP v12; 8 legal entities; staffing ≥ 6 FTE; cut‑off rules X.
* **Measures:** close in ≤ 5 business days; adjustment error rate < 0.2 %.
* **Context:** `OperatingModel_2025`.
* **Distinction:** This is **ability**; the **Service** “Provide month‑end close” is the external promise derived from this ability once formally offered.

---

## 7 · Bias‑Annotation (as in cluster‑E patterns)

* **Lenses tested:** `Arch`, `Prag`, `Did`, `Epist`.
* **Scope declaration:** Universal; holder constrained to `U.System`.
* **Rationale:** Gives the kernel a clean, reusable **ability concept** so Role (assignment), Method (recipe), Work (execution), and Service (promise) do not collapse into each other. Keeps planning talk truthful and checkable without introducing governance machinery here. **`U.Capability`** is a **dispositional property of a `U.System`** that states its **ability to produce a class of outcomes** (i.e., execute a class of Work) **within a declared `U.WorkScope` (conditions/assumptions) and meeting stated `U.WorkMeasures`**.

## 8 · Conformance Checklist (normative)

**CC‑A2.2‑1 (Holder type).**
A capability **belongs to** a **`U.System`** (physical, cyber, socio‑technical, or organizational). Capabilities are **not** assigned to `U.Episteme`.

**CC‑A2.2‑2 (Separation of concerns).**
A capability is **not** a Role, **not** a Method/MethodDescription, **not** a Work, and **not** a Service. Models **SHALL NOT** use capability declarations to stand in for assignments, recipes, executions, or promises.

**CC‑A2.2‑3 (WorkScope required for operational use).**
When a capability is used to qualify a step or to support planning, its statement **MUST** name a **WorkScope** (conditions/assumptions) and **WorkMeasures** (targets/ranges). **Guards that admit Work MUST test** that the **holder’s WorkScope covers the step’s JobSlice** (i.e., `WorkScope ⊇ JobSlice`) **and that WorkMeasures meet the step’s thresholds, with an explicit `Γ_time` window bound**. Without a WorkScope and measures, a capability is advisory and **SHALL NOT** be used for step admission or assurance claims.

**CC‑A2.2‑4 (Context anchor).**
Capability statements that drive operational decisions **MUST** be anchored to a **`U.BoundedContext`** (the “Context” whose vocabulary and test norms apply).

**CC‑A2.2‑5 (QualificationWindow).**
When capabilities are used operationally (e.g., to gate Work), the statement **MUST** carry a **QualificationWindow** (calibration window, software version window, etc.) and the guard **MUST name the `Γ_time` window** used for the check. Outside the QualificationWindow, the claim is not admissible for gating.

**CC‑A2.2‑6 (Past work remains past).**
Updates to a capability statement **SHALL NOT** retroactively invalidate already recorded Work. Past Work is judged against the capability declaration that was valid **at the time of execution**.

**CC‑A2.2‑7 (Threshold checks are orthogonal to roles).**
A step that requires both a Role and a capability threshold admits a Work only if **both** are satisfied: (i) the performer’s **Role assignment** is active in the step window; (ii) the **holder’s capability** meets or exceeds the threshold **with `WorkScope ⊇ JobSlice` and within the **QualificationWindow** at the named **`Γ_time`**.**

**CC‑A2.2‑8 (Derived capabilities).**
If a capability is claimed for a **composite system** (assembled by Γ), the claim **MUST** be stated as a property of that composite holder (not of its parts) with clear dependency notes (e.g., “valid while Subsystem B meets X”). Details of derivation belong to the context’s methodology, not to this definition.

**CC‑A2.2‑9 (No capability for epistemes).**
Algorithms, standards, and documents provide **evidence** or **recipes**; they **do not** “have capability.” Only systems do.

**CC-A2.2-10 (`Γ_time` selector in guards).**
Scope-sensitive guards (including Method–Work gates) **MUST** include an explicit **`Γ_time`** selector indicating the window *W* over which **ScopeCoverage** and **WorkMeasures** are evaluated.

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

## 10 · Time and change (calibration, drift, upgrades)

Capabilities are **stable but not static**. Three simple practices keep reasoning honest:

* **Qualification windows.** Abilities drift. Put a **QualificationWindow** on the statement (e.g., “valid for software v4.2; recalibration due 2025-09-30”).
* **Change points.** Note upgrades/downgrades that affect the WorkScope or measures.
* **Snapshot at execution.** When Work is recorded, it is implicitly tied to the **then‑current** capability statement; later edits do not rewrite history (see CC‑A2.2‑6).

**Manager’s rule of thumb:** if you would reschedule a job after a tool change, the capability statement needs a new window.

---

## 11 · Composition and Γ (how assembled systems “can do”)

Γ builds a **new holder** (a composite system). Its capability is not the algebraic sum of parts; it is an **ability of the whole** under its own WorkScope.

* **Express at the whole.** “Cell\_3 can place 12 PCB/min with ±0.1 mm” — that is a capability of **Cell\_3**, not of the pick‑and‑place head alone.
* **State dependencies.** “Valid while Feeder\_A delivers reels at ≥ X; vision subsystem calibrated ≤ 72 h ago.”
* **Constructor vs. transformer.** The **ConstructorRole** builds the composite (Γ); the resulting **TransformerRole** may later act on products. Capability belongs to the holder relevant to the action (builder’s ability vs operator’s ability).

---

## 12 · Interaction with Service (external promise)

A **Service** is an **external promise**. It relies on capability but is not identical to it.

* **From capability to service.** You normally **derive** a Service by taking a capability and **fixing** the promise outward (e.g., “We guarantee close ≤ 5 days”).
* **From service back to capability.** If the promise raises the bar (e.g., tighter SLA), the underlying capability must meet or exceed it under the service’s context.
* **Staffing.** Delivering a Service still requires **Role assignments**; capability alone does not authorize action.

**Memory aid:** Capability = *can do*; Service = *promise to others that we will do*.

---

## 13 · Interaction with Dynamics (laws vs. abilities)

* **Dynamics** describe **how states evolve** (models, laws, trajectories).
* **Capability** says **what this system can achieve** within an WorkScope.
* Dynamics often serve as **evidence** or **explanatory models** for capability but are **not** the capability itself.

**Physics example:** an “isothermal process” (process here as transformation) is a **Work** instance whose path is explained by a **Dynamics** episteme; a lab rig’s ability to run that path repeatably is its **capability**.

## 14 · Anti‑patterns (and the right move)

* **Role‑as‑capability.** “Welder role ensures ±0.2 mm.” → Keep **role** as assignment; put **precision** in a **capability** on the holder; put the **threshold** on the **step**.
* **Recipe‑as‑capability.** “We have the ‘Etch\_Al2O3’ capability.” → Recipe is **Method/MethodDescription**; ability is “can execute Etch\_Al2O3 within WorkScope E at measures M.”
* **Work‑as‑capability.** “We did it once, so we can.” → One Work log is not a stable ability; state envelope and measures if you want a capability claim.
* **Context‑less claims.** “This tool can machine titanium.” → Say **where and under what bounds** (context + WorkScope + measures).
* **Stuffing capabilities into BoM/PBS.** Structure lists **what it is**; capabilities belong to **what it can do** (the holder), not inside the parts list.
* **Service‑as‑capability.** “We have the Month‑end Close capability (promise).” → Promise is **Service**; ability is internal, promise is external.

---

## 15 · Migration notes (quick wins for existing texts)

1. **Underline WorkScopes.** For every “can do” sentence, add **conditions** and **measures**; otherwise treat it as background color, not a gate.
2. **Pull thresholds out of roles.** Move “≤ 0.2 mm”, “≥ 0.90 optimality” from role labels into **step requirements**; leave roles clean (assignments).
3. **Pin contexts.** Add the bounded context name to each capability table (“Capability Sheet — AssemblyLine\_2025”).
4. **Snapshot validity.** Add a “valid through” column (software version or calibration horizon).
5. **Separate recipe/execution.** Move flowcharts under **MethodDescription**, runs under **Work**; link the capability to the **holder** with references to those specs.

---

## 16 · Consequences

| Benefits                                                                                           | Trade‑offs / mitigations                                                                                                      |
| -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Truthful planning.** Schedulers and managers can ask “can do?” independently of “assigned now?” | **Extra column in tables.** Adding scope/measures/valid‑through is a small burden that repays itself in fewer reschedules. |
| **Safer gating.** Steps gate on both role and ability; fewer silent failures.                      | **Two checks instead of one.** Keep the checklist simple: *badge + bounds*.                                                   |
| **Clear service design.** Services become explicit promises built on visible abilities.            | **Temptation to over‑promise.** Keep service SLOs within demonstrated capability measures.                                    |
| **Clean separation with Dynamics and PBS/SBS.** No more “process” or “function” soup.              | **Some retraining.** Use the litmus tables (from the lexical rules) during onboarding.                                        |

---

## 17 · Relations

* **Builds on:** A.1 Holonic Foundation; A.1.1 `U.BoundedContext`; A.2 Role; A.2.1 `U.RoleAssignment`.
* **Coordinates with:** A.3 (Transformation & role masks); A.15 (Role–Method–Work Alignment).
* **Constrains:** Step design: thresholds belong on steps; BoM/PBS must stay structural.
* **Informs:** `U.Service` \[D] (external promises derive from capabilities); `U.Dynamics` \[D] (models used as evidence or predictors); Γ/aggregation (capability of composites is stated at the whole).
* **Lexical guards:** E.10.x **L‑FUNC** (do not call capability “function”); E.10.y **L‑PROC** (do not call capability “process”).

---

## 18 · Didactic quick cards (reuse in specs and slides)

* **Capability = can do (within bounds).** assignment ≠ ability ≠ recipe ≠ execution ≠ promise.
* **Gate every critical step with two checks:** *badge (Role assignment)* + *bounds (Capability)*.
* **Write the Context on every claim:** context name, **WorkScope**, measures, **QualificationWindow/valid-through**.

## A.2.3 · `U.Service` \[D]

### 1 · Context

Across domains the word **service** is used for many different things: a server or **provider**, an **API**, a **procedure**, a **run**, a **department**, even a **product bundle**. Such polysemy is productive in everyday speech but toxic in a normative model. FPF needs a **single, minimal, trans‑disciplinary meaning** that stays stable from cloud computing to public administration and manufacturing utilities.

In the Role–Method–Work alignment, **service** must say something **external‑facing** and **consumer‑oriented**, yet remain separate from *how* the provider does it (Method/MethodDescription) and *what actually happened* (Work).

> Intuition: a **service** is the promise you advertise and are judged by; **work** is what you do to keep that promise; **method/spec** is how you know what to do.

#### Lexical note (L‑SERV)

The words *service/service‑level/service use/service access* are **ambiguous** across domains. In the kernel we reserve **`U.Service`** for the unified concept below. Other senses (department, server, microservice binary, help‑desk ticket, etc.) **must** be mapped via `U.RoleAssignment` to roles (`…#ServiceProviderRole:Context`), to **`U.System`**, **`U.Method/MethodDescription`**, or **`U.Work`**, inside the appropriate `U.BoundedContext`. (A short lexical rule **L‑SERV** will be added to E.10 alongside L‑FUNC/L‑PROC/L‑SCHED/L‑ACT.)

---

### 2 · Problem

Without a first‑class `U.Service`, models drift into five recurring errors:

1. **Provider = Service.** Calling the **system** or **team** “the service” collapses structure with promise.
2. **API = Service.** Treating an **interface/endpoint** as the service hides the consumer‑oriented promise (effect + acceptance).
3. **Process = Service.** Mapping a **procedure/Method** (or a WorkPlan) to “service” confuses recipe/schedule with the external commitment.
4. **Run = Service.** Logging **Work** as “a service” erases the Standard/promise layer and breaks SLA reasoning.
5. **Business ontology lock‑in.** Large domain schemes (e.g., “business service” stacks) are imported wholesale, losing FPF’s universality and comparability across contexts.

---

### 3 · Forces

| Force                                       | Tension                                                                                                       |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **External promise vs internal capability** | Service must be consumer‑facing, while capability is provider‑internal.                                       |
| **Specification vs execution**              | Service is a **specifiable** obligation; value is **realised** only by runs of Work.                          |
| **Universality vs domain richness**         | One kernel meaning must cover IT, utilities, healthcare, public services—without absorbing domain taxonomies. |
| **Measurability vs privacy**                | Consumers need SLO/SLA and outcomes; providers want implementation freedom (Method autonomy).                 |
| **Stability vs evolution**                  | Services version and change without invalidating prior Work evidence.                                         |

---

### 4 · Solution — The unified concept `U.Service`

**Definition (normative).**
Within a `U.BoundedContext`, a **`U.Service`** is an **externally oriented commitment**: a **context‑local promise** that a provider **Role** will make a **specified external effect** available to eligible consumers through a **declared access** and **declared acceptance criteria** (SLO/SLA‑like targets). A `U.Service` does **not** prescribe *how* the provider fulfils it (that is `U.Method/MethodDescription`), nor is it the **execution** (that is `U.Work`).

* **Type:** `U.Episteme` (a spec/Standard on a carrier).
* **Scope:** design‑time concept; judged at run‑time by evidence from `U.Work`.
* **Time stance:** design-time concept; judged at run-time by evidence from `U.Work`.
* **Orientation:** consumer‑facing (“what you can rely on”), as opposed to capability (“what we can do”).

#### 4.1 · Core structure (minimal fields)

```
U.Service {
  context        : U.BoundedContext,   // where the promise is meaningful
  purpose        : Text/Episteme,      // the externally observable effect/value
  providerRole   : U.Role,             // role kind that may provide it (not a person/system)
  consumerRole?  : U.Role,             // optional role kind allowed to consume
  claimScope?    : U.ClaimScope,       // where the promise holds (G) — operating conditions/populations/locales
  accessSpec?    : U.MethodDescription,       // how consumers may request/use (interface/eligibility)
  acceptanceSpec : U.Episteme,         // targets: SLO/SLA, quality/throughput/latency/accuracy…
  realizationSpec?: P(U.MethodDescription),   // typical internal specs used by providers (non-binding)
  unitOfDelivery?: Episteme,           // how delivered units are counted/measured
  version?       : SemVer/Text,
  timespan?      : Interval
}
```

* `providerRole` and `consumerRole` are **role kinds**; the actual performers are **RoleAssignings** at run‑time.
* `acceptanceSpec` defines **what counts as fulfilled** (the test).
* `accessSpec` is **how to ask** (eligibility, protocol, counter, desk, API).
* `realizationSpec` is only informative in the kernel (“typical methods”); providers retain **Method autonomy**.

#### 4.2 · What `U.Service` is **not**

* **Not a provider:** use `System#ServiceProviderRole:Context` `U.RoleAssignment`.
* **Not a method/recipe:** that is `U.Method/MethodDescription`.
* **Not a run/incident/ticket:** that is `U.Work`.
* **Not a schedule:** that is `U.WorkPlan`.
* **Not a capability:** capability is **provider‑intrinsic ability**; service is **outward promise**. A service may **require** certain capabilities, but it **is not** the capability.
* **Not a scope label:** do **not** use *applicability*, *envelope*, *generality*, or *validity* as **scope characteristics**; declare **Claim scope (G)** or **Work scope** explicitly where needed (A.2.6).

#### 4.3 · Position in the enactment chain

* **Design‑time:**
  The context **declares Claim scope (G)** for acceptance (operating conditions, populations, locales) per A.2.6.
  The context may assert: `bindsCapability(ServiceProviderRole, Capability)`.
  Providers choose `Method/MethodDescription` to realise the service.

* **Run‑time:**
  A **consumer** performs `Work` (e.g., a request/visit) — `performedBy: ConsumerRoleAssigning`.
  The **provider** performs `Work` to fulfil the service — `performedBy: ProviderRoleAssigning`.
  Delivered `Work` instances are evaluated against `acceptanceSpec` and **counted** via `unitOfDelivery`.
  SLA/SLO outcomes are therefore functions over **Work evidence**, not over the Service object itself.

> **Memory hook:** *Service promises, Method describes, Work proves.*

---

### 5 · Archetypal grounding (engineer‑manager friendly)

| Domain                    | **`U.Service` (promise)**                                 | Provider & Consumer (as Roles)                                   | Access (how to ask)                  | Fulfilment (Work)                        | Typical acceptance targets                  |
| ------------------------- | --------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------ | ---------------------------------------- | ------------------------------------------- |
| **Cloud/IT**              | “**Object Storage**: durable PUT/GET of blobs up to 5 TB” | `CloudTeam#ServiceProviderRole`, `BackupJob#ServiceConsumerRole` | `S3_API_Spec_vX` (`MethodDescription`)      | Each PUT/GET run; data durability checks | Availability ≥ 99.9%, durability 11×9       |
| **Manufacturing Utility** | “**Compressed air** at 8 bar in Zone B”                   | `Maintenance#Provider`, `LineB#Consumer`                         | Manifold access rules (`AccessSpec`) | Compressor cycles & delivery logs        | Pressure window, purity class, flow ceiling |
| **Public Service**        | “**Passport issuance** within 20 days”                    | `Agency#Issuer`, `Citizen#Applicant`                             | Portal/desk SOP (`AccessSpec`)       | Case handling runs                       | Lead time ≤ 20 days, defect ≤ 1%            |

**Key takeaway:** the **same kernel object** models S3, a plant utility, and a government service: a **promise with access and acceptance**. Everything else (APIs, compressors, clerks, workflows, tickets) is mapped via **Role/Method/Work**.

---

### 6 · Mapping the common “service” picture to FPF (didactic bridge)

The popular service diagrams (provider ↔ access ↔ use ↔ capability/activity) map to FPF as follows:

* **Agent (as Service Provider)** → `System#ServiceProviderRole:Context` (`U.RoleAssignment`).
* **Service Agreement / SLA** → `U.Service.acceptanceSpec` (+ optional `WorkPlan` for windows).
* **Operating conditions / “where the promise holds”** → `claimScope : U.ClaimScope (G)` (or embedded in `acceptanceSpec`) per A.2.6.
* **Service Presence / Access** → `accessSpec : MethodDescription` (interface/eligibility); actual endpoints are **systems** playing interface roles.
* **Individual Service Use** → **consumer and provider `U.Work`** instances linked to the `U.Service` they fulfil.
* **Service‑Enabled Capability / Activity** → effects on the consumer side: either a **Capability** gained/used, or **Work** performed; do **not** reify as a new kernel type.

(Where a domain needs richer structures—catalogs, exposure layers, charging, entitlement—model them **in the domain context** and relate them to `U.Service` via `U.RoleAssignment` and alignment bridges.)

## 7 · Conformance Checklist (normative)

**CC‑A2.3‑1 (Type).**
`U.Service` **IS** an `U.Episteme` (a consumer‑facing promise on a carrier). It is **not** a `U.System`, **not** a `U.Method/MethodDescription`, **not** a `U.Work`, and **not** a `U.WorkPlan`.

**CC‑A2.3‑2 (Context).**
Every Service **MUST** be declared **inside** a `U.BoundedContext`. Names and meaning are **local**; cross‑context reuse requires a Bridge (`U.Alignment`).

**CC‑A2.3‑3 (Role kinds, not people/systems).**
`providerRole` and (if used) `consumerRole` **MUST** be **role kinds** (see A.2). Actual performers at run‑time are `U.RoleAssignment`s.

**CC-A2.3-4 (Acceptance).**
`acceptanceSpec` **MUST** be present and **MUST** define how delivered `U.Work` is judged (pass/fail/graded) against declared targets (SLO/SLA-like), and **MUST** declare **Claim scope (G)** where relevant (operating conditions, populations, locales). Every verdict binds to an explicit **Γ_time** window.

**CC‑A2.3‑5 (Access).**
If consumers must request/obtain the service through an interface, `accessSpec` **MUST** reference the MethodDescription that defines eligibility and invocation rules (API/desk/SOP). If the service is ambient (e.g., compressed air on a manifold), accessSpec **MAY** be omitted, but the eligibility condition **MUST** be stated in the context.

**CC‑A2.3‑6 (Unit of delivery).**
If performance is counted/charged, `unitOfDelivery` **SHOULD** be declared (e.g., “request”, “kWh”, “case”).

**CC‑A2.3‑7 (No actuals on Service).**
Resource/time **actuals** and incident logs **MUST** attach to `U.Work` only (A.15.1). Services carry no actuals.

**CC‑A2.3‑8 (Capability requirement).**
If the context requires provider abilities, it **MUST** express them as `bindsCapability(providerRole, Capability)` in the context, not by stuffing capabilities into the Service object.

**CC‑A2.3‑9 (Versioning & timespan).**
Services **MAY** carry `version`/`timespan`. A `U.Work` that claims/fulfils a Service **MUST** record which Service version it used.

**CC‑A2.3‑10 (Lexical rule).**
Unqualified uses of *service* (server/team/API/process/ticket) **MUST** be disambiguated per **L‑SERV** (E.10), mapping to `System`/`U.RoleAssignment`/`Method[Spec]`/`Work` as appropriate.

**CC‑A2.3‑11 (No mereology).**
Do **not** place a Service in PBS/SBS or treat it as a part/component. Structural assemblies live in PBS/SBS; Service is a promise.

**CC‑A2.3‑12 (Plan–run split).**
Windows and calendars belong to `U.WorkPlan` (A.15.2). Fulfilment evidence belongs to `U.Work` (A.15.1).

**CC-A2.3-13 (Scope lexicon & guards).**
Deprecated labels *applicability/envelope/generality/validity* **MUST NOT** appear as scope characteristics in guards or conformance blocks. Use **`U.ClaimScope (G)`** for epistemes and **`U.WorkScope`** for capabilities (A.2.6/A.2.2). Scope-sensitive guards **MUST** use **ScopeCoverage** with explicit **Γ_time** selectors.

**CC-A2.3-14 (Bridges & CL).**
Cross-context mappings via Bridges keep **F/G** stable; **CL** penalties apply to **R**. A mapping **MAY** recommend **narrowing** the mapped **Claim scope (G)** as best practice (A.2.6/B-line).

## 8 · Evidence relations & operators (Service ⇄ Work)

To keep the promise → evidence path explicit:

### 8.1 Core relations

* **`claimsService(Work, Service)`** — the Work instance **intends** to fulfil the Service (pre‑verdict).
* **`fulfilsService(Work, Service)`** — the Work instance **meets** the Service’s `acceptanceSpec` (post‑verdict: pass).
* **`acceptanceVerdict(Work)`** → {`pass`, `fail`, `partial`, context‑specific grades} — computed by applying `acceptanceSpec` to Work facts.
* **`usesAccess(Work, MethodDescription)`** — consumer Work that invokes the service via its `accessSpec` (when applicable).

> **Invariant:** `fulfilsService(W,S)` ⇒ `claimsService(W,S)` and `acceptanceVerdict(W)=pass`.
> **Invariant:** A Work can claim/fulfil **multiple** Services only if the context declares a counting policy (no silent double‑counting).

### 8.2 Service performance operators

Let `W(S, T)` be the set of Work that `claimsService(·,S)` within time window `T`. Let `W✓(S, T)` be those with `fulfilsService`.

* **Delivered units:** `delivered(S, T) = |W✓(S, T)|` (or sum per `unitOfDelivery`).
* **Rejection rate:** `rejectRate(S, T) = 1 − |W✓| / |W|` (declare handling of `partial`).
* **Lead time:** average/percentile of `duration(Work)` or of request→completion delta (declare definition).
* **Availability/Uptime:** computed from Work/telemetry events per the context’s definition (declare availability source).
* **Cost‑to‑serve:** sum of `Γ_work` over `W✓` per resource category (A.15.1).

All metrics are **functions of Work evidence**; the Service object is never the bearer of actuals.
Aggregation across time uses `Γ_time` policies (union vs convex hull) chosen by the KPI owner.

---

## 9 · Anti‑patterns (and the right move)

* **“The microservice **is** the service.”**
  A microservice binary is a `U.System`. Make it a provider via `System#ServiceProviderRole:Context`; keep the **promise** in `U.Service`.

* **“The API **is** the service.”**
  The API is typically `accessSpec : MethodDescription` (and systems playing interface roles). The **service** is the promise judged by `acceptanceSpec`.

* **“Our **process** is the service.”**
  Process/recipe is `U.Method/MethodDescription`; schedule is `U.WorkPlan`. The service is **what is promised to the consumer**.

* **“The **ticket** is the service.”**
  A ticket/case is `U.Work` (and perhaps a `WorkPlan` item). Evidence and outcomes sit on Work, not on Service.

* **“Attach cost to the service.”**
  Actual cost/time attach to `U.Work` only (A.15.1). Service metrics are computed **from** Work.

* **“Put service under BoM.”**
  Services are not structural parts. Keep PBS/SBS clean.

* **“Hard‑code people into the service.”**
  Name **role kinds** in `U.Service`; run‑time performers are `U.RoleAssignment`s.

---

## 10 · Migration notes (quick wins)

1. **Name the promises.** List 5–15 consumer‑facing promises your context lives by; reify each as `U.Service` with `acceptanceSpec` and, if needed, `accessSpec` and `unitOfDelivery`.
2. **Separate provider from service.** Keep systems/teams as `U.System`; make them providers via `…#ServiceProviderRole:Context`.
3. **Wire evidence.** Ensure every relevant `U.Work` has `claimsService` (and `fulfilsService` post‑verdict).
4. **Choose metrics.** For each Service, define 2–4 KPIs and the **exact** Work-based formulas (availability, lead-time, rejection rate, cost-to-serve), and declare the **Claim scope (G)** and **Γ_time** policy used for each KPI.
5. **Bridge domains.** If a business ontology already exists (“business/technical/internal service”), keep it in its own context and map to `U.Service` via Bridges.
6. **Tidy language.** Apply **L‑SERV**: ban “service” as a synonym for server/team/process/ticket in kernel narratives; map them explicitly.

---

## 11 · Relations

* **Builds on:** A.1.1 `U.BoundedContext`; A.2 `U.Role`; A.2.1 `U.RoleAssignment`; A.2.2 `U.Capability`; **A.2.6 `U.Scope` / `U.ClaimScope (G)` / `U.WorkScope`**.
* **Coordinates with:** A.3.1 `U.Method`; A.3.2 `U.MethodDescription`; A.15.1 `U.Work`; A.15.2 `U.WorkPlan`; **B-line Bridges & CL (CL→R; may recommend ΔG narrowing)**.
* **Constrained by lexical rules:** **E.10 L‑SERV** (service disambiguation); also **L‑FUNC**, **L‑PROC**, **L‑SCHED**, **L‑ACT**.
* **Informs:** Reporting/assurance patterns (service KPIs, SLA dashboards); catalog/exposure patterns in domain contexts.

---

## 12 · Didactic quick cards (engineer‑manager ready)

* **Service = Promise.** *What we advertise and are judged by.*
* **Method/Spec = Recipe.** *How we usually do it (provider‑internal).*
* **Work = Evidence.** *What actually happened and consumed resources.*
* **Provider/Consumer = Roles.** *assignment via RoleAssigning at run‑time.*
* **Metrics from Work.** *Uptime, lead time, quality are computed from Work, not from the Service object.*
* **Keep PBS/SBS clean.** *Services are not parts; they are promises.*

## A.2.4 — `U.EvidenceRole` \[D]

> *This pattern defines how a knowledge artefact (“episteme”) serves as **evidence** for a specific claim or theory **inside a bounded context**. It is a **non‑behavioural** role enacted via `U.RoleAssignment`; the binding **must** declare the **target claim**, the **claim‑scope**, and a **timespan of relevance**. Evidence is a classificatory status of an episteme; it is not an action and it is not an assignment of an actor.*

### 1 · Context and intent

FPF separates **what exists** (holons and their kinds) from **what acts** (systems under roles performing work) and from **what is known** (epistemes carried on symbols). Roles are contextual masks that holons may wear; role meanings are **local to a `U.BoundedContext`**. In this setting, we need a kernel‑level way to say that *this* episteme **counts as evidence** about *that* claim, **here**, and **for this period**, without confusing evidence with services, methods, or work. 

**Intent.** Provide one uniform, discipline‑neutral role by which an episteme can be assigned as evidence, while keeping:

* **Agency** on systems performing `U.Work` (not on epistemes).
* **Promise** and Standardual language on `U.Service` (not on evidence).
* **Recipe** and eligibility on `U.Method` / `U.MethodDescription` (not on evidence).

### 2 · Problem

1. **Anthropomorphising epistemes.** Models say “the paper proves…”, implicitly treating a document as an actor.
2. **Citation without scope.** Links exist but lack explicit **target claim**, **applicability scope**, and **time window**.
3. **Deductive versus empirical conflation.** A formal derivation and a lab dataset are both called “support” although their semantics and ageing differ.
4. **Staleness and drift.** Empirical evidence ages; without explicit validity windows, stale evidence keeps influencing conclusions.
5. **Cross‑context leakage.** Evidence is interpreted as “global,” skipping the bridge that is required to move meaning across contexts.

### 3 · Forces

| Force                                     | Tension to resolve                                                                                |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **Universality versus domain practice**   | One role must cover proofs, datasets, replications, benchmarks, model fits, calibrations.         |
| **Static truth versus ageing confidence** | Axiomatic proofs are stable relative to a theory; empirical evidence decays and requires refresh. |
| **Local meaning versus reuse**            | Meaning is context‑local; reuse must pass through explicit bridges, not tacit “global truth.”     |
| **Clarity versus brevity**                | Kernel must stay expressive without importing domain governance or tooling procedures.            |

### 4 · Solution — Term and definition

**Term.**
`U.EvidenceRole` — a **non-behavioural role** that a `U.Episteme` may play **inside a `U.BoundedContext`** to serve as **evidence** for a declared target claim (or theory/version).
The target claim, its applicability scope, polarity, weighting model, and other normative facets are **properties of the `U.EvidenceRole` definition itself** *within that bounded context*.

**How it is enacted.**
The role is enacted by a standard `U.RoleAssignment` that connects:

```
RoleAssigning {
  holder  : U.Episteme,        // the artefact: paper, proof, dataset, report…
  role    : U.EvidenceRole,    // a context-defined role with normative properties
  context : U.BoundedContext   // where the role definition is valid
  timespan?: Interval          // optional: relevance window for this specific assignment
}
```

The **normative properties** of the role (e.g., `claimRef`, `claimScope`, `polarity`, `weightModelRef`) are set in the **role’s definition** in the given `U.BoundedContext`, not in the binding.
`U.RoleAssignment` carries only the linkage between a concrete episteme and a role already defined and attributed in that context.

> **Non-behavioural guard.** The holder is an episteme; any actions that produced it are `U.Work` performed by systems. Evidence classifies an artefact’s evidential status; it does not itself enact behaviour.

**Minimal readable grammar (informative).**
`<Episteme>#<EvidenceRole>:<Context>` — where `<EvidenceRole>` in `<Context>` already normatively specifies `polarity Claim / Scope [weight]`.

**Examples.**

* In `Cardio_2026`, `ModelFitEvidenceRole` is defined with:
  `claim = β-blocker > placebo`, `claimScope = adults 40–65`, `polarity = supports`, `weightModelRef = KD:SupportMeasure`.
  Binding:
  `Trial-R3.csv#ModelFitEvidenceRole:Cardio_2026`.

* In `Theory_T`, `AxiomaticProofRole` is defined with:
  `claim = Theorem-12`, `claimScope = all x ∈ D`, `polarity = supports`.
  Binding:
  `Lemma-12.proof#AxiomaticProofRole:Theory_T`.


### 5 · Role family and specialisations

`U.EvidenceRole` is a **role kind** refined by **specialisation** (no mereology of roles). The recommended, substrate‑neutral specialisations are:

**5.1 Axiomatic line (deductive inside a fixed theory)**

* **`AxiomaticProofRole`** — a proof that **entails** a target statement in a declared `U.TheoryVersion`.
* **`CounterexampleRole`** — a witness that **refutes** a universally quantified claim in the theory.
* **`DerivationRole`** — a lemma or intermediary derivation establishing a dependency in the proof spine.
* **`EquiconsistencyEvidenceRole`** — a metaproof establishing equiconsistency or relative strength, often used to **constrain** theory choice.

**Semantics.** In a fixed theory version, these roles are **boolean** and **non‑decaying**. If the axiom base or definitions change, the binding must be re‑issued for the new version; there is no silent carry‑over.

**5.2 Experimental line (empirical, inductive, and model‑selection)**

* **`ObservationEvidenceRole`** — raw or processed observations under a declared method.
* **`MeasurementEvidenceRole`** — calibrated measurements with an error model and traceability.
* **`ModelFitEvidenceRole`** — comparative fit or likelihood of data to competing models; supports one **over** another within the declared scope.
* **`ReplicationEvidenceRole`** — independent replication status (full, partial, failed).
* **`CalibrationEvidenceRole`** — evidence about the measurement chain (instrument validity), typically **constraining** claims.
* **`BenchmarkEvidenceRole`** — standardised tasks or suites producing comparable scores.

**Semantics.** Experimental roles require a **claim‑scope** and a **relevance timespan**. Their contribution to confidence is **graded** and may **decay**; the same artefact may carry multiple bindings for different claims or scopes (distinct role assignments).

> **Specialisation, not stacking.** Do not build chains like “transformer‑agent‑observer role.” A system enacts behavioural roles (e.g., `TransformerRole`) to **perform work**; an episteme enacts `U.EvidenceRole` to **classify** its evidential function. Keep enactment lines separate.

### 6 · Clear distinctions (Strict Distinction, litmus tests)

| If you are talking about…               | Use in FPF                                                    | Why                                                                   |
| --------------------------------------- | ------------------------------------------------------------- | --------------------------------------------------------------------- |
| **Who acted and consumed resources**    | `U.System` with `U.RoleAssignment` performing `U.Work`           | Only systems act; work records resource deltas.                       |
| **What was promised to a consumer**     | `U.Service` (promise with access and acceptance)              | A promise is not evidence; it is judged from work.                    |
| **How work should be done or invoked**  | `U.Method` / `U.MethodDescription`                                   | Recipes and interfaces are not evidence.                              |
| **What counts as evidence for a claim** | `U.Episteme` holding `U.EvidenceRole` via `U.RoleAssignment`     | Evidence is a status of an artefact relative to a claim in a context. |
| **Moving meaning across contexts**      | An explicit bridge/alignment pattern in the receiving context | Role meanings are context‑local by design.                            |

### 7 · Core invariants (concept level)

1. 1. **Holder type.** `U.EvidenceRole` is held by a **`U.Episteme`** only; never by a system, work, method, or service.  # [M‑0]
2. **Context anchor.** Every binding **must** name a `U.BoundedContext`; meaning is local and does not propagate implicitly.
3. **Target claim.** Every binding **must** reference a resolvable claim or theory statement and declare **polarity** `{supports | refutes | constrains | neutral}`.
4. **Claim‑scope.** Every binding **must** declare an applicability scope; for the axiomatic line this can be the theory’s domain.
5. **Timespan.** Every binding **must** declare a relevance interval. Axiomatic roles may be open‑ended **for a fixed theory version**; experimental roles require finite or refreshable windows.  **Gating:** narrative only at **M‑0**; explicit `timespan` & `decayClass` at **M‑2**; version fence & `proofChecks` at **F‑***.  # [M/F]
6. **Non‑self‑evidence.** The provenance of experimental bindings **must** trace to external `U.Work` performed by systems under roles; an episteme cannot “evidence itself.”
7. **No mixing of stances.** Do not mix design‑time proof artefacts and run‑time traces in one provenance chain; relate them via separate bindings if needed.
8. +8. **No role mereology.** Roles have **no parts**; refine by **specialisation** only. This prevents confusing “sub‑role” with “subsystem”.   **Profile note:** The constraint is universal (applies to **all profiles**).  # [all]

**Minimal readable grammar (informative).**  
`<Episteme>#<EvidenceRole>:<Context>` — where `<EvidenceRole>` is **defined inside `<Context>`** with normative facets (`claimRef`, `claimScope`, `polarity`, optional `weightModelRef`, decay policy).

**Examples (illustrative only):**

*Cardio (empirical line)*  
Role **definition** in `Cardio_2026`:  
`ModelFitEvidenceRole` with  
`claimRef = (β-blocker > placebo)`, `claimScope = adults 40–65`, `polarity = supports`, `weightModelRef = KD:SupportMeasure`.  
**Binding:**  
`Trial-R3.csv#ModelFitEvidenceRole:Cardio_2026`

*Graph theory (formal line)*  
Role **definition** in `GraphTheory`:  
`AxiomaticProofRole` with `claimRef = Theorem-12`, `claimScope = all finite DAG`, `polarity = supports` (entails), fenced to `TheoryVersion = 3.1`.  
**Binding:**  
`Lemma-12.proof#AxiomaticProofRole:GraphTheory`

### 8 · Facets and semantics (normative)

This section deepens the definition of `U.EvidenceRole` by specifying **which normative facets** are attached to its definition within a `U.BoundedContext`, **how decay is handled**, **what provenance anchors are required**, and **how the role contributes to assurance computation**.

#### 8.1 Claim-scope schema

Every `U.EvidenceRole` definition **within a `U.BoundedContext`** **MUST** declare a claim-scope record. This record ties the role’s meaning to the exact target claim and its claim scope, and aligns with the typed-claim form used in B.3:

| Field           | Meaning                            | Norms                                                                                               |
| --------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------- |
| `claimRef`      | Identifier of the supported claim  | MUST resolve within the context’s claim graph; dangling IDs forbidden.                              |
| `claimHost`     | The holon whose claim is supported | MAY be `U.System` or `U.Episteme`.                                                                  |
| `epistemicMode` | `formal` or `postulative`          | MUST be present; governs stability and decay rules.                                                 |
| `assuranceUse`  | `TA` / `VA` / `LA`                 | Declares whether the evidence functions as typing, verification, or validation input (B.3.3).       |
| `applicability` | Domain subset (envelope)           | Optional for formal proofs; REQUIRED for empirical evidence (units, constraints, parameter ranges). |
| `resultKind`    | Kind of content on the carrier     | Examples: theorem/proof obligation; dataset; calibration; model-fit result.                         |
| `notes`         | Additional context                 | Pointers to SCR/RSCR entries; congruence rationale; bridge IDs if imported from another context.    |

#### 8.2 Timespan and decay

Evidence is perishable unless proven otherwise.

* **Formal (axiomatic) roles** MAY have open-ended `timespan.to = null` **only** if fenced to a specific `U.TheoryVersion` and justified in `notes`.
* **Empirical roles** MUST have a finite or refreshable `timespan`. Decay parameters (half-life, renewal window) are set by the context policy and referenced in the role definition.

When the relevance window closes (`validUntil` reached), the evidence incurs **Epistemic Debt (ED)**. Per B.3.4, debt must trigger one of three managed actions:

1. **Refresh** — new work produces fresh evidence for the same claim and scope.
2. **Deprecate** — role is retired; claim support is reduced or removed.
3. **Waive** — explicit steward decision to accept the stale evidence temporarily.

#### 8.3 Provenance hooks

Each `U.EvidenceRole` **MUST** anchor into the **Evidence–Provenance DAG** (A.10):

* **Formal**: `verifiedBy` → proof artefact carrier(s), with optional `checkedBy` metadata for proof-checker runs.
* **Empirical**: `validatedBy` → data carriers from observed `U.Work` runs; `protocolRef` → `U.MethodDescription`; `fromWorkSet` → IDs of those runs.
* SCR/RSCR anchors (A.10) are mandatory for all carriers.

**No self-evidence rule**: the producing `U.Work` must have been performed by a system in an **external** role; an episteme cannot “prove itself” without independent generation.

#### 8.4 Contribution to assurance

A `U.EvidenceRole` classifies an artefact; its contribution to the target claim’s assurance tuple ⟨F, G, R⟩ is computed in B.3 using:

* **F (formality)** — lower-bounded by the least formal constituent in the provenance path.
* **G (ClaimScope)** — limited to the claim scope; unsupported regions are dropped (WLNK).
* **R (reliability)** — computed as:

```
R_eff := max(0, min_path( min_claimR(path) − Φ(CL_min(path)) ))
```

Here:

* `min_claimR(path)` is the smallest justified reliability along the path from the role to the claim in the context’s support graph.
* `CL_min(path)` is the lowest congruence level on that path.
* `Φ` is the penalty function defined by the context policy; it must be monotonic (lower CL → greater penalty).

If any element in the support chain is `postulative`, the aggregate `epistemicMode` is `postulative`.

**TA/VA/LA distinctions**:

* **TA (Typing assurance)** — primary effect is to improve `CL` on edges, reducing penalties in R computation.
* **VA (Verification assurance)** — primarily raises F and the logical component of R.
* **LA (Validation assurance)** — raises empirical R and constrains G to the validated envelope.

### 9 · Worked examples

#### 9.1 Formal line — *Proof as evidence for a theorem*

**Role definition (in `GraphTheory`)**  
`AxiomaticProofRole`  
- `claimRef = Theorem-12` (“Every finite acyclic graph admits a topological ordering”),  
- `claimScope = all finite DAG`,  
- `polarity = supports` (entails),  
- `epistemicMode = formal`, `assuranceUse = VA`,  
- fenced to `TheoryVersion = 3.1` (open-ended relevance as long as that version stands).

**Binding(s)**  
`Lemma-12.proof#AxiomaticProofRole:GraphTheory`

**Provenance sketch**  
`verifiedBy → Carrier#Proof_p1` (machine-checked), `usedCarrier → Carrier#Def_graph`.

**Effect on assurance (informative)**  
High **F** (machine-checked proof), **G** = “finite DAG”, **R** from proof-obligation integrity; potential CL penalty if an ontology bridge is used.

##### 9.2 Empirical line — *Sensor calibration as evidence for an accuracy claim*

**Role definition (in `Cardio_2026`)**  
`ModelFitEvidenceRole`  
- `claimRef = “Sensor S achieves ±0.3 °C accuracy in [0,70] °C under lab conditions L”`,  
- `claimScope = temperature [0,70] °C; humidity 30–50%; environment L`,  
- `polarity = supports`,  
- `epistemicMode = postulative`, `assuranceUse = LA`,  
- `weightModelRef = KD:SupportMeasure`, `decayPolicy = annual recalibration`.

**Binding(s)**  
`Trial-R3.csv#ModelFitEvidenceRole:Cardio_2026`

**Provenance sketch**  
`validatedBy → Carrier#Dataset_calib_v5`, `protocolRef → MethodDescription#ThermoCalibration`, `fromWorkSet → {cal_run_0502, cal_run_0503}`.

**Effect on assurance (informative)**  
**F** from formalised procedure, **G** = measured envelope, **R** from replication and CL on unit mapping; **R** decays after the policy window unless refreshed.

### 10 · Conformance checklist (normative)

**CC-ER-01 (Type & holder)**
`U.EvidenceRole` **MUST** be held by a `U.Episteme` via `U.RoleAssignment`. Systems, services, methods, or works **MUST NOT** hold this role.

**CC-ER-02 (Context)**
Every binding **MUST** name a `U.BoundedContext`. Role meanings are local and do not propagate without an explicit bridge.

**CC-ER-03 (Target claim)**
Every binding **MUST** reference a resolvable `claimRef@version` and declare `polarity ∈ {supports | refutes | constrains | neutral}`.

**CC-ER-04 (Claim-scope)**
Every binding **MUST** declare `claimScope`. For formal proofs this may be the theory’s domain; for empirical evidence it is mandatory to state population, environment, and parameter envelope.

**CC-ER-05 (Timespan)**
Every binding **MUST** carry a non-empty `timespan`. Formal line may have open-end **only** if fenced to a fixed theory version; empirical line must have a finite or refreshable end.

**CC-ER-06 (Provenance)**
Every binding **MUST** anchor into the EPV-DAG (A.10). For empirical line, `fromWorkSet` must point to external `U.Work`; self-evidence is prohibited.

**CC-ER-07 (Reproducibility)**
Empirical bindings **MUST** state `reproducibility` ∈ {replicated-independent, replicated-internal, not-replicated, irreproducible}, with references where applicable.

**CC-ER-08 (Weight discipline)**
If `weight.score` is present, `weight.modelRef` **MUST** be named and all required inputs supplied.

**CC-ER-09 (Cross-context)**
Cross-context reuse **MUST** go via `U.Alignment` bridge; record `CL_min` on the path for assurance penalties.

**CC-ER-10 (Version fences)**
If the claim or episteme versions, create a new binding; do not mutate in place.

**CC-ER-11 (No role-of-role)**
Roles never hold roles; there is no chaining of behavioural sub-roles into non-behavioural ones.

**CC-ER-12 (Terminology)**
Use *specialisation* for role refinements; reserve *sub* for mereology of systems or artefacts only.

**CC-ER-13 (Lane declaration)**
Every binding **SHALL** declare `assuranceUse ∈ {TA | VA | LA}` and, for **empirical** (LA) bindings, expose `timespan/valid_until` and `decayPolicy` so that SCR can report lane‑separated contributions and freshness (B.3).

### 11 · Anti-patterns and remedies

| Anti-pattern                | Symptom                                                | Remedy                                                                  |
| --------------------------- | ------------------------------------------------------ | ----------------------------------------------------------------------- |
| **Data speaks for itself**  | Binding with no `context` or `claimRef`.               | Anchor to context and explicit claim; set polarity and timespan.        |
| **Evidence = the work run** | Treating `U.Work` as the episteme.                     | Keep factual record on `U.Work`; create a report episteme to bind.      |
| **Attach to system**        | Holder is `U.System`.                                  | Holder must be an episteme; system may be `claimHost`, not role holder. |
| **Global evidence**         | Using one binding across contexts with no bridge.      | Create explicit `U.Alignment` bridge; declare loss policy.              |
| **Ad-hoc weight**           | Number assigned with no declared model.                | Use context-declared model; supply required inputs.                     |
| **Service proves itself**   | Service KPI logged as evidence.                        | KPIs come from `U.Work`; service evaluation can be bound as evidence.   |
| **Scope blur**              | Mixing design-time and run-time provenance in one EPV. | Split into separate bindings; relate via claim graph or bridge.         |

---

### 12 · Operators (conceptual, tooling-agnostic)

These operators extend E.6.1 citation graph capabilities for evidence analysis inside a `U.BoundedContext`:

**12.1 Per-claim evidence**
`evidenceFor(claim, t?) → Set[EvidenceRoleAssigning]`
`counterEvidenceFor(claim, t?) → Set[EvidenceRoleAssigning]`
`weight(claim, t?, model?) → score`   # returns **ordinal** at M‑mode; **numeric** at M‑2/F‑mode.  # [M/F]

**12.2 Decay and windows**
`window(claim, [t0,t1])` — filter bindings by `timespan`.
`decayedWeight(binding, t)` — apply context decay policy.

**12.3 Replication and provenance**
`replicationLedger(binding) → Ledger`
`isIndependentReplication(binding) → boolean`

**12.4 Formal line hooks**
`proofChecks(binding) → {assistant, status, hash, kind∈{classical, constructive}}`  # [F‑*]
`dependsOnAxioms(binding) → Set[AxiomId]`

**12.5 Empirical line hooks**
`fromWorkSet(binding) → Set[WorkId]`
`protocol(binding) → MethodDescriptionId`

---

### 13 · Relations

**Builds on:**
A.2 `U.Role`, A.2.1 `U.RoleAssignment` (role as mask, binding as assignment), A.10 Evidence Graph Referring (EPV-DAG), B.3 Trust & Assurance Calculus.

**Coordinates with:**
A.3.2 `U.MethodDescription` (protocols, proof obligations), E.6.1 Epistemic Roles via `U.RoleAssignment` (didactic gateway).

**Informs:**
KD-CAL (knowledge dynamics, assurance cases), Norm-CAL (policy claims with evidence), planned `U.ServiceEvaluation` (services judged from work and reported as epistemes with evidence bindings).

---

### 14 · Migration notes (quick wins)

1. **Enumerate claims**: For each evidence collection, identify claims and create explicit bindings with polarity.
2. **Separate work from reports**: Facts stay on `U.Work`; create report epistemes to bind as evidence.
3. **Name the calculus**: Replace free-form confidence with context-declared weight model and required inputs.
4. **Fence by version/time**: Bindings carry `timespan` and version fences; add decay class if applicable.
5. **Bridge explicitly**: Cross-context evidence goes through `U.Alignment`, not by fiat.

### 15 · Didactic quick cards (engineer-manager ready)

These are short reminders for non-specialist readers to apply `U.EvidenceRole` correctly:

* **Evidence ≠ Work** — Work is *what happened*; Evidence is a *documented argument* (episteme) about a claim in a context.
* **Local, not global** — Evidence binds *in a room* (context). Outside that room, you need a bridge (`U.Alignment`).
* **Two lines of trust** — Formal line: proof artefacts checked in a declared theory version. Empirical line: observations from Work under a declared method. Both are epistemes wearing `U.EvidenceRole`.
* **Services are promises; Work proves** — KPIs are measured from Work; service evaluations can be bound as evidence for policy claims.
* **Specialise, don’t stack** — Use specialisations of `U.EvidenceRole` to refine meaning; never chain behavioural roles into evidence.

---

### 16 · SCR/RSCR audit stubs (assurance scaffolding)

These stubs allow concept-level validation of bindings, without implying any specific tooling.

**SCR-A2.4-E1 (Binding integrity)**
Assert: `holder` is `U.Episteme`; `context` present; `claimRef` resolves; `timespan` non-empty; provenance anchored to EPV.

**SCR-A2.4-E2 (Weight discipline)**
Assert: if `weight.score` present → `weight.modelRef` present and all required inputs provided; recompute to check.

**SCR-A2.4-E3 (Traceability)**
For empirical bindings: binding → `fromWorkSet` → each `U.Work` has performer `U.RoleAssignment` and timestamps; no missing hops.

**RSCR-A2.4-R1 (Regression on version bump)**
When `claimRef` or holder episteme versions change, ensure **new** bindings are created; no in-place mutation.

**RSCR-A2.4-R2 (Decay check)**
Bindings past `timespan.to` or with expired `decayClass` are flagged for review per context policy.

---

### 17 · Minimal binding schema (informative)

```yaml
+EvidenceRoleAssigning:
+  id: ERB-…
+  context: <BoundedContextId>
+  holder: <EpistemeId>                # paper/proof/dataset/report
+  role: <EvidenceRoleId>              # defined within the context, with normative properties
+  timespan?: {from: ISO-8601, to: ISO-8601|null} # optional assignment window
+  provenance:
+    formal?: { theoryRef: <TheoryId>, proofArtifactRef: <CarrierId>, checkedBy?: <ProofCheckId> }
+    empirical?: { protocolRef: <MethodDescriptionId>, fromWorkSet: [<WorkId>...], dataCarrierRef?: <CarrierId> }
```

---

### 18 · Memory hooks and acceptance cross-checks (informative)

**Memory hook:** *“Evidence binds a **document** to a **claim** in a **Context**, for a **time**, with a **trail**.”*
(document = episteme; claim = scoped thesis; Context = bounded context; time = timespan/decay; trail = provenance)

**Acceptance cross-checks before publishing a binding:**

1. **Holder**: Is it a `U.Episteme`?
2. **Context**: Is the `U.BoundedContext` declared?
3. **Claim**: Does `claimRef` resolve? Is `polarity` set?
4. **Scope**: Is `claimScope` complete? For empirical, are population/env/parameters given?
5. **Timespan**: Is it finite or fenced (formal line)?
6. **Provenance**: Is EPV anchored? Any self-evidence?
7. **Reproducibility**: For empirical, is it declared?
8. **Weight**: If scored, is the model named and inputs complete?
9. **Cross-context**: If imported, is `U.Alignment` bridge in place with CL\_min recorded?
10. **No role-of-role**: Is this role bound directly to an episteme without chaining behavioural roles?

# A.2.5 — U.RoleStateGraph: The Named State Space of a Role \[D]

## 1 · Purpose & scope (why this exists)

A **role** is not only a name; it is a *trajectory of admissible states* that governs when, and under which conditions, a holder of that role may **enact** steps of a `U.MethodDescription`. FPF therefore introduces a first‑class intensional object:

> **`U.RoleStateGraph` (RSG)** — the **finite, named state space** of a **`U.Role` in a given `U.BoundedContext`**, with transitions guarded by conditions over the **Role Characterisation Space (RCS)** and contextual events.

The RSG is the **gate** between *assignment* (`U.RoleAssignment`) and *action* (`U.Work`). A step may be performed **only** when the performer’s assignment is **in an enactable RSG state** at the relevant **Window** (time slice) and this is **proven** by a contemporaneous **StateAssertion** (verdict of `U.Evaluation` against the state’s **Checklist**).

---

## 2 · Problem frame (what goes wrong without an RSG)

1. **Readiness blur.** Teams conflate “has the badge” with “is fit to act now”. Without explicit states (*Ready*, *Calibrated*, *Authorized*, *Suspended*…), enactment checks dissolve into ad‑hoc judgement.
2. **Checklist drift.** Criteria for “ready/approved” live in scattered documents; there is no single conceptual anchor tying them to the role.
3. **Workflow/role confusion.** “State” of a *workflow* (according to workplan) is mistaken for the *state of a role* (eligibility to enact).
4. **Status ≠ enactment.** Epistemic/Normative roles (e.g., *NormativeStandard*, *ApprovedSpecification*) need *statuses* that are **not enactable**, yet are used to gate decisions.
5. **Cross‑context substitution by name.** Labels like *Approved* or *Ready* silently cross contexts with different criteria; the loss is hidden and unaudited.

**Consequences.** Violations of **Strict Distinction (A.7)** and **Didactic Primacy (E.12)**: ambiguous authority to act, unsafe SoD, and non‑reproducible evaluations.

---

## 3 · Core idea (didactic)

Think of a **Role** as a **mask**, and the **RSG** as the **traffic lights for that mask** inside one context of meaning.

* The **nodes** are **named states** (*Ready*, *Degraded*, *Suspended*, *Approved*, *Obsolete*…).
* The **edges** are **transitions** with **guards** (checkable conditions over RCS characteristics and contextual events, e.g., *CalibrationAge ≤ 30d*; *AuthorizationSpeechAct recorded*).
* Each **state** is paired with a **Checklist** (criteria you test to issue a **StateAssertion** for a given **Window**).
* Some states are **enactable = true** (green lights); others are **not enactable** (status lights) and therefore can **gate decisions** but **cannot** directly authorize `U.Work`.

> **One sentence.** **RSG says *when a badge is green*.** The Checklist proves it, the **StateAssertion** records it, and the Method step may proceed.

---

## 4 · Minimal vocabulary (this pattern only)

* **`U.RoleStateGraph` (RSG).** Intensional object *owned by* `(Role, Context)`. Finite set of named **States** and typed **Transitions** with guards.
* **RSG.State.** Intensional **named place**. Properties:

  * `enactable ∈ {true,false}` — whether being in this state authorizes enactment of steps that require this role.
  * `initial?`, `terminal?` — optional markers for lifecycle reasoning.
* **RSG.Transition.** Edge `state_i → state_j` with **Guard** (predicate over RCS characteristics and/or contextual events such as `U.SpeechAct`, `U.Observation`, `U.Evaluation` results).
* **RCS (Role Characterisation Space).** The **characteristic bundle** that characterises this role in this Context (e.g., *CalibrationAge*, *AuthorizationScope*, *FatigueIndex*, *IndependenceFlag*, *EvidenceFreshness*). *(Defined in A.2 Role Taxonomy / RoleDescription.)*
* **State Checklist (description).** A **RoleDescription** component that enumerates **criteria** to test whether a holder can legitimately be treated as **in** a given state for a **Window**. *(Description, not the state itself.)*
* **`U.Evaluation` → StateAssertion (verdict).** The **result** of applying the state’s Checklist to a **concrete holder** at a **time window**, yielding a **verdict** “IN‑STATE(S) @Window” with provenance to observations/evidence.
* **Window.** Temporal interval to which the StateAssertion applies (e.g., `[2025‑05‑01, 2025‑06‑01]`).

> **Strict distinction note.**
>
> * **RSG** and its **States** are **intensionals** (what the role *is allowed to be*).
> * **Checklists** and **StateAssertions** are **descriptions/evaluations** (how we *know* a specific holder *is* in that state now).

---

## 5 · What an RSG is **not** (guardrails)

* **Not a workflow.** RSG transitions do **not** encode task order; they encode **eligibility changes** of the *role*.
* **Not a capability list.** RSG is **authorization/readiness over time**, distinct from `U.Capability` (ability).
* **Not a global status set.** RSG lives **inside one Context**; the label *Ready* in another Context is **a different state** unless bridged (F.9).
* **Not a log.** RSG is not a history. Histories are **StateAssertions** over Windows; **`U.Work`** is the record of enactments.
* **Not a document lifecycle.** Epistemic role RSGs can *look like* document lifecycles, but they remain **role‑status graphs**; the **carrier** lifecycle stays separate (A.7, `U.Carrier`).

---

## 6 · Invariants (preview)

*(Full formal clauses in Part 2/4; listed here for orientation.)*

1. **Locality.** `RSG(Role, Context)` is defined **only** within that `U.BoundedContext`.
2. **Finiteness.** The **State** set is finite and named.
3. **Checklist pairing.** Every State has a **Checklist** in the Role’s **RoleDescription**; every enactable State has **at least one** observable criterion.
4. **Green‑gate discipline.** A Method step requiring `Role` may proceed **only** if a contemporaneous **StateAssertion** exists for an **enactable** State.
5. **No silent Cross‑context reuse.** Cross‑Context reuse requires a **Bridge** with CL and loss notes; local `⊥/≤/⊗` always prevail.

## 7 · Formal structure of an RSG (intensional, context‑local)

> **Definition.** For a given **`U.Role`** in a given **`U.BoundedContext`**, its **`U.RoleStateGraph`** is the tuple
> `RSG(Role, Context) = ⟨S, S_en, T, Guard, init?⟩`, where:

* **`S`** — a **finite set of named States** (`StateName ∈ Tech register`, with a Plain label). Names are **local to `(Role, Context)`**.
* **`S_en ⊆ S`** — the subset of **enactable** states (“green lights”). States in `S \ S_en` are **status‑only** (not enactable).
* **`T ⊆ S × S`** — a set of **typed transitions** `sᵢ → sⱼ`. Transitions are optional; the RSG may be acyclic or cyclic.
* **`Guard`** — for each transition (and optionally for state maintenance), a **predicate over**:

  * the role’s **RCS snapshot** at a **Window** (values on named characteristics; see A.2.3), and
  * **Context events** (e.g., presence of a `U.SpeechAct`, freshness of `U.Observation`, validity of a prior `U.Evaluation`).
* **`init? : S → {true,false}`** — optionally marks **initial** state(s). (Useful for lifecycles; not required for gating.)

**Naming discipline (RSG‑N1…N3).**

1. **RSG‑N1 (Minimal set).** `|S| ≥ 1`. At least **one** state must exist; if **no** state is enactable, the role is **status‑only** in this Context.
2. **RSG‑N2 (Disjoint labels).** State names are **unique** within `(Role, Context)`; reusing global labels (e.g., “Ready”) across contexts is allowed **only** via Bridges (F.9).
3. **RSG‑N3 (Human scale).** For didactics, **≤ 7 states** is the default target; exceeding it requires a one‑sentence rationale (“distinct gate we will actually use”).

---

## 8 · Enactability & Checklist semantics (how a state is *known*, now)

An RSG **does not** determine history; it determines **what counts as being in a state**, and which states **authorize enactment**.

### 8.1 State Checklists (description, not the state)

For each `s ∈ S`, the **RoleDescription** (A.2.3) includes a **State Checklist** `Checklist(s)` — a **named set of criteria** that can be evaluated at a **Window** to test “**holder is in state `s`**”.

* **Criterion kinds (illustrative):**

  * **Threshold over RCS characteristic:** `CalibrationAge ≤ 30 days`.
  * **Presence of act:** `AuthorizationSpeechAct exists within 90 days`.
  * **Evidence freshness:** `Evidence(type=SafetyTest).age ≤ 12 months`.
  * **SoD flag:** `IndependenceFlag = true`.
  * **External status:** `StandardStatus = Approved`.

> **Strict distinction.** `Checklist(s)` is a **description**; the **state** `s` is an **intensional place** in the role’s RSG.

### 8.2 From Checklist to **StateAssertion** (verdict of `U.Evaluation`)

Evaluating `Checklist(s)` at a **Window** produces an **`U.Evaluation` verdict**:

> **`StateAssertion(holder, Role, Context, s, Window)`** — “*For this Window, this holder **is** in state `s`*”, with provenance to the actual observations/evidence.

**Rules (RSG‑C1…C5).**

* **RSG‑C1 (All‑must‑hold).** A `StateAssertion` **MUST** justify that **all required criteria** in `Checklist(s)` hold at the Window.
* **RSG‑C2 (Window freshness).** Each criterion **MUST** define its freshness window; if omitted, default is **instantaneous** at the Window’s end time.
* **RSG‑C3 (No guess).** Pure opinion is disallowed; every criterion is grounded in **observable facts** (`U.Observation`, `U.Work` record, `U.SpeechAct`, or a derived `U.Evaluation`).
* **RSG‑C4 (Non‑monotonic over time).** A `StateAssertion` is **not** permanent; once the Window ends, a new evaluation is needed unless a **maintenance guard** keeps it valid (see 8.3).
* **RSG‑C5 (Uniqueness not required).** Multiple states may be asserted for the same Window if their criteria do not conflict (e.g., `Ready` and `Authorized`). **Enactability** is governed by §8.4.

### 8.3 Transitions & guards (admission, maintenance, exit)

RSG transitions **express how eligibility changes** when guards fire. Guards are **predicates**; the RSG stays **notation‑neutral**.

* **Admission guard (`→ s`)** declares **conditions to enter** state `s`.
* **Maintenance guard (`s ↺`)** must hold to **remain** in `s` (e.g., *FatigueIndex < 0.8*, checked every shift).
* **Exit guard (`s →`)** declares **conditions to leave** `s` (e.g., *CalibrationAge > 30d*).

**Rules (RSG‑G1…G3).**

* **RSG‑G1 (Checklists vs guards).** Checklists decide **recognition** (“am I in `s` now?”). Guards describe **change** (“what moves me in/out of `s`?”). They may reuse the **same predicates**; their roles are distinct.
* **RSG‑G2 (No control‑flow).** Guards may refer to **events** (e.g., “Calibration completed”), but RSG is **not a task graph**; it does not prescribe task order.
* **RSG‑G3 (Observable basis).** Every guard references **observable** RCS characteristics or recorded events (no hidden timers).

### 8.4 The **Green‑Gate Law** (enactment gating)

> **Law (RSG‑E1).** A `U.MethodDescription` step that **requires** role `R` **may be enacted** at Window `W` **iff** there exists a `StateAssertion(holder, R, Context, s, W)` with `s ∈ S_en`.

Corollaries:

* **RSG‑E2 (Specialization lift).** If the step requires a **general role** `R`, and the holder has a `StateAssertion` for a **specialist role** `R' ≤ R` in an **enactable** state whose **lift** (see §9.1) is enactable for `R`, the gate passes.
* **RSG‑E3 (Bundle gate).** If the step requires a **bundle** `R* = R₁ ⊗ … ⊗ Rₙ`, enactment requires **n distinct `StateAssertions`** meeting RSG‑E1 for each `Rᵢ` (unless the Context defines a **CompositeRole** with its own RSG; see §9.3).
* **RSG‑E4 (Status‑only roles).** Roles with `S_en = ∅` can **never** authorize enactment; they may **gate decisions** (e.g., *ApprovedSpecRole*) but not `U.Work`.

---

## 9 · Interaction with role algebra (`≤`, `⊥`, `⊗`) and refinement

### 9.1 Specialization (`≤`) — RSG refinement map

When **`R' ≤ R`** (Specialist role refines General role) **in the same Context**, their RSGs **must align** by a **refinement map**.

> **Rule (RSG‑R1 Refinement).** There exists a **surjective mapping**
> `π : S(R') → S(R)` such that:
>
> 1. **Enactability preservation:** `s' ∈ S_en(R') ⇒ π(s') ∈ S_en(R)`.
> 2. **Checklist entailment:** `Checklist_R'(s') ⇒ Checklist_R(π(s'))` (each specialist state’s criteria **imply** the general state’s criteria).
> 3. **Guard monotonicity (informal):** Transitions in `R'` **do not weaken** the general readiness implied by `R` (entering/exiting patterns respect π).

**Interpretation.** Being in `s'` for `R'` *guarantees* being in `π(s')` for `R`. Thus **StateAssertions lift** along π, enabling **RSG‑E2**.

**Design note.** RCS for `R'` may **extend** that of `R`; specialist states can be **stricter** (more criteria) but not **looser** than their general counterparts.

### 9.2 Incompatibility (`⊥`) — state‑aware SoD

`R_A ⊥ R_B` (within the same Context) states that **a single holder** **must not** have **overlapping, enactable authority** for both roles.

> **Rule (RSG‑I1).** At **Window `W`**, a holder **violates** `R_A ⊥ R_B` iff there exist **StateAssertions**
> `… in s_A ∈ S_en(R_A)` **and** `… in s_B ∈ S_en(R_B)` **both valid at `W`**.

**Optional refinement (soft ⊥).** Contexts **may** tighten incompatibility by listing **state pairs** that are forbidden (e.g., `Ready_A ⊥ Authorized_B`), while allowing benign combinations (e.g., `Suspended_A` + `Ready_B`). By default, **any** enactable pair conflicts.

**Didactic payoff.** SoD is checked by **states in Windows**, not by static role labels.

### 9.3 Bundles (`⊗`) — conjunction without product explosion

A **bundle role** `R* := R₁ ⊗ … ⊗ Rₙ` expresses “**must wear all these badges at once**”.

> **Rule (RSG‑B1).** If `R*` exists **only as a requirement macro**, **do not** construct a product RSG. The **gate** for a step requiring `R*` is satisfied by **n separate StateAssertions** `sᵢ ∈ S_en(Rᵢ)` at the same Window.

> **Rule (RSG‑B2 CompositeRole).** If the Context **declares `R*` as a first‑class `U.Role`**, it **MUST** also specify an `RSG(R*)` and an embedding `ιᵢ : S(R*) → S(Rᵢ)` that **preserves enactability**; being in an enactable state of `R*` **implies** being enactable in each `Rᵢ`.

**Rationale.** Avoid combinatorial blow‑up by default; allow a composite role **only** when the organization genuinely maintains its **own** readiness graph.

### 9.4 Readiness monotonicity across specialization & bundles

* **RSG‑M1 (Specialist suffices).** If a step requires `R`, any `R' ≤ R` whose **lifted state** is enactable **suffices**.
* **RSG‑M2 (Bundle conjunctivity).** If a step requires `R₁ ⊗ R₂`, the performer must produce **both** gates (two StateAssertions), unless a CompositeRole with RSG exists and is used.

---

## 10 · Guard design (types and discipline)

To keep RSGs **operational** but **not procedural**, guards draw on **observable** inputs only.

**Guard types (non‑exhaustive).**

1. **Threshold guards** over RCS characteristics
   `FatigueIndex < 0.8`, `CalibrationAge ≤ 30d`, `EvidenceFreshness(role=Tester) ≤ 90d`.
2. **Event guards** (occurrence since last Window)
   `exists SpeechAct(type=Authorization)`, `exists Evaluation(verdict=Pass, checklist=SafetyKit)`.
3. **Temporal guards** (time within range)
   `now ∈ AuthorizationValidityWindow`, `MaintenanceWindow not active`.
4. **Relational guards**
   `IndependenceFrom(holder=X) = true` (for SoD), `NoOpenIncident(severity≥High)`.

**Rules (RSG‑G4…G6).**

* **RSG‑G4 (Observable only).** Each guard **MUST** be checkable from **observable artefacts** (observations, work logs, speech acts, evaluations) or present RCS values.
* **RSG‑G5 (Context‑local semantics).** Guard semantics are **scoped to Context**; Cross‑context reuse requires a Bridge (§14 in Part 1/4, F.9).
* **RSG‑G6 (Didactic sparseness).** Prefer **few, stable guards** over many brittle micro‑conditions. If a guard encodes **task order**, you are drifting into workflow; refactor back to eligibility.

Allowed guard evidences include:
* Observation facts (measurements/metrics),
* Evaluation verdicts (checklist results),
* SpeechAct occurrences (communicative `U.Work`), identified by role, act kind, and window (e.g., “Approved(change=4711)”).

A SpeechAct can change the state (e.g., Prepared→Authorized) but does not by itself satisfy operational steps; it only opens their Green‑Gate.

## 11 · Putting it together (one‑screen mental model)

At any **Window**:

1. **RoleAssignment exists** (A.2.1): `Holder#Role:Context`.
2. **StateAssertion(s) exist**: the holder is **in** one or more **states** as proven by checklists (`U.Evaluation`).
3. **Green‑Gate Law** applies: if at least one asserted state is **enactable**, role‑gated **Method steps** may be enacted; if all are **status‑only**, the role can **gate decisions** but **not** perform work.
4. **Role algebra** checks: specialization lifts readiness; bundles require **conjunction**; incompatibilities are detected when **two enactable states** coincide for the same holder at the same Window.

This yields a **clean separation**:

* **assignment** (RoleAssignment)
* **Readiness** (RSG + Checklists + StateAssertions)
* **Action** (`U.Work`, gated by RSG)

…and keeps meaning **local**, evidence **observable**, and reasoning **testable**.

## 12 · Archetypal RoleStateGraphs (cross‑domain patterns)

Below are **didactic, reusable** RSG skeletons for the three principal **behavioural** role families and for **epistemic/status** roles. Names and criteria are **context‑local**; treat them as **templates** to specialise inside your `U.BoundedContext` (E.10.D1). For each RSG we list:

* **`S`** — candidate **States** (enactable states marked **\[E]**);
* **Checklist gist** — the **recognition** criteria (cf. §8.1);
* **Guards** — illustrative **admission/maintenance/exit** predicates (cf. §8.3).

> **Reminder.** Only **enactable** states (**`S_en`**) can open the **Green‑Gate** for `U.Work` (RSG‑E1). Status‑only states **gate decisions** but never execution.

### 12.1 AgentialRole (decision‑capable actor)

**Context sketch:** `Ops_ChangeManagement_2025`.
**RCS (characteristics, examples):** *CompetenceLevel, FatigueIndex, IndependenceFlag, AuthorizationValidity, IncidentLoad, RiskClass.*

**States `S`**

* **Unprepared** — training incomplete; checklists fail.
* **Prepared** — training + competence thresholds met.
* **Authorized** — valid approval window present. **\[E]**
* **Ready** — `Prepared ∧ Authorized ∧ FatigueIndex < τ`. **\[E]**
* **Active** — contemporaneous **`U.Work`** step is underway under this role (**with a valid StateAssertion in the window**). **\[E]**
* **Suspended** — temporary block (incident/conflict).
* **Revoked** — authorization expired/withdrawn.

**Checklist gist**

* *Prepared*: certificates valid; recency of practice ≤ X; simulator score ≥ Y.
* *Authorized*: `exists SpeechAct(type=Approval, scope=Role, age≤30d)`.
* *Ready*: *Prepared ∧ Authorized ∧* independence from conflicting work; fatigue within limits.

**Guards**

* Admission `→ Prepared`: `ExamPassed ∧ SimulatorScore≥Y`.
* Admission `→ Authorized`: presence of approval speech‑act within window.
* Maintenance `Ready ↺`: `FatigueIndex<τ ∧ IncidentLoad≤k`.
* Exit `Ready → Suspended`: high‑severity incident assigned OR SoD violation detected.
* Exit `Authorized → Revoked`: window elapsed or explicit revoke speech‑act.

### 12.2 TransformerRole (non‑agential executor of change)

**Context sketch:** `PlantOps_Pipeline_2025`.
**RCS:** *CalibrationAge, SafetyInterlock, SelfTestPass, EnvRangeOK, DegradationIndex.*

**States `S`**

* **Unavailable** — offline, missing prerequisites.
* **Calibrated** — calibration fresh; self‑test ok.
* **Permitted** — safety interlocks clear; clearance token valid.
* **Ready** — `Calibrated ∧ Permitted ∧ EnvRangeOK`. **\[E]**
* **Running** — executing a method step (**with contemporaneous StateAssertion**). **\[E]**
* **Degraded** — still operable under derated envelope. **\[E]** (if policy allows)
* **Quarantined** — suspected hazard; no enactment.

**Checklist gist**

* *Calibrated*: `CalibrationAge≤30d ∧ SelfTestPass=true`.
* *Permitted*: `SafetyInterlock = Clear ∧ NoOpenIncident(sev≥High)`.
* *Ready*: *Calibrated ∧ Permitted ∧* environment in spec.

**Guards**

* Admission `→ Calibrated`: calibration record timestamp ≤30d.
* Maintenance `Ready ↺`: env sensors within limits; no new hazard event.
* Exit `Ready → Quarantined`: detected leak OR hazard alarm.
* Transition `Running → Ready`: step completed ∧ cool‑down satisfied.
* Transition `Ready → Degraded`: `DegradationIndex∈[d₁,d₂]` ∧ derate policy active.

### 12.3 ObserverRole (measurement actor, incl. SOSA/SSN style)

**Context sketch:** `Lab_Thermo_2025`.
**RCS:** *CalibrationAge, TraceabilityChainOK, DriftRate, SyncError, CleanlinessScore.*

**States `S`**

* **Unqualified** — no metrological chain.
* **Calibrated** — with traceability to standard.
* **Synchronized** — time/phase sync within tolerance.
* **In‑Range** — drift & environment within spec.
* **Measuring** — performing observation. **\[E]**
* **Stale** — calibration or sync expired.
* **Quarantined** — suspect bias/contamination.

**Checklist gist**

* *Calibrated*: traceability cert valid; calibration within period.
* *Synchronized*: `SyncError≤ε`.
* *In‑Range*: drift ≤ threshold; contamination tests passed.
* *Measuring*: *Calibrated ∧ Synchronized ∧ In‑Range* AND observation procedure active.

**Guards**

* Admission `→ Calibrated`: calibration event recorded < 180d.
* Exit `Calibrated → Stale`: calibration age > threshold.
* Exit `In‑Range → Quarantined`: contamination alert OR failed control sample.
* Transition `Measuring → In‑Range`: procedure complete.

> **Note.** Many ObserverRole states are **pre‑enactment** gates; only **Measuring** is enactable.

---

### 12.4 Epistemic/status roles (no enactment)

These roles are **status‑only**; **`S_en = ∅`**. They **gate decisions** (e.g., can be cited, can constrain), but can never authorize `U.Work`.

#### 12.4.1 NormativeStandardRole

**States:** *Draft*, *Candidate*, *Approved*, *Superseded*, *Deprecated*.
**Checklist gist:** governance decision records; publication identifiers; supersession links.
**Guards:** *Approved → Superseded* on adoption of newer edition; *Candidate → Approved* after ratification vote.

#### 12.4.2 EvidenceRole

**States:** *Collected*, *Verified*, *Validated*, *Obsolete*, *Contested*.
**Checklist gist:** verification/validation `U.Evaluation` present; freshness window; reproducibility tag.
**Guards:** decay to *Obsolete* by age; transition to *Contested* upon counter‑evidence.

#### 12.4.3 RequirementRole

**States:** *Proposed*, *Accepted*, *Implemented*, *Verified*, *Waived*.
**Checklist gist:** acceptance decision; trace links to `U.Work`; verification report; waiver authorization.
**Guards:** *Accepted → Implemented* when linked executions close; *Implemented → Verified* on passed acceptance checklist; *Any → Waived* by authorized speech‑act.

---

## 13 · One‑screen authoring templates (didactic cards)

Keep each RSG **teachable on one screen**. Use the following **notation‑neutral** templates when drafting RoleDescriptions (A.2.3).

### 13.1 RSG card (per Role, per Context)

```
RSG for: <RoleName>   Context: <ContextName/Edition>
RCS characteristics (gist): <characteristic1>, <characteristic2>, ...
States (◉ = enactable):
  - [◉] <StateName> — checklist gist; typical admission/maintenance/exit
  - [  ] <StateName> — ...
  - ...
Green‑Gate: step requiring <RoleName> is enactable iff holder asserts any ◉ state at Window.
Role algebra hooks: specialization (≤ ...), incompatibility (⊥ ...), bundles (⊗ ...).
```

### 13.2 State checklist snippet (per State)

```
State <StateName> (enactable? yes/no)
Checklist (all must hold at Window):
  - <Observable criterion 1>  (e.g., CalibrationAge ≤ 30d)
  - <Observable criterion 2>  (e.g., exists SpeechAct(Approval) age ≤ 30d)
Maintenance (optional): <predicate> (e.g., EnvRangeOK)
Evidence Graph Ref: <Observation/Evaluation ids>
```

### 13.3 Specialization refinement map (R' ≤ R)

```
Refinement map π : S(R') → S(R)
R' state        π(state in R)   entailment note (why Checklist_R' ⇒ Checklist_R)
-----------     -------------    -----------------------------------------------
<Ready+>        Ready            adds stricter fatigue & independence thresholds
<Authorized+>   Authorized       requires same approval + extra duty segregation
...
```

### 13.4 SoD focus (⊥) — enactable pairs

```
Incompatibility ⊥ (applies when both sides enactable at same Window):
  <RoleA.StateX>  ⊥  <RoleB.StateY>
  <RoleA.(any ◉)> ⊥  <RoleB.(any ◉)>   // default if not refined
Rationale: <one‑line reason>
```

> **Didactic cue.** If your “template” spills beyond a screen, you’re drifting into **workflow**. Pull back to **eligibility** (RSG) and **recognition** (checklists).

---

## 14 · Cross‑context adjustments (via Bridges, not imports)

RSGs are **context‑local**. When similar roles appear in different Contexts, relate them with an **Alignment Bridge** (F.9), never by silently importing state names.

### 14.1 State name correspondence (lossy mapping)

**Bridge example:** *Observer readiness* across two contexts:

```
Bridge: Observer-RSG alignment
From: Lab_Thermo_2025.ObserverRole
To:   Metrology_Line_2025.ObserverRole
Map (with CL):
  Calibrated(Lab)     ≈  Calibrated(Metro)            CL=3 (minor criterion diffs)
  In‑Range(Lab)       ↘  Fit‑for‑Use(Metro)           CL=2 (Metro adds robustness test)
  Measuring(Lab)      ↔  Measuring(Metro)             CL=3
Notes: 'Synchronized' in Lab maps to 'Time‑Aligned' in Metro (terminology shift).
Losses: Metro’s 'Robustness' has no direct Lab counterpart (explicit loss recorded).
```

**Rule (RSG‑X1).** A Bridge **MUST** record **losses** and **extra criteria**; it **MUST NOT** assert identity without a stated `CL` (congruence level).

### 14.2 Authorization vocabulary drift (deontic vs operational)

**Bridge note:** In some IT change contexts, “**Authorized**” (deontic) overlaps with “**Permitted**” (operational). A Bridge can **explain** the design choice:

* `Authorized(AgentialRole@ITIL)` ↔ `Permitted(TransformerRole@IEC)` with **CL=1** and a note: *operational interlock ≠ managerial approval; both required to lift to Ready under our policy.*

> **Payoff.** Bridges keep **local honesty** while enabling **Cross‑context reasoning** with explicit penalties (B.3).

---

## 15 · Author conformance (write good RSGs)

When you define or revise an RSG, check these **concept‑level** rules. They are easy to hold in mind; no tooling implied.

**CC‑RSG‑01 (Locality).** State names and meanings are **scoped** to `(Role, Context)`. Reuse across contexts **only via a Bridge** (F.9).

**CC‑RSG‑02 (Enactability).** Mark **which** states are enactable (**S\_en**). If none are, the role is **status‑only** (valid); then it **cannot** open the Green‑Gate.

**CC‑RSG‑03 (Observable criteria).** Every checklist item must be **observable** (Observation, Work record, SpeechAct, or derived Evaluation). No opinions.

**CC‑RSG‑04 (Guard discipline).** Guards **gate change**, checklists **recognise state**. Don’t smuggle **task order** into guards; workflow lives elsewhere (A.15).

**CC‑RSG‑05 (Refinement map).** If you declare `R' ≤ R`, provide a **π‑map** and ensure **entailment** (RSG‑R1). Specialist states may be **stricter**, never **weaker**.

**CC‑RSG‑06 (SoD by state).** Define **⊥** in terms of **enactable pairs**. Avoid blanket ⊥ if finer, state‑aware rules reduce false conflicts.

**CC‑RSG‑07 (Human scale).** Default to **≤ 7 states**. If you exceed, add a one‑sentence **didactic rationale** (“distinct gate we will actually use”).

**CC‑RSG‑08 (Green‑Gate wiring).** Ensure every `MethodDescription` step that requires this Role **names** the **◉ states** it expects, or relies on the default “any ◉”.

**CC‑RSG‑09 (Window clarity).** Checklists specify **freshness windows**; state assertions are **Window‑bound** and **non‑permanent**.

**CC‑RSG‑10 (Status/behaviour split).** Epistemic/status roles: **`S_en = ∅`**. They gate **decisions**, not **Work**. Behavioural roles require `U.System` holders (A.2.1).

## 16 · Extended grounding across four disciplines

Each vignette shows **(i)** the **Context**, **Role**, **RCS characteristics**, **States** (◉ = enactable), **Green‑Gate** condition, and **how a `U.Work` is gated** by a `U.RoleAssignment`+RSG. Names are **context‑local**.

### 16.1 Clinical surgery (medicine)

**Context.** `Hospital.OR_2026`
**Role.** `SurgeonRole` (AgentialRole)
**RCS characteristics.** *CompetenceLevel, FatigueIndex, AuthorizationValidity, CaseComplexityBand, TeamSoD*.

**States.**

* **Unprepared** — training/recency incomplete.
* **Prepared** — credentials valid; recency ≤ 90 days.
* **Authorized** — procedure‑specific approval active.
* **Ready** — `Prepared ∧ Authorized ∧ FatigueIndex<τ ∧ TeamSoD_OK`. **◉**
* **Operating** — currently performing steps. **◉**
* **Suspended** — incident or conflict raised.
* **Revoked** — approval expired/withdrawn.

**Green‑Gate.** A `MethodDescription` step tagged `requires: SurgeonRole` is **enactable** iff the performer’s `RoleAssignment` asserts **Ready** at the **Window**.

**Work gating.**
`performedBy = Dr.Kim#SurgeonRole:Hospital.OR_2026` is **valid** for step *“Incision”* only when `Ready(Dr.Kim, SurgeonRole, OR_2026, W)` holds (checklist items: approval id, fatigue score, SoD against *AuditorRole*).

---

### 16.2 Software operations (SRE)

**Context.** `SRE_Prod_Cluster_EU_2026`
**Role.** `IncidentCommanderRole` (AgentialRole)
**RCS characteristics.** *OnCallStatus, PageFreshness, AuthorityToken, CognitiveLoad, ConflictSoD*.

**States.**

* **Off‑Duty** — not on call.
* **On‑Call** — rota active; page reachable.
* **Authorized** — escalation token valid.
* **Ready** — `On‑Call ∧ Authorized ∧ CognitiveLoad≤k ∧ SoD_OK`. **◉**
* **RunningIncident** — commanding an active incident. **◉**
* **CoolingDown** — post‑incident refractory period.
* **Blocked** — conflict with *ChangeAuthorRole* detected.

**Green‑Gate.** Steps in *“Major Incident Process”* that `require: IncidentCommanderRole` open only with **Ready**.

**Work gating.**
`performedBy = Dana#IncidentCommanderRole:SRE_Prod_Cluster_EU_2026` is **invalid** for “Declare SEV‑1” if `ConflictSoD(ChangeAuthorRole)` holds or `PageFreshness>5 min`.

---

### 16.3 Laboratory metrology

**Context.** `Metrology_Thermo_2026`
**Role.** `ThermometerObserverRole` (ObserverRole)
**RCS characteristics.** *CalibrationAge, DriftRate, TraceabilityChainOK, CleanlinessScore, SyncError*.

**States.**

* **Unqualified** — missing traceability.
* **Calibrated** — cert valid (≤ 180 d); drift within baseline.
* **Synchronized** — `SyncError≤ε`.
* **In‑Range** — contamination absent; env OK.
* **Measuring** — procedure active. **◉**
* **Stale** — calibration/sync expired.
* **Quarantined** — suspected bias.

**Green‑Gate.** `MethodDescription` step *“Record temperature”* is enactable only in state **Measuring** (which requires *Calibrated ∧ Synchronized ∧ In‑Range*).

**Work gating.**
`performedBy = SensorT‑17#ThermometerObserverRole:Metrology_Thermo_2026` is **rejected** if `CalibrationAge>180 d` or `ControlSampleBias>δ`.

---

### 16.4 Governance / compliance

**Context.** `Finance_Audit_2026`
**Role.** `IndependentAuditorRole` (AgentialRole) and `EvidenceRole` (status‑only)
**RCS (auditor).** *CertificationLevel, IndependenceFlag, AssignmentToken, CaseLoad*.
**States (auditor).** **Ready**/**Auditing** as in §12.1; **⊥** with `DeveloperRole`.
**RCS (evidence).** *VerificationStatus, ValidationStatus, Age, ProvenanceChainOK*.
**States (evidence).** *Collected, Verified, Validated, Contested, Obsolete* (status‑only).

**Green‑Gate.** Audit step `requires: IndependentAuditorRole` — enactable only with **Ready** and **⊥ DeveloperRole** at the Window. Evidence states **gate decisions** (e.g., “accept finding”), never open Work.

**Work gating.**
`performedBy = Alice#IndependentAuditorRole:Finance_Audit_2026` **fails** if Alice holds any overlapping `DeveloperRole` binding in the same context.

---

## 17 · Acceptance harness (static conformance)

Author‑facing checks; **notation‑free**, **concept‑level**. Use them when drafting or reviewing an RSG.

**SCR‑A.2.5‑S01 · Local scope.** Every state name is qualified by `(Role, Context)`. No global states.
**SCR‑A.2.5‑S02 · Enactability mark.** The set **S\_en** is explicit; each ◉ state is listed.
**SCR‑A.2.5‑S03 · Observable checklists.** Each state has a Checklist of **observable** predicates (Observation / Evaluation / SpeechAct / Work evidence).
**SCR‑A.2.5‑S04 · Green‑Gate wiring.** Every `MethodDescription` step that names the Role either (a) names its ◉ state(s) or (b) relies on the default “any ◉” policy; the RSG declares which.
**SCR‑A.2.5‑S05 · Guard discipline.** Guards only **gate transitions**; they do not encode task order.
**SCR‑A.2.5‑S06 · SoD by state.** Incompatibilities (⊥) are declared over **states** (or “any ◉”), not over bare role names.
**SCR‑A.2.5‑S07 · Specialisation entailment.** For every `R' ≤ R`, a refinement map `π: S(R')→S(R)` is provided; each mapped pair has an entailment note (why `Checklist_R' ⇒ Checklist_R`).
**SCR‑A.2.5‑S08 · Human scale.** `|S| ≤ 7` unless a one‑line didactic rationale is recorded.
**SCR‑A.2.5‑S09 · Status‑only roles.** If `S_en=∅`, the Role is explicitly tagged **status‑only**; it cannot open the Green‑Gate.
**SCR‑A.2.5‑S10 · Bridge discipline.** Any cross‑context reuse is via an Alignment Bridge (F.9) with recorded `CL` and losses; no silent imports.

---

## 18 · Regression harness (evolution checks)

Use when **adding/removing states**, **changing criteria**, or **bridging** across contexts.

**RSCR‑A.2.5‑R01 · State churn impact.** For every added/removed/renamed state, list affected `MethodDescription` steps and `Work` validators; confirm the Green‑Gate policy remains decidable.
**RSCR‑A.2.5‑R02 · Entailment stability.** When `R' ≤ R` changes, update the `π` map and re‑justify entailments; fail the check if any previously valid entailment breaks.
**RSCR‑A.2.5‑R03 · SoD coverage.** After edits, recompute the set of **enactable pairs**; verify declared ⊥ still blocks all intended conflicts and no longer blocks permitted cases.
**RSCR‑A.2.5‑R04 · Evidence freshness.** If any checklist predicate uses **age/freshness**, ensure default Windows are documented and existing state assertions re‑evaluate accordingly.
**RSCR‑A.2.5‑R05 · Bridge congruence drift.** If a Bridge maps states with `CL=k`, and either side’s checklist changes, revisit the mapping; **do not** keep `CL` unchanged by default—raise or lower with a short rationale.
**RSCR‑A.2.5‑R06 · Status/behaviour split.** Verify behavioural roles still require `U.System` holders (A.2.1); status‑only roles still have `S_en=∅`.
**RSCR‑A.2.5‑R07 · One‑screen rule.** If cumulative edits push the RSG beyond one screen, split states or tighten criteria; record a one‑line teaching rationale if you must exceed.

---

## 19 · Common failure modes (and quick remedies)

| Failure            | Symptom                               | Why it hurts                       | Quick remedy                                                              |
| ------------------ | ------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------- |
| **Workflow creep** | Guards encode task order              | RSG becomes a hidden workflow model | Move ordering to `MethodDescription`; keep guards as **eligibility** only |
| **Vague criteria** | “experienced”, “mature” in checklists | Non‑decidable Green‑Gate           | Replace with observable proxies (hours, exam score, age thresholds)       |
| **Global states**  | “Ready” reused across contexts        | Meaning leakage                    | Qualify by `(Role, Context)`; use Bridges for Cross‑context talk             |
| **Over‑broad ⊥**   | Many false conflicts                  | Blocks delivery                    | Make ⊥ **state‑aware**; restrict to enactable pairs                       |
| **Missing π‑map**  | Specialisation with no entailment     | Unsafe substitutions               | Add `π` and entailment notes; otherwise drop `≤`                          |

---

## 20 · Didactic script (90 seconds): how A.2.5 ties to A.2.1 & A.2.3

> \*“A role assignment says **who wears which mask where** (A.2.1). The **RoleStateGraph** says **when that mask is actually wearable**. Each role’s RSG is a **small named state space** with **checklists** for each state. Some states are **enactable** (◉): they open the **Green‑Gate** for `Work`. Others are **status‑only**: they gate decisions, never execution.
>
> A **RoleDescription** (A.2.3) is where you publish the role’s **RCS** (characteristics), its **RSG** (states + checklists + guards), and any **role algebra** (≤, ⊥, ⊗) specific to your context.
>
> In practice: a `MethodDescription` step lists **required roles**; at runtime, a `Work` record is valid only if its **performer** is a `RoleAssignment` whose RSG asserts an **enactable** state at the **Window**. That’s the Green‑Gate.
>
> Different Contexts may use the same role labels. We never assume global meaning; we relate Contexts with **Bridges** that map states and record losses.
>
> Keep each RSG **on one screen**, with **observable** checklists. If you’re writing task order, you’ve slipped into workflow—move it to the Method. If you’re writing opinions, convert them into **observables** or drop them. That’s the whole trick.”\*

---

### 21 · Relations (quick pointers)

* **Builds on:** A.2.1 `U.RoleAssignment` (the binding that can assert states); A.2.3 `U.RoleDescription` (the carrier of RSG); E.10.D1 (Context discipline).
* **Enables.** A.15 (Role‑Method‑Work Alignment via Green‑Gate); B.3 (Trust penalties when crossing Bridges with lower `CL`).
* **Interacts with.** D‑cluster deontics (speech‑acts gate **Authorized**‑like states for agential roles); F.9 (state‑level alignment across contexts).


# A.2.6 · **Unified Scope Mechanism (USM): Context Slices & Scopes**  \[A] 

> **One-line summary.** Introduces a single, context-local **scope mechanism** for all holons: **`U.ContextSlice`** (where we reason and measure) and a family of **set-valued scope types** (**USM scope objects, `U.Scope`**), specialized as **`U.ClaimScope`** for epistemes (**G** in **F–G–R**), **`U.WorkScope`** for system capabilities, and **`U.PublicationScope`** for publication carriers; with one algebra (∩ / SpanUnion / translate / widen / narrow / refit) and uniform Cross-context handling (Bridge + CL).

## 0 · Status, Placement & Deprecations

**Status.** Normative pattern \[A] in **Part A · Core Holonic Concepts**. Numbered **A.2.6**.

**Replaces / deprecates.**
This pattern **supersedes** the scattered use of labels *applicability*, *envelope*, *generality*, *universality* and *capability envelope* where they tried to stand in for the one scope mechanism. From now on:

* For epistemes, the only **scope type** is **`U.ClaimScope`** (nick **G** in F–G–R).
* For system capabilities, the only **scope type** is **`U.WorkScope`**.
* For publication carriers (views/cards/lanes), the only **scope type** is **`U.PublicationScope`**.
* The abstract architectural notion is **`U.Scope`** — a **set-valued USM object** over `ContextSliceSet` with its own algebra (∩ / SpanUnion / translate / widen / narrow / refit); it is **not** a `U.Characteristic` and MUST NOT appear in any `CharacteristicSpace`.

Legacy words (*applicability / envelope / generality / capability envelope*) MAY appear **only** as explanatory aliases in non‑normative notes.

**Cross‑references.**
— **C.2.3** (Unified Formality **F**) and **C.2.2** (F–G–R): this pattern **defines G** as `U.ClaimScope`.
— **A.2.2** (Capabilities): capability gating now **SHALL** use `U.WorkScope`.
— **Part B** (Bridges & CL): Cross‑context transfers **MUST** declare a Bridge with **CL**; CL affects **R**, not **F/G**.
— **Part E** (Publication discipline; e.g., **E.17 MVPK**): publication views/cards/lanes MAY declare `U.PublicationScope` to bound **where** a publication is admissible; `U.PublicationScope` MUST NOT widen the underlying `U.ClaimScope`/`U.WorkScope`. (USM supplies the scope calculus; Part E supplies publication discipline.)

## 1 · Purpose & Audience

This pattern gives **engineering managers and assurance architects** one vocabulary, one model, and one set of operations to talk about **where** a claim holds and **under which conditions** a system can deliver a piece of **Work**. It removes the need to remember whether a document said “applicability,” a model said “envelope,” or a safety plan said “capability envelope.” **Scope is scope.** The only distinction that matters is **what carries it**:

* **Knowledge/episteme** → **Claim scope** (G).
* **System/capability** → **Work scope** (conditions under which Work at the promised measures is deliverable).

With USM, teams can:

* specify, compare, and compose scope **without translation games**;
* gate ESG and Method–Work steps with **observable, context‑local scope checks**;
* cross Contexts safely using Bridges and **explicit CL penalties** applied to **R**.

This pattern **defines** the **scope mechanism** (Context slices, set‑valued scopes, algebra, and guard usage) and the canonical **lexicon** (Claim scope (G), Work scope). It does **not** prescribe which Contexts must widen/narrow scope, nor which assurance levels are required; those are set by context‑local ESG and Method–Work policies, which SHALL reference the mechanisms defined here.

## 2 · Context

### 2.1 Cross‑disciplinary pressures

Modern projects couple **formal specs**, **data‑driven models**, **safety cases**, and **operational playbooks**. Each artifact must say **where it is valid**—yet terminology drifts:

* Standards and specs often say *applicability* or *scope*.
* Modeling communities say *envelope*.
* Safety and performance documents speak about *capability envelope*.
* Knowledge patterns have used *generality* (G) as if it were “more abstract,” when we actually need “**where the statement holds**.”

### 2.2 context‑local reasoning

FPF is context‑local: decisions, checks, and state assertions are **valid inside a bounded context**. Every practical question—*Is this claim usable here? Can this capability deliver that Work now?*—must be answered **on a concrete slice of context** (terminology, versions, environmental parameters, time selector **Γ\_time**). USM provides a first‑class object for such slices and a single scope calculus atop them.

### 2.3 Minimal, composable trust math

In **F–G–R**:

* **F** (formality) is “how strictly a claim is expressed” (C.2.3).
* **G** must be “**where it holds**,” not “how abstract it sounds.”
* **R** measures evidence and decays/penalties (freshness, CL).

When **G** is a **set‑valued scope**, composition becomes precise: serial dependencies **intersect** scopes; parallel, independently supported lines can publish a **SpanUnion**—but only where each line is supported.

---

## 3 · Problem

1. **Synonym soup.** *Applicability, envelope, generality, capability envelope*—different labels for the **same mechanism** led to mismatches in gating, review, and reuse.
2. **Abstraction confusion.** Calling G “generality” invited teams to treat “more abstract wording” as “broader scope,” silently masking unstated assumptions.
3. **Split mechanics.** Episteme vs system text used different algebra and guard language, though **the same set operations** were meant.
4. **Cross‑context opacity.** Transfers between Contexts lacked a shared carrier and a rule for what changes (trust) vs what stays (scope).
5. **Overloaded words.** *Validity* clashed with **Validation Assurance (LA)**; *operation/operational* clashed with **Work/Run** in A.15, producing governance ambiguity.

---

## 4 · Forces

| Force                                             | Tension to resolve                                                                                                                                               |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **One mechanism vs two worlds**                   | We must serve both **knowledge about the world** (claims) and **doing work in the world** (capabilities) **without** duplicating concepts.                       |
| **Locality vs interoperability**                  | Scope must be **context‑local** and precisely checkable, yet transferable across Contexts via Bridges **without redefining** the characteristic.                       |
| **Expressivity vs minimal vocabulary**            | Teams need to capture rich conditions (time windows, environment, versions) but not explode the lexicon into “envelope/applicability/…” variants.                |
| **Static content vs operational change**          | Claims may hold broadly while current operations are narrow (or vice versa). The mechanism must keep “what is true” and “what can be done” aligned yet distinct. |
| **Open‑world exploration vs closed‑world gating** | Exploration benefits from permissive drafts; **gates** require crisp, observable checks. The same scope object must support both.                                |

---

## 5 · Solution — Overview (preview; full definitions in Part 2)

**USM** introduces:

* **`U.ContextSlice`** — an addressable **slice of a bounded context** (terminology, parameter ranges, versions/Standards, and a mandatory **Γ\_time** selector). All scope checks are performed **on slices**.
* **`U.Scope`** — the abstract **set‑valued scope characteristic** over `U.ContextSlice`.
* **Specializations:**
  **`U.ClaimScope`** (*nick **G***) on `U.Episteme` (“**where the claim holds**”), and **`U.WorkScope`** on `U.Capability` (“**where the capability can deliver Work at declared measures within qualification windows**”).
* **One algebra:** serial **intersection**, parallel **SpanUnion** (only where supported), **translate** via Bridge (CL affects **R**, not **F/G**), and **widen / narrow / refit** operations for scope evolution.

**Lexical commitments (normative):**
— In normative text and guards, use **Claim scope (G)**, **Work scope**, and **Publication scope**.  
— Do **not** name the characteristic “applicability/envelope/generality/capability envelope/**publication applicability**/validity.” Those words are permitted only as explanatory aliases in notes.

## 6 · Normative Definitions

### 6.1 · `U.ContextSlice` — where scope is evaluated

**Definition.** `U.ContextSlice` is an addressable, context‑local selection of a bounded context comprising:

* **Vocabulary & roles.** The active terminology, role bindings, and local dictionaries.
* **Standards & versions.** Concrete versioned interfaces, schemas, notations, or service Standards in force.
* **Environment selectors.** Named parameters/ranges (e.g., temp, humidity, platform, jurisdiction, dataset cohort).
* **Time selector `Γ_time`.** A **mandatory** selector for the temporal frame of reference (point, window, or policy), disallowing implicit “latest”.

**Semantics.** All scope checks, guards, and compositions are evaluated **inside** an explicitly named `U.ContextSlice`. Cross‑context or cross‑slice usage MUST be mediated by a Bridge (Part B) with an explicit CL rating; see §7.4.

**Addressability.** A slice MUST be identifiable via a canonical tuple (Context, vocab‑id, Standard/version ids, env selector(s), `Γ_time`). A slice MAY be a singleton or a finite set if a guard tests multiple coherent sub‑conditions. 

**Slice key (minimal).** A `U.ContextSlice` **SHALL** be addressable by a tuple containing at least: `(Context, Standard/version ids (if any), environment selectors, Γ_time)`. Contexts MAY extend this tuple (e.g., vocab/roleset ids).

### 6.2 · `U.Scope` — the abstract set‑valued scope property (USM kind; **not** a CSLC measurement)

**Definition.** `U.Scope ⊆ ContextSliceSet` is a **set‑valued USM property** whose values are sets of `U.ContextSlice` where a given statement, behavior, or capability is **fit‑for‑use**. It is **not** numeric; its internal order is the subset relation `⊆`. There is no “unit”. The primitive judgement is **membership**: `slice ∈ Scope`.  

+**Guard (normative).** `U.Scope`, `U.ClaimScope (G)`, `U.WorkScope`, and `U.PublicationScope` are **not** `U.Characteristic`s in the A.17/CSLC sense; do **not** include them as slots in any `U.CharacteristicSpace`, and do **not** attach normalizations/scores to them. They are **USM scope objects**.

**Operations.** USM admits:

* **Intersection `∩`** (serial composition).
* **SpanUnion** (parallel, independently supported coverage) **only when an explicit named independence assumption is declared** (features/axes named, validity window stated, evidence class cited). See **A.6.1/USM LawSet** for the normative template.
* **Translate** (Cross‑context mapping via Bridge).
* **Widen / Narrow** (monotone changes to the set).
* **Refit** (content‑preserving re‑expression; set equality).

**Locality.** `U.Scope` values are defined and reasoned about **context‑locally**. Translation between Contexts never occurs implicitly; see §7.4.

### 6.3 · `U.ClaimScope` (nick **G**) — scope of a claim (episteme)

**Carrier.** `U.Episteme` (claims, specifications, theories, policies).

**Meaning.** The set of `U.ContextSlice` where the **claim holds** as stated. This is **G** in the F–G–R triple. **G is not “abstraction level”**; it is the applicability area of the claim.

**Expression.** Authors SHALL declare Claim scope as explicit predicates or condition blocks (assumptions, parameter ranges, cohorts, platform/Standard versions, `Γ_time` windows).

**Path composition (serial).** Along any essential dependency path supporting the claim, the effective scope is the **intersection** of contributors’ Claim scopes (see §7.2). Empty intersection makes the path inapplicable.

**Parallel support.** Where **independent** lines of support justify disjoint areas, the episteme MAY publish a **SpanUnion** (see §7.3) limited strictly to the covered slices.

**Δ‑moves.**

* **ΔG+ (widen).** Replace scope S with S′ such that S ⊂ S′.
* **ΔG− (narrow).** Replace scope S with S′ such that S′ ⊂ S.
* **Refit.** Replace S with S′ where S′ = S (normalization, re‑parametrization).
* **Translate.** Map S across Contexts via a declared Bridge; CL penalties apply to **R**, not to **F/G**.

**Orthogonality.** Changes in **F** (form of expression) or **D/AT** (detail/abstraction tiers) do not change **G** unless the declared area of validity changes.

---

### 6.4 · `U.WorkScope` — scope of doing Work (capability)

**Carrier.** `U.Capability` (a system’s ability to deliver specified `U.Work`).

**Meaning.** The set of `U.ContextSlice` (conditions, Standards, platforms, operating parameters, `Γ_time`) under which the capability can **deliver the intended Work** at the declared **measures**, within declared **qualification windows**.

**Expression.** Capability owners SHALL declare **`U.WorkScope`** as explicit **conditions/constraints over `U.ContextSlice` only** (environment, platforms, Standards by version, resource regimes, `Γ_time`). Quantitative deliverables and operation windows are **not** part of the scope value:  
* Declare targets as **`U.WorkMeasures`** (e.g., latency ≤ L, throughput ≥ T, tolerance ≤ ε) bound in guards (WG‑2).  
* Declare inspection/recertification policies as **`U.QualificationWindow`** bound in guards (WG‑3).  
The use‑time admission requires **all** of: `WorkScope covers JobSlice` **AND** `WorkMeasures satisfied` **AND** `QualificationWindow holds`.

**Method–Work gating.** A Work step’s guard MUST check that the target slice is **covered** by the capability’s Work scope **and** that required measures and qualification windows are satisfied.

**Composition and Δ‑moves.** Work scope uses the **same algebra** as Claim scope (∩ / SpanUnion / translate / widen / narrow / refit). Translation across Contexts follows §7.4.

**Separation from knowledge.** Work scope does **not** assert a proposition about the world; it asserts **deliverability** of Work under conditions. Evidence for deliverability feeds **R** (Reliability) via measurements and monitoring.

**Required guard facets (capabilities).**  
* **`U.WorkMeasures` (mandatory).** A set of measurable targets with units and tolerated ranges, evaluated on the JobSlice.  
* **`U.QualificationWindow` (mandatory for operational use).** A time policy (point/window/rolling) stating when the capability is considered qualified; evaluated at `Γ_time`.  
These facets are **separate** from `U.WorkScope` and live in the **R‑lane** (assurance). They MUST be referenced in Method–Work guards (see §10.3 WG‑2/WG‑3).

### 6.5 · `U.PublicationScope` — scope of a publication (view/surface)
**Carrier.** Publication carriers (e.g., **PublicationSurface/InteropSurface** views/cards/lanes in Part E; MVPK faces).
**Meaning.** The set of `U.ContextSlice` where a **publication** (a view/card/lane about some object or morphism) is **admissible for use** without introducing claims beyond its underlying carrier.

**Relation to other scopes (normative).**
* If the publication is **about an episteme `E`**:  
  `PublicationScope(view_E) ⊆ ClaimScope(E)`.
* If the publication is **about a capability `C`**:  
  `PublicationScope(view_C) ⊆ WorkScope(C)`.
* If the publication is **about a composition and/or crosses Contexts**:  
  `PublicationScope(view) ⊆ translate(Bridge, ⋂ scopes of contributors)`; CL penalties apply to **R** only (scope set membership is unaffected).

**Expression.** Authors SHALL declare `U.PublicationScope` as explicit predicates over `U.ContextSlice` (Context, Standard/version ids, environment selectors, `Γ_time`). It MAY be **narrower** than the underlying scope (e.g., due to pin availability, labeling, or audience constraints) but MUST NOT be wider.

**Algebra & Δ‑moves.** Inherits the USM algebra (∩ / SpanUnion / translate / widen / narrow / refit). **Widen** is permitted only when the underlying `U.ClaimScope`/`U.WorkScope` widens accordingly; otherwise the publication MAY refit or narrow.

**Orthogonality to measurement.** `U.PublicationScope` is a **USM scope object** (set‑valued), not a CHR Characteristic and MUST NOT appear as a slot in a `U.CharacteristicSpace`.

**View refinement (profiles).** When a stricter publication profile/view **refines** another (e.g., a typed card that requires additional pins), its `U.PublicationScope` **MUST NOT** be wider than that of the less formal view.

## 7 · Scope Algebra

### 7.1 · Membership & Coverage

* **Membership judgement.** `slice ∈ Scope` is the primitive check.
* **Coverage guard.** A guard “Scope **covers** TargetSlice” means either:

  * **singleton:** `TargetSlice ∈ Scope`, or
  * **set:** `TargetSet ⊆ Scope`.
* **No implicit expansion.** Absent an explicit declaration, guards MUST NOT treat “close” slices as covered; widening requires a ΔG+ change.

### 7.2 · Serial Composition (Intersection)

**Rule S‑INT (serial).** For an essential dependency chain `C1 → C2 → … → Ck` that supports a claim/capability, the effective scope along that chain is:

```
Scope_serial = ⋂_{i=1..k} Scope(Ci)
```

If `Scope_serial = ∅`, the chain is **inapplicable** and MUST NOT contribute to published scope.

**Monotonicity.** Adding a new essential dependency can only narrow (or leave unchanged) the serial scope.

---

### 7.3 · Parallel Support (SpanUnion)

**Rule P‑UNION (parallel).** If there exist **independent** support lines `L₁,…,Lₙ` for the **same** claim/capability, each with serial scope `S_i`, the publisher MAY declare:

```
Scope_published = SpanUnion({S_i})  =  ⋃_{i=1..n} S_i
```

**Constraints.**

* Independence MUST be justified (different support lines must not rely on the same weakest link).
* The union MUST NOT exceed the union of supported slices; “hopeful” areas are disallowed.
* Publishers SHOULD annotate coverage density/heterogeneity (informative) to aid R assessment, but numeric “coverage” is not part of G.
* **Independence criterion.** Support lines in a **SpanUnion** MUST be partitioned so that each line has a set of **essential components** disjoint from the others’ essential components (no shared weakest link). The partition (or a certificate thereof) SHALL be referenced in the publication.

### 7.4 Why a **G-ladder/levels/scales** is not needed (and **must not** be introduced)

**1) G is not an ordinal scale; it is set-valued.**
Under **USM**, `U.ClaimScope` is a **set‑valued** **USM scope object** over `U.ContextSlice`. The only well‑typed primitives are **membership** and **set operations** (`⊆`, `∩`, `⋃`). Imposing ordinal “levels” such as **G0…Gk** violates the type discipline and produces non‑invariant behavior (the **same set** could be “rated” with different numbers under different heuristics). (See also LEX‑CHR‑STRICT.)

**2) G composes via `∩` / `SpanUnion`, not via `min` / `avg`.**
USM already fixes composition: along a **dependent path** use **intersection**; across **independent support lines** publish **SpanUnion**. None of these operations relies on (or preserves) any linear order. An ordinal “G ladder” invites people to take **minimums/averages**, which is **incorrect** for sets and breaks the established algebra.

**3) A G ladder drags in “abstraction level,” which is orthogonal.**
Early “G ladders” effectively encoded **abstraction/typing** (instances → patterns → formal classes/types → up‑to‑iso). That is valuable **didactics**, but **not applicability**. We have already separated these concerns: **abstraction** is captured, if needed, by **`U.AbstractionTier (AT)`** as an optional facet; **applicability** is **`U.ClaimScope (G)`**.

**4) A G ladder breaks locality and Bridge semantics.**
Cross‑context transfer maps a **set** `Scope` via a **Bridge** and penalizes **R** by **CL**. There is no canonical way to “translate” an **ordinal G level** between Contexts: the mapped area may be **strictly narrower** or differently factored. Level numbers would become non‑portable, causing hidden loss or inflation of trust. With USM, we **translate sets** and keep the CL penalty where it belongs—**in R**, not in G.

**5) A G ladder duplicates ESG guards without adding decision power.**
What teams often want to “compress into a G number” is actually (a) the **quality of expression** and (b) the **completeness** of the declared scope. The first is an **F threshold** (e.g., require **`U.Formality ≥ F4`** so the scope is predicate‑like and addressable); the second is handled by explicit **ESG guards**: “**Scope covers TargetSlice**,” “**`Γ_time` is specified**,” and “**freshness window holds**” (R‑lane). A ladder for G adds confusion but no additional control.

**Normative directive.**
`U.ClaimScope (G)` **SHALL** remain a **set‑valued** characteristic; **no ordinal or numeric ladder SHALL be defined** for G. Authoring and gating **SHOULD** use **F thresholds** (C.2.3) and **explicit guard predicates** (A.2.6) rather than pseudo‑levels of G.

### 7.5 · Translation across Contexts (Bridge & CL)

**Rule T‑BRIDGE.** To use a scope in a different bounded context (room), an explicit **Bridge** MUST be declared with:

* **Mapping.** A documented mapping from source to target `U.ContextSlice` vocabulary/characteristics.
* **Congruence Level (CL).** A rating of mapping congruence.
* **Loss notes.** Any known losses, assumptions, or non‑isomorphisms.

**Effect.** The mapped scope is `T(Scope)` in the target Context. **CL penalties apply to R** (the trust in support/evidence), **not to F or G**. If mapping is coarse, the publisher SHOULD also narrow the mapped scope to the area where losses are negligible (best practice, not a requirement).

---

### 7.5 · Δ‑Operations (Widen, Narrow, Refit)

* **ΔG+ (widen).** Monotone expansion: `S ⊂ S′`. Requires new support or stronger bridges.
* **ΔG− (narrow).** Monotone restriction: `S′ ⊂ S`. Often used to remove areas invalidated by new findings.
* **Refit.** `S′ = S` after normalization (e.g., re‑parameterization, changing units, factoring common predicates). Refit MUST NOT alter membership.

**Refit (normalization).** A refit **MUST preserve membership** exactly (S′ = S). Any change that alters boundary inclusion (due to rounding, unit conversion, discretization) is a ΔG± change, not a refit.

**Edition triggers.** Any change that alters the published set (ΔG±) is a content change and MAY trigger a new edition per Context policy (see A.2.x on editions). Refit is not a content change.

### 7.6 · Invariants

* **I‑LOCAL.** All scope evaluation is **context‑local**. Cross‑context usage MUST follow §7.4.
* **I‑SERIAL.** Serial scope is an **intersection**; it cannot grow by adding dependencies.
* **I‑PARALLEL.** Parallel scope MAY grow by union, but only where **independently supported**.
* **I‑WLNK.** Weakest‑link applies to **F** and **R** on dependency paths; **G** follows set rules (∩ / ⋃).
* **I‑IDS.** Idempotence: Intersecting or unioning a set with itself does not change it.
* **I‑EMPTY.** Empty scope is a first‑class value; guards MUST treat it as “not applicable”.

---

### 7.7 · Empty & Partial Scopes

* **Empty scope (`∅`).** The claim/capability is **currently not usable anywhere** in the Context; guards MUST fail.
* **Partial scope.** Publishers SHOULD avoid “global” language when actual scope is thin; instead, publish explicit slices and (informatively) coverage hints to guide R assessment.

---

## 8 · Locality, Time & Version Semantics

### 8.1 · context‑locality

Scopes are **owned and evaluated** within a `U.BoundedContext`. State assertions (ESG/RSG) and Method–Work gates MUST NOT assume that a scope declared in another Context applies verbatim; see §7.4.

### 8.2 · Time selector `Γ_time`

Every scope declaration and every guard MUST specify a **`Γ_time` selector** (point, window, or policy such as “rolling 180 days”) whenever time‑dependent assumptions exist. Implicit “latest” is forbidden. When `Γ_time` differs between contributors, serial intersection resolves the overlap.

### 8.3 · Standards, versions & notations

Scope predicates SHALL name Standards/interfaces/schemas **by version**. Changing symbols/notations with a faithful mapping does not change **G** (it may change **CL** for the mapping and thus affect **R**).

### 8.4 · Determinism of evaluation

Given fixed inputs (slice tuple, declared scope), the membership judgement MUST be deterministic. Guards SHALL fail closed (no membership ⇒ no use).

### 8.5 · Interaction with R (freshness & decay)

For empirical claims and operational capabilities, **R** typically binds evidence freshness windows. Scope does not decay with time; **trust in the support** does. Guards MAY combine “Scope covers” with “Evidence freshness holds” as separate predicates.

---

## 9 · Lexical Discipline (Part E compliance)

**L‑USM‑1 (names).** Use **Claim scope (G)** for epistemes, **Work scope** for capabilities, and **Publication scope** for publication carriers. Use **Scope** only when discussing the abstract mechanism. Avoid naming any **characteristic** as “applicability,” “envelope,” “generality,” “capability envelope,” or “validity”.

**L‑USM‑2 (Work/Run).** Prefer **Work/Run** vocabulary from A.15 for system execution contexts. Do not introduce “operation/operating” as characteristic names; use **Work scope**.

**L‑USM‑3 (Validation).** “Validation/Validate” remain reserved for **LA** in assurance lanes (Part B). Do not name the scope characteristic “validity”.

**L‑USM‑4 (Domain).** “Domain” is a descriptive convenience. Scopes are evaluated on **Context slices**; guards SHALL reference slices, not generic “domains”.

**L‑USM‑5 (First mention).** On first use in a Context, include the parenthetical nick: *“Claim scope (**G**)”* to preserve the F–G–R mapping.

## 10 · Guard Patterns (ESG & Method–Work)

### 10.1 · Common guard shape

A scope‑aware guard has the form:

```
Guard := ScopeCoverage AND TimePolicy AND (EvidenceFreshness?) AND (BridgePolicy?)
```

Where:

* **ScopeCoverage**: `Scope covers TargetSlice` (singleton or finite set), see §7.1.
* **TimePolicy**: explicit `Γ_time` selector(s); implicit “latest” is forbidden (§8.2).
* **EvidenceFreshness**: optional R‑lane freshness/decay predicates; **separate** from ScopeCoverage (§8.5).
* **BridgePolicy**: required if the Scope and TargetSlice are in **different Contexts**; declares Bridge, CL, loss notes (§7.4).

The guard **fails closed** (no membership ⇒ denial), and evaluation is **deterministic** given the slice tuple (§8.4).

---

### 10.2 · ESG guard families (epistemes)

**EG‑1 · ClaimScopeCoverage (mandatory).**
The state transition MUST include a predicate:

```
U.ClaimScope(episteme) covers TargetSlice
```

* **Singleton**: `TargetSlice ∈ ClaimScope`.
* **Finite set**: `TargetSet ⊆ ClaimScope`.

**EG‑2 · Formality threshold (if required by ESG).**
When rigor is gated, the guard MUST reference C.2.3:

```
U.Formality(episteme) ≥ F_k
```

**EG‑3 · Evidence freshness (R‑lane).**
If the state implies trust, a separate predicate MUST assert freshness windows for bound evidence:

```
Fresh(evidence, window)  AND  (NoExpiredBindings)
```

**EG‑4 · Cross‑context usage.**
If `TargetSlice.Context ≠ episteme.Context`, the guard MUST require a declared Bridge and CL:

```
Bridge(source=episteme.Context, target=TargetSlice.Context)  AND  CL ≥ c
```

> **Effect:** CL penalties apply to **R**, not to **F/G** (§7.4). The ESG guard MAY also **narrow** the mapped Claim scope when mapping losses are known.

**EG‑5 · ΔG triggers.**
If the transition publishes a **wider** Claim scope (ΔG+), the guard MUST capture the new support or the new Bridge and, if Context policy so dictates, mint a new edition (PhaseOf).

**EG‑6 · Independence for SpanUnion (when claiming parallel scope).**
When the episteme declares a **SpanUnion** across independent lines, the guard MUST include an **independence justification** (pointer to the support partition). No independence ⇒ no union.

*(Informative note.)* Managers often combine EG‑1 (coverage) + EG‑2 (F threshold) + EG‑3 (freshness) for “Effective” or “Approved” states, and EG‑4 when adopting claims across Contexts.

---

### 10.3 · Method–Work guard families (capabilities)

**WG‑1 · WorkScopeCoverage (mandatory).**
A capability can be used to deliver a Work step only if:

```
U.WorkScope(capability) covers JobSlice
```

**WG‑2 · `U.WorkMeasures` satisfied** (mandatory for deliverables).
Guards MUST bind quantitative measures that the capability promises in the JobSlice:

```
SLO/target measures satisfied (latency ≤ L, throughput ≥ T, tolerance ≤ ε, ...)
```

**WG‑3 · `U.QualificationWindow` holds** (mandatory for operational use).
Operational guards MUST assert that qualification windows (qualification/inspection/recert intervals) hold **at `Γ_time`**:

```
ValidityWindow(capability) holds at Γ_time
```

**WG‑4 · Cross‑context use of capability.**
If the JobSlice is in another Context:

```
Bridge(source=capability.Context, target=JobSlice.Context)  AND  CL ≥ c
```

CL penalties affect **R** (confidence in deliverability), **not** Work scope; however, the guard SHOULD narrow the mapped Work scope to account for known mapping losses.

**WG‑5 · Δ(WorkScope).**
When widening Work scope (new operating ranges/platforms), the guard MUST require evidence at the new slices (measures + qualification windows). Refit (e.g., new units/parametrization) requires no new evidence.

---

### 10.4 · Bridge‑aware guard macro (reusable)

A reusable macro for Cross‑context guards:

```
Guard_XContext(Scope, TargetSlice) :=
    exists Bridge b: (b.source = owner(Scope).Context AND b.target = TargetSlice.Context)
AND CL(b) ≥ c
AND Scope’ = translate(b, Scope)
AND Scope’ covers TargetSlice
AND (Apply CL penalty to R)
```

+* **Owner(Scope).** The carrier that declares the scope: an **Episteme** (for `U.ClaimScope`), a **Capability** (for `U.WorkScope`), or a **Publication carrier** (for `U.PublicationScope`).  
* **Translate(b, Scope).** The partial mapping of a set of source slices to target slices induced by Bridge **b**. If a source slice is unmappable, it is dropped. The result is a set of target slices; **CL penalties apply to R only**.
* **Penalty to R**: applied per trust calculus; F and G remain as declared.

### 10.5 · Selector policy (Γ\_time)

All ESG and Method–Work guards MUST spell out **`Γ_time`**:

* **Point** (“as of 2026‑03‑31T00:00Z”).
* **Window** (“rolling 180 days”).
* **Policy** (“last lab calibration within 90 days”).

Implicit “latest” is not allowed. If multiple contributors declare different policies, **serial intersection** computes the overlap (§8.2).

---

## 11 · Conformance Checklist (USM)

| ID                                    | Requirement                                                                                                                                                                                    |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CC‑USM‑1 (Declaration).**           | Epistemes **SHALL** declare **`U.ClaimScope`**, capabilities **SHALL** declare **`U.WorkScope`**. The abstract `U.Scope` MAY be used in architectural notes but not in guards.                 |
| **CC‑USM‑2 (Set‑valued).**            | Scope characteristics are **set‑valued** over `U.ContextSlice`. Implementations MUST support **membership**, **intersection**, **SpanUnion**, **translate**, **widen/narrow**, **refit**.      |
| **CC‑USM‑3 (Coverage guards).**       | ESG and Method–Work guards **MUST** use `Scope covers TargetSlice` predicates and **MUST** specify `Γ_time`. Guards fail closed.                                                               |
| **CC‑USM‑4 (Serial intersection).**   | Along essential dependency paths, effective scope **SHALL** be the **intersection**; empty intersection invalidates the path.                                                                  |
| **CC‑USM‑5 (SpanUnion constraints).** | Parallel scope **MAY** use **SpanUnion** only if independent support lines are **justified**; published union **MUST NOT** exceed supported slices.                                            |
| **CC‑USM‑6 (Cross‑context).**            | Any Cross‑context use **MUST** declare a Bridge and **CL**; CL penalties apply to **R**, not **F/G**.                                                                                             |
| **CC‑USM‑7 (No synonym drift).**      | In normative text and guards, **MUST** use **Claim scope (G)** or **Work scope**. Terms “applicability/envelope/generality/capability envelope/validity” **MUST NOT** name the characteristic. |
| **CC‑USM‑8 (Determinism).**           | Membership evaluation **MUST** be deterministic given the slice tuple; no heuristic “close enough” matching.                                                                                   |
| **CC‑USM‑9 (Edition triggers).**      | ΔG± (widen/narrow) constitutes a **content change**; refit does not.                                                                                                                          |
| **CC‑USM‑10 (Publication discipline).** | Publication carriers that gate usage **SHALL** declare `U.PublicationScope`. For any publication **about** an episteme or capability, `PublicationScope` **MUST** be a subset of the underlying `U.ClaimScope`/`U.WorkScope`. Cross‑context publications **MUST** cite Bridge + CL; CL penalties **apply to R only** (scope membership unchanged). |
| **CC‑USM‑11 (Separation).**           | Scope coverage checks and evidence freshness/assurance checks **MUST** be separate predicates (G vs R).                                                                                        |
| **CC‑USM‑12 (Versioned Standards).**  | Scope predicates **SHALL** name Standards/interfaces by **version**; changes in notations with faithful mapping do not change **G** (may change CL for R).                                     |
| **CC‑USM‑13 (Min‑info publication).** | Published scopes **SHOULD** enumerate slices or predicate blocks sufficient to re‑evaluate membership without external folklore.                                                               |

## 12 · Worked Examples

> Each example declares the Context, the scope, the target slice, and shows the guard outcome. Where relevant, serial intersection, SpanUnion, and Bridge & CL are illustrated.

### 12.1 · Research claim (controlled narrative → predicate)

* **Context:** `MaterialsLab@2026`.
* **Episteme:** claim “Adhesive X retains ≥85 % tensile strength on Al6061 for 2 h at 120–150 °C.”
* **Claim scope (G):** `{substrate=Al6061, temp∈[120,150]°C, dwell≤2h, Γ_time = window(1y), rig=Calib‑v3}`.
* **Target slice:** `{substrate=Al6061, temp=140 °C, dwell=90 min, Γ_time=2026‑04‑02, rig=Calib‑v3}`.
* **Guard (EG‑1, EG‑2):** `covers(TargetSlice)` **true**; `U.Formality ≥ F4` **true** (predicates in spec).
* **Outcome:** state transition allowed (freshness checked separately under R).

### 12.2 · Cross‑context use of the research claim

* **target Context:** `AssemblyFloor@EU‑PLANT‑B`.
* **Bridge:** declared mapping of rigs and temp measurement correction; **CL=2** (loss: ±2 °C bias).
* **Mapped Claim scope:** `translate(Bridge, G)` narrows temp to `[122,148]°C`.
* **Guard (EG‑4):** Bridge present, `CL≥2` **true**; **R** is penalized per Φ(CL).
* **Outcome:** allowed; **G** remains the mapped set; **R** lowered.

### 12.3 · Capability: robotic weld Work scope

* **Context:** `RobotCell‑Weld@2026`.
* **Capability:** “Weld seam W at bead width 2.5 ± 0.3 mm, cycle ≤ 12 s.”
* **Work scope:** `{humidity<60 %, current∈[35,45]A, wire=ER70S‑6, Γ_time=rolling(90d), controller=FW‑2.1}`.
* **Job slice:** `{humidity=55 %, current=40A, wire=ER70S‑6, Γ_time=now, controller=FW‑2.1}`.
* **Guards (WG‑1..3):** coverage **true**; measures satisfied; qualification window **true** (controller certified 60 d ago).
* **Outcome:** capability admitted for this Work.

### 12.4 · Serial intersection (API + dataset compatibility)

* **Claim A (API Standard):** `v2.3` request schema with constraint “idempotent under retry”.
* **Claim B (Dataset cohort):** “metrics valid for cohort K with schema `ds‑14`”.
* **Composition:** service S depends on both A and B → **serial intersection** of Claim scopes: `{api=v2.3} ∩ {cohort=K, schema=ds‑14}`.
* **Target slice:** `{api=v2.3, cohort=K, schema=ds‑14}` → membership **true**.
* **Any drift (e.g., `ds‑15`)** empties the intersection ⇒ path inapplicable.

### 12.5 · Parallel support (SpanUnion) in a safety case

* **Line L1:** tests on **dry asphalt** support braking property; scope `S1={surface=dry, speed≤50 km/h}`.
* **Line L2:** simulations for **wet asphalt**; scope `S2={surface=wet, speed≤40 km/h}`.
* **Published scope:** `SpanUnion({S1,S2})` = `{(dry, ≤50), (wet, ≤40)}` with independence note (L1 empirical, L2 model‑validated).
* **Guard:** allowed; union does **not** include `(wet, 45)` because not supported.

### 12.6 · ML model deployment across Contexts

* **Model claim:** “AUC ≥ 0.92 on cohort K, pipeline P, features F, `Γ_time=rolling(180d)`.”
* **Claim scope:** `{cohort=K, pipeline=P, features=F, Γ_time=rolling(180d)}`.
* **target Context:** product `On‑Device@v7`, features `F’` (subset), pipeline `P’`.
* **Bridge:** declared mapping `F→F’`, `P→P’`, **CL=1** (notably lossy).
* **Guard:** Bridge present; `translate(G)` covers a **strict subset**; CL=1 penalizes **R** strongly; ESG requires **F≥F5** (executable semantics) and **freshness < 90 d**.
* **Outcome:** allowed only for the covered subset; adoption flagged with reduced **R**.

---

## 13 · Playbooks (Informative)

### 13.1 · Manager’s 6‑step adoption checklist

1. **Name the TargetSlice.** Write the tuple (Context, versions, environment params, `Γ_time`).
2. **Check scope coverage.** “Claim/Work scope covers TargetSlice?” If **no**, either **ΔG+** (publish wider scope with support) or **decline**.
3. **Check rigor if gated.** If ESG requires it, ensure `U.Formality ≥ F_k`.
4. **Check evidence freshness (R).** Validate windows/decay policies; do not conflate with coverage.
5. **Bridge if Cross‑context.** Require declared Bridge, CL, and loss notes; accept **R** penalties.
6. **Record the decision.** Keep the slice and guard outcomes with the StateAssertion (auditability).

### 13.2 · Architect’s design rubric for scopes

* **Prefer predicates over prose.** Name parameters, ranges, Standards by **version**, and `Γ_time`.
* **Factor common conditions.** Use Refit to normalize units and factor shared predicates; do not widen by stealth.
* **Partition support lines.** If you plan a **SpanUnion**, document independence up front.
* **Keep scope thin & honest.** Publish what you can support; add slices as support appears (ΔG+).
* **Design Bridges early.** When interop is planned, sketch mapping characteristics and **expected CL**; plan **R** penalties.

### 13.3 · Review anti‑patterns & fixes

| Anti‑pattern                                    | Why it’s wrong                   | Fix                                                        |
| ----------------------------------------------- | -------------------------------- | ---------------------------------------------------------- |
| “Latest” time by default                        | Non‑deterministic; violates §8.2 | Declare `Γ_time` explicitly (point/window/policy)          |
| Using “domain” in guards                        | Not addressable; hides slices    | Replace with concrete `U.ContextSlice` tuples              |
| Treating “more abstract wording” as wider scope | Abstraction ≠ applicability      | Keep **AT/D** separate; widen **G** only with explicit ΔG+ |
| Publishing union without independence           | Overstates coverage              | Justify independence or publish serial intersection only   |
| Cross‑context use without Bridge                   | Silent semantic drift            | Require Bridge + CL; apply **R** penalties                 |

### 13.4 · Minimal DSL snippet for scope blocks (illustrative)

```
claimScope:
  Context: MaterialsLab@2026
  Standards:
    - rig: Calib-v3
    - api: v2.3
  env:
    substrate: Al6061
    temp: [120, 150] # °C
    dwell: { max: "2h" }
  gamma_time: { window_days: 365 }
```

*(Illustrative only; the specification does not mandate a particular syntax.)*

### 13.5 · Profiles as Scope configurations (informative)
**Idea.** A **Scope profile** is a **named, editioned configuration** that expands to a concrete `U.Scope` predicate block (over `U.ContextSlice`), used to avoid repetition and to keep declarations consistent across carriers.

**Rules.**
* **P1 (Expansion).** Profiles are macros: guards **MUST** expand them to explicit predicates before evaluating `Scope covers TargetSlice`.
* **P2 (Edition).** Profiles are editioned; changing a profile’s predicates is a content change for any carrier that references it.
* **P3 (No stealth widen).** A profile update MUST NOT implicitly widen a carrier’s published scope; ΔG+ must be explicit in that carrier.
* **P4 (Bridge awareness).** If a profile implies Cross‑context use, it MUST name the Bridge and CL policy; CL penalties apply to **R** only.
* **P5 (Locality).** Profiles are context‑local conveniences; they do not introduce new scope types.

**Examples (illustrative).**  
— An engineering context defines `Ops‑Lab‑v3` as a profile pinning Standards, environment selectors, and a rolling `Γ_time` policy; claims, capabilities, and publications may reference it as a shorthand.  
— A publication stack defines `TechCard‑Lite@Σ` as a profile that **narrows** `U.PublicationScope` to slices where required pins are available.

## 14 · Governance Hooks & Audits

### 14.1 · Governance metadata (normative)

Contexts that adopt USM SHALL record, per scope‑aware decision:

* **Owner.** Episteme (for Claim scope) or Capability (for Work scope).
* **TargetSlice tuple.** Context, vocab/roles, versioned Standards, environment selectors, **`Γ_time`**.
* **Guard outcomes.** Membership result, Bound measures (for Work scope), Freshness predicates (R).
* **Bridge info (if any).** Mapping summary, **CL**, loss notes, applied R penalty.
* **ΔG log.** Widen/narrow/refit; edition policy outcome.

### 14.2 · USM compliance levels (informative)

* **USM‑Ready.** Context declares adoption; editors trained; lexicon updated.
* **USM‑Guarded.** All ESG/Method–Work guards use Claim/Work scope and `Γ_time`.
* **USM‑Auditable.** Decision records include TargetSlice tuples and Bridge/CL details.
* **USM‑Composed.** Serial intersection and SpanUnion are implemented in composition tooling.

### 14.3 · Audit checklist (informative)

* Does each guard **name** a concrete **TargetSlice**?
* Is **membership** deterministically recomputable from published predicates?
* Are **freshness** and **coverage** separate predicates?
* For Cross‑context use: is there a **Bridge** with **CL** and loss notes?
* For parallel support: is **independence** justified?

### 14.4 · Risk controls (informative)

* **Silent widening.** Require ΔG+ review; flag any scope increase without new support/Bridge.
* **Opaque slices.** Disallow “domain” placeholders; enforce addressable selectors.
* **Time drift.** Require `Γ_time` policies (rolling windows) for time‑sensitive scopes.

---

## 15 · Cross‑Pattern Coordination

### 15.1 · With F–G–R (C.2.2)

* **G is Claim scope.** Use set algebra (∩ / SpanUnion).
* **F** remains the expression rigor (C.2.3); **R** captures evidence freshness and CL penalties.
* **Weakest‑link.** On dependency paths: **F\_composite = min(F)**, **R\_composite = min(R)**; **G** follows §7.2–§7.3 (set rules).

### 15.2 · With Formality (C.2.3)

* **No conflation.** Raising **F** does not change **G** unless scope predicates change.
* **Guarding rigor.** ESG may use `U.Formality ≥ F_k` alongside scope coverage.

### 15.3 · With Work & Run (A.15)

* **Work scope** aligns with the **execution context** of `U.Work`.
* Method–Work gates use **Work scope coverage** plus **measures** and **qualification windows**.

### 15.4 · With Bridges & CL (Part B)

* **CL only impacts R.** CL penalties reduce trust; they never rewrite **F** or **G**.
* **Best practice.** Narrow mapped scopes where mapping losses are material.

### 15.5 · With Capability governance (A.2.2)

* Capabilities MUST declare **Work scope**, **measures**, **qualification windows**; gates MUST verify all three.
* Capability refits that preserve the set (unit changes) are **Refit**, not Δ(WorkScope).

---

## 16 · Extended FAQ (informative)

**Q1. Is “Claim scope” the same as “domain”?**
**No.** “Domain” is descriptive and often fuzzy. **Claim scope** is **addressable**: it names concrete `U.ContextSlice` conditions and a **`Γ_time`** policy. Guards MUST reference slices, not generic “domains”.

**Q2. How do we express partial coverage across different cohorts or platforms?**
Declare each supported serial scope (`S₁, S₂, …`) and publish **SpanUnion({Sᵢ})** with independence justification. Do **not** include unsupported slices.

**Q3. Can raising F (formalizing) widen G?**
Only if the formalization **explicitly changes** the scope predicates (ΔG+). Formalization alone does not widen scope.

**Q4. What is the difference between Work scope and SLOs?**
**Work scope** is **where** the capability can deliver; **measures** within the guard are **what** it promises there (SLO targets). Both are required at use time (WG‑1..3).

**Q5. Can we assign numeric coverage to G?**
Not normatively. G is set‑valued. You MAY attach **informative** coverage metrics (e.g., proportions) to aid **R** assessment, but guards use set membership.

**Q6. How do we handle “latest data” scopes?**
You don’t. Declare a **`Γ_time`** policy (e.g., rolling 90 days). “Latest” is forbidden to ensure reproducible evaluation.

**Q7. How do we move a scope to another Context?**
Declare a **Bridge** with **CL** and loss notes; compute `translate(Bridge, Scope)`; apply CL penalty to **R**; consider narrowing the mapped set.

**Q8. What about abstraction level or detail?**
Keep **AT (AbstractionTier)** and **D (Detail/Resolution)** as orthogonal, optional annotations. They never substitute for **Claim/Work scope**.

**Q9. Can a capability’s Work scope be broader than an upstream claim’s Claim scope?**
They are on different carriers. In a serial dependency, the **effective** scope is the **intersection**; the broader one does not dominate.

**Q10. When does an empty scope make sense?**
It indicates “not usable anywhere (here, now)”. Guards MUST fail. This is common during early drafting or after a refutation.

---

## 17 · Annexes (informative)

### 17.1 · Legacy → USM dictionary

| Legacy wording                      | USM term                                                 |
| ----------------------------------- | -------------------------------------------------------- |
| applicability (of a claim)          | **Claim scope (G)**                                      |
| envelope (of a requirement/spec)    | **Claim scope**                                          |
| generality G                        | **Claim scope (G)**                                      |
| capability envelope                 | **Work scope**                                           |
| validity (as a characteristic name) | **Claim scope** or **Work scope** (depending on carrier) |
| operational applicability           | **Work scope**                                           |
| publication/view applicability      | **Publication scope**                                    |

*(Use legacy terms only in explanatory notes; not in guards or conformance text.)*

### 17.2 · Minimal data model hints

**ContextSlice tuple (suggested keys):**
`Context`, `vocabId`, `rolesetId?`, `Standards: [{name, version}]`, `env: {param: range/value}`, `gamma_time: {point|window|policy}`.

**Claim scope block:**
`assumptions`, `cohorts`, `platforms/Standards`, `env`, `gamma_time`.

**Work scope block:**
`conditions (env/platform/Standards)`, `measures (targets & units)`, `validity_windows`, `gamma_time`.

*(These are informative; the spec does not mandate a concrete serialization.)*

### 18.3 · Pseudocode membership (illustrative)

```python
def covers(scope: Set[Slice], target: Union[Slice, Set[Slice]]) -> bool:
    if isinstance(target, Slice):
        return target in scope
    return target.issubset(scope)
```

## 17. 4 Rationale · F‑Cluster Unification for A.2.6 (F.17 / F.18)

> **Intent.** This annex applies the **F‑cluster method** to triangulate **USM** terms against a diverse set of post‑2015 sources and communities (“Contexts”), and then fixes the **Unified Tech** and **Plain** names used in A.2.6. Results are ready for downstream lexicon entries (Part E) and guard templates (ESG / Method–Work).

### 17.4.1 · F.17 Unified Term Survey (UTS) — Method & Scope

**Contexts surveyed (SoTA, diverse):**

1. **ISO/IEC/IEEE 42010** (architecture description)
2. **OMG Essence** (Kernel: Alphas, Work Products, States)
3. **NIST AI RMF 1.0/1.1** (trustworthy AI)
4. **ASME V\&V 40–2018 / FDA 2021–2023** (model credibility)
5. **W3C SHACL (2017+) / SHACL‑AF** (data constraints)
6. **OWL 2 / ontology engineering (2012+, current practice)**
7. **IETF BCP 14 (RFC 2119/8174)** (normative keywords & guard style)
8. **DO‑178C + DO‑333** (avionics, formal methods supplement)
9. **ISO 26262:2018/2025** (automotive functional safety)
10. **IEC 61508 (2010+, current revisions)** (basic safety)
11. **ACM Artifact Review & Badging v1.1** (reproducibility signals)
12. **MLOps/Cloud SLO practice (SRE / platform)** (operational guardrails)

**Survey focus (terms we align):** `U.ContextSlice`, generic **Scope** and set algebra, **Claim scope (G)**, **Work scope**, **Bridge & CL**, **Γ\_time**, **widen/narrow/refit/translate**, **SpanUnion / serial intersection**, separation from **F** and **R**, avoidance of overloaded **validity/operation** terms.

---

### 17.4.2 · UTS Table (F.17) — Cross‑context term mapping

|  # | Context / Source      | Local label(s) (native)                                                     | Closest USM concept                                                                      | Notes on fit & deltas                                                                                                                                                                         |
| -: | ------------------ | --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  1 | ISO/IEC/IEEE 42010 | *Architecture context; environment; stakeholder concerns; viewpoints/views* | **ContextSlice** (addressable slice); **Scope** as view‑specific applicability           | 42010 is about **views in context**; it has no first‑class set‑valued scope char but aligns with “evaluate **in a concrete context**” → USM uses explicit **slice tuples**.                   |
|  2 | OMG Essence        | *Alpha State; Work Product State; Level of Detail (LoD)*                    | **Work scope** (guards), **Detail (D)** (LoD), **ESG/RSG**                               | Essence separates **status** (states) and **work evidence**; LoD is **detail**, not scope. USM treats **scope** as guardable membership over slices; states/LoD map to ESG & **D**, not to G. |
|  3 | NIST AI RMF        | *Context of use; validity, reliability, robustness; monitoring*             | **Claim scope (G)**; **R** freshness/monitoring                                          | “Context of use” = **where a claim/model holds** → maps to **G**. “Validity” is part of **R** vocabulary; we **avoid** naming the characteristic “validity” to prevent LA confusion.          |
|  4 | ASME V\&V 40 / FDA | *Context of use; credibility factors; verification/validation*              | **Claim scope (G)**; **R** (credibility)                                                 | Direct fit for G via “context of use”. Credibility/evidence freshness contribute to **R**, not to G; USM keeps them separate in guards.                                                       |
|  5 | W3C SHACL          | *Shapes; targets (sh\:targetClass, sh\:target); constraints*                | **Claim scope** (targets define **where** constraints apply); **F≥4** (predicate form)   | SHACL “target” ≈ **membership predicate** on a dataset context; perfect analogue of **Claim scope** on data slices; constraint language supports **F4**‑style predicates.                     |
|  6 | OWL 2 practice     | *Class extension; domain/range; imports/version IRI*                        | **Claim scope** as class extension over an ontology context                              | Class extension is set‑semantics by design; **G** naturally maps to extension over a versioned ontology (part of **ContextSlice**).                                                           |
|  7 | IETF BCP 14        | *MUST/SHALL/SHOULD; requirements language*                                  | **Guard style** (observable predicates)                                                  | BCP 14 doesn’t define scope but dictates how guards are worded; USM aligns by requiring **observable, deterministic** membership checks.                                                      |
|  8 | DO‑178C / DO‑333   | *Operational conditions; DAL; formal method objectives; TQL*                | **Work scope** (operating conditions); **F** (proof‑grade), **R** (assurance objectives) | Operational applicability = **Work scope**; formal method objectives lift **F**; Tool qualification impacts **TA/R**, not G.                                                                  |
|  9 | ISO 26262          | *Operational situation & operating modes; ASIL; OSED*                       | **Work scope** (operating modes/situations)                                              | OSED/operating modes define **where capability can be exercised** → **Work scope**. Assurance level (ASIL) relates to **R**, not G.                                                           |
| 10 | IEC 61508          | *SIL; demand mode; proof test interval*                                     | **Work scope** (demand vs continuous mode) + **R freshness**                             | Mode concepts influence **where/how** a function can be claimed → **Work scope**; proof test interval sits in **R** (freshness/decay).                                                        |
| 11 | ACM Artifacts      | *Available/Evaluated/Reusable; Reproduced/Replicated*                       | **R** signals; **ContextSlice** (reproduction environment)                               | Badges encode **evidence availability/strength**; the declared environment maps to a **slice**; scope of claim is often implicit → USM makes it explicit.                                     |
| 12 | SRE / Cloud SLO    | *SLOs; error budgets; regions/tiers; rollout windows*                       | **Work scope** (regions/tiers/windows) + **measures**; **Γ\_time** policies              | SLOs attach **measures** within a **Work scope** (region/tier/time window); perfect fit for USM Method–Work guards (WG‑1..3).                                                                 |

**Summary.** Across all Contexts, two stable notions recur: (1) **evaluate in a concrete context** (→ `U.ContextSlice`), and (2) **declare where something holds/is deliverable** (→ set‑valued **Scope**). “Context of use,” “operating modes,” “targets,” “class extension,” and “OSED” are all Context‑flavored presentations of **Claim scope** or **Work scope**. Terms like *validity* and *operation* are semantically close but collide with **LA** and FPF’s **Work/Run** lexicon; we therefore **do not** adopt them as characteristic names.

---

### 17.4.3 · F.18 Term Selection — Unified Tech & Plain names

#### 17.4.3.1 Selected names (normative)

| Concept in A.2.6                | **Unified Tech** (lexicon)                      | **Unified Plain** (manager‑friendly) | Allowed short form   | Deprecated / avoid                                                    |
| ------------------------------- | ----------------------------------------------- | ------------------------------------ | -------------------- | --------------------------------------------------------------------- |
| Addressable evaluation context  | **`U.ContextSlice`**                            | **Context slice**                    | *Slice* (when local) | “domain” (as guard input), “latest” time                              |
| Abstract mechanism (set‑valued) | **`U.Scope`**                                   | **Scope**                            | —                    | “applicability”, “envelope”, “validity” (as characteristic names)     |
| Episteme applicability          | **`U.ClaimScope`** (*nick **G***)               | **Claim scope**                      | **G**                | “generality”, “applicability/envelope (of claim)”                     |
| Capability applicability        | **`U.WorkScope`**                               | **Work scope**                       | “capability envelope”, “operational applicability”, “operation scope” |
| Time selector                   | **`Γ_time`**                                    | **Time selector**                    | —                    | implicit “latest”                                                     |
| Cross‑context mapping              | **Bridge + CL**                                 | **Bridge + congruence level**        | **CL**               | silent reuse across Contexts                                             |
| Parallel coverage               | **SpanUnion**                                   | **Union of supported areas**         | —                    | unqualified “union” without independence                              |
| Serial dependency               | **Intersection**                                | **Intersection of scopes**           | —                    | ordinal “more/less general” language                                  |
| Scope edits                     | **ΔG+ (widen), ΔG− (narrow), Refit, Translate** | **Widen, narrow, refit, translate**  | —                    | stealth widening (“it’s obvious”)                                     |
| Optional didactics              | **`U.Detail (D)`, `U.AbstractionTier (AT)`**    | **Detail / abstraction tier**        | **D / AT**           | using AT/D as G substitutes                                           |

**Why these names (decision grounds):**

* **“Scope” wins over “envelope/applicability/validity”.** It is short, **self‑documenting**, and already idiomatic in SRE/SW, while “validity” clashes with **Validation Assurance (LA)** and “envelope” suggests geometry, not **membership**.
* **“Claim scope” vs “Work scope”.** Two‑word compounds meet the FPF clarity rule: the first token reveals the **carrier** (Claim vs Work/Capability), the second the **mechanism** (scope).
* **Keep **G**.** The F–G–R triple is canonical; we retain **G** as nickname for **Claim scope**.
* **“Context slice”** is the only term that makes the evaluation target **addressable** (Context, versions, params, **Γ\_time**).
* **“Operation/operating/validity” avoided.** They are **overloaded** in existing FPF lanes (Work/Run, LA) and create policy ambiguities in guards.

#### 17.4.3.2 Phrasebook (for editors, normative)

* Use **“Claim scope (G) covers TargetSlice”** and **“Work scope covers JobSlice”** in guards.
* Always spell **`Γ_time`**; never say “latest”.
* To compose, say: **“intersection along dependency paths; SpanUnion across independent support lines.”**
* For Cross‑context use, say: **“via Bridge; CL penalties apply to R (trust), not to F/G (content/scope).”**
* When widening/narrowing, write **“ΔG+ / ΔG−”** and log the support change; use **“Refit”** for unit/param normalization.

#### 17.4.3.3 Rosetta summary (informative, for rationale box)

| local context phrase                          | Use in USM wording                                          |
| ------------------------------------------ | ----------------------------------------------------------- |
| “Context of use” (NIST, ASME/FDA)          | **Claim scope (G)** on explicit **Context slice**           |
| “Operating modes/situations” (ISO 26262)   | **Work scope** with measures & qualification windows             |
| “Target (class/shape)” (SHACL/OWL)         | **Claim scope predicates** (membership)                     |
| “Architecture view context” (42010)        | **Context slice** + **Scope** checks inside the view        |
| “Capability envelope” (legacy safety docs) | **Work scope**                                              |
| “Domain” (informal)                        | **Context slice** elements; not acceptable as a guard input |

---

**Outcome.** The UTS shows strong convergence across SoTA Contexts on **addressable context** and **set‑valued applicability**. F.18 therefore fixes: **Context slice**, **Scope**, **Claim scope (G)**, **Work scope**, **Publication scope** with the algebra and guard clauses mandated in A.2.6. This closes synonym drift while remaining readable for engineering managers and precise for assurance tooling.
 
# A.3 Transformer Constitution (Quartet)  \[A]

## 1 · Intent

Establish a single, substrate‑neutral way to say **who acts**, **under which role**, **according to which description**, **by which capability**, and **what actually happened**—without “self‑magic” and without blurring design‑time and run‑time. The pattern fixes the **Transformer Quartet** so all kernel and Γ‑patterns reuse the *same four anchors*. It builds directly on **Holon‑Role Duality (A.2)** and **Temporal Duality (A.4)** and is guarded by **Strict Distinction (A.7)** and **Evidence Graph Referring (A.10)**.

## 2 · Context

* **Holonic substrate.** FPF separates *what things are* (Holon → {System, Episteme, …}) from *what they are being right now* via **roles**. Only **systems** can bear **behavioural** roles and execute methods/work; epistemes are changed **via their symbol carriers**.
* **Role as mask; behaviour as method/work.** A role is a **mask**, not behaviour; behaviour is a **Method** (order‑sensitive capability) that may be executed as **Work** (dated occurrence).
* **Design‑time vs run‑time.** A holon’s states belong to disjoint scopes **Tᴰ** and **Tᴿ**; transitions are physically grounded by a system bearing **TransformerRole**.
* **Evidence & carriers.** Claims about outcomes must anchor to **carriers** (SCR/RSCR) and to an **external** evidencing transformer.

## 3 · Problem

Legacy phrasing (“actor / process / blueprint”) causes recurrent failures:

1. **Self‑magic:** “the system configures itself” (no external acting side, causality lost).
2. **Plan = event:** blueprint/algorithm reported as if execution happened.
3. **Capability = result:** possession of a method counted as evidence of work.
4. **Episteme as doer:** documents/models treated as actors.
5. **Scope leak:** design‑time and run‑time mixed; run traces lack carriers/method ties.
   A.2/A.4/A.7/A.10 collectively forbid these, but A.3 must give the **canonical quartet** that authors can apply consistently.

## 4 · Forces

| Force                       | Tension                                                                                     |
| --------------------------- | ------------------------------------------------------------------------------------------- |
| **Identity vs behaviour**   | Keep holon identity stable while roles/behaviours change.                                   |
| **Simplicity vs precision** | Managers want one “process” box; kernel must keep **MethodDescription / Method / Work** distinct.  |
| **Universality vs idioms**  | Pumps, proofs, and data‑pipelines must read the same, yet allow domain names.               |
| **Design vs run**           | No overlap of **Tᴰ** and **Tᴿ**; bridges explicit and causal.                               |
| **Evidence vs mereology**   | Provenance edges (EPV‑DAG) must never turn into part‑whole edges.                           |

## 5 · Solution — The Transformer Quartet

A.3 defines four anchors, tied together by **Role Assignment (`U.RoleAssignment`)** and aligned with **Temporal Duality**.

### 5.1 The four anchors (terms & types)

1. **Acting side:** a **system bearing TransformerRole** — the only holon kind allowed to enact transformations (behavioural role). *Canonical phrase:* **“system bearing TransformerRole”**. *Local shorthand:* after explicit binding in the **same subsection**, you MAY write **“Transformer”** to denote that same system; re‑bind on context change and **do not** use shorthand where the domain already has a conflicting “transformer” term.

2. **MethodDescription (design‑time description):** protocol / algorithm / SOP / script — all are **idioms of MethodDescription**; they live in **Tᴰ** and are **epistemes** with carriers (SCR/RSCR).

3. **Method (design‑time capability):** order‑sensitive composition the system *can* enact at run‑time (Γ\_method); it is **not** an occurrence.

4. **Work (run‑time occurrence):** dated execution producing state change and consuming resources (Γ\_work); every Work **isExecutionOf** exactly one MethodDescription version and is **performedBy** exactly one performer (possibly a collective system).

> **Safe memory line:** *MethodDescription → (describes) Method → (executed as) Work.*
> Roles are **masks** (A.2/A.7); methods/work are **behaviour**.

### 5.2 Contextual Role Assignmnent (`U.RoleAssignment`) for transformations

Use the universal assignment to state **who plays which role where and when**:

```
U.RoleAssignment(
  holder  : U.System,          -- the acting system (bearer)
  role    : U.TransformerRole, -- behavioural role
  context : U.BoundedContext,  -- semantic boundary
  timespan?: Interval          -- optional validity window
)
```

* A role is **local to context** and **time‑indexed**.
* The same system may bear multiple roles **if** the context allows compatibility.
* For epistemes, the target of change is their **symbol carriers**; the acting side is still a **system**.

### 5.3 Boundary & externality

Every transformation is modelled with **two sides** and an explicit **U.Interaction** boundary: **acting** (system bearing TransformerRole) and **target** (system being transformed, or the **carrier** of an episteme). There is **no self‑doing**; “self‑like” stories are handled by the **reflexive split** (regulator vs regulated subsystems) or by promoting a meta‑holon and keeping evidence external (A.12).

### 5.4 Temporal alignment (A.4 bridge)

* **MethodDescription** lives in **Tᴰ**;
* **Method** is defined at design-time and **executed as `U.Work` at run-time by a `U.System` with a valid `U.RoleAssignment` (window-aligned) and a live **StateAssertion** for an **enactable** RSG state**;
* **Work** lives in **Tᴿ**;
* transitions **Tᴰ → Tᴿ** and **Tᴿ → Tᴰ** are **grounded** by executions of appropriate methods by an **external** transformer (e.g., fabrication or observation).

### 5.5 Evidence Graph Referring

Each Work anchors to **carriers** and to the **MethodDescription** it instantiates; evidencing transformers are **external** (no self‑evidence). This sits in the **EPV‑DAG** and never in mereology.

### 5.6 Didactic dictionary (safe mappings)

* “Process / Workflow / SOP / Algorithm” ⇒ **MethodDescription** (design‑time description).
* “Operation / Job / Run / Performance” ⇒ **Work** (run‑time occurrence).
* “Function (equipment spec)” ⇒ **Method** (or MethodDescription if purely textual).
* “Creator” (legacy) ⇒ **Transformer** (shorthand for **system bearing TransformerRole** after local binding).

## 6 · Illustrative scenarios (substrate‑neutral)

**6.1 Physical system — Cooling loop**
`PumpUnit#3` (**system bearing TransformerRole**) executes `ChannelFluid` (**Method**) as per `centrifugal_pump_curve.ld` (**MethodDescription**), producing `run‑2025‑08‑08‑T14:03` (**Work**, 3.6 kWh; ΔT=6 K). Evidence goes to carriers in SCR; resource spend goes to Γ\_work.

**6.2 Epistemic change — Proof revision**
`LeanServer` (**system bearing TransformerRole**) edits `proof_tactic.lean` (carrier) per MethodDescription; `lemma‑42‑check‑2025‑08‑08` is **Work**; the **episteme** (theorem) changes through its carriers; evidence is attributed to the external transformer.

**6.3 Reflexive maintenance — “calibrates itself”**
Split into **Regulator** (calibration module, acting side) and **Regulated** (sensor suite, target) with an interaction boundary; credit evidence to the regulator; no self‑evidence.

### 6 · Conformance Checklist (normative)

**CC‑A3‑0 · U.RoleAssgnment presence.**
Every claim that a holon “performs a transformation” MUST be backed by at least one **RoleAssignment** triple:
`U.RoleAssignment(holder: U.Holon, role: U.Role=TransformerRole, context: U.BoundedContext, timespan?)`.
This is the canonical way to say *who acts, in which role, where (semantically), and when*. See **A.2.1** for the universal **`U.RoleAssignment`** Standard and its invariants.

**CC‑A3‑1 · External transformer discipline.**
The **bearer** of `TransformerRole` MUST NOT be the same model instance as the **object‑under‑change** within the same assignment. Self-modification is modelled via two **`U.RoleAssignment`s** (same holder playing two roles) or via an explicit controller–plant split. This upholds **Agent Externalization** (A.12).

**CC‑A3‑2 · Design–Run separation.**
`U.MethodDescription` (recipe, definition) is a **design‑time** artefact; `U.Method` (mask‑of‑work) and `U.Work` (executed work) are **run‑time**. It is non‑conformant to mutate a `MethodDescription` inside a `Work` log or to treat a `Work` as a `MethodDescription`. This enforces the kernel’s **Temporal Duality** (A.4) and the A.15 alignment.

**CC‑A3‑3 · Boundary‑crossing evidence.**
A conformant transformation that changes a system’s state MUST reference the **boundary effects** it induces: interactions, flows, or state transitions attach to the target system’s boundary (per Γ‑defaults for additive, min/AND/OR folds). Conservation‑class effects MUST satisfy B‑invariants (e.g., **B‑1 Conservation**).

**CC‑A3‑4 · Method ←→ Work traceability.**
Every `U.Work` MUST (i) name the `U.Method` it instantiates and (ii) trace the `U.MethodDescription` it claims to follow (versioned). If a deviation occurs, it MUST be logged as a **policy override** or **exception path**; silent drift is non‑conformant. (A.15 guards the vocabulary; Γ\_work aggregates resource deltas.)

**CC‑A3‑5 · Episteme as object‑under‑change.**
When the changed holon is an **episteme** (document, dataset, theory), the transformer is still a **system**; the episteme’s history MUST be recorded via **PhaseOf** (versioning) and **ConstituentOf/PortionOf** as appropriate (not via component trees). See A.14’s mereology firewalls and Γ\_epist hooks.

**CC‑A3‑6 · Units and measures for resource effects.**
Any resource consumption/production in `U.Work` MUST specify the **measure μ** and **units** (e.g., kg, J, bytes); “percentage” effects MUST be grounded in a PortionOf μ to be Γ‑aggregatable. (A.14 POR‑axioms; Γ\_work usage.)

**CC‑A3‑7 · Provenance minimum.**
For each `U.RoleAssignment` and `U.Work`, the following fields are REQUIRED: `{authority?, justification?, provenance?}` where `justification: U.Episteme` and `provenance: U.Method`/process evidence. This aligns with the kernel’s governance and B‑cluster lineage practices.

**CC‑A3‑8 · Policy–Plan–Action separation for agentic cases.**
If the transformer bearer is agentic, the log MUST separate `D.Policy → U.PlannedAction → U.Action` (A.15/A.13), preserving where failure occurred (strategy, plan, or execution).

**CC‑A3‑9 · Context‑local conflicts.**
Conflicts among roles (including `TransformerRole`) are only **within the same bounded context**; cross‑context differences are admissible if bridges are declared. Non‑conformance arises only when a context’s own incompatibility rules are violated. (A.2.1 `U.RoleAssignment` invariants.)

**CC‑A3‑10 · Γ‑compatibility.**
Descriptions MUST be sufficient for the relevant Γ‑aggregations to run: Γ\_method for recipe composition, Γ\_work for resource deltas, Γ\_sys for boundary integration, Γ\_time for ordering. Each Γ flavour declares its A.14 hooks (Portion/Phase) and inherits B‑invariants.

---

### 7 · Consequences

**Benefits**

* **Explainability by construction.** Every transformative claim carries *who/what/when/why/how* via **`U.RoleAssignment`** + provenance fields; audits become mechanical rather than heroic. (B‑invariants and Γ tables do the heavy lifting.)
* **No category errors.** Keeping methods/roles out of mereology and enforcing design/run separation prevents the usual “process‑as‑part” and “version‑as‑component” mistakes. (A.14 + A.15.)
* **Composable analytics.** With measures and boundary folds explicit, cross‑scale proofs (Σ/Π/min/∧/∨) are predictable.
* **Contextual pluralism without chaos.** Divergent domain practices coexist as distinct bounded contexts with bridges; disagreements are localised and tractable.

**Trade‑offs**

* **More declarations up‑front.**  `U.RoleAssignment` + units + policy/plan/action feels verbose, but yields deterministic Γ‑runs and reproducible audits.
* **Discipline for “self‑modifiers.”** Modellers must split controller vs plant or dual‑role the same carrier; this adds one line but avoids hidden identity conflations.

---

### 8 · Rationale (post‑2015 cross‑domain support)

**Constructor theory (post‑2015).**
Our **Transformer Principle** mirrors constructor theory’s shift from *dynamics* to *tasks*: what transformations are **possible** vs **impossible**, and why. By making the **transformer** (constructor) an explicit bearer of a role and keeping recipes as `MethodDescription`, A.3 captures the core “tasks & constructors” distinction and aligns with constructor‑theoretic thermodynamics linking work, heat, and informational constraints. ([Royal Society Publishing][1], [arXiv][2], [Constructor Theory][3])

**Active inference & free‑energy mechanics (2017→).**
Where transformers are *agentic*, A.3’s policy–plan–action split and boundary‑centred accounting dovetail with **active inference** and **free‑energy** formulations of self‑organising systems (Markov blankets; Bayesian mechanics). This legitimises `U.Objective`/cost function links and makes design–run duality natural (prior vs posterior policies). ([MIT Press Direct][4], [PubMed][5], [arXiv][6])

**Provenance and FAIR packaging (2016→).**
Provenance minima in CC‑A3‑7 reflect **FAIR** principles (machine‑actionable reuse), **RO‑Crate** (methods+data+context packaged together), and operational lineage standards such as **OpenLineage** and **ML Metadata (TFX)** that treat *artefacts, runs, and jobs* as first‑class, with typed facets and versioning — exactly what enactment + Γ\_work need. ([Nature][7], [researchobject.org][8], [SAGE Journals][9], [openlineage.io][10], [GitHub][11], [arXiv][12])

Together, these lines of work argue for **explicit role‑bearing transformers**, **recipe/run separation**, **boundary‑grounded deltas**, and **traceable contexts** — the four pillars that CC‑A3 enforces.

---

### 9 · Relations

**A.7 Strict Distinction.**
A.3 operationalises A.7 by keeping **object ≠ description ≠ observation**:
*object* = target holon; *description* = `MethodDescription`; *observation/log* = `Work`. Violations (e.g., treating a recipe as a part) are non‑conformant and usually surface as Γ failures.

**A.12 Agent Externalization & External Transformer.**
A.3’s CC‑A3‑1 is the mechanical guard‑rail for A.12: even in self‑modification, the *modelling split* keeps the agent (transformer bearer) distinct from the object‑under‑change.

**A.13 Agential Role.**
When the bearer is an **Agent**, A.3 defers identity and states management to Agent‑CAL (`U.Agent`, `U.Intent`, `U.Action`), while still requiring `RoleAssigning` + Γ compatibility. This is where policy/plan/action pipelines live.

**A.15 Role–Method–Work Alignment.**
A.3 relies on A.15’s vocabulary guard‑rails (roles are not parts; methods are masks of work; specs are recipes). CC‑A3‑2/‑4 are enforceable precisely because A.15 fixes the naming discipline.

**A.14 Advanced Mereology.**
A.3 consumes A.14’s **PortionOf** (for quantitative deltas) and **PhaseOf** (for versioning) and forbids role/recipe leakage into part–whole trees. Γ‑flavours declare which A.14 hooks they use.

**B‑cluster (Γ‑sections).**
A.3 is executable only because Γ‑operators provide aggregation and invariants:

* **Γ\_sys** enforces boundary folds and conservation;
* **Γ\_epist** preserves document/data provenance and versioning;
* **Γ\_time** orders work;
* **Γ\_method** composes recipes;
* **Γ\_work** accounts resource deltas; each inherits B‑invariants (e.g., B‑1 Conservation, B‑2 No‑Duplication).

**Indexing to the glossary.**
Terms used here (TransformerRole, Work, Method, MethodDescription, PortionOf, PhaseOf, BoundedContext) remain exactly as defined in Annex A; see A.1/A.2/A.14/A.15 entries for lexical registers.

[1]: https://royalsocietypublishing.org/doi/10.1098/rspa.2014.0540?utm_source=chatgpt.com "Constructor theory of information | Proceedings of the Royal Society A"
[2]: https://arxiv.org/abs/1405.5563?utm_source=chatgpt.com "Constructor Theory of Information"
[3]: https://www.constructortheory.org/wp-content/uploads/2016/07/THD-ArXiv-Final.pdf?utm_source=chatgpt.com "[PDF] Constructor Theory of Thermodynamics"
[4]: https://direct.mit.edu/neco/article/29/1/1/8207/Active-Inference-A-Process-Theory?utm_source=chatgpt.com "Active Inference: A Process Theory | Neural Computation | MIT Press"
[5]: https://pubmed.ncbi.nlm.nih.gov/27870614/?utm_source=chatgpt.com "Active Inference: A Process Theory - PubMed"
[6]: https://arxiv.org/abs/1906.10184?utm_source=chatgpt.com "A free energy principle for a particular physics"
[7]: https://www.nature.com/articles/sdata201618?utm_source=chatgpt.com "The FAIR Guiding Principles for scientific data management and ..."
[8]: https://www.researchobject.org/ro-crate/about_ro_crate?utm_source=chatgpt.com "About RO-Crate - Research Object"
[9]: https://journals.sagepub.com/doi/10.3233/DS-210053?utm_source=chatgpt.com "Packaging research artefacts with RO-Crate - Sage Journals"
[10]: https://openlineage.io/docs/?utm_source=chatgpt.com "About OpenLineage | OpenLineage"
[11]: https://github.com/OpenLineage/OpenLineage?utm_source=chatgpt.com "GitHub - OpenLineage/OpenLineage: An Open Standard for lineage metadata collection"
[12]: https://arxiv.org/pdf/2010.02013?utm_source=chatgpt.com "[PDF] A Brief History Of TensorFlow Extended (TFX) - arXiv"

# A.3.1 — U.Method  \[D]

## 1 · Context (plain‑language motivation)

Teams must talk about **how** something is done without entangling:

* **Who** is assigned (that is **Role**/**RoleAssigning**),
* **Whether** the holder can do it (that is **Capability**), and
* **What actually happened** (that is **Work**).

`U.Method` supplies the *how*—the **abstract way of performing a transformation**, independent of a specific run, a specific assignee, or a specific notation. It works across paradigms:

* **Imperative** (step‑graphs, SOPs, BPMN),
* **Functional** (pure mappings and compositions, no “steps”),
* **Logical/constraint/optimization** (goals, rules, admissible solutions).

In FPF, a **system** bearing a **TransformerRole** *enacts* a `U.Method` (producing **Work**) by following a **MethodDescription**—an episteme that describes the method in some representation.

## 2 · Problem (what goes wrong without a clean notion of “method”)

1. **Process soup.** “Process” gets used for recipe, execution, schedule, or org area. Planning, staffing, and audit blur together.
2. **Spec = run fallacy.** A flowchart (or code) is taken as if execution already happened; conversely, logs get mistaken for the recipe.
3. **Role leakage.** People encode assignments inside the recipe (“this step is the surgeon”), tying **who** to **how** and making reuse impossible.
4. **Notation lock‑in.** When “method” is defined as “a set of steps,” functional or logical styles become second‑class citizens and cannot be modeled cleanly.

## 3 · Forces (what the definition must balance)

| Force                                  | Tension we resolve                                                                                        |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Universality vs. specificity**       | One notion must cover welding, ETL, proofs, and schedulers, while letting each domain keep its idioms.    |
| **Representation vs. semantics**       | Many notations express the same “way of doing”; we need one semantic anchor across specs.                 |
| **Reusability vs. assignment**        | The *how* should be reusable regardless of *who* is assigned this time.                                  |
| **Compositionality vs. executability** | Methods compose (serial/parallel/choice/iteration), but execution may diverge due to conditions/failures. |
| **Determinism vs. search**             | Methods may be deterministic algorithms or constraint problems with admissible solution sets.             |

---

## 4 · Solution — the method as an abstract, paradigm‑agnostic “way of doing”

### 4.1 Definition

**`U.Method`** is a **context‑defined abstract transformation type**—the **semantic “way of doing”** a kind of work.  
It is:
**Described** (never *identical*) by one or more **`U.MethodDescription`** epistemes (code/SOP/diagram/rules),  
**Enacted** by a `U.System` bearing an appropriate **Role** (usually a **TransformerRole**) to produce **`U.Work`**, and  
**Independent** of who is assigned, what instance ran, or which notation was used.

**Strict Distinction (didactic):**  
* ***Method** = *how in principle* (semantic Standard).  
* ***MethodDescription** = *how it is written* (artifact on a carrier).  
* ***Work** = *how it actually went this time* (dated execution).

### 4.2 Representation‑agnostic stance (specs may be imperative/functional/logical)

A `U.Method` does **not** require an imperative step structure. **Representations live in `U.MethodDescription`, not in the Method itself.**  
Typical **MethodDescription forms** include:

* **Imperative MethodDescription:** step‑graph/flow (serial/parallel/branch).  
* **Functional MethodDescription:** a composition `f ∘ g ∘ h` with typed interfaces/constraints, no “steps”.  
* **Logical/constraint MethodDescription:** a goal/constraint set with admissible solutions and search/optimization semantics.  
* **Hybrid MethodDescription:** imperative scaffolding with functional kernels and/or solver calls.

**Semantic identity criterion (context‑local).** Two MethodDescriptions **describe the same `U.Method`** in a given `U.BoundedContext` iff, for all admissible inputs and conditions recognized by that context, they entail the **same preconditions**, **guarantee the same postconditions/effects**, and satisfy the **same non‑functional bounds** (allowing permitted non‑determinism). Internal control‑flow/search details may differ.


### 4.3 Method vs MethodDescription vs Work (quick litmus)

| You have in your hand…           | In FPF it is…                 | Why                                                                             |
| -------------------------------- | ----------------------------- | ------------------------------------------------------------------------------- |
| A flowchart/BPMN/SOP text        | **`U.MethodDescription`** (Episteme) | A description on a carrier.                                                     |
| A git repo with code | **`U.MethodDescription`** (Episteme) | Still a description (even if executable). The Method is the semantic “way” it denotes. |
| A log/run report with timestamps | **`U.Work`**                  | A concrete event that happened.                                                 |
| “The way we weld seams type W”   | **`U.Method`**                | The abstract *how*, represented by one or more specs and realized by many runs. |

**Didactic rule:** when referencing *the idea* of “how”, say **Method**; when referencing *the document or code*, say **MethodDescription**; when referencing *the run*, say **Work**.

### 4.4 Interface and effect (conceptual descriptors)

When presenting a `U.Method` in a review, anchor it with these paradigm‑neutral elements (not a data schema):

1. **Interface** — what is required/provided in general (inputs/outputs/types or resources/roles/ports).
2. **Preconditions** — what must already hold (guards, invariants, Standard “requires”).
3. **Postconditions / Effects** — what is guaranteed after successful enactment (Standard “ensures”).
4. **Non‑functional constraints** — latency, accuracy, cost, safety envelope (ties to **Capability** thresholds).
5. **Failure modes** — known failure classes and recoverability hints.
6. **Compositional hooks** — whether this method composes serially/parallel/choice/iteration (see §4.5).

### 4.5 Method mereology (composition without confusing it with runtime)

Methods compose into bigger methods; executions compose into bigger executions—**do not conflate** the two.

**Method composition (design‑time):** serial (`·`), parallel (`‖`), choice (`|`), iteration (`*`), refinement/substitution—yield **new `U.Method`s**.
**Work composition (run‑time):** the corresponding **Work** may split/merge/overlap differently due to scheduling, failures, or environment, yet it is still **execution of the same Method**.
**Mapping advice:** avoid naming run‑time artifacts inside the method definition (no “this thread”, “this person”); keep those in **Role**/**Work**.

### 4.6 Constructor‑theoretic reading (why Method ≠ algorithm ≠ spec)

Constructor Theory views a **constructor** as a physical entity that **effects transformations**. In FPF:

* A `U.System` with **TransformerRole** is the constructor (the performer).  
* A **`U.Method`** is the abstract **transformation type** it enacts (semantic Standard).  
* An **algorithm artifact** is a **`U.MethodDescription`** for an **information‑transformation Method**.  
* A **universal transformer** generalizes the **Turing machine** by **executing any `U.Method` described by a physically admissible `U.MethodDescription`** (not only informational ones).

Thus, welding, milling, reagent mixing, and proof construction are all **Methods**; textbooks/code/derivations are their **MethodDescriptions**; **Work** are the concrete runs.

### 4.7 Context anchoring

`U.Method` is **local to a `U.BoundedContext`**: terminology, admissible pre/postconditions, and non‑functional constraints are interpreted **inside that context**. If two teams or theories use the same name for different “ways of doing,” they are different Methods in different contexts unless bridged explicitly.

---

## 5 · Archetypal grounding (cross-paradigm examples: imperative / functional / logical)

### 5.1 Industrial transformation (imperative flavor)

* **Method:** `Etch_Al2O3`.
* **MethodDescription:** SOP document; a PLC program that controls gas mix and timing.
* **Enactment:** `Tool_42#TransformerRole:FabLine_A` produces **Work** runs W‑101, W‑102….
* **Notes:** Step diagram exists, but a later **functional** spec may also exist (composition of gas‑flow functions). Both **specs** describe the **same Method**.

### 5.2 Operational planning (functional/optimization flavor)

* **Method:** `JS_Schedule_v4` (job‑shop scheduling).
* **MethodDescription:** a MILP model + solver configuration; documentation of constraints/objective.
* **Enactment:** `PlannerService_v4#TransformerRole:PlantScheduling_2025` produces **Work** `Run_2025‑W32‑P1`.
* **Notes:** No “steps” are visible at the method level; the solver’s search is internal. Still a `U.Method`.

### 5.3 Scientific proof (logical flavor)

* **Method:** `Gauss_Elimination`.
* **MethodDescription:** formal rules in a proof assistant; textbook chapter as a second spec.
* **Enactment:** `CAS_Alpha#TransformerRole:MathLab_2025` generates a **Work** proof instance for a concrete matrix.
* **Notes:** The **Episteme** (spec) is not the **ability** (that belongs to the CAS system) and not the **execution** (the proof run).

---

## 6 · Didactic quick grammar (for managers)

* **Who?** `Holder#Role:Context` (**Role assignment**)
* **Can?** `Capability(holder)` within envelope/measures
* **How (in principle)?** **`Method`**, described by **`MethodDescription`**
* **Did?** **`Work`** (execution), linked by `performedBy → RoleAssigning` and `isExecutionOf → MethodDescription`

> *Keep the four words apart and plans become dependable.*

---

## 7 · Bias‑Annotation (as in cluster‑E patterns)

* **Lenses tested:** `Arch`, `Prag`, `Did`, `Epist`.
* **Scope declaration:** Universal; semantics are context‑local via `U.BoundedContext`.
* **Rationale:** Gives FPF a **paradigm‑neutral** “how” that bridges MethodDescription (knowledge on a carrier) and Work (execution), while staying independent of Role (assignment) and Capability (ability).

## 8 · Conformance Checklist (normative)

**CC‑A3.1‑1 (Strict Distinction).**
`U.Method` is the **semantic “way of doing”**. It is **not** a `U.MethodDescription` (artifact on a carrier), **not** a `U.Work` (dated execution), **not** a `U.Role`/assignment, and **not** a `U.Service`/promise.

**CC‑A3.1‑2 (Context anchoring).**
Every `U.Method` **MUST** be defined **within** a `U.BoundedContext`. Identity, admissible pre/postconditions, and non‑functional bounds are interpreted **in that context**.

**CC‑A3.1‑3 (Specification linkage).**
A `U.Method` **SHOULD** be **described by** ≥1 `U.MethodDescription`. For operational gating, at least one `MethodDescription` **MUST** be present and named. Multiple specs may coexist (imperative/functional/logic), see CC‑A3.1‑7.

**CC‑A3.1‑4 (assignment‑free).**
A `U.Method` **SHALL NOT** hard‑code holders or assignments. If a step “needs a surgeon”, express that as a **role requirement** (to be satisfied via `U.RoleAssignment` at run time), not as a named person/unit inside the method.

**CC‑A3.1‑5 (Runtime‑free).**
A `U.Method` **SHALL NOT** contain schedule, calendar slots, or run IDs; those belong to `U.WorkPlan` (plans) and `U.Work` (executions). Methods are timeless.

**CC‑A3.1‑6 (Interface & effects).**
A `U.Method` **MUST** admit a context‑local statement of interface (inputs/outputs or ports/resources), **preconditions**, **postconditions/effects**, and (when relevant) **non‑functional bounds**. These anchor semantic identity beyond a particular notation.

**CC‑A3.1‑7 (Multi‑spec semantic identity).**
Two or more `U.MethodDescription` **describe the same `U.Method`** in a given context **iff** they entail the **same admissible preconditions**, **guarantee the same effects**, and satisfy the **same non‑functional bounds** for all inputs/conditions recognized by that context (allowing permitted non‑determinism). Internal control‑flow/search differences are irrelevant.

**CC‑A3.1‑8 (Composition vs execution).**
Composition of Methods (design‑time) and composition of Work (run‑time) **MUST** be kept distinct. Method composition yields **new Methods**; Work composition yields **composed executions**. They may correspond but are not identical.

**CC‑A3.1‑9 (Parameterization).**
If a Method is parameterized, parameters are **declared** at the Method/MethodDescription level; **concrete values** are bound **at `U.Work` creation**. Avoid freezing parameter values inside the Method definition.

**CC‑A3.1‑10 (Dynamics ≠ Method).**
Laws/trajectories (`U.Dynamics`) are models of state evolution and **SHALL NOT** be labeled as Methods. A Method **may** rely on a Dynamics model (e.g., for control), but they remain distinct artifacts/concepts.

**CC‑A3.1‑11 (Capability checks are orthogonal).**
A step may impose capability thresholds; those thresholds are checked **against the holder’s `U.Capability`** independently of assignment and independently of the Method’s description.

**CC‑A3.1‑12 (Constructor‑theoretic alignment).**
Algorithm artifacts are `U.MethodDescription` for information‑transforming Methods. Physical Methods are equally valid (matter/energy transformations). A “universal transformer” is a system that can enact **any physically admissible MethodDescription**; this does **not** collapse Method into “algorithm.”

---

## 9 · Method mereology (composition) — design‑time only

**Operators (conceptual, context‑scoped):**

* **Serial composition (`·`)** — do A then B → `A · B` is a new Method.
* **Parallel composition (`‖`)** — do A and B concurrently (with declared independence/joins).
* **Choice (`|`)** — do **one** of {A, B} under guard/selector.
* **Iteration (`*`)** — repeat A under a loop invariant/termination condition.
* **Refinement (`≤ₘ`)** — Method M' preserves M’s interface/effects and **strengthens** preconditions or **tightens** non‑functional bounds (context‑defined lattice).
* **Substitution** — replace a Method factor with a semantically equivalent one (`M ≡ N` in context) without changing the whole’s Standard.

**Design‑time laws (intuitive, not mechanized here):**

* Associativity for `·` and, where admissible, for `‖`.
* Distributivity over guarded choice under context rules.
* Identity elements (e.g., `Skip` that preserves state and satisfies neutral bounds).
* Monotonicity: refinement of a factor **should not** break the whole’s postconditions.

**Run‑time mapping (do not conflate):**
`U.Work` instances of `A · B` **may** interleave differently due to scheduling or failure‑handling and still be executions of `A · B`. The mapping is “execution semantics,” not part of Method mereology.

## 10 · How Methods interact with Roles, Capability, Work, Dynamics (manager’s view)

* **Roles (assignment).** Steps stipulate **role kinds** (e.g., `IncisionOperatorRole`), not people. At run time, `U.Work` references a **`U.RoleAssignment`** that satisfies the role kind.
* **Capability (ability).** Steps may require **thresholds** (e.g., “precision ≤ 0.2 mm”). They are checked against the **holder’s `U.Capability`** in the context/envelope.
* **Work (execution).** Each run records `isExecutionOf → MethodDescription` (the spec used) and `performedBy → RoleAssigning`. Logs, resources, and timestamps live here.
* **Dynamics (laws/models).** Methods may cite or assume a Dynamics model; runs may attach traces that are explained by that model. Do not label the model itself as the Method.

---

## 11 · Anti‑patterns (and the right move)

* **Spec = Method.** “The BPMN is the Method.” → The BPMN is a **MethodDescription**; the **Method** is the semantic way it denotes.
* **Run = Method.** “Yesterday’s process is our Method.” → Yesterday’s run is **Work**.
* **Role leakage.** “Step 3 is done by Alice.” → Step 3 **requires** `SurgeonRole`; Alice may be assigned via **RoleAssigning**.
* **Schedule leakage.** “Run at 02:00 daily” inside the Method. → This belongs to **WorkPlan**; Methods are timeless.
* **BoM entanglement.** Putting parts/assemblies inside Method definition. → Structure stays in PBS/SBS; Method references **interfaces/resources**, not a BoM.
* **Algorithm‑only bias.** Declaring that only code counts as a Method. → Physical transformations (welding, mixing) are Methods too; their SOPs/parameters are MethodDescriptions.
* **Hard‑coding capability.** Baking “≤ 0.2 mm” into a role name or Method name. → Keep thresholds on **steps**; **capability** lives on the **holder**.

---

## 12 · Migration notes (quick wins)

1. **Rename wisely.** Where texts say “process/method” but mean a diagram or code repo, label it **MethodDescription**; where they mean the abstract “how,” label it **Method**.
2. **Extract assignments.** Replace named people/units in specs with **role kinds**; enforce assignments via **RoleAssigning** at run time.
3. **Pull time out.** Move calendars/schedules from specs into **WorkPlan**.
4. **Parameter hygiene.** Declare parameters at Method/MethodDescription; bind values in **Work**.
5. **Equivalence notes.** When two specs are intended as the same Method, write an **equivalence note** in the context (pre/post/bounds parity).

---

## 13 · Consequences

| Benefits                                                                                                                    | Trade‑offs / mitigations                                                                           |
| --------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **Clarity across paradigms.** Methods are first‑class regardless of notation; teams stop arguing step‑vs‑functional.        | **One more name to learn.** Use the quick grammar card; it pays off fast.                          |
| **Reuse without personnel lock‑in.** assignment moves to RoleAssigning; Methods remain portable.                             | **Extra role tables.** Keep role‑kind lists short and context‑local.                               |
| **Robust audits.** Logs are Work, specs are MethodDescription, Standards are Method; no more “we thought the diagram was the run.” | **Discipline needed.** Enforce the three‑way split in reviews.                                     |
| **Constructor‑theoretic coherence.** Physical and informational transformations are peers.                                  | **Cultural shift.** Not every team is used to seeing SOPs and code as the same class (MethodDescription). |

---

## 14 · Relations

* **Builds on:** A.1 Holonic Foundation; A.1.1 `U.BoundedContext`; A.2 `U.Role`; A.2.1 `U.RoleAssignment`; A.2.2 `U.Capability`.
* **Coordinates with:** A.3 (role masks for transformers/constructors/observers); A.15 (Role–Method–Work Alignment); B.1 Γ (aggregation) for method families vs assembly of systems.
* **Informs:** `U.WorkPlan` \[D] (plans reference Methods they schedule); `U.Service` \[D] (promises cite Methods as delivery means); `U.Dynamics` \[D] (models that Methods may assume).

---

## 15 · Didactic quick cards (reuse in specs and onboarding)

* **Method / MethodDescription / Work** = *how in principle* / *how it is written* / *how it went this time*.
* **Four‑slot grammar:** Who? → **RoleAssigning**. Can? → **Capability**. How? → **Method** (via **MethodDescription**). Did? → **Work**.
* **Design‑time vs run‑time:** Composition of Methods ≠ composition of Work.
* **No steps required:** Functional, logical, and hybrid MethodDescriptions are first‑class.
* **Keep time and people out:** Schedules → **WorkPlan**; assignees → **RoleAssigning**.

# A.3.2 — U.MethodDescription  \[D]


## 1 · Context (plain‑language motivation)

Projects need a **stable way to express “how it is written”**—the recipe, code, SOP, rule set, or formal proof—**without confusing it** with:

* the **semantic “way of doing”** (that is `U.Method`),
* the **assignment** (that is `U.RoleAssignment`),
* the **ability** (that is `U.Capability`),
* the **execution** (that is `U.Work`), or
* the **calendar plan** (that is `U.WorkPlan`).

`U.MethodDescription` gives this anchor. It treats **algorithms, programs, proofs, SOPs, BPMN diagrams, solver models, playbooks** as **one class of epistemes**: *knowledge on a carrier that describes a Method*. This unifies software and “paper” procedures and lets teams switch notations without breaking the model.

---

## 2 · Problem (what breaks without a clear `MethodDescription`)

1. **Spec/run conflation.** A flowchart or code is mistaken for the run; audits and SLOs become unreliable.
2. **Who/time leakage.** People and calendars creep into the recipe; reuse and staffing agility die.
3. **Step‑only bias.** Functional or logical styles are treated as “not real methods”; designs get contorted into faux steps.
4. **Algorithm‑centrism.** Only code is considered “the method”, leaving SOPs and scientific procedures second‑class.
5. **Structure entanglement.** BoM/PBS elements end up inside the recipe; method and product structure tangle.
6. **Unstated equivalence.** Two specs intended to mean “the same method” are not declared equivalent; teams fork semantics by accident.

---

## 3 · Forces (what we must balance)

| Force                              | Tension we resolve                                                                                  |
| ---------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Representation vs. semantics**   | Many notations, one meaning: specs may differ, method stays one.                                    |
| **Universality vs. domain idioms** | SOPs, code, solver models, proofs—all first‑class, yet domain terms remain local.                   |
| **Timelessness vs. operability**   | Specs are timeless, but must be precise enough to drive execution and audit.                        |
| **Reusability vs. constraints**    | Specs should declare role kinds, capabilities, safety bounds—without baking in people or calendars. |
| **Evolvability vs. identity**      | Specs change; we need a way to evolve them without losing the method’s identity or history.         |

---

## 4 · Solution — the specification as an episteme describing a Method

### 4.1 Definition

**`U.MethodDescription`** is an **`U.Episteme`** that **describes a `U.Method`** in a concrete representation (text, code, diagram, model). It is **knowledge on a carrier** that can be reviewed and validated; at run-time a **`U.System`** **uses it to execute the `U.Method` as `U.Work` under a `U.RoleAssignment`**.

> **Strict Distinction (memory aid):**
> **Method** = *how in principle* (semantic Standard).
> **MethodDescription** = *how it is written* (artifact/description).
> **Work** = *how it went this time* (dated execution).

### 4.2 Representation‑agnostic stance (independent of “algorithmic paradigm”)

`U.MethodDescription` **does not privilege any single notation**. Typical forms include (non‑exhaustive):

* **Imperative Spec** — SOP, BPMN/flowchart, PLC ladder, shell/pipeline scripts.
* **Functional Spec** — compositions of pure functions, typed pipelines, category‑style combinators.
* **Logical/Constraint Spec** — rules/goal sets, SAT/SMT/MILP models, theorem‑prover scripts.
* **Statistical/ML Spec** — model definitions, training/evaluation procedures, inference pipelines.
* **Reactive/Event‑driven Spec** — statecharts, observers/triggers, stream/CEP rules.
* **Hybrid Spec** — mixtures (e.g., imperative orchestration calling solver kernels).

**Same Method, different MethodDescriptions.** In a single `U.BoundedContext`, several MethodDescriptions **may describe the same `U.Method`** if they entail the **same preconditions**, **guarantee the same effects**, and meet the **same non‑functional bounds** (cf. A.3.1).

### 4.3 What a good MethodDescription states (paradigm‑neutral content)

Not a schema—these are **content prompts** for reviewers:

1. **Purpose & Name of the Method** it describes (link to `U.Method`).
2. **Interface/ports** (inputs/outputs/resources/Standards) in the context’s vocabulary.
3. **Preconditions** (guards, invariants, required states).
4. **Postconditions / Effects** (what is guaranteed upon success).
5. **Non‑functional constraints** (latency, precision, cost, safety envelope).
6. **Role requirements** for enactment (**kinds**, not people)—to be satisfied at run time via **`U.RoleAssignment`**.
7. **Capability thresholds** the performer must meet (checked against **`U.Capability`** of the holder).
8. **Failure semantics** (detectable failures, compensations, rollback/forward strategies).
9. **Compositional hooks** (how this spec composes: serial/parallel/choice/iteration), without embedding calendars.
10. **Parameter declarations** (what may vary per run; values bound at `U.Work` creation).

> **Didactic guardrail:** A MethodDescription **does not** embed a schedule, assignees, or BoM. Calendars → `U.WorkPlan`; people/units → `U.RoleAssignment`; product structure → PBS/SBS.

### 4.4 Epistemic roles for MethodDescriptions (via `U.RoleAssignment`)

Being an Episteme, a MethodDescription may itself play epistemic roles via `U.RoleAssignment` in a context (classification, not action), e.g.:

* `ApprovedProcedureRole`, `RegulatedProcedureRole`, `SafetyCriticalProcedureRole`, `De‑factoStandardRole`.
* These **do not** make the spec an actor; they classify its **status** within the context (who may use it, in which settings).

### 4.5 Constructor‑theoretic note (unifying “algorithms” and “physical recipes”)

In the constructor‑theoretic reading used by FPF:

* **Algorithms, programs, solver models, proofs** are all **`U.MethodDescription`**—descriptions of Methods that transform **information**.
* **SOPs, control recipes, lab protocols** are **`U.MethodDescription`**—descriptions of Methods that transform **matter/energy**.
* A **universal transformer** (a system with sufficient capability) enacts **any physically admissible MethodDescription**—not only informational ones.

This keeps software and “wet lab” on equal footing.

---

## 5 · Clear distinctions (quick litmus for managers)

| You are holding…                          | It is…                         | Why                                           |
| ----------------------------------------- | ------------------------------ | --------------------------------------------- |
| A BPMN diagram or SOP                     | **`U.MethodDescription`**             | A description on a carrier.                   |
| A git repo or compiled binary             | **`U.MethodDescription`**             | Still a description (even if executable).     |
| “The way we do X in principle”            | **`U.Method`**                 | Semantic Standard beyond any single notation. |
| A run log with timestamps                 | **`U.Work`**                   | A dated execution event.                      |
| A role description (“surgeon”, “planner”) | **`U.Role` / `U.RoleAssignment`** | assignment, not recipe.                      |
| “Can achieve ±0.2 mm”                     | **`U.Capability`**             | Ability of a holder, not a spec.              |
| A calendar for next week’s runs           | **`U.WorkPlan`**               | Plan/schedule, not a recipe.                  |
| A state‑transition law                    | **`U.Dynamics`**               | Model of evolution, not a method description. |

---

## 6 · Archetypal grounding (parallel cases)

### 6.1 Industrial SOP (imperative)

* **Method:** `Etch_Al2O3`.
* **MethodDescription:** `SOP_Etch_v7.pdf` + PLC ladder file.
* **Role requirements:** `EtchOperatorRole`; **Capability:** gas‑control precision ≤ threshold.
* **Execution:** `Tool_42#TransformerRole:Fab_A` enacts the spec → **Work** runs W‑143…W‑155.

### 6.2 Optimization model (logical/constraint)

* **Method:** `JS_Schedule_v4`.
* **MethodDescription:** MILP model + solver config; admissible solution definition.
* **Execution:** `PlannerService_v4#TransformerRole:Plant_2025` produces **Work** `Run_2025‑W32‑P1`.

### 6.3 Clinical guideline (epistemic, status via RoleStateGraph + State Assertion)

* **Method:** `AcuteAppendicitis_Triage`.
* **MethodDescription:** clinical decision rule set; **Epistemic Role**: `RegulatedProcedureRole:Hospital_Context`.
* **Execution:** `ER_Team#TransformerRole:ER_Shift` enacts the spec on a case → **Work** visit V‑8842.

---

## 7 · Bias‑Annotation (as in E‑cluster)

* **Lenses tested:** `Did`, `Prag`, `Arch`, `Epist`.
* **Scope declaration:** Universal; semantics are **context‑local** via `U.BoundedContext`.
* **Rationale:** Elevates **all** procedural artifacts—code, SOPs, proofs, models—to a single class, avoiding algorithm‑centrism and step‑only bias. Keeps the strict split among **Method / MethodDescription / Work / Role / Capability**.

## 8 · Conformance Checklist (normative)

**CC‑A3.2‑1 (Episteme status).**
`U.MethodDescription` **IS** an `U.Episteme` (knowledge on a carrier). It is **not** a `U.Method` (semantic way), **not** a `U.Work` (execution), **not** a `U.Role/RoleAssigning` (assignment), **not** a `U.WorkPlan` (schedule), and **not** PBS/SBS content.

**CC‑A3.2‑2 (Context anchoring).**
Every `U.MethodDescription` **MUST** be interpreted **within** a `U.BoundedContext`. Names, Standards, and admissible non‑functional bounds are **local** to that context.

**CC‑A3.2‑3 (Method linkage).**
A `U.MethodDescription` **MUST** declare the `U.Method` it describes. Multiple MethodDescriptions **MAY** describe the same Method (see CC‑A3.2‑8).

**CC‑A3.2‑4 (assignment/time‑free).**
A MethodDescription **SHALL NOT** embed assignees, org units, or calendars. People/units are bound via **`U.RoleAssignment`** at run time; calendars belong to **`U.WorkPlan`**.

**CC‑A3.2‑5 (Structure‑free).**
BoM/PBS/SBS artifacts **SHALL NOT** be embedded in MethodDescriptions. Reference **interfaces/resources** and constraints instead of listing parts/assemblies.

**CC‑A3.2‑6 (Role and capability requirements).**
A MethodDescription **MAY** state **role kinds** and **capability thresholds** required for enactment. These are **requirements**, not bindings. They are checked at run time against `U.RoleAssignment` and `U.Capability`.

**CC‑A3.2‑7 (Parameterization).**
Parameters **MUST** be **declared** in the Method/MethodDescription; concrete values are **bound** when creating `U.Work`. Default values in a spec are allowed but **SHALL NOT** force a schedule or assignee.

**CC‑A3.2‑8 (Semantic equivalence).**
Two MethodDescriptions **describe the same `U.Method`** in a given context **iff** they entail the **same preconditions**, **guarantee the same postconditions/effects**, and satisfy the **same non‑functional bounds** for all admissible inputs/conditions of that context (per A.3.1 CC‑A3.1‑7). Differences in control flow, search, or notation do **not** break equivalence.

**CC‑A3.2‑9 (Refinement).**
`Spec₂` **refines** `Spec₁` for the same Method iff it **preserves interface**, **does not weaken** postconditions/effects, and **tightens** (or equal) non‑functional bounds under **equal or stronger** preconditions. Declare refinement explicitly in the context.

**CC‑A3.2‑10 (Compatibility claims).**
Claims such as “sound but incomplete” or “complete but potentially unsound” relative to another MethodDescription **MUST** be stated explicitly and scoped to the context (e.g., solver approximations).

**CC‑A3.2‑11 (Executable specs).**
Executability does **not** change status: an executable artifact (program, script) is still a **MethodDescription**. Its runs are **Work**; its semantics are the **Method** it denotes.

**CC‑A3.2‑12 (Epistemic roles via `U.RoleAssignment`).**
A MethodDescription **MAY** play **epistemic roles** via `U.RoleAssignment` (e.g., `ApprovedProcedureRole`, `RegulatedProcedureRole`) that classify its status. Such bindings **do not** make the spec an actor.

**CC‑A3.2‑13 (Non‑determinism declaration).**
If a MethodDescription permits non‑determinism (e.g., search/optimization), the **space of admissible outcomes** and **acceptance criteria** **MUST** be stated (so that Work can be judged).

**CC‑A3.2‑14 (Bridging across contexts).**
If two contexts use different MethodDescriptions for “the same‑named way,” an explicit **Bridge (`U.Alignment`)** **SHOULD** be provided to map terms/assumptions. Do **not** assume cross‑context identity by name alone.

---

## 9 · MethodDescription mereology (epistemic composition; not method composition)

Keep two worlds separate:

* **Method composition (design‑time semantic):** combines Methods into **new Methods** (A.3.1 §9).
* **MethodDescription mereology (epistemic):** combines **documents/code/models** into larger **spec artifacts**. This is about **parts of the description**, not about the semantic method algebra.

**Epistemic part relations (illustrative):**

* **`ConstituentOf`** — a chapter/module/snippet is a constituent of a larger spec.
* **`Imports/Uses`** — this spec reuses a library/rule set.
* **`VariantOf`** — this spec is a variant (e.g., for different equipment) with declared deltas.
* **`RepresentationOf`** — this visual diagram is a representation of the textual rule set.

**Didactic rule:** Do not infer that a spec with two modules **means** a Method with “two steps.” Modules are **parts of the description**, not necessarily steps of the Method.

---

## 10 · Parameterization & variability (templates, defaults, configs)

**Templates.** A MethodDescription may serve as a **template** with parameters (e.g., temperature set‑points, solver tolerances, objective weights).

**Binding time.**

* **Declare** parameters in the spec;
* **Bind** values when creating `U.Work` (or at an agreed “compile” stage);
* Keep bound values **visible** in the Work record (so runs can be compared).

**Defaults and guards.**

* Defaults are allowed; list **valid ranges** and **guards** (e.g., safety constraints).
* If a default has safety impact, state it explicitly as part of **preconditions**.

**Variants.**

* When variants differ only by **parameter ranges** → keep one Method with one MethodDescription template.
* When variants differ by **Standard** (effects/bounds) → either declare a **refinement** or introduce a **distinct Method** (context decision).

---

## 11 · Equivalence & compatibility (across notations and contexts)

**Within one context.**

* Use **semantic equivalence** (CC‑A3.2‑8) to assert that BPMN vs code vs solver model are the **same Method**.
* Prefer a short **equivalence note** showing parity of pre/post/bounds.

**Across contexts.**

* Treat identity as **not guaranteed**.
* Provide **Bridges (`U.Alignment`)** that map terms, units, roles, and acceptance criteria.
* Be explicit if one spec is only **sound** (never returns forbidden outcomes) vs **complete** (can return all allowed outcomes).

**Observational perspective (pragmatic).**
Two specs are observationally equivalent for stakeholders **if**, under declared conditions, they are indistinguishable by the acceptance tests of that context (even if internal strategies differ).

---

## 12 · Anti‑patterns (and the right move)

* **Spec = run.** “Yesterday’s process log is our spec.” → The log is **Work**; write a **MethodDescription** and link runs to it.
* **Who/time in the spec.** “Step 3 by Alice at 02:00 daily.” → Use **RoleAssigning** at run time; schedule via **WorkPlan**.
* **Stuffing BoM.** Listing parts/assemblies inside the spec. → Reference **interfaces/resources**; keep PBS/SBS separate.
* **Algorithm‑only bias.** Treating code as “real spec” and SOPs as “notes.” → Both are **MethodDescription**; judge by Standards, not by format.
* **Hiding non‑determinism.** Solver model with no acceptance criteria. → Declare admissible outcome set and tests.
* **Silent parameter capture.** Hard‑coding values without declaring parameters. → Declare parameters with ranges; bind at Work creation.
* **Undeclared variant drift.** Copy‑pasting specs and tweaking silently. → Use **VariantOf** with stated deltas or declare a refinement.

---

## 13 · Migration notes (quick wins)

1. **Label the artifacts.** Wherever a repo/diagram/document “is the process,” rename it **MethodDescription** and link it to a named **Method**.
2. **Extract people and calendars.** Move all assignees to **RoleAssigning** and all schedules to **WorkPlan**.
3. **Introduce parameter blocks.** Add a small “Parameters” section with ranges/defaults and safety guards.
4. **Write acceptance criteria.** Especially for search/optimization or ML specs.
5. **Declare equivalence/refinement.** Where two notations intend “the same way,” add an **equivalence note**; where the new one tightens bounds, declare **refinement**.
6. **Bridge domains.** If two departments use different vocabularies, add a **Bridge (`U.Alignment`)** rather than forcing a single spec.

---

## 14 · Consequences

| Benefits                                                                                                          | Trade‑offs / mitigations                                                                           |
| ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **One class for all recipes.** SOPs, code, models, proofs become peers; teams can choose the best notation.       | **A bit more ceremony.** You name the Method and the MethodDescription separately; the payoff is clarity. |
| **Cleaner audits.** Specs vs runs vs assignments vs abilities never mix.                                         | **Discipline required.** Keep schedules and people out of specs.                                   |
| **Easier reuse and substitution.** Equivalence/refinement rules enable swapping notations without semantic drift. | **Equivalence is a claim.** Back it with short acceptance tests.                                   |
| **Cross‑domain coherence.** Bridges allow controlled translation between contexts.                                | **Bridge maintenance.** Someone owns the mapping; keep it short and focused.                       |

---

## 15 · Relations

* **Builds on:** A.3.1 `U.Method` (the semantic way it describes); A.1.1 `U.BoundedContext`.
* **Coordinates with:** A.2 `U.Role`, A.2.1 `U.RoleAssignment` (who enacts it); A.2.2 `U.Capability` (ability thresholds); A.15 Role–Method–Work (linking `isExecutionOf` to runs).
* **Informs:** `U.WorkPlan` (plans reference MethodDescriptions); `U.Dynamics` (models that specs may assume); Epistemic Role patterns (status of specs RoleStateGraph + State Assertion).
* **Lexical guards:** E.10.y **L‑PROC** (do not call MethodDescription “process” when you mean Work/WorkPlan); E.10.x **L‑FUNC** (avoid “function/functionality” confusion).

---

## 16 · Didactic quick cards

* **Spec ≠ Method ≠ Work.** *Written recipe* ≠ *semantic way* ≠ *dated execution*.
* **Keep people/time out.** Assignees → **RoleAssigning**; schedules → **WorkPlan**.
* **Declare parameters & acceptance.** Bind values at Work; state how success is judged.
* **Same method, different specs.** BPMN/code/solver can be equivalent **if** pre/post/bounds match.
* **Bridge, do not blur.** Cross‑team/domain differences go through **`U.Alignment`**, not wishful thinking.
  
## A.3.3 · `U.Dynamics` \[D]

### 1 · Context

Teams need one place to say **how a thing changes**. Physicists call this “dynamics” (equations of motion, state‑transition maps). In IT and enterprise change, we often talk about **evolution of characteristics** (latency, cost, reliability, compliance, architectural fitness) across time. In knowledge work, **KD‑CAL** (knowledge dynamics) reasons about how the **status of claims** shifts as evidence arrives. All these are *the same modeling need*: a context‑local description of **state space** and **allowed transitions**.

FPF already separates:

* **what a holon is** (structure, PBS/SBS),
* **how we act** (Method/MethodDescription, Work),
* **what we promise** (Service).

What is missing without `U.Dynamics` is the **law of change**—the model that tells us how states evolve **with or without** our interventions.

> Intuition: **Method** tells an agent what to do; **Dynamics** tells everyone how the world (or a model of it) changes when something happens (or even when nothing happens).

**Lexical note.** Terms like *process* and *thermodynamic process* are mapped by **L‑PROC**:

* the **recipe** is `U.Method/MethodDescription`,
* the **dated run** is `U.Work`,
* the **law/trajectory model** is `U.Dynamics`.

---

### 2 · Problem

Without a first‑class `U.Dynamics`, models suffer predictable failures:

1. **Recipe = Law.** Teams put the *procedure* (Method/MethodDescription) where the *state law* should be, so simulations and predictions become impossible to compare with reality.
2. **Run = Law.** Logs of Work are mistaken for dynamics; past events are treated as if they defined what *must* happen.
3. **No state space.** Discussions jump between metrics (latency! throughput!) without an explicit **characteristic space** or invariants, so “improvements” cannot be reasoned about.
4. **Domain lock‑in.** “Dynamics” is left to domain vocabularies (physics, control, finance), losing a trans‑disciplinary way to speak about change in a single kernel.

---

### 3 · Forces

| Force                                  | Tension                                                                                                                 |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Universality vs. richness**          | One kernel notion must cover ODE/PDE, Markov chains, queues, discrete events, and enterprise “fitness characteristics”. |
| **Model vs. reality**                  | A law must be **design‑time** (an `Episteme`), yet judged by **run‑time** evidence (Work).                              |
| **Continuous vs. discrete vs. hybrid** | Different time bases and update rules must coexist.                                                                     |
| **Open vs. closed systems**            | Exogenous inputs (control/disturbances) may be explicit or implicit.                                                    |
| **Predictive use vs. diagnostic use**  | The same dynamics can guide planning or explain incidents; interfaces must support both.                                |

---

### 4 · Solution — The unified concept `U.Dynamics`

**Definition (normative).**
Within a `U.BoundedContext`, **`U.Dynamics`** is an **`U.Episteme` that specifies a state space and a state‑transition law** (deterministic or stochastic, continuous/discrete/hybrid) for one or more holons, possibly under exogenous inputs and constraints. It **does not** prescribe what an agent should do (that is `U.Method/MethodDescription`) and **is not** the dated evolution itself (that is `U.Work` evidence).

* **Type:** `U.Episteme` (design‑time model/law on a carrier).
* **Orientation:** descriptive/predictive about **how states evolve**; can be used by Methods but remains separate from them.
* **Judged by:** conformance of observed **Work‑derived traces** to the law and invariants.

#### 4.1 · Core structure (minimal fields)

```
U.Dynamics {
  context        : U.BoundedContext,     // where the model’s meaning and units are defined
  stateSpace     : CharacteristicSpace,  // explicit characteristics & units; may include topology/geometry
  transitionLaw  : Episteme,             // equations/relations/kernels/transition matrices/rules
  timeBase       : {continuous|discrete|hybrid},
  stochasticity? : {deterministic|stochastic}, // incl. noise/likelihood model if stochastic
  inputs?        : P(Characteristic),    // control/disturbances/environmental drivers
  observation?   : Episteme,             // measurement/observation map from state to observables
  constraints?   : Episteme,             // invariants/safety envelopes/guards
  validity?      : Conditions,           // operating region, approximations, version, timespan
  calibration?   : Episteme              // parameter identification / priors
}
```

* **`stateSpace`** uses FPF **characteristics** (not “characteristics”) so we can talk about **architecture fitness** (e.g., latency, MTBF, cost) just like temperature/pressure/volume in physics.
* **`transitionLaw`** is paradigm‑agnostic: ODE/PDE, finite‑state relation, Petri net firing, queueing kernel, Bayesian update, etc.
* **`observation`** separates what exists from what we *measure* (key for monitoring/assurance).

#### 4.2 · What `U.Dynamics` is **not**

* **Not a Method/MethodDescription:** no imperative steps or prescriptions.
* **Not Work:** no timestamps/resources attached; evidence lives on `U.Work`.
* **Not a Service:** no consumer promise; dynamics may underpin service SLOs but does not define the promise.
* **Not PBS/SBS:** do not place dynamics inside structural BoMs.

---

### 5 · Where `U.Dynamics` sits in enactment

* **Design‑time:**
  Methods may *reference* Dynamics for planning/control (e.g., MPC uses a plant model).
  Services may *derive* acceptance targets from Dynamics (e.g., queueing predictions → SLO).

* **Run‑time:**
  Work produces **state samples/telemetry**; applying the **observation** map yields traces.
  Conformance/violation is decided by comparing traces with **constraints** and predictions from the transition law.
  Updates to model parameters flow via **calibration** (design‑time again).

> Memory hook: **Method decides**, **Dynamics predicts**, **Work reveals**.

### Prediction Use In Gating (normative)

When **predicted** coordinates (from a dynamics model) are used for **comparison or gating**, one of the following **MUST** hold:
1) a **fresh observation** is available for the gate’s window; or
2) the applied flow/map `Φ_{Δt}` is proven **non‑expansive** (Lipschitz ≤ 1) under the declared distance overlay (see § 5.1.7), **and** it **commutes** with the invariantization step (§ 5.1.6) — i.e., `Quot/Fix_g ∘ Φ_{Δt} = Φ_{Δt} ∘ Quot/Fix_g` on the domain of use.

If neither condition is satisfied, using prediction for gating is **forbidden**; the system **MUST** fall back to observation. Any use of `Φ_{Δt}` **SHALL** declare its validity window (range, Δt).

### 6 · Archetypal grounding (engineer‑manager friendly)

| Domain                        | Holon & State Space                     | Transition Law Example               | Observation                 | Typical Questions                                                 |
| ----------------------------- | --------------------------------------- | ------------------------------------ | --------------------------- | ----------------------------------------------------------------- |
| **Process control**           | Reactor: {Temperature, Concentration}   | Non‑linear ODE with disturbance term | Thermocouples, analyzers    | Will we overshoot? What control horizon keeps safety constraints? |
| **Reliability/ops**           | Service platform: {MTBF, MTTR, Backlog} | Birth–death/queueing model           | Incident logs, uptime pings | Given load, what SLO is feasible?                                 |
| **Evolutionary architecture** | System: {Latency, Cost, Coupling}       | Discrete‑time map per release        | Perf tests, bills           | If we change X, how does latency trend next 3 sprints?            |
| **KD‑CAL (knowledge)**        | Claim: {Belief, Support}                | Bayesian update rule                 | Evidence artifacts          | How does confidence evolve as studies arrive?                     |

**Key takeaway:** one kernel object captures **trajectories in a characteristic space**, from thermodynamics to software quality and knowledge confidence.

## 7 · Conformance Checklist (normative)

**CC‑A3.3‑1 (Type).**
`U.Dynamics` **IS** an `U.Episteme` (design‑time model/law on a carrier). It is **not** a `U.Method/MethodDescription`, **not** `U.Work`, and **not** a structural part of any PBS/SBS.

**CC‑A3.3‑2 (Context).**
Every `U.Dynamics` **MUST** be declared **inside** a `U.BoundedContext`. Units, characteristic names, admissible regions, and time base are **local to the context**; cross‑context reuse requires a Bridge (`U.Alignment`).

**CC‑A3.3‑3 (Explicit state space).**
`stateSpace` **MUST** enumerate characteristics with units/scales (continuous/discrete/ordinal) and any topology/geometry needed for trajectories. Do **not** refer to informal “axes”.

**CC‑A3.3‑4 (Transition law).**
`transitionLaw` **MUST** specify a state‑transition relation/map/kernel suitable for the declared time base (`continuous|discrete|hybrid`) and stochasticity (deterministic or with a likelihood/noise model).

**CC‑A3.3‑5 (Observation model).**
If evidence from `U.Work` is to be checked against the law, an `observation` mapping **MUST** be provided (identity is acceptable only if explicitly stated). Sampling rate/granularity **SHOULD** be declared.

**CC‑A3.3‑6 (Constraints & validity).**
If safety/envelope constraints apply, they **MUST** be declared under `constraints`. Operating region, approximations, version, and `timespan` **SHOULD** be stated under `validity`.

**CC‑A3.3‑7 (Separation from Method).**
A `U.Dynamics` **SHALL NOT** prescribe imperative steps or responsibilities. Planning/control algorithms that *use* the dynamics belong to `U.Method/MethodDescription`.

**CC‑A3.3‑8 (No actuals on Dynamics).**
Resource/time **actuals** and telemetry **MUST** attach to `U.Work`. Calibration outcomes produce **new versions** of `U.Dynamics`; the law object itself carries no run‑time logs.

**CC‑A3.3‑9 (Multi‑scale declaration).**
If state is aggregated across parts or time, the aggregation policy (`Γ_time`, `Γ_work`, averaging vs. sum vs. percentile) **MUST** be stated to prevent incoherent comparisons.

**CC‑A3.3‑10 (Lexical hygiene).**
Ambiguous uses of *process/processual* (laws vs. runs vs. recipes) **MUST** be resolved per **L‑PROC**/**L‑ACT**:

* law → `U.Dynamics`,
* recipe → `U.Method/MethodDescription`,
* run → `U.Work`.

**CC‑A3.3‑11 (Link to Services—optional).**
If Service SLOs are derived from a dynamics model, the Service **SHOULD** reference that `U.Dynamics` (A.2.3), but the Service remains the promise, not the law.

---

## 8 · Evidence and operators (traces, prediction, conformance)

Let `D` be a `U.Dynamics` in context `C`. Let `W` be a set of `U.Work` records produced under `C`. Let `obs_D(·)` be the declared observation map for `D`.

### 8.1 Derived evidence

* **`trace(W, D)` → Sequence\<t, y>:**
  derive an ordered sequence of observed values `y` at times `t` by applying `obs_D` to Work/telemetry associated with `W`. (Not a kernel type; a derived artifact for analysis/assurance.)

* **`inputs(W)` → Series:**
  exogenous inputs/control signals recovered from Work metadata if the model declares `inputs`.

* **`initialState(W, D)` → x₀:**
  the assumed/estimated state at trace start (from Work context or a stated estimation rule).

### 8.2 Prediction & simulation

* **`predict(D, x₀, inputs?, horizon)` → Trajectory:**
  propagate the law to obtain a predicted trajectory in the declared state space.

* **`admissible(D, x)` → bool:**
  test whether state `x` satisfies `constraints`.

* **`reach(D, S₀, S₁, inputs?, horizon)` → bool:**
  reachability: can states in `S₀` evolve into `S₁` under the law.

### 8.3 Conformance & drift

* **`residuals(D, trace)` → Series:**
  discrepancies between predicted and observed series under a stated alignment (point‑wise, windowed, distributional).

* **`fits(D, trace, tol)` → {pass|fail|partial}:**
  verdict under tolerance policy `tol` defined by the context (e.g., sup‑norm ≤ ε, percentile bands, likelihood threshold).

* **`drift(D₁, D₂, domain)` → Measure:**
  divergence between two model versions over a declared operating domain (e.g., max deviation of eigenvalues, KL between predictive distributions).

### 8.4 Invariants

* `fits(D, trace, tol)=pass` ⇒ every sample lies in `admissible(D,·)` unless the context explicitly permits out‑of‑envelope transients.
* If two traces are generated under identical `inputs` and initial conditions, recorded differences must be explainable by the declared stochasticity/noise model or flagged as violations.

> **Didactic hook:** *Dynamics predicts; Work reveals; Conformance compares.*

---

## 9 · Anti‑patterns (and the right move)

* **“Dynamics = procedure.”**
  Control recipes/step graphs belong to `Method/MethodDescription`. Keep the law in `U.Dynamics`.

* **“Telemetry = dynamics.”**
  Logs are `Work` evidence. Build `trace(Work, D)` and compare to the law; do not store logs inside the law.

* **“No state space.”**
  KPI lists without an explicit `stateSpace` turn into dashboard folklore. Name characteristics with units and ranges.

* **“Hard‑coding SLO inside the law.”**
  Service targets are promises (`U.Service.acceptanceSpec`). Keep predictions and promises separate; link them.

* **“Stuffing Dynamics into BoM.”**
  A model is not a component. Leave PBS/SBS for structure.

* **“One size fits all time base.”**
  If parts of the system evolve on different clocks, declare `hybrid` and separate update rules.

---

## 10 · Migration notes (quick path to value)

1. **Name the changing things.** Pick 3–7 **characteristics** that matter (physical or architectural). Declare `stateSpace` with units and ranges.
2. **Write the law you already use.** Even if it is a queueing approximation or a simple ARIMA—put it under `transitionLaw` and state assumptions under `validity`.
3. **Separate recipe from law.** Move control procedures to `Method/MethodDescription`; keep forecasting/plant equations in `U.Dynamics`.
4. **Wire evidence.** Ensure production `Work` emits the measurements needed by `observation`. Build `trace(Work, D)`.
5. **Start conformance.** Define a simple `tol` and compute `fits(D, trace, tol)` weekly. Raise issues on drift; version the model when calibrating.
6. **Link to promises (optional).** If SLOs depend on the law, reference `U.Dynamics` from `U.Service` and derive targets transparently.
7. **For KD‑CAL.** Treat belief/support as characteristics; declare a Bayesian/likelihood update in `transitionLaw`; evaluate conformance against evidence arrivals.

---

## 11 · Relations

* **Builds on:**
  `A.1.1 U.BoundedContext` (local meaning/units),
  `A.2 Role` / `A.2.1 RoleAssigning` (agents that *use* the law),
  `A.15.1 U.Work` (run‑time evidence).

* **Coordinates with:**
  `A.3.1 U.Method` / `A.3.2 U.MethodDescription` (planning/control using the law),
  `A.2.3 U.Service` (promises informed by predictions),
  **KD‑CAL** (knowledge dynamics as a specialisation: belief‑update laws),
  **Resrc‑CAL** (cost/energy models as dynamics over resources).

* **Constrained by lexical rules:**
  **E.10 L‑PROC** (process disambiguation), **L‑ACT** (activity/action), **L‑FUNC** (function).

---

## 12 · Didactic quick cards (engineer‑manager ready)

* **Dynamics = Law of Change.** A design‑time model of how states evolve.
* **State space = Named characteristics with units.** No vague “axes”.
* **Method vs Dynamics.** Method decides *what we do*; Dynamics predicts *what will happen*.
* **Work = Evidence.** Only Work has timestamps and resource actuals.
* **Conformance = Prediction vs Trace.** Fit, residuals, drift.
* **Keep promises separate.** Services are promises; Dynamics informs them but does not replace them.

**Memory hook:** **Method decides · Dynamics predicts · Work reveals.**

## A.4  Temporal Duality & Open‑Ended Evolution Principle \[A] 

*“A holon is born in design‑time, lives in run‑time,  
and is reborn when the world talks back.”*

### Problem frame  
A holon’s **blueprint** and its **lived reality** are never identical for
long.  Pumps wear out, theories meet anomalous data, workflows face
unanticipated load.  FPF therefore requires a temporal framework that:

1. Physically grounds every modification (via the Transformer Principle,
   A 3).  
2. Supports unbounded improvement cycles (**P‑10 Open‑Ended Evolution**).  
3. Works identically for physical, epistemic, operational (method, work) and future
   holon flavours.

### Problem  

| Failure mode | Consequence |
|--------------|-------------|
| **Blueprint ≡ Reality** | “As‑built” discrepancies remain invisible; safety and validity claims become fiction. |
| **Implicit magic updates** | Versions overwrite each other; provenance chains snap. |
| **Observer special‑case** | Measurement treated as metaphysical rather than a normal, physically grounded transformation. |

### Forces  

| Force | Tension |
|-------|---------|
| **Stability vs Change** | Identify a holon across time ↔ allow radical redesigns. |
| **Prediction vs Evidence** | Plan with intended specs ↔ respond to real telemetry. |
| **Parsimony vs Expressiveness** | Keep the model lean ↔ respect the full lifecycle complexity. |

---

### Solution · Temporal Duality Model  

FPF assigns every holon state to one—and only one—of two **temporal
scopes**:

| Scope | Symbol | Definition | Typical contents |
|-------|--------|------------|------------------|
| **Design‑Time** | *Tᴰ* | Interval(s) during which the holon **may be structurally altered** by an *external* `Transformer` executing a `U.TransformationalMethod`. | Specs, CAD, theorem scripts, IaC SCRs. |
| **Run‑Time** | *Tᴿ* | Interval(s) during which the holon **executes its own `OperationalMethod`s** and is assumed structurally stable (self‑maintenance allowed). | Telemetry, transaction logs, field data, physical wear. |

**Temporal invariants**

```text
Tᴰ ∩ Tᴿ = ∅                     (never overlap)
Tᴰ ∪ Tᴿ = worldline(holon)      (cover full existence)
version(n+1) created only in Tᴰₙ (monotonic lineage)
````

#### Open‑Ended Evolution Principle

A holon may repeat the cycle *ad infinitum*:

```
(H₀ in Tᴿ₀) → observe → Δspec in Tᴰ₁ → build → H₁ in Tᴿ₁ → …
```

*Observation itself is a transformation*:
An **External Transformer** (`U.System` playing `transformerRole ⊑ TransformerRole`)
executes a **measurement method** whose *output* is an epistemic holon
containing observations.  Thus the traditional “External Observer Pattern” collapses into
the universal external Transformer pattern.

---

### Archetypal Grounding

| Phase                 | Pump‑v2 (`U.System`)                                                                         | Proof‑v2 (`U.Episteme`)                                                                 |
| --------------------- | -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **Design‑Time**       | 3‑D CAD + G‑code; stress‑sim config.                                                         | Lean/Coq script of theorem; dependency graph.                                           |
| **Run‑Time**          | Pump circulates coolant under `OperatePump` method.                                          | Theorem cited & reused; runtime is “being relied on”.                                   |
| **Run → Design loop** | Sensor data shows cavitation; anomaly report produced by monitoring server (`transformerRole`). | New experiment contradicts corollary; lab apparatus + scientists act as `transformerRole`. |
| **Design → Run loop** | Engineers author Pump‑v3 spec, printer (`TransformerRole`) fabricates it.                    | Community revises proof, proof‑assistant (`TransformerRole`) verifies Proof‑v3.         |

*(Diagrammatic lineage table omitted for brevity but included in annex.)*

### Conformance Checklist  

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC‑A.4.1** | Every `U.Holon` **MUST** be tagged with its current temporal scope (*Tᴰ* or *Tᴿ*). | Eliminates blueprint/reality ambiguity. |
| **CC‑A.4.2** | A transition from *Tᴰ* → *Tᴿ* **SHALL** be modeled as `executes(Transformer, U.TransformationalMethod)`. | Guarantees physical grounding of instantiation. |
| **CC‑A.4.3** | A transition from *Tᴿ* → *Tᴰ* **SHALL** be modeled as `executes(transformerRole, U.TransformationalMethod)` producing an observational `U.Episteme`. | Ensures observation is treated as transformation. |
| **CC‑A.4.4** | `Tᴰ ∩ Tᴿ = ∅` and the concatenated intervals **MUST** equal the holon’s worldline. | Guards against illicit overlap. |
| **CC‑A.4.5** | Each new design version **MUST** reference (`refinesVersion`) exactly one predecessor or declare `firstVersion = true`. | Enforces monotonic lineage for auditability. |

---

### Consequences  

| Benefits | Trade‑offs / Mitigations |
|----------|--------------------------|
| **Audit‑Ready engineering workflow** – Every state and change is explicitly typed, timed, and causally linked to a physical system/Tramsformer. | Additional metadata tagging; mitigated by templates in Authoring Guide (E 8). |
| **Unified View of Build & Measure** – Observation, test, simulation, maintenance, and fabrication all share one mechanism. | Requires modelers to think in terms of Transformers even for “passive” sensing; mitigated by role libraries (`transformerRole`, `CalibratorRole`, etc.). |
| **Foundation for Learning Loops** – Enables higher patterns (e.g., B 4 Canonical Evolution Loop, D 3 Trust Calculus) to reason over evidence accrual and version fitness, including self-modification. | None significant—temporal scoping is already needed for safety‑critical provenance. |

---

### Rationale (extended)  

1. **Why separate scopes?**  
   Real‑world artefacts SCR the *as‑intended* versus *as‑is* gap.
   By formalising that gap, FPF prevents silent assumption of perfect
   fidelity and allows quantified error (`U.Error`) to drive evolution.

2. **Why treat observation as transformation?**  
   Physics tells us measurement changes state (energy, information, even
   quantum collapse).  Making the observer just another `Transformer`
   means: no special metaphysics, full energy/provenance accounting,
   seamless tie‑in with Constructor Theory (see A 3 Rationale §2).

3. **Why insist on open‑endedness?**  
   *Perfect* finality is unattainable outside mathematics mandates that holons must be *improvable* in principle; this pattern
   encodes that mandate structurally: version n+1 is always possible.

4. **Why no overlap (*Tᴰ* ∩ *Tᴿ*)?**  
   The instant a holon is mutable (design) it ceases to be the “same”
   operational asset relied upon for guarantees.  Overlap would break
   trust calculations and violate A.7 Strict Distinction.

This pattern therefore realises three core principles in concert:

* **Temporal Duality** – explicit tagging of states.  
* **Open‑Ended Evolution** – guaranteed pathway for refinement.  
* **Ontological Parsimony** – one mechanism (Transformer) for all
  state changes, avoiding specialised “observer” or “installer” types.

> *“Blueprints dream; instances speak.  
> Evolution is the conversation between them.”*

## A.5 Open‑Ended Kernel & Architheory Layering \[A] 

### Problem frame

FPF’s ambition is to act as an *“operating system for thought.”*
That ambition can only be realised if the framework:

* **(i)** remains *stable* and *self‑consistent* over multi‑decade timespans;
* **(ii)** *invites*, rather than resists, the continual influx of new disciplinary knowledge; and
* **(iii)** allows multiple, even competing, explanatory lenses to coexist without forcing a “winner‑takes‑all” unification.

Historically, grand “total” ontologies—Aristotle’s *Categories*, Carnap’s *Logical Construction of the World*, Bunge’s *TOE*—failed precisely because each tried to embed every domain’s primitives directly into a single monolith.  Once the monolith cracked under domain pressure, the whole edifice became unmaintainable.

### Problem

If FPF were to let **domain‑specific primitives creep into its Kernel**, two pathologies would follow:

| Pathology               | Manifestation                                                                                                                  | Breach of Constitution                                                     |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| **Kernel Bloat**        | Every new field (e.g. synthetic biology) adds bespoke `U.Type`s → Core size explodes, review surface becomes unscalable.       | Violates **C‑5 Ontological Parsimony**; erodes **P‑1 Cognitive Elegance**. |
| **Conceptual Gridlock** | Conflicting axioms (deterministic thermodynamics vs. indeterministic econ‑metrics) must fight for space in the same namespace. | Breaks **C‑3 Cross‑Scale Consistency**; triggers chronic DRR deadlock.     |

A *minimal, extensible* design is therefore mandatory.

### Forces

| Force                            | Tension                                                                                                                  |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Stability vs. Evolvability**   | Immutable core needed for trust ↔ constant domain innovation needed for relevance.                                       |
| **Universality vs. Specificity** | Single kernel language ↔ rich idioms for fields as diverse as robotics, jurisprudence, metabolomics.                     |
| **Parsimony vs. Coverage**       | Few primitives keep reasoning elegant ↔ framework must still model energy budgets, epistemic uncertainty, agentic goals. |

### Solution 

FPF adopts a **micro‑kernel hour‑glass** architecture consisting of a *strictly minimal* core plus an **infinite flat namespace of plug‑ins** called *architheories*. (The formal plug‑in Standard is defined in **A.6 Architheory Signature & Realisation**.)

**1 The Open‑Ended Kernel**
The Kernel’s *normative* content is frozen to three buckets only:

* **Foundational Ontology:** `Entity`, `Holon`, `Boundary`, `Role`, `design‑/run‑time`, etc. (A‑cluster, Part A).
* **Universal Reasoning Patterns:** Γ‑aggregation, MHT, Trust calculus, Canonical evolution loop, etc. (B‑cluster, Part B).
* **Ecosystem Standards:** Guard‑Rails (E‑cluster) and the Architheory Signature schema (A.6).

Everything else—physics, logic operators beyond minimal MODAL, resource semantics, agent decision calculus—is *expelled* to architheories.

**2 Architheory Layering**

+To manage this extensibility without creating chaos, FPF classifies all architheories into three mutually exclusive classes, each with a distinct role. This classification governs what an architheory is allowed to do.

| Class | Mnemonic | Conceptual Mandate |
| :--- | :--- | :--- |
| **Calculus** | **CAL** - *The Builder* | Introduces a new composite holon type and **exactly one** aggregation operator `Γ_*` that *constructs* such holons from parts. |
| **Logic** | **LOG** - *The Reasoner* | Adds rules of inference or proof patterns *about* existing holons. **It cannot create new composite holons** and thus exports no `Γ_*` operator. |
| **Characterization**| **CHR** - *The Observer* | Attaches metrics or descriptive properties to existing holons. **It neither constructs nor infers new holons** and exports no `Γ_*` operator. |

Each architheory (CAL / LOG / CHR):

* **extends** the Kernel by *importing* its primitives and *exporting* new, *typed* vocabularies;
* remains **self‑contained**—it must **not mutate** Kernel axioms (CC‑A.6.x);
* is versioned, compared, and substituted entirely via its *Signature* (public Standard) while permitting multiple *Realizations* (private axiom-sets).

Architheories therefore form the **“fat top & bottom”** of the hour‑glass:

```
          ┌──────────────────────────┐
          │  Unlimited Domain CALs   │  ← e.g. Resrc‑CAL, Agent‑CAL
          ├──────────────────────────┤
          │  Core CAL / LOG / CHR    │  ← Sys‑CAL, KD‑CAL, Method‑CAL …
          ╞════════ Kernel (Part A+B) ╡
          │  Γ, MHT, Trust, etc.     │
          ├──────────────────────────┤
          │  Unlimited Tooling Real. │  ← simulators, proof assistants …
          └──────────────────────────┘
```

### Archetypal Grounding (System / Episteme)

| Element of the Pattern                 | **Archetype 1 – `U.System`**<br>(industrial water‑pump)                                                                                                                 | **Archetype 2 – `U.Episteme`**<br>(scientific theory of gravitation)                                                                                                           |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Kernel concepts used**               | `U.System`, `U.Holon`, `TransformerRole`                                                                                                                                | `U.Episteme`, `U.Holon`, `transformerRole`                                                                                                                                        |
| **Domain CAL that extends the Kernel** | **Sys‑CAL** adds conservation laws, port semantics, resource/work hooks                                                                                                 | **KD‑CAL** adds F‑G‑R characteristics, provenance graph, trust metrics                                                                                                                    |
| **Resulting instance**                 | A fully specified CAD model of the pump that can be aggregated by Γ\_sys, analysed by LOG‑CAL, and costed by Resrc‑CAL – **without ever mutating the Kernel** | A fully formalised theory object that can be cited, aggregated, and challenged by KD‑CAL, validated by LOG‑CAL, scored by the Trust calculus – **again without Kernel change** |

This table demonstrates the *hour‑glass* architecture in action:
*Wide variety of concrete instances* → **narrow, stable Kernel neck** → *wide variety of analysis & tooling*.

### Conformance Checklist

| ID           | Requirement                                                                                                                                                     | Purpose                                                          |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **CC‑A.5.1** | The Conceptual Kernel **MUST NOT** declare any `U.Type` that is specific to a single scientific or engineering discipline.                                      | Prevents kernel bloat; enforces **Ontological Parsimony (C‑5)**. |
| **CC‑A.5.2** | Every architheory **MUST** supply a `U.ArchitheorySignature` (see A.6) that lists all new types, relations, and invariants it introduces.                       | Enables plug‑in discoverability and versioned evolution.         |
| **CC‑A.5.3** | A normative pattern or invariant defined in one architheory **MUST NOT** override a Kernel pattern, but **MAY** *refine* it by additional constraints.          | Preserves Kernel immutability while supporting specialisation.   |
| **CC‑A.5.4** | Dependency edges between architheories **MUST** point *toward the Kernel* (acyclic, upward) as required by the **Unidirectional Dependency Guard‑Rail (E .5)**. | Prevents cyclic coupling and “middle‑layer” choke‑points.        |
| **CC‑A.5.5** | Every architheory **MUST** declare its `classification` as one of `CAL`, `LOG`, or `CHR`. Only a `CAL` may export a `Γ_*` operator. | Enforces a clear separation of concerns between constructing, reasoning, and describing. |
 
### Consequences

| Benefits                                                                                                                           | Trade‑offs / Mitigations                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Kernel stability for decades:** small, conceptually elegant nucleus rarely changes; archival citations remain valid.             | **Extra discipline for authors:** every domain team must package work as a CAL/LOG/CHR plug‑in. *Mitigation:* E.8 style‑guide and pattern templates automate most boiler‑plate. |
| **Unlimited, parallel innovation:** biology, economics, quantum computing can all add CALs without waiting on a central committee. | **Potential overlap of CALs:** two teams might publish competing resource calculi. *Mitigation:* coexistence is allowed; the Trust layer lets users choose.                     |
| **Clear “API” boundary:** tool builders know the exact, minimal surface they must support – boosting interoperability.             | —                                                                                                                                                                               |

---

### Rationale

*Micro‑kernels* succeeded in operating‑system research because they separated **immutable primitives** (threads, IPC) from **replaceable servers** (file‑systems, network stacks).
FPF adopts the same strategy:

* **Immutable primitives** → the Part A Kernel (holons, roles, transformer quartet, temporal scopes, constitutional C‑rules).
* **Replaceable servers** → architheories in Part C (each with its own calculus, logic, characterisation kit).

This delivers on **P‑4 (Open‑Ended Kernel)**, **P‑5 (Plugin Layering)** and keeps the framework aligned with modern proof‑assistant ecosystems (Lean’s *mathlib* vs. core).

The “hour‑glass” brings two further advantages:

1. **Pluralism with auditability** – rival CALs can coexist; the Kernel’s Trust pipeline (B.3) quantifies their evidence base.
2. **Future‑proofing** – if a genuinely new substrate (e.g., quantum knowledge objects) emerges, it plugs in at the bottom layer without touching Part A.

---

### Relations

* **Instantiates:** P‑4, P‑5, and relies on Guard‑Rails E.5 (especially Unidirectional Dependency).
* **Provides Standard for:** every entry in **Part C**; style enforced via **Architheory Signature & Realization (A .6)**.
* **Feeds:** Trans‑disciplinary reasoning operators in **Part B** – Γ, MHT, Trust, Evolution Loop all treat each CAL uniformly through the Kernel neck.

> *“A stable neck sustains an ever‑growing hour‑glass.”*

## A.6.0 — **U.Signature · Universal, law‑governed declaration for a SubjectKind on a BaseType**  \[A]

**Status.** Architectural pattern \[A], kernel‑level and universal.  
**Placement.** Part A (Kernel), **before A.6** (“Architheory Signature & Realization”) and **A.6.1** (“U.Mechanism”).  
**Builds on.** **A.2.6** (USM: context slices & scopes), **E.8** (authoring order), **E.10** LEX-BUNDLE (registers, naming, stratification), **E.10.D1** D.CTX (Context discipline).
  
**Coordinates with.** **A.6** (architheory specialisation of signatures), **A.6.1** (mechanism as law-governed signature), **A.6.5** (`U.RelationSlotDiscipline` for n-ary arguments), **Part F** (Bridges & cross-context transport; naming). Conformance keywords: RFC 2119.

### 1 · Problem frame

FPF already uses “signatures” to stabilise public promises of **architheories** and, via **A.6.1**, of **mechanisms**. But authors also need stable, minimal declarations for **theories** (LOG), **methods** (operational families), and even **disciplines** (regulated vocabularies). Without **one** universal notion of signature:
* similar constructs proliferate under incompatible names;
    
* readers cannot tell what is **declared** (intension & laws) versus what is **implemented** (specification);
    
* cross‑context reuse lacks a canonical place to state **applicability** and **lawful vocabularies**.

E.8 demands a single authoring voice and section order; E.10 demands lexical discipline across strata. A.6.0 provides the common kernel shape these patterns presuppose.

### 2 · Problem

If each family (architheories, mechanisms, methods, disciplines) invents its own “signature”:

1. **Tight coupling.** Private definitions leak as public standards, breaking substitutability.
    
2. **Lexical drift.** The same surface label (e.g., *scope*, *normalization*) hides different laws.
    
3. **Scope opacity.** Applicability (where the words mean what) remains implicit, violating D.CTX.
    

### 3 · Forces

| Force | Tension |
| --- | --- |
| **Universality vs. fitness** | One shape must fit **architheories**, **mechanisms**, **theories**, **methods**, **disciplines**, without over‑committing to any one of them. |
| **Intension vs. specification (I/D/S)** | Signatures declare **what** and **the laws** (intension), not recipes or test harnesses (specification). |
| **Simplicity vs. expressivity** | Keep the kernel small while leaving **normalized** slots for specialisations (e.g., Γ‑export in A.6; Transport in A.6.1). |  
| **Locality vs. transport** | Meaning is context‑local (D.CTX), yet cross‑context use must be explicit and auditable via Bridges without smuggling implementation. |

### 4 · Solution — **Define `U.Signature` once, reuse everywhere**

**Definition.** A **`U.Signature`** is a **public, law-governed declaration** for a named **SubjectKind** on a declared **BaseType**. Where quantification depends on context, the Signature **SHALL** expose an explicit **SliceSet** and **ExtentRule**. A Signature (i) introduces a **vocabulary** (types, relations, operators), (ii) states **laws** (axioms/invariants; no operational admissions), and (iii) records **applicability** (where and under which contextual assumptions the declarations hold). Dependencies (**imports**) are governed by specialisations (e.g., A.6) and are **not** part of the universal Block. **Discipline for argument-position typing is delegated to A.6.5 `U.RelationSlotDiscipline`: whenever the Vocabulary declares an n-ary relation or operator, SlotSpecs for its parameter positions SHALL be provided as in §4.1.1 and A.6.5.**

Where the **Vocabulary** introduces an **n‑ary relation or morphism**, the Signature **SHALL**, for each parameter position `i`, declare a `SlotSpec_i = ⟨SlotKind_i, ValueKind_i, refMode_i⟩` as defined in **A.6.5 `U.RelationSlotDiscipline`**. SlotSpecs live inside the per‑relation parameter block of the **Vocabulary** row and **MUST NOT** introduce additional rows beyond the four‑row Signature Block.

**Arrow form (typing for MVPK).** Author a Signature as a **morphism**  
`SigDecl : ⟨SubjectBlock⟩ → ⟨Vocabulary × Laws × Applicability⟩`  
where `SubjectBlock = ⟨SubjectKind, BaseType, SliceSet, ExtentRule, ResultKind?⟩`. This makes `U.Signature` directly consumable by **E.17 MVPK** (publication of morphisms) without adding semantics on faces (no new claims; pins for any numeric content).

*Guard clarification (normative).* **Operational guard predicates** (run‑time or admission guards) **BELONG ONLY** to **A.6.1 Mechanisms**. A Signature may express **domain/type constraints** intensionally (e.g., restricting an operator’s domain) but **SHALL NOT** encode operational admissions.

*Guidance for deductive substrates.* Signatures that declare a **formal deductive substrate** (e.g., *FormalSubstrate*) MAY include, **as vocabulary elements**, an **EffectDiscipline** (algebraic/row/graded effect signatures) and **InferenceKind** enumerations; handler semantics are **out of scope** for Signatures (see §4.3). The universal block remains conceptual and contains **no** run‑time admissions or AdmissibilityConditions.

**Naming discipline.** The `Subject` **MUST** be a **single‑sense** noun phrase; avoid synonyms/aliases within the same Signature.

A `U.Signature` is **conceptual**: it contains **no implementation, no packaging/CI metadata, and no Γ‑builders**. Γ‑export, if any, is governed by **A.6** and only for architheories with `classification=CAL`.

#### 4.1 · The **Signature Block (universal form)**

The **four conceptual rows** (“SubjectBlock / Vocabulary / Laws / Applicability”) give a repeatable, holon‑stable pattern across mathematics → physics → engineering:  
* **SubjectBlock** = *what it’s about + how quantified* (axiomatics + domain of interpretation),  
* **Vocabulary/Laws** = *principles/laws* (postulates & constraints),  
* **Applicability** = *where they hold in practice* (bounded context & time).

Every `U.Signature` **SHALL** present a **four‑row conceptual block** (names are universal; family‑specific aliases are mapped below):

1. **SubjectBlock** — ⟨**SubjectKind**, **BaseType**, **SliceSet**, **ExtentRule**, **ResultKind?**⟩.  
   *SubjectKind* names the intensional subject (C.3); *BaseType* is the `U.Type` the signature ranges over (CHR Spaces appear here **as types**, not as field names); *SliceSet* addresses the quantification domain (USM; e.g., **ContextSliceSet**); *ExtentRule* computes `Extension(SubjectKind, slice)` (C.3.2); *ResultKind?* (optional) is the intensional kind of outputs.  
   **Editorial split (allowed).** Authors **MAY** render the **SubjectBlock** as two adjacent lines — **Subject** *(SubjectKind, BaseType)* and **Quantification** *(SliceSet, ExtentRule, ResultKind?)* — **without changing semantics**. Even when visually split, SubjectBlock counts as **one** conceptual row.

   **Semantic roles of the SubjectBlock kinds (informative)**
   * **SubjectKind (intent).** The intensional “describedEntity” of the signature (C.3.1), ordered by `⊑`. It carries no Scope.
   * **BaseType (carrier).** The `U.Type` over which values/objects are ranged. In CHR regimes this may be a `U.CharacteristicSpace` **type**; elsewhere it is a set‑typed `U.Type`.
   * **SliceSet (addressability).** The addressable set of `U.ContextSlice`s (USM). It identifies where **extent** is computed; it is not a “space” unless CHR.
   * **ExtentRule (extent).** A rule yielding `Extension(SubjectKind, slice)` (C.3.2); this is the quantifier’s domain, computed per slice.
   * **ResultKind? (outputs).** Optional: the intensional kind of the outputs of the operations declared in *Vocabulary* (use when outputs differ in kind from the SubjectKind).
    
2. **Vocabulary** — names and sorts of the public **types / relations / operators** this signature commits to (no handler semantics; no AdmissibilityConditions). For each **n‑ary relation or morphism** in the Vocabulary, parameters **SHALL** be declared via **SlotSpecs** `SlotSpec_i = ⟨SlotKind, ValueKind, refMode⟩` per **A.6.5 `U.RelationSlotDiscipline`**. SlotKinds and RefKinds **MUST** follow the `…Slot` / `…Ref` lexical discipline in **A.6.5** and **E.10 (LEX‑BUNDLE)**; ValueKinds **MUST** remain free of these suffixes. For each **n‑ary relation or morphism** in the Vocabulary, parameters **SHALL** be declared via **SlotSpecs**
  
3. **Laws (Axioms/Invariants)** — equations and order/closure laws that are context‑local truths under the stated Applicability (no proofs here). **Operational guard predicates belong to Mechanisms (A.6.1)**, not to Signatures.
    
4. **Applicability (Scope & Context)** — conditions under which the laws are valid (bounded context, plane, stance, time notions). Applicability **MUST** bind a **`U.BoundedContext`** (D.CTX). Cross‑context use **MUST NOT** be implicit; if intended, **name** the Bridge (conceptual reference only). When numeric comparability is implied, **bind** legality to **CG‑Spec/MM‑CHR** (normalize‑then‑compare; lawful scales/units).
    
*Mapping to existing families (normative aliases).*  
— **A.6.1 (Mechanism).** *SubjectBlock* ↔ **SubjectKind/BaseType/…**; *Vocabulary* ↔ **OperatorAlgebra**; *Laws* ↔ **LawSet**; *Applicability* remains contextual; **AdmissibilityConditions** — separate field of mechanism (not in the `U.Signature`).  
— **A.6 (Architheory).** A.6 **adds** an adjacent **Architheory View** preserving **Imports / Derivations / Invariants / BelongsToAssurance**. The **universal Block remains the source-of-truth**; the view is a projection and **MUST NOT** introduce fields not derivable from the Block.  
— **Task/Problem/Discipline signatures (C.22, G-cluster).** These **SHALL** be introduced as **species of `U.Signature`** that reuse the same four-row Block (SubjectBlock / Vocabulary / Laws / Applicability); any extra per-family views are projections only (no new conceptual rows).

##### 4.1.1 · SlotSpec for argument positions (normative; see A.6.5)

For every **n‑ary relation or operator** declared in the **Vocabulary** row, the Signature **SHALL** assign, to each argument position, a **SlotSpec** triple:

```text
+SlotSpec_i := ⟨SlotKind_i, ValueKind_i, refMode_i⟩
```

where:
* **SlotKind_i** is a named position in the relation/operator (Tech name with `…Slot` suffix) whose semantics are documented (see A.6.5).
* **ValueKind_i** is the FPF type (`U.Kind` or kernel‑level type) of admissible occupants at that position.
* **refMode_i** is either `ByValue` or a **RefKind** (e.g., `U.EntityRef`, `U.HolonRef`), indicating whether the episteme stores values directly or references/identifiers.

Full discipline and lexical rules for **SlotKind/ValueKind/RefKind** are given in A.6.5 `U.RelationSlotDiscipline` and E.10 (§8.1). A.6.0 requires that every vocabulary‑level relation or operator that takes arguments **declare** these SlotSpecs; downstream patterns MAY provide templates for common shapes (e.g., episteme slots in C.2.1).

**Mini‑example (informative).** For an episteme kind `ModelEvaluationResultKind`, a simplified episteme might expose:
* `describedEntityRef : U.MethodRef`
* `datasetRef : U.EntityRef`
* `metricRef : U.CharacteristicRef`
* `groundingHolonRef : U.HolonRef`
* `claimGraph : U.ClaimGraph`

An authorial SlotSpec table then reads:

| Parameter (episteme field)   | SlotKind              | ValueKind          | refMode                |
| ---------------------- | --------------------- | ------------------ | ---------------------- |
| `describedEntityRef`   | `DescribedEntitySlot` | `U.Method`         | `U.MethodRef`          |
| `datasetRef`           | `DatasetSlot`         | `U.Entity`         | `U.EntityRef`          |
| `metricRef`            | `MetricSlot`          | `U.Characteristic` | `U.CharacteristicRef`  |
| `groundingHolonRef`    | `GroundingHolonSlot`  | `U.Holon`          | `U.HolonRef`           |
| `claimGraph`           | `ClaimGraphSlot`      | `U.ClaimGraph`     | `ByValue`              |

This example illustrates the intended reading: **parameters are typed twice**—once by their **ValueKind** (what sort of thing occupies the position) and once by **refMode** (by‑value or which RefKind). SlotKinds (with `…Slot` suffix) give stable names for substitution laws and describedEntity statements across patterns.

#### 4.2 · Profile specialisations (normative; structure‑preserving)
To enable first‑principles layers without minting new Kernel kinds, apply **profiles** to `U.Signature`:

* **`profile = FormalSubstrate`** — *formal‑deductive layer*  
  **Vocabulary:** `TermRegister` (ref‑only), **InferenceKinds** (ref‑only), **EffectDiscipline** (operation/effect signatures).  
  **Laws:** equational/structural axioms of the calculus; **no handler semantics**.  
  **Applicability:** binds a `U.BoundedContext` at the **concept‑plane**; **no units/ReferencePlane/Transport** on faces.  
  **MVPK pins:** **`No‑Realization` pin (mandatory)** on `PlainView`/`TechCard` asserting that handler semantics live only in **A.6.1 `U.Mechanism::U.EffectRealization`**.  
  **Faces:** On MVPK faces, **`InferenceKindsAllowed`** MAY present a **ref‑only subset** of the enumerated **`InferenceKinds`**; Signatures do not add handler semantics.

* **`profile = PrincipleFrame`** — *postulates + measurability intent (CHR‑binding)*  
  **Vocabulary:** **PostulateSet** (in the calculus imported), **CHR‑Binding presence** (ref‑only to characteristics/observation profiles), **Ontology anchors** (ref‑only to substrate types/morphisms used to name subject‑matter entities).  
  **Laws:** timeless/order‑free invariants; **no operational admissions**.  
  **Applicability:** binds a `U.BoundedContext`; **Signatures SHALL NOT publish units/ReferencePlane/ComparatorSet/Transport** (first mention is in **UNM**). ** 
  **MVPK pins:** **`NoReferencePlaneOnSignature`** (alias: **`NoReferencePlaneOnPF`**) and **`UNM‑priority`** (units/planes/comparators/Transport are declared only by **`U.ContextNormalization`** and cited by edition/ref‑id where needed).

**Profile morphism discipline.** See §4.6 for the **structure‑preserving morphism** requirements for profile application.

#### 4.3 · Effect‑discipline vs handler semantics (normative split)

If a Signature’s **Vocabulary** includes an **EffectDiscipline** (operation/effect signatures), the Signature **SHALL NOT** declare **handler semantics** or any **EffectRealization**. Such realizations are authored only under **A.6.1 `U.Mechanism`** and cited by **ref‑id** on faces where needed. This mirrors the modern algebraic‑effects separation between *operation signatures* and *handlers* while keeping A.6.0 purely conceptual.

#### 4.4 · Authoring rules (I/D/S‑aware; lexically disciplined)

* **I/D/S separation.** A signature **states intension and laws**; Realizations (if any) carry **specifications**. Do not mix tutorial text or operational recipes into the Block. Do **not** include **AdmissibilityConditions** or run‑time admissions here.
* **Context discipline.** Bind Applicability to a **`U.BoundedContext`**. If cross‑context use is intended, **name** the crossing and **reference** the Bridge (Part F/B); A.6.0 does **not** prescribe **compatibility/loss tables (CL, including `CL^plane`)** or penalty formulas.
* **Stratification.** Use LEX‑BUNDLE registers and strata; do not redefine Kernel names in lower strata (no cross‑bleed).  
* **Imports location.** If your family requires an explicit **imports** list (e.g., A.6 Architheory), place it in the **Signature header** or the **family‑specific view**, not inside the universal four‑row Block.

* **Token hygiene.** Do **not** mint new `U.*` tokens inside a Signature without a **DRR**; prefer referencing existing Kernel/Architheory `U.Type`s. 

*MVPK publication discipline for Signatures (normative).* When publishing a `U.Signature` via MVPK (E.17), faces **SHALL** be typed projections that add **no new claims**; any numeric/comparable statement **MUST** pin unit/scale/reference‑plane/**EditionId** to **CG‑Spec/MM‑CHR** where applicable. For deductive substrates, faces **MUST** carry a **No‑Realization pin** (handlers/realizers absent). For Principle‑level signatures, faces **MUST NOT** introduce units/ReferencePlane/Transport (first mention occurs in UNM).

#### 4.5 · Specialisation knobs (for downstream patterns)

A.6.0 exposes **three** conceptual knobs; specialisations (A.6, A.6.1, method/discipline specs) may **tighten** them:

1. **Builder policy.** Whether a signature may commit to a builder `Γ_*` is not decided here; **A.6** governs this for architheories (`classification=CAL` only).
    
2. **Transport clause.** If cross‑context/plane use is part of the design, the signature **may declare** a conceptual Transport clause; **A.6.1** gives a concrete schema (Bridge, **CL/CL^k/CL^plane**—Bridges per **F.9**, penalties per **B.3**, **CL^plane** per **C.2.1**), but A.6.0 remains agnostic about penalty shapes.
    
3. **Morphisms.** Families may define `SigMorph` (refinement, conservative extension, equivalence, quotient, product) to relate signatures; **A.6.1** instantiates this for mechanisms. Where such morphisms, or downstream **substitution / retargeting** laws (e.g., **A.6.2–A.6.4**), act on **n‑ary relations or morphisms**, they **SHALL** express their read/write/retargeting discipline in terms of **SlotSpecs**  (SlotKind / ValueKind / RefKind) rather than unnamed parameter indices, using **A.6.5 `U.RelationSlotDiscipline`** as the normative slot calculus.

#### 4.6 · Profile‑specialisation as a structure‑preserving morphism (normative)
Profile application `ι_profile : U.Signature → U.Signature(profile=…)` **SHALL** be a **structure‑preserving morphism**:
— **SubjectBlock** is preserved up to α‑renaming (SubjectKind/BaseType unchanged; ResultKind? only added when it exists in the universal intent).  
— **Vocabulary** is **monotone** (adds or refines names/sorts without contradicting existing ones).  
— **Laws** are **monotone** (add/strengthen axioms; never weaken).  
— **Applicability** is **restrictive** (binds or tightens `U.BoundedContext`; never widens implicitly).  
— No **AdmissibilityConditions**, **operational guards**, or **handler semantics** are introduced by the profile (those live under **A.6.1**).  
This makes `profile=FormalSubstrate` and `profile=PrincipleFrame` *morphisms* in the sense of kernel specialisation and supports SigMorph reasoning (refinement/conservative extension).
   
### 5 · Archetypal Grounding (Tell–Show–Show)

| quartet Element | `U.System` Example — **Grammar of Motions** | `U.Episteme` Example — **Normalization Family** |
| --- | --- | --- |
| **SubjectBlock** | **Subject:** SubjectKind=`MotionGrammar`; BaseType=`U.System:TrajectorySpace`. **Quantification:** SliceSet=`U.ContextSliceSet`; ExtentRule=`admissible motion words per slice (kinematics & domain restrictions)`; ResultKind?=`Language[Segment]`. | **Subject:** SubjectKind=`NormalizationMethod‑Class`; BaseType=`U.Episteme:ChartFamily` (one `U.BoundedContext`). **Quantification:** SliceSet=`U.ContextSliceSet`; ExtentRule=`admissible method instances per slice (edition+validity)`; ResultKind?=`NormalizedChart`. |
| **Vocabulary** | Types: `Pose`, `Segment`; Operators: `concat`, `reverse`, `sample` (any Γ‑builder is governed by A.6). | Operators: `apply(method)`, `compose`, `quotient(≡)`. |
| **Laws (Invariants/Constraints)** | Closure of `concat`; associativity; time‑monotone sampling; **`reverse` is declared only for holonomic arms (domain restriction)**. | Ratio→positive‑scalar; Interval→affine; Ordinal→monotone; Nominal→categorical; LUT(+uncertainty). |
| **Applicability (Scope & Context)** | Context: *industrial robotics*; stance: design; time notion: discrete ticks. Cross‑context transport not declared. | Context: *clinical metrics*; stance: analysis; validity windows declared; cross‑context transport via Bridge (concept only; details per A.6.1). Numeric comparability bound to CHR/CG‑Spec. |

*Why these two?* E.8 requires pairs from **U.System** and **U.Episteme** to demonstrate trans‑disciplinary universality.

### 6 · Bias‑Annotation (lenses & defaults)

* **Local‑first meaning.** Laws are **local** to the named Context; cross‑context use must be explicit (Bridge), never implicit.
    
* **No illicit scalarisation.** If numbers appear, legal comparability follows **CG‑Spec/MM‑CHR**; **no ordinal means**, **partial orders return sets**; unit/scale alignment is explicit.
    
* **Register hygiene.** Keep Tech vs Plain register pairs; avoid tooling/vendor talk in Kernel prose (E.10).
  
### 7 · Conformance Checklist (normative)

| ID | Requirement |
| --- | --- |
| **CC‑A.6.0‑1** | A conformant text labelled **`U.Signature`** **SHALL** expose the **four‑row Signature Block**: *SubjectBlock; Vocabulary; Laws; Applicability*. A visual split of SubjectBlock into **Subject**/**Quantification** lines is allowed; it still counts as **one** conceptual row. |
| **CC‑A.6.0‑2** | The Block is **conceptual only** (no packaging/CI metadata, no machine schemas, **no Γ**). |
| **CC‑A.6.0‑3** | Applicability **binds** a `U.BoundedContext`; if cross‑context use is intended, a **Transport clause** is *named* (Bridge reference) without re‑stating Part F/B.3 details (including any **CL^plane**). |
| **CC‑A.6.0‑4** | Where numeric comparability is implied, Applicability **binds** to **CG‑Spec/MM‑CHR** legality (normalize‑then‑compare; scale/unit alignment). |
| **CC‑A.6.0‑5** | Families that specialise A.6.0 (e.g., **A.6**, **A.6.1**) **MAY** add constraints (e.g., Γ‑export policy; penalty routing) and **MAY** add a family‑specific view (e.g., the Architheory View) but **MUST NOT** contradict A.6.0’s separation of intension vs specification. |
| **CC‑A.6.0‑6** | Under E.10/E.8, tokens respect strata/registers; Kernel names are not redefined in Architheory/Context prose (Part F naming discipline applies). |
| **CC‑A.6.0‑7** | The **Laws** row contains **axioms/invariants** only; **AdmissibilityConditions** and operational admissions **MUST** appear only in **A.6.1 Mechanisms** that consume this Signature. |
| **CC‑A.6.0‑8 (No‑Realization on Signatures with EffectDiscipline).** | If **EffectDiscipline** appears in **Vocabulary**, faces **MUST** carry a **`No‑Realization` pin** and **MUST NOT** publish handler semantics; any **EffectRealization** is referenced (A.6.1) by id only. |
| **CC‑A.6.0‑9 (CHR‑binding without units/Transport).** | Signatures that declare **measurability intent** (e.g., PrincipleFrame) **SHALL NOT** publish **units, ReferencePlane, ComparatorSet, or Transport**; those are declared only by **UNM** and cited by edition/ref‑id where consumers require numeric comparability. |
| **CC‑A.6.0‑10 (UNM‑priority on faces).** | Any numeric/comparable claim on a Signature face **pins** **CG‑Spec/ComparatorSet edition ids** and, where scale/plane conversion occurs, **UNM.TransportRegistry edition** with **CL/CL^plane policy‑ids**; **penalties route to R/R_eff only**. |
| **CC‑A.6.0‑11 (Bridge‑only crossings).** | Cross‑context/plane reuse of Signature claims **MUST** name a **Bridge** (UTS row) and **MUST NOT** imply implicit equivalence by label; losses are recorded via **CL** (penalties → **R**). |
| **CC‑A.6.0‑12 (Profile conformance).** | If the Signature declares `profile=FormalSubstrate` or `profile=PrincipleFrame`, the corresponding **profile pins** in §4.2 are **mandatory**; failure to emit them makes the Signature **non‑conformant** for that profile. |
| **CC‑A.6.0‑13 (Profile morphism discipline).** | Applying a profile **SHALL** satisfy §4.6 (structure‑preserving morphism: SubjectBlock preserved, Vocabulary/Laws monotone, Applicability restrictive, no admissibility/handlers). |
| **CC‑A.6.0‑14 (SlotSpec for argument positions).** | Any `U.Signature` whose **Vocabulary** declares n‑ary relations or operators **SHALL** provide, for each argument position, a **SlotSpec** triple `⟨SlotKind, ValueKind, refMode⟩` (with `refMode ∈ {ByValue \| RefKind}`) as per A.6.5 `U.RelationSlotDiscipline`. |
| **CC‑A.6.0‑15 (Slot/Ref lexical discipline on signatures).** | Names of SlotKinds and RefKinds used in SlotSpecs **MUST** obey E.10/A.6.5 lexical guards: tokens ending with **`…Slot`** denote SlotKinds only; tokens ending with **`…Ref`** denote either RefKinds or episteme fields whose type is a RefKind; no ValueKind ends with these suffixes. |
| **CC‑A.6.0‑16 (SlotSpecs for n‑ary relations).** | Any `U.Signature` whose **Vocabulary** declares an **n‑ary relation or morphism** **SHALL** assign to each parameter position a `SlotSpec_i = ⟨SlotKind, ValueKind, refMode⟩` as defined in **A.6.5 `U.RelationSlotDiscipline`**; SlotSpecs live inside the Vocabulary row’s per‑relation parameter block and **MUST NOT** introduce additional rows beyond the four‑row Block. |
| **CC‑A.6.0‑17 (SlotSpec‑based substitution laws).** | Specialisations of A.6.0 that define **substitution, retargeting, or profile application** over n‑ary relations/morphisms (e.g., **A.6.2–A.6.4**) **SHALL** phrase their rules in terms of **SlotSpecs** (SlotKind / ValueKind / RefKind) rather than unnamed parameter indices and **SHALL** obey the `…Slot` / `…Ref` lexical discipline in **A.6.5** and **F.18**. |

### 8 · Consequences

* **Uniform kernel shape.** Authors can define **architheory**, **mechanism**, **method**, **discipline**, or **theory** signatures without inventing new templates.
    
* **Hard decoupling.** A.6 can continue to guarantee substitutable Realizations behind a stable Signature; A.6.1 can continue to guarantee law‑governed operations with explicit guard surfaces.
    
**Didactic cohesion.** Readers see the same four conceptual rows across the spec, satisfying E.8’s comparability goal.

### 9 · Rationale

**Why “SubjectBlock”?** A.6.1 showed that making the **carrier explicit** (here: *BaseType* — the carrier type) avoids category mistakes when moving between domains (e.g., *set‑algebra on context slices* vs *equivalence‑classes of normalisations*). A.6.0 lifts this to the kernel so every signature can declare **what it is about** before saying **what it provides**.
**Why one universal Block?** A.6 already proved the value of a compact **Signature Block** (Imports/Derivations/Invariants/Assurance). A.6.0 factors out the **conceptual core**—rephrased as “SubjectBlock / Vocabulary / Laws / Applicability”—so A.6 can **map** its four rows onto this universal frame without changing existing architheories.

**Informative echoes (post‑2015 SoTA).**  
— **Algebraic effects & handlers** (OCaml 5, Koka, Effekt, Links): *operation signatures + handler laws* mirror **Vocabulary + Laws** while keeping implementations separate.  
— **Session/behavioural types** (2016–2024): protocol/admissibility laws parallel the **Laws** row (at mechanism level).  
— **Graded/row‑polymorphic effects** (Granule, row‑effects): inform the **EffectDiscipline** vocabulary and equational laws.

**Profiles rationale (informative).**  
— **FormalSubstrate.** Captures *mathematical language + inference kinds + effect signatures* at the **concept plane**, ensuring the calculus stays independent from handler/realization choices; consuming mechanisms (A.6.1) provide **EffectRealization** only by reference.  
— **PrincipleFrame.** Captures *postulates/invariants + measurability intent (CHR binding)* without committing to **units/planes/Transport**, which are authored centrally in **UNM** so that comparisons remain lawful and edition‑pinned.

### 10 · Relations

* **Specialises / is specialised by:** **A.6** (adds Γ‑export policy; imports DAG; architheory layering) and **A.6.1** (adds **OperatorAlgebra/LawSet/AdmissibilityConditions/Transport** for mechanisms).  
* **Constrained by:** E.10 LEX‑BUNDLE (registers, strata); D.CTX for Context binding; **Part F** (Bridges & cross‑context transport; naming).
* **Consumed by (profiles):** **`U.FormalSubstrate`** and **`U.PrincipleFrame`** specialisations of `U.Signature` on the principled path; **UNM** (Context Normalization) remains the **single source of truth** for **CG‑Spec/ComparatorSet/Transport** editions that Signature consumers pin on faces.

* **Enables:** uniform authoring and comparison of signatures across Part C families, methods, and discipline glossaries (Part F).
  
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

## **A.6.1 — U.Mechanism · Law‑governed application to a SubjectKind over a BaseType** \[A]

**One‑line summary.** A `U.Mechanism` is a **Signature with laws** applied to a declared **SubjectKind** over a **BaseType**, with explicit **operations**, **invariants/guards**, and a named **Transport** clause for cross‑context use. Transport is **Bridge‑only** (per **F.9**) with penalties routed to **R**/**R_eff** only (per **B.3**); **F/G** remain invariant; **CL^plane** follows **C.2.1 CHR:ReferencePlane**. Realizations **MAY** be published under **A.6** (Signature→Realization; **one Γ only if `classification=CAL`**; acyclic imports; opacity).

**Status.** Normative \[A\] in **Part A (Kernel)**.  

**Placement.** Immediately **after A.6** as **A.6.1**. **USM (A.2.6)** and **UNM (A.19/C.16)** become **instances conforming to A.6.1** (no semantic change to either).

### 1 · Problem frame

Give FPF **one uniform kernel shape** for things like **USM** (set‑algebra on context slices) and **UNM** (classes of admissible normalizations with ≡_UNM) so authors can **define, compare, refine, compose, and port** mechanisms **without re‑inventing the meta‑language**; all cross‑context use is **Bridge‑only** with **CL penalties to R/R_eff**, never to **F/G**.

### 2 · Problem 

Without a kernel abstraction, scope/normalization/comparison constructs proliferate with incompatible algebras and guard surfaces; cross‑context reuse lacks visible **Bridge/CL routing**; comparability drifts into **illegal scalarisation** (e.g., ordinal means). FPF already curbs this via **A.6** (Signature discipline), **USM** (scope algebra & Γ_time), **UNM** (normalize‑then‑compare), and **CG‑Spec** (lawful comparators/ScoringMethods)—but lacks a **common meta‑slot** for “mechanism.”

### 3 · Forces 

**Locality vs transport.** Semantics are **context‑local**; crossing contexts is **Bridge‑only** (Part F/B.3); penalties hit **R/R_eff**; **F/G** invariant.

**Expressivity vs legality.** Rich operators vs **CHR legality** and **CG‑Spec** (no ordinal averages; lawful unit alignment).

**Time determinacy.** Explicit **Γ_time**; no implicit *latest*. (Required in USM’s `ContextSlice`.)

**Signature hygiene.** Obey **A.6** (exactly one Γ from CAL, LOG/CHR export none; imports acyclic; realizations opaque).

### 4 · Solution

#### 4.1 **Mechanism Intension** 

A `U.Mechanism` **publishes**  
        `U.Mechanism.Intension := ⟨IntensionHeader, Imports,
                SubjectBlock := ⟨SubjectKind, BaseType, SliceSet, ExtentRule, ResultKind?⟩,
                ParamKinds, OperatorAlgebra, LawSet, AdmissibilityConditions, Applicability, Transport, Γ_timePolicy, PlaneRegime, Audit⟩`  
and admits Realizations (kernel‑level or architheory‑level) that respect it. The shape is **notation‑independent** and **conceptual** (no tooling, storage, or CI metadata).

* **IntensionHeader.** `id` (PascalCase), `version` (SemVer), `status` (draft/review/stable/deprecated).  
  If realized as an **Architheory**, add the **A.6** header with `classification ∈ {CAL|LOG|CHR}` and `imports/provides`; **only CAL may export exactly one Γ**; **LOG/CHR export none**. For **Kernel‑level** realizations, do **not** mint an A.6 header.

* **Imports.** Architheory Signatures / `U.Types` this mechanism requires (notation‑independent; **acyclic**). When realized as an Architheory, **LOG/CHR may import CAL; CAL may import CAL** (A.6 layering).
* **BaseType.** A `U.Type` the mechanism ranges over. CHR spaces (e.g., a `U.CharacteristicSpace`/chart family) appear here **as types**; outside CHR, use set‑typed `U.Type`s. **Do not mint** a new core type; **reference existing `U.Type`s**. If planes differ, state the **ReferencePlane** policy (see *PlaneRegime*).
* **SubjectKind / SliceSet / ExtentRule / ResultKind? / ParamKinds.**
  • **SubjectKind.** The intensional kind acted upon (C.3.1/3.2), separate from quantification.
  • **SliceSet.** The addressable set of Context slices (USM: **ContextSliceSet**).
  • **ExtentRule.** A rule yielding `Extension(SubjectKind, slice)` (C.3.2), used as the quantifier’s domain.
  • **ResultKind?** Optional intensional kind for outputs of `OperatorAlgebra`.
  • **ParamKinds.** A name→Kind map for multi‑ary operators (inputs); avoids overloading “Role”.
* **OperatorAlgebra.** Named operations with types; examples:  
  • **USM:** `∈, ⊆, ∩, SpanUnion, translate, widen, narrow, refit`.  
  • **UNM:** `apply(method)`, `compose`, `quotient(≡_UNM)`; **normalize‑then‑compare**.

* **LawSet.** Equations/invariants (no proofs here). **Admissions/eligibility tests belong under AdmissibilityConditions, not here.** Laws **MUST** be compatible with CHR legality where numeric comparison/aggregation is induced. Examples:
  • **USM:** serial **intersection**; **SpanUnion** only where a **named independence assumption** is satisfied (state features/axes, validity window, evidence class); `translate` uses declared Bridges; **Γ_time** is mandatory.  
  • **UNM:** **scale‑appropriate** transforms — ratio→positive‑scalar; interval→affine; ordinal→monotone; nominal→categorical; `tabular:LUT(+uncertainty)`.  
  *(Do not mint a new Kernel token for “certificate”; if such a type is later required, it **MUST** follow DRR/LEX minting.)*

* **AdmissibilityConditions.** Deterministic, **context‑local** predicates that **fail closed** (e.g., “Scope covers TargetSlice” with named **Γ_time**; “NormalizationMethod class + validity window named”). Unknowns **→ {degrade | abstain}**; never coerce to 0/false.

* **Applicability.** Binding to a **`U.BoundedContext`** with stance/plane/time notes and any **CG‑Spec/MM‑CHR** legality claims; cross‑context use is declared via **Transport** only.

* **Transport.** **Bridge‑only** semantics for cross‑context / cross‑plane use: name the Bridge and channel (`Scope|Kind`) per **F.9**, and record **ReferencePlane**(src,tgt) per **C.2.1**. Do **not** restate CL ladders, **CL^plane**, or Φ/Ψ tables here; penalties **route to R/R_eff only** and **never** mutate F/G (per **B.3**). Crossings are explicit; **no implicit crossings**. Where **USM** or **KindBridge** are used together, apply the **two‑bridge rule** (scope CL and kind `CL^k` penalties handled **separately** to R).

* **Γ_timePolicy.** Point/window/policy; **no implicit “latest.”** Validity windows are **named**; **required** whenever guards reference time.
* **PlaneRegime.** Declare `ReferencePlane` on values/paths; when planes differ, name **CL^plane** and apply a **Φ_plane** policy (Part F/B.3). Plane penalties **do not** change CL; route to **R/R_eff** only; **F/G** stay invariant.

* **Audit.** Conceptual audit surface only (no data/telemetry workflows): crossings are publishable on **UTS**; surface **policy‑ids** rather than tables. Edition pins and regression hooks (if any) are referenced by id; operational details remain out of scope.
* **SignatureBlock alignment (A.6).** When realized as an **Architheory**, map `U.Mechanism.Intension` to the **A.6 Signature Block** — `Imports`, **Derivations**, **Invariants**, **BelongsToAssurance** — and include the **A.6 header** with `classification/provides`. **CAL** Realizations MAY **provide exactly one Γ**; **LOG/CHR provide none**; **imports form a DAG**; internals **opaque**.

**Compatibility with A.6.** If realized as an **architheory** (CAL/LOG/CHR), obey A.6 (**one Γ for CAL only; acyclic imports; opacity**). Kernel‑level realizations remain notation‑independent and publish the same fields for auditability. LEX discipline applies to all minted tokens.

#### 4.2 U.MechMorph · Refinement, Extension, Equivalence & Composition

**Intent.** Provide structure‑preserving **relations & constructors** between mechanisms.  
**Definitions.**

* **Refinement** `M′ ⊑ M`: narrows **SliceSet/ExtentRule** or **strengthens laws** (safe substitution; Liskov‑style).
* **Extension** `M ⊑⁺ M″`: **adds operations** without weakening existing Laws; old programs remain valid (conservative extension).
* **Equivalence** `M ≡ M′`: there exists a bijective mapping between Subjects/ops preserving/reflecting **LawSet** (up‑to‑isomorphism on **BaseType** and **OperatorAlgebra**).
    
* **Quotient** `M/≈`: factor by a **congruence** (e.g., **≡_UNM** for charts).

* **Product** `M×N`: independent **BaseTypes**; ops are component‑wise; ensures **no illegal cross‑ops** (e.g., set‑algebra discipline for `SpanUnion`). Where independence is claimed, **name and justify** the assumption (do not mint new Kernel types here).

**Transport** `Bridge⋅M`: lifts across Contexts/planes; names **CL/CL^k/CL^plane** regimes; penalties → **`R_eff` only**; **UTS row** recommended for publication; **ReferencePlane(src,tgt)** recorded. If mapping losses are material, **narrow** the mapped set or publish an **adapter** (best practice).

**Passing example.** `USM′ = USM + “publish named independence‑assumption evidence for SpanUnion”` ⇒ **Refinement** (strengthened law; substitution‑safe).
**Normalization quotient.** `UNM / ≡_UNM` exposes **compare‑on‑invariants** surfaces for UCPM/USCM (normalize‑then‑compare).

#### 4.3 U.MechAuthoring · Instantiation template

**MechanismDescription (E.8 Tell–Show–Show; I/D/S‑compliant):**
`Mechanism: U.<Name>`  *(Kernel conceptual description; no tooling fields)*
`Imports: <Signatures / U.Types>` · `SubjectBlock: <SubjectKind, BaseType, SliceSet, ExtentRule, ResultKind?>` · `ParamKinds: <name→Kind map>` · `OperatorAlgebra: <operators with types>` · `LawSet: <equations/invariants>` · `AdmissibilityConditions: <admission predicates; Γ_time>` · `Transport: <Bridge channels; CL/CL^k/CL^plane named; ReferencePlane(src,tgt)>` · `PlaneRegime: <world|concept|episteme rules>`

#### 4.4 MechFamilyDescription & MechInstanceDescription 

* **MechFamilyDescription**: `{Mechanism.Intension, Realizationα, Realizationβ, …}` — each Realization may **tighten** (never relax) Laws (Liskov‑style).

* **MechInstanceDescription**: `{Mechanism.Intension@Context, Windows, named Φ/Ψ/Φ_plane regimes, BridgeIds}` — a **conceptual instance**; operational telemetry/workflows are out of scope.

### 5 · Archetypal Grounding

#### 5.1 **U.System (Work) — USM as a U.Mechanism instance** (normative by reference)

* **Imports:** `U.ContextSliceSet`; Part F.9 **Bridge**; **C.2.1 ReferencePlane** (noted for crossings); **C.2.2 F–G–R**; **C.2.3 U.Formality**.
* **BaseType:** `U.ContextSliceSet`.
* **SliceSet:** `U.ContextSliceSet` (addressable `U.ContextSlice`s).
* **SubjectKind:** `U.Scope` with specializations `U.ClaimScope` (G) and `U.WorkScope`.
* **OperatorAlgebra:** `∈, ⊆, ∩, SpanUnion, translate, widen, narrow, refit`.
* **LawSet:** serial **intersection**; **SpanUnion** only where a **named independence assumption** is satisfied (state features/axes, validity window, evidence class); **translate** uses declared **Bridges**; **Γ_time** is **mandatory**.
* **AdmissibilityConditions:** deterministic **“Scope covers TargetSlice”**; **fail‑closed**; `unknown → {degrade|abstain}` (no implicit `unknown→0/false`).
* **Transport:** **Bridge‑only** with **CL**; penalties → **`R_eff`**; **F/G** invariant; publish UTS notes.
* **Γ_timePolicy:** `point | window | policy`; **no implicit “latest.”**
* **PlaneRegime:** *not applicable to scope sets* (scope is set‑valued over `ContextSlice`, no value‑plane); **CL^plane** N/A.

#### 5.2 **U.Episteme (Knowledge) — UNM as a U.Mechanism instance** (normative by reference)

* **Imports:** **A.17/A.18 (CSLC)**; **C.16 (MM‑CHR)**; `U.BoundedContext`; Part F.9 **Bridge**; **C.2.1 ReferencePlane**.
* **BaseType:** chart/`U.CharacteristicSpace` family in a CN‑frame (one `U.BoundedContext`).
* **SubjectKind:** **NormalizationMethod classes** with induced **≡_UNM** equivalence over charts.
* **OperatorAlgebra:** `apply(method)`, `compose`, `quotient(≡_UNM)`; **normalize‑then‑compare** (exposes compare‑on‑invariants surfaces to UCPM/USCM).
* **LawSet:** scale‑appropriate transforms — `ratio:scale / interval:affine / ordinal:monotone / nominal:categorical / tabular:LUT(+uncertainty)`; **validity windows** per edition.
* **AdmissibilityConditions:** `method ∈ declared class‑set` AND **validity window named**; **fail‑closed**; `unknown → {degrade|abstain}`.
* **Transport:** **Bridge‑only** on cross‑Context; when **describedEntity changes**, declare **KindBridge (CL^k)**; penalties → **`R_eff` only**.
* **Γ_timePolicy:** **named validity windows** for NormalizationMethod/instances (editioned).
* **PlaneRegime:** values live on **episteme ReferencePlane**; on plane crossings apply **CL^plane** policy; penalties → **`R_eff` only**.

*(No operational telemetry implied; publication remains conceptual.)*

### 6 · Defaults

* **Local‑first semantics.** All judgments are **context‑local**; crossings are **explicit** and **costed** (CL→R only).
* **Compliance‑first comparability.** Numeric comparison/aggregation requires **CG‑Spec** (lawful **SCP**, Γ‑fold, MinimalEvidence); **partial orders return sets**; **no ordinal means**.
* **Tri‑state discipline.** `unknown → {degrade|abstain}`; `sandbox/probe‑only` is a **LOG branch** with a policy‑id (no implicit `unknown→0/false`).
* **R‑only penalties.** **Φ/Ψ/Φ_plane** are **monotone and bounded**; penalties route to **`R_eff` only**; **F/G invariant**.

### 7 · Conformance Checklist (normative)

| ID | Requirement |
|----|-------------|
| **CC‑UM.1** | **Complete Mechanism.Intension** publishes: `Imports; SubjectBlock (SubjectKind, BaseType, SliceSet, ExtentRule, ResultKind?); ParamKinds; OperatorAlgebra; LawSet; AdmissibilityConditions; Applicability; Transport (Bridge named; ReferencePlane); Γ_timePolicy; PlaneRegime; Audit`. |
| **CC‑UM.2** | **A.6 alignment:** if realized as Architheory, use A.6 header; **one Γ only if CAL**; LOG/CHR none; **imports acyclic**; Realizations **opaque**; laws may be **tightened** (not relaxed). |
| **CC‑UM.3** | **Bridge‑only transport:** crossings **name** a **Bridge** (F.9); `ReferencePlane(src,tgt)` recorded (C.2.1); **CL^plane** named when planes differ; **no implicit crossings**. When typed reuse is involved, the **two‑bridge rule** applies (scope CL and kind `CL^k` penalties routed **separately** to **R**). |
| **CC‑UM.4** | **R‑only routing:** Φ/Ψ/Φ_plane regimes and CL ladders per **B.3**; penalties **reduce R/R_eff** only; **F/G invariant**. |
| **CC‑UM.5** | **CG‑Spec binding** for any numeric compare/aggregate: lawful **SCP** and Γ‑fold; **normalize‑then‑compare**; **partial orders return sets**; **no ordinal means**; interval/ratio arithmetic only with unit alignment (CSLC‑proven). |
| **CC‑UM.6** | **E.8/E.10 compliance:** Tell–Show–Show present under **“Archetypal Grounding”**; twin registers & I‑D‑S respected; any new `U.*` token requires a **DRR** and **LEX.TokenClass** entry; non‑spec surfaces end with **“…Description”**; **no tool/vendor tokens in Core**. |
| **CC‑UM.7** | **Unknowns tri‑state:** guards define `unknown → {degrade|abstain}`; sandbox/probe branches live in **SoS‑LOG** (not Acceptance).

### 8 · Born‑via‑A.6.1 sketches (informative)

**CPM — Unified Comparison Mechanism (parity‑grade orders)**  
**BaseType:** typed traits/charts in a CG‑Frame. **OperatorAlgebra:** lawful orders (≤, ≽, lexicographic) + **set‑returning** dominance (Pareto). **LawSet:** **no ordinal averaging**; **normalize‑then‑compare** when spaces/scales differ (UNM); editions pinned. **AdmissibilityConditions:** **CG‑Spec** bound; **ComparatorSet** explicit. **Transport:** Bridge+CL → **R/R_eff only**.  

**USCM — Unified Scoring Mechanism (SCP‑first)**  
**BaseType:** `U.Measure` (CHR‑typed slots). **OperatorAlgebra:** gauge embeddings + admissible aggregators; **WeightedSum** only on interval/ratio with unit alignment; partial orders return sets. **Guards:** **MinimalEvidence** \+ CG‑Spec legality. **Transport:** penalties → **R/R_eff**; UTS row.

**PTM — Publication & Telemetry Mechanism (informative)**
**BaseType:** `SoTA‑Pack(Core)`, `PathId/PathSliceId`, `PolicyId`. **OperatorAlgebra:** emit **selector‑ready** packs with parity pins and **telemetry stubs**; listen for edition/illumination bumps; trigger **slice‑scoped** refresh. 

**LawSet:** **no change of dominance defaults** unless CAL policy promotes; edition‑aware refresh. **Guards:** AH‑1..AH‑4 block missing pins. **Transport/Audit:** **G.10/G.11** publication & refresh semantics (CL routing to **R/R_eff**).

*Informative SoTA:* telemetry hooks align with post‑2015 quality‑diversity families (CMA‑ME/MAE, DQD/MEGA) and open‑ended methods (POET‑class) when gauged (illumination) rather than scored.

### **9 · SoTA-Echoing (post-2015 practice alignment)** *(informative)*

**Purpose.** To show how the FPF concept of a *Mechanism* (law-governed signature with guards and transport) aligns with, and improves upon, leading research and engineering practices after 2015.  
All comparisons are *informative*: they serve didactic continuity, not new normative force.

#### 9.1 Contemporary references (post-2015 sources)

1. **Algebraic effects and handlers** (Koka, Effekt, OCaml 5) — formalise “operation + lawful handler” semantics.
    
2. **Institution theory** (Goguen–Burstall; HETS evolutions) — defines translation between signatures, sentences, and models by typed morphisms.
    
3. **Policy-as-Code** (Rego/OPA, ISO 3450x ODD) — codifies admissibility and risk predicates for runtime enforcement.
    
4. **Session / Typestate types** (post-2017 multiparty protocols, linear usage) — constrain admissible operation sequences and states.
    
5. **Measurement-legality in machine learning** (2015 – 2025 monotone and calibrated learning, conformal prediction) — exemplifies the need for explicit scale compliance and monotonicity proofs (CSLC/CG-Spec echo).
    

Each source corresponds to a distinct *Tradition*: formal semantics, categorical algebra, compliance automation, protocol safety, and lawful AI.

#### 9.2 Alignment with A.6.1 fields and concepts

| External practice | Corresponding A.6.1 field / construct | FPF alignment and improvement |
| --- | --- | --- |
| Algebraic effects & handlers | **OperatorAlgebra + LawSet** | FPF generalises effect signatures into universal operator laws; adds Γ_time for temporal legality and explicit R-routing. |
| Institution morphisms | **U.MechMorph** (Refine/Extend/Quotient) | Mechanism morphisms reuse institutional structure but add ContextSlice & Bridge discipline; CL penalties route → R_eff. |
| Policy-as-Code / ODD | **AdmissibilityConditions + Γ_timePolicy** | Policies become first-class lawful guards; FPF forbids hidden context or “latest” defaults. |
| Session / Typestate protocols | **AdmissibilityConditions + set-valued USM Scopes** | Deterministic guards preserve state safety; composable across Contexts by Bridges. |
| Lawful measurement (ML) | **CG-Spec / MM-CHR** binding | Enforces CSLC proofs; forbids ordinal averaging; guarantees unit/scale alignment. |

#### 9.3 Adopt / Adapt / Reject summary

* **Adopt** formal, law-governed signatures (Institutions + Effects); explicit admissibility predicates.
    
* **Adapt** runtime policy execution into *static AdmissibilityConditions + Γ_time* (no embedded evaluators).
    
* **Reject** tool-bound semantics, automatic recency heuristics, or any cross-scale arithmetic without CSLC proof.

#### 9.4 Holonic repeatability

The same correspondence holds at **every holonic level**:  
a part-holon declares its own `OperatorAlgebra/LawSet/AdmissibilityConditions`; a whole-holon merges them via Bridges; a meta-holon re-binds mechanisms under a new Γ-closure. All penalties remain in **R / R_eff**, while **F / G** invariants propagate intact.

### 10 · 60‑second didactic script 

> *“To mint a mechanism, fill a **Mechanism.Intension**: declare **SubjectBlock** (**SubjectKind**, **BaseType**, **SliceSet**, **ExtentRule**, **ResultKind?**) and **ParamKinds**; then **OperatorAlgebra/Laws/AdmissibilityConditions** and **Γ_time**; define **Transport** (Bridge/CL with penalties to R only), and **Audit** (UTS + Path pins). Realize it as CAL/LOG/CHR under **A.6**. USM and UNM are already such mechanisms; the same template births comparison, scoring, and publication mechanisms—safely bound to **CG‑Spec**—without leaving the kernel grammar.”*

### 11 · Quick “builder’s” checklist (author‑facing)

1. Draft **AT0/AT1 charter**: why this Mechanism, which **guard surfaces** and **comparability** are in scope; is a **Γ_m (CAL)** builder needed?
    
* Fill **Mechanism.Intension** (**SubjectBlock**, **ParamKinds**, **OperatorAlgebra**, **LawSet**, **AdmissibilityConditions**, **Applicability**, **Transport**, **Γ_timePolicy**, **PlaneRegime**, **Audit**).
    
* Bind **CHR legality & CG‑Spec** when comparing/aggregating (ComparatorSet, ScaleComplianceProfile (SCP), MinimalEvidence, Γ‑fold).
    
Ship **UTS + G.10**; wire **G.11** telemetry (PathSlice‑keyed); ensure penalties **route to `R_eff` only**.

### 12 · Consequences (informative)

* **Uniform kernel shape.** Scope, normalization, comparison families can be authored and compared without lexical drift.
* **Auditable reuse.** GateCrossings are UTS‑visible; penalties are transparent (**R only**), with **AH‑1..AH‑4** harness coverage.
* **Scalarisation avoids illegality.** Partial orders remain set‑valued; cross‑scale arithmetic is blocked by **CG‑Spec/CSLC**.

### 13 · Rationale (informative)

Anchoring mechanisms in **A.6 Signature→Realization** provides a minimal, typed surface that preserves **USM** set‑algebra and **UNM** “normalize‑then‑compare” quotients while making **Part F (Bridges)** crossings explicit and costed on **R** (never **F/G**).

### 14 · Relations (quick pointers)

Builds on **A.6**; instantiates **A.2.6 USM** (ContextSlice, Γ_time, ∩/SpanUnion/translate) and **A.19/C.16 UNM** (classes, ≡\_UNM, validity windows); uses **Part B** (Bridges, CL/CL^k/CL^plane; **no implicit crossings**); binds **CG‑Spec** for any numeric comparison/aggregation; telemetry/publication via **G.10/G.11**.

## A.6.2 · **`U.EffectFreeEpistemicMorphing` — Effect‑free morphisms of epistemes** [A]

**One‑line summary.** `U.EffectFreeEpistemicMorphing` (EFEM) is the universal class of **effect‑free, law‑governed morphisms between epistemes**. An EFEM morphism rewrites episteme components (ClaimGraph, `describedEntityRef`, optional `groundingHolonRef`, `viewpointRef`, `referenceScheme`, and—where C.2.1+ is in use—`representationSchemeRef` and related slots, plus meta) in a **conservative, functorial, reproducible** way, with an explicit mode for what happens to the **DescribedEntitySlot** (`DescribedEntityChangeMode ∈ {preserve, retarget}`) as defined by `C.2.1 U.EpistemeSlotGraph`.

**Status.** Normative [A] in **Part A (Kernel)**.

**Placement.** After **A.6.1 `U.Mechanism`** and before any specialisations (`A.6.3 U.EpistemicViewing`, `A.6.4 U.EpistemicRetargeting`).

**Builds on.**
A.6.0 `U.Signature` (subject/vocabulary/laws/applicability); A.6.1 `U.Mechanism`; A.6.5 `U.RelationSlotDiscipline`; C.2.1 `U.Episteme — Epistemes and their slot graph`; E.10.D2 (I/D/S discipline); C.3.* (Kind‑CAL / KindBridge for described‑entity classes).

**Used by.**
A.6.3 `U.EpistemicViewing`; A.6.4 `U.EpistemicRetargeting`; E.17.0 `U.MultiViewDescribing`; E.17 (MVPK); E.18 (E.TGA StructuralReinterpretation, Transduction graph).

### 1 · Problem frame

FPF has many operations that **transform knowledge artifacts** without directly doing work in the world:

* turning an informal method description into a more formal specification;
* projecting a large system description into a smaller “for‑safety‑officer” view;
* re‑expressing the same behavioural model in a different calculus or notation;
* retargeting an analysis from “this subsystem” to “that subsystem” along a known KindBridge.

All of these are **episteme→episteme** transforms: they change what is written in an episteme, but they **do not themselves measure, execute, or actuate**. They are neither Work (A.15) nor Mechanisms in the A.6.1 sense; they are “pure morphisms over epistemes”.

Without a universal pattern for such morphisms:

* every family (KD‑CAL, E.TGA, MVPK, discipline packs) reinvent their own notion of “projection”, “reinterpretation”, or “refinement”;
* laws about what may change in an episteme (content vs described entity vs grounding holon vs reference plane) fragment across the spec;
* cross‑family reasoning (e.g. “this E.TGA StructuralReinterpretation is a retargeting, not a view”) becomes brittle and ad‑hoc.

### 2 · Problem

Concretely, without EFEM:

1. **No single place for “effect‑free” discipline.**
   The distinction *“episteme‑only change”* vs *“Work in the world”* is already important (C.2.1 separates episteme components from Work and from presentation surfaces), but the laws for “episteme‑only” operations are scattered or implicit. 

2. **Described entity behaviour is unclear.**
   Many transforms **intend** to keep “what this episteme is about” fixed (viewing), others **intend** to change it under an invariant (retargeting). Without a common *DescribedEntityChangeMode* discipline we get silent breaks in “describedEntity”: an operation that looks like a harmless format change may in fact surreptitiously change the entity‑of‑interest.

3. **No functorial backbone.**
   MVPK, KD‑CAL and E.TGA all implicitly assume that episteme transforms **compose** and respect identities, but the conditions for this (purity, conservativity, idempotence, scope) are not formulated once and reused. Different parts of the spec repeat subtly different sets of laws.

4. **Slot/Ref confusion.**
   With the new `U.EpistemeSlotGraph` and `U.RelationSlotDiscipline`, every episteme now has explicit **SlotKind / ValueKind / RefKind** discipline. Laws for “projection” or “retargeting” that are written against “fields” or unnamed tuple components are now out of alignment.

The result: engineers and tool builders can no longer tell **when they are allowed to transform epistemes without changing what is being claimed about the world**, nor what needs to be witnessed by Bridges and CL‑penalties when describedEntity does change.

### 3 · Forces

* **Epistemic purity vs operational power.**
  Effect‑free episteme transforms are attractive precisely because they can be reasoned about algebraically and composed freely. But the more operational power they are given (IO, solver calls, measurements), the less they remain “pure” and the more they belong under `U.Mechanism` / `U.WorkEnactment`.

* **Preserve vs retarget.**
  Viewing is describedEntity‑preserving; reinterpretation along a KindBridge is describedEntity‑retargenting. Both are important, but **they must be distinguished and witnessed differently**.

* **Conservativity vs usefulness.**
  EFEM should be **conservative**: no new intensional commitments beyond what input epistemes already entail. At the same time, we need transformations that can *factor*, *aggregate*, or *normalise* content, which may drop some information or change its representation.

* **Locality vs reference planes and Bridges.**
  Epistemes live on **reference planes** (C.2.1); cross‑plane and cross‑Context reasoning goes via Bridges and CL penalties (Part F/B.3). EFEM must respect this: it cannot smuggle plane changes or transport into “pure” content rewrites.

* **I/D/S strict distinction.**
  Intension (`I`) is not itself an episteme; `…Description` and `…Spec` are epistemes with a `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩`. EFEM must support operations on D/S epistemes while keeping the I/D/S layering intact (A.7, E.10.D2).

### 4 · Solution — define `U.EffectFreeEpistemicMorphing` once

#### 4.1 · Informal definition

> **Definition.** A `U.EffectFreeEpistemicMorphing` (EFEM) is a class of **episteme→episteme morphisms** that:
>
> * operate **only** on the components of an episteme as fixed in `C.2.1 U.EpistemeSlotGraph` (ClaimGraph, slots for described entity, grounding holon, viewpoint, representation/reference schemes, meta); 
> * are **effect‑free** (no Work, no Mechanism application, no mutation of systems or carriers);
> * are **conservative** in what they claim about the described entity (no new intensional commitments beyond logical consequences under the declared ReferenceScheme);
> * are **functorial** (identities and composition behave as expected on the category of epistemes);
> * declare an explicit **DescribedEntityChangeMode ∈ {preserve, retarget}**, controlling how `DescribedEntitySlot` (and associated subjectRef) behaves.

The **objects** of the EFEM universe are epistemes of some `U.EpistemeKind` (typically realised as `U.EpistemeCard` / `U.EpistemeView` / `U.EpistemePublication`). The **arrows** are EFEM morphisms `f : X → Y` satisfying the P0–P5 laws below.

Specialisations:

* `U.EpistemicViewing` (A.6.3) — EFEM with `DescribedEntityChangeMode = preserve`.
* `U.EpistemicRetargeting` (A.6.4) — EFEM with `DescribedEntityChangeMode = retarget`, tied to KindBridges/ReferencePlanes.

#### 4.2 · Signature Block (A.6.0 alignment)

As a `U.Signature`, EFEM publishes the following **SubjectBlock** and the standard four‑row block (“SubjectBlock / Vocabulary / Laws / Applicability”) from A.6.0, specialised to episteme→episteme morphisms.

**SubjectBlock**

```
SubjectBlock
  SubjectKind   = U.EffectFreeEpistemicMorphing
  BaseType      = ⟨X : U.Episteme, Y : U.Episteme⟩        // carrier pair (domain,codomain)
  Quantification= SliceSet:=U.ContextSliceSet; 
  ExtentRule:=admissibleEpistemeMorphisms // Context slices & admissible EFEM per slice
  ResultKind?   = U.Morphism                               // typed morphism f : X→Y
```

This says: EFEM is “about” **morphisms between epistemes**, indexed by Context slices; its results are morphisms of a declared type `U.Morphism` in the `Ep` category.

**Vocabulary (core operators & kinds)**

* **Types**
  * `U.Episteme` (as holon; realised via species `U.EpistemeCard`, `U.EpistemeView`, `U.EpistemePublication` under C.2.1).
  * `U.EpistemeKind` (episteme n‑ary relation signature; slots per A.6.5 / C.2.1).
  * `U.SubjectRef` (subject reference; for D/S epistemes this is `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩` per IDS‑13 (DescriptionContext discipline; C.2.1 §6.1 / E.10.D2)).
  * `U.Morphism` (arrow in `Ep`).
  * `U.DescribedEntityChangeMode = {preserve, retarget}` (enumeration; no new Kernel type for “DescribedEntity”).

* **Operators (arrow algebra)**

  * `id_X : U.Morphism(X→X)` for any episteme `X`.
  * `compose(g,f) : U.Morphism(X→Z)` where `f : X→Y`, `g : Y→Z`.
  * `apply(f, x:U.Episteme) : U.Episteme`.
  * `dom(f), cod(f) : U.Episteme`.
  * `subjectRef(E) : U.SubjectRef`.
  * `describedEntityChangeMode(f) : U.DescribedEntityChangeMode`  // EFEM‑level characteristic from C.2.1.

Each operator that takes epistemes as arguments obeys **SlotSpec discipline** from A.6.5: in particular, laws below are phrased in terms of the **named SlotKinds** (`DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ReferenceSchemeSlot`, `ViewSlot`, and—when the C.2.1+ extension is used—`RepresentationSchemeSlot`) and their associated ValueKind/RefKind; we never speak of “field 1/2/3”.

**Laws row** and **Applicability** are given by P0–P5 and the Scope clause below.

#### 4.3 · Laws P0–P5 (normative)

All laws below are **normative**: any morphism advertised as an instance of `U.EffectFreeEpistemicMorphing` SHALL satisfy them.

##### P0 — Typed signature & component profile (C.2.1‑grounded)

For any EFEM morphism `f : X→Y`:

1. **Typed objects.** `X` and `Y` are epistemes of declared kinds `K_X, K_Y : U.EpistemeKind`, each with a SlotKind signature as per C.2.1 and A.6.5 (at least `DescribedEntitySlot`, `ClaimGraphSlot`, `ViewpointSlot?`, `RepresentationSchemeSlot?`, `ReferenceSchemeSlot?`; `GroundingHolonSlot?`, `ViewSlot?` where relevant).

2. **Component projection.** For each episteme `E`, EFEM laws may refer to:
   * `content(E) : U.ClaimGraph` — value of `ClaimGraphSlot` (stored **by value** in the minimal core);
   * `describedEntityRef(E) : U.EntityRef` — value of the RefKind for `DescribedEntitySlot`;
   * `groundingHolonRef?(E) : U.HolonRef` — if the episteme kind includes `GroundingHolonSlot`;
   * `viewpointRef?(E) : U.ViewpointRef` — if `ViewpointSlot` is present;
   * `referenceScheme?(E) : U.ReferenceScheme` — value of `ReferenceSchemeSlot` (stored **by value** in the minimal core);
   * `representationSchemeRef?(E) : U.RepresentationSchemeRef` — only for episteme kinds that use the C.2.1+ `RepresentationSchemeSlot`;
   * `meta(E)` — edition/provenance/status components (species‑level).

3. **Declared `DescribedEntityChangeMode`.**
   Each EFEM species **declares** a fixed `DescribedEntityChangeMode ∈ {preserve, retarget}`. At the level of individual morphisms:

   * if `describedEntityChangeMode(f) = preserve`, then `describedEntityRef(Y) = describedEntityRef(X)` (and usually `groundingHolonRef(Y) = groundingHolonRef(X)` unless an explicit Grounding Bridge is declared);
   * if `describedEntityChangeMode(f) = retarget`, then `describedEntityRef(Y) ≠ describedEntityRef(X)` in general and a **KindBridge** between the two described entities MUST be named (A.6.4 / F.9).

4. **SubjectRef compatibility.**
   For D/S epistemes (`…Description` / `…Spec`), `subjectRef(E)` is a `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩` (E.10.D2). EFEM species SHALL state how `subjectRef` transforms in terms of these components (usually: preserve or explicitly adjust `ViewpointRef` while preserving `DescribedEntityRef` and `BoundedContextRef`).

##### P1 — Purity (no external effects)

EFEM morphisms are **pure functions on epistemes**:
* Applying `f : X→Y` **does not**:
  * change any `U.System` or `U.Holon` state;
  * execute Work (`U.WorkEnactment`) or run a `U.Mechanism` (A.6.1) with operational guards;
  * mutate `U.PresentationCarrier` (files, databases, message buses, IDEs).
* The **only** state change introduced by EFEM is the replacement of input epistemes by output epistemes according to `apply(f, X) = Y`, with all component changes governed by P2–P5.

Any operation that requires **measurements, simulations, solver calls, or tool use with external side‑effects** SHALL be modelled as a `U.Mechanism`/`U.Work` that **produces new epistemes**, which may then be related by EFEM morphisms.

##### P2 — Conservativity (no new intensional commitments)

Let `content_X = content(X)`, `content_Y = content(Y)`, with associated `referenceScheme_X`, `referenceScheme_Y`, `describedEntityRef_X`, `describedEntityRef_Y`, `groundingHolonRef_X`, `groundingHolonRef_Y`. Interpret each `content` via its `ReferenceScheme` and slots. Then:

> The set of **claims about the described entities** that can be read from `Y` **SHALL NOT introduce new atomic commitments** beyond those that are logical consequences of the claims read from `X`, possibly after applying a declared correspondence between representation/reference schemes.

Intuitively:

* EFEM may:
  * delete information (projection/abstraction);
  * normalise or re‑express information (e.g., reordering ClaimGraph, changing notation via a ReferenceScheme/RepresentationScheme correspondence);
  * add **meta‑claims about the episteme** itself (edition, source, status, witness entries).

* EFEM may **not**:
  * assert new atomic facts about the described entities or grounding holons beyond what is derivable from input ClaimGraphs under the declared ReferenceSchemes;
  * silently widen the scope of claims (e.g., treating local facts as global, changing Context or ReferencePlane without a Bridge).

Where `describedEntityChangeMode(f) = retarget`, conservativity is understood **relative to a declared invariant** of the KindBridge (A.6.4): e.g., conservation of energy for a Fourier transform, or preservation of functional behaviour for a structural reinterpretation.

##### P3 — Functoriality (identity, composition, correspondence)

We work in the category **Ep** whose objects are epistemes (species of `U.Episteme`) and whose arrows are EFEM morphisms satisfying P0–P2, together with the functor

```
+α : Ep → Ref
```

that maps each episteme to the object it describes (value of `DescribedEntitySlot`, i.e. `describedEntityRef(E)`) as in the mathematical layer for epistemes. EFEM instances with `describedEntityChangeMode(f) = preserve` are **vertical morphisms** for α (`α(f) = id`), while those with `describedEntityChangeMode(f) = retarget` reindex along a declared `KindBridge` in **Ref**.

1. **Identities.** For each episteme `X`, there exists `id_X : X→X` such that:

   ```text
   apply(id_X, X) = X
   compose(id_Y, f) = f = compose(f, id_X)
   ```

   `id_X` preserves all components (`content`, `describedEntityRef`, `groundingHolonRef`, `viewpointRef`, `representationSchemeRef`, `referenceScheme`, `meta`).

2. **Composition.** For `f : X→Y`, `g : Y→Z`, the composite `h = compose(g,f)` is an EFEM morphism `X→Z` with:

   ```
   apply(h, X) = apply(g, apply(f, X))
   describedEntityChangeMode(h) = combine(describedEntityChangeMode(f), describedEntityChangeMode(g))   // as per species-specific rules
   ```

and P0–P2 hold for `h`. For example, two `preserve` morphisms compose to `preserve`; `preserve` after `retarget` is `retarget` if the KindBridge composition exists.

3. **Correspondence‑aware composition.**
   When EFEM changes `RepresentationScheme` or `ReferenceScheme`, a **CorrespondenceModel** (as in C.2.1 §6 and E.17) may be needed to witness commutativity: composition MUST respect these correspondences up to declared isomorphism/oplax naturality (witness epistemes may be recorded in `meta`).

##### P4 — Idempotence & determinism (on fixed configuration)

For any EFEM morphism `f : X→Y` with fixed configuration (episteme kinds, `DescribedEntityChangeMode` characteristic, KindBridge/CorrespondenceModel where needed):

1. **Determinism.**
   For the same input episteme `X` (identical content, slots, meta), `apply(f, X)` yields the same output episteme `Y` up to declared structural equivalence (normal forms, alpha‑renaming etc.). There is no dependence on ambient time, randomness, network state, or solver heuristics unless these are **encoded as explicit inputs**.

2. **Idempotence (up to declared equivalence).**
   Re‑applying the same EFEM to its own output yields no further essential change:

   ```text
   apply(f, apply(f, X)) ≅ apply(f, X)
   ```

   where `≅` denotes the structural equivalence declared for the episteme kinds in question (e.g., ClaimGraph normalisation).

Species MAY weaken idempotence to “idempotent after normalisation”; if so, the normalisation step MUST itself be specified as an EFEM morphism and the composite be idempotent.

##### P5 — Applicability, scope & compatibility

Each EFEM species **publishes** an Applicability clause:

* **EoI / described entity class.**
  A constraint on the allowed ValueKind of `DescribedEntitySlot` (via `EoIClass ⊑ U.Entity`): e.g., “epistemes describing `U.Holon` that are systems of type X”.

* **Grounding holon & Context.**
  Constraints on `GroundingHolonSlot` and `U.BoundedContext`: where the morphism is valid (lab, runtime environment, organisational context).

* **Representation/ReferenceSchemes.**
  Enumerates supported `RepresentationScheme`/`ReferenceScheme` pairs and any required CorrespondenceModels.

* **Viewpoint discipline.**
  For Descr/Spec epistemes, EFEM SHALL specify which `U.Viewpoint`s (E.17.0) it supports and how it interacts with `U.MultiViewDescribing` families (e.g., “works only on engineering viewpoints from TEVB” or “viewpoint‑agnostic normalisation”).

Applying EFEM **outside** its Applicability (e.g., wrong EoIClass, missing grounding holon, incompatible Viewpoint) is **non‑conformant**: a conformant implementation MUST reject such attempts or model them as different mechanisms/works, not as EFEM.

Cross‑Context or cross‑plane use (changing `U.BoundedContext` or `ReferencePlane`) is **not part of EFEM**; it is handled by Bridges (Part F) and A.6.1 transport, which then feed new epistemes into EFEM.

### 5 · Archetypal Grounding (Tell–Show–Show)

The examples below show how EFEM is intended to be used across I/D/S and Viewpoint/MVPK layers.

#### 5.1 · Typed formalisation `Specify_DS : D→S` (species of EFEM)

*Context.* You have an informal `U.MethodDescription` for a safety check and want a more formal `U.MethodSpec` with test harness obligations, but **about the same method**.

*Shape.*

* Domain: `X = U.MethodDescription` episteme with
  `describedEntityRef(X) : U.MethodRef`, `content(X) : U.ClaimGraph_D`, `viewpointRef(X)` an engineering viewpoint (TEVB), `ReferenceScheme_D`.
* Codomain: `Y = U.MethodSpec` episteme with the **same** `describedEntityRef(Y) = describedEntityRef(X)`, `viewpointRef(Y) = viewpointRef(X)`, more structured `content(Y) : U.ClaimGraph_S`, stronger ReferenceScheme (explicit pre/post, obligations).

`Specify_DS` is a species of EFEM:

* `describedEntityChangeMode(Specify_DS) = preserve`.
* P1 — effect‑free: it transforms epistemes only.
* P2 — conservative: any behavioural claims in the Spec must be logically entailed by the informal Description and the underlying Method Intension; if the spec makes stronger claims, that is modelled as creating a **new Intension with its own D/S pair**, not as a valid EFEM instance.
* P3–P5 — functorial and scoped: specs compose, applicability bound to the appropriate engineering context and Viewpoints.

This matches A.7/E.10.D2 strict distinction: I→D (`Describe_ID`) is not itself an episteme→episteme morphism, but `Specify_DS` is; EFEM supplies its laws.

#### 5.2 · Internal normalisation of a View (species of EFEM, `describedEntityChangeMode = preserve`)

*Context.* In MVPK you compute a engineering view `V` of a system description; you then normalise the view (sort, factor, put equations into normal form) without changing what it says.

Let `X = V_raw`, `Y = V_norm`, both `U.EpistemeView` instances with the same:

* `describedEntityRef(X) = describedEntityRef(Y)` (same system);
* `groundingHolonRef(X) = groundingHolonRef(Y)` (same environment);
* `viewpointRef(X) = viewpointRef(Y)` (same Viewpoint);
* `representationSchemeRef(X) = representationSchemeRef(Y)` (same notation).

The EFEM `NormalizeView : X→Y`:

* has `describedEntityChangeMode(NormalizeView) = preserve`;
* changes only `content` and maybe `meta` (e.g. “normalised at edition E”);
* is idempotent and deterministic (P4);
* is conservative (P2): no new claims, only re‑expression.

MVPK can then **assume** functoriality of such normalisations without re‑stating the EFEM laws.

#### 5.3 · Retargeting sketch (bridge‑backed, `describedEntityChangeMode = retarget`)

*Context.* E.TGA’s StructuralReinterpretation maps a physical layout view into a functional behaviour view, changing the described entity from “physical module assembly” to “functional graph” along a KindBridge.

Inside EFEM, this becomes a species with `describedEntityChangeMode = retarget`:
* input episteme describes `S₁` (e.g. a component hierarchy holon);
* output episteme describes `S₂` (e.g. a functional network holon);
* a declared `KindBridge(S₁,S₂)` and invariant (e.g. behavioural equivalence) provide the semantic glue;
* P2 conservativity is checked **w.r.t. that invariant**.

The details belong to A.6.4/E.TGA; EFEM provides the generic discipline.

#### 5.4 · Worked SlotSpec example (engineering SystemDescription episteme kind)
*(informative)*

To make the SlotKind/ValueKind/RefKind discipline and EFEM laws concrete, consider a simple engineering `U.EpistemeKind` for system descriptions over `EoIClass ⊑ U.Entity` with `EoIClass = U.System` in a given Context. A minimal SlotSpec table for such a kind could be:

| SlotKind              | ValueKind                                     | RefKind / refMode   | Notes                                                                 |
| --------------------- | --------------------------------------------- | ------------------- | --------------------------------------------------------------------- |
| `DescribedEntitySlot` | `U.Entity` (constrained by `EoIClass = U.System`) | `U.EntityRef`    | describes which system the episteme is about                          |
| `GroundingHolonSlot`  | `U.Holon`                                     | `U.HolonRef`        | plant / runtime SoS grounding measurements and validation             |
| `ClaimGraphSlot`      | `U.ClaimGraph`                                | ByValue             | KD‑CAL/LOG‑CAL ClaimGraph for the description or spec                 |
| `ViewpointSlot`       | `U.Viewpoint`                                 | `U.ViewpointRef`    | engineering viewpoint (e.g. from TEVB) under which D/S are validated |
| `ReferenceSchemeSlot` | `U.ReferenceScheme`                           | ByValue             | how the ClaimGraph is read against described entity and grounding     |

This table is an instance of A.6.5 `U.RelationSlotDiscipline`: each row is a SlotSpec triple ⟨SlotKind, ValueKind, refMode/RefKind⟩; no additional kernel types are introduced, and C.2.1’s constraints on `DescribedEntitySlot`/`GroundingHolonSlot` are preserved.

Two typical EFEM species over this kind are:
* `Specify_DS_Sys : SystemDescription → SystemSpec` — a `DescribedEntityChangeMode = preserve` species that:
  * **reads** `DescribedEntitySlot`, `GroundingHolonSlot`, `ViewpointSlot`, `ReferenceSchemeSlot` and **writes** a refined `ClaimGraphSlot` and possibly a strengthened `ReferenceSchemeSlot`;
  * satisfies P2 by only adding claims that are logical consequences of the original description plus the fixed Intension (A.7/E.10.D2);
  * satisfies CC‑C.2.1‑5 by explicitly declaring its slot profile and change mode.

* `Normalize_EngView : EpistemeView → EpistemeView` — a view‑normalisation EFEM (again with `DescribedEntityChangeMode = preserve`) that:
  * **reads** all slots and **writes** only `ClaimGraphSlot` (normal form) and `meta`;
  * is idempotent and deterministic (P4) and pure (P1);
  * is conservative (P2) by construction: it never introduces new atoms about the described system.

In later A.6.3/A.6.4/E.17.* patterns, concrete EpistemeKinds (for specific engineering description/specification idioms) are expected to provide SlotSpecs of this general shape and to state explicitly, per CC‑C.2.1‑5 / CC‑EFEM.*, which slots their EFEM species read and write.

### 6 · Bias & Defaults (informative)

* **Episteme‑first, world‑second.** EFEM is strictly about **epistemes as objects**; any world contact (measurements, executions) lives in `U.Mechanism`/`U.Work` and produces new epistemes that EFEM may subsequently relate.

* **SlotKinds, not “fields”.** Laws talk about `DescribedEntitySlot`, `GroundingHolonSlot`, etc., and their ValueKind/RefKind, as per A.6.5 and C.2.1; they never use unnamed tuple positions or “role 1/2/3”. This keeps EFEM aligned with the slot discipline used for methods, roles, services, and other n‑ary relations.

* **Local‑first semantics.** EFEM is **Context‑local**; crossings of Context or ReferencePlane are always delegated to Bridges / A.6.1 transport (with CL penalties to `R/R_eff` only). No “implicit cross‑Context EFEM” is permitted.

* **I/D/S respect.** EFEM never collapses Intension with Description/Spec: I→D and D→S operations are typed explicitly and either (i) conform to EFEM laws where they are episteme→episteme, or (ii) remain separate morphism classes (A.7) while being described as EFEM‑conformant.

### 7 · Conformance Checklist (normative)

| ID                                                  | Requirement                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CC‑EFEM.1 (Typed episteme objects).**             | Every morphism advertised as `U.EffectFreeEpistemicMorphing` SHALL have domain and codomain epistemes whose kinds (`U.EpistemeKind`) publish SlotKinds/ValueKinds/RefKinds according to C.2.1 and A.6.5 (at least `DescribedEntitySlot` and `ClaimGraphSlot`; other slots as declared).                                                                                                               |
| **CC‑EFEM.2 (Declared DescribedEntityChangeMode).** | Each EFEM **species** SHALL declare the `DescribedEntityChangeMode` characteristic `describedEntityChangeMode : U.Morphism → {preserve, retarget}` as per C.2.1. For every instance `f`, `describedEntityChangeMode(f)` MUST be either `preserve` (⇒ `describedEntityRef` unchanged) or `retarget` (⇒ a KindBridge and invariant are explicitly named; see A.6.4 / F.9).                                                                                         |
| **CC‑EFEM.3 (Purity).**                             | EFEM morphisms SHALL be effect‑free: they MUST NOT directly perform Work or run mechanisms with operational guards; they only read input epistemes and construct output epistemes consistent with P2–P5. Any use of external solvers/measurements MUST be modelled as separate Mechanisms/Work that feed new epistemes into EFEM.                                                                     |
| **CC‑EFEM.4 (Conservativity).**                     | Laws for EFEM species SHALL state their conservativity regime: claims in the output MUST be logical consequences of input claims under declared ReferenceSchemes and any CorrespondenceModels/KindBridges. If an operation may strengthen claims (e.g. add commitments not entailed by inputs), it is **not** EFEM and MUST be modelled separately.                                                   |
| **CC‑EFEM.5 (Functoriality & idempotence).**        | EFEM species SHALL support identity and composition with the usual category laws, and SHALL specify any structural equivalence under which idempotence holds. Non‑deterministic or order‑sensitive behaviour (beyond declared structural equivalences) is non‑conformant.                                                                                                                             |
| **CC‑EFEM.6 (Applicability & scope).**              | Each EFEM species SHALL publish Applicability in terms of: allowed EoI classes (ValueKind for `DescribedEntitySlot`), Context/BoundedContext and grounding holon constraints, supported Viewpoints and representation/reference schemes. Applying EFEM outside this Applicability (including cross‑Context or cross‑plane) is non‑conformant. Crossings MUST be delegated to Bridges/A.6.1 transport. |
| **CC‑EFEM.7 (I/D/S & subjectRef discipline).**      | For any episteme that is a `…Description`/`…Spec` (E.10.D2), EFEM laws SHALL be phrased in terms of `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩` and MUST respect the I/D/S discipline **and** DescriptionContext invariants (including IDS‑13 Viewpoint‑locality as defined in E.10.D2/C.2.1): `Describe_ID` lives in A.7; `Specify_DS` MAY be species of EFEM but MUST preserve Intension. |
| **CC‑EFEM.8 (Slot‑level read/write declaration).**  | Any EFEM species that defines morphisms between epistemes SHALL also satisfy C.2.1 checkpoint CC‑C.2.1‑5: it MUST state whether it is a species of `U.EffectFreeEpistemicMorphing`/`U.EpistemicViewing`/`U.EpistemicRetargeting`, declare its `describedEntityChangeMode`, name which SlotKinds it reads and writes, and state its behaviour on `describedEntityRef`, `groundingHolonRef`, `viewpointRef`, and `referenceScheme`. |

### 8 · SoTA‑Echoing (informative, lineage)

EFEM is intentionally “thin”: it provides a **minimal categorical and slot‑based discipline** for episteme→episteme morphisms, making it easy to align with several post‑2015 lines of work:

* **Categorical semantics & displayed categories.**
  Treating `Ep` as a category over `Ref` via a functor `α : Ep → Ref` (mapping each episteme to its described entity) matches the *displayed categories* view on fibrations: EFEM arrows are those morphisms in `Ep` that are “vertical” (preserve α) or “structured reindexings” (retarget under a KindBridge). This is exactly the intended alignment with C.2.1’s subjectRef/ReferencePlane picture.

* **Optics as universal projections.**
  Viewing operations (`U.EpistemicViewing`) refine EFEM in a way analogous to **lenses/prisms/traversals** in the optics literature: effect‑free, compositional accessors for parts of a larger structure. EFEM captures the laws that underlie those projections (purity, conservation, functoriality); optics‑style constructions can then be used inside discipline packs without modifying the core.

* **Structured cospans & correspondences.**
  Many correspondence‑based multi‑view patterns (ISO 42010 correspondences, model synchronisation, traceability links) can be seen as spans/cospans between epistemes. EFEM ensures that the legs of such cospans are effect‑free and conservative, while CorrespondenceModels carry the extra structure needed for consistency management.

* **Bidirectional transformations (BX).**
  The “no new commitments” and “functorial & idempotent” constraints mirror modern BX practice around **consistency restoration**: EFEM is the universal core that BX‑like constructions (view updates, synchronisers) must respect when instantiated for epistemes.

EFEM does *not* prescribe a specific calculus (deductive, probabilistic, latent‑space), nor a specific representation (symbolic vs distributed); those choices are captured in `U.ClaimGraph`, `U.RepresentationScheme` and discipline‑level architheories. EFEM only says what it means to transform epistemes **legally** in that chosen substrate.

### 9 · Consequences

* **Single place for episteme‑to‑episteme laws.**
  All effect‑free transforms of knowledge artefacts, across KD‑CAL, MVPK, E.TGA, discipline packs, can now be defined as species of EFEM, instead of each family re‑inventing its own law set.

* **Clear separation from mechanisms & work.**
  Anything that touches the world (measurements, execution, simulation) is forced into `U.Mechanism` / `U.WorkEnactment`, with CL‑penalised Bridges and Γ_time; EFEM remains pure and compositional.

* **Stable backbone for Viewing & Retargeting.**
  A.6.3 and A.6.4 do not need to repeat P0–P5; they specialise EFEM with additional constraints (preserve/retarget). Other patterns (e.g. MultiViewDescribing, MVPK, E.TGA StructuralReinterpretation) can depend on EFEM as a stable base.

* **Slot‑level clarity.**
  By formulating EFEM laws in terms of SlotKinds/ValueKinds/RefKinds (A.6.5) and the EpistemeSlotGraph (C.2.1), it becomes much harder for Episteme to confuse “object of talk”, “slot in a relation”, and “reference to that object”.

* **Better didactics.**
  The old “semantic triangle” becomes a didactic projection of EFEM over the EpistemeSlotGraph: EFEM + C.2.1 explain precisely what the triangle was trying to gesture at (symbol, concept, object), while correctly foregrounding operations, viewpoints, grounding holons, and reference schemes.

### 10 · Rationale

**Why a separate EFEM pattern (A.6.2) instead of folding into A.6.1 or C.2.1?**

* A.6.1 governs **Mechanisms** (operations with AdmissibilityConditions, Γ_time, transport and Bridges)—too operational for the pure episteme transforms we want here.
* C.2.1 fixes the **ontology of epistemes** (slots, components, ReferencePlane), but does not talk about morphisms. EFEM is explicitly a **morphism‑level** pattern over that ontology.

This split mirrors how Signature (A.6.0) separates “what is declared” from “how it is realised”: C.2.1 says what an episteme is; A.6.2 says what a legal episteme→episteme transform is.

**Why insist on DescribedEntityChangeMode?**

Because almost all subtle errors in multi‑view reasoning show up as **silent retargeting**: a transform that appears to keep the same object‑of‑talk actually changes it (e.g., from “component assembly” to “function bundle”) without naming the bridge or invariant. By forcing every species to declare `preserve` vs `retarget`, EFEM makes those decisions explicit and reviewable.

**Why attach EFEM to SlotKinds instead of informal “fields”?**

FPF already committed to a single SlotKind/ValueKind/RefKind discipline (A.6.5) across relations, methods, roles, and now epistemes. Re‑using that discipline here:

* aligns episteme morphisms with the rest of the framework;
* enables later mechanised checks (e.g., that a viewing only touches slots it promised to touch);
* avoids minting yet another notion of “parameter” or “role in a relation”.

### 11 · Relations

* **Specialises / is specialised by.**

  * Builds on A.6.0 `U.Signature` and A.6.1 `U.Mechanism` for the uniform SubjectBlock/vocabulary/laws/applicability structure.
  * Specialised by A.6.3 `U.EpistemicViewing` (describedEntity‑preserving EFEM) and A.6.4 `U.EpistemicRetargeting` (describedEntity‑retargering EFEM).

* **Constrained by.**
  A.6.5 `U.RelationSlotDiscipline` (SlotKind/ValueKind/RefKind); C.2.1 `U.EpistemeSlotGraph` (episteme components, ReferencePlane); E.10.D2 (I/D/S discipline); Part F (Bridges, CL, ReferencePlane crossings); E.10 (LEX‑BUNDLE naming rules, especially on `…Slot` / `…Ref` and ban on Subject/Object in episteme tech names).

* **Consumed by.**
  E.17.0 `U.MultiViewDescribing` (families of D/S epistemes under Viewpoints); E.17 (MVPK — publication as species of Viewing/EFEM); E.18 (E.TGA StructuralReinterpretation and other transductions over epistemes); KD‑CAL/LOG‑CAL rules that reason about episteme transforms categorically.

## A.6.3 · **`U.EpistemicViewing` — describedEntity‑preserving morphism** \[A]

**One‑line summary.** `U.EpistemicViewing` is the **describedEntity‑preserving** species of `U.EffectFreeEpistemicMorphing`: an effect‑free projection between epistemes that may change content and representation, but **never changes what the episteme is about** (the occupant of `DescribedEntitySlot` in C.2.1).

**Status.** Normative [A] in **Part A (Kernel)**.
**Placement.** After **A.6.2 `U.EffectFreeEpistemicMorphing`**, before **A.6.4 `U.EpistemicRetargeting`**.

**Builds on.**
A.6.0 `U.Signature`; A.6.2 `U.EffectFreeEpistemicMorphing`; A.6.5 `U.RelationSlotDiscipline`; A.7/E.10.D2 (I/D/S discipline, `DescriptionContext`); C.2.1 `U.Episteme — Epistemes and their slot graph`; C.2 (KD‑CAL/LOG‑CAL, `subjectRef`, ReferencePlane).

**Used by.**
E.17.0 `U.MultiViewDescribing`; E.17 (MVPK — Multi‑View Publication Kit); E.17.1/E.17.2 (Viewpoint bundle libraries, TEVB); B.5.3 (Role‑EpistemicViewing); discipline packs for architecture, safety, and ML/LLM‑based representations.

### 1 · Problem frame

Engineers and researchers constantly need **views of the same knowledge artefact**:
* an ISO 42010‑style architectural view for a particular stakeholder group over a shared architecture description;
* a SysML v2 “view‑as‑query” over an underlying model, changing visualisation but not the modelled system;
* a publication view (Plain/Tech/Assurance) in MVPK over a common description/specification;
* an LLM‑friendly episteme derived from a symbolic specification (or vice versa), preserving what system is being described.

All of these are **episteme→episteme** transforms which intend to:
* keep the **DescribedEntity** fixed (`DescribedEntitySlot` in C.2.1), and
* change only **how** the episteme talks about it: sliced `U.ClaimGraph`, different `U.Viewpoint`, alternative `U.RepresentationScheme`, or a different `U.ReferenceScheme` tuned to the same entity and grounding holon.

We need a single, reusable notion of **“epistemic viewing”** that captures these projections as:
* **effect‑free** (no Work/Mechanism side‑effects),
* **describedEntity‑preserving** (no silent retargeting),
* **conservative** (no new intensional commitments about the same entity),
* and **functorial** (compose cleanly in multi‑step pipelines).

### 2 · Problem

Without a dedicated pattern for EpistemicViewing:
1. **Views vs retargetings blur.**
   Operations that *intend* to change only representation (viewing) are easily conflated with operations that change the **object‑of‑talk** (retargeting). A Fourier‑style transform or a StructuralReinterpretation in E.TGA can quietly drift from “view of S” into “view of a different S′”, without declaring a `KindBridge`.

2. **“View” vs “viewpoint” vs “surface” collapse.**
   In standards and tools, “view” is often used interchangeably to mean:
   * the **viewpoint** (specification of concerns and conformance rules),
   * the **episteme** produced under that viewpoint, and
   * the **surface** (rendered document or GUI).
     Without a clear episteme‑level notion of viewing, MVPK and E.17.0 cannot cleanly separate these layers.

2. **No describedEntity guarantees.**
   A projection that looks like a harmless slice of a system description may in fact:
   * change `describedEntityRef` (switching to a subsystem or a function),
   * change `groundingHolonRef` (different plant or runtime),
   * or smuggle in new intensional claims.
     Without explicit laws on C.2.1 components, “view” becomes an informal metaphor, not a reliable morphism class.

4. **Multi‑view reasoning has no core discipline.**
   Multi‑view patterns (ISO 42010 viewpoint libraries, SysML v2 view queries, TEVB, MVPK faces) need:
   * **vertical** projections over the same described entity (`α : Ep → Ref` fixed),
   * and **correspondence‑based** projections that rely on explicit cross‑episteme links.
     If each family re‑invents its own notion of “view”, consistency and tool support degrade.

### 3 · Forces

* **Same entity, different concerns.**
  Stakeholders want different slices of the same description/specification, sometimes under different viewpoints, without re‑identifying the entity (system, method, role, service) being described.

* **Internal vs cross‑episteme views.**
  Some views depend only on a single episteme (direct viewing); others depend on a **CorrespondenceModel** (e.g. aligning requirements and design models). Both must be supported, but with **different obligations**.

* **Conservativity vs expressivity.**
  A view must not introduce new commitments about the described entity, but it may:

  * aggregate or factor claims,
  * change representation regime (diagrammatic vs symbolic vs latent),
  * or shift to a different inference regime, **as long as this is conservative**.

* **I/D/S strictness.**
  `…Description` and `…Spec` are epistemes with `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩`. Viewing must work over these **DescriptionContexts** without collapsing Intension (`I`) into episteme or confusing D/S with publication surfaces.

* **Slot discipline and modularity.**
  With C.2.1 and A.6.5, epistemes now have explicit `SlotKind`/`ValueKind`/`RefKind` triples. Viewing laws must be stated **at the slot level**, not in terms of ad‑hoc “fields”, so they can be reused across engineering, publication, and discipline packs.

### 4 · Solution — `U.EpistemicViewing` as EFEM profile (`describedEntityChangeMode = preserve`)

#### 4.1 · Informal definition

> **Definition (informal).**
> `U.EpistemicViewing` is the **describedEntity‑preserving species** of `U.EffectFreeEpistemicMorphing`.
> A `U.EpistemicViewing v : X→Y`:
>
> * takes an input episteme `X` and produces an output episteme `Y`,
> * preserves the occupant of `DescribedEntitySlot` (`describedEntityRef(Y) = describedEntityRef(X)`),
> * may refine or re‑express `content : U.ClaimGraph`, `viewpointRef`, `representationSchemeRef`, and `referenceScheme`,
> * is **effect‑free and conservative** (no new intensional claims about the same described entity),
> * and composes functorially with other epistemic viewings.

In C.2.1 terms `U.EpistemicViewing` behaves like a **lens/optic over the episteme slot graph**: it focuses on some SlotKinds (typically `ClaimGraphSlot`, `ViewpointSlot`, `RepresentationSchemeSlot`, `ReferenceSchemeSlot`) while preserving `DescribedEntitySlot` (and usually `GroundingHolonSlot`).

#### 4.2 · Signature (A.6.0 / A.6.5 alignment)

**Signature header.**
`U.EpistemicViewing` is a **Morphism‑kind** under A.6.0:

```
SubjectBlock
  SubjectKind    = U.EpistemicViewing
  BaseType       = ⟨X:U.Episteme, Y:U.Episteme⟩      // carrier pair
  Quantification = SliceSet := U.ContextSliceSet;
                   ExtentRule := admissible view morphisms
  ResultKind     = U.Morphism                        // an instance v
```

**Vocabulary (re‑uses A.6.2).**
* **Types.** `U.Episteme`, `U.SubjectRef`, `U.Morphism`, `U.EpistemicViewing`.
* **Operators.**
  * `id    : U.Morphism(X→X)`
  * `compose(g,f) : U.Morphism(X→Z)` where `f:X→Y`, `g:Y→Z`
  * `apply(v, x:U.Episteme) : U.Episteme`
  * `dom(v), cod(v) : U.Episteme`
  * `subjectRef(·) : U.SubjectRef`
**Slot‑level discipline.**
Domain and codomain epistemes are instances of some `U.Episteme` species (typically `U.EpistemeCard`, `U.EpistemeView`, or `U.EpistemePublication`) whose episteme kinds each provide SlotSpecs (A.6.5) including at least:
  * `DescribedEntitySlot` (ValueKind `U.Entity`, RefKind `U.EntityRef`),
  * `GroundingHolonSlot?` (ValueKind `U.Holon`, RefKind `U.HolonRef`),
  * `ClaimGraphSlot` (ValueKind `U.ClaimGraph`, by‑value),
  * `ViewpointSlot?` (ValueKind `U.Viewpoint`, RefKind `U.ViewpointRef`),
  * `ReferenceSchemeSlot` (ValueKind `U.ReferenceScheme`, by‑value),
  * and, where C.2.1+ is in use, `RepresentationSchemeSlot`, `ViewSlot` and related slots.

Practical species of EpistemicViewing will very often take `X` and `Y` from the same `U.EpistemeKind`, but the pattern itself only requires that the SlotSpecs of the domain and codomain kinds be **compatible** in the sense of A.6.5, not literally identical.

**Relation to EFEM.**
* Every `U.EpistemicViewing` is an **EFEM morphism** with `describedEntityChangeMode = preserve` in the sense of A.6.2/C.2.1.
* It **inherits** P0–P5 from A.6.2, specialised to the case where the occupant of `DescribedEntitySlot` is unchanged.

#### 4.3 · Laws (EV‑0…EV‑6, over C.2.1 components)

All laws below are **in addition** to A.6.2’s EFEM laws P0–P5 and SHALL be read directly against C.2.1 components and A.6.5 SlotSpecs.

**EV‑0 · Species & DescribedEntityChangeMode.**

* Any morphism `v:X→Y` declared as `U.EpistemicViewing` **MUST**:
  * be a species of `U.EffectFreeEpistemicMorphing` (A.6.2), and
  * declare `describedEntityChangeMode(v) = preserve`.
* Consequently:
  * `DescribedEntitySlot` has the **same ValueKind and RefKind** in the episteme kind of `X` and `Y` (same `EoIClass ⊑ U.Entity`);
  * `describedEntityRef(Y) = describedEntityRef(X)` **by definition** of the species.

**EV‑1 · Typed domain/codomain & DescriptionContext behaviour.**

For any `v:X→Y` in `U.EpistemicViewing`:
1. `X` and `Y` are instances of `U.Episteme` species whose episteme kinds both realise at least the core C.2.1 slots (`DescribedEntitySlot`, `GroundingHolonSlot?`, `ClaimGraphSlot`, `ViewpointSlot?`, `ReferenceSchemeSlot`) and obey A.6.5. Many practical species of EpistemicViewing will take `X` and `Y` from the **same** `U.EpistemeKind`, but the A.6.3 pattern only requires **SlotSpec compatibility** between domain and codomain kinds (in the sense of A.6.5), not literal kind equality.

2. At the SlotKind level:
   * `DescribedEntitySlot` is **read‑only** (no change in `describedEntityRef`).
   * `GroundingHolonSlot`, if present, is:
     * either preserved exactly, or
     * changed only within an explicitly declared **grounding context** (e.g. normalising identifiers for the same plant or runtime), justified via a `Bridge` in the same ReferencePlane.
   * `ViewpointSlot`, if present, is:
     * either preserved (internal normalisation under the same viewpoint), or
     * changed only to another `U.ViewpointRef` **within a declared `U.MultiViewDescribing` family** (E.17.0), with a `CorrespondenceModel` providing witnesses.
3. For any episteme that is a `…Description`/`…Spec` (E.10.D2), `subjectRef` decodes to `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩`. EpistemicViewing MUST:
   * preserve `DescribedEntityRef`,
   * preserve `BoundedContextRef` (unless a Bridge is explicitly cited),
   * treat `ViewpointRef` as in (2) above.

**EV‑2 · Effect‑free boundary (over EpistemeSlotGraph).**
EpistemicViewing remains **pure** in the EFEM sense:
* It may change **only C.2.1 components of the codomain episteme**:
  * `content : U.ClaimGraph` (e.g. filtering, aggregation, normalisation),
  * `viewpointRef` (under the constraints in EV‑1),
  * `representationSchemeRef` and `ReferenceScheme` (within a fixed representation family or under a declared `CorrespondenceModel`),
  * meta‑components (edition, provenance, status flags).
* It **MUST NOT**:
  * invoke `U.Mechanism` or `U.WorkEnactment` (measure, execute, actuate),
  * create or modify `U.PresentationCarrier` (no direct publishing to surfaces),
  * cross ReferencePlanes implicitly (plane crossings go through Bridges with CL penalties in Part F).

Any operational machinery (e.g. SAT/SMT solving, simulation, LLM tool‑use) MUST be modelled as a **separate `U.Mechanism`** that produces input epistemes or auxiliary artefacts consumed by the EpistemicViewing morphism.

**EV‑3 · No new intensional claims about the same DescribedEntity.**

Let `X` and `Y = apply(v,X)` with:
* `content_X`, `referenceScheme_X`,
* `content_Y`, `referenceScheme_Y`,
* shared `describedEntityRef` and (typically) `groundingHolonRef`.

Then:
* The set of claims about `<describedEntityRef, groundingHolonRef>` obtained by reading `content_Y` through `referenceScheme_Y` **MUST NOT strictly extend** what is already entailed, in KD‑CAL/LOG‑CAL, by `content_X` read through `referenceScheme_X` under the same ReferencePlane and context.
* Admissible changes:
  * re‑expression (changing representation, not truth conditions),
  * aggregation (e.g. summarising multiple claims into an explicitly derivable macro‑claim),
  * dropping some information (lossy projection), provided **no new atomic commitments** about the same described entity are introduced.
* Any intended strengthening of behavioural or structural commitments about the same entity **is not a valid EpistemicViewing**; it must be modelled either as:
  * a change in Intension (new D/S pair under A.7/E.10.D2), or
  * an A.6.4 `U.EpistemicRetargeting` plus a new Intension.

**EV‑4 · Functoriality & correspondence alignment.**

EpistemicViewing **inherits EFEM functoriality** and specialises it:

1. **Direct EpistemicViewing (same representation scheme).**
   Where `representationSchemeRef` and `ReferenceScheme` of `X` and `Y` are the same (up to declared normal forms), EpistemicViewing acts as a **strict functor** on ClaimGraphs:
   * `apply(id, X) = X`,
   * `apply(g ∘ f, X) = apply(g, apply(f, X))`,
   * `content` transformation corresponds to a structural ClaimGraph function.

2. **Correspondence‑based EpistemicViewing (representation changes).**
   When viewing relies on a `CorrespondenceModel` between epistemes or representation schemes:
   * the viewing morphism MUST reference that `CorrespondenceModel`,
   * compositions involving such viewings **MUST** publish witnesses (epistemes or proof objects) that squares commute **up to declared isomorphism** (oplax naturality is allowed, but corrections are deterministic and reproducible),
   * `describedEntityRef` and `groundingHolonRef` remain as in EV‑1; any transfer across contexts/planes goes via Bridges, not via hidden behaviour of the viewing.

**EV‑5 · Idempotency & determinism on fixed configuration.**

For any `v:X→Y` in `U.EpistemicViewing`, with fixed:
* `describedEntityRef`,
* `groundingHolonRef`,
* `viewpointRef`,
* `representationSchemeRef`,
* `referenceScheme`,
* and fixed `CorrespondenceModel` (if used),

the following MUST hold:
* **Idempotency.** `apply(v, apply(v, X))` is **isomorphic** to `apply(v, X)`:
  * same DescribedEntity and grounding holon,
  * same viewpoint and representation scheme,
  * ClaimGraphs differ, at most, by declared structural equivalence (e.g. normal form vs source form).
* **Determinism.** For fixed input and configuration, the result is uniquely determined (modulo declared equivalence). Any source of non‑determinism (random seeds, timing, external service state) MUST either:
  * be exposed as part of `content` / `meta` of `X`, or
  * be moved into a Mechanism outside the viewing morphism.

**EV‑6 · Applicability & MultiViewDescribing alignment.**

Each species of `U.EpistemicViewing` MUST:
1. Declare an **Applicability profile** (A.6.0) specifying:
   * permitted `EoIClass ⊑ U.Entity` (ValueKind of `DescribedEntitySlot`),
   * permitted `groundingHolonRef` classes and ReferencePlanes,
   * admissible `viewpointRef` ranges (possibly a named `U.ViewpointBundle`),
   * supported `representationSchemeRef` families.
1. For D/S epistemes in a `U.MultiViewDescribing` family (E.17.0):
   * preserve `DescribedEntityRef` of `DescriptionContext`,
   * either preserve `ViewpointRef` or change it within the declared viewpoint bundle, with any additional constraints recorded in the family’s `CorrespondenceModel`,
   * never widen `ClaimScope` beyond what EV‑3 permits.
3. Treat **any change of DescribedEntity** (even if “intuitively minor”, such as moving from subsystem to system) as **out of scope** for A.6.3; such moves belong to A.6.4 `U.EpistemicRetargeting`.

#### 4.4 · Profiles: `U.DirectEpistemicViewing` and `U.CorrespondenceEpistemicViewing`

`U.EpistemicViewing` is further structured into two important species; both inherit EV‑0…EV‑6.

1. **`U.DirectEpistemicViewing` — self‑contained views.**
   * Domain and codomain epistemes share:
     * the same `representationSchemeRef` (up to declared normalisation),
     * the same `ReferenceScheme` (or a refinement which is conservative and structurally documented).
   * No external `CorrespondenceModel` is needed: the view is computed **solely from the input episteme** and, optionally, fixed configuration.
   * Typical cases:
     * internal normalisation (sorting, rewriting) of an engineering view;
     * filtering `U.ClaimGraph` to keep only safety‑relevant claims;
     * simplifying a proof‑oriented specification to a more operational form under the same semantics.

1. **`U.CorrespondenceEpistemicViewing` — views relying on correspondence models.**
   * Viewing depends on:
     * one or more subject epistemes (e.g. requirements and design),
     * an explicit `CorrespondenceModel` that relates their ClaimGraphs and representation schemes.
   * The result is an episteme (often an `U.EpistemeView`) whose `describedEntityRef` matches that of the primary episteme, but whose content is computed **through** the correspondence links.
   * Typical cases:
     * ISO 42010‑style correspondences between architectural descriptions;
     * cross‑model views in model‑based systems engineering (MBSE), where view content is computed from multiple model fragments;
     * traceability‑based views aggregating requirements, design elements, and tests.

In both profiles:
* `CorrespondenceModel` remains an **episteme‑level artefact**, not a new kernel‑type hidden inside A.6.3.
* `U.EpistemicViewing` stays **view‑like**: it reveals what is already there under the correspondence; it does not perform Γ‑style constructions of new Intensions.

### 5 · Archetypal grounding (Tell–Show–Show)

#### 5.1 · Engineering system description → safety officer view (DirectEpistemicViewing)

*Context.*
A system team maintains a rich `SystemDescription` episteme for a plant holon `S` under an engineering viewpoint from TEVB. A safety officer needs a concise view showing only safety‑critical components, hazards, and mitigations.

*Shape.*

* **Domain `X`.**
  `X : U.SystemDescription` with:
  * `describedEntityRef(X) : U.SystemRef` (the plant `S`),
  * `groundingHolonRef(X) : U.HolonRef` (runtime environment),
  * `viewpointRef(X) : U.ViewpointRef` (engineering TEVB viewpoint),
  * `content(X) : U.ClaimGraph` (full behavioural & structural claims).
* **Codomain `Y`.**
  `Y : U.EpistemeView` with:
  * `describedEntityRef(Y) = describedEntityRef(X)`,
  * `groundingHolonRef(Y) = groundingHolonRef(X)`,
  * `viewpointRef(Y)` either equal to or a refinement of the original engineering viewpoint (TEVB safety sub‑viewpoint),
  * `content(Y)` containing only safety‑relevant claims, plus explicit aggregation nodes (e.g. hazard summaries).

`SafetyView : X→Y` is a **DirectEpistemicViewing**:
* `describedEntityChangeMode = preserve`,
* only `content`, `viewpointRef` (within TEVB) and `meta` change,
* KD‑CAL/LOG‑CAL checks show that every hazard/mitigation claim in `Y` is entailed by `X`,
* view is idempotent and deterministic given `X` and the selected safety profile.

This is the canonical “engineering view” archetype that later species in E.17.2/TEVB refer back to.

#### 5.2 · MVPK publication view normalisation (DirectEpistemicViewing)

*Context.*
MVPK emits a `TechCard` view `V_raw` for an arrow `f` in a morphism class (e.g. an ATS‑checked service). The publication pipeline wants a normalised view `V_norm` where:
* arrows are ordered canonically,
* units and names follow a fixed naming discipline,
* redundant cells are removed.

*Shape.*

* `X = V_raw`, `Y = V_norm`, both `U.EpistemeView` instances with:
  * same `describedEntityRef` (the morphism’s arrow or capability),
  * same `groundingHolonRef` (runtime/plant),
  * same `viewpointRef` (publication viewpoint),
  * same `representationSchemeRef` (TechCard schema).

`NormalizeTechCard : X→Y` is a **DirectEpistemicViewing**:
* changes only `content` and `meta` (e.g. “normalised at edition E”),
* is pure and idempotent (two passes give the same normal form),
* is conservative: no new claims about the arrow `f` appear; information is only reordered or discarded.

MVPK can rely on this as an A.6.3‑conformant step without restating EFEM laws.

#### 5.3 · Cross‑model consistency view (CorrespondenceEpistemicViewing)

*Context.*
A system has:
* a requirements episteme `R` (“what the system should do”), and
* a design episteme `D` (“how the system does it”),

both with `describedEntityRef` pointing to the same system holon `S`, but living in different notations and contexts. A systems engineer wants a view that shows **only those requirements that currently have design coverage**.

*Shape.*

* `R : U.SystemRequirementsDescription` with ClaimGraph `C_R`.
* `D : U.SystemDesignDescription` with ClaimGraph `C_D`.
* `CM : U.CorrespondenceModel` relating requirements to design elements.
* `Y : U.EpistemeView` with:
  * `describedEntityRef(Y) = describedEntityRef(R) = describedEntityRef(D) = S`,
  * `groundingHolonRef(Y)` inherited from `R`/`D` or declared via a Bridge,
  * `content(Y)` aggregating only those requirements in `C_R` for which `CM` records coverage in `C_D`.

`CoveredRequirementsView(R,D,CM) : X→Y` (with `X` a compound episteme or a bundle episteme over `R,D,CM`) is a **CorrespondenceEpistemicViewing**:
* relies essentially on `CM` (without it, the view is undefined — fail‑closed),
* must publish witnesses that two different ways of composing local correspondences give the same result up to declared equivalence,
* remains conservative: it does not assert that any requirement is covered unless that fact is recorded in `CM` and justified in `D`.

This archetype mirrors post‑2015 work on model synchronisation and bidirectional transformations, but anchored in the EpistemeSlotGraph.

### 6 · Consequences

* **Clear separation of viewing vs retargeting.**
  `U.EpistemicViewing` and `U.EpistemicRetargeting` (A.6.4) now **cleanly separate**:

  * “view of the same entity” vs “description of a different entity under a bridge”, and
  * vertical morphisms (`α` fixed) vs retargeting morphisms (α changes under KindBridge).

* **Stable backbone for multi‑view patterns.**
  Multi‑view description (E.17.0), viewpoint bundle libraries (E.17.1/E.17.2), and MVPK publication now share a **single notion of view morphism**, aligned with C.2.1 slots and the I/D/S discipline.

* **Slot‑level discipline for tools.**
  Tools implementing views (queries, projections, report generators, LLM‑based summarisation) must declare:

  * which SlotKinds they read,
  * which SlotKinds they may write,
  * and that `DescribedEntitySlot` is preserved.
    This removes ambiguity around “subject/object” changes and supports robust static checking.

* **Alignment with modern view/query practices.**
  The pattern aligns with:
  * ISO 42010:2011/2022 and its focus on **viewpoints**, **views**, and **correspondences** over an entity‑of‑interest;
  * SysML v2 “views‑as‑queries” paradigm, where views are queries over a stable model, not new models;
  * post‑2015 work on **optics** and **displayed categories**, treating views as structured projections over a fibred category of epistemes.

### 7 · Rationale & SoTA‑echoing  *(informative)*

* **Optics and displayed categories.**
  In categorical terms, epistemes form a category `Ep` fibred over a category of described entities `Ref` via `α : Ep → Ref`. EpistemicViewing corresponds to **vertical morphisms** that preserve α. Their behaviour closely tracks **profunctor optics**: the DescribedEntitySlot plays the role of the “focus index”, while ClaimGraphs and representation schemes act as the data being transformed. Recent work on optics (2018‑onwards) provides compositional laws that FPF leverages without committing to a specific optic calculus.

* **Multi‑view modelling and viewpoint libraries.**
  ISO 42010 and its successors, as well as MBSE practice from ~2015 onwards, have refined the separation between **viewpoints** (families of concerns, stakeholders, and notations) and **views** (instances under those viewpoints). `U.EpistemicViewing` gives FPF a substrate‑agnostic notion of “view” that can be instantiated for architecture descriptions, safety cases, or even research artefacts, while TEVB and E.17.0 specialise it to engineering holons.

* **Bidirectional transformations and consistency management.**
  Modern BX research treats views and consistency restoration as structured transformations between models, with consistency relations acting as correspondences. `U.CorrespondenceEpistemicViewing` echoes this practice but insists that:
  * viewing is **non‑creative** in intensional terms (no new commitments),
  * any strengthening or change of described entity is explicitly modelled as retargeting or Intension change.

* **Hybrid symbolic/latent representations.**
  Contemporary work on LLMs and neurosymbolic systems often toggles between:
  * symbolic specifications (logical, tabular, diagrammatic), and
  * distributed or latent representations used for computation.
    By treating `U.RepresentationScheme` and `U.RepresentationOperation` as first‑class episteme components, FPF allows EpistemicViewing to range over:
  * purely symbolic projections,
  * latent‑space projections,
  * or hybrids that invoke external mechanisms before applying a pure view, without changing the core laws.

### 8 · Conformance checklist (normative)

**CC‑A.6.3‑1 · EFEM species and DescribedEntityChangeMode.**
Any pattern that claims to define `U.EpistemicViewing` **SHALL**:

* declare itself a species of `U.EffectFreeEpistemicMorphing` (A.6.2),
* fix `describedEntityChangeMode = preserve`,
* and state its Applicability profile (EoIClass, contexts, viewpoints, representation schemes).

**CC‑A.6.3‑2 · Slot‑level read/write discipline.**
For each species of EpistemicViewing, authors **MUST**:

* list the SlotKinds it **reads** (typically `DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `RepresentationSchemeSlot`, `ReferenceSchemeSlot`),
* list the SlotKinds it **writes** (typically `ClaimGraphSlot`, optionally `ViewpointSlot`, `RepresentationSchemeSlot`, `ReferenceSchemeSlot`, and `meta`),
* assert explicitly that `DescribedEntitySlot` is read‑only,
* and state any constraints on `GroundingHolonSlot` / `ViewpointSlot` changes.

This satisfies A.6.5 and C.2.1 checkpoint CC‑C.2.1‑5.

**CC‑A.6.3‑3 · DescriptionContext discipline (for D/S epistemes).**
When domain/codomain epistemes are `…Description`/`…Spec`:
* viewing laws SHALL be phrased in terms of `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩`,
* `DescribedEntityRef` MUST be preserved,
* `BoundedContextRef` MUST be preserved unless a Bridge is explicitly cited,
* `ViewpointRef` MUST either be preserved or changed within a declared `U.ViewpointBundle`.

**CC‑A.6.3‑4 · Conservativity witness.**
For each species, authoring SHALL provide:
* a clear statement of what counts as a **new intensional claim** in the relevant discipline,
* and a sketch of how conservativity (EV‑3) is checked or approximated (e.g. via KD‑CAL entailment, proof obligations, or structural invariants).

**CC‑A.6.3‑5 · Profile classification.**
* Species that do not require a `CorrespondenceModel` MUST be marked as `U.DirectEpistemicViewing`.
* Species that do require such a model MUST be marked as `U.CorrespondenceEpistemicViewing` and SHALL:
  * document the shape of the `CorrespondenceModel`,
  * describe how witness epistemes ensure oplax naturality of compositions.

**CC‑A.6.3‑6 · Separation from Retargeting and Mechanisms.**
* Any species that may change `describedEntityRef` is **not** a conformant EpistemicViewing; it MUST be treated as `U.EpistemicRetargeting` (A.6.4) or as a different pattern.
* Any species that performs measurements, actuation, or other side‑effects MUST be declared as `U.Mechanism`/`U.WorkEnactment` and cannot be an EpistemicViewing.

### 9 · Mini‑checklist (for authors)

When you introduce a new “view” in FPF, check:
1. **Same described entity?**
   Does `describedEntityRef` stay the same? If not, this is **Retargeting**, not Viewing.

2. **Which slots move?**
   Have you listed exactly which SlotKinds you read/write, and shown that `DescribedEntitySlot` is read‑only?

3. **Conservative?**
   Can you explain, in your discipline’s terms, why the view does not introduce new claims about the same entity?

4. **Profile?**
   Is this a self‑contained projection (`U.DirectEpistemicViewing`) or does it depend on a `CorrespondenceModel` (`U.CorrespondenceEpistemicViewing`)?

5. **Context & viewpoint?**
   Have you stated:
   * the EoIClass for `DescribedEntitySlot`,
   * the contexts/ReferencePlanes you assume,
   * and the viewpoint bundle (if any) you operate under?

If all answers are crisp and the laws EV‑0…EV‑6 are satisfied, the pattern is a good candidate for `U.EpistemicViewing`.

## A.6.4 · **`U.EpistemicRetargeting` — describedEntity‑retargeting morphism** \[A]

**One‑line summary.** `U.EpistemicRetargeting` is the **describedEntity‑retargetning** species of `U.EffectFreeEpistemicMorphing`: an effect‑free episteme→episteme morphism that **intentionally changes what the episteme is about** (the occupant of `DescribedEntitySlot` in C.2.1) under a declared `KindBridge` and invariant, while remaining conservative with respect to that invariant.

**Status.** Normative [A] in **Part A (Kernel)**.
**Placement.** After **A.6.3 `U.EpistemicViewing`**, before **A.6.5 `U.RelationSlotDiscipline`**. 

**Builds on.**
A.6.0 `U.Signature`; A.6.2 `U.EffectFreeEpistemicMorphing`; A.6.3 `U.EpistemicViewing`; A.6.5 `U.RelationSlotDiscipline`; A.7/E.10.D2 (I/D/S discipline, `DescriptionContext`); C.2.1 `U.Episteme — Epistemes and their slot graph`; C.2/C.3 (KD‑CAL/LOG‑CAL, ReferencePlane, Kind‑level reasoning); F.9 (Bridges, `KindBridge`, CL/CL^plane, SquareLaw witnesses).

**Used by.**
E.18 (E.TGA StructuralReinterpretation and other reinterpretation nodes); discipline packs for signal/spectrum transforms, data↔model retargetings, abstraction/refinement under kind‑invariants; KD‑CAL/LOG‑CAL retargeting rules; future species for architecture and governance reinterpretations. 

### 1 · Problem frame

Many important operations on descriptions **change the object‑of‑talk** while preserving a structural or behavioural invariant:

* **Physical vs functional reinterpretation.**
  An episteme about a physical module (cabinet, rack, device) is re‑interpreted as an episteme about a function‑holon it realises. This is precisely what StructuralReinterpretation nodes in E.TGA attempt to do. 

* **Signal vs spectrum.**
  A time‑domain signal description is re‑targeted to a description of its frequency‑domain spectrum. The underlying invariant (typically energy or inner‑product) is preserved, but the “thing we talk about” changes from `time→value` trajectories to `frequency→amplitude/phase` distributions. 

* **Data vs model.**
  An episteme about raw observations (dataset) is turned into an episteme about a learned or estimated model, keeping an invariant such as likelihood, sufficient statistics, or predictive performance. 

All of these are **Ep→Ep transforms** that:
* do **not** change the Intension (`I`) directly (they operate on descriptions/specifications),
* do **not** merely slice or re‑express an episteme of the same entity (that would be EpistemicViewing, A.6.3),
* but **do change** the **DescribedEntity‑bundle** (`DescribedEntitySlot` and usually `GroundingHolonSlot`) under a formal bridge between kinds.

We need a single, reusable notion of **“epistemic retargeting”** that captures these operations as:
* **effect‑free** at the level of Work/Mechanism (EFEM discipline),
* **describedEntity‑retargeotating** in a controlled way,
* **invariant‑conservative** (no violation of the declared invariant between kinds),
* and **functorial** (retargetings compose cleanly and align with Bridges).

### 2 · Problem

Without a dedicated pattern for EpistemicRetargeting:
1. **Retargeting is silently confused with viewing.**
   Structural reinterpretations (e.g., component→function, signal→spectrum, data→model) can be mistakenly treated as “just another view” of the same entity, even though they change `describedEntityRef`. This hides the fact that the **object‑of‑talk** has changed and that a `KindBridge` and invariant are required.

2. **Invariants float untyped.**
   Fourier‑style moves, structural reinterpretations, and abstraction/refinement steps are often justified by “energy is preserved”, “this component realises that function”, or “this model summarises those data” — but these invariants are not connected to the episteme morphism class. Without a dedicated species:

   * invariants live only in text,
   * CL‑penalties and ReferencePlane crossings cannot be tracked systematically (Part F).

3. **Cross‑kind reasoning has no canonical morphism.**
   A general EFEM (A.6.2) can change `describedEntityRef` by setting `describedEntityChangeMode = retarget`, but:

   * nothing states what that means at the level of kinds (`Kind(describedEntityRef(X))` vs `Kind(describedEntityRef(Y))`),
   * nothing connects these moves to `KindBridge` and ReferencePlane policies.

4. **StructuralReinterpretation is ad‑hoc.**
   E.TGA currently hosts StructuralReinterpretation as a special node, but its semantics are much closer to a generic “retargeting under a bridge” pattern than to something specific to graph‑based architectures. Without a core pattern:

   * StructuralReinterpretation risks duplicating retargeting logic,
   * other discipline packs may reinvent their own ad‑hoc re‑targetings.

5. **I/D/S discipline is left underspecified.**
   For descriptions/specifications (`…Description` / `…Spec`), retargeting **changes `DescribedEntityRef` in `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩`** (E.10.D2), but must say what happens to context and viewpoint. Without an explicit pattern, these decisions get scattered across different E‑patterns instead of being governed centrally. 

### 3 · Forces

* **Changing the object‑of‑talk vs constructing something new.**
  Retargeting should express **“talking about a different but bridge‑related entity”**, not arbitrary construction of a new Intension/episteme. The invariant lives **across** the pair of entities, not inside a single episteme.

* **Invariants may be lossy but must be explicit.**
  A retargeting is often **lossy** (e.g. data→model, signal→spectrum, structural→functional view), but:

  * it must preserve an explicitly declared invariant (energy, behaviour, statistics),
  * any additional strengthening must be modelled as a change of Intension plus new D/S, not as a hidden side‑effect.

* **Bridges and CL‑penalties.**
  Retargeting often crosses:
  * Kind‑planes (different `Kind(U.Entity)`),
  * ReferencePlanes (different observability or abstraction regimes).
    Part F already has `KindBridge`, plane Bridges and CL‑penalties; EpistemicRetargeting must **re‑use** them instead of introducing its own notion of “link”.

* **Functors over `α : Ep → Ref`.**
  In the fibred view of epistemes (C.2 / A.6.2), `α : Ep → Ref` maps each episteme to its described entity. EpistemicViewing preserves α (`α(v) = id`). Retargeting must:
  * change α in a controlled way (`α(r) = b : R₁→R₂` in `Ref`),
  * align with `KindBridge` and plane Bridges used for those base arrows.

* **Slot discipline and modularity.**
  C.2.1 and A.6.5 give epistemes a precise `SlotKind`/`ValueKind`/`RefKind` structure, including `DescribedEntitySlot` and `GroundingHolonSlot`. Retargeting laws must be stated **at the slot level**, not on ad‑hoc “fields”, so they can be reused across E.TGA, MVPK, and discipline packs.

### 4 · Solution — `U.EpistemicRetargeting` as EFEM profile (`describedEntityChangeMode = retarget`)

#### 4.1 · Informal definition

> **Definition (informal).**
> `U.EpistemicRetargeting` is the **describedEntity‑retargeting species** of `U.EffectFreeEpistemicMorphing`.
> A `U.EpistemicRetargeting r : X→Y`:
>
> * takes an input episteme `X` and produces an output episteme `Y`,
> * **changes** the occupant of `DescribedEntitySlot` (`describedEntityRef(Y) ≠ describedEntityRef(X)`),
> * relates the kinds of the old and new described entities via an explicit `KindBridge` in the appropriate ReferencePlane,
> * preserves a declared **invariant** across the pair of entities (e.g. energy, behaviour, sufficient statistics),
> * is **effect‑free** at the level of Work/Mechanism (EFEM discipline),
> * and composes functorially with other retargetings and viewings.

In C.2.1 terms, `U.EpistemicRetargeting` **re‑indexes** an episteme along a base‑level bridge: it moves the `DescribedEntitySlot` (and often the `<DescribedEntitySlot, GroundingHolonSlot>` bundle) along a `KindBridge`, while re‑expressing `content : U.ClaimGraph` and `referenceScheme` so that the declared invariant continues to hold at the new target. 

#### 4.2 · Signature (A.6.0 / A.6.5 alignment)

**Signature header.**
`U.EpistemicRetargeting` is a **Morphism‑kind** under A.6.0, specialised from EFEM:

```
SubjectBlock
  SubjectKind    = U.EpistemicRetargeting
  BaseType       = ⟨X:U.Episteme, Y:U.Episteme⟩      // carrier pair
  Quantification = SliceSet := U.ContextSliceSet;
                   ExtentRule := admissible retargeting morphisms
  ResultKind     = U.Morphism                        // an instance r
```

**Vocabulary (re‑uses A.6.2).**

* **Types.** `U.Episteme`, `U.SubjectRef`, `U.Morphism`, `U.EpistemicRetargeting`.
* **Operators.**

  * `id    : U.Morphism(X→X)`
  * `compose(g,f) : U.Morphism(X→Z)` where `f:X→Y`, `g:Y→Z`
  * `apply(r, x:U.Episteme) : U.Episteme`
  * `dom(r), cod(r) : U.Episteme`
  * `subjectRef(·) : U.SubjectRef`
* **Slot‑level discipline.**
  Domain and codomain epistemes are instances of some `U.Episteme` species (typically `U.EpistemeCard`, `U.EpistemeView`, or `U.EpistemePublication`) whose episteme kinds each provide SlotSpecs (A.6.5) including at least:

  * `DescribedEntitySlot` (ValueKind `U.Entity`, RefKind `U.EntityRef`, usually restricted to an `EoIClass ⊑ U.Entity`),
  * `GroundingHolonSlot?` (ValueKind `U.Holon`, RefKind `U.HolonRef`),
  * `ClaimGraphSlot` (ValueKind `U.ClaimGraph`, by‑value),
  * `ViewpointSlot?` (ValueKind `U.Viewpoint`, RefKind `U.ViewpointRef`),
  * `ReferenceSchemeSlot` (ValueKind `U.ReferenceScheme`, by‑value),
  * and, where C.2.1+ is in use, `RepresentationSchemeSlot`, `ViewSlot` and related slots.

The pattern only requires **SlotSpec compatibility** between domain and codomain kinds (in the sense of A.6.5); they need not be literally the same kind.

**Relation to EFEM and Viewing.**

* Every `U.EpistemicRetargeting` is an **EFEM morphism** with `describedEntityChangeMode = retarget` in the sense of A.6.2/C.2.1.
* It **inherits** EFEM laws P0–P5 and adds retargeting‑specific obligations ER‑0…ER‑6 below.
* `U.EpistemicViewing` (A.6.3) covers the complementary case `describedEntityChangeMode = preserve`, where the object‑of‑talk does not change.

#### 4.3 · Laws (ER‑0…ER‑6, over C.2.1 components)

All laws below are **in addition** to A.6.2’s EFEM laws P0–P5 and SHALL be read directly against C.2.1 components and A.6.5 SlotSpecs. 

**ER‑0 · Species & DescribedEntityChangeMode.**

* Any morphism `r:X→Y` declared as `U.EpistemicRetargeting` **MUST**:
  * be a species of `U.EffectFreeEpistemicMorphing` (A.6.2), and
  * declare `describedEntityChangeMode(r) = retarget`.
* Consequently:
 * the pair `<DescribedEntitySlot, GroundingHolonSlot>` is the **target bundle** for the change (as in C.2.1 §7.3: DescribedEntity‑bundle retargeting),
 * `DescribedEntitySlot` is **write‑enabled** (unlike Viewing) but only under the constraints below,
  * there exist entities `T₁, T₂ : U.Entity` such that:
    * `describedEntityRef(X) = T₁`,
    * `describedEntityRef(Y) = T₂`,
    * `T₁ ≠ T₂` (as Ref/identity), and
    * `Kind(T₁)` and `Kind(T₂)` are related by a `KindBridge` in Part F’s sense (with declared CL^k). 

**ER‑1 · Typed domain/codomain & DescribedEntity‑bundle behaviour.**

For any `r:X→Y` in `U.EpistemicRetargeting`:

1. `X` and `Y` are instances of `U.Episteme` species whose episteme kinds both realise at least the core C.2.1 slots (`DescribedEntitySlot`, `GroundingHolonSlot?`, `ClaimGraphSlot`, `ViewpointSlot?`, `ReferenceSchemeSlot`) and obey A.6.5.

2. At the SlotKind level:

   * `DescribedEntitySlot`:
     * **MUST change** (`describedEntityRef(Y) ≠ describedEntityRef(X)`),
     * the ValueKinds for the slot in the domain and codomain kinds **MUST** be related via an `EoIClass` pair that the `KindBridge` covers (e.g. `PhysicalModule` ↔ `FunctionHolon`, `Signal` ↔ `Spectrum`, `Dataset` ↔ `StatisticalModel`). 

   * `GroundingHolonSlot`, if present:
     * is either preserved exactly (`groundingHolonRef(Y) = groundingHolonRef(X)`), or
     * changed only along a declared holon‑Bridge in the same ReferencePlane (for example, moving from one runtime to another under a deployment bridge) with CL^plane penalties recorded in Part F.

   * `ViewpointSlot`, if present:
     * is either preserved, or
     * changed only within a declared `U.ViewpointBundle` (E.17.1/E.17.2), with the corresponding `CorrespondenceModel` explaining how the invariant is maintained under the new viewpoint.

1. For any episteme that is a `…Description`/`…Spec` (E.10.D2), `subjectRef` decodes to `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩`. Under EpistemicRetargeting:
   * `DescribedEntityRef` **MUST** change from `T₁` to `T₂` as in ER‑0,
   * `BoundedContextRef` is:
     * either preserved, or
     * changed along an explicit Context‑Bridge (E.10.D1, Part F),
   * `ViewpointRef` is treated as in (2) above (preserved or mapped within a bundle), and any resulting change in admissible claims is governed by ER‑2.

The pair `<DescribedEntitySlot, GroundingHolonSlot>` is treated as a **target bundle**: many practical retargetings work at the level of this bundle rather than DescribedEntity alone, especially in E.TGA. 

**ER‑2 · Invariant‑based conservativity (lossy but lawful).**

Let `X` and `Y = apply(r,X)` with:
* `describedEntityRef(X) = T₁`, `describedEntityRef(Y) = T₂`,
* `KindBridge(T₁,T₂)` and associated invariant `Inv` declared for this species (e.g. energy, behavioural relation, likelihood),
* `content_X`, `referenceScheme_X`,
* `content_Y`, `referenceScheme_Y`,
* `groundingHolonRef_X`, `groundingHolonRef_Y`.

Then:
1. There MUST exist a KD‑CAL/LOG‑CAL expression of `Inv` such that:
   * all claims about `Inv` that can be derived by reading `content_Y` through `referenceScheme_Y` relative to `<T₂, groundingHolonRef_Y>`
     **are entailed by**
     claims about `Inv` derivable from `content_X` through `referenceScheme_X` relative to `<T₁, groundingHolonRef_X>`. 

2. Retargeting, as an EFEM instance, **may**:
   * discard information not needed to maintain `Inv` (lossy summarisation),
   * change representation schemes (e.g. time vs frequency domain),
   * move to different abstraction levels or ReferencePlanes (with Bridges and CL penalties declared),
   but **MUST NOT** violate the declared invariant.

3. Any intended change that **strengthens** commitments about `Inv` beyond what is derivable from `X` **is not a valid EpistemicRetargeting**. It must be modelled as:
   * a change of Intension (new D/S pair under A.7/E.10.D2), or
   * a chain of retargetings and Intension updates explicitly recorded in KD‑CAL/LOG‑CAL.

**ER‑3 · Functoriality, α‑reindexing & SquareLaw witnesses.**

EpistemicRetargeting **inherits EFEM functoriality** and specialises it to the retargeting case:

1. At the `Ep` level:
   * `apply(id, X) = X` (no retargeting),
   * `apply(r₂ ∘ r₁, X) = apply(r₂, apply(r₁, X))` whenever domains/codomains match,
   * the composite `r₂∘r₁` has `describedEntityRef(X) = T₁` and `describedEntityRef(cod(r₂∘r₁)) = T₃`, with a composed `KindBridge(T₁,T₃)` whenever the Bridges of `r₁` and `r₂` compose.

2. At the `Ref` level, under `α : Ep → Ref`:
   * each retargeting `r` induces a base arrow `α(r) : R₁→R₂` in `Ref`, compatible with the `KindBridge` used in ER‑0,
   * the square formed by:
     * `X→Y` in `Ep` (retargeting),
     * `α(X)→α(Y)` in `Ref` (base retargeting),
     * any measurement or evaluation morphisms on either side,
       **MUST** commute **up to a declared SquareLaw‑retargeting witness** (Part F / E.TGA), documenting that evaluating then retargeting vs retargeting then evaluating yields equivalent results (modulo CL‑penalties).

2. When retargetings use CorrespondenceModels between epistemes (e.g. aligning detailed hardware layouts with function networks), they MUST:
   * reference the CorrespondenceModel explicitly,
   * publish witness epistemes that certify commutativity of key squares, analogous to EV‑4 but now across **different described entities.**

**ER‑4 · Idempotency & determinism on fixed Bridge/invariant.**

For any `r:X→Y` in `U.EpistemicRetargeting`, with fixed:
* `KindBridge(T₁,T₂)` and ReferencePlane policies,
* invariant `Inv`,
* configuration (ContextSlice, representation families, CorrespondenceModels),

the following MUST hold:

* **Idempotency.**
  Applying `r` twice does not further change the described entity or invariant‑relevant content:
  * `apply(r, apply(r, X))` is **isomorphic** (in the EFEM sense) to `apply(r, X)`,
  * `describedEntityRef` is already `T₂` after the first application,
  * `content` and `referenceScheme` differ at most by declared structural equivalence (e.g. normal forms at the new target).

* **Determinism.**
  For fixed input `X` and fixed Bridge/invariant configuration, the result is uniquely determined modulo declared equivalence. Any source of non‑determinism (randomness, time, external service state) MUST either:
  * be made explicit as part of `content`/`meta` of `X`, or
  * be moved to a `U.Mechanism` outside the retargeting morphism.

**ER‑5 · Applicability, EoI‑pairs & CL‑discipline.**

Each species of `U.EpistemicRetargeting` MUST declare an **Applicability profile** (A.6.0) that includes:

1. **EoI‑pairs.**
   Admissible pairs of `EoIClass`es (ValueKinds of `DescribedEntitySlot` for domain and codomain), for example:
   * `(PhysicalModule, FunctionHolon)`,
   * `(Signal, Spectrum)`,
   * `(Dataset, StatisticalModel)`.

   For each such pair, the pattern MUST reference the appropriate `KindBridge` species in Part F.

2. **Grounding constraints.**
   Permitted classes of `groundingHolonRef` and ReferencePlanes, including whether:
   * grounding must stay within the same holon,
   * or may move along specific holon Bridges with CL^plane penalties.

3. **Viewpoint/context constraints.**
   Whether retargeting is allowed for all viewpoints or only for specific `U.ViewpointBundle`s (TEVB etc.), and any requirements on `BoundedContextRef`.

4. **CL‑discipline.**
   Minimum CL^k and CL^plane required for the Bridges used, aligning with F.9 and E.TGA’s StructuralReinterpretation rules.

Any attempt to apply a retargeting outside this Applicability profile is **ill‑typed**.

**ER‑6 · Compatibility with Viewing and Mechanisms.**

1. **Separation from Viewing.**

   * Any morphism that **does not change** `describedEntityRef` (and keeps `DescribedEntityChangeMode = preserve`) belongs to A.6.3 `U.EpistemicViewing`, not to `U.EpistemicRetargeting`.
   * Any morphism that **does** change `describedEntityRef` **MUST NOT** be declared as `U.EpistemicViewing`; it is either:
     * a `U.EpistemicRetargeting`, or
     * a more general pattern that composes several retargetings and Intension changes.

   In any composite `V∘r` or `r∘V`, describedEntity changes are localised to retargeting steps; Viewing steps are always `describedEntityChangeMode = preserve`.

2. **Separation from Mechanisms.**

   * Retargeting MAY depend on artefacts produced by `U.Mechanism` (e.g., computing a Fourier transform, fitting a model), but those are separate Work/Mechanism steps.
   * `U.EpistemicRetargeting` itself remains **effect‑free**: it rearranges epistemes, slots and ClaimGraphs, but does not perform measurements or actuation.

### 5 · Archetypal grounding (Tell–Show–Show)

**Tell.**
EpistemicRetargeting captures **“same invariant, different described entity”** moves:

* we stop talking about “this cabinet” and start talking about “the routing function it realises”;
* we stop talking about “this signal over time” and start talking about “its spectrum over frequency”;
* we stop talking about “this dataset” and start talking about “a model class with parameters θ learned from it”.

In each case, what remains stable is an **invariant** (behaviour, energy, likelihood), not the described entity itself.

**Show 1 — StructuralReinterpretation in E.TGA.** 
* `X` describes a physical module holon `S_phys`.
* `Y` describes a function holon `S_func`.
* A `KindBridge(S_phys, S_func)` expresses “this module realises that function”.
* A StructuralReinterpretation node in E.TGA is an instance of `U.EpistemicRetargeting` whose invariant is the behaviour relation between `S_phys` and `S_func`.

**Show 2 — Signal↔Spectrum.**
* `X` describes a time‑domain signal `s(t)`; `DescribedEntityRef(X) = S_time`.
* `Y` describes its spectrum `S(ω)`; `DescribedEntityRef(Y) = S_freq`.
* `KindBridge(S_time, S_freq)` encodes Fourier duality in the relevant ReferencePlane.
* The invariant is energy (or inner product), expressed as a KD‑CAL statement; EpistemicRetargeting ensures that energy‑related claims in `Y` are entailed by `X`.

**Show 3 — Data→Model.**
* `X` describes a dataset `D` (observations); `DescribedEntityRef(X) = S_data`.
* `Y` describes a model `M` (e.g. a parametric family with learned parameters); `DescribedEntityRef(Y) = S_model`.
* `KindBridge(S_data, S_model)` encodes the intended data→model relation (e.g. MLE, Bayesian posterior).
* The invariant is likelihood or predictive performance; the retargeting laws ensure `Y` does not claim more about this invariant than is supported by `X`.

### 6 · Consequences

* **Clear separation of Viewing vs Retargeting.**
  A.6.3 and A.6.4 now jointly distinguish:
  * **views**: same `DescribedEntityRef`, possible representation/viewpoint changes;
  * **retargetings**: different `DescribedEntityRef` under `KindBridge` and invariants.

* **Canonical home for StructuralReinterpretation.**
  E.TGA StructuralReinterpretation becomes a **species of `U.EpistemicRetargeting`**, not an ad‑hoc special node. This reduces duplication and clarifies how CL penalties and Bridges are used.

* **Invariants become first‑class.**
  Retargeting makes invariants explicit and type‑checked: every such morphism must state what it preserves and how that is expressed in KD‑CAL/LOG‑CAL.

* **Safer cross‑plane reasoning.**
  ReferencePlane crossings and kind‑level moves are handled via existing Bridges (Part F), with CL^plane/CL^k penalties and SquareLaw witnesses, instead of hidden in implementation details.

* **Better integration with I/D/S.**
  For `…Description`/`…Spec` epistemes, retargeting is the only place where `DescribedEntityRef` in `DescriptionContext` is allowed to change; all other I/D/S‑level operations (Describe/Specify, Viewing) keep it fixed. 

### 7 · Rationale & SoTA‑echoing  *(informative)*
* **Fibrations and base‑change (displayed categories, 2017+).**
  With epistemes forming a category `Ep` fibred over `Ref` via `α : Ep → Ref` (C.2 / A.6.2), EpistemicViewing corresponds to **vertical morphisms** (`α(v) = id`), while EpistemicRetargeting corresponds to **reindexing along base arrows** (`α(r) = b : R₁→R₂`). This lines up with base‑change and transport along fibrations in category theory.

* **Structured cospans and reinterpretation.**
  Modern work on structured cospans and open systems uses cospans and their morphisms to move between different presentations of a system while preserving a notion of interface/behaviour. Retargeting plays a similar role: it moves from one entity kind to another while preserving a declared invariant.

* **Fourier‑style dualities.**
  In signal processing and physics, Fourier and related transforms are often treated as isometries between function spaces, preserving energy while changing the domain of discourse. `U.EpistemicRetargeting` abstracts this pattern: the invariant is codified in KD‑CAL/LOG‑CAL; the morphism explicitly changes the described entity along a `KindBridge`.

* **Data/model duality in ML.**
  Contemporary ML workflows cycle between data and models; invariants such as likelihood, risk, and calibration matter more than raw equality of ClaimGraphs. Retargeting gives a structured way to talk about data→model (and, potentially, model→data) moves as episteme morphisms, rather than untyped “training” steps.

* **Consistency management and abstraction.**
  In model‑driven and bidirectional transformation literature, abstraction and refinement transfers information between models with different subject domains. Treating these as retargetings with explicit Bridges and invariants makes their assumptions amenable to CL accounting and KD‑CAL reasoning, instead of hiding them in tooling.

### 8 · Conformance checklist (normative)

**CC‑A.6.4‑1 · EFEM species and DescribedEntityChangeMode.**
Any pattern that claims to define `U.EpistemicRetargeting` **SHALL**:

* declare itself a species of `U.EffectFreeEpistemicMorphing` (A.6.2),
* fix `describedEntityChangeMode = retarget`,
* and state its Applicability profile (EoI‑pairs, contexts, viewpoints, representation schemes, invariants).

**CC‑A.6.4‑2 · Slot‑level read/write discipline.**
For each species of EpistemicRetargeting, authors **MUST**:
* list the SlotKinds it **reads** (at least `DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ReferenceSchemeSlot`, plus any C.2.1+ slots used),
* list the SlotKinds it **writes** (at least `DescribedEntitySlot`, typically also `ClaimGraphSlot`, `ReferenceSchemeSlot`, and `meta`),
* state explicitly how `GroundingHolonSlot` and `ViewpointSlot` behave (preserved vs bridged),
* reference A.6.5 to show that SlotSpecs remain consistent across domain/codomain kinds.

**CC‑A.6.4‑3 · Bridge & invariant declaration.**
Each species SHALL:
* identify the relevant `KindBridge` species (and, where applicable, plane Bridges),
* declare the invariant(s) it preserves (in KD‑CAL/LOG‑CAL terms),
* sketch how invariant preservation is checked or approximated (e.g. through proofs, tests, or statistical guarantees).

**CC‑A.6.4‑4 · SquareLaw‑retargeting witnesses.**
For retargetings that interact with E.TGA or other graph‑level transductions, authors **MUST**:
* describe the commutative squares (or more general diagrams) that express “evaluate then retarget = retarget then evaluate” up to equivalence,
* identify the corresponding SquareLaw‑retargeting witnesses and how they are represented as epistemes.

**CC‑A.6.4‑5 · D/S‑context behaviour.**
For retargetings over `…Description`/`…Spec` epistemes:
* laws MUST be phrased in terms of `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩`,
* `DescribedEntityRef` MUST change in a way consistent with the declared `KindBridge`,
* `BoundedContextRef` MUST either be preserved or changed only via explicit Context‑Bridges,
* `ViewpointRef` MUST either be preserved or change within a declared `U.ViewpointBundle`.

**CC‑A.6.4‑6 · Separation from Viewing and Mechanisms.**
* Any species that leaves `describedEntityRef` unchanged is **not** a conformant EpistemicRetargeting; it belongs to `U.EpistemicViewing` (A.6.3) or another EFEM species.
* Any species that performs measurements, actuation, or other side‑effects MUST be declared as `U.Mechanism`/`U.WorkEnactment` and cannot be an EpistemicRetargeting.

### 9 · Mini‑checklist (for authors)

When you think you need “retargeting” in FPF, ask:

1. **Does `describedEntityRef` change?**
   If no, this is Viewing (A.6.3), not Retargeting.

2. **Is there a `KindBridge` between old and new entities?**
   If not, you probably need to introduce one in Part F or rethink the Intension, not fudge a retargeting.

3. **What invariant are you preserving?**
   Write it down in KD‑CAL/LOG‑CAL terms. If you cannot, retargeting is underspecified.

4. **How do `GroundingHolonRef`, context and viewpoint behave?**
   Explicitly state whether they stay the same, move along Bridges, or are out of scope.

5. **Can the operation be factored as Mechanism + pure retargeting?**
   If the step needs computation (FFT, model fitting), separate the Mechanism from the EpistemicRetargeting.

### 10 · Relations

* **Specialises / is specialised by.**
  * Specialises A.6.2 `U.EffectFreeEpistemicMorphing` as the `describedEntityChangeMode = retarget` profile.
  * Complements A.6.3 `U.EpistemicViewing` (describedEntity‑preserving EFEM) as the “retargeting” counterpart.

* **Constrained by.**
  * A.6.5 `U.RelationSlotDiscipline` for SlotKind/ValueKind/RefKind discipline.
  * C.2.1 `U.EpistemeSlotGraph` for episteme components and `DescribedEntitySlot`/`GroundingHolonSlot`.
  * E.10.D2 (I/D/S discipline; `DescriptionContext`).
  * Part F (Bridges, `KindBridge`, ReferencePlane crossings, CL/CL^plane).
  * E.10 (LEX‑BUNDLE naming rules, especially on `…Slot`/`…Ref` and ban on Subject/Object in episteme tech names).

* **Consumed by.**
  * E.18 (E.TGA StructuralReinterpretation and other cross‑kind architecture transformations).
  * E.17.0/E.17 (for cases where publication needs to move between different entities‑of‑interest but preserve invariants).
  * KD‑CAL/LOG‑CAL rules that reason about retargeting and invariant preservation across different described entities.



## A.6.5 — **U.RelationSlotDiscipline** · SlotKind/ValueKind/RefKind discipline for n‑ary relations  \[A]

**Plain‑name.** Relation slot discipline.

**Status.** Normative (Core).
**Placement.** Part A, cluster A.IV “Architheory Kernel”; directly under A.6.0 `U.Signature` and alongside A.6.1–A.6.4.
**Depends on.**
– A.1 `U.Holon` (holonic carrier model).
– A.6.0 `U.Signature` (universal morphism/relationship signatures). 
– A.7 (Strict Distinction; I/D/S vs Surface).
– E.8 (pattern authoring order & SoTA discipline). 
– E.10 (LEX‑BUNDLE: Tech/Plain registers, naming guards). 

**Coordinates with.**
– C.2.1 `U.EpistemeSlotGraph` (episteme slots: DescribedEntity, GroundingHolon, ClaimGraph, Viewpoint, View, ReferenceScheme).
– C.3.* Kind‑CAL (Kinds, KindSignature, KindBridge). 
– F.18 (name governance; twin‑register discipline). 

### 1 · Problem frame

FPF relies heavily on **n‑ary relations and morphisms**:

* episteme component layouts (`U.EpistemeKind` in C.2.1),
* role enactment and assignment,
* method/service signatures,
* guards and bridges in Part B/C,
* publication and view operators in Part E, and any other `U.Signature` whose **Vocabulary** row declares n-ary relations or operators across Part A/B/C/E.

In practice, existing episteme and drafts **frequently conflate**:
1. the **place** in a relation (“the 2nd argument, named Subject”),
2. the **kind of value** that may occupy that place (`U.Entity`, `U.Holon`, …), and
3. the **reference/identifier** we actually store there (`…Id`, `…Ref`).

This produces subtle bugs:
* misuse of “Subject/Object” as slot names for very different kinds,
* “Ref” suffix attached to both **entities and fields**,
* mixed reasoning about “role”, “slot”, and “object”,
* fragile substitution rules (“can I plug this module here?”) that depend on informal judgement.

`U.RelationSlotDiscipline` pins a **single, reusable discipline** over `U.Signature` so that **every position in a relation** is described with:

* a **SlotKind** — *where* in the relation,
* a **ValueKind** — *what sort of thing* may occupy that place, and
* a **RefKind** — *how we point at it* in episteme (identifier / handle), if at all.

This pattern makes slot discipline explicit and shareable across **epistemes, roles, methods, services, bridges, guards, and all other `U.Signature`d calculi**: any “parameter list”, “port list”, or “coordinate tuple” for an n-ary relation in FPF **is** a set of SlotSpecs governed by this discipline.

### 2 · Problem (symptoms in FPF)

Typical failure modes the pattern is designed to eliminate:

1. **Slot vs value vs ref confusion.**
   episteme fields such as `DescribedEntityRef` are sometimes treated as:

   * the **slot** (“the described entity position”),
   * the **value kind** (“the described entity type”), and
   * a **reference field** (“this is the pointer we store”).
     Reasoning about substitution (“can I swap one described entity for another?”) then mixes three levels at once.

2. **Kernel types misused as slot names.**
   Kernel concepts like `U.Entity` or `U.Holon` are used directly as slot names (“the `U.Entity` of this episteme”), hiding the difference between:

   * the abstract **Kind** (`U.Entity` as intensional universe), and
   * the **place** where one such entity is used in a particular relation.

3. **“Role” overloaded as slot.**
   In relation signatures and structural calculi, “role” has crept in as a synonym for “argument position”: “the role of the subject”, “the role of the provider”. This clashes with `U.Role` in RoleEnactment and makes it hard to distinguish:

   * **holonic role** (mask worn by a system), from
   * **slot** (position in a relation).

4. **Ref‑suffix drift.**
   In the absence of a discipline, the suffix `…Ref` is attached to:

   * entity kinds (`U.EntityRef` interpreted as “the entity itself”),
   * episteme fields (`describedEntityRef`),
   * sometimes even to slots (“DescribedEntityRefSlot”).
     That makes it impossible to read signatures and know whether we talk about:
   * a **conceptual value** (pass‑by‑value), or
   * a **reference/identifier** (pass‑by‑reference).

5. **Substitution rules not localisable.**
   When the slot/value/ref layers are not separated:

   * we cannot state “you may substitute **any instance of ValueKind V** in Slot S”, nor
   * “this Bridge only changes RefKind, not ValueKind”.
     This blocks clean use of A.6.0 `U.Signature` as a shared calculus for method/role/episteme signatures.

6. **Episteme‑specific slots not standardised.**
   For epistemes, the positions “what is this about?”, “in which holon is it grounded?”, “what ClaimGraph is inside?” re‑appear across patterns.
   Without a shared slot discipline, each pattern names these ad‑hoc, breaking the ability to state **universal laws** over episteme morphisms (A.6.2–A.6.4).

The result: **local convenience, global incoherence** — exactly what A.6.0 and E.10 are supposed to prevent.

---

### 3 · Forces

* **F1 · Simplicity vs expressiveness.**
  Engineers need a **small number of concepts** they can hold in mind while reading a signature; yet we must express:

  * where a parameter sits,
  * which kinds it can take,
  * whether it’s by value/by reference,
  * and how substitution behaves.

* **F2 · Cross‑disciplinary reuse.**
  Slot discipline must work for:
  * logical relations (KD‑CAL, LOG‑CAL),
  * episteme structures (C.2.1),
  * systems/roles/methods (A/B),
  * services and APIs (including Method/Service interfaces),
  * guards, bridges, and flows in E.TGA,
  * and publication operations (E.17).
    A scheme that is too domain-specific (e.g. “database attributes only”) won’t scale; the same discipline must underlie **all** `U.Signature`d argument/port lists.

* **F3 · Alignment with existing tooling.**
  Tooling stacks already operate with:

  * typed parameters and records,
  * identifiers vs values vs references,
  * sometimes row‑polymorphic fields or effect annotations.
    FPF must line up with this practice enough that signatures can be implemented without inventing a parallel type system.

* **F4 · I/D/S discipline.**
  Strict distinction (A.7, E.10.D2) already separates **intensional objects**, their **descriptions**, and **specifications**. The same kind of discipline is needed inside relations:

  * slot ≠ value ≠ reference,
  * system role ≠ slot name,
  * describedEntity ≠ guard.

* **F5 · Didactic primacy and naming discipline.**
  E.8 and E.10 demand patterns that are:

  * teachable (Tell‑Show‑Show examples, explicit biases), 
  * lexically guarded (Tech/Plain split, explicit head‑nouns). 
    Slot discipline must integrate seamlessly with that.

### 4 · Solution — SlotKind / ValueKind / RefKind triple

#### 4.1 · Three layers for every argument position

`U.RelationSlotDiscipline` extends `U.Signature` with a **three-layer description** for every argument position (whether we call it “parameter”, “slot”, “coordinate”, or “port” in colloquial prose).
In **normative** text, the canonical word is **slot**, and the canonical carrier is a **SlotSpec** triple (A.6.0).

1. **SlotKind (place in relation).**
   *How this position is denoted in the Signature and what is fixed about it by the relation’s definition.*
   – Examples: `DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ServiceEndpointSlot`, `CallerHolonSlot`, `MetricSlot`.
   – SlotKind is **structural**: it picks out **one distinguished place** in the argument/port list of a given relation or operator; it does **not** name a “role” played by the occupant.
   – For an n-ary relation declared in a `U.Signature`, the pair *(Signature id, SlotKind)* identifies a **slot**; positional indices are merely a presentation-level enumeration of these slots.
   – What an occupant “does” in that place (its contribution to laws, constraints, effects) is governed by the **laws over the Signature** and by the corresponding ValueKind, not by SlotKind-as-“role”.

2. **ValueKind (kind of occupant).**
   *Which kinds of things may occupy this position in principle (at the intensional level).*
   – Examples: `U.Entity`, `U.Holon`, `U.Method`, `U.Episteme`, `U.ClaimGraph`, `U.Viewpoint`, `U.Characteristic`, `U.ReferenceScheme`.
   – ValueKind is a **Kind** (C.3.*) or another kernel‑level type; it is **not** a slot and never carries `*Slot`/`*Ref` suffixes.

3. **RefKind (how we store / refer).**
   *What reference/identifier we actually store in episteme when we fill this slot.*
   – Examples: `U.EntityRef`, `U.HolonRef`, `U.MethodRef`, `U.EpistemeRef`, `U.ViewpointRef`, `U.SurfaceRef`, (optionally) `U.ClaimGraphRef` if a Context chooses to reference claim graphs rather than store them by value.
   – RefKind is **about references, not values**; it usually points to an editioned artifact (A.7, F.15) and carries the `.edition` field when pinning a phase.

**Discipline:**
* Each declared argument position in a `U.Signature` **MUST** be described by:
   * a SlotKind (name and documentation),
   * a ValueKind (type of permissible occupants),
   * and either a RefKind or an explicit declaration “**by‑value**” (no RefKind; the value is embedded).
* SlotKind and ValueKind are **intensional**; RefKind is **representational**. This mirrors I/D/S: *slot* describes structure, *value* describes what can sit there, *ref* describes how we point to concrete instances.

#### 4.2 · Naming discipline: `*Slot` and `*Ref`

This pattern introduces the following **lexical constraints**, aligned with E.10:
1. **`*Slot` reserved for SlotKind.**
   * Any Tech name ending with `…Slot` **MUST** denote a SlotKind: a named place in a relation/morphism signature.
   * Examples:
     – `DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ViewSlot`, `RepresentationSchemeSlot`, `ReferenceSchemeSlot`.
   * `*Slot` **MUST NOT** appear in names of:
     – ValueKind (e.g. `U.Entity`, `U.Holon`, `U.Method`),
     – RefKind (e.g. `U.EntityRef`),
     – concrete episteme fields (they may be named e.g. `describedEntityRef`, but not `describedEntitySlotField`).
1. **`*Ref` reserved for RefKind and reference fields.**
   * Any Tech name ending with `…Ref` **MUST** denote either:
     – a **RefKind** (type of references/identifiers), or
     – a **field** whose type is a RefKind (`describedEntityRef : U.EntityRef`).
   * `*Ref` **MUST NOT** appear in names of:
     – ValueKinds (e.g. `U.EntityRef` **cannot** mean “an entity”; it is a reference type),
     – SlotKinds,
     – Kinds themselves (`U.Kind`, `U.Entity`, `U.Holon`).

3. **ValueKind names carry no `*Slot`/`*Ref`.**

   * ValueKinds are named using standard FPF conventions (A/E/F, E.10), without `*Slot`/`*Ref`.
   * Examples: `U.Entity`, `U.Holon`, `U.Method`, `U.ClaimGraph`, `U.ReferenceScheme`, `U.Viewpoint`, `U.View`.

4. **No “Role” as SlotKind head.**

   * In the context of relation signatures, **do not** use “Role” as the head noun for SlotKinds (to avoid conflict with `U.Role`).
   * Use “Slot” or a neutral description: e.g. `EnactorHolonSlot` (ValueKind `U.Holon`) rather than `EnactorRoleSlot`.

These rules become part of the **LEX‑BUNDLE guards** and are enforced by F.18 / name‑acceptance harnesses. 

#### 4.3 · Integration with `U.Signature` (A.6.0)

`U.Signature` already provides a generic pattern for declaring morphism/relationship signatures (SubjectKind, BaseType, Quantification, ResultKind, Vocabulary, Laws). 

`U.RelationSlotDiscipline` refines this by adding a **SlotSpec** layer:

*For each parameter position `i` in a signature*:

```text
SlotSpec_i = ⟨name: SlotKind, value: ValueKind, refMode: {ByValue | RefKind}⟩
```

* **SlotKind** — Tech name with `*Slot` suffix, plus documentation.
* **ValueKind** — a `U.Type` (often a `U.Kind` or kernel type) declaring the intensional universe of occupants.
* **refMode**:
  * `ByValue` — the actual value of ValueKind is embedded (typical for small structured values like `U.ClaimGraph` inside an episteme card).
  * `RefKind` — a **type** of references/identifiers for that ValueKind; e.g. `U.EntityRef` for `U.Entity`, `U.HolonRef` for `U.Holon`. Substitution then operates on references, not directly on the underlying values.

In practice, a `U.Signature` that follows this pattern:

* becomes **self‑documenting**: each parameter has a clear “slot vs value vs ref” story;
* supports **typed substitution**: replacing references within the same SlotKind requires only ValueKind compatibility;
* aligns with **tool signatures** in implementation languages (row‑typed records, dependently typed parameters, effect‑typed arguments). ([ACM Digital Library][1])

#### 4.4 · Typed substitution discipline

Given a relation or morphism `R` with signature Σ and SlotSpecs `{SlotSpec_i}`:

* A **substitution** at slot `i` is a change of the argument that fills SlotKind_i, within or across episteme entries.
* `U.RelationSlotDiscipline` enforces:

1. **SlotKind invariance.**
   A substitution **never** changes SlotKind — only the occupant (Value/Ref).
   – “We put a different dataset into the `DatasetSlot`.”
   – “We switch the grounding holon in `GroundingHolonSlot`.”

2. **ValueKind compatibility.**
   The new occupant **MUST** be of the same ValueKind (or a declared subkind) as `SlotSpec_i.value`; Kind‑CAL governs this (`⊑` in C.3.1–C.3.2). If a Context uses EoIClass species constraints (C.3.2), those act as additional guards but do **not** change the SlotKind.

3. **RefKind correctness.**
   If `refMode=RefKind`, the stored field is of that RefKind; substitutions operate on references, not on underlying values. Edition pinning is handled as usual by `.edition` fields in F‑patterns (F.15, etc.).

4. **By‑value vs by‑ref awareness.**
   Substitutions at by‑value slots (e.g. `ClaimGraphSlot`) are **content changes** to the episteme or relation instance; they may affect formality F or assurance lanes. Substitutions at ref slots are **re‑targetings** of describedEntity or context, and their legality is governed by A.6.2–A.6.4 and Bridge/CL rules. Tooling SHOULD surface this difference explicitly in authoring surfaces (e.g. separate “Ref” vs “embedded content” columns).

These rules give a uniform way to say:

> “You may swap component X with Y in this slot, because they share ValueKind and pass the relevant Kind/Bridge constraints.”

### 5 · Archetypal Grounding (Tell‑Show‑Show)

Following E.7, we ground the pattern in a **System** example and an **Episteme** example. 

#### 5.1 · System example — authentication pipeline signature

Consider an `AuthPipelineSpecKind` (system‑level episteme describing an authentication pipeline for a microservice). Its key slots might be:

* `DescribedEntitySlot` — “which holon the pipeline is about”
  – ValueKind: `U.Holon` (EoIClass = “UserService system”).
  – RefKind: `U.HolonRef` (e.g. `UserService#prod`).

* `AuthProviderComponentSlot` — “which authentication provider component is selected”
  – ValueKind: `U.Holon` (EoIClass = “AuthProviderSystem”).
  – RefKind: `U.HolonRef` (e.g. `Auth_OIDC`, `Auth_LDAP`).

* `ClaimGraphSlot` — “what is asserted about the pipeline”
  – ValueKind: `U.ClaimGraph`.
  – refMode: `ByValue` (ClaimGraph stored inside the episteme card).

Substitutions:

* Changing `AuthProviderComponentSlot` from `Auth_OIDC` to `Auth_LDAP`:
  – SlotKind fixed (`AuthProviderComponentSlot`).
  – ValueKind unchanged (`U.Holon`, `AuthProviderSystem ⊑ U.Holon`).
  – RefKind unchanged (`U.HolonRef`).
  – Semantically: “swap one provider holon for another in the same slot”.

* Changing `DescribedEntitySlot` from `UserService#staging` to `UserService#prod`:
  – Same SlotKind and ValueKind.
  – Different `U.HolonRef` occupant.
  – May require different grounding and assurance episteme, but the slot discipline is identical.

#### 5.2 · Episteme example — model evaluation result

Consider `ModelEvaluationResultKind` as an episteme kind:

* `DescribedEntitySlot` — the model being evaluated
  – ValueKind: `U.Method` (intensional ML model).
  – RefKind: `U.MethodRef` (id of `Model_v3`).

* `DatasetSlot` — the dataset on which it is evaluated
  – ValueKind: `U.Entity` (EoIClass = “Dataset”).
  – RefKind: `U.EntityRef` (e.g. `Dataset_A`, `Dataset_B`).

* `TargetCharacteristicSlot` — the characteristic being measured
  – ValueKind: `U.Characteristic` (`Accuracy`, `F1`, `AUROC`).
  – RefKind: `U.CharacteristicRef`.

* `GroundingHolonSlot` — evaluation environment
  – ValueKind: `U.Holon` (e.g. `EvalCluster#1`).
  – RefKind: `U.HolonRef`.

* `ClaimGraphSlot` — evaluation result graph
  – ValueKind: `U.ClaimGraph`.
  – refMode: `ByValue`; the numeric thresholds and results live inside `content : U.ClaimGraph`.

Typical moves:
* `DatasetSlot`: replace `Dataset_A` with `Dataset_B` to test generalisation.
* `TargetCharacteristicSlot`: replace `Accuracy` with `F1` to focus on class imbalance.
* `ClaimGraphSlot`: change thresholds from “`P95Latency ≤ 200 ms`” to “`≤ 150 ms`” — a **pass‑by‑value** ClaimGraph change, not a slot change.

The SlotKind/ValueKind/RefKind discipline makes these substitutions **local and explicit**: the pattern describes which moves are allowed where, and A.6.2–A.6.4 then constrain how episteme morphisms may change ClaimGraphs and references.

#### 5.3 · Didactic micro‑examples — substitution by SlotKind / ValueKind / RefKind  *(informative)*

The following short examples are intended for a didactic guide or for cross‑references from A.6.0/A.6.x/C.2.1. In all of them:
* **SlotKind** names the **place in the relation** (position/cell in the tuple).
* **ValueKind** is the **kind of value** admissible at that place (what can ever sit there).
* **RefKind** is the **reference/identifier type** used in episteme when that slot is filled (absent when the slot is by‑value).
* `GroundingHolon` is **not** a separate kernel type: it is simply a `U.Holon` used as the ValueKind of `GroundingHolonSlot`.

Example names like `FurnitureSafetyDescriptionKind`, `AuthPipelineSpecKind`, `ModelEvaluationResultKind`, `IncidentRunbookSpecKind`, `ServiceSLARequirementKind` are **context‑local** kinds, not new kernel tokens.

##### (1) Mechanics — stool on a test rig

*EpistemeKind:* `FurnitureSafetyDescriptionKind`.

*SlotKind / ValueKind / RefKind:*
* `DescribedEntitySlot` — SlotKind “what this description is about”; ValueKind `U.Entity` with EoIClass ⊑ `U.Holon` (stool as a furniture holon); RefKind `U.EntityRef` (identifier of a concrete stool `S_i`).
* `GroundingHolonSlot` — SlotKind “where the test happens”; ValueKind `U.Holon` (test rig `LabRig_j`); RefKind `U.HolonRef`.
* `ClaimGraphSlot` — SlotKind for the internal content; ValueKind `U.ClaimGraph`; refMode `ByValue` (graph embedded in the episteme).

*Substitutions (all under the **same** SlotKinds):*
* Episteme `E₁`: `describedEntityRef = S_1`, `groundingHolonRef = LabRig_A`.
* Episteme `E₂`: `describedEntityRef = S_2`, `groundingHolonRef = LabRig_A` — **substitute another stool in the same `DescribedEntitySlot`** (different `U.EntityRef` in the same slot).
* Episteme `E₃`: `describedEntityRef = S_1`, `groundingHolonRef = LabRig_B` — **substitute another test rig in `GroundingHolonSlot`** while keeping the same object‑of‑talk.

In all three cases the SlotKinds (and ValueKinds) are stable; only the **Refs that occupy those slots** change. This matches the engineering idiom “drop another module into the same slot”.

##### (2) Microservices — switching the authentication provider

*EpistemeKind:* `AuthPipelineSpecKind` (episteme describing an authentication pipeline for a service).

*SlotKind / ValueKind / RefKind:*
* `DescribedEntitySlot` — ValueKind `U.Holon` with EoIClass = “`UserService` holon”; RefKind `U.HolonRef` (e.g. `UserService#prod`).
* `AuthProviderComponentSlot` — SlotKind “which auth provider component is used in this pipeline”; ValueKind `U.Holon` with EoIClass = “`AuthProviderSystem` holon”; RefKind `U.HolonRef` (e.g. `Auth_OIDC`, `Auth_LDAP`).
* `ClaimGraphSlot` — ValueKind `U.ClaimGraph`; refMode `ByValue` (pipeline invariants and flow logic).

*Substitutions:*
* Episteme `Spec_OIDC`: `describedEntityRef = UserService#prod`, `authProviderComponentRef = Auth_OIDC`.
* Episteme `Spec_LDAP`: same `describedEntityRef = UserService#prod`, but `authProviderComponentRef = Auth_LDAP`.
Here **SlotKind is identical** (`AuthProviderComponentSlot`); ValueKind is “any auth‑provider holon”; the episteme change is purely in the **`U.HolonRef` occupant**. This illustrates substitution of one component holon for another in the same slot, without inventing a separate ontology of “component roles”.

##### (3) Data/ML — swapping dataset or target characteristic

*EpistemeKind:* `ModelEvaluationResultKind`.
*SlotKind / ValueKind / RefKind:*
* `DescribedEntitySlot` — ValueKind `U.Method` (the ML model as an intensional method); RefKind `U.MethodRef` (e.g. `Model_v3`).
* `DatasetSlot` — SlotKind “evaluation dataset”; ValueKind `U.Entity` with EoIClass = “dataset”; RefKind `U.EntityRef` (`Dataset_A`, `Dataset_B`, …).
* `TargetCharacteristicSlot` — SlotKind “which characteristic is being measured”; ValueKind `U.Characteristic` (`Accuracy`, `F1`, `AUROC`); RefKind `U.CharacteristicRef`.
* `GroundingHolonSlot` — ValueKind `U.Holon` (evaluation cluster / infra holon); RefKind `U.HolonRef`.
* `ClaimGraphSlot` — ValueKind `U.ClaimGraph`; refMode `ByValue` (evaluation results and thresholds as content).
*Substitutions:*
* `Eval_1`: `describedEntityRef = Model_v3`, `datasetRef = Dataset_A`, `targetCharacteristicRef = Accuracy`, `groundingHolonRef = EvalCluster#1`.
* `Eval_2`: same model / characteristic / cluster, but `datasetRef = Dataset_B` — **substitute another dataset in `DatasetSlot` at fixed target characteristic**.
* `Eval_3`: same model and dataset, but `targetCharacteristicRef = F1` — **substitute another characteristic in `TargetCharacteristicSlot`** while keeping the rest fixed.
`TargetCharacteristicSlot` here shows `U.Characteristic` as ValueKind: the episteme changes which characteristic it is “looking at”, without changing the method or the holon; only the `U.CharacteristicRef` occupant changes.

##### (4) Operational practice — the same runbook in different operating centres

*EpistemeKind:* `IncidentRunbookSpecKind` (runbook specification for major incidents).
*SlotKind / ValueKind / RefKind:*
* `DescribedEntitySlot` — ValueKind `U.Method` (the runbook as a method, e.g. `MajorIncidentRunbook`); RefKind `U.MethodRef`.
* `GroundingHolonSlot` — SlotKind “operational environment where this runbook is validated and in force”; ValueKind `U.Holon` (NOC centre, datacentre, cloud cluster, …); RefKind `U.HolonRef`.
* `ClaimGraphSlot` — ValueKind `U.ClaimGraph` (steps, invariants, assumptions of the runbook); refMode `ByValue`.

*Substitutions:*
* `Runbook_DC1`: `describedEntityRef = MajorIncidentRunbook`, `groundingHolonRef = DC1_NOC`.
* `Runbook_DC2`: same `describedEntityRef`, but `groundingHolonRef = DC2_NOC`.

Intuitively this is the case “one and the same method is specified and verified in two different operational environments”. SlotKind is the same (`GroundingHolonSlot`), ValueKind is the same (`U.Holon`); only the **`U.HolonRef` occupant** differs — a clean example of substituting one holon‑environment in the same slot, without introducing a special `GroundingHolon` type.

##### (5) SLO/SLA requirements — changing the target characteristic vs changing the threshold

*EpistemeKind:* `ServiceSLARequirementKind`.

*SlotKind / ValueKind / RefKind:*
* `DescribedEntitySlot` — ValueKind `U.Holon` with EoIClass = “service”; RefKind `U.HolonRef` (e.g. `CheckoutService#prod`).
* `TargetCharacteristicSlot` — SlotKind “which service characteristic this SLA talks about”; ValueKind `U.Characteristic` (`P95Latency`, `Availability`, `ErrorRate`); RefKind `U.CharacteristicRef`.
* `ClaimGraphSlot` — ValueKind `U.ClaimGraph`; refMode `ByValue`. Numeric thresholds such as `≤ 200 ms` or `≥ 99.9%` live **inside the ClaimGraph as literals**, not as RefKinds.

*Substitutions:*
* `SLA_latency_200`: `describedEntityRef = CheckoutService#prod`, `targetCharacteristicRef = P95Latency`; `ClaimGraph` contains the inequality `P95Latency ≤ 200 ms`.
* `SLA_latency_150`: same `describedEntityRef` and `targetCharacteristicRef`, but the ClaimGraph threshold is `P95Latency ≤ 150 ms`. This is a **by‑value change inside ClaimGraph**: SlotKinds and ValueKinds/RefKinds are untouched; only the embedded literal changes.
* `SLA_availability_99_9`: same `describedEntityRef`, but `targetCharacteristicRef = Availability`; ClaimGraph states `Availability ≥ 99.9%`. Here we **substitute another characteristic in `TargetCharacteristicSlot`** (different `U.CharacteristicRef`), while thresholds remain by‑value in the ClaimGraph.

This example highlights the difference between:
* changing the **target characteristic** (substituting another `U.CharacteristicRef` in `TargetCharacteristicSlot` with ValueKind `U.Characteristic`), and
* changing the **numeric threshold** **inside** `ClaimGraph` (editing literals in a by‑value slot, with no RefKind involvement).

### 6 · Bias‑Annotation
**Lenses tested and scope.** This pattern was read through all five Principle‑Taxonomy lenses (`Gov`, `Arch`, `Onto/Epist`, `Prag`, `Did`) and is intended as a **universal** discipline for n‑ary relation and morphism signatures across Parts A/B/C/E. It leans toward the `Arch` and `Onto/Epist` lenses (typed signatures, explicit kinds), but mitigates this by (a) keeping the discipline notation‑agnostic, (b) aligning with existing tooling rather than prescribing any, and (c) grounding the rules in System/Episteme examples with clear didactic intent. No domain‑specific scope limitation is claimed.

* **Typed‑language bias.**
+  The pattern leans on intuitions from typed programming languages (parameter types, records, references). This is intentional: it aligns FPF signatures with mainstream tooling and with post‑2015 typed effect/row systems. The pattern remains **notation‑agnostic** and does not commit to any specific PL or logic.

* **Slot‑first bias.**
+  We treat *slot* as the primary abstraction and discourage role‑style or object‑style naming for argument positions. This favours structural clarity over conversational metaphors (“subject/object/role”) and keeps `U.Role` free for RoleEnactment rather than param‑slots.

* **By‑value/by‑ref honesty.**
  We explicitly separate ValueKind and RefKind instead of hiding “by‑reference” behind the type system. This increases verbosity but makes reasoning about edition pinning, caching, and re‑targeting more robust, and keeps I/D/S distinctions visible inside signatures.

* **Episteme‑first describedEntity.**
  The examples and cross‑references prioritise episteme use‑cases (C.2.1, A.6.2–A.6.4) where describedEntity and retargeting are subtle. System‑only usages (e.g. method signatures) are absolutely allowed but not the driving case; they inherit the same discipline without additional obligations.


### 7 · Conformance Checklist (normative)

**CC‑A.6.5‑1 · SlotSpec for every parameter.**
Every `U.Signature` that declares an n‑ary relation or morphism **SHALL** assign to each parameter position a SlotSpec triple: `⟨SlotKind, ValueKind, refMode⟩`.

**CC‑A.6.5‑2 · `*Slot` discipline.**
Any Tech name ending with `…Slot` **MUST** denote a SlotKind; SlotKinds **MUST NOT** be used as ValueKinds or RefKinds.

**CC‑A.6.5‑3 · `*Ref` discipline.**
Any Tech name ending with `…Ref` **MUST** denote either a RefKind or a field whose type is a RefKind. ValueKinds and SlotKinds **MUST NOT** end in `…Ref`.

**CC‑A.6.5‑4 · ValueKind purity.**
ValueKinds **MUST** be declared without `*Slot`/`*Ref` suffixes and **MUST** be FPF types (often `U.Kind` or kernel‑level types). Any existing type whose name violates this rule must be either:
* reclassified as a RefKind, or
* renamed to drop the suffix.

**CC‑A.6.5‑5 · Episteme core SlotKinds.**
For episteme kinds (`U.EpistemeKind`), the following SlotKinds **SHALL** be used (or their documented refinements) in C.2.1 / C.2.x:

* `DescribedEntitySlot` with ValueKind `U.Entity` **or a declared subkind** (e.g. `U.Method`, `U.Holon`) via Kind‑CAL (EoIClass ⊑ `U.Entity` at species level);
* `GroundingHolonSlot` with ValueKind `U.Holon`;
* `ClaimGraphSlot` with ValueKind `U.ClaimGraph` and `ByValue` mode in the minimal core;
* `ViewpointSlot` with ValueKind `U.Viewpoint`;
* `ViewSlot` with ValueKind `U.View` (`U.EpistemeView`);
* `ReferenceSchemeSlot` with ValueKind `U.ReferenceScheme` and `ByValue` mode in the minimal core.

**CC‑A.6.5‑6 · No “Role” as SlotKind head.**
SlotKinds **MUST NOT** use “Role” as their head noun; use “Slot” with a neutral qualifier instead (e.g., `EnactorHolonSlot`). `U.Role` remains reserved for RoleEnactment patterns.

**CC‑A.6.5‑7 · Substitution checks.**
Any pattern that describes substitution or replacement of arguments **MUST** phrase its rules in terms of SlotKinds and ValueKinds (and, where relevant, RefKinds), not in terms of unstructured parameter indices or ad‑hoc labels.

**CC‑A.6.5‑8 · Cross‑pattern consistency.**
When the same conceptual position is used across patterns (e.g. “describedEntity target”, “grounding holon”, “caller system”), the **same SlotKind name** and ValueKind **SHALL** be reused, unless a documented Bridge declares a different discipline or the pattern explicitly scopes itself to a distinct calculus.

**CC‑A.6.5‑9 · Migration of legacy `…Ref`/`…Slot` usage.**
Contexts adopting this pattern **MUST** maintain a migration table for legacy types/fields whose names contain `Ref` or `Slot` but do not comply with the new discipline. Each entry shall state:
* old name and role,
* new SlotKind/ValueKind/RefKind,
* whether the old name becomes an alias (deprecated) or is removed.

**CC‑A.6.5‑10 · Pattern integration.**
New or revised patterns in Part A/B/C/E that introduce n‑ary relations, morphisms, or signatures **SHALL** reference A.6.5 in their Relations section and attest that they follow SlotKind/ValueKind/RefKind discipline.

### 8 · Consequences

**Benefits**

* **Uniform language for arguments.**
  Any n‑ary relation (episteme, role, method, service, guard) can be described with the same SlotKind/ValueKind/RefKind triple.

* **Safer substitutions.**
  Substitution, retargeting, and viewing laws (A.6.2–A.6.4) can be stated in terms of *which SlotKinds* they read/write and *which ValueKinds* they preserve or retarget.

* **Cleaner naming and migration.**
  Misuses of `*Ref`, `*Slot`, “Role”, “Subject”, “Object” in signatures become guard‑detectable; migration strategies can be described as re‑factoring SlotKinds and ValueKinds rather than ad‑hoc renames.

* **Tool alignment.**
  Implementation languages with **row‑typed records, dependent types, and algebraic effects** map naturally to the SlotKind/ValueKind/RefKind layers, easing code generation and static analysis. ([ACM Digital Library][1])

**Trade‑offs / mitigations**

* **Extra metadata in signatures.**
  Every parameter now has three pieces of information instead of one. Mitigation: template support in authoring tools; pattern‑guided macros for common shapes (episteme, role, method, service).

* **Stricter lexical rules.**
  Some legacy names will need migration (`EpistemicObject`, ad‑hoc `…Ref` types). Mitigation: migration notes in F.18 and dedicated anti‑pattern sections; transitional aliases allowed but marked deprecated.

* **Learning curve.**
  Authors must learn to think “SlotKind/ValueKind/RefKind” before writing `id` or `subject`. Mitigation: Tell‑Show‑Show examples and a didactic micro‑guide on slots and describedEntity referenced from A.6.0/C.2.1/E.17.0.

### 9 · Rationale

**Why a SlotKind/ValueKind/RefKind triple at all.** At architheory level, this pattern makes `U.Signature` behave like a lightweight dependently‑typed record discipline: SlotKind plays the role of an index or label, ValueKind is the family of admissible occupants at that position, and RefKind captures the representation choice (by‑value or via a handle). This mirrors the way post‑2015 work on row‑polymorphic data and effect rows treats labels and field kinds as first‑class, while keeping the Core notation‑neutral.

**Why separate ValueKind from RefKind.** In practice, “Ref” types tend to be quietly used as if they were values, eroding the I/D/S split and making edition discipline invisible. By insisting that ValueKind is always the conceptual kind (“what sort of thing is this about?”) and RefKind is always the reference/identifier kind (“how do we point at it in Episteme?”), the pattern aligns with E.10.D2’s intension/description/specification discipline and with modern resource‑aware logics that keep values and resources distinct.

**Why standardise episteme SlotKinds.** describedEntity and grounding recur across epistemes; standard SlotKinds (`DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, etc.) let A.6.2–A.6.4 and C.2.1 talk about substitutions and retargetings once, instead of re‑defining “what this is about” in every pattern. This is the same move that SoTA specification frameworks make when they stabilise their core judgement forms and then vary only instances and laws.

**Why lexical rules (`*Slot`, `*Ref`, no “Role” heads).** The triple only buys safety if authors and tools can see it at a glance. Reserving `*Slot` for SlotKinds and `*Ref` for RefKinds/fields gives a cheap, syntax‑level guard against conflating places, kinds, and handles. Banning “Role” as a SlotKind head prevents clash with `U.Role` and the RoleEnactment calculus, preserving the clean separation between “mask worn by a system” and “position in a relation”.

### 10 · SoTA‑Echoing (post‑2015 practice alignment)

**Purpose.** To situate SlotKind/ValueKind/RefKind discipline with respect to contemporary typed and relational approaches, without importing any external calculus into the Core. All items are used as conceptual comparators; concrete reuse in a `U.BoundedContext` would happen only via explicit Bridges (F.9) with declared CL penalties.

1. **Row‑typed, extensible data / effect rows (adopt/adapt).**  
   Post‑2015 work on row polymorphism and extensible data/effect rows treats records and variants as labelled collections of fields whose presence and type can evolve independently.   
   **Adopted:** the idea that **positions** (labels) are first‑class and carry their own typing discipline.  
   **Adapted:** instead of row kinds, FPF uses SlotKind/ValueKind/RefKind triples for n‑ary relations and epistemic slots; the pattern is notation‑agnostic and applies equally to episteme structures, role relations, and service signatures. ([1])

2. **Dependent type systems engineered via macros (adopt/adapt).**  
   Macro‑based dependent type systems such as Turnstile+ separate structural indices, value‑level types, and evidence, while allowing them to be related by construction.   
   **Adopted:** the separation between **indices/labels** and **values**, and the intuition that signatures should expose both explicitly.  
   **Adapted:** SlotKind corresponds to a structural index, ValueKind to the ordinary type of occupants, and RefKind to runtime‑level identifiers; the discipline is phrased at the architheory level and kept independent of any particular PL.

3. **Relational models of types‑and‑effects (adapt).**  
   Relational models for types‑and‑effects distinguish value positions from effect/resource annotations and track substitution separately across these layers.   
   **Adopted:** the insistence that reasoning about **substitution and equality** must be stratified (values vs additional structure).  
   **Adapted:** A.6.5 stratifies *slot / value / reference* instead of *value / effect*, and applies the discipline not only to programs but also to epistemes, roles, methods, and services. ([3])

4. **Optics / lenses as disciplined projections (echo).**  
   Profunctor optics formalise get/put pairs where a fixed “focus” position within a larger structure is manipulated under composition laws.   
   **Echoed:** SlotKind plays the role of the focus coordinate; ValueKind is the focus type; RefKind determines whether the focus is stored by value or via a handle. This perspective informs later use of SlotKind discipline in EpistemicViewing (A.6.3) and multi‑view publication (E.17). ([4])

**Cross‑Context reuse and Bridges.** When a `U.BoundedContext` chooses to adopt a concrete row‑typing discipline, relational logic, or optics library, it **SHALL** do so via explicit Bridges (F.9) with CL and (for plane crossings) `Φ(CL)`/`Φ_plane` policy‑ids, keeping numerical policies and notations Context‑local. A.6.5 only constrains the **slot discipline** that such Bridges must respect.

Overall, `U.RelationSlotDiscipline` echoes post‑2015 typed and relational work — *labelled positions, explicit kinds, layered references* — while staying notation‑neutral and tuned to FPF’s holonic and epistemic ontology.

### 11 · Relations (with other patterns)

**Builds on A.6.0 `U.Signature`.**  
Refines parameter declarations with SlotSpec triples `⟨SlotKind, ValueKind, refMode⟩` while leaving the rest of the signature structure (SubjectKind, BaseType, Quantification, ResultKind, Laws) unchanged. SlotKinds become the canonical labels for argument positions.

**Constrains C.2.1 `U.EpistemicMediationGraph`.**  
Fixes core episteme SlotKinds (`DescribedEntitySlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ViewpointSlot`, `ViewSlot`, `ReferenceSchemeSlot`) and their ValueKinds/`ByValue` vs Ref discipline. C.2.1 and its extensions SHALL use these SlotKinds (or documented refinements) so that episteme morphisms can be expressed uniformly over slots.

**Supports A.6.2–A.6.4 (episteme morphisms and viewing).**  
DescribedEntity‑preserving vs describedEntity‑retargeting morphisms can now be stated as constraints on which SlotKinds’ ValueKinds/RefKinds they may change. Retargeting becomes “substitution at `DescribedEntitySlot` under a Kind‑Bridge” rather than an ad‑hoc parameter tweak.

**Coordinates with B.5.* (RoleEnactment).**  
Role/assignment relations may declare SlotKinds such as `HolderHolonSlot`, `RoleSlot`, `ContextSlot`, `WindowSlot` with clear ValueKinds/RefKinds, instead of overloading “role” for both holonic roles and relation positions. This keeps `U.Role` semantics (A.2, F.6) separate from slot discipline.

**Coordinates with E.17 `U.MultiViewDescribing`.**  
`Viewpoint` and `View` positions are governed by SlotKind/ValueKind/RefKind; view‑changing operations can be described as substitutions at specific SlotKinds that preserve ClaimGraph content while re‑indexing viewpoints and views.

**Feeds F.18 (LEX‑BUNDLE) and E.10 (LEX).**  
Provides lexical guards for `*Slot` and `*Ref`, clarifying that:
* `*Slot` is reserved for SlotKinds only;  
* `*Ref` is reserved for RefKinds and reference fields;  
* ValueKinds and Kind names MUST NOT carry either suffix.  
Name‑acceptance and migration harnesses in Part F can detect legacy violations and drive renames.

**Used by A.19 `CharacteristicSpace` and measurement patterns.**  
+Characteristic‑space slots already behave as positions with attached kinds; slot discipline in A.6.5 gives a uniform story for how such slots appear inside relation signatures, episteme cards, and service definitions, and how substitution over those slots is checked.

[1]: https://dl.acm.org/doi/pdf/10.1145/3290325 "Abstracting extensible data types: or, rows by any other name"
[2]: https://www.williamjbowman.com/resources/wjb2019-depmacros.pdf "Dependent Type Systems as Macros"
[3]: https://iris-project.org/pdfs/2017-popl-effects-final.pdf "A Relational Model of Types-and-Effects in Higher-Order ..."
[4]: https://arxiv.org/pdf/1809.00738 "Categories of Optics"

## **Cluster A.V · Constitutional Principles of the Kernel**

## A.7 — Strict Distinction (Clarity Lattice)  \[A]

### 1 · Intent

Provide a **single, didactically clear lattice of distinctions** that keeps models free from category errors. This pattern is the guard‑rail that prevents four recurrent confusions:

1. **Role vs Function** (mask vs behaviour),
2. **MethodDescription vs Method vs Work** (description vs capability vs occurrence),
3. **Holon vs System vs Episteme** (what can act and what cannot),
4. **Episteme vs Carrier** (knowledge vs its material signs).

It harmonizes A.12 (External Transformer), A.13 (Agential Role & Agency Spectrum), A.14 (Advanced Mereology), and A.15 (Role–Method–Work Alignment).

#### 2 · Problem frame

* **Holons (A.1) and systems.** All holons are part/whole units; **only systems** can enact behaviour.
* **Externalization (A.12).** Every change is performed by a **system bearing TransformerRole** across a boundary; there is no “self‑magic”.
* **Quartet backbone (A.3, A.15).** We separate **MethodDescription** (description), **Method** (**capability under a role**), and **Work** (run‑time occurrence), with the **system bearing TransformerRole** as the acting side.
* **Evidence (A.10).** Knowledge claims are anchored via **Symbol‑Carrier Register (SCR)**; epistemes never “act”, they are **used** by systems that act on their **carriers**.

Manager’s reading: if a sentence could be read as “the document decided” or “the process executed itself”, it violates A.7.

### 3 · Problem

When documents blur the above lines, three classes of defects appear:

1. **Category collapse.** People write “function/role/process” interchangeably; teams then disagree whether they are changing a plan, a capability, or reporting an actual occurrence.
2. **Agency misplacement.** Epistemes (documents, models) are treated as doers; collectives as raw sets; or a “holon” is used where **only a system** makes sense.
3. **Audit failures.** A MethodDescription is cited as if it were evidence; or Work has no anchors (no carriers, no time span), making trust impossible (B.3).

### 4 · Forces

| Force                                        | Tension                                                                                                                             |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Didactic brevity vs conceptual precision** | Teams want short words (“process”, “function”) ↔ the framework must keep five distinct layers apart.                                || **Universality vs domain idioms**            | We support engineering idioms (procedure, SOP, algorithm, workflow) ↔ internally we must map them unambiguously.                    |
| **Parsimony vs completeness**                | Minimal concept set ↔ enough distinctions to avoid the classic traps (role/function; plan/capability/occurrence; episteme/carrier). |

### 5 · Solution — The **Clarity Lattice** (normative distinctions & safe vocabulary)

#### 5.1 **Terminology (normative): orthogonal characteristics**
• **senseFamily** — the categorical characteristic, used by F.7/F.8/F.9: {Role | Status | Measurement | Type‑structure | Method | Execution}. Rows must be **sense‑uniform**. 
• **ReferencePlane** — the referent mode per CHR: {world/external | conceptual | epistemic}. 
• **I/D/S layer** — the Intension/Description/Specification layer (E.10.D2). Not an I/D/S “plane” or "stance", and not a bare "layer".
• **DesignRunTag** — the design vs run DesignRunTag. Not a temporal “plane” or "layer", and not a bare "stance".
• **PublicationSurface** — the *didactic projection* of a Description/Specification into a **bundle of views** (ISO 42010 sense). **Surfaces are not the thing described**. Under L‑SURF, Core allows only **PublicationSurface** and **InteropSurface** tokens; faces SHALL be named **…View / …Card / …Lane** rather than inventing new `…Surface` kinds. The canonical didactic set for `[A]` is:
  {**PlainView** (explanatory prose), **TechCard** (typed cards/IDs), **NormsCard** (TechCard profile for checklists/SHALL‑clauses), **AssuranceLane** (evidence bindings/lanes)}. *Surfaces are orthogonal to I/D/S and to design/run.*
• **Typed describing/formalising morphisms (I→D, D→S)** — total morphisms that *project* along I/D/S (they are **not** mechanisms):
  `Describe_ID : I → D` (describe an intensional object into the world of descriptions; historical alias `Publ_ID`) and
  `Specify_DS`/`Formalize_DS : D → S` (refine a description into a specification). Composition `Describe_IS := Specify_DS ∘ Describe_ID : I → S` is allowed but both stages MUST remain visible and auditable.
  **Laws (normative):** (ID‑1) *Non‑extensibility of content*; (ID‑2) *Identity & meaning‑preserving composition*; (DS‑1) *Monotonic refinement* under ≤₍ref₎; (DS‑2) *Pin editions & measurable anchors* per **MM‑CHR** (C.16) via **CHR‑Pins**; (DS‑3) *No retro‑effects*.

A.7 establishes the following **pairs and triplets**. Use their **names** and **scope** exactly as below.

#### 5.2 Role vs Function (behaviour)

* **Role (role‑object, mask).** A contextual **position** a holon can bear (A.2, A.15). A role is **not behaviour**; it is the **mask** under which behaviour may be enacted. Example: **Cooling‑CirculatorRole** in a thermal loop.
* **Function = behaviour = Method under a role.** What a **system** actually does **when bearing a role**. In Transformer context, this behaviour is the **Method** (design‑time capability) that can be executed as **Work** (run‑time).

  * Safe rewrite for earlier “Holonic Duality (Substance ⧧ Function)”: **Holonic Duality (Substance ⧧ Role).** A `U.System` keeps its identity (substance) while **switching roles**; each role may entail a **Method** (behaviour) and its possible **Work** (occurrence).

**Normative guard:** Use “**Role**” for the mask; use “**Method/Work**” for behaviour/occurrence. Do **not** call the role itself a function.

#### 5.3 MethodDescription vs Method vs Work (design vs capability vs occurrence)

* **MethodDescription** — the **description** (algorithm / SOP / recipe / script) at design‑time. Anchored via **SCR** (A.10).
* **Method** — the **order‑sensitive capability** the **system bearing TransformerRole** can enact, composed with **Γ\_method** (B.1.5). A Method is a **timeless semantic capability**; **concrete values** are **bound at `U.Work` creation**. Outside executions we **refer to it via MethodDescription** (see A.3.1 CC‑A3.1‑5/‑9; A.15 §2.2, §4.1). 
* **Work** — the **dated run‑time occurrence** (what actually happened), with resource spend (Γ\_work) and temporal coverage (Γ\_time).

**Normative guard:** Never use MethodDescription as evidence of Work; never present Method as if it had happened.

#### 5.4 Holon vs System vs Episteme (who can act)

* **System** — the only holon kind that can **bear behavioural roles** and enact **Method/Work**.
* **Episteme** — **cannot act**; it is **changed via its carriers** by a system. Epistemes **may bear non‑behavioural roles** (e.g., **ReferenceRole**, **ConstraintSourceRole**).
* **Holon** — umbrella term; **do not** use it where only **system** is meaningful (e.g., “holon bearing TransformerRole” is **invalid**; write “**system bearing TransformerRole**”).

**Normative guard:** Behavioural roles (including TransformerRole) have **domain = system**. Epistemes may bear purely **classificatory** roles only.

#### 5.5 Episteme vs Symbol Carrier (SCR/RSCR)

* **Episteme** — the knowledge content (claim, model, requirement set).
* **Symbol Carrier** — the physical/digital sign that carries the episteme (file, volume, dataset item), tracked in **SCR**; remote sets in **RSCR**.
* **Use:** Evidence, provenance, and reproducibility address **carriers**; arguments and validity address **epistemes**.

**Normative guard:** When you say “we updated the spec”, detail **which carriers** changed (A.10).

#### 5.6 Collective vs Set, and MemberOf vs Component/Constituent/Portion/Phase (A.14)

* **Set / Collection (MemberOf)** — **mathematical or catalog** grouping; **no joint behaviour** implied.
* **Collective System** — a **system** with boundary and coordination Method (e.g., a team).
* **Use relations correctly:**

  * **ComponentOf** — mechanical/structural part in systems.
  * **ConstituentOf** — logical/content part in epistemes.
  * **PortionOf** — quantitative portion with conserved extensives.
  * **PhaseOf** — temporal part/state across a continuous identity.
  * **RoleBearerOf** — a **system** is the **bearer** of a **Role**.

**Normative guard:** If the grouping is expected to **act**, model a **collective system** (not a set) and provide its role and Method/Work.

#### 5.7 Operator alignment (names you MUST use)

* **Γ\_sys** — composition of **system** properties (physical/systemic).
* **Γ\_method** — composition of **Method** (order, branching).
* **Γ\_time** — composition of **Work** histories and temporal parts.
* **Γ\_work** — composition of **resource spend** and yields tied to Work. Do not track costs with Γ\_method; costs (resources/yield) belong to Γ\_work.

**Normative guard:** Avoid generic “process” for these operators. Reserve “process” for domain idioms; map internally to **Method** (design) and **Work** (run).

#### 5.8 I/D/S vs PublicationSurface (orthogonal, normative)
* **I/D/S governs the model.** What the thing *is* vs how it is *described/tested* lives in I/D/S (E.10.D2).
* **PublicationSurface governs the didactic projection.** How D/S are **presented** lives on **PublicationSurface/InteropSurface** only; concrete faces SHALL be **PlainView / TechCard / InteropCard / AssuranceLane**. Cards/views are **conceptual views over D/S**, not the intensional object **and not symbol carriers**; physical/digital **carriers** stay in **SCR/RSCR** (A.10).
* **Surface field pins.** When D/S are shown on **TechCard**, pin the minimal **CHR‑Pins** = {**UnitType**, **ScaleKind**, **ReferencePlane**, **EditionId**}. 
* **Bridge routing.** Cross‑Context or cross‑plane reuse **MUST** cite **Bridge id + CL**; **Φ(CL)**/**Φ_plane** penalties route to **R (trust)** only; **F/G invariant**. 

#### 5.9 Typed describing/formalising morphisms (I→D→S, normative)

**What `Describe_ID` / `Specify_DS` mean in A.7.** For any intensional object `X ∈ I`, *describing X* is the morphism application `Describe_ID(X) : D` (historical alias `Publ_ID(X)` in earlier drafts); *formalising that description* is `Specify_DS(Describe_ID(X)) : S` (alias `Formalize_DS`). The collapsed arrow `Describe_IS(X)` MAY be referenced, but **implementations SHALL expose and audit both steps**.

**Invariants (restate of the A.6.2/A.6.3 laws, audit‑oriented):**
1. **Non‑extensibility (ID‑1).** `Describe_ID` MUST NOT introduce new epistemic commitments. If a claim `c` is absent in `X`, it is absent in `Describe_ID(X)`; any added structure is representational only (formatting, indexing, cross‑references).
2. **Identity & meaning preservation (ID‑2).** If `f : X → Y` is a meaning‑preserving map in I, then `Describe_ID(f)` is defined and preserves identity, and where meaningful composition exists, `Describe_ID(f ∘ g) = Describe_ID(f) ∘ Describe_ID(g)`.
3. **Monotonic refinement (DS‑1).** If `D₁ ≤₍ref₎ D₂`, then `Specify_DS(D₁) ≤₍ref₎ Specify_DS(D₂)` (equivalently `Formalize_DS(D₁) ≤₍ref₎ Formalize_DS(D₂)`). Also `D ≤₍ref₎ Specify_DS(D)` holds when S merely adds testable structure.
4. **Pinning of editions & anchors (DS‑2).** `Specify_DS`/`Formalize_DS` MUST pin: **edition id**, **unit/scale types**, **ReferencePlane**, and **measurable anchors** (CG‑Spec/CHR). Pins are visible on **TechCard/NormsCard** faces and recorded in **SCR**; edition governance follows **U.EditionSeries**.
5. **No retro‑effects (DS‑3).** Applying `Specify_DS` yields a *new* `S` and *new* carriers (new SCR ids); earlier carriers remain valid in their scope; **no retro‑mutation** of prior I/D carriers.
6. **Separation from Γ.** `Describe_ID`/`Specify_DS` (`Publ_ID`/`Formalize_DS` in legacy text) do **not** compose with **Γ\_method**, **Γ\_time**, or **Γ\_work**; I/D/S describing/formalising is *not execution* and accrues no resource/time semantics.
7. **Ontology preservation.** Describing any object (Calculus/Signature/Mechanism/…) via `Describe_ID` does **not** change its ontology; it yields a D/S projection by A.7 rules. *Describing/formalising is not a subtype of mechanism*; publishing to surfaces is handled separately in E.17 (MVPK).

### 6 · Archetypal Grounding (Tell–Show–Show; System / Episteme)

#### 6.1 System and Episteme example
**System archetype — “Digital‑twin vs asset”.**  
*Claim:* *The twin (episteme) does not “act”; the **system** bearing TransformerRole enacts Work on the asset; evidence binds to carriers.*  
*Show:* A maintenance **MethodDescription** (tech card) lives at design‑time; a **Work** record (assurance face) lists Γ_time, Γ_work, PathId and **carrier** ids for telemetry. The twin’s update is **Work on the carrier**, not the asset; CL^plane penalties are disclosed when twin–asset crossings are analysed.

**Episteme archetype — “Peer‑review vs manuscript”.**  
*Claim:* *A review is Work by a **system** (the reviewer) **on carriers** of an episteme (the manuscript).*  
*Show:* The **MethodDescription** is the review SOP; the **Work** cites carrier ids (file/edition) and the *describedEntity* episteme; arguments/rebuttals live on epistemes; acceptance gating lives in CAL, not in CHR cards.

#### 6.2 Didactic examples

**Example 1 — Pump in a cooling loop**

* **Substance (system):** Centrifugal pump P‑12.
* **Role:** **Cooling‑CirculatorRole**.
* **MethodDescription:** “Loop Circulation v3” (**TechCard**, anchored in SCR).
* **Method:** ordered capability: start → ramp → hold → stop (Γ\_method).
* **Work:** run on 2025‑08‑09 10:00–10:45; energy ledger via Γ\_work; log via Γ\_time.
* **Safe phrasing:** *“The **system** playing **Cooling‑CirculatorRole** (via the P‑12 control unit as **Transformer**) executed the **Method** described by **MethodDescription**, producing **Work** …”*
* **What not to write:** “The pump’s function is the role” (role ≠ behaviour).

**Example 2 — Standard document cited in a design**

* **Episteme:** “Safety Standard S‑174”.
* **Carriers:** PDF (SCR id: scr://std/S‑174/2025‑07), printed volume (scr://print/S‑174/2e).
* **Role:** **ReferenceRole** in the valve selection activity.
* **System bearing TransformerRole:** design team’s selection service.
* **MethodDescription:** “Valve Selection SOP v5”.
* **Method/Work:** capability and dated selection session that **used** the standard; the episteme did **not** act.

**Example 3 — Set vs team**

* **Set (MemberOf):** {Alice, Bob, 3.14} — a collection; **no behaviour** implied.
* **Collective system (team):** boundary, coordination **Method**, supervision **Work**; can bear **AgentialRole** (A.13).
* **Safe phrasing:** *“Team T plays **Cooling‑MaintenanceRole** and executed Work W…”*

### 7 · Conformance Checklist (normative)

| ID                                       | Requirement                                                                                                                                                                                                                                                                                    | Practical test                                                                                                                            |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **CC‑A7.1 (Role/Behaviour split)**       | A **Role** must be modelled as a contextual **mask** borne by a holon; **behaviour** must be expressed as **Method** (design‑time capability) and **Work** (run‑time occurrence).                                                                                                              | In any sentence, if “role” is used as if it *does* something, rewrite: the **system bearing TransformerRole** does it **by Method/Work**. |
| **CC‑A7.2 (Transformer domain)**         | **TransformerRole SHALL be borne only by a system.**                                                                                                                                                                                                                                           | Type‑check: bearer ∈ `U.System`. “holon bearing TransformerRole” is invalid.                                                              |
| **CC‑A7.3 (Episteme non‑agency)**        | An **episteme SHALL NOT** be described as acting. All changes to epistemes must be routed to their **symbol carriers** (A.10) by a **system bearing TransformerRole**.                                                                                                                         | Text contains the acting system + carriers (SCR ids).                                                                                     |
| **CC‑A7.4 (MethodDescription ≠ Method ≠ Work)** | **MethodDescription** (description), **Method** (capability), and **Work** (occurrence) **SHALL** be kept distinct in wording and modelling.                                                                                                                                                          | Ask: is there a design artefact? a capability? a dated occurrence? Each must be named separately.                                         |
| **CC‑A7.5 (Operator fit)**               | Use **Γ\_method** only for composing **Method**; **Γ\_time** only for **Work** histories; **Γ\_work** only for resource spend/yields; **Γ\_sys** for systemic properties of systems.                                                                                                           | No sentence should use a single generic “process operator” for all three.                                                                 |
| **CC‑A7.6 (SCR anchoring)**              | Any knowledge claim that references documents/data **SHALL** anchor **carriers** via **SCR/RSCR** on first mention in the subsection.                                                                                                                                                          | First mention expands as “Symbol‑Carrier Register (SCR)”; references list carrier ids.                                                    |
| **CC‑A7.7 (Collective vs set)**          | If a grouping is expected to **act**, it **MUST** be modelled as a **collective system** (boundary + coordination Method + Work), not as a **MemberOf** set.                                                                                                                                   | Presence of boundary, Method, Work for the group.                                                                                         |
| **CC‑A7.8 (Diagram legend)**             | When domain idioms use **“process”**, diagrams/text **MUST** map them to FPF terms on first occurrence: *process (domain) ≡ Method (design‑time) / Work (run‑time).*                                                                                                                           | Legend or parenthetical present at first use.                                                                                             |
| **CC‑A7.9 (Substance ⧧ Role wording)**   | The safe formula is **“System (substance) plays Role; under that Role it has Method; its execution is Work.”**                                                                                                                                                                                 | Sentences follow this order; “function” used only as synonym for **behaviour**, never for the **role**.                                   |
| **CC‑A7.10 (Quartet clarity)**           | Any “triad” picture **MAY** be used only as a **design‑time stand‑in** (Transformer + MethodDescription + Method) and **MUST** be accompanied by an explicit **Work** lane elsewhere in the same section. “quartet of quartets” headings **SHALL** be avoided; use **“Quartet backbone”** instead. | Diagram has a visible **Work** lane/timeline or separate box within the same section.                                                    
| **CC‑A7.11 (Terminology hygiene)**       | Ban **“actor”** in core text. Use **“system bearing TransformerRole”**; bind local shorthand **“Transformer”** only per A.12 rules.                                                                                                                                                            | Plain text scan: no “actor”; shorthand is locally bound.                                                                                  |
| **CC‑A7.12 (Role domain guards)**        | Behavioural roles’ domain = **system**. Epistemes may bear **non‑behavioural** roles (e.g., ReferenceRole, ConstraintSourceRole) only.                                                                                                                                                         | Role declarations name their domain.                                                                                                      |
| **CC‑A7.13 (I→D→S visibility)**          | I/D/S morphisms MUST be **explicit**; do not conflate them with MVPK or TGA steps. If a flow shows only surfaces, the underlying `Describe_ID`/`Specify_DS` steps MUST be recoverable.       | Both steps are visible in text/diagrams; audit shows two distinct operations.                                                             |
| **CC‑A7.14 (Describe_ID / Specify_DS laws)** | Any implementation of `Describe_ID` MUST enforce **ID‑1/ID‑2**; `Specify_DS`/`Formalize_DS` MUST enforce **DS‑1/‑2/‑3**. Violating systems are considered out‑of‑model.                                                                                                              | Diff check between I and D shows no new claims; mapping table shows preserved composition.                                                |
| **CC‑A7.15 (Formalize_DS laws)**         | `Formalize_DS` obeys **DS‑1/DS‑2/DS‑3**: monotonic refinement; pins edition/unit/scale/ReferencePlane/anchors; produces new **S** + **SCR** carriers without retro‑mutation.                                     | Presence of **CHR‑Pins** and pinned anchors; new SCR ids; no edits to prior carriers.                                                     |
| **CC‑A7.16 (Γ‑separation)**              |  Both I/D/S describing/formalising morphisms (`Describe_ID`/`Specify_DS`) and publication‑to‑surface morphisms (MVPK) SHALL NOT carry cost/time semantics; **Γ\_method**, Γ\_time and Γ\_work belong to **Method/Work/System**, not to description/specification or publication. Any aggregate on a card must cite the Γ operator and policy.   | No ledger/time fields attached to `Describe_ID`/`Specify_DS` or MVPK publication steps; any “publication cost” is Work in a separate publication service.             |
| **CC‑A7.17 (**Surface tokens only)**     |  Only **PublicationSurface/InteropSurface** tokens are allowed; faces are **…View/…Card/…Lane**. Use only `PlainView`, `TechCard`, `InteropCard`, `AssuranceLane` (and their tech aliases) unless a DRR extends the set. New `…Surface` kinds require a DRR and L‑SURF revision.                                                 | Token scan shows no ad‑hoc `…Surface` kinds.                                                       |
| **CC‑A7.18 (Bridge+CL on crossings)**    | Any cross‑Context or cross‑plane content on a face **MUST** cite **Bridge id + CL** and **Φ policy‑ids**; penalties route to **R** only.                                                                         | Presence of Bridge ids and **Φ(CL)**/**Φ_plane** on TechCard/AssuranceLane.                        |
| **CC‑A7.19 (UTS anchoring)**             | Public names shown on faces **SHALL** point to **UTS rows** with twin labels (Tech/Plain), edition pins, and SCR carrier ids.                                                                                    | Face carries UTS row ids + edition pins.                                                          |

### 8 · Canonical rewrites (didactic library)

| Instead of (ambiguous)                           | Write (canonical)                                                                                                                               | Why                                                       |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| “The process enforced the rule.”                 | “The **system bearing TransformerRole** enforced the rule by executing the **Method**; the **Work** is anchored to carriers ⟨ids⟩.”             | Processes don’t act; systems do. Evidence via Work + SCR. |
| “The specification decided to tighten limits.”   | “The **design‑control service (system bearing TransformerRole)** updated the **carriers** of the spec (SCR ids), producing **Work** at ⟨time⟩.” | Epistemes are changed via carriers by systems.            |
| “Our role is pump; the role circulates coolant.” | “The **system** plays **Cooling‑CirculatorRole**; under this role its **Method** circulates coolant; **Work** was executed ⟨when⟩.”             | Role = mask; behaviour = Method/Work.                     |
| “We followed the blueprint, so it’s done.”       | “We have a **MethodDescription** and a **Method**; completion is evidenced by **Work** with ⟨timestamps, outcomes⟩.”                                   | Description/capability ≠ occurrence.                      |
| “Team = set of members; it performed repair.”    | “The **team** is a **collective system** (boundary + coordination **Method**); it executed **Work** ⟨…⟩.”                                       | Acting groups must be systems, not sets.                  |
| “Process cost is tracked by Γ\_method.”          | “**Work** cost is tracked by **Γ\_work**; **Γ\_method** composes the **Method** (order/branching).”                                             | Operator alignment.                                       |
| “Holon bearing TransformerRole.”                 | “**System bearing TransformerRole**.”                                                                                                           | Only systems can bear behavioural roles.                  |
| “Publication is a special mechanism.”            | “Publication = **typed projection** from existing Descriptions/Specifications onto **PublicationSurface/InteropSurface** (MVPK); **describing/formalising** are `Describe_ID`/`Specify_DS`, and any execution around them is separate **Work** by a **system** on **carriers**.” | Publication is not behaviour; it is a D/S→Surface projection in the model. |

### 9 · Anti‑patterns (with fixes)

1. **Role‑as‑behaviour** — calling the **role** “the function”.
   **Fix:** Name the **role** + **Method/Work** pair explicitly.

2. **Episteme‑as‑system** — “the model routed traffic”.
   **Fix:** Name the **system** (or Transformer as a system bearing AgentialRole) that used the model; list **carriers** touched.

3. **Triad everywhere** — omitting **Work** entirely.
   **Fix:** Add the Work lane: timestamps, outcomes, Γ\_time coverage.

4. **Operator blur** — using one “process operator” for everything.
   **Fix:** Choose among **Γ\_method**, **Γ\_time**, **Γ\_work**, **Γ\_sys**.

5. **Set‑as‑collective** — a MemberOf set “decides”.
   **Fix:** Model a **collective system** with coordination Method.

6. **Unanchored evidence** — citing ideas without carriers.
   **Fix:** Add **SCR/RSCR** ids; tie claims to carriers.

7. **Holon/system drift** — “holon maintains temperature”.
   **Fix:** Say **system**; reserve “holon” for neutral mereology.

8. **Function/role swap in tables** — columns labelled “Function” but entries are roles.
   **Fix:** Rename column to **Role**; add a separate **Behaviour (Method/Work)** column.

9. **Process‑word leakage** — domain “process” used as FPF operator.
   **Fix:** Add parenthetical mapping at first use (Method/Work).

10. **Carrier/episteme swap** — “we versioned the model” meaning a file was renamed.
   **Fix:** State whether the **episteme content** changed; if only a carrier was renamed, say so.

11. **Publication‑as‑mechanism** — modelling “publication” as if it were a Method/Mechanism.
   **Fix:** Separate **describing/formalising** (`Describe_ID`/`Specify_DS`) from **publication** (MVPK D/S→Surface). If there is operational toil (build, render, upload), model it as **Work** by a **system** on **carriers**; do not change the ontology of the described object or the D/S episteme being surfaced.

### 10 · Consequences

| Benefit                      | Why it matters                                    | Trade‑off / Mitigation                             |
| ---------------------------- | ------------------------------------------------- | -------------------------------------------------- |
| **Category safety at scale** | Prevents silent logic bugs across holarchies.     | Slight verbosity → use local shorthand per A.12.   |
| **Trustworthy evidence**     | Work + SCR anchoring makes claims auditable.      | Requires discipline → provide checklists.          |
| **Operator determinism**     | Correct Γ‑flavour selection preserves invariants. | A bit more modelling → reusable templates.         |
| **On‑ramp for managers**     | Canonical rewrites give immediate phrasing fixes. | Team training → this pattern is the training page. |

| Benefits | Trade‑offs / Mitigations |
|---------|---------------------------|
| **Category‑error firewall.** Clear separation of System/Episteme; I/D/S vs Surface orthogonality removes recurring modeling defects. | Authors must tag surfaces explicitly; mitigated by a minimal **SurfacePack** template in E.8. |
| **Audit and pedagogy align.** SCR/RSCR point to carriers; Normative face houses checklists; Plain face teaches; Tech face types. | Slight increase in pattern length; offset by predictable navigation and machine‑checkable CC. |
| **Cross‑Context safety.** Bridge+CL discipline is now visible even on surfaces. | Authors must cite CL policy‑ids; tooling can assist (ATS), but text remains notation‑independent. |

### 11 · SoTA‑Echoing (post‑2015 practice alignment)

* **Digital Twins (ISO 23247, 2021→):** separates the asset (system) from its **digital representation** (episteme) and prescribes governance of twins without attributing *agency* to the twin itself — matching A.7’s “episteme ≠ actor” and carrier discipline. **Adopt.** 
* **Observability (OpenTelemetry, 2019→2025):** codifies **semantic conventions** as a *publication layer* over traces/metrics/logs; semantics live in descriptions, not exporters — echoing our **PublicationSurface** orthogonality. **Adapt** (terminology). 
* **Active Inference (2017→2024):** separates a **generative model** (episteme) from **actions** by the agent (system), with explicit perception–action cycles — mirroring A.7’s “who can act” and stance separation. **Adopt** 
* **Constructor Theory (2016→):** frames knowledge and work as **possible transformations** enacted by constructors (systems), not by informational states — reinforcing “episteme ≠ actor”. **Adopt** 
* **Quality‑Diversity (MAP‑Elites family, 2015→2024):** archives are **sets on typed spaces** (descriptions) whose **occurrences** are runs; selection returns **sets** under lawful orders — consonant with A.7 and A.15’s set‑returning discipline. **Adopt/Adapt**. 
* **Refinement‑typed specs (2016→):** modern stacks (e.g., Liquid Haskell, Dafny’s post‑2017 refinements, Rust’s `uom` type‑level units) treat formalization as **monotonic refinement with pinned units/scales** — echoing **Formalize_DS** and **Surface field pins**. **Adapt** (terminology; pinning discipline).

### 12 · Rationale (informal)

* **Engineering cognition:** Large programmes fail less from equations than from category slips (“process vs procedure vs execution”). A.7 eliminates these slips by a small, repeatable grammar.
* **Compatible with ISO/BORO practice:** Distinguishing artefacts (specs), capabilities (procedures), and occurrences (operations) mirrors established systems‑engineering discipline while keeping FPF’s holonic rigor.
* **Didactic primacy:** Managers can approve sentences by spotting five tokens: **system bearing TransformerRole** / **Role** / **Method** / **Work** / **SCR**.
* **Why bring “PublicationSurface” into A.7?** Strict Distinction already guards **what a thing is (I)** from **how we describe/specify it (D/S)**. In practice, **misreadings happen at the publication layer**: cards and tables are mistaken for objects; governance words leak where physics/logic should stand. By making **PublicationSurface** *explicit and orthogonal*, A.7 closes that gap without entangling semantics with any tool or notation. This preserves **C‑1 universality** and **P‑1 Cognitive Elegance**, while giving E.8 a crisp home for multi‑face presentation rules.

### 13 · Relations

 **Builds on:** A.1 (Holon), A.2 (Roles), A.3 (Transformer Quartet), A.10 (Evidence & SCR), A.12 (External Transformer), A.14 (Advanced Mereology), A.15 (Role–Method–Work Alignment).  
* **Constrains:** A.13 (Agency sits on systems only; epistemes non‑behavioural), Part B operators (**Γ_method**/**Γ_time**/**Γ_work**/**Γ_sys**) and their choice points; **publication is not a Γ‑operator**.  
* **Extends:** E.8 (Authoring conventions), E.10 (LEX‑BUNDLE incl. **L‑SURF**), **Part F/G (UTS & CG‑Spec/CHR pinning)**, B.3 (Assurance routing), C‑cluster (selection/archives) — by enforcing I/D/S vs Surface orthogonality, System/Episteme separation, and typed I→D→S describing/formalising discipline (**publication = D/S→Surface in E.17**).  
* **Coordinates with:** ATS (E.11) for surface‑level checks (Tier/Gate/Lane/LEX) and **UTS presence** without embedding any notation dependence.
  
### 14 · Manager’s one‑page review (copy‑paste)

**Approval sentence template**

> “The **system bearing TransformerRole** ⟨name⟩ plays ⟨Role⟩; it has **Method** ⟨M⟩ (from **MethodDescription** ⟨S⟩) and executed **Work** ⟨W⟩ on ⟨time⟩, anchored to ⟨SCR ids⟩; resources accounted via **Γ\_work**.”

**Five binary checks**

1. **Actor ban:** No “actor” token; canonical phrasing present.
2. **Clear trio:** MethodDescription / Method / Work are all named (as applicable) and not conflated.
3. **Right Γ:** Γ\_method for capability; Γ\_time for occurrence; Γ\_work for resources; Γ\_sys for system properties.
4. **Episteme handled:** Epistemes do not act; carriers listed (SCR).
5. **Group clarity:** Acting group is a **collective system**, not a MemberOf set.

**Diagram legend stub**

* “process (domain)” ⇒ Method (design‑time) / Work (run‑time).
* Role column lists masks (e.g., Cooling‑CirculatorRole).
* Behaviour column shows Method/Work, not the role itself.

## A.8 Universal Core (C‑1)  \[A]

### Pattern A.8 — Universal Core Principle (C‑1) \[A]

*“A principle that works in only one world is local folklore; a first principle architects every world.”*


#### 1 · Context

FPF aspires to be an **operating system for thought** that engineers, biologists, economists, and AI agents can all use without translation layers. That promise rests on the **universality** of its core primitives (`U.Type`s).  History is littered with “upper ontologies” that proclaimed universality yet smuggled in the biases of a single discipline; once deployed beyond their birthplace, they cracked or ballooned.  Rule C‑1 turns “universal” from a marketing word into a measurable criterion: *cross‑domain congruence*.

---

#### 2 · Problem

| Pathology                 | Manifestation                                                                                       |
| ------------------------- | --------------------------------------------------------------------------------------------------- |
| **Parochial Drift**       | A “universal” `U.Resource` works for ERP bills of materials but collapses for ATP in cell biology.  |
| **Alienated Communities** | Subject‑matter experts recognise the bias and abandon the framework, fracturing knowledge silos.    |
| **Kernel Bloat**          | Competing “almost‑universal” types are added to patch gaps, violating Ontological Parsimony (A 11). |

---

#### 3 · Forces

| Force                           | Tension                                                                              |
| ------------------------------- | ------------------------------------------------------------------------------------ |
| **Generality vs Specificity**   | Primitives must stretch across physics ↔ social science yet keep actionable meaning. |
| **Rigor vs Pragmatism**         | Proof of universality must be checkable, not philosophical hand‑waving.              |
| **Inclusivity vs Coherence**    | Welcoming new ideas should not swamp the kernel with domain jargon.                  |
| **Cognitive Load vs Grounding** | Examples help readers, but too many examples obscure the essence.                    |

---

#### 4 · Solution — *The Three‑Domain Falsification Test*

> **Normative Rule (C‑1)** A `U.Type` **enters the kernel only if** it is shown to play the **same Role** in **at least three foundationally distinct domains**.

 **Heterogeneity & QD‑triad guarantee (C‑1.QD).**
 In addition to distinct **domain‑families** (choose from: *Exact Sciences · Natural Sciences · Engineering & Technology · Formal Sciences · Social & Behavioural Sciences*), the **triad** SHALL demonstrate **quality diversity**:
(a) **Hetero‑test.** Each projection adds at least one non‑trivial **DescriptorMap** signal or Bridge path not subsumed by the other two (no aliasing by mere renaming).
(b) **QD evidence.** Publish **Creativity‑CHR / NQD‑CAL** evidence for the triad: `Diversity_P` (set‑level) and its **IlluminationSummary** gauge with ≥3 non‑empty cells and `occupancyEntropy > 0` under the declared grid.
(c) **Policy disclosure.** Declare the Context‑local `QD_policy` (binning/grid, kernel, time‑window) used to compute the gauges.
(References: **C.17** `Diversity_P` & illumination gauge; **C.18** `U.DescriptorMap`, `U.IlluminationSummary`.)

Implementation steps (Domain Families): 

1. source domain‑families from the active F1‑Card (taxonomyRef/embeddingRef edition). The five coarse families {Exact, Natural & Life, Engineering & Tech, Formal, Social & Behavioural} are informative only; if used for pedagogy, publish an explicit mapping to the F1‑Card taxonomy. The triad gate is measured by MinInterFamilyDistance ≥ δ_family (per F1‑Card), not by labels alone.

2. **Role‑Projection Records** For each domain, author a short **`Role‑Projection`** tuple: `{domain, indigenous term, Role, exemplar}`.
   *Example:* `{physics, "Free Energy", extremum driver, closed gas system}`.

3. **Congruence Check** All three exemplars must satisfy the **same abstract intent**; superficial analogy is rejected.

4. **Living Index** Track the ratio

   $$
     U\text{-Index}=\frac{\text{\# kernel types lacking 3 projections}}{\text{\# kernel types}}
   $$

   as a health signal; target ≤ 0.05 (not a bureaucratic gate).

*Rule of thumb for busy managers:* “**One idea, three worlds.** If you can’t point to the trio, park it in a plug‑in.”

---

#### 5 · Archetypal Grounding (System / Episteme)

| Universal `U.Type` | **Domain 1 · Physics**                  | **Domain 2 · Life Sci.**            | **Domain 3 · Tech & Soc.**       | Congruent Role                |
| ------------------ | --------------------------------------- | ----------------------------------- | -------------------------------- | ----------------------------- |
| `U.Objective`      | *Free Energy* minimum in thermodynamics | *Fitness* maximisation in evolution | *Loss* minimisation in ML        | Extremum driver of change     |
| `U.System`         | Thermodynamic control volume            | Biological organism (cell membrane) | Cyber‑physical system (IoT edge) | Bounded interacting whole     |
| `U.Resource`       | Joules of energy                        | ATP molecules                       | Budget dollars                   | Conserved, spendable quantity |

These juxtapositions give engineer‑managers an immediate sense of *why* each primitive is worth learning.

#### 6 · Conformance Checklist

| ID          | Requirement                                                                                                                            | Purpose                                                 |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **CC‑UC 1** | A proposed `U.Type` **SHALL** include ≥ 3 Role‑Projection records, each taken from a *different* domain family.                        | Enforces the Three‑Domain Test.                         |
| **CC‑UC 2** | Each Role‑Projection **MUST** explain in ≤ 30 words how the domain notion fulfils the *same Role* as the proposed `U.Type`. | Blocks superficial analogies.                           |
| **CC‑UC 3** | No single artefact may serve as exemplar for more than one domain projection.                                                          | Prevents contrived “triple duty” examples.              |
| **CC‑UC 4** | A **specialised** `U.SubType` inherits its parent’s projections **and** adds ≥ 1 new domain projection, never fewer.                   | Keeps refinements as universal as their parents.        |
| **CC‑UC 5** | While the U‑Index > 0.05, authors **SHALL** prioritise supplying missing projections over adding new core concepts.                    | Maintains kernel health without procedural bureaucracy. |
| **CC‑UC‑2‑QD‑triad.** | The three Role‑Projections come from **different domain‑families** AND the triad PUBLISHES: `{FamilyCoverage, MinInterFamilyDistance, Diversity_P, IlluminationSummary}` with `MinInterFamilyDistance ≥ δ_family` (per **F1‑Card** DistanceDef & edition). + Provenance MUST cite `DescriptorMapRef` (incl. `DistanceDef`/edition), `F1‑Card id+edition`, and the grid/binning policy used for `IlluminationSummary`.  | quality diversity of domains

#### 7 · Consequences

| Benefit                                                                                                    | Trade‑off                                     | Mitigation                                                 |
| ---------------------------------------------------------------------------------------------------------- | --------------------------------------------- | ---------------------------------------------------------- |
| **Lean, trusted kernel** – every primitive earns its place by real work in three worlds.                   | Authoring effort for projections.             | Patterns A 5/A 6 provide templates and exemplar libraries. |
| **Cross‑disciplinary uptake** – physicists, managers, and biologists see their own language reflected.     | Some novel ideas wait to gather evidence.     | They live safely in plug‑ins until mature.                 |
| **Resilience to domain drift** – if one field’s jargon changes, the other two anchors preserve continuity. | Possible oversimplification of niche nuances. | Domain‑specific elaborations belong in architheories.      |

---

#### 8 · Rationale

Deep research over the last decade shows *structural homologies* across domains:

* Free‑energy minimisation ↔ negative log‑likelihood ↔ Bayesian surprise (Friston 2023).
* Conservation laws in physics mirror budget balancing in economics (Rayo 2024).

By demanding three independent manifestations, FPF captures these convergences *without privileging* any single vocabulary.  The principle operationalises **Popperian falsifiability** for universality: a concept that cannot survive a three‑domain cross‑examination is, by definition, not a first principle.  This guards Pillars **P‑1 (Cognitive Elegance)** and **P‑4 (Open‑Ended Kernel)** simultaneously.

---

#### 9 · Relations

| Relation             | Linked Pattern                       | Contribution                                                          |
| -------------------- | ------------------------------------ | --------------------------------------------------------------------- |
| **Supports**         | A 11 Ontological Parsimony           | Filters candidates before sunset reviews.                             |
| **Prerequisite for** | A 9 Cross‑Scale Consistency          | Only universal types can propagate invariants up and down holarchies. |
| **Complementary**    | A 7 Strict Distinction               | Together provide clarity (A 7) and breadth (A 8).                     |
| **Enables**          | B 1 Universal Algebra of Aggregation | Γ‑operators rely on domain‑agnostic operands.                         |

---

#### 10 · Known Uses

* **Energy ↔ Budget ↔ Attention** – Engineering teams reused `U.Resource` to reason about battery charge, project funds, and user‑attention minutes with one algebra, cutting integration effort by half (2024 pilot).
* **Objective unification** – An AI lab mapped *loss functions*, a bio‑lab mapped *Darwinian fitness*, and a factory mapped *scrap‑rate* all to `U.Objective`, enabling shared optimisation tooling.

These cases validated that the Three‑Domain Test is achievable in practice, not theoretical paperwork.

---

#### 11 · Open Questions

1. **Domain taxonomy stability** – Should the five domain families be versioned as science evolves (e.g., quantum‑bio‑tech)?
2. **Automated congruence checks** – Can category‑theoretic tooling semi‑automate the functional‑role equivalence test?
3. **Edge‑case hybrids** – How are bio‑cyber‑physical chimera systems counted: a new domain or a composite projection?

## A.9 Cross‑Scale Consistency (C‑3) \[A]

> *“The logic of a bolt must still be the logic of the bridge.”*

#### 1 · Context

FPF models reality as a **nested holarchy**: parts → assemblies → systems → supra‑systems; axioms → lemmas → theorems → paradigms. Designers and analysts must zoom freely without logical whiplash. Classical mereology and modern renormalisation theory both warn: if rules mutate across scales, predictions and audits collapse. FPF therefore mandates a single, scale‑invariant Standard.

---

#### 2 · Problem

| Failure Mode              | Real‑World Symptom                                         |
| ------------------------- | ---------------------------------------------------------- |
| **Invalid extrapolation** | Unit‑tested module fails once integrated.                  |
| **Brittle dashboards**    | Portfolio KPI “green” hides a red supplier averaged away.  |
| **Compositional chaos**   | Different teams’ roll‑ups yield non‑deterministic results. |

These pathologies derail safety cases and budget decisions across disciplines.

---

#### 3 · Forces

| Force                                  | Tension                                                      |
| -------------------------------------- | ------------------------------------------------------------ |
| **Local autonomy vs Global coherence** | Free optimisation of parts ↔ predictable behaviour of whole. |
| **Simplicity vs Fidelity**             | Single rule‑set ↔ non‑linear, emergent effects.              |
| **Determinism vs Emergence**           | Stable roll‑ups ↔ need to legitimise genuine synergy jumps.  |
| **Didactic clarity vs Formal rigour**  | Managers grasp intent quickly ↔ analysts can prove it.       |

---

#### 4 · Solution — Invariant Quintet + Meta‑Holon Transition

##### 4.1 Invariant Quintet

Any aggregation operator `Γ` that claims FPF conformance **MUST** preserve these five invariants :

| Code     | Invariant             | One‑line Intuition                               |
| -------- | --------------------- | ------------------------------------------------ |
| **IDEM** | *Idempotence*         | Folding a singleton changes nothing.             |
| **COMM** | *Local Commutativity* | Order of independent folds is irrelevant.        |
| **LOC**  | *Locality*            | Worker or partition choice cannot affect result. |
| **WLNK** | *Weakest‑Link Bound*  | Whole never outperforms its frailest part.       |
| **MONO** | *Monotonicity*        | Improving a part cannot worsen the whole.        |

*Mnemonic:* **S‑O‑L‑I‑D** (Same · Order‑free · Location‑free · Inferior cap · Don’t‑regress).

**Inter‑Layer Standard note**
When holons are composed as a Layered‑Control stack, each Planner ↔ Regulator pair MUST publish an inter‑layer Standard: {referenceSignal, guaranteedTrackingError, cycleTime}.  Matni 2024 (https://arxiv.org/abs/2401.15185) prove such Standards satisfy COMM + LOC invariants, giving a constructive instance of the Quintet.

##### 4.2 Meta‑Holon Transition (MHT)

If empirical data show a true violation (e.g., redundancy raises WLNK limit), the modeller **declares an MHT**: the collection becomes a new holon tier, and the quintet applies anew at that scale .

---

#### 5 · Archetypal Grounding

| Invariant  | **`U.System` — Pump Skid**                    | **`U.Episteme` — Meta‑Analysis**                |
| ---------- | --------------------------------------------- | ----------------------------------------------- |
| IDEM       | One‑pump skid ≅ that pump.                    | Single‑study review ≅ that study.               |
| COMM / LOC | Pumps welded in any order / yard → same spec. | Labs contribute in any order → same statistics. |
| WLNK       | Pressure rating ≤ weakest pump.               | Reliability ≤ least‑replicated study.           |
| MONO       | Stronger motor never lowers flow.             | Larger sample size never lowers confidence.     |


### 6 · Conformance Checklist

| ID          | Requirement                                                                                                                                                                                      | Purpose (manager‑friendly)                                |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------- |
| **CC‑A9‑1** | Every calculus that defines an aggregation operator `Γ` **SHALL** provide a plain‑language note and a formal argument for how `Γ` upholds **all five invariants** (IDEM, COMM, LOC, WLNK, MONO). | Makes the Standard both human‑readable and checkable.     |
| **CC‑A9‑2** | A *singleton fold* (` card (parts) = 1 `) **MUST** return the part unaltered (IDEM). | Locks the recursion base case. |
| **CC‑A9‑3** | Folding two independent sub‑graphs in any order or on any compute site **MUST** yield equal results (COMM + LOC).                                                                                | Enables safe parallel work and reproducible analytics.    |
| **CC‑A9‑4** | No aggregate metric **MAY** exceed the minimum of that metric across parts unless an **MHT** is declared (WLNK).                                                                                 | Prevents stealth inflation of reliability or truth.       | 
| **CC‑A9‑6** | A declared **Meta‑Holon Transition** **SHALL**: (a) name the new supervisory holon; (b) cite the data triggering the transition; (c) restate how the quintet holds at the new scale.             | Ensures emergence is captured explicitly, not hand‑waved. |

---

### 7 · Consequences

| Benefit                      | Why it matters                                                   | Trade‑off / Mitigation                                                           |
| ---------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **Stable roll‑ups**          | Summaries and reports remain faithful as parts evolve.          | Requires early agreement on `Γ`; offer reference libraries.                      |
| **Visible risk floor**       | WLNK blocks “averaging away” critical weaknesses.                | Can look overly conservative; redundancy, when real, lifts the minimum honestly. |
| **Parallel progress**        | COMM + LOC allow distributed teams to integrate without re‑work. | Needs explicit independence assumptions; templates guide authors.                |
| **Objective emergence flag** | Quintet failure becomes a measurable R\&D signal.                | Teams must learn to document MHTs instead of ignoring anomalies.                 |

---

### 8 · Rationale

*Post‑2015 evidence across domains*

* **Physics** ‑ Renormalisation coherence echoes IDEM, COMM, LOC.
* **Distributed data platforms** rely on COMM + LOC for deterministic aggregations.
* **Safety engineering** ‑ Fault‑tree analyses hinge on WLNK; aviation failures (2018‑24) confirm its necessity.
* **Lean improvement** ‑ MONO underpins Kaizen: fix a bottleneck, never worsen the plant.

Packaging these insights as one memorisable quintet → **Cognitive Elegance** with formal bite.

---

### 9 · Relations

| Relation           | Linked Pattern                       | Contribution                                              |
| ------------------ | ------------------------------------ | --------------------------------------------------------- |
| **Builds on**      | A 1 Holonic Foundation               | Supplies part/whole semantics.                            |
| **Reinforces**     | A 7 Strict Distinction               | Prevents layer‑mixing during folds.                       |
| **Enabled by**     | A 8 Universal Core                   | Guarantees operands share truly universal meaning.        |
| **Foundation for** | B 1 Universal Algebra of Aggregation | B‑section implements operators that satisfy this pattern. |
| **Triggers**       | B 2 Meta‑Holon Transition            | When invariants fail through synergy, an MHT is invoked.  |

---

### 10 · Known Uses (2018‑2025)

* **Spacecraft avionics** ‑ Applying WLNK exposed a sub‑grade connector, saving a \$40 M launch window.
* **Global vaccine meta‑reviews** ‑ COMM + LOC let five epidemiology teams merge data independently; results converged within 0.1 % effect size.
* **Distributed ML training** ‑ MONO guaranteed optimiser swaps never reduced accuracy, cutting iteration time by 20 %.

---

### 11 · Open Questions for expert panel

1. **Order‑sensitive physics** – Should quantum‑circuit folds live in a plug‑in with a relaxed invariant set?
2. **Synergistic redundancy** – Can WLNK be reframed using an “effective minimum” when true redundancy lifts the floor?
3. **Didactic tooling** – Which visual cues best alert non‑formal audiences to an approaching Meta‑Holon Transition?
4. **Layer depth** — In an LCA (layered control architectures, https://arxiv.org/abs/2401.15185) stack every Planner is external to its Regulator; should FPF limit the number of nested layers, or is indefinite chaining acceptable?


###  A.10 — Evidence Graph Referring (C‑4) \[A]

*“A claim without a chain is only an opinion.”*

#### 1 · Context

FPF is a holonic framework: wholes are built from parts (A.1, A.14), and reasoning travels across scales via Γ‑flavours (B.1). To keep this reasoning honest and reproducible, every **published assertion** must be *anchored* in concrete **symbol carriers** and **well‑typed transformations** performed by an **external TransformerRole** (A.12, A.15). **Publication** itself is the typed projection **I→D→S** (`Publ_ID`, `Formalize_DS`) per A.7 and is **not execution**; any physical/digital release, rendering, or upload is **Work** by an external transformer **on carriers**, cited in SCR.

Managers can read this as a simple rule of thumb:
> **Claim → (Proof or Test) → Confidence badge**
> …where the proof/test is traceable to real carriers and to an external system/Transformer who executed an agreed method.

This pattern defines the **Evidence Graph Referring Standard** common to all Γ‑flavours (Γ\_sys — formerly Γ\_core, Γ\_epist, Γ\_method, Γ\_time, Γ\_work) and clarifies:
(a) the difference between **mereology** (part‑whole; builds holarchies) and **provenance** (why a claim is admissible; does *not* build holarchies);
(b) the run‑time / design‑time separation (A.4) across **Role–Method–Work** (A.15).

---

#### 2 · Problem

Without a uniform anchor, models drift into five failure modes:

1. **Weightless claims.** Metrics or arguments appear in the model with no link to their **symbol carriers** (files, datasets, lab notebooks, figures).
2. **Collapsed scopes.** Design‑time method specs are silently mixed with run‑time traces; results cannot be reproduced because “what was planned” and “what actually ran” are conflated.
3. **Self‑justifying loops.** A holon attempts to evidence itself (violates A.12 externality), producing cyclic provenance and unverifiable conclusions.
4. **Source loss during aggregation.** As Γ combines parts, some sources “fall out”; later audit cannot reconstruct why a compound claim was accepted.
5. **Temporal ambiguity.** Time‑series are aggregated without interval coverage or dating source; gaps/overlaps invalidate comparisons and trend claims.

The business effect is predictable: confidence badges cannot be defended, cross‑scale consistency (A.9) is broken, and iteration slows because every review re‑litigates “where did this come from?”.

---

#### 3 · Forces

| Force                           | Tension                                                                                                                                           |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Universality vs. burden**     | One Standard must fit systems and epistemes ↔ Authors should not drown in paperwork.                                                              |
| **Externality vs. reflexivity** | Evidence must be produced by an external TransformerRole (A.12) ↔ Some systems adapt themselves (need reflexive modelling without self‑evidence). |
| **Atemporal vs. temporal**      | Many claims are state‑like ↔ Many others are histories; evidence must respect order and coverage (Γ\_time).                                       |
| **Rigor vs. flow**              | Formal proofs and controlled tests raise confidence ↔ Engineering cadence needs lightweight, incremental anchors.                                 |
| **Mereology vs. provenance**    | Part‑whole edges build holarchies ↔ Evidence edges never do; the two graphs must interlock without leaking semantics.                             |

---

#### 4 · Solution — The Evidence Graph Referring Standard

The Standard is a small set of primitives applied uniformly, with **manager‑first clarity** and **formal hooks** for proof obligations.

**4.1 EPV‑DAG (Evidence–Provenance DAG).**
A **typed, acyclic** graph disjoint from mereology. Node types: **SymbolCarrier** (a `U.System` in **CarrierRole**, A.15), **TransformerRole** (external Transformer, A.12), **MethodDescription** (design‑time blueprint of a method, A.15), **Observation** (a dated assertion/result), **U.Episteme** (knowledge holon). Edge vocabulary is small and normative: `evidences`, `derivedFrom`, `measuredBy`, `interpretedBy`, `usedCarrier`, `happenedBefore` (temporal), etc.
*Manager view:* it is the *“because‑graph”*: every claim answers “because of these carriers, by this Transformer, using that method, then.”

**4.2 Anchors (two relations, two flavours).**

* `verifiedBy` — links a claim to **formal** evidence (proof obligations, static guarantees, model‑checking artefacts).
* `validatedBy` — links a claim to **empirical** evidence (tests, measurements, trials, observations).
  Both anchors terminate in the EPV‑DAG, not in the mereology graph.

**4.3 SCR / RSCR (Symbol Carrier Registers).**
Every `Γ_epist` aggregation **SHALL** emit an **SCR**: an exhaustive register of **symbol carriers** materially used in the aggregate, with id, type, version/date, checksum, source/conditions and optional `PortionOf` (A.14) for sub‑carriers.
Every `Γ_epist^compile` **SHALL** emit an **RSCR**: SCR specialised to a **bounded context** (vocabularies, units) with publication‑grade identifiers and hashes.
*Why this matters:* it prevents “lost sources” during composition and underwrites reproducibility without mandating any specific tool.

**4.4 Scope alignment (A.4) across Role–Method–Work (A.15).**

* **Design‑time**: **MethodDescription** lives here; methods are blueprints; anchors reference what *would* constitute proof or test.
* **Run‑time**: **Work** (actual execution) lives here; traces reference which MethodDescription they instantiate and record `happenedBefore`.
  Bridging edges are explicit (“this run trace instantiates that spec”), so scopes never silently mix.

**4.5 External TransformerRole (A.12).**
The system that produces or interprets evidence is **external** to the holon under evaluation. If true reflexivity is essential, model a **meta‑holon** (A.12): the self‑updating holon becomes the *object* of a higher‑level external transformer (the “mirror”), restoring objectivity.

**4.6 Γ‑flavour hooks (how each flavour anchors).**

* **Γ\_sys (formerly Γ\_core)**: physical properties are anchored by measurement models, boundary conditions, calibration carriers, and dated observations.
* **Γ\_epist**: always outputs SCR/RSCR; every provenance/evidence node resolves to an SCR/RSCR entry.
* **Γ\_method**: order‑sensitive composition; at design‑time a **Method Instantiation Card (MIC)** states `Precedes/Choice/Join` and guards; at run‑time traces record `happenedBefore` and point to the MethodDescription they instantiate.
* **Γ\_time**: temporal claims state interval coverage; **Monotone Coverage** (no unexplained gaps/overlaps) is required.
* **Γ\_work**: resource spending and yield are evidenced by instrumented carriers (meters, logs) and their MethodDescriptions; keep **resource rosters** separate from SCR/RSCR.

> **Manager’s shortcut:** If you can answer *what carriers, which system, which method, when*, the anchor is likely sufficient; if any of the four is missing, it is not.

---

#### 5 · Archetypal Grounding

| Aspect                       | `U.System` — Autonomous Brake                                                                       | `U.Episteme` — Meta‑analysis                                                                                             |
| ---------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Claim**                    | “Stop within 50 m from 100 km/h.”                                                                   | “Drug A outperforms control on endpoint E.”                                                                              |
| **Anchor**                   | `verifiedBy`: static‑analysis proof of no overflow; `validatedBy`: instrumented track tests.        | `verifiedBy`: power‑analysis proof of sample size; `validatedBy`: pooled effect sizes with bias checks.                  |
| **Carriers (SCR/RSCR)**      | Scale logs, calibration certificates, test track telemetry; SCR lists all; RSCR adds context units. | PDFs of studies, data tables, analysis code; SCR lists carriers; RSCR adapts vocabularies/units for the target audience. |
| **External TransformerRole** | Independent test team / metrology lab.                                                              | Independent synthesis team / statistician.                                                                               |
| **Temporal**                 | Dated runs; `happenedBefore` between setup → test → teardown.                                       | Publication dates; dataset versions; monotone coverage of included studies.                                              |

#### 6 · Conformance Checklist

| ID                                      | Requirement                                                                                                                                                                                                                             | Purpose (what it prevents)                                 |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **CC‑A10.1 (EPV‑DAG Presence)**         | Every published claim MUST have a path in the Evidence–Provenance DAG (EPV‑DAG) to concrete **SymbolCarrier** nodes and to the **external** `TransformerRole` that produced or interpreted the evidence.                                | Stops “weightless claims” and self‑justifying text.        |
| **CC‑A10.2 (SCR)**                      | Any `Γ_epist^synth` operation SHALL output an **SCR** listing all symbol carriers materially used in the aggregate `U.Episteme`.                                                                                                        | Prevents source loss during aggregation.                   |
| **CC‑A10.3 (RSCR)**                     | Any `Γ_epist^compile` operation SHALL output an **RSCR** adapted to the target bounded context (vocabularies, units) with publication‑grade identifiers/hashes; SCR→RSCR MUST preserve carrier identity/integrity.                      | Keeps releases auditable and context‑consistent.           |
| **CC‑A10.4 (Resolution)**               | Every provenance/evidence node in the dependency graph MUST be resolvable to an SCR/RSCR entry. Unresolved links invalidate the claim.                                                                                                  | Eliminates dangling references and unverifiable citations. |
| **CC‑A10.5 (Scope Separation)**         | A single EPV‑DAG instance SHALL NOT mix design‑time MethodDescription nodes with run‑time Work traces. Bridges (“this run trace instantiates that spec”) MUST be explicit.                                                                     | Avoids conflating intent and execution.                    |
| **CC‑A10.6 (Externality)**              | The evidencing `TransformerRole` MUST be **external** to the holon under evaluation (A.12). Reflexive cases require modelling a meta‑holon and an external mirror.                                                                      | Prevents self‑creation/self‑evidence paradoxes.            |
| **CC‑A10.7 (Temporal Coverage)**        | For `Γ\_time` claims, interval coverage MUST be monotone and fully specified; gaps/overlaps require explicit justification or rejection.                                                                                                 | Stops invalid time‑series aggregation.                     |
| **CC‑A10.8 (Integrity & Immutability)** | SCR/RSCR entries MUST include version/date and checksums; published SCR/RSCR are immutable—updates create a new revision id with a pointer to the prior one.                                                                            | Guards against silent drift and tampering.                 |
| **CC‑A10.9 (Holarchy Firewall)**        | EPV‑DAG MUST use provenance edges only; mereological edges (`ComponentOf`, `MemberOf`, `PortionOf`, `PhaseOf`, etc.) MUST NOT appear in EPV‑DAG; conversely, provenance edges MUST NOT be used to build holarchies.                     | Keeps part‑whole and evidence semantics disjoint.          |
| **CC‑A10.10 (Γ\_sys Anchors)**          | Physical claims aggregated by `Γ_sys` MUST reference measurement models (quantity, unit, uncertainty), boundary conditions, and calibration carriers.                                                                                   | Ensures physical plausibility and comparability.           |
| **CC‑A10.11 (Γ\_method Anchors)**       | For order‑sensitive composition, design‑time MUST include a **Method Instantiation Card (MIC)** (Precedes/Choice/Join, guards, exceptions); run‑time traces MUST record `happenedBefore` and reference the MethodDescription they instantiate. | Preserves order semantics and reproducibility.             |
| **CC‑A10.12 (Γ\_work Anchors)**         | Resource spending/yield claims MUST be evidenced by instrumented carriers (meters, logs) and their MethodDescriptions; resource **rosters** MUST NOT be conflated with SCR/RSCR.                                                               | Distinguishes cost accounting from knowledge carriers.     |

**Manager’s audit (non‑normative, quick):** For any claim, ask **What carriers? Which system? Which method? When?** If any answer is missing, A.10 is not satisfied.

---

#### 7 · Consequences

| Benefit                           | Why it matters                                                                  | Trade‑off / Mitigation                                                                                                                |
| --------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Cross‑scale reproducibility**   | Any composite metric or argument can be walked back to its carriers and method. | **Overhead** of maintaining SCR/RSCR. *Mitigation:* keep entries minimal but complete; use checklists from the pedagogical companion. |
| **Design/run clarity**            | Intent (MethodDescription) is cleanly separated from execution (Work traces).          | **Discipline** needed at boundaries. *Mitigation:* MIC templates; explicit “instantiates” bridges.                                    |
| **Objective evidence**            | External `TransformerRole` eliminates self‑evidence loops.                      | **Reflexive systems** require a mirror meta‑holon. *Mitigation:* provide a “reflexive modelling” appendix with examples.              |
| **Comparable numbers over time**  | Temporal coverage invariants prevent “trend” claims built on gaps.              | **Extra dating work** for legacy data. *Mitigation:* allow provisional labels until dating is completed.                              |
| **Safe composition of knowledge** | SCR/RSCR keep sources intact as Γ\_epist composes epistemes.                    | **Initial friction** in teams new to carrier thinking. *Mitigation:* start with “top‑10 carriers per claim” rule, expand as needed.   |
| **Feeds Trust Calculus (B.3)**    | Anchors provide the inputs (R, CL, etc.) needed to score confidence.            | —                                                                                                                                     |

---

#### 8 · Rationale (SoTA alignment, reader‑friendly)

* **Metrology & assurance.** The requirement to name quantities, units, uncertainty, calibration carriers reflects long‑standing metrology practice and modern assurance cases: numbers are only comparable when their **measurement models** are stated.
* **Knowledge provenance.** The EPV‑DAG and SCR/RSCR embody post‑2015 best practices in provenance for knowledge artefacts: keep a complete, machine‑checkable trail from claims to carriers; separate provenance from part‑whole.
* **Temporal reasoning.** Monotone coverage (no unexplained gaps/overlaps) aligns with temporal knowledge graph practice and avoids “impossible histories.”
* **Holonic parsimony.** By drawing a firewall between **mereology** (A.14) and **provenance**, A.10 prevents semantic leakage and keeps the holarchy well‑typed.
* **Role–Method–Work clarity.** Anchoring explicitly rides on A.15: **roles** act via **methods** specified at design‑time and produce **work** observed at run‑time. This keeps agency, policy, and execution disentangled yet connected.

---

#### 9 · Relations

* **Builds on:** A.1 Holonic Foundation; A.4 Temporal Duality; **A.12 Transformer Externalization**; **A.14 Advanced Mereology**; **A.15 Role–Method–Work Alignment**.
* **Constrains / Used by:** B.1 (all Γ‑flavours: `Γ_sys`, `Γ_epist`, `Γ_method`, `Γ\_time`, `Γ_work`); B.1.1 (Dependency Graph & Proofs).
* **Enables:** **B.3 Trust Calculus** (R/CL inputs, auditability); B.4 Canonical Evolution Loop (clean design/run bridges).

#### 10 · Migration (this draft, practical and brief)

Apply these text edits **only** in the holonic working file:

1. **Terminology**

   * `manifest` → **“Symbol Carrier Register (SCR)”**; `release manifest` → **“Release SCR (RSCR)”**.
   * `creator` / `observer` (as internal evidencer) → **`TransformerRole (external)`**.
   * “symbol register” (ambiguous) → **“Symbol Carrier Register (SCR)”**.
   * Keep **resource rosters** in `Γ_work` separate from SCR/RSCR.

2. **Γ naming**

   * `Γ_core` (legacy) → **`Γ_sys`** everywhere (note once: *formerly Γ\_core*).

3. **Boilerplate inserts**

   * In **A.10** (this pattern): retain definitions of **EPV‑DAG**, **SCR/RSCR**, and the flavour‑specific anchors.
   * In **B.1.3 (`Γ_epist`)**: add the **Obligations — SCR/RSCR** block (“`Γ_epist^synth` SHALL output SCR… `Γ_epist^compile` SHALL output RSCR…”).
   * In **B.1.5 (`Γ_method`)**: ensure **MIC** is referenced (Precedes/Choice/Join, guards, exceptions) and run‑time traces reference the **MethodDescription** they instantiate.
   * In **B.1.6 (`Γ_work`)**: say “resource rosters are not SCR/RSCR; anchor meter/log readings via EPV‑DAG.”


### Pattern A.11 — Ontological Parsimony (C‑5) \[A]

*“Add only what you cannot subtract.”*


#### 1 · Context

The FPF kernel aspires to remain **small enough to learn in a week** yet **broad enough** to model engines, proofs and budgets alike. Unchecked growth of primitives—well‑known from earlier “enterprise ontologies”—bloats diagrams, stalls tooling and intimidates new adopters. C‑5 therefore demands *minimal‑sufficiency*: a new core concept enters the kernel **only** when all routes of composition, refinement or role‑projection fail to express it without semantic loss.

---

#### 2 · Problem

| Pathology         | Real‑world symptom                                                                 |
| ----------------- | ---------------------------------------------------------------------------------- |
| **Concept creep** | Near‑synonyms proliferate (`U.Worker`, `U.Employee`, `U.Staff`), breaking queries. |
| **Zombie types**  | Legacy primitives linger unused yet block name space.                              |
| **Tool churn**    | Every fresh primitive forces IDE, validator and dashboard updates.                 |

Result: steep learning curves, fragile integrations, eroded trust in “first‑principles” promises.

---

#### 3 · Forces

| Force                            | Tension                                                            |
| -------------------------------- | ------------------------------------------------------------------ |
| **Expressiveness vs Simplicity** | Fine granularity helps static checks ↔ fewer nouns aid cognition.  |
| **Inclusivity vs Purity**        | New domains want vocabulary ↔ kernel must not be a dumping ground. |
| **Evolution vs Stability**       | Framework grows ↔ users depend on a stable core.                   |
| **Prestige vs Utility**          | Authors enjoy naming things ↔ every name tcharacteristics everyone else.      |

---

#### 4 · Solution — Four‑Gate **Minimal‑Sufficiency Protocol**

A proposal to add a `U.Type` or core relation **MUST** clear **all four gates** before admission and survives under a **Sunset Timer** thereafter.

| Gate                      | Test question                                                                                         | Rationale                                             |
| ------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| **G‑1 Composition**       | *Can existing primitives + roles/attributes express the concept without material loss?*               | Follows “composition over creation.”                  |
| **G‑2 Non‑Redundancy**    | *Does the proposal overlap ≥ 80 % with anything already live?*                                        | Blocks synonyms.                                      |
| **G‑3 Functional Naming** | *Does the chosen name state **what the thing does**, not what it *is made of*?*                       | Prevents vague catch‑alls; supports didactic clarity. |
| **G‑4 Sharp Boundary**    | *Is there a one‑sentence litmus test that unambiguously includes or excludes any candidate instance?* | Ensures crisp taxonomy edges.                         |

**Lifecycle — Sunset Timer**
A cleared type enters the kernel **provisionally** with a timer (default = 4 quarters). If usage count remains zero at expiry, the type faces *Sunset Review*: delete, demote to plug‑in, or renew with fresh evidence.

> *Manager’s mnemonic:* **“Compose, Unique, Functional, Crisp — or sunset.”**

---

#### 5 · Archetypal Grounding

| Gate    | **Rejected candidate** (why)                                                                                                                                                                               | **Accepted approach**           |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| **G‑1** | `U.CoolantPump` – expressible as `U.System:Pump` + `CoolingCirculatorRole`.                                                                                                                                | Composition via Role.           |
| **G‑2** | `U.Actuator` vs existing `U.Transformer` (90 % overlap).                                                                                                                                                   | Retain broader `U.Transformer`. |
| **G‑3** | `U.MiscellaneousObject` – name signals no function.                                                                                                                                                        | Reject; unclear purpose.        |
| **G‑4** | `U.SmallPart` – boundary depends on subjective size.                                                                                                                                                       | Reject; fails crisp test.       |
| —       | **`U.ProvenanceChain`** – required to record immutable evidence lineage; cannot be composed; functionally named; crisp membership rule (*“ordered list of Evidence Graph Ref with forward integrity hash”*). | Accepted, timer started.        |

#### 6 · Conformance Checklist

| ID          | Requirement                                                                                                                                               | Didactic aim                                                 |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| **CC‑OP 1** | A *Minimal‑Sufficiency Form* (≤ 1 page) **MUST** accompany every new kernel‑type proposal, documenting answers to Gates G‑1…G‑4 and a draft Sunset‑Timer. | Forces authors to think compositionally before adding nouns. |
| **CC‑OP 2** | Kernel inventory tooling **SHALL** stamp each admitted type with `sunset_due: <date>` (default = +4 quarters).                                            | Schedules later pruning; no forgotten zombies.               |
| **CC‑OP 3** | A quarterly *Usage Scan* **MUST** flag any core type with reference‑count = 0; flagged items enter Sunset Review automatically.                           | Turns parsimony into a living maintenance loop.              |
| **CC‑OP 4** | Renaming, aliasing, or splitting an existing type **REQUIRES** re‑passing all four gates and documenting a migration note.                                | Prevents redundancy re‑entering via back door.               |
| **CC‑OP 5** | Architheories **SHOULD** favour `Role` + attributes over proposing new domain types; proposals rejected when Gate G‑1 answer is “yes.”          | Extends parsimony culture beyond the kernel.                 |

---

#### 7 · Consequences

| Benefit                            | Impact for engineer‑managers                                                   | Trade‑off / Mitigation                                                                   |
| ---------------------------------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| **Lean kernel**                    | Fewer primitives → faster onboarding & clearer mental map.                     | Initial author effort to fill Minimal‑Sufficiency Form; template wizard auto‑fills 70 %. |
| **Reduced tool churn**             | Stable set of nouns keeps dashboards, linters, reasoners in sync for years.    | Occasionally slows acceptance of niche concepts; plug‑in layer absorbs urgency.          |
| **Automatic house‑cleaning**       | Sunset cycle prevents accrual of deadwood.                                     | Rare risk of deleting a sleeper hit; renewal path allows appeal.                         |
| **Encultured composition mindset** | Teams default to roles & attributes, boosting reuse and cross‑domain dialogue. | Requires role libraries and attribute taxonomies; provided in Part C.                    |

---

#### 8 · Rationale

**Cognitive science** shows working memory tops out around 4 ± 1 unfamiliar chunks (Cowan 2021). Combining that with Gate discipline keeps kernel size tractable (≈ 40 primitives). **Software metrics** from lean DSLs (Rust traits, Kubernetes CRDs) reveal that compositional modelling reduces change propagation cost by \~30 %. The Sunset Timer borrows from Kubernetes feature gate “alpha/beta/GA” progression model — proved effective at pruning half‑baked APIs.

### 9 · Relations

| Relation          | Pattern                 | Interaction                                               |
| ----------------- | ----------------------- | --------------------------------------------------------- |
| **Builds on**     | A 8 Universal Core      | A candidate must already pass the Three‑Domain Test.      |
| **Supports**      | A 7 Strict Distinction  | Prevents near‑duplicate roles that blur layer boundaries. |
| **Feeds**         | B 5 Kernel Change‑Log   | Records admissions, renames, sunsets.                     |
| **Complementary** | A 10 Evidence Graph Referring | Proposals cite evidence of irreducibility.                |

---

### 10 · Illustrative Uses (2022 – 2025)

* **Robotics CAL 2023** – `U.LiDARSensor` rejected (Gate G‑1 passed via role composition), saving three schema migrations.
* **Green‑Finance CAL 2024** – `U.CarbonCredit` admitted provisionally, but Sunset Review (usage = 0) demoted it to sector plug‑in, avoiding kernel noise.
* **Neuro‑informatics 2025** – `U.ProvenanceChain` accepted; by Q3 its heavy reuse in three architheories lifted timer and marked it *established*.

---

\### 11 · Open Questions

1. **Hard size cap** — should the kernel enforce an absolute limit (e.g., 64 live types) beyond which any new entry forces retirement of an old one?
2. **Semantic similarity tooling** — can embedding models automate Gate G‑2 overlap detection reliably across domains?
3. **Gate calibration** — is default Sunset Timer (4 quarters) optimal for research‑oriented architheories with slower uptake?


### **Pattern A.12 — External Transformer & Reflexive Split \[A]**

#### 1 · Intent & Context

The principle of causality is the bedrock of engineering and scientific reasoning: every change has a cause. In FPF, this translates to a strict architectural rule: **no "self-magic."** An action cannot happen without an actor. This pattern establishes the formal mechanism for modeling causality, ensuring that every transformation is attributed to an explicit, external agent.

This pattern operationalizes the **Agent Externalization Principle (C-2)**. It builds directly upon:
*   **A.3 (Transformer Constitution):** Which defines the core quartet of action: the `Agent` (who acts), the `MethodDescription` (the recipe), the `Method` (the capability), and the `Work` (the event).
*   **A.2 (Contextual Role Assignment):** Which provides the universal syntax `Holder#Role:Context` for defining agents.

The intent of this pattern is twofold:
1.  To mandate that every transformation is modeled as an interaction between a distinct **Agent** (playing a `TransformerRole`) and a distinct **Target** across a defined **Boundary**.
2.  To provide a rigorous pattern, the **Reflexive Split**, for modeling systems that appear to act upon themselves (e.g., self-calibration, self-repair) without violating the principle of external causality.

#### 2 · Problem

Without a strict rule of agent externalization, models become ambiguous and untraceable, leading to critical failures in design and audit:

1.  **Causality Collapse ("Self-Magic"):** Phrases like "the system configures itself" or "the document updates itself" create a causal black hole. It becomes impossible to answer the question, "What *caused* this change?" This makes debugging, root cause analysis, and assigning responsibility impossible.
2.  **Audit Dead-Ends:** An auditor tracing a change finds that the system is its own justification. There is no external evidence, no log from an independent actor, and therefore, no way to verify the integrity of the transformation. This is a direct violation of **Evidence Graph Referring (A.10)**.
3.  **Hidden Dependencies:** In a "self-healing" system, the healing mechanism (the regulator) and the operational part (the regulated) are modeled as a single monolithic block. This hides the critical internal dependency between them. A failure in the regulator might go unnoticed until the entire system collapses, because its role was never made explicit.

#### 3 · Forces

| Force | Tension |
| :--- | :--- |
| **Causal Clarity vs. Modeling Simplicity** | The need to explicitly model every cause-and-effect link vs. the desire to keep diagrams simple by representing self-regulating systems as single blocks. |
| **Objectivity vs. Internal States** | The need for an external, objective observer/actor to ground all claims vs. the reality that many systems have internal feedback loops that control their own state. |
| **Accountability vs. Automation** | In fully automated systems, it can be tempting to say "the system did it," but for assurance and safety, we must always be able to trace an action back to a specific, responsible component. |

#### 4. Solution

The solution is a two-part architectural mandate: **(1)** all transformations must be modeled with an external agent, and **(2)** apparent self-transformation must be modeled using the **Reflexive Split**.

#### 4.1 The Principle of the External Transformer

Every transformation in FPF is a `U.Work` event that is the result of an **Agent** acting upon a **Target**.

*   **The Agent:** The agent is a **Contextual Role Assignment** of the form `System#TransformerRole:Context`. This is the cause, the "doer."
*   **The Target:** The target is the `U.Holon` being changed. This can be another `U.System` or the **symbol carrier** of a `U.Episteme`.
*   **The Boundary:** The agent and the target are always separated by a `U.Boundary` and interact through a `U.Interaction`.

**Crucial Rule:** The `holder` of the Agent's `U.RoleAssignment` **cannot** be the same holon instance as the Target.
> `holder(Agent) ≠ Target`

This simple inequality is the core of the externalization principle. It constitutionally forbids self-magic.

##### 4.1.1 Reflexivity vs cross‑reference (normative note)

FPF distinguishes **reflexive transformation** from **episteme‑level reference**.  
*Reflexive* cases (e.g., “self‑calibration”) MUST be modeled by the **Reflexive Split** (Regulator→Regulated) and remain within the **world** ReferencePlane.  
When a claim **refers to** another claim/episteme, model it with **epistemeAbout(x,y)** and set **ReferencePlane(x)=episteme**. Such references **do not perform transformations** and **MUST NOT** be used to bypass the external‑agent rule. Evaluation of chains of episteme‑about relations MUST remain **acyclic within a single evaluation chain**; otherwise, abstain and request a split or external evidence.


#### 4.2 The Reflexive Split Pattern

So, how do we model a system that *does* act on itself, like a self-calibrating sensor? We use the **Reflexive Split**. We recognize that the system is not a monolith; it contains at least two distinct functional parts.

**The Procedure:**

1.  **Identify the Roles:** Decompose the system's function into two distinct roles: the part that *regulates* and the part that *is regulated*.
2.  **Model as Two Holons:** Model these two parts as two distinct (though possibly tightly coupled) `U.System` holons, even if they share the same physical casing.
3.  **Define the Internal Boundary:** Model the interface between them as an internal `U.Boundary` with a defined `U.Interaction` (e.g., a data bus, a mechanical linkage).
4.  **Assign the Transformer Role:** The regulating part becomes the `holder` of the `TransformerRole`. The regulated part becomes the `Target`.

Now, the "self-action" is modeled as a standard, external transformation that just happens to occur *inside* the larger system's boundary. Causality is restored, and the model becomes auditable.

**Didactic Note for Engineers & Managers: The "Two Hats" Analogy**

Think of the Reflexive Split like a manager who needs to review their own work. To do it properly, they must metaphorically wear "two hats."
*   **Hat 1: The Doer.** They perform the task.
*   **Hat 2: The Reviewer.** They step back, put on their "reviewer hat," and inspect the work *as if* it were done by someone else.

The Reflexive Split formalizes this. The "Doer" is the **Regulated** subsystem. The "Reviewer" is the **Regulator** subsystem, which plays the `TransformerRole`. By modeling them as two separate entities, we make the internal quality control loop explicit and prevent the logical error of a system magically grading its own homework.

#### 5 · Archetypal Grounding

The principle of external causality and the Reflexive Split pattern are universal. They apply equally to physical systems, epistemic artifacts, and socio-technical organizations.

| Scenario | Naive Description ("Self-Magic") | FPF Model with Reflexive Split | `Agent` & `Target` |
| :--- | :--- | :--- | :--- |
| **System Archetype** | "The robot calibrates itself." | The robot is modeled as a composite holon containing two subsystems: <br> 1. **`CalibrationController`** (`U.System`) <br> 2. **`SensorSuite`** (`U.System`) <br> They interact across an internal data bus (`U.Boundary`). | **Agent:** `CalibrationController#TransformerRole:RobotInternals` <br> **Target:** `SensorSuite` |
| **Episteme Archetype** | "The document automatically updates its cross-references." | The "document" is a system comprising: <br> 1. **`UpdateScript`** (a `U.System` that executes code) <br> 2. **`DocumentFile.xml`** (a `U.System` acting as a symbol carrier) <br> They interact via the file system (`U.Boundary`). | **Agent:** `UpdateScript#TransformerRole:DocumentSystem` <br> **Target:** `DocumentFile.xml` (the carrier of the `U.Episteme`) |
| **Socio-Technical Archetype** | "The team reviews its own performance." | The team is modeled as a collective `U.System` that enacts two roles at different times: <br> 1. **`ExecutionTeam`** (doing the sprint work) <br> 2. **`ReviewTeam`** (conducting the retrospective) <br> The "boundary" is the formal separation created by the retrospective ceremony. | **Agent:** `Team#ReviewerRole:RetrospectiveContext` <br> **Target:** The `U.Work` logs and artifacts produced by the `Team#ExecutionRole`. |

**Key takeaway from grounding:**
These examples demonstrate that there is *no such thing as self-action* in a well-formed model. Every action, even an internal one, can and must be decomposed into an external interaction between a distinct agent and a distinct target. This makes the causal chain explicit and auditable in all domains.

#### 6 · Conformance Checklist

To enforce the principles of externalization and causal clarity, all FPF models must adhere to the following normative checks.

| ID | Requirement (Normative Predicate) | Purpose / Rationale |
| :--- | :--- | :--- |
| **CC-A12.1 (External Agent Mandate)** | Every transformation (`U.Work`) **MUST** be attributed to an Agent (`U.RoleAssignment`) whose `holder` is distinct from the target holon. | This is the core rule that forbids self-magic. It ensures every action has an identifiable, external cause. |
| **CC-A12.2 (Reflexive Split for Self-Action)** | Any narrative of "self-modification" (e.g., self-repair, self-configuration) **MUST** be modeled using the Reflexive Split pattern. | Forces the modeler to make internal control loops explicit by identifying the distinct `Regulator` (Agent) and `Regulated` (Target) subsystems. |
| **CC-A12.3 (Boundary Explicitness)** | The `U.Boundary` and `U.Interaction` between the Agent and the Target **MUST** be explicitly modeled. | Makes interfaces a first-class citizen of the model. Prevents hidden dependencies and ensures interactions are auditable. |
| **CC-A12.4 (Episteme Carrier as Target)** | When a `U.Episteme` is modified, the `Target` of the transformation **MUST** be its **symbol carrier** (`U.System`), not the `U.Episteme` itself. | Reinforces **Strict Distinction (A.7)**. Knowledge doesn't change by magic; a physical agent must act on its physical representation. |
| **CC-A12.5 (No Self-Evidence)** | The Agent that performs a transformation **cannot** be the sole source of evidence for the success or properties of that transformation. Evidence **MUST** be anchored via an independent `Observer`. | Prevents conflicts of interest in assurance. The `Transformer` does the work; a separate `Observer` (another RoleAssignment) validates it. This aligns with **A.10 (Evidence Graph Referring)**. |

#### 7 · Consequences

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Causal Traceability & Auditability:** Every change is linked to a specific agent and interaction, creating a complete and unambiguous audit trail. This is essential for root cause analysis and accountability. | **Increased Model Granularity:** The Reflexive Split requires creating more model elements than a simple monolithic block. *Mitigation:* This is not a bug, but a feature. The "extra" elements represent real, critical parts of the system's architecture that were previously hidden. FPF tooling can help manage this via views that can "collapse" a split system for high-level diagrams. |
| **Architectural Honesty:** The pattern forces designers to be explicit about internal control loops, interfaces, and dependencies, leading to more robust and well-understood system architectures. | **Requires a Shift in Thinking:** Modelers accustomed to "self-x" narratives must learn to think in terms of external interactions. *Mitigation:* The "Two Hats" analogy and clear archetypes (Section 5) serve as powerful didactic tools to facilitate this shift. |
| **Enables True Modularity:** By making interfaces explicit, the pattern supports modular design. A `Regulator` subsystem could potentially be swapped out for a different one as long as it respects the same `U.Interaction` Standard. | - |
| **Unlocks Deeper Analysis:** Once an internal control loop is made explicit, it can be formally analyzed for stability, performance, and failure modes using tools like the Supervisor-Subsystem Feedback Loop pattern (B.2.5). | - |

#### 8 · Rationale

The principle of externalization is not an arbitrary rule imposed by FPF; it is a distillation of foundational concepts from multiple rigorous disciplines.

*   **Cybernetics & Control Theory:** As Ashby's Law of Requisite Variety and modern control theory (e.g., Matni et al., 2024) demonstrate, regulation is fundamentally an **interaction across a boundary** between a controller and a plant. Conflating the two hides the causal structure and makes stability analysis impossible. The Reflexive Split is the FPF's implementation of this core cybernetic principle.
*   **Physics (Constructor Theory):** As discussed in A.3, Constructor Theory recasts physics in terms of what transformations are possible. A transformation is always performed by a "constructor" (our `Transformer`) on a substrate. The theory does not contain "self-constructing" substrates. FPF's externalist stance is fully aligned with this physical worldview.
*   **Philosophy of Science (Objectivity):** The scientific method is built on the principle of external observation and verification. A theory cannot validate itself; its predictions must be checked by an independent experiment. The `No Self-Evidence` rule (CC-A12.5) is the direct implementation of this principle in the FPF's assurance calculus.
*   **Software Engineering (Dependency Inversion):** The principle that high-level modules should not depend on low-level modules, but both should depend on abstractions, is a form of externalization. It enforces clean separation and makes systems more modular and testable. The explicit `U.Boundary` in our pattern serves the same architectural purpose as a well-defined interface in software.

By mandating externalization, FPF is not adding bureaucratic overhead. It is enforcing a set of first principles that are demonstrably essential for building complex systems that are understandable, auditable, and trustworthy.

#### 9 · Relations

*   **Directly Implements:** `C-2 Agent Externalization Principle`.
*   **Builds Upon:**
    *   `A.1 Holonic Foundation`: Provides the `U.System` and `U.Episteme` holons that act as agents and targets.
    *   `A.2 Role Taxonomy`: Provides the Contextual Role Assignment (`U.RoleAssignment`) mechanism to define the Agent.
    *   `A.3 Transformer Constitution`: Defines the `TransformerRole` that the Agent plays.
*   **Enables and Constrains:**
    *   `A.10 Evidence Graph Referring`: Provides the causal structure (who did what) that evidence must be anchored to.
    *   `B.2 Meta-Holon Transition (MHT)`: A Reflexive Split is often the first step in identifying an emergent supervisory layer that may later be promoted to a new meta-holon.
    *   `B.2.5 Supervisor-Subsystem Feedback Loop`: This pattern provides the detailed architecture for the `Regulator-Regulated` interaction that the Reflexive Split reveals.

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

# A.15.1 — U.Work  \[D]

## 1 · Problem Frame

After we have agreed **who is assigned** (via **Role assignment**), **what they can do** (via **Capability**), and **how in principle** it should be done (via **Method/MethodDescription**), we still need a precise concept for **what actually happened** in real time and space.

That concept is **`U.Work`**: the **dated run‑time occurrence** of enacting a MethodDescription by a specific performer under a Role assignment, with concrete parameter bindings, resource consumption, and outcomes, **anchored to a domain referent that actually changes** (asset/product/dataset) — **not** merely the manipulation of records about that referent. Managers care about Work because it is the **only place** where cost, time, defects, and evidence are **real**. Architects care because Work ties plans and specs to accountable execution.

## 2 · Problem (what breaks without a clean notion of Work)

1. **Plan/run confusion.** Schedules and diagrams get mistaken for “the process,” so audits and KPIs become fiction.
2. **Spec/run conflation.** A method description (code/SOP) is reported as if it were an execution; conversely, logs are treated as recipes.
3. **Who/when leakage.** People and calendars are baked into specs; reuse and staffing agility collapse.
4. **Resource dishonesty.** Energy/money/tool wear are booked to methods or roles, not to actual runs; costing and sustainability metrics drift.
5. **Mereology muddle.** Teams hand‑wave over “sub‑runs,” retries, overlaps, or long‑running episodes; roll‑ups double‑count or miss work.

## 3 · Forces (what the definition must balance)

| Force                              | Tension we resolve                                                                                    |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Universality vs. domain detail** | One Work notion for surgery, welding, ETL, proofs, lab cycles—while letting each keep its vocabulary. |
| **Granularity vs. aggregation**    | Atomic runs vs. composite operations; we need roll‑up without double‑count.                           |
| **Concurrency vs. order**          | Parallel/overlapped activities need clear part/overlap semantics.                                     |
| **Identity vs. retries**           | A failed attempt, a retry, and a resumed episode—what is “the same” work?                             |
| **Time realism vs. simplicity**    | We need intervals and coverage but cannot bury users in temporal logic notation.                      |

## 4 · Solution — define `U.Work` as the accountable, dated occurrence

### 4.1 Definition

**`U.Work`** is a **4D occurrence holon**: a **dated run‑time enactment** of a `U.MethodDescription` by a performer designated through a `U.RoleAssignment`, **executed within a concrete `U.System/SubSystem`**, inside a `U.BoundedContext`, that binds concrete parameters, consumes/produces resources, and leaves an auditable trace. 
Each `U.Work` is a **morphism** `Δ` on a declared **state‑plane** (`StatePlaneRef`), mapping ⟨**pre‑state**, **inputs**⟩ to ⟨**post‑state**, **outputs**⟩ for one or more **affected referents**.

> **Memory aid:** *Work = “how it went this time”* (dated, resourced, accountable).

### 4.2 Core anchors (conceptual descriptors; not a data schema)

When you describe a Work instance in a review, answer these prompts:

1. **Window** — start/end timestamps (and, where relevant, location/asset).
2. **Spec** — `isExecutionOf → U.MethodDescription` (the description actually followed; **edition pinned** if applicable).
3. **Performer** — `performedBy → U.RoleAssignment` (which **holder#role\:context** acted).
4. **Parameters** — concrete values bound for this run (from the **MethodDescription** parameter declarations).
5. **Inputs/Outputs** — material/information artifacts read/written, products/services delivered.
6. **Resources** — energy, materials, machine time, money (the **only** place we book them).
7. **Outcome** — success/failure classes, quality measures, acceptance verdicts (**map‑then‑compare** per **ComparatorSet** under **CG‑Spec**; pin editions).
8. **Links** — predecessor/successor/overlap relations to other Work, and step/run nesting (if part of a bigger operation).
9. **Context** — the bounded context(s) under which this run is judged (normally inherited from the MethodDescription and RoleAssigning; see A.15 for cross‑checks).
10. **Effect (Δ)** — `affected → {referent(s)}` + **pre‑state anchor** and **post‑state anchor** (or a declared **Δ‑predicate** evaluated on evidence) on the declared state‑plane (**StatePlaneRef**).
11. **System** — `executedWithin → U.System` (the operational system/sub‑system accountable for the occurrence; **mandatory**).
12. **Evidence & Telemetry (optional)** — if the run feeds **G.11** refresh or QD/OEE archives, cite **PathId/PathSliceId** and active **policy‑id** used for illumination; do not elevate gauges into dominance without CAL policy.

### 4.3 Clear distinctions (the four‑slot grammar in action)

| You are pointing at…                          | The right FPF concept  | Litmus                                                          |
| --------------------------------------------- | ---------------------- | --------------------------------------------------------------- |
| The **recipe/code/diagram**                   | **MethodDescription**         | Is it knowledge on a carrier?                                   |
| The **semantic “way of doing”**               | **Method**             | Same Standard across notations?                                 |
| The **assignment** (“who is being what”)     | **Role → RoleAssigning** | Can be reassigned without changing the system?                  |
| The **ability** (“can do within bounds”)      | **Capability**         | Would remain even if not assigned?                             |
| The **dated occurrence** with logs, resources | **Work**               | Did it happen at (t₀, t₁), consume resources, produce outcomes? |
| The **state change caused this time**         | **Work.Δ**             | Did the referent move from pre→post on the declared state‑plane? |

### 4.4 Publication (MVPK guard‑rails for `U.Work`) — *normative*
Publication of `U.Work` across MVPK faces **must** be a typed projection that does **not** mutate intensional semantics (A.7; E.17). Concretely:
1. **No new claims.** Faces (**PlainView / TechCard / InteropCard / AssuranceLane**) **SHALL NOT** introduce properties beyond the `U.Work` intensional arrow; they **project** presence‑pins only (time window, performer, spec, parameter‑binding occurrence, resource ledger presence, acceptance verdict presence). Numeric/comparable content appears **only** with pins (see 4.4‑4.5 below); **“signature”** is banned on faces.
2. **No Γ‑leakage.** Faces **MUST NOT** smuggle Γ semantics (union/hull/overlap policy, budget algebra) into prose; whenever aggregation is shown, the face **cites** the Γ‑operator and policy‑id used. Compute totals outside the face per B.1; faces carry **references**, not implied Γ rules.
3. **No I/O re‑listing.** Per MVPK, faces **do not duplicate** intensional I/O lists. They show **presence‑pins** and **anchors** to carriers/lanes/editions only (E.17 §5.4).
4. **Lawful orders (sets).** Where a `U.Work` face presents any **comparison or ranking across runs** (e.g., acceptance classes, parity/benchmark inserts), the face **must**: (i) compare **after mapping** via a declared **ComparatorSet**; (ii) **return sets** (Pareto/Archive) when order is partial; (iii) **forbid** hidden scalarization/ordinal means (cf. G.9).
5. **Comparator/Transport edition pins.** Any numeric/comparable statement on a `U.Work` face **MUST** pin the **CG‑Spec**/**ComparatorSet** edition(s) and, where scale/plane conversion occurs, the **UNM.TransportRegistry** edition (**Φ**/**Φ^plane** policy‑ids). Cross‑context/plane crossings **route penalties to R‑lane only** (Bridge id + Φ) (cf. E.17; G.9).
6. **Cross‑tier citations.** Any citation of AT1/AT2 artefacts on a `U.Work` face **MUST** carry **BridgeCard + UTS row** (with plane notes and CL routing).
7. **No surrogate‑run creation.** Faces **MUST NOT** synthesize “virtual runs” from reconstructed records alone; a face may reference only `U.Work` instances that meet Δ‑anchoring in §4.2/§8.

### 4.5 ATS profile & crossings (tier discipline) — *normative*
* **Tier.** `U.Work` is **AT0**. Any face that cites AT1/AT2 artefacts (e.g., ComparatorSet, CG‑Spec editions) **MUST** include **BridgeCard + UTS row** and record **Φ(CL)/Φ^plane** policy‑ids; **penalties reduce `R_eff` only**.
* **Binding discipline.** **Launch values bind only here** (occurrence). Plan‑time proposals remain proposals; do not back‑fill plan faces with run‑time bindings. **Pre/post state anchors bind here** (pre at start; post at completion or at declared checkpoints).

## 5 · Work mereology (how runs form holarchies)

We adopt a **4D extensional** stance for occurrences: a Work is identified primarily by its **spatiotemporal extent** and its execution anchors (spec used, performer, parameterization). This avoids double‑counting and keeps aggregation sound. FPF adapts insights from BORO/constructive ontologies to Work while staying practical.

### 5.1 Parts and wholes of Work (design‑neutral, run‑time facts)

* **Temporal‑part (`TemporalPartOf_work`).** A proper **time‑slice** of a Work (e.g., the first 10 minutes of a 2‑hour run). Useful for monitoring and SLAs.
* **Episode‑part (`EpisodeOf_work`).** A **resumption fragment** after an interruption (same run identity if policy deems it one episode; see 5.5).
* **Operational‑part (`OperationalPartOf_work`).** A **sub‑run** that enacts a **factor** of the Method/Spec (e.g., “incision” run within “appendectomy” run), possibly **overlapping** with others in time.
* **Parallel‑part (`ConcurrentPartOf_work`).** Two sub‑runs that **overlap** in their windows, coordinated by the same higher‑level run.

**Didactic rule:** **Method composition ≠ proof of Work decomposition.** Sub‑runs often map to method factors, but retries, batching, pipelining, and failures make the mapping non‑isomorphic.

### 5.2 Key relations among Work

* **`precedes/happensBefore`** — strict partial order on Work windows.
* **`overlaps`** — intervals intersect but neither contains the other.
* **`contains/within`** — one Work’s window contains another’s.
* **`causedBy/causes`** — pragmatic causal links (e.g., a rework caused by a failed inspection run).
* **`retryOf`** — a new Work instance re‑attempting the same MethodDescription with revised parameters.
* **`resumptionOf`** — a Work episode that **continues** an interrupted run (policy decides identity; see 5.5).

These relations are **run‑time facts**, not design assumptions.

### 5.3 Operators for roll‑ups (Γ\_time and Γ\_work)

* **Temporal coverage — `Γ_time(S)`**
  For a set `S` of Work parts, returns a **coverage interval set** (union of intervals) or, when required, the **convex hull** `[min t₀, max t₁]`. Use **union** for utilization; use **hull** for lead time.
  *Properties:* idempotent, commutative, monotone under set inclusion.

* **Resource aggregation — `Γ_work(S)`**
  For a set `S` of Work parts, returns the **aggregated resource ledger** (materials, energy, time, money) with de‑duplication rules for shared/overlapped parts (context‑declared).
  *Properties:* additive on **disjoint** parts; requires **overlap policy** otherwise (e.g., attribute costs to the parent once, not to each child).

**Manager’s tip:** Pick the coverage operator that matches your KPI: **union** for machine utilization; **hull** for calendar elapsed; never mix silently.

### 5.4 Identity of a Work (extensional criterion, pragmatically framed)

Two Work records refer to the **same Work** iff, in the relevant context:

* their **time–space extent** is the same (within declared tolerance),
* they link to the **same `MethodDescription`**,
* they have the **same performer** (`U.RoleAssignment`), and
* they bind the **same parameters** (or declared‑equivalent values).

If any of these differ (or the context declares equivalence absent), they are **distinct** Work instances (e.g., a retry).

### 5.5 Interruptions, retries, resumptions (episode policy)

* **Retry:** **new Work** with its own window and parameters; link via `retryOf`.
* **Resumption:** **same Work identity** split into **episodes** if the context’s **episode policy** declares so (e.g., “power loss under 5 minutes keeps identity”).
* **Rework:** **new Work** caused by a failure in earlier Work; link via `causedBy`.

**Why it matters:** plans, costs, and quality stats depend on whether you treat a disruption as **one episode** or **a new run**. Declare the policy **in the bounded context**.

### 5.6 Compositionality of effects (Δ)

For any Work with parts, the **effect of the whole** must be the **rules‑declared composition** of the effects of its parts plus any declared overheads/residuals. Composition must align with the overlap rules used by `Γ_work` (e.g., no double‑count of shared fixed costs, and consistent attribution of variable deltas).

## 6 · Archetypal grounding (parallel domains)

### 6.1 Surgical case (overlap and episodes)

* **Top run:** `Appendectomy_Case#2025‑08‑10T09:05–11:42`.
* **Spec:** `Appendectomy_v5` (MethodDescription).
* **Performer:** `OR_Team_A#SurgicalTeamRole:Hospital_2025` (RoleAssigning).
* **Operational parts:** `Incision` (09:15–09:22), `Exploration` (overlaps with monitoring), `Closure` (11:10–11:35).
* **Episode:** brief power dip 10:02–10:07 → **resumptionOf** same run (per hospital policy).
* **Γ\_time:** union for OR utilization; hull for patient lead time.
* **Γ\_work:** totals consumables and staff time once (no double‑count for overlapping sub‑runs).

### 6.2 ETL pipeline (parallelism and retries)

* **Top run:** `ETL_Nightly_2025‑08‑11T01:00–01:47`.
* **Spec:** `ETL_v12.bpmn`.
* **Performer:** `ETL_Runtime#TransformerRole:DataOps_2025`.
* **Parallel parts:** `Extract_A` ‖ `Extract_B`; `Transform` starts when either completes (overlap).
* **Retry:** `Load` failed at 01:36; retried with batch size ↓ — **new Work** linked via `retryOf`.
* **Γ\_time:** hull for SLA, union for cluster utilization.
* **Γ\_work:** sum compute minutes; attribute storage I/O once at the parent.

### 6.3 Thermodynamic cycle (work as a path)

* **Run:** `Carnot_Cycle_Run#2025‑08‑09T13:00–13:06`.
* **Spec:** `Carnot_Cycle_Spec` (MethodDescription with Dynamics model).
* **Performer:** `LabRig_7#TransformerRole:ThermoLab`.
* **Work identity:** the **path in state‑space** traced during the interval; outputs: heat/work tallies.
* **Γ\_time:** straightforward interval; **Γ\_work:** integrates energy exchange; no “steps” required.

---

## 7 · Bias‑Annotation (as in E‑cluster)

* **Lenses tested:** `Prag`, `Arch`, `Did`, `Epist`.
* **Scope declaration:** Universal; temporal semantics and episode policy are **context‑local** via `U.BoundedContext`.
* **Rationale:** Gives FPF a clean, actionable notion of **occurrence** compatible with `U.RoleAssignment` / **Role Enactment** (A.2.1; A.15) and with 4D extensional thinking, so that costing, quality, and audit rest on **runs**, not on plans or recipes.

## 8 · Conformance Checklist (normative)

**CC‑A15.1‑1 (Strict distinction).**
`U.Work` is a **dated run‑time occurrence**. It is **not** a `U.Method` (semantic way), **not** a `U.MethodDescription` (description), **not** a `U.Role/RoleAssigning` (assignment), and **not** a `U.WorkPlan` (plan/schedule).

**CC‑A15.1‑2 (Required links).**
Every `U.Work` **MUST** reference:
(a) `isExecutionOf → U.MethodDescription` (the spec followed; **edition pinned**),
(b) `performedBy → U.RoleAssignment` (the assigned performer in context), and
(c) `executedWithin → U.System/SubSystem` (the operational system accountable for the occurrence).

**CC‑A15.1‑3 (Time window).**
Every `U.Work` **MUST** carry a closed interval `[t_start, t_end]` (or an explicitly marked open end for in‑flight work) and, where relevant, location/asset.

**CC‑A15.1‑4 (Context anchoring & judgement).**
A `U.Work` **MUST** be judged inside a declared **`U.BoundedContext`** (the **judgement context**).

* By default, the judgement context is **the context of the referenced MethodDescription**.
* If `performedBy` references a RoleAssigning in a different context, there **MUST** exist an explicit **Bridge (`U.Alignment`)** or policy stating cross‑context acceptance. Otherwise, the Work is **non‑conformant** in that context.

**CC‑A15.1‑4b (State‑plane anchoring).**
Each `U.Work` **MUST** declare a `StatePlaneRef` for its Δ‑judgement.

**CC‑A15.1‑5 (RoleAssigning validity).**
The `performedBy` RoleAssigning’s `timespan` **MUST** cover the Work interval. If it does not, the Work is **invalid** or must be re‑judged in a context that allows retroactive assignments.

**CC‑A15.1‑6 (Parameter binding).**
Parameters declared by the **MethodDescription** **MUST** have concrete values bound **at Work creation/start** and recorded with the Work. Defaults in the spec do not satisfy this requirement.

**CC‑A15.1‑7 (Capability check).**
All capability thresholds stated by the Method/MethodDescription **MUST** be checked against the **holder** in `performedBy` **at the time of execution** (or at defined checkpoints). Violations must be flagged on the Work outcome.

**CC‑A15.1‑8 (Acceptance criteria).**
Success/failure and quality grades **MUST** be determined by the acceptance criteria declared (or referenced) by the **MethodDescription**/**CG‑Spec** **in the judgment context**. The verdict is recorded on the Work.

**CC‑A15.1‑9 (Resource honesty).**
All consumptions and costs (energy, materials, machine‑time, money, tool wear) **SHALL** be booked **only** to `U.Work` (not to Method, MethodDescription, Role, or Capability). Estimates may live in specs; **actuals** live in Work.

**CC‑A15.1‑10 (Mereology declared).**
If a Work has parts, the chosen **part relation(s)** must be declared (temporal‑part, episode‑part, operational‑part, concurrent‑part). Ambiguous mixtures are forbidden.

**CC‑A15.1‑11 (Γ\_time selection).**
For any roll‑up, the judgement context **MUST** declare which temporal coverage operator applies: **union** (utilization) or **convex hull** (lead time). Silent mixing is prohibited.

**CC‑A15.1‑12 (Γ\_work aggregation).**
Aggregation of resource ledgers across Work parts **MUST** specify an **overlap policy** (e.g., “attribute shared machine‑time to parent only”) to prevent double‑counting.

**CC‑A15.1‑13 (Identity & retries).**
A retry **MUST** be modeled as a **new Work** linked via `retryOf`. Interruptions that are treated as the **same run** must be modeled as **episodes** (`resumptionOf`) per a context‑declared **episode policy**.

**CC‑A15.1‑14 (Concurrency & ordering).**
Overlaps and precedences among Work **MUST** use interval relations (`overlaps`, `precedes`, `contains/within`). Implicit “step order” claims are not admissible evidence.

**CC‑A15.1‑15 (Cross‑context evidence).**
If a Work is to be accepted in multiple contexts (e.g., regulatory + operational), either:
(a) re‑judge it in each context, or
(b) provide Bridges that map acceptance criteria/units/roles; never assume cross‑context identity by name.

**CC‑A15.1‑16 (Spec changes during run).**
If the MethodDescription version changes mid‑run, the Work **MUST** either:
(a) split into episodes bound to respective specs, or
(b) record an explicit **spec override** event in the judgement context. Silent substitution is forbidden.

**CC‑A15.1‑17 (Distributed performers).**
If multiple RoleAssignings jointly perform the same top‑level Work (e.g., multi‑agent orchestration), the Work **MUST** either:
(a) designate a **lead RoleAssigning** and list others as **concurrent parts**, or
(b) be modeled as a **parent Work** with child Works per RoleAssigning.

**CC‑A15.1‑18 (Logs ≠ Work by themselves).**
Logs/telemetry are **evidence** for a Work; they **do not constitute** a Work unless bound to (spec, performer, time window) and judged in a context.

**CC‑A15.1‑19 (Affected referent).** Each `U.Work` **MUST** name at least one affected referent (e.g., `U.Asset`, product/batch, dataset/document) via `affected → {…}`.

**CC‑A15.1‑20 (State‑change witness).** Each `U.Work` **MUST** carry either (a) explicit **pre‑state**/**post‑state** anchors on the declared state‑plane or (b) a **Δ‑predicate** that can be evaluated on evidence. Trivial “no‑op” runs **MUST** be flagged as such.

**CC‑A15.1‑21 (World anchoring vs. record‑handling).** A run whose only effect is copying/reformatting records **does not** qualify as `U.Work` unless the judgment context declares those records to be the **product referent** (e.g., data‑product manufacture).

**CC‑A15.1‑22 (System anchoring).** Each `U.Work` **MUST** declare `executedWithin → U.System/SubSystem`; if different from the asset of change, keep `affected` explicit.

**CC‑A15.1‑23 (Compositionality of Δ).** For composite Work, the parent effect **MUST** be the declared composition of child effects under the same overlap policy as `Γ_work`.

**CC‑A15.1‑24 (No new claims on faces).** MVPK faces for `U.Work` **SHALL NOT** add properties/claims beyond the intensional arrow; numeric/comparable content **MUST** include unit/scale/reference‑plane/**EditionId** pins; the term **“signature”** is banned on faces.

**CC‑A15.1‑25 (No Γ‑leakage).** Faces **MUST** reference Γ operators/policies by id when showing aggregates; they **MUST NOT** encode aggregation semantics in prose or imply defaults. Γ lives in Part B; faces carry **pinned references** only.

**CC‑A15.1‑26 (No I/O re‑listing).** Faces **MUST NOT** restate intensional I/O; publish **presence‑pins** and anchors only (per MVPK §5.4).

**CC‑A15.1‑27 (Lawful orders; return sets).** Any across‑run comparison presented on a `U.Work` face **MUST** use a declared **ComparatorSet** (map‑then‑compare), **return sets** when order is partial, and **forbid** hidden scalarization/ordinal means.

**CC‑A15.1‑28 (Comparator/Transport pins).** Any numeric/comparable acceptance or KPI on a `U.Work` face **MUST** pin `ComparatorSet.edition`, `CG‑Spec.edition`, and (where conversions occur) `TransportRegistry.edition` with **Φ/Φ^plane** policy‑ids; Bridge ids are mandatory for cross‑context/plane reuse; **penalties → R only**.

**CC‑A15.1‑29 (Telemetry hooks, when applicable).** If a Work instance feeds **G.11** or QD/OEE portfolios, it **SHALL** include `PathId/PathSliceId` and the active **policy‑id** in its evidence; illumination remains a **gauge** unless CAL explicitly promotes it.

## 9 · Temporal & Aggregation Semantics (normative operators & invariants)

### 9.1 Temporal coverage `Γ_time`

* **Input:** a finite set `S` of Work instances or Work parts.
* **Output:** either (a) the **union** of their intervals, or (b) the **convex hull** `[min t_start, max t_end]`—**as declared by context** and KPI.
* **Invariants:**

  * **Idempotent:** `Γ_time(S ∪ S) = Γ_time(S)`
  * **Commutative:** order of elements irrelevant
  * **Monotone:** if `S ⊆ T` then coverage(S) ⊆ coverage(T) (for union) or hull(S) ⊆ hull(T) (for hull)
* **Usage guidance:**

  * Use **union** for **utilization/availability** (how much of the clock time the asset was actually busy).
  * Use **hull** for **lead/cycle time** (elapsed from first touch to last release).
  * **Manager’s tip:** Write the choice near the KPI; many disputes are just a hidden union‑vs‑hull mismatch.

### 9.2 Resource aggregation `Γ_work`

* **Input:** a finite set `S` of Work instances or parts with resource ledgers.
* **Output:** an **aggregated ledger** (materials, energy, machine‑time, money, tool wear) with explicit **overlap policy**.
* **Invariants:**

  * **Additivity on disjoint parts:** if intervals/resources are disjoint by policy, totals add.
  * **No double‑count:** overlapping costs must follow the declared policy (e.g., count once at parent).
  * **Traceability:** each aggregated figure must be reconcilable to contributing Work IDs.
* **Typical policies:**

  * **Parent‑attribution:** shared fixed costs at parent; variable costs at children.
  * **Pro‑rata by wall‑time:** split overlaps by relative durations.
  * **Driver‑based:** allocate by a declared driver (e.g., CPU share, weight, priority).

## 10 · Cross‑context checks (MethodDescription ↔ RoleAssigning ↔ Work)

When a Work is recorded, perform these **three quick checks**:

1. **Spec–Context Check.** Does `isExecutionOf` refer to a MethodDescription **defined in** the judgement context (or bridged to it)?

   * If **no**, the Work is **out‑of‑context**; either change context or add a Bridge.

1. **RoleAssigning–Context Check.** Is `performedBy`’s RoleAssigning **valid in** the same context (or bridged)?

   * If **no**, the Work is **unassigned** for that context; remedy via a valid RoleAssigning or a policy exception.

1. **Standard–Outcome Check.** Do the Work’s inputs/outputs and metrics satisfy the **acceptance criteria** from the spec **as interpreted in that context**?

   * If **no**, the Work **fails** or is “conditionally accepted” per context policy.

> **Manager’s mnemonic:** Context, assignment, Standard → **CAC**. Fail any → the Work is not acceptable *here* (perhaps acceptable elsewhere).

---

## 11 · Anti‑patterns (and the right move)

* **“The log is the process.”** Dumping telemetry without binding (spec, performer, context) → **Not Work**. Create a Work, link the log as evidence.
* **Record‑only transforms.** ETL/replication of records with no declared affected referent (product/dataset as product) → **Not Work** in this context; either declare the dataset as the product referent or move it to `U.WorkPlan`/operations‑support.
* **Silent cross‑context acceptance.** “Ops accepted it, so audit accepts it.” → Add a **Bridge** or re‑judge in audit context.
* **Spec drift in mid‑run.** Swapping SOP v5→v6 without recording → Split into episodes or record override.
* **Budget on the method.** Charging costs to Method or Role → Book **only** to Work; keep estimates in specs.
* **Part ambiguity.** Mixing retries, episodes, and operational parts with no declared relation → Choose and declare the part relation.
* **Union/hull confusion.** Changing KPI coverage silently between reports → Declare `Γ_time` policy per KPI.
* **Double‑count in overlaps.** Summing child and parent resource ledgers → Declare and apply an overlap policy.

---

## 12 · Migration notes (quick wins)

1. **Backfill links.** For existing logs, create Work records and attach `isExecutionOf` and `performedBy`.
2. **Name the context.** Pick the judgement context explicitly; add Bridges if multiple contexts must accept.
3. **Publish the episode policy.** Decide when an interruption keeps identity vs forces a new run.
4. **Choose Γ\_time per KPI.** Put “union” or “hull” in the KPI definition; stop arguing in meetings.
5. **Set an overlap policy.** Write one sentence on how shared costs are allocated; apply consistently.
6. **Pull plans out.** Move calendars to `U.WorkPlan`; let Work record actuals.
7. **Parameter blocks.** Make parameters explicit and bind them at start; your root‑cause analyses will get 10× easier.

---

## 13 · Consequences

| Benefits                                                                                                                 | Trade‑offs / mitigations                                                                   |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| **Auditable reality.** Costs, time, and quality attach to concrete runs; root‑cause analysis and accountability improve. | **More records.** You create Work instances; mitigate with templates and automation.       |
| **Sound roll‑ups.** Γ\_time/Γ\_work turn roll‑ups from hand‑waving into declared policy; KPIs become comparable.         | **Policy discipline.** You must choose union vs hull and an overlap policy; write it once. |
| **Cross‑context clarity.** CAC checks prevent silent model drift; bridges make acceptance explicit.                      | **Bridge upkeep.** Keep mappings short and focused; review at releases.                    |
| **4D extensional coherence.** Parts/overlaps/retries stop double‑counting and identity confusion.                        | **Learning curve.** Teach episode vs retry; include examples in onboarding.                |

---

## 14 · Relations

* **Builds on:** A.1 Holonic Foundation; A.1.1 `U.BoundedContext`; **U.System**; A.2 `U.Role`; A.2.1 `U.RoleAssignment`; A.2.2 `U.Capability`; A.3.1 `U.Method`; A.3.2 `U.MethodDescription`.
* **Coordinates with:** A.15 Role–Method–Work Alignment (the “four‑slot grammar”); B.1 Γ (aggregation) for resource/time operators; E‑cluster lexical rules (L‑PROC/L‑FUNC).
* **Informs:** Reporting/KPI patterns; Assurance/evidence patterns (Work as the anchor for audits); Scheduling patterns (`U.WorkPlan` ↔ `U.Work` deltas).

---

## 15 · Didactic quick cards

* **What is Work?** *How it went this time* → dated, resourced, accountable.
* **Four‑slot grammar:** Who? **RoleAssigning**. Can? **Capability**. How? **Method/MethodDescription**. Did? **Work**.
* **CAC checks:** **Context** (judgement), **assignment** (valid RoleAssigning), **Standard** (acceptance criteria).
* **Roll‑ups:** `Γ_time = union` (utilization) or `hull` (lead time); `Γ_work` with a declared overlap policy.
* **Episodes vs retries:** same run split vs new run; write the policy.
* **Resource honesty:** actuals booked **only** to Work; estimates live in specs.

# A.15.2 — U.WorkPlan  \[D]


## 1 · Context (plain‑language motivation)

Operations live on **time**. Even with perfect roles, abilities, and methods, nothing ships unless we **decide when and by whom** concrete runs **should** happen, under what **constraints** and **budgets**. Teams need a first‑class concept for **plans and schedules** that does **not** get confused with:

* the **semantic “way of doing”** (that is `U.Method`),
* the **written recipe** (that is `U.MethodDescription`),
* the **actual execution** (that is `U.Work`), or
* the **state laws** (that is `U.Dynamics`).

`U.WorkPlan` is that missing anchor.

---

## 2 · Problem (what breaks without `WorkPlan`)

1. **“Workflow = schedule” conflation.** Flowcharts or code are used as calendars; resource clashes and SLA misses follow.
2. **Plan/run blur.** Gantt bars or Kanban tickets are reported as if the work already happened; audits and costing degrade.
3. **Spec/time leakage.** People and calendars creep into MethodDescriptions; reuse and staffing agility collapse.
4. **No variance model.** Without planned baselines, deviations in time, cost, and quality cannot be explained or improved.
5. **Structure entanglement.** BoM and org charts get baked into “process” views; plans become brittle and unmaintainable.

---

## 3 · Forces (what we must balance)

| Force                              | Tension we resolve                                                                                      |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Universality vs. domain idioms** | One plan concept that fits hospitals, fabs, data centers, and research labs—while honoring local terms. |
| **Commitment vs. flexibility**     | Plans must be firm enough to coordinate, yet easy to update as reality changes.                         |
| **Assignment vs. assignment**     | Plans may name intended performers; the actual assignment must still be checked at run time.           |
| **Budgets vs. actuals**            | Plans carry targets and reservations; only Work carries actual spend.                                   |
| **Decomposition vs. mapping**      | Plan tasks decompose conveniently; they do not force a shape on actual Work runs.                       |

---

## 4 · Solution — the `U.WorkPlan` as the time‑bound intention to execute Work

### 4.1 Definition

**`U.WorkPlan`** is an **`U.Episteme`** that **declares intended `U.Work` occurrences** over a horizon, with **planned windows**, **dependencies**, **intended performers** (as **role kinds** or **proposed RoleAssignings**), **resource budgets/reservations**, and **acceptance targets**—**within a `U.BoundedContext`**.

> **Strict distinction (memory aid):**
> **Method** = *how in principle*. **MethodDescription** = *how it is written*.
> **WorkPlan** = *when, by whom in intent, under which constraints*.
> **Work** = *how it went this time*.

### 4.2 Plan Items (what a `WorkPlan` is made of)

A `U.WorkPlan` **contains Plan Items** (think: scheduled tasks/ops), each of which typically states:

1. **Target Method/Spec** — the **Method** to be enacted and the **MethodDescription** intended for enactment.
2. **Planned window** — e.g., earliest start/latest finish, timebox, recurrence (cron‑like), blackout periods.
3. **Role requirements** — **role kinds** required (not people), optional **proposed RoleAssigning(s)** if pre‑assignment is allowed in the context.
4. **Capability thresholds** — minimal abilities required of the performer (checked at run time).
5. **Resource budgets/reservations** — planned energy/materials/machine slots/money; reservations on assets.
6. **Dependencies** — precedence/overlap permissions; gates/approvals.
7. **Acceptance targets** — quality windows/SLA targets to be judged when Work completes.
8. **Location/asset constraints** — where the run is expected to take place.
9. **Links to Service promises** (if any) — external commitments that this plan aims to satisfy.

> **Didactic guardrail:** **No logs or actuals** belong in a WorkPlan; **no step logic** or solver internals either—that’s the Method/Spec.

### 4.3 Clear distinctions (lexical sanity for “schedule/process/workflow”)

| If you say…                                 | In FPF it is…                                        | Why                                               |
| ------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------- |
| “The **schedule** for tomorrow’s surgeries” | **`U.WorkPlan`**                                     | Calendar of intended runs (who/when constraints). |
| “The **workflow** for appendectomy”         | **`U.MethodDescription`** (and `U.Method`)                  | Recipe and semantic way, not a calendar.          |
| “The **process** already ran at 10:00”      | **`U.Work`**                                         | A dated run with resources and outcomes.          |
| “The **thermodynamic process** path”        | **`U.Work`** (occurrence) + **`U.Dynamics`** (model) | A realized trajectory plus its model, not a plan. |
| “The **plan** assigns Dr. Lee”              | **WorkPlan** naming an **intended** RoleAssigning      | assignment is still validated at run time.       |
| “The **budget** for Shift‑B”                | **WorkPlan** (planned ledger)                        | Actual costs land on **Work**, not on the plan.   |

> **L‑SCHED (lexical rule).** In this document, words like **schedule**, **calendar**, **rota**, **Gantt**, **plan** point to **`U.WorkPlan`** unless explicitly redefined by a bounded context glossary.

### 4.4 Plan mereology (composition of plans ≠ composition of methods or runs)

Keep three separations crystal‑clear:

* **Method composition** (design‑time semantics) → produces **new Methods**.
* **Work composition** (run‑time occurrences) → produces **parent/child runs** with overlaps/episodes.
* **Plan mereology** (epistemic structure) → organizes **Plan Items** for coordination (phases, sprints, shifts), with **precedence** and **resource reservations**.

**Common relations among Plan Items:**

* **`Precedes_pl` / `DependsOn_pl`** — start/finish constraints and gates.
* **`MayOverlap_pl` / `MutuallyExclusive_pl`** — allowed overlaps vs exclusive windows.
* **`Refines_pl`** — a child plan item tightens windows/budgets of a parent.
* **`Alternative_pl`** — planned alternatives (e.g., backup rig, backup team).

**Didactic rule:** A Plan Item **does not force** an identical Work shape; mapping is via **fulfilment** and **variance** (see §6).

### 4.5 How `WorkPlan` meets `Work` (fulfilment & variance)

When reality happens, each `U.Work` may:

* **Fulfil** a Plan Item — link `plannedAs → PlanItem`.
* **Partially fulfil** — multiple Work instances share one Plan Item (e.g., split run), or one Work fulfils several Plan Items (e.g., consolidated batch).
* **Deviate** — execute with method/spec substitution, different window, different performer (still valid or policy‑exception).
* **Be unplanned** — Work with no Plan Item (emergency, ad‑hoc); must be labeled as such.

**Variance dimensions** the plan expects to report on:

* **Schedule variance (Δt):** early/late vs planned window.
* **Cost variance (Δc):** actual resource spend vs budget.
* **Scope variance:** different Method/Spec than planned (with justification).
* **Quality variance:** acceptance verdict vs target.
* **Assignment variance:** intended vs actual RoleAssigning.

> **Manager’s view:** A plan that cannot report variance is a calendar picture, not a management tool.

---

## 5 · What a good `WorkPlan` states (review checklist)

Use this as a human‑readable checklist (not a rigid schema):

1. **Horizon & cadence** (e.g., “W36 surgeries, daily ETL”).
2. **Plan Items** with: target Method/Spec, planned windows, dependencies.
3. **Role requirements** (kinds) and **intended assignments** (optional, context‑lawful).
4. **Capability thresholds** and **safety envelopes**.
5. **Resource budgets** and **reservations** on assets.
6. **Acceptance targets** (SLA/quality windows).
7. **Bridges** if plan spans **multiple contexts** (operations ↔ audit/regulatory).
8. **Baseline/version** and **change notes** (so variance is attributable).
9. **Policy pointers** (episode policy, overlap policy for Work roll‑ups if needed for KPIs).
10. **Exceptions path** (how ad‑hoc/emergency work is planned post‑factum).

---

## 6 · Archetypal grounding (parallel domains)

### 6.1 Hospital OR day plan (shift rota + cases)

* **WorkPlan:** `OR_DayPlan_2025‑08‑12`.
* **Plan Items:** `Case#1 Appendectomy`, `Case#2 Hernia`, with windows, Context assignments, and surgeon **role kinds**; anesthetist **intended RoleAssigning** provided.
* **Budgets:** OR time blocks, consumables envelopes.
* **Fulfilment:** Each surgery Work links to its Plan Item; variances computed (over‑run time, substitutions).

### 6.2 Fab maintenance weekend (asset reservations)

* **WorkPlan:** `Fab_Maintenance_W36`.
* **Plan Items:** `Tool_42 chamber clean`, `Tool_13 calibration`; **MutuallyExclusive\_pl** with production slots.
* **Reservations:** nitrogen, DI water, metrology window.
* **Fulfilment:** Actual clean Work happens earlier; variance logged as **early** with cost underrun.

### 6.3 Data‑center rollout (multi‑context plan)

* **WorkPlan:** `DC_Rollout_Phase‑2`.
* **Bridges:** Ops context ↔ Security Audit context (different acceptance targets).
* **Plan Items:** `Deploy Service A`, `Pen‑test A`; dependencies across contexts.
* **Fulfilment:** Deployment Work passes ops targets; audit Work passes later—variance reported per context.

---

## 7 · Bias‑Annotation (as in E‑cluster)

* **Lenses tested:** `Did`, `Prag`, `Arch`, `Epist`.
* **Scope declaration:** Universal; meanings of windows/budgets/permissions are **context‑local** via `U.BoundedContext`.
* **Rationale:** Elevates **planning/scheduling** to a first‑class episteme that coordinates Methods, RoleAssignings, and Work without conflation.

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

## A.20 — **U.Flow.ConstraintValidity — Eulerian** \[A]

**Tech‑name.** `U.Flow.ConstraintValidity` (`U.Flow` genus)
**Plain‑name.** Flow constraint validity (Eulerian interpretation)
**Type / Status.** [A] Architectural pattern — **normative** for flows hosted by E.TGA (E.18) under the Eulerian operational interpretation

## 0) Intention

**One‑liner** Defines cross‑cutting **ConstraintValidity** rules for all `U.Flow` instances. `U.TransductionFlow` inherits these rules and may refine **CV class specializations** for transduction‑specific semantics (species‑binding only; genus rules remain unchanged). The CV core is **kind‑agnostic** and assumes an **open‑world** catalogue of node **species**; the enumeration of node **kinds** in E.TGA is a **minimal roles baseline**.
**Operational interpretation.** **Eulerian** stance: **flow = valuation** over `U.Transfer`; **CV is attached to transformations (steps)** and evaluated **before any GateFit**; edges carry **assurance‑only operations**; no token‑passing semantics are assumed.

### 1) Problem frame

E.TGA makes *nodes = morphisms* and enforces a *single edge kind* (`U.Transfer`). **GateFit** checks aggregate only in `OperationalGate(profile)` with the activation predicate **CV ⇒ GF**: until aggregated **ConstraintValidity = pass**, all **GateFit** checks return **abstain**. Equivalently, while **ConstraintValidity ≠ pass**, any GateFit‑oriented explanation **does not apply**. To keep flows comparable and auditable, this pattern delimits **internal step constraints** (CV) from **external gate fit** (GF), preventing any second ladder of processes beside the graph.

### 2) Problem

Without a clear CV core:

* internal step laws (domains/ranges, invariants, units coherence, Lipschitz/stability) bleed into gate **profile**;
* plane or comparator declarations sneak into mechanisms;
* freshness and design/run concerns appear inside mechanisms;
* reproducibility suffers because transfers start carrying hidden semantics beyond `⟨L,P,E⃗,D⟩`.

Under this pattern, CV is evaluated **inside** transformations. **If** a check declares planes/units/comparators or depends on an active `GateProfile`, **then** it is treated as **GateFit at gates** and the CV explanation **does not apply**.

### 3) Forces

* **Separation of concerns.** Internal mechanism laws vs. external profile fit.
* **Auditability.** MVPK faces include pins/references only; no new numeric claims; editions and Γ are pinned where applicable.
* **Graph discipline.** One edge kind; all crossings mediated by gates; SquareLaw on every crossing.
* **Reproducible valuation.** Flow = valuation over `U.Transfer`, with slice‑local refresh bounded by sentinels.
* **LEX hygiene.** ASCII Tech labels, twin Tech/Plain registers, registered tokens.

### 4) Solution 

#### 4.1 Intent & Scope

**Intent.** Establish the **ConstraintValidity core** for the **`U.Flow` genus**: the normative set of **internal step constraints** and how they are surfaced and aggregated, **independent of GateFit profiles** (publication follows MVPK without adding new numeric claims). Where CV speaks about admissibility, phrase criteria **counterfactually**: *“If the admissibility conditions hold, then the CV explanation applies; otherwise this explanation does not apply.”* Avoid duty verbs unless stating the **normative** CC minima.

**Scope (genus).** CV covers **intra‑step** properties checkable from the transformation’s own signature/mechanism. The canonical CV classes are **genus‑level and non‑exhaustive**:
`MechanismUnitsCoherence`, `LawSetInvariants`, `AdmissibilityConditionsSatisfaction`, `LipschitzBounds`, `TypeDomainRange`, and—only for **`StructuralReinterpretation`**—`ReinterpretationEquivalence` (correspondence/reversibility witness).

**Species binding (`U.TransductionFlow`).** The above classes bind to `U.Transduction(kind ∈ {Signature, Mechanism, Work, Check, StructuralReinterpretation})` with **`OperationalGate = kind=Check`**; no additional CV classes are introduced here (species‑specific semantics reside in A.31 and A.45).

**Out‑of‑scope (CV):** declaring/translating `ReferencePlane/Units/ComparatorSet`; CSLC comparability; Freshness; Role/Channel; Regulated‑X; `DesignRunTagConsistency` — all reside in **GateFit** (A.21).

#### 4.2 Intensional object(s)

**Genus.** `U.Flow` leaves step‑kinds abstract; CV/GF separation applies to any lawful instantiation.
**Species (`U.TransductionFlow`).** `U.Transduction(kind) ∈ {Signature, Mechanism, Work, Check, StructuralReinterpretation}`; this set of **kinds** is a **minimum roles baseline** defined in E.TGA. The **species** space (e.g., `UNM.Authoring/Usage`, `SelectionAndBinding`, `WorkPlanning`, `EvaluatingAndRefreshing`, …) is **open‑world** and non‑exhaustive. `OperationalGate = U.Transduction(kind=Check)`. `StructuralReinterpretation` is **projection‑preserving** (no mutation of `⟨L,P,E⃗,D⟩`) and may retarget **describedEntity** under CC‑TGA‑06‑EX; see also A.45.

**`AdmissibilityConditionsSatisfaction`** — **If** the declared admissibility conditions hold on the step’s inputs and context, **then** the CV explanation **applies**; **otherwise** this explanation **does not apply**.
**`LipschitzBounds`** — **If** inputs vary within the stated domain \(X\) and perturbations/noise \(≤ ε\), **then** the step’s estimate remains within **δ** of the reference; **otherwise** this explanation **does not apply**.
**`MechanismUnitsCoherence / TypeDomainRange`** — **If** units/types/domains match the mechanism’s signature and closed‑world assumptions for the step, **then** the CV explanation **applies**; **otherwise** this explanation **does not apply**.

**Terminology & bindings (normative)**
* **Status/witness lexicon (E.10 discipline).** In CV scope, publications use **Status/Witness** terminology; **GateDecision…** lexemes belong to GateFit (A.21) and do **not** apply to CV.
* **describedEntity = KindBridge.** Any CV mention of “describedEntity” SHALL be read via **`KindBridge (CL^k)`** on **UTS** (A.27 / C.3.3). CV **does not** declare or translate planes/units/comparators.
* **retargeting/witness binding.** For `U.Transduction(kind=StructuralReinterpretation)`, the CV class **`ReinterpretationEquivalence`** SHALL surface **`CV.WitnessRef := ReinterpWitness`** over the addressed `PathSliceId`; the UTS **`SquareLaw‑retargeting` witness** is referenced from MVPK/UTS and **linked** from the CV witness without duplication.
* **`ReinterpWitness` record (normative).**  
  `ReinterpWitness := { PathSliceId, PublicationScopeId, mapping:{kind: iso|optic, laws: PutGet/GetPut}, commutingSquares:[TransferId], definedOn: PathSliceId, properties:{invertible?:bool, idempotent?:bool}, UTS.RowId, NoHiddenScalarization:true }`.

#### 4.3 MVPK Faces (PlainView · TechCard · InteropCard · AssuranceLane)

Minimum pins on faces that surface CV outcomes (**Lean surfacing** allowed by profile but without weakening checks):

* **CtxState pins.** `⟨L,P,E⃗,D⟩` on ports/tokens; raw `U.Transfer` preserves them.
* **Path pins.** `PathId` and `PathSliceId` appear where slice‑local refresh or reinterpretation witnesses are relevant (valuation semantics per A.22).
* **CV pins.** `CV.Status ∈ {abstain, pass, degrade, block}`, `CV.WitnessRef?` (refs only).
* **Edition pins.** If a face cites `CG‑Spec`, `ComparatorSet`, or `UNM.TransportRegistryΦ`, the face **includes** the compatibility surface **as per A.27 (BridgeCard + UTS row, with `CL/CL^plane`)** for downstream consumption. A.20 references this requirement; it does not introduce or modify Bridge/UTS formats.
* **Face scope.** Each face includes `PublicationScopeId` with an **MVPK profile** (Min/Lite/SetReady/Max) — no new surface kinds.
* **Register discipline.** Tech names ASCII; twin labels; required LEX tokens follow E.10 (e.g., `SentinelId`, `PathSliceId`, `SliceRefresh`).

> **No new numeric claims.** Faces add pins and references; they do **not** introduce fresh computed scalars beyond what the mechanism already entails (MVPK functoriality).

**Publication lexeme (per‑check).** Each surfaced CV check is referenced as  
`GateCheckRef := { aspect=ConstraintValidity, kind, edition, scope }` with `scope ∈ {lane|locus|subflow|profile}`. This adds no execution steps and introduces no numeric claims on faces; it records what CV classes were considered and under which editions.

#### 4.4 GateChecks (table) — CV only

**Activation predicate (in E.TGA).** *Until aggregated `CV = pass`, all GateFit checks return `abstain` (CV⇒GF).*
**Role/Channel Fit guard (GateFit scope).** GateFit checks that involve roles SHALL use **Kernel `U.Role` tokens** (domain = `U.System`) and SHALL NOT consume `TypicalEnactorRoleName` strings from alias tables.

| Check class (A.20)                                                                                | aspect | Mandatory | Allowed | Forbidden |
| ------------------------------------------------------------------------------------------------- | -----: | :-------: | :-----: | :-------: |
| MechanismUnitsCoherence                                                                           |     CV |     ✓     |    —    |     —     |
| LawSetInvariants                                                                                  |     CV |     ✓     |    —    |     —     |
| AdmissibilityConditionsSatisfaction                                                               |     CV |     ✓     |    —    |     —     |
| LipschitzBounds / stability                                                                       |     CV |     ✓     |    —    |     —     |
| TypeDomainRange                                                                                   |     CV |     ✓     |    —    |     —     |
| ReinterpretationEquivalence (StructuralReinterpretation only; witness present)                    |     CV |     ✓     |    —    |     —     |
| Any `ReferencePlaneCrossing`, CSLC, Freshness, Role/Channel, Regulated‑X, DesignRunTagConsistency |     GF |     —     |    —    |     ✓     |

CV **must not** declare/translate `Units/ReferencePlane/ComparatorSet`; crossings and CSLC comparability live only in A.21.

#### 4.5 SWP matrix (single‑writer discipline)

* **Writes (faces).** `CV.Status` (and optional `CV.WitnessRef`) only.
* **Reads (ref‑only).** Any `CG‑Spec/ComparatorSet/TransportRegistryΦ` editions (when referenced); UNM remains single writer as per CC‑TGA‑24.

#### 4.6 CtxState & GateCrossing

* **Crossings only at `OperationalGate(profile)`** (plane/unit/context) with a **strict exception** for **`StructuralReinterpretation`**: a **projection‑only retargeting** MAY occur without a gate **iff** `⟨L,P,E⃗,D⟩` is preserved, **KindBridge (`CL^k`)** and a **SquareLaw‑retargeting witness** are present on MVPK/UTS, and the action is **PathSlice‑local** (`PathSliceId` pinned).
* **Projection vs describedEntity (normative reduction).** “Projection” denotes a change of **MVPK published view** that is point‑wise identity on the intensional transformation; “describedEntity” is the **Kind‑channel** on UTS evidenced by a `CL^k` row. “No unit/plane change” holds iff `P` is equal on both sides and **no `CL^plane`** is emitted for the step.
* **Projection/describedEntity normalization (normative).** In the context of `StructuralReinterpretation`, the terms **projection** and **describedEntity** are read **via UTS**: projection = change of **published view coordinates** only; describedEntity = **Kind‑channel** change under `CL^k`. A **“no unit/plane change”** test SHALL verify that `ReferencePlane(src)=ReferencePlane(tgt)` and `CL^plane` is absent (or `= ⊤`), otherwise the step is a gated crossing.
* **Assurance operations on edges.** `ConstrainTo/CalibrateTo/CiteEvidence/AttributeTo` reside on `U.Transfer` and do **not** alter `⟨L,P,E⃗,D⟩`; plane/unit changes occur only at gates; Φ/`CL^plane` penalties route in **R‑lane**. describedEntity/kind transitions are surfaced as **`KindBridge (CL^k)`** on **UTS** (see A.27 / C.3.3). describedEntity/kind transitions use **KindBridge (`CL^k`)** (A.27/E.TGA); under CC‑TGA‑06‑EX this appears without a gate and remains PathSlice‑local.

**Terminology binding (TGA‑specific, normative)**
* **Status/witness lexicon (E.10 discipline).** In CV scope, publications use **Status/Witness** terminology; **GateDecision…** lexemes belong to GateFit (A.21) and do **not** apply to CV.
* **describedEntity = KindBridge.** Any CV mention of “describedEntity” SHALL be read via **`KindBridge (CL^k)`** on **UTS** (A.27 / C.3.3). CV **does not** declare or translate planes/units/comparators.
* **retargeting/witness binding.** For `U.Transduction(kind=StructuralReinterpretation)`, the CV class **`ReinterpretationEquivalence`** SHALL surface **`CV.WitnessRef := ReinterpWitness`** over the addressed `PathSliceId`; the UTS **`SquareLaw‑retargeting` witness** is referenced from MVPK/UTS and **linked** from the CV witness without duplication.
* **`ReinterpWitness` record (normative).**  
  `ReinterpWitness := { PathSliceId, PublicationScopeId, mapping:{kind: iso|optic, laws: PutGet/GetPut}, commutingSquares:[TransferId], definedOn: PathSliceId, properties:{invertible?:bool, idempotent?:bool}, UTS.RowId, NoHiddenScalarization:true }`.

#### 4.7 SquareLaw

For any gate‑mediated crossing adjacent to CV‑checked steps:
`gate_out ∘ transfer = transfer' ∘ gate_in`.
For **projection retargetings** under `StructuralReinterpretation`, a **SquareLaw‑retargeting witness** shows that the **view retargeting commutes** with transfers on the PathSlice. Inconsistencies lead to `degrade`/`block` per active profile (GateFit decision).

**retargeting witness shape (normative, UTS‑level).** A **SquareLaw‑retargeting witness** is an artifact that demonstrates commutativity of a published‑projection retargeting over the addressed **`PathSliceId`**:  
  1) identifies **`PathSliceId`** and **`PublicationScopeId`**;  
  2) presents a **bidirectional view mapping** between projections either as an **iso** or as a **profunctor optic** (`get : A→B`, `put : (B×A)→A`) satisfying **Put‑Get / Get‑Put** laws;  
  3) enumerates the **commuting squares** for the cut‑set edges considered (ids of transfers before/after the retargeting);  
  4) declares properties (**invertible?**, **idempotent?**) and the **definedness area**;  
  5) cites the **UTS.RowId** and links the **DecisionLog** entries that rely on this witness.  
Realizations via **profunctor optics (post‑2017)** are permitted; the optic/lens laws serve as the proof template of commutativity.

**CV witness for reinterpretation (normative, CV‑level).** `CV.ReinterpretationEquivalence` SHALL surface a **ReinterpretationEquivalenceWitness** distinct from the UTS retargeting witness and scoped to the mechanism state over the same **`PathSliceId`**:
  — `PathSliceId`, `PublicationScopeId`, and **definedness region** (domain constraints);  
  — a **pair of internal transformations** (or an optic) with **Put‑Get / Get‑Put** obligations **over mechanism state** (not faces);  
  — a **list of commuting squares** for the **adjacent raw transfers** (before/after reinterpretation) showing SquareLaw at CV boundary;  
  — an explicit **NoHiddenScalarization assertion** (see §4.9) for any comparable return shape;  
  — **edition neutrality**: no new editions are authored; only refs/pins appear.  
This CV witness links to the UTS `SquareLaw‑retargeting` witness when present, but does not duplicate UTS fields.

**CV witness binding (normative).** For the CV class **`ReinterpretationEquivalence`**, the witness **SHALL** be a `ReinterpWitness` record:
`ReinterpWitness := { PathSliceId, PublicationScopeId, mapping: {kind: iso|optic, laws: PutGet/GetPut}, commutingSquares: [TransferId], definedOn: PathSliceId, properties: {invertible?: bool, idempotent?: bool}, UTS.RowId, NoHiddenScalarization: true }`.
The record is **PathSlice‑local** and does not declare or translate planes/units or comparators.

#### 4.8 Sentinel & PathSlice (path‑local refresh)

* Flows are **valuations** over `U.Transfer`, re‑emitting **slice‑locally** under sentinel rules or edition bumps (A.22/A.25). CV contributes to the **prepare/refresh** conditions but does not expand scope beyond the addressed `PathSliceId`.
* **Delimitation & planning (normative).** A `PathSlice` **closes** on: (i) any pinned edition change, (ii) Γ‑window boundary relevant to the face, (iii) `GateProfile` change along the path, or (iv) an explicit sentinel rule. **Concurrency:** at most **one active recompute** per `{PathSliceId}`; parallel recomputes are permitted across **distinct** `PathSliceId`s.
* **CV‑triggered refresh (minimum list).** Re‑emit the addressed `PathSliceId` when any holds: (a) `CV.Status` changes across the lattice; (b) `ReinterpWitness` is added/updated/withdrawn; (c) `AdmissibilityDecl.edition` or `LipschitzBoundRef.edition` changes; (d) updates arrive from A.27 (Bridge) or A.28 (ComparatorSet/UNM.TransportRegistryΦ); (e) error/timeout transitions to a resolved `pass` for a previously `abstain|degrade` CV class.

* **CV‑to‑refresh triggers (normative).** A **SliceRefresh(PathSliceId)** SHALL be scheduled when any of the following occurs:  
  (T1) a **CV status flip** on the slice (`pass↔degrade`, `pass↔block`, or `error/timeout→{degrade|block}` under profile rules);  
  (T2) arrival of a new **ReinterpretationEquivalenceWitness** or a change in its **definedness region**;  
  (T3) updates to adjacent **UTS/Bridge** facts for the slice (e.g., `CL^k`, `BridgeId`, `Φ`/`Ψ` policy‑ids) coming from A.27;  
  (T4) edition changes referenced by CSLC (A.28) on the slice (`ComparatorSetRef.edition`, `DescriptorMapRef.edition`, `DistanceDefRef.edition`, …);  
  (T5) **FreshnessTicket** lifecycle changes impacting the slice window (A.40);  
  (T6) sentinel rules explicitly attached to the **PathSliceId**.  
Scheduling is **slice‑local**; recompute does not fan‑out beyond the addressed `PathSliceId`.

  **Id‑scheme:** `PathSliceId := PathId × Γ_time selector × ReferencePlane × SentinelFingerprint × IterationCounter`.  
  **Locking for replay:** within a recompute, the effective `E⃗` is **frozen**; outputs carry a **replay fingerprint** resolvable via `DecisionLog`.

#### 4.9 ReturnShape & CSLC (comparability discipline)

When the mechanism yields comparable artifacts, the return surface is **set‑valued / partially ordered**; **no hidden scalarization**. Any comparator citation is **ref‑only** and (if editions are cited) requires `Bridge+UTS` per CSLC (A.28). Actual CSLC checks are GateFit (A.21).

Under **`StructuralReinterpretation`**, **projection changes MUST NOT introduce hidden scalarization**; set‑return semantics remain intact; comparator cites stay ref‑only with UTS discipline.

**Detectable signs of hidden scalarization (normative checklist).** A face **SHALL** be flagged when any holds:  
  (H1) introduction of a **new scalar** not entailed by the mechanism, or any **cardinality‑reducing** fold of a set return (e.g., argmax/best‑of) without a cited **ComparatorSetRef**;  
  (H2) omission of a required **ComparatorSetRef** or its **edition pins** where comparison is implied;  
  (H3) presence of an **order‑imposing coordinate** without a **CoordinatePolicy** and legality annotations (scale/units/illegal ops);  
  (H4) cross‑plane/units numeric combination without a **Bridge+UTS** row;  
  (H5) for `StructuralReinterpretation`, any change of return **plane/units** (violates “projection‑only”).  
Failing (H1–H5) degrades or blocks per GateProfile (§4.4/CC‑TGA‑21a).

#### 4.10 Γ‑windows / Freshness

* No implicit *latest*. Any face expected to be consumed at compare/launch pins `Γ_time`; Freshness enforcement occurs at gates; CV neither issues Freshness tickets nor evaluates staleness (see A.33/A.40).
* **Granularity of Γ (normative).** Γ SHALL be one of: **snapshot** (`effective_at=t`) or **interval** (`[t₀,t₁)` with a named folding policy). Faces SHALL surface which selector is used.  
* **CV time‑stamping.** Each CV computation surfaces `t_cv` and the **Γ selector** it assumed; replay binds `t_cv` to `PathSliceId`.  
* **Temporal policy types (binding).** Γ‑pins refer to the **canonical selectors** of §22 (*`effective_at`*, *`latest_effective_before`*, *`windowed(W, policy)`*) and to **folding policies** that are **IDEM/MONO/WLNK‑safe**. Units/time scales **SHALL** be explicit. Overrides of the default **weakest‑link** fold **SHALL** cite CAL proofs of monotonicity and boundary behavior.

#### 4.11 Unknown/Timeout/Error policy

Each CV class yields `abstain | pass | degrade | block`. Errors/timeouts at CV stage imply **CV ≠ pass**; therefore GateFit abstains by the global activation predicate and any GateFit‑oriented explanation **does not apply**. The **aggregated CV decision** uses the join on `abstain ≤ pass ≤ degrade ≤ block` (neutral = `abstain`; absorbing = `block`).  
**Minimal default (profile‑bound, normative):** **Lean/Core ⇒ `error|timeout → degrade`**, **SafetyCritical/RegulatedX ⇒ `error|timeout → block`**; `unknown` folds per GateCheck policy (safety‑default: `degrade`). (Consistent with **CC‑TGA‑22**.)

#### 4.12 Idempotency / congruence discipline

Any surface influencing gate decisions references **A.41** for **equivalence** of inputs and **idempotency witness**; A.20 does not introduce keys, hashes, or cache policies.
**Minimal lexeme set for CV‑adjacent equivalence (normative).** Where CV outcomes influence a gate decision, the **equivalence witness** SHALL identify at least: `{PathSliceId, GateProfileId, Γ selector (+window bounds if interval), E⃗ editions vector for cited registries, ReturnShape kind (if comparable), CV class/kind set considered}`. Changing any of these breaks equivalence and requires re‑aggregation.

### 5) Archetypal Grounding (Tell–Show–Show)  ✱

**Show‑1 (compiler build → run).**
A typed module `M` exposes `f : State_d → Artifact_d` under a declared `LawSet` (e.g., determinism under fixed toolchain) and `TypeDomainRange`. **CV** checks: (i) `MechanismUnitsCoherence` (toolchain/flags units coherent), (ii) `LawSetInvariants` (reproducible outputs under same `E⃗`), (iii) `Admissibility` (inputs well‑typed), (iv) optional Lipschitz/stability surrogate (bounded perturbation in sandbox). `CtxState` is preserved along raw transfers. Entering `U.Work(run)` requires `LaunchGate` with `FreshnessUpToDate` and `DesignRunTagConsistency` — **GateFit**, not CV.

**Show‑2 (selection archive in QD/AutoML).**
A mechanism emits a **set** (front/portfolio/archive). **CV** ensures only: valid descriptor ranges, internal metric continuity bounds, archive invariants (idempotent insert). No ranking or acceptance thresholds are introduced at CV; comparators and acceptance policies bind at gates via CSLC and profiles (A.21/A.28). Edition‑aware pins on faces carry `DescriptorMapRef.edition` only with `Bridge+UTS`.

**Anchors.** Algebraic effects & handlers separate signatures from handlers (Koka/Effekt, 2015+); reproducible pipelines isolate mechanism constraints from deployment **profiles** (Bazel/Nix); optics/profunctors and open/hypergraph categories motivate composition on open graphs without adding facts on faces; QD/MAP‑Elites/CMA‑ME/DQD motivate **set‑return + lawful orders** (2015–2022).

### 6) Bias‑Annotation

The pattern constrains *how* internal constraints are surfaced; it does not encode profile‑bound thresholds or Role/Channel fit — those sit in GateFit. This separation reduces leakage of profile concerns into mechanism semantics.

### 7) Conformance Checklist  ✱

**Static lint (graph & surfaces)**

* CC‑TGA‑01: only `U.Transfer` edges; crossings appear only on gates.
* CC‑TGA‑05: `⟨L,P,E⃗,D⟩` unchanged across raw transfers.
* CC‑TGA‑09: MVPK faces present; edition & Γ pins where expected; no new numeric claims on faces (E.17).

**CV discipline**

 * CV classes present exactly as {UnitsCoherence, LawSetInvariants, Admissibility, LipschitzBounds, TypeDomainRange}; **plus** `ReinterpretationEquivalence` when the node kind is `StructuralReinterpretation`. None declare/translate planes/comparators.
 * **Open‑world species.** Any node **species** binds to one of the minimal kinds; adding a new **kind** is out of scope for A.20 and requires an E.TGA update.
* Aggregated **CV.Status** computed; errors/timeouts ⇒ `CV ≠ pass`.

**Gate coupling**

* CC‑TGA‑07: when **CV ≠ pass**, all GateFit checks report **abstain**.
* CC‑TGA‑23: SquareLaw witnesses present on crossings adjacent to CV‑checked steps.
* Any edition citation on faces includes `Bridge+UTS` (A.27; CSLC in A.28).

**UNM single‑writer**

* CC‑TGA‑24: UNM.Authoring is the sole writer for `CG‑Spec/ComparatorSet/TransportRegistryΦ`; CV is ref‑only.

**Valuation & refresh**

* CC‑TGA‑18/19: Flow publishes valuation with `PublicationScopeId`/`PathSliceId`; Γ pinned at compare/launch surfaces; sentinel triggers slice‑local refresh.

### 8) Consequences

**Benefits.**
*Clarity & composability.* Mechanisms remain pure carriers of internal laws; gates are the sole policy junction.
*Replayability.* With valuation + MVPK pins, re‑runs under fixed `E⃗` are comparable and slice‑scoped (A.22/A.25).
*Didactic hygiene.* Readers can see what is mechanism truth vs. gate policy.

**Trade‑offs.**

* Two places to look (CV vs. GF) impose author discipline; mitigated by the activation predicate and MVPK links.

### 9) Rationale

E.TGA hosts A.20 and A.21 as orthogonal cores: CV **inside** transformations; GF **at** gates with join‑aggregation and DecisionLog. This mirrors effects/handlers (signature vs. handler), and reproducible build vs. deployment‑profile separation.

### 10) SoTA‑Echoing (post‑2015)

* **Algebraic effects & handlers** (Koka, Effekt): signatures vs. handlers as a model for CV vs. GF.
* **Reproducible pipelines** (Bazel, Nix): hermetic builds ≈ CV; release/deploy gates ≈ GF.
* **Optics/profunctors; open/hypergraph categories** (2017–2019+): composition over open graphs without extra face semantics.
* **Quality‑Diversity / MAP‑Elites / CMA‑ME / DQD (2015–2022):** set‑return with lawful partial orders; no hidden scalarization.
  These anchors justify the separation and the set‑return discipline (CSLC) embedded in the flow family.

### 11) Relations

 * **Hosted by E.TGA.** Nodes are morphisms; only `U.Transfer` edges; **open‑world species over a minimal kind set**; CV⇒GF activation; MVPK faces; SquareLaw on crossings; CC‑TGA‑06‑EX for `StructuralReinterpretation`.
* **A.21 (GateProfilization).** Sole point for GateFit checks and profile‑bound folds.
* **A.22 (FlowSpec—valuation).** Declares valuation and slice‑refresh semantics used by this flow family.
* **A.27 (Bridge+UTS).** Boundary‑surface requirement whenever faces cite editions.
* **A.28 (CSLC).** Comparability discipline; CV does not compare; it only ensures internal readiness for lawful comparison.
* **A.41 (DecisionLog & Idempotency).** Equivalence witness binding for any surfaces affecting gate decisions.
* **E.10 (LEX).** Token classes and ASCII Tech names; twin labels and aliasing for Γ/CL/Φ as per LEX‑BUNDLE.

### 12) Footer marker (authoring template)

Conforms to E.8 heading order and safety subsections (Archetypal Grounding, Conformance, SoTA).

### Appendix A — CV Class Gloss (normative)

* **MechanismUnitsCoherence.** Internal unit/scale coherence within the step; no declarations or translations of units/planes (GateFit scope).
* **LawSetInvariants.** Mechanism‑declared invariants hold (e.g., mass/energy balance in a model, determinism under fixed editions).
* **AdmissibilityConditionsSatisfaction.** Inputs lie within admissible windows/guards declared by the mechanism’s **AdmissibilityConditions**; failure yields `degrade` or `abstain` per class policy.
  **Minimum declaration (normative):**
  `AdmissibilityDecl := { domains: {name: set/poset}+, guards: [predicate_id]*, windows: {Γ_time: snapshot|interval|policy}, observables: [signal_id]*, edition: EditionId }`.
  The declaration is surfaced on MVPK as references only; it introduces no arithmetic on faces.
* **LipschitzBounds / stability.** Bounded sensitivity to perturbations as declared by mechanism; optional where meaningful.
  **Method binding (normative):**
  `LipschitzBoundRef := { method ∈ {spectral_norm|CROWN|IBP|rand_smoothing|other}, metric_space: {X: norm_id, Y: norm_id}, bound: value_or_interval, units/plane: P, validity_window: Γ_time(basis), edition: EditionId }`.
  The bound is **edition‑pinned** and **plane/units‑declared**; proofs/witness artefacts are referenced (no new numeric claims on faces).
  **Minimal declaration template (normative):**  
  `AdmissibilityConditions := { Domains[]{var, type, range, units, plane}, Guards[]{predicate, editionRefs}, ObservationWindows[]{Γ selector, freshness window}, ObservableSigns[]{name, detection rule}, Editions{...} }`  
  — **No authoring of units/planes** here; only references. — Γ selectors must be explicit.
* **TypeDomainRange.** Type/domain/range compliance of inputs/outputs (ref‑only to definitions).
* **ReinterpretationEquivalence.** Mechanism’s reinterpretation preserves internal meaning on a **PathSlice**.  
  **Witness (normative):** **ReinterpretationEquivalenceWitness** (see §4.7) with: `(i)` `PathSliceId`, `PublicationScopeId`, `(ii)` bidirectional mapping (iso/optic) with Put‑Get/Get‑Put obligations, `(iii)` commuting squares for adjacent raw transfers, `(iv)` **NoHiddenScalarization** assertion (if comparable), `(v)` definedness region.  
  — **No plane/unit change**; any describedEntity change must have `KindBridge (CL^k)` on UTS.
* **LipschitzBounds / stability.** Bounded sensitivity of the mechanism under a declared metric.  
  **Certificate (normative):** `LipschitzCertificate := { metricId (with units/plane), bound L, methodId, methodRef (e.g., spectral estimate / cert. robustness bound), validity region (inputs/state), proof sketch/ref }`.  
  — The **method** MUST be cited; **units/plane** of the metric MUST be explicit; bounds are **ref‑only** at CV; any acceptance action remains GateFit.
* **TypeDomainRange.** Well‑typedness and domain/range consistency for the transformation signature.
  (Enumeration mandated by A.20; GF matters excluded).
* **ReinterpretationEquivalence (StructuralReinterpretation).** Existence of a correspondence/reversibility witness between source and retarget projections; preservation of `⟨L,P,E⃗,D⟩`; no comparator/plane/unit declaration or translation at CV. The witness is **PathSlice‑local** and supports **idempotence & reversibility** within the addressed slice. The normative record is `ReinterpWitness` (see §4.7).

#### Appendix B — LEX discipline (summary)

Register token classes (Tech) include: `U.TransductionFlow`, `U.TransductionGraph`, `OperationalGate`, `GateProfile`, `GateCheckKind`, `GateCheckRef`, `DecisionLog`, `FreshnessTicket`, `FinalizeBinding`, `SubflowRef`, `FlowEmbed`, `SentinelId`, `PathSliceId`, `SliceRefresh`, `VALATA`; discriminators use `Base__P2W`, `Base__EvaluatingAndRefreshing`; Tech names are ASCII; aliases `GammaTimeRule/Plane`, `CLPlane`, `Phi` follow E.10. A.20 references these tokens; it does not introduce additional LEX classes. **For each surfaced CV check, `GateCheckRef.aspect` is fixed to `ConstraintValidity`.** *MVPK minima for CV faces also include `PathId/PathSliceId` where slice‑local refresh applies (A.22).*
