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
