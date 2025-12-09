## C.24 — Agentic Tool‑Use & Call‑Planning (C.Agent‑Tools‑CAL)  \[A]

**Status.** Architheory specification (**CAL**). Defines the conceptual calculus for **agentic selection and sequencing of tool calls** under budgets, trust gates, and policy. **ΔKernel = 0** (no kernel primitives added). *Minting note:* this CAL **does not mint** new U‑types; it **aliases** canonical U‑types where appropriate via **E.10/UTS**.

**Instantiates / Refines Pillars.** E.2 P‑3 Scalable Formality, P‑7 Pragmatic Utility, P‑10 Open‑Ended Evolution, P‑11 SoTA Alignment, and the **Bitter‑Lesson Preference** (prefer scalable, general methods that benefit from more data/compute over fragile hand‑tuned heuristics when assurance/cost are comparable).

**Depends on.** A‑kernel (A.1–A.15) for holonic basics and **Role–Method–Work** separation; **B.3** Trust & Assurance (F–G–R with CL penalties); **E.3/E.5** (precedence & Guard‑Rails); **C.5** Resrc‑CAL; **C.18** NQD‑CAL (candidate generation/portfolio); **C.19** E/E‑LOG (explore–exploit policies); **optional** Compose‑CAL and KD‑CAL (knowledge dynamics) where available.

**Coordinates with.**
U.WorkPlan and U.Service bindings (acceptance gates), Working‑Model publication discipline (**per B.3**), Evidence/Provenance (G.6).

### 1) Problem frame

Modern systems increasingly rely on **agents** that can **choose tools** (services/methods) and **plan sequences** of calls to achieve objectives in uncertain contexts. Without a calculus:

* calls are scheduled by **ad‑hoc heuristics**,
* **budgets** (compute, cost, wall‑time) are implicit,
* **assurance** and **policy provenance** are lost, and
* agents either over‑constrain themselves with brittle scripts or wander without guard‑rails.

This CAL provides the **conceptual API for thought** that lets any implementation (LLM‑based, search‑based, code‑based, robotic) plan calls **lawfully**, **audibly**, and **scalably**. (Role–Method–Work alignment; didactic primacy.)  

### 2) Problem

We need a **tool‑agnostic** way to (i) identify **admissible tools**, (ii) **score** candidate call sequences, (iii) allocate an **explore/exploit** share, (iv) enforce **budget & harm** gates, and (v) **replan** on signals—**without** baking domain‑specific heuristics into the core and **without** violating B.3 assurance discipline. 

### 3) Forces

| Force                              | Tension                                                                                                        |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **General methods vs. hand‑craft** | Scalable, model‑centric search ↔ short‑term wins of bespoke scripts (guarded by **Bitter‑Lesson Preference**). |
| **Assurance vs. Autonomy**         | F‑G‑R gates & CL penalties ↔ agent freedom to sequence calls and learn online.                                 |
| **Exploration vs. Delivery**       | Exploration share for illumination ↔ delivery SLAs and cost ceilings (E/E‑LOG policy).                         |
| **Separation of concerns**         | Planning (MethodDescription) ↔ execution (Work) ↔ service promises (U.Service).                                |

### 4) Solution — Signature & Realization

**Types (aliases).**
*`ATC.CallSpec`* ≡ `U.MethodDescription` with `accessSpec` for a tool service;
*`ATC.CallPlan`* ≡ `U.WorkPlan` specialised for tool invocations;
*`ATC.CallGraph`* ≡ Evidence/Provenance graph over a `U.Work` ledger;
*`ATC.Policy`* references `U.EmitterPolicyRef` (E/E‑LOG) and local call gates **including BLP tolerances (α, δ)**.

**Roles.**
A **System in AgentialRole** composes a **Plan** (MethodDescription); upon enactment, a **Performer** executes **Work** (calls), and **Observers** record **Observations** with acceptance checks. (A.15 strict distinction.) 

**Operators (Γ_agent; CAL, conceptual):**

1. `Γ_agent.eligible(tool, TaskSignature, K_ctx) → {true|false, notes}`
   *Eligibility gate* based on capability fit, policy allow‑list/deny‑list, and context K (incl. safety constraints).

2. `Γ_agent.enumerate(TaskSignature, K_ctx) → CandidateSet<ATC.CallSpec>`
   Returns admissible calls. **MAY** delegate to **NQD‑CAL** for portfolio enumeration when families are heterogeneous and **MUST** apply the current **E/E‑LOG lens** (objectives & gauges) to tag candidates.

