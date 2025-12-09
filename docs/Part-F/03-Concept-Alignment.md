# **Part F — The Unification Suite (U‑Suite): Concept‑Sets, SenseCells & Contextual Role Assignment**


---

## 3 · Minimal Artefacts (conceptual, notationally neutral)

> These artefacts are **thought‑objects**; they specify **what must exist conceptually**, not how it is stored.

### 3.1 **Context Card** (for each `U.BoundedContext`)

A terse descriptor used in the **Context Map** (F.1):

* `id` (stable local handle) · `title` · `edition/year`
* `family` (discipline family; informal) · `scope gist`
* `timeStance?` (`design` / `run`, if inherent)
* `trip‑wires` (few lexical caveats that often mislead, e.g., “*process*≠thermo process”)

### 3.2 **SenseCell** (unit of local meaning, inside one context)

* `label.tech` / `label.plain` (two registers)
* `gloss` (minimal generality, Context‑true)
* `notes?` (warnings, edition shifts)
* **No** behaviour/deontics/equations (C‑6)

> **Where it comes from.** F.2 describes how SenseCells can be *derived* from local term evidence; F.0.1 only **requires** that local meaning be expressible as a SenseCell.

### 3.3 **Alignment Bridge** (between SenseCells from different Contexts)

* `left: SenseCell⟨·@A⟩`, `right: SenseCell⟨·@B⟩`
* `relation` (e.g., *equivalent‑under‑assumptions*, *overlaps*, *broader‑than*)
* `CL` (Congruence Level; feeds B.3 Trust & Assurance)
* `loss/fit` (explicit statement of what is lost or assumed)

---


---

## 11 · SCR/RSCR acceptance checks (conceptual)

> *These checks are **content‑oriented**; they validate that a manuscript/model respects Part F principles. No process/tool assumptions are implied.*

### 11.1 SCR — Static conformance

* **SCR‑F01 (Context‑qualified).** Every normative term is Context‑qualified (directly, or via a scoped header that unambiguously fixes the Context).
* **SCR‑F02 (Local cells).** Each SenseCell belongs to **exactly one** Context; no cell aggregates Cross‑context **senses**.
* **SCR‑F03 (senseFamily hygiene).** SenseCell glosses contain no behaviours/deontics/equations; those appear only in their architheories.
* **SCR‑F04 (Bridges explicit).** Every Cross‑context relation appears as a Bridge with `relation` and `CL` and a short **loss/fit** note.
* **SCR‑F05 (No string identity).** There is no use of string equality to stand in for Cross‑context identity.
* **SCR‑F06 (Time stance fidelity).** Where a Context fixes `design/run`, the SenseCells and any Bridges reflect that stance explicitly.
* **SCR‑F07 (Row viability).** Any Concept‑Set row shown is supported by a connected subgraph of Bridges with **CL ≥ threshold** and no contradictions.

### 11.2 RSCR — Regression & evolution

* **RSCR‑F01 (Edition split).** When a source edition changes materially, SenseCells tied to the old edition remain; new cells bind to the new Context; Bridges are re‑assessed.
* **RSCR‑F02 (Bridge stability).** If any Bridge endpoint changes gloss/stance, downgrade or retire the Bridge, documenting the **loss/fit** change.
* **RSCR‑F03 (Composition guard).** When composing Bridges in a chain, the resulting `CL` never exceeds the minimal link; relation weakens monotonically.
* **RSCR‑F04 (Heterogeneity + QD guard):** requires ≥3 domain‑families AND MinInterFamilyDistance ≥ δ_family (per the active F1‑Card edition), with QD‑triad evidence (publish Diversity_P and IlluminationSummary on the declared grid/kernel). Near‑alias pairs (per dSig rule) SHALL be flagged and excluded or merged before the guard is evaluated. Record the F1‑Card edition id.

### 11.3 Publish‑ready summary

An artefact is **ready** with respect to F.0.1 when:

1. **SCR‑F01…F07** hold for all terms, cells, rows, and bridges it presents;
2. **RSCR‑F01…F04** hold under simulated edition/stance changes;
3. Every Cross‑context statement can be read as a **Bridge** or as a composition of Bridges with stated attenuation.

---


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

## 7 · What to record (conceptual, not clerical)

**7.1 The two‑minute memory.**
Everything you need to *think correctly later* fits on an eight‑line card. No registries, no workflows, no storage choices.

**7.2 The Context Card (one‑screen sketch).**
*(Each bullet is a thought, not a field.)*

* **Name & edition.** *“BPMN 2.0 (2011)”* • *“W3C PROV‑O (2013)”* • *“ITIL 4 (2020)”*.
* **Domain family.** *workflow* / *provenance* / *services* / *deontics* / *sensing* / *types* / *control* … *(informative only; never used to infer meaning).*
* **Scope gist** *(didactic; ≠ `USM.ScopeSlice(G)`)*. One line that marks the **inside/outside** (“workflow **graphs & participants**”, “provenance **entities/activities/agents**”).
* **Time stance** *(if inherent)*. Does the canon speak **design** (specifications, models) or **run** (occurrences, acts)?
* **Lexical trip‑wires.** Known homonyms or false friends in this Context (*“process ≠ thermodynamic process”*, *“role (RBAC) ≠ behavioural role”*).
* **Neighbour Contexts** *(informative)*. Close cousins that people often conflate (*BPMN ↔ PROV‑O*, *ITIL ↔ ODRL*).
* **Recency note.** *Current* / *superseded* / *candidate* (only as a reminder to yourself which text you mean).
* **Why this Context matters here.** One sentence linking to your unification line (“we will name Executions later; PROV‑O keeps them run‑time”).
* **Diversity signature (dSig).** A 5‑characteristics discrete signature for `U.BoundedContext`: **[Sector, Function, Archetype, Regime, MetricFamily]**. Authors SHOULD pick from local discipline taxonomies. **Publish a `dSigSource` list (five refs/URIs, one per axis) on every Card**, falling back to free‑text only where no canonical term exists. Two Contexts are flagged as **Near‑Duplicate** when ≥3 characteristics match. Publish `dSig` and `dSigSource` on every Card.

> *If your Card spills beyond a screen, you are collecting facts, not fixing meaning.*

F1‑Card (normative artefact): { taxonomyRef, embeddingRef, DistanceDef, δ_family, confidenceBand, calibrationSet, edition, subFamilyDef? }. subFamilyDef (optional): declares the stable partitioning below a domain‑family (e.g., taxonomic sub‑fields or CVT clusters with parent family anchors).  When HET‑FIRST quotas refer to “sub‑family”, they MUST use this declared subFamilyDef.
Declare **DomainDistance** policy (cosine or transport) and δ_family threshold; version as part of DescriptorMapRef. Publish `confidenceBand` (e.g., CI90%) for the calibrated `δ_family`; treat numbers in examples as illustrative, not normative.


---

## 15 · Migration notes (conceptual)

1. **New edition appears.** Keep the old Card; add a new Card with the new edition. If the sense shifts, treat it as a **new Context**; if it is strictly editorial, mark recency but keep one context.
2. **New family emerges.** If a missing family explains recurrent confusion in your line, admit it with **one exemplar** Context; remove a less informative Context to keep parsimony.
3. **Language variants.** Treat language editions as **separate Contexts** unless the canon itself declares a single normative bilingual mapping.
4. **Trip‑wire growth.** When you notice a recurring confusion, add a crisp trip‑wire to the relevant Card (one line; no essays).
5. **Bridges discovered later.** Do not back‑port bridges into F.1; leave the Cards untouched and record the mapping in **F.9**.
6. **Dormant Contexts.** If a Context no longer contributes to any active line, move it to a *parking shelf* (informative note on the Card) rather than deleting it.

---


---

## 16 · Acceptance tests (SCR/RSCR — concept‑level)

