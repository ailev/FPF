## 4 · Solution — the **LEX‑BUNDLE** rule‑set (overview)

**LEX‑BUNDLE** aka **ULR (Unified Lexical Rules)** is a compact set of **register, naming, and rewrite** rules with conformance checks.

1. **Vertical Stratification Ladder** (E.10 → four strata);
2. **Twin‑Register Discipline** (Tech/Plain pairs);
3. **Minimal Generality (MG)** principle + tests;
4. **Morphology & Style** (suffixes, casing, reserved prefixes);
5. **Canonical Rewrites** for overloaded words (L‑rules);
6. **Conformance Checklist (CC‑LEX)** and **Regression Stubs (RSCR‑LEX)**.

Below are the **normative clauses** 


---

## E.17.0 — `U.MultiViewDescribing — Viewpoints, Views & Correspondences` \[A]

> **Tech‑name:** `U.MultiViewDescribing`
> **Plain‑name:** multi‑view describing (viewpoints, views, correspondence for families of descriptions/specifications)

**Status & placement.** Part E (Describing & Publication). Normative architectural pattern.
**Builds on:** C.2.1 `U.EpistemeSlotGraph` (DescribedEntity/Viewpoint/View slots), A.6.2 `U.EffectFreeEpistemicMorphing`, A.6.3 `U.EpistemicViewing`, A.6.4 `U.EpistemicRetargeting`, A.7 (Strict Distinction; I/D/S vs Surface), E.10.D1 (Context), E.10.D2 (I/D/S discipline).
**Used by:** E.17 (MVPK — publication as a specialisation of multi‑view describing for morphisms), E.17.1 `U.ViewpointBundleLibrary`, E.17.2 `TEVB`, E.18.S12 (E.TGA engineering viewpoint families), domain‑specific description schemes (architecture, safety cases, governance, research). 

**Guard (lexical).**

* `U.Viewpoint` is the ValueKind of `ViewpointSlot` and denotes **intensional viewpoint specs**, not surfaces or carriers. 
* `U.View` is an alias of `U.EpistemeView`, i.e. an **episteme‑level view**, not a document or file. Views are epistemes; Surfaces are carriers in L‑SURF.
* `ViewFamilyId` is a lexical tag for **families of viewpoints** (e.g. TEVB), never for view kinds, MVPK `U.View`/`U.ViewFamily(·)` bundles or Surface kinds. MVPK face kinds remain `{PlainView, TechCard, InteropCard, AssuranceLane}`. 

### 1 · Problem frame  *(informative)*

Complex systems (social‑technical, cyber‑physical, organisational) are routinely described from **many perspectives**:

* functional vs structural vs deployment vs behavioural views,
* safety vs performance vs cost vs governance views,
* formal specs vs operational runbooks vs regulatory dossiers.

Post‑2015 MBSE and architecture practice emphasise **viewpoints and views** (ISO 42010, SysML v2), and contemporary model‑based toolchains treat views as **queries or projections over shared models** rather than independent documents.

In FPF terms:

* the things we talk about — systems, methods, services, epistemes — are `U.Entity`/`U.Holon` values in `DescribedEntitySlot`; 
* descriptions and specifications of those things are `U.Episteme` instances (`…Description` / `…Spec`) with a **DescriptionContext** = `⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩`; 
* episteme‑level views are `U.View` (`U.EpistemeView`) that slice ClaimGraphs under specific viewpoints and representation schemes. 

What we lack without this pattern is a **universal way to organise families of descriptions/specifications under multiple viewpoints** — for any entity‑of‑interest, not only for architecture, and without collapsing “view” into “document” or “diagram”.

### 2 · Problem  *(informative, but sharp)*

Without `U.MultiViewDescribing`:

1. **Viewpoints, views, and surfaces collapse.**
   In practice, “architecture view”, “diagram”, “spec”, and “published deck” are used interchangeably. This:

   * confuses *episteme* (`U.View`) with *carrier* (`U.Surface`),
   * hides which **concerns and stakeholders** a description is written for,
   * makes it impossible to check whether a given description family is “complete enough” for a chosen viewpoint library.

2. **Descriptions float without viewpoints.**
   Legacy I/D/S discipline distinguishes Intension vs Description vs Spec, but does not, on its own, forbid “view‑from‑nowhere” descriptions (no declared viewpoint). That contradicts the pragmatic stance encoded in C.2.1: **no episteme without concerns**.

3. **Each domain reinvents multi‑view semantics.**
   Architecture, safety cases, governance frameworks, and research workflows all use local notions of “view”, “viewpoint”, and “consistency between views”. Without a shared pattern:

   * E.TGA, MVPK, and discipline packs introduce their own “view” laws, duplicating work;
   * cross‑domain reasoning (e.g. mapping a safety view to an architecture view) becomes ad‑hoc;
   * we cannot give a single formal story for consistency, correspondence, and EpistemicViewing across families of descriptions.

4. **No place to attach correspondence.**
   ISO 42010‑style *correspondences* and modern BX/consistency relations have nowhere canonical to live. We need a **CorrespondenceModel over families of D/S epistemes** that integrates with `U.EpistemicViewing`/`U.EpistemicRetargeting` and C.2.1’s slot graph.

### 3 · Forces  *(informative)*

| Force                                  | Tension                                                                                                                                                                                |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Universality vs domain idioms**      | One pattern should handle engineering, safety, governance, research, etc. ↔ domain communities expect their own jargon (architecture description, safety case, dossier…).              |
| **Viewpoint locality vs reuse**        | Viewpoints must be local to families of descriptions (`EoIClass`, Context) ↔ we want reusable **viewpoint bundles** (libraries) across projects and domains.                           |
| **I/D/S strictness vs pragmatics**     | Intension ≠ Episteme; D/S are epistemes with DescriptionContext ↔ engineers think in “views over a system”, not in pure I/D/S algebra.                                                 |
| **Slot discipline vs approachability** | C.2.1/A.6.5 give a clean SlotKind/ValueKind/RefKind discipline ↔ authors want to talk about “functional view” and “safety view” without carrying all slot jargon in didactic material. |
| **Epistemic vs surface layers**        | Views (epistemes) must be clearly separated from PublicationSurface and carriers ↔ authors often conflate “viewpoint”, “view”, and “document”.                                         |
| **Consistency vs incremental change**  | We want strong correspondence between views ↔ views evolve asynchronously; partial inconsistency must be representable and repairable (BX‑style).                                      |

### 4 · Solution — `U.MultiViewDescribing` as the universal multi‑view scaffold  *(normative core)*

#### 4.1 · Overview

`U.MultiViewDescribing` organises **families of descriptions/specifications** for a shared entity‑of‑interest into a multi‑view structure with:

* **explicit viewpoints** (`U.Viewpoint`) as intensional specs of stakeholders, concerns, allowed D/S kinds, and conformance rules; 
* **episteme‑level views** (`U.View = U.EpistemeView`) as view‑epistemes over those descriptions/specs; 
* a **CorrespondenceModel** capturing correspondences between D/S and their views across viewpoints.

The pattern is **parameterised by a class of described entities**:

> **Parameter:** `EoIClass ⊑ U.Entity` — the class of entities‑of‑interest
> (typical species: `U.Holon` for engineering holons, `U.Morphism` for morphism publication, `U.Episteme` for meta‑describing epistemes).

All members of a `U.MultiViewDescribing[EoIClass]` family share:

* `DescribedEntitySlot` value in that `EoIClass`, and
* a `BoundedContextRef` (E.10.D1) forming a **DescriptionScope** together with the entity. 

Informally:

* Fix an entity `T ∈ EoIClass` and a bounded context `C`.
* The **multi‑view family** for `<T,C>` consists of a set of `…Description` / `…Spec` epistemes, each under a declared viewpoint, plus their `U.View` views, together with a correspondence model relating them.

#### 4.2 · Core constructs

##### 4.2.1 `EoIClass` and DescriptionScope

1. **EoIClass.**
   A `U.MultiViewDescribing` instance declares an `EoIClass ⊑ U.Entity` that acts as a **species‑level constraint** on the ValueKind of `DescribedEntitySlot`.

   * In engineering species (TEVB) this is typically `U.Holon` restricted to `U.System` or `U.Episteme`. 
   * In MVPK, `EoIClass = U.Morphism`. 

2. **DescriptionScope (informal).**
   For a fixed `T ∈ EoIClass` and `C : U.BoundedContext`, the **DescriptionScope** `Scope(T,C)` is the notional scope under which:

   * all descriptions/specifications have `DescribedEntityRef = T` and `BoundedContextRef = C` in their DescriptionContext; 
   * all views (`U.View`) attached to this family preserve that `DescribedEntityRef` and `BoundedContextRef` (for D/S views).

   Formal USM treatment of `U.DescriptionScope` is fixed in E.10/L‑SURF; here we only rely on the intuition “**we are describing this thing, in this context**”.

##### 4.2.2 `U.Viewpoint` (intensional viewpoint spec)

`U.Viewpoint` is already introduced in C.2.1 as the ValueKind of `ViewpointSlot`; E.17.0 fixes its **internal structure** for describing families. 

**Definition (normative, intensional).**
A `U.Viewpoint` is an intensional specification:

* `EoIClassSpec ⊑ U.Entity` — the class of entities this viewpoint is defined for (must be compatible with the family’s `EoIClass`);
* `StakeholderFamilies : FinSet(U.RoleEnactor)` — stakeholder / RoleEnactor families the viewpoint speaks for (e.g. “safety engineers”, “operations teams”).
* `Concerns : FinSet(U.Concern)` — concern set (qualities, risks, obligations) that matter under this viewpoint.
* `AllowedEpistemeKinds : FinSet(U.EpistemeKindId)` — which D/S episteme kinds are admissible as **primary descriptions** and as **derived views** under this viewpoint (e.g. system‑level behaviour description, test harness spec, safety case, CG‑Spec slice).
* `ConformanceRules` — a structured bundle of rules/tests describing when a D/S episteme or view **conforms** to the viewpoint, including:

  * minimal content requirements (e.g. “must cover all safety‑critical functions”),
  * admissible `U.EpistemicViewing` pipelines to derive views from base descriptions,
  * allowed degrees of incompleteness and evidence requirements (link to E.11/ATS and Part F harnesses).

**Slot alignment.**

* `ViewpointSlot` has ValueKind `U.Viewpoint`, RefKind `U.ViewpointRef`; episteme fields are named `viewpointRef : U.ViewpointRef?`. 
* For D/S epistemes in a `U.MultiViewDescribing` family, `viewpointRef` is **mandatory** as part of `DescriptionContext`.

##### 4.2.3 `U.View` (episteme‑level views)

`U.View` is an alias for `U.EpistemeView`, a species of `U.Episteme` whose kind includes:

* `ClaimGraphSlot` (often a sliced or projected ClaimGraph),
* `DescribedEntitySlot`,
* `ViewpointSlot`,
* `ReferenceSchemeSlot` (and usually a `RepresentationSchemeSlot` in C.2.1+).

Normatively:

* A `U.View` in `U.MultiViewDescribing` is obtained via a `U.EpistemicViewing` morphism from some base D/S episteme in the family (see 4.3). It **shares the same `describedEntityRef`** and usually the same `BoundedContextRef`.
* `ViewSlot` is reserved for **references to such views** in meta‑structures (e.g. correspondence models, MVPK view families), never for carriers.

##### 4.2.4 `U.CorrespondenceModel` (view–view correspondence)

`U.CorrespondenceModel` is an episteme (typically a `U.EpistemeCard`) whose ClaimGraph expresses **correspondence relations between D/S epistemes and/or views** within a DescriptionScope:

* cross‑viewpoint correspondences (e.g. “this safety requirement is realised by this design element”),
* structural/behavioural consistency conditions (BX‑style consistency relations),
* change‑impact links (which views must be revisited when some view changes).

`CorrespondenceModel` is **used, but not defined, by A.6.3**: species of `U.CorrespondenceEpistemicViewing` reference it when computing views that depend on multiple epistemes or representation regimes.

### 4.3 · Multi‑view families and their laws (MVD‑0…MVD‑7)  *(normative)*

We now fix the laws that any `U.MultiViewDescribing[EoIClass]` instance must satisfy.

#### MVD‑0 · Family objects

For a fixed `EoIClass` and bounded context `C`, a **multi‑view family** for an entity `T ∈ EoIClass` consists of:

* a (finite) set `D_S(T,C)` of D/S epistemes such that for each `E ∈ D_S(T,C)`:

  * `E : U.Episteme` of some kind in `AllowedEpistemeKinds` of its viewpoint,
  * `subjectRef(E)` decodes to `DescriptionContext(E) = ⟨DescribedEntityRef = T, BoundedContextRef = C, ViewpointRef(E)⟩`,
  * `viewpointRef(E)` lies in the family’s viewpoint set `Σ ⊆ FinSet(U.Viewpoint)`;
* a set `Views(T,C) ⊆ U.View` of view‑epistemes over those D/S epistemes, obtained by declared `U.EpistemicViewing` species (see MVD‑3);
* zero or more `U.CorrespondenceModel` epistemes over `{D_S(T,C), Views(T,C)}`.

Families are **scoped**: the same entity in a different `U.BoundedContext` belongs to a different family.

#### MVD‑1 · Viewpoint locality and totality for D/S

For any multi‑view family:

1. **Viewpoint‑totality for D/S.**
   Each D/S episteme in `D_S(T,C)` **MUST** have a `viewpointRef` either:

   * explicitly populated, or
   * deterministically derived from a `U.ViewpointBundle` the family declares (see E.17.1).

   There are no “viewpoint‑free” D/S epistemes inside a `U.MultiViewDescribing` family.

2. **Viewpoint locality.**
   `ViewpointRef` values for `D_S(T,C)` must belong to a **finite viewpoint set `Σ`** declared for the family (locally or via a bundle). Cross‑family reuse happens **via bundles and Bridges**, not by silently sharing viewpoints across unrelated scopes.

3. **DescriptionContext alignment.**
   `DescriptionContext(E)` for any D/S episteme in the family must use the **same `DescribedEntityRef` and `BoundedContextRef`** as the family; any change of described entity or context is **outside this family** and must be expressed via `U.EpistemicRetargeting` and/or Context Bridges.

#### MVD‑2 · Views are EpistemicViewing results

For any `V ∈ Views(T,C)`:

1. There exists a base episteme `E ∈ D_S(T,C)` and a morphism `v : E → V` such that:

   * `v` is a species of `U.EpistemicViewing`, i.e. an **effect‑free, describedEntity‑preserving** episteme morphism;
   * `describedEntityRef(V) = describedEntityRef(E) = T`,
   * `BoundedContextRef(V) = BoundedContextRef(E) = C`,
   * `viewpointRef(V)` is either:

     * the same as `viewpointRef(E)` (internal normalisation), or
     * a viewpoint in the same family `Σ`, with the change recorded in the family’s `CorrespondenceModel` (see MVD‑4).

2. No view may be introduced “out of thin air”: every `U.View` in the family is traceable to at least one D/S episteme (or a finite diagram thereof) via a **documented EpistemicViewing pipeline**.

3. Views **do not introduce new intensional commitments** about `T` beyond what is licensed by EFEM & EpistemicViewing laws (no new atomic claims about the same described entity). Strengthening Intension requires new D/S under A.7/E.10.D2, not a view.

#### MVD‑3 · Applicability profiles for viewings

Any EpistemicViewing species used inside `U.MultiViewDescribing` **MUST**:

* declare an Applicability profile as per EV‑6: permitted `EoIClass`, grounding, viewpoint ranges, and representation schemes; 
* for D/S epistemes in a family:

  * **preserve** `DescribedEntityRef` and `BoundedContextRef` of `DescriptionContext`,
  * either preserve `ViewpointRef` or change it **within the family’s viewpoint bundle**, with constraints recorded in `CorrespondenceModel`,
  * never widen ClaimScope beyond EFEM/EpistemicViewing allowances.

Any change of described entity (even “small”, e.g. subsystem→system) must be expressed via `U.EpistemicRetargeting` and is **not** a MultiViewDescribing view refinement.

#### MVD‑4 · CorrespondenceModel as the home of cross‑view correspondences

When views or D/S epistemes under different viewpoints are meant to be **kept in correspondence** (in ISO 42010 or BX sense), the family **SHALL**:

1. Provide a `U.CorrespondenceModel` episteme whose `ClaimGraph` captures correspondences and consistency relations over `{D_S(T,C), Views(T,C)}`.

2. Ensure that any `U.CorrespondenceEpistemicViewing` that depends on multiple epistemes or representation schemes:

   * references that `CorrespondenceModel`, and
   * publishes witnesses (proof objects, trace links) that make diagrams commute up to declared isomorphism (oplax naturality allowed).

3. Treat temporary inconsistency explicitly: there may be states where some correspondences are violated; this is represented as **facts in the correspondence ClaimGraph**, not as hidden weakening of viewing laws.

#### MVD‑5 · Separation from publication (MVPK)

`U.MultiViewDescribing` is purely **epistemic**:

* D/S epistemes and views live entirely in Ep‑space (`U.Episteme`);
* it does **not** define PublicationSurface, carriers or rendering;
* MVPK (E.17) sits **on top**:

  * taking morphisms and/or D/S epistemes as input,
  * using `U.EpistemicViewing` plus publication‑specific viewpoints,
  * emitting `U.View` instances that then get attached to Surfaces via L‑SURF.

MultiViewDescribing therefore **does not re‑define I→D/D→S** (`Describe_ID`, `Specify_DS`) and does not introduce any Work on carriers; those remain in A.7/E.10.D2 and E.17.

#### MVD‑6 · I/D/S alignment

For any `U.MultiViewDescribing` instance:

1. Every `…Description` and `…Spec` episteme in the family must satisfy E.10.D2:

   * be an episteme with `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩`,
   * be linked to a unique Intension via `isDescriptionOf` / `isSpecOf` with the additional `ViewpointRef` parameter.

2. Viewings and correspondence operations **must not**:

   * collapse Intension into episteme,
   * confuse D/S with publication surfaces,
   * reinterpret described entity without going through A.6.4 retargeting.

#### MVD‑7 · Slot discipline

All constructs in this pattern **SHALL** respect `U.RelationSlotDiscipline`:

* SlotKinds (`DescribedEntitySlot`, `ViewpointSlot`, `ViewSlot`, `GroundingHolonSlot`, `ClaimGraphSlot`, `ReferenceSchemeSlot`) and their ValueKinds/RefKinds follow A.6.5 and C.2.1.
* `*Slot` suffix is reserved for SlotKinds; `*Ref` for RefKinds/fields, never for Kinds or objects. 
* MultiViewDescribing patterns **must not** invent parallel slot disciplines for “roles in relations”; they reuse SlotKind as the notion of position.

### 5 · Archetypal grounding  *(informative)*

1. **Engineering holon (TEVB).** 
   * `EoIClass = U.Holon` (restricted to `U.System`/`U.Episteme`).
   * TEVB (E.17.2) supplies a viewpoint bundle with canonical engineering viewpoints: Functional, Structural, Role‑Enactor, Module‑Interface, etc.
   * For a particular system `S` in context `C`, D/S epistemes include functional descriptions, structural designs, role‑enactment models, and interface specs.
   * Views derived via EpistemicViewing include sliced safety views, performance‑focused views, and minimal runbooks.
   * `CorrespondenceModel` records how functional elements are realised structurally, where hazards map to components, etc.

