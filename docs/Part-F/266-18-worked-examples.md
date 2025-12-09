## 18 · Worked examples (compact)

> Each example shows **how the Protocol steers naming** so engineers and managers can communicate without hidden Cross‑context leaks.  
> **Card hygiene shown explicitly:** each example **states the Kind and the Purpose/use‑domain** and **chooses Tech/Plain labels from a small NQD‑frontier** (seed set diversified by traditions, novelty/familiarity, and lexical form; see Part G (G.18)).
> **Head-term diversity:** each example **MUST** also state the **distinct head-term families** represented in its NQD candidate set (lexical “roots” such as *Recipe*, *Run*, *Episode*, not prepositional/morphological variants). This prevents faking Diversity_P with near-clones of one head.

### Example 1 — *MethodDescription* vs *Work* (recipe vs run)

* **Context harvest:**
  *BPMN 2.0 (2011):* “Process model” (recipe) and “Activity instance” (run).
  *PROV‑O (2013):* `prov:Plan` vs `prov:Activity`.
  *ITIL:* “Work instruction” vs “Change implementation record.”
* **Kind:** `U.MethodDescription` (design‑time artifact) **and** `U.Work` (run‑time occurrence).
* **Purpose / use‑domain:** planning/scheduling vocabulary across BPMN, PROV‑O, ITIL; separates *design recipe* from *execution episode* for governance and telemetry.
* **NQD‑front (seed candidates):**  
  *design‑time:* *Procedure*, *ProcessModel*, *MethodSpec*, *WorkflowDefinition*, *Recipe*, *MethodScript*  
  *run‑time:* *Run*, *Execution*, *Enactment*, *ActivityInstance*, *Job*, *Episode*
* **Head-term families used (design/run):**  
  *design-time heads:* {Procedure, ProcessModel, MethodSpec, WorkflowDefinition, Recipe, MethodScript}  
  *run-time heads:* {Run, Execution, Enactment, ActivityInstance, Job, Episode}
* **Chosen from frontier (Unified Tech / Plain):**  
  `U.MethodDescription` / “recipe”; `U.Work` / “run”.  
  *Discarded highlights:* **Procedure** (collides with governance “procedure/policy”); **Execution** (overloaded in CS/security); 
* **Anti-pattern (for illustration only, non-conformant).**  
 > *Bad CandidateSet (lexically narrow):* {“Reference plane”, “Plane of reference”, “Planar reference”, “Ref. plane v2”}.  
 > All four are one **head-term family** (*plane*). Even if Diversity_P over raw strings looks high (four labels), **head-term diversity is 1**, so this set **fails** the F.18 diversity intent. A conformant Card would either: (a) add labels with other heads (e.g., *Layer*, *Track*, *Band*), or (b) explicitly record why other heads are rejected (AliasRisk, domain idiom) and accept low lexical Diversity_P with a rationale.
* **Enactment** (speech‑act nuance).
* **Bridges:** recipe↔run **related**, not identical; loss note “control‑flow vs. execution.”
* **Why it matters:** Managers can schedule **Work** while authors improve the **MethodDescription**—no category errors. The NQD‑front preserves tradition‑diverse, lexically stable options until a reasoned choice is made. (F.11/F.16; F.17 rows.)

### Example 2 — *Service* (promise) vs *SpeechAct* (utterance) vs *Commitment* (deontic)

* **Context harvest:**
  *IT service canon:* “SLA/OLA clause”, “ticket approved”.
  *Speech‑act theory:* “performative utterance”.
  *Org governance:* “approval signature”.
* **Kind:** `U.Service` (promise), `U.SpeechAct` (utterance), `U.Commitment` (deontic bond).
* **Purpose / use‑domain:** ops/governance vocabulary connecting ITSM, organizational policy, and pragmatics; separates saying, binding, and promising.
* **NQD‑front (seed candidates):**  
  *promise:* *Service*, *Offering*, *Provision*, *CapabilityOffer*  
  *utterance:* *SpeechAct*, *Performative*, *Utterance*, *Declaration*  
  *deontic bond:* *Commitment*, *Obligation*, *Binding*, *Duty*