### 16.1 Static conformance checks (SCR)

* **SCR‑F1‑S01 (Heterogeneity).** For each unification line, the set of Cards spans **≥ 3 distinct domain families**.
* **SCR‑F1‑S02 (One‑screen Cards).** Each Card fits on one screen: name+edition; family; scope gist; time stance (if inherent); 1–3 trip‑wires; neighbour Contexts (optional); recency note.
* **SCR‑F1‑S03 (Locality pledge).** Nowhere in F.1 are Cross‑context equivalences or merges asserted.
* **SCR‑F1‑S04 (Parsimony).** In every family, **1–3** Contexts are kept; if more, a clear sentence justifies each extra Context’s unique sense contribution.
* **SCR‑F1‑S05 (Context discipline).** “Context” is used only as a synonym of **U.BoundedContext**; “domain” appears only as an informative family label.
* **SCR‑F1‑S06 (Temporal honesty).** If a canon fixes DesignRunTag, the Card states it.
* **SCR‑F1‑S07 (Family neutrality).** No claim, classification, or relation in F.1 relies on Domain‑family membership; families appear only as shelf labels on cards.
* **SCR‑F1‑S08 (dSig present).** Every Context Card has a 5‑characteristics `dSig`.
* **SCR‑F1‑S09 (Collision policy).** Any pair with `dSig` match on ≥3 characteristics is either merged or replaced; SCR records the action.

### 16.2 Regression checks (RSCR)

* **RSCR‑F1‑E01 (Edition churn).** When a new edition is added, prior Cards remain; no silent replacement.
* **RSCR‑F1‑E02 (Family balance).** Adding/removing Cards does not drop any line below **three families**.
* **RSCR‑F1‑E03 (Trip‑wire coverage).** After introducing a new Context, the trip‑wire lists of neighbouring Contexts are reconsidered and updated if needed.
* **RSCR‑F1‑E04 (No creep).** Periodically apply the **memory rule**: if the cut no longer fits in working memory, shrink it.

---


---

## 14 · Migration notes (conceptual)

1. **New edition appears.** Add a Context in F.1; harvest afresh in F.2 using that Context; do not overwrite earlier units.
2. **Idiomatic update discovered.** If your LNF fought the canon’s idiom, **re‑LNF** within the same context; keep labels/glosses steady unless the canon itself differs.
3. **Ambiguity inside a Context.** If use splits, **mint two units** with distinct glosses; F.3 will sort their relation (same/different Local‑Sense).
4. **Language split.** Treat each language canon as its **own Context**; resist cross‑language merges in F.2.
5. **Tail pruning.** If units accumulate without feeding F.3/F.4/F.9, drop them from the working set; keep head terms that carry bridges.
6. **DSL quarantine.** If a tool dialect is unavoidable, keep it as one context among others; never let it define the idiom for other Contexts.

---


---

## 15 · Acceptance tests (SCR/RSCR — concept‑level)

### 15.1 Static conformance (SCR)

* **SCR‑F2‑S01 (context‑locality).** Every unit cites a Context from F.1.
* **SCR‑F2‑S02 (Idiomatic LNF).** Each LNF reflects the Context’s spelling/hyphenation/casing with **minimal edits**.
* **SCR‑F2‑S03 (Two registers).** Each unit carries both **Tech** and **Plain** labels; if not, a reason exists tied to didactics.
* **SCR‑F2‑S04 (Lexical‑only).** No gloss contains behaviour, deontics, measurement math, or type axioms.
* **SCR‑F2‑S05 (No Cross‑context claims).** Nowhere does F.2 assert equivalence/similarity/subsumption across Contexts.
* **SCR‑F2‑S06 (Minimal generality).** Glosses match the Context’s use; no globalisation.
* **SCR‑F2‑S07 (Temporal honesty).** For Contexts with fixed DesignRunTag, units and glosses respect it.

### 15.2 Regression (RSCR)

* **RSCR‑F2‑E01 (Edition split).** Introducing a new edition yields new units under a new Context; earlier units persist unchanged.
* **RSCR‑F2‑E02 (Normaliser stability).** Adjusting an LNF does not silently widen/narrow the gloss.
* **RSCR‑F2‑E03 (Language split).** Adding a second language yields a second Context; no bilingual collapse in F.2.
* **RSCR‑F2‑E04 (No stealth bridges).** After updates, F.2 still contains **zero** Cross‑context identity claims; any mapping appears only in F.9.
* **RSCR‑F2‑E05 (Head‑term focus).** Periodic check shows the unit set remains small and oriented to F.3/F.4/F.9 needs.

---


---

## 7 · Outputs (conceptual, not clerical)

F.3 yields, **per Context**:

1. A **small set of Local‑Senses**, each with:

   * **Label pair**: *Tech* (idiomatic) · *Plain* (didactic).
   * **Sense line**: one‑sentence usage statement, in the Context’s voice.
   * **Inside list** (informative): which Units from F.2 it consolidates.
   * **Counter‑example** (optional but powerful): a short use that must **not** be included.
1. A **SenseCell address** for each Local‑Sense: *(Context, Local‑Sense)*.

These are **thinking reference points** (cognitive only), not records or files. Later patterns **cite SenseCells by name**; nothing about storage is implied.

---


---

## 15 · Migration notes (conceptual)

1. **Usage clarifies → merge.** If two Local‑Senses never lead to different conclusions in the Context’s canon, **merge** and keep the narrower sense line.
2. **Usage diverges → split.** If new reading reveals incompatible roles/entailments, **split** and attach a counter‑example to each side.
3. **Edition change → new Context.** When a new edition **reframes** usage, treat it as a **separate Context** (F.1) and re‑cluster there.
4. **Label upkeep.** If the Plain label tempts broadening, tighten it; if the Tech label drifts from idiom, restore the canon term.
5. **Dormant sense.** If a Local‑Sense ceases to matter for any active line, leave it listed but mark it **low‑use** in your own notes; do not fold it into another unless rule 1 holds.
6. **Bridge temptation.** Record tensions to bridge **elsewhere**; F.3 never resolves Cross‑context relations.

---


---

## 16 · Acceptance tests (SCR/RSCR — concept‑level)

### 16.1 Static conformance (SCR)

* **SCR‑F3‑S01 (context‑locality).** Every Local‑Sense is paired with **exactly one context**; no Cross‑context clustering appears.
* **SCR‑F3‑S02 (Label pair).** Each Local‑Sense has **Tech** (idiomatic) and **Plain** (didactic) labels; neither widens usage beyond the sense line.
* **SCR‑F3‑S03 (Sense line fidelity).** Each sense line is **grounded in canonical statements** of the Context; no behaviour/deontic/math content.
* **SCR‑F3‑S04 (Parsimony).** The set of Local‑Senses per Context is small enough to **recall unaided** by a careful mind.
* **SCR‑F3‑S05 (Counter‑example presence).** For any ambiguous head, at least one **counter‑example** is recorded to guard the boundary.
* **SCR‑F3‑S06 (Temporal honesty).** Where the Context has a declared stance, sense lines **respect design/run**.

### 16.2 Regression (RSCR)

* **RSCR‑F3‑E01 (Merge soundness).** Every merge is justified by a **failed distinction test** (no selectional or entailment difference).
* **RSCR‑F3‑E02 (Split necessity).** Every split cites a **role/entailment conflict** or a concrete **counter‑example**.
* **RSCR‑F3‑E03 (Edition guard).** No Local‑Sense spans Contexts that differ by edition **with usage shift**.
* **RSCR‑F3‑E04 (Label stability).** Changes to labels do **not** change sense; if they do, the change is treated as a split/merge per E01/E02.
* **RSCR‑F3‑E05 (Downstream continuity).** After splits/merges, **SenseCell** references in F.4/F.7/F.9 remain **referentially clear** (new addresses are explicit; no silent aliasing).

