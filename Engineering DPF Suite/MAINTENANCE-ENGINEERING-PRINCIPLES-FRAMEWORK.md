# Maintenance Engineering and Management Principles Framework

Anatoly Levenchuk · First edition · 8 September 2026

Original framework content © 2026 Anatoly Levenchuk, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Third-party sources retain their own terms.


# Table of Contents

Search for the maintenance difficulty or result you need. Dependencies identify useful result relations, not a mandatory sequence.

## Public units

| Unit | Reader use |
| :--- | :--- |
| [Maintenance Engineering and Management Principles Framework Readme](#maintenance-engineering-and-management-principles-framework-readme) | Choose a direct maintenance question or the connected condition-to-result entry. |
| [Citation](#citation) | Cite the framework or one continuing pattern contribution. |
| [Preface](#preface) | Understand the language, its result relations, alternatives and limits. |
| [Cross-Pattern Applications](#cross-pattern-applications) | Follow PS17, the fleet comparison and shared-resource coordination. |
| [Source Responsibility and References](#source-responsibility-and-references) | Recover source contributions and their applicable limits. |
| [Framework Boundary and Refresh](#framework-boundary-and-refresh) | Understand scope, pattern continuity and action-changing refresh. |

**Part A - Maintained Use, Policy, Failure, and Condition**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [MNT.1 - Identify the Maintained System, Use, and Permission Boundary](#mnt1---identify-the-maintained-system-use-and-permission-boundary) | Draft | *Keywords:* equipment identity, required function, configuration, control. *Query:* "Which System and use does this maintenance question concern?" Bound the question and its operating and permission conditions. | FPF [A.1.SCR](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a1scr---finding-the-acting-or-changed-system), [A.2.8.PER](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a28per---granted-permission-exercise-and-non-prohibition); [SYSE.13](SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse13---establish-configuration-identity-variants-and-effectivity) |
| 2 | [MNT.2 - Select and Reopen the Maintenance Policy](#mnt2---select-and-reopen-the-maintenance-policy) | Draft | *Keywords:* maintenance policy, corrective, preventive, condition-based, failure-finding. *Query:* "Which task should be retained or changed for this failure?" Compare applicable tasks and response conditions without a technology ladder. | [MNT.3](#mnt3---establish-degradation-and-failure-evidence), [MNT.4](#mnt4---monitor-and-interpret-current-condition), [MNT.5](#mnt5---prepare-maintenance-service-capability-spares-tools-and-authority); FPF [C.11.DUA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11dua---decision-useful-advice-and-evidence-demands) |
| 3 | [MNT.3 - Establish Degradation and Failure Evidence](#mnt3---establish-degradation-and-failure-evidence) | Draft | *Keywords:* failure evidence, mechanism, cause, exposure, censoring. *Query:* "What does the failure history actually support?" Separate observation, diagnosis and consequence at the resolution needed by the decision. | [MNT.1](#mnt1---identify-the-maintained-system-use-and-permission-boundary), [MNT.4](#mnt4---monitor-and-interpret-current-condition), [MNT.12](#mnt12---maintain-maintenance-information-and-configuration-continuity); FPF [A.10](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a10---evidence-graph-referring-claim-bound-evidence-and-provenance-graph), [C.16](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c16---measurement-metrics-characterization-mmchr) |
| 4 | [MNT.4 - Monitor and Interpret Current Condition](#mnt4---monitor-and-interpret-current-condition) | Draft | *Keywords:* condition monitoring, alarm, baseline, forecast, remaining life. *Query:* "What does this signal mean under the actual operating conditions?" Return a qualified condition account or the precise interpretation limit. | [MNT.1](#mnt1---identify-the-maintained-system-use-and-permission-boundary), [MNT.3](#mnt3---establish-degradation-and-failure-evidence); FPF [C.16](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c16---measurement-metrics-characterization-mmchr) |

**Part B - Readiness, Intervention Choice, Coordination, and Protection**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 5 | [MNT.5 - Prepare Maintenance Service Capability, Spares, Tools, and Authority](#mnt5---prepare-maintenance-service-capability-spares-tools-and-authority) | Draft | *Keywords:* spare applicability, tools, competence, readiness, lead time. *Query:* "Can the selected maintenance task obtain usable support in time?" Establish task-specific readiness or its action-changing deficiency. | [MNT.2](#mnt2---select-and-reopen-the-maintenance-policy), [MNT.6](#mnt6---diagnose-condition-and-select-an-intervention); [SYSE.12](SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse12---develop-an-engineering-platform-for-practitioner-work); FPF [A.2.2](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a22---ucapability---system-ability-envelope-and-measures) |
| 6 | [MNT.6 - Diagnose Condition and Select an Intervention](#mnt6---diagnose-condition-and-select-an-intervention) | Draft | *Keywords:* diagnosis, repair, replace, defer, restriction, recommendation. *Query:* "What maintenance response is supported now?" Compare plausible interventions and finish sufficient advice without compulsory physical work. | [MNT.3](#mnt3---establish-degradation-and-failure-evidence), [MNT.4](#mnt4---monitor-and-interpret-current-condition), [MNT.5](#mnt5---prepare-maintenance-service-capability-spares-tools-and-authority), [MNT.7](#mnt7---coordinate-intervention-and-continuing-operation); FPF [C.11.DUA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11dua---decision-useful-advice-and-evidence-demands) |
| 7 | [MNT.7 - Coordinate Intervention and Continuing Operation](#mnt7---coordinate-intervention-and-continuing-operation) | Draft | *Keywords:* outage, service capacity, preparation, testing, restoration, contingency. *Query:* "Does the whole intervention fit the operating commitment?" Compare complete elapsed demand with the qualified service envelope. | [MNT.5](#mnt5---prepare-maintenance-service-capability-spares-tools-and-authority), [MNT.6](#mnt6---diagnose-condition-and-select-an-intervention); [OPS.10](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops10---qualify-capacity-under-variability) |
| 8 | [MNT.8 - Isolate, Make Safe, and Authorize the Intervention](#mnt8---isolate-make-safe-and-authorize-the-intervention) | Draft | *Keywords:* isolation, energy, protection, intervention permission, scope. *Query:* "What supports beginning this protected intervention?" Establish applicable actual protection and bounded authority, or return the unmet condition. | [MNT.1](#mnt1---identify-the-maintained-system-use-and-permission-boundary), [MNT.5](#mnt5---prepare-maintenance-service-capability-spares-tools-and-authority), [MNT.7](#mnt7---coordinate-intervention-and-continuing-operation); FPF [A.2.8.PER](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a28per---granted-permission-exercise-and-non-prohibition) |

**Part C - Performed Intervention, Functioning, and Return to Use**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 9 | [MNT.9 - Perform and Record the Maintenance Intervention](#mnt9---perform-and-record-the-maintenance-intervention) | Draft | *Keywords:* performed maintenance, deviation, interruption, actual parts, work record. *Query:* "What work actually occurred and in what resulting state?" Perform within operative conditions and preserve useful intervention evidence. | [MNT.6](#mnt6---diagnose-condition-and-select-an-intervention), [MNT.8](#mnt8---isolate-make-safe-and-authorize-the-intervention); FPF [A.13](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a13---the-agential-role-agency-spectrum), [A.15.1](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a151---uwork) |
| 10 | [MNT.10 - Verify Restored Functioning](#mnt10---verify-restored-functioning) | Draft | *Keywords:* restored function, representative load, verification, test limits. *Query:* "What required functioning does the evidence support?" Check the actual resulting configuration and return qualified functioning evidence. | [MNT.9](#mnt9---perform-and-record-the-maintenance-intervention); FPF [B.3](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#b3---trust-and-assurance-calculus), [A.10](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a10---evidence-graph-referring-claim-bound-evidence-and-provenance-graph), [C.16](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c16---measurement-metrics-characterization-mmchr) |
| 11 | [MNT.11 - Certify, Hand Back, and Authorize Resumed Use](#mnt11---certify-hand-back-and-authorize-resumed-use) | Draft | *Keywords:* hand-back, release, certification, control, resumed use. *Query:* "Who can resume which use of the returned System?" Reconcile functioning, state and applicable release conditions while transferring control. | [MNT.8](#mnt8---isolate-make-safe-and-authorize-the-intervention), [MNT.9](#mnt9---perform-and-record-the-maintenance-intervention), [MNT.10](#mnt10---verify-restored-functioning); FPF [A.2.8.PER](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a28per---granted-permission-exercise-and-non-prohibition) |

**Part D - Information, Programme, Methods, Simultaneous Work, and Culture**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 12 | [MNT.12 - Maintain Maintenance Information and Configuration Continuity](#mnt12---maintain-maintenance-information-and-configuration-continuity) | Draft | *Keywords:* maintenance history, serial unit, configuration, effectivity, event coding. *Query:* "Which history and description apply to this installed state?" Restore event and configuration continuity for the receiving decision. | [SYSE.13](SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse13---establish-configuration-identity-variants-and-effectivity); [MNT.3](#mnt3---establish-degradation-and-failure-evidence), [MNT.9](#mnt9---perform-and-record-the-maintenance-intervention) |
| 13 | [MNT.13 - Coordinate the Maintenance Programme and Fleet Learning](#mnt13---coordinate-the-maintenance-programme-and-fleet-learning) | Draft | *Keywords:* fleet, programme, failure rate, exposure, support, improvement. *Query:* "What does comparable fleet evidence warrant changing?" Return a qualified programme decision with its population and causal limits. | [MNT.2](#mnt2---select-and-reopen-the-maintenance-policy), [MNT.5](#mnt5---prepare-maintenance-service-capability-spares-tools-and-authority), [MNT.12](#mnt12---maintain-maintenance-information-and-configuration-continuity); FPF [E.23](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#e23---quality-improvement-loop-method) |
| 14 | [MNT.14 - Compare and Refresh Maintenance Methods](#mnt14---compare-and-refresh-maintenance-methods) | Draft | *Keywords:* Method comparison, predictive maintenance, practical worth, variant, refresh. *Query:* "Should this way of obtaining maintenance results be retained or replaced?" Compare the same use and whole burden, with conditional trials and useful retain decisions. | [MNT.2](#mnt2---select-and-reopen-the-maintenance-policy), [MNT.13](#mnt13---coordinate-the-maintenance-programme-and-fleet-learning); [ME.14](METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me14---evaluate-practical-worth-against-current-alternatives), [ME.15](METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me15---maintain-method-variants-provenance-and-reuse) |
| 15 | [MNT.15 - Reconcile Simultaneous Maintenance, Operation, and Support Work](#mnt15---reconcile-simultaneous-maintenance-operation-and-support-work) | Draft | *Keywords:* simultaneous work, shared specialist, overload, fallback, coordination. *Query:* "Why do individually feasible jobs fail together?" Resolve shared demands and moved burden at the whole-combination scope. | [MNT.5](#mnt5---prepare-maintenance-service-capability-spares-tools-and-authority), [MNT.6](#mnt6---diagnose-condition-and-select-an-intervention), [MNT.7](#mnt7---coordinate-intervention-and-continuing-operation); FPF [C.32.MWA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c32mwa---practice-architecture-synthesis-from-several-structures); [ME.6](METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me6---compare-method-architecture-alternatives-and-simultaneous-enactment-conflicts) |
| 16 | [MNT.16 - Deliberately Continue and Change Maintenance Culture](#mnt16---deliberately-continue-and-change-maintenance-culture) | Draft | *Keywords:* maintenance culture, transmission, enactment, recognition, retention. *Query:* "Is the practice actually being continued or changed?" Separate availability, actual use and effects, and select a supported continuation. | [MNT.13](#mnt13---coordinate-the-maintenance-programme-and-fleet-learning), [MNT.14](#mnt14---compare-and-refresh-maintenance-methods); FPF [C.36](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c36---cultural-evolution-and-cultural-evolution-engineering) |

# Maintenance Engineering and Management Principles Framework Readme

## Practical entries

Bring the maintenance question you actually need to answer. These are selected examples, not a catalogue or coverage boundary. If none fits, use the Table of Contents to find the relevant pattern directly. The pattern numbers are addresses, not an instruction to perform all sixteen Methods.

### MNT-POLICY — Retain or change a maintenance policy

- **Situation:** A recurring task or proposed technology lacks a convincing maintenance contribution.
- **Question:** Which task policy is appropriate for this failure and use?
- **First useful result or honest blocker:** A supported retain or change decision, or the failure or use condition that prevents one.
- **Start with:** [MNT.2](#mnt2---select-and-reopen-the-maintenance-policy); use [MNT.3](#mnt3---establish-degradation-and-failure-evidence) only where the failure account is inadequate.
- **Stop or return:** Stop when the policy question is answered. Reopen when failure behaviour, consequences or feasible response changes.

### MNT-CONDITION — Interpret an alarm

- **Situation:** A value, trend or forecast may change the maintenance response.
- **Question:** What does the current evidence support under this operating condition?
- **First useful result or honest blocker:** A qualified condition account or its precise measurement or interpretation limit.
- **Start with:** MNT.4.
- **Stop or return:** An adequate existing interpretation completes the request. Return to [MNT.6](#mnt6---diagnose-condition-and-select-an-intervention) when an intervention choice is wanted.

### MNT-RECOMMEND — Choose the present maintenance response

- **Situation:** A suspected fault has prompted a proposed repair.
- **Question:** What should be done now or at the next suitable opportunity?
- **First useful result or honest blocker:** A supported recommendation, selected intervention or exact unresolved choice.
- **Start with:** [MNT.6](#mnt6---diagnose-condition-and-select-an-intervention), using available failure and condition evidence.
- **Stop or return:** Finish sufficient advice now. Continue into preparation and protected work only when that intervention is selected.

### MNT-FLEET — Learn from maintenance history

- **Situation:** Fleet counts, recurring delays or programme results suggest a change.
- **Question:** What does comparable evidence warrant changing or retaining?
- **First useful result or honest blocker:** A qualified fleet account and programme decision, or the event/exposure mismatch preventing the comparison.
- **Start with:** [MNT.13](#mnt13---coordinate-the-maintenance-programme-and-fleet-learning); use [MNT.12](#mnt12---maintain-maintenance-information-and-configuration-continuity) for an answer-changing history contradiction.
- **Stop or return:** Retaining an adequate programme can finish the request. Select new inquiry only for a worthwhile attainable answer.

### MNT-METHODS — Keep or replace a way of working

- **Situation:** A maintenance Method or supporting tool may no longer fit.
- **Question:** Does another approach improve the same maintenance result at acceptable whole burden?
- **First useful result or honest blocker:** A retain, revise, replace, branch or stop decision with its conditions.
- **Start with:** MNT.14.
- **Stop or return:** Existing evidence can settle the comparison. A new trial is conditional on its contribution, feasibility and burden.

### MNT-CARD-01 — From a condition concern to the result actually needed

- **Situation:** A condition concern leads toward an intervention while operation must continue.
- **Question:** What can we answer now, and what governs any selected work and return?
- **First useful result or honest blocker:** Sufficient advice, or the specific condition limiting the next selected act.
- **Start with:** [MNT.1](#mnt1---identify-the-maintained-system-use-and-permission-boundary) or [MNT.6](#mnt6---diagnose-condition-and-select-an-intervention); continue through [MNT.5](#mnt5---prepare-maintenance-service-capability-spares-tools-and-authority), [MNT.7](#mnt7---coordinate-intervention-and-continuing-operation)–[MNT.11](#mnt11---certify-hand-back-and-authorize-resumed-use) only as the selected result requires.
- **Stop or return:** A recommendation can finish before repair. Actual work retains its protection, competence and permission conditions.

The requested question determines when the answer is sufficient. If an intervention is chosen, prepare its means and whole operating window, establish applicable protection and permission, perform and record the work, verify the required functioning and return control for the permitted use. Reopen a question when its conditions change.

PS17 shows the distinction. Existing evidence supports a bearing-replacement recommendation while a required spare applicability return is missing. Advice is complete; replacement cannot begin. When the extended intervention is selected and its conditions are met, the whole outage includes testing and hand-back, not just the repair.

The result may stop at a different point: a qualified condition interpretation, an infeasible time window, performed work awaiting a functioning result, or functioning evidence awaiting the relevant operating decision. Each return answers a different question; the corresponding direct patterns supply its reasoning.

## How to read and apply the framework

Use a pattern's Problem frame and Solution for the first working move. Its worked case shows the result and a consequential branch. Its checklist, source comparison and relations provide the further assurance and context needed for a more consequential use.

This first edition offers source-grounded guidance and constructed applications. It does not report field effectiveness of the integrated language or supply equipment-specific procedures. Competent practitioners and the applicable operating, engineering and protection sources remain necessary for actual equipment work.

## Citation

Cite: Anatoly Levenchuk, *Maintenance Engineering and Management Principles Framework*, first edition, 8 September 2026. For a particular contribution, add its PatternID and title. The framework was developed with AI-assisted authoring and review. The original text is reusable under the license above; cited third-party works are not relicensed by this publication.

# Preface

## The working problem and practical gain

A useful maintenance result connects knowledge of a System's condition to the functioning that someone needs. The practitioner may be an engineer choosing policy, a technician preparing an intervention, a planner coordinating access, an operator receiving control or a programme lead comparing fleet history. Their questions are related, but their results differ.

The name makes both engineering and management visible. Engineering includes failure interpretation, intervention choice and functioning verification. Management includes policy, service capability, information, programme, coordination and continuation of actual practice, not just scheduling or resource administration. Maintenance Engineering and Maintenance Management are both established expressions; the shorter engineering name also has broad uses. This framework's compound name makes its connected contribution explicit without dividing the sixteen Methods into two separate products.

An abnormal signal alone does not decide the response. The relevant failure may be uncertain, a suitable part may be unavailable, or testing and restoration may not fit the loss-of-service window. At fleet scale, raw counts can favour the wrong group. At practice scale, a revised manual can be available while the older Method remains in use.

The language helps readers make those connections without imposing a complete intervention-and-return sequence on every request. Its gain is a supported maintenance decision, feasible selected work and a truthful account of what can be used afterwards. A recommendation or a decision to retain an adequate policy can be that complete result. A stronger claim is withheld only by the limit that actually affects it.

The maintained subject is the functioning of Systems in use, especially physical and cyber-physical equipment under identifiable operating conditions. Maintenance includes preserving or restoring the required contribution and selecting its policies, support and programme. It interacts with engineering design, operation, organizational provision and asset management. A choice about an asset's continued use, renewal, replacement, repurposing or withdrawal retains its own value-oriented decision, as do a new service concept and a changed engineered design.

For one pump, selecting maintenance policy or an intervention to preserve or restore required functioning is a maintenance result. Comparing whether to continue its use or choose another asset option by value, costs, risks and service effects is an asset-management result, even for that single pump. Conversely, coordinating a fleet's maintenance programme remains MNT.13. A replacement may occur in either question; the verb, horizon, job title and number of assets do not decide the boundary. One case can need both contributions.

The adjacent Engineering Asset Management Principles Framework concerns engineered assets, asset Systems and portfolios. Related [Enterprise Asset Management](https://www.sap.com/resources/what-is-eam) terminology also includes substantial physical-asset, maintenance, information and cross-functional practice; it does not mean software alone. The two field expressions do not make every external source's scope identical. A particular receiving question identifies which asset-management contribution is needed. Asset existence and use over time are distinct from how engineering Work is organized; no universal sequence of engineering stages follows.

## Organizing the Methods around different results

The sixteen patterns are grouped into four publication Parts:

- Part A identifies the maintained use, chooses policy and interprets failure and condition through [MNT.1](#mnt1---identify-the-maintained-system-use-and-permission-boundary)–MNT.4.
- Part B makes a present response feasible and properly bounded through [MNT.5](#mnt5---prepare-maintenance-service-capability-spares-tools-and-authority)–MNT.8.
- Part C distinguishes performed intervention, restored functioning and return to use through [MNT.9](#mnt9---perform-and-record-the-maintenance-intervention)–MNT.11.
- Part D maintains information, programme learning, Method choice, simultaneous coordination and cultural continuation through [MNT.12](#mnt12---maintain-maintenance-information-and-configuration-continuity)–MNT.16.

These are navigation groups. They do not assert four stages of every job or one composite Method containing all sixteen contributions. Enter a Method where the question starts, using current adequate evidence or a qualified equivalent result. An unused sibling contributes no prerequisite.

A typical condition-to-intervention route starts with an interpreted condition from [MNT.4](#mnt4---monitor-and-interpret-current-condition) and a choice from MNT.6. Readiness from [MNT.5](#mnt5---prepare-maintenance-service-capability-spares-tools-and-authority) and operating coordination from [MNT.7](#mnt7---coordinate-intervention-and-continuing-operation) qualify feasible performance. [MNT.8](#mnt8---isolate-make-safe-and-authorize-the-intervention) establishes the protection and permission for the selected act. [MNT.9](#mnt9---perform-and-record-the-maintenance-intervention) then supplies evidence of work and actual configuration; [MNT.10](#mnt10---verify-restored-functioning) supplies the functioning result; [MNT.11](#mnt11---certify-hand-back-and-authorize-resumed-use) supplies hand-back and resumed-use permission. The route is conditional: it stops earlier when the requested result is already adequate.

Other questions use different connections. [MNT.12](#mnt12---maintain-maintenance-information-and-configuration-continuity)'s maintenance history supports [MNT.13](#mnt13---coordinate-the-maintenance-programme-and-fleet-learning) only where events and exposure are comparable. [MNT.14](#mnt14---compare-and-refresh-maintenance-methods) compares a Method's practical worth; [MNT.16](#mnt16---deliberately-continue-and-change-maintenance-culture) examines whether variants are transmitted and enacted in the practice population. [MNT.15](#mnt15---reconcile-simultaneous-maintenance-operation-and-support-work) handles common conditions that separate successful job decisions cannot establish.

## What the principal objects mean in practice

A maintained System is the equipment or other System whose contribution is at issue. A part is an actual constituent; a part number can describe many such individuals. A configuration is the relevant actual arrangement and values over an interval; a configuration description carries claims about it.

An observation says what was measured or inspected. A diagnosis explains the condition to the degree supported. A prognosis concerns future condition under stated assumptions. The maintenance choice uses these accounts but also considers feasible response and consequence.

A policy is the reusable selection of task and applicability conditions. A particular intervention decision selects a response now. A Method is a reusable way of obtaining a result; this framework's pattern prose explains those ways. A plan describes intended work, while the performed work and its effects require evidence of what occurred.

These distinctions matter where they change action. Ordinary equipment and maintenance language is enough elsewhere; a routine repair need not acquire an ontology form. FPF supplies the general recognition, evidence, comparison, permission and assurance Methods. MNT adds the failure, task, support, operating and restoration reasoning that those general contributions do not decide by themselves.

## Competing values and the whole-use constraints

Maintenance balances failure consequences with intervention burden and disturbance. Earlier detection is useful only if its interpretation and response can improve the result. More stock, inspection or data can help, but also consume resources or displace more valuable work. A programme decision includes whose downtime, effort and exposure are counted.

Two whole-use constraints are especially visible in the applications. [MNT.7](#mnt7---coordinate-intervention-and-continuing-operation)'s PS17 calculation accounts for the complete outage, including controlled testing, restoration and contingency. [MNT.15](#mnt15---reconcile-simultaneous-maintenance-operation-and-support-work)'s shared-specialist example compares the combined demand, not just each job's separate fit. Those sections carry the respective calculations; affected decisions return there instead of treating local approvals as proof of the whole combination.

Where a protective or administrative requirement is disputed, assess its merits as well as preserving its present force. Identify the protected party, relevant harm and evidence, the baseline and incremental protection, the full burden and displaced harms, and who can amend it. Harmful retention or tightening deserves the same scrutiny as harmful relaxation. The existence of a rule does not prove its proportionality; disagreement with it does not cancel its authority.

## Architectural Rationale

The language follows recurring differences in maintenance decisions. Policy is reusable across cases; diagnosis and intervention choice concern the present case. Support and operation can defeat a technically plausible repair. Protection governs a selected act. Intervention, functioning and permission produce different claims. History, fleet learning and practice continuation work across longer horizons and populations.

Collapsing these questions into “maintain the asset” would shorten the index but leave the practitioner to invent their connections. Turning them into one mandatory workflow would create a different failure: a sufficient recommendation would wait for part certification, an outage and release that the advice request never asked to perform. The conditional arrangement retains professional depth and useful early completion together.

A technology ladder from reactive through predictive to autonomous is also insufficient. Corrective maintenance can be appropriate for an obvious low-consequence failure; a hidden protective function can require failure-finding; a sensor can be technically impressive while its warning arrives too late for an available response. The policy and Method comparisons therefore retain plural alternatives at the actual use and burden.

A maintenance taxonomy is useful for finding omitted topics, but it does not tell the reader how to obtain a supported result. GFMAM and IAM contribute breadth and neighbouring boundaries. The domain Methods transform those concerns into decisions about failure, response and continuity.

Systems Engineering contributes configuration and enabling-arrangement results. Operations contributes capacity and work-management results. Method Engineering contributes general practical-worth and variant comparisons. Their presence does not settle maintenance-specific policy, diagnosis or restoration. Conversely, MNT does not take over the investment, service-design or general administration decisions of its neighbours.

This arrangement has a cost: users sometimes need to reconcile several qualified results. It is worth that cost when the distinctions prevent an incorrect maintenance or operating decision. A direct equipment procedure or an already adequate specialist answer is preferable when it fully answers the current question. A specialist profile may be preferable when a jurisdiction or equipment family needs substantially different authoritative content.

## Applying and checking the whole language

Begin by asking what the recipient needs now. Reuse enough identification and evidence to answer that question; select more work only when it can change the answer or satisfies an operative requirement. Continue into physical intervention only when that work is selected and its conditions are met.

At whole-language scale, ask whether the chosen Methods actually supply the required result and whether their outputs concern compatible subjects, configurations, operating conditions and horizons. Check any shared resource or service constraint at the scope of the whole combination. Preserve the distinction between what was proposed, performed, observed and permitted.

The direct checklists ask questions about their own result. They are not sixteen mandatory forms. If a recommendation is the request, the supported advice and its action-changing limits complete it. If the selected result is an actual return to service, its applicable protection, functioning and permission conditions remain real.

The main text-invited mistakes are reading the Parts as stages, treating a closed work order as restored service, taking a prediction score as maintenance value and mistaking a published Method for its adoption. The relevant corrections are embedded in [MNT.6](#mnt6---diagnose-condition-and-select-an-intervention), [MNT.9](#mnt9---perform-and-record-the-maintenance-intervention)–[MNT.11](#mnt11---certify-hand-back-and-authorize-resumed-use), [MNT.14](#mnt14---compare-and-refresh-maintenance-methods) and [MNT.16](#mnt16---deliberately-continue-and-change-maintenance-culture) rather than delegated to a generic warning.

## Assumptions, costs and limits

The principal examples concern industrial equipment and draw some bounded protection and human-performance lessons from aviation. They do not establish a universal transfer to software services, nuclear facilities or every other maintenance setting. An application needs the equipment's failure and operating basis and its actual current protection rules.

The language favours explicit supported claims. That can reveal an uncertainty that an informal plan concealed. It can also save investigation or paperwork when a smaller answer is sufficient. Its expected contribution is better maintenance reasoning and fewer unsupported transitions, not a guaranteed decrease in failures, cost or exposure.

All application names, observations, quantities and outcomes in this edition are constructed. They make the reasoning inspectable; they are not evidence that the framework has improved an actual plant. A measured-effect claim requires its own population, comparator, observation and causal basis.

## Shared source synthesis and useful neighbours

The selected line combines mechanism-sensitive task choice, evidence interpreted for its receiving decision, feasible support and action-specific protection. The serious alternatives are taxonomy-only guidance, technology ranking and task-completion-only control. The patterns show the particular differences in action and the limits that the selected line preserves.

The professional sources shape this synthesis selectively. Their claims are not copied as complete procedures or universal optima. A research model's gain remains bounded to its assumptions; a regulator's text remains bounded to its jurisdiction and scope. The source account below gives direct returns, inspected scope and the change that should prompt reconsideration.

The strongest common contributions are already available in FPF: [A.1.SCR](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a1scr---finding-the-acting-or-changed-system) for System recognition; [A.10](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a10---evidence-graph-referring-claim-bound-evidence-and-provenance-graph) and [C.16](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c16---measurement-metrics-characterization-mmchr) for evidence and measurement; [C.11](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11---decision-theory-decsn-cal) and [C.11.DUA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11dua---decision-useful-advice-and-evidence-demands) for comparison, advice and evidence demands; [A.2.2](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a22---ucapability---system-ability-envelope-and-measures) for capability; [A.2.8.PER](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a28per---granted-permission-exercise-and-non-prohibition) for permission; [B.3](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#b3---trust-and-assurance-calculus) for assurance; [E.23](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#e23---quality-improvement-loop-method) for improvement; [C.32.MWA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c32mwa---practice-architecture-synthesis-from-several-structures) for a needed cross-structure synthesis; and [C.36](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c36---cultural-evolution-and-cultural-evolution-engineering) for cultural relations. MNT uses their results where needed rather than requiring their complete records at every entry.

The supporting DPF results have concrete receiving uses. [SYSE.12](SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse12---develop-an-engineering-platform-for-practitioner-work) helps develop the enabling arrangement consumed by MNT.5. [SYSE.13](SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse13---establish-configuration-identity-variants-and-effectivity) supplies the identity and effectivity basis used by MNT.12. [OPS.10](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops10---qualify-capacity-under-variability) supplies qualified capacity used in MNT.7. [ME.6](METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me6---compare-method-architecture-alternatives-and-simultaneous-enactment-conflicts) supports a real cross-structure conflict in [MNT.15](#mnt15---reconcile-simultaneous-maintenance-operation-and-support-work), while [ME.14](METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me14---evaluate-practical-worth-against-current-alternatives) and [ME.15](METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me15---maintain-method-variants-provenance-and-reuse) support practical-worth and Method-variant questions in MNT.14. These result exchanges do not require reading every sibling edition first.


# Part A - Maintained Use, Policy, Failure, and Condition

## MNT.1 - Identify the Maintained System, Use, and Permission Boundary

> **Type:** Method
> **Status:** Draft

### MNT.1:1 - Problem frame

Use this pattern when a maintenance request names equipment but leaves unclear what must keep working, in which configuration, for whom or under whose control. A planner asked to “fix PS17” needs a sufficiently bounded question before choosing a task or promising an outage.

Identify the maintained System, its required use and the decisions that control access and return to operation. The first useful result is a question that the maintenance practitioner and the receiving operator understand alike. If those values are already clear and adequate, use them directly. Selecting a replacement bearing belongs in [MNT.6](#mnt6---diagnose-condition-and-select-an-intervention); changing the plant's service concept belongs with the responsible engineering and operating decisions.

### MNT.1:2 - Problem

A stock number identifies a replaceable part, an equipment tag identifies a unit and an operating commitment identifies a required contribution. They answer different questions. Repairing the tagged unit can still leave the required service unavailable when a shared controller, cooling supply or bypass is outside the assumed boundary.

Unclear control makes the same mistake consequential: the person requesting a recommendation may be unable to stop the equipment, authorize intrusive work or accept restricted operation. Knowing that distinction early prevents a recommendation from becoming an unsupported commitment to act.

### MNT.1:3 - Forces

A narrow boundary keeps the question answerable, but omitting a shared dependency can make the answer unusable. A broad inventory may reveal more equipment while delaying the urgent decision. Required functioning also varies with load, season and time horizon; a configuration adequate for reduced summer demand may be inadequate for peak demand. The useful boundary includes what changes this maintenance answer, not everything connected to the machine.

### MNT.1:4 - Solution

Begin with the requested result: condition interpretation, policy choice, intervention recommendation, actual repair, functioning evidence or return to use. Ask what decision will consume it and by when. This often resolves apparent disagreement: the engineer can finish advice today although the repair remains unready.

Locate the actual unit and maintenance-relevant configuration. Reconcile its tag with installed constituents and applicable descriptions only where a difference could change the answer. For a bearing decision, the actual bearing arrangement and shaft assembly matter; an unrelated cabinet-label discrepancy may not. Preserve an unknown configuration as unknown until it is resolved for a use that needs it.

State required functioning as an observable contribution under an operating envelope. For example, “circulate heating water for the east district at the agreed seasonal flow and pressure” is more useful than “pump healthy.” Include the horizon, permissible loss of service and any qualified fallback. Obtain those operating values from the responsible operation; maintenance does not invent a capacity allowance.

Then trace the few interactions that can change the decision. A shared electrical supply can prevent simultaneous isolation; a standby pump can preserve service only if it is actually available under the same conditions. Identify affected people and other Systems when their exposure, access or service loss changes the alternatives.

Recover control at the point where it matters. Establish who can request and receive advice, permit access, stop operation, authorize the proposed intervention and resume use. One person may hold several of these roles, but possession of one authority does not establish the others. For an advice-only request, resolve only authority questions that constrain the recommendation or its interpretation.

Return the bounded question in the existing work discussion or record. A useful concise form is: “For this unit and configuration, under this required use and horizon, decide this maintenance question; this operating limit and this unresolved fact can change the answer.” A separate inventory or new form is unnecessary when the current record already supplies those values.

For a consequential reliance claim, inspect the identity evidence, operating-source applicability and actual permission basis. Recognition of the right equipment is a lighter claim than assurance that a proposed act is permitted. A disagreement about the merits of a requirement belongs in a separate appraisal under [C.11.DUA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11dua---decision-useful-advice-and-evidence-demands); it does not silently alter present authority.

### MNT.1:5 - Archetypal Grounding

In the constructed PS17 case, the request on 18 September 2026 concerns PumpTrain-PS17-B in configuration C41. Its bearing vibration is rising. DistrictHeatingOperation-East can tolerate the agreed reduced-capacity state for four hours; the operating capacity result supplies the applicable demand and standby assumptions.

The first question is “Should we recommend a bearing replacement at the next suitable outage?” It is not yet “May we dismantle the bearing now?” The planner identifies the installed bearing arrangement and retains the specialist applicability return needed for a replacement. The operating controller retains the stop and resume decisions.

This boundary permits a supported recommendation while the replacement-part return is outstanding. If the standby train later becomes unavailable, the four-hour allowance is no longer usable on its earlier basis. The recommendation's service assumptions and scheduling branch reopen; an unrelated equipment inventory does not.

For a small noncritical fan with an unambiguous tag, known function and a currently applicable work procedure, the existing identification can be enough. Rebuilding the whole plant's asset hierarchy adds no value to that task.

### MNT.1:6 - Bias-Annotation

Equipment registers favour named, owned assets. Shared utilities, contractor access, operators and people affected by loss of service can be less visible. Follow the actual consequence and control relation when it changes the question, even if the relevant party has no row in the maintenance database.

### MNT.1:7 - Conformance Checklist

For the requested use, can the recipient identify the actual maintained unit and the configuration distinctions that affect the answer? Is required functioning tied to the relevant operating envelope and horizon? Are material service dependencies and loss allowances supported? Are access, intervention and resumed-use authorities distinguished where they change the next act?

An adequate existing answer closes this identification task. These questions do not require a complete inventory, a new permission record for advice or examination of unaffected constituents.

### MNT.1:8 - Common Anti-Patterns and How to Avoid Them

“Fix asset 204” leaves the required service unstated. Recover what the unit must contribute before treating a component-level success as the answer. Conversely, expanding a bearing question into an enterprise-wide asset study postpones the useful result; include only answer-changing dependencies.

A requester's urgency can also be mistaken for operating authority. Return the recommendation to that requester while obtaining any actual intervention decision from its proper holder.

### MNT.1:9 - Consequences

The maintenance practitioner can direct evidence and effort toward the same use that the operator needs. The cost is a small amount of boundary reconciliation, sometimes revealing that the question cannot yet be answered as phrased. A bounded recommendation remains useful even when an operating or permission limit blocks the proposed work.

### MNT.1:10 - Architectural Rationale

Function, configuration and control are identified together because each can invalidate the same apparently sensible repair. Making them one entry Method is less costly than diagnosing the wrong unit and correcting the plan later. It does not make this entry compulsory: direct condition, policy or fleet questions can start from already adequate identification.

Maintenance retains the function-in-use question. Broader investment, disposal and service redesign remain decisions of their own practices.

### MNT.1:11 - SoTA-Echoing

The practice question is which boundary makes maintenance advice useful. This pattern adapts the function-and-maintenance-regime relationship in IAM's 2024 *Anatomy of Asset Management*, §7.7.5, and uses [SYSE.13](SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse13---establish-configuration-identity-variants-and-effectivity) for configuration identity. Against a register-only starting point, its exact change is the required-use and control reasoning in the Solution and PS17 case. It accepts a small identification cost to avoid a wrong-subject or wrong-service answer. IAM's broader discipline does not become this pattern's scope. Reopen the boundary when a changed use, installed configuration or shared dependency changes the maintenance decision. See [IAM's account](https://theiam.org/media/5615/iam-anatomy-version-4-final.pdf).

### MNT.1:12 - Relations

[MNT.2](#mnt2---select-and-reopen-the-maintenance-policy) uses the bounded functioning question to select a policy; [MNT.3](#mnt3---establish-degradation-and-failure-evidence) and [MNT.4](#mnt4---monitor-and-interpret-current-condition) use it to interpret failure and condition. [MNT.8](#mnt8---isolate-make-safe-and-authorize-the-intervention) and [MNT.11](#mnt11---certify-hand-back-and-authorize-resumed-use) develop the action-specific permission and return-to-use results. FPF [A.1.SCR](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a1scr---finding-the-acting-or-changed-system) supports System recognition, [A.2.8.PER](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a28per---granted-permission-exercise-and-non-prohibition) supports permission and [SYSE.13](SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse13---establish-configuration-identity-variants-and-effectivity) supplies configuration identity and effectivity. [OPS.10](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops10---qualify-capacity-under-variability) supplies an operating capacity result when the maintenance question consumes it.

### MNT.1:End

## MNT.2 - Select and Reopen the Maintenance Policy

> **Type:** Method
> **Status:** Draft

### MNT.2:1 - Problem frame

Use this pattern when a recurring maintenance task, inspection interval or proposed technology needs a reason to be retained or changed. A calendar says “replace every year,” but the planner cannot explain which failure this prevents or why a different task would be worse.

Choose a reusable maintenance policy for the identified functioning and failure situation. Here a policy states which task applies and under what condition it is performed. The first result can be a justified decision to retain the current policy. A one-off response to today's condition belongs in [MNT.6](#mnt6---diagnose-condition-and-select-an-intervention); a fleet-wide support and work decision belongs in MNT.13.

### MNT.2:2 - Problem

Task frequency and technical sophistication are poor substitutes for policy reasoning. An age-based replacement may remove a wear-related failure, do little for a largely age-independent fault or introduce a new installation fault. A sensor may observe degradation without leaving enough time to obtain a part and act.

A policy therefore needs a credible connection between failure behaviour, what the task can change, the consequence of waiting and the practical burden of intervention.

### MNT.2:3 - Forces

Prevention can avoid an expensive failure but consume useful component life and introduce disturbance. Frequent inspection can shorten detection delay while consuming access and interpretation effort. Keeping stock shortens response time but ties up resources and can leave obsolete parts. Hidden protective functions create a different trade-off from failures that operation immediately notices. Compare these consequences within the maintained use; do not reduce every value to downtime alone.

### MNT.2:4 - Solution

Start from the required function and a failure account sufficient to distinguish policy alternatives. Identify the loss of function, credible mechanisms and consequences. When one policy covers several mechanisms, check each mechanism that could justify a different task. Retain uncertainty where it matters rather than inventing a lifetime distribution from sparse events.

Construct the plausible task alternatives. The following distinctions help select a task; they are not a ladder of maturity.

| Task family | What can make it useful | What can defeat it |
| --- | --- | --- |
| Corrective or deliberate run-to-failure | Failure is detectable and its consequence, recovery demand and collateral effects are acceptable for the use. | A hidden protection loss, unacceptable exposure or unavailable recovery capability makes waiting untenable. |
| Age- or usage-based action | Failure behaviour and restoration effectiveness support acting before a relevant age or usage condition. | Calendar age is a weak predictor, or replacement repeatedly introduces faults. |
| Condition-based action | An observable condition changes early enough to support a useful response. | The relevant failure is not detected, the alarm is unreliable, or response lead time exceeds the usable warning. |
| Failure-finding | A task reveals loss of a function that normal operation does not expose, such as a standby protective function. | The test misses the relevant failure or creates unacceptable exposure without adequate controls. |
| Opportunity-based combination | Shared access or downtime makes coordinated tasks worthwhile. | Bundling consumes useful life, creates interference or overcommits the outage. |

For each credible alternative, explain what performing the task changes. Include imperfect repair, task-induced defects and residual failure modes when material. If no acceptable maintenance action addresses a serious failure, return the specific redesign, redundancy or changed-use question to engineering or operation. Adding inspections that cannot reveal or alter the failure is not a substitute.

For condition-based work, reason across the complete response. The usable interval between detectable degradation and unacceptable functioning must accommodate detection delay, interpretation, obtaining support, access and the selected intervention, with uncertainty appropriate to the consequence. This is an applicability question, not a universal formula for a safe interval. A local detection threshold or interval needs the equipment and operating evidence that supports it.

Compare alternatives using the receiving use's relevant values: loss of service, exposure, labour, material, disturbance, environmental effects and uncertainty. Use comparable operating horizons and state deliberately accepted trade-offs. Existing adequate evidence may already settle the choice. Select further investigation only when an attainable answer could change it enough to justify acquisition, interpretation, delay and displaced work.

State the chosen policy in actionable terms. Name the applicable population or configuration, task, trigger or interval basis, relevant support assumptions, response to an out-of-scope condition and the evidence or changed use that would reopen it. Where an operative requirement fixes a task, preserve its current force. A separate merits appraisal may support a request to the authorized rule holder; it does not authorize unilateral relaxation.

### MNT.2:5 - Archetypal Grounding

For PS17, the constructed condition history supports a bearing-related deterioration concern. The team retains a condition-informed policy for this failure family because the interpreted signal can support a planned response in the stated use. The present recommendation still depends on actual support and access; an alarm alone does not establish that replacement can fit the next outage.

Consider instead a cheap, accessible indicator lamp whose failure is obvious and has no protection role. If its loss and replacement demand are acceptable, deliberate run-to-failure can be a sound policy. Scheduling repeated intrusive replacement needs an additional gain to justify its burden.

The same choice is unsuitable for an otherwise unobserved protective trip function. Normal production can continue while that function has failed. A suitable failure-finding task addresses that detection problem; an operator's observation that “the line still runs” does not. The applicable specialist basis determines the test and interval.

In the 48-pump fleet example, the operating exposures differ, and policy selection is not randomized. Four failures versus six do not by themselves justify replacing the policy. Retain the current policy when its existing failure-and-response basis remains adequate; address the known spare-support deficiency on its own existing evidence. Failure to prove a better rival does not establish that the current policy is adequate.

### MNT.2:6 - Bias-Annotation

Breakdowns are conspicuous; unnecessary preventive work and failures introduced by maintenance can disappear into ordinary cost codes. Include those consequences in a comparison. A vendor's technology categories can also favour its own sensor or software offering over a simpler adequate task.

### MNT.2:7 - Conformance Checklist

Does the policy address a stated functioning loss and credible failure behaviour? Can the selected task detect, prevent, mitigate or restore the relevant failure in time? Are consequence, support and task-induced effects considered where they distinguish the alternatives? Is the chosen applicability and trigger usable by the intended practitioner?

A retain decision can close the question. New trials, a complete failure model and numerical optimization are warranted only when their obtainable contribution changes this choice.

### MNT.2:8 - Common Anti-Patterns and How to Avoid Them

“Predictive is better than preventive” ranks technology without the failure and response conditions. Compare what each arrangement can actually change. “We have always replaced annually” conceals the interval's basis; recover that basis and reopen only the unsupported choice.

A protective function that has never been demanded can appear failure-free. Examine how its failed state would be detected before choosing run-to-failure.

### MNT.2:9 - Consequences

The chosen task has an explicit maintenance contribution and a useful reopen condition. Some existing work can be retained; some unnecessary work can stop through the applicable decision. Where no task provides an acceptable answer, the Method makes the engineering or operating problem visible instead of disguising it as a maintenance backlog.

### MNT.2:10 - Architectural Rationale

A reusable policy differs from a current intervention choice: one establishes when a task generally applies, while the other resolves a present case. Keeping them related but separate permits a valid policy to coexist with an exceptional current response.

The task alternatives remain plural because failure visibility, mechanism, consequence and support differ. A single escalating technology sequence would discard legitimate corrective and failure-finding policies.

### MNT.2:11 - SoTA-Echoing

For the question “Which task is worth performing for this failure?”, this pattern adapts the applicable/effective task reasoning of NASA's historical 2008 RCM guide and the mechanism-plus-decision-model line discussed by Arts and colleagues in 2025. It rejects a technology ladder as the policy rule: the comparison table and complete-response reasoning preserve corrective, hidden-function and support-limited cases that the ladder obscures. More demanding models remain useful when their decision gain warrants their effort. Neither source supplies a universal interval or permission rule. Reopen when failure behaviour, warning time, restoration effectiveness or the operating consequence changes. See the [RCM task discussion](https://www.nasa.gov/wp-content/uploads/2023/06/nasa-rcmguide.pdf) and [maintenance optimization account](https://orbilu.uni.lu/bitstream/10993/61558/1/1-s2.0-S0377221724005241-main.pdf).

### MNT.2:12 - Relations

[MNT.3](#mnt3---establish-degradation-and-failure-evidence) supplies failure evidence and [MNT.4](#mnt4---monitor-and-interpret-current-condition) supplies condition interpretation. [MNT.5](#mnt5---prepare-maintenance-service-capability-spares-tools-and-authority) and [MNT.7](#mnt7---coordinate-intervention-and-continuing-operation) qualify response feasibility; [MNT.6](#mnt6---diagnose-condition-and-select-an-intervention) selects the present intervention. [MNT.13](#mnt13---coordinate-the-maintenance-programme-and-fleet-learning) uses policy consequences across a fleet and [MNT.14](#mnt14---compare-and-refresh-maintenance-methods) compares Method changes. FPF [C.11](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11---decision-theory-decsn-cal) supports comparison, and [C.11.DUA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11dua---decision-useful-advice-and-evidence-demands) governs a disputed evidence demand or requirement appraisal.

### MNT.2:End

## MNT.3 - Establish Degradation and Failure Evidence

> **Type:** Method
> **Status:** Draft

### MNT.3:1 - Problem frame

Use this pattern when a fault code, alarm or repair history leaves the mechanism or consequence needed for a maintenance decision unclear. “Bearing failure” may describe an observed damaged part without explaining whether lubrication, alignment, contamination or another condition changes the next policy or intervention.

Establish a qualified failure account for the receiving question. The result connects observed departures from required function with the causes and consequences that current evidence supports. [MNT.4](#mnt4---monitor-and-interpret-current-condition) interprets a current measurement or trend; [MNT.6](#mnt6---diagnose-condition-and-select-an-intervention) uses a failure account to choose the present response. A complete root-cause inquiry is unnecessary when remaining explanations lead to the same adequate answer.

### MNT.3:2 - Problem

Observation, diagnosis and consequence are easily collapsed. A high vibration value is an observation under particular measurement conditions. A damaged bearing is a condition claim. A lubrication mechanism is a causal explanation. Loss of district-heating service is a possible System-level consequence. Evidence supporting one does not automatically support the others.

Maintenance history adds another ambiguity: a removed component may have failed, been replaced preventively or been removed because another fault was suspected. Counting all removals as failures can change a policy for the wrong reason.

### MNT.3:3 - Forces

Detailed inquiry may discriminate mechanisms, but it consumes access, specialist time and potentially destructive examination. Early restoration may destroy useful evidence; preserving every part indefinitely may also be wasteful. Sparse failures favour physical reasoning, while confident causal stories can ignore contradictory observations. The required resolution is determined by the decision the evidence must support.

### MNT.3:4 - Solution

State the functioning question and the failure claim that would change the decision. Separate a complete loss, degraded contribution and loss of a protective function. Define the event sufficiently for another reader to distinguish it from an inspection finding or preventive removal.

Recover available evidence at its actual scope. For a physical component, this can include operating conditions, measurements, photographs, inspection returns, installation and removal facts, applicable configuration and the sequence of earlier work. Preserve when and how observations were obtained. An occurrence reconstructed from an operator's report has a different evidential limit from a directly inspected fracture surface.

Build the smallest useful causal account. Connect the required function to the observed departure, candidate mechanism, local effect, System effect and consequence. A short table can keep alternatives visible:

| Candidate explanation | Observation it explains | Evidence that could change the maintenance choice |
| --- | --- | --- |
| Bearing damage | A supported bearing-related signal or physical finding | The specialist interpretation and applicable component inspection. |
| Alignment or installation problem | A change associated with installation or operating load | Existing alignment and installation records, or a justified discriminating check. |
| Measurement or operating-context change | A discontinuity matching sensor, speed or load change | Comparable measurement conditions and instrument information. |

These are example hypotheses, not a diagnostic rule for all pumps. Include a different mechanism when the actual evidence makes it consequential.

Distinguish what is supported, what remains plausible and what is contradicted. Do not turn a possibility into a cause by placing it in a fault-tree box. Where several explanations support the same immediate recommendation, return that recommendation's evidential basis and leave the stronger causal claim unresolved. Where the alternatives require different actions, identify the smallest attainable observation that could discriminate them.

For population claims, recover the denominator and observation process. Operating hours, starts, cycles, calendar exposure and units under observation answer different questions. A unit still operating at the end of observation has a known survival interval, not a known eventual lifetime. A preventive removal ends or changes that component's exposure; an overhaul may not restore it to an as-new state. Treat those distinctions explicitly before fitting or comparing a failure model.

When selecting an investigation, compare its obtainable contribution with the whole burden. Include the effect of delay, disturbance, specimen preservation and specialist interpretation. A low-value inquiry can stop while an adequate maintenance answer remains available. If a claim has high consequence, use the applicable evidence and assurance rules for that claim; more records alone do not establish it.

Return a failure account whose uncertainty changes action where necessary. Preserve evidence needed by a real later decision in the maintenance history. State a reopen condition, such as recurrence under a supposedly corrected condition or a newly inspected part contradicting the diagnosis.

### MNT.3:5 - Archetypal Grounding

In the constructed PS17 case, the available specialist interpretation and comparable condition history support recommending bearing replacement at a suitable outage. They do not establish why the degradation arose or whether a recurring programme-level defect has been eliminated.

The planner can therefore give the recommendation now. If the selected intervention exposes material damage, the team preserves the observations needed for the relevant later cause question. It does not claim a lubrication cause merely because the bearing is replaced.

The 48-pump example exposes a different error. Group A has four relevant failure events in 20,000 operating hours; group B has six in 56,000. The comparable crude event rates are 0.20 and approximately 0.107 per 1,000 hours. The first group has fewer events but a higher exposure-adjusted rate. Neither comparison proves a causal policy difference: operating conditions, component histories, event coding and selection may differ.

If two of the six records are preventive removals, even that crude rate needs correction before use. The useful result is a qualified failure account and the exact coding contradiction, not an automatically fitted lifetime distribution.

### MNT.3:6 - Bias-Annotation

The part found damaged at dismantling can attract all causal attention even when an upstream condition produced its damage. Work-order codes can favour the easily named component over installation, operating or maintenance-induced causes. Check those alternatives only where they can change the receiving answer.

### MNT.3:7 - Conformance Checklist

Can the reader distinguish the required functioning, observed departure, diagnosis and consequence? Does each decision-bearing causal claim have usable evidence? Are unknown or competing explanations retained at their actual strength? For a population claim, do event definitions, exposures and observation limits support the comparison?

The requested account is complete when it supports the receiving maintenance decision or identifies its exact evidential limit. It need not resolve every possible root cause.

### MNT.3:8 - Common Anti-Patterns and How to Avoid Them

A failure code becomes a mechanism when the record never established causation. Recover the observation and explain the inference. A list of removed parts becomes a failure count when preventive removals are silently included. Recover event meaning and exposure before comparing groups.

An open recurrence question can also be treated as a reason to withhold an already supported local recommendation. Separate the recommendation's claim from the stronger explanation that remains unresolved.

### MNT.3:9 - Consequences

Policy and intervention decisions can use evidence at a defensible resolution. Some inquiries become narrower; others stop because they would not change the answer. The remaining cost is preserving enough provenance and uncertainty to prevent a later user from making a stronger claim than the account supports.

### MNT.3:10 - Architectural Rationale

Mechanism, observed condition and consequence are connected in one account because their separation is what makes diagnosis usable. Population evidence is included when it changes that account, rather than treated as an automatic statistics exercise. The Method supports maintenance reasoning; it does not replace specialist materials analysis or a research design.

### MNT.3:11 - SoTA-Echoing

The practice question is how much failure knowledge is sufficient for a maintenance choice. The selected line combines physical explanation with qualified observation and decision relevance. It adapts the failure-mechanism emphasis in the [2025 maintenance optimization account](https://orbilu.uni.lu/bitstream/10993/61558/1/1-s2.0-S0377221724005241-main.pdf) and uses FPF [A.10](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a10---evidence-graph-referring-claim-bound-evidence-and-provenance-graph) and [C.16](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c16---measurement-metrics-characterization-mmchr) for evidential and measurement claims. Against fault-code counting or mandatory exhaustive root-cause analysis, the exact changes are the separated claims, observation limits and conditional inquiry in the Solution. The trade-off is an explicitly narrower causal answer in exchange for useful timely action. Reopen when new failure or exposure evidence can distinguish a consequential alternative.

### MNT.3:12 - Relations

[MNT.1](#mnt1---identify-the-maintained-system-use-and-permission-boundary) supplies the functioning question, [MNT.4](#mnt4---monitor-and-interpret-current-condition) supplies current condition observations, and [MNT.12](#mnt12---maintain-maintenance-information-and-configuration-continuity) supports the relevant configuration and history. [MNT.2](#mnt2---select-and-reopen-the-maintenance-policy), [MNT.6](#mnt6---diagnose-condition-and-select-an-intervention) and [MNT.13](#mnt13---coordinate-the-maintenance-programme-and-fleet-learning) consume the resulting failure account for different decisions. FPF [A.10](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a10---evidence-graph-referring-claim-bound-evidence-and-provenance-graph) qualifies evidence, [C.16](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c16---measurement-metrics-characterization-mmchr) governs measurement and [C.11.DUA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11dua---decision-useful-advice-and-evidence-demands) governs the contribution and burden of further inquiry.

### MNT.3:End

## MNT.4 - Monitor and Interpret Current Condition

> **Type:** Method
> **Status:** Draft

### MNT.4:1 - Problem frame

Use this pattern when a measurement, inspection or prediction needs interpretation for a maintenance question. A dashboard turns red, but the planner needs to know what changed, how much confidence to place in the signal and whether it changes a decision.

Return a qualified account of current condition, and of future condition only when a forecast is needed and supported. An existing adequate account can complete the request. Selecting the intervention belongs in [MNT.6](#mnt6---diagnose-condition-and-select-an-intervention); procuring or redesigning the monitoring arrangement is a different question unless its deficiency prevents the present answer.

### MNT.4:2 - Problem

A value without its measurand and operating conditions can be misleading. Measurements at different loads or locations may not be comparable. Missing samples can disappear into an apparently smooth trend. A remaining-life estimate can conceal assumptions about future duty that operation will not satisfy.

Even a well-performing predictor can be a poor maintenance arrangement if nobody can interpret the alarm or obtain a feasible response before the relevant deterioration.

### MNT.4:3 - Forces

Sensitive alarms reveal earlier changes but can increase false positives and disruptive investigations. Averaging reduces noise while obscuring short events. More sampling can improve discrimination but burden storage, interpretation and access. The choice depends on the failure mechanism, time available for action and consequences of both missed and unnecessary responses.

### MNT.4:4 - Solution

Name the condition question first. Identify the functioning or failure concern and what a different answer would change. A request to interpret today's alarm can often be answered from existing observations; it does not automatically justify a new monitoring programme.

Recover the measurement basis. State what is measured, the unit and relevant measurement location, method, sampling window and operating state. Establish instrument and inspection limitations that can change interpretation. A vibration trend under changing speed needs a comparison appropriate to that change; the same displayed number does not establish comparable condition.

Find the relevant reference: an applicable baseline, a specialist interpretation, a known operating relation or a justified threshold. Distinguish an action threshold from an instrument's display range or a convenient colour band. Preserve the basis for the threshold and the action it is intended to support. Numerical limits for a real machine come from the applicable equipment and use evidence, not this framework's examples.

Reconcile conflicting channels by their subject and conditions before averaging them. A local temperature rise and a vibration change can concern different mechanisms. A sensor replacement can explain a discontinuity. Missing data can mean a lost measurement, a stopped machine or an unobserved interval; choose only the interpretation that the available evidence supports.

Return three claims separately where needed: what was observed, what condition is inferred and what is forecast. For a forecast, state horizon, future-duty assumptions and uncertainty relevant to the decision. If those assumptions do not cover the planned duty, limit the forecast's use instead of presenting its central estimate as a deadline.

Consider whether more monitoring is worthwhile. Ask which obtainable observation could change the maintenance response, when it would arrive, whether interpretation and response capability exist and what work it would displace. A technically improved predictor needs a maintenance-use gain to justify deployment. Conversely, a simple repeat measurement can be valuable when it cheaply distinguishes a changed instrument from a real deterioration.

Complete the condition account with its supported interpretation, material limits and response or return point. If the interpretation is adequate for the receiving question, stop. A condition account can recommend returning to diagnosis without prescribing a particular repair. For consequential assurance, examine the measurement's applicability and the reasoning that connects it to the claim, using [C.16](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c16---measurement-metrics-characterization-mmchr) and [A.10](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a10---evidence-graph-referring-claim-bound-evidence-and-provenance-graph) at the required scope.

### MNT.4:5 - Archetypal Grounding

For PS17 in configuration C41, the constructed question is whether today's vibration increase is a comparable condition change or merely a changed observation. The existing setup measures radial vibration velocity at the same marked bearing-housing point, with the same mounted sensor, frequency band and 60-second RMS window. The three observations below share the specified 1,450 r/min operating point, flow and temperature range. The supplied measurement account finds no sensor or mounting change. Its comparison bounds include the relevant measurement limitations; the healthy reference also includes the observed variation under those operating conditions. These are teaching premises, not equipment limits or statistical confidence intervals.

| Observation at 1,450 r/min | RMS velocity, mm/s | Supplied comparison bounds, mm/s |
| --- | --- | --- |
| Applicable healthy reference | 1.0 | 0.8–1.2 |
| Earlier comparable observation | 2.4 | 2.3–2.5 |
| Today's observation | 3.0 | 2.9–3.1 |

Today's lower comparison bound, 2.9, exceeds both the healthy upper bound, 1.2, and the earlier upper bound, 2.5. Under this supplied basis, ordinary healthy variation or the stated measurement limitations do not explain the change. The qualified condition conclusion is an abnormal and increasing vibration at this bearing location under the compared duty. That is not, by itself, a unique diagnosis of bearing damage or a remaining-life estimate. [MNT.6](#mnt6---diagnose-condition-and-select-an-intervention) combines it with the existing diagnostic evidence and consequences to select a response.

Now change only the speed to 1,750 r/min within a second operating point already covered by the case's specialist comparison map. That map says to divide this point's indicated velocity and comparison bounds by 2 to compare them with the 1,450 r/min reference. The new reading is 6.0 mm/s, with supplied bounds 5.8–6.2. Conversion gives 3.0 and 2.9–3.1: the raw doubling does not establish further deterioration, while the abnormal condition relative to the healthy reference remains. The map is an explicitly supplied relation for these two points, not a general speed law or permission to operate at the second speed. Without an applicable relation, the 6.0 reading remains an observation but cannot be appended to the earlier condition trend; a response-changing comparison then needs a bounded specialist return.

In a different branch, the dashboard predicts “30 days remaining” using an assumed steady duty. Operation proposes a materially heavier cycle next week. The forecast cannot settle that use without an applicable relation. The team can still report today's observed condition and the forecast limitation; it need not invent a new life model to give that smaller answer.

At programme scale, a proposed online monitor is compared with the existing periodic inspection at the actual alarm-to-action boundary. A higher prediction score alone does not answer whether service loss, unnecessary interventions or total effort will improve.

### MNT.4:6 - Bias-Annotation

Visible channels draw attention away from unmeasured mechanisms and missing intervals. A precise numerical forecast can appear more authoritative than an experienced but qualified interpretation. Preserve what each source can actually support, including relevant counter-observations.

### MNT.4:7 - Conformance Checklist

Is the condition question clear? Are measurand, operating context and comparison basis adequate for the inference? Are observations, inferred condition and forecasts distinguishable? Are missing data, uncertainty and future-duty assumptions retained where they change use? Can the intended recipient act on the account or identify its exact limit?

Further monitoring is not a universal completion condition. Its attainable decision contribution and whole burden need to justify it.

### MNT.4:8 - Common Anti-Patterns and How to Avoid Them

A dashboard colour is treated as a diagnosis. Recover the observed quantity, reference and supported inference. A remaining-life estimate becomes a guaranteed repair deadline. Recover its future-use assumptions and uncertainty before using it for scheduling.

An alarm programme is judged only by prediction accuracy. Compare its actual maintenance consequences, including response delay and unnecessary interventions, before selecting an expansion.

### MNT.4:9 - Consequences

The recipient receives condition information with a usable meaning rather than a disconnected signal. Existing evidence can close a question quickly. Some stronger forecasts remain unavailable, and the cost of that limit becomes visible without invalidating the observations that are already useful.

### MNT.4:10 - Architectural Rationale

Monitoring and interpretation are kept together because the maintenance value lies in the interpreted condition, not collection alone. Intervention selection remains separate so that the same condition account can support different policies, operating restrictions or maintenance choices.

A new monitoring arrangement is selected by its contribution to that use. The Method does not assume that greater data volume or autonomy is inherently a better maintenance result.

### MNT.4:11 - SoTA-Echoing

For the question “Does this monitoring arrangement improve the maintenance decision?”, this pattern adapts the consequence-oriented evaluation line in Dadfarnia, Sharp and Herrmann's 2025 review. Against prediction-score-only comparison, the exact mutation is the alarm-to-action and full-burden reasoning in the Solution and programme example. This accepts the effort of connecting signals to actual maintenance outcomes while allowing an adequate existing interpretation to finish. The review's heterogeneous evidence does not establish a universal gain or mandatory evaluation study. Reopen when the failure, operating duty, observation process or feasible response changes. See [NIST's publication and source return](https://www.nist.gov/publications/comprehensive-evaluations-condition-monitoring-based-technologies-industrial).

### MNT.4:12 - Relations

[MNT.1](#mnt1---identify-the-maintained-system-use-and-permission-boundary) supplies required functioning, [MNT.3](#mnt3---establish-degradation-and-failure-evidence) distinguishes failure and causal claims, and [MNT.6](#mnt6---diagnose-condition-and-select-an-intervention) consumes condition for the current intervention choice. [MNT.2](#mnt2---select-and-reopen-the-maintenance-policy) can use it to reopen policy. [MNT.5](#mnt5---prepare-maintenance-service-capability-spares-tools-and-authority) and [MNT.7](#mnt7---coordinate-intervention-and-continuing-operation) establish whether an indicated response is feasible. [MNT.13](#mnt13---coordinate-the-maintenance-programme-and-fleet-learning) and [MNT.14](#mnt14---compare-and-refresh-maintenance-methods) compare the worth of monitoring at programme and Method scale. FPF [C.16](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c16---measurement-metrics-characterization-mmchr), [A.10](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a10---evidence-graph-referring-claim-bound-evidence-and-provenance-graph) and [C.11.DUA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11dua---decision-useful-advice-and-evidence-demands) govern measurement, evidence and conditional evidence demands.

### MNT.4:End

# Part B - Readiness, Intervention Choice, Coordination, and Protection

## MNT.5 - Prepare Maintenance Service Capability, Spares, Tools, and Authority

> **Type:** Method
> **Status:** Draft

### MNT.5:1 - Problem frame

Use this pattern when a maintenance policy or intervention depends on support that may not be ready at the required time. The spare is in stock, but its applicability is unresolved; the tool is available, but no competent provider can use it in the outage.

Establish the support that makes the selected maintenance task feasible, or return the deficiency that changes the choice. This is maintenance readiness for a stated task and use. Designing a changed workshop, service platform or supply arrangement uses [SYSE.12](SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse12---develop-an-engineering-platform-for-practitioner-work) where needed. A recommendation can already be complete while readiness for its performance remains incomplete.

### MNT.5:2 - Problem

An available resource can be unsuitable for the task. Stock presence does not establish part compatibility, an organization chart does not establish available competence and a tool listing does not establish a usable measurement capability. A nominally quick repair can therefore have a long or uncertain real response time.

The opposite error is to require every conceivable support record before answering any maintenance question. Readiness concerns the selected work, not a universal administrative package.

### MNT.5:3 - Forces

More reserve support reduces some response delays but consumes storage, money and maintenance effort. Shared specialists and repairable pools can improve use of resources while creating contention. Long-term support must address obsolescence and shelf condition; an urgent task needs the smallest adequate answer now. Readiness decisions also affect the people expected to extend a shift or absorb unexpected work.

### MNT.5:4 - Solution

Derive support from the actual task content and its uncertainty. Identify the relevant procedure, access, expected work and foreseeable branches. A bearing replacement and a fault diagnosis may use different competence, tools and information even when they concern the same unit.

Check readiness at the point of use. For spares, establish applicability to the installed configuration and the condition needed for installation. Resolve material compatibility, preservation, shelf-life or specialist-return requirements where they actually govern this task. A certificate is useful when it supplies a required claim; collecting an unrelated certificate does not repair a compatibility gap.

For tools and information, determine whether the practitioner can perform and judge the task. This may require the applicable instruction, fit-for-purpose measurement capability, access to configuration information and suitable workspace. A calibration label alone does not settle whether the instrument's range and uncertainty suit the measurement.

For providers, establish relevant competence, actual availability, access and action-specific authority. Include working conditions and likely task duration when these affect capability. If unexpected work would require relief, obtain a viable relief arrangement or preserve the resulting limit. An instruction to concentrate harder does not create another qualified person.

Relate obtaining lead times to the maintenance need. Distinguish what can be prepared during continuing operation from what requires shutdown or protected access. Include supplier uncertainty, transit, acceptance and replenishment where they change response feasibility. For a repairable pool, consider units already removed for repair and common demands on the same stock; nominal pool size is not available reserve.

Choose the smallest adequate support action. It may be to use an existing spare, reserve a qualified specialist, resolve one applicability question, obtain another window or change the intervention alternative. If the support arrangement itself is inadequate across recurring tasks, return that enabling-arrangement development question to [SYSE.12](SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse12---develop-an-engineering-platform-for-practitioner-work) and the programme decision to MNT.13.

Return the task-specific readiness result with the condition that can invalidate it. A part reserved for this job can be reassigned; a provider can become unavailable; an installed configuration can change. Reopen only the affected readiness claim. A support deficiency limits the proposed work but need not prevent a useful diagnosis or recommendation.

### MNT.5:5 - Archetypal Grounding

In APP-MNT-01, a replacement bearing for PS17 is physically available. The case's governing conditions require a specialist applicability/certification return for that replacement in configuration C41. Until that return arrives, the proposed replacement cannot begin. The planner's supported recommendation remains complete.

The team uses the available time to prepare the applicable instruction, reserve the qualified provider and check the required tools without entering the protected work area. When the specialist return arrives, it closes the part question only; the actual isolation and permission remain [MNT.8](#mnt8---isolate-make-safe-and-authorize-the-intervention)'s result.

A late return can invalidate the intended outage even though the part becomes acceptable. [MNT.7](#mnt7---coordinate-intervention-and-continuing-operation) then compares another window or another supported response. Entering the outage first and hoping the return will arrive would turn a support uncertainty into service exposure.

For a fleet of obsolete components, a different result may be necessary: a repairable pool with a credible turnaround arrangement or an engineering-approved replacement design. Purchasing more unusable legacy stock does not establish readiness.

### MNT.5:6 - Bias-Annotation

Inventory systems make material shortages visible while hiding interpretation work, contractor access and specialist fatigue. Include those support demands when they change the task. A procurement saving can move cost to downtime or the people expected to compensate for an unsuitable resource.

### MNT.5:7 - Conformance Checklist

Can the selected task be performed and judged with the actual available part, provider, tool, information and access? Are material compatibility and permission conditions supported? Do obtaining and relief arrangements fit the needed time? Are shared demands and support uncertainties retained where they change feasibility?

A readiness answer can be “adequate for this task” or a specific deficiency. It does not require a new platform, a complete stock catalogue or closure of an advice request through physical work.

### MNT.5:8 - Common Anti-Patterns and How to Avoid Them

“Two in stock” is taken as proof that two replacements can proceed. Check applicable condition, reservations and shared resources. A named service provider is treated as available capability when its competent person is committed elsewhere. Recover the actual obtaining arrangement and timing.

A complete support checklist is imposed on a simple recommendation. Limit readiness work to what the present result consumes, and preserve requirements that govern any later intervention separately.

### MNT.5:9 - Consequences

The plan uses support that can actually contribute to maintenance. Some apparent quick fixes become infeasible; some preparation can proceed without consuming the outage. The cost is explicit attention to readiness and replenishment where nominal resource counts were previously enough.

### MNT.5:10 - Architectural Rationale

Readiness belongs between maintenance intent and feasible performance because selecting a technically sensible task does not obtain its means. Keeping the Method domain-specific preserves compatibility, repairable-stock and maintenance-access reasoning while reusing the general enabling-arrangement contribution from SYSE.12.

### MNT.5:11 - SoTA-Echoing

The question is how to turn nominal resources into a feasible maintenance response. This pattern adapts the human/material-support emphasis in GFMAM's 2021 framework, §6.5, into task-specific readiness reasoning. Against stock-count-only planning, the exact additions are applicability, provider availability and obtaining lead time. It accepts some reservation and reconciliation effort to expose a real support limit before an outage begins. The source supplies breadth, not a universal documentation checklist. Reopen when task content, support lead time or available capability changes. See [GFMAM's maintenance framework](https://www.gfmam.org/sites/default/files/2021-02/GFMAM%20Maintenance%20Framework%20-%202nd%20Edition%20Final.pdf).

### MNT.5:12 - Relations

[MNT.2](#mnt2---select-and-reopen-the-maintenance-policy) and [MNT.6](#mnt6---diagnose-condition-and-select-an-intervention) identify task needs; [MNT.7](#mnt7---coordinate-intervention-and-continuing-operation) and [MNT.15](#mnt15---reconcile-simultaneous-maintenance-operation-and-support-work) consume readiness in coordination. [MNT.8](#mnt8---isolate-make-safe-and-authorize-the-intervention) establishes permission for the actual protected work. [MNT.12](#mnt12---maintain-maintenance-information-and-configuration-continuity) supplies configuration and history where applicability depends on them. [SYSE.12](SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse12---develop-an-engineering-platform-for-practitioner-work) supplies enabling-arrangement development, and FPF [A.2.2](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a22---ucapability---system-ability-envelope-and-measures) supports capability-envelope claims.

### MNT.5:End

## MNT.6 - Diagnose Condition and Select an Intervention

> **Type:** Method
> **Status:** Draft

### MNT.6:1 - Problem frame

Use this pattern when current condition raises a maintenance choice: repair, replace, adjust, inspect, defer, restrict use or stop. The first suspected cause has attracted a repair proposal, but the practitioner needs to know whether it is the supported and feasible response.

Return the diagnosis needed for that choice and a recommendation or selected intervention with its limits. A recommendation is a finished result when it adequately answers the request. Selecting an intervention does not establish its permission, perform it or demonstrate restored functioning.

### MNT.6:2 - Problem

Diagnosis can become either premature certainty or an endless search. A plausible cause triggers the first familiar repair; alternatively, advice is withheld until every possible root cause is eliminated. Both lose the practical question: which remaining uncertainty changes what should be done now?

A technically effective repair can also be worse than another response when access, support, service loss or intervention-induced faults are considered.

### MNT.6:3 - Forces

Waiting may allow deterioration or loss of service; acting early may waste useful life and create new faults. More diagnosis can narrow the choice but delay a necessary response. A reversible restriction can preserve useful operation while reducing demand, but only within its supported and permitted envelope. Compare these consequences without treating urgency as evidence of either cause or authority.

### MNT.6:4 - Solution

Begin with the requested decision and time horizon. Recover the relevant required function, current condition and failure account. Use already adequate evidence before asking for more. Separate the diagnosis supported now from the stronger causal account that may remain unresolved.

Form the alternatives that can answer this case. Include retaining the present arrangement, deferring with stated conditions, restricting operation, targeted inspection and stopping when they are plausible responses. Repair and replacement can have different support, downtime and recurrence consequences. A candidate without the means or authority for its actual performance can remain a recommendation, but it is not a feasible immediate act.

Compare the alternatives at the same required use. Explain what failure or condition each addresses, the consequence of delay, the expected intervention effect and its material uncertainty. Include disturbance, introduced defects, access, support, service loss and later restoration. Do not conceal an unacceptable condition by averaging it into a favourable cost score.

Test whether the remaining diagnosis uncertainty changes the choice. If all plausible mechanisms justify the same bounded response, give that response with its supported explanation. If one mechanism favours replacement and another would make it ineffective, seek the smallest worthwhile discrimination. State the result needed from a specialist rather than commissioning an unrestricted investigation.

Use [MNT.5](#mnt5---prepare-maintenance-service-capability-spares-tools-and-authority) and [MNT.7](#mnt7---coordinate-intervention-and-continuing-operation) where support and operation can change feasibility. A part awaiting applicability evidence can block installation while leaving replacement at a suitable future outage as the best recommendation. If no feasible alternative preserves the required use, return the precise unmet condition to the appropriate operating or engineering decision.

State the chosen answer in ordinary terms: what to do or recommend, for which unit and configuration, under which conditions, why it is preferable and what would reopen it. Retain only uncertainty and conditions that change the recipient's use. If the request is for advice and the answer is adequate, stop.

For actual performance, carry the selected scope to [MNT.8](#mnt8---isolate-make-safe-and-authorize-the-intervention) and MNT.9. When an operative requirement is disputed, appraise its merits separately: the protected party, relevant harm, baseline and marginal protection, whole burden and displaced harm matter. Preserve present force while the authorized holder considers an amendment. A maintenance recommendation does not amend that requirement.

### MNT.6:5 - Archetypal Grounding

For PS17 in configuration C41, the constructed decision is how to meet the required normal duty after the next planned outage, not how to guarantee an indefinite bearing life. [MNT.4](#mnt4---monitor-and-interpret-current-condition) supplies the abnormal, increasing condition account; vibration magnitude alone does not choose replacement. The case additionally supplies an existing machine-specific inspection and diagnostic account identifying a localized defect in the installed bearing's rolling contact. Its relevant mounting and lubrication findings support replacement under the unchanged design basis rather than correction of an ongoing mounting or lubrication defect. These are explicit diagnostic premises for this teaching case, not conclusions obtainable from the three vibration values alone.

The operating assessment supplies a distinct premise: a permitted lower-duty assignment for this unit still meets the full present district-heating demand until the planned outage two days away. This is not XRI-09's reduced-capacity outage, whose separate bound remains four hours. Normal demand then returns, and that lower-duty assignment cannot meet it. This two-day boundary is a service and supported-use boundary, not a predicted time to bearing failure. Continued use remains within the supplied condition and protection limits; losing one of those limits reopens the operating response immediately.

| Live response | Effect and consequence under the supplied case conditions | Place in the answer |
| --- | --- | --- |
| Continue unrestricted use without intervention | Leaves the diagnosed defect in place, while the available condition assessment does not support unrestricted normal-duty use over the receiving period. | Does not provide a supported answer to the required use. |
| Use the permitted temporary restriction | Reduces the present demand on the affected unit and meets current service needs within its supported conditions; it neither removes the defect nor supplies the later normal duty. | A usable bridge to the outage, not a substitute for restoration. |
| Replace the applicable bearing at the planned outage | Removes the identified local defective component. Preparation, testing and hand-back provisionally fit [MNT.7](#mnt7---coordinate-intervention-and-continuing-operation)'s 225-minute demand within the 240-minute bound. Replacement introduces intervention risk and still needs applicable parts, protected work and functioning verification. | The supported restoration recommendation, conditional on those operative requirements. |
| Stop immediately | Avoids further running of the affected unit but causes service loss that the permitted bridge avoids under the present facts. | Not the preferred present response; return to the operating/protection decision if the bridge loses its supported conditions. |

The recommendation follows from the combination: the restriction meets only the short receiving need, whereas replacement addresses the identified defect and has a bounded usable opportunity before normal demand returns. Neither the vibration rise nor the availability of an outage would establish that comparison alone. The spare applicability/certification return remains outstanding. The finished advice is therefore “use the supported temporary arrangement and recommend replacement at the suitable outage, subject to applicable part and operative work conditions,” not “begin replacement now.” If the part or full window does not become usable, the team must reopen the service arrangement; it cannot silently extend the temporary restriction.

Why this bearing deteriorated earlier than comparable units remains unresolved. The supplied diagnostic basis supports removing the present local defect, but does not establish that replacement prevents every recurrence. That stronger causal uncertainty does not defeat this bounded recommendation; it limits the claim to the present restoration question. Actual resulting functioning and resumed-use authority still require their separate [MNT.10](#mnt10---verify-restored-functioning) and [MNT.11](#mnt11---certify-hand-back-and-authorize-resumed-use) returns.

Suppose an existing inspection instead shows that a shared mounting defect would make another bearing replacement ineffective. That evidence changes the alternatives and reopens the choice. The team returns the mounting or engineering question instead of repeating the same repair.

In the shared-specialist case, a less urgent job can be deferred only if its failure consequence and operating conditions support that choice. The arithmetic showing that both jobs cannot fit identifies the conflict; it does not decide which consequence to accept.

### MNT.6:6 - Bias-Annotation

The available spare, a recent training course or a vendor's diagnostic label can make one intervention disproportionately salient. Explicitly compare a plausible no-change or less intrusive alternative when it can satisfy the same use. Include the burden borne by operation and maintenance staff, not just the repair budget.

### MNT.6:7 - Conformance Checklist

Does the diagnosis support the actual decision rather than a stronger unnecessary claim? Have the plausible alternatives been compared at the same use and horizon? Are response feasibility, service effects and material uncertainty visible? Is the result clearly advice, a selected act or an unresolved decision?

An adequate recommendation closes the advice request. Any selected further inquiry has an attainable action-changing contribution; actual performance retains its particular conditions.

### MNT.6:8 - Common Anti-Patterns and How to Avoid Them

“Fault detected, replace component” skips the question of whether the replacement addresses the failure. Compare its expected effect with the supported mechanism. “Root cause not proven, no advice possible” withholds a smaller answer even when all remaining causes support it.

A conditional recommendation is then treated as permission. Carry the condition into the receiving work decision rather than dropping it when the work order is opened.

### MNT.6:9 - Consequences

The recipient obtains a timely, qualified choice and knows what is still needed for a different or stronger use. Some investigations stop; some interventions are deferred or redirected. Residual uncertainty remains explicit without becoming a blanket reason to delay every maintenance result.

### MNT.6:10 - Architectural Rationale

Diagnosis and present intervention choice belong together because the required diagnostic resolution depends on the alternatives. Policy remains separate because a reusable task rule can be sound while this case requires an exception. Permission and functioning evidence remain separate because they answer different questions about the selected act.

### MNT.6:11 - SoTA-Echoing

The practice question is how condition knowledge becomes an actionable maintenance answer. This pattern adapts the prediction-to-action gap identified in the 2025 prescriptive-maintenance synthesis into explicit diagnosis, alternative comparison and feasibility returns. Against automatic repair from a prediction, the Solution adds the action-changing uncertainty test and a sufficient-recommendation stop. The source's abstract-level contribution does not establish a deployed autonomous algorithm or a particular repair rule. FPF [C.11.DUA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11dua---decision-useful-advice-and-evidence-demands) supplies the general conditional-inquiry reasoning. Reopen when a new mechanism, feasible alternative or consequence changes the answer. See [the author-deposited source](https://orbilu.uni.lu/handle/10993/65591).

### MNT.6:12 - Relations

[MNT.1](#mnt1---identify-the-maintained-system-use-and-permission-boundary), [MNT.3](#mnt3---establish-degradation-and-failure-evidence) and [MNT.4](#mnt4---monitor-and-interpret-current-condition) supply the bounded question, failure account and condition. [MNT.5](#mnt5---prepare-maintenance-service-capability-spares-tools-and-authority) and [MNT.7](#mnt7---coordinate-intervention-and-continuing-operation) qualify feasible performance. [MNT.8](#mnt8---isolate-make-safe-and-authorize-the-intervention) governs actual intervention permission; [MNT.9](#mnt9---perform-and-record-the-maintenance-intervention)–[MNT.11](#mnt11---certify-hand-back-and-authorize-resumed-use) supply performance, functioning and hand-back results when selected. FPF [C.11](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11---decision-theory-decsn-cal) supports comparison and [C.11.DUA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11dua---decision-useful-advice-and-evidence-demands) supports advice and evidence-demand appraisal.

### MNT.6:End

## MNT.7 - Coordinate Intervention and Continuing Operation

> **Type:** Method
> **Status:** Draft

### MNT.7:1 - Problem frame

Use this pattern when maintenance and operation need one feasible arrangement for access, service continuity and return to use. A repair estimate fits the outage, but shutdown, testing and restoration have not been counted.

Relate the selected intervention's whole demands to the operation's actual service result. Return an actionable timing and operating arrangement, or the unmet condition that prevents it. A recommendation can finish before this coordination is complete. Several jobs that compete across shared resources additionally need [MNT.15](#mnt15---reconcile-simultaneous-maintenance-operation-and-support-work)'s whole-combination reasoning.

### MNT.7:2 - Problem

A task duration is not an outage duration. Preparation may occur during operation, while isolation, intrusive work, controlled tests and restoration can consume the service-loss window. Concurrent work can share an access opportunity but also interfere or remove a fallback.

Ignoring the ending conditions is especially costly: a mechanically completed repair can leave the operator without the evidence, configuration or control needed to resume use.

### MNT.7:3 - Forces

A longer window permits more contingency but increases loss of service. Preparation before shutdown can shorten the outage while consuming scarce support. Fallback operation may preserve a contribution at reduced capacity, but only within a qualified demand and duration. The arrangement must account for uncertainty without counting the same allowance twice.

### MNT.7:4 - Solution

Recover the operating commitment for the actual horizon: required service, permissible reduction, applicable fallback and authority over changes. Use a qualified capacity result such as [OPS.10](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops10---qualify-capacity-under-variability) where relevant. Do not substitute a pump's nameplate rating for the operation's service claim.

Lay out the intervention's dependency and time demands. Separate preparation that can occur without the outage from work that requires shutdown, protected access or a changed operating state. Include the necessary testing and return to control. Some activities can overlap; establish that they do not compete for the same person, equipment, access or protection condition.

Use an elapsed-time model appropriate to the real dependencies. Sum sequential activities; use the critical path only when the supported overlaps are real. Identify whether task estimates already include contingency before adding another allowance. Labour-hours, access-hours and elapsed service-loss time are different quantities.

Compare the resulting demand with the whole available service envelope. If it does not fit, change a real variable: another window, another supported intervention, qualified fallback, additional capable provider, permitted rate adjustment or a justified deferral. A smaller written estimate does not change the work. A rate change is useful only when its service and deterioration consequences are supported.

Agree what happens when a condition changes during the window. The relevant response can be a safe hold, restoration to a supported condition, a separately permitted extension or a revised operating decision. Identify the latest decision point before loss of a viable return becomes consequential. Do not treat an allowance as permission to omit a required check when time runs short.

Return the coordinated arrangement to the people who control operation and maintenance. Preserve the service assumptions, actual resource commitments, protection transitions and stopping conditions that they need to act. The result is qualified by those conditions, not a guarantee that no interruption will occur.

### MNT.7:5 - Archetypal Grounding

The following is the authoritative whole-outage calculation for the constructed PS17 application. It is a reasoning example, not an equipment procedure or a time standard. The qualified operating result allows four hours, or 240 minutes, of the stated reduced-capacity operation.

| Selected activity | Elapsed minutes inside the outage | Basis in this constructed plan |
| --- | ---: | --- |
| Controlled shutdown and establishment of isolation | 30 | The applicable protected-access work is included. |
| Selected bearing intervention | 95 | Parts, tools and provider are ready before shutdown. |
| Controlled testing and functioning verification | 45 | Includes the necessary test-state transitions. |
| Final restoration and return of control | 25 | Includes the receiving operator's hand-back work. |
| Explicit contingency | 30 | This is additional to the task estimates, which exclude it. |
| **Whole planned demand** | **225** | Sequential demands; no unsupported overlap is assumed. |

Ninety minutes of preparatory work occurs before the outage and is excluded from its demand. The plan leaves 15 minutes beyond the explicit contingency within the 240-minute operating bound. That arithmetic establishes fit only for the constructed estimates and supported conditions.

If an additional 20-minute demand arises beyond all included allowances, the demand becomes 245 minutes and no longer fits. The team revisits the operating or intervention arrangement. It does not consume testing or hand-back time to preserve the appearance of a four-hour plan.

If the spare applicability return is absent before the planned start, the team does not begin this replacement branch. If the actual isolation cannot be established, the affected protected work does not start. Those limits preserve the earlier completed recommendation and return a different coordination question.

### MNT.7:6 - Bias-Annotation

Repair estimates often reflect the technician's direct work and omit operator preparation, controlled testing or waiting for a release. Name whose time and service loss are counted. A successful previous outage can also hide favourable conditions that are absent now.

### MNT.7:7 - Conformance Checklist

Does the arrangement consume a valid operating-capacity and service result? Are preparation, protected work, testing, restoration and material contingency accounted for without double counting? Are overlaps compatible with actual resources and protection? Is there a supported response when the plan no longer fits?

A coordination result is complete when the responsible people can act on its bounded arrangement or know the exact unmet condition. Completing every maintenance Method is not its acceptance test.

### MNT.7:8 - Common Anti-Patterns and How to Avoid Them

“The repair takes three hours, so it fits” excludes the rest of the outage. Compare complete elapsed demand with the service envelope. Preparation is assumed to overlap operation even though it needs the same isolated machine. Check the dependency before removing it from the outage.

Time pressure can turn contingency into permission to skip restoration evidence. Return to the operating decision when the supported plan expires.

### MNT.7:9 - Consequences

The maintenance and operating commitments refer to one feasible arrangement. Some preparation moves earlier; some work moves to another window. The additional planning effort is justified where it prevents unsupported service promises and identifies the first condition that changes the plan.

### MNT.7:10 - Architectural Rationale

This Method coordinates one intervention with continuing operation. The complete elapsed-time condition belongs here because pairwise task approvals cannot establish whole-window fit. [MNT.15](#mnt15---reconcile-simultaneous-maintenance-operation-and-support-work) extends that reasoning when several jobs and support arrangements impose simultaneous demands.

Rate adjustment and more advanced scheduling remain options, not compulsory tools. A simple bound can already settle the present question.

### MNT.7:11 - SoTA-Echoing

The practice question is whether maintenance can fit the real operating commitment. This pattern adapts preparation-before-intervention and flexible timing as candidate choices from the bounded scheduling work of Gan and colleagues and Kasuya and Jin. Against repair-duration-only planning, the exact mutation is the complete elapsed-demand comparison and conditional operating return above. Their models do not supply these constructed times, field effectiveness or permission to change duty. The selected arithmetic is preferable at comparable effort when it already settles fit; optimization becomes useful for a harder unresolved choice. Reopen when demand, preparation dependency or operating capacity changes. See [preparation-aware scheduling](https://journals.sagepub.com/doi/abs/10.1177/09544054251350538) and [flexible-timing research](https://www.sciencedirect.com/science/article/abs/pii/S095183202600342X).

### MNT.7:12 - Relations

[MNT.5](#mnt5---prepare-maintenance-service-capability-spares-tools-and-authority) supplies readiness and [MNT.6](#mnt6---diagnose-condition-and-select-an-intervention) the selected intervention. [OPS.10](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops10---qualify-capacity-under-variability) supplies qualified capacity where used. [MNT.8](#mnt8---isolate-make-safe-and-authorize-the-intervention)–[MNT.11](#mnt11---certify-hand-back-and-authorize-resumed-use) govern the actual protection, work, functioning and hand-back returns whose time this Method includes. [MNT.15](#mnt15---reconcile-simultaneous-maintenance-operation-and-support-work) handles simultaneous shared demands. A changed service concept returns to operation or engineering rather than being inferred from this maintenance plan.

### MNT.7:End

## MNT.8 - Isolate, Make Safe, and Authorize the Intervention

> **Type:** Method
> **Status:** Draft

### MNT.8:1 - Problem frame

Use this pattern when a selected maintenance intervention will expose people, equipment or the environment to a hazard that requires controlled access, isolation or other protection. A work order is ready, but the actual protection and permission for the proposed act have not been established.

Use the applicable equipment procedure and competent authorized people to establish, verify and maintain those conditions. Return a supported permission to begin the bounded work or the exact unmet condition. This framework gives maintenance reasoning, not a substitute isolation procedure. A diagnosis-only or recommendation-only answer is not forced through an intervention-permission task.

### MNT.8:2 - Problem

Stopping normal operation does not by itself establish control of every relevant exposure. Stored energy, reaccumulation, shared supplies, remote commands or simultaneous work can leave an intervention unsafe. A permit can state a required condition while the actual machine remains in another state.

Permission and protection also change with the scope of work, crew, shift or test configuration. A correct initial condition can cease to apply.

### MNT.8:3 - Forces

Protection must address the actual hazard and intervention without becoming an unrelated paper exercise. An urgent service need may increase pressure to proceed, while an overbroad restriction may displace harm or prevent useful work. The merits of a requirement and its present operative force are separate questions; neither urgency nor paperwork answers both.

### MNT.8:4 - Solution

Recover the proposed work scope, actual configuration, relevant hazards and applicable procedure. Qualified people determine the equipment- and jurisdiction-specific controls. If the procedure's applicability or the authority to act is unresolved, return that limit before the affected work begins.

Trace the exposure paths needed for the intervention. Depending on the equipment, these can include electrical, mechanical, hydraulic, pneumatic, thermal, chemical or other sources, including stored or reaccumulating energy. This list is illustrative: the applicable procedure and actual hazard analysis establish the set for the job. A control-system stop command is not assumed to be an energy-isolating measure.

Establish the selected isolation and protective conditions through the applicable procedure. Verify the condition that protects the people who will perform the work, using the required competent personnel and suitable means. A signed statement is evidence only to the extent that it supports the actual condition and applicable authority.

Coordinate people whose work can alter that condition. Where contractors, groups, shift changes or simultaneous jobs are involved, maintain the required protection and control through those transitions. A person leaving the work area does not by itself resolve the transfer of protection or permission.

Define the bounded permission for the actual intervention: permitted scope, configuration, protection conditions and the material change that requires a hold or revised decision. During work, respond to a loss of protection or an unexpected condition using the applicable safe hold, restoration or reassessment procedure. Testing that needs an energized or otherwise changed state has its own controlled transition; initial isolation does not authorize any later test state.

If a requirement's merits are disputed, use a separate appraisal. Identify the protected bearer, relevant harm and causal basis, baseline and incremental protection, whole burden and displaced harms. Compare harmful relaxation with harmful retention or tightening, and name who may amend the requirement. Until an authorized change applies, preserve current force. This separation permits substantive criticism without turning a framework discussion into permission to bypass a control.

Return permission only for the supported work and conditions, or state the missing protection, applicability or authority. Keep evidence proportionate to the actual reliance and applicable requirements. A universal extra certification bundle is not created by this Method.

### MNT.8:5 - Archetypal Grounding

In the constructed PS17 case, the specialist part return has arrived and the planned outage is feasible. The authorized personnel still establish the applicable isolation and access conditions for the actual configuration before the bearing intervention.

Suppose they discover that a shared path can reintroduce energy and the assumed isolation does not control it. The protected work does not begin. They return the actual discrepancy for the required competent decision and revise the outage arrangement if necessary. The earlier replacement recommendation remains a completed answer.

In the extended branch, the applicable procedure establishes and verifies protection. The permission covers the selected bearing work, not unrestricted work on neighbouring equipment. A later test that requires a changed operating state uses its applicable controlled transition. Successful testing and final hand-back remain separate results.

OSHA 29 CFR 1910.147 provides a US jurisdiction-bounded illustration of energy-control, verification and restoration requirements, with its own scope and exclusions. Its presence here does not establish that this standard governs PS17 or supply a complete procedure for another installation.

### MNT.8:6 - Bias-Annotation

A familiar machine can make practitioners underestimate changed stored energy, configuration or shared work. A permit's visible completion can also displace attention from the condition it is meant to establish. Recover the actual protection at the point where it matters.

### MNT.8:7 - Conformance Checklist

Is the procedure applicable to the actual intervention and configuration? Have competent authorized people established and verified the required protection? Do shared work and planned state transitions preserve it? Is the permission bounded to the supported scope, with a usable response to material change?

These questions apply to the selected intervention. They neither require a permission package for advice nor authorize omission of operative protection because a recommendation is already complete.

### MNT.8:8 - Common Anti-Patterns and How to Avoid Them

“The machine is stopped” is used as an isolation claim. Establish the applicable exposure controls and their verification. “The permit is signed” is used as proof of the actual state. Check the correspondence between the permission and protection in place.

A disputed requirement is silently relaxed to meet the window. Keep its merits appraisal separate and obtain any amendment from the holder of the relevant authority.

### MNT.8:9 - Consequences

The intervention proceeds only within a supported protection and permission boundary. Some jobs stop or change scope before exposure occurs. The Method adds no claim of universal safety; its result is conditional on the actual procedure, competent performance and continued applicability.

### MNT.8:10 - Architectural Rationale

Selection, protection and performance are distinct because each can be adequate while another remains unresolved. Keeping action-specific protection here preserves the ability to finish useful advice without weakening any condition governing actual work.

A generic framework cannot enumerate every equipment hazard or jurisdictional exception. It therefore governs how the applicable protection is recovered and used, while the qualified procedure supplies the concrete acts.

### MNT.8:11 - SoTA-Echoing

For the question “What supports beginning this protected intervention?”, this pattern adapts the actual-control and verification logic illustrated by [OSHA 1910.147](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.147). Against a stop-command or permit-only default, the exact additions are verified protection, bounded permission and controlled changes of state. The source is an operative US example within its scope, not a universal maintenance law; the local application needs its actual current requirements. FPF [A.2.8.PER](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a28per---granted-permission-exercise-and-non-prohibition) and [C.11.DUA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11dua---decision-useful-advice-and-evidence-demands) distinguish permission from requirement merits. Reopen when work, configuration, exposure, personnel transition or the applicable rule changes.

### MNT.8:12 - Relations

[MNT.1](#mnt1---identify-the-maintained-system-use-and-permission-boundary) identifies the relevant unit, use and control. [MNT.5](#mnt5---prepare-maintenance-service-capability-spares-tools-and-authority) and [MNT.7](#mnt7---coordinate-intervention-and-continuing-operation) establish support and timing; [MNT.6](#mnt6---diagnose-condition-and-select-an-intervention) selects the proposed work. [MNT.9](#mnt9---perform-and-record-the-maintenance-intervention) performs within the resulting conditions, while [MNT.10](#mnt10---verify-restored-functioning) and [MNT.11](#mnt11---certify-hand-back-and-authorize-resumed-use) use controlled testing and restoration for their different results. FPF [A.2.8.PER](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a28per---granted-permission-exercise-and-non-prohibition) governs permission, [A.2.2](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a22---ucapability---system-ability-envelope-and-measures) capability and [C.11.DUA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11dua---decision-useful-advice-and-evidence-demands) a requirement-merits appraisal.

### MNT.8:End

# Part C - Performed Intervention, Functioning, and Return to Use

## MNT.9 - Perform and Record the Maintenance Intervention

> **Type:** Method
> **Status:** Draft

### MNT.9:1 - Problem frame

Use this pattern when a selected maintenance intervention is being performed and later decisions depend on what actually happened. The planned bearing has been replaced, but an interruption, substituted part or changed setting can leave the work record inconsistent with the machine.

Perform the task within its applicable procedure and operative conditions, preserving the material actions and actual resulting configuration. The first result is evidence of the performed intervention, including its incomplete or changed portions. [MNT.10](#mnt10---verify-restored-functioning) establishes restored functioning and [MNT.11](#mnt11---certify-hand-back-and-authorize-resumed-use) establishes the hand-back result. This pattern does not require physical work to finish a recommendation request.

### MNT.9:2 - Problem

A work order describes intended work. Closing its tasks can conceal what was skipped, repeated, changed or performed under different conditions. A subsequent tester may then check the wrong configuration, and a future maintainer may infer that a suspected cause was confirmed.

Unexpected conditions make this worse when the team improvises beyond the permitted scope without revisiting protection, competence or the maintenance choice.

### MNT.9:3 - Forces

The practitioner needs enough freedom to respond to the actual machine while preserving the limits that make the response acceptable. Detailed recording can support later diagnosis but distract from protected work if poorly timed. A work interruption can require relief or re-establishment of a condition; simply extending the shift may impair performance.

### MNT.9:4 - Solution

Recover the selected task and the operative work conditions before performing it. The applicable equipment procedure supplies the concrete technique, tool use, tolerances and controls. This Method organizes maintenance performance and its usable account; it does not replace that procedure.

Maintain correspondence between work and actual state. Identify the unit, relevant configuration, selected parts and settings. Where the procedure requires a check before an irreversible or consequential step, perform that check at the point where it establishes the needed condition. A later signature cannot recreate an unobserved state that is no longer recoverable.

When the actual condition differs from the expected one, determine what changes. A harmless access detail may remain within the permitted task. Unexpected damage, a different part interface, a lost protection condition or a larger repair can change competence, permission, time and verification. Use the applicable hold or restoration procedure and return the changed maintenance decision rather than silently extending the scope.

Handle interruption explicitly. Preserve a condition that the next practitioner can safely recognize, transfer the relevant unfinished work and protection through the applicable arrangement, and re-establish any condition that no longer has usable support. If fatigue or working conditions impair the task, change allocation, relief or timing. The completion pressure does not supply capability.

Preserve the facts that later users actually need. These commonly include material actions, installed or removed part identities, relevant settings and measurements, deviations from the selected work and unresolved conditions. Use the existing maintenance record when it serves that purpose. Applicable regulatory or organizational retention requirements remain in force; the framework does not create a separate universal bundle.

Keep statements at their supported level. “Bearing installed using the applicable procedure” concerns the intervention. “The required flow is restored” needs functioning evidence. “This recurring failure has been eliminated” needs a different horizon and causal basis. Link those later results when they exist without assigning them to a task-completion entry.

Return the performed work and resulting configuration to the tester, operator or maintenance-history user who needs them. If the work is incomplete, state its actual stopping state and the condition needed for continuation. A truthful partial result is more useful than a closed order that implies unperformed work.

### MNT.9:5 - Archetypal Grounding

In the extended constructed PS17 branch, the part return, protected access and permission are in place. The team performs the selected bearing intervention under the applicable equipment procedure.

The removed bearing is identified as R551 and the installed compatible bearing as R607. These are constructed serial-unit identifiers. The resulting installed configuration is identified as C42; it retains the same approved design basis while the actual bearing individual has changed. The maintenance record describes that change; it is not the physical configuration itself.

If unexpected housing damage is found, the original bearing task may no longer answer the condition. The team preserves the supported state and obtains the relevant revised diagnosis and work decision. It does not mark the original plan complete merely because the replacement bearing was available.

In the completed branch, the intervention record supplies the actual configuration and material observations to MNT.10. It does not yet claim restored district-heating service or removal of the unresolved long-horizon recurrence mechanism.

### MNT.9:6 - Bias-Annotation

Completion targets reward closed tasks and can discourage reporting deviations or unfinished work. A detailed plan can also make the practitioner expect the machine to match it. Keep actual observations visible where they change the work or later interpretation.

### MNT.9:7 - Conformance Checklist

Was the selected work performed within its applicable procedure and operative conditions? Were material deviations, interruptions and changed scope handled by the relevant decision? Can the next user recover the actual installed state and supported work claims? Are incomplete portions and unresolved consequences stated?

The result concerns performed intervention. Functioning and resumed-use claims require their own support only when those are the selected subsequent results.

### MNT.9:8 - Common Anti-Patterns and How to Avoid Them

A task is closed because the planned hours were consumed. Record what actually happened and the remaining state. A substituted part is described only as “equivalent” when applicability is material. Preserve the basis that makes it usable in this configuration.

An exhausted specialist is instructed to finish more carefully. Revise relief or timing in response to the actual capability limit.

### MNT.9:9 - Consequences

The tester and operator receive an account that corresponds to the intervention, including its limits. Some work returns for a revised decision rather than being completed under an obsolete plan. Recording costs remain focused on useful later claims and operative retention requirements.

### MNT.9:10 - Architectural Rationale

Performance and its account are joined because later maintenance decisions rely on that correspondence. The Method does not make the record the work itself. Separating intervention evidence from functioning and release prevents one completion claim from silently taking on several incompatible meanings.

### MNT.9:11 - SoTA-Echoing

The practice question is how to preserve reliable continuation when work differs from its plan. This pattern adapts the work-management concern in GFMAM's maintenance framework and the fatigue-reporting problem in CASA's 2026 maintenance risk account. Against task-closure-only management, its exact changes are the interruption, actual-state and relief decisions in the Solution. It accepts focused reporting and occasional replanning to avoid concealing incomplete or unsupported work. CASA's aviation account supplies a relevant failure mechanism, not a universal duty-time threshold. Reopen when a new work variant or observed interruption defeats the continuation arrangement. See [GFMAM](https://www.gfmam.org/sites/default/files/2021-02/GFMAM%20Maintenance%20Framework%20-%202nd%20Edition%20Final.pdf) and [CASA's fatigue account](https://www.casa.gov.au/operations-safety-and-travel/safety-management-systems/sector-safety-risk-profiles/maintenance-activities-sector-safety-risk-profile/fatigue).

### MNT.9:12 - Relations

[MNT.6](#mnt6---diagnose-condition-and-select-an-intervention) supplies the selected intervention, [MNT.5](#mnt5---prepare-maintenance-service-capability-spares-tools-and-authority) its support and [MNT.8](#mnt8---isolate-make-safe-and-authorize-the-intervention) its operative protection and permission. [MNT.7](#mnt7---coordinate-intervention-and-continuing-operation) and [MNT.15](#mnt15---reconcile-simultaneous-maintenance-operation-and-support-work) handle changed timing or shared work. [MNT.10](#mnt10---verify-restored-functioning) consumes performed-work and configuration evidence; [MNT.12](#mnt12---maintain-maintenance-information-and-configuration-continuity) preserves its useful history. FPF [A.13](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a13---the-agential-role-agency-spectrum) and [A.15.1](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a151---uwork) govern precise performer and performed-Work claims when those stronger claims are made.

### MNT.9:End

## MNT.10 - Verify Restored Functioning

> **Type:** Method
> **Status:** Draft

### MNT.10:1 - Problem frame

Use this pattern when a performed maintenance task is being used to claim that the System can again support its required use. A bearing replacement is complete, but the receiving operator needs evidence about functioning under the relevant configuration and load.

Establish the functioning claim that the available evidence supports, or return its unsupported portion. “Restored” means adequate for the stated use and envelope; it need not mean as-new equipment or absence of every defect. [MNT.11](#mnt11---certify-hand-back-and-authorize-resumed-use) handles the distinct permission and transfer of control for resumed use.

### MNT.10:2 - Problem

A completed procedure can leave the original problem unresolved or introduce another fault. An unloaded spin can appear successful while a loaded duty fails. Conversely, repeating every earlier test wastes time when the intervention did not affect those claims and their earlier evidence remains applicable.

The check must be able to reveal the defect that would invalidate the receiving functioning claim.

### MNT.10:3 - Forces

Representative testing improves evidence but can consume the outage and create its own controlled exposure. A short test can support an immediate operating claim while leaving long-horizon reliability unresolved. Stronger assurance may require a specialist or independent return; its value and requirements depend on the actual consequence, not the number of signatures collected.

### MNT.10:4 - Solution

State the required functioning claim, actual configuration, operating envelope and relevant horizon. Recover the operating and engineering acceptance basis. Select the performance, protection or interaction properties whose failure would change the return-to-use decision.

Relate the intervention to those claims. Identify the functioning it was intended to restore and credible faults it could have introduced. Use current adequate evidence for unaffected claims where its subject, conditions and scope still fit. A component or configuration change that invalidates that evidence reopens the affected check.

Choose checks that can discriminate the relevant success and failure states. Use the applicable equipment procedure, measurement basis and competent providers. Where real operating conditions cannot be represented, state what the test does and does not establish. A measurement needs suitable range, uncertainty and operating context for its acceptance comparison.

Plan the check's controlled state transitions with [MNT.8](#mnt8---isolate-make-safe-and-authorize-the-intervention) and its time with MNT.7. Verification that requires energization or other exposure does not inherit unrestricted permission from the earlier protected repair. The applicable procedure governs how the test state is established and ended.

Compare observed outcomes with the stated basis. Retain the actual subject, load, duration and material limitations. A passing result supports the named claim only at that scope. A failed result returns to the affected diagnosis, intervention or engineering question; unrelated passing tests do not cancel it.

Return qualified functioning evidence. A restricted-use claim may be supportable when unrestricted use is not, provided the relevant acceptance and authority conditions allow that distinction. Certification or an independent check is obtained where the concrete use requires it. Do not impose one on every functioning question, or omit an operative one merely because a task looks routine.

Stop when the receiving functioning question is adequately answered. A recurrence or life-extension claim may remain unresolved without defeating the narrower current-use result. Select further evidence only when its obtainable contribution or operative requirement justifies it.

### MNT.10:5 - Archetypal Grounding

For the extended constructed PS17 case, the tested installed configuration is C42, with the bearing replacement recorded in MNT.9. The following values are invented to demonstrate a comparison; they are not pump acceptance limits.

The case's agreed immediate-duty basis requires at least 20 litres per second at a differential pressure of at least 150 kilopascals during a 30-minute representative run. Its supplied acceptance rule is simple comparison of the reported values with those limits, using an already qualified measurement basis for this range and duty. The premise includes a prior assessment of calibration and measurement uncertainty, with the resulting decision risk accepted for this limited claim; it does not assume zero uncertainty or make simple comparison suitable for every use. Instrument drift or changed measurement conditions that invalidate that assessment reopen the comparison.

Under those supplied conditions, the constructed observation is 20.8 litres per second at 154 kilopascals throughout that run, with the applicable equipment-specific condition checks also satisfied: 20.8 exceeds 20 and 154 exceeds 150 under the stated rule. The 45-minute test allowance in [MNT.7](#mnt7---coordinate-intervention-and-continuing-operation) includes this run and its controlled transitions.

Those observations support the stated immediate duty in the tested envelope. They do not establish performance at an untested winter peak, an as-new lifetime or elimination of the long-horizon recurrence mechanism. The operator receives that scope explicitly.

If the loaded test instead reaches only 18 litres per second, the performed bearing replacement can still be correctly recorded while the required functioning claim fails. The team returns to diagnosis or the relevant engineering question. A test record with a completed checkbox cannot convert that result into restored service.

### MNT.10:6 - Bias-Annotation

The effort already spent on repair creates pressure to interpret a marginal test as success. A familiar easy-to-measure property can also displace the required operating contribution. State the acceptance basis before reading the outcome where that prevents retrospective adjustment.

### MNT.10:7 - Conformance Checklist

Does the evidence concern the actual resulting configuration and required use? Can the selected checks expose the intervention's relevant failure or introduced fault? Are measurement and test conditions suitable for the claim? Are unchanged evidence and unresolved portions used at their true scope? Are required specialist or independent returns present where applicable?

A supported current-use answer closes this question. It does not claim long-term reliability or authorize resumed use by itself.

### MNT.10:8 - Common Anti-Patterns and How to Avoid Them

“Part replaced” is used as evidence of service. Test the functioning the recipient actually needs. “It ran unloaded” becomes permission for full-duty operation. Qualify the operating envelope or obtain the evidence that changes that use.

Every historical test is repeated after a small change. Reopen the claims actually affected, while preserving any concrete requirement for the current verification.

### MNT.10:9 - Consequences

The operator receives an applicable functioning result and can distinguish it from completed maintenance work. Some repairs return for further action; some systems support only a narrower use. Verification effort is concentrated on claims and consequences rather than repeated by checklist inertia.

### MNT.10:10 - Architectural Rationale

The Method is separate from both intervention and release because their outcomes can differ. A task can be performed correctly without restoring the required contribution, and functioning can be established while control or permission remains unresolved.

Claim-specific checking permits adequate prior evidence to remain useful. It also makes a genuine configuration or load change visible as a reason to reopen the affected conclusion.

### MNT.10:11 - SoTA-Echoing

The practice question is what evidence warrants a restored-functioning claim after maintenance. This pattern adapts FPF [B.3](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#b3---trust-and-assurance-calculus)'s use-specific assurance and [C.16](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c16---measurement-metrics-characterization-mmchr)'s measurement discipline to intervention-induced failure and operating-envelope checks. Against task-sign-off or indiscriminate retesting, the exact mutation is the claim-to-check reasoning and the loaded PS17 comparison. The trade-off is retaining an explicitly limited immediate-use result instead of claiming lifetime restoration. Equipment procedures supply the concrete acceptance criteria; this synthesis does not establish universal test values. Reopen when configuration, required duty, consequence or the earlier evidence's applicability changes.

### MNT.10:12 - Relations

[MNT.1](#mnt1---identify-the-maintained-system-use-and-permission-boundary) supplies the required functioning and [MNT.9](#mnt9---perform-and-record-the-maintenance-intervention) the performed intervention and resulting state. [MNT.8](#mnt8---isolate-make-safe-and-authorize-the-intervention) governs test protection; [MNT.7](#mnt7---coordinate-intervention-and-continuing-operation) includes its time. [MNT.11](#mnt11---certify-hand-back-and-authorize-resumed-use) consumes the supported functioning claim for hand-back. [MNT.12](#mnt12---maintain-maintenance-information-and-configuration-continuity) retains the useful evidence and [MNT.13](#mnt13---coordinate-the-maintenance-programme-and-fleet-learning) addresses later recurrence learning. FPF [B.3](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#b3---trust-and-assurance-calculus), [A.10](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a10---evidence-graph-referring-claim-bound-evidence-and-provenance-graph) and [C.16](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c16---measurement-metrics-characterization-mmchr) support assurance, evidence and measurement.

### MNT.10:End

## MNT.11 - Certify, Hand Back, and Authorize Resumed Use

> **Type:** Method
> **Status:** Draft

### MNT.11:1 - Problem frame

Use this pattern when maintenance control is being returned to operation and the receiving person needs a supported basis to resume use. The work is complete and functioning has been checked, but restrictions, configuration changes or required release authority are still unresolved.

Reconcile the evidence and actual state, obtain certification where the concrete use requires it, transfer control and establish the operative permission for resumed use. The result can be unrestricted use, supported restricted use or the precise missing condition. This pattern is not a prerequisite for completing maintenance advice.

### MNT.11:2 - Problem

Task completion, functioning evidence, a certificate and permission to operate can support different claims. Treating them as one “released” status can leave the operator unaware of an outstanding limitation or can imply authority that the signer does not hold.

Hand-back can also fail physically: the expected configuration, controls, access arrangements or temporary restrictions may not match what is actually returned.

### MNT.11:3 - Forces

Operation needs a clear timely return, while relevant assurance and protection cannot be inferred from urgency. A restricted use can preserve service but imposes conditions that the receiving people must be able to maintain. Excessive generic sign-offs add delay; missing an applicable release condition can invalidate the intended use.

### MNT.11:4 - Solution

Identify the receiving use and its decision holder. Recover what that holder needs to take control: the actual configuration, supported functioning, material unfinished work and restrictions. The receiving use may differ from the original unrestricted plan; make that change explicit.

Reconcile the intervention and verification accounts with the actual returned state. Confirm the relevant temporary arrangements have the disposition required by the applicable procedure. A temporary test configuration is not assumed to be the final operating configuration. Where actual state remains unknown, identify the observation or competent return that can resolve it.

Obtain certification or independent returns when the equipment, contract, rule or consequence requires them. Identify the claim each return supports and the authority of its issuer for that scope. A certificate about a component or specified task does not automatically establish the whole System's readiness for every use.

Resolve remaining limitations through the applicable decision. Some defects or unfinished work permit a defined restricted use; others prevent the intended operation. The restriction must be technically supported, permitted and practically maintainable by the receiving operation. If no such basis exists, return the unmet condition rather than relabelling the state as temporary permission.

Transfer control so that maintenance and operation know who controls the next state change. Communicate the configuration and conditions that change the receiver's action, using the existing hand-back arrangement. One person may hold both responsibilities, but the evidence and decisions remain distinguishable.

Record or communicate the resulting permission at the level the actual use and operative requirements need. Do not create a universal release certificate for every machine. Conversely, a framework's preference for a small useful result cannot cancel a concrete requirement.

Reopen the hand-back result when its configuration, functioning, restrictions or authority basis changes. A completed maintenance recommendation remains usable within its earlier scope even if the proposed intervention's release is still unavailable.

### MNT.11:5 - Archetypal Grounding

In the extended PS17 case, [MNT.9](#mnt9---perform-and-record-the-maintenance-intervention) records the bearing intervention and installed configuration C42. [MNT.10](#mnt10---verify-restored-functioning) supports the stated immediate duty, not an untested winter peak or long-term recurrence claim.

The authorized receiving operator reconciles the returned state with those results. The applicable restoration procedure is completed, relevant temporary test arrangements have their required disposition, and control is transferred. The operating decision then permits the supported resumed use within the case's conditions. These events are constructed teaching observations, not a real authorization.

In a limited branch, the functioning check is satisfactory but the required receiving authority is unavailable. The functioning evidence remains valid at its scope, while the intended resumed-use decision is outstanding. The team does not treat the technician's task-completion entry as a substitute.

Aviation illustrates why the distinction matters. EASA's September 2025 Part-145 guidance distinguishes certification of the specified maintenance from the separate responsibility for an aircraft's continuing airworthiness. This dated illustration is not a complete current legal basis and is not transferred as a certification requirement for PS17.

### MNT.11:6 - Bias-Annotation

“Released” is often a single software status even when several people and claims are involved. Recover its meaning for the receiving use. Operators can also accept an inconvenient restriction in the moment without having the means to maintain it through the next shift.

### MNT.11:7 - Conformance Checklist

Can the receiving person identify the actual returned configuration and supported functioning? Are material unfinished work and restrictions resolved for the intended use? Are required certificates or independent returns applicable and issued within their authority? Has control been transferred, and is the resumed-use permission supported?

A qualified restricted-use or missing-condition answer can close the hand-back question. It does not automatically complete the intended unrestricted operation.

### MNT.11:8 - Common Anti-Patterns and How to Avoid Them

A component certificate is read as whole-System permission. Recover the certified claim and the still-needed operating decision. A successful test is treated as a physical hand-back while temporary controls remain in the test state. Reconcile actual restoration and control.

A recommendation is withheld until release paperwork exists. Return the adequate advice at its own boundary; obtain release only for the selected actual use.

### MNT.11:9 - Consequences

The receiver knows what can be used, under which conditions and who controls the next action. A technically successful repair may still await permission; a supported restricted use may return earlier than an unrestricted one. Communication is focused on action-changing conditions and applicable requirements.

### MNT.11:10 - Architectural Rationale

Hand-back joins the evidence and control needed by operation without collapsing their kinds. It remains separate from [MNT.10](#mnt10---verify-restored-functioning) because “functioning supported” and “use permitted” can truthfully have different outcomes. Certification is a conditional contributor, not the universal definition of maintenance completion.

### MNT.11:11 - SoTA-Echoing

The practice question is what a maintenance completion claim permits the receiver to infer. This pattern adapts the bounded certification distinction in [EASA's September 2025 Part-145 guidance, GM1 145.A.50(a)](https://www.easa.europa.eu/en/document-library/easy-access-rules/online-publications/easy-access-rules-continuing-airworthiness?erules-id=ERULES-1963177438-272). Against a single undifferentiated release status, the exact change is separate reconciliation of functioning, certification, control and permission. It accepts a small amount of explicit hand-back reasoning to prevent an unsupported whole-use claim. The [edition notice](https://www.easa.europa.eu/en/document-library/easy-access-rules/easy-access-rules-continuing-airworthiness) identifies unincorporated later requirements; live aviation work needs its applicable current legal sources. Reopen when the receiving use, state or permission basis changes.

### MNT.11:12 - Relations

[MNT.9](#mnt9---perform-and-record-the-maintenance-intervention) supplies performed-work evidence and [MNT.10](#mnt10---verify-restored-functioning) qualified functioning. [MNT.8](#mnt8---isolate-make-safe-and-authorize-the-intervention) supplies the protection and restoration conditions that remain applicable; [MNT.12](#mnt12---maintain-maintenance-information-and-configuration-continuity) preserves configuration continuity. [MNT.1](#mnt1---identify-the-maintained-system-use-and-permission-boundary) identifies the operating control boundary. FPF [A.2.8.PER](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a28per---granted-permission-exercise-and-non-prohibition) governs permission and [B.3](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#b3---trust-and-assurance-calculus) supports claim-specific assurance.

### MNT.11:End

# Part D - Information, Programme, Methods, Simultaneous Work, and Culture

## MNT.12 - Maintain Maintenance Information and Configuration Continuity

> **Type:** Method
> **Status:** Draft

### MNT.12:1 - Problem frame

Use this pattern when a maintenance decision depends on connecting service history to the correct unit, installed part, configuration or applicable description. The work log says a bearing was replaced, the stock system says it was returned and the condition trend still carries the previous unit's identifier.

Restore a usable information basis for the receiving maintenance question. Reuse [SYSE.13](SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse13---establish-configuration-identity-variants-and-effectivity)'s configuration identity and effectivity contribution; this Method adds the service-event and exposure continuity that maintenance decisions consume. A new database, complete digital twin or plant-wide inventory is unnecessary when a smaller reconciliation answers the question.

### MNT.12:2 - Problem

The same part number can identify a design used by many physical units. A new document edition can exist while the installed machine remains unchanged. A planned replacement can appear in a system before the work occurs. Treating those entries as one current configuration can attach evidence to the wrong subject.

History can also lose the difference between failure, inspection, preventive removal and restoration. A later policy comparison then counts unlike events or assigns exposure to a component after it was removed.

### MNT.12:3 - Forces

More detail supports future analysis but burdens people recording work under time pressure. A unified schema can aid retrieval while concealing meaningful local distinctions. Preserving provenance helps resolve disagreement, but retaining obsolete duplicated “current” records creates another disagreement. Keep one usable account for the decision and recoverable supporting sources where needed.

### MNT.12:4 - Solution

Start from the receiving maintenance decision and its required distinctions. A spare-applicability question needs different history from a recurrence study or a hand-back. Identify the actual unit, component individuals and configuration changes that can affect that use.

Recover the configuration basis under SYSE.13. Distinguish actual, intended and unknown installed state; part or variant descriptions; document editions; and the conditions under which a description applies. A date or shared label cannot establish those correspondences by itself.

Connect the maintenance events to that basis over time. Preserve relevant installation, removal, inspection, condition, intervention and restoration facts, including the sources that support them. Where exposure matters, establish which unit or component accumulated it during which interval and under what operating conditions. A replaced component does not inherit the predecessor's age merely because the equipment tag is unchanged.

Resolve contradictions according to their consequence. A stock return may refer to unused material while the intervention record identifies the installed part. Compare subject, event, time and identifier scheme before treating the records as inconsistent. If they actually conflict, use the available observation or accountable source that can resolve the receiving question; preserve uncertainty when it cannot.

Maintain the intended user's ability to retrieve and interpret the result. Use the existing work log, engineering system or maintenance database when it can carry the necessary relations. Avoid copying one mutable current-state claim across several manually edited files. A source history can remain historical while one current account describes the relevant installed state.

Keep corrections distinguishable from new physical events. Correcting a mistaken serial number changes the account; replacing the component changes the machine. A Method or software change can also alter the meaning of a code without changing earlier events. Preserve the interpretation needed for comparison instead of silently recoding the past as if the categories were always identical.

Return the qualified information basis, its source links and any uncertainty that changes the next use. If the present question is answered, stop. Broader data repair is selected only when another real use warrants the work. Where retention or access is governed by operative requirements, preserve those obligations without inventing a new universal retention rule.

### MNT.12:5 - Archetypal Grounding

In the extended constructed PS17 case, the pre-intervention configuration C41 contains bearing R551. The performed intervention removes R551 and installs compatible bearing R607. C42 identifies the resulting installed configuration under the same approved design basis.

The work record describes those events. The condition account before the intervention concerns C41; the functioning test after it concerns C42. The change of record alone would not have established that installation, and the new bearing does not erase the older unit's useful failure history.

Suppose the stock system also lists R607 as returned. The receiving question is whether the functioning evidence concerns the actually installed bearing. The team compares the material movement and intervention evidence and obtains the relevant physical or accountable return if the conflict remains. It does not average the two records into a “probably current” state.

In the fleet case, two preventive removals originally coded as failures are corrected as descriptions of those events, not counted as new maintenance occurrences. Exposure is assigned to the component intervals that actually existed. That smaller reconciliation can restore a usable comparison without migrating the whole fleet database.

### MNT.12:6 - Bias-Annotation

A central database may seem more authoritative than an inconvenient local observation. Conversely, a practitioner's recollection can override a traceable record without adequate evidence. Use the claim's subject and evidential support, not the prestige of its storage location.

### MNT.12:7 - Conformance Checklist

Can the recipient connect the relevant events and evidence to the actual unit and configuration? Are intended, observed and unknown states distinguishable? Are part individuals, descriptions and editions kept separate where they affect applicability? Are exposure and event meanings compatible with the intended comparison?

The information basis is complete for its receiving use, not necessarily for every future analysis. Material uncertainty remains visible rather than being hidden by a current-status field.

### MNT.12:8 - Common Anti-Patterns and How to Avoid Them

The equipment tag is treated as a lifetime identifier for every replaceable component. Recover component intervals when failure or life claims depend on them. A planned configuration is marked current before installation. Establish the actual state separately.

Every record discrepancy triggers a new digital-twin project. Resolve the contradiction needed by the present decision first and return any genuinely broader need on its own merits.

### MNT.12:9 - Consequences

Condition, policy and hand-back decisions can refer to the same actual maintenance history without confusing records with the machine. Some data remains qualified or incomplete. The cost of maintaining useful correspondence is concentrated on the distinctions that affect use.

### MNT.12:10 - Architectural Rationale

General configuration identity belongs in SYSE.13. Maintenance adds event meaning, exposure intervals and continuity across service replacements. Keeping that domain contribution here avoids both duplicating the configuration Method and leaving fleet learning dependent on uninterpretable work-order counts.

### MNT.12:11 - SoTA-Echoing

The practice question is which information is sufficient for a maintenance decision across changing installed state. This pattern adopts [SYSE.13](SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse13---establish-configuration-identity-variants-and-effectivity)'s distinction between actual configuration, descriptions and effectivity, and adapts GFMAM's maintenance-information concern to service events and exposure. Against a latest-record-only default, the exact change is the time-bound event/configuration correspondence in the Solution and C41-to-C42 case. It accepts focused provenance work while rejecting a complete information-platform replacement as an automatic prerequisite. Reopen when an event definition, installed state or receiving comparison changes. See [GFMAM's information-management account](https://www.gfmam.org/sites/default/files/2021-02/GFMAM%20Maintenance%20Framework%20-%202nd%20Edition%20Final.pdf).

### MNT.12:12 - Relations

[SYSE.13](SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse13---establish-configuration-identity-variants-and-effectivity) supplies configuration identity and effectivity. [MNT.3](#mnt3---establish-degradation-and-failure-evidence) and [MNT.4](#mnt4---monitor-and-interpret-current-condition) consume failure and condition history; [MNT.5](#mnt5---prepare-maintenance-service-capability-spares-tools-and-authority) uses applicability; [MNT.9](#mnt9---perform-and-record-the-maintenance-intervention)–[MNT.11](#mnt11---certify-hand-back-and-authorize-resumed-use) supply intervention, functioning and hand-back facts. [MNT.13](#mnt13---coordinate-the-maintenance-programme-and-fleet-learning) uses comparable population history. FPF [A.10](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a10---evidence-graph-referring-claim-bound-evidence-and-provenance-graph) supports evidential qualification.

### MNT.12:End

## MNT.13 - Coordinate the Maintenance Programme and Fleet Learning

> **Type:** Method
> **Status:** Draft

### MNT.13:1 - Problem frame

Use this pattern when maintenance decisions span a population of equipment and repeated work: which policies to retain, where support is inadequate and what can be learned from the accumulated history. A fleet report shows fewer failures in one group, but its operating exposure and maintenance conditions differ.

Return a qualified programme or fleet-learning decision. The result can be to retain an adequate programme, correct one misleading comparison or change a supported policy or resource arrangement. A fleet maintenance programme remains a maintenance question. An asset-management question can concern just one pump: compare continued use, renewal, replacement, repurposing or withdrawal by the desired value, costs, risks and service alternatives over the relevant horizon. Maintenance consequences inform that choice without settling it. Portfolio acquisition and disposal are further asset-management uses, not the scale boundary between the fields.

### MNT.13:2 - Problem

Local repairs can repeatedly succeed while the programme leaves the same failure, delay or support deficiency untouched. Conversely, crude fleet comparisons can trigger a large policy change on weak evidence.

A programme is the arrangement of maintenance policies, support and work for an identified population. Its document describes that arrangement. Writing a new programme does not establish that it was enacted or improved equipment performance.

### MNT.13:3 - Forces

Common policies and resources can improve continuity, but equipment, duty and consequences vary. Pooling data increases apparent sample size while possibly mixing unlike events. Fleet-wide improvement can consume access and specialist capacity needed for current service. Compare gains and burdens for operation, maintenance staff and affected service users.

### MNT.13:4 - Solution

Bound the population, service question and horizon. Identify the programme decision at stake: retain a policy, change a task, improve spare readiness, resolve a backlog or compare performance. An equipment-family name alone does not establish that units have comparable duty or failure behaviour.

Recover the event and exposure basis under [MNT.3](#mnt3---establish-degradation-and-failure-evidence) and MNT.12. Distinguish failures, inspections, preventive removals and incomplete observation. Compare units at compatible configuration, operating conditions and consequence where those differences can change the answer. Retain a stratified account when aggregation would conceal the difference.

Relate the observations to possible programme causes and actions. Repeated waiting for an applicable spare can justify a support decision without proving that the preventive policy is ineffective. A changed reporting rule can increase counted failures without worsening the machine. Use the failure and operating evidence to distinguish these interpretations.

Compare credible programme alternatives. Retain a sound existing arrangement, change one policy family, improve support, alter coordination or return a design question as appropriate. Include the total obtaining and continuing burden of the change, its effect on service and any protected trade-offs. A local cost reduction that increases shared downtime is not an unqualified programme gain.

When a deliberate improvement is selected, use [E.23](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#e23---quality-improvement-loop-method)'s loop at this subject: name the programme arrangement and the maintenance contribution sought, choose the evaluation that will judge it, perform the selected change only when authorized, and compare the changed arrangement through the same relevant measures. Selection, implementation and observed effect remain different facts.

Choose further fleet inquiry only when its attainable result can change the decision enough to warrant its design, access, measurement, interpretation and displaced work. If current evidence already supports retaining the policy or fixing a known support deficiency, return that answer now. Sparse or incomparable data withholds the stronger causal claim, not every programme decision.

Return the decision with the population and evidence limits that affect its use. Identify the recurrence, changed duty, support failure or new professional result that would reopen it. A long-term learning question can remain open while today's programme answer is complete.

### MNT.13:5 - Archetypal Grounding

APP-MNT-02 is a constructed comparison of 48 pumps. Twenty units have four relevant failures over 20,000 operating hours; 28 units have six over 56,000 hours. The rates are 0.20 and approximately 0.107 events per 1,000 hours. Raw counts favour the first group, while exposure-adjusted rates favour the second.

Neither result establishes a causal policy effect. The engineer recovers duty, component histories, event definitions and the reasons units entered each group. The answer to “Do these counts justify replacing the fleet policy?” is no on this basis. In the retention branch of this constructed case, the policy's existing failure-and-response basis remains adequate for the stated duties; the counts do not establish that adequacy. Retaining the policy on that existing basis can be the completed decision while the support deficiency below is corrected. If that basis no longer holds, return the unsupported policy choice without waiting for these data to prove a rival policy.

The same current records identify an applicable spare unavailable for a known upcoming task. Correcting that support deficiency can be selected on its own evidence; the engineer does not wait for a new causal fleet study to address it.

If a different question warrants a policy comparison, its achievable design must account for the small event count, available population and operating constraints. It may support only a narrower conclusion. The first return remains valid without commissioning that further inquiry.

### MNT.13:6 - Bias-Annotation

Fleet averages can hide the units with the greatest exposure or service consequences. Improved reporting can appear as worse reliability. Programmes also tend to count scheduled labour while omitting operator work, waiting and corrective disruption. Preserve those differences where the decision depends on them.

### MNT.13:7 - Conformance Checklist

Is the population and receiving programme decision clear? Do event meanings, exposure and observation conditions support the comparison? Are causal and descriptive claims distinguished? Does the selected change improve the intended maintenance contribution without concealing moved burden? If implementation or improvement is claimed, is that claim supported separately from the proposal?

An adequate retained programme or qualified fleet account is a completed answer. Further inquiry needs its own attainable contribution and burden justification.

### MNT.13:8 - Common Anti-Patterns and How to Avoid Them

Fewer failures are read as a better policy without exposure. Recover a compatible comparison. A dashboard target is improved by recoding failures rather than changing functioning. Preserve event meaning and compare the actual programme contribution.

Every incomplete causal explanation becomes a research programme. Return the supported maintenance decision first and select only the inquiry that can improve a real next use.

### MNT.13:9 - Consequences

Repeated work can change the programme when the evidence warrants it, while adequate policies avoid unnecessary churn. Some comparisons remain descriptive or population-limited. Learning effort is directed toward maintenance decisions rather than data accumulation for its own sake.

### MNT.13:10 - Architectural Rationale

Programme coordination joins policies, support and population evidence because changes in one can explain apparent changes in another. It is broader than [MNT.2](#mnt2---select-and-reopen-the-maintenance-policy)'s task policy and [MNT.6](#mnt6---diagnose-condition-and-select-an-intervention)'s present intervention, but does not subsume the asset-value choice for one asset, an asset System or a portfolio. The question and justified result distinguish the contributions; the number of assets does not.

[E.23](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#e23---quality-improvement-loop-method) supplies the reusable improvement organization. This pattern supplies the maintenance population, event meaning, response alternatives and operating consequences that make the loop useful here.

### MNT.13:11 - SoTA-Echoing

The question is how fleet evidence should change a maintenance programme. This pattern adapts GFMAM's programme-management breadth and the consequence-oriented evaluation concern in the 2025 NIST review, with [E.23](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#e23---quality-improvement-loop-method) supplying conditional improvement. Against raw-count ranking or automatic technology expansion, the exact mutation is the qualified population comparison and separate support-deficiency decision. It accepts narrower conclusions when comparison is weak, preserving a useful current answer. Neither source proves that a particular policy will win in this fleet. Reopen with changed exposure, failure meaning, operating consequences or applicable evaluation evidence. See [GFMAM](https://www.gfmam.org/sites/default/files/2021-02/GFMAM%20Maintenance%20Framework%20-%202nd%20Edition%20Final.pdf) and [NIST's evaluation review](https://www.nist.gov/publications/comprehensive-evaluations-condition-monitoring-based-technologies-industrial).

### MNT.13:12 - Relations

[MNT.2](#mnt2---select-and-reopen-the-maintenance-policy) supplies policies, [MNT.5](#mnt5---prepare-maintenance-service-capability-spares-tools-and-authority) support and [MNT.12](#mnt12---maintain-maintenance-information-and-configuration-continuity) usable history. [MNT.3](#mnt3---establish-degradation-and-failure-evidence) qualifies failure claims; [MNT.14](#mnt14---compare-and-refresh-maintenance-methods) compares Method changes and [MNT.16](#mnt16---deliberately-continue-and-change-maintenance-culture) addresses actual continuation in the practice. FPF [E.23](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#e23---quality-improvement-loop-method) supplies improvement, [C.16](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c16---measurement-metrics-characterization-mmchr) measurement and [C.11.DUA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11dua---decision-useful-advice-and-evidence-demands) conditional inquiry. Engineering Asset Management receives the specific investment or retirement question when maintenance cannot settle it.

### MNT.13:End

## MNT.14 - Compare and Refresh Maintenance Methods

> **Type:** Method
> **Status:** Draft

### MNT.14:1 - Problem frame

Use this pattern when an established way of doing maintenance may no longer be the best answer for the current failure, equipment or operating setting. A new predictive tool is proposed, or a once-useful inspection produces little actionable information.

Compare the pertinent Methods and return a justified retain, revise, replace, branch or stop decision. Here a Method is the reusable way of obtaining a maintenance result; a software product or manual can support or describe it. A new trial is selected only when it can provide worthwhile attainable information.

### MNT.14:2 - Problem

A Method can appear superior because it was evaluated on easier equipment, a different consequence or a narrower burden. Changing the tool can be advertised as changing the Method even when the practitioner does the same work. Conversely, a small change in interpretation or response can materially change the Method while leaving the software unchanged.

A useful comparison needs the same receiving maintenance question, supported alternatives and a truthful account of what changes in practice.

### MNT.14:3 - Forces

New Methods can improve detection or response while adding training, integration, false alarms and dependence on a supplier. Keeping a familiar Method reduces transition cost but can retain an ineffective task. A controlled trial can reduce uncertainty, but a small fleet or restricted access may make its promised answer unattainable.

### MNT.14:4 - Solution

State the maintenance result and conditions for the comparison. Recover the failure mechanism, consequence, condition information, support, access and operating needs that can change the answer. Compare the current Method with plausible alternatives at that same use.

Describe the action-changing difference. Is the candidate a different task, a changed trigger, another diagnostic interpretation, a revised response rule or only a different description or software implementation? Keep those objects distinct when continuity, training or evaluation depends on them. A useful Method change should alter what the practitioner notices, decides, does, needs or obtains.

Compare practical worth over a relevant horizon. Include preparation, acquisition, configuration, competence, interpretation, false responses, missed conditions, maintenance of the tool, supplier dependence and exit where they matter. Use [ME.14](METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me14---evaluate-practical-worth-against-current-alternatives) for the practical-worth comparison and [ME.15](METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me15---maintain-method-variants-provenance-and-reuse) when variant identity or maintenance of the repertoire needs that more general Method.

Test the candidate against a consequential unlike case. A Method useful for a visible degradation trend may not expose a hidden protection failure. An online predictor may improve timing while remaining unusable where the support lead time is longer than its warning. These differences can justify branching the repertoire instead of replacing one Method everywhere.

Use existing evidence first. If it already establishes that the candidate cannot support the needed response, reject it for that use without a trial. If it supports retaining the current Method, return that decision. When an uncertainty could change the choice, assess what a feasible trial or analysis could actually discriminate and the whole burden of obtaining that result. Do not turn a possible study design into an obligatory next task.

Select the supported continuation. State the changed or retained Method and its applicability, the description or tool that will carry it, any real transition support and the condition for reopening the choice. A selected change remains a proposal until performed. Claims about improved maintenance outcomes require evidence at the relevant use, not just successful installation of a tool.

Refresh selectively when a failure, operating condition, support arrangement or answer-changing source result changes. An annual reminder can prompt attention, but currentness is established by the comparison that matters, not a date stamp.

### MNT.14:5 - Archetypal Grounding

A constructed fleet comparison considers replacing periodic condition interpretation with an online predictive service. The new service produces a more frequent remaining-life estimate, but the recurring maintenance decision is whether an actionable warning arrives in time for applicable support and access.

For the current use, existing provider information shows no improvement in the feasible response: the same specialist and part constraint dominates, while the new arrangement adds interpretation and integration work. The engineer retains the current Method and addresses the support deficiency. No new live trial is needed to answer that question.

A different unit family has a supported rapidly changing condition and a genuinely available response. The candidate may be useful there. A bounded comparison can therefore select a separate Method variant instead of a fleet-wide replacement, provided the obtainable evidence warrants the change.

In PS17, long-horizon recurrence remains unresolved after the local repair. The current account can be retained while a future Method comparison is reserved for evidence that changes the policy or response. “Complete a new trial” is not a universal stop condition.

### MNT.14:6 - Bias-Annotation

Technology labels and benchmark accuracy favour visible novelty. Familiarity favours the incumbent. Compare both at the same maintenance result and burden, including effects outside the team purchasing the tool.

### MNT.14:7 - Conformance Checklist

Are the compared Methods and their practical differences identifiable? Do they answer the same maintenance question at comparable conditions and effort? Are implementation, transition and continuing burdens included where material? Does the decision preserve unlike uses through an appropriate retain, branch or replacement result?

Any trial has an attainable decision-changing purpose. A supported comparison can close without new experimentation or adoption.

### MNT.14:8 - Common Anti-Patterns and How to Avoid Them

A higher model score is treated as a better maintenance Method. Follow the prediction through interpretation, support and actual response. A software upgrade is called a Method change without an action-changing difference. State what the practitioner does differently.

A comparison ends only after a trial because the template requires one. Use current evidence when it already settles the choice; select a trial only for the remaining worthwhile uncertainty.

### MNT.14:9 - Consequences

The maintenance repertoire changes where practical evidence warrants it and remains stable where it already works. Some new approaches are retained as bounded variants rather than universal replacements. Transition and continuing support costs become part of the choice.

### MNT.14:10 - Architectural Rationale

Method refresh is distinct from changing one policy parameter or executing one repair. It concerns the reusable way of obtaining results and its continued usefulness. Reusing [ME.14](METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me14---evaluate-practical-worth-against-current-alternatives)/15 prevents duplication of general comparison and variant reasoning; the failure, support and service conditions remain this pattern's domain contribution.

### MNT.14:11 - SoTA-Echoing

The practice question is when a new maintenance approach is worth adopting. This pattern adapts [ME.14](METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me14---evaluate-practical-worth-against-current-alternatives)/15 and the consequence-oriented line in the [2025 NIST review](https://www.nist.gov/publications/comprehensive-evaluations-condition-monitoring-based-technologies-industrial). Against a predictive-to-autonomous maturity ladder, the exact mutation is a same-use, whole-burden comparison with retain and branch outcomes. Better prediction remains a possible contribution, not a sufficient adoption argument. The source evidence does not establish universal comparative effectiveness. Reopen with an attainable new capability, changed failure or operating need, or evidence that reverses the practical comparison.

### MNT.14:12 - Relations

[MNT.2](#mnt2---select-and-reopen-the-maintenance-policy) supplies policy questions; [MNT.3](#mnt3---establish-degradation-and-failure-evidence)/4 supply failure and condition knowledge; [MNT.5](#mnt5---prepare-maintenance-service-capability-spares-tools-and-authority)/7 supply response feasibility; [MNT.13](#mnt13---coordinate-the-maintenance-programme-and-fleet-learning) supplies programme consequences. [ME.14](METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me14---evaluate-practical-worth-against-current-alternatives) supplies practical-worth comparison and [ME.15](METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me15---maintain-method-variants-provenance-and-reuse) Method-variant maintenance. FPF [C.11.DUA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11dua---decision-useful-advice-and-evidence-demands) governs a demanded trial's contribution and burden, while [G.11](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#g11---telemetry-driven-refresh-and-decay-orchestrator) supports selective refresh.

### MNT.14:End

## MNT.15 - Reconcile Simultaneous Maintenance, Operation, and Support Work

> **Type:** Method
> **Status:** Draft

### MNT.15:1 - Problem frame

Use this pattern when individually plausible maintenance, operating and support plans cannot be performed together. Two jobs fit their own windows but need the same qualified specialist; an operating fallback depends on equipment that another job intends to isolate.

Recover the actual shared demands and choose a feasible coordination change, or state the unmet combined commitment. A simple resource or dependency bound can be enough. Use [C.32.MWA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c32mwa---practice-architecture-synthesis-from-several-structures) or [ME.6](METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me6---compare-method-architecture-alternatives-and-simultaneous-enactment-conflicts) only when the question requires a broader practice-architecture comparison across different structures.

### MNT.15:2 - Problem

Separate plans can each be valid while their combination is impossible. A Method's steps, actual Work overlaps, System dependencies, provider allocation and authority are different relations. Their descriptions may be drawn as aligned boxes even when the practice does not align that way.

Solving one local conflict can move the burden to operation, an unqualified provider, an exhausted specialist or an unavailable fallback.

### MNT.15:3 - Forces

Shared resources improve utilization while making simultaneous commitments fragile. Combining outages can reduce disruption but increase interference and recovery consequences. Extra capacity can resolve a timing conflict only if it is actually capable, available and permitted. The arrangement must preserve the relevant service and protection conditions as a whole.

### MNT.15:4 - Solution

Name the combined commitment and the conflict that changes it. Use the actual or proposed work and operating horizon. A prospective schedule is not evidence that the work occurred.

Choose only the structures needed to explain the conflict. For a shared specialist, work duration and provider availability may suffice. For simultaneous isolation and fallback, the maintained Systems, operating dependencies and protection authority also matter. A description's nesting does not establish work order or resource independence.

Recover shared demands using compatible quantities and conditions. Distinguish elapsed time from person-hours, nominal capacity from available qualified capacity and sequential dependence from possible overlap. Include common-mode dependencies that could invalidate a fallback or protection assumption.

Compare the whole combination. A condition applying to all selected work cannot be established by approving each job separately. Locate the overload, interference or unsupported transition and determine which alternatives change it: defer a supported job, select another window, obtain another qualified provider, change permitted operating rate or revise the intervention arrangement.

Evaluate what each apparent repair moves elsewhere. A second provider may need access, familiarization and its own support. Deferral changes the failure consequence. A longer shift changes fatigue and protection conditions. A shared outage can remove the recovery option that made each individual plan acceptable.

If the conflict requires a different organization of the practice, use [C.32.MWA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c32mwa---practice-architecture-synthesis-from-several-structures) or [ME.6](METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me6---compare-method-architecture-alternatives-and-simultaneous-enactment-conflicts) to compare the relevant Method, Work, System, provider and description structures. Preserve their actual relations rather than making one universal layer stack. If the simple bound already answers the question, stop there.

Return the selected arrangement or the exact combined commitment that cannot be met. Identify the people with authority over the changed work and operation. Reopen when a shared resource, interruption, protection condition or service requirement changes.

### MNT.15:5 - Archetypal Grounding

APP-MNT-03 uses a constructed packaging-plant arrangement. Two jobs each require four hours of the same qualified specialist inside one six-hour access window. Their eight-hour combined specialist demand exceeds the six available hours. Each job fits separately; the combination does not.

Preparatory work can overlap continuing production where its access and resources permit. That does not create a second specialist. Reordering two four-hour demands also cannot make their total fit the same six-hour single-person window.

The team compares deferring the lower-consequence job, obtaining another suitable window, using a genuinely qualified additional provider or changing the supported operating arrangement. [MNT.6](#mnt6---diagnose-condition-and-select-an-intervention) supplies the consequence of deferral; [MNT.5](#mnt5---prepare-maintenance-service-capability-spares-tools-and-authority) establishes any added provider's readiness. The selected alternative changes a real constraint rather than the appearance of the schedule.

If an unplanned extension would leave the specialist unable to perform the later protected task adequately, the allocation or timing changes. “Use more care” does not close that capability question.

For a broader conflict, suppose both jobs rely on the same standby equipment while each plan treats it as independent fallback. The decision now needs the System and operating-dependency structures as well as time. That is a reason to expand the comparison, not to derive an architecture from the schedule's page layout.

### MNT.15:6 - Bias-Annotation

Local planners see their own job's benefits and can assume a shared resource is available because it appears in their plan. Cross-team costs are often assigned to “coordination” without anyone receiving the actual unresolved demand. Name the consuming work and affected operation.

### MNT.15:7 - Conformance Checklist

Does the comparison include every shared demand that can defeat the combined commitment? Are quantities, resource availability and dependencies compatible? Does the selected change alter a real constraint? Are moved burden, failure consequences and protection conditions retained? Do the relevant decision holders control the changed arrangement?

A supported simple bound can complete the question. A comprehensive architecture model is needed only when its additional relations change the answer.

### MNT.15:8 - Common Anti-Patterns and How to Avoid Them

Both jobs are approved, so the programme is assumed feasible. Check the whole shared demand. A second team is added on paper while both depend on the same specialist or tool. Recover the actual independence.

A schedule conflict becomes a universal reorganization project. Use the smallest constraint or structure set that resolves the present coordination question.

### MNT.15:9 - Consequences

The combined arrangement can be judged on actual capacity, service and protection rather than local plan validity. Some commitments are deferred or renegotiated. Broader architectural work remains available when a narrow repair would merely move the conflict.

### MNT.15:10 - Architectural Rationale

[MNT.7](#mnt7---coordinate-intervention-and-continuing-operation) coordinates an intervention with continuing operation; this Method addresses simultaneous commitments whose common conditions cannot be established pairwise. It reuses general cross-structure synthesis only when that larger question is real.

The example's arithmetic is deliberately simple. A more elaborate optimizer is justified by an unresolved decision, not by the existence of several jobs.

### MNT.15:11 - SoTA-Echoing

The question is why individually feasible maintenance plans fail together. This pattern adapts [C.32.MWA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c32mwa---practice-architecture-synthesis-from-several-structures)'s conflict-and-moved-burden comparison to maintenance resources, fallback and protected work. Against copying a work-breakdown diagram as the practice architecture, the exact additions are actual-relation recovery and the whole-demand test. It accepts a bounded cross-team comparison to expose a shared constraint while retaining the simple-arithmetic stop. Preparation-aware scheduling research supplies an optional overlap alternative, not proof of independent resources or live effectiveness. Reopen when a new shared dependency or changed operating commitment alters the combination.

### MNT.15:12 - Relations

[MNT.5](#mnt5---prepare-maintenance-service-capability-spares-tools-and-authority) supplies ready resources, [MNT.6](#mnt6---diagnose-condition-and-select-an-intervention) the consequences of alternative interventions and deferral, and [MNT.7](#mnt7---coordinate-intervention-and-continuing-operation) the individual operating arrangement. [MNT.8](#mnt8---isolate-make-safe-and-authorize-the-intervention) preserves protection across shared work. [C.32.MWA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c32mwa---practice-architecture-synthesis-from-several-structures) and [ME.6](METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md#me6---compare-method-architecture-alternatives-and-simultaneous-enactment-conflicts) support a needed cross-structure architecture comparison. OPS contributes the qualified service and work-management results that the selected coordination consumes.

### MNT.15:End

## MNT.16 - Deliberately Continue and Change Maintenance Culture

> **Type:** Method
> **Status:** Draft

### MNT.16:1 - Problem frame

Use this pattern when the question concerns how maintenance practice is actually continued or changed among people: a hand-back Method is taught, a new diagnostic approach spreads or an older practice persists despite a revised manual.

Return a qualified account of the relevant cultural relations or a supported decision to continue, change, branch or stop an arrangement. Maintenance culture here concerns the generation, transmission, enactment, recognition, selection, retention and loss of practice variants in a stated population. A training release alone does not establish those outcomes.

### MNT.16:2 - Problem

Documents, training attendance and organizational labels are visible, while actual use is harder to observe. A team can receive a new Method description yet continue its previous work. A practice can spread because it is convenient or rewarded without improving maintenance outcomes.

Deliberate intervention and cultural effect also differ. Choosing to alter training or recognition does not establish that practitioners changed their work, that the change persisted or that equipment functioning improved.

### MNT.16:3 - Forces

Shared practice supports continuity but can retain a stale or harmful habit. Local variation can fit a different operating setting while making handover difficult. Observing people consumes time and can change what they do. Reporting incentives, fatigue, access and status differences affect which variants become visible and survive.

### MNT.16:4 - Solution

State the maintenance population, period and receiving question. Identify the relevant Method variant and the work or result whose continuation matters. Use ordinary terms before introducing a cultural label such as school, tradition or maturity.

Recover the cultural relations that the available basis supports. A manual can transmit a description; a mentor can demonstrate a technique; practitioners can enact it in actual work; peers or supervisors can recognize and reward it; the population can retain or abandon it. These are different claims. Use [C.36](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c36---cultural-evolution-and-cultural-evolution-engineering) when their distinction changes the account.

Connect an enactment claim to actual practitioners, work and maintained Systems at the scope needed for that claim. A selected class of technicians or a training plan does not supply an observed occurrence. If a precise performed-Work claim is needed, FPF [A.13](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a13---the-agential-role-agency-spectrum) and [A.15.1](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a151---uwork) govern the performer and occurrence; assignment-bound attribution is added only when that relation is actually consumed.

Compare plausible explanations for the current pattern of use. A variant may persist because it works under local conditions, because suitable tools are available, because reporting rewards it or because another variant cannot be enacted with the available time. Retain hypotheses at their actual support. A population-wide causal explanation may remain unresolved while a bounded current account is complete.

Select a deliberate change only when its attainable contribution warrants the whole burden. The action might change access to applicable descriptions, mentoring, recognition, provider support or the conditions that discourage reporting. Compare keeping, revising, branching and stopping the arrangement. Include effects on practitioners and operation, not just attendance or publication counts.

Keep proposal, performed intervention, changed practice and measured maintenance effect separate. If an intervention is performed, judge it by the relevant actual-use and maintenance consequences. Training completion can establish a training result; it does not by itself establish adoption, reliability improvement or safer work.

Return the supported continuation and its population, period and uncertainty. A new survey or experiment is selected only for a worthwhile attainable answer. When the existing evidence already supports retaining a practice or fixing a known access problem, return that answer without requiring a full cultural study.

### MNT.16:5 - Archetypal Grounding

In a constructed two-shift maintenance team, a revised hand-back description separates performed work, functioning evidence and permission. Six practitioners receive it. That establishes availability to those recipients, not use.

Three observed hand-backs are then described in the teaching case. Two include the relevant configuration and functioning limits; one still treats a closed work order as the complete release. The supported account is limited to those observations. It does not establish the practice of the whole team or a reduction in equipment failures.

The lead finds that the second shift's terminal opens the older hand-back instructions. Correcting that known access problem is a supported intervention option. A new survey is unnecessary to establish the mismatch. Later actual-use observations could support a broader conclusion, but commissioning them is a separate value-and-burden choice.

In another branch, fatigue reports disappear after a reward scheme penalizes unfinished work. The relevant response examines the reporting and allocation arrangement; exhorting practitioners to report honestly leaves the disincentive untouched.

### MNT.16:6 - Bias-Annotation

Visible experts and day-shift work can dominate the account while contractors and night-shift constraints are missed. An observer may see exemplary performance rather than ordinary use. State those limits when generalizing; do not turn a few convenient observations into a population-wide claim.

### MNT.16:7 - Conformance Checklist

Are population, period, Method variant and receiving use clear? Are transmission, enactment, recognition, selection and retention distinguished where the conclusion depends on them? Are proposed changes, performed actions and observed effects separately supported? Does a selected intervention address an actual relation or condition rather than only a label?

A qualified current account or supported continuation can close the request. New inquiry and stronger causal claims need their own attainable contribution and evidence.

### MNT.16:8 - Common Anti-Patterns and How to Avoid Them

“The manual was published, so the culture changed” replaces actual use with availability. Recover the practice observations. “Everyone completed training” becomes a reliability claim. Identify the training result and the still-unestablished maintenance effect.

A cultural problem is answered by adding awareness training when access or incentives prevent enactment. Change the relevant arrangement or preserve that limit in the recommendation.

### MNT.16:9 - Consequences

The maintenance lead can act on a specific continuation problem without overstating adoption or effect. Useful local variants can be retained and access or recognition problems can be addressed. Some broader cultural or causal claims remain unavailable, while the smaller supported account remains complete.

### MNT.16:10 - Architectural Rationale

[MNT.14](#mnt14---compare-and-refresh-maintenance-methods) compares reusable maintenance Methods; this pattern asks how variants are generated and continued in an actual practice population. [MNT.13](#mnt13---coordinate-the-maintenance-programme-and-fleet-learning) evaluates programme consequences. Keeping those questions related but separate prevents a Method choice or programme document from being mistaken for cultural change.

[C.36](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c36---cultural-evolution-and-cultural-evolution-engineering) supplies the general relation distinctions. The maintenance contribution lies in connecting them to enacted diagnosis, intervention, hand-back, provider conditions and fleet consequences.

### MNT.16:11 - SoTA-Echoing

The question is how to choose a useful maintenance-culture intervention from limited evidence. This pattern adapts [C.36](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c36---cultural-evolution-and-cultural-evolution-engineering)'s relation-specific account and conditional inquiry, with CASA's 2026 fatigue-reporting concern as a domain counterexample to awareness-only responses. Against training-count or maturity-label reasoning, the exact mutation is the separate transmission/enactment/effect account and the second-shift access case. It accepts bounded observation and uncertainty while avoiding an unnecessary universal study. The aviation source does not prove the same incentive effect in every maintenance population. Reopen when actual-use evidence, provider conditions or consequences change the continuation decision. See [CASA's account](https://www.casa.gov.au/operations-safety-and-travel/safety-management-systems/sector-safety-risk-profiles/maintenance-activities-sector-safety-risk-profile/fatigue).

### MNT.16:12 - Relations

[C.36](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c36---cultural-evolution-and-cultural-evolution-engineering) supplies cultural-relation and intervention distinctions. [MNT.14](#mnt14---compare-and-refresh-maintenance-methods) supplies the Method-variant question and [MNT.13](#mnt13---coordinate-the-maintenance-programme-and-fleet-learning) programme effects. [MNT.5](#mnt5---prepare-maintenance-service-capability-spares-tools-and-authority), [MNT.9](#mnt9---perform-and-record-the-maintenance-intervention) and [MNT.11](#mnt11---certify-hand-back-and-authorize-resumed-use) supply maintenance support, performance and hand-back situations in which variants are enacted. FPF [C.11.DUA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11dua---decision-useful-advice-and-evidence-demands) governs conditional inquiry, [A.10](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a10---evidence-graph-referring-claim-bound-evidence-and-provenance-graph) evidence and [C.16](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c16---measurement-metrics-characterization-mmchr) measurement. Claims about a changed practice or its effects retain their own support.

### MNT.16:End

# Cross-Pattern Applications

## APP-MNT-01 — PS17: advice, selected intervention and return to use

The constructed case begins on 18 September 2026 with rising bearing-related vibration in PumpTrain-PS17-B, configuration C41. DistrictHeatingOperation-East supplies a qualified capacity result for the stated horizon: its agreed reduced-capacity operation can last four hours under the specified demand and fallback conditions. That operating contribution is the result exchange also identified as XRI-09.

The requested first result is a replacement recommendation. [MNT.1](#mnt1---identify-the-maintained-system-use-and-permission-boundary) bounds the unit and use. [MNT.3](#mnt3---establish-degradation-and-failure-evidence) and [MNT.4](#mnt4---monitor-and-interpret-current-condition) keep the supported failure and condition interpretation separate from an unproved long-term cause. [MNT.6](#mnt6---diagnose-condition-and-select-an-intervention) compares the plausible responses and returns the recommendation from the evidence already adequate for it.

The replacement needs the case's specialist applicability/certification return for the spare. [MNT.5](#mnt5---prepare-maintenance-service-capability-spares-tools-and-authority) identifies that unmet condition. The recommendation is complete, while actual replacement cannot start. The team may prepare compatible information, tools and available support without consuming the protected outage or pretending that the missing return exists.

In the extended branch, the specialist return arrives and the intervention is selected. [MNT.7](#mnt7---coordinate-intervention-and-continuing-operation)'s whole-outage calculation includes shutdown and isolation, the intervention, controlled testing, final restoration, return of control and explicit contingency. The resulting 225-minute plan fits the four-hour bound under the constructed estimates. Its authoritative calculation and delay branch are in [MNT.7](#mnt7---coordinate-intervention-and-continuing-operation); the plan is not a time promise for an unknown pump.

[MNT.8](#mnt8---isolate-make-safe-and-authorize-the-intervention) establishes the applicable actual protection and permission. If an uncontrolled shared energy path is found, the protected work does not start and the arrangement returns for a competent revised decision. The earlier advice remains complete.

In the performed branch, [MNT.9](#mnt9---perform-and-record-the-maintenance-intervention) records removal of bearing R551 and installation of compatible bearing R607. Configuration C42 identifies the resulting installed arrangement under the same approved design basis. [MNT.12](#mnt12---maintain-maintenance-information-and-configuration-continuity) preserves the connection between those events and the earlier C41 history.

[MNT.10](#mnt10---verify-restored-functioning) then checks the immediate-duty claim under the constructed operating basis, using its stated measurements and limitations. [MNT.11](#mnt11---certify-hand-back-and-authorize-resumed-use) reconciles the returned state, transfers control and obtains the operative resumed-use decision. A successful function test does not automatically establish that permission or an untested broader duty.

Long-horizon recurrence remains unresolved. [MNT.13](#mnt13---coordinate-the-maintenance-programme-and-fleet-learning) can retain the current programme account, and [MNT.16](#mnt16---deliberately-continue-and-change-maintenance-culture) can describe the team's observed use only within the constructed case. A further investigation or practice intervention is selected for its worthwhile attainable contribution; it is not required to make the local recommendation or repair result true.

## APP-MNT-02 — A fleet comparison that reverses when exposure is counted

The constructed fleet contains 48 pumps in two groups. One has fewer counted failures but also substantially less operating exposure. [MNT.13](#mnt13---coordinate-the-maintenance-programme-and-fleet-learning) contains the numerical comparison and its decision: the crude rates do not establish a causal policy advantage, and the current policy can be retained.

[MNT.3](#mnt3---establish-degradation-and-failure-evidence) determines what counts as the relevant failure; [MNT.12](#mnt12---maintain-maintenance-information-and-configuration-continuity) connects events and exposure to actual components and configurations. If records mix preventive removals with failures, that discrepancy changes the rate before it changes any policy. A qualified current account is useful even when the data cannot support a strong causal comparison.

[MNT.2](#mnt2---select-and-reopen-the-maintenance-policy) and [MNT.14](#mnt14---compare-and-refresh-maintenance-methods) then examine which task or Method fits the actual failure and response conditions. A known applicable-spare deficiency can be addressed without waiting for a new fleet study. A low-consequence obvious failure and a hidden protective-function failure remain materially different policy cases.

A proposed further comparison needs a question that the available population, time and access can answer. Its acquisition and interpretation burden belongs in the choice. “Collect more data” is not the automatic result of a limited causal account.

## APP-MNT-03 — Individually feasible jobs and one shared specialist

The constructed packaging-plant case has two jobs that each fit a six-hour access window but together exceed the available time of one qualified specialist. [MNT.15](#mnt15---reconcile-simultaneous-maintenance-operation-and-support-work) contains the whole-demand calculation and the alternatives that change it.

[MNT.5](#mnt5---prepare-maintenance-service-capability-spares-tools-and-authority) establishes whether another provider is genuinely available and capable. [MNT.6](#mnt6---diagnose-condition-and-select-an-intervention) supplies the consequences of deferring either job. [MNT.7](#mnt7---coordinate-intervention-and-continuing-operation) relates the chosen arrangement to continuing operation. The solution is a real allocation, timing or supported operating change, or an honest unmet commitment.

Preparation that can overlap production remains useful but does not resolve a shared-person overload. An unplanned extension also changes the capability and fatigue conditions. The team revises allocation or timing rather than treating greater attention as additional capacity.

When a shared fallback or isolation dependency joins the conflict, the comparison expands to those actual System and protection relations. A work-breakdown diagram's hierarchy does not establish them.

# Source Responsibility and References

## Source roles and scope of reliance

This framework is an original selective synthesis, not a replacement edition or complete translation of a Guide, standard or paper. Source accounts contribute to specific decisions; their complete procedures, derivations and jurisdictional provisions remain with the original works.

| Source return | Contribution used here | Limit that changes reliance |
| --- | --- | --- |
| [NASA, Reliability-Centered Maintenance Guide, 2008](https://www.nasa.gov/wp-content/uploads/2023/06/nasa-rcmguide.pdf), task-selection discussion | Historical task-applicability and effectiveness reasoning in MNT.2. | This is not a current universal standard or a universal interval source. |
| [Arts, Boute, Loeys and van Staden, Fifty years of maintenance optimization, 2025](https://orbilu.uni.lu/bitstream/10993/61558/1/1-s2.0-S0377221724005241-main.pdf), EJOR 322(3), 725–739, DOI 10.1016/j.ejor.2024.07.002 | Coupled physical-failure and decision reasoning in [MNT.2](#mnt2---select-and-reopen-the-maintenance-policy)/3; support remains part of feasible response. | Models and the source's data-oriented maturity account do not rank every maintenance practice. |
| [Dadfarnia, Sharp and Herrmann, Comprehensive evaluations of condition monitoring-based technologies in industrial maintenance, 2025](https://www.nist.gov/publications/comprehensive-evaluations-condition-monitoring-based-technologies-industrial), JMS 82, 449–477 | Receiving-use consequences in [MNT.4](#mnt4---monitor-and-interpret-current-condition)/13/14. | Heterogeneous study evidence does not supply a universal effectiveness estimate. |
| [Orošnjak, Saretzky and Kedziora, Prescriptive Maintenance, 2025](https://orbilu.uni.lu/handle/10993/65591), Applied Sciences 15(15), 8507 | The condition-to-action question used in MNT.6. | The inspected abstract and synthesis do not warrant adopting a particular deployed algorithm. |
| [Gan and colleagues, preparation-aware scheduling](https://journals.sagepub.com/doi/abs/10.1177/09544054251350538), 2026 issue, first online July 2025 | Preparation overlap as a candidate choice in [MNT.5](#mnt5---prepare-maintenance-service-capability-spares-tools-and-authority)/7/15. | The inspected abstract's scheduling model supplies neither plant-wide proof nor these case times. |
| [Kasuya and Jin, flexible decision timing, 2026](https://www.sciencedirect.com/science/article/abs/pii/S095183202600342X), DOI 10.1016/j.ress.2026.112528 | Operating-rate and maintenance-timing alternatives in [MNT.7](#mnt7---coordinate-intervention-and-continuing-operation)/14. | The inspected abstract/introduction concerns modeled systems, not universal field transfer. |
| [GFMAM, The Maintenance Framework, second edition, 2021](https://www.gfmam.org/sites/default/files/2021-02/GFMAM%20Maintenance%20Framework%20-%202nd%20Edition%20Final.pdf), §6 | Breadth of task, support, information and programme concerns. | Its subject inventory is not copied as a compulsory Method sequence. |
| [IAM, An Anatomy of Asset Management, version 4, 2024](https://theiam.org/media/5615/iam-anatomy-version-4-final.pdf), §§7.5.9 and 7.7.5 | Maintained function and the relation to value-oriented decisions about an individual asset, an asset System or a portfolio. | Comparing continued use, renewal, replacement, repurposing or withdrawal by value, costs, risks and service effects is broader than MNT's maintained-functioning result; portfolio scale is not compulsory. |
| [OSHA, 29 CFR 1910.147](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.147) | A bounded example of operative energy-control, verification and restoration requirements. | Actual use requires the applicable current rules, scope and equipment procedure. |
| [EASA, September 2025 Part-145 guidance](https://www.easa.europa.eu/en/document-library/easy-access-rules/online-publications/easy-access-rules-continuing-airworthiness?erules-id=ERULES-1963177438-272), 145.A.50 and GM1 145.A.50(a) | Distinguishing specified maintenance certification from a broader use claim in MNT.11. | This is a dated illustration; the [edition notice](https://www.easa.europa.eu/en/document-library/easy-access-rules/easy-access-rules-continuing-airworthiness) identifies missing later requirements. |
| [CASA, maintenance-activities risk profile: Fatigue, 24 April 2026](https://www.casa.gov.au/operations-safety-and-travel/safety-management-systems/sector-safety-risk-profiles/maintenance-activities-sector-safety-risk-profile/fatigue) | A human-performance counterexample to attention-only responses in [MNT.9](#mnt9---perform-and-record-the-maintenance-intervention)/16. | An aviation account does not supply a universal threshold or quantified causal effect. |

The Systems Modeling Guide's current R6.6:6 and R6.6:10 passages contribute configuration and enabling-service questions. Systems Management R10.7:1, R10.7:9 and R10.11:1 contribute work-management and provision questions. The source line used is the Guides' 8 September 2026 current-editing edition; earlier DOCX formulations provide history, not the operative configuration or service distinctions. [SYSE.12](SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse12---develop-an-engineering-platform-for-practitioner-work)/13 and the relevant OPS results carry the more precise contributions used here.

For related explanations across the engineering languages, use the [Engineering DPF Suite Reference](ENGINEERING-DPF-SUITE-REFERENCE.md). Direct governing Methods remain with FPF and the named DPF patterns; a source catalogue is a finding aid rather than independent confirmation of their claims.

# Framework Boundary and Refresh

The framework's code remains MNT. Earlier references to Maintenance Engineering Principles Framework name this same product; the fuller name makes the engineering-and-management scope explicit. PatternIDs identify its continuing practical contributions; Parts and positions describe this edition's reading order. A changed title or publication position does not by itself create a new Method. A changed problem, action or result needs an explicit continuity decision and a return for affected users.

The first edition has no separate jurisdictional or equipment profile. Its constructed cases support learning the reasoning, not a claim of observed organizational adoption or universal effectiveness. For a live intervention, use the competent equipment sources and operative requirements of that setting.

Refresh the affected contribution when new failure behaviour changes a policy, a measurement or operating change invalidates interpretation, a support or authority change alters feasibility, an installed change defeats earlier verification, or comparable fleet evidence changes the programme. Reconsider a Method when a serious alternative changes its practical worth, and a cultural account when actual enactment or its conditions change.

A new source date alone need not reopen a completed maintenance answer. Conversely, an old but applicable source can remain useful with its stated limits. For a specialist legal use, recover the actual current law and procedure instead of relying on the dated illustrations in this edition.

The framework can help a reader give a smaller supported answer while a stronger question remains open. Continuing that stronger inquiry is a separate practical choice with its own attainable value, burden and authority.
