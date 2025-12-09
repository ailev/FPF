# E.10 — LEX‑BUNDLE*: Unified Lexical Rules for FPF (Registers, Naming, and Forbidden Forms) \[A]
*Definitional pattern \[D]; normative for all Core/Architheory text and for any Context that claims FPF conformance.*

**Status & placement.** Part E.10 (“Lexical Discipline & Stratification”); complements **E.10.D1 (D.CTX)**, **E.10.D2 (I/D/S)**, and **E.11 (Authoring‑Tier Scheme)**, and is referenced by F‑cluster naming practices (F.4–F.8). This bundle consolidates all lexical constraints in one place so authors can cite **“LEX‑BUNDLE”** instead of listing rules scattered across documents.

**Builds on:** A.7 **Strict Distinction (Clarity Lattice)**; E.5 Guard‑Rails (DevOps Lexical Firewall; Notational Independence; Unidirectional Dependency); F.5 **Naming Discipline for U.Types & Roles**.
**Coordinates with.** A.2/A.15 (Role–Method–Work alignment), A.10 (Evidence Graph Referring), B.1/B.3 (Γ‑algebras & assurance), F‑cluster (context of meaning; Bridges).

---


---

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

## 6 · Ontology Guards 

### 6.1 Tech register ontology guards

> **Purpose.** This section stabilises the Tech register of the kernel lexicon by enforcing head‑anchored naming, explicit *object‑of‑talk*, I/D/S morphology, disciplined treatment of **Role / Holder**, and Domain usage consistent with **D.CTX** and **UTS**. It aligns with **F.4 Role Description (RCS/RSG)**, **F.11 Method Quartet Harmonisation**, and **F.17 UTS**. **Scope:** Guidance is **register‑agnostic** and applies to the whole FPF; examples are illustrative and MUST pass Minimal Generality & Domain Anchoring (MG·DA) and other rules of lexical governance pattern E*. This guidance applies to kernel and non‑kernel components (including Part G and patterns in Part C) and SHOULD be reused across extensions.
> 
**Onto1 — Head‑anchoring**  *(use Kernel heads + pass LEX.TokenClass / I/D/S gates)*
* **Rule:** The **head noun of a term MUST explicitly signal the kind** (`System`, `Holon`, `Role`, `Work`, `Episteme`, `Tradition`, `Lineage`, `Characteristic`, `Method`, `Profile`, `Description`, `Spec`, `Flow`, `Card`, `Pack`, `Dashboard`, …).
* **Figurative heads** with obvious overload (“Tradition”, “family”, “process”, “function”) are **forbidden in the kernel**. Use **plain twins** only with a 1:1 Tech mapping and declare **`LEX.TokenClass`** for the Tech token. They **MAY** appear **only in the Plain register** as 1:1 twin‑mappings to a Tech token, but **MUST NOT** appear in the Tech register. Plain language should minimise lexical error from overloaded terms; use plain‑twin lexical guards.
  * ***Do:** `IncidentDashboard`, `MethodSpec`, `TraditionProfile`, `FlowDescription`.
* ***Don’t:** `IncidentBoard`, `TDD Tradition`, `Production Process` (kernel), `Service Function` (kernel).

 **Onto2 — I/D/S on the surface (Intension/Description/Specification morphology)**  *(ref. E.10.D2)*
* **Rule:** Any **intensional** object is a bare head: `Method`, `Tradition`, `Characteristic`. Any **description** appends **`…Description`**: `MethodDescription`, `TraditionDescription`. Any **testable specification** appends **`…Spec`** and presupposes acceptance criteria and harnesses (normative in **E.10.D2**). E.g., *Algorithm* is a species of `MethodDescription` for a computer (a system in the role of information transformer); **If** expressed in a formal language **and** bundled with acceptance tests, it is **`MethodSpec`** (per **F.11**). **If** expressed as pseudo‑code, it is **`MethodDescription`**.
* **Extension:** Apply the same pattern to non‑method objects where appropriate: `FlowDescription`/`FlowSpec`, `SystemDescription`/`SystemSpec`.
* **Do:** `SamplingMethod` · `SamplingMethodDescription` · `SamplingMethodSpec`.
* **Don’t:** `SamplingAlgorithm` (when it is just prose), `SamplingProcessSpec` (head not signalling kind).

**Onto3 — Roles, Holders, and Carriers (holonic)**  *(ref. F.4 / F.5)*
* **Rule:** The playable intention is named **`…Role`** and described through **F.4 Role Description** (RCS/RSG), e.g., `SafetyOfficerRole`, `ReviewerRole`. The party **assuming a role** is the **Holder**. Use the **`Holder#Role:Context`** pattern to type the assumption (where `Context` is a `U.BoundedContext`), e.g., `Team‑Alpha (U.Holon) is Holder#SafetyOfficerRole:Plant‑Ops`. **Carrier** is **reserved for a system that bears a symbol of episteme** (`U.Episteme`, `Tradition`, `Lineage`, `Profile`, repertoire) **independent of any concrete role assumption**, e.g., `LeanTraditionCarrier`, `CalibrationLineageCarrier`. Avoid **`Artefact`** as a head in the kernel: it is ambiguous between a Carrier (e.g., document), a system “made by” some transformer, or an episteme abstracted from its carrier.
* **Register note:** Job titles (`Reviewer`, `Owner`, `Lead`) belong in the **Plain** register and MUST twin‑map to explicit Tech `…Role` tokens.
* **Why:** This resolves the inconsistent “role carrier vs role holder” usage: **use “Holder” for holonic role assumption**, keep **“Carrier”** for the *system that bears a symbol of episteme*. 
* **Migration note.** Legacy `…CarrierRole` **MUST be rewritten** to `Holder#…Role:Context`. Use SCR‑LEX to enforce the rewrite.
* **Do:** `ReviewerRole` (or `AssessorRole`), `Holder#ReviewerRole:Journal‑Issue‑42` (or `Holder#AssessorRole:Procurement‑Lot‑42`); `LeanTraditionCarrier (U.Holon)`, independent of any particular role.
**Don’t:** `Reviewer` (as a kernel type), `ReviewerCarrier` (to mean a role holder), `SystemReviewer` (role collapsed into a type).

**Onto4 — Domain only as a catalog mark**  *(ref. E.10.D1 D.CTX; publish stitching on UTS)*
* **Rule:** `Domain` is **not a kernel kind** and carries **no semantics, inheritance, or reasoning rights**. It is a **catalog mark** that groups several `U.BoundedContext` entries.
* **Required stitching (see D.CTX & UTS).** Any use of `Domain` **MUST** present: 1. the enumerated list of `ContextId` in **D.CTX**, and 2. the corresponding **UTS strings** (F.17) with twin labels.
* **“Discipline ≠ Domain.”** _Domain_ labels are **catalog‑only (D.CTX + UTS)**; **Discipline** is a **CG‑Spec‑governed holon** (`U.Discipline`). Cross‑use requires **Bridge (F.9) + CL**; **LexicalCheck** MUST fail texts that equate Domain with Discipline.
* **Governance.** **No “Domain … governance”.** Rules of comparability/aggregation belong to **Discipline/CG‑Spec** (Gauge, MinimalEvidence, Γ‑fold, CL‑routing), *not* to `Domain`. Prefer `DomainFamily` + stitching over inventing new “Domain” types.
* **Do:** `DomainBundle: ClinicalSafety → {ContextId: AdverseEvents, DeviceLabelling, …} + UTS twins`.
* **Don’t:** `ClinicalSafetyDomain` as a type with inheritance; `Domain Governance` sections in Tech.

**Onto5 — Always state the **object‑of‑talk**
* **Rule.** The definition or first line of a gloss **MUST state what the term is about**: a `U.Holon`/`U.System`, a `U.Episteme` (`Tradition`, `Lineage`, `Profile`), a `Role`, a `Work` execution, a `Characteristic`, or a `Carrier`.
* **Do:** “**Object‑of‑talk:** `ReviewerRole` — a role intention playable by a holon within an editorial context.”
* **Don’t:** “Reviewer — a person who …” (blurs kind and object‑of‑talk).

**Onto6 — Bans and canonical rewrites**  *(mirror E.10 § 9 L‑rules; do not duplicate tables)*
* `process / function / activity` → **`Work` / `MethodDescription` / `Flow`** (context‑dependent).
* `Tradition` → **`Tradition`** (Tech); leave “Tradition” only as a Plain twin with an adjacent Tech label.
* `domain` → **`DomainFamily` + {ContextId list} + UTS twins**.
* legacy `…CarrierRole` → **`Holder#…Role:Context`**.
* ambiguous `Owner` in role names → prefer **`StewardRole` / `CustodianRole` / explicit responsibility head**.
* job titles (`owner`, `lead`, `champion`) in the kernel → **use explicit `…Role` names**; keep titles in Plain with twin‑labels.
* **Do:** `FlowDescription: ReturnsHandling`, `Tradition: Test‑Driven`, `Holder#CustodianRole:Asset‑Ledger`.
* **Don’t:** `Returns Process`, `TDD Tradition` (kernel), `Ledger Owner` (underspecified).

**Worked mini‑examples across arenas**
1. **Software engineering:** `BuildFlowDescription`, `CIHarnessSpec`; `Holder#MaintainerRole:Repo‑X`. Avoid `Build Process`, `Repo Owner`.
2. **Applied research / experimentation:** `SamplingMethodSpec`, `CalibrationLineageCarrier`; `Holder#ReviewerRole:Grant‑Call‑Y`.  Avoid `Sampling Algorithm` (if prose), `Lab Owner`.
3. **Production / service management:** `ShiftWork`, `SafetyOfficerRole`; `Holder#SafetyOfficerRole:Plant‑Ops`.  Avoid `Safety Officer` as a type, `SafetyDomain Governance`.
4. **Operations research / optimisation:**  `RoutingMethodDescription`, `CostCharacteristic`; `Holder#ModelStewardRole:OR‑Program`.  Avoid `Routing Function`, `Model Owner`.
5. **Healthcare / clinical ops:** `CarePathwayFlowDescription`, `MedicationAdministrationWork`; `Holder#AttendingPhysicianRole:Ward‑12`. Avoid `Care Process`, `Ward Owner`.
6. **Finance & accounting:** `ReconciliationMethodSpec`, `JournalPostingWork`; `Holder#TreasuryStewardRole:Liquidity‑Book`. Avoid `Reconciliation Process`, `Account Owner` (underspecified).
7. **Legal / compliance:** `RetentionPolicySpec`, `InvestigationWork`; `Holder#DataProtectionOfficerRole:Org‑X`. Avoid `Compliance Function`, `Data Owner` (underspecified).
8. **Cloud / IT operations:** `IncidentFlowDescription`, `RunbookMethodSpec`; `Holder#OnCallEngineerRole:Service‑Y`. Avoid `Incident Process`, `Service Owner` (underspecified).
9. **Logistics / supply chain:** `PickingWork`, `RoutingMethodSpec`; `Holder#DispatcherRole:Hub‑Z`. Avoid `Picking Process`, `Fleet Owner`.
10. **Construction / civil engineering:** `PermitAcquisitionFlowDescription`, `InspectionMethodSpec`; `Holder#SiteStewardRole:Project‑Lot‑17`. Avoid `Inspection Process`, `Site Owner`.
11. **Emergency response:** `TriageMethodDescription`, `EvacuationFlowDescription`; `Holder#IncidentCommanderRole:Event‑R`. Avoid `Triage Function`, `Incident Owner`.
12. **Agriculture:** `IrrigationFlowDescription`, `SoilSamplingMethodSpec`; `Holder#FieldStewardRole:Plot‑17`. Avoid `Irrigation Process`, `Field Owner`.

**Checklist before minting a KernelToken**
* Head noun signals kind (Onto1).
* I/D/S morphology correct (Onto2).
* If role‑related: **Role vs Holder vs Carrier** separation observed; holonic scope explicit (Onto3).
* Any Domain mention stitched to D.CTX and UTS; **no norms on Domain** (Onto4, Onto6).
* Object‑of‑talk declared (Onto5).
* SCR‑LEX rewrites checked / legacy forms migrated (Onto6).
> **Note on registers.** Keep figurative or business‑casual terms in the **Plain** register only, with strict **twin‑label** links to the Tech token (LEX‑BUNDLE). In the **Tech** register, speak in KL‑CAL: **episteme‑about‑epistemes** (Tradition, Lineage, Profile), not in catalogue‑admin idioms.

* **Onto‑Deon — Deontic lexicon guard (Core register)**  
 **Rule.** In the Conceptual Core, avoid **“Standard/Standardual”** unless the object is an explicit **deontic speech‑act** under the **Gov** lens (cf. E.3). For interface/boundary invariants and public commitments of **things** (holons, interfaces, ports), prefer **standard**, **interface standard**, or **compliance profile**.  Standard is a Description or Specification. If you have standard, check a name of an intensional object: is it true name that compliant with this pattern guards? If not, change a name for a proper intensional name and then add "standard" as "description with intended compliance checks".
 **Rewrite hints (Tech → Tech).**  
 `publication Standard` → `publication standard`;  
 `frame Standard` → `frame standard`;  
 `measurement Standard` → `measurement standard`;  
 `Method Interface Standard (MIC)` → `Method Interface Standard (MIS)` *(alias acceptable during transition)*;  
 `Boundary‑Inheritance Standard (BIC)` → `Boundary‑Inheritance Standard (BIS)` *(alias acceptable during transition)*.  
 **Rationale.** Keeps Core prose centred on **intensional objects** and their boundary invariants; reserves deontic obligations for governance contexts and **U.Service**‑like promises. Do **not** misuse “plane”: deontic speech‑acts are analysed via the **Gov** lens, while **ReferencePlane** remains `{world | concept | episteme}`.


---

## 8 · Morphology & Lexical Form (LEX.Morph)

> **Principle.** Form follows **object‑of‑talk**. A token’s morphology (suffix/prefix/casing) must (a) express **what kind of thing** it names, (b) respect **MG·DA** (Minimal Generality & Domain Anchoring), and (c) pass **LEX.TokenClass** gates:
> `LEX.TokenClass(token) ∈ {KernelToken | ContextToken | DiscriminatorToken}`.
> Morphological choices never override **I/D/S layers** or **CHR\:ReferencePlane** semantics.

### 8.0 Casing & basic forms

**M‑0 (Casing and categories).**
Types & role kinds: **UpperCamelCase** (`IncisionOperatorRole`, `MethodDescription`).
Relations/verbs: **lowerCamelCase** (`performedBy`, `isExecutionOf`, `bindsMethod`).
IDs/instances: **flat with delimiters** (context‑defined) but never collide with type forms (e.g., `W#Seam134`, `ctx:Hospital.OR_2025`).
**Register discipline:** normative tokens use the Technical register; Plain synonyms are allowed in prose only, never in constraints.

---

### 8.1 Reserved suffixes (gated by LEX.TokenClass and I/D/S)

> **Use tables as a whitelist.** Rows indicate **when** a suffix is permitted and **what it means**. “Layer gate” prevents I/D/S confusion; “Examples” are illustrative.