---


---

## 13 · Migration notes (conceptual)

1. **When a Context changes edition.** Names stay; the **SenseCell** shifts to the new edition. Only change a label if the **sense** has changed; then **split** the card rather than mutate the name. (INV‑F5‑2, R‑RD‑7)

2. **When a Concept‑Set row gains a new witness Context.** Re‑ask neutrality: if the Tech label now privileges a Context, **refactor to a more neutral head** (e.g., `Observation` → `Result`). (R‑UT‑1, R‑UT‑2)

3. **Collision emergence.** If a **Role card** and a **Status card** converge phonetically (`Approver` vs `Approved`), keep both but add the **minimal morphological disambiguator** only where the Context idiom demands it (`Reviewer Role`). (R-RD-3)

4. **Family hygiene.** As families grow, keep **parallel shapes** (`… Level`, `… Status`). If a legacy label breaks shape, add a **Plain alias** for teaching; don’t rename the Tech label without Concept‑Set pressure. (R‑UT‑7, R‑UT‑6)

5. **Language variants.** Non-English canons keep **their own Tech labels** (idiomatic in that Context); the **Plain** label remains English in FPF unless the Part mandates localisation. (R-RD-4, INV-F5-1)

6. **Symbol addition.** You may add a **symbolic alias** later for readers of formal sections; never promote a symbol to the Tech label. (R‑UT‑8)

7. **De‑jargonising the Plain label.** If readers stumble, adjust **Plain** wording only; do **not** widen the sense. (Plain‑safety check)

8. **Deprecation path.** If a label must change, publish the **new Tech + Plain**, keep the old as an **alias** in the registry (F.13), and leave the reasoning trail in the Concept‑Set row that forced the rename. (R‑UT‑6, F.13 linkage)


---

## 14 · Acceptance tests (SCR/RSCR — concept‑level)

### 14.1 Static conformance (SCR)

* **SCR-F5-S01 (Two registers).** Every Role Description card and U.Type **has both** Tech and Plain labels; any symbol is marked **alias**.
* **SCR-F5-S02 (Context fidelity for Role Descriptions).** For any Role Description `T` in Context `C`, `Tech(T)` appears idiomatic **in C**; `Plain(T)` does **not** broaden `sense(T)`.
* **SCR‑F5‑S03 (Neutrality for U.Types).** For any U.Type `U`, its Tech label does **not** coincide with a witness Context’s proprietary term when alternatives exist.
* **SCR‑F5‑S04 (senseFamily morphology).** Role labels are **countable nouns**; Status labels are **state nouns** / adjectival‑noun forms.
* **SCR-F5-S05 (Minimal generality).** For each label, there exists a reading where the **name’s scope ⊆ invariant scope** (Role Description) or **⊆ row intersection** (U.Type).
* **SCR‑F5‑S06 (No Context tags).** No label embeds Context or edition strings.
* **SCR‑F5‑S07 (Family coherence).** Families that claim parity (e.g., Levels) show **parallel shapes** across members.

### 14.2 Regression checks (RSCR)

* **RSCR‑F5‑E01 (Witness drift).** When a Concept‑Set row gains/removes a witness Context, re‑evaluate **neutrality**; if violated, refactor the Tech label to a more neutral head.
* **RSCR-F5-E02 (Edition churn).** When a Context updates, Role Description labels remain stable unless the **sense** changed; if sense changed, **split** the card and keep aliases in F.13.
* **RSCR‑F5‑E03 (Collision guard).** If two labels become confusable across **senseFamilies**, either add the **minimal** disambiguator (Role Description only, Context‑idiom) or separate the concepts.
* **RSCR‑F5‑E04 (Rhetoric creep).** Periodic skim for decorative adjectives; remove them unless they encode formal levels or families.


---

# F.7 — Concept‑Set Table \[A]

**“Show one thing across Contexts—only where explicit bridges allow it.”**

**Status.** Architectural pattern \[A], architheory‑agnostic.
**Depends on.** E.10.D1 **Lexical Discipline for ‘Context’** (Context ≡ `U.BoundedContext`); **F.0.1 senseFamily (normative)**; F.1 **Domain‑Family Landscape Survey**; F.2 **Term Harvesting**; F.3 **Intra‑Context Sense Clustering** (SenseCells); F.5 **Naming Discipline**; F.9 **Alignment & Bridge Across Contexts**.
**Coordinates with.** F.4 **Role Description**; F.6 **Role Assignment & Enactment Cycle (Six-Step)**; Part C architheories (for examples), **MM‑CHR (for Characteristic)**.
**Aliases (informative).** *Concept‑Set table*, *comparison grid*.

---


---

## 6 · The table (conceptual layout)

> One page. Fixed column order by Context. Each row fits in **five lines** max.

```
FPF Label (Tech / Plain) | Row Scope | Row CL(min) | [Context A] local label | [Context B] local label | [Context C] local label | Rationale | Counter‑examples
```

**Reading rules (didactic):**

1. **Cells are local.** A cell is **not** a translation; it is the Context’s **own** label for its SenseCell.
2. **Scope is king.** The FPF label only licenses sameness **within its Row Scope**. Outside that scope, treat cells as **different**.
3. **Row CL(min) governs trust.** Lower CL ⇒ narrower applicability; **never** up‑scope a row without revisiting Bridges.
4. **Rationale & counter‑examples** are **obligatory one‑liners**; if you need paragraphs, you need an F.9 walkthrough, not a row.

**Didactic name rationale** “Giants' table’” that alludes to *standing on the shoulders of giants*: each row explicitly leans on authoritative context of meaning (**U.BoundedContext**) established by prior disciplines and not imagined. It does **not** mean a physically large table; the name signals epistemic humility and traceable reliance on those sources. "We are like dwarfs on the shoulders of giants, so that we can see more than they, and things at a greater distance, not by virtue of any sharpness of sight on our part, or any physical distinction, but because we are carried high and raised up by their giant size." by Bernard of Chartres , d. c.1130, French philosopher.


---

## 7 · Conceptual construction (thought moves, not workflow)

> The table is derived from earlier patterns; it **creates nothing new**.

* **Sourcing.** Candidate cells come **only** from **SenseCells** (F.3).
* **Licensing.** A row exists **iff** the relevant **Bridges (F.9)** already justify sameness at the chosen **Row Scope**.
* **Bounding.** Prefer **2–4 Contexts** per row (parsimony); add more only if each adds a *distinct necessity* for the sameness claim.
* **Typing.** A row is **typed by senseFamily**: Role, Status, Type‑structure, Measurement, etc. **Do not mix senseFamilies** in one row.
* **Temporal honesty.** A row’s cells must share **compatible DesignRunTag**; if not, either split into two rows or mark a **contrast row**.

---


---

## 14 · Migration notes (conceptual)

1. **Bridge update.** If any supporting Bridge’s CL changes, recompute **Row CL(min)**. If it drops below the printed value, either **lower Row Scope**, **split** the row, or **retire** it.
2. **New Context appears.** Do **not** auto‑expand rows. Test with **12.5**; add only if it brings a **distinct necessity**.
3. **Sense revision inside a Context.** If a SenseCell splits (F.3), decide which child cell (if any) remains in the row; the rest may require **new rows** or a **contrast**.
4. **Scope promotion.** To use a row for a stronger purpose (e.g., from **Naming-only** to **assignment/enactment-eligibility**), first ensure **Row CL(min) ≥ τ(new scope)**; otherwise construct **new Bridges** or **decline** promotion.
5. **Deprecation.** If a row no longer meets its invariant, mark its FPF label as **retired** in F.5 and point to successor rows (if any).
6. **Edition churn.** When a Context is superseded (F.1), either keep the cell (if semantics stable) or treat the successor as a **new Context** and re‑evaluate licensability.

---


---

## 15 · Acceptance tests (SCR/RSCR — concept‑level)

