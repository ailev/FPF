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