* **Chosen from frontier (Unified Tech / Plain):**  
  `U.Service` / “service (promise)”; `U.SpeechAct` / “utterance”; `U.Commitment` / “commitment”.  
  *Discarded highlights:* **Offering** (business‑model connotations); **Declaration** (too narrow for performatives); **Obligation** (legalese; narrower than commitment envelope).
* **Bridges:** utterance **institutes** commitment; commitment **binds** service clause; no synonymy claimed.
* **Why it matters:** Status tracking becomes intelligible without pretending that a “service” acts; the NQD‑front yields neutral, cross‑tradition readable labels. (F.12; F.17 blocks D/R.)

### Example 3 — *Characteristic* names without lifecycle bias

* **Context harvest:**
  *Quality canon:* “maturity level”; *Performance canon:* “throughput”.
 **Kind:** `U.Characteristic` (measurement names).
* **Purpose / use‑domain:** CHR‑compatible measurements for planning and performance; bridgeable across engineering and management.
* **NQD‑front (seed candidates):**  
  *readiness (ordinal):* *MaturityLevel*, *ReadinessLevel*, *PhaseReadiness*, *TRL*, *ReadinessScore*  
  *throughput (ratio):* *Throughput*, *Rate*, *ProcessingRate*, *OpsPerSecond*, *FlowRate*
* **Chosen from frontier (Unified Tech / Plain):**  
  `U.ReadinessLevel` / “readiness level” (ordinal); `U.Throughput` / “throughput” (ratio).  
  *Discarded highlights:* **TRL** (tied to a specific scale/tradition); **Rate/OpsPerSecond** (over‑specific units baked in).
* **Narrative:** Dynamics are shown as **movement in state‑space**, not via lifecycle‑laden names such as “pre‑production process”.
* **Why it matters:** Prevents lifecycle/time from leaking into labels; the NQD‑front ensures neutrality and recognizability. (A‑series CHR rationale; F.17 §4–§6.)

### 19 · FAQ (authoring hygiene)

**Q1. How many Contexts must a naming proposal cite?**
**A.** The **sheet** for a thread should cite **≥ 3** distinct Contexts overall; an individual row may cite fewer if the concept appears in fewer Contexts. The point is breadth at the **UTS** level, not token‑stuffing rows. (F.17 §6 constraint.)

**Q2. Can a Source Context’s term ever become the Tech label?**
**A.** Only if its form is **already neutral** and does **not** smuggle in that Context’s private commitments. When in doubt, pick a fresh neutral Tech label and keep the Source term in **SenseCells**. (F.5.)

**Q3. Where do we put discipline‑vantage views like “Operations” vs “Research”?**
**A.** Use the **discipline columns** in a teaching layout if helpful, but remember: **discipline columns are not Context columns** and carry no editions. (F.17 §5.)

**Q4. How do we keep names stable while the story evolves?**
**A.** Keep **row ids** stable; evolve placement via the **Block Plan** and record moves in **Notes**. Use F.13 for renames/splits/merges. (F.17 §16; F.13.)

**Q5. What if two teams insist on different Tech labels for the same concept?**
**A.** Publish **one** Tech label; treat the other as a **deprecated alias** (Annex). Bridge their local senses on the row. (F.13; Part H.)

---

### 20 · 90‑second teaching script (for engineer‑managers)

> “**Local‑first** means we start in **context of meaning**—we harvest terms **inside** each Context and only then unify. A unified name is a **teachable promise**: one **Tech** label for precision, one **Plain** label for outreach. Its **row** in the **UTS** shows where the idea lives in real disciplines (the **SenseCells**) and how those Contexts connect (explicit **Bridges** with a brief loss note). We never equate terms by spelling; we argue sameness with a **bridge**. We also never bake stages or actors into names—those belong to **dynamics** and **roles**, not labels. When the story changes, we evolve names with **lexical continuity** rather than re‑inventing words. The result is a vocabulary managers and engineers can **hold on one page** and use the same way across projects.”