### 15.1 Static conformance checks (SCR)

* **SCR‑F7‑S01 (Context‑loyal cells).** Every non‑empty cell references an existing **SenseCell** (F.3) in a declared Context (F.1).
* **SCR‑F7‑S02 (Closure & bottleneck).** For each Concept‑Set row, **every pair** of cells has a Bridge path with CL ≥ **Row CL(min)** printed; **Row CL(min)** equals the **minimum** pairwise CL.
* **SCR‑F7‑S03 (Typed & scoped).** Each row declares a **Row Scope** from the controlled set and is **senseFamily‑uniform** (Role **or** Status **or** Measurement **or** Type‑structure…).
* **SCR‑F7‑S04 (Temporal compatibility).** Non‑contrast rows have **compatible** DesignRunTag across cells.
* **SCR‑F7‑S05 (Loss disclosure).** If any supporting Bridge has a recorded loss, the row includes **≥1 counter‑example** line.
* **SCR‑F7‑S06 (Parsimony).** Rows contain **2–4 Contexts** unless a one‑line necessity is stated for each extra Context.

### 15.2 Regression checks (RSCR)

* **RSCR‑F7‑E01 (Bridge drift).** After any Bridge change (F.9), recompute **Row CL(min)**; flag rows whose scope is now overstated.
* **RSCR‑F7‑E02 (Sense split).** After a SenseCell splits (F.3), ensure rows referencing it either pick a child cell or retire.
* **RSCR‑F7‑E03 (Scope integrity).** No consumer pattern uses a row outside its declared **Row Scope**.
* **RSCR‑F7‑E04 (No stealth growth).** Additions of cells never lower **Row CL(min)** silently; if they do, either split the row or reduce scope.

---


---

# F.8 — Mint or Reuse? (U.Type vs Concept-Set vs Role Description vs Alias) \[A] 

**“Name only what thinking **requires**, and reuse everything else.”**

**Status.** Architectural pattern \[A], architheory‑agnostic.
**Depends on.** E.10.D1 **Lexical Discipline for “Context” (D.CTX)**; A.7 **Strict Distinction**; A.11 **Ontological Parsimony**; A.8 **Universal Core**.
**Coordinates with.** F.1 **Contexts (Contexts)**; F.2 **Harvest**; F.3 **SenseCells**; F.4 **Role Description**; F.5 **Naming Discipline**; F.7 **Concept‑Set Table**; F.9 **Alignment & Bridge**.
**Aliases (informative).** *Mint‑vs‑Reuse gate*; *Naming governor*.

---


---

## 5 · The decision lattice (conceptual, notation‑free)

> Read top‑to‑bottom; the **first satisfied** branch decides. At every step, **state the senseFamily** (Role / Status / Measurement / Type‑structure / Method / Execution) before you proceed.

### Q0 — What is the **senseFamily** of your need?

* If **uncertain**, return to F.1/F.3: stabilise the Context(s) and the local sense.
* If **mixed**, split the need: one decision **per senseFamily** (A.7).

### Q1 — Is there a **single Context** whose SenseCell already expresses it?

* **Yes →** **Reuse** the **SenseCell**’s label **inside that Context**.

  * If you need assignable behaviour or deontics on that sense: **define a Role Description** **anchored to that SenseCell** (F.4).
* **No →** go to Q2.

> *Example (engineer).* You want “**task execution**” in control software. In `IEC 61131‑3` there is a clear SenseCell for **task execution**. **Reuse** that label; if you need responsibilities (“who monitors runs”), define a **Role Description** anchored to this SenseCell.

### Q2 — Do you need to **read across Contexts** (same senseFamily)?

* **No →** stay within one context; if your desire is merely a nicer label, consider an **Alias** (Q3).
* **Yes →** check F.7 for a **Concept‑Set row** covering your cells **in this senseFamily** with adequate **Row Scope** and **Row CL(min)**.

  * **Found & sufficient →** **Reuse the row’s FPF label** at that scope.
  * **Not found or insufficient →** either (a) **publish a contrast** (teach difference), or (b) propose a **new row** but only after F.9 Bridges exist at **τ(scope)**.

> *Example (manager).* You want one label for the **actor** in workflow and provenance prose. F.7 has a **Naming‑only** row mapping *BPMN Participant* ↔ *PROV Agent* at CL = 2. **Reuse** “actor” **at Naming‑only** scope; do **not** infer identity in models.

### Q3 — Is this **only a wording preference** for an existing FPF label?

* **Yes →** add an **Alias** in F.5 (Tech register and/or Plain register), no semantics changed.
* **No →** go to Q4.

> *Example (researcher).* You prefer “**is‑a**” to “**subclass‑of**” in Type pages. That is an **Alias** for the same concept; no new row, no new U.Type.

### Q4 — Does your need recur across Contexts in a way **not captured** by current rows, **with Bridges** already available at the required CL?

* **Yes →** propose a **new Concept‑Set row** (F.7): small (2–4 Contexts), **one senseFamily**, declare **Row Scope** and **Row CL(min)**, include a **counter‑example** if any Bridge has loss notes.
* **No →** go to Q5.

> *Example (engineer).* You repeatedly compare **runtime occurrence** in PROV with **PLC task runs**. F.9 Bridges exist at CL = 2. Propose **row “execution-occurrence”** at **assignment/enactment-eligibility** scope (not Type-structure).

### Q5 — Are you describing a **kernel‑level notion** missing from the catalogue, **not** reducible to existing rows or Role Descriptions, and **present across ≥ 3 domain families** (A.8)?

* **Yes →** propose a **new U.Type** (rare). Supply:
  (i) the minimal **intensional definition**; (ii) cross‑family evidence (≥ 3 Contexts, **distinct families**); (iii) how it **doesn’t** duplicate an existing U.Type.
* **No →** you **do not mint** a new type. Re‑express the need in terms of **Context reuse**, **row reuse**, **Alias**, or a **Role Description**.

> *Example (researcher).* You think we need **U.InfluenceEdge** (causal tendency). If it appears as a stable, **senseFamily‑specific** notion across **control**, **epistemic inference**, and **methods** (≥ 3 families), and cannot be formed from existing `U.Relation` subtypes, it **may** qualify. Otherwise, treat it as a **pattern** or a **row**.

---


---

## 14 · Migration notes (conceptual)

1. **Old “anchor” language.** Replace legacy “anchor” with: **SenseCell** (local sense) + **Role Description** (assignable Standard) + (optionally) **Concept‑Set row** (Cross‑context reading).
2. **Over-strong rows.** If a row was used for **assignment/enactment-eligibility** or **Type-structure** but **CL drops**, **downgrade row scope** to **Naming-only** in prose; adjust examples.
3. **Split rows.** If one row covers cells whose Bridges diverge, **split** into two narrower rows with explicit loss notes.
4. **Alias proliferation.** Collapse redundant Aliases under a single F.5 entry; keep both registers (Tech/Plain).
5. **Proto‑types.** Suspect kernel inflation? Attempt **reduction**: SenseCell + row + existing U.Type. Only if irreducible across ≥ 3 families, reopen as a U.Type candidate.

---


---

## 15 · Acceptance tests (SCR/RSCR — concept‑level)

### 15.1 Static conformance (SCR)

* **SCR‑F8‑S01 (senseFamily purity).** Every decision record names **one senseFamily**; mixed needs are split.
* **SCR‑F8‑S02 (Proper anchoring).** Every Role Description cites **one SenseCell**; **no row** is used as a assignment/enactment anchor.
* **SCR‑F8‑S03 (Row scope).** Whenever a row is reused, its **Scope** is stated and **Row CL(min) ≥ τ(scope)** holds.
* **SCR‑F8‑S04 (Alias modesty).** Aliases introduced in F.5 do **not** claim new semantics or change senseFamily.
* **SCR‑F8‑S05 (Kernel restraint).** Any new U.Type proposal includes **≥ 3 domain families** of evidence and an **irreducibility** note.