3. `Γ_agent.plan(Objective, CandidateSet, Budget, ATC.Policy) → ATC.CallPlan`
   Produces a **call plan** with steps `{pre, call, post}`, *explicit budgets* (compute, cost, time, risk), and **E/E policy** (explore_share, tie‑breakers, stop‑conditions). The plan is a MethodDescription, not Work.  

4. `Γ_agent.execute(ATC.CallPlan) → {ATC.CallGraph, Observations}`
   Executes with **hard gates** (budget, risk, constraint‑fit) and logs provenance suitable for B.3 assurance reporting (design/run separated). 

5. `Γ_agent.replan(Signals, ATC.CallPlan, Budget′) → ATC.CallPlan′`
   Triggered by sentinel breaches, assurance drops, or policy events; preserves **editioned** policy and context. (Design/run separation; Working‑Model handshake.) 

6. `Γ_agent.score(Plan or Step) → ⟨ValueProxies, Cost, Risk, FGR_floor⟩`
   Computes selection signals **without** illegal scalarisation across mixed scales; **uses Pareto comparison under the C.19 E/E‑LOG lens** and defers final dominance to declared policies. 

**Normative Laws (ATC‑Laws).**

* **ATC‑1 (Model‑the‑Call, not the App).** A tool call is a **Work** instance that enacts a referenced **MethodDescription** promised by a **Service**; plans schedule calls but are **not the calls**. (A.15.)
* **ATC‑2 (Bitter‑Lesson Preference).** When two admissible choices are within **δ (assurance)** and **α (budget)**, **prefer the more general, scale‑benefiting method** whose **slope vector Pareto‑dominates** under the declared E/E‑LOG objectives; any override **MUST** record a **BLP‑waiver** with expiry. (E.2; precedence governed by E.3.)
* **ATC‑3 (Budget & Harm Gates).** Plans **SHALL** declare ceilings on compute, cost, wall‑time, and risk; execution **MUST** abort or replan on breach. (Assurance ties to B.3; design/run kept separate.)
* **ATC‑4 (Explore‑Share Discipline).** Plans **MUST** declare `explore_share`; defaults **inherit from E/E‑LOG profiles**. **Informative defaults**: `0` for safety‑critical or deterministic tasks; `≈0.2–0.4` for ambiguous tasks with heterogeneous tool families. Promotion of illumination gauges into dominance **requires explicit policy**.
* **ATC‑5 (Provenance & Replay).** Every call **MUST** emit a **CallGraph** with: Service id, MethodDescription edition, inputs/outputs (redacted per privacy), **EmitterPolicyRef**, and budget deltas. (NQD/E/E provenance fields apply when used.)
* **ATC‑6 (Assurance‑First Decisions).** Selection **MUST** respect B.3: WLNK minima on F/R (weakest‑link floors), CL penalties on integration, and **no** chimera scores across design/run. Publish **⟨F,G,R⟩** for the *typed claim* “this plan is admissible under K,S”.
* **ATC‑7 (Notation/Vendor Independence).** Core pattern text **MUST NOT** encode vendor‑specific tokens; bindings occur in Context via Bridges/Profiles. (Lexical guard‑rails.)


### 5) Policy Block (normative, profile‑able)

**ATC‑Policy fields (conceptual):**
`{ backstop_confidence, explore_share, risk_bound, cost_ceiling, time_ceiling, tie_breakers, novelty_quota?, wild_bet_quota?, stop_conditions, BLP_delta_α, BLP_delta_δ }` — realized by referencing an **E/E‑LOG EmitterPolicy** and adding **BLP** clauses. Defaults inherit from E/E‑LOG; any deviation is editioned.

**BLP Precedence.** In conflicts with tactics that hard‑code narrow scripts, **BLP** applies **subject to E.3/E.5 precedence**. Where scripts encode **safety‑critical gating or regulatory compliance**, scripts **prevail** unless a DRR records: (i) **override rationale**, (ii) **expiry**, (iii) **measured hazard** avoided, and (iv) planned **re‑evaluation** window (P‑10 evolution duty).

### 6) Archetypal Grounding (informative; non‑binding)

1. **LLM Research Agent (knowledge work).**
   Task: answer a novel technical question. Candidate tools: retrieval, structured web search, code runner, table/plot generator.
   **Plan:** `enumerate → plan(explore_share≈0.4) → call(search→retrieve→synthesise→code‑check) → replan on sentinel (low R)`; **BLP** favours **general retrieval + prompting policies** over hand‑coded, per‑site scrapers unless assurance demands otherwise. (Echoes SoTA: *ReAct* (2022), *Self‑Ask* (2022), *Reflexion* (2023), *Tree‑of‑Thoughts* (2023), *Toolformer* (2023).)

