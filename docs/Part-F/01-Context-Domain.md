# **Part F — The Unification Suite (U‑Suite): Concept‑Sets, SenseCells & Contextual Role Assignment**


---

# Cluster F.I — context of meaning & Raw Material


---

# **F.0.1 — Contextual Lexicon Principles** \[A]

> **One‑sentence summary.** All meanings in FPF are **local to a `U.BoundedContext`** (“Context of meaning”); terms are **spoken with their Context**, and any relation **across Contexts** exists **only** as an explicit **Alignment Bridge** with stated loss/fit.

**Status.** Architectural pattern \[A], architheory‑agnostic.
**Builds on:** A.1.1 `U.BoundedContext` (formal frame); A.7 *Strict Distinction* (C‑6); A.8 *Universal Core* (C‑1); A.11 *Ontological Parsimony* (C‑5); A.4 *Temporal Duality* (C‑7); **E.10.D1 D.CTX** (lexical discipline for “Context”).
**Coordinates with.** **F.1** (Context Map via Context Cards), **F.2** (local term capture), **F.3** (intra‑Context clustering), **F.7** (Concept‑Set Table), **F.9** (Alignment & Bridge), **B.3** (Trust & Assurance; CL penalties).

> **Didactic note.** In the Tech register, **Context ≡ `U.BoundedContext`** (per E.10.D1). We use “Context of meaning” as a **metaphor only**; *Context* remains the normative short form for `U.BoundedContext`. The word **anchor** is not used in FPF.

> **Didactic note.** In the Tech register, **Context ≡ `U.BoundedContext`** (per E.10.D1). We use “Context of meaning” as a **metaphor only**; *Context* remains the normative short form for `U.BoundedContext`. The word **anchor** is not used in FPF. The word *plane* is reserved to **CHR:ReferencePlane** only.

**Terminology guard (normative, Part F).** The **row classifier** is **senseFamily**: {Role | Status | Measurement | Type‑structure | Method | Execution}. **Characteristic** (MM‑CHR) names measurable aspects only (A.17–A.19) and MUST NOT be used for row typing in Part F. Avoid the generic word **facet** in Part F; when unavoidable, reference **C.3.5 KindAT (informative facet)** or **Compose‑CAL `U.Facet`** explicitly. Only **CHR:ReferencePlane** is permitted (no bare “plane”); use **I/D/S layer** for intension/description/specification; use **stance** for design vs run.


---

# F.1 — Domain‑Family Landscape Survey \[A]

**“Fix the context of meaning before you name anything.”**
**Status.** Architectural pattern \[A], architheory‑agnostic.
**Depends on.** E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; **F.0.1 Contextual Lexicon Principles**; A.7 **Strict Distinction (Clarity Lattice)**; A.11 **Ontological Parsimony**.
**Coordinates with.** F.2 **Term Harvesting & Normalisation**; F.3 **Intra‑Context Sense Clustering**; F.4 **Role Description**; F.9 **Alignment & Bridge Across Contexts**; **G.0–G.1** *(Scope/describedEntity handoff)*.  *(Bridges live only in F.9.)*

**Aliases (informative).** *Contexts‑first survey*; *Context cut*.


---

## 6 · Solution — the Contexts‑first survey (conceptual, notation‑free)

**Step 1 — Declare your unification line(s).**
State which architheory threads are in play (e.g., *Enactment + KD‑CAL sensing + Sys‑CAL execution*). This keeps the cut purposeful.

**Step 2 — Cut the landscape by domain families.**
For each line, **select at least three distinct domain families** (heterogeneity guard). Examples:

* *Workflow & provenance* (BPMN 2.0; W3C PROV‑O)
* *Services & deontics* (ITIL 4; ODRL 2.2)
* *Sensing & measurement* (SOSA/SSN; ISO 80000‑1)
* *Types & taxonomies* (OWL 2; FCA corpus)
* *Control & actuation* (state‑space control texts; IEC 61131‑3)

**Step 3 — For each family, sketch 1–3 Context Cards.**
Prefer canonical, widely cited canons. If a field is fragmented, choose one **exemplar** and one **counter‑voice** to surface heterogeneity.

**Step 4 — Make **locality** explicit.**
Treat words as **context‑local**. *Process (BPMN)* ≠ *process (thermodynamics)* ≠ *process (PROV)*. Do not reconcile. Do not average. **Just fix the Contexts.**

**Step 5 — Bound the set.**
Small enough to hold in working memory. As a rule of thumb:

* per unification line: **≥ 3 families**;
* per family: **1–3 Contexts**.
  More only if a missing Context hides a known sense‑split you will certainly need.

**Step 6 — Postpone bridges.**
If two Contexts seem “close”, **resist** collapsing. Note the tension and defer to **F.9 Alignment & Bridge**.


---

# F.2 — Term Harvesting & Normalisation \[A] 

**“Harvest words *inside Contexts*, name them in the Context’s own idiom, and stop there.”**
**Status.** Architectural pattern \[A], architheory‑agnostic.
**Depends on.** E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; **F.0.1 Contextual Lexicon Principles** (Source · Local Meaning · Bridge‑Only Crossing); A.7 **Strict Distinction**; A.11 **Ontological Parsimony**.
**Coordinates with.** F.1 **Context Map via Context Cards**; F.3 **Intra‑Context Sense Clustering**; F.4 **Role Description**; F.9 **Alignment & Bridge Across Contexts**.
**Aliases (informative).** *context‑local harvesting*; *Local normalisation*.

---


---

## 8 · Micro‑examples (illustrative, context‑local)

> Each line is *one* local lexical unit. No relations are implied across lines.

* **Context:** *BPMN 2.0 (2011)* — **LNF:** `process`
  **Tech:** `process` · **Plain:** `workflow process`
  **Gloss:** “Directed graph of flow nodes and sequence flows enacted by participants.”

* **Context:** *PROV‑O (2013)* — **LNF:** `activity`
  **Tech:** `activity` · **Plain:** `temporal occurrence`
  **Gloss:** “Time‑bounded occurrence that uses and generates entities and is linked to agents.”

* **Context:** *ITIL 4 (2020)* — **LNF:** `service‑level‑objective`
  **Tech:** `service‑level‑objective` · **Plain:** `service target`
  **Gloss:** “Target value for a service characteristic within a service promise vocabulary.”

* **Context:** *NIST RBAC (2004)* — **LNF:** `role`
  **Tech:** `access‑role` · **Plain:** `permission role`
  **Gloss:** “Named grouping of permissions assignable via sessions.”

* **Context:** *SOSA/SSN (2017)* — **LNF:** `observation`
  **Tech:** `observation` · **Plain:** `measurement act`
  **Gloss:** “Act applying a procedure to a feature of interest to produce a result.”

* **Context:** *IEC 61131‑3* — **LNF:** `task`
  **Tech:** `task` · **Plain:** `runtime program execution`
  **Gloss:** “Cyclic or event‑driven execution unit for control programs.”

---


---

## 11 · Worked examples (multi‑architheory, context‑local only)

> Each line is a **local lexical unit** *(Context, LNF, Tech, Plain, Gloss)*.
> No Cross‑context relation is implied. Later clustering (F.3) and bridges (F.9) may connect them.

### 11.1 Enactment + sensing

* **Context:** *BPMN 2.0 (2011)* — **LNF:** `process`
  **Tech:** `process` · **Plain:** `workflow process`
  **Gloss:** “Directed graph of flow nodes and sequence flows enacted by participants.”

* **Context:** *PROV‑O (2013)* — **LNF:** `activity`
  **Tech:** `activity` · **Plain:** `temporal occurrence`
  **Gloss:** “Time‑bounded occurrence that uses and generates entities and links to agents.”

* **Context:** *SOSA/SSN (2017)* — **LNF:** `observation`
  **Tech:** `observation` · **Plain:** `measurement act`
  **Gloss:** “Act applying a procedure to a feature of interest to produce a result.”

* **Context:** *ITIL 4 (2020)* — **LNF:** `service‑level‑objective`
  **Tech:** `service‑level‑objective` · **Plain:** `service target`
  **Gloss:** “Target value for a service characteristic within a service promise vocabulary.”

*Thinking pay‑off:* you can phrase “compare **observation** to **service‑level‑objective**” without importing workflow or provenance semantics.

---

### 11.2 Sys‑CAL / LCA‑CAL + services

* **Context:** *State‑space control texts* — **LNF:** `actuation`
  **Tech:** `actuation` · **Plain:** `control output`
  **Gloss:** “Signal applied to the plant to influence state/output.”

* **Context:** *IEC 61131‑3* — **LNF:** `task`
  **Tech:** `task` · **Plain:** `runtime program execution`
  **Gloss:** “Cyclic or event‑driven execution unit for control programs.”

* **Context:** *ITIL 4 (2020)* — **LNF:** `incident`
  **Tech:** `incident` · **Plain:** `reported disruption`
  **Gloss:** “Unplanned interruption or reduction in the quality of a service.”

*Thinking pay‑off:* avoids calling a plant fault an “incident” unless you **cross Contexts later** with an explicit bridge.

---

### 11.3 Kind-CAL + Method‑CAL + KD‑CAL

* **Context:** *OWL 2 (profiles)* — **LNF:** `subclass‑of`
  **Tech:** `subclass‑of` · **Plain:** `is‑a (type hierarchy)`
  **Gloss:** “C ⊑ D: every instance of C is an instance of D.”

* **Context:** *FCA corpus* — **LNF:** `formal‑concept`
  **Tech:** `formal‑concept` · **Plain:** `extent–intent node`
  **Gloss:** “Maximal (objects, attributes) pair under a Galois connection.”

* **Context:** *SPEM 2.0 / ISO 24744* — **LNF:** `method`
  **Tech:** `method` · **Plain:** `abstract way of doing`
  **Gloss:** “Abstract how‑to independent of specification or execution.”

* **Context:** *SOSA/SSN (2017)* — **LNF:** `procedure`
  **Tech:** `procedure` · **Plain:** `measurement recipe`
  **Gloss:** “Specification guiding how an observation is produced.”

*Thinking pay‑off:* discourages treating an FCA “concept” as a `U.Type`, or a **procedure** as a **method** without later proof.

---


---

# F.3 — Intra‑Context Sense Clustering \[A] 

**“Within one context, decide what ‘the same sense’ really is—before you ever cross Contexts.”**
**Status.** Architectural pattern \[A], architheory‑agnostic.
**Depends on.** F.1 **Domain‑Family Landscape Survey**; F.2 **Term Harvesting & Normalisation**; E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; A.7 **Strict Distinction**; A.11 **Ontological Parsimony**.
**Coordinates with.** F.4 **Role Description**; F.7 **Concept‑Set Table**; F.8 **Mint or Reuse Decision**; F.9 **Alignment & Bridge Across Contexts**.
**Aliases (informative).** *context‑local clustering*; *Sense consolidation*.

---


---

## 11 · Local‑Sense Cards (one‑glance form)

> A **Local‑Sense Card** is a **one‑glance** sketch per sense in a Context. It teaches faster than prose lists and keeps senses crisp.

**Fields (thought‑items, not fields to fill):**

* **Context** (U.BoundedContext, edition)
* **Label pair** — **Tech** (idiomatic) · **Plain** (didactic)
* **Sense line** — one sentence in the Context’s voice
* **Inside** — which F.2 Units it consolidates (names only)
* **Counter‑example** — a short use that must **not** be included

---


---

## 12 · Worked examples (multi‑architheory, all **intra‑Context**)

### 12.1 BPMN 2.0 (workflow Context)

**Card A — “process (graph)”**