### 15.2 Regression (RSCR)

* **RSCR‑F8‑E01 (CL drift).** If any Bridge’s CL changes, re‑evaluate dependent rows; **downgrade or split** where τ(scope) is no longer met.
* **RSCR-F8-E02 (Row overuse).** Scan examples: no case uses **Naming-only** rows to justify **Assignment-eligibility** or **Type-structure** claims.
* **RSCR‑F8‑E03 (Alias creep).** Ensure no Alias has accreted senseFamily‑specific semantics; if it has, migrate to a **row** or **Role Description**.
* **RSCR‑F8‑E04 (Kernel hygiene).** New U.Type proposals are rejected if a **SenseCell + row** construction suffices.

---


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

## 8 · The Bridge Card (one‑screen sketch)

> A **thought‑format** (not a form). Every bullet can be said in a sentence.

* **Cells.** `σA@contextA` ↔ `σB@contextB`.
* **senseFamily.** *Role / Status / Measurement / Type‑structure / Method / Execution …*
* **Kind.** *≈ / ⊑ / ⊒ / ⋂ / ⊥ / ⇄ᴅʀ / →ᴍᴇᵃ / →ᴅᵉᵒ*.
* **Direction.** *A→B* (if non‑symmetric) or *A↔B*.
* **CL.** *0–3* with a short **why**.
* **Loss Notes (bullets).** What fails to carry (units, scope, granularity, preconditions, time stance).
* **Counter‑example.** The crispest case where substitution would mislead.
* **Allowed use.** *Naming-only / Role Assignment & Enactment-eligible / Type-structure / Explanation-only*.
* **Didactic hook.** The helpful sentence a careful engineer can remember.

*If your Bridge Card doesn’t fit on a screen, you’re describing the Contexts, not the Bridge.*

---


---

## 15 · Migration notes (conceptual)

1. **Edition shift in a Context.** Re‑read affected **Cells**; if sense moved, split the Bridge or **lower CL**; keep the older Bridge for historical claims.
2. **New evidence of mismatch.** Add a **counter‑example**; **decrease CL** or change **kind** (e.g., from ≈ to ⊑ or ⋂).
3. **Convergence over time.** When invariants demonstrably match, and counter‑examples evaporate, **raise CL** cautiously; for **CL=3**, cite invariants.
4. **senseFamily refactor.** If a Cell’s senseFamily was mis‑typed, fix the senseFamily first in F.3, then revisit Bridges; **Interpretation** is safer than forced substitution.
5. **Row under‑protected.** If a row’s scope exceeds the weakest Bridge, either **split the row** by Context or **downgrade scope** to Naming‑only.
6. **Bridge sprawl.** Consolidate near‑duplicates into one Bridge with richer **Loss Notes**; retire the rest.

---


---

## 16 · Acceptance tests (SCR/RSCR — concept‑level)

### 16.1 Static conformance (SCR)

* **SCR‑F9‑S01 (Well‑typed).** Every Bridge names **two SenseCells**, each bound to a **Context** from F.1, and states **senseFamily**, **kind**, **dir** (if needed), **CL**, **Loss**, **scope**.
* **SCR‑F9‑S02 (senseFamily discipline).** Any Bridge that licenses **Role/Enactment-eligible** substitution is **senseFamily‑preserving** and **kind ∈ {≈,⊑,⊒}**.
* **SCR‑F9‑S03 (Loss visibility).** Every Bridge has **non‑empty Loss Notes** (the word “none” is allowed only with **CL=3** and stated invariants).
* **SCR‑F9‑S04 (Counter‑example hygiene).** Bridges with **CL≤2** carry at least one **counter‑example**; Bridges with **CL=3** cite **matching invariants**.
* **SCR‑F9‑S05 (Row compliance).** Every Concept‑Set row shows a **scope** no greater than the **minimum CL** across its supporting Bridges; no row relies on **Interpretation** Bridges.

### 16.2 Regression (RSCR)

* **RSCR‑F9‑E01 (Edition churn).** When a Context’s edition changes, re‑validate all Bridges touching it; **flag CL drift** and update rows’ scopes if needed.
* **RSCR‑F9‑E02 (Counter‑example drift).** New counter‑examples lower **CL**; deletions do not automatically raise **CL**.
* **RSCR‑F9‑E03 (senseFamily drift).** If a Cell’s senseFamily is corrected, all Bridges crossing that Cell are re‑typed; any substitution that would now cross senseFamilies is **invalidated**.
* **RSCR‑F9‑E04 (Weakest‑link enforcement).** Adding a low‑CL Bridge to a row **reduces** the row’s scope; if the row’s published scope would exceed the new minimum, **split** or **downgrade** the row.

---


---

## 7 · Solution — how meanings connect (conceptual, notation‑free)

**S‑1. Anchor status meanings per Context.**
Every status word (*validated*, *approved*, *compliant*) is treated as a **StatusCell** inside a specific Context. The **ladder position** is determined **locally** (e.g., “validated (metrology)” aligns to **Replicated** with CL stated; “validated (software)” may align to **Corroborated**).

**S‑2. Attach statuses to the right Targets.**
*EvidenceStatus → Claim or Quantity; StandardStatus → Method/Artefact; RequirementStatus → Clause.*
This prevents swapping “how we measure” with “what we promise”.

**S‑3. Translate via Bridges, not by name.**
Example: **Measured availability (SOSA)** →ᴍᴇᵃ **SLO clause (ITIL)** with **CL=2**, Loss: sampling window & clock skew. This supports **explanation**; **substitution** (“Satisfied”) requires **same StatusModality**, a stricter Bridge kind (F.9) **and** a declared evaluation rule (from the Service pattern), not from F.10.

**S‑4. Keep design/run honest.**
**StandardStatus** is design‑stance; **EvidenceStatus** is run‑signal; **RequirementStatus** spans both. Use **Interpretation Bridges** (F.9) for design↔run readings, not equivalence.

**S‑5. Prefer explanation over substitution.**
If a Bridge cannot reach **CL≥2** on the **same senseFamily**, do **not** substitute. Use **Naming‑only** rows or **explanations**; keep Role Descriptions (F.4) out of harm’s way.

---


---

## 14 · Migration notes (conceptual)

1. **New status word appears.** Treat it as a **StatusCell** in its Context; place it on the local ladder; only then consider Bridges.
2. **Edition changes.** If a Context redefines a status, **fork the StatusCell** (new SenseCell) and relate old↔new via a **Bridge** (often ⊑/⊒ with Loss).
3. **Threshold tuning.** The project sets **θ** (minimum CL for substitution). Lowering θ widens reuse but increases risk; document the choice in F.7 terms.
4. **Clause redesign.** If a requirement clause changes, keep old **Windows** intact; new clause starts a new Target; do **not** rewrite history.
5. **Explode→compress.** When many bespoke tool statuses pile up, **map** them to the nearest ladder level in their Contexts; keep tool labels as **Naming‑only**.
6. **Bridge hardening.** If explanation Bridges are used frequently, reconsider experiments that could raise **CL** enough to permit substitution—or accept explanation as sufficient and stop short of substitution.

---


---

## 15 · Acceptance tests (SCR/RSCR — concept‑level)

### 15.1 Static conformance (SCR)