| **Suffix**              | **Kind named** (object‑of‑talk)            | **Layer gate**                       | **LEX.TokenClass gate**         | **Examples**                                      | **Forbidden misuses (typical)**                                       |
| ----------------------- | ------------------------------------------ | ------------------------------------ | ------------------------------- | ------------------------------------------------- | --------------------------------------------------------------------- |
| **`Role`**              | **Role kind** (intensional)                | I‑layer                              | KernelToken/ContextToken        | `TransformerRole`, `ApproverRole`                 | Appearing in BoM/mereology; mixing with run logs.                     |
| **`Method`**            | **Abstract way of doing** (recipe type)    | I‑layer                              | KernelToken/ContextToken        | `SteriliseInstrumentMethod`                       | Versioning on `Method` (version the `MethodDescription` instead).     |
| **`MethodDescription`** | **Recipe/description** (notation‑agnostic) | D‑layer                              | KernelToken/ContextToken        | `JS_Schedule_v4_MethodDescription`                | Calling it “process”; encoding runtime actuals here.                  |
| **`…Spec`**             | **Testable specification** (acceptance‑bound) | S‑layer                              | KernelToken/ContextToken        | `MethodSpec`, `FlowSpec`, `SystemSpec`            | Using “Spec” without acceptance tests/harness; putting runtime actuals here. |
| **`Work`**              | **Execution** (runs or kinds of runs)      | (run artefact; not I/D/S)            | KernelToken/ContextToken        | `SpeechActWork`, `W#Seam134`                      | Plans/schedules; design‑time recipes.                                 |
| **`WorkPlan`**          | **Schedule of intent**                     | D‑layer (plan artefact)              | ContextToken                    | `MaintenanceWorkPlan_Q3`                          | Logging actuals; claiming execution.                                  |
| **`Service`**           | **External promise object**                | I‑layer (Standarded intension)       | KernelToken/ContextToken        | `ObjectStorageService`, `PassportIssuanceService` | Naming teams/APIs as “Service”.                                       |
| **`Capability`**        | **System ability**                         | I‑layer                              | KernelToken/ContextToken        | `ScheduleGenerationCapability`                    | Mislabeling roles or methods as capabilities.                         |
| **`Dynamics`**          | **Law/model of change**                    | I‑layer                              | KernelToken/ContextToken        | `LotkaVolterraDynamics`                           | Using for abilities (`Capability`) or recipes (`Method`).             |
| **`Observation`**       | **Observation record/kind**                | (run artefact; not I/D/S)            | ContextToken/DiscriminatorToken | `VibrationObservation`                            | Mixing with `MethodDescription` or `Evaluation`.                      |
| **`Evaluation`**        | **Evaluation artefact**                    | D/S‑layer (epistemic episteme)              | ContextToken/DiscriminatorToken | `CalibrationEvaluation`                           | Using to name roles or methods.                                       |
| **`EvidenceRole`**      | **Role in evidence assembly**              | I‑layer (role kind)                  | KernelToken/ContextToken        | `WitnessStatementEvidenceRole`                    | Using as a generic “evidence”.                                        |
| **`Episteme`**          | **Epistemic knowledge unit** (structural)  | D/S‑layer                            | KernelToken/ContextToken        | `TraceabilityEpisteme`                            | Colliding with CHR **ReferencePlane** (never suffix “Plane”).         |
| **`System`/`Holon`**    | **Substantial entity**                     | I‑layer                              | KernelToken/ContextToken        | `AnesthesiaSystem`, `OrderFulfillmentHolon`       | Using to denote Context or run artefact.                              |
| **`Boundary`**          | **System boundary**                        | I‑layer                              | KernelToken/ContextToken        | `SterileFieldBoundary`                            | Using as a role or method.                                            |
| **`Objective`**         | **Target state**                           | I/D‑layer (depends on formalization) | KernelToken/ContextToken        | `HemostasisObjective`                             | Encoding acceptance tests here (put tests in Spec/MethodDescription). |
| **`Requirement`**       | **Obligation at acceptance**               | D/S‑layer                            | KernelToken/ContextToken        | `LatencyRequirement`                              | Using as a role or capability.                                        |
| **`BoundedContext`**    | **Context card**                           | (meta‑structural; not I/D/S)         | ContextToken                    | `ITIL_2020_BoundedContext`                        | Treating Context as domain; minting `U.*` inside a Context.           |
| **`Surface`**              | Publication/Interop surface (episteme)   | D/S-layer (publication)     | ContextToken                     | PublicationSurface, InteropSurface       | StructureSurface, MechanismSurface, PortfolioSurface |
| **`Card`**                 | UTS/record unit (episteme)               | D-layer (publication)       | ContextToken                     | MethodCard, ExternalIndexCard            | Encoding runtime actuals; using as a ‘Service’  |
 
| **Suffix** | **Lexical class** | **Meaning / Ontology** | **Where it lives** | **Examples / Notes** |
|--- |--- |--- |--- |--- |
| **Space** | Intensional kind | A typed **state space** (finite product of Characteristic×Scale slots); no procedures | Kernel A.19; CHR/space consumers | `CharacteristicSpace`, `CreativitySpace`. Edition of a Space is a **phase** of the episteme that defines it. |
| **SpaceRef** | Pointer | Registry reference to a Space | Data fields / UTS | `CharacteristicSpaceRef`. Use **`.edition`** on the **Ref** when pinning a historical phase. |
| **Map** | Intensional kind (method) | A **mapping method** from subjects to coordinates in a declared Space (encoder/featurizer) | Kernel/Method family (I‑layer), described/spec’d via I/D/S | `DescriptorMap` (declares invariances, corpus typing). Not a record or file. |
| **MapRef** | Pointer | Registry reference to a **Map** | Data fields / UTS | `DescriptorMapRef`. Pin the method phase via **`DescriptorMapRef.edition`**. |
| **Def** | S‑layer alias (CG‑Spec family) | A **definition/specification artifact** that fixes a **formula** or **distance** over a space; *synonym of …Spec* **within CG‑Spec registries only** | Part G (CG‑Spec family) | `DistanceDef` ≍ `DistanceSpec`. Prefer **…Spec** in new normative prose; **…Def** retained where already published. |
| **DefRef** | Pointer | Registry reference to a **…Spec/…Def** | Data fields / UTS | `DistanceDefRef`. Use **`DistanceDefRef.edition`** to pin the exact formula edition. |
| **Spec** | S‑layer | Testable invariants bound to acceptance harness (per E.10.D2) | S‑layer, Spec‑gated | Use for normative calculi and gauges. |
| **Slot** | Structural position | Named **argument position** in a relation/morphism signature (SlotKind in A.6.5) | Kernel A.6.0/A.6.5 | `DescribedEntitySlot`, `GroundingHolonSlot`. Always names a *position*; never used for ValueKinds or episteme fields. |
| **Ref** | Pointer | **Reference/identifier** to a registry item of some ValueKind (RefKind in A.6.5), not the thing itself | Data fields / UTS; RefKind types | `U.EntityRef`, `U.HolonRef`; episteme fields `…Ref : U.EntityRef`. Reserved for **RefKinds** and episteme fields typed as them; `…Ref` **never** carries content and is never used for ValueKinds or SlotKinds. |
| **Series** | Governance object | A **PhaseOf chain** (“editions”) for an episteme | Edition governance | `U.EditionSeries`. Holds immutability and provenance rules. |
| **.edition** | Attribute (on **Ref**) | The **phase id** of the **referenced artifact**; attaches to `…Ref`, not to the artifact’s name | Data fields / UTS | Use `XRef.edition`, **not** bare `XEdition` fields. Lower camelCase for keys. |

**Notes.**
• **Kernel‑only ban list** remains in § 8.3.
• **CHR guard:** the only token that may use the word *plane* is **CHR:ReferencePlane**.
• **Axis/dimension metaphors** are deprecated; use **Characteristic / CharacteristicSpace** where an enumeration is intended (see § 7).

**Not only suffix guard**
* Suffixes are strongly related to kinds and **should** be clearly guarded by MG·DA.
* Other morphemes (not only suffixes) also **must** respect kinds. For example, **Space is a geometric concept** — **never** use it as a suffix (`…Space…`) or other morpheme in beginning or in the middle of a term to name non‑geometric entities (e.g. prefer **Set/Kid/Kit** instead of **Space** where membership is intended).

**L‑SURF — disciplined use of *Surface* **
* ***Definition.** *Surface* is reserved for **publication/interoperability surfaces** (UTS, shipping, interop) that present lawful, plane‑aware summaries for human/selector consumption. A **Surface is a bundle of views** (ISO 42010 sense) packaged for a stated **audience** and **purpose**, with declared **viewpoint**. Surfaces are **conceptual** (E.5.2); serialisations live in Annex/Interop. Surfaces package **D/S** projections produced via `Describe_ID` / `Specify_DS` (A.7) and do **not** change object ontology.
* ***Allowed:** `PublicationSurface`, `InteropSurface` (G.10/G.13).  
* ***Forbidden:** `StructureSurface`, `MechanismSurface`, any `…Surface` that denotes a structural, mechanistic or measurement object.  
* ***Preferred alternatives:** use `…Boundary` (structural border), `…View` (publication view), or `…Card` (UTS record).

**L‑SPACE — disciplined use of *Space* **
* Use *Space* only for **CHR‑grounded measurement/state constructs** (e.g., `CharacteristicSpace` per A.19). Do **not** coin generic `…Space` for sets/portfolios or publication artefacts. Publish portfolios/archives as **sets** via lawful selectors; surface them on UTS as **views/cards**, not as spaces. 
* **Field‑name guard (Kernel blocks).** In **Kernel conceptual blocks** (e.g., A.6.0/A.6.1 lists), **do not** name a field `…Space`; reserve *Space* to the **types** (CHR/ReferencePlane families). Use **BaseType** as the field name and let the referenced `U.Type` carry `…Space` where appropriate; otherwise, for set‑valued universes, use `…Set`.
* Space is geomertic concept, neve use it even not as a suffix for naming non-geometric spaces (e.g. instead of Sets with membership)

**L‑ROLE — disciplined use of *Role***
* **Role** is always **Role Enactment for the `U.Holon`/`U.System` kind** (agentive use).
* **Param‑slot / relation‑endpoint guard.** Do **not** use the morpheme **`Role`** for **formal parameter positions** in operator algebra declarations (`OperatorAlgebra`) or Signature arguments. Reserve **`Role`** for **agentive kinds** only (A.2/F.4/F.6). Use a **`ParamKinds`** list (name→Kind) or `RelationEndpointKinds` to type formal slots. Same for similar situations (table columns, tuple placements): use MG·DA with domain‑**specific** terminology, never “Role”. 

### 8.2 Forbidden suffixes & the DevOps and Data Governance Lexical Firewall

**M‑F (Forbidden in Kernel tokens).** In KernelToken names, do **not** use: *…Function*, *…Process*, *…Task*, *…Activity*. These are ambiguous or vacuous—map using § 6 typing rules (often to `Method`, `MethodDescription`, or `Work`).

**M‑FW (Tool/file markers).** Tooling/file suffixes (*…API*, *…JSON*, *…YAML*, *…CI*, *…Kafka*, *…Postgres*) are **not** part of conceptual names. Place them in **Context** glossaries or operational configs (DevOps Lexical Firewall). Kernel names never carry tool/format/notation marks. It is pure conceptual, no data management and data governance intended.

### 8.3 Prefix discipline

**M‑P1 (Reserved prefixes).** `U.` reserved for **Kernel types**; `Γ_` for algebraic operators; `CAL/LOG/CHR` for **architheory packages**. Never mint `U.*` inside a Context.

**M‑P2 (Edition markers).** Apply explicit edition/version markers to **Contexts** and to `MethodDescription` / `Service`—**not** to `Method` (e.g., `BPMN_2.0_BoundedContext`, `JS_Schedule_v4_MethodDescription`, `PassportIssuanceService_v2025`).  Authors MAY annotate Context or Service names for didactics.
**Norms (edition vs release vs version).**
1) **edition** — the **content phase** of an episteme (Concept/Object/Symbol where Symbol‑only notation swaps do not force a phase). Lives in `U.EditionSeries`. Never embedded in labels (see R‑RD‑7); bind via data: `…Ref.edition`. 
2) **release** — a **Work** of making a **Carrier** public; may carry tags/dates; does **not** change episteme identity or phase.
3) **version** — a **tooling/carrier** identifier (file/package/code). Use only in Tooling/Pedagogy families; not in Core names.

**Property discipline.** When a field pins a referenced artifact’s phase, write it as **`<Thing>Ref.edition`** (dot notation), never as a standalone `…Edition` key. E.g., replace `DHCMethodEdition` with `DHCMethodRef.edition`.

### 8.4 Morphology tests (apply with § 7 MG·DA)

**M‑1 (Slot test).** The candidate fits **one** slot in the Strict Distinction lattice (Object ≠ Description ≠ Carrier; Role ≠ Method ≠ Work). If not, **rename** or split.

**M‑2 (Object‑of‑talk anchoring).** The head noun names the **object being classified** (Role/Method/Service/Work/Context/Characteristic). No free‑floating metaphors.

**M‑3 (Family congruence).** Where eligibility clarity is needed, add a **Context‑specific characteristic** (RCS) as a qualifier (e.g., `NormativeStandardRole`). Do **not** fake families with bare metaphors (no `RowPlane`, `senseFamily`, `…Lane`).

**M‑4 (Run vs design).** Use **`Work`** only for executions; use **`MethodDescription`** for recipes; never cross.

**M‑5 (Kernel parochiality).** KernelToken names carry **no domain nouns**; push domain markers to Context or RCS.

**M‑6 (Vacuity ban).** Avoid vacuous heads (*Thing, Event, Process, Resource*). Use established kernel heads (`U.Holon`, `U.Work`, `U.Method`, `U.Resrc`, …).

**M‑7 (Notation independence).** Intensional meaning survives notation/tool swaps.

**M‑8 (Collision & uniqueness).** Before merge, run **full‑text** + **Reserved‑Names** checks; the token must not collide with any other meaning anywhere in FPF (cf. § 7 MG·DA‑T5).

### 8.5 Alias hygiene

Aliases live **only** inside a **Context Glossary** and map to **one** technical label with an **equivalence** note (≡). No global aliases.

### 8.6 Compatibility with USM (acts vs tokens)

**LEX applies to tokens; USM applies to acts.** Mint/rename/use are **LexicalActs** that carry a USM scope (e.g., ClaimScope, WorkScope). LEX constrains **where** a token form may appear via **AllowedScopes** policies:

`LEX.TokenClass(t)=c  ⇒  USM.Scope(usage) ∈ AllowedScopes(c)`.

Example: using a `KernelToken` in a Context constraint may require a Bridge/alias; logging `Work` inside a MethodDescription violates M‑4 and the policy.

### 8.7 Acceptance & regression checks (LEX/USM)

* **SCR‑MOR‑S01 (Suffix whitelist).** Every normative token with a reserved suffix matches § 8.1 row semantics and passes Layer gates.
* **SCR‑MOR‑S02 (Kernel bans).** KernelToken names contain none of the forbidden suffixes (§ 8.2).
* **SCR‑MOR‑S03 (Prefixes).** Reserved prefixes obey § 8.3; no `U.*` minted in Context.
* **SCR‑MOR‑S04 (Run/design gate).** `Work` appears only for executions; `MethodDescription` has no runtime actuals.
* **SCR‑MOR‑S05 (Collision).** Full‑text + Reserved‑Names checks pass (no other sense of the token elsewhere).
* **SCR‑MOR‑S06 (Object‑of‑talk).** Heads pass M‑2; no bare metaphors as heads.
* **RSCR‑MOR‑E01 (DevOps firewall).** Tool/file suffixes quarantined to Context; none leak into KernelToken names.
* **RSCR‑MOR‑E02 (USM compliance).** For each LexicalAct, verify `USM.Scope ∈ AllowedScopes(LEX.TokenClass)` (see § 7.5).

### 8.8 Autonomy lexicon (L‑AUTO )
**Forbidden (Core):** bare “validity”, “actor/agent” (as free‑standing nouns), “kill switch”, “process” for behavior, “envelope” when used **as scope**.
**Use instead:** *Scope (G)* for epistemic scope; *WorkScope* for capability bounds; *RoleAssignment* for who acts; *SpeechAct* for overrides; *SafeStop* instead of “kill switch”.
**Named prefixes (policy & registry):**
* `aut:` for AutonomyBudgetDecl fields (e.g., `aut:action_tokens`, `aut:risk_bands`);
* `guard:` for guard checks bound to `AdmissibilityConditionsId`;
* `ovr:` for override SpeechActs (`ovr:PauseAutonomy`, `ovr:ResumeAutonomy`, …).

**Notes.**
1) Scope‑sensitive guards **must** declare the **Γ_time** window selector used for admission checks.
2) Proper names of patterns/components that already include “Agent/Agency” (e.g., *Agency‑CHR*, *Agent‑Tools‑CAL*) are permitted as **titled terms**; avoid re‑introducing “agent” as a free‑standing noun in new prose.

### 8.9 · LEX-CHR-STRICT — Reserve *Characteristic* for CSLC-measurable aspects

**Intent.** Prevent calling **non-measurable** objects (sets, statuses, scopes, policies, bridges, contexts, guards) “characteristics”.