* **Label**: Tech **process** · Plain **workflow graph**
* **Sense line**: A BPMN **graph of flow nodes and sequence flows** **specifying orchestration among participants** *(design‑time)*.
* **Inside**: *process*, *process model*, *business process* (when used as diagram).
* **Counter‑example**: *“This process took 5 minutes”* ← **runtime** occurrence, **not** this sense.

**Card B — “event (node‑type)”**

* **Label**: Tech **event (node)** · Plain **event symbol**
* **Sense line**: A **node‑type** that marks starts, ends, and intermediates; typed by trigger/result.
* **Inside**: *start event*, *message event*, *end event*.
* **Counter‑example**: *“The outage event happened at 13:05”* ← narrative occurrence, **not** the node‑type.

> **Outcome:** “Process uptime” is rejected as a BPMN sense; Execution belongs to another Context.

---

### 12.2 PROV‑O (provenance Context)

**Card C — “activity (run)”**

* **Label**: Tech **activity** · Plain **time‑bounded execution**
* **Sense line**: An **occurrence** that **uses** and **generates** entities; linked to agents; has start/end.
* **Inside**: *activity*, *execution* (when PROV authors use it).
* **Counter‑example**: *“Sorting algorithm”* ← capability/method, **not** an occurrence.

**Card D — “agent (provenance)”**

* **Label**: Tech **agent** · Plain **provenance actor**
* **Sense line**: Thing that bears **responsibility** for an activity’s effects (person, org, software).
* **Inside**: *agent*.
* **Counter‑example**: *“RBAC role”* ← access status, **not** a PROV agent.

---

### 12.3 ITIL 4 (services Context)

**Card E — “service‑level objective”**

* **Label**: Tech **SLO** · Plain **service target**
* **Sense line**: A **target value/range** for a **service characteristic** used to define acceptable service.
* **Inside**: *service‑level objective*, *SLO*.
* **Counter‑example**: *“Actual availability 99.5%”* ← observation, **not** the target.

**Card F — “incident”**

* **Label**: Tech **incident** · Plain **service disruption**
* **Sense line**: An **unplanned interruption** or reduction in quality of a service.
* **Inside**: *incident*.
* **Counter‑example**: *“Fault in plant sensor”* ← Sys‑CAL fault; different Context.

---

### 12.4 SOSA/SSN (sensing Context)

**Card G — “observation (act)”**

* **Label**: Tech **observation** · Plain **measurement act**
* **Sense line**: An **act** applying a **Procedure** to a **FeatureOfInterest** to yield a **Result** for a property.
* **Inside**: *observation*.
* **Counter‑example**: *“Temperature is 20 °C”* ← **result value**, not the act.

---

### 12.5 OWL 2 (types Context)

**Card H — “subclass‑of”**

* **Label**: Tech **subclass‑of** (⊑) · Plain **is‑a (class)**
* **Sense line**: A **class inclusion**: every instance of **C** is an instance of **D**.
* **Inside**: *SubClassOf*, *is‑a* (when authors use it for classes).
* **Counter‑example**: *rdf\:type* (instance‑of) — not class inclusion.

**Card I — “equivalent‑class”**

* **Label**: Tech **equivalent‑class** · Plain **same class extension**
* **Sense line**: Mutual class identity by extension; two labels for **the same** set of instances.
* **Inside**: *EquivalentClasses*.
* **Counter‑example**: *owl\:sameAs* (individual identity), different predicate.

---

### 12.6 IEC 61131‑3 (control‑runtime Context)

**Card J — “task (runtime)”**

* **Label**: Tech **task** · Plain **program runner**
* **Sense line**: A **cyclic or event‑driven** execution unit that **invokes programs** on schedule or trigger.
* **Inside**: *task*.
* **Counter‑example**: *“Control algorithm”* ← design/method, not the runtime task.

---


---

## 5 · Normative rules — Role Descriptions (context‑local labels)

Let **T** be a Role Description in Context **C** with SenseCell `sense(T)=⟨C,σ⟩`.

**R‑RD‑1 (Two registers).** Provide **both**:
`Tech(T)` = the **Context‑idiomatic** phrase (exact canon wording if possible).
`Plain(T)` = a brief, neutral explanation *that does not broaden meaning*.
*Symbolic alias* is optional and purely informative.

**R‑RD‑2 (No Context tags in labels).** Do **not** embed the Context name in the label (avoid “(BPMN)” in the label itself). Context is already carried by the **SenseCell**; keep labels clean.

**R‑RD‑3 (senseFamily‑aware morphology).**
— **Role** names are **countable nouns** for masks (e.g., *Participant*, *Operator*, *Reviewer*). Avoid verbs and gerunds. Add the suffix **“Role”** **only** if the Context idiom risks confusion with a substance or a status (e.g., *“Reviewer Role”* in a Context that also has a *“Reviewer Status”*).
— **Status** names are **state nouns** or **adjectival‑noun collocations** (e.g., *Approved*, *Compliant*, *In‑Service*, *Access Role* (RBAC)). If a family of levels exists, encode the **level** (`Assurance L1`, `Readiness L2`) rather than inventing decorative adjectives.

**R‑RD‑4 (Local idiom first).** Prefer the **canon’s term of art** even if it sounds narrower than a cross‑discipline cliché. The Plain label handles pedagogy; the Tech label honours the Context.

**R‑RD‑5 (Minimal generality).** Choose the **narrowest label** whose invariants you actually assert. Do **not** “upgrade” *Task* to *Activity* or *Process* just to sound universal.

**R‑RD‑6 (No permissions by stealth).** Role labels **must not** imply entitlement (*“Privileged Operator”* is a Status+Role mashup). Keep deontics in **Status** names in the **deontics Context**.

**R‑RD‑7 (Edition‑neutral labels).** Do **not** bake edition/profile into labels. Edition lives in the **Context**; the card binds to a SenseCell that already encodes edition where needed.

**R‑RD‑8 (Short and stable).** Favour **1–3 words**. Avoid rhetorical adjectives (*“robust, optimal, best‑practice”*).

---


---

## 6 · Normative rules — U.Types (Cross‑context labels)

Let **U** be a U.Type minted from a **Concept‑Set row** (F.7) satisfying A.8 (≥3 domain families) AND MinInterFamilyDistance ≥ δ_family (from F1‑Card).

+**R‑UT‑1 (Witnessed neutrality).** The Tech label **must not** be a term owned by one context when alternatives exist. Prefer **discipline‑neutral head nouns** (*Result, Reading, Execution, Evidence, Requirement, State, Type Node*). **Use** *Characteristic/Scale/Value/Level/Coordinate/Score/Gauge* **only** when the U.Type denotes a **measurement‑sense** kind anchored in a declared **CharacteristicSpace**; otherwise avoid these measurement‑canon terms to prevent semantics bleed.

**R‑UT‑2 (Minimal generality).** Name the **least upper sense** that all row witnesses share. If *Observation* and *Measurement* disagree, perhaps the U.Type is **Result** or **Reading**, not **Observation**.

**R‑UT‑3 (No senseFamily mixing in names).** Do **not** name a U.Type with deontic or behavioural language (*“PermittedService”*, *“ResponsibleAgent”*). **Role/Status/Method/Execution** belong to **Role Descriptions (F.4)** or local senses; U.Types are *what‑it‑is* kinds, not *what‑it‑does* or *what‑is‑allowed*.

**R‑UT‑4 (Head–modifier discipline).** Prefer **head nouns** with **light modifiers** over stacked compounds.
Good: *Evidence Status*, *Requirement Status*, *Type Node*.
Risky: *Multi‑stage‑workflow‑execution‑record* (compresses a scenario into a name).

**R‑UT‑5 (No Context tags in names).** U.Types are **Context‑agnostic**; never append “(BPMN)”/“(PROV)”. Provenance for the row lives in F.7, not in the name.

**R‑UT‑6 (Alias only for pedagogy).** Allow **Plain aliases** for teaching; **Tech label** is unique and stable. Synonym management belongs to **F.13**; do not invent alternates ad hoc.

**R‑UT‑7 (Family coherence).** When minting a **family**, use **parallel shapes** (*… Status*, *… Level*, *… Characteristic* **only for measurement families with a declared CharacteristicSpace**) so related U.Types signal relation by form.

**R‑UT‑8 (Symbolic names sparingly).** Symbols may be listed as *aliases* for readers of formal sections; they are **never** the U.Type’s Tech label.

**R‑UT‑9 (No edition/version in name).** Versions live in the Concept‑Set evidence; the name denotes a **time‑robust kind**.



---

# F.9 — Alignment & Bridge across Contexts \[A] 

**“Translate across Contexts; never collapse them.”**
**Status.** Architectural pattern \[A], architheory‑agnostic.
**Builds on:** E.10.D1 (Context discipline: Context ≡ U.BoundedContext); **F.0.1 (senseFamily & StatusModality guard; Bridge‑only crossing)**; F.1 (Contexts fixed); F.2/F.3 (Cells exist); F.7 (rows depend on Bridges); F.8 (thresholds τ).

**Coordinates with.** B.3 **Trust & Assurance Calculus** (uses CL penalties); **A.6.1 U.Mechanism** (Transport clause for cross‑context use; penalties route to **R/R_eff** only; **F/G** invariant); Part C architheories (apply Bridges in formal claims).
**Aliases (informative).** *Context‑to‑Context translator*; *Sense bridge*.


---

## 6 · Bridge kinds (senseFamily‑aware)

> **Two families** of Bridges: **Substitution Bridges** (senseFamily‑preserving; can support Concept‑Set rows) and **Interpretation Bridges** (explanatory; **not** for substitution).

### 6.1 Substitution Bridges (sense‑preserving)

These relate **SenseCells of the same senseFamily** and may license **limited substitution**:

1. **Equivalence (≈)** — *near‑identity of sense*. Symmetric. Rare.
   *Use:* May support **Type‑structure** rows when CL=3 and invariants match.
   *Loss Notes:* usually “none” or “profiling differences”.

2. **Narrower‑than (⊑)** / **Broader‑than (⊒)** — *proper inclusion of sense*. Directional.
  *Use:* Safe to substitute **narrower → broader** in **Naming-only** and sometimes **Role Assignment & Enactment**; **broader → narrower** is unsafe.
   *Loss Notes:* “loses special cases X”.

3. **Partial‑overlap (⋂)** — *non‑empty intersection, neither includes the other*.
  *Use:* **Naming-only** at best. **Never** justifies Role Assignment & Enactment / Type-structure.
   *Loss Notes:* “A-only senseFamily”, “B-only senseFamily”.

4. **Disjoint (⊥)** — *explicit contrast*.
   *Use:* For **didactic warnings**; not a reuse license.
   *Loss Notes:* n/a (it asserts incompatibility).

### 6.2 Interpretation Bridges (cross‑senseFamily, explanatory)

These **do not allow substitution** but **explain connections** across senseFamilies:

5. **Design‑spec ↔ Run‑trace (⇄ᴅʀ)** — a design concept relates to its run‑time occurrence.
   *Example:* *BPMN\:Process* ⇄ᴅʀ *PROV\:Activity*.
   *Use:* Explain pipelines (design → execution → provenance). No Concept‑Set rows.
   *Loss Notes:* “graph vs event”, “control‑flow vs temporal extent”.

6. **Measure‑of / Evidence‑for (→ᴍᴇᵃ)** — a measurement SenseCell evidences or quantifies another **senseFamily** (e.g., a Requirement clause).
   *Example:* *SOSA\:Observation* →ᴍᴇᵃ *ITIL\:SLO fulfilment*.
   *Use:* Explain evaluation. No substitution.

7. **Policy‑implies / Obliges (→ᴅᵉᵒ)** — a deontic statement constrains another **senseFamily**.
   *Example:* *ODRL\:Duty* →ᴅᵉᵒ *Service behaviour*.
   *Use:* Explain constraint propagation.