2. **Morphism publication (MVPK).**
   * `EoIClass = U.Morphism`.
   * D/S epistemes capture the semantic characterisation of morphisms (pre‑/post‑conditions, CG‑Specs, CHR pins).
   * Viewpoints are publication‑oriented (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`); views are MVPK faces over those morphisms.
   * CorrespondenceModel states how the same morphism appears as a simple narrative, a typed card with units, an interoperability card, and an assurance lane with evidence bindings — all without new claims.

3. **Safety case vs architecture vs operations.**
   * `EoIClass = U.Holon`.
   * Viewpoints: SafetyCase, Architecture, Operations.
   * Families tie together safety requirements, architectural structures, and operational procedures for the same plant `P` in context `C`.
   * Views: a safety‑focused slice of the architecture description, an operational runbook annotated with safety invariants, etc.
   * CorrespondenceModel expresses coverage and consistency between these views, enabling BX‑style repair when one side changes.

### 6 · Conformance checklist (author’s quick use)  *(normative)*

When defining a new `U.MultiViewDescribing` species or using it in a discipline pack:

1. **Declare the EoIClass.**
   *Explicitly state `EoIClass ⊑ U.Entity` and ensure all families restrict `DescribedEntitySlot` accordingly.*

2. **Define the viewpoint set Σ.**
   *List `U.Viewpoint` instances (possibly via a `U.ViewpointBundle`) with stakeholders, concerns, allowed EpistemeKinds, and conformance rules.*

3. **Require DescriptionContext for D/S.**
   *Ensure every `…Description`/`…Spec` episteme in the family has `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩` and that `ViewpointRef ∈ Σ`.*

4. **Specify admissible EpistemicViewing species.**
   *List the `U.EpistemicViewing` profiles used to derive views; declare their Applicability profiles and assert they are describedEntity‑preserving (EV‑6).*

5. **Attach CorrespondenceModel where needed.**
   *Whenever cross‑view consistency matters, introduce a `U.CorrespondenceModel` episteme and reference it from any `U.CorrespondenceEpistemicViewing`.*

6. **Separate describing from publication.**
   *Check that pattern text does not treat I→D/D→S as “publication”, and that any talk of Surfaces/carriers is clearly delegated to MVPK/L‑SURF.*

7. **Respect SlotKind/ValueKind/RefKind discipline.**
   *Use `*Slot` only for SlotKinds, `*Ref` only for RefKinds/fields; avoid `Subject`/`Object` roots in episteme types; use `DescribedEntitySlot` and `viewpointRef` instead.*

### 7 · Consequences  *(informative)*

* **Unified multi‑view story across domains.**
  Engineering descriptions, safety cases, governance dossiers, research artefacts — all become instances of the same multi‑view pattern, enabling coherent tooling and education.

* **Explicit, testable viewpoints.**
  Viewpoints move from vague labels (“architecture view”) to first‑class objects (`U.Viewpoint`) with stakeholder families, concerns, allowed D/S kinds, and conformance rules. This allows ATS‑style checks and better review practices.

* **Views as disciplined projections, not new documents.**
  `U.View` is an episteme generated by viewings, not a free‑floating PowerPoint. This constrains what tools are allowed to do when “generating views”, and prevents silent strengthening of commitments.

* **Correspondence as a first‑class citizen.**
  Consistency and traceability between views are expressed via ClaimGraphs in `U.CorrespondenceModel`, not as scattered hyperlinks or spreadsheet columns.

* **Clean separation of describing vs publishing.**
  `U.MultiViewDescribing` ends the long‑standing conflation between describing (I→D→S) and publication (D/S→Surface). MVPK becomes a clean specialisation on top, not a second I/D/S discipline.

* **Slot‑level interoperability.**
  C.2.1/A.6.5 slot discipline applies uniformly; new domains can introduce viewpoint bundles and multi‑view families without inventing new ontologies for “view positions” or “roles in relations”.

### 8 · Rationale & SoTA‑echoing  *(informative)*

* **ISO 42010 and viewpoint libraries.**
  ISO 42010 distinguished *viewpoints* (stakeholders + concerns + conventions) from *views* (descriptions under those viewpoints) and introduced viewpoint libraries. `U.MultiViewDescribing` generalises this beyond “architecture descriptions” to **any descriptions/specifications**, with `EoIClass` parameter and explicit viewpoint bundles used by TEVB and MVPK. 

* **MBSE & SysML v2 views‑as‑queries.**
  Modern MBSE treats views as **queries over shared models** with controlled rendering. That aligns with `U.EpistemicViewing` as a pure, describedEntity‑preserving morphism, and with `U.View` as an episteme view derived from D/S under a viewpoint.

* **BX / model synchronisation.**
  Bidirectional transformations literature treats consistency relations and repair as first‑class. `U.CorrespondenceModel` and `U.CorrespondenceEpistemicViewing` provide an FPF‑native home for such relations, ensuring that consistency rules live in ClaimGraphs and respect episteme morphism laws, rather than being buried in tool code. 

* **Optics and displayed categories.**
  With C.2.1 and A.6.3, epistemes form a category fibred over described entities; viewings act like optics over the episteme slot graph. `U.MultiViewDescribing` is the **displayed‑category‑like** organisation of families indexed by `DescribedEntitySlot` and `ViewpointSlot`, making later categorical reasoning (e.g. structured cospans for view composition) straightforward.

* **Hybrid symbolic/latent representations.**
  By treating `U.RepresentationScheme` and `U.RepresentationOperation` as episteme components, families can mix symbolic specs, diagrams, code, and latent representations (e.g. LLM‑based summaries) while staying within the same multi‑view discipline and EpistemicViewing laws.

### 9 · Relations  *(informative summary)*

* **Builds on C.2.1 `U.EpistemeSlotGraph`.**
  Uses `DescribedEntitySlot`, `ViewpointSlot`, `ViewSlot`, `ClaimGraphSlot`, `ReferenceSchemeSlot` as the structural backbone for descriptions, views, and correspondence.

* **Builds on A.6.2–A.6.4.**
  Families rely on `U.EffectFreeEpistemicMorphing` for view‑producing morphisms, `U.EpistemicViewing` for describedEntity‑preserving views, and `U.EpistemicRetargeting` for moves that change the described entity (outside a given family).

* **Constrains E.17 (MVPK).**
  MVPK is a **publication‑specialised MultiViewDescribing for morphisms**: its viewpoints are publication viewpoints; its ViewFamily is a special case of `Views(T,C)` with `T` a morphism; its laws must respect MVD‑0…MVD‑7.

* **Constrains E.17.1 / E.17.2.**
  `U.ViewpointBundleLibrary` and TEVB provide concrete viewpoint bundles populating `Σ` for particular `EoIClass` (e.g. engineering holons), but they must treat viewpoints as `U.Viewpoint` values in `ViewpointSlot`, not as ad‑hoc tags. 

* **Coordinates with E.10.D2 (I/D/S) and E.10 LEX‑BUNDLE.**
  Ensures every D/S episteme in a family has a DescriptionContext, keeps “Describe/Specify” distinct from “Publish”, and respects lexical guards around `View`, `Viewpoint`, `Surface`, `ViewFamilyId`, `*Slot`, `*Ref`.

* **Coordinates with B.5.* / F‑cluster.**
  Viewpoints’ stakeholder families and concerns link naturally with RoleEnactment (B.5.*) and Part F role descriptions, assignments, harnesses — without overloading `U.Role` as a coordinate in I/D/S or episteme slots.


---

## E.17.1 — `U.ViewpointBundleLibrary — Reusable Viewpoint Bundles` \[A]

> **Tech‑name:** `U.ViewpointBundleLibrary`
> **Plain‑name:** viewpoint bundle library (reusable viewpoint families)

**Status & placement.** Part E (Describing & Publication). Normative architectural pattern.

**Builds on:**
A.6.2–A.6.4 (Episteme morphism classes),
A.6.5 `U.RelationSlotDiscipline` (SlotKind/ValueKind/RefKind discipline),
A.7 (Strict Distinction; I/D/S vs Surface),
E.7 (Archetypal Grounding),
E.10 (LEX‑BUNDLE, especially naming discipline for `ViewFamilyId`),
E.10.D1/D2 (Context and I/D/S discipline),
E.17.0 `U.MultiViewDescribing`.

**Used by:**
E.17.2 (TEVB — Typical Engineering Viewpoints Bundle),
E.18.S12 (E.TGA engineering viewpoint families),
future domain‑specific viewpoint packs (architecture, governance, safety, research).

**Guard (lexical & ontological).**

* A **viewpoint bundle** is a family of `U.Viewpoint` values (intensional specs) plus metadata; it is **not** a collection of `U.View`, `PublicationSurface`, or files.
* `ViewFamilyId` is a lexical tag that names a **viewpoint family** (bundle), never:
  * a `U.View` kind,
  * an MVPK face/surface kind,
  * nor a file/folder label in L‑SURF.
* `EngineeringVPId` / `PublicationVPId` remain separate (E.18.S12, E.17); E.17.1 does **not** collapse engineering and publication viewpoints into one id.
* Bundles are **intensional catalogue objects**: they specify reusable viewpoint families that `U.MultiViewDescribing` instances may import; they do not define new episteme kinds or surface kinds.

### 1 · Problem frame  *(informative)*

`U.MultiViewDescribing` organises descriptions/specifications of an entity‑of‑interest into multi‑view families with explicit viewpoints and correspondence. In practice:
* engineering teams talk about “functional / procedural / structural / module‑interface” views of a system;
* governance teams talk about “risk / compliance / operations” views of a service;
* research teams talk about “theory / experiment / inference / limitations” views of a method.

Across organisations and projects, these **viewpoint families repeat** with only minor variations. ISO 42010 already recognises *viewpoint libraries* as a way to capture such recurring families for architecture descriptions; MBSE stacks and SysML v2 profiles do the same for model views.

FPF needs a **uniform way to define and reuse such viewpoint families**:
* so that `U.MultiViewDescribing` can import them instead of redefining Σ from scratch;
* so that E.TGA and MVPK can refer to the same engineering viewpoint families via stable ids;
* so that authoring guidance (E.8/E.12) and lexical discipline (E.10) can attach to named families rather than ad‑hoc sets.

### 2 · Problem  *(informative)*

Without a dedicated pattern for viewpoint bundle libraries:

1. **Each domain bakes its own “viewpoint sets”.**
   E.TGA, MVPK, safety‑case disciplines, and governance packs tend to introduce local notions such as “engineering views”, “assurance views”, “governance decks” without a shared representation. Viewpoints drift, and cross‑domain mapping becomes opaque.

2. **Viewpoint identity is unstable.**
   A team may call something “functional view” in one project and “capability view” in another, even though the underlying concerns, stakeholders, and conformance rules are identical. The same `U.Viewpoint` is re‑invented and slightly renamed, making long‑term consistency and automation harder.

3. **MultiViewDescribing cannot easily reuse families.**
   `U.MultiViewDescribing` allows an arbitrary finite set of viewpoints Σ for each `<T,C>` (entity, context). Without a standard way to say “Σ is the TEVB engineering family” or “Σ is the governance‑risk bundle”, each family has to list viewpoints explicitly and locally.

4. **ISO 42010 viewpoint libraries remain external.**
   There is no canonical place in FPF where ISO‑style viewpoint libraries (for architecture descriptions) can be represented as first‑class objects and aligned with FPF’s `U.Viewpoint`, I/D/S discipline, and episteme morphisms.

5. **Lexical aliases leak into semantics.**
   Names like “Functional”, “SafetyCase”, or “Regulatory” may be used both as:

   * intensional viewpoint specs; and
   * ad‑hoc labels on documents, files or MVPK faces.
     Without a clear lexical discipline, this causes confusion about what exactly is being reused.

E.17.1 addresses these issues by introducing `U.ViewpointBundleLibrary` as the place where **reusable viewpoint families** are defined, named, and versioned.

### 3 · Forces  *(informative)*

| Force                                     | Tension                                                                                                                                                                       |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Reuse vs local fit**                    | Organisations want shared viewpoint families (engineering, safety, governance) ↔ projects need to tweak or subset them for specific contexts and maturity levels.             |
| **Domain idioms vs neutral core**         | Domains carry their own jargon (architecture, safety case, regulatory dossier) ↔ FPF needs a neutral `U.Viewpoint` core to support cross‑domain reasoning and tooling.        |
| **Stability vs evolution**                | Viewpoint families must be stable enough to support long‑term automation and training ↔ they must evolve as practices and standards evolve.                                   |
| **Intensional vs artefact layers**        | Viewpoint families talk about concerns and conformance rules ↔ teams routinely attach the same name to concrete documents or MVPK faces.                                      |
| **Engineering vs publication viewpoints** | Engineering viewpoints govern how a holon is described ↔ publication viewpoints govern how those descriptions are exposed as surfaces; we need both, without collapsing them. |
| **Library size vs cognitive load**        | Rich libraries with many viewpoint families increase flexibility ↔ authors must still be able to choose and understand a small subset in each project.                        |

### 4 · Solution — `U.ViewpointBundleLibrary`  *(normative core)*

#### 4.1 · Overview

`U.ViewpointBundleLibrary` is the **architectural home for reusable viewpoint families**.

* A **viewpoint library** is a collection of **viewpoint bundles**; each bundle names and packages a finite family of `U.Viewpoint` values that are intended to be reused together.
* Each **viewpoint bundle**:

  * is identified by a `ViewFamilyId` lexical tag;
  * constrains an `EoIClass ⊑ U.Entity` for which its viewpoints are valid;
  * enumerates a finite set Σ of `U.Viewpoint` definitions;
  * may carry archetypal grounding cards (E.7) and alignment notes (e.g., ISO 42010 mappings).

`U.MultiViewDescribing[EoIClass]` then uses such bundles as **providers of Σ** for families of descriptions/specifications:

* for a fixed entity `T ∈ EoIClass` and bounded context `C`, a `U.MultiViewDescribing` family may declare:

  * that its viewpoint set Σ is **imported from** a specific `ViewFamilyId`, possibly with a finite subset selection; or
  * that Σ is locally defined (no bundle) — still allowed, but less reusable.

TEVB (E.17.2) and E.TGA S12 are species of this pattern for engineering holons.

#### 4.2 · Core constructs

##### 4.2.1 `U.ViewpointBundleLibrary` (library object)

**Tech:** `U.ViewpointBundleLibrary` (kernel/species type).
**Plain:** viewpoint library.

A `U.ViewpointBundleLibrary` is a **catalogue of viewpoint bundles**, with at least:

* `libraryId : LibraryId` — lexical identifier of the library (e.g. `FPF.Core.Viewpoints`, `OrgX.EngineeringViewpoints`).
* `bundles : FinSet(U.ViewpointBundle)` — finite or countable set of bundles it provides.
* `editionId : EditionId` — edition of the library, subject to the usual LEX‑AUTH / LAT discipline (E.15).
* optional `scopeTags` and governance metadata (owner, change‑control).

**Normative constraints.**

1. Within a given `U.ViewpointBundleLibrary` edition, `ViewFamilyId` values **SHALL be unique**.
2. Libraries **SHALL NOT** define new kernel episteme kinds or surface kinds; they only package `U.Viewpoint` values and metadata.
3. Libraries **MAY** be specialised:

   * a core FPF library (e.g. TEVB, generic governance bundles);
   * organisational libraries extending or subsetting core bundles.

##### 4.2.2 `U.ViewpointBundle` and `ViewFamilyId` (viewpoint family)

**Tech:** `U.ViewpointBundle` (species type), `ViewFamilyId` (lexical id).
**Plain:** viewpoint family, bundle of viewpoints.

A `U.ViewpointBundle` is a **family of compatible viewpoints** packaged for reuse. Minimal structure:

* `viewFamilyId : ViewFamilyId` — lexical id for the family (e.g. `VF.TEVB.ENG`, `VF.GovRisk`, `VF.ResearchMethod`).
* `EoIClassSpec ⊑ U.Entity` — class of entities this family is meant for (must be compatible with each viewpoint’s `EoIClassSpec`).
* `viewpoints : FinSet(U.Viewpoint)` — finite, non‑empty set of `U.Viewpoint` values (typically referenced via `U.ViewpointRef` in episteme cards).
* optional `ArchetypalCards : FinSet(U.ArchetypalGroundingRef)` — grounding cards per viewpoint (E.7).
* optional `AlignmentNotes` — e.g., ISO 42010 mappings, domain standard references.

**Normative constraints.**

VBL‑1. **EoIClass compatibility.**
For every `vp ∈ viewpoints`:

* `vp` **SHALL** resolve to a `U.Viewpoint` whose `EoIClassSpec` refines `EoIClassSpec` of the bundle (`EoIClassSpec(vp) ⊑ EoIClassSpec(bundle)`).

VBL‑2. **Finite, named family.**

* `viewpoints` **SHALL** be finite and non‑empty.
* Each `U.Viewpoint` **SHOULD** carry a stable `ViewpointId` (lexical id) distinct from `ViewFamilyId`.
* The same `U.Viewpoint` **MAY** appear in multiple bundles (e.g. a general “Regulatory” viewpoint in both engineering and governance bundles).

VBL‑3. **Lexical non‑collision.**

* `ViewFamilyId` **MUST NOT** be used as:

  * a `U.ViewId` / `U.ViewFamily(·)` id in MVPK,
  * a `SurfaceKind` or carrier kind in L‑SURF,
  * a generic `ViewpointId` without qualifier (E.18.S12).
* Libraries **SHOULD** adopt naming schemes that make the distinction clear, e.g. `VF.*` for families, `VP.*` for viewpoints, `PV.*` for publication viewpoints.

VBL‑4. **Intensionality.**

* A `U.ViewpointBundle` is **intensional**: it talks about the family of `U.Viewpoint` specs and their intended use; it does **not** contain any D/S epistemes, `U.View` instances, or `PublicationSurface` artefacts.
* Any concrete document or MVPK face referencing a family **SHALL** do so through its `ViewFamilyId` and per‑view `ViewpointId`, not by embedding the bundle.

##### 4.2.3 Binding bundles into `U.MultiViewDescribing`

`U.MultiViewDescribing[EoIClass]` organises families of descriptions/specifications for a fixed `<T,C>` (entity, context) with a finite viewpoint set Σ.

**Binding rule (informal).**

* Given a `U.ViewpointBundleLibrary` and a bundle with `EoIClassSpec` compatible with the family’s `EoIClass`, a `U.MultiViewDescribing[EoIClass]` instance **MAY** declare:

  * `ViewFamilyId` — the bundle that provides its “canonical” viewpoint set;
  * `ActiveViewpoints ⊆ viewpoints(bundle)` — the subset actually used in this `<T,C>` family.

**Normative constraints.**

VBL‑5. **Bundle import.**
For any `U.MultiViewDescribing[EoIClass]` instance that declares a `ViewFamilyId`:

* its viewpoint set Σ **SHALL** be a finite subset of the `viewpoints` of that bundle;
* every D/S episteme in the family **SHALL** have `viewpointRef` in Σ (as required by E.17.0 / E.10.D2);
* every `U.View` attached to that family under E.17.0 **SHALL** preserve `viewpointRef` from Σ.

VBL‑6. **Multi‑bundle coordination.**
A single `<T,C>` family **MAY** rely on more than one bundle (e.g. TEVB + a safety bundle). In that case:

* the family **SHALL** declare how Σ is partitioned by `ViewFamilyId` (e.g. engineering vs safety);
* any CorrespondenceModel in the family that links views across families **SHALL** cite the relevant `ViewFamilyId` values.

VBL‑7. **No implicit bundles.**
If a `U.MultiViewDescribing` family does **not** declare a `ViewFamilyId`, its Σ is considered **local**. Such families are valid but:
* provide no guarantee of reuse in other projects;
* may be required, by organisational policy, to migrate to a library bundle before external publication.

### 5 · Archetypal grounding  *(informative)*

#### 5.1 · TEVB engineering viewpoints (preview species)

*Context.*
An engineering organisation wants a **standard family of viewpoints** for describing holons (`U.System` or `U.Episteme`) in E.TGA and MVPK.

*Bundle shape (TEVB, to be defined fully in E.17.2).*

* `viewFamilyId = VF.TEVB.ENG`
* `EoIClassSpec = U.Holon` (with species restriction “is `U.System` or `U.Episteme`”)
* `viewpoints = {VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface, …}`

Each `VP.*` is a `U.Viewpoint` with:

* `StakeholderFamilies` drawn from engineering RoleEnactors (design, operations, safety);
* `Concerns` tuned to capability, process, structure, and interface questions;
* `AllowedEpistemeKinds` pointing to E.TGA‑level descriptions/specs;
* `ConformanceRules` linked to CV/GF check catalogues.

The bundle is defined once, in a shared library; E.TGA S12 then **imports** `VF.TEVB.ENG` and maps these viewpoints to E.TGA constructs without re‑defining them.

#### 5.2 · Governance & risk bundle

*Context.*
A governance team wants a reusable set of viewpoints across projects: “Risk”, “Control”, “Compliance”, “Operations”.

*Bundle shape.*

* `viewFamilyId = VF.GovRisk`
* `EoIClassSpec = U.Holon` (holons representing services or programmes)
* `viewpoints = {VP.Risk, VP.Control, VP.Compliance, VP.Operations}`

The same bundle is used:

* in a MultiViewDescribing family for a specific service holon;
* in a publication context where MVPK faces for governance reports reference `VF.GovRisk` and specific `VP.*` ids.

Archetypal grounding cards (E.7) illustrate each viewpoint with a 1‑page “Tell–Show–Show” example.

### 6 · Conformance checklist  *(normative)*

| ID                                           | Requirement                                                                                                                                                                          | Practical test                                                                             |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| **CC‑VBL‑0 (Unique ViewFamilyId)**           | Within a library edition, each `ViewFamilyId` is unique and refers to exactly one `U.ViewpointBundle`.                                                                               | Scan library metadata; no duplicates; foreign keys resolve.                                |
| **CC‑VBL‑1 (EoIClass compatibility)**        | For every bundle, all `U.Viewpoint` members have `EoIClassSpec` refining the bundle’s `EoIClassSpec`.                                                                                | Check `EoIClassSpec(vp) ⊑ EoIClassSpec(bundle)` for each `vp`.                             |
| **CC‑VBL‑2 (Bundle‑backed families)**        | Any `U.MultiViewDescribing` family that declares a `ViewFamilyId` uses Σ equal to a finite subset of that bundle’s `viewpoints`; all D/S epistemes and views use `viewpointRef ∈ Σ`. | For each family, inspect Σ and `viewpointRef` fields; verify subset and coverage.          |
| **CC‑VBL‑3 (No surface hijack)**             | `ViewFamilyId` never appears as a `SurfaceKind`, MVPK face kind, or carrier type.                                                                                                    | Token scan of schemas and configs; no matches outside library metadata.                    |
| **CC‑VBL‑4 (Archetypal grounding coverage)** | For bundles intended for non‑expert authors, each viewpoint has at least one `U.ArchetypalGrounding` reference.                                                                      | For each such bundle, check that `ArchetypalCards` cover all `viewpoints`.                 |
| **CC‑VBL‑5 (Edition discipline)**            | Libraries and bundles are editioned; changes in viewpoint membership or semantics create new editions rather than silently mutating existing ones.                                   | LAT / change log shows edition bumps for breaking changes; older editions remain readable. |


### 7 · Cross‑cutting constraints & naming discipline  *(normative)*

1. **E.10 / A.6.5 alignment.**
   `U.ViewpointBundleLibrary` **SHALL** follow LEX‑BUNDLE and `U.RelationSlotDiscipline`:
   * separate **Tech** and **Plain** registers in names and prose;
   * respect the `*Slot`/`*Ref` conventions from A.6.5 (no `ViewFamilySlot` here; `ViewFamilyId` is a lexical token, not a SlotKind);
   * treat `U.Viewpoint` as the ValueKind for `ViewpointSlot` and `U.ViewpointRef` as its RefKind (no new SlotKinds for viewpoint families);
   * avoid overloading `view`, `viewpoint`, `Surface`, `carrier`.

1. **Engineering vs publication viewpoint ids.**
   * Engineering viewpoint families (TEVB, E.TGA S12) use `EngineeringVPId` for `U.Viewpoint` in the bundle.
   * Publication viewpoint families (MVPK) use `PublicationVPId` for MVPK viewpoint ids.
   * A bundle **MAY** contain engineering viewpoints, publication viewpoints, or both, but the id namespaces **SHALL** be disambiguated (e.g. `VP.Eng.*` vs `VP.Pub.*`).

1. **ISO 42010 mapping.**
   * An ISO 42010 “viewpoint library” becomes a `U.ViewpointBundleLibrary` edition.
   * Individual ISO viewpoints correspond to `U.Viewpoint` values inside one or more bundles.
   * ISO “architecture descriptions” correspond to concrete combinations of `U.MultiViewDescribing` families + MVPK surfaces that import those bundles; E.17.1 does not define architecture itself.

1. **Archetypal grounding linkage.**
   * For any bundle that is intended for non‑expert authors, each `U.Viewpoint` in `viewpoints` **SHOULD** have at least one `U.ArchetypalGrounding` card (E.7) referenced from the bundle.
   * These cards are didactic only; they do not alter the semantics of the viewpoints.

1. **Tooling hooks.**
   * Tools **MAY** treat `ViewFamilyId` as a primary key for viewpoint selection widgets, template libraries, or documentation navigation.
   * Tools **MUST NOT** infer semantics from the shape of `ViewFamilyId`; semantics come from the `U.Viewpoint` definitions.

### 8 · Consequences  *(informative)*

| Benefit                                    | Why it matters                                                                                                           | Trade‑offs / Mitigations                                              |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| **Reusable viewpoint families.**           | Teams and tools can share a common understanding of “functional view”, “risk view”, etc., across projects and domains.   | Requires governance of libraries and editions (E.15).                 |
| **Cleaner MultiViewDescribing instances.** | Families can say “we use TEVB+GovRisk” instead of spelling out Σ by hand.                                                | Local Σ are still allowed; migration to bundles may be an extra step. |
| **Better ISO 42010 alignment.**            | ISO viewpoint libraries become first‑class, mappable objects in FPF.                                                     | Needs careful mapping work per architecture sub‑domain.               |
| **Terminology hygiene.**                   | Distinguishing ViewFamilyId from ViewpointId and from surfaces reduces confusion in tooling and documentation.           | Enforced via LEX‑guards and CI checks.                                |
| **Cross‑domain reasoning.**                | The same bundle can be referenced from E.TGA, MVPK, and discipline packs, enabling consistent cross‑view correspondence. | Libraries must stay small and curated to avoid cognitive overload.    |

### 9 · Rationale & SoTA‑echoing  *(informative)*

* **ISO 42010 (Edition 2) viewpoint libraries.**
  ISO 42010 generalises *system‑of‑interest* to *entity‑of‑interest* and allows viewpoint libraries that define reusable viewpoint sets for architecture descriptions. `U.ViewpointBundleLibrary` adopts this idea but generalises it beyond architecture to any `EoIClass`, and connects it to FPF’s explicit `U.Viewpoint`, I/D/S discipline, and episteme morphisms.

* **MBSE and SysML v2 view definitions.**
  Modern MBSE practice treats views as **queries over models** governed by named viewpoints, often organised into libraries or profiles. `U.ViewpointBundleLibrary` provides a neutral representation of such libraries so that SysML‑like stacks can be integrated without hard‑coding their terminology into the core.

* **Safety and assurance cases.**
  Safety‑case frameworks (e.g. GSN‑based) implicitly rely on recurrent viewpoints (“hazard analysis”, “mitigation design”, “evidence aggregation”). Embedding them into bundles allows assurance‑oriented Viewpoint families to be reused and linked to Part F harnesses and ATS tiers.

* **Governance and research workflows.**
  Governance / audit frameworks and research pipelines similarly rely on recurring perspectives (e.g. “internal validity”, “external validity”, “reproducibility”). Viewpoint bundles allow these perspectives to be captured once and referenced across many MultiViewDescribing instances.

Overall, `U.ViewpointBundleLibrary` is the mechanism by which **post‑2015 multi‑view practice** (viewpoint libraries, reusable view definitions) is integrated into the FPF stack without compromising strict I/D/S separation or the episteme slot discipline of C.2.1/A.6.5.

### 10 · Relations  *(informative summary)*

* **Builds on C.2.1 `U.EpistemeSlotGraph`.**
  Uses `ViewpointSlot` / `ViewSlot` as the structural anchors for viewpoints and views; bundles provide reusable values for `ViewpointSlot`.

* **Builds on A.6.2–A.6.4.**
  Viewpoint bundles do not change episteme morphism laws; they parameterise which `U.EpistemicViewing` pipelines are admissible under a given viewpoint family.

* **Builds on A.7 / E.10.D2.**
  Description/specification epistemes remain I/D/S‑disciplined; bundles only constrain the `viewpointRef` part of `DescriptionContext`.

* **Builds on E.7.**
  Archetypal grounding cards for viewpoints are organised and referenced via bundles, making didactic examples reusable.

* **Constrains E.17.0 `U.MultiViewDescribing`.**
  Families that declare a `ViewFamilyId` must draw Σ from the corresponding `U.ViewpointBundle` (VBL‑5/6).

* **Constrains E.17 (MVPK).**
  MVPK viewpoint sets for publication **SHOULD** be declared as bundles in a library; MVPK faces must not treat `ViewFamilyId` as a surface kind.

* **Constrains E.17.2 (TEVB) and E.18.S12 (E.TGA engineering viewpoint families).**
  TEVB must be expressed as one or more `U.ViewpointBundle` instances; E.TGA S12 maps engineering viewpoints by referring to those bundles, not by defining its own opaque ids.

* **Coordinates with E.10 (LEX‑BUNDLE) and E.15 (LEX‑AUTH).**
  `ViewFamilyId` and `ViewpointId` naming, editioning and evolution follow lexical and authoring protocols; migrations between library editions are tracked in LATs.


---

## E.17.2 — `TEVB — Typical Engineering Viewpoints Bundle`  \[A]

> **Tech‑name:** `TEVB` (Typical Engineering Viewpoints Bundle, bundle id `VF.TEVB.ENG`)
> **Plain‑name:** typical engineering viewpoints bundle for holons
> **Tag:** [A] — archetypal species of `U.ViewpointBundle` for engineering holons

**Status.** New; archetypal, notation‑agnostic species of `U.ViewpointBundle` / `U.ViewpointBundleLibrary`.
It is an engineering‑level bundle over holons; it does not itself constitute an architecture framework or architecture‑specific viewpoint library. Architecture‑focused viewpoint bundles are introduced as separate `U.ViewpointBundle` species that may import TEVB.

**Builds on.**
* **E.17.0 — `U.MultiViewDescribing`.** Supplies the generic notion of `U.Viewpoint`, `U.View`, and `ViewFamily` over an `EoIClass ⊑ U.Entity` (here: `EoIClass = U.Holon`).
* **E.17.1 — `U.ViewpointBundleLibrary`.** Provides the generic `U.ViewpointBundle`/`ViewFamilyId` structure; TEVB is a concrete bundle (`VF.TEVB.ENG`) in the core library.
* **A.1 — Holon.** Holon kinds `U.System` and `U.Episteme` as the typical engineering entities‑of‑interest.
* **A.6.2–A.6.4 — Episteme morphisms.** `U.EffectFreeEpistemicMorphing`, `U.EpistemicViewing`, `U.EpistemicRetargeting` as the generic morphism classes behind engineering views.
* **A.7 / E.10.D2 — Strict Distinction & I/D/S.** I/D/S discipline and DescriptionContext; engineering descriptions/specifications under TEVB are D/S‑epistemes with explicit `ViewpointRef`.
* **C.2.1 — `U.EpistemeSlotGraph`.** Provides `DescribedEntitySlot`, `ViewpointSlot`, `ViewSlot` and the slot discipline (A.6.5) used by TEVB‑aligned descriptions/specs.

**Used by.**
* **E.18.S12 — E.TGA viewpoint map.** As a canonical consumer, E.TGA binds its engineering transduction families (Functional, Procedural, Role‑Enactor/Device‑Structure, Module‑Interface) to TEVB viewpoints `VP.Functional`, `VP.Procedural`, `VP.RoleEnactor`, `VP.ModuleInterface`.
* **E.17 (MVPK).** Publication of engineering morphisms uses TEVB engineering viewpoints on the description/spec side and PublicationVPs on the Surface side.
* **Engineering description/spec patterns.** System, method, module/interface and role‑related description/spec patterns for holons (`U.System`, `U.Episteme`) refer to TEVB when declaring their `ViewpointRef`.
* **ISO‑aligned architecture‑description bundles.** Future species patterns for architecture‑specific viewpoint bundles reuse TEVB as the canonical engineering view family (Functional vs Structural etc.) over systems and their epistemes.

**Guard (lexical & ontological).**
1. **Engineering scope only.** TEVB applies to `EoIClass = U.Holon` with typical cases `U.System` and `U.Episteme`. Using TEVB viewpoints for non‑holonic entities (e.g., pure data structures, abstract theories) requires an explicit species‑level justification; by default it is a conformance violation.
2. **Viewpoint vs Surface.** `VP.Functional`, `VP.Procedural`, `VP.RoleEnactor`, `VP.ModuleInterface` are **viewpoints** (intensional `U.Viewpoint` specifications), **not** Surface kinds. They MUST NOT be used as carrier/Surface names (those remain `{PlainView, TechCard, NormsCard, InteropCard, AssuranceLane, …}` under L‑SURF).
3. **EngineeringVPId vs PublicationVPId.** `VP.*` in this pattern are **EngineeringVPId** values (E.18.S12) and SHALL NOT be reused as PublicationVPs in MVPK. MVPK must introduce separate `PublicationVPId` symbols, linked to TEVB viewpoints only through correspondences.
4. **No new role coordinates in I/D/S.** TEVB references stakeholder groups via `U.RoleEnactor` families but does not introduce `U.Role` as a coordinate in I/D/S signatures (E.10.D2). Role semantics remain confined to RoleEnactment patterns (A.15, F‑R family).
5. **No extra viewpoints inside TEVB.** TEVB defines a **fixed core set** of four engineering viewpoints. Other labels such as “Assurance‑Oriented”, “Interop‑Oriented”, “Information/Data‑Oriented”, “Operational/Deployment”, “Mission/Context” may appear only as **lexical aliases** in E.18.S12 (e.g. as `ViewFamilyId` / `AliasInViewFamilies` values for transduction species). They MUST NOT extend `TEVB.EngBundle.viewpoints` and MUST NOT be interpreted as additional `U.Viewpoint` kinds in this bundle; when SoTA or local practice demands explicit assurance, information, or mission viewpoints, these SHALL be provided as **separate `U.ViewpointBundle` species** that can be imported alongside TEVB rather than by mutating `VF.TEVB.ENG`.
6. **Not an architecture framework.** TEVB is an engineering‑level viewpoint bundle; architecture‑specific viewpoint bundles and architecture frameworks MUST be introduced as separate `U.ViewpointBundle` species that may import TEVB. They MUST NOT redefine `VF.TEVB.ENG` as an “architecture viewpoint library” or extend it with architecture‑only viewpoints.

### 1 · Problem frame  *(informative)*

Engineering teams almost always talk about systems and their models through a **small set of recurring “views”**:
* *What capabilities and behaviours does the system enact?* — function‑oriented, transduction‑oriented talk.
* *What sequences, workflows, and control logics does it realise?* — procedure/process/state‑oriented talk.
* *Who or what enacts which roles?* — role‑enactment, organisational and socio‑technical talk.
* *How is the system decomposed into modules and interfaces?* — physical/logical architecture talk.

In industry, these lenses show up under many names: *functional view, logical view, behavioural view, process view, structural/physical view, deployment view, responsibility view,* and so on. Modern standards and tools (ISO/IEC/IEEE 42010:2022, INCOSE SE Handbook, SysML v2 “views as queries”) all recognise that **viewpoints should be reusable structures**, not ad‑hoc labels.

In FPF, E.17.0 and E.17.1 give the **generic machinery**:
* `U.Viewpoint` as an intensional specification (stakes/concerns/allowed D/S kinds),
* `U.View` as an episteme‑level view (epistema under a viewpoint),
* `U.ViewpointBundle` / `ViewFamilyId` as reusable collections of viewpoints.

E.TGA (E.18.S12) already assumes a **canonical engineering family** with names like “Functional”, “Procedural”, “Role‑Enactor (Device‑Structure)”, “Module‑Interface”. Without a formal bundle tying these together, those names drift and the mapping between E.TGA, MVPK and I/D/S becomes fragile.

TEVB addresses this by defining a **single, explicit engineering bundle** with a fixed `ViewFamilyId` and a small set of canonical engineering viewpoints over `U.Holon`.

### 2 · Problem  *(informative)*

Without TEVB, several failure modes recur:
1. **Inconsistent “functional/structural/behavioural” vocabularies.** Different teams define “functional view” or “process view” differently, even within one organisation; E.TGA S12 then has to guess how to map transduction graphs onto whichever interpretation is currently in play.
2. **Architecture frameworks leak into the kernel.** 4+1‑style and similar architectural frameworks get hard‑coded as if they were universal; FPF loses its holonic neutrality and becomes biased to a particular school.
3. **Viewpoints conflated with surfaces and files.** “Functional view” is used both for the underlying viewpoint and for a concrete document or dashboard; MVPK faces, E.TGA transduction families, and I/D/S disciplines become entangled.
4. **Role leakage into I/D/S.** Engineering views that are about role‑enactors are written directly in terms of `U.Role`, blurring the boundary between RoleEnactment (A.15) and description/spec layers, and breaking A.7/E.10.D2.
5. **Poor reuse across systems.** Even when organisations want to reuse the same engineering views across products, plants, or models, there is no canonical bundle to import; each programme recreates “its own” functional/structural views.

TEVB makes engineering viewpoint families **first‑class reusable bundles** and pins them to an explicit `EoIClass` (engineering holons) so that E.TGA, MVPK and discipline‑packs can align on the same vocabulary.

### 3 · Forces  *(informative)*

| Force                                       | Tension                                                                                                                                                                       |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Universality vs domain idioms**           | We need engineering viewpoints that work for *any* holon (hardware/software/socio‑technical), yet remain recognisable to practitioners steeped in domain‑specific frameworks. |
| **Parsimony vs expressiveness**             | A small, stable **NQD‑front** set of engineering view families (Function, Behaviour/Process, Role‑Enactor, Module‑Interface) vs the temptation to proliferate specialised views for every stakeholder group or quality attribute. |
| **Neutral core vs architecture frameworks** | FPF core must stay neutral and not encode a specific framework (4+1, DoDAF, etc.), while still being compatible with them.                                                    |
| **Consistency vs organisational autonomy**  | Central TEVB definitions must be stable, yet individual organisations need room to refine concerns and episteme kinds within the bundle.                                      |
| **I/D/S clarity vs convenient shortcuts**   | Viewpoints must not re‑introduce `Role` as a coordinate in I/D/S, nor blur Description/Spec/Surface distinctions, even though practitioners informally mix these.             |

TEVB resolves these by fixing a **minimal engineering bundle** and leaving customisation to **species patterns and ViewpointBundleLibrary entries** that refine concerns and allowed episteme kinds without changing the core families.

### 4 · Solution — TEVB as a core `U.ViewpointBundle` for holons  *(normative)*

#### 4.1 TEVB bundle identity

TEVB is the **core engineering viewpoint bundle** over holons.

* **Bundle object.** There exists a canonical `U.ViewpointBundle` instance:

  ```
  TEVB.EngBundle : U.ViewpointBundle
  ```

* **ViewFamilyId.**

  ```
  TEVB.EngBundle.viewFamilyId = VF.TEVB.ENG
  ```

  `VF.TEVB.ENG` is reserved for **“Typical Engineering Viewpoints (Engineering)”** in the FPF core ViewpointBundleLibrary.

* **EoIClassSpec (holon scope).**

  TEVB is parameterised by

  ```
  TEVB.EngBundle.EoIClassSpec =
    { h : U.Holon | holonKind(h) ∈ {U.System, U.Episteme} }
  ```

  That is, TEVB applies to holons that are either `U.System` or `U.Episteme`. Other holon kinds MAY be added by species patterns but MUST be justified and documented; the default conformance profile assumes systems and epistemes.

* **Library placement.**

  TEVB lives in the core viewpoint library:

  ```
  TEVB.Library : U.ViewpointBundleLibrary
  TEVB.Library.libraryId = FPF.Core.Viewpoints
  TEVB.Library.bundles ⊇ { TEVB.EngBundle }
  ```

  Additional organisational libraries MAY import and specialise TEVB, but SHALL NOT redefine `VF.TEVB.ENG` with incompatible semantics.

* **Viewpoint set.**

  TEVB defines a **finite set of canonical engineering viewpoints**:

  ```
  TEVB.EngBundle.viewpoints =
    { VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface }
  ```

The selection `{VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}` is the current **NQD‑frontier** for engineering holon viewpoints in Part G: it realises a Function–Behaviour–Structure‑plus‑Role (`F–B–S+R`) cut that is non‑dominated against candidate families including explicit information/data, assurance/safety, and mission/context viewpoints under the N/U/C/D axes (C.18, G.0). Part G records the SoTA candidate set and rejected alternatives; TEVB only fixes the **core four** where each `VP.* : U.Viewpoint` is defined below. These four are the **only** viewpoints in the core TEVB bundle.

  > **Note.** Other ViewFamilyId values used in E.TGA (e.g., *Assurance‑Oriented*, *Interoperability‑Oriented*, *Information/Data‑Oriented*, *Operational/Deployment*, *Mission/Context*) remain **lexical families only** for transduction species (E.18.S12). They do not add viewpoints to TEVB; they are orthogonal to TEVB’s `viewpoints` set.

#### 4.2 TEVB engineering viewpoints

Each TEVB viewpoint is a `U.Viewpoint` with:
* `viewpointId : ViewpointId` (concrete identifier, e.g., `VP.Functional`);
* `EoIClassSpec` **inherited from the bundle** (`U.Holon` with `System`/`Episteme` kinds);
* `StakeholderFamilies : FinSet(RoleEnactorFamilyId)` — families of `U.RoleEnactor` that are the primary audience;
* `Concerns : FinSet(ConcernId)` — engineering concerns this viewpoint foregrounds;
* `AllowedEpistemeKinds : FinSet(U.EpistemeKindRef)` — description/spec kinds admissible under this viewpoint (all obeying I/D/S discipline and C.2.1 slot discipline);
* `ConformanceRules : FinSet(RuleId)` — references to checklist items in conformance packs (CV/GF/engineering checklists).

The subsections below fix the **normative intent and minimal field profiles** for each TEVB viewpoint. Species patterns and discipline‑packs may refine `Concerns`, `AllowedEpistemeKinds` and `ConformanceRules`, but MUST preserve the intent.

##### 4.2.1 `VP.Functional` — capability & transduction viewpoint

**Intent.** Look at a holon in terms of **what it can do** under roles: capabilities, transductions, and functional responsibilities, rather than in terms of modules or procedures.

* **viewpointId.**

  ```
  VP.Functional : ViewpointId  // EngineeringVPId
  ```

* **EoIClassSpec.**
  Same as the bundle: `U.Holon` with `System`/`Episteme` kinds.

* **StakeholderFamilies (typical examples).**
  Actual `StakeholderFamilies : FinSet(U.RoleEnactor)` values are defined in RoleEnactment discipline packs; labels below are informal.
  * System engineering leads and architects (e.g. SysEng‑lead enactors).
  * Product owners / capability owners.
  * Reliability / performance engineers when reading capability envelopes.

* **Concerns (typical).**
  * Capabilities and functions provided by the holon (`CapabilityConcerns`).
  * Behaviour under roles (`RoleBehaviourConcerns`).
  * Non‑functional envelopes: throughput, latency, availability, energy, safety (`NFPEnvelopeConcerns`).
  * Compositional semantics of functions/transductions (`TransductionCompositionConcerns`).

* **AllowedEpistemeKinds (shape).**
  `VP.Functional` admits descriptions/specifications whose **DescribedEntitySlot** is a holon’s **capability/Method/Mechanism** under a role, e.g.:
  * `SystemFunctionalDescription`, `SystemFunctionalSpec` (species of `U.EpistemeKind` describing system‑level capabilities and their interconnection).
  * `TransductionDescription`, `TransductionSpec` (E.TGA functional lanes).
  * `ServiceCapabilityDescription`, `ServiceCapabilitySpec` (when a holon is in Service role).

  All such epistemes MUST:
  * obey I/D/S discipline: `…Description`/`…Spec` as D/S‑layers for `U.Method`/`U.Mechanism`/`U.Service`;
  * make their `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩` explicit, with `ViewpointRef = VP.Functional`.

* **ConformanceRules (examples).**
  * Functional flows are **total** over their declared domain (no implicit dangling capabilities).
  * Transductions are typed at interfaces (A.6.0, A.6.1) and respect A.6.2/A.6.3 purity/conservativity.
  * When functional views participate in retargeting patterns (e.g. structural reinterpretation species based on `U.EpistemicRetargeting`), they MUST satisfy the relevant retargeting constraints from A.6.4; concrete consumer patterns (such as E.TGA structural reinterpretation, E.18.S9) MAY impose additional rules.

* **SoTA echo (informative).** `VP.Functional` corresponds to the “functional view” in ISO‑aligned architecture descriptions and domain reference architectures (functional viewpoints in IoT and space reference architectures, functional/logical layers in sector frameworks), and to the **Function** axis in FBS‑style design ontologies. It is also the natural home for SysML/SysML‑v2 capability and logical architecture models and for “logical view” slices in 4+1‑style frameworks, once recast into holon/capability terms.

##### 4.2.2 `VP.Procedural` — process & control viewpoint

**Intent.** Look at a holon in terms of **how behaviours are sequenced and controlled**: workflows, state machines, operational procedures, and control logic.

* **viewpointId.**

  ```
  VP.Procedural : ViewpointId  // EngineeringVPId
  ```

* **EoIClassSpec.**

  Same as the bundle.

* **StakeholderFamilies (typical).**
  * Operations and run‑time owners (`OperationsEnactorFamily`).
  * Control engineers and automation specialists (`ControlEngineerEnactorFamily`).
  * Safety engineers concerned with procedural correctness (`SafetyEngineerEnactorFamily`).

* **Concerns (typical).**
  * Control flow and ordering of actions (`OrderConcerns`).
  * State‑machine behaviour and lifecycle (`StateLifecycleConcerns`).
  * Concurrency, synchronisation, and error handling (`ConcurrencyConcerns`).
  * Operational modes and transitions (startup, shutdown, degraded modes) (`OperationalModeConcerns`).

* **AllowedEpistemeKinds (shape).**
  `VP.Procedural` admits descriptions/specifications where the **DescribedEntitySlot** is a method/process/control Behaviour for the holon, e.g.:
  * `MethodDescription`, `MethodSpec` for operational procedures (A.3.1–A.3.2).
  * `ControlLogicDescription`, `ControlLogicSpec` (IEC 61131‑3 style step diagrams/statecharts).
  * `WorkflowDescription`, `WorkflowSpec` (business processes, orchestration logic).

  These epistemes:
  * must respect the **order discipline** (Γ_method, Γ_ctx) and A.15 (Role–Method–Work alignment);
  * must carry I/D/S‑conformant DescriptionContext with `ViewpointRef = VP.Procedural`.

* **ConformanceRules (examples).**
  * Pre/post‑conditions at step boundaries are explicit and type‑checked (A.3.1/A.3.2, Γ_method).
  * No embedding of Work or calendars inside procedural descriptions (A.7/E.10.D2).
  * Failure modes and recovery actions are declared and traceable to safety analyses (F.15 harnesses where relevant).

* **SoTA echo (informative).** `VP.Procedural` captures the dynamic/process dimension found in SoTA architecture and MBSE practice: process views in 4+1, operational/behavioural views in defence and enterprise frameworks, behaviour diagrams in SysML (activity, sequence, state, interaction), and procedure/control‑oriented models in industrial standards. TEVB abstracts this into a notation‑agnostic “behaviour over time” viewpoint for holons.

##### 4.2.3 `VP.RoleEnactor` — role & device‑structure viewpoint

**Intent.** Look at a holon in terms of **who/what plays which roles** and **how physical/organisational structure supports those roles**. This viewpoint covers both socio‑technical role assignments and “device view” readings of transduction graphs (E.TGA).

* **viewpointId.**

  ```
  VP.RoleEnactor : ViewpointId  // EngineeringVPId
  ```

* **EoIClassSpec.**

  Same as the bundle.

* **StakeholderFamilies (typical).**
  * Organisational designers and operations managers (`OrgDesignEnactorFamily`).
  * Safety and compliance officers concerned with separation of duties (`SegregationOfDutyEnactorFamily`).
  * Hardware/system engineers concerned with which devices carry which functions (`DeviceEngineerEnactorFamily`).

* **Concerns (typical).**
  * Which holons enact which roles under which contexts (`RoleEnactmentConcerns`).
  * Allocation of capabilities to devices/subsystems (`CapabilityAllocationConcerns`).
  * Organisational constraints: segregation of duties, responsibilities, escalation paths (`GovernanceConcerns`).
  * Device‑view readings of functional graphs (E.TGA Device‑View).

* **AllowedEpistemeKinds (shape).**
  `VP.RoleEnactor` admits descriptions/specifications where the **DescribedEntitySlot** is a **role structure or capability allocation** associated with the holon, e.g.:
  * `RoleDescription`, `RoleSpec` (F.4, F.18) for human or system roles.
  * `RoleEnactmentDescription` for mappings `Holder#Role:Context` (A.15).
  * `DeviceAllocationDescription` mapping functions/transductions to physical modules or devices.

  As with other TEVB viewpoints, these are D/S‑epistemes with `DescriptionContext.ViewpointRef = VP.RoleEnactor`.

* **ConformanceRules (examples).**
  * Role vs Method vs Work vs Capability separation is upheld (A.7, A.15).
  * Device‑view reinterpretation from functional flows MUST be expressed as `U.EpistemicRetargeting` with an explicit `KindBridge` witness (A.6.4). Specific retargeting schemes (for example, E.TGA’s structural reinterpretation in E.18.S9) may add further constraints but are not fixed by TEVB itself.
  * No “role as behaviour” conflation: Roles are masks, behaviours remain Methods/Work.

* **SoTA echo (informative).** `VP.RoleEnactor` aligns with the allocation/responsibility and resource/organisational view clusters seen across MBSE frameworks: allocation views in UAF/NAF, role‑responsibility matrices and RACI‑style artefacts, and “who/what plays which role” slices in usage and operational viewpoints. Many post‑2015 reference architectures treat this axis implicitly; TEVB makes it explicit and holon‑centred while remaining compatible with socio‑technical and device‑allocation practices.

##### 4.2.4 `VP.ModuleInterface` — module & interface viewpoint

**Intent.** Look at a holon in terms of its **modules, interfaces, and structural composition**: what parts exist, how they connect, and how their contracts are specified.

* **viewpointId.**

  ```
  VP.ModuleInterface : ViewpointId  // EngineeringVPId
  ```

* **EoIClassSpec.**
  Same as the bundle.

* **StakeholderFamilies (typical).**
  * Hardware and software architects responsible for structure (`StructureArchitectEnactorFamily`).
  * Integration and test engineers (`IntegrationEngineerEnactorFamily`).
  * Lifecycle and maintenance planners looking at replaceable units (`MaintenancePlannerEnactorFamily`).

* **Concerns (typical).**
  * Module decomposition and containment (mereology) (`ModuleMereologyConcerns`).
  * Interfaces and contracts — ports, APIs, physical connectors (`InterfaceConcerns`).
  * Dependency structures and allowed couplings (`DependencyConcerns`).
  * Replaceability and variation points (`VariabilityConcerns`).

* **AllowedEpistemeKinds (shape).**
  `VP.ModuleInterface` admits descriptions/specifications where the **DescribedEntitySlot** is a **structural architecture** of the holon, e.g.:
  * `SystemStructureDescription`, `SystemStructureSpec` (module/connector descriptions).
  * `ModuleInterfaceDescription`, `ModuleInterfaceSpec` (signature, contracts, physical interface definitions).
  * E.TGA‑style interface/port descriptions over `Signature`/`Mechanism` graphs.

  These epistemes describe the carrier (structure) rather than capability. Functional↔physical reinterpretations between `VP.Functional` and `VP.ModuleInterface` are expressed via `U.EpistemicRetargeting` + `KindBridge` (A.6.4, E.18.S9).

* **ConformanceRules (examples).**
  * Interfaces are typed and explicitly bound to standards where applicable (A.6.0, F‑specs).
  * No inlining of Methods/Work into structure (strict separation of structure vs behaviour).
  * Reinterpretations from functional views into structure MUST respect the applicable `U.EpistemicRetargeting`/Bridge constraints (A.6.4). When combined with a concrete retargeting scheme (e.g. E.TGA structural retargeting, CC‑TGA‑06‑EX), that scheme’s additional rules also apply.

* **SoTA echo (informative).** `VP.ModuleInterface` matches the structural/implementation/deployment families that dominate SoTA architecture descriptions: development and physical views in 4+1, construction/deployment viewpoints in IoT reference architectures, logical/physical architecture layers in UAF/NAF and RASDS‑style frameworks, and structural and interface‑focused models in SysML‑based MBSE. TEVB treats all of these as specialisations of a single holonic “modules and interfaces” viewpoint.

### 5 · Archetypal grounding  *(informative)*

A minimal TEVB instantiation looks as follows:

```
TEVB.EngBundle :
  U.ViewpointBundle {
    viewFamilyId   = VF.TEVB.ENG
    EoIClassSpec   = { h : U.Holon | HolonKind(h) ∈ {System, Episteme} }
    viewpoints     = { VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface }
    LibraryRef     = FPF.Core.Viewpoints
  }
```

Each `VP.*` viewpoint is a `U.Viewpoint` as in E.17.0, with:

* `viewpointId ∈ {VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}`,
* `EoIClassSpec` inherited from `TEVB.EngBundle`,
* `StakeholderFamilies`, `Concerns`, `AllowedEpistemeKinds`, `ConformanceRules` aligned with the subsections above.

**Engineering holon (example).**

Let `Plant_X : U.System` be a production plant, and `ControlStack_X : U.Episteme` be its control and optimisation stack as a holon.

* Under `VP.Functional`, `Plant_X` is viewed as a bundle of capabilities and transductions: material/energy/product flows, optimisation functions, safety envelopes.
* Under `VP.Procedural`, `Plant_X` is viewed as sets of procedures and control sequences: startup/shutdown, normal operation, emergency handling.
* Under `VP.RoleEnactor`, `Plant_X` is viewed as networks of role‑enactors: human operators, controllers, subsystems enacting roles in SOPs and safety cases.
* Under `VP.ModuleInterface`, `Plant_X` is viewed as modules and interfaces: equipment units, pipelines, control modules, buses, and their interfaces/contracts.

Each of these is a **family of D/S‑epistemes** with `DescriptionContext = ⟨DescribedEntityRef(Plant_X or ControlStack_X), BoundedContextRef, ViewpointRef=VP.*⟩` and TEVB ensures that E.TGA and MVPK can rely on this common structure.

### 6 · Conformance checklist  *(normative)*

**CC‑TEVB‑1 (Bundle identity).**
Any artefact claiming to be “TEVB engineering viewpoints” MUST:

* refer to `viewFamilyId = VF.TEVB.ENG`,
* have `EoIClassSpec = {h : U.Holon | HolonKind(h) ∈ {System, Episteme}}`,
* enumerate `viewpoints = {VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}` and no others.

**CC‑TEVB‑2 (Viewpoint definition).**
Each `VP.*` viewpoint MUST be a well‑formed `U.Viewpoint` per E.17.0:

* `viewpointId` equal to one of the four engineering IDs,
* `EoIClassSpec` equal to the bundle’s,
* `StakeholderFamilies`, `Concerns`, `AllowedEpistemeKinds`, `ConformanceRules` explicitly declared.

**CC‑TEVB‑3 (DescriptionContext completeness).**
Every D/S‑episteme participating in a TEVB‑managed multi‑view family for a holon MUST have a `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩` with:

* `DescribedEntityRef` referencing a `U.System` or `U.Episteme`,
* `ViewpointRef ∈ {VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}`,
* `BoundedContextRef` pointing to the engineering context (E.10.D1).

**CC‑TEVB‑4 (Separation from PublicationVPs).**
`VP.*` identifiers from TEVB MUST NOT be used as `PublicationVPId` in MVPK. Publication viewpoints live in MVPK and may **correspond** to TEVB engineering viewpoints via `CorrespondenceModel`, but are separate symbols.

**CC‑TEVB‑5 (No Role coordinate in I/D/S).**
TEVB‑aligned descriptions/specs MAY reference `U.RoleEnactor` families in `StakeholderFamilies` but SHALL NOT add `Role` or `RoleEnactor` as axes in I/D/S signatures beyond what A.7/E.10.D2 already provides. Role semantics stay in RoleEnactment patterns; TEVB just selects concerns.

**CC‑TEVB‑6 (Alignment with consumer viewpoint maps).**
When a pattern defines engineering viewpoint families named “Functional”, “Procedural”, “Role‑Enactor (Device‑Structure)”, or “Module‑Interface” over the same `EoIClass` and claims TEVB alignment (for example, E.TGA S12 viewpoint map), it MUST bind them to TEVB viewpoints as follows:

* “Functional” → `VP.Functional`,
* “Procedural” → `VP.Procedural`,
* “Role‑Enactor (Device‑Structure)” → `VP.RoleEnactor`,
* “Module‑Interface” → `VP.ModuleInterface`.

Any deviation MUST be explicitly documented as a species‑level extension and MUST NOT reuse `VF.TEVB.ENG`.

### 7 · Rationale & SoTA echoing  *(informative)*

#### 7.1 NQD‑grounded choice of the core four

Part G’s NQD discipline treats candidate viewpoint families as points in an N/U/C/D quality space (Use‑Value, Constraint‑Fit, Novelty, Diversity_P). Applied to a SoTA‑harvested candidate set of engineering viewpoints (Functional, Behavioural/Procedural, Structural/Module, Allocation/Role, Information/Data, Assurance/Safety, Mission/Context, Deployment/Operational, Business/Usage), this yields a small Pareto frontier for *engineering holon* viewpoints. On that frontier, the `F–B–S+R` cut implemented by `{VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}` is the minimal set that:
* spans the Function–Behaviour–Structure ontology used in contemporary design theory while adding an explicit allocation/responsibility axis;  
* aligns with the “functional/process/structural/deployment” clusters recurrent in standards and architecture frameworks;  
* stays neutral with respect to domain‑specific qualities (`‑ilities`) and business/mission framing, which are captured in separate Q‑bundles and governance/viewpoint packs rather than in TEVB itself.

Other candidates (e.g. dedicated information, assurance, or mission viewpoints) remain important but either duplicate concerns already captured by TEVB (when specialised to engineering holons) or are better modelled as orthogonal quality bundles (C.25) or non‑engineering bundles (business/governance packs). TEVB therefore pins only the core four and leaves the rest to specialised families.

#### 7.2 Alignment with post‑2015 engineering practice

* Modern architecture standards built on ISO/IEC/IEEE 42010 describe viewpoint libraries in which functional, behavioural/process, structural/deployment, and business/usage concerns are the dominant clusters; sector RAs such as IoT RA 30141 and space‑domain RAs provide explicit functional and construction/implementation viewpoints alongside business/usage and trustworthiness viewpoints. TEVB reuses the functional and construction/structural clusters as `VP.Functional` and `VP.ModuleInterface`, while treating business and trustworthiness as separate bundles.  
* Model‑based systems engineering practice (INCOSE MBSE guidance, SysML v2 “views‑as‑queries”, UAF/NAF view grids) converges on a small set of core diagram families: structure vs behaviour vs allocation/responsibility vs requirements/mission. TEVB’s `VP.Procedural` and `VP.RoleEnactor` correspond to the behaviour and allocation/responsibility axes, respectively, and are designed to be notation‑neutral over SysML/UAF/UML/Capella‑style models.  
* The FBS family of design ontologies (Function–Behaviour–Structure and extensions) provides a widely used conceptual basis for separating what a system is for, what it does over time, and what it consists of. TEVB’s four viewpoints intentionally implement an FBS+R split at the holon level: `VP.Functional` ≈ Function, `VP.Procedural` ≈ Behaviour, `VP.ModuleInterface` ≈ Structure, with `VP.RoleEnactor` capturing the explicit mapping from functions/behaviours to role‑enacting carriers.  
* Within FPF itself, E.TGA’s “viewpoint families” (Functional, Procedural, Role‑Enactor/Device‑Structure, Module‑Interface, plus assurance/interoperability/data/operational/mission aliases) are harmonised by letting the **core four** be TEVB viewpoints and treating the rest as lexical or bundle‑level overlays, not as new kernel viewpoints.

#### 7.3 Why TEVB stays small

TEVB is deliberately *not* a complete architecture framework. It gives FPF a stable, holon‑centred engineering bundle that:
* is small enough to keep in working memory and to govern via EpistemeSlotGraph discipline;  
* is expressive enough to host mappings from SoTA architecture frameworks (4+1, domain‑specific RAs, UAF/NAF grids, SysML‑based MBSE method kits);  
* can be safely combined with additional `U.ViewpointBundle` species (safety/assurance packs, business/mission packs, information/data packs) without mutating the core four;
* sits conceptually **below** architecture‑specific viewpoint libraries, which are introduced as separate `U.ViewpointBundle` species layering TEVB with mission/quality/business viewpoints instead of redefining TEVB.

As SoTA evolves, new bundles can be added or TEVB can gain a new edition with a revised NQD‑frontier, but the TEVB‑A edition fixed here remains the archetypal engineering bundle for holons.

### 8 · Relations  *(informative)*

* **Builds on.** E.17.0 (`U.MultiViewDescribing`), E.17.1 (`U.ViewpointBundleLibrary`), A.7/E.10.D2 (I/D/S), C.2.1 (EpistemeSlotGraph), A.6.2–A.6.4 (episteme morphisms).
* **Constrains.** E.18.S12 (E.TGA viewpoint map), engineering description/spec patterns, MVPK engineering publication profiles.
* **Coordinates with.** L‑SURF/L‑PUBSURF (Surface kinds), F‑R family (Role, RoleDescription, RoleSpec), F.18 (naming discipline for ViewFamilyId / ViewpointId / EngineeringVPId / PublicationVPId).
* **Non‑goals.** TEVB does not prescribe modelling notations (SysML, BPMN, IEC 61131‑3, etc.), storage formats, or tool APIs. It only fixes the **conceptual viewpoint bundle** that such tools must respect when claiming FPF alignment.


---

## E.17 — **Multi‑View Publication Kit (for Morphisms)** \[A]

> **Tech‑name:** `U.MultiViewPublicationKit` (**MVPK**)  
> **Plain‑name:** Multi‑view publication kit (for morphisms)  
> **Signature (conceptual form):**  `MVPK : (U.Morphism, Σ_viewpoints) ↦ U.ViewFamily` with per‑viewpoint components
> `ViewObj_s : U.Object → U.ViewObj_s` and `Emit_s(·) : U.Morphism → U.ViewMorph_s`,
> such that `(ViewObj_s, Emit_s)` forms a functor `U → View_s(U)`. For each `s ⪯ t`, a **reindexing coercion**
> `PromoteView[s→t]_X : ViewObj_s(X) → ViewObj_t(X)` exists and is **natural in `X`**: for every `f : X → Y`,
> `PromoteView[s→t]_Y ∘ Emit_s(f) = Emit_t(f) ∘ PromoteView[s→t]_X` (see Laws §6.2).
> **Notation:** `Σ_viewpoints` is abbreviated as `Σ` where convenient.
> **Twin‑register aliases (naming discipline):**
> • **Tech:** `Emit_PlainView`, `Emit_TechCard`, `Emit_InteropCard`, `Emit_AssuranceLane`; `PromoteView[s→t]_·`.  
> • **Plain:** `PlainView(x)`, `TechCard(x)`, `InteropCard(x)`, `AssuranceLane(x)`; “Promote to *t*”.

> **USM binding (overview):** `PublicationScope` is a **USM‑class** object that parameterizes MVPK; see §5.0.  
> **Episteme level.** MVPK treats each face as a `U.View` in the sense of C.2.1/E.17.0 (species `U.EpistemeView`). For a morphism `f`, every `Emit_s(f)` is such a view whose `DescribedEntitySlot`/`DescriptionContext` target is `f : U.Morphism` and whose `viewpointRef` is a publication `U.Viewpoint` (`PublicationVPId`) drawn from a `U.ViewpointBundle` (E.17.1/E.17.2). Slot discipline (`ViewSlot`/`ViewRef`) is inherited from C.2.1/A.6.5 and is not redefined in MVPK.

### 1 · Intent

Provide a **disciplined, compositional way to publish morphisms** (arrows) across multiple didactic faces (views/cards) **without adding semantics**, while keeping **viewpoints** (the specifications that constrain views) explicit and auditable. Authors get a small **view‑pack** that, when applied to any `U.Morphism` (including compositions), yields a **family of views** that commute with arrow composition and respect edition/measurement pinning (Part F/G).

### 2 · Problem frame

* Teams routinely need several **faces** of the *same* arrow: a **Tech card** for the catalog, an **Interop card** for machine exchange, a **Plain view** for narrative, and an **Assurance lane** for evidence.    
* Informal “renderings” quietly **drift semantics**; **composite arrows** are often published piecemeal, breaking traceability; **evidence** forgets unit/scale/edition pins.    
* “View” and “viewpoint” are **blurred** in practice; authors conflate **publication** with **mechanism**.    
* L‑SURF requires **Surface token discipline**; Core allows only **PublicationSurface/InteropSurface**; faces are **…View / …Card / …Lane** (no ad‑hoc `…Surface` kinds). 

**MVPK** fixes this by making publication a **typed, functorial projection** from existing D/S‑epistemes via species of `U.EpistemicViewing` (A.6.3/E.17.0, A.7 §5.9/E.10.D2) subject to explicit **viewpoint specs** and **pinning guards**. **Part E is conceptual:** no machine‑exchange formats are specified here.

### 3 · Problem

1. **Semantic drift in publication.** Unchecked “presentations” introduce claims not present in the D/S‑epistemes about the arrow (epistemes with `DescriptionContext = ⟨DescribedEntityRef, BoundedContextRef, ViewpointRef⟩` in the sense of E.10.D2/E.17.0).    
2. **Non‑compositionality.** Publishing `g∘f` yields surfaces that don’t match composing the surfaces of `f` and `g`.    
3. **View vs viewpoint confusion.** A single template is treated as “the view”, with no declared concerns or conformance rules.    
4. **Unpinned numbers.** Numeric claims lack unit/scale/reference‑plane and **edition pins** (Part F/G), undermining auditability.    

### 4 · Forces

| Force | Tension |
| --- | --- |
| **Compositionality vs legibility** | Preserve arrow laws across views ↔ keep each view didactic and audience‑appropriate. |
| **Neutral naming vs domain idioms** | Use vocabulary stable across domains ↔ allow local templates (SOPs, APIs, checklists). |
| **Surface orthogonality (A.7)** | Publication must not mutate I/D/S semantics ↔ authors expect “rich presentations”. |
| **Evidence discipline** | Views must cite CG‑Spec/CHR anchors ↔ authors want compact cards. |

### 5 · Solution — the **MVPK Kit**

#### 5.0 USM anchoring (normative)
* **PublicationScope (USM).** Define `U.PublicationScope` in **USM** analogously to `U.WorkScope` and `U.ClaimScope`. An MVPK kit instance is **governed by** a `PublicationScope` that fixes:
  * (a) the **viewpoint index** `Σ` and its partial order `⪯`,
  * (b) the **profile** (MVPK‑Min/Lite/SetReady/Max) as a *configuration* of this scope,
  * (c) the admissible **Publication characteristics (PC)** and required **pinning contracts**,
  * (d) any **cross‑Context/plane** constraints (Bridge/CL policies) applicable to emitted faces.
* **Scope lineage.** `PublicationScope` participates in the same USM lineage regime as `WorkScope`/`ClaimScope` (editioning and migration rules); MVPK emits faces **under** a declared `PublicationScopeId`.
* **L, P, D, E quartet.** The canonical MVPK‑Max scope enumerates exactly four **face kinds**: `PlainView (P)`, `TechCard (T)`, `InteropCard (I)`, `AssuranceLane (A)`. If a program elects to retain the mnemonic **(L, P, D, E)** tuple, it MUST map it 1‑to‑1 onto these **face kinds** within `PublicationScope` and SHALL NOT introduce additional kinds without a USM extension.

#### 5.1 Terminology (normative)

* **View** (`U.View`): an episteme‑level view (`U.EpistemeView` in the sense of C.2.1/E.17.0) produced *under* a publication viewpoint. In MVPK each face (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`) is such a `U.View` whose `DescribedEntitySlot`/`DescriptionContext` target is a `U.Morphism` and whose `viewpointRef` is a publication `U.Viewpoint`.  
  Every MVPK `U.View` **SHALL** declare:  
  `SurfaceKind ∈ {PublicationSurface, InteropSurface}`, `PublicationVPId : U.ViewpointRef`, references to the underlying D/S‑epistemes produced by `Describe_ID`/`Specify_DS` in A.7/E.10.D2, and a `U.PublicationScope` (USM §6.5).  
  Any materialization/rendering is separate **Work on SCR/RSCR carriers** and is not part of `U.View`.
* **Publication vs presentation vs rendering vs representation (guard):**    
    * **Publication** = typed projection from existing D/S‑epistemes about a morphism onto a `U.View`/`PublicationSurface` via species of `U.EpistemicViewing` (A.6.3) under the I/D/S discipline of A.7/E.10.D2.        
    * **Presentation** = rhetorical arrangement of a published carrier; **notation‑neutral**, adds no claims and is **not** a Surface kind.        
    * **Rendering** = display/layout of a carrier, purely graphical/formatting; **Work on carriers** (A.7), not a Surface kind.        
    * **Representation** = episteme↔referent relation (C.2.1/A.6.2–A.6.4); **not** a surface act. Use **publication** and **view** here; treat presentation/rendering as **Work on carriers** (A.7).
* **ISO mapping note.** ISO **viewpoint** → `PublicationVPId` (publication layer); **engineering viewpoint** → `EngineeringVPId` (E.TGA §S12). An ISO **view** may be a single MVPK face; “bundles” are packaging only.
* **No‑mechanism equivalence:** MVPK **is not** a mechanism; any operational toil (build/render/upload) is **separate Work by a system on carriers** (A.7; see **Laws 5 — No Γ‑leakage** in §6).
* **ViewpointSpec (`U.Viewpoint`)** — a typed specification that declares stakeholders, concerns, conformance rules, allowed **Publication Characteristics**, and pinning requirements per profile. The index set `Σ` consists of identifiers of `U.Viewpoint` instances, typically drawn from `U.ViewpointBundle` species (E.17.1/E.17.2) (see §5.3).

#### 5.2 Allowed surfaces at Part E (L‑SURF discipline)
Part E restricts the term *Surface* to **PublicationSurface** and **InteropSurface**. Concrete faces SHALL be named **…View / …Card / …Lane**. 

**USM linkage (normative).** Every `U.View` **SHALL** declare a `U.PublicationScope` (USM §6.5).  
For a view **about an episteme** `E`: `PublicationScope(view_E) ⊆ ClaimScope(E)`.  
For a view **about a capability** `C`: `PublicationScope(view_C) ⊆ WorkScope(C)`.  
Cross‑context views **SHALL** cite Bridge + CL; **CL penalties apply to R only** (scope membership unchanged).

**L‑PUBSURF naming discipline**
 * Allowed surface kinds: **PublicationSurface**, **InteropSurface**.
 * Concrete faces MUST be named **…View / …Card / …Lane**.
* The tokens **carrier/bearer/holder** MUST NOT name a `U.View` or any publication entity.  
  Use **`U.View`** (PlainView / TechCard / InteropCard / AssuranceLane) for conceptual publication faces.  
  Reserve **carrier** exclusively for **SCR/RSCR** (symbol/document/data carriers) and **Work on carriers**.
* Avoid geometric metaphors (axis/dimension) for publication artifacts; use **Characteristic/CharacteristicSpace** only when referring to CHR‑MM entities.
* **Non‑collision guard.** `ViewFamilyId` (lexical tag for viewpoint families) MUST NOT be used to name any `U.View` or surface kind; MVPK face kinds remain **{PlainView, TechCard, InteropCard, AssuranceLane}** only.

**MVPK‑Max viewpoints (normative; exactly four; governed by PublicationScope):**
* `PlainView` (explanatory prose view)    
* `TechCard` (typed catalog card)    
* `AssuranceLane` (evidence bindings/lanes)
* `InteropCard` (conceptual interoperability view; **mapping to concrete exchange formats lives in Annex/Interop; Part E does not specify schemas**)

**Lean profiles (small‑team friendly, optional; as PublicationScope configurations):**
* **MVPK‑Min (F0–F1):** Σ = {`PlainView`, `TechCard‑Lite`}. `AssuranceLane` omitted. No interop face.
* **MVPK‑Lite (F1–F3):** Σ = {`PlainView`, `TechCard‑Lite`, `AssuranceLane‑Lite` gated by crossing trigger}. `InteropCard` only if external consumers exist.
* **MVPK‑SetReady (F3–F5):** add `InteropCard` when replayability or external interchange is required (details outside Part E).
* **Escalation triggers:** (i) cross‑Context/plane reuse; (ii) QD/OEE replay needs; (iii) external consumption.
* **“‑Lite” variants (definition):** A *‑Lite* face removes optional fields only (never claims), keeps the same typing as its full counterpart, and MUST retain pins for any numeric content. Upgrading from *‑Lite* to full is a monotone **add‑fields** operation (no retractions).

#### 5.3 The kit (constructs)

1. **Object component** `ViewObj_s` for each viewpoint (see §5.1), to make types explicit.  
2. **Viewpoint set** `Σ : FinSet(U.Viewpoint)` with declared **partial order** `⪯` for formality/refinement (default chain: `PlainView ⪯ TechCard ⪯ InteropCard`; `AssuranceLane` is **orthogonal** and not ordered with respect to others).  
3. **Emitters** `Emit_s(·) : U.Morphism → U.ViewMorph_s` (one per `s ∈ Σ`).
4. **Coherence** (laws §6) + **Pin Characteristics** policy (UnitType/ScaleKind/ReferencePlane/EditionId) for any numeric/comparable content, grounded in CHR/UNM.    
5. **Interop anchors (conceptual)** for `InteropCard` (concerns/semantics only); **any concrete schema/exchange mapping is outside Part E** (Annex/Interop).

**Result:** `MVPK(f, Σ)` returns `U.ViewFamily(f)` whose components are `Emit_s(f)`. Reindexing across `s ⪯ t` is mediated by total object‑level coercions `PromoteView[s→t]_X` (see §6.2).

#### 5.4 Intensional I/O vs Publication (normative convention)
1) **I/O are intensional.** The **Input/Output** sections of a morphism describe **intensional** data types (I/D/S) only; they do **not** depend on any publication face.  
2) **No duplication on faces.** MVPK faces **do not duplicate** I/O lists; they publish a **minimal profile**: **presence‑pins**, **CG‑Spec/CHR anchors**, and **EditionId** only.  
3) **Signature reserved to intensional.** Use **“Signature”** exclusively for intensional objects (`U.Signature`, `U.PrincipleFrame`, …). On faces, avoid “signature” and use **TechName/PlainName**.  
4) **Lawful orders, return sets.** Whenever a face shows **selection or comparison**, it **returns sets / lawful partial orders** and **never hides scalarization**; cite a **ComparatorSetRef** for any total order.  
5) **Bridge routing, penalties.** Crossings go via **Bridge + CL**; publish **Φ(CL)/Φ_plane** ids; penalties route to **R only** (never F/G).  
6) **Carrier anchoring & lanes.** On first mention, anchor carriers (**SCR/RSCR**); keep **Work occurrences** distinct from **epistemic claims** via lanes.  
7) **Publication ≠ execution.** No time/resource semantics on faces; any build/render/upload is separate **Work**.

#### 5.5 Pin & Publication characteristics (normative; never “axes”)
**Intent.** Make pinning and publication‑time measurement claims explicit, typed, and auditable without importing geometric metaphors. This section introduces **Publication characteristics** (PC) as CHR‑grounded, publication‑level facets that can legally appear on MVPK faces.

**Terminology (aligned with CHR‑MM & UNM).**
* **Characteristic** (`U.Characteristic`): a measured aspect as defined in CHR‑MM (entity/relation characteristic with a chosen **Scale**).  
* **CharacteristicSpace** (`U.CharacteristicSpace`): a CHR‑typed product of slots used by dynamics/measurement theories (A.19).  
* **Publication characteristic** (`U.PubCharacteristic`, **PC**): a **declarative facet** that a view/card/lane may expose *about a morphism* under a stated **Viewpoint**. Each PC is **backed by** CHR/CG‑Spec artifacts and **pinned** by {unit/scale/reference‑plane/edition}. PCs are **not** geometry and do **not** define “axes”.

**PC catalog (initial set).** MVPK defines a minimal open set of PCs that are frequently surfaced:
* **PC.Number** — numeric/comparable entries (thresholds, budgets, counts). **Pins required:** unit, scale, reference‑plane, edition.  
* **PC.EvidenceBinding** — bindings to evidence carriers and policies (e.g., PathSliceId, BridgeId, CL notes).  
* **PC.ComparatorSetRef** — an explicit comparator family for lawful partial orders on faces.  
* **PC.CharacteristicSpaceRef?** — optional pointer when a face needs to cite the **space** in which a claim is interpreted (e.g., dominance on a declared space).  
The catalog **MAY** be extended (see “Extensibility” below); PCs **must** remain declarative (no embedded mechanisms).

**Norms (E17‑PC).**
* **E17‑PC‑1 (CHR grounding).** Every PC that yields numeric/comparable content **SHALL** cite CHR/CG‑Spec anchors and carry pins {unit, scale, reference‑plane, edition}.  
* **E17‑PC‑2 (Lexical discipline — no geometry).** Faces and PCs **MUST NOT** use “axis”, “dimension”, or geometric metaphors; use **Characteristic**, **slot**, **CharacteristicSpace** where applicable (**E.10**; see also A.19).  
* **E17‑PC‑3 (No hidden arithmetic).** Faces **MUST NOT** smuggle aggregation/normalization; any such logic lives in **CG‑Spec** (UNM/NormalizationMethod) and is cited by **…Ref.edition**.  
* **E17‑PC‑4 (Plane & crossing).** When a PC depends on **ReferencePlane** or crosses planes/contexts, the face **SHALL** cite `BridgeId` and **CL** policy‑ids; penalties route to the **R‑channel only**.  
* **E17‑PC‑5 (Edition pinning).** PCs that rely on maps or distances **SHALL** pin `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and, if used, `CharacteristicSpaceRef.edition` / `TransferRulesRef.edition`.  
* **E17‑PC‑6 (Viewpoint scope).** Each PC instance declares the **Viewpoint** under which it is valid; promotion `PromoteView[s→t]` **MUST NOT** strengthen claims; at most, it reindexes or annotates.  
* **E17‑PC‑7 (Comparator/SetSemantics edition).** `PC.ComparatorSetRef` and any `SetSemanticsRef` **SHALL carry edition identifiers**; cards MUST be re‑emitted upon edition change with migration notes.

**Surfaces & responsibilities.**
* **PlainView** MAY include **PC.Number** iff fully pinned; otherwise it uses **compare‑only** language.  
* **TechCard** SHOULD carry **PC.Number**, **PC.ComparatorSetRef**, and **PC.CharacteristicSpaceRef?** when faces enable lawful ordering.  
* **AssuranceLane** SHALL carry **PC.EvidenceBinding** and the pins for any numeric claims it relays.  
* **InteropCard** MAY reference PCs conceptually but SHALL remain notation‑neutral in Part E (schemas map in Annex/Interop).

**Rationale.** MVPK is a publication discipline, not a measurement calculus. By naming **Publication characteristics** and pinning them to CHR/UNM, we:
1) prevent geometric leakage (no “axes”);  
2) keep publication neutral yet auditable;  
3) enable lawful set/ordering behavior on faces via explicit **ComparatorSet**;  
4) make plane/crossing obligations first‑class and checkable by declared publication checks / **OperationalGate(profile)** GateChecks.

