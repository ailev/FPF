# Economic Reasoning and Coordination Principles Framework

**DocID:** `ECO` within **FPF Library**.

> A pattern language for connecting different plans and knowledge with scarce means through calculation, exchange, commitments and economic arrangements.

- **Author:** Anatoly Levenchuk, with AI-assisted development and review
- **Version:** 24 October 2026
- **License:** © 2026 Anatoly Levenchuk. Original framework text: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Third-party material retains its own terms.

Start with the economic question your work needs answered. The Table of Contents locates individual Methods. The Readme shows how to use them together, and the Architectural Reference explains their contributions, prerequisites and limits. Use ECO and a Method number to cite a Method. The Parts group related Methods for reading.

This framework has its own publication in the [FPF Library DPF catalogue](https://github.com/ailev/FPF/tree/main/DPFs). Cite the author, title, version shown here and the relevant PatternID or Architectural Reference section.

# Table of Contents

## Public units

| Unit | Title | Use |
| --- | --- | --- |
| Readme | [Economic Reasoning and Coordination Principles Framework Readme](#economic-reasoning-and-coordination-principles-framework-readme) | Connect methods to form a service arrangement, coordinate a shared constraint or use an efficiency gain. |
| Architectural Reference | [Economic Reasoning and Coordination Principles Framework Architectural Reference](#economic-reasoning-and-coordination-principles-framework-architectural-reference) | Understand the connected methods, their rationale, sources and limits. |
| ECO.Reference:1 | [Problem frame - Make an economically workable contribution](#ecoreference1---problem-frame---make-an-economically-workable-contribution) |  |
| ECO.Reference:2 | [Problem and forces - Locally sound contributions can fail together](#ecoreference2---problem-and-forces---locally-sound-contributions-can-fail-together) |  |
| ECO.Reference:3 | [Solution - Connect calculation, exchange and economic arrangements](#ecoreference3---solution---connect-calculation-exchange-and-economic-arrangements) |  |
| ECO.Reference:3.1 | [Calculation rests on economic relationships](#ecoreference31---calculation-rests-on-economic-relationships) |  |
| ECO.Reference:3.2 | [Methods are enacted within a vertical](#ecoreference32---methods-are-enacted-within-a-vertical) |  |
| ECO.Reference:4 | [Archetypal grounding - From a proposed service to a viable arrangement](#ecoreference4---archetypal-grounding---from-a-proposed-service-to-a-viable-arrangement) |  |
| ECO.Reference:5 | [Consequences and limits](#ecoreference5---consequences-and-limits) |  |
| ECO.Reference:6 | [Common failures and useful returns](#ecoreference6---common-failures-and-useful-returns) |  |
| ECO.Reference:7 | [Architectural Rationale](#ecoreference7---architectural-rationale) |  |
| ECO.Reference:8 | [Source use and currentness](#ecoreference8---source-use-and-currentness) |  |
| ECO.Reference:9 | [External contributions and entry](#ecoreference9---external-contributions-and-entry) |  |

## Part I - Calculation and discovery

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [ECO.1 - Recover the Basis for an Economic Calculation](#eco1---recover-the-basis-for-an-economic-calculation) | Stable | prices; weights; exchange; opportunity cost. Which resources, terms and alternatives enter this comparison? | Existing MA/FIN accounts; ECO.3 if an exchange remains missing. |
| 2 | [ECO.2 - Reconsider Resource Use in Response to Price Signals](#eco2---reconsider-resource-use-in-response-to-price-signals) | Stable | price change; substitution; marginal use. What response do the available terms support? | ECO.1 for disputed prices; functional and operating feasibility. |
| 3 | [ECO.3 - Discover an Exchange between Different Plans](#eco3---discover-an-exchange-between-different-plans) | Stable | entrepreneurial discovery; different plans; exchange. Which proposed exchange can the parties carry out? | ECO.1 for calculation; ECO.4 for complementary commitments. |

## Part II - Commitments and adaptation

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [ECO.4 - Form Resource Commitments for an Uncertain Venture](#eco4---form-resource-commitments-for-an-uncertain-venture) | Stable | resource mobilization; uncertainty; complementary commitments. What makes a first action or joint commitment attainable? | A proposed venture; ECO.3 when a new exchange must be found; OPS resources; FIN financing; EXD where understanding is missing. |
| 2 | [ECO.5 - Choose Exchange Terms for Private Information and Effort](#eco5---choose-exchange-terms-for-private-information-and-effort) | Stable | private information; effort; incentives; participation. Which terms make the contribution worthwhile and feasible? | Proposed exchange; ECO.4 commitments or ECO.6 dependence where relevant. |
| 3 | [ECO.6 - Arrange Adaptation in a Dependent Trading Relationship](#eco6---arrange-adaptation-in-a-dependent-trading-relationship) | Stable | dependence; dedicated investment; adaptation; outside option. How will the parties handle a consequential change? | ECO.1 grounds; EAM/FIN consequences; OCE/CGOV for a selected organization change. |

## Part III - Shared and extended coordination

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [ECO.7 - Coordinate Use and Renewal of a Shared Resource](#eco7---coordinate-use-and-renewal-of-a-shared-resource) | Stable | shared resource; renewal; access; collective rules. Can separate uses and contributions preserve the resource? | Physical and operating resource account; ECO.8 or ECO.9 when wider coordination or a change of rule is needed. |
| 2 | [ECO.8 - Join Direct Cooperation with a Wider Economic Order](#eco8---join-direct-cooperation-with-a-wider-economic-order) | Stable | direct cooperation; extended order; Method vertical. Which coordination mechanism fits each relation? | The actual cooperation and exchange relations; ECO.7 for a shared constraint. |
| 3 | [ECO.9 - Decide Whether and How to Change Economic Rules through Their Working Practices](#eco9---decide-whether-and-how-to-change-economic-rules-through-their-working-practices) | Stable | institutional change; cultural evolution; capability. Should this rule be retained or changed, and what working contribution is needed? | Current practice and a question about retaining or changing it; C.36 cultural continuation; HCD/MDPE capability. |

## Part IV - Efficiency and demand

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [ECO.10 - Trace Efficiency Savings through Demand Responses (Rebound Effects)](#eco10---trace-efficiency-savings-through-demand-responses-rebound-effects) | Stable | Jevons; rebound; efficiency; demand; counterfactual. Does a unit saving change total resource use? | Unit-resource relation and counterfactual; ECO.2/.3 for changed prices and uses. |

# Economic Reasoning and Coordination Principles Framework Readme

## Practical entries

Use these Methods to examine how a plan can work economically. A price may be open to question, a technically feasible service may lack a customer commitment, or separate uses may exceed a shared supply. A lower resource cost per unit can also change demand. Start with the relation that matters to the result you need.

The following cases connect Methods to address larger questions. For a question one Method can answer, use the Table of Contents.

Use what you know about the relevant plans and resources to answer the economic question. If you obtain help from a practitioner or agent, explain the question and its intended use and ask for an answer in the language of your work. The result may be an explanation, feasibility assessment or recommendation. State which conclusions depend on assumptions.

### ECO-VENTURE - Turn a useful idea into a feasible service arrangement

- **Situation:** A proposed service needs a customer's order, a supplier's dedicated equipment and finance. Each party finds a different part uncertain.
- **Question:** Which combination of exchange terms, contributions and commitments can make the service attainable?
- **First useful result or blocker:** A finding about whether a first action or set of commitments is attainable, or a specific condition that remains open. If the assignment includes delivering the service, establish that the parties can supply it and carry out the required work.
- **Start with:** Use the existing contributions that fit. The following steps address questions that may remain.

1. Use [ECO.3](#eco3---discover-an-exchange-between-different-plans) if the exchange that could connect the parties’ plans still needs to be constructed. Establish a customer order from commitment to the terms. Check that the operating contribution needed to use an offered asset is available.
2. Use [ECO.1](#eco1---recover-the-basis-for-an-economic-calculation) for a disputed price or alternative-use assumption. Existing MA, FIN and OPS results can already answer the resource and financial questions.
3. Use [ECO.4](#eco4---form-resource-commitments-for-an-uncertain-venture) if the commitments depend on one another. Use EXD when a participant lacks an explanation needed to judge the proposal. A participant who understands and declines it may need different terms to participate, or the venture may need another counterparty.
4. Use [ECO.5](#eco5---choose-exchange-terms-for-private-information-and-effort) if private quality or later action makes the proposed terms unreliable. Use [ECO.6](#eco6---arrange-adaptation-in-a-dependent-trading-relationship) if dedicated investment makes adaptation or exit difficult.
5. If the undertaking requires implementation, carry the selected combination into the applicable agreements and operating work. Use [ECO.8](#eco8---join-direct-cooperation-with-a-wider-economic-order) when a rule for internal cooperation has been applied to an external supplier whose terms differ.

Suppose a supplier needs tooling that will lose most of its value if the customer cancels. Compare an adequate volume commitment, staged investment and a less dependent standard process where these are plausible. If the standard process gives the required result at an acceptable total cost, the firm can avoid dedicated tooling. If it cannot, assess who can decide on later adaptations, on what terms and with what contribution.

Now suppose a reusable interface and another qualified supplier become available. Reassess which risks and safeguards still matter and whether an acquisition proposal still serves a purpose. If the only remaining task is scheduling committed capacity, use the relevant OPS Method.

- **Stop or return:** A finding about the missing commitment can answer a diagnostic question. Use a sufficient existing agreement directly. For a claim that the service has been delivered, establish that the promised work reached its recipient under the agreed conditions.

### ECO-SHARED - Preserve access under a changed shared constraint

- **Situation:** Several local groups have workable allocations, but their combined use now threatens the resource or excludes other legitimate users.
- **Question:** Which shared constraint and coordination relation must their local arrangements retain?
- **First useful result or blocker:** A supported finding about the shared constraint, a feasible allocation with a way to adopt or adapt it, or an incompatibility the current arrangements leave unresolved.
- **Start with:** Use [ECO.7](#eco7---coordinate-use-and-renewal-of-a-shared-resource) to relate withdrawal, renewal and access. Use [ECO.8](#eco8---join-direct-cooperation-with-a-wider-economic-order) when local arrangements need a wider coordination relation. Use [ECO.9](#eco9---decide-whether-and-how-to-change-economic-rules-through-their-working-practices) if the question is whether to preserve, modify or replace a rule, taking account of the practices and capabilities each option requires.

For example, lower canal inflow can make a set of daily allowances infeasible even when every group followed its old limit. Compare the combined withdrawals with the available flow. That finding can answer a question about feasibility. If the task requires a workable new allocation, identify how the affected parties can adopt and adapt it.

Now suppose the water supply recovers but some users cannot operate the new digital access procedure. The water calculation still answers its physical question. Investigate the access problem and, if asked to restore access, assess assistance, a different procedure or the capability the users need. HCD and MDPE can help develop the relevant capability or practice. Publishing the digital rule establishes neither access nor ability to use it.

- **Stop or return:** Give the supported answer about the allocation or rule. If it remains limited by physical supply, access or capability, identify the missing contribution and obtain it when the task requires it and it is available.

### ECO-EFFICIENCY - Decide what a unit saving should change

- **Situation:** A process needs less energy or money per useful result, making several continuations possible.
- **Question:** How does a unit saving affect total use? If a choice is needed, should it reduce burden, expand valuable activity, retain capacity or help meet a cap?
- **First useful result or blocker:** A conditional comparison of total resource use. When a break-even output exists, it identifies where the improved process uses as much resource as the comparison case without the improvement.
- **Start with:** Use [ECO.10](#eco10---trace-efficiency-savings-through-demand-responses-rebound-effects) to separate the technical saving from changes in demand and calculate a threshold when it matters. Use [ECO.2](#eco2---reconsider-resource-use-in-response-to-price-signals) for a resource response to changed prices and [ECO.3](#eco3---discover-an-exchange-between-different-plans) when the released means could support another exchange. Use [ECO.7](#eco7---coordinate-use-and-renewal-of-a-shared-resource) or [ECO.9](#eco9---decide-whether-and-how-to-change-economic-rules-through-their-working-practices) when shared limits or their rules matter.

If energy per unit falls by half, twice the former output uses the same energy within a fixed boundary. Higher output is then possible on this energy account. Whether it can be produced and will be demanded depends on other constraints, value and the new costs of use. Compare attainable uses when the question calls for a choice.

For a resource cap, keep the aggregate limit in the operating plan. For useful expansion, assess the value of the additional output alongside its resource and financial costs. Higher total use may be acceptable for that purpose. Select the purpose on its own grounds.

- **Stop or return:** Report the total-use comparison and the assumptions on which it rests. If the result is to inform a choice, identify the feasible alternatives it distinguishes. Reconsider the affected conclusion when the counterfactual, demand response or receiving purpose changes.

## Using the whole language

Start with the unresolved question and use applicable results already available. If a premise changes, reconsider the contribution that depends on it. The Architectural Reference explains the economic relations, sources and limits. Each Method includes instructions and examples.

Use Management Methods for financial, operating and organizational work, Explanation Design (EXD) for a needed explanation and Human Capability Engineering when a person needs to learn an operation. Core provides general development Methods. Use the [Foundational Thinking DPF Suite](https://github.com/ailev/FPF/blob/main/DPFs/Foundational%20Thinking%20DPF%20Suite/README.md) when mathematical, physical or computational modeling is needed.

# Economic Reasoning and Coordination Principles Framework Architectural Reference

## ECO.Reference:1 - Problem frame - Make an economically workable contribution

Economic reasoning asks how different plans, knowledge, purposes and rights can be connected with scarce means. A technically feasible construction can remain unavailable because its inputs cannot be obtained, its participants will not accept the terms or its effects undermine the arrangement on which it depends.

Use these Methods to examine economic calculation, exchange, resource commitments, adaptation, shared resources and the rules that coordinate their use. They also address what happens to feasible activity and total demand after an efficiency improvement.

Identify the intended result, relevant parties and scarce resources. Use qualified financial, technical, legal or statistical contributions when the economic conclusion depends on them. A practitioner can supply a contribution within their competence or obtain it from another source. Keep its conditions with the result.

## ECO.Reference:2 - Problem and forces - Locally sound contributions can fail together

A calculation can be correct while the quoted resource is unavailable. A working prototype can lack a customer order. An agreement between buyer and supplier can impose costs on other users of a shared resource. A change of flow can defeat a previously feasible allocation. A more efficient process can use more resources in total if output expands sufficiently.

To answer these questions, connect monetary comparisons with the formation of alternatives, access to resources and coordination under actual rules. Purposes help explain why participants act. Prices, commitments, rules and the work undertaken show how their different plans can fit together or fail.

Use formal models or qualitative reasoning as the question requires. A calculation establishes what follows from its assumptions. To apply it to actual people, organizations or markets, establish the relevant evidence and conditions. Use probabilities supported for that use, or show what follows in each case when the probabilities are open.

Further inquiry costs time and resources and may displace other work. Use C.11.DUA to compare investigating with using the available basis, giving a bounded answer, changing an action or stopping.

## ECO.Reference:3 - Solution - Connect calculation, exchange and economic arrangements

The ten Methods are grouped by the economic contributions they provide. Start with the group that addresses the question at hand.

| Group | Contribution | Connection to further work |
| --- | --- | --- |
| Calculation and discovery: ECO.1–.3 | Establish what a comparison means, respond to relevant prices or construct a possible exchange. | Compare a newly feasible alternative. When terms change, establish whether the earlier result still holds or a different proposal is needed. |
| Commitments and adaptation: ECO.4–.6 | Establish which commitments can be made together, assess incentives under private information or arrange adaptation when parties depend on one another. | Use the result to assess the venture or, where selected, to form an agreement, conduct operating work or change the organization. |
| Shared and extended coordination: ECO.7–.9 | Relate use to renewal, connect direct cooperation with wider coordination and assess or change the rule through the practices that carry it. | Check the physical limits, affected interests and capabilities the arrangement needs. |
| Efficiency and demand: ECO.10 | Follow a unit saving through changes in feasible use and demand. | Return conditional total effects to the purpose and existing comparison or portfolio methods. |

A proposal, calculation, agreement and delivered service each answer a different question. Use the evidence for the result being claimed. For example, a signed volume commitment can support a planning calculation before the service has been delivered. The cases in this book are constructed to show how the reasoning works.

### ECO.Reference:3.1 - Calculation rests on economic relationships

Mises’s calculation argument asks what makes unlike productive means comparable across exchanges. A solver can find an optimum for the objectives, prices and feasible operations it receives. To establish what that result means for the parties, use ECO.1 when a material input or its economic basis is open to question.

Use a monetary comparison for the participant’s stated purpose. Identify alternative uses of the resources and consequences of the options that the monetary account leaves out. The comparison need not measure everyone’s welfare. If a market price is missing, a physical comparison or a comparison against the purpose may still be possible. Use the relevant MA and FIN Methods for accounting and financial calculations.

Hayek explains why a participant can adjust to a price change while the cause of the price change is still open. Use ECO.2 to examine the local response. Use ECO.3 to develop a new exchange if the available alternatives do not meet the parties’ plans.

### ECO.Reference:3.2 - Methods are enacted within a vertical

A service developer checking a supplier’s delivery condition can be comparing supply routes and constructing a feasible service arrangement through the same action. The larger service requirement determines which delivery condition matters. The ability to establish that condition limits what the larger development effort can conclude.

Suppose a manager can compute a financial total but cannot establish whether a number is an internal allocation credit or an obtainable price. The arithmetic is usable under the stated inputs. Before relying on the total for a supply choice, establish what the number means, obtain a qualified interpretation or change that part of the comparison. If its meaning remains open, report the limit. Learning to make the distinction is a further option if the manager needs it.

A commitment can connect the supplier’s manufacturing work with the buyer’s plan. To treat manufacturing as a constituent of the buyer’s reasoning method would require another relationship. Trace separately the flows of resources, contract dependencies, organizational assignments, constituent work and transmission of a practice.

Allocate the work according to capability, access and authority. A practitioner or service may perform the whole analysis, or several participants may supply parts. A model can calculate an offer while acceptance belongs to a party with authority to commit resources. The arrangements must make the relevant capabilities, resources and results available where the work needs them.

## ECO.Reference:4 - Archetypal grounding - From a proposed service to a viable arrangement

Suppose a firm proposes a monitoring service. A customer has a use for it, a supplier can prepare equipment and a funder can supply finance. The supplier needs dedicated tooling, the customer may cancel early and the funder requires an order. The technical and financial accounts leave open how the parties can meet these conditions together.

Use [ECO.3](#eco3---discover-an-exchange-between-different-plans) to identify what each party can contribute and which plans the exchange would serve. Use [ECO.1](#eco1---recover-the-basis-for-an-economic-calculation) to examine prices and attainable alternatives, and [ECO.4](#eco4---form-resource-commitments-for-an-uncertain-venture) to identify what can be done first or which commitments can be made together. A small demonstration can answer a technical question. Whether the customer can pay requires financial grounds.

Use [ECO.5](#eco5---choose-exchange-terms-for-private-information-and-effort) to assess whether the proposed terms make the required quality and effort worthwhile for those providing them. With [ECO.6](#eco6---arrange-adaptation-in-a-dependent-trading-relationship), compare protection for dedicated tooling and a less dependent standard process. Include an organizational alternative if it offers a credible response. Use the relevant MA, FIN, OPS and EAM results in the comparison.

The standard process may be preferable if it gives the required result at an acceptable cost with less dependence. If it cannot meet the requirement, the dedicated arrangement may remain preferable under stated conditions. If nobody can make the next contribution at acceptable exposure, identify the failed condition. Develop a different proposal if the task calls for one.

Reusable tooling and interchangeable suppliers change the parties’ dependence. Recheck the affected conclusion and use the earlier calculations where their costs, quantities and terms still hold. Reorganization requires its own grounds.

## ECO.Reference:5 - Consequences and limits

Participants can assess and construct economic arrangements using knowledge and authority distributed among them. The comparison may also establish that none of the available arrangements resolves a particular incompatibility.

Use the ten Methods for the economic relations described here. For a question about macroeconomic forecasts, monetary or credit theory, taxation, competition law, auction design or welfare analysis beyond that scope, obtain the relevant specialist contribution.

Identify whose purpose an arrangement serves and who bears its burdens. Use the relevant rights, resources and evidence to assess whether the promised outcome is attainable. A decision establishes what was decided, including a refusal or permission. Establish any commitment from its applicable terms and delivery from the work performed.

## ECO.Reference:6 - Common failures and useful returns

| Failure in work | Contribution to recover |
| --- | --- |
| A model’s optimum cannot be attained at the assumed prices. | Use ECO.1 to establish which prices and resources are available and what the calculation supports under those conditions. |
| Further explanation has produced no commitment. | Use ECO.4 to distinguish a need for understanding from disagreement or unavailable means. Use ECO.3 if a different proposal is needed. |
| An inexpensive offer leaves the supplier exposed after investing in dedicated assets. | Use ECO.6 to examine the exposure, attainable outside options and proposed arrangements for later adaptation. |
| Allocations fit separately but violate the common constraint when combined. | Use ECO.7 to establish the joint physical and access conditions. Use ECO.8 if a wider coordination relation matters. |
| A copied rule lacks the capability or practice that made it work elsewhere. | Use ECO.9 to establish which contribution is missing and how it could be maintained or transmitted if the rule is to be used. |
| Lower resource use per unit is reported as a total saving. | Use ECO.10 to compare total use against the relevant counterfactual, including changes in demand within the comparison’s scope. |

Use these returns when the failure occurs.

## ECO.Reference:7 - Architectural Rationale

These contributions can fail independently. Ranking existing alternatives leaves open whether a new exchange can be formed. A party may understand a venture and still decline it or lack the necessary means. Acceptable initial incentives can leave a costly later adaptation. Shared-resource arrangements and economic rules can also affect people outside the original transaction.

Use results from Corporate Finance, Management Accounting, Financial Domain Modeling, Operations Management, Organization Change Engineering and Corporate Governance when the economic question needs them. Economic reasoning can also inform development and strategy when exchange, resource use or coordination affects the proposed direction.

Use FPF for agency, composition of Methods, choice, uncertainty and cultural evolution. Use the relevant Foundational Thinking Methods for mathematical, physical or computational modeling. Here the contribution is the economic mechanism that connects those results to the parties’ plans and resources.

## ECO.Reference:8 - Source use and currentness

The Methods draw on historical accounts of economic mechanisms, disagreements among those accounts and later research on particular questions. Use a source for the mechanism it explains and within the conditions its evidence supports.

| Source line | Adopted contribution and limit |
| --- | --- |
| Mises and Hayek | Economic calculation, distributed knowledge and the coexistence of local and extended orders. These do not become blanket verdicts on every public service or a fixed hierarchy of methods. |
| Huerta de Soto | Discovery of opportunities among different plans and the temporal, heterogeneous character of productive means. Actual discovery and provision retain resource costs. |
| Williamson | Comparison of feasible ways to adapt under dependence; no automatic preference for integration. |
| Akerlof and Holmström | Private information, private action, participation and incentive consequences; model assumptions remain explicit. |
| Ostrom and later polycentric-governance research | Shared-resource arrangements, interacting centres and change over time; no guarantee from the label “polycentric”. |
| Foss, Klein and Murtinu | Resource mobilization and differences in understanding novel ventures; conceptual accounts do not guarantee stakeholder agreement. |
| Rebound research, including recent AI work | Demand and wider-use responses to efficiency, with explicit causal and measurement limits. |

Each Method links the sources that inform its instructions. The rebound discussion includes the [FAccT 2025 analysis](https://facctconference.org/static/docs/facct2025-206archivalpdfs/facct2025-final37-acmpaginated.pdf). Hayek addresses different local and wider orders in [The Fatal Conceit, pp. 18–19](https://www.mrsmuellersworld.com/uploads/1/3/0/5/13054185/fatal_conceit_by_hayek.pdf). Use a contribution if it still answers the question under the relevant conditions. Compare later work when it changes a premise, explanation or limit on use.

Reconsider a Method when new evidence changes its explanation, a relevant institution or technology changes, an external method no longer supplies the same contribution, or use exposes a missing operation. Keep the parts of the reasoning whose grounds still hold.

## ECO.Reference:9 - External contributions and entry

This DPF relies on the general meanings and selected methods in [FPF Core](https://github.com/ailev/FPF/blob/main/FPF-Spec.md), including B.1.5 for constituent and encompassing methods, C.11 for proportionate inquiry and C.36 for cultural continuation. The dependence is from ECO to Core.

Use the Management Suite for the cited financial, accounting, operating, asset, organizational or corporate work. Explanation Design (EXD) addresses explanation. Human Capability Development (HCD), in the Human Capability Engineering Suite, addresses human learning. Use existing qualified contributions directly. Obtain or develop a missing result when the economic question depends on it.

Use the [Foundational Thinking DPF Suite](https://github.com/ailev/FPF/blob/main/DPFs/Foundational%20Thinking%20DPF%20Suite/README.md) to construct or interpret a mathematical, physical or computational model when that contribution is needed.

When a supplying Method changes, reconsider the economic conclusion that depends on the changed operation or condition. Use the still-applicable results directly. The Table of Contents and the connected examples in the Readme provide entry points. Stop when the requested result is supported. For the starting question of an economic calculation, see [the earlier ECO.1:4.1](https://github.com/ailev/FPF/blob/1e57ccda08ebbb9d49b7b2190bc2740b72075a13/DPFs/ECONOMIC-REASONING-AND-COORDINATION-PRINCIPLES-FRAMEWORK.md#eco141---recover-the-decision-and-the-consequential-numbers) and [the current ECO.1:4.1](#eco141---identify-the-economic-question-and-the-quantities-that-matter).

## ECO.Reference:End

# Part I - Calculation and discovery

## ECO.1 - Recover the Basis for an Economic Calculation

> **Type:** Method pattern
> **Status:** Stable

### ECO.1:1 - Problem frame

Use this Method when the economic meaning of a calculation is unclear. A price or weight may refer to a real offer, a past exchange, a displaced use or an assumption in a model. Start with a quantity that matters to the question. Establish what it represents, under what conditions, and what comparison follows. If a required input remains open, give the result conditionally.

Use a quotation or resource account directly when it covers the specification, time and access relevant to the question.

### ECO.1:2 - Problem

An optimizer can solve a model whose numbers have different economic meanings. An internal transfer price may implement an allocation policy, an old purchase price can record a past exchange, and a shadow price measures a marginal trade-off in the specified model. Substituting one for another can make an unavailable alternative look attainable.

State the exchange conditions and rights under which a monetary consequence follows. Physical feasibility and the effects on different participants can require separate accounts. To compare satisfaction across people, identify grounds for that comparison.

### ECO.1:3 - Forces

Use enough detail to distinguish the alternatives open to the participants. A price can coordinate unlike resources while each party knows only part of the circumstances. A new arrangement may have no established market price. A conditional calculation or a comparison of physical outcomes can still inform the work.

### ECO.1:4 - Solution

#### ECO.1:4.1 - Identify the economic question and the quantities that matter

Identify what the calculation is meant to establish, whose use or choice it concerns and the period in which the resources matter. Distinguish alternatives that give different results or carry different obligations. Reuse a suitable resource or cash-flow account from MA or FIN.

Trace the quantities whose interpretation matters to the answer. For each, establish whether it denotes an offer, a completed transaction, a budget allocation, an anticipated exchange, a forgone use or a model weight. Identify relevant quantity, quality, location, timing and access. To apply “steel at 500,” determine the unit, terms and supply to which 500 refers.

#### ECO.1:4.2 - Connect the comparison to feasible exchange and use

For an offer, establish who can obtain which supply and under what terms. A nonmatching specification or missed delivery window can exclude the offer for this plan. Use an accepted commitment to establish what the parties have agreed and delivery evidence to establish what reached the recipient.

For a controlled resource, identify what alternative use would be displaced. Historical acquisition cost and the current forgone result can differ. For a new arrangement, use a comparable offer when its differences can be accounted for. Otherwise give a conditional value or compare physical outcomes against the participants’ purposes.

Keep model weights with the objective and constraints that define them. A shadow price can show the marginal contribution of relaxing a specified constraint. To claim someone can buy the resource at that price, establish the available offer and their right to use it.

#### ECO.1:4.3 - Return the comparison that the grounds support

Use the supported quantities and time conditions in the accounting or financial calculation where one is needed. State important consequences outside the monetary account, such as access for an affected community. With several criteria the evidence may leave alternatives incomparable.

If a missing price matters, identify what can already be established from a range, physical limits or the intended use. A matching offer or a new exchange under ECO.3 may resolve a remaining question. Seek it when the likely gain warrants the work. Stop when the evidence supports the requested finding, comparison or choice, including a conditional answer where appropriate.

### ECO.1:5 - Archetypal Grounding

#### ECO.1:5.1 - A cheap plan priced in internal credits

Suppose the repair depot can buy a compatible part for €90 delivered this week. Its spreadsheet prices an internal job at 40 machine credits plus €30 for material. Credits allocate booked machine time. They do not buy more machine time, and the machine has no slot this week. Treating a credit as one euro therefore leaves the apparent €70 plan unsupported.

A nearby provider offers the machining this week for €65 with €30 of depot material. If fit and warranty are equivalent, the two available routes cost €95 and €90. If no matching machining offer can be found, the internal job still lacks a machine slot. Recomputing its allocation does not supply one.

The 40 credits can still be used for their scheduling purpose. Use euro terms for the monetary comparison and capacity evidence for this week’s availability.

#### ECO.1:5.2 - A choice without a market quotation

Suppose a community can repair either of two paths with the same available volunteer time but has no defensible money value for the two improvements. It can compare access needs and the repairs each path allows. That comparison can support a choice. A financial-return claim would require a basis for valuing the outcomes in money.

#### ECO.1:5.3 - A useful marginal value inside a model

A workshop has ten usable machine-hours and demand for up to twelve identical one-hour jobs. Each completed job contributes €30 after the other relevant variable costs; the remaining inputs and commitments permit any of these jobs. The model's best contribution rises from €300 at ten hours to €330 at eleven and €360 at twelve. A thirteenth hour adds nothing under that demand limit.

Each of the next two usable hours adds €30 in this model. If a matching hour is available at €20, the added job contributes €10 after that purchase. The model does not supply an hour or an operator. Keep the conditional comparison where that answers the question. Recalculate the affected margin if demand, job mix or a required complement changes.

### ECO.1:6 - Bias-Annotation

A convenient number can be mistaken for the exchange or constraint it represents. Conversely, a disputed input need not defeat the rest of the calculation. Preserve the supported arithmetic and correct the claim about what the number means.

### ECO.1:7 - Conformance Checklist

What do the consequential quantities mean and when do they apply? If the question concerns availability, identify who can obtain the resource, the conditions under which it is attainable or the grounds for finding it unavailable. Does the comparison preserve alternative uses, obligations and important unpriced consequences? Return the finding or choice the evidence supports, identifying any unresolved exchange or physical constraint.

### ECO.1:8 - Common Anti-Patterns and How to Avoid Them

- **A computed price is treated as an offer.** Establish what the number means in the model. If supply is claimed, establish what someone can obtain on those terms.
- **An unpriced consequence is set to zero.** Keep it as a separate decision consideration or a stated constraint.
- **No complete price system, therefore no action.** Use the comparison that the available physical, contractual and purpose-based grounds already support.

### ECO.1:9 - Consequences

The comparison may give a supported ranking, a conditional one or a finding that an apparently cheap option is unavailable. Any of these can answer the question within its scope.

### ECO.1:10 - Architectural Rationale

An economic comparison uses both a calculation and a basis for interpreting its inputs. Keep the valid mathematical or accounting result when an exchange condition is missing. A common measure of social value requires grounds beyond an ordinary monetary calculation.

### ECO.1:11 - SoTA-Echoing

[Mises, Economic Calculation, §2](https://mises.org/online-book/economic-calculation-socialist-commonwealth/2-nature-economic-calculation) is the historical source for comparing heterogeneous productive means through exchange and for the limits of monetary calculation outside those relations. We adapt that question to the comparison at hand. Physical and purpose-based grounds can still support a choice when market prices are unavailable.

Optimization with assumed weights gives a conditional planning result. To use it for an economic claim about a real participant, check the meaning and applicability of those weights. Reconsider the affected comparison when access, exchange terms, alternatives or the intended use change.

### ECO.1:12 - Relations

Use MA.1 for a resource-and-cost account and FIN.6 for investment comparison with supported cash flows. Use ECO.1 to establish a disputed input or a condition of exchange. Use ECO.2 when prices change and ECO.3 when a new exchange is needed. C.11.DUA helps assess the value and cost of resolving a remaining uncertainty.

### ECO.1:End

## ECO.2 - Reconsider Resource Use in Response to Price Signals

> **Type:** Method pattern
> **Status:** Stable

### ECO.2:1 - Problem frame

Use this Method to establish what a changed price or offer means for the use, substitution or supply of a resource. Identify which exchange has changed and whether the terms apply to the work in question. When the task calls for a response, compare feasible adjustments with continuing the present plan. Report the grounds for a change or for keeping the plan.

Investigate why the market changed when that explanation is requested or would improve the response enough to justify the effort. Apply an adequate operating rule directly to a routine purchase it already covers.

### ECO.2:2 - Problem

Stale internal figures can hide a newly costly input. A new price for a different grade, quantity or delivery date can be irrelevant to the present work. Establish whether the price applies. A supported substitution can proceed while the wider cause is still unknown.

### ECO.2:3 - Forces

A price can convey information beyond one participant’s knowledge while omitting conditions important to its use. An inexpensive reversible adjustment and an irreversible investment need different grounds. Access and service obligations may exclude the cheapest purchase.

### ECO.2:4 - Solution

#### ECO.2:4.1 - Establish the changed exchange

Compare unit, specification, quantity, time, location, payment and access. Identify what changed and whether existing obligations fix the terms for this work. A change in delivery or service can matter even when the quoted amount stays the same.

Establish the terms for the next unit the plan could use. A bulk offer might exceed the storage available. The price paid for earlier units may differ from the price now attainable. Use ECO.1 when the meaning of an input remains in question.

#### ECO.2:4.2 - Construct feasible responses

When a response is needed, consider what changes the work permits. It may be possible to reduce use per result, substitute an input, change timing or output, increase supply or maintain the present use.

For each proposed response, establish the contributions it requires. A substitute may need another tool, skill, inspection or delivery arrangement. To use a different packaging insert, for example, establish whether it protects the product during handling. When this engineering result is missing, use SYSE.9 to obtain and apply it. Use OPS.14 to compare operating alternatives and transition costs, MA.1 for a missing resource account and FIN.6 for an investment comparison if a longer commitment is involved.

Compare the attainable net effects over the relevant period, including transition and forgone uses. Retain differences in performance and affected interests alongside the monetary comparison.

#### ECO.2:4.3 - Match the response to what remains unknown

For a small reversible change, an applicable offer and a sufficient functional account may settle the question. For a long commitment, identify whether uncertainty about persistence, access or substitution could change the comparison or the grounds for relying on it. Seek further information when it is worth the cost, or give the conditional plan the evidence supports.

A price may rise because of supply loss, demand growth, altered quality, taxes or market power. If the question concerns the cause, examine which explanations the evidence supports. If it concerns the response, applicable terms can already justify reducing use or substituting. When proposing or selecting an action, state which conditions support it and what change would call for reconsideration.

### ECO.2:5 - Archetypal Grounding

#### ECO.2:5.1 - A substitute becomes worthwhile

Suppose two packaging inserts meet the same performance requirements and differ only in the stated costs. The current insert uses two units at €3 each, so it costs €6. The other uses 1.5 units at €4 each, plus €0.50 handling, for €6.50 per package.

A matching offer raises the first material to €4 per unit. The current insert now costs €8. The substitute saves €1.50 per package before the €150 changeover. For a confirmed order of 200 packages that gives €300 gross and €150 net saving. Under these terms a practitioner with the necessary authority can select the substitute while the market cause remains open.

If 50 packages remain before a contracted cheaper delivery, the €75 gross saving would leave the substitute €75 more expensive after changeover. At 100 packages the €150 gross saving covers the €150 changeover exactly. Under the stated assumptions the monetary costs then tie, so another consequence can matter. If functional qualification is missing, include its cost, timing and outcome in the comparison.

#### ECO.2:5.2 - A price has a different scope

Suppose the electricity contract fixes the price for today’s shift. A spike in tomorrow’s spot price leaves today’s contracted payment unchanged. It can change the opportunity to sell stored energy or the terms of future production. Establish the relevant exchange before recommending a schedule change.

### ECO.2:6 - Bias-Annotation

A newly published price may not apply to the participant’s work. A preferred substitute may have a transition cost that its quoted price omits. Include the present arrangement where it is still feasible and identify the conditions that support each compared option.

### ECO.2:7 - Conformance Checklist

Which terms changed, and do they apply to the exchange in question? For a proposed response, are its complements and obligations feasible? State what the evidence establishes about the price, the response or its cause, according to the question. Identify the conditions that matter to any proposed commitment.

### ECO.2:8 - Common Anti-Patterns and How to Avoid Them

- **Every price movement triggers a market investigation.** If the question concerns an operating response, examine what the applicable terms already support. Investigate the cause when the task or remaining uncertainty requires it.
- **A cheap input is treated as a cheap result.** Carry substitution through performance, complementary work and transition.
- **Internal historic prices hide a changed external opportunity.** Recalculate the consequential next use rather than replacing every accounting number.

### ECO.2:9 - Consequences

Participants can adapt resource use to changes elsewhere using local knowledge and applicable terms. Those terms can also support retaining the current plan. To assess effects on different parties, examine their interests and consequences outside the price.

### ECO.2:10 - Architectural Rationale

A participant combines local knowledge about possible responses with exchange terms formed elsewhere. The work of forming and interpreting the terms can be distributed, as can production. Match the depth of inquiry to the result and the commitment it will support.

### ECO.2:11 - SoTA-Echoing

[Hayek, The Use of Knowledge in Society, §§V–VI](https://oll-resources.s3.us-east-2.amazonaws.com/oll3/store/titles/92/Hayek_0766_EBk_v6.0.pdf) explains how a participant can respond to a scarcity signal without knowing its complete cause. We adopt this use of distributed knowledge when the observed terms apply to the exchange in question.

A detailed market model can be worth the work when the question concerns future price formation or a commitment depends on it. For a bounded substitution, the applicable offer may already answer the question. Current prices may reflect power or leave effects unpriced. Reconsider the affected conclusion if the offer, the functional substitute or the commitment horizon changes.

### ECO.2:12 - Relations

Use ECO.1 for a disputed calculation basis and ECO.3 to explore a new exchange when current offers no longer meet the need. Use OPS.14 for operating comparisons, MA.1 for resource accounts, FIN.6 for investment and SYSE.9 for an unresolved engineering requirement. Use ECO.10 when the effect on total activity or resource use depends on the demand response.

### ECO.2:End

## ECO.3 - Discover an Exchange between Different Plans

> **Type:** Method pattern
> **Status:** Stable

### ECO.3:1 - Problem frame

Use this Method when different parties have complementary plans or resources and their current arrangements leave a possible exchange unsettled. Identify what each party can provide and wants to obtain. Develop or assess a proposal on those terms, and identify what makes it workable, conditional or infeasible.

Use a satisfactory existing exchange directly. Use the following steps when the combination or its terms still need to be found or assessed.

### ECO.3:2 - Problem

Participants may have complementary resources without recognizing how they could use them together. An attractive technical offer can fail because its timing, risk or required change does not fit the other party’s plan. A comparison of existing products may leave this possible arrangement outside the options considered.

### ECO.3:3 - Forces

Learning about another participant’s plan takes work and can expose private information. The parties can have different purposes and need no common scale of satisfaction to consider the exchange. Transport, timing, assurance, intermediary work and effects on others may defeat an apparent gain.

### ECO.3:4 - Solution

#### ECO.3:4.1 - Recover the relevant parts of the separate plans

Identify each party’s purpose, missing contribution and attainable offer. Use existing information about delivery windows, specification, spare capacity, access, skills or exposure. Clarify an unresolved condition when it matters to the proposed exchange.

Establish separately what the party understood, whether it agreed and which resources it can supply. Someone who understands the offer may prefer the current plan. Silence or expressed interest alone leaves commitment open.

#### ECO.3:4.2 - Construct the combination and terms

For a new proposal, specify who would supply what, to whom, when, on what terms and in return for what. It may change the product, service, counterparties, sequence or ownership. Consider monetary payment, barter, reciprocal service or conditional access as relevant.

For each party, compare participation with its feasible alternative. Include search, agreement, delivery and ongoing provision, including an intermediary’s contribution. Use ECO.1 for a disputed quantity. Different valuations can support a trade even when the parties have different purposes.

Trace the additional contributions required to realize the proposal. Use ECO.4 if supplier, customer, performer or funding commitments remain open. Identify consequences for affected nonparticipants, their rights and shared resources. Agreement between buyer and seller does not settle those further conditions.

#### ECO.3:4.3 - Choose the next move from the available grounds

Use current records, calculations and agreements for the claims they support. If a question remains, establish whether an attainable analysis or interaction could resolve it. A capacity calculation, discussion of terms, matching offer, sample, conditional order or limited use can each answer a different question. Use STR.7 to assess the value and cost of a proposed test. If a condition cannot be resolved, return the proposal or finding within the limits the evidence supports.

If a party understands the proposal and declines, the search can stop or consider different terms or counterparties. If a required contribution is unavailable, state the condition and what it prevents. Use an adequate agreement directly. Fulfil it through the appropriate operating and contractual work when performance is required.

Return the finding or proposal the task requires. Preserve evidence from a rejected proposal when it can inform a later search. Use the relevant FPF or Strategy Methods for a wider search or a different framing of the problem.

### ECO.3:5 - Archetypal Grounding

#### ECO.3:5.1 - Unused capacity meets a different delivery need

Suppose a courier has spare capacity on a return trip leaving at 18:00. A bakery pays €70 for collection at 16:00. It declines the courier’s €35 offer because the goods must leave by 16:30. The lower quote alone misses that time requirement.

The nearby chilled store has staff and a cooled van. It offers to collect the goods at 16:00, reach the store by 16:15 and store them until courier collection at 18:00, for €15. Under the proposed terms, the store would maintain the agreed temperature until handover and the courier would then maintain it and deliver to the café by 19:00. Both this route and the €70 service meet the specified delivery and temperature requirements under the assumptions of the example. The store and courier accept their respective terms and have the necessary capacity. If the bakery uses the combined service, its outlay will be €15 + €35 = €50, a €20 saving before any extra arranging costs.

The bakery can now decide whether to commit to the combined service. Its acceptance would let the parties schedule the work. Establish actual pickup, temperature control, handover and delivery from the work performed. If temperature control or responsibility at handover is unresolved, the proposal remains conditional. If storage damages the goods, the route fails the quality requirement despite its lower price.

#### ECO.3:5.2 - A useful disclosure produces no trade

An engineer offers unused evening machine time. The other workshop needs an operator, and neither party can supply one. This identifies the missing complement and leaves the sale unsupported. If the parties want to continue, they can seek a qualified operator or consider another arrangement.

### ECO.3:6 - Bias-Annotation

Enthusiasm for mutual gain can hide unequal burdens, unavailable contributions and costs imposed on outsiders. Conversely, treating every known preference as a fixed product requirement can hide a different combination both parties could use. Identify each party’s real alternatives and which proposed terms can change.

### ECO.3:7 - Conformance Checklist

For each party, identify the contribution, expected result and relevant alternative. Account for necessary complements, intermediary work and unresolved commitments. State whether the evidence supports a possibility, a conditional proposal, an agreed exchange or a completed delivery.

### ECO.3:8 - Common Anti-Patterns and How to Avoid Them

- **A lower price is assumed to settle rejection.** Recover the part of the other plan that the offer does not serve.
- **Discovery is described as resource-free.** Include the real search, arrangement and provision work.
- **Mutual consent is treated as a complete assessment.** Retain affected rights, shared resources and nonparticipant consequences.

### ECO.3:9 - Consequences

Discovery can put a new alternative into a later calculation, agreement or operating plan. An unsuccessful proposal can establish a constraint or incompatibility that answers the original question or guides a later search.

### ECO.3:10 - Architectural Rationale

Economic discovery changes which alternatives can be considered by connecting separate plans through reciprocal contributions. If a workable solution is still required and local construction has not supplied one, a wider search may be warranted.

### ECO.3:11 - SoTA-Echoing

Huerta de Soto’s *The Austrian School: Market Order and Entrepreneurial Creativity*, chapter 2, provides the historical account of entrepreneurship and dispersed practical knowledge used here. We adapt its connection among different plans. Include the real work of discovering an exchange and making its contributions available.

[Foss, Klein and Murtinu (2025)](https://link.springer.com/article/10.1007/s11138-025-00690-6) extend the account of resource mobilization under uncertainty. We adopt the need to obtain complementary commitments. One way to get an affordable complete service is to ask for other quotations on the original specification. Another is to construct a different combination, as in §5.1, where a store supplies collection and storage for the later courier trip. The second route requires finding a participant, agreeing handovers and sustaining the arrangement. Compare the gains with that work. An adequate complete offer can still be preferable. The example demonstrates the reasoning under stated assumptions. To claim one route costs less in practice, establish the costs of both. Reconsider the comparison when a party’s purpose, alternative or required complement changes.

### ECO.3:12 - Relations

Use ECO.2 when changed terms create an exchange opportunity, ECO.1 for the comparison, and ECO.4 for unresolved commitments. ECO.5 addresses private information, ECO.6 dependence following dedicated investment and ECO.7 the use of shared resources. Use STR.7 to evaluate a bounded experiment. When another way to obtain the result is needed, use FPF C.39 to develop it and C.40 to extend the search from reusable material.

### ECO.3:End

# Part II - Commitments and adaptation

## ECO.4 - Form Resource Commitments for an Uncertain Venture

> **Type:** Method pattern
> **Status:** Stable

### ECO.4:1 - Problem frame

Use this Method when participation in a proposed venture depends on commitments that other customers, suppliers, performers or funders have yet to make. Identify the first contribution in question and the conditions under which its holder can commit it. Establish whether the commitments can be made together. Construct a feasible arrangement if one is required.

Identify who can make each commitment and whether the promised contribution can be supplied. A service may be authorized to reserve a resource or may have authority only to prepare a proposal. Use existing commitments for the work their terms cover.

### ECO.4:2 - Problem

A proposal can be technically feasible and still lack an order, operator or available funds. Interest in buying does not reserve capacity. A willing investor cannot supply an absent operator by committing money alone. More explanation will not reduce exposure for a party that understands and rejects the terms. Check whether conditions that seem attainable separately can take effect together.

### ECO.4:3 - Forces

A participant may have grounds to act even when a novel venture has no complete forecast. Conditions can limit exposure and can also keep every promise inactive. A demonstration is useful when the intended recipient can use its result to answer a relevant question.

### ECO.4:4 - Solution

#### ECO.4:4.1 - Recover the missing contribution and the reason it is missing

Identify the venture step being assessed and what it requires, such as an order, access, finance, capability, supply or permission. Use an applicable OPS or MA account of production and resources. Establish separately what is available, what has been offered or reserved and what a party has bound itself to supply.

If a contribution is unavailable, establish what prevents it. A record may already identify the reason. Ask the party when its understanding, decision or account is needed. For an unclear proposal, use EXD to supply a relevant explanation. For disagreement, consider whether different terms or participants could help. For missing means or capability, establish what can be obtained or developed. A supported finding of the obstacle can answer a diagnostic question.

#### ECO.4:4.2 - Build conditions that can be satisfied together

For each material commitment, identify what is promised, by whom, to whom, when it can take effect and on what terms it can be released or withdrawn. Use the effective agreements where they supply these facts. Check the party’s ability to supply the contribution and its authority to commit it.

Trace which commitments depend on others. If the supplier needs payment to start and the investor pays only after delivery, there is no first action unless someone can fund the start or an available mechanism can satisfy the conditions together. For simultaneous commitments, establish the parties’ resources, authority and means of execution. If those conditions fail and another design is needed, consider a deposit, limited funded trial, staged supply, reservation, another provider or a smaller result. Compare who bears the exposure and what would be lost if the venture stops.

Use a demonstration when it can answer a needed question, such as whether a process handles a customer’s sample or a service fits the customer’s work. Establish any funding, order or authority from the relevant terms and commitments.

#### ECO.4:4.3 - Commit only what the combination can support

Check combined obligations against available resources and timing. A provider can be overcommitted even when each obligation fits separately. Use OPS.13 when the feasibility account is missing, and FIN.10 when financial terms are needed.

Report the attainable combinations, the conditions that remain open or the reason the venture cannot proceed. If a decision is needed, the party authorized to make it can choose a combination, keep a conditional plan or stop. When asked for advice, give the recommendation and its grounds to the intended recipient. For a proposed next step, identify what releases it and who bears the remaining exposure. Reassess an affected conclusion when contributions, understanding, alternatives or dependencies change. Seek further evidence when its likely value to the requested result justifies the inquiry.

### ECO.4:5 - Archetypal Grounding

#### ECO.4:5.1 - Breaking a circular funding condition

Suppose a customer wants to see a working demonstration before ordering a pilot service. The specialist needs €6,000 to prepare it. A successful demonstration could meet the customer’s technical condition for ordering. The signed order would meet the funder’s condition for contributing. Under the proposed terms, no one can pay for the demonstration that would start this sequence.

The entrepreneur can risk €1,000. Using an available test facility, the specialist can demonstrate one limited operation for that amount. The customer agrees that successful handling of its sample would settle the outstanding technical question. Price and delivery terms are stated separately. The entrepreneur can commission the limited demonstration from the available €1,000.

If the demonstration succeeds, establish what the customer decides and whether the funder’s order condition is met. If the customer cannot allocate a budget even after technical success, the demonstration cannot resolve that barrier. The diagnosis may suffice. To proceed, the venture would need another customer, a financing arrangement or a different scope.

In another case, each of two sponsors authorizes the release of €500 provided the other €500 is released at the same time. The administrator holds both sums and can release them together once both authorizations arrive, or return them after the deadline. Those resources and powers make simultaneous release possible. Neither sponsor needs to receive the other payment first.

#### ECO.4:5.2 - An AI service can explain but cannot commit

Suppose an AI service prepares a clear investment proposal but has no authority to reserve funds. This can satisfy a request to prepare the proposal. Funding still requires a commitment by a party authorized to make it. Improving the explanation would not itself reserve the money.

### ECO.4:6 - Bias-Annotation

A founder may interpret interest as agreement, and a technical specialist may treat a successful prototype as evidence the venture can proceed. A sceptical party may understand the offer and face a real constraint. Identify the reason for each outstanding contribution.

### ECO.4:7 - Conformance Checklist

Which contributions are available, and under what conditions? Can an attainable first action or a feasible simultaneous execution satisfy the dependencies? If neither works, identify the obstruction. Distinguish authority, capacity, resources and willingness when they affect the finding or the proposed next step.

### ECO.4:8 - Common Anti-Patterns and How to Avoid Them

- **All parties are willing, so the venture is financed.** Trace the conditions and available first contribution.
- **Explain until the counterpart agrees.** Determine whether the difficulty is understanding, disagreement or unavailable means.
- **A pilot consumes scarce means without resolving a useful question.** Identify the finding or decision its result could support before committing the resources.

### ECO.4:9 - Consequences

A smaller attainable commitment can advance a venture. An inquiry can also establish that no available combination can supply the missing means. State which parties, resources and conditions support the conclusion.

### ECO.4:10 - Architectural Rationale

Mobilizing resources requires commitments that fit together across the parties’ plans. Financing terms, explanation and operating feasibility can each contribute. To use conditional commitments as grounds to proceed, establish how all their conditions can take effect.

### ECO.4:11 - SoTA-Echoing

[Foss, Klein and Murtinu (2025)](https://link.springer.com/article/10.1007/s11138-025-00690-6) examine how entrepreneurs mobilize resources under uncertainty. Their [2026 stakeholder-enrollment analysis](https://link.springer.com/article/10.1007/s11187-026-01192-w) distinguishes difficulties in developing a shared understanding of a novel venture. We adopt those questions and also examine understood disagreement and unavailable resources.

When the parties understand the proposal and only financing terms are open, a standard financing transaction may suffice. To claim it takes less effort, compare the actual financing work with a wider mobilization effort. The sources identify distinctions for that comparison. Reconsider a conclusion when a participant’s decision changes or the proposed demonstration would leave the relevant uncertainty open.

### ECO.4:12 - Relations

Use ECO.3 for a missing exchange, ECO.5 for private information and ECO.6 for dependence after commitment. EXD supports explanation and STR.7 helps assess and design a bounded test. Use OPS.13 for resource feasibility and FIN.10 for financing. Use HCD when a person needs to learn a contribution. A sufficient supplier can also provide the contribution directly.

### ECO.4:End

## ECO.5 - Choose Exchange Terms for Private Information and Effort

> **Type:** Method pattern
> **Status:** Stable

### ECO.5:1 - Problem frame

Use this Method when the terms of exchange depend on quality, circumstances or later action that one party knows or controls and another cannot cheaply verify. Identify each party’s available choices. Assess the existing terms or compare proposals to establish when the desired contribution and participation would be worthwhile.

Return the incentive or selection result the terms support, including a condition that prevents the intended agreement. If different terms are needed, propose them with their mechanism and limits. Use an adequate established purchase directly.

### ECO.5:2 - Problem

A price may attract low-quality sellers and exclude more reliable ones. A payment rule can reward a measurable proxy while the desired work is neglected. An unenforceable promise to take care may leave the provider’s returns unchanged. Terms that shift all risk to the provider can also exclude someone capable of the work.

### ECO.5:3 - Forces

Information has acquisition and verification costs. Incentives and risk sharing can conflict. A strong warranty or stake can make an offer credible while excluding a good provider without enough capital. Observable outcomes can depend on both effort and circumstances outside the performer's control.

### ECO.5:4 - Solution

#### ECO.5:4.1 - Locate the private fact or action

Identify the information or action that matters and who can know or control it. Existing quality, intended use or financial condition may be privately known before agreement. Later maintenance, care or effort may be privately chosen. The same exchange can involve both. Evaluate separately whether changed payment terms affect an action and whether a choice reveals an existing fact.

Identify the choices each party can make under the actual terms. They may disclose or withhold information, select an offer, decline, change effort, manipulate a measure, withdraw or seek new terms. Include the alternatives available to the participant, including ones the designer would prefer them not to take.

#### ECO.5:4.2 - Construct terms from the choices they must change

Start with terms the parties could carry out. These might include payment after an interpretable test, a refund for a defined failure, a deposit at risk, or a choice of services. Establish how the specified event can be observed and who has the means and authority to deliver the consequence. Relate each available choice or event to its payment or service. Use an existing rule directly when its effects meet the need.

**For a private action, compare the participant’s returns under each relevant choice.** Include ways to improve the measure while neglecting the result. To design different incentives, change a term that alters these relative returns. Check participation against the outside alternative, including the participant’s exposure. A design that is to induce the intended action needs both participation and the relevant choice after entry.

In a risk-neutral model, let b be the payment received regardless of the test, w the extra payment for passing, p the probability of passing under an action and c its cost. Expected return is b + p × w − c. Compare returns for the intended action and its relevant alternatives. The difference in expected bonus equals w times the difference in passing probabilities. Increasing b by the same amount for every action raises the return to entering without changing their order in this model. If risk aversion, wealth or payment timing matters, compare the relevant distributions and financing needs or use a qualified specialist result.

**For a private fact, examine the choices of each relevant type of participant.** A seller may know the item’s quality, or a buyer its own need. A model can stipulate possible types without identifying the actual participant’s type. For each type, compare the proposed offer, the other available offers and nonparticipation using its costs, benefits and exposure.

A refund that will be paid costs the more failure-prone seller more in expectation. Different service packages can also have different values to buyers. Use a difference of this kind to construct terms when separation is wanted. Check each type’s available choices. If different types would accept the same offer, acceptance alone leaves their types unresolved. The exchange can still be worthwhile under a supported mixed or conditional account. If later actions can alter the result, compare the incentives for those actions as well.

**Find terms that meet the participation and choice conditions together.** If designing terms, vary the price, contingent payment or service within actual observation and resource limits. Check the result for the other party as well. Indifference establishes a tie. To predict or attribute one of the tied choices, use additional grounds. When no feasible terms satisfy the requirements, report the limit. A further design may change the service, observation, risk allocation or participant. Raising all payments can leave relative incentives unchanged.

Use supported probabilities and valuations for claims about actual participants. For a conditional calculation, state the assumptions. Where the evidence supports only cases or ranges, report what holds across them and what could change the conclusion. Include verification, enforcement, tied-up capital and unpriced effects. A deposit can discourage an unwanted choice while excluding a capable participant unable to bear the exposure.

For an incentive linked to an observed result, establish what the observation reveals about the desired work. If the provider can improve the measure while neglecting the result, reassess the terms or observation. A signal that mainly adds uncontrollable risk can discourage participation. Staged payment can limit exposure to nondelivery while leaving quality unknown. State which consequence the mechanism supports.

#### ECO.5:4.3 - Make the terms usable

To establish that the terms are usable, check whether the warranty provider can pay, how the acceptance condition is interpreted, whether the stake remains exposed and which parties can agree. Obtain a qualified legal or specialist mechanism-design result where the claim depends on enforceability or a particular guarantee. A comparison under stipulated terms can be reported with that condition open.

Report what the terms imply for the relevant choices and what remains uncertain. If proposing a change, explain how the new terms would alter the comparison. Keep effective existing terms when they meet the need. Seek additional information when its likely value justifies the burden.

### ECO.5:5 - Archetypal Grounding

#### ECO.5:5.1 - Care under an outcome-based payment

Suppose a maintenance provider can choose low care, costing €4 with probability 0.5 of passing the test, or high care, costing €12 with probability 0.9. The provider is risk-neutral, has no other relevant costs and could earn €32 from its next best feasible alternative. The test is functionally valid and cannot be cheaply manipulated under these assumptions.

Let the contract pay a nonnegative base b and a nonnegative bonus w for passing. High care strictly beats low care when (0.9 − 0.5) × w > €12 − €4, so w > €20. It strictly beats the outside option when b + 0.9 × w − €12 > €32. With an available €30 bonus this requires b > €17. A €20 base satisfies both. To assess the whole exchange, also compare the result for the buyer with its feasible alternative.

With b = €20 and w = €30, expected payment less effort cost is €31 for low care and €35 for high care. The €12 gain in expected bonus exceeds the €8 extra cost. High care also beats the €32 outside return. Under a flat €35 payment the provider would net €31 for low care and €23 for high care, both below the outside return.

Suppose the risk-neutral buyer values a pass at €80 and a failure at zero. The test and other costs are the same for both offers. Under the conditional contract, expected benefit is €72 and expected payment €47, leaving €25. A second provider offers the same 0.9 pass probability for a fixed €50, leaving €22. The buyer therefore proposes the conditional contract, which also gives the first provider more than its outside option. If a pass were worth only €40 and idle equipment carried no further loss, either contract would give the buyer negative expected net benefit, so the buyer would decline both.

The comparisons establish the modeled direction of the incentives under the given assumptions. An optimality or general behavioral claim needs further grounds. If the provider can pass the test while leaving the equipment unreliable, the terms reward the wrong result. If variable receipts exceed the provider’s tolerance for risk, reassess participation.

With a €15 cap on the bonus, the largest additional expected reward for high care is 0.4 × €15 = €6. That is less than the €8 additional cost. Raising the common base leaves this difference unchanged under the assumptions. If the buyer still needs the work, it can use the other provider if the complete offer remains acceptable or reconsider the observation, the task or the terms.

#### ECO.5:5.2 - A warranty whose issuer cannot pay

Two sellers offer the same warranty, but one has no resources to honour a claim and can disappear after sale. The same promise therefore has different expected consequences. A deposit, credible guarantor, continuing relationship or different offer may change the comparison. Assess what would make the payment or service available.

#### ECO.5:5.3 - Construct a quality offer and test who would accept

Suppose a buyer needs one refurbished component. Sellers know whether their own component has a 0.1 or 0.5 chance of failure during a fixed warranty period. The buyer cannot tell which applies. The model specifies the same verifiable failure, fixed probabilities unaffected by later care, a €40 supply cost, and risk-neutral buyer and sellers. The more reliable seller’s alternative yields €50 net and the less reliable seller’s yields €30. Supply, administration and cash are available with no other relevant costs.

Set a price P and a failure refund R. A trusted administrator can hold R from the price throughout the warranty and refund it if the verifiable failure occurs. The seller can finance the amount held. For a seller with failure probability q, expected net return is P − €40 − q × R. Compare that return with the outside option for that seller.

| Required choice | Comparison | Bound on price |
| --- | --- | --- |
| More reliable seller prefers this offer | P − €40 − 0.1 × R > €50 | P > €90 + 0.1 × R |
| Less reliable seller prefers its outside alternative | P − €40 − 0.5 × R < €30 | P < €70 + 0.5 × R |

Both strict comparisons require R > €50. At R = €50 the two price bounds meet at €95, where both types are indifferent between accepting and their outside option. With a feasible €80 refund, strict separation requires €98 < P < €110. At P = €100 the more reliable seller nets €52 against €50 outside. The less reliable seller would net €20 against €30 outside and declines. Under these assumptions the choices separate the types.

The buyer values a working component at €150 and a failed one at zero. Under the separating offer the buyer’s expected value plus refund less price is 0.9 × €150 + 0.1 × €80 − €100 = €43. A verified alternative with the same 0.1 failure probability costs €120 and carries no refund, giving €15 expected net value. These terms make the proposed exchange preferable to the available alternatives for both the buyer and the more reliable seller. The refund changes who bears the loss. In this model it leaves the selected component’s failure probability at 0.1.

Suppose a refund above €20 cannot be secured. With R = €20, strict acceptance by the reliable seller requires P > €92, while strict rejection by the other requires P < €80. No price meets both. A price that strictly attracts the reliable seller also attracts the other, so acceptance no longer supports the old quality inference. The buyer can use the verified alternative, obtain another credible arrangement or assess an offer for both qualities if their mix can be supported. If the mix is unknown, leave the resulting failure probability open.

Reopen the comparison when a seller's outside option, ability to finance the retained amount, failure observation or competing offer changes. If only one kind can finance the arrangement, acceptance can reflect access to capital as well as quality. Reconsider the claimed inference before using it to procure the component.

### ECO.5:6 - Bias-Annotation

A precise-looking calculation may conceal disputed probabilities, power or a badly chosen proxy. Before attributing a poor outcome to dishonesty, examine which actions the terms made worthwhile and whether the observation tracks the intended result.

### ECO.5:7 - Conformance Checklist

Which private fact or later action matters, and what do the terms imply for the participant’s available choices, including nonparticipation? Establish what the specified observation or enforcement arrangement can support. Identify any tie, infeasible term or unresolved condition and the assumptions on which a numerical comparison depends.

### ECO.5:8 - Common Anti-Patterns and How to Avoid Them

- **Paying for a proxy is treated as paying for the result.** Trace how the performer can improve the proxy and whether that supplies the result.
- **A written promise is treated as a credible consequence.** Recover the means and conditions that make its consequence effective.
- **Only incentives are optimized.** Retain participation, risk bearing, verification and exclusion costs.

### ECO.5:9 - Consequences

Some exchanges become feasible while private facts remain undisclosed. Others may require simpler terms or another participant, or may remain infeasible. Complex terms can increase the work of interpretation and create opportunities to game the rule. Compare that burden with the contribution the terms make possible.

### ECO.5:10 - Architectural Rationale

Terms can change a participant’s feasible choices and their relative attractiveness. Acquiring information and changing the consequences of choices are different ways to improve an exchange. Assess their costs in the case at hand. Check the decision to participate and the subsequent choice of action separately.

### ECO.5:11 - SoTA-Echoing

[Akerlof (1970), §IV](https://www.sfu.ca/~allen/Ackerlof.pdf) identifies guarantees as one possible response to hidden quality. [Rothschild and Stiglitz (1976), §I.1, I.3 and I.6](https://economia.uc3m.es/docencia/MicroII/Rothschild-Stiglitz%201976.pdf) examine how participants select from offered contracts. A contract intended for one type is also available to another, so evaluate both types’ choices. We adapt that comparison to the private-fact case. An insurance-market equilibrium result would require its own applicability grounds in procurement.

[Holmström (1979), §2 and concluding remarks](https://gwern.net/doc/economics/1979-holmstrom.pdf) examines contract choice subject to participation and the participant’s choice of action, including information and risk sharing. The examples here use finite choices and risk-neutral participants to construct feasible terms. The paper’s risk-averse optimization problem has different assumptions.

An ordinary contract with direct observation can suffice when observation is informative and affordable. When observation is costly or incomplete, compare what feasible terms would induce under the stated conditions. Establish legal enforceability or field performance on the grounds those further claims require. Reassess the affected conclusion when participation, available actions, signal quality or enforcement changes.

### ECO.5:12 - Relations

Use ECO.4 for complementary venture commitments and ECO.6 for dependence after investment. Use FPF E.13 if a proxy replaces the intended result and MMP for a needed mathematical model. Applicable law and corporate governance determine who can take a legal or corporate action when the work calls for it.

### ECO.5:End

## ECO.6 - Arrange Adaptation in a Dependent Trading Relationship

> **Type:** Method pattern
> **Status:** Stable

### ECO.6:1 - Problem frame

Use this Method when investment, location, integration or acquired knowledge makes a trading relationship costly to leave and later changes cannot all be settled in advance. Identify what loses value outside the relationship and which disturbance matters. Assess the current terms or compare ways of adapting while limiting each party’s exposure.

Return the supported finding about dependence or a comparison of arrangements. When a choice is required, it can include retaining the current arrangement. Use operating management for routine allocation within existing responsibilities.

### ECO.6:2 - Problem

Several suppliers may compete before a dedicated investment. After investment, switching can forfeit the tooling’s value or require additional time or specialized knowledge. Establish which alternatives remain available after commitment and what the parties can still adapt. Detailed specifications can be too costly to cover every disturbance.

Before diagnosing a need for organizational change, consider whether a technical change, a second source or different terms in the existing agreement can address the dependence.

### ECO.6:3 - Forces

Dedicated resources may improve performance while narrowing outside options. Safeguards may protect investment while limiting flexibility. Common ownership changes authority and incentives and has coordination costs. An arm’s-length agreement can become costly when it must handle a difficult adaptation.

### ECO.6:4 - Solution

#### ECO.6:4.1 - Find the dependence and the required adaptations

Identify who bears the investment or other contribution and what its alternative uses would be. Consider tooling, location, integration and relationship-specific learning where relevant. Compare the outside options before and after commitment. Use EAM or FIN when an exit or redeployment cost still needs to be established.

Identify disturbances the terms need to handle, such as a volume change, new specification, input cost, delay or new use. Establish which the current arrangement covers and which would leave an adaptation unresolved. State why the dependence matters under the conditions examined.

#### ECO.6:4.2 - Compare feasible constructions

Where a change is being considered, examine whether a standard interface, redeployable equipment, buffer or other source would reduce dependence. Use available fit and cost evidence. A reduction in dependence may justify a performance cost if the full comparison supports it.

Where applicable, compare reciprocal commitments, price-adjustment rules, staged investment, asset or knowledge rights, joint adaptation decisions and routes for dispute or exit. Establish who can propose a change, who can decide and who bears its cost. A continuing relationship can support cooperation when future opportunities matter to the parties.

Consider common ownership or organizational change when decision rights, incentives or adaptation costs make it a credible alternative. Include the costs of directing the work after the change. If this alternative is chosen, use OCE and CGOV for the required organizational construction and corporate actions.

#### ECO.6:4.3 - Choose an arrangement for the required adaptations

Compare like intended service and disturbance conditions, including investment exposure, operating performance, delay, enforcement and exit. Use conditional comparisons when a future disturbance cannot be assigned a defensible probability.

Report what the arrangement protects, which adjustments are possible and what remains conditional. For a choice, assess which parties can supply the contributions and identify the conditions that would warrant reconsideration. A legal or technical gap can limit one conclusion while other results remain supported.

### ECO.6:5 - Archetypal Grounding

#### ECO.6:5.1 - Dedicated tooling or a more expensive standard process

Suppose a supplier must spend €20,000 on dedicated tooling with a resale value of €2,000. The customer can cancel after a month, but the supplier’s unit price assumes recovery over a year. Future volume is uncertain. Before customer payments, cancellation would expose the supplier to the difference between investment and resale proceeds.

The parties could accept a minimum-payment commitment or stage the investment. The standard process needs no dedicated tools but adds €3 per unit, or €6,000 on a possible first order of 2,000 units. The initial unrecovered exposure on the dedicated tools is €18,000 before customer payments. Compare the options for the same service and period and identify who bears each amount and how much has already been recovered.

Now suppose only the dedicated process achieves the required surface quality. Both parties can support the investment. They choose supplier-owned tooling and specify how much each customer payment recovers. Under the agreement the purchasing manager can cancel future volume by settling the unrecovered tooling cost less resale proceeds. The supplier is responsible for resale. A change of specification requires a separate agreement.

After the first month, customer payments have recovered €4,000. Demand falls. A buyer offers €2,000 for the tooling. The purchasing manager cancels the remaining volume and pays €20,000 − €4,000 − €2,000 = €14,000. The supplier sells the tooling and recovers the full €20,000. The released capacity can now be reassigned through OPS. The selected arrangement retained the process required for surface quality and permitted this change of volume. A different resale value, an unaffordable settlement or a different disturbance would reopen the affected conclusion. Enforceability in another setting requires grounds from that setting.

If a new interface instead makes the tooling readily reusable, the dependence may shrink enough for ordinary purchasing.

#### ECO.6:5.2 - Counting existing assignments

If a qualified team has promised more work than it can perform this month, compare its commitments with available capacity. A finding of overload can answer the question. Reassigning work within existing authority belongs to OPS. Use ECO.6 when dependence between trading parties or the terms for adapting their relationship are what make the problem consequential.

### ECO.6:6 - Bias-Annotation

The buyer can overlook the supplier’s exposure, and the supplier may request guaranteed revenue for risks it can bear. Compare whose resources and options change under each arrangement. Include feasible ways to reduce dependence itself as well as terms that compensate for it.

### ECO.6:7 - Conformance Checklist

Which dependence and disturbance does the arrangement address? Establish who bears exposure, who can authorize an adjustment and what the exit terms permit. If choosing among arrangements, compare credible technical, contractual and organizational alternatives at compatible scopes.

### ECO.6:8 - Common Anti-Patterns and How to Avoid Them

- **Competitive bidding is assumed to last after dedicated investment.** Compare the outside options before and after commitment.
- **Market failure is compared with a costless organization.** Include the actual costs and limits of every feasible arrangement.
- **An overloaded team is treated as evidence for restructuring.** Establish the workload and capacity first. If a change is needed, assess what can be resolved under the existing allocation authority.

### ECO.6:9 - Consequences

The parties can protect productive investment while preserving an affordable way to adapt. The economically preferred arrangement can be a less specialized technology, a different contract, an existing relationship or an organizational change. Each retains different limitations.

### ECO.6:10 - Architectural Rationale

Dependence arises when commitment changes the value of the parties’ outside options. Assessing how they can adapt helps identify when technical design, contract terms or organization structure would address the economic problem.

### ECO.6:11 - SoTA-Echoing

[Williamson (2010), sections on adaptation and the discriminating alignment of transactions](https://web.pdx.edu/~nwallace/EHP/TCEProgression.pdf) compares market, hybrid and hierarchical arrangements under different conditions of dependence and adaptation. We adopt the comparison of feasible arrangements, including technical changes that make an asset useful in more than one relationship.

An ideal complete contract can clarify what a feasible agreement leaves open. Common ownership may be a credible alternative when its actual costs and adaptation benefits warrant it. Use the economic comparison in any required organizational, asset or financial work. Reconsider the affected conclusion when redeployability, disturbances, rights or adaptation costs change.

### ECO.6:12 - Relations

Use ECO.1 for a disputed calculation, ECO.4 for commitments and ECO.5 for incentive terms. Use EAM.6 and EAM.7 for asset use or replacement and FIN.6 and FIN.8 for financial consequences. OPS covers current flow and resources. Use OCE for organizational arrangements and CGOV for required corporate authority or acts when these are part of the selected alternative.

### ECO.6:End

# Part III - Shared and extended coordination

## ECO.7 - Coordinate Use and Renewal of a Shared Resource

> **Type:** Method pattern
> **Status:** Stable

### ECO.7:1 - Problem frame

Use this Method when separate uses of a shared resource or insufficient upkeep put its useful condition at risk. Identify the condition and the actions that affect it. Assess the existing rules or, if a change is needed, develop workable arrangements for use, renewal and adaptation with those who can make them effective.

For routine allocation of a machine under adequate rules, use the applicable OPS Method. Use ECO.7 when different claims, contributions or effects on the shared resource require examination.

### ECO.7:2 - Problem

A withdrawal that fits one user’s plan can deprive another user or leave too little for renewal. Cutting withdrawals may still leave upkeep unfunded. Include affected downstream and seasonal users and people whose rights or access are easily overlooked. Establish the physical limit, actual rights and provision for upkeep from their respective grounds.

### ECO.7:3 - Forces

Observing withdrawals, upkeep and exclusion can cost time and money. Participants may differ in knowledge, needs, alternatives and power. Check whether a local rule shifts a cost beyond its boundary and whether a common rule covers relevant local differences.

### ECO.7:4 - Solution

#### ECO.7:4.1 - Recover the resource and the actions that affect it

Identify the resource, the units or services obtained from it, the condition that matters and the relevant period. Distinguish withdrawal from provision or renewal. Determine whose actions affect availability, quality or renewal, including parties outside the initial group.

Use an adequate physical or operating account directly. Use PHY, MMP or OPS when a missing fact or model matters. An allocation must fit the available flow. Establish rights to that flow from the applicable rules or agreements.

Identify the current rights of access, exclusion and withdrawal. Compare them with what participants can do and what they have done. A proposed allocation takes effect through the applicable decision or agreement.

#### ECO.7:4.2 - Construct a workable combination of rules

Start with the rules that govern the question. They can concern entry, quantities, timing, upkeep, observation, dispute resolution or authority to change the arrangement. Use suitable existing rules. If a different combination is needed, compare how the proposed arrangements address the actual difficulty.

Assess whether participants have the means and incentives to comply. Include the costs of observation and response, especially for smaller users. Before treating an event as a violation, check what the observation establishes. A missed reading may be a measurement problem. For an established violation, match the response to its effect and the applicable rule.

Trace effects beyond a local arrangement. Several communities may use one catchment or infrastructure even if they allocate separately. Identify the common constraint. Where an operating arrangement is needed, establish how it can handle that constraint while preserving legitimate local decisions.

#### ECO.7:4.3 - Test ordinary use and changed conditions

Compare the proposed allocation with the available resource and the amount needed for renewal or other protected uses. A shortfall can settle a feasibility question. To establish how a proposed rule would work, follow an allocation and renewal case under the relevant conditions. For a claim about low supply, a missing payment, new entry or a disputed reading, identify who can detect the change and what the rule permits. Use a suitable existing case or test when it covers the question.

Return the supported finding, feasible arrangement, proposed trial or constraint still unresolved. Use the observations that distinguish the relevant cases. Reconsider a conclusion when a change in the resource, access or rule affects its grounds.

### ECO.7:5 - Archetypal Grounding

#### ECO.7:5.1 - Sharing water while retaining a downstream flow

Suppose 100 units enter a canal each day. Upstream users consume what they withdraw, and downstream users must receive at least 40 units. Two upstream groups request 50 and 40. Granting both would leave 100 − 50 − 40 = 10 downstream. The maximum combined upstream withdrawal is 60 under these conditions.

The parties know the day’s controlled inflow before withdrawal and have authority to adopt an arrangement. With 100 units, upstream allowances of 35 and 25 leave 40 downstream. A caretaker can read inlet and outlet meters, check gates and perform specified routine upkeep for €40 per week. Each upstream group can pay €20. Larger repairs need a separate decision.

The adopted agreement allows the caretaker to set allowances of 20 and 20 on an 80-unit day. Each group can meet its essential needs at 20. The caretaker announces the allowance before withdrawal and checks what happens. When two credible readings differ between 80 and 100, the parties temporarily use the lower allowance and jointly check the meter. Disagreement alone leaves the cause open.

With 80 units, withdrawals of 20 and 20 leave the required 40 downstream. Below 80 the stated essential uses cannot all be supplied. The caretaker must report that limit. If one group misses its €20 weekly payment and the other pays, the funded €40 reserve covers two weeks of the shortfall. If both groups miss their payments, it covers one week of upkeep. Once the reserve runs out, continuing service requires a replacement contribution or a feasible reduced plan. The case stipulates these means and commitments.

#### ECO.7:5.2 - Information and the services needed to use it

Several teams can copy a software manual without exhausting the copies. They can, however, exhaust a shared service’s processing capacity or its maintainers’ time. Identify which contribution is scarce before applying a withdrawal or access rule.

### ECO.7:6 - Bias-Annotation

Identify dispersed or downstream users who bear consequences even if better-organized participants speak for themselves. Equal percentages can yield different results when rights or needs differ. Explain the physical consequences and the interests affected before drawing a conclusion about fairness.

### ECO.7:7 - Conformance Checklist

Does the finding relate use to the resource’s condition or renewal? Which participants are affected, which rights apply, and which proposed rules are still open? For a claim that an arrangement can operate or adapt, establish the means to observe, supply and decide in the conditions claimed.

### ECO.7:8 - Common Anti-Patterns and How to Avoid Them

- **Allocation is treated as physical feasibility.** Check the resource account and time window.
- **Upkeep is expected to happen by goodwill alone.** Recover its contribution and means, or reduce the promise.
- **A successful local rule is copied into a different setting.** Check whether the receiving resource, users, means of observation and wider effects support the proposed use.

### ECO.7:9 - Consequences

A shared-resource arrangement can protect required uses while allowing changes in supply. Several centres of decision may respond well to local conditions, but they also need ways to coordinate, maintain the resource and handle disputes. Assess the actual arrangement under its conditions.

### ECO.7:10 - Architectural Rationale

Relate physical conditions, rights, participant actions and decisions where they affect one another. A workable allocation needs both a physical basis and an arrangement under which it can take effect. A report on one of these questions can use a narrower account.

### ECO.7:11 - SoTA-Echoing

[Ostrom (2010), sections IV and VII](https://web.pdx.edu/~nwallace/EHP/OstromPolyGov.pdf) provides a basis for comparing shared-resource institutions and interacting decision centres. We adopt the comparison of feasible rules in their settings, including the effects of ownership arrangements where relevant.

[Baldwin and colleagues (2024)](https://onlinelibrary.wiley.com/doi/10.1111/psj.12518) identify limits in the evidence about polycentric arrangements and examine their context and changes over time. The canal case illustrates a local comparison and when to revisit it. Use a single operator’s established allocation if it meets the need. A claim that one arrangement performs better requires comparison under the relevant conditions.

### ECO.7:12 - Relations

Use ECO.8 for wider coordination and ECO.9 when the rules or their implementation need to change. Use OPS for operating allocation and upkeep, and PHY or MMP for a missing physical account or model. Identify applicable rights and authority. Use OCE if an organizational change is selected.

### ECO.7:End

## ECO.8 - Join Direct Cooperation with a Wider Economic Order

> **Type:** Method pattern
> **Status:** Stable

### ECO.8:1 - Problem frame

Use this Method when a rule from one relationship is being applied to another. An expectation of voluntary help can fail in an external service agreement, while pricing every small contribution can disrupt direct cooperation. Identify the interaction and the conditions that make it work. Establish which parts need direct coordination, agreed terms, prices or a wider rule.

The result can be a supported finding about the relationship, an adjustment that addresses a mismatch or the condition still unresolved.

### ECO.8:2 - Problem

A group may expect an outside supplier to share its purpose, local knowledge or willingness to help. That expectation can lead it to promise work the supplier cannot or will not provide. Inside a team, pricing every small contribution may remove discretionary help or shared learning. Explicit terms may instead clarify an otherwise disputed obligation.

Personal knowledge, organizational assignment and exchange can all govern different parts of the same action. Identify the relation that matters to the work. The group’s size alone leaves that question open.

### ECO.8:3 - Forces

Direct coordination can use rich local knowledge but is costly to extend. General rules and exchange terms allow different purposes to coexist but can omit particular needs. Some shared resources require coordination beyond bilateral exchange; a central command requires authority and knowledge it may not possess.

### ECO.8:4 - Solution

#### ECO.8:4.1 - Recover the interaction and its coordination conditions

Identify the result and the participants or services that supply its contributions. Establish what sustains each relevant relation, such as shared purpose, personal knowledge, an assignment, a continuing agreement, a price and specification, a general rule or a shared-resource arrangement.

Personal knowledge can support cooperation. Authority to direct another participant’s work requires its own basis. A contract can connect two separately performed contributions, while a constituent operation forms part of the encompassing work. Distinguish the relations relevant to the supply chain, institution and composition of Methods.

#### ECO.8:4.2 - Find the unsupported transfer of a rule

Assess how the proposed rule would work in the receiving relationship. Which information, agreement, trust, authority or capacity to bear cost does it require? Check whether those conditions are present and whether using the rule would remove a needed contribution.

If a mismatch is established and a repair is needed, address its cause. Define the result an external supplier can deliver, retain local discretion that enables adaptation, give unknown participants access under a general rule, or use ECO.7 for a shared constraint. Different relations can call for different arrangements.

Compare whose purposes and alternatives the repair serves and what it costs others. A current price helps strangers exchange without common goals, but cannot by itself settle every affected right or shared-resource effect.

#### ECO.8:4.3 - Carry the boundary into the work

Identify how each relevant participant can act under the applicable rule or relationship. The same person might offer voluntary help in one situation and supply a paid service in another. Make the terms clear enough to distinguish a request from an invocation of an existing commitment.

When the result depends on a vertical of methods, show the constituent operations and the encompassing method they help enact. For example, checking a supplier's terms may be part of arranging a service that is part of developing a venture. The supplier's separately performed service is connected by the agreement; it does not become a constituent operation of the buyer's method merely because it is needed.

Return the supported account of the coordination, any proposed adjustment or the problem still open. Use OCE or CGOV when a selected change affects organizational arrangements or corporate authority.

### ECO.8:5 - Archetypal Grounding

#### ECO.8:5.1 - A community kitchen buys reliable maintenance

Suppose volunteers at a community kitchen rearrange tasks in conversation and help one another during a difficult shift. The kitchen also needs a refrigeration contractor able to respond outside its normal shift.

Volunteers’ expectations of mutual help do not secure a response from the contractor. Pricing every small favour among volunteers would change the kitchen’s internal cooperation. The kitchen keeps that cooperation and specifies the coverage and contact terms it needs from a paid service. Use ECO.4 to establish whether that service can be obtained and ECO.6 where later dependence on the contractor affects adaptation.

If a volunteer is also the contractor, the two relations still differ. The person needs to know when the kitchen requests voluntary help and when it invokes the paid commitment.

#### ECO.8:5.2 - Local water agreements share a wider constraint

Two canal groups allocate within their areas. Each local rule can be feasible while their combined withdrawals exceed the common supply. That joint limit can answer a question about present feasibility. If a workable arrangement is required, connect the allocations through the physical limit and a decision the parties can carry out.

### ECO.8:6 - Bias-Annotation

Identify which cooperation or exchange the relation can support and who could be excluded or burdened. Personal solidarity and impersonal exchange each have conditions that may be absent in this case.

### ECO.8:7 - Conformance Checklist

Which relation is being examined and what supports it? If a rule has been transferred, establish whether it works under the receiving conditions. For a proposed adjustment, identify any direct cooperation it depends on. If it requires an external contribution, check the terms on which that contribution can be obtained. Distinguish constituent work, contractual dependence, authority and wider coordination where the difference matters.

### ECO.8:8 - Common Anti-Patterns and How to Avoid Them

- **The economy is treated as one organization.** Establish where shared authority and information exist and how the remaining contributions are coordinated.
- **Every relationship becomes a spot transaction.** Preserve a continuing cooperative contribution when the result depends on it.

### ECO.8:9 - Consequences

A practitioner can connect a local undertaking to wider economic activity without erasing the conditions of either. Some disagreements become clearer because they concern which relation applies. Coordinating commitments across these arrangements also takes work.

### ECO.8:10 - Architectural Rationale

Different coordination mechanisms allow participants to use their own knowledge and pursue distinct purposes. Identify the boundary from what the participants can obtain and do through each relation. A separate question is which operations form parts of the same work.

### ECO.8:11 - SoTA-Echoing

[Hayek, The Fatal Conceit, chapter 1, pp. 18–19](https://www.mrsmuellersworld.com/uploads/1/3/0/5/13054185/fatal_conceit_by_hayek.pdf) discusses simultaneous participation in overlapping local and extended orders. We adopt that distinction for the coordination question. Claims about the biological or moral origin of those orders would require other grounds.

Ostrom’s comparative work includes arrangements beyond market exchange and central command. Use ECO.7 when a shared constraint needs coordination. A common organizational plan can work where authority, knowledge and resources fit. Reconsider the affected answer when parties, rules, purposes or shared constraints change.

### ECO.8:12 - Relations

Use ECO.2 and ECO.3 for a response to changed prices or a new exchange, ECO.7 for shared-resource coordination and ECO.9 for the practice through which a rule works. FPF B.1.5 explains constituent and encompassing Methods, and C.36 supports cultural continuation. Use OCE or CGOV for a selected organizational or corporate change, and OPS for operating allocation.

### ECO.8:End

## ECO.9 - Decide Whether and How to Change Economic Rules through Their Working Practices

> **Type:** Method pattern
> **Status:** Stable

### ECO.9:1 - Problem frame

Use this Method to assess a rule for access, exchange, contributions or adaptation when someone questions how it works or proposes changing it. Identify which coordination the rule supplies in practice, whom it affects and what could change. If a new arrangement is needed, compare preserving, modifying or replacing that contribution under feasible transition conditions.

A finding about the current rule, a justified proposal or decision, a bounded trial, or an identified open condition can answer the task. When current evidence establishes urgent harm, identify what immediate protection is available under existing rights and authority.

### ECO.9:2 - Problem

An inherited rule may preserve locally useful knowledge that nobody has fully articulated. It can also perpetuate exclusion or a constraint that no longer serves its purpose. Changing the wording may leave the practice untouched. Removing the rule may also remove access, trust or a way to adapt that participants still need.

Judge the rule by its consequences and applicability to the present use. Its age or the fact that it was deliberately designed does not establish that result.

### ECO.9:3 - Forces

Recovering tacit know-how takes time, and delay can prolong harm. A trial may yield evidence while imposing real costs on participants. A local change can also affect other rules or be adopted under different conditions elsewhere.

### ECO.9:4 - Solution

#### ECO.9:4.1 - Recover the practice and the pressure for change

Establish what participants do, expect and can rely on. Compare the written rule with evidence of actual practice. For a proposed change, identify the difficulty, who experiences it and the intended improvement in access, supply, accountability or adaptation.

Recover the useful contributions and burdens of the existing rule. Use a representative observation or a sufficiently grounded reconstruction. Obtain participants’ accounts when the question depends on their experience or information they hold. An existing record can suffice for what took place under the rule.

#### ECO.9:4.2 - Construct alternatives with a viable continuation

When comparing changes, include the feasible option of retaining the rule, amending it or using another arrangement. For each relevant option, identify who can act, what must be learned or supplied, and how expectations, commitments, entry and exit would change. Include people affected during the transition, including those absent from the original proposal.

If a trial promises continuing service under uncertain demand, establish the work owed through completion. Include the number and timing of cases, ordinary operations, material exceptions and final settlement. Use qualified evidence about the procedure and the work, such as records and a knowledgeable performer’s account. For an assurance of completion, obtain a bound covering the agreed cases and exceptions. Compare obligations with available qualified capacity in each interval, including work due after enrolment closes. Use [OPS.13:4](https://github.com/ailev/FPF/blob/main/DPFs/Management%20DPF%20Suite/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md#ops134---solution) for this comparison. If the bound or capacity is inadequate, obtain more provision, agree a narrower undertaking with those affected or state which promise cannot be made.

Trace the other rules and practices the new arrangement requires. If some users lack a needed capability, service or resource, identify the resulting exclusion. When the task is to preserve access, supply the contribution or revise the proposal. Changing the text alone does not provide it.

Use C.36 to distinguish creating a variant, transmitting it, selection among variants and retention in repeated use. A project decision can change a local arrangement within its authority. Wider adoption depends on what later users receive and do.

#### ECO.9:4.3 - Choose the next action at the scale its grounds support

Compare attainable gains, transition burdens and costs of waiting. An established urgent failure can warrant an available protective action within the holder’s authority. If a change requires another party’s agreement, that condition still applies. A reversible trial can test an open question. Greater or irreversible exposure may require stronger grounds before commitment. Use C.11.DUA to assess whether further inquiry is worth its cost.

For a proposed change or trial, identify what evidence would support continuation, adjustment or withdrawal. Use ordinary records when they supply it. After implementation, examine the practice people can perform and whether a previous contribution was lost. Return a supported finding or, if repair is needed, address the affected rule, provision or capability.

### ECO.9:5 - Archetypal Grounding

#### ECO.9:5.1 - Replacing informal credit with advance payment

Suppose a cooperative shop lets trusted customers pay at their next visit and keeps a small account record. A proposed online system requires prepayment before collection. Under the example’s conditions this would reduce some collection work and exclude customers who can pay later but cannot prepay.

The useful service is short-term credit based on local knowledge. The cooperative compares universal prepayment with limited credit accounts. Its authorized manager can offer a two-week trial to ten consenting customers, including newcomers. A €20 limit per account fits the €200 available beyond other commitments. A trained worker has two hours per week. Using the agreed procedure and existing cases of late payment, disputed purchase and final settlement, the worker and manager establish a weekly upper bound of two hours for ten checks plus one hour shared across reconciliation, exceptions and final settlement. This bounds all the promised work at three hours in each week. It leaves open whether routine operation fits two. The manager is qualified and can reserve one contingency hour in each week, two hours in all. The worker checks the agreed payment date against expected receipts and unpaid purchases, applying the same conditions to newcomers and existing users.

The manager chooses the trial to retain later payment and test whether routine credit work fits the expected capacity. Existing obligations and terms for other customers continue. At weekly settlement, account records show overdue balances, and the worker can report time spent and any refused purchase. Extend the arrangement only if the weekly work fits the continuing two-hour capacity, the combined overdue balance is at most €20 and customers retain the intended access. If week one consumes three hours, the manager uses one contingency hour, stops new enrolment and reserves the remaining hour for week two, including final settlement. The ten customers keep the promised service. Expansion waits for enough continuing capacity or a less demanding procedure. If the promised workload cannot be bounded, change the undertaking or secure adequate provision before offering it as assured.

If the old arrangement also favours friends and excludes newcomers in the same circumstances, retaining it unchanged would fail the access purpose. The revised arrangement needs a workable way to assess new entrants. If that work cannot be supplied, identify it as the missing condition.

#### ECO.9:5.2 - Copying a rule without its supporting capability

A neighboring cash-only shop copies the credit software but lacks anyone who can interpret exceptions and maintain limits. It can continue the cash service. Credit remains unavailable unless it can obtain a capable performer, suitable simpler terms or another provider. The software copy establishes none of those contributions.

### ECO.9:6 - Bias-Annotation

A long-lived rule may no longer serve its users, and a new one may create fresh burdens. A successful local trial establishes what happened under its conditions. Include those who bear the transition when assessing its value and broader applicability.

### ECO.9:7 - Conformance Checklist

What does the current rule do, for whom and under what conditions? For a proposed change, can participants supply the learning, resources, authority and transition work it needs? If the proposal is a trial, do the stakes, remaining uncertainty and available capacity justify it? State the supported finding or how the parties can respond if a premise fails.

### ECO.9:8 - Common Anti-Patterns and How to Avoid Them

- **The old rule is irrational because its rationale is unknown.** Recover the consequential practice before discarding it.
- **The old rule survived, therefore it is justified.** Compare present benefits, harms and alternatives.
- **Publication of a rule is treated as capability.** Establish how participants can perform, learn or obtain the required methods.

### ECO.9:9 - Consequences

A change can preserve useful coordination while easing a burden or widening access. A desirable proposal may still lack a necessary capability. A sufficient current arrangement can be retained within its established conditions.

### ECO.9:10 - Architectural Rationale

Participants sustain coordination under a rule through what they do and what they expect others to do. A revised rule can enter into force while participants continue to follow the previous practice. To assess a proposed revision, identify how participants would receive it, act under it and continue the useful work.

### ECO.9:11 - SoTA-Echoing

Hayek’s *The Fatal Conceit* supplies a historical reason to examine what inherited coordination accomplishes. Whether to keep it depends on the present results, burdens and alternatives. [Baldwin and colleagues (2024)](https://onlinelibrary.wiley.com/doi/10.1111/psj.12518) examine the significance of context and long-term feedback in polycentric arrangements.

Use these questions with FPF’s account of cultural variation, transmission, selection and retention to compare arrangements in their setting. The constructed cases illustrate this reasoning. A claim of superior results needs appropriate comparative evidence. Reconsider a conclusion if practice, capabilities, wider effects or the grounds for retaining a rule change.

### ECO.9:12 - Relations

Use ECO.7 and ECO.8 when shared resources or the connection between orders motivates a rule question. Use C.36 for cultural continuation, HCD or MDPE for the relevant capability or practice, and OCE for a selected organizational change. Use C.11.DUA to assess the value and cost of further inquiry. Use OPS.13 to compare workload with provision when continuing obligations are promised in a trial or changed service.

### ECO.9:End

# Part IV - Efficiency and demand

## ECO.10 - Trace Efficiency Savings through Demand Responses (Rebound Effects)

> **Type:** Method pattern
> **Status:** Stable

### ECO.10:1 - Problem frame

Use this Method when a process or technology needs less resource per useful result and you want to understand total use. Identify the useful result, resource, boundary, period and comparison without the improvement. Trace any change in activity induced by the improvement.

Return a conditional or supported comparison of total use, or the output threshold relevant to it. For a fixed-output question, an engineering comparison can suffice under the stated output assumption. To apply that result to actual use, establish whether output and other material conditions were fixed.

### ECO.10:2 - Problem

Lower unit consumption can make a service cheaper, encourage more use, release spending for other activity or make a new use feasible. A response can offset part or all of an initial saving. If it more than offsets a positive fixed-output saving, the result is backfire, also called Jevons’s paradox.

Demand might have grown without the improvement. To attribute a later rise in use to the efficiency change, distinguish the induced response from other causes. Judge the consequence against the actual purpose, such as growth, access or keeping use below a cap.

### ECO.10:3 - Forces

Physical efficiency, price, demand and total use can refer to different activities and time scales. A threshold may answer a practical question while future output remains uncertain. Assess the cost and likely value of a broader demand investigation before commissioning it.

### ECO.10:4 - Solution

#### ECO.10:4.1 - State the comparison

Identify the useful result and choose a unit that preserves its performance. Specify the resource, activities included, period and comparison without the proposed improvement. Calculate cost, energy and emissions as distinct quantities, using a supported conversion if the question requires it.

Calculate three totals on the same resource account. Find use without the improvement, use with the improvement at the counterfactual output before any induced response, and use with the response. Subtract the second from the first for fixed-output saving. Subtract the second from the third for the response-induced change. Include relevant equipment, infrastructure and transition costs in the appropriate totals. A burden that arises at fixed output belongs in the second total as well as in the third if it continues. Use applicable PHY, MMP, OPS, MA or FIN results.

#### ECO.10:4.2 - Follow the responses that can change the answer

Establish how the improvement affects feasible action. Users may buy more, producers may increase output, released funds may support other work, or a new activity may become practical. Identify constraints such as price, capacity, time, access rules or a resource cap. Use a demand estimate that fits the mechanism claimed.

Distinguish resource use in the focal activity from consequential use elsewhere. Add effects within the declared boundary, count each once and state which remain uncertain. Consider new modeling, causal inquiry or measurement when it could materially improve the finding, choice or intended use at an acceptable cost.

For one unchanged service with resource use e per unit and output q, total use is e × q. Compare the improved total with total use in the counterfactual. Let q0 be counterfactual output and e0 and e1 the old and new unit resource requirements. If e1 > 0 and no other terms enter the account, equal total use occurs at q = q0 × e0/e1. This gives a break-even output under the assumptions. Demand at that output is a separate question. When other terms matter, compare the full totals.

#### ECO.10:4.3 - Return the consequence to the actual purpose

State whether use with the response is below, equal to or above use without the improvement. When the fixed-output saving is positive and well defined, divide the response-induced change by that saving if the requested result needs the fraction offset. A fraction above one indicates backfire under this account. When there is no positive, well-defined fixed-output saving, report the totals and induced change directly. Identify the accounting boundary, since including new equipment or transition can change both the saving and the percentage.

For a resource cap, assess whether aggregate use remains within the limit and whether released capacity needs allocation. If the goal is useful growth, compare the additional output’s value and cost. For a proposed policy, assess feasibility and effects on the parties concerned. A rebound estimate can inform those choices.

Return the supported total-use finding, its assumptions and any material unknown. If the task asks for a choice or operating limit, compare the feasible responses and state which conditions matter to that result.

### ECO.10:5 - Archetypal Grounding

#### ECO.10:5.1 - Half the energy per unit

Suppose production without the improvement would be 100 equivalent units at 2 kWh each, using 200 kWh. The improved process uses 1 kWh per unit, so at the same output it would use 100 kWh and save 100 kWh.

At an induced output of 150 units, total use would be 150 kWh, a saving of 50 kWh against the 200 kWh counterfactual. The added demand would offset 50% of the 100 kWh fixed-output saving. At 220 units, total use would be 220 kWh, a net saving of −20 kWh and a 120% offset. That is backfire. At 200 units the old and new totals are equal.

Now suppose that without the improvement output would already have risen to 180 units. The comparison totals for 220 improved units are then 360 kWh without the improvement, 180 kWh with it at fixed output and 220 kWh with the response. The extra 40 kWh offsets about 22.2% of the 180 kWh fixed-output saving. An observed rise from last year’s 100 units to 220 would not by itself identify either the counterfactual or backfire.

Return to the case with 100 units of output without the improvement. Include 150 kWh for new equipment and transition in the same period. These costs arise at any output with the improvement and are absent without it. If output with the improvement reaches 150 units, the three totals are 200, 250 and 300 kWh. Fixed-output saving is 200 − 250 = −50 kWh. The response adds 300 − 250 = 50 kWh and total use rises by 100 kWh. The process still saves operating energy per unit. On the broader account there is no positive fixed-output saving from which to calculate a fraction offset.

#### ECO.10:5.2 - An AI task becomes cheaper

Suppose a firm lowers the cost per accepted analysis and considers additional analyses. Establish which output is comparable, including acceptance and any required human revision or quality. Compare costs and resource use per accepted result, feasible volumes and the value to the work that receives them. Token count alone need not represent an accepted analysis.

If unit cost falls, the same expenditure may buy more useful analyses. Spending the full budget, using more electricity and using more hardware are separate consequences. Establish each from the corresponding resource account.

### ECO.10:6 - Bias-Annotation

A dramatic paradox can replace a causal account. Engineering optimism can assume fixed demand without saying so; pessimism can assume unlimited expansion. Preserve both the technical gain and the conditions of its economic response.

### ECO.10:7 - Conformance Checklist

Identify the useful result, resource, boundary, period and counterfactual. State the mechanism assumed for each induced response and what the evidence supports. Check the totals, any saving-offset percentage and the result for the stated purpose. Distinguish the consequences of stipulated scenarios from an observed causal effect.

### ECO.10:8 - Common Anti-Patterns and How to Avoid Them

- **A unit saving is reported as a total saving.** Carry it through the relevant volume and other induced uses.
- **Every subsequent increase is called rebound.** Compare with what would have happened without the change.
- **Backfire is assumed for every efficiency gain.** Find the attainable response and its constraints.
- **A carbon, energy or cost figure changes meaning mid-calculation.** Keep each total and its conversion grounds separate.

### ECO.10:9 - Consequences

A comparison can preserve the engineering gain while showing the demand response and total resource consequence. A break-even threshold may settle a question about a bounded trial or operating limit. Report broader effects conditionally when the evidence does not support a precise rate.

### ECO.10:10 - Architectural Rationale

Physical input per useful result supplies one term in the economic account. The improvement can change feasible uses and actual demand, while other causes can change demand independently. Distinguish those effects to interpret total use for the receiving purpose.

### ECO.10:11 - SoTA-Echoing

[Brockway and colleagues (2021)](https://eprints.whiterose.ac.uk/id/eprint/171952/) compare evidence and models for economy-wide energy rebound. Their estimates depend on the scope and assumptions of the studies. The [FAccT 2025 analysis of AI rebound](https://facctconference.org/static/docs/facct2025-206archivalpdfs/facct2025-final37-acmpaginated.pdf) identifies possible AI demand responses and limits on attributing changes to efficiency.

Use the mechanism and boundary analysis at the level of detail the question requires. A fixed-output engineering calculation can suffice for a fixed-output question. Use a broader economic model when additional responses matter to the resulting finding or decision and the assumptions fit. Reassess the affected result when performance, demand, access, prices or the resource boundary changes.

### ECO.10:12 - Relations

Use ECO.2 for price responses, ECO.3 for newly attainable exchanges and ECO.7 or ECO.9 for a selected shared-resource or rule question. Use PHY or MMP for models, OPS for flow and capacity, and MA or FIN for financial and cost comparisons. Use FPF choice or portfolio Methods if the receiving task requires a choice among alternatives. ECO.10 supplies the demand-response contribution to that comparison.

### ECO.10:End