> **Rule of thumb.** If you want **rows** or **substitution**, you need a **Substitution Bridge** on the **same senseFamily**. If you want to **explain** why artefacts relate without claiming sameness, use **Interpretation Bridges**.

---


---

# F.10 — Status Families Mapping (Evidence • Standard • Requirement) \[A] 

**“Keep statuses in their native modality; translate between Contexts explicitly.”**
**Status.** Architectural pattern \[A], architheory‑agnostic.
**Builds on:** E.10.D1 **D.CTX** (Context ≡ `U.BoundedContext`); F.1 (Contexts), F.2 (Seeds), F.3 (Local‑Senses → SenseCells), F.4 (Role Description **Status** templates), F.9 (Bridges).
**Coordinates with.** B.3 **Trust & Assurance Calculus** (interprets CL penalties); Part C architheories: **KD‑CAL** (measurement semantics), **Norm‑CAL** (deontic logic), **Method‑CAL** (DesignRunTag).

---


---

## 6 · The spine: three local ladders (Context‑native, small and renameable)

> The following ladders are **didactic spines**. Each Context may rename levels or insert thin sub‑levels, but Bridges must state how they align to this spine (kind & CL). Names appear in **Tech** / **Plain** register.

 -   **Episteme‑as‑actor (forbidden).** Never attribute **Work** to an Episteme; only Systems act.
    
-   **Requirement vs Hypothesis.** “Desired property/goal” is **not** `Requirement` status; use hypothesis/target + evaluation.
    
-   **Mereology ≠ Provenance.** Part‑whole edges never justify claims; use EPV‑DAG with carriers.


### 6.1 EvidenceStatus (epistemic statusModality)

**Levels (from weaker to stronger):**

1. **Observed** / *Seen once.*
2. **Measured** / *Quantified under a declared procedure.*
3. **Corroborated** / *Seen independently (≥ 2 distinct sources/procedures).*
4. **Replicated** / *Repeated by others under varied conditions.*
5. **Refuted** *(negative polarity)* / *Counter‑evidence overrides prior levels.*
6. **Inconclusive** *(neutral)* / *Insufficient signal.*

**Context alignment examples (illustrative):**
`SOSA/SSN:Observation` ↦ **Observed/Measured**; `GxP validation datapack` may map to **Replicated** (if protocol diversity holds) with **CL stated**.

**Invariants (context‑local):**
*Replicated ⇒ Corroborated ⇒ Measured ⇒ Observed.* Negative (**Refuted**) cancels positives **within the same Window**.

---

### 6.2 StandardStatus (deontic/curatorial statusModality)

**Levels (design‑time stance):**

1. **Candidate** / *Proposed, under review.*
2. **Draft** / *Working text, not normative.*
3. **Approved** / *Normative in this Context/edition.*
4. **Deprecated** *(negative)* / *Discouraged; may be removed.*
5. **Superseded** *(negative)* / *Replaced by a newer edition/profile.*

**Context alignment examples:**
`ISO profile: Published International Standard` ↦ **Approved**; `IETF RFC (Proposed Standard)` ↦ **Draft/Approved** depending on local policy; **CL must be declared** on the Bridge.

**Invariants:**
At most one positive stance at a time **per Context & edition**; **Superseded** implies **Approved** held in a prior Window.

---

### 6.3 RequirementStatus (deontic/compliance statusModality)

**Levels (run‑aware stance toward an obligation):**

1. **Applicable** / *The clause binds in this Window.*
2. **Inapplicable** / *Clause does not bind under stated conditions.*
3. **Satisfied** *(positive)* / *Met within Window.*
4. **Violated** *(negative)* / *Not met within Window.*
5. **Waived** *(neutral/administrative)* / *Binding suspended with justification.*
6. **Pending** *(neutral)* / *Awaiting evaluation or evidence.*

**Context alignment examples:**
`ITIL4:SLO achieved` ↦ **Satisfied**; `ODRL:Duty fulfilled` ↦ **Satisfied**; `ODRL:Prohibition breached` ↦ **Violated**.

**Invariants:**
For the **same clause and Window**, **Satisfied** and **Violated** are **mutually exclusive**. **Applicable** is a **precondition** for either; **Waived** switches off the precondition temporarily.

### 6.4 Contextual Citation Operators (pointer)

**Citation operators (context‑scoped).** Authors MAY use the **typed edges** `supports`, `refutes`, `dependsOn`, `supersedes` **inside a single Context** when expressing how an `Evidence`/`Standard` status applies. **Formal semantics live in B.3.2 (Evidence & Validation Logic).** Cross‑Context use requires a declared **Bridge** (F.9) and carries CL/Loss penalties.



---

# F.11 — Method Quartet Harmonisation \[A] 

**“Keep the *how* (Method), the *recipe* (MethodDescription), the *happening* (Work/Execution), and the *control push* (Actuation) in their own Contexts—then relate them explicitly.”**

