## C.17 — **Creativity‑CHR** — Characterising Generative Novelty & Value 

### 0 · Status, Placement & Exports

**Status.** Architheory specification (**CHR**) — normative where stated.
**Depends on.** A‑kernel (A.1–A.15), **CHR‑CAL** (C.7), **MM‑CHR** measurement infrastructure (C.16), **KD‑CAL** and **Sys‑CAL** for carriers and holons, **Decsn‑CAL** (utility), **Norm‑CAL** (constraints/ethics).
**Coordinates with.** **B.5.2.1 NQD** (abductive generator) for search instrumentation, **Agency-CHR** (C.9) for agential capacity, B-cluster trust/assurance (B.3), Canonical Evolution Loop (B.4), Role Assignment & Enactment Cycle (Six-Step) (F.6) and Naming Discipline for U.Types & Role Names (F.5).
**Guard‑rails.** Obeys E‑cluster authoring rules (Notational Independence; DevOps Lexical Firewall; Unidirectional Dependency).

**What this architheory provides (exports):**

This architheory exports **Characteristics** and measurement templates **only**. It **does not** export any Γ\_\* operators, portfolio composition rules, or selection/scalarization policies; those live in **C.18 NQD-CAL** and **C.19 E/E-LOG** (or **Decsn-CAL** for decision lenses). A Context _publishes_ the measurement space and admissible policies; a decision is taken by an _agent in role_ using a _named lens_ within that space.

* **`U.CreativitySpace`** — a **CharacteristicSpace** (CHR) with named **Characteristics** and scale metadata for evaluating creative work/outcomes **inside a `U.BoundedContext`**.
* **`U.CreativityProfile`** — a vector of coordinates in `U.CreativitySpace` attached by a **`U.Evaluation`** to a specific **Outcome** (usually an `U.Episteme` produced by `U.Work`).
* **Core Characteristics (kernel nucleus; Context‑extensible):**
1. **`Novelty@context`** — distance from a **`ReferenceBase`** in the current Context/time window; ∈ \[0, 1].
2. **`Use‑Value`** *(alias: `ValueGain`)* — measured or predicted improvement against a **declared objective**; interval/ratio scale per Context.
3. **`Surprise`** — negative log‑likelihood under a **GenerativePrior**; bits or nats.
4. **`ConstraintFit`** — degree of **must‑constraint** satisfaction (Norm‑CAL / Service acceptance); ∈ \[0, 1].
5. **Diversity_P (portfolio-level)** — coverage/dispersion (set-level). **Illumination** is a **report-metric over Diversity_P** (coverage/QD-score summaries). It is **report-only** and **never** part of the primary dominance test.
6. **`AttributionIntegrity`** — provenance/licensing discipline for lawful, transparent recombination; ∈ \[0, 1].
7. **`FamilyCoverage`** — (count, polarity ↑, scope=portfolio, unit=families, provenance: F1‑Card)
8. **`MinInterFamilyDistance`** — (ratio [0,1] or metric units, polarity ↑, scope=portfolio, DistanceDef@F1‑Card)
9. **`AliasRisk`** —  (ratio [0,1], polarity ↓, diagnostic; drop if dSig ≥3/5 characteristics collide)
10. **`U.DomainDiversitySignature (dSig)`** — 5‑tuple over discrete characteristics **[Sector, Function, Archetype, Regime, MetricFamily]**  attached to each `U.BoundedContext`. Used for **Near‑Duplicate** diagnostics and `AliasRisk`. Policy: flag as Near‑Duplicate when ≥3 characteristics match; see F.1 invariants and SCR‑F1‑S08..S09. 
11. **Note (AliasRisk binding).** `AliasRisk` MAY be computed using `dSig` collision diagnostics; a Context MUST declare the collision rule and policy id in DescriptorMap provenance when AliasRisk is reported.

* **Supporting types (linking points):**

  * **`U.ReferenceBase`** — the domain‑local corpus (by Context & time window) used to compute `Novelty@context`.
  * **`U.SimilarityKernel`** — a declared similarity metric class for the Context (text/image/design/code/etc.), with invariance notes.
  * **`U.GenerativePrior`** — a predictive model over the Context’s artifacts/behaviours used to compute `Surprise`.
  * **`U.CreativeEvaluation`** — a specialisation of `U.Evaluation` that yields a `U.CreativityProfile` and the Evidence Graph Ref.
  * **`EffortCost`** *(advisory)* — resource outlay to achieve the outcome; from WorkLedger (Resrc‑CAL). *(For normalization and planning; not itself “creativity.”)*


* **Operators (first tranche):** `composeProfiles` (set → portfolio), `dominates` (partial order in space), `frontier` (Pareto set), `normaliseByEffort`. *(Formal laws introduced in Quarter 2.)*
* **Relations (informative; not exported):** dominance relation (partial order in the space), frontier predicate (Pareto set), portfolio composition view. *C.17 exports no operators; these are mathematical relations only.*
* 
> **Scope note.** This architheory **does not** define who is “a creative person.” It characterises **creative outcomes and episodes** as **observed in Work** and **expressed as Epistemes**. Agency (capacity to originate) is measured in **Agency‑CHR (C.9)**; here we measure **what came out** and **how it scores** against stated goals and references.  A **Context publishes** the measurement space and admissible policies; a **decision is made by an agentic system in role**, using a named lens within that space. CHR exports **no Γ‑operators** and **no team workflow rules**.

### 1 · Motivation & Intent (manager’s read‑first)

**Problem we solve.** Teams talk past each other about “creativity”: some prize **novelty**, others **business value**, others **originality** or **risk‑managed invention**. Without a shared, context‑local measurement space, reviews derail, portfolios drift, and safety constraints are waived ad‑hoc.

**Intent.** Provide a **small, universal measurement kit** that turns “this is creative” into **checkable, context‑local statements** — grounded in **evidence**, aligned to **objectives**, and **composable** from individuals to portfolios.

**Manager’s one‑screen summary (what you can do with it):**

1. **Score** a design/code/theory change on **Novelty–Value–Surprise–ConstraintFit** with declared references and models.
2. **Compare** options in a **Pareto sense** (no single magic score forced).
3. **Consider** constraints as a **coordinate** in the space; compare options on **frontiers** while keeping Context for high‑novelty options
4. **Track** a portfolio’s **Diversity** to avoid local maxima and groupthink.
5. **Defend** decisions with an auditable **CreativeEvaluation** that cites **what was new relative to which base**, **how value was measured**, and **why this counts here**.

---

### 2 · Forces

| Force                                | Tension we must resolve                                                                                                                 |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Universality vs. domain detail**   | One kit must serve hardware design, software, policy, and science, yet let each Context pick similarity kernels, priors, and value models. |
| **Invention vs. constraint**         | Creative leaps are valuable; safety, ethics, and acceptance are non‑negotiable.                                                         |
| **Local truth vs. Cross‑context reuse** | Meaning is context‑local (A.1.1); yet we need Bridges to compare across organisations/disciplines.                                         |
| **Single score vs. frontier**        | Management wants a number; reality is multi‑objective.                                                                                  |
| **Randomness vs. intention**         | Random noise looks “novel” yet useless; planned recombination can be highly creative.                                                   |

**Design answer.** A **context‑local CreativitySpace** with a **small set of characteristics**, each with **clear measurement templates** and **Evidence Graph Ref**; composition uses **frontiers and partial orders**, not forced scalarisation.

---

### 3 · Solution Overview — The context‑local CreativitySpace

**Idea.** Creativity is **not a type**; it is a **profile** measured on an **outcome** (episteme) or **episode** (set of works) **inside a bounded context**. The context supplies the **ReferenceBase**, **SimilarityKernel**, **GenerativePrior**, **objective function(s)**, and **acceptance constraints**.

**Objects in play (A‑kernel alignment):**

* A **system** (person, team, service) performs **`U.Work`** under a role (A.2).
* That work yields a **carrier** (doc/model/design/code), i.e., an **`U.Episteme`**.
* We apply a **`U.CreativeEvaluation`** to that episteme (and linked work) to produce a **`U.CreativityProfile`** with evidence.