* **SCR‑F10‑S01 (Modality & Target).** Every StatusCell declares **StatusModality** and **target kind**; none cross modalities.
* **SCR‑F10‑S02 (Windowed polarity).** Every positive/negative StatusCell instance bears a **Window**.
* **SCR‑F10‑S03 (Local order).** EvidenceStatus instances satisfy **monotonicity**; RequirementStatus enforces **mutual exclusivity** per clause+Window.
* **SCR‑F10‑S04 (Bridge citation).** Any Cross‑context comparison cites a **Bridge(kind, CL, Loss)**; absent that, mark as **naming‑only**.
* **SCR‑F10‑S05 (Substitution guard).** Any substitution claim checks **same StatusModality**, **kind ∈ {≈,⊑,⊒}**, **CL≥θ**, **Windows aligned**.
* **SCR‑F10‑S06 (Weakest‑link).** Where multiple Bridges feed one conclusion, the displayed **effective CL** is the **minimum**.

### 15.2 Regression (RSCR)

* **RSCR‑F10‑E01 (Edition churn).** Adding a new edition of a Context **does not** retro‑change past status conclusions; only new Windows see new meanings.
* **RSCR‑F10‑E02 (Threshold change).** If θ changes, re‑evaluate only **substitution** conclusions; **explanations** remain valid.
* **RSCR‑F10‑E03 (Bridge drift).** When a Bridge’s CL/Loss changes, recompute affected **effective CL**; substitution conclusions below θ revert to **explanation**.
* **RSCR‑F10‑E04 (Contradiction catch).** Adding a negative status within a Window **cancels** prior positives for the same clause (or raises a flagged contradiction if both persist).

---


---

## 14 · Migration notes (conceptual)

1. **Split conflated “process”.** Where a single “process” node stands for both plan and run, refactor into **MethodDescription** (design) and **Work** (run); add a Bridge if the prose relied on identity.
2. **Re‑home statuses.** Move any *Approval*‑like statuses from Work to MethodDescription; move *Satisfied/Violated* from Spec to clauses about Work within **Windows**.
3. **Expose actuation.** If control outputs are buried in “execution logs,” mint **Actuation** SenseCells and relate them **within** Work.
4. **Version fences.** Past Works keep references to the **version** of MethodDescription they attempted to follow; don’t update those links retroactively.
5. **Name collisions.** Where *task/activity/process* appear with mixed meanings, prefix with Contexts and relabel per **F.5** (Tech/Plain).
6. **Backfill Bridges.** If earlier text implied Cross‑context equivalence, add explicit Bridges (F.7/F.9) declaring **kind/CL/Loss**.

---


---

## 15 · Acceptance tests (SCR/RSCR — concept level)

### 15.1 Static conformance checks (SCR)

* **SCR‑F11‑S01 (DesignRunTag honesty).** Every normative claim about outcomes is attached to **Work** (with Window), not to **Method/MethodDescription**.
* **SCR‑F11‑S02 (Box placement).** Labels and statuses appear on the correct box (e.g., *Approved* on MethodDescription only).
* **SCR‑F11‑S03 (Actuation inclusion).** All Actuation statements are modeled as **within** a Work interval.
* **SCR‑F11‑S04 (Context discipline).** Each quartet term is expressed as a **SenseCell** with its Context; no Cross‑context identity is asserted here.
* **SCR‑F11‑S05 (Bridge guard).** Any Cross‑context reasoning among quartet terms references an explicit **Bridge** with **kind/CL/Loss**.

### 15.2 Regression checks (RSCR)

* **RSCR‑F11‑E01 (Spec update).** When a MethodDescription changes, previous Works remain valid and unchanged; their statuses don’t shift unless re‑evaluated with explicit rationale.
* **RSCR‑F11‑E02 (Bridge drift).** If a Context updates, revisit Bridges that touch quartet terms; adjust **CL/Loss** only via F.7/F.9.
* **RSCR‑F11‑E03 (Status drift).** Adding new statuses does not move them across boxes (e.g., no new “Work‑Approved”).
* **RSCR‑F11‑E04 (Signal creep).** Introducing new Actuation details does not erase or replace Work context.

---


---

## 7 · Clause templates (conceptual schemata)

> These are **shapes of meaning**, not data fields.

1. **Availability (share‑of‑time)**

* **ClauseCell:** *service availability ≥ 99.9% monthly* (services Context).
* **MeasureCell:** *uptime indicator* over **Work** (KD‑CAL).
* **Predicate:** `good_time/total_time ≥ 0.999`.
* **Window:** calendar month.
* **Bridge:** from monitor semantics → consumer‑perceived availability (**kind:** proxy; **CL:** 2; **Loss:** blind to partial degradations).

2. **Latency (percentile)**

* **ClauseCell:** *p95 latency ≤ 120 ms during incidents* (services Context).
* **MeasureCell:** *response time observation* for the same **Work episode** (KD‑CAL).
* **Predicate:** `P95(latency) ≤ 120ms`.
* **Window:** incident interval.
* **Bridge:** from request‑level telemetry → service‑level promise (**kind:** aggregation; **CL:** 2; **Loss:** sampling bias).

3. **Safety margin (band)**

* **ClauseCell:** *temperature ∈ \[L,U] during batch* (deontics/quality Context).
* **MeasureCell:** *process temperature observation* (KD‑CAL).
* **Predicate:** `min ≥ L ∧ max ≤ U`.
* **Window:** batch run interval (Work).
* **Bridge:** not needed if Measure and Clause are in the same Context; otherwise declare.

4. **MTTR (count‑within‑limit + duration)**

* **ClauseCell:** *MTTR ≤ 60 min per incident*.
* **MeasureCell:** *timestamps of Work phases* (start fix → restore).
* **Predicate:** `restore_time − start_fix ≤ 60 min`.
* **Window:** each incident’s **Work** interval.
* **Bridge:** BPMN design steps → PROV Work **Interpretation** (CL=2; **Loss:** gateways ≠ real branching).

---


---

## 14 · Migration notes (conceptual)

1. **Clause revisions.** Introduce a **new ClauseCell**; keep old verdicts intact (Non‑retroactivity).
2. **Monitor changes.** Update or replace **Bridges** (kind/CL/Loss). Future verdicts use the new Bridge; past ones are annotated, not rewritten.
3. **Scope corrections.** If evidence was about the wrong **Work**, retire the verdict and restate the quadruple; do **not** patch by redefining the Clause.
4. **Unit harmonisation.** When scales/units change, apply **KD‑CAL** conversions inside the Measure’s Context; if Cross‑context mapping is needed, declare a **Bridge**.
5. **Population refinement.** If a Clause’s quantifier is refined (e.g., per‑region → per‑AZ), treat each as a new ClauseCell or a new Window partition; avoid hidden re‑baselining.
6. **Proxy retirement.** When direct Observations become available, prefer them; keep earlier proxy‑based verdicts with their CL/Loss notes.

---


---

## 15 · Acceptance tests (SCR/RSCR — concept‑level)

### 15.1 Static conformance (SCR)

* **SCR‑F12‑S01 (Quadruple present).** Every acceptance statement names **ClauseCell**, **WorkCell**, **MeasureCell**, and **Window**.
* **SCR‑F12‑S02 (context‑locality).** Each of the three Cells cites a **Context** (U.BoundedContext).
* **SCR‑F12‑S03 (Evidence admissibility).** The **Observation(s)** are **about** the **same Work** and lie within the **Window**.
* **SCR‑F12‑S04 (Predicate explicit).** The **Predicate** shape is stated (threshold/percentile/share/band/…) with any needed aggregation scope.
* **SCR‑F12‑S05 (Bridge discipline).** Any Cross‑context use declares **Bridge(kind, CL, Loss)**.
* **SCR‑F12‑S06 (Status trichotomy).** The verdict is exactly one of **{Satisfied, Violated, Inconclusive}** and attaches to **ClauseCell\@Window about WorkCell**.
* **SCR‑F12‑S07 (Unit honesty).** MeasureCell specifies **Characteristic, Scale, Unit** (KD‑CAL).
* **SCR‑F12‑S08 (Temporal honesty).** No verdict is asserted without a **Window**; no clause retroactively changes past verdicts.

### 15.2 Regression checks (RSCR)