### 21 · Acceptance Harness (SCR/RSCR) for F.18

**Purpose.** Provide auditable, notation‑independent checks that a proposed unified name (and its publication on a UTS line) satisfies the **local‑first** unification discipline. The harness extends the general unification checks in **F.15** with **naming‑specific** obligations.

#### 21.1 Static Conformance Rules (SCR‑UNIFY)

| ID                                                                                                                                                                                                       | Requirement (normative “SHALL/SHALL NOT”)                   | Why this exists (conceptual)                                 | Where this is reflected |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------ | ----------------------- |
| **SCR‑U‑01 (Row‑first).** A unified Tech/Plain name **SHALL** be published **only** on a **Concept‑Set row** whose cells are SenseCells drawn from declared Contexts. No free‑floating names.               | Names are *lenses* onto a defended **row**, not vice‑versa. | **F.7** row‑as‑unit; **F.17** UTS row discipline.            | §F.7; §F.17             |
| **SCR‑U‑02 (Bridge‑only equivalence).** Cross‑context sameness **SHALL** be claimed **only** via an explicit **Bridge** with a relation kind and **CL** + loss/fit note.                                    | Prevents “string‑match identity”.                           | **F.9** Bridges; **F.0.1** principles.                       | §F.9                    |
| **SCR‑U‑03 (Neutral Tech).** The **Unified Tech** label **SHALL** be **neutral**—not lifted wholesale from any single Context **unless** the row’s Concept‑Set shows exact identity.                        | Avoids importing a local worldview as global.               | **F.5** naming neutrality; **F.17** 9.8 naming neutrality.   | §F.5; §F.17             |
| **SCR‑U‑04 (Twin registers).** Each row **SHALL** carry **Tech** and **Plain** names with the Part E register discipline; Plain is teacher‑friendly, Tech is morphology‑stable.                          | Satisfies didactic primacy without jargon creep.            | **E.10** registers; **F.5** naming rules.                    | §E.10; §F.5             |
| **SCR‑U‑05 (No window‑in‑name).** Variations by **time/phase/scale** **SHALL** be handled by **applicability windows** on **Statuses** (or examples), **NOT** by baking modifiers into the unified name. | Prevents type/status explosion by adjectives.               | **F.10/F.12** windows; **F.14** explosion guard.             | §F.10; §F.12; §F.14     |
| **SCR‑U‑06 (Heterogeneity).** A UTS block **SHALL** demonstrate **≥ 3** independent domain families across its rows, or an explicit Bias‑Annotation shall scope the claim.                               | Enforces trans‑disciplinary reach or honest scope.          | **F.17** invariants 3; **E.8** Bias‑Annotation.              | §F.17; §E.8             |
| **SCR‑U‑07 (Member≠Component sanity).** Names **SHALL NOT** imply holarchic composition when the row unifies **collections**; keep **MemberOf** distinct from **ComponentOf**.                           | Stops structural category errors.                           | Part F principles / anti‑patterns.                           | §9.8; §13               |
| **SCR‑U‑08 (One‑breath rationale).** Each row **SHALL** include a **single‑sentence** Unification Rationale that states **why** the cells denote the same thing despite wording differences.             | Keeps the argument visible and auditable.                   | **F.17** invariant 7.                                        | §F.17                   |
| **SCR‑U‑09 (Alias budget).** Per register, legacy aliases on a unified name **SHALL** be **≤ 1**; additional legacy labels go to Annex/Glossary.                                                         | Controls lexical drift while preserving continuity.         | **F.13** alias budget rule.                                  | §F.13                   |
| **SCR‑U‑10 (No Cross‑context rename).** A rename **SHALL** occur **within** the same Context or same row; Cross‑context “renames” are **prohibited**—use Bridges.                                                 | Keeps locality intact; forbids silent conflation.           | **F.13** continuity; **F.9** Bridges.                        | §F.13; §F.9             |
| **SCR‑U‑11 (Semantic read‑through).** A unified Tech/Plain name **SHALL** pass a **semantic read‑through**: the Name Card lists **5–10 diverse NQD archetypal situations** and the **NQD‑front notes** record rejected candidate and their **mismatch patterns**. | Prevents labels that mislead across the intended situations; ties lexical choice to demonstrated use. | §F.18 §4.2; §F.18 §5. | §F.18 |