**Extensibility.**
* **E17‑PC‑Ext‑1 (Open catalog).** New PCs MAY be added under `U.PubCharacteristic` provided they are declarative and CHR/UNM‑grounded.  
* **E17‑PC‑Ext‑2 (Kinding).** New PCs MUST declare `kind ∈ {Number, EvidenceBinding, SelectorHint, …}` and a **pinning contract**.  
* **E17‑PC‑Ext‑3 (Twin‑register names).** Supply **Tech** and **Plain** twins; avoid tokens that collide with E.10 bans; do not coin “…Space” names for publication artifacts.  
* **E17‑PC‑Ext‑4 (Edition discipline).** If a PC depends on a definitional artifact, **edition‑pin** the reference (`…Ref.edition`) and document migration rules.

**Adding invariants (procedure).**
1) Place **new invariants** for PCs in **CG‑Spec** (S‑layer), not on faces; supply acceptance tests.  
2) Version any affected **CharacteristicSpace**; publish embeddings if semantics change; never mutate slots in place.  
3) Update **AH‑3/AH‑4 (or AH‑L3/AH‑L4)** to warn/block per **E.11‑M2** red‑lines; never weaken functorial laws.  
4) **Document** edition/migration rules; extend §9 with a conformance item and provide **Lean‑profile downgrade** (advisory vs block) where applicable.

