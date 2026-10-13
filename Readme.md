# FPF Library

The Library's [document identities and current carriers (Library / Library.Reference:11.1)](FPF-LIBRARY-REFERENCE.md#libraryreference111---document-identities-and-current-carriers) identify the complete publications by DocID and full title. Use these document qualifiers with complete PatternIDs or SectionRefs when a reference must remain usable beyond its present hyperlink.

**FPF Library** is the collection of the First Principles Framework project's own publications: **FPF Core**, **Domain Principle Frameworks (DPFs)**, their **Suites**, and accompanying References and usage materials.

> **AI-native declarative pattern languages for reasoning, engineering and development.** FPF gives people and AI agents a shared, precise language for Systems, Methods, architecture, Work, evidence, verification, decisions, improvement, and communication.

[**FPF Core Specification**](FPF-Spec.md) · [**Library Architectural Reference**](FPF-LIBRARY-REFERENCE.md) · [**Domain frameworks** (Domain Principle Frameworks)](DPFs/README.md) · [**Engineering** (Engineering DPF Suite)](DPFs/Engineering%20DPF%20Suite/README.md) · [**Management** (Management DPF Suite)](DPFs/Management%20DPF%20Suite/README.md) · [**Foundational Thinking** (Foundational Thinking DPF Suite)](DPFs/Foundational%20Thinking%20DPF%20Suite/README.md) · [**Human Capability Engineering** (Human Capability Engineering DPF Suite)](DPFs/Human%20Capability%20Engineering%20DPF%20Suite/README.md)


**Author:** Anatoly Levenchuk, with AI-agent assistance

**License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) for original framework content; third-party material retains its own terms.

**Status:** evolving publications; eternal alpha—already used in working projects and development programs while continuing to change.

This repository publishes transdisciplinary **FPF Core**, four **DPF Suites** and further domain frameworks. A Suite describes a composite discipline through its constituent DPFs and their knowledge and practice relations. It is not a list of every discipline that can supply a useful result. **Engineering** concerns construction, change and sustained functioning of systems. **Management** connects direction, commitments, resources and contributions to continuing joint work. **Foundational Thinking** connects mathematical, physical and computational thinking, modeling and notation. **Human Capability Engineering** concerns forming, changing, restoring and maintaining human-held capabilities; its first edition develops the learning and somatic contributions. Other disciplines retain their own frameworks and can supply a Suite or another undertaking without becoming its constituents.