#### 21.2 Regression Rules (RSCR‑UNIFY)

| ID                                                                                                                                                                       | Regression duty across editions                                        | Effect |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- | ------ |
| **RSCR‑U‑E01 (Edition drift).** When a source Context updates, re‑validate the row: stable sense ⇒ **rename/alias**; changed sense ⇒ **split/merge** rows; never overwrite. | Preserves truthfulness without erasing history. **F.13** RSCR.         |        |
| **RSCR‑U‑E02 (CL honesty).** Bridges **SHALL NOT** increase their CL (claiming stronger sameness) without new witnesses; **SHOULD** reduce CL when editions diverge.     | Guards against optimism bias in equivalence. **F.17** migration cues.  |        |
| **RSCR‑U‑E03 (Alias creep).** Periodically prune aliases to the **≤ 1** budget per register.                                                                             | Maintains narratively crisp UTS. **F.13** RSCR‑Alias.                  |        |
| **RSCR‑U‑E04 (Name neutrality check).** If the Unified Tech label is traceable to one context’s idiom, re‑justify neutrality or retitle the row.                            | Keeps the name “ours,” not “theirs.” **F.17** 9.7–9.8.                 |        |
| **RSCR‑U‑E05 (Window misuse).** Reject newly proposed types that are really **windows** on an existing Status/Role.                                                      | Prevents explosion by adjectives. **F.14** S14/E11 patterns.           |        |

### 21 · Migration & Deprecation Notes (informative, naming‑specific)

1. **Start from rows, not strings.** When consolidating legacy labels, **build or revisit the Concept‑Set row** first; only then pick the **Unified Tech/Plain** names. This keeps **meaning** primary. **(F.7, F.17)** 
2. **Prefer alias over merge.** If the *sense* is stable but the label misleads, **rename and retain one alias**; if the sense changed, **mint a new row** (no retrofits). **(F.13)**
3. **Resist modifier types.** New adjectives (e.g., *Peak*, *Remote*, *Night*) usually belong to **windows** or **examples**, not to the unified name. **(F.10/F.12/F.14)** 
4. **Keep neutrality visible.** If stakeholders push a brand‑coloured label, document why the chosen **Unified Tech** is **neutral** and include the brand as an **alias** in Glossary/Annex. **(F.5, F.17)** 
5. **Don’t globalise a Context.** Never move a Context label into the unified name as if it were universal. Use **Bridges** to relate Contexts, with an explicit **loss note**. **(F.0.1, F.9)** 

### 22 · FAQ (authoring hygiene for engineer‑managers)

**Q1. Can we reuse a dominant industry term as the Unified Tech name?**
**A.** Only if the row’s Concept‑Set shows **exact identity** across Contexts; otherwise pick a **neutral** Unified Tech and list the industry label as an **alias** in the Glossary. **(F.5, F.17)** 

**Q2. Two terms look identical across Contexts—may we skip Bridges?**
**A.** No. **Sameness is argued, not spelled.** Publish a **Bridge** with relation kind and **CL** plus a short **loss/fit** note. **(F.9, F.0.1)** 

**Q3. When do we mint a new U.Type vs. add a new row vs. add an alias?**
**A.** Use **F.8 Mint‑or‑Reuse**: if the *intension* changes, **new U.Type**; if the *same thing* spans new Context, **new row**; if only the label misleads, **alias/rename**.