2. **Program Repair Agent (systems/software).**
   Task: propose a patch against a failing test suite. Candidate tools: repo introspection, static analyzer, unit runner.
   **Plan:** prefer **search‑and‑learn loops** with test‑guided feedback over fixed “if error X then patch Y” tables; exploration quota enforces trials across patch families before exploitation. (Aligns with post‑2019 automated program repair lines and *SWE‑bench*‑style agent loops.)

3. **Lab Automation Agent (physical).**
   Task: adjust a wet‑lab protocol under drift. Candidate tools: planner, pipetting controller, spectrometer, Bayesian optimizer.
   **Plan:** **BLP** drives toward **model‑based optimization** under budgeted sample counts; heuristics remain as **policy‑documented** fallbacks with expiry. (Resonates with quality‑diversity and BO practice since 2015, mirrored by NQD/E/E policies.) 

### 7) Conformance Checklist (CC‑AT)

1. **CC‑ATC‑1 — Declared separation.** Plan is a `MethodDescription`; execution is `Work`; acceptance is via `U.Service`. No schedule inside specs; schedules live in `U.WorkPlan`.
2. **CC‑ATC‑2 — Budgets on record.** `time/compute/cost/risk` ceilings exist **ex ante**; stop conditions listed.
3. **CC‑ATC‑3 — E/E policy.** `EmitterPolicyRef` (or equivalent) and `explore_share` are editioned and logged.
4. **CC‑ATC‑4 — Assurance tuple.** Publish the **typed claim** “Plan admissible under K,S” with **⟨F,G,R⟩** and CL penalties traceable in the **CallGraph** SCR. Design/run never merged.
5. **CC‑ATC‑5 — BLP waiver discipline.** Any heuristic override against a general method includes **expiry** and **re‑evaluation** date.
6. **CC‑ATC‑6 — Provenance minimum.** Record `{ServiceRef, MethodDesc.edition, EmitterPolicyRef, DescriptorMapRef? (if NQD), DistanceDefRef? (if NQD), TimeWindow, Seeds?, Dedup?}`.
7. **CC‑ATC‑7 — Notation independence.** No vendor tokens in conceptual text; bindings via Bridges/Profiles only.
8. **CC‑ATC‑8 — BLP tolerances declared.** **α/δ** tolerances are present in `ATC.Policy` or referenced via the active E/E‑LOG profile.

### 8) Consequences

*Positive.* Portable agent patterns; **auditable autonomy**; lawful exploration; faster hypothesis cycles via BLP; replayable call graphs; decision‑grade Working‑Model surfaces.
*Trade‑offs.* Requires explicit budgets/policies; BLP may defer quick wins from bespoke scripts; stronger logging discipline.

### 9) Rationale (post‑2015 SoTA alignment, informative)

* **Scaling‑first methods** (language‑model and representation‑learning scaling laws; subsequent data/compute‑balanced scaling) empirically support **BLP**: general, learnable mechanisms tend to dominate as budgets rise—hence **ATC‑2**.
* **Tool‑use agents** in the literature (*ReAct*, *Self‑Ask*, *Reflexion*, *Toolformer*, *Tree‑of‑Thoughts*, open‑ended *Voyager*‑style skill acquisition) all benefit from **explicit planning + feedback**, exactly what CC‑AT‑2/3/6 encode.
* **Quality‑Diversity & BO** practice motivates the **explore_share** default and the distinction between **dominance vs. illumination gauges** (kept separate unless policy promotes).  

### 10) Relations

* **Builds on:** A.15 Role–Method–Work alignment (planning vs execution vs service), B.3 Trust & Assurance (F–G–R/CL), C.5 Resrc‑CAL, C.18 NQD‑CAL (candidate/portfolio), C.19 E/E‑LOG (policies).    
* **Constrains:** Any `U.Service` used as a “tool” MUST expose acceptance conditions and observation hooks sufficient for B.3 reporting. 
* **Enables:** Human‑centric Working‑Model surfaces with policy/assurance disclosures (design/run separated). 

### 11) Bias‑Annotation

*Lexical firewall* and *notation independence* apply; no vendor tokens; mixed‑scale characteristics are never averaged; illumination remains a **gauge** unless a policy promotes it into dominance.  

#### Didactic Quick Card (1‑screen crib)

**Agentic Call Plan (public):**
*Objective · Context(K) · Budget{time/compute/cost/risk} · PolicyRef (E/E‑LOG) · Explore‑share · Steps[ pre/ call /post ] · Stop‑conditions · **BLP tolerances (α,δ)** · BLP‑note (if any) · Assurance⟨F,G,R|K,S⟩ · Provenance ids.*