#### 5.6 Author ergonomics (non‑normative)
*Quick path for authors (three steps and a micro‑template):*
1. **Declare Σ and profile.** Choose `{PlainView, TechCard, …}` and whether faces are full or *‑Lite*.
2. **Pin once, reuse everywhere.** Attach `{UnitType, ScaleKind, ReferencePlane, EditionId}` to the arrow; cards reference these pins by ID (no duplication).
3. **Emit & verify.** Generate all faces from the arrow.

*Guidance:* treat *‑Lite* as **field‑drop only**; never add claims in *‑Lite*. 

### 6 · Laws (normative)

For any composable arrows `X —f→ Y —g→ Z` in `U`, and any `s, t ∈ Σ_viewpoints`:

1. **Functoriality & typing (per‑viewpoint).**  
    * (a) **Identity:** `Emit_s(id_X) = id_{ViewObj_s(X)}`.    
    * (b) **Composition:** `Emit_s(g∘f) = Emit_s(g) ∘ Emit_s(f)`.    
    * (c) **Typing (totality):** if `f : X → Y` then `Emit_s(f) : ViewObj_s(X) → ViewObj_s(Y)` is **total**; ill‑typed composites must be fixed via `ViewObj_s`, not by weakening laws.    
    * *Intuition:* every viewpoint acts functorially on arrows; publication does not break arrow algebra.