**Status.** Architectural pattern \[A], architheory‑agnostic.
**Builds on:** E.10.D1 **D.CTX** (Context discipline); A.3/**A.3.1**/**A.3.2** (Transformer Constitution; `U.Method`, `U.MethodDescription`); A.15/**A.15.1** (`U.Work` as record of occurrence); Sys‑CAL (control/actuation semantics); KD‑CAL (observation).
**Coordinates with.** F.1–F.3 (Contexts, Seeds → SenseCells), F.4 (Role Description), F.5 (Naming), F.6 (Role Assignment & Enactment Cycle (Six-Step)), F.7/F.9 (Bridges), F.10 (Status families & Windows).
**Aliases (informative).** *Method/Spec/Work/Actuation split*; *design/run harmonisation*.

---


---

## 7 · Harmonisation map (Context‑first)

> Examples of **local SenseCells** and **safe Bridges**. *You may keep the exact Contexts from your F.1 cut.*

**Design (ideas & recipes).**

* *SPEM/ISO 24744 Context*: `SenseCell{Method}` = *Activity Definition / Task Definition*; `SenseCell{MethodDescription}` = *Process Description / WorkProduct* (as recipe).
* *BPMN 2.0 Context*: `SenseCell{MethodDescription}` = *Process (diagram)* as **design‑time** recipe (do not confuse with run).
* *OWL/Kind-CAL Context*: labels for Method kinds (type taxonomies) when needed (naming, not behaviour).

**Run (occurrences & outputs).**

* *PROV‑O Context*: `SenseCell{Work}` = *Activity* (time‑bounded occurrence).
* *SOSA/SSN Context*: Observations **about** Work results (feeds EvidenceStatus).
* *IEC 61131‑3 Context*: `SenseCell{Work}` = *Task executes Program* (runtime); `SenseCell{Actuation}` = *Output command / setpoint* emitted by the program.

**Typical Bridges (with intent).**

* `BPMN:Process (design)` **≈** `SPEM:Process Definition` (design↔design; CL depends on modelling profile; Loss: expressiveness gaps).
* `IEC:Task execution` **⊑** `PROV:Activity` (run↔run; Loss: control‑specific timing semantics, scan cycles).
* `Actuation (IEC)` **⋂** `Activity (PROV)` (intersection: the *sub‑intervals* where outputs are emitted).
* `SOSA:Observation` **interprets** `Requirement clause` (F.10) about **Work outcomes** (**cross‑StatusModality: epistemic→deontic; never substitution**; declare **Bridge(kind=Interpretation, CL, Loss)**).

---


---

# F.12 — Service Acceptance Binding \[A] 

**“Judge promises on what happened, not on what was planned.”**
**Status.** Architectural pattern \[A], architheory‑agnostic.
**Builds on:** F.1 **context of meaning (U.BoundedContext)**; F.2 **Term Harvesting**; F.3 **Intra‑Context Sense Clustering**; F.5 **Naming Discipline**; F.7/F.9 **Bridges & CL**; F.10 **Status Families & Windows**; F.11 **Method Quartet Harmonisation**; A.2.3 **U.Service**.
**Coordinates with.** KD‑CAL (Observation/Characteristic/Scale); Sys‑CAL (Work/Actuation contexts).
**Non‑goals.** No team workflows, no tooling, no editorial procedures. This pattern specifies **how to think** about acceptance, not how to store or operate systems.

---


---

## 9 · Micro‑examples (didactic, multi‑domain)

### 9.1 SaaS uptime (services + sensing)

* **Contexts:** *ITIL 4* (Clause), *PROV‑O* (Work), *SOSA/SSN* (Measure).
* **ClauseCell:** *availability ≥ 99.9% monthly*.
* **WorkCell:** *service provision* Activities during June.
* **MeasureCell:** *uptime observation* from synthetic probes.
* **Predicate:** share‑of‑time ≥ 0.999.
* **Bridge:** probe result → user availability (**kind:** proxy; **CL:** 2; **Loss:** regional gaps).
* **Verdict:** *Satisfied (June)* if the ratio holds; **attaches to Clause\@June about those Works**.

### 9.2 Furnace band (industrial control)

* **Contexts:** *quality/deontics canon* (Clause), *IEC 61131‑3/PROV* (Work), *KD‑CAL* (Measure).
* **ClauseCell:** *product temperature within \[720,740] °C during soak*.
* **WorkCell:** *soak phase* Work interval.
* **MeasureCell:** thermocouple Observations (KD‑CAL).
* **Predicate:** band conformance.
* **Bridge:** IEC task interval → PROV Activity (**Interpretation**, CL=2).
* **Verdict:** *Violated* if any measured value exits the band.

### 9.3 Incident MTTR (services + enactment)

* **Contexts:** *ITIL 4* (Clause), *PROV‑O* (Work).
* **ClauseCell:** *MTTR ≤ 60 min per incident*.
* **WorkCell:** each incident’s handling Activity.
* **MeasureCell:** timestamps (Observed facts) of start‑fix and restore events.
* **Predicate:** duration ≤ 60 min.
* **Bridge:** BPMN steps → PROV Activity (**Interpretation**, CL=2).
* **Verdict:** *Satisfied* if the measured interval meets the target.


---

# F.13 — Lexical Continuity & Deprecation \[A] 

**“Change names without changing history.”**
**Status.** Architectural pattern \[A], architheory‑agnostic.
**Builds on:** F.1 **context of meaning**; F.2 **Term Harvesting**; F.3 **Intra‑Context Clustering (SenseCell)**; F.5 **Naming Discipline**; F.7 **Concept‑Set (row) construction**; F.8 **Mint‑or‑Reuse decision**; F.9 **Bridges**; F.10 **Status windows**.
**Coordinates with.** Part C CALs when canon editions change (Sys/KD/Type/Method/LCA).
**Non‑goals.** No registries, workflows, editors, or storage formats. No by‑name Cross‑context equivalence. No silent rewrites of old texts.

---


---

# F.14 — Anti‑Explosion Control (Roles & Statuses) \[A] 

**“Name less, express more.”**

**Status.** Architectural pattern \[A], architheory‑agnostic.
**Depends on.** F.1 **context of meaning**; F.2 **Harvesting**; F.3 **Local Sense Clustering**; F.4 **Role Description**; F.5 **Naming Discipline**; F.7 **Concept‑Set Table**; F.8 **Mint‑or‑Reuse**.
**Coordinates with.** F.10 **Status Windows & Mapping**; F.11 **Method Quartet Harmonisation**; F.12 **Service Acceptance Binding**; F.13 **Lexical Continuity**.
**Aliases (informative).** *Role/Status economy*; *Explosion guard*.

---


---

# F.15 — SCR/RSCR Harness for Unification \[A] 

**“Prove locality and parsimony first; only then prove composition.”**
**Status.** Architectural pattern \[A], architheory‑agnostic.
**Builds on:** E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; F.0.1 **Foundational Principles**; F.1–F.14.
**Coordinates with.** B.3 **Trust & Assurance Calculus** (for CL use on Bridges).

---


---

# F.16 — Worked‑Example Template (Cross‑Domain) \[A] 

**“Show the thought, not the tooling.”**
**Status.** Architectural pattern \[A], architheory‑agnostic.
**Builds on:** E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; F.1–F.15.
**Coordinates with.** B.3 **Trust & Assurance Calculus** (CL on Bridges); Part C architheories (Sys‑CAL, KD‑CAL, Kind-CAL, Method‑CAL).

---


---

## F.17 — Unified Term Sheet (UTS) \[A]

**“One table that a careful mind can hold.”**
**Status.** Architectural pattern \[A], architheory‑agnostic.
**Builds on:** F.1–F.3 (Contexts → seeds → local senses), F.4 (Role Characterisation), F.5 (Naming), F.7 (Concept‑Set table), F.8 (Mint/Reuse decision), F.9 (Bridges), F.10–F.12 (Status & method/service bindings), F.15 (SCR/RSCR).
**Coordinates with:** A.1.1 `U.BoundedContext`, A.7 **Strict Distinction**, A.8 **Heterogeneity**, A.11 **Ontological Parsimony**, A.15 **Role–Method–Work Alignment**.
**Non‑goals.** No registries, workflows, editors, or storage formats. No by‑name Cross‑context equivalence. No “data pipeline.” This pattern prescribes **what a UTS is** and **how to judge it**, not how to generate files.

### 1 · Intent & Applicability

**Intent.** Provide a **single, normative table**—the **Unified Term Sheet (UTS)**—that distils the output of F.1–F.12 into **human‑readable rows**. Each row expresses **one Concept‑Set** unified into **one FPF U.Type** with its **Tech/Plain names** and **cross‑context senses**. The UTS is the *front‑door view* that authors, engineers, and managers use; it replaces scattered notes and eliminates guesswork.

**Applicability.** Produce a UTS **per architheory thread** (e.g., *Role Assignment & Enactment*, *Method quartet*, *Trust & Evidence*). Use it:

* to **name** U.Types and their **Tech/Plain** labels (F.5),
* to **teach** the mapping from familiar canons to unified concepts,
* to **audit** coverage and heterogeneity (A.8), and
* to **feed** examples in Parts A/C without re‑explaining terminology.

**Why now.** Earlier F‑patterns define *how to think*. **F.17** defines *what you publish* so others can think with you.

### 2 · Problem Frame

Without a single sheet:

1. **Locality is lost.** Mappings hide in prose; readers re‑globalise words.
2. **Naming drifts.** Teams adopt ad‑hoc labels that collide later.
3. **Coverage is opaque.** No quick check that coverage spans **≥ 3 domain families** across the sheet (A.8).
4. **Didactic load spikes.** Each section re‑teaches the same terms.

**UTS** fixes this by putting the **unification decision** and the **cross‑context evidence** on **one line** per concept.

---

### 3 · Forces

| Force                             | Constraint in UTS                                                                                                   |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Didactic primacy vs. fidelity** | UTS keeps **two names** (Tech/Plain) and **one‑line rationale**, but never misstates a source meaning.              |
| **Parsimony vs. recall**          | Each row is one concept; the UTS as a whole demonstrates heterogeneity across ≥ 3 domain families (A.8). Rows may cite fewer Contexts when the concept truly appears in fewer.                   |
| **Locality vs. comparability**    | Senses are **Context‑scoped** (E.10.D1). Cross‑context relations are shown only as **explicit bridges** (F.9) with **CL**. |
| **General usability**             | Sheet must be **legible on paper** and **memorisable** (block structure, stable row order).                         |

---

### 4 · Core Idea

**A UTS is a Concept‑Set table with names.**
Each **row** = one **Concept‑Set** unified into one **FPF U.Type** (the “what we mean”).
Each **column family** shows **how this concept appears** in the chosen **contexts of meaning** (F.1).

Two **canonical layouts** are allowed (pick one or publish both):

* **Layout A — Kernel‑first**: rows keyed by **FPF U.Type**; **Bounded‑Context Columns (BCC)**.
* **Layout B — Base‑concept**: rows keyed by **Base concept** (EN/RU) of a discipline, then unified to **U.Type**; **Discipline Columns (DC)**.

Both layouts are normative; choose based on audience. In Layout A, comparability is by **BCC** (*Bounded‑Context Column*); in Layout B, comparability is by **DC** (*Discipline Column*); never conflate the two.

### 5 · Minimal Vocabulary (for this pattern)

* **UTS (Unified Term Sheet).** The published, human‑readable table per thread.
* **Context.** Alias in Tech register for **`U.BoundedContext`** (E.10.D1). Normative unit of meaning; every SenseCell is scoped to a Context _(name + edition)._  
* **Bounded‑Context Column (BCC).** A didactic column used **only in Layout A**; one column per **Context (`U.BoundedContext`)** from the F.1 cut; **not a model element**; the **header includes the Context name + edition**.  
* **Discipline Column (DC).** A _discipline vantage_ used **only in Layout B** (e.g., _Operational Management_, _IT/Software_, _Physics_). A DC is **not** a **Bounded‑Context Column** and does not carry editions.  
* **Concept‑Set (CSR).** One unified concept with pointers to its SenseCells.  
* **SenseCell.** _(Context × Local‑Sense)_ address—how a Context “says that thing”.  
* **Bridge / CL.** Explicit cross‑context mapping (F.9) with Congruence Level and Loss note.
* **Plain Twin (LEX).** The LEX record pairing the **Unified Tech name** with its **Unified Plain name** for a U.Type; governed by **PTG** and referenced by `Twin‑Map Id (LEX)` (E.10 LEX‑BUNDLE).
* **Block Plan.** Didactic grouping of rows to keep the sheet memorizable.  
* **Unified Tech name / Unified Plain name.** Dual‑register names chosen per F.5; the **Tech name is the neutral, unified term** for the U.Type, not a borrowed Context name.

> **Discipline.** “Context” always means **`U.BoundedContext`** (E.10.D1). No global words.

### 6 · Row Schema (normative)

Every UTS row **MUST** carry the following fields (verbatim headings recommended):

| Field                     | Purpose                                                                                               |
| ------------------------- | ----------------------------------------------------------------------------------------------------- |
| **# / Block**             | Stable id and didactic block (see §7).                                                                |
| **FPF U.Type**            | Canonical kernel type (e.g., `U.Work`).                                                               |
| **Unified Tech name**     | Short technical name used in spec prose (F.5).                                                        |
| **Unified Plain name**    | Everyday name for non‑specialists (F.5).                                                              |
| **Plain‑Twin Governance (PTG) (optional)** | Stance for the Unified Plain twin: {**Strict**, **Guarded**, **Provisional**}; use when additional discipline of the Plain twin is required (E.10 LEX‑BUNDLE). |
| **Twin‑Map Id (LEX) (optional)** | Identifier of the Tech↔Plain twin record in the LEX‑BUNDLE; cite when `PTG ≠ Strict` or when multiple candidate twins exist. |
| **FPF Description**       | One‑line definitional gist (no examples).                                                             |
| **SenseCells (by context)** | Per selected Context: the local term(s) or construct that best realises the concept (one cell per Context). |
| **Bridges (CL/Loss)**     | For any cross‑context relation, record the F.9 Bridge with **CL** and a 2–6‑word loss note; if identity, mark **CL=3 (identity)**. |
| **Unification Rationale** | One sentence: why these senses are the same *conceptually*.                                           |
| **Notes (optional)**      | Brief DesignRunTag or trip‑wire hints (e.g., “design vs run”).                                     |

**Constraint.** “SenseCells (by **Context**)” **MUST** cite **at least three** distinct **Contexts** overall across the sheet for the thread (A.8). A single row may show fewer if the concept truly appears in fewer contexts; coverage is a property of the whole UTS.

**Discipline:** Every SenseCell **must** cite the **Context name + edition** (e.g., _“BPMN 2.0 (2011): Activity instance”_).

#### 6.1 · NQD Fields (normative; when applicable)

If a UTS row **describes** a **Generator/Selector/Portfolio** (design‑time or run‑time artefact), it **MUST** add the following fields. These are *publication* fields, not tooling‑specific formats.

| Field | Purpose |
| --- | --- |
| **N (Novelty)** | Lawful novelty claim tied to `CharacteristicSpaceRef` + `DistanceDefRef` (declare metric/pseudometric & invariances; cite edition ids). |
| **U (Use‑Value)** | Declared acceptance/test value under the active **CG‑Frame** (units & scale typed per MM‑CHR). |
| **C (ConstraintFit)** | Feasibility against **ResourceEnvelope/RiskEnvelope** (and relevant deontic/ethics clauses); no `unknown→0` coercion. |
| **D\_P (Portfolio Diversity)** | Diversity contribution relative to the **current PortfolioPack** (`ArchiveConfig`, grid/binning, K‑capacity, dedup). |
| **E/E‑LOG policy‑id** | Edition id of the explore/exploit governor policy that governed generation/selection budgets. |

**Note.** These fields *extend* the Row Schema; they do not change SenseCells/Bridges/Names. Rows that are *purely definitional* (no generator/selector/portfolio semantics) do not carry §6.1.

#### 6.2 · Autonomy fields (when applicable)
Add the following columns (nullable; **required** when autonomy is claimed by the row’s subject):
* `AutonomyBudgetDeclRef` (id, version)
* `Aut-Guard policy-id`
* `OverrideProtocolRef`
* `Scope (G)` (autonomy scope)
* `Γ_time` (admission window selector)
* *(optional)* `ScaleLensPolicyRef`
* *(optional)* `ScaleLensOptIn ∈ {OptedIn, Neutral, OptedOut}`
**Note.** These fields are required for UTS rows that describe a **Role**, **Method**, **Service**, or **Selector** with autonomy claims; optional fields make **Bitter‑Lesson/Scale‑Lens** an explicit **opt‑in** with published criteria.

### 7 · Block Plan (didactic grouping)

A UTS **MUST** declare a **Block Plan**—the sequence of blocks that group rows. Blocks are **thread‑specific**. Example **Block Plan** for *Role Assignment & Enactment* (matches your earlier tables):

* **Block A · Context & Roles** — `U.BoundedContext`, `U.Role`, `U.RoleAssignment`, `U.Capability`.
* **Block B · Method & Description** — `U.Method`, `U.MethodDescription`, Access/Acceptance descriptions (fields of `U.Service`).
* **Block C · Execution & Schedule** — `U.Work`, `U.WorkDescription`, `U.Observation`.
* **Block D · Service & Deontics** — `U.Service`, `U.SpeechAct`, `U.Commitment`, `U.ServiceClause`, `U.ServiceEvaluation`.
* **Block E · Carriers & Bridges** — `U.Carrier`, *Alignment (Bridge entry)*.
* **Block R · Knowledge Units & Statuses** — `U.Episteme`, `U.EvidenceRole`, `U.StandardStatus`, `U.RequirementStatus`, `U.DefinitionRole`, `U.AxiomaticCoreRole`.

> **Rule.** Block names are **didactic**, not ontological. Do **not** infer mereology or subtyping from blocks.

### 8 · Column Families (two canonical layouts)

#### 8.1 Layout A — Kernel‑first (U.Type as rows)

**Columns:**

* `FPF U.Type · Unified Tech name · Unified Plain name · Plain‑Twin Governance (PTG) · Twin‑Map Id (LEX) · FPF Description` *(left rail; `PTG`/`LEX` are optional)*
* **Bounded‑Context Columns (BCC)** — one column per **Context (`U.BoundedContext`)** from the F.1 cut; each header shows _name + edition_: e.g., **OMG BPMN 2.0**, **W3C PROV‑O**, **ITIL 4**, **NIST RBAC**, **W3C SOSA/SSN**, **OMG Essence (Language)**, **DEMO/DEMO‑EO**, **PMBOK 7**, **CM/BPM (CMMN/BPMN)**, **IEC 61131‑3**, **ODRL 2.2**, **ISO 80000‑1 / Metrology** … *(your chosen 12 Contexts)*
* `Bridges (CL/Loss)`
* `Unification Rationale`
* `Notes`
  
Do not mix **Discipline Columns (DC)** in Layout A. Columns here are only **Bounded‑Context Columns (BCC)**.

#### 8.2 Layout B — Base‑concept pivot (discipline columns)

**Columns:** Base concept · Scale‑map · Unified Tech name · **Unified Plain name** · Plain‑Twin Governance (PTG) · Twin‑Map Id (LEX) · Formal U.Type · **Discipline Columns (DC)** (e.g., Operational Management / IT/Software / Physics / …) · Rationale · Notes.

* `Base concept (EN / RU)`
* `Scale‑map (Σ / Π / μ)` *(optional; see §9.4)*
* `Unified Tech name`
* `Unified Plain name`
* `Plain‑Twin Governance (PTG)` *(optional)*
* `Twin‑Map Id (LEX)` *(optional)*
* `Formal U.Type`

* **Discipline Columns (DC)** (choose 3–5): e.g., **Operational Management**, **IT/Software**, **Physics**, **Science/Theory**, **Math/Proof**, **Literature**, **Religion** *(or other discipline columns suited to the thread)*
 * `Unification Rationale`
* `Notes`
 
> **Guidance.** Publish **Layout A** for kernel users and spec authors; publish **Layout B** for cross‑disciplinary onboarding and teaching.
> **Clarification — Plain vs Base concept.** In Layout B the `Base concept (EN/RU)` is a **discipline vantage** aid and **does not substitute** for the single **Unified Plain name** in the left rail. Do not mint alternative unified‑plain synonyms inside DC cells; flag homonym risks with ⚡ in `Notes`.

### 9 · Invariants (normative constraints)

1. **Locality.** Every SenseCell is **Context‑scoped** (E.10.D1). No global synonyms.
2. **Bridges only via F.9.** Cross‑context equivalence appears **only** as an explicit Bridge with **CL**. Any row citing > 1 **Context** must state at least one Bridge.
3. **Heterogeneity.** Across the UTS, coverage must involve **≥ 3 domain families** (F.1 Step 2; A.8).
4. **Scale‑map tags (optional but disciplined).** If used in Layout B:
   * **Σ (Summative):** concept’s quantitative properties aggregate across a population of executions/holders.
   * **Π (Conjunctive/Compositional):** concept composes by required conjunction (all‑of), not by averaging.
   * **μ (Micro/Atomic):** concept is inherently micro‑level (per single execution/holder).
     *(Tags aid teaching; they do not change semantics.)*
5. **Strict Distinction.** Use `U.Method` vs `U.MethodDescription`, `U.Work` vs `U.WorkDescription`, `U.Role` vs `U.RoleCharacterisation` correctly; do **not** collapse intensional objects with their descriptions.
6. **Dual register.** Every row has **Tech** and **Plain** labels per F.5.
7. **One‑breath rationale.** The `Unification Rationale` is a **single sentence** explaining the conceptual sameness despite local wording.
8. **Unified naming neutrality.** The **Unified Tech name** is the neutral FPF choice per F.5; it is **not** lifted wholesale from any single Context unless the Concept‑Set justification (F.7) shows identity.  
9. **Column discipline.** Layout A uses **Bounded‑Context Columns (BCC)** only; Layout B uses **Discipline Columns (DC)** only. Mixing is non‑conformant.
10. **Plain‑twin discipline.** The single **Unified Plain name** lives in the left rail; BCC/DC cells carry senses only. Any additional Plain aliases are managed in LEX (tv:*) and never minted per column.


### 10 · How to Compile (conceptual moves, not a workflow)

**M1 · Fix contexts (F.1).** Declare the **12 (±)** contexts for this thread.
**M2 · Harvest & cluster (F.2–F.3).** Identify candidate senses per Context; cluster *within* Contexts; mint **SenseCells**.
**M3 · Form Concept‑Sets (F.7).** For each “the‑same‑thing” across Contexts, create one **CSR**; attach SenseCells.
**M4 · Name (F.5).** Choose **Tech/Plain** labels; assert the **FPF U.Type** (or propose a new one via F.8).
**M5 · Bridge (F.9).** Where Cross‑context relations are not exact, assert Bridges with **CL** and a short **Loss** note.
**M6 · Place rows into blocks (§7).** Keep the sheet memorisable.
**M7 · Write one‑line `FPF Description` and the `Rationale`.**
**M8 · Run acceptance harness (F.15).** Apply the UTS checks in §11.

> **Note.** These are **thought moves**. No tooling is implied or required.

### 11 · Acceptance Harness (SCR/RSCR) for a UTS

#### 11.1 Static Conformance Rules (SCR‑UTS)

* **SCR‑UTS‑01 (Row completeness).** Each row contains: `U.Type`, `Tech`, `Plain`, `FPF Description`, `SenseCells (≥ 1)`, `Rationale`.
* **SCR‑UTS‑02 (Dual register).** Each row has both Tech and Plain labels; Tech is used in spec prose, Plain in didactics.
* **SCR‑UTS‑03 (Locality discipline).** Every SenseCell is cited **with its Context name & edition**.
* **SCR‑UTS‑04 (Heterogeneity).** Across the sheet, the set of referenced Context spans **≥ 3 domain families**.
* **SCR‑UTS‑05 (Bridge honesty).** All cross‑context sameness claims are expressed via an F.9 **Bridge** with a **CL** score; if identity, mark **CL=3** and note “identity/no loss” rather than omitting the bridge.
* **SCR‑UTS‑06 (One‑breath rationale).** The rationale is ≤ 35 words and states the **conceptual invariant** that unifies the row.
* **SCR‑UTS‑07 (Block parsimony).** Block Plan uses **≤ 7 blocks**; each block’s rows can be recited from memory by a careful reader.
* **SCR‑UTS‑08 (Strict Distinction).** No row description conflates Method↔MethodDescription, Work↔WorkDescription, Role↔RoleCharacterisation.
* **SCR‑UTS‑09 (Unified naming).** Each row’s **Unified Tech name** complies with F.5 rules (dual register, minimal generality, morphology); it is not a mere alias of one Context unless justified by an F.9 Bridge with **CL=3**.
* **SCR‑UTS‑10 (Column discipline).** **Layout A:** all non‑left‑rail columns are **Contexts** with editions. **Layout B:** all non‑left‑rail columns are **discipline columns**. No cross‑use.
* **SCR‑UTS‑11 (Plain‑twin hygiene).** The **Unified Plain name** appears **once** in the **left rail** (**tv:primary**). Neither BCC (Layout A) nor DC (Layout B) cells may introduce alternative **unified** Plain synonyms; use the ⚡ marker in `Notes` to flag homonym risk where needed.

#### 11.2 Regression Rules (RSCR‑UTS)

* **RSCR‑UTS‑A (Edition churn).** When a Context’s edition changes, old SenseCells remain addressable; new cells are added; **no silent rewrites**.
* **RSCR‑UTS‑B (Name stability).** Tech labels change only with a documented F.5 decision; Plain labels may evolve didactically if the Tech name stays.
* **RSCR‑UTS‑C (Coverage drift).** Adding/removing rows **must not** reduce family heterogeneity below §9.3.
* **RSCR‑UTS‑D (Loss drift).** If new evidence changes a Bridge’s CL/Loss, the row updates both the CL and the 2–6 word loss note.
* **RSCR‑UTS‑E (Plain discipline).** No per‑column Plain text appears in BCC/DC columns; any additional Plain aliases are tracked in Annex with **tv:** entries and counted against the alias budget (F.13). 

### 12 · Canonical Heading Templates (fill with your Contexts/Discipline columns)

**Layout A — Kernel‑first**

```

---

## **F.18 — Local‑First Unification Naming Protocol** \[A]
*Status: normative (Part F, Unification Suite). Audience: engineer‑managers, lead architects, editors of FPF artefacts. 

### 1. Context

Names must carry enough signal for everyday use, yet never smuggle in Cross‑context identities, hidden assumptions, or role/metric clutter. F.18 supplies that naming discipline and weaves it through F.1–F.17: Term Harvesting, Sense Clustering, Role Descriptions, Concept‑Sets, Bridges, Lexical Continuity, Anti‑Explosion control, and the Unified Term Sheet (UTS).

**Scope.** This protocol applies to naming of **any concepts** authored in Part F (U.Types and **local concepts** alike: kinds, roles, services, methods, works, relations, characteristics, states/statuses, etc.). The **U.Types** norms in this section are a **specialization**, not a restriction of scope.

**Purpose of this pattern.** Provide a **human‑legible, context‑anchored naming protocol** that:
* keeps *local meaning first* and prevents Cross‑context conflation;
* makes the **kind** of thing explicit (System, Episteme, Role, Service, Method, Work, Decision, Requirement, etc.);
* integrates smoothly with **Concept-Sets**, **`U.RoleDescription`**, and **Bridges** without requiring any special notation or tooling;
* supports lifecycle actions (mint, reuse, align, deprecate, split/merge) with a paper trail that managers can audit.

### 2. Problem

Without a shared naming protocol inside Part F, the same recurrent failures appear:

1. **Global‑name illusion.** A short label travels from one context to another and is *assumed* to mean the same thing; later, contradictions surface during acceptance or assurance.
2. **Context drift.** A label gradually changes inside its Context (edition, scope, envelope) without leaving a clean trace; readers argue over “what we meant.”
3. **Kind confusion.** Names hide *what sort of thing* is being named (System vs Episteme vs Role vs Service, etc.), leading to category errors and brittle integration.
4. **Threshold‑in‑the‑name.** Numeric limits, duty segregation, or state qualifiers get baked into names (“Critical‑Reviewer‑0.2 mm”), which cannot age or compose.
5. **Stealth renames.** Quiet label swaps, steered by fashion or politics, sever continuity with earlier evidence, plans, and bridges.
6. **Explosion by synonyms.** Teams mint many near‑synonyms instead of reusing a Concept‑Set row or creating an explicit Bridge with loss notes.

These failures erode trust, block reuse, and make Part F machinery (Concept-Sets, `U.RoleDescription`, Bridges) harder to apply.

### 3. Forces

| Force                                      | Tension to balance                                                                                                            |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| **Local truth vs Cross‑context portability**  | The name must “belong” inside one context while remaining referenceable from other contexts through explicit bridges.               |
| **Human ergonomics vs conceptual clarity** | Short, natural labels help teams move; explicit kind and Context cues keep reasoning sound.                                          |
| **Stability vs evolution**                 | Names should be durable, yet easy to deprecate or refine without breaking links to past evidence and work.                    |
| **Brevity vs auditability**                | A compact “badge” for everyday speech, plus an authoritative **Name Card** that records meaning, scope, edition, and lineage. |
| **Parsimony vs inclusivity**               | Reuse existing Concept‑Set rows where possible; mint new names only when indispensable in the local context.                     |

### 4. Solution — The Local‑First Naming Protocol

F.18 defines **eight rules** (R‑rules) and **six practices** (P‑practices). Together they produce **Name Cards** that any reader can interpret **ontologically** without guessing, and that slot cleanly into the rest of Part F.

**Path Card (subset of Name Card).** A **Name Card** whose **object‑of‑talk/entity-of-interest** is an **EvidenceGraph Path**: it cites a **PathId** (or **PathSliceId**), **Context**, **ReferencePlane**, **Γ_time**, and any **Bridge id(s) + CL/CL^plane** (with loss notes). Used by **G.6** and **G.10** to make justifications portable on UTS.

#### 4.1 The Eight R‑rules (normative)

**R1 — Speak every name *with its Context*.**
A name is **never** context‑free. When you introduce or use a name, **pair it with the Bounded Context** where it lives (the “Context of meaning”), and with the **edition** of that Context if relevant. In everyday speech: “X, *in* Y.” Cross‑context use requires a Bridge; labels alone do not travel. 

**R2 — State the ontological *Kind* on the Card.**
Every Name Card **must** state the **Kind** (System, Episteme, Role, Service, Method, Work, Objective, Requirement, Decision, Characteristic, etc.). This prevents category errors and keeps Role–Method–Work alignment clean. *Clarification:* this is a **Card requirement**, not a demand that the label string begin with the Kind.

**R3 — Declare the *Purpose / use‑domain* on the Card.**
In addition to **Kind**, the Name Card **must** state the intended **Purpose / use‑domain** that situates the concept in practice and signals **which families of contexts** are expected to use it (e.g., mathematical formalism, engineering practice, computer science, systems management). This enables reconstruction of usage from the lexicon and reduces unintended scope drift. *Clarification:* this is a **Card field**; it does **not** require the label string to carry the purpose qualifier.

**R4 — Resolve the name to a *Local‑Sense*.**
A minted name must resolve to a Local-Sense inside its Context (the result of F.2–F.3). If a name points to a Role Description, state that template and its sense basis. Avoid heavily overloaded surface terms: when needed, prefer concise two-word Tech labels that hint at the intended sense.

**R5 — Use *Twin Registers* (Unified Tech + Plain).**
Provide two human‑oriented labels on the Name Card, per **E.10** register discipline:
* a **Unified Tech** label (short, morphology‑stable, neutral in wording);
* a **Plain** label (reader‑friendly phrasing for managers and subject‑matter experts).

The **Unified Tech** label is the only one used in **Core** normative prose; **Plain** is for teaching and examples. Both remain **context‑local**; neither establishes Cross‑context identity (that is the job of the **UTS row** and **Bridges**).



+The **Unified Tech** label is the only one used in **Core** normative prose; **Plain** is for teaching and examples. Both remain **context‑local**; neither establishes Cross‑context identity (that is the job of the **UTS row** and **Bridges**).


**R6 — Keep thresholds and states *out of the name*.**
Do not encode numeric limits, separation‑of‑duties, or readiness states in the label. Put thresholds on **Method steps** (capability/acceptance), states in **Role State Graphs**, and SoD via **incompatibility** relations. Names carry *what this is* and *which Context claims it*—not *when and how it may act*.

**R7 — Cross‑context only by *Bridge* with loss notes.**
When another Context needs to reference a name, use an **Alignment Bridge** that states the relation (equivalent, narrower, broader, analogous) and its **Congruence Level** with explicit **loss/fit** annotations. Never equate two names by label alone.

**R8 — Make renames and merges *first‑class events*.**
When a label changes, or two labels consolidate or split, record it on the Name Card as a lifecycle action (rename, merge, split, retire) with rationale and dates. Past uses *remain valid as historical facts*; continuity comes from lineage, not silent edits.

#### 4.2 The Six P‑practices (normative process)

**P1 — Candidate set (*NQD-front* of seed-words).**
Do **not** pick a label “in one shot”. Build a **small, non-dominated candidate set** (an *NQD-front*, typically 5–10 items) by seeding and varying along:
**Traditions** — mathematics, physics, engineering, computer science, systems thinking, management, etc. with their typical contexts and situations; use maximum diversity here;
 **Novelty/Familiarity** — from careful **reuse** of established terms to sharper **neologisms** from recent SoTA traditions;  
 **Lexical form** — distinct **head terms** and morpheme families, readability/pronounceability, inflection/declension, transparency.
Use the **Novelty–Quality–Diversity** discipline from **Part G** to maintain only **non-dominated** candidates; when appropriate, you may implement this via **Γ_nqd.generate (G.18)**. Record the **seeds** and the short rationale in the Card’s notes. Choose final **Unified Tech**/**Plain** labels **from this frontier**; if a strong candidate is discarded, briefly note why.

