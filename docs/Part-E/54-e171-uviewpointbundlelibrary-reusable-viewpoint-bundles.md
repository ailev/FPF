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