**Rule L-CHR-S1 (Reservation).** Use **Characteristic** **only** for variables that **declare a CSLC scale** (nominal/ordinal/interval/ratio) with admissible values/units/polarity (Part C.16/A.17–A.18).  
**Rule L-CHR-S2 (USM).** `U.Scope` / `U.ClaimScope (G)` / `U.WorkScope` are **USM scope objects**, not Characteristics; they **must not** appear in any `CharacteristicSpace`.  
**Rule L-CHR-S3 (Status).** ESG/RSG statuses and deоntic/epistemic statuses — **not Characteristics**; its statuses/states.  
**Rule L-CHR-S4 (Lexical classifiers).** Lexical classifiers/tags — **Facets**/**attributes**; do not name them as Characteristics, if not declared **CSLC**.
**Checks.**  
— **CC-L-CHR-1.** `scope characteristic(s)` is banned in Core/Context.  
— **CC-L-CHR-2.** `CharacteristicSpace` near `Scope` — error.  
— **CC-L-CHR-3.** Canonical rewrite: `F–G–R characteristics` → `F–G–R components`.

### 8.10 LEX‑QA‑1 — Using “‑ility/‑ilities” terms (availability, reliability, …)

**Rule.** Tokens ending with **‑ility/‑ilities** or widely used quality names (**Availability, Reliability, Security, Safety, Scalability, Maintainability, Usability**, …) are **Quality‑Family labels**, not automatically CHR **Characteristics**.  

**Authoring choice:**  
— To use such a term as a **CHR** characteristic (axis), **bind** it to a **named `U.Characteristic` with one CSLC Scale** (A.18) and refer to that Characteristic in guards/UTS;  
— Otherwise **publish a Q‑Bundle** (see **C.25**) that includes **Measures (CHR)** (the measurable slots) and, where relevant, **Scope** (USM set over `U.ContextSlice`) and windows/mechanism/status fields.  

**Rationale.** Scope is **set‑valued** (USM) and **not** a CHR measurement; mechanisms/statuses are governance artefacts. Keeping them outside the CHR CSLC avoids illegal scalarisation and preserves set‑algebra semantics for scope.  (A.2.6 § 6.2; A.6.1; C.16/A.18). 



---

## 9 · Canonical rewrites for overloaded words (LEX L‑rules; normative)

> **What this section does.** LEX L‑rules standardise **how we speak** in Core/Context by mapping overloaded everyday words to **canonical FPF concepts**.
> **What this section does not do.** It does **not** restate naming (see **§ 7 MG·DA**) or morphology/casing/suffix rules (see **§ 8 LEX.Morph**); it **depends** on them.
> **Guards.** Tokens are classified by **`LEX.TokenClass ∈ {KernelToken, ContextToken, DiscriminatorToken}`** (§ 7.1). Only **CHR:ReferencePlane** may use the bare word *plane*; I/D/S are **layers**; enumerations are **Characteristics** in a **CharacteristicSpace** **only when a CSLC scale is declared; otherwise treat such slots as non-measurable attributes (not Characteristics)**.

### 9.1 Hard bans and canonical rewrites (single table; normative)

> **Use this table mechanically.** “Ban” means the weak phrase is **not allowed** in Core prose/identifiers/diagrams unless the **canonical** appears alongside it (or as a registered Context alias). “Layer/Token gates” prevent I/D/S and TokenClass leaks (cf. § 8.1).

| **L‑rule**   | **Weak / ambiguous word (Ban)**                   | **Canonical FPF target(s)**                                                                                                                                                                     | **Layer gate**                                                                       | **TokenClass gate**                         | **Notes**                                                                                            |
| ------------ | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **L‑PROC**   | *process / procedure / function step*             | `U.Method` (abstract way‑of‑doing); `U.MethodDescription` (recipe/notation‑agnostic); `U.Work` (execution); `U.WorkPlan` (schedule)                                                             | I for `Method`; D for `MethodDescription`; run artefact for `Work`; D for `WorkPlan` | Kernel/Context for types; Context for runs  | “Industrial process” as **line role** → model system + `…Role`; chemistry in `Method`/`Dynamics`.    |
| **L‑FUNC**   | *function*                                        | `U.Capability` (ability/envelope) **or** `U.Service` (promise) **or** `U.Method` (recipe) **or** `U.Work` (what happened)                                                                       | I for Capability/Service/Method; run for Work                                        | Kernel/Context                              | Never use *function* as a type name in Core.                                                         |
| **L‑SERV**   | *service* used for team/system/API/ticket/process | `U.Service` = external **promise** (access + acceptance); providers/consumers are **roles** (`…#ServiceProviderRole`) on systems; API is `accessSpec : MethodDescription`; tickets are `U.Work` | I for Service; D for accessSpec; run for Work                                        | Kernel/Context/Discriminator (per artefact) | “API = service” is forbidden; map per row.                                                           |
| **L‑SCHED**  | *schedule / plan / calendar* as execution         | `U.WorkPlan` (intent/window) vs `U.Work` (actuals/telemetry)                                                                                                                                    | D vs run                                                                             | Context                                     | Never attach actuals to a plan.                                                                      |
| **L‑ACT**    | *activity / action / task* as type                | `U.Work` (execution); **steps** belong to `U.MethodDescription` (with `requiredRoles`, capability bounds)                                                                                       | run vs D                                                                             | Context                                     | Reserve verbs: *enact* (role/RSG), *execute* (Work), *actuate* (System), *approve* (SpeechAct Work). |
| **L‑AGENT**  | *agent / actor / doer* (bare)                     | say “system **bearing** `…Role`”; use `U.AgentialRole` where needed                                                                                                                             | I                                                                                    | Kernel/Context                              | Org titles (Owner/Operator/Reviewer) live as **roles in a Context**.                                 |
| **L‑OWNER**  | *owner of X* (global)                             | Ownership is a **Role** inside a `U.BoundedContext` (e.g., `OwnerRole:ITIL_2020`); SoD via `⊥`                                                                                                  | I                                                                                    | Context                                     | No global “owner” property in Kernel.                                                                |
| **L‑CAP**    | *capability* for assignment/recipe/run/promise    | `U.Capability` only = ability with envelope; assignments are `…Role`; recipes `Method/MethodDescription`; runs `Work`; promises `Service`                                                       | I vs D vs run                                                                        | Kernel/Context                              | Holder of a Capability is a `U.System`.                                                              |
| **L‑DYN**    | *process of diffusion / growth / learning*        | `U.Dynamics` (law/model of change)                                                                                                                                                              | I                                                                                    | Kernel/Context                              | Reserve for uncaused change models.                                                                  |
| **L‑EVID**   | “paper/dataset proves/ensures”                    | `…#EvidenceRole:Context` on an **Episteme**; claims/scopes/polarity/timespan; provenance from `Work`                                                                                            | D/S                                                                                  | Context/Discriminator                       | Evidence is a **role binding**, not an actor.                                                        |
| **L‑CTX**    | *context* (fuzzy trope)                           | `U.BoundedContext` (named card)                                                                                                                                                                 | —                                                                                    | Context                                     | Never use “depends on context” in Core; **name** the Context.                                        |
| **L‑BRIDGE** | cross‑context equivalence “by same label”         | `U.Alignment` **Bridge** with relation kind, CL, loss notes                                                                                                                                     | —                                                                                    | —                                           | Same label ≠ same concept without a Bridge.                                                          |

> **Red/Green pattern (example).** ✗ “The **process** ensures quality.” → ✓ “The **MethodDescription** defines steps; **Work** is **evaluated** against **RequirementRole**.”

---

### 9.2 Quick, lintable substitutions (mechanical helpers)

> Editors may auto‑offer these rewrites; accept only if the transformed sentence passes **§ 7 MG·DA** and **§ 8 LEX.Morph** gates.

| **Ban**                         | **Canonical rewrite**                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- |
| “the process owner approves”    | `SystemX#ApproverRole:Context` **performs a SpeechAct Work** “approve …”                |
| “the document enforces policy”  | `Policy_vN#RequirementRole:Context` **gates** Work; enforcement = **SpeechAct** + audit |
| “our service runs nightly jobs” | Nightly **Work** **claimsService**(BatchProcessing); **Service** defines acceptance     |
| “the API is the service”        | API = `accessSpec : MethodDescription`; **Service = promise** with acceptance           |
| “capability assigned to team Y” | Team Y **plays** `Role`; the team (as system) **has Capability** C within envelope E    |
| “process health green”          | StateAssertion for `ObserverRole`/`Service` KPI **passes** acceptance window            |
| “function of component A fails” | **Work** performed by `SystemA#Role` **failed** acceptance (observations show …)        |
| “context is unclear here”       | **Name** the `U.BoundedContext`; else split and Bridge                                  |

---

### 9.3 Acceptance tests (LEX‑AC)

A text **passes** LEX if all answers are **Green**:

1. **Context named.** Polysemous terms appear **inside a named `U.BoundedContext`** (or the page declares a local context card).
2. **Right layer.** I/D/S layer respected: types/roles on I; recipes/docs on D; actuals on runs (cf. § 8.1 gates).
3. **Promise vs ability vs performance.** `Service` (promise), `Capability` (ability), `Work` (performance) are not conflated.
4. **No anthropomorphism.** Documents/datasets/models do not “do”; **Systems** do.
5. **Scheduling hygiene.** No actuals on `WorkPlan`; all actuals live on `Work`.
6. **Cross‑context reuse.** Any reuse across Contexts cites a **Bridge id** with CL & loss notes.
7. **MG·DA ok.** New or refactored tokens pass **§ 7 MG·DA** (anchored head noun; collision check; CharacteristicSpace for enums).
8. **Morphology ok.** Suffix/prefix/casing respect **§ 8 LEX.Morph** (e.g., `…Role`, `MethodDescription`, `Work`, reserved prefixes).
9. **Banned tokens absent.** No *process/function/task/activity* in Kernel senses; no tooling/file suffixes in Kernel tokens.
10. **State gating present (when needed).** Readiness is expressed via **RSG state** + **StateAssertion**, not vague “approved/ready”.

---

### 9.4 Coordination map (how LEX plugs into the rest of FPF)

* **With E.10.D1 D.CTX (Context discipline).**
  ULR–CTX‑1: Every Core meaning that can vary **names its `U.BoundedContext`**.
  ULR–CTX‑2: Same‑spelled labels are **distinct senses** across Contexts; reuse requires a **Bridge** (F.9) with CL & loss notes.

* **With E.10.D2 (I/D/S discipline).**
  Speak in the **right I/D/S layer**. ULR–IDS‑1..3 apply (types/roles = I; descriptions/specs = D/S; work/state assertions = evaluations/occurrences). Upgrades D→S only when **checkable acceptance** exists.

* **With A.2 / A.15 (Role–Method–Work alignment).**
  Role = **assignment**; Method = **way‑of‑doing**; MethodDescription = **documented recipe**; Work = **dated occurrence**. Sentences must keep this split.

* **With F‑cluster (Unification) & UTS (F.17).**
  Harvest in one Context → **SenseCell** → **Concept‑Set row** with relation (`≡/⋈/⊂/⟂`) and losses. UTS is the human‑readable roll‑up.

> **Acts vs tokens.** LEX applies to **tokens**; USM applies to **acts** (mint/rename/use). Conformance: `LEX.TokenClass(t)=c ⇒ USM.Scope(usage) ∈ AllowedScopes(c)` (see § 7.5).

---

### 9.5 Conformance checklist (LEX‑CC)

1. **LEX‑CC‑1 (Bans).** Any banned token in Core/Arch fails unless the **canonical** appears (or the token is a registered Context alias).
2. **LEX‑CC‑2 (Context).** Each polysemous term names its **`U.BoundedContext`**.
3. **LEX‑CC‑3 (Layer/Morph).** Usage passes **§ 8** gates (suffix/prefix/casing) and I/D/S layer checks.
4. **LEX‑CC‑4 (Bridge).** Cross‑context reuse cites **Bridge id** and CL; same‑spelled labels without a Bridge are non‑conformant.
5. **LEX‑CC‑5 (MG·DA).** New tokens pass **MG·DA** tests, including **full‑text collision** and **Reserved‑Names** checks.
6. **LEX‑CC‑6 (Service & evidence).** Service acceptance computed from **Work**; evidence is an **EvidenceRole** on an **Episteme** with provenance.
7. **LEX‑CC‑7 (USM compatibility).** For each LexicalAct, `USM.Scope ∈ AllowedScopes(LEX.TokenClass)`.

---

### 9.6 Worked micro‑examples (short, cross‑domain)

**Factory.**
✗ “The **process** failed; the **service** restarted itself.”
✓ `PLC_17#ObserverRole:PipelineOps` logged **Observations**;
`CAB_Chair#ApproverRole:ChangeControl` **performed a SpeechAct** “approve restart”;
`OpsBot#DeployerRole:CD_Pipeline_v7` **executed Work** `RestartRun‑4711` which **claimsService**(CoolingUtility);
post‑run **Evaluation** shows the **Service** acceptance **passed**.

**Cloud.**
✗ “The **process owner** approved; the **API service** deployed.”
✓ `ProductLead#AuthorizerRole:Rollout_2025` **performed a SpeechAct**;
`sCG‑Spec_ci_bot#DeployerRole:CD_Pipeline_v7` **performed Work** `Deploy‑F123`;
API = `accessSpec : MethodDescription#REST_v12`; **Service** “Feature Access” declares acceptance; telemetry **Work** shows **fulfilsService**.

**Research.**
✗ “Dataset X **proves** the theory; the **process** is reproducible.”
✓ `DatasetX#ModelFitEvidenceRole:Theory_Context` **supports** claim C within scope S;
reproducibility via **StateAssertions** on `ReplicationEvidenceRole`;
procedures are `U.MethodDescription`; re‑runs are **Work**.

---

**Editorial note.**
This section **inherits** § 7 **MG·DA** (anchored head nouns; Characteristic/CharacteristicSpace for enums; collision checks) and § 8 **LEX.Morph** (suffix/prefix/casing). It deliberately **omits** their details to avoid duplication.  The only legitimate uses of *plane* in the Core are **CHR:ReferencePlane** and the derived operators **CL^plane** and **Φ_plane**; policy flags MUST NOT introduce new “planes”. To distinguish pre‑operational vs operational states *within* **ReferencePlane=world**, use **WorldRegime ∈ {prep|live}** (formerly `PlaneRegime`).


---

# E.10.P — **Conceptual Prefixes (policy & registry)**  \[A]
 **Intent.** Provide a compact, **notation‑neutral** registry and **minting policy** for *conceptual prefixes* — short shorthands that signal **cognitive namespaces** used throughout the Core.

 **Policy (normative).**
1. **Purpose.** A conceptual prefix exists **to aid reasoning**, not to name files, serialisations, or APIs. It labels a **role in thought** (e.g., meta‑type, calculus operator, relation family).
 2. **Anchoring.** Every prefix **MUST** be anchored to a **Core architheory**  (CAL/LOG/CHR) or Kernel construct and documented in its *Relations*.
 3. **No tool lock‑in.** A prefix **MUST NOT** imply a particular notation or machine binding (see E.5.1–E.5.2).
 4. **Minting rule.** New prefixes are introduced by a **DRR** (E.9) that demonstrates
    (a) cross‑architheory need, 
    (b) non‑overlap with existing prefixes,
    (c) alignment with Pillars **P‑1/P‑5**.
 5. **Scope.** Prefixes are **globally reserved** within the Core; domain plugins  **MAY** mint local shorthands only inside their Contexts and **MUST NOT** collide with this registry.

 **Registered conceptual prefixes (Core).**
* `U.` — **U.Types meta‑namespace** (holons & primitives). *Anchor:* Kernel Part A.
* `Γ_` — **Calculus operator family** (by flavour: `Γ_sys`, `Γ_epist`, …). *Anchor:* Part B umbrella on Γ.
* `ut:` — **Universal relation family** (e.g., `PartOf` sub‑relations). *Anchor:* A.14 (Mereology) — informative alias vocabulary.
* `tv:` — **Trace & Validation vocabulary** (CT2R‑LOG): `tv:AliasOf`, `tv:groundedBy`. *Anchor:* B.3 (Trust & Assurance, LOG‑use). 
* `ev:` — **Evidence hooks** (bindings/roles). *Anchor:* A.10 / B.3 (Evidence Graph Referring).
* `mero:` — **Mereology trace types** (internal labels: `SumTrace` / `SetTrace` / `SliceTrace`) used **informatively** in examples. *Anchor:* B.1 (Γ‑aggregation).

**Conformance Checklist (E.10.P).**
* **CC‑LEX‑P.1** New Core text **SHALL NOT** introduce an unregistered conceptual prefix.
* **CC‑LEX‑P.2** Each occurrence of a registered prefix **SHALL** cite its anchor pattern on first use in a section.
* **CC‑LEX‑P.3** Examples that expand a prefix into a concrete URI or syntax **MUST** mark the expansion *informative* and locate it in Tooling/Pedagogy.

**Relations.** Constrains E.5.1 (Lexical Firewall) & E.5.2 (Notational Independence); Depends on E.9 (DRR).
  

---

# E.10.D1 — Lexical Discipline for “Context” (D.CTX) \[D]

> **One‑sentence summary.** Make the word **Context** unambiguous: in FPF it **only** denotes the formal primitive **`U.BoundedContext`**; remove the term **anchor**; reserve **Problem Frame** for situational narrative; treat **Domain** as an **informative family label**, not a type.

**Status.** Discipline \[D], architheory‑agnostic.
**Depends on.** C‑6 *Strict Distinction*; C‑7 *Temporal Duality*; G‑1 *Minimal Generality*; G‑2 *Contextual Specification*.
**Coordinates with.** E.10.U1 *Domain‑Family Landscape Survey*; E.10.U2 *Term Harvesting & Normalisation*; E.10.U7 *Concept‑Set Table*; E.10.U9 *Alignment/Bridge*; `RoleAssigning` patterns (e.g., E.10.U4).
**Aliases (informative).** Context Discipline; No‑Anchor Rule.

---


---

## E.10.D2 — Intension–Description–Specification Discipline (I/D/S) \[D]

*Definitional pattern — normative, notation‑agnostic*

> **One‑sentence summary.** For every intensional FPF object (e.g., `U.Role`, `U.Method`, `U.System`, `U.Work`, `U.Service`), clearly distinguish the **thing itself** (*Intension*), its **context‑bound Description** (KU), and its **formal Specification** (KU). Use **–Spec** only when strict, testable invariants and an acceptance harness exist; otherwise use **–Description**. This keeps semantics clean, didactic, and testable across all architheories.

**Status.** Definitional [D], architheory‑agnostic.
**Builds on:** A.7 **Strict Distinction (Clarity Lattice)**; E.10.D1 **D.CTX (Context ≡ U.BoundedContext)**; C.2.1 **U.EpistemeSlotGraph (DescriptionContext, IDS‑13)**; C.2.3 **Unified Formality Characteristic (F)**.
**Coordinates with.** F.4 **Role Description**; F.5 **Naming Discipline**; F.10 **Evaluation**; F.15 **SCR/RSCR Harness**.
**Non‑goals.** No editors, workflows, registries, or storage formats. No tooling commitments.

### 1 · Problem frame

**Intent.** Prevent perennial confusions such as “the role contains the checklist” or “the method is the document.” Establish a universal discipline so that:

* **Intensions** (e.g., `U.Role`, `U.Method`) remain I/D/S layer‑pure and context‑agnostic entities in the kernel.
* **Descriptions** (KUs) capture human‑readable, **Context‑local** semantics (labels, glosses, characterisations, state graphs, checklists).
* **Specifications** (KUs) exist **only** when there are verifiable invariants, an acceptance harness, **and a declared Formality F adequate for checkability (C.2.3; default F ≥ F4)**, making claims testable.

**Applicability.** Whenever an FPF text introduces or uses an intensional `U.Type` (e.g., `U.Role`, `U.Method`, `U.Service`, `U.System`, `U.Work`, `U.RCS`, `U.RSG`, `U.RoleEnactment`) in any part (A–H).

### 2 · Problem 

1. **Plane/layer mixing.** Intensions are routinely conflated with their documents and with runtime facts.
2. **Name drift.** “Spec” gets used for any write‑up; “status” drifts between states of a role and epistemic/deontic statuses over knowledge units.
3. **Didactic friction.** Inconsistent naming raises cognitive load and impedes reuse across architheories.
4. **Unverifiable claims.** Without a clear gate to **–Spec**, normative wording appears without testability.

### 3 · Forces

| Force                        | Tension to resolve                                                                |
| ---------------------------- | --------------------------------------------------------------------------------- |
| **Simplicity vs rigour**     | Easy‑to‑learn naming vs the need for machine‑checkable invariants.                |
| **Universality vs locality** | Kernel intensions must be universal; language and criteria are **Context‑local**. |
| **Stability vs evolution**   | Names should be stable; artefacts must mature via **ΔF** along the **F** ladder cleanly. |

### 4 · Solution — the I/D/S layer + a formal Spec‑gate

#### 4.1 The triad (applies to **any** intensional `U.T`)

**Terminology discipline (normative).** Say **I/D/S layers** when you mean the **stratified order with a Spec‑gate**; say **I/D/S triad** only to note **three‑ness without order or dependency**. **Do not call I/D/S a “plane”.** Reserve **plane** for uses explicitly defined elsewhere (e.g., **`CHR:ReferencePlane`** and status families).
**Layer semantics (clarity).** **I‑layer** = **kernel/intensional type** (non‑epistemic; **not** a episteme) . **D‑layer** and **S‑layer** = **epistemic Knowledge Units** (KUs). The **Spec‑gate** upgrades a Description to a Specification only under declared checkability and harness conditions (unchanged).

For every intensional type `U.T`:

* **Intension — `U.T`.**
  The thing itself (e.g., `U.Role`, `U.Method`, `U.Service`, `U.System`, `U.Work`, `U.RCS`, `U.RSG`).
  *It does **not** contain documents, checklists, or carriers; it is not a runtime event or a file.*

* **Description episteme — `U.TDescription(@Context)`**
  A **Context‑local** knowledge unit that **characterises** `U.T` with labels (Tech/Plain), glosses, and, when applicable, **Role Characterisation Space (`U.RCS`)**, **Role State Graph (`U.RSG`)**, and **state conformance checklists**.
  *Readable, precise, didactic; may reference evaluation criteria but does not assert testable “shall”s by itself.*

* **Specification episteme — `U.TSpec(@Context)`**
  A **Context‑local** knowledge unit that states **testable invariants** for `U.T` and is **bound to an acceptance harness**.
  *Normative, verifiable, suitable for SCR/RSCR (F.15).*

> **Key phrasing discipline.** Intensions are **characterised by** (not “contain”) RCS/RSG/checklists, which **live in** the Description/Spec.
> **Terminology guard.** To avoid collisions with **ReferencePlane** and other semantic planes, the I/D/S triad is referred to as **I/D/S Layers** (Intension Layer · Description Layer · Specification Layer). The word **plane** is reserved for **semantic planes** (Role/Status/Measurement/Type‑structure/Method/Work, etc.) and for the **ReferencePlane** field used in describedEntity/assurance.

#### 4.2 The Spec‑gate (when “–Spec” is allowed)

Use the **–Spec** suffix **only if all** of the following hold:

1. **Formality F (C.2.3):** the artefact declares **F ≥ F4** (or a context-defined higher threshold) so predicates are checkable.
2. **Verifiability:** invariants are stated as checkable predicates or thresholds.
3. **Harness bound:** there is a linked **acceptance harness** (SCR/RSCR matrices per F.15).
4. **Context anchoring:** all wording is explicitly local to a named `U.BoundedContext` (E.10.D1).

If any condition is missing, the artefact **must be** a `…Description`.

#### 4.3 Where RCS/RSG and evaluations sit

* **`U.RCS` (Role Characterisation Space)** and **`U.RSG` (Role State Graph)** are **intensional** types that structure the space of role characteristics and permissible state transitions.
* Their **human presentation** (characteristics, dimensions, node labels, admissible transitions) lives in the **RoleDescription**, and becomes part of **RoleSpec** only when the transitions and state predicates are made **testable** and harness‑bound.
* **`U.Evaluation`** operates on **evidence** against the conformance checklist (from the Description/Spec) to produce a **state attestation** (“X is in state S @Context within window W”).
* **Epistemic/deontic statuses** (e.g., *Evidence*, *Requirement*, *Standard*) are **roles over Epistemes** (not states of the role). They are governed elsewhere (F‑R family) and must not be conflated with `U.RSG` state names.

#### 4.4 Plain‑language memory hook

> *Thing vs words vs rules.*
> **The thing** (`U.Role`, `U.Method`) is clean and abstract.
> **The words** (labels, glosses, RCS/RSG pictures, checklists) live in the **Description**.
> **The rules** (testable “shall”s with harness) live in the **Specification**.
> If you can’t test it, don’t call it **Spec**.

### 5 · Minimal vocabulary & naming discipline (this pattern only)

**Core trio (per intensional `U.T`).**

* **`U.T` — the Intension.**
  Kernel object (e.g., `U.Role`, `U.Method`, `U.Service`, `U.System`, `U.Work`, `U.RCS`, `U.RSG`).
  *Never* a document, *never* an event, *never* a file.

* **`U.TDescription(@Context)` — the Description Episteme.**
  Context‑local characterisation of `U.T`: Tech/Plain labels, gloss, notes; for roles, may **characterise** with an `U.RCS` (characteristics/traits), an `U.RSG` (states/transitions), and **state conformance checklists** (per state). *Readable; precise; not yet a set of testable “shall”s.*

* **`U.TSpec(@Context)` — the Specification Episteme.**
  Context‑local, **testable** invariant set for `U.T`, explicitly **bound to an acceptance harness** (SCR/RSCR matrices per F.15). Use **–Spec** only through the Spec‑gate (Sec. 4.2).

**Suffix rules.**

* Use **`…Description`** by default (M‑mode or F‑mode without harness).
* Use **`…Spec`** *only* when **all** Spec‑gate conditions (Sec. 4.2) hold.
* No alternative suffixes (“Profile”, “Definition”, “Guide”) inside the Core; such epistemes live in pedagogy/tooling layers, not in the I/D/S discipline.

**Naming morphology (recap of F.5 as it applies here).**

* Two registers: **Tech** and **Plain** labels on every Description/Spec.
* Roles use **count nouns** (e.g., *Operator*); states use **state nouns** (e.g., *Approved*).
* Statuses over knowledge (e.g., Evidence/Requirement) are **not** role states; they name **roles over Epistemes** (F‑R family), not nodes in `U.RSG`.

**Context anchoring.**
Every Description/Spec is **local to** a `U.BoundedContext` (E.10.D1). Phrases in the episteme must read correctly once prefixed by the Context name (e.g., “(ITIL4) Acceptance criteria …”).

**Carriers.**
`U.Carrier` holds **encodings** of a Description/Spec; the Episteme’s identity is **not** the file. *Never* say “the role contains the checklist in the PDF”; say “the **RoleDescription** characterises the role with checklists; this **carrier** encodes them.”

**Time stance.**
Descriptions/Specs must declare DesignRunTag when inherent (e.g., RoleDescription is design‑time; state attestation via `U.Evaluation` is run‑time).

### 6 · Invariants (normative)

**IDS‑1 (Plane purity).**
An intensional `U.T` **MUST NOT** be conflated with its Description/Spec or with any `U.Carrier` or `U.Work`.

**IDS‑2 (Context locality).**
Every `…Description/…Spec` **MUST** name a `U.BoundedContext`. Wording inside is read **as‑local**; no global meaning is implied.

**IDS-3 (Spec-gate).**
A episteme **MUST NOT** use the **–Spec** suffix unless: *(a)* the artefact declares **`U.Formality = Fk` with k ≥ 4** per **C.2.3**, *(b)* invariants are testable predicates, *(c)* an acceptance harness is linked (F.15), *(d)* Context is explicit.

**IDS‑4 (Characterisation verbs).**
Texts **MUST** say: *“`U.Role` is **characterised by** `U.RCS`/`U.RSG` in the RoleDescription”*.
They **MUST NOT** say: *“the role **contains** the RCS/RSG”*.

**IDS‑5 (RCS/RSG scope).**
`U.RCS`/`U.RSG` are **intensional structures**. Their **presentations** (characteristics, state names, admissible transitions, checklists) live in the **RoleDescription**, and in **RoleSpec** only when transitions and state predicates are fully testable.

**IDS‑6 (Evaluation semantics).**
`U.Evaluation` **MUST** operate over evidence against conformance checklists from the Description/Spec and **MUST** produce a **state attestation** (who/what is in state *S* @Context within window *W*). Evaluation **does not** mutate the intensional object.

**IDS‑7 (Status separation).**
Epistemic/deontic statuses (Evidence/Requirement/Standard) are roles over **knowledge units**; they **MUST NOT** be used as state names in `U.RSG`.

**IDS‑8 (Register discipline).**
Every Description/Spec **SHOULD** include both **Tech** and **Plain** labels. Symbolic aliases are optional and informative.

**IDS‑9 (No stealth bridges).**
Descriptions/Specs **MUST NOT** import meanings from other Contexts by shared labels. Cross‑context relations exist only as **F.9 Bridges**.

**IDS‑10 (Window honesty).**
When an evaluation is time‑bounded, the **window** **MUST** be stated in the attestation.

**IDS‑11 (Ladder clarity).**
A Description may mature into a Spec by satisfying IDS‑3; the opposite move requires a rationale (loss of testability) and must drop the **–Spec** suffix.

**IDS‑12 (Didactic bound).**
A RoleDescription **SHOULD** fit on one screen per state graph plus one screen of notes; sprawling documents belong to pedagogy, not to the core Description.

### 7 · Reasoning primitives (judgement schemas, notation‑free)

> Judgements are **mental moves**—they assert what follows when premises hold. They do **not** imply queries, storage, or workflows.

1. **Description link (with DescriptionContext)**

   ```
   U.T, C, Vp ⊢ isDescriptionOf(TDesc, U.T, C, Vp)
   ```

   *Reading:* `TDesc` is the Context‑local Description of `U.T` in Context `C` under Viewpoint `Vp`. Its `subjectRef` decodes to `DescriptionContext = ⟨DescribedEntityRef(U.T), C, Vp⟩` (IDS‑13, C.2.1 §6.1).

2. **Spec link (Spec‑gate, viewpoint‑local)**

   ```
   isDescriptionOf(TDesc, U.T, C, Vp) ∧ U.Formality(TSpec) ≥ F4
      ∧ testableInvariants(TSpec) ∧ harnessBound(TSpec)
      ∧ sameDescriptionContext(TSpec, TDesc)
      ⊢ isSpecOf(TSpec, U.T, C, Vp)
   ```

   *Reading:* Only when F‑mode, testability, harness, and a matching `DescriptionContext` are present may we judge `TSpec` a Specification of `U.T` in `C` under Viewpoint `Vp`.

3. **Role characterisation**

  ```
   isDescriptionOf(RoleDesc, U.Role, C, Vp)
   ∧ characterises(RoleDesc, U.RCS) ∧ characterises(RoleDesc, U.RSG)
   ⊢ characterisedBy(U.Role, {U.RCS, U.RSG}) @C
  ```

   *Reading:* The role is *characterised by* the RCS/RSG as presented in the Description (which is pinned to `(C, Vp)`), not that it “contains” them.

4. **State conformance predicate**

   ```
   checklistFor(RoleDesc, state S) = χ
   ∧ evidence E within window W
   ⊢ conformsToState(E, χ, W) ⇒ attestation(subject ∈ S @C, W)
   ```

   *Reading:* Evidence satisfies the checklist for state `S`, yielding a state attestation.

5. **Transition admissibility**

   ```
   U.RSG allows (S → S') @C
   ∧ attestation(subject ∈ S @C, W)
   ∧ conformsToState(E', checklistFor(S'), W')
   ⊢ admissibleTransition(subject : S → S' @C)
   ```

   *Reading:* A move from `S` to `S'` is admissible when RSG permits it and `S'` is satisfied.

6. **Status / state separation guard**

   ```
   statusOverKU(KU, σ) ∧ stateInRSG(ρ)
   ⊢ σ ≠ ρ  (distinct planes)
   ```

   *Reading:* A status over a knowledge unit is not a role‑state.

7. **No Cross‑context import**

   ```
   isDescriptionOf(TDescA, U.T, CA, VpA) ∧ isDescriptionOf(TDescB, U.T, CB, VpB) ∧ CA≠CB
   ⊢ ¬equateByLabel(TDescA, TDescB)  (bridges required in F.9)
   ```

   *Reading:* Identical wording across Contexts (and Viewpoints) does not grant equivalence; only Bridges may relate them.

### 8 · Anti‑patterns & remedies

| ID   | Anti‑pattern                | Symptom                                                              | Why it harms thinking                     | Remedy (concept move)                                                                          |
| ---- | --------------------------- | -------------------------------------------------------------------- | ----------------------------------------- | ---------------------------------------------------------------------------------------------- |
| A‑1  | **Spec‑by‑name**            | Every write‑up is titled “Spec”.                                     | Inflates normativity; untestable claims.  | Apply **Spec‑gate** (IDS‑3). If any condition fails, rename to `…Description`.                 |
| A‑2  | **Role contains RSG**       | “The role contains a state graph.”                                   | Plane mixing; mereological confusion.     | Use **characterised by** phrasing (IDS‑4); RSG presentation lives in RoleDescription/RoleSpec. |
| A‑3  | **Status ≡ state**          | *Approved* (status over episteme)  appears as a node in the role graph.     | Cross‑plane conflation; logic errors.     | Keep **statuses** (over Epistemes) separate from **role states** (IDS‑7).                            |
| A‑4  | **Stealth bridge**          | Copying state names across Contexts to imply sameness.                  | Hidden cross‑context import.              | Declare an **F.9 Bridge** or accept divergence (IDS‑9).                                        |
| A‑5  | **Checklist = process**     | Treating conformance checklist as an execution workflow.             | Category error (design vs run).           | Checklists are **criteria** used by `U.Evaluation`; executions live under `U.Work`.            |
| A‑6  | **Carrier identity**        | File path/version treated as “the spec itself.”                      | Identity drift; archival brittleness.     | Identity is the **KU**; `U.Carrier` is only an encoding (Sec. 5).                              |
| A‑7  | **Windowless verdict**      | Attestations omit time window.                                       | Unreproducible results; stale judgements. | Require **window** in attestation (IDS‑10).                                                    |
| A‑8  | **Over‑formal Description** | Description bloats into a standard; unreadable.                      | Violates didactics; blocks adoption.      | Enforce **one‑screen** discipline (IDS‑12); move exegesis to pedagogy.                         |
| A‑9  | **Spec without harness**    | “Shall” statements with no linked acceptance matrices.               | Unverifiable normativity.                 | Bind to **SCR/RSCR harness** (F.15) or downgrade to Description (IDS‑3).                       |
| A‑10 | **Global language leakage** | Description reads as universal definition rather than Context‑local. | Breaks locality; fuels conflicts.         | Prefix mentally with the Context; rewrite locally (IDS‑2).                                        |

### 9 · Worked examples (multi‑architheory, didactic)

> Each vignette shows **intension ↔ Description/Spec ↔ Evaluation** with **context‑local** wording. No workflows; only thinking moves.

#### 9.1 Enactment (Role Assignment & Enactment line) — *Change Authority* role (ITIL 4 Context)

**Contexts.** `ITIL4_2020` (services/deontics), `PROV_O_2013` (run‑time traces).
**Intension.** `U.Role :: ChangeAuthority` — a behavioural mask that may be worn by a system (person/team/tool) to **authorise** a change.

**RoleDescription\@ITIL4.**

* **Tech/Plain.** *ChangeAuthority* / “change approver”.
* **RCS (characteristics).** CredentialLevel ∈ {L1,L2}; Scope ∈ {Service, Platform}; SeparationOfDuty ∈ {Clean, Violates}.
* **RSG (states).** `Proposed → Designated → Authorized → Active → Suspended → Revoked`.
* **State checklists (sketch).**

  * *Authorized:* { valid nomination, SoD=Clean, credential ≥ required, mandate window set }.
  * *Active:* *Authorized* ∧ { current shift/roster entry ∧ no conflicting active duty }.

**Evaluations.**
`U.Evaluation@ITIL4` over evidence (roster entries, mandate doc, SoD list, PROV Activities of approvals) yields **attestations**:

* `subject=Team‑X ∈ Authorized@ITIL4 in ⟨2025‑08‑01, 2025‑12‑31⟩`.
* Later, `subject=Team‑X ∈ Active@ITIL4 at 2025‑09‑14T10:05Z`.

**Didactic hooks.**

* The **role** is *characterised by* RCS/RSG in the **RoleDescription**; it **does not contain** them.
* The **attestation** is a statement about state‑in‑window; it does **not** mutate the role.

#### 9.2 Method (Essence‑language Context) — *Backlog Refinement* method

**Contexts.** `OMG_Essence_Language_2023` (method language), `PROV_O_2013` (runtime).
**Intension.** `U.Method :: BacklogRefinement`.

**MethodDescription\@Essence.**

* **Tech/Plain.** *BacklogRefinement* / “tidy backlog”.
* **Inputs/Outputs (informative).** Work items (ideas) → clarified items (ready/not‑ready tags).
* **RCS (characteristics).** Cadence ∈ {weekly, continuous}; CollaborationMode ∈ {sync, async}.
* **RSG (states).** `Sketched → Defined → Adopted`.
* **State checklist (Adopted).** { team agreed practice note exists, cadence set, entry/exit criteria published }.

**Spec‑gate outcome.**
No acceptance harness yet → remains **MethodDescription**, **not** MethodSpec.

**Run‑time echo.**
`U.Work` instances (calendar sessions, chat threads) are traced in PROV; **Evaluation** can check whether an *Adopted* practice is being followed in window W without ever reifying the method as a workflow.

#### 9.3 Service (SLO/SLA) — *Calibration Service* (ITIL 4 + SOSA/SSN Contexts)

**Contexts.** `ITIL4_2020` (service), `SOSA_SSN_2017` (observation), `ISO_80000_1_2022` (units).
**Intension.** `U.Service :: CalibrationService`.

**ServiceDescription\@ITIL4.**

* **Tech/Plain.** *CalibrationService* / “we calibrate your sensor”.
* **Acceptance facet (informative).** *SLO: error ≤ 0.5% FS under ISO 80000 units*; **formal criteria live in** ServiceSpec only if harness exists.

**Evaluation\@ITIL4+SOSA.**
Observations (SOSA) from test runs compared with thresholds → **ServiceEvaluation** attests *Met/Not‑Met* in a stated window.
No Cross‑context import: ISO units cited **as context‑local** references.

#### 9.4 Epistemic (KD‑line) — *Evidence status vs role state*

**Contexts.** `PROV_O_2013` (provenance), `FPF_Evidence_Status` (status family).
**Intensions.** `U.KnowledgeUnit :: Report_42`; `U.EvidenceStatus :: SupportsClaim`.

**Separation.**

* `SupportsClaim@C` is a **status over a Episteme** (classifies the report).
* It is **not** a node of any role’s `U.RSG`.
* `U.Evaluation` produces `attestation(Report_42 has EvidenceStatus=SupportsClaim@C, W)`.

**Didactic point.**
State names in *role* graphs do not duplicate **statuses**; planes stay disjoint.

#### 9.5 Control (Sys‑CAL line) — *Control‑Operator* role (IEC 61131‑3 Context)

**Contexts.** `IEC_61131_3` (control languages), `ISA_95` (integration).
**Intension.** `U.Role :: ControlOperator`.

**RoleDescription\@IEC61131‑3.**

* **RCS.** StationLevel ∈ {Cell, Line}; TaskMode ∈ {Cyclic, Event}; AlarmPrivileges ∈ {Ack, Ack+Shelve}.
* **RSG.** `Onboarded → Authorized → ConsoleActive → Paused → Suspended`.
* **Checklists (ConsoleActive).** { Authorized ∧ current console login ∧ task watchlist loaded }.

**Attestation (run‑time).**
`subject=Operator‑A ∈ ConsoleActive@IEC at 2025‑09‑14T08:00Z` based on log evidence.
No “workflow” required in the Description.

### 10 · Relations (with other patterns)

**Builds on:**

* **E.10.D1 — Lexical Discipline for “Context” (D.CTX).** Provides the *Context* primitive and bans “anchor” talk.
* **A.7 — Strict Distinction (Clarity Lattice).** This pattern concretises SD for intension vs description/spec vs carrier vs work.
* **C.2.3 — Unified Formality Characteristic (F).** Supplies the **F** anchors and **ΔF** moves that gate `…Spec`.

**Constrains:**

* **F.1–F.3 (Contexts → seeds → local senses).** Descriptions **must** cite context‑local senses (SenseCells) rather than global words.
* **F.4–F.5 (role/service naming).** Tech/Plain labels on Descriptions obey F.5 morphology rules.
* **F.8 (Service Acceptance Binding).** Evaluations of services read acceptance **from Description/Spec**, compare against Observations.
* **F.9 (Alignment & Bridge).** No Description/Spec may imply Cross‑context equivalence; Bridges carry all Cross‑context semantics.
* **F.15 (SCR/RSCR Harness).** Any `…Spec` must link to its harness; RSCR re‑checks verdict stability across editions/windows.

**Is used by.**

* **Part C architheories.** Sys‑CAL, KD‑CAL, Kind-CAL, Method‑CAL cite `…Description/…Spec` epistemes explicitly and consume **state attestations** from `U.Evaluation`.
* **Part B trust calculus.** Uses the presence/absence of harnessed Specs and the windowed nature of attestations in confidence roll‑ups.

### 11 · Migration notes (conceptual refactor playbook)

> Goal: remove conflations and normalise names without changing underlying models.

1. **Rename by default.** Any `XSpec` lacking a bound acceptance harness becomes **`XDescription`**. Keep content intact; change suffix and preface with a “Description, not Spec” note.
2. **Promote selectively.** For epistemes that *are* testable and declare **F ≥ F4**, add harness links (F.15) and re-label as **`XSpec`** via the Spec-gate.
3. **Fix the verbs.** Rewrite “Role contains RSG/RCS” → “Role is **characterised by** RSG/RCS in RoleDescription”.
4. **Detach carriers.** Replace identity‑by‑file with **`U.Carrier` encodes …Description/Spec** wording.
5. **Add Contexts.** Where a Description drifts globally (“the backlog refinement is…”), prefix with the Context and adjust wording to be **local**.
6. **Split planes.** Move any Evidence/Requirement **statuses** out of role state lists; keep them as roles over **knowledge units**.
7. **Window‑ise verdicts.** Ensure every evaluation statement adds an explicit **window** (instant or interval).
8. **Document maturity.** **Declare each Description’s F** (C.2.3) and track **ΔF** promotions/demotions as part of change notes (no governance implied).

### 12 · Acceptance tests (SCR/RSCR — concept‑level)

#### 12.1 Static conformance checks (SCR)

* **SCR-D2-S01 (Suffix discipline).** Every episteme with suffix **–Spec** passes the **Spec-gate** (**F ≥ F4** ∧ testable invariants ∧ harness link ∧ Context named). Otherwise it bears **–Description**.
* **SCR‑D2‑S02 (Characterisation verbs).** Texts never say an intension “contains” RCS/RSG; they say it is **characterised by** them via the Description/Spec.
* **SCR‑D2‑S03 (Plane purity).** No episteme mixes role **states** and knowledge **statuses**; each appears only on its correct plane.
* **SCR‑D2‑S04 (context‑locality).** Every Description/Spec names its `U.BoundedContext`; wording reads correctly when prefixed by the Context.
* **SCR‑D2‑S05 (Two registers).** Tech **and** Plain labels present on all Descriptions/Specs.
* **SCR‑D2‑S06 (Carrier separation).** Identity statements refer to Epistemes; files are referenced only as `U.Carrier` encodings.
* **SCR‑D2‑S07 (Windowed evaluation).** All state attestations cite a window `W` (instant or interval).

#### 12.2 Regression checks (RSCR)

* **RSCR‑D2‑E01 (Spec demotion guard).** If a **–Spec** loses its harness or testability, it is demoted to **–Description**; diffs show no lingering “shall” claims.
* **RSCR‑D2‑E02 (Bridge drift).** If two Contexts begin to share identical labels, verify no Descriptions/Specs imply Cross‑context identity; add or revise **F.9 Bridges** instead.
* **RSCR‑D2‑E03 (Edition churn).** When a Context’s canon updates, previously valid attestations remain historical (windowed); new Specs/Descriptions cite the new edition.
* **RSCR‑D2‑E04 (Verb hygiene).** Automated grep over corpus finds “contains RSG/RCS” phrasing; none remain after refactor.
* **RSCR‑D2‑E05 (Status bleed).** Spot‑audit a random sample of role graphs to ensure no epistemic/deontic statuses appear as role states.

*Didactic takeaway.*
Think in three layers: **Intension** (what the thing *is*), **Description/Spec** (how we *state* its character and, when mature, *test* it), and **Evaluation** (what we can *attest* about it in a **window**). Keep Contexts local, planes separate, and “contains” out of your vocabulary.

### 13 · Author’s pocket guide (carry‑in‑mind rules)

> **Use these as thinking cues, not as paperwork.** Each cue is a one‑breath test you can apply while writing.

1. **Name the Context.** Write “*Role (ITIL4)*”, “*Method (Essence‑language)*”, “*Execution (PROV)*”. Never speak global words.
2. **Pick the *object-of-talk*.** Am I talking about an **intension** (Role/Method/Service), a **Description/Spec**, an **Evaluation**, or a **Carrier**? Stay on one object-of-talk per sentence.
3. **Prefer –Description.** Use **`…Description`** by default. Switch to **`…Spec`** only after the **Spec‑gate** (testable invariants + harness + F‑mode).
4. **Characterised by…** Say *“Role is **characterised by** RCS/RSG recorded in RoleDescription”*, never *“Role **contains** its states”*.
5. **Window every verdict.** An Evaluation must read “*X ∈ State\@context **in** W*”. No naked, timeless verdicts.
6. **Status ≠ state.** Role **states** live in `U.RSG`; Evidence/Requirement **statuses** classify **knowledge units**. Do not mix.
7. **Bridge later.** If two Contexts “feel the same”, write the itch down and leave it for **F.9 Bridge**.
8. **Two registers.** Every Description/Spec has **Tech** and **Plain** labels; prefer the shortest tech term that matches the invariants.
9. **Carrier humility.** Files and records are **Carriers** of Descriptions/Specs; they don’t *equal* the thing you reason about.
10. **Spec = test.** If you can’t point to a harness that would falsify it, it isn’t a **Spec** yet.

### 14 · Phrasebook & pitfall table (say this, not that)

| Mistaken phrasing (avoid)              | Didactically correct phrasing (use)                                                                                  | Why                                                                                        |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| “The Role **contains** its states.”    | “The **Role** is **characterised by** RCS/RSG **recorded in** the RoleDescription.”                                  | Roles are intensions; state graphs live in their **Descriptions/Specs** (knowledge plane). |
| “MethodSpec (draft).”                  | “**MethodDescription** (Essence‑language Context); not a Spec yet.”                                                     | **–Spec** is reserved for testable artifacts that passed the Spec‑gate.                    |
| “We proved the service meets the SLO.” | “**Evaluation** attests *Service ∈ Met\@ITIL4 in W* based on observations and the **Acceptance harness**.”           | Evaluations produce **windowed attestations**, not timeless facts.                         |
| “Evidence status is a role state.”     | “**Evidence status** classifies a **KnowledgeUnit**; **Role states** live in RSG. Different planes.”                 | Prevents status/state conflation.                                                          |
| “The PDF is the Method.”               | “The PDF is a **Carrier** that **encodes** a **MethodDescription**.”                                                 | Carrier ≠ content.                                                                         |
| “BPMN workflow = PROV activity.”        | “Add a **Bridge (F.9)** if needed; in F.1/F.2/F.3 we treat them as **context‑local** senses.”                           | No Cross‑context identity outside Bridges.                                                    |
| “WorkSpec / WorkPlan (synonyms).”      | “**U.WorkPlan** (preferred). **WorkDescription** is an allowed alias; **WorkSpec** is deprecated.”                   | Aligns with the –Description/–Spec discipline.                                             |
| “RoleSpec is our template.”            | “**RoleDescription** is our template; promote to **RoleSpec** once the harness exists.”                              | Keeps the Spec word meaningful.                                                            |
| “Spec says the same in all Contexts.”     | “Each **Spec/Description** is **context‑local**; Cross‑context reuse requires an **Alignment Bridge** with CL/loss notes.” | Locality guard.                                                                            |

### 15 · Naming & alias policy (normative, notation‑free)

#### 15.1 Suffix discipline (recap).**

* **Preferred default:** **`…Description`** for Role/Method/Service/Work.
* **Reserved:** **`…Spec`** only if the item passed the **Spec‑gate** (F‑mode, testable invariants, harness id, Context named).
* **Banned:** Using **–Spec** as a synonym for “detailed description”.

#### 15.2 Canonical/alias map (current edition).**

| Concept (intension) | Preferred episteme name      | Allowed alias (equal scope)   | Deprecated alias | Notes                                                                                 |
| ------------------- | ---------------------- | ----------------------------- | ---------------- | ------------------------------------------------------------------------------------- |
| Role                | **RoleDescription**    | RoleCard *(Pedagogy only)*    | —                | *RoleCard* is informal (teaching layer), not a normative episteme name.                     |
| Role (F‑mode)       | **RoleSpec**           | —                             | —                | Only after Spec‑gate.                                                                 |
| Method              | **MethodDescription**  | —                             | **MethodSpec**   | Global rename complete; legacy references should be updated.                          |
| Method (F‑mode)     | **MethodSpec**         | —                             | —                | Now reserved for harnessed, testable methods.                                         |
| Work (schedule)     | **U.WorkPlan**         | **WorkDescription**           | **WorkSpec**     | *WorkSpec* alias removed; *WorkDescription* remains as didactic alias for *WorkPlan*. |
| Service             | **ServiceDescription** | ServiceCard *(Pedagogy only)* | —                | As above: Card is informal only.                                                      |
| Service (F‑mode)    | **ServiceSpec**        | —                             | —                | Requires acceptance harness id (F.15).                                                |

#### 15.3 Verb & morphology rules.**

* **Verbs.** Use *characterised by*, *recorded in*, *encoded by*; avoid *contains*, *is stored in*, *is implemented by* when speaking at the conceptual level.
* **Morphology.**

  * Roles name **masks** as **count nouns** (*Operator, ChangeAuthority*).
  * States as **state nouns/participles** (*Authorized, Active*).
  * Status names are **classifiers over knowledge** (*SupportsClaim, NormativeStandard*).
  * Descriptions/Specs use neutral nouns (*RoleDescription, MethodSpec*).

#### 15.4 Deprecations (effective now).**

* **MethodSpec** (as a general name) → **MethodDescription** unless Spec‑gate is met.
* **WorkSpec** (alias for WorkPlan) → **WorkDescription** (allowed alias), or **U.WorkPlan** (preferred).
* Texts must avoid “contains RSG/RCS” phrasing (see RSCR‑D2‑E04).

### 16 · Quick templates (fill‑in‑mind, not forms)

> Copy these **lines** into your prose as thinking scaffolds. They are not schemas, fields, or checklists to fill; they are didactic prompts.

### 16.1 Role (default).

* *Intension.* `U.Role :: <TechName> in <ContextId>`.
* *RoleDescription\@context.* Tech/Plain: **`<TechName> / <PlainName>`**.

* **RCS characteristics.** `<characteristic₁ ∈ {...}>; <characteristic₂ ∈ {...}>`.
* **RSG nodes (→).** `<S₀ → S₁ → ... → Sₙ>`.
* **State checklist (one node).** `<StateX : {criterion₁, …}>`.
* *Evaluation attestation.* `subject=<Holder> ∈ <StateX>@<ContextId> in <Window> (evidence: <cue₁,…>)`. 

#### 16.2 Method (Essence‑language Context).

* *Intension.* `U.Method :: <TechName>`.
* *MethodDescription\@context.* Inputs/Outputs (informative), **RCS/RSG** (if you track adoption).
* *Spec upgrade (optional).* “Becomes **MethodSpec** when harness `<id>` exists.”

#### 16.3 Service (acceptance‑bearing).**

* *ServiceDescription\@context.* Tech/Plain; **Acceptance facet** (informative until harnessed).
* *Evaluation.* `Service ∈ Met/Not‑Met@context in <Window>` based on observations and acceptance criteria.

#### 16.4 Alignment reminder.

* “No Cross‑context identity is implied; if needed, add **F.9 Bridge**: `<ContextA:TermA> ↔ <ContextB:TermB>` with CL/loss notes.”

### 17 · Didactic distillation (90‑second script)

> **“Three layers; one context; no leakage.”**

1. **Pick the Context.** Every word lives **inside** a `U.BoundedContext`.
2. **Pick the I/D/S layer.** Speak about the **Intension (I)**, or about its **Description/Spec (D/S)**—but never mix layers. If your sentence also asserts describedEntity or evidence, **name the `ReferencePlane`** (`world|concept|episteme`).
3. **Describe, then test.** Start with **Role/Method/ServiceDescription**. Only when you can **falsify** it with a harness do you call it a **Spec**.
4. **State is attested.** Role **states** are attested by **Evaluations** as *“X ∈ State\@context **in** W”*. Evidence/Requirement **statuses** classify **knowledge**, not roles.
5. **Carriers carry.** PDFs and repos are **Carriers** of the Description/Spec; they aren’t the thing itself.
6. **Bridges are explicit.** Cross‑context sameness is never assumed; you declare a **Bridge** with CL/loss.
   Follow these six lines and SD (*Strict Distinction*) stops being an abstraction—you feel it in every sentence you write.
   

---

## E.11 — Authoring‑Tier Scheme (ATS) \[A]

*Tech token:* `AuthoringTierScheme` (**ATS**).

**Object‑of‑talk.** `AuthoringTierScheme` — an **Episteme (Scheme, kind‑anchored)** that classifies **Authoring Work** into four **AuthoringTier** levels and governs **gate‑crossings**, **evidence lanes**, and **normative separation** between the levels.

**Register & scope.** Kernel pattern in Part E, applicable across FPF and reusable by Part G (architheory authoring) and Part C (discipline patterns), with guards per **E.10 (LEX‑BUNDLE)** and **C.20 §D.DISC**.

### 1) Intent

Provide a **uniform, testable classification Scheme** for acts of authoring in this project, preventing **normative token leakage** between layers of work, and requiring **explicit publication carriers** (`UTS` rows, `BridgeCard`) for any crossing. The scheme aligns with **USM** by treating each tier as a distinct **Work** class and with **E.10** by enforcing head‑anchored naming and I/D/S morphology.

**Wiring.** ATS is explicitly wired to **A.4 (Temporal Duality & Open‑Ended Evolution Principle)** and **B.4 (Observe→Refine→Deploy)**; the cognitive engine for authoring acts is **B.5/B.5.1 (Explore→Shape→Evidence→Operate)**. Keep **Working‑Model first (Tell–Show–Show)** to avoid gratuitous formalism (per **E.8**). **Telemetry/refresh is consumed by G.11 (PathSlice, decay, edition) via H2–H4/H7/H11 hooks.**

### 2) Problem

Without a disciplined tiering of authoring work:

* **Kinds blur** (execution vs design vs architheory vs meta‑authoring).
* **Tokens leak** (a result minted at one tier is used as if normative at another).
* **Evidence lanes** become non‑comparable; **CL (cross‑context loss)** is unmanaged.
* **“Domain” labels** are mistaken for governance, and job‑title language creeps into kernel tokens.

### 3) Forces

* **Separation of concerns.** Translation from applied problems to transdiscipline tasks must be distinct from architheory authoring and from meta‑authoring.
* **Evidence comparability.** Evidence must run in **lanes** with **CL penalties** recorded and routed.
* **Publication accountability.** Cross‑tier reuse must be visible on **UTS** with **Bridge** entries.
* **Lexical hygiene.** Head‑anchoring, I/D/S morphology, and Role/Holder/Carrier separation must hold across all tiers.
* **Discipline vs Domain.** `U.Discipline` governs comparability **via CG‑Spec**, while **Domain** is catalog‑only and stitched to **D.CTX + UTS**.

### 4) Solution — the Scheme

#### 4.1 The four **AuthoringTier** levels (Tech heads; Plain twins in italics)

**AT0 — `AppliedWork`** *(Plain twin: “Applied‑run”)*

* **Work kind.** Execution of applied methods on situated problems, **outside** FPF’s transdiscipline scope.
* **Typical outputs.** `RunObservation` *(run artefact; cf. `Observation`)*, `WorkLogCarrier`, optional `RunbookMethodDescription`.
* **Normative status inside FPF.** **Non‑normative** to higher tiers; may **inform** AT1 through a **`BridgeCard`** with CL notes.

* **Roles.** `ExecutorRole`, `OperatorRole`; **Holders** are concrete holons (teams/systems).
* **Conformance note.** AT0 tokens **MUST NOT** assert norms for AT1–AT3; **`Work` stays execution‑only**, plans/logs/recipes are modeled as `WorkPlan`/Carriers/`MethodDescription`.

**AT1 — `TransdisciplineDesignWork`** *(Plain twin: “Transdiscipline‑design work”)*

* **Work kind.** Translation of applied problems into **Tasks** and **SoTA‑about‑methods**: methods **about** applied methods.
* **Typical outputs.** `TaskPack`, `TranslationMethodDescription`, `DesignRationaleDescription`.
* **Normative status.** Normative **within AT1**; AT1 tokens **MAY** cite AT0 only through **BridgeCard** with CL captured.
* **Roles.** `DesignerRole`, `TranslatorRole`; **Holders** typed to a `U.BoundedContext`.
* **Scope relation to C.20.** When AT1 uses a discipline, name it as `U.Discipline` (Holon) and place comparison rules in its **CG‑Spec**; **no norms on Domain labels** (stitch Domain mentions to **D.CTX + UTS**).

**AT2 — `ArchitheoryAuthoringWork`** *(Plain twin: “Architheory‑authoring”)*

* **Work kind.** Production of the **SoTA Architheory Pack** used in Part G authoring.
* **Typical outputs.** `ArchitheoryPack`, `GaugeSpec`, `InvariantSetDescription`, `BridgeCard` (AT1↔AT2).
* **Normative status.** AT2 defines the **architheory norm set** (CAL/CHR/LOG) that **feeds** F/G reasoning; it **does not mutate Kernel types** and respects **unidirectional meaning** (Kernel → Architheory → Context → Instance).
* **Portfolio‑aware constraint.** AT2 **MUST** treat **“one signature → many specialisations”** as the norm: do **not** embed **global thresholds** or **forced scalarisations** inside architheory text; selection remains **set‑valued** (Pareto/Archive) under **G.5**, with dominance governed by **CAL** policies. Any maturity floors **SHALL** be expressed via **`CAL.AcceptanceClause`** (clause id cited), not inside LOG.
* **Roles.** `AuthorRole`, `AssessorRole` (review within AT2), `StewardRole` (pack upkeep).
* **Cross‑tier references.** Cite AT1 only through a `BridgeCard` with CL captured **and a matching UTS row**.
* **Evidence.** Publishes **UTS rows** for visibility and **BridgeCard** for any cross‑tier references.

**AT3 — `MetaAuthoringWork`** *(Plain twin: “Meta‑authoring”)*

* **Work kind.** Organisation and governance of AT2 work (e.g., editorial coordination).
* **Typical outputs.** `CoordinationFlowDescription`, `AuthoringPolicySpec`, `PublicationPlanDescription`.
* **Normative status.** AT3 **organises** but **does not overrule** AT2 invariants; under **KD‑CAL/B.3**, AT3 **MUST NOT** alter AT2 **F/G invariants** nor introduce cross‑lane mutations; it sets **how** AT2 is executed, not **what** architheory is true.
* **Roles.** `CoordinatorRole`, `EditorRole`, `DisciplineStewardRole` (if a `U.Discipline` is orchestrated).
* **Evidence.** Publishes **UTS rows** for visibility and **BridgeCard** for any cross‑tier references.

> **USM alignment.** Each AT\* is a **Work** class (USM *act*). Tokens produced at a tier are **typed** to that tier’s Work class and **obey E.10** lexical governance.

#### 4.2 Tiering for autonomy budgets & guards
* **AT0/AT1** (application/bridge authors): may **use** existing `AutonomyBudgetDecl` and `Aut-Guard policy-id` and populate UTS fields; **MUST NOT** create new guard policies.
* **AT2** (architheory users): may **author** context‑local `AutonomyBudgetDecl` that instantiates an existing `Aut-Guard` policy and `OverrideProtocolRef`.
* **AT3** (architheory maintainers): may **mint/modify** `Aut-Guard` policies and **register** `OverrideProtocolRef` speech‑act schemas.
**Gate.** Any UTS row referencing a **new** `Aut-Guard policy-id` without AT3 provenance **fails** ATS checks.

### 5) Gate‑crossings & Evidence lanes

#### 5.1 Gate‑crossing requirement

A **GateCrossing** between tiers (e.g., AT0→AT1, AT1→AT2, AT2→AT3) **MUST** be recorded as:

1. a **`BridgeCard`** linking source tokens to target tokens (with **BridgeId** and **CL** loss notes), and
2. a **UTS row** listing: SourceTier, TargetTier, `ContextId` (from **D.CTX**), **BridgeId**, **bridgeChannel ∈ {Scope, Kind}**, **CL** (and **CL^k** if a **KindBridge** is used) with loss notes, **ReferencePlane** (source/target), **CL^plane** (if planes differ), steward Holder, and twin labels.

**ReferencePlane guard.** When a GateCrossing touches differing planes `{world|concept|episteme}`, compute and publish **CL^plane** (policy‑id + loss note) alongside CL.
* **Evidence.** Publishes **UTS rows** for visibility and **BridgeCard** for any cross‑tier references.

#### 5.2 Evidence lanes & CL routing

**Lane taxonomy (normative).**  
  — **F‑lane (Form):** mechanism‑internal laws (units/coherence, law‑set invariants, type/domain/range). Aggregation default: **min**; unaffected by CL penalties.  
  — **G‑lane (Grounding):** scope coverage and applicability to the declared `PublicationScope`. Aggregation: **intersection along a path; SpanUnion across independent lines**.  
  — **R‑lane (Assurance):** residual risk/assurance accounting; receives **Φ(CL)**/**Ψ(`CL^k`)**/**Φ_plane** penalties (all **monotone, bounded, table‑backed**) that **do not** mutate F/G.  
Materialisation: **SCR/RSCR** carry lane‑split; **UTS rows** cite policy‑ids and `CrossingRef`s; **VALATA** tables provide value annotations; carriers stay referenced via SCR/RSCR.

* **Lane separation.** Keep **Form (F)**, **Grounding (G)**, **Assurance (R)** evidence **disentangled** across all tiers (publish lanes explicitly).
* **CL routing.** Under **KD‑CAL**, **CL/CL^k/CL^plane penalties route to R only** and **MUST NOT** mutate F/G invariants. When planes differ, apply **CL^plane** in the assurance penalty; **Φ(CL)**/**Ψ(CL^k)**/**Φ_plane** MUST be **monotone** and **table‑backed**; publish **policy‑ids** in SCR **and cite them on the UTS row**.
* **Lane provenance.** Each evidence item carries: `LaneId`, `SourceTier`, `ContextId`, `BridgeId` (if imported), **ReferencePlane**, and (if applicable) **CL^plane**.

#### 5.3 Telemetry & Refresh hooks (normative)

* **Sentinel registration.** Every GateCrossing **MUST** register the **BridgeId** on a **PathSlice watch‑list**; edits to **CL/CL^k/CL^plane** or relevant **Φ/Ψ policy‑ids** **MUST** trigger **path‑local RSCR** and schedule **PathSlice** refresh (Γ_time × plane), not pack‑wide reruns.
* **Edition awareness.** Where Bridges reference **`U.DescriptorMapRef`**, **`DistanceDefRef`**, or **`InsertionPolicyRef`** (for archives), any **edition change** **MUST** be published to Telemetry and **MUST** trigger the same path‑local refresh.
* **Dominance policy.** **Illumination/QD signals do not alter dominance by default**; `DominanceRegime` **defaults to `ParetoOnly`**. Participation of illumination in dominance **MUST** be authorised by a **CAL policy** and **MUST** be cited by policy‑id in SCR.
* **Open‑Ended (GeneratorFamily) crossings.** Where a GateCrossing imports evidence from **`GeneratorFamily`** flows (POET‑class) — e.g., **`EnvironmentValidityRegion`** or **`TransferRulesRef`** — **register the BridgeId on the PathSlice watch‑list**; any **`…Ref.edition`** change **MUST** be published to Telemetry and **MUST** trigger a **path‑local RSCR/refresh**. Report **`IlluminationSummary`** as a **gauge**; dominance remains unaffected unless a **CAL** policy promotes it (policy‑id cited).

### 6) Interfaces to **C.20 §D.DISC** and **D.CTX / UTS**

* **Discipline usage.** When referencing a field (e.g., “Transdiscipline”), name it as **`U.Discipline` (Holon)**. Put comparability/aggregation in its **CG‑Spec**; do **not** attach norms to a **Domain** label.
* **Domain as catalog mark.** If “Domain” appears, **stitch** it to an **enumerated set of `U.BoundedContext` ids** (per **D.CTX**) and publish **UTS twins**. **Domain carries zero governance.** **Do not attach TaskSignature governance to Domain**; attach comparability/aggregation norms to the **CG‑Spec of U.Discipline**. C.22 **KindSet** supplies describedEntity; **USM** supplies Scope.
* **Traditions vs “Traditions.”** Sub‑disciplinary “Traditions” appear as **`Tradition`** tokens (Tech). Keep “Tradition” only as a **Plain twin** with a twin‑label.

### 7) Roles, Holders, and Carriers (holonic separation)

* **Role tokens.** `DesignerRole`, `TranslatorRole`, `AuthorRole`, `AssessorRole`, `ReviewerRole`, `CoordinatorRole`, `EditorRole`, `DisciplineStewardRole`.
* **Holders.** Use **`Holder#…Role:ContextId`** to type a role assumption, e.g., `Team‑Alpha is Holder#AuthorRole:Architheory‑Lab‑G`.
* **Carriers.** Use **Carrier** for systems that **bear epistemes**: `ArchitheoryPackCarrier`, `UTSRegisterCarrier`, `BridgeRegisterCarrier`.
* **Canonical rewrites.** Legacy `…CarrierRole` → **`Holder#…Role:Context`** (SCR‑LEX).

### 8) I/D/S morphology (applied here)

* **Intension.** `AuthoringTierScheme` (the Scheme itself).
* **Description.** `AuthoringTierSchemeDescription` (this pattern text).
* **Spec (optional, testable).** `AuthoringTierSchemeSpec` — when acceptance criteria and harnesses per **E.10.D2** are published. See §9.

### 9) Conformance (normative)

**C1 — Head‑anchoring.** All tokens minted under this Scheme **MUST** use explicit heads (`Work`, `MethodDescription`, `Pack`, `Spec`, `FlowDescription`, `BridgeCard`, `…Role`, `…Carrier`) and declare **`LEX.TokenClass`**. Figurative heads (e.g., “Ladder”) are **Plain only** with a 1:1 twin to the Tech token.

**C2 — I/D/S.** Use `…Description` for descriptive texts and `…Spec` only when acceptance criteria + harnesses are declared and executable (per **E.10.D2**).

**C3 — Role/Holon separation.** Use `…Role` for playable intentions; **Holders** assume roles via `Holder#…Role:ContextId`. Keep **Carrier** for systems that bear epistemes. Avoid job titles as kernel heads.

**C4 — Tier containment.**

* **C4.1.** Tokens minted at AT0–AT3 are **scoped** to their tier; **normative content MUST NOT leak** to another tier **without** a `BridgeCard` and **UTS row**.
* **C4.2.** AT3 (MetaAuthoring) **MUST NOT** override AT2 invariants; it may only constrain execution/coordination.

**C5 — Evidence lanes.** Publish F/G/R lanes; **route CL→R only**, record **Φ(CL)** and (if applicable) **Φ_plane**; **no F/G mutation**. Provenance includes **ReferencePlane** on crossings.

**C6 — Domain/Discipline governance.**

* **C6.1.** `U.Discipline` is a **Holon**; comparability rules live in **CG‑Spec**.
* **C6.2.** Any **Domain** mention must include the D.CTX projection and **UTS twins**; **no norms on Domain**.

**C7 — Gate‑crossings.** Every cross‑tier reuse **MUST** provide: `BridgeCard` + `UTS` row (with **ReferencePlane**, **bridgeChannel**, **CL**, **CL^k** *if* `bridgeChannel=Kind`, and **CL^plane** where applicable). No implied crossings.

**C8 — Minimal publication set.**

* AT0↔AT1: `BridgeCard`, `TaskPack` (AT1), CL notes, UTS row.
* AT1↔AT2: `BridgeCard`, `ArchitheoryPack` (AT2), lane mapping, UTS row.
* AT2↔AT3: `BridgeCard`, `CoordinationFlowDescription` (AT3), `AuthoringPolicySpec` (if present), UTS row.

**C9 — ATS harness is blocking.** Failures of **AH‑1..AH‑4** *(Classifier, Gate, Lane, Lexical)* **SHALL** block publication under this Scheme; a non‑conformant crossing **MUST NOT** be consumable by **G.4/G.5**. Record the failure as an **SCR** defect with a remediation note.

**Acceptance harness skeleton (for `AuthoringTierSchemeSpec`).**

* **AH‑1 (Classifier).** A deterministic classifier that maps a candidate **Work** record to {AT0|AT1|AT2|AT3} based on its **object‑of‑talk**, outputs, lane types, and declared Roles.
* **AH‑2 (Gate check).** Given a citation across tiers, verifier **MUST** find a `BridgeCard` and matching **UTS row**; **if `bridgeChannel=Kind`, `CL^k` MUST be present** and **Ψ‑policy id** is visible in SCR.
* **AH‑3 (Lane check).** Verifier **MUST** observe **CL/CL^k/CL^plane → R only**, **F/G invariants unchanged**, and — where planes differ — **CL^plane** presence with **Φ_plane** monotone/bounded and table‑backed; SCR shows **R_eff** as a function of Φ/Ψ terms. **When QD/OEE surfaces are present, edition pins MUST be visible**: `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `CharacteristicSpaceRef.edition` *(if present)*, and (for OEE) `TransferRulesRef.edition`.
* **AH‑4 (Lexical check).** Head‑anchoring + I/D/S + Role/Holon separation checks (SCR‑LEX).

### 10) Structure (informative)

### 10.1 Typing table

| Tier    | Work head (Tech)            | Typical outputs (Tech heads)                                                       | Evidence lane policy                        | Crossing rule                               |
| ------- | --------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| **AT0** | `AppliedWork`               | `RunObservation`, `WorkLogCarrier`, `RunbookMethodDescription`                     | Non‑normative to higher tiers               | `BridgeCard` + UTS for import to AT1        |
| **AT1** | `TransdisciplineDesignWork` | `TaskPack`, `TranslationMethodDescription`, `DesignRationaleDescription`           | CL from AT0 import → **R**                  | `BridgeCard` + UTS for import to AT2        |
| **AT2** | `ArchitheoryAuthoringWork`  | `ArchitheoryPack`, `GaugeSpec`, `InvariantSetDescription`                          | CL from AT1 import → **R**                  | `BridgeCard` + UTS for AT3 use              |
| **AT3** | `MetaAuthoringWork`         | `CoordinationFlowDescription`, `AuthoringPolicySpec`, `PublicationPlanDescription` | Publishes lanes; **does not** alter AT2 F/G | Records UTS; cannot change AT2 invariants   |

#### 10.2 Role map (examples)

* `Holder#DesignerRole:Context‑X` (AT1), `Holder#AuthorRole:Architheory‑Lab` (AT2), `Holder#CoordinatorRole:Program‑G` (AT3).
* `Holder` is always typed to a `U.BoundedContext`.
* Avoid **titles** as kernel types; keep them in the **Plain** register with twin labels.

### 11) Examples (cross‑arena, MG·DA compliant)

1. **Software engineering.** AT0: `RunObservation: CI‑Run‑4711`. AT1: `TaskPack: Refactoring‑Targets`. AT2: `ArchitheoryPack: Modularity‑Gauges` + `GaugeSpec: Coupling/Coherence`. AT3: `AuthoringPolicySpec: Pack‑Update‑Cadence`. Crossings logged with `BridgeCard` and UTS; CL from AT1→AT2 routed to **R**.

2. **Clinical operations.** AT0: `RunLogCarrier: MedicationAdministrationWork`. AT1: `TranslationMethodDescription: Dose‑Adjustment‑Design`. AT2: `ArchitheoryPack: Safety‑Invariants`. AT3: `CoordinationFlowDescription: Evidence‑Intake‑Board`. Domain mentions stitched to D.CTX + UTS; discipline governance via **CG‑Spec**.

3. **Operations research.** AT0: `RunResultDescription: Route‑Plan‑Day‑7`. AT1: `TaskPack: Routing‑Abstractions`. AT2: `GaugeSpec: Cost‑Elasticity`. AT3: `AuthoringPolicySpec: Evidence‑Lane‑Publishing`. All imports bridged; CL→R only.

### 12) Anti‑patterns & canonical rewrites

* **“Process ladder”** → Use **Work** heads: `AppliedWork`, `TransdisciplineDesignWork`, etc.
* **“Domain governance”** → Move rules into a **`Discipline CG‑Spec`**; keep Domain as catalog mark with D.CTX + UTS stitching.
* **`Reviewer` (type)** → `ReviewerRole` with `Holder#ReviewerRole:Context`.
* **`…CarrierRole` (legacy)** → `Holder#…Role:Context`.
* **“Tradition”** → `Tradition` (Tech); keep “Tradition” only as Plain twin with twin‑label to the `Tradition`.

### 13) Quality hooks & metrics (informative)

* **Q1. Tier purity.** Share of tokens whose **SourceTier == TargetTier** (no crossing).
* **Q2. Crossing completeness.** % of cross‑tier citations with `BridgeCard` + UTS.
* **Q3. CL hygiene.** % of imported evidence with CL routed to **R** and explicit loss notes.
* **Q4. Lexical conformance.** % tokens passing **SCR‑LEX** (head‑anchoring, I/D/S, Role/Holon separation).
* **Q5. Publication latency.** Median time between citation and UTS row publication.

### 14) Implementation notes

* **Classifier aid.** A simple rule of thumb:

  * Mentions **real‑world outcomes** → candidate `AppliedWork` (AT0).
  * Mentions **methods‑about‑methods** and **Task packs** → AT1.
  * Mints **gauges/invariants/packs** for reuse → AT2.
  * Sets **policies/coordination** for authoring → AT3.
    Always confirm via **object‑of‑talk** and **output heads**.

**Publication discipline.** Keep a **`BridgeRegisterCarrier`** and a **`UTSRegisterCarrier`** controlled by `Holder#StewardRole:Program‑X`.
 Record twin labels on UTS rows.

### 15) Related patterns

* **A.4** — Temporal Duality & Open‑Ended Evolution Principle (time‑split of design/run).
* **B.4** — Canonical Evolution Loop (Observe→Refine→Deploy) governs ATS change/refresh cadence.
* **B.5/B.5.1** — Canonical Reasoning Cycle (Explore→Shape→Evidence→Operate) as cognitive engine for AT‑work.
* **E.10 (LEX‑BUNDLE)** … **F.17** — UTS publication. **C.20 §D.DISC** … **D.CTX** — Context enumeration and stitching.
* **E.10.D2** — I/D/S acceptance harness (for `…Spec`).
* **F.4** — Role Description (RCS/RSG) for `…Role` tokens.
* **F.11** — Method Quartet Harmonisation (algorithm ↔ method description ↔ spec).
* **F.17** — UTS publication.
* **C.20 §D.DISC** — Discipline CAL lexical guard (Holon, CG‑Spec, Domain stitching).
* **D.CTX** — Context enumeration and stitching.

### 16) Glossary (tokens minted or stabilised here)

* `AuthoringTierScheme` · `AuthoringTierSchemeDescription` · `AuthoringTierSchemeSpec`
* `AppliedWork` (AT0) · `TransdisciplineDesignWork` (AT1) · `ArchitheoryAuthoringWork` (AT2) · `MetaAuthoringWork` (AT3)
* `TaskPack` · `ArchitheoryPack` · `GaugeSpec` · `InvariantSetDescription`
* `BridgeCard` · `UTS row` (PublicationCarrier entry) · `BridgeRegisterCarrier` · `UTSRegisterCarrier`
* Roles: `DesignerRole`, `TranslatorRole`, `AuthorRole`, `AssessorRole`, `ReviewerRole`, `CoordinatorRole`, `EditorRole`, `DisciplineStewardRole`
* Lane markers: `F‑lane`, `G‑lane`, `R‑lane` · `CL` (conformance loss) with **CL→R only**

### 17) Lexical/Conformance checklist (quick use)

* **Head‑anchoring:** All heads signal kind (System/Holon/Work/Method/Pack/Spec/Description/Role/Carrier).
* **I/D/S morphology:** `…Description` vs `…Spec` used correctly; acceptance harness only for `…Spec`.
* **Role vs Holder vs Carrier:** `Holder#…Role:ContextId`; Carriers bear epistemes; no `…CarrierRole`.
* **Object‑of‑talk stated** in first line for every new token.
* **Domain = catalog mark only;** stitched to D.CTX + UTS; comparability in **CG‑Spec** of a `U.Discipline`.
* **Gate‑crossings published:** `BridgeCard` + **UTS row** always present.
* **Evidence lanes:** F/G/R separated; **CL→R only**; provenance recorded.
* **Plain twins:** Figurative heads (e.g., “Ladder”, job titles, “Tradition”) also corrected by a twin plane lexical discipline.
* **No minted `U.Type` “Strategy”.** Treat **strategy/policy** as compositions/lenses in **G.5** under **E/E‑LOG**; keep “strategy” in the **Plain** register only.

### 18) Minimal worked “publish set” (ready‑to‑use)

1. **Mint** `AuthoringTierSchemeDescription` (this pattern).
2. **Optionally mint** `AuthoringTierSchemeSpec` with AH‑1…AH‑4 harnesses (per E.10.D2).
3. **Set up carriers:** `BridgeRegisterCarrier`, `UTSRegisterCarrier`.
4. **Start registering crossings:** whenever AT0 informs AT1, AT1 informs AT2, or AT3 organises AT2, publish a **`BridgeCard`** with CL notes and a **UTS row**; register the Bridge on the **PathSlice sentinel watch‑list**.

### **Pattern E.12 — Didactic Primacy & Cognitive Ergonomics \[A] 

**Context**

The FPF is designed as an "Operating System for Thought," a tool intended to augment and clarify human (and artificial) reasoning. This mission places a unique demand on its architecture: the framework's internal elegance and formal power are secondary to its primary function of being understandable and usable. A perfectly consistent but incomprehensible system fails in its didactic purpose. As formal mechanisms like `Assurance Levels` and epistemic scores are introduced, there is a significant risk that the pursuit of these metrics becomes an end in itself, overshadowing the ultimate goal of fostering clearer thought.

**Problem**

If the framework's design prioritizes theoretical purity or formal completeness over cognitive ergonomics, it becomes vulnerable to two critical failure modes:

1.  **Goodhart's Law:** When a measure (like `AssuranceLevel:L2`) becomes the primary target, it ceases to be a good measure of genuine understanding. Teams may start "gaming the metrics," producing artifacts that are formally perfect but conceptually shallow or pragmatically useless.
2.  **Cognitive Overload & Rejection:** The framework becomes so dense, jargon-laden, and procedurally complex that its users—the very agents it is meant to serve—either burn out or abandon it in favor of simpler, albeit less rigorous, methods. The "Operating System for Thought" devolves into a bureaucratic machine for certification.

**Forces**

| Force | Tension |
| :--- | :--- |
| **Formal Rigor vs. Human Usability** | How to build a system that is both formally sound and cognitively accessible, without sacrificing one for the other. |
| **Intrinsic Complexity vs. Incidental Complexity**| How to distinguish the necessary cognitive load inherent in solving a difficult problem from the unnecessary friction imposed by a poorly designed framework. |
| **Means vs. Ends** | How to ensure that the production of high-quality artifacts (the means) always serves the ultimate goal of enhancing an agent's cognitive capabilities (the end). |

**Solution**

FPF elevates **Didactic Primacy (Pillar P-2)** to a normative architectural principle, operationalized through two conceptual mechanisms designed to act as a permanent counterbalance to excessive formalism.

**1. The Principle of Didactic Primacy (Expanded Definition)**

The primary purpose of the FPF is to enhance the cognitive capabilities (`U.Capability`/`Mastery`) of an Agent (`U.Agent`) in service of its Objectives (`U.Objective`). The creation of artifacts with high assurance levels and epistemic scores is a *means to that end, not the end itself*. Any architectural decision that increases formal rigor at the cost of clarity or usability must be explicitly justified by a demonstrable gain in the agent's ability to reason effectively.

**2. Mechanism 1: The Rationale Mandate**

Every key assurance artifact (such as a `U.AssuranceCase` or `Proof`) **MUST** contain a mandatory, human-readable **`rationale`** component.

*   **Nature:** The `rationale` is not a technical description but a narrative explanation.
*   **Content:** It **MUST** answer the question: *"How does achieving this level of formal assurance tangibly help the agent better understand the problem or make a more reliable decision?"*
*   **Purpose:** This mandate forces a moment of reflection, formally linking the act of formalization back to its pragmatic, cognitive purpose. An empty or perfunctory rationale indicates that the assurance work may be an exercise in formalism for its own sake.

> **Didactic Note for Managers: The "So What?" Test**
>
> The Rationale Mandate is FPF's built-in "So What?" test. When your team presents a complex, formally verified artifact (`AssuranceLevel:L2`), the `rationale` is where they answer your fundamental question: "This is impressive, but *so what*? How does this help us ship a better product, make a smarter investment, or avoid a critical risk?" If the answer isn't clear and compelling in the `rationale`, the formal work may have been a waste of resources. It keeps your most brilliant minds focused on creating value, not just elegant proofs.

**3. Mechanism 2: The Human-Factor Loop (HF-Loop)**

To provide a continuous, self-correcting mechanism against cognitive overload, FPF introduces a conceptual feedback loop.

*   **Core Concept:** The HF-Loop is a formal method of inquiry designed to distinguish between the *essential complexity* of the problem being solved and the *incidental complexity* introduced by the FPF itself.
*   **Trigger Concept:** A review is triggered when the **subjective cognitive workload** associated with using the framework exceeds a conceptual threshold. This is not about performance metrics, but about the perceived mental effort required to use FPF's concepts and structures.
*   **Review Concept:** When triggered, a formal review is conducted by individuals in roles that specialize in human-centric perspectives, such as the **`Ethicist`** and **`UX Design Critic`**.
*   **Output Concept:** The review produces a set of proposed **conceptual simplifications** or **didactic improvements** to the framework's patterns or architheories. These are then submitted as formal change proposals (DRRs).

**Conformance Checklist**

*   **CC-E12.1 (Rationale Mandate):** Every `U.AssuranceCase` or `Proof` artifact at `AssuranceLevel:L2` **MUST** contain a non-empty `rationale` component that satisfies the "So What?" test.
*   **CC-E12.2 (HF-Loop Trigger Condition):** Each architheory that defines a significant workflow **SHOULD** specify a conceptual condition for triggering an HF-Loop review, based on the principle of managing cognitive load.
*   **CC-E12.3 (HF-Loop Review Mandate):** If a trigger condition is met, a review involving the designated human-centric roles **MUST** be initiated. Its outcome **MUST** be a documented set of conceptual refinement proposals.
*   **CC-E12.4 (Didactic Primacy in DRRs):** Any DRR proposing a change to a normative pattern **MUST** include a section analyzing its impact on cognitive ergonomics and didactic clarity.

**Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | Manager's View: What It Looks Like | How FPF Prevents It (Conceptually) |
| :--- | :--- | :--- |
| **The "Ivory Tower" Framework** | The FPF specification becomes a beautiful but impenetrable fortress of abstract logic that no practicing engineer can actually use. | The **HF-Loop** provides a formal channel for user feedback to drive conceptual simplification. The roles of `UX Design Critic` and `Ethicist` are constitutionally empowered to challenge complexity that does not serve a clear purpose. |
| **The "Meaningless Rationale"** | The `rationale` field is filled with boilerplate text like "To increase assurance," without any real connection to the problem. | The "So What?" test is part of the review process for L2 artifacts. A perfunctory `rationale` is grounds for rejecting the artifact's promotion to L2, forcing the author to articulate the *real* value of their formal work. |
| **Glorifying Complexity** | A culture emerges where the most complex and difficult-to-understand models are considered the "best," regardless of their utility. | The core principle of **Cognitive Elegance (P-1)** and the mechanisms in this pattern create a constant pressure towards simplicity and clarity. The framework formally values understanding over mere complexity. |

**Consequences**

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Guards FPF's Core Mission:** This pattern acts as an "immune system," protecting the framework from devolving into sterile formalism and ensuring it remains a tool for enhancing thought. | **Introduces "Softer" Concepts:** Cognitive load and rationale quality are less quantifiable than formal proofs. *Mitigation:* FPF operationalizes them through a formal method. The HF-Loop is a structured inquiry, not an informal chat. |
| **Empowers Human-Centric Roles:** It gives the `Ethicist` and `UX Design Critic` roles a concrete, constitutional function in the evolution of the framework. | - |
| **Prevents User Burnout and Rejection:** The HF-Loop is an early warning system that detects when the framework is becoming too cumbersome, allowing for course correction before users become frustrated and abandon it. | - |
| **Creates a Self-Simplifying System:** The pattern creates a formal pressure that forces FPF to evolve towards greater clarity and usability, balancing the drive for formal rigor. | - |

**Rationale**

This pattern operationalizes **Didactic Primacy (P-2)**, transforming it from a philosophical statement into an enforceable architectural Standard. The `Rationale Mandate` ensures that every act of formalization is tied to a clear purpose. The `Human-Factor Loop` ensures that the *cost* of using the framework is measured not just in resources, but in the most critical resource of all: the cognitive capacity of its users.

This pattern does not weaken the formal rigor established by other ADRs; it complements it. It guarantees that the powerful machinery of FPF is always directed towards a meaningful, human-relevant goal. It is the constitutional guarantee that FPF will remain, first and foremost, an "Operating System for Thought."

**Relations**

*   **Implements:** Pillar `P-2 Didactic Primacy`.
*   **Complements:** `E.13 Pragmatic Utility & Value Alignment` (which focuses on the relevance of the *problem*, while this pattern focuses on the usability of the *framework*).
*   **Is constrained by:** The overall governance process (DRRs), which is the vehicle for implementing the conceptual simplifications proposed by the HF-Loop.

### Pattern E.13 — Pragmatic Utility & Value Alignment \[A] 

**Context**

The FPF provides a powerful engine for constructing formally correct and highly reliable holons. This power, however, introduces a subtle but profound risk: a team can create a perfectly verified and validated artifact (`AssuranceLevel:L2`) that solves an irrelevant, misunderstood, or non-existent problem. The framework guarantees that the solution is *correct*, but it does not, by itself, guarantee that the solution is *useful*.

Furthermore, many of the most important system objectives—such as "safety," "usability," or "security"—are not directly measurable. They are assessed via **proxy characteristics** (e.g., "number of reported vulnerabilities" as a proxy for security). This practice is vulnerable to Goodhart's Law: when a proxy becomes the primary target, it often ceases to be a good measure of the original goal, as teams begin to optimize the proxy at the expense of the real objective.

**Problem**

Without a formal mechanism to keep the entire assurance apparatus tethered to real-world value, FPF risks enabling two critical failure modes:

1.  **Formalism for Formality's Sake:** Teams become preoccupied with achieving high epistemic scores, producing elegant but useless artifacts. The framework is used to build beautiful solutions to the wrong problems.
2.  **Proxy-Metric Distortion (Goodhart's Law):** Teams successfully optimize for a chosen proxy characteristic, but in doing so, they diverge from—or even actively undermine—the true, often qualitative, `U.Objective` that the proxy was intended to represent. The system becomes technically successful but pragmatically a failure.

**Forces**

| Force | Tension |
| :--- | :--- |
| **Measurability vs. Meaning** | How to use quantitative, measurable proxies for progress without losing sight of the qualitative, often un-measurable, goals that truly matter. |
| **Abstraction vs. Application** | How to build and reason with abstract models without them becoming disconnected from any concrete, practical application. |
| **Incremental Progress vs. Global Value** | How to ensure that local optimizations and incremental improvements are genuinely contributing to the overall value proposition of the holon. |

**Solution**

FPF elevates **Pragmatic Utility (Pillar P-7)** to a normative architectural principle, operationalized through two mandatory conceptual mechanisms.

**1. The Principle of Pragmatic Utility (Expanded Definition)**

Any artifact created within the FPF is an instrument for achieving a specific, pragmatic `U.Objective`. The value of an artifact is determined solely by its **utility** in achieving that objective, not by its epistemic scores in isolation.

**2. Mechanism 1: The Proxy-Audit Loop**

To formally manage the risk of Goodhart's Law, FPF introduces a conceptual feedback loop to periodically review the alignment between proxy characteristics and their intended goals.

*   **New Normative Relation:** A new relation, `isProxyFor: U.Characteristic → U.Objective`, is introduced. This relation **MUST** be used to explicitly declare when a measurable characteristic is serving as a proxy for a higher-level, often qualitative, goal.
*   **Conceptual Audit Process:** Any characteristic marked with the `isProxyFor` relation is subject to a **periodic conceptual audit**.
*   **Review Roles:** This audit is conceptually performed by the individual(s) in the **`Strategist`** role. They are tasked with answering the question: *"Is optimizing for this proxy still reliably driving progress toward the actual `U.Objective` it represents, or have we observed a divergence?"*
*   **Output Concept:** If a divergence is identified, a high-priority `U.Method` for revising or replacing the proxy **MUST** be proposed.

> **Didactic Note for Managers: Are You Climbing the Right Mountain?**
>
> The Proxy-Audit Loop is your compass. Your team's dashboards might show all green—metrics are improving, targets are being hit. But the audit loop forces a crucial question: "Are these the *right* metrics?"
>
> Imagine you are trying to improve "customer satisfaction" (`U.Objective`). You choose "average call handle time" as a proxy metric. Your team successfully drives this number down. But the Proxy-Audit reveals that customer satisfaction is actually *decreasing* because agents are rushing and providing poor service to meet the time target. The loop forces you to recognize this divergence and find a better proxy (e.g., "first-call resolution rate"). It ensures your team is not just climbing fast, but climbing the right mountain.

**3. Mechanism 2: The Minimally Viable Example (MVE) Mandate**

To enforce a pragmatic, value-first approach from the very beginning of a project, any new `U.System` or major system component **MUST** begin its development cycle with the creation of a **Minimally Viable Example (MVE)**.

*   **Definition:** An MVE is a simple, end-to-end, working instance of the holon that demonstrates the achievement of at least one core, user-facing objective, however trivial. It is the FPF equivalent of a "Hello, World" for a complex system.
*   **Assurance Requirement:** The MVE **MUST** achieve a minimum of **`AssuranceLevel:L1 (Substantiated)`**. This means the MVE cannot be a mere mock-up or a purely conceptual sketch; it must be supported by at least one piece of tangible evidence (e.g., a passing test case, a formal assertion), as defined in Pattern B.3.3.
*   **Stege transition Precedence:** The development of the full-scale holon cannot proceed to `AssuranceLevel:L2` until the MVE has been created and has met its L1 requirement.

**Conformance Checklist**

*   **CC-E13.1 (Proxy Declaration Mandate):** Any `U.Characteristic` used as a primary driver for an objective **MUST** be explicitly linked to that `U.Objective` via the `isProxyFor` relation.
*   **CC-E13.2 (Proxy-Audit Mandate):** A formal Proxy-Audit review **MUST** be conducted at regular conceptual intervals (e.g., before each major release). The outcome of this review **MUST** be a documented episteme.
*   **CC-E13.3 (MVE Mandate):** The development of any new `U.System` **MUST** be preceded by the creation of an MVE that satisfies the `AssuranceLevel:L1` requirement.
*   **CC-E13.4 (MVE Traceability):** The full-scale `U.System` **MUST** maintain a formal traceability link (`isEvolutionOf`) to its originating MVE.

**Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | Manager's View: What It Looks Like | How FPF Prevents It (Conceptually) |
| :--- | :--- | :--- |
| **The "Perfectly Engineered Irrelevance"** | The team delivers a technically brilliant system that is formally verified and validated, but no one wants to use it because it doesn't solve a real problem. | **CC-E13.3** forces the team to build a working, end-to-end slice of value (the MVE) *first*. This grounds the entire project in a demonstrated solution to a real user need from day one. |
| **The "Metric Myopia"** | The team becomes obsessed with improving a specific KPI, ignoring clear signs that this is not improving—and may even be harming—the overall user experience or business goal. | **CC-E13.2** mandates the Proxy-Audit Loop. This forces a periodic, strategic step-back, where the `Strategist` role is constitutionally required to ask, "Are we still measuring what matters?" |
| **The "Big Design Up Front" Trap** | The team spends months creating a vast, abstract, and highly detailed model of a system before ever building a single working component. | The **MVE Mandate** prevents this. It forces an iterative, pragmatic "build-to-learn" approach, ensuring that models are always grounded in a working reality. |

**Consequences**

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Defense Against Goodhart's Law:** The Proxy-Audit Loop is a concrete, operational defense against the common failure mode of optimizing for the wrong thing. It forces regular, strategic reflection on the meaning of metrics. | **Introduces Strategic Overhead:** The Proxy-Audit Loop and the creation of an MVE require dedicated time for strategic thinking and early implementation. *Mitigation:* This is not an expense but a strategic investment. This upfront effort is designed to prevent the far greater cost of developing the wrong system over months or years. |
| **Ensures Value-Driven Development:** The MVE Mandate guarantees that all major development efforts are grounded in a demonstrated, working solution to a real problem, however small. This prevents teams from investing significant resources in abstract models that have no proven path to practical application. | - |
| **Prevents "Analysis Paralysis":** By requiring an early, working example, this principle encourages an iterative, pragmatic development style. It forces teams to build and learn, rather than over-specifying in a vacuum. | - |
| **Positions FPF as an Engineering Discipline:** This pattern firmly anchors FPF as a tool for practical engineering, not just theoretical modeling. | - |

**Rationale**

This pattern operationalizes **Pragmatic Utility (P-7)**. While Pattern E.12 protects the *agent* from the cognitive overload of the framework, this pattern protects the *problem* from being lost in a sea of formal abstraction. It provides the necessary constitutional guardrails to keep the powerful formal methods of FPF focused on delivering tangible, real-world value.

The **MVE Mandate** ensures that every journey starts with a destination in sight. The **Proxy-Audit Loop** ensures that the compass used on that journey remains pointed in the right direction. Together, these mechanisms guarantee that knowledge generated within FPF is not only formally correct and epistemically reliable, but also meaningful, useful, and aligned with its intended purpose.

**Relations**

*   **Implements:** Pillar `P-7 Pragmatic Utility`.
*   **Complements:** `E.12 Didactic Primacy & Cognitive Ergonomics`.
*   **Provides context for:** The definition of `U.Objective` and `U.Characteristic` by establishing a formal link between them.


---

# E.15 — Lexical Authoring & Evolution Protocol  (LEX‑AUTH) \[A]

> *Author patterns as evidence‑bearing epistemes, evolve them via governed open‑ended search, and publish an auditable trace that improves quality—not just compliance.*


---

## 4) Solution — A *governed evolutionary* authoring method with a publishable **LEX‑AUTH Trace (LAT)**

LEX‑AUTH defines **how** a pattern is **proposed, varied, selected, validated, and merged**, with artifacts and evidence fit to the FPF kernel.

### 4.1 Method (design‑time choreography)

**Stage A — Frame & Scope (Context, Objectives, Invariants)**

1. **Anchor** the work in a **`U.BoundedContext`** for the spec (e.g., `FPF/Core`), cite governing guard‑rails (**E.5.\***), and state **objectives** for the change (e.g., clarity ↑, universality ↑, assurance cost ↓).
2. **Declare the Delta‑Class** (see §4.3) and **impact radius** (dependent patterns, bridges, tests).
3. **Fix acceptance targets** (see §4.4 Quality & SoTA metrics).

**Stage B — Generate candidates (SoTA + NQD)**
4. **Harvest SoTA** inputs (standards, rival patterns, lived domain idioms) and **bind** them as *evidence* via `U.EvidenceRole` with **claim/claim‑scope/timespan** (empirical vs deductive lines).
5. **Generate candidate variants** using **NQD‑CAL** engines (Novelty/Quality/Diversity) with an **E/E policy** (explore↔exploit governor) to populate a **Pareto front** of pattern phrasings/structures. *(No single shot; multiple candidate clauses compete.)*

**Stage C — Shape & Align (Structure, Bridges, USM)**
6. **Shape** top candidates into the standard **\[A] template** (Context → Problem → Forces → Solution → CC → Consequences → Rationale), obeying **LEX‑BUNDLE** (no tooling jargon; twin registers allowed).
7. **Bridge across Contexts** explicitly (F.9): any imported definitions/claims declare **CL** and *loss notes*; propose scoped **narrowing** where needed.
8. **Type scopes** with **USM (A.2.6)**: keep **ClaimScope (G)** distinct from **WorkScope**; no “applicability/envelope” smuggling.

**Stage D — Validate & Decide (Assurance, Tests, DRR)**
9. **Run the harness**: update **SCR/RSCR** (F.15), lint lexical rules (E.10), run **Γ‑consistency** and **RSG/SoD** checks where relevant.
10. **Score** candidates on **Quality & SoTA metrics** (§4.4) and **assurance deltas** (Δ⟨F,G,R⟩).
11. Record a **DRR** (E.9) with *options considered*, *trade‑offs*, chosen candidate, *blast‑radius*.
12. **Merge** the winner; version pattern **SemVer** by Delta‑Class.

**Stage E — Publish & Monitor**
13. Publish the **LEX‑AUTH Trace (LAT)** (§4.2) with the pattern.
14. Schedule **evidence refresh** windows and an **evolution watchpoint** (B.4 loop): when metrics or SoTA inputs decay, reopen Stage B.

### 4.2 The **LEX‑AUTH Trace (LAT)** — what it is and why it matters

A LAT is **not** “we ran a script.” It is a **structured episteme** that lets others **reproduce quality gains** and **re‑run** the search when SoTA shifts.

**LAT minimal contents (publish with the pattern):**

1. **Context & version** (pattern id, context, SemVer, Delta‑Class).
2. **Objective vector** (what we tried to improve: clarity, universality, assurance cost, etc.).
3. **SoTA pack** (sources bound as `U.EvidenceRole` with claim/scope/time and polarity).
4. **NQD settings** (emitters/lenses, diversity characteristics) + **E/E policy** used.
5. **Candidate set** (top K variants with NQD scores + short deltas from baseline).
6. **Bridge ledger** (all cross‑context imports with **CL** and loss notes).
7. **Assurance delta** (Δ⟨F,G,R⟩ from baseline; penalties from CL applied).
8. **Harness results** (checks passed/failed, test diffs).
9. **DRR link** (decision rationale id).
10. **Refresh policy** (evidence decay windows and triggers).

**Uses of the LAT:**
*Reproducibility* (re‑run B‑stages as SoTA changes), *assurance* (explicit impact on F/G/R), *portfolio health* (diversity/coverage), *teaching* (didactic before/after), and *cross‑context safety* (no silent imports).
Publish the pattern with a DRR that carries a LAT pointer (id/URI). The LAT itself is a U.Work evidence pack (non‑normative), archived with edition and Γ_time.

**Example of a LAT‑stub**
```
LAT:
  context: FPF/Core, pattern: F.15, semver: x.y+1, delta-class: Δ‑2
  objectives: {clarity↑, universality↑, assurance-cost↓}
  SoTA-pack: {OpenAlex 2025‑Q3, SPECTER2‑23, DPP‑2019, MAP‑Elites‑2015+}
  NQD-settings: {CharacteristicSpace: domain‑family × …, grid: CVT@k=16}
  candidates: K=4 (wording of RSCR‑F04 & gates)
  bridge-ledger: none (intra‑canon refs only)
  assurance‑delta: ΔF=+, ΔG=+, ΔR=+ (after CL‑penalties=0)
  harness: LEX‑BUNDLE lint pass; F‑suite pass; Γ‑consistency ok
  DRR-id: DRR‑2025‑09‑DFCM‑roll‑in
  refresh: F1‑Card edition refresh window = 6 mo
```

### 4.3 What counts as “changed the pattern as a whole” — **Delta‑Classes & versioning**

Classify the intended change **before** work starts (declared in DRR & LAT):

* **Δ‑0 Lexical polish** — wording/ordering only; **no** change to CC or semantics. → *Patch* (x.y.**z**+1).
* **Δ‑1 Didactic restructure** — narrative/layout; **unchanged** Conformance Checklist (CC). → *Minor* (**x.y**+1.0).
* **Δ‑2 Normative refinement** — CC tightened/clarified; *semantics preserved* by test equivalence. → *Minor* (**x.y**+1.0) + **RSCR** required.
* **Δ‑3 Semantic change** — CC **adds/removes** requirements; downstream contracts shift. → *Major* (**x**+1.0.0) + **impact review** + **bridges refresh**.

> **Definition of “pattern changed as a whole”:** any **Δ‑2/Δ‑3** change (i.e., the **normative surface** or **semantics** changed) counts as a pattern change in the canonical corpus and triggers harness & bridge reviews.

### 4.4 Quality & SoTA metrics (selection lenses)

**Mandatory lenses** (declare in LAT; higher is better unless noted):

* **Clarity** (readability; plain‑register score from didactic rubric).
* **Universality** (C‑1): *≥3 heterogeneous domains* anchored in the Archetypal section.
* **Lexical discipline** (E.10): 0 violations (DevOps lexicon, process/function conflations).
* **Assurance delta**: ΔF (formality), ΔG (scope clarity), ΔR (reliability after CL penalties).
* **Bridge integrity**:  Bridge integrity (policy lens): declare minimum CL thresholds per Context policy; penalties route to R only (B.3/F.9); record policy‑id in LAT.
* **Test conformance**: F‑suite pass; RSCR clean.
* **Exploration health** (NQD): diversity coverage > threshold; no premature convergence.
* **Didactic economy**: length vs density ratio within band; “Tell‑Show‑Show” present.

**Optional lenses** (context‑specific): *Ethical/SoD guard strength; cross‑scale roll‑up integrity; aggregation proofs present;* etc.