For the purposes of **Diversity_P**, group candidates into **head-term families** (same base noun/verb + minor prepositions or case endings). Variants such as *“Reference plane”*, *“Plane of reference”* and *“Referred plane”* **count as one family**, not three distinct candidates. An NQD-front with multiple near-clones from one family **does not** satisfy the diversity requirement. Aim for **≥ 3 distinct head-term families** in the CandidateSet; if the front ends up with fewer families (e.g. due to a very narrow domain or strong AliasRisk on other heads), the Name Card **MUST** record a brief rationale in the NQD-front notes.

**Lexical Q‑axes for the NQD‑front**
When P1 uses **NQD‑CAL (C.18)**, treat the **Quality vector** over candidates as part of the same archive as C.18’s **NQD‑frontier**. Recommended axes (all **ordinal; no arithmetic means**):

 * **SemanticFidelity (P — Ontological precision).**
  *Question.* Does the label verify against the **Minimal Definitional Statement (MDS)** and Concept‑Set row without adding or losing core invariants?
  *Scale (ordinal; ↑ better).* `{Misleading, Vague, Precise, Exact}` with `Exact ≻ Precise ≻ Vague ≻ Misleading`.  
  *Link to P2.* When **P2** is run, derive the SemanticFidelity rating from the per‑sense‑seed judgements: candidates with any **core** sense‑seeds classified as `wrong‑prototype` **MUST** be rated **Misleading**; candidates rated **SemanticFidelity ≥ Precise** **SHOULD** have at least a configurable fraction `θ_P` (default `θ_P = 0.7`) of sense‑seeds in `on‑target` and **NONE** in `wrong‑prototype`. Discard candidates that remain **Misleading** after revision.