* **RSCR‑F12‑E01 (Bridge update).** When a **Bridge CL** changes, past verdicts stand; future verdicts **reference the new CL**; reports surface the difference.
* **RSCR‑F12‑E02 (Edition churn).** When a Context’s canon updates, Cells reference the **edition**; old verdicts remain bound to their original editions.
* **RSCR‑F12‑E03 (Scope drift guard).** If the Work population definition changes, verdicts are not silently re‑interpreted; new verdicts cite the new population.
* **RSCR‑F12‑E04 (Window partition).** Changing from monthly to weekly windows creates **new** verdicts; monthly summaries are expressed as explicit aggregations of weekly statuses.
* **RSCR‑F12‑E05 (Proxy retirement).** When direct Observations replace proxies, the status computation is re‑run **forward‑only**; past proxy‑based verdicts retain their CL/Loss annotations.

---

### 15.3 Didactic distillation (60‑second recap)

> **Bind promises to runs with measurements in time.**
> Name the **Clause**, the **Work** it talks about, the **Measure** of what actually happened, and the **Window**. Evaluate the Clause’s **Predicate** on Observations **about that Work in that Window**. If any concept crosses Contexts, declare a **Bridge** with **kind/CL/Loss**. The verdict (**Satisfied/Violated/Inconclusive**) attaches to **Clause\@Window about Work**, never to a plan or to the abstract service.


---

## 14 · Migration notes (conceptual playbook)

1. **Ask the same‑sense question first.** If the underlying **SenseCell/row** is unchanged, prefer `renames`; else reach for `splits/merges`.
2. **Keep it inside the Context.** If your explanation crosses Contexts, stop—this is **Bridge** territory (F.9), not a rename.
3. **Prefer clarity over fashion.** Rename only when the new label **removes a real ambiguity** (F.5 criteria), not to chase style.
4. **Limit nostalgia.** Admit **one** legacy alias in each register that readers will most likely meet; leave the rest to footnotes in examples.
5. **Deprecate with kindness.** When retiring a label, add a one‑line **pointer note** (e.g., “see `timer event` in BPMN; ‘heartbeat’ in KD‑CAL means sensor liveness”).
6. **Rows before names.** If a rename request coincides with a shift in what the row covers, **refactor rows** (F.7) first, then choose labels.
7. **Edition bumps.** When a canon updates, check labels used in that Context: if definitions shift, it’s a **split/merge**; if not, you may `renames` for style/uniformity.
8. **Teach the delta.** In primers, show a **mini table** with legacy → preferred pairs only where readers will encounter both.

---


---

## 15 · Acceptance tests (SCR/RSCR — concept‑level)

### 15.1 Static conformance (SCR)

* **SCR-F13-S01 (context-local continuity).** Every `renames/aliases` relates labels **within the same context** or the **same row/Role Description**; none cross Contexts.
* **SCR‑F13‑S02 (Truthfulness).** For each `renames`, there exists an unchanged **SenseCell/row**; otherwise the move is rejected.
* **SCR‑F13‑S03 (Alias budget).** For any one thing and register, the number of legacy aliases is **≤ 1**.
* **SCR‑F13‑S04 (Non‑retroactivity).** No requirement or suggestion to rewrite past texts is present; continuity is expressed as **read‑paths**.
* **SCR‑F13‑S05 (Row integrity).** A row rename occurs only when the row’s **intension** is stable; if membership changed, a **row split/merge** is documented (F.7).
* **SCR‑F13‑S06 (Bridge discipline).** No alias/rename is used to imply Cross‑context sameness; any such relation is deferred to **F.9**.

### 15.2 Regression (RSCR)

* **RSCR‑F13‑E01 (Edition drift audit).** When a canon edition changes, all labels from that Context are checked against definitions; moves are `renames` if senses stable, else `splits/merges`.
* **RSCR‑F13‑E02 (Alias creep check).** Periodically ensure alias budgets remain within **≤ 1 per register**; surplus aliases are pruned.
* **RSCR‑F13‑E03 (Bridge leak check).** Scan continuity notes for Cross‑context hints; any such case is converted into a **Bridge** or deleted.
* **RSCR‑F13‑E04 (Didactic continuity).** Sampling of examples shows that readers can **resolve** legacy labels to current ones without confusion (via the continuity notes).

---


---

## 6 · Solution — the control cabinet (conceptual, notation‑free)

### 6.1 Reuse by row (first lever)

* **Move.** If a proposal matches the **intension** of an existing row (F.7), adopt its Role Description or add a local SenseCell **inside that row**.
* **Pay‑off.** Names don’t proliferate; Cross‑context tables stay thin.

**Example (services).** *Service‑availability‑compliance* already exists as a row. New labels *SLO‑Met* / *Uptime‑OK* **reuse** that row; SOSA/SSN Observations later feed it (F.12).

---

### 6.2 Bundle instead of hybrid (second lever)

* **Move.** When practice always pairs two Roles, define a **Bundle** `{RoleA, RoleB}`.
* **Not a hybrid.** Do **not** coin *RoleAB*; you’ll erase SoD options and obscure responsibilities.

**Example (enactment).** `{Requester, Approver}` is a Bundle. *Request‑Approver* (one Role) is **not** allowed; it contradicts intended checks.

---

### 6.3 Separate by SoD, don’t evade (third lever)

* **Move.** Record **SoD constraints** where separation matters (“Requester ⟂ Approver in run window”).
* **Why here.** SoD belongs to **semantics**, not org policy; it protects structure across Contexts and times.

**Example (methods).** `{Author ⟂ Reviewer}` in the **review window**. A proposal *Senior‑Reviewer* to “do both” is rejected; the **Bundle** remains `{Author, Reviewer}` with SoD.

---

### 6.4 Window the Status (fourth lever)

* **Move.** Keep a single Status and attach **windows** for *grace*, *evaluation*, *active*, *archival*.
* **Avoid.** *Compliant*, *At‑Risk*, *Grace* as separate Status types.

**Example (acceptance).** **Compliance** Status has readings per window:

* *evaluation window:* “pending check”,
* *active window:* “met / breached”,
* *grace window:* “temporarily tolerated breach”.
  One Status; clear windows.

---

### 6.5 Factor modifiers as facets, not names

* **Move.** Treat qualifiers (shift, locality, domain) as **facets** of the same Role/Status or as **windows**, not new types.

**Example (operations).** *Operator* with **window facet** `timeOfDay = night`—not a new Role *Night‑Operator*.

---


---

## 13 · Migration notes (conceptual playbook)

1. **Map to rows.** For each existing Role/Status, identify its **Concept‑Set row**; if two names share an intent, **collapse** to one row (keep other names as **aliases**, F.13).
2. **Extract SoD.** Replace “super‑roles” with **Bundles** plus explicit **SoD**; where conflict exists, SoD is **normative**, not cultural.
3. **Demote modifiers.** Convert adjectival Role types into **U.Facet** (per Compose‑CAL) or **windows** on the base Role.
4. **Window statuses.** Merge Status families split by time/scale into **one Status + windows**; move waived/exempt notions to the **deontic Context** if applicable.
5. **Re‑use before minting.** When encountering a gap, scan rows for a near‑match; only if intent genuinely differs, open a **new row** (F.8).
6. **Preserve continuity.** Keep historic labels as **aliases** under the consolidated template (F.13); do not rewrite past texts.
7. **Rehearse the cut.** After consolidation, you should be able to recite the entire Role/Status vocabulary **from memory**; if not, reduce again.

---


---

## 14 · Acceptance tests (SCR/RSCR — concept‑level)

### 14.1 SCR — Static conformance

