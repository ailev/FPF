## **B.3 Trust & Assurance Calculus (F–G–R with Congruence)** \[A]

> **Plain‑English headline.**
> B.3 defines how **assurance** (trust) is **computed and propagated** for both physical systems and knowledge artifacts, using a small set of **characteristics** and **conservative aggregation rules** that respect the Γ‑invariants and A.15 **Strict Distinction**. It treats the **Working‑Model layer** as the **publication surface** for claims, with assurance **attached downward** (Mapping · Logical · Constructive · Empirical) per E.14.

### 1) Problem frame

Every non‑trivial result in FPF—*a composed system is safe*, *a model is credible*, *a conclusion holds*—is a **claim** that rests on **composed evidence**.

* For **U.System** holons (Γ\_sys), assurance is about *capabilities and constraints* under stated conditions.
* For **U.Episteme** holons (Γ\_epist), assurance is about the *quality of support* for a statement or model.

To make such claims comparable and auditable across domains, B.3 introduces a **Trust & Assurance Calculus** that:

* uses a **small set of characteristics** (F–G–R) governed by CHR principles (these are **not** a state space),
* accounts for **integration quality** via **Congruence Level (CL)** along the edges of a `DependencyGraph` (B.1.1, A.14),
* and composes these values with **Γ‑flavours** while respecting the **Invariant Quintet** (IDEM, COMM/LOC or their replacements, WLNK, MONO).

B.3 is **conceptual and normative**: it defines *what must be measured and how the measures propagate*. How you improve those measures (e.g., formalize, replicate, reconcile) is the job of KD‑CAL actions (the knowledge‑dynamics architheory; references are descriptive, not required to read here).

**Mechanism linkage.** For law‑governed operation families (e.g., **USM/UNM**) authored as **mechanisms**, use A.6.1 — U.Mechanism to publish **OperatorAlgebra/LawSet/AdmissibilityConditions** and the **Transport** clause (Bridge‑only, CL/CL^k/CL^plane). All such penalties **reduce `R/R_eff` only**; **F/G** remain invariant.

**Working‑Model handshake (alignment with E.14 · B.3.5 · C.13).**  
Assurance consumes two inputs declared at the **Working‑Model** surface (CT2R‑LOG, B.3.5): the **justification stance** `validationMode ∈ {postulate, inferential, axiomatic}` and, where present, the **grounding link** `tv:groundedBy`. Structural claims that aspire to the strongest guarantees rely on **Constructive** grounding as a **Γₘ** (Compose‑CAL) narrative referenced via `tv:groundedBy`. No assurance artefact **defines** Working‑Model wording or layout (downward‑only dependence, E.14).

### 2) Problem

Without a disciplined calculus, four chronic failures appear:

1. **Trust inflation:** Averaging or summing heterogeneous “quality” tags yields aggregates that look better than their weakest parts, violating WLNK.
2. **Scale confusion:** Mixing ordinal and ratio scales (e.g., averaging “formality levels” with numeric reliabilities) produces meaningless numbers.
3. **Congruence blindness:** Integration quality (how well pieces fit) is invisible; brilliantly strong parts connected by weak mappings produce overconfident wholes.
4. **Scope drift:** Design‑time formalism and run‑time evidence are composed into a single score; dashboards then claim “assurance” for a blueprint using live data, or vice versa.

---

### 3) Forces

| Force                                    | Tension                                                                                                                             |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Conservatism vs. Synthesis**           | Avoid overclaiming (WLNK) ↔ allow real gains from better integration (raise CL) or true emergence (B.2).                            |
| **Universality vs. Domain nuance**       | One calculus for systems and epistemes ↔ physics and epistemology use different primitives; keep them comparable but not identical. |
| **Simplicity vs. Fidelity**              | Keep the characteristic space small (A.11) ↔ capture enough structure to be informative and improvable by KD‑CAL actions.           |
| **Static clarity vs. Dynamic evolution** | A score must be reproducible today ↔ tomorrow it should legitimately rise after formalization, replication, or reconciliation.      |

---

### 4) Solution — **Part 1: The assurance tuple and the universal aggregation skeleton**

B.3 defines **what** to measure, **how** those measures live on nodes and edges of the dependency graph, and the **shape** of the aggregation that any Γ‑flavour must honor when producing an *assurance result*.

#### 4.1 The F–G–R characteristics (CHR‑compliant)

We standardize three characteristics on **nodes (holons)** plus one **edge** characteristic:

1. **Formality (F)** — *how constrained the reasoning is by explicit, proof‑grade structure.*

   * **Scale kind:** **ordinal** (levels do not admit arithmetic).
   * **Canonical levels (example):**
        `F0 Informal prose` · `F1 Structured narrative` · `F2 Formalizable schema` · `F3 Proof‑grade formalism`.
   * **Monotone direction:** higher is better (never lowers assurance when all else fixed).

2. **ClaimScope (G)** — *how broadly the result applies in the relevant domain space.*

   * **Scale kind:** **coverage / span** (set‑ or measure‑based; domain‑specific).
   * **Monotone direction:** larger, but only when **correctly supported** (see WLNK and CL below).

3. **Reliability (R)** — *how likely the claim/behavior holds under stated conditions.*

   * **Scale kind:** **ratio** in `[0,1]` (or a conservative ordinal proxy when numeric modeling is unavailable).
   * **Monotone direction:** higher is better.

2. **Congruence Level (CL)** — *edge property: how well two parts fit* (semantic alignment, calibration, interface Standard).

   * **Scale kind:** **ordinal** with a **monotone penalty function** `Φ(CL)` where `Φ` decreases as CL increases.
   * **Canonical levels (example):**
     `CL0 weak guess` · `CL1 plausible mapping` · `CL2 validated mapping` · `CL3 verified equivalence`.
   * **Interpretation:** low CL reduces the credibility of the *integration itself* (not the parts), and therefore **penalizes** the aggregate **R**.

> **Strict Distinction (A.15).**
>
> * Characteristics live at **value level** (they qualify holons or edges conceptually), while Γ‑flavours fold **structure/order/time**.
> * Do not smuggle characteristics into structural edges; keep them explicit on nodes/edges as CHR metadata.