2. **Reindexing coherence (monotone refinement + naturality).**    
    * (a) If `s ⪯ t` then the `t`‑view **refines** the `s`‑view for the same morphism (**no content extension**; increased formality/typing only).    
    * (b) For each `s ⪯ t` there are **object‑components** `PromoteView[s→t]_X : ViewObj_s(X) → ViewObj_t(X)` natural in `X`, i.e., for every `f : X → Y`  
      `PromoteView[s→t]_Y ∘ Emit_s(f) = Emit_t(f) ∘ PromoteView[s→t]_X`.    
    * (c) **Coherence:** `PromoteView[s→s]_X = id_{ViewObj_s(X)}`, and if `s ⪯ t ⪯ u` then `PromoteView[s→u]_X = PromoteView[t→u]_X ∘ PromoteView[s→t]_X` for all `X`.         
    * *Defaults:* `PlainView ⪯ TechCard ⪯ InteropCard`.    
    * *Note:* `AssuranceLane` is **orthogonal** to the chain; it binds **evidence‑about‑claims** and MUST NOT introduce new claims **of** the morphism. 
3. **D/S sourcing & EpistemicViewing compatibility (A.7/E.10.D2, A.6.2–A.6.3, E.17.0).**    
    * (a) Inputs to `Emit_s(·)` are **existing D/S‑epistemes** about the same arrow (for example, `MethodDescription`, `MethodSpec`) produced by `Describe_ID` and `Specify_DS`/`Formalize_DS` in A.7/E.10.D2. MVPK does **not** redefine or collapse these I→D→S morphisms.  
    * (b) Each `Emit_s(·)` SHALL be realised as a species of `U.EpistemicViewing` (A.6.3) over those D/S‑epistemes: describedEntity‑preserving, effect‑free and conservative in the sense of A.6.2/A.6.3. Publication adds no new commitments beyond what is present in the referenced D/S‑epistemes.  
    * (c) Edition governance respects `U.EditionSeries`/UTS; rows remain the identity anchors for names; MVPK faces MUST be (re‑)emitted when the underlying D/S editions change.
4. **Pin discipline (Part F/G).**  
     * Any numeric/comparable content in a view SHALL pin {UnitType, ScaleKind, ReferencePlane}. **EditionId MAY be coarse at Lean profiles**; if units/scale are unknown, **declare ordinal/compare‑only** and **forbid arithmetic** until CHR pins are available.  Pins upgrade monotonically with profile and risk.
5. **No Γ‑leakage (publication independence).**  
    Publication morphisms carry **no** Γ\_method / Γ\_time / Γ_work semantics. Any build/render/upload toil is **separate Work by a system on carriers** (A.7).    
     **Lean assurance lane:** `AssuranceLane‑Lite` MAY expose only presence bits for {PathId/PathSlice?, Γ_time window?, BridgeId?}; unknowns propagate (tri‑state) with an explicit {degrade|abstain|sandbox} policy note.
6. **Carrier provenance.**  
    Every emitted view records its **SCR/RSCR ids** on first occurrence (A.7 §5.6).
7. **Isomorphism preservation.**    
    * If `f` is an isomorphism in `U`, then `Emit_s(f)` is an isomorphism in `View_s(U)`; inverses map accordingly.  
8. **Cross‑Context/plane bridging.**    
    * If a view crosses contexts or reference planes, it **SHALL** cite the **Bridge + CL policy ids** (A.7 §5.8, “Bridge routing”). Such crossings MUST be explicit on `TechCard` and `AssuranceLane`.
9. **Totality of publication morphisms.**    
    * Publication maps are total on their domains; when a composition in a view would be ill‑typed, the author **must** fix the object mapping (via `ViewObj_s`) rather than weakening functoriality or reindexing laws.
10. **PublicationScope discipline (subset & composition).**  
    * (a) **Subset law:** If a view `v` is about episteme `E` then `PublicationScope(v) ⊆ ClaimScope(E)`; if about capability `C` then `PublicationScope(v) ⊆ WorkScope(C)`.  
    * (b) **No widening by refinement:** If `s ⪯ t`, then promotion `PromoteView[s→t]` MUST NOT widen `PublicationScope`.  
    * (c) **Compositional bound:** For composable arrows `X —f→ Y —g→ Z`,  
      `PublicationScope(Emit_s(g∘f)) ⊆ PublicationScope(Emit_s(g)) ∩ PublicationScope(Emit_s(f))`.

### 7 · Structure & participants
```
                 Σ_viewpoints
                      │
            ┌─────────┴─────────┐
            │                   │
        Emit_s(·)           Emit_t(·)      … (family)
            │                   │
U :  X ──f──▶ Y ──g──▶ Z    X ──f──▶ Y ──g──▶ Z 
        U.ViewMorph        U.ViewMorph
            │                   │
        Emit_s(f),…         Emit_t(f),…
```
* **Author** chooses `Σ_viewpoints` (declared concerns + conformance rules).    
* **MVPK** emits `U.ViewFamily(f)` for each arrow `f`.    
* **Gate‑based validation** (via declared publication checks / OperationalGate(profile) GateChecks) verifies that pins/anchors/IDs are present and that MVPK laws are respected.

### 8 · Examples (SoTA‑echoing)

1. **Composite service pipeline (Interop + Assurance).**  
    `f: Parse → Normalize`, `g: Normalize → Score`.
    `InteropCard(g∘f)` is an interoperability **view** whose path set equals the **relational composition** of the two cards; `AssuranceLane(g∘f)` cites test artefacts as evidence **carriers** with edition pins. (Carriers, not semantics; concrete envelope formats are outside Part E.)
2. **Control loop morphism (Tech + Plain).**
    * For `h: Setpoint → Actuation`, `TechCard(h)` is a typed card with units; `PlainView(h)` narrates the same mapping with no new claims. (Monotone formalization echoes refinement‑typed stacks.)
3. **Optics‑style compositional views.**
    * Treat each `Emit_s(–)` as a **profunctor optic** from arrow semantics to its projection; then (by optics laws) `Emit_s(g∘f) = Emit_s(g) ∘ Emit_s(f)`. *Modern echo:* profunctor/optic literature (2017–2019) establishes precisely the kind of **compositional view** MVPK requires.  

### 9 · Conformance checklist (normative)