**Cre­ativitySpace (first‑class CHR):**
`U.CreativitySpace(Context) := 〈Novelty@context, ValueGain, Surprise, ConstraintFit, Diversity_P, AttributionIntegrity, EffortCost?〉`
with **scale**/**unit** metadata from **MM‑CHR** (C.16), and Context‑specific **measurement methods** bound by **MethodDescription**.

**Design/run split (A.4):**

* **Design‑time**: score **concepts** or **specs** against **surrogate value models** and **priors**; record **assumptions** (USM scopes; A.2.6).
* **Run‑time**: recompute **ValueGain** and **ConstraintFit** from Work evidence (service acceptance, KPIs) and refresh **Surprise** if priors update.

---

### 4 · Vocabulary (CHR terms & D‑stubs)

> Names are **context‑local**; below are kernel terms. Roles like “Designer/Reviewer” are contextual (A.2). **Documents don’t act** (A.7/A.12); they are **evaluated**.

1. **`U.ReferenceBase`** *(D).* A curated, versioned **set of artifacts** (epistemes) and/or behaviours that define “what exists already” **in this Context and time window**.
   **Conformance (RB‑1):** must declare **inclusion criteria**, **time span (`TimeWindow`)**, and **coverage notes**.

2. **`U.SimilarityKernel`** *(D).* A declared **metric family** with invariances (e.g., text: cosine over embeddings, image: LPIPS, code: AST graph edit).
   **Conformance (SK‑1):** must cite **MethodDescription** and **test corpus**; state **limits**.

3. **`U.GenerativePrior`** *(D).* A model that yields **likelihood** of artifacts given the Context’s history (n‑gram/LM, design grammar, trend model).
   **Conformance (GP‑1):** must publish **training slice**, **fit method**, **perplexity/fit metrics**, and **refresh policy**.

4. **`U.CreativeOutcome`** *(D).* Any **`U.Episteme`** put forward for creative evaluation (e.g., new design, algorithm, spec, policy draft).
   **Note.** If the outcome is a **system change** without a single carrier, attach the evaluation to a **bundle** (set) of carriers referenced from Work.

5. **`U.CreativeEvaluation`** *(D).* A **`U.Evaluation`** that outputs a **`U.CreativityProfile`** and anchors to **ReferenceBase**, **Kernel/Prior**, **objective(s)**, **acceptance tests**, and **Work evidence**.

6. **`U.CreativityProfile`** *(D).* The **coordinate tuple** in `U.CreativitySpace` with provenance to the above inputs and **USM scopes**.
   **Conformance (CP‑1):** profile **must** include **scales/units**, **scopes**, **confidence bands** (B.3), and the **edition** of space definitions.

---

### 5 · The Core Characteristics (kernel nucleus)

Each characteristic is specified per **MM‑CHR (C.16)** with: **name**, **intent**, **carrier**, **polarity**, **scale type**, **measurement template**, **evidence**, **scope (USM)**, and **didactic cues**. *Context profiles MAY add characteristics; kernel characteristics MAY NOT be removed without a Bridge.*

#### 5.1 · `Novelty@context` — “How unlike the known set is this?”

* **Intent.** Quantify **distinctness** of the outcome relative to **`U.ReferenceBase`** (global or targeted slice).
* **Carrier.** `U.Episteme` (the outcome).
* **Polarity.** Higher is “more novel.”
* **Scale.** **\[0, 1]**; ratio (0 = duplicate under kernel; 1 = maximally distant).
* **Measurement template (normative pattern):**

  1. Declare **ReferenceBase** `B` and **TimeWindow** window.
  2. Declare **SimilarityKernel** `σ` and its invariances.
  3. Compute **`Novelty@context := 1 − max_{b∈B} sim_σ(outcome, b)`**, or a robust variant (top‑k mean).
  4. Publish **sensitivity note** (how results shift with kernel/`B`).
* **Evidence.** Kernel/version id; top‑k neighbours with distances; ablation on invariances.
* **Scope hooks (USM).** `B` **must** be a declared **slice**; Cross‑context use needs a **Bridge** with **CL** and **loss notes**.
* **Didactic cues.**

  * **Not** “randomness.” Noise has high novelty, low value.
  * **Local, not global.** Novelty is **to this Context now**, not timeless originality.

#### 5.2 · `Use‑Value` *(alias: `ValueGain`)* — “What good did this add under our objective?”

* **Intent.** Quantify **benefit** vs a baseline objective (Decsn‑CAL utility, Service acceptance, KPI).
* **Carrier.** Outcome (episteme) with **Work** evidence.
* **Polarity.** Higher is better.
* **Scale.** Interval/ratio, unit **declared by the Context** (e.g., ΔSNR, % defects, profit/period).
* **Measurement templates (pick one):**

  * **Measured:** `ValueGain := metric_after − metric_before` (declare counterfactual method).
  * **Predicted:** `E[ValueGain | model]` with error bars; update post‑run.
  * **Evidence.**  Declared **objective/criterion**; measurements or credible predictions; counterfactual method (A/B, back‑test, causal inference).
  * **Scope.** State the **context window** used for the objective; claims outside that window are **informative only**.
  * **Didactic cues.**

  * Value is **relative to stated objective**; if the objective is wrong, the value reflects it.
  * Keep **counterfactual discipline**; otherwise “gain” is storytelling.

#### 5.3 · `Surprise` — “How improbable under our learned world?”

* **Intent.** Capture **unexpectedness** given **`U.GenerativePrior`**.
* **Carrier.** Outcome.
* **Polarity.** Higher surprise = more unexpected.
* **Scale.** **bits** or **nats**: `Surprise := −log p_prior(outcome)`.
* **Measurement template:**

  1. Declare **GenerativePrior** (training slice, model class).
  2. Encode outcome for the prior; compute likelihood proxy.
  3. Publish calibration curve (reliability diagram / PIT histogram).
* **Evidence.** Model cards; fit metrics; OOD diagnostics; refresh policy.
* **Scope.** Training slice declared as **ContextSlice**; Bridges penalise **R** (trust), not the value itself (A.2.6).
* **Didactic cues.**

  * **Novelty vs Surprise:** high novelty under one kernel may be low surprise under a broad prior; publish both.

#### 5.4 · `ConstraintFit` — “Did it honour the non‑negotiables?”

* **Intent.** Ensure **mandatory constraints** (safety, ethics, standards, SLOs) are satisfied.
* **Carrier.** Outcome + Work evidence.
* **Polarity.** Higher is **better** (1 = all mandatory satisfied).
* **Scale.** **\[0, 1]**, ratio or pass/fail.
* **Measurement template:** declare **set `C_must`** (Norm‑CAL / Service acceptance), compute **`ConstraintFit := |{c∈C_must : pass(c)}| / |C_must|`**; optionally weight per criticality.
* **Evidence.** Checklists, tests, audits; Who/Role performed the **SpeechActs** (approvals/waivers).
* **Scope.** Constraints are **context‑local**; Cross‑context requires **Bridge**; waivers are **SpeechAct Work** with RSG gates (A.2.5).
* **Interpretation note.** Low `ConstraintFit` signals tension with declared **must‑constraints** and warrants reframing or redesign; **this pattern does not prescribe go/no‑go rules**.

#### 5.5 · `Diversity_P` *(portfolio‑level)* — “Are we exploring the space?”

* **Intent.** At the **set** level, avoid myopic exploitation; promote **coverage**.
* **Carrier.** A **set** of outcomes.
* **Polarity.** Higher means **broader coverage** (not “better” per se).
* **Scale.** Set‑functional; Context defines metric (e.g., **average pairwise distance**, **k‑cover** over features).
* **Template.** Declare **kernel** and **covering policy**; compute score and **coverage map (illumination)**; relate to **USM ClaimScopes**.
* **Alignment note.** The **illumination/coverage** view corresponds to *IlluminationScore* used by **B.5.2.1 NQD‑Generate**; no separate characteristic is introduced here—measure it as part of `Diversity_P`.
* **Evidence.** Distance matrix/cover plots; sensitivity to kernel.
* **Didactic cue.** Use **Diversity\_P** to **shape portfolios**, not to pick single winners.
* **Marginal gain (for generators)** — normative. For a candidate h and current set S, ΔDiversity_P(h | S) := Diversity_P(S ∪ {h}) − Diversity_P(S). Contexts using NQD SHALL compute D as this marginal and publish the Diversity_P definition alongside the CharacteristicSpace/kernel and TimeWindow.

**Heterogeneity Characterisation**
* FamilyCoverage  (polarity ↑) — count of distinct domain‑families covered by a portfolio/triad; unit: families; window: declared.
* MinInterFamilyDistance (polarity ↑) — min distance between selected families in DescriptorMap; unit: per DistanceDef; window: declared.
* AliasRisk (polarity ↓) — collinearity/near‑duplicate risk indicator for contextual signatures; unit: score (0–1) with policy id.


**Lexical special case (F.18 naming).**  
For **lexical CandidateSets** used by Name Cards (F.18), **Diversity_P SHALL be computed over head-term families, not over raw strings**. Variants that share the same lexical head (e.g., “Reference plane”, “Plane of reference”, “Planar reference”) **MUST** be treated as one family for coverage and distance; only candidates with distinct heads contribute to lexical Diversity_P. This aligns lexical use of Diversity_P with `FamilyCoverage` / `AliasRisk` and prevents inflating diversity by near-synonyms of a single head.


#### 5.6 · `AttributionIntegrity` — “Did we credit sources and licences correctly?”

* **Intent.** Discourage “novelty theft”; ensure **recombination** is **lawful and transparent**.
* **Carrier.** Outcome + provenance graph.
* **Polarity.** Higher is better.
* **Scale.** **\[0, 1]**; fraction of **required attributions/licence duties** satisfied.
* **Template.** Trace graph coverage against Context policy; licence constraints as **Norm‑CAL** rules.
* **Evidence.** PROV‑style links; licence scans; acknowledgements.
* **Didactic cue.** High `AttributionIntegrity` signals lawful and transparent recombination; low values indicate unacceptable practice in most Contexts.  
* **Default role.** `AttributionIntegrity` is **measurable but non‑dominant**. It MAY serve as a **policy filter/tie‑break** (C.19). If certain attribution duties are **must‑constraints**, they belong to **ConstraintFit** (Norm‑CAL) and act as **eligibility gates**. It is **not** part of the default dominance set.
* **Dominance & gating note (normative).** `AttributionIntegrity` is a measurable **Characteristic**; it is **not** in the default dominance set. Contexts MAY use it as a **filter** or **tie‑break** via policy (C.19). Legal/ethical **must‑fit** checks live in **ConstraintFit** (Norm‑CAL); failing those blocks eligibility **before** dominance.

#### 5.7 · `EffortCost` *(advisory)* — “What did it take?”

* **Intent.** Normalise comparisons by cost; not part of “creativity” per se.
* **Carrier.** WorkLedger.
* **Polarity.** Lower is better when used as denominator.
* **Scale.** Resource units (hours, energy, \$).
* **Template.** Sum cost categories over Work that produced the outcome.
* **Evidence.** Time/resource logs; BOM deltas.
* **Didactic cue.** Use **`CreativityPerCost := f(Novelty@context, ValueGain, Surprise)/EffortCost`** for operations planning, not for excellence awards.

---

### 6 · Conformance Checklist (first tranche)

| ID                                        | Requirement (normative)                                                                                                                                                                  | Purpose / audit hint                                          |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **CC‑CR‑1 (context‑locality)**               | Every **CreativityProfile** **MUST** name the **`U.BoundedContext`** and the **edition** of `U.CreativitySpace`.                                                                         | Prevents Cross‑context slippage.                                 |
| **CC‑CR‑2 (Declared bases)**              | **Novelty@context** claims **MUST** declare `ReferenceBase`, `SimilarityKernel`, and `TimeWindow`; **Surprise** claims **MUST** declare `GenerativePrior` and its training slice.                 | Makes “new to whom?” and “unexpected under what?” explicit.   |
| **CC‑CR‑3 (Objective anchor)**            | **ValueGain** **MUST** reference the **objective** (KPI/utility) and **counterfactual method** (if predicted, the model).                                                                | Stops free‑form value stories.                                |
| **CC‑CR‑4 (Must‑fit)**                    | If **must** constraints exist, **ConstraintFit** **MUST** be present; enactment decisions **SHALL** treat `ConstraintFit<1` as **fail**, unless an explicit **waiver SpeechAct** exists. | Keeps safety & ethics non‑negotiable.                         |
| **CC‑CR‑5 (Evidence)**                    | Each coordinate **MUST** have Evidence Graph Ref (neighbours, tests, logs, model cards).                                                                                                   | Enables audit & replication.                                  |
| **CC‑CR‑6 (Scopes)**                      | Profiles **MUST** include **USM scopes** (ClaimScope/WorkScope) relevant to measurement; off‑scope claims are advisory.                                                                  | Ties numbers to where they hold.                              |
| **CC‑CR‑7 (No scalarisation by default)** | The architheory **SHALL NOT** force a single scalar “creativity score.” If a Context defines one, it **MUST** publish the weighting and its drift policy.                                   | Keeps decisions on a Pareto frontier unless a policy opts‑in. |
| **CC‑CR‑8 (Bridge discipline)**           | Cross‑context comparisons **MUST** use a **Bridge** with **CL** and recorded **losses**; any mapped coordinate **MUST** note penalties in the **R** lane, not silently alter the value.     | Honest portability.                                           |

---

### 7 · Manager’s Quick‑Start (apply in 5 steps)

1. **Name the Context** *(context + edition)*.
2. **Pick measurement defaults** *(kernel, prior, objective, constraints)* from the Context’s handbook.
3. **Score outcome** → `Novelty@context`, `Use‑Value`, `Surprise`, `ConstraintFit`.
4. **Decide by frontier**: shortlist **non‑dominated** options; use **ConstraintFit** as a gate; apply **policy** if a scalar is approved.
5. **Record a CreativeEvaluation** with evidence; if crossing Contexts, attach the **Bridge id**.

> **Mental check.** *New to our base? Helpful to our objective? Unexpected under our model? Safe & licenced?*
> If any answer is “unknown,” you are **not done measuring**.

---

### 8 · Archetypal Grounding (three domains)

**(a) Manufacturing design change)**
*Outcome.* New impeller geometry for Pump‑37.
*Context.* `PlantHydraulics_2026`.
*Novelty@context* 0.42 (shape‑descriptor kernel vs last 5 years).
*ValueGain.* +6.8% flow @ same power (bench Work).
*Surprise.* 1.3 bits (within evolutionary trend prior).
*ConstraintFit.* 1.0 (materials, safety, noise).
*Decision.* **Frontier winner**: modest novelty, clear value, safe. Portfolio keeps **Diversity\_P** by also funding one high‑surprise concept for exploration.

**(b) Software architecture refactor)**
*Outcome.* New concurrency model for ETL.
*Context.* `DataPlatform_2026`.
*Novelty\_G.* 0.27 (AST/edit kernel vs internal corpus).
*ValueGain.* −20% latency, −35% p95 stalls (A/B Work).
*Surprise.* 0.5 bits (trend prior expected co‑routines).
*ConstraintFit.* 0.83 (fails SoD—same author as reviewer).
*Decision.* Return for **SoD fix**; then likely adopt. Creativity is **not** a waiver over governance.

**(c) Scientific hypothesis)**
*Outcome.* A new scaling law claim.
*Context.* `GraphDynamics_2026`.
*Novelty\_G.* 0.66 (formula kernel vs literature base).
*ValueGain.* Predicted: explains 12 prior anomalies (model check).
*Surprise.* 3.7 bits (strongly unexpected under prior).
*ConstraintFit.* 1.0 (ethics N/A; evidence roles bound with decay windows).
*Decision.* Fund **replication Work**; track **R** decay per policy.

---

### 9 · Anti‑Patterns (fast fixes)

| Anti‑pattern                   | Why it fails                                                                  | Fix with this architheory                                                        |
| ------------------------------ | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **“Creativity = randomness.”** | Noise yields high `Novelty@context`, low `ValueGain` and often low `ConstraintFit`. | Evaluate **all four** characteristics; require ConstraintFit=1 for musts.                   |
| **Global originality claims.** | Ignores context‑local meaning and current corpus.                                | Declare **Context & ReferenceBase**; cross Contexts only via **Bridge**.               |
| **One magic score.**           | Hides trade‑offs; fragile under drift.                                        | Decide on **Pareto frontier**; publish scalar only with explicit weights/policy. |
| **Hand‑wavy value.**           | No objective → no audit.                                                      | Tie to **Service/KPI** or **utility**; state **counterfactual**.                 |
| **Silent borrowing.**          | Legal/ethical risk; reputational damage.                                      | Track **AttributionIntegrity**; licence scans in evidence.                       |

---

### 10 · Relations (where this plugs in)

* **A.2 Role & A.15 Run‑alignment.** Creative **Work** is performed by **systems in roles**; outcomes are **epistemes**. Creativity is **measured by `U.Evaluation`**, not “done by a document.”
* **B.3 Trust/Assurance.** Coordinates carry **confidence bands**; Bridges lower **R** by **CL**. Evidence roles (A.2.4) bind datasets/benchmarks used in measurements.
* **C.9 Agency‑CHR.** Agency measures **capacity to originate**; a high‑agency system may still output low‑creativity outcomes (and vice versa with strong scaffolding).
* **A.2.6 USM (Scope).** All measurements sit on **ContextSlices**; `G‑ladder` is explicitly **not** used (C.17 follows A.2.6’s set‑valued scopes).
* **D‑cluster ethics.** **ConstraintFit** is where **must** constraints, ethics, and safety bind the evaluation; waivers are explicit **SpeechActs**.

---

### 11 · Authoring Aids (didactic cards)

* **Write the Context.** Context + edition on every profile.
* **Name the base & kernel.** Without them, `Novelty@context` is undefined.
* **State the objective.** Value without a KPI is a story.
* **Publish priors.** Surprise needs a trained model with cards.
* **Gate by musts.** `ConstraintFit` < 1 blocks enactment unless waived.
* **Prefer frontiers.** Shortlist non‑dominated options; let governance decide trade‑offs.
* **Bridge explicitly.** Cross‑context talk needs CL and loss notes.


---

## 12 · CSLC recap and the Creativity CharacteristicSpace

**Purpose.** Ground “creativity” as a **measurable family of characteristics** (CHR) rather than a role, capability, or virtue. Each characteristic is scoped to a **`U.BoundedContext`**, evaluated on **`U.Work`** (episodes), **artifacts** (epistemes, e.g., design sketches, models), or **holders** (systems/teams) via **MM‑CHR** exports (`U.DHCMethodRef`, `U.Measure`, `U.Unit`, `U.EvidenceStub`), using the **CSLC** discipline (*Characteristic / Scale / Level / Coordinate*).

> **Strict Distinction (A.7) reminders.**
> *Creativity is not a Role* (no one “plays CreativityRole”). It’s a **characterisation** of outcomes/process.
> *Creativity is not Work* (no resource deltas). Work **produces** artifacts we later characterise.
> *Creativity is not a Service* (no external promise). Services are judged from Work; creativity may correlate with value.

### 12.1 · The Creativity CharacteristicSpace (CHR‑SPACE)

The core **characteristics** below are **kernel‑portable** names; Contexts **specialise** them (rename if needed, but keep semantics). Each characteristic declares: **what we measure**, **on what carrier**, **typical scale**, and **where it lives** in FPF.

| Characteristics (kernel name)       | What it captures (intuitive)                                 | Measured on           | Typical scale (CSLC)                               | Lives with / checked by              |
| ------------------------ | ------------------------------------------------------------ | --------------------- | -------------------------------------------------- | ------------------------------------ |
| **Novelty\@context**        | Distance from known ideas **in this Context**                   | Artifact / Work set   | Ratio or bounded \[0..1] via *similarity→distance* | `KD‑CAL` corpus + `U.BoundedContext` |
| **Use‑Value**            | Benefit vs a **declared objective**                          | Artifact / Evaluation | Ordinal (Fail/Partial/Pass) or scalar KPI          | `B.3` Evidence & `U.Evaluation`      |
| **Surprise**             | Unexpectedness under the Context’s **GenerativePrior**          | Artifact              | bits or nats (−log‑likelihood)                     | Prior cards & calibration            |
| **ConstraintFit**        | Degree of **must‑constraints** satisfied while exploring     | Work / Artifact       | % satisfied (0–100)                                | `Norm‑CAL` + step guards             |
| **Diversity_P**          | Portfolio **coverage/dispersion** (incl. coverage map view)  | Set of artifacts      | Set‑functional; coverage index                     | `Γ_ctx` fold + USM ClaimScopes       |
| **AttributionIntegrity** | Lawful & transparent **provenance/licensing**                | Artifact + provenance | \[0,1]                                              | PROV + Norm‑CAL                      |

> **Locality.** **Every characteristic is context‑local** (e.g., **Novelty\@context**). Cross‑context claims **must** use a **Bridge** and record **CL** penalties (B.3). No global novelty.

#### 12.2 · Context extensions & policy‑level characteristics (non‑kernel)

The following **context‑local** characteristics remain available but are **not** part of the kernel nucleus; use them as **derived** or **policy** measures:

* **ReframeDelta** — change in the **problem frame** that improves solvability (episteme‑pair; ordinal).
* **Compositionality** — degree of **re‑use and new relations** among parts (artifact; boolean + structure score).
* **Transferability\@X** — portability to **Context X** via a Bridge (artifact; ordinal + CL penalty).
* **DiversityOfSearch** — breadth of **approach classes tried** (work set; count/rate).
* **Time‑to‑First‑Viable** — elapsed time to first **Use‑Value = Pass** (work; duration).
* **Risk‑BudgetedExperimentation** — planned vs realized exploration share (workplan vs work; ratio; policy gate).

> **Compatibility note.** This split removes duplicate “core lists” and aligns C.17 with **B.5.2.1 NQD** and **C.16/A.17–A.18**: the **kernel nucleus** captures creativity *qualities*; the items above instrument **process/policy** or **portfolio shaping**.

### 12.3 · Scale choices (CSLC discipline)

For each characteristic, **declare the scale** explicitly (nominal / ordinal / interval / ratio). **Do not** average ordinal scores; fold with medians or distributional summaries. Choose **units** (when applicable) and **coordinate** semantics (e.g., what “distance” means).

* *Novelty\@context.*
  Coordinate = `1 − max_similarity(candidate, corpus)` with a declared encoder (text, graph, CAD). Unitless in \[0..1]. Document encoder & corpus freeze (`A.10` Evidence Graph Ref).
* *Use‑Value.*
  `Pass` iff **acceptanceSpec** (from `U.Service` or Decision KPI) is met from **Work** evidence; else `Partial`/`Fail`. For scalar KPIs, publish mean ± CI and the acceptance threshold; predicted values carry error bars and are updated post‑run.
* *ConstraintFit.*
  Ratio = satisfied / declared **must** constraints. Constraints are `Norm‑CAL` rules; **count only declared** ones (no unspoken “norms”).



---

## 13 · Novelty & transfer are **context‑local** (Bridges mandatory)

**Rule N‑1 (Locality).** `Novelty@context` is defined **only** within its `U.BoundedContext`. **Never** compare scores across Contexts without an **Alignment Bridge** (F.9).

**Rule N‑2 (Directional mapping).** A Bridge may assert a **directional** substitution (e.g., *Novelty\@DesignLab → Novelty\@Manufacturing* with CL = 2, **loss:** aesthetics encoder absent). Reverse mapping is **not** implied.

**Rule N‑3 (Penalty to R, not to G).** Cross‑context novelty **does not** change scope **G**; it **reduces R** (reliability) by the **CL penalty** (B.3), unless validated by pilot Work in the target Context.

**Practical pattern.** Publish novelty **with its Context tag** and—when reused—attach the **Bridge id** and target‑context **pilot** outcomes.

---


---

## 14 · Anti‑Goodhart guard (use creativity metrics safely)

> **Goodhart’s Law:** “When a measure becomes a target, it ceases to be a good measure.” — We bake in **guards** so creativity scoring **improves** outcomes instead of gaming them.

### 14.1 · Guard‑rails (normative)

* **G‑1 Paired appraisal.** **Never** assess **Novelty** in isolation; pair it with **Use‑Value** or **ConstraintFit** to avoid proxy myopia
* **G‑2 Frozen references.** Novelty requires **frozen corpus + encoder**; changes create a **new edition** and **RSCR** rerun. Portfolio/selection heuristics are **policy-level** (see **C.19**); do not “reward” Illumination beyond its role as a report-metric.
* **G‑3 Time‑lag sanity.** Include a **post‑fact check** (e.g., 30–90‑day retention or cost‑to‑serve delta) before celebrating “creative wins.”
* **G‑4 Exploration budget.** Tie **DiversityOfSearch** to **Risk‑BudgetedExperimentation**; flag overspend.
* **G‑5 No ordinal averaging.** Do not average **ordinal** scales; use distributions/medians or convert only under declared models.

### 14.2 · Conformance Checklist — **CC‑C17‑M (metrics & guards)**

| ID             | Requirement                                                                                                                            | Practical test                                                              |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **CC‑C17‑M.1** | Each metric instance **MUST** cite its **Context**, **edition**, and **evidence hooks** (corpus/encoder, acceptanceSpec, constraint set). | Scorecard lists `ContextId`, `Edition`, and hook ids resolvable via `A.10`. |
| **CC‑C17‑M.2** | **Novelty** scores **MUST NOT** be used to approve Work without a **paired gate** (**Use‑Value** **or** **ConstraintFit**).               | Find decisions referencing novelty; check co‑gate present.                  |
| **CC‑C17‑M.3** | Cross‑context reuse **MUST** cite a **Bridge** and record **CL**; **R** is penalised accordingly.                                         | Scorecards with foreign Context tag lacking Bridge → **fail**.                 |
| **CC‑C17‑M.4** | Ordinal metrics **MUST** be summarised with medians/distributions, not means, unless a declared model justifies numeric treatment.     | Reports using a mean on ordinal without model → **fail**.                   |
| **CC‑C17‑M.5** | Metric templates **MUST** be versioned; changing encoder, reference set, or acceptanceSpec **creates a new edition**.                  | Diff shows changed hooks without edition bump → **fail**.                   |

---


---

## C.18 — NQD‑CAL — Open‑Ended Search Calculus \[A]

**Status.** Architheory specification (**CAL**). Exports `Γ_nqd.*` operators for open‑ended, illumination‑style generation. **ΔKernel = 0** (no kernel primitives added). *Minting note:* this CAL **does not mint** new U‑types; it defines **CAL‑records** that MAY alias to registered U‑types where present via **E.10/UTS**.

**Depends on.** A‑kernel (A.1–A.15), **MM‑CHR** (C.16) for measurements, **KD‑CAL** for similarity/corpora, **Sys‑CAL** for carriers, **Decsn‑CAL** (objectives; advisory), **Compose‑CAL** (set aggregation; advisory).

**Coordinates with.** **B.5.2.1** (binding), **C.17 Creativity‑CHR** (characteristics & scales), **C.19 E/E‑LOG** (policies: emitter selection, explore/exploit).

**Exports (CAL; no U‑type minting here).**
 - Records: `NQD.DescriptorMap` (alias of `U.DescriptorMap` if minted), `NQD.NQDArchive` (alias of `U.NQDArchive`), `NQD.Niche`, `NQD.ArchiveCell`, `NQD.EmissionSeed?`, `U.EmitterPolicyRef`, `U.InsertionPolicyRef`, `U.IlluminationSummary`, and `NQD.CandidateSet` (alias of `Set<U.Hypothesis>`).

### Problem frame
Open‑ended search (NQD) equips FPF with illumination‑style generation and Pareto/portfolio selection in multi‑criteria, partially ordered spaces; it feeds G.5 without scalarising ordinal or mixed‑scale characteristics.

### Problem
Without a disciplined NQD calculus, contexts (a) conflate illumination gauges with dominance, (b) lose reproducibility due to undeclared DescriptorMap/DistanceDefRef.editions, and (c) perform illegal aggregations across scales.

### Forces
• Posets vs. scalarisation — selectors must return sets (Pareto/archive) rather than illegal weighted sums across mixed scales.
• Exploration vs. exploitation — emitters must adapt while preserving provenance and editioning.
• Gauge vs. objective — Illumination (coverage/QD‑score) informs health but is not a dominance characteristic by default.
• Reproducibility vs. adaptivity — budgets, ε, K, and InsertionPolicy must be edition‑tracked.

### Solution
Provide Γ_nqd.* operators and U.Types for DescriptorMap, Archive/Niche, policies, and illumination gauges; bind measurement legality to MM‑CHR and policy control to E/E‑LOG. (Exports/Type notes/Operator specs below are normative parts of this Solution.)

- Operators (Γ):
  - `Γ_nqd.generate(seed?, EmitterPolicyRef, Budget, DescriptorMapRef, QualityMeasuresRef, NoveltyMetricRef, CoverageGrid, CellCapacity K=1, EpsilonDominance ε=0, DedupThreshold?, InsertionPolicyRef?) → CandidateSet<U.Hypothesis>`
  - `Γ_nqd.updateArchive(Archive, CandidateSet, InsertionPolicyRef?) → Archive'`
  - `Γ_nqd.illuminate(Archive) → IlluminationSummary{coverage, QD-score, occupancyEntropy, filledCells}` (reporting gauge only; not a dominance characteristic unless a policy explicitly promotes it).
  - `Γ_nqd.selectFront(Archive|CandidateSet, characteristics={Q components, Novelty@context, ΔDiversity_P, …}) → ParetoFront`

**Type notes.**
- `U.DescriptorMap (Tech; twin‑labelled Plain) : Hypothesis → ℝ^d` (declares encoder, invariances, version, **CharacteristicSpaceRef**). Publish Tech/Plain per **E.10**; declare `DescriptorMapRef.edition` and `DistanceDefRef.edition`. **Dimensionality rule.** **Require `d≥2` only when QD/illumination surfaces are active**; for non‑QD contexts `d≥1` is lawful.
- `NQD.CandidateSet` ≡ `Set<U.Hypothesis>` with attached per‑item vectors `{Q_i, N_i, D_i:=ΔDiversity_P, S_i?, provenance_i}`.
- `U.NQDArchive` holds per‑cell elites and genealogy refs; context‑local.
- `U.Niche` is a region in CharacteristicSpace (grid bucket / CVT centroid / cluster).
- `U.EmitterPolicyRef` points to a named policy in **C.19 E/E‑LOG**.
- `U.InsertionPolicyRef` — named archive‑update policy (e.g., `replace_if_better | replace_worst | bounded_age | bounded_regret`); versioned.
- `U.IlluminationSummary` is a **gauge** over `Diversity_P` (see C.17), not a dominance characteristic.

**Operator specs (normative).**
- `Γ_nqd.generate(...)` SHALL:
  (a) respect **Budget**,  
  (b) compute `{Q_i}` (vector), `N_i` (Novelty@context), `D_i := ΔDiversity_P(h_i | Pool)` under the same CharacteristicSpace & TimeWindow as the Pool, and optional `S_i` (Surprise),
  (c) deduplicate by `DedupThreshold` in CharacteristicSpace,  
  (d) record `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `EmitterPolicyRef`, `ε`, `K`, `Seeds`, and genealogy references (parent/seed ids) to enable replay and selection auditing.
- `Γ_nqd.updateArchive` SHALL apply local competition per cell (keep up to K elites), preserve genealogy, and **enact the declared `InsertionPolicyRef`**; default is `replace_if_better` with deterministic tie‑breakers.
- `Γ_nqd.illuminate` SHALL return coverage and QD‑score computed against the declared grid and archive edition.
- `Γ_nqd.selectFront` SHALL compute the (ε‑)Pareto front over the declared characteristics; **Illumination** is excluded by default (report‑only).  

**Pipeline:** apply **Eligibility (ConstraintFit=pass)** → **Dominance (default set from C.19; by default `{Q components}` only)** → **Tie‑breakers (`Novelty@context`, `ΔDiversity_P`, `Surprise`; `Illumination` gauge)**.
**Pure academic QD-mode:** Contexts MAY elect a _pure‑QD_ mode (dominance on `Q` only; `N/ΔD` used via archive occupancy and tie‑breakers). Any deviation SHALL be declared by policy id and recorded in provenance.

**Reproducibility & editions.** Each call SHALL emit provenance sufficient for replay: `{DHCMethodRef.edition, DescriptorMapRef.edition, EmitterPolicyRef (params), **InsertionPolicyRef**, DedupThreshold?, ε, K, Seeds, TimeWindow}`.
Telemetry hook: whenever IlluminationSummary increases (Δcoverage>0 or ΔQD‑score>0), the Context SHALL emit a Telemetry(PathSlice) record that cites {EmitterPolicyRef, DescriptorMapRef.edition, DistanceDefRef.edition, InsertionPolicyRef?, TimeWindow}. (Aligns with G.6/G.7/G.11 portfolio/edition constraints.)

**Measurement alignment.** `Novelty@context`, `Use‑Value (ValueGain)`, `Surprise`, `Diversity_P` SHALL be measured per **C.17** (MM‑CHR templates). **IlluminationSummary** is a gauge over `Diversity_P` (coverage/QD‑score); when CharacteristicSpace includes domain‑family cells, publish grid id and FamilyCoverage, plus **DescriptorMapRef.edition/DistanceDefRef.edition**.
.

### Conformance Checklist
- **C18‑1** Declare `DescriptorMap` (encoder, invariances, corpus edition) before generation.
- **C18‑1b** When used in F/G triads, DescriptorMap SHALL declare a domain‑family coordinate (grid/cells) and reference an F1‑Card::DistanceDefRef & δ_family.
- **C18‑1c**  When a domain‑family coordinate is declared, the Context SHALL compute and publish **AliasRisk** for each front/portfolio emission, together with the dSig collision rule and the policy id. AliasRisk is computed against `U.DomainDiversitySignature (dSig)`; **the DescriptorMap SHALL publish**: (i) `collisionRuleId` (near‑duplicate threshold, e.g. “≥3 characteristics equal”),  (ii) `dSigSource` pointers used for coding the five characteristics. The collision rule and formula **MUST** be part of `DescriptorMap` provenance (see **Creativity‑CHR**, Heterogeneity Characterisation).
- **C18‑2** Record `EmitterPolicyRef` (policy id from C.19) and parameter set.
- **C18‑3** Compute `D = ΔDiversity_P(h | Pool)` under the same DescriptorMap & TimeWindow as the Pool (see C.17).
- **C18‑4** Exclude Illumination from dominance unless policy explicitly promotes it.
- **C18‑5** Keep `Use‑Value` separate from assurance scores; do not alter `F/G/R` semantics (see B.3, C.17 §Use‑Value).
- **C18‑6** Emit full provenance; thinning after front computation MUST be recorded.
- **C18‑7** Before computing any front, apply **ConstraintFit = pass** as a hard eligibility filter.

**Defaults.** Normative defaults **live in C.19 (EmitterPolicy)** and are **not restated** here. Minimum provenance remains: `DescriptorMapRef.edition` and `DistanceDefRef.edition`, `DHCMethodRef.edition`, `EmitterPolicyRef`, `InsertionPolicyRef`, `TimeWindow`, `Seeds`, `DedupThreshold?`; also record `FamilyCoverage/MinInterFamilyDistance`.

**Didactic quickstart (Context).**
1) Pick 2–4 Quality coordinates and a simple DescriptorMap (2–4 dims).  
2) Set defaults: `K=1`, `ε=0`, a conservative `EmitterPolicy`.  
3) Run `Γ_nqd.generate` to fixed Budget; inspect the front; log coverage (IlluminationSummary).  
4) Apply abductive plausibility filters; promote prime hypothesis to L0.

### Archetypal Grounding
**System.** Legged‑robot gait exploration: Q = forward speed & energy efficiency (ratio), D = morphology/coordination descriptors (ℝ^d); Archive = CVT grid; Illumination gauges coverage without entering dominance.
"**Episteme.** SoTA palette synthesis: Q = Use‑Value proxies per C.17 (ratio/interval as legal), D = method‑family niches; publish DescriptorMapRef.edition and DistanceDefRef.edition for reproducible fronts.

### Bias‑Annotation
Lexical firewall and notation independence apply; no vendor/tool tokens; ordinal characteristics never averaged; illumination treated as gauge unless a policy promotes it. (E.5.1, E.5.2, C.16)

### Consequences
• Portfolio honesty (no forced scalarisation). • Reproducible exploration (editioned maps/policies). • Healthy diversity signals via gauges.

### Rationale
Post‑2015 Quality‑Diversity (MAP‑Elites & successors) demonstrates illumination efficacy; NQD‑CAL captures these ideas while preserving MM‑CHR legality and LOG governance.

### Relations
Builds on: C.16, C.2. Coordinates with: B.5.2.1 (binding), C.17, C.19, G.5, G.6, G.11.

### C.18.1 — **SLL — Scaling‑Law Lens (binding)** \[A]

**One‑screen purpose (manager‑first).**
Make **generation/selection** scale‑savvy: at the level of **conceptual descriptors**, declare (a) **which monotone knobs** we would scale, (b) the **ScaleWindow** over which we claim behaviour, and (c) the **elasticity class** we observed—**without** imposing numeric fits or vendor tools at Core level. This surfaces knees early and keeps comparisons lawful and fair across families. (Parity is handled by **G.9**; illumination remains a **gauge** unless promoted by policy.)  

**Builds on.** C.16 (MM‑CHR), C.17 (Creativity‑CHR), C.18 (NQD‑CAL); advisory: C.5 (Resrc‑CAL).
**Coordinates with.** C.19 (E/E‑LOG), G.5 (Selector & Registry), G.9 (Parity Harness), G.10 (Shipping), G.11 (Refresh‑Telemetry), C.24 (Agent‑Tools‑CAL).
**Keywords.** scaling law; **Scale Variables (S)**; ScaleWindow; knee; diminishing returns; **iso‑scale parity**; **gauge mapping**; **scale‑probe**; **DoE** (design‑of‑experiments); segmented regression; knee detection.

#### 1) Problem frame

Teams often say a method “**scales**” without disclosing **which resources**, **across what window**, and **how** outcomes respond (convex rise → knee → plateau). Without that, parity is skewed (unequal budgets, unmatched windows), coverage/illumination report-metrics leak into dominance, and “knees” are found late. SLL supplies a notation‑independent **lens** to make scale behaviour explicit and comparable. 

#### 2) Problem

Omitting **Scale Variables** and the comparison window causes: (i) **unfair parity** (compute/data/FoA mismatched), (ii) **illumination/coverage report-metric  creep** into dominance by default, (iii) late detection of knees and budget waste. **G.9** already forbids scalarising mixed scales and mandates equal **FreshnessWindows**/**pinned editions**; SLL complements this with **ScaleWindow** & elasticity. 