> **Assurance shoulders (Working‑Model split).**  
> **Mapping** raises **TA** (typing, fit/CL). **Logical** and **Constructive** contribute to **VA** (intended relation semantics; Γₘ extensional identity for structure). **Empirical Validation** contributes to **LA** (evidence in a bounded context). These supports attach **downward** from the Working‑Model surface (E.14).

#### 4.2 Assurance as a typed claim

B.3 speaks about **assurance of a specific typed claim** `C` over a holon `H` under context `K` and scope `S ∈ {design, run}`:

```
Assurance(H, C | K, S) = ⟨F_eff, G_eff, R_eff, Notes⟩
```

* `C` examples: *meets load L*, *argument Q holds*, *model M predicts within δ*.
* `K` binds assumptions (environment, usage, priors).
* `Notes` include the **SCR** (all sources, B.1.3), **OrderSpec/TimeWindow** where applicable (B.1.4), cutsets, and evidence citations (A.10).

This tuple gives readers an at‑a‑glance view (didactic primacy) while preserving the pieces needed for audit and improvement.

**Validation modes (declaration, normative).** 
Each published Working‑Model assertion **SHALL** declare **`validationMode ∈ {postulate, inferential, axiomatic}`** (E.14).  
— *postulate* → pragmatic working claim; **Empirical Validation** is **required** for audit.  
— *inferential* → reasoned consequence; **Logical** assurance carries the burden.  
— *axiomatic* → constructive identity; **structural** edges MUST provide a Γₘ narrative and a **`tv:groundedBy`** pointer (C.13, B.3.5).

**Design vs run (no chimeras).** Assurance tuples for **design‑time** and **run‑time** SHALL be reported **separately** and **not composed into a single score**; see the *Scope drift* hazard in §2 and the obligations in B.3.3.

#### 4.3 Where the numbers live (and do not)

* **On nodes:** each input holon contributes its local `F, G, R` according to its nature (system vs. episteme).
* **On edges:** each integration step has a `CL` (congruence of the connection).
* **Not inside Γ:** Γ consumes `D` and returns a composed holon; B.3 governs how `F, G, R, CL` **propagate** to the **Assurance** tuple for that composed holon. This keeps Γ algebra and assurance calculus **separable** and reviewable.
* **Not a state space:** `⟨F,G,R⟩` is an **assurance tuple**, not a `U.CharacteristicSpace`; do **not** draw “trajectories” in `⟨F,G,R⟩`. For episteme evolution, use **ESG** states and the **assurance‑trace** hooks (see below).


---

#### 4.4 Universal aggregation skeleton (domain‑neutral)

Any Γ‑flavour that claims an **Assurance** result **must** adopt the following **conservative skeleton**:

1. **Formality:**

   ```
   F_eff = min_i F_i
   ```

   *Rationale:* the least formal piece caps the formality of the whole (WLNK on F).
   *Monotone:* raising any `F_i` cannot reduce `F_eff`.

2. **ClaimScope:**

   ```
   G_eff = SpanUnion({G_i}) constrained by support
   ```

   * “SpanUnion” is a **set/coverage union** in the domain’s space.
   * **Constraint:** any region in the union **unsupported** by reliable parts is **dropped** (WLNK).
   * *Monotone:* adding supported span cannot reduce `G_eff`.

3. **Reliability (penalized by integration):**

   ```
   R_raw = min_i R_i                       // Weakest-link cap
   R_eff = max(0, R_raw − Φ(CL_min))       // Congruence penalty
   ```

   * `CL_min` is the **lowest** congruence level on any edge in the proof spine / critical integration region for the claim `C`.
   * `Φ` is **monotone decreasing** and **bounded** (never makes negative values).
   * *Monotone:* increasing any `R_i` or any `CL` cannot lower `R_eff`.

4. **SCR and Notes:**
   * The aggregate SHALL produce a SCR listing all contributing nodes and edges, with their F, G, R, CL, scopes, and evidence links (A.10).  
   * The SCR SHALL additionally surface the **describedEntity** (`describe(Object→GroundingHolon)`) and the **ReferencePlane** for the claim, and present a **separable TA/VA/LA table** of evidence contributions with **valid_until/decay** marks and the **Epistemic‑Debt** per § B.3.4.  
   * If order/time mattered for the claim, attach the OrderSpec or TimeWindow identifiers (B.1.4).

This skeleton is **mandatory**. Domain‑specific architheories may add **refinements** (e.g., separate epistemic “replicability” vs. “calibration”) as long as they **do not violate** WLNK or MONO and preserve scale kinds.

---

#### 4.5 System vs. Episteme — same shape, different readings

* **For systems (Γ\_sys):**

  * `F` reads as **engineering discipline** (from ad‑hoc procedure to verified specification).
  * `G` reads as **operational envelope coverage**.
  * `R` reads as **assured reliability** under `K` (requirements, environment, test campaigns).
  * `CL` often arises at **interfaces** (Boundary‑Inheritance Standard; B.1.2): poorly controlled interfaces reduce `R_eff`.

* **For epistemes (Γ\_epist):**

  * `F` reads as **logical/semantic formality** (from prose to proof).
  * `G` reads as **domain span** (concepts, populations, conditions).
  * `R` reads as **evidential support** (replication quality, measurement integrity).
  * `CL` measures **semantic alignment** of merged constructs (terminology mapping, ontology bridges, calibration).

> **Agentness is separate (A.13).**
> Agency metrics (Agency‑CHR) **do not enter the skeleton by default**. They may act as a **contextual overlay** (e.g., to argue why a supervisory policy can maintain `R` across disturbances), but **never** to bypass **WLNK** or the **CL penalty**. Grade shifts should be modeled as **MHT** events when they create new capabilities.

---

#### 4.6 Scale discipline (CHR guard‑rails)

To prevent silent misuse:

* **Ordinal scales (F, CL):** never average or subtract; only `min`/`max`, thresholds, and monotone comparisons are allowed.
* **Coverage scales (G):** use union/intersection in a declared domain space; do not “average” sets. If a numeric proxy is used (e.g., coverage ratio), it **must** be derived from a set operation, not vice versa.
* **Ratio scales (R):** may be combined with `min`, `max`, or **explicitly justified** conservative functions; do not add R’s from different contexts without normalization of `K` (assumptions).

---

#### 4.7 What improves the tuple (action patterns, high‑level)

B.3 remains neutral about *how* improvement happens, but for didactic clarity:

* **Raise F:** formalize narratives (specifications, machine‑checked models).
* **Raise G:** enlarge supported span (new test regimes, new populations) with adequate evidence.
* **Raise R:** replicate, calibrate, tighten measurement error, reduce bias.
* **Raise CL:** reconcile vocabularies, align units, formalize mappings, verify interface Standards.

Each of these corresponds to recognizable **Transformer roles** and KD‑CAL moves (design‑time); their **run‑time** counterparts are covered by Γ\_time (phase evidence) and Γ\_work (cost of obtaining assurance).

### 4.8 Prohibition (normative) — F–G–R is not a CharacteristicSpace
Do not treat `⟨F,G,R⟩` as a `U.CharacteristicSpace` and do not define geometric **trajectories** over it. Use **ESG** for episteme state and the **assurance‑trace** hooks for trends in assurance tuples.

### 5) Proof obligations (attach these when producing an Assurance tuple)

These obligations refine the generic Proof Kit from **B.1.1 §6** for **assurance** outputs. Each Γ‑flavour that emits an *Assurance(H, C | K, S)* tuple MUST attach the applicable obligations below.

#### 5.1 Common obligations (all Γ‑flavours)

* **ASS‑CLM (Typed claim & context).**
  State the **claim** `C` (what is being assured), the **context** `K` (assumptions, environment), and the **scope** `S ∈ {design, run}`.

* **ASS‑SCA (Scale discipline).**
  Declare the **scale kind** used for each characteristic (F ordinal, G coverage, R ratio) and confirm that all operations are **admissible** for that kind (no averaging of ordinals; G via set/coverage ops).

* **ASS‑WLNK (Weakest‑link evidence).**
  Identify the **cutset** (node or edge set) that caps F/G/R for the claim (the proof spine for epistemes, the structural or assurance bottleneck for systems).

* **ASS‑CL (Congruence path).**
  Identify the **relevant integration path(s)** and record `CL_min` used in the penalty `Φ(CL_min)`.

* **ASS‑MAN (SCR).**
  Produce a **SCR** listing all contributing nodes and edges with `(F, G, R)` and `CL` values, their **DesignRunTag**, and Evidence Graph Ref (A.10). If order or time were material, include the **OrderSpec** or **TimeWindow** identifiers from **B.1.4**.

* **ASS‑MONO (Declared monotone characteristics).**
  List the characteristics along which local improvement cannot reduce the aggregate (this supports future evolution, B.4).

#### 5.2 Γ\_sys (systems) — additional obligations

* **CORE‑BIC (Interface congruence).**
  Reference the **Boundary‑Inheritance Standard** (BIC) from **B.1.2** and record any interface mismatches; these contribute to `CL_min`.

* **CORE‑ENV (Operating envelope).**
  Specify the domain used for **G** (e.g., load–temperature region) and how coverage is computed (set union constrained by support).

#### 5.3 Γ\_epist (epistemes) — additional obligations

* **EPI‑SPN (Entailment spine).**
  Identify the **premise/lemma spine** for the claim; `R_raw = min R_i` is taken along this spine, not over arbitrary satellites.

* **EPI‑MAP (Semantic mapping congruence).**
  Point to the **vocabulary/ontology mappings** used; their verification status sets the **CL** levels on the integration edges.

#### 5.4 Γ\_ctx / Γ\_method (order‑sensitive) — additional obligations

* **CTX‑ORD (OrderSpec).**
  Attach the partial or total order `σ` and any **join‑soundness** conditions (types, pre/post‑conditions).
  (See B.1.4 for NC‑1..3 invariants; B.1.5 adds duration/capability typing.)

#### 5.5 Γ\_time (temporal) — additional obligations

* **TIME‑COV (Coverage & identity).**
  Show that `PhaseOf` intervals cover the declared window without overlap for the **same carrier**; justify any gap/overlap explicitly.

> **Note on Γ\_work.**
> Resource spending and efficiency live in **Γ\_work**. Their *measurement integrity* can influence **R** for a claim (e.g., if a reliability figure depends on calibrated energy input), but **costs themselves are not assurance**; keep them in Γ\_work and cite their **measurement assurance** as inputs here.

---

### 6) Archetypal grounding (worked examples)

#### 6.1 System archetype — **Battery pack safety claim**

* **Claim `C`:** *Pack P meets discharge current L with thermal safety margin δ in environment K.*
* **Context `K`:** Ambient ≤ 35 °C; airflow ≥ X; duty cycle Y. Scope `S = run`.
* **Graph:** Cells `ComponentOf` modules `ComponentOf` pack; BIC exposes main power and thermal interface.
* **Inputs:**

  * `F` per node: module spec F2, cell test F1 → `F_eff = F1`.
  * `G`: operating envelope regions; union constrained by supported test regimes.
  * `R`: per‑module reliability from test data; cutset is **hot‑spot path** near weakest cell.
  * `CL`: interface congruence (sensor calibration CL2; thermal contact CL1).
* **Aggregation:**

  * `R_raw = min R_i` along the thermal cutset.
  * `R_eff = max(0, R_raw − Φ(CL_min=CL1))`.
  * `G_eff`: union of supported (L,T) rectangles, dropping regions lacking validated thermal data.
  * `F_eff = min(F_cell=F1, F_module=F2) = F1`.
* **SCR:** Evidence for calibration, test campaigns, BIC.
* **Improvement path:** raise `CL` (better thermal interface verification), raise `F` (formal thermal model), add supported envelope → **R\_eff** and **G\_eff** increase monotonically.

#### 6.2 Episteme archetype — **Meta‑analysis claim**