This Readme helps you choose among the publications. The [Readme inside FPF Core (FPF — First Principles Framework (FPF) Readme)](FPF-Spec.md#first-principles-framework-fpf-readme) gives practical examples of using Core. Each Suite has a short README and a developed Architectural Reference explaining its constituent contributions, their connections and the grounds for that composition. The [FPF Library Architectural Reference](FPF-LIBRARY-REFERENCE.md) explains the wider arrangement, including relations across Suite boundaries and the distinction between discipline composition and using another field's result. It is available when that larger question matters; direct use of a sufficient pattern does not require reading it first.

The wider **FPF ecosystem** also includes other authors' DPFs and LPFs, tools, and services for using FPF.

## Read online or connect your agent

[**fpf.tools**](https://fpf.tools/) provides browser and read-only MCP access to the published FPF Library:

- [**Browse publications and patterns**](https://fpf.tools/publications) to read their contents and source passages.
- [**Search publication texts**](https://fpf.tools/search) by words, quoted phrases or pattern IDs.
- [**Connect through the MCP server**](https://fpf.tools/connect) to let an AI agent search and read the publications. The remote endpoint is `https://mcp.fpf.tools/mcp` (Streamable HTTP); public reading requires no API key.

See [source editions and update status](https://fpf.tools/status) for the revision currently available through the website and MCP.

[Uses and community projects](https://fpf.tools/in-use) is an editorial page on the website, separate from this Library distribution.

## Start here

Before selecting framework guidance, read and apply [Using FPF and its DPF Suites](USING-FPF.md). This instruction applies to project work, framework development, review and coordination. It explains how to find and read relevant content in the publications available to you, including when an interface cannot retrieve a large file.

For unfamiliar terminology or incomplete source access, [FPF F.1](FPF-Spec.md#f1---find-and-select-sources-for-a-current-question) explains how to find inspectable material and return any remaining gap. When several patterns seem plausible, [E.11’s worked comparisons (FPF E.11:4.6.2)](FPF-Spec.md#e11462---resolve-a-first-pattern-ambiguity-with-a-worked-comparison) help recover the fact that changes the first needed result. Use an already known sufficient source directly.

When an AI agent assists you, put this requirement and the instruction's location in your project's `AGENTS.md` or equivalent instructions. If a reading test explicitly limits its reader to an isolated excerpt, use only the materials supplied for that test; do not add USING-FPF.md unless the test includes it.

FPF is designed for two complementary uses:

1. **AI-native, FPF-driven engineering work.** An AI agent can retrieve relevant patterns, compare their declared situations and questions, explain them in plain technical language, expose missing evidence or authority, and help produce the next useful result.
2. **Description and engineering of mixed human–AI work.** People can use the same language to describe which System is being changed, which Method is proposed, which Work is actually performed, which capabilities are available, what is assigned or permitted, who has decision authority, what evidence supports a claim, and what would reopen a decision.

FPF is not an agent framework, an agent runtime, or a software-coding methodology. It is a knowledge and reasoning framework that can guide work in manufacturing, construction, mechanical and electrical engineering, energy, robotics, laboratories, healthcare technology, education, embodied practice, software-intensive Systems, and other fields.

## Why an AI-native pattern language?

The FPF Core contains more than 300 interlinked transdisciplinary patterns. Reading and remembering the entire corpus is not a prerequisite for using it—and is rarely the best human entry mode. A capable AI agent can serve as a high-bandwidth reader of the pattern language: search the corpus, inspect a small set of plausible patterns, quote exact source passages when needed, and translate the relevant distinctions into the engineer's working language.

Instead of asking an agent to improvise from generic model priors, an FPF-driven setup gives it FPF Core and the relevant DPFs as explicit, inspectable references. The agent can then follow a maintained, plural account of current engineering thought, show which patterns and sources it used, and separate a source-grounded recommendation from plausible but unsupported advice.

The engineer supplies what the corpus cannot supply: the actual situation, domain knowledge, observations, constraints, stakes, local history, access to the engineered System, and any real assignment, permission, responsibility, or authority. The agent helps keep these claims distinct rather than silently inventing them.

This division of Work makes FPF useful as a common language between AI agents and **engineer–managers**: engineers who identify primarily as engineers but spend much of their day doing substantive management Work. They coordinate specialists and providers, negotiate architecture and interfaces, organize reviews and working meetings, compare alternatives and trade-offs, formulate strategies, make responsible decisions, preserve knowledge, and allocate Work among people, tools, robots, and AI. The term describes Work, not a corporate job title.

**AI-native does not mean AI-only.** It means that the architecture of the Work can be deliberately reconsidered around the different capabilities and limitations of humans, AI agents, tools, and other Systems. An AI-produced statement is not automatically a fact, evidence, permission, commitment, or decision. Each such relation must be established by its own basis.

## A declarative language, not a prescribed process

FPF and its DPFs are declarative pattern languages. Start from the **current working situation** and the **question that is current now**. Inspect the pattern whose declared Situation and Question match that difficulty. Use its distinctions, constraints, checks, result, and stop or reopen conditions to produce the smallest useful result—or an honest blocker.

Pattern numbers, file order, table-of-contents order, and the order in which examples are presented do not prescribe a project sequence. Several kinds of engineering Work may overlap. A real dependency still matters when one result cannot be used before another exists, but that dependency belongs to the concrete results and Work under consideration, not to a universal process imposed by the pattern language.

A constituent action can also perform several levels of work at once: updating a running total can be part of calculating a result and preparing a report. The encompassing purpose changes what that action must preserve. FPF helps [recover these connections (FPF B.1.5.EW)](FPF-Spec.md#b15ew---recover-how-constituent-actions-enact-encompassing-work) and [compare a replacement in its encompassing uses (FPF B.1.5.RS)](FPF-Spec.md#b15rs---evaluate-a-constituent-method-replacement-in-its-encompassing-uses); the Suite References give domain examples. Using a DPF still requires the relevant capabilities, coordination and resources throughout the needed vertical, including any intermediate contribution that must be learned or obtained.

An AI agent can therefore help choose the **next justified move** without pretending that the entire project follows one fixed sequence. The useful move may be a clarified question, an identified System, an architecture comparison, an evidence request, a decision record, a changed Method, a bounded Work plan, a source-grounded explanation, or an explicit stop because a necessary basis is missing.

## What is in the Library?

| Publication | What it contributes | Typical working questions |
| --- | --- | --- |
| [**FPF Core Conceptual Specification**](FPF-Spec.md) | A transdisciplinary language for entities and relations, Systems, Methods, Work, descriptions, claims, evidence, decisions, architecture, quality, improvement, cultural evolution, publication, and precise language. | What exactly are we discussing? What claim is being made? Which relation obtains? What may the evidence support? Which decision is current? What Work actually occurred? |
| [**Foundational Thinking DPF Suite**](DPFs/Foundational%20Thinking%20DPF%20Suite/README.md) | Mathematical Thinking, Mathematical Modeling, Physical Thinking, Computational Thinking and Notational Engineering, with a Reference for their connected use. | How do we enter an unfamiliar problem, connect its different kinds of reasoning, use the result and change the way of working? |
| [**Engineering DPF Suite**](DPFs/Engineering%20DPF%20Suite/README.md) | Four direct constituent DPFs for system construction and realization, maintenance, knowledge access and semantic integration; organizational and human specializations have their own Suites. | What system effect is needed? Which design, realization, capability, qualification or maintenance contribution makes it possible? |
| [**Management DPF Suite**](DPFs/Management%20DPF%20Suite/README.md) | Eleven constituent DPFs for direction, operations, administration, governance, accounting, finance, marketing, assets, leadership, communities and organizational change. | Which contributions and commitments serve the intended result, and can they be supported together under actual authority and resource conditions? |
| [**Human Capability Engineering DPF Suite**](DPFs/Human%20Capability%20Engineering%20DPF%20Suite/README.md) | Two complete DPFs on human capability development and somatic movement, within the broader construction and maintenance of human-held capabilities. | Which capability needs to change, what learning or embodied change could produce it, and what shows that it is available in later work? |
| [**FPF Library Architectural Reference**](FPF-LIBRARY-REFERENCE.md) | The arrangement of Core, DPFs and Suites, with reasons, alternatives and worked connections. | Why are these boundaries drawn here, which relations cross them, and how does that affect using or adapting the Library? |
| [**Narrativization and Narrative Studies DPF** (NSTD)](DPFs/Narrativization-and-Narrative-Studies-Principles-Framework.md) | Patterns for turning selected source structure into a followable narrative while preserving recoverability, evidence limits, agency boundaries, viewpoint choices, and source return. Includes human and automated narrativization. | What source structure must survive the rendering? What may be compressed or reordered? Did a fluent narrative invent causality, agency, certainty, permission, or authority? |

### Foundational Thinking DPF Suite

Foundational Thinking connects mathematical construction, modeling, physical accounts, algorithms and operative notation. The [Readme (Foundational Thinking DPF Suite)](DPFs/Foundational%20Thinking%20DPF%20Suite/README.md) introduces available members and connected examples. The [Architectural Reference (Foundational)](DPFs/Foundational%20Thinking%20DPF%20Suite/FOUNDATIONAL-THINKING-DPF-SUITE-REFERENCE.md) explains their architecture and how to move between mathematical constructions, modeling and other contributions. Notational Engineering adds methods for making those contributions expressible, interpretable and usable together.

| Domain pattern language | Publication | What it covers |
| --- | --- | --- |
| [**Mathematical Thinking DPF** (MATH)](DPFs/Foundational%20Thinking%20DPF%20Suite/MATHEMATICAL-PRACTICE-DPF.md) | Full pattern language | Twenty patterns and worked connections between their methods. Start with MP-FRAME when you have a working question but do not yet know which mathematics it needs. The embedded Architectural Reference shows how to choose a representation, obtain and interpret a result, and revise the representation when the question changes. The individual bodies develop the mathematical constructions used along the way. This independently usable publication belongs to the Foundational Thinking DPF Suite. The [Suite Architectural Reference (Foundational)](DPFs/Foundational%20Thinking%20DPF%20Suite/FOUNDATIONAL-THINKING-DPF-SUITE-REFERENCE.md) gives working combinations and explains how these methods connect with the general methodological constructions in FPF Core. |
| [**Mathematical Modeling DPF** (MMP)](DPFs/Foundational%20Thinking%20DPF%20Suite/MATHEMATICAL-MODELING-PRACTICE-DPF.md) | Full pattern language | Seventeen patterns and worked connections between their methods. Begin with the [Readme introduction (MMP — Mathematical Modeling - Readme)](DPFs/Foundational%20Thinking%20DPF%20Suite/MATHEMATICAL-MODELING-PRACTICE-DPF.md#mathematical-modeling---readme) when the working question has no mathematical formulation. The methods cover formulation, inference, prediction repair, intervention effects, counterfactual comparisons, observation design, sequential decisions, reduction, surrogates and model coupling. Readme and embedded Architectural Reference show how one result supplies the next operation, how a changed question returns to its affected construction, and when an adequate answer permits stopping. |
| [**Physical Thinking DPF** (PHY)](DPFs/Foundational%20Thinking%20DPF%20Suite/PHYSICAL-THINKING-DPF.md) | Full pattern language | Ten patterns and worked connections between their methods. Start with a physical question for which you need an account, a prediction, an observation or a revised assumption. The methods help constrain unknown laws, choose the effects to retain, derive how a system changes, relate possible microscopic states to collective behavior, use physical similarity and analogues, establish physical limits, and construct measurements and tests. The embedded Architectural Reference shows how physical, mathematical and computational contributions work together, and which contribution to revisit when the physical situation changes. |
| [**Computational Thinking DPF** (CMP)](DPFs/Foundational%20Thinking%20DPF%20Suite/COMPUTATIONAL-THINKING-DPF.md) | Full pattern language | Fourteen patterns for algorithmics within computer science. Its [CMP — Computational Thinking - Readme](DPFs/Foundational%20Thinking%20DPF%20Suite/COMPUTATIONAL-THINKING-DPF.md#computational-thinking---readme) follows connections for translating programs, obtaining answers within resource limits, and sharing calculations while keeping request effects correct. The methods help construct and revise algorithms, control computation cost and error, preserve meaning when translating a program, and make interacting computations produce the required result. The embedded Architectural Reference's worked example changes from finding one optimal solution to enumerating all of them. It shows which earlier pruning and reconstruction choices must change. Numerical computation is one application of these methods. |
| [**Notational Engineering DPF** (NOT)](DPFs/Foundational%20Thinking%20DPF%20Suite/NOTATIONAL-ENGINEERING-DPF.md) | Full pattern language | Eight patterns for designing expressions and their use. Use the [connected examples (NOT — Notational Engineering - Readme)](DPFs/Foundational%20Thinking%20DPF%20Suite/NOTATIONAL-ENGINEERING-DPF.md#notational-engineering---readme) to follow a changed request through several representations, or keep a sequence usable when its reader or reference frame changes. The methods cover grouping and binding, interpretation, meaning-preserving transformation, translation losses, complementary representations, difficult reading operations, and temporal or embodied notation. The embedded Architectural Reference follows a formula, graph and table through a changed request without overwriting independent observations. |

Larger questions need several patterns. [Changing a combining rule (MATH — MP-COMBINE-RESULTS - Change a rule so that separately obtained results can be combined)](DPFs/Foundational%20Thinking%20DPF%20Suite/MATHEMATICAL-PRACTICE-DPF.md#mp-combine-results---change-a-rule-so-that-separately-obtained-results-can-be-combined) connects a counterexample, retained information, an operation and a proof. [Answering with incomplete model detail (MMP — MMP-SUFFICIENT-ANSWER - Answer the working question before reconstructing every detail)](DPFs/Foundational%20Thinking%20DPF%20Suite/MATHEMATICAL-MODELING-PRACTICE-DPF.md#mmp-sufficient-answer---answer-the-working-question-before-reconstructing-every-detail) connects reduction, bounds, interpretation and further work. [Developing a physical prediction (PHY — PH-PREDICT-AND-DISTINGUISH - Develop a physical prediction and the test it needs)](DPFs/Foundational%20Thinking%20DPF%20Suite/PHYSICAL-THINKING-DPF.md#ph-predict-and-distinguish---develop-a-physical-prediction-and-the-test-it-needs) links assumptions about an unknown physical law to a prediction, an observation that distinguishes alternatives, and revision when those assumptions change. [Constructing an algorithm within available resources (CMP — CP-ANSWER-UNDER-LIMITS - Obtain the answer the work needs within available resources)](DPFs/Foundational%20Thinking%20DPF%20Suite/COMPUTATIONAL-THINKING-DPF.md#cp-answer-under-limits---obtain-the-answer-the-work-needs-within-available-resources) connects decomposition, reused subcomputations, search bounds and recovery of the requested answers. [Carrying meaning through several expressions (NOT — NT-CHANGE-TOGETHER - Carry a changed request through several representations)](DPFs/Foundational%20Thinking%20DPF%20Suite/NOTATIONAL-ENGINEERING-DPF.md#nt-change-together---carry-a-changed-request-through-several-representations) connects interpretation, transformation, translation loss and the intended change. These sequences and worked explanations show how the pattern contributions depend on one another.


### General Methods of development and methodological work

Open-ended development grows knowledge and reproducible ways of acting, uses those results and continues to further attainable problems. It is not established by doing more work, acquiring a known Method or completing one improvement. The general constructions are explained in [FPF Core](FPF-Spec.md): constructing opportunities and questions, developing and qualifying Methods, connecting ways with their holders and provision, using results and opening a worthwhile next problem. The general connection is developed in [FPF C.40.OD](FPF-Spec.md#c40od---construct-and-continue-open-ended-development), with [FPF C.40.JD](FPF-Spec.md#c40jd---develop-a-way-its-holder-and-its-provision-together) for the way, its holder and provision, and [FPF C.40.NP](FPF-Spec.md#c40np---continue-from-a-result-to-new-attainable-problems) for continuation after a result. The [Library Architectural Reference (Library / Library.Reference:9)](FPF-LIBRARY-REFERENCE.md#libraryreference9---open-ended-development-belongs-across-these-fields) explains their relation to the domain contributions.

The full Methods for requirements, source recovery, composite Methods, representations, trials, fit, transfer, practical worth, variants, methodological support and pattern-language construction are in Core. Researching what happened in practice or history uses Research Method Practice; mathematical construction and comparison use Mathematical Modeling. The general checklist Methods are also in Core, with their separate questions about selection, formulation, occasion fit, grounded answers, shared results and qualification of checking means.

### Engineering DPF Suite

Engineering concerns constructing, changing and sustaining functioning systems. The [Readme (Engineering DPF Suite)](DPFs/Engineering%20DPF%20Suite/README.md) introduces these four direct constituent languages and their subject-specific Methods. The [Architectural Reference (Engineering)](DPFs/Engineering%20DPF%20Suite/ENGINEERING-DPF-SUITE-REFERENCE.md) explains how the contributions constrain and supply one another without prescribing project stages. Management and Human Capability Engineering describe the organizational and human specializations; OCE has its complete home in Management. Maintenance remains complete here, including its technical and management Methods. A sufficient analysis or recommendation, including a warranted no-change result, can complete a particular engineering task.

| Domain pattern language | Publication | What it covers |
| --- | --- | --- |
| [**Knowledge-Corpus Access Engineering DPF** (KCAE)](DPFs/Engineering%20DPF%20Suite/KNOWLEDGE-CORPUS-ACCESS-ENGINEERING-PRINCIPLES-FRAMEWORK.md) | Full pattern language | access arrangements and source preparation; complementary retrieval and developing queries; candidate assessment, corpus synthesis and combining contributions into a usable result; delivery of reading material, coherent updates, useful encounters, revisable memory and evaluation by useful results and full cost. |
| [**Maintenance Engineering and Management DPF** (MNT)](DPFs/Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md) | Full pattern language | maintenance policy; condition evidence and diagnosis; support readiness; intervention recommendations and protected work; verification and return to use; maintenance information; programme coordination; Method improvement; simultaneous Work; and maintenance culture. |
| [**Semantic Integration Engineering DPF** (SIE)](DPFs/Engineering%20DPF%20Suite/SEMANTIC-INTEGRATION-ENGINEERING-PRINCIPLES-FRAMEWORK.md) | Full pattern language | making separately governed meanings and representations usable together; semantic-model reuse and construction; cross-source correspondences, identities and claims; extraction and transformation; interfaces and validation; response to semantic change; and maintenance of shared semantic modules. Includes ontology and knowledge-graph engineering Methods. |
| [**Systems Engineering DPF** (SYSE)](DPFs/Engineering%20DPF%20Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md) | Full pattern language | project System focus; intended use; affected Systems; problem and System-family options; functional organization; architecture and interfaces; specialist contributions; build, buy, provider, reuse, AI, or hybrid arrangements; recursive realization; integration; platforms; configuration and effectivity; release evidence; source change; evolvability; overlapping Work; and engineering culture. |

**Platform Engineering** is included in Systems Engineering, with common Methods and subject profiles. The [Engineering Reference](DPFs/Engineering%20DPF%20Suite/ENGINEERING-DPF-SUITE-REFERENCE.md) includes both constituent and external contributions for engineering questions. Using an outside discipline does not absorb it into Engineering.

For learning that depends on explanation, varied examples, bodily coordination or participation in work, use HCD's [connected learning cases (HCD / HCD.Application:10)](DPFs/Human%20Capability%20Engineering%20DPF%20Suite/HUMAN-CAPABILITY-DEVELOPMENT-PRINCIPLES-FRAMEWORK.md#hcdapplication10---combine-explanation-experience-and-participation-in-a-changing-practice). They show how to choose and combine the next learning action for language, partnered movement, a clerk's work and an engineering team.

### Management DPF Suite

These eleven constituent languages connect direction and joint work with the authority, resources and contributions needed to obtain results. The [Readme (Management DPF Suite)](DPFs/Management%20DPF%20Suite/README.md) introduces the languages. The [Architectural Reference (Management)](DPFs/Management%20DPF%20Suite/MANAGEMENT-DPF-SUITE-REFERENCE.md) explains the composition, alternatives and conditions on the whole, including when separately feasible commitments compete for the same capacity. OCE supplies the organizational construction within this assembly. Management can use the full maintenance Methods in Engineering, including when a manager performs them directly; the contribution keeps its maintenance subject and conditions.

| Domain pattern language | Publication | What it covers |
| --- | --- | --- |
| [**Community Management DPF** (CB)](DPFs/Management%20DPF%20Suite/COMMUNITY-MANAGEMENT-PRINCIPLES-FRAMEWORK.md) | Full pattern language | useful participation, relationships, shared practice and joint contributions; entry, provision, distributed organizing and continuation among independent carriers as well as organizations. |
| [**Leadership DPF** (LDR)](DPFs/Management%20DPF%20Suite/LEADERSHIP-PRINCIPLES-FRAMEWORK.md) | Full pattern language | contributions to joint work, feasible agreement and preparation through first useful work, with actual authority, refusal and capacity conditions; substantive-discussion construction is supplied by Core B.5.SD. |
| [**Strategy DPF** (STR)](DPFs/Management%20DPF%20Suite/STRATEGY-PRINCIPLES-FRAMEWORK.md) | Full pattern language | finding worthwhile contributions and ways to obtain them; direction under uncertainty; options and scenarios; capabilities, dependencies and initiatives; investments and business models; commitments; and decisions to revise, pivot, pause or stop. |
| [**Corporate Finance DPF** (FIN)](DPFs/Management%20DPF%20Suite/CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md) | Full pattern language | financing, liquidity and working capital; capital allocation and valuation; cost of capital and capital structure; financial exposure; and consequences for other organizational decisions. |
| [**Corporate Governance DPF** (CGOV)](DPFs/Management%20DPF%20Suite/CORPORATE-GOVERNANCE-PRINCIPLES-FRAMEWORK.md) | Full pattern language | corporate matters and rules; shareholding, voting and control; governing powers and contributions; committees, conflicts and independent review; information, internal control and assurance; corporate decisions, minority rights and accountability; effective amendments; and development and continuation of governance methods. |
| [**Engineering Asset Management DPF** (EAM)](DPFs/Management%20DPF%20Suite/ENGINEERING-ASSET-MANAGEMENT-PRINCIPLES-FRAMEWORK.md) | Full pattern language | value, service, cost, risk and capacity over the lives of engineered assets; continued use, renewal, replacement and other changes for one asset, interacting asset systems or portfolios; shared constraints, timing and asset-management practice. |
| [**Management Accounting DPF** (MA)](DPFs/Management%20DPF%20Suite/MANAGEMENT-ACCOUNTING-PRINCIPLES-FRAMEWORK.md) | Full pattern language | cost models for resource use and capacity; allocation of shared costs; reconciliation of operating results, financial reports and cash; forecasts, targets and resource requests; explanation of margin changes; customer and product economics; and behavioral effects of accounting measures. |
| [**Marketing DPF** (MKT)](DPFs/Management%20DPF%20Suite/MARKETING-PRINCIPLES-FRAMEWORK.md) | Full pattern language | customer and market inquiry; offers, positioning and reach; feasible choice; customer experience and journey design; help and relationships; intervention value and cost; promises and provision; repeatability; and programmes for selected customer organisations. |
| [**Operations Management DPF** (OPS)](DPFs/Management%20DPF%20Suite/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md) | Full pattern language | continuing Work; operating modes and admission; cases, queues, flow and work in progress; constraints, capacity and commitments; resources and human conditions; exceptions; quality and reliability; coordination of simultaneous Work; Method improvement from operating evidence; and development of operations culture. |
| [**Organization Administration DPF** (ADM)](DPFs/Management%20DPF%20Suite/ORGANIZATION-ADMINISTRATION-PRINCIPLES-FRAMEWORK.md) | Full pattern language | organizational requests and cases; permissions and effective dates; usable provision and access; obligations, performance and records; exceptions and controls; provider coordination; administrative burden; and revision while open cases continue. |
| [**Organization Change Engineering DPF** (OCE)](DPFs/Management%20DPF%20Suite/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md) | Full pattern language | organizational contributions, roles and assignments; authority and interfaces; capability allocation; comparison and realization of organizational changes; participation and adoption; culture; and the effects of change on actual Work. |

### Human Capability Engineering DPF Suite

Human Capability Engineering concerns forming, changing, restoring and maintaining human-held capabilities. The [Readme (Human Capability Engineering DPF Suite)](DPFs/Human%20Capability%20Engineering%20DPF%20Suite/README.md) introduces the available languages. The [Architectural Reference (HCE)](DPFs/Human%20Capability%20Engineering%20DPF%20Suite/HUMAN-CAPABILITY-ENGINEERING-DPF-SUITE-REFERENCE.md) explains how the human learning and somatic contributions work together. The two complete languages in this edition develop learning and somatic change. They do not exhaust the broader human field: age-specific services, clinical interventions and every method used by a human are not claimed as covered. The changed human capability defines the subject; a teacher, AI assistant or organization can perform a contributing Method.

| Domain pattern language | Publication | What it covers |
| --- | --- | --- |
| [**Human Capability Development DPF** (HCD)](DPFs/Human%20Capability%20Engineering%20DPF%20Suite/HUMAN-CAPABILITY-DEVELOPMENT-PRINCIPLES-FRAMEWORK.md) | Full pattern language | human capability needed for later Work; demand and capability profiles; personal programmes and whole learning products for future audiences; individual and shared practice; learning through explanation, peer review and project comparison; group formation, regulation and shared rhythm; assessment, transfer and retention; providers and support; development portfolios and qualification; and characterization and evaluation of instructional material. |
| [**Somatic Movement Modeling DPF** (SOM)](DPFs/Human%20Capability%20Engineering%20DPF%20Suite/SOMATIC-MOVEMENT-MODELING-PRINCIPLES-FRAMEWORK.md) | Full pattern language | relating bodily experience, voluntary regulation and movement results; making changes distinguishable; regulating effort; combining and recalling coordination; adapting it through changing support or load, within a familiar human movement practice. |

### Further domain frameworks

These ten further fields have complete pattern languages directly under `DPFs/`. No further composite discipline is asserted for these ten fields. The [domain-framework catalogue (Domain Principle Frameworks)](DPFs/README.md) also points to the four Suites. A project can combine the contributions it needs while retaining each field's Methods, assumptions and evidence.

| Domain pattern language | Publication | What it covers |
| --- | --- | --- |
| [**Narrativization and Narrative Studies DPF** (NSTD)](DPFs/Narrativization-and-Narrative-Studies-Principles-Framework.md) | Full pattern language | turning selected source structure into a followable narrative while preserving recoverability, evidence limits, agency boundaries, viewpoint choices and source return; human and automated narrativization. |
| [**Implementation Facilitation DPF** (IS)](DPFs/IMPLEMENTATION-FACILITATION-PRINCIPLES-FRAMEWORK.md) | Full pattern language | agreeing, constructing, adapting and continuing help for enacting an interpretable practice under its actual conditions; choosing and providing human, AI, organizational or external contributions, engaging recipients and helping them use and sustain the practice. The general Method for introduction and reconsideration is in Core A.3.1.MI. |
| [**Decision Design DPF** (PSDA)](DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md) | Full pattern language | constructing problem formulations, alternatives, values, consequence models, uncertainty accounts, comparisons and recommendations; agreeing the helping engagement, participation and representation, facilitation, advice, follow-up, competence and shared work. Substantive discussion has its full general Method in Core B.5.SD. |
| [**Research Method Practice DPF** (RMP)](DPFs/RESEARCH-METHOD-PRACTICE-PRINCIPLES-FRAMEWORK.md) | Full pattern language | qualifying a research question or answering it from existing sources; comparing approaches and selecting a design; operationalization and sampling; records and provenance; claim analysis and criticism; reproducibility, replication and triangulation; corpus synthesis; revision and return of knowledge contributions; and retention or improvement of research Methods. |
| [**Defense and Transmission Modeling DPF** (DTM)](DPFs/DEFENSE-AND-TRANSMISSION-MODELING-DPF.md) | Full pattern language | dependence and consequences; exposure, uptake and reconstruction; coupled continuation and spread; selection within and among collectives; variant interaction; diversion of shared support; protective targets; and response costs, memory and feedback. |
| [**Economic Reasoning and Coordination DPF** (ECO)](DPFs/ECONOMIC-REASONING-AND-COORDINATION-PRINCIPLES-FRAMEWORK.md) | Full pattern language | economic calculation and price response; exchange discovery; resource commitments; private information and incentives; adaptation under dependence; shared resources; local and wider orders; institutional change; and resource use after demand responds to efficiency. |
| [**Embodied Rhythmics DPF** (RHY)](DPFs/EMBODIED-RHYTHMICS-PRINCIPLES-FRAMEWORK.md) | Full pattern language | identifying rhythmic relations; continuous sound and movement with articulation; timing, representations and translation; comparison and transformation; action and cue allocation; shared reference and simultaneous layers; human practice, capability probes and observation; connected cultural uses through Music and Dance Practice Engineering. |
| [**Explanation Design DPF** (EXD)](DPFs/EXPLANATION-DESIGN-PRINCIPLES-FRAMEWORK.md) | Full pattern language | explanatory questions and their subject grounds; worked examples and their limits; coordinated expression; responsive dialogue; targeted feedback and another learner attempt; and worthwhile repair for the recipient and task. Includes instructional, technical and advisory, and human–AI profiles. |
| [**Financial Domain Modeling DPF** (FDM)](DPFs/FINANCIAL-DOMAIN-MODELING-PRINCIPLES-FRAMEWORK.md) | Full pattern language | financial positions, rights and obligations; boundaries of parties and groups; contractual events and payment flows; effects of approvals, postings and payments; and the contribution of a financial service to a participant's result. |
| [**Music and Dance Practice Engineering DPF** (MDPE)](DPFs/MUSIC-AND-DANCE-PRACTICE-ENGINEERING-PRINCIPLES-FRAMEWORK.md) | Full pattern language | embodied capability; coordination; generation; performance; observation; recognition; learning and transmission; supporting arrangements; alternatives; local change; style development; and cultural continuation in Music and Dance practice. |

## What is a DPF?

A **DPF, Domain Principle Framework**, is an FPF-grounded declarative pattern language for a recurring family of domain difficulties. It turns maintained domain knowledge into reusable patterns that can be selected by their Situation and Question rather than read as a textbook chapter sequence.

A DPF is intended to keep a domain's **state of the art (SoTA)** usable. Here, SoTA is not equated with the newest official standard, one institutional consensus, or one fashionable method. It is a current, plural, source-linked account of useful approaches, rival schools, evidence, practitioner experience, known failures, trade-offs, and the conditions under which a particular move is warranted. A DPF must preserve disagreement and source-use limits instead of laundering them into one authoritative-sounding recipe.

DPFs depend on FPF Core for transdisciplinary distinctions and do not silently rewrite it. FPF Core does not depend on any one DPF. More DPFs can be added for other domains while retaining the same shared language for cross-domain human–AI work.

## Recognizable engineering difficulties

FPF becomes useful when an ordinary conversation, document, dashboard, or generated answer no longer keeps difficult Work coherent. Typical signals include:

| What practitioners notice | What FPF helps make explicit |
| --- | --- |
| A late source, requirement, supplier, or design change returns as **rework**. | Which claims and decisions relied on the changed source; what must be revalidated; what remains unaffected. |
| A **handoff** loses scope, configuration, assumptions, evidence, or responsibility. | The exact subject, relation, receiving use, result, evidence limits, assignment, permission, and authority. |
| An **architecture decision** exists only in meeting memory, a chat, or a diagram. | Candidate structures, interfaces, comparison basis, accepted losses, selected structure, decision, and reopen conditions. |
| A design review compares labels such as build, buy, supplier, reuse, automation, or AI. | Comparable whole obtaining arrangements, including integration, assurance, support, capability, lock-in, and exit burdens. |
| A test, simulation, model, certificate, review, or AI answer “passed,” but nobody can say what it proves. | The claim, subject, conditions, configuration, evidence correspondence, traceability, uncertainty, and decision that may rely on it. |
| Parts are complete, but **integration**, **configuration**, **commissioning**, or actual use still fails. | The bounded configuration, intended use, interfaces, unresolved dependencies, operating evidence, fallback, and release decision. |
| Field failures or operating feedback do not return to design and Method decisions. | The affected architecture, source, configuration, evidence, Method, and decision conditions that must be reopened. |
| The result works once but is hard to maintain, reproduce, transfer, or change. | Maintainability and evolvability trade-offs, support arrangements, capability, tacit knowledge, descriptions, trials, and knowledge transfer. |
| One experienced person knows how the Work is really done, while the procedure says something else. | Method, MethodDescription, capability, actual Work, observed result, local variation, and evidence of transfer. |
| Humans and AI agents produce fluent output but disagree about facts, evidence, permission, or who decides. | Separate claims for capability, assignment, permission, authority, responsibility, evidence, and actual performed Work. |
| A technical explanation or narrative is compelling but cannot be traced back to the source structure. | Source selection, preserved and lost relations, viewpoint, compression, reconstruction checks, evidence limits, and source return. |

## Use FPF with your agent

Copy `FPF-Spec.md`, `Readme.md`, `USING-FPF.md`, `LICENSE` and `LICENSING.md` into a folder in your project, for example `fpf/`. For the complete Library, also copy `FPF-LIBRARY-REFERENCE.md` and the complete `DPFs/` directory beside Core, preserving their paths. Each complete DPF has one current full home; using its Methods elsewhere does not require another copy. If you select only part of the Library, include the actual member and supplier files needed for the work, retaining their folder paths and the README/Reference entries you use. Resolve pattern references in the copies you supplied, even when a publication writes them as GitHub links. Choose another edition when your task needs an update or a comparison.

For a project using the complete Library:

```text
fpf/
  FPF-Spec.md
  FPF-LIBRARY-REFERENCE.md
  Readme.md
  USING-FPF.md
  LICENSE
  LICENSING.md
  DPFs/
    README.md
    Engineering DPF Suite/
      README.md
      ENGINEERING-DPF-SUITE-REFERENCE.md
      MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md
      ... three other complete constituent DPF files ...
    Management DPF Suite/
      README.md
      MANAGEMENT-DPF-SUITE-REFERENCE.md
      ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md
      ... ten other complete constituent DPF files ...
    Foundational Thinking DPF Suite/
      README.md
      FOUNDATIONAL-THINKING-DPF-SUITE-REFERENCE.md
      ... five complete constituent DPF files ...
    Human Capability Engineering DPF Suite/
      README.md
      HUMAN-CAPABILITY-ENGINEERING-DPF-SUITE-REFERENCE.md
      HUMAN-CAPABILITY-DEVELOPMENT-PRINCIPLES-FRAMEWORK.md
      SOMATIC-MOVEMENT-MODELING-PRINCIPLES-FRAMEWORK.md
    ... ten further complete DPF files ...
```

Add the following paragraph to the project instructions your agent environment actually loads, whether those are kept in a file or in its settings. Replace `fpf/` with your chosen path:

> Use FPF and the relevant DPFs from `fpf/` for this project's work. Before using them, read `fpf/USING-FPF.md` and follow its guidance for choosing, reading, and applying patterns. Explain results and give feedback in the language of our work. Preserve the meaning of the sources.

If the environment has no persistent project instructions, send that paragraph as the first message. Then describe the actual project question, constraints, and available evidence. [USING-FPF.md (Using FPF and its DPF Suites)](USING-FPF.md) contains the agent's working instructions, file structure, and search examples.

## Start from the question that is current now

| Current question | Useful entry |
| --- | --- |
| What exactly is the project changing, and for which use? | FPF `A.1.SCR`, `A.15.6`; Systems Engineering DPF `SYSE.1`, `SYSE.16`, `SYSE.2`. |
| Which functions, bearers, architecture, and interfaces should be selected? | FPF `C.30`, `C.32`, `C.32.P2S`; Systems Engineering DPF `SYSE.5`, `SYSE.6`. |
| Should we build, buy, reuse, contract a provider, use AI, or combine them? | Systems Engineering DPF `SYSE.24`; compare complete obtaining arrangements rather than labels. |
| What can this test, model, trial, review, or observation justify? | FPF `A.10`, `B.3`, `C.16`; Systems Engineering DPF `SYSE.4`, `SYSE.10`. |
| Which configuration exists, where does the claim apply, and may it be released? | Systems Engineering DPF `SYSE.13`, `SYSE.14`, `SYSE.19`. |
| Which Work may overlap, and which result dependencies really require order? | FPF `A.15.1`, `E.18.NET`; Systems Engineering DPF `SYSE.20`. |
| Which reusable way of working is current, and does it work in this situation? | FPF `A.3.1`, `C.39` and the Core pattern owning the current Method question; use the supplying DPF for a subject-specific construction. |
| What capability is missing for a named family of Work? | FPF `E.23.CDI`; then use the relevant domain pattern for the Work and evidence. |
| What does current SoTA offer, where do approaches disagree, and what should be maintained as a DPF? | FPF `G.2`, `E.4.DPF`; preserve sources, rival approaches, scope, freshness, and stop conditions. |
| How should source material become a technical explanation, learning rendering, or narrative without invented structure? | Narrativization and Narrative Studies DPF `NSTD.*`, selected by the current narrative question. |

These are entry points. One pattern can resolve a local difficulty; a larger question can require results that depend on one another. Use the Suite's connected examples and cards to follow those dependencies, and stop when the result needed by the current work is available.

## One-minute cross-industry example

A factory team needs more throughput from a filling and inspection cell without sacrificing product quality, maintainability, or safe operation. The first discussion jumps between four labels: modify the existing line, buy an integrated cell, assemble a solution from specialist suppliers, or combine operators, robots, machine vision, and AI agents.

An FPF-driven agent does not begin with a software architecture or a generic transformation plan. It helps the engineer:

- identify the actual project System and the operating use that matters;
- recover affected neighbouring and using Systems;
- compare functional, bearer, and interface alternatives;
- turn the four labels into comparable whole obtaining arrangements, including integration, assurance, support, capability, lock-in, and exit burdens;
- identify which configuration and effectivity range each claim concerns;
- connect trials and measurements to the exact claims they may support;
- distinguish overlapping Work from dependencies that genuinely require order;
- expose capability, assignment, permission, and decision-authority gaps;
- record the selected architecture, accepted trade-offs, evidence basis, and reopen conditions;
- return commissioning and field feedback to the affected design, Method, and decision.

The agent can draft and inspect this result using FPF and the Systems Engineering DPF. Engineers and other authorized participants contribute ground truth, evaluate the evidence, negotiate commitments, and make the actual decisions. The same distinctions apply to a building subsystem, laboratory setup, medical device, robotic product, energy installation, organizational method, research program, or software-intensive System.

## Core distinctions that matter in mixed human–AI Work

| Keep distinct | Why it matters |
| --- | --- |
| A System and a description, model, dashboard, or document about it | Changing or approving a description does not by itself change the System. |
| A Method, a MethodDescription, a WorkPlan, and actual Work | A procedure or plan does not prove that capable Work occurred or produced its intended result. |
| Architecture, an architecture description, and an architecture decision | A diagram is not the structure; a selected structure is not automatically realized. |
| Capability, assignment, permission, responsibility, and authority | A person, team, tool, or AI agent may have one relation without the others. A title or technical ability establishes none of them by itself. |
| A claim, its evidence, assurance about reliance, and the decision that uses it | Fluent text, a passed test, or a source citation does not support every nearby conclusion. |
| Result dependency, planned Work order, actual Work order, and teaching order | Each answers a different question. None should be inferred from document order. |
| A local decision and a continuing Method or culture | One successful case does not prove transfer, institutional retention, or universal applicability. |
| A narrative rendering and its source structure | Readability and engagement do not guarantee source fidelity, causal validity, or recoverability. |

## What FPF is not

FPF is not:

- an AI-agent framework, agent runtime, orchestration library, memory service, or autonomous-action permission;
- a software-coding framework, although software-intensive Systems are legitimate engineering subjects;
- a prescribed workflow, project-management methodology, lifecycle, or universal sequence of stages;
- a checklist bureaucracy or a compliance scheme built around official standards;
- a claim that one school, standard, toolchain, model, or institutional consensus is the whole state of the art;
- a replacement for domain expertise, direct observation, experiment, measurement, professional judgement, or legally valid authority;
- a demand that a human read the full specification before obtaining a useful result;
- a guarantee that every project needs every pattern or every DPF.

FPF is most useful when the cost of semantic drift, hidden assumptions, premature convergence, lost handoffs, ungrounded AI output, weak architecture decisions, evidence gaps, rework, or unreviewable collective Work exceeds the cost of using a disciplined pattern language.

## Publication and use status

This README is a public entry point, not the normative specification. It deliberately coarsens and omits detail. When a claim becomes important, inspect the exact pattern body, definitions, checks, source uses, and stop or reopen conditions in [FPF Core](FPF-Spec.md) or the relevant DPF.

The Library's publications are an **eternal alpha**: they are usable now and continuously revised as their sources, working situations, patterns, and evaluations change. AI agents should expose the source edition or snapshot they used whenever currentness matters.

## License and reuse

The original FPF and DPF content by Anatoly Levenchuk, including the DPF Suites and the Narrativization DPF, is available under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): you may share and adapt it, including commercially, with attribution, a license link and an indication of changes. See the [licensing scope (Licensing FPF and its DPF publications)](LICENSING.md) for the full notice and third-party and software boundaries.

You choose the license for your own original DPF or LPF. Using FPF methods or its publication form does not impose CC BY on your work. When sharing licensed FPF or DPF text under CC BY 4.0, preserve its attribution and comply with the license. Where your use needs no copyright permission, including under an applicable exception, these conditions do not apply. The license has no ShareAlike requirement.

## Citation

```text
Levenchuk, Anatoly. FPF Library.
GitHub repository: https://github.com/ailev/FPF
```

For a specific claim or method, cite the publication, edition and pattern used.