* **CognitiveErgonomics (S — Sociolinguistic admissibility).**  
  *Question.* Can the target **RoleEnactors** (engineers, managers) read, pronounce, and recall the label without specialist training?  
  *Scale (ordinal; ↑ better).* `{Alienating, Jargon, Acceptable, Natural}` with `Natural ≻ Acceptable ≻ Jargon ≻ Alienating`. Prefer labels **≥ Acceptable** in the home Context.

* **OperationalAffordance (O — Morphological/action alignment).**
  *Question.* Does the morphology of the label hint at its role in **methods/morphisms** (object vs process vs result) and support the required derivational family (noun/verb/participial forms)?
  *Scale (ordinal; ↑ better).* `{Opaque, Role‑hinting, Action‑aligned}`. Action‑aligned labels make it obvious whether we are naming an **actor**, an **activity**, or an **artifact** (e.g., *Author* vs *Authoring* vs *AuthoredArtifact*).  
  *Kind‑sensitive cues.* When the **Kind** on the Card is a **Role**, prefer agentive/holder morphology (*…Role*, *…er*, *…or* or local equivalents); when the Kind is **Method/MethodDescription**, prefer verbal or gerundive forms; when the Kind is **Holon**, prefer result nouns, when **Work**, prefer verb. Misaligned morphology (e.g., a Role named with a pure process noun) should be treated as a **penalty on OperationalAffordance** and, if retained for legacy or regulatory reasons, called out explicitly in **Card notes**. See F.5/F.11/F.12 and **LEX‑BUNDLE §8**.

* **AliasRisk (A — Lexical overload).**  
  *Question.* How likely is a careful reader to import a **wrong sense** from neighbouring FPF artefacts or external canons when they see this string?  
  *Scale (ordinal; ↓ better).* `{Safe, Context‑dependent, High‑Risk, Overloaded}` with `Safe ≻ Context‑dependent ≻ High‑Risk ≻ Overloaded`. Avoid adopting **Overloaded** labels unless required by legacy and called out explicitly in notes. When C.18’s **DomainDiversitySignature** is available, AliasRisk MAY be refined into a CHR‑typed characteristic with the same polarity.

Use these axes for **Pareto comparison only** (per **C.16** ordinal discipline). Do **not** collapse them into a single scalar score; the NQD‑front is computed over the **vector of lexical Q‑components** together with **Novelty** and **Diversity_P**.

**P2 — Semantic read‑through against archetypal situations.**  
Alongside the NQD‑front of label candidates, maintain a **small set of 5–10 archetypal situations** (“**sense‑seeds**”) that instantiate the intended use (purpose) across different traditions. For **each** candidate label and each sense‑seed, perform a **read‑through test**:  
– write **1–2 short example sentences per sense‑seed** (e.g., “In case X, we perform \<Label\>”);  
– classify the outcome, for a careful reader in the home Context, as one of `{too‑narrow, on‑target, too‑wide, wrong‑prototype}`.  
Maintain, on the Name Card, a small tally per candidate of how many sense‑seeds fall into each class. Use these tallies both to **prune candidates** and to instantiate **SemanticFidelity** (P‑axis): labels with a sustained pattern of `wrong‑prototype` hits on core sense‑seeds **SHALL** be removed from the NQD‑front (or kept only as deprecated aliases with an explicit warning). Candidates rated **SemanticFidelity ≥ Precise** **SHOULD** satisfy the `θ_P` constraint from the SemanticFidelity definition (fraction of `on‑target` seeds) and have no `wrong‑prototype` counts.  
Record **rejected candidates** and their **mismatch patterns** in the Name Card’s **NQD‑front notes**.

**P3 — Mint‑or‑Reuse gate (F.8).**
Before minting, search your Context’s **Concept‑Set table**. If a row already covers your sense, reuse it and only add a **local label**. If not, propose a **new row** and capture the decision in a brief rationale.

**P4 — Concept‑Set linkage (F.7).**
Every Name Card **must** indicate its Concept‑Set row (or record “not applicable” for intentionally Context‑unique names). This is the handle for alignment and anti‑explosion control.

**P5 — UTS registration (F.17).**
Publish each Name Card to the **Unified Term Sheet** with Context, kind, twin labels, sense anchor, edition, and lifecycle status. Keep the UTS the single, human‑readable table of record.

**P6 — Lifecycle hygiene (F.13).**
Apply the same discipline to renames, splits/merges, and retirements; leave a forward/backward pointer so readers can trace continuity at a glance.

### 5. The Name Card (authoring template, representation-agnostic)

#### 5.1 Card purpose & mode guard (normative)

To prevent “post-hoc justification” of intuitively chosen labels, every **Name Card** SHALL declare its
**CardMode ∈ {MintNew, DocumentLegacy}**:

* **MintNew.** The Card is the **output of an NQD-style lexical search** over a **candidate label set** generated inside
  the home Context(s), using the lexical Q-tuple `{SemanticFidelity, CognitiveErgonomics, OperationalAffordance,
  AliasRisk}` together with **Novelty (N)** and **Diversity_P** (per A.0 / C.17–C.18 / B.5.2.1).  
  – The Card SHALL record:  
    – a minimal **CandidateSet** (the labels actually evaluated), with **head-term family** tags for each candidate;  
    – the resulting **NQD-front** of **non-dominated candidates** over ⟨Q-tuple, N, Diversity_P⟩;  
    – a short **selection note** explaining why the chosen Tech/Plain pair was picked from that front
      (e.g., “better CognitiveErgonomics at equal SemanticFidelity”).  
 
  – A single-element NQD-front is permitted only if the Card records a brief rationale why **no alternative candidate
    survived** the lexical and NQD filters (e.g., legacy constraints, strong AliasRisk on all other options).

