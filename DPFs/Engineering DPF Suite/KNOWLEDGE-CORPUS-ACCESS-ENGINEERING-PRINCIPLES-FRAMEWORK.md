# Knowledge-Corpus Access Engineering Principles Framework

**DocID:** `KCAE` within **FPF Library**.

Methods for designing, using and changing access to documentary knowledge.

# Table of Contents

**Reader entry and explanation**

| Publication unit | What it helps you do |
| --- | --- |
| [Knowledge-Corpus Access Engineering Readme](#knowledge-corpus-access-engineering-readme) | Enter through a present access problem. |
| [Knowledge-Corpus Access Engineering Principles Framework Architectural Reference](#knowledge-corpus-access-engineering-principles-framework-architectural-reference) | Understand the field, the relations among its methods and one complete construction. |
| [KCAE.Reference:1](#kcaereference1---the-working-problem-and-the-governed-object) | The working problem and the governed object |
| [KCAE.Reference:2](#kcaereference2---why-changing-questions-defeat-fixed-representations) | Why changing questions defeat fixed representations |
| [KCAE.Reference:3](#kcaereference3---the-objects-an-engineer-must-keep-distinct) | The objects an engineer must keep distinct |
| [KCAE.Reference:4](#kcaereference4---how-the-methods-work-together) | How the methods work together |
| [KCAE.Reference:5](#kcaereference5---alternatives-and-the-cost-of-the-whole-arrangement) | Alternatives and the cost of the whole arrangement |
| [KCAE.Reference:6](#kcaereference6---scope-preparation-and-evidence) | Scope, preparation and evidence |
| [KCAE.Reference:7](#kcaereference7---relation-to-fpf-and-other-frameworks) | Relation to FPF and other frameworks |
| [KCAE.Reference:8](#kcaereference8---using-and-changing-this-account) | Using and changing this account |
| [KCAE.Reference:10](#kcaereference10---fpf-and-dpf-supplier-returns) | FPF and DPF supplier returns |
| [KCAE.Reference:11](#kcaereference11---working-vocabulary-and-result-boundaries) | Working vocabulary and result boundaries |
| [KCAE.Reference:12](#kcaereference12---conditions-that-change-the-framework-and-its-uses) | Conditions that change the framework and its uses |

**Patterns**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| --- | --- | --- | --- | --- |
| 1 | [KCAE.USE - Choose an Access Arrangement for the Work](#kcaeuse---choose-an-access-arrangement-for-the-work) | Stable | workload, authority, source boundary, build or reuse; “What must this access system make possible?” | Uses F.1 and C.11.DUA; supplies all design choices. |
| 2 | [KCAE.SOURCE - Prepare Addressable Sources without Losing Their Context](#kcaesource---prepare-addressable-sources-without-losing-their-context) | Stable | extraction, OCR, table, section, edition, translation; “What does this searchable text leave out?” | Receives the source and use boundary from KCAE.USE; uses A.6.3.RT and NOT.5 where their transformation questions apply. |
| 3 | [KCAE.INDEX - Build Complementary Ways to Find Unknown Material](#kcaeindex---build-complementary-ways-to-find-unknown-material) | Stable | hybrid retrieval, embeddings, BM25, graph, fusion, persistent search; “How do I find a useful passage when I cannot name it?” | Uses KCAE.SOURCE addresses; evaluated by KCAE.EVAL; maintained by KCAE.CHANGE. |
| 4 | [KCAE.SEARCH - Continue a Search as the Question Develops](#kcaesearch---continue-a-search-as-the-question-develops) | Stable | query planning, corpus synthesis, direct scan, blind spot, stopping, coverage; “What should the next search obtain?” | Uses the routes actually available, including KCAE.INDEX; returns candidates to KCAE.ASSESS. |
| 5 | [KCAE.ASSESS - Determine What a Candidate Can Support](#kcaeassess---determine-what-a-candidate-can-support) | Stable | criterion, unknown, contradiction, reranking, typed decision; “Is this useful evidence or merely similar text?” | Receives source context; supplies KCAE.COMPOSE and KCAE.DELIVER. |
| 6 | [KCAE.COMPOSE - Connect Contributions to a Feasible Whole Result](#kcaecompose---connect-contributions-to-a-feasible-whole-result) | Stable | missing result, method set, shared resource, alternatives; “What else is needed, and can these contributions work together?” | Uses C.39, KCAE.ASSESS and relevant subject methods; returns missing inputs to KCAE.SEARCH. |
| 7 | [KCAE.DELIVER - Put Sufficient Source Material within the Reader's Reach](#kcaedeliver---put-sufficient-source-material-within-the-readers-reach) | Stable | context budget, packet, full reading, pagination, history; “What must the recipient actually receive?” | Uses C.2.8; receives KCAE.SOURCE, KCAE.ASSESS and, where needed, KCAE.COMPOSE results. |
| 8 | [KCAE.CHANGE - Keep Source Reading and Derived Views Coherent through Change](#kcaechange---keep-source-reading-and-derived-views-coherent-through-change) | Stable | incremental index, snapshot, deletion, generation, recovery; “What remains usable after this update?” | Preserves KCAE.SOURCE and KCAE.INDEX contracts; reopens dependent judgements. |
| 9 | [KCAE.ENCOUNTER - Arrange a Useful Encounter with Knowledge during Work](#kcaeencounter---arrange-a-useful-encounter-with-knowledge-during-work) | Stable | event, observer, quiet mode, notification, permission; “Why would the user begin this inquiry now?” | Applies A.15.11 and B.5.PI through an actual event source; uses KCAE.SEARCH and KCAE.ASSESS. |
| 10 | [KCAE.MEMORY - Reuse Connections while Keeping Open Questions Revisable](#kcaememory---reuse-connections-while-keeping-open-questions-revisable) | Stable | unresolved cue, episode, conditional memory, recognition question; “What should survive without fixing the next interpretation?” | Uses KCAE.ASSESS, KCAE.COMPOSE and KCAE.CHANGE; can supply KCAE.ENCOUNTER. |
| 11 | [KCAE.EVAL - Compare Access Arrangements by Useful Results and Full Cost](#kcaeeval---compare-access-arrangements-by-useful-results-and-full-cost) | Stable | held-out episode, ablation, no useful answer, update trial; “Which change earns adoption?” | Consumes the use from KCAE.USE and the complete arrangement; uses C.11.DUA. |

**Applications and source return**

| Publication unit | What it helps you do |
| --- | --- |
| [KCAE.Application](#applications) | Work through a large bilingual support corpus, a historical inquiry and a method library. |
| [KCAE.Profiles](#engineering-profiles) | Select replaceable retrieval, assessor and execution technologies. |
| [Source contributions and comparison boundaries](#kcaereference9---source-contributions-and-comparison-boundaries) | Recover external contributions, evidence limits, vocabulary and refresh conditions. |

# Knowledge-Corpus Access Engineering Readme

## Practical entries

These are selected examples of entry, not a catalogue or the coverage boundary. Bring the actual question. Use the index, a direct pattern or search across the publication when neither example fits. You can ask an assisting agent: “Explain this and comment in ordinary language, without framework jargon.”

### changed-reading - A search opens the wrong edition

- **Situation:** A result names a useful clause, but the opened text is newer, missing or at another location.
- **Question:** Can this result still support the work?
- **First useful result or blocker:** A coherent source reading, or a precise unavailable-edition result that prevents the unsupported use.
- **Start with:** KCAE.CHANGE:4.3, then KCAE.SOURCE when the address itself is ambiguous.
- **Stop or return:** Stop when the necessary reading is coherent; reopen its assessment if the governing content or receiving situation changed.

### Practical-Use Cards

These examples retain longer connections across methods. They do not prescribe a workflow for every query.

#### unknown-contribution - Build access for questions that do not name their sources

- **Situation:** A large changing corpus contains useful knowledge, but readers describe work in another vocabulary and cannot identify the right passage.
- **Question:** How can the system obtain a useful contribution at a sustainable cost?
- **First useful result or blocker:** A testable access design with source returns, complementary finding routes, adequate reading and honest limits.
- **Mantra:** Start from the work; preserve sources; widen finding; check the contribution; deliver enough; revisit what changed.
- **Start with:** KCAE.USE, KCAE.SOURCE and KCAE.INDEX; follow the connected construction in KCAE.Reference:4.
- **Stop or return:** Keep a sufficient existing arrangement. Reopen a route, judgement or delivery when its premise fails.

## Who this framework serves

This framework serves information and software engineers who construct or maintain access to technical publications, support libraries, research collections, organizational documentation or comparable documentary corpora. It also serves analysts who must explain an access failure or compare an arrangement supplied by others. Readers are expected to understand ordinary software interfaces, identifiers, data structures, testing and basic descriptive statistics. A named domain specialist or source owner supplies authority rules and interpretations that require that profession; the engineer obtains and carries those results rather than silently inventing them.

You can use a direct pattern without learning the whole framework. Someone who already has a sufficient source can read and apply it immediately. Engineering the access arrangement becomes useful when repeated or difficult use requires better finding, interpretation support, delivery, maintenance or encounter. The aim is to make those operations constructible and revisable, including when an adequate result is a missing fact or an unavailable source.

# Knowledge-Corpus Access Engineering Principles Framework Architectural Reference

## KCAE.Reference:1 - The working problem and the governed object

A support engineer asks how to stop a recurring export failure. The manual calls it a reconciliation failure; a release note supplies an exception; the configuration record decides whether the exception applies. The service returns a plausible retry paragraph while missing that exception. The paragraph is real, its words are relevant, and the proposed action can still be wrong. A week later the paragraph moves and the exception changes. A faster search alone cannot preserve a useful answer through these changes.

Knowledge access sits within the broader work of obtaining and using justified contributions. This framework governs the engineered access arrangement: sources and their editions, readable and searchable representations, finding and assessment operations, delivery to particular readers, and the maintenance and observation that keep those operations available. It explains how an engineer constructs and changes that arrangement. It does not determine whether every source claim is true, replace the receiving profession's judgement, or promise discovery of every future relevant distinction.

The practical gain is a way to diagnose which operation is missing and construct the connection that supplies it. A reader can build a source reader, a persistent additional search route, a bounded assessment service or an event-to-inquiry arrangement; connect them into a larger use; compare credible alternatives; and revise only the results affected by change. Software implementation still requires the ordinary engineering capability stated in the Readme. Domain approval, suitable evidence and actual deployment remain properties to obtain in the receiving setting.

## KCAE.Reference:2 - Why changing questions defeat fixed representations

An index is a purpose-selected view of source material. Its terms, vectors, extracted entities and summaries retain distinctions that help some operations and remove others. If two different passages obtain the same derived representation, a future question can depend on the difference between them. Searching only that representation cannot recover the difference. This argument concerns a lossy mapping and an unrestricted future question; it does not imply that all compression is lossy or that a well-chosen index is poor for its intended workload.

Keeping the original creates a possible second route. It helps only if the reader can reach the relevant original independently of the representation that omitted it, afford the inspection and interpret the result. A source link behind an exclusive failed category filter leaves the practical problem intact. Conversely, reading all source bytes does not establish that a person or model noticed all relevant relations. Coverage of bytes, semantic recognition and justified use are different claims.

Questions also change through inquiry. A request for more training may become a question about an unavailable approval, then a question about a shared resource. Preserve the original episode and distinguish a new question from a synonym added for retrieval. Search translations and hypothetical answers help discover candidates; they do not become case facts. This field therefore combines prepared views with query-time interpretation and routes back to sources. The balance depends on workload and available readers, rather than on a universal preference for either precomputation or agentic exploration.

This distinction has a long information-retrieval lineage. Bates's 1989 account treats searching as an evolving inquiry that collects contributions through several techniques. It is a historical source for preserving the developing question, not contemporary evidence that one software implementation performs best. KCAE.SEARCH gives the present engineering construction; KCAE.Profiles compares current implementation choices.

## KCAE.Reference:3 - The objects an engineer must keep distinct

A **source item** is a particular document, recording, data release or other authored or observed material. An **edition** identifies its particular content. A **corpus snapshot** fixes membership and the selected editions. A **reading unit** is the context needed to understand a contribution; it can span an enclosing section, definition, table note and another document. A **retrieval unit** is the unit indexed or ranked for discovery. A small retrieval unit may point to a much larger reading unit.

A **derived view** includes a text extraction, inverted index, embedding collection, graph, summary, card or transformed package. Each has a source basis and an obtaining procedure. A **route** is an available operation for reaching material, such as exact reading, ranked search, link traversal or direct block inspection. Several routes can share a blind spot, especially when all were built from the same summary. Complementarity means that their different selection grounds can expose different material; it is an engineering hypothesis to test.

A **candidate contribution** is something a source might supply to the current work: a fact, distinction, explanation, procedure, criterion, example or input for another operation. An **assessment** says what the inspected material supports under stated conditions. A **recommendation** adds that pursuing the contribution is worthwhile now. An **application result** is the actual explanation, calculation, decision or changed work obtained using it. Returning a document identifier performs none of the later operations by itself.

Keep four clocks where the use needs them: the source's edition/publication time, the period in which its rule is effective, the time at which the system observed it, and the time of the receiving action. A newly uploaded file can describe an old rule. A preserved historical rule can be correct evidence for an incident and incorrect instruction for today's operation. Authority is a separate relation: a local source owner determines which publication governs which class of decisions. File recency and retrieval rank cannot supply that determination.

The access arrangement is actual software and human work. A stored assessment is a description, not an executed repair. A skill contains instructions, not a continuously operating observer. A package version identifies distributed content, not proof that every client loaded it. These distinctions change architecture choices, so they remain visible in interfaces and examples rather than being confined to terminology.

## KCAE.Reference:4 - How the methods work together

Design begins with a receiving use and its constraints. KCAE.USE produces the workload, source roles, allowed data flow and quality/cost questions that select an arrangement. KCAE.SOURCE produces readable, addressable material with an explicit extraction boundary. KCAE.INDEX uses that material to create reusable finding routes. KCAE.CHANGE preserves the relation between those routes and sources as content changes. These are construction and maintenance operations; they need not run anew for each question.

During an ordinary inquiry, KCAE.SEARCH chooses available routes and follows what remains unknown. It returns source-addressed candidates and a coverage limit. KCAE.ASSESS opens the necessary context and relates the candidate to the receiving result. If several contributions are needed, KCAE.COMPOSE establishes the missing intermediate results, conversions and joint conditions. That can send a new query back to search, or expose a missing capability that no further corpus query can supply. KCAE.DELIVER places the needed instructions and grounds within the particular recipient's reach. A sufficient known result can enter directly at any of these points.

The apparent sequence hides important feedback. Delivery limits can change which otherwise suitable method is affordable. Assessment can reveal that the request itself presupposes a false diagnosis. A source change can invalidate an assessment while leaving an embedding technically reusable. A capability change in the executor can change the delivery design without changing the subject method. Each return follows the failed dependency; the arrangement need not start over.

KCAE.ENCOUNTER adds a separate entry when an authorized work event creates a useful occasion for inquiry. KCAE.MEMORY preserves open questions and conditional connections so that an altered source or a later episode can reopen them. Neither is necessary for a one-time explicit query. KCAE.EVAL compares the whole arrangement at the useful result and isolates component failures when that comparison calls for repair.

Consider the fictional **CedarBench** service, a large documentation corpus for data-export software. A customer says, “Nightly reports finish on time, but our senior analyst removes duplicates every morning. Can we buy faster workers?” The access design supports English and Spanish queries, current operational advice and separate historical explanation. It may read public manuals and an authorized local configuration record; private row data cannot leave the organization.

The system retains the customer's words and searches both worker throughput and duplicate reconciliation. A manual explains automated resend, an old translation omits a condition, and a compatibility table says that the destination's older protocol cannot deduplicate. The decisive case fact—the destination protocol—is initially missing. The first useful return is a request for that configuration fact, with the reason it changes the advice. Faster workers are neither selected nor ruled out by topic similarity.

When the configuration is obtained, the system connects a receipt-reconciliation method with a conditional resend procedure and a resource schedule. A receipt set must exist before missing exports can be selected. Three simultaneous exports each reserve 2 GB in a shared 5 GB cache: every pair fits, while all three do not. The composition schedules at most two together and explains what happens to the third. The recipient receives the source conditions and this connection; the engineer did not merely deliver three independently plausible names.

Revision 8 then changes the resend condition. The source reader can obtain it, but the vector build has failed. A coherent revised exact/lexical route can still serve the new edition, while the old vector view remains limited to an identified unchanged subset or an explicitly historical query. A pending recommendation derived from the changed clause is reassessed before reuse. KCAE.Application:1 provides the concrete source slices, construction and variation behind this account.

## KCAE.Reference:5 - Alternatives and the cost of the whole arrangement

A small stable dossier can be read directly. A large known-name corpus may need an exact reader and lexical index. A heterogeneous corpus with many unknown-source questions can justify persistent semantic retrieval at the outset. A structural question can benefit from explicit references or a qualified graph. A rapidly changing collection with few requests may favour direct or deferred interpretation because repeated preprocessing cannot be amortized. These are alternative answers to the workload, not maturity levels every installation must pass through.

Costs include preparation, extraction repair, storage, rebuilding, request latency, total model input, residual main context, human interpretation, interruption and the work of applying advice. Compare them over a declared time horizon. A source answer for one analyst need not require that analyst to learn the engineering framework. A local engineer may receive the method needed to construct a reusable service. Those are different acquisitions of capability and have different costs.

Persistent retrieval is particularly valuable when the same expensive source inspection can serve many later questions. Deferred interpretation is particularly valuable when questions are rare, change rapidly or need distinctions that prepared views did not anticipate. Hybrid arrangements make both available. They incur more maintenance and require truthful routing when only some views are ready. KCAE.INDEX and KCAE.EVAL explain how to make that choice testable.

The design preserves source return because compression is useful and incomplete. It separates candidate ordering from adequacy because the best result in a weak pool can still be unusable. It separates event observation from user interruption because many inexpensive internal inquiries should end quietly. It preserves query-time connections because usefulness depends on the work, while retaining stable structural links for navigation. These are the shared architectural reasons for the method set.

## KCAE.Reference:6 - Scope, preparation and evidence

The recurring domain questions covered here are use selection; source preparation; persistent and adaptive finding; candidate assessment; multi-contribution construction; delivery; source/view maintenance; authorized encounter; revisable memory; and comparative evaluation. Their necessary same-framework connections are developed in this publication. Retrieval algorithms, database engines, OCR systems, LLMs and event platforms are replaceable means. KCAE.Profiles explains how their capabilities fill the methods without making any provider mandatory.

The worked cases and numerical design examples are constructed. They expose operations, criteria, failures and changed-condition reasoning; they are not measurements of CedarBench or evidence of successful deployment. Cited research supports particular mechanisms or bounded observations at its stated scope. No benchmark on code, synthetic questions or another corpus establishes the benefit of this framework in the reader's installation. KCAE.EVAL gives the way to obtain that evidence.

Recognition comes first in every pattern: a working situation, useful result and ordinary boundary. The later conformance questions support stronger reliance and inspection. They do not turn every lightweight lookup into an audit. Where a result depends on a domain authority, available source, permission, tool capability or trained reader, the public explanation exposes that dependence at the action that needs it.

This framework does not teach every underlying software algorithm, each profession's source interpretation, human skill acquisition or every security control for a production service. It does teach how to obtain and connect those contributions where the access result requires them. A missing profession-specific judgement remains a named input, not a reassuring score. A missing source remains an access result, not evidence that the corpus contains no answer.

## KCAE.Reference:7 - Relation to FPF and other frameworks

The domain methods use FPF distinctions about selecting sources, preserving meaning through representations, reader-relative recoverability, practical burden, inquiry and noticing useful methods. C.39 supplies the general construction and repair of connected contributions. These general contributions retain their Core owners. This framework adds the engineering construction that makes them work across sources, indexes, assessors, readers and changing software conditions. Core use does not depend on this DPF.

Core's Method-development patterns supply additional operations when the material being recovered is a method repertoire; Notational Engineering supplies translation and loss analysis where a notation changes; Computational Thinking supplies representation and operation reasoning. KCAE.Reference:10 identifies the exact public contributions and their receiving use. A source citation or informative example is distinguished there from a required supplier result.

For FPF Library, retrieval returns material to the existing pattern-use and application methods. It also reaches Prefaces, References, examples and explanations that do not have a PatternID. The Library is one application, developed in KCAE.Application:3. Its installed commands, refresh jobs, release routes, service incidents and operating backlog belong to the local practice that runs that installation. They are not general KCAE methods.

## KCAE.Reference:8 - Using and changing this account

The Readme and index select entry; this Architectural Reference explains the whole; the patterns supply repeatable operations; the applications expose connected use; the profiles and references preserve source returns and replaceable engineering choices. The overview deliberately omits implementation detail and per-use evidence. Return to the named pattern when constructing an operation, to the application when a connection is unfamiliar, and to the source when a claimed mechanism or limit changes the design.

Change the smallest explanation whose promise has changed. A new source format reopens extraction and addressing. A model change reopens its question/threshold qualification. A new privacy constraint can eliminate a remote route. An altered work event can invalidate an observer. A demonstrated new kind of useful question can justify another representation or a revised recognition cue. Preserve unchanged results, and test the receiving use after the change. The edition's refresh route is KCAE.Reference:4.

## KCAE.Reference:9 - Source contributions and comparison boundaries

This is a practitioner synthesis with constructed applications. Primary research and implementation documentation supply mechanisms and bounded observations; they do not establish empirical effectiveness of a KCAE installation. The profiles above link the exact contributions used. Primary web material was inspected on 3 October 2026. A retrieval date identifies this reading; it is not an assurance that a later implementation is unchanged.

| Source line | Receiving contribution | Deliberate boundary and return |
| --- | --- | --- |
| [Bates, 1989, the berrypicking account](https://pages.gseis.ucla.edu/faculty/bates/berrypicking.html), especially the evolving-search model | Questions evolve and useful information is gathered by several techniques; informs KCAE.SEARCH and MEMORY. | Historical conceptual lineage. Does not rank modern retrieval engines. Return when the interface makes the original episode or changing question unrecoverable. |
| [Introduction to Information Retrieval, ranked evaluation](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-ranked-retrieval-results-1.html) | A mathematical basis for ranked retrieval measures and their dependence on query/relevance judgements. | Historical algorithmic reference; component relevance is not whole-work benefit. KCAE.EVAL adds that receiving comparison. |
| BM25, RRF, HNSW, ColBERT and HyDE, linked in Profiles:1 | Implementable lexical, fusion, approximate-vector, late-interaction and generated-query mechanisms. | Distinct operations with historical evidence. Select current realizations by use; source figures and parameter choices are not universal defaults. |
| Contextual Retrieval, GraphRAG, RAPTOR and LazyGraphRAG, linked in Profiles:1 | Different retained context, levels of abstraction and preparation/query cost arrangements. | Serious alternatives, not an ordinal maturity ladder. Preserve originals and inspect update and rare-distinction losses. |
| TypeSafe documentation and cookbooks, linked in Profiles:2 | Bounded typed screening, progressive candidate inspection and error-driven question development. | Provider mechanisms and demonstrations. Do not inherit synthetic accuracy, English performance, thresholds or explanatory-method exclusions. |
| Typed-decision audits, linked in Profiles:2.3 | Comparative-design and logical-coherence failure questions. | Early bounded evidence. Neither universal failure nor universal superiority follows. Reopen with changed models and better matched comparisons. |
| [AgentRetrievalBench](https://arxiv.org/html/2607.24882v1), especially natural no-gold analysis and limitations | A concrete test of how retrieval rejection behaves on naturally unsupported requests versus artificial wrong-corpus controls. | Code-retrieval evidence, not downstream task success or a support-corpus rate. Include natural no-use cases in KCAE.EVAL. |
| Provider, VibeVM and storage documentation in Profiles:3; CodeNib v2 | Available access forms, source identities, runtime loading and update guarantees at their stated scope. | Interface and bounded implementation evidence. It cannot establish that an installed reader used the source or that users benefited. Requalify the relevant contract after a version change. |

The best arrangement is unresolved until the receiving workload and comparison make the alternatives decidable. This publication adopts a source-returning, condition-aware construction because it supports those comparisons and local repairs. It rejects a universal requirement to begin with lexical-only retrieval, a universal preference for embedding/graph retrieval and a universal prohibition of dynamic loading. It also rejects treating retained bytes as sufficient access or a high retrieval score as justified use. These choices follow from the differing operations and failure cases developed in the methods, rather than from a claim that every technology has already been tested together.

## KCAE.Reference:10 - FPF and DPF supplier returns

The compatible public supplier set for the uses below is [FPF Library edition d4f6b0ba1a4db119fecf8d5b9d2b526633f2e58a](https://github.com/ailev/FPF/tree/d4f6b0ba1a4db119fecf8d5b9d2b526633f2e58a). This is an identified reproducible edition, not a claim that it is the latest. The direct linked publications contain the named sections and their operative instructions. Use a newer edition only after checking the contribution and conditions actually consumed here; an unchanged identifier alone is insufficient.

| Supplier and exact section | Result received here | Use and limit |
| --- | --- | --- |
| [FPF-Spec.md](https://github.com/ailev/FPF/blob/d4f6b0ba1a4db119fecf8d5b9d2b526633f2e58a/FPF-Spec.md), F.1:4.1–4.2 | An inspected question-relative source cut with roles, gaps and reopen conditions. | KCAE.USE/SOURCE select source bases. F.1's optional search policy is attention guidance; KCAE does not presuppose an unprovided future finding method. |
| Same Core publication, A.6.3.RT:4.1 and C.2.8:4.1–4.3 | A representation-change account and reader-relative recovery of selected structure. | KCAE.SOURCE/DELIVER preserve consequential conditions and diagnose loss. A vector view is not declared a meaning-preserving translation without its own basis. |
| Same Core publication, C.11.DUA:4.1–4.2.1 | A worthwhile, attainable continuation with full recipient burden. | KCAE.USE, SEARCH, ENCOUNTER and EVAL compare inquiry and advice with serious alternatives. It supplies no domain permission. |
| Same Core publication, C.39:4.2–4.4 | Construction from a needed result through neighboring contributions, explained joins, forward application and repair of failed connections. | KCAE.COMPOSE specializes this general construction for bounded search over partial arrangements, source-dependent joins and changing conditions. A failed candidate calls for a constructive continuation, not just a lower score. |
| Same Core publication, B.5.PI:4.1–4.6 and A.15.11:4.1–4.7 | Inquiry opened from actual work and a useful method cue with an attainable next operation. | KCAE.ENCOUNTER/MEMORY construct the access and observation support. A stored cue is not an actual encounter. |
| Same Core publication, E.11.PUR:4.1–4.3 and E.11.PUA:4.1 | Applicability, recommendation, coordination and ordinary pattern use. | KCAE.Application:3 returns FPF use to these owners. General knowledge access does not require every contribution to be a pattern. |
| [Method Engineering](https://github.com/ailev/FPF/blob/d4f6b0ba1a4db119fecf8d5b9d2b526633f2e58a/Engineering%20DPF%20Suite/METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md), ME.4:4, ME.5:4, ME.6:4 and ME.13:4 | Source-faithful method recovery, individual qualification, comparison of whole arrangements and bounded fit/transfer claims. | KCAE.ASSESS/COMPOSE and Application:3 consume these when the material is a method repertoire. A proposed connection or worked illustration remains distinct from observed enactment and transfer. |
| [Notational Engineering](https://github.com/ailev/FPF/blob/d4f6b0ba1a4db119fecf8d5b9d2b526633f2e58a/Foundational%20Thinking%20DPF%20Suite/NOTATIONAL-ENGINEERING-DPF.md), NOT.5:4.1–4.5 | A translation tied to a receiving operation, with collapsed distinctions and a usable return. | Use for tables, notation changes and the method-library example when those distinctions matter. It does not make every extraction a new notation-design project. |
| [Computational Thinking](https://github.com/ailev/FPF/blob/d4f6b0ba1a4db119fecf8d5b9d2b526633f2e58a/Foundational%20Thinking%20DPF%20Suite/COMPUTATIONAL-THINKING-DPF.md), CMP.10:4.1–4.6 and CMP.4:4.1–4.6 | Representation choice from reads/updates/full cost, and computational search with justified exclusions. | Additional construction support for KCAE.INDEX/CHANGE and finite combination search in COMPOSE. A heuristic ordering is not a sound exclusion or an optimality proof. |
| [USING-FPF.md](https://github.com/ailev/FPF/blob/d4f6b0ba1a4db119fecf8d5b9d2b526633f2e58a/USING-FPF.md) | The ordinary practical entry to finding and reading Library contributions. | Access instruction for that distribution, not this domain's universal implementation policy. Follow the instruction applicable to the distribution being used. |

These dependencies run from this DPF to its suppliers. Core remains usable independently. KCAE's software and service choices are its own engineering profiles; an organization supplies its own local installation, operating instructions and authority rules. No citation creates a deployment, role assignment, permission or positive evaluation result.

## KCAE.Reference:11 - Working vocabulary and result boundaries

| Expression | Distinction that changes use |
| --- | --- |
| Source edition / effective rule | Fixed content versus the rule governing a specified time and activity. |
| Retrieval unit / reading unit | Material convenient to rank versus context sufficient to understand or use a contribution. |
| Retained original / usable return | Preserved bytes versus an obtainable route for the actual reader, outside a failed exclusive selector where needed. |
| Derived view / source assertion | A selected or generated representation versus what the original author actually claims. |
| Candidate / qualified contribution | Material worth inspecting versus an inspected contribution under stated conditions. |
| Rank / calibration / threshold / coherence | Ordering, probability reliability, an action rule and logical relations among answers; success at one does not establish the others. |
| Recommendation / application | Advice judged worth pursuing versus an actual result of using the contribution. |
| Coherent generation / current authority | Internally matched sources and views versus permission to rely on their rule for today's action. |
| Event / projection / encounter | An occurrence, its selected representation and a recipient actually meeting a useful cue. |
| Early cue / diagnosis | A preserved unexplained distinction versus an account of what is wrong or what should change. |
| Conditional memory / standing truth | A reusable result with premises versus an unsupported assumption that its earlier conclusion always applies. |

## KCAE.Reference:12 - Conditions that change the framework and its uses

The framework's usefulness is conditional on the receiving use, adopted primary sources and available alternatives. An observed limitation, a changed use or source, or a materially better alternative can defeat a relied-on contribution. The affected method's promised result and source basis identify what has changed. Its operative explanation and application depend on the same useful connection; unaffected constructions remain available, and a material new scope or assumption changes what readers may rely on.

A new retrieval model primarily reopens representation compatibility and its workload comparison. A new corpus format reopens extraction and reading. A new language population reopens recognition and assessment. Changed provider deletion or transaction semantics reopen the update profile. A failed encounter can call for a different occasion rather than another retrieval algorithm. A reader who must invent an essential connection exposes a publication defect, even if its headings and source links are present.

A judgement of a changed contribution concerns its receiving use and an appropriate defeating condition. One corrected case, one unchanged supplier ID or a formal structure check does not establish whole-framework adequacy. [FPF E.4.DPF](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#e4dpf---domain-and-local-principle-frameworks-whether-and-how-to-author-and-publish), [FPF E.19](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#e19---pattern-quality-gates-review-and-refresh-profiles) and [FPF E.21](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#e21---fpf-pattern-quality-evaluation-characteristicspace) supply the framework-authoring, affected-use comparison and pattern-quality methods, including the independent judgement required by the applicable publication practice. Runtime evaluation under KCAE.EVAL supports an installation's choices; it does not automatically admit the publication itself.

A profile's stable domain method remains applicable unless the new evidence defeats that method. A failure in transdisciplinary source selection, representation or inquiry belongs with its existing Core owner; a failed installed command or local service belongs with that local practice. These are different change boundaries. A new technology name alone is no reason to redraw the subject boundary.

## KCAE.Reference:End

# Patterns

## KCAE.USE - Choose an Access Arrangement for the Work

> **Type:** Method pattern
> **Status:** Stable

### KCAE.USE:1 - Problem frame

Use this when you are constructing, buying or changing access to a documentary corpus and several technically feasible arrangements would serve different uses. The governed object is that access arrangement under a workload. The first useful result is a bounded design question with credible alternatives, sources, receiving results and decisive constraints. You need access to representative work and someone who can settle the relevant source authority and data-flow rules. If one known source already answers a one-time question, use it directly.

### KCAE.USE:2 - Problem

“Improve search” does not identify the result that matters. A system can increase matching passages, reduce a single model bill and still produce worse decisions or consume more recipient effort. A design chosen from a familiar tool can also make an incidental local baseline into an unnecessary prerequisite for every corpus.

### KCAE.USE:3 - Forces

Frequent similar requests reward preparation; rare novel requests reward flexible inspection. Different languages and source formats enlarge discovery but increase interpretation and extraction work. Strong currentness, privacy and latency requirements can rule out otherwise attractive routes. The engineer must compare attainable complete results rather than maximize one retrieval score.

### KCAE.USE:4 - Solution

#### KCAE.USE:4.1 - Recover the receiving operation

Observe or reconstruct one work episode. Name who must obtain what result, what they can already do, which sources and tools are available, and which error would change the next action. Write a success condition in the vocabulary of that work: “The analyst obtains the governing retry condition and the missing destination fact before suggesting automation,” rather than “The top result is relevant.” Preserve a different use when its success condition changes, such as explaining which rule was available during an old incident.

Separate the contribution supplied by access from the later domain operation. An access system may return a governing clause and comparison evidence; a qualified domain engineer still approves an equipment change. If the user expects the system to perform that approval, the arrangement needs the relevant capability and authority, not merely a better source link. Establish which receiving results are to be supplied by people, software or a coordinated combination.

#### KCAE.USE:4.2 - Establish the source and authority boundary

For every source class that can change this use, obtain its membership, edition rule, applicable authority and access conditions. Ask the responsible owner what makes a source current for this decision and what happens when sources disagree. Keep a record precise enough to implement that decision: for example, “Published English administrator manual governs supported automation; the localization assists interpretation; release notes override the named clauses from their effective date; the installed destination version comes from the configuration service.” This is a supplied organizational rule in the example, not a universal hierarchy of document types.

Distinguish source unavailability, lack of permission, extraction failure and a source known to contain no relevant passage after an adequate bounded inspection. They imply different next moves. A provider's inability to expose historical editions limits historical reproducibility even if it rejects a stale snapshot identifier. When authority is disputed, obtain the owner's decision or return competing conditional readings; do not resolve the dispute by upload date.

Define the data boundary for each route. Public source text, a private query, case records, assessor prompts, logs, caches and recipient messages are separate flows. A remote model may be permitted for a public manual while the event description must stay local. Construct a permitted projection or use a local alternative. Removing a name does not by itself establish that sensitive meaning has been removed; have the responsible data owner settle the permissible projection at the grain the use requires.

#### KCAE.USE:4.3 - Turn anticipated use into a workload

Sample real requests and failures when available. Include known-name lookup, uncertain vocabulary, cross-document synthesis, historical use, no useful advice and source changes. Record approximate corpus size and growth, request rate, update rate, language/format distribution, acceptable latency, required source return and recipient preparation. Distinguish observations from forecasts. If no log exists, construct explicit scenarios and treat the workload as a design assumption to revisit after use.

Select a finite horizon and identify who bears each cost. Build and extraction costs occur before requests; maintenance follows changes; discovery and reading occur per question; interpretation and action burden fall on the recipient. Retention and notification add separate costs. Shared work is counted once, while costs displaced to a colleague remain costs. KCAE.EVAL supplies the comparison method; the workload supplies its population and use conditions.

#### KCAE.USE:4.4 - Compare complete feasible arrangements

Construct at least the credible existing or simple arrangement and the proposed alternative at the same receiving result. A small dossier can use full reading with a cache. A large evolving corpus can use full-text plus semantic retrieval and independent block inspection. A structured codebase can use qualified symbol navigation. Include what each needs for source preparation, assessment, delivery, updates and recovery. An unsupported capability such as history deletion makes an arrangement unavailable until that capability is supplied.

Eliminate a choice that violates a hard condition before comparing cheaper variants. Then compare quality and cost by workload segment. An untested semantic route can be a reasonable initial design hypothesis for frequent cross-language questions; it does not need an artificial history of lexical failures to be considered. Equally, a graph is not earned by its name: identify the relations its intended queries actually require and the cost of maintaining them.

Use a break-even calculation only for commensurable quantities. Suppose A costs 180 engineering minutes to prepare, 8 minutes per source change and 6 minutes of recurring human effort per request. B costs 780 minutes, 28 minutes per change and 2 minutes per request. For N requests and U changes, B uses less of this measured/estimated effort when 4N exceeds 600 + 20U. With U = 10, that is N greater than 200. These invented values omit model charges and elapsed delay, which remain separate constraints. Neither arrangement is acceptable solely because its effort total is lower; it must supply the required result.

#### KCAE.USE:4.5 - Return the design basis and its reopen conditions

The result identifies the chosen or proposed arrangement, first usable result, alternative retained for comparison, unknown premises and observations that would change the choice. Feed source requirements to KCAE.SOURCE, discovery requirements to KCAE.INDEX, delivery capability to KCAE.DELIVER and adoption questions to KCAE.EVAL. A single concise account can carry this basis; no mandatory per-query form follows.

### KCAE.USE:5 - Archetypal Grounding

CedarBench receives repeated unfamiliar-language support requests over a large corpus. Persistent full-body semantic retrieval is selected for comparison from that workload, alongside lexical and exact routes. The installed protocol remains local; only public text and an authorized abstract query may leave the organization. In a second use, an analyst asks which of three known documents was available during an earlier incident. Direct reading of those editions is sufficient. The same source collection supports two different access choices because the receiving operation changed.

### KCAE.USE:6 - Bias-Annotation

Logs favour questions users already know how to ask. Include episodes where they compensated manually or abandoned inquiry. Engineers also tend to omit the recipient's reading effort and the maintainer's recovery work; obtain those costs from their actual performers.

### KCAE.USE:7 - Conformance Checklist

Can the named recipient obtain the stated result with the supplied preparation and tools? Is source authority obtained independently of ranking? Are private data flows explicit? Does the comparison include a credible simpler arrangement and the same required quality? Are forecasts and unknowns marked where they affect selection?

### KCAE.USE:8 - Common Anti-Patterns and How to Avoid Them

Starting with “add vectors” hides the workload that could justify them; reconstruct the receiving uses first. Requiring every corpus to fail an exact-term search before considering a persistent semantic route hides foreseeable repeated need; compare feasible arrangements directly. Treating the newest file as governing confuses observation with authority; recover the owner's applicable rule.

### KCAE.USE:9 - Consequences

The design becomes explainable and testable. Acquiring representative episodes and authority information costs effort, but it prevents implementing a fast answer to the wrong question. The result can legitimately be retention of the existing arrangement or a bounded missing-capability decision.

### KCAE.USE:10 - Architectural Rationale

Workload and receiving result connect all later engineering choices. A global technology ranking cannot express their different constraints. Keeping authority, access and cost separate also prevents a cheap but impermissible route from winning through a combined score.

### KCAE.USE:11 - SoTA-Echoing

The practice question is whether to precompute, inspect on demand or combine them. Current provider accounts support both just-in-time exploration and long-context/cached reading; the latter still has task-dependent retrieval limits. KCAE.Profiles:1 compares those mechanisms with persistent retrieval. This pattern adopts workload-specific comparison, while rejecting universal vendor or lexical-first ordering. C.11.DUA supplies the broader burden question; the domain addition is the lifecycle workload and source/data-flow contract. Reopen the choice when demand, source volatility, recipient effort or executor capability changes.

### KCAE.USE:12 - Relations

F.1 supplies question-relative source selection; C.11.DUA supplies practical burden comparison. KCAE.SOURCE realizes the chosen source boundary. KCAE.EVAL turns the design questions into evidence. All other KCAE methods can return a failed premise here without invalidating unrelated uses.

### KCAE.USE:End

## KCAE.SOURCE - Prepare Addressable Sources without Losing Their Context

> **Type:** Method pattern
> **Status:** Stable

### KCAE.SOURCE:1 - Problem frame

Use this when documents must become searchable or machine-readable, when a hit cannot be opened reliably, or when extracted text can lose a decisive relation. The governed object is the relation between an exact source edition, its extracted/segmented representations and obtainable reading context. The result is a source inventory and reader that can return that context with known fidelity limits. A clean, fully addressable source already sufficient for the use needs no new extraction pipeline.

### KCAE.SOURCE:2 - Problem

Document bytes, extracted text and meaningful source units are different. A table flattened into lines can attach a permission to the wrong model; OCR can drop “not”; a translation can omit an exception; a heading-based address can drift. A flawless embedding of the resulting text preserves those errors.

### KCAE.SOURCE:3 - Forces

Small retrieval units discriminate topics but sever context. Large reading units preserve relations but cost attention. Normalization improves matching but can erase exact identifiers or provenance. Stable identity must survive harmless movement while still revealing a meaningful edition change.

### KCAE.SOURCE:4 - Solution

#### KCAE.SOURCE:4.1 - Preserve the source and describe its provenance

Obtain an immutable source edition or make a permitted snapshot before extracting it. Preserve publisher/collection, document identity, edition, effective interval when relevant, access class and original format. Use a content digest to detect byte changes; retain semantic identity separately so that identical text in different documents is not accidentally merged. A corpus snapshot fixes a set of source editions, not merely the name of a branch that can move.

For a mutable collection, first capture a coherent set through a source-system snapshot or an approved freeze/copy procedure. A manifest computed while files are changing can describe an impossible combination. If the source system cannot provide a coherent snapshot, state the consistency limit and narrow the usable operation; do not label a best-effort crawl as an atomic edition. KCAE.CHANGE develops live and historical reading contracts.

#### KCAE.SOURCE:4.2 - Extract the relationships needed for reading

Choose the extractor by the actual carrier. Markdown and HTML can expose headings, lists and links. Born-digital PDFs can still scramble columns or reading order. Scanned documents need OCR and inspection of decisive glyphs, tables and notes. Audio/video transcripts need time offsets and returns to the original segment when tone, a demonstration or a visual relation matters. Machine-readable data needs schema, units, null meaning and provenance. Store the original alongside the extraction while permission permits it.

Define a small extraction qualification set from the source's likely failures: an exception containing negation, a multi-column page, a repeated heading, a table with merged cells, a footnote and a cross-document reference. Compare rendered source and extraction for the use-changing relationships, not only character count. Random sampling can detect wider drift, but a sample does not certify every uninspected decisive passage. Mark unqualified regions and allow direct visual or specialist reading where needed.

For a table, retain its title, row identity, column identity, units, span relations and notes. An indexed cell can be small, but its read operation expands to these relations. For example, the extracted CedarBench cell “No” is unusable. The qualified reading says “Destination protocol v1 / automatic resend / No; reconcile receipts manually; note a: receiver lacks duplicate suppression.” The source image or native table remains reachable. If OCR cannot distinguish v1 from v2, return an uncertain extraction and inspect the original before applying the condition.

Distinguish faithful extraction from an authored interpretation. A generated explanatory prefix can make an index easier to search; it remains a derived claim, with the original text separately available. Translation has the same discipline: keep source language and edition, preserve important negations, numerical units and scope, and compare the consequential reading with a competent translator or the source owner when reliance requires it. An old translation can be a search aid or historical artifact without being the current operational authority.

#### KCAE.SOURCE:4.3 - Separate finding units from reading units

Segment by intelligible source structure before imposing a token ceiling. Preserve parent headings, paragraph/list membership, table and figure ownership, explicit references and adjacent conditions. Split an oversized section into bounded retrieval units while leaving its reading unit intact. Overlap can reduce boundary losses, but blind overlap duplicates text and still does not recover a distant definition.

Give each unit a document/edition identity, a local locator, an exact source span where available and an expansion relation. Keep retrieval text, structural metadata and generated context in distinguishable fields. Record which parents or definitions a generated context used. That makes a later parent change capable of invalidating an apparently unchanged child representation.

Choose unit size using the retrieval question and the operation that consumes the hit. A broad research theme may benefit from section summaries; a protocol exception may need paragraph or cell retrieval. Keep an independent raw/full-body path so that summary selection is not the only way to reach the source. Test a question whose deciding text lies beyond the initial unit; the opening operation should recover it without requiring the user to guess its exact location.

#### KCAE.SOURCE:4.4 - Implement and test the source return

A practical exact reader accepts a source edition and a locator, then returns the requested material, its structural envelope, continuation information and the edition actually served. A pagination cursor should bind the edition and requested unit. Expose an end marker or explicit remaining extent so that truncated output cannot masquerade as complete reading. Do not rely on a line number without its edition.

When a heading moves, a semantic document/section identity can help resolve the new location, but exact historical reading still selects the old edition. When a section splits or merges, preserve explicit predecessor/successor relations and inspect them before treating them as equivalent. A fuzzy match may suggest a new location; it cannot silently establish identity or preserve an earlier judgement.

Verify build, persist, reload, find and read on a fixture that includes additions, deletions and shifted headings. Check that the returned text corresponds to the selected source, that a deleted locator yields an explicit result and that a child unit expands through the correct note. Preserve the qualification result with the extraction/version where the installation needs it. KCAE.EVAL distinguishes this mechanical correctness from useful question answering.

### KCAE.SOURCE:5 - Archetypal Grounding

CedarBench's table has two rows: protocol v1 requires receipt reconciliation; v2 permits idempotent resend after absence is confirmed. A flat extractor returns “v1 v2 No Yes” and loses the note. The engineer retains a row/column representation and source-page locator, verifies both rows against the page, and indexes each row with its heading and note. A query can now find the v1 limitation; opening it returns the complete condition. When a later PDF changes only its pagination, source content can remain semantically equal while exact page coordinates change; the new reader generation updates the locators.

### KCAE.SOURCE:6 - Bias-Annotation

Clean text collections make extraction seem trivial. Include the actual poor scans, minority language and awkward tables that the workload contains. Generated context can project the author's interpretation onto ambiguous text; mark it as derived and preserve the source ambiguity.

### KCAE.SOURCE:7 - Conformance Checklist

Can every decisive hit return to its source edition and reading context? Are source and generated text distinguishable? Were characteristic extraction failures inspected against the original? Does the reader expose truncation, inaccessible regions and uncertain mappings? Does persistence/reload preserve the same return?

### KCAE.SOURCE:8 - Common Anti-Patterns and How to Avoid Them

Indexing only summaries makes their omissions universal; retain searchable original units. Hash-only identity merges unrelated copies; include source provenance. Returning a table cell without row, column and note creates a false claim; expand the reading unit. Treating OCR as semantic proof ignores its loss boundary; qualify the relied-on extraction.

### KCAE.SOURCE:9 - Consequences

The arrangement gains trustworthy source return and reusable extraction. It costs storage and qualification work, and some formats continue to require visual or expert reading. Explicit uncertainty prevents a damaged extraction from appearing to be a confident source claim.

### KCAE.SOURCE:10 - Architectural Rationale

The source remains the basis for later questions, while retrieval units optimize discovery. Their separate identities let the system change chunking or embedding without changing what an exact read means. Preserved context dependencies make selective refresh possible.

### KCAE.SOURCE:11 - SoTA-Echoing

The practice question is how to retrieve small passages without making them contextless. Anthropic's 2024 Contextual Retrieval is a useful historical mechanism: attach context to chunks before indexing. This pattern adapts that idea by retaining generated context separately and exposing its source dependencies; it does not adopt the reported corpus-wide gains as a forecast. Full-section indexing is a simpler rival with greater per-hit reading cost. Reopen the unit design when an actual miss depends on omitted context or when expansion overwhelms the reader. NOT.5 supplies a fuller translation/loss method where notation changes; ordinary file parsing alone is not an A.6.3.RT semantic translation claim.

### KCAE.SOURCE:12 - Relations

KCAE.USE supplies the source roles and allowed use. KCAE.INDEX consumes retrieval units; KCAE.DELIVER consumes reading units; KCAE.CHANGE maintains their identities and dependencies. A.6.3.RT and NOT.5 govern their respective representation-loss questions without replacing this domain extraction and source-reader construction.

### KCAE.SOURCE:End

## KCAE.INDEX - Build Complementary Ways to Find Unknown Material

> **Type:** Method pattern
> **Status:** Stable

### KCAE.INDEX:1 - Problem frame

Use this when repeated questions concern a large corpus and the useful source, phrase or contribution is often unknown. The governed object is the reusable retrieval arrangement: indexed units, selection grounds, query operations, result combination and independent source access. Its useful result is an implemented or implementable route design that can expose material a single representation would miss. The source reader and workload must be available. If direct reading of a bounded dossier already supplies the result at acceptable cost, it is a sufficient rival.

### KCAE.INDEX:2 - Problem

A lexical system can miss another profession's vocabulary. A dense embedding can blur negation or a rare identifier. A summary tree can exclude the only branch containing an exception. Adding a second endpoint over the same summaries preserves the same omission. Merely listing these technologies leaves the engineer without the construction that joins their strengths, pays their maintenance cost and preserves a way beyond their common blind spots.

### KCAE.INDEX:3 - Forces

Prepared views reduce recurring work but cost construction and refresh. Several views increase discovery opportunities and duplicate results. Early filtering saves work and can exclude the unknown answer. Rich context improves interpretation but lowers the number of candidates that fit a fixed budget. The aim is a useful and maintainable arrangement for the workload, not an exhaustive representation of all knowledge.

### KCAE.INDEX:4 - Solution

#### KCAE.INDEX:4.1 - Specify the retrieval operations and their source units

Start with the question families from KCAE.USE and the addressable units from KCAE.SOURCE. Define what each route returns: source edition, unit identifier, matched text or span, route and query used, ranking value with its local meaning, and a way to open the reading unit. Preserve version, permission and authority metadata independently of the score. The first interface is a candidate-finding operation; it does not claim that the material supports the user's action.

Build an exact reader and an inventory enumerator even when semantic retrieval is the primary discovery route. The enumerator lists the permitted units in a selected snapshot without requiring a relevance match. It enables update validation and a direct original scan. A source corpus that cannot be enumerated can still be searched through its provider, but the independent-scan promise is then bounded by what that provider actually exposes.

Choose retrieval units by the distinctions the queries need. Index whole source bodies through bounded units, including examples, appendices and footnotes where they can matter. Index titles, controlled vocabulary and summaries as additional fields or views. Keep their source spans and derivation separate so that a hit from an explanatory prefix cannot be misquoted as original text. KCAE.SOURCE supplies the expansion from a small hit to its enclosing conditions.

#### KCAE.INDEX:4.2 - Construct views with different selection grounds

For an exact/lexical route, define normalization and fields deliberately. Preserve exact identifiers and error codes even if a second field lowercases, stems or expands terms. Decide how the languages in the actual corpus are tokenized. A BM25-style inverted index ranks term matches; a raw-text search remains useful for newly changed or unusual strings that the index does not yet represent. Test punctuation-sensitive identifiers, inflections and negation-bearing phrases on actual source snippets. Full-text relevance and exact equality are different operations.

For a dense route, select an embedding model whose language and domain behaviour can be examined on the workload. Embed source units, not only cards. Use the compatible query encoding and similarity operation; record model, dimensions, preprocessing, normalization and unit-generation versions. Keep independently built spaces separate until compatibility has been established. Comparing a new query embedding with vectors from an incompatible earlier model yields a numerically computable but uninterpretable score.

An approximate nearest-neighbour index trades search work and storage for approximation. On a manageable, representative subset, compare its returned neighbours with an exact search in the same vector space. This tests approximation, not semantic relevance. Separately judge whether the model ranks the needed source distinctions. A high approximation recall cannot repair an embedding that never captured the relevant condition. Token-level late interaction is another candidate when finer matching earns its additional representation and query cost; KCAE.Profiles:1 explains the ColBERT lineage without making it mandatory.

For a structural route, extract relations whose meaning is established: section containment, explicit source references, table ownership, edition succession or symbol definitions from a qualified code parser. Store relation kind, source basis and target identity. A query such as “what defines this symbol?” can use that structure directly. A query such as “what would improve this work?” needs additional interpretation; proximity in a document graph does not establish useful contribution.

For broad corpus questions, consider summaries or entity/community views at several scales. They can expose themes that local nearest-neighbour retrieval scatters. Retain source membership for each summary and permit leaf/original retrieval independently of the hierarchy. If an answer claims “the main objections across this corpus,” its sampling and coverage question differs from finding one useful objection. KCAE.SEARCH:4.6 constructs the coverage-to-answer operation; KCAE.ASSESS checks both its individual claims and the scope of its aggregate. A view supplies material to that operation, not the broad conclusion by itself.

#### KCAE.INDEX:4.3 - Make selection filters explicit

Apply access restrictions before material can reach an unauthorized component. Other filters are claims about the question. If the user asks about current operational policy and an authority rule selects the governing edition, use that rule; if the question asks about history or conflicts, retain the relevant older editions. Do not infer a subject/Suite filter from the first few words and then make every route inherit it.

Compare early filtering with later assessment. Early exclusion is appropriate when the predicate is reliable and required, such as an access boundary. A guessed topic is better used as one retrieval preference with a broad route still available. When a route supports only post-filtering of its first K hits, permission-safe candidate inspection may still suffer poor recall because eligible hits were below K. Over-fetching or a natively filtered index can help; measure the actual operation and report the boundary.

A route can fail because the useful document is absent, its extraction is incomplete, the model missed its meaning, the approximate search lost it, a filter excluded it, or the candidate window was too small. Preserve enough route information to distinguish these causes during evaluation. Otherwise every failure invites another model while the source never entered the index.

#### KCAE.INDEX:4.4 - Combine candidates without inventing a common probability

Run the selected routes against the same intended corpus/edition conditions. Deduplicate by source identity and overlap, while retaining which routes found a candidate. Keep competing editions distinct where the use needs them. Merge adjacent fragments into one reading candidate when their overlap would otherwise consume the budget repeatedly; do not merge conflicting source claims merely because their words are similar.

Raw lexical, vector and graph scores usually have different meanings. A simple candidate-combination baseline is rank fusion. Reciprocal rank fusion assigns a candidate the sum of 1/(c + rank) across lists in which it appears. It uses order rather than pretending that raw scores share a scale. The positive constant c controls how much top ranks dominate; the original 2009 study used 60, which is historical experimental selection rather than a universal setting. [RRF source](https://cormack.uwaterloo.ca/cormack/cormacksigir09-rrf.pdf).

Fusion still favours material with several appearances. Preserve a tested allocation for route-unique candidates before the later shortlist: for example, take a fused core, then admit the highest-ranked unrepresented candidate from each materially different route, within the same budget. Treat query paraphrases from one model as related search attempts, not independent votes proving relevance. Compare this diversity policy with simple fusion on held-out questions; keep it only where it recovers valuable contributions at acceptable cost.

For a concrete constructed pool, suppose lexical order is A, B, C and dense order is D, A, B. With c = 60, A receives 1/61 + 1/62, B receives 1/62 + 1/63, and D receives 1/61. A and B win the top two positions because each appears in both lists. The route-unique D disappears from a two-item shortlist. Retaining D for inspection may expose a cross-language exception. Its eventual usefulness must be judged from the source; its uniqueness is a reason to inspect, not evidence of truth.

Choose candidate-window size from downstream reading capacity and error costs. A pool of 100 hits is an internal search result, not a request to stuff 100 fragments into the principal agent's context. Assess and expand within the search service or separate reader where supported; deliver the sufficient result through KCAE.DELIVER. Too narrow a pool cannot be repaired by a perfect reranker, because the relevant source never reaches it.

#### KCAE.INDEX:4.5 - Provide an independent original-text route

Implement a route that can inspect source units without passing the same relevance filter. Enumerate permitted units from the snapshot, divide them into bounded reading batches, include their source addresses and necessary local context, and ask question-relative screening questions. Preserve the unprocessed extent and batch outcomes. The examiner may be a person, a generative model or a qualified typed assessor. The route can be used initially for a rare novel question, as a complement to indexes, or after a consequential suspected miss.

A first pass can ask whether a block contains a potentially useful condition, explanation or method; a second expands promising blocks into reading units. A later pass can search for an unresolved relationship across the retained sources. A single winner from each batch is unsafe where several contributions are needed: allow multiple candidates and an explicit no-candidate/unknown outcome. Scores normalized inside different batches are not globally comparable probabilities. Reassess finalists together or use separately qualified pointwise criteria.

A large corpus makes complete inspection expensive. Schedule by source order, strata or a declared sample that is independent of the failed selector; use affordable partial coverage when that can answer the current question. A stratified sample is a diagnostic route, not an exhaustive scan. If the route first chooses batches by the same summary classifier that failed, its independence has been lost. If the examiner reads all blocks but misses a cross-block relation, byte coverage has increased without semantic completeness. KCAE.SEARCH preserves both limits in its return.

#### KCAE.INDEX:4.6 - Join the routes to maintenance and evaluation

Publish each view with its source generation, covered subset and build configuration. Define readiness per operation: an exact reader can be ready before dense indexing; a graph can support containment while semantic edges remain unqualified. KCAE.CHANGE supplies coherent switching, partial readiness and deletion handling. Decide how new or changed units enter current queries while expensive views catch up.

Test complementary retrieval on cases independently authored from the working needs. Include a rare identifier, vocabulary mismatch, late exception, graph-relevant question, broad synthesis and source not represented by any summary. Measure sufficient contributions recovered within the recipient's budget, not just union size. Remove a redundant route if its maintenance and query cost earn no useful difference. Add or replace a route when a repeated consequential gap exposes a different required distinction.

### KCAE.INDEX:5 - Archetypal Grounding

CedarBench has a hypothetical snapshot of 6,000 documents and 32,000 retrieval units. Many support requests use customer vocabulary absent from the English manual. The engineer builds a lexical field preserving product identifiers, a dense field from complete source units, structural parent/reference relations and an exact reader. The query “our analyst removes double reports every morning” yields a throughput article lexically and a receipt-reconciliation note semantically. The pool retains both and opens their conditions.

A new supplier note appears before its embedding is ready. The current-source inventory and direct reader expose it; the route reports that dense coverage lags. An independent block pass can examine the new units. This is a designed integration of persistent additional retrieval and current source reading, not proof that the dense route is superior. In a three-document historical dossier, a cached full reading can replace this machinery with less total effort.

### KCAE.INDEX:6 - Bias-Annotation

Queries derived from titles favour title-based systems. Test vocabulary and relationships supplied by real work. Correlated retrievers can create apparent agreement; preserve provenance and inspect route-unique gains. Majority-language averages can hide important minority-language losses.

### KCAE.INDEX:7 - Conformance Checklist

Does the design explain source units, encoding, filters, candidate combination, source expansion and maintenance? Can the independent route reach material the principal selector excludes? Are scores interpreted locally? Can a known loss be attributed to ingestion, representation, filtering, approximation, pool size or later assessment? Has the chosen arrangement been compared at the actual reading budget?

### KCAE.INDEX:8 - Common Anti-Patterns and How to Avoid Them

Calling several searches over one card store “independent” hides a shared bottleneck; add an original-body route. Multiplying scores turns retrieval ranks into unsupported probabilities; use a declared ranking policy and a separate assessment. A graph of document mentions is not a graph of necessary method relations; interpret the receiving relationship through KCAE.COMPOSE. A failed lexical trial is not required to justify engineering a semantic route for a forecast workload.

### KCAE.INDEX:9 - Consequences

Unknown material becomes reachable through more than one selection ground, and the system can explain which parts remain unsearched. The design increases storage, update and evaluation work. It cannot guarantee future semantic completeness; it provides attainable ways to investigate consequential omissions.

### KCAE.INDEX:10 - Architectural Rationale

Prepared representations and query-time inspection solve different cost problems. Their common source-address contract makes them interchangeable and combinable, while route independence protects against compression becoming an exclusive ontology. The evaluation decides how much of that plurality earns its cost.

### KCAE.INDEX:11 - SoTA-Echoing

The current practice question concerns hybrid, graph, multiscale and agentic retrieval under a changing corpus. KCAE.Profiles:1 compares their constructions, including the historical ColBERT, HyDE, GraphRAG, RAPTOR and LazyGraphRAG lines with current source/view studies. This pattern adopts multiple candidate grounds and exact source return, adapts fusion to preserve useful unique findings, and rejects a technology-independent winner. Code-domain findings remain code-domain evidence. Reopen the selection after a changed query family, model, update regime or measured loss.

### KCAE.INDEX:12 - Relations

KCAE.SOURCE supplies units and reading expansion. KCAE.SEARCH operates the available routes for a developing question. KCAE.ASSESS decides contribution after retrieval. KCAE.CHANGE maintains source/view correspondence, and KCAE.EVAL tests marginal and whole-use value. CMP.10 can supply the underlying data-structure and operation-cost reasoning.

### KCAE.INDEX:End

## KCAE.SEARCH - Continue a Search as the Question Develops

> **Type:** Method pattern
> **Status:** Stable

### KCAE.SEARCH:1 - Problem frame

Use this when a question has no sufficient known source, when a first result leaves a consequential gap, when new reading changes what should be sought, or when the answer concerns a collection rather than one passage. The governed object is one bounded inquiry through available access routes. The result is useful inspectable material, a supported synthesis within a declared corpus scope, or a precise unresolved/access limit, with enough history to continue without repeating a failed interpretation. An already sufficient source or result is a direct exit.

### KCAE.SEARCH:2 - Problem

A fixed-query loop can repeatedly find the same plausible material. A free-ranging agent can spend its budget without reducing the important uncertainty. Both can return “nothing found” while having considered only one vocabulary or one subset. The next search must follow the receiving question and what the previous reading actually changed. A broad answer additionally needs a way to combine source claims under a declared coverage basis; finding several relevant passages does not perform that aggregation.

### KCAE.SEARCH:3 - Forces

Preserving the original question protects its meaning, while inquiry legitimately changes it. Broader exploration improves opportunity and consumes scarce reading resources. Early useful candidates justify focused reading, but can anchor interpretation. A useful stopping decision needs the limits of the available routes, not a claim of universal absence.

### KCAE.SEARCH:4 - Solution

#### KCAE.SEARCH:4.1 - Keep the question, facts and variants separate

Retain the user's wording or source episode, the receiving result, known facts and current unknowns. Add a corpus-language translation, a description of the missing result, and a rival interpretation when those can expose different material. For CedarBench, “buy faster workers” remains the request; “prevent duplicate resend” is a search hypothesis supported by the morning correction episode, not an established cause.

Generate variants from relations as well as nouns. Ask what operation might produce the missing result, what condition might defeat it and which result an already found method requires. A hypothetical answer can provide retrieval vocabulary, but any invented product, causal link or configuration remains outside the case facts. When an actual reading changes the question, state the change and preserve the unresolved part of the earlier one.

#### KCAE.SEARCH:4.2 - Select the next route by the missing contribution

Choose a route whose selection ground can plausibly reach what is missing. Known identifiers favour exact lookup. Vocabulary mismatch favours corpus-language variants or semantic retrieval. A missing definition favours structural expansion. A global synthesis can need several regions or multiscale summaries. An index blind spot or a newly changed region can justify original-block inspection. The available arrangement may supply only some of these routes; lack of a route is a capability limit.

Keep a small search state: original/current question, inspected source units and editions, useful contributions, disputed assumptions, pending source returns, covered extent and remaining resources. Avoid retaining every verbose search result in the principal reader's context. The state guides the next action; an authorized detailed log can remain outside that context for diagnosis.

For a question with several needed aspects, state what each contribution must establish and mark which remains missing or disputed. More documents about an already answered aspect do not supply another one. Compare new material by the contribution it adds, not only by whether its identifier is new. For example, ten resend paragraphs cannot replace the missing destination configuration; once the governing rule and configuration are sufficient, another synonym search needs a separate reason to continue.

The next action should have an explicit expected contribution: “Open the compatibility note to determine whether protocol v1 supports deduplication,” rather than “search more.” When the required fact is the customer's installed version, use a permitted configuration source or ask the customer. No amount of searching the public manual will establish that local fact. This is a return from finding literature to obtaining case data.

#### KCAE.SEARCH:4.3 - Read promising material and test the interpretation

Open the source around decisive hits through KCAE.SOURCE. Expand through the condition, exception, definition or example that can alter the proposed contribution. Preserve conflicts instead of choosing the more convenient passage. A preliminary score can prioritize this reading; KCAE.ASSESS turns it into a supported or unresolved contribution.

Actively seek a discriminating countercase when two readings would lead to materially different actions. If a retry paragraph appears to allow unattended resend, inspect restrictions on receiver versions and receipt state. That is targeted challenge, not a demand to read every related publication. If the interpretation survives and the receiving result is available, stop. If it fails, use the discovered condition to formulate the next question.

#### KCAE.SEARCH:4.4 - Escape a consequential blind spot

When the query family is unfamiliar, the user rejects the interpretation or the necessary result remains missing, inspect the selection assumptions. Was the corpus reduced to one department? Were examples excluded? Did every query use the same translated diagnosis? Change the relevant assumption and choose a route not bound by it. The alternative need not be expensive: a glossary term, source table of contents or colleague's exact reference may suffice.

For a direct semantic pass, use the independent enumerator from KCAE.INDEX:4.5. Partition by actual accessible source units, not by the failed relevance category. Allocate a bounded initial portion; retain source order or sampled strata, examined extent and reasons for further expansion. Inspect promising units fully and search for missing links across them. A new question can invalidate a prior “not useful” screen, so cache that result with its criterion and question rather than suppressing the unit forever.

If only part of a corpus was examined, return that extent and the practical consequence. “No adequate current automation rule was found in the inspected public manual and release notes; the supplier bulletin was inaccessible” is actionable. “There is no rule” is a stronger conclusion unsupported by that search. A complete deterministic search can establish absence of an exact string from an exact corpus; it cannot establish absence of every relevant meaning.

#### KCAE.SEARCH:4.5 - Spend and stop at the receiving result

Allocate resources to finding, assessment and the reading still required for correct use. Reserve enough for the final necessary source context; spending all capacity on candidates prevents application. Use actual tool/model limits, including latency and rate limits. Stop or narrow the inquiry when a required channel is unavailable, a hard budget is reached or additional accessible work is unlikely to change the next decision enough to justify its burden.

The judgement can be qualitative. Compare the next affordable action with continuing from the present result: what uncertainty could it remove, what action would change and what would the inspection cost? If a numerical value-of-information calculation is used, obtain its probabilities and costs independently; a retrieval score cannot stand in for those values. KCAE.USE supplies the decision context, while C.11.DUA supplies the general burden question.

Return the source candidates and why they matter, the inspected conditions, unresolved premises and any coverage limit that changes use. A short reply can preserve all of these where the case is simple. Distinguish “sufficient material found,” “current candidates rejected,” “missing fact,” “access constrained” and “budget stopped.” They imply different continuations and should remain different in a machine interface.

#### KCAE.SEARCH:4.6 - Construct a bounded corpus-wide synthesis

Use this branch when the requested contribution concerns a collection: its themes, objections, changes, contrasts or distribution of stated positions. First distinguish three results. An **exemplar** shows that a particular contribution occurs. A **thematic overview** organizes identified contributions and their differences over declared material. A **frequency claim** counts a defined feature in a defined unit population. Finding a good example answers the first question; repeatedly retrieving it cannot answer the other two.

**Set the population and the claim before choosing the aggregation route.** Specify membership, time or edition rule, permissions, and the unit about which the answer will speak. Eight current submissions, twelve stored files and eight submitting organizations can be three different populations. Decide whether earlier editions are historical evidence to compare or superseded copies to exclude from the current count. Distinguish documents that repeat one underlying report from independently produced evidence. For themes, state what “main” means in the receiving use: commonly recorded, explanatory of a contrast, or consequential to the decision. Frequency alone need not determine importance.

Obtain an inventory from the source system or KCAE.INDEX's enumerator. Keep each included unit's source identity and selected edition, its assigned reading portion, and whether the relevant content was read, excluded by a stated rule, inaccessible or still unexamined. If only a provider's selected hits are available, that is the available set; do not call it the complete collection. A broad question can legitimately produce an exploratory overview of selected material, provided the answer keeps that scope.

**Choose a route that can cover the required material at an affordable cost.** For a small dossier, a qualified reader can read every included unit, record its question-relevant claims with source returns, and compare them directly. This avoids index and summary preparation and is a serious choice for infrequent inquiries. If the material exceeds one reader's working capacity, partition the enumerated units into bounded reading portions. Give each portion the same question and inclusion rule. Split a long document without losing its unit identity; preserve the necessary cross-boundary context and reconnect claims that span portions. This direct partitioned map/reduce route is available without an entity graph or precomputed summaries.

For a large, repeatedly queried collection, use prepared summaries or communities where their saved query effort earns their preparation and update burden. Choose the regions or hierarchy levels to inspect and resolve their membership back to source units. A parent and its child summaries can describe the same evidence; several graph communities can reach one underlying document. Selection across levels, including RAPTOR's collapsed-tree profile, can find useful material without inspecting the entire population. A query-guided route such as LazyGraphRAG can allocate reading to promising communities, but the retained selection boundary still limits the answer. KCAE.Profiles:1.3 compares these constructions. Use independent original inspection to investigate consequential regions or distinctions the prepared view may omit.

**Map source material to claims that can be combined.** For each reading portion, obtain the proposed answer-bearing claim, its source units and exact passages, the relevant entity/time/condition, and any contradiction or unresolved interpretation. Preserve which words are the source's position and which relation the reader inferred. One portion may supply several themes, a counterexample, an exception or no relevant claim; do not require one winner or one positive answer. A “no claim” screen remains revisable when the question or coding criterion changes.

Carry lineage through intermediate summaries: a claim refers to its contributing source-unit set, not just to the name of the summary that repeated it. When an operation cannot preserve that lineage, use its summary to locate original passages before relying on the aggregate. Keep unread or excluded portions visible alongside positive results. A polished partial answer with no account of what it left out is insufficient input for a claimed whole-corpus conclusion.

**Reduce by meaning and source support, not by the number of summary votes.** Align claims that concern the same object, time, condition and predicate. Merge genuine paraphrases while taking the union of their underlying source-unit sets. Do not merge contrary positions or a conditional exception into the majority wording. Group the resulting claims into themes that answer the receiving question, then explain both recurring relationships and consequential differences. If an initial theme does not explain a substantial contrast, refine it and reopen the source portions whose interpretation can change; merely relabelling the final paragraph leaves the earlier coding unchanged.

For a descriptive count, define the predicate and count each eligible population unit once for that predicate. A unit may belong to several themes; disclose that those categories overlap rather than forcing their percentages to total one hundred. Retain unknown or unread units in the account of the denominator. Do not divide a relevance-selected hit count by the whole collection and call it prevalence. A claim about a wider population needs a justified sampling/estimation method and its assumptions; otherwise return the observed corpus count or a qualitative overview. The number of documents repeating a claim also does not by itself establish its truth.

Protect consequential minority evidence before compressing the answer. Maintain the supported objections, contrary cases, important qualifications and unresolved conflicts that could change the receiving decision, even when they are rare or rank poorly. Ask the relevant domain reader which differences have that consequence when ordinary interpretation cannot settle it. Reserve enough final reading and answer space for those differences, or explicitly narrow the promised answer. If intermediate claims exceed the reduction window, reduce them in further bounded groups while preserving source sets and these outstanding differences; keep the originals obtainable for the final comparison. This controls the next reading operation, not semantic loss by fiat.

**Return an answer whose scope survives the final wording.** State the population and edition basis, the supported themes or counts, material counterevidence and the unexamined or inaccessible remainder. Link decisive generalizations through their intermediate claims to originals. Verify that words such as “all,” “most,” “typical,” “increasing” and “consensus” have the required comparison or counting basis. A minority warning can be important without being typical; silence on a question is not agreement with another submission.

Stop when the intended bounded answer has adequate inspected support, consequential conflicts have dispositions, and the remaining affordable inquiry would not change that receiving result enough to justify its cost. A thematic overview can stop with a named uncovered region when the recipient accepts that narrower use. A complete descriptive count must instead obtain the necessary unit judgements or report the unresolved count; a representative estimate needs its own sampling basis. When the hard budget ends first, return a partial synthesis and the particular next region or ambiguity that matters. Reading every unit establishes an inspection extent, not guaranteed recognition of every possible meaning. KCAE.ASSESS checks the proposed answer against this basis before KCAE.DELIVER carries it to the recipient.

### KCAE.SEARCH:5 - Archetypal Grounding

#### KCAE.SEARCH:5.1 - An evolving local question

The first CedarBench query finds worker-capacity instructions. The retained episode includes duplicate removal, so the second query concerns receipt reconciliation. The source then distinguishes destination protocols. The next useful operation is a permitted local configuration read. It returns v1, redirecting the answer from automatic resend to reconciliation. If the configuration channel is unavailable, the result is a conditional answer and one precise information request. The search has made useful progress without pretending that it established the missing fact.

#### KCAE.SEARCH:5.2 - A dossier's objections, recurring themes and minority condition

Consider a constructed consultation on a research archive's proposed deposit requirements. The receiving question is: “What objections do the current submissions raise, and which conditions should the archive examine before adopting the proposal?” There are eight submitting groups, twelve source files because four are superseded editions, and two overlapping generated summaries. The declared population is the eight groups' latest submissions at the closing date. Earlier editions remain available for historical comparison; the summaries are access views. Neither adds another current respondent.

The eight short submissions fit direct reading in four portions of two, with the same question and source-role instructions. The reader opens every selected edition and returns the following claim map. These invented labels abbreviate source-addressed readings; an installed system retains the actual addresses and qualifiers.

| Current source unit | Question-relevant contribution | Place in the aggregate |
| --- | --- | --- |
| R1 | Objects to metadata-entry effort and storage cost. | Metadata effort; storage cost. |
| R2 | Objects to metadata-entry effort. | Metadata effort. |
| R3 | Objects to metadata-entry effort. | Metadata effort. |
| R4 | Objects to metadata-entry effort and storage cost. | Metadata effort; storage cost. |
| R5 | Objects to metadata-entry effort. | Metadata effort. |
| R6 | Objects to storage cost. | Storage cost. |
| R7 | Warns that publishing precise collection locations could damage a protected site. | A consequential disclosure objection, even though raised once. |
| R8 | Says metadata effort is acceptable if the archive supplies a working template. | A conditional counter-position; inspect the template premise rather than counting this as an unconditional effort objection. |

For the descriptive count, a direct effort objection means an explicit rejection of the proposed metadata workload. A conditional acceptance such as R8 is coded separately and its unresolved condition remains in the overview. For this coding, the direct metadata-objection set is {R1, R2, R3, R4, R5}; storage cost is {R1, R4, R6}. A summary of R1–R4 and another of R3–R8 both mention metadata. They supply overlapping paths to those sets, not two more respondents or two independent confirmations. An older R5 file likewise cannot increase the count. The union operation preserves five current direct metadata objections and three storage objections out of eight, with R1 and R4 in both categories.

The resulting bounded answer is: direct objection to metadata effort is the most frequently recorded objection category in these eight current responses (five of eight), followed by storage cost (three of eight). Those counts describe the submissions, not all potential contributors or the strength of an objection. R8 identifies a template condition under which the effort concern may be resolved; R7 identifies a disclosure problem that an effort/cost majority does not answer. The archive needs to inspect those conditions before treating the aggregate as support for one uniform policy. Each theme returns to its listed sources, and the important contrasting statements return specifically to R7 and R8. No inference of consensus is made from the other groups' silence about locations.

Now change one condition. R5 submits an authorized replacement before the closing date: after trying the supplied template, it withdraws the effort objection. Reopen R5's coded contribution and the aggregate that used it, leaving the other inspected claims intact. The current metadata-objection set becomes {R1, R2, R3, R4}: four of eight, so “more than half object” is no longer justified. The template contrast strengthens in a stated way, but the disclosure concern remains. The old five-of-eight result still describes the earlier snapshot; keeping the old file or an unrefreshed summary cannot make it current. If the replacement's meaning cannot be read, report four confirmed objections and R5 unresolved, rather than silently counting the previous position.

For this small, infrequently queried dossier, direct reading is the selected design: it supplies every current unit without a maintained graph. The four-portion map/reduce construction is a capacity variation of the same source route. A large archive with many repeated cross-document questions can justify prepared community summaries or query-time graph exploration, after comparing their full cost and ability to preserve the minority and changed-edition cases. Their value is not established by needing fewer summaries than original files. The stopping basis here is the inspected eight-unit population, resolved edition membership, traceable coding and stated conditions; no claim of universal thematic completeness is required.

### KCAE.SEARCH:6 - Bias-Annotation

An agent can overfit its first diagnosis and mistake additional supporting hits for independent confirmation. Preserve rival formulations and the user's rejected interpretation. Search logs also omit unseen opportunities; KCAE.EVAL needs separately authored cases to expose them.

### KCAE.SEARCH:7 - Conformance Checklist

Is the original concern recoverable? Does each expansion seek a needed contribution or test a consequential interpretation? Can the search leave the failed selector? Are case facts kept separate from generated hypotheses? Does the stop state accurately describe source coverage, inaccessible material and remaining uncertainty? For a broad answer, can the reader recover its population, aggregation units, source lineage and consequential counterevidence, and distinguish a theme from a frequency claim?

### KCAE.SEARCH:8 - Common Anti-Patterns and How to Avoid Them

Repeating paraphrases of one assumed diagnosis preserves its blind spot; reformulate the missing result or inspect the original episode. Treating no hit as absence exceeds the route's evidence; return its limit. Searching public documents for a private configuration fact wastes budget; obtain the fact from its proper source.

### KCAE.SEARCH:9 - Consequences

Search becomes a sequence of intelligible contributions to work. It may end earlier with a sufficient result or continue farther when a different route has real value. The method preserves uncertainty and cannot guarantee that the next unexamined source would add nothing.

### KCAE.SEARCH:10 - Architectural Rationale

The current gap connects earlier reading to the next operation. Preserving both the original concern and the evolving question avoids the extremes of a fixed query and aimless exploration. A truthful stopping limit supports continuation by another reader without reconstructing all search history.

### KCAE.SEARCH:11 - SoTA-Echoing

Bates's developed historical comparator already permits changing questions, several techniques and movement among sources. This pattern adopts that inquiry, rather than claiming iteration as its invention. Its engineering addition connects each unresolved contribution to available versioned routes, reading capacity, source-return operations and truthful stop states. A fixed retrieval call remains a smaller alternative when the need is stable and it suffices.

The contemporary [BRIGHT-Pro study, section 6.3](https://aclanthology.org/2026.acl-long.1705.pdf), provides bounded agentic-search failure evidence: rewritten queries can repeat unhelpful evidence, new documents can cover only one aspect, and exploration can continue after sufficient evidence was found. KCAE.SEARCH:4.2–4.5 addresses those distinct failures through contribution tracking, selector revision and a receiving-result stop. These are proposed repairs to compare in the intended workload, not a claim that this publication was tested in that study. Reopen the route policy when it repeatedly misses valuable material or spends effort without changing the result.

### KCAE.SEARCH:12 - Relations

F.1 supplies question-relative source selection and an optional search policy in the cited edition. This domain pattern realizes an inquiry through the available retrieval arrangement. KCAE.INDEX supplies routes; KCAE.ASSESS judges inspected contributions; KCAE.COMPOSE generates missing-result queries; KCAE.DELIVER transfers the necessary result.

### KCAE.SEARCH:End

## KCAE.ASSESS - Determine What a Candidate Can Support

> **Type:** Method pattern
> **Status:** Stable

### KCAE.ASSESS:1 - Problem frame

Use this when a retrieved passage, document or method description might contribute to a concrete result, or when an automated score is to affect reading, recommendation or action. The governed object is that bounded contribution judgement and its obtaining procedure. The result states what the inspected source supports, contradicts or leaves unresolved under the receiving conditions. You need the question, source context and access to necessary domain criteria. Ranking already known adequate alternatives is a narrower use; it does not require repeating their unchanged qualification.

### KCAE.ASSESS:2 - Problem

Similarity, authority, truth, applicability and worthwhile intervention answer different questions. An assessor can rank candidates accurately while recommending the best of an entirely inadequate pool. A binary output can turn missing facts into rejection. A polished explanation can invent a criterion that the responsible domain never supplied.

### KCAE.ASSESS:3 - Forces

Cheap screening saves reading; decisive conditions can lie outside the screen. Explicit criteria improve repeatability; fixed criteria can omit a new kind of useful contribution. A typed result simplifies integration but cannot establish its own grounds. Stronger automation requires stronger evidence than ordering the next paragraphs to read.

### KCAE.ASSESS:4 - Solution

#### KCAE.ASSESS:4.1 - Derive the question from the receiving decision

Name the decision affected by this assessment. For screening, ask whether deeper reading could supply a needed contribution. For substantive use, ask which result the candidate can produce or support, under which conditions and with which available inputs. For a recommendation, add whether that result is still needed and worth the recipient's burden. Use separate results when these questions can have different answers.

Construct the criterion from the work and the source. Recover the source's claim or described operation, input requirements, result, scope and exceptions. Obtain domain-specific standards from the responsible source or expert. Compare these with the case facts. If the criterion itself is disputed, return that question to its owner; a general evaluator cannot create the domain's acceptance standard from confidence.

For open-ended material, allow an explanatory distinction or a useful question to count as a contribution. Do not filter everything through “does this call a tool?” A method for understanding a conflict can be useful even when its immediate result is prose. Conversely, mentioning the same topic does not show which missing result the material supplies.

#### KCAE.ASSESS:4.2 - Build an inspectable claim-and-condition reading

Extract the decisive source proposition with its exact location and necessary context. State the proposed correspondence to the case and why it matters. For every decisive premise, distinguish source support, contrary evidence, missing information and unresolved conflict. These states concern evidence for this use, not a universal many-valued logic.

In CedarBench, the inspected manual says that automated resend requires a deduplicating receiver and confirmed absence of a receipt. The case says that duplicates are being removed manually. It does not state receiver protocol or receipt status. The assessment therefore supports the source rule while leaving its applicability unresolved. “There are duplicates” neither proves nor disproves either prerequisite.

After a configuration read supplies protocol v1, the table contradicts the deduplication prerequisite. Automatic resend is unsuitable on that basis; receipt reconciliation can remain useful. A current correction to the table can reopen this judgement. If two authorized sources disagree and precedence is unresolved, return the conflict and its practical effect rather than quietly choosing the higher-scoring source.

Before treating passages as contradictory, align their product or entity, operation, time, scope and exceptions. A draft proposal and an approved rule have different roles; two instructions for different protocols may both hold. For multilingual claims, inspect the specific expression or relation that carries the difference, using a competent translator or established glossary when needed. If the original is unavailable, report the apparent disagreement in the accessible material and the original passage needed to settle it.

A negative reading must have its scope. “This paragraph supplies no evidence of receiver capability” does not imply “the receiver lacks capability.” Where the corpus is known exhaustive for a specific closed predicate, absence may have a defined meaning; obtain that contract explicitly. Most natural-language corpora are not closed in that way.

For a corpus-wide answer, assess two levels separately: whether the source passages support each intermediate claim, and whether their coverage, unit definitions and aggregation support the final scope. KCAE.SEARCH:4.6 supplies that construction. A correct quotation from one response cannot establish what most respondents say. Inspect the originals behind decisive generalizations and contrary cases, and check whether merged claims preserved time and conditions. Confirm that duplication, excluded material or unassessed units did not silently change the denominator or turn a selected overview into a population claim. Return the supported narrower answer when the broader inference remains unjustified.

#### KCAE.ASSESS:4.3 - Select the performer and output contract

Use deterministic code for an exact edition match, permitted identifier, numeric calculation or enumerated rule once its semantic inputs have been established. Use a person or language model for interpretation where needed. A typed assessor can answer bounded questions repeatedly at low cost; a generative reader can extract and explain the grounds. A domain specialist may be required for a disputed interpretation. Choose by the actual operation and evidence, rather than making one model perform everything.

A useful machine contract returns the criterion, relevant source addresses, established and unknown premises, proposed contribution, result kind and model/rule version where applicable. A small human answer can express the same information in ordinary prose. If the assessor cannot generate evidence spans, pair it with a separate retrieval/extraction operation and inspect their agreement. The numerical output alone does not supply provenance.

Keep retrieved text as source data. Pass controlling instructions and allowed actions through the trusted interface. A passage that asks the system to rank it first is not an authority over the evaluator. Test adversarial additions actually delivered to the model; deleting them before the call tests the filter instead. New relevant evidence can legitimately change the judgement, so distinguish it from unsupported persuasion.

#### KCAE.ASSESS:4.4 - Qualify scores for their intended decision

Ranking, calibration, classification at a threshold and agreement among logically related questions are separate properties. A probability distribution over a supplied group is conditional on that group. It can confidently prefer an inadequate candidate when none of the choices is suitable. Keep an explicit adequacy question and permit unresolved/no-useful-candidate results.

When candidates are split into groups, do not compare their locally normalized Choice probabilities as one global distribution. Screen with stable pointwise criteria or jointly reconsider finalists under the same question. For a multi-contribution result, assess the actual composition; multiplying unrelated usefulness probabilities assumes dependence facts that the model has not supplied.

Bind an adequacy result to the candidate actually returned. Suppose a ranking selects A, adequacy scores are A = 0.2 and B = 0.8, and an illustrative screening threshold is 0.3. The maximum score establishes only that some candidate passed; it cannot qualify A. Test the selected candidate's score and source conditions, choose an independently qualified alternative, or return the shortlist for another judgement. Preserve candidate identity, criterion and source context across that selection boundary.

Choose thresholds on development cases representative of the action and evaluate them on separate cases. Retain model, prompt/question, option order/wording, preprocessing, language, source scope and decision cost with the setting. Test near misses, unknown facts, late conditions, all-inadequate pools, longer inputs and meaningful negations. Recheck the affected qualification after a model or criterion change. The same threshold need not govern cheap further reading and a costly user interruption.

Where a score is useful only for ordering inspection, keep that limited claim and avoid pretending to have calibrated adequacy. A human can read the highest-ranked candidates and make the stronger judgement from source evidence. This often provides a viable first arrangement before fully automated recommendation is justified.

#### KCAE.ASSESS:4.5 - Return the contribution and the next useful move

Return an accepted bounded contribution, a reasoned rejection, an information request, a conflict or a need for deeper reading. State what would change the result. If the selected method requires a missing intermediate result, send that requirement to KCAE.COMPOSE or KCAE.SEARCH. If the contribution is already available, reuse it and avoid an unnecessary recommendation. Keep recommendation and application distinct: explaining why reconciliation would help does not reconcile the receipts.

### KCAE.ASSESS:5 - Archetypal Grounding

An assessor gives the retry article a high score for the duplicate-report query. Its first valid use is to order reading. Full reading reveals the receiver and receipt prerequisites. With neither case fact available, the returned result is “Potentially relevant rule; obtain destination protocol and receipt state before selecting automatic resend.” Protocol v1 then defeats the automation branch while retaining reconciliation. The useful result changes because a premise was established, not because the model became more confident.

### KCAE.ASSESS:6 - Bias-Annotation

An option list can force every case into familiar contributions. Include an unresolved outcome and inspect a sample without the existing labels. Fluent models can conceal missing domain criteria; require the source or responsible judgement that supplies the criterion. Repeated calls reveal variability but are not independent evidence of truth.

### KCAE.ASSESS:7 - Conformance Checklist

What decision will consume the result? Where did its criterion come from? Are source claims and case facts separate? Are missing and contradictory conditions distinguished? Can the grounds be inspected? Does score qualification match this model, question, language and action? Is an adequate existing result allowed to end the process?

### KCAE.ASSESS:8 - Common Anti-Patterns and How to Avoid Them

Promoting a screening score into an action approval skips source reading and domain criteria. Using low confidence as proof of corpus absence confuses assessment with search coverage. Summing group probabilities creates a fictitious common scale. An action-only filter discards explanatory methods; assess the needed contribution instead.

### KCAE.ASSESS:9 - Consequences

The recipient receives a usable conditional judgement rather than a mysterious rank. More premises can remain visibly unresolved, which is preferable to silently guessing them. Full automation may be narrower than the set of cases the system can assist.

### KCAE.ASSESS:10 - Architectural Rationale

The criterion, evidence and decision are separate so that a component can be replaced without changing the meaning of its output. Open unknowns allow an information-acquisition operation to complete a case; a single positive/negative score would obscure that continuation.

### KCAE.ASSESS:11 - SoTA-Echoing

Current typed-decision practice offers cheap bounded outputs, but the Jev documentation and recent audits distinguish input-output capability from comparative accuracy and logical coherence. KCAE.Profiles:2 gives their bounded contribution. This pattern adopts typed screening where qualified, adds explicit source/condition recovery, and retains a generative or expert reader as a serious alternative. The audit evidence changes score interpretation, not the public domain's acceptance criteria. Reopen the qualification when its inputs, model, question form or action costs change.

### KCAE.ASSESS:12 - Relations

KCAE.SEARCH supplies candidates and coverage limits; KCAE.SOURCE supplies context; KCAE.COMPOSE consumes qualified contributions; KCAE.DELIVER conveys the result. For FPF methods, E.11.PUR remains the owner of fit, recommendation and coordination judgement; A.3.1.DR, A.3.1.QM and C.32.MWA.PP and A.3.1.FT supply their declared method-recovery and transfer contributions.

### KCAE.ASSESS:End

## KCAE.COMPOSE - Connect Contributions to a Feasible Whole Result

> **Type:** Method pattern
> **Status:** Stable

### KCAE.COMPOSE:1 - Problem frame

**Use this when** the work needs several contributions, one candidate leaves a required result unprovided, or individually suitable methods interact through a common resource or condition. Three relevant procedures can be a useless recommendation if none obtains the input needed by the others. Two good methods can be alternatives rather than steps in a sequence. A compatible pair does not establish a compatible whole.

The gain is an explainable, feasible arrangement of contributions, with outstanding inputs and alternatives visible. Do not use this pattern to turn every source into a workflow. A sufficient explanation or single method can be delivered directly. The receiving discipline still supplies the methods themselves and the criteria for their results.

### KCAE.COMPOSE:2 - Problem

Retrieval ranks items; useful work often requires a set and connections that are absent from the ranking. Similarity, co-citation and adjacent storage do not tell the engineer which result must feed which operation. Selecting the highest individually scored methods can also miss a complementary set whose members are weak alone.

### KCAE.COMPOSE:3 - Forces

Searching every subset is expensive. Pruning by a familiar category can remove the only useful complement. Explicit links save repeated reasoning but age with the sources and receiving situation. More methods can improve coverage while making the whole too costly, too slow or impossible to execute.

### KCAE.COMPOSE:4 - Solution

C.39:4.2–4.4 supplies the general construction: recover a neighboring contribution, work backward from the needed result, explain the joins, then follow the proposed way forward and refine only consequential gaps. The domain work here is to obtain those contributions from a changing corpus, retain several source-qualified partial arrangements, and revise them when a missing contribution or failed connection changes the search.

#### KCAE.COMPOSE:4.1 - Work backward from the receiving result

State the result to be obtained in terms that permit inspection. “Use three patterns” is an inventory objective; “identify which exports are absent without resending an already accepted export” is a receiving result. Recover each candidate's required inputs, produced results, conditions, performer capabilities and resource demands from sufficient source context. Where the source leaves an essential relation implicit, obtain the interpretation from an appropriate reader and label it as interpretation.

Start with a candidate that can produce the receiving result. For each missing required input, ask whether it is already available, can be obtained from the case, or requires another method. Search for that missing result, preserving its meaning. Continue backward until each necessary starting input has a real provider or an explicit unresolved dependency. A circular promise that A will provide B's input after B supplies A's input is not a completed construction; identify an initial value, iterative procedure or outside provider that actually breaks the cycle.

Explanations, distinctions and criteria can be intermediate results. A diagnostic distinction may be needed before choosing an action. Do not exclude it because it is not itself executable software.

#### KCAE.COMPOSE:4.2 - Establish the connection, not just the adjacency

For each proposed connection, compare the actual output with the required input. Check what it denotes, granularity, units, source edition, time, authority and applicable population. A daily count is not a list of individual export identifiers. A list of transmitted identifiers is not proof that the destination accepted them. A percentage of completed jobs cannot silently become a probability of success for a different job.

When the two sides differ, name and obtain a conversion. This may be a deterministic transformation, another method or an expert judgement. State the information it loses and the receiving criterion it preserves. If the required conversion cannot be supplied, the methods do not yet connect. Renaming an output field cannot repair incompatible meanings.

Keep a small explanation of the relation: which result supplies which need, under which case conditions, on which source basis. This can be an annotated diagram, table or ordinary prose; a graph database is optional. Source-authored cross-references remain source relations. A connection inferred for this case remains a situated judgement. Do not silently promote it into a timeless assertion about every use of either method.

#### KCAE.COMPOSE:4.3 - Compare alternatives before selecting the whole

Distinguish a sequence, concurrent work, mutually exclusive alternatives and supportive explanation. A prerequisite must be obtained before the dependent step. Concurrent work requires the shared conditions to hold together. Alternatives offer different ways to obtain the same needed result; listing them together does not authorize doing both.

For a small set, enumerate the feasible combinations. For a large set, retain a bounded frontier: start with several promising receiving methods; expand each at its unresolved inputs; reject combinations with demonstrated contradictions; and retain distinct ways to complete the result. A beam width or a search budget is a declared approximation. It offers tractable search, not proof that the retained set is optimal. Inspect some excluded paths when a cheap screening rule could hide complements. If exact optimality matters, formulate the actual finite optimization problem and obtain an algorithm and assumptions that justify that claim, rather than relabelling heuristic ranking.

A partial arrangement needs enough retained meaning to continue: the receiving result, selected contributions, already obtained results, still missing results, proposed joins, known failed conditions, source editions and remaining search or execution allowance. Keep “result obtained” distinct from “a method could produce it.” In software these can be fields; in a small inquiry an annotated sketch is sufficient. Two arrangements that mention the same methods can differ because one has obtained a required case fact and the other has not.

Choose an unresolved contribution whose possible answers can change completion. Search by the result it must provide, its receiving meaning and necessary conditions, rather than by all the outgoing links of a favored candidate. Add a new candidate to each partial arrangement it can actually extend; qualify its source and joins before treating the extension as feasible. An unknown condition calls for a case fact or a conditional branch. A demonstrated failed join calls for a supplied transformation, a replacement contribution or another arrangement. Merely lowering that arrangement's score does not construct the repair.

Retain materially different alternatives within the budget: for example, a fast route requiring a receipt capability and a slower route that works without it. Prune a branch on a demonstrated failed necessary condition, or on a justified dominance comparison under the same result and conditions. Do not call unlike results dominated because one has a lower retrieval score. If a budget forces removal of an unresolved branch, retain that search limit in the return; do not describe the remaining candidate as the only possible solution.

Assess each whole for result sufficiency, dependencies, total burden and risks. Do not sum normalized within-group selection probabilities as the value of a set. Do not discard a method merely because its independent value is small: receipt reconciliation and safe resend can jointly solve a problem that neither solves alone. Compare that set with a direct manual reconciliation alternative under the same receiving result.

For example, a mapping from local job IDs to destination IDs may have almost no standalone value to the user. Retain it when it supplies the exact connection between a useful local record and an acceptance check. Its correctness, source basis and cost still need qualification. Neither the mapping's low direct task score nor its small size is a reason to discard the only valid join.

#### KCAE.COMPOSE:4.4 - Check joint constraints and scheduling

Collect the resources shared across the whole: a person, permission, device, context window, budget, time interval, data store or physical capacity. Add simultaneous demands where addition has the right meaning; do not add incomparable quantities. Check global conditions as well as pairs.

In CedarBench, three exports each reserve 2 GB and the cache has 5 GB. Every pair needs 4 GB and fits. The whole needs 6 GB and does not. A schedule with two concurrent exports followed by the third removes that particular conflict, provided the first pair releases its reservation. It can still violate a deadline. If each export takes ten minutes and the window is fifteen, this schedule needs twenty minutes and is infeasible. The recommendation must then reduce concurrency demand, change capacity or change the accepted completion condition; simply ordering the steps has not solved the original problem.

Check interference that is not a scalar sum: two methods may mutate the same source, require incompatible configurations or use one judgement as if it were independent evidence for the other. Include transition and cleanup work. “Each method is applicable” and “this whole is feasible now” are different conclusions.

Consider a ten-minute serial work window. The receiving operation B takes four minutes and requires result R. Candidate A obtains R in nine minutes. A followed by B takes thirteen minutes and fails the window. Preserve B and its unsupplied need; search for another way to obtain an equivalent R in at most six minutes, including the joins and preparation. Candidate C supplies the same R under the case's source conditions in five minutes, so C followed by B takes nine and fits. This search constructs an alternative that rejecting A+B alone cannot produce. It does not establish that C is the best possible supplier.

If a new source edition makes C take seven minutes, reopen the partial arrangement whose feasibility used that estimate. C+B now takes eleven minutes. Retain B's still-valid contribution, seek another supplier or a permitted change of schedule, and return the unsatisfied window if neither is available. Do not reuse the earlier nine-minute judgement merely because the method names stayed the same. The durations in this example are constructed assumptions, not measurements of a deployed system.

#### KCAE.COMPOSE:4.5 - Run the construction forward and return the alternatives


Use concrete case values or a minimally realistic example. Starting with the declared inputs, produce each intermediate result and verify that the next operation can consume it. This exposes missing identity mappings, transformations, conditions and capability assumptions that a backward diagram can conceal. A hypothetical execution explains the construction; an observed application supplies stronger use evidence and should be labelled separately.

Return the selected arrangement with its result, source grounds, joining operations and unresolved conditions. Include a meaningful alternative when the choice depends on cost or uncertainty the recipient must decide. If the only feasible continuation is obtaining a case fact or involving a qualified person, say so. Store reusable relations with the conditions and dependencies that made them valid. KCAE.CHANGE and KCAE.MEMORY can then reopen them when those conditions change.

### KCAE.COMPOSE:5 - Archetypal Grounding

CedarBench's receipt method produces destination-accepted export IDs. A set-difference operation compares them with the intended export IDs and produces the missing IDs. The resend procedure consumes those missing IDs only when the destination supports the stated deduplication protocol and a stable batch identity is available. The operations connect through IDs with a common meaning and batch boundary, not through their shared word “export.”

If the destination supplies only a count, the set difference is not available. Search for a way to obtain identity-bearing receipts, or select a manual reconciliation method whose input really is available. If protocol v1 lacks the required deduplication behaviour, acquiring the IDs does not make unattended resend safe. That changed condition selects another whole rather than a lower score for the same sequence.

### KCAE.COMPOSE:6 - Bias-Annotation

A favourite method can become the anchor around which every other result is forced. Compare a different receiving method and a smaller whole. A known taxonomy can hide an explanatory contribution or an unfamiliar intermediate result; use missing-result queries as well as named categories. A diagram can disguise conjecture as a certified interface; retain the source and case basis of each consequential link.

### KCAE.COMPOSE:7 - Conformance Checklist

Can the receiving result be recognized? Does every required starting input have a provider? Do outputs and inputs match in meaning, units, time and authority? Are conversions supplied? Are alternatives distinguished from jointly performed operations? Does the complete resource schedule fit? Can a forward case traverse every link without inventing an essential step?

### KCAE.COMPOSE:8 - Common Anti-Patterns and How to Avoid Them

A top-five list supplies no composition; expose the missing results and connections. A pairwise compatibility matrix can miss a whole-set overload; calculate the total under the schedule. A topic graph is not a method architecture; qualify the relation required by the current result. An unbounded search for the best possible set delays useful work; use a stated approximation and preserve its limit.

### KCAE.COMPOSE:9 - Consequences

The recipient can explain why the selected contributions work together and where the arrangement could fail. This requires more context than ranking alone. The work is justified when missing joins, complementarities or shared constraints can change the outcome; a single sufficient contribution remains a legitimate smaller solution.

### KCAE.COMPOSE:10 - Architectural Rationale

Source material, situated relations and execution are separate because each can change independently. A reusable relation saves work only within its conditions. Backward construction exposes required providers; forward execution exposes mismatches; whole-set checking exposes constraints no individual assessment can see.

### KCAE.COMPOSE:11 - SoTA-Echoing

A.3.1.DR, A.3.1.QM and C.32.MWA.PP and A.3.1.FT supply recovery, qualification, architecture comparison and transfer methods for method repertoires. This pattern consumes their results in an access arrangement and develops the retrieval-to-connection interface, bounded combination search and source-dependent reuse. Computational search is a serious implementation choice when a finite candidate space and constraints can be stated; a conversational proposer is another, with an explicit inspection burden. Neither receives an optimality claim from plausible output. Reopen the choice when the candidate population or cost of missed combinations changes.

### KCAE.COMPOSE:12 - Relations

KCAE.ASSESS supplies qualified contributions. KCAE.SEARCH obtains missing contributions and alternatives. KCAE.DELIVER carries the selected whole to its recipient. KCAE.MEMORY retains conditional links; KCAE.CHANGE reopens dependent links. C.39 supplies the general construction and repair of connected contributions. E.11.PUR governs coordination when the contributions are FPF patterns; CMP.4 supports computational search where its exclusions can be justified.

### KCAE.COMPOSE:End

## KCAE.DELIVER - Put Sufficient Source Material within the Reader's Reach

> **Type:** Method pattern
> **Status:** Stable

### KCAE.DELIVER:1 - Problem frame

**Use this when** a found contribution must cross to another person, model call, tool or later occasion, and its source conditions may not survive that crossing. A brief search excerpt is enough to choose what to open; it may be insufficient to use the method safely or explain its result.

The gain is a receiving reader who has the material, context and access needed for the intended contribution. Do not build a packet when the reader already has and understands the sufficient source. Do not require exhaustive source delivery when a bounded result with recoverable grounds meets the receiving use.

### KCAE.DELIVER:2 - Problem

Source retention, a correct citation and a successful tool call do not establish that the recipient received enough. Truncation can remove a condition, a summary can remove a countercase, and a model can spend its remaining window on candidate listings before reaching the selected method.

### KCAE.DELIVER:3 - Forces

More source context can improve recoverability while increasing cost and distraction. Different readers have different preparation and tools. A compact result can be ideal for one recipient and misleading for another. Some runtimes support isolated readers or controlled history reconstruction; others only return another message into the same accumulating context.

### KCAE.DELIVER:4 - Solution

#### KCAE.DELIVER:4.1 - Specify the receiving contribution and reader

Identify what the recipient will do: choose a source, understand an explanation, perform a method, check a conclusion or maintain the access service. State the preparation already available and the operations the runtime actually supports. For a human, available time, domain competence and access permissions matter. For a model, include current instructions, model capability, tool access, residual window and output limits. Total historical tokens consumed and free space in the active context are different resources.

A search packet can contain a candidate's identity, edition, brief reason for relevance and source address. An application packet usually needs the method's recognition conditions, required inputs, consequential exceptions, operating instructions, stop conditions and any joining operation not already known to the reader. This is a sufficiency question, not a fixed field count. Derive the necessary material from the requested use and inspected source, not a universal 600-token allowance.

#### KCAE.DELIVER:4.2 - Recover the required reading closure

Start with the selected passage and follow dependencies needed to interpret or apply it: definitions, qualifications, tables, footnotes, named prerequisites and relevant adjacent exceptions. Expand across documents when a release note or external criterion changes the meaning. Stop expansion when the intended reader can obtain the receiving result without guessing an essential relation; unrelated background need not travel.

Keep original passages distinguishable from the engineer's explanation. A generated contextual prefix is discovery support, not a quote from the author. A translated passage is a translation with a stated role, not automatically the governing edition. If a missing source dependency prevents adequate delivery, return that specific limitation. Do not manufacture a complete-looking method from fragments.

For difficult or consequential use, test a question that depends on the vulnerable distinction. Can the recipient explain why protocol v1 selects manual reconciliation while v2 may permit a resend? Recognition of a document title would not test that contribution. KCAE.EVAL supplies a bounded reader-use comparison when the design depends on this capability.

#### KCAE.DELIVER:4.3 - Read complete bounded units through a pinned sequence

When source reading is paginated, the reader needs an edition or snapshot identifier, a bounded unit, a continuation token or explicit next position, and a completion indication. Pin the edition for the sequence. Record which portions were actually returned, and detect a gap, duplicate or changed generation before combining them. A source hash can confirm the obtained bytes; it cannot prove that a truncated tool message conveyed those bytes to the reader.

Use the actual output limits. Request a smaller portion when a response is truncated, verify the continuation boundary, and continue until the needed unit is complete. Do not take “command succeeded” as an end-of-document signal. A tool may store a complete file while showing only its beginning. Its reader interface must distinguish the saved result from the shown portion.

A method can span more than one call, provided the recipient can retain or revisit the dependencies it needs. Very long sources may require an external notebook of source-addressed intermediate results and selective rereading. That notebook is itself a lossy representation. Preserve the exact return path and reread the relevant original when its omitted distinction becomes live.

#### KCAE.DELIVER:4.4 - Choose a delivery arrangement the runtime can perform

**Direct complete reading** is suitable for a manageable dossier and a capable recipient. **Retrieval followed by selective reading** spends context on material selected for the current use. **An isolated reader** can inspect a larger or private portion and return a bounded result, provided the platform actually creates an independent context and the result retains enough grounds for its consumer. **Controlled history reconstruction** can retain current instructions and selected state while removing obsolete search output, but only when the runtime exposes that operation.

An instruction such as “forget the preceding search” does not establish deletion or reclaim a context window. A skill or tool that returns a concise message does not establish an isolated reader. Verify these runtime properties through documentation and a relevant observable test. Where isolation is unavailable, keep search material outside the main dialogue as far as the interface allows, use smaller returns and plan the necessary reading before filling the window. Where a fresh context is used, explicitly supply its governing instructions, source permissions, question and necessary prior results; independence is not inherited knowledge.

Separate conversation contexts can still share a filesystem, credentials, tools or network access. Check those actual boundaries before assigning a private dossier to another reader. Context separation alone is neither a permission grant nor a security sandbox. Supply only the authorized material and capabilities needed for the bounded contribution.

A cached long-context source can be a credible alternative when the platform supports it and the workload amortizes cost. Cache storage does not guarantee reliable attention to every needed item. Compare its actual delivery performance and current charging semantics with selective reading. A cache holding an old edition remains an old edition.

#### KCAE.DELIVER:4.5 - Budget discovery, application and explanation together

Reserve room and time for the selected source, necessary connections, answer and uncertainty before spending the entire allowance on candidate discovery. Include the cost of parallel calls and external readers in total work, even if they save main-context space. A cheaper main dialogue can conceal a much more expensive service.

Use a runtime observation of remaining capacity where available. When it is unavailable, label the estimate and leave a margin for interface overhead and output. Cumulative billed tokens across calls do not reveal the active window's remaining space; cached, repeated and external-reader input can be counted differently. Do not present an inferred residual as a measured runtime fact.

For example, if the active window has room for 12,000 further tokens, and source closure plus explanation is estimated at 7,000, a 9,000-token candidate dump is infeasible even if the model has consumed only a small fraction of its account quota. Either shrink discovery output, use a genuine external reader, obtain more capacity or return a narrower justified result. These invented numbers illustrate reservation, not a recommended product limit.

Check data boundaries on every transfer. Public retrieval can use a sanitized question; local case facts can remain with a local assessor. A remote provider's retention and logging behavior is part of the chosen interface, not implied by calling the input “context.” Redact with attention to meaning: if removing the decisive condition makes assessment impossible, obtain an approved local route or a permission decision rather than guessing.

#### KCAE.DELIVER:4.6 - Confirm receipt and expose what remains to be done

Return the contribution at the level the recipient needs: conclusion, grounds, conditions and next operation. For execution, distinguish a recommended action from an action already performed. For later use, include sufficient edition and dependency information to detect staleness. For human adoption, a readable explanation or small first useful exercise can reduce the burden; dumping every engineering detail may make correct material practically unusable.

Confirm actual receipt where the use requires it. Delivery to an API, display in a user interface and human comprehension are different observations. Unknown receipt remains unknown. If the recipient cannot recover a needed distinction, repair the representation, reader preparation or access support indicated by the failure, rather than adding unrelated text.

### KCAE.DELIVER:5 - Archetypal Grounding

A search excerpt says that CedarBench supports automatic resend. The needed manual unit also contains a protocol condition and links to a compatibility-table footnote. The assistant opens the pinned manual section and table, obtains the missing protocol from the authorized local configuration service, and gives the analyst a conditional result. For v1 it explains the manual reconciliation route and the absent automated prerequisite. The excerpt alone would have supported a wrong instruction.

Now change the reader. A service engineer building the integration additionally needs the receipt-ID mapping and the access-generation contract. A customer who only needs to decide whether to schedule manual reconciliation does not need the vector-index construction. The source basis is shared; delivery differs with the contribution.

### KCAE.DELIVER:6 - Bias-Annotation

Authors and powerful models may fill missing connections from their own knowledge and mistake that for sufficient delivery. Test the declared reader, not an omniscient one. Conversely, excessive precaution can overload a simple use. Ask which omitted distinction can change the result before adding another source bundle.

### KCAE.DELIVER:7 - Conformance Checklist

Is the receiving use explicit? Does the material contain the consequential conditions and joins? Are source text and interpretation distinguishable? Has the necessary reading completed without a generation change or hidden truncation? Does the runtime really support the assumed isolation or history control? Are total cost, residual window and permissions treated separately? Is receipt or comprehension claimed only where observed?

### KCAE.DELIVER:8 - Common Anti-Patterns and How to Avoid Them

A citation without obtainable text does not supply the method. A summary of a summary can inherit the very omission that defeated retrieval; return to the source. A success flag is not a reading-completion marker. A request to forget is not a runtime operation. A fixed small packet cannot satisfy every reader and use; derive its content from the receiving contribution.

### KCAE.DELIVER:9 - Consequences

The arrangement can spend less main-context capacity without pretending that all reader work disappeared. Source closure and privacy checks add effort, but make the basis of the result inspectable. Some tasks properly return a delivery limitation or request for a prepared reader.

### KCAE.DELIVER:10 - Architectural Rationale

C.2.8 makes recoverable structure relative to a reader and support. This construction turns that distinction into source expansion, bounded reading, runtime choice and receipt checks. Discovery and application packets differ because they supply different operations, not because shorter text is inherently superior.

### KCAE.DELIVER:11 - SoTA-Echoing

Anthropic's context-engineering account motivates selective runtime access; Gemini's long-context documentation makes caching a serious alternative while retaining multi-item retrieval limitations. These capabilities are developed in KCAE.Profiles:3. The method adopts both as conditional means and requires actual runtime support for history or isolation claims. Requalify delivery when a model, tool-output cap, caching interface or reader population changes.

### KCAE.DELIVER:12 - Relations

KCAE.SOURCE supplies exact reading units and addresses; KCAE.ASSESS and KCAE.COMPOSE determine what the contribution requires; KCAE.CHANGE preserves edition coherence; KCAE.EVAL tests actual receiving use. C.2.8 supplies reader-relative recoverability and C.11.DUA supplies the burden question. Neither is replaced by a token count.

### KCAE.DELIVER:End

## KCAE.CHANGE - Keep Source Reading and Derived Views Coherent through Change

> **Type:** Method pattern
> **Status:** Stable

### KCAE.CHANGE:1 - Problem frame

**Use this when** sources, extraction, permissions, representations or cached judgements change while access continues or resumes after an interruption. A search hit and its opened passage can each be valid in isolation and form an invalid pair.

The gain is a truthful choice among coherent current access, identified historical access and a bounded degraded route. A frozen one-use dossier needs only a fixed source basis, not an elaborate generation service. More machinery becomes justified when concurrent readers, several stores or repeated refresh make that basis hard to preserve.

### KCAE.CHANGE:2 - Problem

Updating one index does not atomically update sources, vectors, summaries, permissions and stored recommendations. A content hash catches a changed block but can miss a changed parent heading or governing exception. A completed update job does not by itself prove that the searchable collection matches a fresh construction or that the result is still applicable now.

### KCAE.CHANGE:3 - Forces

Availability competes with coherent switching. Rebuilding everything can be wasteful; selective reuse can retain hidden stale dependencies. Immutable generations simplify reading but consume storage. Source currency, model compatibility and permission currency can change at different rates.

### KCAE.CHANGE:4 - Solution

#### KCAE.CHANGE:4.1 - Detect changes at the relevant dependency boundaries

Maintain a source inventory that can distinguish addition, deletion, content change, relocation, replacement and a change in role or authority. Identify editions and membership from the source system or a captured snapshot. A directory scan of a changing tree is not automatically a snapshot: obtain source locking, immutable revisions, a stable export, or detect concurrent mutation and retry the affected acquisition.

Establish how a change becomes observable: an authorized event feed, revision query, periodic polling, supplied export or explicit owner notification. Record the last successful observation and the coverage or freshness interval it supports. Detect a broken subscription, failed fetch or missed sequence where the source permits it. “No change event received” supports currency only under a functioning channel with the required coverage; after an unexplained gap, recover the current inventory or mark currentness unknown. A periodic full reconciliation can find missed additions and deletions that an event-only path would retain indefinitely.

Track the dependencies actually used to derive a result. A retrieval unit can depend on its bytes, enclosing heading, table structure, contextual prefix, linked definition, extraction version and model configuration. An assessment additionally depends on the case facts, criterion and source-role basis. A recommendation additionally depends on burden and the receiving opportunity. These are different invalidation sets.

For example, moving an unchanged clause from “general availability” to “obsolete compatibility” leaves its block hash unchanged and changes its practical interpretation. Recompute the context-sensitive representation and reopen dependent assessments. An unchanged embedding can sometimes be reused technically while the source address or applicability is updated; do not infer semantic validity from that reuse.

#### KCAE.CHANGE:4.2 - Construct a candidate generation without disturbing readers

For a repeated service, assign a generation identifier to a coherent source snapshot and the derived views prepared against it. A manifest identifies source membership, editions, extraction and representation configurations, and each view's ready, unavailable or limited status. It need not duplicate the complete data, but it must resolve exact reads and state what a route can search.

Build new or changed units, remove deleted membership, update structural links and recompute context-dependent units. Reuse an embedding only when the required source/context and embedding-space conditions still hold. A change of model, preprocessing, vector dimension or comparison convention can require a new compatible index. Mixed spaces do not become comparable because their numeric dimensions happen to match.

Persist the candidate and test a newly loaded instance, not only the in-memory builder. Exercise build, save, close, load, query and source read. This catches missing files, omitted metadata and incompatible serialization. Validate required view membership, exact return addresses and representative changed cases before making the generation selectable. A failed optional view can leave a useful generation with fewer routes; a failed necessary source reader prevents that use.

#### KCAE.CHANGE:4.3 - Publish and read one coherent generation

In a single store with a transaction that covers all relevant data, use that store's actual transaction and isolation semantics. In a composition of object storage, a lexical database and a vector service, a metadata manifest is not a transaction over those stores. Obtain a different publication construction.

One workable construction uses immutable generation-specific objects and namespaces. Build and durably store all objects needed for a declared route; validate their resolvability; then atomically change a small catalogue pointer to the new manifest using a store that actually supports that operation. Readers acquire the pointer once and pass its generation through search, open and pagination. They can see the complete old generation or the complete new one; they must not independently fetch “latest” at every step. This claim depends on immutable names, durable objects, an atomic pointer operation and preserved objects during a read. Test these assumptions in the chosen stores.

Use an expected previous pointer or equivalent compare-and-swap when concurrent publishers are possible. A publisher that loses the race must reconcile its source basis; blindly installing its older candidate can regress currency. Preserve old objects while readers still hold them, through bounded read leases, reference tracking or a declared retention interval with an explicit expiry response. Garbage collection must not silently break an in-flight read.

If those facilities are unavailable, a maintenance interval with unavailable service during installation is a legitimate simpler construction. State that availability tradeoff. Do not claim atomic continuous service merely because the individual store updates usually finish quickly.

#### KCAE.CHANGE:4.4 - Separate historical coherence from current authority

A pinned historical generation can be perfectly coherent and no longer govern today's action. Mark the requested use: historical explanation, current recommendation or comparison across editions. Before a consequential current recommendation is used, check the authority/currentness condition required by the use. If it changed, reopen the affected judgement against the new source. A user-visible old answer needs a stale or superseded disposition where continued reliance matters.

A failed vector update need not force stale advice. Use the new generation's exact or lexical route, a direct source scan, or a qualified unchanged subset whose dependency boundary is known. Advertise that route's scope. If no adequate current route remains, return an availability limitation. Keeping an old generation online is a service rollback; it does not make an old rule current again.

If users edit sources while the prepared view lags, either construct a new snapshot before serving those edits or expose a delta layer: exact current additions and changes plus tombstones for removed old material, with an explicit combined membership and conflict rule. The merge must remove obsolete hits and open the selected current edition. A silent mixture of edited files and an old index is not an incremental profile.

#### KCAE.CHANGE:4.5 - Handle deletion and permission change explicitly

Source deletion can mean removal from current membership, withdrawal of a claim, retention expiry or access revocation. Obtain that meaning from the source policy. Keep authorized historical material only when retention permits it. Purge or quarantine prohibited copies in indexes, caches, summaries, logs and memory according to that policy; removing one search row is not a complete deletion procedure.

Where a provider removes index entries eventually, enforce current membership and permission at result release and source opening as well as at query filtering. A stale candidate identifier must not expose withdrawn content. Overfetching and post-filtering can change recall and latency; measure that cost. Rechecking permission still leaves a time-of-check/time-of-use question. Use the source service's enforcement at the actual read or action when immediate revocation matters, and state any remaining race rather than claiming universal instantaneous revocation.

A permission cache has its own allowed age. Source-generation pinning must not freeze permission to an obsolete grant. If source content may be retained historically but a particular reader loses access, the generation remains a historical object while that reader's operation is denied.

#### KCAE.CHANGE:4.6 - Test update, recovery and dependent use

Construct changes that exercise the intended guarantees: add a decisive passage; alter a condition; move an unchanged block under a different heading; split a section; delete a source; change a permission; fail a vector build; interrupt before and after pointer publication; reopen from persisted state; and read across the switch. Select cases from the actual architecture rather than treating this list as exhaustive.

Compare incremental and fresh construction on a stable input. For deterministic representations, compare exact membership and expected values. For stochastic extraction or approximate retrieval, compare the intended semantic and retrieval properties with recorded variation; byte inequality is not automatically a defect, and job completion is not equivalence. Repeat questions whose answers depend on the change and unchanged controls that should retain their result.

Follow dependencies into cached assessments, composed relations, deliveries and episode memory. Invalidate, recompute or retain each at its actual basis. A failed source update and a changed model have different consequences. Preserve sound unaffected results, but do not let a valid low-level hash become an all-purpose reuse certificate.

### KCAE.CHANGE:5 - Archetypal Grounding

CedarBench revision 8 adds a destination-certification condition to automatic resend, relocates the procedure and removes an old workaround. The new source and lexical reader pass their checks; vector construction fails. Publish a generation whose current routes are exact and lexical, with vector search unavailable for the changed material. A revision-7 vector hit cannot authorize revision-8 operation. Pending resend advice is reopened because its condition dependency changed.

A historical analyst can still request revision 7 if retention and permission allow it. Its exact reader remains valid for that named inquiry. This is not a claim that the older procedure is approved today. If the source store forbids retained copies after withdrawal, even the historical request must return that access limit.

### KCAE.CHANGE:6 - Bias-Annotation

Successful happy-path refreshes can hide cross-store races. Test interruption and denied access as ordinary states. Desire to avoid rebuilding can make dependencies artificially narrow; inspect contextual changes outside the unchanged block. Conversely, invalidating everything can make maintenance unaffordable; retain results on a sufficiently specific surviving basis.

### KCAE.CHANGE:7 - Conformance Checklist

Is the source snapshot actually stable? Are contextual and configuration dependencies included? Can a freshly loaded instance read the prepared generation? What operation makes it selectable, and which store guarantees it? Does one reader remain on one generation? Can historical coherence be distinguished from current authority? Are deletion and permission enforced at the relevant operations? Have dependent judgements received dispositions?

### KCAE.CHANGE:8 - Common Anti-Patterns and How to Avoid Them

A manifest is not a distributed transaction. A hash of one block is not a hash of its meaning. A successful refresh is not proof of fresh-build equivalence. Rollback does not reinstate superseded authority. Deleting an index entry does not necessarily delete provider-held content or prevent eventual stale hits; enforce the actual data lifecycle.

### KCAE.CHANGE:9 - Consequences

The service can remain useful during partial refresh without hiding its limits. Generations and retained dependencies cost storage and engineering effort. Small installations can choose a frozen snapshot or a maintenance interval instead. Coherence and currency remain separate properties across every profile.

### KCAE.CHANGE:10 - Architectural Rationale

Immutable content plus a controlled selection operation reduces a many-store consistency problem to a smaller publication boundary, under explicit assumptions. Dependency-specific invalidation preserves affordable reuse. Separate permission enforcement prevents an otherwise useful historical snapshot from extending a revoked grant.

### KCAE.CHANGE:11 - SoTA-Echoing

CodeNib's versioned code-corpus construction and update experiments motivate separate checks for source/view identity, persistence and fresh-build comparison; its code results do not establish correctness for another corpus. SQLite documents guarantees within its own database. OpenAI's retrieval documentation distinguishes asynchronous ingestion and eventually consistent removal. KCAE.Profiles:3 uses those bounded capabilities without extending one store's guarantee across a composition. Reopen this construction when the source or provider changes its durability, deletion, namespace or transaction semantics.

### KCAE.CHANGE:12 - Relations

KCAE.SOURCE supplies source identity and context dependencies; KCAE.INDEX supplies view configurations; KCAE.DELIVER consumes pinned reading; KCAE.MEMORY consumes invalidation; KCAE.EVAL compares changed behavior. The receiving domain's authority policy determines what governs current action; this engineering method does not create it.

### KCAE.CHANGE:End

## KCAE.ENCOUNTER - Arrange a Useful Encounter with Knowledge during Work

> **Type:** Method pattern
> **Status:** Stable

### KCAE.ENCOUNTER:1 - Problem frame

**Use this when** useful knowledge is not being requested because the person doing the work has no occasion to notice the question. An on-time result can hide repeated compensating work. A perfectly usable search box does not cause someone who sees no problem to search.

The gain is an authorized, attainable occasion for inquiry and, when worthwhile, a useful suggestion. Do not install continuous observation merely because a library exists. An explicit request, a known sufficient method or an ordinary conversation may already provide the encounter. This pattern does not grant permission to inspect work or interrupt its participants.

### KCAE.ENCOUNTER:2 - Problem

An access package can contain excellent instructions and still never enter the work. Conversely, an always-on recommender can impose surveillance, disclosure and interruption without benefit. The engineer needs an actual path from an allowed observation to a useful receiving opportunity, including the branch that stays quiet.

### KCAE.ENCOUNTER:3 - Forces

Earlier noticing can prevent rework, while incomplete event context encourages false diagnosis. Frequent inexpensive screening can become expensive human interruption. Reliable delivery creates state and maintenance; a simple agreed question at handover may suffice. Broad observation increases coverage and data exposure together.

### KCAE.ENCOUNTER:4 - Solution

#### KCAE.ENCOUNTER:4.1 - Choose an occasion and obtain observation authority

Start from work whose receiving result can matter, not from the available telemetry. Possible occasions include a handover, a changed configuration, a failed test, an unusual manual correction or a scheduled review already attended by a responsible person. Also inspect successful work: repeated compensation can make an inadequate input appear satisfactory. A failure-only trigger cannot expose that class.

Name who authorizes the observation, which events and fields may be used, for what purpose, for how long, and which recipient can receive the result. Obtain the permission through the actual owner. If it is absent, propose an attainable manual occasion or ask for the needed authorization; do not infer consent from installing a skill. State the stop on permission withdrawal.

The occasion must exist in the runtime or practice. A document describing a background observer is not that observer. A callable MCP tool exposes operations when invoked; it does not by itself watch a work stream. A skill can teach a response; it cannot alone schedule its own invocation. Choose an existing human participant, event subscriber, timer, application hook or explicit invocation that actually supplies the opening.

#### KCAE.ENCOUNTER:4.2 - Project an event without erasing the unknown distinction

An event projection carries only the allowed context needed to open inquiry: receiving work, observed result or contrast, the relevant passage or value, source/time identity and available case facts. Preserve the original observation separately from a proposed interpretation. “Three duplicate rows were removed by a senior analyst after a successful export” is evidence of an episode; “workers are too slow” is a hypothesis.

Use deterministic validation for payload shape, identifiers, dates and permissions. Use semantic assessment for the relationship between the event and a possible question. If a projection omits the very compensation that raises the question, improve that projection or obtain the fuller authorized episode. Do not compensate with a more confident classifier on the same insufficient fields.

Minimize private data before any transfer and keep a source return under appropriate access. A public service may receive “repeated duplicate reconciliation after a successful export” while customer identifiers and row contents stay local. If an essential distinction cannot be shared, use a qualified local reader or return a limitation.

#### KCAE.ENCOUNTER:4.3 - Provide actual invocation, deduplication and receipt

For a software observer, identify the event subscription, its delivery semantics, a receiver and failure behavior. Validate the event's source and permitted scope before running retrieval. Use a stable event identity together with the intended operation/version when suppressing repeated processing. Choosing only a case ID can wrongly suppress a later changed condition; choosing the receipt timestamp can fail to recognize a retry of the same event.

Under at-least-once delivery, distinguish a claim to perform the inquiry from a completed result. In a store with suitable conditional writes, create one processing record for the logical event/operation key, with the relevant input identity, an in-progress state, an attempt/owner token and a bounded completion or lease deadline. A duplicate with the same key but a different relevant payload is an identity conflict to resolve, not a cached answer. The first worker's successful claim authorizes that attempt under the stated permission; it does not assert that the inquiry happened.

On a repeated invocation, read the state using the consistency needed by that store's conditional-update contract:

- **Completed, with a durably stored result:** return that result and its original source/case basis, if access and retention still permit it. Do not rerun the inquiry or create another outgoing notice just to answer the duplicate. Missing result data is an integrity/recovery problem, not a successful completed state. KCAE.ENCOUNTER:4.4 separately checks whether an old result can support reliance now.
- **In progress, with a valid claim:** return a pending disposition or arrange a bounded later retry according to the event interface. Do not start a competing inquiry merely because the caller has not received a result. Do not permanently acknowledge unfinished work unless a durable continuation or recovery mechanism has taken responsibility for it.
- **Abandoned or expired, without a completed result:** establish the permitted recovery. A runtime may confirm that the earlier invocation terminated; another environment may only show an expired lease. Conditionally replace the stale claim with a new attempt token so two recovery workers cannot both acquire it. Then resume from a valid checkpoint or rerun only the work whose repetition is safe under the known effect state. If recovery cannot exclude conflicting commits or harmful repeated effects, return a recoverable unresolved state and obtain reconciliation rather than silently treating the event as processed.

Provide the mechanism that revisits an unfinished claim: actual queue redelivery, a recovery scheduler, or a resumable workflow with its documented behavior. A stored deadline does not invoke any of them. Choose bounded retries and account for repeated computation and model charges. Retain completed keys/results for the intended duplicate window, or define how older deliveries are rejected or reconciled when retention expires. An expired cache entry must not silently turn an old consequential operation into a new one.

Lease expiry does not kill a worker. If an old worker can resume after another attempt takes over, guard completion with an atomic comparison of the current owner token and in-progress state; a stale owner must be unable to commit its result or outgoing intent. In this construction, keep the inquiry replayable and defer externally visible effects until that guarded commit. Any effect path outside the guarded store needs its own idempotency or fencing support. Merely checking a lease and later making an unguarded external call leaves a race. If the chosen runtime cannot exclude that race for the proposed action, confirm termination before taking over, or preserve the unresolved effect state for an authorized person.

Persist the accepted result and completed state together. If another service must receive a suggestion, a transactional outbox can also commit the outgoing intent in that same supported local transaction, guarded by the current attempt token. Give the outgoing logical operation a stable identity across attempts. A sender can retry that intent; the recipient must deduplicate or otherwise reconcile repeated effects at its own boundary. The local outbox does not make arbitrary remote effects exactly once.

If an earlier attempt may already have posted a note, sent a message or launched an action before recording completion, inspect the external effect using that stable identity where possible. Recover an observed result, retry through a receiver that enforces the required idempotency window, or perform an explicitly authorized compensating operation when appropriate. Where the effect is unknown and repetition could be harmful, do not automatically replay it. An explicit “inquiry/effect unresolved” return is safer and more truthful than either a fabricated result or indefinite silent suppression.

Separate “event received,” “inquiry performed,” “suggestion sent,” “suggestion displayed” and “person understood or used it.” An acknowledgement lost after display creates an unknown receipt state, not proof of non-delivery. Do not repeatedly interrupt the user merely to make an internal receipt counter definite. Obtain a receiver query or use the agreed duplicate policy. Deletion and permission withdrawal apply to stored event payloads as well as search data.

#### KCAE.ENCOUNTER:4.4 - Turn the occasion into inquiry before recommending a solution

Use the observed work to ask what the result should enable and what remains unexplained. Keep a cue even if no diagnosis is available. B.5.PI supplies this opening of inquiry; KCAE.SEARCH can then find a contribution to the developed question. A practical event need not first match a known pattern label.

Compare the candidate's contribution with the case and a nearby non-fit. “Duplicate reconciliation occurs” does not always imply a software defect: a declared manual control might already be the intended and affordable arrangement. If the current arrangement is adequate, the inquiry can end quietly. If case information is missing, decide whether asking for it is worth the recipient's effort. If a useful new explanation is already available, deliver that explanation instead of demanding that the person learn a framework.

Keep applicability, present recommendation and interruption separate. A method can fit in principle while its benefit is too small now, its necessary support is unavailable, or the timing is poor. Select a quiet link, a digest, an agreed pause, a prompt to the responsible participant or immediate interruption according to the allowed use and consequence. The access system does not invent a new emergency authority.

Before a delayed suggestion is released, check that it still concerns the same episode revision, relevant case facts, source basis and allowed receiving purpose. A ticket edited after inquiry can require reassessment; attaching the old recommendation to the new text would hide that change. Reuse unaffected findings, but reopen any changed premise that can alter the recommendation. If the opportunity has ended, keep a permitted historical result or discard the pending suggestion. Do not broaden an old observation permission to deliver advice for a new purpose.

#### KCAE.ENCOUNTER:4.5 - Test the complete encounter and adjust its burden

Use a real or safely constructed episode with the intended observer, projection, receiver and aids. Check whether the relevant distinction reaches the inquiry, whether the recipient encounters the cue, whether they can understand the offered contribution, and what they do next. Include a similar event where the system should remain quiet, an overlapping retry, a crash after claim creation but before result persistence, a duplicate after completion, an unavailable source and a permission withdrawal. Inspect the allowed continuation and any external effect in each case, including whether a stale worker can still commit. A simulated successful classifier call does not test this complete path.

Measure the work imposed by false suggestions and by obtaining missing facts. Preserve dismissed or unhelpful suggestions only to the extent justified by the retention policy and improvement use. If the same suggestion has become familiar, reduce or remove it. If the cue is understood but the action remains unavailable, obtain support or an appropriate learning method; repeated notices do not supply capability.

### KCAE.ENCOUNTER:5 - Archetypal Grounding

CedarBench already has an authorized weekly support handover. Its ordinary notes include compensating work after nominally successful exports. A designated engineer follows one entry to the receiving use and asks why a senior analyst removes duplicates. The original note and the customer's faster-worker proposal remain distinct. Retrieval exposes the protocol condition; the useful first encounter is a small configuration question at that handover.

For an installation without a permitted event feed, this human occasion is the complete initial profile. Adding a retrieval skill to the helpdesk does not change that fact. Later, an authorized ticket hook can automate projection and inquiry, but its subscription, privacy boundary, receiver and quiet behavior must be constructed and tested.

For a constructed software case, CedarBench receives event E42 and operation version Q3. A database supports conditional claims and an atomic commit of the inquiry result plus an outbox intent. The inquiry only reads permitted, identified inputs; it does not directly send notices or modify the customer's system. The dispatcher and recipient use E42/Q3 as the stable notice identity. These are stipulated capabilities to obtain from a real installation, not effects supplied by the record format.

| Arrival/failure case | Available state and next operation | Result and remaining boundary |
| --- | --- | --- |
| Worker A claims E42/Q3, then crashes before storing a result. | The record is in progress and has no result. A real recovery invocation confirms A's termination, conditionally acquires a new token, repeats the permitted read-only inquiry, then commits its result and one outgoing intent. | The inquiry is completed rather than silently abandoned. A late commit with A's old token is rejected. If A might already have performed an uncontrolled effect, recover its status first or return unresolved instead. |
| A repeated delivery arrives while A's claim is valid. | Return pending or defer according to the queue contract; do not acquire another live claim. The original invocation or the established recovery mechanism remains responsible. | No second inquiry is launched by this duplicate. A later expired claim follows the recovery case; pending is not reported as completion. |
| A repeated delivery arrives after result and completed state were committed. | Retrieve the stored result under the same event/input identity and current access rules. Reuse any existing outgoing intent. | No new inquiry or notice intent is created. A lost display acknowledgement still leaves receipt unknown; the result record does not prove display or use. |

Now remove one stipulated capability: the first worker sends a non-idempotent external notice before saving its result, and the receiver cannot reveal whether it displayed it. A crash then leaves possible delivery with no reliable receipt. Automatic replay is not licensed by the absent local result. Preserve that uncertainty and use the agreed reconciliation or human decision. Restoring automatic recovery requires moving publication behind the guarded outbox construction or obtaining a receiver operation whose repeated effect is controlled.

### KCAE.ENCOUNTER:6 - Bias-Annotation

Telemetry favours what is easy to count, such as failures, and can omit skilled compensation. Library maintainers may recommend their own methods too often. Compare continuing without a suggestion, sample successful work and retain a no-use outcome. Permission for one receiving purpose does not generalize to unrelated monitoring.

### KCAE.ENCOUNTER:7 - Conformance Checklist

Does an actual occasion supply the observation? Is its scope authorized? Can the projection preserve an unresolved cue without making the diagnosis for the user? Are invocation, retries and receipt supported by the chosen runtime? Can a retry distinguish a live claim, a recoverable abandoned attempt and a stored completed result without repeating an uncontrolled effect? Can the result remain quiet? Does the recipient have an attainable next step? Has the complete path been tried under a defeating condition?

### KCAE.ENCOUNTER:8 - Common Anti-Patterns and How to Avoid Them

A better help form does not answer why someone would open it. A skill is not a background observer. A high fit score does not justify an interruption. Successful message transmission does not establish comprehension. Treat each as a separate missing contribution and repair the particular gap.

### KCAE.ENCOUNTER:9 - Consequences

The corpus can contribute before a neatly formulated query exists. Observation, false matches, receipt handling and user attention add costs and privacy obligations. A manual or periodic occasion often gives a useful smaller arrangement. Removing an unhelpful observer can be the correct outcome.

### KCAE.ENCOUNTER:10 - Architectural Rationale

The event opens a question; it does not answer it. Separate observation, inquiry, assessment and interruption preserve the possibility that the initial interpretation is wrong or no recommendation is worthwhile. The real observer and receiver are architectural elements, not properties of the knowledge package.

### KCAE.ENCOUNTER:11 - SoTA-Echoing

A.15.11 and B.5.PI supply method noticeability and inquiry from ongoing work. Contemporary skill, tool and package interfaces can supply instructions and callable access, but their capabilities alone do not establish observation or human uptake. This pattern adds the access-engineering path, permission projection, retry/receipt behavior and quiet branch. Choose a manual occasion as a serious comparator; reopen automation when its available event, receiver or total burden changes.

### KCAE.ENCOUNTER:12 - Relations

A.15.11 governs the useful cue and attainable next operation; B.5.PI governs the inquiry opening. KCAE.SEARCH, KCAE.ASSESS and KCAE.DELIVER obtain and convey the contribution. KCAE.MEMORY can retain a permitted open cue. KCAE.EVAL compares actual benefit and interruption cost.

### KCAE.ENCOUNTER:End

## KCAE.MEMORY - Reuse Connections while Keeping Open Questions Revisable

> **Type:** Method pattern
> **Status:** Stable

### KCAE.MEMORY:1 - Problem frame

**Use this when** repeated inquiries recreate the same source-to-work connection, or an unresolved observation should remain available for a later source, question or change. Storing only “training issue” can erase the very episode that later reveals a configuration problem.

The gain is useful reuse without freezing the first interpretation. Do not retain every conversation indefinitely. A one-time inquiry can end with its ordinary result; memory needs a permitted future use and an affordable maintenance boundary.

### KCAE.MEMORY:2 - Problem

Saved conclusions are cheap to retrieve and expensive to trust when their conditions disappear. Taxonomies and generated features improve recognition but can exclude new situations. A later useful source cannot help an old open problem if memory preserved only an earlier rejected label.

### KCAE.MEMORY:3 - Forces

Rich episodes preserve future distinctions and consume storage, attention and privacy allowance. Compact connections save work and conceal assumptions. Retesting every memory on every source change is wasteful; narrow invalidation can miss an altered governing condition. Familiar positive examples make learned recognition questions look better than they are.

### KCAE.MEMORY:4 - Solution

#### KCAE.MEMORY:4.1 - Retain the smallest revisable episode

Preserve the original expression or observation that matters, the receiving use, allowed source return, current interpretation, rejected interpretations that could otherwise recur, unresolved questions and the grounds of any conclusion. Keep source text separate from the system's interpretation. An early cue may have no selected method, no confirmed anomaly and no confidence score. That is a legitimate unresolved result.

Obtain the retention purpose, scope, access and expiry from the owner. Avoid copying private source material when a protected reference suffices; test that the reference will remain obtainable by an authorized later reader. If the content must be erased, retaining an embedding or paraphrase may still retain the prohibited information. Apply the deletion meaning to every derived copy.

For CedarBench, retain “senior analyst removes duplicates after on-time exports,” the customer proposal, the missing protocol question and the reason a speed-only interpretation was insufficient. Do not reduce the record to “resend recommended.” It may be reopened after a protocol change, even if the original customer never used the word reconciliation.

#### KCAE.MEMORY:4.2 - Store conditional connections with their dependencies

A reusable connection says which contribution helped which kind of receiving result, under what source edition, case conditions, criterion and support. Retain the source address and relevant dependency slice. Store an assessment or recommendation as that result, not as a timeless fact about the source. An observed successful application additionally needs its actual conditions and outcome; a proposed sequence has no observed success merely because it was stored.

Key reuse on the conditions that can change the answer, not only a semantic similarity score. A prior answer can be used directly when its dependencies and receiving use still hold. Where only part survives, reuse that part and reassess the changed premise. Missing dependency information makes the old answer a candidate to inspect, not a qualified shortcut.

Repeated requests can justify a response cache, a source-to-question map or a reusable aid. Choose the smallest representation that serves the repetition. A source-based cached explanation and a trained retrieval model have different refresh and deletion costs. Do not train a broad model merely to avoid a small explicit dependency check.

#### KCAE.MEMORY:4.3 - Let new material find relevant old questions

Maintain a bounded collection of authorized open questions and conditional uses. When a source changes or a newly inspected method supplies a different contribution, query that collection by its possible receiving results and conditions. Reassess candidate episodes against their original cues; do not simply append the new method to every similarly tagged case.

This reverse lookup can be indexed lexically and semantically, with the same source-return and blind-spot limits as forward retrieval. Preserve a route to open episodes outside the existing category. A periodic sample or targeted direct inspection can reveal cases the category map hides. Selection for such inspection must have a declared scope and cost; it is not proof that every past episode has been reconsidered.

Publish a changed connection only after the relevant source and current case basis are inspected. The old configuration may no longer be observable, or the user's need may have ended. Return “potentially relevant, present situation unknown” rather than an unsolicited action based on an old conversation. Permission to remember is not automatically permission to interrupt; KCAE.ENCOUNTER governs the latter.

#### KCAE.MEMORY:4.4 - Improve recognition questions from consequential misses

Take actual misses and false matches whose remedy can change use. Compare them with matched cases and nearby non-fits. Ask what observable question would have distinguished them before the result was known. “Does success require repeated manual compensation?” may expose a broader family than “Did the export fail?” The wording and its observable inputs matter more than a new tag name.

Derive candidate questions from the episodes and subject knowledge, then test them on withheld or independently constructed cases, including negatives and unknowns. A generated question tested only on the examples that generated it supplies no independent recognition evidence. Reject a question that cannot be answered from the authorized event projection, or obtain the needed observation through an approved route.

Keep the question as a useful aid, not an exclusive admission gate for every future concern. Provide an open route for an unrecognized cue. If features become a learned classifier, preserve the training basis, model version, evaluation population and refresh conditions. KCAE.EVAL compares its gain with direct source-based inquiry and the prior recognition aid.

#### KCAE.MEMORY:4.5 - Expire, invalidate and learn without rewriting the past

Use dependency changes from KCAE.CHANGE to reopen stored connections. Distinguish changed source content, changed case facts, changed authority, changed model and an expired receiving opportunity. A newer rule can invalidate current advice without falsifying the earlier historical record. Correct a past factual error with its grounds; do not silently relabel the original observation to match the new interpretation.

Periodically inspect whether retained material is still permitted and useful. Remove obsolete prompts and expired copies. Preserve only the evidence needed for any legitimate historical or accountability use. Measure the effort saved by reuse against maintenance, false suggestions and exposure. Memory that produces more unhelpful work than it saves should be narrowed or removed.

### KCAE.MEMORY:5 - Archetypal Grounding

An old CedarBench episode was left open because its destination protocol was unknown. A later method for obtaining signed configuration reports can provide that missing fact. Reverse lookup proposes the old episode because of the missing result, not because both texts use “export.” The owner authorizes a new inquiry; the current report shows v2. The system reassesses against the now-governing manual before suggesting anything.

If the customer's project has ended, the source-method relation can remain useful engineering knowledge while the encounter ends quietly. If the stored episode's retention permission expired, it cannot be recovered for this purpose merely because the new method seems helpful.

### KCAE.MEMORY:6 - Bias-Annotation

Stored conclusions encourage confirmation and make past success look universal. Preserve the original cue and a discriminating non-fit. Feature discovery can overfit vivid failures; include common ordinary cases and unknown inputs. More memory is not automatically better memory, especially when permissions or source returns are fragile.

### KCAE.MEMORY:7 - Conformance Checklist

Is the future use and retention authorized? Can the original unresolved distinction be recovered? Are observations, interpretations and proposed actions separate? Does reuse check the premises that made the connection valid? Can a new contribution reach old questions outside the initial category? Were improved recognition questions tested away from their derivation examples? Are expiry and deletion applied to derived copies?

### KCAE.MEMORY:8 - Common Anti-Patterns and How to Avoid Them

A saved label is not a preserved episode. A cached judgement is not an enduring permission or truth. A useful new method is not permission to rescan every private conversation. A feature set that only recognizes known failures needs an open cue route and independent tests.

### KCAE.MEMORY:9 - Consequences

The system can learn useful connections and return to unresolved work with less repetition. It also acquires maintenance and privacy obligations. A bounded memory can deliberately forget; lossless retention of every future distinction is neither claimed nor normally attainable.

### KCAE.MEMORY:10 - Architectural Rationale

The episode is retained because the next useful question may differ from today's interpretation. The conditional connection is retained because repeated reasoning is costly. Keeping both, with separate permissions and dependencies, allows reuse without making the interpretation the only route back to the work.

### KCAE.MEMORY:11 - SoTA-Echoing

Bates's evolving inquiry and B.5.PI's retained early cue motivate preserving unfinished distinctions. Retrieval and typed feature discovery can help index episodes or pose recognition questions, but neither establishes the adequacy of the resulting categories. This method develops the episode-to-question-to-source loop, selective revalidation and held-out recognition test. Compare an ordinary source-linked notebook as a smaller alternative; reopen the design when query diversity, retention terms or maintenance cost changes.

### KCAE.MEMORY:12 - Relations

KCAE.ENCOUNTER determines whether a remembered question should reach someone now. KCAE.SOURCE and KCAE.CHANGE preserve its source basis. KCAE.ASSESS and KCAE.COMPOSE supply the conditional contributions. KCAE.EVAL tests reuse and recognition without confusing remembered agreement with new evidence.

### KCAE.MEMORY:End

## KCAE.EVAL - Compare Access Arrangements by Useful Results and Full Cost

> **Type:** Method pattern
> **Status:** Stable

### KCAE.EVAL:1 - Problem frame

**Use this when** adopting, replacing or repairing an access arrangement requires evidence of its practical gain, or a failure needs attribution to the operation that can be repaired. A benchmark score, successful API call or convincing demonstration cannot answer every such question.

The gain is a bounded decision to adopt, retain, change or stop an arrangement on the evidence that can support it. Do not run a large study for a harmless reversible lookup whose adequacy is already inspectable. Scale the comparison to the consequence and uncertainty of the receiving choice.

### KCAE.EVAL:2 - Problem

Retrieval can improve while the final answer remains wrong. A better assessor can appear worse because it receives poorer candidates. An inexpensive model can raise human review or refresh costs. A synthetic test set derived from the same summaries as the index can hide the exact distinctions the arrangement was meant to recover.

### KCAE.EVAL:3 - Forces

Real episodes have greater practical relevance and less convenient labels. Whole-use comparisons establish value but can hide the cause. Controlled component comparisons explain a difference but narrow its reach. Broad coverage, independent judging and repeated trials consume the same resources the system is meant to save.

### KCAE.EVAL:4 - Solution

#### KCAE.EVAL:4.1 - State the decision and serious alternatives

Recover the receiving use, population, corpus editions, permitted data flows and adoption consequence from KCAE.USE. Choose an incumbent that a capable practitioner would actually use. It may be manual reading, exact/lexical search, a current hybrid retriever, an established long-context workflow or a competent existing agent. A weak toy baseline makes an addition easy to justify and hard to trust.

State the proposed difference and the expected useful change. Compare complete feasible arrangements, including required extraction, source reading, assessment and delivery. Keep common components, instructions and sources equal when the question is one component's contribution; disclose changes when equality is impossible. A provider comparison confounded by different prompts or missing tools does not isolate the provider's effect.

Choose whether the decision requires better useful results at a fixed resource boundary, lower cost at a required quality, or a transparent tradeoff. Keep non-negotiable permission and safety constraints separate from preferences; cheap unauthorized processing is not a feasible alternative.

#### KCAE.EVAL:4.2 - Build episodes that can defeat the design

Use actual receiving episodes where access is permitted, or independently construct realistic cases from work conditions. Retain the original request, relevant source basis, available case facts and expected kind of useful result. Separate cases used to design queries, tune thresholds or write features from cases used to assess them. Prevent near-duplicate leakage across that boundary.

Include cases with unknown source names, cross-language wording, useful non-pattern prose, distant prerequisites, misleading vocabulary, an important exception, missing facts and no useful corpus contribution. Include naturally answerless cases from the receiving work, not only deliberately irrelevant collections. Add source changes, stale indexes, revoked access and partial availability when the intended installation must handle them. Select proportions from the expected workload or report separate strata; a hand-balanced set is not automatically representative.

Gold material may be incomplete. Pool candidates from several serious routes and obtain source-based judgements from appropriate readers; sample beyond the pool where practical. Record uncertainty about unjudged material. Do not label every unpooled passage irrelevant. When several answers can serve the work, judge sufficiency and conditions rather than exact string agreement with one preferred answer.

Synthetic questions generated from an index can be useful development probes. Keep that origin visible and do not use them as the only evidence that the same index finds unfamiliar distinctions. For an English-primary assessor serving another language, test that language and important negation/condition forms rather than assuming a good English average transfers.

For a broad synthesis, vary the underlying evidence independently of its presentation. Duplicating an old edition or adding an overlapping summary must not create another population member or inflate a count. A new current counterexample or changed qualifying note must be able to alter the claim it defeats. Inspect whether a rare consequential position survives the map, reduction and delivery, and whether unknown membership remains unknown. Compare the final claims with original-source coding on a manageable dossier; merely counting processed summaries cannot test this contribution. KCAE.SEARCH:5.2 provides a constructed example, not an empirical success rate.

#### KCAE.EVAL:4.3 - Observe the complete useful result and full cost

Have the intended recipient or a qualified judge assess what the arrangement actually enabled: a correct explanation, an applicable conditional proposal, a necessary missing-fact question, a justified no-use result or a completed application. Also inspect unsupported advice, omitted exceptions, false absence claims and unusable deliveries. Source relevance, recommendation worth and actual work benefit remain distinct outcomes.

Measure cost over the selected horizon: preparation, extraction repair, indexing, storage, refresh, all model/tool calls, latency distribution, main-context consumption, human reading, interruptions, follow-up questions, application and recovery. Report total model input separately from residual main-window capacity. Report medians together with tails or failures where those change adoption. Use actual observations for empirical claims; estimates remain estimates with their assumptions.

For paired episodes, compare alternatives on the same case where this does not contaminate the reader. Randomize order or use separate recipients when the first exposure teaches the answer. Keep the judge's criteria independent of the preferred implementation. If a model judges outputs, test its agreement and failure cases against source-grounded human or otherwise competent judgement; do not assume self-evaluation is neutral.

Return distributions or uncertainty appropriate to the data and decision. A handful of designed examples can establish that a mechanism runs and expose failures; it does not estimate a population success rate reliably. A small useful trial can justify a reversible next trial without pretending to prove general superiority.

#### KCAE.EVAL:4.4 - Isolate the failed contribution before repairing

Use controlled substitutions after the whole comparison identifies a consequential question:

- Supply adequate source candidates manually to the same assessor and delivery path. If the result recovers, finding was a limiting factor; if not, downstream work remains.
- Hold the candidate pool and source context fixed while comparing assessors. This separates candidate availability from ranking and condition judgement.
- Hold a qualified contribution fixed while varying delivery. A failed recipient can then expose omitted context, excessive compression, unavailable tools or missing preparation.
- Hold the source snapshot and queries fixed while varying representation or route. Inspect not only aggregate retrieval scores but unique useful discoveries and unique harmful omissions.
- Replay a controlled source change through build, persistence, reload and use. Compare the affected result with unchanged controls.
- Hold inquiry content fixed while changing the encounter occasion. Observe interruption and uptake, not merely whether a notification was sent.

These substitutions diagnose an operation under controlled inputs. They do not prove that the repaired whole will produce those inputs naturally. Re-run the relevant complete use after repair. Components can interact: a larger pool can improve recall and overwhelm an assessor, while a more selective delivery can save context and remove a decisive exception. Do not add separate component gains as if they were independent benefits.

For encounter recovery, interrupt the actual implementation after claiming work, during execution and after committing the result. Present a concurrent duplicate and a later completed duplicate. Observe whether unfinished work has an actual continuation, whether a stale owner can publish, and whether an external effect can be repeated or remains unknown. A constructed state trace can expose a missing branch; it does not establish a real database's atomicity, scheduler behavior or recipient idempotency. Keep those implementation questions separate from a classifier's inquiry quality.

#### KCAE.EVAL:4.5 - Qualify scores for the decision they control

For retrieval, recall over known relevant units, rank-sensitive measures and coverage can help diagnose finding. Their meaning depends on the judgement set. For screening, inspect false positives, false negatives, abstentions and unknown inputs at the proposed threshold. For claimed probabilities, test calibration on the relevant population and scoring event. For typed group choice, retain its within-group meaning; test logical relations among questions separately when the application depends on them.

Choose thresholds on development data using the costs of missed and incorrect actions. Freeze them for the held-out comparison, or account explicitly for adaptive tuning. Include near-boundary cases and no-use outcomes. A threshold that filters deliberately wrong repositories may fail on naturally difficult questions in the right repository. A calibrated score cannot create missing source evidence or domain permission.

Test the identity preserved across ranking, screening and return. Include a case where the ranking winner fails the adequacy threshold while another shortlisted candidate passes. The output must qualify its own candidate, choose a separately qualified alternative, or abstain; the maximum over the pool is not the returned candidate's adequacy. Also test a high-scoring candidate with a contradicted necessary source condition. These cases distinguish a working score interface from a correctly connected decision.

Use executable calculation for counts, ratios, confidence intervals or cost arithmetic where needed. Preserve denominators and the treatment of unknowns. Report “not assessed” separately from failure and success. If a metric cannot distinguish the practical failure that motivated the change, add an appropriate receiving-result observation rather than decorating the same metric.

#### KCAE.EVAL:4.6 - Make the adoption and refresh decision

Relate observed gains and losses to the original use. Keep the incumbent when the addition does not earn its build and maintenance burden. Adopt a narrower profile when it helps one stratum but not another. Change the source preparation, route, assessor, delivery, observer or memory indicated by the evidence. A source gap may require obtaining a source rather than improving retrieval.

Name what the evidence supports, what it leaves untested and which condition reopens the decision. A changed corpus, model, language population, authority rule, workload or privacy constraint can defeat the original comparison. Preserve an operational fallback and observation during a bounded rollout if that is the selected use. A favorable laboratory result alone is not deployment or human benefit.

### KCAE.EVAL:5 - Archetypal Grounding

Suppose CedarBench compares an existing hybrid search workflow with a proposed direct-block supplement on 40 withheld support episodes. These are invented study conditions, not reported measurements. Cases include protocol ambiguity, old translations, useful table notes and naturally unsupported requests. Both alternatives use the same source snapshot, assessor, delivery and recipient rules. The proposed route adds its actual call and maintenance costs.

If a missed exception appears after manually supplying its source, the original finding route was a limitation. If the assessor still recommends resend on protocol v1, retrieval repair alone cannot close the case. If the judgement is correct but the customer receives only the upbeat first sentence, delivery remains defective. The adoption question returns only after the relevant whole is tried again.

### KCAE.EVAL:6 - Bias-Annotation

Authors tend to select examples their design can answer and count improvement where it is easiest to measure. Start from the receiving work and include natural failures and no-use cases. Avoid tuning on the final test, treating model agreement as independent truth, or omitting preparation and interruption costs. A smaller honest conclusion is more reusable than an inflated score.

### KCAE.EVAL:7 - Conformance Checklist

Does the comparison answer a real adoption or repair decision? Is the baseline serious? Are sources, episodes, recipients and costs comparable? Could the cases expose an unknown or absent answer? Are development and evaluation separated? Can the result distinguish finding, assessment, delivery and application? Have component repairs returned to whole use? Are evidence reach and refresh conditions explicit?

### KCAE.EVAL:8 - Common Anti-Patterns and How to Avoid Them

A green API test establishes interface behavior, not useful advice. A stronger retriever with a weaker prompt is not a clean model comparison. An oracle candidate trial is a diagnosis, not end-to-end performance. A gold-free case is not necessarily a true no-answer case; inspect its source basis. A cheap query does not make an expensive maintained service cheap.

### KCAE.EVAL:9 - Consequences

Engineering choices become revisable on evidence relevant to the receiving work. Some promising additions will be rejected or narrowed. Evaluation itself costs work, so reuse current matching results and inspect only changes that can alter the decision. Neither exhaustive metrics nor a universal test-set size is required.

### KCAE.EVAL:10 - Architectural Rationale

Whole-use comparison determines whether the arrangement is worth having. Controlled component substitutions determine where to intervene. Separating those questions avoids both an unexplained aggregate score and a pile of excellent components that fail together.

### KCAE.EVAL:11 - SoTA-Echoing

AgentRetrievalBench contributes a concrete warning about natural no-gold retrieval and limited evidence from artificial controls. Typed-decision audits expose confounding and coherence questions beyond a neat output schema. KCAE.Reference:9 preserves their scope; neither establishes support-library efficacy. Classical information-retrieval evaluation remains useful for component diagnosis. This pattern adds receiving use, source change, reader sufficiency, encounter and full lifecycle cost to the adoption question. Reopen metrics when they cease to distinguish the failure that matters.

### KCAE.EVAL:12 - Relations

KCAE.USE supplies the decision and workload. Every other KCAE method supplies an operation that can be examined without making its local success the whole result. C.11.DUA supplies advice and evidence burden; A.3.1.FT supplies qualified method-transfer questions when transfer is claimed. A publication's own quality and admission remain governed by its authoring and evaluation methods, separate from an installation's runtime comparison.

### KCAE.EVAL:End

# Applications

## KCAE.Application:1 - Constructing access for CedarBench support

### KCAE.Application:1.1 - The receiving work and source authority

CedarBench is a fictional data-export service. Its support collection contains 18,000 documents: manuals, localized copies, release notes, worked examples and private incident records. Public documentation changes several times a week; support receives repeated English and Spanish questions that rarely name the governing paragraph. These are constructed design conditions, not measured characteristics of an existing installation.

The intended result is a source-grounded explanation or conditional support proposal. The service does not autonomously change customer configurations. The product owner supplies the authority rule: the current approved English manual governs operational advice; an approved release note can override its named clause; a translation aids understanding but cannot override a newer governing condition. A local configuration report supplies case facts. An incident note reports what happened and does not amend the manual. Private row data may not be sent to external models. Those stipulated rules are inputs to this case; another organization must obtain its own.

One support episode says: “Nightly reports finish on time, but our senior analyst removes duplicates every morning. Can we buy faster workers?” A Spanish query might instead ask, “Cada manana quitamos filas duplicadas; el envio termina a tiempo.” The practical distinction is successful completion plus repeated compensation, not the word speed. The original episode remains available while queries explore both throughput and receipt reconciliation.

### KCAE.Application:1.2 - The small source slice that decides this episode

The relevant constructed sources are:

| Source and address | Decision-bearing content | Role |
| --- | --- | --- |
| English manual rev. 7, `exports/resend` | Automated resend requires a stable batch identity, destination receipts and protocol v2 deduplication. Select missing export IDs by comparing intended IDs with accepted receipt IDs. | Governing procedure under the stipulated rule. |
| English manual rev. 7, `exports/manual-reconcile` | For protocol v1, compare the export ledger with the destination report and prepare a supervised reconciliation proposal; do not use the automated resend procedure. | Alternative when the automated condition fails. |
| Compatibility table rev. 7, row `v1` | Deduplication: no. Receipt count available; an identity-bearing report must be obtained separately. | Conditions and missing-input distinction. |
| Compatibility table rev. 7, row `v2`, footnote 2 | Deduplication: yes, within one stable batch identity; accepted-ID receipts are available. | Scope of the affirmative table cell. |
| Spanish localization rev. 5, `reenvio` | A general resend explanation that does not state the later protocol distinction. | Discovery and language aid, incomplete for today's advice. |
| Local configuration report, not initially obtained | Destination protocol, batch-identity setting and report endpoint. | Authorized case facts. |
| Capacity note rev. 3, `export-cache` | Each active export reserves 2 GB until completion; the shared cache is 5 GB. | Whole-schedule constraint. |

Prepare the table as addressable rows with column meaning and footnote links. A flat extraction “v1 v2 no yes” cannot support the decision. Check the extracted values against the original table and preserve the visual return. Mark the localization's edition and role so that a high lexical rank cannot make it governing.

The proposed exact reader accepts source identity, edition and unit address, and returns the requested unit with its context links and completion status. Its corpus enumerator can list original units independent of the topic index. A retrieval hit retains both the retrieval-unit address and the reading-unit address. Therefore the table footnote remains obtainable even when the initial hit is only its affirmative cell.

### KCAE.Application:1.3 - Building the repeated retrieval arrangement

Choose the persistent addition from the workload before forcing a lexical failure. Here, repeated multilingual unknown-source requests make a hybrid candidate worth testing. Build an exact/lexical view over original bodies and a multilingual dense view over context-preserving units. Keep exact technical identifiers intact. Include definitions, tables, examples, Prefaces and References where they carry useful content; do not make a pattern or article title the only searchable representation.

Both indexes return the same source-addressed candidate interface. The lexical route also retains rare exact-ID hits. The semantic route uses compatible query/document encoding and records its model and preprocessing basis. Structural expansion follows explicit links from the resend clause to compatibility and resource conditions. Derived contextual prefixes are marked separately from source wording. Permission filters remove private incident material from the public route before scoring or disclosure.

Search variants include “duplicate rows after successful export,” “receipt reconciliation,” the original Spanish wording and an English reformulation. A hypothetical answer can suggest another query but supplies no evidence. Union candidates by exact source-unit identity, retain distinct governing editions, and use rank fusion or a qualified reranker. Inspect whether a route contributes unique useful candidates rather than counting several paraphrases of one passage as independent support.

For an unfamiliar question or a suspected shared blind spot, the same service can enumerate authorized original blocks for direct semantic screening. It batches them within actual model limits, retains all plausible candidates plus unresolved blocks, and opens their reading closures. A screened sample is reported as a sample. A complete enumerated pass establishes inspected coverage, not perfect semantic recognition. Cross-block relations can still require structural expansion or a later question.

### KCAE.Application:1.4 - Assessment changes the next operation

The first candidate pool contains the current resend section, old localization, compatibility table and faster-worker guidance. Read them against the receiving result. The faster-worker paragraph concerns completion delay, which this episode does not establish. It can remain a rival question if actual latency evidence appears, but it does not explain duplicate removal merely because the customer mentioned workers.

The table and procedure reveal a missing case fact. The first returned result is therefore: “The automatic route depends on the destination protocol and stable batch identity. Obtain the authorized configuration report; do not infer those values from the successful export.” This result is useful because it specifies which fact changes the action and how it can be obtained.

Two continuations make the distinction inspectable:

| Configuration result | Assessment | Useful next result |
| --- | --- | --- |
| Protocol v1 | The automatic resend condition is contradicted. A receipt count alone cannot identify missing exports. | Obtain the identity-bearing report and prepare supervised reconciliation under the alternative method. |
| Protocol v2, stable batch identity, accepted-ID receipts available | The named automated prerequisites are supported under rev. 7. | Construct the receipt comparison, verify remaining conditions and propose the bounded resend arrangement. |
| Protocol not obtainable | The decisive basis remains missing. | Give the dependency and access limitation; retain the manual or authorized inquiry alternatives without asserting automated applicability. |

A typed assessor can cheaply screen source-condition questions. The source-reading and case-fact operations remain explicit. A high group-choice probability for the resend section does not decide any of these three branches.

### KCAE.Application:1.5 - Constructing and delivering the whole

For the v2 branch, suppose intended export IDs are `{A, B, C}` and accepted receipt IDs are `{A, C}` for the same batch. A deterministic set difference returns `{B}`. Confirm that both sets use the same identity semantics and that receipts describe acceptance, not merely transmission. The proposed resend method consumes `{B}`, the batch identity and the applicable configuration conditions. Its output is a proposed operation, not evidence that the destination has accepted B.

If three independent exports are scheduled, their peak reservation is 6 GB and exceeds the 5 GB cache. Two concurrent exports followed by the third fit the capacity only if completed reservations are released. With ten-minute jobs and a twenty-five-minute window, the twenty-minute schedule fits the stated timing; with a fifteen-minute window, it does not. The latter requires another feasible arrangement or a changed accepted requirement. These arithmetic results follow from the invented inputs and do not predict real throughput.

The support analyst receives the selected branch, its source conditions, the exact missing or selected IDs, and the scheduling condition needed for the proposal. The integration engineer additionally receives the reader/index/generation interfaces. A customer sees a short explanation and attainable next step, with source return available. The same indiscriminate dump would not serve all three readers.

Deliver the selected manual section, table context and footnote through one pinned edition sequence. Detect truncated tool output and continue the required reading. The main agent does not pretend that asking itself to forget candidate listings reclaims context. If the selected runtime offers an isolated source reader, its bounded result and grounds can be used; otherwise the main reading budget must carry the needed material.

### KCAE.Application:1.6 - A changed source and a failed view

Revision 8 moves the resend section, adds a required destination-certification check, removes an obsolete workaround and retains the table's wording under a changed heading. The acquisition process captures the new snapshot. Context-sensitive units are rederived even where their own bytes are unchanged. Exact and lexical views load and pass changed-case checks; the vector build fails.

The service publishes a manifest with current exact/lexical routes and an explicit vector limitation. A reader pins that generation through search and open. It can obtain the new rule without waiting for every optional view. Pending rev.-7 advice is reopened because certification is a new premise. Old-vector hits cannot silently fall through to an unrelated current paragraph or authorize current action.

If the configuration report shows that certification is absent, the prior v2 proposal no longer qualifies for unattended use. The system returns the supported alternative or the missing certification step under the owner's rule. Fixing the vector service does not itself obtain certification. This separates retrieval availability, source applicability and case readiness.

### KCAE.Application:1.7 - Encounter, memory and evidence

An existing authorized handover can expose the compensating-work episode without a new background observer. A later ticket-hook implementation needs its own subscription, projection, retry and receipt behavior. It must remain quiet for an event whose current manual arrangement is adequate or whose benefit does not justify interruption. Remember the original cue, missing protocol/certification questions and conditional source connections within permitted retention, so that a later source or case change can reopen them.

Before selecting this architecture for actual operation, compare it with the capable incumbent on independently obtained support episodes. Use the complete useful response and maintenance cost. Oracle candidates can isolate a finding failure; fixed candidates can isolate assessment; fixed qualified contributions can isolate delivery. Try changed sources, persisted reload and permission withdrawal. The construction above supplies testable behavior and arithmetic, not a claim that CedarBench has been deployed or outperforms another arrangement.

## KCAE.Application:2 - A historical inquiry with no external processing

A compliance analyst asks which instruction was available to a support team during a past incident. Only three named documents matter: the English manual then published, the Spanish localization then distributed and a dated handover note. The processing permission is local-only. The receiving result is an explanation of the contemporaneous information basis, not today's operational advice.

Select those exact editions and inspect them directly. A persistent semantic index has no demonstrated advantage for this bounded dossier. The old localization now has a different role: its omission can explain what a reader could obtain at that time even though it cannot govern today's procedure. Compare the actual words and their dates without silently applying current rules retroactively.

Publication does not establish distribution; distribution does not establish reading; reading does not establish comprehension. Suppose the distribution record is absent. Return the observed text and publication basis, and preserve uncertainty about which document reached the team. Do not turn a coherent archive into proof of an operator's knowledge or cause of the incident. An authorized additional record or interview may improve that explanation, if attainable and worth its burden.

The exact reader still preserves edition and table context, and the analyst still distinguishes source claims from case facts. The search, remote-assessor and automatic-encounter machinery are not needed. If a new incident document appears, reconsider the source cut and explanation; it need not trigger construction of every KCAE component.

## KCAE.Application:3 - Finding and using contributions from a method library

### KCAE.Application:3.1 - The source is larger than a pattern index

A method library contains pattern bodies, Prefaces, explanations, examples, reference material and relations. An index is an entry aid. A request about an unrecognized difficulty may match an example or a distinction that no title names. Prepare original-body retrieval and exact reading for those units, preserving their position and source edition. Cards and skill descriptions can supplement that access; they do not exhaust the library's knowledge.

For FPF, the current applicable USING-FPF instruction supplies the ordinary finding/reading entry. F.1 supplies question-relative source selection. E.11.PUR supplies applicability, recommendation and coordination, and E.11.PUA supplies ordinary pattern use and a first useful result. These contributions retain their public owners and can be used without implementing this DPF. KCAE explains the engineering arrangement that makes larger-scale or repeated access obtainable.

### KCAE.Application:3.2 - A success that hides missing knowledge

Consider a constructed team that reports every handover on time because one experienced engineer silently translates ambiguous equipment names. Someone asks for better deadline reminders. Preserve that proposal and the underlying episode separately. Searching only deadline labels can miss the missing identity correspondence. Searching for receiving use, repeated manual compensation and notation translation can obtain an explanatory example in B.5.PI and a method in NOT.5.

Read B.5.PI's operative inquiry, not merely its example. The first contribution is to compare the successful handover with what the recipient can actually identify. If the notation mapping is then live, NOT.5 supplies the translation and lost-distinction question. Obtain the actual authoritative naming source and location context. Ten labels may map uniquely while two require building identity. The result can be a repaired correspondence and two explicit unresolved inputs, not a universal replacement of every abbreviation.

The episode does not prove a general need for more training. A direct correction, an available mapping, a maintained aid and a suitable learning method are different continuations. Compare them at the actual receiving use and burden. If the recipient already understands both notations and the retyping is cosmetic, the claimed identity problem disappears.

### KCAE.Application:3.3 - Preserve fit, recommendation and actual result

Finding NOT.5 yields a candidate. E.11.PUR asks whether its problem frame, forces, conditions, boundary and result fit this use. Missing source context yields insufficient basis; a contradicted condition yields non-fit. An applicable method need not be worth introducing now if a current result already resolves the concern. E.11.PUA then supports an actual bounded use and asks what result exists, not only which pattern was selected.

When several methods are co-used, establish the actual result-use connections and shared capacity. Reading order in a publication is not a mandatory work order, and co-use does not by itself identify one composite Method. A.3.1.DR, A.3.1.QM and C.32.MWA.PP supply recovery and qualification of method contributions and comparison of architecture alternatives. KCAE.COMPOSE supplies the access-side discovery of missing inputs and source-dependent relations, while leaving those general and method-engineering meanings intact.

An assessor trained only to distinguish tool actions from prose explanations would reject useful explanatory methods in this library. Replace that screening criterion with the required contribution to the work. Test queries whose answer lies in Prefaces or examples, natural no-use cases, partially known situations and combinations with a shared resource constraint.

### KCAE.Application:3.4 - Ecosystem and local installation boundaries

A library publisher can provide stable source addresses, edition-aware reading, useful search cues, source-returning representations and access profiles with declared limitations. Those facilities help several tools and readers consume the same content. A package, skill or service can realize that access under its own supported operations.

The publisher's choices do not supply an organization's event observer, permissions, local configuration facts or adoption evidence. Concrete commands, rollout order, current service incidents, deployment counts and operating backlog belong to the local practice running the installation. Changing them need not change the domain methods. A defect in the general meaning of source selection or pattern use returns to its direct Core owner; Core never acquires a normative dependence on this access-engineering DPF.

## KCAE.Application:End

# Engineering profiles

## KCAE.Profiles:1 - Retrieval and query construction

These profiles are replaceable implementations of the methods, not successive generations every installation must adopt. Select from the receiving workload and test the complete arrangement. A name such as RAG, agentic search or knowledge graph does not specify source authority, reading sufficiency or update semantics.

### KCAE.Profiles:1.1 - Exact, lexical and semantic units

**Exact and lexical retrieval.** Retain a resolver for named addresses and an inverted index for original terms. BM25 is a credible term-ranking choice: its weighting accounts for term occurrence, frequency and document length. Its tuning belongs to development data and the chosen retrieval unit. An exact technical identifier may deserve a separate lane because stemming or dense similarity can weaken its distinction. Lexical retrieval can work very well when the question and source share vocabulary; it can miss a useful paraphrase or another language. The algorithmic supplier is the historical [BM25 treatment in Introduction to Information Retrieval](https://nlp.stanford.edu/IR-book/html/htmledition/okapi-bm25-a-non-binary-model-1.html).

**Dense retrieval over original units.** Encode source units with a selected document encoder, encode the question compatibly, and retrieve nearby vectors under the model's similarity convention. Store source identity and context with each vector. An approximate nearest-neighbour index trades search work against agreement with exact vector neighbours; this agreement is not semantic recall. [HNSW](https://arxiv.org/abs/1603.09320) is an established historical algorithmic option, not a guarantee about the useful passages in a new corpus. Test multilingual queries, rare identifiers, conditions and negation. Keep a source route outside the embedding view.

**Late interaction.** The original [ColBERT](https://arxiv.org/abs/2004.12832) contribution represents a document and query with token-level embeddings and postpones fine-grained interaction until retrieval. It offers a richer matching alternative to a single vector per unit, with different storage and query costs. Its 2020 evaluation is historical evidence for that construction, not a current ranking of all retrieval models. Apply KCAE.SOURCE and KCAE.CHANGE to its larger representation just as to a simpler index.

### KCAE.Profiles:1.2 - Query variants and contextual representations

Question reformulation can expose aliases, translations and the result a method must provide. In [HyDE](https://aclanthology.org/2023.acl-long.99/), a generated hypothetical document supplies text to encode for retrieval. That 2023 mechanism can bridge vocabulary without making the generated document evidence. Keep the original question, reject invented case facts, and test whether expansion helps the receiving population rather than only increasing pool size.

[Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval) attaches generated document context to chunks before embedding and lexical indexing, then combines retrieval and reranking. Its 2024 account supplies a useful context-preservation construction and reported provider experiments. Here it is a historical comparator: the prefix can make an otherwise ambiguous chunk findable, but it is derived text and has context dependencies to refresh. It cannot replace the source reading or warrant transfer of the reported gains.

For fusion, [Cormack, Clarke and Buettcher's Reciprocal Rank Fusion](https://cormack.uwaterloo.ca/cormack/cormacksigir09-rrf.pdf) supplies the rank-based mechanism used in KCAE.INDEX:4.4. It avoids requiring comparable raw score magnitudes. The original constant and results belong to the original experiment. Choose pool depths and fusion behavior with the actual candidate population, and retain source-return and permission checks after fusion.

### KCAE.Profiles:1.3 - Structural and multiscale retrieval

Explicit section containment, definitions and references are useful low-cost structure. A generated graph or hierarchy adds inferred relations and its own loss. Use those relations to propose material, then inspect the source support appropriate to the question.

[GraphRAG §2.6](https://arxiv.org/html/2404.16130v1) selects a community level, shuffles its summaries into bounded contexts, produces intermediate answers, then combines them within a final context budget after helpfulness-based filtering. Its direct source-text map/reduce comparator is also a serious alternative. Prepared communities can amortize repeated broad questions, while preparation, updating and successive compression add burden and loss. The reported answer comparisons do not establish completeness of every summary or resulting answer.

[RAPTOR](https://arxiv.org/html/2401.18059v1) recursively clusters and summarizes material. Its query construction offers both traversal with pruning at successive levels and collapsed-tree retrieval across all levels. The latter can recover a useful node without requiring a successful top-down path, but a selected cross-level set is still not the whole source population. Preserve underlying membership when parent, child or overlapping summaries contribute to one answer. These 2024 sources supply implementable alternatives; KCAE.SEARCH:4.6 supplies the population and aggregation conditions for using their output in a bounded synthesis.

[LazyGraphRAG](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/) builds noun-phrase co-occurrence communities without advance LLM summaries. At query time it develops subqueries, explores communities through relevance testing, groups relevant source chunks, extracts claims and reduces selected claims to an answer. A relevance-test budget bounds exploration. This shifts preparation toward query-time work and is a serious comparator where advance summary cost is hard to amortize. Its selected claims and stopping condition still need an honest coverage account; deferred interpretation does not eliminate selection loss. The provider's bounded experiments do not transfer their quality/cost ratios to another corpus.

### KCAE.Profiles:1.4 - Direct semantic inspection and long-context reading

A direct original-block pass is useful when the question needs distinctions outside prepared selectors, or when the corpus is small enough that preparation would not pay. Enumerate blocks from the source inventory, supply the bounded state and criterion, retain plausible and unresolved blocks, and inspect their reading closures. The TypeSafe [semantic-find cookbook](https://docs.typesafe.ai/cookbooks/semantic_find) demonstrates addressed clause selection over a supplied document with a separate adequacy question. Its Jev 1.12 example is a bounded mechanism, not evidence of exhaustive semantic search in an arbitrarily large corpus.

Long-context reading can supply another direct profile, especially for a small stable dossier or repeated cached use. The [Gemini long-context documentation](https://ai.google.dev/gemini-api/docs/long-context) treats caching as a cost option and warns that multiple-item retrieval performance can vary. Compare actual model/version behavior and full lifecycle cost. A large accepted input window neither ensures every relevant relation is recovered nor makes a changed source cache current. KCAE.DELIVER remains necessary even when the whole dossier fits.

## KCAE.Profiles:2 - Typed assessors and generative readers

### KCAE.Profiles:2.1 - A bounded Jev role

The TypeSafe interface takes a state and typed questions. It can fill a screening or classification role when inputs, meanings and subsequent operations are controlled. It does not replace source acquisition, explanation, deterministic calculation or final domain judgement. [Model documentation](https://docs.typesafe.ai/models) describes English as the primary language and calls for testing other languages. Text-only inputs require an adequate prior transformation of a diagram or table. Treat version, limits, prices and availability as implementation inputs to verify at use, not durable properties of this framework.

The [Jev 1.13 jaggedness account](https://docs.typesafe.ai/model-jaggedness/jev-1.13) identifies sensitivities including negation, indirection, mathematical content, long irrelevant state and adversarial instructions. Give the assessor a focused state and explicit criterion, test the forms your cases use, and calculate exact arithmetic in code after semantic facts are obtained. A typed shape reduces parsing ambiguity; it is not an accuracy certificate. Keep retrieved instructions as untrusted source content, not a change to the assessor's authority.

Use a generative reader when the task needs an explanation, missing-condition recovery, query construction or a new connection that the fixed questions cannot express. Use an appropriate specialist when interpretation or authority depends on that profession. Combine roles only when the receiving result and total cost justify them.

### KCAE.Profiles:2.2 - What the cookbooks contribute, and what must change

The [skill-suggestion cookbook](https://docs.typesafe.ai/cookbooks/skill_suggestion) supplies progressive selection: short descriptions for a wide ranking, fuller descriptions plus instruction openings for the shortlisted Choice, and full descriptions for per-candidate fits. Its Jev 1.12 demonstration uses synthetic requests. The inspected code gates on the maximum fits score, then returns the Choice winner; these can refer to different candidates. This is a static example defect, not a measured failure rate or a general vendor claim. KCAE.ASSESS:4.4 binds adequacy to the returned candidate. Method-library use also replaces the example's action-oriented screen with the required contribution, including explanations, and reads complete necessary instructions before reliance.

The [feature-discovery cookbook](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery) proposes natural-language questions, obtains numeric features, uses supervised-model errors to revise them and assesses held-out data. It demonstrates this on a bounded tasting-note prediction problem. KCAE.MEMORY adapts the error-to-question loop for recognition aids, while requiring actual permitted episodes and a separate test population. The adaptation is a proposed domain construction, not evidence that the cookbook already solves open-ended method noticing.

### KCAE.Profiles:2.3 - Comparative evidence beyond the output type

The 2026 [early empirical audit of typed decision models](https://arxiv.org/html/2609.32160v1) warns that interface specialization and comparison conditions can be confused with intrinsic accuracy gains. [Typed decision coherence beyond calibration](https://arxiv.org/html/2609.33209v1) separates logical consistency among answers from probability calibration. These are bounded, early studies, useful as failure and comparison evidence rather than a final vendor ranking.

Accordingly, compare the actual typed and generative alternatives with matched evidence and required output. Test ranking, adequacy thresholds, calibration and any logical relationships separately. A model that selects the best available option can still need a distinct all-options-inadequate outcome. No scalar combines source authority, completeness, capability and permission into an automatic licence to act.

## KCAE.Profiles:3 - Packages, tools, dynamic loading and storage

### KCAE.Profiles:3.1 - Put the appropriate work at preparation and query time

A skill can carry a usable entry and the procedure for obtaining deeper sources. A tool service can expose search and edition-aware reading. A package can pin and distribute content and dependencies. A local reader can keep sensitive source material within a permitted environment. These contributions can be combined. Their exact contract must state identity, allowed data flow, completeness, freshness and failure behavior; the form's name supplies none of those guarantees.

[Anthropic's context-engineering account](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) describes lightweight identifiers and runtime source loading, including combinations of prepared retrieval and exploration. This is a current implementation comparator for the preparation/query split. It highlights why additional exploration has a cost. KCAE uses the mechanism where the runtime supplies it and tests the actual reader result instead of treating dynamic loading as inherently superior.

**VibeVM is a concrete package/runtime alternative.** Its [project README](https://github.com/vibevm/vibevm/blob/main/README.md) distinguishes resolved package identities, materialized content and computed agent boot material. The [boot-lane manual](https://github.com/vibevm/vibevm/blob/main/vibevm/vibepacks/org.vibevm.core/vibevm-docs/v1.0.0/vibevm/vibespecs/model/boot-lane.xml) describes a priority text plus an index of static or dynamic contributions, consumer-selected inclusion and conditional loading. It also directs citations back to authored sources rather than generated boot positions. That supplies a practical deferred-reading profile. Qualify the package/version and host behavior used; the documentation is not an observed deployment of this corpus. Dynamic inclusion is neither a guarantee that an unknown useful method will be noticed nor a substitute for complete source reading. It can coexist with semantic search, an exact reader and a separately authorized observer.

The engineering question is therefore not “packages or RAG?” A package can distribute an exact source and entry, a service can search it, an assessor can qualify candidates and a host can load the selected material. Another installation can use direct local files and no service. Compare the operations, source returns and costs of those actual arrangements.

### KCAE.Profiles:3.2 - Storage guarantees belong to their real scope

[SQLite's isolation documentation](https://www.sqlite.org/isolation.html) supports reasoning about committed database transactions and snapshots within its database. It does not transact a separate vector provider or object store. Use it for the atomic catalogue or local state only when the selected mode and operations provide the required behavior.

The [OpenAI retrieval documentation](https://developers.openai.com/api/docs/guides/retrieval) describes asynchronous file ingestion and eventually consistent removal. A service using that interface must wait for actual readiness and handle stale removal results. Do not infer complete deletion or cross-store consistency from a successful request submission. This is one provider-specific contract to place inside KCAE.CHANGE, not a universal ban on remote retrieval.

[CodeNib v2](https://arxiv.org/html/2607.25431v2), especially its boundaries and update experiments, distinguishes a useful multi-view code corpus from a transaction over a mutable workspace. Its incremental/fresh comparisons expose variation and incomplete equivalence despite completed updates. Adopt persistence/reload and changed-case checks; do not claim that its code-corpus results validate a support or method library. The general engineering requirement is to test the source/view relation the receiving use relies on.

A software observer can obtain idempotency support from a runtime library where its persistence and execution assumptions hold. The [AWS Powertools idempotency documentation](https://docs.aws.amazon.com/powertools/python/latest/utilities/idempotency/), especially “Concurrent identical in-flight requests” and “Lambda request timeout,” distinguishes in-progress and completed records, rejects concurrent processing and allows another attempt after the in-progress timeout. This is a concrete comparator for KCAE.ENCOUNTER:4.3, not a required SDK. Its stored-result behavior does not settle an external effect performed before completion, or transfer Lambda's timeout semantics to another worker environment. Obtain those properties from the actual receiver and runtime.

## KCAE.Profiles:End