* **Claim `C`:** *Intervention X reduces outcome O by Δ on population P.*
* **Context `K`:** Inclusion/exclusion criteria, measurement protocol; `S = design`.
* **Graph:** Studies `MemberOf` evidence corpus; effect models `ConstituentOf` synthesis; mappings align different outcome scales.
* **Inputs:**

  * `F`: two RCTs at F3, one observational at F2 → `F_eff = F2`.
  * `R`: per‑study replication/quality → weakest R on the entailment spine caps `R_raw`.
  * `CL`: mapping of scales (CL1 vs CL3).
  * `G`: populations union, but unsupported sub‑populations are dropped.
* **Aggregation:**
+* **Aggregation:**  
* **\[M‑1]** ordinal support ranking; note weakest‑link study.  
* **\[M‑2]** compute `R_eff` with Φ table; record `CL_min` for scale mappings.  
* **\[F‑constructive]** formalise the effect‑model equivalence and export proof‑term hash.  # [M/F]

  * `R_eff = max(0, min(R_RCT1, R_RCT2, R_OBS) − Φ(CL_min=CL1))`.
  * `G_eff`: union of supported sub‑populations; out‑of‑scope groups excluded.
* **SCR:** Data provenance, scale mappings, bias assessment.
* **Improvement path:** upgrade mapping verification to CL2/CL3; increase `F` via registered analysis plan; replicate lagging study.

#### 6.3 Order/Process archetype — **Manufacturing route assurance**

* **Claim `C`:** *Route R meets output defect rate ≤ ε.*
* **Context `K`:** Materials, equipment class; `S = run`.
* **Γ\_ctx artifacts:** `σ` order; declared independent branches; join conditions at inspection.
* **Assurance:**

  * `R_raw = min R_step` along the **critical path** (includes inspection effectiveness).
  * Penalty from poor join soundness `CL_min`.
  * Improvement via faster but **verified** inspection (↑R\_step) or tighter join spec (↑CL).

#### 6.4 Temporal archetype — **Versioned model credibility**

* **Claim `C`:** *Model M predicts within ±δ over τ.*
* **Context `K`:** Data regime and drift tolerance; `S = run`.
* **Γ\_time artifacts:** `PhaseOf` slices v1, v2, v3 covering `τ`.
* **Assurance:**

  * `R_raw = min(R_v1, R_v2, R_v3)`;
  * penalty if v2–v3 interface had low calibration congruence;
  * improvement via re‑calibration (↑CL) or new validation campaign (↑R\_v3).

### 7) Conformance Checklist (normative)