**Q4. Our team keeps proposing “qualified roles” (e.g., *Night‑Operator*). What do we do?**
**A.** Keep the **Role** unified and express qualifiers as **windows** on **Statuses** or as **example context**. This follows **F.14** and **F.12**.

**Q5. Can we compress two near‑equivalent rows into one to “simplify the sheet”?**
**A.** Only if the **one‑breath rationale** remains true after review and the Bridges support equivalence with the same or stronger CL; otherwise keep **two rows** with explicit differences. **(F.17, F.9)** 

### 23 · Didactic distillation (90‑second script)

> **“Name on a row, never on a whim.”** In FPF we **speak on rows, not on vibes**: a **Name Card** ties each Tech/Plain pair to a concrete Context, Concept‑Set row, and SenseCells, with a small **NQD‑front** of rejected alternatives. This gives you **bridged precision** without losing **local comfort**. **Your UTS is the one page a careful mind can hold.**

### 24 · SoTA‑Echoing (post‑2015 practice alignment)

* **Neural WSD & sense evaluation (2015→).** P2’s sense‑seed read‑through is a human‑scale analogue of modern **word‑sense disambiguation** evaluation, where models are scored by the fraction of examples assigned the correct sense and by error profiles across sense inventories. Post‑2015 neural WSD benchmarks (e.g., multi‑domain evaluations reported in ACL venues) motivate the explicit `{too‑narrow, on‑target, too‑wide, wrong‑prototype}` labelling and the `θ_P` threshold for **SemanticFidelity**.
* **Quality‑Diversity & multi‑objective search (MAP‑Elites, NSGA‑II families, 2015→).** P1’s NQD‑front and **CC‑F18‑13** follow the same discipline as QD/NSGA‑style archives in optimisation: maintain a **set of non‑dominated candidates** over a vector of objectives rather than a single scalar score. The lexical Q‑tuple `{SemanticFidelity, CognitiveErgonomics, OperationalAffordance, AliasRisk}` is deliberately small so that human authors can inspect a Pareto frontier in the same way QD methods expose illumination archives.
* **Design‑space exploration & idea ranking (mechanical/industrial design, 2018→).** The PSOA‑style Name‑Card tables echo contemporary **design‑space ranking** practice, where candidate concepts are compared on diversity and quality rather than on a single “score”. Explicitly surfacing *why* one candidate dominates another improves auditability and supports teaching, mirroring recent work on ranking ideas for both diversity and quality in engineering design.
* **Semantic transparency & morphology in interfaces and code (HCI and PL practice, 2015→).** The strengthened **OperationalAffordance** guidance aligns with empirical results on **semantic transparency** of labels and identifier names: morphology that cues “actor vs activity vs artifact” improves comprehension and reduces error rates in both UIs and source code. F.18 turns these findings into a simple naming discipline (agentive forms for Roles, verbal forms for Methods, result nouns for Work/Artifacts) that can be enforced on Name Cards.

### 25 · Relations

**Builds on:**
**F.0.1** Contextual Lexicon Principles (local meaning; bridge‑only Cross‑context claims). **F.1–F.3** Contexts → term harvesting → local sense clustering. **F.5** Naming discipline. **F.7** Concept‑Set construction. **F.8** Mint‑or‑Reuse decision lattice. **F.13** Lexical continuity (renames/aliases/splits/merges). **F.14** Anti‑explosion controls (bundles, SoD, windows). **F.15** SCR/RSCR harness. **F.17** UTS as the publication surface.  

**Constrains:** 
All patterns that propose or consume unified names and rows in Part F; any Part A/C pattern that cites U.Types on UTS rows inherits these naming duties (through the UTS linkage), while keeping **structural/epistemic/temporal** aspects distinct per Part E authoring rules.

**Coordinates with.**
**A.17/A.18** for measurement lexicon when rows concern measurable notions (Characteristic/Scale/Level/Coordinate vocabulary), ensuring neutral naming aligns with canonical terms and eases external alignment via Bridges.  