| ID | Requirement | Practical test |
| --- | --- | --- |
| **CC‑MVPK‑0 (Lean publication guard)** | For Lean profiles, a minimal guard runs: (i) set‑returning selection present; (ii) ReferencePlane present; (iii) any crossing cites BridgeId+CL with penalties routed to R only. | Validation report shows presence bits; penalties route to R only. |
| **CC‑MVPK‑1 (Viewpoint explicit)** | Each view declares its **Viewpoint** (stakeholders, concerns, conformance) as a publication `U.Viewpoint`. | Cards show `PublicationVPId` (or equivalent publication‑viewpoint field) and concerns. |
| **CC‑MVPK‑2 (Functoriality)** | `Emit_s(id)` is identity; `Emit_s(g∘f) = Emit_s(g)∘Emit_s(f)`. | Compose two cards and diff with the card of the composite. |
| **CC‑MVPK‑3 (No content extension)** | `PlainView`, `TechCard`, and `InteropCard` add **no new claims** beyond the underlying D/S‑epistemes. | Red‑line vs D/S episteme output (`Describe_ID`/`Specify_DS`) shows only formatting/indexing. |
| **CC‑MVPK‑4 (Pins & anchors)** | Numbers/thresholds pin {...}. **Lean exception:** at MVPK‑Min/Lite profiles, EditionId MAY remain coarse; ordinal claims are legal only as compare‑only (no means/z‑scores). | Validation shows pins present or compare‑only mode engaged. |
| **CC‑MVPK‑4b (Lean assurance)** | If `AssuranceLane‑Lite` is used, presence bits for {PathSliceId?, BridgeId?} suffice; full artefact lists are deferred. | Presence bits visible; deferred artefacts marked TODO. |
| **CC‑MVPK‑4c (I/O vs publication)** | Faces **do not** restate I/O; they carry **presence‑pins + anchors + EditionId** only. | Face inspection shows no I/O duplication. |
| **CC‑MVPK‑4d (Lawful orders)** | Any selection/comparison on faces **returns sets / lawful partial orders** with a **ComparatorSet** citation. | No hidden scalarization; ComparatorSetRef present. |
| **CC‑MVPK‑4e (Signature on faces — banned)** | The term **“signature”** is **not used** on faces; use **TechName/PlainName**. | Token scan: no “signature” on faces. |
| **CC‑MVPK‑4f (PC discipline)** | Any numeric/comparable publication uses **Publication characteristics** (PC) and carries pins {unit, scale, reference‑plane, edition}. | Cards show PC fields + pins; validation passes. |
| **CC‑MVPK‑4g (No axis/dimension)** | Faces avoid “axis/dimension/plane” metaphors except **ReferencePlane**; use CHR terms (**Characteristic/slot/CharacteristicSpace**). | Lexical check flags none; only `ReferencePlane` appears. |
| **CC‑MVPK‑4h (Edition pins on defs)** | Where maps/distances/spaces are cited, the face pins `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and `CharacteristicSpaceRef.edition?`. | Validation shows edition fields populated. |
| **CC‑MVPK‑4i (Crossings gated)** | Plane/Context crossings cite **Bridge + CL** policies; penalties route to **R‑channel** only. | IDs present; routing verified in harness logs. |
| **CC‑MVPK‑4j (PublicationScope present)** | Each view **declares `U.PublicationScope`** (USM §6.5). | Field present; presence‑bit green. |
| **CC‑MVPK‑4k (Subset‑of underlier)** | For views about epistemes/capabilities, `PublicationScope ⊆ ClaimScope/WorkScope`; reindexing **does not widen** it. | Subset witness passes; promotion diff shows no widening. |
| **CC‑MVPK‑5 (Carrier anchoring)** | First mention includes **SCR/RSCR** ids. | SCR ids visible on the card. |
| **CC‑MVPK‑6 (Γ‑separation)** | No cost/time/data‑spend on publication morphisms. | CI shows proofs/witness artefacts; gate validation passes. |
| **CC‑MVPK‑7 (Reindexing monotone)** | If `s ⪯ t`, then `Emit_s(x) ⪯ Emit_t(x)`. | `TechCard` ≤ `InteropCard` (more structure, same claims). |
| **CC‑MVPK‑8 (Surface discipline)** | Only **PublicationSurface/InteropSurface** are used; faces named …**View/…Card**. | Token scan; no “rendering/presentation” as surface kinds. |
| **CC‑MVPK‑9 (Reindexing naturality)** | Reindexing coercions `PromoteView[s→t]` exist, are total, and commute with composition. | Witness shows `PromoteView[s→t]_Z ∘ Emit_s(g∘f) = (Emit_t(g) ∘ Emit_t(f)) ∘ PromoteView[s→t]_X`. |
| **CC‑MVPK‑10 (Iso‑preservation)** | Isomorphisms in `U` remain isomorphisms under each viewpoint. | Cards show mapped inverses or an iso‑witness. |
| **CC‑MVPK‑11 (Typing & totality)** | Ill‑typed composites are rejected at `ViewObj_s` rather than weakening functoriality. | Type‑check fails early; no “best‑effort” composition in cards. |
| **CC‑MVPK‑12 (Bridge+CL on crossings)** | Any cross‑Context/plane view cites **Bridge + CL** policy ids. | IDs present on `TechCard`/`AssuranceLane`. |

### 10 · Anti‑patterns (with fixes)

1. **“Presentation logic” as semantics.**  
    *Fix:* Move any logic to `Describe_ID`/`Specify_DS` or CG‑Spec/KD‑CAL; keep views declarative; publication adds **zero** claims.    
2. **Publishing only objects.**  
    *Fix:* MVPK **acts on arrows**. Always emit views for `g∘f`, not just for objects `X, Y, Z`.    
3. **Unpinned numbers.**  
    *Fix:* Reject card; supply **pins** and CG/CHR anchors.    
4. **Viewpointless views.**  
    *Fix:* Define Viewpoint; attach concerns + conformance; re‑emit.    
5. **Interop ≡ Tech duplication.**  
    *Fix:* `InteropCard` may refine typing/shape but cannot contradict `TechCard` (reindexing monotone).    

### 11 · Consequences

| Benefit | Why it matters | Trade‑off / Mitigation |
| --- | --- | --- |
| **Arrow‑level traceability.** | Composition preserved across views enables chain‑of‑evidence on pipelines. | Slight authoring overhead → MVPK templates. |
| **Audit‑ready surfaces.** | Pins + CHR anchors make numeric claims verifiable. | Gate‑based validation performs checks. |
| **Terminology hygiene.** | Clear View vs Viewpoint, Publication vs Presentation. | Enforce L‑SURF tokens in CI. |
| **Notation independence.** | Viewpoints talk concerns, not tools. | Provide adapters to local stacks. |

### 12 · SoTA-echoing (post‑2015; conceptual pointers)

* **Profunctor/optic accounts (2017–2019).** Establish **compositional “views”** that compose like arrows—mirrors MVPK’s functorial law.    
* **Refinement‑typed ecosystems (2016→).** Units/scale at type level echo **pin discipline**.    
* **Interoperability & evidence envelopes.** External standards exist, but **their concrete formats live outside Part E** (see Annex/Interop for examples and mappings).

(References are illustrative exemplars of practice; MVPK remains notation‑agnostic.)

### 13 · Relations

* **Builds on:** A.7/E.10.D2 (Strict Distinction & I/D/S discipline), A.6.2–A.6.3 (episteme morphisms, `U.EffectFreeEpistemicMorphing` / `U.EpistemicViewing`), E.17.0 (`U.MultiViewDescribing`), E.8 (Authoring conventions), E.10 (LEX‑BUNDLE incl. L‑SURF), Part F/G (UTS, CG‑Spec, CHR pins).    
* **Constrains:** Any surface‑emitting automation; must treat publication as a species of `U.EpistemicViewing` over existing D/S‑epistemes, not as a new I→D→S mechanism.    
* **Coordinates with:** B‑operators (no Γ‑leakage), C‑cluster (selection/archives: views are publication faces, not selections), **CHR‑MM** (measurement semantics), **UNM** (normalization families).

### 14 · Minimal authoring template (E‑level)

**Header:** `MVPK v⟨edition⟩ — Σ = {PlainView ⪯ TechCard ⪯ InteropCard, AssuranceLane ⟂}`  
**For each arrow `f`:** emit `{Emit_s(f) | s ∈ Σ}` (or use the plain aliases `{PlainView(f), TechCard(f), …}`) with: **PublicationScope**, ViewpointId, pins, CHR/CG anchors, SCR ids, Bridge+CL ids (if crossing), and—if composite—machine‑checkable witnesses that `Emit_s(g∘f) = Emit_s(g)∘Emit_s(f)` **and** for each `s ⪯ t` the naturality square `PromoteView[s→t]_Y ∘ Emit_s(f) = Emit_t(f) ∘ PromoteView[s→t]_X`.

### 15 · Manager’s one‑page review (copy‑paste)

> “We publish every **morphism** under a declared **set of viewpoints** using **MVPK**. Each **view** is **functorial** (identities, composition), **adds no new claims**, and pins **unit/scale/reference‑plane/edition** with **CHR/CG** anchors. **Interop** views clarify concerns/semantics only (concrete exchange lives outside Part E); **Assurance** cites evidence carriers (SCR). Any cross‑Context/plane view cites **Bridge+CL** (Φ→R only). Publication toil is **Work on carriers**, not a mechanism change.” 


---

## E.18 **Transduction Graph Architecture** (E.TGA) · \[A]

> **Tech‑name:** **E.TGA** (pattern label)
> **Plain‑name:** Architecture of the transduction graph
> **Twin labels:** Tech / Plain per E.10; faces emitted via E.17 MVPK (no schemas in Part E). 

### 1 · Intent

Provide a **notation‑independent** architecture for graphs whose vertices are **morphisms (transductions)** and whose edges are **typed transfers**. The architecture is **agnostic to the concrete morphism set** and equips the graph with **publication, comparability, crossing, and budget** disciplines so that **flows** are **valuations over paths** within the same object. Faces appear via **MVPK**; numeric/comparable publication carries **pins** with **Bridge/CL** notes; Φ/CL^plane penalties remain in **R**.  
*Style note:* wording follows the **counterfactual register** of FPF: invariants are stated as model conditions, not deontic obligations (per E.8 style and the assignment).

### 2 · Problem frame

Teams can produce many **valid flows** over the same capability: e.g., the assignment’s reference path
`U.FormalSubstrate → U.PrincipleFrame → U.Mechanism → U.ContextNormalization (UNM) → U.SelectionAndBinding ↔ U.WorkPlanning → U.Work → U.EvaluatingAndRefreshing`
is one **path** among many possible domain paths. Without a common **graph‑level architecture**:

* flows look ad‑hoc and **non‑comparable**;
* cross‑Context **crossings** (plane/Context changes) are undocumented;
* publication surfaces **smuggle arithmetic** or restate I/O;
* set‑returning selection is silently replaced by **single scores**;
* cycles lack **budget** discipline; refresh is **out‑of‑band**.

MVPK already fixes publication drift at the **single‑arrow** level; E.TGA lifts those **publication and comparability laws** to the **graph as a whole**. 

### 3 · Problem

1. **Morphisms ≠ Graph.** A catalog of morphism‑level patterns (e.g., UNM, Selector, Work, Refresh) does not, by itself, explain **how the whole graph is built, constrained, and audited**.
2. **Flow proliferation.** Multiple “reference flows” can be authored; readers need **one orchestration** that keeps them legal and comparable **without privileging any single flow**.
3. **Unsafe publication.** Faces re‑list I/O, hide scalarization, or omit edition/plane pins; cross‑Context reuse lacks **Bridge/CL** citation; **plane penalties** leak to F/G. 
4. **Cycles without norms.** Selection↔Planning loops run without explicit **budget (Γ_time)**, **FreshnessRequest**, or **slice‑scoped** refresh; **Work** bindings are made too early (outside `U.Work`). 

### 4 · Forces

| Force                                            | Tension                                                                                                                                                                    |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Universality vs specialization**               | One architecture must host supply chains, water networks, ML functionals, and the assignment’s “first‑principles → work” path, **without** baking in any one morphism set. |
| **Publication neutrality vs auditability**       | Keep faces notation‑neutral and non‑mechanistic ↔ require **pins**, **ComparatorSet**, **Bridge/CL**, and **PublicationScope**.                                            |
| **Set legality vs business pressure for totals** | Preserve **return‑sets / lawful partial orders** ↔ stakeholders demand single numbers.                                                                                     |
| **Cross‑Context reuse vs safety**                | Enable reuse across `U.BoundedContext` ↔ enforce **Bridge/CL** with **R‑only penalties**.                                                                                  |
| **Agility vs reproducibility**                   | Permit evolving CG‑Spec/UNM/Comparator editions ↔ require **edition pins** and **re‑emission** on change.                                                                  |
| **Cycles vs convergence**                        | Allow Selection↔Planning iteration ↔ impose **budget** and **slice‑scoped** refresh to prevent thrash.                                                                     |

### 5 · Solution — the E.TGA kit (graph model + choreography)

#### S1 · Graph object (conceptual)

Define a **typed, editioned, directed multigraph**
`TransductionGraph := (V, E, τ_V, τ_E, Γ_time, Bridge, CL, TransportRegistry^Φ)`
with:

* **Vertices `V`:** instances of `U.Morphism` (open world). Common specialisations **include but are not limited to** the assignment’s set: `U.FormalSubstrate`, `U.PrincipleFrame`, `U.Mechanism`, `U.ContextNormalization (UNM)`, `U.SelectionAndBinding`, `U.WorkPlanning`, `U.Work`, `U.EvaluatingAndRefreshing`. This list is **illustrative**, not exhaustive—the graph **does not depend** on this particular set.
* **Edges `E`:** a **single edge kind `U.Transfer`** (typed) carrying artifacts/tokens; all **plane/Context/edition** changes occur **only at nodes via `OperationalGate(profile)`** with **Bridge + CL** annotations; penalties **→ R only**. Transport conversions pin **Φ‑policies** and editions.
* **Scopes:** `Γ_time` (budgets, horizons), `PublicationScope` for faces (E.17), and **slice ids** for refresh (G.11).

 **CtxState (PS‑projection; closed slots):** `CtxState = ⟨L, P, E⃗, D⟩` is the **projection of E.17 Publication Scope**.
 **Slot definitions (normative):**
  • `L := Locus` — an element of a partially ordered **ContextSlice** poset; addresses *where* claims apply (disciplinary / organizational / holonic slice).
  • `P := ReferencePlane` — the reference plane/units registry id; **no plane/unit declarations or translations** occur in CV; crossings remain gated (A.21).
  • `E⃗ := Edition vector` — a **partial map** `edition_key ↦ EditionId` over named families `{CG‑Spec, ComparatorSet, UNM.TransportRegistryΦ}` and optional `{DescriptorMapRef, DistanceDefRef, CharacteristicSpaceRef}` when cited.
  • `D := DesignRunTag` — `design(T^D)` or `run(T^R)`, used by **LaunchGate** and acceptance/telemetry duties.
 **Invariants.** Raw `U.Transfer` does **not** mutate `⟨L,P,E⃗,D⟩`; any change or entry to `U.WorkEnactment` occurs at `OperationalGate(profile)`.
 **Extension discipline.** Any extra slot beyond ⟨L,P,E⃗,D⟩ **SHALL** be registered in the **E.17/LEX “CtxState Extension Registry”** with slot‑id, intent, partial‑order law (neutral/absorbing), and SquareLaw compatibility; unregistered extensions are non‑conformant.
 **Data‑shape location.** Concrete record shapes for `PathId/PathSliceId`, Γ‑pins, and lineage remain in A.22 `FlowSpec`; E.TGA fixes that **flow = valuation** and that `CtxState` is preserved across raw transfers.

 * **Kinds:** `U.Transduction(kind∈{Signature, Mechanism, Work, Check, StructuralReinterpretation})`.  
  **Exact identification (no TGA‑local taxonomy):**  
  — `Signature` **≡** **A.6.0** `U.Signature` (universal, law‑governed declaration).  
  — `Mechanism` **≡** **A.6.1** `U.Mechanism` (law‑governed application over a SubjectKind/BaseType).  
  — `Work` **≡** **A.15** `U.WorkEnactment` (bind‑in‑world; `FinalizeBinding` only here).  
  — `Check` **≡** `OperationalGate(profile)` (universal **gate**; A.* patternisation pending; CC‑TGA catalog applies).  
  — `StructuralReinterpretation` **≡** a species of **A.6.4** `U.EpistemicRetargeting` used as a graph node in E.TGA. **All retargeting semantics** (slot‑level discipline, `DescribedEntitySlot`/`GroundingHolonSlot` behaviour, invariants, Bridges, witnesses) come from **C.2.1** and **A.6.2–A.6.5**; E.TGA does **not** introduce a TGA‑local variant of retargeting.  
  `OperationalGate ≔ U.Transduction(kind=Check)` with DecisionLog aggregation.  
  The only extra discipline E.TGA adds for `StructuralReinterpretation` is **graph‑local**: CtxState and GateCrossing behaviour are governed by **CC‑TGA‑06‑EX** and **CC‑TGA‑11** (projection‑preserving w.r.t. `⟨L,P,E⃗,D⟩`, PathSlice‑local, and “no plane/unit change without a gate”). 

> **MVPK binding (import).** Every vertex with an external surface is published via **MVPK** faces (`PlainView`, `TechCard`, `AssuranceLane`, `InteropCard`) under a declared **PublicationScope** (E.17). E.TGA **reuses** MVPK’s publication laws (pins, lawful‑order discipline, “no new numeric claims / no I/O re‑listing”) and only adds graph‑level constraints in S3 and **CC‑TGA‑09/10**; it does **not** define a second, local publication semantics. 

**GateCrossing (normative)**
**Definition.** A **GateCrossing** is the typed transition at a node that changes any of:
  (i) `U.BoundedContext` (**Context**), (ii) **ReferencePlane**, (iii) any member of the **Edition vector** `E⃗` (e.g., `CG‑Spec`, `ComparatorSet`, `UNM.TransportRegistryΦ`, `DescriptorMapRef`, `DistanceDefRef`, `CharacteristicSpaceRef`), (iv) **DesignRunTag** (`T^D↔T^R`), or (v) **Kind/describedEntity** (only under `StructuralReinterpretation` subject to **CC‑TGA‑06‑EX**).
**Invariants.** Raw `U.Transfer` preserves `CtxState`; a GateCrossing occurs at exactly one `OperationalGate(profile)` (SquareLaw applies).
**Required pins (minimum).** `BridgeCard + UTS row`; `CL` for scope bridges; `CL^plane` for plane crossings; `CL^k` with `bridgeChannel=Kind` for kind transitions; `PublicationScopeId`; `PathSliceId`; Γ‑pins on compare/launch faces.
**Canonical reference.** `CrossingRef := ⟨GateId, channel, from, to, UTS.RowId, PathSliceId⟩`. Any DecisionLog entry whose rationale depends on a crossing **SHALL** cite `CrossingRef`.
**Term separation.** **Transfer** denotes the sole edge kind `U.Transfer` (graph edges). **Transport** denotes Φ‑governed conversion **policies/registries** (**`TransportRegistry^Φ`** under UNM). Wording “reuse via Transport” refers to registries/policies, not to an additional graph edge.

#### S2 · Flows as valuations (paths + state + guards)
* A **Flow** is a **valuation** `ν` over `U.Transfer` edges and cut‑sets, paired with an **admissible path** `p = v₀ → … → v_k`. The valuation assigns tokens/states under `CtxState` and records publication events under a declared `PublicationScopeId`. **The concrete pins and identifiers (`PathId`, `PathSliceId`, Γ_time on compare/launch faces) are specified in A.22 `FlowSpec` and A.25 `Sentinel & SubFlow`.** This reflects the “graph ≠ flow” norm (flow = valuation), with gates placed exactly on GateCrossings.  
* **Admissible path (definition).** A path `p` is **admissible** iff:  
  (a) node/edge types match the declared `τ_V, τ_E`;  
  (b) any change to `⟨L,P,E⃗,D⟩` (or kind‑retargeting under `StructuralReinterpretation`) appears at **exactly one** `OperationalGate(profile)`;  
  (c) each GateCrossing on `p` has a **SquareLaw witness** (CC‑TGA‑23) and, where applicable, a **SquareLaw‑retargeting witness** (CC‑TGA‑06‑EX);  
  (d) no hidden crossings occur across raw transfers;  
  (e) Γ‑pins are present on compare/launch faces;  
  (f) `T^D↔T^R` occurs **only** at `LaunchGate`.

* `U.Transfer` preserves `CtxState` (`⟨L,P,E⃗,D⟩`) and carries **Assurance‑operations** only (see S3b); any crossing of locus/plane/editions or `T^D↔T^R` is placed at `OperationalGate(profile)`.
* A **PathSlice** is a **slice‑scoped execution window** used for refresh/telemetry; faces pin `PathSliceId`; **re‑emission** happens when any pinned edition changes or `SliceRefresh` is triggered by sentinel rules.

> **Consequences.** The assignment’s “reference flow” is simply one `p` in `TransductionGraph`. Other domains (supply chain, water network, NN functional) instantiate different `p` on the **same architecture**.
> 
**Why "flow = valuation" doesn't kill the "something is flowing" intuition**
There are two complementary perspectives:
* **Lagrangian (intuitive):** "water particles" run through pipes; you "track" tokens.
* **Eulerian (architectural):** you define a **function on edges** ("how much/what passes through each edge under a given regime"), with gate laws. E.TGA deliberately fixes the **Eulerian semantics of flow** at the architectural level: "flow (= valuation) + publication log", while the dynamics of "movement" show up as **re-valuation** over a **PathSlice** (the execution/republishing window) under gate rules and the SquareLaw. This yields comparability, reproducibility, and slice-local refresh.

#### S3 · Publication discipline (faces)

E.TGA **imports E.17** wholesale **and binds MVPK to `PublicationScope` (USM)**.  
**MVPK remains the normative source** for:
* the set of face kinds (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`),
* pin discipline and Publication Characteristics (PC),
* “no new numeric claims / no I/O re‑listing / no Γ‑semantics on faces”.

E.TGA **does not re‑specify** these laws; it only adds **graph‑level obligations** for faces emitted over transduction paths:

1. **Crossings on faces.** When a face participates in a GateCrossing (S1.b/S9), it **SHALL** cite `BridgeId + UTS row + CL` and publish **Φ(CL)/Φ_plane RuleId**; **penalties remain in R‑lane**.
2. **Gate‑requirement on cited editions.** Any face that references editions of `CG‑Spec` / `ComparatorSet` / `UNM.TransportRegistryΦ` includes **`BridgeCard + UTS row`**; faces without this are treated as **non‑consumable downstream**.  (delegated tests → A.27/A.34)  
3. **ComparatorSet & set returns (graph‑scope).** Any `ComparatorSet` and `SetSemanticsRef` used along a transduction path **SHALL** carry **edition identifiers**; flows **re‑emit** faces on edition change; faces with comparison **return sets / lawful partial orders** (no hidden scalarization), reusing MVPK’s lawful‑order discipline.
4. **Γ_time on compare/launch faces.** All compare/launch faces on E.TGA paths pin `Γ_time`; implicit *latest* is illegal. The **shape and evaluation** of `Γ_time` live in A.26; E.TGA only mandates presence. **CHR avoids acceptance thresholds** (*NoThresholdsInCHR*); thresholding and launches surface in G‑patterns and `U.Work`.  (delegated tests → A.32/A.33). **Unknowns remain tri‑state (`pass|degrade|abstain`) and fold per GateProfile (A.21/A.26).**  