| ID          | Requirement                                                                                                                                                                   | Purpose                                      |                                   |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- | --------------------------------- |
| **CC‑B3.1** | An assurance result **SHALL** be a typed claim \`Assurance(H, C                                                                                                               |  K, S)`with`S ∈ {design, run}\`.             | Prevent scope drift and chimeras. |
| **CC‑B3.2** | `F` **SHALL** be treated as **ordinal** (`min`/thresholds only); `G` as **coverage** (set/measure union constrained by support); `R` as **ratio** (`min` + conservative ops). | Preserve scale integrity (CHR).              |                                   |
| **CC‑B3.3** | The **Congruence Level** `CL` **SHALL** live on **edges**; the penalty `Φ(CL)` **SHALL** be **monotone decreasing** and **bounded** (`R_eff ≥ 0`).                            | Make integration quality first‑class.        |                                   |
| **CC‑B3.4** | `R_eff` **SHALL** be computed as `R_eff = max(0, min_i R_i − Φ(CL_min))` for the relevant integration path(s), unless a stricter domain‑specific rule is justified.           | Enforce WLNK and penalize weak integrations. |                                   |
| **CC‑B3.5** | `F_eff = min_i F_i`; `G_eff = SpanUnion({G_i})` **constrained by support**.                                                                                                   | Prevent over‑generalization.                 |                                   |
| **CC‑B3.6** | An **Assurance SCR** **SHALL** be produced, listing node/edge values, Evidence Graph Ref, and any OrderSpec/TimeWindow identifiers, **and SHALL also display**:  (i) the **describedEntity binding** `describe(Object→GroundingHolon)` for the claim and the declared **CHR:ReferencePlane ∈ {world|concept|episteme}** (cf. C.2.3); (ii) a **TA/VA/LA breakdown** of anchored evidence **kept separable** per **CC–KD‑08**, with **decay/valid‑until** indicators on empirical bindings (A.10), and the **Epistemic‑Debt** tally as computed in **§ B.3.4**. | Provide auditability (A.10).                 |                      
| **CC‑B3.7** | **Agency‑CHR** values (A.13) **SHALL NOT** override WLNK or `Φ(CL)` penalties; if agency grade change alters capabilities, model it as a **Meta‑Holon Transition**.           | Preserve safety; keep agency separate.       |                                   |
| **CC‑B3.8** | Design‑time and run‑time assurance **SHALL NOT** be mixed in one tuple; compare them side‑by‑side if needed.                                                                  | Avoid design/run mixing.                     |                                   |

### 8) Anti‑patterns and repairs

| Anti‑pattern             | Symptom                                                    | Repair                                                                                                         |
| ------------------------ | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Averaging assurance**  | Mean of `R_i` reported as system reliability               | Use `min R_i` on the cutset, then apply `Φ(CL_min)`.                                                           |
| **Ordinal arithmetic**   | Averaging `F` or `CL` to produce “2.3”                     | Use `min`/`max` or thresholds; never average ordinals.                                                         |
| **Coverage as centroid** | Replacing `G` union with a single “typical point”          | Keep `G` as set/coverage; if a numeric proxy is needed, derive it from the set.                                |
| **Ignoring congruence**  | No penalty for weak mappings/interfaces                    | Assign `CL` to integration edges; apply `Φ(CL_min)`.                                                           |
| **Design/run chimera**   | “One score” mixing blueprint and telemetry                 | Split into `S=design` and `S=run` tuples; compare explicitly.                                                  |
| **Agency override**      | Claiming higher assurance because a controller is “clever” | Agency may justify *how* improvements are achieved; it cannot remove WLNK or `Φ`.                              |
| **MemberOf as stock**    | Using `MemberOf` to sum reliabilities                      | Keep `MemberOf` for collections; reliability comes from the relevant **Γ** composition (e.g., Γ\_sys cutset). |

---

### 9) Consequences

**Benefits**

* **Comparable, conservative, improvable.** The tuple ⟨F, G, R⟩ with **edge‑level CL** gives a compact, auditable view that improves monotonically under targeted actions (formalize, replicate, reconcile).
* **Cross‑scale coherence.** Works for assemblies and arguments, procedures and histories, without leaking order/time/cost into structure.
* **Clear upgrade paths.** It is obvious **what to do** to raise each component (raise F/G/R locally or raise CL on the glue).

**Trade‑offs**

* **More explicit metadata.** You must state scale kinds, cutsets, and mapping congruence; this is intentional transparency.
* **Conservatism may feel pessimistic.** True synergy appears only via **MHT** or after raising CL—never by arithmetic optimism.

---

### 10) Rationale (informative)

B.3 distills mature post‑2015 practice across several fields into a single, small calculus:

* **Assurance by weakest link** reflects reliability engineering and safety cases in complex systems; composing claim strength by minima prevents over‑statement.
* **Formality and verifiability** mirror advances in model‑based engineering and formal verification, where raising F turns subjective arguments into verifiable artifacts.
* **Coverage as set/measure** follows evidence synthesis and validation practice that treat applicability as a domain region, not a scalar to “average.”
* **Congruence on edges** captures what meta‑analysis, interface control, and ontology alignment have repeatedly shown: integration quality is often the real bottleneck. Penalizing low‑CL is a principled way to prevent silent over‑confidence while rewarding verified reconciliation.

This arrangement preserves **A.11 Parsimony** (few characteristics), aligns with **A.14/A.15** (clear separation of structure, order, time, cost, values), and leaves Context for domain‑specific refinements that do not break the invariants.

---

### 11) Relations

* **Builds on:** B.1 (Universal Γ), B.1.1 (Proof Kit), B.1.2 (Γ_sys & BIC), B.1.3 (Γ_epist & SCR), B.1.4 (Γ_ctx/Γ_time), A.12 (Transformer), A.14 (Mereology), A.15 (Strict Distinction), **C.13 (Compose‑CAL)**.
* * **Coordinates with:** **E.14 (Human‑Centric Working‑Model)** for publication‑surface discipline and **B.3.5 (CT2R‑LOG)** for Working‑Model relation aliasing and grounding (`tv:*`, `validationMode`).
* **Used by:** KD‑CAL action patterns (to plan improvements), B.4 (Evolution loops that raise F/G/R or CL over time).
* **Triggers:** B.2 (Meta‑Holon Transition (MHT): Recognizing Emergence and Re‑identifying Wholes) when genuine new capabilities emerge that change the applicable cutsets or envelopes.

> **One‑page takeaway.**
> Report assurance as **⟨F, G, R⟩** for a **typed claim** under explicit **context/scope**, and penalize by the **lowest edge‑level congruence**.
> Improve assurance by raising **F**, **G**, **R**, or **CL**—and keep order, time, and cost in their own lanes.

### **Pattern B.3.3 — Assurance Subtypes & Levels [D]**

**Context**

A complex project may generate hundreds of artifacts: design specifications, simulation models, test suites, and operational logs. While the Trust & Assurance Calculus provides a framework for evaluating these artifacts, teams often face a critical challenge: how to aggregate this diverse evidence into a single, meaningful signal of an artifact's maturity. Simply counting the number of tests or documents can lead to "paper compliance," where an artifact appears well-supported but has critical, unexamined weaknesses in its formal structure or conceptual alignment.

**Problem**

How do we create an objective, auditable, and balanced Standard for what constitutes "trustworthiness" at each stage of an artifact's development cycle? FPF requires a mechanism that moves beyond simple evidence counting to a qualitative assessment of assurance. This mechanism must prevent common failure modes, such as over-investing in run-time validation (LA) at the expense of design-time verification (VA), or neglecting the critical work of ensuring concepts are correctly mapped and typed (TA).

**Solution**

FPF establishes a formal Standard that links three distinct **Assurance Subtypes** to three computable **Assurance Levels**. An artifact's level is not assigned manually by an author; it is **derived automatically** by its anchored evidence. This creates a transparent and falsifiable system for tracking an artifact's journey from a speculative idea to a robust, reliable holon.

**1. Assurance Subtypes: The Three Pillars of Trust**

These three subtypes categorize the kind of question an assurance activity answers, ensuring a balanced approach to building confidence.

| Subtype | Code | Core Question | Links to Epistemic Score | Manager's View: What It Prevents |
| :--- | :--- | :--- | :--- | :--- |
| **Typing Assurance** | TA | “Does the artifact faithfully represent its intended concept?” | **CL** (Congruence Level) | **Miscommunication & Integration Failures.** TA ensures that when a requirement says "Sensor," the design model's "Sensor" component is the same conceptual thing. This activity directly improves the Congruence Level (CL) of the integration *edges* between artifacts. |
| **Verification Assurance**| VA | “Is the holon logically correct under its stated assumptions?” | **FV** (Formal Verifiability)| **"It Works on Paper" Errors.** VA catches design flaws, logical inconsistencies, and specification errors before a single line of code is written or a physical part is machined. It ensures the blueprint is sound. |
| **Validation Assurance**| LA | “Does the holon work correctly in the real world?” | **EV** (Empirical Validability)| **"Works in the Lab, Fails in the Field" Surprises.** LA confirms that the holon performs as expected under real or simulated operational conditions, accounting for noise, unexpected inputs, and environmental factors. |

**2. Computed Assurance Levels: The Ladder of Maturity**

An artifact’s level is computed based on the evidence it has accumulated. This creates a clear, step-by-step path for increasing trust.

| Level | Name | How It Is Computed |
| :--- | :--- | :--- |
| **Level 0** | **Unsubstantiated** | No `verifiedBy` or `validatedBy` evidence is present. The artifact is a claim or an idea. |
| **Level 1** | **Substantiated** | At least one `verifiedBy` or `validatedBy` link to an evidence artifact exists, and the artifact is supported by Typing Assurance (TA). |
| **Level 2** | **Axiomatic** | The artifact is `verifiedBy` either a proof **or** a **Compose‑CAL (Γₘ) constructive narrative** that the author has linked from the Working‑Model via `tv:groundedBy` (CT2R‑LOG). Its FormalVerifiabilityScore (FV) meets or exceeds a pre‑defined threshold. Additionally, if the holon is designated as safety‑critical, it **MUST** also be supported by **Validation Assurance (LA)**. For non‑critical holons, LA is strongly recommended (`SHOULD`). |

> **Didactic Note for Managers: What 'Level 1' Really Means**
>
> Think of moving from Level 0 to Level 1 as the first step toward professional seriousness.
>
> *   **Level 0** is an idea on a whiteboard. It has potential, but no receipts.
> *   **Level 1** means you have **at least one receipt**. You have anchored the idea to something concrete: a passing test, a formal sketch, a simulation result. It's no longer just an opinion.
>
> Crucially, Level 1 also demands **Typing Assurance (TA)**. This sounds technical, but its business impact is simple: **it means you've named your terms correctly and consistently**. You've used the Role-Projection Bridge (Pattern B.5) to ensure that the "Sensor" in your requirements document is the same "Sensor" in your architectural diagram. This basic alignment work is what prevents costly integration failures and endless meetings where teams talk past each other. Good typing is the foundation of clear communication, and at Level 1, FPF makes it mandatory.

**Conformance Checklist**

To ensure the integrity of the assurance calculus, the following rules are normative. A **Target of Assurance (ToA)** is any working-model element designated as a root claim (e.g., a top-level system requirement, safety goal, or core hypothesis).

*   **CC-B3.3.1 (L1 Anchor Mandate):** A ToA **SHALL NOT** be considered to have reached `AssuranceLevel:L1` unless it is linked to at least one evidence artifact via `verifiedBy` or `validatedBy`.
*   **CC-B3.3.2 (L1 Typing Mandate):** A ToA at `AssuranceLevel:L1` or higher **MUST** be supported by **Typing Assurance (TA)**. This includes, at a minimum, that its core concepts are mapped via the Role-Projection bridge (Pattern B.5) and it conforms to its declared schema.
*   **CC-B3.3.3 (L2 V&V Mandate):** A ToA at `AssuranceLevel:L2` **MUST** satisfy all L1 criteria. In addition, it **MUST** be supported by **Verification Assurance (VA)** with `FV ≥ threshold_FV`. For holons designated as safety-critical (e.g., `criticality ≥ SIL-2`), the ToA **MUST** also be supported by **Validation Assurance (LA)** with `EV > 0`. For non-critical holons, LA **SHOULD** be present.
    *   *Exemption Note:* Purely formal artifacts (e.g., mathematical axioms) may justify an exemption from the LA requirement, provided this is documented in their rationale.
*   **CC-B3.3.4 (Concept-Bridge Completeness):** For any architheory used in a model at `AssuranceLevel:L1` or higher, all of its mandatory U.Types **MUST** be mapped to domain concepts via the Role-Projection bridge (Pattern B.5).
*   **CC-B3.3.5 (Scope Separation):** Assurance claims **MUST** maintain a strict separation between `design-time` and `run-time` scopes (Pattern A.4). An assurance tuple for a `MethodDescription` (design-time) SHALL NOT be conflated with one for its corresponding `Work`/`Trace` (run-time). The Evidence Graph Ref (`verifiedBy`, `validatedBy`) must point to artifacts of the appropriate scope.
* **CC-B3.3.6 (CT2R‑LOG Handshake):** If a ToA depends on **structural** claims, those claims **SHALL** be published as **Working‑Model** relations and, when used to justify `L2`, **SHALL** declare `validationMode=axiomatic` and provide **Constructive** grounding with `tv:groundedBy → Γₘ.(sum|set|slice)` (see B.3.5 and C.13).  
* **CC-B3.3.7 (Downward‑Only Dependence):** Assurance artefacts (Mapping/Logical/Constructive/Evidence) **SHALL NOT** impose vocabulary or layout back onto the Working‑Model surface (E.14).
 
**Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | Manager's View: What It Looks Like | How FPF Prevents It |
| :--- | :--- | :--- |
| **The "Tested but Untyped" Mess** | "Our code has 100% test coverage, but we still have integration bugs and nobody understands what the architheories do." | **CC-B3.3.2** makes Typing Assurance (TA) mandatory for L1. You cannot claim your work is "Substantiated" without first ensuring your terms and concepts are clear and consistently mapped. |
| **The "Perfect Blueprint, Flawed Reality"** | "The design was formally proven to be perfect, but the physical product failed catastrophically in the field." | **CC-B3.3.3** mandates Validation Assurance (LA) for safety-critical systems at L2. A perfect blueprint (`FV=4`) is not enough; you must also provide empirical evidence (`EV>0`) that it works in the real world. |
| **The "Paper Compliance" Shell Game** | "We have thousands of documents and links, so we must be at a high assurance level." | The computed `AssuranceLevel` is not based on the *quantity* of evidence but on its *type* and *quality* (via FV/EV scores). You cannot reach L2 without strong formal verification (VA), no matter how much validation (LA) you do. |

**Consequences**

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Objective Gatekeeping:** The rules provide a clear, objective, and falsifiable basis for an artifact's assurance status, eliminating subjective judgment and "assurance theater." | **Risk of Over-stringency:** The rules might feel too strict for rapid prototypes. *Mitigation:* The requirements for `L1` are deliberately lightweight, demanding only one piece of evidence and basic typing, making the first step onto the ladder accessible. |
| **Balanced Assurance:** The Standard requires a mix of evidence types for higher levels, preventing teams from over-investing in one area (e.g., testing) while neglecting another (e.g., formal specification). | **Risk of Evidence Inflation:** Teams might add trivial evidence just to meet the criteria. *Mitigation:* The quality of evidence is assessed via the epistemic scores (FV, EV, CL); merely linking to low-quality evidence will not significantly raise the scores needed for L2. |
| **Clear Progress Tracking:** The ladder provides a clear roadmap for maturing an artifact from an idea to a fully assured component, making planning and progress monitoring transparent. | **Overhead for Complex Holons:** A holon with many ToAs may require significant assurance work. *Mitigation:* The framework allows grouping, where a parent claim's evidence can satisfy the coverage requirements for its children if explicitly declared. |

**Rationale**

This pattern transforms the assurance framework from a descriptive taxonomy into a prescriptive, actionable Standard. By binding the computed `AssuranceLevel` to mandatory, well-defined evidence coverage, it makes the notion of "trustworthiness" in FPF an objective and auditable property. The rules ensure that as an artifact's formality and claimed reliability increase, the rigor and balance of its supporting evidence increase in lockstep, operationalizing the principle of "no blind trust." The separation of `design-time` and `run-time` evidence, mandated by CC-B3.3.5, further ensures that claims made about a blueprint are not confused with claims made about a running system, preserving the integrity of the entire lifecycle.

**Relations**

*   **Builds on:** `B.3.1 Characteristic & Epistemic Spaces`, `A.10 Evidence Graph Referring`, `A.4 Temporal Duality`.
*   **Constrains:** The computation and interpretation of `AssuranceLevel` for all holons.
*   **Enables:** Objective quality gates in the Canonical Evolution Loop (B.4) and reliable inputs for the Trust-Aware Mediation Calculus (D.4).

### B.3.4 — Evidence Decay & Epistemic Debt \[A] 

**Context**

The FPF assurance model (Pattern B.3.3) provides a robust framework for building trust in holons by anchoring claims to a rich body of evidence. However, it implicitly treats this evidence as timeless. A proof verified today is assumed to hold forever; a validation test run last year is given the same weight as one run yesterday. This assumption is dangerously flawed in any dynamic environment.

Consider a bridge certified in 1980. The assurance case, resting on evidence about steel fatigue from that era, would be considered highly reliable *at that time*. Today, after decades of environmental change, new material science insights, and an entirely different traffic load, would we still trust that original certification without re-evaluation? The context has drifted, and the original evidence has lost its relevance. FPF requires a formal mechanism to account for this natural decay of trust.

**Problem**

Without a calculus for evidence aging, FPF models are vulnerable to three critical failure modes:

1.  **Silent Risk Accumulation:** Trust silently decays. A component's high `AssuranceLevel` can become an illusion, resting on foundational evidence that is no longer valid in the current operational context. When aggregated, this stale trust propagates upwards, creating a seemingly robust system-of-systems that is, in fact, incredibly brittle.
2.  **Audit Illusion:** An artifact can pass an audit with flying colors, showing a complete set of anchors to high-quality evidence, yet be fundamentally untrustworthy because that evidence is obsolete. This leads to a false sense of security and undermines the very purpose of the assurance case.
3.  **Maintenance Paralysis:** Without a systematic way to flag stale evidence, re-validation efforts are often misdirected. Teams either engage in costly, unfocused re-testing of everything, or, more commonly, do nothing, allowing epistemic debt to accumulate until a failure forces a crisis.

**Forces**

| Force | Tension |
| :--- | :--- |
| **Timeless Truth vs. Contextual Reality** | Formal proofs and logical derivations feel permanent and universal, yet the assumptions they make about the world are context-dependent and perishable. |
| **Rigor vs. Agility** | Continuously re-validating every piece of evidence is prohibitively expensive and would paralyze any agile workflow. |
| **Transparency vs. Cognitive Load** | We need to make the "staleness" of evidence visible, but we must do so without overwhelming teams with a constant barrage of decay alerts. |
| **Governance vs. Flexibility** | There must be a formal method for managing aging evidence, yet teams need the autonomy to make risk-informed decisions about when to accept, refresh, or deprecate it. |

**Solution**

FPF introduces a formal freshness model and a governance loop that make evidence aging a first-class, manageable property of the assurance calculus.

**1. The Principle of Perishable Evidence**

The core of the solution is a new normative principle: **Evidence is perishable**. The relevance of any piece of evidence is a function of time and context. An `AssuranceLevel` is therefore not a permanent achievement but a state that must be actively maintained.

**2. Mechanism 1: The Freshness Standard (`valid_until`)**

Every evidence artifact anchored in the Assurance Layer **MUST** carry a `valid_until` attribute.

*   **`valid_until: ISO-8601-date | null`**
*   This attribute acts as a "best before" date, explicitly stating the time horizon over which its creators consider it to be fully relevant without review.
*   A value of `null` signifies that the evidence is considered **perpetual**. This is reserved for artifacts like mathematical axioms or fundamental physical laws whose validity is not expected to decay on engineering timescales.

**3. Mechanism 2: The Epistemic Debt Metric (ED)**

When the current time `t` surpasses an evidence artifact's `valid_until` date, that artifact begins to accrue **Epistemic Debt (ED)**.

*   **Definition:** Epistemic Debt is a quantitative measure of an artifact's "staleness." It is a function of its age past its expiry date.
*   **Purpose:** ED is not a penalty but a **signal**. It makes the invisible risk of relying on old evidence visible and measurable.

**4. Mechanism 3: The Governance Loop (`Refresh / Deprecate / Waive`)**

Epistemic Debt is managed through a project-level **epistemic_debt_budget**. When the total accrued debt exceeds this budget, an alert is triggered, and the team **MUST** take one of three actions:

| Action | What It Means | Manager's View: The Practical Consequence |
| :--- | :--- | :--- |
| **Refresh** | Produce new, up-to-date evidence and set a new `valid_until` date. | **"We invest the resources to re-validate."** This is the engineering fix: run the tests again, update the model, re-certify the component. |
| **Deprecate**| Acknowledge that the evidence is no longer valid and formally downgrade the `AssuranceLevel` of the dependent artifact (typically to `L0` or `L1`). | **"We accept the risk by lowering the component's official status."** The component is no longer considered fully assured and may be flagged for restricted use until it is refreshed. |
| **Waive** | A designated authority (e.g., a senior systems engineer or a safety officer) formally accepts the risk of using the stale evidence for a limited time. | **"I am signing off on this risk, for now."** This is a temporary, auditable override. It keeps the project moving but makes the risk acceptance explicit and assigns responsibility. |

> **Didactic Note for Managers: Managing Your "Trust Budget"**
>
> Think of Epistemic Debt exactly like financial or technical debt. It’s not inherently evil, but it must be managed. The FPF dashboard now includes a "Trust Health" meter.
>
> *   **Green:** Your evidence is fresh. Your assurance case is solid.
> *   **Amber:** Epistemic Debt is accumulating. It's time to plan for re-validation work in the next sprint.
> *   **Red:** Your debt has exceeded its budget. Your CI/CD pipeline might be issuing warnings, and you are now carrying un-budgeted risk. You must immediately decide: **Pay it down (Refresh), write it off (Deprecate), or take out a short-term, high-visibility loan (Waive).**
>
> This loop transforms the vague problem of "keeping things up to date" into a concrete, resource-managed, and auditable engineering process.

**5. Mechanism 4: The Epistemic Debt (ED) Calculation & Aggregation**

To make ED a useful leading indicator, it must be computed and aggregated consistently.

*   **Calculation:** For a single evidence artifact `i`, its debt at time `t` is a function of its age past expiry:
    `ED_t(i) = k * max(0, t - valid_until_i)`
    *   The coefficient `k` is a configurable linear decay factor (default: `1.0 per day`), allowing projects to tune the "interest rate" on their debt.

*   **Aggregation:** The total ED for an artifact `A` is the sum of the debt from all its direct and transitive Evidence Graph Ref:
    `ED_t(A) = Σ_i ED_t(evidence_i)`
    *   This rule ensures that debt propagates up the holarchy. If a foundational component's validation expires, the entire system that depends on it inherits that debt.

*   **Impact on Assurance Level:** When an artifact's total `ED_t(A)` exceeds a defined threshold (typically `> 0` unless waived), its computed `AssuranceLevel` is **provisionally downgraded by one level**. For example, an `L2` artifact with expired evidence is treated as `L1` for governance and risk purposes until the debt is resolved. This makes the consequence of inaction immediate and visible on project dashboards.

**Conformance Checklist**

*   **CC-ED.1 (Freshness Mandate):** Every evidence artifact anchored via `verifiedBy` or `validatedBy` **MUST** include a `valid_until` attribute. A value of `null` (perpetual) **MUST** be justified in the artifact's rationale.
*   **CC-ED.2 (Debt Budget Mandate):** Every project or `U.System` at `AssuranceLevel:L1` or higher **MUST** declare an `epistemic_debt_budget` in its manifest.
*   **CC-ED.3 (Aggregation Mandate):** The total Epistemic Debt of a composite holon **MUST** be the sum of the debt of its constituent parts, consistent with the aggregation rule `ED_t(S) = Σ_j ED_t(child_j)`.
*   **CC-ED.4 (Downgrade Mandate):** An artifact with `ED_t > epistemic_debt_budget` **SHALL** have its effective `AssuranceLevel` provisionally downgraded until the debt is resolved via `Refresh`, `Deprecate`, or `Waive`.
*   **CC-ED.5 (Waiver Auditability):** Any `Waive` action **MUST** be recorded as a formal, auditable event, citing the responsible authority, the rationale, and a new, short-term expiry date for the waiver itself.

**Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | Manager's View: What It Looks Like | How FPF Prevents It |
| :--- | :--- | :--- |
| **The "Perpetual Evidence" Fallacy** | "We verified this component five years ago, so it's still L2. It's just a simple library, nothing has changed." | **CC-ED.1** forces a `valid_until` date. The context (compiler versions, new vulnerabilities, OS updates) has certainly changed. Setting `valid_until: null` requires explicit justification that the artifact is truly timeless, like a mathematical theorem. |
| **The "Invisible Debt" Trap** | A critical, low-level component's test suite has been failing silently for months, but the high-level system dashboard is still green. | **CC-ED.3** ensures that the debt from the failing component's expired evidence propagates up to the system level, turning the dashboard amber or red and forcing attention. |
| **The "Risk Acceptance by Silence"** | "We know those tests are stale, but we're too busy to fix them. Let's just ignore the warnings for now." | **CC-ED.5** makes risk acceptance an explicit, auditable action. A manager must formally `Waive` the debt, putting their name on the decision. This transforms passive neglect into active, accountable risk management. |

**Consequences**

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Lifecycle Honesty:** The framework provides a transparent, quantitative way to track the erosion of trust over time, preventing "assurance rot." | **Process Overhead:** Teams must now manage `valid_until` dates and respond to debt alerts. *Mitigation:* Tooling can automate much of this, suggesting default expiry dates based on artifact type and providing one-click actions for the governance loop. |
| **Risk-Informed Maintenance:** Epistemic Debt becomes a leading indicator for maintenance and re-validation planning, allowing teams to allocate resources proactively, not reactively. | **Risk of False Positives:** Overly aggressive decay coefficients (`k`) could create excessive noise. *Mitigation:* The `k` value is configurable, and the `Waive` mechanism provides a safety valve for situations where a formal refresh is not yet warranted. |
| **Enhanced Auditability:** The entire state progression of evidence—from creation to expiry and resolution—is now a traceable, auditable part of the FPF model. | - |

**Rationale**

Knowledge frameworks that ignore time degrade silently. By embedding entropy accounting (epistemic debt) directly into the assurance calculus, FPF gains a self-regulating "immune system." This pattern operationalizes the common-sense insight that evidence is perishable, transforming maintenance from an ad-hoc, often-neglected chore into a budgeted, auditable, and risk-informed engineering activity. It complements the human-centric loop of ADR-014 and the pragmatic utility guardrail of ADR-015 by ensuring that what we trust today remains trustworthy tomorrow.

**Relations**

*   **Builds on:** `B.3.3 Assurance Subtypes & Levels`, `A.10 Evidence Graph Referring`.
*   **Constrains:** The temporal validity of `AssuranceLevel` for all holons.
*   **Enables:** Proactive maintenance planning within the Canonical Evolution Loop (B.4) and provides a dynamic risk input for ethical and strategic decision-making (Part D).
