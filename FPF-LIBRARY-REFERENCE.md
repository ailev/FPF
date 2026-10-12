# FPF Library Architectural Reference

**Architecture and connected use of the Library's pattern languages**

- **Author:** Anatoly Levenchuk, with AI-assisted development
- **Date:** 12 October 2026
- **Use:** Understand the Library's architecture, select the appropriate level of explanation and preserve the relations between contributions from different fields.
- **Source return:** [FPF Core](FPF-Spec.md), the [domain-framework catalogue](DPFs/README.md) and the full publications linked below.

FPF Library gives people and assisting AI agents a connected language for reasoning about work, constructing useful results and developing better ways to obtain them. Its common distinctions and general Methods meet specialized knowledge in domain frameworks. A reader can use one sufficient contribution directly or follow a larger question across several publications.

This Reference explains how that language is organized and why its boundaries matter. It develops the shared account across individual frameworks: what the larger wholes are, how their contributions connect, which alternatives explain the arrangement and what changes when a relied-on premise changes. The full patterns supply the Methods, cases and source grounds. For practical search and reading, use [Using FPF](USING-FPF.md); the root [Readme](Readme.md) is the short publication entry.

## Contents

- [One connected language, several kinds of whole](#libraryreference1---one-connected-language-several-kinds-of-whole)
- [What the names refer to](#libraryreference2---what-the-names-refer-to)
- [Why general Methods belong in Core](#libraryreference3---why-general-methods-belong-in-core)
- [Why these Suites form useful wholes](#libraryreference4---why-these-suites-form-useful-wholes)
  - [Engineering connects knowledge to functioning systems](#libraryreference41---engineering-connects-knowledge-to-functioning-systems)

  - [Management connects direction to jointly supportable commitments](#libraryreference42---management-connects-direction-to-jointly-supportable-commitments)
  - [Foundational Thinking connects formal constructions and their interpretations](#libraryreference43---foundational-thinking-connects-formal-constructions-and-their-interpretations)
  - [Human Capability Engineering changes the human holder](#libraryreference44---human-capability-engineering-changes-the-human-holders-capabilities)

- [Why some DPFs stand outside the Suites](#libraryreference5---why-some-dpfs-stand-outside-the-suites)
- [Several relations, not one hierarchy](#libraryreference6---several-relations-not-one-hierarchy)
- [How the language makes connected work intelligible](#libraryreference7---how-the-language-makes-connected-work-intelligible)
- [A worked connection across the Library](#libraryreference8---a-worked-connection-across-the-library)
  - [Different contributions to one useful result](#libraryreference81---different-contributions-to-one-useful-result)
  - [What a changed condition sends back](#libraryreference82---what-a-changed-condition-sends-back)
- [Open-ended development belongs across these fields](#libraryreference9---open-ended-development-belongs-across-these-fields)
- [What justifies another pattern, DPF, Suite or LPF](#libraryreference10---what-justifies-another-pattern-dpf-suite-or-lpf)
- [Publications, access and changes of boundary](#libraryreference11---publications-access-and-changes-of-boundary)
- [The Library and its wider ecosystem](#libraryreference12---the-library-and-its-wider-ecosystem)

## Library.Reference:1 - One connected language, several kinds of whole

The Library becomes useful when a question crosses boundaries that an isolated answer leaves unresolved. A sound model may be unusable with the available observations. A feasible design may lack an authorized commitment. A helpful AI answer may leave the person unable to make the next judgement independently. In each case, the missing contribution has to be identified and connected to the work that consumes it.

The common language makes these differences expressible. Core distinguishes a System, a Method, its description, performed Work, capability, evidence and authority. The domain languages explain what those distinctions require in particular practices. A mathematical consequence, a corporate decision and an acquired bodily skill therefore retain different construction and qualification conditions while participating in one undertaking.

FPF Library is an organized collection of related framework publications with this connected public account. Its unity of description comes from shared meanings, general Methods, explicit dependencies and developed returns between contributions. That does not establish one discipline above every field in the collection. A Library-wide explanation can be necessary even when the explained publications describe several independently constituted disciplines.

Within the Library, a Suite makes a stronger subject claim: it describes a composite discipline through constituent DPFs and their connections. Engineering, Management, Foundational Thinking and Human Capability Engineering each have an account of that whole. A DPF outside those Suites keeps its own subject; its Methods can supply contributions to the same work. Neither arrangement determines how many publications a particular task needs.

This distinction follows [E.4's ecosystem architecture](FPF-Spec.md#e4---fpf-ecosystem-architecture-framework-families-products-and-dpf-suites) and [C.20's construction of a discipline](FPF-Spec.md#c204---solution---recover-the-whole-from-direct-construction). The requirement for a shared explanation, including alternatives, whole conditions and worked connections, comes from [E.11.PFP:4.7](FPF-Spec.md#e11pfp47---explain-the-methods-at-each-selected-scale).

## Library.Reference:2 - What the names refer to

The same word can name a field, a framework about it or a file. Keep the subject of the claim recoverable before relying on its name.

| Object | What it contributes to this architecture | What a change affects |
| --- | --- | --- |
| Domain | A subject area used to frame a question or organize material. | A revised boundary changes what the designation covers; it does not by itself constitute a discipline. |
| Discipline | A whole of knowledge and reusable practice, with actual constituent relations and a way those contributions constrain and revise one another. | Changes to knowledge, Methods or institutions can preserve the field when its essential connections and continuity conditions remain. |
| Principle framework | An account of recurring situations, problems, forces, Methods, cases, consequences and their relations, expressed as a pattern language. | A revised account can improve the description or change its field promise. |
| Framework edition | An identified body of framework claims about its subject under its reference scheme. In FPF terms, an episteme. | A change in the claims or effective reference scheme identifies another episteme; its continuity and compatibility with earlier editions require their own grounds. |
| DPF Suite | A larger domain framework describing a composite discipline through constituent DPFs and any justified whole-level patterns. | A constituent or connection changes the described whole only under the relevant discipline conditions; editorial inclusion alone supplies no parthood. |
| Product series | A continuing collection of editions under declared admission and reidentification rules. | Admission, retirement and continuity concern the publishing series, separately from the described discipline. |
| Publication carrier and access route | A file, site, rendering or service through which a reader obtains the content. | Availability, layout or retrieval can change while the described Method remains the same. |

These distinctions are developed in [C.20:4.6](FPF-Spec.md#c2046---keep-neighboring-objects-with-their-subject-patterns), [E.4:4.1](FPF-Spec.md#e441---place-support-units-and-adjacent-products-deliberately) and [E.4:4.2](FPF-Spec.md#e442---describe-a-composite-discipline-with-a-dpf-suite). They prevent a practical error: moving a file, giving a publication a name or admitting an edition cannot supply a missing methodological contribution.

A pattern is also distinct from the Method it explains. The text may help a reader perform, criticize or adapt a way of working. The occurrence of that work and its actual result need their own basis. [A.3.1](FPF-Spec.md#a31---umethod-reusable-way-of-doing-with-explicit-applicability) and [A.3.2](FPF-Spec.md#a32---umethoddescription-description-episteme-for-a-way-of-doing) retain that distinction; [A.15.1](FPF-Spec.md#a151---uwork-dated-performed-work-occurrence) supplies the account of performed Work.

## Library.Reference:3 - Why general Methods belong in Core

[FPF Core](FPF-Spec.md) contains both common conceptual distinctions and developed transdisciplinary Methods. Its Kernel is the subset that defines universal meta-concepts and the rules for their meanings and relations. Core also explains how to investigate a question, construct and combine Methods, compare arrangements, qualify claims, make decisions and continue development. The Kernel is not the whole of Core.

The placement question turns on what an operation requires. Constructing a Method from interacting contributions, comparing its performance and provision, or deciding which questions a checklist must answer can apply across fields without importing one field's substantive mechanism. These general constructions belong with their shared conditions in Core. Repeated domain copies add a duty to keep the same general construction consistent.

For example, [C.32.MWA.PP](FPF-Spec.md#c32mwapp---construct-and-compare-method-performance-and-provision-arrangements) constructs and compares complete performance and provision arrangements. [A.15.8.MS](FPF-Spec.md#a158ms---configure-methodological-support-for-work) configures the methodological support that actual work needs. [C.41 and its connected patterns](FPF-Spec.md#c41---select-checklist-questions-for-a-work-result) distinguish selecting checklist questions, making their reusable expression, fitting an occasion, obtaining grounded answers, reconciling shared uses and qualifying the checking means. These remain several Methods with different results, rather than one compulsory checklist process. [E.8.ML](FPF-Spec.md#e8ml---construct-a-pattern-language-for-connected-methods) explains the construction of a pattern language for connected Methods.

Wide applicability alone does not justify Core placement. Mathematical Modeling constructs correspondences, transformations and mathematical consequences under mathematical premises. Research Method Practice reconstructs practice and investigates competing accounts under inquiry-specific evidence conditions. Organization Change Engineering constructs contribution, information, assignment and authority arrangements in an organization whose work continues. The common idea of improving a method does not teach those specialized operations.

The architecture therefore keeps a general construction once and gives its specialized realization an explicit supplier. The test is whether the full operation and its conditions survive a change of subject, and what domain knowledge still has to be supplied. An abstract object, a broad title or use by many professions cannot settle that test. [E.4.PFAD](FPF-Spec.md#e4pfad---principle-framework-architecture-decision) compares the actual contributions and their organization; [E.4.CM](FPF-Spec.md#e4cm---develop-connected-methods-as-framework-contributions) distinguishes an already explained connection from a missing reusable Method.

## Library.Reference:4 - Why these Suites form useful wholes

A Suite describes a field whose knowledge and reusable practices form a larger whole. Its constituent languages remain usable independently, but the Suite also explains the consequential connections: what one contribution constrains, what result another consumes, how failure returns to an affected premise and which substitutions preserve the whole. The four Suites below cover selected portions of their fields, not every practice associated with their broad names. Their subjects and knowledge-practice connections, rather than the current number of files, establish the boundaries.

### Library.Reference:4.1 - Engineering connects knowledge to functioning systems

The [Engineering Suite](DPFs/Engineering%20DPF%20Suite/README.md) is organized around designing, realizing, changing and sustaining functioning systems. This edition directly assembles Systems Engineering, Maintenance Engineering and Management, Knowledge-Corpus Access Engineering and Semantic Integration Engineering. Management describes the organizational specialization, including OCE, and Human Capability Engineering describes the human specialization in §4.4. Their separate Suite editions retain their engineering subjects while making the corresponding specialized knowledge and practices available in full.

Direct constituents and specialized contributions can constrain the same realization. An attainable operator capability can change automation. A maintenance condition can change a design. The meanings carried across an information interface must remain usable in the receiving operation. Organizational authority and protected practice time can determine whether a new way of working becomes possible while existing obligations continue. Qualification and later use can reopen the knowledge or design on which those arrangements depended.

Engineering includes discovering and reformulating the problem, not only executing a settled specification. A particular task can finish with an adequate analysis, design or justified no-change recommendation; a claim that a system actually changed requires that result. Similarly, HCD's engineering contribution concerns constructed and qualified capability development. The fact that all thinking and learning have physical bearers does not make every intellectual or learning activity engineering.

The [Engineering Reference](DPFs/Engineering%20DPF%20Suite/ENGINEERING-DPF-SUITE-REFERENCE.md) explains selected combinations and the external contributions they need. An asset valuation, a research finding or a management commitment can be indispensable without bringing its whole discipline into Engineering.

### Library.Reference:4.2 - Management connects direction to jointly supportable commitments

The [Management Suite](DPFs/Management%20DPF%20Suite/README.md) concerns directing and sustaining joint activity through worthwhile direction, legitimate and feasible commitments, provision, performance and warranted reconsideration. Its eleven constituent languages are Strategy, Operations Management, Organization Administration, Corporate Governance, Management Accounting, Corporate Finance, Marketing, Engineering Asset Management, Leadership, Community Management and Organization Change Engineering.

A customer promise constrains operating work. Capacity and existing obligations constrain the promise. Resource and monetary accounts connect that work to funding choices. Authority determines which proposed act can become effective. Participation conditions determine which contributions can actually be relied on. A locally sound answer can therefore fail in the whole: the budget, schedule and promise may depend on the same unavailable resource or on an agreement that has not been made.

The composite contribution is a jointly supportable management arrangement, with a return from actual performance to the premise that needs reconsideration. The same construction accommodates a business, public service, temporary collaboration or voluntary community. Corporate Finance and Corporate Governance retain their corporate conditions; membership of the Suite does not impose those conditions on every undertaking.

For an organization as the target system, management specializes the construction and sustained functioning of organized joint work: authority, interests, commitments and resources have their own substantive conditions. A changed allocation or operating commitment can change the organization's state without redesigning its architecture. Management is therefore not separated from engineering by an alleged absence of system change. It also receives independently useful results from other disciplines. A voluntary population or network is not automatically one organization or capability holder; the relevant whole and authority must be established for that use.

Organization Change Engineering belongs directly to Management: organizational constructions constrain feasible commitments, and changed commitments can require another arrangement. Maintenance Engineering and Management belongs directly to Engineering: failure and condition knowledge, maintenance policy, provision and intervention connect to sustained functioning; later functioning can reopen them. Management practitioners can apply the full maintenance Methods themselves or obtain their results. This preserves the technical and management connections inside MNT without making its complete field an additional Management constituent. Each complete language has one home in its respective Suite.

### Library.Reference:4.3 - Foundational Thinking connects formal constructions and their interpretations

The [Foundational Thinking Suite](DPFs/Foundational%20Thinking%20DPF%20Suite/README.md) connects Mathematical Thinking, Mathematical Modeling, Physical Thinking, Computational Thinking and Notational Engineering. These Methods can produce new objects, explanations, correspondences, algorithms and languages, as well as use existing ones. A subject difficulty can call for a new formal construction; a formal construction can open a new subject question.

A physical account constrains admissible model relations. Mathematical construction derives consequences. An algorithm must obtain the required answer within its resource and interaction conditions. Modelling connects that answer back to the subject question; notation keeps the distinctions operable and their changes recoverable. The whole makes a consequence jointly interpretable and revisable while retaining its separate mathematical, physical, computational and expressive grounds.

An observational mismatch can reopen an idealization; computing the same model more accurately does not repair that premise. A numerical error can require an algorithmic correction without invalidating the physical account. These different returns are part of the field's construction. The [Foundational Thinking Reference](DPFs/Foundational%20Thinking%20DPF%20Suite/FOUNDATIONAL-THINKING-DPF-SUITE-REFERENCE.md) explains such connections.

The name does not designate all thinking or a universal learning sequence. A pure mathematical result can be complete without a physical application. Explanation Design, Research Method Practice and Narrativization have other subjects and remain independent suppliers. Their use of mathematics or notation does not absorb their full fields into this Suite.

### Library.Reference:4.4 - Human Capability Engineering changes the human holder's capabilities

The [Human Capability Engineering Suite](DPFs/Human%20Capability%20Engineering%20DPF%20Suite/README.md) concerns forming, changing, restoring and maintaining what a human holder can do. Human designates the target of the change, not necessarily its performer. A human teacher, an organization or suitable AI assistance may contribute; the resulting capability claim still concerns the person. The first edition connects the full Human Capability Development and Somatic Movement Modeling languages.

HCD connects later Work, the person's starting evidence, programme alternatives, practice, provision and qualification. SOM supplies the bodily distinctions, regulation and coordination needed for its movement-learning branch. Their results constrain one another: a programme cannot supply a missing coordination by listing it, and a local movement exercise does not establish performance of the whole task. A dancer may have adequate strength, a stationary axis and a remembered figure while lacking coordination during rotation. The two languages connect the missing bodily contribution to whole-task practice, variation, transfer and retention, rather than treating separate successful exercises as a complete result.

This is a capability-engineering synthesis with limited present coverage. It does not claim all medicine, psychology, personality change or personal management, and it does not imply that these questions are reducible to teaching. When physiological, clinical, motivational or other mechanisms are necessary, their substantive Methods and qualified provision must be obtained. The current two DPFs are the available part of the field, not a reason to close its boundary around the files already written.

The qualification Capability distinguishes this target from the human–system interaction studied in ergonomics. A bounded capability change also differs from open-ended development. The [Human Capability Engineering Reference](DPFs/Human%20Capability%20Engineering%20DPF%20Suite/HUMAN-CAPABILITY-ENGINEERING-DPF-SUITE-REFERENCE.md) explains the field, alternatives, available constructions and limits. An assisted answer can satisfy an immediate need without changing the person; acquiring a capability can finish while a wider open-ended development undertaking continues.

## Library.Reference:5 - Why some DPFs stand outside the Suites

A standalone DPF is an independently usable domain language whose own subject and useful results warrant its boundary, without a demonstrated constituent relation to one of the described assemblies in this Library edition. It is not a lesser framework or an item waiting for a folder to complete a classification.

The ten standalone languages have the following distinct contributions:

| DPF | Contribution that retains its own boundary |
| --- | --- |
| [Decision Design](DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md) | Constructing a decision situation, ends and possible means, alternatives, consequence and uncertainty accounts and warranted recommendations, together with the engagement, participation and facilitation that make them usable. |
| [Research Method Practice](DPFs/RESEARCH-METHOD-PRACTICE-PRINCIPLES-FRAMEWORK.md) | Inquiry and criticized knowledge contributions, including source recovery, observation, research design and evidence limits. |
| [Explanation Design](DPFs/EXPLANATION-DESIGN-PRINCIPLES-FRAMEWORK.md) | Making warranted relations recoverable and usable by an intended recipient. |
| [Narrativization and Narrative Studies](DPFs/Narrativization-and-Narrative-Studies-Principles-Framework.md) | Constructing and examining followable narratives with purpose, viewpoint, arrangement and recoverable source relations. |
| [Implementation Facilitation](DPFs/IMPLEMENTATION-FACILITATION-PRINCIPLES-FRAMEWORK.md) | Agreeing, constructing, adapting and continuing facilitation through which participants make an interpretable practice workable under actual conditions, including brokerage and their further facilitation capability. |
| [Financial Domain Modeling](DPFs/FINANCIAL-DOMAIN-MODELING-PRINCIPLES-FRAMEWORK.md) | Financial parties, positions, rights, obligations, events and flows with their domain meanings. |
| [Economic Reasoning and Coordination](DPFs/ECONOMIC-REASONING-AND-COORDINATION-PRINCIPLES-FRAMEWORK.md) | Scarcity, incentives, exchange, commitments, institutions and coordination under economic conditions. |
| [Defense and Transmission Modeling](DPFs/DEFENSE-AND-TRANSMISSION-MODELING-DPF.md) | Transmission, reconstruction, variants, selection, protection and consequential feedback. |
| [Music and Dance Practice Engineering](DPFs/MUSIC-AND-DANCE-PRACTICE-ENGINEERING-PRINCIPLES-FRAMEWORK.md) | Musical and dance creation, performance, learning, transmission and cultural continuation, including engineered performing configurations and changes to their supporting environment. |
| [Embodied Rhythmics](DPFs/EMBODIED-RHYTHMICS-PRINCIPLES-FRAMEWORK.md) | Performed rhythmic relations, their representation, transformation, coordination, practice and observation. |

Within Decision Design, construction of alternatives and professional engagement have different completion conditions. A sound comparison can exist while representation, consent or the conditions for useful advice remain unresolved. Conversely, a well-conducted engagement does not supply a missing mathematical or empirical argument. One language keeps these Methods independently selectable while explaining their necessary connections. Its warranted recommendation is not the authorized choice, implementation of that choice, or engineering of an operational decision service.

Narrativization supplies another case. A narrative can serve inquiry, management, teaching or artistic practice, but its purposes and viewpoint choices are not exhausted by any of those uses. Putting it under every consuming field would confuse use with composition. Leaving it standalone preserves the whole narrative question and its returns to source.

Standalone placement is open to substantive revision. A newly established larger discipline could include a field under [C.20](FPF-Spec.md#c20---composition-of-udiscipline-discipline-cal); a changed problem family could justify repartition.

## Library.Reference:6 - Several relations, not one hierarchy

The Library uses several structures at once. Their relations answer different questions.

| Relation | Architectural consequence | Example |
| --- | --- | --- |
| Discipline parthood | A constituent contributes to the continuing practice-and-knowledge assembly described by a Suite. | Maintenance knowledge and intervention practice participate in Engineering's account of sustained functioning. |
| Method composition | Constituent Methods together obtain the result of a larger Method under their joint conditions. | A way of answering a decision question can combine Methods for obtaining observations, interpreting them and comparing alternatives. |
| Specialization | An inherited construction is developed under additional subject conditions. | Somatic Movement Modeling gives bodily sensing and coordination constructions within human capability development. |
| Supplying use | One Method's result is consumed by another operation under stated conditions. | An engineering choice receives a financial constraint without absorbing Corporate Finance. |
| Framework dependency | A framework relies on claims or Methods in an identified supplying edition. | A domain language uses Core's distinction between capability, assignment and performed Work. |
| Publication assembly | Selected complete descriptions are included with their entries and source returns. | OCE has its full home in the Management Suite and MNT in the Engineering Suite; uses from elsewhere return to those same complete descriptions. |

Discipline parthood is established for the field, Method parthood for the way of working, and Work containment for performed activity. A project's participants and timetable do not establish any of these other relations. [C.32.MWA](FPF-Spec.md#c32mwa---synthesize-an-architecture-account-of-methods-and-their-use) helps recover the Method, Work, capability and provision structures when they do not correspond one-for-one.

The directory tree supplies an unambiguous home for full descriptions. It does not turn all semantic relations into a tree. A claim of multiple disciplinary parthood needs grounds for each assembly; repeated usefulness is insufficient. Nor does a graph with several parents automatically form a mathematical lattice. A formal model requires its selected elements, relation and mathematical properties, as [E.11.PFP:4.7](FPF-Spec.md#e11pfp47---explain-the-methods-at-each-selected-scale) explains.

OCE's organizational construction participates in the Management whole, a specialization of engineering. A management undertaking can also use MNT's full policy or programme Method while maintenance remains a constituent of the broader Engineering edition. In that use the manager can perform the Method: the supplying discipline need not be represented by a different person. Corporate Finance can similarly supply a constraint to an engineering project without that use establishing its whole field as an Engineering constituent. The subject and the relation of the complete field to the whole decide composition; a useful connection alone does not.

The transformed object also differs from the performer and recipient. Replacing a teacher with an AI assistant can leave the human-learning target unchanged. Replacing the learner with a robot changes the target and can require different learning and control Methods. A shared input/output signature does not supply those bodies. Replacing an instrument can change motor demands and attainable musical material; changing listeners or cultural selection can change what is retained for other reasons. The complete MDPE.20 account preserves these distinct mechanisms. The general constructions remain in Core; the bodies that depend on a particular target and mechanism remain with their substantive fields.

## Library.Reference:7 - How the language makes connected work intelligible

The Library's pattern languages are declarative. Their order of publication does not prescribe a project process. A current question selects a relevant contribution; a real dependency requires another result only when the selected operation cannot proceed without it. Existing adequate results can let the reader enter farther along the connection.

The useful connection is more specific than a sequence of titles. A supplying Method returns something of an identified kind, a receiving operation uses it, and the conditions on that result remain available at the join. A model with an error bound may support one decision but not another. A proposed contribution needs agreement and authority before it can be relied on as a commitment. An observed successful run can support a bounded performance claim while leaving transfer or independent capability open.

[C.39](FPF-Spec.md#c39---find-and-develop-a-way-to-obtain-a-result) starts from the result needed by the receiving work and develops a missing way where necessary. [E.4.CM](FPF-Spec.md#e4cm---develop-connected-methods-as-framework-contributions) distinguishes a genuine missing Method or connection from an adequate contribution whose explanation or access needs repair. The larger public accounts make those connections understandable; the bodies supply the developed operations. A link to a related topic cannot fill an unwritten operation.

There is also a connection within ongoing work. While someone checks the units in a calculation, that action can be part of obtaining a model result, comparing a design and supporting a larger engineering decision at the same moment. The encompassing purpose determines which distinctions the check must preserve. [B.1.5.EW](FPF-Spec.md#b15ew---recover-how-constituent-actions-enact-encompassing-work) recovers this constituent-to-whole connection; [B.1.5.RS](FPF-Spec.md#b15rs---evaluate-a-constituent-method-replacement-in-its-encompassing-uses) examines a proposed replacement in its encompassing uses. A missing intermediate capability or unavailable shared resource can defeat the whole even when elementary operations are individually available.

This account applies to human, AI and mixed arrangements. A supplied result and the recipient's own mastery are different goals. [C.32.MWA.PP](FPF-Spec.md#c32mwapp---construct-and-compare-method-performance-and-provision-arrangements) compares complete arrangements, including coordination, checking, waiting and correction; [C.11.DUA](FPF-Spec.md#c11dua---make-advice-and-evidence-demands-worth-their-burden) keeps an additional inquiry or check proportionate to what it could change. Assignment and permission remain separate from capability. The Library supplies ways to reason about the arrangement; the actual situation supplies its facts, powers and available performers.

## Library.Reference:8 - A worked connection across the Library

The following constructed case illustrates the architecture. It is not a model of every laboratory or a required sequence of Methods.

Three laboratories want a more dependable diagnostic measurement practice. An existing calculation works for familiar specimens but gives unexplained disagreements for a new class. The groups also want practitioners to handle further unfamiliar cases. They are considering better source access, an external specialist service, a shared support office and local provision coordinated by their leads.

### Library.Reference:8.1 - Different contributions to one useful result

The intended results already reveal several subjects. A functioning measurement arrangement is an engineering result. An explanation of the discrepancy is a knowledge result. A practitioner's ability to recognize and investigate a new case is a capability result. A feasible agreement about contributions is a management result. None can be inferred merely from completion of another.

[Decision Design](DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md) helps construct the question and compare alternatives without assuming at the outset that the answer is an office or a course. [Research Method Practice](DPFs/RESEARCH-METHOD-PRACTICE-PRINCIPLES-FRAMEWORK.md) supplies inquiry when existing knowledge cannot explain the disagreement. If the issue is a model premise, [Foundational Thinking](DPFs/Foundational%20Thinking%20DPF%20Suite/README.md) connects physical explanation, model correspondence and calculation. A faster or more accurate computation of the same inadequate model does not resolve that premise.

The resulting explanation changes what must be obtained. If a usable method already exists and the only defect is access, [Implementation Facilitation](DPFs/IMPLEMENTATION-FACILITATION-PRINCIPLES-FRAMEWORK.md) can supply the missing help. If the desired result is each practitioner's independent judgement, external answers alone are insufficient; [Human Capability Development](DPFs/Human%20Capability%20Engineering%20DPF%20Suite/HUMAN-CAPABILITY-DEVELOPMENT-PRINCIPLES-FRAMEWORK.md) supplies the relevant learning and capability qualification. When organizational contributions or authority must change, [Organization Change Engineering](DPFs/Management%20DPF%20Suite/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md) constructs that realization while ongoing obligations remain in view.

The office alternatives concern how these transformations will be performed and supported. [C.32.MWA.PP](FPF-Spec.md#c32mwapp---construct-and-compare-method-performance-and-provision-arrangements) compares their complete performance and provision. A common office for several masteries is a serious alternative when the same contribution can serve them without erasing their different criteria, and the gain from sharing exceeds the extra coordination and interpretation burden. Specialized development support has a case when it supplies methodological inquiry that each workplace lacks while receiving subject expertise from the laboratories. Local leadership, distributed specialists or external provision can be sufficient when those arrangements supply the whole needed contribution under attainable conditions. A label such as common, specialized or AI-assisted establishes none of that sufficiency.

[STR.16](DPFs/Management%20DPF%20Suite/STRATEGY-PRINCIPLES-FRAMEWORK.md#str16---construct-a-feasible-portfolio-with-shared-or-branch-specific-support) compares shared and branch-specific support while preserving each branch's purpose. [LDR.2](DPFs/Management%20DPF%20Suite/LEADERSHIP-PRINCIPLES-FRAMEWORK.md#ldr2---agree-feasible-joint-contributions) obtains responses to a feasible joint proposal. Where independent groups require a common mandate, [CB.13](DPFs/Management%20DPF%20Suite/COMMUNITY-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#cb13---establish-a-workable-mandate-for-shared-decisions) supplies that contribution; the participants retain powers they have not delegated.

Suppose one qualified specialist has eight available hours in the relevant week and each of two distinct activities requires five hours of that specialist's time, including preparation and return. Each activity is individually feasible; the pair needs ten hours. Shared administration does not supply the missing two hours. Different timing, a qualified substitute or a smaller promise can make a different arrangement feasible. The choice depends on which change preserves the required result, not on the number of offices or participants. This is a condition on the whole combination, not a defect in either local Method.

### Library.Reference:8.2 - What a changed condition sends back

If the new specimen class defeats an assumption in the model, the return is to that assumption and its dependent conclusions. If the model remains adequate but the specialist withdraws, the return is to provision and commitments. If the service delivers good answers but practitioners still cannot investigate unfamiliar cases, the missing result is their capability; repeating the service's success does not answer that question. If the scientific result is adequate but its explanation cannot be used at the workplace, [Explanation Design](DPFs/EXPLANATION-DESIGN-PRINCIPLES-FRAMEWORK.md) supplies the recipient-relative construction.

These branches show why the Library retains different languages. Research retains its independently useful knowledge result and its own field boundary when this engineering work uses it. Reclassifying every useful supplier as a Management constituent would obscure its own field. Copying their descriptions into a new office framework would add duplication without supplying the missing connection. The existing Methods instead preserve the changed premise, the receiving action and the relevant return.

Once the practice works adequately, one branch can finish. The new understanding may reveal a harder but attainable problem, such as recognizing an unfamiliar failure before it affects a measurement. [C.40.NP](FPF-Spec.md#c40np---continue-from-a-result-to-new-attainable-problems) develops that continuation. If several independent practitioners need to reconstruct and adapt the method, [C.36.RP](FPF-Spec.md#c36rp---sustain-and-renew-shared-ways-of-working) supplies cultural retention and renewal, with [Community Management](DPFs/Management%20DPF%20Suite/COMMUNITY-MANAGEMENT-PRINCIPLES-FRAMEWORK.md) where participation or common work needs organizing. Neither a permanent office nor an endlessly open project is required by that continuation.

The same architecture can serve a question that has no laboratory or system-realization goal. A mathematical investigation may finish with a warranted construction; a narrative may finish with a source-faithful account suited to its purpose. The example explains relations among contributions, not a boundary around the Library's possible uses.

## Library.Reference:9 - Open-ended development belongs across these fields

Open-ended development expands knowledge, understanding and reproducible ways of obtaining results, then uses that changed starting position to open further worthwhile and attainable problems. The novelty can be new to a person, organization or community without being new to humanity. An adequate knowledge contribution can matter before all prospective applications have been realized.

The general connection is developed in [C.40.OD](FPF-Spec.md#c40od---construct-and-continue-open-ended-development), [C.40.JD](FPF-Spec.md#c40jd---develop-a-way-its-holder-and-its-provision-together) and [C.40.NP](FPF-Spec.md#c40np---continue-from-a-result-to-new-attainable-problems). They connect a consequential difficulty, problematisation, a useful direction, construction of a way, its holder and provision, application and the next possibility. They keep the branch that supplies an immediate result distinct from the branch that develops a performer's capability and the branch that develops the Method itself.

That construction is transdisciplinary. It can concern a person, organization, AI system or distributed cultural carriers while requiring different mechanisms in each case. HCD explains human practice, feedback and transfer. OCE explains organizational realization and authority. RMP explains research. Community Management explains participation where a common undertaking exists. An executable learning system also needs its own challenge representations, learning and transfer mechanisms; the general development account is not their implementation.

The general construction remains incomplete for a concrete use until its needed subject mechanisms are supplied. Keeping those mechanisms in their domain languages preserves their distinct premises, evidence and revision. Putting the general connection inside one domain framework would make a common Method depend on that field. Keeping only scattered citations would leave the reader to invent how a sufficient result opens the next problem. The selected architecture develops the common connection in Core and retains its subject-specific suppliers.

Repeated delivery, a new version or a higher current score alone does not establish this continuation. Nor can a finite observation demonstrate an infinite future. The useful claim concerns the growth actually obtained, the problems it enables and the conditions supporting further development. A bounded service or project can end while its result supports that wider practice.

## Library.Reference:10 - What justifies another pattern, DPF, Suite or LPF

The Library's boundaries follow useful constructions and their subjects. A new topic or an awkward folder location is a reason to inspect the architecture, not a sufficient reason for another framework.

[E.4.DPF](FPF-Spec.md#e4dpf---domain-and-local-principle-frameworks-whether-and-how-to-author-and-publish) and [E.4.PFAD](FPF-Spec.md#e4pfad---principle-framework-architecture-decision) compare the recurring problems, available full Methods, their connections and the independently useful result. That comparison can retain an adequate supplier, improve its explanation, add a missing Method, regroup a developed field or identify another field. Existing elementary operations do not prevent a new composition; a useful summary does not establish one.

| Proposed contribution | What gives it the corresponding boundary |
| --- | --- |
| A new or revised pattern | A recurring problem and reproducible construction with its own useful result, conditions and cases; an existing owner is preferable when the addition completes that owner's promised result. |
| A DPF | A coherent domain problem family with constructive Methods, a usable first field account, domain knowledge and evidence practice, and a justified boundary for later change. |
| A DPF Suite | A composite discipline established through C.20, constituent DPFs and developed whole connections; more patterns or more cited suppliers do not supply that construction. |
| An LPF | Guidance for a bounded local practice, such as an organization, project, tool arrangement or practitioner setting, using applicable Core and domain contributions under its actual local conditions. |
| An Architectural Reference | A needed public account of an existing whole, its architecture, alternatives, connections and returns. The underlying Methods remain developed at their substantive owners. |
| A pedagogical companion or tool | Learning support or an operational means of access, calculation or checking with its own intended use and limits. |

An LPF can select local responsibilities, tools and working arrangements without turning those choices into universal rules. A domain framework can receive an existing Method or split into better field descriptions; novelty of every operation is not the test of its identity. A proposed Suite must explain the larger field's actual knowledge-practice coupling and its continuity through permissible changes.

The consequential comparison is what each boundary changes in obtaining, understanding, adapting and maintaining a useful result. Shared content can reduce duplicate explanation while increasing reliance on access and compatible sources. Independent variants can preserve necessary differences at the cost of maintaining them. A new framework is warranted when its field and useful whole justify that burden, not merely when a name is available.

## Library.Reference:11 - Publications, access and changes of boundary

The public arrangement gives Core its full home in [FPF-Spec.md](FPF-Spec.md). The [DPFs catalogue](DPFs/README.md) locates four Suite folders and ten standalone DPFs. Engineering has four direct constituent descriptions, Management eleven, Foundational Thinking five and Human Capability Engineering two: together with the ten standalone languages, these are thirty-two distinct DPF descriptions. OCE has its full home in Management and MNT in Engineering; neither is directly included in both Suites. Each Suite has its own entry and Architectural Reference and identifies every full description it includes. This root Reference carries the Library-wide explanation. Each complete supplying text has an identifiable public home; this arrangement is a publication view of the richer relations described above.

For connected use, the receiving arrangement needs the full relevant texts, including external suppliers. A Suite directory is not necessarily a self-contained distribution: its constituent descriptions can rely on Core, specialized Suites and outside suppliers. A link names a destination; usable access requires that the reader or assisting agent can obtain its relevant explanation. [Using FPF](USING-FPF.md) supplies the ordinary search and reading method. An unavailable source narrows the supported answer until the required contribution can be recovered.

The README provides a short entry. The whole-language account explains the framework's subject, construction, relations and alternatives. That account can be embedded in the same publication as its patterns or carried separately; its explanatory responsibility is the same. Each publication's table of contents locates its whole-language account. Full pattern bodies supply separately selectable Methods. A reader may enter at any of these levels when the needed conditions remain recoverable.

Current use and a reproducible comparison also have different needs. An ordinary application needs an adequate current source and its use conditions. A comparison between editions needs the identified sources whose changes could affect the conclusion. Publication date, a stable filename and a successful retrieval are not substitutes for those content conditions.

When a framework boundary changes, preserve the complete useful constructions and return to their actual supplying bodies. Distinguish a corrected description of the field from a change to the field itself, and both from a layout or access change. [E.4.PFIP](FPF-Spec.md#e4pfip---principle-framework-publication-integration-and-preservation) governs preservation across reconstructed publications; [E.4.PFR](FPF-Spec.md#e4pfr---pattern-framework-relation-and-edition-discipline) handles relied-on edition relations. A reference to a successor title is insufficient if the operation, conditions or receiving use have disappeared.

The affected answer is reopened where its premise changed. A revised mathematical assumption can change a comparison while leaving the authority arrangement intact; an unavailable provider can change realization without defeating retained knowledge. [C.39.MC](FPF-Spec.md#c39mc---continue-method-development-from-changed-conditions) develops methodological continuation from changed conditions, and [G.11](FPF-Spec.md#g11---decide-whether-and-how-to-refresh-sota-packs-and-related-results-telemetry-and-decay) supplies the source-currentness question when reliance requires it.

## Library.Reference:12 - The Library and its wider ecosystem

FPF Library is the project's publication collection. The wider FPF ecosystem also includes other authors' domain and local frameworks, teaching materials, tools, services and the people and organizations that use and maintain them. A common conceptual dependency does not put all of these products inside the Library or give them one publication or maintenance responsibility.

This distinction lets the public Methods remain complete without making every useful learning arrangement part of the Library. A pedagogical companion can sequence practice, give feedback or adapt material for an audience. Tooling can retrieve a passage, compute a result or perform a declared check. Those contributions need their own capabilities and evidence; the fact that they cite FPF does not establish them. The Library's Reference explains its architecture and connected language, while learning programmes and operational tools retain their own purposes.

Public architectural reasons belong where they help readers understand and adapt the language: why a boundary exists, which serious alternative it excludes, what a dependency supplies and which condition would reopen the choice. Dated authoring decisions, review correspondence and release records serve other readers. [E.11.PFP:4.4](FPF-Spec.md#e11pfp44---keep-support-units-and-adjacent-products-distinct) distinguishes those functions without hiding the useful rationale in internal records.

The resulting architecture offers common meanings and reusable general Methods, specialized constructive knowledge and explicit ways to connect them. It also leaves meaningful limits visible: field coverage can be incomplete; source grounds can be disputed or dated; a necessary supplier, capability or authority can be absent. A sufficient answer can be used directly. An unresolved contribution remains a particular work question, rather than being supplied by another label, file or larger diagram.

Original content is published under the terms stated in [LICENSE](LICENSE) and [LICENSING.md](LICENSING.md). For a specific Method or architectural claim, cite the supplying publication, its edition and PatternID or section address. Cite this account as *FPF Library Architectural Reference*, using the date at its entry and a `Library.Reference` section when needed.

## Library.Reference:End