> **Reminder.** MVPK already bans “signature” on faces, I/O re‑listing, arithmetic on faces, and unpinned numeric content (E.17 §5.4–5.5). E.TGA **does not weaken or override** those rules; it only constrains how they are used along transduction paths.

**Lean publish‑mode (AssuranceLane‑Lite).** Lean affects **faces only** (`PlainView`/`AssuranceLane` minimal), not checks; publication shows `GateProfile`, `GateCheckRef[]`, and `DecisionLogRef`; the underlying GateChecks list remains unchanged.

**Decision stability & idempotency (delegated).** Gate decisions are **idempotent** under a congruence relation over inputs; the **witness and equivalence criteria** are specified in **A.41 DecisionLog**. E.TGA **does not** prescribe storage formats, key shapes, or hashing schemes.

**KindBridge admissibility (publication).**  
Treat a step as a **describedEntity/kind** transition (including `StructuralReinterpretation` under CC‑TGA‑06‑EX) **iff** the **UTS row**:
  — satisfies the **minimal Bridge row** obligations of A.27 (identity, `ReferencePlane`, `CL/CL^plane`, edition‑pins for `CG‑Spec` / `ComparatorSet` / `UNM.TransportRegistryΦ`, `ComparatorSetRef`, `BridgeId`, `Φ‑RuleIds`), and  
  — is additionally marked as a **KindBridge** per C.3 (`bridgeChannel=Kind`, `CL^k`, mapping or signature‑translation, order‑preservation claims, loss notes, definedness area, determinism).  
Otherwise this KindBridge explanation does not apply (the step falls back to a gated crossing). When the gate owns the crossing, `CrossingRef` is surfaced and linked from the `DecisionLog`.

#### S4 · Assurance‑operations on `U.Transfer` (counterfactual admissibility)
On `U.Transfer` edges, an operation is interpreted as a **declarative assurance‑operation** **iff** it is one of  
`ConstrainTo(rule)` · `CalibrateTo(map|standard)` · `CiteEvidence(anchor)` · `AttributeTo(agent|role)`; otherwise this explanation does not apply.
Under this interpretation, `CtxState⟨L,P,E⃗,D⟩` is preserved.  
If an effect entails a plane/unit change, the assurance‑operations explanation does not apply and the step is handled as a gated crossing (`OperationalGate(profile)+Bridge+UTS`).  
If Φ assigns penalties, they appear in the R‑lane; otherwise no penalties are surfaced here.

#### S5 · Comparability & aggregation (normalize‑then‑compare; counterfactual form)

The comparison explanation applies under the following admissibility conditions:

* If a path segment intends to compare/aggregate, it is admissible as a comparison **only when** UNM precedes it; UNM is **method‑independent**, publishes **TransportRegistry^Φ** and **CG‑Spec** anchors, and faces cite those editions; otherwise this comparison explanation does not apply.
* If the comparator defines a **lawful partial order**, then returns are **sets/archives** (Pareto/Archive); if a **total order** is declared, it is the one provided by the comparator; otherwise set semantics apply and covert scalarization is out of scope here.
* If a claim is **ordinal‑only**, then only comparisons are surfaced; arithmetic transforms (e.g., means/z‑scores) are out of scope of this explanation and belong to declared comparators or downstream policy.

**Edition‑aware artifacts (e.g., QD archives) MUST pin `DescriptorMapRef.edition` / `DistanceDefRef.edition` (and `CharacteristicSpaceRef.edition` when applicable); refresh is slice‑local.**  (delegated tests → A.34/A.37)  

#### S6 · Cycle discipline (Selection ↔ Planning)

* The architecture centers the loop between `U.SelectionAndBinding` and `U.WorkPlanning`.
* The loop operates under a local **budget / max_iter** in `Γ_time`; at expiry, the selector emits the **current `CandidateSet`** and **`MethodTuning`** with a **partial‑optimality** flag; further improvement rolls into the **next `PathSlice`**.
* **UNM occurs before the loop**; if measurements are missing/stale, UNM emits a **FreshnessRequest** which is **planned** in `U.WorkPlanning` and **executed** in `U.Work`. Transfers, units, and calibrations are surfaced publication‑wise as `CalibrateTo(map|standard)` and pinned to `TransportRegistry^Φ` (**R‑channel only** for penalties).
* **WorkEnactment is the only binding site** for launch values (`FinalizeBinding / BindLaunchValuesOnly`). 
> **Refresh orchestration.** Telemetry from `U.WorkEnactment` and publications are **slice‑scoped**, editions re‑pinned, faces **re‑emitted**. 

#### S7 · Selector semantics (G.5) & parity harness (G.9)

* **Selectors return sets.** Default **DominanceRegime** is `ParetoOnly`; **Illumination/coverage** are **gauges** (reported), excluded from dominance **unless** policy escalates via CAL.
If `PortfolioMode=Archive`, a **QD archive** may be returned; when generation is in scope, pairs `{environment, method}` are managed under declared **EnvironmentValidityRegion** and **TransferRulesRef**; parity artefacts and `PathSliceId` are pinned on publication. Details of comparator semantics and archive pinning live in **A.28/A.34**.

