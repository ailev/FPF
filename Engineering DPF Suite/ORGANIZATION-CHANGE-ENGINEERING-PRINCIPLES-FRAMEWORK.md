# Organization Change Engineering Principles Framework

> A domain pattern language for changing an organization's contributions, working relations, and capability while its work continues.

- **Author:** Anatoly Levenchuk, with AI-assisted development and review
- **Version:** 3 September 2026
- **Status:** Eternal alpha: a published working framework, already used in analyses and worked applications, while continuing to evolve.
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
| [Organization Change Engineering Principles Framework Readme](#organization-change-engineering-principles-framework-readme) | Find a first useful result for common organization-change difficulties. |
| [Citation](#citation) | Cite the framework or one pattern with its author, title, release date, and publication address. |
| [Preface](#preface) | Distinguish actual arrangements from proposed ones and choose the structures relevant to the decision. |
| [Cross-Pattern Application](#cross-pattern-application) | Work through PumpWorks, a hospital, a member-governed association, and OCE practice across practitioners. |
| [Framework Boundary and Refresh](#framework-boundary-and-refresh) | Find scope limits, dependencies, source use, related practices, and refresh conditions. |

**Part I - Frame the Change and Compare Organization Concepts**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [OCE.1 - Identify the Changed Organization and Intended Contribution](#oce1---identify-the-changed-organization-and-intended-contribution) | Eternal alpha | *Keywords:* change focus, organization boundary, outside contribution. *Question:* Which organization are we changing, and what contribution should guide the change? | FPF A.1.SCR, A.1.CSD, A.15.6 |
| 2 | [OCE.2 - Recover Current Organization Work and Arrangement](#oce2---recover-current-organization-work-and-arrangement) | Eternal alpha | *Keywords:* current organization, actual Work, formal and informal arrangements. *Question:* How does the organization get work done, and which relations support or obstruct it? | OCE.1; FPF A.22, A.2.1, A.13, A.15.1 |
| 3 | [OCE.3 - Generate and Compare Organization Concepts](#oce3---generate-and-compare-organization-concepts) | Eternal alpha | *Keywords:* organization concepts, alternatives, exploration. *Question:* Which materially different organization concepts are worth comparing? | OCE.1, OCE.2; FPF A.22, C.17, conditional C.18, C.11 |

**Part II - Design Organization Relations and Work Arrangements**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 4 | [OCE.4 - Design Contribution Architecture](#oce4---design-contribution-architecture) | Eternal alpha | *Keywords:* contribution architecture, specialization, boundary crossings. *Question:* How should contributions be distributed and connected across specialization boundaries? | OCE.1-OCE.3; FPF A.22, C.30, C.32.PAD |
| 5 | [OCE.5 - Define Organization Positions](#oce5---define-organization-positions) | Eternal alpha | *Keywords:* institutional position, vacancy, continuity. *Question:* Is a stable organization position needed, and what establishes its identity? | OCE.1; conditional OCE.4; FPF A.2.1, A.6.REL |
| 6 | [OCE.6 - Establish Holder Assignments and Enabling Relations](#oce6---establish-holder-assignments-and-enabling-relations) | Eternal alpha | *Keywords:* assignment, holder, authority, access, responsibility. *Question:* Who is assigned to contribute, with what authority and access, and which enabling relations are missing? | OCE.4; conditional OCE.5; FPF A.2.1, A.2.2, A.6.REL |
| 7 | [OCE.7 - Coordinate Product-or-Service and Organization Architecture Decisions](#oce7---coordinate-product-or-service-and-organization-architecture-decisions) | Eternal alpha | *Keywords:* product and organization architecture, Conway, alignment, mismatch. *Question:* How should the two architecture decisions constrain one another, including an intentional mismatch? | OCE.3, OCE.4; FPF C.30, C.32.CONWAY, C.32.PAD |
| 8 | [OCE.8 - Configure Human–AI, Robotic, and Provider Work Arrangements](#oce8---configure-humanai-robotic-and-provider-work-arrangements) | Eternal alpha | *Keywords:* train, hire, provider, AI, robot, hybrid, whole work arrangement. *Question:* Which complete arrangement enables participants to obtain the same bounded result? | OCE.1-OCE.3; FPF A.15.8, A.2.2, E.23.CDI, C.38, C.11 |

**Part III - Realize Change While Work Continues**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 9 | [OCE.9 - Realize a Bounded Organization-Capability Increment](#oce9---realize-a-bounded-organization-capability-increment) | Eternal alpha | *Keywords:* capability increment, representative work, integration, exception return. *Question:* How can the organization obtain the selected contribution beyond an isolated demonstration? | OCE.4/OCE.8 decision; OCE.6; qualified integration, learning and service results |
| 10 | [OCE.10 - Diagnose Participation and Change Target Working Culture](#oce10---diagnose-participation-and-change-target-working-culture) | Eternal alpha | *Keywords:* participation, resistance, working culture, intervention. *Question:* Why is a needed contribution not occurring, and which intervention addresses the supported cause? | OCE.6; applicable HCD.1/HCD.3/HCD.4 or direct professional results; C.36; conditional C.28 |
| 11 | [OCE.11 - Coordinate Change Work with Continuing Service](#oce11---coordinate-change-work-with-continuing-service) | Eternal alpha | *Keywords:* continuing service, capacity, dual operation, recovery, hand-back. *Question:* How can change work overlap with service without breaching its protected conditions? | ME.6; OPS.5-OPS.7; conditional OCE.8/OCE.16; direct service and protection results |
| 12 | [OCE.12 - Distribute Leadership Contributions in Organization Change](#oce12---distribute-leadership-contributions-in-organization-change) | Eternal alpha | *Keywords:* leadership, briefing, feedback, mutual assistance, continuity. *Question:* Which leadership contribution is missing from the next work episode, and how can it continue? | Qualified leadership and learning Methods; OCE.6; conditional OCE.10/OCE.11; applicable HCD results |

**Part IV - Observe Consequences and Revise the Organization**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 13 | [OCE.13 - Observe and Compare Organization-Change Consequences](#oce13---observe-and-compare-organization-change-consequences) | Eternal alpha | *Keywords:* consequences, observation, comparison, gains, losses, causal limits. *Question:* What changed, for whom, and which comparison can change the next organization decision? | Qualified observation and measurement results; FPF C.16, A.10; C.28 when causal reliance is needed |
| 14 | [OCE.14 - Revise the Organization from Qualified Results](#oce14---revise-the-organization-from-qualified-results) | Eternal alpha | *Keywords:* organization revision, retention, repair, reversal, authority. *Question:* Which relation should change on the strength of the qualified result, under whose authority? | OCE.13 or a current direct result; actual authority; FPF C.11; conditional OCE.3-OCE.12/OCE.16 |

**Part V - Sustain Methods, Cross-Change Coordination, and OCE Practice**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 15 | [OCE.15 - Develop and Refresh Organization-Change Methods](#oce15---develop-and-refresh-organization-change-methods) | Eternal alpha | *Keywords:* Method repertoire, candidate Method, local adaptation, refresh. *Question:* How can we repair a repertoire or construct an OCE candidate Method for the current use? | Method Engineering Principles Framework ME.1-ME.16 as applicable; FPF A.3.1, A.10 |
| 16 | [OCE.16 - Reconcile Simultaneous Organization-Change Work](#oce16---reconcile-simultaneous-organization-change-work) | Eternal alpha | *Keywords:* simultaneous changes, dependency, support retirement, direct return. *Question:* Does another separately managed change still need the condition we propose to alter? | ME.6; applicable OCE, OPS.1-OPS.7, A.15, C.32.MWA, and direct domain results |
| 17 | [OCE.17 - Continue and Renew Organization-Change Engineering Practice](#oce17---continue-and-renew-organization-change-engineering-practice) | Eternal alpha | *Keywords:* OCE practice, practitioner population, continuation, renewal. *Question:* Which practices continue across practitioners, and what makes them easier or harder to use? | FPF C.36; actual OCE cases; OCE.15/Method Engineering for Method repair; applicable HCD and direct conditions |

# Organization Change Engineering Principles Framework Readme


## Practical entries

Use these patterns to decide which organization relation or capability to change and how to obtain the intended contribution. Organization-change practitioners, designers, affected participants and assisting agents can use them for their part of the change; managers act within their change authority.

The framework contains seventeen pattern bodies. The thirteen entries below are selected examples. If none fits, search the Table of Contents and open the relevant pattern. Obtain a needed result from the practice that governs it; if its source or pattern is unavailable, name that gap. Choose by the working question, not by the order of the entries.

### OCE-FOCUS - Bound the organization, recover actual Work, and compare serious concepts

- **Situation:** A request proposes an organization model before participants have agreed which organization to change and what it should contribute. The proposal may be a chart, an AI-first slogan or a favored topology; current Work, authority, resource access, boundary relations and affected Systems still need to be identified.
- **Question:** Which organization and contribution should guide the change, how is work done now, and which materially different concepts deserve comparison?
- **First useful result or honest blocker:** A bounded change focus, an evidence-based account of current Work and relations, or a comparison that keeps proposed concepts distinct from actual arrangements. Otherwise name the missing System identity, Work evidence, relation, authority, participant contribution or specialist result.
- **Start with:** `OCE.1`. Use `OCE.2` when the focus exists but current Work and relations are not grounded. Use `OCE.3` when both can support alternatives.
- **Stop or return:** Stop at the first decision-changing result. Return specialist questions to their owning practices.

### OCE-DESIGN - Find the organization-design question that needs an answer

- **Situation:** A bounded organization concept exists, but a chart, job title, staffing row, RACI, or mirroring slogan still hides which design or effectivity question is current.
- **Question:** Do we need to design future contributions, establish a stable position, make a holder assignment effective, coordinate product-or-service and organization architectures, or compare complete Work arrangements for one result?
- **First useful result or honest blocker:** `OCE.4` returns specifications for future relations and specialization boundaries; `OCE.5`, a position identity or a return to a direct arrangement; `OCE.6`, the holder assignments and enabling relations that actually hold, with unresolved gaps; `OCE.7`, separately governed architecture decisions, including a bounded mismatch; `OCE.8`, a same-result comparison and authorized choice, probe, rejection or return to a missing premise.
- **Start with:** `OCE.4` when crossings and boundaries are undecided; `OCE.5` when vacancy or position continuity changes use; `OCE.6` when you need to establish or check an assignment and its enabling relations; `OCE.7` when structures on both architecture sides constrain the choice; `OCE.8` when several complete ways of obtaining the same result must be compared.
- **Stop or return:** Return from a wrong entry as soon as the governed subject changes. A position is optional, an assignment need not use one, and a paired decision can preserve non-isomorphic structures.

### OCE-ARRANGEMENTS - Compare whole ways to obtain the same result

- **Situation:** The current arrangement is insufficient or uncertain. Proposals such as training, hiring, a provider, platform repair, automation, a robot or a hybrid have not yet been completed around one result.
- **Question:** Under which complete arrangement can participants obtain this bounded contribution through representative Work? Compare the arrangements for the same use, situation, horizon, acceptance basis and protected conditions.
- **First useful result or honest blocker:** A comparable baseline and complete OptionSet plus an authorized choice, discriminating probe, rejection of the current set, or exact reroute to a missing premise, authority, access, safety, provider, or other direct result.
- **Start with:** `OCE.8`. Use `OCE.1` or `OCE.3` first when the result premise or serious concept set is still disputed.
- **Stop or return:** Do not treat a training, staffing, provider, interface, platform, or automation fragment as a whole option. Keep each claim explicit: what is recommended, what was chosen, what was provided, what Work occurred, what capability was demonstrated, and what arrangement was enacted.

### OCE-REALIZE - Make a selected organization contribution work

- **Situation:** A design, appointment or tool exists, but the organization cannot yet obtain the intended contribution through representative work.
- **Question:** Which enabling relations must be established so that the organization can perform the contribution and handle exceptions in representative work?
- **First useful result or honest blocker:** A bounded tested organization-capability increment, or the exact missing condition, failed attempt and next repair.
- **Start with:** OCE.9 from a selected design or duly authorized bounded attempt. Obtain the direct assignment, access, learning, support and service results it needs.
- **Stop or return:** Obtain trial authority before dependent trial work. Assess organization capability through representative work, including exceptions; a recommendation, installed platform or isolated demonstration is insufficient.

### OCE-PARTICIPATE - Match a participation or working-culture intervention to its cause

- **Situation:** A needed contribution is avoided, distorted, late or burdensome despite nominal support for the change.
- **Question:** Which supported cause changes the next action, and what intervention can improve actual participation or recurrent local practice?
- **First useful result or honest blocker:** A cause-sensitive intervention and bounded consequences, or an unresolved rival, professional result or protection gap.
- **Start with:** OCE.10 and one concrete work episode. Obtain the relevant access, authority, workload, learning or other result from its responsible practice.
- **Stop or return:** Do not treat a valid objection as resistance, attendance as capability, or one meeting as changed culture. Use OCE.17 for the continuation of OCE practice among practitioners.

### OCE-COEXIST - Change while continuing service

- **Situation:** Learning, setup, dual operation, observation or recovery compete with current service commitments.
- **Question:** What bounded overlap can preserve the service conditions while the organization changes?
- **First useful result or honest blocker:** An authorized coexistence arrangement, observed consequences and hand-back, or a smaller slice, deferral or exact missing service result.
- **Start with:** OCE.11 and the actual service owner's coverage/recovery conditions. Use ME.6, OCE.8, OCE.16 and OPS only for their specific current questions.
- **Stop or return:** Calendar vacancies are not capacity evidence. Reduce or stop the change when its conditions fail, and obtain missing service or protection results from the responsible practice.

### OCE-LEAD - Obtain and sustain a particular leadership contribution

- **Situation:** Explanation, constructive challenge, help in a role, mutual assistance or learning support is missing or depends on one initiator.
- **Question:** Which concrete leadership Method and qualified contributors can enable the receiving work and its next episode?
- **First useful result or honest blocker:** A performed contribution and tested continuation arrangement, or a precise participation, capability, authority or support gap.
- **Start with:** OCE.12. Use a brief, role conversation, feedback, debrief or other qualified Method matched to the difficulty.
- **Stop or return:** Verify the contribution in the receiving work. Facilitation, coaching, expertise, authority and resource provision may require different people, including non-subordinates.

### OCE-OBSERVE - Compare consequences for the next organization decision

- **Situation:** A change shows a local gain, but its consequences for contribution, coordination, workers, customers or other affected Systems are uncertain or conflicting.
- **Question:** What changed, for whom and under which conditions, and which observation can change the receiving decision?
- **First useful result or honest blocker:** A comparison that states observed gains and losses, rival explanations, conditions of use and missing evidence; or a bounded plan for obtaining the missing observations.
- **Start with:** OCE.13 and the receiving decision. Reuse current observations and obtain the smallest missing measurement or professional result.
- **Stop or return:** Preserve a descriptive comparison without inventing causation. Return an organization-revision question to OCE.14 and an exact missing result to its direct owner.

### OCE-REVISE - Change the relation that a qualified result challenges

- **Situation:** Observations, or changed authority, service, provider or other conditions, invalidate a current organization premise.
- **Question:** Which bounded relation should be retained, repaired, replaced, reversed, stopped or investigated, under whose actual authority?
- **First useful result or honest blocker:** An authorized disposition with its effective scope, losses and remaining work; without authority, a bounded proposal or exact authority request.
- **Start with:** OCE.14 from the qualified result and current relation. OCE.13 is one possible supplier, not a mandatory predecessor.
- **Stop or return:** A decision or revised model is not realized capability. Return assignment, realization, participation, service and observation work only where it remains necessary.

### OCE-METHODS - Repair a repertoire or construct an OCE candidate Method

- **Situation:** Available ways of changing the organization mix stage models, implementation strategies, process models, determinant accounts, evaluation frames, local routines, tools, training, and remembered practice.
- **Question:** Does the current use need a repaired repertoire, a domain-filled candidate Method account, or both?
- **First useful result or honest blocker:** A named-use repertoire, an OCE candidate account ready for Method Engineering qualification, or a blocker naming the missing organization result, situation claim, authority, capability, support, protection, evidence, or ME result.
- **Start with:** `OCE.15`. Use the [qualified Method Engineering dependency](#current-method-engineering-dependency) for Method focus, qualification, trial, fit, worth, variant and introduction decisions.
- **Stop or return:** Keep strategy, process, determinants, evaluation, implementation outcomes, and organization results distinct. Selection or participation alone does not establish adoption, capability, effects or culture.

### OCE-RECONCILE - Find and return one consequential dependency between separately managed changes

- **Situation:** One organization change proposes to alter or retire a contribution, assignment, authority, access path, provider relation, information return, acceptance route, capability condition, or support interval that another separately managed change may still use.
- **Question:** Which other change uses that condition for which exact participant action or decision, during which window, and what current evidence supports or defeats the claimed dependency?
- **First useful result or honest blocker:** A supported cross-change question, the Method and responsible practice best able to resolve it, or the missing fact or result. Stop if the dependency is absent or already answered. After the responsible practice returns its result, give each affected change the result, applicable condition and observation that would reopen it.
- **Start with:** OCE.16. Use ME.6 when Method or candidate-account co-use depends on order, allocation, subject/support, access, authority, evidence, burden, or another selected structure -- even if every Method remains unchanged and the result is relation-only. Use the OCE, OPS, A.15 or C.32.MWA pattern that governs the needed result. For a professional result, return to the relevant Strategy, Governance, Administration, HCD, safety, legal, finance, security, provider, service or other practice.
- **Stop or return:** Stop when no consequential consumer exists or the direct answer and per-change consequences are already recoverable. OCE.16 does not compare joint architectures, select an arrangement, authorize Work, establish compatibility, or create a superior change authority.

### OCE-PRACTICE - Continue and renew operative OCE practice

- **Situation:** An OCE practice spreads, changes or fades across practitioners while its name, carrier or events may tell a different story from actual work.
- **Question:** Which operative move continues, what supports or impedes its continuation, and what bounded response is justified?
- **First useful result or honest blocker:** A scoped continuation account and a permitted retention, intervention or direct return, with later observed use or an exact opportunity/evidence gap.
- **Start with:** OCE.17 and one consequential OCE episode. Compare claimed practice with the action and result a recipient can actually use.
- **Stop or return:** Use OCE.10 for target-organization culture, OCE.15 for a reusable-Method problem and qualified HCD or learning providers for a human-development question. A population is not one capability holder.

### OCE-PUMPWORKS - Compare weekly AI-inspection work arrangements while service continues

- **Situation:** Under its current functional arrangement, PumpWorks produces an evidenced AI-inspection package quarterly but needs the same bounded package weekly. Proposals for another holder, platform repair, provider AI and hybrid review are still fragments. A hypothetical repository-consolidation change would also retire an evidence-return contribution at migration completion while the hybrid-trace change may still need it for challenged packages.
- **Question:** Under which whole Work arrangement can PumpWorks obtain the weekly result while protecting Safety/release authority, provenance, confidentiality, continuing service and recovery? Does repository retirement remove a condition still needed by the arrangement change?
- **First useful result or honest blocker:** The OCE.8 case compares three complete same-result candidates and returns a hybrid probe recommendation with gaps in trial authority, effective provider access and protection/recovery evidence. OCE.16 can qualify the support-retirement dependency and route it to ME.6 and direct relation owners; it makes no second arrangement choice.
- **Start with:** OCE.8 using the current OCE.1–OCE.7 results. Use OCE.16 only when the separate consolidation change introduces the cross-change dependency; ME.6 owns the resulting candidate-account co-use comparison.
- **Stop or return:** The quarterly baseline stays outside the target-result OptionSet. The hybrid remains a recommendation, not a ChoiceResult. Migration completion cannot silently retire another change's premise; return the direct result to both changes. The probe remains pending until its trial authority, access and protection/recovery conditions are supplied.

A separately conditioned continuation in APP-OCE-01 connects OCE.9–OCE.12 after the missing operational inputs are supplied. It preserves the initial reroute and adds realization, participation, service-coexistence and leadership results only within that hypothetical continuation.

A further constructed episode uses OCE.13/OCE.14 to compare consequences and revise one support relation. APP-OCE-04 separately follows OCE practice among practitioners; it is not another claim about PumpWorks' employee culture.

## Citation

If you use this framework, please cite:

```text
Levenchuk, Anatoly. Organization Change Engineering Principles Framework.
3 September 2026.
GitHub repository: https://github.com/ailev/FPF
```

For a particular pattern, add its PatternID and title, for example: Organization Change Engineering Principles Framework, OCE.1 - Identify the Changed Organization and Intended Contribution. Retain the release date, and include a permanent link or stored copy when the exact wording matters.

# Preface


Use Organization Change Engineering when the decision is how to change an organization's relations or capability to make an intended contribution. For other management decisions, use their responsible practices.

Start outside-in with the contribution needed or the condition to preserve. Recover how the organization gets work done and the relations that make that possible, including effects on continuing service and other Systems. A chart can help locate a question; inspect the organization and Work it depicts.

## Actual, formal, and possible claims remain distinct

Sources differ in what they can establish. Use a chart, policy, position description, process map, interview, Work trace or service record for the bounded claim it supports. Check whether the asserted organization relation actually holds in the relevant situation and time window.

An organization concept describes possible relations; choosing it does not establish them. A WorkPlan describes intended change Work. Support claims about performed Work, changed relations, organization capability, participation, adoption, implementation outcomes, organization results, retention and culture with the evidence each claim needs.

## Several structures and several views can coexist

For the current decision, select the structure and direct relation you need to inspect. Relevant structures may concern contributions, Work, assignments, authority, resource access, information use, material transfer, service provision, coordination, capability, providers or culture. They need not be isomorphic. Do not call every connected arrangement a graph; a mathematical graph is one possible lens after its nodes, edges, relation meanings and intended use are selected.

Project, process, and case views can expose different claims about the same Work. A project viewpoint foregrounds commitments, allocations, and decision slots; a process viewpoint recurring contributions and controls; a case viewpoint changing evidence, exceptions, and next decisions.

## Pattern relations do not prescribe a lifecycle

`OCE.1 → OCE.2 → OCE.3` shows the result dependencies when the change focus, current-organization account and concept alternatives must all be developed. It is not a calendar sequence. A current account can be repaired while a repertoire is refreshed; a known concept can enter downstream design without repeating every earlier result; changed evidence reopens only defeated claims.

Use the smallest pattern whose result can change the decision. Follow a prescribed sequence when the selected Method requires it. The PumpWorks application is a worked example, the Table of Contents gives reading order, and a return to another practice asks for a needed specialist result.

## How the contributions connect

The patterns connect organization design and realization with consequence comparison, revision, Method development and continuation of OCE practice. The [Table of Contents](#table-of-contents) identifies the specific question addressed by each pattern.

Use OCE.13 to assemble decision-relevant observations and compare consequences; causal attribution needs its own support. Use OCE.14 to decide how to revise organization relations within the decision-maker's authority and identify the work still needed. OCE.9–OCE.12 retain the local observation, correction and continuation tests used in realization, participation, service and leadership work.

Use `OCE.10` for a participation or adoption gap in the target organization's working culture, with `OCE.12` for leadership contributions and `C.36` for culture mechanics. Use OCE.17 to follow how OCE Methods are encountered, criticized, selected, enacted, retained or lost among practitioners. Distinguish that practice from its description and carrier, and identify the actual uses within the practitioner population. Treating that population as one System or capability holder requires a separate basis.

Continuing organization development can combine these contributions with Strategy, Operations, Administration, human learning, research and product engineering. A comparison can remain useful when a proposed revision cannot proceed. An authorized revision still needs realization and later observation.


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

### OCE.1:0.1 - Working Distinctions

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

| Source line | Retained contribution | Use boundary |
| --- | --- | --- |
| Current FPF `A.1.SCR`, `A.1.CSD`, `A.15.6`, and `A.10` | System recognition, affected-System discovery, project-relative subject recovery, and evidence use. | Use these results for System, affected-System and evidence questions; select the contribution, Work/capability questions, authority return and continuation for the OCE decision. |
| Fraccaroli, Zaniboni, and Truxillo, [work-design review](https://doi.org/10.1146/annurev-orgpsych-081722-053704) | Work design and affected-person outcomes belong in the initial boundary. | Use the review to frame work-design and affected-person questions; qualify its applicability to the organization being changed. |
| Aust et al., [organizational interventions and occupational health](https://doi.org/10.5271/sjweh.4097) | Worker health, wellbeing, retention, implementation, and conditions remain possible consequences. | Evidence varies by intervention and outcome; assess effectiveness for the intended intervention. |
| Albert, [organization-structure perspectives](https://doi.org/10.1007/s41469-023-00152-y) | Activity arrangement, decision representation, and legal-entity structure answer different questions. | Choose the perspective for the current question and recover the organization boundary and obtaining relations from appropriate evidence. |

Reopen when a recurring first-use case cannot orient change through one organization/contribution focus, or when evidence shows that an omitted System, relation, authority, or consequence class changes action.

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

### OCE.2:0.1 - Working Distinctions

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

1. **Bound the recovery use.** State organization, contribution, decision, horizon, Work families, selected structures, and exclusions.
2. **Collect sources for the needed claims.** These may include charts, position descriptions, policies, decision records, Work products, observations, interviews, provider records and service evidence. State what each can establish.
3. **Recover actual Work and results.** For a relied-on Work claim, recover the performers' `A.13` basis and the `A.15.1` occurrence basis. Keep plans, routine descriptions, schedules and reports distinct from the Work occurrences they describe. When the basis is incomplete, record the supported observations and the missing basis.
4. **Recover supplied-result and boundary relations.** For every relevant path, name supplier and receiver Systems, result or content, direct predicate, conditions, and evidence. Distinguish a contribution supplied, information used, material transferred, decision issued or accepted, service provided, resource accessed, and coordination occurrence.
5. **Recover position-related claims without invention.** A current organization position requires its establishment and continuation basis. Otherwise record only the position description, expected contribution, eligible system-role kinds, holder Systems, and assignments that are separately supported. Use `A.2.1` for obtaining assignments.
6. **Recover authority, responsibility, resources, and access.** Name each direct relation. Record a blocker instead of inferring authority or access from hierarchy, responsibility, budget, or tool presence.
7. **Compare formal and observed claims.** State `agree`, `contradict`, `unknown`, or `changed-window` for each decision-changing pair. Ask what result and consequence the difference has; do not call it dysfunction by default.
8. **Inspect participation and consequences.** Identify whose Work and burden are absent, which affected-System questions remain open, and which sensitive claims require protection or specialist handling.
9. **Stop at the decision boundary.** Return the account, gaps, and constraints when they are enough to generate concepts or expose a blocker. Do not design the target inside the baseline.
10. **Reopen from evidence.** Reopen the smallest Work or relation claim when a new occurrence, source edition, participant account, provider condition, authority decision, or service result defeats it.

#### OCE.2:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| use boundary | Organization, contribution, receiving decision, horizon, selected structures, and exclusions. |
| source evidence | Source or observation, claim kind, scope/window, sensitivity, and evidential limit. |
| actual Work | Supported occurrences, performers and their A.13 basis, enacted Methods, time intervals, conditions, containing Systems, associated results and limits; otherwise the observations and unresolved occurrence claim. |
| supplied results and boundary relations | Participants, direct predicate, result/content/resource, conditions, carrier/support distinction, evidence, and status. |
| position-related claims and assignments | Position establishment/continuation basis when available; otherwise separate description, expected-contribution, eligibility, holder, and assignment facts plus the missing establishment or identity basis. |
| authority, responsibility, resources | Direct relations, subjects, scopes, windows, bases, evidence, and blockers. |
| formal/observed comparison | Matched claims with `agree`, `contradict`, `unknown`, or `changed-window` and the decision consequence. |
| participation/consequences | Missing participants, hidden burden, affected-System questions, protection needs, and specialist returns. |
| return | Grounded account, unresolved gaps, constraints for `OCE.3` or `OCE.11`, stop, and reopen triggers. |

#### OCE.2:4.3 - What Changes in Practice

The organization is no longer represented by one chart. Practitioners can see which Work and relations matter, where formal and observed claims differ, what remains unknown, and which gap must be resolved before a concept or coexistence decision can be trusted.

### OCE.2:5 - Archetypal Grounding -- PumpWorks Current Relations

The `OCE.1` focus selects `PumpWorks-EngineeringOrg` and weekly evidenced AI-inspection releases while service continues. Recovery is limited to release Work, result supply and use, decision authority, provider service, rig access, and field-service information return.

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
- [ ] Sources state scope, window, sensitivity, and evidential limits.
- [ ] Actual Work is separate from plans, routines, process descriptions, and reports.
- [ ] Contribution supply, information use, material transfer, decision, service provision, access, and coordination remain distinct.
- [ ] A position claim has an establishment/continuation basis, or only its separately supported neighboring facts are recorded.
- [ ] Job title, position, system-role kind, holder, assignment, capability, responsibility, participation, and authority remain distinct.
- [ ] Every authority and access relation names its participants, scope, window, basis, and evidence.
- [ ] Formal/observed differences have explicit status and are not judged by mismatch alone.
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

| Source line | Retained contribution | Use boundary |
| --- | --- | --- |
| Current FPF `A.22`, `A.6.REL`, `A.2.1`, `A.13`, `A.15.1`, and `A.10` | Structure selection, relation recovery, assignments, performers, Work, and evidence use. | OCE.2 selects organization-specific questions and direct receiving relations. |
| Albert, [organization-structure perspectives](https://doi.org/10.1007/s41469-023-00152-y) | Activity, decision, and legal-entity structures can all matter and need not coincide. | The perspectives are lenses for recovery, not one complete model. |
| Grote et al., contribution-based engineering role modeling (`SRC-ENGINEERING-ROLE-MODELING-2025`) | Required contributions can expose role bundles more accurately than inherited titles. | Use the role bundles to examine needed contributions. Assignment and transfer beyond the studied cases require their own basis. |
| Fraccaroli, Zaniboni, and Truxillo, [work-design review](https://doi.org/10.1146/annurev-orgpsych-081722-053704) | Actual Work characteristics and affected-person outcomes belong in the baseline. | Use direct evidence for authority and capability claims, and a separate decision for the target organization. |

Reopen when representative use exposes a decision-changing relation the result cannot preserve, or when a stronger source changes how formal and observed claims should be compared.

### OCE.2:12 - Relations

- `OCE.1` supplies organization, contribution, Work/capability questions, affected-System gaps, authority boundary, and horizon.
- `A.22` governs selected structure identity; direct relation patterns govern supplied-result, assignment, authority, access, information-use, transfer, service, and coordination claims.
- Use `A.13` for the performer basis, then `A.15.1` for actual Work; use `A.2.1` for assignments. Support each claim needed by the receiving decision.
- `OCE.5` governs organization-position identity and descriptions; `OCE.6` governs holder assignments and enabling relations. Until their needed result is available, record the missing position-establishment or identity basis rather than inferring a position.
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

Do not use OCE.3 to make a concept obtain, establish a position, assign holders, establish capability, authorize change Work, or prove adoption or effectiveness. Send selected design questions to `OCE.4`–`OCE.8` and realization to `OCE.9`.

### OCE.3:0.1 - Working Distinctions

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
2. **State comparison dimensions before forms.** Name the supplied-result, Work, specialization, eligibility, assignment, authority, access, information-use, service and coordination relations that can change the decision. Keep differences in product/service architecture, human–AI or provider arrangements, capability, coexistence conditions and burden explicit.
3. **Choose bounded participants.** Invite or otherwise obtain contributions from participants whose knowledge of actual Work, burden, local adaptation, authority, safety, service or providers can alter the candidate set or comparison. Record missing participation and protection limits; preserve decision authority separately.
4. **Generate materially different alternatives.** Include incumbent-plus-repair; a changed specialization, contribution, or authority configuration; and a boundary/provider or human–AI alternative when plausible. Each alternative must change at least one named decision-bearing relation. Stop when another variant changes no live assumption or criterion, or record the unmet generation need.
5. **Decide whether retained exploration is current.** For a one-time small decision set, proceed without Archive/Front apparatus. Use `C.18` only for retained or open-ended exploration; use `C.17` only to characterize candidates already present.
6. **Describe selected structures.** Name possible constituents and relations. Use charts, maps, scenarios, prototypes, or mathematical lenses only for declared questions and state their losses.
7. **Expose feasibility assumptions.** State required capabilities, authority, resource access, provider commitments, product/service claims, participation conditions, and continuing-service constraints.
8. **Compare contributions and burdens.** Compare intended contribution, coordination, resilience, affected-System consequences, participant burden, service interruption, reversibility, and uncertainty.
9. **Choose, narrow, probe, or stop.** Select under named authority, retain ties, or request the specialist result that changes the comparison. Selection does not establish organization relations.
10. **Return constraints and reopen evidence.** Supply the selected questions and assumptions to downstream patterns and name observations that reopen them.

#### OCE.3:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| comparison boundary | Organization, contribution, decision, authority, horizon, non-negotiables, and tolerated/blocked gaps. |
| generation account | Domain generation branches used, relation changed by each alternative, stop rule, discarded decorative variants, and any conditional `C.18` use. |
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

| Concept | Possible relation changes | Main promise | Main burden and uncertainty |
| --- | --- | --- | --- |
| `OC-PW-FUNCTIONAL-REPAIR` | Retain functional assignments; establish named electrical-evidence supply and use, safety acceptance, release decision, rig-access priority, and field-service information-return relations | Preserves specialist depth, current authority, and low migration burden | Coordination load may remain high; weekly recurrence is unproved |
| `OC-PW-STREAM-ENABLING` | Create a stream-aligned release configuration with explicit Safety and platform contributions while retaining functional capability homes | Shortens some evidence and decision paths | Requires new assignments, authority, access, and capability; scarce specialists may be overloaded |
| `OC-PW-PROVIDER-HYBRID` | Expand provider model-operation and evidence-preparation contributions while PumpWorks retains safety, release, exception, recovery, and service decisions | May increase specialist capacity | Commitment, access, assurance, recovery, knowledge retention, and authority remain unresolved |

A chart view can show possible position descriptions; a process view recurring release contributions; a case view one release’s evidence and next decision; and a project view transition commitments and conflicts. These are views of possible or actual Work and relations, not four concepts.

The small set needs no Archive or Front. `C.17` may characterize diversity or novelty after the three concepts exist. If later exploration retains many variants and lineage across decisions, that new use can invoke `C.18`.

If the authorized decision-maker must decide before provider and capacity evidence arrives, the honest result is a narrowed choice between functional repair and stream/enabling plus named probes. Selection supplies design constraints; it does not make a configuration obtain.

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
- [ ] The set contains materially different relations and an incumbent-repair branch.
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

| Source line | Retained contribution | Use boundary |
| --- | --- | --- |
| Current FPF `A.22`, `C.17`, `C.18`, `C.11`, `C.30`, and `C.32.CONWAY` | Selected structures; characterization of existing candidates; conditional open-ended exploration; bounded choice; architecture and mirroring distinctions. | Use these patterns for their stated questions; generate the organization-specific alternatives and participant/burden comparison here. |
| Conway (1968) and Colfer & Baldwin (2016) | Communication and product structures can constrain one another; mirroring has exceptions. | Test the correspondence for the chosen product and organization; allow exceptions and compare alternatives. |
| Skelton and Pais, `Team Topologies` (2019; 2025) | Stream-aligned, enabling, platform, subsystem, and interaction concepts can generate candidates. | The line is software-heavy. Establish authority, capability and effects separately for the local case. |
| Schulze-Meeßen and Hamborg, [participatory work-design representations](https://doi.org/10.1016/j.apergo.2023.104012) | Participant-facing prototypes can improve some recognition and acceptance. | Keep the study's recognition and acceptance results separate from evidence about organization relations and participants' contributions. |
| Heusinkveld and Smits, [organization-design knowledge perspectives](https://doi.org/10.1007/s41469-024-00176-y) | Design ideas should be examined through plural development and translation perspectives. | Use the perspectives to examine design knowledge, then make the local concept decision under the applicable authority. |

Reopen when a recurring concept family cannot be generated by these branches, a representation hides a decision-bearing relation, or actual realization defeats the comparison dimensions.

### OCE.3:12 - Relations

- `OCE.1` supplies organization, contribution, authority boundary, and affected-System scope. `OCE.2` supplies actual Work, direct relation evidence, and gaps.
- OCE.3 supplies bounded organization-concept generation. `C.17` characterizes candidates already present; `C.18` governs retained/open-ended exploration only when current; `C.11` governs bounded choice.
- `A.22` governs selected structures; `C.30` and `C.32.CONWAY` govern architecture and mirroring claims.
- `OCE.4`, `OCE.5`, `OCE.7`, and `OCE.8` consume selected constraints for specialization, positions, product/service alignment, and human–AI/provider configurations. `OCE.11` consumes current and possible relations for coexistence.
- Use `OCE.9` to realize the selected concept; identify performed Work and changed organization relations from their evidence.

### OCE.3:End

# Part II - Design Organization Relations and Work Arrangements

## OCE.4 - Design Contribution Architecture

> **Type:** Method pattern
> **Status:** Eternal alpha
>
> **Primary working result:** an **inspectable contribution-architecture design**: a decision and possible-future description recording selected specialization boundaries, contribution-relation specifications, acceptance and exception conditions, affected burdens, receiving decisions, and the evidence needed to establish which direct relations later obtain.

### OCE.4:0 - Use This When

Use this pattern when an organization concept has been selected or narrowed, but its chart, topology, or operating-model label still does not say how contributions reach their receivers. Enter when specialization boundaries, supplied results, information use, decisions, services, resource access, or coordination must be designed before positions or assignments can be settled.

Begin with a compatible `OCE.1` focus, `OCE.2` current account, and `OCE.3` concept comparison or equivalent content. Name any tolerated evidence gap and any gap that blocks design.

The first useful result is small: one organization concept, a few decision-bearing contribution-relation specifications, their intended suppliers and receivers, the selected specialization boundaries, and the conditions under which later Work may realize or reopen them.

Use `C.30` directly when the question is only whether one actual or candidate structure is architecture-relevant. Use `OCE.5` for position identity, `OCE.6` for holder assignments and enabling relations, `OCE.7` for paired product-or-service and organization architecture decisions, and `OCE.9` for realization and organization-capability evidence.

### OCE.4:0.1 - Working Distinctions

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

#### OCE.4:4.0 - One bounded first design

For a small first use, keep the selected concept and already qualified constraints fixed and resolve one troublesome contribution crossing. Suppose a small engineering organization has the authority and participant inputs needed to decide how compatibility evidence reaches its release integrator. A short design note can state:

> Electrical supplies a configuration-C7 compatibility-evidence package to Integration for Friday's review. Each claimed interface must have a traceable source and test; Integration returns an unsupported claim to Electrical before evidence closure. The design decision keeps electrical expertise with Electrical and package assembly with Integration, using the agreed review time rather than merging the two specializations. Safety acceptance and release remain separate decisions. A missing source or an unworkable review burden reopens this design. Use the first package to test whether the planned supply and exception return actually work.

This is one bounded design result, not evidence that the supply relation already obtains. Reuse the supporting focus, current account, participant correction and decision basis instead of restating them. Add another structure, alternative or specialist return when it can change this decision; a missing authority or protection premise remains a blocker. The same short note can carry the needed content listed below. Elaborate the questions that remain open rather than turning this first use into a full-organization redesign.

#### OCE.4:4.1 - Pattern-Use Unfolding

1. **Bind the design question.** Name the organization, intended outside contribution, selected concept, decision subject, authority, horizon, affected Systems, and first receiving use of the result.
2. **Recover the current relation basis.** Carry forward current Work and direct-relation evidence from `OCE.2`, plus constraints, participants, assumptions, and burdens from `OCE.3`. Record unavailable or incompatible inputs explicitly.
3. **Select structures by question.** Choose contribution, Work, decision, information-use, material-transfer, service, access, coordination, legal-entity, or other structures only when each changes the design. Use process, project, and case viewpoints on the same Work to expose different Method, coordination, state, and authority constraints. Retain the account of obtaining occurrences unless new evidence warrants revision; keep proposed structures and crossings modal. Preserve differences among the selected structures when those differences matter to the decision.
4. **Set specialization boundaries.** Group contribution or Work where shared knowledge, equipment, evidence, decision, locality, customer, product, service, or provider conditions justify it. State the condition and the burden moved by each boundary.
5. **Write contribution-relation specifications.** For every decision-bearing crossing, name the intended direct relation kind or predicate, supplier and receiver Systems, result or preserved condition, applicability, acceptance or use condition, exception return, scope, horizon, and evidence need. Use “interface” only as an orientation label after this content is visible. Do not report an occurrence before its predicate is satisfied.
6. **Obtain participant corrections.** Use participant-facing views to test actual Work, burden, accessibility, safety, provider, and service-continuity assumptions. Record whose contribution changed the design and which material voice is missing.
7. **Compare whole structures.** Compare how each candidate handles intended contribution, coordination load, decision latency, evidence, scarce capability, resilience, provider dependence, affected Systems, reversibility, and change burden. Keep unlike characteristics separate unless a justified aggregation Method exists.
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

| Comparison position | Selected result for practice |
| --- | --- |
| Current question | Which organization structures and possible-future direct-relation specifications should guide one contribution decision? |
| Selected current line | Treat organization design as several complementary questions—configuration, control, channelization, and coordination—then select only the structures that change this contribution decision. Bind proposed crossings to contribution and receiving use, and keep participant corrections and later occurrence evidence visible. |
| Serious alternative | Start from one chart, topology, operating-model template, or activity grouping and infer interfaces from adjacency. |
| When the alternative is sufficient | A single representation is enough for orientation when it makes no claim to settle direct relations, authority, acceptance, or realization and the underlying occurrences are already established elsewhere. |
| When the selected line changes action | If the representation cannot name the supplied result, receiver, acceptance or use, exception return, or an unlike structure that changes the decision, write relation specifications and compare the necessary structures before fixing boxes. |
| Reopen | Reconsider the selection when a representative contribution cannot be expressed, a serious alternative reaches the same decision with less modeling burden, or a current source changes the organization-design action. |

#### OCE.4:11.2 - Source Contributions and Boundaries

| Source line | Retained contribution | Use boundary |
| --- | --- | --- |
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
- `OCE.9` consumes design constraints and later returns realization evidence. `OCE.12` may consume contribution architecture for leadership-contribution distribution.
- Strategy, Corporate Governance, Operations, Administration, Systems Engineering, finance, legal, labor, safety, privacy, and other specialists supply only their available compatible results or qualified direct sources.

### OCE.4:End

## OCE.5 - Define Organization Positions

> **Type:** Method pattern
> **Status:** Eternal alpha
>
> **Primary working result:** **organization-position descriptions and establishment or continuation decisions** that name the owning organization, effective establishment basis, identity-bearing expected contributions and assignment-eligibility criteria, continuation conditions, and evidence needs without asserting a holder or performed Work.

### OCE.5:0 - Use This When

Use this pattern when an organization needs a stable institutional position for expected contributions, but a title, job description, team label, or current holder is being used as the position itself. Enter when vacancy, holder replacement, eligibility, establishment, abolition, or continuation changes the decision.

Begin with a bounded organization and contribution need. A compatible `OCE.4` result is useful when the position follows from a new contribution architecture; an existing law, charter, bylaw, appointment scheme, or organization decision may instead supply the basis for a current position.

The first useful result names one owning organization, one position identity, its establishment and continuation basis, the expected contributions that distinguish it, the eligible system-role kinds, and a description usable by `OCE.6`. A vacant position is a complete result when no holder decision is current.

Use `A.2.1` directly when only a holder assignment is needed and no organization-position identity changes the use. Use `OCE.6` to establish assignments, authority, responsibility, resource, or access relations. Use Human Capability Development for developing a person's capability and applicable labor, legal, governance, compensation, privacy, or safety practice for their own decisions.

### OCE.5:0.1 - Working Distinctions

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

#### OCE.5:4.0 - One first position description

Suppose a standards association's effective bylaw 8 already establishes an editorial-chair position, its expected contribution and its eligible local role kind. An organizer preparing an appointment can begin with one short description:

> The association's EditorialChair position is established by bylaw 8 and is currently vacant. It remains the same position while that basis and its identity-bearing criteria remain in force. It expects amendment-packet preparation and the return of unsupported evidence to contributors. The association's defined MemberEditorSystemRole kind is eligible for assignment. Return publication access as an enabling need for the separate appointment decision. Holder selection, authority, and effective access remain to be established.

Return that description and its bylaw basis to the person arranging the assignment. The appointment, candidate's capability and effective access remain OCE.6 or direct-owner questions. If the establishment or continuation basis is missing, return a proposed description or unresolved position claim instead.

The fuller questions below become useful when the position's identity, eligibility, contribution or institutional basis is unresolved or must change. Reuse current answers and add only the neighboring requirements that change this position or the next assignment; no separate form is required.

#### OCE.5:4.1 - Pattern-Use Unfolding

1. **Bind the position question.** Name the owning organization, intended contribution, current design or operating need, decision subject, authority, horizon, and first receiver of the position description.
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

The `OCE.4` design requires stable coordination of electrical compatibility evidence, platform test results, provider model artifacts, unresolved assumptions, and the evidence package used by Safety. PumpWorks decides that this expected contribution should persist beyond one release or holder.

`PumpWorks-EngineeringOrg` is the owning organization. Authorized organization decision `PW-OD-2026-04` establishes `PW-ReleaseEvidenceIntegrationPosition` from 2026-10-01 while the decision remains effective. The identity-bearing expected contribution is to maintain the traceable release-evidence assembly and return unresolved mismatches to the participants supplying the underlying evidence. The eligible local system-role kinds are `SystemsIntegrationEngineerSystemRole` and `ReleaseEvidenceCoordinatorSystemRole` under the current PumpWorks role-kind scheme.

The position description names coordination and evidence-return expectations; safety-evidence acceptance and release authority remain with their separate decision-makers. The description records test-environment and provider-artifact access as enabling needs for `OCE.6`. The position is initially vacant.

| Change | Position disposition |
| --- | --- |
| a holder is assigned on 2026-10-01 | Same position; `OCE.6` governs the assignment occurrence |
| holder leaves and the position becomes vacant | Same position while `PW-OD-2026-04` and identity-bearing criteria remain in force |
| title changes to “Release Evidence Coordinator” | Same position if the designation changes and the identity-bearing criteria do not |
| description clarifies a reporting view | Same position; the description episteme changes |
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

| Comparison position | Selected result for practice |
| --- | --- |
| Current question | Does this recurring expected contribution need a stable organization-dependent position, or can direct assignments, tasks, projects, or other arrangements carry it? |
| Selected current line | Establish or preserve a position only when vacancy, holder replacement, continuation, institutional force, and identity-bearing expected contribution or eligibility change the decision. Otherwise keep the contribution and direct assignments without inflating a durable position. |
| Serious alternative | Treat the job title, job description, chart box, role taxonomy, or fully deconstructed task/project market as the default organization design. |
| When the alternative is sufficient | A direct task, project, or assignment is sufficient when no stable institutional locus must persist across holders and no establishment or continuation claim is needed. |
| When the selected line changes action | If the organization must recognize vacancy, continuation, abolition, eligibility, or the same contribution locus across holder changes, recover the owning organization and establishment predicate, then define identity-bearing criteria. |
| Reopen | Reconsider when unlike institutional settings defeat the identity test, current work-design evidence changes the position versus direct-assignment choice, or the institutional locus must persist outside any one owning organization. |

#### OCE.5:11.2 - Source Contributions and Boundaries

| Source line | Retained contribution | Use boundary |
| --- | --- | --- |
| Current FPF `A.2.1`, `A.2.2`, `A.6.REL`, `A.10`, `A.13`, and `A.15.1` | Role-kind classification, assignment, capability, relation obtaining, evidence, performer, and Work remain separately governed. | FPF does not currently define the organization-dependent institutional position. |
| [R5/R10](#guide-source-keys) contribution-position synthesis | Position can persist across holders, carry several expected contributions, remain vacant, and depend on organization establishment. | Use the owning organization’s actual establishment and continuation basis to determine which local position is in force. |
| Rogiers and Collings, [job-deconstruction paradoxes](https://doi.org/10.5465/amp.2022.0236) | Task- and project-based alternatives can add adaptability, while deconstructing jobs creates persistent human and organization paradoxes rather than a universal replacement for positions. | Make the local position-versus-direct-arrangement choice using the organization’s contribution and institutional conditions. |
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

## OCE.6 - Establish Holder Assignments and Enabling Relations

> **Type:** Method pattern
> **Status:** Eternal alpha
>
> **Primary working result:** the **obtaining holder assignments and enabling relations** needed for a bounded organization contribution, together with their predicates, participants, authority, effectivity, evidence, unresolved gaps, and any possible-future specifications that have not yet taken effect.

### OCE.6:0 - Use This When

Use this pattern when a contribution architecture or position design names who must contribute, yet the actual holder assignment, authority, responsibility, resource, access, permission, or other enabling relation is unclear or not effective. Enter when a staffing decision, appointment letter, budget, licence, roster, or tool account is being treated as proof that the complete arrangement now obtains.

Begin with a bounded contribution need and candidate holder Systems. Use an `OCE.5` position when the assignment depends on one; otherwise begin from the direct contribution and the exact local system-role kind. Recover the authority under which each change can be made.

The first useful result can be partial: one effective assignment, its exact species and interval, separately effective enabling relations, and a visible list of pending, contradicted, expired, or missing relations. A truthful blocker is useful when authority or a direct predicate is absent.

Use `A.2.1` directly when the assignment species and occurrence are already known and no OCE coordination changes the result. Use Administration for participant records, provisioning, or service cases; Human Capability Development for developing a holder's capability; Corporate Governance, legal, labor, safety, security, finance, or another specialist practice for their decisions and predicates; and `OCE.9` for organization-capability realization.

### OCE.6:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| candidate holder | An actual `U.System` being considered for an assignment. Assess classification, eligibility, capability, consent, and assignment under the criteria applicable to the proposed contribution. |
| assignment specification | Possible-future content naming a proposed direct assignment species, participants, applicability, intended interval, and conditions. |
| assignment decision | A separately governed decision to establish, change, suspend, or end an assignment. It creates an occurrence only when the admitted species predicate gives that decision constitutive effect and every condition is satisfied. |
| assignment occurrence | One obtaining occurrence of a directly declared species under `U.SystemRoleAssignment`, with holder, exact local system-role kind, every real additional participant, predicate, applicability, and uninterrupted interval recoverable. |
| position-sensitive assignment | An assignment species whose direct predicate requires an actual `OCE.5` organization position as a participant. The position is included only because it changes predicate or identity. |
| enabling relation | Readable OCE wording for one separately admitted authority, responsibility, permission, resource-allocation, access, membership, commitment, or other relation needed for the contribution. It is not a new root relation family. |
| capability evidence | Evidence bearing on a holder-dependent `A.2.2` capability instance. Assignment, title, position, training, resource, or tool presence does not replace it. |
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

For a small first use, take one contribution with a current, reusable assignment result and resolve the enabling gap that changes its next Work. In the PumpWorks case below, verify the appointment's continued effectivity and obtain the repository-access owner's current result. The practitioner can return this short account to the person arranging the integration:

> E27's release-integration appointment is effective from 2026-10-01 under PW-APPT-2026-17 and the declared PumpWorks appointment species. Its participants and uninterrupted interval are recoverable from that result. Provider-repository access is decided but not effective because identity federation is unfinished. Administration/security owns the access return. Provider-artifact integration remains blocked. The appointment still obtains; effective access and capability for provider-tool use require separate evidence.

Keep the existing assignment, authority and capability evidence with this account rather than reproducing it. When the access owner returns effective access, reassess the dependent Work; any other required but missing relation or capability remains a blocker. The fuller questions below are for new, unresolved or changed claims. This first use does not require re-declaring a current assignment species or surveying every possible enabling relation.

#### OCE.6:4.1 - Pattern-Use Unfolding

1. **Bind the contribution and use.** Name the organization, contribution, position when current, receiving decision or Work, scope, horizon, effectivity need, affected Systems, and first consumer of the result.
2. **Recover authority and participation conditions.** Identify who may establish or end each assignment and enabling relation, under which predicate, basis, scope, and interval. Obtain consent, labor, election, membership, or protection results when their owners require them.
3. **Identify candidate holder Systems.** Recover each actual System, exact local system-role-kind classification when needed, relevant capability evidence, availability, conflicts, and current assignments. Keep preference and development needs separate.
4. **Select or declare the direct assignment species.** Reuse an applicable species under `A.2.1`; declare one only when the needed species is missing. Recover the holder slot, exact local assigned-kind domain, every real additional participant, predicate, applicability, and occurrence-identity law. Add an `OCE.5` position participant only when the species truly depends on it.
5. **Specify the proposed assignment.** State candidate holder, assigned kind, position or locus when required, intended interval, conditions, conflicts, and basis. Preserve possible-future status.
6. **Make or obtain the assignment decision.** Use the applicable decision and authority. Determine whether and when the direct species predicate becomes satisfied; a document or record is constitutive only when that predicate says so.
7. **Establish neighboring enabling relations.** For each required authority, responsibility, permission, resource, access, membership, commitment, compensation, provider, or equipment relation, obtain the direct owner's result and satisfy its predicate. Return `missing-governor` rather than inventing a general relation.
8. **Verify effectivity and contradiction.** Observe or otherwise ground the relation occurrence, participants, interval, basis, and currentness. Classify each claim as proposed, decided-not-effective, effective, contradicted, expired, suspended, or missing.
9. **Check capability separately.** Use `A.2.2` for the holder's ability under the required Work envelope. State whether a capability result supports current use, requires development, or remains unavailable. Assignment remains usable as a relation claim even when capability fit fails.
10. **Coordinate records and provision.** Use Administration for participant state, access cases, provisioning, reconciliation, and records when available. A record supports retrieval and evidence; the direct relation remains the result consumed here.
11. **Return precise downstream results.** Supply effective assignments and enabling relations to `OCE.9`; send the authorized holder/resource-assignment result to `ADM.2` under `XRI-07`; send gaps to the exact owner whose action can change them.
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
| “The employee completed training, therefore can perform.” | Use HCD evidence and `A.2.2` to establish the bounded capability instance and fit; training completion remains a separate result. |
| “The assignment ended because the record is stale.” | Distinguish missing current evidence from demonstrated predicate failure; record the occurrence as ended only when its direct identity law supports that conclusion. |

### OCE.6:9 - Consequences

Assignments and enabling relations become usable by later Work, Administration, and capability realization without being bundled. Expiration, suspension, partial provision, and missing authority can be handled locally.

The cost is coordination across owners. Legal authority, security permission, labor consent, finance allocation, and specialist capability require the relevant owners’ actions and evidence; the coordinated design must make those dependencies visible.

### OCE.6:10 - Rationale

An assignment answers who holds which local system-role kind under one direct species. Organization contribution often needs more: authority to decide, responsibility to respond, access to resources, provider commitments, and capability under current conditions. These requirements matter together, but each calls for its own claim and evidence.

Separating specification, decision, and effectivity also gives the practitioner an honest path from design to actuality. A partial result can guide the next action without claiming that the complete arrangement exists.

### OCE.6:11 - SoTA-Echoing

#### OCE.6:11.1 - Current-Line Selection for Assignment and Enabling Relations

| Comparison position | Selected result for practice |
| --- | --- |
| Current question | Which holder assignment and enabling relations actually support the bounded contribution now? |
| Selected current line | Begin from the contribution and interdependent Work, select or declare the exact assignment species, and verify assignment, authority, responsibility, permission, resource, access, provider, and capability claims through their separate predicates and current intervals. Return partial and missing states rather than a completed staffing row. |
| Serious alternative | Use a roster, RACI, appointment letter, function-allocation table, budget, or provisioned account as the complete readiness result. |
| When the alternative is sufficient | Such an artifact is sufficient as a retrieval view when every relied-on direct relation is already established, current, and recoverable from its owner. |
| When the selected line changes action | If Work entry depends on another owner, predicate, effectivity window, or evidence for consent, access, authority, resources, provider support, or capability, verify the affected claim separately and return its exact gap. |
| Reopen | Reconsider when actual use exposes a recurring relation state the result cannot express, a direct source changes the holder/enabling action, or a needed relation has no applicable definition. |

#### OCE.6:11.2 - Source Contributions and Boundaries

| Source line | Retained contribution | Use boundary |
| --- | --- | --- |
| Current FPF `A.2.1`, `A.2.2`, `A.6.REL`, `A.13`, `A.15.1`, `F.6`, and `A.10` | Direct assignment species, holder capability, relation obtaining, performer, Work, assignment-bound attribution, and evidence remain separate. | Obtain responsibility, authority, resource, and access predicates from their owning domains; select a coordination Method for the organization’s contribution. |
| Joseph and Sengul, [current organization-design review](https://doi.org/10.1177/01492063241271242) | Configuration, control, channelization, and coordination expose different organization-design features and consequences. | Use these design features to find the local assignments and enabling relations that need current evidence. |
| Grote et al., [contribution-based engineering role modeling](https://doi.org/10.1109/ISSE65546.2025.11370103) | Required contributions and stakeholder evidence can expose candidate holder/role bundles and gaps. | Use the bundles as candidate input; establish assignments and positions, recover authority, and assess capability separately. |
| Fraccaroli, Zaniboni, and Truxillo, [work-design review](https://doi.org/10.1146/annurev-orgpsych-081722-053704) | Technology, algorithmic management, diverse work arrangements, and affected-person outcomes change holder and enabling conditions. | Recover assignment identity and authority and access predicates from the applicable local rules. |
| Waterson et al., [function allocation for responsible AI](https://publications.ergonomics.org.uk/uploads/Function-Allocation-for-Responsible-Artificial-Intelligence-How-do-we-allocate-trust-and-responsibility.pdf) | Allocation should expose interdependence, joint operation, decision points, responsibility points, outcomes, authority, and dynamic trust. | The evidence comes from an early framework and small experiments. Test its fit for the local human–AI arrangement; qualify responsibility allocation and authority transfer under their own rules. |

Reopen when a recurring assignment species or enabling relation lacks an applicable definition, when a stronger direct source changes the holder/enabling action, or when actual use shows that the partial-result states cannot guide Work entry.

### OCE.6:12 - Relations

- `OCE.4` supplies contribution and enabling needs. `OCE.5` supplies position identity, eligibility, expected contributions, and effectivity when a position-sensitive assignment is current.
- `A.2.1` governs assignment species and occurrences. `A.2.2` governs capability. `A.13` and `A.15.1` govern performer and Work; `F.6` applies only when precise assignment-bound attribution is needed.
- `OCE.9` consumes effective assignments and enabling relations for realization and organization-capability evidence. `ADM.2` may consume the authorized holder/resource-assignment result under `XRI-07`.
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

### OCE.7:0.1 - Working Distinctions

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

#### OCE.7:4.0 - One first paired decision

An instrument maker's engineering organization and inspection product form one bounded pair: two contribution groups serve two product modules that share a test setup. For the next two releases, reuse their current architecture accounts, participant corrections and qualified test, safety and service constraints. The proposed coordination pressure stays in a synthesis frame unless its direct influence relation is established.

The two authorized decision-makers can work from one short paired note:

> The organization-only candidate would merge the groups and disrupt an existing specialist-service commitment. The product-only and joint candidates require redesign that cannot fit the two-release window under the current engineering assessment. We therefore choose a bounded mismatch. The product decision retains the module and test boundaries. The organization decision retains the two groups and specifies one integration contribution and exception return per release. The gain is low migration burden; the accepted cost is shared-test coordination and no claim of independent release by each group. Reopen both decisions if the shared-test burden defeats the protected service commitment, or when the two-release window ends.

Each decision-maker records the decision for their own subject and authority. Send the needed assignment, access, test-time and service-protection requests to their owners for action before the dependent releases. Keep the existing evidence with the note. Use the fuller questions below for an unresolved claim or consequence that could change the pair, rather than rebuilding settled architecture accounts.

#### OCE.7:4.1 - Pattern-Use Unfolding

1. **Bind the paired question.** Name the intended contribution, organization holon, product-or-service holon, decision subjects, authorities, current Work, horizon, evolution window, protected characteristics, and first users of both decisions.
2. **Recover both architecture sides.** Separate actual `ArchitectureRelation` occurrences from candidate, required, desired, or expected `ArchitectureClaim` content. Name each selected structure, description source, currentness, and known loss.
3. **Recover each directional pressure relation.** State which side supplies the influence source and which side contains the changed architecture referent for this candidate; the direction can reverse between pressures. State how a communication, Work, test, deployment, approval, evidence, provider, capability-home, legal, service, or other source structure constrains the transformed-side candidate. Use the applicable direct predicate or keep a `C.32.CONWAY` frame with a missing governor. A reciprocal claim requires its own reversed frame or relation occurrence.
4. **Select decision characteristics.** Name the few characteristics and burdens that can reverse the choice. Ask about the intended contribution, coordination, latency, changeability, safety, evidence, resilience, provider dependence, capability and service continuity, migration, effects on affected Systems, or another exact concern.
5. **Prepare all four candidate forms.** Change the organization side while retaining product/service content; change the product/service side while retaining organization content; change both; or keep a bounded mismatch with explicit cost and return. A form can be rejected quickly when a non-negotiable condition fails.
6. **Obtain qualified domain inputs.** Use available `SYSE.1`, `SYSE.2`, and `SYSE.9` results for engineering focus, linked use/System concepts, and professional contributions when compatible. Use qualified direct sources or return the missing result when a sibling body is unavailable.
7. **Compare whole consequences.** Include current and transition Work, provider and platform arrangements, independent authority, evidence paths, scarce capability, legal and service boundaries, affected Systems, reversibility, and the burden of preserving deliberate non-isomorphism.
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

PumpWorks selects the joint candidate for a bounded release family. The product architecture decision selects the alignment of module/evidence-package boundaries. The organization decision selects stream contribution boundaries and identifies the release-evidence integration need. Safety acceptance remains independent, platform and scarce capability homes remain shared, and provider support does not mirror a product module.

The two decisions cite the same assumptions and evolution window but retain separate authorities and realization Work. `OCE.6` supplies assignments and access; product realization remains with Systems Engineering; `OCE.9` later tests organization relations and capability; Operations supplies continuing-release and service observations. A changed safety regime, provider boundary, platform coupling, product family, or observed coordination burden reopens the affected decision pair.

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

| Comparison position | Selected result for practice |
| --- | --- |
| Current question | Which organization-side, product-or-service-side, joint, or bounded-mismatch candidate best serves the contribution across the declared evolution window? |
| Selected current line | Treat architecture correspondence as contingent, directional, and co-evolving. Compare all four candidate forms because value capture, regulation, authority, evidence, search, migration, provider, and capability conditions can make correspondence or deliberate non-correspondence preferable for a bounded use. |
| Serious alternative | Apply universal mirroring or fixed end-to-end ownership from product modularity, a communication pattern, or a team-topology slogan. |
| When the alternative is sufficient | Similar boundaries can be selected when direct local evidence shows that they reduce the decision-bearing burden without defeating protected shared or independent relations. |
| When the selected line changes action | If value, search, regulation, authority, shared platform, independent assurance, provider, or changing interorganization boundaries alter the consequences, retain the unlike structures and compare joint change and bounded mismatch explicitly. |
| Reopen | Reconsider when a recurring case needs another candidate form, current evidence changes the correspondence answer, or observed realization exposes a missed pressure or burden. |

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
| DORA, [loosely coupled teams](https://dora.dev/capabilities/loosely-coupled-teams/) | Team independence, testing, deployment, and coordination load provide practitioner recognition and possible pressure variables. | Use this software-heavy practitioner guidance for recognition, then test local relations and ownership against the broader research and the organization’s conditions. |

Reopen when a recurring organization/product-or-service case needs another decision-changing candidate form, a current source changes the correspondence answer, or observed realization shows that the selected pressure and burden variables miss the actual constraint.

### OCE.7:12 - Relations

- `OCE.3` supplies organization concepts and correspondence assumptions. `OCE.4` supplies the organization-side contribution-architecture design. `OCE.6` can supply effective assignments and enabling relations needed by realization.
- `C.32.CONWAY` supplies correspondence framing and exact rows; `C.32.PAD` supplies project architecture decisions; `C.30` and `A.22` govern architecture content and selected structures.
- Available compatible `SYSE.1`, `SYSE.2`, and `SYSE.9` results may supply engineering focus, linked use/System concepts, and qualified contributions. Systems Engineering retains product architecture and realization.
- `OCE.9` consumes organization design constraints and later returns actual relation/capability evidence. `OCE.11` can coordinate organization-change and continuing-service Work. Operations returns operating observations.
- Governance, Administration, legal, labor, safety, privacy, finance, providers, HCD, and other practices keep their decisions, predicates, evidence, and authority.

### OCE.7:End

<a id="oce-8"></a>

## OCE.8 - Configure Human–AI, Robotic, and Provider Work Arrangements

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

### OCE.8:0.1 - Working Distinctions

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

Hold one result premise stable. Recover the obtaining baseline, generate serious candidates from five arrangement families, and complete only those fragments that can become whole ways of obtaining the same result. Carry participant knowledge and missing voices into the exact candidates, assumptions, protected conditions, comparison positions, or returns they change.

Compare whole candidates rather than labels. Include the best applicable solo configuration whenever a human–AI or human–robotic synergy claim can change the choice. Freeze only complete-enough ways into the C.11 OptionSet, name the DecisionSubject and authority, and apply an explicit ChoiceRule. Choose, authorize a discriminating probe, reject the set, or reroute; do not promote a recommendation into a decision.

Recognition is cheap: a proposed staffing, provider, platform, automation, or hybrid answer that cannot yet be compared as one whole way is enough to enter. Assurance is stronger: a choice needs current authority, a frozen OptionSet and basis, protected-condition results, and enough evidence for the stated rule. Configuration testing additionally needs the exact A.15.8 plan-or-actual-Work input.

#### OCE.8:4.1 - Pattern-Use Unfolding

1. **Test the result premise.** State the governed result, receiving use, situation, horizon, and acceptance basis. Return to OCE.1, OCE.3, or the exact contribution, demand, affordability, product, service, or acceptance owner if one of those is the live decision.
2. **Bind the organization question.** Name the organization, contribution, representative Work family, affected Systems, decision boundary, protected conditions, evidence window, and intended user of the comparison.
3. **Carry decision-bearing participant knowledge.** For each current or missing perspective, state the bounded evidence or proposal and the exact arrangement, assumption, protected condition, OptionSet position, comparison basis, or return it changes. Preserve protection and burden limits. Keep the basis for agreement, a veto, authority, choice, adoption, and participation repair separate from these knowledge contributions.
4. **Recover the obtaining baseline and bottleneck.** Ground actual Work, performers, assignments, capabilities, supports, provider relations, authority, access, interfaces, recovery, and current evidence. Name the exact limiting contribution or relation; do not substitute a chart or tool inventory.
5. **Generate across the five families.** Consider developing a current holder, assigning another internal holder, obtaining a provider contribution, changing a Method/interface/platform/support arrangement, and allocating bounded Work across human, AI, robotic, provider, or hybrid Systems. Also retain the current arrangement and the smallest repair that could make it adequate. Reject a family by a decision-bearing condition, not a stereotype.
6. **Complete candidates around parity.** Give each retained way the same required result, representative Work, use, situation, acceptance basis, scope, horizon, protected conditions, and honest account of any non-equivalence. Mark a baseline or fragment as baseline-only, incomplete, dominated, rejected, or retained for combination until it is whole.
7. **Preserve governed objects and truth status.** Keep performers, supports, capabilities, assignments, provider commitments and provision, participant contributions, authority, decisions, information and asset custody, interfaces, recovery, plans, actual Work, and possible configurations distinct.
8. **Compare whole consequences.** Use only characteristics that can reverse the choice: contribution quality, latency, cost and resource use, coordination, cognitive and physical burden, autonomy, safety, security, privacy, resilience, continuing service, affected-System consequences, reversibility, uncertainty, provider dependence, and capability erosion. Compare the best applicable solo way when a synergy claim is material.
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
| generation account | Families considered, fragments and combinations, value-based rejection reason, and each non-option’s baseline-only, incomplete, dominated, rejected, or retained-for-combination status. |
| whole candidates | Same-result parity, Work/configuration, capability/development, assignment/authority, Method/interface/platform, provider, protected-condition, consequence, recovery/exit, and evidence positions. |
| comparison | Decision-reversing gains, losses, burdens, uncertainties, applicable best-solo comparator, and non-negotiable conditions. |
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
- [ ] The baseline and all five arrangement families were considered, with value-based rejection or non-option status.
- [ ] Only complete-enough whole ways under one parity basis enter the OptionSet.
- [ ] The best applicable solo configuration remains visible when a synergy claim is material.
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

A sociotechnical comparison is stronger than static function allocation because distributed Systems, artifacts, providers, decision points, communication, adaptation, affected-person burden, and recovery can determine whether the arrangement works. A same-result comparison is stronger than a list of interventions because it prevents a complete hybrid from winning against a failing baseline and partial fragments.

Choice remains a separate governed act. Recommendation, provider commitment, configuration testing, provision, performed Work, capability change, participation repair, adoption, and operating-organization capability each need their own truth makers.

### OCE.8:11 - SoTA-Echoing

#### OCE.8:11.1 - Current-Line Selection for Work Arrangements

| Comparison position | Selected result for practice |
| --- | --- |
| Current question | Which complete organization arrangement can obtain this bounded result through representative Work under the same use, situation, horizon, acceptance basis, and protected conditions? |
| Selected current line | Use a Work-first, same-result, sociotechnical, status-preserving, and evidence-returning comparison across current repair, holder development, internal assignment, provider contribution, Method/interface/platform change, and human–AI–robotic/provider configuration. |
| Serious alternative | Allocate functions on a static human-versus-machine scale, choose staffing/procurement/automation separately, or presume hybrid superiority. |
| Defect overcome | Those alternatives hide distributed Work, incomplete candidates, provider and interface burdens, decision and responsibility points, affected participants, the best solo comparator, and recovery or exit. |
| Practical move | Keep one result premise, use decision-bearing participant knowledge, complete whole candidates, freeze one OptionSet, and return an authorized choice or probe, rejection, or exact reroute. Verify enactment later. |
| Trade-off | More inputs and exact returns are required; a fast slogan may become an explicit blocker. In exchange, the decision does not externalize burden or invent authority, capability, provision, or effect. |
| Reopen | Reconsider when a representative case cannot yield decision-usable whole arrangements, another current pattern supplies the move with less burden, a source changes practitioner action, or use defeats the result-premise, authority, provider, recovery, or evidence boundary. |

#### OCE.8:11.2 - Source Contributions, Limits, and Currentness

| Source line | Retained contribution | Use boundary and currentness |
| --- | --- | --- |
| Current FPF A.15.8, A.2.2, E.23.CDI, C.38, and C.11 | Configuration inputs and recovery probes; holder-specific capability and development; same-result comparison; and separately governed choice. | Use these patterns to qualify configuration, comparison, and choice; generate organization-specific candidates here and obtain local authority and realization evidence from their owners. |
| Naikar et al., [distributed and joint human–AI design](https://doi.org/10.1080/00140139.2023.2281898) | Distributed teams, artifacts, networked technologies, communication, adaptation, and self-organization replace a dyadic human-versus-machine frame. | Treat the conceptual synthesis and illustrative application as design input; qualify the local allocation Method and institutional authority separately. |
| Waterson et al., [function allocation for responsible AI](https://publications.ergonomics.org.uk/publications/function-allocation-for-responsible-artificial-intelligence-how-do-we-allocate-trust-and-responsibility) | Interdependence, joint operation, decision and responsibility points, outcomes, authority, dynamic trust, failure, and recovery extend static allocation. | The evidence comes from an early framework and small experiments. Select local responsibility predicates, legal rules, and organization-design Methods for the actual setting. |
| Vaccaro, Almaatouq, and Malone, [human–AI meta-analysis](https://doi.org/10.1038/s41562-024-02024-1) | Human-only, AI-only, and combined comparison remains visible when synergy matters; task type and the best solo alternative can reverse the answer. | The evidence covers heterogeneous experiments through June 2023. Test local comparative performance and obtain authority, safety, and provider conditions separately. |
| NASA, [Objective Function Allocation Method](https://techport.nasa.gov/projects/95457) | Several human, automation, and robotic allocations can be compared through task and performance trade spaces rather than stereotypes. | Qualify transfer from the completed deep-space project to the local organization, provider, authority, and affected-person conditions. |
| Lagomarsino et al., [adaptive task planning and dynamic role allocation](https://doi.org/10.1146/annurev-control-022624-013624) | Communication, skill transfer, adaptive planning, control, feedback, and reallocation matter when robotic roles change during Work. | Robotics algorithms, safety thresholds, and execution-time control remain with direct engineering and Operations Methods. |
| ISO [6385:2016](https://www.iso.org/standard/63785.html) and ISO [10218-1/-2:2025](https://www.iso.org/committee/5915511/x/catalogue/) | Human, social, technical, equipment, workspace, environment, skill, well-being, lifecycle, and current industrial-robot safety conditions belong in applicable comparisons. | Check which edition and requirements apply to the arrangement. Use the relevant requirements in the comparison, then qualify performers, capability, authority, and safe use for the actual arrangement. |
| NIST [AI RMF 1.0 Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) and [human–AI interaction appendix](https://airc.nist.gov/airmf-resources/airmf/appendices/app-c-ai-risk-management-and-human-ai-interaction/) | Explicit roles and oversight where applicable, third-party risk, deployment-representative evaluation, monitoring, incident response, recovery, override, and change management. | AI RMF 1.0 is voluntary and under revision in 2026. It supplies risk-management outcomes, not OCE authority, a universal human-in-the-loop rule, or provider adequacy. |
| Aksin and Masini, [shared-service organization configurations](https://doi.org/10.1016/j.jom.2007.02.003) | Shared-service configurations and their effectiveness are contingent rather than one universal best practice. | Qualify transfer from administrative and business services before choosing an internal, external, engineering, clinical, robotic, AI, or mixed arrangement. |
| Goth et al., [shared-service administrative cost evidence](https://doi.org/10.1108/JSTP-10-2024-0345) | Objective cost-reduction evidence for administrative shared services is often weak or methodologically under-specified. | Require local evidence of cost gain, capability, provision, and arrangement adequacy before relying on the proposed shared service or outsourcing. |

Refresh only the affected OCE.8 claim when a governing FPF distinction changes, an official standard or AI-risk edition changes the action, later human–AI/robotic or provider evidence reverses a comparison obligation, a direct specialist result changes a candidate, or representative use exposes a missing arrangement move. A new publication alone does not reopen the pattern.

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

#### OCE.9:4.2 - Trace the contribution and exception paths with participants

Walk backward from the accepted result to its request, then forward through a representative exception. Ask each participant to show the input used, contribution made, next recipient and basis for accepting or returning it.

Inspect the crossings that can defeat the slice: source/version interpretation, effective assignment, decision authority, access, equipment, provider response, information custody, available time and support. A chart or a specification helps locate these questions but does not answer them.

Obtain the participants' account of the difficult parts. A receiver may know why a formally complete package is unusable; a provider may reveal a support-window limit absent from the design.

#### OCE.9:4.3 - Obtain and exercise the missing conditions

For each action-changing gap, ask its direct owner for the result needed by the receiving work. Name the participant or subject, configuration and window, missing condition, evidence needed, protection boundary and condition for trying again. Distinguish a promise from effective provision.

Use OCE.6 for assignment and enabling-relation questions. Obtain actual access or support through Administration, the provider or other responsible practice. Use OCE.11 when learning, dual operation or recovery conflicts with continuing service. Use OCE.12 when the missing contribution is explanation, constructive challenge, mutual help or another leadership activity.

When a person needs development, supply the representative later-work demand and the task conditions. Current HCD.1, HCD.3 and HCD.4 can help establish the demand, distinguish a human capability target from non-training causes, and qualify a capability profile. Learning design, practice, assessment and transfer still require a qualified direct provider where no current HCD body supplies them.

Secure the whole learning opportunity: an appropriate demonstration, practice on the difficult situation, criterion-based feedback, and later use under the receiving conditions. The learning professional qualifies that design and its assessment. The organization supplies the time, tools, access, protection and support needed to use it. Assess independent later performance in the receiving work, with any instructor assistance made explicit.

#### OCE.9:4.4 - Run a bounded integrated attempt

Before starting dependent trial work, confirm its decision and authority, protected conditions, effective access, capable participants, service coverage and recovery. Stop the defeated branch if one of these is missing. Independent preparation may continue under its own conditions.

Exercise the ordinary request, contribution, challenge, acceptance and exception return with the actual intended configuration and participants. Include a relevant failure such as missing evidence or provider unavailability. Keep the test small enough for the agreed recovery to remain credible.

Compare the observed contribution with its acceptance basis. Record a failed attempt as failed, including special assistance and workarounds. A receiving owner accepts only the result within that owner's remit; evidence acceptance is not automatically release or service authorization.

#### OCE.9:4.5 - Repair the first defeated crossing and observe later use

Repair the supported difficulty rather than relabel the whole change. An unsuitable design returns to OCE.4, OCE.7 or OCE.8. An ineffective relation returns to its owner. A participation or recurrent-practice difficulty enters OCE.10. Revise the trial or learning arrangement if the new observation defeats its premise.

Then exercise the repaired crossing inside the complete contribution again. Include the variation, support loss or substitution relevant to the intended claim. When independence from an initiating facilitator matters, observe a later episode without that person doing the work.

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
| The first rehearsal includes an obsolete source revision beside the current one. The display makes their labels hard to distinguish, and the package contains an unsupported link. | E27 returns the link instead of calling the package complete. The tool/description owner fixes the version cue. The observation also returns to the learning provider; “train harder” is not the sole repair. |
| A qualified provider demonstrates correct and incorrect binding, offers varied practice cases and criterion-based feedback, and observes a fresh case without coaching under the repaired configuration. | The learning result now answers the tool-specific demand at its stated limit. OCE.9 still needs the integrated organization contribution, not merely the individual assessment. |
| The authorized probe supplies comparison evidence. A separate, qualified OCE.8 arrangement decision then selects limited hybrid use under current protection, burden and recovery conditions. | Performing a probe has not selected an arrangement. The chosen use has its own decision basis. |
| Three later weekly package-preparation episodes exercise the revised contribution and return paths. One provider-unavailable case uses the qualified manual fallback; the last episode omits the initiating facilitator. | The receiving owner can inspect what the organization accomplished under those conditions, including retained support and the failure return. Three is a case value, not a general capability threshold. |

The resulting conclusion is bounded to that release family, configuration, participants/support and observed window. It does not establish capability for another holder, general reliability, customer benefit, release permission or enduring culture. OCE.11 carries the interruption and service account; OCE.10 follows whether early challenge becomes a recurrent local practice; OCE.12 supplies the brief, feedback and peer-support work.

If a separate repository change would retire Electrical's evidence-return support too soon, use OCE.16 for the cross-change question. Consume ME.6's or the direct owner's returned retention/replacement result; do not silently assume it from migration completion.

#### OCE.9:5.2 - An association's amendment packet

A member-governed association can realize a bounded evidence-preparation contribution without acquiring an employer's authority over volunteers. Suppose an editorial Method, volunteer acceptances, permitted evidence use, translation and repository support are supplied. Members submit, challenge and revise one amendment packet in two rounds.

The first useful capability result is preparing that packet under those conditions. A missing bylaw or ballot-authority result stops adoption of the standard, not independently permitted editorial preparation. Volunteer windows and publication support replace PumpWorks employment and release assumptions.

### OCE.9:6 - Bias-Annotation

A sponsor can choose an easy demonstration or hide exceptional assistance. Include the failure and support conditions that matter to the receiving use, make refusals and failed attempts reportable, and separate participant accounts from the sponsor's success claim. Do not equate slower performance during safe learning with unwillingness.

### OCE.9:7 - Conformance Checklist

- The slice reaches a named contribution and receiving use, including an exception return.
- The participants can distinguish selected design, effective conditions, performed attempt and capability conclusion.
- Missing assignment, access, authority, learning, service or protection results stop their dependent action.
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

The organization obtains a small contribution with inspectable limitations, and the next repair becomes specific. This requires participant time, suitable practice, support and observation. A narrower result can be more useful than an unsupported declaration that the whole change is implemented.

### OCE.9:10 - Rationale

A complete small contribution exposes dependencies that isolated deliverables conceal. Exercising its failure return reveals who can challenge, decide and recover when the nominal path breaks. Repeated use tests whether the contribution depends on temporary assistance. Returning observations to the relevant organization, platform, Method or learning question allows development at several scales without merging their results.

### OCE.9:11 - SoTA-Echoing

The practice question is how an intended organization contribution becomes usable beyond an introduction event. **Adapt** determinant-sensitive implementation and work-linked learning, while retaining direct integration and introduction Methods for their own results.

| Comparison and selected move | Effect here, evidence limit and reopen condition |
| --- | --- |
| A qualified SYSE.11 System-use result and ME.16 Method-introduction result are serious reusable alternatives to inventing another technical integration or rollout procedure. They do not alone establish the organization's contribution crossings. | Steps 4.1–4.6 consume those results and exercise participation, receiving acceptance, continuing support and later use. Keep the direct result when it answers the whole question; use OCE.9 only for the remaining organization realization. Reopen if that domain difficulty disappears. |
| [Implementation Mapping](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2019.00158/full) connects performer actions, determinants, mechanisms and practical support; its [2025 review](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2025.1603178/full) limits any claim of a guaranteed matching procedure. | Adapt steps 4.2–4.5: obtain and test the condition that changes contribution. This costs inquiry and observation beyond deliverable acceptance. The health-implementation evidence does not validate PumpWorks; an unfit mechanism or defeated condition reopens that intervention. |
| Current [transfer research](https://www.tandfonline.com/doi/full/10.1080/1359432X.2024.2376909) and [reverse training transfer](https://doi.org/10.1016/j.ssci.2025.106920) challenge a course-completion account by connecting workplace opportunity, feedback and reciprocal learning. | Adapt steps 4.3–4.5: secure qualified practice and later use, and return work failures to learning design. Scoping and maritime evidence are not engineering effect estimates. The accepted cost is practice/support time; a receiving-task or support change reopens the learning reliance. |

### OCE.9:12 - Relations

OCE.1 supplies the organization/contribution focus; OCE.4 and OCE.8 supply design and arrangement decisions; OCE.6 supplies effective assignments and enabling relations. OCE.10 addresses supported participation and working-culture difficulties, OCE.11 service coexistence, OCE.12 leadership contributions, OCE.15 a Method-account question, and OCE.16 a consequential cross-change dependency.

Use the current SYSE.11 bounded System-use result and ME.16 introduction result only for the exact configuration and use they support. Use HCD.1/HCD.3/HCD.4 for their demand, target, and capability-profile questions. Where a current HCD learning-design or transfer result is unavailable, obtain a qualified direct provider result or keep the dependent action stopped. OCE.13/OCE.14 are not prerequisites for the observations and corrections needed by this bounded Method, and this Method does not supply their general organization-observation or revision functions.

### OCE.9:End

## OCE.10 - Diagnose Participation and Change Target Working Culture

> **Type:** Method pattern
> **Status:** Eternal alpha
>
> **Primary working result:** a cause-sensitive intervention and its bounded participation or working-culture consequences, or the exact unresolved explanation, professional result or stop.

### OCE.10:0 - Use This When

People nominally support an organization change, but the needed contribution is avoided, distorted, late or unnecessarily burdensome. Begin with one concrete episode: what contribution was expected, what happened when a participant tried, and what made another action more reasonable or safer?

Use OCE.10 to investigate the organization-side conditions, choose an intervention matched to the supported cause, perform it within its protection and authority limits, and observe the receiving work. The target-working-culture branch concerns how local ways of contributing, challenging and helping are learned, recognized and repeated. It is not a programme for changing people's personalities.

The first useful result may be “repair the missing access”, “change the contradictory consequence”, “obtain qualified practice”, or “the current evidence does not distinguish these causes”. A resistance label or a culture score is not an intervention.

Do not use this pattern to settle an employment, clinical, legal or personal-welfare case, or to replace a direct task or service decision whose cause is already known. Use its qualified owner. OCE.17 concerns the culture of Organization Change Engineering practice; OCE.10 concerns the organization being changed.

### OCE.10:1 - Problem Frame

A practitioner and the affected participants need to make a selected contribution workable in the target organization. A new request may conflict with an old reward, an effective duty, workload, belonging, legitimate concern or an established local practice. Formal design and nominal consent can coexist with those conflicts.

The governed move is a bounded intervention on participation conditions or recurrent working practice. The practical gain is a different, supported action instead of repeated persuasion or a larger training order.

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

Current HCD.3 can help distinguish a same-person capability target from task, access and support causes. Obtain clinical judgement or a full learning intervention from the appropriately qualified professional. Preserve a surviving rival when the evidence is insufficient; request the discriminating observation instead of declaring the diagnosis complete.

#### OCE.10:4.3 - Choose a bounded, source-supported intervention

State the intended contribution, supported cause, mechanism hypothesis, participants, effort, protection and authority, expected first difference, adverse consequence and stop. Choose the actual Method or professional intervention that fits those facts. A determinant name or a strategy-menu item does not supply that Method.

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

Return what changed in participation and receiving work, what remained costly or missing, and which rival explanation survives. Continue only the intervention supported by current observations; revise a defeated mechanism or return a professional question to its owner.

An intervention can be useful without being sufficient. Distinguish a bounded participation improvement, evidence of recurrent local practice, an unchanged gap and a wider causal or cultural claim.

For ordinary local action, a short account of the episode, change and next observation can suffice. Stronger causal reliance uses C.28 and suitable evidence. Privacy, worker protection, safety, employment authority and professional competence remain direct conditions even for a small intervention. For a wider consequence comparison, use OCE.13; for an authorized organization-relation revision, use OCE.14. This Method includes the observations and local corrections needed for its own intervention.

### OCE.10:5 - Archetypal Grounding

#### OCE.10:5.1 - PumpWorks: make early evidence challenge usable

In a constructed continuation of the weekly inspection-package change, missing source inputs are disclosed late. Do not infer this cause from the earlier OCE.8 case: its trial authority and provider-access gaps remain separate until supplied.

The participants reconstruct a disputed trace. Permitted task evidence and their accounts show two difficulties: a source-access defect and a local pattern of blaming the person who delays a release. Praise is attached to meeting the date, even when the evidence later needs repair. Another participant also needs practice in explaining a version-binding objection.

The access owner repairs the first condition. For the second, the authorized change owner establishes a protected early-challenge route and changes what is recognized in the package discussion: a timely, substantiated challenge that enables correction is a contribution, not failure to cooperate. Participants co-design the request and response using the disputed trace. A qualified provider supplies practice and feedback for the difficult explanation; the receiving task gives a real opportunity to use it.

In the next constructed episodes, a peer raises a missing-source question before package assembly, the receiver investigates it, and the discussion recognizes the useful correction. A later participant can recover the example and uses the same practice without the initiating sponsor prompting the exchange.

The supported result is a changed local participation practice in those episodes. Access repair, changed consequences and practice happened together; no isolated causal effect is claimed. A count of earlier reports is insufficient by itself: the questions must be relevant and the burden and receiving result must be inspected. The whole organization's culture, release quality and enduring adoption remain unestablished.

If interviews instead showed that people already challenge freely but cannot obtain the needed source, the appropriate intervention would be access repair, not a culture campaign.

#### OCE.10:5.2 - Participation without common employment authority

In a distributed standards association, silence may reflect language, time-zone burden, employer-owned evidence or a seniority norm. An executive-style demand for commitment would miss the actual constraints.

Suppose the association obtains qualified translation and a lawful evidence-use boundary. Participants test an asynchronous challenge-and-response practice on one amendment packet. A junior member can submit a permitted question, an editor responds within an accepted volunteer window, and the correction reaches the packet. Later peer use can support a narrow norm-change observation.

The association has not acquired authority over employer time or permission to publish protected evidence. Missing bylaw or publication decisions still stop their dependent action.

### OCE.10:6 - Bias-Annotation

Sponsor-centred inquiry can turn valid objections into resistance. Fear of consequences can make reported agreement unreliable. Use several relevant perspectives, protect dissent and compare accounts with work evidence. Do not infer a capability deficit, personal motive or group culture from one visible non-use.

### OCE.10:7 - Conformance Checklist

- The gap concerns a concrete contribution and receiving work, not only an attitude label.
- Rival explanations that change action have been considered; uncertainty remains visible.
- The chosen intervention has a supported mechanism, suitable Method, owner, protection and stop.
- Actual use, non-use, burden and receiving consequences are observed.
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

The practitioner can choose a smaller intervention that addresses the actual difficulty and can stop an unsupported one. Participants gain a workable contribution and a way to raise valid concerns. Inquiry, protection, practice and follow-up consume effort; they may reveal that the selected design itself must change.

### OCE.10:10 - Rationale

Participation arises in a working situation with capabilities, relations, interests and consequences. Changing only an explanation or a person's knowledge can leave the operative constraint intact. Cultural continuation adds a further question: whether others can learn and use the practice when the initial intervention is no longer carrying it.

### OCE.10:11 - SoTA-Echoing

The practice question is how to choose a useful participation intervention rather than treating non-use as one kind of resistance. The selected line is determinant-sensitive, participatory and mechanism-explicit. It accepts the cost of bounded inquiry and follow-up rather than assuming a universally correct change recipe.

| Comparison and disposition | Pattern consequence, source limit and reopen condition |
| --- | --- |
| **Adapt** [Implementation Mapping](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2019.00158/full): connect a performer's action, determinant, mechanism and practical support. The [2025 scoping review](https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2025.1603178/full) exposes uneven prioritization and outcome evaluation. | Steps 4.1–4.4 select and test an intervention; a determinant catalogue alone does not do so. The research supplies no guaranteed matching algorithm or engineering effect. Reopen when the mechanism, setting or observed consequence defeats the selection. |
| **Use, with a boundary**, the [2025 CFIR guide](https://pmc.ncbi.nlm.nih.gov/articles/PMC12357348/) for selecting informative determinants and sources. A serious menu-based alternative can organize inquiry but does not itself provide intervention design or enactment. | Step 4.2 keeps a small action-changing explanation set; step 4.3 must still obtain the actual Method. More coded factors are not a better intervention. Reopen if an omitted determinant changes the action. |
| **Retain as comparators** current [ADKAR](https://www.prosci.com/methodology/adkar) and [Kotter's evolving accelerators](https://www.kotterinc.com/methodology/8-steps/), not caricatures of training-only or linear change. Their engagement and support moves may be useful. | Steps 4.2–4.6 additionally bind the local cause, actual authority, consequences and recurrence evidence. Provider accounts are not independent comparative proof. Keep their direct contribution where it fits; reopen if it answers the local question more economically without losing those conditions. |
| **Adapt bounded participant inspection** from the [sociotechnical-prototype experiment](https://doi.org/10.1016/j.apergo.2023.104012). Understandable representations can help participants inspect proposed work; whether cooperation improves must be observed in subsequent use. | Step 4.3 uses a concrete working case and participant co-design, then step 4.4 observes use. The experiment does not establish implementation effectiveness. Reopen when participants cannot understand or use the proposed arrangement. |

### OCE.10:12 - Relations

OCE.6 and the direct relation owners establish assignments, authority and enabling conditions. OCE.8 can reconsider a flawed Work arrangement. OCE.9 integrates the repaired contribution; OCE.11 addresses service/change burden; OCE.12 supplies and develops leadership contributions. OCE.15 and current Method Engineering qualify a new Method account rather than treating an intervention label as an admitted Method.

Current HCD.1/HCD.3/HCD.4 can supply demand, target-diagnosis and capability-profile results; missing learning, clinical or other professional results remain external. C.36 governs cultural relations, and C.28 stronger causal use. OCE.17's OCE-discipline culture is a different subject, not a synonym for target-organization working culture.

### OCE.10:End

## OCE.11 - Coordinate Change Work with Continuing Service

> **Type:** Method pattern
> **Status:** Eternal alpha
>
> **Primary working result:** a bounded, authorized arrangement for change and continuing service to coexist, its observed consequences and hand-back, or an exact reason that no current coexistence is available.

### OCE.11:0 - Use This When

The organization must change while continuing to serve users, but learning, setup, dual operation or recovery compete with existing commitments. Use OCE.11 to make that overlap workable: identify the service conditions that must survive, account for the whole change burden, obtain the necessary decisions, operate a bounded change slice and recover before handing it back.

Begin with one impending collision in time, support or coverage. A vacant calendar slot is not evidence of service headroom. The first useful result can be a smaller change interval, retained support, deferred work or a stop at an unavailable service result.

This pattern concerns coexistence around an organization change. Routine dispatch and case priority belong to Operations; a whole Work-arrangement comparison belongs to OCE.8; comparison of Method or candidate-account co-use belongs to ME.6. OCE.16 supplies the cross-change entry and per-change return when another separately managed change alters a needed condition.

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

With the participating workers and service owner, place the continuing commitments and the complete change burden in the same relevant time and resource view. Include preparation, practice, coaching, dual operation, observation, extra review, exception handling, recovery, catch-up and hand-back.

Keep unlike constraints visible. A holder can have hours but lack the needed capability, authority or access. Another participant's free time may not substitute. A provider's availability can constrain the whole attempt.

Use the smallest representation that reveals the collision. A weekly allocation can suffice for one expert; a time-sensitive service may need shift-level or event-level conditions. Do not add unlike resources into one unexplained capacity number.

#### OCE.11:4.3 - Construct a bounded coexistence arrangement

Combine the direct decisions into a workable overlap. Specify the service coverage to retain, the size and timing of change exposure, available practice/support, the bridge or fallback, the condition for reducing or stopping starts, and what the receiving service owner must obtain at hand-back.

For example, limit a trial to one package, place its protected learning interval where the qualified coach is available, retain the old evidence-return channel until its last consuming obligation ends, and defer further starts when an incident consumes the agreed margin. Each condition must have an effective owner and basis.

Do not repeat a comparison that another Method has already supplied:

- Use ME.6 for a material co-use choice involving Methods or candidate accounts, including changed order, support, allocation or burden when the Methods themselves stay unchanged.
- Use OCE.8 when the question is which whole arrangement should obtain the same result.
- Use OCE.16 when a separately managed change would remove a contribution, access path, authority or support interval needed here. Apply the returned direct result if it already answers the dependency.

If no arrangement satisfies the service and protection conditions, reduce the change, reschedule it, obtain different support, or return the decision to its authorized decision-maker. Do not make the plan feasible by silently assuming overtime or weaker protection.

#### OCE.11:4.4 - Obtain the decisions that make the arrangement usable

Before the dependent work starts, obtain the current service and change decisions, effective allocations and access, relevant admission or amended commitments, specialist protection results and recovery acceptance.

Current OPS.5 can admit exact demand and limit starts; OPS.6 can support case continuation; OPS.7 can revise a bounded priority or commitment. They do not supply every capacity, queue, buffer, constraint or whole-service judgement. Request each missing result from the actual professional owner with the contribution, interval, operating configuration, evidence and retry condition it must answer.

Verify the operating conditions separately from approval of the change plan. Obtain another employer’s allocation from that employer and renewed officeholder authority under its applicable rules.

#### OCE.11:4.5 - Operate the overlap and respond to interruption

Observe service and change separately at the points that can change action. Compare actual work and support with the agreed conditions. When a signal is reached, reduce the change slice, stop new starts, use the qualified fallback or begin recovery under the applicable rule.

Treat a hard safety, rights, security or legal condition as a condition, not a spendable reliability budget. A service-specific trade-off requires that service's own rule and observations; borrowing software percentages does not establish it.

Record what actually happened. Deferred learning or a cancelled probe is not performed work. Failed attempts, missing observations, and unused reserve must remain visible rather than being counted as successful change outcomes. When an interruption invalidates a permission, access condition, support assumption or participant window, renew that input before restarting the defeated branch.

#### OCE.11:4.6 - Recover and hand back with explicit remaining obligations

Recover the affected service and re-establish the conditions required for restart before resuming the blocked change. Avoid charging the same recovery interval to both service restoration and planned change output. If the original arrangement no longer fits, return to the exact allocation, commitment or co-use decision.

At hand-back, obtain the receiving service owner’s acceptance of the actual configuration, support, capability conditions, open obligations and next reconsideration. Retire temporary support only when its agreed consuming obligations and replacement conditions are satisfied.

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

The retention decision still does not establish provider access, service recovery or trial authority that it did not supply. If one of those is absent, stop its dependent action rather than reopening the answered retention question.

#### OCE.11:5.3 - Volunteer windows and an expiring chair

A standards association coordinates amendment preparation with current ballot and publication obligations. Members accept bounded volunteer windows under independent employers. The chair's term ends before a proposed binding decision.

The members and service participants negotiate the editorial overlap and protect publication support within their accepted volunteer commitments. Their agreement by itself changes neither an employer's allocation nor the chair's term. Return the authority question to Governance and stop the binding decision. Separately permitted editorial work can continue. Establish the successor’s authority under the applicable rules before resuming that decision; the project date does not renew the expiring term.

In a hospital, the equivalent service conditions include licensed competence, staffing/fatigue, medical safety and privacy. Obtain those results from the responsible professionals before a patient-facing trial.

### OCE.11:6 - Bias-Annotation

A change sponsor may count only visible project tasks, while a service owner may treat all existing demand as immutable. Recover actual commitments, displacement and hidden learning/recovery burden with the affected participants. Make deferred work visible without treating honest interruption reporting as poor performance.

### OCE.11:7 - Conformance Checklist

- Continuing users, commitments, configuration and protection/recovery conditions are explicit.
- The overlap includes learning, support, dual operation, observation and recovery at the times they consume resources.
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

The organization can reduce change exposure before it defeats continuing service, and can distinguish a recovered service from a completed change. The cost is explicit support, participant time and sometimes slower change. A stop can preserve the possibility of a later useful attempt.

### OCE.11:10 - Rationale

The coexistence problem is temporal and relational: who must provide which contribution while another condition is changing? Counting all burden and applying the direct owners' results makes that overlap inspectable. Observation and hand-back keep a once-credible plan from silently becoming an unsupported operating commitment.

### OCE.11:11 - SoTA-Echoing

The practice question is how to sustain an actual service during bounded organizational change. The selected line combines qualified service conditions, complete overlap accounting, limited exposure, interruption response and accepted hand-back.

| Comparison and disposition | Pattern consequence, evidence limit and reopen condition |
| --- | --- |
| **Reuse** current ME.6 co-use comparison and OPS.5–OPS.7 decisions rather than implementing another portfolio or priority procedure. A broader capacity or portfolio Method is a serious alternative when the question exceeds one bounded overlap. | Steps 4.1–4.4 obtain its exact result and operate the local coexistence. The extra contribution is the organization's learning, support, recovery and hand-back work. Reopen the direct question when conditions change; do not silently claim unavailable OPS capacity bodies. |
| **Adapt** bounded exposure and failure return illustrated by Google's [Canarying Releases](https://sre.google/workbook/canarying-releases/) and service-sensitive reduction illustrated by its [Example Error Budget Policy](https://sre.google/workbook/error-budget-policy/), both 2018 operational references. | Steps 4.3–4.6 qualify exposure, observations and recovery for the actual service. The deliberate cost is slower change and retained support. Software rollback assumptions, percentages and windows do not transfer to people or physical systems; a missing domain recovery/protection result stops that branch. |
| **Reject as a sufficient answer** date-led completion or calendar-only allocation: both can leave learning and recovery unaccounted for. | The forty-hour case includes those costs and preserves the deferred probe. This is a constructed demonstration, not evidence that a fixed reserve is generally adequate. Reopen when observed burden or variability defeats the supplied envelope. |

### OCE.11:12 - Relations

OCE.9 uses the allowed realization interval and returns its observed support needs. OCE.10 can expose a participation consequence of overload or conflicting incentives; OCE.12 needs genuine time for leadership and learning contributions. OCE.8 owns whole-arrangement comparison. OCE.16 qualifies cross-change dependencies and returns direct results; ME.6 owns any required co-use comparison.

Current OPS.1–OPS.7 and qualified direct service owners supply their actual operating results. Coordinating the overlap does not supply a missing operating or professional result. General service capacity, protection and recovery judgements remain with their professional owners; OCE.13/OCE.14's wider organization observation/revision functions remain outside this bounded Method.

### OCE.11:End

## OCE.12 - Distribute Leadership Contributions in Organization Change

> **Type:** Method pattern
> **Status:** Eternal alpha
>
> **Primary working result:** a performed leadership contribution and a tested arrangement for continuing it, or the exact missing participation, capability, authority or support result.

### OCE.12:0 - Use This When

A change depends on somebody making its purpose intelligible, surfacing concerns, helping people perform roles, negotiating assistance or turning a difficult episode into learning. That work is missing, or it works only while one initiator is present. Use OCE.12 to obtain the particular leadership contribution, perform it, develop the needed capability and support its next use.

Start with the contribution that should change: who needs to understand, decide, learn, challenge, help or coordinate what? Choose a concrete working conversation or other qualified Method and name the agreement, corrected action, support or observation it should return.

Leadership here means contribution to people's coordinated work and development. It is not a personality essence, a job title or universal decision authority. The person who facilitates, the person who coaches and the person who can allocate time may be different people.

Do not use this pattern as a substitute for the domain decision, a clinical intervention, an employment action or an already sufficient operating instruction. Use the qualified owner for that result. A needed leadership contribution may come from a peer or mentor who is not the participant's manager.

### OCE.12:1 - Problem Frame

A change practitioner needs practical cooperation from people whose understanding, concerns, attention, capability and working circumstances differ. Formal assignments do not ensure that a difficult question is asked, assistance is obtained or a new skill survives its first use.

The governed move is to obtain, perform and sustain a specific leadership contribution in the organization change. The useful result is something it enabled in the receiving work, with a way to continue or an honest support gap.

### OCE.12:2 - Problem

A role roster can name a sponsor, champion and coach while leaving their actual work unspecified. A central leader may perform every difficult conversation and make the arrangement appear self-sustaining. A leadership course may improve a practice exercise but leave no safe opportunity, feedback or support in the workplace.

The organization needs the contribution and its conditions, not another list of leadership traits.

### OCE.12:3 - Forces

| Force | Tension |
| --- | --- |
| Distributed contribution | Several people can lead useful work, while each has a bounded capability, authority and available time. |
| Role performance | People need a clear expected contribution without reducing their concerns or identity to a job description. |
| Development | Developing the required capability is one task; securing a suitable opportunity and support for later use, and obtaining evidence of that use, is another. |
| Continuation | The initiator should not be indispensable to every episode, but removing that person cannot mean removing all support. |
| Plural authority | Peers and volunteers may contribute leadership without being another person's subordinate. |

### OCE.12:4 - Solution

#### OCE.12:4.1 - Locate the contribution that is missing

Name one receiving difficulty. Examples include an unclear purpose, a feared consequence nobody raises, confusion on entering a role, loss of attention to the expected result, a need to leave or hand over a role safely, incompatible contributions, unavailable help or learning time, and a challenge that the group does not know how to handle.

Recover the expected contribution, situation and evidence. Ask the affected participants what help would change their next action. If the problem is an ineffective access relation or an unresolved technical decision, obtain that direct result rather than substituting an inspiring conversation.

Use OCE.10 when the cause of a participation gap is still uncertain. OCE.12 can also be entered directly when the needed leadership work is already clear.

#### OCE.12:4.2 - Select a concrete contribution and capable participants

Choose a Method for the actual difficulty: a preparation brief, a change-of-situation huddle, a role-performance conversation, task-focused feedback, a debrief, participant inquiry or a qualified coaching/development intervention. State the result it should return and why it fits.

Obtain capable, willing contributors and real time. Separate facilitation, domain knowledge, decision authority, resource provision, coaching and peer support. A capable facilitator need not be able to assess professional competence; a manager may allocate time without knowing how to coach the task.

Secure the participation and protection conditions. For non-subordinates, negotiate contributions through their actual authority and commitment arrangements. A leadership label creates no right to command employer time, protected disclosure or another professional's decision.

#### OCE.12:4.3 - Perform the working conversation

Choose the smallest conversation that can produce the needed result.

**Before shared work, conduct a brief.** State the intended result and current conditions; ask participants to explain their contribution and its limit; identify missing capability, access, time or support; agree the challenge, exception and help paths. Confirm who can make each actual decision. Close with the next contribution and the conditions that would stop or change it.

**When the situation changes, conduct a huddle.** Bring forward the new fact and the affected contribution. Reassess the immediate work, burden and support with the relevant participants. Return any allocation, priority or authority decision to its owner. A huddle cannot approve what its participants are not authorized to decide.

**For role performance, work with the participant.** Recover the expected result and role boundary, then compare them with the participant's understanding, aims, concerns and observed work. Help the person enter the role, maintain attention on its contribution or arrange a lawful, safe handover through the actual assignment procedures. Agree one next contribution or a specific repair and obtain feedback from that work. Do not infer a defective personality from role difficulty.

**After an episode, conduct a task-focused debrief.** Reconstruct what happened from the relevant work and evidence. Ask what helped, what failed, which explanation remains uncertain and what should change next. Assign the actual repair through its owner and agree a later observation. Focus on the task and its conditions, with protection for reporting error; a debrief is not an improvised disciplinary or clinical session.

For a contribution conflict, make the incompatible requests, evidence, consequences and authority visible. Negotiate what can change and return the remaining decision to its owner. Agreement to discuss a conflict is not evidence that it has been resolved.

#### OCE.12:4.4 - Develop the missing contribution capability

When capability is missing, give a qualified learning provider the exact target: who needs to perform which contribution, in what later situation, under which conditions and with what evidence of useful performance.

Obtain a suitable learning design. It may combine a worked demonstration, observation of a competent colleague, practice on the difficult situation, criterion-based feedback and later use without coaching. These are design positions to qualify for the target, not a universal curriculum or mandatory number of hours.

Current HCD.1/HCD.3/HCD.4 can supply a representative-work demand, a qualified target or non-training return, and a capability profile. They do not supply every learning, assessment or transfer Method. Obtain the missing professional result directly; do not award a generic leadership or “master” qualification from one episode.

The organization must make later use possible. Obtain protected practice time, usable tools and information, a receiving task, feedback and support. If the workplace punishes the contribution being learned, return that condition to OCE.10 or its direct owner rather than commissioning another course.

#### OCE.12:4.5 - Arrange the next episode without making a hero indispensable

Agree how the contribution continues: a qualified peer arrangement, access to useful working examples, available coaching or escalation, and an accepted allocation of time. Record only what the next participant needs to perform the work; a growing manual is not the result.

Observe a subsequent episode. When independence from the initiator is the claim, let another qualified participant perform the contribution without the initiator doing it for them. Retain the support actually needed. Rotation is useful only when the next participant is qualified and the participation/authority conditions permit it.

Return an observation to the appropriate development scale. A person's target can change, the organization's support may need repair, a platform may need redesign, or the Method may need qualification. Mentor, manager, provider and receiving worker retain their distinct contributions.

#### OCE.12:4.6 - Return the enabled contribution and its limits

State what the leadership work enabled in the receiving episode, what remained unsupported, what the next episode showed and which assistance was still present. Keep an agreement, performed contribution, capability assessment and cultural-continuation claim distinct.

Use OCE.10 for the recurrent target-working-culture question. Use OCE.11 when the contribution competes with service, and OCE.15/current Method Engineering when the leadership Method itself needs qualification or revision.

Ordinary use can be a brief conversation and a visible next action. Stronger reliance on assessed capability, causal effect or culture requires the relevant professional evidence and A.2.2, C.28 or C.36. Precise dated Work and performer claims require their own A.13/A.15.1 basis; recover actual performance evidence rather than relying only on a participant roster or written plan.

### OCE.12:5 - Archetypal Grounding

#### OCE.12:5.1 - PumpWorks: distributed help around a disputed trace

This constructed continuation assumes the bounded probe and work conditions separately supplied in OCE.9; the earlier OCE.8 recommendation has not become trial authority by being discussed.

Before an inspection-package episode, E27 and an Electrical peer conduct a contribution brief. They state the source/version evidence needed, distinguish tool suggestions from checked links, identify who can challenge a missing source, and confirm that Safety accepts evidence while release authority remains separate.

The first rehearsal exposes an ambiguous version cue. During a protected debrief, E27 shows where the cue led to a mistaken interpretation; the Electrical peer reconstructs the receiving interpretation; the tool/description owner takes the correction. The debrief returns a repair request and a plan for another observation; it gives no basis for judging that E27 lacks commitment.

Different contributors supply the enabling work:

| Needed contribution | What is actually supplied |
| --- | --- |
| Protected learning opportunity | The line manager obtains time under the service/change arrangement; a calendar invitation alone is not the allocation. |
| Difficult challenge practice | A qualified coach/provider demonstrates the conversation, observes varied practice and returns criterion-based feedback. |
| Acceptance boundary | Safety explains which evidence it can accept or return; the separate release decision remains with its authorized holder. |
| Recovery visibility | The service liaison explains the consequence of an incident and the conditions for reducing the change. |
| Peer continuation | E27 and a qualified peer retain a useful example and a way to obtain support for the next episode. |

In a later episode, the peer conducts the brief and raises a missing-source question without the initiating facilitator doing so. The receiver investigates and the group uses the agreed return. The continuation arrangement works in that constructed episode with its retained support.

This does not establish an enduring distributed-leadership culture, universal leadership capability, causal effectiveness or a professional qualification. The learning provider owns its assessment; OCE.9 judges the bounded organization contribution; OCE.10 follows recurrence and recognition.

#### OCE.12:5.2 - A mentor who is not a manager

In a member-governed standards association, a prospective facilitator observes a qualified colleague conduct an evidence-challenge discussion. The pair practises a difficult disagreement with feedback. The prospective facilitator then conducts a later editorial episode within the accepted volunteer and bylaw boundaries.

The mentor supplies demonstration and feedback, not employer authority. The elected chair or other authorized holder makes only the decisions within the actual term and remit. The association obtains an inspectable contribution and a bounded learning result; it has not created a new hierarchy.

If employer time, evidence rights or a qualified learning result is unavailable, the dependent activity stops or changes. A public-hospital version additionally requires the proper clinical, staffing, fatigue, privacy and patient-safety conditions; leadership training does not authorize patient-facing work.

### OCE.12:6 - Bias-Annotation

A celebrated initiator can hide dependence on personal effort or informal power. A formal leader can mistake compliance for understanding. Make peer, service and participant contributions visible, test later use with the stated support, and preserve legitimate refusal or disagreement. Avoid clinical, coercive or employment interpretations of an ordinary work conversation.

### OCE.12:7 - Conformance Checklist

- The leadership contribution answers one concrete receiving difficulty.
- Its Method, intended result and capable contributors are explicit.
- Facilitation, expertise, coaching, authority and time provision remain separate where needed.
- The contribution is performed; a role roster alone is not the result.
- Development includes qualified practice, feedback and an actual opportunity for later use.
- The continuation claim states the next episode, retained support, limits and remaining gap.

### OCE.12:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Better action |
| --- | --- |
| Appoint a champion and assume the leadership work exists. | Name and perform the contribution needed by the receiving task. |
| Ask the central leader to handle every difficult conversation. | Develop and observe a qualified peer arrangement with retained support. |
| Teach constructive challenge while punishing it at work. | Repair the contradictory consequence and provide a protected receiving opportunity. |
| Treat mentor, manager and decision authority as one role. | Obtain each contribution and authority through its actual relation. |

### OCE.12:9 - Consequences

The organization can obtain useful leadership work from several qualified participants and can expose dependence on an initiator before it becomes critical. This requires protected time, capable support and honest feedback. Some contributions remain specialist or authority-bound and should not be rotated merely to demonstrate distribution.

### OCE.12:10 - Rationale

Leadership becomes usable when expressed as work that helps another contribution succeed. Briefs, role conversations and debriefs produce different results; matching the Method to the difficulty makes those results inspectable. Work-linked development and subsequent use connect the holder’s learning with the organization’s support. The mentor’s contribution and managerial authority remain separate.

### OCE.12:11 - SoTA-Echoing

The practice question is how leadership work becomes useful and repeatable in a change. **Adapt** task-focused team communication and multilevel, work-linked leadership development. A single capable change lead remains a valid arrangement when it supplies the needed contributions and continuation; distribution is not a universal value or permission to rotate unqualified people.

| Comparison and selected contribution | Effect here, limit and reopen condition |
| --- | --- |
| AHRQ's current TeamSTEPPS [brief](https://www.ahrq.gov/teamstepps-program/curriculum/team/tools/briefs.html), [debrief](https://www.ahrq.gov/teamstepps-program/curriculum/team/tools/debrief.html) and [tool set](https://www.ahrq.gov/teamstepps-program/resources/modules/index.html) give concrete alternatives to a generic call for better communication. | Adapt step 4.3 to the bounded organization task: clarify contributions before work and derive a correction afterwards. These are qualified adaptations outside healthcare, not clinical permission or an engineering effect estimate. Reopen when the conversation fails to produce its intended work result or protection. |
| The [2024 LOCI trial](https://doi.org/10.1016/j.josat.2024.209437) combines assessment/feedback, leadership training/coaching and higher-level support, offering a serious alternative to an isolated leadership course. | Adapt steps 4.2, 4.4 and 4.5 by obtaining support at the relevant levels and later work. The multicomponent clinical study does not identify one universally effective component or prove transfer to PumpWorks. Added support costs time; changed setting or unsupported transfer reopens the intervention choice. |
| [Making soft skills stick](https://www.tandfonline.com/doi/full/10.1080/1359432X.2024.2376909), 2024, and [reverse training transfer](https://doi.org/10.1016/j.ssci.2025.106920), 2025, connect learning with workplace opportunity, feedback and reciprocal work-to-training effects. | Adapt steps 4.4–4.6: request qualified practice and later-use evidence, and return actual task failures to learning design. Scoping and maritime evidence are not causal guarantees. Reopen the target or support when the contribution does not survive its receiving conditions. |

### OCE.12:12 - Relations

OCE.10 diagnoses and changes participation or target-working-culture conditions. OCE.9 uses the leadership contribution to realize the organization increment. OCE.11 secures feasible overlap with service. OCE.6 and the direct institutional owners establish assignments and authority; OCE.15 and current Method Engineering address the Method itself.

Current HCD.1/HCD.3/HCD.4 and qualified learning providers retain their demand, target, profile, intervention and assessment results. C.36 governs a cultural-continuation claim; C.28 a stronger causal claim. OCE.17's culture of OCE practice is distinct from these leadership contributions in the target organization.

### OCE.12:End

# Part IV - Observe Consequences and Revise the Organization

## OCE.13 - Observe and Compare Organization-Change Consequences

> **Type:** Method pattern
> **Status:** Eternal alpha
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

Bound the inquiry by that decision. If one current service or authority result already determines the permitted next action, return it directly. If a wider observation would not change the decision, do not require it merely to fill an evaluation framework.

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

If the next useful output is an observation plan, name the question, procedure, permitted source, responsible provider, timing and conditions. Do not describe its proposed readings as obtained.

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

The next inquiry is specific. Inspect the obtaining release-support and service assignments, their work intervals and the relevant work evidence to determine whether one holder is committed in incompatible windows. Request the service owner's qualified coverage and substitution conditions if revision becomes the receiving question. The comparison itself does not supply those results.

The result returned to OCE.14 therefore contains the two contrasts, the report's limited reach, live staffing and mix explanations, and the exact assignment question. If the later assignment result confirms a conflict, an authorized revision can respond to that conflict without claiming that this observational comparison established the hybrid arrangement's full causal effect.

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

The cost is explicit comparability and source work. Some results arrive later than the decision window or remain inaccessible. The appropriate response may be a narrower claim, a bounded observation or an authorized precaution supplied by another owner.

### OCE.13:10 - Rationale

Organization change alters relations through which contributions are obtained and burdens distributed. Observing only the intended local result can miss the reason a revision is needed. Beginning with the receiving decision selects an informative, affordable observation scope.

A qualified comparison preserves the meaning of each value and the conditions under which it was obtained. That permits a decision owner to distinguish a real conflict, a measurement problem and an unresolved causal question, instead of treating every disappointing observation as proof that the whole arrangement failed.

### OCE.13:11 - SoTA-Echoing

The practice question is how to obtain enough consequence evidence to change an organization decision. The selected line is decision-led, context-sensitive and proportionate evaluation. Two serious alternatives are reporting the existing KPI set unchanged and requiring a full causal evaluation before any useful return.

**Adapt the current evaluation line.** The [updated MRC framework (Skivington et al., 2021)](https://doi.org/10.1136/bmj.n2061) connects questions, intervention/context relations, stakeholders and consequential uncertainty. Sections 4.1–4.2 adopt those questions for organization contributions and displaced burden rather than a fixed phase sequence. It is a health-intervention research contribution, not evidence that this OCE Method produces a particular effect.

The [Magenta Book (HM Treasury, May 2026)](https://www.gov.uk/government/publications/the-magenta-book/magenta-book-central-government-guidance-on-evaluation-html), especially §§2.2.1–2.2.2 and §3.4, supports intended-user and decision-timing questions, proportionate designs and explicit explanatory limits. Sections 4.3–4.5 adapt that line: reuse suitable evidence, expose rivals and request specialist attribution when it changes the use. Obtain the local measurement result and organization decision authority from their respective owners.

**Adopt the domain consequence question.** R10 Systems Management and R11 Development for the Advanced distinguish desired results, observations of drift, sacrificed work and different development contributions. The PumpWorks and hospital cases carry those distinctions into an OCE comparison; the fuller Guide source keys remain the return for the narratives.

**Reject** unchanged KPI reporting when it omits a decision-changing burden, and reject universal causal study as the price of a descriptive result. At comparable effort, qualifying the two relevant contrasts in PumpWorks yields a more useful next question than broad reporting. More demanding evidence is deliberately retained when its answer can change a high-consequence claim. Reopen the selected comparison when a changed population, procedure, configuration, applicable rival design or later consequence defeats its basis.

### OCE.13:12 - Relations

[C.16](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c16---measurement--metrics-characterization-mmchr) supplies measurement and comparability distinctions. [A.10](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a10---evidence-graph-referring-claim-bound-evidence-and-provenance-graph) governs claim-bound provenance and gaps. [C.28](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c28---causaluse-cal-causal-use-questions-identification-and-realizability) governs the support needed for a particular causal use. The applicable domain professional still supplies the measurement, interpretation or causal result.

OCE.1/OCE.2 and the current arrangement supply the organization and actual-work question where those facts are not already known. OCE.9–OCE.12 keep the observations and corrections needed for their own bounded Methods; they need not wait for a wider OCE.13 comparison.

OCE.14 receives qualified results when an organization relation may need revision. OCE.10 receives a participation or target-culture question; OCE.11 a service/change conflict. OCE.15 and OCE.17 receive feedback only when it changes a reusable Method or the continuation of OCE practice.

Strategy, Operations, human development and clinical, safety, labor, legal, privacy, financial, ecological or customer-domain owners retain their decisions and professional results. The framework's current dependency account distinguishes an available Method from a still-missing result in the case.

### OCE.13:End

## OCE.14 - Revise the Organization from Qualified Results

> **Type:** Method pattern
> **Status:** Eternal alpha
>
> **Primary working result:** an authorized retain, repair, replace, reverse, stop or investigate disposition for identified organization relations or conditions, with its effective scope, accepted losses and remaining realization or observation work; without authority, a bounded proposal or exact authority request.

### OCE.14:1 - Problem frame

**Use this when** a qualified result challenges an organization relation or condition that was previously selected or put into use. A release-support arrangement improves evidence returns but occupies a service interval already promised to customers. The next question is which relation should change, who can change it and what useful contribution must be preserved.

Start from the challenged relation and the result that challenges it. Recover what obtains now, what was only proposed, and the current authority for a change. Then form materially different bounded alternatives.

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

Recover the current relation and the challenged premise; distinguish revision from direct correction; generate and compare bounded alternatives; make the authorized disposition effective; and return unrealized work and future observations.

Recognition is light: one consequential result can justify examining a relation. Assurance is specific to the disposition. A proposal needs a recoverable problem and alternatives. An authorized decision needs its actual mandate and applicable decision rule. An obtaining assignment or enabling relation needs the acts and conditions that make it effective. Realized capability and causal effect require their own evidence.

#### OCE.14:4.1 - Recover what can be revised now

Name the relation or condition, its participants, the contribution it supports and the evidence of its current state. Separate an obtaining arrangement from a selected but unrealized design. If only a proposal is being changed, the result remains a revised proposal until a proper owner decides and the applicable conditions take effect.

Recover the present problem, relevant observations and limits, accepted commitments, affected parties and hard constraints. Ask which current premise is defeated or uncertain. “Performance is down” is too broad if the actual issue is one support interval that now overlaps a service obligation.

Identify the owner and scope of the contemplated decision, including its effective period. A manager's assignment authority, a provider's commitment, a safety acceptance and a member body's ballot decision can be separate. An old approval may not cover a new holder, a different configuration or a later term.

Keep the governing evidence close to the claim. If current evidence does not establish whether the relation obtains, obtain the missing result through OCE.2/OCE.6 or its direct owner. Do not redesign a relation that is only imagined to obtain.

#### OCE.14:4.2 - Choose the smallest revision subject that answers the problem

Decide what kind of result is actually missing.

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

Keep the current arrangement visible with its observed benefits, costs and limits. If a binding condition excludes its continued use, retain it as a reference, not as an admissible continuation option.

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
- [ ] Materially different complete alternatives include an honest current reference and any feasible repair, stopping, recovery or probe branch.
- [ ] Comparison preserves contribution, losses, burden-bearers, continuing service, transition, uncertainty and recovery.
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

The cost is completing alternatives and obtaining the exact relations and external results they require. A revision may remain a proposal, a choice with pending conditions or a stopped dependent action. Those are usable results when they make the next work clear.

### OCE.14:10 - Rationale

An organization is changed through actual relations and contributions, not merely through its description. Consequence evidence therefore has to reach a concrete revision subject and a legitimate decision, while the selected arrangement still has to become usable.

Separating comparison, authority, effectivity and realization lets a practitioner act at the justified scope. It also preserves the value of a good observation when a repair is blocked, and the need for further observation after an authorized repair.

### OCE.14:11 - SoTA-Echoing

The practice question is how to revise an organization after consequences or changed conditions defeat a current premise. The selected line combines explicit alternatives and losses, actual authority, practical support and evidence-driven revision. A serious alternative is to continue a staged rollout toward its original target, treating feedback only as a request for more implementation effort.

**Adopt and adapt the domain line.** R10 Systems Management, R10.5:7 and R10.10:5, separates desired world results from Methods and connects authority, support, first real work, sacrificed alternatives and later improvement. R11 Development for the Advanced, R11.5:13–17, keeps organization revision distinct from direction, platform, learning and research contributions. Sections 4.1–4.6 and the PumpWorks case carry these moves. Fixed adoption calendars, compulsory software and a universal corporate decision owner are not imported.

**Adapt proportionate evaluation use.** The [MRC update (Skivington et al., 2021)](https://doi.org/10.1136/bmj.n2061) and [Magenta Book (HM Treasury, May 2026)](https://www.gov.uk/government/publications/the-magenta-book/magenta-book-central-government-guidance-on-evaluation-html) support revisiting explanations and evidence needs when the receiving decision changes. Section 4.4 retains stronger causal inquiry where it matters without making it a prerequisite for every bounded revision. Obtain local authority and the direct service, clinical or employment result from their qualified owners.

**Reject** both blind rollout continuation and automatic full redesign. At comparable bounded effort, recovering the actual support conflict and completing three alternatives preserves a useful contribution while exposing its cost. The trade-off is that some proposed repairs stop for a missing condition instead of producing a confident new plan. Reopen the decision when an applicable rival, an unavailable recovery condition, changed authority or later consequence defeats its selected basis.

### OCE.14:12 - Relations

[C.11](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11---decision-theory-decsn-cal) supplies choice after the options, chooser and basis are formed. A.3.4 distinguishes the actual bounded change; A.10 and G.11 support evidence and currentness for the relied-on claims.

OCE.13 supplies a qualified consequence comparison when needed. A current direct owner result can also enter OCE.14 without a general observation exercise. OCE.1/OCE.2 recover the organization and actual relations when those are uncertain.

OCE.3–OCE.8 supply the applicable concept, contribution, position, assignment, paired-architecture or whole-arrangement result. OCE.6 establishes obtaining assignments and enabling relations; OCE.9 realizes the contribution; OCE.10/OCE.12 support participation and leadership; OCE.11 coordinates change with continuing service.

OCE.16 handles an actual consequential dependency on a condition another separately managed change uses. OCE.15 and Method Engineering receive a reusable-Method defect; OCE.17 can receive evidence about continuation of OCE practice. Obtain the required authority, professional evidence and actual work results from their respective owners.

### OCE.14:End

# Part V - Sustain Methods, Cross-Change Coordination, and OCE Practice

## OCE.15 - Develop and Refresh Organization-Change Methods

> **Type:** Method pattern
> **Status:** Eternal alpha
>
> **Primary working result:** an **organization-change Method development-and-repertoire result for a named use**. It contains either a repaired named-use repertoire, a bounded OCE candidate Method account prepared for Method Engineering qualification, or both, while keeping intervention contributions, implementation functions, situation claims, mechanisms, source/evidence limits, authority/capability/support conditions, affected Systems, outcomes, and refresh triggers distinct.

### OCE.15:0 - Use This When

Use this pattern when practitioners need to choose, combine, construct, adapt, explain, or replace ways of changing an organization and the available material mixes stage models, intervention lists, implementation strategies, process models, determinant accounts, evaluation frames, local routines, consultancy packages, research findings, tools, training, and remembered practice.

Begin with the organization-change situation and the next OCE result. Choose one or both branches:

1. **Repertoire branch:** recover, qualify, compare, select, and refresh the smallest set of Methods, candidate accounts, and source contributions for the named use.
2. **Domain candidate branch:** construct or adapt the OCE-specific semantics of one bounded candidate Method -- its receiving OCE result, intervention contribution, participants, affected Systems, authority, capability, support, protection, situation claims, mechanism hypotheses, outcome distinctions, stops, and allowed variation -- then pass it to Method Engineering for identity, qualification, trial, fit, worth, variant, and introduction decisions.

The first useful result can be a small inspectable repertoire, a domain-filled candidate account, or an honest blocker. Do not use OCE.15 to declare a branded framework universally effective, turn an intervention label into a Method, infer adoption from participation, or treat a project, process, or case view as the Method.

### OCE.15:0.1 - Working Distinctions

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

A useful OCE Method result therefore preserves what each item is for, its candidate or admitted status, situation claims, mechanism hypotheses, implementation outcomes, organization results, and adaptation triggers.

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

Start from the receiving OCE result, choose the repertoire branch, domain candidate branch, or both, and preserve every item’s function and status. Use OCE.15 to specify what the organization-change Method must do in its working situation. The current Method Engineering Principles Framework supplies general focus, repertoire, criteria, qualification, trial, fit/transfer, worth, variant/provenance, and introduction/revision results.

Recognition is cheap: a named recipe with no inspectable function, status, situation, evidence boundary, or receiving result is enough to enter. Assurance is claim-specific: Method admission, source reliance, situation fit, actual Work, contribution, implementation outcome, and organization result remain separate.

#### OCE.15:4.1 - Pattern-Use Unfolding

1. **Name the receiving OCE result.** State organization, contribution, OCE question, receiver, horizon, decision authority, and stop. Do not begin from a framework name.
2. **Choose the branch.** State whether the need is repertoire repair, domain candidate construction/adaptation, or both. Name the result that each branch must return.
3. **Recover current items and functions.** Identify admitted Methods, candidate accounts, observed routines, intervention or implementation-strategy contributions, process models, determinant accounts, evaluation frames, support, and actual Work. Preserve status and function.
4. **Qualify source contributions.** Record source and edition, population and setting, claim used, measures, evidence design, reported limits, and the OCE decision that the source can change.
5. **Record decision-sensitive situation facts and changes.** Name the Systems, relations, conditions, histories, resources, authority, technology, institutions, populations, and continuing Work that matter. Record observed or anticipated changes and the reassessment trigger.
6. **State reusable semantics and mechanism hypotheses.** Describe entry conditions, operations or contributions, dependencies, stops, results, and allowed variation. State hypotheses or evidence-bearing claims about how ability, motivation, opportunity, mastery, meaning, belonging, participation, access, authority, coordination, and social influence affect the receiving result.
7. **Recover capability, support, authority, and protection.** State who must be capable, assigned, permitted, and authorized; needed tools, data, forums, providers, time, resources; and affected Systems needing representation or specialist protection.
8. **Preserve several Work viewpoints.** Project views foreground commitments, dates, resources, and decision slots; process views recurring contributions and controls; case views changing evidence, exceptions, and next decisions. Use these views to describe the same Work; identify the reusable Method separately.
9. **Compare individual items before bundles.** Ask which item can contribute to the receiving result. For a bundle, state contribution relations, overlap, interactions, combined burden, contradictory assumptions, and stops.
10. **Complete the repertoire branch.** Return the smallest qualified set, visible gaps, selection or probe, and refresh triggers. State whether the selected items remain separate or have been qualified as one composed Method.
11. **Complete the domain candidate branch.** Construct or adapt the bounded candidate semantics with OCE result, intervention contribution, participants, affected Systems, situation facts, authority/capability/support/protection, mechanism hypotheses, implementation outcomes, organization results, stops, and allowed variation. Then use `ME.1`, `ME.3`, `ME.5`, `ME.11`, `ME.13`, `ME.14`, `ME.15`, and `ME.16` as applicable. Obtain the applicable admission, trial, fit, worth, variant, and adoption results through those Methods.
12. **Observe and refresh the smallest claim.** Bind Work, participation, implementation outcomes, organization results, and unintended consequences to the item, semantics, population, conditions, and window. Refresh only the defeated claim.

#### OCE.15:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| named use and branch | Organization, contribution, receiving OCE result, receiver, horizon, authority, stop, and selected branch or branches. |
| item identity/status/function | Method or candidate; separate intervention strategy, process model, determinant account, evaluation frame, description, carrier, tool, training, support, WorkPlan, actual Work, and local routine. |
| domain candidate semantics | Entry conditions, contributions/operations, dependencies, stops, result, variation; participants and affected Systems; authority/capability/support/protection; mechanism and evidence needs. |
| situation facts and changes | Decision-sensitive facts, observed or anticipated changes, and reassessment triggers. |
| implementation and organization results | Implementation outcomes with referent/window and distinct intended organization results. |
| sources/evidence | Source edition, population, setting, measures, design, used findings, limits, qualification window, and unintended-consequence questions. |
| views and structures | Project/process/case viewpoints; same Work; selected Method, Work, assignment, authority, support, or cultural structures; losses. |
| alternatives/bundles | Individual qualification, interaction, overlap, combined burden, contradictions, uncertainty, and status. |
| disposition | Repertoire, candidate return to ME, selected item/set/probe/stop, authority, alternatives, and next action. |
| refresh | Defeated claim, observation, currentness/retirement meaning, preserved history, and external return. |

#### OCE.15:4.3 - What Changes in Practice

Practitioners stop asking which complete framework should be rolled out. They can repair a repertoire or construct the OCE-specific semantics of a candidate, distinguish strategy, process, determinants, evaluation, implementation outcomes, and organization results, and then use Method Engineering for general Method decisions.

### OCE.15:5 - Archetypal Grounding -- PumpWorks Method Result

PumpWorks needs ways to support current-relation recovery, concept comparison, participation, and a bounded capability increment while service continues.

| Item | Function and status | Situation/mechanism hypothesis | Evidence boundary and next use |
| --- | --- | --- | --- |
| `C-PW-PARTICIPATORY-WORK-RECOVERY` | Candidate Method account: reconstruct one release case with protected contributions from Product, Electrical, Software, Safety, Field Service, platform, and provider participants | Opportunity to contribute, meaning, and belonging may improve information quality; participation adds burden and may be unsafe | Use as an `OCE.2` evidence probe only with authority, confidentiality, and burden limits |
| `C-PW-EVIDENCE-RETURN-REPAIR-TRIAL` | Domain candidate: in sampled releases, require Electrical to supply compatibility evidence, the integration holder to use it, Safety to issue an evidence-acceptance result, and the release director to issue the release decision; observe each direct relation and stop on safety or service breach | Visible evidence-use and authority relations may improve coordination; recurrence and reinforcement remain hypotheses | No trial exists. Send the candidate semantics to ME for qualification and trial design; a successful occurrence would not establish whole-organization capability |
| `C-PW-STREAM-ENABLING-INCREMENT` | Candidate account for one stream-aligned increment with enabling Safety and platform contributions | Shorter handoffs may improve coordination; scarce-specialist overload and identity loss compete | Team Topologies is a concept source, not effectiveness proof; assignments, authority, access, coexistence, and service evidence are required |
| `C-PW-PROVIDER-HYBRID-INCREMENT` | Candidate account expanding provider contribution under named access, assurance, exception, recovery, and release-authority relations | External capacity may improve ability; dependence, knowledge loss, and authority ambiguity may worsen results | Provider commitment and authority are unresolved; selection stops until those results exist |
| `PW-QUARTERLY-HANDOFF-PRACTICE` | Observed local-practice account, not an admitted Method | Current coordination may preserve specialist assurance but contribute to delay | Keep as evidence; use ME candidate recovery only if reusable semantics are needed |

For this use, participatory Work recovery is an implementation-strategy contribution inside a candidate Method. The release-case sequence describes the process; claims about missing rig access and authority form a determinant account; the evaluation frame supplies the questions for the measurement plan. Record actual participation separately. Assess feasibility, fidelity, and sustained use as distinct implementation outcomes, and weekly evidenced releases with continuing safe service as organization results. Use the evidence appropriate to each question.

Use project, process, and case views to coordinate commitments, recurring evidence contributions, and one release’s changing evidence. Identify the reusable Method separately. The repertoire branch can select the participatory probe; the domain candidate branch can return the evidence-relation candidate account to Method Engineering for qualification and trial design. Attendance records support an attendance claim; keep decision-bearing contributions and adoption separate.

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
- [ ] Domain candidate construction supplies OCE semantics and returns general Method decisions to the named ME results.
- [ ] Situation claims state the relevant facts, their observed or anticipated changes, and what those changes mean for use.
- [ ] Strategy, process model, determinant account, evaluation frame, implementation outcome, and organization result remain distinct.
- [ ] Mechanisms remain hypotheses or evidence-bearing claims.
- [ ] Capability, assignment, permission, authority, access, support, provider commitment, and protection remain distinct.
- [ ] Project, process, and case views describe the same Work; the reusable Method is identified separately.
- [ ] Bundles expose overlap, interactions, contradictions, burden, and status.
- [ ] Refresh names the smallest defeated claim and preserves unaffected uses and history.

### OCE.15:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Kotter versus ADKAR: choose one.” | Recover contributions, functions, mechanisms, situations, evidence, and smaller alternatives. |
| “Use CFIR as the change Method.” | Use a determinant account only for the bounded questions it answers; choose or construct action separately. |
| “Communication and training handle resistance.” | Diagnose capability, authority, resources, incentives, access, meaning, belonging, participation, and protection. |
| “We tailored the slides, so this is our Method variant.” | Send changed reusable semantics to ME; otherwise maintain the description, support, or local Work result. |
| “Everyone attended, so adoption and success are proven.” | Obtain separate participation, implementation-outcome, organization-result, capability, retention, and culture evidence. |
| “The process view is our change Method.” | Name the viewpoint and same Work; recover the reusable way of doing separately. |

### OCE.15:9 - Consequences

The organization can maintain plural change Methods without arbitrariness and can develop domain candidate semantics without duplicating general Method Engineering. Practitioners see why an item is present, what it can do, which conditions and mechanisms are assumed, and what outcome it can and cannot establish.

The cost is disciplined status and evidence work. Popular interventions can remain source contributions or candidate accounts; bundles need explicit interaction reasoning; selected candidates can still fail in actual Work.

### OCE.15:10 - Rationale

Organization-change Methods address changing organization relations, affected people and Systems, distributed authority, continuing service, and heterogeneous intervention evidence. These conditions change what practitioners must do. Use Method Engineering and FPF for general questions of Method identity, architecture, qualification, trial, fit, worth, variants, introduction, and culture.

[R7](#guide-source-keys) preserves the connected Method, Work, description, capability, instrument, role, variant, and culture account. [R10](#guide-source-keys) shows project, process, and case management as different viewpoints on one Work rather than rival Methods. OCE.15 keeps both connections.

### OCE.15:11 - SoTA-Echoing

| Source | Retained contribution | Boundary and practitioner implication |
| --- | --- | --- |
| Hagl et al., [change-management intervention review](https://doi.org/10.1016/j.hrmr.2023.101000) | Intervention families and ability, motivation, and opportunity-to-contribute mechanisms support repertoire fields. | The synthesis is not a universal sequence; interactions, boundaries, measurement, and consequences remain open. |
| Ekendahl et al., [context-based adaptation](https://doi.org/10.1080/14697017.2026.2638768) | Decision conditions must be assessed and reassessed while change unfolds. | Use the study’s entity/process perspectives to inspect changing conditions; qualify the local adaptation Method separately. |
| Kamarova et al., [behavior and organizational-change synthesis](https://doi.org/10.1002/job.2832) | Mastery, meaning, belonging, and participation counter recipe and “resistance” reduction. | The synthesis is selective and primarily individual-level. |
| Geerligs et al., [implementation-framework scoping review](https://doi.org/10.1186/s13012-023-01296-x) and Nilsen, [taxonomy](https://doi.org/10.1186/s13012-015-0242-0) | Determinant, process, strategy, evaluation, and measurement purposes must remain distinct. | Use the taxonomies to distinguish functions, then select or construct the Method needed for the local result. |
| Powell et al., [ERIC strategies](https://doi.org/10.1186/s13012-015-0209-1) | Discrete implementation strategies can be candidate contributions. | Determine the required sequence, local fit, and effects for the selected contributions. |
| Damschroder et al., [updated CFIR](https://doi.org/10.1186/s13012-022-01245-0) and Reardon et al., [CFIR User Guide](https://doi.org/10.1186/s13012-025-01450-7) | A determinant framework requires project-specific boundary and construct operationalization. | CFIR is not designed to develop an innovation or specify the implementation process and is not a universal OCE Method. |
| Proctor et al., [implementation outcomes](https://doi.org/10.1007/s10488-010-0319-7) and [ten-year review](https://doi.org/10.1186/s13012-023-01286-z) | Implementation outcomes need named referents and remain distinct from service, client, and organization results. | Causal relations among strategies, mechanisms, implementation outcomes, and downstream outcomes remain weakly established. |
| Current Method Engineering Principles Framework; [R7/R10](#guide-source-keys) | General Method results, connected conceptual synthesis, and several viewpoints on one Work. | OCE.15 consumes the named ME results and adds only organization-change semantics and use. |

Reopen when a source or representative use exposes a materially different domain contribution, framework function, mechanism, situation change, outcome boundary, bundle interaction, or candidate-development need, or when Method Engineering makes an OCE move redundant.

### OCE.15:12 - Relations

- The supplying product is the current `Method Engineering Principles Framework` named in the framework dependency account. `ME.1` supplies Method focus, `ME.2` named-use repertoire structure, `ME.3` situational criteria, `ME.5` individual qualification, `ME.11` trial, `ME.13` fit/transfer, `ME.14` worth, `ME.15` variants/provenance, and `ME.16` introduction/observation/revision.
- OCE.15 supplies the receiving OCE result, organization-change contribution, participants and affected Systems, decision-sensitive situation facts, authority/capability/support/protection, mechanism hypotheses, implementation outcomes, and organization results. A domain candidate remains a candidate until the applicable ME results say otherwise.
- `OCE.1` supplies organization and contribution; `OCE.2` and `OCE.3` can supply current relations and concepts. Any OCE pattern can request a named-use repertoire or domain candidate.
- `OCE.10` can consume a qualified contribution for participation or target-organization working-culture repair and return observations. `OCE.13` supplies later organization and affected-System observations. Qualify any Method-effectiveness claim against the evidence and intended use.
- `OCE.16` consumes a compatible Method/repertoire result for simultaneous Work. `OCE.17` concerns enacted OCE discipline culture and can supply bounded feedback; it is not the owner of the target organization’s culture.

### OCE.15:End

## OCE.16 - Reconcile Simultaneous Organization-Change Work

> **Type:** Method pattern
> **Status:** Eternal alpha
>
> **Primary working result:** a **qualified cross-change question and per-change return for one consequential dependency**. The question identifies separately managed changes, the organizational condition one change would alter, the other change's exact action or decision that may use it, the interaction window, the claim status and evidence, the strongest direct Method and result owner, and any exact missing result. After that direct Method returns, OCE.16 tells each affected change which governed result it can use, what condition it must preserve or revise, and what observation reopens the question.

### OCE.16:0 - Use This When

Use this pattern when two or more separately managed organization changes may alter the same contribution, holder assignment, authority, access path, provider relation, information return, acceptance route, capability-development condition, support interval, or continuing-Work condition, but no current account yet establishes whether they form one decision question.

A recognizable entry is small: one change proposes to alter a named organizational condition and another change plausibly uses that condition for one consequential participant action or decision in an overlapping window. The first useful result can be a qualified cross-change question, a direct exit because the claimed dependency is absent or already answered, or an exact request for a missing owner result.

Do not use OCE.16 merely because initiatives run at the same time, share a dashboard, use different descriptions, or draw from one aggregate resource pool. If the exact question and its consequences for each change are already recoverable, use the direct Method and stop. OCE.16 does not compare joint architectures, select an arrangement, reschedule a portfolio, authorize Work, establish compatibility, or create a superior change authority.

### OCE.16:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| separately managed change | A proposed or actual organization change with its own subject, intended result, status, scope, owner, evidence, and next decision. Separation does not imply independence. |
| organizational condition | A contribution, assignment, authority, permission, access path, provider or support relation, information return, acceptance route, participation condition, capability condition, or other organization relation or condition that a change may alter. |
| consequential dependency | A claim that alteration of one named condition can change another change's exact action or decision within a stated window. It is not proved by temporal overlap, a diagram, or a participant's interpretation alone. |
| participant account | A bounded report from a participant or affected System about an action, demand, consequence, or condition. Use it to locate a possible dependency, then test the claimed contradiction against current evidence and recover decision authority separately. |
| qualified cross-change question | Ordinary decision-support content naming the changes, altered condition, consumer action or decision, window, participants, evidence and claim status, direct Method, result owner, and any missing input. |
| direct Method | The strongest current Method that owns the substantive comparison, relation, authority, operating, specialist, or other decision after the question is qualified. |
| per-change return | A readable application of already-governed direct results to every affected change. It adds no second choice or authorization. |
| direct exit | A stop in OCE.16 because no consequential consumer exists, the dependency is unsupported, or the direct answer and its per-change consequences are already available. |

Different project, process, case, architecture, Method, organization, and operating descriptions remain different. OCE.16 asks whether one change alters a condition another actually uses; it does not force unlike subjects into one view or one programme.

### OCE.16:1 - Problem Frame

Each change can look locally plausible while the conjunction is not. One effort can promise autonomy while another introduces a new approval; a provider or repository transition can retire an evidence-return contribution that another change still needs; two changes can rely on the same holder in action windows that aggregate availability hides; or an authority change can depend on a credential contribution whose own authorization depends on the incoming authority.

The reverse error also matters. Practitioners can infer a contradiction from different language, a programme map, or one actor's prediction even though the direct relations are compatible. The useful move is therefore not a universal scan or premature joint design. It is a bounded dependency probe around one consequential action.

### OCE.16:2 - Problem

Separately maintained change accounts often stop at their own boundary. The owner of the alteration sees a completed migration, assignment, or design; the owner of the consuming change discovers the missing condition only during enactment. A central coordination layer can make the problem worse by replacing exact subjects, truth statuses, and authorities with traffic-light summaries.

Without a domain entry-and-return Method, practitioners either miss the interaction or duplicate the direct comparison. The first loses an enabling condition. The second lets a coordination note appear to choose architecture, authority, support, or operating commitments that remain owned elsewhere.

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

For one proposed organizational alteration, identify one plausible consumer in another change and qualify their exact dependency before invoking any substantive comparison. Use the strongest direct Method for the question and return its governed result to every affected change.

Recognition is cheap: one named alteration and one plausible consumer action are enough to inspect. Assurance is use-specific: recover the changes and subjects, current statuses, altered condition, receiving action or decision, interaction window, participant accounts, direct evidence, governing Method and result owner. OCE.16 cannot assure a result the direct route has not produced.

#### OCE.16:4.1 - Five-Move Pattern-Use Unfolding

1. **Bind the separately managed changes.** Name each actual or proposed change, its subject, intended result, current status, scope, owner, next decision, and relevant window. Do not begin from a programme row or assume that two descriptions name one Work.
2. **Find one consequential dependency.** For one organizational condition a change would alter, ask: which other change uses this condition, for which exact participant action or decision, and during which window? Stop if there is no plausible consequential consumer. Do not inventory or pairwise-scan every initiative.
3. **Qualify the claim with participants and current evidence.** Recover the participant account and distinguish observed fact, current relation, expected consequence, proposal, interpretation, and decision. Test the named condition, consumer action, timing, effectivity, alternatives, and evidence. Return a supported or absent dependency, a compatible difference, an unsupported claim, a missing fact, or an exact missing-owner result.
4. **Invoke the strongest direct Method.** Route the qualified question to ME.6, C.32.MWA, the exact OCE or OPS Method, A.15, Strategy, Governance, Administration, HCD, safety, legal, finance, security, procurement, service, or another direct owner. Give it the smallest sufficient question and evidence. Use the comparison, selection, compatibility judgment, acceptance, or authorization returned by that Method and its actual owners.
5. **Return governed results to every affected change.** For each change, state the direct result it can use, the condition it must preserve, revise, obtain, or stop assuming, the owner and validity window, and the observation that reopens the question. Leave unaffected Work on its current basis. If the direct result is missing, return that exact absence and its consequence rather than filling it by coordination language.

#### OCE.16:4.2 - Choose the Strongest Direct Route

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
| direct route | Strongest direct Method, bounded question, required inputs, result owner and authority, and exact unavailable result. |
| direct result | The governed comparison, relation, authority, operating, specialist, stop, or missing-result return. Do not relabel it as an OCE.16 decision. |
| per-change return | For every affected change: usable result, preserved or revised condition, next action or stop, validity window, and reopen observation. |
| economy and exit | Why the probe is proportionate, what unaffected Work remains unchanged, and whether the Method exits without further coordination. |

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
- [ ] The strongest direct Method and result owner are named before substantive alternatives are compared.
- [ ] ME.6 owns Method/candidate-account co-use, including unchanged-Method relation-only arrangements.
- [ ] OCE.16 makes no architecture selection, compatibility judgment, authorization, acceptance, readiness, priority, or capacity decision.
- [ ] Every affected change receives the governed result or exact missing result; unaffected Work keeps its current basis.
- [ ] A direct exit is used when the dependency is absent or already answered.
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

The cost is a bounded qualification effort and an honest possibility of no result. Participants and owners must expose exact actions, windows, evidence, and authority. The Method can end with an unsupported dependency, a missing fact, or an unavailable owner result rather than a harmonized plan.

### OCE.16:10 - Rationale

The difficulty addressed here is finding a consequential dependency and returning its resolution across separately managed changes. ME.6 already compares Method and candidate-account co-use through order, allocation, support, access, authority, evidence, burden, and other decision-changing structures, including relation-only arrangements with unchanged Methods. OCE.4-OCE.8 and direct domain Methods already own contribution, assignment, enabling, architecture, and arrangement results.

Use OCE.16 when the consequential cross-change question still needs to be found or qualified, or when a direct result still needs to reach the changes that depend on it. The consequential-action probe is smaller than an initiative inventory yet stronger than temporal overlap. Per-change return prevents a locally completed change from concealing a defeated premise without creating a superior authorization.

### OCE.16:11 - SoTA-Echoing

| Source | Retained contribution | Boundary and practitioner implication |
| --- | --- | --- |
| Kanitz, Huy, Backmann and Hoegl, [No change is an island](https://doi.org/10.5465/amj.2019.0413) | Interacting changes can generate cognitive, normative, and procedural inconsistency judgments beyond a simple resource collision. | Inspect joint demands and organizational prescriptions. The primary abstract supports recognition of possible inconsistency; qualify local causal and effectiveness claims with further evidence. |
| Skov and Lê, [Resisting by not resisting](https://doi.org/10.1177/00187267241248529) | Actors can construct relationships and inconsistency claims between mandated changes. | Test the claimed dependency and underlying condition; neither dismiss it as resistance nor accept it automatically. Use the abstract for this recognition question; a motive diagnosis requires its own qualified evidence. |
| Rishani, Schouten and Hoever, [Navigating multiple team membership](https://doi.org/10.1111/spc3.12899) | Membership, time allocation, and variety are different, with heterogeneous relations to effectiveness. | Inspect actual role demands, action windows, informational benefit, and burden. No universal team-count or utilization threshold transfers. |
| Zhang, Li, Zhang, Deng and Yang, [Time the Surge](https://journals.aom.org/doi/abs/10.5465/amj.2024.0522?af=R) | Non-coinciding project portfolios and shared external overlap make timing of team activity consequential. | Probe whose actions coincide rather than using total allocation alone. Use the primary abstract to recognize a timing question, then obtain a schedule qualified for the actual work. |
| Martinsuo and Ahola, [Multi-project management in inter-organizational contexts](https://doi.org/10.1016/j.ijproman.2022.09.003) | Inter-organizational multi-project settings alter strategy, resource, governance, and learning questions. | Challenge one-firm authority assumptions. Use the conceptual primary abstract to recognize interorganizational questions; obtain the applicable authority and Method from their owners. |
| Fischer, Marcus and Röglinger, [A portfolio management Method for process-mining-enabled improvement projects](https://doi.org/10.1007/s12599-024-00906-2) | A contemporary portfolio Method can directly relate strategy, identification, selection, implementation, and monitoring in its bounded setting. | Use such a Method when portfolio selection is the problem. Do not generalize its cases, data, or authority to every organization change. |
| Current ME, OCE, OPS, A.15, C.32.MWA, and C.11 results | Supply the substantive Method-co-use, organization, operating, Work, synthesis, and decision results. | Use OCE.16 for discovery, qualification, access to the direct Method, and per-change return; obtain any missing substantive result from its owner. |

Reopen when a direct supplier or existing entry supplies the same recognition, qualification, and per-change return at comparable effort; representative use finds no missed interaction that changes action; a new source defeats the consequential-action probe or participant/evidence boundary; or changed ME, OCE, OPS, or domain results make the route or promised use false.

### OCE.16:12 - Relations

- [ME.6 in the current Method Engineering Principles Framework](METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md) owns Method and candidate-account co-use comparison, including relation-only arrangements with unchanged Methods. OCE.16 supplies a qualified cross-change input and per-change return.
- [C.32.MWA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c32mwa---practice-architecture-synthesis-from-several-structures) owns prospective practice-architecture synthesis after relevant structures and subjects are selected.
- [OCE.4](#oce4---design-contribution-architecture), OCE.5, and [OCE.6](#oce6---establish-holder-assignments-and-enabling-relations) own contribution-design, position, assignment, and enabling-relation results. [OCE.7](#oce7---coordinate-product-or-service-and-organization-architecture-decisions) owns paired product/service and organization architecture decisions.
- [OCE.8](#oce8---configure-humanai-robotic-and-provider-work-arrangements) owns whole same-result arrangement comparison and its choice, probe, rejection, or reroute result.
- OCE.15 supplies a compatible named-use Method/repertoire result. OCE.16 does not repair or admit it.
- [The current Operations Management Principles Framework (preview)](README.md#development-previews) supplies currently available operating results. A.15 supplies general Work distinctions and decisions. C.11 and direct domain governors own choices.
- Use OCE.11 for its change/service-coexistence Method; OCE.16 does not supply that Method's actual result. Use OCE.13 to compare wider organization-change consequences, OCE.14 to revise an organization relation within its authority and effectivity limits, and OCE.17 to examine continuation of OCE practice. These are optional returns for their own questions, not substitutes for the direct owner of the current cross-change result. A missing service, Strategy, Governance, Administration, HCD, safety, legal, finance, security, procurement, or provider result stays missing until its direct owner returns it.

### OCE.16:End

## OCE.17 - Continue and Renew Organization-Change Engineering Practice

> **Type:** Method pattern
> **Status:** Eternal alpha
>
> **Primary working result:** a bounded account of which OCE practice continues, how its continuation is supported or impeded, and the justified retention, intervention or return, with observed later use or an exact observation gap.

### OCE.17:1 - Problem frame

**Use this when** an organization-change practice seems to be spreading, fading or changing among practitioners, and that difference matters to their next work. A case group still teaches “organization mapping”, yet its members now submit charts without recovering who supplies an input, who uses it and who can decide. Elsewhere the old name disappears, but practitioners still make those distinctions in real cases. The useful question is what continues in the work, not which label survives.

Start with one consequential OCE move in one organization-change episode. Compare the practice claimed with the action and usable result actually recoverable there. Then examine the connections through which another practitioner could encounter, attempt, criticize and continue it.

Continuing organization development is the wider concern. This Method covers the cultural continuation of **Organization Change Engineering practice across practitioners and work settings**. Its subject is the practice and the relations through which it is transmitted, recognized, selected, enacted, retained or lost. A practitioner population is not automatically one organization, System or capability holder. A Method is a reusable way of obtaining a result. Its description, a carrier such as a file or course handout, and an occasion of using the Method are different things; teaching can use the description and carrier as support.

The first useful result may be “the operative practice continues under another name”, “the recognition rule rewards the wrong result”, or “there was no suitable opportunity to observe use”. A supported intervention can follow; a workshop or profession-wide survey is not an entry requirement.

**Use another pattern when** the question is the working culture of the organization being changed: OCE.10 supplies that branch. Use OCE.15 when the reusable OCE Method or repertoire itself needs repair. A person's learning target without a cultural-continuation question belongs with HCD or the qualified learning provider. An adequate current continuation account can simply be used.

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

Generate a few materially different responses to the supported difficulty. Keeping a useful current variant is one of them. Compare the expected contribution, burden, participation conditions and the observation that could show each response was mistaken.

For a transmission gap, let practitioners compare an actual organization-change result with the deficient example. Make the missing distinction visible in critique, preserve the exact source and a counterexample, and arrange a later opportunity to use it. For example, compare a filled organization chart with a recoverable evidence-supply and receiving-decision relation; ask what each lets the receiving practitioner decide.

For misdirected recognition, change what the group asks contributors to show. A case can be recognized for tracing an actual contribution, exposing an authority limit, comparing serious alternatives or preserving conflicting consequences. Let practitioners challenge the judgement and show why a different form still supplies the result. A facilitator's permission to change peer feedback is not authority to change an employer's appraisal, credential or pay rule.

For a single-mentor dependency, obtain another qualified practitioner and a recoverable explanation of the case, including why plausible alternatives failed. A name on a support roster is insufficient: the person must be willing, capable and available for the required contribution.

For an obsolete or defective Method, retain the problem evidence and return it to OCE.15. If the direct Method already contains the needed branch, repair its transmission rather than inventing a new variant. If it does not, a cultural intervention cannot supply the missing reusable answer.

Select a response only within the actual authority and participation conditions. Qualified learning, facilitation, human assessment, employment, service and protection results remain with their direct providers. A bounded case discussion can be useful without claiming to be a complete development intervention.

#### OCE.17:4.5 - Perform the intervention and look beyond the event

Obtain the commitments, lawful evidence use, work opportunity, support and qualified contributions that the selected response requires. Separate what was agreed from what was done. Record the actual case discussion, changed example, recognition decision or support contribution at the detail needed for later interpretation.

At a later suitable opportunity, inspect whether the practitioner used the relevant OCE distinctions and produced a result another participant could use. Choose a case without the original initiator, or with a changed condition, when that contrast matters to the intended continuation claim. Do not require every case to be unassisted: assistance may be a legitimate part of the practice, but its contribution must remain visible.

An event attendance record supports attendance. A later case can support a bounded enactment claim. Learning, transfer, lasting retention and the causal contribution of the intervention each need their own qualified evidence. If there was no permitted opportunity, the next result is an opportunity gap, not evidence that teaching failed.

Check the cost of the response as well as its apparent success. Did additional case work displace service, expose protected information, discourage dissent or shift the burden to an unsupported practitioner? Stop or narrow the dependent intervention when those conditions fail.

#### OCE.17:4.6 - Return the supported continuation and its limits

State which operative variant, practitioners, cases and period the account covers; what was observed; what remains inferred or missing; what changed in transmission, recognition or support; and what decision or next observation follows. Ordinary work can use a short note with the relevant case references. A new register or universal maturity scale is unnecessary.

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

The group retains the four usable variants. Within its permission, it chooses a bounded response for the gap: a qualified practitioner leads one case critique, the group replaces the deficient example with a source-linked case and counterexample, and later peer feedback asks for the usable contribution and decision relation. The practitioners agree a permitted later opportunity where one exists. No employer is assumed to supply time or access merely because the group chose the response.

In the fictional follow-up, one of the two practitioners independently recovers the crossing and receiving authority in a different organization case. The other cannot access the required evidence in the later window. The result is therefore mixed: a later operative use is observed for one practitioner, and an access gap remains for the other. It is not “two people trained, one passed”; no controlled learning-effect claim was sought or supplied.

The continuation account names those cases and limits. The access question returns to its organization owner. If the critique had instead found that OCE.2 itself lacked a needed move, the facilitator would return that specific problem to OCE.15; changing peer recognition would not repair the Method.

#### OCE.17:5.2 - A useful absence and a voluntary boundary

An association sees fewer position-design diagrams and fears that its members have abandoned organization design. A permitted case shows why: the current OCE.5 question concluded that a short-lived editorial contribution needed direct assignments, not a continuing institutional position. The absence of a position diagram is appropriate use, not cultural loss. The group keeps the example and asks whether its recognition questions wrongly require the diagram.

Members work for independent employers. The association can offer a case clinic under its participation rules, but cannot promise employer evidence, assign protected work or extend an expired chair's authority. If access is denied, only the access-dependent use remains unobserved. This boundary changes what the group may do; it is not solved by calling the members a community.

### OCE.17:6 - Bias-Annotation

Prestige can make a copied example appear valid; inspect the actual receiving result and a serious countercase. Survivor bias can hide departed or excluded practitioners; include their experience when it could change the account. A facilitator can prefer visible events over slow, less visible work opportunities; distinguish the event from later use and its costs.

The goal is useful continuation, not maximum conformity. Preserve dissent that reveals a poor Method, unsuitable conditions or a less burdensome valid variant.

### OCE.17:7 - Conformance Checklist

- [ ] A named operative OCE move is recovered from a real or explicitly constructed work episode and compared with its Method or declared variant.
- [ ] The practitioner and case scope is explicit; a population is not silently made one capability holder.
- [ ] Transmission, recognition, opportunity, enactment and retention are distinguished where they can change the explanation.
- [ ] Competing source, interpretation, access, support, recognition, capability and Method-fit explanations receive the evidence their use needs.
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

The cost is access to informative cases and willing, qualified contributions. Some conclusions remain narrow because later work, permission or evidence is absent. That limit is preferable to burdening people with an intervention whose actual target has not been found.

### OCE.17:10 - Rationale

An OCE practice matters because its distinctions change organization-change action and the result a recipient can use. Its cultural continuation depends on more than a preserved description: practitioners must encounter the move, have conditions for using it, receive meaningful criticism and recognition, and be able to continue in later work.

This makes diagnosis by case comparison practical. A preserved result under a new name, a chart rewarded for the wrong feature and an absent work opportunity lead to different actions. Keeping those differences visible permits both continuity and renewal without treating every change as loss.

### OCE.17:11 - SoTA-Echoing

The practice question is how to respond when an apparent OCE practice fails to continue. The selected line is case-based recognition followed by a mechanism-matched, condition-qualified response and later observation. The serious alternative is a common communication or training package applied to every apparent non-use. It is cheaper to schedule, but cannot distinguish a deficient example from missing permission or a valid refusal of an obsolete move.

**Adopt and adapt the domain line.** R7 Methodology, R7.5:13–15 and :19 and R7.6:12/:14, supports recovering operative Methods across carriers and practitioners. R11 Development for the Advanced, R11.9:7–8, :12–15 and :22–24, adds repeated work in unlike settings. Sections 4.1–4.2 and the two cases carry that contribution. Do not import fixed hours, status ladders, biological analogies or label popularity as evidence of mastery or persistence. The fuller narratives are discoverable through the framework's Guide source keys.

**Adapt current implementation inquiry.** The [NPT coding manual (May et al., 2022)](https://doi.org/10.1186/s13012-022-01191-x) and [NPT-derived strategy synthesis (May et al., 2025)](https://doi.org/10.1186/s13012-025-01444-5) are best-known-line contributors for matching implementation work to an identified difficulty. They change sections 4.3–4.5: ask about understanding, participation, support and appraisal before selecting a response. The synthesis used 63 health/social-care studies and interpretive coding; it supplies no comparative effectiveness result for OCE practitioners.

**Retain the contextual challenge.** The [NPT consolidation, version 1 (May, Finch and Rapley, 2026)](https://doi.org/10.3310/nihropenres.14315.1) strengthens attention to changing conditions and distributed burdens in sections 4.2 and 4.5. It is a qualified comparison, not proof of cultural-evolution or individual-learning mechanisms.

At comparable bounded effort, inspecting one useful and one doubtful case can distinguish next actions that the generic package leaves conflated. The deliberate cost is obtaining case evidence and professional input where the question needs them. **Reject** the claim that this comparison establishes intervention efficacy. Reopen the selected response when later cases, a better applicable rival or changed source evidence defeats its mechanism, protection or continuation premise.

### OCE.17:12 - Relations

[C.36](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c36---cultural-evolution-and-cultural-evolution-engineering) supplies cultural-case, transmission, recognition, selection and memory distinctions, including the difference between an intervention and observed cultural change. A.10 supports evidence provenance; C.28 governs stronger causal reliance.

OCE.2, OCE.3, OCE.5 and other OCE Methods supply the actual domain moves recognized in cases. [OCE.15](#oce15---develop-and-refresh-organization-change-methods) receives a reusable-Method or repertoire problem and uses current Method Engineering for qualification, fit, trial and variants.

OCE.10 governs participation and working culture in the organization being changed. OCE.12 can supply a concrete qualified explanation, critique or support contribution. OCE.13 can provide a consequence comparison relevant to a practice question; OCE.14 supplies an authorized organization-relation revision, not authority over a practitioner population.

Current HCD.1/HCD.3/HCD.4 supply their bounded human-demand, diagnostic and profile results. Learning design, practice, assessment, transfer and retention outside those results remain requests to qualified providers. The framework's dependency and sibling-return account states the current CAE/CDI contribution limits; the population does not become one development holder by association.

### OCE.17:End

# Cross-Pattern Application

## APP-OCE-01 - PumpWorks weekly AI-inspection releases

This constructed case concerns the existing PumpWorks engineering organization. PumpWorks intends weekly evidenced AI-inspection releases while field service and support continue; the case is illustrative, not empirical evidence about a company.

`OCE.1` selects `PumpWorks-EngineeringOrg` rather than the whole company, an imagined AI team, or a provider-inclusive whole. It states contribution, Work/capability questions, affected Systems, authority boundary, and reopen evidence.

`OCE.2` recovers actual release Work; electrical-evidence supply and use; separate safety-acceptance and release decisions; provider model-artifact and support provision; rig access; field-service information return; holder assignments; participation; and evidence windows. It keeps the relations separate and leaves any position claim unresolved until its establishment and identity basis is available.

`OCE.3` obtains contributions from affected Work participants and generates three alternatives by changing named relations: functional repair, stream/enabling, and provider hybrid. The small decision set needs no Archive/Front. `C.17` can characterize candidates after generation.

`OCE.4` selects several structures and writes possible-future contribution-relation specifications for electrical and platform evidence, provider artifacts, Safety acceptance, the release decision, and field-service information return. The specifications describe proposed relations; later realization must establish whether they obtain.

`OCE.5` establishes one continuing release-evidence integration position because vacancy, holder replacement, expected contribution, and eligibility matter across releases. Safety acceptance and release authority stay outside that position.

`OCE.6` returns one effective holder assignment and rig-access relation, one provider-access relation that is decided but not effective, separately held acceptance and release authority, a missing responsibility governor, and a bounded capability gap. The receiving practitioner can act on the distinct effective and missing conditions.

`OCE.7` compares organization-side, product-side, joint, and bounded-mismatch candidates. PumpWorks selects a bounded joint change while shared platform, independent Safety, scarce capability homes, and provider support remain deliberately non-isomorphic.

`OCE.8` holds the weekly evidenced package and acceptance basis stable, keeps the quarterly functional handoff as baseline-only, and completes three whole candidates: `PW-WA-INTERNAL-PLATFORM`, `PW-WA-DUAL-HOLDER`, and `PW-WA-HYBRID-TRACE`. Participant knowledge changes named option and protection positions. The hybrid is only a probe recommendation; missing trial DecisionSubject/authority, ineffective provider access, and unresolved protection/recovery evidence make the current disposition `reroute`, not a `ChoiceResult`.

OCE.15 repairs the named-use repertoire and constructs one evidence-return repair candidate. It distinguishes implementation strategy, process description, determinants, evaluation frame, implementation outcomes, and organization results, then uses the current Method Engineering Principles Framework for general Method qualification and trial decisions.

For a hypothetical simultaneous repository-consolidation change, OCE.16 asks whether retiring the existing Electrical evidence-return contribution at migration completion can remove evidence needed for Engineer-E27's challenged-package integration action. It keeps the hybrid recommendation, trial authority, provider access, E27 assignment and rig access, Safety acceptance, release authority, protection, and recovery as separate claims. ME.6 supplies comparison of retirement, bounded retention, qualified replacement, and the incumbent; authorized owners decide, applying C.11 when a precise choice result is needed, while OCE.4 and OCE.6 own changed contribution and effective-relation results. OCE.16 returns those governed results or exact gaps to both changes and makes no second selection.

Enter at the question relevant to the current work and stop when its needed result has been obtained. At this point, the hybrid arrangement remains a recommendation with explicit realization and evidence gaps.

### Conditioned continuation -- realization, participation, service and leadership

The following is a new hypothetical six-week continuation beginning after the OCE.6 appointment's effective date. It does not alter the initial recommendation or reroute. Suppose the properly authorized decision-maker separately authorizes a bounded representative probe; the provider and security owner make permitted access effective; qualified learning and service owners supply the practice, coverage, protection and recovery conditions. The missing coordination-responsibility predicate remains missing.

OCE.9 follows the weekly contribution from Electrical evidence through provider suggestions and E27's source/version check to separate Safety acceptance. A failed rehearsal exposes an ambiguous version cue. Its owner repairs the cue; a qualified provider supplies practice, feedback and fresh uncoached assessment. The probe supplies evidence to a separate bounded OCE.8 decision that selects limited hybrid use. Three later weekly package-preparation episodes, including a provider-failure manual return and one without the initiating facilitator, support only the stated release family, configuration, participants/support and observation window.

OCE.10 distinguishes an access defect from the discouragement of early disclosure through blame and date-only recognition. The authorized intervention changes the challenge/response and recognition practice, with qualified practice where needed; subsequent peer use supports a narrow local result, not an isolated causal effect or whole-organization culture. OCE.12 supplies the contribution brief, role support, task feedback and debrief through several capable participants, including the manager who obtains time and the learning provider who owns the assessment.

OCE.11 accounts for learning, setup, extra review and debrief inside the supplied change allowance. An incident consumes the reserve and reduces change work; the displaced probe remains unperformed. A current retention/replacement result returned through OCE.16 and ME.6 is applied to the support interval and hand-back without another comparison. The pattern bodies provide the actions, numerical service example, stops and evidence limits. General reliability, customer benefit and enduring culture would require their own observations beyond this constructed case.

### Consequence comparison and authorized support revision

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

## APP-OCE-02 - Public hospital emergency-flow change

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
| Method return | `OCE.15` distinguishes implementation strategies and outcomes from patient, worker, and service results. |
| What fails or stops | PumpWorks cadence, product-team topology, release authority, and provider assumptions do not transfer. Verify clinical Work, authority, access, and patient benefit independently of a pathway description. |
| specialist return | Clinical safety, medical authority, labor, privacy, legal, public-governance, and Operations Management results are required where they change the decision. |
| Non-transfer boundary | OCE helps organize the change and formulate requests to qualified clinical, legal, labor, and service-continuity decision-makers. Those specialists supply the substantive judgments within their respective remits. |

## APP-OCE-03 - Distributed member-governed standards association

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
| Method return | OCE.15 records participation burden, authority gaps, and situation changes without treating member consultation as adoption or authority. |
| Simultaneous-change return | Suppose a credential-issuer change expects authorization from an incoming elected chair, while the election change expects new credentials before the ballot that establishes that chair. Under OCE.16, examine the supplied bylaws, current authority, credential evidence, ballot rules, and term windows to assess the claimed circular dependency. Use ME.6 to compare order/support arrangements and OCE.4 and OCE.6 to resolve contribution and enabling relations; obtain the bylaw-authority judgment from the association's authorized governance body. Return the resulting credential and authorization/order conditions to both changes. An expired term remains expired. |
| What fails or stops | Employer hierarchy, employee-only participation, and a single-company position or assignment model do not transfer. Missing required member, bylaw, employer, or provider authority blocks establishment or use of the dependent relation. |
| specialist return | Association governance, applicable law, publication, finance, and employer commitments remain separately owned. |
| Non-transfer boundary | Establish each organization's authority and commitments under its own rules. Use those conditions when designing and comparing organization relations and candidate change Methods across organizations. |

## APP-OCE-04 - OCE practice across a practitioner population

This constructed application concerns eight OCE practitioners across three organizations, not the working culture of one target organization. The population is not asserted to be one System. Supplied permitted case extracts, practitioner explanations, a shared source example and peer-recognition questions allow examination of one OCE.2 move: recovering actual contribution and receiving-decision relations.

The old “organization mapping” label is fading. Four observed cases still recover actual Work, evidence-return and decision relations under different titles. Two newer cases provide filled charts but do not recover the relevant crossing; their explanations do not yet close it. Two practitioners have no suitable permitted case in the period.

Using OCE.17, the group first separates three results: continued operative use in the four observed cases; a bounded gap to investigate in the two chart-only cases; and unobserved use for the two without opportunity. The group compares a usable crossing with the shared deficient example and finds that its recognition question rewards completed department boxes. This finding gives the group a reason to examine how the move is taught and how its use is recognized. It does not yet establish a sole cause or an individual capability deficit.

Within the case group's permission, a qualified facilitator and willing practitioners choose and perform a bounded case critique. They retain the usable local variants and replace the deficient example with a source-linked case and counterexample. In later peer feedback, they ask practitioners to show the contribution and decision relation that the recipient can use. A permitted later case opportunity is arranged where its owner can supply it. Any employment decision, qualified learning assessment, or evidence-access permission still requires its own authorized and qualified provider.

In the fictional follow-up, one practitioner independently recovers the crossing and receiving authority in a different case; another lacks permitted evidence access. The first is an observed later use, while the second is an access gap. These observations support neither causal attribution to training nor profession-wide retention.

Return the access question to the person or body responsible for granting it. Use HCD.3 only if distinguishing a human capability, misconception, or behaviour limit from an access or work-condition gap would change the next action. Return a specific reusable-Method defect to OCE.15/Method Engineering if the critique discovers one; correcting an example does not by itself call for a new Method variant. Use OCE.10 for working-culture questions about the target organization. OCE.17 gives the complete practice sequence and an unlike association case, including the relevant stop conditions.

# Framework Boundary and Refresh

## Intended use and ordinary non-use

Use this framework when an intended contribution requires deliberate change to an organization's relations or capability, or when such a change creates material consequences. Enter OCE.17 when the continuation or renewal of OCE practice among practitioners is the working question. Use one pattern or a small cooperating set.

Do not use it merely because Work occurs inside an organization, a manager makes a routine decision, an operating flow needs coordination, one person needs capability development, or a product requires engineering. Use the practice that owns that question; return a result to OCE only when an organization-change decision needs it.

## PatternID and reader order

`OCE.*` is the Organization Change Engineering PatternID namespace. Numbers are stable addresses, not steps. The Parts provide reader order. A dependency identifies a result needed for a particular use.

## Using the available Methods

This publication contains all seventeen pattern bodies. For the selected use, gather the required case observations, obtain professional contributions, verify authority and effective relations, and check which planned results have actually been realized. If a needed Method is not provided here or in an available sibling framework, obtain a qualified contribution or stop the dependent action.

## Pattern selection and result relations

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
| Which intervention can repair this participation or working-culture gap? | OCE.10 | Intervention matched to the qualified diagnosis and its bounded local consequences, or an unresolved competing explanation or gap | direct relation/learning owner; OCE.9, OCE.11 or OCE.12 where its result is needed |
| How can change and continuing service coexist? | OCE.11 | Authorized overlap, observed service/change consequences and hand-back, or deferral/stop | current ME.6, OPS.5–OPS.7, OCE.8/OCE.16 or the exact service/protection owner |
| Which leadership contribution is missing or dependent on one initiator? | OCE.12 | Performed contribution and tested continuation arrangement, or exact support gap | qualified learning provider, OCE.10/OCE.11, assignment/authority owner or OCE.15 |
| What changed, for whom and under which conditions? | OCE.13 | Qualified consequence comparison with conflicting results, competing explanations and gaps, or an observation plan | OCE.14, OCE.10/OCE.11, or the owner of the needed measurement, evaluation or affected-result judgment |
| Which organization relation should now be retained, repaired, replaced, reversed, stopped or investigated? | OCE.14 | Authorized disposition with effective scope, losses and remaining work; otherwise a proposal or authority request | OCE.6/OCE.9–OCE.12, later OCE.13, and OCE.16 only for an actual cross-change consumer |
| Which organization-change Methods are usable and worth developing? | OCE.15 | Named-use repertoire or domain candidate account | Method Engineering and the exact missing OCE result owner |
| Which other separately managed change uses the organizational condition now being altered? | OCE.16 | Qualified cross-change question, direct exit, or specific missing result; then return of the resolved condition to each affected change | ME.6, C.32.MWA, the applicable OCE/OPS/A.15 Method, or the specialist responsible for the needed decision or result |
| Which OCE practice continues across practitioners and work settings? | OCE.17 | Scoped continuation account, a retained practice variant, permitted intervention, or specific return, with later observation or a named gap | OCE.15/Method Engineering for a reusable-Method problem; applicable HCD or direct opportunity, authority and evidence owners |

Choose the next pattern from the result needed, not from a presumed lifecycle. OCE.13/OCE.14 can use a direct result without repeating a wider evaluation; OCE.17 can support retaining useful practice without a new intervention.

## Source use and currentness

### Guide source keys

These keys identify working Markdown guides by Anatoly Levenchuk consulted for this release on 2 September 2026. Use the linked texts and named sections to recover the conceptual argument. Establish local authority and performed-change claims from their own rules and evidence. A later Guide edit reopens only an OCE claim that depends on the changed content.

| Key | Source identity and discovery | Reading scope and qualification |
| --- | --- | --- |
| R5 | Руководство по системному мышлению — Guide to Systems Thinking | Maintained working text, especially R5.6:7.A, “Характеризация роли”. It distinguishes role and organization-position questions; it does not establish a local position, its institutional force or a holder's authority. |
| R7 | Руководство по методологии для инженеров-менеджеров — Guide to Methodology for Engineers and Managers | Maintained working text, especially R7.3:11; R7.5:13–15 and :19; R7.6:12 and :14. Recover operative Methods across words, carriers and practitioners; distinguish exposure, support, use and continuation. Culture analogies, popularity, hours and ranks supply no evidence of mastery or universal sequence. |
| R10 | Системный менеджмент — Systems Management | Maintained working text: R10.3:6 for roles/positions, R10.7:1–2 for project/process/case viewpoints, R10.5:7 for desired results and sacrificed alternatives, and R10.10:1–5 for leadership, authority, practical support and revision. The 2002 strategy/tactic-tree discussion is a historical anchor. Fixed rollout periods, compulsory software and one universal corporate owner are not imported; local authority and actual outcomes remain separate. |
| R11 | Развитие для развитых — Development for the Advanced | Working narrative developed from the 2026 seminar; R11.5:13–17 and R11.9:1, :7–8, :12–15 and :22–24 connect observations, several development scales, work-linked learning and later use outside direct supervisory control. The synthesis supplies neither an enacted intervention nor a universal duration, qualification ladder, transfer or effect claim. |

[R7](#guide-source-keys) helps recover a Method across different descriptions, instruments, practitioners, and variants while distinguishing it from performed Work and capability. [R10](#guide-source-keys) relates project, process, and case viewpoints on the same Work to assignments, participation, and development of organization capability. [R11](#guide-source-keys) connects learning, professional work, organization and platform development, and inquiry at different scales while distinguishing their results.

Each pattern's SoTA-Echoing section identifies the direct sources used for its moves, the retained contribution, and the source's limits. The summaries below highlight contributions that span several decisions or impose a significant reliance boundary.

For OCE.8, Naikar et al. and Waterson et al. contribute distributed sociotechnical and responsibility/recovery questions. Vaccaro et al.'s findings support comparison with the best applicable solo arrangement when synergy matters. NASA and Lagomarsino et al. contribute human/automation/robotic allocation and dynamic-reallocation questions. ISO 6385:2016 contributes ergonomic requirements and ISO 10218-1/-2:2025 industrial-robot safety requirements; check the editions and requirements applicable to the proposed work. The voluntary NIST AI RMF 1.0 contributes third-party, monitoring, incident, recovery, override, and change-management questions; check later revisions before relying on those contributions. Aksin and Masini plus Goth et al. bound shared-service configuration and cost claims. The local choice still needs authority and a whole-arrangement comparison, followed by separate provision and enactment evidence. Require a human in the loop only when the direct authority, safety, or performance basis warrants it.

For OCE.16, Kanitz et al. support inquiry into cross-initiative cognitive, normative, and procedural interference. Skov and Lê help distinguish a claimed inconsistency from established conditions. Rishani et al. distinguish membership, allocation, variety, informational benefit, and burden; Zhang et al. add participant-specific timing pressure. Martinsuo and Ahola challenge one-firm governance assumptions, while Fischer et al. supply a bounded portfolio alternative. Use these findings to formulate the dependency question. A portfolio Method remains one alternative. Test OCE.16 effectiveness with applicable evidence and make the local decision under current authority.

For OCE.9–OCE.12, Implementation Mapping and its 2025 review support cause-sensitive intervention with explicit limits; the 2025 CFIR guide supports inquiry into determinants, not an implementation procedure. The transfer, LOCI, and TeamSTEPPS sources connect qualified practice, feedback, workplace support, and concrete leadership contributions. Use the sociotechnical-prototype experiment to plan participant inspection; verify cooperation during actual Work. SRE examples help plan bounded exposure and recovery, but their software thresholds and trade-offs do not override the target domain's hard protection conditions. The bodies explain the alternatives, practical moves, and source limits. The constructed OCE cases illustrate those moves rather than establish their empirical effectiveness.

For OCE.17, the [NPT coding manual (2022)](https://doi.org/10.1186/s13012-022-01191-x) and [NPT-derived strategy synthesis (2025)](https://doi.org/10.1186/s13012-025-01444-5) contribute mechanism-sensitive inquiry and intervention candidates. The latter interprets 63 NPT-using health/social-care studies published through 2021, not comparative OCE effectiveness. The [2026 consolidation, version 1](https://doi.org/10.3310/nihropenres.14315.1), with two reviews approved with reservations, strengthens changing-context and burden questions; it supplies no general cultural-evolution or individual-learning proof. OCE.17 adapts these contributions to actual OCE case recognition, transmission, opportunity and later use.

For OCE.13/OCE.14, the [MRC update (2021)](https://doi.org/10.1136/bmj.n2061) contributes questions about the decision, context, stakeholders, and uncertainty. The [Magenta Book (May 2026)](https://www.gov.uk/government/publications/the-magenta-book/magenta-book-central-government-guidance-on-evaluation-html), especially §§2.2.1–2.2.2 and §3.4, supports proportionate evidence use and explanatory limits. OCE adapts these contributions from health-intervention research and government evaluation to the design of local comparisons. Obtain local measurements, qualify causal claims, and make organization-design and professional decisions separately. The bodies give the concrete comparisons, alternatives, and reopen conditions.

Refresh only the affected pattern or repertoire claim when a governing FPF distinction changes, a direct source changes practitioner action, a representative case defeats a branch, or use exposes a missing OCE move. A new publication alone does not reopen the framework.

## FPF dependency and compatibility

**Depended-on state.** This release relies on **First Principles Framework (FPF) - Core Conceptual Specification, Version August 2026**, status **Normative kernel, eternal alpha**, including the current pattern hosts used for this release. “Current FPF” inside a body refers to that source state; apply the compatibility rule below when a later host changes.

**Direct uses.** FPF supplies concepts and rules for System recognition, affected-System discovery, direct relations and selected structures, Work and WorkPlans, assignments and performers, capability, evidence, comparison, choice, Method identity and description, several-structure reconciliation, currentness, and culture mechanics. OCE applies these to organization-change situations, domain relations and Methods, participants, authority, consequences, and receiving results.

**Status-sensitive inputs.** C.32.MWA, A.15.8, and A.15.9 are Candidate hosts in the relied-on source state. OCE.16 can route a bounded question to them. Apply their stated candidate-use limits and obtain the actual result before using it in an organization-change decision.

**Compatibility.** A compatible FPF change leaves unaffected OCE results reusable. A changed relied-on kind, relation, Solution, or result form reopens only the consuming pattern and dependency claim.

**Dependency and contribution direction.** This release uses FPF's transdisciplinary concepts and rules. Return a transdisciplinary discovery to FPF and an organization-change-specific move to OCE. Propose a change of placement through the owning framework's decision; keep one authoritative definition of the moved content.

## Current Method Engineering dependency

The supplying product is the [Method Engineering Principles Framework, 2 September 2026](METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md). OCE.15 uses ME.1 for Method focus, ME.2 for named-use repertoire structure, ME.3 for situation criteria, ME.5 for individual qualification, ME.11 for trial, ME.13 for fit/transfer, ME.14 for worth, ME.15 for variants/provenance, and ME.16 for introduction/observation/revision.

OCE.16 uses ME.6 when Methods or candidate accounts can be co-used in materially different ways because of composition, Work order or overlap, allocation, subject/support arrangement, provider access, authority, evidence, burden, description, culture, or another selected structure. ME.6 can return a relation-only arrangement while the Methods remain unchanged. OCE.16 only discovers and qualifies a cross-change input before that comparison and returns its governed result afterwards.

OCE.9 and OCE.10 use ME.16 to obtain a needed Method-introduction result; OCE.9 retains organization realization and OCE.10 participation as its own question. OCE.11 obtains ME.6's qualified co-use result when its overlap question requires one and applies it without a second comparison. OCE.12 and OCE.15 return a leadership Method-account or repertoire question to the current Method Engineering result that answers it.

OCE.17 returns the actual practice problem, variant, case conditions and continuation evidence through OCE.15 when the reusable Method needs work. A cultural intervention does not itself qualify a Method variant, development intervention or transfer result.

OCE.15 supplies the Method Engineering work with domain-specific content: the organization-change result and intervention contribution, participants and affected Systems, decision-sensitive situation facts and changes, authority/capability/support/protection conditions, mechanism hypotheses, implementation outcomes, and organization results. OCE.16 supplies an account of the separately managed changes, altered organizational condition, consequential consumer action, interaction window, participant and evidence basis, and required return to each change. Use the supplying framework's [Table of Contents](METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#table-of-contents) to find the named Method and obtain its result.

Apply the supplying Method to qualify an OCE candidate or obtain the needed fit, trial, transfer, or variant result. Use local evidence for introduction, adoption, and effect claims, and establish authority for a cross-change arrangement separately. Reopen only the consuming OCE claim when a named ME result changes, becomes unavailable, or no longer answers the receiving use.

## Sibling-domain returns

Use Strategy for direction and commitments, Corporate Governance and the applicable legal practice for authority, Organization Administration for continuing provision, Operations Management for continuing Work, Human Capability Development for one person's capability development, and Systems Engineering for product/service engineering decisions. Obtain legal, safety, medical, ecological, labor, financial, and other professional judgments from qualified specialists. Check the available body or provider before relying on a specific result.

The supplied [Operations Management Principles Framework (preview)](README.md#development-previews) contains OPS.1–OPS.7. These Methods return bounded operating-scope, work-management, state, shared-attention, admission, case-continuation, and service-commitment results. For a constraint, capacity, portfolio, improvement, or continuing-service question not answered by those bodies, obtain the appropriate qualified contribution. OCE.11 coordinates a bounded change/service overlap using the actual service or OPS result; OCE.16 returns cross-change questions to the same direct owners.

The [Human Capability Development Principles Framework foundation slice, 1 September 2026 (preview)](README.md#development-previews) supplies HCD.1, HCD.3, and HCD.4: representative later-work demand, qualified target/non-training diagnosis, and a condition-qualified capability profile for one person. OCE.9/OCE.10/OCE.12 and OCE.17 use those results where applicable. Obtain learning design, practice, assessment, transfer, or retention results not supplied by that slice from a qualified direct provider. Use its Table of Contents to find the named body. Changed task or support conditions reopen the consuming result, not the whole framework.

The HCD source qualifies E.23.CAE's observation-first reference contrasts for HCD.3. The applicable HCD bodies and OCE.8:4.2 also qualify uses of E.23.CDI concerning the independently identified holder System, baseline and target capability, limiting contribution, protected conditions, and representative transfer evidence. CAE and CDI remain Candidate; use them within those receiving boundaries. OCE.17 requires the applicable HCD result and a separate System basis for any claim that its practitioner population is one capability holder.

The [Systems Engineering Principles Framework, 2 September 2026](SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md) provides SYSE.11 for a bounded System/configuration-use question. When application of SYSE.11 returns qualified integration evidence, OCE.9 can use that evidence, its limits, and fallback while establishing the organization contribution and participation relations separately. Open the supplying SYSE.11 body for its configuration/use conditions.

When the needed sibling result is available and current for the use, apply it within its scope. Otherwise obtain a qualified direct contribution or name the missing result and the OCE action that depends on it.

## Representative case coverage

The applications and related pattern-local cases are constructed examples of combined use. Keep each episode's supplied facts and unresolved conditions visible when following its continuation; the examples illustrate the Methods, not empirical results about real organizations or practitioners.

| Case | Useful comparison or move | Boundary for reuse |
| --- | --- | --- |
| [PumpWorks AI-inspection releases](#app-oce-01---pumpworks-weekly-ai-inspection-releases) | Connect design, assignment, and whole-arrangement comparison with OCE.15/OCE.16 Method and cross-change questions. Follow the separately conditioned OCE.9–OCE.12 continuation through a failed rehearsal, qualified practice, later use, participation intervention, service interruption, and peer leadership; then use OCE.13/OCE.14 for consequence comparison and support-allocation revision. | The initial quarterly baseline is outside the weekly OptionSet; the hybrid remains a recommendation and access remains ineffective in that episode. Later episodes supply their additional conditions. Release requires its own authorization, and the bounded observations establish neither general reliability nor enduring culture. Conflicting descriptive results supply no net-success or causal conclusion; missing protected coverage blocks the dependent repair, not the comparison. |
| [Public hospital emergency flow](#app-oce-02---public-hospital-emergency-flow-change) | Choose between a stable position and direct assignment, verify licensed holders, and compare whole clinician/provider/human–AI arrangements while care continues. Follow patient/worker protection, privacy/data, provider-continuity/exit, and structural-mismatch questions through realization, participation, and leadership. Examine case mix when comparing waiting times; a separate qualified safety result can support an authorized protective pause. | Obtain medical, legal, labor, privacy, provider-service, and clinical-safety judgments from qualified specialists. Competence, coverage, fatigue, protection, and recovery conditions precede patient-facing trial work. Admitted-case waiting observations do not establish benefit for diverted or unobserved patients; a protective pause needs its own authority. |
| [Distributed standards association](#app-oce-03---distributed-member-governed-standards-association) | Connect bylaw-governed assignment and the OCE.16 issuer/election dependency with amendment-packet preparation, asynchronous challenge, qualified translation and evidence use, accepted volunteer windows, and peer-facilitator learning. Consider a revision after the chair's authority expires. | Packet preparation is not adoption of a standard. Obtain Governance, ME.6, OCE.4/OCE.6, and professional results from their direct providers. Authority remains with bodies and office-holders established under association and employer rules; an expired term cannot support a new binding decision. A revision proposal remains a proposal until an authorized body or office-holder decides. |
| [OCE practitioner population](#app-oce-04---oce-practice-across-a-practitioner-population) | Recognize operative use despite changed labels; distinguish chart-only cases from missing opportunities; repair a source example and peer recognition, then examine mixed later observations. | No single holder System is claimed for the population. An observed later use, an access gap, a learning effect, and profession-wide retention require different evidence. |

## Publication boundary

The full pattern bodies are the working references for each Method's moves, conditions, evidence boundaries, stops, and specialist returns. Use the Readme, Preface, Table of Contents, and applications to find and combine the relevant patterns.

This framework presents organization-change Methods and their relations. Use an instructional Guide for sequenced learning and memory formation. The Engineering DPF Suite Reference supports cross-framework lookup.
