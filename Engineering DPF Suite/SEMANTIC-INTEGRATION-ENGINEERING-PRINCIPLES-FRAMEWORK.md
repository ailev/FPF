# Semantic Integration Engineering Principles Framework

> A domain pattern language for making separately governed meanings and representations usable together for a named receiving use.

- **Author:** Anatoly Levenchuk, with AI-assisted development and review
- **Version:** 8 September 2026
- **Status:** Eternal alpha: the complete twelve-pattern first edition, open to correction as methods, sources, and applications change. The Methods support use-qualified model reuse or construction, semantic interfaces, affected-use revalidation, and modular semantic commons.
- **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) for original framework content; third-party material retains its own terms.
- **Publication:** [FPF repository](https://github.com/ailev/FPF)

Use the Readme to enter from a working difficulty, or the Table of Contents to open one available pattern. The Preface explains how the contributions work together and the scope of their use. For references to this version, use the [Citation](#citation).

# Table of Contents

Use the Readme when you recognize a difficulty but do not yet know the PatternID. Use this Table of Contents when you know the result you need. The 12 included bodies are the authoritative Methods for this first edition.

`SIE.*` is the PatternID namespace. Numbers are stable addresses, not a Work sequence.

## Public units

| Unit | Reader use |
| :--- | :--- |
| [Semantic Integration Engineering Principles Framework Readme](#semantic-integration-engineering-principles-framework-readme) | Start from a receiving-use, source, model, correspondence, identity, claim, mapping, realization, interface, validation, change, or commons difficulty. |
| [Citation](#citation) | Cite this first edition or one pattern with its PatternID and date. |
| [Preface](#preface) | Understand how the contributions connect, why their boundaries matter, and which combined results the repertoire can support. |
| [Authoritative Pattern Bodies](#sie1---bound-the-receiving-use-and-semantic-contract) | Use the twelve SIE bodies under their own entry conditions; PatternID order is not a lifecycle. |
| [Cross-Pattern Application](#cross-pattern-application) | Inspect AP242/QIF, semiconductor identity, quality/provenance, high-change-provider, and semantic-commons cases. |
| [Framework Boundary and Refresh](#framework-boundary-and-refresh) | Check package anatomy, availability, sources, neighboring modeling work, owners, and edition limits. |

## Part I - Semantic Integration Engineering Methods

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [SIE.1 - Bound the Receiving Use and Semantic Contract](#sie1---bound-the-receiving-use-and-semantic-contract) | Eternal alpha | What exact receiving use, semantic loss boundary, authority, and validation obligation govern this integration? | FPF C.37; ME.3; direct receiver and source-owner results |
| 2 | [SIE.2 - Recover and Qualify Source Semantics and Authority](#sie2---recover-and-qualify-source-semantics-and-authority) | Eternal alpha | What does each load-bearing source mean, under which edition, effectivity, authority, and access conditions? | SIE.1 or equivalent contract; FPF F.0.1, F.0.2; direct source owners |
| 3 | [SIE.3 - Construct or Reuse a Semantic Model for a Named Use](#sie3---construct-or-reuse-a-semantic-model-for-a-named-use) | Eternal alpha | Does an available model answer the receiving questions, or what semantic extension is needed? | SIE.1 or equivalent use; relevant SIE.2 source meanings; domain participants |
| 4 | [SIE.4 - Establish Use-Qualified Cross-Source Correspondences](#sie4---establish-use-qualified-cross-source-correspondences) | Eternal alpha | Which exact endpoint relation, difference, or incompatibility is warranted and usable here? | SIE.2; supplied SIE.3 result when required; FPF F.9 |
| 5 | [SIE.5 - Resolve Cross-Source Identity without Erasing Identifier Authority](#sie5---resolve-cross-source-identity-without-erasing-identifier-authority) | Eternal alpha | Do these source endpoints concern the same entity at the required grain and interval, or another relation? | SIE.2; conditional SIE.4; direct MDM/domain authority inputs |
| 6 | [SIE.6 - Fuse Source-Qualified Claims without Erasing Conflict](#sie6---fuse-source-qualified-claims-without-erasing-conflict) | Eternal alpha | How can source claims be composed while preserving scope, authority, uncertainty, conflict, and non-comparability? | SIE.2, SIE.4; SIE.5 when identity is load-bearing; FPF C.2.1, A.10 |
| 7 | [SIE.7 - Specify Semantic Extraction and Transformation Mappings](#sie7---specify-semantic-extraction-and-transformation-mappings) | Eternal alpha | Which executable rules preserve the accepted correspondences, identities, claim branches, and losses? | SIE.2, SIE.4; conditional SIE.5 and SIE.6; FPF A.6.3.RT |
| 8 | [SIE.8 - Choose Virtual, Materialized, or Hybrid Semantic Realization](#sie8---choose-virtual-materialized-or-hybrid-semantic-realization) | Eternal alpha | Which available realization can meet the semantic, freshness, access, provenance, recovery, and combined resource conditions? | SIE.1, SIE.7; direct Data Engineering, platform, provider, and protection results |
| 9 | [SIE.9 - Connect a Receiving Use through a Semantic Interface](#sie9---connect-a-receiving-use-through-a-semantic-interface) | Eternal alpha | What smallest interface carries the required meanings, branches, provenance, and return paths into receiving Work? | SIE.1, SIE.7, SIE.8; conditional SIE.4-SIE.6 results |
| 10 | [SIE.10 - Validate a Semantic Integration Result for Its Receiving Use](#sie10---validate-a-semantic-integration-result-for-its-receiving-use) | Eternal alpha | What does the evidence settle about the named receiving use, and which claimed premises still need validation? | SIE.1 or equivalent use; relevant SIE.2-SIE.9 results; direct domain and receiver acceptance criteria |
| 11 | [SIE.11 - Trace Semantic Change and Revalidate Affected Uses](#sie11---trace-semantic-change-and-revalidate-affected-uses) | Eternal alpha | Which receiving results depend on the changed semantic premise, and what can now continue? | Changed relied-on premise; relevant SIE.2-SIE.10 results; FPF A.10.1 when discovery is needed |
| 12 | [SIE.12 - Govern Modular Semantic Commons without Universal Authority](#sie12---govern-modular-semantic-commons-without-universal-authority) | Eternal alpha | How can actual users maintain and rely on shared semantic modules and their changes? | Actual shared-module uses; SIE.3, SIE.4, and SIE.11 when their results are needed |

# Semantic Integration Engineering Principles Framework Readme

## Practical entries

Use Semantic Integration Engineering when separately governed meanings, models, schemas, identifiers, claims, data, or representations must become usable together for one named query, decision, operation, or engineering workflow. Start with the difficulty that can change the receiving use. Do not begin from a preferred ontology language, graph database, integration platform, or universal vocabulary.

The repertoire contains the twelve bodies `SIE.1`–`SIE.12`. A practitioner can obtain a model, qualify and connect separately governed meanings, validate a receiving result, revisit changed reliance, or maintain shared semantic modules under the relevant entry conditions. Pattern numbers are stable addresses; the needed results determine their use.

The entries help recognize a first useful move; they do not require a complete integration package for every question. Read the [Preface](#preface) when several contributions must work together, and its [Architectural Rationale](#siepreface7---architectural-rationale) when you need to compare arrangements or understand the boundaries. A direct pattern remains usable without reading that whole account first.

These entries illustrate common situations. For a question they do not cover, name the receiving use and first missing result, consult [Pattern selection and first returned result](#pattern-selection-and-first-returned-result), and check the selected body's use conditions. If the question belongs to another practice, follow the [owner boundaries](#fpf-neighboring-practice-and-authority-boundaries) to its result; keep any unsupplied result explicit.

### SIE-CONTRACT - Bound the receiving use before integrating sources

- **Situation:** A team has been asked to “integrate the data” or “build the knowledge graph”, but the receiver, question, acceptable loss, currentness, authority, and pass condition are unstated.
- **Question:** What exact use must the semantic arrangement serve, and what would make its answer usable or unsafe?
- **First useful result or honest blocker:** A `SemanticIntegrationUseContract@Use`, or a blocker naming the missing receiver, authority, source permission, acceptance rule, or representative test.
- **Start with:** `SIE.1`.
- **Stop or return:** Stop before model or technology selection when the contract cannot distinguish a useful answer from a misleading one.

### SIE-SOURCES - Recover what each source actually means and may establish

- **Situation:** Familiar labels, columns, classes, codes, API fields, and identifiers appear comparable, but their source schemes, editions, meanings, owners, or effectivity differ.
- **Question:** Which source-local meanings and authority claims are load-bearing for this use?
- **First useful result or honest blocker:** A `SourceSemanticInventory@Use` with exact gaps and source returns.
- **Start with:** `SIE.2`.
- **Stop or return:** Return a missing domain meaning, identifier-owner rule, access permission, or authoritative value to its direct owner. Return unsettled model adequacy to SIE.3; SIE.4 and SIE.5 supply correspondence and identity results when needed.

### SIE-MODEL - Construct or reuse a semantic model for the named use

- **Situation:** An integration needs particular meaning distinctions and the adequacy of its available models is unsettled.
- **Question:** Does a current model answer the receiving questions, or what extension or construction is needed?
- **First useful result or honest blocker:** A `UseFitSemanticModel@Use`, which can be a qualified existing model, or the precise unresolved model question.
- **Start with:** `SIE.3`, the receiving questions, and the relevant source meanings.
- **Stop or return:** Finish sufficient reuse. Develop content only for a demonstrated gap; an unresolved definition limits the dependent correspondence, mapping, or use.

### SIE-CORRESPOND - Establish or reject cross-source correspondences

- **Situation:** Two endpoints look similar, share a label, or were matched automatically, but the intended relation and permitted loss remain unproved.
- **Question:** Which exact relation, difference, or incompatibility obtains for this use?
- **First useful result or honest blocker:** A `QualifiedCorrespondenceSet@Use` containing accepted, rejected, unresolved, and incompatible rows.
- **Start with:** `SIE.4` after source-local endpoint meanings are available.
- **Stop or return:** Stop at unresolved endpoint senses, unsupported relation truth, or loss outside the use contract.

### SIE-IDENTITY - Decide cross-source identity at the required grain

- **Situation:** Several identifiers may denote the same thing, a part, a version, a variant, a family, or unrelated things, and a shared ID would erase issuer authority.
- **Question:** What identity disposition is warranted for each load-bearing endpoint, interval, and grain?
- **First useful result or honest blocker:** A `CrossSourceIdentityDisposition@Use` that preserves every scheme, issuer, evidence item, and unresolved case.
- **Start with:** `SIE.5`.
- **Stop or return:** Return master identity and authoritative-value decisions to MDM or the domain authority. Do not manufacture equivalence to complete a join.

### SIE-CLAIMS - Compose source-qualified claims without flattening conflict

- **Situation:** A receiving answer combines claims from different sources whose scope, time, authority, uncertainty, or conclusions differ.
- **Question:** Which claims are comparable, contradictory, non-comparable, or unresolved, and what qualified view can the receiver use?
- **First useful result or honest blocker:** A `SourceQualifiedClaimFusion@Use` or an explicit conflict/non-comparability return.
- **Start with:** `SIE.6`.
- **Stop or return:** Stop when composition would hide source scope, identity premises, conflict, or the authority that owns truth or action.

### SIE-MAPPING - Specify executable extraction and transformation semantics

- **Situation:** Correspondences have been discussed, but implementation still depends on undocumented joins, defaults, code conversions, unit changes, or error handling.
- **Question:** Which executable rules preserve the accepted meanings and expose their losses and failures?
- **First useful result or honest blocker:** An `ExecutableSemanticMappingSpecification@Use` with examples and traceable tests.
- **Start with:** `SIE.7`.
- **Stop or return:** Return physical pipeline construction and operation to Data Engineering; stop if a required correspondence, identity disposition, or composition premise is missing.

### SIE-REALIZE - Choose virtual, materialized, or hybrid realization

- **Situation:** A graph store, warehouse, federation, API composition, or cache has been proposed before freshness, access, provenance, recovery, and source authority were compared.
- **Question:** Which realization can meet this contract without hiding source change or unacceptable operating burden?
- **First useful result or honest blocker:** A `SemanticRealizationDecision@Use`: a supported choice, sufficient exclusion or rejection, worthwhile probe, or missing-input return; identify the implementation or provider results the selected choice still needs.
- **Start with:** `SIE.8`.
- **Stop or return:** Finish a decisive exclusion with sufficient grounds. Compare serious remaining alternatives as complete arrangements; obtain further evidence only when its possible decision contribution justifies its full burden and displaced work.

### SIE-INTERFACE - Connect the receiver to the bounded meanings

- **Situation:** Mappings or an integrated store exist, yet the receiving query or workflow cannot discover provenance, interpretation, currentness, unresolved branches, or source-return paths.
- **Question:** What smallest interface carries the required semantic result into the receiving Work?
- **First useful result or honest blocker:** A `ReceivingSemanticInterface@Use`.
- **Start with:** `SIE.9`.
- **Stop or return:** The application still owns authorization, risk acceptance, and outcome. A reachable endpoint is not a validated semantic interface.

### SIE-VALIDATE - Validate an integration result for its receiving use

- **Situation:** A schema, shape, pipeline, or sample query passes, but identity, authority, provenance, quality, conflict, or a representative receiving workflow remains untested.
- **Question:** Which validation layers pass, narrow the usable result, remain unresolved, or require a stop?
- **First useful result or honest blocker:** A `SemanticIntegrationValidationAccount@Use` supporting a sufficient bounded failure or scoped gap, or a positive result with full coverage of its load-bearing premises.
- **Start with:** `SIE.10`.
- **Stop or return:** A known decisive failure can finish with its supporting evidence. Distinguish unexamined premises from passes. Positive validation covers all load-bearing conditions of the named whole use or permitted subset, including receiving interpretation.

### SIE-CHANGE - Trace semantic change to affected uses

- **Situation:** A relied-on source, model, identifier rule, mapping, or interface meaning changes and continued use needs a decision.
- **Question:** Can a compatible repair finish, or which receiving results depend on a material change?
- **First useful result or honest blocker:** A qualified direct repair or affected-use result; an `AffectedSemanticUseRevalidationAccount@Change` only when a receiver needs a common account.
- **Start with:** `SIE.11` and the earlier and later relied-on meanings.
- **Stop or return:** Complete supported branches at their scope. A wider no-impact claim needs matching coverage; inaccessible or unexamined reliance remains unresolved.

### SIE-COMMONS - Govern shared semantic modules

- **Situation:** Independently governed users rely on shared semantic modules and need to maintain their meanings and changes.
- **Question:** What module boundaries, dependencies, decision rights, and release arrangements serve those uses?
- **First useful result or honest blocker:** A `ModularSemanticCommonsAccount@Community` that makes a concrete module change and its use workable, or the unresolved right or dependency that prevents it.
- **Start with:** `SIE.12` and the actual shared-module users.
- **Stop or return:** A model and interface agreement can finish one local interface. In a commons, qualify the arrangement to the rights and reliance actually established.

## Citation

If you use this edition, cite:

```text
Anatoly Levenchuk, with AI-assisted development and review.
Semantic Integration Engineering Principles Framework.
8 September 2026. First edition.
GitHub repository: https://github.com/ailev/FPF
```

For a particular pattern, add its PatternID and title. Retain the edition designation and date, and include a permanent link or stored copy when exact wording matters.

# Preface

Semantic integration is professional Work that makes separately governed meanings and representations usable together for a particular receiver. Its governed object is the maintained semantic-integration arrangement: the use contract, qualified sources and needed model content, correspondences, identity and claim dispositions, executable mappings, realization, interface, validation, and their dependencies and maintenance. An ontology file, mapping table, graph database, registry, API, or pipeline can contribute to that arrangement; none is the whole by itself.

Begin from one receiver and one query, decision, operation, or engineering workflow. Work backward to the answer claims, distinctions, sources, authorities, losses, currentness, and tests that the use needs. Preserve explicit incompatibility when it is more truthful than a common value.

An integration practitioner works with source experts and the receiving engineer, analyst, application team, or other owner of the use. A successful join may still answer the wrong question: the same code can name a product family in one source and a particular item in another, or two availability fields can carry different commitments. At the other extreme, requiring a common ontology or store for every source can delay a small useful answer and suppress a difference the receiver needs. The working problem is to connect the required meanings while keeping their authority, limits, and consequences recoverable.

The main trade-offs follow from that problem. A narrower source cut costs less but may omit a claim that changes the answer. Preserving more distinctions and provenance improves what can be inspected but increases source work, interface detail, and tests. Live access can preserve a source's control while making availability and repeatability harder to obtain; copying can support repeatable queries while adding permission, refresh, correction, and custody obligations. The contract makes these choices answerable to the actual use.

## SIE.Preface:1 - Meanings, identifiers, claims, carriers, and world-side referents remain distinct

| Working object | Question it answers | What it does not establish by itself |
| --- | --- | --- |
| term or designation | Which sign is used in one source? | one shared concept or referent |
| concept, type, or relation | Which meaning or classification does the source express? | that another source uses the same meaning |
| schema or semantic model | Which structures and constraints can be represented? | truth of the represented claims or fitness for this receiver |
| identifier | Which scheme-specific sign identifies under one issuer's rules? | cross-source identity, master identity, or authoritative value |
| claim | What is asserted with which scope, interval, source, and uncertainty? | agreement, preference, authorization, or action |
| data item or carrier | Where is a representation recorded or transported? | preservation of meaning through extraction or transformation |
| world-side referent | Which entity or occurrence the claim is about | that two descriptions identify it at the same grain and interval |

## SIE.Preface:2 - Source authority and receiving authority remain separate

A source owner can define a scheme or publish a value without authorizing the receiver's decision. A master-data steward can decide an enterprise identity without deciding product release or recall. Systems Engineering can decide configuration and effectivity without owning a cross-source mapping. Data Engineering can operate a pipeline without deciding semantic equivalence. The receiving application or professional practice owns its operational or decision outcome.

SIE makes the semantic premises and losses inspectable, tests them for the named use, and returns unresolved decisions to their direct owners. It does not borrow their authority.

## SIE.Preface:3 - Pattern relations do not prescribe a lifecycle

The patterns have information dependencies, not one mandatory calendar sequence. `SIE.1` and `SIE.2` often expose the first stop. A practitioner may enter `SIE.5` when the use and source inventory already exist, `SIE.8` when a realization choice is current, or `SIE.10` when an existing interface needs validation. Discovery, alignment, mapping, implementation, and testing can iterate.

`SIE.3` supplies a qualified reused or developed model when adequacy is unsettled. `SIE.11` follows a changed semantic premise to the results that actually relied on it; a compatible reference repair can finish directly. `SIE.12` supplies the arrangements needed by actual shared-module users. A known adequate model, an unchanged use, or one local interface can continue without performing those further Methods.

## SIE.Preface:4 - The first whole result

The first useful whole is `SemanticIntegrationPackage@Use`. It is a connected, inspectable set of eight results, not necessarily one file and not necessarily RDF or a graph:

1. use contract;
2. source manifest;
3. correspondence set;
4. cross-source identity disposition when it is load-bearing;
5. source-qualified claim composition;
6. mapping specification;
7. realization and interface;
8. validation account.

The package references any SIE.3 model qualification on which it relies. Preserve identity premises where the answer depends on them; explain their non-use only when it affects interpretation or later reliance. A package may return explicit conflict or non-comparability. Positive validation requires matching evidence for every load-bearing premise of the claimed whole use or contract-permitted subset.

## SIE.Preface:5 - Use the repertoire at the scale of the missing result

The [package anatomy](#package-anatomy-and-direct-result-relations) states what must be inspectable when the promised result is a whole semantic interface package. Use the Methods whose results are missing or whose qualifications need reopening. With a supplied use contract and qualified source meanings, [SIE.4](#sie4---establish-use-qualified-cross-source-correspondences) can return one warranted correspondence or an incompatibility and stop. With an existing interface and its premises, [SIE.10](#sie10---validate-a-semantic-integration-result-for-its-receiving-use) can identify a failed receiving-use obligation without rebuilding that interface. Reuse an available result when its subject, source editions, use, and conditions still match; reopen the contribution whose premise changed.

Some relations need separate answers even when one practitioner handles them. A correspondence supplies a relation between meanings; [SIE.5](#sie5---resolve-cross-source-identity-without-erasing-identifier-authority) supplies a cross-source identity disposition when the answer depends on the same entity at a particular grain and interval. [SIE.6](#sie6---fuse-source-qualified-claims-without-erasing-conflict) then qualifies the composition of source claims. Identity can hold while claims conflict, and claims can be compared without merging their subjects. [SIE.7](#sie7---specify-semantic-extraction-and-transformation-mappings) specifies executable behavior from those premises; [SIE.8](#sie8---choose-virtual-materialized-or-hybrid-semantic-realization) compares ways of supplying it; [SIE.9](#sie9---connect-a-receiving-use-through-a-semantic-interface) carries the qualified result into the receiver's work. Their results constrain one another, while a defect can return to any supplying pattern.

A bounded interface package needs adequate models, its other load-bearing premises, and the required implementation and validation evidence. The five [applications](#cross-pattern-application) demonstrate interface and shared-module uses. Their differences change the work: AP242/QIF needs configuration and effectivity premises; semiconductor traceability makes identity grain and issuer rules central; an analytic can fail on a unit conversion or hidden default; live provider comparison may need qualified difference and non-comparability instead of a shared value. The shared-equipment commons adds module decisions, dependencies, and semantic change. Each application uses the same repertoire at the scope of its receiving question.

If a required distinction cannot be expressed, SIE.3 reuses, extends, or constructs the needed semantic content. An unresolved source definition still limits the dependent mapping or interface claim. SIE.11 compares changed reliance and obtains the affected domain results; its wider account is conditional on a receiving need. SIE.12 supplies shared-module maintenance and decision arrangements where actual users require them. The source, implementation, and receiving owners retain their respective returns.

## SIE.Preface:6 - Qualify the combined arrangement

Three questions remain distinct. Is each source meaning, correspondence, identity disposition, or composition rule supported? Does that result permit the particular use made of it? Can all relied-on results and their realization satisfy the receiving contract together? A true relation may be too lossy for one transformation. Two individually current sources may concern different effectivity intervals. Several feasible components may exceed a shared access limit. The relevant bodies answer their local questions; the whole-use conclusion also needs these joins and common conditions.

For the combination, bind the same receiving question and the actual subjects, grain, intervals, source and rule versions, accepted losses, authority, and failure branches. Where contributions use shared requests, credentials, storage, time, or operating support, compare their total demand with the applicable conditions, including required trace and recovery behavior. A permission to query does not imply permission to replicate or disclose. Keep a common source or derivation visible when several results rely on it; repeated citations or passing tests of the same premise are not independent support for a different claim. The comparison belongs in [SIE.8, Solution](#sie84---solution) and the bounded validation in [SIE.10, Solution](#sie104---solution).

### SIE.Preface:6.1 - A shared request limit changes the provider result

Consider a constructed variation of [APP-SIE-04](#app-sie-04---high-change-provider-availability-without-a-materialized-graph). The receiving contract allows an explicitly incomplete purchasing answer. Assume that adequate models and the required source, correspondence, identity, and composition premises have been supplied. Provider A still means “on hand”; provider B means “available to promise”; their claims must keep those meanings. Permissions allow live retrieval and the agreed immediate presentation, but prohibit replication.

For this illustration, four calls retrieve A's required rows, four retrieve B's, and three retrieve the common source and rule trace required even for a partial answer. All calls consume one gateway allowance of ten requests in the agreed request window; none is shared or counted twice. Retries also consume the allowance, and the contract accepts neither a copied cache nor deferral to another window for this answer. Each pair of contributions fits: 8, 7, or 7 calls. The complete answer requires at least 11 before retries, so pairwise feasibility does not establish the whole arrangement.

SIE.8 therefore cannot select that arrangement as supplying the complete result. Under the stated incomplete-answer permission, an A-only result with the required trace uses seven calls before retries and can be proposed with B explicitly marked as not retrieved under the request limit. SIE.9 must preserve A's on-hand meaning and the incomplete branch; it must not render B as zero stock or call the response a complete provider comparison. For example, an A source value `on_hand = 12` observed at `T` becomes a receiving row `12 on hand at T`, with its source and rule trace and the branch `B not retrieved`. It supplies no available-to-promise value.

SIE.10 tests the remaining required conditions before any bounded positive validation. If both providers are mandatory, return a stop and the exact missing result: for example, an access-owner decision changing the allowance or an implementation that demonstrably reduces calls while preserving meanings and trace. Omitting provenance is not an equivalent repair.

The quantities are construction assumptions, not measurements of providers. Actual use needs evidence for the gateway condition, call demand, permissions, freshness, behavior under failure, and the receiver's interpretation. Passing source lookups or several pairwise tests cannot supply that evidence for the whole. A changed allowance reopens the affected realization and use validation; an unchanged correspondence can remain usable.

## SIE.Preface:7 - Architectural Rationale

The language is organized around the results that make a receiving use possible. Source recovery, relation truth, bounded identity, claim composition, executable semantics, realization, interface, and validation can fail independently and return to different owners. Keeping their Methods directly accessible permits a useful early stop and replacement of one contribution without inventing a new lifecycle for the entire arrangement.

| Serious alternative | When its contribution is enough | Why SIE keeps a different boundary for the combined use |
| --- | --- | --- |
| Use FPF and the owning engineering, data, MDM, or application practice directly | One exact representation, domain identity, configuration, pipeline, or decision result closes the question. | A recurring cross-source interface question still needs source-qualified correspondences, mappings, interpretation, and receiving-use validation joined together. SIE supplies that remainder and returns the other results to their owners. |
| Treat ontology engineering as the whole practice | The missing result is a model that expresses the required distinctions and questions. | An adequate existing model can support integration without a new ontology. Model construction alone does not supply identity dispositions, claim composition, executable mappings, or a usable interface. SIE.3 supplies that distinct model result. |
| Make a materialized knowledge graph the standard result | Permitted copying, a suitable refresh and correction arrangement, and reproducible queries meet the contract. | A graph is one realization. The live-provider case forbids replication, and useful incompatibility must remain expressible. Conversely, live federation is unsuitable when its access, availability, or repeatability cannot meet the use. |
| Use one canonical enterprise model and master identity | A responsible domain or MDM authority has supplied a bounded common model, identity, or authoritative-value result that the use can rely on. | Integration alone cannot grant that authority or erase local grains, versions, claims, and incompatible meanings. SIE preserves the supplied result's scope and the source identifiers that make correction possible. |
| Collapse the work into one prescribed lifecycle | A local team may use a repeatable plan for a recurring, stable situation. | A direct identity question, realization decision, or validation failure has different inputs and stops. The pattern language preserves those entries and conditional result relations; the local plan remains one use of it. |
| Separate Ontology Engineering, Knowledge Graph Engineering, and Semantic Integration into independent languages | A substantially independent first use, result chain, practitioner community, and source-refresh need would justify reconsidering the split. | The represented uses share receiving contracts, correspondence and mapping work, authority boundaries, and whole-use validation. A different technology or familiar professional name alone does not separate that work. |

The complete repertoire joins model adequacy, semantic interfaces, changed reliance, and commons maintenance through their actual results. Completing a small model or interface question remains useful on its own. A continuing service requires its operational results, and a commons requires the rights and dependencies of its actual users.

### SIE.Preface:7.1 - Source contributions behind the arrangement

The [source-use account](#source-use-and-currentness) gives the qualified source cut and its dates. The shared architecture combines contributions that answer different questions; it does not treat a standard or tool family as a complete integration Method.

Terminology and registry practice, including [ISO 704:2022](https://www.iso.org/standard/79077.html) and [ISO/IEC 11179-3:2023](https://www.iso.org/standard/78915.html), makes source objects, concepts, definitions, designations, items, and versions distinguishable. SIE.2 adapts that contribution into the smallest inventory needed by the receiver. This improves on schema inspection plus informal recollection: a mapping can point to the operative definition and edition. It still cannot infer a cross-source relation from a registry entry. FPF's source-local meaning and direct Bridge distinctions supply the separate generic questions used by SIE.2 and SIE.4.

[SKOS](https://www.w3.org/TR/skos-reference/) supplies different correspondence forms; [SSSOM 1.0](https://mapping-commons.github.io/sssom/1.0/spec-model/) makes endpoints, predicates, justification, provenance, and source versions inspectable. [OAEI 2025](https://oaei.ontologymatching.org/2025/results/) contributes task-dependent alignment evidence. In [SIE.4, SoTA-Echoing](#sie411---sota-echoing), SIE.4 uses those contributions to separate candidate generation, direct relation judgment, and a receiving-use qualification. A two-column crosswalk or score can help find a candidate, but the chosen relation, permitted loss, and counterexamples determine whether it can support this transformation. A new endpoint sense or defeating counterexample reopens that row.

[ISO 8000-115:2024](https://www.iso.org/standard/88847.html?browse=tc) contributes identifier ownership, semantics, restrictions, and resolution inputs within its declared scope. [PROV-O](https://www.w3.org/TR/prov-o/) supplies distinctions for derivation, attribution, revision, specialization, and alternate descriptions. SIE.5 and SIE.6 adapt these into two different results: an identity disposition and a source-qualified claim composition. A merged key cannot replace the first, and provenance cannot settle the second's truth or authority. The SEMI and GS1 traceability sources in [SIE.5, SoTA-Echoing](#sie511---sota-echoing) make grain, issuer, and event-time failures concrete; they do not authorize a recall or establish an enterprise master identity.

[R2RML](https://www.w3.org/TR/r2rml/) and [QVT 1.3](https://www.omg.org/spec/QVT/) contribute bounded declarative mapping and transformation forms. The [Ontop line](https://ontop-vkg.org/research/publications.html) demonstrates a virtual realization over mappings. SIE.7 and SIE.8 adapt those contributions into an independently inspectable semantic rule and a choice among whole arrangements. This costs explicit specification and comparison, but it permits an implementation to change while preserving the required behavior. Neither RDF nor MOF nor a graph store is required. Failure of a mapping premise returns to the semantic rule; an implementation discrepancy returns to its implementer.

[SHACL](https://www.w3.org/TR/shacl/) supplies declared graph-constraint tests. [DQV](https://www.w3.org/TR/vocab-dqv/) and the data-quality sources in [SIE.10, SoTA-Echoing](#sie1011---sota-echoing) contribute dimensions, measurements, and process questions. SIE.10 retains their distinct evidence roles and adds the representative receiving-use replay. A passing shape can coexist with the wrong identity or a concealed stale branch. The arrangement therefore uses categorical pass, narrow, unresolved, and stop results under the contract, rather than a compensating overall score. Evidence for implementation and operation remains necessary when the conclusion relies on actual service behavior.

[LOT](https://doi.org/10.1016/j.engappai.2022.104755) contributes ontology requirements, development, publication, and maintenance to SIE.3. Sufficient model reuse remains a completed result. [LOT4KG](https://lot.linkeddata.es/LOT4KG/) distinguishes ontology work from graph construction and relates changes to dependent mappings, constraints, and validation; SIE.11 uses those relationships for graph realizations. [OBO Foundry principles](https://obofoundry.org/principles/fp-000-summary.html) contribute scoped module, term-stability, maintenance, and communication practices to SIE.12, with their community-specific rules qualified in the source account.

Reconsider the affected choice when a simpler qualified contribution supplies the same result, a represented use repeatedly needs a missing Method, or a source or case defeats a relied-on boundary. When the need is a reusable Method repertoire, [ME.2](METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me2---recover-a-reusable-method-repertoire-and-its-lineages) returns inspectable alternatives, source contributions, relations, and gaps for that comparison; the integration-specific question stays in SIE. A substantially independent practice remainder can reopen the field split described above.

## SIE.Preface:8 - Costs, perspectives, and correction

The gain is an answer whose meanings, sources, qualifications, and unresolved branches can survive into receiving work. The cost is source recovery, explicit relation and loss judgments, trace, implementation evidence, and representative tests. Keep that burden proportional to what can change the answer. A single correspondence question does not require a service architecture; a claim of a usable whole interface cannot omit a load-bearing identity or provenance obligation merely to stay cheap.

The source cut reflects the receiver's question and the sources practitioners can inspect. A well-documented schema or a familiar formal vocabulary can receive more attention than an inaccessible local rule. Source experts and receiving users may also differ over which distinctions matter. Make missing access, authority, meanings, and perspectives visible in the contract and inventory instead of treating absence as agreement. The five constructed applications illustrate how to work; their [coverage limits](#representative-case-coverage) supply no empirical claim about production performance or effectiveness in other settings.

Correct the result at the point that owns the defect. A hidden default returns to SIE.7; an unsafe interpretation of a partial response to SIE.9; unsupported identity to SIE.5 and the required domain authority; a pipeline discrepancy to Data Engineering. For the AP242/QIF case, [SYSE.13](SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse13---establish-configuration-identity-variants-and-effectivity) supplies the decision-specific configuration basis, including actual subjects and effectivity; SIE consumes those premises and can return a mismatch, but does not decide the engineering configuration. The other [owner boundaries](#fpf-neighboring-practice-and-authority-boundaries) remain in force. Preserve unaffected qualified contributions and retest what the correction can change.

## SIE.Preface:9 - Before relying on the whole result

Recognition asks which available pattern can supply the next useful result. Assurance asks what supports the actual reliance. Use the checklists in the selected bodies and inherit their answers only while the subject, content, use, source versions, and relevant conditions match. For a combined package, answer these questions in the account the receiver needs:

- Can the receiver recover the question, answer claims, accepted losses, authority boundary, and useful stop? An early correspondence or inventory result must not be presented as a validated interface.
- Can every load-bearing correspondence, identity disposition, and claim-composition premise be traced through the mapping and interface, with its grain, interval, limits, and unresolved branches?
- Does the [whole arrangement](#siepreface6---qualify-the-combined-arrangement) meet shared semantic, access, resource, currentness, provenance, and failure conditions? Which implementation or owner result is still absent?
- Does each evidence item support the claim made from it, and does the representative receiving-use test cover positive, negative, and unlike cases? Several passing layers cannot compensate for a hard stop in another.
- Is a narrow result recognizable as narrow, with excluded or unexamined branches and their consequences visible? In the request-limit example, an A-only answer cannot stand for the complete provider comparison.
- Do a model gap, changed semantic premise, or shared-module decision reach SIE.3, SIE.11, or SIE.12 where needed? Are source, implementation, and receiving decisions returned to their owners, with unresolved dependence made visible?

These questions address the failures in the applications: field-name equivalence, merged identifiers without authority, source claims flattened into one value, healthy transport mistaken for semantic fitness, and missing branches hidden from the receiver. Repair the specific premise or interface, obtain the missing contribution, narrow under the contract, or stop.


# Part I - Semantic Integration Engineering Methods

## SIE.1 - Bound the Receiving Use and Semantic Contract

> **Type:** Method pattern
> **Status:** Eternal alpha
> **Normativity:** Normative method guidance within SIE; examples are constructed and non-normative.
>
> **Primary working result:** a `SemanticIntegrationUseContract@Use` that names one receiver and use, required answer claims, source cut, tolerated loss and uncertainty, currentness, latency, quality, authority, representative tests, stop conditions, and reopen conditions.

### SIE.1:1 - Problem Frame

**Use this when** a request says “integrate the data”, “align the models”, “build the knowledge graph”, or “make one source of truth”, but the intended receiver and decision-changing answer are not yet explicit. The recognizable failure is a technically impressive integration whose values cannot be interpreted, trusted, or used safely by the Work that requested it.

The primary EntityOfConcern is one semantic-integration use: a named receiver performing a named query, decision, operation, or engineering workflow under stated conditions. The first move is to state that use and the answer claims it needs. The first result is a bounded contract that lets later workers decide which semantic loss, source age, unresolved row, and test outcome are acceptable.

The practical gain is a testable stopping rule before source, ontology, mapping, or platform choices accumulate. Do not use this pattern to authorize the receiving decision, decide product configuration, choose master identity, operate a data pipeline, or define generic evidence law. Obtain those results from their owners. Do not reopen a current contract merely because another source exists; reopen it when the receiver, use, answer, conditions, authority, or acceptance boundary changes.

### SIE.1:2 - Problem

Without a receiving-use contract, “semantic integration” expands toward every source and every possible reuse. Similar labels are merged without a loss budget, freshness is treated as an implementation detail, and a passing schema or sample query is reported as success. The project cannot distinguish an informative unmatched row from a defect, or a harmless delay from a stale answer that changes action.

Technology then supplies the hidden contract. A graph platform encourages graph-shaped outputs, a warehouse encourages copying, and an API encourages whichever fields are easiest to expose. None says which answer claims the receiver may rely on, who owns them, or when the correct result is to stop.

### SIE.1:3 - Forces

| Force | Tension |
| --- | --- |
| Breadth | More sources may enable future reuse, while every added source creates meanings, authority, currentness, and validation obligations. |
| Speed | A quick join can demonstrate access, while early conflation makes later correction expensive and hard to trace. |
| Loss | A useful common view often coarsens detail, while silent loss can reverse a decision or erase incompatibility. |
| Freshness and latency | Query-time access can be current but slow or fragile; copied data can be fast but stale and harder to govern. |
| Authority | Source owners, integrators, and receivers contribute different decisions; visibility or custody does not transfer authority. |
| Assurance | A finite representative test is needed now, while no test establishes universal semantic correctness. |
| Reuse | A broad contract appears reusable, while a small contract is easier to validate and honestly reopen. |

### SIE.1:4 - Solution

Construct the smallest semantic contract that can change the named receiving action. Begin from the receiver and work backward to required answer claims, source contexts, meanings, losses, currentness, quality, authority, representative cases, and exact stops. Treat the contract as an input to later SIE patterns, not as proof that any source, correspondence, identity, mapping, interface, or implementation exists.

#### SIE.1:4.1 - Pattern-Use Unfolding

1. **Name the receiver and receiving Work.** Identify the System or role that will use the result, the query, decision, operation, or workflow, the horizon, and the first useful answer.
2. **State the answer claims.** Write the fields or propositions the receiver needs, including scope, grain, interval or effectivity, and the action each claim can change. Keep a value, its provenance, its authority, and the receiver's decision distinct.
3. **Select the source cut.** Name only the governed contexts and candidate source assets that can change the answer. Mark sources whose inclusion is uncertain rather than adding them silently.
4. **State preserved distinctions and tolerated loss.** Name identities, versions, units, codes, relations, claim scopes, and incompatibilities that must survive. For each permitted coarsening or omission, state why the receiver can tolerate it.
5. **State currentness, latency, availability, and quality conditions.** Choose thresholds or explicit unresolved returns only where they change use. Do not copy every available quality dimension into the contract.
6. **Recover authority, permission, and protection boundaries.** Name who defines source meanings, who may grant access, who decides identities or authoritative values, who accepts semantic loss, and who owns the receiving action. Record an exact blocker where a required relation is absent.
7. **Design representative tests before implementation.** Include at least one expected positive case, one negative or unmatched case, and one unlike or changed-source case that could defeat the proposed integration. Name the expected branch rather than requiring every test to return a value.
8. **State pass, narrow, unresolved, and stop outcomes.** A contract permits a bounded usable subset or explicit incompatibility when that is useful. Stop when a load-bearing meaning, source edition, identity authority, permission, or acceptance rule is unavailable.
9. **State reopen conditions and next result.** Identify observations that change the contract and the smallest next result, often `SourceSemanticInventory@Use` from `SIE.2`.

#### SIE.1:4.2 - Record the Result

| Contract position | Required content |
| --- | --- |
| receiver and use | named receiver, Work, query/decision/operation/workflow, horizon, and first useful answer |
| answer claims | propositions or fields, grain, scope, interval/effectivity, and action changed |
| source cut | governed contexts, candidate assets, inclusion reason, and known access limits |
| semantic boundary | distinctions to preserve, permitted loss, uncertainty treatment, unmatched/incompatible behavior |
| service conditions | currentness, latency, availability, recovery, and quality thresholds that change use |
| authority and protection | meaning owner, identifier or value authority, access/permission, receiver authority, and protected conditions |
| validation | representative positive, negative, unlike/change cases and expected branches |
| disposition | pass, narrow, unresolved, or stop rules; next result and observable reopen conditions |

#### SIE.1:4.3 - What Changes in Practice

The team stops treating integration scope as the set of reachable sources. Every later correspondence, identity disposition, mapping rule, realization, interface field, and validation claim must answer to a named receiving use and loss boundary. Explicitly unmatched or incompatible results become valid outcomes rather than defects to hide.

### SIE.1:5 - Archetypal Grounding - AP242/QIF Configuration Query

A quality engineer asks which QIF inspection plan and result concern feature `F` in released AP242 product-definition revision/configuration `R` at effectivity `E`. The initial request is “connect PLM and quality data in a knowledge graph.” SIE.1 replaces the carrier proposal with this contract:

| Position | Constructed value |
| --- | --- |
| receiver/use | quality engineer preparing an evidence return for one configuration-bound review; query by revision/configuration, feature, and effectivity |
| answer claims | AP242 feature identifier and configuration/effectivity claim; QIF plan, characteristic, and result identifiers; relation disposition; source edition; timestamp; provenance; unmatched/incompatible status |
| preserved distinctions | product feature versus inspection characteristic; definition versus performed result; revision versus configuration; applicability/effectivity; source identifier and issuer; plan versus result |
| tolerated loss | display may coarsen source-local labels after exact identifiers and relations remain available; no unmatched feature or incompatible characteristic may become a positive relation. For this constructed evidence-return review, the receiver permits the qualified row set with unresolved local-extension and unknown-unit branches shown separately; the partial answer supplies available qualified evidence while leaving those branches unresolved |
| currentness and latency | for this constructed review at time T, the receiver requires the released AP242 configuration applicable to the review, QIF observations from T minus 24 hours through T, and a query response within two seconds. These are stipulated receiving-contract criteria for this demonstration |
| authority | Systems Engineering owns release, configuration, and effectivity; the quality authority owns acceptance; source owners define their models; SIE may qualify mappings but authorizes neither decision |
| tests | known match; unmatched feature; changed revision; incompatible characteristic; stale QIF result; missing provenance; source timeout |
| stop/reopen | stop on unresolved configuration/effectivity, source edition, feature identity, permission, or acceptance rule; reopen when a relied-on AP242/QIF edition, review use, or protected condition changes |

This result does not claim that the two source models correspond or that an interface works. It makes those later claims testable. AP242 edition 4 is recorded by `SIE.2` with its current source status; SIE.1 only requires the edition and reopen rule to be explicit.

### SIE.1:6 - Bias-Annotation

| Lens | Likely drift | Repair |
| --- | --- | --- |
| Governance | The integration team silently accepts loss or acts as source/value authority. | Name each decision subject and the direct authority relation; make absence a blocker. |
| Architecture | Platform boundaries define the semantic use. | Begin from the receiving result and keep realization alternatives open. |
| Ontology/Epistemology | A shared label or data field is treated as a shared meaning or true claim. | State answer claims, source contexts, preserved distinctions, and uncertainty separately. |
| Pragmatics | The contract becomes a complete requirements catalogue rather than a decision tool. | Keep only conditions that can change the receiving action or stop. |
| Didactics | Readers infer that SIE.1 must precede every other pattern. | Enter directly elsewhere when an equivalent current contract already exists; verify compatibility instead of repeating it. |

### SIE.1:7 - Conformance Checklist

- [ ] One named receiver and receiving Work are explicit.
- [ ] The first useful answer is expressed as claims or fields with grain, scope, and interval/effectivity.
- [ ] The source cut is justified by the use rather than by reachability.
- [ ] Preserved distinctions, permitted loss, uncertainty, and unmatched/incompatible behavior are explicit.
- [ ] Currentness, latency, availability, recovery, and quality are included only where action-changing.
- [ ] Meaning, identity/value, access, semantic-loss, and receiving-action authorities remain distinct.
- [ ] Positive, negative, and unlike or changed-source tests have expected branches.
- [ ] Pass, narrow, unresolved, stop, next-result, and reopen rules are stated.
- [ ] The contract claims no correspondence, implementation, validation, authorization, or outcome that has not been obtained.

### SIE.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Integrate all enterprise data.” | Name one receiver and the smallest source cut that can change one use. |
| “The knowledge graph is the deliverable.” | State the receiving answer and treat graph materialization as one later realization option. |
| “No information loss.” | Name the distinctions and tests; unlimited preservation is not an operational contract. |
| “Real time.” | State a measurable currentness and latency condition for the use. |
| “Single source of truth.” | Name source, identity, and value authorities and the claims each may establish. |
| “Every test must return a row.” | Define legitimate unmatched, incompatible, unavailable, and stop branches. |

### SIE.1:9 - Consequences

The contract limits source fan-out, makes semantic loss and authority visible, and gives implementation and validation a shared target. It can stop an integration before expensive model or platform work. It also makes conflicts and narrow usable subsets publishable outcomes.

The cost is early negotiation about the receiver, evidence, loss, and stop conditions. Some attractive future reuse remains outside the first package and must earn its own contract or compatible extension.

### SIE.1:10 - Rationale

Semantic adequacy is relative to a use, but relativity does not make it arbitrary. A receiver, answer claim, source context, permitted loss, authority, and representative test together constrain what counts as a successful integration. Beginning there prevents a carrier choice from becoming an implicit ontology, authority model, and acceptance rule.

### SIE.1:11 - SoTA-Echoing

The best-known line for this question combines use-bounded representation selection, situational Method criteria, quality-for-use, and explicit source/provenance practice. The serious default alternative is technology- or source-led integration. Its defect is not the use of a graph, warehouse, or federation; it is allowing that choice to define the answer and loss boundary. SIE.1 mutates the line by making the whole semantic contract, including authorities and legitimate unresolved branches, the first domain result.

| Source line | Adopt, adapt, or reject | Role and limit |
| --- | --- | --- |
| Current FPF `C.37` | adopt | Bounds representation selection and co-use to a named use; does not supply the SIE package or application authority. |
| Current `ME.3` | adapt | Situational criteria help state receiving Work and fit conditions; SIE adds semantic endpoints, loss, source, authority, and layered tests. |
| [DQV](https://www.w3.org/TR/vocab-dqv/) and [ISO/IEC 25012:2008](https://www.iso.org/standard/35736.html) | adapt | Supply quality dimensions and vocabulary; the contract selects only dimensions that change this use. |
| [Data on the Web Best Practices](https://www.w3.org/TR/dwbp/) | adapt | Contributes provenance, version, access, and reuse questions; no Web publication form is mandatory. |
| platform-first “single source of truth” | reject as default | A carrier and custody arrangement cannot establish cross-source meaning, authority, or receiving-use adequacy. |

Reopen this pattern when representative uses cannot express action-changing loss, authority, or validation obligations through the contract positions, or when a source line supplies a materially better first result.

### SIE.1:12 - Relations

- `SIE.2` consumes the source cut, answer claims, distinctions, and currentness questions to produce `SourceSemanticInventory@Use`.
- `SIE.4`–`SIE.10` consume the compatible contract positions relevant to their results; none may silently widen the receiver or accepted loss.
- `C.37` governs generic use-bounded representation selection. `A.10` and `A.10.1` govern evidence/provenance and generic affected-use questions.
- Applications, Systems Engineering, Operations, quality, safety, legal, and other direct owners supply their acceptance and authority results.
- A changed contract reopens the package branches that rely on the changed premise. `SIE.11` supplies affected-use discovery and integration revalidation where the affected results still need to be established.

### SIE.1:End

## SIE.2 - Recover and Qualify Source Semantics and Authority

> **Type:** Method pattern
> **Status:** Eternal alpha
> **Normativity:** Normative method guidance within SIE; examples are constructed and non-normative.
>
> **Primary working result:** a `SourceSemanticInventory@Use` that records the load-bearing source assets, local meanings, schemes, editions and effectivity, identifiers, claims, owners and authority scope, provenance, access, currentness, gaps, and exact returns for one semantic-integration use.

### SIE.2:1 - Problem Frame

**Use this when** a bounded integration use exists, yet endpoint meanings are being inferred from labels, column names, class names, diagrams, sample values, or undocumented organizational knowledge. The recognizable failure is a mapping that runs while joining different concepts, editions, grains, or authority scopes.

The primary EntityOfConcern is the set of source-local semantic premises that the receiving use actually consumes. The first move is to select one load-bearing source asset and recover its scheme, edition or effectivity, meaning, owner, authority, provenance, and access conditions. The first result is an inventory that makes both usable premises and exact gaps inspectable.

The payoff is a clean separation between what a source says, what an integrator infers, and what another owner must decide. Do not use SIE.2 to construct an ontology, establish a cross-source correspondence, decide identity, fuse claims, or judge receiving-use adequacy. If model adequacy for a required distinction remains unsettled, request `UseFitSemanticModel@Use` from `SIE.3` or another qualified direct provider. Adequate reuse can finish that question; an actual missing distinction may require extension or construction.

### SIE.2:2 - Problem

Source inventories often list files and endpoints but omit the meanings that make their values usable. A table called `feature`, an API field called `available`, and an identifier called `partNumber` appear self-describing. Their actual senses may depend on an edition, profile, configuration, interval, issuer, lifecycle state, organizational rule, or local extension.

When those dependencies are hidden, later workers can neither justify a correspondence nor trace a failure. A changed source looks like a schema defect even when the meaning changed; an access right is mistaken for authority; and a provenance record is mistaken for truth.

### SIE.2:3 - Forces

| Force | Tension |
| --- | --- |
| Selectivity | Reading every source is infeasible, while skipping one load-bearing definition can invalidate the package. |
| Formal and operative meaning | Standards and schemas provide inspectable definitions, while actual profiles, extensions, and Work can narrow or alter use. |
| Edition and effectivity | A stable name aids reuse, while its meaning or applicability can change across revisions, profiles, configurations, and intervals. |
| Authority | Publishers and stewards define bounded schemes or values, while the receiver may need a decision outside their scope. |
| Access | A source may be meaningful but unavailable, restricted, delayed, or legally unusable for the proposed integration. |
| Adequacy | Existing models reduce construction work, while forcing an inadequate model hides a real semantic gap. |

### SIE.2:4 - Solution

Recover source semantics at the smallest grain that can change the receiving answer. Preserve term, concept, type, relation, schema, model, claim, data item, carrier, identifier, and world-side referent as different questions. Qualify each relied-on premise by source identity, edition/effectivity, authority scope, provenance, access, currentness, and known gaps.

#### SIE.2:4.1 - Pattern-Use Unfolding

1. **Take the source cut from the use contract.** Add another source only when it can change an answer claim, test, loss, or stop condition.
2. **Identify the source asset and carrier.** Record publisher or owning System, title or endpoint, profile/module, version or edition, publication and effectivity, retrieval location, and carrier kind. Keep the asset distinct from the concepts and claims it carries.
3. **Recover the local scheme and scope.** State the domain, population, lifecycle state, configuration, jurisdiction, or Work context in which the source definitions apply.
4. **Recover exact meanings.** For every load-bearing endpoint, record the designation, definition or operative rule, type/relation role, examples and counterexamples, units or codes, and unresolved ambiguity. Use source-local language before normalizing it.
5. **Separate identifiers and identified entities.** Record the scheme, issuer or owner, syntax, resolution behavior where relevant, use restrictions, grain, interval, and what the identifier does not establish.
6. **Separate claims, data, and provenance.** Record which claim a data item represents, its scope and time, how it was derived, who or what supplied it, and which uncertainty or status accompanies it. Provenance does not make the claim true.
7. **Recover authority and access.** Name who may define the scheme, issue identifiers, decide authoritative values, approve local extensions, grant access, and authorize receiving use. Mark unsupported assumptions.
8. **Assess currentness and use adequacy.** Compare the source premise with the contract. State whether it is adequate, adequate only under conditions, unresolved, obsolete for this use, inaccessible, or missing.
9. **Return an inadequate model honestly.** If the required distinction cannot be expressed in the available source or supplied semantic model, request `UseFitSemanticModel@Use`; do not hide the gap in a mapping rule.
10. **Record dependencies and next results.** Identify the exact definitions, editions, authority facts, and gaps consumed by `SIE.4`–`SIE.10`, plus observations that reopen this inventory.

#### SIE.2:4.2 - Record the Result

| Inventory position | Required content |
| --- | --- |
| source identity | owning/publishing System, asset or endpoint, profile/module, carrier, location |
| edition and applicability | version/edition, publication, effectivity/configuration/interval, local extension status |
| local semantic endpoints | designation, definition or operative rule, type/relation role, scope, examples/counterexamples, units/codes |
| identifiers | scheme, issuer/owner, syntax, resolution behavior, restrictions, grain, interval, identified-entity claim |
| claims and data | source claim, represented data item, scope/time, uncertainty/status, derivation and provenance |
| authority and access | meaning, identifier, value, extension, access, and receiving-use authority scopes |
| qualification | adequate, conditional, unresolved, obsolete, inaccessible, missing, or model-gap return with reason |
| dependency and reopen | consuming package rows, known gaps, next result, and source/edition/meaning changes that reopen |

#### SIE.2:4.3 - What Changes in Practice

The team stops mapping from field names. A later correspondence or transformation can point to exact source-local endpoints and editions, and a failure can return to the owner of the missing meaning, authority, access, or model. An inventory row can be useful even when its disposition is unresolved or inaccessible.

### SIE.2:5 - Archetypal Grounding - AP242 and QIF Source Cut

For the AP242/QIF query in `SIE.1`, the team inventories only source premises that can change the configuration-bound answer.

| Source row | Qualification for the constructed use |
| --- | --- |
| AP242:2025 edition 4 | Product-definition, configuration/change, and effectivity source for the case. Record the official publication identity and current stage 90.92, “to be revised”. The source owner defines its model; Systems Engineering decides which released configuration applies locally. |
| local AP242 exchange/profile | Record the exact application protocol/profile, implementation conventions, export version, local extensions, identifiers, and configuration/effectivity fields actually supplied. The standard title alone does not establish those facts. |
| QIF source | Record the applicable ISO 23952:2020 carrier/profile, plan, characteristic, and result meanings, identifiers, measurement context, status, and local quality authority. A QIF result identifier does not establish AP242 feature identity. |
| local source records | Record export or API occurrence, timestamps, derivation, access, issuer, local configuration or inspection status, and gaps. A reachable file is not automatically current or authorized for review. |

The inventory marks an unresolved local AP242 extension used by one feature class. Because its meaning can change the correspondence, the package stops that row and returns to the extension owner. Other rows can continue. If neither AP242 nor QIF can express a required tolerance-state distinction, the inventory requests a qualified `UseFitSemanticModel@Use`; it does not invent the distinction in the transform.

### SIE.2:6 - Bias-Annotation

| Lens | Likely drift | Repair |
| --- | --- | --- |
| Governance | Custody or access is mistaken for semantic or value authority. | Record each authority scope and the evidence for it separately. |
| Architecture | The inventory mirrors the integration platform rather than governed sources. | Identify source assets and meanings independently of the selected realization. |
| Ontology/Epistemology | Term, concept, type, relation, identifier, claim, data, and referent collapse into one “field”. | Use separate inventory positions and preserve unresolved senses. |
| Pragmatics | Exhaustive documentation delays the use without changing it. | Inspect only premises that can change an answer, loss, test, or stop. |
| Didactics | A standards citation is read as proof that the local export conforms or is current. | Record the local profile, occurrence, evidence, extension, and effectivity separately. |

### SIE.2:7 - Conformance Checklist

- [ ] Every included source can change a named contract position.
- [ ] Source asset, carrier, local scheme, semantic endpoint, identifier, claim, data item, and referent remain distinguishable.
- [ ] Edition, profile/module, effectivity/configuration/interval, and local extensions are explicit where load-bearing.
- [ ] Definitions or operative rules include scope and at least one discriminating example or counterexample where ambiguity matters.
- [ ] Identifier scheme, issuer/owner, grain, interval, restrictions, and resolution assumptions are explicit.
- [ ] Claims retain provenance, scope, time, status, and uncertainty without treating provenance as truth.
- [ ] Meaning, identifier, authoritative-value, extension, access, and receiving-use authorities remain separate.
- [ ] Every row has an adequate, conditional, unresolved, obsolete, inaccessible, missing, or model-gap disposition.
- [ ] Consuming rows and reopen conditions are recoverable.

### SIE.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Data dictionary by column name | Add source-local definition, scope, edition, units/codes, examples, and authority. |
| Standards title as implementation evidence | Inspect the actual profile, export, extension, occurrence, and conformance evidence. |
| “Same ID format means same object.” | Record scheme, issuer, grain, interval, and identified-entity claim; use `SIE.5` for cross-source identity. |
| Provenance equals truth | Keep derivation and source authority separate from domain truth and receiving acceptance. |
| Read every source | Start from the contract and add only action-changing premises. |
| Patch a model gap in code | Return the missing semantic-model result before relying on the rule. |

### SIE.2:9 - Consequences

Mappings become reviewable against exact endpoints, and source changes can be traced to the rows that relied on them. Authority, access, and model gaps appear before implementation. The same inventory can support several direct pattern entries while each use retains its own qualification.

The cost is source-local reading and coordination with publishers, stewards, domain specialists, and access owners. Some attractive automation must wait because the source meaning or applicability is unresolved.

### SIE.2:10 - Rationale

Semantic integration cannot preserve a meaning that has not been recovered at the source. Source-local recovery also prevents a shared vocabulary from becoming a hidden replacement for source authority. Qualification by use keeps the inventory finite and prevents documentation breadth from substituting for a workable package.

### SIE.2:11 - SoTA-Echoing

The best-known line combines terminology work, metadata-registry discipline, provenance, and source-local meaning recovery. The serious default is schema inspection plus organizational folklore. Its defect is not informality alone; it leaves no stable relation among the source claim, edition, authority, and mapping premise. SIE.2 adapts the line into a use-qualified manifest with an explicit inadequate-model return.

| Source line | Adopt, adapt, or reject | Role and limit |
| --- | --- | --- |
| Current FPF `F.0.1` and `F.0.2` | adopt | Recover source-local meaning and episteme identity; do not establish a cross-source correspondence or domain truth. |
| [ISO 704:2022](https://www.iso.org/standard/79077.html) | adapt | Keeps objects, concepts, definitions, and designations distinct; it does not decide the receiving integration. |
| [ISO/IEC 11179-3:2023](https://www.iso.org/standard/78915.html) and its [item-mapping amendment](https://www.iso.org/standard/89914.html?browse=tc) | adapt | Contribute registry-item identity, versions, definitions, and mapping metadata; no automatic cross-source identity or fitness follows. |
| [PROV-O](https://www.w3.org/TR/prov-o/) | adapt | Distinguishes entities, activities, agents, derivation, revision, invalidation, attribution, and primary source; provenance establishes neither truth nor permission. |
| schema-only discovery | reject as sufficient | Structure and samples can locate questions but cannot replace source-local meaning, edition, authority, and applicability. |

Reopen when a source change alters a relied-on meaning, scheme, edition, effectivity, authority, access condition, or provenance chain, or when repeated cases show that an inventory position cannot support the downstream decision.

### SIE.2:12 - Relations

- `SIE.1` supplies the receiving use, source cut, answer claims, preserved distinctions, and stop conditions.
- `SIE.3` qualifies an available model for the named use or develops an actual missing distinction. Request that result when the recovered source model leaves the integration's model question unsettled.
- `SIE.4`, `SIE.5`, and `SIE.6` consume exact endpoint meanings, source claims, identifiers, editions, and authority limits.
- `SIE.7`–`SIE.10` consume the manifest, provenance, currentness, and gap dispositions relevant to implementation and validation.
- Domain sources, MDM, access owners, Systems Engineering, Data Engineering, and applications retain their respective meanings, values, permissions, operational results, and decisions.

### SIE.2:End

## SIE.3 - Construct or Reuse a Semantic Model for a Named Use

> **Type:** Method pattern
> **Status:** Eternal alpha
> **Normativity:** Normative method guidance within SIE; examples are constructed and non-normative.
>
> **Primary working result:** a `UseFitSemanticModel@Use`: a reused, extended, or constructed semantic model qualified for the questions and distinctions that its receiving use requires.

### SIE.3:1 - Problem Frame

**Use this when** an integration needs to express a meaning or answer a question and the adequacy of its available models is unsettled. For example, a source describes an inspection requirement, while the receiving query needs to distinguish that requirement from an observation of a particular configured feature.

Start with one question the model must help answer and examples of answers that would count as different. Ask the domain participants to explain those distinctions before choosing an encoding. The first useful result can be confirmation that an existing model is sufficient, with its applicable edition and use conditions.

The object is the semantic model for that use: its concepts, relation meanings, constraints, and relevant commitments. The practical gain is a model whose distinctions can guide correspondence and mapping work. A stronger claim, such as adequacy for additional questions or valid inference in a formal language, needs evidence for those additional conditions.

If the supplied model is already qualified for the unchanged use, reuse that result. If the only open question is a correspondence between adequately understood source meanings, use SIE.4. A new integration endpoint alone does not create a model-construction requirement.

### SIE.3:2 - Problem

Available models often look adequate because their terms resemble the receiving question. A field named `inspection` may cover a plan, a requirement, an occurrence, or a result. Mapping every such field to one class can remove exactly the distinction the receiver needs.

The opposite failure is to construct a larger ontology whenever a model question arises. That incurs design and maintenance work even when an existing model can answer the question. Both failures begin before formalization: the required meaning and its useful boundary have not been established.

### SIE.3:3 - Forces

| Force | Tension |
| --- | --- |
| Reuse | Existing meanings and tools save work, while an unrecognized gap can invalidate the receiving answer. |
| Domain understanding | Participants know their practice, while familiar words can hide different concepts, grains, or temporal commitments. |
| Expressiveness | Richer formalization can support useful inference, while its cost and restrictions may exceed the use. |
| Modularity | An extension can preserve reusable content, while incompatible commitments may require a different model. |
| Maintenance | Consumers need a stable reference, while the domain and its required questions can change. |

### SIE.3:4 - Solution

Select or develop only the semantic content needed for the named use. Qualify it through discriminating cases and make its maintained edition accessible to the consumers who will rely on it.

#### SIE.3:4.1 - Pattern-Use Unfolding

1. **State the questions and answer distinctions.** Use competency questions or an equivalent plain description. Name the subject, grain, configuration or interval where relevant, expected answer, and a counterexample. Work with domain participants at a level where they can explain the distinction. Separate a useful model question from a request to choose a storage or diagramming tool.
2. **Recover the available meanings.** Use the relevant SIE.2 results or directly supplied source meanings. Inspect candidate models' definitions, relations, constraints, examples, edition, access, and maintenance conditions where those can affect the use. Source labels alone cannot settle suitability.
3. **Try sufficient reuse.** Replay the required questions and counterexamples against an available model. When its content and applicable conditions suffice, return that model and the qualification. This completes the Method. Leave an uncovered question explicit if a permitted narrower use can continue.
4. **Locate the actual gap.** Identify the missing distinction, relation, constraint, or incompatible commitment. Extend a module when the addition can preserve the existing commitments that consumers still use. Construct a different model when reuse or such an extension cannot supply the required content. Keep the reason tied to the gap.
5. **Develop the meaning before encoding it.** Define the needed concepts and relations, their domains of application, and the grain or temporal interpretation required by the question. Show examples and counterexamples to domain participants. Preserve a source disagreement that affects use; SIE.4 can establish a qualified correspondence between different meanings.
6. **Choose sufficient formalization.** A maintained vocabulary and relation description can be enough for some uses. Select a formal language or profile when exchange, constraints, or inference require its semantics. Check the properties claimed under that choice as well as the domain cases. Repair or qualify a model that passes an encoding check but answers the domain question incorrectly.
7. **Return a maintained, use-qualified model.** Identify the edition or stable content, covered questions, material limits, and the access and maintenance arrangement its consumers need. Return its meanings to correspondence or mapping work and its cases and qualifications to validation. A missing authoritative definition can leave one question unresolved while independently supported questions finish.

A small model can express these obligations in one short maintained description. Formalization adds the assurance required by the selected language and use. It does not change which domain question the model must answer.

#### SIE.3:4.2 - Record the Result

| Result position | Content needed by the receiver |
| --- | --- |
| Named use | Questions, expected answer distinctions, and applicable subject, grain, time, or configuration. |
| Selected model | Reused model or developed module, its edition, definitions, relation meanings, and required commitments. |
| Reuse or development decision | The adequacy evidence, or the gap that justified an extension or different model. |
| Qualification | Covered cases, counterexamples, limits, unresolved questions, and any selected formal checks. |
| Continued reliance | Access, maintenance responsibility, relied-on source conditions, and change conditions that can reopen the result. |

The result can refer to an existing qualified model instead of reproducing it. Record a reason only where it helps a consumer interpret or rely on the selection.

#### SIE.3:4.3 - What Changes in Practice

The integrator can explain why the model distinguishes two answers, or why an existing distinction is sufficient. A mapping author receives meanings and cases rather than an unexplained class list. Model construction becomes a response to a demonstrated gap.

### SIE.3:5 - Archetypal Grounding

#### SIE.3:5.1 - Reuse for Provider Availability

The receiving interface returns separately attributed provider quantities. Its questions are “How much is on hand now?” and “How much can this provider promise under its reservation and time-horizon rules?”

An available model already distinguishes both measures, their provider, unit, observation time, and relevant horizon. The integrator checks the following cases:

| Case | Required model interpretation |
| --- | --- |
| Provider A reports 12 on hand; provider B reports 9 available to promise. | Two qualified quantities with distinct measure meanings. |
| Both values happen to equal 12. | Numerical equality does not remove the difference between the measures. |
| The provider changes the promise horizon. | The horizon remains part of the promise meaning used by the receiver. |

The model represents these cases and has suitable access and maintenance conditions. The completed result references that edition for the two questions. It supplies no common quantity formed by adding the values; that operation would require a separately justified receiving meaning.

#### SIE.3:5.2 - Extend an Inspection Model

A constructed product-definition and inspection integration asks: “What observation concerns requirement Q for feature F in configuration R?” The source model already describes the feature and its requirement, but represents no actual observation.

| Model content | Development and case |
| --- | --- |
| Existing feature and requirement | Reuse their qualified definitions and configuration applicability. |
| Observation | Add the actual observation as distinct from its plan and the requirement being checked. |
| Observation relation | State which configured feature and applicable requirement it concerns. |
| Unit and time | Express the interpretation required for this observation and question. |
| Counterexamples | A planned inspection is not an observation; an observation of another configuration does not answer this question. |

The domain participants confirm those distinctions and identify any unresolved source-specific interpretation. The module can then supply SIE.4 and SIE.7 with the required meanings. In an AP242/QIF installation, its actual profiles, configuration relations, and inspection meanings must come from the qualified source results; the constructed model above is the working example, not a claim about a particular exchange's conformance.

### SIE.3:6 - Bias-Annotation

| Lens | Likely drift | Repair |
| --- | --- | --- |
| Governance | One participant's preferred vocabulary silently becomes the shared meaning. | Obtain the meanings needed by the receiving use and preserve unresolved authority or source disagreement. |
| Architecture | A platform choice determines the model's concepts. | State the questions and distinctions before selecting formalization or realization. |
| Ontology/Epistemology | Requirement, plan, observation, and result collapse because they share a label. | Use a counterexample that changes the receiving answer. |
| Pragmatics | A new ontology is built despite adequate reusable content. | Try the existing model and finish when the use is supported. |
| Didactics | A formal diagram appears sufficient without a working example. | Show how the model answers the question and excludes its counterexample. |

### SIE.3:7 - Conformance Checklist

- [ ] The receiving questions and material answer distinctions are recoverable.
- [ ] Available model content is compared with those questions before development is selected.
- [ ] Sufficient reuse can complete the result.
- [ ] Developed content answers an identified gap and preserves relied-on commitments or qualifies the affected use.
- [ ] Domain examples and counterexamples support the claimed scope.
- [ ] Formal checks match the selected encoding and claimed inference or exchange use.
- [ ] The receiver can identify and access the maintained model and its limits.

### SIE.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Model from familiar labels | Recover relation meanings and replay a discriminating question. |
| Construction as proof of progress | Return adequate existing content when the use is already supported. |
| Hidden repair in a transformation rule | Develop the missing semantic distinction and give the rule a qualified premise. |
| Language validity used as domain adequacy | Check the domain answer as well as the selected formal properties. |

### SIE.3:9 - Consequences

A qualified model makes correspondence and mapping decisions more explicit and reusable. Small integrations can finish with a small model. Extensions expose their actual commitments to later consumers.

The work costs domain conversation, example construction, and any formal checks the chosen use requires. Some questions remain unresolved until a source owner supplies a needed meaning. Larger scope creates additional content and maintenance obligations.

### SIE.3:10 - Architectural Rationale

Questions and counterexamples locate the distinctions that an integration must preserve. Reuse is therefore judged by its contribution to the question; extension is justified by a specific gap. Keeping model content, its maintained edition, its formal encoding, and its instances distinct makes both adequacy and later change easier to assess.

### SIE.3:11 - SoTA-Echoing

The practice question is how to settle an available model's adequacy for the receiving questions when that adequacy is still unknown. For the inspection question in §5.2, the selected starting line is requirements-led model qualification: recover the distinction between requirement, plan, and observation, try the available meanings, and develop only the gap that survives that trial. This adapts [LOT](https://doi.org/10.1016/j.engappai.2022.104755) and its [maintained resources](https://github.com/oeg-upm/LOT-resources).

A serious alternative for that same unsettled question is to develop the model together with a small knowledge-graph prototype, adapting the ontology-and-graph work described by [LOT4KG](https://lot.linkeddata.es/LOT4KG/). The prototype can reveal a missing relation when the receiving query is executed. Compare a bounded prototype with bounded model qualification, rather than charging it for a complete production platform:

| Answer to the same inspection-model question | Comparable work and useful evidence | Choice and accepted trade-off |
| --- | --- | --- |
| Qualify or extend the model before selecting its realization | Examine the required definitions with domain participants and replay the requirement/plan/observation, configuration, unit, and time cases. Keep the model and cases sufficient for that query. | **Adapt** LOT in §4.1.1–5 and §5.2. This settles the semantic distinction without choosing graph encoding or query machinery. It supplies no evidence that an executable mapping or query is correct; SIE.7 and SIE.10 still need that evidence for their own claims. |
| Qualify the model through a small graph and executable query | Examine the same definitions and cases, then encode representative instances and the query. This adds encoding and execution work but can expose errors that a prose-only model trial misses. | **Adapt** the LOT4KG route when execution can settle an uncertainty material to model adequacy, especially when graph realization is already selected. In §5.2, the first unresolved issue is what counts as an observation; executing a query over a class that also includes plans cannot settle that domain meaning. The model-first route is selected for that issue, accepting deferred execution evidence. |

The comparison is qualitative and scoped to the same questions and counterexamples; it is not a claim that one route is always cheaper or more effective. A prototype's additional effort earns its place when it can change the qualification. Neither route can replace domain meaning with successful execution.

The remaining contributions constrain that choice:

| Source and comparison role | Operative move and limit |
| --- | --- |
| LOT supplies the selected requirements, development, publication, and maintenance line. | **Adopt** domain questions and participant validation; **adapt** §4.1.3 and §4.1.7 so sufficient reuse can finish and the receiver can rely on a maintained model. The source does not decide local meanings or establish this model's adequacy. |
| LOT4KG supplies the coupled ontology/graph alternative. | **Adapt** its separation of ontology work and graph construction to the comparison above; **reject** treating graph construction as the only way to qualify a model. Its described activities support this alternative, not a measured superiority claim. |
| [OWL 2 Overview](https://www.w3.org/TR/owl2-overview/) supplies language and profile choices when formal semantics matter. | **Adapt** §4.1.6: check the properties actually claimed for the chosen language as well as the domain cases. Encoding validity cannot replace the model-adequacy question. |
| The public [ISO/IEC 21838-1](https://www.iso.org/standard/71954.html) scope supplies a possible top-level basis. | **Adapt** §4.1.2/6 only when that basis contributes needed coherence. It establishes neither a universal upper-ontology requirement nor local maintenance and versioning rules. |

Reopen the comparison if one required answer depends on a selected query or inference behavior that the model-only trial cannot settle, if a bounded prototype exposes a missed distinction, or if an available model can now answer the same cases with less qualification work. Return only to the affected question and §4.1.2–6. An already qualified model for an unchanged use remains the sufficient direct result in §4.1.3.

### SIE.3:12 - Relations

- SIE.1 supplies the receiving question, preserved distinctions, and permitted scope.
- SIE.2 supplies source meanings and identifies model gaps.
- SIE.4 uses model meanings to establish qualified correspondences; SIE.7 uses them in executable mappings.
- SIE.10 validates the integration's claimed receiving result using the relevant model qualification.
- SIE.11 follows a changed model premise to affected uses. SIE.12 supplies shared-module arrangements when an actual commons requires them.
- FPF terminology, kind, relation, and evidence guidance constrains the corresponding model claims; domain participants supply the problem-specific meanings.

### SIE.3:End

## SIE.4 - Establish Use-Qualified Cross-Source Correspondences

> **Type:** Method pattern
> **Status:** Eternal alpha
> **Normativity:** Normative method guidance within SIE; examples are constructed and non-normative.
>
> **Primary working result:** a `QualifiedCorrespondenceSet@Use` whose rows identify exact source-local endpoints, relation or incompatibility, orientation, bounded use, permitted loss, justification and evidence, source versions, counterexamples, confidence where meaningful, and accepted, rejected, unresolved, or incompatible disposition.

### SIE.4:1 - Problem Frame

**Use this when** two or more governed sources contain concepts, types, relations, fields, codes, model elements, or claims that appear to match and a receiving use needs their relation made explicit. Typical triggers are a shared label, a crosswalk, an automated matcher result, a spreadsheet of “equivalences”, or a model-to-model mapping whose semantic premise has never been judged.

The primary EntityOfConcern is one use-qualified cross-source correspondence row. The first move is to recover both endpoint senses and ask which direct relation, difference, or incompatibility is actually supported. The first result is a set that preserves accepted, rejected, unresolved, and incompatible rows rather than forcing every candidate into an equivalence.

The payoff is a defensible semantic premise for identity work, claim composition, executable mappings, and validation. Do not use SIE.4 to construct a missing semantic model, decide cross-source identity, define transformation code, or choose the authoritative value. A local relation inside one governed source remains with its source owner unless the cross-source use makes it an integration premise.

### SIE.4:2 - Problem

Correspondence candidates are cheap. Labels can be normalized, lexical similarity scored, hierarchies compared, and model structures aligned. Yet “similar”, “related”, “narrower”, “same field name”, and “safe to substitute here” answer different questions. A row can be a true relation and still lose distinctions that the receiving use requires.

When candidate generation and qualification collapse, downstream mapping code inherits an unstated ontology and loss policy. Counterexamples are discarded as data-quality defects, source versions disappear, and a reviewer cannot tell whether the relation itself or only its use is unsupported.

### SIE.4:3 - Forces

| Force | Tension |
| --- | --- |
| Automation | Matchers can surface many candidates, while their scores do not establish relation truth or permitted use. |
| Reuse | A general crosswalk is attractive, while relation adequacy can change with receiver, grain, interval, and accepted loss. |
| Precision | Exact relation kinds prevent overclaim, while sources may not support a complete formal characterization. |
| Coverage | Pressure favors filling every row, while unresolved and incompatible rows can be the most decision-useful result. |
| Direction | Transformation needs an orientation, while many conceptual relations are not symmetric or safely reversible. |
| Versioning | Stable mapping identifiers aid reuse, while endpoint meaning can change across source editions and profiles. |

### SIE.4:4 - Solution

Separate candidate discovery, direct relation judgment, and bounded-use qualification. For each row, identify exact source-local endpoints, state the relation or incompatibility and orientation, justify it with evidence and counterexamples, then decide whether that relation may support the named use under a stated loss boundary. Keep the direct relation and its use qualification independently inspectable.

#### SIE.4:4.1 - Pattern-Use Unfolding

1. **Take the question from the contract.** State the receiving answer and why this endpoint relation can change it.
2. **Bind exact endpoints.** Reference the `SIE.2` source rows, schemes, definitions, editions, profiles, effectivity, units, codes, and local extensions. Do not map labels without their senses.
3. **Generate candidates without promotion.** Lexical, structural, instance, expert, historical, or matcher evidence may nominate a row. Record the candidate source and score where useful, but do not treat nomination as acceptance.
4. **State the direct relation or difference.** Use the narrowest warranted relation vocabulary. State direction and whether the inverse, symmetry, or transitivity is actually supported. If no positive relation is established, choose rejected, unresolved, or incompatible with reason.
5. **Test examples and counterexamples.** Include instances or cases that should satisfy the relation and cases that distinguish endpoints, including version, unit, code, granularity, lifecycle, and authority differences.
6. **Qualify the receiving use.** State which substitution, comparison, join, navigation, or transformation the row permits, what semantic loss it introduces, and which uses remain forbidden.
7. **Preserve evidence and authority.** Record justification, evidence source, reviewer or domain authority where required, uncertainty or confidence, and the owner of any unresolved domain judgment.
8. **Assign a row disposition.** Use accepted-for-use, accepted-with-loss, rejected, unresolved, or incompatible. A row can state a true broader/narrower relation yet be rejected for this use.
9. **State dependencies and tests.** Name whether `SIE.5`, `SIE.6`, or `SIE.7` consumes the row, plus a test or observation that reopens it.

#### SIE.4:4.2 - Record the Result

| Correspondence position | Required content |
| --- | --- |
| row identity and use | stable row identifier, receiver/use, consuming result |
| source endpoint | source, scheme/model, exact sense, edition/profile/effectivity, identifier |
| target endpoint | source, scheme/model, exact sense, edition/profile/effectivity, identifier |
| direct relation | relation or explicit difference/incompatibility, orientation, inverse/symmetry/transitivity qualification |
| use qualification | permitted operation, accepted loss, forbidden reuse, conditions |
| warrant | candidate origin, justification, evidence, authority, uncertainty/confidence where meaningful |
| challenge | positive examples, counterexamples, negative/unlike cases |
| disposition and continuation | accepted-for-use, accepted-with-loss, rejected, unresolved, incompatible; downstream reference and reopen condition |

#### SIE.4:4.3 - What Changes in Practice

The team stops treating a mapping spreadsheet as a bag of equalities. A matcher result becomes a candidate; a domain judgment becomes a relation warrant; and a receiving-use decision states what the relation may safely support. Unresolved and incompatible rows remain visible to the interface and tests.

### SIE.4:5 - Archetypal Grounding - Product Feature and Inspection Characteristic

In the AP242/QIF application, the lexical candidate `feature ↔ characteristic` is too broad. The source inventory distinguishes an AP242 product-definition feature, a QIF inspection characteristic, the plan relation that applies a characteristic to a feature, and a measured result concerning that characteristic.

| Candidate row | Direct relation judgment | Use qualification and disposition |
| --- | --- | --- |
| AP242 feature `F-17` ↔ QIF characteristic `C-17` | not identity and not class equivalence; the QIF plan asserts that `C-17` concerns the identified product feature under configuration/effectivity `R/E` | accepted-for-use as a directed `inspection-characteristic-concerns-feature` relation only after `SIE.5` qualifies the feature endpoint; no reverse substitution |
| AP242 feature type `hole` ↔ QIF characteristic type `diameter` | a diameter characteristic can characterize some holes, but the types are neither equal nor simply broader/narrower | accepted-for-use for navigation from a selected plan row with a qualified feature endpoint to its linked hole feature and diameter characteristic. Return their separate source identifiers and types with the plan relation; forbidden as a global type crosswalk |
| AP242 feature `F-22` ↔ QIF characteristic `C-99` | the candidate arose from a shared local label; effectivity and plan evidence do not support the relation | rejected; the interface returns unmatched rather than joining |
| legacy feature class ↔ current QIF characteristic class | one local extension lacks an authoritative definition | unresolved and stopped for dependent mapping; return to the extension owner |

The set records endpoint editions and counterexamples such as a non-dimensional inspection characteristic and a feature absent at effectivity `E`. It establishes semantic premises; it does not decide that identifiers denote the same entity or specify executable joins.

### SIE.4:6 - Bias-Annotation

| Lens | Likely drift | Repair |
| --- | --- | --- |
| Governance | A matcher or integrator silently becomes the domain relation authority. | Record the warrant, decision scope, and required domain authority for each accepted row. |
| Architecture | Available mapping technology limits the relation vocabulary. | State the semantic relation first; choose its carrier later. |
| Ontology/Epistemology | Similarity, correlation, broader/narrower relation, and equivalence collapse. | Use the narrowest supported relation and preserve uncertainty and counterexamples. |
| Pragmatics | Every possible endpoint pair is reviewed. | Restrict rows to relations that can change the contract or a dependent result. |
| Didactics | Direction arrows are read as a mandatory processing order. | Explain orientation as relation or transformation meaning, not lifecycle sequence. |

### SIE.4:7 - Conformance Checklist

- [ ] Every row serves a named receiving use and consuming result.
- [ ] Both endpoints reference exact source-local senses and applicable editions/profiles.
- [ ] Candidate generation is distinguishable from relation judgment.
- [ ] The direct relation, difference, or incompatibility uses the narrowest warranted kind and states orientation.
- [ ] Inverse, symmetry, and transitivity are not inferred without support.
- [ ] Positive examples and discriminating counterexamples are present where load-bearing.
- [ ] Permitted operation, semantic loss, conditions, and forbidden reuse are explicit.
- [ ] Evidence, uncertainty/confidence, and decision authority are inspectable.
- [ ] Rejected, unresolved, and incompatible rows remain available to downstream interfaces and tests.
- [ ] The set claims neither cross-source identity nor executable transformation by implication.

### SIE.4:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Same label, therefore same meaning | Recover endpoint senses and test counterexamples. |
| Matcher score as truth | Treat the score as candidate evidence; obtain a relation warrant and use decision. |
| Every relation is `sameAs` | Distinguish identity, equivalence, broader/narrower, related, concerns, transforms-to, difference, and incompatibility. |
| One global crosswalk | Qualify rows by use, source editions, loss, and forbidden reuse. |
| Symmetric spreadsheet mapping | State orientation and test whether the inverse is supported. |
| Delete failed rows | Retain rejected, unresolved, and incompatible dispositions for receiver and validation behavior. |

### SIE.4:9 - Consequences

The correspondence set gives mapping and interface work explicit semantic premises and preserves honest negative results. It makes version and loss dependencies visible and allows a narrow use to proceed while other rows remain unresolved.

The cost is row-level judgment and counterexample work. Automated matchers remain useful for candidate discovery but cannot close the relation or its receiving-use qualification alone.

### SIE.4:10 - Rationale

A direct relation and permission to use that relation answer different questions. Keeping them separate allows a true relation to be rejected for a loss-sensitive use and a qualified narrow relation to support one operation without being promoted globally. This is the smallest structure that protects both semantic truth and practical action.

### SIE.4:11 - SoTA-Echoing

The best-known line combines explicit relation vocabularies, mapping metadata, alignment evaluation, and direct Bridge truth. The serious default is a two-column crosswalk plus confidence score. Its defect is that it hides endpoint senses, relation algebra, bounded-use loss, and counterexamples. SIE.4 adapts current mapping practice into a set whose negative dispositions and use qualification are first-class.

| Source line | Adopt, adapt, or reject | Role and limit |
| --- | --- | --- |
| Current FPF `F.9` | adopt | Governs each direct cross-context Bridge and separate bounded-use claim; a package row must not replace Bridge truth. |
| [SKOS Reference](https://www.w3.org/TR/skos-reference/) | adapt | Supplies distinct mapping relation forms and cautions through their semantics; SKOS does not prove a candidate relation or authorize substitution. |
| [SSSOM 1.0](https://mapping-commons.github.io/sssom/1.0/spec-model/) | adapt | Contributes inspectable subjects, predicates, objects, provenance, justification, confidence, and source versions; metadata completeness is not relation truth. |
| [OAEI 2025 results](https://oaei.ontologymatching.org/2025/results/) | adapt | Demonstrate task- and track-dependent alignment evaluation; benchmark performance does not decide a local row. |
| label-only or score-only crosswalk | reject as sufficient | It can nominate candidates but cannot establish endpoint senses, relation, permitted loss, or authority. |

Reopen when an endpoint meaning or edition changes, a counterexample defeats the relation or use qualification, the receiver's loss boundary changes, or a better relation vocabulary materially changes action.

### SIE.4:12 - Relations

- `SIE.2` supplies exact endpoint senses, editions, profiles, authority limits, and model gaps.
- `SIE.3` is a conditional external return when available models cannot express a required endpoint distinction.
- `SIE.5` consumes rows that expose a load-bearing cross-source identity question.
- `SIE.6` uses correspondences to decide which source claims are comparable or composable without erasing scope or conflict.
- `SIE.7` consumes only accepted rows under their stated use and loss conditions; it adds executable transformation semantics.
- `SIE.10` tests correspondence truth and use qualification independently from mapping execution.

### SIE.4:End

## SIE.5 - Resolve Cross-Source Identity without Erasing Identifier Authority

> **Type:** Method pattern
> **Status:** Eternal alpha
> **Normativity:** Normative method guidance within SIE; examples are constructed and non-normative.
>
> **Primary working result:** a `CrossSourceIdentityDisposition@Use` that states, for each load-bearing endpoint pair or set, the required entity grain and interval, identity-related disposition, source identifier schemes and issuers, evidence, authority boundary, unresolved cases, and the exact mappings, claim compositions, interfaces, and tests that may consume it.

### SIE.5:1 - Problem Frame

**Use this when** an integration needs to decide whether records or identifiers from different sources concern the same entity, a part, a version, a variant, an alternate description, a family, or different or unresolved entities. The recognizable failure is a join, merged key, or `sameAs` assertion that makes identifiers appear unified while erasing their issuers, grains, intervals, and authority.

The primary EntityOfConcern is one bounded cross-source identity question for a named use. The first move is to state the entity grain and time or effectivity interval at which sameness matters. The first result is a disposition that downstream work can inspect and challenge without replacing source identifiers or master-data authority.

The payoff is that the integration can join only warranted cases, return exact unresolved branches, and preserve source trace. Do not use SIE.5 to create identifiers, choose enterprise master identity or survivorship, decide authoritative values, or prove a source claim true. Those decisions remain with identifier owners, MDM, or the direct domain authority.

### SIE.5:2 - Problem

The same real-world item can carry manufacturer, supplier, enterprise, lot, serial, package, event, and temporary process identifiers. Conversely, the same character string can be reused by different issuers or at different times. Version, configuration, part-whole, and alternate-description relations can be mistaken for identity because they support some joins.

If an integration collapses those distinctions, provenance becomes decorative: the merged record no longer shows which identifier asserted what, when, or under whose rules. Contradictory events appear to concern one thing without evidence, and a master key silently becomes a domain decision.

### SIE.5:3 - Forces

| Force | Tension |
| --- | --- |
| Joinability | A common key makes computation easy, while premature merging can create false identity and irreversible provenance loss. |
| Grain | Receivers want one “item”, while wafer, die, device, package, lot, feature, version, and event answer different questions. |
| Time and effectivity | Identity may be stable across one interval, while reuse, replacement, split, merge, and revision change the warranted claim. |
| Authority | Identifier issuers and master-data stewards govern different schemes and decisions; crosswalk custody transfers neither authority. |
| Incomplete evidence | A bounded decision is needed, while some pairs must remain unresolved without blocking independent rows. |
| Reuse | A disposition can help several mappings, while its grain, interval, and use boundary prevent blanket equivalence. |

### SIE.5:4 - Solution

Frame identity as a source-qualified, grain- and interval-specific disposition for one receiving use. Preserve every source identifier and issuer. Compare the entity criteria, relation evidence, version/effectivity, and authoritative decisions that matter. Return same, different, part, version, variant, alternate-description, family, or unresolved only at the precision supported; do not force every useful relation into identity.

#### SIE.5:4.1 - Pattern-Use Unfolding

1. **Name the receiving identity question.** State which mapping, claim composition, query, or decision needs an identity premise and what a wrong merge or split would change.
2. **Fix entity grain and interval.** Name the relevant individual or occurrence kind, part-whole level, version/configuration, lifecycle state, jurisdiction or organization, and time/effectivity interval.
3. **Bind source endpoints.** Reference each `SIE.2` identifier scheme, issuer/owner, syntax, resolution behavior, restrictions, identified-entity claim, edition, and source provenance.
4. **Separate candidate relation kinds.** Consider same individual at the stated grain, different individuals, part/whole, earlier/later version or specialization, variant, alternate description, family membership, or unresolved. Do not use one boolean until the use truly needs only that distinction.
5. **Collect discriminating evidence.** Use issuer records, source assertions, configuration/effectivity, provenance, physical or domain characteristics, event histories, and counterexamples. A shared string or co-occurrence is only candidate evidence.
6. **Recover authority.** Name who may decide scheme-local identity, master identity, authoritative values, or the domain relation. SIE may record and use a bounded disposition; it does not acquire those authorities.
7. **Assign the narrowest warranted disposition.** State conditions, confidence or uncertainty where meaningful, rejected alternatives, and unresolved evidence. Preserve source IDs even for accepted same-entity rows.
8. **Propagate the premise explicitly.** Reference the disposition from every mapping, claim composition, interface row, and identity test that relies on it. Never copy only the merged key.
9. **Test difficult cases and reopen.** Include identifier reuse, split/merge, version/configuration change, part-whole confusion, contradictory source events, and absent-link cases. State the source or observation change that reopens the row.

#### SIE.5:4.2 - Record the Result

| Identity position | Required content |
| --- | --- |
| identity question and use | receiver, dependent action, wrong-merge/wrong-split consequence |
| entity boundary | kind and grain, part-whole level, version/configuration, interval/effectivity, relevant context |
| source identifiers | scheme, identifier, issuer/owner, syntax/resolution/restrictions, source edition and provenance |
| candidate relations | same, different, part, version/specialization, variant, alternate description, family, unresolved alternatives |
| warrant | evidence, counterevidence, counterexamples, uncertainty/confidence, rejected alternatives |
| authority | scheme-local, master-data, domain, and receiving-decision scopes |
| disposition | narrowest warranted relation or unresolved result, conditions, source-ID preservation rule |
| downstream and reopen | mapping/composition/interface/test references and exact change or observation that reopens |

#### SIE.5:4.3 - What Changes in Practice

The integration stops minting a common key as proof of identity. Every load-bearing join points to a disposition with grain, interval, source identifiers, evidence, and authority. Unresolved identity becomes an explicit interface and validation branch instead of a row silently dropped or merged.

### SIE.5:5 - Archetypal Grounding - Semiconductor Recall Trace

A recall-triage query crosses a wafer identifier from a fabrication source, die coordinates, device serials, package identifiers, supplier lot identifiers, GS1 event identifiers, and an enterprise material master. The receiving question is whether a shipped device can be traced to an affected fabrication lot.

| Endpoint question | Constructed disposition |
| --- | --- |
| wafer `W-204` and supplier lot `L-88` | not identity; the supplier record asserts that the wafer is a member/output associated with the lot under a bounded process interval. Preserve both identifiers and relation provenance. |
| die coordinate `(x17,y9)` on wafer `W-204` and device serial `D-771` | same physical die/device at the selected post-singulation grain only when the packaging event and issuer records connect them; accepted with interval and event evidence. |
| device serial `D-771` and package code `P-55` | unresolved because the package identifier is reused after rework and the event history lacks effectivity. Stop the dependent trace branch. |
| enterprise material master `M-12` and device serial `D-771` | family/type membership, not individual identity. The master describes a material/product class and authoritative enterprise attributes within its stewardship scope. |
| GS1 event `E-901` and device `D-771` | event and object are different entities; the event may concern the device. Never merge their identifiers. |

Tests cover reused package identifiers, a die split/merge error, contradictory supplier events, a missing cross-enterprise link, and a later correction. The interface returns supported trace segments and the unresolved `P-55` branch. MDM or the domain steward may later decide a master identity; SIE.5 has not done so.

### SIE.5:6 - Bias-Annotation

| Lens | Likely drift | Repair |
| --- | --- | --- |
| Governance | The integration registry becomes the de facto master-data authority. | State the bounded disposition and retain MDM/domain decision ownership. |
| Architecture | One canonical key is required because the platform prefers it. | Carry a surrogate technical key only with source IDs and the identity disposition it indexes. |
| Ontology/Epistemology | Same individual, part, version, variant, alternate, and family relations collapse. | Fix grain and interval, then choose the narrowest warranted relation. |
| Pragmatics | Every identifier pair receives a costly adjudication. | Decide only pairs that are load-bearing for the receiving use; leave independent rows untouched. |
| Didactics | “Same” is read as timeless universal identity. | Display conditions, interval/effectivity, scheme, and forbidden reuse beside the disposition. |

### SIE.5:7 - Conformance Checklist

- [ ] The receiving action and wrong-merge/wrong-split consequence are named.
- [ ] Entity kind, grain, part-whole level, version/configuration, and interval/effectivity are explicit.
- [ ] Every identifier retains its scheme, issuer/owner, restrictions, source edition, and provenance.
- [ ] Useful non-identity relations are not compressed into a boolean same/different field.
- [ ] Shared strings, co-occurrence, and crosswalk membership are treated only as candidate evidence.
- [ ] Evidence, counterevidence, counterexamples, and uncertainty are inspectable.
- [ ] Scheme-local, master-data, domain, and receiving-decision authority scopes remain separate.
- [ ] Accepted same-entity rows do not delete source identifiers.
- [ ] Every dependent mapping, composition, interface, and test references the disposition.
- [ ] Reuse, split/merge, version/configuration, part-whole, contradiction, and absent-link cases are tested where applicable.

### SIE.5:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Same string, same entity | Add scheme, issuer, grain, interval, and discriminating evidence. |
| Universal `sameAs` | Use the narrowest relation and record unresolved or different cases. |
| Master key by integration fiat | Return master-identity and survivorship decisions to their authority. |
| Version equals object | State whether the use concerns one continuing entity, a version-specific configuration, or a relation among them. |
| Part joined as whole | Fix the entity grain and preserve part-whole relations explicitly. |
| Drop unresolved rows | Expose them as interface and validation branches with dependent actions. |

### SIE.5:9 - Consequences

The package can join warranted identities without losing source trace and can stop only the branches that depend on unresolved identity. Corrective source or steward decisions can be replayed against explicit consumers. The method also reveals when the useful relation is part, version, membership, or event participation rather than identity.

The cost is domain evidence and authority work. Some convenient global keys remain technical indexes rather than semantic truths, and some desired traces return incomplete.

### SIE.5:10 - Rationale

Identifiers are governed signs, not entities. Cross-source identity is therefore a relation claim that depends on scheme, grain, interval, evidence, and use. Preserving source identifiers and authority makes the claim reversible and prevents integration convenience from becoming a master-data or domain decision.

### SIE.5:11 - SoTA-Echoing

The best-known line combines explicit identifier ownership and restrictions, provenance-qualified alternate/specialization relations, and domain traceability practice. The serious default is entity resolution that optimizes a match score or golden record. Its defect is not probabilistic matching itself; it is allowing the score or merged record to erase grain, issuer, interval, and decision authority. SIE.5 mutates the line into a bounded disposition consumed explicitly by downstream semantic results.

| Source line | Adopt, adapt, or reject | Role and limit |
| --- | --- | --- |
| Current FPF identity and relation law | adopt | Keeps identity and direct relations as explicit claims; generic law does not decide a domain pair. |
| [ISO 8000-115:2024](https://www.iso.org/standard/88847.html?browse=tc) | adapt | Contributes identifier owner, use restriction, semantics, and resolution inputs; excludes identifier creation, query/response syntax, and resolution method and does not decide equivalence. |
| [PROV-O](https://www.w3.org/TR/prov-o/) | adapt | Supplies specialization, alternates, derivation, attribution, revision, and invalidation relations useful to evidence; provenance relations are not blanket identity. |
| [SEMI traceability standards](https://www.semi.org/en/products-services/standards/traceability) and [GS1 EPCIS 2.0.1](https://ref.gs1.org/standards/epcis/2.0.1/) | adapt | Supply semiconductor and event-based identity/traceability probes; scheme use does not create enterprise master identity or authorize recall. |
| golden-record or score-only merging | reject as sufficient | It may support candidate generation or a steward decision but cannot erase source identifiers, relation kinds, and authority. |

Reopen when an identifier scheme or issuer rule changes, new event/configuration evidence changes the disposition, the required grain or interval changes, or repeated cases show that the disposition vocabulary cannot preserve an action-changing relation.

### SIE.5:12 - Relations

- `SIE.1` supplies the receiving action, identity-sensitive answer claims, loss boundary, tests, and stop.
- `SIE.2` supplies identifier schemes, issuers, restrictions, source claims, editions, provenance, and authority gaps.
- `SIE.4` may expose an identity question but does not answer it merely by accepting a semantic correspondence.
- `SIE.6` consumes identity dispositions when composing claims about the same bounded entity; it preserves contradictory claims separately.
- `SIE.7` and `SIE.9` reference dispositions rather than copying only merged keys.
- `SIE.10` tests every load-bearing identity premise. MDM and domain authorities retain master identity, authoritative values, and action.

### SIE.5:End

## SIE.6 - Fuse Source-Qualified Claims without Erasing Conflict

> **Type:** Method pattern
> **Status:** Eternal alpha
> **Normativity:** Normative method guidance within SIE; examples are constructed and non-normative.
>
> **Primary working result:** a `SourceQualifiedClaimFusion@Use` that preserves each source claim, subject and any relied-on identity premise, scope, interval, authority, uncertainty, derivation, and relation to other claims, then returns a qualified view, explicit conflict, non-comparability, or unresolved result for one receiving use.

### SIE.6:1 - Problem Frame

**Use this when** a receiving answer must combine claims from separately governed sources and a simple union, priority rule, average, overwrite, or “golden record” would hide differences in meaning, subject, time, authority, or uncertainty. The recognizable failure is one clean value whose provenance can be displayed but whose conflict or non-comparability can no longer be recovered.

The primary EntityOfConcern is one source-qualified claim composition for a named receiving question. The first move is to state the exact source claims and the subject relation the receiving question requires. The first result is either a qualified view with explicit derivation or an honest conflict, non-comparability, or unresolved branch.

The payoff is an answer the receiver can interpret without pretending that integration owns truth or preference. Do not use SIE.6 to decide domain truth, authoritative value, survivorship, risk acceptance, or action. A domain authority or receiving decision may consume the composition and choose; SIE preserves what that choice depends on.

### SIE.6:2 - Problem

Claims that share a field name can concern different concepts, entities, grains, intervals, or authority scopes. Claims that do concern the same entity can disagree without either being malformed. A timestamp does not settle whether one claim supersedes another; a source rank does not explain why the rank applies; and an average can be meaningless across different measurement definitions.

If composition silently collapses these differences, later validation can test only the fused value. It cannot test the losing claim, the identity premise, the conflict rule, or the receiver's permitted use. Provenance survives as a list of sources but no longer constrains meaning.

### SIE.6:3 - Forces

| Force | Tension |
| --- | --- |
| Simplicity | Receivers prefer one view, while a truthful answer may need several qualified rows or an explicit conflict. |
| Authority | Some sources are authoritative for bounded claims, while no source may own the whole receiving question. |
| Time | Newer claims may supersede older ones, while differing intervals, effectivity, or observation times can make them jointly informative. |
| Identity | Composition needs a subject relation, while an unresolved identity premise must stop only the dependent branch. |
| Uncertainty | Quantification can support comparison, while unlike confidence, status, or evidence forms should not be normalized without warrant. |
| Performance | Precomputed canonical values are convenient, while preserving source-qualified alternatives and derivation costs storage and query work. |

### SIE.6:4 - Solution

Compose claims only after their meanings, subjects, scopes, intervals, authority, uncertainty, and provenance are explicit. Classify the relation among claims before applying a rule. Preserve the source claims and any relied-on identity premises in the result. Return a qualified view only under a stated rule and use boundary; otherwise return conflict, non-comparability, or unresolved.

#### SIE.6:4.1 - Pattern-Use Unfolding

1. **Name the receiving question and action.** State what the composed answer may change and which outcomes are acceptable: one qualified row, several rows, conflict, non-comparability, unresolved, or stop.
2. **Bind exact source claims.** Reference `SIE.2` rows and `SIE.4` correspondences. Record each proposition or data-derived claim, scope, interval/effectivity, units, status, uncertainty, derivation, source, and authority.
3. **Bind the subject relation needed by the use.** Reference `SIE.5` when composition depends on claims concerning the same entity. For separately attributed claims about clearly distinct subjects, preserve their subjects and attribution. Keep an explanation of unused identity only when it affects interpretation or later reliance. A correspondence alone does not establish subject identity.
4. **Test comparability.** Decide whether claims use compatible concepts, subjects, grains, units, intervals, and observation/decision roles. Preserve non-comparability as a result.
5. **Classify the claim relation.** Distinguish compatible conjunction, refinement, overlap, duplication, supersession under a justified rule, contradiction, non-comparability, and unresolved relation.
6. **Choose a bounded composition rule.** Examples include retaining all qualified claims, selecting one claim under an explicit domain authority/effectivity rule, deriving a new claim through a stated calculation, or returning conflict. State rejected alternatives and semantic loss.
7. **Construct the qualified output.** Include the source claims or stable references, applied rule, any relied-on identity premise, derived value if any, provenance/trace, authority boundary, uncertainty, conflict/non-comparability status, and permitted receiving use.
8. **Expose failure and challenge.** Define missing-source, stale-source, unresolved-identity, incompatible-unit, contradictory-authority, and unsupported-default branches. Do not convert them into null or a chosen value without the contract's permission.
9. **State downstream and reopen conditions.** Identify mappings and interfaces that consume the composition and the source, identity, rule, authority, or use change that reopens it.

#### SIE.6:4.2 - Record the Result

| Composition position | Required content |
| --- | --- |
| receiving use | question, action changed, acceptable output branches |
| source claims | exact propositions/data claims, meanings, subjects, scopes, intervals/effectivity, units, status, uncertainty, source and derivation |
| identity premise | referenced `SIE.5` disposition when composition relies on identity; an explanation of unused identity only when it affects interpretation or later reliance |
| comparability | compatible dimensions and any difference that prevents comparison |
| claim relation | conjunction, refinement, overlap, duplicate, qualified supersession, contradiction, non-comparability, unresolved |
| composition rule | rule, authority/evidence basis, conditions, rejected alternatives, semantic loss |
| output | qualified view or explicit conflict/non-comparability/unresolved result, provenance/trace, permitted use |
| downstream and reopen | mapping/interface references, failure branches, exact changes that reopen |

#### SIE.6:4.3 - What Changes in Practice

The team stops treating a canonical value as the natural output of integration. A receiver can see why claims were combined, retained separately, or stopped, and can return to the exact source, identity, authority, or rule that changes the answer.

### SIE.6:5 - Archetypal Grounding - Provider Availability Claims

Two providers expose availability for the same buyer-recognized product family. Provider A returns `onHand = 12` at 10:00; Provider B returns `availableToPromise = 9` at 10:02. A purchasing integration initially proposes a single `available = 21` value.

The source inventory shows that `on hand` is current physical stock before reservations, while `available to promise` is a provider-governed commitment quantity after its own reservation and horizon rules. The values are not additive and are not globally equivalent. A product-family correspondence exists, but individual inventory objects are not asserted identical.

| Claim relation question | Constructed result |
| --- | --- |
| Can the two values be summed? | non-comparable for summation because definitions, allocation rules, and authority scopes differ |
| Can both support a “which provider can satisfy quantity 8 now?” query? | conditionally comparable only after the contract accepts Provider A's additional reservation check and Provider B's promise horizon; retain separate rows |
| What if Provider A reports 12 and a later status reports 4? | classify by source occurrence, observation interval, and justified supersession rule; retain both claims and derivation rather than overwriting silently |
| What if product identity is unresolved? | stop that product branch and expose the unresolved `SIE.5` premise |
| What if one API times out? | return available source-qualified rows plus an incomplete-result flag if the contract permits; never substitute zero |

The interface can return two qualified provider rows, explicit non-comparability for arithmetic aggregation, and a missing-source branch. Purchasing owns supplier choice and risk acceptance. SIE.6 supplies no canonical stock fact.

### SIE.6:6 - Bias-Annotation

| Lens | Likely drift | Repair |
| --- | --- | --- |
| Governance | A source priority table silently decides truth or business action. | Name the authority and exact claim scope for every selection or supersession rule. |
| Architecture | The target schema requires one value and erases alternatives. | Change the output shape or expose conflict/non-comparability as first-class branches. |
| Ontology/Epistemology | Data values, claims, facts, and decisions collapse. | Record propositions, scope, uncertainty, derivation, and receiver decision separately. |
| Pragmatics | Every disagreement becomes an elaborate dispute. | Classify only relations that can change the receiving answer; retain independent claims without forced comparison. |
| Didactics | “Fusion” is read as merge or averaging. | Show examples where the correct fusion is a qualified set, conflict, or non-comparability. |

### SIE.6:7 - Conformance Checklist

- [ ] The receiving question and every allowed output branch are explicit.
- [ ] Source claims retain meaning, subject, scope, interval/effectivity, units, status, uncertainty, source, and derivation.
- [ ] Every load-bearing subject identity premise is referenced and tested.
- [ ] Comparability is judged before aggregation or selection.
- [ ] Compatible, refining, overlapping, duplicate, superseding, contradictory, non-comparable, and unresolved relations are distinguishable.
- [ ] A composition rule states its authority/evidence basis, conditions, rejected alternatives, and loss.
- [ ] Source claims remain recoverable from the output.
- [ ] Missing, stale, unresolved-identity, incompatible-unit, contradictory-authority, and default branches are explicit where applicable.
- [ ] The result does not claim domain truth, authoritative value, preference, authorization, or action beyond its source and receiver boundaries.

### SIE.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Last write wins | State why time establishes supersession for this claim and interval; otherwise retain both. |
| Trusted source always wins | Name the source's exact authority scope and preserve losing claims and conflict. |
| Average the values | Establish compatible meaning, subject, unit, interval, and aggregation semantics first. |
| Null means zero or absent | Preserve missing, unavailable, unknown, not applicable, and zero as distinct branches. |
| Provenance after fusion | Keep source claims and derivation as inputs to the composition, not decoration on the result. |
| One canonical fact | Return a qualified view only when the use and authority rule warrant it; otherwise return plural claims or conflict. |

### SIE.6:9 - Consequences

Receivers obtain explainable views and honest conflict branches. Corrections can target the source claim, identity premise, composition rule, or receiving use without reconstructing an opaque golden record. Different receivers may lawfully obtain different bounded views from the same preserved claims.

The cost is richer output and explicit rule ownership. Some applications must handle plural, incomplete, or conflicting results instead of one scalar value.

### SIE.6:10 - Rationale

Claims are source- and scope-bearing assertions, not free-floating values. Composition is therefore a new derivation whose premises and authority must remain inspectable. Preserving the inputs is what makes conflict, correction, and changed-use replay possible.

### SIE.6:11 - SoTA-Echoing

The best-known line combines claim individuation, provenance, authority-aware data integration, and explicit uncertainty. The serious default is master-record survivorship or source ranking. Those Methods can be valid under an authorized MDM use, but they are defective as a universal semantic-integration default because they hide non-comparability and transfer authority. SIE.6 adapts the line by making the qualified composition or explicit conflict the domain result.

| Source line | Adopt, adapt, or reject | Role and limit |
| --- | --- | --- |
| Current FPF `C.2.1` | adopt | Keeps claims as distinct representational objects; SIE supplies the cross-source use composition. |
| Current FPF `A.10` | adopt | Governs claim-bound evidence and provenance reliance; evidence law does not choose the domain truth or action. |
| [PROV-O](https://www.w3.org/TR/prov-o/) | adapt | Supports derivation, attribution, revision, and invalidation traces; provenance alone establishes no truth, priority, or comparability. |
| MDM survivorship and golden-record practice | adapt only under direct authority | May supply an authoritative-value result for a bounded domain; SIE preserves its source and scope rather than generalizing it. |
| last-write, average, or global source-rank defaults | reject as universal | Each may be a justified local rule, but none is semantically safe without compatible claims and authority. |

Reopen when a source claim, identity premise, authority rule, interval, uncertainty model, or receiving use changes, or when representative conflict cases cannot be expressed without hiding action-changing information.

### SIE.6:12 - Relations

- `SIE.2` supplies source claims, meanings, editions, authority, provenance, currentness, and gaps.
- `SIE.4` supplies the qualified correspondences needed to compare claim predicates or values.
- `SIE.5` supplies load-bearing subject identity dispositions; claim conflict does not alter those identities by itself.
- `SIE.7` may implement the qualified composition rule but must preserve its branches and trace.
- `SIE.9` exposes qualified views, plural claims, conflict, non-comparability, and incomplete-source states to the receiver.
- `SIE.10` tests the composition rule and negative branches. MDM, domain, and application owners retain truth, value, preference, authorization, and action.

### SIE.6:End

## SIE.7 - Specify Semantic Extraction and Transformation Mappings

> **Type:** Method pattern
> **Status:** Eternal alpha
> **Normativity:** Normative method guidance within SIE; examples are constructed and non-normative.
>
> **Primary working result:** an `ExecutableSemanticMappingSpecification@Use` that states source and target schemes, accepted correspondence, identity, and claim-composition premises, extraction and transformation rules, selection and cardinality, units and codes, conditions, defaults, errors, information loss, trace, examples, and tests.

### SIE.7:1 - Problem Frame

**Use this when** accepted semantic correspondences must become repeatable extraction or transformation behavior, or existing code contains joins, conversions, defaults, and exclusions that cannot be traced to their semantic premises. The recognizable failure is a pipeline that runs successfully while changing meanings, merging unresolved identities, dropping conflicts, or inventing values through defaults.

The primary EntityOfConcern is one executable semantic rule set for a named use, independent of the physical pipeline that may enact it. The first move is to bind each output claim to accepted input senses and relation, identity, or composition results. The first result is a mapping specification precise enough to implement and test without reopening its semantic choices in code.

The payoff is a clean handoff to Data Engineering or another implementer and a traceable object for validation. Do not use SIE.7 to choose virtual versus materialized realization, build or operate the pipeline, or authorize access. A correspondence set is an input, not executable behavior; a running transform is evidence, not the specification itself.

### SIE.7:2 - Problem

Mapping logic is often dispersed across SQL, ETL configuration, model transformations, lookup tables, API adapters, and undocumented operator knowledge. The same “mapping” word then refers to a semantic relation, an extraction query, a unit conversion, a data movement, and the Work that ran it.

When these objects collapse, semantic review happens after implementation and cannot identify what was intended. Defaults conceal missing inputs, many-to-one mappings drop distinctions, identifiers are normalized without issuer context, and error rows vanish. A code diff reveals mechanics but not the receiving-use claim it is allowed to produce.

### SIE.7:3 - Forces

| Force | Tension |
| --- | --- |
| Executability | Rules must be precise enough to run, while binding them to one technology can hide their semantic intent. |
| Completeness | Every output branch needs behavior, while invented defaults make an incomplete rule appear total. |
| Performance | Efficient joins and precomputation matter, while optimization must preserve semantic premises and trace. |
| Cardinality | Source and target structures differ, while one-to-many and many-to-one choices can create loss or duplication. |
| Error handling | Operational systems prefer a value or null, while semantic failure needs distinct unresolved, incompatible, stale, and source-error branches. |
| Change | Stable rule identifiers aid maintenance, while source editions and accepted correspondences can invalidate a rule. |

### SIE.7:4 - Solution

Specify semantic mapping rules separately from their implementation. Bind every rule to a receiving-use contract, exact source and target schemes, and accepted correspondence, identity, and claim-composition premises. Make selection, cardinality, conversions, defaults, errors, loss, trace, and tests explicit. Require implementations to preserve these behaviors or return a named discrepancy.

#### SIE.7:4.1 - Pattern-Use Unfolding

1. **Name the output claim and receiver.** State the target field or proposition, its meaning, grain, interval/effectivity, and the action it supports.
2. **Bind source and target schemes.** Reference exact `SIE.2` source rows and target interface/model definitions, editions, profiles, units, codes, identifiers, and access assumptions.
3. **Bind semantic premises.** Reference accepted `SIE.4` correspondence rows, every load-bearing `SIE.5` identity disposition, and the `SIE.6` composition or conflict branch. Stop on an unresolved required premise.
4. **Specify selection and extraction.** State source records, predicates, joins, windows, configuration/effectivity filters, ordering, and behavior for missing or duplicate inputs.
5. **Specify transformation.** State direction, construction, decomposition, aggregation, unit/code conversion, normalization, derivation, and required external lookup. Name the authority for any conversion or code table.
6. **Specify cardinality and identity preservation.** State one-to-one, one-to-many, many-to-one, or conditional behavior; keep source identifiers and disposition references when rows combine or split.
7. **Specify defaults and errors.** Distinguish absent, unknown, not applicable, inaccessible, stale, incompatible, unresolved, source failure, and actual zero or empty value. Permit a default only when the contract and semantic warrant state its meaning and loss.
8. **State information loss and forbidden reuse.** Name omitted distinctions, coarsening, precision, interval, provenance, or conflict and the use for which the loss is accepted.
9. **Provide trace and examples.** Give stable rule identifiers, input-to-output trace positions, positive examples, boundary and counterexamples, and expected negative branches.
10. **Define implementation conformance and reopen.** State observable behavior an implementation must match and source, premise, contract, or target changes that invalidate the rule.

#### SIE.7:4.2 - Record the Result

| Mapping position | Required content |
| --- | --- |
| rule and use | stable rule identifier, receiver, output claim, grain, interval/effectivity |
| schemes | source/target assets, models/schemas, editions/profiles, fields/types/relations, units/codes |
| semantic inputs | correspondence rows, identity dispositions, composition/conflict result and their conditions |
| extraction | selection, joins, filters, windows, effectivity, duplicates, missing-input behavior |
| transformation | direction, construction/decomposition/aggregation, conversions, lookups, derivation |
| cardinality and identifiers | source-target multiplicity, split/merge behavior, source-ID and premise preservation |
| defaults and errors | distinguished states, permitted default and meaning, failure branches, quarantine or stop |
| loss and trace | accepted/forbidden loss, provenance, rule and premise references, input-output trace |
| examples and conformance | positive, boundary, negative/unlike examples, expected outputs, implementation predicate, reopen |

#### SIE.7:4.3 - What Changes in Practice

Semantic decisions leave code and configuration comments and become an independently reviewable specification. Data Engineering can optimize or replace an implementation while preserving the mapping behavior, and a failed output can be traced to a source premise, rule, implementation discrepancy, or receiving-use change.

### SIE.7:5 - Archetypal Grounding - AP242/QIF Mapping Rules

The AP242/QIF package needs a row set for the configuration-bound inspection query. Its specification includes these constructed rules:

| Rule | Semantic and executable behavior |
| --- | --- |
| `MAP-SIE-APQ-01` | Select the released AP242 product-definition revision/configuration supplied by Systems Engineering and filter features by effectivity `E`. Do not select “latest” as a substitute. |
| `MAP-SIE-APQ-02` | For each accepted `SIE.4` plan-characteristic-concerns-feature row, join exact source identifiers only under the referenced `SIE.5` feature disposition. Preserve AP242 and QIF IDs and issuers. |
| `MAP-SIE-APQ-03` | Compose AP242 definition/effectivity and QIF plan/result claims through the referenced `SIE.6` result. Emit compatible qualified claims, explicit contradiction, non-comparability, or unresolved branches; never overwrite. |
| `MAP-SIE-APQ-04` | Convert units only through the contract-approved code/unit table and retain original value, unit, conversion rule, precision, and loss. An unknown unit stops that result row. |
| `MAP-SIE-APQ-05` | Return unmatched AP242 feature, unmatched QIF characteristic, stale result, missing provenance, and source-error states distinctly. No state defaults to an accepted match. |

Positive examples cover one known configuration/feature/characteristic/result chain. Boundary cases cover one-to-many characteristics and repeated results. Negative cases cover an obsolete revision, incompatible feature, unresolved identity, unknown unit, contradictory result status, and absent QIF plan. A SQL view, R2RML mapping, QVT transformation, or application code may implement the rules; none changes the specification without reopening the affected rule.

### SIE.7:6 - Bias-Annotation

| Lens | Likely drift | Repair |
| --- | --- | --- |
| Governance | Mapping code silently decides source priority, identity, or authoritative value. | Require references to accepted premises and the direct authority for conversions or defaults. |
| Architecture | A tool's expressiveness defines the semantic rule. | State implementation-independent behavior and return an implementation gap when the tool cannot preserve it. |
| Ontology/Epistemology | Correspondence truth, transformation rule, performed transformation, and output claim collapse. | Keep the rule and its evidence separate from execution occurrences and resulting claims. |
| Pragmatics | The specification reproduces every implementation detail. | Include only behavior needed to preserve semantics, errors, trace, and conformance. |
| Didactics | Examples are copied as the complete rule. | State the general condition and use examples as tests, including counterexamples. |

### SIE.7:7 - Conformance Checklist

- [ ] Every rule names a receiving output claim and use.
- [ ] Source and target schemes, editions/profiles, meanings, units, codes, and identifiers are exact.
- [ ] Accepted correspondence, identity, and composition premises are referenced rather than re-decided in code.
- [ ] Selection, joins, filters, windows, effectivity, duplicates, and missing inputs are explicit.
- [ ] Transformations, conversions, external lookups, and their authority are explicit.
- [ ] Cardinality, split/merge behavior, and source-identifier preservation are specified.
- [ ] Absent, unknown, not applicable, inaccessible, stale, incompatible, unresolved, source failure, zero, and empty values remain distinguishable where relevant.
- [ ] Defaults have a semantic warrant, accepted loss, and test.
- [ ] Information loss, forbidden reuse, provenance, and input-output trace are inspectable.
- [ ] Positive, boundary, negative, and unlike cases define observable implementation conformance.
- [ ] The specification claims no running pipeline, service level, or receiving-use validation.

### SIE.7:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| SQL is the mapping | Extract the semantic rule, premises, loss, errors, and tests; treat SQL as one implementation. |
| Crosswalk equals transformation | Add selection, direction, cardinality, conversions, defaults, errors, trace, and examples. |
| Null for every failure | Define distinct semantic and operational states and their receiver behavior. |
| Latest record wins | Use the direct configuration/effectivity or justified interval rule. |
| Normalize identifiers | Preserve scheme and issuer and reference the identity disposition. |
| Hidden unit conversion | Record source/target units, authority, precision, loss, and counterexample tests. |

### SIE.7:9 - Consequences

Implementers receive a bounded contract that can survive technology change, and reviewers can distinguish a semantic defect from an implementation defect. Negative branches and accepted loss become testable, and optimization can proceed under a preservation predicate.

The cost is explicit rule and example work before or alongside coding. Some tools cannot represent the required branches or trace and must be wrapped, changed, or rejected for this use.

### SIE.7:10 - Rationale

A semantic correspondence states a relation; an executable mapping states how source occurrences produce target claims under conditions. Making that extra structure explicit prevents implementation convenience from becoming a semantic decision and lets Data Engineering own execution without inheriting unstated SIE authority.

### SIE.7:11 - SoTA-Echoing

The best-known line combines declarative mapping languages, model transformation, traceability, and representation-preservation checks. The serious default is code-first ETL. Code is necessary in many realizations, but as the sole specification it hides semantic premises and loss. SIE.7 adapts the line into a technology-independent, receiving-use mapping contract with explicit negative states.

| Source line | Adopt, adapt, or reject | Role and limit |
| --- | --- | --- |
| Current FPF `A.6.3.RT` | adopt | Governs preservation through representation transition; it does not specify this domain mapping. |
| [R2RML](https://www.w3.org/TR/r2rml/) | adapt | Demonstrates declarative relational-to-RDF mapping structures; RDF and relational sources are optional technology families. |
| [OMG QVT 1.3](https://www.omg.org/spec/QVT/) | adapt | Contributes model-query/view/transformation and trace forms; MOF/QVT is not mandatory. |
| [PROV-O](https://www.w3.org/TR/prov-o/) | adapt | Supports derivation and activity/agent/entity trace; provenance does not prove semantic preservation. |
| code-first ETL as sole contract | reject as sufficient | Execution can be tested only against an independently recoverable rule, loss, and branch contract. |

Reopen when an input or target scheme changes, a correspondence/identity/composition premise changes, a counterexample defeats the rule, the receiver changes accepted loss, or implementations cannot satisfy the preservation predicate.

### SIE.7:12 - Relations

- `SIE.1` supplies the output claims, accepted loss, service conditions, tests, and stop.
- `SIE.2` supplies exact source and target semantics, editions, identifiers, units/codes, provenance, and gaps.
- `SIE.4`, `SIE.5`, and `SIE.6` supply the semantic premises the rules reference.
- `SIE.8` consumes rule behavior and implementation conditions to compare realization alternatives.
- `SIE.9` exposes the rule outputs and error branches to the receiver.
- `SIE.10` tests both specification semantics and implementation conformance. Data Engineering owns pipeline construction, operation, observability, reliability, and recovery.

### SIE.7:End

## SIE.8 - Choose Virtual, Materialized, or Hybrid Semantic Realization

> **Type:** Method pattern
> **Status:** Eternal alpha
> **Normativity:** Normative method guidance within SIE; examples are constructed and non-normative.
>
> **Primary working result:** a `SemanticRealizationDecision@Use`: a supported choice, sufficient rejection, worthwhile probe, or missing-input result for a named semantic-integration use. A positive choice identifies the implementation results it still requires.

### SIE.8:1 - Problem Frame

**Use this when** accepted semantic mappings exist and the current question is whether to evaluate them at query time, persist integrated results, or combine both. Enter also when a graph database, warehouse, federation, cache, search index, API composition, or “virtual knowledge graph” has already been proposed and its semantic consequences need comparison.

The primary EntityOfConcern is one realization decision for a named semantic-integration use. The first move is to derive realization-sensitive criteria from the use contract and mapping specification. The first result is a bounded choice, probe, rejection, or missing-input return that leaves physical implementation and operation with their owners.

The payoff is a realization selected because it preserves the required meanings and service conditions, not because one carrier is fashionable or already available. Do not use SIE.8 to build, deploy, or operate a data service, select a whole enterprise platform, authorize access, or prove that the interface works. Data Engineering, platform, security, provider, finance, and other direct owners supply those results.

### SIE.8:2 - Problem

Materialization can improve latency and independence from source availability but creates copied state, invalidation, custody, storage, and refresh obligations. Virtual access can preserve source currency and authority but inherits source latency, availability, access, and query-capability limits. A hybrid can isolate hot or stable subsets but adds coherence and branch complexity.

When the choice is made from technology labels, these consequences remain hidden until operation. A copied graph is described as semantic truth, a federation as automatically current, or a cache as harmless optimization. The same mapping semantics can yield different provenance, currentness, error, and recovery behavior in each realization.

### SIE.8:3 - Forces

| Force | Tension |
| --- | --- |
| Freshness | Virtual reads can observe current source state, while network and source delays can still make answers stale or inconsistent. |
| Latency | Materialization and caching can respond quickly, while refresh and invalidation may violate the use's time boundary. |
| Availability | Copies can survive source outages, while they can conceal that authority or access conditions changed. |
| Source authority | Querying the source keeps custody visible, while a receiver may need stable snapshots and reproducible answers. |
| Security and permission | Fewer copies reduce exposure, while live federation can broaden runtime credentials and cross-source disclosure. |
| Provenance and reproducibility | Materialized snapshots aid replay, while virtual results need captured queries, source versions, and occurrence metadata. |
| Operability and recovery | A simpler runtime can reduce failure modes, while hybrid arrangements add invalidation and coherence responsibilities. |
| Cost | Storage, compute, licenses, egress, support, and provider dependency trade differently across cases. |

### SIE.8:4 - Solution

First use decisive conditions to exclude arrangements that cannot serve the contract. Describe and compare the serious remaining alternatives as complete arrangements, including source access, rule execution, state/copy behavior, provenance, currentness, failure branches, security, operation, recovery, exit, and joint resource demand. Return a supported choice, sufficient rejection, worthwhile probe, or missing-input result for the named use.

#### SIE.8:4.1 - Pattern-Use Unfolding

1. **Fix the receiving result.** Reference the `SIE.1` answer, `SIE.7` rules, required source/identity/claim branches, and validation conditions that a successful candidate must preserve.
2. **Apply decisive exclusions.** A known source prohibition or other sufficient condition can defeat an arrangement. Record the condition and evidence needed for that conclusion and stop developing the excluded alternative. If no serious candidate remains, return the bounded rejection or the exact missing result.
3. **Describe a serious virtual alternative.** When query-time access remains a candidate, state source access, rule evaluation, pushdown or mediation, credentials, latency/availability behavior, provenance capture, and failure return.
4. **Describe a serious materialized alternative.** When copying remains a candidate, state copied or derived state, snapshot identity, refresh/invalidation, storage and custody, source deletion/correction behavior, provenance, recovery, and exit.
5. **Describe a hybrid where warranted.** Identify which permitted subset is materialized and which source-sensitive part remains virtual. State coherence, invalidation, and fallback behavior. Confirm permission for each subset selected for copying.
6. **Compare complete remaining arrangements.** Use the conditions that can change the receiving result: freshness, latency, availability, access, protection, source authority, reproducibility, provenance, operability, recovery, cost, and semantic loss. Include concurrent source calls, shared credentials, trace, retries, support, and other demands within each applicable resource envelope. Pairwise feasibility cannot establish a jointly infeasible arrangement.
7. **Examine relevant failure and change cases.** Use the source outages, corrections, access changes, mapping changes, stale or partial refresh, provenance loss, and recovery cases needed for the proposed conclusion. Earlier sufficient evidence can support a bounded rejection; a positive selection needs its load-bearing conditions.
8. **Choose or identify worthwhile further work.** Select a supported arrangement, reject it, or return the missing result. Commission a discriminating probe only when its obtainable result can change the decision enough to justify its full burden and displaced work. Keep an unresolved comparison explicit when further inquiry is unavailable or not worthwhile. State the reasons for the disposition that its receiver needs.
9. **Name implementation returns for a selected choice.** Identify the Data Engineering, platform, provider, security, legal, finance, or operating results required to realize that choice.
10. **Return the conditions needed by this result.** For a selected realization or supplied receiving result, give `SIE.9` its service, error, currentness, and fallback meanings. Retain observations that can reopen the conclusion where they change continued reliance.

#### SIE.8:4.2 - Record the Result

The result follows the conclusion actually supplied. A sufficient rejection of one proposed arrangement is complete with the receiving use, named proposal, decisive grounds and evidence, scope, and material limits. It does not require a comparison with unrequested alternatives or an implementation and interface design. Unused positions create no empty fields, waivers, or explanations of omission.

| Decision content | When it is needed | Content supplied |
| --- | --- | --- |
| Receiving use and disposition | Every result | The question and proposed arrangement or comparison scope, supported choice/rejection/probe/missing-input result, grounds, and material limits. |
| Decisive exclusion | A proposed arrangement is rejected on sufficient grounds | The condition that defeats it, the evidence and applicability needed for that condition, and the scope of the rejection. |
| Candidate arrangements and comparison | A comparison remains live or a positive choice is made | Serious remaining alternatives as complete arrangements: required semantic branches, access, state, execution, currentness, latency, provenance, protection, failure, operation, recovery, exit, and joint resource demand. |
| Failure/change evidence | The supplied conclusion depends on it | Evidence for its load-bearing conditions. One qualified prohibition can suffice for rejection; positive selection needs the relevant failure and change cases for the claimed arrangement. |
| Further inquiry | A probe is proposed | Obtainability, possible decision contribution, full burden, displaced work, and how its result can change the decision. |
| Implementation returns | A realization has been selected | Exact required direct-owner results, what is supplied or still missing, and the acceptance evidence needed to realize that choice. |
| Interface semantics | A selected realization or receiving result needs them | Currentness, source/error, incomplete-result and fallback meanings supplied to SIE.9. |
| Continued reliance | A condition can materially change the result's use | The observation, source change, or receiving change that reopens the affected decision. |

A positive choice cannot use the rejection boundary to omit a condition on which that choice relies. The selected arrangement and its implementation returns remain qualified by all their actual semantic, service, access, and resource conditions.

#### SIE.8:4.3 - What Changes in Practice

The team compares ways to supply the same semantic result rather than comparing product categories. A graph store may survive as a materialized candidate, a federation as a virtual candidate, or neither. The selected decision states what still has to be implemented and operated before any service claim is made.

### SIE.8:5 - Archetypal Grounding - Provider Availability without Replication

Two providers expose current availability through governed APIs. Provider A means “on hand”; Provider B means “available to promise”. `SIE.4` preserves the semantic difference and `SIE.6` permits a qualified side-by-side answer but forbids arithmetic fusion. Neither provider permits replication of its availability state.

If the question is only whether a proposed copied availability store may serve that contract, the completed answer is: “Reject the proposed copied availability store for this purchasing use: the qualified provider conditions prohibit copying the required availability state.” The contract, proposal, and provider conditions identify its scope and grounds. This concludes that question without a latency study, credential design, recovery plan, or alternative selection.

When the receiving question also asks which remaining arrangement to use, continue with the following comparison:

| Candidate | Constructed comparison |
| --- | --- |
| materialized common graph | excluded by the providers' prohibition on copying availability state; that condition is sufficient without developing its implementation, recovery, and exit |
| query-time virtual mapping | retained alternative: preserves source custody and timestamps and can return provider-specific qualified rows; depends on runtime credentials, latency, provider availability, query limits, and explicit timeout/incomplete branches |
| hybrid metadata plus virtual values | selected conditionally: materialize stable product-family correspondences, mapping rules, and source metadata where their copying and maintenance are permitted; retrieve volatile availability values at query time; invalidate metadata when source definitions or product relations change |

The decision selects the hybrid arrangement because stable semantic premises can be inspected and volatile restricted values remain at their sources. It requires Data Engineering and security results for credential handling, concurrent calls, timeout behavior, observability, and recovery. SIE.9 receives separately attributed quantities and timestamps, provider errors, and the permitted incomplete-result and fallback behavior. No running interface or provider reliability is claimed.

### SIE.8:6 - Bias-Annotation

| Lens | Likely drift | Repair |
| --- | --- | --- |
| Governance | Materialization silently transfers custody, authority, or permission. | Record source rights, retention, correction, and use authority for every copied state. |
| Architecture | The incumbent platform determines the answer, or every conceivable alternative requires full design. | Use sufficient exclusions, then compare serious alternatives as complete arrangements on the receiving basis. |
| Ontology/Epistemology | A graph or warehouse is treated as the semantic arrangement itself. | Keep mapping premises, claims, provenance, and validation independent of carrier. |
| Pragmatics | Every unresolved comparison commissions a probe. | Compare obtainable decision benefit with the probe's full burden and displaced work. |
| Didactics | “Virtual is fresh; materialized is fast” becomes a universal rule. | Show source latency, snapshot reproducibility, invalidation, and failure conditions that reverse the slogan. |

### SIE.8:7 - Conformance Checklist

Check the conclusion being returned. Only its applicable checks need an answer; unused branches require neither a record nor an omission explanation.

**For every result**

- [ ] The receiving question, named proposal or comparison scope, disposition, grounds, and material limits are recoverable.
- [ ] The evidence supports that disposition at its stated scope; it creates no broader feasibility, running-service, or achieved-performance claim.

**For a sufficient rejection**

- [ ] The decisive condition and its qualified evidence defeat the named proposal for this use.

That rejection completes the Method when it answers the requested question. The following comparison and implementation checks do not become prerequisites for it.

**For a live comparison or positive selection**

- [ ] A successful candidate preserves the receiving result, mapping rules, and required semantic branches.
- [ ] Serious remaining candidates expose access, state, execution, provenance, failure, operation, recovery, exit, and joint resource demand.
- [ ] Freshness and latency are defined for the receiving use.
- [ ] Source authority, custody, permissions, correction/deletion, and retention consequences are explicit.
- [ ] Security/privacy and runtime credential differences are compared where they can change the result.
- [ ] Reproducibility and provenance behavior are specified for the candidate's virtual occurrences and copied state.
- [ ] Relevant outage, access, mapping, correction, refresh, provenance-loss, and recovery cases support the proposed conclusion.
- [ ] For a selected realization, exact implementation and operating results remain with their direct owners, and SIE.9 receives the required currentness, error, incomplete-result, and fallback meanings.

**For a proposed inquiry**

- [ ] Its obtainable decision contribution justifies the full burden and displaced work.

### SIE.8:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Knowledge graph” as the requirement | Restate the receiving result and compare graph and non-graph realizations. |
| Virtual means no state | Record mappings, caches, credentials, query occurrences, source snapshots, and provenance state actually required. |
| Materialized means reliable | Test refresh, invalidation, correction/deletion, recovery, and source-authority changes. |
| Hybrid means best of both | Expose coherence, invalidation, fallback, and doubled operating responsibilities. |
| Product feature checklist | Compare serious arrangements on use-sensitive criteria, joint resource demand, and relevant failure cases. |
| Decision equals implementation | Name the exact build, provider, security, and operating results still missing. |

### SIE.8:9 - Consequences

The realization becomes a reversible bounded decision with visible source, semantic, and operating trade-offs. Interface designers receive explicit currentness and error behavior, while implementers receive a clear invariant to preserve.

The cost is comparison beyond the preferred platform and coordination with operational owners. A selected candidate may still stop because access, security, service, provider, or cost evidence is missing.

### SIE.8:10 - Rationale

Virtual and materialized are not merely deployment choices: they change when and where mappings execute, which state is copied, how provenance and currentness are established, and which failures reach the receiver. Those changes can alter semantic adequacy, so SIE owns the bounded comparison while direct practices own implementation and operation.

### SIE.8:11 - SoTA-Echoing

The best-known line combines declarative mappings, virtual knowledge-graph systems, data federation, materialized integration, and operational data-product practice. The serious default alternatives are “materialize one canonical graph” and “federate everything live”. Each can be correct under conditions; each is defective as a universal answer because it hides a different set of currentness, access, provenance, and recovery obligations. SIE.8 mutates the line into a whole-arrangement choice around one semantic result.

| Source line | Adopt, adapt, or reject | Role and limit |
| --- | --- | --- |
| [Ontop virtual-KG line](https://ontop-vkg.org/research/publications.html) | adapt | Demonstrates query-time virtual realization over mappings; it does not make virtual RDF mandatory or supply source access and receiving acceptance. |
| [R2RML](https://www.w3.org/TR/r2rml/) | adapt | Supplies one declarative mapping form usable in virtual or materialized arrangements; relational/RDF technology is optional. |
| [Data on the Web Best Practices](https://www.w3.org/TR/dwbp/) | adapt | Contributes access, version, provenance, reuse, and persistence questions; Web publication is not required. |
| universal canonical graph | reject as default | Materialization is one candidate and cannot transfer source authority or erase incompatibility. |
| universal live federation | reject as default | Query-time access does not guarantee freshness, availability, permitted disclosure, or reproducibility. |

Reopen when source access or replication rights change, measured latency/availability defeats the use, refresh/invalidation fails, mapping or source semantics change, security/provenance conditions change, or a new candidate materially improves the comparison.

### SIE.8:12 - Relations

- `SIE.1` supplies the invariant result and use-sensitive service and protection conditions.
- `SIE.7` supplies executable semantic behavior and loss/error branches every candidate must preserve.
- `SIE.2`, `SIE.5`, and `SIE.6` supply source authority, identity, claim, provenance, and currentness conditions.
- `SIE.9` consumes the selected realization's currentness, latency, availability, provenance, error, access, and fallback semantics.
- `SIE.10` tests the realized candidate and receiving workflow; it can narrow or fail the decision's assumed conditions.
- Data Engineering, platform, provider, security, legal, finance, and Operations owners supply implementation and operating results.

### SIE.8:End

## SIE.9 - Connect a Receiving Use through a Semantic Interface

> **Type:** Method pattern
> **Status:** Eternal alpha
> **Normativity:** Normative method guidance within SIE; examples are constructed and non-normative.
>
> **Primary working result:** a `ReceivingSemanticInterface@Use` defining the smallest query, view, API, message, schema, report, or other boundary that carries the required meanings and branches to the receiver with interpretation, source and provenance, currentness, accepted loss, access assumptions, errors, unresolved returns, and a path back to the owning source or decision.

### SIE.9:1 - Problem Frame

**Use this when** semantic mappings or integrated state exist but the receiving Work still cannot obtain, interpret, challenge, or return the bounded result. Enter when a technically reachable endpoint hides source meanings, currentness, unmatched rows, conflicts, or the difference between “no value” and “source unavailable”.

The primary EntityOfConcern is one semantic interface between the maintained integration arrangement and a named receiving use. The first move is to restate the receiver's action and select the smallest interaction and result form that carries every load-bearing semantic branch. The first result is an interface contract and supplied candidate interface, not a claim that the receiver is authorized or that the service is operationally adequate.

The payoff is a boundary at which semantic meaning, failure, and provenance are usable by ordinary Work. Do not use SIE.9 to design the application's whole user experience, make its decision, operate the service, or accept engineering/quality results. Those owners consume the interface under their own Methods and authority. Stop rather than return a positive interface when a required semantic branch, interpretation, provenance/currentness condition, source-return path, or receiver-side use test cannot be represented or traced.

### SIE.9:2 - Problem

Integrated data can remain unusable because the receiver cannot ask the relevant question or distinguish the answer's conditions. An API may omit source edition and effectivity; a report may list a fused value without conflict; a schema may use one null for unknown, not applicable, stale, and timeout; a user may have no path to challenge an identity or mapping premise.

When the interface is treated as transport only, semantic obligations remain in internal documentation. The receiving Work either overtrusts the result or reconstructs meanings informally, creating a second uncontrolled integration at the boundary.

### SIE.9:3 - Forces

| Force | Tension |
| --- | --- |
| Minimality | A small interface is easier to use and maintain, while hiding source, loss, or failure makes it unsafe. |
| Human and machine use | Machines need stable schemas and branch codes; people need interpretations and challenge paths. |
| Abstraction | Receiver-friendly names reduce burden, while source identifiers and exact meanings must remain recoverable. |
| Performance | Rich provenance and alternative claims cost bandwidth and attention, while omitted trace defeats challenge and validation. |
| Security | The receiver needs enough source information to rely, while disclosure can violate provider, privacy, or protection conditions. |
| Evolution | Stable interface promises aid use, while source or mapping changes must not be hidden behind unchanged field names. |

### SIE.9:4 - Solution

Design the interface from receiving actions and semantic branches, not from the internal store. Expose the smallest result that preserves interpretation, source/version, currentness, accepted loss, identity and claim status, provenance, access assumptions, errors, unresolved returns, and source-return paths. Bind every field and branch to the use contract, mapping rules, and selected realization.

#### SIE.9:4.1 - Pattern-Use Unfolding

1. **Name the receiver interaction.** State who or what asks, the query/message/report action, timing, input parameters, and the next Work or decision that consumes the answer.
2. **Select the interface form.** Choose query, view, API, message, schema, report, file, or mixed human/machine form based on the receiving Work. Do not inherit the internal realization shape automatically.
3. **Define semantic inputs.** State required identifiers, schemes, configuration/effectivity, time windows, units, locale or code context, permissions, and validation of requests.
4. **Define result claims and interpretation.** For each output, state meaning, grain, scope, interval/effectivity, units/codes, source identifier behavior, accepted loss, and permitted use.
5. **Expose qualified branches.** Represent matched/qualified, unmatched, incompatible, unresolved identity, source-qualified conflict, non-comparability, stale, inaccessible, timeout/source error, and partial result where applicable.
6. **Expose provenance and currentness.** Provide source/edition or a stable reference, observation/retrieval time, mapping/composition rule version, derivation/trace reference, and freshness status needed by the receiver.
7. **State access, protection, and authority assumptions.** Explain what the interface verifies, what the caller supplies, what may be disclosed, and which actions remain unauthorized by the semantic result.
8. **Provide challenge and return paths.** A receiver must be able to identify the source, correspondence, identity, composition, mapping, or operational result that owns a defect or unresolved branch.
9. **Bind service behavior without claiming it.** State latency, availability, pagination/volume, ordering, idempotence or snapshot expectations only where semantic use depends on them; obtain implementation/operation evidence separately.
10. **Define conformance and reopen.** Give representative requests, responses, error branches, compatibility conditions, deprecation/change behavior, and observations that reopen the interface.

#### SIE.9:4.2 - Record the Result

| Interface position | Required content |
| --- | --- |
| receiver interaction | caller/reader, receiving Work, request, timing, next action |
| interface form | query/view/API/message/schema/report/file and why it fits the Work |
| request semantics | parameters, identifiers/schemes, configuration/effectivity, windows, units/codes, permissions |
| response semantics | claims, grain, scope, interval, units/codes, source IDs, accepted loss, permitted use |
| branch model | qualified, unmatched, incompatible, unresolved identity, conflict, non-comparable, stale, inaccessible, source error, partial |
| provenance/currentness | source/edition, times, rule versions, derivation/trace, freshness status |
| protection/authority | verified and assumed conditions, disclosure limits, action not authorized |
| challenge/return | stable path to source, semantic premise, mapping, implementation, or direct decision owner |
| service/conformance | action-sensitive service conditions, examples, errors, compatibility/deprecation, reopen |

#### SIE.9:4.3 - What Changes in Practice

The receiver no longer has to infer semantic meaning from field names or call the integration team to understand a missing row. Qualified, incompatible, conflicting, stale, and source-error states become part of the normal interface contract, and every challenge can be returned to a specific premise or owner.

### SIE.9:5 - Archetypal Grounding - AP242/QIF Review Interface

The quality engineer uses a view or API with request parameters `productDefinitionRevision`, `configuration`, `featureIdentifier`, and `effectivity`. The candidate response preserves these positions:

| Response position | Constructed behavior |
| --- | --- |
| `feature` | AP242 source identifier, issuer/profile, configuration/effectivity, source edition, and receiver-friendly label |
| `inspectionCharacteristic` | QIF source identifier, plan and characteristic meanings, source edition, and the accepted correspondence-row reference |
| `inspectionResult` | source-qualified QIF claim, observation time/status, unit and original value, provenance, and any conversion rule |
| `identityDisposition` | referenced `SIE.5` result and its grain/interval, not a copied boolean |
| `claimStatus` | qualified, conflict, non-comparable, or unresolved with the `SIE.6` composition reference |
| `freshness` | released AP242 configuration/effectivity used, QIF observation window, retrieval time, and stale status |
| `rowDisposition` | matched, unmatched-feature, unmatched-characteristic, incompatible, unresolved-identity, stale, source-error, or prohibited |
| `returnPath` | source record and mapping/correspondence/identity/composition rule references plus the direct engineering or quality owner for the decision |

A known match returns a qualified row. A feature absent at effectivity `E` returns unmatched rather than the nearest label. An unresolved identity returns that branch without claiming no inspection exists. A source timeout returns partial/incomplete only if the contract permits it. The interface does not accept the result or release the configuration.

### SIE.9:6 - Bias-Annotation

| Lens | Likely drift | Repair |
| --- | --- | --- |
| Governance | Interface access is mistaken for permission to act or disclose. | State verified/assumed permissions, disclosure limits, and the direct action authority. |
| Architecture | Internal graph or warehouse schema becomes the public contract. | Design from receiving actions and preserve realization independence where useful. |
| Ontology/Epistemology | Field name, status code, and claim meaning collapse. | Define every output and branch with scope, source, time, and permitted use. |
| Pragmatics | Full provenance overwhelms routine use. | Expose the action-changing summary and a stable trace path to detailed premises. |
| Didactics | Error branches look like exceptional implementation failures. | Teach unmatched, incompatible, conflict, and unresolved as normal semantic outcomes. |

### SIE.9:7 - Conformance Checklist

- [ ] The interface is tied to one named receiver, Work, request, and next action.
- [ ] The form is chosen for receiving use rather than copied from internal realization.
- [ ] Request identifiers, schemes, configuration/effectivity, windows, units/codes, and permissions are explicit.
- [ ] Response claims state meaning, grain, scope, interval, source identifiers, loss, and permitted use.
- [ ] Qualified, unmatched, incompatible, unresolved identity, conflict, non-comparability, stale, inaccessible, source-error, and partial branches remain distinguishable where applicable.
- [ ] Source/edition, observation/retrieval time, rule versions, derivation/trace, and freshness are recoverable.
- [ ] Protection, disclosure, and authority assumptions are explicit; the interface grants no unstated authorization.
- [ ] The receiver can return a defect or gap to a specific source, semantic premise, mapping, implementation, or decision owner.
- [ ] Action-sensitive latency, availability, snapshot, and volume behavior are stated without claiming unobserved performance.
- [ ] Representative requests, responses, errors, compatibility/deprecation behavior, and reopen conditions are present.

### SIE.9:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Expose the integrated table | Start from the receiving action and design only the claims and branches it needs. |
| One null or HTTP error for every absence | Distinguish semantic absence/unresolved states from access, timeout, and implementation failure. |
| Provenance in internal logs only | Expose the action-changing provenance/currentness summary and stable trace reference. |
| Hide source IDs behind one key | Preserve source schemes and identity-disposition references. |
| Endpoint is available, therefore usable | Validate meanings, branches, currentness, service conditions, and representative Work through `SIE.10`. |
| Semantic result authorizes action | Name the application, engineering, quality, safety, legal, or other decision owner. |

### SIE.9:9 - Consequences

The semantic arrangement becomes directly usable and challengeable. Receivers can distinguish a negative semantic result from an operational failure, and implementations can evolve behind a stable bounded contract while preserving source and rule trace.

The cost is a richer branch model and deliberate presentation of uncertainty and provenance. Some internal schemas or protocols must be wrapped rather than exposed directly.

### SIE.9:10 - Rationale

An integration result has practical value only when it crosses into receiving Work without losing the conditions that make it meaningful. The interface is therefore semantic, not merely syntactic: it carries interpretation, qualification, and return paths while leaving decision authority with the receiver.

### SIE.9:11 - SoTA-Echoing

The best-known line combines explicit API/data-contract practice, data-on-the-Web provenance/version guidance, event interfaces, and standards-based engineering exchange. The serious default is transport-first interface design. Its defect is that success is reduced to reachability and schema conformance. SIE.9 mutates the line by making semantic branches, currentness, provenance, and challenge paths part of the receiving contract.

| Source line | Adopt, adapt, or reject | Role and limit |
| --- | --- | --- |
| [Data on the Web Best Practices](https://www.w3.org/TR/dwbp/) | adapt | Contributes metadata, provenance, version, access, and reuse questions; Web publication is optional. |
| [GS1 EPCIS 2.0.1](https://ref.gs1.org/standards/epcis/2.0.1/) | adapt | Supplies an event-oriented cross-enterprise interface case with identifiers and query semantics; it does not decide SIE identity or receiving action. |
| [ISO 10303-242:2025](https://www.iso.org/standard/84300.html?browse=tc) and [ISO 23952:2020](https://www.iso.org/standard/77461.html) | adapt | Supply unlike versioned engineering source/interface cases; their model scopes and direct authorities remain intact. |
| internal-schema or transport-first API | reject as sufficient | Reachability and schema shape cannot establish semantic interpretation, provenance, loss, branch behavior, or receiving-use fitness. |

Reopen when the receiver or action changes, a source/mapping/realization premise changes, observed service behavior violates a semantic condition, branch handling causes unsafe interpretation, or a protocol change defeats compatibility.

### SIE.9:12 - Relations

- `SIE.1` supplies the receiving action, answer claims, loss, service conditions, tests, and authority boundary.
- `SIE.2` supplies source meanings, identifiers, editions, access, provenance, and currentness.
- `SIE.4`–`SIE.7` supply correspondence, identity, composition, and executable mapping references and branches.
- `SIE.8` supplies selected realization, service assumptions, fallback, and missing implementation results.
- `SIE.10` validates the candidate interface and representative receiving workflow.
- Applications and direct professional owners retain authorization, risk acceptance, and actual outcomes; Data Engineering and Operations retain service execution.

### SIE.9:End

## SIE.10 - Validate a Semantic Integration Result for Its Receiving Use

> **Type:** Method pattern
> **Status:** Eternal alpha
> **Normativity:** Normative method guidance within SIE; examples are constructed and non-normative.
>
> **Primary working result:** a `SemanticIntegrationValidationAccount@Use` that supports a bounded pass, narrow, unresolved, or stop conclusion with appropriate evidence and reopen conditions. A positive receiving-use claim covers all of its load-bearing obligations.

### SIE.10:1 - Problem Frame

**Use this when** a candidate semantic interface or mapping package exists and somebody asks whether it is ready, correct, valid, trustworthy, or fit for use. Enter especially when one test family already passes and is being used as evidence for the whole: valid JSON, conforming RDF shapes, successful ETL, high matcher score, complete provenance, good data-quality metrics, or one successful demonstration.

The primary EntityOfConcern is one semantic-integration result under one receiving-use contract and one inspectable package revision. The first move is to identify the receiving claim being judged and whether known evidence already settles a bounded failure or unresolved result. For a positive claim, identify its load-bearing obligations and the evidence that can test them. The first result can be a supported local failure, scoped uncertainty, or qualified positive use.

The payoff is a truthful decision boundary: the receiver knows which result may be relied on, under which source editions and conditions, and which gaps remain. Do not use SIE.10 to authorize product release, accept a quality result, approve a recall, certify a service, or prove business effectiveness. Direct owners consume the bounded validation account and make those decisions.

### SIE.10:2 - Problem

Semantic integrations fail across several independent layers. A carrier can be well formed while meanings are wrong; correspondences can be defensible while transformation code violates them; identity rows can pass while claim conflicts are flattened; provenance can be complete while source claims are stale or false; quality dimensions can look good while the representative workflow receives the wrong answer.

One aggregate “quality” or “confidence” score hides which premise failed and what must reopen. It also encourages compensating a hard stop, such as unresolved identity or unauthorized source use, with strong results elsewhere.

### SIE.10:3 - Forces

| Force | Tension |
| --- | --- |
| Layering | Separate tests localize defects, while the receiver needs a whole-use conclusion. |
| Positive evidence | Expected matches demonstrate a path, while negative and unlike cases reveal hidden compression and defaults. |
| Coverage | A positive use claim needs its load-bearing premises supported, while a bounded failure can be settled by sufficient defect evidence. |
| Automation | Schemas, shapes, queries, and metrics scale checks, while semantic and authority judgments often require qualified human/domain input. |
| Change | Stable evidence is reusable, while source editions, rules, interfaces, and receiving conditions can invalidate only some results. |
| Decision pressure | Stakeholders want pass/fail, while narrow or unresolved can be the most useful truthful disposition. |

### SIE.10:4 - Solution

Choose the conclusion at its actual scope. A known decisive failure or bounded unresolved premise can finish with sufficient evidence for that result. For a positive whole-use or contract-permitted narrower result, obtain matching evidence for every load-bearing premise, including the receiver's interpretation. Use earlier results when their conditions still match. Preserve hard stops and distinguish unexamined premises from passing ones.

#### SIE.10:4.1 - Pattern-Use Unfolding

Steps 3–10 locate evidence for a positive use conclusion. A sufficient bounded failure or unresolved result can finish at step 2. Reuse matching earlier results for the applicable layers; a changed receiving interpretation can reopen a claim even when its carrier is unchanged.

1. **Identify the validation subject.** Name the mapping, interface, or package result and receiving use being judged. Record the revisions and conditions on which the conclusion depends.
2. **Choose the conclusion and inspect known evidence.** Take the relevant answer claim and stop condition from `SIE.1`. If a demonstrated defect already defeats it, return that bounded failure with sufficient evidence. If a necessary premise is unresolved and that settles the requested question, return the scoped gap. Further obligations remain unexamined. For a positive claim, derive all load-bearing distinctions, loss, currentness/service/quality, authority, protection, branch, and representative-use obligations.
3. **Validate carrier and schema.** Test parseability, declared schemas/shapes, required fields, datatypes, cardinalities, identifiers, and branch encodings. Treat a pass as structural only.
4. **Validate semantic-model and endpoint adequacy.** Test whether source and target concepts, types, relations, constraints, units/codes, and any supplied model express the required distinctions and examples/counterexamples.
5. **Validate correspondences and mappings.** Challenge accepted `SIE.4` rows and execute `SIE.7` positive, boundary, negative, and unlike examples. Check selection, cardinality, conversion, defaults, errors, loss, and trace independently.
6. **Validate identity and authority.** Test every load-bearing `SIE.5` disposition at its grain and interval, including issuer, version, part-whole, reuse, split/merge, and unresolved branches. Verify required authority and permission inputs rather than inferring them from data access.
7. **Validate claim composition.** Test `SIE.6` comparability, conflict, non-comparability, supersession, incomplete-source, and uncertainty branches. Confirm that source claims and derivation remain recoverable.
8. **Validate realization and interface behavior.** Test currentness, latency, availability, snapshot/caching, invalidation, source failure, partial results, access/protection, provenance, error semantics, and challenge paths required by `SIE.8` and `SIE.9`.
9. **Validate provenance, currentness, and quality.** Check that every relied-on output can recover its source and rule premises, that source/version/time status satisfies the use, and that selected quality measurements meet their action-changing thresholds. Do not treat provenance or process conformance as truth.
10. **Replay representative receiving Work.** Run the named query, decision preparation, operation, or engineering workflow with expected positive, negative, and unlike cases. Observe whether the receiver obtains and interprets the required result and stops on forbidden branches.
11. **Assign dispositions at the supported scope.** Use pass, narrow, unresolved, or stop for tested claims, and preserve any material unexamined reach. A positive narrow result states the contract-permitted subset and covers all of that subset's load-bearing premises; excluded branches remain explicit. A hard stop cannot be offset by scores elsewhere.
12. **Record repairs, returns, and reopen.** Send source, semantic, mapping, implementation, authority, or receiver defects to their direct owners; state which layer and consumers require retest after change.

#### SIE.10:4.2 - Record the Result

| Validation position | Required content |
| --- | --- |
| subject and use | package/interface revision, source/rule versions, realization/test state, receiver and use |
| obligations | premises relevant to the claimed conclusion; all load-bearing contract obligations for a positive use claim |
| layer result | layer, tested claim, method/case, evidence, expected/observed result, pass/narrow/unresolved/stop, defect owner |
| dependency | exact source, correspondence, identity, composition, mapping, realization or interface premise consumed |
| coverage | examined cases and matching earlier results; material unexamined or unresolved premises, distinguished from passing ones |
| use disposition | supported local failure or gap, or positive result with its conditions and full load-bearing coverage; excluded subset and hard stops |
| continuation | repairs or direct-owner returns, focused retest, affected consumers, reopen condition |

#### SIE.10:4.3 - What Changes in Practice

The team stops asking whether “the integration” passed one test. Each claim has an appropriate layer, evidence, and owner. A bounded subset can be used without hiding excluded rows, and a source or rule repair triggers focused revalidation instead of an automatic full rebuild or a silent continuation.

### SIE.10:5 - Archetypal Grounding

#### SIE.10:5.1 - Positive AP242/QIF Subset Validation

The constructed AP242/QIF package is frozen with named AP242/QIF source occurrences, correspondence set, identity dispositions, claim-composition rules, mapping specification, hybrid realization, and review interface. It uses SIE.1:5's stipulated receiving contract: the preceding 24-hour observation window, two-second response limit, and permission to return qualified evidence while showing unresolved local-extension and unknown-unit branches separately.

| Layer | Constructed probe and result |
| --- | --- |
| carrier/schema | Request and response validate against their declared forms; unmatched, incompatible, unresolved, stale, and source-error states are representable. Passes structurally. |
| semantic-model/endpoints | AP242 feature/configuration/effectivity and QIF plan/characteristic/result senses are recoverable. One local extension remains undefined; rows that consume it are unresolved. |
| correspondence | Known plan/feature relation passes; shared-label false match is rejected; non-dimensional characteristic defeats a global type equivalence. Passes for the accepted row set. |
| identity/authority | Known feature identifier relation passes at revision/configuration/effectivity grain; obsolete revision and unresolved local ID stop their dependent branches. Engineering and quality authority remain external. |
| claim composition | Compatible AP242 definition/effectivity and QIF plan/result claims retain sources; contradictory result status returns conflict; incompatible intervals remain non-comparable. Passes for qualified branches. |
| transformation | Known mapping, one-to-many characteristic, unit conversion, unmatched feature, unknown unit, stale result, missing provenance, and source-timeout cases return the specified branches. One unknown-unit row stops. |
| realization/interface | Stable semantic metadata is available; volatile source data is queried under captured occurrence times. The constructed one-second response meets the two-second limit. Timeout returns incomplete only under the contract; challenge paths resolve to premises. Conditional pass. |
| provenance/currentness/quality | Every accepted output row recovers sources, rules, and times. The configuration matches the released review basis; QIF observations six hours before T meet the 24-hour window, while a 25-hour control returns stale. Undefined-extension rows remain visibly unresolved outside the qualified set. |
| receiving workflow | The quality engineer retrieves a known result, recognizes unmatched/incompatible/conflict states, and stops on unresolved configuration or identity. Passes for the bounded subset. |

The whole-use disposition is **narrow** under the stated contract: the qualified row set is usable for the evidence-return workflow, while the undefined local-extension and unknown-unit branches remain separately visible and unresolved. The receiver's permission covers this partial evidence answer. The account does not accept the inspection result or release the configuration. A definition or unit-table repair reopens only the affected rows and receiving tests.

#### SIE.10:5.2 - A Decisive Defect and a Changed Receiving Meaning

In a constructed mapping probe, an input of 1 metre produces an output labelled 1 millimetre; the receiving contract requires 1000 millimetres. The input, rule, expected value, and observed output are enough to establish this mapping failure. Return that defect to SIE.7. Other layers remain unexamined; their results are unnecessary for this bounded failure. If the source unit is unavailable instead, the conversion premise remains unresolved at that scope.

Now consider a previously qualified availability interface. Its JSON field and numeric type stay unchanged, but the source changes the value from present availability to a future promise horizon. The receiver still reads the displayed quantity as “available now”. A passing shape check cannot support the earlier use conclusion: the changed interpretation defeats a relied-on premise. SIE.11 identifies the affected mapping and interface uses.

After repair, a positive conclusion for that receiving use needs the corrected interpretation and every other load-bearing condition. Matching earlier evidence can supply unchanged conditions; the known failure or its repair alone cannot establish the whole result.


### SIE.10:6 - Bias-Annotation

| Lens | Likely drift | Repair |
| --- | --- | --- |
| Governance | The validation team is treated as release, quality, safety, or business authority. | State the semantic conclusion and return the owning decision with its conditions. |
| Architecture | Available automated tests define all validation layers. | Add qualified semantic, identity, authority, and receiving-work evidence where automation cannot decide. |
| Ontology/Epistemology | Well-formed representation, true relation, supported claim, and usable decision collapse. | Test each claim at its layer and keep the whole-use composition explicit. |
| Pragmatics | A decisive failure still triggers every layer test. | Finish the bounded failure with sufficient evidence; require full load-bearing coverage for a positive whole-use or permitted subset claim. |
| Didactics | A score invites compensation across hard stops. | Use categorical layer dispositions with evidence and state that stops are non-compensatory. |

### SIE.10:7 - Conformance Checklist

Apply the layer requirements below to the conclusion being claimed. A bounded failure or unresolved result needs sufficient evidence for that result; a positive use claim needs all of its load-bearing obligations covered.

- [ ] The subject, receiving use, and conditions required by the conclusion are identified.
- [ ] Known decisive evidence can finish a bounded failure or scoped gap; material unexamined premises remain distinct from passing ones.
- [ ] Carrier/schema pass is not reported as semantic or receiving-use pass.
- [ ] Endpoint/model adequacy includes examples and counterexamples for required distinctions.
- [ ] Correspondence judgment and mapping execution are tested separately.
- [ ] Every load-bearing identity disposition, issuer/authority condition, and unresolved branch is tested.
- [ ] Claim composition tests include conflict, non-comparability, incomplete source, and source-claim recoverability.
- [ ] Realization/interface tests cover currentness, failure, partial results, access/protection, provenance, and challenge paths as applicable.
- [ ] Quality dimensions and thresholds are selected by the use and do not replace representative Work.
- [ ] Positive, boundary, negative, unlike, and changed-source cases cover the material failure modes.
- [ ] Whole-use disposition is pass, narrow, unresolved, or stop with no score-based compensation of hard stops.
- [ ] Repairs, direct-owner returns, focused retests, affected consumers, and reopen conditions are explicit.
- [ ] No external release, acceptance, authorization, effect, or universal correctness claim is implied.

### SIE.10:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Valid schema, therefore valid integration | Test meanings, relations, identity, composition, mappings, provenance, quality, and receiving Work separately. |
| One quality/confidence score | Record layer-specific evidence and categorical dispositions; preserve hard stops. |
| Happy-path demonstration | Add negative, boundary, unlike, changed-source, stale, conflict, and failure cases. |
| Provenance completeness means truth | Test the source claim and receiving adequacy; provenance only makes derivation inspectable. |
| High alignment benchmark score | Validate local endpoint relations and use loss against representative cases. |
| All-or-nothing readiness | A known defect can finish a bounded failure. A positive subset result requires the contract's permission and all premises on which that subset relies. |
| Semantic validation authorizes release | Return the account to the actual engineering, quality, safety, legal, or application authority. |

### SIE.10:9 - Consequences

Defects are localized to source, semantic, identity, composition, mapping, realization, interface, quality, or receiving-use layers. A bounded useful result can proceed without hiding excluded branches, and later changes can trigger focused replay through explicit dependencies.

The cost is several kinds of evidence and collaboration with domain and receiving practitioners. Some integrations that appear technically complete remain unresolved or stop because their identity, authority, or representative-use premises are missing.

### SIE.10:10 - Rationale

Semantic integration is a claim chain. Different links require different evidence, and the receiver depends on their composition. Layered validation preserves this structure: no lower layer proves a higher one, while a positive conclusion requires support for every load-bearing premise of the claimed whole use or contract-permitted subset.

### SIE.10:11 - SoTA-Echoing

The best-known line combines constraint validation, ontology-alignment evaluation, provenance, data-quality models, quality management, and user/task validation. The serious defaults are conformance-only testing and aggregate quality scoring. Their defect is not automation or measurement; it is using one layer as a proxy for the whole use. SIE.10 mutates the line into a dependency-aware account with categorical bounded dispositions and representative Work replay.

| Source line | Adopt, adapt, or reject | Role and limit |
| --- | --- | --- |
| [SHACL](https://www.w3.org/TR/shacl/) | adapt | Supplies declared RDF graph constraint validation; passing shapes do not establish all semantics, identity, truth, or use fitness. |
| [DQV](https://www.w3.org/TR/vocab-dqv/) and [ISO/IEC 25012:2008](https://www.iso.org/standard/35736.html) | adapt | Supply quality vocabulary and a data-quality model; select dimensions and measurements by receiving action. |
| [ISO 8000-61:2016](https://www.iso.org/standard/63086.html) | adapt | Contributes data-quality management process questions; process conformance does not prove a particular answer fit. |
| [OAEI 2025 results](https://oaei.ontologymatching.org/2025/results/) | adapt | Provide alignment-evaluation tasks and evidence; benchmark results do not validate a local correspondence set universally. |
| one conformance gate or aggregate score | reject as sufficient | Unlike layers and hard stops must remain separately visible before a whole-use conclusion. |

Reopen when a relied-on source, model, identifier, correspondence, composition, mapping, realization, interface, quality threshold, or receiving workflow changes; when new evidence defeats a layer; or when a representative case exposes an untested load-bearing obligation.

### SIE.10:12 - Relations

- `SIE.1` supplies the receiving obligations, accepted loss, authority, representative cases, and stop rules.
- `SIE.2` supplies source meanings, editions, authority, provenance, access, currentness, and gaps.
- `SIE.4`–`SIE.9` supply the correspondence, identity, claim-composition, mapping, realization, and interface subjects and their branch contracts.
- Current FPF `A.10` and `A.10.1` govern evidence/provenance reliance and generic affected-use discovery.
- `SIE.11` traces changed source, model, mapping, or interface premises to the receiving uses that rely on them. Matching earlier validation remains usable for unaffected results; material changes reopen the relevant premises and receiving interpretation.
- Applications, Systems Engineering, quality, safety, legal, MDM, Data Engineering, and Operations owners consume the bounded account and retain their own acceptance, authorization, operation, and outcome decisions.

### SIE.10:End

## SIE.11 - Trace Semantic Change and Revalidate Affected Uses

> **Type:** Method pattern
> **Status:** Eternal alpha
> **Normativity:** Normative method guidance within SIE; examples are constructed and non-normative.
>
> **Primary working result:** qualified results for the semantic-integration uses affected by a changed premise; an `AffectedSemanticUseRevalidationAccount@Change` assembles them when a receiving use needs a common account.

### SIE.11:1 - Problem Frame

**Use this when** a relied-on source definition, model commitment, identifier meaning, mapping premise, or interface interpretation changes and the integration's continued use needs a decision. A familiar warning sign is an unchanged API field that now answers a different question.

Start by comparing the earlier and later meaning at the receiving question. A compatible documentation move can finish with a reference repair. A changed meaning can require repair or renewed validation of the integration results that relied on it.

The object is the affected semantic reliance and its consequences for receiving uses. The gain is a justified continuation, repair, narrowed use, or scoped unresolved result. To assert that all uses remain unaffected, establish adequate coverage of the relevant uses and their reliance.

Use the applicable domain Method directly for a known operational change that does not alter a relied-on source or semantic premise. If one already identified use is the whole question, resolve that use directly with the relevant domain Method and A.10 reliance guidance. A.10.1 is needed when affected uses must be discovered across a scope.

### SIE.11:2 - Problem

A source update can be treated as harmless because the schema still parses, or as universally disruptive because its version changed. Either response misses the actual reliance. Some consumers use a definition that changed; others use a different proposition from the same source; still others are merely mentioned in nearby records.

Indiscriminate revalidation consumes work without settling those differences. An incomplete search can create the opposite error: one repaired mapping is reported as proof that the entire integration remains valid.

### SIE.11:3 - Forces

| Force | Tension |
| --- | --- |
| Selectivity | Only affected reliance needs reopening, while hidden consumers can remain dependent on changed meaning. |
| Continuity | Matching earlier results save work, while changed assumptions can invalidate them. |
| Coverage | A local answer can finish promptly, while a wider no-impact claim needs wider support. |
| Authority | An integrator can repair its mappings and interfaces, while source and receiving decisions retain their owners. |
| Evidence effort | Additional inquiry can change a decision, while unavailable or low-value information can consume the work needed for repair. |

### SIE.11:4 - Solution

Follow the changed proposition through actual semantic dependencies to the results and receiving uses it can alter. Complete supported branches at their proper scope. Assemble a wider account only for a receiver that needs it.

#### SIE.11:4.1 - Pattern-Use Unfolding

1. **Compare the relied-on meaning.** Identify what the receiving question depended on in the earlier source or premise and what the later content says. Include changed applicability, subject grain, interval, assumptions, or limits where relevant. An inaccessible later definition leaves that comparison unresolved.
2. **Finish a compatible repair when sufficient.** If content, applicability, and access remain compatible for the use, make the needed reference repair and retain matching results. A version or URL change alone does not require every downstream Method to run again.
3. **Find affected uses when their scope is unsettled.** Apply A.10.1 to discover actual reliance within the question's scope, using source-side and receiver-side evidence or an index that adequately covers both. Distinguish a material dependency from a mention. Retain coverage gaps that limit the intended conclusion.
4. **Select the integration result that the change can alter.** Use the domain returns below. Follow a further consumer only when the changed result can alter its action or claim. The physical proximity of files is not a dependency rule.
5. **Repair or revalidate that result.** Apply its defining Method to the changed premise. Reuse earlier evidence whose actual conditions still match. Return a supported continuation, repair, permitted narrower use, or scoped gap. Source truth, master identity, product release, and application decisions go to the owners of those decisions.
6. **Return the completed branch.** Give the receiver the result it needs, with the changed premise and remaining limits where those affect reliance. A completed direct result is sufficient for its own receiving question.
7. **Combine results when a receiver needs the wider answer.** State the covered uses, their relevant results, unresolved uses or discovery gaps, and the continuation that those results support. A broader no-impact conclusion requires the corresponding coverage; completed local branches cannot supply unexamined ones.

When additional evidence is being considered, apply `C.11.DUA` to compare its attainable contribution to the receiving decision with its cost, delay, downside, and displaced work. A gap can remain a qualified gap when further inquiry cannot support a worthwhile next action; that limitation does not warrant a stronger claim.

#### SIE.11:4.2 - Domain Returns

| Changed reliance | Integration result to revisit |
| --- | --- |
| A concept, relation, or model constraint | SIE.3 model adequacy and any affected SIE.4 correspondence. |
| Identifier meaning, scheme, grain, or interval | SIE.5 identity disposition and the results that actually use it. |
| Source-claim scope or interpretation | SIE.6 composition, conflict, or non-comparability result. |
| A transformation premise | SIE.7 mapping and its affected outputs. |
| Availability, permissions, freshness, or service conditions | SIE.8 realization choice or SIE.9 receiving interface, according to the changed condition. |
| Receiving meaning or acceptance condition | SIE.9 interface contract and the corresponding SIE.10 validation. |

This table locates the defining result; the actual dependency determines which returns are needed and their useful order.

#### SIE.11:4.3 - Record the Result

For a direct repair, use the result already needed by its consumer. For a common account, retain the following content at the scope the receiver needs:

| Account position | Receiving content |
| --- | --- |
| Change and reliance | Earlier relied-on meaning, later meaning, and the affected question. |
| Covered uses | Actual dependencies and the basis for the stated discovery scope. |
| Direct results | Completed repairs, revalidation, permitted continuation, or narrowed uses under their defining Methods. |
| Unresolved reach | Unexamined or inaccessible reliance, discovery gaps, and their effect on the conclusion. |
| Continued use | What the receiver can now rely on and which changed conditions would reopen it. |

The account summarizes its constituent results. It does not serve as a circular input that those results must await before they can be completed.

#### SIE.11:4.4 - What Changes in Practice

The maintainer can say which interface meaning changed, which mapping or identity result was revisited, and what can continue. A corrected local reference can finish immediately. A broader claim remains bounded by the uses actually discovered and assessed.

### SIE.11:5 - Archetypal Grounding

#### SIE.11:5.1 - Compatible Reference Repair

A publisher moves a vocabulary definition to a new documentation address. The integrator can access both the relied-on content and its new location. The definition, applicability, and access needed by the mapping remain compatible.

The integrator updates the reference used by that mapping. Its existing qualification still answers the unchanged question. This is the completed result for the reference-maintenance use; no multi-use account is needed.

If the later definition cannot be inspected, the same evidence cannot support this conclusion. The result then names the inaccessible comparison and the reliance it leaves unresolved.

#### SIE.11:5.2 - Changed Promise Horizon

A provider changes `availableToPromise` from the reservation meaning used for present availability to a promise for a future horizon. The API field and its numeric type stay the same. The semantic-integration maintainer compares the two meanings and inspects the actual consumers.

| Use | Reliance and result |
| --- | --- |
| Present-availability endpoint | Its mapping treated the quantity as answering “available now”. That premise changed. Repair the mapping and interface meaning, or withhold that answer until a qualified present-time source is supplied. SIE.10 checks the supported receiving result. |
| Future planning view | It can potentially use the new quantity when it exposes the horizon and the receiving question agrees. Validate those conditions instead of assuming that every use must stop. |
| Descriptive product catalogue | Its definitions and product descriptions do not consume the changed quantity. Where that independence is established, retain its matching result. |
| A consumer with unavailable interpretation | The maintainer cannot determine how it uses the quantity. Return that scoped uncertainty; the other completed branches retain their own results. |

If the service owner needs an integration-wide continuation decision, the account combines those results and the remaining uncertainty. It does not state that all uses are unaffected. The provider controls its source definition; the integrator controls the supplied semantic interface; each application owner determines whether the qualified answer is adequate for its decision.

### SIE.11:6 - Bias-Annotation

| Lens | Likely drift | Repair |
| --- | --- | --- |
| Governance | The integration maintainer appears to authorize the application's decision. | Return the qualified integration result to the receiving decision owner. |
| Architecture | Every linked component is treated as an affected consumer. | Follow the changed proposition through dependencies that can alter results. |
| Ontology/Epistemology | An unchanged field name is read as unchanged meaning. | Compare the actual definition, applicability, and receiving interpretation. |
| Pragmatics | All validation restarts after every source version change. | Retain matching results and finish sufficient direct repairs. |
| Didactics | A list of completed checks looks like complete coverage. | State which uses the evidence covers and preserve unresolved reach. |

### SIE.11:7 - Conformance Checklist

- [ ] The compared change concerns a premise used by an identified receiving question.
- [ ] Compatible reference repair can complete without a wider account.
- [ ] Discovery, where needed, supports the stated scope and distinguishes dependencies from mentions.
- [ ] Each affected integration result uses its defining Method.
- [ ] Reused evidence still matches its actual conditions.
- [ ] Independently supported branches finish at their own scope.
- [ ] A common account has a receiving use and preserves unresolved coverage.
- [ ] A wider no-impact claim has support for the uses it covers.

### SIE.11:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Schema compatibility as semantic compatibility | Compare the question answered by the field, including its horizon and applicability. |
| Every reference occurrence requires revalidation | Establish whether the result relies on the changed proposition. |
| One repaired branch clears the whole integration | Bound the conclusion by discovered and assessed uses. |
| Summary required before its constituent decisions | Complete direct domain results first and summarize only when a receiver needs it. |

### SIE.11:9 - Consequences

Supported uses can continue while affected branches receive focused repair. Dependency evidence becomes useful because it points to a changed receiving result. Local completion no longer waits for an unnecessary integration-wide account.

Finding hidden reliance and interpreting source changes can require domain and receiver participation. A wider assurance claim may remain unavailable while an actual consumer or later definition is inaccessible. The result preserves that limitation without erasing completed branches.

### SIE.11:10 - Architectural Rationale

The changed proposition, rather than the changed carrier, determines semantic impact. Direct domain Methods decide the affected result; discovery determines where those questions arise. Keeping those contributions distinct permits reuse, independent completion, and honest limits on wider conclusions.

### SIE.11:11 - SoTA-Echoing

The practice question is which receiving uses must change when one semantic premise has changed and the affected scope is still unsettled. In §5.2, both the present-availability endpoint and other consumers exist; knowing the changed field alone does not settle their reliance. The selected line combines A.10/A.10.1's premise comparison and scoped discovery with the integration-specific returns in §4.2.

The serious alternative is a bounded full regression: identify the same receiving scope, update the tests to the new source meaning, and revalidate every registered use in it. This can be preferable when the suite is small and inexpensive or a reliable dependency analysis would cost more. It is not merely rerunning old tests against an unchanged schema.

| Answer to the same multi-use horizon change | Work and evidence at the same scope | Selection and accepted trade-off |
| --- | --- | --- |
| Discover changed reliance and revalidate affected results | Compare the two meanings, inspect source-side and receiver-side dependencies, qualify coverage, and retest results that rely on the changed horizon. Keep applicable evidence for the independent catalogue. | **Adopt** A.10/A.10.1 in §4.1.1–3/5–7; **adapt** §4.2 and §5.2 to semantic model, mapping, interface, and validation results. This avoids repeating the catalogue's unrelated checks and lets supported branches finish. It spends effort establishing dependencies and leaves an inaccessible consumer unresolved. |
| Revalidate every identified use in the same receiving scope | Make the same meaning and coverage comparison, then execute the appropriate receiving-use checks for every member, including those ultimately found independent. | Retain this alternative when those checks are cheaper or more dependable than selective impact analysis. It may reduce reliance on a detailed dependency model, but can repeat unaffected checks and delay a common release. It still cannot clear an unknown consumer or infer meaning from schema compatibility. |

For the worked horizon case, the established catalogue independence and separable endpoint results justify selective revalidation. The accepted trade-off is the work needed to establish that independence and the explicit limit on the unknown consumer; no universal cost or completeness advantage is claimed. §4.1.7 prevents local completions from being mistaken for a wider no-impact result. For one already known use, the direct domain result remains sufficient under §1.

[LOT4KG](https://lot.linkeddata.es/LOT4KG/) supplies a current candidate line for changes that propagate between an ontology, mappings, graph content, constraints, and validation. **Adapt** those relationships in §4.1.4–5 and §4.2 when a KG realization is selected. They help locate which integration result needs work; they do not choose source truth, application action, or a universal regression policy. For other realizations, the same return question is answered from their actual semantic dependencies. **Reject** a changed version alone as evidence that every use failed, and an unchanged carrier alone as evidence that every use passed.

Reopen this comparison when one actual affected use was missed, when a dependency or coverage claim is defeated, or when the cost of qualifying selective impact exceeds the available full receiving-use regression. Reconsider only the affected discovery and checking choice in §4.1.3–5. Changed results still require their domain evidence whichever strategy is selected.

### SIE.11:12 - Relations

- A.10.1 governs affected-use discovery when the scope of reliance needs to be found.
- SIE.2 supplies the source meaning, edition, authority, and access premises used in the comparison.
- SIE.3–SIE.9 supply the domain results located in §4.2; SIE.10 supplies validation for the affected receiving claim.
- SIE.12 supplies the module dependencies and material-change arrangements of an actual commons.
- Domain source owners, MDM, SYSE, operational providers, and receiving applications retain their respective decisions.

### SIE.11:End

## SIE.12 - Govern Modular Semantic Commons without Universal Authority

> **Type:** Method pattern
> **Status:** Eternal alpha
> **Normativity:** Normative method guidance within SIE; examples are constructed and non-normative.
>
> **Primary working result:** a `ModularSemanticCommonsAccount@Community` describing how actual users maintain and rely on shared semantic modules, their dependencies, decisions, and releases.

### SIE.12:1 - Problem Frame

**Use this when** independently governed participants depend on shared semantic modules and need an arrangement for maintaining them. A typical failure is a changed shared term whose consumers cannot determine who could approve the change, which meaning their interface uses, or how to migrate.

Start with one module and the uses that actually depend on it. Establish its scope, who can decide its content and release, and how its users can obtain an identifiable maintained edition. The first useful result is an agreement through which those participants can make and use a concrete module change.

The object is the shared maintenance and reliance arrangement for semantic modules. The gain is continued reuse with explicit local commitments, contribution rights, dependencies, and change consequences. A compatibility claim covering additional users needs support for those users' relevant reliance.

A team or a pair maintaining one interface can use its ordinary model and interface agreement when that suffices. A repeated file or shared repository alone does not establish a commons that needs this Method.

### SIE.12:2 - Problem

Reusable semantic assets acquire users outside their original project. A term, class, relation, or mapping then carries assumptions into interfaces maintained by other participants. Changes can break those assumptions even when the shared file remains available.

One response is to require every participant to adopt one centrally controlled model. Another is to allow local changes without a recoverable relation to the shared meaning. Both can defeat useful reuse: the first can suppress necessary domain distinctions, while the second makes compatibility impossible to assess.

### SIE.12:3 - Forces

| Force | Tension |
| --- | --- |
| Shared meaning | Common modules reduce repeated work, while participants retain distinct purposes and source authority. |
| Local development | Extensions can answer local questions, while consumers need to know which shared commitments still hold. |
| Decision rights | Maintainers need power to release a module, while contact or repository access alone cannot establish that remit. |
| Stability | Identifiable meanings support reliance, while mistakes and changed requirements need correction. |
| Participation | Open contribution can improve coverage, while unresolved proposals still need a usable decision path. |

### SIE.12:4 - Solution

Define the smallest shared module arrangement that serves the actual users. Make its semantic scope, decisions, dependencies, and releases usable in their integration work. Preserve local modules and disagreement where convergence is unnecessary or unsupported.

#### SIE.12:4.1 - Pattern-Use Unfolding

1. **Identify the shared use.** Name the users and questions that depend on the module. Locate the semantic content they share and the local distinctions they still need. If the actual need is only one interface agreement, complete that agreement through the relevant SIE Methods.
2. **Set module boundaries.** State the module's domain, concepts and relations, intended uses, material exclusions, and relation to local extensions. Use SIE.3 for content that needs model development and SIE.4 for qualified correspondences between different module meanings.
3. **Establish identification and dependencies.** Choose namespaces or identification practices that let consumers recover the intended term or module meaning. Identify editions and the dependencies each supported use needs. A permitted version range must have a semantic compatibility basis for its claimed use.
4. **Assign the decisions and communication.** State who may propose changes, decide module content, release an edition, resolve a disagreement under the community's rules, and communicate with users. Record the actual remit of each responsibility. A source owner retains its source meaning and issuance authority.
5. **Make contribution workable.** Give a proposer enough guidance to supply the changed meaning, rationale, examples, affected modules, and known consumer consequences. Route the proposal to the people authorized to decide it. Keep an unresolved disagreement explicit and permit a scoped local extension or alternative module when it can serve its users honestly.
6. **Prepare the release for its consumers.** Identify material semantic changes and use SIE.11 for affected reliance. Provide the edition, access, dependency conditions, and migration or deprecation information needed by those users. Distinguish a clarification from a changed meaning; preserve a way to identify the earlier meaning when consumers still rely on it.
7. **Notify and maintain at the agreed scope.** Give affected users notice that permits the action required by their dependency and the community agreement. Maintain a responsive contact and a workable path for corrections. An urgent correction may require immediate qualified publication and notification; describe the resulting limits honestly.
8. **Return the usable arrangement.** Show how the named participants can obtain a module, propose a change, decide and release it, and interpret the effect on their supported uses. An unresolved decision right or dependency limits the part of the commons that can be claimed as governed.

These responsibilities can fit a small agreement for a small commons. Broader participation adds work only where additional semantic dependence or decision needs arise.

#### SIE.12:4.2 - Record the Result

| Arrangement position | Content used by participants |
| --- | --- |
| Shared module and users | Semantic scope, supported uses, and the participants who depend on it. |
| Local relationship | Extensions, maintained correspondences, disagreements, and the commitments claimed across module boundaries. |
| Identification and dependencies | Namespaces or equivalent identifiers, recoverable editions, access, and dependency or compatibility conditions. |
| Decisions and communication | Proposal, content, release, dispute, and contact responsibilities at their actual remit. |
| Change and continued use | Material-change assessment, notices, correction, migration, deprecation, and maintained access needed by consumers. |

Refer to existing module definitions and working agreements when they supply this content. The account makes the arrangement recoverable; it need not reproduce every module or introduce a separate record for each responsibility.

#### SIE.12:4.3 - What Changes in Practice

A user can identify the meaning and edition its interface consumes and find the decision needed for a proposed change. Maintainers can release a scoped improvement while preserving the commitments they claim to retain. Participants can keep different local meanings through explicit module boundaries and correspondences.

### SIE.12:5 - Archetypal Grounding

#### SIE.12:5.1 - Equipment Classes Shared by Three Organizations

Two manufacturers and a service partner exchange service observations using a shared equipment-classification module. Each manufacturer also has local classes needed for its own products.

| Arrangement | Concrete use |
| --- | --- |
| Shared core | Describes the equipment categories needed to interpret the service observations. |
| Local modules | Retain product-specific distinctions and identify their relation to the shared core. |
| Correspondences | State the qualified relations between local and shared classes; different meanings remain visible. |
| Content decision | The agreed maintainers decide changes to the shared module within its stated scope. |
| Release decision | The participant authorized to release the module publishes an identified edition and its dependency conditions. |
| Contact | A reachable participant receives questions, communicates decisions, and helps route disputes. |
| Source authority | Each manufacturer retains the authority for its product descriptions and issued source claims. |

A participant proposes changing a shared class from “equipment with a replaceable drive” to “equipment serviced through a replaceable drive module.” The second definition changes the classification criterion. Existing service queries can depend on the first meaning.

For this constructed agreement, the maintainers retain the earlier class and introduce a distinct class for the new criterion. The illustrative identifier `equip:DriveReplaceable` continues to mean “equipment with a replaceable drive”; `equip:DriveModuleServiceable` means “equipment serviced through a replaceable drive module.” The second module edition contains both definitions and leaves the earlier edition accessible. It asserts no equivalence between the classes.

The manufacturers' qualified product descriptions supply these discriminating cases:

| Equipment | Earlier class | New class |
| --- | --- | --- |
| X: its drive can be replaced as a separate part; it has no replaceable drive service module. | Included: the drive is replaceable. | Excluded: module replacement is not its service arrangement. |
| Y: its drive can be replaced separately, and the supported service arrangement also provides a replaceable drive module. | Included. | Included under the module-service criterion. |

SIE.11 follows the changed classification need to the actual queries. Two consumer outcomes complete the illustrative transition:

- The service partner changes its receiving question to module-replacement planning. It adopts `equip:DriveModuleServiceable`, updates the relevant correspondence and query, and verifies that Y is included and X excluded. The receiving owner accepts that scoped result; SIE.10 validates its integration premises.
- Manufacturer A retains its spare-drive query against `equip:DriveReplaceable`. Its required meaning and the qualified X/Y results remain unchanged, so it retains matching evidence for that use. Adopting the new class is not a prerequisite for continuing this query.

The participant authorized to release the module publishes the identified edition with those definitions, dependency conditions, and migration information. Contact supplies the notice; the content decision, product-source claims, and receiving decisions keep the separate remits shown above. The two completed consumer results do not establish migration by every other user.
If the two manufacturers require incompatible local criteria, the commons can retain scoped local modules and their qualified correspondences. No broader equivalence is asserted merely to make the shared diagram simpler.

#### SIE.12:5.2 - A Sufficient Interface Agreement

Two providers agree to expose separately attributed `on hand` and `available to promise` values. They have no additional users maintaining a shared module.

Their agreement identifies the meanings, source owners, interface responsibilities, and change conditions. SIE.3 and SIE.9 can supply the model and interface results. Those results complete the current need. A commons arrangement becomes useful if independently maintained shared modules and their users create a further maintenance problem.

#### SIE.12:5.3 - Urgent Semantic Correction

A shared mapping incorrectly interprets a quantity's unit, and a supported interface can return a wrong answer. The authorized maintainer corrects or withdraws the affected mapping according to the community's rules, identifies the affected edition, and notifies its consumers. The notice explains the correction and the supported continuation.

The completed action is an urgent qualified correction with notification. Earlier users' unresolved reliance remains visible for SIE.11; the action cannot establish that every consumer has already migrated.

### SIE.12:6 - Bias-Annotation

| Lens | Likely drift | Repair |
| --- | --- | --- |
| Governance | A listed contact is treated as the owner of every semantic decision. | State content, release, dispute, communication, and source responsibilities at their actual remits. |
| Architecture | A single large model replaces useful local modules. | Start with the shared uses and retain local distinctions through scoped dependencies and correspondences. |
| Ontology/Epistemology | A stable label conceals a changed classification criterion. | Compare meanings and examples; keep earlier and replacement meaning identifiable. |
| Pragmatics | A small interface acquires unnecessary community machinery. | Complete the local agreement when that is the actual shared need. |
| Didactics | A version number is read as a guarantee of compatibility. | State the semantic basis and receiving scope of compatibility. |

### SIE.12:7 - Conformance Checklist

- [ ] Actual users and their shared-module reliance justify the arrangement.
- [ ] The shared scope and local extensions preserve the commitments they claim to use.
- [ ] Consumers can identify the model meaning, edition, access, and applicable dependencies.
- [ ] Proposal, content, release, dispute, contact, and source responsibilities are distinguishable where they matter.
- [ ] A material change has a usable decision and affected-consumer path.
- [ ] Identification, notice, migration, and deprecation follow the chosen rules and actual use consequences.
- [ ] A local interface can finish without creating an unnecessary commons.
- [ ] Unresolved rights or reliance limit the corresponding claimed arrangement.

### SIE.12:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Shared repository treated as governance | Establish the decisions and dependency conditions actual users need. |
| Contact metadata treated as decision authority | Identify who may decide content and releases and at what scope. |
| Silent meaning replacement | Expose the changed criterion, identification treatment, and consumer consequences. |
| Mandatory convergence of incompatible meanings | Retain scoped alternatives and the correspondences that are actually supported. |
| Announcement treated as completed migration | Distinguish notification from each affected consumer's result. |

### SIE.12:9 - Consequences

Shared modules can evolve while their users retain identifiable meanings and workable returns. Local development remains possible, and a community can decide changes without claiming authority outside its remit.

The arrangement costs maintenance, communication, and change assessment. Those costs increase with real dependency and participation. Some proposals remain local or unresolved when shared convergence cannot be justified.

### SIE.12:10 - Architectural Rationale

A commons is useful through the semantic commitments its users share and the decisions they can actually make. Module boundaries preserve the scope of those commitments. Identifiable meanings and dependencies let users determine how a change affects their work; assigned rights let the relevant participants act on that result.

### SIE.12:11 - SoTA-Echoing

The practice question is how the three independently governed organizations in §5.1 can change their shared equipment classification while keeping supported service queries interpretable. The selected line is a scoped shared core with separately maintained local modules, explicit dependencies, identifiable meanings, and assigned content and release rights. It adapts the [OBO Foundry principles](https://obofoundry.org/principles/fp-000-summary.html) to these actual users.

A serious alternative for these same users is a jointly qualified release bundle: publish the relevant shared core and local profiles as one identified, compatible combination. This also preserves source authority and can retain older supported editions. It offers one combination to qualify instead of asking every consumer to select compatible module editions; it need not impose a universal ontology.

| Arrangement for the same equipment-class change | Comparable effort and gain | Selection and accepted trade-off |
| --- | --- | --- |
| Shared core with independently maintained local modules | Examine the same changed criterion, equipment counterexamples, mappings, and receiving queries. Qualify the affected module interfaces and state the editions each supported use can combine. An unchanged local module can remain on its supported basis. | **Adapt** §4.1.2–3/5–7 and §5.1. Separate module maintenance preserves the participants' local distinctions and lets a scoped change proceed without constructing another joint bundle. It requires explicit dependency and compatibility evidence; independent version numbers alone are insufficient. |
| One jointly qualified bundle of the relevant core and profiles | Use the same meanings and cases and reuse unchanged component evidence, then qualify and identify the supported combination. Coordinate its release and continued support with the three participants. | Retain this alternative when consumers need a common deployment combination or the participants can qualify it more economically than separate compatibility claims. It simplifies edition selection but adds joint-release coordination, including when only one component changes. |

For §5.1's independently owned local classifications, the modular arrangement is selected to preserve useful local change and scoped reuse. The accepted cost is maintaining compatibility and reliance evidence at the module interfaces. A joint bundle may be better when the shared receiving use actually requires it; fewer files or a central release number cannot decide the comparison. A pair needing only one interface remains the distinct sufficient-agreement case in §5.2, not the rival used to justify this commons.

The source contributions change particular responsibilities:

| Source and role | Operative move and transfer limit |
| --- | --- |
| OBO Foundry principles supply the selected commons-practice line. | **Adapt** actual users, collaboration, modular reuse, and maintained access in §4.1.1–2/5/8. OBO participation criteria keep their community scope; they do not prescribe the release arrangement of these three organizations. |
| OBO [term stability](https://obofoundry.org/principles/fp-019-term-stability.html) constrains either arrangement. | **Adapt** §4.1.3/6 and §5.1 so a materially changed criterion remains distinguishable from the earlier meaning under the chosen identification rules. **Reject** silent replacement behind a familiar label. |
| OBO [contact responsibility](https://obofoundry.org/principles/fp-011-locus-of-authority.html) supplies a communication contribution. | **Adapt** §4.1.4/7 to a reachable contact and mediation path. Assign content and release rights separately; contact alone establishes neither. |
| OBO [change notice](https://obofoundry.org/principles/fp-013-notification.html) constrains continued reliance. | **Adapt** §4.1.6–7 to actual consumer action and the community agreement. A community-specific notice interval does not settle another commons' timing, and notification does not prove migration. |
| The public [ISO/IEC 21838-1](https://www.iso.org/standard/71954.html) scope supplies a possible common top-level basis. | **Adapt** §4.1.2 only when that basis contributes needed coherence. It decides neither module maintenance nor the release and versioning arrangement compared above. |

Reopen the arrangement comparison when one supported use requires a joint edition that separate compatibility claims cannot economically supply, when a mistaken module-dependency claim breaks a receiving query, or when changed participant rights prevent the selected release path. Reconsider the affected module combination and §4.1.3–7. A new local distinction alone does not require replacing the entire commons.

### SIE.12:12 - Relations

- SIE.3 develops or qualifies module content; SIE.4 establishes correspondences between different meanings.
- SIE.5 retains identifier authority and grain when identity is actually a premise.
- SIE.9 supplies the receiving interfaces that consume shared modules.
- SIE.11 follows material semantic change to affected results and users; SIE.10 supplies their integration validation.
- Domain authorities retain source meanings and claims. ME contributes Method introduction or revision when the community is changing how it works.

### SIE.12:End


# Cross-Pattern Application

## APP-SIE-01 - AP242 and QIF product-lifecycle query

A quality engineer asks: “For released product-definition revision and configuration `R`, which QIF inspection plan and result concern feature `F` at effectivity `E`?” The AP242 and QIF sources use different models and identifiers. SIE may connect their qualified claims; Systems Engineering and authorized quality Work retain configuration, release, applicability, and acceptance decisions.

The application uses the repertoire as follows:

| Contribution | Constructed application result |
| --- | --- |
| `SIE.1` | The constructed contract in SIE.1:5 names the engineer, workflow, answer columns and effectivity. It supplies the 24-hour QIF observation window and two-second response limit and permits qualified evidence with separately visible unresolved local-extension and unknown-unit branches. Authority, negative cases and stops remain explicit. |
| `SIE.2` | A source inventory records AP242:2025 edition 4 at stage 90.92, “to be revised”, the applicable QIF edition, source models, identifiers, configuration/effectivity meanings, owners, and unresolved local extensions. |
| `SIE.3`, when needed | Qualify an existing model, or extend it to distinguish an inspection requirement from an observation of the applicable configured feature. The plan and an observation of another configuration provide counterexamples. |
| `SIE.4` | Correspondence rows distinguish product feature, inspection characteristic, plan applicability, configuration, and result relations; unsupported equivalence and incompatible-feature rows remain explicit. |
| `SIE.5` | Feature and characteristic identities are disposed at the required revision, configuration, and effectivity grain; source identifiers and issuers remain visible. |
| `SIE.6` | AP242 definition/effectivity claims and QIF plan/result claims are composed with source, interval, authority, and conflict branches preserved. |
| `SIE.7` | Executable rules select the released configuration, map accepted endpoint relations, preserve identifiers, reject unsupported joins, and trace every output row to its premises. |
| `SIE.8` | A virtual or hybrid realization is selected against freshness, access, latency, provenance, and recovery rather than because a graph store is preferred. |
| `SIE.9` | The receiving interface returns matched, unmatched, incompatible, stale, and source-error branches with their interpretations and provenance. |
| `SIE.10` | Layered tests cover carrier/schema, source semantics, correspondence, identity/effectivity, composition, transformations, provenance/currentness, quality, and the representative query. SIE.10:5.1 applies the stated freshness, response and partial-answer criteria while keeping excluded branches visible. |

The constructed package returns the contract-permitted qualified row set, with unmatched or incompatible results and the unresolved local-extension and unknown-unit branches visible separately. It stops if configuration/effectivity or feature identity is unresolved, a load-bearing source edition cannot be qualified, a conflict is hidden, or the receiving query fails. It supplies evidence to the applicable `SYSE.7`, `SYSE.13`, `SYSE.14`, or quality owner; it does not choose the released revision or accept the inspection result.

## APP-SIE-02 - Semiconductor identity and traceability

A recall-triage query crosses SEMI device/substrate identifiers, GS1 events, supplier identifiers, and enterprise master data. The package preserves wafer, die, device, package, lot, and event grains. `SIE.5` records same, different, part, version, variant, alternate, or unresolved dispositions with each scheme and issuer. `SIE.6` retains event time, source authority, contradictory events, and absent links. `SIE.10` tests positive, reused-identifier, split/merge, contradictory-event, and missing-link cases.

The interface can return a bounded trace, unresolved branch, or prohibited-disclosure stop. MDM and domain stewards retain authoritative identity and value decisions; quality, safety, and recall authorities retain action.

## APP-SIE-03 - End-to-end quality and provenance

A data pipeline is syntactically healthy, yet an analytic may be unsafe because a source version is stale, a unit conversion is wrong, a default hides absence, a mapping omits one category, or derivation is missing. The contract selects only quality dimensions and thresholds that can change this use. The source manifest and mapping specification expose versions, units, defaults, error branches, and provenance. The claim composition keeps governed inputs and contradictions visible. Validation can return a usable subset, an explicit failure, or an unresolved measurement need.

A mapping that returns 1 millimetre for an input of 1 metre fails the required conversion to 1000 millimetres. That probe can finish a bounded failure; unrelated layers remain unexamined. Conversely, an unchanged JSON field can carry a new future-horizon meaning while the receiver still reads “available now”. Its structural pass cannot preserve the earlier use claim.

For a positive whole-use or permitted subset result, SIE.10 covers every load-bearing premise, including receiving interpretation, with new or matching earlier evidence. Pipeline defects return to Data Engineering, mapping defects to SIE.7, and source defects to their owners. A quality vocabulary or process certificate cannot supply missing evidence for the receiving claim.

## APP-SIE-04 - High-change provider availability without a materialized graph

Two providers expose current availability through governed APIs. One field means “on hand”; the other means “available to promise”. Neither permits replication. The contract requires a purchasing comparison with timestamps and explicit incomplete results. `SIE.4` keeps the meanings distinct and accepts only narrower qualified relations. `SIE.6` composes rows where supported and returns non-comparability otherwise. `SIE.8` excludes copying from the providers' existing prohibition, then selects query-time virtual mappings subject to the receiving latency, trace, and failure conditions. The excluded copying alternative needs no implementation, recovery, or exit design. The interface exposes timeouts, source errors, timestamps, and incompatible rows.

SIE.3 can finish by reusing a model that distinguishes the two quantities, their attribution, unit, time, and horizon. If a provider later changes its promise horizon, SIE.11 finds which mappings and receiving interpretations depend on that meaning; unaffected product descriptions can retain their qualification. The purchasing application decides what to do with incomplete or non-comparable results.

## APP-SIE-05 - A Modular Equipment-Classification Commons

Two manufacturers and a service partner share equipment classes to interpret service observations. Local modules retain product-specific distinctions; qualified correspondences state how they relate to the shared core. SIE.12 identifies the actual users, module scope, dependencies, content and release rights, and contact.

A proposal changes a shared class's criterion from equipment with a replaceable drive to equipment serviced through a replaceable drive module. Examples show which equipment changes classification. The authorized maintainers decide the shared content; the community's identification rules keep the earlier and replacement meanings recoverable. In the worked disposition, the earlier `equip:DriveReplaceable` class keeps its meaning and the new `equip:DriveModuleServiceable` class receives a distinct identifier. SIE.11 follows the change to affected service queries and local correspondences. The service partner's module-planning query adopts the new class: equipment X with only a separately replaceable drive is excluded, while equipment Y with the supported drive-module service arrangement is included. Manufacturer A retains its spare-drive query and matching evidence under the earlier class. The identified release keeps both meanings recoverable and supplies the migration and notice those users need; these two results do not establish every user's migration.

The contact communicates and routes questions. Source owners retain their product descriptions; consumers decide whether a module edition supports their use. Incompatible local criteria can remain in scoped modules with supported correspondences. A pair that needs only one availability interface can finish its model and interface agreement without creating this commons.

# Framework Boundary and Refresh

## Intended use and ordinary non-use

Use this framework when the working result must make separately governed meanings, identities, claims, or representations usable together for a named receiver. Use one pattern or a small cooperating set and stop at the first decision-changing result or honest blocker.

Do not use SIE for local modeling with no cross-source receiving-use question, physical data movement, pipeline operation, one application's schema design, master-data authority, product configuration or release, generic representation choice, or the receiver's operational decision. Obtain those results from their owning practices. A local mapping inside one source can remain local unless it changes a cross-source semantic result.

## PatternID and reader order

`SIE.*` is the Semantic Integration Engineering PatternID namespace. Numbers are stable addresses, not steps or maturity levels. The Table of Contents gives reader order. A dependency names a result needed by one use; it does not require every lower-numbered body to run.

## Supplied pattern repertoire

The complete first edition supplies `SIE.1`–`SIE.12`. The model, change, and commons entries return these domain results:

- `SIE.3 - Construct or Reuse a Semantic Model for a Named Use`: adequate reuse or the semantic development required by a demonstrated gap.
- `SIE.11 - Trace Semantic Change and Revalidate Affected Uses`: direct affected-use results, with a common account when a receiver needs it.
- `SIE.12 - Govern Modular Semantic Commons without Universal Authority`: a working shared-module arrangement for actual users.

A supplied Method guides the work; an inaccessible source, unresolved meaning, missing right, or absent implementation result can still limit a particular use.

## Package anatomy and direct result relations

| Package part | Supplying body or return | Minimum inspectable content |
| --- | --- | --- |
| use contract | `SIE.1` | receiver, use, answer claims, tolerated loss/uncertainty, freshness/latency/quality, authority, representative tests, stop and reopen |
| source manifest | `SIE.2`; SIE.3 qualification when needed | assets, schemes, editions/effectivity, meanings and identifiers used, owners/authority, provenance/access, gaps, and references to required model qualifications |
| correspondence set | `SIE.4` | endpoints, relation or incompatibility, orientation, bounded use, permitted loss, justification/evidence, source versions, counterexamples and unresolved rows |
| cross-source identity disposition | `SIE.5` | load-bearing endpoints, grain and interval, disposition kind, schemes and issuers, evidence, authority boundary, downstream references for the relied-on identity; an explanation of unused identity only when it affects interpretation or later reliance |
| source-qualified claim composition | `SIE.6` | source claims, scope, interval, authority, uncertainty, derivation, relied-on identity premises, comparable/conflicting/non-comparable/unresolved relation, qualified view or explicit conflict |
| mapping specification | `SIE.7` | schemes, accepted semantic inputs, rules, conditions, cardinalities, units/codes, defaults, errors, loss, trace, examples and tests |
| realization and interface | `SIE.8`, `SIE.9` | virtual/materialized/hybrid decision, required implementation result, receiver contract, interpretation, currentness, errors, provenance, access assumptions and return path |
| validation account | `SIE.10` | evidence sufficient for the bounded disposition; every load-bearing layer and required cases for a positive use claim; material unexamined reach, pass/narrow/unresolved/stop, and reopen condition |

`SIE.1 → SIE.2` supplies the use and source cut. `SIE.2 → SIE.3` is conditional. `SIE.2` and any supplied use-fit model feed `SIE.4`–`SIE.6`. `SIE.4` can expose an identity question for `SIE.5` and supplies semantic premises to `SIE.7`. `SIE.5` supplies load-bearing identity premises to `SIE.6`, `SIE.7`, and `SIE.10`. `SIE.6` supplies a qualified composition or explicit conflict branch to `SIE.7` and `SIE.9`. `SIE.7 → SIE.8 → SIE.9 → SIE.10` connects executable semantics to realization, receiver, and bounded validation. SIE.11 revisits only affected reliance, using these dependencies where material. SIE.12 supplies shared-module arrangements when actual users require them. These relations may iterate.

## Pattern selection and first returned result

| Working question | Start or return | First result |
| --- | --- | --- |
| What use and loss boundary govern the integration? | `SIE.1` | `SemanticIntegrationUseContract@Use` |
| What does each source mean and own? | `SIE.2` | `SourceSemanticInventory@Use` |
| Are the available models adequate, or what content must change? | `SIE.3` when adequacy is unsettled | `UseFitSemanticModel@Use` or exact blocker |
| Which endpoints correspond or remain incompatible? | `SIE.4` | `QualifiedCorrespondenceSet@Use` |
| Which identifiers concern the same entity at this grain and interval? | `SIE.5` | `CrossSourceIdentityDisposition@Use` |
| How can governed claims be composed without hiding conflict? | `SIE.6` | `SourceQualifiedClaimFusion@Use` |
| Which executable rules implement the accepted semantics? | `SIE.7` | `ExecutableSemanticMappingSpecification@Use` |
| Should the arrangement be virtual, materialized, or hybrid? | `SIE.8` | `SemanticRealizationDecision@Use` |
| What interface carries the meaning into receiving Work? | `SIE.9` | `ReceivingSemanticInterface@Use` |
| Is the result usable for the named receiver? | `SIE.10` | `SemanticIntegrationValidationAccount@Use` |
| What follows from a changed semantic premise? | `SIE.11` | qualified direct result, scoped gap, or a common affected-use account when needed |
| How should shared semantic modules be maintained? | `SIE.12` for actual commons users | `ModularSemanticCommonsAccount@Community` or exact blocker |

## Source use and currentness

The source contributions guide particular actions and qualifications. Each body states what a source contributes and what remains outside its authority.

| Source family | Contribution used here | Qualification and reopen |
| --- | --- | --- |
| Current FPF | source-local meaning, episteme identity, direct Bridge truth, bounded representation use, claim/provenance reliance, representation transition, currentness and affected-use distinctions | FPF retains the generic concepts and assurance law. A changed relied-on result reopens only its SIE consumer. |
| Current Method Engineering | situational criteria and the separate repertoire, variant, introduction, and revision Methods in `ME.2`, `ME.15`–`ME.17` | SIE supplies domain content; it does not duplicate Method identity or lifecycle decisions. |
| Current Systems Engineering | engineering-description, configuration/effectivity, change, release, integration, and assurance results | SIE can supply a qualified semantic premise; SYSE retains engineering decisions. |
| [ISO 704:2022](https://www.iso.org/standard/79077.html) and [ISO/IEC 11179-3:2023](https://www.iso.org/standard/78915.html) | distinguish objects, concepts, definitions, designations, registry items, versions, and mapping metadata | do not establish cross-source identity, truth, or receiving-use fitness |
| [LOT](https://doi.org/10.1016/j.engappai.2022.104755), [maintained LOT resources](https://github.com/oeg-upm/LOT-resources), and [LOT4KG](https://lot.linkeddata.es/LOT4KG/) | competency/use questions, domain-participant validation, qualified reuse or development, and dependencies between an ontology and a selected graph realization | reuse can finish the model question; LOT4KG's maintained activities do not establish a final peer-reviewed edition or a measured advantage |
| [OWL 2](https://www.w3.org/TR/owl2-overview/) and the public [ISO/IEC 21838-1:2021](https://www.iso.org/standard/71954.html) description | explicit language semantics and profile choices when formalization is useful; a deliberately selected top-level basis when coherence needs it | formal validity does not supply domain adequacy; no universal ontology or full-standard conformance is required or claimed |
| [OBO Foundry principles](https://obofoundry.org/principles/fp-000-summary.html), including [term stability](https://obofoundry.org/principles/fp-019-term-stability.html), [contact responsibility](https://obofoundry.org/principles/fp-011-locus-of-authority.html), and [notification](https://obofoundry.org/principles/fp-013-notification.html) | actual module users, stable identification, scoped shared content, reachable responsibility, and notice of changes affecting reliance | adapt to the particular commons; contact does not itself assign content or release rights, and an OBO-specific notice interval is not universal |
| [SKOS](https://www.w3.org/TR/skos-reference/), [SSSOM 1.0](https://mapping-commons.github.io/sssom/1.0/spec-model/), and [OAEI 2025](https://oaei.ontologymatching.org/2025/results/) | correspondence kinds, reusable mapping metadata, and task-dependent alignment evidence | a label, similarity score, or matcher output remains a candidate premise |
| [ISO 8000-115:2024](https://www.iso.org/standard/88847.html?browse=tc), [PROV-O](https://www.w3.org/TR/prov-o/), [SEMI traceability](https://www.semi.org/en/products-services/standards/traceability), and [GS1 EPCIS 2.0.1](https://ref.gs1.org/standards/epcis/2.0.1/) | identifier-owner/use-restriction inputs, provenance relations, and domain identity/traceability probes | they create no cross-source equivalence, master identity, authoritative value, or receiving action |
| [R2RML](https://www.w3.org/TR/r2rml/), [OMG QVT 1.3](https://www.omg.org/spec/QVT/), and [Ontop](https://ontop-vkg.org/research/publications.html) | bounded executable mapping and virtual/materialized realization forms | no mandatory RDF, MOF, graph store, or source authority |
| [SHACL](https://www.w3.org/TR/shacl/), [DQV](https://www.w3.org/TR/vocab-dqv/), [Data on the Web Best Practices](https://www.w3.org/TR/dwbp/), [ISO/IEC 25012:2008](https://www.iso.org/standard/35736.html), and [ISO 8000-61:2016](https://www.iso.org/standard/63086.html) | distinct validation, quality, provenance/version, and quality-management questions | no one layer or score proves receiving-use adequacy |
| [ISO 10303-242:2025](https://www.iso.org/standard/84300.html?browse=tc) and [ISO 23952:2020](https://www.iso.org/standard/77461.html) | versioned product-definition/configuration and manufacturing-quality source cases | AP242 edition 4 is at stage 90.92, “to be revised”; a changed relied-on successor reopens the affected source, mapping, interface, and case only |

The foundation source cut was qualified on 4 September 2026. The model, evolution, and commons contributions were qualified on 8 September using LOT, the maintained LOT4KG description, OWL 2, and the selected OBO principles. LOT4KG's site cites an under-review manuscript and contains mixed date metadata; its inspected activities supply method guidance rather than proof of a final peer-reviewed edition or measured advantage. The earlier [2024 joint-methodology proposal](https://2024.eswc-conferences.org/wp-content/uploads/2024/05/77770275.pdf) is historical background; its future-work account does not describe the maintained method's current evolution activities. The public ISO/IEC 21838-1:2021 description and stage 90.20 systematic review since 15 July 2026 delimit its use here; no full-standard conformance is claimed. Reopen only choices affected by changed relied-on content or use conditions.

## Related modeling and engineering work

Use SIE for the contribution that makes separately governed meanings usable together. The following working questions locate that contribution and the decisions that remain with neighboring practices.

| Working question | SIE contribution | Boundary retained |
| --- | --- | --- |
| Terminology and ontology across source models | `SIE.2` recovers source meanings, `SIE.3` qualifies or develops model content for an integration use, and `SIE.4` supplies correspondences | generic terminology, ontology, formal science, and local modeling remain with their direct owners |
| A model needed for a receiving integration answer | `SIE.2`, `SIE.3`, `SIE.4`, `SIE.7`, and `SIE.10` apply when the model supplies a named semantic-integration result | local model construction and research remain outside SIE |
| Formal apparatus needed by a semantic mapping or validation | exact formal apparatus may become a source, mapping, or validation premise | formal modeling itself is not an SIE lifecycle |
| Connected engineering descriptions and changed lifecycle information | SIE can return a qualified semantic interface, mapping package, identity/claim result, or affected-use result | SYSE keeps engineering descriptions, configuration, release, assurance, and digital-thread decisions; Data Engineering keeps pipeline operation |

## FPF, neighboring practice, and authority boundaries

FPF owns generic representation, grounding, evidence, source/currentness, identity, comparison, and assurance distinctions. Method Engineering owns Method identity, qualification, trial, fit, worth, repertoire, variant, introduction, and revision. Systems Engineering owns engineered-System, engineering-description, configuration, integration, release, and assurance decisions. Data Engineering owns extraction execution, pipeline/service construction, orchestration, observability, reliability, and recovery. MDM and domain authorities own master identity, authoritative values, survivorship, and domain truth. Applications and operating or decision owners own authorization, risk acceptance, and actual outcomes.

SIE supplies Methods for use-qualified model content, cross-source meanings and correspondences, identity and claim composition, executable mappings, realization, interfaces, validation, changed semantic reliance, and modular commons. Return every non-SIE result to its owner with the exact dependent action.

## Representative case coverage

The five applications are constructed method demonstrations, not evidence of a production integration, product release, recall decision, analytic validity, provider performance, or practical effectiveness.

| Case | What it tests | Boundary for reuse |
| --- | --- | --- |
| AP242/QIF | configuration/effectivity, feature identity, source-qualified composition, mapping, interface, and receiving-use validation | engineering and quality authorities retain release and acceptance; AP242 revision reopens affected premises |
| semiconductor traceability | several identifier schemes, grains, issuers, time, contradiction, and disclosure | MDM/domain and recall authorities retain identity, value, and action |
| quality/provenance | mapping coverage, units, defaults, derivation, currentness, and a representative analytic | Data Engineering and source owners repair their results; quality measures do not decide use alone |
| high-change providers | sufficient model reuse, explicit semantic difference, virtual realization, availability/error branches, changed promise horizon, and non-comparability | providers retain source meanings and permissions; purchasing owns action |
| equipment-classification commons | module boundaries, local correspondences, identification, decision and release rights, semantic change, migration, and notice | contacts communicate; source owners and receiving users retain their respective decisions |

## Edition return

**Semantic Integration Engineering Principles Framework — First Edition, 8 September 2026** designates the source, twelve authoritative pattern bodies, and deterministic carrier of the complete twelve-pattern first edition. The publication supplies practitioner guidance and constructed examples. An implemented service, maintained commons, or receiving decision needs the corresponding actual work and evidence.

## Publication boundary

This publication combines twelve authoritative pattern bodies with the shared reader account. The bodies govern their Methods; the Readme, Preface, applications, Table of Contents, and boundary account help readers find and combine them.

Use an instructional Guide for sequenced learning and memory formation. Use the Engineering DPF Suite Reference for cross-framework discovery. Neither publication replaces the pattern bodies or supplies a missing SIE result.