* **DocumentLegacy.** The Card documents an **externally imposed legacy label** (e.g., a regulatory or de facto Standard)
  and its mapping to FPF structures. In this mode the Card MAY omit a full NQD-front, but SHALL:  
  – state the **legacy source / provenance**;  
  – either (i) provide at least a **sketched NQD-comparison** of viable internal variants against the legacy label, or  
    (ii) record a short **out-of-scope rationale** (e.g., “name frozen by law; see cited Standard”) explaining why NQD
    search is not being used for selection.

For all **Core-surface naming of U.Types and other canonical FPF concepts**, **MintNew** is the **default** CardMode; using
DocumentLegacy for such names requires an explicit justification on the Card.

A **Name Card** is the authoritative, human‑readable record of a name inside its Context. It has these fields; teams may add local notes.

1. **Row ID** — the stable, opaque **UTS row identifier** (the identity anchor).
2. **Twin labels** — **Unified Tech** and **Plain** (per E.10).
3. **Context of meaning** — the Bounded Context and, if relevant, its edition.
4. **Kind** — what sort of thing this is (System, Episteme, Role, Service, Method, Work, Objective, Requirement, Decision, Characteristic, etc.). This is an **ontological category**, not a surface‑string prefix. 
5. **Purpose / use‑domain** — the intended area(s) of use (which families of contexts are expected to use it).
6. **Minimal Definitional Statement (MDS)** — one‑paragraph intended sense in the home context (no tool/process slang).
7. **Didactic subtitle** — ≤ 12 words that signal pragmatic use.
8. **Sense reference** — a Local‑Sense reference (how F.2–F.3 clustered it).
9. **Concept‑Set linkage** — Concept‑Set reference or “not applicable” (with rationale).
10. **Alignment note** — if a Bridge exists to other Contexts, cite it and record **loss/fit** in plain words (no formulas required on the Card).
11. **Relation kind** — if the name is for a relation, declare **structural** vs **epistemic** and `validationMode ∈ {axiomatic, inferential, postulate}`. For **structural** relations, provide **Constructive** grounding (`tv:groundedBy → Γₘ.sum|set|slice`). If the name is not for a relation with arity ≥ 2, set this field to “n/a”.
12. **Manager’s clip** — one‑line “use/avoid” guidance for everyday communication.
13. **Archetypal situations (sense‑seeds)** — **5-10 short “X‑case” lines** used by **P2** for the semantic read‑through; keep them **edition‑aware** and **context‑local**.
14. **NQD‑front seeds** — brief rationale for discarded candidates (**include mismatch patterns from P2 and any lexical Q‑scores used in P1**).
15. **SemanticFidelity/CognitiveErgonomics/OperationalAffordance/AliasRisk** scores for the NQD-front labels.
16. **Version**  — current status and history of editions.
17. **Card notes** — optional free text with comments about the name (e.g., recommended translations, etymology, pronunciation). 

**Manager’s reading habit.** When two names collide in a meeting, ask for their **Context**, **Kind**, **Purpose/use‑domain**, and **Sense anchor**. If any of those differ, you are comparing different things; switch to **Bridge** talk, not label talk.

### 6. What *belongs* in the label—and what does not

**Belongs (keeps the label clean and durable):**

* The **core head word** that names the thing *(the **Kind** is recorded on the Card; the string need not encode it)* (e.g., “Pump”, “Standard”, “Requirement”, “Surgeon”, “Cooling”).
* A **purpose qualifier** if it is essential to the local sense and stable across editions (e.g., “Cooling” vs “Fuel”).
* A **scope qualifier** only if it is part of the *meaning* rather than the current plan (“Surgical Ward” rather than dates or batch numbers).

**Does not belong (move elsewhere):**

* **Numbers and thresholds** (put on steps, capabilities, acceptance clauses).
* **States** (use Role State Graphs and checklists).
* **Temporal windows** (work plans and history).
* **Organisational authorisations** (speech acts and assignments).
* **Imported acronyms** from other Contexts (use Bridges with loss notes instead).

**Quick litmus for authors.** If removing a number, date, or state *does not* change the *meaning* of the thing, it should **not** be in the label.

### 7. Worked triad (three short, context‑local examples)

*(Names below are illustrative; the same words in other Contexts may mean something else. The point is how the Name Card keeps them clear.)*

#### 7.1 Industrial operations Context: “Thermal Management · 2026”

* **Kind:** Service
* **Purpose / use‑domain:** industrial thermal utilities; line‑level planning and operations
* **Unified Tech label:** Cooling Supply
* **Plain label:** Chilled water for line B
* **Sense anchor:** supply of water at defined temperature/flow to boundary B
* **Concept‑Set:** “Utility service” row; local variant recorded
* **Alignment note:** Bridge to “Plant Utilities · 2026” notes that “Cooling Supply” there bundles filtration; *loss:* filtration is not guaranteed in this Context
* **Version:** 20 Feb 2024
* **NQD‑front (seed candidates):** *Cooling Supply*, *Chilled Water Service*, *Process Cooling*, *Cooling Utility*. **Chosen:** *Cooling Supply* (neutral, morphology‑stable).

**Why it’s good.** The label doesn’t encode temperature or flow limits (those live in acceptance). It names a Service; nobody will confuse it with a pump System or a Method.

#### 7.2 Clinical Context: “Hospital OR · 2026”

* **Kind:** Role
* **Purpose / use‑domain:** OR governance and staffing; credentialing and checklists
* **Unified Tech label:** Surgeon Role
* **Plain label:** Operating surgeon
* **Sense anchor:** person who is authorised to perform surgical steps under defined checks
* **Concept‑Set:** “Clinical roles” row
* **Alignment note:** Bridge to “Training & Credentialing · 2026” shows partial overlap; *loss:* that Context’s “Senior Surgeon” carries teaching duties that do not apply here
* **Version:** Feb 2025; renamed‑from “Lead Surgeon” (2025) with rationale: avoided “lead” vs “operating” ambiguity
* **NQD‑front (seed candidates):** *Surgeon Role*, *Operating Surgeon*, *Primary Surgeon*, *Operating Physician*. **Chosen:** *Surgeon Role* (Kind‑neutral string; Plain clarifies).
*Lexical Q snapshot (PSOA‑style, informative).*  

| Candidate | SF | CE | OA | A‑Risk | Comment |
| --- | --- | --- | --- | --- | --- |
| Surgeon Role | Precise | Acceptable | Role‑hinting | Safe | Neutral head noun; morphology matches **Role** Kind; works across departments. |
| Operating Surgeon | Precise | Natural | Role‑hinting | Context‑dependent | Reads well, but “operating” competes with “operating theatre/room”; kept as Plain label only. |
| Primary Surgeon | Vague | Natural | Role‑hinting | Context‑dependent | “Primary” ambiguous (training vs shift); rejected for governance vocabulary. |
| Operating Physician | Vague | Jargon | Role‑hinting | High‑Risk | Collides with non‑surgical physician roles; rejected despite familiarity in some hospitals. |
 
**Why it’s good.** No fatigue thresholds or readiness states in the name; those live in the Role’s state graph and checklists.

#### 7.3 Public service Context: “Civic Services · 2026”

* **Kind:** Requirement
* **Purpose / use‑domain:** service performance management; public service SLAs
* **Unified Tech label:** Passport Lead‑Time
* **Plain label:** Time to issue a passport
* **Sense anchor:** elapsed time from complete application to issuance
* **Concept‑Set:** “Service quality requirements” row
* **Alignment note:** Bridge to “Legal Framework · 2026” records that legal “deadline” has different remedies; *loss:* legal exemptions not carried into this Context
* **Version:** current
* **NQD‑front (seed candidates):** *Passport Lead‑Time*, *Issuance Time*, *Service Turnaround*, *Time to Issue Passport*. **Chosen:** *Passport Lead‑Time* (neutral; Plain remains didactic).

**Why it’s good.** Target values (e.g., ≤ 20 days) are not in the label; they live in acceptance clauses.

---

### 8. Conformance Checklist (editor aid) — *Part I: naming & cards* (**non‑normative**)

**CCE‑F18.1 (Context pairing).**
Every name used in normative text **must** be paired with its **Context of meaning**. If you cannot name the Context, you do not have a valid name.

**CCE‑F18.2 (Kind clarity).**
Every Name Card **must** state the **kind** (System, Episteme, Role, Service, Method, Work, Objective, Requirement, Decision, Characteristic, …). Using labels that hide kind is non‑conformant.

**CCE‑F18.2a (Purpose declared).**
Every Name Card **must** state the **Purpose / use‑domain** (families of contexts where the concept is expected to be used). Omitting Purpose is non‑conformant.

**CCE‑F18.3 (Sense anchoring).**
A minted name **must** resolve to a **Local‑Sense** in its Context. If a sense cannot be stated, label minting is deferred.

**CCE‑F18.4 (Twin registers).**
Each Name Card carries a **Unified Tech** and a **Plain** label (E.10). Tech appears in **Core** prose; Plain in teaching/examples.

**CCE‑F18.5 (No thresholds/states in labels).**
Numeric limits, readiness states, and separation‑of‑duties **must not** appear in labels. Put them on steps, checklists, and role algebra.

**CCE‑F18.6 (Bridge‑only travel).**
Cross‑context reuse of a name **must** go through an **Alignment Bridge** with an explicit relation and **loss/fit** notes. Label matching alone is forbidden.

**CCE‑F18.7 (Lifecycle visibility).**
Renames, splits/merges, and retirements **must** be recorded on the Name Card with dates and rationale. Past occurrences remain valid as historical facts.

**CCE‑F18.8 (Mint‑or‑Reuse gate).**
Before minting, authors **must** check the Context’s Concept‑Set table; if a row exists, **reuse** it with a local label unless a documented reason compels a new row.

**CCE‑F18.9 (UTS entry).**
Names used in normative artefacts **must** appear on the **Unified Term Sheet** with the specified **Name‑Card fields**; include Notes when present).

**CCE‑F18.10 (No cross‑kind labels).**
Do not reuse the same **Unified Tech label** for different kinds inside one context (e.g., “Cooling” as a Service and as a Method). If unavoidable, add a stable qualifier to disambiguate and record the decision on both Name Cards.

**CCE‑F18.11 (Manager’s clip).**
Each Name Card **should** carry a one‑line “use/avoid” note to guide everyday speech. Where omitted, editors add it during review.

**CCE‑F18.12 (Anti‑explosion check).**
If three or more near‑synonyms for the same Local‑Sense appear in drafts, authors **must** either consolidate to one label or record an intentional synonym pair with use/avoid notes and a plan to converge.

### 9. Normative Standard (what must be true)

> This section is binding. It specifies the publication Standard for unification‑oriented names in the Unification Suite (Part F), with **local‑first authority**, **bounded context clarity**, and **one‑way unification** upwards along the ladder. It complements, and does not replace, the structural and epistemic Standards elsewhere in FPF.

**9.1 Local authority & home.**
Every unification name has a **single home**: exactly one *Bounded Context* that authors and stewards it. The home is responsible for the definition, examples, and lifecycle of the name. Cross‑context reuse happens by **bridges**, not by relocating the home.

**9.2 Minimum definitional payload.**
A published name MUST ship with a human‑readable **Minimal Definitional Statement (MDS)** that states the intended sense in the home context, and a **Didactic Subtitle** (≤ 12 words) that signals its pragmatic use. The MDS must be free of process slang and implementation jargon.

**9.3 Row ID + label surfaces.**
For each adopted name, the home supplies:
* a **Row ID** (the opaque UTS identifier — the **identity anchor**), and
* two **label surfaces**: a **Unified Tech** label (for Core prose) and a **Plain** label (for teaching).
  Both labels refer to the same underlying sense; **Plain** may simplify terms, not premises.