* **SCR‑F14‑S01 (Row reuse).** Every newly proposed Role Description either **references an existing row** or includes a clear **F.8 justification** for a new row.
* **SCR‑F14‑S02 (No hybrids).** No Role Description’s label or definition **conflates** two Roles that stand in a declared **SoD** relation.
* **SCR‑F14‑S03 (Windowed statuses).** Each Status family that shows temporal/scale variation is expressed as **one Status + windows** (not multiple Status types).
* **SCR‑F14‑S04 (Facet over modifier).** Role names do not encode circumstantial modifiers; such modifiers appear only as **facets/windows**.
* **SCR‑F14‑S05 (Context locality).** Every Role Description is anchored to **exactly one SenseCell**; no Cross‑context semantics inside a single template.
* **SCR‑F14‑S06 (Bundles are pure).** Every **Bundle** is a **set of templates** with **no additional semantics** beyond membership and referenced **SoD**.

### 14.2 RSCR — Regression (evolution)

* **RSCR‑F14‑E01 (Vocabulary slope).** Over a given interval, the count of distinct Role/Status templates **does not increase** unless matched by **row justifications** (F.8).
* **RSCR‑F14‑E02 (SoD integrity).** Adding templates does not introduce a label that **circumvents** any existing **SoD** relation.
* **RSCR‑F14‑E03 (Window integrity).** When windows are refined, **Status type count** remains constant; only window definitions change.
* **RSCR‑F14‑E04 (Alias discipline).** When labels change, prior names are recorded as **aliases** (F.13); no silent type multiplication.

---


---

## 16 · Migration cues (conceptual)

1. **When in doubt, fork—not overwrite.** New edition? **Add a Context** unless you can argue sense identity in one sentence.
2. **Name pain → aliases, not merges.** If a label confuses, **rename with an alias**; if meaning changed, **mint new**.
3. **Rows age gracefully.** Never retrofit a row; **retire and re‑row** when any cell’s sense shifts.
4. **Bridges get colder over time.** Prefer to **lower CL** when editions drift; raising CL needs fresh witnesses.
5. **Windows absorb variation.** Resist splitting Status types; **window** by time/scale/phase.
6. **Guard SoD early.** When binding composite responsibilities (F.14), check SoD before naming.
7. **Teach the delta.** When things evolve, write one‑breath deltas (“what changed, why it matters”) as part of the example narrative—no registries implied.

---


---

## 15 · Migration notes (conceptual)

1. **Refactor long tutorials.** Extract the **claim**; pick **3–6 Contexts** (Cards); list the **SenseCells** you actually use; craft **one tight row**; surface any cross‑talk as **Bridges** with loss notes; delete everything else.
2. **Split crowded rows.** If a row tries to carry more than \~4 cells, split into two rows and write a **one‑line purpose** for each.
3. **Stabilise vocabulary.** If you find yourself rewriting terms mid‑page, you likely forgot a Context; return to F.1 and add a Card.
4. **Teach the bridge itch.** Leave “*these are the same*” feelings ungratified until you can articulate **kind, CL, loss** in one sentence.
5. **DesignRunTag respect.** If a design‑only Context tempts you into runtime talk, move that part of the narrative into a **run‑Context** and Bridge as needed.
6. **Keep the page living.** When upstream rows/bridges evolve (F.7–F.9), adjust the page *minimally* and call out the change in a margin note (conceptual, not procedural).

---


---

# | Block | Base concept (EN / RU) | Scale‑map (Σ/Π/μ)
  | Unified Tech name | Unified Plain name | Plain‑Twin Governance (PTG) | Twin‑Map Id (LEX) | Formal U.Type
  | DisciplineColumn‑1 (discipline) | DisciplineColumn-2 (discipline) | DisciplineColumn‑3 (discipline) | DisciplineColumn‑4 (discipline) | DisciplineColumn‑5 (discipline)
  | Unification Rationale | Notes
```

**Examples of Discipline Columns (illustrative):** Operational Management · IT/Software · Physics · Science/Theory · Mathematics · Literature · Religion.  
_(Choose 3–5 that fit the thread; do not place Contexts here.)_

### 13 · Didactic Aids

* **Trip‑wire column (optional).** A ⚡ marker in `Notes` for known homonyms (e.g., *process (BPMN) ≠ process (thermo)*).
* **DesignRunTag tag (optional).** `design` / `run` hint for concepts whose senses split by time.

### 14 · Micro Examples (one line each, illustrative)

*(These illustrate Layout A headings; swap Contexts to match your cut.)*

**Row: `U.Work` (Execution)**
`Tech=Execution · Plain=run` — “Dated, resource‑consuming occurrence realising a MethodDescription.”
**BPMN 2.0 (2011)**: *Activity instance* · **PROV‑O (2013)**: `prov:Activity` · **ITIL 4**: *change/incident record (run)* · **SOSA/SSN**: *(context: producer of Observation)* · **Essence (Language)**: *Activity occurrence* · **Bridges**: CL=3 (BPMN≍PROV) · **Rationale**: *All cells denote the concrete happening, not the recipe nor the capability.*

**Row: `U.MethodDescription` (Recipe)**
`Tech=MethodDescription · Plain=recipe` — “Recorded specification guiding executions.”
**BPMN 2.0 (2011)**: *Process model* · **PROV‑O (2013)**: `prov:Plan` · **ITIL 4**: *SOP / Work instruction* · **Essence (Language)**: *Activity space/Practice description* · **Bridges**: CL=2 (loss: control‑flow vs intent) · **Rationale**: *All cells denote the codified ‘how’, distinct from both the performer and the run.*

> These rows are examples only; your UTS MUST be compiled from your chosen **Contexts** (Layout A) or **Discipline Columns (DC)** (Layout B) and SenseCells.

### 15 · Relations

* **Builds on:** F.1–F.3 (contexts & local senses), F.7 (Concept‑Set), F.5 (names), F.9 (Bridges).
* **Feed:** Part A and Part C definitions/examples (row ids used as cross‑refs); teaching bundles (F.16).
* **Constrained by.** A.7 **Strict Distinction**, A.11 **Parsimony**, **E.10 §6 Twin‑Register Discipline** (Tech/Plain), **E.10.P (prefix registry: tv: / ut:)**, E.10.D1 **Context discipline**.

### 16 · Migration Notes

* **Re‑blocking.** If the Block Plan changes, keep row ids stable; move rows between blocks rather than renumbering.
* **Context growth.** When adding a new Context, populate SenseCells progressively; do not claim coverage until ≥ 1 row per block cites it.
* **Name evolution.** Update **Plain** labels freely for pedagogy; change **Tech** labels only via F.5 with clear S‑rules.


### 17 · FAQ (authoring hygiene)

**Q1. Is the UTS a registry?**
*A.* No. It is a **didactic publication artifact**. No CRUD semantics, no workflows.

**Q2. Can we collapse two Contexts if their terms look identical?**
*A.* Only via **F.9 Bridge** with **CL=3**. Identity must be argued, not assumed by spelling.

**Q3. Where do state‑graphs (A.2.5) show up?**
*A.* In `Notes` or as a dedicated row if the stateful nature of a Role family is central to the thread.

**Q4. How do we show deontic approvals?**
*A.* The concept rows (`U.SpeechAct`, `U.Commitment`, `U.ServiceClause`, `U.ServiceEvaluation`) make the communicative/epistemic pieces visible; enactment appears in examples, not as sheet mechanics.

### 18 · 90‑Second Teaching Script

> “To make our language usable, we publish a **Unified Term Sheet** for each thread. Each **row** is one **unified concept** (a Concept‑Set) named with a **Tech** and a **Plain** label and tied to concrete senses in our chosen **context of meaning**. If two contexts differ, we show an explicit **Bridge** with a **CL score** and a short **loss note**. The rows are grouped into 5–7 **didactic blocks** so the whole sheet fits in working memory. This is not a database; it’s the **one table** a careful mind can hold. From this sheet, everyone—engineers, managers, researchers—can talk precisely about **the same things** across disciplines.”