#### 3) Forces

Notation independence vs useful scaling heuristics; local context vs cross‑context generality; **gauges vs objectives** (illumination stays a gauge unless policy promotes it); early exploration vs reproducible policy.

#### 4) Solution — *binding lens for generator/selector profiles* (normative)

**4.1 Types (aliases; ΔKernel = 0).**
`SLL.Profile` is an **annotation** on a `MethodFamily/Generator` or a `Selector` profile; **no new U.Types** are minted (LEX discipline). 

**4.2 Fields (conceptual descriptors).**

* **S — Scale Variables.** Minimal set of **monotone knobs** for the Context: `compute` (steps/tokens/FLOPs/time/energy), `data` (size/quality), `model capacity` (params/branches), `iteration budget`, **`freedom‑of‑action (FoA)`**/**environment richness**, etc. Declare **units** via **Resrc‑CAL** and bind to a **ScaleWindow**. Where training/inference trade, **name the phase** the claim concerns.
* **ScaleWindow.** Declared range of `S` values for which behaviour claims hold (editioned). This is **distinct from** **FreshnessWindow** used by parity. 
* **Scale‑Probe.** At least **two** (preferably **≥ 3**) **parity‑respecting** points in `S` within the ScaleWindow, recorded with **replicates/seeds** and **CI/error bars** to support elasticity classification. Pick points via a **small factorial or Latin‑hypercube** when multiple knobs vary.
* **ElasticityClass** `χ ∈ {rising, knee, flat, declining}` — a **qualitative** class; numeric exponents/fits live in domain annexes, not Core.
* **ParityNotes.** `iso‑scale parity?` flag (and **loss notes** if not achieved), plus **Bridge/Φ/Ψ** IDs when crossing contexts (penalties **route to R only**). 

**4.3 Norms (SLL).**

* **SLL‑1 (Declaration).** Any profile **claiming scale behaviour SHALL** declare `S` and a **ScaleWindow** for the Context.
* **SLL‑2 (Probe).** Early investigation **SHALL** include a **scale‑probe** (≥ 2 points in `S`, with replicates/CI) and record **χ**. Multi‑knob probes **SHALL** hold unspecified knobs fixed or pinned, and disclose invariants.
* **SLL‑3 (Parity).** Where `S` is declared, comparisons **SHALL** ensure **iso‑scale parity** and lawful **gauge mapping** across heterogeneous knobs (e.g., FLOPs↔tokens) **before** comparing outcomes; **FreshnessWindows/editions** must be equal/pinned per **G.9**. Record **seeds/replicates**, ComparatorSet, and policy‑ids in telemetry/SCR. 
* **SLL‑4 (Selection lens).** Within the **same Context and ScaleWindow**, if other heads (N/U/C) are tied, selectors **MAY** use **χ** as a **policy‑level tie‑breaker** under **E/E‑LOG**; illumination remains a **gauge** unless a CAL policy promotes it.
* **SLL‑5 (Knee test).** A **knee** is **claimed** only where a monotone rise is followed by a **statistically significant** slope drop across adjacent probe points within the ScaleWindow; thresholds (e.g., Δslope & CI level) are **policy‑defined** (E/E‑LOG) and must be cited. Absent such evidence, classify as **rising**.
* **SLL‑6 (Telemetry invariants).** Probes **SHALL** export seeds/replicates, edition pins, policy‑ids, and Resrc‑CAL units to **G.11**.

**4.4 Method — minimal SoTA probe recipe (notation‑agnostic; informative).**
1) **Choose knobs** `S` that are plausibly monotone in the Context (compute/data/capacity/FoA).  
2) **Pick 3–5 probe points** per active knob (edge/mid/edge) under iso‑scale parity; use a **fractional factorial** if >2 knobs.  
3) **Run replicates** (≥ 3 preferred) and **bootstrap** 95% CI on the primary objective(s); log seeds.  
4) **Estimate local slopes** on a log‑log grid; apply **piecewise/segmented regression** or a **knee detector** (e.g., L‑curve/Kneedle) to support `χ`.  
5) **Record invariants** (pinned knobs, safety envelope) and publish **SLL.Card@Context**.  
6) **If χ changes** across the window, split the ScaleWindow and re‑classify per segment.

#### 5) Interfaces — minimal I/O (conceptual)

**G.9 Plan/Run Parity** consumes `S`/ScaleWindow to align budgets, **pin editions**, and perform **gauge mapping**; **G.11** carries **policy‑id**, **PathSliceId**, seeds/replicates, CI level, and edition pins per parity CC. 

#### 6) Conformance Checklist (CC‑SLL)

1. `S` declared **or** `S = N/A` with rationale.
2. **Scale‑probe** performed; **χ** recorded with **replicates/CI**; invariants disclosed.
3. **iso‑scale parity** or **loss notes** + penalties **→ R only**; editions/seeds pinned; ComparatorSet cited.
4. If used as tie‑breaker, the selector cites **χ** and **lens id** in **E/E‑LOG** provenance.
5. Knee claims cite the **policy threshold** and CI level used.

#### 7) Anti‑patterns & remedies

Hidden budget mismatches; averaging ordinals across families; **illumination in dominance by default**; unpinned editions; slope claims without **replicates/CI**; training/inference phase mixing → **cure** with **G.9** parity (equal windows/editions; normalize‑then‑compare; return sets), phase‑label the claim, and record slope uncertainty per Scale‑Audit discipline.  

#### 8) Archetypal grounding (post‑2015; informative)

* **LLM scaling.** Kaplan‑style & **Chinchilla‑optimal** regimes; **Mixture‑of‑Experts** and **retrieval‑augmented** families shift effective capacity with different inference budgets; prompt‑policies often transfer better than narrow pipelines.
* **RL/Planning.** Model‑based optimization & general agents vs hand‑tuned controllers; slopes reported wrt budget/FoA under safety envelopes.
* **QD/OEE.** MAP‑Elites, **CMA‑ME**, **DQD**, **QDax**; **POET/Enhanced‑POET** families: coverage/illumination as gauges; parity uses fixed grids/spaces and edition pins.  

#### 9) Payload — exports

`SLL.Card@Context` (UTS row; editioned):
`⟨S{knobs, units, phase}, ScaleWindow, Scale‑Probe{points≥2, design=one‑liner, seeds, CI}, ElasticityClass χ, ParityNotes{iso‑scale?|loss, invariants}, BridgeIds?/Φ/Ψ, PolicyIds? (E/E‑LOG), PathSliceId?⟩`.

**UTS row template (conceptual; pencil‑ready).**
`SLL.Card@Context := S=(COMPUTE|DATA|CAPACITY|FOA; units=…; phase=TRAIN|INFER), ScaleWindow=[LOW…HIGH], Probe=(points=…, design=factorial|LHD, seeds=…, CI=…), χ=rising|knee|flat|declining, ParityNotes=(iso=true|false; invariants=…), Bridge/Φ/Ψ=(…), PolicyIds=(…), PathSliceId=(…)`.

#### 10) Relations

**Builds on:** C.16/17/18. **Coordinates with:** C.19 (lenses/policies), **G.5** (set‑returning selector), **G.9** (parity; **ParetoOnly** default; gauge‑mapping), **G.10** (shipping). 

> *Pedagogical cue.* **Say what you would scale, probe it twice, and use the slope‑class to steer.**


---

## C.19 — E/E‑LOG — Explore–Exploit Governor \[A]

**Status.** Architheory specification (**LOG**). Defines exploration/exploitation policies and selection lenses. **No Γ operators** are exported; policies parameterize calls in **C.18 NQD‑CAL**.

### Problem frame
The E/E governor provides named, versioned policies and lenses that steer NQD generation/selection under lawful dominance and provenance constraints.

### Problem
Ad‑hoc exploration mixes ordinal and interval folds, silently scalarises posets, and loses lens/policy provenance—undermining legality and reproducibility.

### Forces
• Trust gates vs. discovery — graduation requires backstop confidence while maintaining explore_share.
• Heterogeneity vs. focus — fairness quotas by family vs. depth on proven lines.
• Lens expressiveness vs. audit — scalarised choices must not be called 'the frontier' and MUST record lens ids.

### Solution
Define EmitterPolicy (class, params, ε, K, insertion/dedup) and selection lenses with a fixed pipeline (Eligibility → Dominance → Tie‑breakers); bind provenance (policy id, lens id) and guard promotions of Surprise/Illumination to dominance to explicit policy declarations.

**Agency note.** Decisions are taken by a **system in role**. **Contexts publish** measurement spaces and admissible policies as **semantic frames**; LOG profiles lenses and policies but does **not** enact choices.
**Depends on.** **C.18 NQD‑CAL** (generators), **C.17 Creativity‑CHR** (measurements), **Decsn‑CAL** (objectives/constraints, scalarization lenses), **B.3** (trust adjustments), **Compose‑CAL** (set aggregation; advisory).

**EmitterPolicy (named profile).** A context‑local, versioned policy with fields:
`{ name, class ∈ {UCB, Thompson, BO‑EI, GP‑UCB, PES, …}, params, explore_share∈[0,1], temperature τ≥0, rebalance_period, wild_bet_quota≥0, backstop_confidence (assurance level), epsilon_dominance ε, cell_capacity K, **insertion_policy**, **dedup_threshold** }`.
Policies are referenced as `U.EmitterPolicyRef` by NQD generator call (C.18) and are conceptual lenses, not staffing/budget instructions.

**Defaults (if policy is unspecified):**  
• **Dominance:** `{Q components}` with `ConstraintFit=pass` as **eligibility gate**.  
• **Tie‑breakers:** `Novelty@context`, `ΔDiversity_P`, `Surprise`; `Illumination` (gauge over Diversity_P) MAY be used as a tie‑breaker but is **not** in the dominance set.  
• **Archive:** `K=1`, `ε=0`, deduplication in `CharacteristicSpace`.  
• **Policy:** UCB‑class with moderate temperature; `explore_share ≈ 0.3–0.5`.  
• **Provenance (minimum):** record `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `DHCMethodRef.edition`, `EmitterPolicyRef`, `InsertionPolicyRef`, `dedup_threshold?`, `TimeWindow`, `Seeds`.

**Scalarization lenses (policy‑level).** A lens `J_ℓ` declares: (a) hard eligibility conditions (e.g., ConstraintFit=pass), (b) soft aggregation (weights/curves), (c) trust policy (how assurance/CL discounts enter).  
**Conformance.** A Context MUST name the lens used to pick from a frontier; scalarized rankings MUST NOT be presented as “the frontier”; the **`lens id MUST be recorded in provenance of each selection`**.

**Promotion rules (policy).**  
- **Tie‑breaks.**  `Surprise` and `Illumination` MAY act as tie‑breakers; **promotion into the dominance set MUST be declared by lens or policy id** and captured in provenance.
- **Graduation.** Profiles graduate from Explore→Exploit when **backstop_confidence** (B.3 level) and eligibility conditions are met.  
- **Sunset/Pivot.** Profiles failing VOI/backstop thresholds are sunset or pivoted at `rebalance_period`.

**Explore/Exploit loop (per rebalance_period).**
1) Recompute frontier with trust discounts.  
2) Enforce `explore_share` (minimum attention on high‑Novelty, not‑yet‑proven profiles).  
3) Update generator `temperature τ` / emitter mix.  
4) Apply `backstop_confidence` to graduate; sunset stale probes.  
5) Satisfy `wild_bet_quota` by seeding fresh high‑Novelty candidates.
6) HET‑FIRST — apply group‑fairness quotas by domain‑family and/or DPP/Max‑min repulsion before exploit lenses; log quotas and sampler policy id.

**Named lenses (heuristics; policy‑level, not norms)**
The following **lens profiles** are **illustrative heuristics**. Contexts MAY reuse/modify them; they are **not** normative.
• **Frontier‑sweeper** — maintain attention on the full front; promote only when `backstop_confidence` holds.  
• **Barbell** — enforce `explore_share ≥ θ` with a `wild_bet_quota`; otherwise exploit top‑trust region.  
• **Spike‑first** — pick highest **Use‑Value** subject to `ConstraintFit=pass` and a small **Cost‑to‑Probe** cap.  
• **Safety‑first** — minimize **SafetyRisk** subject to `Use‑Value ≥ θ` and `ConstraintFit=pass`.  
• **Platform‑option** — maximize **Option‑Value** under probe cost bounds.  
• **Pilot‑then‑scale** — optimize **Use‑Value** on pilot scope with `BackstopConfidence ≥ L1`; widen `G` once **R** holds.  
• **Heterogeneity‑first (policy id).** Eligibility → Dominance → Tie‑breakers; Hard gate: FamilyCoverage ≥ k, MinInterFamilyDistance ≥ δ_family; Fairness quotas: ≤1 candidate per sub‑family at pre‑front sampling; DPP/Max‑min sampler allowed.
**Conformance (lens recording).** A decision that uses any lens **MUST** record its **lens id** alongside `EmitterPolicyRef`. (This restates and localizes C19‑3.)

### Conformance Checklist
- **C19‑1** Each NQD generator call (C.18) **SHALL** cite `U.EmitterPolicyRef` (policy id + params) **and the active `InsertionPolicyRef`/`dedup_threshold` when not inherited**.
- **C19‑2** The characteristic set & signs used for dominance **MUST** be declared; eligibility conditions applied first. *(References to C.18 generator operators are descriptive only; LOG exports no Γ.)*
- **C19‑3** If a lens is used, its id MUST be recorded; do not label scalarized top‑1 as “frontier”.  
- **C19‑4** Promotion of Surprise/Illumination into dominance MUST be explicit in policy.  
- **C19‑5** USM/RSG gate applies: policy actions SHALL operate within the Context’s scope and enactable RSG states.
- **C19‑6** Each selection lens **MUST** implement and document the pipeline` Eligibility (ConstraintFit=pass) → Dominance (declared set) → Tie‑breakers (declared)`. Any **promotion** of Surprise/Illumination into the dominance set **MUST** be named by lens/policy id and recorded in provenance.
- **C19‑7 (LEX‑AUTH trigger).** Any change to `EmitterPolicy` defaults that affects domain‑family quotas/samplers (HET‑FIRST), or any change to `DescriptorMap` family coordinates, `DistanceDef`, or the `δ_family` threshold MUST be authored via **E.15 LEX‑AUTH** with a published **LAT**; the DRR SHALL carry the LAT pointer (see **CC‑DRR.6**). Record policy/card ids in SCR.
- **C19‑8**  When the Heterogeneity‑first lens is used, provenance MUST include: (i) the family‑quota vector (including the default triad quota k), (ii) the subFamilyDef id (from F1‑Card) if sub‑family quotas apply, (iii) the sampler class, seed, and policy id.

**Illumination & Diversity_P.** Illumination is a **gauge over Diversity_P** (coverage/QD‑score). It informs exploration health and tie‑breaks; it is **not** a dominance characteristic by default.

When **Name Cards** (F.18) use NQD-CAL for lexical search, the underlying `DescriptorMap` and `Diversity_P` **MUST** follow the **head-term family** discipline:  
– group label candidates into families by lexical head (base noun/verb, ignoring minor prepositions and inflection);  
– compute Diversity_P and any illumination/coverage gauges over these families (cf. `FamilyCoverage`, `AliasRisk`), not over individual string variants.  
This requirement prevents treating small morphological tweaks of one head as a “diverse” frontier and keeps lexical NQD-fronts honest.

**Baseline profile (informative, context‑local template).**
`EmitterPolicy#NQD-Default-2025`:
    class=`UCB`, explore_share=`0.3–0.5`, temperature `τ=moderate`,
    rebalance_period=`Context default`, wild_bet_quota=`≥0`,
    backstop_confidence=`policy L1`, epsilon_dominance=`ε=0`,
    cell_capacity=`K=1`.
Contexts MAY clone/adjust; if used, record its id in provenance.

**Didactic quickstart (Context).**
- Start with policy class = `UCB` or `Thompson`; set `explore_share≈0.3–0.5`, `τ` moderate.  
- Name the dominance set: `{Q components, Novelty@context, ΔDiversity_P}` with `ConstraintFit=pass` as gate.  
  *(Use‑Value / Cost‑to‑Probe may appear in **lenses** or **constraints**; they are **not** in the default dominance set.)*
- Pick a lens for the final choice (or stick to frontier if undecided); record the lens id in the decision memo.

### Archetypal Grounding
**System.** Policy‑driven A/B of architectural variants: Eligibility = constraint‑fit; Dominance = {Q components, Novelty@context, ΔDiversity_P}; lens = 'Frontier‑sweeper' vs 'Barbell'.
**Episteme.** Method‑family portfolio in SoTA pack: fairness quotas across traditions; lens id recorded; Illumination used as tie‑breaker only unless promoted.

### Bias‑Annotation
No global scalarisation of partial orders; ordinal scales excluded from arithmetic; all selections record lens id and policy id; notation/tool neutrality.

### Consequences
• Transparent exploration budgets. • Repeatable lens‑based selections. • Heterogeneity preserved without illegal aggregates.

### Rationale
Post‑2015 exploration practice (bandits/BO/RL with QD) shows policies must be explicit, auditable, and editioned; LOG provides that governance.

### Relations
Builds on: Decsn‑CAL, B.3. Coordinates with: C.18, C.17, G.5, G.9.

### C.19.1 — **BLP — Bitter‑Lesson Preference (policy)** \[A]

**One‑screen purpose (manager‑first).**
Establish, at **governing policy** level, the empirical **Bitter Lesson**: **prefer general, scale‑amenable methods**—those that improve with **more data/compute/capacity and greater freedom‑of‑action**—over narrow hand‑crafted heuristics **when safety and legality are equal**. Exceptions require a transparent **Scale‑Audit** under the parity harness. 

**Builds on.** C.19 (E/E‑LOG), C.24 (Agent‑Tools‑CAL; **ATC‑2**), B.3 (Assurance), E.3 (Precedence), E.5 (Guard‑Rails).
**Coordinates with.** G.5 (Selector), G.8 (SoS‑LOG Bundles), G.9 (Parity), G.11 (Refresh‑Telemetry), A.0 (On‑Ramp).
**Keywords.** general‑method preference; scale‑amenability; **BLP‑waiver**; iso‑scale parity; **Scale‑Audit**; slope vector; **α/δ tolerances**.

#### 1) Problem frame

Bespoke heuristics can win locally but **do not scale**; general methods (search/learning/planning) **improve with scale** and transfer across bridges/planes. Without a standing policy, selectors drift toward hand‑craft and single‑winner leaderboards, violating parity and lawful orders. 

#### 2) Policy clauses (normative; synchronized with Core)

**BLP‑1 — Scale‑Audit requirement.**
Any DRR that selects a **narrower/hand‑engineered** method over a **general/scalable** alternative **MUST** include a **Scale‑Audit**:
(a) **Parity harness**: equal **FreshnessWindows**, a common **ComparatorSet**, **replicates/seeds**, **portfolio‑first** evaluation; **Dominance = ParetoOnly** unless a CAL policy says otherwise (policy‑id cited).  
(b) **Budget sweeps**: vary **compute**, **data**, and **FoA** within a fixed safety envelope; **pin** any unsweepable knob and record the invariant. 
(c) **Slopes & uncertainty**: report ∂quality/∂compute, ∂quality/∂data, and (where applicable) ∂coverage/∂FoA, with **CI/error bars** and **edition/policy pins** in telemetry. Use **bootstrapped CIs** or repeated‑seed estimates; disclose heteroscedasticity handling.
(d) **Resources**: publish **Resrc‑CAL** accounts (time/energy/FLOPs) and assurance deltas (B.3). 
(e) **Objective vector**: list **Q/Risk/Cost** and—**only if policy promotes them**—illumination/coverage gauges. 
(f) **DoE recipe**: for ≥2 active knobs, apply a **fractional factorial** or **Latin‑hypercube** with ≥ 3 levels per knob to avoid aliasing; justify any lower design.  
(g) **Knee & regret tests**: if claiming a heuristic wins, show either (i) a **knee** inside the audited window for the general method (per SLL‑5 policy thresholds) or (ii) **budget‑constrained regret** over the sweep where the heuristic dominates within CI.

**BLP‑2 — Preference rule (with α/δ tolerances).**
Among admissible options with comparable assurance (within **δ**) and budget (within **α**), prefer the method whose **slope vector** **Pareto‑dominates** over the audited range; if no dominance within error bounds, prefer the **more general** method; else resolve by the **E/E‑LOG** tie‑breakers declared in policy. (Agentic contexts implement this as **ATC‑2**; **BLP_delta_α/δ** live in **ATC.Policy**.)  

> **BLP‑2.1 — Valid waiver grounds (override transparency).**
> Overrides of BLP‑2 are allowed **only** when:
> • **Deontic override:** regulation/ethics make the general method inapplicable (E.5/E.3).
> • **Scale‑probe overturn:** under **iso‑scale parity** in the declared **ScaleWindow**, the heuristic **sustainedly outperforms** with uncertainty accounted for.
> • **Complementary bias:** the heuristic is an **inductive bias** that **improves** the general method **without blocking scale** (graceful degradation as `S` grows).
> All overrides record a **BLP‑waiver** with rationale, owner, and expiry/review in the DRR. 

**BLP‑3 — Minimal‑prescription default.**
Author **rules‑as‑prohibitions** (negative constraints) instead of stepwise scripts; encode limits in **Φ policy tables** (and **Φ_plane**) and allow agents to **sequence autonomously** within those constraints. Scripts are permissible only when mandated by safety/regulation or with compelling DRR evidence reviewed under E.3/E.5. 

**BLP‑4 — Heuristic‑Debt register (mandatory).**
Any admitted heuristic is recorded as **Heuristic Debt** with scope, owner, expiry/review window, and a de‑hardening plan; track in **CalibrationLedger/BCT** and cite in SCR. 

**BLP‑5 — Continuous‑learning posture.**
Where product policy allows, enable **feedback‑driven adaptation** (preference learning, critique loops) within Guard‑Rails and privacy controls; disabling adaptation requires DRR justification and review date. 

**BLP‑6 — Precedence & safeguards.**
BLP is constitutional (instantiates **P‑10/P‑11/P‑7/P‑1**), but **does not supersede Guard‑Rails (E.5) or precedence rulings (E.3)**. Where **NQD/E/E‑LOG** promotes illumination into dominance, **BLP adopts that lens** for the audited window.  

**BLP‑7 — Publication discipline.**
Scale‑Audit artefacts **SHALL** be exported to **G.11** with edition pins, CI level, α/δ, ComparatorSet, and **BLP.Policy@Context** reference so downstream selectors can reuse evidence without re‑running audits.

#### 3) Conformance Checklist (CC‑BLP)

1. **α/δ tolerances** declared in DRR or via policy profile (and CI level stated).
2. DRR includes a **Scale‑Audit** (BLP‑1a–g) with slopes, **CI**, edition/policy pins, and Resrc‑CAL.
3. Selection cites **BLP‑2** and precedence checks.
4. Any heuristic is logged as **Heuristic‑Debt** with expiry and de‑hardening plan.
5. Authoring defaults to **rules‑as‑prohibitions**; deviations are DRR‑justified and safety‑anchored.
6. **Resrc‑CAL** accounts and assurance deltas reported.
7. **Replicate counts/seeds** and **confidence intervals** recorded for slope estimates; heteroscedasticity handling disclosed.
8. Audit artefacts exported to **G.11** with **BLP.Policy@Context** id.

#### 4) Anti‑patterns & remedies

Single‑winner leaderboards; hidden budget mixing; promoting illumination into dominance **without policy**; missing edition pins; heuristics without expiry; slope estimates without CI or with aliased designs → **remedy** with G.9 parity + edition pins, explicit **policy‑ids**, DRR publication, **Heuristic‑Debt** entries, and BLP‑1f DoE discipline. 

#### 5) Archetypal grounding (post‑2015; informative)

* **LLMs:** prompt‑programs, **retrieval‑augmented** and **MoE** policies vs narrow task‑specific pipelines; portfolio‑first selection across editions/budgets.
* **RL & planning:** model‑based optimization/general agents vs hand‑coded controllers (subject to α/δ and safety).
* **Preference learning:** **RLHF ↔ DPO** families.
* **QD/OEE:** MAP‑Elites/**CMA‑ME**/**DQD**/**QDax**; **POET/Enhanced‑POET**; illumination remains a **gauge** unless policy promotes it. 

#### 6) Payload — exports

`BLP.Policy@Context` (UTS row; editioned):
`⟨PreferenceDefault, α/δ tolerances + CI, Scale‑Audit recipe (G.9 link; DoE), WaiverRegister{reason, owner, expiry}, E/E‑LOG lens policy‑ids, ATC.PolicyRef? (agentic), G.11.TelemetryPins⟩`.

**UTS row template (conceptual; pencil‑ready).**
`BLP.Policy@Context := PreferenceDefault=(prefer‑general|neutral), α/δ=(α=…, δ=…, CI=…), Scale‑Audit=(parity=G.9; sweep=S={…}; DoE=factorial|LHD; kneeTest=policy‑τ), WaiverRegister=[{reason=…, owner=…, expiry=…}], E/E‑LOG=(policyIds=…), ATC.PolicyRef=(…), TelemetryPins=(edition=…, seeds=…, comparatorSet=…)`.

#### 7) Relations

**Depends on:** **G.5/G.9** (selector/parity), **G.11** (refresh telemetry), **C.5** (Resrc‑CAL), **C.18** (NQD‑CAL), **C.19** (E/E‑LOG), **F.7/F.9** (Bridges, CL/Φ/Ψ). **Constrained by:** **E.5** Guard‑Rails and **E.3** precedence. 

> *Memory hook.* **Prefer what scales; explain when you don’t.**
