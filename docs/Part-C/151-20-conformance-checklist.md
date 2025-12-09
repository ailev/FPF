## 20 · Conformance Checklist (pattern‑level, normative)

> *Pass these and your CS modelling remains a thinking architecture, not a team‑management manual.*

**CC‑C17‑1 (context‑local CS).**
Every **CreativitySpace** (the characteristic set where ideation and selection are measured) **MUST** be defined *inside one* `U.BoundedContext`; all characteristics and their scales are local to that Context. (Bridges with CL penalties are required across Contexts; see §C.17.16.)

**CC‑C17‑2 (Characteristics, not “characteristics”).**
Each CS dimension **SHALL** be a named **Characteristic** per **MM‑CHR**, with kind (`qualitative`, `ordinal`, `interval`, `ratio`, or `set‑valued`), unit/scale, polarity, and admissible operations. No free‑floating coordinates. (A.CHR‑NORM / A.CSLC‑Kernel.)

**CC‑C17‑3 (Profile ≠ plan).**
A **Profile** is a *state description over characteristics* (what the option *is* in CS); a **Plan** or **Method** is *how you will act*. Never encode choices or schedules into the profile.

**CC‑C17‑4 (Portfolio = set + rule).**
A **Portfolio** is a set of candidate profiles **plus** a selection rule (objective + constraints) declared *in the same Context*. Presenting only a scatterplot is non‑conformant.

**CC‑C17‑5 (Dominance operator well‑typed).**
A dominance claim **MUST** name the **characteristic subset and polarity** under which it is evaluated. Dominance on incomparable scales (or mixed polarities without explicit transformation) is invalid.

**CC‑C17‑6 (Frontier from rule, not from taste).**
A **Frontier** (Pareto or constraint‑bound) **SHALL** be computed from the declared selection rule; drawing a “nice hull” by eye fails conformance.

**CC‑C17‑7 (Search–Exploit as **dynamics**, not policy dogma).**
Exploration/exploitation **MUST** be expressed as a **dynamics on the portfolio measure(s)** (e.g., exploration share as a function of marginal value of information), *not* as a prescriptive budget recipe. (Design‑time statements belong to Decsn‑CAL; see §C.17.16.)

**CC‑C17‑8 (Evidence Graph Referring for scores).**
Any numeric score in a profile **MUST** cite its **MeasurementTemplate** (MM‑CHR) and the **observation/evaluation** that yielded it. No anonymous numbers.

**CC‑C17‑9 (Separable uncertainty lanes).**
Keep **aleatory** vs **epistemic** uncertainty separate on characteristics; their combination rule **MUST** be stated (e.g., interval arithmetic, conservative bound).

**CC‑C17‑10 (Time is explicit).**
Comparisons across iterations **MUST** state `TimeWindow` (snapshot window) and whether *drift* or *refit* occurred (§C.17.14). “Latest” is not a time selector.

**CC‑C17‑11 (No proxy collapse).**
If a composite “creativity index” is used, its **aggregation algebra** (weights, monotone transforms) **MUST** be declared; the primitive characteristics remain queryable.

**CC‑C17‑12 (Work stays on Work).**
Resource/time actuals and run logs live on `U.Work`; CS never carries actuals. We reason **about** profiles/portfolios; we do not audit operations here.


### 21 · Worked‑Context Handbooks (concept cards, not runbooks)

> *Each Context publishes one page per card. These are **thinking kernels**: priors, objectives, admissible characteristics, and example transforms. No staffing, no process charts.*

**(a) Kernel Card — “What is a creative win here?”**

* **Context:** `<Context/Edition>`
* **Purpose Characteristic(s):** what “win” means (e.g., *Novelty*, *Usefulness*, *Adoptability*), with polarity and admissible ops.
* **Constraint Characteristics:** *Risk*, *Cost of change*, *Time to learn*, etc.
* **Objective** *(Decsn‑CAL pointer)*: Maximise `<purpose>` subject to declared constraints.
* **Frontier Rule:** Pareto over `{purpose ↑, risk ↓, cost ↓, time ↓}`.
* **Evidence Hooks:** which observations/evaluations populate each characteristic.

**(b) Priors Card — “What we believe before seeing data.”**

* **Default priors** on uncertainty for each characteristic (e.g., Beta for adoption probability).
* **Bridge policy:** minimal CL acceptable for imported profiles.
* **Exploration prior:** initial exploration share as a function of prior entropy.

**(c) Objective Variants Card — “Admissible objective shapes.”**

* Catalog the *few* objective forms this Context allows (lexicographic tie‑break, ε‑constraint, max‑min fairness), with **didactic pictures** of their frontiers.
* State when to switch objective (e.g., during bootstrapping vs exploitation).

**(d) Ready‑to‑use transforms** *(MM‑CHR aligned)*

* Monotone maps (e.g., log utility), normalizations, ordinal→interval “do & don’t” (only with evidence of order‑to‑interval validity).
* **Forbidden transforms** list (e.g., averaging ordinal ranks).

