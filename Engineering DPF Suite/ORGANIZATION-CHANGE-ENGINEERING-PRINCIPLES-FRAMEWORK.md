# Organization Change Engineering Principles Framework

> A domain pattern language for changing an organization's contributions, working relations, and capability while its work continues.

- **Author:** Anatoly Levenchuk, with AI-assisted development and review
- **Version:** 3 October 2026
- **Status:** Eternal alpha: a published working framework, already used in analyses and worked applications, while continuing to evolve.
- **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) for original framework content; third-party material retains its own terms.
- **Publication:** [FPF repository](https://github.com/ailev/FPF)

Begin with the organization-change difficulty that blocks useful work: the contribution to make, a relation to establish or revise, a work arrangement to compare, or a capability to realize.

Search the Table of Contents by a familiar term or working question to find the relevant PatternID. Use that pattern's Problem frame, Solution, worked cases, and checklist for your organization and decision. Start with the smallest result that changes the decision; follow another pattern when its contribution is needed.

The Readme offers selected practical entries. The Preface explains recurring distinctions, and the cross-pattern applications show how several contributions can be used together. The complete Table of Contents also serves questions outside those examples. For references to this version, use the [Citation](#citation).


# Table of Contents

Search the Keywords & Search Queries column for a difficulty, subject, or result you recognize. Each row links to the full pattern. The Readme offers selected starting examples; use this complete index for other working questions.

`OCE.*` is this framework's PatternID namespace. Numbers are stable addresses; the Parts give reader order and do not prescribe Work order.

## Public units

| Unit | Reader use |
| :--- | :--- |
| [Organization Change Engineering Principles Framework Readme](#organization-change-engineering-principles-framework-readme) | Follow connected methods through arrangement design, consequences, coordinated changes and continuing practice. |
| [Citation](#citation) | Cite the framework or one pattern with its author, title, release date, and publication address. |
| [Preface](#preface) | Distinguish actual arrangements from proposed ones and choose the structures relevant to the decision. |
| [OCE.Application - Cross-Pattern Application](#cross-pattern-application) | Work through PumpWorks, a hospital, a member-governed association, and OCE practice across practitioners. |
| [OCE.Reference - Framework Boundary and Refresh](#framework-boundary-and-refresh) | Find scope limits, dependencies, source use, related practices, and refresh conditions. |

**Part I - Frame the Change and Compare Organization Concepts**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [OCE.1 - Identify the Changed Organization and Intended Contribution](#oce1---identify-the-changed-organization-and-intended-contribution) | Eternal alpha | *Keywords:* change focus, organization boundary, outside contribution. *Question:* Which organization are we changing, and what contribution should guide the change? | FPF A.1.SCR, A.1.CSD, A.15.6 |
| 2 | [OCE.2 - Recover Current Organization Work and Arrangement](#oce2---recover-current-organization-work-and-arrangement) | Eternal alpha | *Keywords:* current organization, actual Work, formal and informal arrangements. *Question:* How does the organization get work done, and which relations support or obstruct it? | OCE.1; FPF A.22, A.2.1, A.13, A.15.1 |
| 3 | [OCE.3 - Generate and Compare Organization Concepts](#oce3---generate-and-compare-organization-concepts) | Eternal alpha | *Keywords:* organization concepts, alternatives, exploration. *Question:* Which materially different organization concepts are worth comparing? | OCE.1, OCE.2; FPF A.22, C.17, conditional C.18, C.11 |

**Part II - Design Organization Relations and Work Arrangements**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 4 | [OCE.4 - Design an Organization's Contribution Architecture](#oce4---design-an-organizations-contribution-architecture) | Eternal alpha | *Keywords:* contribution architecture, specialization, boundary crossings. *Question:* How should contributions be distributed and connected across specialization boundaries? | OCE.1-OCE.3; FPF A.22, C.30, C.32.PAD |
| 5 | [OCE.5 - Define Organization Positions](#oce5---define-organization-positions) | Eternal alpha | *Keywords:* institutional position, vacancy, continuity. *Question:* Is a stable organization position needed, and what establishes its identity? | OCE.1; conditional OCE.4; FPF A.2.1, A.6.REL |
| 6 | [OCE.6 - Establish Holder Assignments and Enabling Relations for Organization Change](#oce6---establish-holder-assignments-and-enabling-relations-for-organization-change) | Eternal alpha | *Keywords:* assignment, holder, authority, access, responsibility. *Question:* Who is assigned to contribute, with what authority and access, and which enabling relations are missing? | OCE.4; conditional OCE.5; FPF A.2.1, A.2.2, A.6.REL |
| 7 | [OCE.7 - Coordinate Product-or-Service and Organization Architecture Decisions](#oce7---coordinate-product-or-service-and-organization-architecture-decisions) | Eternal alpha | *Keywords:* product and organization architecture, Conway, alignment, mismatch. *Question:* How should the two architecture decisions constrain one another, including an intentional mismatch? | OCE.3, OCE.4; FPF C.30, C.32.CONWAY, C.32.PAD |
| 8 | [OCE.8 - Compare Human, AI, Robotic, and Provider Arrangements for the Same Organizational Work Result](#oce8---compare-human-ai-robotic-and-provider-arrangements-for-the-same-organizational-work-result) | Eternal alpha | *Keywords:* train, hire, provider, AI, robot, hybrid, whole work arrangement. *Question:* Which complete arrangement enables participants to obtain the same bounded result? | OCE.1-OCE.3; FPF A.15.8, A.2.2, E.23.CDI, C.38, C.11 |

**Part III - Realize Change While Work Continues**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 9 | [OCE.9 - Realize a Bounded Organization-Capability Increment](#oce9---realize-a-bounded-organization-capability-increment) | Eternal alpha | *Keywords:* capability increment, representative work, integration, exception return. *Question:* How can the organization obtain the selected contribution beyond an isolated demonstration? | OCE.4/OCE.8 decision; OCE.6; qualified integration, learning and service results |
| 10 | [OCE.10 - Choose a Response to Participation or Working Culture Difficulties in the Target Organization](#oce10---choose-a-response-to-participation-or-working-culture-difficulties-in-the-target-organization) | Stable | *Keywords:* participation, resistance, working culture, intervention. *Question:* Why is a needed contribution not occurring, and what response is warranted by the available evidence? | OCE.6; applicable HCD.1/HCD.3/HCD.4 or direct professional results; C.36; conditional C.28 |
| 11 | [OCE.11 - Coordinate Organization-Change Work with Continuing Service](#oce11---coordinate-organization-change-work-with-continuing-service) | Stable | *Keywords:* continuing service, capacity, dual operation, recovery, hand-back. *Question:* How can change work overlap with service without breaching its protected conditions? | ME.6; applicable OPS admission, resource and service results; conditional OPS.11.1/OPS.19, OCE.8/OCE.16; direct protection results |
| 12 | [OCE.12 - Distribute Leadership Contributions in Organization Change](#oce12---distribute-leadership-contributions-in-organization-change) | Stable | *Keywords:* leadership, briefing, feedback, mutual assistance, continuity. *Question:* Which leadership contribution is missing from the next work episode, and how can it continue? | Qualified leadership and learning Methods; OCE.6; conditional OCE.10/OCE.11; applicable HCD results |

**Part IV - Observe Consequences and Revise the Organization**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 13 | [OCE.13 - Observe and Compare Organization-Change Consequences](#oce13---observe-and-compare-organization-change-consequences) | Stable | *Keywords:* consequences, observation, comparison, gains, losses, causal limits. *Question:* What changed, for whom, and which comparison can change the next organization decision? | Qualified observation and measurement results; FPF C.16, A.10; C.28 when causal reliance is needed |
| 14 | [OCE.14 - Decide Whether and How to Revise the Organization from Qualified Results](#oce14---decide-whether-and-how-to-revise-the-organization-from-qualified-results) | Stable | *Keywords:* organization revision, retention, repair, reversal, authority. *Question:* Should the challenged organization relation be retained or changed, and under whose authority? | OCE.13 or a current direct result; actual authority; FPF C.11; conditional OCE.3-OCE.12/OCE.16 |

**Part V - Sustain Methods, Cross-Change Coordination, and OCE Practice**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 15 | [OCE.15 - Choose, Develop, or Refresh Organization-Change Methods](#oce15---choose-develop-or-refresh-organization-change-methods) | Stable | *Keywords:* Method repertoire, candidate Method, local adaptation, refresh. *Question:* Which existing Method or source contribution serves this use, and what repertoire repair or candidate construction is needed? | Method Engineering Principles Framework ME.1-ME.16 as applicable; FPF A.3.1, A.10 |
| 16 | [OCE.16 - Reconcile Simultaneous Organization-Change Work](#oce16---reconcile-simultaneous-organization-change-work) | Stable | *Keywords:* simultaneous changes, dependency, support retirement, direct return. *Question:* Does another separately managed change still need the condition we propose to alter? | ME.6; applicable OCE, OPS.1-OPS.7, A.15, C.32.MWA, and direct domain results |
| 17 | [OCE.17 - Continue and Renew Organization-Change Engineering Practice](#oce17---continue-and-renew-organization-change-engineering-practice) | Stable | *Keywords:* OCE practice, practitioner population, continuation, renewal. *Question:* Which practices continue across practitioners, and what makes them easier or harder to use? | FPF C.36; actual OCE cases; OCE.15/Method Engineering for Method repair; applicable HCD and direct conditions |

# Organization Change Engineering Principles Framework Readme

## Practical entries

Organization Change Engineering connects a proposed contribution with the relations that let an organization obtain it. A design states who should supply what to whom; assignments, access and authority determine which actions can occur; representative work shows whether the receiving result can be obtained. Observed consequences can then change a particular relation while useful parts of the arrangement continue.

These are selected examples of the language at work, not a catalogue or a prescribed transformation sequence. Enter where you have adequate inputs, and stop at the result your decision needs. The [Table of Contents](#table-of-contents) gives direct access to the methods; the [Preface](#preface) explains their boundaries and shared conditions. You can ask an assisting agent to explain a pattern or comment on your case in the language of your work, without framework jargon.

The cases are constructed illustrations. Their authority, service, learning and protection results are supplied premises, not evidence about actual organizations. In a real application, obtain the professional contribution or decision from the participant who can supply it.

### OCE-PUMPWORKS - Compare weekly AI-inspection work arrangements while service continues

- **Situation:** PumpWorks produces an inspection package with supporting evidence quarterly and needs the same bounded package weekly. Staffing, platform and provider proposals do not yet describe complete ways of obtaining it.
- **Question:** Which whole arrangement can produce the weekly contribution, and what is still needed before a trial or continuing use can rely on it?
- **First useful result or blocker:** A comparison of complete alternatives for the same result, with a decision or probe recommendation at its supported scope and the authority, access, support or protection still needed.
- **Start with:** [OCE.8 - Compare Human, AI, Robotic, and Provider Arrangements for the Same Organizational Work Result](#oce8---compare-human-ai-robotic-and-provider-arrangements-for-the-same-organizational-work-result), using the current organization, contribution and relation accounts. Reopen those inputs only where the comparison exposes a gap.
- **Stop or return:** Keep the initial recommendation, a later trial authorization and an observed capability result distinct. A changed support or service condition returns to the action and decision that rely on it.

1. **Recover what the comparison is meant to change.** In the [PumpWorks application](#oceapplication1---app-oce-01---pumpworks-weekly-ai-inspection-releases), [OCE.1 - Identify the Changed Organization and Intended Contribution](#oce1---identify-the-changed-organization-and-intended-contribution) bounds the engineering organization and its intended contribution. [OCE.2 - Recover Current Organization Work and Arrangement](#oce2---recover-current-organization-work-and-arrangement) recovers actual evidence supply, receiving decisions, provider support and service commitments. [OCE.3 - Generate and Compare Organization Concepts](#oce3---generate-and-compare-organization-concepts) uses participant knowledge to generate functional repair, changed stream/enabling relations and a provider hybrid.
2. **Make the contributions and their conditions explicit.** [OCE.4 - Design an Organization's Contribution Architecture](#oce4---design-an-organizations-contribution-architecture) specifies Electrical's evidence supply, Integration's source check and the return of unsupported claims. Safety acceptance and release remain separate decisions. [OCE.6 - Establish Holder Assignments and Enabling Relations for Organization Change](#oce6---establish-holder-assignments-and-enabling-relations-for-organization-change) establishes which appointment and access conditions are effective: E27's appointment and rig access obtain in the stated interval, while provider-repository access is decided but not effective. The separate claim of coordination responsibility lacks the rule and participant information needed to establish it. That distinction tells the practitioner which work can proceed.
3. **Compare whole ways for the same weekly result.** OCE.8 completes internal-platform, dual-holder and hybrid-trace alternatives around their performers, support, acceptance, burden and recovery. The quarterly baseline is useful comparison evidence but does not meet the weekly target. The result is a recommendation to probe the hybrid, with missing trial authority, effective provider access and protection/recovery evidence. It is not yet a choice of the hybrid or permission to run the probe.
4. **Use later supplied conditions without rewriting the earlier result.** The application's separate hypothetical continuation supplies trial authorization, effective permitted access, qualified learning support and service/recovery conditions. [OCE.9 - Realize a Bounded Organization-Capability Increment](#oce9---realize-a-bounded-organization-capability-increment) can then exercise the contribution through source/version checking, challenge, acceptance and an exception return. An ambiguous version cue defeats a rehearsal; its owner repairs it, and a qualified learning provider supplies practice, feedback and an uncoached assessment. The probe informs a separate bounded choice of limited hybrid use. Three later episodes, including provider-failure recovery and one without the initiating facilitator, support only the stated configuration, participants, release family and period.
5. **Include the whole change burden in continuing service.** [OCE.11 - Coordinate Organization-Change Work with Continuing Service](#oce11---coordinate-organization-change-work-with-continuing-service) uses the supplied forty-hour week: twenty-four hours of service, six of other commitments and four of interruption reserve leave at most six for all change work. A six-hour incident uses the reserve and two of those hours, leaving four. Learning, setup, extra review and debrief must fit together; the owners reduce starts, and the displaced probe remains unperformed. A larger incident or lost support reopens the remaining allowance.
6. **Repair the actual participation difficulty.** [OCE.10 - Choose a Response to Participation or Working Culture Difficulties in the Target Organization](#oce10---choose-a-response-to-participation-or-working-culture-difficulties-in-the-target-organization) distinguishes ineffective access from discouragement of early challenge through blame or date-only recognition. Access repair and an authorized challenge-and-response change are different actions. [OCE.12 - Distribute Leadership Contributions in Organization Change](#oce12---distribute-leadership-contributions-in-organization-change) obtains the needed brief, role support, feedback and debrief from capable participants; the manager's allocation of time does not replace a learning provider's assessment. Later peer use can support a local participation result, while wider cultural or causal claims remain open.

If another change proposes retiring an evidence-return channel still needed for challenged packages, use OCE.16 as shown below. Migration completion alone does not end that receiving need. Apply an adequate retention or replacement result in the service arrangement without repeating its comparison.

### OCE-CONSEQUENCES - Keep a useful contribution while repairing the service it disrupts

- **Situation:** The intended contribution improves, but another service deteriorates and the same support holder may be committed in incompatible windows.
- **Question:** What do the observations establish, and which relation can the responsible owner change now?
- **First useful result or blocker:** A comparison preserving both gain and loss, then a justified authorized revision or the particular missing relation, protection or authority result.
- **Start with:** [OCE.13 - Observe and Compare Organization-Change Consequences](#oce13---observe-and-compare-organization-change-consequences) for the unresolved consequence question. If an adequate result already identifies the challenged relation, enter [OCE.14 - Decide Whether and How to Revise the Organization from Qualified Results](#oce14---decide-whether-and-how-to-revise-the-organization-from-qualified-results) directly.
- **Stop or return:** Preserve a descriptive contrast at its supported scope. An authorized allocation change still needs effective assignments, usable support and the relevant receiving observations.

1. **Compare like observations and retain unlike consequences.** In the later, separately constructed PumpWorks episode, matching eligibility and counting rules apply to two eight-week windows. Late evidence returns fall from 8/40 (20%) to 3/40 (7.5%). Late service follow-ups rise from 2/20 (10%) to 6/20 (30%). Reports of extra checking after hours have no comparable earlier report set. OCE.13 retains all three results at their actual reach; staffing, incident and product mix still prevent attribution to the hybrid arrangement.
2. **Obtain the fact that changes the revision choice.** Suppose the assignment and work account separately confirms that one support holder is committed in incompatible windows. Qualified service and employment contributions establish protected coverage and feasible substitution. That result supports a bounded repair question without first proving the overall causal effect of the organization design.
3. **Compare the real revision alternatives.** OCE.14 compares the current assignment, a repaired support interval with qualified substitution, and suspension of the affected hybrid contribution with an available manual recovery. Under the supplied service constraint, unchanged double allocation cannot continue. The authorized owner selects support repair and accepts less time for other change work. Independent Safety acceptance and release authority remain unchanged.
4. **Make the decision usable and return its consequences.** After the required allocation and holder-acceptance acts occur, OCE.6 supplies the changed effective relation. OCE.9 establishes the still-missing support integration; OCE.11 protects the overlap and return to service; OCE.13 supplies the next comparison when it can change continuation. If protected coverage is unavailable, the dependent repair stops. The observed contrasts and unaffected contributions remain usable.

The [hospital application](#oceapplication2---app-oce-02---public-hospital-emergency-flow-change) changes the receiving question: shorter waiting among admitted cases can coexist with more severe-case diversion and missing follow-up. Obtain the clinical and measurement result needed for the intended patient claim. A qualified protection requirement can justify an authorized pause before overall causal attribution is settled; OCE does not supply the clinical judgement or that authority.

### OCE-ASSOCIATION - Preserve contribution and authority across membership and service changes

- **Situation:** A distributed association depends on volunteers, employers, publication services and bylaw-governed decisions. A chair's term or another change can remove a condition needed by continuing work.
- **Question:** Which relations remain effective, which contribution can continue, and which direct decision must return to each affected change?
- **First useful result or blocker:** The position and assignment facts needed for the next action, coordinated architecture decisions or a supported cross-change dependency with its direct result still needed.
- **Start with:** OCE.6 for an enabling condition, [OCE.5 - Define Organization Positions](#oce5---define-organization-positions) when position continuity or vacancy matters, or [OCE.16 - Reconcile Simultaneous Organization-Change Work](#oce16---reconcile-simultaneous-organization-change-work) for a condition changed by a separate initiative.
- **Stop or return:** Stop the action whose authority or support has expired; keep unaffected permitted work. A referral to governance is not its decision, and OCE.16 creates no authority over the participating organizations.

1. **Separate a continuing position from its present holder.** In the [association application](#oceapplication3---app-oce-03---distributed-member-governed-standards-association), OCE.5 describes the editorial-chair position already established by the effective bylaw, with its expected contribution and eligibility. If that basis is missing, the description remains a proposal or the position claim remains unresolved. Vacancy or a replacement holder need not create a different position. OCE.6 separately obtains the required election or appointment acts, volunteer acceptance, publication access and any employer permission. When no continuing position is needed, a direct assignment can suffice.
2. **Coordinate structures without forcing them to match.** [OCE.7 - Coordinate Product-or-Service and Organization Architecture Decisions](#oce7---coordinate-product-or-service-and-organization-architecture-decisions) compares organization-side, publication-service-side, joint changes and a bounded mismatch. Ballot rules, repositories, language communities and employer arrangements can justify different structures and timetables. Each responsible owner makes its own decision and states the contribution, accepted burden and condition that reopens it.
3. **Use the arrangement for a bounded receiving result.** With qualified participants, lawful source use, translation and repository support supplied, OCE.9 exercises an amendment packet through submission, challenge and correction. OCE.12 can supply peer facilitation and feedback. Packet preparation is not adoption of the standard. If the chair's term expires, OCE.11 stops the action needing that officeholder's authority; an OCE.14 reassignment remains a proposal until the body authorized by the current rules decides it.
4. **Follow one consequential dependency between changes.** Suppose a credential change expects authorization from an incoming chair, while the election change expects new credentials before the ballot establishing that chair. OCE.16 checks the alleged circle against the actual bylaws, authority, credential evidence and windows. Method Engineering ME.6 can compare the relevant order and support arrangements; OCE.4 and OCE.6 supply contribution and enabling-relation results; the association's governance body supplies the bylaw-authority judgement. Return each resulting condition, or the missing result, to both changes. An expired term remains expired, and a sufficient direct answer ends this coordination question.

### OCE-PRACTICE-CONTINUATION - Keep useful practice when names, examples and opportunities differ

- **Situation:** Practitioners use different labels for organization mapping; some recover useful relations, some fill charts, and others have no permitted case on which to act.
- **Question:** What is continuing, what needs repair, and what would another practitioner need to produce a usable result?
- **First useful result or blocker:** An account of observed use, a supported repair to its example or conditions for further use, or a specific method, capability, opportunity or access question.
- **Start with:** [OCE.17 - Continue and Renew Organization-Change Engineering Practice](#oce17---continue-and-renew-organization-change-engineering-practice) and one consequential episode.
- **Stop or return:** Use adequate current practice and qualified support directly. An additional clinic or handover needs a distinct receiving benefit worth its whole burden; a ready answer or lost opportunity can cancel it. Changed terminology, attendance and lack of opportunity do not by themselves establish either learning or loss of the method's useful action.

1. **Recover the action behind the label.** In the [practitioner application](#oceapplication4---app-oce-04---oce-practice-across-a-practitioner-population), eight practitioners work across three organizations. Four observed cases recover actual work, evidence supply and receiving decisions under different titles; two show charts without the needed relation; two lack a suitable permitted case. These are continued use, a gap to examine and unobserved use respectively.
2. **Use the sufficient current response.** Comparing a usable case with the shared example reveals that its recognition question rewards completed department boxes. Existing qualified case help can perform the needed critique and example/feedback repair within the group's permission. Use that provision and retain useful variants. Account for preparation, participation and follow-up; do not add a duplicate clinic. Later feedback asks which supplied contribution and receiving decision the practitioner recovered.
3. **Use another method only for its distinct question.** If the actual OCE method already contains the needed move, repairing its example need not create a variant. [OCE.15 - Choose, Develop, or Refresh Organization-Change Methods](#oce15---choose-develop-or-refresh-organization-change-methods) enters when the reusable method or available repertoire lacks an answer; it returns an account of available methods and remaining gaps, or an OCE candidate requiring the applicable Method Engineering qualification. Use qualified HCD or learning help when distinguishing a human difficulty from conditions of use would change the action. Use OCE.10 for participation in the target organization, which is a different question from continuation of OCE practice.
4. **Keep the later observation within its reach.** In the fictional follow-up, one practitioner recovers the contribution and authority in another case; another cannot obtain permitted evidence access. Retain the observed use and return the access gap to its owner. This does not establish the intervention's causal effect or lasting retention across the profession. A later changed case or lost support reopens the particular conclusion it affects.

## Citation

If you use this framework, cite it as below and add the version date shown above:

```text
Levenchuk, Anatoly. Organization Change Engineering Principles Framework.
GitHub repository: https://github.com/ailev/FPF
```

For a particular pattern, add its PatternID and title, for example: Organization Change Engineering Principles Framework, OCE.1 - Identify the Changed Organization and Intended Contribution. Retain the release date, and include a permanent link or stored copy when the exact wording matters.

# Preface


Use Organization Change Engineering when the decision is how to change an organization's relations or capability to make an intended contribution. For other management decisions, use their responsible practices.

Start outside-in with the contribution needed or the condition to preserve. Recover how the organization gets work done and the relations that make that possible, including effects on continuing service and other Systems. A chart can help locate a question; inspect the organization and Work it depicts.

The recurring difficulty is that a change proposal can name a desirable organization model while leaving the work of making it useful unspecified. An approved chart can coexist with inaccessible evidence; a capable employee can lack an effective assignment; faster internal work can shift delay to service users. OCE helps practitioners identify the particular relation or capability at issue, compare ways to change it, and obtain a result that another participant can use. A smaller repair or an explicit missing condition may answer the immediate question.

The language offers related Methods that can be used in different combinations. Its seventeen patterns retain separate entries because an organization concept, an effective assignment, an operating contribution, a consequence comparison and a revised arrangement answer different questions. The [pattern selection and result relations](#ocereference4---pattern-selection-and-result-relations) identify those first results. To recognize a useful entry, start with a concrete difficulty in work; obtain the stronger evidence and authority only for the claim or action that will rely on them.

## OCE.Preface:1 - From a bounded change to continuing organization development

Continuing organization development concerns how an organization can keep making worthwhile contributions as its situation changes. OCE supplies the deliberate change of organization relations and capability within that broader work. Strategy can change the intended direction; Operations can reveal an unworkable commitment; human learning can supply a needed capability; product or platform engineering can change what support is possible. Each contribution retains its own result and professional basis.

A bounded increment can therefore lead to further development without turning into one indefinitely continuing project. In the [PumpWorks application](#oceapplication1---app-oce-01---pumpworks-weekly-ai-inspection-releases), weekly evidence work becomes possible under additional conditions. Later observations show fewer late evidence returns alongside more late service follow-ups. The next change concerns a support assignment and its work interval. The organization can retain the useful contribution while repairing that relation, then observe what follows. A revisable programme can connect such efforts through actual commitments and dependencies; its description does not make future work performed or require a fixed maturity ladder.

Keep the subject of development explicit:

| Subject and practical question | Needed result and connection |
| --- | --- |
| A person must perform a contribution under stated conditions. | Human Capability Development supplies the human demand, diagnosis, intervention, assessment or later-use evidence actually needed. OCE can change assignment, access, support and work opportunity around that person. Their development and the organization's ability to obtain a joint contribution remain separate claims. |
| An organization must obtain a contribution through several participants and supports. | OCE.9 first uses a sufficient current realization result; where the organizational claim remains unsupported, it establishes and exercises the missing relations in representative work, including exception and recovery paths. Individual demonstrations are inputs; the receiving claim concerns what the organization can obtain under its actual conditions. |
| Participants in the changed organization repeatedly avoid or distort a needed contribution. | OCE.10 examines the cause in concrete episodes and changes a supported participation or working-culture condition. Access, workload, authority, learning and recognition can require different interventions. |
| OCE practitioners must continue a useful way of doing organization-change work across cases. | OCE.17 examines how the operative Method is encountered, criticized, selected, enacted, retained or lost. OCE.15 and Method Engineering receive a Method defect; HCD receives a human-development question. A source collection or workshop can support continuation, but later practice supplies its evidence. |

Use these distinctions to connect development contributions: later work can expose a learning need, improved support can make existing capability usable, and criticism of an OCE case can improve the Method. The relevant result crosses between practices only when it changes the receiving question.

## OCE.Preface:2 - Actual, formal, and possible claims remain distinct

Sources differ in what they can establish. Use a chart, policy, position description, process map, interview, Work trace or service record for the bounded claim it supports. Check whether the asserted organization relation actually holds in the relevant situation and time window.

An organization concept describes possible relations; choosing it does not establish them. A WorkPlan describes intended change Work. Support claims about performed Work, changed relations, organization capability, participation, adoption, implementation outcomes, organization results, retention and culture with the evidence each claim needs.

## OCE.Preface:3 - Several structures and several views can coexist

For the current decision, select the structure and direct relation you need to inspect. Relevant structures may concern contributions, Work, assignments, authority, resource access, information use, material transfer, service provision, coordination, capability, providers or culture. They need not be isomorphic. Do not call every connected arrangement a graph; a mathematical graph is one possible lens after its nodes, edges, relation meanings and intended use are selected.

Project, process, and case views can expose different claims about the same Work. A project viewpoint foregrounds commitments, allocations, and decision slots; a process viewpoint recurring contributions and controls; a case viewpoint changing evidence, exceptions, and next decisions.

**Constituent actions in ongoing work.** During a rehearsal of a proposed work arrangement, eliciting a handoff from one participant can be part of testing the new coordination Method, within the team's ongoing adoption work. If the intended arrangement requires colleagues to notice an exception without a manager's prompt, the facilitator's prompt changes the evidence obtained. Participants can know their individual tasks yet lack the intermediate coordination that makes the arrangement work. Make the needed practice and available support explicit before extending the change. FPF B.1.5.EW recovers the constituent connection; successful performance in this rehearsal remains distinct from sustained organizational capability.

[Connect contributions, concerns and consequences across a whole project](ENGINEERING-DPF-SUITE-REFERENCE.md#connect-contributions-concerns-and-consequences-across-a-whole-project) develops the connection from engineering an offering to changing the organization that supplies its professional work. The module-and-laboratory case joins contribution design, positions, assignments, authority, capability and provision, then exercises the arrangement and returns changed conditions to the responsible practice.

## OCE.Preface:4 - Pattern relations do not prescribe a lifecycle

`OCE.1 → OCE.2 → OCE.3` shows the result dependencies when the change focus, current-organization account and concept alternatives must all be developed. It is not a calendar sequence. A current account can be repaired while a repertoire is refreshed; a known concept can enter downstream design without repeating every earlier result; changed evidence reopens only defeated claims.

Use the smallest pattern whose result can change the decision. Follow a prescribed sequence when the selected Method requires it. The PumpWorks application is a worked example, the Table of Contents gives reading order, and a return to another practice asks for a needed specialist result.

## OCE.Preface:5 - How the contributions connect

The patterns connect organization design and realization with consequence comparison, revision, Method development and continuation of OCE practice. The [Table of Contents](#table-of-contents) identifies the specific question addressed by each pattern.

Use OCE.13 to assemble decision-relevant observations and compare consequences; causal attribution needs its own support. Use OCE.14 to decide how to revise organization relations within the decision-maker's authority and identify the work still needed. OCE.9–OCE.12 retain the local observation, correction and continuation tests used in realization, participation, service and leadership work.

Use `OCE.10` for a participation or adoption gap in the target organization's working culture, with `OCE.12` for leadership contributions and `C.36` for culture mechanics. Use OCE.17 to follow how OCE Methods are encountered, criticized, selected, enacted, retained or lost among practitioners. Distinguish that practice from its description and carrier, and identify the actual uses within the practitioner population. Treating that population as one System or capability holder requires a separate basis.

Continuing organization development can combine these contributions with Strategy, Operations, Administration, human learning, research and product engineering. A comparison can remain useful when a proposed revision cannot proceed. An authorized revision still needs realization and later observation.

## OCE.Preface:6 - Conditions for using the contributions together

A combination must fit the actual organization and interval in which its results are needed. Preparing participants, practising, installing support, running old and new arrangements together, reviewing exceptions, observing consequences and recovering service can all consume the same person's time or depend on the same provider. Individually plausible contributions can therefore be unavailable together. Establish the joint feasibility of the selected contributions with the participants whose work or support is required, including capability, access, authority and protection conditions that hours alone cannot express. When change work overlaps with a continuing service, use OCE.11 to recover the complete overlap with the affected participants and service owner.

OCE.11's constructed PumpWorks case makes this condition concrete. In E27's supplied forty-hour week, continuing service uses twenty-four hours, other commitments six and interruption reserve four, leaving at most six for all change-related work. A six-hour incident consumes the reserve and two change hours, leaving at most four. Learning, setup, extra review and debrief must fit that remainder together. The responsible owners reduce the change start; the displaced probe remains unperformed. This is a qualified case input, not a general capacity formula. Another specialist's availability and the provider's support require their own basis. A larger incident can invalidate the remaining allowance.

The same joint question applies to relations as well as resources. A repository change may retire an evidence return while another change still needs it. OCE.16 finds that consequential dependency between separately managed changes and returns the direct result to each. ME.6 supplies a needed Method co-use comparison; OCE.8 supplies a whole work-arrangement comparison; Operations and other responsible practices supply the operating and professional decisions. Where the interaction affects continuing service, OCE.11 applies the relevant results to that bounded overlap and hand-back. Once a sufficient result exists, use it within its conditions.

When an interval, support, protection or authority condition changes, reconsider the combinations that depend on it. The change need not invalidate an independent organization account, comparison or retained Method. This permits continued useful work while a defeated branch waits for the result it needs.

## OCE.Preface:7 - Architectural Rationale

OCE is organized around recurring organization-change difficulties and the results that answer them. FPF supplies the shared distinctions for Systems, relations, capability, Work, evidence, Methods, comparison and choice. The OCE contribution is to use them in organization-change work: generate organization concepts, design contribution and position arrangements, establish assignments and enabling relations, realize a contribution while service continues, examine consequences, revise the organization, and continue the practice of doing that work. Using FPF and direct sources alone is sufficient for a question they already answer; the connected OCE language makes the recurring domain work available without reconstructing it each time.

The separation among patterns follows consequential choices in practice:

| Architectural choice | Serious alternative and when it can help | Why the distinction changes OCE use |
| --- | --- | --- |
| Separate contribution design, position identity, effective assignment and realization. | A chart or position description can give a compact view. A direct arrangement can suffice where vacancy and position continuity do not matter. | OCE.4 describes proposed contribution relations. OCE.5 establishes a continuing position when needed. OCE.6 establishes or checks the assignment and enabling relations; OCE.9 uses sufficient existing evidence or tests the still-unsupported organization contribution. A proposed design, appointment and installed tool can be useful before the capability exists. |
| Coordinate organization and product/service architectures through separate decisions. | Similar boundaries can reduce a demonstrated coordination burden. | OCE.7 compares organization-side change, product/service-side change, joint change and a bounded mismatch. Shared platforms, scarce capability, independent assurance, regulation and provider relations can justify unlike structures. Each decision still needs its own authority and evidence. |
| Compare complete work arrangements for the same result. | A learning, staffing, provider, platform, automation or robotic proposal can be a useful candidate contribution. | OCE.8 completes each serious option around one result, use, horizon and acceptance basis before comparison. Supporting work, recovery, participant consequences and professional conditions can reverse a component's apparent advantage. A human–AI synergy claim needs comparison with the applicable solo alternatives and representative evidence. |
| Give realization, participation, service coexistence and leadership their own entries. | Competent implementation can already supply a qualified whole result, including participation, support and evaluation. | Use that result where it is sufficient. For a remaining difficulty, OCE.9–OCE.12 answer different causes and return different first results. A participation gap may need access repair; a service conflict may need a smaller change interval; a leadership contribution may need practice and support. The same word “implementation” does not determine those actions. |
| Keep consequence comparison separate from organization revision. | A local observe-and-correct Method can already close a bounded problem. | OCE.13 can produce a useful comparison when nobody present can authorize a revision. OCE.14 can use a direct service, safety or authority result without a broader observation exercise. Causal evaluation is needed where causal reliance changes the decision; a qualified descriptive result can support a narrower response. |
| Distinguish Method maintenance, working culture in the target organization and OCE practice across practitioners. | One combined learning or culture account can show their connections. | OCE.15 can repair a Method even when it is popular; OCE.17 can investigate why a sound Method no longer gets used. OCE.10 acts on a target organization's participation and recurrent work. A change in any one can supply evidence to the others without settling their claims. |

A fixed change-stage model is useful when a selected Method actually requires that sequence. The language as a whole instead preserves direct entries, conditional returns and simultaneous work. Its Parts group reading, and its pattern relations explain how one result can support another. Neither relation imposes a complete route on every use.

## OCE.Preface:8 - Applying the language in different settings

The shared questions about contribution, actual work, relations, realization and consequences stay available as the setting narrows. The existing applications show which assumptions must change:

| Setting | What changes in the use | First result that remains useful at the boundary |
| --- | --- | --- |
| Engineering organization with AI and provider support | Same-result comparison must include the actual support, evidence, provider-access and recovery configuration. Safety acceptance and release authority can remain separately held. | PumpWorks first returns an arrangement recommendation with a precise reroute. Only the later episode's additional authority, access and professional conditions permit its bounded probe. |
| Public hospital with uninterrupted clinical service | Clinical competence, licensure, patient protection, privacy, staffing and case mix qualify the organization-change work. Product-team assumptions need their own justification. | A contribution or arrangement comparison can expose the professional result still missing. Observations about admitted cases do not answer for diverted or unobserved patients. |
| Member-governed standards association | Bylaws, independent employers, voluntary work windows and expiring officeholder authority replace assumptions of one executive and freely allocable staff. | A qualified editorial arrangement or revision proposal remains useful while a binding decision waits for its actual authority. |

These applications use shared Methods with changed conditions; they do not establish transfer of a clinical, engineering or governance result between the settings. The [practitioner-population application](#oceapplication4---app-oce-04---oce-practice-across-a-practitioner-population) changes the subject again: it concerns OCE continuation across practitioners, including observations outside one organization's control. It needs evidence about their actual cases and opportunities, rather than treating the population as one organization or capability holder.

## OCE.Preface:9 - Practical gains, costs and limits

The practical gain is a more precise next change: retain what works, identify the relation that prevents the intended contribution, obtain its missing professional result, or stop an unsupported action. The consequence comparison keeps an observed local improvement visible beside transferred burden. Revision can change the failing relation without discarding the whole arrangement. The cost is work to recover current conditions, involve knowledgeable participants, compare serious alternatives and observe use. Even a small intervention can consume scarce learning, support and recovery time.

The sources and cases bring perspectives with different limits. A sponsor can see formal milestones while workers experience hidden coordination or displaced work. Available records can omit dissenting, departed or peripheral participants and people without permitted evidence access. Ask whose missing account could change the diagnosis or comparison, and preserve uncertainty when it cannot be obtained. Healthcare implementation research, software service practice and technical-product examples require qualification when used in another setting. The constructed applications illustrate the Methods; they supply no estimate of OCE's comparative effectiveness or enduring organizational improvement.

## OCE.Preface:10 - Questions before relying on a combined result

For the current use, ask:

- Which organization, contribution and changed relation does this result concern, and what can the receiving participant now do?
- Which claims describe possibilities, effective relations, performed work or demonstrated capability, and what supports the distinction?
- Do the necessary contributions fit together under the actual time, support, authority and protection conditions?
- Which observations include benefits, displaced burden, affected participants and material uncertainty? Does the proposed reliance need stronger evidence?
- Which result still has to come from another practice, and which action depends on it?
- What changed condition would reopen this conclusion while leaving the other results usable?

Use the selected bodies' checklists for their specific questions. Recognition of an OCE difficulty needs less than assurance of an organization capability, authorized revision or causal effect; the claimed result determines the further evidence.

## OCE.Preface:End


# Part I - Frame the Change and Compare Organization Concepts

## OCE.1 - Identify the Changed Organization and Intended Contribution

> **Type:** Method pattern
> **Status:** Eternal alpha
>
> **Primary working result:** a **bounded organization-change focus** naming the actual organization System, intended outside contribution, changed Work and capability questions, consequence-bearing Systems, decision and authority boundary, evidence gaps, next result, and one observation that reopens the focus.

### OCE.1:0 - Use This When

Use this pattern when a request says “transform the organization”, “change the operating model”, “reorganize the team”, or “become AI-first”, but nobody can yet state which organization is changing or what outside contribution should improve. Enter when a chart, programme name, leader’s remit, or population label is standing in for the organization and the affected Work.

Begin with the decision that needs the focus and the contribution expected outside the organization boundary. Identify the actual organization System when systemhood matters. Keep the actual organization distinct from a possible future organization, a target chart and the programme for changing it. Treat a coalition, provider network or list of people as that organization only when the required System and relation claims are supported.

The first useful result is small: one organization, one intended outside contribution, the Work and capability questions that may need to change, the authority under which the focus can be used, and a bounded affected-System account or explicit discovery gap.

Do not use OCE.1 to choose strategy, grant corporate or legal authority, manage continuing operations, design a product, develop one person’s capability, or decide a target organization. Obtain the specialist result when it is the current blocker. Return to OCE.1 only if it changes the organization, contribution, affected Work, authority, or consequence boundary.

#### OCE.1:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| changed organization | The actual organization System selected for one change decision. A business-unit name or chart box may help locate it but does not establish its boundary or relations. |
| intended outside contribution | The contribution the organization is intended to make to a containing, using, receiving, or neighboring System under stated conditions. It orients change; assess its value and achievement separately. |
| changed Work question | A question about the actual or intended Work whose result, performer, coordination or conditions may need to change. Distinguish this Work from the Work of the change programme. |
| organization capability question | A question about the named organization’s ability to perform a named Work family under stated conditions. Capability is not a position, tool, training event, resource, assignment, or isolated result. |
| decision-relevant organization facts | Separately governed claims about actual Work occurrences or intended Work, supplied results and contributions, holder assignments, decision authority, resource access, information use, material transfer, service provision, coordination, and participation. These fact questions help choose what to investigate next. |
| affected-System account | The ordinary `A.1.CSD` result for Systems whose decision-relevant characteristics may change through supported relations or modal paths. Assess harm, benefit, interest and causal effect separately. |
| authority boundary | The independently supported relation under which a named System may issue or use the current organization-change decision. Sponsorship, responsibility, capability, budget, and assignment do not imply it. |
| organization-change focus | The bounded result returned by this pattern. It selects attention and downstream questions; it does not select an organization concept or authorize change Work. |

### OCE.1:1 - Problem Frame

Organization change is often named from the inside: a reporting line, function, headcount, technology introduction, merger programme, or leadership concern. Yet the reason for changing usually lies in a contribution outside that description: safer service, shorter evidenced delivery, restored reliability, a different customer outcome, or a new regulatory result.

Starting from the inside hides cross-boundary Work and can smuggle the preferred intervention into the problem. A bounded focus keeps the contribution, organization, affected Work, authority, and consequences visible before concepts are generated.

### OCE.1:2 - Problem

Without a bounded focus, every later result can be locally polished and globally misplaced. A team can optimize one handoff while the intended contribution depends on another organization; call a provider part of the organization without a supported relation; treat employees as the only affected Systems; or widen an executive request into authority for every downstream decision.

The change effort then has no truthful stop because neither the receiving contribution nor the changed organization was fixed.

### OCE.1:3 - Forces

| Force | Tension |
| --- | --- |
| Urgency | Leaders want a target quickly, while a false organization boundary makes later speed expensive. |
| Familiar labels | Charts and programme names aid orientation, while they can hide the actual System and relations. |
| Outside contribution | One contribution should orient the focus, while an organization can make several contributions to several receivers. |
| Consequence breadth | Employees and customers are visible, while providers, service Systems, products, natural Systems and future users may also bear consequences. |
| Authority | A bounded decision needs a legitimate issuer, while responsibility, influence, sponsorship, and access can be mistaken for authority. |
| Reopening | The focus must be useful now, while evidence about Work, contribution, authority, or affected Systems can defeat it. |

### OCE.1:4 - Solution

Select the smallest organization-and-contribution focus that can orient the current change decision. Recover the actual organization through `A.1.SCR` when needed, use `A.1.CSD` for affected-System discovery, then state the intended contribution, Work and capability questions, authority, participation questions and result needed by downstream patterns.

Use an adequate existing strategy or organization-change brief as input. If it already establishes the contribution, organization, authority and consequence boundary needed here, reuse that content. Obtain a strategy result when the direction itself is disputed; only a changed organization question returns here.

An ambiguous transformation request is enough to enter when the receiving decision lacks a clear organization or contribution. Before relying on the focus, obtain evidence for its claims about System identity, Work, contribution, assignment, authority, access, participation, capability and consequences.

#### OCE.1:4.1 - Pattern-Use Unfolding

1. **Name the receiving decision and first user.** State who needs the focus, what decision it enables, the horizon, and what useful result permits a stop.
2. **List materially different organization candidates.** Consider a formal entity or unit, an organization spanning cross-boundary Work, or one including providers when each is plausible. Keep a return to a non-organization question available. Use `A.1.SCR` only when System identity changes the decision.
3. **State the intended outside contribution.** Name the receiver, relevant conditions, and supplied result or preserved condition. Keep strategy, value, benefit, and performance as separate questions.
4. **Recover changed Work and capability questions.** Name the Work families, result or contribution relations, performer or coordination facts, and capability claims that could change. Do not infer them from a chart, proposed position, plan, or tool.
5. **Name other decision-relevant organization facts.** Ask which holder assignments, authority relations, resource-access relations, information-use relations, material transfers, service provisions, coordination occurrences, and participation facts must be recovered next. If a source calls these an “interface”, select the boundary and direct relations before relying on it.
6. **Discover consequence-bearing Systems.** Use `A.1.CSD` from the organization, contribution, affected Work, horizon, and decision. Include employees, providers, customers, products, service Systems, neighboring organizations and other material Systems when supported.
7. **Recover authority and specialist returns.** Name the authority subject, decision scope, window, and basis. Return unresolved strategy, governance, legal, safety, labor, operations, engineering, finance, or person-capability results to their owners.
8. **Select, return, and reopen.** State the organization, contribution, included questions, affected-System scope, exclusions, rejected candidates, next result, and one observation that reopens the focus.

#### OCE.1:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| use boundary | First user, receiving decision, horizon, and useful stop. |
| organization candidates | Candidate Systems or intended referents, supporting and missing relations, rejected alternatives, and selected organization. |
| intended contribution | Receiver, contribution claim, conditions, and unresolved value or performance questions. |
| changed Work and capability | Work families, current or intended status, supplied-result or contribution relations, and capability questions. |
| organization facts to recover | Named assignment, authority, access, information-use, transfer, service, coordination, and participation questions; no catch-all relation. |
| affected Systems | `A.1.CSD` reference or bounded Systems, supported relations or modal paths, possible changed characteristics, gaps, and specialist returns. |
| authority | Subject, decision scope, window, basis, and evidence boundary; otherwise an authority blocker. |
| continuation | Next useful result and one observable reopen condition. |

#### OCE.1:4.3 - What Changes in Practice

The practitioner stops treating “the organization” as self-evident. Every downstream concept or intervention must answer to one contribution, actual Work and capability questions, affected Systems, and a real authority boundary. The focus remains small without erasing providers, customers, continuing service, or specialist constraints.

### OCE.1:5 - Archetypal Grounding -- PumpWorks AI-Inspection Releases

PumpWorks wants weekly evidenced AI-inspection releases while field service and support continue. The initial request says “make Engineering product-oriented and AI-first.” The chart does not decide whether the changed organization is all of PumpWorks, the Engineering organization, a release coalition, or a provider-inclusive whole.

| Candidate | Current disposition |
| --- | --- |
| `PumpWorks` legal and operating company | Too broad for this organization-design decision; corporate and legal questions remain specialist returns. |
| `PumpWorks-EngineeringOrg` | Selected actual organization System because the named Work and decision concern its cross-functional engineering contribution. |
| “AI release team” | Not an actual organization System; retain as a possible future concept label. |
| AI provider plus PumpWorks Engineering | A possible cross-boundary configuration, not an obtaining organization whole. Provider relations must be recovered directly. |

The intended outside contribution is that `PumpWorks-EngineeringOrg` enables weekly evidenced AI-inspection releases usable by the product and service organization while current field service and support continue. Its value, feasibility, safety and achievement remain separate questions.

Changed Work questions concern product definition, electrical and software integration, safety evidence, model-artifact supply, release decisions, and field-service information returns. The capability question asks whether Engineering can repeatedly produce the evidenced release under those conditions. A plan, AI tool, or isolated build does not establish that capability.

Affected-System discovery includes the contributing practitioners, provider, customers and service personnel, released products, service Systems, and other Systems reached through supported safety, information, Work, or use relations. The focus records unknown customer-use and provider-authority paths.

The engineering director’s sponsorship is not universal authority. The next `OCE.2` account must recover actual Work, supplied-result and information-use relations, holder assignments, safety and release authority, rig access, provider service and support relations, participation, and evidence windows. Reopen the focus if field-service or provider Work makes another organization System the decision-bearing subject.

### OCE.1:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| chart-boundary bias | A box becomes the changed organization. | Test System identity and the relations needed by the decision. |
| intervention-first bias | “Agile”, “AI-first”, or a target operating model becomes the contribution. | State the outside contribution and changed Work first. |
| employee-only bias | Only people inside the formal unit are treated as affected. | Trace supported relations to consequence-bearing Systems without inferring value or harm. |
| sponsor-authority bias | A visible sponsor is assumed to hold every decision right. | Recover subject, scope, window, basis, and evidence for authority. |
| capability-by-resource bias | A tool, hire, training event, or budget is reported as capability. | Name the Work family and conditions and obtain capability evidence. |
| whole-by-cooperation bias | Repeated cooperation with a provider creates one organization. | Keep Systems and their obtaining relations distinct. |

### OCE.1:7 - Conformance Checklist

- [ ] The opening names a receiving decision, first user, horizon, and useful stop.
- [ ] The changed organization is selected from materially different candidates with supported System status.
- [ ] The intended contribution names its receiver and conditions without claiming value or achievement by declaration.
- [ ] Work, capability, assignment, authority, access, participation, and supplied-result claims remain separately governed.
- [ ] Affected-System discovery uses supported relations or modal paths and states uncertainty and specialist returns.
- [ ] Claims about assignment, responsibility, sponsorship, permission, capability and authority have their respective support; none is inferred from another category alone.
- [ ] An “interface” is never used instead of the selected boundary and direct relations.
- [ ] Exclusions, next result, and an observable reopen condition are explicit.

### OCE.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “The whole company is transforming.” | Name the decision and compare organization candidates at the smallest decision-changing grain. |
| “Our goal is to implement Team Topologies.” | Treat the topology as a possible concept; recover the contribution first. |
| “Employees are the stakeholders.” | Discover consequence-bearing Systems and keep interest, representation, protection, benefit, and harm separate. |
| “The executive asked for it, so authority is covered.” | Recover the authority relation for each relied-on decision scope. |
| “Training the team creates the capability.” | Treat training as a possible intervention and evaluate capability for the Work family separately. |

### OCE.1:9 - Consequences

The focus makes later recovery and concept generation answerable and reveals when the useful next result belongs outside OCE. Some requests narrow sharply or stop because the contribution, organization, authority, or consequence path is unsupported.

The cost is early disagreement about boundaries and evidence. That disagreement occurs before a target organization accumulates commitment and sunk cost.

### OCE.1:10 - Rationale

An organization-change decision concerns the relations that need to change among actual Systems and Work. Beginning with outside contribution protects the reason for change while System and consequence recovery prevent an inside-only view. The pattern stops before concept generation because a bounded focus is already useful.

### OCE.1:11 - SoTA-Echoing

**Practice question.** What is the smallest defensible focus for an organization-change decision before a target configuration is chosen? The selected answer combines an intended outside contribution with a supported organization boundary, decision authority and consequential outside relations. Its gain is a usable focus even when an executive label, provider boundary or affected population is misleading; it does not supply the strategy itself.

A serious alternative is the strategy-led framing in Galbraith's [Star Model](https://jaygalbraith.com/wp-content/uploads/2024/03/StarModel.pdf), especially its Strategy and Implications sections. It starts from direction and criteria for design trade-offs, then coordinates structure, processes, rewards and people. This remains a substantive practitioner alternative although the text is historical; its current hosting date does not make it new research. **Adopt** deriving organization-design criteria from the contribution and direction. **Adapt** that framing in OCE.1:4.1, steps 1–4 and 7, by separately establishing the organization and authority to which the change applies. **Reject** treating a sponsor's remit as sufficient evidence for every needed decision.

Compare the two on the same bounded task, with the same existing strategy, permitted records, participants and decision deadline. Either can identify the weekly evidenced release in the PumpWorks case. OCE.1:5 additionally makes the competing organization referents and separate safety/release authority inspectable before the concept is built. This is useful where those claims are unsettled; it costs explicit boundary and evidence work. A strategy-led inquiry is shorter when those premises are already clear, and an adequate result from it is reused under OCE.1:4. The selection accepts the extra work only when it can change the focus. The constructed comparison establishes that distinction, not measured superiority in organizations.

[Albert's 2023 online/2024 issue account](https://doi.org/10.1007/s41469-023-00152-y) supplies another serious starting point: choose among activity, decision-representation and legal-entity perspectives. **Adopt** their possible divergence and **adapt** them to the candidate-boundary questions in OCE.1:4.1, steps 2 and 5. A perspective-led focus can suffice for a known entity. For a provider-spanning proposal, the selected OCE answer adds the System question from `A.1.SCR` and consequence discovery from `A.1.CSD`, rather than inferring a whole from one representation. Albert's point-of-view argument is not an exhaustive organization ontology or empirical validation of this method; requiring all three perspectives for every small use is rejected.

The [work-design review by Fraccaroli, Zaniboni and Truxillo](https://doi.org/10.1146/annurev-orgpsych-081722-053704) provides a consequential limit on a focus confined to output and structure: the work people perform and their outcomes also matter. **Adapt** that concern in OCE.1:4.1, steps 4 and 6, through separate Work and affected-System questions. The accessible abstract of [Aust et al. (2023)](https://doi.org/10.5271/sjweh.4097) supports outcome-specific caution, not a ranking of interventions. Neither source turns consequence discovery into proof of benefit or effectiveness; OCE.1:0 and :5 keep those questions separate. No fuller Aust result is relied on here.

Reopen when a recurring case cannot be bounded this way, a credible alternative obtains an equally usable focus with less total work, or new evidence about organization identity, authority or consequences changes the receiving decision.

### OCE.1:12 - Relations

- `A.1.SCR` governs System recognition when systemhood is load-bearing; `A.1.CSD` governs affected-System discovery. Use their results to define the organization and consequence boundary for OCE.1.
- `A.15.6` keeps project System, use, Work, Method, support, and development subjects distinct; `A.10` governs evidence reliance.
- Strategy supplies direction and strategic commitments. Corporate Governance and specialist legal practices supply their authority results. Obtain the applicable authority result before relying on the focus for that decision.
- `OCE.2` consumes the selected organization, contribution, Work questions, named organization-fact questions, affected-System gaps, and authority boundary. `OCE.3` receives the focus only with a grounded current account or explicit tolerated gap.
- Use `OCE.10` for target-organization working-culture questions arising from participation or adoption gaps; use `OCE.17` for the culture of OCE practice among practitioners.

### OCE.1:End

## OCE.2 - Recover Current Organization Work and Arrangement

> **Type:** Method pattern
> **Status:** Eternal alpha
>
> **Primary working result:** a **grounded current-organization account** that identifies the actual Work, supplied results, holder assignments, authority, responsibilities, resource access, information use, material transfer, service provision, coordination, participation, and results needed by one organization-change decision, while keeping formal, observed, contradicted, and unknown claims distinct.

### OCE.2:0 - Use This When

Use this pattern when a chart, process map, job catalogue, policy, target operating model, or leader interview is being used as a complete account of the current organization. Enter when a decision depends on how Work actually proceeds, who contributes, which assignments and authority relations obtain, what resources are accessible, or where formal and observed claims diverge.

Begin with a compatible `OCE.1` focus or equivalent content. Select only the Work and direct relations that can change the decision.

The first useful result is a bounded account with each claim's source, status, window and uncertainty. Stop when it supports the decision or identifies the gap that prevents it.

Do not use OCE.2 to invent target positions, assign holders, redesign contribution boundaries, or judge an informal relation defective merely because it differs from policy. Use `OCE.3` for concepts and the owning downstream pattern for design or assignment.

#### OCE.2:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| actual Work | A dated performed occurrence admitted under `A.15.1`, with the performers' `A.13` basis, an enacted Method, time interval and containing System. If that basis is incomplete, keep the supported observations and the unresolved Work claim. A schedule, workflow description or recurring label is not Work. |
| supplied result and contribution | A result or preserved condition supplied to a receiving System or Work through a named relation. A duty statement does not prove supply. |
| organization position | An organization-dependent institutional position governed by OCE.5. Its identity depends on the owning organization, an effective establishment basis, and identity-bearing expected-contribution and assignment-eligibility criteria. It continues only while that basis remains in force and those criteria remain the same. It is neither a System, system-role kind, assignment, holder, nor description. |
| position description | An episteme describing a position, its expected contributions, eligibility, and applicability. A description does not establish the position or an assignment. |
| system-role kind | A local classification usable by a declared assignment species. Support any assignment, capability, responsibility, authority or performed-Work claim separately. |
| assignment | An obtaining occurrence of a declared species under `U.SystemRoleAssignment`. Its holder, assigned system-role kind, scope, window, and any real position participant remain recoverable. Identify the actual performer separately. |
| authority | A direct relation under which a named System may issue a named decision result within a scope, window, and basis. It is not inferred from assignment, responsibility, seniority, or participation. |
| resource-access relation | The relation by which Work or a System can use a named resource under stated conditions. Resource presence, budget, and licence are different claims. |
| boundary relations | Named contribution, information-use, material-transfer, decision, service-provision, access, or coordination relations across a selected organization boundary. “Interface” may be retained as ordinary shorthand only after the boundary, selected structure, members, and direct relations are stated. |
| formal/observed claim pair | Two separately sourced claims about what should obtain and what evidence says obtains. Their difference is a finding, not automatic failure. |
| current-organization account | The bounded episteme returned for one decision use, describing the supported Work and organization-relation claims and their gaps. |

If an existing organization-position claim lacks an effective establishment basis or the OCE.5 identity criteria, do not infer a position from a title or description. Record the expected-contribution claim, eligibility claim, holder, and assignment separately, plus the missing position-establishment or identity basis.

### OCE.2:1 - Problem Frame

Formal descriptions support authorization, communication, administration, or staffing. Observed Work exposes who resolves exceptions, which evidence reaches a decision, where providers enter, what resource is scarce, and which informal coordination preserves service. Both can matter; neither replaces the other.

Select separate contribution, Work, assignment, authority, resource-access, information-use, material-transfer, service-provision, and coordination structures for the decision. They can overlap without being isomorphic. A mathematical graph is an optional lens only after its nodes, edges, semantics, and use are selected.

### OCE.2:2 - Problem

When the chart stands for the organization, a designer can move boxes while leaving the actual bottleneck untouched. When observation stands alone, a temporary workaround can be mistaken for a reusable arrangement and formal authority or safety obligations can disappear.

The resulting concept has no defensible baseline. Later claims cannot say which relation changed, whether it obtained before, or who bore the burden.

### OCE.2:3 - Forces

| Force | Tension |
| --- | --- |
| Economy | A fast baseline is needed, while collecting everything produces an unusable inventory. |
| Formal and observed truth | Formal claims matter, while actual Work can differ and either branch can be stale. |
| Sensitive evidence | Interviews and traces reveal hidden Work, while they expose people, power, and provider relations. |
| Several structures | Contributions, Work, authority, and access answer different questions, while one diagram is easier. |
| Attribution | Practitioners need to know who performed Work and issued decisions, while assignment, authority, and performance are easy to collapse. |
| Currentness | Relations change during recovery, while false precision can outlive its evidence window. |

### OCE.2:4 - Solution

Recover the smallest evidence-bearing set of actual Work and direct organization relations that can change the decision. Use `A.22` to select each structure and the direct FPF or domain governor for each relation. Preserve formal, observed, contradicted, and unknown statuses, evidence provenance, and currentness.

One decision-changing difference between a formal description and observed Work is enough to enter. Support each Work, supply, assignment, authority, access, information-use, transfer, service-provision or coordination claim with evidence appropriate to its meaning and time window.

#### OCE.2:4.1 - Pattern-Use Unfolding

1. **Bound the recovery use.** State the organization, intended contribution, receiving decision and horizon. Select a result or preserved condition whose current production or use can change that decision. Begin with an available episode, including an unsuccessful attempt; extend the sample only where another condition could change the account.
2. **Reconstruct the episode from permitted sources.** Follow the result from the receiving use back to its contributors, then forward through the actual use and any exception return. Use the source-to-claim moves below. Ask participants to show what they used, supplied or decided on that occasion; retain their explanation and the supporting or conflicting trace separately.
3. **Identify Work at its supported precision.** For a relied-on Work claim, recover the performers' `A.13` basis and the `A.15.1` occurrence basis. Keep plans, routine descriptions, schedules and reports distinct from the occurrences they describe. When the basis is incomplete, preserve the observations and name the unresolved occurrence claim. Use `B.1.5.EW:4.1–4.5` when the connection between a constituent action and the receiving whole is unclear; it helps explain what that action performs, supplies or supports.
4. **Recover the decision-bearing relations.** Use `A.22:4–4.1` to select the structures needed by this question and `A.6.REL` or the direct relation governor to keep each predicate and its participants explicit. Recover supplied results, information use, material transfer, decisions, service provision, access and coordination as the episode requires. A carrier such as a ticket can supply evidence for several different relations.
5. **Check the institutional basis where it matters.** For a position, obtain the establishment and continuation basis under OCE.5; otherwise retain only the supported description, contribution, eligibility and holder claims. Use `A.2.1` for obtaining assignments. Establish authority, responsibility and resource access separately, with their scope, window and basis. Ask the participant or owner who can supply the missing evidence; hierarchy or a budget entry cannot settle another relation's claim.
6. **Match formal and observed claims.** Compare the same action or relation, participants, conditions and time window. Resolve an apparent difference by inspecting its basis, or retain the contradiction and competing explanations. The account distinguishes `agree`, `contradict`, `unknown` and `changed-window`; the worked procedure below explains their use.
7. **Return a bounded account or a specific gap.** Include omitted participants or burdens that can change the decision, the supported result path and its uncertainty. Use OCE.10:4.1–4.3 for a consequential participation gap, including its participant explanation and discriminating contrast. Stop when the account supports the receiving use or exposes the precise missing contribution. Reopen the affected claim when a new occurrence, source edition, participant account, provider condition, authority decision or service result defeats it.

##### OCE.2:4.1.1 - Turn an episode into a result path

Choose the episode from the receiving question. For a delayed acceptance decision, begin with the evidence that acceptance needed; for an unreliable service return, begin with the result the service user could or could not use. A conveniently documented meeting is a useful starting point only if it connects to that result. An ordinary completed episode can expose the usual path. A relevant exception, failed attempt or other contrast can expose a condition concealed by success. Neither is a statistical sample of the whole organization merely because it is concrete.

Put the permitted materials beside one another: the applicable rule or commitment; the result and its revisions; traces of request, supply, use and decision; and accounts from the people who performed or received the contribution. Ask ordinary questions: What did you need at this moment? What did you receive? What did you actually do with it? What happened when it was missing or unusable? Whom did you ask next? Ask the next consequential supplier or receiver to inspect that part of the account. This follows a result across a real boundary without requiring interviews with everyone.

Construct a short path in verbs, for example: Electrical supplied a compatibility report; Integration used it to challenge a package claim; Electrical returned a corrected result; Safety accepted the evidence; the release director decided release. Follow both the normal route and the exception that changes the decision. If a contribution serves two receiving uses, keep their different conditions visible. Use `B.1.5.EW` to settle whether an observed action is part of the encompassing performance or supplies separate support; temporal order alone does not settle that connection.

For each consequential link, inspect what the evidence establishes. A repository entry can establish that a version was present; it does not by itself show who interpreted it or whether a receiver used it. A decision record can show an issued result; the effective rule or delegation supplies its authority basis. A participant can explain an undocumented action; another trace or participant may corroborate, qualify or dispute that account. Write the supported claim at this stage, including a reported but uncorroborated action when that is all that is available. Keep a missing link visible instead of completing the expected route from the procedure manual.

##### OCE.2:4.1.2 - Match claims and resolve only consequential differences

Translate the relevant formal statement into the same concrete question as the observation. “Software owns the package” may concern package assembly, while “Electrical supplied the evidence” concerns the source of one input. Both can hold. Ask which action, result, participants and conditions each sentence names before marking contradiction. A policy that applied before a temporary delegation and an observation after it form a `changed-window` pair until the effective window is recovered.

When two claims really concern the same case and predicate, inspect the source closest to the disputed fact and an account from a participant affected by it. A newer chart is not automatically stronger than a dated transaction; an event log is not automatically stronger than the rule defining authority. Record which claim changes and why. If the source supports supply but receiving use is unobserved, that use remains `unknown`. If an applicable rule requires a prior acceptance and the inspected release record precedes the acceptance, retain a `contradict` pair at that scope; separately investigate its explanation and consequences.

Keep alternatives when they imply different repairs. A late return may result from unavailable rig access, a missing request, an unrecognized obligation or an incomplete log. Look for the smallest available contrast that can distinguish the live alternatives, such as the request and access state in another comparable episode. Use OCE.10 for the participation branch and the direct service or resource owner for the corresponding condition. A majority of interviewees agreeing does not remove contrary evidence, and a disagreement need not prevent an account that honestly preserves it.

##### OCE.2:4.1.3 - Stop in proportion to the decision

Ask which unresolved claim could reverse the next decision or make its use unsupported. Obtain another permitted observation only when it can change that decision, its warranted claim or its conditions enough to justify retrieval, participant effort and delay; use `C.11.DUA` when that appraisal is itself difficult. A sufficient existing result can end the inquiry. If neither rival explanation changes the current concept boundary, carry both into OCE.3 and stop. If a missing authority basis prevents an intervention, stop that intervention while preserving the account and permitted design work.

The result can be a few linked claims with a stated missing path. It need not be a census, a complete model, agreement among all participants or an admitted Work occurrence for every observation. Protect personal and commercially sensitive material according to the actual permission and professional conditions. If a source cannot be used, retain the resulting evidence limit; do not fill it with an inference from an unrelated case.

#### OCE.2:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| use boundary | Organization, contribution, receiving decision, horizon, selected structures, and exclusions. |
| source evidence | Permitted source or observation, the episode/result path it supports, claim kind, scope/window, sensitivity, and evidential limit. |
| actual Work | Supported occurrences, performers and their A.13 basis, enacted Methods, time intervals, conditions, containing Systems, associated results and limits; otherwise the observations and unresolved occurrence claim. |
| supplied results and boundary relations | Participants, direct predicate, result/content/resource, conditions, carrier/support distinction, evidence, and status. |
| position-related claims and assignments | Position establishment/continuation basis when available; otherwise separate description, expected-contribution, eligibility, holder, and assignment facts plus the missing establishment or identity basis. |
| authority, responsibility, resources | Direct relations, subjects, scopes, windows, bases, evidence, and blockers. |
| formal/observed comparison | Matched claims with `agree`, `contradict`, `unknown`, or `changed-window`; the reasoning resolving an apparent difference; surviving explanations and the decision consequence. |
| participation/consequences | Missing participants, hidden burden, affected-System questions, protection needs, and specialist returns. |
| return | Grounded account, unresolved gaps, constraints for `OCE.3` or `OCE.11`, stop, and reopen triggers. |

#### OCE.2:4.3 - What Changes in Practice

The organization is no longer represented by one chart. Practitioners can see which Work and relations matter, where formal and observed claims differ, what remains unknown, and which gap must be resolved before a concept or coexistence decision can be trusted.

### OCE.2:5 - Archetypal Grounding -- PumpWorks Current Relations

The `OCE.1` focus selects `PumpWorks-EngineeringOrg` and weekly evidenced AI-inspection releases while service continues. Recovery is limited to release Work, result supply and use, decision authority, provider service, rig access, and field-service information return.

The following inputs are stipulated for this constructed case. They show how an account is obtained, rather than supplying evidence about a real company. The recovery question is whether weekly package preparation should change its contribution boundaries. The practitioner obtains the current quarterly release procedure, the packages and permitted review records for a routine release R41 and a challenged release R42, the effective safety delegation, a rig-booking extract, and short accounts from the integrator, Electrical contributor and service liaison.

**Start at the receiving use.** The integrator identifies the compatibility claim needed for accepting R42's package. The package history points to Electrical's report E7, while the procedure says that Software prepares the integrated package. Reading these as source and assembly claims removes the apparent contradiction: Software assembled the package using evidence supplied by Electrical. The review's challenge refers to E7 and Electrical's corrected E8; this supports receiving use and exception return, not merely the files' presence. The participants identify the relevant actions, intervals and containing organization. A separate provider upload uses a shared account, however: the artifact's presence is supported while the precise performer and Work basis remain unresolved.

**Separate decisions and match windows.** The record contains a safety-evidence acceptance and a later release decision issued by different people. The effective delegation confirms their distinct scopes. The everyday phrase “Safety signs the release” is therefore replaced with two claims. For a meeting held before that delegation became effective, the same authority basis cannot be assumed; that earlier claim remains a separate window question.

**Work through a real mismatch.** The release plan claims rig access on Thursday; the booking extract and the integrator's account show that service diagnostics occupied the required interval. Those claims concern the same rig and interval, so access is contradicted although Engineering's general permission remains supported. A later timestamp also shows that the field-service fault summary arrived after R42's review. The liaison reports that a service incident delayed it; the integrator recalls requesting it late. The available records do not distinguish these explanations. Both justify keeping the information-return relation and its timing visible; neither establishes a general causal bottleneck or poor motivation.

**Choose the next observation or stop.** The request timestamp and the liaison's permitted allocation record could distinguish late request from service displacement. For the present concept comparison, either explanation requires an explicit information-return and exception arrangement, so the practitioner carries both forward without expanding the inquiry. A decision to reallocate liaison time would need that missing distinction and the service owner's conditions. The unsampled release families remain outside the account. The table below summarizes the supported claims and gaps; it is produced by this reconstruction, not inferred from the chart.

| Selected claim | Formal claim | Observed or current evidence | Current disposition |
| --- | --- | --- | --- |
| integrated-release evidence | Software prepares the integrated package at the quarterly checkpoint | Electrical engineers supply compatibility evidence used in a recurring cross-functional review with Software | Both supplied-result and information-use relations obtain in sampled occurrences; the chart does not show them |
| safety and release decisions | “Safety signs the release” | A named safety reviewer issues an evidence-acceptance result; the release director issues the release decision | Preserve two decision and authority relations |
| field-service information return | Field Service supplies quarterly feedback | Fault-pattern information reaches Product through a service liaison; completeness and window are unknown | Retain the observed information-supply/use relations and evidence gap |
| provider contribution | Provider supplies inspection models | Provider supplies model artifacts and remote support; access, exception handling, assurance, and decision authority differ by case | Recover each supply, service, access and authority relation separately; a claim that both parties form one organization needs its own basis |
| inspection-rig access | Engineering has the rig | The rig is shared with service diagnostics and unavailable in some release windows | Resource presence is supported; decision-window access is not |
| “release team” | A cross-functional release team performs releases | No maintained team assignment or position-establishment basis is supported; named people contribute through several assignments and coordination occurrences | Keep the phrase as a view label; recover holders, assignments, Work, and authority separately |

The account records sampled occurrences and source windows. Organization capability and causal-bottleneck claims need additional evidence appropriate to those claims. The rig-access gap, separate safety and release decisions, informal service return, and provider exception path constrain `OCE.3` and a future `OCE.11` decision.

### OCE.2:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| chart realism | Formal reporting relations become all organization relations. | Select each decision-changing structure and recover its relations. |
| observation realism | One workaround becomes a stable arrangement. | State occurrence, scope, recurrence evidence, and currentness. |
| title-to-position bias | A title identifies a position, system-role kind, assignment, capability, and authority. | Require the position basis or keep every supported claim separate. |
| carrier-as-relation bias | A meeting, ticket, API, or document becomes the contribution relation. | Name participants, direct predicate, result or content, conditions, and carrier use. |
| deviation-as-defect bias | Any formal/observed mismatch is called resistance. | Ask what result and consequence the difference produces. |
| complete-model bias | Recovery expands until every relation is mapped. | Stop at the receiving decision or blocker. |

### OCE.2:7 - Conformance Checklist

- [ ] The account names one decision, horizon, selected structures, and exclusions.
- [ ] The account shows how permitted traces and participant accounts support the consequential links of a selected episode, with scope, window, sensitivity and evidential limits.
- [ ] Actual Work is separate from plans, routines, process descriptions, and reports.
- [ ] Contribution supply, information use, material transfer, decision, service provision, access, and coordination remain distinct.
- [ ] A position claim has an establishment/continuation basis, or only its separately supported neighboring facts are recorded.
- [ ] Job title, position, system-role kind, holder, assignment, capability, responsibility, participation, and authority remain distinct.
- [ ] Every authority and access relation names its participants, scope, window, basis, and evidence.
- [ ] Formal/observed differences have explicit status and are not judged by mismatch alone.
- [ ] An unresolved difference is retained with its competing explanations or missing basis; further inquiry is selected by what it can change.
- [ ] The result stops before target design and supplies usable constraints.

### OCE.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “The org chart is the as-is architecture.” | Recover the Work and direct relations needed by the decision. |
| “The process map proves this is how work happens.” | Treat it as an episteme; identify actual occurrences and evidence. |
| “The product owner owns the decision.” | Recover the authority or ownership relation; the word “owner” supplies neither. |
| “Everyone works around the process, so adoption is low.” | Name the formal/observed relation difference, result, burden, and reason first. |
| “We need a complete digital twin.” | Recover only the structures and currentness needed by the decision. |

### OCE.2:9 - Consequences

The baseline can support concept generation because claims are tied to subjects, relations, evidence, and windows. It can also preserve valuable informal contributions that a target design might destroy.

The cost is plural representation. Contribution, authority, Work, access, and information-use structures may need different views. Their non-isomorphism is a finding.

### OCE.2:10 - Rationale

Ground the account in observed Work and supported direct relations. Separating formal and observed claims makes discrepancies inspectable. Requiring a position-establishment basis prevents a title or description from becoming an organization object by wording alone.

### OCE.2:11 - SoTA-Echoing

**Practice question.** How can a practitioner obtain a bounded current-organization account from heterogeneous permitted records and participant explanations, including disagreement and missing evidence? The selected answer is the episode reconstruction in OCE.2:4.1.1–4.1.3: follow a needed result through supply, use, decision and exception; match formal and observed claims at compatible scope and time; resolve only consequential differences and preserve the rest. `A.22`, `A.6.REL`, `A.2.1`, `A.13`, `A.15.1` and `B.1.5.EW` supply the distinct structure, relation, assignment and performance operations. The source-to-account connection is the OCE synthesis.

The serious alternative considered here is an experienced practitioner organizing a trace/interview walkthrough with [Albert's activity, decision and legal-entity perspectives](https://doi.org/10.1007/s41469-023-00152-y) (2023 online/2024 issue). Albert supplies those perspectives and explains their different implications; the trace/interview combination is specified here as a practical comparator, not attributed to that paper as a complete protocol. Both answers use the same available episodes, permitted documents and bounded participant access. The alternative can expose a structure absent from the chart and may already supply an adequate account. Such a result can be used directly.

The selected OCE answer makes the intermediate inferences explicit for a reader who must construct the account. In OCE.2:5, package assembly and evidence supply cease to look contradictory, the rig claim is matched to its actual interval, and a late request remains a rival to service displacement. Those distinctions affect different possible repairs even though the same high-level organization views could describe all of them. The added cost is claim matching and returning to a source when the receiving decision depends on it; no larger sample is prescribed. This is a constructive reason to select the developed method for this use, not an empirical finding that experienced reconstruction is inferior.

**Adopt** Albert's plural perspectives; **adapt** their use in OCE.2:4.1, steps 1 and 4, to structures that can change this decision; **reject** a requirement to recover every perspective before retaining a useful observation. The paper acknowledges other structures and permits a sufficient single perspective. OCE.2:4.1.2 adds its own formal/observed comparison, while :4.1.3 prevents that precision from becoming an organization census. When the missing link concerns participation, OCE.10:4.1–4.3 supplies the episode/participant/contrast inquiry; its result is reused at that narrower scope.

The [work-design review by Fraccaroli, Zaniboni and Truxillo (2024)](https://doi.org/10.1146/annurev-orgpsych-081722-053704) supports **adapting** the account to actual work characteristics and affected-person outcomes, reflected in OCE.2:4.1, step 7. It supplies no authority or capability conclusion for the organization being examined. [Grote et al., ISSE 2025](https://doi.org/10.1109/ISSE65546.2025.11370103), is an abstract-only contribution-bundle cue here: it can prompt investigation beyond job titles in step 5. The full method and results have not been established in this comparison, so that cue neither proves local assignments nor ranks a workshop method against this reconstruction. A fuller applicable treatment could change the comparison.

Reopen when the method loses a consequential informal contribution, cannot keep incompatible source windows apart, demands more inquiry than the decision can justify, or a developed rival supports the same distinctions with less total reconstruction work.

### OCE.2:12 - Relations

- `OCE.1` supplies organization, contribution, Work/capability questions, affected-System gaps, authority boundary, and horizon.
- `A.22` governs selected structure identity; direct relation patterns govern supplied-result, assignment, authority, access, information-use, transfer, service, and coordination claims.
- Use `A.13` for the performer basis, then `A.15.1` for actual Work; use `A.2.1` for assignments. Support each claim needed by the receiving decision.
- `OCE.5` governs organization-position identity and descriptions; `OCE.6` governs holder assignments and enabling relations. Until their needed result is available, record the missing position-establishment or identity basis rather than inferring a position.
- `B.1.5.EW` explains constituent/encompassing performance when needed; `OCE.10:4.1–4.3` supplies the participation-gap inquiry; `C.11.DUA` appraises additional inquiry when its worth is unresolved.
- `OCE.3` consumes the grounded Work and direct-relation account. `OCE.11` consumes it for change/continuing-Work coexistence.

### OCE.2:End

## OCE.3 - Generate and Compare Organization Concepts

> **Type:** Method pattern
> **Status:** Eternal alpha
>
> **Primary working result:** a **bounded organization-concept comparison** stating how alternatives differ in contribution, Work, assignment eligibility, authority, resource access, information use, service, coordination, capability, provider involvement, coexistence and burden; which participant contributions or missing voices matter; the decision or honest stop; and evidence that reopens the comparison.

### OCE.3:0 - Use This When

Use this pattern when one incumbent arrangement, target operating model, topology, reporting-line change, centralization/decentralization slogan, or provider proposal is being treated as inevitable. Enter when the organization and intended contribution are bounded and enough current Work and relation evidence exists to generate serious alternatives.

Begin with a compatible `OCE.1` focus and `OCE.2` current account or equivalent content. State which gaps are tolerated and which block comparison.

The first useful result is a small decision set of materially different possible organization concepts. Describe each concept with its assumptions, participant input, supporting evidence, trade-offs and authority conditions. A rejected concept remains useful when it exposes a hidden contribution or burden.

Do not use OCE.3 to realize the proposed configuration, establish a position, assign holders, establish capability, authorize change Work, or prove adoption or effectiveness. Send selected design questions to `OCE.4`–`OCE.8` and realization to `OCE.9`.

#### OCE.3:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| organization concept | A possible organization configuration described far enough to answer one decision. Its Work and relations remain possible until realized and observed. |
| concept alternative | A materially different way to satisfy or revise the intended contribution, including repairing the incumbent configuration. |
| selected structure | Constituents and relations selected for a comparison use, such as contribution, Work, assignment, authority, resource-access, information-use, service, coordination, or capability structure. |
| view | A description produced under a viewpoint. Project, process and case viewpoints ask different questions; charts, maps or models can present the resulting descriptions. |
| bounded generation move | The OCE.3 move that varies decision-bearing relations through incumbent repair, changed specialization/contribution/authority, and boundary/provider or human–AI alternatives, then stops at a small serious set. |
| participant contribution | Evidence or a proposed alternative supplied by people or other Agents whose knowledge of actual Work, burden, authority, safety, service or providers can change the set or comparison. Participation is not consensus or veto. |
| concept assumption | A claim that must hold for feasibility or worth but is not established. |
| coexistence and change burden | The demands and risks of changing while continuing Work shares the same conditions. These include learning and migration effort, provider and governance demands, service interruption, opportunity costs, and the effort or risk of reversal. |
| organization-concept comparison | Alternatives, criteria, evidence, uncertainty, consequences, decision or stop, and reopen conditions. It is not a target organization by itself. |

### OCE.3:1 - Problem Frame

Organization concepts arrive with persuasive forms. Charts foreground reporting; team topologies interaction; provider proposals service boundaries; process views recurring contributions. Each can expose a question, but none contains every authority, capability, resource, contribution, or consequence relation.

Concept generation must vary decision-bearing relations rather than redraw one configuration. It must include incumbent repair and obtain design knowledge from participants whose Work or burden is otherwise hidden.

### OCE.3:2 - Problem

A favored concept turns evidence collection into confirmation. Practitioners compare names instead of relations, infer capability from a proposed position, infer authority from hierarchy, and hide the burden of continuing service.

Several diagrams may still be views of one concept. Without a serious alternative and participant contribution, the decision cannot expose which assumption makes the preferred concept better.

### OCE.3:3 - Forces

| Force | Tension |
| --- | --- |
| Diversity | Serious alternatives reveal assumptions, while decorative variants waste attention. |
| Comparability | Shared concerns aid comparison, while concepts allocate contributions and burden through unlike structures. |
| Participation | Actual Work knowledge can change alternatives, while participation can be burdensome, unsafe, or outside authority. |
| Novelty and continuity | New relations may unlock capability, while incumbent relations carry memory, authority, and service continuity. |
| Product/organization alignment | Mirroring can reduce some coordination, while one-to-one correspondence is contingent. |
| Decision speed | A bounded selection is useful, while scalar scores create false precision. |

### OCE.3:4 - Solution

Generate a small decision set by changing the relations that matter to the contribution. Begin from the incumbent and current relation account; vary specialization, supplied-result, authority, assignment, access, coordination, provider, and human–AI relations; include affected participants whose knowledge can change a candidate; and stop when the set contains serious alternatives that challenge the favored concept's assumptions, or a generation gap is explicit.

Use `C.17` only after candidates exist, and only for novelty, diversity, value, or comparison characteristics actually judged. Use `C.18` only when retained or open-ended exploration -- including its Archive, Front, descriptors, telemetry or lineage -- is part of the working question. Use `C.11` or another applicable decision Method after alternatives, non-negotiables, uncertainty, and authority are explicit.

#### OCE.3:4.1 - Pattern-Use Unfolding

1. **Bind the comparison.** Name organization, contribution, decision authority, horizon, current account, non-negotiables, and tolerated or blocking gaps.
2. **Explain the difficulty before choosing a form.** From OCE.2, state which needed contribution is delayed, unusable, missing or unnecessarily burdensome, under which conditions, and which explanations remain possible. Name the relations that a change could affect. Preserve the product/service, authority, protection and continuing-work conditions against which a candidate must be compared.
3. **Choose bounded participants.** Invite or otherwise obtain contributions from participants whose knowledge of actual Work, burden, local adaptation, authority, safety, service or providers can alter the candidate set or comparison. Record missing participation and protection limits; preserve decision authority separately.
4. **Construct combinations from that difficulty.** Use §4.1.1 to connect contribution, specialization and allocation with the information, decisions, participation and support that would make each candidate work. Include incumbent-plus-repair; a changed specialization, contribution or authority configuration; and a boundary/provider or human–AI alternative when plausible. Explain why each combination could change the difficulty and what could defeat it. Stop generation when another variant changes no live assumption or criterion, or record the unmet generation need.
5. **Decide whether retained exploration is current.** For a one-time small decision set, proceed without Archive/Front apparatus. Use `C.18` only for retained or open-ended exploration; use `C.17` only to characterize candidates already present.
6. **Describe the whole candidate at the needed grain.** Use C.32:4 for the candidate palette, with the organization-specific reasons developed below. Name the selected structures, changed relations, expected gain and loss. Use charts, maps, scenarios, prototypes or mathematical lenses for the question each can answer and state their losses.
7. **Expose feasibility assumptions.** State required capabilities, effective authority, resource access, provider commitments, product/service claims, participation conditions and continuing-service constraints. Use the direct suppliers in §4.1.2 for a still-missing combination, replacement or coexistence result.
8. **Compare contributions, interactions and burdens.** Follow §4.1.2 through a condition that can defeat the proposed mechanism. Retain useful parts, revise the combination or reject it. Compare intended contribution, coordination, resilience, affected-System consequences, participant burden, service interruption, reversibility and uncertainty without hiding unlike outcomes in a score.
9. **Choose, narrow, probe, or stop.** Select under named authority, retain ties, or request the specialist result that changes the comparison. Selection does not establish organization relations.
10. **Return constraints and reopen evidence.** Supply the selected questions and assumptions to downstream patterns and name observations that reopen them.

##### OCE.3:4.1.1 - Derive an organizational combination

Begin with a short explanation of the work: the receiver needs a particular result under certain conditions; current contributors attempt to obtain it in a known way; a recovered difficulty prevents or burdens that contribution. Keep an explanation that remains uncertain as a hypothesis. If the difficulty is merely a missing permission or an isolated execution error, repairing that condition may be the serious incumbent option. Larger regrouping needs a reason that the local repair leaves unanswered.

**Find the contribution that must change.** Follow the receiving result back through the necessary subject work, using `B.1.5.EW` if its constituent connections are unclear. Obtain the relevant professional explanation when “prepare evidence”, “support users” or another label conceals work the designer does not understand. Identify where the current way creates delay, repeated interpretation, loss of information, incompatible demands or another supported difficulty. This yields a concrete design question, such as how Electrical's changing compatibility evidence can reach package assembly early enough, rather than an instruction to become more cross-functional.

**Give a reason for grouping and allocation together.** Use the specialization reasons and contribution-crossing specification in `OCE.4:4.0–4.1` to develop the candidate. Close, frequent mutual adjustment can favor bringing contributors together around a result. Scarce expertise, shared equipment, professional development or independent judgement can favor retaining a specialization and improving its contribution to several receivers. Compare those reasons in this case. Name who would supply each needed result, who would receive it, and how an unusable result returns. A proposed group with an unfilled contribution remains incomplete. C.32:4 supplies functional allocation, retargeting and bearer-feasibility repairs when needed. The draft concept can be refined through OCE.4; a full contribution-architecture decision need not precede generating it.

**Make information and decisions fit that allocation.** Ask what each deciding participant would need to know, when it would arrive and who could respond to an exception. If knowledge stays distributed, alternatives include supplying it to an integrator, enabling local decisions under compatible conditions, or changing the work so that fewer decisions need joint information. Choose a candidate reason, not a universal preference for centralization. Keep safety acceptance, release, resource allocation and other independently governed decisions separate where their bases require it. Grouping people together does not change those bases. Use `OCE.7` and `C.32.CONWAY` when product/service and organization choices constrain one another; retain a justified mismatch.

**Make participation and support fit the expected contribution.** Ask which accepted work a contributor would have to interrupt, which local success criterion the contribution might conflict with, and what access, capability, response or protection it requires. Obtain OCE.10's account when a participation difficulty needs explanation. Use that result to change the candidate: for example, pair an earlier evidence-return obligation with an accepted allocation and recognition of useful challenge, rather than expecting extra hidden work. The relevant owner must establish any changed condition. Required capability may be supplied by an existing contributor, development or another arrangement; it is not supplied by naming the group. OCE.11 provides the shared service/change conditions when the same people or support would be occupied.

**State the mechanism of the combination.** Explain how the changes would affect the recovered difficulty: “earlier electrical input lets Integration detect an incompatible claim before assembly closes; a reserved response interval lets Electrical correct it; separate Safety acceptance preserves the required judgement.” Name the expected observable difference and a condition under which it would not appear. This explanation shows which parts depend on one another and gives the comparison something to challenge. It remains a proposed mechanism; the attractive configuration and its eventual causal effect are different claims.

Generate another serious combination by changing a consequential premise of that mechanism. Retaining specialists with a reliable crossing, grouping recurring contributors around a receiving result, and obtaining a contribution from a provider can respond differently to scarcity or delay. A provider/AI branch is useful only when a plausible supplied contribution exists; OCE.8 develops the complete work arrangement. A cosmetic reporting change that leaves the causal difficulty and relevant relations untouched adds no alternative.

##### OCE.3:4.1.2 - Challenge the combination and change it

Bring each candidate's prospective result path and assumptions to the general method that answers the unresolved question. `C.30.ASV:4.5a` distinguishes Method composition, work, information, support and other structures when that distinction changes the design; `C.32.MWA:4.1–4.4` combines those accounts and exposes conflict or burden moved between them. Enter MWA with a prospective case for a proposed organization of Method use. Existing observed relations keep their own evidence; missing Work identity does not become an invented obtaining occurrence.

For the finite change from the incumbent to a candidate, use `C.11.CRC:4` to compare effects under the same horizon, scenarios and protected conditions, including interactions. Use `B.1.5.RS:4` when replacing a contribution: follow it through every receiving whole that can change the choice, including an adapter or fallback the replacement needs. Reuse a sufficient comparison. OCE.11:4.1–4.3 supplies the time and resource overlap with continuing service; the concept uses those conditions instead of constructing another capacity account.

The organization question supplied to these methods is whether the proposed specialization, allocation, decisions, information and participation can jointly deliver the contribution. For example, a common integration queue may reduce duplicated interpretation yet delay local corrections. Keeping local output targets while adding a shared evidence obligation may make the apparently available contributors unavailable in practice. Such an interaction gives a reason to change a relation or support condition, retain a bounded exception, reduce the demand, or reject the candidate. A compensating policy is part of the candidate, with its burden and authority conditions, rather than a free remedy added after comparison.

Retain an incumbent repair when it satisfies the needed result at acceptable burden. Retain a tie when the observations do not distinguish the serious configurations. Request only the next result that could change the choice, and return a specific feasibility or authority gap when no candidate can meet the current conditions. Concept comparison can finish with that honest stop; it does not require a workshop, organization-wide agreement or an experiment for every alternative.

#### OCE.3:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| comparison boundary | Organization, contribution, decision, authority, horizon, non-negotiables, and tolerated/blocked gaps. |
| generation account | Difficulty and surviving explanations; reasons for each combination and its proposed mechanism; changed relations, adverse interaction and revision/rejection; generation stop and any conditional `C.18` use. |
| participant contribution | Participants sought, contribution used, missing voice, protection/burden limit, and effect on alternatives or comparison. |
| concept structures | Possible supplied-result, Work, eligibility/assignment, authority, access, information-use, service, coordination, capability, and provider relations. |
| assumptions | Capability, authority, access, commitment, product/service, participation, and service-continuity claims with status. |
| comparison | Contribution, coordination, resilience, affected Systems, participation, coexistence, burden, reversibility, and uncertainty. |
| specialist returns | Needed result, owning practice, scope, and effect on the comparison. |
| decision or stop | Selection, narrowed question, probe, or stop; basis, alternatives, ties, and authority. |
| continuation | Downstream constraints and evidence that reopens the comparison. |

#### OCE.3:4.3 - What Changes in Practice

Teams compare possible organization relations rather than fashionable names. The incumbent can be repaired, product and organization structures can differ deliberately, participants can change the alternatives without receiving an automatic veto, and provider or AI contributions can be designed without pretending that outsourcing or automation supplies authority, capability, or results.

### OCE.3:5 - Archetypal Grounding -- PumpWorks Concepts

The comparison uses `PumpWorks-EngineeringOrg`, weekly evidenced AI-inspection releases, the `OCE.2` account, and non-negotiable safety authority, evidence traceability, and continuing service.

Product, Electrical, Software, Safety, Field Service, platform, provider, and service-liaison participants contribute knowledge of actual Work, scarcity, burden, authority, exceptions and provider conditions. Missing customer-use evidence remains visible; participation does not transfer the release decision.

**Derive the repair from the current difficulty.** OCE.2's R42 reconstruction shows that Electrical's evidence is used during package challenge, that a planned rig interval can be displaced by service, and that field-service information can arrive too late. The cause of the last delay remains unresolved. The design therefore starts with timely usable evidence and a working exception return. It cannot yet justify a blanket claim that departments cause the delay.

For `OC-PW-FUNCTIONAL-REPAIR`, keep specialist contribution in Electrical and assembly in Integration. Use OCE.4's crossing to specify which configuration the evidence concerns, when Integration needs it and how a challenged claim returns. Pair that contribution with a prospective rig-access arrangement and a known escalation path for missed information. Safety still accepts evidence; the director still decides release. The mechanism hypothesis is that an explicit earlier request and response can remove avoidable coordination delay while preserving expertise and independent judgement. This candidate is serious even if no reporting line changes. Its limit is that a crossing agreement cannot create an unavailable expert or rig interval.

**Construct and challenge a different combination.** If frequent mutual correction is the unresolved pressure, propose a stable release integration group with recurring Electrical and Software contributions and platform support. This is the reason for the stream/enabling candidate: participants can resolve a changing compatibility question in the same working interval. It does not require moving independent Safety into the group's release authority or abandoning functional capability homes.

Suppose the bounded participant discussion now adds that Electrical is judged on its own completed design tasks and that its specialist also covers service diagnostics. The service owner confirms that the proposed response interval is already committed to protected diagnostics and no substitute is available. Moving evidence preparation into a common queue while retaining that commitment defeats the assumed response interval; the local output criterion creates a further participation question. The group could improve package assembly while leaving Electrical's answers later or displacing protected service. Apply MWA to expose this conflict and OCE.11 to obtain the service/participation conditions; the unrepaired stream candidate is rejected for this use.

A revised candidate would pair the recurring group with a different specialist response interval under qualified service coverage, recognition of the cross-group contribution by the relevant manager, and a fallback to the existing exception route when service interrupts. These changes still need the relevant owners' decisions and effective conditions. Its extra coordination, setup and displaced work belong in the CRC comparison. If the service owner cannot supply the required coverage, narrow the release demand or keep the functional repair; a nominal allocation cannot make the revised candidate feasible. RS governs any proposed replacement of the old evidence-return contribution, including its other service users. OCE.10 is used only if the participation explanation still changes the intervention.

The provider-hybrid candidate changes another premise: an outside contributor might supply model-operation and evidence-preparation work. OCE.8 must develop its receiving use, exception, access and recovery conditions. The missing provider commitment and acceptance basis keep its capacity gain hypothetical. The resulting comparison can now use the following compact descriptions.

| Concept | Possible relation changes | Main promise | Main burden and uncertainty |
| --- | --- | --- | --- |
| `OC-PW-FUNCTIONAL-REPAIR` | Retain functional assignments; establish named electrical-evidence supply and use, safety acceptance, release decision, rig-access priority, and field-service information-return relations | Preserves specialist depth, current authority, and low migration burden | Coordination load may remain high; weekly recurrence is unproved |
| `OC-PW-STREAM-ENABLING` | Combine recurring release integration with specialist response intervals, compatible contribution recognition, independent Safety and platform support; retain functional capability homes and an exception fallback | Could shorten mutual correction by making the required contributors available together | Depends on accepted allocation and service coverage; unrepaired double commitment rejects the candidate, and the compensation adds burden |
| `OC-PW-PROVIDER-HYBRID` | Expand provider model-operation and evidence-preparation contributions while PumpWorks retains safety, release, exception, recovery, and service decisions | May increase specialist capacity | Commitment, access, assurance, recovery, knowledge retention, and authority remain unresolved |

A chart view can show possible position descriptions; a process view recurring release contributions; a case view one release’s evidence and next decision; and a project view transition commitments and conflicts. These are views of possible or actual Work and relations, not four concepts.

The small set needs no Archive or Front. `C.17` may characterize diversity or novelty after the three concepts exist. If later exploration retains many variants and lineage across decisions, that new use can invoke `C.18`.

If the authorized decision-maker must decide before provider and capacity evidence arrives, the honest result is a narrowed choice between functional repair and stream/enabling plus named probes. Selection supplies design constraints; realization and observation must establish the proposed configuration.

**Change the setting and the available evidence.** In a member-governed standards association, the comparable difficulty may be late cross-language evidence in an amendment packet. Missing volunteer activity logs leave the source of delay uncertain, but permitted packet revisions and two contributor accounts show repeated requests for clarification. Retaining language specialists with an explicit clarification return is an incumbent repair. A shared editorial group is another candidate only if volunteers can contribute in compatible windows and the relevant body can establish the proposed arrangement. Suppose the bylaws reserve acceptance to voting members. Giving that decision to a paid coordinator would violate the authority condition; concentrating clarification in one language could also suppress other language groups' concerns. Retain those decisions, compare a bounded editorial contribution with the distributed repair, and carry the unresolved delay explanation forward. The same constructive reasoning yields different arrangements because authority, participation and receiving use differ.

### OCE.3:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| topology prestige | A fashionable form becomes the only serious concept. | Generate alternatives by changing named relations, including incumbent repair. |
| diagram diversity | Several views count as several concepts. | Compare underlying possible relations. |
| expert-only design | Designer knowledge excludes actual Work and burden. | Obtain bounded participant contributions and record missing voices. |
| mirroring determinism | Product architecture dictates organization structure one-for-one. | Test named correspondences and deliberate non-mirroring. |
| resource invisibility | A concept moves scarce capability or burden without showing it. | Compare participants, resource windows, and transferred burden. |
| selection-as-reality | The chosen concept is reported as the new organization. | Preserve possible status until realization and observation. |

### OCE.3:7 - Conformance Checklist

- [ ] The comparison has a compatible focus and grounded current account or explicit blocking gaps.
- [ ] Comparison dimensions distinguish proposed relations, arrangements, capability, coexistence conditions and burden before forms are chosen.
- [ ] Participants whose Work or burden can change the alternatives contribute under bounded protection and authority.
- [ ] The set contains materially different combinations and an incumbent-repair branch, with a reason linking each to the recovered difficulty.
- [ ] Each serious combination has a mechanism hypothesis; a consequential interaction has been examined and its compensation, limit or rejection is visible.
- [ ] `C.17` characterizes existing candidates; `C.18` appears only when retained or open-ended exploration is current.
- [ ] Each concept names possible direct relations; views remain descriptions.
- [ ] Capability, authority, access, provider commitment, and continuity assumptions remain explicit.
- [ ] The decision does not convert selection into an obtaining organization.
- [ ] Downstream constraints and reopen evidence are explicit.

### OCE.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Choose between functional, matrix, and product.” | Name the contribution, authority, access, service, coordination, capability, and burden relations that differ. |
| “Team Topologies is the target architecture.” | Use its concepts for one candidate and compare unlike alternatives. |
| “Organization should mirror product architecture.” | State the proposed correspondence and test exceptions and burden. |
| “The provider owns the AI part.” | Recover contribution, commitment, access, assurance, recovery, responsibility, and authority separately. |
| “The workshop generated options, so participation is covered.” | Show whose knowledge changed which alternative and whose absence remains material. |
| “The highest weighted score wins.” | Preserve non-negotiables, uncertainty, incompatible measures, and authority. |

### OCE.3:9 - Consequences

A target organization is no longer a picture selected by familiarity. Practitioners obtain alternatives with visible participant knowledge, feasibility, consequences, and transition burden.

The cost is that a favored concept can remain unresolved. More evidence or a smaller probe may be required before selection.

### OCE.3:10 - Rationale

Organization concepts are possible relation structures for a named contribution. Several views can help, but the decision turns on relations and consequences. A bounded domain generation move avoids importing open-ended search apparatus into every design while keeping that option available when retained exploration is real.

### OCE.3:11 - SoTA-Echoing

**Practice question.** How can a practitioner construct a small set of coherent organization alternatives from a needed contribution and a recovered difficulty? The selected answer is the domain synthesis in OCE.3:4.1.1: derive a reason for specialization and allocation, connect it to information and decisions, make participation and support compatible with the expected work, and state how the combination could change the difficulty. OCE.3:4.1.2 uses the existing C.32, MWA, CRC, RS and OCE suppliers for synthesis, interactions, replacement and continuing-service conditions. This connection is an authored answer; it is not a new generic architecture or comparison method.

| Serious alternative at comparable effort | Selection, source use and accepted trade-off | Exact consequence in this pattern |
| --- | --- | --- |
| Galbraith's [Star Model](https://jaygalbraith.com/wp-content/uploads/2024/03/StarModel.pdf), especially its policy-fit and Overcoming Negatives Through Design explanation, develops a configuration by relating strategy, structure, processes, rewards and people. Compare two or three bounded candidates with the same participant access and available evidence, not a whole-company exercise against an OCE note. | **Adopt** constructing policies together and compensating a structure's adverse effects. **Adapt** the management-policy framing to separately held authority, outside providers and supported current/prospective relations. A sufficient Star-Model design remains usable. OCE's selected connection adds explicit reconstruction of which contribution each choice serves and which conditions are still missing. Its cost is more explanation and returns to the supplying methods; no measured general superiority is claimed. The historical text's current hosting date supplies no newer validation. | OCE.3:4.1.1 connects allocation, decisions, participation and support; :4.1.2 makes compensation part of the compared candidate. In :5, the initial integration group fails on the protected service interval, while the revised combination needs a different qualified interval and recognition of its contribution. |
| The current [Team Topologies public concepts](https://teamtopologies.com/key-concepts) offer stream alignment, enabling and platform contributions, specialist subsystems, explicit interaction modes and cognitive-load limits. This is a developed conditional rival for a team-of-teams flow problem, not merely a chart label. | **Adopt** team interaction and cognitive-load questions; **adapt** them as candidates when the organization's result is obtained through those team relations. Compare on the same result and burden. The broader OCE synthesis is selected when independent acceptance, service obligations, provider boundaries or another receiving whole changes the design. **Reject** making the public catalogue exhaustive for that wider question. The comparison uses the available official explanation, not a claimed full reading or validation of either book edition. | OCE.3:4.1, steps 3–4, and :4.1.1 preserve a serious stream/enabling branch, incumbent repair and a conditional provider branch. OCE.3:5 retains functional capability homes and independent Safety, and its association variation changes the grouping and decision combination. |

[Joseph and Sengul's 2024 online/2025 issue review](https://doi.org/10.1177/01492063241271242) strengthens the comparison beyond a single favored form: configuration, control, attention/information and coordination expose different dependencies. **Adapt** its internal/external-fit and decision-context questions in OCE.3:4.1.1's mechanism explanation and :4.1.2's interaction question. The review is a current synthesis informing the candidate, not a recipe or evidence that the PumpWorks design works. OCE.3:5 therefore separates the proposed gain, the known conflicting commitment and the still-unqualified compensation.

[Heusinkveld and Smits (2025)](https://doi.org/10.1007/s41469-024-00176-y) distinguishes perspectives on the development and translation of organization-design knowledge. **Adopt** that challenge to choosing by popularity in OCE.3:2 and :6; source uptake does not decide local worth. The accessible abstract of [Schulze-Meeßen and Hamborg (2023)](https://doi.org/10.1016/j.apergo.2023.104012) supports using participant-facing representations as an aid to recognition and acceptance. **Adapt** that limited contribution in :4.1, steps 3 and 6. The full experimental method and results are not relied on here; improved representation does not establish the organization relations, capability or effectiveness excluded by :0.

Reopen when a recurring contribution cannot be constructed through these branches, a serious alternative supplies the same usable combination at lower total effort, a participant reveals an omitted interaction, or realization defeats the stated mechanism or protected condition. A new source changes this selection only through such a substantive difference.

### OCE.3:12 - Relations

- `OCE.1` supplies organization, contribution, authority boundary, and affected-System scope. `OCE.2` supplies actual Work, direct relation evidence, and gaps.
- OCE.3 supplies bounded organization-concept generation. `C.17` characterizes candidates already present; `C.18` governs retained/open-ended exploration only when current; `C.11` governs bounded choice.
- `A.22` governs selected structures; `C.32:4` supplies architecture synthesis. `C.30.ASV:4.5a` selects Method/use structures and `C.32.MWA:4.1–4.4` synthesizes them when conflict or moved burden matters. `C.32.CONWAY` and `OCE.7` govern the paired-architecture question.
- `C.11.CRC:4` supplies the finite configuration comparison; `B.1.5.RS:4` supplies replacement by receiving use. `OCE.4:4.0–4.1`, `OCE.10:4.1–4.3` and `OCE.11:4.1–4.3` supply contribution-boundary, participation and coexistence results at the points of need.
- `OCE.4`, `OCE.5`, `OCE.7`, and `OCE.8` consume selected constraints for specialization, positions, product/service alignment, and human–AI/provider configurations. `OCE.11` consumes current and possible relations for coexistence.
- Use `OCE.9` to realize the selected concept; identify performed Work and changed organization relations from their evidence.

### OCE.3:End

# Part II - Design Organization Relations and Work Arrangements

## OCE.4 - Design an Organization's Contribution Architecture

> **Type:** Method pattern
> **Status:** Eternal alpha
>
> **Primary working result:** an **inspectable contribution-architecture design**: a decision and possible-future description recording selected specialization boundaries, contribution-relation specifications, acceptance and exception conditions, affected burdens, receiving decisions, and the evidence needed to establish which direct relations later obtain.

### OCE.4:0 - Use This When

Use this pattern when an organization concept has been selected or narrowed, but its chart, topology, or operating-model label still does not say how contributions reach their receivers. Enter when specialization boundaries, supplied results, information use, decisions, services, resource access, or coordination must be designed before positions or assignments can be settled.

Begin with a compatible `OCE.1` focus, `OCE.2` current account, and `OCE.3` concept comparison or equivalent content. Name any tolerated evidence gap and any gap that blocks design.

The first useful result is small: one organization concept, a few decision-bearing contribution-relation specifications, their intended suppliers and receivers, the selected specialization boundaries, and the conditions under which later Work may realize or reopen them.

Use `C.30` directly when the question is only whether one actual or candidate structure is architecture-relevant. Use `OCE.5` for position identity, `OCE.6` for holder assignments and enabling relations, `OCE.7` for paired product-or-service and organization architecture decisions, and `OCE.9` for realization and organization-capability evidence.

#### OCE.4:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| specialization boundary | A selected boundary between domains of organization contribution or Work for the current design use. Decide separately which organization units, positions, assignments, and authority relations are needed at that boundary. |
| contribution-relation specification | Possible-future design content naming an intended direct relation kind or predicate, supplier and receiver, result or preserved condition, applicability, acceptance or use condition, exception return, scope, horizon, and evidence need. The specified relation remains proposed until its obtaining conditions are met. |
| contribution relation occurrence | One obtaining occurrence of the admitted direct relation named by a specification or current account. Its predicate, participants, applicability, interval, and evidence must be recoverable independently of the design. |
| contribution structure | An actual `A.22` structure selecting obtaining contribution relation occurrences and their participants for one declared use. Describe a candidate contribution structure as possible-future content until the selected occurrences obtain. Information-use, decision, access, service, coordination, legal-entity, and Work structures can remain separate. |
| contribution architecture | The way selected structures organize the named organization for its intended contribution, qualified under `C.30`. Actual architecture requires the applicable subject relations and architecture relation to obtain; candidate or desired architecture remains claim or description content. |
| position-design need | A need to decide whether one or more expected contributions warrant a stable organization position. `OCE.5` makes that decision and, when warranted, defines the position. |
| acceptance condition | The condition under which a receiver can use or accept the supplied result for the named decision. State the condition in the specification or claim, then use the applicable predicate and evidence to test whether it is met. |
| exception and escalation relation | An obtaining direct relation for returning an unusable result, resolving a conflict, or issuing a decision when ordinary contribution cannot continue. Specify that relation explicitly when designing a possible future. |
| contribution-architecture decision | A decision selecting possible-future organization structures, relation specifications, constraints, and open refinements for later change Work. It does not make those structures or relations actual. |

### OCE.4:1 - Problem Frame

Organization design often begins with grouping: functions, products, customers, regions, programmes, professions, or platforms. Grouping helps attention, yet the organization contributes through relations that cross those groups. Evidence is supplied and used, decisions are issued and accepted, materials move, services are provided, resources are accessed, and exceptions return.

A contribution-architecture description makes intended relation specifications, any obtaining occurrences, and their receiving decisions visible while distinguishing proposed from actual relations. It may use several structures because activity grouping, decision representation, legal entities, information use, and service provision answer different questions. The design can then state which boundaries should change and which cross-boundary contributions must remain.

### OCE.4:2 - Problem

A target chart can move boxes while preserving the failed contribution path. A topology can give every group a familiar label while leaving the result, receiver, acceptance condition, or exception owner unknown. A generic “interface” can hide that one boundary carries evidence supply, a separate release decision, resource access, provider service, and field information.

The design then cannot guide position definition or realization. Teams infer authority from placement, capability from staffing, and acceptance from handoff. When problems appear, nobody can tell whether the missing element is Work, an assignment, access, an authority relation, a contribution predicate, or evidence that the relation obtains.

### OCE.4:3 - Forces

| Force | Tension |
| --- | --- |
| Specialization | Concentrated knowledge and equipment can improve contribution, while every boundary creates coordination and return needs. |
| Stable ownership | Receivers need reliable contribution, while fixed boxes can preserve obsolete Work and authority assumptions. |
| Several structures | One picture is easy to communicate, while contribution, decision, access, service, legal, and Work structures need not coincide. |
| Participant knowledge | People performing Work and using its results can expose hidden relations, while participation does not transfer design authority. |
| Provider boundaries | External provision can add capability and scale, while contracts, access, recovery, evidence, and decision authority remain separate. |
| Realization | Designers need a usable possible-future account now; later Work may realize the relations, and observations can support claims that they obtain. |

### OCE.4:4 - Solution

Design from the intended contribution and the relations needed to produce, use, accept, and return results. Select the few structures that change the current decision. State possible-future crossings as contribution-relation specifications, then make a contribution-architecture decision that fixes only the boundaries and conditions later Work must realize.

Recognition is cheap: one selected organization concept whose result path cannot be stated from supplier to receiving decision is enough to enter. Assurance is relation-specific: each actual contribution, information-use, decision, service, access, material-transfer, or coordination claim needs its own predicate, participants, scope, window, and evidence.

First inspect an existing coordination model, if one is available. A competent transaction account may already explain who requests a result, who commits to supply it, what is produced and declared ready, and how the receiver accepts or returns it. Reuse that account when the specialization boundaries and other enabling conditions can stay fixed. Broaden the design when changing a boundary could alter access, decision independence, support or another receiving contribution. Compare those effects with the people who provide and receive them; add only the structures needed to settle the choice. Also ask whether the policies supporting the exchange fit together. For example, participants may report that early mismatch returns are penalized while nominal completion is rewarded. Compare a change to that recognition policy with moving the boundary; the policy owner must decide the change, and later use must test the expected improvement. Reuse the compatible policy and participant results from `OCE.3`. Section 11 explains this choice against transaction modeling and interacting organization-design policies.

#### OCE.4:4.0 - One bounded first design

For a small first use, keep the selected concept and already qualified constraints fixed and resolve one troublesome contribution crossing. Suppose a small engineering organization has the authority and participant inputs needed to decide how compatibility evidence reaches its release integrator. A short design note can state:

> Electrical supplies a configuration-C7 compatibility-evidence package to Integration for Friday's review. Each claimed interface must have a traceable source and test; Integration returns an unsupported claim to Electrical before evidence closure. The design decision keeps electrical expertise with Electrical and package assembly with Integration, using the agreed review time rather than merging the two specializations. Safety acceptance and release remain separate decisions. A missing source or an unworkable review burden reopens this design. Use the first package to test whether the planned supply and exception return actually work.

This is one bounded design result, not evidence that the supply relation already obtains. Reuse the supporting focus, current account, participant correction and decision basis instead of restating them. Add another structure, alternative or specialist return when it can change this decision; a missing authority or protection premise remains a blocker. The same short note can carry the needed content listed below. Elaborate the questions that remain open rather than turning this first use into a full-organization redesign.

#### OCE.4:4.1 - Pattern-Use Unfolding

1. **Bind the design question.** Name the organization, intended outside contribution, selected concept, decision subject, authority, horizon, affected Systems, and first receiving use of the result.
2. **Recover the current relation basis.** Carry forward current Work and direct-relation evidence from `OCE.2`, plus constraints, participants, assumptions, and burdens from `OCE.3`. Record unavailable or incompatible inputs explicitly.
3. **Select structures by question.** Choose contribution, Work, decision, information-use, material-transfer, service, access, coordination, legal-entity, or other structures only when each changes the design. Use process, project, and case viewpoints on the same Work to expose different Method, coordination, state, and authority constraints. Retain the account of obtaining occurrences unless new evidence warrants revision; keep proposed structures and crossings modal. Preserve differences among the selected structures when those differences matter to the decision.
4. **Set specialization boundaries.** Group contribution or Work where shared knowledge, equipment, evidence, decision, locality, customer, product, service, or provider conditions justify it. State the condition and the burden moved by each boundary.
5. **Write contribution-relation specifications.** For every decision-bearing crossing, name the intended direct relation kind or predicate, supplier and receiver Systems, result or preserved condition, applicability, acceptance or use condition, exception return, scope, horizon, and evidence need. Use “interface” only as an orientation label after this content is visible. Do not report an occurrence before its predicate is satisfied. Where participants must negotiate a contribution, distinguish a request, the accepted commitment, production of the result, its declaration and receiving acceptance. Use `OCE.12:4.3.1` for the cooperation that obtains agreed terms and `OPS.13` when a promise must be established or changed. A changed request or withdrawn support returns to the affected participants; it does not silently change their existing commitments.
6. **Obtain participant corrections.** Use participant-facing views to test actual Work, burden, accessibility, safety, provider, and service-continuity assumptions. Record whose contribution changed the design and which material voice is missing.
7. **Compare whole structures.** Compare how each candidate handles intended contribution, coordination load, decision latency, evidence, scarce capability, resilience, provider dependence, affected Systems, reversibility, and change burden. Keep unlike characteristics separate unless a justified aggregation Method exists. Include a repair that retains the present specialization and improves its coordination. Compare total effort: recovering the existing model, participant inquiry, making the decision, establishing changed relations, maintaining descriptions and handling exceptions. A more detailed model earns its cost only through a decision or receiving use that needs it.
8. **Make the architecture decision.** Use `C.32.PAD`, `C.11`, or the applicable decision pattern for the claim being made. State selected structures, accepted losses, fixed constraints, open refinements, rejected alternatives, and reopen observations. Preserve modal status.
9. **Return position and paired-architecture questions.** Send stable expected-contribution and eligibility needs to `OCE.5`. Send organization/product-or-service correspondence pressure to `OCE.7`. Keep holder, authority, capability, and realization questions with their owners.
10. **Specify realization evidence.** Name which later Work and observations can show that each specified relation obtains, fails, or remains unresolved. Supply design constraints to `OCE.9` without reporting organization capability.
11. **Stop at contribution sufficiency.** Return when affected practitioners can name the contribution path, boundaries, contribution-relation specifications, accepted burdens, open refinements, and observations that reopen the design.

The steps are a reasoning aid. Existing structures may be repaired, new boundaries may be tried, and participant evidence may reopen an earlier decision at any time.

#### OCE.4:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| design boundary | Organization, contribution, concept, authority, horizon, first receiver, and affected Systems. |
| selected structures | Structure kind, constituents, occurrence refs when actual, modal structure or relation claims when proposed, declared use, and known losses. |
| specialization decisions | Boundary, reason, expected gain, burden moved, retained cross-boundary contribution, and open refinement. |
| contribution-relation specifications | Intended direct relation kind or predicate, supplier, receiver, result or preserved condition, applicability, acceptance/use, exception return, scope, horizon, and evidence need; occurrence ref only when independently established. |
| participant corrections | Participants sought, design change made, missing voice, burden or protection limit, and unresolved claim. |
| architecture decision | Selected option, fixed constraints, accepted losses, rejected or retained alternatives, modal or actual status, and decision basis. |
| downstream returns | Position needs, paired product/service questions, realization constraints, specialist results, and missing governors. |
| continuation | Realization observations, evidence windows, and the smallest event that reopens the decision. |

#### OCE.4:4.3 - What Changes in Practice

Practitioners design the contribution path before finalizing boxes. Every stable boundary has a reason, every decision-bearing crossing has an explicit relation specification, and every target relation retains its modal status until its direct predicate is satisfied. Position, assignment, capability, authority, and provider questions remain available for their own decisions instead of being hidden in the chart.

### OCE.4:5 - Archetypal Grounding -- PumpWorks Contribution Architecture

PumpWorks continues from the `OC-PW-STREAM-ENABLING` concept. The current decision concerns weekly evidenced AI-inspection releases while field service continues. `PumpWorks-EngineeringOrg` is the organization; the proposed stream configuration and its relations remain possible-future content.

The selected design describes several proposed structures: contribution relations for supplying results to receiving decisions; decision relations that separate safety-evidence acceptance from release authorization; access relations for the test rig and model artifacts; provider-support service relations; and field-information relations for returning operating observations.

| Proposed crossing | Contribution-relation specification | Acceptance, exception, and evidence need |
| --- | --- | --- |
| Electrical → Release Integration | supply compatibility-evidence package for the named configuration | Integration can trace every claimed interface and test; unresolved mismatch returns to Electrical before evidence closure |
| Platform → Release Integration | provide qualified test environment and deployment service | Configuration and availability window match the release candidate; outage opens the fallback environment decision |
| AI provider → PumpWorks Integration | supply versioned model artifact and remote support under named access conditions | Provenance, compatibility, recovery, and access are present; provider supplies neither safety acceptance nor release authority |
| Release Integration → Safety | supply assembled evidence package and unresolved assumptions | Safety can evaluate the named release claim; rejection returns the exact missing or contradicted evidence |
| Safety → Release director | issue an evidence-acceptance result | Acceptance concerns the evidence question; the release director separately issues the release decision |
| Field Service → product and integration teams | provide incident and use-condition information | The report identifies product configuration and service episode; privacy and customer-use gaps return to their owners |

PumpWorks first considers a transaction-based repair of the Electrical–Integration exchange. Integration requests evidence for C7; Electrical can accept that request, produce the package and declare it ready; Integration checks the specified receiving conditions and accepts or returns it. This can fix an unclear handoff while keeping the two specializations. A team with an adequate existing model can reuse it without creating another account.

For the wider weekly-release decision, however, moving package assembly into Electrical would also change who challenges its claims and who needs the rig and provider support. PumpWorks therefore retains that transaction account and adds the separate decision, access and service questions represented above. It accepts the inquiry and maintenance cost of those additional views because the assembly-location choice cannot be settled from the evidence exchange alone. A competent transaction model extended with the same policy and resource answers would also be sufficient; redrawing its information in an OCE-specific format would add no gain. The design preserves independent Safety acceptance and compares the coordination burden of keeping Integration separate with the burden and conflicts a merger would introduce.

Now suppose the product team asks for C8 after Electrical has committed to C7. Electrical's declaration that the C7 package is ready does not answer the changed request. Integration returns the unmet C8 condition, and the affected participants consider a revised package and review time through `OCE.12:4.3.1`; the promise owner uses `OPS.13` for the resulting commitment change. The qualified C7 evidence remains useful for its own configuration. Rig access for the new interval and Safety's later acceptance still require their separate answers. This change refines one crossing; it need not reopen every specialization boundary unless the new burden makes the retained arrangement unworkable.

The design groups recurring release-integration contribution without dissolving Electrical, Safety, platform, provider, or field-service specialization. Its specifications return a position-design need for stable release-evidence integration to `OCE.5`, a holder/access question for `OCE.6`, and a product-module/organization-boundary question for `OCE.7`.

The table describes proposed relations. In later realization, use `OCE.9` to compare actual Work and independently evidenced relation occurrences with the design and determine whether a bounded organization-capability increment is supported.

#### OCE.4:5.1 - Transfer Probes

| Setting | Reusable move | Required return or changed content |
| --- | --- | --- |
| public-hospital emergency flow | Start from the patient-care contribution, separate clinical decision, diagnostic-information, transfer, access, escalation, and continuing-service structures | Use clinical rather than product-release terms; obtain statutory clinical-authority, labor, privacy, safety, bed-access, and Operations results from their owners |
| distributed standards association | Start from the standard-publication contribution, volunteer Work, editorial evidence, member decision, ballot, publication-service, and employer-resource relations | Use the association’s bylaws and elected authority; retain several employers, volunteer availability, publication, and finance conditions rather than assuming one employer hierarchy |

These are hypothetical transfer probes of the design move. Adoption and benefit would require evidence from actual use.

### OCE.4:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| chart completion | Every required contribution receives a box, so the design appears complete. | Trace direct results to receiving decisions and exception returns. |
| interface bundling | Several unlike relations become one line. | Name each direct predicate and use a visibly reduced orientation label only afterward. |
| symmetry preference | Similar product or customer groups receive identical organization units. | Preserve differences in Work, authority, evidence, capability, provider, and service conditions. |
| informal-relation erasure | Useful observed coordination disappears because policy does not name it. | Preserve the observed relation and decide whether to formalize, support, replace, or stop relying on it. |
| participation-as-approval | A workshop is treated as design authority or adoption. | Record the knowledge contribution and keep authority and realization separate. |
| future-as-current | The selected picture is called the new organization. | Keep possible relations in claim and decision content until direct evidence shows they obtain. |

### OCE.4:7 - Conformance Checklist

- [ ] The organization, contribution, concept, authority, horizon, and first receiving use are explicit.
- [ ] Each selected structure answers a declared question and states its losses.
- [ ] Specialization boundaries name their gain and moved burden.
- [ ] Every decision-bearing crossing has a contribution-relation specification naming the intended direct relation kind or predicate, supplier, receiver, result, conditions, acceptance/use, exception return, and evidence need.
- [ ] “Interface” does not replace direct relation content.
- [ ] Participant knowledge changes or challenges identifiable design content.
- [ ] Contribution-relation specifications, modal architecture claims, and obtaining relation occurrences remain distinguishable.
- [ ] Position, holder, assignment, capability, authority, product/service, and realization questions have explicit returns.
- [ ] The decision states fixed constraints, open refinements, accepted losses, and reopen observations.

### OCE.4:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Create product teams and define interfaces.” | Name the contribution and Work basis for each boundary, then write separate possible-future specifications for supplied-result, decision, information-use, access, service, and coordination relations. |
| “One owner per deliverable.” | Recover the result, receiver, acceptance decision, contributing Systems, authority, and exception path; choose an ownership predicate only when it is actually governed. |
| “Put everyone involved in one team.” | Select the smallest contribution-bearing boundaries and preserve scarce capability homes, independent acceptance, providers, and continuing service where they change the decision. |
| “The matrix has two reporting lines.” | State which contribution, decision, authority, access, or coordination relation each line is intended to represent. |
| “The architecture is now implemented.” | Compare actual Work and obtaining relations after change; retain the current item as decision and possible-future description until then. |

### OCE.4:9 - Consequences

The contribution-architecture design becomes inspectable before a chart is finalized. Position design can start from expected contributions, and realization can test independently obtaining relation occurrences against explicit specifications instead of visual conformity.

The cost is that one page may no longer contain the whole answer. Several structures and evidence returns may be needed, and an attractive topology can remain undecided when a provider, authority, access, safety, or service condition is missing.

### OCE.4:10 - Rationale

An organization contributes through actual Systems, Work, and direct relation occurrences. Design-time specifications preserve why a proposed boundary exists without asserting that the relation already obtains, so later evidence can show whether the intended architecture was realized.

Several structures are expected. The activity arrangement, decision representation, legal entities, information use, access, and service provision can overlap without becoming one structure. Their non-isomorphism can expose a design risk rather than a modeling defect.

### OCE.4:11 - SoTA-Echoing

#### OCE.4:11.1 - Current-Line Selection for Contribution Design

The question is how Electrical's compatibility evidence can reach Integration in a usable form, and whether the specialization that supports that exchange should change. Compare methods on that same crossing and release horizon, including investigation, participant time, implementation, exceptions and upkeep of the account.

| Competent answer | What it supplies and when it is sufficient | Choice made here |
| --- | --- | --- |
| A bounded DEMO transaction model, including its BPMN expression | The initiator/executor exchange distinguishes coordination from production and includes rejection and allowable revocation. It can repair the evidence exchange while leaving existing boundaries intact. | **Adopt** the request-to-receiving-result distinctions in step 5 and the changed-C8 case. Reuse an adequate model. **Adapt** its questions into ordinary contribution specifications; a DEMO model and its full transaction semantics are not prerequisites for every OCE design. |
| An organization design using Galbraith's interacting policies | Strategy, structure, information/decision processes, rewards and people policies allow a designer to examine why a boundary and its coordination are or are not supported. A competent use includes lateral relations, rather than stopping at the chart. | **Adopt** the need to examine policy fit in steps 4, 6 and 7. If the problem is an unrewarded or unsupported exchange, changing the relevant policy may be sufficient; another specialization boundary is not automatically the answer. |
| The scoped combination used by OCE.4 | Keep a sufficient exchange account, then connect only the decision, access, service or other structures that can change the specialization choice. Preserve each result's acceptance and realization conditions. | **Construct** the boundary decision from these answers in steps 7–10 and the PumpWorks case. Accept additional inquiry when it prevents a boundary choice from hiding a consequential burden or independent decision. |

The combination is selected for the multi-relation PumpWorks choice, not ranked above the other methods for every use. It costs more than fixing one adequately modeled exchange and does not supply DEMO's formal protocol analysis. That is an accepted trade-off when a small, inspectable decision across unlike relations is needed and a complete formal model would have no receiving use. If an established transaction or policy-design practice already supplies those answers, use its result and stop. A bare chart that leaves the exchange unspecified is a failure case, not the serious rival.

Reopen when the extra structures do not change the decision, maintaining separate views creates inconsistent commitments, or another method supplies the same boundary and receiving-use answers at lower total effort.


#### OCE.4:11.2 - Source Contributions and Boundaries

| Source line | Retained contribution | Use boundary |
| --- | --- | --- |
| Guerreiro and Dietz, [DEMO enhanced BPMN](https://arxiv.org/abs/2410.08215) (2024), §§2 and 4–6 | Serious constructive alternative for coordination: transaction roles, production and receiving acceptance, exceptions and conditional revocation. | The paper develops a modeling construction and illustration. It does not establish comparative effectiveness for PumpWorks; OCE does not import the whole DEMO ontology or claim its protocol guarantees for plain specifications. |
| Galbraith, [Star Model](https://jaygalbraith.com/services/star-model/) and [organization-design practice](https://jaygalbraith.com/services/organization-design/) | Serious policy-design alternative: compare organization options through interacting structure, processes, rewards and people policies for the strategy. | These practitioner explanations support the policy questions, not an empirical ranking or a rule that every design needs all five policies changed. |
| Current FPF `A.22`, `C.30`, `C.30.AD`, `C.32`, and `C.32.PAD` | Selected structures, actual versus modal architecture, candidate synthesis, descriptions, and decisions remain separate. | Use these distinctions to qualify the local design; derive specialization boundaries and contribution content from the organization’s working problem. |
| Joseph and Sengul, [current organization-design review](https://doi.org/10.1177/01492063241271242) | Contemporary organization design uses complementary configuration, control, channelization, and coordination approaches; one representation or feature does not cover the field. | The review organizes research rather than selecting a local organization, relation predicate, or architecture decision. |
| Albert, [organization-structure perspectives](https://doi.org/10.1007/s41469-023-00152-y) | Activity arrangement, decision representation, and legal-entity perspectives can expose different design consequences. | Select the local organization and any additional perspective needed for its design question. |
| Grote et al., [contribution-based engineering role modeling](https://doi.org/10.1109/ISSE65546.2025.11370103) | Required contributions and stakeholder evidence can expose organization-specific contribution bundles and gaps. | The evidence covers three industrial cases and one workshop/clustering Method. Test transfer beyond those cases; decide local positions and assignments separately. |
| Fraccaroli, Zaniboni, and Truxillo, [work-design review](https://doi.org/10.1146/annurev-orgpsych-081722-053704) | Work characteristics, technology, diversity, and affected-person outcomes belong in design. | Supply the target organization and authority basis locally, and select a Method suited to its design problem. |
| Schulze-Meeßen and Hamborg, [participatory work-design representations](https://doi.org/10.1016/j.apergo.2023.104012) | Participant-facing representations can improve recognition and design knowledge. | Use representations to elicit design knowledge; test actual relations, authority, capability, and effects with the evidence appropriate to each claim. |

Reopen when representative use exposes a recurring contribution crossing the result cannot express, a serious alternative produces the same decision with less modeling burden, or a direct source changes the specialization or participant action.

### OCE.4:12 - Relations

- `OCE.1` supplies the organization, contribution, authority boundary, and affected-System scope. `OCE.2` supplies current Work and direct-relation evidence. `OCE.3` supplies candidate relation structures, assumptions, participants, and burdens.
- `A.22` governs actual selected structures; `C.30` governs possible-future structure and relation content; `A.6.REL` and the applicable domain predicates govern obtaining direct relation occurrences; `C.32.PAD` governs an architecture decision when that use is current.
- `OCE.5` consumes stable position-design needs. `OCE.6` establishes holder assignments and enabling relations. `OCE.7` consumes organization-side structure for paired product-or-service decisions.
- `OCE.9` consumes design constraints and later returns realization evidence. `OCE.12` may consume contribution architecture for leadership-contribution distribution. `OCE.12:4.3.1` supplies the cooperation needed to reach or revisit agreed contributions; `OPS.13` supplies establishment and authorized change of promises. Their results can refine a crossing while other architecture decisions remain in force.
- Strategy, Corporate Governance, Operations, Administration, Systems Engineering, finance, legal, labor, safety, privacy, and other specialists supply only their available compatible results or qualified direct sources.

### OCE.4:End

## OCE.5 - Define Organization Positions

> **Type:** Method pattern
> **Status:** Eternal alpha
>
> **Primary working result:** **organization-position descriptions and establishment or continuation decisions** that name the owning organization, effective establishment basis, identity-bearing expected contributions and assignment-eligibility criteria, continuation conditions, and evidence needs without asserting a holder or performed Work.

### OCE.5:0 - Use This When

Use this pattern when an organization needs a stable institutional position for expected contributions, but a title, job description, team label, or current holder is being used as the position itself. Enter when vacancy, holder replacement, eligibility, establishment, abolition, or continuation changes the decision.

Use it also when that stable-position need is undecided. Compare a position with a supported task, project or hybrid arrangement before undertaking establishment. Repeated work alone does not settle the choice.

Begin with a bounded organization and contribution need. A compatible `OCE.4` result is useful when the position follows from a new contribution architecture; an existing law, charter, bylaw, appointment scheme, or organization decision may instead supply the basis for a current position.

The first useful result names one owning organization, one position identity, its establishment and continuation basis, the expected contributions that distinguish it, the eligible system-role kinds, and a description usable by `OCE.6`. A vacant position is a complete result when no holder decision is current.

Use `A.2.1` directly when only a holder assignment is needed and no organization-position identity changes the use. Use `OCE.6` to establish assignments, authority, responsibility, resource, or access relations. Use Human Capability Development for developing a person's capability and applicable labor, legal, governance, compensation, privacy, or safety practice for their own decisions.

#### OCE.5:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| organization position | An organization-dependent institutional subject whose identity depends on one owning organization, an effective establishment basis, and identity-bearing expected-contribution and assignment-eligibility criteria. |
| establishment basis | The applicable constitutive rule and the authorized act or other facts satisfying it for the owning organization. A statute, charter, bylaw, or organization decision may supply the rule or its application basis. A document is evidence or a carrier unless the applicable rule gives its issuance constitutive effect. |
| continuation basis | The current facts and governed relation under which the position remains in force with the same identity-bearing criteria. |
| expected contribution | A possible-future contribution expected from a holder assigned through an eligible system-role kind. It is position content, not performed Work or evidence of result. |
| assignment-eligibility criteria | Criteria selecting which local system-role kinds may be assigned in relation to the position. Classify a particular System, assess its capability, and establish its assignment separately. |
| position description | An episteme describing the position, basis, expected contributions, eligibility, conditions, and neighboring requirements. Editing the description changes the episteme first. |
| holder | One actual `U.System` that may participate in an assignment concerning the position. A position can be vacant, and one System can hold several assignments. |
| title | A designation useful for recognition and retrieval. Title continuity does not prove position continuity; title change does not by itself reidentify the position. |

### OCE.5:1 - Problem Frame

Organizations need persistent contribution loci that survive ordinary holder changes. A safety-acceptance position, treasurer position, editorial-chair position, or release-integration position can remain while vacant, while different eligible Systems are assigned, or while its description is republished.

The persistent subject is institution-dependent. Its establishment, identity, and continuation depend on the owning organization and its applicable authority. Expected contributions and eligibility make the position usable for organization design, while the actual holder, assignment, capability, authority, responsibility, and Work remain separately governed.

### OCE.5:2 - Problem

When title, position, role kind, holder, and assignment are merged, ordinary changes become ambiguous. Replacing a person can appear to abolish a position. Renaming a title can appear to create one. Readers can mistake a job description for a grant of authority or proof of capability. A vacant position can disappear from the model even though the organization still relies on its expected contribution.

The reverse error models every recurring contribution or temporary assignment as a position. The organization records supposed positions without an establishment basis, and downstream users cannot tell which vacancies, appointments, or descriptions have institutional force.

### OCE.5:3 - Forces

| Force | Tension |
| --- | --- |
| Continuity | The organization needs stable contribution expectations, while holders, descriptions, and Work change. |
| Local law | Position identity depends on the organization and applicable basis, while reusable modeling needs a common working move. |
| Contribution breadth | One position can expect several contributions, while a broad bundle can hide incompatible eligibility or authority. |
| Eligibility | The position needs qualified kinds of assignee, while kind membership, capability, and assignment require separate evidence. |
| Vacancy | Planning and governance may need the position while no holder exists. |
| Description usability | Practitioners need a readable description that distinguishes the institutional position from its description and holder assignments. |

### OCE.5:4 - Solution

Define the position from its owning organization and institutional contribution, then recover the direct establishment and continuation predicates that give it force. Select only the expected contributions and eligibility criteria that distinguish the position for its current use. Publish a description after the position claim is recoverable, or publish an explicitly proposed description while establishment remains a future decision.

Recognition is cheap: enter when a decision about a position is blocked by confusion among vacancy, holder change, and description revision. Assurance is stronger: a current position claim needs its owning organization, direct establishment basis, identity-bearing criteria, continuation condition, scope, interval, and evidence.

When the organization is free to choose, compare ways to sustain the same contribution over the same horizon. A task or project arrangement can include explicit receivers, paid coordination and handover time, replacement, workload limits and access to support; do not compare a position with an unsupported labor market. Ask what must remain when the current assignment ends or its holder leaves. If current assignments and an existing institutional basis already provide the needed continuity, return that arrangement to `OCE.6`. If the organization needs a separately identifiable position through vacancy and successive appointments, recover or propose the rule that establishes it. If an applicable bylaw already requires an office, a position-free alternative would first require an authorized change to that rule.

#### OCE.5:4.0 - One first position description

Suppose a standards association's effective bylaw 8 already establishes an editorial-chair position, its expected contribution and its eligible local role kind. An organizer preparing an appointment can begin with one short description:

> The association's EditorialChair position is established by bylaw 8 and is currently vacant. It remains the same position while that basis and its identity-bearing criteria remain in force. It expects amendment-packet preparation and the return of unsupported evidence to contributors. The association's defined MemberEditorSystemRole kind is eligible for assignment. Return publication access as an enabling need for the separate appointment decision. Holder selection, authority, and effective access remain to be established.

Return that description and its bylaw basis to the person arranging the assignment. The appointment, candidate's capability and effective access remain OCE.6 or direct-owner questions. If the establishment or continuation basis is missing, return a proposed description or unresolved position claim instead.

The fuller questions below become useful when the position's identity, eligibility, contribution or institutional basis is unresolved or must change. Reuse current answers and add only the neighboring requirements that change this position or the next assignment; no separate form is required.

#### OCE.5:4.1 - Pattern-Use Unfolding

1. **Bind the position question.** Name the owning organization, intended contribution, current design or operating need, decision subject, authority, horizon, and first receiver of the position description. When establishment is still a choice, compare a supported direct arrangement with the proposed position. Include coordination, replacement, capability support, worker burden and institutional maintenance, not just the time to write either description. Stop the position branch if an adequate existing arrangement meets the receiving need.
2. **Recover candidate claims.** Collect the current charter, bylaws, organization decisions, position descriptions, title uses, contribution architecture, assignments, holder facts, and observed Work. State what each source can establish.
3. **Find the establishment predicate.** Identify the applicable domain predicate, authority, act or relation that creates the position, its effective condition, and its owning organization. If the applicable predicate or establishment basis is unavailable, retain a proposed description or unresolved position claim.
4. **Set the identity-bearing criteria.** State the expected contributions and assignment-eligibility criteria that distinguish this position. Add another criterion only when changing it would change which institutional position the organization means.
5. **Specify eligible role kinds.** Name the exact local system-role-kind domain and criteria relevant to assignment. Keep System classification, candidate-holder capability, and actual assignment as later questions.
6. **Separate neighboring relations.** State responsibility, authority, permission, resource, access, compensation, reporting, or membership requirements as separately governed needs. Include one only when it changes the position design or downstream assignment.
7. **State continuation and termination.** Name the basis remaining in force, identity-bearing criteria that must remain, effectivity window, abolition or suspension condition, and evidence that triggers re-evaluation. Holder or description change alone preserves identity unless the applicable basis says otherwise.
8. **Write the position description.** Give the title or designations, owner, basis, expected contributions, eligibility, scope, conditions, neighboring requirements, vacancy status, and source return. Mark a proposal as possible-future content.
9. **Test identity changes.** Replay vacancy, holder replacement, title change, description correction, changed expected contribution, changed eligibility, abolition, and re-establishment. State which preserve identity and which require a new or unresolved position claim.
10. **Return assignment input.** Supply position identity, eligible kinds, expected contributions, establishment/continuation facts, and enabling needs to `OCE.6`. Return capability, legal, labor, governance, compensation, privacy, or safety questions to their owners.
11. **Stop at position sufficiency.** Return when a reader can tell whether the position exists, what makes it the same position, which contributions it expects, who may be assigned by kind, and what observation reopens that account.

#### OCE.5:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| use boundary | Owning organization, contribution need, decision, authority, horizon, and first receiver. |
| position identity | Position reference or proposed reference, owning organization, direct establishment predicate and basis, identity-bearing criteria, scope, and interval. |
| expected contributions | Receivers, results or preserved conditions, applicability, acceptance needs, and relation to `OCE.4` when current. |
| eligibility | Exact local system-role kinds, criteria, exclusions justified by the contribution, and unresolved classification or capability questions. |
| neighboring requirements | Separately governed authority, responsibility, permission, access, resource, compensation, reporting, membership, legal, or safety needs that change later assignment. |
| continuation | Current basis, continuation evidence, suspension or abolition condition, and identity-changing observations. |
| description | Title/designations, content, source return, publication boundary, current or proposed status, and known losses. |
| assignment return | Inputs and gaps supplied to `OCE.6`; no holder or Work assertion. |

#### OCE.5:4.3 - What Changes in Practice

Practitioners can keep a position visible while vacant and can replace a holder without rewriting the position. They can also change a title or description without claiming an institutional change. When expected contribution or eligibility changes materially, the organization makes that identity question explicit instead of hiding it in a revised document.

### OCE.5:5 - Archetypal Grounding -- PumpWorks Release-Evidence Integration Position

The `OCE.4` design requires coordination of electrical compatibility evidence, platform test results, provider model artifacts, unresolved assumptions, and the evidence package used by Safety. PumpWorks compares two supported ways to obtain that contribution for the next twelve weekly releases.

In the project arrangement, a named integrator receives an assignment for the release sequence, with protected time, a replacement arrangement, retained evidence and a handover to the next integrator. Participants have a way to challenge overload and obtain learning support; project opportunities are allocated under the organization's applicable fair-access conditions. This is a credible way to supply the twelve releases. Repetition and the risk of absence do not by themselves defeat it.

The remaining need is continuity of the expected evidence-integration contribution between programmes: Safety and the provider must know which contribution the organization still expects while the integrator is absent or after the project ends. In this hypothetical case, no existing position has that continuing remit. The organization wants vacancy and succession to remain explicit until it changes or abolishes that remit. It selects a hybrid: one institutional position for that continuing contribution, with bounded holder assignments and project-specific work. It accepts the cost of establishing and maintaining the position, filling vacancies and revising a remit that could become obsolete. Coordination time, support and protection of participants are required under either arrangement. If an existing position already carried this remit, extending its supported assignments could be sufficient; a duplicate position would buy no continuity.

`PumpWorks-EngineeringOrg` is the owning organization. Authorized organization decision `PW-OD-2026-04` establishes `PW-ReleaseEvidenceIntegrationPosition` from 2026-10-01 while the decision remains effective. The identity-bearing expected contribution is to maintain the traceable release-evidence assembly and return unresolved mismatches to the participants supplying the underlying evidence. The eligible local system-role kinds are `SystemsIntegrationEngineerSystemRole` and `ReleaseEvidenceCoordinatorSystemRole` under the current PumpWorks role-kind scheme.

The establishment decision also permits the authorized role-scheme maintainer to update accepted evidence of qualification within either eligible local kind without changing the position. Changing the eligible kinds themselves or the position's expected contribution requires a separate continuation decision. These are supplied rules of this example, not a universal rule about eligibility.

The position description names coordination and evidence-return expectations; safety-evidence acceptance and release authority remain with their separate decision-makers. The description records test-environment and provider-artifact access as enabling needs for `OCE.6`. The position is initially vacant.

| Change | Position disposition |
| --- | --- |
| a holder is assigned on 2026-10-01 | Same position; `OCE.6` governs the assignment occurrence |
| holder leaves and the position becomes vacant | Same position while `PW-OD-2026-04` and identity-bearing criteria remain in force |
| title changes to “Release Evidence Coordinator” | Same position if the designation changes and the identity-bearing criteria do not |
| description clarifies a reporting view | Same position; the description episteme changes |
| an authorized eligibility-description update accepts an equivalent training route within the same eligible local kind | Same position under the stated continuation rule; the description changes, while a candidate still needs classification, capability and assignment evidence |
| expected contribution changes from evidence integration to issuing the release decision | Reopen identity and authority; do not silently continue the same position |
| `PW-OD-2026-04` is abolished with no continuation rule | The current position ceases; later re-establishment needs a new or explicitly continued identity basis |

The result supplied to `OCE.6` contains the position, eligible kinds, expected contribution, access needs, effectivity, and vacancy. It contains no candidate-holder selection or capability conclusion.

#### OCE.5:5.1 - Transfer Probes

| Setting | Reusable move | Required return or changed content |
| --- | --- | --- |
| public-hospital emergency flow | Define a clinical coordination or acceptance position from the hospital's applicable statutory and governance basis and its contribution | Clinical authority, licensure, labor agreement, shift assignment, privacy, and patient-safety conditions remain separate and can block assignment |
| distributed standards association | Define an editorial-chair or treasurer position from bylaws, member decision, expected contribution, eligibility, term, and continuation rules | Election, volunteer availability, employer permission, financial authority, publication access, and actual Work remain separate; no executive hierarchy is assumed |

### OCE.5:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| title realism | A familiar title is treated as the position identity. | Recover owner, establishment basis, expected contribution, eligibility, and continuation. |
| incumbent anchoring | The current holder's skills and habits define the position. | Start from the organization contribution and keep holder-specific capability or preference outside the identity. |
| document constitution | Publishing or editing a job description is treated as establishment. | Apply the direct establishment predicate and keep the description as an episteme. |
| hierarchy default | Every position is placed in a reporting tree. | Add reporting, authority, or membership only through their direct relations and when they change use. |
| vacancy erasure | An unfilled position disappears from organization design. | Retain the position while its establishment and continuation conditions obtain. |
| durable-object inflation | Every temporary contribution or assignment becomes a position. | Require an institutional establishment basis and stable identity-bearing criteria. |

### OCE.5:7 - Conformance Checklist

- [ ] One owning organization and one current or proposed position are explicit.
- [ ] The establishment predicate, authority, basis, effectivity, and evidence are stated or a missing governor is returned.
- [ ] Identity-bearing expected contributions and eligibility criteria are distinguishable from descriptive detail.
- [ ] Eligible system-role kinds come from an exact local domain; eligibility does not classify or assign a holder.
- [ ] Vacancy, holder change, title change, description change, identity-criterion change, abolition, and re-establishment have explicit dispositions.
- [ ] Authority, responsibility, permission, access, resources, compensation, reporting, membership, capability, and Work use their own relations when current.
- [ ] The position description states current or proposed status and its source return.
- [ ] The `OCE.6` return contains no inferred assignment or capability.

### OCE.5:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “The product manager role owns the roadmap.” | Recover whether the phrase denotes a position, role kind, assignment, authority, responsibility, contribution expectation, or current Work; establish each needed claim directly. |
| “Create a position by adding a box to the chart.” | Obtain the authorized establishment decision or other applicable constitutive basis, then publish the chart as a view. |
| “The position requires strategic thinking and leadership.” | State the expected contribution and eligible role kinds first; send measurable holder capability and person-development needs to their owners. |
| “The incumbent defines the job.” | Use observations of Work and participants’ knowledge as evidence, then decide the position from the organization’s intended contribution and institutional basis. |
| “No holder means no position.” | Check continuation conditions. Record vacancy and the assignment need separately. |

### OCE.5:9 - Consequences

Position continuity, vacancy, assignment, and description revision become manageable. Organization design can name persistent expected contributions while separately recording the actual holders and position descriptions.

The cost is local grounding. Different organizations can establish positions through different legal, governance, membership, or organization predicates. A reusable title list cannot replace that work.

### OCE.5:10 - Rationale

A position is useful because it persists across ordinary holder and Work changes. That persistence requires an organization-dependent identity rather than a label or person. Expected contribution and eligibility provide the stable organization-design content; establishment and continuation provide institutional force.

Keeping the position separate from `U.SystemRoleAssignment` also preserves cases where an assignment has no position and cases where a position is vacant. It lets `A.2.1` retain exact assignment species while OCE supplies the domain subject needed by organization design.

### OCE.5:11 - SoTA-Echoing

#### OCE.5:11.1 - Current-Line Selection for Position Design

The question is whether the same expected contribution should be sustained through supported task/project assignments or an institutional position with bounded assignments. The serious alternative is the protected form of job deconstruction discussed by Rogiers and Collings, not a title mistaken for an institution. Their accessible author explanation supports attention to worker discretion, inclusion and continuing support when work is allocated across tasks and projects.

| Decision-bearing need | Protected task/project or hybrid arrangement | Position-based arrangement and the local choice |
| --- | --- | --- |
| Adaptable contribution | Reassign work as demand and capability change, while preserving goals, resources, partners and support across the person's portfolio. | A continuing remit can make the receiving expectation easier to retain, but a rigid bundle can impede reassignment. Use direct assignments where the bundle need not persist. |
| Continuity and replacement | Name a substitute, handover and the party responsible for reallocating unfinished work. A project ending need not erase its obligations. | Preserve the same institutional subject through vacancy and successive holders when the organization needs that subject beyond current projects. Reuse an existing position when it already supplies this continuity. |
| Institutional constraints | Use the assignments allowed by the actual charter, labor or other applicable rules. | Establish a new position only through its applicable rule. A required office cannot be removed merely by choosing a task allocation scheme. |
| Coordination and worker burden | Pay for selection, switching, coordination and handover; protect access to opportunities and capability support. | Pay for establishment, vacancy handling and remit maintenance as well as the holder's coordination and support. A stable title by itself removes none of those burdens. |

**Adapt** the protected task/project line into the comparison in the Solution opening and step 1; **adopt** its worker-support questions for both arrangements. **Construct** the position/assignment separation and local continuity test in steps 3–9. For PumpWorks, a continuing evidence-integration remit beyond one programme justifies the hybrid in section 5, with an explicit institutional-maintenance cost. For a bounded release project with adequate succession and no additional institutional need, the protected project arrangement is sufficient and the position branch stops.

This is a conditional construction, not evidence that positions generally outperform deconstructed jobs. Reopen when task switching or position rigidity changes the burden, when a cheaper arrangement supplies the same continuity, or when the governing institution changes its establishment or continuation rule.

#### OCE.5:11.2 - Source Contributions and Boundaries

An organization position can persist across holders, carry several expected contributions and remain vacant. Determine which position is in force from the organization's rules for establishing and continuing it.

| Source line | Retained contribution | Use boundary |
| --- | --- | --- |
| Current FPF `A.2.1`, `A.2.2`, `A.6.REL`, `A.10`, `A.13`, and `A.15.1` | Role-kind classification, assignment, capability, relation obtaining, evidence, performer, and Work remain separately governed. | FPF does not currently define the organization-dependent institutional position. |
| Rogiers and Collings, [job-deconstruction paradoxes](https://doi.org/10.5465/amp.2022.0236) (2024), and [Rogiers’s explanation of the proposed protections](https://dobetter.esade.edu/en/end-jobs-unveiling-paradoxes-job-deconstruction) | Serious task/project alternative: retain flexibility with attention to control, inclusion and stability, including portfolio and career support. | The comparison uses the article’s abstract and this author explanation. They do not supply an institutional position-identity rule or measured comparative results for PumpWorks. Apply the protections to the actual work and local conditions. |
| Grote et al., [contribution-based engineering role modeling](https://doi.org/10.1109/ISSE65546.2025.11370103) | Deriving contribution bundles from required process contributions and stakeholder evidence can expose gaps hidden by titles. | Test transfer beyond the bounded engineering cases; establish local positions and assignments under the owning organization’s rules. |
| Albert, [organization-structure perspectives](https://doi.org/10.1007/s41469-023-00152-y) | Activity grouping, decision representation, and legal-entity perspectives can give different evidence about a position's place. | Use the perspective as evidence, then recover the position’s establishment basis and any separate authority relation. |
| Fraccaroli, Zaniboni, and Truxillo, [work-design review](https://doi.org/10.1146/annurev-orgpsych-081722-053704) | Work characteristics and affected-person outcomes must inform position design and later holder use. | Combine work-design evidence with the organization’s establishment basis; assess a proposed holder’s current capability separately when a holder decision is current. |

Reopen when a representative institutional setting cannot distinguish position identity from assignment, a stronger source changes the position-versus-direct-arrangement choice or identity-bearing criteria, or the required institutional locus must persist outside any one owning organization.

### OCE.5:12 - Relations

- `OCE.1` supplies the organization and contribution boundary. `OCE.2` supplies current descriptions, assignments, holders, Work, and gaps in the position-establishment or identity basis. `OCE.3` and `OCE.4` supply possible position needs and expected contributions.
- `A.2.1` defines direct assignment species and occurrences. `A.2.2` defines holder capability. `A.6.REL` governs direct relation obtaining and occurrence identity.
- `OCE.6` consumes position identity, eligibility, expected contributions, effectivity, and enabling needs; a position must have its own establishment basis when one is needed.
- Legal, labor, governance, compensation, privacy, safety, licensing, membership, and other domain practices govern their own predicates and decisions. An OCE position description can cite their available results without absorbing them.
- `OCE.9` later tests organization capability and actual relations. That test requires organization-level evidence beyond the holder-assignment and vacancy facts.

### OCE.5:End

## OCE.6 - Establish Holder Assignments and Enabling Relations for Organization Change

> **Type:** Method pattern
> **Status:** Eternal alpha
>
> **Primary working result:** the **obtaining holder assignments and enabling relations** needed for a bounded organization contribution, together with their predicates, participants, authority, effectivity, evidence, unresolved gaps, and any possible-future specifications that have not yet taken effect.

### OCE.6:0 - Use This When

Use this pattern when a contribution architecture or position design names who must contribute, yet the actual holder assignment, authority, responsibility, resource, access, permission, or other enabling relation is unclear or not effective. Enter when a staffing decision, appointment letter, budget, licence, roster, or tool account is being treated as proof that the complete arrangement now obtains.

Begin with a bounded contribution need and candidate holder Systems. Use an `OCE.5` position when the assignment depends on one; otherwise begin from the direct contribution and the exact local system-role kind. Recover the authority under which each change can be made.

The first useful result can be partial: one effective assignment, its exact species and interval, separately effective enabling relations, and a visible list of pending, contradicted, expired, or missing relations. A truthful blocker is useful when authority or a direct predicate is absent.

Use `A.2.1` directly when the assignment species and occurrence are already known and no OCE coordination changes the result. Use Administration for participant records, provisioning, or service cases; Human Capability Development for developing a holder's capability; Corporate Governance, legal, labor, safety, security, finance, or another specialist practice for their decisions and predicates; and `OCE.9` for organization-capability realization.

#### OCE.6:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| candidate holder | An actual `U.System` being considered for an assignment. Assess classification, eligibility, capability, consent, and assignment under the criteria applicable to the proposed contribution. |
| assignment specification | Possible-future content naming a proposed direct assignment species, participants, applicability, intended interval, and conditions. |
| assignment decision | A separately governed decision to establish, change, suspend, or end an assignment. It creates an occurrence only when the admitted species predicate gives that decision constitutive effect and every condition is satisfied. |
| assignment occurrence | One obtaining occurrence of a directly declared species under `U.SystemRoleAssignment`, with holder, exact local system-role kind, every real additional participant, predicate, applicability, and uninterrupted interval recoverable. |
| position-sensitive assignment | An assignment species whose direct predicate requires an actual `OCE.5` organization position as a participant. The position is included only because it changes predicate or identity. |
| enabling relation | Readable OCE wording for one separately admitted authority, responsibility, permission, resource-allocation, access, membership, commitment, or other relation needed for the contribution. It is not a new root relation family. |
| capability evidence | Evidence bearing on a qualified ability claim about the holder under `A.2.2`. Assignment, title, position, training, resource, or tool presence does not replace it. |
| assignment-and-enabling result | The account of direct relation claims returned by this pattern, including effective relations, proposed changes, and unresolved conditions. |

### OCE.6:1 - Problem Frame

Organization change becomes operational when actual Systems hold effective assignments and the other relations needed for their contribution obtain. An appointment can identify a holder and system-role kind, while resource access, decision authority, responsibility, equipment availability, provider commitment, and capability remain separate. Each has its own participants or bearer, governing conditions, basis, and effective interval.

The practitioner therefore coordinates a small set of direct changes rather than filling one staffing row. They decide what should become effective, obtain the acts or services required by each owner, and then verify the relations that actually obtain.

### OCE.6:2 - Problem

A chart or roster can show a name next to a position before an appointment is effective. A signed appointment can coexist with missing system access. A budget can exist without a resource-allocation relation for the Work. Responsibility can be stated without an admitted predicate. A capable person can lack authority, while an authorized holder can lack capability for the current envelope.

When these claims are bundled, later Work fails in ways that look personal or motivational. The organization cannot identify the exact missing relation, its owner, or its effective window. Conversely, a completed provisioning ticket can be mistaken for the whole organization change.

### OCE.6:3 - Forces

| Force | Tension |
| --- | --- |
| Speed | Contributions need holders quickly, while premature effectiveness claims hide blockers. |
| Exact species | Reusable assignment logic is valuable, while appointments, shifts, elected offices, provider assignments, and equipment roles have different participants and predicates. |
| Capability and authority | Both can be necessary for Work, while neither implies the other. |
| Resource readiness | Access and equipment can enable contribution, while their presence does not assign a holder or establish capability. |
| Several owners | Organization change needs a coherent result, while legal, governance, labor, security, finance, administration, and safety retain their authority. |
| Currentness | Assignment and access can expire or be suspended, while stale records remain visible. |

### OCE.6:4 - Solution

Start from the contribution and select the exact assignment species, then establish every needed neighboring relation through its own owner and predicate. Keep proposed, decided, effective, contradicted, expired, and missing states separate. Return only relations whose obtaining conditions are satisfied, along with explicit gaps that change Work entry or later realization.

Recognition is cheap: one required contribution with an ambiguous holder or missing enabling condition is enough to enter. Assurance is predicate-specific: the holder, local role kind, additional participants, authority, applicability, extent, basis, evidence, and currentness of every relied-on relation must be recoverable.

#### OCE.6:4.0 - One bounded first return

First consider an adequate service instruction plus the existing assignment result. `ADM.2:4.1–4.4` can establish which participants, grants and effective conditions an administrative action needs, return a missing condition to its owner, and reuse what is already settled. If that instruction and the owners' current results cover this contribution, reuse them; an OCE summary is not another approval gate.

For a small first use, take one contribution with a current, reusable assignment result and resolve the enabling gap that changes its next Work. In the PumpWorks case below, verify the appointment's continued effectivity and obtain the repository-access owner's current result. The practitioner can return this short account to the person arranging the integration:

> E27's release-integration appointment is effective from 2026-10-01 under PW-APPT-2026-17 and the declared PumpWorks appointment species. Its participants and uninterrupted interval are recoverable from that result. Provider-repository access is decided but not effective because identity federation is unfinished. Administration/security owns the access return. Provider-artifact integration remains blocked. The appointment still obtains; effective access and capability for provider-tool use require separate evidence.

Use the fuller coordination below when the contribution requires several changes whose results must fit together, such as an appointment interval, rig booking and provider-access window. Ask the owners what each can establish, compare the returned conditions against the same receiving Work, and return only the incompatible or missing part. Keep an existing service case as the carrier when it already supports that exchange.

Keep the existing assignment, authority and capability evidence with this account rather than reproducing it. When the access owner returns effective access, reassess the dependent Work; any other required but missing relation or capability remains a blocker. The fuller questions below are for new, unresolved or changed claims. This first use does not require re-declaring a current assignment species or surveying every possible enabling relation.

#### OCE.6:4.1 - Pattern-Use Unfolding

1. **Bind the contribution and use.** Name the organization, contribution, position when current, receiving decision or Work, scope, horizon, effectivity need, affected Systems, and first consumer of the result. Inspect the current service instruction and adequate relation results before choosing additional coordination. A routine administrative action may need only `ADM.2` and its direct providers; a changed contribution may need the coordinated establishment below.
2. **Recover authority and participation conditions.** Identify who may establish or end each assignment and enabling relation, under which predicate, basis, scope, and interval. Obtain consent, labor, election, membership, or protection results when their owners require them.
3. **Identify candidate holder Systems.** Recover each actual System, exact local system-role-kind classification when needed, relevant capability evidence, availability, conflicts, and current assignments. Keep preference and development needs separate.
4. **Select or declare the direct assignment species.** Begin with an ordinary claim, such as “E27 is appointed as release integrator under the PumpWorks appointment conditions.” Reuse an applicable species under `A.2.1`; declare one only when the needed species is missing. Recover the holder slot, exact local assigned-kind domain, every real additional participant, predicate, applicability, and occurrence-identity law. Add an `OCE.5` position participant only when the species truly depends on it. For a new species, use `A.2.1:4.1–4.4` and `A.6.REL` together with the organization's applicable assignment rules. These sources explain participants, obtaining conditions and episode identity; the organization must supply its own appointment or election rule. If that rule or a required participant kind is absent, return the missing governor for this assignment. Reuse an existing species without declaring it again. Expose an episode identifier only when the receiving use must distinguish or cite that episode.
5. **Specify the proposed assignment.** State candidate holder, assigned kind, position or locus when required, intended interval, conditions, conflicts, and basis. Preserve possible-future status.
6. **Make or obtain the assignment decision.** Use the applicable decision and authority. Determine whether and when the direct species predicate becomes satisfied; a document or record is constitutive only when that predicate says so.
7. **Establish neighboring enabling relations.** For each required authority, responsibility, permission, resource, access, membership, commitment, compensation, provider, or equipment relation, obtain the direct owner's result and satisfy its predicate. Return `missing-governor` rather than inventing a general relation.
8. **Verify effectivity and contradiction.** Observe or otherwise ground the relation occurrence, participants, interval, basis, and currentness. Classify each claim as proposed, decided-not-effective, effective, contradicted, expired, suspended, or missing. Compare the conditions needed together for the same contribution: individually effective results may cover different holders, resources, configurations or times. Give an affected owner the particular incompatibility and requested decision; retain unrelated effective results. Include inquiry, waiting, rechecking and continuing coordination in the choice of how much work to organize.
9. **Check capability separately.** Use `A.2.2` for the holder's ability under the required Work envelope. State whether a capability result supports current use, requires development, or remains unavailable. Assignment remains usable as a relation claim even when capability fit fails.
10. **Coordinate records and provision.** Use Administration for participant state, access cases, provisioning, reconciliation, and records when available. A record supports retrieval and evidence; the direct relation remains the result consumed here.
11. **Return precise downstream results.** Supply effective assignments and enabling relations to `OCE.9`. Give `ADM.2` an adequate effective holder or resource-assignment result when its particular administrative action depends on that relation. State its participants, scope, interval and grounds; permission, decision authority, access and any other required condition remain separate questions for that action. Send each gap to the owner whose action can change it.
12. **Stop at entry sufficiency.** Return when the people preparing the receiving Work or realization decision can tell which relations obtain now, which conditions block entry, which owner must act, and which observation reopens the account.

#### OCE.6:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| use boundary | Organization, contribution, position or direct need, receiving Work/decision, scope, horizon, and first consumer. |
| holder basis | Candidate Systems, local kinds and classifications when current, capability references, availability, conflicts, and evidence limits. |
| assignment species | Species, holder, assigned-kind domain, additional participants, predicate, applicability, identity law, and authority. |
| assignment branches | Proposed specification, decision, effective occurrence, interval, basis, evidence, and proposed/decided-not-effective/effective/contradicted/expired/suspended/missing disposition. |
| enabling relations | One row per direct authority, responsibility, permission, resource, access, membership, commitment, provider, equipment, or other relation actually needed; predicate, participants, basis, interval, evidence, and gap. |
| capability boundary | Required Work envelope, current capability result or unavailable return, and development or alternative-holder question. |
| records and provision | Available Administration or specialist result, record/source reference, and the direct relation it supports without replacing. |
| continuation | Work-entry effect, downstream receivers, expiring conditions, contradictions, and smallest reopen observation. |

#### OCE.6:4.3 - What Changes in Practice

Practitioners stop asking whether a position is “filled” as if that settled readiness. They can point to the exact effective assignment, authority, access, resource, and capability claims needed by the receiving Work. Missing relations become actionable returns to their owners instead of character judgments about a holder.

### OCE.6:5 - Archetypal Grounding -- PumpWorks Assignment and Access

`PW-ReleaseEvidenceIntegrationPosition` exists and is vacant. PumpWorks considers `Engineer-E27`, an actual System classified under `SystemsIntegrationEngineerSystemRole`, for the recurring release-evidence integration contribution.

The organization declares `PumpWorksReleaseIntegrationAppointment <: U.SystemRoleAssignment`. Its required participants are the holder System, one assigned role-kind value from the PumpWorks integration-role domain, and the actual `PW-ReleaseEvidenceIntegrationPosition`. Its predicate requires an effective appointment decision issued under the named PumpWorks staffing authority, an in-force position, fixed participants, the required holder acceptance, and no current suspension. One occurrence is the maximal uninterrupted interval during which that predicate remains true for those participants.

Appointment decision `PW-APPT-2026-17` becomes effective on 2026-10-01. The resulting assignment occurrence has `Engineer-E27` as holder and `SystemsIntegrationEngineerSystemRole` as assigned kind. The decision record describes and supports the occurrence because this species gives the effective decision constitutive force; the file alone is not the assignment.

| Needed relation | Current result | Consequence |
| --- | --- | --- |
| release-integration assignment | effective from 2026-10-01 under the species above | Holder and assigned kind are usable for the bounded contribution |
| test-rig access | effective rig-access occurrence under the admitted PumpWorks rig-access predicate for the named rig and release window after provisioning evidence | Integration Work may use the rig within that scope; licence or account evidence outside the interval does not establish access during it |
| provider-artifact repository access | decided but not effective because provider identity federation has not completed | Work entry remains blocked for provider-artifact integration; Administration/security owns the provisioning return |
| release-evidence coordination responsibility | source text says “responsible”, but no admitted predicate and participants are current | Return `missing-governor`; do not convert the assignment or position expectation into a responsibility occurrence |
| safety-evidence acceptance authority | the direct safety-evidence-acceptance authority relation obtains for another named Safety holder under its own predicate and basis | `Engineer-E27` coordinates evidence and cannot issue the acceptance result |
| release authority | the direct release-authority relation obtains for the release director under its own predicate and basis | The integration assignment supplies no release decision power |
| holder capability | current evidence supports the required integration Work envelope except provider-tool use | HCD or a supervised trial can address the capability gap without changing the effective appointment |

For the repository-access action alone, the existing appointment and an adequate service instruction are sufficient inputs to `ADM.2`. Administration identifies the eligible requester, the access decision maker and the permitted provisioning action, then obtains the federation result from its provider. Repeating all appointment work would add delay without helping that action. Successful provision would settle access within its returned scope; provider-tool capability remains a separate condition for integration.

Now suppose federation can be completed only after the booked rig window ends. The access owner and rig owner can each return a correct result, yet those results do not jointly enable provider-artifact integration in the planned interval. OCE.6's coordination compares the conditions against that one contribution and returns a new-window question to the rig owner and a corresponding access-window question to Administration/security. The result may be a compatible later window, a supported alternative arrangement, or no available window. Until then the appointment remains effective, the independently supported electrical-evidence preparation may continue under its own conditions, and provider-artifact integration remains blocked. The coordination does not extend a booking or grant access. If the current service case already obtains and reconciles these answers, reuse it rather than opening a parallel OCE case.

The result supplied to `OCE.9` contains one effective assignment, one effective rig-access relation, one pending provider-access relation, two separately held authority relations, a missing responsibility governor, and the bounded capability gap. Return the authorized holder/resource-assignment result to `ADM.2` for the Administration work that depends on it.

#### OCE.6:5.1 - Transfer Probes

| Setting | Reusable move | Required return or changed content |
| --- | --- | --- |
| public-hospital emergency flow | Declare the exact appointment or shift-assignment species, recover licensed holder, clinical authority, access, equipment, and current interval | Statutory authority, licensure, labor, fatigue, privacy, safety, and bed/equipment availability can each block entry; verify the required conditions from their current evidence rather than the HR roster alone |
| distributed standards association | Declare bylaw- or election-sensitive assignment species for a volunteer position and recover publication, ballot, repository, and financial access | Employer assignments, volunteer acceptance, elected term, member authority, several time zones, and employer permission remain separate; no executive staffing predicate is imported |

### OCE.6:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| roster truth | A name in a staffing table is treated as an effective assignment. | Apply the direct species predicate and current interval. |
| title authority | Seniority or position title supplies authority. | Recover the independently obtaining authority relation. |
| budget readiness | Budget or headcount is treated as usable resource access. | Identify the resource, allocation/access predicate, scope, and effectivity. |
| capability by appointment | Selection is treated as ability. | Use holder-dependent capability evidence and fit for the Work envelope. |
| record completion | Provisioning or HR record closure is treated as organization realization. | Verify the direct relations needed by the receiving contribution. |
| universal assignment | Every appointment receives the same binary holder/kind form. | Declare exact species and every real participant that changes predicate or identity. |

### OCE.6:7 - Conformance Checklist

- [ ] The contribution, receiving Work or decision, position when current, scope, horizon, and first consumer are explicit.
- [ ] Every assignment uses one directly declared `A.2.1` species with exact participants, predicate, applicability, identity, and interval.
- [ ] The position participates only when it changes the direct assignment species.
- [ ] Proposed, decided-not-effective, effective, contradicted, expired, suspended, and missing branches remain distinguishable.
- [ ] Authority, responsibility, permission, resource, access, membership, commitment, provider, equipment, and compensation relations use direct predicates.
- [ ] Capability is holder-dependent and separately evidenced for the required Work envelope.
- [ ] Records and provisioning support but do not replace direct relations.
- [ ] Downstream results name only relations that obtain and the exact gaps that block use.

### OCE.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “The position is staffed, so the team is ready.” | Recover the assignment occurrence, capability fit, authority, permissions, resources, access, provider conditions, and receiving Work separately. |
| “RACI assigns responsibility.” | Treat the matrix as a description; apply an admitted responsibility predicate or return a missing governor. |
| “The manager delegated it in chat.” | Recover the communicative Work, authority, delegation predicate, participants, scope, effectivity, acceptance, and evidence required by the applicable domain. |
| “The tool licence grants access.” | State the actual access or permission occurrence and its current scope; licence ownership can be a separate condition. |
| “The employee completed training, therefore can perform.” | Use HCD evidence and `A.2.2` to establish the holder's bounded ability and its fit to the receiving demand; training completion remains a separate result. |
| “The assignment ended because the record is stale.” | Distinguish missing current evidence from demonstrated predicate failure; record the occurrence as ended only when its direct identity law supports that conclusion. |

### OCE.6:9 - Consequences

Assignments and enabling relations become usable by later Work, Administration, and capability realization without being bundled. Expiration, suspension, partial provision, and missing authority can be handled locally.

The cost is coordination across owners. Legal authority, security permission, labor consent, finance allocation, and specialist capability require the relevant owners’ actions and evidence; the coordinated design must make those dependencies visible.

### OCE.6:10 - Rationale

An assignment answers who holds which local system-role kind under one direct species. Organization contribution often needs more: authority to decide, responsibility to respond, access to resources, provider commitments, and capability under current conditions. These requirements matter together, but each calls for its own claim and evidence.

Separating specification, decision, and effectivity also gives the practitioner an honest path from design to actuality. A partial result can guide the next action without claiming that the complete arrangement exists.

### OCE.6:11 - SoTA-Echoing

#### OCE.6:11.1 - Current-Line Selection for Assignment and Enabling Relations

The question is how to make E27's provider-artifact integration possible in the intended window. The serious direct alternative is an adequate appointment result plus a competent service instruction: `ADM.2` identifies the action and participants, distinguishes eligibility, grant and provision, and directs an exact missing condition to its owner. The relevant owners establish the conditions, including actual provision. This arrangement can settle a routine access gap without another assignment or readiness procedure.

**Adopt** that reuse in section 4.0 and step 1. The OCE coordination adds value when establishing a changed contribution requires several owner-specific results to fit together and the existing service instruction does not obtain that combination. **Adapt** the same action-specific reasoning into step 8: compare the results' holders, resources and windows for the common contribution, obtain a changed result only from the owner entitled to supply it, and preserve supported partial work. Section 5's delayed federation/rig-window case demonstrates that return.

Compare total effort for the same integration result. A maintained service instruction costs preparation, owner inquiry, provision, exception handling and upkeep; reusing it while the assignment and dependencies remain stable avoids reconstructing those settled answers. Explicit coordination adds recovery of cross-owner dependencies, joint timing inquiry, waiting and rechecking after changes. Accept that cost when no current instruction supplies the needed combination and failure would otherwise be discovered at integration. It can avoid a wasted attempt while returning a precise remaining dependency, but neither saved time nor successful capability is guaranteed. If the service arrangement already coordinates the same results and changed-condition returns, it is sufficient; OCE adds no mandatory second case, record or approval.

An appointment letter or completed account mistaken for complete readiness remains a failure example in sections 2 and 8. Waterson's human–AI function-allocation work helps reveal relevant dependencies during design; it is not the method that establishes this appointment, access or authority. Reopen the selection when coordination overhead exceeds the consequence it prevents, a service instruction covers the changed contribution adequately, or a needed relation lacks a usable governing rule.

#### OCE.6:11.2 - Source Contributions and Boundaries

| Source line | Retained contribution | Use boundary |
| --- | --- | --- |
| Current FPF `A.2.1`, `A.2.2`, `A.6.REL`, `A.13`, `A.15.1`, `F.6`, and `A.10` | Direct assignment species, holder capability, relation obtaining, performer, Work, assignment-bound attribution, and evidence remain separate. | Obtain responsibility, authority, resource, and access predicates from their owning domains; select a coordination Method for the organization’s contribution. |
| Current Organization Administration `ADM.2:4.1–4.4` | Serious direct alternative and receiving Method: recover the participants and effective relations needed by one administrative action, reuse adequate supplied results, and send an exact gap to its owner. | It can supply the whole needed inquiry for a routine action. Additional OCE coordination is justified by unresolved contribution-wide establishment, not by an assumed defect in Administration; successful provision and capability retain their own evidence. |
| Joseph and Sengul, [current organization-design review](https://doi.org/10.1177/01492063241271242) | Configuration, control, channelization, and coordination expose different organization-design features and consequences. | Use these design features to find the local assignments and enabling relations that need current evidence. |
| Grote et al., [contribution-based engineering role modeling](https://doi.org/10.1109/ISSE65546.2025.11370103) | Required contributions and stakeholder evidence can expose candidate holder/role bundles and gaps. | Use the bundles as candidate input; establish assignments and positions, recover authority, and assess capability separately. |
| Fraccaroli, Zaniboni, and Truxillo, [work-design review](https://doi.org/10.1146/annurev-orgpsych-081722-053704) | Technology, algorithmic management, diverse work arrangements, and affected-person outcomes change holder and enabling conditions. | Recover assignment identity and authority and access predicates from the applicable local rules. |
| Waterson et al., [function allocation for responsible AI](https://publications.ergonomics.org.uk/uploads/Function-Allocation-for-Responsible-Artificial-Intelligence-How-do-we-allocate-trust-and-responsibility.pdf) | Allocation should expose interdependence, joint operation, decision points, responsibility points, outcomes, authority, and dynamic trust. | The evidence comes from an early framework and small experiments. Test its fit for the local human–AI arrangement; qualify responsibility allocation and authority transfer under their own rules. |

Reopen when a recurring assignment species or enabling relation lacks an applicable definition, when a stronger direct source changes the holder/enabling action, or when actual use shows that the partial-result states cannot guide Work entry.

### OCE.6:12 - Relations

- `OCE.4` supplies contribution and enabling needs. `OCE.5` supplies position identity, eligibility, expected contributions, and effectivity when a position-sensitive assignment is current.
- `A.2.1` governs assignment species and occurrences. `A.2.2` governs capability. `A.13` and `A.15.1` govern performer and Work; `F.6` applies only when precise assignment-bound attribution is needed.
- `OCE.9` consumes effective assignments and enabling relations for realization and organization-capability evidence. `ADM.2` consumes an adequate effective holder or resource-assignment result when the administrative action needs that relation for the named participants, scope and interval. It still establishes or obtains that action’s other required permissions, authority and effective conditions separately.
- Administration can supply records, access cases, provision, and reconciliation. Corporate Governance, legal, labor, security, safety, finance, privacy, HCD, and other practices keep their predicates, decisions, and evidence.
- When a sibling result is unavailable, use a qualified direct source if it answers the needed question; otherwise retain an explicit missing result.

### OCE.6:End

## OCE.7 - Coordinate Product-or-Service and Organization Architecture Decisions

> **Type:** Method pattern
> **Status:** Eternal alpha
>
> **Primary working result:** **coordinated but separately governed product-or-service and organization architecture decisions** that name both holons and selected structures, correspondence pressure, four candidate forms, expected gains and losses, authority, evolution window, realization returns, and observations that reopen either decision.

### OCE.7:0 - Use This When

Use this pattern when a product or service architecture and an organization design constrain each other strongly enough that deciding one side alone would create avoidable coordination, evidence, provider, safety, or evolution burden. Enter when “the organization should mirror the product”, “teams own services end to end”, or “change the platform to fit the organization” is being used as the decision.

Begin with one bounded contribution and at least one organization-side structure or candidate from `OCE.3` or `OCE.4`. Recover the product-or-service focus, concept, architecture claims, and qualified specialist contributions from Systems Engineering or another owning practice when available. State missing inputs and what they block.

The first useful result can be a bounded mismatch: two separately governed decisions that say which structures will align, which will remain deliberately non-isomorphic, what burden is accepted, and what observation will reopen that choice.

Use `C.32.CONWAY` directly when only correspondence candidate synthesis is needed. Use `C.32.PAD` or the owning domain pattern for each architecture decision. Use `OCE.4` when only organization contribution structure is changing, Systems Engineering when only the engineered product architecture is current, and Operations when the question concerns managing continuing Work rather than changing the organization.

#### OCE.7:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| organization-side architecture content | Actual or modal `C.30` content about the named organization holon and selected contribution, Work, decision, information, access, service, coordination, legal, or other structures. |
| product-or-service-side architecture content | Actual or modal architecture content about the named product, service System, offering System, platform, or other exact product-or-service-side holon. For each stated directional pressure, identify whether this content describes the influence-source side or the side being changed. |
| correspondence pressure | A bounded claim that one side's selected structures influence the feasibility or burden of candidates on the other side through a named relation. It is not a universal law or automatic decision. |
| correspondence frame | The `C.32.CONWAY` synthesis frame used while either side is modal or the direct influence relation is unresolved. |
| exact correspondence row | A reusable `C.32.CONWAY` row about one obtaining direct influence relation whose two participants are obtaining `C.30` architecture-relation occurrences, with each holon and selected structure recoverable. |
| evolution window | The period and expected change range over which the correspondence decision is intended to guide Work. |
| coordinated decision set | Two or more separately governed decisions linked by shared assumptions, constraints, and reopen conditions. |
| bounded mismatch | A deliberate choice to keep selected structures non-isomorphic for the stated window while accepting and managing the resulting burden. |

### OCE.7:1 - Problem Frame

Products and services are produced, operated, supported, assured, and changed through organizations. Communication, deployment, test, approval, provider, evidence, and capability-home structures can make some product or service architectures easier to sustain. Technical dependencies can in turn create coordination and specialization pressure in the organization.

Correspondence can help without becoming one-to-one mirroring. Independent safety acceptance, scarce specialist homes, legal entities, platform services, regional operations, provider contracts, and continuing service can justify deliberate non-isomorphism. The task is to decide both sides with their gains, losses, authorities, and evolution windows visible.

### OCE.7:2 - Problem

One-sided decisions externalize burden. A modular product can be assigned to nominally independent teams that still share one test rig, safety decision, data source, or specialist. A reorganized stream can inherit a tightly coupled product that requires constant cross-stream integration. A service boundary can be redrawn without the provider authority, observability, or recovery conditions needed to operate it.

Mirroring language hides these facts when it treats similarity as adequacy or inevitability. Practitioners can also mistake an influence on the design, expressed in a chart, architecture description, or decision record, for the Work that realizes it. They then cannot tell what relation created the pressure, which System performed the Work, or which side should change.

### OCE.7:3 - Forces

| Force | Tension |
| --- | --- |
| Local autonomy | Aligned boundaries can reduce coordination, while shared safety, evidence, platform, and capability conditions can require cross-boundary relations. |
| Technical integrity | Product or service cohesion matters, while organization migration and provider arrangements constrain feasible change. |
| Specialist depth | Stable capability homes improve difficult Work, while contributors may face queues and extra handoffs across those boundaries. |
| Independent authority | Separate acceptance or governance can protect a characteristic, while it prevents full end-to-end ownership. |
| Evolution | Current alignment can be useful, while products, services, people, providers, and regulation change at different rates. |
| Evidence | Correspondence studies reveal contingent patterns, while a local decision still needs direct structures, relations, and consequences. |

### OCE.7:4 - Solution

Frame one exact organization/product-or-service architecture pair and generate four candidate forms: change the organization side, change the product-or-service side, change both, or keep a bounded mismatch. Compare complete candidates across the declared evolution window. Make the organization and product-or-service decisions under their own authorities, then connect them through explicit constraints, accepted burdens, realization returns, and shared reopen conditions.

Recognition is cheap: one architecture choice whose feasibility depends on an unlike structure on the other side is enough to enter. Assurance is stronger: actual correspondence claims require the exact holons, selected structures, direct influence predicate and occurrence, conditions, evidence, and window. Modal material remains in the synthesis frame.

Begin with the strongest applicable existing arrangement. For a software-delivery question, a competent DORA-style design may already support independent testing and deployment, clear service contracts and feasible operating support. Reuse its settled answers and qualified constraints. The paired comparison is useful when a consequential product or organization choice remains unresolved, for example whether an independent acceptance function should remain separate or a shared test resource prevents the proposed independence. Consider all four directions at the depth needed to settle that question; a disqualified form needs its reason, not a complete redesign. Count the effort of this comparison alongside the migration and continuing coordination it could change.

#### OCE.7:4.0 - One first paired decision

An instrument maker's engineering organization and inspection product form one bounded pair: two contribution groups serve two product modules that share a test setup. For the next two releases, reuse their current architecture accounts, participant corrections and qualified test, safety and service constraints. The proposed coordination pressure stays in a synthesis frame unless its direct influence relation is established.

The two authorized decision-makers can work from one short paired note:

> The organization-only candidate would merge the groups and disrupt an existing specialist-service commitment. The product-only and joint candidates require redesign that cannot fit the two-release window under the current engineering assessment. We therefore choose a bounded mismatch. The product decision retains the module and test boundaries. The organization decision retains the two groups and specifies one integration contribution and exception return per release. The gain is low migration burden; the accepted cost is shared-test coordination and no claim of independent release by each group. Reopen both decisions if the shared-test burden defeats the protected service commitment, or when the two-release window ends.

Each decision-maker records the decision for their own subject and authority. Send the needed assignment, access, test-time and service-protection requests to their owners for action before the dependent releases. Keep the existing evidence with the note. Use the fuller questions below for an unresolved claim or consequence that could change the pair, rather than rebuilding settled architecture accounts.

#### OCE.7:4.1 - Pattern-Use Unfolding

1. **Bind the paired question.** Name the intended contribution, organization holon, product-or-service holon, decision subjects, authorities, current Work, horizon, evolution window, protected characteristics, and first users of both decisions.
2. **Recover both architecture sides.** Separate actual `ArchitectureRelation` occurrences from candidate, required, desired, or expected `ArchitectureClaim` content. Name each selected structure, description source, currentness, and known loss.
3. **Recover each directional pressure relation.** State which side supplies the influence source and which side contains the changed architecture referent for this candidate; the direction can reverse between pressures. State how a communication, Work, test, deployment, approval, evidence, provider, capability-home, legal, service, or other source structure constrains the transformed-side candidate. Use the applicable direct predicate. Keep modal architecture content or unresolved facts in a `C.32.CONWAY` frame, naming what is unestablished; return `missing-governor` only when the required influence kind or predicate is absent. A false predicate excludes the claimed occurrence. A reciprocal claim requires its own reversed frame or relation occurrence.
4. **Select decision characteristics.** Name the few characteristics and burdens that can reverse the choice. Ask about the intended contribution, coordination, latency, changeability, safety, evidence, resilience, provider dependence, capability and service continuity, migration, effects on affected Systems, or another exact concern.
5. **Prepare all four candidate forms.** Change the organization side while retaining product/service content; change the product/service side while retaining organization content; change both; or keep a bounded mismatch with explicit cost and return. A form can be rejected quickly when a non-negotiable condition fails. Reuse a domain method’s existing comparison when it answers these choices at the required scope. Develop only unresolved consequences; the four forms do not require four complete alternative projects.
6. **Obtain qualified domain inputs.** Use available `SYSE.1`, `SYSE.2`, and `SYSE.9` results for engineering focus, linked use/System concepts, and professional contributions when compatible. Use qualified direct sources or return the missing result when a sibling body is unavailable.
7. **Compare whole consequences.** Include current and transition Work, provider and platform arrangements, independent authority, evidence paths, scarce capability, legal and service boundaries, affected Systems, reversibility, and the burden of preserving deliberate non-isomorphism. Include the effort to recover both sides, consult their decision makers, investigate rejected options and maintain coupled decisions. Accept that extra comparison only for a consequence that can alter the pair; retain a sufficient narrower answer when those conditions are already settled.
8. **Challenge the preferred pair.** Ask which omitted dependency, exception, configuration, operating episode, or later evolution would reverse the choice. Use prototypes, simulations, participant criticism, sampled Work, or specialist results only within their evidence limits.
9. **Make separate decisions.** Use `C.32.PAD`, `C.11`, or the owning pattern for each decision. State selected structures, fixed constraints, open refinements, accepted losses, authority, effectivity, retained alternatives, and relation to the paired decision.
10. **Specify realization and coexistence returns.** Name the organization-change Work, product/service realization Work, continuing-service conditions, assignment/access needs, and observations each owner must return. Keep the realization Work and its evidence separate from the decisions selecting it.
11. **Reopen locally or jointly.** Reconsider only the affected decision when one side changes without altering the correspondence choice. Reopen both when the pressure relation, accepted mismatch, protected characteristic, or evolution window changes materially.
12. **Stop at coordinated sufficiency.** Return when both owners know what is selected, what remains open, why structures align or differ, which burden is accepted, and what evidence can reopen the pair.

#### OCE.7:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| paired boundary | Contribution, two holons, decision subjects, authorities, current Work, horizon, evolution window, protected characteristics, and first users. |
| architecture sides | Actual relation or modal claim status, selected structures, descriptions, sources, currentness, and known losses for each side. |
| correspondence | Direction of each pressure, direct influence predicate/occurrence or synthesis frame, source and transformed architecture content, affected characteristic, evidence, and missing governor. |
| candidate forms | Organization-side change, product/service-side change, joint change, bounded mismatch, expected gain, known loss, migration burden, and rejected non-negotiables. |
| comparison | Contribution, coordination, safety, evidence, resilience, provider, capability, service, affected-System, reversibility, and uncertainty consequences that change this decision. |
| separate decisions | Selected option and structure effects, authority, fixed/open boundary, accepted losses, retained alternatives, effectivity, and cross-reference to the paired decision. |
| realization returns | Work, assignments, access, provider, coexistence, specialist, observation, and evidence results required from each owner. |
| continuation | Local and joint reopen observations, source-return conditions, and end of the evolution window. |

#### OCE.7:4.3 - What Changes in Practice

Practitioners stop treating product and organization architecture as either independent or forced copies. They can change the cheaper or more valuable side, change both, or accept a visible mismatch. Independent safety, evidence, platform, provider, capability-home, and service boundaries become design constraints rather than embarrassing exceptions to a topology slogan.

### OCE.7:5 - Archetypal Grounding -- PumpWorks Product and Organization Decisions

PumpWorks is deciding how weekly AI-inspection releases should relate to the product's module/evidence structure. The organization-side input is the `OCE.4` contribution-architecture design. The product-side input identifies field-module boundaries, model artifacts, electrical compatibility evidence, shared platform services, safety evidence, and release configuration. Both sides remain possible-future where their direct relations do not yet obtain.

The current directional pressure uses the product-side architecture as influence source and the organization-side architecture as transformed side: module and evidence dependencies influence how independently release contributions can be prepared, tested, accepted, and deployed. The synthesis stays in a `C.32.CONWAY` frame until direct influence and both actual architecture relations are available. If an organization-side structure is later claimed to constrain a product-architecture candidate, PumpWorks records a second frame or occurrence with the direction reversed; reciprocity is not inferred from the first pressure.

| Candidate form | Proposed change | Main gain | Known loss or burden |
| --- | --- | --- | --- |
| organization-side change | Create one stream-aligned release configuration around the current product/evidence couplings | Shorter recurring coordination path | Cross-stream shared rig, Safety, platform, and scarce specialists remain bottlenecks |
| product/service-side change | Refactor module and evidence-package boundaries while retaining functional contribution homes | More independent test and evidence preparation | Product migration and assurance cost; organization coordination still spans releases |
| joint change | Align selected release-evidence packages and stream contributions while keeping shared platform and independent Safety relations explicit | Reduces some repeated crossings without hiding protected independence | Requires coordinated product refactoring, new assignments/access, and transition Work |
| bounded mismatch | Retain current product and functional organization for the window; add named integration and evidence-return relations | Lowest migration burden | Continuing coordination load and slower learning are accepted and measured |

For the software portion, PumpWorks also considers a qualified DORA-style arrangement with independent evidence-package tests and deployments, explicit service contracts and supported operation. It could settle a software change whose remaining acceptance and resource conditions are already compatible. Here the shared rig, system-level evidence and independent Safety decision remain consequential, so nominal software independence alone cannot settle the whole weekly inspection release. PumpWorks reuses the proposed software tests and contracts, then compares the four forms above for the remaining coupled choice. It accepts the additional inquiry and decision coordination because the choice can move substantial migration and continuing-service burden; it does not infer that every software team needs this broader exercise.

PumpWorks selects the joint candidate for a bounded release family. The product architecture decision selects the alignment of module/evidence-package boundaries. The organization decision selects stream contribution boundaries and identifies the release-evidence integration need. Safety acceptance remains independent, platform and scarce capability homes remain shared, and provider support does not mirror a product module.

The two decisions cite the same assumptions and evolution window but retain separate authorities and realization Work. `OCE.6` supplies assignments and access; product realization remains with Systems Engineering; `OCE.9` later tests organization relations and capability; Operations supplies continuing-release and service observations. A changed safety regime, provider boundary, platform coupling, product family, or observed coordination burden reopens the affected decision pair.

The correspondence is partial. Routine package production follows the selected module boundaries, while the knowledge needed to challenge cross-module assumptions remains with a wider integration and specialist network. Safety acceptance also spans the release. The pair deliberately retains these wider relations rather than treating them as defective copies of the production structure.

In a continuation of this hypothetical case, a review discovers an omitted cross-module electrical assumption. Qualified engineering assessment finds that the product boundaries and tests remain adequate once that assumption is checked. The organization decision maker adds a specialist review relation within the available supported review interval; the product decision remains unchanged. This is a local revision because the observation changes how evidence is challenged without changing the selected product decomposition or its accepted conditions.

A later provider version introduces shared calibration state across the modules. The supplied engineering assessment now finds that the independently prepared packages no longer establish compatibility for that version. Both decisions reopen. The owners compare isolating the state, retaining it with joint test and integration work, and deferring the version. In this case isolating it exceeds the change capacity for the release window, while the qualified engineering and service results support one joint-test interval. The product decision therefore requires a jointly tested configuration for this version; the organization decision selects the corresponding integration and evidence-return contributions while keeping independent Safety acceptance. Each owner obtains the necessary realization and resource results through their own authority. If the joint-test interval becomes unavailable, the supported response is to defer or obtain another feasible arrangement, not to preserve the release merely because the earlier pair was accepted.

#### OCE.7:5.1 - Transfer Probes

| Setting | Reusable move | Required return or changed content |
| --- | --- | --- |
| public-hospital emergency flow | Pair the hospital organization structures with the emergency-service architecture: triage, diagnostics, treatment, bed flow, escalation, and information continuity | There may be no product modularity question; statutory clinical authority, privacy, labor, safety, facility, and continuing Operations can justify deliberate non-isomorphism |
| distributed standards association | Pair volunteer/editorial organization structures with the standard-development and publication-service architecture | Bylaw decisions, ballots, employer resources, volunteer availability, repositories, publication services, and language communities evolve at different rates; no single firm boundary or executive authority is assumed |

### OCE.7:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| mirroring determinism | Structural similarity is treated as a law or quality. | Recover the exact pressure, candidate forms, gains, losses, and local decision. |
| organization-only repair | Teams move while product/service dependencies remain unchanged. | Include the product/service-side and joint candidates. |
| product-only repair | Technical modularity is expected to remove authority, evidence, or provider coordination. | Preserve organization-side structures and enabling relations. |
| autonomy prestige | End-to-end ownership hides shared safety, platform, capability, and service relations. | State protected independent/shared contributions and their burdens. |
| diagram causality | Architecture descriptions are said to create the result. | Name Systems, Work, direct influence relations, decisions, and realization separately. |
| window blindness | Current alignment is treated as permanent. | State the evolution window and asymmetric change rates. |

### OCE.7:7 - Conformance Checklist

- [ ] The contribution, two exact holons, decisions, authorities, current Work, and evolution window are explicit.
- [ ] Actual architecture relations and modal claims remain distinguishable on both sides.
- [ ] The correspondence uses a direct predicate/occurrence or an explicitly provisional `C.32.CONWAY` frame.
- [ ] Organization-side, product/service-side, joint, and bounded-mismatch candidates are considered.
- [ ] Comparison includes the characteristics, independent/shared contributions, migration, affected Systems, and uncertainty that can change this decision.
- [ ] Systems Engineering or other domain results are consumed only when available and compatible.
- [ ] The paired decisions retain separate authorities, subjects, fixed/open boundaries, and realization Work.
- [ ] Local and joint reopen observations are stated.

### OCE.7:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “The organization must mirror the product architecture.” | State the exact structures and pressure relation, then compare all four candidate forms and accepted losses. |
| “Every service has one autonomous team.” | Recover shared platform, data, safety, evidence, provider, capability, Operations, and governance relations before deciding autonomy. |
| “Refactor the monolith and coordination will disappear.” | Name the organization Work and relations that the technical change is expected to alter, and observe them after realization. |
| “Reorganize around customer journeys.” | Identify the service and contribution structures, decision authority, shared capabilities, provider boundaries, and journeys' representation losses. |
| “The Conway workshop approved the target.” | Treat workshop output as candidate and participant evidence; make the separate architecture decisions under current authority. |

### OCE.7:9 - Consequences

Product-or-service and organization changes become one coordinated design question without losing their distinct subjects and authorities. Deliberate non-isomorphism becomes a controllable decision with visible cost.

The cost is broader evidence and coordination. Two decision owners may need different sources, and the attractive joint candidate can remain blocked by migration, safety, provider, capability, or continuing-service conditions.

### OCE.7:10 - Rationale

Mirroring is useful as a contingent hypothesis about coordination and cognitive burden. Current reviews and cases also show co-evolution, changing causal direction, value- and regulation-sensitive exceptions, and situations where deliberate non-correspondence supports search or contribution. A four-form comparison turns that evidence into constructive alternatives instead of a slogan.

Separate decisions preserve accountability and distinguish selected changes from realized ones. An organization change can be selected while product realization is still future, or a product architecture can change while the organization remains stable. Their correspondence matters only through named relations and consequences.

### OCE.7:11 - SoTA-Echoing

#### OCE.7:11.1 - Current-Line Selection for Coordinated Architectures

Compare answers for the same weekly inspection-software contribution, product family and evolution window, retaining the same safety, resource and service conditions. DORA's *Loosely coupled teams* is a serious conditional answer: it links testing and deployment independence with architecture and team design, compares architectural trade-offs, and recommends incremental change. It also exposes operating and dependency-management costs. It is more capable than universal mirroring.

**Adopt** its tests of practical software independence and **adapt** its evolutionary approach in the Solution opening and PumpWorks software slice. Where an existing software arrangement can meet the contribution and its governing conditions, that narrower answer is sufficient. Keeping a suitable small monolith or existing team arrangement can be legitimate. The practitioner need not manufacture a new paired decision just to restate it.

The OCE construction is selected when the unresolved question crosses product and organization authority or includes a consequential shared or independent relation. **Construct** the explicit organization-only, product/service-only, joint and bounded-mismatch comparison in steps 5–9 using `C.32.CONWAY` and the two owners' domain methods. It asks, for example, whether preserving independent acceptance and a shared rig is better than paying for a product redesign or organization migration. The partial-correspondence continuation in section 5 retains a wider knowledge boundary and shows why one observation revises only the organization, while changed calibration dependencies require both owners to decide again.

The extra work is recovery of two architecture accounts, consultation, investigation of alternatives and maintenance of shared assumptions. Accept it when it can avoid transferring an unresolved burden to the other side or distinguish a feasible mismatch from an infeasible alignment. This is a deliberate effort/coverage trade-off, not a claim that four-form comparison is cheaper for ordinary software changes. Compare preparation, migration, recurring operation and later revision together; reuse DORA or another established practice when it already supplies the same qualified alternatives and decisions. More candidate descriptions alone produce no benefit.

The wider comparison retains the contingent research line in section 11.2; DORA's software guidance supplies no universal institution or product-domain rule. **Reject** universal mirroring as the decision rule, while retaining it as the failure example in section 8. Reopen when added coordination does not change a decision, a sufficient narrower method becomes available, or a new product, provider or operating condition changes the accepted burden or correspondence.

#### OCE.7:11.2 - Source Contributions and Boundaries

| Source line | Retained contribution | Use boundary |
| --- | --- | --- |
| Current FPF `C.30`, `C.32`, `C.32.CONWAY`, `C.32.PAD`, `A.22`, and `A.6.REL` | Exact holons, actual and modal architecture, candidate synthesis, four correspondence forms, decisions, structures, and relation obtaining remain distinct. | Apply these distinctions while the authorized owners make the organization and product/service decisions separately. |
| Joseph and Sengul, [current organization-design review](https://doi.org/10.1177/01492063241271242) | Contemporary organization design is multi-approach and contingent; coordination and structure cannot be reduced to one representation or feature. | Select the local product/organization pair and test the relevant consequences before deciding. |
| Zani, Denicol, and Broyd, [megaproject organization-design review](https://doi.org/10.1016/j.ijproman.2024.102634) | Temporary and interorganizational boundaries evolve, and integration of product and organization architectures is a distinct design question. | Qualify transfer from megaprojects before using the evidence to choose a lifecycle, correspondence strategy, or product change in another setting. |
| Brusoni et al., [twenty-year modularity synthesis](https://doi.org/10.1093/icc/dtac054) | Product, organization, and industry architectures co-evolve; causal direction and the value of fit depend on context, evolution, and the question being asked. | Recover local authority and any claimed direct influence, then compare candidates for the declared window. |
| Burton and Galvin, [value and mirroring exceptions](https://doi.org/10.1016/j.jbusres.2022.07.023) | Regulation and value capture can make deliberate non-correspondence and stronger supplier ties preferable despite product modularity. | Treat the result as evidence from one industry case; test whether its value and regulatory conditions apply to PumpWorks. |
| Conway, [historical communication/architecture anchor](https://www.melconway.com/Home/Committees_Paper.html) | Communication arrangements can shape designed-system structure. | Use this historical anchor to ask about communication pressure; qualify the direct local relation and compare mirroring with the other candidate forms. |
| MacCormack, Rusnak, and Baldwin, [historical product/organization architecture study](https://doi.org/10.1016/j.respol.2012.04.011) | Comparable products developed under different organization forms provide evidence of architecture correspondence. | Test correspondence in the local pair and compare redesign consequences before selecting a change. |
| Colfer and Baldwin, [mirroring evidence and exceptions](https://doi.org/10.1093/icc/dtw027) | Mirroring is prevalent but not universal; exceptions and organizational forms matter. | Assess local adequacy separately; recover decision authority and, when realization is claimed, the actual performers and Work. |
| DORA, [loosely coupled teams](https://dora.dev/capabilities/loosely-coupled-teams/), “How to implement” and “Ways to improve” | Serious software-design alternative: test actual independence, compare architectural trade-offs and change incrementally with operating dependencies visible. | Apply it within software-delivery use and the actual authority and assurance conditions. The page’s particular API policies and wider causal performance claims are not adopted as universal OCE rules; the paired construction adds no empirical superiority claim. |

Reopen when a recurring organization/product-or-service case needs another decision-changing candidate form, a current source changes the correspondence answer, or observed realization shows that the selected pressure and burden variables miss the actual constraint.

### OCE.7:12 - Relations

- `OCE.3` supplies organization concepts and correspondence assumptions. `OCE.4` supplies the organization-side contribution-architecture design. `OCE.6` can supply effective assignments and enabling relations needed by realization.
- `C.32.CONWAY` supplies correspondence framing and exact rows; `C.32.PAD` supplies project architecture decisions; `C.30` and `A.22` govern architecture content and selected structures.
- Available compatible `SYSE.1`, `SYSE.2`, and `SYSE.9` results may supply engineering focus, linked use/System concepts, and qualified contributions. Systems Engineering retains product architecture and realization.
- `OCE.9` consumes organization design constraints and later returns actual relation/capability evidence. `OCE.11` can coordinate organization-change and continuing-service Work. Operations returns operating observations.
- Governance, Administration, legal, labor, safety, privacy, finance, providers, HCD, and other practices keep their decisions, predicates, evidence, and authority.

### OCE.7:End

<a id="oce-8"></a>

## OCE.8 - Compare Human, AI, Robotic, and Provider Arrangements for the Same Organizational Work Result

> **Type:** Method pattern
> **Status:** Eternal alpha
>
> **Primary working result:** a **bounded same-result Work-arrangement comparison** that keeps the obtaining baseline and serious whole candidate arrangements comparable, carries decision-bearing participant knowledge and protected conditions, and returns one authorized allocation or development choice, an authorized probe, rejection of the current set, or an exact reroute.

### OCE.8:0 - Use This When

Can this organization obtain the same bounded result another way -- by repairing the current arrangement, developing a current holder, assigning another internal holder, obtaining a provider contribution, changing a Method or support arrangement, or configuring human, AI, robotic, and provider Systems together? Use OCE.8 when that is the live organization-change question and the current way is insufficient or uncertain.

First check that the governed result, receiving use, situation, horizon, and acceptance basis are current enough to hold fixed. If the real question is whether the result is still needed, affordable, correctly defined, or accepted for that use, return before comparing arrangements. Contribution deletion, demand reduction, and result redefinition are different decisions.

Begin with a bounded organization and contribution plus current-enough Work and relation evidence. Carry forward the OCE.3 alternatives, assumptions, participant contributions, missing voices, and protection limits that can change an arrangement, comparison, or return. Equivalent qualified content is sufficient; the PatternIDs are not mandatory stages.

The first useful result may be an exact blocker. A missing authority, protected-condition result, access relation, provider condition, or result premise is more useful than an invented allocation. Use OCE.9 to realize a selected design or carry out a duly authorized bounded attempt even when necessary relations are not yet effective. Before dependent Work, establish the required choice or trial authorization, access, capability, and other necessary relations on their own grounds, or return the exact gaps.

Do not use OCE.8 for routine dispatch inside an already accepted arrangement, execution-time robot control, capability development alone, procurement alone, or product/service design alone. Return those questions to Operations, the applicable human-capability, AI, robotics, provider, Systems Engineering, or other owning practice.

#### OCE.8:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| result premise | The governed contribution or result, receiving use, situation, horizon, and acceptance basis held stable enough for same-result comparison. |
| Work-arrangement description | An episteme describing one possible-future way to obtain a result through named Work, performers or providers, capabilities, assignments and enabling relations, Methods and supports, authority and decision points, interfaces, recovery or exit, protected conditions, and evidence. Identify the actual Systems and relations separately when realization is claimed. |
| obtaining baseline | The separately grounded actual Work, performers, assignments, capabilities, supports, provider/service relations, authority, access, and direct relations currently relevant to the decision. |
| representative Work family | A recurring enough Work/result class used to generate and compare possible arrangements. Use the class to generate candidates; a configuration probe requires an exact WorkPlan or actual Work occurrence with the corresponding performer and authority basis. |
| arrangement fragment | Training, staffing, provider, interface, platform, automation, or another partial intervention that is not yet one complete way to obtain the governed result. |
| whole candidate arrangement | A complete-enough possible way to obtain the result under the same use, situation, horizon, acceptance basis, evidence window, and protected conditions. |
| participant contribution | Bounded evidence or a proposed alternative from people or other Agents whose knowledge of Work, burden, adaptation, authority, safety, service, providers, or affected use can change this decision. Agreement, a veto, authority, choice, adoption, or a changed relation each needs its own basis. |
| recommendation | An episteme proposing an option or probe and its grounds. A recommendation can inform a choice; authorization, assignment, provider commitment, and Work require their own decisions or realization evidence. |
| lawful disposition | The current decision result: choose now, probe again, reject the current set, or reroute to an exact missing premise, authority, or supplier result. |
| provision and enactment | Actual provider or internal Work, supplied results, effective assignments and relations, performed change Work, and later capability evidence. These require their own direct predicates and observations. |

### OCE.8:1 - Problem Frame

A bounded organization unit cannot reliably obtain a needed contribution. Familiar responses are to recruit a specialist, train an incumbent, buy an AI service, automate a task, acquire a robot, outsource the result, add a platform, or ask current members to absorb more Work.

These proposals can hide unlike changes. The limitation may be one holder’s capability, an ineffective assignment, missing authority, an unusable interface, weak input evidence, a provider commitment, a Method defect, a shared platform bottleneck, or a recovery condition. A useful decision compares whole ways of obtaining one result rather than ranking people, tools, and suppliers as isolated substitutes.

### OCE.8:2 - Problem

Partial proposals are easy to present but may be incomparable as complete ways to obtain the result. A training course is compared with a provider service although the course does not repair the interface. A complete hybrid configuration is compared with a failing incumbent baseline. A robot demonstration is treated as a Work arrangement without assignments, safeguards, fallback, or service continuity. A provider promise is read as provision, and a recommendation is reported as a decision.

Static “human versus machine” allocation also hides distributed Work. Identify how people, AI Systems, robots, provider Systems, platforms, artifacts, authorized decision-makers, and affected participants are involved -- as performers, supports, providers, or participants in other relations, as applicable. A hybrid chosen on presumed superiority can add coordination and review burden while performing worse than the best applicable solo configuration.

### OCE.8:3 - Forces

| Force | Tension |
| --- | --- |
| same-result comparability | Candidates need one parity basis, while some attractive proposals quietly change the result, use, acceptance basis, or horizon. |
| completeness and speed | Whole arrangements expose real burdens, while an early decision may have missing inputs and limited time. |
| capability and acquisition | Developing current holders preserves knowledge, while another holder or provider may close the gap sooner. |
| automation and judgement | AI or robotic support can expand capacity, while interaction, review, control, recovery, and exception Work can erase the gain. |
| provider leverage and dependence | Providers can supply scarce capability or service, while custody, continuity, substitution, recovery, and exit can become new constraints. |
| participation and authority | Work and affected-use knowledge can change the options, while decision authority and specialist predicates remain separately held. |
| assurance and learning | A representative probe can discriminate among candidates, while a demonstration outside the receiving situation supplies false confidence. |
| continuity and change | A new arrangement may improve the target result, while migration and continuing service protect current contributions and affected Systems. |

### OCE.8:4 - Solution

Hold one result premise stable and first inspect the comparison already available. A competent joint-work or adaptive-allocation study may already compare complete ways, including dependencies, changing conditions, several costs, participant burden and recovery. If its candidate scope, receiving use, horizon, evidence and protected conditions answer this organization decision, use that result under C.38:4.4 and take it to the authorized choice owner. Do not regenerate the five families or reproduce the study in an OCE account. A domain study can also cover development, assignment or provider alternatives; its substantive coverage decides whether it is sufficient.

When a decision-changing organizational question remains, name it before extending the comparison. A study may, for example, assume one provider and a fixed support team while the organization must decide who will supply continuing support. Reuse its qualified task-allocation results. Use the five families in §4.2 to find serious ways to obtain the missing contribution, retaining the smallest adequate incumbent repair. C.38:4.1–4.4 develops comparable whole ways; its C.39 return constructs a missing obtaining connection. OCE.3:4.1.1–4.1.2 develops the grouping, allocation, information, decision, participation and support mechanism, and C.32.MWA checks conflicts and displaced burden. Keep technical allocation and control operations with their domain Methods.

Bound the extra work by the choice it could change. Reuse available participant and specialist results, identify a plausible reversal or an unresolved protected condition, and estimate the preparation, consultation and delay needed to settle it. A possible gain too small to justify that work calls for a sufficient existing result, a narrower decision or an explicit unresolved return. A binding protected condition still requires its own result. Carry participant knowledge and missing voices into the exact candidates, assumptions, conditions or returns they change.

Compare whole candidates rather than labels. Include the best applicable solo configuration whenever a human–AI or human–robotic synergy claim can change the choice. Freeze only complete-enough ways into the C.11 OptionSet, name the DecisionSubject and authority, and apply an explicit ChoiceRule. Choose, authorize a discriminating probe, reject the set, or reroute; do not promote a recommendation into a decision.

Recognition is cheap: a proposed staffing, provider, platform, automation, or hybrid answer that cannot yet be compared as one whole way is enough to enter. Assurance is stronger: a choice needs current authority, a frozen OptionSet and basis, protected-condition results, and enough evidence for the stated rule. Configuration testing additionally needs the exact A.15.8 plan-or-actual-Work input.

#### OCE.8:4.1 - Pattern-Use Unfolding

1. **Test the result premise.** State the governed result, receiving use, situation, horizon, and acceptance basis. Return to OCE.1, OCE.3, or the exact contribution, demand, affordability, product, service, or acceptance owner if one of those is the live decision.
2. **Bind the organization question.** Name the organization, contribution, representative Work family, affected Systems, decision boundary, protected conditions, evidence window, and intended user of the comparison.
3. **Carry decision-bearing participant knowledge.** For each current or missing perspective, state the bounded evidence or proposal and the exact arrangement, assumption, protected condition, OptionSet position, comparison basis, or return it changes. Preserve protection and burden limits. Keep the basis for agreement, a veto, authority, choice, adoption, and participation repair separate from these knowledge contributions.
4. **Recover the obtaining baseline and bottleneck.** Ground actual Work, performers, assignments, capabilities, supports, provider relations, authority, access, interfaces, recovery, and current evidence. Name the exact limiting contribution or relation; do not substitute a chart or tool inventory.
5. **Reuse a sufficient comparison or generate the missing alternatives.** Check the available domain comparison against this result and decision boundary. If it is sufficient, reuse it and proceed to the separate choice; no new family account is needed. Otherwise consider developing a current holder, assigning another internal holder, obtaining a provider contribution, changing a Method/interface/platform/support arrangement, and allocating bounded Work across human, AI, robotic, provider or hybrid Systems for the unresolved question. Retain the current arrangement and its smallest adequate repair. Reject a family by a decision-bearing condition, not a stereotype.
6. **Complete candidates around parity.** Give each retained way the same required result, representative Work, use, situation, acceptance basis, scope, horizon, protected conditions, and honest account of any non-equivalence. Mark a baseline or fragment as baseline-only, incomplete, dominated, rejected, or retained for combination until it is whole.
7. **Preserve governed objects and truth status.** Keep performers, supports, capabilities, assignments, provider commitments and provision, participant contributions, authority, decisions, information and asset custody, interfaces, recovery, plans, actual Work, and possible configurations distinct.
8. **Compare whole consequences and full effort.** Use only characteristics that can reverse the choice: contribution quality, latency, cost and resource use, coordination, cognitive and physical burden, autonomy, safety, security, privacy, resilience, continuing service, affected-System consequences, reversibility, uncertainty, provider dependence and capability erosion. Include the preparation and modelling of the comparison itself, learning and transition, integration and review, and continuing support, recovery and change over the same horizon. Reuse common costs visibly; do not count them twice or omit them from only one way. Compare the best applicable solo way when a synergy claim is material. Keep role-specific capacity and non-negotiable conditions separate from a total cost; state a chosen trade-off when no way is no worse on all relevant values.
9. **Freeze and decide lawfully.** Put only complete-enough ways in one frozen OptionSet. Name the DecisionSubject, current authority, comparison basis, ChoiceRule, probe value, retained alternatives, conditions precedent, and one lawful disposition. A recommendation remains separate.
10. **Return selected constraints and evidence needs.** Send only selected possible-future relation, assignment, provider, capability, Method/interface/platform, coexistence, probe, and observation needs to their direct owners and later OCE.9 use. Report authorization, provision, performed Work, changed relations, capability, adoption, and organization results only with the support required for each claim.
11. **Reopen the smallest premise or candidate.** Reopen the result premise when its use, demand, identity, horizon, acceptance basis, or affordability changes. Reopen one candidate when its supplier result changes. Reopen the OptionSet when parity, authority, a protected condition, or another decision-bearing candidate changes.
12. **Stop at decision-usable sufficiency.** Stop when the authorized decider can choose, authorize a discriminating probe, reject the set, or follow an exact reroute without confusing a proposal with an obtaining arrangement.

#### OCE.8:4.2 - Generate Serious Arrangement Families

| Arrangement family | Complete the candidate with | Return without overclaim |
| --- | --- | --- |
| develop a current holder or admitted collective | Exact holder System, target Work family, current capability envelope and evidence, limiting contribution, intervention and provider if any, protected conditions, and representative transfer check. | E.23.CDI and the direct human, AI, robotic, organizational, or domain development Method own development and transfer. Check transfer to the target Work separately from completion of training, tuning, calibration, tooling, or provider delivery. |
| recruit or assign another internal holder | Required contribution, candidate holder kind and actual System when known, capability fit, exact assignment species, authority, resource and access needs, integration Work, continuity, substitution, and evidence. | OCE.5 and OCE.6 own positions, obtaining assignments, and enabling relations. Assess capability and verify assignment effectivity separately from recruitment and titles. |
| obtain a provider contribution | Provider System, bounded Work/result/service/support, capability evidence, receiving acceptance, retained or supplied authority, information and asset custody, access, dependency, monitoring, failure return, continuity, recovery, substitution, and exit. | Procurement, contract, finance, legal, privacy, security, safety, Administration, and provider practices retain their direct results. A promise is not provision; provider success is not receiving-organization capability. |
| change a Method, contribution interface, or platform/support arrangement | Exact limiting result, Method or MethodDescription, direct contribution/interface relation, supporting System, changed burden, migration, trial, recovery, and evidence that the change addresses the bottleneck. | OCE.4, OCE.7, OCE.15, Method Engineering, Systems Engineering, Administration, Operations, or the direct platform owner retains the changed object and result. Test whether the realized change improves the named bottleneck. |
| allocate bounded Work across human, AI, robotic, provider, or hybrid Systems | Work status; separately identified performers, supports, and providers; capability evidence; assignments and permissions; authority and decision points; interfaces and coordination; control, supervision, override, escalation, recovery; and representative probe evidence. | A.15.8 owns a configuration/recovery probe only after its exact input exists. A.13 and A.15.1 own actual performers and Work. Direct AI, robotics, human-factors, safety, and domain Methods own mechanisms and thresholds. |

The obtaining baseline and these five families are generation aids, not six automatic options. One whole arrangement may combine several families. A failing baseline remains comparison evidence outside the target-result OptionSet; a partial intervention remains a component until the other required relations and conditions are supplied.

#### OCE.8:4.3 - Keep Configuration, Choice, Provision, and Enactment Separate

Use a named Work family to generate possible arrangements; identify intended performers only in the particular plan. For a prospective A.15.8 configuration or recovery probe, require one exact present WorkPlan; intended performers and configured performance stay declaration-local to that plan. For an actual baseline or probe, require one exact admitted Work occurrence and independently recover its actual performers and supports.

A recommendation can propose a preferred option or probe. Choose now additionally requires a named authorized DecisionSubject and sufficient current basis. Probe again requires an authorized reversible probe whose observations can discriminate among pending options at proportionate burden. Reject current set means no complete option survives the rule. Reroute names the exact missing premise, authority, or supplier result. After the decision, verify provision, performed Work, changed relations, capability, adoption, and organization effectiveness through the evidence appropriate to each claimed result.

#### OCE.8:4.4 - Record the Result

| Result position | Required content |
| --- | --- |
| result premise | Governed contribution/result, representative Work, receiving use, situation, acceptance conditions, scope, evidence window, horizon, and premise-return conditions. |
| organization boundary | Organization, affected Systems, decision boundary, protected conditions, and intended user of the comparison. |
| current arrangement | Actual Work, performers, assignments, capabilities, supports, provider/service relations, authority, access, interfaces, recovery, evidence, and exact bottleneck. |
| participant knowledge | Contributor or missing perspective, bounded evidence/proposal or protection limit, and exact candidate, assumption, condition, comparison position, or return changed. |
| generation account | Sufficient existing comparison and its applicability, or the unresolved question, families considered, combinations and value-based rejection reasons. Keep each fragment’s baseline-only, incomplete, dominated, rejected or retained-for-combination status. |
| whole candidates | Same-result parity, Work/configuration, capability/development, assignment/authority, Method/interface/platform, provider, protected-condition, consequence, recovery/exit, and evidence positions. |
| comparison | Decision-reversing gains, losses, full preparation and continuing-use burden, uncertainties, applicable best-solo comparator, non-negotiable conditions and any accepted trade-off. |
| choice boundary | DecisionSubject, authority, frozen OptionSet, comparison basis, ChoiceRule, probe value, retained alternatives, lawful disposition, conditions precedent, and exact blocker. |
| continuation | Direct supplier requests, selected possible-future constraints, evidence obligations, realization boundary, and local or premise-level reopen conditions. |

Reuse current accounts of Work, Systems, capability, assignments, Methods, decisions, evidence, and relations. Record only the positions needed to understand or act on this comparison.

#### OCE.8:4.5 - What Changes in Practice

Practitioners stop asking whether “AI,” “a provider,” “training,” or “another hire” is best in the abstract. They compare complete ways of obtaining one result, see whose knowledge changed the set, preserve authority and protected conditions, and can name why the honest result is a choice, a probe, rejection, or reroute. Downstream realization receives explicit constraints and evidence duties instead of an automation or outsourcing slogan.

### OCE.8:5 - Archetypal Grounding -- PumpWorks Weekly Evidence Arrangement

PumpWorks intends weekly evidenced AI-inspection releases usable by the product and service organization while field service continues. The obtaining functional handoff produces the package quarterly, so it is useful baseline evidence but does not satisfy target-result parity.

The comparison inherits OCE.3 contributions by decision effect. Product, Electrical, and Software describe their integration Work, version dependencies, incompatibility returns, trace needs, and review burden. Safety supplies independent evidence-acceptance conditions and exceptions. Field Service and the service liaison supply continuing-service, incident-return, and fallback knowledge; customer-use evidence remains missing. The platform participant contributes knowledge of shared rig capacity, access, and recovery. The provider explains artifact, support, access, assurance, failure-return, and knowledge-retention conditions. Each contribution changes named assumptions or options. Agreement, a veto, trial or release authority, a choice, and adoption each require their own basis.

Family fragments are classified before choice:

| Generation input | Disposition | Why it is not yet a target-result option |
| --- | --- | --- |
| obtaining functional handoff | baseline-only | It misses weekly cadence and repeats integration burden. |
| develop Engineer-E27 | incomplete | It does not repair inputs, interface failure, capacity, recovery, or assembly. |
| second internal holder | retained for combination | It still needs capability, assignment, access, integration, continuity, and authority. |
| provider end-to-end package | rejected | It conflicts with access/confidentiality, receiving knowledge, recovery, Safety acceptance, and release authority. |
| interface/platform repair | retained for combination | It repairs evidence flow but not review judgement or capacity. |

Three complete possible-future ways share the weekly result, bounded release family, evidence interval, OCE.4 crossings, independent Safety evidence acceptance, separate release decision, continuing service, and manual/revert need:

| Option | Whole arrangement | Decision-reversing unknowns |
| --- | --- | --- |
| PW-WA-INTERNAL-PLATFORM | Engineer-E27 manually reviews traces and assembles the package over versioned inputs, permitted automated rig collection, a provider-artifact handoff with established custody, and a manual/revert path; Safety accepts evidence and the release director decides release. | Weekly capacity, review error and time, handoff latency and provenance, service burden, and recovery. |
| PW-WA-DUAL-HOLDER | Assign a second qualified integration holder; both holders partition and cross-review Work over the same interface, rig, Safety/release, continuity, fallback, and provider-artifact conditions. | Capability and assignment, acquisition time and cost, coordination, shared access, continuity, and substitution. |
| PW-WA-HYBRID-TRACE | The provider’s AI System proposes trace links from permitted versioned content; rig support collects named results; Engineer-E27 accepts or rejects each suggestion and assembles the package after targeted development addresses only E27’s provider-tool capability gap; Safety and release decisions stay separate and a manual/revert path remains. | Effective access, confidentiality and custody, provenance, false links, mismatches, review burden, provider/model failure return, and specialist-safety conditions. |

The constructed ChoiceRule excludes a way that cannot preserve Safety and release authority, confidentiality, provenance, service continuity, or practicable failure return. The hybrid is a probe recommendation because its narrow trace-review question could discriminate false-link, burden, and recovery risk before provider commitment or another-holder acquisition. It is not selected.

No exact PumpWorks trial DecisionSubject or effective arrangement-trial authority is supplied. Engineering sponsorship, Safety acceptance authority, and release authority do not substitute. Provider repository access is decided but ineffective, and protection, recovery, burden, and specialist-safety results remain unresolved. The lawful current disposition is reroute: obtain the deciding System and authority predicate, basis, scope, horizon, and authorized probe, plus effective access, custody, provenance, recovery, and specialist-safety results.

No exact present WorkPlan or trial exists. A requested PW-TraceReview-RepresentativeProbePlan name does not make one present. If a probe is authorized, its owner first forms the exact WorkPlan and keeps intended performers declaration-local. If Work later occurs, admit that exact occurrence and independently recover actual performers. The probe can then compare applicable human-only, AI-suggestion-only, and hybrid trace results for completeness, false links, mismatches, review burden, provenance recovery, provider failure return, and protected Safety/release conditions.

#### OCE.8:5.1 - Unlike Transfer Probe -- Emergency-Department Medication Reconciliation

A public hospital emergency department considers third-party AI support from medication-history assembly through acceptance of the reconciled list and any medication-order action. Continuous service, patient and worker protection, privacy, licensed practice, and statutory authority remain in force. PumpWorks thresholds, roles, and options do not transfer.

Gather decision-bearing perspectives before drawing specialist conclusions. Clinicians and pharmacists describe actual reconciliation Work, exceptions, handoffs, suggestion-review burden, and fallback. Other emergency-department workers, Operations, and service staff supply queue, coordination, downtime, and continuity knowledge. Patients and caregivers supply evidence about medication-use, communication, privacy, and protection conditions; a missing voice qualifies only the dependent claim or option. Provider technical and service staff supply service-boundary, data/model handling, support, failure-return, substitution, knowledge-retention, and exit knowledge. Use these contributions to revise the comparison. Any clinical or legal conclusion, agreement, veto, authority, choice, or adoption claim needs its own applicable basis.

| Direct owner | What absence blocks | Result needed to reopen the affected option |
| --- | --- | --- |
| clinical governance and licensure | Any discrepancy acceptance, reconciled-list acceptance, or medication-order action assigned to provider AI/staff or an unqualified holder. | For each action and holder: allowed, conditional, or forbidden, with authority/licensure basis, scope, supervision, escalation, interval, and evidence. |
| clinical safety and target-domain practice | AI-suggestion options and their probe, not a complete clinician-only way. | Conditions for displaying, using, checking, overriding, escalating, and stopping suggestions, plus comparison, failure, and clinician-only fallback evidence. |
| privacy, information governance, and cybersecurity | Any unapproved data flow or provider service. | Permitted fields, purpose, accessors, locations, interval, provider access, custody, retention/deletion, provenance, incident return, and patient-information condition. |
| provider, procurement, contract, and service | Reliance on an unproved promise, continuity, recovery, substitution, or exit. | Bounded promise and capability evidence, continuity window, failure return, substitution, exit, and data/model/artifact/knowledge return. |
| Operations, workforce/labor, human factors, and patient/worker protection | Any arrangement or probe whose service burden or fallback cannot be compared safely. | Service window, queue/workload and coordination burden, downtime/manual fallback, staffing constraints, protection conditions, and stop/revert observations. |

For each provider contribution, use only the action and holder combination permitted by the direct authority, licensure, safety, and data-governance results. Bounded processing or suggestions can be considered within those conditions; clinical acceptance or medication-order action needs its own affirmative basis. Verify provision separately from a commitment and qualify capability for the required Work envelope separately from one successful case. Keep applicable clinician-only and AI-only comparisons visible; reject AI-only enactment when a direct authority or safety result forbids it. When a required result is absent, keep the dependent action blocked and name the request and affected option. Obtain the jurisdiction-specific predicates even when a proposal includes “human in the loop”.

#### OCE.8:5.2 - A Sufficient Comparison and a Changed Support Condition

This constructed variation supplies conditions missing from the initial PumpWorks case; it does not report that its trial or deployment occurred. Operations Director D12 receives a qualified joint-work study for eight weekly releases. This variation supplies D12 as the authorized DecisionSubject for that arrangement choice, with Safety acceptance and release authority remaining separate. The study covers representative normal and failure cases, versioned inputs, effective access, capability, role-specific capacity and continuing field service. It compares human trace review with AI-assisted review over the same interface repair and manual fallback. The supplied Safety condition requires a qualified human to accept each trace link; an AI-only trace-review way therefore fails that condition. The human trace-review way is the best applicable solo comparator here. Another-holder and provider alternatives have already been examined and offer no decision-changing advantage within this horizon.

The following person-hours are supplied planning assumptions, including all preparation, learning, coordination, review and support within the stated boundary. Provider fees and other resource costs are stipulated equal. The rule first requires the protected conditions and minimum result quality, then minimizes total effort; the qualified role capacities cannot be exchanged merely because the totals fit.

| Complete effort over eight releases | Human review with interface repair | AI suggestions with human review |
| --- | ---: | ---: |
| Completed comparison study, common to both ways | 6 | 6 |
| Common interface preparation, independent acceptance and field-service continuity | 20 | 20 |
| Additional setup and learning | 8 | 16 |
| Produce, review and integrate eight packages | 64 | 40 |
| Trace-tool support, expected recovery and fallback readiness | 8 | 12 |
| **Total person-hours** | **106** | **94** |

The decider chooses the AI-assisted way on these supplied grounds and sends its conditions to OCE.9. The study already answers the organization question. Repeating generation in OCE.8 would add work without improving this decision; selection still does not establish assignments, provision or performed Work.

Before commitment, the provider changes the support offer: PumpWorks must now retain recoverable local trace artifacts and monitor their export. The study had held that contribution fixed. Manual export and monitoring would add three hours per release to the AI-assisted way, raising its total to **118**. The unchanged human-review way remains **106**. If the domain study can qualify this amendment, its updated comparison is sufficient too.

**Choose with the present basis.** The qualified human-review way remains available at **106** hours. An unresolved AI-support question does not prevent that choice. The case supplies no credible prospect of a sufficiently cheaper support repair, or a further warranted claim needed for the current decision, to justify commissioning a four-hour extension. D12 chooses the human-review repair now and sends its conditions to OCE.9.

**Reconsider an attainable inquiry.** Compare a feasible inquiry with the available 106-hour continuation under C.11.DUA:4.1–4.4. With four inquiry hours and the original 94-hour AI-assisted way, a repair’s additional setup and continuing support would have to total **less than eight hours** merely to leave a possible effort saving. That threshold is necessary for this saving claim, not sufficient reason to inquire: the prospective result must be attainable within the decision window and worth its uncertainty, displaced work and downside. Another needed claim or protected condition could justify a different trade-off, but it would need to concern the chosen receiving use; missing custody for an unchosen AI way does not disqualify the human way.

**Conditional support construction.** If a later question warrants completing another support candidate, work backward from the recoverable package to the missing retained artifacts, then forward from the available versioned store under C.39:4.3. A platform participant proposes automatic export to that store, with Engineer-E27 checking failures and returning to manual export. This combines a platform change and support assignment while retaining the provider’s trace suggestions. The local technical result supplies the export mechanism and its failure conditions; capability, access, capacity and custody evidence require their own basis.

Suppose those contributions are qualified and completing the candidate exposes **12** additional setup/learning hours and **8** additional support hours over the original AI-assisted way: **114** in total. If four common inquiry hours had been spent, the totals would be **110** for human review, **122** for AI assistance with manual export, and **118** for AI assistance with automatic export and internal support. Human review would still be selected, at **four hours more** than choosing it on the present sufficient basis. The twelve-hour gap between the first two post-inquiry alternatives is an arrangement difference, not a saving produced by the inquiry. These conditional calculations retain the support construction without recommending its investigation now. Keep an unsupported candidate conditional; a later material change in support cost, evidence or horizon can reopen the affected comparison. OCE.9 establishes the selected arrangement’s remaining realization conditions.

### OCE.8:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| technology-first framing | The tool or supplier becomes the decision subject. | Hold the result premise and representative Work stable, then generate whole arrangements. |
| novelty preference | The obtaining arrangement is excluded because it is familiar. | Include the baseline and its smallest serious repair. |
| fragment comparison | Training, hiring, outsourcing, platform, and automation labels are compared as if complete. | Complete each around parity or mark its non-option status. |
| hybrid optimism | Human–AI or human–robotic coupling is presumed synergistic. | Compare the best applicable solo configuration and observe interaction burden. |
| provider halo | Contract, catalogue, or demonstration is read as provision and capability. | Recover capability evidence, acceptance, custody, continuity, recovery, substitution, and exit. |
| participation theater | A workshop is said to provide consent, authority, or adoption. | Show whose knowledge changed which decision position and keep authority separate. |
| generic oversight | “Human in the loop” replaces exact decision, control, override, escalation, and evidence. | Request the direct predicates and conditions for this Work and jurisdiction. |
| recommendation inflation | A preferred probe becomes a ChoiceResult. | State the authorized DecisionSubject, rule, and lawful disposition independently. |

### OCE.8:7 - Conformance Checklist

- [ ] The governed result, receiving use, situation, horizon, and acceptance basis are stable enough for same-result comparison, or the exact premise return is named.
- [ ] The organization, contribution, representative Work family, affected Systems, authority boundary, protected conditions, and evidence window are explicit.
- [ ] The obtaining baseline and exact limiting contribution or relation are grounded.
- [ ] Current and missing participant perspectives are connected to the exact candidate, assumption, protected condition, comparison position, or return they change.
- [ ] A sufficient domain comparison is reused; otherwise the five families and incumbent repair have been considered for the unresolved question, with value-based rejection or non-option status.
- [ ] Only complete-enough whole ways under one parity basis enter the OptionSet.
- [ ] The best applicable solo configuration remains visible when a synergy claim is material; both sides include decision preparation, transition, review and continuing support at the same horizon.
- [ ] Work family, WorkPlan, actual Work, intended performers, actual performers, supports, and configuration claims remain distinct.
- [ ] Capability, assignment, authority, recommendation, choice, provider promise, provision, Work, adoption, and enactment remain distinct.
- [ ] The DecisionSubject, current authority, OptionSet, comparison basis, ChoiceRule, probe value, lawful disposition, and exact blockers are present.
- [ ] Prospective A.15.8 testing has one exact present WorkPlan; actual testing has exact admitted Work and independently recovered performers.
- [ ] Direct specialist, provider, realization, participation-repair, and OCE.9 returns name the result needed and what it changes.

### OCE.8:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Automate 60 percent of the process.” | Name the result and Work, then specify performer/support roles, interfaces, authority, recovery, and evidence for complete candidates. |
| “Train the current team or outsource.” | Complete both ways around capability, access, integration, provider, continuity, and transfer conditions before comparison. |
| “AI plus a reviewer is safest.” | Request the exact safety and authority results; compare human-only, AI-only when admissible, and combined performance at parity. |
| “The vendor owns the outcome.” | Separate supplied Work/result/service, receiving acceptance, retained authority, provider capability, provision, and exit. |
| “The robot passed the demo.” | Require representative Work or a present WorkPlan, applicable safety conditions, actual performers/supports, recovery, and receiving-use evidence. |
| “Participants chose the hybrid.” | Record their decision-bearing evidence or proposal and make the choice under current authority. |
| “Start the pilot and decide later.” | First name the trial DecisionSubject, authority, reversible probe, protected conditions, evidence window, and stop/revert rule. |
| “OCE.8 selected it, so the new arrangement exists.” | Return selected constraints to direct owners and OCE.9; observe actual Work, relations, capability, and results separately. |

### OCE.8:9 - Consequences

The organization can compare development, assignment, provider, Method/interface/platform, and hybrid possibilities without collapsing them into one automation scale. Baselines and fragments stay visible, participant knowledge changes explicit decision positions, and a missing authority or safety result becomes a precise return.

The cost is disciplined incompleteness. Attractive proposals may remain outside the OptionSet, and the current result may be reroute rather than a choice. Whole-candidate evidence can require specialist, provider, participant, and Operations work before a lawful probe or allocation is possible.

### OCE.8:10 - Rationale

The recurring organization problem is not “human or technology?” It is how one organization should obtain a bounded contribution through representative Work under current conditions. That frame keeps development, assignment, provider, Method/interface/platform, and hybrid branches comparable while their changed objects and direct owners remain distinct.

Current joint-work design can already handle the interactions that defeat static allocation. Dynamic human–robot planning and allocation treats changing human and robot conditions, feasibility, several objectives and reassignment; AI risk management includes costs, alternatives, third-party conditions and recovery. OCE.8 therefore accepts a sufficient domain comparison. Its additional contribution is to complete an unresolved organizational choice using the same qualified domain results, such as who supplies support and how that changes the whole obtaining way. The extra comparison consumes time too. In §5.2, accepting the original study avoids duplicate preparation; after the provider change, the available comparison already supports the human-review way at 106 hours. No further inquiry is justified on the supplied basis. The conditional support construction shows how a later comparison could proceed and why its four hours cannot be credited as an effort saving when the same qualified way was already available. A useful extension must earn its burden against that actual continuation, not against choosing a worse arrangement.

Choice remains a separate governed act. Recommendation, provider commitment, configuration testing, provision, performed Work, capability change, participation repair, adoption, and operating-organization capability each need their own truth makers.

### OCE.8:11 - SoTA-Echoing

#### OCE.8:11.1 - Current-Line Selection for Work Arrangements

| Comparison position | Selected result for practice |
| --- | --- |
| Current question | Which complete arrangement should obtain one bounded organizational result, given qualified task-allocation results and the full effort of deciding, preparing and sustaining the alternatives? |
| Selected current line | Reuse a sufficient same-result domain comparison. Extend only an unresolved organizational choice through C.38, C.39 and OCE.3, keeping the incumbent repair, applicable best solo way, participant knowledge and protected conditions visible. |
| Serious current alternative | Use a competent joint/adaptive-work design directly. Lagomarsino et al., §§3–4, explains planning and allocation with feasibility, changing conditions, multiple objectives and switching costs. For AI use, NIST AI RMF Map 3 and Manage 2.1 include benefits, costs and viable non-AI alternatives, with continuing third-party and recovery work. |
| Sufficient exit and remaining issue | When that method or its supplied result already covers the decision-bearing organizational alternatives and burdens, it is sufficient, including when it covers development or provider choice. Additional OCE work is useful when, for example, a qualified allocation study fixes a support contribution that the organization must now obtain differently. Missing scope in that particular result is the reason to extend it; a domain Method can itself supply the extension. |
| Adopt, adapt and construct | **Adopt** joint/adaptive interaction and whole-use cost questions. **Adapt** their results at the organization’s scope through §4 and steps 5–8; retain domain algorithms with their direct Methods. **Construct** only the missing whole-way connection with the stated suppliers. §5.2 works both sufficient reuse and a support change through an explicit choice rule on conditional inputs. |
| Full-effort comparison and chosen trade-off | Compare the same receiving result and horizon, using the same qualified domain evidence on both sides. Charge preparation, modelling, learning, coordination, review and continuing support to the ways that require them. Sufficient reuse adds no second account. Appraise an additional inquiry against the best currently qualified continuation, including any separately needed warranted claim. In §5.2 the 106-hour human way is already sufficient; the conditional inquiry would leave it selected at 110 hours. The case therefore stops without that extension and retains its support construction for a justified reopening. No empirical effectiveness or universal superiority is inferred. |
| Reopen | Reconsider the affected choice when a domain result covers the residual question more cheaply, a candidate or protected condition changes, or new workload, support, evidence or horizon reverses the comparison. An unchanged complete comparison needs no new family exercise. |

#### OCE.8:11.2 - Source Contributions, Limits, and Currentness

| Source line | Retained contribution | Use boundary and currentness |
| --- | --- | --- |
| Current FPF A.15.8, A.2.2, E.23.CDI, C.38→C.39, C.32.MWA and C.11; OCE.3 | **Adopt:** exact configuration inputs, holder-specific capability, sufficient-result reuse, construction of missing obtaining connections, whole-arrangement conflict checks and separate choice. | C.38:4.1–4.4 and C.39:4.3 supply comparison and construction; OCE.3:4.1.1–4.1.2 develops the organizational mechanism. Obtain local authority and realization evidence from their owners. |
| Naikar et al., [distributed and joint human–AI design](https://doi.org/10.1080/00140139.2023.2281898) | Distributed teams, artifacts, networked technologies, communication, adaptation, and self-organization replace a dyadic human-versus-machine frame. | Treat the conceptual synthesis and illustrative application as design input; qualify the local allocation Method and institutional authority separately. |
| Waterson et al., [function allocation for responsible AI](https://publications.ergonomics.org.uk/publications/function-allocation-for-responsible-artificial-intelligence-how-do-we-allocate-trust-and-responsibility) | Interdependence, joint operation, decision and responsibility points, outcomes, authority, dynamic trust, failure, and recovery extend static allocation. | The evidence comes from an early framework and small experiments. Select local responsibility predicates, legal rules, and organization-design Methods for the actual setting. |
| Vaccaro, Almaatouq, and Malone, [human–AI meta-analysis](https://doi.org/10.1038/s41562-024-02024-1) | Human-only, AI-only, and combined comparison remains visible when synergy matters; task type and the best solo alternative can reverse the answer. | The evidence covers heterogeneous experiments through June 2023. Test local comparative performance and obtain authority, safety, and provider conditions separately. |
| NASA, [Objective Function Allocation Method](https://techport.nasa.gov/projects/95457) | **Adapt:** compare joint crew, automation and robotic arrangements through work models and several performance measures, including off-nominal conditions. | The project description proposes the approach; the closeout summary reports simulations and experimental confirmation. Completed-project metadata and that summary do not qualify transfer to a local organization: obtain the relevant validation and receiving-use evidence before relying on effectiveness. |
| Lagomarsino et al., [adaptive task planning and dynamic role allocation](https://doi.org/10.1146/annurev-control-022624-013624), 2026, §§3–4 | **Adopt** as a serious current rival: planning, feasibility and adaptive allocation account for changing conditions, workload, quality and switching costs. | The review explains several methods and their limits, not one universal algorithm. Robotics control, safety thresholds and local algorithm qualification remain with engineering and Operations; §4 reuses their sufficient results. |
| ISO [6385:2016](https://www.iso.org/standard/63785.html) and ISO [10218-1/-2:2025](https://www.iso.org/committee/5915511/x/catalogue/) | Human, social, technical, equipment, workspace, environment, skill, well-being, lifecycle, and current industrial-robot safety conditions belong in applicable comparisons. | Check which edition and requirements apply to the arrangement. Use the relevant requirements in the comparison, then qualify performers, capability, authority, and safe use for the actual arrangement. |
| NIST [AI RMF 1.0 Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) and [human–AI interaction appendix](https://airc.nist.gov/airmf-resources/airmf/appendices/app-c-ai-risk-management-and-human-ai-interaction/) | **Adopt:** Map 3’s benefit/cost and scope questions, Manage 2.1’s viable non-AI alternatives, and third-party, monitoring, recovery and retirement conditions. These can support a sufficient domain comparison. | The voluntary 2023 framework is under revision. It supplies risk-management outcomes; the local comparison must still provide its allocation mechanism, authority, capability and provider evidence. |
| Aksin and Masini, [shared-service organization configurations](https://doi.org/10.1016/j.jom.2007.02.003) | Shared-service configurations and their effectiveness are contingent rather than one universal best practice. | Qualify transfer from administrative and business services before choosing an internal, external, engineering, clinical, robotic, AI, or mixed arrangement. |
| Goth et al., [shared-service administrative cost evidence](https://doi.org/10.1108/JSTP-10-2024-0345) | Objective cost-reduction evidence for administrative shared services is often weak or methodologically under-specified. | Require local evidence of cost gain, capability, provision, and arrangement adequacy before relying on the proposed shared service or outsourcing. |

When a changed source or specialist result alters an assumption, obligation or comparison for this arrangement, reopen the affected result premise, candidate or OptionSet. Return a missing reusable arrangement move exposed by use to OCE.15.

### OCE.8:12 - Relations

- OCE.1 supplies the bounded organization and contribution. OCE.2 supplies actual Work, direct relations, and evidence. OCE.3 supplies alternatives, assumptions, participant contributions, missing voices, and protection or burden limits that change this decision.
- OCE.4, OCE.6, and OCE.7 may supply contribution specifications, obtaining assignments and enabling relations, and paired-architecture constraints. Their PatternIDs are not mandatory stages.
- A.15.8 supplies configuration and recovery-probe discipline only after one exact present WorkPlan or admitted actual Work exists. A.13 and A.15.1 govern actual performers and Work.
- A.2.2, E.23.CAE, and E.23.CDI govern capability identity/evidence, ambiguity-resolving probes, development, and transfer. C.38 and C.11 govern same-result comparison and choice mechanics.
- OCE.5 and OCE.6 retain positions, assignments, and enabling relations. OCE.4, OCE.7, OCE.15, Method Engineering, Systems Engineering, Administration, Operations, and platform owners retain the objects and results they change.
- Provider, procurement, contract, finance, legal, labor, privacy, security, safety, human-factors, AI, robotics, target-domain, and governance practices retain their predicates, evidence, thresholds, commitments, and authority.
- OCE.9 later receives selected possible-future constraints and returns actual bounded organization-capability evidence and gaps. OCE.10 retains participation and target-working-culture repair. Use those patterns when realization or participation repair becomes the current question.

### OCE.8:End

# Part III - Realize Change While Work Continues

## OCE.9 - Realize a Bounded Organization-Capability Increment

> **Type:** Method pattern
> **Status:** Eternal alpha
>
> **Primary working result:** a tested, condition-qualified ability of an organization to obtain one contribution through representative work, or the exact unrealized condition and next repair that prevent it.

### OCE.9:0 - Use This When

The design has been selected and tools or appointments may already exist, but the organization still cannot produce the intended contribution reliably enough for the receiving use. Use OCE.9 to make one bounded organization-capability increment work: establish the necessary contribution and enabling relations, exercise them together, repair the first failure, and observe later use.

Start with one useful request-to-result path and its exception return. Ask who must actually supply, interpret, challenge and accept what. The first useful result can be a missing access, authority, learning, support or service condition; entering this Method does not require realization to have succeeded.

A selected design or an authorized bounded attempt can still contain unrealized relations. Obtain those relations through their owners before the dependent action. An arrangement recommendation alone supplies neither a choice nor trial permission.

Do not use this pattern for an isolated tool installation, one person's training, introduction of one Method, or a product-integration question that has no organization-change difficulty. Use the direct professional Method for that question. OCE.9 consumes its result when the organization contribution needs it.

### OCE.9:1 - Problem Frame

A change practitioner and the participating workers must make a designed contribution possible while the organization continues working. The difficulty often lies between otherwise competent participants: the request uses one version, a provider returns another, a holder cannot inspect the source, or nobody can accept an exception without improvising.

The governed subject is the organization's bounded capability, not the design document or the purchased platform. Here capability means an ability to obtain the stated contribution under stated conditions. The practical gain is a usable contribution with known limits, or a precise repair that replaces an undifferentiated “implementation is incomplete”.

### OCE.9:2 - Problem

Separate completion reports hide broken crossings. Staffing can be complete while access is ineffective. Training can be complete while the receiving task offers no opportunity to use it. A successful demonstration can depend on a facilitator who will not be present in ordinary work.

The organization needs evidence from the complete contribution and its failure return. It must retain which conditions were supplied, which actions occurred, and what the observed result can support.

### OCE.9:3 - Forces

| Force | Tension |
| --- | --- |
| Small increment | A small change is easier to recover from, but a fragment that never reaches a receiving use cannot demonstrate organization capability. |
| Integration | Participants must work together, while assignment, authority, access, provision, learning and acceptance remain different results. |
| Representative practice | Realistic work exposes failures, but exposure must stay within the authorized and protected envelope. |
| Continuing service | Learning, supervision and recovery require time that existing service may already consume. |
| Repetition | Later use tests dependence on special support; no fixed number of repetitions proves every capability claim. |

### OCE.9:4 - Solution

#### OCE.9:4.1 - Select a complete, small contribution

Name the changed organization, receiving user, contribution, current arrangement and either the selected design or the duly authorized bounded attempt. Hold the acceptance basis and representative work family clear enough to recognize success and failure. If the desired result itself is disputed, return to OCE.1 or the result owner. If neither a design has been selected nor an attempt authorized, return the missing arrangement or trial decision; an OCE.8 recommendation alone is insufficient.

Choose a slice that reaches an actual receiving decision or useful output. “Install the repository” is a support task. “Supply a version-bound evidence package, obtain acceptance or a reasoned return, and recover a missing-source case” is a candidate organization-capability slice.

State the permitted variation, observation window, protection and recovery conditions. Use a short existing work note if it carries these facts; no new record format is required.

First compare available implementation, integration or introduction results with this receiving use. A competent effort may already have established the contribution and its ordinary and exception paths, with current participants, support, protection and observation limits. If that result is sufficient and the receiving owner accepts its service consequences, use it and return the bounded result in step 4.6. Do not repeat tracing, practice, an integrated attempt or later observation simply to run this pattern.

Otherwise name the organizational claim still unsupported and the first additional action or relation that could settle it. Compare a competent continuation of the existing implementation with the proposed remaining work here, on the same contribution, configuration, window, protection and available results. Include participant effort, preparation, retained support, learning only if selected, service displacement, exception recovery and follow-up. Where both call for the same work, adopt one plan and its results; adding an OCE account is not another realization. Proceed only when the obtainable contribution warrants that complete burden against the available continuation or an explicitly accepted delay or narrower result. Steps 4.2–4.5 develop that residue, not a compulsory second implementation. Section 5.1.2 works both the sufficient-result and changed-support branches.

#### OCE.9:4.2 - Trace the contribution and exception paths with participants

Walk backward from the accepted result to its request, then forward through a representative exception. Ask each participant to show the input used, contribution made, next recipient and basis for accepting or returning it.

Inspect the crossings that can defeat the slice: source/version interpretation, effective assignment, decision authority, access, equipment, provider response, information custody, available time and support. A chart or a specification helps locate these questions but does not answer them.

Obtain the participants' account of the difficult parts. A receiver may know why a formally complete package is unusable; a provider may reveal a support-window limit absent from the design.

When participants can perform separate tasks but the contribution still fails, choose one action at a revealing moment. Explain what encompassing work is being performed through it now and which constituent actions make it possible. For example, interpreting a source can be part of judging support for a claim while that judgement is part of preparing an inspection package. The package's intended use changes what the interpretation must establish.

Use `B.1.5.EW` to follow those connections in both directions, only while they change performance, learning, allocation or use. Recover an unclear operation, obtain a capable contributor, or practise an understood operation under the encompassing conditions. Stop at an understood operation or an available contribution sufficient for this use. Keep the genuine earlier-result dependencies alongside this vertical. An enabling tool or external service has its own relation to the work; needing it does not by itself make its production a constituent action.

Use available knowledge to vary one whole condition and identify what must change in the selected action; then consider a limitation of that action and its effect on the whole. Distinguish the absent intermediate operation from inadequate access, a misleading cue or an infeasible demand. Further observation is useful when its attainable result can change the repair, what can be concluded about the capability or how the result may be used, and that gain warrants its full burden.

#### OCE.9:4.3 - Obtain and exercise the missing conditions

When a needed condition is missing, first use an adequate result or contribution already available. When a new outside result is needed, use `A.15.9` and `C.11.DUA` to compare its obtainable contribution and complete burden with a narrower return, another arrangement or continuation under the remaining uncertainty. For the selected request, name the participant or subject, configuration and window, missing condition, needed support for the claim, protection boundary and condition for trying again. Distinguish a promise from effective provision. If a required condition remains absent, keep the dependent action stopped and return the usable independent result.

Use OCE.6 for assignment and enabling-relation questions. Obtain actual access or support through Administration, the provider or other responsible practice. Use OCE.11 when learning, dual operation or recovery conflicts with continuing service. Use OCE.12 when the missing contribution is explanation, constructive challenge, mutual help or another leadership activity.

When a person needs development, supply the representative later-work demand and the task conditions. HCD.1, HCD.3 and HCD.4 help establish the demand, distinguish a human capability target from non-training causes, and qualify a capability profile where those questions are open. HCD.6 helps design a sufficiently whole practice task that exposes the missing action; HCD.7 arranges its support; HCD.9 conducts attempts with feedback; HCD.11 assesses what the person performed. Obtain the qualified provider and subject-specific criteria these Methods need. A described learning Method is usable guidance, while its required contribution must still be performed or supplied.

Secure the whole learning opportunity: an appropriate demonstration, practice on the difficult situation, criterion-based feedback, and later use under the receiving conditions. The learning professional qualifies that design and its assessment. The organization supplies the time, tools, access, protection and support needed to use it. Assess independent later performance in the receiving work, with any instructor assistance made explicit.

#### OCE.9:4.4 - Run a bounded integrated attempt

Before starting dependent trial work, confirm its decision and authority, protected conditions, effective access, capable participants, service coverage and recovery. Stop the defeated branch if one of these is missing. Independent preparation may continue under its own conditions.

Exercise the ordinary request, contribution, challenge, acceptance and exception return needed to settle the remaining claim, using the actual intended configuration and participants. Reuse matching observations already available. Include a relevant failure such as missing evidence or provider unavailability where its consequence remains unresolved. Keep the test small enough for the agreed recovery to remain credible.

Compare the observed contribution with its acceptance basis. Record a failed attempt as failed, including special assistance and workarounds. A receiving owner accepts only the result within that owner's remit; evidence acceptance is not automatically release or service authorization.

#### OCE.9:4.5 - Repair the first defeated crossing and observe later use

Repair the supported difficulty rather than relabel the whole change. An unsuitable design returns to OCE.4, OCE.7 or OCE.8. An ineffective relation returns to its owner. A participation or recurrent-practice difficulty enters OCE.10. Revise the trial or learning arrangement if the new observation defeats its premise.

Use the repair result and its evidence where they already settle the affected claim; otherwise exercise the repaired crossing inside the complete contribution again. Include the variation, support loss or substitution relevant to that claim. When independence from an initiating facilitator matters, observe a later episode without that person doing the work. Deliberately retained qualified support is a condition of a supported organizational ability, not an instruction to make every participant perform independently.

Choose repetition and observation strength from the consequence and variability of the receiving use. Three successful examples may justify a narrow local conclusion and still be inadequate for a reliability commitment, a substitute holder or a different product family.

#### OCE.9:4.6 - Return a bounded capability result and usable hand-back

State the contribution now supported, configuration, participants or qualified substitutions, work family, observed window, retained support, failures, limits and next reconsideration. The receiving Operations owner must accept the service and support consequences through its own decision.

Alternatively return the exact unresolved condition, who can supply it, the dependent action stopped, and the observation that permits another attempt. A useful realization result need not be positive.

Keep improvement at the right scale. A platform defect returns to its platform owner; a human target to its learning provider; a poor contribution premise to the organization decision; a recurring local norm to OCE.10. Those developments may interact without becoming one development object or a prescribed lifecycle.

#### OCE.9:4.7 - When stronger assurance is needed

For a consequential capability reliance, use A.2.2 and A.10 to qualify the capability and evidence rather than extrapolating from the demonstration. If the account asserts precise dated Work or a change attributed to the intervention, independently establish the performer through A.13 and the Work/change claim through A.15.1 and A.3.4; add assignment-bound attribution only when it is used. When Method enactment is claimed, identify the Method enacted in the actual Work.

A claim that this intervention caused the improvement requires the relevant causal-use qualification through C.28. Ordinary observation can support a narrower continuation or repair without making that causal claim.

### OCE.9:5 - Archetypal Grounding

#### OCE.9:5.1 - PumpWorks: a failed source-version rehearsal

This constructed six-week continuation begins after the appointment date in OCE.6. It is separate from OCE.8's earlier hybrid recommendation and reroute. None of its observations is empirical evidence about an actual company.

The earlier case lacks trial authority, effective provider access and protection/recovery results. The practitioner identifies the missing results and requests them from their owners; participants do not start the dependent trial until the required conditions hold. For the continuation, suppose the properly authorized change decision-maker separately defines and authorizes a bounded representative probe, the provider and security owner test permitted source access, and the service owner supplies coverage and manual-recovery conditions. E27's appointment and rig access are effective. The missing coordination-responsibility predicate remains missing.

The contribution is one weekly, version-bound inspection-evidence package. Electrical supplies source evidence; the provider’s AI System proposes trace links; E27 checks, challenges and assembles them; Safety separately accepts or returns the evidence. The provider stays outside PumpWorks-EngineeringOrg. Release remains another decision.

| Attempt or observation | What changes in practice |
| --- | --- |
| The first rehearsal includes an obsolete source revision beside the current one. The display makes their labels hard to distinguish, and the package contains an unsupported link. | E27 returns the link instead of calling the package complete. The person responsible for the tool's version display makes the old and current revision labels distinguishable. The observation also returns to the learning provider; “train harder” is not the sole repair. |
| A qualified provider demonstrates correct and incorrect binding, offers varied practice cases and criterion-based feedback, and observes a fresh case without coaching under the repaired configuration. | The learning result now answers the tool-specific demand at its stated limit. OCE.9 still needs the integrated organization contribution, not merely the individual assessment. |
| The authorized probe supplies comparison evidence. A separate, qualified OCE.8 arrangement decision then selects limited hybrid use under current protection, burden and recovery conditions. | Performing a probe has not selected an arrangement. The chosen use has its own decision basis. |
| Three later weekly package-preparation episodes exercise the revised contribution and return paths. One provider-unavailable case uses the qualified manual fallback; the last episode omits the initiating facilitator. | The receiving owner can inspect what the organization accomplished under those conditions, including retained support and the failure return. Three is a case value, not a general capability threshold. |

The resulting conclusion is bounded to that release family, configuration, participants/support and observed window. It does not establish capability for another holder, general reliability, customer benefit, release permission or enduring culture. OCE.11 carries the interruption and service account; OCE.10 follows whether early challenge becomes a recurrent local practice; OCE.12 supplies the brief, feedback and peer-support work.

If a separate repository change would retire Electrical's evidence-return support too soon, use OCE.16 for the cross-change question. Consume ME.6's or the direct owner's returned retention/replacement result; do not silently assume it from migration completion.

##### OCE.9:5.1.1 - Clear source labels with a missing interpretation skill

Consider a different failure in the same kind of contribution. The source labels and access are adequate. E27 can retrieve the current source and enter its identifier, yet cannot determine whether the source supports the claim under the package's stated configuration. At the act of comparing claim and source, that interpretation is part of assessing evidence, which is part of preparing the package for its receiving decision. Correct retrieval and transcription leave this intermediate operation unresolved.

Recover or obtain the required domain interpretation. A qualified interpreter can supply the missing contribution without waiting for E27 to master it. If developing E27's capability is also chosen, provide practice that keeps the claim, configuration and acceptance conditions together. If the package changes configuration, examine whether the same source still supplies support. If neither E27 nor that contributor can make the judgement, return the unsupported claim. The original case's misleading version cue instead calls for the person responsible for the display to make the revision labels distinguishable; these explanations lead to different actions.

##### OCE.9:5.1.2 - Use an adequate implementation; reopen changed support

Continue the interpretation variant, not the failed-label rehearsal. Suppose a competent participatory implementation has already established E27's request, a retained qualified interpreter's source judgement, Safety's separate acceptance or return, and the manual recovery path. Its evaluated ordinary and exception uses cover the present release family, configuration, four-week window and intended support. Its work account includes participant diagnosis, preparation, any selected learning, actual provision, protected exercises, service cover, recovery and later observation. These are supplied conditions of this constructed case, not consequences inferred from an implementation label.

The receiving owner accepts that bounded supported contribution. A competent implementation practitioner and an OCE.9 practitioner can both use this result now. No second path reconstruction, exercise or course is needed; there is no remaining organization-realization task merely because the work was described through another Method. E27's independent interpretation ability remains unestablished, but it is not required by the chosen supported arrangement.

Now suppose the retained interpreter becomes unavailable for the next two weekly packages. The old result remains evidence for its observed configuration; it no longer warrants those packages without that contribution. E27's retrieval and preparation remain usable. Both approaches face the same changed-support question under unchanged receiving dates, source configuration, acceptance and protection: obtain the interpretation through a qualified substitute, or defer the dependent packages. The existing implementation practitioner proposes that focused repair; competent implementation does not require restarting its whole programme.

The first added move is for E27, the receiving owner and the proposed substitute to locate the needed source judgement and establish who can supply it in that window. Suppose the substitute has the required domain capability, while access, the contribution interface and evidence of this joint use still need to be established. The following is the complete **additional** work budget for either continuation; normal package production and separate Safety review remain the same in both and remain charged in the continuing-service plan. The hours are summed person-hours, not an elapsed-time promise or interchangeable role capacity.

| Additional work in the two-week window | Person-hours in either continuation |
| --- | ---: |
| Participants and the deciding, service and receiving owners locate the affected judgement, compare available contributions and agree and authorize the bounded repair. | 1 |
| Substitute and E27 prepare the source/configuration interface; the responsible owner establishes and checks permitted access. | 2 |
| Participants perform a protected ordinary and exception attempt, including the agreed recovery and any assistance. | 2 |
| Other workers supply the service cover needed by those activities; their effort is not counted in the rows above. | 2 |
| The substitute supplies interpretation for the two later packages and participants observe the affected crossing, including use without the initiating facilitator. | 2 |
| The receiving owner and change practitioner review the resulting evidence and hand back its conditions and unresolved limits. | 1 |

Both the competent implementation continuation and this OCE.9 use require **ten additional person-hours** on these assumptions. No learning is commissioned: the substitute is already qualified, and E27's development is a separate possible choice. The authorized change decision-maker approves the bounded substitution and attempt. The service owner confirms each role's actual window and accepts deferring two hours of nonurgent service work as well as funding the cover. The receiving owner judges the two timely packages worth that burden; deferral would preserve protection but miss their receiving dates. This chooses timely delivery at the stated effort and service burden; it claims no cost advantage for OCE. If that trade-off or required protection cannot be accepted, return the affected packages for deferral rather than conceal the missing resource.

Adopt the competent implementation plan, with the organizational judgement and return explicit; do not perform it once under each Method name. If the repair and later uses succeed, the result supports the organization with this retained substitute under these conditions, not E27's unaided mastery. If an adequate current substitute-use result were already available, reuse it and omit the work it settles. Loss of the substitute, a changed source/acceptance premise or a defeated service window reopens only the dependent claim; it does not erase independent preparation or require a new course by default.

#### OCE.9:5.2 - An association's amendment packet

A member-governed association can realize a bounded evidence-preparation contribution without acquiring an employer's authority over volunteers. Suppose an editorial Method, volunteer acceptances, permitted evidence use, translation and repository support are supplied. Members submit, challenge and revise one amendment packet in two rounds.

The first useful capability result is preparing that packet under those conditions. A missing bylaw or ballot-authority result stops adoption of the standard, not independently permitted editorial preparation. Volunteer windows and publication support replace PumpWorks employment and release assumptions.

Suppose the supplied editorial rules distinguish a correction of wording from a proposed requirement change. A volunteer can copy a submission accurately but cannot yet apply that distinction. Classifying the submission is part of preparing the packet for the appropriate receiving decision, and the rules governing that decision constrain the classification. Obtain an explanation or another qualified editorial contribution; practise a contrasting pair of submissions when that can repair the limitation. Until the distinction is resolved, retain the submission without presenting it as a completed classification.

### OCE.9:6 - Bias-Annotation

A sponsor can choose an easy demonstration or hide exceptional assistance. Include the failure and support conditions that matter to the receiving use, make refusals and failed attempts reportable, and separate participant accounts from the sponsor's success claim. Do not equate slower performance during safe learning with unwillingness.

### OCE.9:7 - Conformance Checklist

- The slice reaches a named contribution and receiving use, including an exception return. An adequate current whole result is reused; additional realization answers a named remaining claim and warrants its full burden.
- The participants can distinguish selected design, effective conditions, performed attempt and capability conclusion.
- Missing assignment, access, authority, learning, service or protection results stop their dependent action.
- When adequate separate actions fail to form the intended contribution, the needed constituent/encompassing connection and the supported repair are explained.
- Failed attempts, repairs, assistance and later-use conditions remain visible.
- The conclusion states its configuration, work family, window, support and limits; stronger reliance has its own evidence.
- The receiving operation has an explicit hand-back or a named remaining gap.

### OCE.9:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Better action |
| --- | --- |
| Count installations, appointments or attendance as realized capability. | Follow one contribution to its receiving use and exercise the exception path. |
| Repair the person when the source, access or task cue is defective. | Compare rival causes and repair the supported condition through its owner. |
| Treat a facilitator-assisted demonstration as normal operation. | Record the assistance and observe the claimed continuation arrangement. |
| Repeat the successful trial until it looks convincing. | Select the variations and failure conditions that can defeat the receiving claim. |

### OCE.9:9 - Consequences

The organization obtains or reuses a small contribution with inspectable limitations, and any next repair becomes specific. New realization can require participant time, suitable practice, support, displaced service and observation; those costs are not justified by the OCE name. In section 5.1.2, adequate implementation ends the work, while lost support warrants the same ten-hour repair under either approach only on the accepted service trade-off. A narrower result or deferral can be more useful than an unsupported declaration that the whole change is implemented.

### OCE.9:10 - Rationale

A complete small contribution exposes dependencies that isolated deliverables conceal. Exercising its failure return reveals who can challenge, decide and recover when the nominal path breaks. Repeated use tests whether the contribution depends on temporary assistance. Returning observations to the relevant organization, platform, Method or learning question allows development at several scales without merging their results. Competent implementation can already do this work. OCE.9 selects that constructive line and makes the organizational contribution, remaining crossing and bounded capability return explicit; it does not earn another round of implementation. The supported arrangement in section 5.1.2 is sufficient until a relied-on support condition changes. Its continuation adopts the same focused repair and full burden that competent implementation supplies.

The same action can help perform an encompassing contribution at that moment; it need not merely produce an input for a later task. This explains why knowing the separate steps can leave an intermediate interpretation or coordination unperformable. B.1.5.EW supplies the general recovery, while OCE.9 uses it to obtain a complete organizational contribution. Follow only the connections relevant to this difficulty, retaining external support and sequence relations in their own meanings.

### OCE.9:11 - SoTA-Echoing

The practice question is how to obtain a usable, condition-qualified organizational contribution, given current implementation results and any remaining difficulty. **Adopt** competent participatory, determinant-sensitive implementation where it already answers that question; **adapt** its remaining work to the contribution and return in steps 4.1–4.6. Work-linked learning is conditional on a missing human contribution, not a required implementation stage.

| Comparison and selected move | Effect here, evidence limit and reopen condition |
| --- | --- |
| **Adopt** a sufficient SYSE.11 or ME.16 result. Their actual operations include consequential relations, support, failure, later use and bounded return; either may already answer the organizational question at its declared scope. | Step 4.1 compares the supplied result with the present receiving claim before adding work. Section 5.1.2 returns the supported contribution without another exercise or course. A result covering only part of the use leaves that precise gap, not a presumed gap attached to its source framework. Reopen only when a relied-on condition or receiving claim changes. |
| **Adapt** [Implementation Mapping](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2019.00158/full): participatory assessment, action and change objectives, mechanism-sensitive strategies, prepared and pretested support, and evaluation with iteration. This is the serious constructive line being used, not a course-completion foil. | Steps 4.1–4.5 keep sufficient results and bound further work to the changed contribution. In section 5.1.2 both competent Mapping-based continuation and OCE use the same ten-hour support repair; the accepted trade-off is timely packages against that effort and displaced service, not OCE superiority. The [2025 review](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2025.1603178/full) reports substantial effort and no formal evaluation of Mapping's effects in the included studies. Its healthcare evidence neither validates this case nor prescribes a universal minimum sequence. Reopen the local choice on a changed support, receiving or burden premise. |
| Current [transfer research](https://www.tandfonline.com/doi/full/10.1080/1359432X.2024.2376909) and [reverse training transfer](https://doi.org/10.1016/j.ssci.2025.106920) challenge a course-completion account by connecting workplace opportunity, feedback and reciprocal learning. | Adapt steps 4.3–4.5: secure qualified practice and later use, and return work failures to learning design. Scoping and maritime evidence are not engineering effect estimates. The accepted cost is practice/support time; a receiving-task or support change reopens the learning reliance. |

### OCE.9:12 - Relations

OCE.1 supplies the organization/contribution focus; OCE.4 and OCE.8 supply design and arrangement decisions; OCE.6 supplies effective assignments and enabling relations. OCE.10 addresses supported participation and working-culture difficulties, OCE.11 service coexistence, OCE.12 leadership contributions, OCE.15 a Method-account question, and OCE.16 a consequential cross-change dependency.

Use the current SYSE.11 bounded System-use result and ME.16 introduction result for the configuration and use they support. B.1.5.EW recovers the constituent/encompassing performance when a connection inside the contribution is unclear. A.15.9 and C.11.DUA govern obtaining a needed outside result. Use the named HCD demand, diagnosis, profile, practice, support and assessment Methods for the human questions in step 4.3; HCD.12 or HCD.13 addresses unfamiliar use, delay or changed support when that separate question matters. Their actual results retain their conditions. OCE.13/OCE.14 are not prerequisites for the observations and corrections needed by this bounded Method, and this Method does not supply their general organization-observation or revision functions.

### OCE.9:End

## OCE.10 - Choose a Response to Participation or Working Culture Difficulties in the Target Organization

> **Type:** Method pattern
> **Status:** Stable
>
> **Primary working result:** a warranted participation or working-culture response, its bounded consequences when performed, or the exact unresolved explanation, professional result or stop. A response can be supported across surviving explanations without claiming a unique cause or creating a new study.

### OCE.10:0 - Use This When

People nominally support an organization change, but the needed contribution is avoided, distorted, late or unnecessarily burdensome. Begin with one concrete episode: what contribution was expected, what happened when a participant tried, and what made another action more reasonable or safer?

Use OCE.10 to investigate the organization-side conditions and choose a supported response. When the task includes performing an intervention, retain its protection and authority limits and observe the receiving work. A sufficiently supported recommendation or current continuation may finish before an intervention or new inquiry is selected. The target-working-culture branch concerns how local ways of contributing, challenging and helping are learned, recognized and repeated; it is not a programme for changing people's personalities.

The first useful result may be “repair the missing access”, “change the contradictory consequence”, “obtain qualified practice”, or “the current evidence does not distinguish these causes”. A resistance label or a culture score is not an intervention.

Do not use this pattern to settle an employment, clinical, legal or personal-welfare case, or to replace a direct task or service decision whose cause is already known. Use its qualified owner. OCE.17 concerns the culture of Organization Change Engineering practice; OCE.10 concerns the organization being changed.

### OCE.10:1 - Problem Frame

A practitioner and the affected participants need to make a selected contribution workable in the target organization. A new request may conflict with an old reward, an effective duty, workload, belonging, legitimate concern or an established local practice. Formal design and nominal consent can coexist with those conflicts.

The governed move is to choose and return a warranted response to the participation or working-culture difficulty: retain a sufficient current practice, recommend a change, or perform a bounded intervention when that work is assigned. The practical gain is a supported next action instead of repeated persuasion or a larger training order.

### OCE.10:2 - Problem

The same visible non-use can have different causes. A participant may not know how, may lack permission or access, may be overloaded, may expect punishment for raising a problem, or may see a genuine defect in the change. Acting on the wrong explanation can increase burden and concealment.

An initial helpful conversation also differs from cultural continuation. A practice can be used once because its initiator is present and disappear in the next episode.

### OCE.10:3 - Forces

| Force | Tension |
| --- | --- |
| Timely action | A bounded repair is useful now, but a convenient cause can be unsupported. |
| Participation | Affected people know their work and consequences; consultation does not automatically confer choice or authority. |
| Local culture | Recognition and repeated practice matter, while a population-wide label can hide unlike situations. |
| Protection | Candid accounts need appropriate privacy and protection; inquiry must not become covert assessment or retaliation. |
| Evidence | Small observations can guide a local repair without supporting a universal or causal claim. |

### OCE.10:4 - Solution

#### OCE.10:4.1 - Recover one consequential participation gap

Choose a missed or distorted contribution that changes the organization's result. Recover the request, participant, receiving work, situation and timing. Ask for an actual example rather than a general attitude.

With the affected participant, reconstruct what was understood, attempted, available and expected to happen next. Ask what the person stood to lose, protect or accomplish by acting differently. Compare the account with permitted task evidence, including an occasion when the contribution did work. A manager's explanation is one source, not the default truth.

Keep work-relevant evidence and personal information separate. Obtain the appropriate permission and protection for interviews, observation or shared examples. Stop that inquiry branch when its lawful or professional basis is absent.

#### OCE.10:4.2 - Distinguish explanations that imply different actions

Keep the smallest live set of rival explanations that would change the next move. The following are examples, not a closed taxonomy:

| What the episode may show | Discriminating question | Different next action |
| --- | --- | --- |
| The source cannot be inspected. | Does the same participant perform correctly when access and the task conditions are supplied? | Repair effective access through its owner. |
| The task is unfamiliar or a skill does not transfer. | Is the difficulty still present under usable task conditions, and which representative later action is affected? | Use a qualified human-target diagnosis and learning provider. |
| Contribution competes with commitments or recovery. | What work and interruption burden occupy the necessary interval? | Obtain an allocation or service/change decision, using OCE.11 where applicable. |
| Early challenge is punished or date-only compliance is rewarded. | What actually follows a challenge, and does that consequence differ from the stated policy? | Obtain an authorized change to the consequence and test its use. |
| The role or change conflicts with participants' understanding and concerns. | Can people explain the contribution and its limit, and which concern survives that explanation? | Use inquiry, role dialogue or participant co-design; revise the design when the concern is valid. |
| A recurrent norm blocks help or challenge. | How do people learn, recognize and repeat that norm in the relevant group? | Change the demonstrated practice, recognition and support, then observe recurrence. |

Current HCD.3 can help distinguish a same-person capability target from task, access and support causes. Use the appropriately qualified professional when a clinical judgement or learning intervention is actually needed. Preserve a surviving rival when evidence does not distinguish it, and withhold an unsupported unique-cause conclusion. Request a new contrast only when its attainable result could change the response or warranted claim enough to justify its whole burden, delay and displaced work. Include the effort of designing the inquiry; C.11.DUA supplies that appraisal when needed. If the response is robust across the rivals, the contrast cannot arrive in time, or its burden exceeds its contribution, finish the qualified response on the available basis.

#### OCE.10:4.3 - Choose a sufficient response and develop only what remains

First compare the available response with the work that remains. A competent participatory implementation team may already have joined the participants' actions, relevant conditions, practical support and receiving-use observations. If that result supports the requested contribution under the current window, authority, protection and burden, use it. Do not repeat its inquiry, practice or evaluation to give it an OCE description. Uncertainty that cannot change this response may remain unresolved.

When a real gap remains or a serious alternative is offered, put the current response and the proposed continuation on the same receiving task and acceptance conditions. Recover the whole work each needs: participants' preparation and use, the construction and conduct of inquiry, facilitation or translation, condition repair, support, correction and later observation. Count shared work once in each alternative; compare who carries it and what other work it displaces, as well as total effort and elapsed time. Keep unavailable authority or protection as a stop, not a burden that benefits can compensate. Choose a supported improvement at comparable whole effort, or name the gain and the disadvantage that the affected participants and responsible owners accept. If neither is warranted, retain the sufficient response, narrow the result or return the missing contribution. Section 5.2 shows why equal hours can still imply a consequential choice.

For the intervention still needed, state the intended contribution, supported condition or surviving explanations, mechanism hypothesis, participants, effort, protection and authority, expected first difference, adverse consequence and stop. Choose the actual Method or professional intervention that fits those facts. When several explanations support the same bounded response, retain that uncertainty without inventing a unique cause. A determinant name or a strategy-menu item does not supply the Method.

For a role-understanding difficulty, conduct a working conversation: reconstruct the expected result and limit with the participant; compare them with the person's goals, concerns and observed task; resolve the actionable misunderstanding or return the unresolved design conflict; agree one next contribution and how feedback will be obtained. OCE.12 can help obtain and sustain this leadership contribution.

For a challenge norm, jointly construct a usable challenge-and-response practice. Name what evidence may be challenged, how a concern reaches the receiving decision, who can respond, what protects a legitimate question, and how useful challenge will be recognized. Practise an actual difficult case so participants can test the challenge, response, and protection conditions.

For a burden, incentive, access or authority conflict, obtain the direct change from the owner who can establish it. Persuasion is not a substitute. For missing capability, obtain qualified demonstration, practice, feedback and later-use evidence. A genuinely new Method account returns through OCE.15 and Method Engineering qualification.

#### OCE.10:4.4 - Perform the intervention and observe both use and cost

Run the smallest meaningful intervention under its agreed conditions. Make the new action and receiving response available at the point where the contribution occurs. Observe use, refusal, non-use, workarounds, burden and the receiving result.

Keep changes to the target arrangement separate from changes in how it is introduced. A repaired access path, protected discussion and new practice exercise can all contribute; their joint outcome does not identify each component's causal effect.

If the intervention produces harm, overload or a new protection problem, stop or reduce it under its governing rule. If participants reveal a valid flaw in the change, return that flaw to the design or decision owner rather than inferring a capability or motivation problem in the participant.

#### OCE.10:4.5 - Follow cultural continuation only where it is claimed

For a target-working-culture question, follow the relevant practice variant through demonstration, teaching, copying, recognition, challenge, working memory and later use. Who learned it from whom? What happened when a peer used it? Did the consequences in the receiving work encourage the stated action or its opposite? What remains available for the next participant?

Look beyond the initiating meeting. Observe another work episode and, when independence is claimed, an episode without the original sponsor performing the support. Record the population, relation, situation and window; a local finding does not describe every team in the organization.

Use C.36 for the cultural relations. The decision to promote a practice and the evidence that a population has learned or repeated it are different claims. A debrief, favourable survey or new document can support inquiry but cannot alone establish changed working culture.

#### OCE.10:4.6 - Return the consequence, revise or stop

Return what the available grounds warrant now. For a performed intervention, state what changed in participation and receiving work, what remained costly or missing, and which rival explanation survives. Continue only within the support of the current observations; revise a defeated mechanism or return a professional question to its owner. A useful response can remain warranted while its isolated causal explanation is unresolved.

An intervention can be useful without being sufficient. Distinguish a bounded participation improvement, evidence of recurrent local practice, an unchanged gap and a wider causal or cultural claim.

For ordinary local action, a short account of the episode, supported response and its use limit can suffice. Include a next observation only when the inquiry has a worthwhile attainable contribution. Stronger causal reliance uses C.28 and suitable evidence. Privacy, worker protection, safety, employment authority and professional competence remain direct conditions even for a small intervention. For a wider consequence comparison, use OCE.13; for an authorized organization-relation revision, use OCE.14. This Method includes the observations and local corrections needed for a claimed performed intervention.

### OCE.10:5 - Archetypal Grounding

#### OCE.10:5.1 - PumpWorks: make early evidence challenge usable

In a constructed continuation of the weekly inspection-package change, missing source inputs are disclosed late. Do not infer this cause from the earlier OCE.8 case: its trial authority and provider-access gaps remain separate until supplied.

The participants reconstruct a disputed trace. Permitted task evidence and their accounts show two difficulties: a source-access defect and a local pattern of blaming the person who delays a release. Praise is attached to meeting the date, even when the evidence later needs repair. Another participant also needs practice in explaining a version-binding objection.

The access owner repairs the first condition. For the second, the authorized change owner establishes a protected early-challenge route and changes what is recognized in the package discussion: a timely, substantiated challenge that enables correction is a contribution, not failure to cooperate. Participants co-design the request and response using the disputed trace. A qualified provider supplies practice and feedback for the difficult explanation; the receiving task gives a real opportunity to use it.

In the next constructed episodes, a peer raises a missing-source question before package assembly, the receiver investigates it, and the discussion recognizes the useful correction. A later participant can recover the example and uses the same practice without the initiating sponsor prompting the exchange.

The supported result is a changed local participation practice in those episodes. Access repair, changed consequences and practice happened together; no isolated causal effect is claimed. A count of earlier reports is insufficient by itself: the questions must be relevant and the burden and receiving result must be inspected. The whole organization's culture, release quality and enduring adoption remain unestablished.

For a current continuation of the combined repair, suppose the existing observations support its useful contribution and acceptable burden, while a component-by-component comparison would take the qualified provider away from needed practice and could not change the decision to retain it. Continue within that scope and keep the causal alternatives unresolved. A new interview or experiment is not required to finish that response. If changed access, burden or protection makes the response differ across the surviving explanations, select an obtainable worthwhile contrast or take the warranted narrower action or stop; do not claim the missing distinction.

If available interviews instead showed that people already challenge freely but cannot obtain the needed source, the appropriate intervention would be access repair, not a culture campaign.

#### OCE.10:5.2 - Participation without common employment authority

In a constructed distributed standards association, silence may reflect language, time-zone burden, employer-owned evidence or a seniority norm. A competent team using Implementation Mapping has already obtained participant input, qualified translation, a lawful evidence-use boundary and an asynchronous challenge-and-response practice. Its prepared materials and observed use in two amendment packets support a sufficient current response: a junior member submits a permitted question, an editor answers it and the correction reaches the packet. Retain that response for the same conditions; another culture survey is not required.

A proposed live editorial clinic, with qualified facilitation and materials already available, would let contributors clarify difficult objections together and finish in one day. A volunteer objects to making common attendance a condition of having evidence considered. This is a concern about contribution and decision relations, not evidence of deficient motivation. Under the supplied bylaws, packet preparation requires specified qualified inputs and an editor's acceptance, not attendance by every contributor; the formal ballot remains separate. Both a facilitated clinic and separate submissions are lawful and available. The current question is one corrected packet within five working days, with the same technical review and evidence protections.

The following illustrative estimates are total person-hours for that packet. They include the necessary selection work, participant work, support and follow-up; they are stipulated case inputs, not measured effectiveness of either school.

| Work through receiving use | Competent live clinic | Retain the prepared asynchronous practice |
| --- | --- | --- |
| Clarify this packet and compare responses; confirm authority, protection and availability; prepare its permitted evidence | 6 | 6 |
| Contributors prepare questions and participate, including the clinic's waiting time or separate exchanges | 10 | 4 |
| Editorial facilitation, qualified translation and response routing | 5 | 11 |
| Correct the packet and inspect receiving use and burden | 3 | 3 |
| **Whole work** | **24** | **24** |

Both alternatives have the same nine hours of shared work; it is included once per alternative. The clinic finishes in one day; separate exchanges take three. The editor and support providers confirm that the extra six hours are available by postponing optional index maintenance; participants accept their individual windows. They and the publication owner choose the asynchronous practice: it moves six hours of burden away from contributors while accepting six more support hours, the postponed maintenance and slower response. It saves no total work. The objection changes the proposed organization design: separate qualified contributions can reach the accepting editor without a universal-attendance condition. A competent implementation team can make this same revision; OCE adds no second intervention to its sufficient result.

If the packet becomes due in one day, that choice no longer meets the receiving window. Reconsider the clinic with the actual participants, translation and protection conditions, or return the deadline problem. Do not demand commitment to an unavailable arrangement. Later peer use can support a narrow observation about this participation practice; these packet results do not establish a culture change across the association. Missing bylaw or publication decisions still stop their dependent action, and the association gains no authority over employer time or protected evidence.

### OCE.10:6 - Bias-Annotation

Sponsor-centred inquiry can turn valid objections into resistance. Fear of consequences can make reported agreement unreliable. Use several relevant perspectives, protect dissent and compare accounts with work evidence. Do not infer a capability deficit, personal motive or group culture from one visible non-use.

### OCE.10:7 - Conformance Checklist

- The gap concerns a concrete contribution and receiving work, not only an attitude label.
- Rival explanations that change action have been considered and uncertainty remains visible. A new contrast is selected only for a worthwhile attainable contribution, including design effort, delay and displaced work; a response supported across the rivals can finish without it.
- A sufficient current response is used directly. Any remaining intervention has a supported mechanism, suitable Method, owner, protection and stop; its comparison includes whole participant and support work, later use and any accepted disadvantage.
- A claimed performed intervention uses actual observations of use, non-use, burden and receiving consequences. A recommendation, current continuation or selected probe is not reported as a newly performed intervention.
- A cultural claim includes transmission, recognition and later use within a named population and window.
- A stronger causal or professional claim is not inferred from a local participation result.

### OCE.10:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Better action |
| --- | --- |
| “People resist change; communicate more.” | Recover one episode and distinguish the causes that imply different repairs. |
| Commission training for an access, authority or workload defect. | Repair that condition and reassess the remaining human target. |
| Declare culture changed after a workshop. | Follow practice transmission, receiving consequences and later peer use. |
| Suppress objections to protect momentum. | Test whether the objection exposes a design, protection or contribution problem. |

### OCE.10:9 - Consequences

The practitioner can retain a sufficient response, develop the intervention still needed and stop an unsupported one. Participants gain a workable contribution and a way to raise valid concerns. A better fit for participants can require more support or slower completion; make that choice explicit. Inquiry, protection, practice and follow-up consume effort, and valid concerns may require changing the organization design itself.

### OCE.10:10 - Rationale

Participation arises in a working situation with capabilities, relations, interests and consequences. Changing only an explanation or a person's knowledge can leave the operative constraint intact. Cultural continuation adds a further question: whether others can learn and use the practice when the initial intervention is no longer carrying it.

### OCE.10:11 - SoTA-Echoing

The practice question is which participation response can support the needed contribution now. The selected line is to use sufficient competent participatory implementation directly, and to develop or obtain only its consequential remainder. Compare feasible responses under the same receiving conditions and whole work, retaining the determinant sensitivity and follow-up already supplied by competent implementation.

| Comparison and disposition | Pattern consequence, source limit and reopen condition |
| --- | --- |
| **Adopt and adapt** [Implementation Mapping](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2019.00158/full), Tasks 1–5, as a strong constructive line: participant involvement, action and change objectives, suitable strategies, prepared support and evaluation. Its sufficient result is the serious alternative to another OCE-led intervention. | Step 4.3 accepts that result without repeating its work. In 5.2, the prepared asynchronous practice and a competent live clinic each need 24 person-hours; the chosen response reduces contributor burden at the explicit cost of support, displaced maintenance and time. This is a conditional local choice, not evidence that OCE outperforms Implementation Mapping. Reopen for a changed receiving window, burden, support or protection. The [2025 scoping review](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2025.1603178/full) reports uneven application and evaluation; it supplies no ranking of these constructed alternatives. |
| **Use, with a boundary**, the [2025 CFIR guide](https://pmc.ncbi.nlm.nih.gov/articles/PMC12357348/) to select determinants and sources for a question that can change the response. It explicitly connects strategy development to participatory methods such as Implementation Mapping; use it for that determinant question. | Step 4.2 keeps the inquiry question and burden bounded; 4.3 uses an adequate existing response or obtains the actual intervention Method. More coded factors do not justify another intervention. Reopen only when an omitted or changed determinant can change the action or its warranted claim. |
| **Use a sufficient contribution from** current [ADKAR](https://www.prosci.com/methodology/adkar) or [Kotter's evolving accelerators](https://www.kotterinc.com/methodology/8-steps/). Ability and reinforcement, barrier removal and institutional continuation can already support the local participation task. Compare retaining that supported work with the proposed replacement or extra diagnosis, not with training-only or announcement-only caricatures. | Steps 4.2–4.6 retain useful support and add work only for a consequential unresolved question. If further diagnosis cannot change the warranted response, continuing that support is sufficient, as in 5.1. If a gap survives, count both alternatives' complete burden through use as in 5.2. The public descriptions bound this comparison: detailed professional techniques and comparative effectiveness remain unestablished. Reopen on a changed contribution, condition or observed consequence. |
| **Adapt bounded participant inspection** from the [sociotechnical-prototype experiment](https://doi.org/10.1016/j.apergo.2023.104012). Understandable representations can help participants inspect proposed work; whether cooperation improves must be observed in subsequent use. | Step 4.3 uses a concrete working case and participant co-design, then step 4.4 observes use. The experiment does not establish implementation effectiveness. Reopen when participants cannot understand or use the proposed arrangement. |

### OCE.10:12 - Relations

OCE.6 and the direct relation owners establish assignments, authority and enabling conditions. OCE.8 can reconsider a flawed Work arrangement. OCE.9 integrates the repaired contribution; OCE.11 addresses service/change burden; OCE.12 supplies and develops leadership contributions. OCE.15 and current Method Engineering qualify a new Method account rather than treating an intervention label as an admitted Method.

Current HCD.1/HCD.3/HCD.4 can supply demand, target-diagnosis and capability-profile results; missing learning, clinical or other professional results remain external. C.36 governs cultural relations, C.28 stronger causal use, and C.11.DUA appraisal of a questionable inquiry demand. OCE.17's OCE-discipline culture is a different subject, not a synonym for target-organization working culture.

### OCE.10:End

## OCE.11 - Coordinate Organization-Change Work with Continuing Service

> **Type:** Method pattern
> **Status:** Stable
>
> **Primary working result:** a bounded, authorized arrangement for change and continuing service to coexist, its observed consequences and hand-back, or an exact reason that no current coexistence is available.

### OCE.11:0 - Use This When

The organization must change while continuing to serve users, but learning, setup, dual operation or recovery compete with existing commitments. Use OCE.11 to make that overlap workable: identify the service conditions that must survive, account for the whole change burden, obtain the necessary decisions, operate a bounded change slice and recover before handing it back.

Begin with one impending collision in time, support or coverage. A vacant calendar slot is not evidence of service headroom. The first useful result can be a smaller change interval, retained support, deferred work or a stop at an unavailable service result.

This pattern concerns coexistence around an organization change. Its operating resource account can include assignments made under an unchanged authority structure: new work does not by itself establish organizational redesign. Conversely, a changed practice can need learning, support and new contribution relations even when job titles stay unchanged. Routine dispatch and case priority belong to Operations; a whole Work-arrangement comparison belongs to OCE.8; comparison of Method or candidate-account co-use belongs to ME.6. OCE.16 supplies the cross-change entry and per-change return when another separately managed change alters a needed condition.

### OCE.11:1 - Problem Frame

A change practitioner and the receiving service owner must agree what can change while current users still depend on the organization. A pilot may require the same scarce expert as live service. Training may consume recovery time. A temporary bridge may be removed before the receiving service owner can manage the new arrangement.

The governed move is to establish and operate a bounded coexistence arrangement. Describe its actual coverage, change exposure, support, interruption response and hand-back conditions. Qualify any whole-service capacity claim separately.

### OCE.11:2 - Problem

Change plans often count installation but omit learning, supervision, double entry, observation, exception repair, recovery and catch-up. The resulting plan allocates the same participant’s time or support resource twice.

An incident can then consume the assumed margin while the change continues unchanged. A nominal migration finish can retire support that another change or service still uses. Neither a milestone nor an approved document establishes that the overlap remains workable.

### OCE.11:3 - Forces

| Force | Tension |
| --- | --- |
| Continuing commitments | Users need service while the organization needs time to improve its ability to serve them. |
| Real burden | Learning and recovery are necessary work, not free overhead. |
| Limited exposure | A small trial reduces possible harm, but only if fallback and support are actually usable. |
| Several decisions | Allocation, admission, priority, service protection and change authority may belong to different owners. |
| Hand-back | Temporary support must eventually end, but ending it by date alone can remove a still-needed condition. |

### OCE.11:4 - Solution

#### OCE.11:4.1 - Recover the service that the change can disturb

Name the continuing contribution, receiving users, current commitments, operating configuration and interval. Ask the service owner for the applicable coverage, response, protection and recovery conditions and the evidence that supports them.

Identify the particular change contribution and the resources it can consume or interrupt. Do not substitute total staffing, average utilization or a free calendar for the qualified service result. When coverage under variability, a buffer policy or a service-credibility judgement is needed and not supplied, obtain that professional result before relying on it.

#### OCE.11:4.2 - Account for the overlap at the needed times

Begin with the current service/change arrangement. Competent release and operating practice can already cover limited exposure, participant load, interruption response, recovery and support hand-back. If its current result covers this contribution, receiving obligations, interval and protection, use it without constructing another coordination account.

Where a consequential gap remains, name the exact relation or interval whose answer can change the overlap: for example, who must answer a late challenge after a temporary support contribution is due to end. With the participating workers and service owner, extend a suitable existing account, or construct the needed account when none is suitable. Place the continuing commitments and complete change burden in the same relevant time and resource view. Include preparation, practice, coaching, dual operation, observation, extra review, exception handling, recovery, catch-up and hand-back. Count obtaining and keeping the needed account and any needed specialist returns current; that work also consumes the overlap.

Keep unlike constraints visible. A holder can have hours but lack the needed capability, authority or access. Another participant's free time may not substitute. A provider's availability can constrain the whole attempt.

Use the smallest representation that reveals the collision. A weekly allocation can suffice for one expert; a time-sensitive service may need shift-level or event-level conditions. Do not add unlike resources into one unexplained capacity number.

Use OPS.11.1 when the overlap requires reconstructing a network of transformations, resources and enabling conditions. Keep changes to the product route distinct from changes to who can request, promise or accept the result. Count the change work and its support beside continuing work wherever they occupy the same resource. Reuse an adequate operating model; this coordination method does not require another model of its own.

#### OCE.11:4.3 - Construct a bounded coexistence arrangement

Compare the competent current continuation with the proposed change on the same receiving result, authority, protected conditions and horizon through hand-back. Continued support or a qualified deferral can be a sufficient alternative. Use a current ME.6 co-use or OPS.19 operating comparison when it already answers this choice; do not rebuild it here.

For a remaining choice, compare the complete work in each continuation, not just the proposed trial. Include the account and specialist-return work in 4.2, enactment, learning, retained support, recovery and later receiving use. Count shared work once in each alternative; distinguish total effort from burden on a scarce participant, elapsed time and work displaced elsewhere. Choose an improvement without hidden loss at comparable whole effort, or the gain and disadvantage that the affected participants and responsible owners explicitly accept. An unavailable protection, assignment or authority is a stop, not a disadvantage to buy away. If the added work cannot change a worthwhile result, retain the sufficient continuation.

Combine the selected direct decisions into a workable overlap. Specify the service coverage to retain, the size and timing of change exposure, available practice/support, the bridge or fallback, the condition for reducing or stopping starts, and what the receiving service owner must obtain at hand-back.

For example, limit a trial to one package, place its protected learning interval where the qualified coach is available, retain the old evidence-return channel until its last consuming obligation ends or a qualified replacement can carry it, and defer further starts when an incident consumes the agreed margin. Each condition must have an effective owner and basis.

Do not repeat a comparison that another Method has already supplied:

- Use ME.6 for a material co-use choice involving Methods or candidate accounts, including changed order, support, allocation or burden when the Methods themselves stay unchanged.
- Use OCE.8 when the question is which whole arrangement should obtain the same result.
- Use OCE.16 when a separately managed change would remove a contribution, access path, authority or support interval needed here. Apply the returned direct result if it already answers the dependency.

If no arrangement satisfies the service and protection conditions, reduce the change, reschedule it, obtain different support, or return the decision to its authorized decision-maker. Do not make the plan feasible by silently assuming overtime or weaker protection.

#### OCE.11:4.4 - Obtain the decisions that make the arrangement usable

Before the dependent work starts, obtain the current service and change decisions, effective allocations and access, relevant admission or amended commitments, specialist protection results and recovery acceptance.

OPS.5–OPS.7 supply admission, case continuation and bounded priority or commitment decisions. OPS.8–OPS.13 and OPS.19 supply the applicable release, resource, capacity, human-condition, service and combined operating results. Use the result that answers the actual overlap question; request a missing professional result with its contribution, interval, operating conditions, basis for reliance and condition for reconsidering an unavailable input. A resource calculation does not confer authority or make a pending assignment effective.

Verify the operating conditions separately from approval of the change plan. Obtain another employer’s allocation from that employer and renewed officeholder authority under its applicable rules.

#### OCE.11:4.5 - Operate the overlap and respond to interruption

Observe service and change separately at the points that can change action. Compare actual work and support with the agreed conditions. When a signal is reached, reduce the change slice, stop new starts, use the qualified fallback or begin recovery under the applicable rule.

Treat a hard safety, rights, security or legal condition as a condition, not a spendable reliability budget. A service-specific trade-off requires that service's own rule and observations; borrowing software percentages does not establish it.

Record what actually happened. Deferred learning or a cancelled probe is not performed work. Failed attempts, missing observations, and unused reserve must remain visible rather than being counted as successful change outcomes. When an interruption invalidates a permission, access condition, support assumption or participant window, renew that input before restarting the defeated branch.

#### OCE.11:4.6 - Recover and hand back with explicit remaining obligations

Recover the affected service and re-establish the conditions required for restart before resuming the blocked change. Avoid charging the same recovery interval to both service restoration and planned change output. If the original arrangement no longer fits, return to the exact allocation, commitment or co-use decision.

At hand-back, obtain the receiving service owner’s acceptance of the actual configuration, support, capability conditions, open obligations and next reconsideration. Retire temporary support only when its agreed consuming obligations and replacement conditions are satisfied. An open obligation may pass to a qualified replacement under its effective assignment and support; transferring that obligation and closing it are different results. The owner can accept a bounded configuration while refusing removal of support that it still needs.

Return the actual overlap and service consequences, not merely the plan. An honest result can be “service recovered; the trial was deferred; this missing observation remains open”.

#### OCE.11:4.7 - Stronger assurance follows the receiving claim

Use the direct operating and professional governors for service capability, safety, fatigue, security, legal authority or reliability. A.10 governs the evidence used; C.11 governs a precise choice claim. If the account asserts dated Work, performer or transformation claims, qualify them through A.13, A.15.1 and the relevant change governor rather than inferring them from an allocation table.

For an ordinary bounded coordination decision, retain only the facts that change the allowed overlap, stop, recovery or hand-back. The Method does not require a portfolio office, a universal capacity model or a new record for every observation.

### OCE.11:5 - Archetypal Grounding

#### OCE.11:5.1 - PumpWorks: an incident consumes the change interval

This is a constructed continuation, not a completion of OCE.8's earlier reroute. Suppose trial authority, effective provider access, protection, a qualified manual fallback and the service owner's coverage/recovery result have separately been supplied for the bounded weekly-package experiment.

The service owner supplies the following forty-hour envelope for E27. It is a case input, not an OCE capacity formula. Other participants and provider support have their own qualified availability; E27's hours do not establish theirs.

| E27's weekly envelope | Normal planned week | Week with the constructed incident |
| --- | ---: | ---: |
| Continuing service | 24 hours | 30 hours, including 6 incident hours |
| Other accepted commitments | 6 hours | 6 hours |
| Interruption reserve still unconsumed | 4 hours | 0 hours |
| At most change-related work | 6 hours | 4 hours |
| Total envelope | 40 hours | 40 hours |

Learning, setup, extra review and debrief all consume the change allowance. The incident takes four reserve hours and two hours returned from change. The responsible owners reduce the planned change start and make the necessary OPS.5/OPS.7 admission or commitment dispositions. No overtime is assumed.

The service is recovered under the service owner's rule. The displaced probe remains unperformed and its observation missing, regardless of the milestone status. Before restarting, check current access, support and service conditions. If the incident exceeds the supplied recovery envelope, the four-hour change remainder is not automatically available.

During later bounded use, one provider-unavailable package uses the qualified manual return within its supplied service conditions. OCE.9 uses that observation only for its narrow organization-capability conclusion. OCE.11 returns the actual service consequence and the support/hand-back conditions; it does not declare general reliability from this episode.

#### OCE.11:5.2 - A retained support result is ready to use

Suppose repository consolidation would retire Electrical's evidence-return contribution before a challenged package is closed. OCE.16 identifies the consuming action and interval; ME.6 and the direct owners return a qualified retention arrangement through the last consuming package and a tested replacement.

Use that result in the coexistence arrangement: preserve the support interval, adjust the proposed retirement and carry the receiving obligation to hand-back. Do not open another comparison merely because a new repository option exists. If the result already answers the dependency, further inquiry that cannot change this use is unnecessary.

In a distinct pre-decision variant, no current return yet covers transferring that last obligation. The competent existing arrangement can keep Electrical's evidence-return contribution through Friday, close the challenged package and then retire the bridge. It already includes monitoring, interruption response and qualified recovery. A proposed alternative would transfer the remaining obligation to an available participant with the relevant preparation and retire the old bridge on Wednesday. The organizational remainder is who can obtain the old package's exact evidence and answer its challenge after that transfer, under which assignment, access and support interval. A successful trial on new packages does not answer it.

Both alternatives must close the same package by Friday, preserve the same continuing service and protection, and cover hand-back and an already committed five-hour diagnostic-library task by the following Wednesday. The responsible owners supply compatible participant calendars for either arrangement. The library task may use its preferred Thursday slot or an authorized following-Monday slot. These are constructed case premises, not general capacity results.

Unchanged continuing-service work and the same qualified interruption cover are held constant. The estimates below include all additional work through that common horizon, including obtaining and updating the needed account, professional returns and later use. They are stipulated person-hours, not observed savings or a forecast of every possible incident.

| Additional work through the receiving horizon | Retain the competent current arrangement | Transfer the remaining obligation earlier |
| --- | ---: | ---: |
| Common selection, service checks, package disposition, observation and recovery preparation, plus the five-hour library task | 10 | 10 |
| Obtain and maintain arrangement-specific facts and the responsible owners' returns | 1 | 5 |
| Additional preparation, coached practice and setup for the receiving participant | 0 | 5 |
| Bridge and receiving-participant support through Friday | 8 | 3 |
| Final hand-back inspection and support retirement | 1 | 1 |
| **Whole additional work** | **20** | **24** |

Under retention, Electrical supplies the eight bridge hours. Under early transfer, Electrical supplies two of the five preparation hours and one of the three support hours; the receiving participant supplies the remaining work in those rows. The five Electrical hours released from bridge work let the already-counted library task use Thursday rather than Monday. The service and support owners choose early transfer and the participants accept its allocations: they accept four more total hours to avoid that deferral. They do not claim a labour saving. A competent service/change team can produce the same relation within its existing method; use that result. The addition is useful here because it permits a different support retirement and work allocation.

The trial is nominally complete on Tuesday, but the receiving owner refuses the proposed unconditional hand-back: the receiving participant has so far handled only new packages, and the old challenged package remains open. The old route stays available. During the selected Wednesday preparation, the participant retrieves the exact old evidence under current access, works through its challenge and returns a usable response to the accepting owner. The owner checks that the effective assignment and supplied support cover further clarification through Friday. Only then does the owner accept that bounded transfer and permit retirement of Electrical's old bridge. The challenged package is still an open receiving obligation, now carried by the replacement. On Friday the package's authorized receiver accepts its disposition; the service owner can then end the temporary clarification support under the agreed condition. Neither Tuesday's trial result nor Wednesday's transfer falsely closes the package.

If the Wednesday qualification, access or support return is unavailable, early retirement stays blocked. Retention may still work, but reconsider the remaining work and commitments after any preparation already consumed; the original 20-hour estimate cannot erase that cost. If early release of Electrical no longer changes useful work and retention remains adequate, keep retention instead. An incident reopens the affected service and recovery conditions as in 5.1; its actual work must be counted, not hidden inside the no-incident estimate. A returned adequate retention or transfer result ends this choice without a fresh model or trial.

These decisions still do not establish provider access, service recovery or trial authority that they did not supply. If one of those is absent, stop its dependent action rather than reopening the answered retention question.

#### OCE.11:5.3 - Volunteer windows and an expiring chair

A standards association coordinates amendment preparation with current ballot and publication obligations. Members accept bounded volunteer windows under independent employers. The chair's term ends before a proposed binding decision.

The members and service participants negotiate the editorial overlap and protect publication support within their accepted volunteer commitments. Their agreement by itself changes neither an employer's allocation nor the chair's term. Return the authority question to Governance and stop the binding decision. Separately permitted editorial work can continue. Establish the successor’s authority under the applicable rules before resuming that decision; the project date does not renew the expiring term.

In a hospital, the equivalent service conditions include licensed competence, staffing/fatigue, medical safety and privacy. Obtain those results from the responsible professionals before a patient-facing trial.

### OCE.11:6 - Bias-Annotation

A change sponsor may count only visible project tasks, while a service owner may treat all existing demand as immutable. Recover actual commitments, displacement and hidden learning/recovery burden with the affected participants. Make deferred work visible without treating honest interruption reporting as poor performance.

### OCE.11:7 - Conformance Checklist

- Continuing users, commitments, configuration and protection/recovery conditions are explicit.
- An adequate current coexistence result is used directly. Any addition answers a consequential relation, interval or obligation, and its comparison counts account upkeep, specialist returns and whole learning, support, execution and recovery work through the receiving horizon.
- Required co-use, arrangement, admission and commitment decisions are obtained from their owners and not repeated here.
- Stop, reduction and fallback conditions change actual action.
- Interrupted or deferred work and missing observations remain visible.
- The receiving service owner accepts hand-back and the end condition for temporary support.

### OCE.11:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Better action |
| --- | --- |
| Schedule change in “spare” time without service evidence. | Obtain the coverage and recovery result for the actual interval and participants. |
| Treat learning and dual operation as free. | Include their burden in the same overlap view as service commitments. |
| Spend a hard protection condition as an error budget. | Use the governing professional limit; reduce or stop the change when it does not hold. |
| Recompare a dependency already answered by a current direct result. | Apply the result and retain only genuinely open inputs. |
| End a bridge because migration is nominally complete. | End it when its consuming obligations and qualified replacement conditions are satisfied. |

### OCE.11:9 - Consequences

The organization can reduce change exposure before it defeats continuing service, and can distinguish a recovered service from a completed change. A sufficient current arrangement can finish the coordination question. A justified revision may free a scarce participant earlier while requiring more total work elsewhere; the accepted allocation and timing trade-off remain part of the result. A stop can preserve the possibility of a later useful attempt.

### OCE.11:10 - Rationale

The coexistence problem is temporal and relational: who must provide which contribution while another condition is changing? Counting all burden and applying the direct owners' results makes that overlap inspectable. Observation and hand-back keep a once-credible plan from silently becoming an unsupported operating commitment.

### OCE.11:11 - SoTA-Echoing

The practice question is which work remains necessary to sustain service through this organization change and its hand-back. The selected line adopts sufficient competent service/change coordination and adds only a consequential missing organizational relation or interval. Compare the complete continuations at their full burden and preserve the sufficient incumbent.

| Comparison and disposition | Pattern consequence, evidence limit and reopen condition |
| --- | --- |
| **Adopt** bounded exposure, suitable observation and failure return from [Canarying Releases](https://sre.google/workbook/canarying-releases/), together with actual-load reconstruction, support hand-back and training investment in [Identifying and Recovering from Overload](https://sre.google/workbook/overload/). These primary SRE treatments already supply serious service/change coordination. | Step 4.2 uses an adequate current result without another account. In 5.2, retaining the bridge needs 20 additional hours; the 24-hour transfer is selected only for its explicit earlier release of Electrical and accepted extra burden. That constructed choice establishes no empirical ranking of OCE or SRE. Reopen when the receiving obligation, participant window, support or useful timing difference changes. |
| **Reuse** ME.6 for the actual co-use choice and applicable OPS results for operating admission, allocation, capacity and service. OPS.11.1 constructs a needed operating network; OPS.19 already requires sufficient-account reuse and exact additions with their upkeep cost. | Steps 4.2–4.4 consume the result that answers the overlap, not the whole repertoire. In 5.2, the addition binds the final package's obligation to its qualified receiver and support interval; it does not duplicate the supplied comparison. Hand-back in 4.6 can accept that transfer without pretending the obligation is closed. If the same relation is already covered, reuse it; reopen only the changed premise. |
| **Adapt within its scope** the service-sensitive stop, exception and escalation choices in the [Example Error Budget Policy](https://sre.google/workbook/error-budget-policy/). Reject treating its software percentages or rollback assumptions as protection permission for people or physical systems. | Steps 4.3–4.6 retain direct service and professional conditions. The forty-hour case uses its supplied envelope and leaves the cancelled probe unperformed. The three SRE references are 2018 operational treatments, not a claim about a universal current policy, guaranteed effects or a generally adequate reserve. Changed burden, recovery or protection defeats the dependent continuation, including the apparently cheaper one. |

### OCE.11:12 - Relations

OCE.9 uses the allowed realization interval and returns its observed support needs. OCE.10 can expose a participation consequence of overload or conflicting incentives; OCE.12 needs genuine time for leadership and learning contributions. OCE.8 owns whole-arrangement comparison. OCE.16 qualifies cross-change dependencies and returns direct results; ME.6 owns any required co-use comparison.

OPS supplies the operating focus, admission and commitment decisions, resource and service results, and the combined operating decision needed for the overlap. Use OPS.11.1 if constructing or reconciling its operating model changes that decision; otherwise reuse the available account. Direct professional owners retain service capacity, protection and recovery judgements outside the supplied OPS result. Coordinating the overlap does not create a missing result. OCE.13/OCE.14's wider organization observation and revision remain outside this bounded method.

### OCE.11:End

## OCE.12 - Distribute Leadership Contributions in Organization Change

> **Type:** Method pattern
> **Status:** Stable
>
> **Primary working result:** a leadership contribution performed in the change work, with a tested way to continue it, or an identified obstacle to performing or continuing it.

### OCE.12:0 - Use This When

An organization change needs somebody to explain its purpose, bring concerns into discussion, help people perform their roles, negotiate assistance or learn from a difficult episode. This contribution is missing or depends on one initiator. Use OCE.12 to obtain the contribution, develop any missing capability and arrange help for its next use.

Start by asking what someone needs to do differently and what help would make that possible. Choose a working conversation or another Method suited to the difficulty, and state the result it should produce. When advice conflicts with assigned work, use 4.2 to arrange the conditions that let people act on it. Use 4.3.2 when a discussion must construct a substantive result, 4.3.3 when a proposal needs preparation with trusted advisers and a workable start, and 4.4.1 when the change involves a career transition.

Leadership here is work that helps people coordinate their contributions and develop the capability to perform them. Facilitating a conversation, coaching a task and allocating work time may require different people.

Do not substitute a leadership conversation for a domain decision, clinical care or an employment action: involve the practitioner responsible and qualified for that work. If an adequate operating instruction already resolves the difficulty, follow it. Leadership help may come from a peer or mentor without managerial authority.

### OCE.12:1 - Problem Frame

People differ in their understanding of a change and in their concerns, attention, capability and circumstances for contributing. A formal assignment alone does not ensure that a difficult question is asked, assistance is obtained or a new skill is used successfully at work.

Obtain the contribution from people able to perform it, observe what it enables in the change work, and arrange its continuation. If it cannot continue, identify the unmet condition.

### OCE.12:2 - Problem

A person may be assigned a leadership title without anyone specifying the contribution they must make. One initiator may conduct every difficult conversation, leaving others dependent on their presence. A course may improve performance in an exercise without providing a safe workplace opportunity, feedback or help.

A mentor may encourage investigation while the manager assigns a full week of delivery and rewards only rapid closure. HR may offer development without knowing which future work can use it. A well-moderated discussion may collect everyone's views yet leave the needed explanation or proposal unbuilt. In each case, performing the named activity leaves another contribution missing.

### OCE.12:3 - Forces

| Force | Tension |
| --- | --- |
| Distributed contribution | Several people can contribute; their capabilities, authority and available time differ. |
| Role performance | People need to know their expected contribution; their concerns and aims may also affect how they perform it. |
| Capability development | Developing a capability and arranging its later use require different work; that use also needs help and observation. |
| Continuation | Continuation should not require the initiator at every episode, but other contributors may still need help. |
| Plural authority | A peer or volunteer can contribute without becoming anyone's subordinate. |
| Negotiated contribution | A feasible proposal may impose conditions or burdens that a participant cannot accept. Benefit alone does not establish consent. |

### OCE.12:4 - Solution

#### OCE.12:4.1 - Locate the contribution that is missing

Name the difficulty in the work that needs help. Examples include an unclear purpose, an unvoiced concern, confusion on entering a role, loss of attention to its expected result, a need to hand over or leave a role safely, incompatible contributions, and unavailable help or learning time.

State the expected contribution, where it is needed and what shows the difficulty. Ask the affected participants what help would change their next action. If someone lacks access to a needed resource, obtain that access; if a technical decision is pending, take it to the responsible decision maker.

Use OCE.10 when the cause of a participation gap is uncertain. Enter OCE.12 directly when the needed leadership work is clear.

#### OCE.12:4.2 - Select a contribution and capable participants

Choose a Method suited to the difficulty. Examples include a preparation brief, a huddle when the situation changes, a conversation about role performance, task-focused feedback, a debrief, inquiry with participants about the help they need, negotiation over incompatible contributions, and coaching or another intervention to develop the required capability. State the result it should produce and why it fits.

First look for a competent arrangement already available. If none can meet the need, identify the contribution still to be obtained and construct its arrangement through the steps below. A leader who obtains capable help, allocates work, listens to objections, changes the plan and checks the result may supply everything needed. Retain that work and its usable answers. A new mentor, negotiation round, training programme or record needs a remaining contribution to justify it; distributing leadership is not a requirement to replace effective help.

Compare the alternatives for the same receiving result over the period in which it is needed. Include the work retained in both, then the differing preparation, participation, representation, inquiry, qualified assistance, allocation, implementation, support and later checking. Include waiting and the work displaced from other receivers. Developing another participant may require more total work than continuing competent assistance, especially while that assistance remains available as a fallback. State the gain sought and whose added burden or delay is accepted. For example, the organization may pay that cost to obtain evidence of a second participant's bounded continuation, without claiming a saving or established capability before it is observed.

Choose only the addition warranted by that comparison. When the existing arrangement supplies the intended continuation, use it without repeating sufficient inquiry or training. When the added contribution remains uncertain, keep an adequate way to obtain the receiving result or defer the work that lacks support. State what observation would support continuation, further help or stopping the addition. Use 4.4 for development and 4.5 for the later work; use 4.3.1 when the changed contributions need agreement.

Obtain willing people with the competence and time to make the contribution. Distinguish the tasks of facilitating, providing domain expertise, making decisions, supplying resources, coaching and helping peers. Match each needed task with someone competent and, where required, authorized to perform it. A capable facilitator may lack the expertise to assess professional competence; a manager may allocate time without knowing how to coach the task.

When help requires a change in work, recover a representative task, the participant's aims, current instructions, time allocation and the way performance is evaluated. Identify who understands the work and who can change each condition. Specify the help as an action: demonstrate an operation, diagnose an error, give feedback, arrange practice, allocate work or judge a result. Combine the needed contributions into a workable arrangement. OCE.4 helps design their relations; OCE.6 establishes the assignments, access and authority needed to act. Use OCE.5 only when a continuing position must be established or changed.

A mentor without managerial authority can explain, demonstrate and critique. If acting on that help requires different assignments or evaluation, obtain those changes from the people who control them. Include displaced work and its receivers when reallocating time; use 4.3.1 if the demands must be negotiated. If the manager already supplies the needed help competently, an additional mentor title may add nothing. If the manager cannot teach the task, obtain capable help. Where the existing conditions already permit useful assistance, arrange it directly.

Secure people's agreement to participate and the protection needed for candid discussion. For peers and volunteers, confirm who can commit their work time and what they have agreed to do. Permission to facilitate gives no right to demand protected information or make another professional's decision.

#### OCE.12:4.3 - Perform the working conversation

Choose the smallest conversation that can produce the needed result.

**Before shared work, conduct a brief.** State the intended result and current conditions. Ask participants to explain their contribution and its limits; identify missing capability, access, time or help. Agree how to raise an objection, report an exception and obtain help. Confirm who can make each decision. Close with the next contribution and the conditions that would stop or change it.

**When the situation changes, conduct a huddle.** Bring forward the new fact and the affected contribution. Reassess the immediate work, burden and help with the relevant participants. Take decisions about allocation, priority or authority to the person authorized to make them.

**For role performance, work with the participant.** Clarify the expected result and limits of the assignment, and check the participant's understanding of them. Discuss how the person's aims and concerns affect the contribution. Compare observed work with the expected result and assignment limits. Help the person enter the role, maintain attention on its contribution or arrange a handover. Follow the applicable assignment rules and safety requirements when the person leaves or hands over the role. Agree one next contribution or a specific repair and obtain feedback from that work. Difficulty performing a role is insufficient grounds for a judgement about the person's personality.

**After an episode, conduct a task-focused debrief.** Reconstruct what happened from the work and evidence. Ask what helped, what failed, which explanation remains uncertain and what should change next. Agree who is responsible for the repair and how its effect will be observed. Protect participants who report error. Keep disciplinary decisions and clinical care with the responsible practitioners.

For a conflict between contributions, make the incompatible requests explicit, with the evidence, consequences for participants and authority needed to change them. A short conversation may settle a limited change: obtain acceptance from those whose work or conditions would change, and take any remaining decision to its responsible decision maker. Use the branch below when a mutually acceptable arrangement still has to be constructed. Agreement to discuss the conflict is only the start of that work.

##### OCE.12:4.3.1 - Obtain an agreement on incompatible contributions

The immediate result is agreement on who will contribute what and under which conditions, or a specific unresolved condition or refusal. Use this branch when cooperation requires an agreement that has not yet been reached.

**Prepare participation and the means to negotiate.** Obtain willing participants, time and a safe way to raise objections, consult represented people or decline a proposal. Identify those affected by the proposal, those able to provide its contributions and those authorized to commit them. A representative needs a mandate covering the proposed change; where it is missing, obtain the represented party's response before treating the contribution as agreed. Include people whose existing work would be displaced, even if they were absent from the first meeting.

Choose a negotiation Method that the participants can use, with a competent facilitator when needed. For example, the [CBI Mutual Gains Approach brief](https://www.cbi.org/assets/resource/media/cbi-mgabrief-2023.pdf) explains how to prepare around interests, mandates and alternatives, develop combinations of terms before commitment, discuss reasons for sharing costs and benefits, and arrange follow-through. A team already using the voluntarily adopted protocol described in CB.13 can continue with it under its stated conditions. Confirm that participants can perform the selected Method; obtain qualified help or develop the needed capability under step 4.4, allowing for its time and cost.

**Recover the condition behind each objection.** Ask which needed result the proposal would prevent or which protected condition it would violate, and what observation or change could answer the concern. Distinguish a required outcome from an assumed means. “The complete interface must be ready by day 20” may combine a need for daily data with an untested assumption that automatic control must arrive in the same release. Confirm this interpretation with the party that set the requirement; only someone authorized to change it may relax it.

Choose the work that can answer the objection. For a disputed technical possibility, obtain evidence from a qualified specialist. An assumed necessary means can be reconsidered with B.5.QD.CF. A dispute about consequences may need D.4 to examine different value premises and develop alternatives. Obtain a missing mandate from the party entitled to grant it. Establish what information participants may share and keep protected information confidential. A relevant condition that is withheld or unknown remains unresolved.

**Construct and investigate whole proposals.** For each condition, ask what else could supply the needed result: change the proposed scope, timing, performer, support or distribution of burden. Combine compatible changes into an arrangement that each party can assess, while retaining the applicable technical, safety and institutional constraints. Explore proposals before asking for commitments. Include what each party can feasibly do if no agreement is reached; refusal can remain preferable to an unsupported commitment.

When acceptability depends on an unknown, formulate the question that would change the choice and obtain the contribution needed to answer it. A proposed read-only release may need an engineering probe and an offer of support from the provider. Agree the probe's question and cost. Before doing it, assess how conducting it could affect participants and ongoing work, agree the conditions needed to protect them, and obtain the required permission. Permission for the probe does not authorize introduction. Return the evidence with its limits. Then revise the whole proposal: a support offer can change price, local workload and displaced work as well as technical feasibility. If the probe rules out the release, revise or reject that option.

**Make the burden and terms discussable.** Show what each participant would receive, provide, pay, defer or risk under the same proposed arrangement. Use reasons the parties can examine, such as measured support demand, protected service capacity and the value of the first usable result. Let them question both the estimates and the proposed distribution. Agreement on how to compare proposals may help, but a favorable combined score does not establish a party's acceptance.

Estimate the effort and cost of preparation, representation, consultation, facilitation and subject inquiry. Include waiting for replies, implementation, continuing support, monitoring and possible renegotiation; identify the work these activities displace. Resolve contested allocations with the people authorized to decide them. If investigation or negotiation would exceed its authorized effort, obtain a revised allocation, reduce the question or stop.

**Obtain acceptance of one complete version.** Present the revised scope, contributions, limits, timing, resources and change conditions together. Ask each party, directly or through an authorized representative, whether they accept their contribution and conditions in that arrangement. Distinguish acceptance, conditional acceptance, refusal and an unanswered question. A condition such as “only with funded support” is not satisfied by agreement to seek funding. If an amendment changes another participant's burden or benefit, return the same amended version to the affected parties; consult the represented people when the mandate no longer covers it.

Keep the accepted terms and remaining questions usable by those who must act. Silence, attendance and a majority's preference do not establish mutual agreement. Where a party refuses or a necessary condition remains unmet, identify what prevents agreement. The parties can revise the proposal or leave it unagreed. An authorized decision without mutual consent, where available, needs its own grounds and should be presented as that decision.

**Return the result to the receiving work and revisit changed conditions.** Give those responsible for the work that requested cooperation the accepted contributions and conditions, or the unresolved issue. When the agreement concerns an engineered product and the organization that provides it, use OCE.7 to coordinate the product and organization architecture decisions through their constraints and required contributions, with each decision made under its own authority. Use the agreed terms and remaining uncertainty in SYSE.6 when deciding the engineering architecture, or in SYSE.24 when choosing how to obtain an engineering result. Where a promise is being established or changed, use OPS.13 to establish its accepted terms. Agreement alone supplies neither technical evidence nor permission for introduction, and does not establish that the work has been performed.

Agree how a consequential change will reach the affected parties and who will obtain their responses. If promised support disappears, identify which accepted contributions depended on it, obtain feasible replacements and return the altered whole for acceptance. Keep independent results whose conditions still hold. If no replacement supports the proposed use, return the dependent choice to its decision maker, the unmet support need to the person responsible for arranging it, and any affected promise to the party authorized to change it. Until an authorized revision occurs, the existing commitment still applies.

##### OCE.12:4.3.2 - Construct a usable result in a facilitated discussion

Use this branch when the discussion must produce an explanation, design or proposal on which subsequent work will depend. Begin with its receiving question. For example: can the modules work together under the agreed load, and what supports that answer? State what the receiver must be able to decide or do with the result. Then choose a way to construct it and obtain the people able to perform that work.

Recover the relevant objects, claims and relations. For the module question, distinguish claims about individual modules from claims about their interaction. Identify the configuration each claim concerns, its supporting observations and the conditions under which they apply. Ask the specialists to examine the dependencies: does one module's output meet the other's input requirements, and do the separate tests exercise their joint operation? Combine the answers into an explanation of the proposed whole. Two successful component tests can still leave an interaction unsupported.

Work through a missing or disputed relation with the contributor who can resolve it. Evidence from an earlier configuration requires an applicability judgement; an untested interaction may require a joint test, a narrower claim or a revised design. Develop those alternatives far enough that the receiving decision maker can compare their consequences. Retain uncertainty when the needed result cannot yet be obtained.

An integrator constructs the connected account with the domain specialists. A facilitator can perform this contribution too when their competence supports it; otherwise arrange for someone who can. Facilitation helps participants hear objections, inspect evidence and work together. It does not make their separate statements into a justified whole merely by collecting them.

An agenda or canvas can help expose gaps; follow the reasoning the problem requires. Before relying on the result, trace the receiving decision through the explanation, and change one consequential condition to see which conclusions or actions must return for reconsideration. If participants can only repeat their individual views, obtain the missing construction or domain contribution. Another round of speaking turns may leave the same gap.

Apply the receiving-use question to coaching as well: which later action should improve, how will the proposed help address the observed difficulty, and what observation could show that it did? A reflective conversation can supply that help. An assignment conflict still needs a work-allocation decision, and a technical uncertainty still needs the relevant professional answer.

##### OCE.12:4.3.3 - Prepare a proposal for decision and first use

Use this branch when people need to examine a proposed organizational change before committing to it, or an agreed change has yet to become a workable first contribution. Begin with the result another person will use. Follow how the proposed practice would produce it: which working product changes, who prepares and receives it, and which tools, access, learning or help must be available. Retain an adequate existing arrangement. A short brief may suffice when the proposal and conditions are already settled.

**Bring the needed judgement into preparation.** Ask the decision maker and affected participants whose advice they need to assess the proposal and which question that person could help answer. A trusted former colleague, peer or specialist outside the formal project may influence the decision. Offer an appropriate explanation or permitted example through an agreed contact; let the recipient consult privately when that is preferable. Seek the grounds of the returned concern, including what would answer it. An adviser may clarify a consequence without speaking for the people who bear it or having authority to commit their work.

Concentrate on advice and affected interests that could change the decision. A credible technical objection needs the relevant specialist's answer; a concern about burden needs examination of the work and its receivers. When a material question remains confidential or inaccessible, agree a narrower way to examine it or retain the uncertainty. Exhaustively discovering everyone's informal contacts is neither necessary nor a condition for proceeding.

**Make the proposed work and its consequences examinable.** Explain how the proposed arrangement would produce the needed result and compare it with the present way of working. Use one representative task, its working products and the receiving decision. Let participants expose extra operations, missing inputs, displaced work and consequences they cannot accept. Separate a misunderstanding from a true disadvantage or an unsupported promise of benefit. Repair the explanation through dialogue, obtain the missing domain answer through 4.3.2, or revise the proposal. An understood proposal can still be declined.

Discuss the contribution and its conditions far enough to know what must be done before bargaining over personal appointments or titles. Include actual competence, authority and available resources whenever they change feasibility; postponing those questions would conceal a defect. Examine consequences for both current service and the change work, using OCE.11 where they compete. Preparation itself needs time for explanation, consultation, trials and revision. Use an adequate answer already available; limit new inquiry to a question whose answer can change the decision enough to warrant that burden.

**Obtain a decision on a workable proposal.** Where contributions conflict, use 4.3.1 to construct and obtain agreement on the whole arrangement. Identify who can authorize its start and commit each required contribution through OCE.6. If the participants cannot commit a needed resource, take the proposal and its unresolved condition to the person who can; keep the dependent start conditional. An institutional rule may permit a decision despite disagreement. Name that rule and retain the objection instead of reporting mutual consent. When a refused voluntary contribution is necessary, obtain an acceptable alternative or leave that use unagreed.

Keep responsibility for organizing the change distinguishable from responsibility for running and receiving the resulting work; one person can hold both when the arrangement permits it. Make the effective decision, its scope, timing and conditions recoverable in the form the organization uses. A promise to find time or support later leaves that condition outstanding. Authorize only the preparation, trial or use whose conditions are satisfied; retain an unresolved issue, refusal or deferral where they are not.

**Make the agreed start mutually visible.** Give the people whose actions depend on one another the same accepted proposal and effective decision. In a brief or a suitable shared exchange, let them confirm their contribution, the help available and how an exception will reach someone able to respond. Each needs to know what the others have actually undertaken, including the arrangements for an absent shift or provider. A readable update with the necessary responses can supply this result without a launch meeting. Attendance or silence leaves an unconfirmed contribution unresolved.

Use this exchange to confirm what is settled and expose what changed. A new substantive objection returns to the affected inquiry, agreement or decision; an announcement cannot close it. Identify which work must wait and which preparation can continue under its own conditions. When a revision changes another person's work or reliance, obtain the affected response and communicate the resulting version before that use. Existing commitments remain effective until their authorized change.

**Obtain the first useful handover.** Put the working product, access, permitted help and receiving contribution in place. When a checklist supports the occasion, [CHK.3](CHECKLIST-PRINCIPLES-FRAMEWORK.md#chk3---fit-a-checklist-to-its-occasion-of-use) locates its questions where observations and answers can change the work. Use the subject practice's criteria to produce and check the result; give the receiver the applicable result and unresolved questions. Follow what the receiver can actually do with it. Opening a form or reporting agreement leaves that handover untested.

Arrange a first assisted use when assistance is needed, and retain that condition in the result. A failed attempt may reveal a missing explanation, unavailable means or an unworkable arrangement; return that difficulty to its supplier rather than repeating the announcement. Use OCE.9 when the question is whether the organization can provide the whole capability, and CHK.3 for ordinary later use of the aid. One successful handover can justify its bounded continuation without establishing independent performance, recurring provision or usefulness across the organization.

#### OCE.12:4.4 - Develop the missing contribution capability

When capability is missing, give a qualified learning provider the target: who needs to perform which contribution, in what later situation, under which conditions and with what evidence of useful performance.

Obtain a learning design for that target. It may combine a demonstration, observation of a competent colleague, practice in performing the contribution in a difficult situation, feedback against stated criteria and later use without coaching. Have the provider explain how the chosen activities address the target.

Use [HCD.7](HUMAN-CAPABILITY-DEVELOPMENT-PRINCIPLES-FRAMEWORK.md#hcd7---arrange-providers-access-tools-and-ai-support-for-human-capability-development) to establish whether the proposed provider can supply the particular help with the needed preparation, time, access and assessment. Examine a representative learner difficulty: can the mentor demonstrate the operation, recognize the relevant error and give useful feedback? Agree how practice observations may be used and who may receive them. Obtain capable help, prepare the provider through suitable learning or revise the arrangement when that contribution is unavailable. A mentoring title or an available meeting slot does not establish it.

HCD.1 helps establish what the person's later work requires. HCD.3 helps identify a changeable human limitation supported by evidence, or return the question for a different remedy or missing evidence. HCD.4 helps build a capability profile across the person's simultaneous work. Obtain the learning, assessment and transfer Methods still needed from competent practitioners. An assessment of one episode supports only the capability claim its conditions and evidence justify.

With the people responsible for workplace assignments and resources, obtain protected practice time, usable tools and information, a task in which to use the capability, feedback and support. If people are penalized for making the contribution, use OCE.10 to investigate the cause or take a known adverse condition to the person authorized to change it.

##### OCE.12:4.4.1 - Connect a career transition to the work it should enable

Use this branch when the organization change calls for a person to take on different work. Start with the person's intended direction and plausible receiving work. With those responsible for that work, recover its expected results, constraints and needed contributions from representative cases. HCD.1 establishes capability demand; a future job still under design supplies a demand hypothesis. HCD.4 relates that demand to the person's supported capability and consequential gaps across their work.

Bring the development and work decisions together. HR can supply shared personnel policies, access to learning and work with the employee community. Line managers or other work owners contribute knowledge of their actual jobs and processes, opportunities for practice and the assignment decisions within their authority. Establish who controls the receiving work when the present manager does not. In a matrix or across employers, recover these relations from the actual arrangement.

For a proposed course, have the work owner identify the later task and what suitable performance would look like. A capable learning practitioner examines whether the teaching, practice and assessment address that task. HR can arrange access and procurement under the applicable rules. An administrator's preference for an attractive or familiar presentation does not settle its instructional value; complexity does not settle it either.

Construct a development path together with a realizable work opportunity. Obtain protected practice and feedback under 4.4, the receiving owner's conditions for a trial or appointment, and a feasible change to current work under 4.2. A capability profile informs the decision; it does not appoint the person. Preserve the person's aims and the agreed limits on using learning observations in employment decisions.

If no receiving work is available, retain worthwhile learning while keeping the career transition prospective. If a place exists but the required capability is unsupported, obtain the needed development or change the proposed assignment. Sending the whole problem to HR, the current manager or a coach leaves it unresolved when that person cannot supply the missing contribution.

#### OCE.12:4.5 - Arrange continuation without dependence on one initiator

Agree the time allocation and the help needed for the next contribution. As needed, arrange peer help or coaching, provide working examples and name someone to contact when a difficulty exceeds the participant's capability or authority. Record what the next participant needs to perform the work.

Observe a subsequent episode. When independence from the initiator is the claim, let another capable participant perform the contribution without the initiator doing it for them. Retain the help still needed. Rotate the contribution only when the next person is capable and willing, the agreed protections are in place, and any necessary authorization has been obtained.

According to the problem observed, ask the learning provider to revisit the person's target, the people arranging workplace support to repair it, the person responsible for the affected tool to redesign it, or a Method specialist to qualify or revise the Method.

#### OCE.12:4.6 - Return the enabled contribution and its limits

State what the leadership work enabled in the receiving episode, which needed contributions still lacked capable people or help, what the next episode showed and which assistance was still present. For any claim about agreement, performed contribution, capability or cultural continuation, state what required evidence is available and what is still missing.

Use OCE.10 to examine how the target working culture recurs. Use OCE.11 when the contribution competes with operating service for resources. When the leadership Method needs qualification or revision, use OCE.15 to specify the organization-change contribution and Method Engineering to qualify the proposed way of doing.

Ordinary use can be a brief conversation and an observable next action. Assessing capability requires the relevant professional evidence and A.2.2; a causal-effect claim uses C.28, and a claim about cultural continuation uses C.36. For a precise claim about a dated Work occurrence, establish the performer basis under A.13 and the occurrence under A.15.1. Ground that claim in evidence of performance, not only a participant roster or written plan.

### OCE.12:5 - Archetypal Grounding

#### OCE.12:5.1 - PumpWorks: distributed help around a disputed trace

This constructed example uses the authorized probe, access, service coverage and recovery conditions stipulated in OCE.9.

Before preparing an inspection-evidence package, E27 and a peer from Electrical conduct a brief. They identify the source revisions needed to support the package's claims, distinguish tool-proposed links from checked links, identify who can raise a question when a required source is missing, and confirm that Safety accepts or returns evidence while release requires a separate decision.

The first rehearsal exposes an ambiguous version cue. During a protected debrief, E27 shows the ambiguous labels for the old and current revisions. Using the displayed labels, the Electrical peer explains how a recipient could mistake the obsolete revision for the current one. They give the person responsible for the tool's version display a repair request and arrange another observation.

Contributors supply the conditions for practice and later use:

| Needed contribution | What is supplied |
| --- | --- |
| Protected learning opportunity | The line manager obtains time for practice while preserving the agreed service coverage. |
| Difficult challenge practice | A qualified coach demonstrates the conversation, observes varied practice and gives feedback against stated criteria. |
| Acceptance boundary | Safety explains which evidence it can accept or return; release remains with the person authorized to decide it. |
| Incident effects on service and change work | The service liaison explains how an incident would affect service and when change work must be reduced. |
| Peer continuation | E27 and a capable peer retain a useful example and a way to obtain help for the next episode. |

In a later episode, the peer conducts the brief and raises a missing-source question without the initiating facilitator doing so. The person responsible for supplying the source investigates, and the group follows the agreed way of returning unsupported claims. The continuation works in that constructed episode with its retained support.

A professional capability assessment remains with the learning provider. Use OCE.9 to judge the bounded organization contribution and OCE.10 to examine recurrence and recognition. The episode does not establish enduring culture, general leadership capability or causal effectiveness.

#### OCE.12:5.2 - A mentor who is not a manager

In this constructed member-governed standards association, three editorial discussions are due over six weeks. Each must return the disputed claim and its grounds, a restatement confirmed by the participants, and the evidence question for a qualified member to answer before the editorial decision. In a preliminary attempt at these steps, the prospective facilitator substitutes their preferred wording for an objection; the experienced colleague restores the objection with its author. That attempt can be completed with the colleague's help, but the member cannot yet be relied on to perform the restatement step. The association also expects this work to continue as volunteers rotate. It would value evidence that a second member can conduct these discussion steps with the agreed specialist help, but the three current discussions must not depend on successful learning.

An experienced colleague can lead all three. This is a competent current arrangement: the colleague prepares with the participants, confirms the available time and expertise, conducts the discussion, obtains task assistance when needed and uses feedback to adjust the next occasion. The source check and the chair's decision remain with their qualified or authorized performers. All three dates and support commitments are available. If these three results are all the association needs, this arrangement is sufficient; no development episode is required.

The alternative retains that arrangement as a fallback and prepares a willing member to lead the bounded discussion. The experienced colleague also agrees to mentor this development. Both alternatives include preparation of the actual cases, the three discussions, participants' consultation, the qualified source checks, editorial decisions, access, scheduling, ordinary feedback and follow-through. The development alternative adds the mentor's preparation of varied practice, the learner's practice and feedback, an observation on a new case and observation of the later editorial contribution. The experienced colleague's agreed availability is retained for these six weeks, so the comparison credits no saved colleague time. The chair and participants must also arrange the additional volunteer time and any employer permission; work displaced from another receiver needs that receiver's agreed accommodation.

Here the learner and mentor accept that extra work, and the chair confirms feasible opportunities and support without delaying the three editorial dates. They choose the more demanding alternative to obtain bounded evidence for local continuation during volunteer rotation. This is an accepted development investment, not an efficiency result: its benefit depends on the later observation, and capability for a later quarter remains unestablished. If the association values only the current discussions, cannot provide the extra time, or already has adequate evidence of another member's capability, it retains the competent current arrangement or uses that member directly.

The learner observes the qualified colleague, then practises facilitating a difficult disagreement with that colleague's feedback. Using HCD.7, they establish that the mentor can diagnose these steps and has time for the preparation, observation and feedback as well as the retained facilitation. The arrangement must fit the weeks when those demands overlap. The mentor and learner agree what can be inferred from the observations and how they may be used.

On a new practice case, the mentor observes those steps without giving prompts. The participants confirm the restatement and the question to investigate. This is evidence that the learner can perform those steps in the conditions observed. The pair uses it to plan a comparable editorial discussion with the mentor available for help.

The facilitator takes on that discussion under the association's agreed volunteer commitments and bylaws, with access to the evidence being discussed. In the editorial episode, the facilitator helps the members frame a question about whether a cited source supports a disputed clause. A member qualified to assess the source agrees to perform that check and return the findings for the editorial decision. The elected chair retains the decisions reserved to that office within its current term and remit.

If the learner cannot restate the objection accurately or needs the mentor to form the inquiry question, the mentor identifies the missed step and the help still needed. The editorial discussion proceeds with the capable colleague leading or with the learner receiving that help. The association compares further targeted practice with retaining this sufficient assistance; it does not authorize another learning episode merely to complete a programme. If practice is chosen, obtain its time and help. If the mentor's promised availability is withdrawn, recover a qualified contribution before relying on the learner or revise the affected date through the chair. The earlier learning observations remain useful, but the proposed continuation no longer has its stated support.


The association requests any missing permission to use evidence from the party entitled to grant it. A participant who needs employer time obtains the employer's agreement. The group defers or revises only the work that depends on an unavailable permission or time allocation.

When applying OCE.12 in a hospital, obtain the applicable clinical and patient-safety permissions, comply with staffing and fatigue limits, and ensure the required privacy protections are in place. Training grants no permission for patient-facing work.

#### OCE.12:5.3 - Agree a first interface and return when its support disappears

This constructed engineering case concerns a new interface to an operating service. The customer requests the complete interface by day 20. The engineer cannot obtain the evidence needed for automatic control before day 28. After protecting the old service, support has sixteen hours weekly available for change, eight of which are already allocated to an internal improvement. These conditions leave a promise of the complete interface by day 20 unsupported.

A capable facilitator works with participants who agree to explore a joint proposal but have not adopted the CB.13 team protocol. The customer representative can accept a reduced first scope and expenditure. The service owner can allocate change time while preserving old service; the improvement owner must decide any displacement. The engineer provides technical judgement and the provider commits the support it supplies. Operators contribute the conditions for using the interface. Their participation and consultation time are allocated before negotiation.

The facilitator asks what would fail without the complete interface on day 20. The customer confirms that the first necessary result is usable daily data without interrupting production; automatic control is desirable but need not arrive then. The support team objects that an unspecified temporary interface could consume capacity needed by the old service. The engineer retains the evidence constraint. These answers expose an alternative worth investigating: a limited read-only first release with a defined support arrangement.

The parties consider three proposals. Full automatic control on day 20 lacks evidence. Postponing every useful result is unacceptable to the customer. The read-only proposal needs evidence of technical feasibility and an offer of support. The participants authorized to fund the inquiry pay for a bounded technical probe and request a provider offer; this preparation is additional to the implementation price. The probe asks whether the limited configuration can return the required daily records without sending control commands or interrupting the old service. Its conditions and authority cover the inquiry, not production use.

In the stipulated outcome, the qualified engineering team obtains the required records and confirms those isolation conditions in the permitted probe. The result supports the limited read-only configuration within the examined conditions. The provider offers six weeks of support for 15,000 currency units, requiring twelve local hours weekly. The revised proposal gives the customer the read-only first scope on day 20, subject to the separate introduction decision; automatic control awaits a later decision with its own evidence. The proposal includes the provider's six weeks, twelve local hours each week, protected old service and reconsideration by the affected parties if support changes. The proposed agreement covers those six weeks of limited use; continued use needs a further supported agreement. It promises no automatic-control date merely because day 28 is the earliest evidence date.

The service owner can supply twelve hours only by taking four of the eight hours assigned to improvement: eight unallocated plus four displaced gives twelve, leaving four for improvement. Over six weeks that displaces twenty-four hours. The improvement owner explicitly accepts that loss. The customer accepts the reduced first scope and expenditure; the provider accepts its support terms; the service owner accepts the twelve-hour allocation with old service protected; the engineer confirms the limited technical basis. Operators confirm the proposed reading task and operating conditions within their authorized work. Each party responds to the same complete version, including the displaced improvement work and the support limit. The case stipulates these acceptances; the probe supplies the engineering evidence. If the customer instead retains full automatic control by day 20 as a non-negotiable condition, this proposal remains unagreed.

The result gives the product and organization decision makers coordinated conditions for use with OCE.7, the engineering decision maker a supported limited alternative, and those responsible for promises accepted terms for use with OPS.13. These participants must still obtain separate permission for introduction and perform their contributions. Preparation and consultation, the probe, reply delays, implementation, monitoring and possible revision remain costs of the whole arrangement in addition to the quoted support price and local hours.

Now the provider withdraws before introduction. Replacing its contribution locally would require thirty-six hours weekly against sixteen available even if all improvement work were displaced. Another provider can begin only on day 27. The customer refuses that delay. None of these alternatives supplies an agreed, supported day-20 introduction. The facilitator returns the changed proposal to the affected parties. The engineering decision maker reconsiders the first configuration; those arranging support revisit its provision, using OCE.7 to coordinate product and organization decisions; the party responsible for the existing promise uses OPS.13 to obtain an authorized response to the customer. Permission to proceed cannot rely on the withdrawn support. The independent probe result and the protected old service remain useful; the earlier promise has not been automatically cancelled.

#### OCE.12:5.4 - Make mentoring usable in an employee's working week

In this constructed case, an engineer wants to move into evidence integration. A mentor asks the engineer to investigate unsupported source links, but the line manager assigns forty hours of delivery and rewards package closure without distinguishing a warranted return of an unsupported claim. HR has enrolled the engineer in a generic leadership course.

The engineer and receiving work owner examine a representative integration package. The required contribution includes recognizing a configuration mismatch, returning an unsupported claim to its supplier and assembling a traceable package. They use HCD.1 and HCD.4 to establish the demand and the capability evidence still needed. A learning practitioner examines whether the proposed course teaches those operations. If it does not, they obtain suitable instruction and practice; HR arranges the corresponding access.

The manager and engineer propose thirty-six hours of delivery and four hours of protected practice within the same forty-hour week. They identify a four-hour report-presentation task that can be deferred while retaining every required evidence check. Its receiving team accepts the later date. The manager changes the allocation and establishes how a justified return of an unsupported claim will be treated in performance evaluation. If the receiving team needs the original date, obtain another feasible allocation, negotiate a different scope or postpone the practice.

The mentor prepares a configuration-mismatch case, demonstrates the operation and observes the engineer's attempt. Before counting that help as available, HCD.7 establishes that the mentor can distinguish a real mismatch from an irrelevant objection, give usable feedback and supply the preparation and observation time. The participants agree which practice observations may be used for learning and any separate employment assessment. The receiving work owner provides a supervised assignment and states what would justify a later appointment. Safety retains its separate acceptance decision.

At the joint session, the proposed acceptance claim concerns configuration C7, but its cited test used C6. The engineer exposes the changed interface and asks the responsible specialist whether the evidence remains applicable. Where applicability is unsupported, they develop a joint-test proposal: identify the relevant interaction, load, configuration, observation needed and the decision that would use it. The connected result now explains the evidence gap and a way to answer it. Agreement that everyone should communicate better would leave that result missing.

Suppose the laboratory later withdraws the required window. The account shows which tests and acceptance claims depend on it, so the engineering and allocation owners can reconsider the test, schedule or proposed release. The discussion's conclusions do not silently remain adequate under the changed condition.

Now remove the manager's four-hour practice allocation. The earlier observations and mentor preparation remain useful within their scope, but the next workplace learning episode lacks its conditions. Reallocate work, obtain a feasible later opportunity or retain only independent practice that remains worthwhile. Absence of this performance does not establish a motivation deficit. Conversely, if the time remains but the mentor cannot diagnose the task, obtain capable help or develop the provider's capability. More authority does not supply the missing instruction.

The constructed result is an arrangement that permits the needed help to reach work, followed by observations at their stated scope. Neither the arrangement nor one successful episode establishes a general capability, an appointment or a causal effect of mentoring.

#### OCE.12:5.5 - Prepare a checked calculation handover with a trusted adviser

In a constructed engineering case, an organizer proposes a checklist for handing a module calculation to its independent reviewer. The reviewer needs the identified configuration, calculation, applicability grounds and unresolved questions before making the review decision. The organizer can arrange the change; the engineering lead authorizes its work allocation; the reviewer retains the technical judgement. The proposal initially adds a separate status tracker to the existing calculation package. In this case, the review rule permits evidence from an earlier configuration only when a qualified specialist explains why it remains applicable to the changed parameters. An unsupported conclusion returns for correction.

The engineering lead wants advice from a former colleague outside the project. With permission to share a non-sensitive example, the organizer explains the proposed handover and asks which consequence concerns the adviser. The adviser recalls a previous introduction that doubled status reporting. The engineer and reviewer trace a representative package whose calculation is already available: preparing and checking the handover takes twenty minutes, and copying its status to the tracker takes another five. Only twenty minutes of the engineer's time are available. Producing a missing calculation and performing the independent review have separate estimates and allocations. Agreement with the purpose leaves the proposed handover infeasible.

They examine the second view's receiving use. In this case no one uses it for a separate decision, and the person responsible for that view can retire it. The revised proposal keeps the existing package, adds the questions at the handover, and makes its status and unresolved issues visible to the reviewer. It needs twenty minutes. If the tracker instead supplied another team's required input, its removal would need an adequate replacement or a changed commitment. The adviser's concern has improved the proposal; the lead and the other responsible participants still make their own decisions.

The engineer and reviewer accept the revised contributions. The lead reserves the twenty-minute interval and authorizes one assisted handover. The organizer arranges a capable colleague's help and the source access; their preparation and assistance time are provided separately from the engineer's interval. In a shared brief they confirm the same scope, configuration, contributions and response to a missing ground. The receiver can see that the engineer has the interval, and the engineer can see that the reviewer will examine the return. An absent support colleague receives the terms and confirms the agreed help before it is relied on.

On that first attempt, the checklist brings attention to a test from configuration C6 cited in the C7 calculation package. The engineer can state the mismatch but needs help deciding its significance. A qualified colleague identifies a changed parameter whose effect the old test did not cover. Under that review rule, applicability to C7 remains unsupported. The engineer returns that gap to the specialist; the reviewer receives the unresolved claim and withholds the dependent review conclusion. The twenty-minute handover allocation includes no promise to produce a new calculation within that interval.

The specialist estimates the corrective calculation and its checking. The lead obtains the needed allocation with the people whose work would move, and the reviewer accepts a later receiving window. If those conditions cannot be arranged, the gap remains open and the dependent release waits. In the successful continuation stipulated here, the specialist supplies the C7 calculation and its grounds. The engineer completes the handover with the permitted help; the reviewer examines the applicable result under that rule and makes the review decision. That is the first completed contribution for this receiving use. A tick beside “configuration checked” without the corrected contribution would leave it missing. This constructed sequence establishes no measured effect or independent capability of the engineer.

Now change one condition before the next handover. If the twenty-minute interval is withdrawn, the lead must obtain a feasible allocation or defer the affected start; the adviser's earlier reasoning and the first result remain useful. If the required specialist belongs to another unit, the lead's authority over the engineer cannot reserve that specialist's time: request the contribution from its responsible owner and keep the proposed date conditional until it is supplied. If another receiver reveals a needed use of the supposedly redundant tracker, recover that input requirement, compare ways to supply it and obtain acceptance of the changed arrangement. The brief is reopened where reliance changes, not repeated to secure the same assent. If source access alone fails, restore it before the dependent check; a new leadership title or more persuasion supplies no missing observation.

### OCE.12:6 - Bias-Annotation

A celebrated initiator can hide dependence on personal effort or informal power. A formal leader can mistake compliance for understanding. Identify who provides each contribution, observe later use with the stated help, and preserve legitimate refusal or disagreement. Keep the conversation within its agreed purpose and safeguards.

### OCE.12:7 - Conformance Checklist

- The leadership contribution answers a named difficulty in the receiving work.
- Its Method, intended result and capable contributors are explicit.
- Facilitation, expertise, coaching, decision authority and time allocation are distinguished where they affect the contribution.
- When assistance requires different work conditions, the arrangement includes the relevant assignment, evaluation and resource changes, together with any displaced work.
- A discussion that promises an explanation or proposal produces the connected result needed by its receiver, with unsupported relations and changed-condition returns exposed.
- A career transition connects the person's development with receiving work and its actual assignment authority.
- The result reports what was performed and any condition that still prevents the needed contribution.
- Capability development uses a learning design supplied by a qualified learning provider, with practice, feedback and an opportunity for later use.
- The continuation claim states the observed next episode, retained help, limits and remaining gap.
- For negotiated contributions, identify the parties whose acceptance was obtained, the complete proposal they accepted, the mandates held by any representatives, the resources committed, and any refusal or unresolved condition.
- After a consequential support change, the affected parties reconsider the agreement and the responsible decision makers revisit dependent choices and promises. Unaffected results remain usable within their limits.

### OCE.12:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Better action |
| --- | --- |
| Appoint a champion and assume the leadership work has been performed. | Name and perform the contribution needed by the receiving task. |
| Ask the central leader to handle every difficult conversation. | Prepare peers to conduct the conversation, observe their later performance and retain the help they need. |
| Teach constructive challenge while punishing it at work. | Take the punitive workplace condition to someone authorized to change it, and obtain a protected opportunity to practise. |
| Assume a mentor can allocate work time or authorize another person's decision. | Identify who can teach, allocate time and make each decision, and obtain those contributions from them. |
| Select development from a course catalogue without identifying its receiving work. | Establish the later task, examine the instructional contribution and obtain a feasible practice or appointment opportunity. |
| Count a well-organized meeting as a constructed explanation. | Relate the domain claims and their grounds, resolve the needed dependencies and trace the receiving decision through the result. |
| Treat a technically feasible proposal as agreement by everyone affected. | Ask each party to respond to the whole proposal; keep refusal and missing representation explicit. |

### OCE.12:9 - Consequences

The organization can obtain leadership work from several capable participants and identify dependence on an initiator. This requires protected time, competent help and feedback. Some contributions require specialist competence or a particular authorization. Retain those conditions when deciding whether another person can take over. Preparing another participant can cost more than continuing competent help. It is warranted when the additional continuation or learning evidence is worth that accepted burden. Keep the sufficient current arrangement when it already meets the need; do not count retained assistance as a saving or an intended learning result as an observed capability.

### OCE.12:10 - Rationale

Naming the needed contribution makes it possible to choose a fitting Method. Briefs, role conversations and debriefs solve different difficulties. Practice followed by workplace use connects a person's learning with the organization's provision of time, resources and help. Mentoring and managerial decisions remain different contributions.

### OCE.12:11 - SoTA-Echoing

The practice question is how leadership work becomes useful and repeatable in a change. One choice is whether to continue competent assistance or add development of another participant. **Adapt** task-focused teamwork and supported development; select between their available arrangements through 4.2. A capable current lead or qualified substitute can supply the required results and continuation.

| Comparison and selected contribution | Effect here, limit and reopen condition |
| --- | --- |
| AHRQ's TeamSTEPPS [team leadership](https://www.ahrq.gov/teamstepps-program/curriculum/team/tools/index.html), [brief](https://www.ahrq.gov/teamstepps-program/curriculum/team/tools/briefs.html), [debrief](https://www.ahrq.gov/teamstepps-program/curriculum/team/tools/debrief.html) and [mutual support](https://www.ahrq.gov/teamstepps-program/curriculum/mutual/tools/index.html) include capable participants, resource allocation, assistance, feedback and changes to plans. This is a serious current way to obtain useful teamwork. | Adapt the working conversations in 4.3 while retaining competent existing help as a sufficient alternative in 4.2 and 5.2. The source's healthcare setting supplies no measured effect for the association or engineering cases. A missing locally capable contributor may warrant development, but the comparison must include its added work and retained assistance. Reopen when the result, support or continuation demand changes. |
| In the [2024 LOCI trial](https://doi.org/10.1016/j.josat.2024.209437), supervisors use feedback from leadership assessments to plan their development. Training is accompanied by continuing coaching and support from higher organizational levels. | Adapt steps 4.2, 4.4 and 4.5 by arranging the required organizational support and subsequent workplace use. Treat qualified programmes combining these contributions as alternatives to arranging separate local support. The trial evaluates a combined intervention in clinical services. Assess whether the intervention fits the work and support conditions of the organization where it would be used before using the findings to choose it. Account for the time needed to provide support; reconsider the intervention when the setting changes or evidence for applying it there is insufficient. |
| [Making soft skills stick](https://www.tandfonline.com/doi/full/10.1080/1359432X.2024.2376909), 2024, examines conditions for using learned skills at work. The [reverse training transfer](https://doi.org/10.1016/j.ssci.2025.106920) study, 2025, examines how workplace experience also feeds back into training. | Adapt steps 4.4–4.6: obtain practice designed by a qualified learning provider and evidence from later use, and use task failures to revise the learning design. The scoping review and exploratory maritime case guide design; causal effectiveness in a new setting requires its own evidence. Revisit the target or workplace support when the contribution fails under the receiving conditions. |
| The [CBI Mutual Gains Approach brief](https://www.cbi.org/assets/resource/media/cbi-mgabrief-2023.pdf), 2023, explains a negotiation approach for parties seeking a mutually acceptable arrangement. | Adapt step 4.3.1 by checking proposals against engineering evidence and available resources, and obtaining each party's acceptance of its contribution and conditions in the whole proposal. Obtain participants capable of performing the negotiation Method. Reconsider the approach when participation, representation, capability or the available inquiry budget is insufficient for the needed result. |
| [Tailoring Requirements Negotiation to Sustainability](https://pure.hud.ac.uk/ws/portalfiles/portal/14095615/RE2018bCRpdf.pdf), 2018, explains WinWin's stakeholder objectives, conflicting or uncertain conditions, options and agreements. It extends the negotiation to indirect and later effects of requirements. | Adapt this distinction in 4.3.1: construct options, examine their consequences and obtain acceptance of the resulting proposal. The exploratory study's restricted stakeholder participation and workshop time limit its findings, especially for cumulative long-term effects. Reconsider an affected proposal when an unrepresented consequence or changed premise matters. |

R10, *Systems Management*, 3:6 and 11:2, contributes practitioner cases of mentoring without control over assignments, conflicting HR and line-management decisions, and administrative course selection. Adapt them in 4.2 and 4.4.1 by connecting competent help, actual work, evaluation and receiving opportunities. The cases expose design problems; their categorical organizational preferences are not universal rules.

The critical practitioner essay [“Об фасилитаторов”](https://ailev.livejournal.com/1520610.html), 2020, distinguishes organizing communication from constructing connected thought and recognizes facilitators able to do both. Adapt 4.3.2 by obtaining substantive reasoning and a usable result. Its broad effectiveness claims are not premises here. Reconsider the arrangement when orderly participation still leaves the receiving question unanswered.

R10, *Systems Management*, 10:2 and 10:5, contributes preparation with trusted advisers, a publicly understood start and organizational change made real in working products, means and first use. Adapt these in 4.3.3 and 5.5. The source's fixed durations, universal safety assurances and categorical attribution of non-use to resistance do not govern this Method. Real disadvantages and unavailable resources can warrant revision or refusal.

The current CFIR guide's [Opinion Leaders](https://cfirguide.org/constructs/opinion-leaders) distinguishes informal influence and reports varying effects; its [Engaging](https://cfirguide.org/constructs/engaging) account includes people delivering and receiving the innovation. Adapt the attention to relevant advice and participation, with the decisions and representation established for this work. These constructs help locate a missing contribution; they do not supply its explanation or guarantee acceptance. AHRQ's [brief](https://www.ahrq.gov/teamstepps-program/curriculum/team/tools/briefs.html) and [huddle](https://www.ahrq.gov/teamstepps-program/curriculum/team/tools/huddle.html) distinguish sharing a plan from adjusting it when conditions change. Adapt that distinction to 4.3.3, retaining healthcare as their original use. These are already substantive parts of competent teamwork. Steps 4.2 and 4.3.3 use an adequate existing answer directly and add preparation only for the contribution still missing. Reconsider the arrangement when a later objection or failed handover defeats its grounds.

The comparison in 5.2 concerns the same three editorial results over six weeks. Experienced facilitation can supply them with qualified support and no new development. It does not, by itself, establish that a second member can perform the bounded discussion steps. The selected addition uses 4.4 to prepare that member and 4.5 to observe later use, while retaining the competent fallback. The association accepts extra practice, provider work and coordination for that additional evidence; no reduction in total work or general leadership effect is claimed. The choice concerns these available arrangements for this task. If local continuation is not valuable, adequate capability evidence already exists, or the extra work cannot be supported, the reason for the addition disappears. Reconsider after failed practice, withdrawn help or a changed receiving task.

### OCE.12:12 - Relations

[CHK.3](CHECKLIST-PRINCIPLES-FRAMEWORK.md#chk3---fit-a-checklist-to-its-occasion-of-use) fits a checklist to the actual first and later occasions of work; OCE.12:4.3.3 prepares the organizational decision and shared start on which that use depends. OCE.10 addresses obstacles to participation and to recurring ways of working. OCE.9 uses the leadership contribution in realizing an organization-capability increment. OCE.11 helps reconcile change work with continuing service. Use OCE.6 with the responsible institutional decision makers to establish assignments and authority. OCE.15 develops the organization-change content of a proposed Method; Method Engineering qualifies the way of doing.

For negotiated contributions, OCE.7 coordinates product and organization architecture decisions. SYSE.6 guides the engineering architecture decision; SYSE.24 guides comparison and choice among complete ways to obtain an engineering result. OPS.13 helps maintain commitments through authorized changes. [SYSE.17](SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse17---find-systems-that-may-bear-engineering-consequences) helps identify systems that may bear engineering consequences and the conditions that matter to them. [CB.13](COMMUNITY-BUILDING-PRINCIPLES-FRAMEWORK.md#cb13---establish-a-workable-mandate-for-shared-decisions) explains representation, mandates and the conditional option of a team protocol. [B.5.QD.CF](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#b5qdcf---reformulate-a-problem-by-examining-its-conflicting-assumptions) helps reconsider an assumed necessary means; [D.4](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#d4---ethical-mediation-and-decision-use) helps compare alternatives under conflicting value premises. [C.11](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11---decision-theory-decsn-cal) keeps a conflict among collectives explicit when treating the choice as one decision maker's comparison would conceal it.

HCD.1 supplies capability demand. HCD.3 supplies a target justified by evidence or helps return the question for another remedy or missing evidence. HCD.4 supplies a capability profile. [HCD.7](HUMAN-CAPABILITY-DEVELOPMENT-PRINCIPLES-FRAMEWORK.md#hcd7---arrange-providers-access-tools-and-ai-support-for-human-capability-development) establishes the availability and conditions of providers, access, tools and support; use its return to HCD.8 when a provider's missing capability must be developed. OCE.4 designs the needed contribution relations, OCE.5 addresses a continuing position when needed, and OCE.6 establishes the enabling relations for actual work. Learning providers remain responsible for intervention and assessment. C.36 governs claims about cultural continuation; C.28 governs causal claims. Use OCE.17 when the subject is the continuing practice of organization-change engineering itself.

### OCE.12:End

# Part IV - Observe Consequences and Revise the Organization

## OCE.13 - Observe and Compare Organization-Change Consequences

> **Type:** Method pattern
> **Status:** Stable
>
> **Primary working result:** a decision-useful comparison of observed organization-change consequences, stating what the evidence supports and preserving conflicting results, uncertainty, missing evidence, and the next decision or observation question.

### OCE.13:1 - Problem frame

**Use this when** a decision about an organization change needs to know what changed, for whom and under which conditions. A release handoff becomes faster, but field-service replies become later and participants report more unplanned checking. The result may justify retaining one contribution and investigating another; a single “change succeeded” score cannot tell the decision owner what to do.

Begin with the receiving decision and one finding that could change it. Name the organization arrangement, the contribution or protection that matters, the people or other Systems affected, and when the answer is needed. Inspect existing observations before commissioning more measurement.

Continuing organization development is the wider concern. This Method covers **comparison of organization-change consequences**: operating, contribution, coordination, human-condition, customer and relevant surrounding-System results as they bear on a particular decision. The primary result is a qualified comparison, not an intervention, revision authority or a causal explanation.

A descriptive comparison can be useful: fewer late evidence returns alongside more late service follow-ups. Its conditions and limits travel with it. An observation plan is an earlier useful result when evidence is missing, but remains a plan.

**Use the direct owner instead** when an already understood local defect has a sufficient correction under OCE.9–OCE.12 or the receiving operation. A binding authority or protection condition can also require a direct response without a general evaluation. Use measurement or evaluation specialists for results that need their competence. OCE.13 organizes their contributions around the organization-change question; it does not replace them.

### OCE.13:2 - Problem

Local improvement is easily mistaken for an overall result. A shorter handoff can transfer work to another role, defer an exception, exclude difficult cases or depend on extra support. Favorable implementation outcomes, such as attendance or adoption, can coexist with poor customer or worker consequences.

Observations can also cease to be comparable. Demand, staffing, eligibility, the work configuration or the measurement procedure changes, but a before/after chart hides the difference. Missing observations are treated as zero problems; plausible explanations become asserted causes.

The practitioner needs to assemble the consequences that can change the decision, qualify what each observation supports and return a comparison that preserves both gains and losses.

### OCE.13:3 - Forces

| Force | Tension |
| --- | --- |
| Decision timing | An answer is needed while change is still possible, but some consequences emerge only later. |
| Comparability | A shared basis permits useful contrast, while the work, population and measurement can change. |
| Breadth and effort | Relevant transferred burdens must be found, while observing every possible consequence would stop useful work. |
| Attribution | A decision may need a causal claim, while descriptive evidence is often the available and sufficient first result. |
| Affected participants | People can expose hidden consequences, while evidence use must respect privacy, protection and the cost of contributing it. |

### OCE.13:4 - Solution

Choose the consequence questions from the receiving decision, obtain or reuse observations at their supported scope, compare them without hiding conflicting effects, and state the next usable result or gap.

Recognition needs only a consequential unanswered question. Assurance depends on how the comparison will be used. An ordinary count under an agreed procedure can support a bounded descriptive claim. A patient-effect estimate, a causal claim, a general reliability claim or an assertion about a whole population requires the corresponding professional method and evidence. More polished reporting does not strengthen the underlying claim.

#### OCE.13:4.1 - Start with the decision and what could change it

Recover the arrangement or change being examined and the actual organization it concerns. Name the intended contribution, current commitments and protected conditions. Ask the receiving owner what findings could alter retention, repair, stopping or further inquiry, and when that choice remains possible.

Do not begin by choosing a dashboard. Begin, for example, with “Should the release-support arrangement continue under its current assignment?” The relevant findings may include timely evidence, the burden placed on service work and the conditions under which the same people supply both.

Ask affected participants which consequences the initial account omits. Follow the contribution outward and the work backward: who receives the result, who supplies it, who handles failures, whose work is displaced and which surrounding System could bear a material consequence? Participant accounts can reveal a question without yet settling its answer.

Bound the inquiry by that decision. If one current service or authority result already determines the permitted next action, return it directly. A competent existing evaluation may already answer the whole consequence question, including displaced burdens and explanatory limits. Check its fit to the present arrangement and receiving use, then use that answer without commissioning another OCE comparison. If a wider observation would not change the decision, do not require it merely to fill an evaluation framework.

For a consequential gap, compare using the supported current answer with extending it or obtaining another qualified result. Keep the receiving decision, required protection and decision window fixed. Say what each continuation would let the owner decide, including an explicit deferral when that is permitted. An extension is useful when its possible findings would change that choice.

Compare the complete work required to reach and use each return. Keep common collection, interpretation and decision work in both accounts; reuse completed work rather than charging for it again. For the difference, include access and provider preparation, participants' contributions, collection and checking, reconciliation of disagreements, coordination, communication, and the support or rework needed to use the result. Count displaced commitments and continued support while waiting. Distinguish total effort, who bears it and elapsed time: a short analyst task can still require scarce participant time or miss the decision. Use available estimates or a bounded qualitative comparison; leave unknown costs visible. Agree any additional burden and delay with those who allocate and perform the work. Choose the extension only for its stated gain at that accepted cost; otherwise return the sufficient result or the narrower supported answer and its unresolved question.

#### OCE.13:4.2 - Make the consequence questions observable

Look across operating results, contribution crossings, coordination, human conditions, customers and relevant surrounding Systems. These are places to discover a missed consequence, not six compulsory metrics. Select only the questions whose answers can change the receiving use.

For each selected comparison, make the following recoverable in ordinary language or an existing measurement account:

- the exact subject and eligible episodes, including which people, recipients, failures or diverted cases are excluded;
- the arrangement, exposure and other conditions under which each observation applies;
- the observation period, relevant delay and baseline or other comparator;
- the characteristic, unit or category and the measurement or collection Method;
- missing observations, uncertainty and the basis on which the readings can be compared;
- the interpretation the receiving decision needs and the claim the evidence cannot yet support.

For a late evidence-return proportion, for example, identify the eligible requested crossings, the agreed receiving deadline, the observed return time and the rule for cases still open at the end of the window. “Late” must mean the same thing on both sides of the proposed contrast. If the rule changes, recover a common basis from the underlying observations where possible or state that the values are not comparable.

Use C.16 for the exact measurement question, including the applicable model, calibration, scale and uncertainty. Reuse a qualified measurement procedure instead of inventing a new one to suit the desired conclusion. A survey response about burden, an observed missed deadline and an inferred workload mechanism remain unlike results.

Preserve subgroup and reach differences that could change the decision. An average among completed cases may say nothing about those diverted, abandoned or never admitted. Do not enlarge the observed population merely because the decision concerns the whole organization.

#### OCE.13:4.3 - Obtain and qualify the observations

Inspect current records and existing results first. Reuse one only if its subject, arrangement, period, measurement and intended use fit this question. A current file can contain an old observation, and a recent observation can concern another configuration.

Where permitted and within competence, collect ordinary work observations through the applicable procedure. Bind a reading to its actual episode and source. For a reported experience, preserve who or what population the report represents, how it was obtained and the limits of its use without unnecessarily exposing identities.

Request the smallest missing professional result. It may be a valid denominator, a clinical interpretation, a customer observation, a worker-protection constraint, an estimate under a tested measurement model or causal support. Name the receiving question and the required scope; a request for “more evidence” alone gives the provider little to act on.

Triangulate a consequential self-report with appropriate other evidence when this can distinguish live explanations. Two sources can share the same omission or incentive. Agreement between them is not automatic independence or proof.

Keep observation, report and interpretation separate. “Six returns were late under the stated rule” differs from “participants report doing checks after hours” and from “the new assignment caused overload”. Preserve missing or incompatible evidence locally: an absent customer result may block a customer-benefit claim while leaving the evidence-return comparison usable.

#### OCE.13:4.4 - Compare consequences under their supported basis

Put the qualified values beside their common basis and important differences. State what improved, worsened, remained unchanged or cannot be compared, and who receives each consequence. Keep losses visible even when the intended contribution improves.

Test the explanations that could alter interpretation: demand and case mix, staffing, seasonal conditions, other concurrent changes, selection into the observed set, delayed effects and changes to the measurement procedure. Do not list every imaginable rival. Seek a distinguishing result only when its answer can change the claim or decision.

A before/after contrast usually leaves these alternatives open. Report that contrast as such. Do not subtract unrelated scales into a net-success score or silently let a local efficiency gain compensate for a protected condition. A lawful trade-off, if needed, is a decision for the appropriate owner, not an operation performed by the observer's spreadsheet.

If the receiving claim needs “caused by”, identify the exact causal-use question and obtain the applicable C.28 support and domain evaluation result. Different questions may call for different designs. Neither an appealing mechanism story nor the existence of a comparison group automatically supplies identification, validity or transfer to another organization.

A stronger causal study is not a universal prerequisite for a bounded response. A current assignment conflict or qualified protection result may support a specific authorized repair while the overall effect remains uncertain. Conversely, a favorable descriptive trend cannot authorize an action whose required conditions do not hold.

#### OCE.13:4.5 - Return the comparison and the next question

Give the receiving decision the supported contrasts, their subjects and periods, the conflicting benefits and burdens, incompatible or missing evidence, surviving explanations and the exact uncertainty that still changes action. Keep enough provenance to recover the observations and enough currentness information to know when they cease to apply.

A compact result can say:

> For the declared release family and observation windows, late evidence returns decreased, while late service follow-ups increased. The counting rules are aligned; staffing and case mix are not held equal. The comparison does not attribute either difference to the hybrid arrangement. The next decision-changing question is whether the current release-support assignment occupies the interval needed for service return.

Use OCE.14 when that result challenges an organization relation and a revision is the next question. Use OCE.10 for a supported participation or target-culture question, OCE.11 for a service/change conflict, or the direct measurement, safety, customer or other owner for its missing result. Give OCE.15 or OCE.17 feedback only when a reusable Method or practice-continuation question actually arises.

If the next useful output is an observation plan, name the question, procedure, permitted source, responsible provider, timing and conditions. Do not describe its proposed readings as obtained. If access fails or the result will arrive after its receiving decision, reconsider the addition with that owner: a timely narrower return, a permitted delay or a separately authorized protective response may now be preferable. Keep already supported contrasts, and commission a later observation only for a later use that still warrants its work.

What changes in practice is the choice of the next move. The organization can retain an observed gain, investigate a displaced loss and stop an unsupported claim without treating them as one all-or-nothing verdict on the change.

### OCE.13:5 - Archetypal Grounding

#### OCE.13:5.1 - PumpWorks gains and transferred burden

This is a constructed extension of the PumpWorks example. Its observations are fictional. A separately authorized limited hybrid arrangement is in use for the weekly evidenced release family.

The receiving decision is whether the current release-support assignment should continue. The example supplies permitted records and a locally qualified counting procedure. It defines an eligible evidence crossing and service follow-up, the agreed information deadline and how open cases are handled. The same definitions apply in two declared eight-week windows.

| Observation under the supplied procedure | Before | After | Supported descriptive contrast |
| --- | --- | --- | --- |
| Eligible evidence returns that missed their agreed window | 8 of 40: 20% | 3 of 40: 7.5% | The observed late proportion is lower by 12.5 percentage points. |
| Eligible field-service follow-ups that missed their agreed information window | 2 of 20: 10% | 6 of 20: 30% | The observed late proportion is higher by 20 percentage points. |
| Protected reports of unplanned cross-checking after formal hours | The supplied material does not give a comparable earlier report set. | Some interviewed participants describe additional checking. | This is a bounded report, not a measured population change or causal result. |

Staffing, incident mix and product mix may differ. The equal denominators do not make the before and after cases a controlled experiment or identical population.

OCE.13 preserves both numerical contrasts and the limited interview evidence. It does not average the two proportions, call the change a net success or infer whole-organization customer benefit. The observed return improvement remains useful even while its cause and wider effects remain open.

A competent evaluation team can already supply these contrasts, participant accounts and limits. Producing them includes permitted record extraction, checking the counting procedure, participant consultation, interpretation with qualified providers, reconciliation and a usable return. OCE does not repeat that work. The evaluator, relevant holders and receiving owner check whether its arrangement, intervals and intended use are still current. If the result also contains a qualified current assignment account that answers the overlap question, return it directly. Obtain the service owner's coverage and substitution conditions only where the receiving revision needs them. This is a sufficient evaluation result, not a reason for another observation cycle.

Now suppose the assignments changed after the observed windows. The historical contrasts remain supported, but the evaluator cannot yet say whether the current release-support and service commitments occupy incompatible intervals for the same holder. The organization owner needs a warranted basis by Friday for choosing the support arrangement for the next two weekly releases. For this choice, the direct owners separately supply a permitted temporary manual arrangement through the next scheduled review, with its staffing, service protection and recovery conditions. These are case inputs, not consequences inferred from the table.

Both continuations use the completed evaluation, its currentness check, the owner's Friday decision and the work of implementing, communicating and checking whichever disposition is authorized. Temporary support through Friday is common work. Compare what differs:

| Continuation for the Friday decision | Additional work and timing | Useful return and accepted limitation |
| --- | --- | --- |
| Use the competent current evaluation and defer the unresolved assignment decision to the scheduled review. | No new collection now. The holders and service owner arrange and perform temporary manual support for the two releases; the evaluator carries the exact gap into the existing review. Its later inquiry and participants' preparation still cost work. | The owner can choose the supplied temporary arrangement without attributing either contrast to the hybrid. The current assignment question stays open, and the hybrid-dependent contribution is deferred. |
| Extend that evaluation with a current assignment-and-work check before Friday. | The record custodian checks permitted access and extracts the relevant assignment and episode records; the affected holder and release/service leads explain actual intervals and exceptions; the evaluator reconciles them and returns a bounded conclusion by Thursday. The service owner checks what that conclusion means for coverage. Their added preparation, coordination, correction and return occupy time otherwise allocated to a non-urgent cross-team documentation review. Any resulting reassignment, substitute and follow-up remain work to be provided, not a saving credited in advance. | A confirmed conflict opens the specific OCE.14 revision question; a supported absence of that conflict removes this particular ground for repair. An inconclusive return leaves the temporary option available under its supplied conditions. No outcome identifies the hybrid's overall causal effect. |

In this case these participants and providers can complete the check and return by Thursday; they and those responsible for their allocation accept postponing the documentation review. The organization owner chooses the extension because a timely answer can settle this ground for repairing the assignment before Friday, when a supported revision can still be considered for the next releases. A usable answer creates that earlier choice; it does not guarantee a permissible revision or preservation of the hybrid's contribution. This is an accepted expenditure for a useful earlier choice, not demonstrated net economy. The temporary arrangement's work remains in the comparison; the burden of any eventual repair must be accepted separately. If the current evaluation already answered the assignment question, or the earlier choice did not matter enough to those bearing the additional work, the extension would not be selected.

Suppose the qualified check then confirms incompatible commitments. OCE.14 receives that result alongside the two descriptive contrasts, the report's limited reach and the live staffing/mix explanations. Its owner still needs current coverage, substitution and authority before changing the relation. The inquiry has supplied no such permission.

Change one condition: the custodian can release the needed records only after Friday, and no timely qualified substitute result is available. The proposed extension cannot support this Friday choice. The owner uses the already permitted temporary arrangement, with its actual burden and deferred hybrid contribution, and reconsiders the observation for the later review. If that temporary arrangement is also unavailable, return the unsupported continuation to the direct owner rather than inventing cover. Neither delay erases the two historical contrasts or turns them into an answer about the changed assignments.

#### OCE.13:5.2 - Hospital waiting time and missing severe cases

A public hospital reports shorter emergency-department waiting times after a flow change. The supplied observation covers admitted cases, while more severe cases are diverted and some have no comparable follow-up in the available material.

The first OCE result is not “patient benefit improved”. It identifies the changed population and the missing consequence of diversion. The practitioner returns the exact eligibility, observation and clinical-interpretation questions to qualified measurement and clinical owners. The current admitted-case waiting result may remain reportable at its narrow scope; it cannot stand for all arrivals or outcomes.

An authorized clinical decision-maker may separately require a protective pause. OCE.13 preserves that result and its basis; OCE.14 can carry only the actual authorized organization scope. Neither pattern supplies treatment advice or creates clinical, statutory or worker-protection authority.

#### OCE.13:5.3 - A changed counting rule

A service team reports fewer late replies, but changed the rule from elapsed hours to working hours between windows. If retained timestamps and the applicable collection procedure permit recalculation, compute both sets under one justified rule. If not, report the two observations with their different meanings and return the comparability gap.

The repair is to the comparison basis, not automatically to the organization. Demanding an organization redesign or a causal study before resolving this simple difference would miss the immediate result.

### OCE.13:6 - Bias-Annotation

Available metrics favor visible, easily counted work; ask which recipient or burden is missing. Survivor and selection bias can make the observed population easier after the change; preserve exclusions and changed eligibility. Sponsor preference can reward a favorable story; show the strongest decision-changing rival and the people bearing the loss.

Participant evidence can expose what records omit, but contributors may face unequal risks or incentives. Keep lawful evidence use, protection and the limits of each report part of the result.

### OCE.13:7 - Conformance Checklist

- [ ] The receiving decision, arrangement, affected organization, timing and decision-changing questions are explicit.
- [ ] The chosen consequences follow the contribution and affected parties rather than a compulsory metric panel.
- [ ] A sufficient current evaluation can finish the inquiry; any extension has a decision-changing result, full common/additional work, timing and an accepted burden.
- [ ] Subjects, eligible episodes, windows, conditions, measurement procedures and comparison basis are recoverable.
- [ ] Reports, observations, interpretations, uncertainty and missing evidence retain their different meanings.
- [ ] Relevant gains, losses, transferred burdens and subgroup differences remain visible.
- [ ] Live rival explanations are addressed to the degree needed by the receiving use; causal claims have separately qualified support.
- [ ] Professional, privacy and protection conditions remain with their actual owners.
- [ ] The return supplies a usable comparison or a clearly identified plan/gap, its limits and the next decision or observation question.

### OCE.13:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Better move |
| --- | --- |
| “The dashboard is green, so the change succeeded.” | Recover the receiving decision, omitted consequences and who bears the costs. |
| “Before is worse than after, so the intervention caused improvement.” | Report the qualified contrast and obtain causal support only for the causal use actually needed. |
| “The averages improved for everyone.” | Inspect population reach, exclusions and decision-changing subgroup differences. |
| “No record means no adverse consequence.” | Keep missing observation separate from a measured zero. |
| “One missing measure invalidates everything.” | Stop only the dependent comparison or claim; preserve supported results. |
| “More data will solve the authority gap.” | Return the authority question to its owner; an observation result does not authorize the action. |

### OCE.13:9 - Consequences

The practitioner obtains a result that can support a specific next decision without concealing displaced work or overstating causation. A useful local contrast can survive an unresolved wider question, and a missing observation becomes an actionable request rather than a vague demand for more study.

The cost includes participants and providers as well as analysis: comparability, access, interpretation, reconciliation, return, displaced work and continued support while waiting. An existing competent result can avoid a new inquiry. An extension may instead justify greater effort for an earlier or better-supported choice, as in PumpWorks; neither its narrower scope nor its OCE label proves economy. A late or inaccessible result can make a narrower return, permitted deferral or separately authorized precaution the better continuation.

### OCE.13:10 - Rationale

Organization change alters relations through which contributions are obtained and burdens distributed. Observing only the intended local result can miss the reason a revision is needed. Beginning with the receiving decision identifies which observation could matter; comparing its complete work and timely use determines whether obtaining it is worthwhile. When a competent evaluation already supplies the answer, specialization to OCE adds no reason to repeat it.

A qualified comparison preserves the meaning of each value and the conditions under which it was obtained. That permits a decision owner to distinguish a real conflict, a measurement problem and an unresolved causal question, instead of treating every disappointing observation as proof that the whole arrangement failed.

### OCE.13:11 - SoTA-Echoing

The practice question is whether the current consequence evidence is sufficient for an organization decision, and which further evaluation, if any, is worth its work. **Adopt** competent, proportionate evaluation that relates its question, evidence and return to that decision. A sufficient existing evaluation is the principal alternative to a new OCE-led extension. Sections 4.1 and 5.1 let it finish the inquiry after its applicability has been checked.

**Adapt** the [updated MRC framework (Skivington et al., 2021)](https://doi.org/10.1136/bmj.n2061): questions about intervention/context relations, stakeholders and consequential uncertainty become questions about organization contributions and displaced burden in 4.1–4.2. It is a health-intervention research contribution, not evidence that this OCE Method produces a particular effect.

The [Magenta Book (HM Treasury, May 2026)](https://www.gov.uk/government/publications/the-magenta-book/magenta-book-central-government-guidance-on-evaluation-html), especially §§2.2.2, 3.1–3.2 and 4.2, supplies the strong evaluation line: purpose and use, feasible timing, participant burden and explicit methodological trade-offs. Sections 4.1/4.3/4.5 adapt it to the receiving organization question. Local measurement, professional interpretation and organization authority still need their actual providers.

The constructed PumpWorks comparison specializes this evaluation line for an organization decision. The competent bounded return supports a permitted temporary arrangement. A timely current-assignment check costs additional participant/provider work and displaces a documentation review, but can change which specific relation the owner considers repairing before the next releases. That accepted trade-off, including continuing support and the uncredited cost of any later repair, justifies the addition in the stated case. A sufficient current assignment result removes the need for it; late access removes its Friday payoff. Sections 4.1/4.5 and 5.1 make the choice depend on the available evidence, burden and time left to use the result.

Unchanged indicators that omit a material burden and compulsory causal research for every descriptive return remain failures to avoid, not the strongest alternatives. Obtain stronger causal evidence where the receiving claim requires it. Reopen the comparison when the decision window, available answer, population, procedure, arrangement, provider access, burden or a serious evaluation alternative changes.

### OCE.13:12 - Relations

[C.16](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c16---measurement--metrics-characterization-mmchr) supplies measurement and comparability distinctions. [A.10](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a10---evidence-graph-referring-claim-bound-evidence-and-provenance-graph) governs claim-bound provenance and gaps. [C.28](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c28---causaluse-cal-causal-use-questions-identification-and-realizability) governs the support needed for a particular causal use. The applicable domain professional still supplies the measurement, interpretation or causal result.

OCE.1/OCE.2 and the current arrangement supply the organization and actual-work question where those facts are not already known. OCE.9–OCE.12 keep the observations and corrections needed for their own bounded Methods; they need not wait for a wider OCE.13 comparison.

OCE.14 receives qualified results when an organization relation may need revision. OCE.10 receives a participation or target-culture question; OCE.11 a service/change conflict. OCE.15 and OCE.17 receive feedback only when it changes a reusable Method or the continuation of OCE practice.

Strategy, Operations, human development and clinical, safety, labor, legal, privacy, financial, ecological or customer-domain owners retain their decisions and professional results. The framework's current dependency account distinguishes an available Method from a still-missing result in the case.

### OCE.13:End

## OCE.14 - Decide Whether and How to Revise the Organization from Qualified Results

> **Type:** Method pattern
> **Status:** Stable
>
> **Primary working result:** an authorized retain, repair, replace, reverse, stop or investigate disposition for identified organization relations or conditions, with its effective scope, accepted losses and remaining realization or observation work; without authority, a bounded proposal or exact authority request.

### OCE.14:1 - Problem frame

**Use this when** a qualified result challenges an organization relation or condition that was previously selected or put into use. A release-support arrangement improves evidence returns but occupies a service interval already promised to customers. The next question is which relation should change, who can change it and what useful contribution must be preserved.

Start from the challenged relation and the result that challenges it. Recover what obtains now, what was only proposed, and the current authority for a change. Use a sufficient current revision decision or comparison; form materially different bounded alternatives only for the question still open.

Continuing organization development is the wider concern. This Method covers **revision of the organization's contribution, assignment, authority, access, support, provider, participation or other relevant relations and conditions**. Strategic direction, investment, continuing Operations, human development and specialist protection decisions retain their own owners. A revisable development programme is not one indefinitely continuing work occurrence or a universal maturity ladder.

OCE.13 can supply consequence observations, but is not a mandatory predecessor. A direct service, authority, safety, provider or arrangement result may already answer the evidence question. The first useful result can be a scoped proposal or missing-authority return; a practitioner does not acquire decision authority by applying the Method.

**Use a narrower direct response** when the current design remains suitable and only its realization or an ordinary operating correction is missing. OCE.9–OCE.12 or the receiving operation may already close that question. Use OCE.15 and Method Engineering for a defective reusable Method, and the appropriate owner when the intended direction itself is disputed.

### OCE.14:2 - Problem

Organizations can preserve an arrangement long after its premises fail, or replace too much after one adverse observation. The former transfers losses to less visible participants; the latter destroys useful contributions and creates unnecessary transition work.

A revised chart, a chosen option and a signed decision are also easily mistaken for the new organization. Assignments, permissions, access, support and actual capability may still be absent. An old arrangement may no longer be recoverable even when its diagram remains available.

The practitioner needs to identify a useful revision subject, compare complete alternatives under current evidence and authority, make the actual decision or relation effective within its scope, and return the work that remains.

### OCE.14:3 - Forces

| Force | Tension |
| --- | --- |
| Timely response | A loss may need action before its full causal mechanism is known, while unsupported intervention can make it worse. |
| Preservation and change | A bounded repair can retain a useful contribution, while too narrow a repair can leave the defeated premise untouched. |
| Authority | A legitimate owner can change one relation, but cannot silently change another owner's commitments or protections. |
| Continuing service | Transition and learning consume resources already committed to operating work. |
| Recovery | Reversal can limit loss, but people, access, providers and obligations may have changed since the earlier arrangement. |

### OCE.14:4 - Solution

Recover the current relation and the challenged premise; distinguish revision from direct correction; reuse a sufficient revision or develop the missing comparison; make the authorized disposition effective; and return unrealized work and future observations.

Recognition is light: one consequential result can justify examining a relation. Assurance is specific to the disposition. A proposal needs a recoverable problem and alternatives. An authorized decision needs its actual mandate and applicable decision rule. An obtaining assignment or enabling relation needs the acts and conditions that make it effective. Realized capability and causal effect require their own evidence.

#### OCE.14:4.1 - Recover what can be revised now

Name the relation or condition, its participants, the contribution it supports and the evidence of its current state. Separate an obtaining arrangement from a selected but unrealized design. If only a proposal is being changed, the result remains a revised proposal until a proper owner decides and the applicable conditions take effect.

Recover the present problem, relevant observations and limits, accepted commitments, affected parties and hard constraints. Ask which current premise is defeated or uncertain. “Performance is down” is too broad if the actual issue is one support interval that now overlaps a service obligation.

Identify the owner and scope of the contemplated decision, including its effective period. A manager's assignment authority, a provider's commitment, a safety acceptance and a member body's ballot decision can be separate. An old approval may not cover a new holder, a different configuration or a later term.

Keep the governing evidence close to the claim. If current evidence does not establish whether the relation obtains, obtain the missing result through OCE.2/OCE.6 or its direct owner. Do not redesign a relation that is only imagined to obtain.

#### OCE.14:4.2 - Choose the smallest revision subject that answers the problem

First inspect any current revision already prepared or decided through competent operating review, adaptive management or a specialist contribution. Does it answer this organization question for the same contribution, period and protected conditions, with an applicable basis? A sufficient comparison can go directly to the actual decider. A sufficient decision within current authority needs only its remaining effective acts under §4.5; an already effective disposition goes to the receiving work in §4.6. Reuse those results without regenerating alternatives, repeating observation or requiring an additional OCE approval. Remaining integration or later performance evidence does not by itself make the revision decision insufficient.

For what remains unresolved, decide what kind of result is actually missing.

| Current difficulty | First useful return |
| --- | --- |
| A selected arrangement has not yet been made usable. | OCE.9 and the direct assignment, access, support or professional owner supply realization conditions; revision is needed only if the selection itself must change. |
| A known local participation, leadership or service defect has a sufficient correction. | Use OCE.10, OCE.11, OCE.12 or the actual operating owner. |
| An organization premise or relation no longer fits the contribution or conditions. | Continue here with bounded organization-revision alternatives. |
| The reusable OCE Method lacks a needed move or no longer fits. | Return the specific problem and evidence to OCE.15 and Method Engineering. |
| Direction, investment or another external commitment is now the real question. | Return that question to its owner; preserve the organization facts it needs. |

Smallest does not mean cosmetic. Change enough of the arrangement to answer the defeated premise, while keeping useful unaffected contributions visible. If no local revision can meet the intended contribution and constraints, return the larger question explicitly.

A missing observation may justify a bounded inquiry instead of a redesign. A qualified risk may justify an authorized protective action before all explanations are settled. Preserve which of these is the current reason.

#### OCE.14:4.3 - Form materially different bounded alternatives

For the unresolved revision question, keep the current arrangement visible with its observed benefits, costs and limits. If a binding condition excludes its continued use, retain it as a reference, not as an admissible continuation option.

Try different ways of answering the problem:

- repair a failing contribution or enabling condition while keeping the successful arrangement;
- change holder assignment, authority distribution, support, work interval or provider boundary;
- isolate or stop the affected contribution while preserving other work;
- reverse to a specifically recoverable earlier arrangement;
- conduct a bounded observation or probe when it can distinguish alternatives that would change the decision.

Complete each serious alternative around the result, affected relations, people, support, authority, protection and transition it actually needs. “Add training” or “use a provider” is still a fragment until those dependencies and contributions are supplied.

Use OCE.3–OCE.8 when a concept, contribution architecture, continuing position, assignment, paired architecture or whole work arrangement must be designed or compared. Bring back that result; do not replace it with a revision label. A product-side change still needs its product or service owner.

Test reversal against the present world. Are the former holder, access, evidence, provider support and recovery conditions still available and permitted? An earlier chart does not restore them. Keep a qualified alternative with its real cost, or return the precise recovery gap.

#### OCE.14:4.4 - Compare complete options under one current basis

Compare the alternatives against the same intended contribution, decision window and current constraints. For each, expose what is retained or surrendered, who bears the loss, effects on continuing service and other commitments, transition work, recovery conditions and uncertainty.

Also distinguish choosing an organization arrangement from choosing how much work to do to obtain that choice. A sufficient competent continuation may be a bounded repair or an authorized temporary recovery while a more ambitious revision waits. Use OCE.8:4.1, especially sufficient-result reuse and the full-effort comparison, to compare that actual continuation with the proposed addition. Keep the receiving result, decision window and protected conditions the same. Name the unresolved relation or condition the addition could settle and the resulting choice it could change; the number of new alternatives is not its payoff.

Reuse the common preparation and qualified participant or provider results in both ways. Include added consultation and design, the actual decision and relation-establishment work, integration, continuing service, later observation and recovery through the same period. Ask the affected participants which other work would wait and whether the answer can arrive before it is needed. Keep their capacity and protected obligations visible even when no credible total of hours is available. Accept the addition for a stated useful difference and an explicit trade-off, or use the competent continuation. If a sufficient decision arrives or the useful window closes, withdraw the now-unneeded inquiry rather than charging its hoped-for benefit to the result. A changed mandatory condition still needs its own response.

Carry non-negotiable conditions separately from trade-offs. An organization owner cannot waive clinical, safety, legal, labor, privacy or financial conditions merely because the organization alternative looks attractive. Obtain the exact applicable result from the qualified owner.

Use C.11 after the options, chooser and comparison basis are defined. The result may be a choice, rejection of the set, further probe or reroute. A probe also needs its own permission, exposure and recovery conditions; choosing to investigate does not authorize arbitrary live work.

Request stronger evidence only where its possible result can change the choice or its permitted scope. For example, an actual double allocation can justify a scheduling repair without proving the overall causal effect of the organization design. If the choice depends on that effect, obtain the appropriate causal and domain evaluation result.

Make accepted losses explicit. A repair that protects service by reducing new change work can be preferable, but the surrendered change contribution remains a real consequence. Do not hide it in an overall success label.

If no currently admissible alternative answers the question, return that result and the smallest missing decision or condition. Do not silently select an incomplete option to keep the programme moving.

#### OCE.14:4.5 - Make the authorized disposition effective

The proper owner performs or obtains the acts required by the actual organization rule and records their result. These may establish, change, retain, revoke or time-limit a decision, assignment, permission or commitment. State the subject, scope, effective time or condition, accepted losses and remaining approvals.

Do not assume one universal authorization ceremony. A member association may need a ballot and a current office holder; an employer may require assignment acceptance and a published allocation; a provider relation may require its own agreement and provision. Apply the rule that governs the actual relation.

A decision can be issued while its operational conditions remain ineffective. Keep those facts separate. Use OCE.6 when the revision changes an assignment or enabling relation. A decision to provide access is not the provision of access, and a revised work allocation is not evidence that the contribution has succeeded.

When authority is missing, return the bounded proposal, alternatives and exact request to the proper owner. Stop the action that depends on that authority. Other unaffected work may continue only under its own existing conditions.

Use the organization's normal record when it preserves the result. The Method requires a recoverable disposition and its limits, not a new universal revision form or central register.

#### OCE.14:4.6 - Return the work and the observation that can reopen it

Give the receiving participants the effective result and the remaining work:

- OCE.9 receives the contribution still to be realized and its acceptance or failure conditions.
- OCE.10 and OCE.12 receive the actual participation, explanation, challenge, leadership or learning-support need.
- OCE.11 receives the permitted overlap, continuing-service protection, recovery and hand-back conditions.
- OCE.16 receives a consequential dependency only if another separately managed change actually uses the altered condition.
- OCE.13 receives the next observation that could change the disposition, including transferred burden or an anticipated effect that fails to appear.

These are conditional returns, not a required circuit through every pattern. A direct owner may already hold a sufficient result.

Retain the reason for the revision, the rejected alternatives and the losses needed for a later decision. Reopen the affected relation when its authority expires, a relied-on condition changes, a protection or service result fails, or observation defeats the intended contribution. Keep unrelated results usable.

What changes in practice is the scope of action: the organization can retain a demonstrated contribution, repair a particular relation and expose the cost and unfinished realization, rather than treating a new diagram as a completed change.

### OCE.14:5 - Archetypal Grounding

#### OCE.14:5.1 - Repairing PumpWorks support while preserving the release contribution

This constructed case continues only after the separately supplied conditions of limited hybrid use. Safety acceptance and release authority remain separately held; the coordination-responsibility predicate is still missing.

OCE.13 supplies a bounded comparison: late evidence returns fell from 8/40 to 3/40, while late service follow-ups rose from 2/20 to 6/20 under the same counting rules. Staffing, incident and product mix remain possible explanations. The comparison does not prove that the hybrid arrangement caused either difference.

For this revision case, additional inputs are explicitly supplied:

- a current assignment and work account confirms that one release-support specialist is committed in incompatible release-checking and service-return intervals;
- the qualified service and employment owners specify protected coverage and a feasible substitute for the delimited support contribution;
- the proper organization owner can change that allocation, but cannot change Safety acceptance or release authority;
- the direct owners confirm that a bounded manual recovery arrangement remains available under its stated conditions.

The revision subject is the support assignment and interval, not the entire organization or the reusable hybrid Method.

| Complete alternative | Retained contribution and loss | Disposition under the supplied conditions |
| --- | --- | --- |
| Keep the present assignment and observe further. | Keeps the familiar release arrangement, but leaves the confirmed interval conflict. | Rejected for the next interval where protected service coverage would fail. It remains the comparison reference. |
| Move the cross-check/support interval and obtain the qualified substitute. | Preserves the weekly release contribution and protected service coverage; reduces the allowance for additional change work. | Selected by the proper owner within its allocation authority. |
| Suspend the affected hybrid contribution and use the qualified manual recovery arrangement. | Avoids the hybrid-dependent support conflict but surrenders its expected contribution and consumes the manual recovery effort. | Retained as a recoverable alternative under the separately supplied conditions. |

The choice uses the direct assignment conflict and qualified coverage result. It does not require an unsupported claim about the hybrid arrangement's full causal effect.

Suppose the required holder acceptance and allocation acts are then performed under the organization's rules. The support interval and assignment become effective at their stated time. That is the obtained relation result. The revised support integration has not yet demonstrated capability or produced a later release result.

OCE.9 receives the remaining integration and representative-use question. OCE.11 receives protected service coverage, reduced change allowance and the hand-back conditions. OCE.13 receives the next comparable evidence-return and service-follow-up observations. If another separately managed change relies on the old support interval, OCE.16 qualifies that particular consumer and returns the direct result to it.

Now remove one supplied condition: protected service coverage is not available. The selected repair cannot take effect as proposed; no substitute is invented. The consequence comparison remains valid at its original scope. The owner must obtain the missing coverage, select another currently permitted alternative or stop the dependent work. The result is not rewritten as successful realization.

**Compare the work of obtaining this revision.** If the ordinary operating review has already delivered the middle-row decision with current coverage, substitute, authority and accepted loss, use it. Applying OCE.14 adds no second workshop or approval. The allocation acts, integration, service protection and observation above remain necessary where unfinished; they are not evidence that the comparison must be repeated.

For a different starting condition, suppose the conflict and manual recovery are qualified, but the substitute's compatibility with current obligations has not yet been established. The receiving question is a permissible support disposition for the next two weekly releases, retaining the release contribution where feasible while protecting service. Competent current management can already answer it by using manual recovery for those two cycles and reconsidering the hybrid repair at the next ordinary allocation review. That is a sufficient bounded answer, not blind rollout or a failed revision.

| Way of obtaining and using the disposition over those two cycles | Work and consequence to compare |
| --- | --- |
| Use the competent current recovery decision. | Reuse the conflict, authority and protection results; obtain any remaining recovery-allocation acts. The existing support participants perform the qualified manual checks and hand-offs, service participants maintain protected coverage, and the ordinary review uses the next evidence-return and service observations. No special substitute-design session is required. The opportunity to resume the affected hybrid contribution is deferred for two cycles; manual work and its stated limits remain real costs. |
| Complete the open support relation before the first release, with recovery if completion fails. | Reuse the same facts and use the qualified manual recovery until the new conditions actually obtain. The service planner, support specialist and proposed substitute jointly resolve compatible intervals and displaced commitments; the proper owners supply the needed coverage and allocation results. The receiving participants then prepare the revised hand-offs and obtain the required integration result before relying on the repair. This adds joint preparation, consultation and transition work, followed by support, service and observation during the same two cycles. If completion misses the cutoff or coverage fails, use the qualified recovery; the extra work is still spent. |

Suppose those participants can resolve the bounded question before the first release only by deferring a noncritical process-improvement workshop, and the owners of that work accept the deferral. The organization owner chooses this addition for the opportunity to resume the hybrid contribution within these two cycles, accepting the joint work, possible unsuccessful completion and the reduced allowance for other change that the repaired arrangement requires. No lower total cost or superior causal effect is asserted. Only if the qualified owners supply the coverage and substitute results assumed in the original branch can the owner select its middle row and proceed to the separate effective acts and realization.

If a current sufficient middle-row decision arrives before the extra session starts, cancel the duplicate session and use the result. If completion can return only after both releases, it cannot earn the stated two-cycle benefit: retain the current recovery disposition and reconsider any later proposal against its later use. In either change of condition, keep the original consequence observations and the independently held Safety and release authority unchanged.

#### OCE.14:5.2 - A good proposal after an association chair's term

A standards association has evidence that an editorial-return assignment delays member review. The proposed reassignment is reasonable, volunteers are willing and the repository can support it. The current chair's term has nevertheless ended, and the bylaws do not give that former holder the required decision authority.

OCE.14 returns a bounded proposal and the exact current authorization question to the association's governance owner. It can preserve ordinary interim work only to the extent already permitted by the applicable rules. It cannot extend the term, manufacture employer commitments or treat volunteer agreement as a substitute for the required decision.

After an authorized decision-maker supplies a current decision, use OCE.6 to establish the specific assignment and access relations where needed. Carry out the later editorial work under those effective conditions. Adopting the standard still requires its own decision.

#### OCE.14:5.3 - Protective action before causal attribution

A hospital's qualified safety owner supplies a current requirement to pause one organization-flow trial under a stated patient-protection condition. The available waiting-time comparison has changed case mix and cannot attribute an overall effect.

OCE.14 can carry the actual authorized pause and its organization scope while preserving the unresolved causal question. It cannot alter clinical treatment, statutory responsibilities or protection requirements by preference. A favorable median waiting time supplies no missing authority to continue.

### OCE.14:6 - Bias-Annotation

Action bias favors a visible redesign over a sufficient correction; ask which relation is actually defeated. Sunk-cost bias favors continuing an arrangement despite a lost premise; keep stopping and reversal visible. Restoration nostalgia treats an old arrangement as still available; verify present recovery conditions.

Sponsor power can hide burdens accepted by someone else. Identify the affected parties and the actual authority for each trade-off, keeping professional and protected conditions outside ordinary compensation.

### OCE.14:7 - Conformance Checklist

- [ ] The challenged organization relation or condition and its current evidence are identified separately from a proposed design.
- [ ] The actual decision scope, owner, effective interval and hard constraints are recovered.
- [ ] Direct correction, realization, Method repair and strategic questions are distinguished from organization revision.
- [ ] A sufficient current revision is reused; otherwise materially different complete alternatives answer the unresolved question and include an honest current reference and any feasible repair, stopping, recovery or probe branch.
- [ ] Comparison preserves contribution, losses, burden-bearers, continuing service, transition, uncertainty and recovery; any added revision work has a useful difference and accepted trade-off covering the whole effort against the competent current continuation.
- [ ] The authorized acts and any remaining ineffective conditions are stated without implying realized capability.
- [ ] Missing authority, protection or external results stop only the dependent action; no replacement or approval is invented.
- [ ] Receiving work, conditional cross-change consumers and the observation that can reopen the disposition are explicit.

### OCE.14:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Better move |
| --- | --- |
| “One metric worsened; redesign the whole organization.” | Recover the challenged premise and the smallest revision that can answer it. |
| “The sponsor approved it, so every condition is satisfied.” | Separate the sponsor's scope from other authority, protection, assignment and provision results. |
| “The revised chart is now the organization.” | Identify which decisions and relations actually took effect and which contribution remains unrealized. |
| “We can always roll back.” | Qualify the former holder, access, obligations, support and present recovery conditions. |
| “Wait for full causal proof before any response.” | Match evidence to the actual decision; a qualified risk or direct relation conflict may support a bounded authorized response. |
| “The new assignment solved service and capability.” | Observe the receiving work under the changed conditions; an effective relation is not its later performance. |

### OCE.14:9 - Consequences

A useful contribution can survive a revision while its failing support or assignment changes. The decision owner sees the real losses, authority boundaries and unfinished work, and later observers know what result could defeat the disposition.

A sufficient existing revision can end the comparison without another study. Where an organization question remains, completing alternatives, obtaining relations and carrying the chosen change into use consume real participant and support work. An addition may be worth that price without being cheaper; it may also be declined in favor of a sufficient current disposition. A revision may remain a proposal, a choice with pending conditions or a stopped dependent action. Those are usable results when they make the next work clear.

### OCE.14:10 - Rationale

An organization is changed through actual relations and contributions, not merely through its description. Consequence evidence therefore has to reach a concrete revision subject and a legitimate decision, while the selected arrangement still has to become usable.

Separating comparison, authority, effectivity and realization lets a practitioner act at the justified scope. It also preserves the value of a good observation when a repair is blocked, and the need for further observation after an authorized repair. A capable existing review can supply the comparison or decision already. The reason to add work is an unresolved organization question whose answer is worth obtaining in time, not the availability of another method description. Comparing organizational options alone cannot establish that repeating their construction is worthwhile.

### OCE.14:11 - SoTA-Echoing

The practice question is how to obtain a justified, timely organization revision after consequences or changed conditions defeat a current premise. Competent adaptive management is the serious current alternative: it can use existing evidence, compare feasible repairs and recovery, involve affected participants, obtain the proper decision and return remaining work. When that practice supplies a sufficient current disposition, it is the selected answer; §4.2 and §5.1 use it without a second construction or OCE approval.

**Adapt the connection from evidence to action.** The [Magenta Book (HM Treasury, 15 May 2026), §§6.1–6.2](https://www.gov.uk/government/publications/the-magenta-book/magenta-book-central-government-guidance-on-evaluation-html) relates evidence use to the recipients, decision timing, proportionate information and their capacity to act. The [MRC update (Skivington et al., 2021)](https://doi.org/10.1136/bmj.n2061) contribution is context-sensitive, iterative reconsideration of consequential uncertainty. These sources strengthen the competent comparator; they do not supply a local organization mandate or demonstrate OCE's effectiveness. Section 4.4 retains stronger causal inquiry where it changes the decision, while direct qualified relation facts can suffice for a bounded revision.

**Add only the unresolved organization construction.** Separate the result sought from the way of obtaining it, including authority, support, first use and sacrificed work. Where an existing disposition leaves a consequential relation question open, §§4.3–4.5 connect the actual OCE.3/.6/.8 and C.11 contributions to its completion. PumpWorks compares a competent two-cycle recovery with completing a compatible support assignment in time. The latter offers an earlier opportunity to resume the hybrid contribution, but adds joint work and transition, defers another workshop and accepts reduced change allowance and the risk of unsuccessful completion. The owner accepts that trade-off; comparable total effort or general superiority is not claimed. If ordinary review already supplies the repair, or the answer would arrive after its useful window, no such extra work earns that payoff.

Blind rollout and automatic full redesign remain rejected failure modes, not substitutes for this comparison. The organization-specific contribution is to complete a missing relation and carry its actual effectivity and unfinished work to their owners. Reopen only the affected choice when a stronger available disposition, changed burden or timing, expired authority, unavailable recovery or later consequence changes its basis. Obtain local service, clinical, employment and other protected results from their qualified owners; a source-guided comparison cannot waive them.

### OCE.14:12 - Relations

[C.11](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11---decision-theory-decsn-cal) supplies choice after the options, chooser and basis are formed. A.3.4 distinguishes the actual bounded change; A.10 and G.11 support evidence and currentness for the relied-on claims.

OCE.13 supplies a qualified consequence comparison when needed. A current direct owner result can also enter OCE.14 without a general observation exercise. OCE.1/OCE.2 recover the organization and actual relations when those are uncertain.

OCE.3–OCE.8 supply the applicable concept, contribution, position, assignment, paired-architecture or whole-arrangement result. OCE.8:4.1 supplies sufficient-comparison reuse and the comparison of common and added work for a needed extension. OCE.6 establishes obtaining assignments and enabling relations; OCE.9 realizes the contribution; OCE.10/OCE.12 support participation and leadership; OCE.11 coordinates change with continuing service.

OCE.16 handles an actual consequential dependency on a condition another separately managed change uses. OCE.15 and Method Engineering receive a reusable-Method defect; OCE.17 can receive evidence about continuation of OCE practice. Obtain the required authority, professional evidence and actual work results from their respective owners.

### OCE.14:End

# Part V - Sustain Methods, Cross-Change Coordination, and OCE Practice

## OCE.15 - Choose, Develop, or Refresh Organization-Change Methods

> **Type:** Method pattern
> **Status:** Stable
>
> **Primary working result:** an **organization-change Method development-and-repertoire result for a named use**. It contains either a repaired named-use repertoire, a bounded OCE candidate Method account prepared for Method Engineering qualification, or both, while keeping intervention contributions, implementation functions, situation claims, mechanisms, source/evidence limits, authority/capability/support conditions, affected Systems, outcomes, and refresh triggers distinct.

### OCE.15:0 - Use This When

Use this pattern when practitioners need to choose, combine, construct, adapt, explain, or replace ways of changing an organization and the available material mixes stage models, intervention lists, implementation strategies, process models, determinant accounts, evaluation frames, local routines, consultancy packages, research findings, tools, training, and remembered practice.

Begin with the organization-change situation and the next OCE result. Choose one or both branches:

1. **Repertoire branch:** recover, qualify, compare, select, and refresh the smallest set of Methods, candidate accounts, and source contributions for the named use.
2. **Domain candidate branch:** obtain a proposed reusable way of changing an organizational contribution. Recover where a current attempt fails, work from the receiving need back to the action that could supply it, and connect that action to the participants, conditions and returns it needs. Explain why the proposed intervention should address this difficulty, what would defeat it, and what can vary on another occasion. Then use Method Engineering for the applicable qualification, trial, fit, worth, variant and introduction decisions.

A sufficient current Method or result can finish the use directly. Otherwise the first useful result can be a small inspectable repertoire, an explained candidate procedure, or an honest blocker at a named missing operation or condition. Do not use OCE.15 to declare a branded framework universally effective, turn an intervention label into a Method, infer adoption from participation, or treat a project, process, or case view as the Method.

#### OCE.15:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| organization-change Method | An independently admitted reusable way of obtaining or preserving an OCE result under stated applicability and limits. |
| candidate Method account | An episteme describing a possible reusable way of doing while identity or applicability remains open. Track admission separately from inclusion in the repertoire. |
| intervention contribution | A bounded action, support, participation, communication, reinforcement, structural, or other contribution proposed for an OCE result. A label may be too coarse to identify a Method. |
| implementation strategy | A bounded contribution intended to improve implementation of an innovation or way of working. It is neither automatically a complete Method nor the implemented result. |
| process model | A description organizing implementation activities or temporal dependencies. Recover the reusable Method and actual Work separately. |
| determinant account | Claims about conditions that may enable, hinder, or explain implementation. Obtain an action sequence and any needed causal support separately. |
| evaluation frame | Questions, characteristics, measures, and comparison rules used to evaluate implementation. It is not an intervention. |
| implementation outcome | A result such as acceptability, adoption, appropriateness, feasibility, fidelity, cost, penetration, or sustainment for a named referent and window. Report it separately from the intended outside organization contribution. |
| organization result | The operating, contribution, coordination, capability, human-condition, customer, or other affected-System result whose change matters. It remains distinct from implementation activity and outcome. |
| intended mechanism | An explanation of how a contribution could change a named condition. State whether it is a hypothesis or has qualified causal support. |
| decision-sensitive situation claims | Claims about named Systems, relations, conditions, histories, resources, authority, technologies, institutions, populations, and continuing Work that can change selection or fit. |
| situation-change account | Observed or anticipated changes in those facts and the observation that reopens a fit, mechanism, support, status, or selection claim. |
| Method repertoire | The smallest inspectable set of admitted Methods, candidate accounts, source contributions, statuses, relations, evidence limits, gaps, and selection positions for one use. |
| MethodDescription and its carrier | A description states Method content; a file, book, card, software tool, or other medium carries that description. Training can use descriptions and carriers as support. Recover the Method described separately. |
| participation and adoption | Record actual participant contributions and relations. Qualify adoption for a separate bounded referent and window; assess capability, retention, effectiveness, and culture with the evidence required for each claim. |

### OCE.15:1 - Problem Frame

Recognizable schools and recipes make communication cheap but hide unlike functions: diagnosis, participation, strategy, process guidance, determinant analysis, evaluation, training, reinforcement, structural change, resource provision, and cultural work. A complete sequence is often applied when one bounded repair would do.

A useful OCE Method result therefore preserves what each item is for, its candidate or admitted status, situation claims, mechanism hypotheses, implementation outcomes, organization results, and adaptation triggers. The harder situation is a competent current practice that obtains today's result with help, while a changed receiving contribution exposes a missing reusable move. The practitioner must decide whether to keep that adequate supported continuation, repair its conditions, or develop a different procedure. Naming the desired fields in a procedure does not make that choice or construct its actions.

### OCE.15:2 - Problem

A method base can become a shelf of brands. Popularity is treated as admission; a local success as effectiveness; a changed slide deck as a Method variant; attendance as adoption; a determinant framework as an intervention; and a favorable implementation outcome as the organization result.

When results disappoint, practitioners cannot tell whether the problem lies in Method semantics, description, performer capability, authority, support, implementation, changing conditions, measurement, or the organization concept.

### OCE.15:3 - Forces

| Force | Tension |
| --- | --- |
| Practical speed | Teams need a contribution now, while Method identity and evidence cannot be granted by a familiar label. |
| Repertoire breadth | Several mechanisms prevent recipe lock-in, while an encyclopedic catalogue is unusable. |
| Domain development | OCE must supply domain semantics, while general Method identity and qualification remain in Method Engineering. |
| Changing conditions | Stable criteria support reuse, while situation facts change during organization-change Work. |
| Bundles | Contributions can complement one another, while interactions, burden, and causal contribution are hard to isolate. |
| Participation | Involvement can improve information, while it can be symbolic, burdensome, unsafe, or outside authority. |
| Evidence | Reviews improve grounding, while heterogeneous measures and settings limit transfer and causal claims. |

### OCE.15:4 - Solution

Start from the receiving OCE result and inspect the adequate current answer before choosing the repertoire branch, domain candidate branch, or both. Preserve every item’s function and status. C.39 supplies the general way to recover, connect and change operations; the current Method Engineering Principles Framework supplies general focus, repertoire, criteria, description development, qualification, trial, fit/transfer, worth, variant/provenance and introduction/revision. Use those contributions directly where they answer the question. Sections 4.1.1–4.1.2 below fill the organizational connection: how evidence about a failed contribution changes an intervention, and when developing that intervention is worth adding to competent current work.

Recognition is cheap: a named recipe with no inspectable function, status, situation, evidence boundary, or receiving result is enough to enter. Assurance is claim-specific: Method admission, source reliance, situation fit, actual Work, contribution, implementation outcome, and organization result remain separate.

#### OCE.15:4.1 - Pattern-Use Unfolding

1. **Name the receiving OCE result.** State organization, contribution, OCE question, receiver, horizon, decision authority, and stop. Do not begin from a framework name.
2. **Try the sufficient answer, then choose the branch.** Inspect what the current procedure or supplied result lets the receiver do, including necessary assistance. Use it when it answers the named need; do not repeat its classification, construction or trial. If a consequential question remains, state whether it requires repertoire repair, domain candidate construction/adaptation, or both. Name the missing result.
3. **Recover current items and functions.** Identify admitted Methods, candidate accounts, observed routines, intervention or implementation-strategy contributions, process models, determinant accounts, evaluation frames, support, and actual Work. Preserve status and function.
4. **Qualify source contributions.** Record source and edition, population and setting, claim used, measures, evidence design, reported limits, and the OCE decision that the source can change.
5. **Record decision-sensitive situation facts and changes.** Name the Systems, relations, conditions, histories, resources, authority, technology, institutions, populations, and continuing Work that matter. Record observed or anticipated changes and the reassessment trigger.
6. **Obtain the missing reusable move.** Follow section 4.1.1 from the difficulty and competing explanations to a changed action, its receiving result and the reason for that connection. Explain a mechanism when its distinction changes the intervention or its use, retaining whether it is a hypothesis or an evidence-supported claim. Inability to perform a contribution and lack of access can require different repairs. Investigate other human or organizational conditions only when they can change this decision; do not complete a fixed factor list.
7. **Recover capability, support, authority, and protection.** State who must be capable, assigned, permitted, and authorized; needed tools, data, forums, providers, time, resources; and affected Systems needing representation or specialist protection.
8. **Recover what each account is about.** A project account may concern future commitments and resources, a process account a reusable procedure, and a case account one unresolved authority claim. Keep those subjects distinct and relate their needed contributions. When the accounts actually concern the same performed Work, project, process and case viewpoints can expose different aspects of that Work. Use A.15.6 and ME.1:4.1 for this distinction; use ME.9 only when a needed correspondence between accounts remains unclear.
9. **Compare individual items before bundles.** Ask which item can supply the remaining contribution. For a bundle, follow what each action makes possible or obstructs for the others, including simultaneous participant demands. Restrict, replace or remove a contribution that defeats the whole. Apply section 4.1.2 before paying for further development.
10. **Complete the repertoire branch.** Return the smallest qualified set, visible gaps, selection or probe, and refresh triggers. State whether the selected items remain separate or have been qualified as one composed Method.
11. **Return the explained candidate for the decision it needs.** Use ME.8 to make the obtained rule or professional judgement executable from its description. Supply the operations, reasons, conditions and unresolved claims developed below, rather than asking the recipient to invent them from a table. ME.5 can qualify the candidate; ME.11 obtains selected trial evidence; ME.13 judges fit/transfer; ME.14 compares worth; ME.15 distinguishes a semantic variant from a description or support change; ME.16 introduces and revises the selected way. Obtain only the results required by this use. A written procedure remains a candidate until the relevant qualification supports a stronger claim.
12. **Observe and refresh the smallest claim.** Bind Work, participation, implementation outcomes, organization results, and unintended consequences to the item, semantics, population, conditions, and window. Refresh only the defeated claim.

##### OCE.15:4.1.1 - Construct a procedure from the failed or needed contribution

**Recover the break in ordinary work.** Start with an instance in which someone could not take the needed next action, or with a proposed action whose prerequisite is visibly missing. Use OCE.2 to recover what was done, requested, supplied and understood, with the disagreements and evidence limits intact. Follow the receiving action: what must its holder know, receive, be able to do or be permitted to decide? Compare that requirement with what the contributor actually supplies. A late report, a refusal and an unavailable decision can have different causes. Retain competing explanations until the available evidence distinguishes them; useful observations need not wait for a complete account of the organization.

**Locate what needs changing.** Inspect the current way with the people who perform and receive the contribution. If its rule already answers the difficulty, correct its description, access, assignment, support or execution as appropriate. If the technical answer is unknown, obtain that professional contribution; an organizational workshop cannot manufacture it. A Method-development question remains when a reusable choice, joining action or return is missing or no longer fits. For example, both parties may know how to produce and interpret evidence, yet have no rule for settling which scope the receiver needs before production begins. That is a different defect from an unreadable version label on an otherwise adequate instruction.

**Work backward from the receiving result and then forward through the intervention.** Apply C.39:4.3: identify the result the receiver needs, the operation that could supply it and the mismatch between them. For an organizational handoff, recover the producer's contribution, the consumer's consequential action, the scope and timing each assumes, and the authority and continuing work that constrain their interaction. Construct the smallest action that can resolve the mismatch. It might ask the receiver to state a concrete use, have the producer test that request against what can be supplied, and return the disagreement to the person able to change the requirement or provision. Follow the answer forward: does it now let the receiver act, or does it merely add another report? OCE.3 can supply an organizational option; OCE.4 explains the proposed relations and OCE.6 obtains the actual assignments and conditions needed to realize it. Their descriptions do not themselves make those relations obtain.

**Select the intervention by the difference it can make.** Compare actions that address the live explanations. Earlier notice helps if the missing condition is preparation time; a scoped producer–consumer comparison helps if the two parties assume different required results; practice with feedback helps a learnable performance gap. Training cannot settle an absent decision right. For the selected action, explain why the observed difference makes its expected contribution plausible and which observation would contradict it. ME.16:4.5 supplies the distinction between failed delivery, an unsupported mechanism, changed conditions and hidden extra support. These alternatives determine what to observe; they are not a demand for a complete causal study or psychological diagnosis before every change.

**Construct the interaction as well as each action.** Select participants because they supply, use or can change a consequential contribution, not just because they are influential. ME.8:5.4 develops that working-dependency reasoning. Give a disagreement a usable return: who can answer which question, and what continues while it remains open? Compare the proposed joint activity with continuing service and protected work. If a workshop improves information exchange but removes the only service specialist from duty, separate the recoverable information contribution from simultaneous attendance. Obtain a permitted account first and reserve a smaller joint discussion for the unresolved dependency. If safe participation or needed evidence is unavailable, retain that gap and a feasible continuation; refusal can reveal an invalid arrangement rather than a defect in the person.

**Make the proposed way repeatable and revisable.** Distinguish the organization-change procedure from the operating routine it may introduce. The first might recover and repair an evidence handoff; the second governs the later releases. Explain the variable inputs, retained conditions, action, result and return for each claimed reuse. C.39.RO:4 supplies the move from case choices to a reusable operation. Replace a particular person's name with the contribution and decision condition the next use requires, not with an unrestricted “stakeholder”. Keep the technical acceptance rule with its qualified supplier. Follow a materially changed condition through the affected action and its consumers; preserve independent contributions. Return the resulting account to the selected ME decision with what is known, proposed and still untested. Do not infer repeatable capability or effectiveness from this construction.

##### OCE.15:4.1.2 - Decide whether to add development work

Use ME.14's comparison for the same receiving result, horizon and protected conditions. A competent current implementation effort may already identify the relevant determinants, design and adapt the intervention, pretest its materials and obtain adequate use with support. Implementation Mapping is one such constructive approach, not merely a source of labels. A sufficient result from it or another qualified Method is a real finish here. Use the resulting procedure or supported continuation directly.

When a residual question matters, compare the complete continuation with and without the proposed addition. Retain common work on both sides: source and situation recovery, relevant participants, technical and organizational design, authorization, assistance, qualification and testing, integration, continuing service, observation, upkeep and failure recovery. Add development, learning and recurring burdens where they actually arise, including work displaced for participants and providers. Do not count a facilitator's presence as free, or remove that help from the proposed line before evidence supports doing so.

Name the attainable difference and the decision it could change. An addition may warrant more effort because it can settle, before a handover, which parts of a contribution a successor can perform with specified support. That is an accepted cost for a bounded allocation decision, not an established saving or general capability. Keep the adequate current arrangement as the fallback. If an existing qualified procedure already answers the handover question, or the observation will arrive after the allocation must be made, cancel that addition for this use. A later development opportunity needs its own worthwhile receiving question.

#### OCE.15:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| named use and branch | Organization, contribution, receiving OCE result, receiver, horizon, authority, stop, and selected branch or branches. |
| item identity/status/function | Method or candidate; separate intervention strategy, process model, determinant account, evaluation frame, description, carrier, tool, training, support, WorkPlan, actual Work, and local routine. |
| domain candidate semantics | Explained transition from difficulty and evidence to changed operations and their relations; why the candidate addresses the live explanation; retained and variable conditions, stops and failure returns; participants, authority, capability, support and protection; bounded mechanism and evidence claims. |
| situation facts and changes | Decision-sensitive facts, observed or anticipated changes, and reassessment triggers. |
| implementation and organization results | Implementation outcomes with referent/window and distinct intended organization results. |
| sources/evidence | Source edition, population, setting, measures, design, used findings, limits, qualification window, and unintended-consequence questions. |
| accounts and their subjects | What each project, process or case account concerns, including any selected organizational or Method-related structure; the needed correspondence or use; common-Work viewpoints only when that Work is their shared subject; material omissions and losses. |
| alternatives/bundles | Sufficient current answer, remaining question, individual qualification, interaction, full common and additional burden, displaced work, attainable difference, accepted trade-off, uncertainty and status. |
| disposition | Repertoire, candidate return to ME, selected item/set/probe/stop, authority, alternatives, and next action. |
| refresh | Defeated claim, observation, currentness/retirement meaning, preserved history, and external return. |

#### OCE.15:4.3 - What Changes in Practice

Practitioners can finish with an adequate current way, repair a condition of its use, or obtain a proposed procedure from a specific missing organizational contribution. They can explain why a scoped comparison, changed participation arrangement or other intervention follows from the evidence, what it costs beyond competent current work, and which changed condition removes its purpose. They retain distinct strategy, process, determinant, evaluation and outcome claims, then use Method Engineering for the required general Method decisions.

### OCE.15:5 - Archetypal Grounding -- PumpWorks Method Result

PumpWorks needs ways to support current-relation recovery, concept comparison, participation, and a bounded capability increment while service continues.

| Item | Function and status | Situation/mechanism hypothesis | Evidence boundary and next use |
| --- | --- | --- | --- |
| `C-PW-PARTICIPATORY-WORK-RECOVERY` | Candidate Method account: reconstruct one release case with protected contributions from Product, Electrical, Software, Safety, Field Service, platform, and provider participants | Opportunity to contribute, meaning, and belonging may improve information quality; participation adds burden and may be unsafe | Use as an `OCE.2` evidence probe only with authority, confidentiality, and burden limits |
| `C-PW-EVIDENCE-RETURN-REPAIR-TRIAL` | Candidate organization-change procedure: recover a failed evidence handoff, compare the receiver's required scope with the supplier's available contribution, construct and rehearse a scoped request/return, and obtain the separate conditions for its bounded introduction | Making the scope mismatch discussable before integration may prevent unusable evidence returns; expert mediation remains a rival explanation of success | Constructed below; no trial result is supplied. The proposed operating routine keeps Electrical production, integration use, Safety acceptance and release authorization distinct. A successful occurrence would not establish whole-organization capability |
| `C-PW-STREAM-ENABLING-INCREMENT` | Candidate account for one stream-aligned increment with enabling Safety and platform contributions | Shorter handoffs may improve coordination; scarce-specialist overload and identity loss compete | Team Topologies is a concept source, not effectiveness proof; assignments, authority, access, coexistence, and service evidence are required |
| `C-PW-PROVIDER-HYBRID-INCREMENT` | Candidate account expanding provider contribution under named access, assurance, exception, recovery, and release-authority relations | External capacity may improve ability; dependence, knowledge loss, and authority ambiguity may worsen results | Provider commitment and authority are unresolved; selection stops until those results exist |
| `PW-QUARTERLY-HANDOFF-PRACTICE` | Observed local-practice account, not an admitted Method | Current coordination may preserve specialist assurance but contribute to delay | Keep as evidence; use ME candidate recovery only if reusable semantics are needed |

For this use, participatory Work recovery is an implementation-strategy contribution inside a candidate Method. The release-case sequence describes the process; claims about missing rig access and authority form a determinant account; the evaluation frame supplies the questions for the measurement plan. Record actual participation separately. Assess feasibility, fidelity, and sustained use as distinct implementation outcomes, and weekly evidenced releases with continuing safe service as organization results. Use the evidence appropriate to each question.

#### OCE.15:5.1 - Derive the evidence-handoff repair

Consider a stipulated continuation with qualified Electrical, integration, Safety and release holders, permitted evidence access and protected service coverage. These are case inputs, not results produced by writing the procedure. Three sampled release records show compatibility evidence supplied on time. In two, integration asked for a further configuration after Electrical had completed its check. The producer and receiver confirm that the current routine says when to upload evidence but leaves who settles its requested scope unspecified. Both can perform the technical checks. A competent facilitator currently settles the scope through separate conversations and can continue doing so for the next four weekly releases.

These observations weaken “send the report earlier” and “teach the technical check” as the first repairs. They do not prove that scope negotiation causes every delay: access, workload or an unusual technical condition may still matter. The missing reusable move is how producer and receiver settle the needed contribution before its production. The practitioner constructs the candidate as follows.

| Evidence or dependency | Operation obtained from it | Result used next, and limit |
| --- | --- | --- |
| The receiver's later request changes what evidence is needed. | Ask the integration holder to use one concrete upcoming integration decision to state the configurations and compatibility claims it must receive, using the qualified technical criteria. | Electrical receives a scoped request to compare with its planned check, not a generic request for “more communication”. |
| Electrical can perform a check but cannot promise every requested configuration in the available window. | Have Electrical return what it can supply, what the request leaves ambiguous and what would require a changed plan. Put only the unresolved difference before the holders who can change that requirement or provision. | An agreed scope or an explicit unresolved dependency. A meeting's agreement does not grant resources or release authority. |
| A supplied file previously concealed that difference until integration. | Rehearse a normal request and a changed-configuration request. The receiver compares the returned evidence scope with the intended use and returns a mismatch instead of treating upload as completion. | A concrete continuation or stop can be inspected before introduction. Safety still issues its own acceptance result; the release director still decides release. |
| The facilitator's separate conversations may be doing essential work. | Explain the comparison and return rule in the candidate, then select an ME.11 observation that records when the facilitator must resolve an unprovided judgement. | Evidence can distinguish following the supplied rule from succeeding through hidden mediation. An unresolved professional judgement is returned for development, not counted as independent use. |

This constructs two related accounts. The organization-change procedure recovers the failed dependency, elicits the paired accounts, resolves or returns their difference, rehearses the proposed routine and obtains its introduction conditions. The target operating routine asks for, produces, checks and returns evidence on the settled scope. OCE.6 supplies actual assignments, access and decisions; OCE.9 uses those conditions for bounded realization. OCE.15 has not obtained them by describing their place in the procedure. ME.8 can now develop the explanation from known actions; ME.5 and ME.11 can judge and examine a candidate with inspectable operations. The trial stops on a safety or protected-service breach and returns the dependent realization to its responsible holder.

The initial intervention proposal brought every affected participant into a standing workshop. Field Service reports that this would interrupt protected diagnostics. More participation would help recover exceptions while defeating continuing service. The practitioner therefore obtains a permitted account of the service constraint asynchronously and reserves joint discussion for the remaining producer–receiver disagreement, with a service representative only when that question requires one and coverage permits. If the decisive condition cannot be represented safely, the candidate retains the gap and supported current continuation. The refusal changed the intervention; it was not reclassified as resistance.

The reusable action is to compare a receiver's concrete needed contribution with what its producer can supply, then resolve or return the difference before relying on the contribution. The case-specific configurations, named holders and meeting format may vary. Qualified technical criteria, legitimate decisions and protected continuing work remain conditions. If inspection instead finds that the current routine already supplies this rule and the only defect is a misleading instruction, repair the instruction and cancel this Method-development proposal. If the scope comparison reveals an unsolved technical test, return that test to its professional owner and retain the useful request and uncertainty; the organizational procedure does not invent the test.

#### OCE.15:5.2 - Price the addition against a sufficient continuation

For the same four weekly evidenced releases with safe service, competent facilitator-assisted practice is sufficient. Assume a new integration holder is to take over during this window and one protected overlap period is available before the third release. The release director may retain expert attendance for all four releases; there is no requirement to develop a new Method. The optional remaining question is whether a specified scope-comparison contribution can be allocated to the incoming holder, with stated standby support, for the last two releases. This must be decided while the current holder and facilitator can still examine the attempt. Any released expert attention has a named use: two nonroutine interface reviews currently wait behind routine scope-setting. Their earlier slots must be reserved before the third release; otherwise the later schedule remains. Keeping those reviews later is acceptable, so the incumbent remains sufficient; bringing them forward is the additional benefit under consideration.

| Work and condition | Continue the competent current way | Develop and examine the proposed procedure |
| --- | --- | --- |
| Common preparation and delivery | Use the existing situation account, technical criteria, authorized holders, provider/access conditions, service coverage, ordinary handover, evidence production, Safety acceptance and release decisions. | Retain all of that work and its costs. The new description does not replace technical assurance or organizational realization. |
| Coordination and assistance | Fund the facilitator's scope-setting conversations and attendance throughout the window, including exceptions and recovery. This is a feasible complete answer. | Reserve the same assistance and fallback until the bounded observation supports a different allocation. Count every intervention by the facilitator as support used. |
| Additional development and examination | No new construction or special trial; ordinary monitoring and instruction upkeep continue. | Recover the three cases with producer and receiver; design and explain the comparison/return rule; obtain the service account; qualify the candidate; rehearse normal and changed requests; observe its use; compare results and burdens; maintain or withdraw the account. Count participants, author, facilitator, technical reviewers and any provider effort. |
| Time and displaced work | Current holders spend time on repeated mediation; the incoming holder receives the ordinary supported handover. | The protected overlap is spent on construction, practice and observation. An agreed noncritical improvement is deferred; protected service is not borrowed. Later exception handling, updating and possible return to facilitated work remain costs. |
| Attainable choice | Retain facilitated operation for the remaining releases, with the nonroutine reviews later in the window. | If the selected evidence supports the bounded contribution, allocate it to the incoming holder with specified standby support and bring the expert reviews forward; otherwise retain the facilitated operation and its schedule. General capability, sustained independence and total savings remain unestablished. |

The director accepts the additional work and the deferral of a noncritical improvement to try transferring routine scope decisions and bringing the two expert reviews forward. The observation during the unique overlap can still change that allocation; a later observation cannot recover that scheduling opportunity. This is an explicit priority trade-off with a possible bounded benefit, not a promised reduction in hours. If the evidence does not support the transfer, the development has incurred its cost without obtaining that benefit. The plan keeps the incumbent feasible even if the candidate fails. A complete current Method result that already supports this handover removes the development work. If the incoming holder or the decisive observation becomes available only after the third-release allocation, the time-specific payoff disappears: retain expert attendance and stop this inquiry for the current window. Preserve the observations for a later use without treating them as an achieved saving.

#### OCE.15:5.3 - Keep account subjects and unlike participation conditions visible

The four-release plan concerns future commitments; the new procedure account concerns a reusable way; the unresolved provider-authorization case concerns one permission claim. They are connected because the plan needs authorized provision and a usable way of coordinating it, not because they are three views of one performed Work. After a particular release actually occurs, accounts of its commitments as performed, recurring contributions and exception decisions may all concern that release Work. Recover that common subject before using the viewpoint relation.

In a professional association, the difficulty may instead be an unresolved editorial contribution: members in several time zones can review a draft but cannot attend a compulsory joint session. Recover which disputed claims the editor needs resolved and which members can supply the relevant experience. Compare written, scoped questions with a live discussion; obtain permitted extracts when the full case is confidential. Return conflicting answers to the editor with their reasons rather than treating majority attendance as agreement. An expired chair's authority cannot be replaced by member participation, so the dependent decision waits for its legitimate holder while permitted review continues. Here the same construction changes the participation form and preserves a separate authority gap; it does not import PumpWorks assignments or require a volunteer to accept an employment-like obligation.

Attendance records in either situation support an attendance claim. Decision-bearing contributions, adoption, capability and organization results require their own evidence.

### OCE.15:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| brand-recipe bias | A framework is treated as one admitted universal Method. | Recover reusable contributions, function, status, sources, and situation limits. |
| framework-function collapse | Determinants, process, strategy, evaluation, and outcomes become interchangeable. | Record each item’s function and receiving use. |
| stage-sequence bias | A teaching or project order becomes a lifecycle. | Preserve dependencies, overlap, early stops, and several views. |
| participation-romance | More involvement is assumed beneficial and harmless. | State purpose, authority, protection, burden, missing voices, mechanism, and consequences. |
| resistance label | Capability, authority, resources, incentives, access, mastery, meaning, belonging, participation, or protection collapse into a person defect. | Diagnose the named condition or relation. |
| static-situation bias | Conditions are assessed once. | Record changed facts and reassessment triggers during change and continuing Work. |
| evidence inheritance | Findings transfer automatically to an adaptation or bundle. | Bind evidence to semantics, population, conditions, alternatives, and window. |
| carrier-as-Method | A playbook, course, tool, canvas, or workshop becomes the Method. | Keep Method, description, carrier, support, Work, and result distinct. |

### OCE.15:7 - Conformance Checklist

- [ ] The result names the receiving OCE use, authority, stop, and repertoire/candidate branch.
- [ ] Every item retains its identity, status, function, and limits of supported use.
- [ ] Candidate construction explains how the difficulty and evidence select the changed operation, why its results connect, and what defeats or alters that choice; general Method decisions return to the named ME results.
- [ ] A sufficient competent current answer can finish; any addition has a remaining question, full effort comparison and an attainable benefit or explicit accepted trade-off.
- [ ] Situation claims state the relevant facts, their observed or anticipated changes, and what those changes mean for use.
- [ ] Strategy, process model, determinant account, evaluation frame, implementation outcome, and organization result remain distinct.
- [ ] Mechanisms remain hypotheses or evidence-bearing claims.
- [ ] Capability, assignment, permission, authority, access, support, provider commitment, and protection remain distinct.
- [ ] Each project, process or case account retains its direct subject; a common-Work viewpoint claim is used only when that subject is actually shared.
- [ ] Bundles expose overlap, interactions, contradictions, burden, and status.
- [ ] Refresh names the smallest defeated claim and preserves unaffected uses and history.

### OCE.15:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Kotter versus ADKAR: choose one.” | Recover contributions, functions, mechanisms, situations, evidence, and smaller alternatives. |
| “Use CFIR as the change Method.” | Use a determinant account only for the bounded questions it answers; choose or construct action separately. |
| “Communication and training handle resistance.” | Identify the condition that defeats the contribution or makes participation unacceptable. Choose a repair for that condition; training requires a learnable contribution to repair. |
| “We tailored the slides, so this is our Method variant.” | Send changed reusable semantics to ME; otherwise maintain the description, support, or local Work result. |
| “Everyone attended, so adoption and success are proven.” | Obtain separate participation, implementation-outcome, organization-result, capability, retention, and culture evidence. |
| “The process view is our change Method.” | Recover what the account concerns and the actual way of acting. A diagram of performed work, a future plan and a reusable procedure need not have the same subject. |

### OCE.15:9 - Consequences

The organization can maintain plural change Methods without arbitrariness and can develop domain candidate semantics without duplicating general Method Engineering. Practitioners see why an item is present, what it can do, which conditions and mechanisms are assumed, and what outcome it can and cannot establish.

The cost includes obtaining the missing organizational knowledge, constructing and explaining the intervention, participant and specialist time, support, qualification, observation, upkeep and displaced work. A competent current way may be cheaper and sufficient. Popular interventions can remain source contributions or candidate accounts; bundles need explicit interaction reasoning; selected candidates can still fail in actual Work. Retaining a supported continuation after a failed candidate is a useful decision, not evidence that the proposed new Method worked.

### OCE.15:10 - Rationale

Organization-change Methods address changing organization relations, affected people and Systems, distributed authority, continuing service, and heterogeneous intervention evidence. These conditions change what practitioners must do. Use Method Engineering and FPF for general questions of Method identity, architecture, qualification, trial, fit, worth, variants, introduction, and culture.

Recover the relations among the Method, performed Work, descriptions, capability, instruments, roles, variants and culture. Describing an organization or a successful work result does not supply a reusable way to change it. The construction follows the receiving dependency backward and tests the proposed actions forward; it keeps a mechanism explanation separate from evidence that the mechanism operated. Project, process and case accounts retain their direct subjects, with common-Work viewpoints as one conditional use. These distinctions make the proposed procedure changeable without promoting its plan, description or first success into capability.

### OCE.15:11 - SoTA-Echoing

The current choice is to use a sufficient available way directly, and to construct only a worthwhile organizational remainder. [Implementation Mapping (Fernández et al., 2019)](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2019.00158/full), especially Tasks 1–5, already links needs and implementation actors to performance/change objectives, selects methods and practical strategies, develops and pretests materials, and plans evaluation. Its theoretical methods have conditions of use; an action label alone is insufficient. [Warhurst et al.'s 2025 review](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2025.1603178/full), Discussion 4–4.3, adds reported context-sensitive prioritization and reassessment, but also substantial resource demands and insufficient evidence for general effects. Its healthcare-heavy evidence does not establish an OCE procedure's effectiveness.

That is a strong alternative for PumpWorks: a competent implementation practitioner with current ME can already obtain the supported handoff or develop an adequate procedure. OCE.15 does not require adding its own construction when that result exists. Where the producer–receiver rule is still missing, sections 4.1.1 and 5.1 make the organizational join explicit: distinguish a scope mismatch from unavailable skill or authority, derive the paired request/return, and alter participation when it defeats service. C.39 and ME.8 supply the general construction and explanation, while ME.14 supplies the worth decision. The full-work comparison in 5.2 accepts extra development for a timely allocation choice and withdraws it when that choice can no longer benefit. This is a bounded domain construction, not evidence that OCE outperforms Implementation Mapping or ME.

Keep source meanings local. Implementation Mapping's performance objectives and change methods, a CFIR determinant, an OCE organizational relation and an FPF-admitted Method are not identical because their terms sound alike. Use a source operation for the result it actually obtains; inspect its conditions before connecting that result to another operation. The following sources retain their narrower roles; the 2015 taxonomy and strategy catalogue are historical anchors, not current superiority claims.

| Source | Retained contribution | Boundary and practitioner implication |
| --- | --- | --- |
| Hagl et al., [change-management intervention review](https://doi.org/10.1016/j.hrmr.2023.101000) | Intervention families and ability, motivation, and opportunity-to-contribute mechanisms support repertoire fields. | The synthesis is not a universal sequence; interactions, boundaries, measurement, and consequences remain open. |
| Ekendahl et al., [context-based adaptation](https://doi.org/10.1080/14697017.2026.2638768) | Decision conditions must be assessed and reassessed while change unfolds. | Use the study’s entity/process perspectives to inspect changing conditions; qualify the local adaptation Method separately. |
| Kamarova et al., [behavior and organizational-change synthesis](https://doi.org/10.1002/job.2832) | Mastery, meaning, belonging, and participation counter recipe and “resistance” reduction. | The synthesis is selective and primarily individual-level. |
| Wang et al., [implementation-framework scoping review](https://doi.org/10.1186/s13012-023-01296-x) and Nilsen, [taxonomy](https://doi.org/10.1186/s13012-015-0242-0) | Determinant, process, strategy, evaluation, and measurement purposes must remain distinct. | Use the taxonomies to distinguish functions, then select or construct the Method needed for the local result. |
| Powell et al., [ERIC strategies](https://doi.org/10.1186/s13012-015-0209-1) | Discrete implementation strategies can be candidate contributions. | Determine the required sequence, local fit, and effects for the selected contributions. |
| Damschroder et al., [updated CFIR](https://doi.org/10.1186/s13012-022-01245-0) and Reardon et al., [CFIR User Guide](https://doi.org/10.1186/s13012-025-01450-7) | A determinant framework requires project-specific boundary and construct operationalization. | CFIR is not designed to develop an innovation or specify the implementation process and is not a universal OCE Method. |
| Proctor et al., [implementation outcomes](https://doi.org/10.1007/s10488-010-0319-7) and [ten-year review](https://doi.org/10.1186/s13012-023-01286-z) | Implementation outcomes need named referents and remain distinct from service, client, and organization results. | Causal relations among strategies, mechanisms, implementation outcomes, and downstream outcomes remain weakly established. |
| Current Method Engineering Principles Framework | General Method results, executable explanation of supplied rules, account-subject distinctions, observation-driven revision and full-effort comparison. | OCE.15 supplies only the missing organizational construction and receiving use; account correspondence and common-Work viewpoints remain conditional. |

Reopen when a source or representative use exposes a materially different domain contribution, framework function, mechanism, situation change, outcome boundary, bundle interaction, or candidate-development need, or when Method Engineering makes an OCE move redundant.

### OCE.15:12 - Relations

- The supplying product is the current `Method Engineering Principles Framework` named in the framework dependency account. `ME.1` supplies Method focus, `ME.2` named-use repertoire structure, `ME.3` situational criteria, `ME.5` individual qualification, `ME.8` development of an executable explanation from supplied knowledge, `ME.9` needed correspondences between unlike accounts, `ME.11` trial, `ME.13` fit/transfer, `ME.14` worth, `ME.15` variants/provenance, and `ME.16` introduction/observation/revision.
- `C.39:4.2–4.6` supplies the general recovery, construction, explanation and selective change of operations; `C.39.RO:4` supplies their development beyond one case. `A.15.6:4.0/4.2–4.4` governs direct account subjects and the conditional viewpoint branch. These contributions remain with their suppliers.
- OCE.15 supplies the organizational difficulty and its evidence, the constructed intervention and reasons for its operations and returns, participants and affected Systems, decision-sensitive conditions, authority/capability/support/protection, mechanism hypotheses, separate outcomes, whole burden and change triggers. A domain candidate remains a candidate until the applicable ME results say otherwise.
- `OCE.1` supplies organization and contribution; `OCE.2` and `OCE.3` can supply current relations and concepts. Any OCE pattern can request a named-use repertoire or domain candidate.
- `OCE.10` can consume a qualified contribution for participation or target-organization working-culture repair and return observations. `OCE.13` supplies later organization and affected-System observations. Qualify any Method-effectiveness claim against the evidence and intended use.
- `OCE.16` consumes a compatible Method/repertoire result for simultaneous Work. `OCE.17` concerns enacted OCE discipline culture and can supply bounded feedback; it is not the owner of the target organization’s culture.

### OCE.15:End

## OCE.16 - Reconcile Simultaneous Organization-Change Work

> **Type:** Method pattern
> **Status:** Stable
>
> **Primary working result:** a **qualified cross-change question and per-change return for one consequential dependency**. The question identifies separately managed changes, the organizational condition one change would alter, the other change's exact action or decision that may use it, the interaction window, the claim status and evidence, the Method needed for that question and its result owner, and any exact missing result. After that direct Method returns, OCE.16 tells each affected change which governed result it can use, what condition it must preserve or revise, and what observation reopens the question.

### OCE.16:0 - Use This When

Use this pattern when two or more separately managed organization changes may alter the same contribution, holder assignment, authority, access path, provider relation, information return, acceptance route, capability-development condition, support interval, or continuing-Work condition, but no current account yet establishes whether they form one decision question.

A recognizable entry is small: one change proposes to alter a named organizational condition and another change plausibly uses that condition for one consequential participant action or decision in an overlapping window. The first useful result can be a qualified cross-change question, a direct exit because the claimed dependency is absent or already answered, or an exact request for a missing owner result.

Do not use OCE.16 merely because initiatives run at the same time, share a dashboard, use different descriptions, or draw from one aggregate resource pool. If the exact question and its consequences for each change are already recoverable, use the direct Method and stop. OCE.16 does not compare joint architectures, select an arrangement, reschedule a portfolio, authorize Work, establish compatibility, or create a superior change authority.

#### OCE.16:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| separately managed change | A proposed or actual organization change with its own subject, intended result, status, scope, owner, evidence, and next decision. Separation does not imply independence. |
| organizational condition | A contribution, assignment, authority, permission, access path, provider or support relation, information return, acceptance route, participation condition, capability condition, or other organization relation or condition that a change may alter. |
| consequential dependency | A claim that alteration of one named condition can change another change's exact action or decision within a stated window. It is not proved by temporal overlap, a diagram, or a participant's interpretation alone. |
| participant account | A bounded report from a participant or affected System about an action, demand, consequence, or condition. Use it to locate a possible dependency, then test the claimed contradiction against current evidence and recover decision authority separately. |
| qualified cross-change question | Ordinary decision-support content naming the changes, altered condition, consumer action or decision, window, participants, evidence and claim status, direct Method, result owner, and any missing input. |
| direct Method | A Method whose result answers the qualified question within its stated applicability. For example, ME.6 compares ways of using Methods together; an appointment requires the applicable assignment Method and actual authority. |
| per-change return | A readable application of already-governed direct results to every affected change. It adds no second choice or authorization. |
| direct exit | A stop in OCE.16 because no consequential consumer exists, the dependency is unsupported, or the direct answer and its per-change consequences are already available. |

Different project, process, case, architecture, Method, organization, and operating descriptions remain different. OCE.16 asks whether one change alters a condition another actually uses; it does not force unlike subjects into one view or one programme.

### OCE.16:1 - Problem Frame

Each change can look locally plausible while the conjunction is not. One effort can promise autonomy while another introduces a new approval; a provider or repository transition can retire an evidence-return contribution that another change still needs; two changes can rely on the same holder in action windows that aggregate availability hides; or an authority change can depend on a credential contribution whose own authorization depends on the incoming authority.

The reverse error also matters. Practitioners can infer a contradiction from different language, a programme map, or one actor's prediction even though the direct relations are compatible. The useful move is therefore not a universal scan or premature joint design. It is a bounded dependency probe around one consequential action.

### OCE.16:2 - Problem

Separately maintained change accounts often stop at their own boundary. The owner of the alteration sees a completed migration, assignment, or design; the owner of the consuming change discovers the missing condition only during enactment. A central coordination layer can make the problem worse by replacing exact subjects, truth statuses, and authorities with traffic-light summaries.

Where existing coordination leaves this connection unexamined, practitioners can miss an interaction and lose an enabling condition. An added coordination pass can instead duplicate the direct comparison and let a coordination note appear to choose architecture, authority, support, or operating commitments that remain owned elsewhere.

### OCE.16:3 - Forces

| Force | Tension |
| --- | --- |
| Cheap discovery | A possible interaction should be noticed early, while exhaustive pairwise initiative comparison creates disproportionate maintenance. |
| Participant knowledge | Participants often see the consequential action first, while their account can be incomplete, interpreted, or strategically framed. |
| Local autonomy | Each change needs bounded ownership, while local closure cannot silently defeat another change's still-current premise. |
| Several structures | Project, process, case, Method, organization, and operating views can each matter, while no fixed trio or master view applies to every question. |
| Direct authority | Coordination needs a usable return, while comparison, choice, authorization, acceptance, and specialist predicates stay with their direct owners. |
| Timing | Total allocation can look feasible, while consequential actions, access, authority, or support windows still collide. |
| Evidence economy | The probe should be proportionate, while a consequential claim needs more than temporal overlap or a shared label. |

### OCE.16:4 - Solution

For one proposed organizational alteration, identify one plausible consumer in another change and qualify their exact dependency before invoking any substantive comparison. Use a Method that supplies the required result under the question's conditions, and return that result to every affected change.

Recognition is cheap: one named alteration and one plausible consumer action are enough to inspect. Assurance is use-specific: recover the changes and subjects, current statuses, altered condition, receiving action or decision, interaction window, participant accounts, direct evidence, governing Method and result owner. OCE.16 cannot assure a result the direct route has not produced.

#### OCE.16:4.1 - Five-Move Pattern-Use Unfolding

1. **Bind the separately managed changes.** Name each actual or proposed change, its subject, intended result, current status, scope, owner, next decision, and relevant window. Do not begin from a programme row or assume that two descriptions name one Work.
2. **Find one consequential dependency.** For one organizational condition a change would alter, ask: which other change uses this condition, for which exact participant action or decision, and during which window? Stop if there is no plausible consequential consumer. Do not inventory or pairwise-scan every initiative.
3. **Qualify the claim with participants and available results.** Recover the participant account and distinguish observed fact, current relation, expected consequence, proposal, interpretation, and decision. Use what is already known to examine the named condition, consumer action, timing, effectivity and alternatives. Seek a further observation or outside result only when its attainable contribution can change the next action, change which conclusion is supported or make the proposed use admissible, and that gain warrants its full burden; use `C.11.DUA` and `A.15.9` for that question. Return a supported or absent dependency, a compatible difference, an unresolved claim, or a missing fact or owner result with its effect on the proposed continuation.
4. **Use the Method for the required result.** Choose the applicable Method and result owner using the question in the table in section 4.2. Give it the smallest sufficient question and evidence. Use the comparison, selection, compatibility judgment, acceptance, or authorization returned by that Method and its actual owners.
5. **Return governed results to every affected change.** For each change, state the direct result it can use, the condition it must preserve, revise, obtain, or stop assuming, the owner and validity window, and the observation that reopens the question. Leave unaffected Work on its current basis. If the direct result is missing, return that exact absence and its consequence rather than filling it by coordination language.

Before adding qualification work in move 3, compare it with the **competent current continuation for the same receiving action and window**. Existing coordination may already have found the dependency, consulted the relevant participants, obtained the owner result and made its conditions usable by both changes. Apply that answer and finish. Do not repeat its evidence recovery or comparison merely to put it through OCE.16. If something remains unanswered, name the particular condition or consequence and why its possible answers would change a current action; do not substitute a general need for better coordination.

Price the complete continuations using C.11.DUA and A.15.9. Retain their common operating work, evidence, decisions, support and communication; work already performed to obtain a still-adequate result is neither repeated nor credited as a new saving. For the proposed addition, include participant time, access and evidence recovery, question formulation, the direct supplier's work, interpretation, each change's usable return, upkeep or recovery, delay and displaced work. Compare that addition with what the current continuation can already achieve, including a supported retention or deferral. Identify the last useful receiving window and confirm that the required people, evidence and decision can be available before it. The responsible owner may accept extra work or a displaced lower-priority activity for a named timely benefit; that is a trade-off, not proof of lower total cost or better coordination in general. An adequate available answer removes duplicate work. A late answer loses the expired benefit; keep any useful evidence and reconsider only a still-live question. Neither outcome waives a missing authority or protection condition.

#### OCE.16:4.2 - Choose the Method for the Required Result

| Qualified question | Direct route and OCE.16 boundary |
| --- | --- |
| Can admitted Methods or candidate Method accounts be co-used under materially different Work order, allocation, subject/support, provider-access, authority, evidence, burden, description, or cultural relations? | Use ME.6. It can return a relation-only arrangement while every Method remains unchanged and no composite Method is proposed. OCE.16 supplies the missed cross-change input and later per-change return only. |
| Which prospective organization synthesis preserves the relevant subjects and several structures with tolerable conflict and moved burden? | Use C.32.MWA for the prospective organization synthesis; return its result to the affected changes. |
| What contribution, crossing, position, assignment, permission, authority, access, provision, or enabling relation should be specified or established? | Use OCE.4, OCE.5, OCE.6, or the direct provider, governance, administration, or specialist result. OCE.16 preserves each truth status and authority. |
| How should product or service architecture and organization architecture be coordinated? | Use OCE.7. OCE.16 only reveals a relied-on condition altered by another change. |
| Which whole human, AI, robotic, provider, platform, or hybrid arrangement should obtain a bounded result? | Use OCE.8 to complete and compare arrangements, preserving the distinction between a probe recommendation and an authorized choice. |
| Which organization-change Method or candidate account is available for a named use? | Use OCE.15 and the applicable Method Engineering results for the repertoire, admission, or refresh question. |
| What does current operating Work require, admit, continue, interrupt, prioritize, or return? | Use the applicable current OPS.1-OPS.7 and A.15 results; obtain any missing operating or capacity decision from its direct owner. |
| What authority, safety, legal, financial, security, labor, clinical, service, or capability predicate is required? | Use the named domain owner. A referral is not the result; OCE.16 returns the exact missing predicate when it is unavailable. |

A direct route can need several suppliers. Name each requested result, its owner, and its authority and evidence conditions, then return those results to the affected changes.

#### OCE.16:4.3 - Record the Result

| Result position | Required content |
| --- | --- |
| changes and subjects | Independently identified changes, affected subjects, statuses, scopes, owners, intended results, next decisions, and windows. |
| alteration and consumer | The exact organizational condition one change would alter and the other change's consequential action or decision that may use it. |
| claim qualification | Participant accounts; observed facts; current relation/effectivity evidence; expected consequences; proposals; interpretations; decisions; uncertainty and missing facts. |
| direct route | Applicable Method, bounded question, required inputs, result owner and authority, and any unavailable result. |
| direct result | The governed comparison, relation, authority, operating, specialist, stop, or missing-result return. Do not relabel it as an OCE.16 decision. |
| per-change return | For every affected change: usable result, preserved or revised condition, next action or stop, validity window, and reopen observation. |
| continuation and exit | Any further work selected for this question, what unaffected Work remains unchanged, and whether the Method exits without further coordination. |

A short note in an existing change account can carry the result. Retain only what the affected changes need to act on the dependency.

#### OCE.16:4.4 - What Changes in Practice

Practitioners stop asking whether whole initiatives “conflict” and stop waiting for a central programme view to decide. They test one alteration against one consequential consumer action, distinguish participant interpretation from current relation evidence, reach the Method that owns the substantive result, and give that result back to every affected change.

### OCE.16:5 - Archetypal Grounding -- PumpWorks Support Retirement

PumpWorks already has an OCE.8 hybrid-trace probe recommendation, not a selected or enacted arrangement. Its trial DecisionSubject and trial authority are missing; provider repository access is decided but not effective; protection, recovery, burden, and specialist-safety results remain unresolved. Safety evidence acceptance and the release decision have separate authorities. Engineer-E27's integration assignment and rig access are also distinct from provider access.

Now suppose a separately managed repository-consolidation change proposes to retire the existing Electrical evidence-return contribution when migration is declared complete. The hybrid-trace change may still need that contribution when Engineer-E27 handles a challenged package after the nominal migration date.

Apply OCE.16:

1. **Bind.** Keep the hybrid-trace arrangement change and repository-consolidation change separate. Record their candidate/proposal statuses, owners, scopes, next decisions, and migration, probe, integration, Safety-acceptance, and release windows.
2. **Find one dependency.** Ask whether retiring the existing evidence-return contribution at migration completion can remove evidence needed for E27's challenged-package integration action before Safety acceptance and release decision.
3. **Qualify.** Treat “challenged packages can occur after migration” as an expected consequence until release history, migration scope, package provenance, current repository relation, participant accounts, and timing evidence support it. Keep decided-but-ineffective provider access, E27 assignment/rig access, Safety acceptance, release authority, protection, and recovery as separate claims. If the evidence shows that challenged packages cannot cross that boundary, return an absent dependency and exit.
4. **Route.** If the candidate accounts' co-use result depends on first-then order, evidence return, access, authority, or support, ME.6 compares retirement at migration completion, bounded retention, qualified replacement, and the incumbent. The authorized decision owner chooses, applying C.11 when a precise choice result is needed. OCE.4 specifies any changed evidence-return contribution; OCE.6 establishes assignment, access, permission, authority, or provision relations; OCE.8 retains the arrangement/probe reroute and protected-condition duties. OCE.16 makes none of those selections.
5. **Return.** Tell repository consolidation whether migration completion can also retire the contribution, what governed retention/replacement condition applies, and what observation reopens it. Tell the hybrid-trace change which evidence-return and access conditions it may rely on, which are still missing, and what stops its probe. Preserve the separate Safety and release decisions.

If ME.6 returns bounded retention until challenged packages and acceptance obligations end, use that relation arrangement under the actual decision owner’s authority. If direct owners instead establish a qualified replacement, return that result. If no lawful provider access, protection, recovery, or authority result exists, return the exact absence to both changes.

A continuing-service question takes the direct service and OPS route. Use OCE.11 for change/service coexistence and obtain the actual coexistence and service results before relying on them. Nominal completion of either change does not prove that the other's premise has survived.

**A sufficient current answer.** Consider a conditional continuation of PumpWorks, not a claim that the initial hybrid probe has become admissible. Suppose ordinary coordination has already obtained an effective owner decision to retain the existing Electrical evidence-return contribution for the two named challenged packages and their acceptance obligations. Its scope, covering assignments, access, service protection and recovery are current. E27's ordinary integration and the separate Safety and release decisions have their own qualified basis; the hybrid trial's missing conditions remain missing. The result already says: repository consolidation may complete migration but must not retire this contribution while either package still consumes it; the consuming change may rely only on the named existing return and must reopen the question if package scope or support conditions change. Apply that result in the two existing change accounts and finish. No new participant interview, ME.6 comparison or coordination artifact is needed.

**A remaining question with a useful window.** Now suppose that, before the second package's integration, a newly supplied package record suggests that its Electrical evidence was fully transferred and no further Electrical return is needed. The old retention decision remains a safe sufficient continuation, but this new record does not itself establish the narrower absence of dependency. A technical owner must qualify evidence scope and configuration, and the support decision owner must apply any resulting change to the actual reservation. A separate, already authorized fault-isolation appointment could use the Electrical specialist assigned to the second package's Thursday coverage and an available instrument slot that day, if the second reservation is released by Tuesday noon. Its qualified result could inform Friday's design review; the accepted current plan instead performs the appointment in the next agreed slot and revisits the provisional design conclusion afterwards. Neither plan violates the supplied safety or continuing-service conditions. This is a priority choice about earlier information, not a claim that migration or the hybrid probe requires the appointment.

| Continuation for the same two-package window | Complete work and consequence |
| --- | --- |
| Apply the adequate current retention result | Preserve both reservations and the qualified Electrical response whenever the packages require it. Use the existing owner updates and per-change communication; perform the fault-isolation appointment in its later agreed slot. This achieves the supported joint continuation without new qualification work and is an acceptable finish. |
| Add a bounded qualification of the second package now | Inherit the same current result and keep both reservations until a governed change is effective. The package originator and E27 reconcile the new record with the requested configuration; Electrical and the technical evidence owner examine the exact remaining return obligation. Include recovering accessible records, formulating the question, obtaining the owner's answer, interpreting its limits, updating both change accounts, communicating the effective reservation and maintaining the stop/recovery condition. If a new co-use choice remains, ME.6 supplies that comparison and its effort is part of this line; if the existing conditional result already decides it, do not repeat ME.6. The support owner then obtains any necessary changed assignment or provision result. |

Both lines retain the underlying package evidence and integration, separate Safety and release work, actual needed Electrical support, access, protection and recovery. The additional inquiry is not paid by silently removing these conditions. For this constructed choice, the relevant records and owners are available before Tuesday noon, and the extra work can be accommodated only by deferring a noncritical documentation improvement. The responsible owner accepts that deferral and the extra participant/supplier work for the possibility of obtaining the fault-isolation result before Friday's review. The evidence question can be settled within that window; its answer remains open. A negative or unresolved answer keeps the second reservation, loses the early appointment and still incurs the work already performed. This choice establishes no net time saving, effectiveness advantage or new capability.

If a current qualified answer already establishes the second package's condition, apply it and its authorized consequences without the added inquiry. If the records or owner can return only after Tuesday noon, the Thursday slot cannot be recovered by that inquiry: retain the adequate continuation, remove the expired Friday payoff from the justification and do not commission this addition for that purpose. Preserve the late record for a later question if useful. If the existing coordinator can already make this same timely qualification and return, use that work directly; OCE.16 describes the missing connection, not another layer above it. Any reduced reservation still requires the actual owner's result, and none of these returns makes the hybrid trial's missing access or authority effective.

#### OCE.16:5.1 - Unlike Transfer -- Distributed Standards Association

A distributed standards association changes its credential issuer while also changing elected committee-holder assignments. The issuer proposal expects authorization from the incoming elected chair; the election proposal assumes voters receive new credentials before the ballot that establishes that chair. Independent member organizations, bylaw authority, current term expiries, and credential and ballot obligations remain distinct.

OCE.16 binds the two proposal accounts and asks one consequential question: does the ballot action lawfully depend on credentials from the new issuer during a window in which that issuer itself lacks authorization? Participant accounts can expose the cycle, but the supplied bylaws, current authority relations, credential evidence, ballot rule, and term windows qualify it.

Use ME.6 if the proposal Methods or candidate accounts require a different order or support/authority arrangement; use OCE.4 and OCE.6 for credential contribution and enabling relations; use the actual Governance result for bylaw authority. A direct result may retain the current issuer, establish a lawfully authorized interim contribution, change order, or stop with a missing interim-authority result. OCE.16 selects none of them and cannot extend an expired term.

Return the governed credential condition to the election change and the governed authorization/order condition to the issuer change. When an already authorized independent secretariat can continue narrowly, its decision owner may retain that contribution through the named credential and ballot obligations and move cutover afterwards. When no such permission exists, return the exact missing authority and affected continuations to both changes. No universal executive, PumpWorks staffing authority, or one-firm portfolio structure transfers to this case.

### OCE.16:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| local-completion bias | One change's milestone is treated as closure of another change's premise. | Test the altered condition against one consequential consumer action and return the direct result to both. |
| simultaneity bias | Overlapping dates are treated as a dependency. | Name the exact altered condition, consumer action, consequence, and interaction window. |
| inconsistency literalism | A participant's inconsistency claim becomes an objective contradiction. | Preserve the account, then test current relations, evidence, interpretation, and authority separately. |
| resistance attribution | A challenged conjunction is dismissed as opposition to change. | Ask what organizational prescription, action, burden, authority, or support condition the participant identifies. |
| aggregate-capacity bias | Total FTE or team count is treated as proof of feasible participation. | Inspect exact role demands, consequential actions, access, timing, informational benefit, and burden. |
| programme-superiority bias | A central view silently chooses for direct owners. | Route each substantive question to its governing Method and return its result without new authority. |
| artifact inflation | A cross-change table or dashboard becomes a control structure or compatibility certificate. | Keep the note as ordinary decision-support content and recover actual subjects and relations. |
| duplicate-decision bias | OCE.16 repeats ME.6 or an OCE comparison after routing. | Attribute the comparison and choice to the direct result; OCE.16 only qualifies entry and returns it. |

### OCE.16:7 - Conformance Checklist

- [ ] Each change, subject, status, owner, scope, result, next decision, and window is independently identified.
- [ ] One named organizational alteration is connected to one consequential action or decision, not merely to coincident dates.
- [ ] Participant accounts, facts, relations, expected consequences, proposals, interpretations, and decisions remain distinct.
- [ ] Recognition is cheap and assurance is specific to the claimed use and result.
- [ ] The selected Method answers the required question under the stated conditions; its result owner is identified before substantive alternatives are compared.
- [ ] ME.6 owns Method/candidate-account co-use, including unchanged-Method relation-only arrangements.
- [ ] OCE.16 makes no architecture selection, compatibility judgment, authorization, acceptance, readiness, priority, or capacity decision.
- [ ] Every affected change receives the governed result or exact missing result; unaffected Work keeps its current basis.
- [ ] A direct exit is used when the dependency is absent or already answered.
- [ ] Any added qualification is compared with the adequate current continuation at full common and incremental burden; its accepted gain is still attainable before the receiving window closes.
- [ ] The result requires no universal inventory, fixed project/process/case schema, dashboard, programme hierarchy, or new persistent artifact.

### OCE.16:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Put every initiative in the reconciliation matrix.” | Begin from one alteration and one plausible consequential consumer; stop when no decision changes. |
| “These two plans use different language, so they conflict.” | Recover the actual subjects, relations, action, condition, and window before asserting dependency. |
| “OCE.16 selects the combined arrangement.” | Route Method/candidate-account synthesis to ME.6 and organization relations to their direct OCE or domain owners. |
| “The programme owner can waive the missing access.” | Obtain the actual permission, authority, provider, security, or other direct result. |
| “The person has capacity across the quarter.” | Inspect the consequential action windows, assignment, access, authority, burden, and support. |
| “Migration is complete, so old support can end.” | Return the direct relation result to every change that still consumes the condition. |
| “The dashboard is green, therefore the changes are compatible.” | Treat the display as a carrier; recover the evidence, decision, and actual relations it describes. |
| “Create a new coordination body for every interaction.” | Use the existing owners and Methods; establish a new organization relation only through its direct design and authority results. |

### OCE.16:9 - Consequences

A practitioner can discover an interaction before one change removes another's premise, challenge an alleged inconsistency without dismissing the participant, reach the correct direct Method, and preserve the result across local change boundaries. Several authorities and unlike structures remain visible.

The qualification has a real cost: participant and supplier attention, evidence recovery, interpretation, usable returns and later upkeep can exceed the work of applying an adequate current answer. Keep shared operating and support work in both continuations. The PumpWorks addition accepts this extra work and a deferred improvement for a possible earlier diagnostic result; it does not establish a general saving. When that receiving opportunity expires, its justification expires too. The Method can also end with an unsupported dependency, a missing fact or an unavailable owner result, preserving the competent current continuation where its conditions still hold.

### OCE.16:10 - Rationale

The difficulty addressed here is finding a consequential dependency and returning its resolution across separately managed changes. ME.6 already compares Method and candidate-account co-use through order, allocation, support, access, authority, evidence, burden, and other decision-changing structures, including relation-only arrangements with unchanged Methods. OCE.4-OCE.8 and direct domain Methods already own contribution, assignment, enabling, architecture, and arrangement results.

Competent coordination can already supply the same recognition, owner result and usable return. When it does, another OCE.16 pass adds no practical gain. The retained contribution is the explicit connection from one proposed alteration to a consequential consumer action, and from the governed answer back to each separately managed change where that connection is still missing. In PumpWorks, the current retention answer finishes the original question; the changed package record opens only the narrower return obligation. A justified timely inquiry may change that reservation, but it does not replace the shared package work, the direct owner's decision or ME.6's comparison. This bounds the extra work by its receiving consequence instead of treating a smaller-than-universal inventory as sufficient evidence of worth.

### OCE.16:11 - SoTA-Echoing

For the question **what further work is worth doing before one change alters a condition another uses**, the selected line is direct use of adequate current coordination and owner results, with OCE.16's bounded entry and return only for the unresolved connection. The serious alternative is competent existing coordination, including dependency-aware portfolio practice in its applicable setting. Its sufficient answer wins in the first PumpWorks continuation. In the changed continuation, the still-unqualified second-package obligation could affect a usable Thursday appointment; the additional work is selected only under the stated availability and deliberately accepted deferral, while retention remains feasible. Use this comparison in move 3 before commissioning the extra work. It neither ranks whole frameworks nor claims that a narrowly framed probe is inherently cheaper.

| Source | Retained contribution | Boundary and practitioner implication |
| --- | --- | --- |
| Kanitz, Huy, Backmann and Hoegl, [No change is an island](https://doi.org/10.5465/amj.2019.0413) | Interacting changes can generate cognitive, normative, and procedural inconsistency judgments beyond a simple resource collision. | Inspect joint demands and organizational prescriptions. The primary abstract supports recognition of possible inconsistency; qualify local causal and effectiveness claims with further evidence. |
| Skov and Lê, [Resisting by not resisting](https://doi.org/10.1177/00187267241248529) | Actors can construct relationships and inconsistency claims between mandated changes. | Test the claimed dependency and underlying condition; neither dismiss it as resistance nor accept it automatically. Use the abstract for this recognition question; a motive diagnosis requires its own qualified evidence. |
| Rishani, Schouten and Hoever, [Navigating multiple team membership](https://doi.org/10.1111/spc3.12899) | Membership, time allocation, and variety are different, with heterogeneous relations to effectiveness. | Inspect actual role demands, action windows, informational benefit, and burden. No universal team-count or utilization threshold transfers. |
| Zhang, Li, Zhang, Deng and Yang, [Time the Surge](https://journals.aom.org/doi/abs/10.5465/amj.2024.0522?af=R) | Non-coinciding project portfolios and shared external overlap make timing of team activity consequential. | Probe whose actions coincide rather than using total allocation alone. Use the primary abstract to recognize a timing question, then obtain a schedule qualified for the actual work. |
| Martinsuo and Ahola, [Multi-project management in inter-organizational contexts](https://doi.org/10.1016/j.ijproman.2022.09.003) | Inter-organizational multi-project settings alter strategy, resource, governance, and learning questions. | Challenge one-firm authority assumptions. Use the conceptual primary abstract to recognize interorganizational questions; obtain the applicable authority and Method from their owners. |
| Fischer, Marcus and Röglinger, [A portfolio management Method for process-mining-enabled improvement projects](https://doi.org/10.1007/s12599-024-00906-2), §§4.1–4.2.5 | Adopt as a serious current comparator: dependency-aware selection is connected to implementation, resource consequences and feedback to responsible owners. | Use its sufficient applicable result directly, not only for a selection label. Its process-mining project setting bounds transfer; the added OCE question must still earn its full price. The source does not establish OCE superiority or association authority. |
| Current ME, OCE, OPS, A.15, C.32.MWA, and C.11 results | Supply the substantive Method-co-use, organization, operating, Work, synthesis, and decision results. | Use OCE.16 for discovery, qualification, access to the direct Method, and per-change return; obtain any missing substantive result from its owner. |

Reopen the addition when an adequate answer becomes available, its full burden changes, or its useful window is missed. Reopen the retained pattern when a direct supplier or existing entry supplies the same recognition, qualification, and per-change return at comparable effort; representative use finds no missed interaction that changes action; a new source defeats the consequential-action probe or participant/evidence boundary; or changed ME, OCE, OPS, or domain results make the route or promised use false.

### OCE.16:12 - Relations

- [ME.6 in the current Method Engineering Principles Framework](METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md) owns Method and candidate-account co-use comparison, including relation-only arrangements with unchanged Methods. OCE.16 supplies a qualified cross-change input and per-change return.
- [C.32.MWA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c32mwa---synthesize-an-architecture-account-of-methods-and-their-use) owns prospective practice-architecture synthesis after relevant structures and subjects are selected.
- [OCE.4](#oce4---design-an-organizations-contribution-architecture), OCE.5, and [OCE.6](#oce6---establish-holder-assignments-and-enabling-relations-for-organization-change) own contribution-design, position, assignment, and enabling-relation results. [OCE.7](#oce7---coordinate-product-or-service-and-organization-architecture-decisions) owns paired product/service and organization architecture decisions.
- [OCE.8](#oce8---compare-human-ai-robotic-and-provider-arrangements-for-the-same-organizational-work-result) owns whole same-result arrangement comparison and its choice, probe, rejection, or reroute result.
- OCE.15 supplies a compatible named-use Method/repertoire result. OCE.16 does not repair or admit it.
- [The current Operations Management Principles Framework](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md) supplies currently available operating results. A.15 supplies general Work distinctions and decisions. C.11 and direct domain governors own choices.
- Use OCE.11 for its change/service-coexistence Method; OCE.16 does not supply that Method's actual result. Use OCE.13 to compare wider organization-change consequences, OCE.14 to revise an organization relation within its authority and effectivity limits, and OCE.17 to examine continuation of OCE practice. These are optional returns for their own questions, not substitutes for the direct owner of the current cross-change result. A missing service, Strategy, Governance, Administration, HCD, safety, legal, finance, security, procurement, or provider result stays missing until its direct owner returns it.

### OCE.16:End

## OCE.17 - Continue and Renew Organization-Change Engineering Practice

> **Type:** Method pattern
> **Status:** Stable
>
> **Primary working result:** a bounded account of which OCE practice continues, how its continuation is supported or impeded, and the justified retention, intervention or return, with observed later use or an exact observation gap.

### OCE.17:1 - Problem frame

**Use this when** an organization-change practice seems to be spreading, fading or changing among practitioners, and that difference matters to their next work. A case group still teaches “organization mapping”, yet its members now submit charts without recovering who supplies an input, who uses it and who can decide. Elsewhere the old name disappears, but practitioners still make those distinctions in real cases. The useful question is what continues in the work, not which label survives.

Start with one consequential OCE move in one organization-change episode. Compare the practice claimed with the action and usable result actually recoverable there. Then examine the connections through which another practitioner could encounter, attempt, criticize and continue it.

Continuing organization development is the wider concern. This Method covers the cultural continuation of **Organization Change Engineering practice across practitioners and work settings**. Its subject is the practice and the relations through which it is transmitted, recognized, selected, enacted, retained or lost. A practitioner population is not automatically one organization, System or capability holder. A Method is a reusable way of obtaining a result. Its description, a carrier such as a file or course handout, and an occasion of using the Method are different things; teaching can use the description and carrier as support.

The first useful result may be “the operative practice continues under another name”, “the recognition rule rewards the wrong result”, or “there was no suitable opportunity to observe use”. A supported intervention can follow; a workshop or profession-wide survey is not an entry requirement.

**Use another pattern when** the question is the working culture of the organization being changed: OCE.10 supplies that branch. Use OCE.15 when the reusable OCE Method or repertoire itself needs repair. A person's learning target without a cultural-continuation question belongs with HCD or the qualified learning provider. An adequate current continuation account and the qualified help already supplying the needed practice can simply be used; no additional diagnostic, clinic or culture intervention is required.

### OCE.17:2 - Problem

Practice can disappear while its carrier thrives. People attend events, repeat a vocabulary and fill the expected forms, but no longer obtain the result that made the practice useful. Conversely, a changed tool, title or teacher can hide a practice that remains effective for its bounded use.

A generic response -- more communication, more training or tighter compliance -- misses different causes. A newcomer may misunderstand the move, lack permitted case access, be rewarded for another result, have insufficient support, or correctly reject a Method whose conditions no longer fit. Treating all these cases as loss of skill burdens people and can spread the wrong practice.

The practitioner needs to discover the operative variant and the relation that can be changed, preserve competing explanations, and observe what happens in later work.

### OCE.17:3 - Forces

| Force | Tension |
| --- | --- |
| Recognizable practice | Shared names help people find one another, while changed names and tools can conceal continuity or difference. |
| Evidence at working scale | One real case can reveal a useful gap, while one case cannot represent a whole profession. |
| Transmission and opportunity | Good explanation matters, while access, permission, time and suitable work determine whether it can be attempted. |
| Recognition and participation | Peer judgement can sustain useful distinctions, while prestige, compulsory participation and rewards for appearances can suppress them. |
| Continuity and renewal | Retaining a useful variant saves effort, while preserving a harmful or obsolete one defeats the purpose. |

### OCE.17:4 - Solution

Recover a concrete OCE move, trace its continuation conditions, distinguish the difficulty, and change only the relation the evidence supports. Observe a later suitable use before making a continuation claim.

Recognition is light: an apparent difference between claimed practice and one real OCE episode is enough to begin. Assurance is proportional to the result being used. A claim about one later use needs its case evidence; a claim about a population, lasting retention, learning or intervention effectiveness needs additional evidence suited to that claim. These are not interchangeable levels of confidence in one fact.

#### OCE.17:4.1 - Recover the operative variant from real work

Choose an episode in which an OCE move should matter. Examples include bounding the changed organization, recovering an actual contribution crossing, comparing organization concepts, distinguishing appointment from authority, protecting continuing service or revising a relation after adverse consequences. Name the receiving result: what should another person have been able to do with the work?

Inspect the permitted work products and, where needed, a work observation or the practitioner's explanation. Ask what difficulty was recognized, which distinctions changed an action, what was done, what result followed and what the recipient could use. For an OCE.2 case, “we drew the process” is not yet the answer. Recover a particular input, its supplier and user, the occasion of its use, and the evidence or decision relation that mattered.

Compare that occurrence with the relevant OCE Method and any declared local adaptation. Keep three possibilities open: the same operative move in different words; a genuinely different variant; and a familiar name with no evidence of the required move. A missing account can also be an observation gap rather than an absent practice. Ask for the smallest permitted evidence that distinguishes them.

Do not make conformity to one notation the criterion. If a short conversation and work trace make the relation recoverable, a missing chart does not defeat the result. If a polished chart cannot support the receiving decision, its presence does not supply it.

#### OCE.17:4.2 - Trace how another practitioner could continue it

Follow the connections relevant to this move. Who shows a real case? Which source and counterexample does the practitioner encounter? Who can question the result? What opportunity allows an attempt? What support, permission and evidence access are needed? Which result receives recognition? What remains available when a mentor leaves or the next case differs?

Distinguish exposure, understanding, an authorized opportunity, an attempted use, repeated use and later retention. These can have different evidence and different owners. A case bank can remain accessible while no one has time to use it; an excellent teacher can leave behind no recoverable explanation; a practitioner can understand a move but lack permission to inspect the receiving organization's work.

Inspect a supported instance alongside the doubtful one when that contrast could change the explanation. Include a peripheral, dissenting or departed participant when excluding that experience could reverse the account. This is a bounded inquiry, not a requirement to map every member or association.

Keep observed cultural selection separate from the group's decision about an intervention. Practitioners may copy a prestigious example despite the facilitator's choice, or retain a useful variant without a central decision. Neither copying nor a management decision proves that the practice is better.

#### OCE.17:4.3 - Distinguish the difficulty before choosing a remedy

Ask which explanation changes the next work. Use the evidence already available; request another contrast only when its possible answers can change the intervention or the scope of the conclusion.

| What the case suggests | Discriminating next move |
| --- | --- |
| The example omits the operative OCE distinction. | Compare it with the actual Method and a usable case. Repair the description or example if the Method already supplies the answer. |
| A practitioner encounters the right account but interprets it differently. | Have them explain and attempt the relevant move on a permitted case; identify the exact misunderstanding before selecting qualified learning support. |
| No suitable case, access, permission or work interval exists. | Return the specific opportunity or enabling gap to its owner. Do not infer a learning failure from non-use. |
| Recognition rewards a completed chart or fluent vocabulary. | Compare the rewarded product with the contribution, alternatives, authority or consequence result its recipient actually needs. Inspect what participants reasonably optimize. |
| Workload, support or protection makes the practice impracticable. | Obtain the relevant workload, service or protection result. More practice is not a substitute for it. |
| A previously qualified practitioner seems unable to perform the move. | Use an applicable HCD.3 differential when it can change the next action; preserve access, conditions, adaptation and enactment as alternatives to capability loss. |
| The Method no longer fits the problem or causes unacceptable consequences. | Return the problem, failed move, conditions and evidence to OCE.15 and the applicable Method Engineering work. Do not propagate a replacement before its qualification. |
| Later use cannot be observed. | State what remains unknown and the smallest permitted observation needed. Neither continuation nor loss has been established for that use. |

These are competing explanations, not diagnostic labels to assign to people. Several may coexist. A report of difficulty is evidence of that report; its proposed explanation may still need support. Stronger causal reliance uses the appropriate C.28 and professional result.

HCD.3's observation-first use of Candidate E.23.CAE can help separate an apparent loss from changed conditions or access when its stated conditions hold. Its result is a qualified human target, non-training return or unresolved differential, not a cultural verdict. Candidate E.23.CDI contributes to separately qualified development and transfer uses. Obtain any missing intervention, assessment or learning result from the appropriately qualified provider.

#### OCE.17:4.4 - Change the practice relation that matters

Begin with the receiving OCE result, the practitioners and cases that need it, its usable window, and the actual authority and access. Recover the strongest available continuation. Qualified current help may already compare cases, explain the consequential move, correct an example or peer-recognition question, adapt support and inspect later work. Do not remove those operations from the alternative merely because they resemble the proposed response. If an adequate answer and the needed continued provision already exist, use them and finish this question.

Name only the contribution still unavailable under those conditions. For example, a competent provider may supply the needed case result while no qualified help is obtainable during a short observation window. That is an availability question, not evidence that the provider's Method is defective or that every participant must learn it. Keeping the current arrangement, obtaining another contribution and developing a participant can remain different responses. C.36.RP:4.2–4.5 explains how to locate and obtain the missing contribution; use the relevant OCE or qualified human-development Method for its actual performance.

Compare complete continuations, not a diagnostic sample with an entire course. Keep the ordinary OCE case work, service protection and qualified support in both lines. Follow what each additionally asks of the case owner, practitioner, helper and later recipient: obtaining and protecting material; preparing and explaining the relevant case; designing and performing critique or a recognition change; arranging the later opportunity; interpreting its result; and keeping the necessary help and explanation available. Credit an existing usable result without charging its reconstruction again. Include displaced work, the timing of the burdens and who can accept them. Two inspected cases do not price the response that follows.

Choose an addition only for a useful difference it can attain in that window, or for an explicit trade-off those bearing the burden accept. A possible earlier clarification can justify more preparation without making the whole response cheaper or establishing that it will work. If current provision already gives that clarification, cancel duplicate work. If permission, support or the opportunity disappears or arrives too late, remove the dependent payoff and retain the adequate continuation, supported observations and useful partial material. Reopen only a later use that gives the remaining work a reason.

Generate a few materially different responses to the supported difficulty. The following moves construct a response when the comparison warrants it; they are not an additional programme to impose on adequate current work.

For a transmission gap, let practitioners compare an actual organization-change result with the deficient example. Make the missing distinction visible in critique, preserve the exact source and a counterexample, and arrange a later opportunity to use it. For example, compare a filled organization chart with a recoverable evidence-supply and receiving-decision relation; ask what each lets the receiving practitioner decide.

For misdirected recognition, change what the group asks contributors to show. A case can be recognized for tracing an actual contribution, exposing an authority limit, comparing serious alternatives or preserving conflicting consequences. Let practitioners challenge the judgement and show why a different form still supplies the result. A facilitator's permission to change peer feedback is not authority to change an employer's appraisal, credential or pay rule.

For a single-mentor dependency, compare continuing qualified provision with making another contribution obtainable. Obtain the selected practitioner and a recoverable explanation of the case, including why plausible alternatives failed. A name on a support roster is insufficient: the person must be willing, capable and available for the required contribution. A handover can connect an already qualified person to unfamiliar case material; it is not by itself evidence that a new capability was learned.

For an obsolete or defective Method, retain the problem evidence and return it to OCE.15. If the direct Method already contains the needed branch, repair its transmission rather than inventing a new variant. If it does not, a cultural intervention cannot supply the missing reusable answer.

Select a response only within the actual authority and participation conditions. Qualified learning, facilitation, human assessment, employment, service and protection results remain with their direct providers. A bounded case discussion can be useful without claiming to be a complete development intervention.

#### OCE.17:4.5 - Perform the intervention and look beyond the event

Obtain the commitments, lawful evidence use, work opportunity, support and qualified contributions that the selected response requires. Separate what was agreed from what was done. Record the actual case discussion, changed example, recognition decision or support contribution at the detail needed for later interpretation.

At a later suitable opportunity, inspect whether the practitioner used the relevant OCE distinctions and produced a result another participant could use. Choose a case without the original initiator, or with a changed condition, when that contrast matters to the intended continuation claim. Do not require every case to be unassisted: assistance may be a legitimate part of the practice, but its contribution must remain visible.

An event attendance record supports attendance. A later case can support a bounded enactment claim. Learning, transfer, lasting retention and the causal contribution of the intervention each need their own qualified evidence. If there was no permitted opportunity, the next result is an opportunity gap, not evidence that teaching failed.

Check the cost of the response as well as its apparent success. Did additional case work displace service, expose protected information, discourage dissent or shift the burden to an unsupported practitioner? Stop or narrow the dependent intervention when those conditions fail.

#### OCE.17:4.6 - Return the supported continuation and its limits

State which operative variant, practitioners, cases and period the account covers; what was observed; what remains inferred or missing; what changed in transmission, recognition or support; and what decision or next observation follows. Ordinary work can use a short note with the relevant case references.

Return a specific reusable-Method problem to OCE.15: the failed or adapted move, receiving OCE result, conditions, evidence and surviving alternatives. Return an organization's participation or authority question to that organization's actual owner and the applicable OCE pattern. Keep a human capability question with the qualified HCD or professional result.

Retain a useful variant without requiring a new intervention. Revise the account when a later case defeats its scope, a source changes the relied-on move, support disappears, a new burden is found or the practice is no longer needed. Keep the conclusion within its supported practitioner, case, and time scope; any wider standard requires a separate basis.

The group can now retain a usable variant, repair a demonstrated continuation gap, or return a missing condition without treating these as the same result.

### OCE.17:5 - Archetypal Grounding

#### OCE.17:5.1 - Eight practitioners and a disappearing label

This constructed case illustrates the Method; the observations are fictional, not evidence about a real community. Eight OCE practitioners from three organizations share a case collection. The collection's “organization mapping” label is disappearing. The set of practitioners is not asserted to be one System.

The supplied material includes permitted case extracts, the group's current example and recognition questions, and explanations from the practitioners. The current OCE.2 Method supplies the reusable move being examined. The case group's permission covers peer discussion of the permitted material, not employment decisions.

| Supplied case evidence | First result of the comparison |
| --- | --- |
| Four practitioners' cases, under a different title, recover actual input supply, its receiving use and the relevant decision authority. | The operative OCE.2 move is observed in those cases despite the label change. |
| Two newer cases contain filled charts but do not recover the consequential evidence crossing. Their explanations do not yet supply the missing relation. | There is a bounded practice gap to investigate; neither population-wide loss nor an individual incapability is established. |
| Two practitioners had no suitable permitted case during the period. | Use is unobserved for them. Their absence from the case set is not a failed attempt. |

The facilitator compares the chart-only cases with a usable one. In the usable case, an engineering decision-maker uses a particular maintenance observation from a field-service report; the account shows who supplies the information, who may release it, and who uses it. The chart-only example shows departments but cannot answer those questions. The group's existing recognition rule asks whether every department box is present. That is evidence of a competing recognition demand, not yet proof of its exclusive causal role.

**The competent current continuation is sufficient here.** The receiving result is a disposition for these eight practitioners' cases and support for the permitted later opportunities, not restoration of an old label. The group's existing qualified case help can compare the extracts, lead the critique, replace the deficient example and peer-feedback question, and discuss a later case. Its current participation arrangement permits those actions. Calling that same work an OCE intervention would not add a contribution.

The group therefore uses that provision. It retains the four usable variants, replaces the deficient example with a source-linked case and counterexample, and asks in later feedback for the usable contribution and decision relation. The practitioners agree a permitted later opportunity where one exists. No employer is assumed to supply time or access merely because the group chose the response.

This is not a cost-free alternative. Case owners prepare and authorize extracts; practitioners explain their work and perform the later OCE work; the helper prepares and leads the critique; the group changes its example and feedback practice; and participants interpret the follow-up and keep the changed material usable. Ordinary service and evidence protection remain in place. Those contributions already fit the agreed case-help provision and participants' available time in this constructed case. A second diagnostic or clinic would repeat them without changing the receiving result, so it is not selected. If later support were actually missing, that new question would require the comparison in section 4.4.

In the fictional follow-up, one of the two practitioners independently recovers the crossing and receiving authority in a different organization case. The other cannot access the required evidence in the later window. The result is therefore mixed: a later operative use is observed for one practitioner, and an access gap remains for the other. It is not “two people trained, one passed”; no controlled learning-effect claim was sought or supplied.

The continuation account names those cases and limits. The access question returns to its organization owner. If the critique had instead found that OCE.2 itself lacked a needed move, the facilitator would return that specific problem to OCE.15; changing peer recognition would not repair the Method.

#### OCE.17:5.2 - A useful absence and a voluntary boundary

An association sees fewer position-design diagrams and fears that its members have abandoned organization design. A permitted case shows why: the current OCE.5 question concluded that a short-lived editorial contribution needed direct assignments, not a continuing institutional position. The absence of a position diagram is appropriate use, not cultural loss. The group keeps the example and asks whether its recognition questions wrongly require the diagram.

Members work for independent employers. The association can offer a case clinic under its participation rules, but cannot promise employer evidence, assign protected work or extend an expired chair's authority. If access is denied, only the access-dependent use remains unobserved. This boundary changes what the group may do; it is not solved by calling the members a community.

#### OCE.17:5.3 - The mentor leaves, but qualified provision remains

This separate constructed case changes the support conditions. Two practitioners need usable OCE.2 accounts for two design reviews in the next month. Their usual case mentor leaves before those cases. A competent replacement provider has already agreed to brief the practitioners and review both accounts before their decisions. The provider can explain the move, challenge an account, adapt the example and help with feedback; mentor departure does not make that service inadequate. Both alternatives below must supply the same two bounded case results within the month and report how the practice was supported.

In the first case, the person who can explain a disputed maintenance record is available only during a permitted site visit. The provider can prepare questions beforehand and interpret permitted extracts afterwards, but cannot join that visit. The design review can still use a qualified account with the disputed crossing left unresolved and retain its conservative organization option. A later access window would be needed before relying on the less restrictive option. The supplied earlier case work shows that the two practitioners can follow the briefing and record answers but still need help interpreting conflicting trace histories. A local peer is already qualified in that OCE.2 work, willing and available during the visit, and has permission for these two cases; the peer has not yet recovered their particular evidence history.

**Continue the available service.** The provider's preparation, questions, explanations, two reviews, follow-up and correction remain real work. Case owners authorize and prepare the material; practitioners obtain it lawfully, construct the accounts and use the qualified results. Service protection, decision authority and the return of an unresolved crossing remain with their existing owners. This line supplies an adequate result and is the choice if earlier resolution of the disputed crossing is not worth an addition.

**Add a bounded local handover while retaining that service.** Reuse the provider's existing briefing. Before leaving, the mentor supplies only the still-missing case history: why the old chart failed and how the source-linked case and counterexample recover the supplier, permitted release and receiving decision. The peer reconstructs those relations on the permitted material; the mentor critiques that reconstruction and leaves the unresolved evidence question explicit. During the site visit the peer can then recognize an unexpected answer and ask the record's owner for the needed distinction. The provider's agreed reviews and fallback stay available; this proposal claims no saving from cancelling them. If the handover exposes an unavailable skill or permission, return that question to its qualified owner rather than call the peer ready.

The addition requires the mentor's explanation and critique, the peer's preparation, participation in the visit and later case support, the owners' preparation and protection of the handover material, and the participants' comparison of the later results. The peer agrees to keep the explanation current through these two cases, using corrections from the retained provider reviews; that upkeep also takes time. Those burdens are additional to the common case work and retained service. The willing contributors and their actual work owners accept postponing a non-urgent case-bank revision to make this possible; the group cannot allocate their employer's time. The reason is the possibility of resolving the crossing while its knowledgeable source is available, allowing the first design review to consider the less restrictive option. It is a priority trade-off for a timely option, not evidence of lower total effort, intervention efficacy or a new capability.

In a conditional follow-up, the provider's prepared question already asks which release the maintenance record describes. At the visit, its owner says the record was carried forward after an equipment change. The peer uses the recovered history to ask which assertions were checked again for the new equipment. The owner supplies a permitted trace for that distinction, and the provider's review confirms which claims the receiving comparison can use. Retain that local result. It does not prove that the handover caused it, that unassisted performance was learned, or that the second case will succeed; inspect the second case under its own conditions and retain the promised support meanwhile.

**Change the condition.** If the practitioners' existing briefing already settles the crossing, use that answer. If the provider can supply the needed critique during the visit, use that provision. Either sufficient result cancels the duplicate handover. If permission or the handover arrives only after the visit, it cannot earn the earlier clarification payoff. Continue the adequate service and the conservative option, retaining the unresolved crossing and any useful preparation without calling the sunk effort a benefit. A later handover needs a still-live receiving use; the mentor's departure alone is not one.

### OCE.17:6 - Bias-Annotation

Prestige can make a copied example appear valid; inspect the actual receiving result and a serious countercase. Survivor bias can hide departed or excluded practitioners; include their experience when it could change the account. A facilitator can prefer visible events over slow, less visible work opportunities; distinguish the event from later use and its costs.

The goal is useful continuation, not maximum conformity. Preserve dissent that reveals a poor Method, unsuitable conditions or a less burdensome valid variant.

### OCE.17:7 - Conformance Checklist

- [ ] A named operative OCE move is recovered from a real or explicitly constructed work episode and compared with its Method or declared variant.
- [ ] The practitioner and case scope is explicit; a population is not silently made one capability holder.
- [ ] Transmission, recognition, opportunity, enactment and retention are distinguished where they can change the explanation.
- [ ] Competing source, interpretation, access, support, recognition, capability and Method-fit explanations receive the evidence their use needs.
- [ ] Sufficient competent continuation is used directly; an addition has a distinct receiving benefit and a comparison of both complete continuations, including the accepted burden and the condition that cancels it.
- [ ] The selected retention or intervention is within actual authority, participation, professional and protection conditions.
- [ ] Performed work and later observations are distinguished from proposals, attendance and missing opportunities.
- [ ] Learning, transfer, causal effect and population-wide continuation are claimed only with their separately qualified evidence.
- [ ] The result names its usable scope, exact gaps, direct returns and an observation or source change that would reopen it.

### OCE.17:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Better move |
| --- | --- |
| “Nobody uses the old term, so the practice is lost.” | Recover the action and receiving result across changed words and tools. |
| “Run the same course for every non-user.” | Distinguish misunderstanding, opportunity, support, recognition and Method fit before selecting learning work. |
| “The workshop restored our culture.” | Inspect later suitable cases and state exactly what their evidence supports. |
| “Everyone must use our form.” | Judge the operative OCE result; preserve a different form that makes the necessary relation recoverable. |
| “The group selected it, so it will be retained.” | Observe copying and continued use separately from the intervention decision. |
| “The practice should survive indefinitely.” | Reconsider its usefulness and conditions; return a defective or obsolete move to Method Engineering through OCE.15. |

### OCE.17:9 - Consequences

Practitioners can retain useful OCE work across changes in vocabulary, tools, teachers and settings, and can repair a specific transmission or recognition difficulty without imposing a generic programme. The account also makes legitimate non-use and missing observation visible.

Competent current help can supply this result without an extra intervention. Where an addition is warranted, its cost includes preparation, protected access, qualified explanation or critique, later work and interpretation, continued support and what contributors must defer. The added work can buy a timely opportunity while being more burdensome overall. Some conclusions remain narrow because later work, permission or evidence is absent. Losing the useful window removes the dependent reason for the addition; it does not erase an adequate case result or make the remaining uncertainty a failed learning outcome.

### OCE.17:10 - Rationale

An OCE practice matters because its distinctions change organization-change action and the result a recipient can use. Its cultural continuation depends on more than a preserved description: practitioners must encounter the move, have conditions for using it, receive meaningful criticism and recognition, and be able to continue in later work.

This makes diagnosis by case comparison practical. A preserved result under a new name, a chart rewarded for the wrong feature and an absent work opportunity lead to different actions. Keeping those differences visible permits both continuity and renewal without treating every change as loss.

### OCE.17:11 - SoTA-Echoing

The practice question is how to keep a needed OCE result obtainable when its apparent continuation changes. The serious current alternative is competent, case-sensitive implementation support that can inquire, adapt explanation and participation, obtain qualified help and reassess later use. The selected line retains that strength: use sufficient current provision directly, then compare only a missing OCE contribution under the actual case, access and timing conditions. It does not claim that adding an OCE label improves an otherwise identical operation.

**Recover the practice being continued.** Identify operative Methods across descriptions, instruments and practitioners, and examine repeated Work in unlike settings. Sections 4.1–4.2 and the cases show how exposure, support, use and continuation can differ.

**Adapt current implementation inquiry without weakening it in the comparison.** The [NPT coding manual (May et al., 2022)](https://doi.org/10.1186/s13012-022-01191-x) supports interpreting the implementation difficulty. The [NPT-derived strategy synthesis (May et al., 2025)](https://doi.org/10.1186/s13012-025-01444-5), particularly Results and “Using NPT-derived implementation strategies”, supports adaptation, participant feedback, resources and planned responsibilities. Its interpretive synthesis of 63 health/social-care studies does not establish OCE effectiveness. Sections 4.3–4.5 use these contributions for both alternatives, not just the preferred one.

**Retain the contextual challenge.** The [NPT consolidation, version 1 (May, Finch and Rapley, 2026)](https://doi.org/10.3310/nihropenres.14315.1) strengthens attention to changing conditions and distributed burdens in sections 4.2 and 4.5. It does not establish cultural-evolution or individual-learning mechanisms.

The OCE-specific construction connects the actual domain move and its receiving result to that inquiry and to C.36.RP's obtainability choice. Section 5.1 selects the sufficient existing help, with no additional clinic. Section 5.3 preserves an adequate provider continuation and prices the extra local handover, retained provider support and displaced revision against a possible earlier clarification. That limited timing benefit, not a general superiority over competent implementation practice, can justify the accepted extra work. Sections 4.4 and 9 carry the same whole-effort and lost-window conditions. **Reject** efficacy or capability claims from the conditional examples. A sufficient ready contribution, changed opportunity, better applicable rival or changed source premise reopens only the choice that relies on it.

### OCE.17:12 - Relations

[C.36](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c36---cultural-evolution-and-cultural-evolution-engineering) supplies cultural-case, transmission, recognition, selection and memory distinctions, including the difference between an intervention and observed cultural change. [C.36.RP](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c36rp---sustain-and-renew-shared-ways-of-working):4.2–4.5 supplies locating the missing contribution, choosing provision or acquisition and making it obtainable; OCE.17 retains the domain case and cultural-continuation question. A.10 supports evidence provenance; C.28 governs stronger causal reliance.

OCE.2, OCE.3, OCE.5 and other OCE Methods supply the actual domain moves recognized in cases. [OCE.15](#oce15---choose-develop-or-refresh-organization-change-methods) receives a reusable-Method or repertoire problem and uses current Method Engineering for qualification, fit, trial and variants.

OCE.10 governs participation and working culture in the organization being changed. OCE.12 can supply a concrete qualified explanation, critique or support contribution. OCE.13 can provide a consequence comparison relevant to a practice question; OCE.14 supplies an authorized organization-relation revision, not authority over a practitioner population.

Current HCD.1/HCD.3/HCD.4 supply their bounded human-demand, diagnostic and profile results. Learning design, practice, assessment, transfer and retention outside those results remain requests to qualified providers. The framework's dependency and sibling-return account states the current CAE/CDI contribution limits; the population does not become one development holder by association.

### OCE.17:End

# Cross-Pattern Application

<a id="app-oce-01---pumpworks-weekly-ai-inspection-releases"></a>

## OCE.Application:1 - APP-OCE-01 - PumpWorks weekly AI-inspection releases

This constructed case concerns the existing PumpWorks engineering organization. PumpWorks intends weekly evidenced AI-inspection releases while field service and support continue; the case is illustrative, not empirical evidence about a company.

`OCE.1` selects `PumpWorks-EngineeringOrg` rather than the whole company, an imagined AI team, or a provider-inclusive whole. It states contribution, Work/capability questions, affected Systems, authority boundary, and reopen evidence.

`OCE.2:5` reconstructs two permitted release episodes from the procedure, package revisions, review and booking records, effective delegation and participant accounts. It distinguishes Software's assembly from Electrical's evidence supply and receiving use, separates safety acceptance from release, and finds that planned rig access conflicts with service diagnostics. Late request and service displacement remain alternative explanations for late field information. The account preserves useful observations when a provider upload lacks a precise Work basis, and leaves a position claim unresolved until its establishment and identity basis is available. The present concept comparison can continue without choosing between the two delay explanations; reallocating liaison time would require the missing distinction and service conditions.

`OCE.3:4.1.1` uses that difficulty to construct functional repair, a recurring stream/enabling combination and a conditional provider hybrid. The functional repair connects earlier evidence requests and exception return while retaining specialist contribution and independent acceptance. A first stream candidate fails when the required specialist interval is already committed to protected service. Its revision needs a different qualified interval, compatible recognition and a fallback; those conditions remain prospective. The pattern uses C.32/MWA, CRC/RS and the direct OCE suppliers to compare the whole combination and its burden. The small set needs no Archive/Front, and `C.17` can characterize candidates after generation.

`OCE.4` selects several structures and writes possible-future contribution-relation specifications for electrical and platform evidence, provider artifacts, Safety acceptance, the release decision, and field-service information return. The specifications describe proposed relations; later realization must establish whether they obtain.

`OCE.5` establishes one continuing release-evidence integration position because vacancy, holder replacement, expected contribution, and eligibility matter across releases. Safety acceptance and release authority stay outside that position.

`OCE.6` returns one effective holder assignment and rig-access relation, one provider-access relation that is decided but not effective, separately held acceptance and release authority, a missing responsibility governor, and a bounded capability gap. The receiving practitioner can act on the distinct effective and missing conditions.

`OCE.7` compares organization-side, product-side, joint, and bounded-mismatch candidates. PumpWorks selects a bounded joint change while shared platform, independent Safety, scarce capability homes, and provider support remain deliberately non-isomorphic.

`OCE.8` holds the weekly evidenced package and acceptance basis stable, keeps the quarterly functional handoff as baseline-only, and completes three whole candidates: `PW-WA-INTERNAL-PLATFORM`, `PW-WA-DUAL-HOLDER`, and `PW-WA-HYBRID-TRACE`. Participant knowledge changes named option and protection positions. The hybrid is only a probe recommendation; missing trial DecisionSubject/authority, ineffective provider access, and unresolved protection/recovery evidence make the current disposition `reroute`, not a `ChoiceResult`.

OCE.15 repairs the named-use repertoire and, when a reusable move is missing, constructs an evidence-handoff repair candidate. Its worked continuation in OCE.15:5.1 derives a scoped producer–receiver comparison from the difficulty, distinguishes it from the target operating routine, and changes participation when a workshop would interrupt service. OCE.15:5.2 compares the complete additional work with a sufficient facilitated continuation; the added inquiry stops if its allocation choice can no longer benefit. These are conditional constructions, not already performed trials. The current Method Engineering Principles Framework supplies the applicable general qualification, trial and worth decisions.

For a hypothetical simultaneous repository-consolidation change, OCE.16 asks whether retiring the existing Electrical evidence-return contribution at migration completion can remove evidence needed for Engineer-E27's challenged-package integration action. It keeps the hybrid recommendation, trial authority, provider access, E27 assignment and rig access, Safety acceptance, release authority, protection, and recovery as separate claims. ME.6 supplies comparison of retirement, bounded retention, qualified replacement, and the incumbent; authorized owners decide, applying C.11 when a precise choice result is needed, while OCE.4 and OCE.6 own changed contribution and effective-relation results. OCE.16 returns those governed results or exact gaps to both changes and makes no second selection. Its conditional support-retirement continuation shows a sufficient current answer completing the question. A new package-specific uncertainty justifies extra qualification only when its full additional work is accepted for a still-attainable receiving benefit; a ready answer or missed useful window removes that addition, without making the hybrid trial admissible.

Enter at the question relevant to the current work and stop when its needed result has been obtained. At this point, the hybrid arrangement remains a recommendation with explicit realization and evidence gaps.

<a id="conditioned-continuation----realization-participation-service-and-leadership"></a>

### OCE.Application:1.1 - Conditioned continuation -- realization, participation, service and leadership

The following is a new hypothetical six-week continuation beginning after the OCE.6 appointment's effective date. It does not alter the initial recommendation or reroute. Suppose the properly authorized decision-maker separately authorizes a bounded representative probe; the provider and security owner make permitted access effective; qualified learning and service owners supply the practice, coverage, protection and recovery conditions. The missing coordination-responsibility predicate remains missing.

OCE.9 follows the weekly contribution from Electrical evidence through provider suggestions and E27's source/version check to separate Safety acceptance. A failed rehearsal exposes an ambiguous version cue. Its owner repairs the cue; a qualified provider supplies practice, feedback and fresh uncoached assessment. The probe supplies evidence to a separate bounded OCE.8 decision that selects limited hybrid use. Three later weekly package-preparation episodes, including a provider-failure manual return and one without the initiating facilitator, support only the stated release family, configuration, participants/support and observation window.

OCE.10 distinguishes an access defect from the discouragement of early disclosure through blame and date-only recognition. The authorized intervention changes the challenge/response and recognition practice, with qualified practice where needed; subsequent peer use supports a narrow local result, not an isolated causal effect or whole-organization culture. OCE.12 supplies the contribution brief, role support, task feedback and debrief through several capable participants, including the manager who obtains time and the learning provider who owns the assessment.

OCE.11 accounts for learning, setup, extra review and debrief inside the supplied change allowance. An incident consumes the reserve and reduces change work; the displaced probe remains unperformed. A current retention/replacement result returned through OCE.16 and ME.6 is applied to the support interval and hand-back without another comparison. The pattern bodies provide the actions, numerical service example, stops and evidence limits. General reliability, customer benefit and enduring culture would require their own observations beyond this constructed case.

<a id="consequence-comparison-and-authorized-support-revision"></a>

### OCE.Application:1.2 - Consequence comparison and authorized support revision

The following further episode is constructed. It adds observations after the separately authorized limited use, without changing the initial reroute or the six-week continuation. A locally qualified procedure supplies two eight-week before/after windows for the same release family, with the same eligibility and counting rules.

| Supplied observation | Before | After | OCE.13 result |
| --- | --- | --- | --- |
| Late integration-evidence returns among eligible crossings | 8 of 40, or 20% | 3 of 40, or 7.5% | A lower observed late proportion under the stated rule. |
| Field-service follow-ups missing their agreed information window | 2 of 20, or 10% | 6 of 20, or 30% | A higher observed late proportion under the stated rule. |
| Protected reports of unplanned cross-checking after formal hours | No comparable earlier report set is supplied. | Some participants report additional work. | A bounded report whose population reach and causal interpretation remain limited. |

Staffing, incident and product mix remain possible explanations. OCE.13 preserves the improvement beside the service loss; it supplies neither a net-success score nor attribution of either change to the hybrid arrangement. The next question concerns the actual release-support and service assignments and their work intervals.

For the OCE.14 continuation, suppose a separately supplied assignment/Work account confirms that the same support holder is committed in incompatible windows. Qualified service and employment owners supply protected coverage and feasible substitution; the actual organization owner can change that allocation, and the direct owners confirm a recoverable manual arrangement.

OCE.14 compares retaining the current assignment with observation, repairing the support interval and qualified substitution, and suspending the affected hybrid contribution with manual recovery. Under the supplied service constraint, unchanged double allocation is not an admissible continuation. The proper owner selects the support repair and accepts a reduced allowance for other change work. Safety acceptance and release authority remain separately held; the missing coordination-responsibility predicate is not supplied by this choice.

Suppose the required allocation and holder-acceptance acts then occur. OCE.6 supplies the changed effective relation where applicable. OCE.9 receives the still-unrealized support integration, OCE.11 the protected overlap and hand-back, and OCE.13 the next comparable observations. OCE.16 is used only if another separately managed change consumes the altered condition. If protected coverage is unavailable, the dependent repair stops; the descriptive comparison and unaffected earlier results remain usable.

<a id="app-oce-02---public-hospital-emergency-flow-change"></a>

## OCE.Application:2 - APP-OCE-02 - Public hospital emergency-flow change

| Change question | Application |
| --- | --- |
| Situation | A public hospital emergency department must reduce unsafe waiting and handover loss while continuous clinical service, statutory authority, labor constraints, and patient protection remain in force. |
| focus and current account | `OCE.1` bounds the department and safe timely care contribution; `OCE.2` separates actual clinical Work, assignments, treatment decisions, information use, bed access, and service provision. |
| Concepts and contribution design | `OCE.3` compares incumbent repair, a cross-specialty flow configuration, and a hospital/community-provider boundary change. `OCE.4` specifies who supplies and receives diagnostic information, who transfers patients and accepts handover, and who supplies bed access, escalation decisions, treatment decisions, and continuing service. Distinguish proposed relations shown in a pathway view from relations already in effect. |
| Position and assignment branch | Use `OCE.5` to define a stable coordination or acceptance position when its establishment, vacancy, and continuation matter. Otherwise proceed directly to holder assignment under `OCE.6`. Verify the holder's license, the kind and effective interval of the shift or appointment, clinical authority, access, equipment, and labor/fatigue conditions separately. |
| Paired architectures | Use `OCE.7` to compare the selected hospital organization and emergency-service architectures. Statutory clinical authority, shared diagnostics, facility constraints, and uninterrupted Operations may justify retaining a bounded structural mismatch instead of mirroring a product-team structure. |
| Work arrangements | `OCE.8` compares complete ways to produce the same required result: for example, changing the qualified holder, improving an interface, obtaining a provider contribution, or combining clinician and AI performance. Use clinician/pharmacist, other worker/Operations, patient/caregiver, and provider knowledge to examine the options. Obtain the licensure/authority, clinical-safety, privacy/data, provider-continuity/exit, workforce, and protection results needed for each option; an absent result blocks the action that depends on it. |
| Realization and participation | OCE.9 can prepare and exercise a bounded contribution only under the necessary clinical and service conditions. OCE.10 distinguishes access, workload, role understanding and local challenge norms rather than treating every gap as resistance. |
| Continuing service and leadership | Use OCE.11 to obtain clinical coverage, staffing/fatigue, privacy, and recovery results for the planned exercise before patient-facing exposure. OCE.12 organizes a qualified brief, debrief, or learning-support contribution. Qualify clinical competence separately and establish medical decision authority under the applicable rules. |
| Consequence comparison | OCE.13 examines a shorter admitted-case waiting time alongside changed case mix, more severe-case diversion and missing follow-up. It returns the exact measurement and clinical comparison question rather than inferring patient benefit for all arrivals. |
| Authorized revision | An applicable clinical-safety requirement may justify a bounded protective pause ordered by an authorized decision-maker under OCE.14 before overall causal attribution is settled. The pause remains within that decision-maker's clinical and statutory remit and the applicable worker-protection conditions. |
| Method return | OCE.15 first uses an adequate current procedure or supported continuation. If a reusable move is missing, it follows the failed receiving contribution to a proposed action and its conditions; the clinic supplies its own clinical criteria, authority and protected care requirements. Implementation and organization outcomes remain distinct from patient, worker and service results. |
| What fails or stops | PumpWorks cadence, product-team topology, release authority, and provider assumptions do not transfer. Verify clinical Work, authority, access, and patient benefit independently of a pathway description. |
| specialist return | Clinical safety, medical authority, labor, privacy, legal, public-governance, and Operations Management results are required where they change the decision. |
| Non-transfer boundary | OCE helps organize the change and formulate requests to qualified clinical, legal, labor, and service-continuity decision-makers. Those specialists supply the substantive judgments within their respective remits. |

<a id="app-oce-03---distributed-member-governed-standards-association"></a>

## OCE.Application:3 - APP-OCE-03 - Distributed member-governed standards association

| Change question | Application |
| --- | --- |
| situation | A distributed professional association wants faster evidence-backed standards revisions, but Work is performed by members across independent employers and no single executive holds universal assignment or change authority. |
| focus and current account | `OCE.1` tests whether the association, one committee, or a cross-organization coalition is the changed System. `OCE.2` recovers volunteer Work, member assignments, bylaw authority, evidence use, publication decisions, and provider services. |
| Concepts and contribution design | Use member and secretariat knowledge to generate and compare alternatives under `OCE.3`. `OCE.4` specifies evidence supply, editorial return, ballot, publication-service, employer-resource, and volunteer-coordination crossings while keeping the different legal and employer structures visible. |
| Position and assignment branch | Use `OCE.5` to define an editorial-chair or treasurer position, including its establishment rule, any required member decision, term, expected contribution, and eligibility. The position need not be an employment position. Under `OCE.6`, establish the elected or other bylaw-governed assignment through the required acts. Verify volunteer acceptance, repository/publication access, financial authority, employer permission, and the relevant effective intervals separately. |
| Paired architectures | `OCE.7` compares the selected member/editorial organization architecture with the standard-development and publication-service architectures. A bounded mismatch may be worth retaining: changes to ballot rules, repositories, publication services, and employer arrangements can follow different timetables, while language-community needs and volunteer availability constrain who can participate and when. |
| Bounded realization and participation | In a separately conditioned continuation, qualified editorial participants have volunteer acceptances, lawful evidence use, translation, and repository support. Under OCE.9 they prepare one amendment packet through submission, challenge, and correction. Under OCE.10 they try an asynchronous challenge-and-response practice; later peer use can support a narrow observation of changed participation norms. Packet preparation is not adoption of a standard. |
| Continuing service and leadership | Use OCE.11 to protect accepted volunteer and publication windows and stop a decision that requires the chair's authority when that term expires. OCE.12 organizes peer facilitation, qualified practice and feedback, and a later editorial episode in which participants can demonstrate the capability. A mentor need not be a manager. |
| Revision after changed authority | OCE.14 can return an editorial/evidence-return reassignment as a proposal when the chair's term has ended. Only the body or office-holder authorized under the current bylaws may make the required decision; any interim continuation stays within existing rules. |
| Practice continuation | Use OCE.17 to examine how members encounter and continue OCE moves under their participation and evidence conditions. Obtain any needed association-governance decisions and employer permissions separately. |
| Method return | OCE.15:5.3 derives scoped asynchronous review from the needed editorial contribution and members' participation conditions, while retaining a separate decision gap when the chair's authority has expired. Member consultation supplies neither adoption nor authority; reuse a sufficient existing procedure before developing another. |
| Simultaneous-change return | Suppose a credential-issuer change expects authorization from an incoming elected chair, while the election change expects new credentials before the ballot that establishes that chair. Under OCE.16, examine the supplied bylaws, current authority, credential evidence, ballot rules, and term windows to assess the claimed circular dependency. Use ME.6 to compare order/support arrangements and OCE.4 and OCE.6 to resolve contribution and enabling relations; obtain the bylaw-authority judgment from the association's authorized governance body. Return the resulting credential and authorization/order conditions to both changes. An expired term remains expired. |
| What fails or stops | Employer hierarchy, employee-only participation, and a single-company position or assignment model do not transfer. Missing required member, bylaw, employer, or provider authority blocks establishment or use of the dependent relation. |
| specialist return | Association governance, applicable law, publication, finance, and employer commitments remain separately owned. |
| Non-transfer boundary | Establish each organization's authority and commitments under its own rules. Use those conditions when designing and comparing organization relations and candidate change Methods across organizations. |

<a id="app-oce-04---oce-practice-across-a-practitioner-population"></a>

## OCE.Application:4 - APP-OCE-04 - OCE practice across a practitioner population

This constructed application concerns eight OCE practitioners across three organizations, not the working culture of one target organization. The population is not asserted to be one System. Supplied permitted case extracts, practitioner explanations, a shared source example and peer-recognition questions allow examination of one OCE.2 move: recovering actual contribution and receiving-decision relations.

The old “organization mapping” label is fading. Four observed cases still recover actual Work, evidence-return and decision relations under different titles. Two newer cases provide filled charts but do not recover the relevant crossing; their explanations do not yet close it. Two practitioners have no suitable permitted case in the period.

Using OCE.17, the group first separates three results: continued operative use in the four observed cases; a bounded gap to investigate in the two chart-only cases; and unobserved use for the two without opportunity. The group compares a usable crossing with the shared deficient example and finds that its recognition question rewards completed department boxes. This finding gives the group a reason to examine how the move is taught and how its use is recognized. It does not yet establish a sole cause or an individual capability deficit.

The existing qualified case-help arrangement is sufficient: within the group's permission, the facilitator and willing practitioners critique the cases, retain usable variants and replace the deficient example with a source-linked case and counterexample. Later feedback asks for the usable contribution and decision relation. The arrangement carries the owners' protected-material preparation, participants' case work, qualified explanation, later opportunity and interpretation, and upkeep of the changed example. Use it without a second diagnostic or clinic. A permitted opportunity still comes from its owner; employment, learning assessment and evidence-access decisions keep their own authorized and qualified providers.

In the fictional follow-up, one practitioner independently recovers the crossing and receiving authority in a different case; another lacks permitted evidence access. The first is an observed later use, while the second is an access gap. These observations support neither causal attribution to training nor profession-wide retention.

Return the access question to the person or body responsible for granting it. Use HCD.3 only if distinguishing a human capability, misconception, or behaviour limit from an access or work-condition gap would change the next action. Return a specific reusable-Method defect to OCE.15/Method Engineering if the critique discovers one; correcting an example does not by itself call for a new Method variant. Use OCE.10 for working-culture questions about the target organization. OCE.17 gives the complete practice sequence and an unlike association case. Its mentor-departure case also compares adequate continuing provision with an additional local handover: retain common qualified work, accept the complete increment only for the timely receiving benefit, and cancel duplicate or late preparation when that benefit disappears. These are conditional constructions, not effectiveness evidence.

## OCE.Application:End


# Framework Boundary and Refresh

<a id="intended-use-and-ordinary-non-use"></a>

## OCE.Reference:1 - Intended use and ordinary non-use

Use this framework when an intended contribution requires deliberate change to an organization's relations or capability, or when such a change creates material consequences. Enter OCE.17 when the continuation or renewal of OCE practice among practitioners is the working question. Use one pattern or a small cooperating set.

Do not use it merely because Work occurs inside an organization, a manager makes a routine decision, an operating flow needs coordination, one person needs capability development, or a product requires engineering. Use the practice that owns that question; return a result to OCE only when an organization-change decision needs it.

<a id="patternid-and-reader-order"></a>

## OCE.Reference:2 - PatternID and reader order

`OCE.*` is the Organization Change Engineering PatternID namespace. Numbers are stable addresses, not steps. The Parts provide reader order. A dependency identifies a result needed for a particular use.

<a id="using-the-available-methods"></a>

## OCE.Reference:3 - Using the available Methods

This publication contains all seventeen pattern bodies. For the selected use, gather the required case observations, obtain professional contributions, verify authority and effective relations, and check which planned results have actually been realized. If a needed Method is not provided here or in an available sibling framework, obtain a qualified contribution or stop the dependent action.

<a id="pattern-selection-and-result-relations"></a>

## OCE.Reference:4 - Pattern selection and result relations

| Working question | Start or continue with | First returned result | Main return or continuation |
| --- | --- | --- | --- |
| Which organization and contribution are being changed? | `OCE.1` | Bounded organization-change focus | `OCE.2`, `OCE.3`, or the direct owner of a non-OCE question |
| What Work and relations obtain now? | `OCE.2` | Grounded current organization account | `OCE.3` or the exact missing evidence/relation owner |
| Which materially different organization concepts deserve comparison? | `OCE.3` | Status-preserving concept set and decision | `OCE.4`, conditional `OCE.5`, `OCE.7`, or `OCE.8` |
| Which contribution paths and specialization boundaries should guide design? | `OCE.4` | Contribution-architecture decision and possible-future description, including relation specifications | `OCE.5`, `OCE.7`, `OCE.9` for realization, or the owner of the needed relation |
| Does a stable institutional position need to exist? | `OCE.5` | Position identity and establishment/continuation result, or direct-arrangement return | `OCE.6` or the applicable institutional owner |
| Which assignments and enabling relations obtain? | `OCE.6` | Predicate-specific effective relations and exact gaps | `OCE.9` for realization, `ADM.2`, or the relation owner |
| How should product/service and organization architectures constrain each other? | `OCE.7` | Separate coordinated decisions across four candidate forms | product/service owner, `OCE.9` for realization, or continuing Operations |
| Which complete work arrangement can produce the same bounded result? | `OCE.8` | Same-result baseline and whole-candidate comparison, followed by an authorized choice or probe, rejection, or reroute; a preliminary result may be a recommendation | Obtain the needed capability, assignment, provider, safety/domain, or Operations result from its owner. Use OCE.9 to realize missing conditions; dependent trial Work still needs its own authorization. |
| How can the selected organization contribution become usable? | OCE.9 | Bounded capability increment or exact failed/unrealized condition | OCE.6, OCE.10–OCE.12, receiving operation or the direct result owner |
| Which response can repair this participation or working-culture gap? | OCE.10 | Supported response and bounded consequences when performed, or an unresolved competing explanation or gap; no new contrast when the current response is sufficiently supported across rivals | direct relation/learning owner; OCE.9, OCE.11 or OCE.12 where its result is needed |
| How can change and continuing service coexist? | OCE.11 | Authorized overlap, observed service/change consequences and hand-back, or deferral/stop | current ME.6, OPS.5–OPS.7, OCE.8/OCE.16 or the exact service/protection owner |
| Which leadership contribution is missing or dependent on one initiator? | OCE.12 | Performed contribution and tested continuation arrangement, or exact support gap | qualified learning provider, OCE.10/OCE.11, assignment/authority owner or OCE.15 |
| What changed, for whom and under which conditions? | OCE.13 | Qualified consequence comparison with conflicting results, competing explanations and gaps, or an observation plan | OCE.14, OCE.10/OCE.11, or the owner of the needed measurement, evaluation or affected-result judgment |
| Which organization relation should now be retained, repaired, replaced, reversed, stopped or investigated? | OCE.14 | Authorized disposition with effective scope, losses and remaining work; otherwise a proposal or authority request | OCE.6/OCE.9–OCE.12, later OCE.13, and OCE.16 only for an actual cross-change consumer |
| Which organization-change Methods are usable and worth developing? | OCE.15 | Named-use repertoire or domain candidate account | Method Engineering and the exact missing OCE result owner |
| Which other separately managed change uses the organizational condition now being altered? | OCE.16 | Qualified cross-change question, direct exit, or specific missing result; then return of the resolved condition to each affected change | ME.6, C.32.MWA, the applicable OCE/OPS/A.15 Method, or the specialist responsible for the needed decision or result |
| Which OCE practice continues across practitioners and work settings? | OCE.17 | Scoped continuation account, a retained practice variant, permitted intervention, or specific return, with later observation or a named gap | OCE.15/Method Engineering for a reusable-Method problem; applicable HCD or direct opportunity, authority and evidence owners |

Choose the next pattern from the result needed, not from a presumed lifecycle. OCE.13/OCE.14 can use a direct result without repeating a wider evaluation; OCE.17 can support retaining useful practice without a new intervention.

<a id="source-use-and-currentness"></a>

## OCE.Reference:5 - Source use and currentness

<a id="source-use-and-conceptual-synthesis"></a>

### OCE.Reference:5.1 - Source use and conceptual synthesis

Recover a Method across descriptions, instruments, practitioners and variants while distinguishing it from performed Work and capability. Recover each project, process or case account's direct subject first: a plan, reusable procedure and unresolved authority claim can contribute to the same change without describing the same Work. Common-Work viewpoints are useful when that Work is actually their shared subject. Use only the correspondences needed for assignments, participation or capability development. Learning, professional Work, organization and platform development, and inquiry can contribute at different scales; distinguish their results when choosing or revising a change.

Each pattern's SoTA-Echoing section relates its working answer to sources, alternatives and limits. OCE.1–OCE.3 compare their focus, reconstruction and concept-generation methods at a bounded common effort and identify the affected body sections. The summaries below highlight contributions that span several decisions or impose a significant reliance boundary.

For the early design questions, the [Star Model](https://jaygalbraith.com/wp-content/uploads/2024/03/StarModel.pdf) supplies a serious policy-fit alternative. OCE.3 adapts its constructive lesson: grouping, information, decisions, participation and support must work together, and compensation for an adverse interaction belongs in the compared candidate. The [current Team Topologies concepts](https://teamtopologies.com/key-concepts) supply a serious conditional team/interaction alternative; their scope is tested against the actual contribution, independent authority and continuing-service conditions. These comparisons do not establish empirical superiority of OCE.

The shared architecture also draws on sources whose contributions span the early design and Method questions. [Albert's organization-structure account](https://doi.org/10.1007/s41469-023-00152-y) distinguishes activity, decision and legal-entity perspectives. OCE.1–OCE.7 retain several selected structures because those perspectives can expose different work and authority claims. Those perspectives provide useful views, not an exhaustive organization ontology. The [work-design review by Fraccaroli, Zaniboni and Truxillo](https://doi.org/10.1146/annurev-orgpsych-081722-053704) keeps actual work characteristics and affected-person outcomes in design. The [participatory-prototype study](https://doi.org/10.1016/j.apergo.2023.104012) supports making a proposed arrangement understandable to participants; it does not establish that the arrangement is enacted or effective.

For coordinated architectures, OCE.7 adapts the contingent line developed in [Joseph and Sengul's organization-design review](https://doi.org/10.1177/01492063241271242), the [modularity synthesis by Brusoni and colleagues](https://doi.org/10.1093/icc/dtac054) and the [value-and-mirroring case by Burton and Galvin](https://doi.org/10.1016/j.jbusres.2022.07.023). Organization and product structures can affect one another while their desirable correspondence changes with regulation, value, search and evolution. Conway's communication argument remains a historical anchor. The practitioner consequence is to compare organization-side change, product/service-side change, joint-change and bounded-mismatch candidates for the same pair and horizon, then use evidence about that pair to choose the next move. An industry case or software guideline supplies no universal organization form.

OCE.15 uses the [change-intervention review by Hagl and colleagues](https://doi.org/10.1016/j.hrmr.2023.101000) and the [implementation-framework review by Wang and colleagues](https://doi.org/10.1186/s13012-023-01296-x) to retain different intervention contributions and implementation functions. [Nilsen's 2015 taxonomy](https://doi.org/10.1186/s13012-015-0242-0) supplies a historical distinction among framework functions; [ERIC's 2015 catalogue](https://doi.org/10.1186/s13012-015-0209-1) supplies candidate implementation strategies. The [2025 CFIR User Guide](https://doi.org/10.1186/s13012-025-01450-7) strengthens situation-specific determinant inquiry; a determinant account still leaves the intervention Method to be selected or constructed. [The ten-year review of implementation outcomes](https://doi.org/10.1186/s13012-023-01286-z) also limits inference from adoption or implementation success to later service and organization results. [Implementation Mapping](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2019.00158/full) supplies a serious constructive comparator; its [2025 review](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2025.1603178/full) preserves context, effort and evidence limits. OCE.15:4.1.1–4.1.2 and :5 derive the organizational procedure only for the remaining question, using C.39 and current ME rather than treating a taxonomy, organization description or successful work result as the way of acting. Source-local concepts and operations retain their different subjects and conditions.

For engagement and continuation, the [ADKAR](https://www.prosci.com/methodology/adkar) and [Kotter](https://www.kotterinc.com/methodology/8-steps/) provider accounts used in this edition are serious repertoire comparators. They contribute targeted support, enabling action and reinforcement; Kotter's account also describes evolution from steps into accelerators. In the OCE case, practitioners still need to establish which organization relations obtain, whose authority applies and what service recovery or capability evidence supports the intended action. Provider descriptions are not independent evidence that one school is more effective.

For OCE.8, Naikar et al. and Waterson et al. contribute distributed sociotechnical and responsibility/recovery questions. Vaccaro et al.'s findings support comparison with the best applicable solo arrangement when synergy matters. NASA and Lagomarsino et al. contribute human/automation/robotic allocation and dynamic-reallocation questions. ISO 6385:2016 contributes ergonomic requirements and ISO 10218-1/-2:2025 industrial-robot safety requirements; check the editions and requirements applicable to the proposed work. The voluntary NIST AI RMF 1.0 contributes third-party, monitoring, incident, recovery, override, and change-management questions; check later revisions before relying on those contributions. Aksin and Masini plus Goth et al. bound shared-service configuration and cost claims. The local choice still needs authority and a whole-arrangement comparison, followed by separate provision and enactment evidence. Require a human in the loop only when the direct authority, safety, or performance basis warrants it.

For OCE.16, Kanitz et al. support inquiry into cross-initiative cognitive, normative, and procedural interference. Skov and Lê help distinguish a claimed inconsistency from established conditions. Rishani et al. distinguish membership, allocation, variety, informational benefit, and burden; Zhang et al. add participant-specific timing pressure. Martinsuo and Ahola challenge one-firm governance assumptions. Fischer et al. provide a serious bounded comparator connecting dependency-aware selection, implementation and owner feedback, not merely a portfolio label. Use an adequate current answer directly. OCE.16:4.1/:5/:9–:11 explain the priced residual qualification and per-change return, including the sufficient-answer and missed-window exits. Keep source-local subjects and authorities; the comparison is conditional and does not establish empirical OCE effectiveness.

For OCE.9–OCE.12, Implementation Mapping and its 2025 review support cause-sensitive intervention with explicit limits; the 2025 CFIR guide supports inquiry into determinants, not an implementation procedure. The transfer, LOCI, and TeamSTEPPS sources connect qualified practice, feedback, workplace support, and concrete leadership contributions. Use the sociotechnical-prototype experiment to plan participant inspection; verify cooperation during actual Work. SRE examples help plan bounded exposure and recovery, but their software thresholds and trade-offs do not override the target domain's hard protection conditions. The bodies explain the alternatives, practical moves, and source limits. The constructed OCE cases illustrate those moves rather than establish their empirical effectiveness.

For OCE.17, the [NPT coding manual (2022)](https://doi.org/10.1186/s13012-022-01191-x) and [NPT-derived strategy synthesis (2025)](https://doi.org/10.1186/s13012-025-01444-5) contribute mechanism-sensitive inquiry and intervention candidates. The latter interprets 63 NPT-using health/social-care studies published through 2021, not comparative OCE effectiveness. The [2026 consolidation, version 1](https://doi.org/10.3310/nihropenres.14315.1), with two reviews approved with reservations, strengthens changing-context and burden questions; it supplies no general cultural-evolution or individual-learning proof. OCE.17 retains competent current inquiry, adaptation and support as a sufficient alternative. Its domain comparison at :4.4/:5/:9/:11 adds only a missing contribution, prices the complete continuations and tests ready-answer and lost-window conditions; it claims no general advantage over that practice.

For OCE.13/OCE.14, the [MRC update (2021)](https://doi.org/10.1136/bmj.n2061) contributes questions about the decision, context, stakeholders, and uncertainty. The [Magenta Book (May 2026)](https://www.gov.uk/government/publications/the-magenta-book/magenta-book-central-government-guidance-on-evaluation-html), especially §§2.2.1–2.2.2 and §3.4, supports proportionate evidence use and explanatory limits. OCE adapts these contributions from health-intervention research and government evaluation to the design of local comparisons. Obtain local measurements, qualify causal claims, and make organization-design and professional decisions separately. The bodies give the concrete comparisons, alternatives, and reopen conditions.

Refresh only the affected pattern or repertoire claim when a governing FPF distinction changes, a direct source changes practitioner action, a representative case defeats a branch, or use exposes a missing OCE move. A new publication alone does not reopen the framework.

<a id="fpf-dependency-and-compatibility"></a>

## OCE.Reference:6 - FPF dependency and compatibility

**FPF sources.** This framework uses the **First Principles Framework (FPF) — Core Conceptual Specification** and the patterns named in the OCE bodies. The ordinary links lead to evolving public text; a link alone does not identify the edition underlying a particular claim.

**Recovering a comparison baseline.** To assess a later FPF change, obtain from the OCE author or source holder the previously used FPF passage and any additional host text for the consuming OCE claim, identified by PatternID and text edition. Compare those texts with the proposed changed source. Until the earlier text is recovered, the before/after compatibility conclusion for that dependency remains unresolved. Other OCE uses can continue when their needed premises and results can be established independently.

**Direct uses.** FPF supplies concepts and rules for System recognition, affected-System discovery, direct relations and selected structures, Work and WorkPlans, assignments and performers, capability, evidence, comparison, choice, Method identity and description, several-structure reconciliation, currentness, and culture mechanics. OCE applies these to organization-change situations, domain relations and Methods, participants, authority, consequences, and receiving results.

**Conditions of outside results.** C.32.MWA, A.15.8 and A.15.9 answer different architecture, work-performance and outside-result questions. Use the relevant source's stated applicability, status and claim limits. OCE.16 can expose a need for their contributions; use a supplied result only within the conditions it establishes. A route to a Method does not provide that result.

**Compatibility.** A compatible FPF change leaves unaffected OCE results reusable. A changed relied-on kind, relation, Solution, or result form reopens only the consuming pattern and dependency claim.

**Dependency and contribution direction.** This release uses FPF's transdisciplinary concepts and rules. Return a transdisciplinary discovery to FPF and an organization-change-specific move to OCE. Propose a change of placement through the owning framework's decision; keep one authoritative definition of the moved content.

<a id="current-method-engineering-dependency"></a>

## OCE.Reference:7 - Current Method Engineering dependency

The supplying product is the [Method Engineering Principles Framework](METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md). OCE.15 uses ME.1 for Method focus, ME.2 for named-use repertoire structure, ME.3 for situation criteria, ME.5 for individual qualification, ME.8 for executable explanation from supplied knowledge, ME.9 for a needed correspondence between unlike accounts, ME.11 for trial, ME.13 for fit/transfer, ME.14 for worth, ME.15 for variants/provenance, and ME.16 for introduction/observation/revision. FPF C.39 supplies general construction and connection of operations; C.39.RO develops reuse beyond one case. OCE.15 fills the organizational contribution and interaction that the receiving use still needs.

OCE.16 uses ME.6 when Methods or candidate accounts can be co-used in materially different ways because of composition, Work order or overlap, allocation, subject/support arrangement, provider access, authority, evidence, burden, description, culture, or another selected structure. ME.6 can return a relation-only arrangement while the Methods remain unchanged. OCE.16 only discovers and qualifies a cross-change input before that comparison and returns its governed result afterwards.

OCE.9 and OCE.10 use ME.16 to obtain a needed Method-introduction result. OCE.9 first checks whether that result already supports the bounded organizational contribution and adds only worthwhile remaining realization; OCE.10 retains its participation question. OCE.11 obtains ME.6's qualified co-use result when its overlap question requires one and applies it without a second comparison. OCE.12 and OCE.15 return a leadership Method-account or repertoire question to the current Method Engineering result that answers it.

OCE.17 returns the actual practice problem, variant, case conditions and continuation evidence through OCE.15 when the reusable Method needs work. A cultural intervention does not itself qualify a Method variant, development intervention or transfer result.

OCE.15 supplies the Method Engineering work with the organizational difficulty and evidence, the constructed intervention, reasons for its operations and returns, participants and affected Systems, decision-sensitive conditions, authority/capability/support/protection, bounded mechanism claims, distinct implementation and organization results, full burden and change triggers. If a qualified current result already answers the use, it is applied without a duplicate construction. OCE.16 supplies an account of the separately managed changes, altered organizational condition, consequential consumer action, interaction window, participant and evidence basis, and required return to each change. Use the supplying framework's [Table of Contents](METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#table-of-contents) to find the named Method and obtain its result.

Apply the supplying Method to qualify an OCE candidate or obtain the needed fit, trial, transfer, or variant result. Use local evidence for introduction, adoption, and effect claims, and establish authority for a cross-change arrangement separately. Reopen only the consuming OCE claim when a named ME result changes, becomes unavailable, or no longer answers the receiving use.

<a id="sibling-domain-returns"></a>

## OCE.Reference:8 - Sibling-domain returns

Use Strategy for direction and commitments, Corporate Governance and the applicable legal practice for authority, Organization Administration for continuing provision, Operations Management for continuing Work, Human Capability Development for one person's capability development, and Systems Engineering for product/service engineering decisions. Obtain legal, safety, medical, ecological, labor, financial, and other professional judgments from qualified specialists. Check the available body or provider before relying on a specific result.

The supplied [Operations Management Principles Framework — First Edition](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md) contains OPS.1–OPS.20. This OCE framework uses the named OPS.1–OPS.7 results for bounded operating-scope, work-management, state, shared-attention, admission, case-continuation, and service-commitment questions. Other OPS patterns remain available under their own working conditions; their presence does not silently make them inputs to every OCE use. OCE.11 coordinates a bounded change/service overlap using the actual service or applicable OPS result; OCE.16 returns cross-change questions to the same direct owners.

The [Human Capability Development Principles Framework](HUMAN-CAPABILITY-DEVELOPMENT-PRINCIPLES-FRAMEWORK.md) supplies Methods for human development. OCE.9, OCE.10, OCE.12 and OCE.17 use HCD.1, HCD.3 and HCD.4 where applicable: representative later-work demand, a human target or non-training diagnosis, and a condition-qualified capability profile. OCE.9 also identifies the practice-design, support, feedback and assessment Methods needed to develop a missing human contribution. Use HCD's current Table of Contents for further programme, transfer, retention and revision questions. A Method's presence supplies guidance; an OCE case still needs the performed contribution and its qualified result. Changed task or support conditions reopen the consuming result, not the whole framework.

The HCD source qualifies E.23.CAE's observation-first reference contrasts for HCD.3. The applicable HCD bodies and OCE.8:4.2 also qualify uses of E.23.CDI concerning the independently identified holder System, baseline and target capability, limiting contribution, protected conditions, and representative transfer evidence. Use each within those receiving boundaries and its own stated applicability. OCE.17 requires the applicable HCD result and a separate System basis for any claim that its practitioner population is one capability holder.

The [Systems Engineering Principles Framework](SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md) provides SYSE.11 for a bounded System/configuration-use question. When SYSE.11 already supports the bounded organizational contribution, OCE.9 uses that result with its limits and fallback. If a contribution or participation relation remains unrealized, establish only that missing condition and the evidence needed for its receiving claim; do not repeat adequate integration. Open the supplying SYSE.11 body for its configuration/use conditions.

Use [Problem Structuring and Decision Support](PROBLEM-STRUCTURING-AND-DECISION-SUPPORT-PRINCIPLES-FRAMEWORK.md) when the missing result is inquiry or advice: for example, a bounded advising engagement, plural problem formulations, an alternative set, a value-sensitive comparison or a qualified recommendation. PSD.1 establishes the engagement and authority boundary; PSD.3 supports competing formulations; PSD.8–PSD.13 supply the needed alternative, comparison and recommendation contributions under their own conditions. OCE supplies its organization-specific result to that work. The adviser can return a useful comparison or exact missing premise while the recipient's choice and organization-change authority remain separate.

Use [Development Opportunity Construction and Development Direction Advising](DEVELOPMENT-OPPORTUNITY-CONSTRUCTION-AND-DEVELOPMENT-DIRECTION-ADVISING-PRINCIPLES-FRAMEWORK.md) when useful future work or a development direction still has to be constructed. DOCA.1–DOCA.4 can recover the inquiry, worthwhile problem, prospective contribution and support configuration; DOCA.5 examines whether necessary conditions can hold together. These uses can stop at a conditional opportunity without an adviser or a selected programme. For an organization, OCE.8 becomes the direct entry when one result, use and acceptance premise are sufficiently stable and the decision concerns whole ways to obtain it. A result for human learning, organization capability or AI support still comes from its own practice; a reachable direction or recommendation does not supply that result or authorize its realization.

When the needed sibling result is available and current for the use, apply it within its scope. Otherwise obtain a qualified direct contribution or name the missing result and the OCE action that depends on it.

<a id="representative-case-coverage"></a>

## OCE.Reference:9 - Representative case coverage

The applications and related pattern-local cases are constructed examples of combined use. Keep each episode's supplied facts and unresolved conditions visible when following its continuation; the examples illustrate the Methods, not empirical results about real organizations or practitioners.

| Case | Useful comparison or move | Boundary for reuse |
| --- | --- | --- |
| [PumpWorks AI-inspection releases](#oceapplication1---app-oce-01---pumpworks-weekly-ai-inspection-releases) | Connect design, assignment, and whole-arrangement comparison with OCE.15/OCE.16 Method and cross-change questions. Follow the separately conditioned OCE.9–OCE.12 continuation through a failed rehearsal, qualified practice, later use, participation intervention, service interruption, and peer leadership; then use OCE.13/OCE.14 for consequence comparison and support-allocation revision. | The initial quarterly baseline is outside the weekly OptionSet; the hybrid remains a recommendation and access remains ineffective in that episode. Later episodes supply their additional conditions. Release requires its own authorization, and the bounded observations establish neither general reliability nor enduring culture. Conflicting descriptive results supply no net-success or causal conclusion; missing protected coverage blocks the dependent repair, not the comparison. |
| [Public hospital emergency flow](#oceapplication2---app-oce-02---public-hospital-emergency-flow-change) | Choose between a stable position and direct assignment, verify licensed holders, and compare whole clinician/provider/human–AI arrangements while care continues. Follow patient/worker protection, privacy/data, provider-continuity/exit, and structural-mismatch questions through realization, participation, and leadership. Examine case mix when comparing waiting times; a separate qualified safety result can support an authorized protective pause. | Obtain medical, legal, labor, privacy, provider-service, and clinical-safety judgments from qualified specialists. Competence, coverage, fatigue, protection, and recovery conditions precede patient-facing trial work. Admitted-case waiting observations do not establish benefit for diverted or unobserved patients; a protective pause needs its own authority. |
| [Distributed standards association](#oceapplication3---app-oce-03---distributed-member-governed-standards-association) | Connect bylaw-governed assignment and the OCE.16 issuer/election dependency with amendment-packet preparation, asynchronous challenge, qualified translation and evidence use, accepted volunteer windows, and peer-facilitator learning. Consider a revision after the chair's authority expires. | Packet preparation is not adoption of a standard. Obtain Governance, ME.6, OCE.4/OCE.6, and professional results from their direct providers. Authority remains with bodies and office-holders established under association and employer rules; an expired term cannot support a new binding decision. A revision proposal remains a proposal until an authorized body or office-holder decides. |
| [OCE practitioner population](#oceapplication4---app-oce-04---oce-practice-across-a-practitioner-population) | Recognize operative use despite changed labels; distinguish chart-only cases from missing opportunities; repair a source example and peer recognition, then examine mixed later observations. | No single holder System is claimed for the population. An observed later use, an access gap, a learning effect, and profession-wide retention require different evidence. |

<a id="publication-boundary"></a>

## OCE.Reference:10 - Publication boundary

The full pattern bodies are the working references for each Method's moves, conditions, evidence boundaries, stops, and specialist returns. Use the Readme, Preface, Table of Contents, and applications to find and combine the relevant patterns.

This framework presents organization-change Methods and their relations. Use an instructional Guide for sequenced learning and memory formation. The Engineering DPF Suite Reference supports cross-framework lookup.

## OCE.Reference:End