#### S8 · Guard ownership and handling (USM §1.2)
* **USM.CompareGuard**/**USM.LaunchGuard** **publish `GuardOwnerGateId`**. Guard failures are **events** aggregated by the owner gate (not GateChecks).
* **Ownership rules:** (i) `USM.LaunchGuard.owner = LaunchGateId(U.WorkEnactment)`; (ii) inside a Subflow, `USM.CompareGuard.owner = OperationalGate(InSentinel)`; Join‑nodes cannot own guard pins.

**GateProfile data shape (cross‑reference).** The **entire data shape** (SoD/quorum, declassify, budgets, TOCTOU/freshness windows, editions vector, scopes) is **specified in A.26**. E.TGA **only names** the structure and defers its fields to A.26.

**Bridge‑aware guards (cross‑reference).** USM guards apply bridge‑translation semantics (`translate(Bridge, Scope)`) with CL penalties in R‑lane; the conceptual macro is defined in **A.24 USM.Guards**.

**Error/timeout/unknown (profile‑bound).** GateCheck errors/timeouts fold to **`degrade`** under `Lean|Core` and to **`block`** under `SafetyCritical|RegulatedX`; `unknown` follows the GateCheck’s intensional rule (safety‑default: `degrade`). **The DecisionLog shape and the idempotency witness are defined in A.41; E.TGA does not define storage or key structures.**  

#### S9 · Transport & crossings
* Cross‑Context or cross‑plane edges appear as **GateCrossings** that include a **Bridge** with **CL** policy; **Φ(CL)/Φ_plane** are published; penalties route **to R only**; **Scope membership** (USM) is unchanged by crossings. **SquareLaw is checked within a single `DesignRunTag`; a `T^D↔T^R` change is modelled as a pair of coordinated gates with `DesignRunTagFrom/To` and an external enactor (see A.29).** 
* When *describedEntity/kind* changes across a boundary, declare an explicit **KindBridge (`CL^k`)** in addition to plane/context CL; cross‑context reuse of UNM **must** go via `Transport`, with any `CL^plane` penalties routed to **R‑lane** only.

#### S10 · Non‑mechanism boundary

* Publication is a **typed projection**, not execution. Any build/render/upload is **Work on carriers**; **no Γ‑semantics** may leak into faces. 

#### S11 · Coordination thread (optional)
Introduce **CoordinationFlow** as a named thread laid over `U.TransductionFlow__P2W`; crossings with production flow go via **Bridge+UTS**; coordination publishes **LexicalView** labels only and adds **no checks** or mechanisms.

### S12 · Viewpoint families → E.TGA constructs (neutral, holonic)

E.TGA does not mint new viewpoint or view kinds. It **imports** the generic multi‑view machinery of E.17.0 `U.MultiViewDescribing`, bundles from E.17.1, and the TEVB engineering bundle from E.17.2. S12 only describes how these existing `U.Viewpoint` / `U.ViewpointBundle` ids are *used* in transduction graphs and in `UTS.ViewpointMap`; intent/concern semantics live in E.17.0–E.17.2.

**Two‑layer use of TEVB and MVPK (ISO 42010 summary, no local re‑definition).**

* **Engineering viewpoints.** For engineering holons, E.TGA assumes a TEVB bundle with `ViewFamilyId = VF.TEVB.ENG`. `EngineeringVPId` is one of `{VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}`, and TEVB is the normative source for their semantics. E.TGA does not refine these viewpoints.  
* **Publication viewpoints.** Publication viewpoints come from MVPK (E.17); `PublicationVPId` is a `MVPK.ViewpointId` that governs faces under a `PublicationScope`.  
* **Architecture description.** Under ISO 42010, an architecture description for a holon is: (i) an E.TGA transduction graph over that holon, plus (ii) MVPK faces emitted for its morphisms, with correspondences per E.17.0 linking each face to the engineering view(s) it implements. Crossings and penalties follow E.TGA’s gating rules (S9; CC‑TGA‑11/23) but do not change viewpoint semantics.  
* **Separation of roles.** `VP.*` from TEVB are **EngineeringVPId** values only; they are not surfaces. `PublicationVPId` values live in MVPK. The mapping between them is entirely via ISO‑style correspondences and the `UTS.ViewpointMap`; E.TGA does not define a second notion of viewpoint.

**Entities‑of‑interest (summary).**

* **EoI‑ENG.** The engineering entity described by TEVB/E.TGA is a holon (`U.System` or `U.Episteme`) per TEVB’s `EoIClassSpec`. E.TGA does not broaden or narrow this set.  
* **EoI‑PUB.** MVPK may treat the *architecture description* itself as an entity‑of‑interest; publication viewpoints for that AD are defined in MVPK, not here. E.TGA only requires that such faces honour MVPK discipline and E.TGA’s crossing rules.

**Naming rules (aligned with E.17.0/E.17.1/E.17.2).**  
* `ViewFamilyId` is the `U.ViewpointBundle.viewFamilyId` (e.g. `VF.TEVB.ENG` for TEVB); its lexical and ontological discipline is governed by E.17.1.  
* `EngineeringVPId : ViewpointId` is always a `U.ViewpointId` drawn from some bundle (for TEVB, one of `{VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}`). E.TGA never defines new `VP.*` ids.  
* `PublicationVPId : ViewpointId` is a `MVPK.ViewpointId` defined in E.17; TEVB viewpoints are **never** reused as publication viewpoints (per TEVB guard and MVPK).  
* The legacy unqualified column name `ViewpointId` MUST NOT be used. Where it exists, it is interpreted as `PublicationVPId` and is DEPRECATED (sunset when E.23 is published).

**Terminology guards (no local semantics).**
* Within S12, “viewpoint”, “view” and “correspondence” have exactly the meanings given in E.17.0; “publication surface” means an MVPK face (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`) under some `PublicationVPId`.  
* Faces are **carriers for views**: a face is part of a view only when linked via an ISO‑style `CorrespondenceRef` to an engineering `U.View` under some `EngineeringVPId`; S12 does not add extra conditions beyond E.17.0/E.17.2.  
* Labels such as “Functional view”, “Procedural view”, “Role‑Enactor view”, “Module‑Interface view” in this section are lexical aliases for TEVB viewpoints; they MUST NOT be interpreted as extra viewpoint kinds or as surface types.

**Purpose.** Provide a neutral (F.18) mapping from TEVB engineering *viewpoint families* — bundle `VF.TEVB.ENG` with `VP.Functional / VP.Procedural / VP.RoleEnactor / VP.ModuleInterface` — to E.TGA constructs so that the same holon can be described functionally, procedurally, structurally, or as a module‑and‑interface architecture **without changing the underlying graph**. S12 does not introduce new `U.Viewpoint` or `U.View` kinds; it reuses those defined in E.17.0/E.17.2.

**Holon target.** The mapping applies to any holon, with the constraint that only `U.System` enacts `U.Work` (A.3/A.15). Supervisory and structural hierarchies remain distinct (B.2.5).

**Viewpoint family → primary E.TGA constructs (TEVB‑aligned)**  
*All four families referenced below are TEVB engineering viewpoints; the “what …” clauses are interpretive glosses for how they *use* E.TGA constructs. Formal intent/concerns/allowed episteme kinds remain in TEVB (E.17.2).*
1) **Function‑Oriented View (`EngineeringVPId = VP.Functional`, capability‑flow)** — “what transformation is achieved under roles”
    * **Flow substrate:** `U.TransductionFlow__P2W` through nodes `Signature → Mechanism → UNM → SelectionAndBinding ↔ WorkPlanning → Work → EvaluatingAndRefreshing`.
    * **Publication:** MVPK publication surfaces per E.17; comparable claims pin to `CG‑Spec/ComparatorSet` editions; crossings surface via `Bridge+UTS` and `CL/CL^plane` (penalties → **R‑lane** only). 
    * **Checks:** A.20 (CV) inside transformations; A.21 (GateFit) at gates; enforce CSLC/No‑Hidden‑Scalarization per A.28. 
    *  **Holonic note:** `U.Episteme` does not *act*; it is used by systems acting on carriers; `U.Work` appears only for `U.System`. 
2) **Procedure‑Oriented View (`EngineeringVPId = VP.Procedural`, step/time storyboard)** — “what steps occur and when”
    * **Artifacts:** `U.WorkPlan` (A.15.2) for intent/schedule; `U.WorkEnactment` for enactment.
    * **Boundary:** entry into `U.WorkEnactment` is via `OperationalGate(profile)` with `USM.LaunchGuard`; `DesignRunTag` separates design time from run time; `DesignRunTagFrom/To` appear only at gates. 
    * **Holonic note:** Applies to any `U.System` scope (single holon or a supervised sub‑holon cluster); supervisory layering is handled by roles rather than structural mereology (B.2.5).
3) **Role‑Enactor / Device‑Structure View (`EngineeringVPId = VP.RoleEnactor`)** — “what carrier/ports/constraints exist; who typically enacts it”
    * **Artifacts:** Module *interfaces* are `Signature` nodes; module realizations are `MechanismRealization` nodes; inter‑module dependencies traverse `U.Transfer`, with gates on crossings. 
    * **Publication:** MVPK faces are **typed projections**, not executable artifacts; faces add **no new numeric claims** (E.17). Constraints and compatibility appear as CV checks (A.20). 
    * **Holonic note:** Structural mereology (part/whole of the carrier) is modeled in Part A; E.TGA binds interface/exposure semantics to morphisms and gates.
    * **Device‑View reading (Transduction↔Transductor).** The same capability‑flow MAY be read as a **device** that performs the transduction (**transductor**) without changing the graph: model with `Signature` + `Mechanism` only; do **not** introduce extra edge kinds. If describedEntity retargets (function↔element), use `StructuralReinterpretation` with a **`KindBridge (CL^k)`** on **UTS** and a **SquareLaw‑Retargeting witness**; preserve `⟨L,P,E⃗,D⟩` and treat it as a non‑crossing (**CC‑TGA‑06‑EX**; witness shape §4.7).  
    * **Role‑label guard.** `TypicalEnactorRoleName` is **pedagogical only** and MUST NOT be used as a GateFit role; GateFit uses `U.Role` (A.21).
4) **Module‑Interface View (`EngineeringVPId = VP.ModuleInterface`, physical/logical architecture)** — “what modules exist and how they contract across interfaces”
    * **Artifacts:** Module *interfaces* are `Signature` nodes; module realizations are `Mechanism` nodes; inter‑module dependencies traverse `U.Transfer`, with gates on crossings. 
    * **describedEntity note:** Functional↔element reinterpretation follows the **Device‑View reading** rule above (Role‑Enactor family) and **CC‑TGA‑06‑EX**; see **§4.7** for the retargeting witness shape and CV witness binding.
    * **Holonic note:** The same module may appear as a holon in multiple views; supervisory loops (B.2.5) remain orthogonal to structural composition.
This is an expandable list of viewpoint families; TGA is intentionally viewpoint‑neutral. Additional engineering bundles beyond TEVB (safety, mission, information, …) are introduced as separate `U.ViewpointBundle` species via E.17.1/E.17.2; S12 does not define them.

**Alias families for transduction species (LEX‑only).**
*Scope.* Authors MAY declare `AliasesInViewFamilies[]` for `U.Transduction` species so readers can recognise familiar engineering view families. All semantics come from the referenced bundles (typically TEVB) and MVPK; aliases are purely lexical.

*Norms.*
1. Each `U.Transduction` species MAY publish `AliasesInViewFamilies[]` — an open list of records  
   `{ ViewFamilyId, EngineeringVPId?, Alias : TechASCII }`.  
   * If `ViewFamilyId = VF.TEVB.ENG`, then `EngineeringVPId` MUST be one of `{VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}` (TEVB; CC‑TEVB‑1/6).  
   * Other `ViewFamilyId` values MUST denote `U.ViewpointBundle` instances defined elsewhere (e.g. safety/assurance/information bundles), not ad‑hoc local families.
2. Aliases are LEX‑only: **no arithmetic, no new claims, no check participation, no `CtxState` or `DesignRunTag` change**. They do not create MVPK faces.  
3. Aliases MUST NOT be used as `PublicationVPId`; publication viewpoints remain in MVPK.  
4. Twin registers are allowed (Tech/Plain) per E.10; naming follows F.18 local‑first discipline.  
5. Do not name transductions by operands/effects (operation ≠ operand).  
6. `TypicalEnactorRoleName` MAY be added for pedagogy; it SHALL NOT be used as a GateFit role (GateFit uses `U.Role` only).  
7. Morphology: ASCII TitleCase; conjunctions via `And`; for composite actions use `XingAndYing` (or `XAndYing` if grammar requires).  
8. The P2W reference species table (SubstrateFormalization … EvaluatingAndRefreshing with functional/procedural aliases and `TypicalEnactorRoleName`) is **informative** and does not change kind or viewpoint semantics.

**Deliverable — `UTS.ViewpointMap` (normative, TEVB‑aligned).**  
Publish a UTS block named `ViewpointMap` that ties engineering viewpoints (from bundles such as TEVB) to E.TGA constructs and MVPK faces.

*Minimum row schema (per row).*
* `ViewFamilyId` — `U.ViewpointBundle.viewFamilyId` (e.g. `VF.TEVB.ENG` for TEVB, or another bundle id).  
* `EngineeringVPId : ViewpointId` — a viewpoint from that bundle (for TEVB, one of `{VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}`).  
* `PublicationVPId : ViewpointId?` — MVPK publication viewpoint id that governs faces implementing this engineering view (optional if not publishing).  
* `TargetHolon ∈ {U.System, U.Episteme}` *(extended species may add `{U.Service|U.MethodFamily}`; if `TargetHolon ≠ U.System`, no `U.Work` enactment appears).*  
* `PrimaryTGAConstructs` — nodes/edges/gates actually used for this `(ViewFamilyId, EngineeringVPId, TargetHolon)` (typically one of the four families above).  
* `Crossings{BridgeId, CL/CL^plane?}` — crossings involved; penalties route to R‑lane only.  
* `EditionPins{…}` whenever comparable claims appear (bind to CG‑Spec/ComparatorSet editions; any face citing editions includes `BridgeCard + UTS` row per MVPK/UNM).  
* `SenseCells[]` (≥ 2 per row), each citing Context name + edition (F.17/E.10 discipline; UTS‑wide coverage rules still apply).  
* *(REQUIRED when publishing)* `CorrespondenceRef[]` — ISO 42010 correspondences linking emitted faces to the engineering view(s) they implement; may cross architecture descriptions.  
* *(RECOMMENDED)* `ConcernsCovered[]` — ISO 42010 stakeholder concerns addressed by this row via GateProfiles/check catalogues.

**Conformance (S12‑scoped).**  
(i) `UTS.ViewpointMap` exists.  
(ii) For each holon that claims TEVB alignment, there are ≥ 4 rows whose `{ViewFamilyId, EngineeringVPId}` cover `{VF.TEVB.ENG × {VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}}` (per CC‑TEVB‑1/6).  
(iii) Rows that surface editions also include `BridgeCard + UTS` rows per A.27; edition‑bearing faces that lack such rows MUST NOT be used for downstream consumption.  
(iv) Each row has ≥ 2 `SenseCells` and the sheet meets global UTS coverage rules.  
(v) Any `TargetHolon = U.System` that reaches `U.Work` shows `LaunchGate` with `DesignRunTag` consistency.  
(vi) Crossings referenced in `ViewpointMap` follow CC‑TGA‑11; comparability along the mapped paths follows CC‑TGA‑10.  
(vii) Rows MUST NOT use an unqualified `ViewpointId`; they MUST use `EngineeringVPId` and/or `PublicationVPId` explicitly.  
(viii) When faces are published, `CorrespondenceRef[]` MUST be present and resolvable to `U.Viewpoint` ids.  
(ix) Additional bundles (e.g. assurance, information, mission) MAY appear as extra `ViewFamilyId` values but MUST be declared as `U.ViewpointBundle` species; they do not extend `VF.TEVB.ENG`.

### 6 · Archetypal Grounding (Tell–Show–Show; concise)

*Show‑A (Supply chain).* Nodes: procurement → inbound QC (UNM) → selection (supplier set; lawful order) ↔ planning (lotting/schedule; budget) → execution (receipts; **WorkEnactment binds**) → refresh (quality telemetry; re‑emit faces). Crossings: vendor Context via **Bridge/CL**; penalties **→ R only**; comparators pinned to CG‑Spec edition. 

*Show‑B (Neural‑net functional).* Nodes: formal substrate (typed tensor ops) → mechanism (combinator algebra) → UNM (dataset normalization; **TransportRegistry^Φ**) → selection (architecture/hyperparam set; Pareto set over accuracy@ratio & FLOPs@ratio) ↔ planning (compute budget horizon) → Work (training runs; Δ anchored) → refresh (parity inserts; slice‑scoped). Faces pin **DescriptorMapRef.edition / DistanceDefRef.edition** when QD metrics are shown; illumination remains a **gauge** by default. 

> *Post‑2015 SoTA echoes (illustrative):* **TAMP/MPC**, **MAP‑Elites / QD (incl. CMA‑ME)**, **refinement‑typed stacks**, **profunctor optics**. **Worked‑examples and Tell–Show–Show vignettes move to A.31/A.34/A.37; E.TGA keeps only the carcass‑level alignment.**

### 7 · Conformance — **Unified checklist (normative)**

| ID | Requirement | Practical test |
|----|-------------|----------------|
| **CC‑TGA‑01 — Single edge kind** | The graph uses exactly one edge kind `U.Transfer`; all plane/Context/edition transitions occur only at nodes via `OperationalGate(profile)`. | Model lint finds no auxiliary edge kinds for unit/plane changes; crossings sit on declared gates. |
| **CC‑TGA‑02 — Nodes are morphisms** | Nodes are intensional `U.Transduction(kind∈{Signature,Mechanism,Work,Check,StructuralReinterpretation})`. This enumeration is a **minimal roles baseline**. **Domain‑specific species are open‑world** and non‑exhaustive; they bind to one of these kinds. Adding a **new kind** requires an explicit E.TGA update. `StructuralReinterpretation` nodes are **projection‑preserving** (no mutation of `⟨L,P,E⃗,D⟩`) and carry CV/GF obligations per A.20/A.21/A.45. **Mapping to A.\*** (normative): the enumeration is **not** a TGA‑local taxonomy; each `kind` is identified 1‑to‑1 with its A.\* anchor: `Signature→A.6.0`, `Mechanism→A.6.1`, `Work→A.15`, `Check→OperationalGate` (until a dedicated A.\* pattern is published). **Disambiguation:** `Signature (kind)` ≠ `KindSignature` (C.3.2) and ≠ `A.6 Architheory Signature` view. | Type registry shows at least the listed kinds; additional species map to one of them; checks realized as `OperationalGate` (see CC‑TGA‑06‑EX/11). **Lint:** registry/table exposes `{species → {kind, KindDefinition}}`; missing or mismatched `KindDefinition` fails. |
| **CC‑TGA‑03 — Identity, composition, functorial faces** | Identities exist; path composition associative; publication is functorial: `Emit_s(t₂∘t₁)=Emit_s(t₂)∘Emit_s(t₁)`. | Pick two‑step path; MVPK faces commute (Square witness). |
| **CC‑TGA‑04 — Graph spec** | Spec declares `τ_V, τ_E`, `Γ_time`, Transport/Bridge registries. | Spec file shows typed registries and Γ policy. |
| **CC‑TGA‑05 — CtxState pins** | `CtxState=⟨L,P,E⃗,D⟩` is pinned on ports/tokens; raw `U.Transfer` does **not** change it. | Along a raw transfer, ⟨L,P,E⃗,D⟩ is preserved. |
| **CC‑TGA‑06 — Operational gates only** | Any change in ⟨L,P,E⃗,D⟩ or entry into `U.WorkEnactment` is mediated by `OperationalGate(profile)` with aggregated `DecisionLog`. | Diff CtxState across edges; if changed, exactly one gate exists with DecisionLog. |
| **CC‑TGA‑06‑EX (strictly limited) — Projection retargeting without gate** | A node of kind **`StructuralReinterpretation`** MAY retarget the **published projection** without invoking `OperationalGate` **only if all hold**: **(a)** `⟨L,P,E⃗,D⟩` is preserved; **(b)** any **describedEntity** change has a **KindBridge** (`CL^k`) entry on MVPK/**UTS**; **(c)** a **SquareLaw‑retargeting witness** is present (on UTS); **(d)** the operation is **PathSlice‑local** (`PathSliceId` pinned); **(e)** **no plane/unit change** occurs (plane/unit changes remain gated); **(f)** **CV.ReinterpretationEquivalence** (A.20) is `pass`; **(g)** **NoHiddenScalarization** — if the step concerns a comparable return shape, set/partial‑order semantics are preserved and comparators remain ref‑only (cf. A.28). | UTS row includes `bridgeChannel=Kind` and `CL^k`; SquareLaw‑retargeting witness present; PathSliceId pinned; CV status recorded; no scalarization detected. |
| **CC‑TGA‑07 — CV⇒GF activation predicate** | Until **aggregated `ConstraintValidity` = `pass`**, all **GateFit** checks return `abstain`. | Simulate CV failure ⇒ GateFit `abstain`. |
| **CC‑TGA‑08 — LaunchGate discipline (incl. pre‑run barrier)** | Each `U.WorkEnactment` has exactly one `LaunchGate` owning `USM.LaunchGuard`; **mandatory** checks: `FreshnessUpToDate`, `DesignRunTagConsistency`. If preceding step’s CV ≠ `pass`, LaunchGate decision is `block` (cause logged). | Owner resolution `GuardOwnerGateId = LaunchGateId(U.WorkEnactment)`; CV≠pass ⇒ `block` with log. |
| **CC‑TGA‑09 — MVPK publication discipline** | Every surfaced node uses MVPK; faces carry `PublicationScopeId`, presence‑pins, **edition ids**, Γ pins; **no I/O duplication** or arithmetic; faces add no new numeric claims. | Cards show `PublicationScopeId`; pins present; no “signature”/math on faces. |
| **CC‑TGA‑10 — Normalize→Compare (CSLC)** | Any comparison cites **UNM/CG‑Spec** editions and **ComparatorSetRef**; ordinal claims are compare‑only; partial orders return sets; edition‑aware artifacts (QD/archives) pin `{DescriptorMapRef, DistanceDefRef, CharacteristicSpaceRef?}.edition`; **any face citing editions includes `BridgeCard + UTS row`**. **NoHiddenScalarization — detection criteria:** (1) return shape is **set/poset**, not scalar; (2) `ComparatorSetRef` is present and edition‑pinned; (3) MVPK faces add **no new numeric claims**; (4) any summarisation is **order‑preserving & set‑valued**; otherwise conformance fails. | Faces show comparator pins; archive pins present; linter rejects edition cites without UTS; scalarisation checks pass.
| **CC‑TGA‑11 — Crossings gated** | Cross‑Context/plane crossings publish **BridgeId + UTS + CL/CL^plane** and are mediated by `OperationalGate(profile)`; **Φ/Φ_plane penalties → R‑lane only**; describedEntity change publishes **KindBridge (CL^k)**. **Exception (StructuralReinterpretation):** a **projection‑only** describedEntity retargeting is surfaced **without** a gate **iff** **CC‑TGA‑06‑EX** holds; then the UTS row includes `bridgeChannel=Kind`, `CL^k`, and a **retargeting witness**; any plane/unit change falls back to a gated crossing; `PathSliceId` is pinned; UNM reuse cross‑context continues via `Transport`. | Crossing surfaces show Bridge/UTS/CL pins; penalties routing audited. |
| **CC‑TGA‑12 — Set‑returning selection** | `U.SelectionAndBinding` returns sets/archives under declared comparators (`ParetoOnly` by default) — no covert scalarization. | Selector output is a set/archive; policy id present if escalated. |
| **CC‑TGA‑13 — Budgeted Selection↔Planning loop** | The loop declares **budget / max_iter**; on expiry selector publishes partial‑optimal set + `MethodTuning`; next **PathSlice** scheduled. | Logs show budget stop and slice rollover. |
| **CC‑TGA‑14 — UNM before loop & Freshness lifecycle** | UNM runs before selection; stale/missing inputs produce **FreshnessTicket/FreshnessRequest** planned in `WorkPlanning` and executed in `WorkEnactment`; calibrations appear as `CalibrateTo(map|standard)` with Φ pins. | Ticket state machine Issued→Planned→Executed→Closed; calibrations pinned. |
| **CC‑TGA‑15 — FinalizeBinding only in WorkEnactment** | Only `U.WorkEnactment` performs `FinalizeBinding` and binds launch values. | Any earlier attempt blocks at LaunchGate; binding witness present in Work. |
| **CC‑TGA‑16 — Guard ownership & semantics** | `USM.CompareGuard`/`USM.LaunchGuard` publish owner gate; guards are **events**, not GateChecks; failures are aggregated by owner’s gate per profile. | Guard pins show owner; GuardFail routed to owner’s DecisionLog. |
| **CC‑TGA‑17 — Assurance ops on Transfer** | On `U.Transfer` only `ConstrainTo/CalibrateTo/CiteEvidence/AttributeTo`; none mutate `⟨L,P,E⃗,D⟩`. | Edge audit shows ops; CtxState unchanged across the edge. |
| **CC‑TGA‑17a — Assurance ops contracts (normative)** | **ConstrainTo(region|policy)**: tightens declared region/policy; **pre**: region⊆current; **post**: `⟨L,P,E⃗,D⟩` unchanged; **idem.** and **monotone** under composition. **CalibrateTo(map|standard)**: attaches **editioned** calibration map/standard with Φ‑policy id; lawful per CG‑Spec; **post**: `⟨L,P,E⃗,D⟩` unchanged; **idem.** on same edition; penalties **→ R only**. **CiteEvidence(anchor)**: binds carriers via **SCR/RSCR**; adds no numeric claims; **idem.**; missing carriers ⇒ **abstain**. **AttributeTo(role|source)**: provenance only; decision algebra unaffected; **idem.** Hidden GateChecks, plane/unit changes, or edition writes on edges are **forbidden**. | Contracts visible on edge audit; violations fail lint. |
| **CC‑TGA‑18 — Flow = valuation & slice‑local refresh** | A flow declares valuation `ν` over `U.Transfer` plus `PublicationScopeId` and `PathSliceId`; **sentinel‑bounded** refresh; re‑emit on edition change or sentinel rule. | FlowSpec shows ν; sentinel bump triggers slice‑local recompute. |
| **CC‑TGA‑19 — Γ_time on compare/launch** | All compare/launch faces pin `Γ_time`; no implicit *latest*. | Face audit shows Γ pins; LaunchGate blocks on stale. |
| **CC‑TGA‑19a — Γ_time pin shape (normative)** | The `Γ_time` pin is one of: `snapshot(t)`, `interval[t1,t2]` (closed), or `policy(Γ_timeRuleId)` that resolves to either; CV computations record the **resolved time basis** in `DecisionLog` and do not widen Γ at publication time. | DecisionLog shows basis; linter rejects missing/implicit Γ. |
| **CC‑TGA‑20 — Lean publish‑mode ≠ weaken** | `AssuranceLane‑Lite` affects faces only; required GateChecks for the active profile remain intact. | Gate in Lean/Core shows minimal pins; GateChecks list unchanged. |
| **CC‑TGA‑21 — Decision stability & idempotency witness** | Gate decisions are stable under the equivalence relation defined in **A.41**; a **witness of equivalence** is present on the DecisionLog surface; any change that breaks equivalence requires re‑aggregation. **Minimum lexeme (CV‑relevant surfaces):** `EquivalenceWitness := { keys, E⃗, Γ_time(basis), PathSliceId?, ReturnShapeClass, ComparatorSetRef?, profile }`. | Modify any input outside the declared equivalence ⇒ re‑aggregation; DecisionLog records the witness (A.41); lexeme present.
| **CC‑TGA‑21a — Decision join (publication algebra)** | Aggregation over GateChecks is the **idempotent, commutative, associative join** on the lattice `abstain ≤ pass ≤ degrade ≤ block` with **neutral = `abstain`** and **absorbing = `block`**. The algebra is conceptual; publications surface only (i) the aggregated **GateDecision** and (ii) its **GateDecisionRationale** recorded in the **DecisionLog**. A **GateDecisionExplanation** is an optional human‑readable narrative derived from the GateDecisionRationale; it is **not** a decision and MUST NOT be used as one. If aggregated `ConstraintValidity ≠ pass` or the active profile suppresses narratives, any GateFit‑oriented GateDecisionExplanation **does not apply**. | Review a gate with multiple GateChecks: the aggregated decision matches the lattice join; no per‑check arithmetic is introduced on faces. |
| **CC‑TGA‑22 — Errors/unknowns fold by profile** | Errors/timeouts fold to `degrade` under `Lean|Core` and to `block` under `SafetyCritical|RegulatedX`; `unknown` folds per GateCheck policy (safety‑default: `degrade`). | DecisionLog shows folds; profile switch changes fold behavior accordingly. |
| **CC‑TGA‑23 — SquareLaw on crossings** | For every GateCrossing, `gate_out ∘ transfer = transfer' ∘ gate_in`; LaunchGate case is mandatory. | MVPK shows commuting square; inconsistency yields `block|degrade` per profile. |
| **CC‑TGA‑24 — UNM single‑writer** | `CG‑Spec`, `ComparatorSet`, `UNM.TransportRegistryΦ` editions are authored only by `UNM.Authoring` (others ref‑only). | Authorship cards: UNM is sole writer; others have refs only. |
| **CC‑TGA‑25 — Evidence lanes & DecisionLogs** | AssuranceLane surfaces GateProfile, GateCheckRef list, edition pins, aggregated decision, `DecisionLogRef`; **evidence pins follow a two‑layer scheme**: **carriers** are pinned via **`SCR/RSCR`**, and **value annotations** are surfaced under **`VALATA (VA/LA/TA)`**. | Gate surfaces include these pins; logs retrievable. |

> **Coupling note.** `CC‑TGA‑07 (CV⇒GF)` and `CC‑TGA‑21a (Decision join)` together ensure that any GateFit‑scoped GateCheckRef **returns `abstain`** until the aggregated CV status equals `pass`; CV/GF separation remains intact. 
> **Authoring note (scope of E.TGA vs A.*):** Detailed, mechanism‑level checks and most publication content are specified in the **A.* patterns** (A.20…A.42). E.TGA fixes only carcass‑level obligations above.

**Glossary (additions)**  
* *Open‑world species* — non‑exhaustive domain‑level specializations of `U.Transduction` that map to the minimal kind set.  
* *Signature (TGA kind)* — `U.Transduction(kind=Signature)`; **identical to** **A.6.0** `U.Signature` (universal block). **Not** a `C.3.2 KindSignature`.  
* *Architheory Signature (A.6)* — family‑specific **view** and discipline that **specialises** A.6.0 for architheories; the universal A.6.0 block remains the source of truth.  
* *KindSignature (C.3.2)* — intensional definition of a `U.Kind` (intent/extent, F); **unrelated** to TGA kinds; never a `genus`.  
* *Species (domain‑level)* — typed specialisations `speciesOf(kind=…)` that **MUST** declare `KindDefinition=A.*` id (e.g., `kind=Mechanism; KindDefinition=A.6.1`).  
* *KindBridge (`CL^k`)* — a compatibility surface on UTS for describedEntity/kind transitions; required by CC‑TGA‑06‑EX and crossings (CC‑TGA‑11).
* *Eulerian interpretation* — operational stance where a flow is treated as a valuation over `U.Transfer` and edges perform assurance‑only operations (no token‑passing semantics).
* **GateCheckRef shape (publication lexeme, normative here).** Where GateChecks are surfaced, a **GateCheckRef** is a record
  `GateCheckRef := { aspect, kind, edition, scope }` with:
  `aspect ∈ {ConstraintValidity, GateFit}`, `kind ∈ GateCheckKind`, `edition ∈ Editions`, and `scope ∈ {lane | locus | subflow | profile}`. 
* **GateDecision / GateDecisionRationale / GateDecisionExplanation (terminology).**
  — **GateDecision** — the aggregated lattice value produced by `OperationalGate(profile)` for a specific `{GateProfile, GateCheckRef[]}`.
  — **GateDecisionRationale** — the minimal structured support **for that GateDecision**: per‑check outcomes, profile‑bound folds, and surfaced evidence/witness references on the DecisionLog; it records **why the GateDecision is admissible** under the active profile.
  — **GateDecisionExplanation** — an optional human‑readable narrative derived from the GateDecisionRationale; it **does not carry decision status**. While aggregated `ConstraintValidity ≠ pass`, GateFit‑scoped checks return `abstain`; any GateFit‑oriented GateDecisionExplanation **does not apply**.
> **Clarity note.** **GateDecision ≠ GateDecisionExplanation**; narratives are optional and derivative of GateDecisionRationale.

* **GateFit (aspect, not an entity).** GateFit names the **aspect** of checks that evaluate **profile‑fit**; there is no separate GateFit entity. “Gate decision under GateFit” means “the gate’s decision computed from GateChecks with `aspect=GateFit`”.

  This shape is publication‑level only; it introduces no new execution steps and no arithmetic on faces.  (Couples to A.20/A.21 without duplicating their check catalogs.)
* *VALATA (VA/LA/TA)* — value‑annotation scheme used on **AssuranceLane**; **carriers** are referenced via **SCR/RSCR**; detailed obligations live in A.10/A.29. Included here so evidence pins are self‑describing in E‑level texts.
* *Transfer vs Transport* — **Transfer** = the sole graph edge kind `U.Transfer`. **Transport** = Φ‑policy/registry‑defined conversions (`TransportRegistry^Φ`) referenced by UNM; “reuse via Transport” refers to the latter.
* *GateCrossing* — a typed node transition that changes a CtxState slot or the kind‑channel; see **S1.b** for the normative list and required pins.
* *Admissible path* — a typed path obeying the GateCrossing discipline (no hidden crossings; witnesses present), Γ‑pinned on compare/launch, and `T^D↔T^R` only at `LaunchGate`; see **S2**.

### Gating Profiles (applied to E.TGA)

> Gating is expressed as **publication‑gating** per E.17 profiles. The graph model aligns with the **CC items** listed for the chosen profile; higher profiles include all lower‑profile items.

| Profile                          | Required CC‑items                                         | Additional notes                                                                               |                                                                  |
| -------------------------------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Lean**                         | 01–06, 08–09, 11–12, 15, 19–21, 25                                                                                                           | Minimal MVPK presence; LaunchGate keeps `FreshnessUpToDate` & `DesignRunTagConsistency`. |
| **Core**                         | **Lean** + 07, 10, 13–14, 16–18, 22–23, 24                                                                                                  | Adds CV⇒GF order, CSLC pins, budgeted loop, guards, valuation/sentinel refresh, error folds, SquareLaw, UNM single‑writer. |
| **Safety‑Critical / RegulatedX** | **Core** + profile‑specific GateChecks (safety envelope, regulator id/editions) with stricter folds per **CC‑TGA‑22**; SquareLaw audits tightened | — |

**Recommended defaults (non‑normative, tie‑in to A.26).** Profiles inherit along a `PathSlice`; local overrides may only **add** GateChecks; weakening requires a new `PathSlice` via sentinel (cf. A.26/A.25).
### TGA LEX discipline (registration)
Register Tech tokens (ASCII) used by this architecture with twin‑labels: `U.TransductionGraph`, `U.TransductionFlow`, `StructuralReinterpretation`, `OperationalGate`, `GateProfile`, `GateCheckRef`, **`GateCheckKind`**, `DecisionLog`, `USM.CompareGuard`, `USM.LaunchGuard`, `KindBridge`, `SubflowRef`, `FlowEmbed`, `SentinelId`, `PathSliceId`, `SliceRefresh`, `FinalizeBinding`, `VALATA`. Add an ASCII alias **`CLKind`** ↔ Plain `CL^k` (cf. `CLPlane` ↔ `CL^plane`). Reference MVPK E.17 naming for faces.  
**CtxState Extension Registry.** Register any extra CtxState slot beyond ⟨L,P,E⃗,D⟩ with: slot id, informal intent, partial‑order law (with neutral/absorbing), SquareLaw compatibility note, and the owning Gate profile(s) that may change it. Absence of registration ⇒ **non‑conformant**.

### Consequences

**Benefits.**

1. **Universality with discipline:** one edge kind and explicit gates eliminate “second process ladders” and make cross‑domain flows (ML, supply‑chain, TAMP/MPC, scientific workflows) uniformly analyzable and auditable.
2. **Comparability & replayability:** CSLC and edition‑pinned comparators prevent covert scalarization and enable lawful set returns and reproducible decisions.
3. **Locality of change:** sentinel subflows restrict refresh to affected `PathSlice`s; large graphs remain stable under frequent edition bumps.
4. **Clean design/run fold:** LaunchGate and `DesignRunTagConsistency` stop premature binding; acceptance and telemetry live where they occur (`U.Work`).
5. **Assurance visibility:** MVPK makes GateProfile/DecisionLog surfaces locally checkable and cacheable for the same `{PathSlice, GateChecks, Editions}`.

**Trade‑offs.**
a) **Higher upfront modeling cost:** explicit Bridge/UTS pins and GateProfiles demand care; mitigated by Lean profile and templates.
b) **Longer edge surfaces:** MVPK faces are verbose by design; Lean surfaces can be used for low‑risk segments.
c) **Tooling alignment:** some incumbent DAG‑only orchestrators conflict with budgeted cycles and set‑return semantics; adapters must project E.TGA semantics to their interop layer (never the other way round).

### Rationale

E.TGA enforces **strict separation of concerns** (carcass‑level only); **specialized semantics live in A.* patterns**:

* **What the graph is:** typed intensional morphisms and a single transport edge `U.Transfer`.
* **Where/when it may cross contexts:** **only** at `OperationalGate(profile)`, with Bridge+UTS, CL/CL^plane, and Φ routed to R‑lane.
* **How comparability works:** UNM authors units/planes/transports (single writer) and selectors operate **only** on normalized, edition‑pinned comparators, returning sets/archives—not totals. **Edition‑aware pins and archive semantics are tested in A.28/A.34/A.37 (not repeated here).**
* **How change propagates:** sentinel‑bounded `PathSlice` refresh; editions are monotone; LaunchGate is the only binder of launch‑values.

This arrangement guarantees **functorial publication** (commuting squares on crossings) and **orthogonality** of inner technical validity (ConstraintValidity) to context fit (GateFit), which in turn makes gate aggregation **order‑independent** and cements the CV⇒GF activation predicate.