These cards are *conceptual fixtures*; **Tooling** may implement them, **Pedagogy** may teach them, but **C.17** only standardises their content as **thinking affordances**.

### 22 · Placement sanity‑check across the pattern language** *(avoid scope creep)

* **MM‑CHR (C.16):** defines **Characteristic/Scale/Unit/Measure** and the *characterisation discipline*. **All** CS dimensions live there; C.17 **uses** them, never re‑defines scales.
* **A.CHR‑SPACE (A.19):** exports **CharacteristicSpace & Dynamics hooks**; C.17 is a **Contexted specialisation** for creative reasoning (profiles/portfolios/selection).
* **Decsn‑CAL (C.11):** hosts **objective functions, constraints, preference orders, utility proofs**, and the **search–exploit dynamics** as decision policies. C.17 only **names** the hooks (objective, rule), keeps policy math out.
* **KD‑CAL (C.2) & B.3 (Trust):** carry **evidence provenance**, **assurance** and **congruence penalties (CL)** for Cross‑context reuse. C.17 requires anchors; it does not invent confidence calculus.
* **Compose‑CAL (C.13):** governs **set/union/slice** aggregation; the portfolio set is a **Γ\_m.set** over profiles; frontier is derived **without** ad‑hoc geometry.
* **B.4 Canonical Evolution Loop:** where *Run→Observe→Refine→Deploy* sits. C.17 supplies the **view** in which refinement is judged.

**Out of scope here:** team staffing, budgeting workflows, data‑governance procedures, ticket states, any “how to manage people”. This pattern organises **thought**, not **teams**.

### 23 · Anti‑patterns & canonical rewrites (conceptual hygiene)

1. **characteristic‑speak.** “Along the novelty characteristic…” → **Rewrite:** “Along the **Novelty characteristic** (ordinal; higher is better)…”.
2. **Pretty hulls.** Drawing a convex hull and calling it a frontier → **Rewrite:** compute Pareto under declared characteristic polarities.
3. **Ordinal arithmetic.** Averaging ranks or Likert values → **Rewrite:** either treat as **ordinal** and use **order‑safe** operators, or justify an interval mapping via MM‑CHR evidence.
4. **Proxy tyranny.** Single composite index driving choice unseen → **Rewrite:** publish **primitive characteristics**, index formula, and sensitivity.
5. **Policy‑as‑math.** “10% wild bets” as a rule → **Rewrite:** declare an **exploration dynamics** tied to value‑of‑information; if keeping a heuristic, label it as such.
6. **Global meaning.** Porting a profile from another Context by name → **Rewrite:** attach a **Bridge** with CL and loss notes; adjust trust, not scales.
7. **Plan‑profile blur.** Putting milestones into profiles → **Rewrite:** move schedules to `U.WorkPlan`; keep CS for *how options compare*, not *how to execute*.

### 24 · Minimal didactic cards (one screen each)

**(1) Profile Card**

* **Option id & Context**
* **Characteristics table** (value, unit/scale, uncertainty split)
* **Evidence Graph Ref** (Observation/Evaluation ids)
* **Notes** (bridges used, CL penalties)

**(2) Portfolio‑with‑Rule Card**

* **Set of candidate profiles (refs)**
* **Objective & constraints** (Decsn‑CAL pointer)
* **Dominance subset** & **Frontier snapshot** (with TimeWindow)
* **Delta vs previous** (entered/exited/moved)

**(3) Search–Exploit Card** *(conceptual)*

* **Exploration share** as function of **marginal VOI** (symbolic)
* **Update cadence** (TimeWindow policy)
* **Stop conditions** (e.g., VOI below threshold; risk bound reached)

**(4) RSCR Summary Card**

* **What changed?** (refit/Δ±)
* **Sentinels status**
* **Frontier churn**
* **Bridge CL drift**

These cards are **thinking scaffolds**; they do not prescribe org process.

### 25 · Consequences (informative)

| Benefit                    | Why it matters                                                                                                                    |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **context‑local rigour**      | Creative comparison is made decidable *where meaning lives*; Cross‑context reuse is explicit and penalised only in trust, not scale. |
| **Frontier honesty**       | Decisions rest on declared characteristics and polarities; frontiers follow rules, not taste.                                     |
| **Temporal comparability** | RSCR prevents silent drift; “better/worse” claims retain meaning over iterations.                                                 |
| **Method independence**    | Any tooling can implement the cards; C.17 remains a conceptual API for thought.                                                   |

**Trade‑offs:** upfront ceremony (declare characteristics, polarity, TimeWindow) and disciplined bridges. The payoff is comparability and explainability.

### 26· Open questions (non‑normative, research hooks)**

* **Information geometry of CS:** can certain Contexts justify canonical distance metrics across characteristics without violating MM‑CHR parsimony?
* **Multi‑agent exploration:** how to couple individual CS frontiers into a *co‑exploration* equilibrium without importing team governance?
* **Learning‑to‑rank vs measurement:** what minimal evidence suffices to treat an ordinal characteristic as interval for the purpose of frontier estimation?