**9.4 One‑way dependencies.**
Each rung on the ladder depends only **downwards**: a name at rung *n* can rely on names ratified at rungs ≤ *n*, never sideways or upwards. Cycles are prohibited. If a dependency is not yet ratified at the required rung, the new name remains Draft or Pilot.

**9.5 Local‑first before reuse.**
Teams MUST first **identify and stabilize the local sense** (within their Bounded Context). **Within the home**, reuse existing **Concept‑Set rows** where they fit (§4.2 **P1**). **Across contexts**, reuse occurs via **Alignment Bridges** that map the local sense to an existing sense elsewhere—without collapsing the local home.

**9.6 Sense, not string.**
Publication concerns **sense** (intended meaning in context), not the literal string. Synonyms are allowed as **Plain** labels or **aliases** only if they point to the same **Row ID** and pass the conformance checks in §15 (“CC‑F18”). Strings must not be treated as identity.

**9.7 Relation-kind discipline (structural vs epistemic).**
If the public name surfaces a **structural relation**, its intended sense **MUST** be backed by *exactly one Constructive trace* in the structural calculus (Compose-CAL) and **SHALL** declare `validationMode=axiomatic` (see E.14). If the name surfaces an **epistemic relation**, Constructive backing is optional; **declare** `validationMode ∈ {inferential, postulate}` and use **Logical/Mapping** and/or **Empirical Validation** as appropriate. **Do not mix relation kinds** inside a single name. *(Do not use “Tier-1/2”; formality is expressed via F per C.2.3.)*

**9.8 Member vs Component.**
Names that describe collection membership MUST NOT be used to imply part‑whole structure, and vice versa. If both aspects are needed, publish two names with their own MDS and an explicit bridge.

**9.9 Lifecycle states.**
A name travels through **Idea → Draft → Pilot → Ratified → Deprecated**. Transitions require explicit human review gates. Ratified names carry a clear stewardship contact and date.

**9.10 Anti‑duplication duty.**
Before ratification, the home MUST perform a **near‑neighbor review**: identify adjacent names, record the decision to align, merge, or keep separate, and publish the rationale in the name’s record.

**9.11 Local clarity over global neatness.**
When in doubt, prefer **local intelligibility** for practitioners over global symmetry. Global neatness can be achieved later via bridges; loss of local sense is hard to repair.

**9.12 No imported tool terms in Core names.**
Names and their MDS must not carry terms whose only meaning is tied to operating tools or pipelines. If such terms are unavoidable in pedagogy, confine them to Working-Names and examples with disclaimers.

**9.13 Human‑only conformance.**
Conformance for this protocol is judged by trained human reviewers using the author/reviewer checklists in §14 and the conformance criteria in §15 (“CC‑F18”). Automated heuristics, if any exist in an organization, have no standing in the Core.

### 10. Rationale (why this exists and why these rules)

**10.1 Local‑first unlocks velocity without lexical debt.**
Centralized naming regimes seem tidy but slow learning and create brittle compromises. Local‑first minting lets teams speak clearly **now**; unification comes from disciplined bridges and one‑way dependencies, not from premature centralization.

**10.2 One home lowers ambiguity.**
Names with “many owners” drift. A **single home** concentrates accountability for sense, examples, and lifecycle, while still enabling broad reuse via alignment bridges.

**10.3 Unified Tech + Plain serve two audiences.**
Engineers need **precise** wording; managers and stakeholders need **approachable** wording. Splitting the surfaces keeps the same sense while protecting accuracy and pedagogy; both are anchored by the **Row ID**.

**10.4 One‑way ladder prevents conceptual knots.**
Acyclic dependencies cut off circular definitions and policy deadlocks. The ladder provides a simple mental model: *build on what is already firm*.

**10.5 Relation-kind discipline prevents category errors.**
Part-whole claims **(structural)** must rest on **Constructive** grounds (`tv:groundedBy → Γₘ.sum|set|slice`, `validationMode=axiomatic`). Experience-based or evaluative relations **(epistemic)** follow assurance rules (**Logical/Mapping**, and **Empirical Validation** when *postulate*), with an explicit `validationMode ∈ {inferential, postulate}`. Mixing relation kinds inside a single name confuses review and invites hidden assumptions. 

**10.6 Sense over string reduces false conflicts.**
Disputes often orbit the string (“we hate that word”). By separating **sense** (what we mean) from **string** (how we say it), the protocol enables peaceful coexistence: keep the **Row ID** constant; use one **Plain** label and, where helpful, a budgeted **alias** per register.


### 11. Application Guidance (how to apply, step by step)

**11.1 Prepare (30–60 min).**

* Clarify **your Bounded Context** and audience.
* Collect 2–3 typical user stories that require the name.
* Scan near‑neighbors in adjacent contexts (see §14.2 Reviewer checklist).

**11.2 Mint locally.**

* Write the **MDS** in plain language, one paragraph.
* Draft a **Didactic Subtitle** (≤ 12 words): “what this name buys you.”
* Decide whether the intended **relation kind** is **structural** or **epistemic** (do not mix), and declare `validationMode`.

**11.3 Choose surfaces.**

* **Unified Tech label**: concise, morphology‑stable, neutral; avoid metaphor.
* **Plain label**: approachable phrasing for non‑specialists.
* **How to choose**: pick both **from a small NQD‑frontier** (see §4.2 P1 (candidate set), P2(read-through)): diversify by tradition, novelty/familiarity, and lexical form; record discarded contenders and rationale on the Card.

**11.4 Place on the ladder.**

* Verify all dependencies are at the same rung or below.
* If a dependency is still Draft/Pilot, keep this name at most Pilot.

**11.5 Align, don’t erase.**

* Where overlap exists with another context, propose an **alignment bridge**.
* Keep your home; record the mapping and any known divergence in reading.

**11.6 Publish and steward.**

* Publish the name with MDS, subtitle, rung, home contact, examples.
* Schedule a **first refresh**: when should the home examine usage and drift?

**11.7 Deprecate gracefully.**

* If the sense is superseded, publish **Deprecation Notes**: what to use instead, and why. Keep old Working-Names visible long enough to allow safe migration.

**11.8 The “Friday test.”**

* On a busy Friday, could a competent colleague apply the name correctly using only the MDS, subtitle, and two examples? If not, refine before ratification: it too overloaded with meanings to be helpful.

### 12. Examples (worked mini‑cases for engineer‑managers)

> These examples are deliberately simple. They show how local‑first minting, one‑way unification, and tier discipline operate together.

**12.1 “Module” vs “Component” (engineering structure).**

* *Home A (Platform)* mints **Component** with MDS: “A physically or logically integrated part whose removal would alter the integrity of the whole.” **Structural**.
* *Home B (App Team)* mints **Module** with MDS: “A deployable bundle of functionality maintained as a unit.” **Epistemic** (usage practice), not a structural claim.
* **Unification:** An alignment bridge states: “In Platform, every Component may host one or more Modules; Modules are not Parts.” Dependencies are one‑way: *Module* depends on *Component*; *Component* does not depend on *Module*. No synonymy asserted. Both names remain in their homes.

**12.2 “Incident” vs “Event” (operational sense).**

* *Home C (Operations)* mints **Incident** with MDS: “An unplanned interruption or reduction in the quality of a service.” **Epistemic**.
* *Home D (Monitoring)* mints **Event** with MDS: “A recorded observation of a state change in a system.” **Epistemic**.
* **Unification:** Bridge notes: “Some Events are Incidents when they degrade service; not all Events are Incidents.” **Plain** labels (and at most one alias per register) may vary (e.g., “Outage” as an alias for **Incident**), but the **Row IDs** stay distinct. No part‑whole claims are implied.

**12.3 “Customer” vs “Account Holder” (business roles).**

* *Home E (Sales)* mints **Customer**: “A party that receives value from an offering in exchange for consideration.” **Epistemic**.
* *Home F (Finance)* mints **Account Holder**: “A party legally responsible for an account.” **Epistemic**.
* **Unification:** Bridge states overlaps and divergence: “A Customer can be an Account Holder; an Account Holder may not be a Customer (e.g., trustee).” The homes retain stewardship; a shared Working-Name “Client” may be used in executive materials with a clear note: **Working-Name only; see Concept-IDs for decisions**.

**12.4 “Batch” vs “Lot” (collection vs integration).**

* *Home G (Manufacturing)* mints **Batch**: “A collection of items produced under shared conditions.” **Epistemic membership**.
* *Home H (Quality)* mints **Lot**: “An integrated whole packaged and tracked as one item.” **Structural whole**.
* **Unification:** Bridge notes: “A **Lot** may originate from a single **Batch** or a slice of a Batch; not every Batch yields a single Lot.” Relation mapping: **MemberOf** (Batch membership) vs **ComponentOf**/**Whole** (Lot integration). *Loss note:* membership evidence does **not** imply part‑whole structure; part‑whole structure does **not** imply shared production conditions.

### 13. Anti‑Patterns & Failure Modes (what to avoid)

**13.1 “Global name first.”**
Trying to coin a single global string before local understanding is mature. **Fix:** mint locally, publish MDS, then align.

**13.2 “Synonym storm.”**
Collecting many strings without stabilizing the Concept-ID. **Fix:** one Concept-ID per sense; multiple Working-Names only if they truly help didactics.

**13.3 “Process leakage into names.”**
Burying workflow or tool steps inside the MDS. **Fix:** keep process in method descriptions; keep names about sense, not procedure.

**13.4 “Member‑implies‑part.”**
Letting collection names induce part‑whole claims. **Fix:** separate names, separate MDS; don’t smuggle structure into membership.

**13.5 “Sideways dependency.”**
Defining a name by appealing to another Draft at the same rung or higher. **Fix:** depend only downward or postpone ratification.

**13.6 “Alias/Plain drift.”**
Letting a Plain label or alias accumulate extra meanings absent in the underlying row. **Fix:** periodic label review; prune metaphors that start bending sense; respect the alias budget.

### 14. Assurance & Conformance (human‑only checks)

**14.1 Author checklist (before requesting review).**

* [ ] I identified the **home Bounded Context** and audience.
* [ ] I wrote a clear **MDS** (≤ 1 paragraph) and a **Didactic Subtitle** (≤ 12 words).
* [ ] I declared the **relation kind** (structural vs epistemic) and the **validationMode**; no mixing.
* [ ] If **structural**, I can point to **exactly one Constructive trace** that backs the structural claim.
* [ ] I surveyed near‑neighbors and recorded my decision to align, merge, or keep separate.
* [ ] I produced both **Unified Tech** and **Plain** labels (per E.10), with the same sense and pointing to the same **Row ID**.
* [ ] Dependencies point **only downward**; no sideways or upward pulls.
* [ ] I scheduled a **refresh date** and listed 2–3 usage examples.

**14.2 Reviewer checklist (at the gate).**

* [ ] One home is declared; stewardship contact is clear.
* [ ] The MDS is free from process jargon and implementation slang.
* [ ] The declared **relation kind** is justified; **structural** claims are constructively grounded; **epistemic** claims declare `validationMode` and evidential posture.
* [ ] Member vs Component is respected where relevant.
* [ ] Alignment bridges are proposed where overlap exists, with explicit reading of convergence/divergence.
* [ ] The ladder discipline holds: acyclic, downward‑only dependencies.
* [ ] The **Plain** label does not smuggle extra commitments; **Unified Tech** and **Plain** remain co‑referential and point to the same **Row ID**.
* [ ] Lifecycle state is accurate (Idea/Draft/Pilot/Ratified/Deprecated) and dated.

**14.3 Lightweight outcomes.**

* **Ratify** (meets all checks).
* **Pilot** (publish with explicit questions and a refresh date).
* **Revise** (return to author with targeted gaps).
* **Merge** (replace with an alignment to an existing name).
* **Deprecate** (publish successor guidance and sunset plan).
