# Engineering DPF Suite

> Methods for difficult engineering decisions, explained as patterns you can use with your colleagues and AI assistants.

- **Author:** Anatoly Levenchuk, with AI-assisted development and review
- **Version:** 11 September 2026
- **Status:** Eternal alpha: already used in project analyses and development programmes, and revised as the methods and their evidence improve.
- **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) for original framework content; third-party material retains its own terms.
- **Publication:** [FPF repository](https://github.com/ailev/FPF)

You may be choosing an architecture, trying to make a working method reproducible, reorganizing a team, or deciding what to develop next. The Suite helps you find a useful way to tackle that particular difficulty and produce an answer you can act on.

A **DPF**, or **Domain Principle Framework**, collects methods for a field as a language of patterns. Each pattern explains a recurring difficulty, a way to address it, the result to obtain, and the conditions that affect its use. The methods are connected: one can help you discover or supply what another needs.

[FPF Core](https://github.com/ailev/FPF/blob/main/FPF-Spec.md) supplies the common concepts used across fields. The DPFs bring in the field's methods, competing approaches, examples and source evidence. This combination lets a team discuss technical choices, ways of working and organizational consequences in a shared language.

## Start with the problem in front of you

Describe the situation in ordinary words. For example:

> “We can buy a controller, commission one, or build it ourselves. How do we compare the alternatives, including the work and cost that each leaves to us?”

Open [SYSE.24 - Choose How the Project Will Obtain a Needed Engineering Result](SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse24---choose-how-the-project-will-obtain-a-needed-engineering-result). It helps you compare complete ways to obtain the result: equipment alone, integration work, operating support, capability, access and eventual replacement can all change the choice. Your first useful result may be a defensible comparison or a precise question to put to a supplier.

Use a pattern's **Problem frame** to check that it fits. Its **Solution** gives the working moves; the example shows how they fit a case, and the checklist helps inspect your result. Bring in another pattern when you need its answer. You can begin from a result your project already has.

You can read this way yourself, use a pattern in a working meeting, or ask an AI assistant to help apply it. You do not need to read every framework before starting.

## Choose a DPF

The public folder contains seventeen published DPFs with 272 pattern bodies. Start with the working question nearest to yours. Each linked publication provides its full searchable pattern index.

### Published DPFs

| What you are trying to do | Published DPF | A result it can help you obtain |
| --- | --- | --- |
| Bring about or change an engineered system, from its intended use to working integration and continued development. | [Systems Engineering](SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md) - 41 patterns | A system boundary, architecture decision, comparison of ways to obtain a result, integration plan, or justified release decision. It also covers general Platform Engineering and a substantial software delivery and reliability profile. |
| Choose, explain, test or improve a way of working, or develop a pattern language from source knowledge. | [Method Engineering](METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md) - 24 patterns | An explicit method, a useful description or support arrangement, evidence about fit, transfer and practical value, or a source-based contribution to a method description in pattern-language form. |
| Change how an organization contributes, assigns work and enables people and other performers to act. | [Organization Change Engineering](ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md) - 17 patterns | A compared organizational arrangement, clarified assignments and authority, a supported change, or a decision about its consequences. |
| Work out what the problem is, compare possible directions, or prepare a recommendation. | [Problem Structuring and Decision Support](PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md) - 17 patterns | Several useful problem formulations, decision alternatives, a comparison under uncertainty, or a recommendation with its grounds and limits. |
| Find a worthwhile contribution or an obtaining way, and relate direction, options and bounded commitments under uncertainty. | [Strategy](STRATEGY-PRINCIPLES-FRAMEWORK.md) - 15 patterns | A qualified or provisional problem/contribution account, conditional direction, explained options with their support and gaps, comparison, recommendation or authorized commitment; a decision about conflicting work, changed assumptions or strategic practice. A sufficient answer can finish without an experiment or a new commitment. |
| Create, perform, teach or develop music and dance practices. | [Music and Dance Practice Engineering](MUSIC-AND-DANCE-PRACTICE-ENGINEERING-PRINCIPLES-FRAMEWORK.md) - 22 patterns | A performance or practice design, a useful observation, a transmission method, or a choice about the practice's next development. |
| Keep an operation working while demand, queues, capacity, commitments and evidence change. | [Operations Management](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md) - 20 patterns | A bounded admission or continuation decision, queue or constraint treatment, capacity and service account, operating-method improvement, quality response, simultaneous-work reconciliation, or cultural-continuation decision. |
| Explain how work uses resources and how that use appears in money, forecasts and performance accounts. | [Management Accounting](MANAGEMENT-ACCOUNTING-PRINCIPLES-FRAMEWORK.md) - 9 patterns | A resource and cost model, capacity account, cost allocation, reconciliation, forecast, margin explanation or assessment of accounting incentives. |
| Establish whose financial position is described, what can change it and how a financial service contributes to a participant's result. | [Financial Domain Modeling](FINANCIAL-DOMAIN-MODELING-PRINCIPLES-FRAMEWORK.md) - 5 patterns | A model of parties, rights and obligations; conditional contractual flows; an established financial effect; or a connection between a service and its use. |
| Handle an administrative request, resolve a difficult case, or improve the arrangement providing the service. | [Organization Administration](ORGANIZATION-ADMINISTRATION-PRINCIPLES-FRAMEWORK.md) - 15 patterns | Usable provision, a resolved exception, reconciled obligations and records, or a choice about controls, provider contributions and administrative burden. |
| Preserve or restore required equipment functioning, and manage the policies, support and programme that make maintenance useful. | [Maintenance Engineering and Management](MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md) - 16 patterns | A qualified condition account, supported policy or intervention recommendation, feasible protected work and return to use, or a justified information, programme, Method or practice decision. Advice can be complete before repair. |
| Compare continued use, renewal, replacement or other changes for one asset, an interacting system or a portfolio. | [Engineering Asset Management](ENGINEERING-ASSET-MANAGEMENT-PRINCIPLES-FRAMEWORK.md) - 16 patterns | An applicable asset account, supported alternatives or programme recommendation, feasible timing, an asset decision, or a choice about improving asset-management arrangements, methods or culture. |
| Derive and develop one person's capability for representative later work. | [Human Capability Development](HUMAN-CAPABILITY-DEVELOPMENT-PRINCIPLES-FRAMEWORK.md) - 19 patterns | A supported demand, target or profile; a compared development programme; representative practice and support; performance, transfer or retention evidence; a continuing-development decision, or an instructional-material evaluation through its separate profile. |
| Construct a useful development opportunity, or advise a person, organization or other developing subject. | [Development Opportunity Construction and Development-Direction Advising](DEVELOPMENT-OPPORTUNITY-CONSTRUCTION-AND-DEVELOPMENT-DIRECTION-ADVISING-PRINCIPLES-FRAMEWORK.md) - 9 patterns | A bounded inquiry, characterized change, candidate direction with its supports, joint-reachability result, retained opportunity, or qualified advising engagement. PSD supplies the actual comparison and recommendation when those are needed. |
| Decide whether research is needed, conduct it, examine its conclusions or improve its methods. | [Research Method Practice](RESEARCH-METHOD-PRACTICE-PRINCIPLES-FRAMEWORK.md) - 9 patterns | An answer from existing evidence or a justified research plan; a protocol and record of research performed; an analysis, credibility judgement or corpus synthesis with its limits; a revised claim or question for another practice; or a choice to retain or improve the research method. |
| Connect separately governed meanings for a receiving use, qualify a model, handle semantic change or maintain shared modules. | [Semantic Integration Engineering](SEMANTIC-INTEGRATION-ENGINEERING-PRINCIPLES-FRAMEWORK.md) - 12 patterns | A bounded integration result, adequate model reuse or construction, affected-use repair or revalidation, or a sufficient interface agreement or modular-commons arrangement. |
| Help someone follow why an outcome occurred, how a calculation works, or why a recommendation follows. | [Explanation Design](EXPLANATION-DESIGN-PRINCIPLES-FRAMEWORK.md) - 6 patterns | A useful explanatory question, an account with its grounds, a worked example, coordinated text and diagrams, a repaired exchange, or a supported choice about improving an explanation. Includes instructional, technical and advisory, and human–AI profiles. |

The word *engineering* includes physical equipment, factories, laboratories, buildings, robots and software, as well as the means needed to develop them. A platform can be a manufacturing or laboratory platform. The software profile addresses its particular delivery and reliability difficulties.

When your question crosses fields, open the [Suite Reference](ENGINEERING-DPF-SUITE-REFERENCE.md). It provides a detailed question index and worked cases, including [direct software-platform questions](ENGINEERING-DPF-SUITE-REFERENCE.md#resolve-a-software-platform-difficulty) for measurement, alerts, release exposure, recovery and repetitive work. The [instructional-material questions](ENGINEERING-DPF-SUITE-REFERENCE.md#evaluate-instructional-material-for-its-intended-use) lead to evaluation-specification construction and material evaluation; the [research preparation and trace questions](ENGINEERING-DPF-SUITE-REFERENCE.md#make-research-executable-and-inspect-its-course) lead to the RMP publication's operationalization and research-trace methods. When combining methods, match the result one supplies to what another needs and check their conditions of use. It also gives direct entries for [settling an HCD Method's supported use](ENGINEERING-DPF-SUITE-REFERENCE.md#develop-a-practice-or-a-persons-capability) and [analyzing a research claim or choosing a relevant credibility examination](ENGINEERING-DPF-SUITE-REFERENCE.md#analyze-a-claim-or-examine-its-credibility). For retaining or changing a research Method and returning its consequences, use [the research-Method entry](ENGINEERING-DPF-SUITE-REFERENCE.md#retain-or-improve-a-research-method).

For preserving or restoring equipment functioning, use the [maintenance question index](ENGINEERING-DPF-SUITE-REFERENCE.md#maintain-equipment-and-manage-maintenance) or the [PS17 advice-to-selected-work example](ENGINEERING-DPF-SUITE-REFERENCE.md#can-we-recommend-a-repair-before-it-is-ready-to-begin). To compare continued use, renewal, replacement or withdrawal by value, cost, risk and service, use the [asset-management question index](ENGINEERING-DPF-SUITE-REFERENCE.md#choose-how-to-use-and-change-engineered-assets). EAM provides both a [single-asset comparison](ENGINEERING-ASSET-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#eam-asset---compare-continued-use-and-change-for-one-asset) and a [programme choice under shared constraints](ENGINEERING-ASSET-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#eam-combination---choose-asset-work-under-shared-constraints). Choose by the result your question needs; either practice can concern one asset or many.

For a cost model, operating forecast or reconciliation of profit and cash, use the [management-accounting questions](ENGINEERING-DPF-SUITE-REFERENCE.md#explain-resource-use-costs-and-operating-accounts). For parties, rights, contractual events or the effects of financial actions, use the [financial-modeling questions](ENGINEERING-DPF-SUITE-REFERENCE.md#model-financial-positions-and-effects).

For an explanation that someone must understand and use, start with the [explanation questions](ENGINEERING-DPF-SUITE-REFERENCE.md#make-an-explanation-understandable-and-usable). They distinguish the grounds for an account, its expression, the help a recipient needs and whether further repair is worthwhile.

## Looking for development recommendations?

Open [Development Opportunity Construction and Development-Direction Advising](DEVELOPMENT-OPPORTUNITY-CONSTRUCTION-AND-DEVELOPMENT-DIRECTION-ADVISING-PRINCIPLES-FRAMEWORK.md) for the development-specific question. Its two branches can be used independently.

If useful opportunities are missing, start with [DOCA.1](DEVELOPMENT-OPPORTUNITY-CONSTRUCTION-AND-DEVELOPMENT-DIRECTION-ADVISING-PRINCIPLES-FRAMEWORK.md#doca1---bound-the-development-opportunity-inquiry) or the first missing construction result in its pattern index. To establish the terms of help from an adviser, use [DOCA.7](DEVELOPMENT-OPPORTUNITY-CONSTRUCTION-AND-DEVELOPMENT-DIRECTION-ADVISING-PRINCIPLES-FRAMEWORK.md#doca7---bound-the-development-direction-advising-engagement). When the inputs and service boundary are already adequate, go directly to the missing comparison or recommendation method: [PSD.13](PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md#psd-13) may be enough. [DOCA.8](DEVELOPMENT-OPPORTUNITY-CONSTRUCTION-AND-DEVELOPMENT-DIRECTION-ADVISING-PRINCIPLES-FRAMEWORK.md#doca8---requalify-changed-development-opportunities) helps requalify opportunities after their premises change.

For a particular person's programme comparison, use [HCD.2](HUMAN-CAPABILITY-DEVELOPMENT-PRINCIPLES-FRAMEWORK.md#hcd2---compose-and-compare-capability-development-programmes-for-later-work) once the relevant demand, starting performance, support and candidate programmes are available. The Reference also provides a separate [programme-design entry for future learners](ENGINEERING-DPF-SUITE-REFERENCE.md#recommend-a-programme-before-the-learners-are-known).
For example, “What should our engineering team learn or change over the next four months?” calls for evidence about the work it needs to perform, present limits, feasible alternatives and opportunity costs. A course is one possible response. The inquiry can also reveal a method, tooling or organizational change that would help more. The Reference explains [how to connect advice with those domain results](ENGINEERING-DPF-SUITE-REFERENCE.md#how-do-we-recommend-a-development-direction).

## Work with an AI assistant

Give the assistant access to FPF Core and the relevant DPF files. Tell it about the actual project, the decision you face, your constraints and the evidence available. Ask it to read the patterns it uses.

A useful starting request is:

> Help me work through this situation using FPF and the relevant Engineering DPFs: [describe the situation]. Identify the question we need to answer now, select the pattern that fits it, and help produce the next usable result. Explain the reasoning in ordinary engineering language, show the PatternIDs you used, and say which missing facts could change the answer.

Inspect the answer against the pattern and your project evidence. You and the other participants supply observations, specialist judgement and the authority to make real decisions. The assistant can help search, compare, draft and question the reasoning.

## What to read next

| You need... | Use... |
| --- | --- |
| A quick introduction and a first attempt with the Suite | This README. |
| A precise starting pattern, or a worked example involving several fields | [Engineering DPF Suite Reference](ENGINEERING-DPF-SUITE-REFERENCE.md). |
| The method itself, its example, checks and source discussion | The selected DPF's pattern body. Its Readme gives examples within that field. |
| An explanation of a shared FPF concept or general reasoning method | [FPF Core](https://github.com/ailev/FPF/blob/main/FPF-Spec.md). |
| A programme of study, exercises and feedback to build your abilities | An instructional Guide or a separately designed development programme. The Reference is organized for lookup while you work. |

The README introduces the Suite. The Reference helps you find and combine methods. Full pattern bodies remain the place to inspect what a method asks you to do.

## Suite scope and membership

Engineering DPF Suite brings together domain pattern languages for developing engineered systems and the work, organizations and capabilities needed for them. It serves practitioners choosing and improving methods across these fields, using FPF's shared concepts.

**Current scope decision, effective 11 September 2026.** Under this purpose, the Suite includes the DPF series named in [Published DPFs](#published-dpfs), together with the [Engineering DPF Suite Reference](ENGINEERING-DPF-SUITE-REFERENCE.md) series. This section and the declared list are the current Suite identity and membership account. Each product keeps its own field boundary, readers, methods and dated editions. The list links available editions; the future-publication catalogue records planned additions.

Include a DPF when its accepted product boundary and published pattern language supply a useful contribution to this common purpose, its relevant FPF dependencies are stated, and readers can reach its admitted edition and conditions of use. Record inclusion by updating this declared list when that product decision takes effect. A first accepted publication can implement the product and Suite-inclusion decisions together. Subsequent editions are admitted under the product's own rules; changing an edition or its availability leaves the product's Suite membership in place.

Review the scope when new practitioner needs, changed foundations or a product's limitations alter its contribution. A limitation calls for an explicit warning and a decision to repair, remove or replace the affected contribution. A dated removal ends membership; preserve the earlier fact for readers of older editions. If a product series ends or changes identity, its former membership ends and the replacement needs an inclusion decision.

Adding, removing or revising products preserves this Suite while its common purpose, inclusion rules and identity conditions remain. A change outside that scope identifies another Suite. If the shared purpose can no longer be served, decide whether to restore the collection or retire it; an empty or one-product interval needs an explicit restoration or retirement decision. State any continuing maintenance or future-availability commitment separately from this scope decision.

## Publication scope

The [FPF repository's Suite table](https://github.com/ailev/FPF#engineering-dpf-suite) also lists the DPFs selected for future publication. When an available pattern does not cover a result your project needs, obtain that result from the relevant practice. The date at the start of each DPF identifies the publication you are using.

## Sources, revisions and citation

The DPFs bring together useful research and practitioner approaches, including disagreements and known limits. Source discussions explain what an approach contributes and where its evidence stops. The methods continue to change as better answers become available.

For consequential decisions, keep the publication date and the evidence behind the result you used. Revisit the affected conclusion when the situation or a relied-on source changes.

To cite the collection:

```text
Levenchuk, Anatoly. Engineering DPF Suite.
11 September 2026.
GitHub repository: https://github.com/ailev/FPF
```

For a particular method, cite its DPF, PatternID, title and the date shown in that publication.

## License and reuse

The original FPF and DPF content by Anatoly Levenchuk, including the Engineering DPF Suite and Narrativization DPF, is available under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): you may share and adapt it, including commercially, with attribution, a license link and an indication of changes. See the [licensing scope](https://github.com/ailev/FPF/blob/main/LICENSING.md) for the full notice and third-party and software boundaries.

You choose the license for your own original DPF or LPF. Using FPF methods or its publication form does not impose CC BY on your work. When sharing licensed FPF or DPF text under CC BY 4.0, preserve its attribution and comply with the license. Where your use needs no copyright permission, including under an applicable exception, these conditions do not apply. The license has no ShareAlike requirement.
