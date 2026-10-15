# Engineering Asset Management Principles Framework

**DocID:** `EAM` within **FPF Library**.

> A domain pattern language for making and revising value-oriented decisions about engineered assets over their lives, for one asset, an interacting asset System or a portfolio.

- **Author:** Anatoly Levenchuk, with AI-assisted development and review
- **Release:** 27 September 2026
- **Status:** Eternal alpha: the current Methods can be used for their stated asset questions and conditions; the framework continues to develop as practice, sources and evidence change.
- **License:** Original framework content © 2026 Anatoly Levenchuk, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Third-party sources retain their own terms.
- **Publication:** [FPF Library repository](https://github.com/ailev/FPF)

Start with the [Readme](#engineering-asset-management-principles-framework-readme) for a working difficulty or the [Table of Contents](#table-of-contents) for a familiar question or PatternID. Open the pattern that can supply the needed answer and stop when that answer is sufficient. Use the [Citation](#citation) to identify this release.


# Table of Contents

Search for the asset decision or result you need. Dependencies identify useful result relations, not a mandatory sequence.

## Public units

| Unit | Reader use |
| :--- | :--- |
| [Engineering Asset Management Principles Framework Readme](#engineering-asset-management-principles-framework-readme) | Follow connected asset decisions and their changed-condition returns. |
| [Citation](#citation) | Cite the framework or a particular pattern contribution. |
| [Engineering Asset Management Principles Framework Architectural Reference](#engineering-asset-management-principles-framework-architectural-reference) | Understand the asset-value problem, the related Methods and their limits. |
| [EAM.Reference:1](#eamreference1---the-working-problem-and-practical-gain) | The working problem and practical gain |
| [EAM.Reference:2](#eamreference2---forces-and-working-distinctions) | Forces and working distinctions |
| [EAM.Reference:3](#eamreference3---architectural-rationale) | Architectural Rationale |
| [EAM.Reference:4](#eamreference4---recognition-assurance-and-ordinary-stops) | Recognition, assurance and ordinary stops |
| [EAM.Reference:5](#eamreference5---predictable-mistakes-consequences-and-bias) | Predictable mistakes, consequences and bias |
| [EAM.Reference:6](#eamreference6---current-sources-and-what-they-support) | Current sources and what they support |
| [EAM.Reference:7](#eamreference7---qualified-returns-from-related-practice) | Qualified returns from related practice |
| [EAM.Sources:1](#eamsources1---professional-and-technical-sources) | Professional and technical sources |
| [EAM.Application - Cross-Pattern Applications](#cross-pattern-applications) | Follow one asset and its different choice in a constrained programme. |
| [Engineering Asset Management Principles Framework Sources and Edition Notes](#engineering-asset-management-principles-framework-sources-and-edition-notes) | Recover the source contributions and qualified specialist returns. |
| [EAM.Boundary - Framework Boundary and Refresh](#eamreference8---framework-boundary-and-revision) | Find the scope, ordinary stops and reasons to reopen a result. |

**Part A - Outcomes and the Asset Information Basis**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [EAM.1 - Frame the Engineered Assets and Required Outcomes](#eam1---frame-the-engineered-assets-and-required-outcomes) | Stable | *Keywords:* single asset, asset System, portfolio, service, horizon. *Query:* "Which options should we compare for this asset or portfolio, for what service and period?" Agree the asset options, required service, comparison period and decision maker. | [EAM.2](#eam2---relate-assets-to-strategy-services-and-required-capability), [EAM.3](#eam3---establish-the-asset-information-and-configuration-basis); FPF [FPF A.1.SCR](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a1scr---finding-the-acting-or-changed-system) |
| 2 | [EAM.2 - Relate Assets to Strategy, Services, and Required Capability](#eam2---relate-assets-to-strategy-services-and-required-capability) | Stable | *Keywords:* strategy, service, stakeholder, required capability. *Query:* "What required contribution must the assets support?" Relate proposed asset work to an actual service outcome and its authority. | [EAM.1](#eam1---frame-the-engineered-assets-and-required-outcomes), [EAM.4](#eam4---assess-demand-and-service-need-for-asset-decisions), [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence); [OPS.1](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops1---identify-the-operating-system-commitments-and-flow-units) |
| 3 | [EAM.3 - Establish the Asset Information and Configuration Basis](#eam3---establish-the-asset-information-and-configuration-basis) | Stable | *Keywords:* unit identity, configuration, effectivity, source applicability. *Query:* "Which information applies to this asset and comparison?" Resolve the answer-changing mismatch with a sufficient information basis. | [SYSE.13](../Engineering%20DPF%20Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse13---establish-configuration-identity-variants-and-effectivity); [EAM.1](#eam1---frame-the-engineered-assets-and-required-outcomes), [EAM.5](#eam5---assess-asset-condition-and-performance); FPF [FPF A.10](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a10---evidence-graph-referring-claim-bound-evidence-and-provenance-graph) |

**Part B - Demand, Condition, Capacity, and Interdependence**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 4 | [EAM.4 - Assess Demand and Service Need for Asset Decisions](#eam4---assess-demand-and-service-need-for-asset-decisions) | Stable | *Keywords:* demand, components, drivers, coincident peak, scenario, forecast, service requirement. *Query:* "What service will be needed under the conditions that matter?" Construct compatible demand scenarios and distinguish their evidence from the mandated service. | [EAM.2](#eam2---relate-assets-to-strategy-services-and-required-capability), [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence); [OPS.1](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops1---identify-the-operating-system-commitments-and-flow-units) |
| 5 | [EAM.5 - Assess Asset Condition and Performance](#eam5---assess-asset-condition-and-performance) | Stable | *Keywords:* condition, performance, diagnosis, exposure, forecast. *Query:* "What do observed condition and delivered performance support?" Return a qualified account for the asset decision. | [MNT.4](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt4---monitor-and-interpret-system-condition-for-maintenance), [MNT.6](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt6---diagnose-condition-and-choose-a-maintenance-response); [OPS.18](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops18---control-operating-quality-and-reliability); [EAM.3](#eam3---establish-the-asset-information-and-configuration-basis) |
| 6 | [EAM.6 - Assess Asset Capacity, Resilience, and Interdependence](#eam6---assess-asset-capacity-resilience-and-interdependence) | Stable | *Keywords:* capacity, bottleneck, resilience, shared dependency, usable reserve, recovery intervals. *Query:* "Can the assets support service during normal use and disturbance?" Derive lost contributions and follow available service and reserve through recovery. | [EAM.4](#eam4---assess-demand-and-service-need-for-asset-decisions), [EAM.5](#eam5---assess-asset-condition-and-performance); [OPS.10](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops10---qualify-operating-capacity-under-variability), [OPS.11](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops11---coordinate-interacting-operating-structures) |

**Part C - Alternatives, Conflicts, Combinations, and Timing**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 7 | [EAM.7 - Generate Ways to Supply an Asset-Dependent Service](#eam7---generate-ways-to-supply-an-asset-dependent-service) | Stable | *Keywords:* acquire, modify, lease, service option, functional alternative. *Query:* "Which acquisition or change can provide the needed contribution?" Generate comparable qualified alternatives with their whole burden. | [EAM.2](#eam2---relate-assets-to-strategy-services-and-required-capability), [EAM.3](#eam3---establish-the-asset-information-and-configuration-basis), [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence); [SYSE.5](../Engineering%20DPF%20Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse5---develop-an-engineered-systems-functional-organization-and-bearer-alternatives) |
| 8 | [EAM.8 - Generate Maintenance, Renewal, and Retirement Alternatives](#eam8---generate-maintenance-renewal-and-retirement-alternatives) | Stable | *Keywords:* continue, maintain, renew, replace, retire, later intervention, horizon, residual value. *Query:* "Which continued-use or change option is worth considering?" Construct supported policies with dated consequences and a compatible ending premise. | [EAM.5](#eam5---assess-asset-condition-and-performance), [EAM.9](#eam9---compare-asset-alternatives-and-reconcile-decisions-when-they-conflict); [MNT.6](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt6---diagnose-condition-and-choose-a-maintenance-response), [MNT.7](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt7---coordinate-maintenance-intervention-and-continuing-operation); [FIN.6](CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin6---value-capital-projects), [FIN.7](CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin7---value-assets-and-the-corporation); FPF [FPF C.11](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11---decision-theory-decsn-cal) |
| 9 | [EAM.9 - Compare Asset Alternatives and Reconcile Decisions When They Conflict](#eam9---compare-asset-alternatives-and-reconcile-decisions-when-they-conflict) | Stable | *Keywords:* asset alternatives, lifetime consequences, conflicting choices, funding, service mandate, simultaneous work. *Query:* "Which asset alternative is supported, and what unresolved conflict remains?" Compare eligible asset alternatives and identify any conflicting service, funding or work condition and the decision needed to resolve it. | [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence), [EAM.10](#eam10---compare-engineered-asset-portfolio-combinations), [EAM.11](#eam11---time-asset-interventions-and-manage-dependencies), [EAM.12](#eam12---integrate-specialist-results-for-an-asset-recommendation-or-decision); FPF [FPF C.32.MWA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c32mwa---synthesize-an-architecture-account-of-methods-and-their-use) |
| 10 | [EAM.10 - Compare Engineered-Asset Portfolio Combinations](#eam10---compare-engineered-asset-portfolio-combinations) | Stable | *Keywords:* capital allocation, indivisible options, portfolio, combination, shared work, joint consequences. *Query:* "Which eligible asset combination should receive the allocation?" Construct whole consequences and compare programmes under the dated binding conditions. | [EAM.7](#eam7---generate-ways-to-supply-an-asset-dependent-service), [EAM.8](#eam8---generate-maintenance-renewal-and-retirement-alternatives), [EAM.9](#eam9---compare-asset-alternatives-and-reconcile-decisions-when-they-conflict), [EAM.11](#eam11---time-asset-interventions-and-manage-dependencies); [FIN.9](CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin9---compare-capital-investments-and-allocations); FPF [FPF C.11](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11---decision-theory-decsn-cal) |
| 11 | [EAM.11 - Time Asset Interventions and Manage Dependencies](#eam11---time-asset-interventions-and-manage-dependencies) | Stable | *Keywords:* whole outage, dependencies, calendar, preparation, contingency. *Query:* "Can the selected programme be completed while preserving service?" Construct a supported calendar or expose the limiting prerequisite. | [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence), [EAM.9](#eam9---compare-asset-alternatives-and-reconcile-decisions-when-they-conflict), [EAM.10](#eam10---compare-engineered-asset-portfolio-combinations); [MNT.7](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt7---coordinate-maintenance-intervention-and-continuing-operation), [MNT.15](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt15---reconcile-simultaneous-maintenance-operation-and-support-work); [OPS.10](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops10---qualify-operating-capacity-under-variability) |

**Part D - Decisions, Outcomes, and Continuing Practice**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 12 | [EAM.12 - Integrate Specialist Results for an Asset Recommendation or Decision](#eam12---integrate-specialist-results-for-an-asset-recommendation-or-decision) | Stable | *Keywords:* recommendation, specialist result, decision, authorization. *Query:* "What supported answer is requested and who makes the asset decision?" Integrate applicable results and distinguish advice from actual authorization. | [EAM.1](#eam1---frame-the-engineered-assets-and-required-outcomes), [EAM.9](#eam9---compare-asset-alternatives-and-reconcile-decisions-when-they-conflict), [EAM.10](#eam10---compare-engineered-asset-portfolio-combinations), [EAM.11](#eam11---time-asset-interventions-and-manage-dependencies); FPF [FPF A.6.F](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a6f---function-and-functional-precision-restoration-rpr-function), [FPF A.10](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a10---evidence-graph-referring-claim-bound-evidence-and-provenance-graph) |
| 13 | [EAM.13 - Track Realized Outcomes and Reconsider Asset Plans](#eam13---track-realized-outcomes-and-reconsider-asset-plans) | Stable | *Keywords:* realized outcome, variance, attribution, revision, changed premise. *Query:* "What has actually changed, and should the asset plan be retained or revised?" Compare obtained outcomes with the decision premises at the same scope. | [EAM.3](#eam3---establish-the-asset-information-and-configuration-basis), [EAM.12](#eam12---integrate-specialist-results-for-an-asset-recommendation-or-decision); FPF [FPF A.10](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a10---evidence-graph-referring-claim-bound-evidence-and-provenance-graph), [FPF C.16](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c16---measurement--metrics-characterization-mmchr) |
| 14 | [EAM.14 - Decide Whether and How to Change the Asset-Management System](#eam14---decide-whether-and-how-to-change-the-asset-management-system) | Stable | *Keywords:* roles, information flow, responsibility, management system, arrangement. *Query:* "What in the organization of asset work prevents timely, supported decisions?" Compare feasible changes to responsibilities, information flow or support with keeping the current arrangement. | [EAM.13](#eam13---track-realized-outcomes-and-reconsider-asset-plans), [EAM.15](#eam15---decide-whether-and-how-to-change-engineering-asset-management-methods), [EAM.16](#eam16---deliberately-continue-and-change-engineering-asset-management-culture); [OPS.11](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops11---coordinate-interacting-operating-structures); [OCE.9](ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce9---realize-a-bounded-organization-capability-increment); FPF [FPF C.11.DUA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11dua---make-advice-and-evidence-demands-worth-their-burden) |
| 15 | [EAM.15 - Decide Whether and How to Change Engineering Asset-Management Methods](#eam15---decide-whether-and-how-to-change-engineering-asset-management-methods) | Stable | *Keywords:* Method, reusable operations, comparison, variant, trial, refresh. *Query:* "Should this way of making asset decisions be retained or changed?" Compare ways of answering the same asset question, including the effort of applying and maintaining them. | [EAM.10](#eam10---compare-engineered-asset-portfolio-combinations), [EAM.13](#eam13---track-realized-outcomes-and-reconsider-asset-plans); [FPF A.3.1.MV](../../FPF-Spec.md#a31mv---construct-and-maintain-a-method-variant); FPF [FPF C.11.DUA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11dua---make-advice-and-evidence-demands-worth-their-burden) |
| 16 | [EAM.16 - Deliberately Continue and Change Engineering Asset-Management Culture](#eam16---deliberately-continue-and-change-engineering-asset-management-culture) | Stable | *Keywords:* culture, transmission, use, recognition, selection, retention, branch. *Query:* "Which asset-management practices do people use, and should they continue or change?" Establish what the evidence supports and compare continuation, change, a qualified branch or stopping. | [EAM.14](#eam14---decide-whether-and-how-to-change-the-asset-management-system), [EAM.15](#eam15---decide-whether-and-how-to-change-engineering-asset-management-methods); [FPF C.36.MC](../../FPF-Spec.md#c36mc---qualify-and-develop-a-method-culture); FPF [FPF C.36](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c36---cultural-evolution-and-cultural-evolution-engineering) |

# Engineering Asset Management Principles Framework Readme

## Practical entries

The connections below follow an asset question through the methods whose results it needs. Start where the uncertainty lies: a supported option comparison can go straight to the decision, while a shared funding or outage constraint changes the question to a whole programme. Use the Table of Contents for a known PatternID or a question not illustrated here. When working with a colleague or assistant, describe the asset, the difficulty and the answer you need in ordinary work language.

The CityWater amounts and conditions are constructed teaching inputs. The two full [Cross-Pattern Applications](#cross-pattern-applications) retain the engineering qualifications, service requirements and calculations behind the shorter uses below.

### EAM-ASSET - Compare continued use and change for one asset

- **Situation:** CityWater can keep pump D functioning under a supported policy, but replacement may give better value.
- **Question:** Which policy should the infrastructure committee choose for the required service and horizon?
- **First useful result or blocker:** A supported recommendation, or the service, engineering or economic uncertainty preventing it.
- **Start with:** [EAM.8](#eam8---generate-maintenance-renewal-and-retirement-alternatives) for the policies; [EAM.1](#eam1---frame-the-engineered-assets-and-required-outcomes) if the comparison is unclear.
- **Stop or return:** Sufficient advice can finish the inquiry. A shared resource constraint sends the policies to the programme comparison.

The committee's value question differs from the maintenance question of which intervention supports continued functioning. If only a repair estimate is available, [EAM.8](#eam8---generate-maintenance-renewal-and-retirement-alternatives) first constructs the service policy: supported intervals, recurring duties, later work and ending. Its separate four-year example shows how an omitted year-three overhaul can reverse the comparison. A complete qualified policy can go directly to comparison.

[EAM.8](#eam8---generate-maintenance-renewal-and-retirement-alternatives) uses the applicable condition and maintenance results to describe two complete policies: continued use with its initial intervention and recurring support, and replacement with integration and terminal value. [EAM.9](#eam9---compare-asset-alternatives-and-reconcile-decisions-when-they-conflict) consumes those qualified alternatives and compares their consequences on the same basis.

In [APP-EAM-01](#eamapplication1---app-eam-01---one-asset-and-a-supported-value-comparison), at the example's 3% real rate, five-year present cost is about €5.080 million for continuation and €3.568 million for replacement. With the required service equal and resources available for either, the €1.512 million difference supports recommending replacement. The break-even annual cost of continued use is about €0.670 million: an applicable range of €0.95–1.05 million leaves the recommendation unchanged, whereas a credible €0.60 million could reverse it. Further costing is useful when its attainable answer can change the decision enough to warrant the inquiry.

[EAM.12](#eam12---integrate-specialist-results-for-an-asset-recommendation-or-decision) uses the comparison and its conditions to give the committee sufficient advice. The committee can then select a policy within its authority; maintenance and operating practitioners settle permissions for the work and return to service. If the request concerned only the maintenance response, the applicable MNT result could already finish it. If D competes with other assets for funding or an outage window, take its two policies into the combination below.

### EAM-COMBINATION - Choose asset work under shared constraints

- **Situation:** CityWater's individually preferred asset options exceed the shared capital allocation.
- **Question:** Which complete programme supplies the required service within the funding and work windows?
- **First useful result or blocker:** A programme recommendation with a supported calendar, or the conflict preventing it.
- **Start with:** [EAM.10](#eam10---compare-engineered-asset-portfolio-combinations) when alternatives and conditions are known; establish a missing service or option result where needed.
- **Stop or return:** Finish with sufficient programme advice. A changed funding, service or work condition reopens the affected comparison.

The demand and capability comparison in [EAM.4](#eam4---assess-demand-and-service-need-for-asset-decisions) and [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence) identifies North's wet-season shortfall: 1,100 m³/h required against 1,000 available. [EAM.7](#eam7---generate-ways-to-supply-an-asset-dependent-service) supplies two qualified ways to add 200 m³/h at C, modification or leased service. Together with the supported A, B and D policies, these become the alternatives for [EAM.9](#eam9---compare-asset-alternatives-and-reconcile-decisions-when-they-conflict) to reconcile and [EAM.10](#eam10---compare-engineered-asset-portfolio-combinations) to combine.

Under the €8 million capital limit and the other supplied limits, [APP-EAM-02](#eamapplication2---app-eam-02---the-same-asset-in-a-constrained-programme) finds the least-cost eligible programme: refurbish A and B, modify C, continue D. It uses €7 million capital, €0.50 million initial operating expenditure and €1.85 million annually; its present cost is €14.592 million. Replacing D as well would require €10 million capital. Leasing C instead makes D replacement affordable, but raises total present cost to €15.350 million. The individual D result therefore remains true under its own resource assumption, while the programme comparison favors continuation.

[EAM.11](#eam11---time-asset-interventions-and-manage-dependencies) consumes the selected interventions and their whole outage durations. A on days 1–2, B on 3–4, C on 5–7 and D on day 8 fits the twelve-day window and the single team, restoring each asset before the next outage. It avoids the A/C and B/D overlaps that would breach the dry-window service minimum. Use [EAM.12](#eam12---integrate-specialist-results-for-an-asset-recommendation-or-decision) to send a programme recommendation with a supported calendar to the committee.

If a demand driver or shared dependency changes, [EAM.4](#eam4---assess-demand-and-service-need-for-asset-decisions) and [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence) reconstruct the affected service conditions before the same options are compared again. If work can share a real preparation or mobilization, [EAM.10](#eam10---compare-engineered-asset-portfolio-combinations) reconciles the whole consequences with the separate policies and [EAM.11](#eam11---time-asset-interventions-and-manage-dependencies) qualifies that arrangement. Its separate P+Q case changes a 4.0 estimate to 3.8 by paying for one mobilization; incompatible access windows remove that saving. These constructions are used when their premise is missing or changes.

A changed limit returns to the affected choice. If the funding board raises capital to €10 million, retaining the other premises, replacing D joins the preferred programme. If only seven days remain, the eight-day arrangement fails: the declared alternatives instead permit A refurbishment, B replacement, C leased service and D continuation. If D's engineering qualification fails, remove continuation before comparing programmes; cost savings cannot restore it. Each changed case is worked through in the full application.

### EAM-CHANGE - Reconsider a decision after a changed condition

- **Situation:** Observed service, condition or expenditure differs from a relied-on plan premise.
- **Question:** Does the difference change the plan, its explanation or the next decision?
- **First useful result or blocker:** A retained or revised plan, or the applicable observation needed to decide.
- **Start with:** [EAM.13](#eam13---track-realized-outcomes-and-reconsider-asset-plans) for the outcome comparison; use [EAM.3](#eam3---establish-the-asset-information-and-configuration-basis) first if asset or configuration correspondence is unsettled.
- **Stop or return:** Retain a sufficient plan; reopen the choice changed by the observation. Further inquiry needs an attainable answer worth its burden.

Suppose annual expenditure for the selected CityWater policy is €1.95 million against €1.85 million planned. [EAM.13](#eam13---track-realized-outcomes-and-reconsider-asset-plans) compares the same scope and interval. Applicable bills explain a €0.12 million tariff effect and a €0.02 million reduction elsewhere: 1.85 + 0.12 − 0.02 = 1.95.

That result updates the price premise for [EAM.9](#eam9---compare-asset-alternatives-and-reconcile-decisions-when-they-conflict) or [EAM.10](#eam10---compare-engineered-asset-portfolio-combinations) where it can change the next choice. It does not establish an equipment defect. If the comparison instead joins different units or configurations, [EAM.3](#eam3---establish-the-asset-information-and-configuration-basis) first resolves that mismatch. If C's work is complete but usable service falls below the wet-season requirement, return the service deficiency to [EAM.5](#eam5---assess-asset-condition-and-performance) and [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence) and the applicable operating or engineering response. The cause can remain under investigation while a supported response is taken.

### EAM-PRACTICE - Improve how asset decisions are made

- **Situation:** Appraisals repeatedly fail or consume avoidable effort despite usable individual asset plans.
- **Question:** What should change in the way the decisions are produced?
- **First useful result or blocker:** Supported advice about the arrangement, method or continued practice, or a result needed to decide.
- **Start with:** [EAM.14](#eam14---decide-whether-and-how-to-change-the-asset-management-system) for the working arrangement, [EAM.15](#eam15---decide-whether-and-how-to-change-engineering-asset-management-methods) for the selection method, or [EAM.16](#eam16---deliberately-continue-and-change-engineering-asset-management-culture) for use and continuation among practitioners.
- **Stop or return:** Answer the identified recurring difficulty; change another part of the practice when its contribution matters to that answer.

In [EAM.14](#eam14---decide-whether-and-how-to-change-the-asset-management-system)'s appraisal office, mismatched station identifiers cause six hours of rework a week. A maintained correspondence and responsibility for returning mismatches would take twelve hours to establish and half an hour a week to maintain. Over ten comparable weeks, that is seventeen hours against sixty hours of continued rework, if the repair removes the mismatch. The comparison supports proposing the bounded repair; examine later appraisals to see whether it helps. Use [EAM.3](#eam3---establish-the-asset-information-and-configuration-basis) to establish the applicable unit correspondence. If assigned work exceeds available time under adequate existing responsibilities, [EAM.14](#eam14---decide-whether-and-how-to-change-the-asset-management-system) uses OPS to compare operating adjustments. If organizational responsibilities or decision rights must change, or agreed responsibilities must become workable, it uses [OCE.9](ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce9---realize-a-bounded-organization-capability-increment) to exercise an appraisal from request to usable result and an unmatched-unit return.

If the information is adequate but the selection rule fails, [EAM.15](#eam15---decide-whether-and-how-to-change-engineering-asset-management-methods) addresses the method instead. Funding D, C and A in condition-priority order exhausts CityWater's capital before B, whereas combination comparison supplies the required programme. That calculation supports changing the comparison for this case. A proposed reusable method can be tried on other relevant cases when the consequences for adoption justify the effort.

[EAM.16](#eam16---deliberately-continue-and-change-engineering-asset-management-culture) takes that proposed instruction into a question about its transmission, use or continuation among practitioners. Distribution and teaching establish different facts from later appraisals using the method. Its existing branch example retains programme comparison for central planners with shared constraints and single-asset comparison for depot cases whose independence is established. A shared constraint returns a depot case to the programme comparison.

## How to read and apply the framework

Begin with a pattern's Problem frame and Solution. Its worked case shows a minimally useful result and a consequential branch. Read its assurance questions, alternatives and source comparison to judge a more consequential use.

This edition proposes source-grounded Methods and constructed applications. It does not report field effectiveness of the integrated repertoire. An equipment-specific assessment, financial input, operating condition or actual authorization must come from the practice or authority responsible for it.

## Citation

Cite: Anatoly Levenchuk, *Engineering Asset Management Principles Framework*, version shown above. For a particular contribution, add its PatternID and title. The framework was developed with AI-assisted authoring and review. Original text is reusable under the license above; cited third-party works are not relicensed.

# Engineering Asset Management Principles Framework Architectural Reference

## EAM.Reference:1 - The working problem and practical gain

Engineering asset management concerns the value obtained through engineered assets over time. A practitioner may need to compare the continued use of one pump, choose an interacting set of renewals, reconsider a service contribution, or improve the practice that makes those decisions. Asset count does not determine which of these questions is present.

An equipment register can identify property without explaining what service needs it. An alarm can justify investigation without deciding replacement. A project with attractive savings can consume the funding that a necessary programme needs elsewhere. A completed intervention can leave its promised service unestablished. Each difficulty calls for a result that a particular recipient can use.

This language helps the practitioner establish the required contribution, compare supported alternatives, reconcile their interactions and return the asset answer that was requested. The answer can be sufficient advice, a decision to retain an option, an authorized programme or an exact unmet condition. A whole-enterprise study is not the default price of answering one asset question.

An *asset* is considered here for the value its use can contribute. The governed objects are engineered assets, an interacting asset System and a portfolio of assets or interventions. A portfolio groups assets for management; evidence of functional interaction is still needed before treating it as one System. The framework governs decisions about their contribution, use and change, and the continuation of that decision practice. It leaves equipment diagnosis, design realization, protected maintenance work and service operation with their relevant Methods.

The Russian plain designation is *управление техническими активами*. The English name makes the engineered-asset scope visible. Enterprise Asset Management is a serious overlapping professional usage that includes maintenance, information and cross-functional practice. It is neither confined to software nor to large enterprises. Here the Engineering qualification states this language's subject; portfolio management names only one of its questions.

## EAM.Reference:2 - Forces and working distinctions

A decision needs enough scope to include an answer-changing dependency and enough restraint to remain usable. A longer horizon can expose renewal and residual value while increasing uncertainty. Equal financial units help comparison but cannot turn a service obligation or unsupported engineering claim into an acceptable option. Local efficiency can move cost, work or loss of service to someone else.

The practitioner therefore keeps several distinctions visible in ordinary working language. Required service differs from observed demand and usable capacity. An installed unit differs from its description. A condition observation differs from diagnosis and a qualified forecast. An option differs from a selected programme; a forecast benefit differs from an obtained outcome.

A recommendation also differs from authorization. An analyst can answer a committee's request by giving the supported option, reasons and conditions. The committee separately makes the decision within its authority. A funding board may control allocations, a service authority may control delivery commitments, and maintenance or operating authorities may control work and resumption. Supplying a cost estimate does not grant any of those powers.

Use the detail that can change the answer. Existing evidence can be sufficient. Where a missing result matters, ask what an attainable inquiry could resolve and include obtaining, interpreting and maintaining its evidence, delay, disruption and displaced work in its burden. [FPF C.11.DUA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11dua---make-advice-and-evidence-demands-worth-their-burden) supplies the general guidance for that choice.

## EAM.Reference:3 - Architectural Rationale

The sixteen contributions are related by the results they supply, rather than by one lifecycle diagram. Four publication parts help navigation; they are not stages.

[EAM.1](#eam1---frame-the-engineered-assets-and-required-outcomes)–[EAM.3](#eam3---establish-the-asset-information-and-configuration-basis) establish what asset contribution is being decided and which information applies. [EAM.4](#eam4---assess-demand-and-service-need-for-asset-decisions)–[EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence) assess service need, actual condition and performance, and capability under the relevant dependencies. When the demand basis is missing, [EAM.4](#eam4---assess-demand-and-service-need-for-asset-decisions) constructs a scenario from compatible observations and explicit driver changes; [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence) receives its quantity, location, period and conditions. For an interacting asset system, [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence) derives lost contributions from shared dependencies and follows service and reserve through recovery intervals. A clear existing result can enter directly into a later comparison; every use need not reconstruct those accounts.

[EAM.7](#eam7---generate-ways-to-supply-an-asset-dependent-service) and [EAM.8](#eam8---generate-maintenance-renewal-and-retirement-alternatives) generate materially different ways of obtaining or continuing the contribution. Acquisition, modification, maintenance, renewal, lease, changed use and withdrawal can compete at that scope. [EAM.8](#eam8---generate-maintenance-renewal-and-retirement-alternatives) connects the technically supported intervals of a continuing policy to its dated work, economic consequences and ending. [FIN.6](CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin6---value-capital-projects) and [FIN.7](CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin7---value-assets-and-the-corporation) supply financial construction and valuation where needed; their return must retain the same service policy, perspective, dates and assumptions. [EAM.9](#eam9---compare-asset-alternatives-and-reconcile-decisions-when-they-conflict) resolves conflicts among proposed decisions; [EAM.10](#eam10---compare-engineered-asset-portfolio-combinations) compares the full combination where allocations and interactions matter. It distinguishes technical prerequisites, shared resource limits and joint consequences, reconstructing costs or benefits from the actual combined work. [FIN.9](CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin9---compare-capital-investments-and-allocations) supplies the financial interaction and dated funding comparison when needed. [EAM.11](#eam11---time-asset-interventions-and-manage-dependencies) establishes a complete feasible timing proposal using the requisite operating and maintenance results. A project ranking, capacity bound or sum of job durations cannot substitute for all three questions.

[EAM.12](#eam12---integrate-specialist-results-for-an-asset-recommendation-or-decision) integrates the qualified inputs and distinguishes the advice requested from the asset decision actually made. [EAM.13](#eam13---track-realized-outcomes-and-reconsider-asset-plans) tests the retained plan against obtained outcomes and changed premises. The return may go to demand, configuration, engineering support, an option or its authority. There is no requirement to restart every earlier pattern.

[EAM.14](#eam14---decide-whether-and-how-to-change-the-asset-management-system)–[EAM.16](#eam16---deliberately-continue-and-change-engineering-asset-management-culture) address three different continuing subjects. The management system arranges responsibilities, information flows and provision. A Method supplies reusable operations for obtaining an asset-management result. Culture concerns the continuation and change of practice among people: transmission, actual use, recognition, selection and retention have distinct evidence. A new application, a revised comparison rule and a teaching initiative can affect one another without becoming the same change.

The asset's functional dependencies, the portfolio allocation, the team calendar, configuration evidence and actual authority are different structures related through identifiable assets, services and decisions. A single decomposition loses some of those relations. [FPF A.22](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a22---structure-and-structural-views-struct-cal) gives guidance for selecting the constituents, actual relations and constraints needed for a particular structural question. [FPF C.32.MWA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c32mwa---synthesize-an-architecture-account-of-methods-and-their-use) helps combine contributions from the different structures needed for the practice.

Maintenance can fully answer a maintained-functioning question for one asset or a fleet. EAM adds the question of value among asset options, including for one asset. Operations Management supplies a qualified account of service, demand, operating capability or coordination where needed. Systems Engineering supplies an applicable functional alternative or configuration account. EAM uses those results for the asset choice rather than reproducing their full disciplines.

This division avoids three losses. A portfolio-only language would exclude the D comparison. A maintenance-only language would leave its common-horizon value question unanswered. A universal financial score would conceal ineligible service, engineering or authority conditions. A complete enterprise application is one possible support, not the definition of the practice.

**Constituent actions in ongoing work.** While assessing an asset's service capability, interpreting a condition reading can constitute part of that assessment, and the assessment can constitute part of an ongoing renewal comparison. A changed service requirement can make a formerly acceptable reading inadequate for the comparison. The team needs the measurement interpretation and service reasoning that connect the reading to the decision. [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence) develops the capability question, and [EAM.10](#eam10---compare-engineered-asset-portfolio-combinations) retains the shared operating, financial and specialist constraints on the combination. If these connections are unclear, use [FPF B.1.5.EW](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#b15ew---recover-how-constituent-actions-enact-encompassing-work) to recover how the reading interpretation participates in the ongoing assessment and renewal comparison, and which constituent operations the team must perform or obtain. Carry the conditions of the larger work through those connections: merely supplying a result for later use does not make an action part of that ongoing work. A good local condition result leaves the whole renewal choice open.

## EAM.Reference:4 - Recognition, assurance and ordinary stops

Recognition begins with the working cue: an estimate for the wrong unit, an alarm presented as a diagnosis, a forecast treated as a mandate, two feasible jobs that fail together, or a promised benefit treated as achieved. The relevant pattern identifies a useful first move.

Assurance follows the requested claim. Technical eligibility needs applicable engineering support. Cost comparison needs consistent perspective, cash timing, horizon and sensitivity. Programme feasibility needs the actual allocation, service and whole-work conditions. An authorization claim needs the responsible decision. Actual effectiveness, causation and cultural retention each need evidence of their own subjects.

The checklists ask whether those contributions can be recovered; they do not supply missing domain evidence. Complete information, a causal model, an optimizer or a new trial is unnecessary when the available supported result already answers the request. A smaller truthful answer remains useful when a stronger claim is unsupported.

The two common applications demonstrate conditional economic and allocation reasoning. They do not establish real pump reliability, hydraulic behaviour, investment performance or equipment-work permission. A practitioner must obtain the actual inputs and authority required by the intended use.

## EAM.Reference:5 - Predictable mistakes, consequences and bias

Starting from “replace this asset” can remove a viable maintenance or service alternative before comparison. Ranking condition scores can spend money on a less useful programme. Comparing purchase prices over unequal horizons can hide operating burden and remaining service value. Adding a generic risk allowance to costs that already include the same response can count them twice.

The positive corrections are small and specific: restate the required contribution, compare qualified whole options, retain separate conditions, and reconcile the complete programme. The CityWater cases show that an individually sound replacement recommendation can coexist with a different programme recommendation.

The process can still privilege those who fund or request a project. Identify whose service, work, access and future costs change. Do not silently turn an unpriced consequence into zero or a missing observation into evidence of no effect. A technology supplier's claim and an available template establish neither applicable performance nor actual use.

Using the language adds some comparison and coordination burden. Its benefit is a decision whose scope, conditions and consequences the recipient can understand. Retaining a supported option or correcting a small information mismatch can be the useful outcome. The appropriate depth depends on the decision, possible consequences and attainable evidence.

## EAM.Reference:6 - Current sources and what they support

The GFMAM Asset Management Landscape, third edition (2024), and IAM's *Asset Management — an Anatomy*, version 4 (2024), locate this work within broad professional asset-management practice. This framework turns selected concerns into explicit practitioner operations and examples; those publications do not establish the effectiveness of these particular Methods.

Public ISO/TC 251 material locates the management-system relationship. NIST Handbook 135, 2025 edition, supplies dated cost and ending treatment, common horizons and choice under funding constraints. Its federal application conditions are not imported into CityWater. The water-planning guidance supplies the component and critical-period construction adapted in [EAM.4](#eam4---assess-demand-and-service-need-for-asset-decisions); IAM's recovery treatment informs EAM.6. Corporate Finance supplies the developed cash, ending-valuation and joint-consequence operations used in [EAM.8](#eam8---generate-maintenance-renewal-and-retirement-alternatives) and EAM.10. Their qualified returns are identified below.

General evidence, comparison, information and cultural distinctions remain with FPF. The references identify the specific contributions and receiving uses. Those source relations support reasoned use and refresh; a cited Method description still needs to yield a qualified result for an actual asset case.

## EAM.Reference:7 - Qualified returns from related practice

A description tells the reader how a result may be obtained. Before relying on an actual return, match its subject, configuration, use, horizon or observation window, assumptions and limits to the receiving decision. An existing adequate return can be used directly. A changed subject or condition reopens the affected use.

| Supplying contribution | Result that can be used | Receiving asset question and return condition |
| --- | --- | --- |
| [Maintenance Engineering and Management (MNT)](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md), [MNT.4](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt4---monitor-and-interpret-system-condition-for-maintenance) and [MNT.6](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt6---diagnose-condition-and-choose-a-maintenance-response) | A qualified condition account and supported maintenance response. | [EAM.5](#eam5---assess-asset-condition-and-performance) and [EAM.8](#eam8---generate-maintenance-renewal-and-retirement-alternatives) use the particular diagnosis, duty and policy. A new mechanism, changed duty or unsupported horizon returns to the supplying question. |
| [MNT.7](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt7---coordinate-maintenance-intervention-and-continuing-operation) and [MNT.15](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt15---reconcile-simultaneous-maintenance-operation-and-support-work) | Whole intervention/return demand and applicable shared-provider coordination. | [EAM.9](#eam9---compare-asset-alternatives-and-reconcile-decisions-when-they-conflict) and [EAM.11](#eam11---time-asset-interventions-and-manage-dependencies) use complete work and service implications. A changed protection, readiness, resource or return condition reopens feasibility. |
| [Operations Management (OPS)](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md), [OPS.1](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops1---identify-the-operating-system-commitments-and-flow-units), [OPS.10](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops10---qualify-operating-capacity-under-variability) and [OPS.11](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops11---coordinate-interacting-operating-structures) | A bounded service account, capability comparison and operating coordination result; OPS.11.1 supplies the operating model when needed. | [EAM.2](#eam2---relate-assets-to-strategy-services-and-required-capability), [EAM.4](#eam4---assess-demand-and-service-need-for-asset-decisions), [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence) and [EAM.11](#eam11---time-asset-interventions-and-manage-dependencies) match population, service unit, configuration and time. [EAM.14](#eam14---decide-whether-and-how-to-change-the-asset-management-system) uses operating adjustments within existing responsibilities and authority. A capacity bound alone does not establish a schedule or reliability probability. |
| [OPS.18](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops18---control-operating-quality-and-reliability) | The applicable service, quality or reliability evidence component of an operating decision. | [EAM.5](#eam5---assess-asset-condition-and-performance) uses that evidence at its stated population and window. The operating decision is not a general certificate of asset condition. |
| [Systems Engineering (SYSE)](../Engineering%20DPF%20Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md), [SYSE.5](../Engineering%20DPF%20Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse5---develop-an-engineered-systems-functional-organization-and-bearer-alternatives) and [SYSE.13](../Engineering%20DPF%20Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse13---establish-configuration-identity-variants-and-effectivity) | A qualified functional/bearer alternative or configuration identity and effectivity basis. | [EAM.7](#eam7---generate-ways-to-supply-an-asset-dependent-service) and [EAM.3](#eam3---establish-the-asset-information-and-configuration-basis) use the particular option and unit correspondence. Intended allocation differs from realized capability; a changed interface or configuration reopens applicability. |
| [Organization Change Engineering (OCE)](ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md), [OCE.9](ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce9---realize-a-bounded-organization-capability-increment) | A tested, condition-qualified organizational ability to obtain a contribution, or the missing condition and next repair. | [EAM.14](#eam14---decide-whether-and-how-to-change-the-asset-management-system) uses the return when organizational responsibilities or decision rights must change, or agreed responsibilities must become workable. Match the intended result, participants, work, observation window, retained support and limits. Information correction stays with [EAM.3](#eam3---establish-the-asset-information-and-configuration-basis) and operating coordination within existing responsibilities with OPS. |
| [FPF A.3.1.MV](../../FPF-Spec.md#a31mv---construct-and-maintain-a-method-variant) and [FPF C.36.MC](../../FPF-Spec.md#c36mc---qualify-and-develop-a-method-culture) | Reusable-variant/provenance guidance and applicable distinctions for Method-related cultural work. | [EAM.15](#eam15---decide-whether-and-how-to-change-engineering-asset-management-methods) and [EAM.16](#eam16---deliberately-continue-and-change-engineering-asset-management-culture) use the needed contribution. Preserve the difference between a proposed appraisal rule, its desk calculation and evidence of identified practitioners actually using its operations on stated occasions. Continued use needs evidence from the later occasions claimed. |
| [Corporate Finance (FIN)](CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md), [FIN.6](CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin6---value-capital-projects), [FIN.7](CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin7---value-assets-and-the-corporation) and [FIN.9](CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin9---compare-capital-investments-and-allocations) | A dated incremental financial account, valuation under the stated ending premise, and joint cash/funding comparison. | [EAM.8](#eam8---generate-maintenance-renewal-and-retirement-alternatives) matches asset/configuration, service policy, perspective, dates, price/rate and relevant tax/financing assumptions. [EAM.10](#eam10---compare-engineered-asset-portfolio-combinations) uses the whole combination and common baseline. A changed later intervention, horizon, ending, joint-work effect or funding date returns to the affected account. The financial result does not qualify engineering service. |
| Responsible local service, engineering, finance and decision authorities | The required contribution, eligible policies, cost basis, funding allocation and actual scope of decision. | [EAM.2](#eam2---relate-assets-to-strategy-services-and-required-capability), [EAM.9](#eam9---compare-asset-alternatives-and-reconcile-decisions-when-they-conflict), [EAM.10](#eam10---compare-engineered-asset-portfolio-combinations) and [EAM.12](#eam12---integrate-specialist-results-for-an-asset-recommendation-or-decision) use those actual answers. A missing general textbook does not block a sufficient direct answer; a missing action-changing result remains explicit. |

FPF [FPF A.1.SCR](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a1scr---finding-the-acting-or-changed-system) supports clear use of the actual subject and its descriptions. [FPF A.6.F](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a6f---function-and-functional-precision-restoration-rpr-function) and [FPF A.10](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a10---evidence-graph-referring-claim-bound-evidence-and-provenance-graph) support interpretation and evidence responsibility; [FPF C.11](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11---decision-theory-decsn-cal)/[FPF C.11.DUA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11dua---make-advice-and-evidence-demands-worth-their-burden) support comparison and useful inquiry; [FPF C.16](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c16---measurement--metrics-characterization-mmchr) supports qualified measurement; [FPF A.22](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a22---structure-and-structural-views-struct-cal) supports selecting the relevant constituents, relations and constraints for a structural question; [FPF C.32.MWA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c32mwa---synthesize-an-architecture-account-of-methods-and-their-use) supports simultaneous-work reasoning; B.1.5.EW helps recover how constituent actions enact encompassing work and which conditions must hold across that connection; [FPF C.36](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c36---cultural-evolution-and-cultural-evolution-engineering) supports cultural continuation and change. Their general Methods remain at their own sources.

## EAM.Reference:8 - Framework boundary and revision

The framework covers value-oriented decisions about engineered assets and the practice that makes them. It can be used for one asset, an interacting System or a portfolio. It does not make every asset problem a portfolio appraisal or every maintenance programme an EAM task.

Use a sufficient direct answer from another discipline when it already resolves the question. Equipment diagnosis, design realization, financial valuation, operating control, organizational change and protected work retain their own competence, evidence and authority requirements. EAM integrates their relevant returns for the asset decision.

The sixteen PatternIDs identify continuing problem contributions. Their numbers provide addresses, not maturity levels or mandatory stages. A reader can return directly to the pattern whose premise or result has changed.

Revisit an asset result when its service requirement, demand, configuration, engineering qualification, option, cost basis, allocation, calendar or authority changes enough to affect the answer. Revisit a practice result when the actual provision, reusable operations, relevant people or evidence of use changes. Preserve a still-applicable result; investigate the changed question.

A new source edition or an attractive technology can suggest a question without proving a better Method. Compare what changes for the same use, what the evidence supports and the whole burden of obtaining and maintaining the result. Report a proposed trial as a trial, an obtained result as obtained, and a cultural observation at the population and occasion it actually covers.

For source qualifications, citation and edition information, see the [Sources and Edition Notes](#engineering-asset-management-principles-framework-sources-and-edition-notes).

## EAM.Reference:End


# Part A - Outcomes and the Asset Information Basis

## EAM.1 - Frame the Engineered Assets and Required Outcomes

> **Type:** Method
> **Status:** Stable

### EAM.1:1 - Problem frame

Use this pattern when an asset decision lacks a clear service or value question. A pump has become expensive to maintain, an asset register has been completed, or a replacement budget is available, but the practitioner still needs to establish what the choice should achieve.

Begin with the requested answer: for which asset and receiving use should the practitioner compare continued use or change, over what horizon? Agree with the decision maker which options to compare for the named asset, which service they must provide, and over what period. An existing adequate framing can be retained.

A single asset can need this work. When the question is only how to maintain an already selected function, use the applicable maintenance guidance directly.

### EAM.1:2 - Problem

Ownership, a register boundary and a functional boundary often differ. One pump can serve several areas; a group of assets can share a budget without operating as one System. Beginning from the accounting list can therefore omit a service dependency or include equipment irrelevant to the decision.

An equally costly mistake begins with a favored action. Calling the question “replace the pump” hides whether the needed outcome could be obtained by maintenance, a different operating arrangement, shared service or withdrawal of an obsolete contribution.

### EAM.1:3 - Forces

A narrow boundary makes comparison manageable, while a missing dependency can reverse the answer. Current users, future users and the people funding the asset can value different outcomes. A short horizon can conceal renewal costs; a remote horizon can invite unsupported forecasts. Select the boundary and precision needed for the actual decision.

### EAM.1:4 - Solution

Name the recipient and the requested result. Distinguish advice about options, a choice among them and authorization to act. For advice, identify what the recipient needs to decide; the practitioner can finish by giving a sufficient supported recommendation.

Identify the engineered asset, interacting asset System or portfolio. State the service it contributes to, the receiving population and the conditions that matter. Use actual unit and configuration identifiers where differences can change the answer. A portfolio is a management grouping; establish functional interaction separately when the comparison relies on it.

Recover the required outcomes and their sources. A water-delivery commitment, desired reduction in energy use and available capital are different conditions. Name who can change each consequential commitment or allocation. Do not treat a proposed improvement as an existing obligation.

Choose the horizon and perspective of comparison. State whose costs, service, risk and continuing burden matter. Include an outside dependency when changing it could alter eligibility or preference: power supply, a shared standby unit, access, disposal or a receiving service can matter even outside ownership.

Write a short framing that identifies the assets, use, desired result, horizon and material constraints. It can be ordinary prose. Keep unresolved facts only when they change the next question. Use [EAM.2](#eam2---relate-assets-to-strategy-services-and-required-capability) for an unclear service contribution and [EAM.3](#eam3---establish-the-asset-information-and-configuration-basis) for an unclear information basis.

Stop when the framing allows the recipient to ask or answer the intended asset question. A request to compare two supported options does not require reconstructing the whole enterprise strategy or completing its asset register. Reopen when the service, asset boundary, horizon or actual decision scope changes.

### EAM.1:5 - Archetypal Grounding

Consider CityWater's pump D. The maintenance practitioner can recommend an initial intervention costing €0.50 million to support continued functioning under the supplied duty and five-year maintenance policy. The infrastructure committee asks a different question: should D continue under that policy or be replaced, given the same service and comparison horizon?

A useful framing is: compare D's supported five-year continued-use policy with replacement for its contribution to East's water delivery, using the stated cost perspective, technical qualification and actual funding and outage conditions. This is enough to compare continued use and replacement of D in [EAM.8](#eam8---generate-maintenance-renewal-and-retirement-alternatives) and EAM.9. Assess other assets where their service, funding or outage conditions affect that choice.

If D competes with A, B and C for the same funding, extend the comparison to that combination under EAM.10. The other eight stations matter through their continuing service contribution; their inclusion in the utility's register does not require eight additional investment analyses. The common CityWater applications provide the complete constructed premises.

### EAM.1:6 - Bias-Annotation

The person requesting the investment can dominate the framing. Ask which service users bear a loss, whose continuing work increases and which costs fall outside the requesting department. Include those parties through the consequences that matter, rather than adding a universal stakeholder inventory.

### EAM.1:7 - Conformance Checklist

Can the reader identify the asset and use, recipient, requested result and horizon? Are service commitments, aspirations and funding conditions distinguishable? Does every included dependency change the question, and does any omitted dependency plausibly reverse it?

### EAM.1:8 - Common Anti-Patterns and How to Avoid Them

A replacement request presented as the problem forecloses alternatives. Restate the required contribution before comparing interventions.

Using asset count to separate maintenance from asset management misroutes both a fleet maintenance question and a single-asset value question. Select by the decision being made.

### EAM.1:9 - Consequences

The next analysis can use a shared question and stop at a useful answer. Some apparent investment problems become maintenance, operating or service decisions. The boundary can remain provisional where a missing dependency matters; the practitioner reports that limit instead of giving an unqualified recommendation.

### EAM.1:10 - Architectural Rationale

Framing comes from the use of assets because that use determines relevant value, performance and alternatives. A register-first or budget-first approach remains useful for information and constraints but cannot select the decision's purpose. Keeping the first result small supports direct use without forcing a portfolio programme.

### EAM.1:11 - SoTA-Echoing

For deciding what to compare for an engineered asset, select a service-and-value question with a stated recipient, horizon and material dependencies. Adopt the proportional decision reasoning in IAM's *An Anatomy of Asset Management*, version 4, July 2024, decision-making and life-cycle investment discussion ([pp. 72–75](https://theiam.org/media/5615/iam-anatomy-version-4-final.pdf#page=72)). Adapt it in the Solution by identifying the requested answer before expanding the asset or information boundary. The resulting question can concern D alone while retaining a shared funding or service condition that would change its answer.

A serious alternative is to begin by preparing or refreshing the broader asset-management plan. GFMAM's *Asset Management Landscape*, third edition, June 2024, section 3.4 ([pp. 35–36](https://gfmam.org/sites/default/files/2024-06/GFMAM_AM_Landscape_v3.0_English_2024.pdf#page=35)), supplies that planning comparator. Such a plan is useful when the organization needs to settle its connected activities, rather than one already bounded option choice. For D's question, requiring that wider planning work first would also involve assets whose treatment cannot change the comparison. The selected framing retains the consequential dependencies with less preparatory work; it deliberately gives no conclusion about the whole register or enterprise plan. Neither source prescribes CityWater's boundary or supplies its service facts. Reopen the framing choice when an omitted dependency changes an option's eligibility or value, the decision maker asks for a wider plan, or a changed service or horizon makes the narrow question insufficient.

### EAM.1:12 - Relations

[EAM.2](#eam2---relate-assets-to-strategy-services-and-required-capability) relates outcomes to service and capability; [EAM.3](#eam3---establish-the-asset-information-and-configuration-basis) establishes the information needed for the chosen boundary. [MNT.1](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt1---identify-the-maintained-system-use-and-permission-boundary) supplies maintained-use facts, while [OPS.1](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops1---identify-the-operating-system-commitments-and-flow-units) supplies an operating service and commitment account. [EAM.8](#eam8---generate-maintenance-renewal-and-retirement-alternatives)–[EAM.12](#eam12---integrate-specialist-results-for-an-asset-recommendation-or-decision) use the resulting asset question. FPF [FPF A.1.SCR](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a1scr---finding-the-acting-or-changed-system) supports boundary recovery and [FPF C.11.DUA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11dua---make-advice-and-evidence-demands-worth-their-burden) supports a sufficient answer at proportionate effort.

### EAM.1:End

## EAM.2 - Relate Assets to Strategy, Services, and Required Capability

> **Type:** Method
> **Status:** Stable

### EAM.2:1 - Problem frame

Use this pattern when a desired outcome has been translated directly into an asset purchase or renewal, or when an existing asset's continuing contribution is unclear. A requirement for reliable water delivery has become “buy another pump,” but the practitioner needs to establish which capability is actually missing.

Begin with the receiving service and show how the asset could contribute to it. Return the supported outcome–service–capability relationship and any gap that changes the option choice. A supplied local service mandate can be enough; a complete strategy document is not a prerequisite.

### EAM.2:2 - Problem

An asset can be technically effective without serving the current purpose. Conversely, an important service can depend on several assets whose individual records do not explain their joint contribution. Broad strategic language leaves those relations unresolved and can make a familiar construction appear necessary.

### EAM.2:3 - Forces

Long-term outcomes guide investment while immediate commitments constrain what can change now. An asset can support several services with competing priorities. A detailed model can expose a missing dependency, but excessive tracing can delay a decision already supported by a simple relationship.

### EAM.2:4 - Solution

State the desired outcome and its recipient. Distinguish an aspiration from an adopted objective or service obligation. Identify the required service, population, location, conditions and horizon at the grain that changes the asset decision.

Describe the contribution needed to supply that service. Use quantities and conditions where they matter: flow at the delivery point, usable storage, response time or an available operating interval. A count of installed assets is not itself that contribution.

Relate the contribution to possible assets or arrangements. One contribution can require several interacting Systems, and one asset can support several contributions. Preserve the actual dependencies instead of forcing the relationships into a one-to-one hierarchy. Use [SYSE.5](../Engineering%20DPF%20Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse5---develop-an-engineered-systems-functional-organization-and-bearer-alternatives) when the bearer or allocation alternatives need engineering development.

Compare the needed capability with an applicable account of the present arrangement. Identify the consequential gap and its evidence. A supplied qualified result can be used directly; otherwise obtain the specific service or engineering result required. Separate a known shortfall from an uncertain forecast.

Challenge the necessity of the first asset proposal. Consider a different bearer, shared service, operating change or demand change when it could satisfy the same need. Keep a materially different alternative only with the conditions that would make its contribution real.

Return the supported relations and the next asset question. Stop when they are sufficient to generate or compare options. Reopen when the service, outcome priority or a relied-on capability changes.

### EAM.2:5 - Archetypal Grounding

CityWater's North area requires at least 1,100 m³/h in the wet season, while the supplied account supports 1,000. The gap is 100 m³/h of delivered service. The two shortlisted C options each add 200: a modification or a leased service. Both therefore meet the quantity requirement, subject to their technical and operating qualifications.

The useful relationship is from the water-delivery requirement to additional usable service capability, then to those alternative arrangements. It is not from a general growth objective directly to ownership of a new pump. The extra 100 above the minimum can matter as margin, but it is not proof that every contingency is covered.

If an authorized demand-management arrangement could reduce the wet requirement to 1,000 without an unacceptable loss, it would be another alternative. A planner's desire to reduce the requirement does not amend CityWater's water-service mandate; its issuing authority must make that decision.

### EAM.2:6 - Bias-Annotation

Internal objectives can omit losses experienced by customers or another service area. Trace the contribution to the actual recipient and identify whose outcome changes. Do not assume that a locally favorable utilization or accounting measure represents the service's value.

### EAM.2:7 - Conformance Checklist

Is the service requirement recoverable from its source? Does each relied-on asset contribution have the right quantity and conditions? Can the reader distinguish a demonstrated gap, a forecast and an alternative proposal?

### EAM.2:8 - Common Anti-Patterns and How to Avoid Them

A line from “strategy” to a purchase request does not establish the missing contribution. State the service and capability relation.

Treating installed capacity as delivered service hides configuration, access and network constraints. Use a qualified operating or engineering result.

### EAM.2:9 - Consequences

The practitioner can generate alternatives against a concrete need and identify assets whose contribution is no longer required. A missing relation becomes a bounded question, while unrelated strategic analysis can remain outside the current task.

### EAM.2:10 - Architectural Rationale

This pattern connects outcomes to engineering capability because asset ownership is only one way of obtaining a contribution. It retains the strategy and service decisions with their actual sources and makes the engineering allocation a separate question. That structure supports both new investment and continued-use decisions.

### EAM.2:11 - SoTA-Echoing

For deciding which asset contribution a strategic or service need requires, select an explicit comparison between the required service and a qualified present capability, followed by alternative ways to close the gap. Adopt the bounded service and commitment result from [OPS.1](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops1---identify-the-operating-system-commitments-and-flow-units) and adapt the functional-organization and bearer comparison in [SYSE.5](../Engineering%20DPF%20Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse5---develop-an-engineered-systems-functional-organization-and-bearer-alternatives) to this asset question. The Solution therefore keeps the required contribution separate from the first proposed purchase and preserves many-to-many dependencies where they matter. In North, the comparison reveals a 100 m³/h shortfall and leaves both a modification and a leased contribution available.

A serious starting alternative is to trace the investment through the organization's strategic asset-management objectives. GFMAM's *Asset Management Landscape*, third edition, June 2024, section 3.1 ([pp. 29–30](https://gfmam.org/sites/default/files/2024-06/GFMAM_AM_Landscape_v3.0_English_2024.pdf#page=29)), provides that strategic-alignment comparator. Its contribution is the link to organizational objectives; it does not qualify either CityWater option's delivered flow. Adapt that alignment by asking what service must change before treating an aligned project as necessary. The extra effort is one explicit service/capability comparison where adequate results already exist. It can expose a different bearer or demand option that an objective-to-purchase shortcut misses. The trade-off is that this local result does not settle competing strategic priorities; obtain that decision from its responsible source when it can change the asset choice. Reopen the comparison when that priority, the service mandate or a relied-on capability changes, or when an option cannot be distinguished without a more detailed allocation analysis. The professional source does not require the one-to-one hierarchy that the shortcut assumes.

### EAM.2:12 - Relations

[EAM.1](#eam1---frame-the-engineered-assets-and-required-outcomes) supplies the asset question; [EAM.4](#eam4---assess-demand-and-service-need-for-asset-decisions) qualifies demand and [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence) compares capability. [EAM.7](#eam7---generate-ways-to-supply-an-asset-dependent-service) develops alternatives. [OPS.1](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops1---identify-the-operating-system-commitments-and-flow-units) supplies service and commitment facts; [SYSE.5](../Engineering%20DPF%20Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse5---develop-an-engineered-systems-functional-organization-and-bearer-alternatives) supplies functional-organization and bearer alternatives. FPF [FPF A.6.F](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a6f---function-and-functional-precision-restoration-rpr-function) supports function-like claims when their meaning requires restoration.

### EAM.2:End

## EAM.3 - Establish the Asset Information and Configuration Basis

> **Type:** Method
> **Status:** Stable

### EAM.3:1 - Problem frame

Use this pattern when a choice depends on matching asset, condition, cost and intervention records. Two records have the same station label but concern different installed units, or a proposal uses a description that no longer applies.

Start with the decision and identify which differences would change its answer. Return a usable information basis for those assets, with unresolved matches and their consequences. An adequate current basis can be reused.

For practice with record dates, installed state and quotation validity, use [the first-use task](#eam341---first-use-with-two-quotations).

### EAM.3:2 - Problem

A station code, serial unit, design variant and configuration description can share a convenient name while denoting different things. Combining them can attach an old condition account to new equipment or price a modification of a configuration that is not installed. Requiring a complete database before any choice creates the opposite problem: useful work waits for irrelevant information.

### EAM.3:3 - Forces

Stable identifiers support continuity while changing configuration changes applicability. More data can improve the answer but adds collection, reconciliation and maintenance work. A missing match can block one option without blocking the whole asset question.

### EAM.3:4 - Solution

Name the receiving decision and select the information it requires. Identify the actual assets or intended asset referents, their locations and the configuration boundaries whose differences matter. Use [SYSE.13](../Engineering%20DPF%20Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse13---establish-configuration-identity-variants-and-effectivity) when identity, description edition or effectivity needs a fuller account.

For each relied-on record, recover its subject, source and applicable interval. Distinguish what was designed, observed, installed or proposed. A current database entry is evidence only to the extent that its source and maintenance support the claim being used.

Match the condition and performance observations to the actual unit, duty and measurement basis. Match the intervention proposal to the installed constituents and interfaces. Match costs to that same scope and horizon. State any correspondence used to join records with different identifiers.

Resolve conflicting records at their sources. A later timestamp alone does not make a record more applicable. An inspection, installation record or responsible specialist's reconciliation may settle the particular conflict. Preserve a known mismatch rather than averaging incompatible values.

Consider the consequence of each gap. If every plausible value leaves the requested answer unchanged, qualify the answer and continue. If the value changes technical eligibility, cost or service, obtain the smallest worthwhile applicable result or keep the affected option conditional.

Return the information needed for the choice in a form its recipient can inspect. A small table can suffice. Identify the configuration, duty or source change that would reopen it. An enterprise data-model redesign belongs in [EAM.14](#eam14---decide-whether-and-how-to-change-the-asset-management-system) only when that arrangement is the recurring problem being addressed.

#### EAM.3:4.1 - First use with two quotations

Use this practice when you can read asset and supplier records but still need to distinguish a record's date, the installed state and the time for which a price applies. Keep your first answer before reading the explanation and discussion. The figures and dates below are constructed teaching inputs.

**Make a first attempt.** C-07 has had drive configuration V2 since time 8; its installed state is confirmed for the required decision time 15. Quotation Q1 was issued at 12 and covers V1. A separate, unwithdrawn Q2 was issued at 6 and expressly covers the required V2 modification, service and appraisal horizon; its commercial terms remain valid until 20. Neither quotation is treated as a successive edition of the other. Which quotation can support the modification-cost claim at 15, and why? Record any correspondence or fact you cannot yet establish.

Choose an available edition containing [Use a record for one configuration-dependent claim (SYSE.13:4.4)](../Engineering%20DPF%20Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse1344---use-a-record-for-one-configuration-dependent-claim), including its uncertain-time explanation, and keep that copy available for the exercise. Read that bounded fragment with your attempted answer in view. Return here with the supported installed state, the quotation's subject and conditions, and the period needed by the decision. The rest of [SYSE.13](../Engineering%20DPF%20Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse13---establish-configuration-identity-variants-and-effectivity) is needed only if another configuration question requires it.

**Compare your reasoning.** Q2 supports the specified cost claim at 15: it covers the actual V2 modification, the needed scope and the applicable commercial period. Q1 remains a quotation for V1 despite its later issue date. Q2's issue before installation does not prevent it from describing the later installed configuration. If your actual records leave V2 or interface coverage unsettled, ask the supplier that specific question or retain a conditional cost. A quotation alone does not establish future service performance; independently applicable water-demand information remains usable.

Revise your answer where its grounds differ from this account. Then try the following changes before reading their discussions.

**Changed time.** The decision is now required at 21. Configuration and work scope are unchanged, and no renewed Q2 terms have been supplied. What remains supported?

**Discussion.** Q2 no longer supplies a valid price for the required time. Obtain applicable terms or leave the cost conditional. The installed-state account and independently usable demand information remain valid.

**Uncertain installation time.** For this separate variation, return to the decision at 15. Replace both the original installation-time premise and the confirmation of V2 at 15 with evidence of exactly one transition from V1 to V2 at a time τ in [14,16]. No independent evidence establishes the configuration at 15. Q2 covers only V2 and remains valid until 20. Can it now supply an unconditional cost?

**Discussion.** Its commercial period fits, but V2 at 15 is not established. Keep Q2's cost conditional until evidence establishes the relevant state or another applicable cost result covers the remaining possibilities. Q1's existence alone does not supply such a result. Where a requested conclusion is supported for every admissible state, retain that conclusion with its information limit; these inputs do not establish that condition for the Q2 price.

Use the same reasoning on one of your own records, stating what the available source supports and what would reopen the match. Comparing an answer with this discussion can guide correction; it does not establish independent ability on new material. If the remaining distinction is unclear, obtain competent feedback on that step before relying on an unsupported match.

### EAM.3:5 - Archetypal Grounding

In a constructed C modification case, the station register names C, the installation record identifies serial unit C-07 with drive configuration V2, and a vendor estimate prices modification of V1. The estimate cannot yet supply C-07's modification cost or feasibility.

The practitioner asks the supplier whether the proposed modification and price cover C-07/V2, giving the installed configuration and required service. A returned applicable estimate closes that gap; a statement that V2 needs another interface changes the option's cost or timing. The water-demand account can remain usable throughout this repair.

If the discrepancy concerns only an old descriptive label and the source records establish that both labels denote the same installed state, record that correspondence and reuse the estimate. No new asset or design variant is created by the label difference.

### EAM.3:6 - Bias-Annotation

Well-maintained records tend to make their assets easier to compare, which can disadvantage poorly documented sites. Treat missing evidence as an information limit rather than automatically poor condition. A vendor or asset owner may also describe scope in the way most favorable to its proposal.

### EAM.3:7 - Conformance Checklist

Can each material observation, price and intervention be matched to the right asset, configuration and use? Are actual and proposed states distinct? Does every unresolved match have a stated consequence for the receiving decision?

### EAM.3:8 - Common Anti-Patterns and How to Avoid Them

Using the latest record without checking its subject can replace applicable evidence with an unrelated revision. Match identity and effectivity first.

Completing every register field before giving advice burdens a decision that may need only one configuration fact. Select information by its use.

### EAM.3:9 - Consequences

The practitioner can combine records without silently changing their subjects. Some options remain conditional while others can be compared. Keeping the basis current costs work, so its detail and refresh conditions follow the decisions that depend on it.

### EAM.3:10 - Architectural Rationale

The information basis is organized around one decision rather than a universal asset schema. It relies on configuration guidance already available in Systems Engineering and supplies the asset-specific joins needed for condition, cost and intervention comparison.

### EAM.3:11 - SoTA-Echoing

For deciding whether a condition observation and intervention estimate apply to the same installed asset, adopt the decision-specific configuration basis in [SYSE.13](../Engineering%20DPF%20Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse13---establish-configuration-identity-variants-and-effectivity): identify the unit, distinguish it from its descriptions, and establish their applicability under the relevant conditions. Adapt that result in the Solution by joining condition, proposal and cost only where the asset choice needs the correspondence. In the C-07/V2 case, asking whether the V1 estimate covers the actual configuration can resolve or expose the consequential mismatch without recollecting the usable demand information.

The serious broader alternative is a maintained configuration baseline within an integrated asset-information arrangement. GFMAM's *Asset Management Landscape*, third edition, June 2024, sections 5.4–5.5 ([pp. 66–69](https://gfmam.org/sites/default/files/2024-06/GFMAM_AM_Landscape_v3.0_English_2024.pdf#page=66)), supplies that organization-wide information/configuration comparator. Reuse such an arrangement when it already supports the needed match. Establishing or repairing the whole arrangement first can be worthwhile for repeated decisions, but its existence or a current-status label cannot settle this particular unit/estimate correspondence. The selected local reconciliation puts effort into the answer-changing gap and preserves its evidence for reuse; it accepts less coverage of unrelated assets. It does not relax applicable configuration-control requirements. [SYSE.13](../Engineering%20DPF%20Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse13---establish-configuration-identity-variants-and-effectivity) supplies the identity and effectivity distinctions, while the professional source describes the wider maintained capability; neither establishes C-07's installed state. Reopen the comparison if an installation or source revision invalidates a match, an unresolved difference can change the option, or repeated reconciliation costs make a shared information repair the better answer under EAM.14.

### EAM.3:12 - Relations

[EAM.1](#eam1---frame-the-engineered-assets-and-required-outcomes) selects the concern. [EAM.5](#eam5---assess-asset-condition-and-performance) uses matched observations; [EAM.7](#eam7---generate-ways-to-supply-an-asset-dependent-service) and [EAM.8](#eam8---generate-maintenance-renewal-and-retirement-alternatives) use applicable proposals; [EAM.12](#eam12---integrate-specialist-results-for-an-asset-recommendation-or-decision) checks the results before decision. [SYSE.13](../Engineering%20DPF%20Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse13---establish-configuration-identity-variants-and-effectivity) governs the needed configuration basis, and [MNT.4](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt4---monitor-and-interpret-system-condition-for-maintenance) supplies condition content with its measurement and duty conditions.

### EAM.3:End

# Part B - Demand, Condition, Capacity, and Interdependence

## EAM.4 - Assess Demand and Service Need for Asset Decisions

> **Type:** Method
> **Status:** Stable

### EAM.4:1 - Problem frame

Use this pattern when an asset choice depends on how much service will be needed, where and when. Average demand can fit current capability while a seasonal peak, protected service group or changing use makes an option inadequate.

Begin with the service question and distinguish current commitments from forecasts. Return the demand scenarios and requirements needed to compare asset options. If an existing demand assessment answers the question at the relevant boundary and period, use it. Construct a new account when its missing basis could change the asset choice.

### EAM.4:2 - Problem

Demand totals hide timing, location and service differences. Forecasts can be treated as commitments, while existing commitments can be dismissed as optional scenarios. Even plausible forecasts may conceal which observation, population or loss allowance produced the number. A large forecast model can also obscure a simple known shortfall.

### EAM.4:3 - Forces

Underestimating demand can leave service inadequate; overestimating it can commit resources to unnecessary capacity. Better forecasts cost time and data work. Uncertainty matters through the options or claims it could change, not merely through the width of a reported interval. A useful component account must preserve the period and boundary in which its quantities can be combined.

### EAM.4:4 - Solution

#### EAM.4:4.1 - Fix the service question and reuse an adequate answer

Identify the service result, recipients and relevant horizon. State the quantity and quality required, its timing and location, and the source and authority of any commitment. [OPS.1](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops1---identify-the-operating-system-commitments-and-flow-units) can supply the operating service and commitment account.

Separate an authorized requirement from a forecast of use. A known seasonal commitment can be compared directly with the applicable capability. Further forecasting is useful when the choice depends on a missing or uncertain demand premise. Keep a protected-service or peak requirement explicit even when average consumption is lower.

#### EAM.4:4.2 - Construct an applicable observation basis

Choose the boundary at which demand will be compared with asset contribution. For a water district, distinguish water delivered to users from water entering the district: distribution losses make the quantities different. For a transport service, trips requested, passengers carried and vehicle movements likewise need a stated relation.

Recover present use, unmet requests and committed future use. Establish whether the observations cover the relevant users, place, period and operating conditions. Rationing, failure or inaccessible capacity can suppress recorded delivery. Obtain the missing need estimate or retain that uncertainty; relabeling observed delivery does not recover it.

Separate components whose drivers or possible interventions differ. Household use, other use and losses may be useful for a water decision. Reconcile their sum with the total on the same boundary and interval. If they disagree, investigate the mismatch that could affect the choice. A residual between compatible inlet and customer measurements may estimate losses; an unexplained discrepancy between incompatible meters cannot be assigned that meaning.

Keep the observation and its limitations available alongside the component account. More detailed segmentation is useful when it changes an option or the needed forecast. It is unnecessary merely to make the account larger.

#### EAM.4:4.3 - Vary drivers and form coherent scenarios

For each material change, explain how it affects a component: more users, different use per user, a new industrial commitment, changed losses or a shared environmental condition. Apply that change to the appropriate base. For example, a 10% increase in household use changes the household component, not automatically the district's losses and industrial use.

Combine component values that can obtain together. Several site maxima can occur at different hours; weather can also make formerly separate peaks coincide. Where timing matters, construct a common-period profile or obtain the applicable specialist account. Preserve location, service class and quality conditions that a total could conceal.

Form an unchanged-policy baseline before crediting a proposed demand-management measure. Describe a measure's affected users, expected effect, delivery conditions and cost as an alternative for EAM.7. Use its reduction only in the scenario where those conditions hold. A proposed service reduction remains subject to the relevant authority.

Test the drivers that can change eligibility or preference. A justified range or a few explicit scenarios can be sufficient. If an option has 100 units of spare contribution, an uncertain additional demand spanning 90–170 leaves its adequacy unresolved; a range wholly above 100 establishes that this option cannot cover that demand range without another contribution. This threshold can identify a useful further inquiry. Give a scenario a probability only when evidence supports that interpretation.

A more elaborate forecast is needed when an important dependency, changing population or response to price, weather or restrictions cannot be supported by the simple account. Ask the specialist for the demand at the required boundary and periods, the relevant driver combinations, uncertainty and limitations. The receiving asset decision still compares the returned result under those conditions.

#### EAM.4:4.4 - Return the demand and the premise that could change it

Compare the constructed demand with the contribution being considered, including losses, coincidence, storage and operating conditions through applicable relationships. Return quantity, recipients, location, period, drivers and uncertainty conditions to [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence) and EAM.7. Keep the source of an authorized commitment distinguishable from the evidence for a forecast.

Stop when the account distinguishes the useful options or identifies a specific unresolved premise. Obtain further forecasting or measurement when its attainable answer can change the choice or warranted claim enough to justify its burden and delay. When an observation changes a relied-on driver, [EAM.13](#eam13---track-realized-outcomes-and-reconsider-asset-plans) returns to this account and the affected capability or alternative; unchanged components can remain usable.

### EAM.4:5 - Archetypal Grounding

#### EAM.4:5.1 - Use a supplied requirement

In CityWater, North's dry-window minimum is 700 m³/h and its wet-season minimum is 1,100. Current usable capability is 1,000. An annual average of 800 would not establish adequacy for the wet season: the explicit deficit is 100 m³/h at that required time. Both shortlisted C arrangements add 200 and pass this quantity comparison under their supplied qualifications.

Now suppose a new forecast suggests 1,250 in a later period. That forecast is not automatically a revised mandate. The practitioner reports that the current 1,200-capability option would fall short by 50 under this scenario and identifies which service or investment decision would use it. A sufficiently credible and consequential scenario can warrant another option without inventing a new commitment.

#### EAM.4:5.2 - Build the scenario from its components

In a separate constructed district, Westbank, compatible observations of an unrestricted critical hour give 1,000 m³/h at the inlet: 600 for households, 300 for other users and 100 losses. The case supplies compatible measurement coverage and the loss estimate. Proposed usable capability at the same inlet is 1,200 m³/h; required quality is unchanged.

| Component at the common critical hour | Observed base, m³/h | Scenario assumption | Scenario demand, m³/h |
| --- | ---: | --- | ---: |
| Household use | 600 | 10% more use on the same service basis | 660 |
| Other use | 300 | No material change | 300 |
| Losses | 100 | Qualified future estimate of 140 | 140 |
| Total at the inlet | 1,000 | Sum of compatible components | 1,100 |

The calculation is 600 × 1.10 + 300 + 140 = 1,100. It leaves 100 m³/h of contribution available within the proposed capability. A separately supported new industrial requirement of 150 during that same hour gives 1,250 and exceeds capability by 50. The industrial addition is counted once: it was absent from the 300 base.

If the industrial maximum occurs at another hour, the practitioner obtains the other components for that hour before forming its total. Adding unrelated maxima would not establish the actual peak. If the original 1,000 observation was rationed, the unrestricted baseline first needs an applicable estimate of suppressed use.

A proposed leakage measure may reduce the scenario's losses from 140 to 80. With the industrial addition, the total would then be 660 + 300 + 150 + 80 = 1,190. [EAM.7](#eam7---generate-ways-to-supply-an-asset-dependent-service) can compare that measure with added supply, using its cost and evidence of achievable reduction. The ten-unit margin exists only while the assumed reduction, coincidence and other contributions remain supported. Treating the proposed 80 as the unchanged-policy loss estimate would hide the intervention that makes the option work.

These values illustrate the construction. They neither reconstruct CityWater's supplied demand figures nor establish an empirical forecast for another district.

### EAM.4:6 - Bias-Annotation

Observed delivery favors users who currently receive service. Consider excluded or suppressed demand when it changes the intended outcome. Demand reduction can move burden onto users whose interests are absent from the investment meeting.

### EAM.4:7 - Conformance Checklist

Can the reader recover the observation base and each material driver? Do component sums share a boundary and period, with suppressed use and coincidence addressed where they matter? Are the unchanged-policy baseline and proposed measures distinct? Are commitments, observations and forecasts distinguishable? Does each selected scenario change a decision or claim, and is any probability supported?

### EAM.4:8 - Common Anti-Patterns and How to Avoid Them

Comparing average demand with peak capacity can answer the wrong question. Compare required service at its actual window.

Using forecast demand as an authorized obligation silently changes the decision. Preserve the forecast's evidence and let the relevant authority decide any commitment.

Crediting a proposed reduction in the baseline conceals the option needed to produce it. Keep its effect with its implementation conditions and burden.

### EAM.4:9 - Consequences

Asset alternatives can be sized and timed against a need whose construction is recoverable. Some expansion proposals become unnecessary, while a local or seasonal deficit becomes explicit. Changing one driver can reopen the affected scenario without rebuilding adequate observations. The account remains qualified by its assumptions and does not guarantee future use.

### EAM.4:10 - Architectural Rationale

Capacity is judged relative to a receiving service. [EAM.4](#eam4---assess-demand-and-service-need-for-asset-decisions) supplies the demand construction and its conditions; [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence) determines what an asset arrangement can deliver, and [EAM.7](#eam7---generate-ways-to-supply-an-asset-dependent-service) compares ways to close the gap. Keeping forecasts, commitments and proposed measures distinct supports both a direct known-requirement comparison and adaptation when the demand basis changes.

### EAM.4:11 - SoTA-Echoing

Choose the least burdensome supported comparison that distinguishes the asset options. [FPF C.16](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c16---measurement--metrics-characterization-mmchr) supplies measurement and uncertainty distinctions; [OPS.1](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops1---identify-the-operating-system-commitments-and-flow-units) supplies the service and commitment account. North's known 1,100 m³/h requirement already exposes a 100 m³/h shortfall. A more accurate annual average would not resolve that peak-service question.

The Environment Agency, Natural Resources Wales and Ofwat's *Water resources planning guideline*, updated 16 June 2026, [§§6.1 and 6.4.1–6.4.3](https://www.gov.uk/government/publications/water-resources-planning-guideline/water-resources-planning-guideline#section-6--developing-your-demand-forecast), develops component demand, the observed baseline, critical periods and assumptions before additional measures. EAM adapts that contribution in the component reconciliation and driver construction above. The Westbank case shows why a changed driver or proposed reduction changes the asset comparison. Its values and arithmetic are constructed here.

A full specialist forecast is preferable when the relevant dependencies or uncertainty cannot be supported by that small construction. Request its result for the actual asset boundary and decision horizon. Reopen the method choice when new observations invalidate a driver or range, a changed period reveals a consequential peak, or the decision needs a fuller forecast. The water-planning source's jurisdictional duties and planning horizon remain with that source.

### EAM.4:12 - Relations

[EAM.2](#eam2---relate-assets-to-strategy-services-and-required-capability) supplies the service contribution and its source. [OPS.1](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops1---identify-the-operating-system-commitments-and-flow-units) supplies operating commitments and populations. [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence) consumes the scenario's quantity, place, period and conditions to compare capability; [EAM.7](#eam7---generate-ways-to-supply-an-asset-dependent-service) uses its gap and qualified demand-management possibilities to develop alternatives. [EAM.13](#eam13---track-realized-outcomes-and-reconsider-asset-plans) returns changed observations or commitments to the affected part of this account.

### EAM.4:End

## EAM.5 - Assess Asset Condition and Performance

> **Type:** Method
> **Status:** Stable

### EAM.5:1 - Problem frame

Use this pattern when condition observations or service performance can change an asset decision. A warning appears on a dashboard while the asset continues delivering service, or apparently good availability conceals deterioration.

Start with the claim the decision needs. Return an applicable account of observed condition, its supported interpretation and the service consequence. Reuse an adequate maintenance or operating result instead of commissioning another assessment.

### EAM.5:2 - Problem

Condition, delivered performance and future failure are different claims. A vibration increase can be real without identifying its cause or remaining life. Successful service during one interval can coexist with a condition that requires intervention. Aggregating them into a single health score can hide the reason an option is eligible or unacceptable.

### EAM.5:3 - Forces

Earlier interpretation can improve response while false signals cause unnecessary work. More observations can clarify deterioration but impose access, analysis and delay costs. The useful resolution depends on the asset choice, duty, consequences and time available.

### EAM.5:4 - Solution

Identify the asset, installed configuration, required functioning and decision horizon. Recover the condition account from [MNT.4](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt4---monitor-and-interpret-system-condition-for-maintenance) when available. Check the measurement location, method, units, operating state, observation window and relevant limitations before comparing values.

Keep observed, inferred and forecast claims separate. State what changed in the observations, what the applicable diagnostic evidence supports and what future-duty assumptions a forecast requires. Use a specialist's diagnosis where the mechanism matters; an alarm alone does not supply it.

Recover the relevant service-performance evidence. The useful content from [OPS.18](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops18---control-operating-quality-and-reliability) might be an affected population, observed loss, quality result or reliability evidence, with its requirement and window. A favorable operating decision is not an asset-condition certificate.

Relate condition and performance to the proposed options. Identify what contribution is at risk, the consequence of delay and the supported intervention effect. Distinguish a condition ranking from risk: risk additionally depends on the exposure, uncertainty and consequence needed for this decision.

Reconcile apparent disagreements before drawing a stronger conclusion. A change in sensor, load or reporting population can explain a discontinuity. When no adequate correspondence exists, retain separate accounts and state the claim they cannot jointly support.

Return the supported interpretation and its implication for [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence) or EAM.8. Ask for more evidence only when its attainable result could change the option, response or justified claim enough to warrant the full burden. If the existing condition assessment answers the recipient's question, provide it and finish the inquiry. Estimate remaining life only when that further answer is needed.

### EAM.5:5 - Archetypal Grounding

In the constructed D case, the supplied maintenance account identifies abnormal increasing vibration under comparable duty. A separate specialist diagnosis and policy qualification support the initial intervention and five-year continued-use policy under stated conditions. Those are distinct premises; the vibration observation does not establish the policy by itself.

Suppose the operating record also shows delivery meeting the service requirement during the observed month. The practitioner can report both maintained service during that month and abnormal condition needing the supported response. Neither claim erases the other.

If later inspection finds a different structural defect outside the policy's qualification, the EAM practitioner removes D continuation from the eligible alternatives. The portfolio changes to FFLR under the common application's unchanged limits. A continued green service dashboard does not restore the invalid engineering support.

### EAM.5:6 - Bias-Annotation

Easily measured signals can dominate attention while poorly observed failure mechanisms are neglected. Preserve the measurement's actual coverage. A predictive model's apparent precision can also disguise a duty change or insufficient evidence for its receiving use.

### EAM.5:7 - Conformance Checklist

Do the records concern the same asset and duty? Are observation, diagnosis, forecast and service result distinguishable? Does the inferred consequence follow from applicable evidence, and is the option's qualification still valid?

### EAM.5:8 - Common Anti-Patterns and How to Avoid Them

Interpreting a health score as a remaining-life date gives an unsupported forecast. Recover the model and duty assumptions or report the narrower condition result.

Interpreting current service success as proof of sound condition ignores deterioration. Keep the actual condition and functioning claims separate.

### EAM.5:9 - Consequences

The asset decision can use the available evidence without overstating it. Some options become conditional or ineligible; some investigations are unnecessary for the bounded answer. Remaining uncertainty is visible at the claim it limits.

### EAM.5:10 - Architectural Rationale

The pattern joins condition and performance at their asset consequence while leaving diagnosis, measurement and operating decisions with their supplying practices. A single score is convenient only when its construction and intended use preserve the distinctions the choice needs.

### EAM.5:11 - SoTA-Echoing

For deciding what the available condition evidence implies for an asset option, adopt the separation of observation, interpretation and forecast in [MNT.4](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt4---monitor-and-interpret-system-condition-for-maintenance), and use the applicable service-evidence component of OPS.18. The Solution matches those claims to the actual unit and duty before using them in eligibility or consequence reasoning. In D's case, the supplied diagnosis and policy qualification support the continued-use option while the observed vibration alone supports a narrower condition statement. Reusing those adequate results is the selected answer to the present question.

A serious technical alternative, when the asset choice needs a life forecast, is to fit a degradation model and project time to a supported failure criterion. The NIST/SEMATECH *e-Handbook of Statistical Methods*, [section 8.4.2.3, “Fitting models using degradation data instead of failures”](https://www.itl.nist.gov/div898/handbook/apr/section4/apr423.htm), supplies an established regression-based comparator and its physical, measurement and model assumptions. It is useful where that relationship and future-duty transfer are supported; a vibration trend by itself does not supply them. Adapt this modeling route when an obtainable life forecast could change the asset policy or timing. For the already qualified D alternatives, developing it anew would add data, fitting and validation work without being necessary for the stated comparison. The deliberate trade-off is a supported option implication with no independently derived remaining-life date. Neither the handbook nor [MNT.4](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt4---monitor-and-interpret-system-condition-for-maintenance) supplies a real pump's failure threshold. Reopen the choice when the diagnosis, duty or policy qualification changes, or when a forecast's expected decision contribution justifies the work of establishing its applicable model and evidence.

### EAM.5:12 - Relations

[EAM.3](#eam3---establish-the-asset-information-and-configuration-basis) establishes the information match. [MNT.4](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt4---monitor-and-interpret-system-condition-for-maintenance) supplies condition interpretation and [MNT.6](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt6---diagnose-condition-and-choose-a-maintenance-response) diagnosis and intervention content. [OPS.18](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops18---control-operating-quality-and-reliability) supplies the relevant operating evidence. [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence) assesses consequences and capability; [EAM.8](#eam8---generate-maintenance-renewal-and-retirement-alternatives) uses the account in asset alternatives. [FPF A.10](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a10---evidence-graph-referring-claim-bound-evidence-and-provenance-graph) and [FPF C.16](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c16---measurement--metrics-characterization-mmchr) support the relied-on evidence and measurement claims.

### EAM.5:End

## EAM.6 - Assess Asset Capacity, Resilience, and Interdependence

> **Type:** Method
> **Status:** Stable

### EAM.6:1 - Problem frame

Use this pattern when an asset option must meet demand through a particular arrangement, outage or disruption. The total installed rating appears sufficient, but the needed contribution depends on shared assets, access, timing or recovery.

Begin with the service criterion and one applicable capacity bound. Return the supported capacity and consequence account, including the condition that makes a proposed option fail. A simple calculation can be sufficient. Develop the dependencies and recovery intervals when they determine what service remains available.

### EAM.6:2 - Problem

Nominal ratings can be added even when the assets cannot supply the same service together. A fallback can rely on the same failed provider as the asset it is meant to replace. Normal-load adequacy and a successful isolated-outage calculation can then conceal loss of several contributions together.

Recovery also changes the answer over time. Enough stored reserve for one interval may be exhausted before another asset becomes usable. A single final recovery time hides that intermediate service failure.

### EAM.6:3 - Forces

Reserve capability and recovery provisions cost resources while protecting a specified service. Pooling can improve utilization but create common dependencies. More elaborate models can improve a consequential assessment, but unsupported detail cannot establish a probabilistic reliability claim.

### EAM.6:4 - Solution

#### EAM.6:4.1 - Establish the contribution being tested

Recover demand, required service, configuration and horizon. Keep quantities and time units compatible. [EAM.4](#eam4---assess-demand-and-service-need-for-asset-decisions) can supply scenario demand and its place, period and driver conditions; [EAM.5](#eam5---assess-asset-condition-and-performance) can supply the applicable condition concern. Use [OPS.10](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops10---qualify-operating-capacity-under-variability) or a specialist result to distinguish nominal capability from usable contribution.

State where the service must be delivered and which population or function it protects. An aggregate spare capacity elsewhere is useful only if the arrangement can deliver it where and when needed. Begin with a supply or load bound that the available inputs support.

#### EAM.6:4.2 - Derive the disturbance from actual dependencies

Identify the asset contributions and the dependencies that can change the answer. Follow shared power, control, providers, access, storage or another asset's functioning to the service they enable. Explain which contributions cease, degrade or remain usable when a selected dependency is lost. Include a common dependency even when it crosses the portfolio's ownership boundary.

Test a fallback against that same loss. A second pump on the failed feeder supplies no replacement flow until its needed power is restored. An alternative is independent of that feeder loss only when its power, control, connection and other necessary support remain usable under the stated scenario. This is a dependency claim for the named disturbance; a separate statistical independence claim needs its own evidence.

Choose adverse conditions because their consequences can change the asset decision: a named outage, common-provider loss or credible demand burst. Use an existing qualified scenario where it matches. Preserve simultaneous calls on shared reserve; one standby contribution cannot be allocated twice to incompatible users.

Compare material alternatives on the same disturbance and service criterion. An alternative may change the dependency itself, so recalculate the remaining contributions rather than carrying over the old consequence account.

#### EAM.6:4.3 - Follow service through recovery

Divide the disturbance into intervals at which demand, usable contribution or restoration changes. Use times to usable service, including the necessary access, work, testing and return conditions. A repair-completion estimate alone may omit the time before the contribution can actually be used.

For each interval, compare required service with supported available contribution. Where an additive bound is applicable, the positive difference is the deficit. Multiply a constant deficit by the interval length to obtain the reserve volume or resource needed during it. Carry the remaining usable reserve forward; test both its deliverable rate and its remaining amount. Account for other users' simultaneous demands on it.

Credit replenishment only when its route, rate, timing and operating conditions are supported. If flows or demand vary materially within an interval, refine the intervals or obtain an appropriate time-dependent result. A total-volume comparison alone cannot establish pressure, quality or other delivery conditions.

The service requirement may include an allowed interruption, minimum contribution or restoration deadline. Apply that actual criterion to each interval. Report where and for how long it fails. Keep evidence for restoration timing separate from a proposed recovery plan: an unqualified time leaves the dependent conclusion conditional.

#### EAM.6:4.4 - Compare remedies and return the conditions

Compare additional capability, demand changes, sequencing, reserve, another fallback or changed recovery. Preserve burden and lost service moved to other users. An option that meets this scenario becomes a qualified candidate for the asset comparison, with its costs and remaining conditions.

Obtain a hydraulic, electrical, structural or stochastic result when that relationship determines the answer. Specify the arrangement, disturbance, required service and intervals it must address. A supported specialist result can replace an inadequate simple bound without restarting unrelated parts of the assessment.

Return the service envelope, failed scenario or precise missing result to [EAM.7](#eam7---generate-ways-to-supply-an-asset-dependent-service)–[EAM.10](#eam10---compare-engineered-asset-portfolio-combinations), and the relevant outage and recovery conditions to EAM.11. Stop when the receiving question is answered. Reopen on changed demand, dependencies, recovery support or operating conditions. Passing the selected scenarios supports only their stated scope.

### EAM.6:5 - Archetypal Grounding

#### EAM.6:5.1 - A sufficient outage and buffer bound

CityWater's North area has 1,000 m³/h usable capability before C is modified and needs 700 during the dry work window. Removing A's 200 leaves 800; removing C's 300 leaves 700. Each isolated outage passes the quantity bound. Removing both leaves 500, a 200 m³/h shortfall. Their individual feasibility therefore does not justify simultaneous work.

In an additional constructed variant, an independently qualified usable buffer contains 400 m³ and can cover that deficit at the required delivery conditions. The arithmetic gives 400 ÷ 200 = two hours. It cannot support a three-hour combined outage without another qualified contribution. This calculation assumes the stated usable volume and delivery rate; it does not derive them from tank size or establish water quality.

After the selected 200 m³/h addition, normal North capability is 1,200 against the wet minimum of 1,100. That comparison does not establish performance under every loss of station, power or control. Any such stronger claim needs its own applicable scenario or model.

#### EAM.6:5.2 - Shared failure and different recovery intervals

A separate constructed water system must continuously deliver 400 m³/h. Two units each supply a qualified 250 m³/h but share one feeder. An independent third source supplies 100 m³/h. Usable stored reserve is 300 m³, with delivery qualified for the deficits considered here. These are teaching inputs, not additional CityWater facts.

A feeder loss removes both 250 contributions. One returns after one hour and the other after two. During the first hour, only 100 m³/h remains, so preserving service requires (400 − 100) × 1 = 300 m³. The reserve is exhausted at one hour. During the next hour, 250 + 100 = 350 m³/h leaves another 50 m³/h deficit. The arrangement fails the continuous-service requirement despite normal capability of 600 m³/h.

Now consider a qualified additional 250 m³/h supply that can operate independently of this feeder loss and is usable after half an hour. Its support and connection are supplied as case premises.

| Interval after loss | Available contribution, m³/h | Required reserve rate, m³/h | Required reserve volume, m³ |
| --- | ---: | ---: | ---: |
| 0–0.5 h | 100 | 300 | 150 |
| 0.5–1 h | 350 | 50 | 25 |
| 1–2 h | 600 | 0 | 0 |

Before the first feeder-dependent unit returns, required reserve is 150 + 25 = 175 m³. The initial 300 therefore covers the stated intervals, leaving 125 m³; no replenishment is assumed. From one hour, the available contributions meet the 400 requirement. The added supply is a feasible response to this constructed scenario, to be compared with other supported remedies and their burden.

If the added supply actually depends on the failed feeder, remove its contribution and the first conclusion returns: service fails after one hour. If it is independent but becomes usable only after 1.5 hours, the first hour exhausts storage and the next half-hour has a 50 m³/h deficit. Independence alone therefore does not establish timely service. Earlier availability, a further usable 25 m³ of reserve, a different restoration arrangement or another supported alternative could change that latter result.

Use actual dependency and restoration evidence before relying on such a calculation. The case establishes neither the probability of feeder loss nor the hydraulic feasibility of an unexamined network. [EAM.7](#eam7---generate-ways-to-supply-an-asset-dependent-service)/.8 compare the supported remedy; [EAM.11](#eam11---time-asset-interventions-and-manage-dependencies) must retain its half-hour availability and restoration conditions in the time arrangement.

### EAM.6:6 - Bias-Annotation

Average service can hide a severe local loss. Inspect the protected population or location used by the decision. Dependency data can also overrepresent documented technical links while omitting access, providers or decisions that affect real recovery.

### EAM.6:7 - Conformance Checklist

Are demand and usable capability compared under the same conditions? Can the reader trace the selected dependency loss to the contributions that cease? Does the reserve remain available under that loss and concurrent use? Are its amount and rate sufficient in every relevant interval? What supports restoration timing, and what stronger claim would require another model?

### EAM.6:8 - Common Anti-Patterns and How to Avoid Them

Adding nameplate ratings can overstate joint capacity. Recover the actual combined service contribution.

Calling unused capacity “resilience” leaves the protected disturbance unknown. State the loss or demand scenario and test what remains deliverable.

Using final restored capacity to cover an earlier deficit hides interrupted service. Follow the contributions and remaining reserve through the intervening intervals.

### EAM.6:9 - Consequences

The practitioner can reject an infeasible combination or identify a proportionate recovery change before committing resources. The account shows which dependency or restoration premise changes the result, so the affected alternative or timing can be reconsidered. It remains conditional on the modeled service, dependencies and evidence.

### EAM.6:10 - Architectural Rationale

The same arrangement supplies normal service and responses to disturbance. Recovering its dependencies constructs the scenario; interval comparisons establish its service consequences. [OPS.10](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops10---qualify-operating-capacity-under-variability) and specialist models supply applicable capacity reasoning, while EAM relates that result to asset choices and recovery conditions. A necessary bound and a sufficient supported scenario have different reach.

### EAM.6:11 - SoTA-Echoing

For a named outage, first use the qualified capacity/service reasoning in [OPS.10](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops10---qualify-operating-capacity-under-variability) and an applicable supply or duration bound. The constructed 400 m³ buffer and 200 m³/h deficit establish a two-hour limit, sufficient to reject the three-hour proposal.

[IAM Anatomy v4, §7.5.6, pp. 66–67](https://theiam.org/media/5615/iam-anatomy-version-4-final.pdf#page=66), relates disturbance to the extent and duration of service loss and recovery objectives. [GFMAM Landscape v3, §3.9](https://gfmam.org/sites/default/files/2024-06/GFMAM_AM_Landscape_v3.0_English_2024.pdf#page=45), distinguishes asset and organizational resilience. The dependency and recovery construction above adapts those concerns to an asset choice: the shared feeder removes two contributions, and the time at which independent supply becomes usable changes the answer. More normal capacity alone does not resolve either fact.

For consequential water-network relationships, extended-period hydraulic analysis is a stronger alternative. The US EPA's [EPANET capabilities and hydraulic modeling description](https://www.epa.gov/water-research/epanet) covers pressure, flow, tank levels and controls. Obtain such a result when deliverability or changing network behavior remains unqualified. Reuse an applicable existing result where available.

A supported simple bound is enough for the failed-duration question; dependency and interval reasoning is needed for the shared-loss question. Neither substitutes for an unresolved hydraulic relationship or failure-probability estimate. Reopen the choice of method when controls, demand, reserve delivery or restoration conditions change the answer beyond the current model's reach.

### EAM.6:12 - Relations

[EAM.4](#eam4---assess-demand-and-service-need-for-asset-decisions) supplies demand and [EAM.5](#eam5---assess-asset-condition-and-performance) the condition concern. [EAM.7](#eam7---generate-ways-to-supply-an-asset-dependent-service)/.8 use a required contribution or recovery alternative; [EAM.9](#eam9---compare-asset-alternatives-and-reconcile-decisions-when-they-conflict)/.10 use the resulting service and dependency constraints. [EAM.11](#eam11---time-asset-interventions-and-manage-dependencies) consumes the interval-specific outage and recovery conditions. [OPS.10](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops10---qualify-operating-capacity-under-variability) supplies qualified capacity reasoning, and [FPF C.16](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c16---measurement--metrics-characterization-mmchr) supports compatible quantities and uncertainty.

### EAM.6:End

# Part C - Alternatives, Conflicts, Combinations, and Timing

## EAM.7 - Generate Ways to Supply an Asset-Dependent Service

> **Type:** Method
> **Status:** Stable

### EAM.7:1 - Problem frame

Use this pattern when a needed service contribution has become a proposal to acquire or modify an asset. A team has a preferred machine, supplier or design, but materially different ways of obtaining the contribution could change cost, risk or feasibility.

Begin by separating the required contribution from the first bearer assumption. Return a small, technically meaningful alternative set, including the realization conditions the next comparison needs.

### EAM.7:2 - Problem

Searching only within the familiar equipment category can exclude sharing, leasing, reconfiguration or demand change. The opposite mistake lists attractive concepts without showing how their contributions could be realized. A vendor's availability claim then substitutes for an applicable engineering answer.

### EAM.7:3 - Forces

Ownership can provide control while creating continuing support and exit burdens. Shared or leased service can reduce initial capital while adding dependency and recurring cost. A technically novel arrangement can improve value but require evidence and integration work that the decision window cannot support.

### EAM.7:4 - Solution

Recover the required outside contribution, recipients, conditions and horizon from [EAM.1](#eam1---frame-the-engineered-assets-and-required-outcomes) and EAM.2. Identify which feature of the incumbent arrangement is an assumption rather than a requirement.

Form materially different ways to supply the contribution. Depending on the problem, these can include changing an existing asset, acquiring a new one, redistributing capability, sharing a provider, leasing a service or changing demand. A renamed supplier offering with the same relevant behavior is not a distinct architectural alternative.

Describe how each option could work. Identify the asset or provider, integration with the present arrangement, interfaces, access, support and changes to operation. Use an applicable [SYSE.5](../Engineering%20DPF%20Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse5---develop-an-engineered-systems-functional-organization-and-bearer-alternatives) result when functional organization and bearer allocation determine the option. Obtain subject-specific engineering where physics or other specialist constraints decide feasibility.

State the realization conditions and consequences at the same service basis. Include procurement and integration time, interruption, continuing cost, dependency, reversal and exit. Preserve what remains unknown; a proposed interface is not demonstrated compatibility.

Compare the set with the incumbent or a no-build response. Explain why withdrawal, demand change or another contribution is included or excluded in this case. If an option requires amending a service commitment, identify that separate decision rather than assuming the amendment.

Return enough alternatives for [EAM.9](#eam9---compare-asset-alternatives-and-reconcile-decisions-when-they-conflict) to make a genuine comparison. Stop adding options when further generation is unlikely to improve the requested answer at a worthwhile burden. Keep the precise unsupported dependency that prevents a promising option from being used.

### EAM.7:5 - Archetypal Grounding

CityWater's wet-season North requirement exceeds the present 1,000 m³/h capability by 100. The shortlisted C modification and leased service each add a qualified 200. The modification requires €3 million initial capital and €0.20 million annually; the leased service requires no initial capital and €1.20 million annually, under the supplied five-year terms.

The alternatives differ in funding, continuing cost, realization time and dependence on the service provider. Their common quantity contribution does not make them interchangeable. The lease can free capital for D replacement, while its recurring cost changes the whole portfolio comparison.

If the proposed leased service has no applicable evidence for the required connection and delivery conditions, it remains conditional. A quotation and a nominal pump rating do not establish that service. The practitioner asks for the needed engineering result rather than silently treating the option as available.

### EAM.7:6 - Bias-Annotation

A procurement channel can narrow the set before the asset question is answered. Supplier information can favor purchase or service contracts according to commercial interest. Preserve the costs and dependencies borne by the utility and service users.

### EAM.7:7 - Conformance Checklist

Are the alternatives materially different ways to provide the same needed contribution? Are their realization conditions and continuing consequences visible? Can the recipient distinguish a supported candidate from a concept awaiting a decisive result?

### EAM.7:8 - Common Anti-Patterns and How to Avoid Them

Three bids for effectively the same arrangement can conceal a missing service alternative. Challenge the bearer assumption before counting options.

Treating a service contract as removal of engineering dependence hides the provider and interface conditions. State the actual contribution and evidence required.

### EAM.7:9 - Consequences

The comparison can reveal a lower-capital, more reversible or otherwise valuable alternative. Some concepts remain conditional, and more engineering may be required for a consequential choice. Generating a set does not choose or realize an option.

### EAM.7:10 - Architectural Rationale

The pattern separates desired contribution from physical or contractual form. That preserves meaningful alternatives while allowing the engineering and financial consequences to be reconciled later. It complements [EAM.8](#eam8---generate-maintenance-renewal-and-retirement-alternatives)'s policies for existing assets instead of making acquisition the default beginning.

### EAM.7:11 - SoTA-Echoing

For finding materially different ways to obtain an asset's required contribution, adopt SYSE.5:4.1's joint development of functional organization, bearers, interfaces and realization conditions. Adapt it to the receiving asset comparison by retaining the few alternatives whose capital, continuing burden, service or dependency differences can change the choice. In CityWater, modification and qualified leased service provide the same additional flow but compete differently for capital and continuing expenditure. The Solution therefore establishes the contribution before fixing ownership or a particular construction.

A serious alternative is specification-led acquisition: hold an already justified asset arrangement fixed and compare designs or suppliers able to realize it. GFMAM's *Asset Management Landscape*, third edition, June 2024, section 6.2 ([pp. 72–73](https://gfmam.org/sites/default/files/2024-06/GFMAM_AM_Landscape_v3.0_English_2024.pdf#page=72)), provides the acquisition and integration comparator; its section 3.4 also keeps new, existing and non-asset responses available at planning scope. Retain specification-led comparison when the bearer decision is already supported. Where ownership is only an initial assumption, selecting it first could exclude C's service option before its funding consequence is examined. The broader contribution comparison costs some additional provider/interface analysis, accepted because it can change the feasible asset programme; it stops short of detailed engineering for every conceivable option. These sources supply operations and professional scope, not the lease's actual availability or compatibility. Reopen the choice when a required interface cannot be realized, a provider qualification changes, an incumbent assumption becomes an actual requirement, or a newly supported arrangement could improve the decision enough to justify examining it.

### EAM.7:12 - Relations

[EAM.2](#eam2---relate-assets-to-strategy-services-and-required-capability) and [EAM.4](#eam4---assess-demand-and-service-need-for-asset-decisions) supply the need; [EAM.3](#eam3---establish-the-asset-information-and-configuration-basis) and [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence) supply configuration and capability conditions. [SYSE.5](../Engineering%20DPF%20Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse5---develop-an-engineered-systems-functional-organization-and-bearer-alternatives) supports bearer and interface alternatives. [EAM.8](#eam8---generate-maintenance-renewal-and-retirement-alternatives) supplies existing-asset policies, [EAM.9](#eam9---compare-asset-alternatives-and-reconcile-decisions-when-they-conflict) compares value and [EAM.11](#eam11---time-asset-interventions-and-manage-dependencies) tests realization timing.

### EAM.7:End

## EAM.8 - Generate Maintenance, Renewal, and Retirement Alternatives

> **Type:** Method
> **Status:** Stable

### EAM.8:1 - Problem frame

Use this pattern when an engineered asset's future use is in question: retain it with maintenance, renew it, replace it, repurpose it or withdraw it. A feasible repair has been proposed, but the decision maker needs comparable asset policies over the relevant service horizon.

Return a small set of supported or explicitly conditional alternatives, with the consequences needed for value comparison. An adequate existing set can be reused. If the only question is which intervention maintains the already chosen function, the maintenance recommendation may answer it directly.

### EAM.8:2 - Problem

A repair estimate describes one intervention. It can omit years of energy, inspection, support and further work. A replacement estimate can omit commissioning, service interruption, exit cost or remaining value. Comparing those estimates as if they described the same service policy produces a misleading choice.

Continued use can also become a fictitious zero-cost alternative when its required maintenance and fallback are omitted. Ending a spreadsheet after two years does not establish that the asset stops working then or that its remaining contribution is worthless.

### EAM.8:3 - Forces

Early replacement can reduce continuing burden but discard useful service life. Renewal can preserve infrastructure while retaining a limiting design. Withdrawal can avoid future cost while removing a needed contribution. Long-horizon comparisons need enough detail to expose those consequences without pretending that future duty or condition is certain.

### EAM.8:4 - Solution



#### EAM.8:4.1 - Establish the service that each policy must support


Recover the required service, asset configuration and horizon. Use the relevant condition and diagnostic account to establish which maintained-use responses are supported. [MNT.4](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt4---monitor-and-interpret-system-condition-for-maintenance) supplies condition interpretation; [MNT.6](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt6---diagnose-condition-and-choose-a-maintenance-response) supplies the diagnosis and intervention recommendation. Their result must apply to this asset and proposed duty.

Form policies rather than isolated job labels. A continued-use policy includes its initial intervention, recurring maintenance, permitted duty, contingency and exit conditions. A renewal policy states what capability or useful life it changes. Replacement includes the new asset's integration and the old asset's disposition. Repurposing names the different receiving use; withdrawal names how a still-required service will be supplied or the decision that ends that requirement.

Lay out the period covered by each technical qualification. An initial repair supported for three years cannot by itself supply a four-year policy. Obtain the further intervention, replacement or service alternative that closes the remaining interval. Where condition determines the next work, state the observation and threshold that trigger it, the time needed to respond and how service remains supported while responding. A conditional forecast retains its duty and mechanism assumptions.

Keep technical eligibility separate from preference. Label an option conditional when a decisive engineering, support or permission result is missing. A proposal can be worth discussing while that result is sought, but it cannot be treated as a feasible immediate act.



#### EAM.8:4.2 - Construct the dated consequence account


For each policy, follow the work and use through time: initial preparation and integration, recurring operation and support, subsequent interventions, interruptions and temporary provision, and the intended ending. Attach each consequence to its cause and date. Include the whole intervention and return to service supplied by [MNT.7](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt7---coordinate-maintenance-intervention-and-continuing-operation); the time spent physically repairing equipment alone can understate the interruption. Carry the resulting work and service conditions into EAM.11.

Then obtain the economic consequences of that same policy. [FIN.6](CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin6---value-capital-projects) develops a dated incremental cash account: compare the proposed policy with its actual alternative, include changed operating and investment cash, and distinguish historical expenditure from future avoidable consequences. Identify the asset and configuration, receiving service, comparison perspective and date, price and discount-rate basis, relevant tax and financing treatment, and ending premise. Ask the finance supplier to return the amounts and dates, significant assumptions and unresolved limits. Its corporate-finance assumptions apply only where appropriate to the receiving case.

A recurring service price may already include maintenance, response or replacement. Check those inclusions before adding separate allowances. Conversely, a required future overhaul is still a consequence when it falls outside the current capital request. Preserve unpriced service loss, safety, environmental or other material consequences for [EAM.9](#eam9---compare-asset-alternatives-and-reconcile-decisions-when-they-conflict) instead of silently treating them as zero. A finance result values the stated policy; it does not establish that the policy can supply the service.



#### EAM.8:4.3 - Reconcile horizon and ending


Place the alternatives on a common service and analysis horizon. If their technical lives differ, describe the further work needed to cover that horizon or obtain an applicable value of remaining service. A repeating replacement chain needs supported availability, duty and cost assumptions; extending an annuity factor cannot supply them.

Distinguish the end of the study from the end of use. If the asset continues beyond the explicit account, obtain a remaining-value estimate consistent with that continuation and its further support needs. [FIN.7](CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin7---value-assets-and-the-corporation) develops valuation under a stated continued-use or disposal premise. If the asset will actually be withdrawn, use realizable proceeds and the dated cost of disconnection, disposal, closure or replacement service as applicable. Book value alone supplies neither answer. Do not add liquidation proceeds for resources whose continuing use is already included in the terminal value.

When only the explicit table endpoint moves, reconcile the value at the new endpoint with the same later payments and ending premise. The whole policy's present cost remains the same. If a supplied valuation disagrees, use [FIN.7](CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin7---value-assets-and-the-corporation) to identify the changed cash, dates, rights or assumptions before relying on it.

Use constant prices with a real discount rate, or a consistent current-price basis with its corresponding rate. Changing the required service horizon calls for reconsidering which interventions occur, which support still applies and what ending is being valued. If the service itself ends, reconsider withdrawal and other alternatives.



#### EAM.8:4.4 - Return comparable choices and their conditions


Compare eligible policies using the applicable criterion in EAM.9. Return their service and configuration, dated work and consequences, ending premise, technical support and material conditions. [EAM.10](#eam10---compare-engineered-asset-portfolio-combinations) can then combine them without losing a later funding need or counting shared work twice.

Retain the smallest alternative set that includes materially different feasible ways to meet the need. Obtain more diagnosis or costing only when an attainable answer could change eligibility, preference or the requested claim enough to justify its full burden. If [EAM.13](#eam13---track-realized-outcomes-and-reconsider-asset-plans) reports a changed duty, price or support result, revise the affected policy and its recipients; an unrelated qualified policy need not be reconstructed.

### EAM.8:5 - Archetypal Grounding



#### EAM.8:5.1 - Constructing a four-year policy


Consider a separate constructed asset E supplying the same required service under two technically qualified policies. All amounts are constant-price €million; the comparison uses a 3% real rate, year-end cash and sufficient resources for either policy. Tax and financing differences are held equal. These assumptions do not supply rates or technical support for a real asset.

Policy X retains E: initial work costs 0.40 and supports its duty through year three; a 0.90 overhaul at the end of year three supplies the further support needed for year four. Policy Y replaces E initially for 1.50 and has qualified support throughout the four years. The following account includes recurring operation and routine maintenance separately from the overhaul.

| Consequence and date | Retain and overhaul X | Replace Y |
| --- | ---: | ---: |
| Initial work at year zero | 0.40 | 1.50 |
| Recurring cost at each year end, years 1–4 | 0.30 | 0.15 |
| Further work at the end of year three | 0.90 | 0 |
| Value of continued use at the end of year four | 0.20 | 0.50 |

The teaching qualifications include permitted eight-hour work windows and temporary service sufficient to preserve the requirement during initial work and X's later overhaul. The corresponding costs are included in the initial and overhaul amounts. That makes the policies service-comparable; omitting the later window or temporary provision would leave X conditional. No other material consequence distinguishes the eligible policies in this example.

At 3%, the four-year annuity factor is 3.717098, the year-three discount factor 0.915142 and the year-four factor 0.888487. X's present cost is `0.40 + 0.30 × 3.717098 + 0.90 × 0.915142 − 0.20 × 0.888487 = 2.161060`. Y's is `1.50 + 0.15 × 3.717098 − 0.50 × 0.888487 = 1.613321`. Replacement has the lower comparable cost. Omitting the overhaul would report X as 1.337432 and reverse the recommendation while removing the work needed to support year four.

Now move the end of the explicit cash table to year two, keeping both complete policies, the required service, the rate and all later amounts unchanged. Express the remaining year-three and year-four cash, including the stated year-four continuing value, as an equivalent net value at year two:

- X: `V_X(2) = −(0.30 + 0.90)/1.03 + (0.20 − 0.30)/1.03² ≈ −1.259308`.
- Y: `V_Y(2) = −0.15/1.03 + (0.50 − 0.15)/1.03² ≈ 0.184278`.

These values represent the same remaining account on the cost-comparison basis. X's negative value means its later support payments exceed its discounted year-four continuing value. The common required service remains the same and its equal benefits are outside both cost accounts. The calculation does not estimate a sale price.

Let `a₂ = 1/1.03 + 1/1.03²` and `d₂ = 1/1.03²`. Using unrounded values, the shortened explicit accounts give X: `0.40 + 0.30 × a₂ − V_X(2) × d₂ = 2.161060`; Y: `1.50 + 0.15 × a₂ − V_Y(2) × d₂ = 1.613321`. Replacement remains cheaper. Moving the table boundary has moved later consequences into the ending value; it has removed neither their cost nor their service obligations. A different supplied appraisal needs reconciliation of its changed assumptions before it can support a different recommendation.

Actual withdrawal at year two is another case. If the authority ends the service and X incurs a net exit cost of 0.10 while Y yields net sale proceeds of 0.60, replace the continuing values with those consequences. Present costs are then 1.068300 and 1.221463. X is cheaper in this different case because the service requirement and exit consequences have changed. There is no year-three service obligation in this case. If the service remains required, withdrawal alone is incomplete: a qualified replacement service and its consequences must join the policy.



#### EAM.8:5.2 - Comparing the complete supplied policies for D


For the constructed D case, both policies supply the same required service for five years under their stated engineering qualifications. Continued use needs €0.50 million initially as operating expenditure and €1.00 million at each year end, with zero terminal value. Replacement needs €3.00 million capital, €0.35 million each year and has €1.20 million terminal value. These are teaching inputs, not estimates for a real pump.

At a 3% real rate, the five-year annuity factor is 4.579707 and the terminal factor is 0.862609. The comparable present costs are 0.50 + 1.00 × 4.579707 = 5.079707 and 3.00 + 0.35 × 4.579707 − 1.20 × 0.862609 = 3.567767 million. The comparison therefore favors replacement when both options are eligible and resources are available.

The continued-use policy is supported for the stated horizon; a one-year forecast alone would not justify five-year use. If a new finding invalidates that support, the practitioner marks the policy ineligible before comparing cost. If instead the service is no longer required, withdrawal becomes a new alternative with its own exit consequences. [EAM.10](#eam10---compare-engineered-asset-portfolio-combinations) examines D's choice together with competing assets.

### EAM.8:6 - Bias-Annotation

Retaining an asset can be favored because its purchase cost is remembered; replacing it can be favored because a supplier reports only purchase savings. Use the same receiving service and future-cost boundary, and disclose where data come from interested parties.

### EAM.8:7 - Conformance Checklist

Can the practitioner trace each policy from required service through supported intervals, later work and ending? Are its cash dates, unpriced consequences, horizon and valuation premise compatible? Can the recipient distinguish a supported option from a conditional proposal and identify what would change that distinction?

### EAM.8:8 - Common Anti-Patterns and How to Avoid Them

Treating “do nothing” as free hides maintenance and service consequences. Write the actual continued-use policy.

Treating a maintenance recommendation as the asset decision loses alternative service and lifetime-value questions. Preserve the recommendation and compare its policy with the other relevant options.

Using a valuation for a different date or continuation can create a false change in preference. Reconcile the remaining cash and ending premise before comparing.

### EAM.8:9 - Consequences

Decision makers obtain alternatives whose differences can be explained and recalculated. Some options are excluded, some remain conditional and some investigations stop. The result supports asset choice. The maintenance team carries out the intervention and returns the equipment to service under the applicable maintenance and operating decisions.

### EAM.8:10 - Architectural Rationale

This pattern joins maintained-functioning results to the asset-value question without merging them. A policy description exposes continuing consequences that a list of interventions hides. Keeping repurposing and withdrawal available prevents replacement from becoming the assumed end of a universal lifecycle.

### EAM.8:11 - SoTA-Echoing

NIST HB135e2025, chapter 4, develops the timing of initial, recurring, replacement and residual consequences on a common study period. That discipline supports the dated account here; its federal rates and programme rules are not adopted. A payback-only screen loses later support and the ending premise.

[FIN.6](CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin6---value-capital-projects) supplies the incremental financial construction, and [FIN.7](CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin7---value-assets-and-the-corporation) supplies a valuation consistent with continued use or actual disposal. Use their developed treatment when financial construction or appraisal is needed; retain a sufficient qualified local answer when it already supplies the result. EAM connects those returns to the technically supported asset policy. The numerical cases demonstrate this conditional connection and do not estimate financial or engineering performance in practice.

### EAM.8:12 - Relations

[EAM.3](#eam3---establish-the-asset-information-and-configuration-basis) and [EAM.5](#eam5---assess-asset-condition-and-performance) supply applicable asset and condition information. [MNT.6](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt6---diagnose-condition-and-choose-a-maintenance-response) supplies the maintenance recommendation and [MNT.7](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt7---coordinate-maintenance-intervention-and-continuing-operation) the whole intervention and return. [EAM.7](#eam7---generate-ways-to-supply-an-asset-dependent-service) supplies alternative ways of obtaining a changed service contribution. [FIN.6](CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin6---value-capital-projects) and [FIN.7](CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin7---value-assets-and-the-corporation) supply the dated financial account and qualified ending value; their perspective and conditions must match the asset policy. [EAM.9](#eam9---compare-asset-alternatives-and-reconcile-decisions-when-they-conflict) compares the policies, [EAM.10](#eam10---compare-engineered-asset-portfolio-combinations) tests combinations and [EAM.11](#eam11---time-asset-interventions-and-manage-dependencies) tests timing. [EAM.13](#eam13---track-realized-outcomes-and-reconsider-asset-plans) returns changed premises. [FPF C.11.DUA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11dua---make-advice-and-evidence-demands-worth-their-burden) governs the worth of further inquiry.

### EAM.8:End

## EAM.9 - Compare Asset Alternatives and Reconcile Decisions When They Conflict

> **Type:** Method
> **Status:** Stable

### EAM.9:1 - Problem frame

Use this pattern when a proposed asset choice must satisfy different technical, service, financial or operating conditions, or when individually reasonable decisions cannot hold together. It also provides the comparison for one asset whose feasible alternatives have different lifetime consequences.

Begin with the conflict or difference that can change the choice. Return a reconciled comparison, a supported recommendation or the precise unresolved conflict. A transparent cost comparison can be sufficient when service and other eligibility conditions are equal.

### EAM.9:2 - Problem

A local saving can move downtime, cost or risk to another participant. A favorable financial score can conceal an unavailable service or unsupported asset policy. Conversely, building a universal weighted score can add assumptions that nobody is authorized or able to justify.

### EAM.9:3 - Forces

Different interests and quantities need a usable decision without pretending that they share one scale. Binding conditions restrict the feasible set, while preferences compare its members. More evidence or negotiation can resolve a conflict, but it must be attainable and worth its full burden.

### EAM.9:4 - Solution

Name the alternatives, receiving service and horizon. Recover the conditions that determine eligibility and their sources. A funding allocation sets a spending limit; a service mandate sets required delivery; engineering evidence supports the proposed functioning. State their different consequences for the choice.

Identify the actual couplings behind a conflict. The same assets can participate in an operating network, a crew schedule, a maintenance programme and a funding decision. Relate their common subjects and dependencies without treating those structures as identical. Use [OPS.11](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops11---coordinate-interacting-operating-structures), [MNT.15](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt15---reconcile-simultaneous-maintenance-operation-and-support-work) or [FPF C.32.MWA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c32mwa---synthesize-an-architecture-account-of-methods-and-their-use) when their specific coordination question is needed.

Exclude unsupported alternatives from the eligible comparison or retain them explicitly as conditional proposals. An invalid qualification for D continuation cannot be offset by a low cost. If no option remains, report the unmet service or resource condition and the decision or specialist result that could change it.

Compare eligible alternatives on compatible consequences. For equal required service and admitted nonfinancial conditions, present cost can be a useful criterion. With initial capital K, initial operating cash O, annual costs Ct, terminal value S, rate r and horizon n, use K + O + Σ Ct/(1+r)^t − S/(1+r)^n. Use a consistent price/rate basis and account for costs and residual value once.

When important consequences differ, preserve those differences. An alternative is dominated only when another is at least as good on every relevant criterion and better on at least one under the same conditions. Retain a non-dominated set when no justified priority resolves the trade-off; identify who can make that choice. Do not invent weights to force a ranking.

Test assumptions that can reverse eligibility or preference. A range, scenario or break-even can be enough. Select additional inquiry by the answer it could change and the work, delay and disruption it requires.

Return the recommendation with its reasons, conditions and remaining conflict. Use [EAM.10](#eam10---compare-engineered-asset-portfolio-combinations) for a genuine combination decision and [EAM.12](#eam12---integrate-specialist-results-for-an-asset-recommendation-or-decision) for the requested asset decision or authorization. Stop when sufficient advice has been delivered.

### EAM.9:5 - Archetypal Grounding

For D alone, the constructed five-year present costs are €5.079707 million for the supported continued-use policy and €3.567767 million for replacement. With equal required service, applicable technical support and resources for either, the practitioner recommends replacement on cost: the difference is €1.511940 million.

Keeping replacement inputs fixed, continued use becomes equally costly at about €0.669861 million annual cost. A justified range of 0.95–1.05 does not reverse the answer; a credible 0.60 estimate would. The calculation identifies a potentially useful inquiry boundary without giving that lower estimate a probability or treating it as fact.

At the portfolio scope, the same D replacement needs capital that C modification and other work also need. [EAM.10](#eam10---compare-engineered-asset-portfolio-combinations) compares the whole combinations. The independent D comparison is not wrong; its resource assumption differs from the shared decision.

In a separate constructed choice, three policies are technically supported and affordable. The service mandate permits up to six hours of planned interruption for the same users in the same work window. All three meet that condition; their only material preference differences on the supplied five-year basis are:

| Policy | Present cost, € million | Planned service interruption, hours |
| --- | ---: | ---: |
| P | 3.0 | 4 |
| Q | 3.4 | 1 |
| R | 3.6 | 5 |

R is dominated: P costs less and interrupts service for less time, and Q also improves both consequences. P and Q remain: P is cheaper, while Q avoids three more hours of interruption for an additional €0.4 million in present cost. The infrastructure committee is authorized to choose within the mandate, but no priority between these two consequences has been supplied. The practitioner returns P and Q with that specific trade-off for the committee's decision. Inventing monetary weights for the interruption would conceal the unresolved preference. If a changed mandate permits only two hours, P becomes ineligible and Q is the sole eligible policy on these premises.

### EAM.9:6 - Bias-Annotation

A single monetary criterion can hide losses to groups outside the accounting perspective. Preserve nonfinancial requirements and material unpriced consequences. A familiar model can also hide false precision about future costs or terminal values.

### EAM.9:7 - Conformance Checklist

Are eligibility conditions separated from preferences? Do the quantities share a justified comparison basis? Are transferred burdens and real conflicts visible? Does the recommendation state the assumptions that can reverse it and the recipient's remaining decision?

### EAM.9:8 - Common Anti-Patterns and How to Avoid Them

A weighted score that compensates for failed required service admits an ineligible option. Apply the service condition before comparing preferences.

Treating different views as one aligned hierarchy hides shared dependencies. Recover the actual assets, work, resources and decisions that connect them.

### EAM.9:9 - Consequences

The decision maker receives an explainable preference or a bounded unresolved trade-off. Some options are excluded and some inquiries stop. The comparison can remain conditional without pretending that a budget or service amendment establishes technical feasibility.

### EAM.9:10 - Architectural Rationale

Eligibility, preference and actual authority answer different questions. Keeping them separate permits simple economic comparison where justified and richer multi-criterion judgement where needed. The asset-specific consequence account is what connects general comparison guidance to this domain.

### EAM.9:11 - SoTA-Echoing

The common NIST source supports compatible lifecycle-cost comparisons, while the professional landscape recognizes wider value and risk. This pattern uses minimum present cost only under its stated equality and eligibility conditions. Payback, condition rank or an unexplained weighted sum cannot replace that decision basis.

### EAM.9:12 - Relations

[EAM.5](#eam5---assess-asset-condition-and-performance)–[EAM.8](#eam8---generate-maintenance-renewal-and-retirement-alternatives) supply assessments and alternatives. [EAM.10](#eam10---compare-engineered-asset-portfolio-combinations) compares combinations, [EAM.11](#eam11---time-asset-interventions-and-manage-dependencies) timing and [EAM.12](#eam12---integrate-specialist-results-for-an-asset-recommendation-or-decision) the decision. [OPS.11](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops11---coordinate-interacting-operating-structures) and [MNT.15](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt15---reconcile-simultaneous-maintenance-operation-and-support-work) supply their bounded coordination results; [FPF C.11](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11---decision-theory-decsn-cal), [FPF C.11.DUA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11dua---make-advice-and-evidence-demands-worth-their-burden) and [FPF C.32.MWA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c32mwa---synthesize-an-architecture-account-of-methods-and-their-use) support comparison, useful inquiry and synthesis across relevant structures.

### EAM.9:End

## EAM.10 - Compare Engineered-Asset Portfolio Combinations

> **Type:** Method
> **Status:** Stable

### EAM.10:1 - Problem frame

Use this pattern when asset choices compete for shared funding, service, people, outages or other resources. Several individually attractive projects cannot all be performed, choosing one changes the feasible alternatives for another, or performing them together changes their consequences.

Begin with the actual combination question and its constraints. Return the preferred feasible combination, a justified non-dominated set or the precise condition that prevents one. An isolated single-asset comparison can remain in EAM.9.

### EAM.10:2 - Problem

Ranking assets by condition or ranking projects by a benefit ratio can miss a better feasible combination. Options can be indivisible, mutually exclusive or dependent. A low-capital alternative at one station can release funding for a valuable option elsewhere, while separate project approval hides that interaction.

Adding standalone costs can also count shared preparation twice or omit a cost caused by the combination. Calling the difference a portfolio saving without identifying its cause leaves the decision dependent on an unsupported discount.

### EAM.10:3 - Forces

Shared allocation must preserve required service and actual technical eligibility while comparing value. A more complete model can reveal a better combination but costs effort and relies on input quality. Deferral can preserve flexibility or create unacceptable risk, depending on its supported policy.

### EAM.10:4 - Solution



#### EAM.10:4.1 - Define complete choices and different kinds of coupling


State the portfolio scope, requested result and horizon. Recover the alternatives and their eligibility from [EAM.7](#eam7---generate-ways-to-supply-an-asset-dependent-service)–EAM.9. Identify which choices are mutually exclusive, mandatory, optional or dependent, and why. Include continued use or no new work when it is a qualified alternative. An omitted asset can still matter through a shared service or resource.

Distinguish three questions about a proposed combination. A prerequisite or exclusion determines which selections can coexist: a new unit may need an enabling connection, while two replacements for the same role may be mutually exclusive. A shared resource limit constrains the work or use at a particular time: two eligible jobs may need the same crew or exceed an outage allowance. A joint consequence changes what happens when the choices are taken together: common mobilization may reduce cost, while simultaneous demand can require additional provision. One arrangement can create all three, but each needs its own evidence.

For each material relation, identify the affected alternatives, its operating or engineering cause, the time and conditions under which it holds, and the resulting constraint or consequence. [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence) supplies service and dependency conditions. A promised saving cannot make a combination technically eligible.



#### EAM.10:4.2 - Construct the whole consequence account


Start from compatible policies on the same service boundary, perspective and horizon. If a policy omits later support or its ending, return to EAM.8. Then describe what work and service the combination actually entails. Identify shared preparation, enabling work, recurring operation, temporary service and ending consequences. Obtain amounts and dates for those actual operations.

Reconcile this whole account with the separate accounts. For costs on the same basis, `joint adjustment = whole-combination cost − sum of standalone costs`. A negative amount is a saving; a positive amount is an additional cost. Explain what causes it and when it occurs. Where effects differ by date, construct the dated differences first and obtain their financial value through [FIN.9](CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin9---compare-capital-investments-and-allocations) on the applicable basis. [FIN.9](CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin9---compare-capital-investments-and-allocations) develops this interaction comparison and dated funding constraints; its return must identify the combination, common baseline, perspective, amounts, dates and significant assumptions.

Count each shared consequence once. If two estimates each contain the same mobilization, the combination that uses one mobilization retains one payment. If three jobs share it, reconstruct their common account; summing all three pairwise discounts could remove more mobilizations than were included. If sharing requires extra supervision or temporary service, include that cost too. An allocation of common cost among departments does not by itself create a saving in the whole payment.

Keep unpriced consequences visible. Shared disruption can change a service or environmental result even when the expenditure sum is unchanged. Use [EAM.9](#eam9---compare-asset-alternatives-and-reconcile-decisions-when-they-conflict)'s actual criteria to compare those consequences; a cash adjustment cannot silently settle them. When the combination changes a demand or recovery premise, return that premise to [EAM.4](#eam4---assess-demand-and-service-need-for-asset-decisions) or [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence) before relying on its qualification.



#### EAM.10:4.3 - Test constraints and compare the feasible combinations


Write the constraints at the whole-combination scope. Separate initial capital, initial operating expenditure and recurring operating envelopes where they are different decisions. Include later commitments when they bind: the year-three overhaul in an [EAM.8](#eam8---generate-maintenance-renewal-and-retirement-alternatives) policy needs its funding, crew and service window at that time. A low initial outlay does not establish that later provision. Do not count a resource twice or assume unused funding must be spent.

Enumerate a small finite set of indivisible choices. For the CityWater shortlist, choose exactly one of two options for each of four stations and compare all sixteen. For a different question, the feasible no-work, single and combined choices depend on what service is mandatory. Remove combinations excluded by a supported prerequisite, technical condition or resource limit, retaining the reason. Obtain a feasible service-preserving calendar through [EAM.11](#eam11---time-asset-interventions-and-manage-dependencies) where timing can defeat an otherwise eligible selection.

For a larger problem, select an optimization or scenario method whose objective, choices, constraints and interactions represent the actual question. Specify what is selectable, which selections imply or exclude others, dated resource use and the joint effects. Model contingent actions with the information available when each action is chosen; the combination cannot assume different early choices for future outcomes that are not yet known. A mathematical optimum applies to the represented set and basis.

Compare eligible combinations using the actual value criteria. When required service and other material consequences are equal, minimize total present cost. Otherwise preserve justified trade-offs or a non-dominated set. A cheaper programme that requires more scarce resources does not automatically dominate a dearer one.



#### EAM.10:4.4 - Explain the choice and the condition that could change it


Show the preferred combination and the consequential alternatives it displaces. Test a changed funding limit, engineering qualification, demand driver, shared-work condition or resource date when it could alter the answer. Use coherent conditions across the combination; a common disruption cannot be favorable for one component and absent for another without grounds.

Return the recommendation, the whole consequence account, feasibility conditions and the decision-changing uncertainty to [EAM.11](#eam11---time-asset-interventions-and-manage-dependencies) and EAM.12. [EAM.13](#eam13---track-realized-outcomes-and-reconsider-asset-plans) later returns observations to the premise they affect. If a missing shared-work fact can change the choice, obtain it only when its attainable answer warrants the inquiry's full burden. A project that remains locally useful can be deferred for a qualified portfolio reason without being relabelled technically poor.

### EAM.10:5 - Archetypal Grounding



#### EAM.10:5.1 - A shared operation changes the comparison


Consider a separate constructed service requirement. Two interventions P and Q together and a different complete solution Z are both qualified to supply it over the same horizon. P or Q alone is insufficient. Their subsequent operating, ending and other material consequences are equal; all different costs are payable now in €million, and funding is sufficient for either whole solution. Thus their initial cost difference decides this bounded comparison.

P costs 2.0, including 0.2 mobilization, and Q also costs 2.0 including 0.2. Z costs 3.9. The operating practitioner establishes that P and Q can be performed sequentially during one qualified visit, using one 0.2 mobilization. Required service remains supported during the work; the shared visit incurs no additional consequence outside the supplied account.

| Whole choice | Separate estimate | Joint adjustment | Comparable cost |
| --- | ---: | ---: | ---: |
| P and Q with one mobilization | 4.0 | −0.2 | 3.8 |
| Complete solution Z | 3.9 | 0 | 3.9 |

The whole P+Q account is `1.8 + 1.8 + 0.2 = 3.8`. Adding the separate estimates would prefer Z at 3.9; the supported joint account prefers P+Q by 0.1. That result concerns one actual payment saved through a feasible work arrangement.

Suppose incompatible access windows require two visits and two mobilizations. P+Q returns to 4.0 and Z becomes cheaper at 3.9. If instead the proposed shared visit fails the service condition, remove that arrangement as ineligible and compare any qualified two-visit arrangement with Z. Reducing its price cannot repair the lost service. [EAM.11](#eam11---time-asset-interventions-and-manage-dependencies) establishes which visit arrangement is feasible; [EAM.10](#eam10---compare-engineered-asset-portfolio-combinations) uses its consequences.

The example does not infer a common saving for CityWater's separate station jobs. A proposed CityWater sharing arrangement would need its own work, service and financial account before altering the following result.



#### EAM.10:5.2 - The sixteen supplied CityWater combinations


The common CityWater application supplies four two-option choices. Initial capital must not exceed €8 million, initial operating expenditure €0.60 million, annual operation €3 million and the available team/outage time twelve days. All amounts and eligibility results are constructed.

FFMK—refurbish A and B, modify C, continue D—uses €7 million capital, €0.50 million initially for operation, €1.85 million annually and eight days. Its present cost is €14.592284 million, the lowest among the declared eligible combinations. The common application provides all sixteen rows, so this conclusion is reproducible.

Adding D replacement while retaining the other choices gives FFMR: €10 million capital and lower present cost of €13.080344 million. It is infeasible at the €8 million allocation. Switching C to leased service permits D replacement within capital, but FFLR costs €15.350138 million overall.

If the funding board raises capital to €10 million, FFMR becomes preferred. If D continuation instead loses its engineering qualification, FFLR becomes preferred at the original limits. These changed outcomes follow from changed conditions, not from changing the ranking arbitrarily.

### EAM.10:6 - Bias-Annotation

A portfolio objective can conceal which users bear losses and which costs are left outside the model. Document material omissions and the authority for trade-offs. Model size and numerical precision do not establish that the options or consequences are complete.

### EAM.10:7 - Conformance Checklist

Are all required choices, prerequisites and exclusions represented? Does the selected combination meet the dated whole-set constraints and admit a feasible schedule? Can its joint effects be traced to actual work or use and counted once? Can the recipient reproduce the preference and identify a condition that would reverse it?

### EAM.10:8 - Common Anti-Patterns and How to Avoid Them

Funding the highest-ranked items until money runs out can miss a feasible combination of different options. Evaluate the relevant combinations.

Accepting each project separately does not establish the shared condition. Construct the actual whole demands and consequences, then test their dependencies at portfolio scope.

A generic synergy percentage hides which work or cash changes. Reconcile the whole account with the separate accounts and retain the conditions that make the difference possible.

### EAM.10:9 - Consequences

The portfolio can deliver more useful service or value within actual constraints. Some individually preferred projects are displaced. The result's quality still depends on the eligible option set, consequence model and supported feasibility; it does not authorize work.

### EAM.10:10 - Architectural Rationale

The combination is the subject because shared constraints and joint consequences can change which option should be selected at each asset. This differs from both single-asset value comparison and maintenance scheduling. Enumeration is selected for small cases because the assumptions and omitted alternatives remain inspectable.

### EAM.10:11 - SoTA-Echoing

NIST HB135e2025, chapters 4, 7 and 8, supplies common-period costing, comparison of alternatives and programmes, and sensitivity reasoning. Those operations support the explicit consequence comparison; its federal rates and programme rules are outside this use.

[FIN.9](CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin9---compare-capital-investments-and-allocations) develops whole incremental cash under interactions, dated constraints and service continuations. Its B+C example shows that a negative joint cash effect can reverse the allocation even when the combined initial funding remains feasible. Use that financial construction together with the actual engineering and operating conditions; financial interaction and physical feasibility answer different questions.

Enumeration fits a small indivisible shortlist because every permissible combination and exclusion can be inspected. Independent ranking is defensible only when the relevant choices and consequences are independent and the allocation rule fits the constraints. The value-per-capital ranking in [FIN.9](CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin9---compare-capital-investments-and-allocations) requires divisible, linearly scalable investments and one initial capital limit; indivisibility, minimum scale, interactions or later funding needs can defeat it. These conditions do not hold merely because each asset has a score.

An optimizer can help when enumerating a larger set becomes burdensome, provided the actual selection rules, interactions, dates and criteria can be represented. If a consequential relation remains unqualified, retain that uncertainty or obtain the missing result. Solver precision supplies no missing alternative or engineering support. A tutorial for a particular solver is unnecessary when the finite comparison already answers the asset question.

### EAM.10:12 - Relations

[EAM.7](#eam7---generate-ways-to-supply-an-asset-dependent-service)–[EAM.9](#eam9---compare-asset-alternatives-and-reconcile-decisions-when-they-conflict) supply supported policies and comparison criteria. [EAM.4](#eam4---assess-demand-and-service-need-for-asset-decisions) supplies applicable demand; [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence) supplies service and dependency conditions. [FIN.9](CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin9---compare-capital-investments-and-allocations) supplies compatible joint financial consequences and dated funding comparison. [EAM.11](#eam11---time-asset-interventions-and-manage-dependencies) establishes timing; [EAM.12](#eam12---integrate-specialist-results-for-an-asset-recommendation-or-decision) receives the recommendation for decision; [EAM.13](#eam13---track-realized-outcomes-and-reconsider-asset-plans) returns changed premises. [FPF C.11](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11---decision-theory-decsn-cal) supports multi-criterion comparison, and [FPF C.11.DUA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11dua---make-advice-and-evidence-demands-worth-their-burden) supports proportionate additional inquiry.

### EAM.10:End

## EAM.11 - Time Asset Interventions and Manage Dependencies

> **Type:** Method
> **Status:** Stable

### EAM.11:1 - Problem frame

Use this pattern when the timing of an asset intervention can change whether the service or portfolio plan is feasible. A job estimate fits the window, but its preparation, shutdown, testing, return or shared resources do not.

Begin with the complete intervention and its service conditions. Return a feasible timing arrangement or the exact unmet condition. A value recommendation can be delivered before a particular work window has been authorized.

### EAM.11:2 - Problem

Task hours are often substituted for elapsed outage time. Local plans can share the same crew or remove each other's fallback. Reordering work can improve feasibility, but cannot reduce the total demand on one exclusive resource below its actual work requirement.

### EAM.11:3 - Forces

A larger window and more contingency improve recoverability while consuming service and resources. Combining work can reduce repeated access but increase interference. Deferral can preserve an opportunity only when the continued-use policy remains supported.

### EAM.11:4 - Solution

Recover the selected or proposed interventions, the required service and the actual calendars. Use the whole-outage arrangement from [MNT.7](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt7---coordinate-maintenance-intervention-and-continuing-operation) where applicable and the operating envelope from OPS.10. Identify the duty, configuration, access and protection assumptions those results need.

Separate preparation possible during operation from work requiring the outage. Include supported shutdown, protected access, intervention, testing and return. Establish whether estimates already include allowance before adding contingency. Distinguish person-hours, exclusive-team occupancy and elapsed service-loss time.

Represent the dependencies that determine timing. Some activities must precede others; some can overlap only with independent providers and compatible service conditions. A shared standby unit, isolation or recovery resource can prevent overlap even when labor is available.

Place the complete demands in actual windows. A necessary resource bound is total exclusive demand no greater than available time. Passing it is not sufficient when release dates, simultaneous resources or service dependencies prevent a schedule. Use a finite schedule for a small known set.

If the arrangement fails, compare a real change: another window, another supported option, a qualified provider, a service-preserving fallback or justified deferral. Include its cost and moved burden. Changing the written estimate does not change the work.

State what happens if an important condition changes during the window. Identify the time, personnel, access or fallback needed to return this asset to a supported operating state, and keep those resources available. Agree with the people controlling maintenance and operation when they must decide on a supported hold or return before that option is lost. Obtain the required allocation or operating decision before relying on reassigned resources, an extended window or changed service.

Return the timing arrangement to the people controlling the work and operation. Stop when the requested planning question is answered. Actual protected work and resumption require their own applicable permissions and evidence.

### EAM.11:5 - Archetypal Grounding

For FFMK in CityWater, the supplied whole durations are A two days, B two, C three and D one. One qualified team is available for twelve comparable work days. A on days 1–2, B on 3–4, C on 5–7 and D on 8 uses eight days, and every asset is restored before the next begins.

North's A and C outages cannot coincide: their combined loss would reduce delivery below the dry-window minimum. East's B and D outages have the same incompatibility. The serial schedule respects both conditions and the shared team. The four remaining days are uncommitted allowance, not permission to omit a return condition.

If only seven days are available, the eight-day plan fails. The declared options permit FRLK—A refurbishment, B replacement, C leased service and D continuation—in seven days at higher present cost. The practitioner compares that real option or another qualified arrangement; shortening the original estimates would not solve the conflict.

### EAM.11:6 - Bias-Annotation

Optimistic duration estimates can favor a preferred option. Treat estimate uncertainty, readiness and actual staffing explicitly. An apparent schedule saving can transfer fatigue, recovery burden or service loss to another participant.

### EAM.11:7 - Conformance Checklist

Does the schedule include the complete outage and return? Are exclusive resources and actual dependencies respected? Do service conditions hold in each interval, and is there a supported response if the work exceeds its plan?

### EAM.11:8 - Common Anti-Patterns and How to Avoid Them

Summing labor-hours and calling them an outage mixes quantities. Model the actual elapsed dependencies.

Assuming that two individually feasible outages can overlap can remove the fallback supporting each. Check their combined service and resource conditions.

### EAM.11:9 - Consequences

The programme can be planned against real windows and revised when a constraint changes. Some apparently cheaper options become infeasible. The schedule remains a prospective arrangement; actual work, functioning and resumed-use authority require their own results.

### EAM.11:10 - Architectural Rationale

Timing follows the whole intervention's participation in service rather than a universal lifecycle. This keeps scheduling, technical support and authority distinct while allowing a small finite plan to settle the current question.

### EAM.11:11 - SoTA-Echoing

[MNT.7](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt7---coordinate-maintenance-intervention-and-continuing-operation) supplies whole-outage reasoning and [OPS.10](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops10---qualify-operating-capacity-under-variability) qualified service analysis. The common asset-management sources recognize outage and resource planning. This pattern uses those results at the asset programme's horizon rather than prescribing a particular project-management tool or mandatory scheduling sophistication.

### EAM.11:12 - Relations

[EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence) supplies the service envelope; [EAM.8](#eam8---generate-maintenance-renewal-and-retirement-alternatives)–[EAM.10](#eam10---compare-engineered-asset-portfolio-combinations) supply options and combinations. [MNT.7](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt7---coordinate-maintenance-intervention-and-continuing-operation) supplies intervention timing and [MNT.15](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt15---reconcile-simultaneous-maintenance-operation-and-support-work) shared-work coordination. [EAM.12](#eam12---integrate-specialist-results-for-an-asset-recommendation-or-decision) receives the feasible arrangement for the asset decision, and [EAM.13](#eam13---track-realized-outcomes-and-reconsider-asset-plans) revisits its assumptions after relevant observations.

### EAM.11:End

# Part D - Decisions, Outcomes, and Continuing Practice

## EAM.12 - Integrate Specialist Results for an Asset Recommendation or Decision

> **Type:** Method
> **Status:** Stable

### EAM.12:1 - Problem frame

Use this pattern when an asset recommendation or decision must combine specialist answers. Finance reports affordability, maintenance recommends an intervention and operation offers an outage, but somebody must determine whether those answers concern the same option and whether the decision lies within their authority.

Begin with the result requested: advice, an asset choice or authorization. Give the recipient a supported answer at that scope. Delivering adequate advice can complete the request for advice before an authorizing decision exists.

### EAM.12:2 - Problem

Specialist results can disagree without using contradictory words. A cost estimate can concern another configuration, a condition forecast another duty and an outage another period. Combining their favorable conclusions does not establish that one asset option is feasible.

Financial advice, a spending allocation, an asset decision and equipment-work permission can also be mistaken for one approval.

### EAM.12:3 - Forces

Integration must preserve specialist limits while giving the decision maker a usable answer. Waiting for every conceivable result can postpone sufficient advice; omitting one decisive condition can make implementation unjustified. Authority may be distributed even when one committee makes the portfolio choice.

### EAM.12:4 - Solution

Name the decision and recipient. Establish whether the practitioner is asked to recommend an option, select it within delegated scope or authorize a specified action. Recover the actual basis and limits of the relevant authority when the requested conclusion relies on it.

For each specialist result used, match the asset, configuration, receiving service, horizon and proposed intervention. Extract the part that changes this decision: a condition account, qualified capacity, intervention scope, cost estimate, funding allocation or outage arrangement. The existence of a supplying framework description is not an obtained case result.

Resolve conflicting assumptions before combining conclusions. If engineering supports one duty and the operating proposal requires another, obtain an applicable result or keep that option conditional. If two estimates include the same expense, count it once. Preserve material uncertainty and missing results in the recommendation.

Distinguish advice from the conditions it uses. A finance practitioner can estimate cost and assess affordability against a funding allocation; the allocation sets the spending limit. A service mandate states the required delivery; engineering evidence supports what an arrangement can actually deliver. Identify the particular authority whose decision would change an allocation or mandate. Their amendment does not establish physical capability.

Present the supported option, reasons, conditions and displaced alternatives to the person who will decide. A concise recommendation can be sufficient. When uncertainty can change the decision, identify the missing result and the attainable inquiry worth undertaking; do not replace that question with a demand for every specialist's approval.

The authorized decision maker selects an asset option within the actual spending, service and other applicable conditions. State what was selected and the conditions of its use. Maintenance and operating authorities separately settle the permissions for protected work and resumption when that work is to occur.

Return the answer that exists. Report advice as advice, an authorized choice as an authorized choice and an unresolved decision as unresolved. Reopen the affected choice when a relied-on result, authority, configuration, duty or condition changes.

### EAM.12:5 - Archetypal Grounding

In the constructed CityWater case, the funding board allocates €8 million capital, €0.60 million initial operating expenditure and €3 million annually. The water-service authority sets the required delivery and has authority over its mandate. The infrastructure committee selects the asset programme within those conditions.

The EAM team recommends refurbishing A and B, modifying C and continuing D under its supported policy. The combination uses €7 million capital, €0.50 million initially for operation, €1.85 million annually and eight available work days. The finance practitioner checks those amounts against the allocations. The operating and engineering results qualify service and technical feasibility for the proposed work.

Sending that recommendation answers the committee's request for advice. If the committee then selects it within its authority, the team can report the authorized asset programme. That fact alone does not permit a maintenance crew to isolate D. Its work and resumption permissions must apply to the actual intervention. If finance's cost model instead concerns a replacement of D, the team reconciles that mismatch before relying on its favorable affordability conclusion.

### EAM.12:6 - Bias-Annotation

A powerful specialist or committee can make its preferred criterion appear universal. Preserve the source and scope of the conditions used, the interests affected and the decision rights of other participants. An estimate from a recognized expert still needs to concern this option.

### EAM.12:7 - Conformance Checklist

Do all relied-on results apply to the same option and use? Is the result advice, selection or authorization, with its actual recipient and scope? Are financial evidence, spending allocation, service obligation and technical support distinct? Can the recipient see the remaining condition that changes implementation?

### EAM.12:8 - Common Anti-Patterns and How to Avoid Them

Collecting favorable signatures without reconciling their assumptions leaves the option unsupported. Compare the relevant content of the results.

Using a budget approval as permission to operate or isolate equipment changes the scope of authority. Obtain the decision for the actual act when it is needed.

### EAM.12:9 - Consequences

The recipient gets one usable answer with its reasons and conditions. Some decisions remain conditional while adequate advice is delivered. The integration work can expose a precise missing result instead of commissioning a broad new study, and actual responsibility for implementation remains visible.

### EAM.12:10 - Architectural Rationale

The pattern integrates results at the asset decision because no single specialty owns all of its premises. It retains distributed authority rather than inventing one universal approver. Separating the requested result from later actions makes a small advice task both useful and complete.

### EAM.12:11 - SoTA-Echoing

The common professional source account connects asset value decisions to multidisciplinary contributions. This pattern favors content reconciliation over a generic approval checklist.

### EAM.12:12 - Relations

[EAM.9](#eam9---compare-asset-alternatives-and-reconcile-decisions-when-they-conflict)–[EAM.11](#eam11---time-asset-interventions-and-manage-dependencies) provide reconciled alternatives, combinations and timing. [MNT.6](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt6---diagnose-condition-and-choose-a-maintenance-response) and [MNT.7](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt7---coordinate-maintenance-intervention-and-continuing-operation) supply their maintenance results; [OPS.10](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops10---qualify-operating-capacity-under-variability) supplies the relevant service comparison; [SYSE.13](../Engineering%20DPF%20Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse13---establish-configuration-identity-variants-and-effectivity) supports configuration applicability. [FPF C.11.DUA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11dua---make-advice-and-evidence-demands-worth-their-burden) supports useful advice and proportionate evidence demands.

### EAM.12:End

## EAM.13 - Track Realized Outcomes and Reconsider Asset Plans

> **Type:** Method
> **Status:** Stable

### EAM.13:1 - Problem frame

Use this pattern when observations can change an asset plan or the explanation for its results. Work has been completed or money spent, but the practitioner needs to know whether the required service and expected value have been obtained.

Begin with the particular assumption or outcome at issue. Return a supported continue, revise, stop or reframe decision. An adequate operating observation can answer the question without a new monitoring programme.

### EAM.13:2 - Problem

Intervention completion, resulting configuration, delivered service and realized value can be collapsed into one success report. A changed price or demand can then be mistaken for poor intervention performance, while a completed installation can conceal an unfulfilled service contribution. Conversely, every variance can trigger an investigation that costs more than the useful answer it could provide.

### EAM.13:3 - Forces

Timely adjustment protects service and resources, while premature reaction to noise can destabilize a sound plan. Attribution requires more evidence than observing a difference. New information is useful only with enough time and capability to interpret and act on it.

### EAM.13:4 - Solution

Recover the selected asset plan and the assumptions whose truth matters now. Name the service, cost, condition, risk or continuing burden being compared, its population and interval. Preserve the distinction between a predicted consequence and an adopted requirement.

Obtain the applicable observations. Match the actual configuration, duty, measurement and reporting window to the claim. Use MNT or OPS results already available when they answer the question. A work-completion record can establish what was done without establishing the resulting service.

Compare observed and expected quantities on the same basis. Explain changes in exposure, demand, prices or accounting boundaries before treating a difference as an intervention effect. Keep a descriptive variance separate from a causal conclusion that needs more evidence.

Determine which decision changes. Continuing the current policy can be justified even when an explanation remains uncertain. A service failure or invalid engineering qualification can require a supported immediate response while its cause is investigated. A changed cost assumption can reopen the option comparison without erasing evidence of functioning.

Consider further inquiry by its attainable contribution. Identify what answer could change the plan or warranted claim, when it could arrive and the full burden of obtaining and using it. Existing observations may support the necessary update; a broad improvement study is not the default.

Return the revised or retained plan with the condition that justifies it and the next action-changing observation. Use [EAM.14](#eam14---decide-whether-and-how-to-change-the-asset-management-system), [EAM.15](#eam15---decide-whether-and-how-to-change-engineering-asset-management-methods) or [EAM.16](#eam16---deliberately-continue-and-change-engineering-asset-management-culture) only when the recurring arrangement, reusable Method or cultural process is the object needing change. Stop when the present outcome question is answered.

### EAM.13:5 - Archetypal Grounding

In a constructed later observation, annual expenditure for the selected policy is €1.95 million against the planned €1.85 million. Applicable bills show a €0.12 million tariff effect, while the remaining expenditure is €0.02 million below the comparison basis: 1.85 + 0.12 − 0.02 = 1.95.

The practitioner can update the price assumption and reconsider its effect on future options. The €0.10 million variance alone does not show that the equipment performs poorly. A separate applicable operating result is needed to establish the delivered service.

If C's installation is complete but measured usable North capability is below the required wet-season delivery, the practitioner returns that service deficiency to the operating and engineering decisions. Expenditure within budget does not settle it. The continuing supported options and response conditions remain explicit while the cause is examined.

### EAM.13:6 - Bias-Annotation

Reports can favor easily counted expenditure and completed jobs over difficult service outcomes. Survivorship, changed reporting and unequal observation can also distort comparisons. Preserve the actual population and window, including material missing observations.

### EAM.13:7 - Conformance Checklist

Are work completion, resulting configuration and realized outcomes distinct? Is the comparison basis compatible? Does the proposed action follow from the observed difference, and is any stronger causal claim supported? Is further inquiry worth its attainable contribution?

### EAM.13:8 - Common Anti-Patterns and How to Avoid Them

Calling a completed project a realized benefit skips the receiving service. Obtain the outcome evidence needed for that claim.

Treating every variance as a reason for organizational redesign misidentifies the subject. Resolve the changed assumption before choosing a broader intervention.

### EAM.13:9 - Consequences

Asset plans can adapt to actual service and changed conditions while retaining useful earlier evidence. Some uncertainties remain without blocking sufficient decisions. Continuing observation has a cost, so it follows the claims and decisions that depend on it.

### EAM.13:10 - Architectural Rationale

Outcome comparison returns to the assumptions used in the choice because a generic performance dashboard can answer a different question. Separating description, cause and decision allows timely action without pretending that every variance is fully explained.

### EAM.13:11 - SoTA-Echoing

For deciding whether new observations require an asset-plan revision, select a matched comparison of the actual outcome with the premise used in the decision, followed by reconsideration of the affected future option. Adopt [FPF C.16](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c16---measurement--metrics-characterization-mmchr)'s comparison-basis discipline and [FPF C.11.DUA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11dua---make-advice-and-evidence-demands-worth-their-burden)'s connection between an inquiry and the decision it can improve. The Solution therefore separates the observed variance, an explanation of that variance and the next choice. In the expenditure example, the applicable bills permit a price-premise update while service performance remains a separate question. This yields a usable current answer without waiting for a general explanation of the intervention's effectiveness.

A serious alternative when the receiving question concerns attributable effects is an experimental or quasi-experimental impact evaluation. The *Magenta Book: Central Government guidance on evaluation*, updated 15 May 2026, chapter 2, [“Experimental and quasi-experimental approaches to impact evaluation”](https://www.gov.uk/government/publications/the-magenta-book/magenta-book-central-government-guidance-on-evaluation-html), supplies that comparator: comparison with a defensible unaffected group or period, supported by adequate data. Adapt such a design when the causal answer could change continuation or replication and the comparison can be obtained. For the present cost-premise update, its additional design, data and elapsed-time demands would buy a stronger claim than the decision needs. The selected narrower answer accepts unresolved causal attribution; it is not a lower-cost way to establish the same causal effect. The guide also allows other impact-evaluation approaches where a credible counterfactual is unavailable, so no universal control-group requirement follows. Reopen the choice when a repeat-investment decision depends on the intervention's effect, unexplained changes reverse the supported plan, or newly available comparison evidence makes a consequential causal inquiry worthwhile. The source's government evaluation context supplies no observed CityWater outcome.

### EAM.13:12 - Relations

[EAM.12](#eam12---integrate-specialist-results-for-an-asset-recommendation-or-decision) supplies the selected decision and conditions. [EAM.3](#eam3---establish-the-asset-information-and-configuration-basis), [EAM.5](#eam5---assess-asset-condition-and-performance) and relevant MNT/OPS results supply observations and applicability. [EAM.4](#eam4---assess-demand-and-service-need-for-asset-decisions)–[EAM.11](#eam11---time-asset-interventions-and-manage-dependencies) receive changed assumptions; [EAM.14](#eam14---decide-whether-and-how-to-change-the-asset-management-system)–[EAM.16](#eam16---deliberately-continue-and-change-engineering-asset-management-culture) address recurring practice questions when they arise. [FPF C.11.DUA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11dua---make-advice-and-evidence-demands-worth-their-burden) supports the inquiry decision.

### EAM.13:End

## EAM.14 - Decide Whether and How to Change the Asset-Management System

> **Type:** Method
> **Status:** Stable

### EAM.14:1 - Problem frame

Use this pattern when the arrangement performing asset management repeatedly prevents useful decisions: information is joined incorrectly, responsibility is unclear, a needed capability is absent or a decision cannot reach the person authorized to make it.

Begin with the actual recurring failure and the people, tools and relations involved. Return a supported decision to retain or change that arrangement. A small correction can suffice; a new enterprise system is one alternative, not the default result.

### EAM.14:2 - Problem

An organization can possess policies, software and a complete asset register while its practitioners still cannot make a timely supported choice. A management-system document describes requirements or an arrangement; it does not establish that people can perform the work, obtain the information or exercise the required authority.

### EAM.14:3 - Forces

A shared arrangement can reduce duplication while creating a bottleneck or common failure. Standardization helps reuse but can obscure local service and asset differences. Changing tools or responsibilities consumes migration, learning and continuing support work whose burden can exceed the improvement.

### EAM.14:4 - Solution

Name the asset-management result that is failing and a representative occurrence or source account. Identify the receiving practitioner and decision, the observed difficulty and its consequence. Keep an untested diagnosis of the cause separate from the observation.

Recover the actual arrangement needed for that result: participating people and Systems, responsibilities, information, tools, capabilities and decision interfaces. Choose only the relations that explain the failure. The asset System being managed and the organization performing asset management are different subjects.

Compare plausible alternatives for the arrangement. These might include retaining the current arrangement, repairing one information correspondence, changing a responsibility, providing a capability, altering a decision interface or replacing a tool. Explain what each alternative would mean for the needed result and what it moves elsewhere.

Include the whole burden: design, access, migration, training, disruption, operation and maintenance of the changed arrangement. Preserve applicable authority and obligations. Obtain the arrangement or trial decision from the person authorized to make it.

Recommend retention or a change whose expected result meets the stated need and whose supported gain warrants its whole burden. Compare adequate alternatives under the relevant priorities, retaining unresolved trade-offs for the person who can decide them. If the cause is uncertain and can alter the choice, obtain the worthwhile discriminating evidence. A conditional recommendation or authorized bounded attempt can be the useful result. If an obvious correctable mismatch already explains the difficulty, give the bounded repair decision without demanding a whole-system study.

Choose the realizing practice by what must change. An information correspondence can be corrected through EAM.3. Use [OPS.11](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops11---coordinate-interacting-operating-structures) to compare already assigned work with available resources and adjust case allocation, release or coordination within existing responsibilities and authority. This includes giving another case to an already qualified and authorized performer. OPS.11.1 helps identify the activities, shared resources and completion conditions when that operating model is unclear.

Use [OCE.9](ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce9---realize-a-bounded-organization-capability-increment) for a change to organizational responsibilities or decision rights, or to establish agreed responsibilities that participants cannot yet exercise. Supply the selected arrangement or authorized bounded attempt, receiving result, participating people, representative work, service conditions and recovery needs. The change practitioner exercises one complete request-to-result path and its exception return, obtains missing access, support or authority from their responsible providers, and observes the relevant later use.

Bring back the capability that the evidence supports, with its participants, work conditions, retained support and limits, or the missing condition and next repair. Use that result to judge whether the changed arrangement can supply the asset decision on time. When correcting the mismatch under [EAM.3](#eam3---establish-the-asset-information-and-configuration-basis) answers the recipient's information question, the practitioner can provide that answer and finish the inquiry. Selection, implementation and observed effect remain different facts; preserve the fallback needed by current decisions.

Return the retained or changed arrangement and the condition that would reopen it. Use [EAM.15](#eam15---decide-whether-and-how-to-change-engineering-asset-management-methods) for a reusable Method change and [EAM.16](#eam16---deliberately-continue-and-change-engineering-asset-management-culture) for a cultural-process question rather than treating every improvement as the same intervention.

### EAM.14:5 - Archetypal Grounding

In a constructed appraisal office, four cases a week each lose 1.5 practitioner-hours because cost and condition records use inconsistent station identifiers. The observed burden is six hours a week. A proposed maintained correspondence and one responsibility for returning mismatches requires twelve hours to establish, including training, then half an hour a week to maintain.

Over ten comparable weeks, continued rework would consume sixty hours if the observed rate persists. The bounded repair would consume 12 + 10 × 0.5 = seventeen hours if it removes that mismatch. A proposed new application requires eighty hours to establish and two hours a week to support: one hundred hours on the same horizon. These are explicit teaching assumptions, and consequential error risk must be compared separately from time.

The practitioner can recommend the bounded repair, then inspect whether matching actually improves. The projected forty-three-hour difference is not a claim of realized savings. If records reveal that the mismatch was only a symptom of an unresolved configuration, [EAM.3](#eam3---establish-the-asset-information-and-configuration-basis)'s information question remains necessary.

In a larger constructed variant, a new arrangement changes the roles' ongoing responsibilities: the cost analyst is to request a joint appraisal, the condition engineer is to resolve the unit correspondence with the source, and the committee secretary is to return an incomplete contribution to the responsible participant. All three use the maintained unit correspondence when preparing and receiving the appraisal. These contribution and return responsibilities must become workable. Once the authorized arrangement or trial decision is supplied, [OCE.9](ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce9---realize-a-bounded-organization-capability-increment) can exercise an appraisal from its request through comparison to a usable committee packet, including an unknown-unit case. If the condition engineer lacks effective access, the useful first result is that missing access and the responsible provider's required action. After it is supplied, representative later appraisals can establish what the new arrangement actually supports. The result states the observed conditions and remaining limits; purchasing the shared tool does not establish that capability.

A different office may already have adequate responsibilities but have twelve assigned half-hour condition checks competing for four available engineer-hours. Under those durations, the available time accommodates eight checks. The practitioner uses [OPS.11](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops11---coordinate-interacting-operating-structures) to compare which checks to release now and when to do the remaining four, carrying the effects on the asset decisions. OPS.11.1 relates the checking step to the analyst's and secretary's work before anyone promises completed appraisals. When these choices lie within existing responsibilities and authority, this is operating coordination; a changed allocation does not itself require redesigning the contribution relationships.

### EAM.14:6 - Bias-Annotation

Software providers and organizational sponsors can make their solution define the problem. Include work shifted to frontline practitioners and service users. A structurally neat responsibility chart is not evidence of usable capability or information access.

### EAM.14:7 - Conformance Checklist

Is the failed asset-management result recognizable? Does the selected change act on the actual arrangement and have a plausible mechanism of improvement? Are implementation authority, whole burden and the intended outcome comparison explicit?

### EAM.14:8 - Common Anti-Patterns and How to Avoid Them

Purchasing an application and declaring the management system realized skips the work and relationships needed to use it. Establish the actual capability and interfaces.

Changing the organization to fix one record mismatch can impose needless burden. Compare the bounded correction with the larger alternatives.

### EAM.14:9 - Consequences

Practitioners can obtain a more usable arrangement or retain an adequate one. The change can have migration and continuing costs, and its effects need observation at the intended result. A new document or tool alone supplies no effectiveness conclusion.

### EAM.14:10 - Architectural Rationale

The pattern's subject is the arrangement that performs asset management. Keeping it separate from the managed assets, reusable Methods and cultural processes makes the proposed intervention and its evidence testable. The realizing practice follows the needed change: OPS supports operating coordination within existing responsibilities, while [OCE.9](ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce9---realize-a-bounded-organization-capability-increment) supports changing organizational responsibilities or decision rights and making agreed responsibilities workable. [EAM.14](#eam14---decide-whether-and-how-to-change-the-asset-management-system) uses the resulting capability and its limits to reconsider the asset-management arrangement.

### EAM.14:11 - SoTA-Echoing

How should an appraisal office repair a recurring failure to produce a usable asset decision? Adopt the result-driven comparison in this Solution: identify the failed contribution, compare a bounded correction with retention and larger arrangement changes, and include their continuing burden. For operational adjustment within existing responsibilities, use the coordination in [OPS.11](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops11---coordinate-interacting-operating-structures) and the OPS.11.1 operating model. When the difficulty requires organizational realization, adapt the complete contribution and exception test in [OCE.9](ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce9---realize-a-bounded-organization-capability-increment) (§§4.1–4.6) to the asset-appraisal work.

An organization-wide maturity assessment is a serious alternative when the weakness is not yet localized. GFMAM's Landscape, third edition (2024), pp.9–10, describes that broader assessment. It can reveal weaknesses outside the observed appraisal flow. For the known identifier mismatch, however, broader coverage does not resolve the mismatch or demonstrate that the repaired flow works. The chosen trade-off is a narrower conclusion with a directly testable correction: the Solution and worked case address this failed contribution without claiming that the entire management system is adequate.

[OCE.9](ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce9---realize-a-bounded-organization-capability-increment) supplies the realization operations and their result limits; the constructed office comparison supports the bounded burden calculation, not observed improvement. The GFMAM assessment is retained for the wider question, rather than rejected as ineffective. Reopen this choice if failures extend beyond the selected flow, the correction leaves the problem unexplained, or a wider assessment reveals a common cause that changes the proposed arrangement.

### EAM.14:12 - Relations

[EAM.13](#eam13---track-realized-outcomes-and-reconsider-asset-plans) can reveal the recurring problem and [EAM.3](#eam3---establish-the-asset-information-and-configuration-basis) the information mismatch. [EAM.15](#eam15---decide-whether-and-how-to-change-engineering-asset-management-methods) addresses reusable ways of doing the work; [EAM.16](#eam16---deliberately-continue-and-change-engineering-asset-management-culture) addresses transmission and continued practice. [FPF A.22](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a22---structure-and-structural-views-struct-cal) supports selected structures and [FPF C.32.MWA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c32mwa---synthesize-an-architecture-account-of-methods-and-their-use) the needed synthesis across unlike practice structures. [OPS.11](OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops11---coordinate-interacting-operating-structures) and OPS.11.1 support workload and flow adjustments within existing responsibilities. [OCE.9](ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce9---realize-a-bounded-organization-capability-increment) supplies a qualified realization or missing-condition result when organizational responsibilities or decision rights must change, or agreed responsibilities must become workable.

### EAM.14:End

## EAM.15 - Decide Whether and How to Change Engineering Asset-Management Methods

> **Type:** Method
> **Status:** Stable

### EAM.15:1 - Problem frame

Use this pattern when the reusable way of making asset decisions no longer answers current questions, or when a new technique could improve it. A condition ranking fails a coupled investment choice, a forecasting model no longer fits demand, or a new optimizer promises improvement without accounting for its data and interpretation burden.

Begin with the working question and the reusable operation that may need change. Return an adequate existing Method, a supported change or an explicitly qualified candidate. A new standard edition or tool release alone is not a reason to replace the repertoire.

### EAM.15:2 - Problem

Template, software and vocabulary changes can be mistaken for Method improvement. Conversely, a changed rule for eligibility, comparison or stopping can be hidden inside a spreadsheet update. Selecting techniques by fashion leaves their actual contribution and continuing burden unresolved.

### EAM.15:3 - Forces

Reusable Methods improve consistency while their assumptions can fail as assets and environments change. More sophisticated analysis can improve a consequential choice but demand unavailable evidence or displace useful work. General reuse needs enough explanation of applicability without freezing one context's inputs as universal rules.

### EAM.15:4 - Solution

Name the asset-management result and present difficulty. Recover the current way of obtaining it: operations, necessary inputs, comparison rules, applicability, useful result and stopping conditions. Distinguish a Method question from missing data, a tool failure or an organizational bottleneck.

Compare the existing way with materially different alternatives using the same question. Consult the relevant current technical sources, preserve their scope and identify what each alternative changes in practice. A different rate or asset price can be an input change; a different eligibility or selection rule can change the reusable way of doing.

Test the alternatives on the situations that expose the claimed difference. A desk calculation can establish a mathematical failure or improved answer for those inputs. A claim about real practitioner effort, decision quality or continuing effectiveness needs evidence of that actual use.

Compare the whole burden of obtaining, using and maintaining the proposed technique, including model fitting, data, interpretation, training and displaced decisions. Select further inquiry or a trial only when its attainable result can change the choice or warranted claim enough to justify that burden.

State the selected disposition. Retain a sufficient Method, adopt a supported change within actual authority, keep a candidate for a bounded trial or return the specific unresolved result. A current answer to one asset question need not wait for a general field-effectiveness study.

When later users need to distinguish a reusable variant, candidate lineage, changed description or tool, use [FPF A.3.1.MV](../../FPF-Spec.md#a31mv---construct-and-maintain-a-method-variant)'s provenance and reuse guidance. Preserve which operations are proposed, where they came from, the conditions and tests supporting them, and what remains untried. A desk calculation can establish how a proposed comparison works on supplied inputs. To report its actual application, identify the practitioners, the appraisal occasions, the operations they performed with the available information and support, and the results they returned. Neither a proposal nor its successful calculation establishes that later users have applied it.

Keep the applicable repertoire and its reconsideration conditions discoverable to users. Reopen it when a new problem, evidence or technical result changes its contribution; avoid mandatory refresh merely because a date or publication changed.

### EAM.15:5 - Archetypal Grounding

For CityWater, consider the candidate rule “fund the highest-condition-priority asset first, using its individually preferred option.” A priority order D, C, A, B would allocate 3 to D replacement, 3 to C modification and 2 to A refurbishment, exhausting the capital before B's required option. The rule fails to supply the needed four-station programme under the declared conditions.

Combination comparison instead finds FFMK within capital and service constraints. This desk case establishes the limitation of the priority rule for this problem and supplies a supported present answer. It does not establish that a new tool improves every real investment decision.

For repeated use, practitioners can compare the techniques on representative cases with the same available inputs, recording unmet constraints, decision differences and total analysis effort. A bounded trial is useful when those real-use consequences can change adoption. Adding a more complex optimizer to a sixteen-combination problem needs a gain beyond producing the same answer.

### EAM.15:6 - Bias-Annotation

Successful demonstrations can overrepresent easy cases and expert users. Compare relevant failure cases, data availability and routine practitioner burden. A tool's technical benchmark can differ from the asset decision's useful result.

### EAM.15:7 - Conformance Checklist

Is the changed object a reusable operation, an input, a description or a tool? Does the comparison use the same practical question and preserve applicability? Is the gain supported at the scope claimed, with full burden and candidate status visible?

### EAM.15:8 - Common Anti-Patterns and How to Avoid Them

Equating newer software with a better Method bypasses the receiving decision. Compare its contribution using relevant cases.

Treating one successful calculation as field effectiveness overstates the evidence. Keep the mathematical result and observed practice claim separate.

### EAM.15:9 - Consequences

The repertoire can remain useful as asset questions and technical knowledge change. Some incumbent Methods are retained, some candidates need evidence and some techniques are unnecessary for the current task. Maintenance of reusable guidance has its own cost and responsibility.

### EAM.15:10 - Architectural Rationale

The pattern concerns reusable ways of obtaining asset-management results rather than the organization or one asset choice. It uses direct technical comparison and the existing Method Engineering contribution.

### EAM.15:11 - SoTA-Echoing

The common source account distinguishes professional concerns from technical Methods, including the limits of ratio ranking and whole-cost comparison. This pattern compares the actual contemporary technique needed for the question rather than treating an institutional repertoire as timeless or universally optimal.

### EAM.15:12 - Relations

[EAM.1](#eam1---frame-the-engineered-assets-and-required-outcomes)–[EAM.13](#eam13---track-realized-outcomes-and-reconsider-asset-plans) supply the working questions and outcomes that motivate Method change. [EAM.14](#eam14---decide-whether-and-how-to-change-the-asset-management-system) supplies an arrangement change where needed; [EAM.16](#eam16---deliberately-continue-and-change-engineering-asset-management-culture) concerns cultural continuation. [FPF A.3.1.MV](../../FPF-Spec.md#a31mv---construct-and-maintain-a-method-variant) supplies variant, provenance and reuse guidance. [FPF C.11.DUA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11dua---make-advice-and-evidence-demands-worth-their-burden) governs the worth of additional inquiry and trials.

### EAM.15:End

## EAM.16 - Deliberately Continue and Change Engineering Asset-Management Culture

> **Type:** Method
> **Status:** Stable

### EAM.16:1 - Problem frame

Use this pattern when the question concerns how a bounded population generates, transmits, uses, recognizes, selects, retains or loses an asset-management practice. A new appraisal template has been distributed, but the practice leader needs to know whether planners and decision makers actually continue the intended way of comparing assets.

Begin with the particular cultural claim and the people and interval it concerns. Return a supported account or a decision to retain, change, branch or stop a practice, with the limits needed by its recipient. Further inquiry is conditional on its useful contribution and full burden.

### EAM.16:2 - Problem

Teaching, access to tools, a declared policy and actual continued practice can be treated as the same event. A committee's selection of an asset can also be mistaken for cultural selection of the appraisal rule used to recommend it. These errors make an intervention appear effective before the relevant receiving or later activity is known.

### EAM.16:3 - Forces

Continuity preserves useful knowledge while changed conditions can make inherited practice ineffective. A centrally promoted rule can improve coordination or silence local evidence. Observing cultural processes takes access and interpretation work, and an intervention can impose burden on people beyond its sponsor.

### EAM.16:4 - Solution

State what the recipient needs to know or decide. Bound the practice content, population, setting and interval. “Asset-management culture” is too broad when the question concerns one appraisal rule among a particular group of planners and committee participants.

Distinguish the cultural processes that matter to that question. Generation concerns a proposed variant; transmission concerns its passage to recipients; receiving use concerns what they actually do. Recognition concerns which practice is treated as competent or appropriate; selection concerns which reusable practice is favored or continued; retention and loss concern what persists or disappears across later relevant occasions. Select the claims needed here rather than demanding evidence for every process in every case.

Identify the actual participants and carriers used by those claims: people, descriptions, templates, teaching or decision activity, and the arrangements through which they interact. A document's presence can support an availability claim. It does not by itself establish teaching, actual use or continued use.

Recover the available evidence for each claimed process and its limits. Keep observation, interpretation and causal explanation distinct. For a proposed appraisal rule, identify the operations it recommends and the cases or tests that support that proposal. For an actual-use claim, identify who used which operations in a particular appraisal, with what information and support, and what result they returned. Appraisal records, observation or a practitioner's account can support that claim to the extent that they show those actions; state what is unknown or only reported. A successful desk calculation supports that calculation. It does not establish use by planners, committee recognition or persistence on later occasions.

Give the supported answer now. If the recipient asks what current evidence establishes, a report of known transmission and unknown later use can be sufficient. If a conclusion about continuation is required, identify the missing evidence and consider an attainable inquiry whose contribution warrants its access, interpretation, delay and displaced work.

When change is worthwhile, compare continuation and plausible interventions at the actual practice. A revised example, peer demonstration, altered appraisal rule or recognition condition can affect different participants and processes. Name who is authorized to make that change, the intended contribution and the evidence that would support or defeat it. Do not infer authority from sponsorship, expertise or possession of the template.

Consider a branch when identified groups work under materially different conditions and one common instruction would lose a needed distinction or impose avoidable work. A branch keeps a distinct, condition-qualified practice for part of the population. Name each group, the relevant conditions, which rule it is to use, and the observations or other grounds supporting that choice. Keep common service, evidence and authority requirements explicit. Compare the gain with maintaining and explaining two variants, exclusion risks and the chance that someone will select the wrong one. Mere disagreement or a group's preference is insufficient.

Return which practice each group may continue or is proposed to adopt, the decision maker and their authority, the supported scope, and the reason. When the recipient needs a proposal to decide whether to make the change, the practitioner can submit the supported proposal and finish the inquiry. If the authorized decision is to branch, make the two instructions and their selection condition available to the affected practitioners. Reconsider the branch if the conditions cease to distinguish the groups, a variant produces an unsupported decision, or the burden of keeping them separate outweighs the gain. Observe later use or retention only when the decision or claim requires it. A complete current account need not create a new survey, training event or culture-change programme.

### EAM.16:5 - Archetypal Grounding

In a constructed example, three CityWater planners receive a common-horizon appraisal template and attend a documented explanation. Those records establish distribution and teaching. The practice leader asks what is known about continued use. The investigator reports those facts and states that later use by planners and recognition by the committee have not yet been established.

Suppose two later appraisal records are then available. One uses the stated horizon and compares eligible combinations; the other ranks interventions by condition alone. The investigator can report that the two observed appraisals differ in the relevant practice. That is evidence about those occasions, not retention across the whole population or a causal effect of the teaching.

If a decision about continuation needs more evidence, the investigator considers later comparable appraisals and committee decisions whose interpretation is attainable and useful. If change is selected, the practice leader can propose a worked example or a changed appraisal instruction within their authority. The committee's actual choice of the FFMK programme remains separate from any decision to retain the combination-comparison rule for future work.

A separate constructed case shows a branch. At another utility, central planners prepare programmes whose assets share funding and outage constraints. Depot planners also appraise isolated assets where the stated service, funding and calendar conditions do not couple that choice to other assets. Available appraisal records show the central group comparing combinations and the depot group comparing the eligible options for one asset, with a stated horizon and whole-life costs. Requiring a programme table for every isolated choice adds preparation without introducing another eligible combination. The practice owner is authorized to set these groups' appraisal instructions and decides to retain both forms: central planners use the combination comparison; depot planners may use the single-asset comparison only while the independence conditions hold. Both retain the service requirements and actual decision authorities. A shared constraint sends a depot appraisal to the programme comparison. The result is a qualified instruction for each group, supported by those working conditions and records. It establishes neither later compliance with the instructions nor retention throughout either group. A later case revealing a missed shared constraint reopens the selection condition and the affected appraisal.

### EAM.16:6 - Bias-Annotation

Visible participants and formal documents can dominate the account while informal transmission and excluded practitioners remain unobserved. Avoid treating one group's preferred practice as universal competence. Account for the burden and interests of the people expected to change.

### EAM.16:7 - Conformance Checklist

Are the practice content, population and interval clear? Does the evidence support the particular transmission, use, recognition or retention claim? For a branch, can each group identify its rule and the conditions under which it applies, with a reason for maintaining the difference? Is a proposed intervention directed at that process under actual authority, and is additional inquiry worthwhile for the requested answer?

### EAM.16:8 - Common Anti-Patterns and How to Avoid Them

Training attendance is evidence of attendance, not continuing appraisal practice. Obtain or qualify the receiving-use claim.

An asset decision is not automatically selection of a reusable Method. Identify which practice the relevant population is recognizing or retaining and the evidence for that conclusion.

Keeping two templates does not establish a useful branch. Distinguish the groups' working conditions, the rule each uses, the common requirements and the circumstances that reopen that choice.

### EAM.16:9 - Consequences

A practice leader can distinguish useful continuity, a supported change and honest uncertainty. Some investigations stop with a sufficient account. Cultural effects can remain unproven after a technical or organizational change, and different groups can legitimately retain different qualified variants.

### EAM.16:10 - Architectural Rationale

Cultural continuation has different subjects and evidence from asset outcomes, organizational arrangement or reusable Method design. Keeping those questions separate avoids inferring adoption from publication while allowing an ordinary bounded account before formal modeling is needed.

### EAM.16:11 - SoTA-Echoing

For the question of whether to continue or change one appraisal practice, adopt C.36:4's process-specific cultural account and adapt C.36.MC:4.1's qualified continuation, intervention and branching comparison. They supply the selected line: first establish what happened among the named people, then choose only the change or inquiry that can improve their actual decision. The Solution therefore allows a sufficient account of known teaching and unknown later use, and gives a branch a population, rule, conditions and reason. It accepts a narrower conclusion in exchange for avoiding unsupported claims about a whole organization.

A serious alternative for carrying a selected change across an organization is a structured change-management programme. GFMAM's *Asset Management Landscape*, third edition, June 2024, section 4.5, supplies that comparator, including communication, training and reinforcement ([pp. 56–57](https://gfmam.org/sites/default/files/2024-06/GFMAM_AM_Landscape_v3.0_English_2024.pdf#page=56)). Adapt those activities when the actual intervention needs them. They do not answer the separate question of which planners used a particular comparison on later occasions. For the two-record case, beginning a wider rollout would add participant and coordination work before the evidence identifies the needed change; the selected account can already return the known difference and its limits. This is a scope and burden trade-off, not a claim that a bounded account delivers the effects of a change programme. [FPF C.36](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c36---cultural-evolution-and-cultural-evolution-engineering) and [FPF C.36.MC](../../FPF-Spec.md#c36mc---qualify-and-develop-a-method-culture) provide the distinctions and decision operations, not evidence that CityWater's practice persisted. Reopen the comparison when later observations show a failure shared across the bounded groups, the branch no longer separates their conditions, or an attainable intervention can improve the required practice enough to justify its wider work.

### EAM.16:12 - Relations

[EAM.13](#eam13---track-realized-outcomes-and-reconsider-asset-plans) supplies outcome observations, [EAM.14](#eam14---decide-whether-and-how-to-change-the-asset-management-system) arrangement questions and [EAM.15](#eam15---decide-whether-and-how-to-change-engineering-asset-management-methods) reusable Method proposals. [FPF C.36](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c36---cultural-evolution-and-cultural-evolution-engineering) is the direct general cultural contribution. [FPF C.36.MC](../../FPF-Spec.md#c36mc---qualify-and-develop-a-method-culture) supplies related Method-engineering cultural guidance when that specific question is present, including the distinction between proposed practice, observed use and later continuation.

### EAM.16:End

# Cross-Pattern Applications



## EAM.Application:1 - APP-EAM-01 - One asset and a supported value comparison



### EAM.Application:1.1 - Shared CityWater premises

CityWater 2027 is a fictional utility with twelve pumping stations in two service areas. A and C are in North; B and D are in East; the other eight stations supply the remaining capability and are unchanged by the compared options. A, B and D have abnormal vibration. Existing, case-supplied diagnostic accounts distinguish their conditions and support the particular interventions below; the vibration label alone supplies neither diagnosis nor a life estimate.

The case supplies an existing water-delivery mandate issued by CityWater's water-service authority. It requires water of the stated quality and minimum delivered North/East rates of 700/700 m³/h during the dry work window and 1,100/900 during the wet season. The case assigns revision of this mandate to the water-service authority; the infrastructure committee chooses the asset programme within it.

Separately, the supplied operating account gives normal usable North/East capability of 1,000/1,000 m³/h. The wet-season North requirement exceeds present usable capability by 100 m³/h. Both shortlisted C options add 200 m³/h, either by modification or by a qualified leased service. The 200 is the contribution of these options, not an unstated minimum increment. During a dry-window outage, A removes 200 from North and C removes 300; B and D each remove 200 from East. One A or C outage fits the dry requirement, but their simultaneous outage gives only 500 and does not. Simultaneous B and D outages leave 600 in East and also fail. These are finite supplied service bounds, not a hydraulic model or a probability of reliability.

The case additionally supplies applicable engineering and service-risk qualifications for each shortlisted policy, including the supported fallback and response to abnormal conditions. Their boundaries cover the stated duty and horizon. No claim about every contingency or a new real equipment limit is derived from the simple supply totals. If a qualification is absent or invalidated, [EAM.9](#eam9---compare-asset-alternatives-and-reconcile-decisions-when-they-conflict) removes that option from the eligible comparison and returns the missing specialist question. Lower financial cost does not repair the missing qualification.

The comparison horizon is the five years beginning with the initial 2027 decisions. All values are constructed millions of constant-price euros, from the utility's stated perspective. The real discount rate is 3% solely for this example. Initial capital and initial operating cash occur at time zero; recurring costs occur at each year end; residual value occurs at the end of year 5. The supplied terminal values represent remaining service value, net of the stated exit costs, on the same basis for every option. A different sale/withdrawal decision needs its own terminal-value basis. Different technical lives do not disappear at the five-year boundary.

The annual amounts include the specified energy, routine maintenance, inspection, contingent response and continuing service costs under each policy; do not add them again as a separate generic risk allowance. A material unpriced consequence remains outside the sum and must retain its own criterion. Historical expenditure is sunk for this future choice. Accounting depreciation is not an additional cash outflow. Financing and tax effects are held equal in this constructed comparison; a real difference would require explicit treatment by its supplying practice.

Define `a = Σ(t=1..5) 1/(1.03)^t = 4.579707187` and `d = 1/(1.03)^5 = 0.862608784`. For each option, `present cost = initial capital + initial operating cash + annual cost × a − terminal value × d`.

| Asset/option | Initial capital | Initial operating cash | Annual cost | Terminal value | Whole team/outage days | Present cost |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| A: refurbish (`F`) | 2.0 | 0 | 0.30 | 0.40 | 2 | 3.028869 |
| A: replace (`R`) | 3.5 | 0 | 0.18 | 1.30 | 3 | 3.202956 |
| B: refurbish (`F`) | 2.0 | 0 | 0.35 | 0.40 | 2 | 3.257854 |
| B: replace (`R`) | 3.5 | 0 | 0.18 | 1.30 | 3 | 3.202956 |
| C: modify (`M`) | 3.0 | 0 | 0.20 | 0.80 | 3 | 3.225854 |
| C: leased service (`L`) | 0 | 0 | 1.20 | 0 | 1 | 5.495649 |
| D: continued-use policy (`K`) | 0 | 0.50 | 1.00 | 0 | 1 | 5.079707 |
| D: replace (`R`) | 3.0 | 0 | 0.35 | 1.20 | 3 | 3.567767 |

Each duration includes the required isolation, intervention, testing and return for that option, using one already qualified and available team. Prerequisite design, procurement and non-outage preparation are supplied as complete before the window. Days denote the same staffed whole-work windows in both the calendar and the estimates; they are not individual person-days. These are teaching inputs, not equipment procedures or industry duration norms. For a real case, use the [MNT.7](../Engineering%20DPF%20Suite/MAINTENANCE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#mnt7---coordinate-maintenance-intervention-and-continuing-operation) result rather than assuming those inclusions.

The D continued-use policy is a supported five-year service policy with the specified initial maintenance intervention, recurring maintenance, response and backup provisions. It is not an unsupported extrapolation of a one-year condition forecast. The case's qualification is conditional on unchanged duty and the identified failure mechanism; a new structural finding invalidates it. No new diagnosis, repair effectiveness or permission is inferred from the economic calculation.



### EAM.Application:1.2 - The request about D and its answer

The infrastructure committee asks the EAM practitioner whether D should continue under the supported maintenance policy or be replaced now, assuming both choices have funding and a suitable window. MNT can adequately recommend the 0.50 intervention for maintained functioning. EAM asks the additional value question at the same service and horizon.

Continued use costs `0.50 + 1.00 × a = 5.079707`. Replacement costs `3.00 + 0.35 × a − 1.20 × d = 3.567767`. Replacement saves 1.511940 in present cost within the admitted comparison. The completed result can therefore be a recommendation to replace, qualified by the supplied service, engineering, funding and timing conditions. It is not a work order or a hand-back result.

The comparison also gives a useful stop for inquiry. Holding the other inputs fixed, continued use and replacement are equal when the continued-use annual cost is 0.669861. An existing justified range of 0.95–1.05 does not reverse the recommendation, so a new cost investigation solely to decide between these options is unnecessary. A credible annual cost of 0.60 would reverse that economic choice; a credible result about that possibility could be useful if obtainable in time at a justified total burden. This is sensitivity, not a probability distribution or a blanket claim that further knowledge has no value. The EAM practitioner uses the specialist's engineering assessment of D's stated duty and the water-delivery mandate in the shared premises above to establish which policies remain eligible. The sensitivity calculation answers only the cost question.

If the operator asks only about present condition or the intervention needed to maintain the already selected use, the maintenance practitioner can answer by supplying the applicable condition account or intervention recommendation. The operator receives that bounded maintenance answer. When the question is instead which asset option offers better value over this horizon, the EAM practitioner supplies the additional comparison even though there is only one asset.



### EAM.Application:1.3 - When the complete policy is still missing

The D comparison above starts from complete, supported policies. When a new request instead supplies only an initial repair price, [EAM.8](#eam8---generate-maintenance-renewal-and-retirement-alternatives) constructs the policy before [EAM.9](#eam9---compare-asset-alternatives-and-reconcile-decisions-when-they-conflict) compares it. In its separate asset E case, initial work supports three years but the service is required for four; the further overhaul, its window and temporary service belong to the alternative. Omitting that work reverses the apparent cost preference while leaving year four unsupported.

[FIN.6](CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin6---value-capital-projects) supplies the dated financial account for the stated technical policy, and [FIN.7](CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin7---value-assets-and-the-corporation) supplies its ending valuation. Moving only the end of the explicit table to year two requires a value that represents the same later cash and ending premise; [EAM.8](#eam8---generate-maintenance-renewal-and-retirement-alternatives) shows that the whole present cost and preference remain unchanged. Ending the service at year two instead changes the required policy and uses actual exit consequences. A different supplied valuation must be reconciled to its changed assumptions before it can change the recommendation. If an observation later changes technical support or the ending premise, [EAM.13](#eam13---track-realized-outcomes-and-reconsider-asset-plans) returns the affected policy to [EAM.8](#eam8---generate-maintenance-renewal-and-retirement-alternatives) and the comparison. D's supplied five-year premises and the programme calculation below remain their own case.



## EAM.Application:2 - APP-EAM-02 - The same asset in a constrained programme

CityWater's funding board has allocated 8 for initial capital, a separate 0.60 for initial operating expenditure and 3 for annual operation. The infrastructure committee is authorized to select the asset programme within those allocations; changing an allocation requires a decision by the funding board. The operating plan separately supplies twelve available team/outage days before the wet season. These allocations, authorities and operating conditions are constructed case premises. No later funding is assumed in this base comparison. Each station needs exactly one of its two qualified options. For this small problem, enumerate all sixteen combinations; do not rank individual condition scores or savings ratios.

Codes below follow asset order A/B/C/D. Every row satisfies the initial and recurring operating allowances and the twelve-day bound; the base funding column identifies the remaining capital constraint. The service checks still require a non-overlapping schedule for the connected outages.

| Combination | Initial capital | Days | Total present cost | Base funding eligible? |
| --- | ---: | ---: | ---: | --- |
| `FRMR` | 11.5 | 11 | 13.025446 | capital exceeds 8 |
| `FFMR` | 10.0 | 10 | 13.080344 | capital exceeds 8 |
| `RRMR` | 13.0 | 12 | 13.199533 | capital exceeds 8 |
| `RFMR` | 11.5 | 11 | 13.254431 | capital exceeds 8 |
| `FRMK` | 8.5 | 9 | 14.537386 | capital exceeds 8 |
| `FFMK` | 7.0 | 8 | 14.592284 | yes |
| `RRMK` | 10.0 | 10 | 14.711473 | capital exceeds 8 |
| `RFMK` | 8.5 | 9 | 14.766371 | capital exceeds 8 |
| `FRLR` | 8.5 | 9 | 15.295240 | capital exceeds 8 |
| `FFLR` | 7.0 | 8 | 15.350138 | yes |
| `RRLR` | 10.0 | 10 | 15.469327 | capital exceeds 8 |
| `RFLR` | 8.5 | 9 | 15.524225 | capital exceeds 8 |
| `FRLK` | 5.5 | 7 | 16.807180 | yes |
| `FFLK` | 4.0 | 6 | 16.862078 | yes |
| `RRLK` | 7.0 | 8 | 16.981268 | yes |
| `RFLK` | 5.5 | 7 | 17.036166 | yes |

`FFMK` is the minimum-cost eligible combination: refurbish A and B, modify C and retain D under its supported policy. It uses 7 of capital, 0.50 of initial operating cash, 1.85 annually and eight team/outage days. Its total present cost is 14.592284. A feasible twelve-day calendar under these premises can place A on days 1–2, B on 3–4, C on 5–7 and D on 8, with four uncommitted days. Each restored station is available before another dependent station is removed. The uncommitted allowance is not permission to bypass a return condition or proof that all disturbances fit.

The individual D recommendation remains true under its assumptions, but replacing D while retaining both refurbishments and C modification needs 10 of capital and is infeasible at 8. `FFLR` frees C's capital through leased service and replaces D, but costs 15.350138 overall. Thus merely swapping in the individually preferred D option is not the portfolio answer. The unused 1 of capital is not an extra benefit or an instruction to spend it.

Three separate changed-condition branches show the decision's sensitivity:

- With the funding board's capital allocation raised to 10 and the other premises unchanged, `FFMR` becomes best: both refurbishments, C modification and D replacement, present cost 13.080344 and ten days. The authorized funding change precedes reliance on that feasible set; a desired budget increase is not available money.
- With only seven team/outage days and the original capital limit, `FRLK` becomes best among the supplied options: refurbish A, replace B, lease C's added service and continue D. It takes seven days, 5.5 capital and costs 16.807180. A cheaper eight-day combination does not fit merely because each job fits separately. Another qualified team or extended window would be another explicit alternative with its own full cost and service implications.
- If a new engineering finding invalidates D's continued-use policy, remove every `...K` combination. At the original limits, `FFLR` is then best, at 15.350138 and eight days. The supported response changes before any attempt to justify D continuation by its affordability. If the leased service were also unavailable, return the resulting unmet service/funding condition to the responsible decisions.

The EAM team submits its programme recommendation to the infrastructure committee. The finance practitioner supplies cost estimates and an affordability assessment against the funding board's allocations; those allocations set the spending limits. The infrastructure committee selects and authorizes an asset programme that fits those limits and the water-delivery mandate. MNT and operating authorities subsequently determine the permissions and conditions for protected work and resumption. The team can deliver its supported recommendation before the committee decides; the team reports an authorized programme only after that decision is supplied.



### EAM.Application:2.1 - When the demand basis changes

The original sixteen combinations use the supplied North wet-season requirement of 1,100 m³/h. Suppose a later, separately qualified demand account gives 1,250 for a period the asset choice must cover. [EAM.4](#eam4---assess-demand-and-service-need-for-asset-decisions) establishes its component basis, coincidence and status as a forecast or commitment; its Westbank example shows that construction with separate teaching inputs. [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence) then compares the new scenario with the 1,200 contribution supported by either current C option. The 50 m³/h gap means none of the sixteen existing combinations supplies that scenario. Re-ranking their costs cannot repair the missing service.

Return to [EAM.7](#eam7---generate-ways-to-supply-an-asset-dependent-service) for an additional supported contribution or a qualified demand-management alternative, then compare the resulting policies and combinations on the revised premises. A proposal to change the service obligation goes to its actual authority. The original programme calculation remains applicable to its original conditions. If later observations reveal the changed driver, [EAM.13](#eam13---track-realized-outcomes-and-reconsider-asset-plans) reopens this affected account and its option consequences.



### EAM.Application:2.2 - When a shared dependency changes recovery

A common dependency can require another option even when the normal-demand comparison passes. [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence)'s separate feeder example shows both units losing their contribution together, reserve exhaustion before full recovery, and an independent supply whose time to usable service changes the result. Its qualified recovery conditions become inputs to [EAM.7](#eam7---generate-ways-to-supply-an-asset-dependent-service)/.8's alternatives and [EAM.11](#eam11---time-asset-interventions-and-manage-dependencies)'s calendar. A favourable price or available team does not restore the missing service.

To apply that construction to CityWater, obtain the relevant dependency, deliverability, usable reserve and restoration account for its actual service boundaries. Compare the resulting options in [EAM.9](#eam9---compare-asset-alternatives-and-reconcile-decisions-when-they-conflict)/.10 and retain the relied-on recovery conditions in the recommendation. The original CityWater outage bounds remain useful for the situations they describe. If an observed restoration time or dependency changes, [EAM.13](#eam13---track-realized-outcomes-and-reconsider-asset-plans) returns to the affected capability, option and timing rather than treating the former programme as qualified for the new loss.



### EAM.Application:2.3 - When shared work changes the consequences

The sixteen rows above use their declared additive costs and whole-work times. They do not establish whether a different work arrangement could share a mobilization, require extra temporary service or change a later commitment. [EAM.10](#eam10---compare-engineered-asset-portfolio-combinations)'s separate P+Q/Z case shows why that question matters: one qualified shared mobilization makes the joint solution cost 3.8 against the alternative's 3.9, while two required visits make it cost 4.0.

For a proposed CityWater arrangement, [EAM.11](#eam11---time-asset-interventions-and-manage-dependencies) must establish its actual windows and whole work, and [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence) its service conditions. [EAM.10](#eam10---compare-engineered-asset-portfolio-combinations) then reconstructs that combination's consequences; [FIN.9](CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin9---compare-capital-investments-and-allocations) supplies the financial return if joint cash or dated funding must be developed. Recompute the affected rows rather than applying a discount to all sixteen. If the change also affects demand, recovery or a continuing policy, return that premise to [EAM.4](#eam4---assess-demand-and-service-need-for-asset-decisions), [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence) or EAM.8. The existing capital, time and D-qualification branches remain valid on their stated premises.



### EAM.Application:2.4 - What subsequent outcomes and practice questions would mean

The programme promises the qualified added service from C, continued supported use of D and the stated spending. Completion of the work alone establishes none of those whole-programme outcomes. [EAM.13](#eam13---track-realized-outcomes-and-reconsider-asset-plans) shows how an obtained variance changes a particular premise, without inferring a technical cause from cost alone.

The later practice examples are separately constructed continuations. [EAM.14](#eam14---decide-whether-and-how-to-change-the-asset-management-system) compares a small responsibility/information repair with a new application. [EAM.15](#eam15---decide-whether-and-how-to-change-engineering-asset-management-methods) compares a condition-priority rule with complete combination comparison and distinguishes a desk result from a trial in real decisions. [EAM.16](#eam16---deliberately-continue-and-change-engineering-asset-management-culture) examines teaching, later use and selection of the reusable practice with different evidence. An observed asset selection is not automatically selection of the Method that helped produce it.

## EAM.Application:End


# Engineering Asset Management Principles Framework Sources and Edition Notes

## EAM.Sources:1 - Professional and technical sources

| Source | Contribution used here | Applicable limit |
| --- | --- | --- |
| [GFMAM Asset Management Landscape, third edition, June 2024](https://gfmam.org/sites/default/files/2024-06/GFMAM_AM_Landscape_v3.0_English_2024.pdf) | Professional asset-management concerns, particularly value-oriented decisions, investment, lifecycle work and configuration. | A professional landscape does not validate this repertoire's effectiveness or prescribe its pattern boundaries. |
| [IAM, Asset Management — an Anatomy, version 4, July 2024](https://theiam.org/media/5615/iam-anatomy-version-4-final.pdf) | Proportionate appraisal of costs, risk, benefits and time; §7.5.6 supplies the service-loss and recovery comparison used in EAM.6. | EAM develops its own dependency and interval construction; the source does not qualify the case equipment or its recovery times. |
| [ISO/TC 251 public ISO 55001 account](https://committee.iso.org/sites/tc251/home/projects/published/iso-55001.html) and [ISO 55000:2024 — Asset management — Vocabulary, overview and principles, catalogue entry](https://www.iso.org/standard/83053.html) | The ISO/TC 251 account provides management-system context; the separate ISO 55000 entry identifies its vocabulary, overview and principles publication. | Public descriptions and catalogue metadata only; this is not a clause-by-clause application or a conformity or certification claim. |
| [NIST Handbook 135e2025, Life-Cycle Costing Manual for the Federal Energy Management Program](https://nvlpubs.nist.gov/nistpubs/hb/2025/NIST.HB.135e2025.pdf), chapters 4, 7 and 8 | Dated initial, recurring, replacement and ending consequences on a common period; competing alternatives and programme selection; sensitivity/break-even reasoning. | Federal rates, legal eligibility and financing rules do not govern the fictional utility. Its 3% real rate and values are constructed inputs. |
| [Water resources planning guideline, updated 16 June 2026](https://www.gov.uk/government/publications/water-resources-planning-guideline/water-resources-planning-guideline), sections 6.1 and 6.4.1–6.4.3 | [EAM.4](#eam4---assess-demand-and-service-need-for-asset-decisions) develops component reconciliation, driver changes and critical-period scenarios, with an unchanged-policy baseline distinguished from proposed measures. | The small construction and examples are EAM adaptations; specialist estimation, jurisdictional duties and the source's planning horizon retain their own conditions. |
| [NIST/SEMATECH e-Handbook, section 8.4.2.3](https://www.itl.nist.gov/div898/handbook/apr/section4/apr423.htm) | [EAM.5](#eam5---assess-asset-condition-and-performance)'s degradation-model comparator and its assumptions. | An established statistical method, not a pump-specific diagnosis, threshold or life qualification. |
| [US EPA, EPANET 2.2, hydraulic modeling capabilities](https://www.epa.gov/water-research/epanet) | [EAM.6](#eam6---assess-asset-capacity-resilience-and-interdependence) compares a sufficient capacity/duration bound with extended-period hydraulic analysis. | The software's capabilities supply no model or verified hydraulic result for CityWater. |
| [Magenta Book, updated 15 May 2026](https://www.gov.uk/government/publications/the-magenta-book/magenta-book-central-government-guidance-on-evaluation-html), chapter 2 impact-evaluation approach comparison | [EAM.13](#eam13---track-realized-outcomes-and-reconsider-asset-plans) distinguishes a sufficient plan update from an inquiry into attributable effects. | Method and evidence comparator; no actual outcome or government evaluation obligation is asserted for CityWater. |


These sources have different jobs. Professional coverage supports recognition of the problem; a technical Method supports a specific operation; actual observations and specialist judgements support a case result. The constructed applications are original teaching examples and are labelled as such. No single source is treated as the authority for all these claims.

The [Architectural Reference](#engineering-asset-management-principles-framework-architectural-reference) explains the connected language and the consequences of these sources for its use.

## EAM.Sources:End
