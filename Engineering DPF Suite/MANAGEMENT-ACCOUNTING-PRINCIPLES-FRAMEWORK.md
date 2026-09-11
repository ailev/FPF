# Management Accounting Principles Framework

**Edition:** [MA 1.0](#edition-record)

**Author:** Anatoly Levenchuk, with AI-assisted development and review

Management Accounting helps a controller, accountant or manager explain how work uses resources and how that use appears in money, forecasts and performance accounts. Begin with the decision or account that needs a better explanation. A small model of the relevant work can be sufficient.

# Table of Contents

**Reader entry**

| § | Publication unit | Use |
| --- | --- | --- |
| R | [Management Accounting Readme](#management-accounting-readme) | Select a first question and obtain a useful result. |
| P | [Preface](#preface) | Understand the connected methods, alternatives and limits. |

**Patterns**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| --- | --- | --- | --- | --- |
| 1 | [MA.1 - Build the Resource-Consumption and Cost Model](#ma1---build-the-resource-consumption-and-cost-model) |  | Resource demand; setup; additional order; cost model detail | OPS.14 uses the model; OPS.15 supplies needed account definitions. |
| 2 | [MA.2 - Explain the Cost and Use of Capacity](#ma2---explain-the-cost-and-use-of-capacity) |  | Paid and usable capacity; reserve; released hours; payment savings | MA.1 for missing demand; OPS for the operating capacity decision. |
| 3 | [MA.3 - Assign Shared Costs for the Stated Use](#ma3---assign-shared-costs-for-the-stated-use) |  | Shared cost; allocation; segment closure; tracing | MA.1–2 for resource meaning; OPS.14 for a closure comparison. |
| 4 | [MA.4 - Reconcile Operating, Reporting and Cash Accounts](#ma4---reconcile-operating-reporting-and-cash-accounts) |  | Profit versus cash; inventory; receivables; reporting bridge | MA.1–3 and OPS.15; applicable reporting rules. |
| 5 | [MA.5 - Construct and Update an Operating Forecast](#ma5---construct-and-update-an-operating-forecast) |  | Demand outlook; scenarios; supply threshold; forecast update | MA.1–4 for assumptions; MA.6 for conflicting number uses. |
| 6 | [MA.6 - Separate Forecasts, Targets and Resource Requests](#ma6---separate-forecasts-targets-and-resource-requests) |  | Expected, targeted, requested and authorized; budget bias | MA.5 for the expectation; MA.1–2 for resource conversion. |
| 7 | [MA.7 - Explain a Cost or Margin Difference](#ma7---explain-a-cost-or-margin-difference) |  | Variance; mix; volume; usage; price; causal explanation | MA.1–4 for comparable meanings; the relevant response method. |
| 8 | [MA.8 - Account for Customer and Product Economics Over Time](#ma8---account-for-customer-and-product-economics-over-time) |  | Cohort; acquisition; retention; support; scale; time horizon | MA.1–5; FDM for missing financial terms; finance for valuation. |
| 9 | [MA.9 - Examine the Behavioral Effects of an Account](#ma9---examine-the-behavioral-effects-of-an-account) |  | Unit-cost target; inventory building; hidden forecast; incentive | MA.1–8 for consequences; OCE for a wider organizational change. |

# Management Accounting Readme

## Practical entries

These are selected entry examples, not a catalogue or a coverage boundary. Bring the actual accounting question. Use the index or a direct pattern when no example fits, and use an adequate existing account when it already answers.

**MA** is the reference code for this framework. In MA.4:5, 4 identifies the pattern and 5 its section. The index gives publication order, not a required order of work.

### MA-E1 — An order is priced below reported average cost

- **Situation:** A proposed order looks loss-making in the standard report, but its actual resource requirements and payment consequences are unclear.
- **Question:** What resources and money would this work require under the available arrangement?
- **First useful result or honest blocker:** A sufficient resource-consumption and cost model, or the specific dependency or capacity premise still missing.
- **Start with:** [MA.1](#ma1---build-the-resource-consumption-and-cost-model).
- **Stop or return:** Supply adequate quantities and conditions to OPS.14 for the comparison. Return an unresolved operating schedule, financial term or funding question to the practice that can settle it.

### MA-E2 — Profit and cash movement disagree

- **Situation:** A positive reported result appears alongside a cash shortfall.
- **Question:** Which inventory, recognition and settlement differences explain the two accounts?
- **First useful result or honest blocker:** A reconciled explanation retaining each account's meaning, or a located event or policy discrepancy.
- **Start with:** [MA.4](#ma4---reconcile-operating-reporting-and-cash-accounts).
- **Stop or return:** Use the account required by the receiving decision. An actual funding question needs the whole timed cash position.

### MA-E3 — The forecast has become a resource negotiation

- **Situation:** A team is expected to report one number as its demand outlook, target and request for resources.
- **Question:** What does each number mean, and which decision would resolve the consequential gap?
- **First useful result or honest blocker:** Distinguishable expectations, ambitions, requests and authorizations on an adequate comparison basis.
- **Start with:** [MA.6](#ma6---separate-forecasts-targets-and-resource-requests).
- **Stop or return:** Keep the expectation visible and obtain the relevant management or resource decision. A revised forecast does not itself grant resources.

# Preface

## MA.Preface:1 - The working problem

A controller is asked whether another order is worthwhile. The report supplies a cost per unit, but the order needs a setup, qualified staff and perhaps an extra machine block. The unit cost does not explain those dependencies. Elsewhere, a manager sees profit rise while cash falls, or receives a demand forecast that has been negotiated to match a spending ceiling.

Management Accounting serves these internal accounts and their uses. Its central work is to construct and interpret the relationships between work, resources, money, expectations and measured performance. The resulting account can support a decision, explanation or inquiry. The decision itself retains the criteria and authority of the responsible operating, financial or management practice.

An account's purpose matters. A required external statement, a resource-consumption model and a timed cash account can all be correct while carrying different amounts. The aim is to supply the account the receiving use needs and preserve its relationship to the other valid views.

## MA.Preface:2 - How the methods connect

MA.1 constructs the resource-consumption and cost model when it is missing. It begins with work outputs and consequential resource dependencies, then relates quantities to supply, money and payment time. It also chooses detail: an interval can suffice when its variation cannot change the relevant threshold or comparison.

MA.2 and MA.3 are independent entries when capacity or shared assignment is the unresolved problem. Their results can improve MA.1's model, but neither is a mandatory stage in every model construction. MA.4 reconciles operating, reporting and cash accounts after their subjects and rules are known.

MA.5 uses adequate demand, resource and monetary relationships to forecast the relevant outlook. MA.6 preserves its distinction from targets and resource decisions. MA.7 explains a difference without treating arithmetic decomposition as causal evidence. MA.8 extends the account through customer or product time, and MA.9 examines what an account's actual use encourages people to do.

These methods can be used in different combinations. An established model can feed a forecast directly. A surprising variance can lead to a revised dependency or reveal a changed allocation. A harmful unit-cost target can require changing its use while keeping the report needed for another purpose. Enter the unresolved question and stop when the receiving use has an adequate result.

## MA.Preface:3 - A model that changes the next decision

In MA.1's constructed test-order case, 100 accepted units require 26–29 rig-hours. The supplied arrangement has 20 usable hours and one additional ten-hour block costing 240. Materials and supplier use add 300. The model therefore supplies 540 of additional payments, rather than the report's 1,500 assigned cost.

OPS.14 uses those quantities and the stated absence of displacement to compare the 1,200 receipt with 540, giving 660. Its funding question uses the whole timed cash position. Under the example's explicit baseline-cash premise, 440 is paid now, 100 is due on day 7 and the receipt arrives on day 28; a 40 day-7 funding gap remains. The favorable comparison and the unresolved funding are both useful results.

Other entries change different actions. MA.4 explains how inventory and receivables connect profit to cash. MA.6 preserves an expectation of 100, ambition of 120, request for provision covering 130 and authorization covering 110. MA.8 distinguishes the recovery of a past acquisition payment from a new continuation choice. A reader does not have to reconstruct the order model to use these methods.

## MA.Preface:4 - Correct use, evidence and effort

Begin by stating what the account must explain. For a connected use of the language, establish that the chosen methods answer that question, that their resource and monetary meanings agree where they connect, and that material time, uncertainty and supply conditions survive the connection. Use each pattern's substantive questions for the result it supplies; reopen the conditions changed by the current use.

A recognizable discrepancy is a reason to investigate. It is not proof that a proposed order should be accepted, that an allocated cost is avoidable or that a measure caused behavior. The worked examples establish reasoning under supplied facts. An actual conclusion needs adequate support for its resource relationships, terms, observations and causal claims.

The gain is a smaller and better explained next decision. The cost is obtaining and maintaining the facts the account needs. Reuse adequate models and observations. Increase detail where a plausible difference could change the answer or its required assurance.

A commercial example supplies no universal monetary objective. An internal or public service can use these accounting methods while obtaining its intended result and choice criteria from the responsible practice. Forecast and performance arrangements must also be examined from the affected participants' positions, rather than assuming a single account expresses every interest.

## MA.Preface:5 - Why this organization of methods

The language separates quantity construction, monetary interpretation, comparison and evidence because a failure in one cannot be repaired by precision in another. Multiplying a reported rate more accurately cannot recover a missing setup. A reconciled variance cannot establish its cause. A forecast cannot authorize a resource request.

OPS.14 already supplies the operating comparison, including changed flows, displacement, timing and funding. OPS.15 supplies account definitions and source events. MA therefore supplies the missing accounting construction and interpretation instead of introducing another comparison or observation method under a new name.

A stable simple report is adequate when it preserves the distinctions its use needs. A detailed activity model, forecast system or broader Beyond Budgeting arrangement becomes useful when its additional contribution warrants the effort. The alternative to an inadequate report can be a small supported model; the alternative to a misunderstood forecast can be a clarified use rather than a replacement management system.

## MA.Preface:6 - Sources, qualifications and changed conditions

Internal and externally required accounts serve different uses. An account must retain capacity thresholds and the acquisition or scale assumptions that change its resource and monetary consequences. Changing an expectation is distinct from deciding about resources. Cost models remain useful when their meaning fits the receiving decision. Revenue uncertainty calls for warranted scenarios; unit economics, ROI and ROMI need their actual definitions and cannot be treated as interchangeable labels.

IMA's managerial-cost-model guidance contributes resource dependencies and a use-driven choice of model detail. Bragg and Caspari supply historical constraint-accounting cases that expose the difference between assigned cost, capacity and changed payments. The relevant TameFlow capacity distinctions are used with adequate OPS operating results; elapsed flow time alone does not identify the constraint.

Bogsnes and the continuing Beyond Budgeting principles shape MA.5–6's separation of expectation, ambition and resource allocation. The wider organizational proposal is an alternative whose value depends on the actual problem. The customer-model sources used in MA.8 qualify population, horizon and continuation assumptions. Their contribution is to avoid an unwarranted universal formula, not to require every account to adopt one predictive model.

Use the source qualifications in the relevant pattern when adapting its method. Reopen an affected account when actual resource behavior, contract terms, reporting rules, population or decision use changes.

## MA.1 - Build the Resource-Consumption and Cost Model

**Type:** Architectural

### MA.1:0 - Use this when

Use this pattern when a cost report cannot explain what a proposed order, changed method or different workload would require. A quote below reported average cost, a claimed labor saving or a sudden rise in unit cost can expose this difficulty. Start by identifying the resource dependency that the existing account leaves unanswered.

The pattern governs a model relating work outputs to resource consumption and monetary amounts for a stated use. Its useful result is enough of that model to explain the relevant quantities, capacity conditions and money. The operating decision can then use [OPS.14][OPS] to compare options.

If an existing model already supplies adequate quantities and conditions, use it. Rebuilding the whole cost system adds no value to a question that an adequate account can already answer.

### MA.1:1 - Problem frame

A service can use a machine, qualified staff, consumables and a supplier's processing service to deliver one accepted result. Each resource has a different relationship to the work. The machine is occupied during setup and processing; staff may supervise only part of that time; consumables may be used on unsuccessful attempts as well as accepted units. A supplier may charge for an attempt, a completed batch or a reserved block.

The money follows further relationships. Stock consumed today may have been paid for last month. Salaried capacity may be available within unchanged pay. Another machine block may require a payment before the customer pays. An internal unit-cost report may also assign a share of the building and management costs. These amounts can all be meaningful while answering different questions.

Management accounting needs an explanation connecting those facts. The relevant boundary follows the work, resource behavior and receiving use; it need not coincide with the chart of accounts or an organizational department.

### MA.1:2 - Problem

A monetary total compresses the relations needed to explain a change. Multiplying average cost by a proposed quantity can miss available capacity, a setup, failed attempts or a supply threshold. It can also turn an allocation into an apparent payment consequence.

A model that contains every observable detail has the opposite defect: it costs too much to construct and maintain, while its precision may exceed what the underlying observations support. The working problem is to recover the dependencies that can change this answer and stop at a justified level of detail.

### MA.1:3 - Forces

Consumption, available capability and payment are connected but need different evidence. The person who supplies a credible processing-time estimate may not know the supplier's charging terms or the actual payment date. Bringing these facts together is useful even when each is already recorded elsewhere.

Grouping resources makes an account usable. It loses value when the group hides a capability requirement, a different response to demand or a payment threshold. More detailed observation can reduce a consequential uncertainty, but detailed tracking itself consumes resources and can encourage people to optimize what is easiest to count.

### MA.1:4 - Solution

#### MA.1:4.1 - Begin with the missing explanation

State the work being considered, the relevant result and the period over which the model must answer. Inspect the existing account with its user. Ask what it cannot presently explain: the resources required for another order, the effect of a changed batch size, the cost of unused provision or some other concrete dependency.

Use that question to choose the first observations. For a proposed order, obtain the actual processing route and the conditions under which it works. For a reusable product-cost account, obtain representative routes and the variation the account must retain. Ask the people who perform or arrange the work, and compare their explanation with available operating records. A ledger category locates recorded money; it does not by itself explain how the work consumes a resource.

#### MA.1:4.2 - Recover outputs and resource dependencies

Identify the accepted outputs and the intermediate results that materially consume resources. Recover setups, attempts, rework, inspection and handling where their resource demands differ. Distinguish quantities of accepted results from quantities of attempts: a charge on every processing attempt will not generally equal a charge on every accepted output.

For each relevant resource, express the dependency in meaningful units. A simple relationship may be:

> Required rig-hours = setup hours + processing attempts × rig-hours per attempt.

Other resources can require a table, interval, threshold or conditional rule. A one-time setup, a resource shared by simultaneous tasks and a failure-dependent repeat are not all linear per-unit demands. Preserve the conditions under which each relationship holds, including product type, qualification, batch size or equipment state when these matter.

Establish the reason for the relationship. Engineering knowledge, applicable terms and observations of the process can support different parts of it. Mark an estimate as an estimate and retain the assumption that makes it usable. An observed association between order value and staff expense may help prediction; it does not establish that an extra currency unit of sales consumes a particular staff quantity. When that distinction changes the decision, investigate the mechanism or return the missing dependency.

#### MA.1:4.3 - Keep resource quantities and supplied capacity distinct

A rig-hour, a qualified staff-hour and an elapsed hour measure different things. Recover what each resource must actually provide. Check that an estimate of machine occupation has not silently become an estimate of staff attendance.

Group resources only while the grouping preserves relevant capability, consumption and money. Two machines can share a pool if their interchangeable capability and behavior suffice for this use. A specialist machine that alone performs a required test needs its own boundary. Likewise, splitting identical consumables by invoice number may add detail without improving the answer.

Compare demand with the supplied capacity conditions for the required time window. Retain commitments to other work, unavailable time and protected reserve. Keep thresholds such as an additional shift, license tier, supplier block or specialist booking visible. Obtain an adequate operating result when feasibility, the constraint or the schedule is unresolved; the cost model uses that result rather than establishing a feasible schedule from a total number of hours. [MA.2](#ma2---explain-the-cost-and-use-of-capacity) deepens the account when the meaning or cost of capacity itself needs explanation.

#### MA.1:4.4 - Attach the relevant monetary meanings

Connect resource quantities to money through the relationship that actually applies. For each amount that could be misread, make clear whether it is:

- consumption valued for the account, such as materials issued from stock;
- the payment required to supply or obtain a resource, such as a whole additional shift;
- a payment at a particular time; or
- an assigned share under an allocation convention.

The distinction can be carried in ordinary columns or explanatory prose.

A supplied resource can be consumed without another payment in the period. Record the capability used and the account's warranted value without inventing a cash saving or expenditure. Conversely, obtaining a resource block may require paying for more capacity than the proposed work consumes. Use the charging rule for that block. An average rate multiplied by consumed hours does not reproduce every supply arrangement.

Preserve the horizon. A salaried hour whose payment is unchanged this week can still matter to a later staffing decision or to displaced work now. Stock consumption can trigger a replacement payment, use scarce inventory or have another relevant consequence even though the original purchase is sunk. Obtain those facts for the receiving comparison instead of classifying a cost as permanently fixed or variable.

When a shared assignment is the unresolved issue, use [MA.3](#ma3---assign-shared-costs-for-the-stated-use). When management, reporting and cash amounts appear inconsistent, use [MA.4](#ma4---reconcile-operating-reporting-and-cash-accounts). These are separate questions that can also be answered from adequate existing accounts.

#### MA.1:4.5 - Choose the detail that can change the answer

Ask which plausible differences could change feasibility, a payment threshold, the comparison or the assurance needed for this use. Split a resource group or obtain another observation when such a difference is concealed. Preserve a justified range when all values in it support the same relevant conclusion.

For example, a setup estimate of six to nine hours may be sufficient if every value requires exactly one additional ten-hour block and fits the supplied arrangement. Measuring setup to the minute adds little to that choice. If the estimate straddles the available capacity, its uncertainty matters: obtain a better bound, change the option or report unresolved feasibility.

This stopping rule applies to the stated use. A model sufficient for one order can be inadequate for a pricing policy, capital decision or assurance claim with a longer horizon. Reuse the established relations, then deepen only the part the new use needs. [C.11.DUA][DUA] supplies the broader inquiry decision when the value of further information is itself disputed.

#### MA.1:4.6 - Return a model someone can use

Return the quantities and dependencies together with the conditions needed to interpret them. A short table can be enough. Make an unresolved premise visible at the point where it changes the result: required qualification, available block, rework rate, supplier terms or another specific issue.

For an operating option, supply the resource and monetary consequences to OPS.14. That method compares options, considers displacement and tests timing and funding. A favorable difference is a result of the comparison under its premises; building the model does not authorize the work or supply missing capacity.

Retain the observations worth reusing and the conditions that would reopen the account. Actual use of a different process, changed terms or a new demand range can require a revision.

### MA.1:5 - Archetypal Grounding

#### MA.1:5.1 - A test order below reported average cost

A test service considers an order for 100 accepted units at 12 currency units each. Its standard report assigns an average cost of 15 per unit. The manager first needs the resource model; the comparison follows from it. The following is a constructed case with supplied operating and contractual facts.

The resource owner supplies an adequate schedule, qualification and reserve account. There are 20 uncommitted usable rig-hours in the required window. Exactly one additional contiguous ten-hour block can be obtained for 240, subject to booking. Setup requires six to nine rig-hours, followed by 0.2 rig-hours per processed unit. One successful attempt per accepted unit is assumed.

The work requires 14 qualified staff-hours; 16 usable hours are already available and pay is unchanged. Materials for this order must be bought now at 2 per unit. A supplier charges 1 per processed unit.

| Recovered dependency | Quantity or amount | What the receiving comparison can use |
| --- | --- | --- |
| Setup plus processing occupies the rig. | 6–9 + 100 × 0.2 = **26–29 rig-hours**. | The supplied 20 hours are insufficient; one extra ten-hour block makes the supplied arrangement adequate. |
| Qualified staff support the work. | **14 staff-hours** within the supplied 16. | The option uses capability, with no additional wage payment under these terms. |
| Materials are consumed and purchased for the order. | 100 × 2 = **200**. | A payment of 200 now. |
| The supplier charges per processing attempt. | 100 × 1 = **100**. | A payment of 100 under the one-attempt premise. |
| Extra rig capacity is sold as one block. | **240** for the ten-hour block. | A payment of 240, although the extra occupation is only six to nine hours. |
| The existing report assigns average cost. | 100 × 15 = **1,500**. | A reported amount whose assignment basis remains available for its own use. |

The model supplies **540** in additional payments. OPS.14 compares the 1,200 receipt with those payments: the difference is **660**, over a horizon that includes both, with all other flows unchanged and no displaced contribution. The reported 1,500 does not establish this incremental amount.

Payment time changes what is feasible. Without the order, unrestricted cash available for these payments would remain **500 through day 28 after all other receipts and obligations**. Materials and the block require 440 now, leaving 60. The supplier's 100 is due on day 7; the customer pays on day 28. There is therefore a **40 funding gap on day 7**. The operating or finance decision must resolve that gap before treating the option as funded.

If an additional receipt of 50, unchanged between accepting and declining the order, instead arrives before day 7, cash after both payments is **10**. The order's incremental difference remains 660. The unchanged receipt cancels from that difference but changes the whole cash position used to establish payment feasibility.

The setup interval is sufficient for the one-block question: 26–29 hours always lies within the supplied 30. A new product requiring an eleven-hour setup would require **31 hours**. That case reopens feasibility and the resource model; the earlier result cannot be extended by merely changing the sales quantity. Failed attempts, different staff qualifications or changed supplier terms likewise require attention where they affect the dependencies.

#### MA.1:5.2 - A faster method with unchanged wages

A repair method reduces salaried technician attendance from six hours to four for one job. The two released hours become usable capability if the schedule and qualification allow their use. Pay this week remains unchanged.

The model returns the two-hour reduction and the unchanged payment. If another valuable job can use the released time, OPS.14 can compare the resulting options. If no work is displaced and no payment changes, the model provides no current cash saving. For a later staffing question, construct the relevant demand and supply relationship over that later horizon.

### MA.1:6 - Bias-Annotation

An accountant may favor categories already present in the ledger; an operator may favor the resource easiest to observe. Both can miss the relation that changes the answer. Compare their accounts around the actual work and keep different units explicit.

The order example concerns a commercial service and a short horizon. Its arithmetic does not establish that profit is every organization's purpose or that all long-run choices can be made from short-run payments. Public and internal services can use the same construction to explain required resources while obtaining their objectives and decision criteria from the responsible practice.

### MA.1:7 - Conformance Checklist

For the model's stated use, examine whether:

1. The work, output and horizon are clear enough to choose the relevant dependencies.
2. Attempts, setups, resource units and capability boundaries are retained wherever they can change the answer.
3. The relationships have adequate support, with material estimates and unresolved assumptions identifiable.
4. Capacity conclusions use an adequate supplied operating account, including commitments, reserve and relevant thresholds.
5. Consumption values, supply payments, timing and allocations can be distinguished where their meanings affect use.
6. The chosen detail preserves the consequential variation, and the returned result names any premise still needed by its recipient.

A plausible entry cue establishes a reason to inspect the account. These questions assess the model and its warranted use; observing actual consumption, obtaining a resource and achieving the business result require their own evidence.

### MA.1:8 - Common Anti-Patterns and How to Avoid Them

**Rejecting an order from the average-cost multiplication alone.** Recover what changes when the order is undertaken, including the capacity and payment conditions. Keep the original report's meaning available.

**Valuing every released hour as an avoided wage payment.** State the released capability and the action, if any, that changes payment or displaced work. An unchanged salary cannot be saved merely by assigning it fewer hours.

**Refining a harmless decimal while concealing a threshold.** Preserve the supply block or qualification boundary first. Add measurement detail only where its plausible variation can change the use.

**Using paid capacity as proof of timely availability.** Obtain the actual usable and committed capacity for the required window. Payment for a resource does not establish the schedule.

### MA.1:9 - Consequences

The user can explain why a proposed workload consumes particular resources and why its monetary consequences differ from a report. The result supports a small first decision and can be extended when another use needs more detail.

The model also exposes missing operational or contractual facts that accounting categories previously concealed. Recovering those facts has a cost. Keeping only consequential detail reduces maintenance, while explicit conditions make later reuse more demanding than copying a single unit-cost number.

### MA.1:10 - Architectural Rationale

The construction begins with work and quantitative dependencies because a money total cannot recover a lost capability requirement or setup. Monetary interpretation follows the relevant resource relation. This order also lets an existing operating account supply a sufficient quantity directly.

A report based on a stable average can be adequate for the question it was designed to answer. Replacing it is justified when its aggregation conceals an answer-changing relation. A comprehensive activity model can support repeated heterogeneous decisions, but its collection and maintenance burden is unnecessary for a small case whose decisive relations are already known.

Keeping the model separate from the option comparison makes both usable independently. The same model can support a forecast or variance explanation; the same comparison method can use an already adequate model. A longer horizon or different decision changes the needed relationships rather than making one cost label universally correct.

### MA.1:11 - SoTA-Echoing

The practical question is how much resource and monetary structure an internal account needs to support its use. The selected line combines causal management-cost modeling with the constraint-accounting distinction between consumed capability and payments. It adapts IMA's [Developing an Effective Managerial Costing Model][IMA2019]: model resources and their quantitative dependencies, distinguish their monetary treatment, and choose sophistication for the decision. Here those contributions change the construction and detail decision in §§4.2–4.5.

At the effort of recovering a few consequential relationships, this line can distinguish the extra capacity block from a reported average that obscures it. A detailed activity or time-driven model becomes preferable when repeated decisions need the distinctions it supplies and their maintenance is worthwhile. Its use still needs adequate capacity and monetary premises.

Bragg's *Throughput Accounting* (2007), printed pp.44–47 and 84–86, supplies historical examples and assumptions behind short-run comparisons. The pattern retains their attention to changed payments and capacity, while including supplier charges, setup supply and other changed flows when actual terms require them. Caspari and Caspari's *Management Dynamics* (2004), printed pp.1–11, supplies the counterexample in which local time reduction need not improve the constrained system or reduce wages. These sources inform the returned quantities and the faster-method case.

Reconsider the model when observed work, relevant terms or the receiving use defeats its dependency, capacity or detail assumptions. A newer cost-model label alone is not evidence that a more elaborate account would answer the question better.

### MA.1:12 - Relations

[OPS.14][OPS] consumes adequate resource quantities, monetary consequences and conditions for its incremental comparison. The relevant OPS capacity and scheduling methods supply an unresolved operating result. [OPS.15][OPS] supplies operating-account definitions and source events where those are missing.

MA.2 explains capacity use and its cost; MA.3 resolves shared assignment; MA.4 reconciles differing accounts. MA.5 can reuse the dependencies in a forecast, MA.7 in a variance explanation and MA.8 in a cohort or product account. Each is entered for its own unresolved question.

[C.16][MEAS] supplies measurement discipline when a quantity's meaning or evidence is disputed. C.11.DUA supplies the inquiry decision when further information could change the action.

### MA.1:End

## MA.2 - Explain the Cost and Use of Capacity

**Type:** Architectural

### MA.2:0 - Use this when

Use this pattern when paid capacity, used capacity and apparently idle capacity have been treated as the same thing. A proposed efficiency saving, staff reduction or extra workload often exposes the difference.

The pattern governs an account of resource supply, usable capability, its use and its monetary consequences. It returns an explanation of what is available, what is used or reserved, and what action could change supply or payments.

Use an adequate capacity account directly. The operating choice about the constraint, reserve or feasible schedule belongs to the relevant [OPS][OPS] method.

### MA.2:1 - Problem frame

A team pays for a resource arrangement that supplies capability over time. Some provision can be unavailable for the relevant service; some usable capacity can support actual work; some can protect the service against variation. A remaining unused portion may offer another use or a possible supply change.

These quantities do not have one monetary meaning. Released time can increase available capability without changing the current payment. A supply reduction can save money while also removing capacity needed in another time window.

### MA.2:2 - Problem

An account that prices every unused hour as waste invites a reduction that may damage service. An account that treats every paid hour as available can promise work the resource cannot perform.

The working difficulty is to explain both use and monetary consequence without making an accounting classification decide the operational question.

### MA.2:3 - Forces

A simple utilization ratio is easy to communicate. Its denominator can hide unavailability, capability differences and reserve. A very detailed capacity account can become expensive while still failing to establish a feasible schedule.

A reserve consumes an opportunity to use capacity elsewhere. Its reason and size require an operating judgement; calling it protective cannot by itself justify keeping it indefinitely.

### MA.2:4 - Solution

#### MA.2:4.1 - Define the resource and relevant capacity quantity

Name the resource arrangement, capability, time window and receiving question. Recover the supplied quantity, the unit and the conditions under which it can serve the relevant work. Distinguish staff attendance, machine occupation and elapsed time.

Use the current operating account for availability, commitments and reserve. If those results are disputed, obtain the missing OPS result before attaching a monetary conclusion to them.

#### MA.2:4.2 - Explain the supplied, used and unused portions

Reconcile the supplied quantity with its relevant uses and restrictions. Identify unavailable or differently committed provision, actual or expected consumption, protected reserve and any remaining unused usable capacity. Keep the categories mutually interpretable for this account; reserve can be part of available capacity while being unavailable for ordinary commitment.

Investigate the reason for an apparently idle portion. It may reflect demand variation, a necessary skill mix, downtime, a minimum supplier block or inadequate demand. Preserve a disputed explanation as disputed. A utilization label is an entry cue, not a causal diagnosis.

#### MA.2:4.3 - Connect a capacity change to a supply action

Ask what action would change resource supply and on what terms. Recover notice periods, minimum blocks, alternative uses and consequential payments for the stated horizon.

A saved hour can be used elsewhere if capability and scheduling permit it. A payment saving requires an avoided or reduced payment within the stated horizon. A smaller assigned share of unchanged payroll establishes neither.

Retain the threshold. Removing five hours of work may leave the same supplied shift; adding five can require another whole block. [MA.1](#ma1---build-the-resource-consumption-and-cost-model) supplies a missing demand model.

#### MA.2:4.4 - Return the capacity and monetary account

Return the quantities, reasons and relevant supply options with their limits. If a unit cost is useful, state its denominator and purpose. Dividing the same payment by supplied, used or productive hours gives different rates.

Supply the supported quantities and payment conditions to OPS for the capacity or incremental decision. Keep uncertainty about the operating reserve separate from uncertainty about a supplier's terms.

### MA.2:5 - Archetypal Grounding

A service purchases 100 scheduled qualified staff-hours for 2,400 in a period. An adequate supplied operating account identifies 20 hours unavailable for the service, 50 used on service work, 10 held as justified reserve and 20 otherwise unused usable hours. The account reconciles **20 + 50 + 10 + 20 = 100**.

Dividing 2,400 by all 100 supplied hours gives 24 per supplied hour. Dividing it by the 50 service hours gives 48 per used service hour. Neither division establishes the payment avoided by releasing another hour.

A changed method releases two service hours. Pay remains 2,400 under the arrangement. The result is two hours of released capability, subject to their actual usefulness in the schedule. Multiplying two by 24 or 48 does not establish a cash saving.

Consider an extra request under the original arrangement, before the method change. It needs 25 hours in the same window. The supplied operating account permits ordinary commitment of only the 20 unused hours while retaining the reserve. A feasible additional block of 20 hours costs 500 under the supplied terms. The model returns the five-hour gap and the block's payment, or the question whether OPS should change the reserve or option. It does not silently consume the reserve to make the request fit.

### MA.2:6 - Bias-Annotation

A high-utilization target can conceal the value of protective capacity; the label “reserve” can conceal unnecessary provision. Examine the actual operating reason and consequence.

The period account does not establish a long-run staffing result. A later horizon can change demand, terms and the feasible supply action.

### MA.2:7 - Conformance Checklist

Examine whether the account identifies the resource, capability, unit and window; reconciles supply with relevant uses and restrictions; retains the operating basis of reserve; distinguishes released capability from changed payment; and names the action and conditions needed for a supply change.

These checks assess the explanation. The existence of paid capacity does not establish a feasible schedule or the adequacy of a reserve.

### MA.2:8 - Common Anti-Patterns and How to Avoid Them

**Booking every released hour as a saving.** Find the payment or opportunity that actually changes.

**Removing reserve because it appears unused.** Obtain the operational consequence of removing it, including the variation it was intended to absorb.

**Comparing utilization rates with different denominators.** Recover what each denominator includes before judging a difference.

### MA.2:9 - Consequences

The user can distinguish an efficiency improvement, unused provision and an avoidable payment. This improves the information supplied to a capacity decision.

The account may leave the operating choice unresolved. That is useful when its remaining question is explicit, such as the needed reserve or the feasibility of a replacement block.

### MA.2:10 - Architectural Rationale

Supply, capability and consumption are separated because each responds differently to action. A single hourly rate can support a defined account, but cannot carry all three meanings.

The accounting method explains quantities and money while OPS decides the operating arrangement. Combining them without preserving that boundary would let a chosen denominator decide what the service can safely promise.

### MA.2:11 - SoTA-Echoing

The selected line combines resource-based managerial costing with the distinction between productive, protective and excess capacity discussed in Tendon and Doiron's *Tame your Work Flow* (2020), chapter 7. It adapts the distinction to the actual operating account: the reason for reserve must be established, and elapsed flow time alone does not identify a constrained resource.

In the historical fixture example in Caspari and Caspari's *Management Dynamics* (2004), shortening work at one station does not reduce wages; under high demand, the extra time at the constrained station reduces output. These contributions inform §§4.2–4.3 and the released-hours example.

At the effort of reconciling one resource pool, this account exposes distinctions a utilization percentage hides. More detailed tracking is worthwhile when a capability or time boundary changes the decision. Reopen the account when those conditions or the supply terms change.

### MA.2:12 - Relations

MA.1 supplies resource demand. MA.3 uses adequate pool meanings for shared assignment; MA.4 reconciles monetary views. OPS supplies constraint, reserve, schedule and capacity decisions and consumes this account's supported quantities.

### MA.2:End

## MA.3 - Assign Shared Costs for the Stated Use

**Type:** Architectural

### MA.3:0 - Use this when

Use this pattern when a shared cost must be assigned to products, customers or units, or when an assigned amount is being interpreted as something its recipient caused or can avoid.

The pattern governs a purpose-qualified shared-cost assignment. It returns assigned amounts reconciled to the source total, with the consumption evidence and any allocation convention needed to interpret them.

If the current assignment is adequate for its use, retain it. An incremental choice can often use actual changed flows without allocating every shared cost.

### MA.3:1 - Problem frame

A shared resource supports several recipients. Some consumption can be traced to a recipient; some sustains the group or cannot be separated at warranted effort. A reporting, pricing, charging or responsibility question can still require a distributed total.

The need to assign money does not establish that one assignment rule answers all those purposes. A contractual charging convention can be valid for billing while being inadequate as evidence of avoidable cost.

### MA.3:2 - Problem

An allocation makes an account add up, which can give the assigned number an unwarranted causal meaning. Closing a segment can then appear to avoid a payment even when the payment for the shared resource stays unchanged and only its allocation among the remaining segments changes.

Refusing every assignment is also unhelpful when the receiving use legitimately requires one. The task is to supply that assignment while preserving what it actually means.

### MA.3:3 - Forces

Tracing can improve the account but has a measurement cost. Convenient drivers are cheap and can be misleading. More precise allocation does not establish a payment consequence when the shared supply remains unchanged.

Recipients can influence both the rule and recorded use. An apparently technical choice can therefore change incentives or who bears a charge.

### MA.3:4 - Solution

#### MA.3:4.1 - Establish the receiving purpose and source total

State what the assignment must support: a management account, agreed charge, pricing analysis, reporting requirement or another particular use. Recover the source pool, period, included costs and relevant resource meaning.

Separate pools whose capability or monetary behavior would change the interpretation. Reconcile the source total before distributing it; an unexplained residual must not be hidden in a recipient's rate.

#### MA.3:4.2 - Trace what the evidence supports

Recover the resource consumption attributable to each recipient at warranted detail. Use MA.1 for missing dependencies and MA.2 for a disputed supply or capacity meaning.

Retain joint or sustaining costs at the level their explanation supports when the receiving purpose allows it. A sales-value percentage can be an allocation convention; it does not establish resource consumption merely because it correlates with a recipient's size.

#### MA.3:4.3 - Make a necessary convention explicit

When the receiving purpose requires distribution beyond supported tracing, select or obtain the rule appropriate to that purpose. State the basis and why it is usable here. An applicable agreement or reporting rule may determine it.

Apply the rule consistently to the defined source total and recipients. Retain rounding, excluded items or residuals where they affect reconciliation. Distinguish a change in the total from a change in its assignment.

Where plausible rules could change a consequential interpretation, show that sensitivity or return the disputed rule.

#### MA.3:4.4 - Return the assignment with its warranted interpretation

Supply the assigned amounts, their source total and the tracing or convention needed to interpret them. State whether the assignment describes resource consumption, an agreed charge or another specific account.

If someone proposes an avoidance or closure conclusion, obtain the actual payment and opportunity changes through MA.1–2 and OPS.14. MA.9 examines the assignment's behavioral consequences when they are the unresolved question.

### MA.3:5 - Archetypal Grounding

A shared support arrangement costs 1,200 per period. Its supplied terms keep the payment unchanged if either segment closes during this horizon. A required internal charge uses observed support-hours: six for A and four for B. The agreed assignment is therefore **720 to A and 480 to B**.

A has revenue 900 and other avoidable payments of 300. B has revenue 700 and other avoidable payments of 200. After the shared assignment, A shows **−120** and B **20**; together they show **−100**.

If A closes and all other conditions remain unchanged, the group loses its 600 contribution while the shared payment remains 1,200. B's remaining account is **700 − 200 − 1,200 = −700**. The assigned loss of 120 did not identify a 720 payment saving.

If an actual permitted supply change instead avoids 300 of the shared payment in the relevant horizon, include that changed amount. The comparison now differs by **−600 + 300 = −300**, under the stated remaining premises. OPS.14 performs the choice with any further displacement, timing and feasibility consequences. Reallocating the same 1,200 does not supply this change.

### MA.3:6 - Bias-Annotation

A recipient can prefer a driver that lowers its charge. An analyst can prefer measurable activity even when it poorly explains the resource pool. Make the source purpose and evidence inspectable.

The example uses an agreed internal convention. Its validity for that charge does not establish a universally fair or causal allocation rule.

### MA.3:7 - Conformance Checklist

Examine whether the assignment has a stated use; its source pool and period are adequate; supported tracing is distinguishable from convention; assigned amounts reconcile with explicit residuals; and the recipient can tell what the amounts support.

An avoidance claim additionally needs evidence of the actual change. Reconciliation alone cannot supply it.

### MA.3:8 - Common Anti-Patterns and How to Avoid Them

**Saving an allocated share by deleting its recipient.** Inspect which payments and opportunities disappear.

**Calling a convenient driver causal.** Establish the consumption relationship or label the warranted convention.

**Forcing every sustaining cost onto a unit.** Retain its supported level when the receiving purpose permits; allocate further only for a use that needs it.

### MA.3:9 - Consequences

The user obtains an assignment that can be reconciled and interpreted. Different accounts can serve their stated purposes. An assigned share alone does not show which payments or opportunities would change.

The rule can distribute burden and affect behavior. Its maintenance and measurement cost must be justified by the use it serves.

### MA.3:10 - Architectural Rationale

Purpose precedes the assignment rule because tracing, internal charging and a required reporting allocation have different standards of adequacy. Reconciliation preserves the total; the explanation preserves the assigned amounts' meaning.

A single stable driver is adequate when it serves the agreed purpose. A more detailed model becomes useful when heterogeneity changes that use. Neither removes the need to establish actual changed flows for a closure decision.

### MA.3:11 - SoTA-Echoing

The selected line uses managerial costing's separation of supported consumption from attribution and the throughput-accounting warning about average or allocated amounts in an incremental choice. Bragg's *Throughput Accounting* (2007), printed pp.44–47, supplies historical pricing and allocation examples; MA.1 supplies the quantitative resource construction used here.

The adaptation retains an allocation when the receiving purpose needs it, while withholding an unsupported avoidance interpretation. At the effort of identifying one pool and its rule, the segment example reveals a closure loss that its allocated result conceals. Reopen the assignment when its purpose, source pool, consumption evidence or applicable rule changes.

### MA.3:12 - Relations

MA.1–2 supply consumption and capacity meanings. MA.4 reconciles different accounts; MA.7 explains a changed assignment or cost; MA.9 examines resulting incentives. OPS.14 uses actual incremental consequences for the operating comparison.

### MA.3:End

## MA.4 - Reconcile Operating, Reporting and Cash Accounts

**Type:** Architectural

### MA.4:0 - Use this when

Use this pattern when the same work seems to produce incompatible profit, inventory or cash results in different accounts. Begin with the difference that changes a decision or interpretation.

The pattern governs an explanation connecting the relevant accounts while retaining each account's purpose and rules. Its result is a reconciled difference, or a located discrepancy requiring correction or specialist interpretation.

Use an adequate existing reconciliation directly. The method does not replace the applicable financial, tax or other reporting rules.

### MA.4:1 - Problem frame

Production, sale, recognition of an expense and payment can occur at different times. One management account can expense a supplied resource in the period; another account can include an eligible share in inventory until sale. An unpaid credit sale can increase reported revenue and create a customer receivable before cash arrives.

These accounts can disagree numerically without contradicting one another. They can also contain an error. The model must establish which explanation applies.

### MA.4:2 - Problem

A profit figure is often treated as cash generated, or a management restatement as a correction to an external report. That loses recognition, valuation or settlement conditions.

A reconciliation that merely inserts an unexplained balancing amount has the opposite defect: it makes totals agree while hiding the unresolved question. The practitioner needs an explicit explanation of the difference.

### MA.4:3 - Forces

Each account simplifies work for a purpose. Comparing them requires enough common subject and period information to retain their different rules. A detailed event reconstruction is costly when a small inventory or receivable bridge is sufficient.

A correct mathematical reconciliation can still use an inapplicable policy. Reporting adequacy and arithmetic therefore need different evidence.

### MA.4:4 - Solution

#### MA.4:4.1 - Recover what each account measures

Identify the entities, work, period, currency and intended use of each account. Recover the recognition and valuation rules relevant to the disputed amount. State whether the account concerns revenue, expense, inventory, resource consumption, payments or another quantity.

Use OPS.15 for an unresolved event or observation definition. Use the responsible reporting practice when the applicable policy is missing or disputed.

#### MA.4:4.2 - Establish a common event and opening basis

Recover the opening balances and the production, purchase, sale, settlement or other events needed to explain the difference. Match their subjects and dates. Do not compare unlike periods by inserting a residual.

A sufficient existing source account can supply these facts. Reconstruct individual events only where aggregation prevents the required explanation.

#### MA.4:4.3 - Explain the differences by their actual causes

Reconcile the relevant amounts, including balances of inventory, receivables and payables. Explain differences caused by the recognition or valuation rules. Keep a management reclassification distinct from an actual settlement.

Show the calculation at enough detail to expose a missing term. A difference caused by timing can reverse in a later period; a difference in valuation policy can persist. State which is being explained.

#### MA.4:4.4 - Return the reconciled views and any discrepancy

Preserve each account for its warranted use and return the explanation connecting them. If a source is wrong, identify the correction for its responsible process. A management model does not silently amend a statutory account.

Supply the required monetary basis to the receiving operating or financial method. If funding is at issue, use the whole timed cash position, including other relevant receipts and obligations.

### MA.4:5 - Archetypal Grounding

A constructed service-manufacturing account has no opening balances or other transactions. During the period it produces 100 units, spending 200 on materials and 300 on production-resource supply. All 500 is paid in the period. It sells 60 units at 10, recognizes revenue of 600 under the supplied policy and receives 400; the remaining 200 is receivable.

Under the example's supplied full-production-cost policy, eligible cost is 500, or 5 per unit. Cost of the 60 units sold is 300, closing inventory is 200 and the reported result is **600 − 300 = 300**. The cash movement is **400 − 500 = −100**.

An internal throughput-style account carries only materials in inventory and expenses the 300 resource supply in the period. Materials in the 60 sold units cost 120; closing material-valued inventory is 80. Its result is **600 − 120 − 300 = 180**.

The accounts connect explicitly:

| Connection | Calculation | Result |
| --- | --- | ---: |
| Internal result to the supplied full-cost result | 180 + 120 of production-resource cost retained in closing inventory | **300** |
| Full-cost result to cash movement | 300 − 200 increase in inventory − 200 increase in receivables | **−100** |
| Internal result to cash movement | 180 − 80 increase in material-valued inventory − 200 increase in receivables | **−100** |

The 120 difference is a recognition and valuation effect under the supplied policies. It is not another cash receipt. The unpaid customer balance and closing inventory explain why either positive result coexists with negative cash movement.

An actual reporting use must establish the applicable capitalization, recognition and measurement rules. The example supplies its policies to demonstrate the reconciliation.

### MA.4:6 - Bias-Annotation

An internal decision maker can prefer the view that supports a proposal; an external-reporting practitioner can treat a required account as adequate for every internal choice. Retain the purposes and rules of both.

A familiar bridge can also conceal a new item. An unexplained residual remains a discrepancy rather than evidence that the reconciliation is complete.

### MA.4:7 - Conformance Checklist

Examine whether the accounts' subjects, periods, currency and purpose are clear; relevant recognition and valuation rules are established; opening values and events support the comparison; differences reconcile without an unexplained residual; and corrections are distinguished from valid alternative views.

Arithmetic establishes the connection under those premises. Policy applicability and actual settlement require their own support.

### MA.4:8 - Common Anti-Patterns and How to Avoid Them

**Reading profit as available cash.** Reconcile inventories, unsettled balances and other relevant movements, then establish the timed cash position.

**Correcting one legitimate account into another.** Explain the policy and purpose difference before changing a source.

**Hiding the gap in “other”.** Locate the unresolved event, period or valuation item.

### MA.4:9 - Consequences

The user can explain apparently conflicting accounts and choose the monetary basis the receiving decision needs. An actual error becomes distinguishable from a valid difference in purpose or timing.

The work can require specialist interpretation of a reporting policy. A completed management bridge does not confer that reporting authority or supply missing event evidence.

### MA.4:10 - Architectural Rationale

The method connects views through their subjects, events and rules because a shared monetary unit does not give them a shared meaning. It preserves the views instead of manufacturing one universal profit number.

A small bridge is preferable when a few known balance movements explain the difference. Event-level reconstruction becomes worthwhile when the aggregate no longer locates the discrepancy.

### MA.4:11 - SoTA-Echoing

The method distinguishes internal from externally required accounts and uses the inventory bridge discussed in Bragg's *Throughput Accounting* (2007), printed pp.111–112. It adapts that explanation to explicit policies and actual settlements rather than treating a management view as a substitute for required reporting.

[IAS 2][IAS2] provides a relevant external-reporting comparator: inventory cost and its later recognition as expense have rules that differ from simply recording cash paid. Its applicability and detailed requirements belong to the reporting question. Here that distinction changes §§4.1–4.3 and the inventory example.

At the effort of reconciling inventory and receivables, the example explains three valid numbers that a profit-to-cash identification cannot. Reopen the bridge when policies, balances, event meanings or the receiving period changes.

### MA.4:12 - Relations

MA.1–3 supply resource and assignment meanings. MA.5 uses reconciled assumptions in a forecast; MA.7 investigates differences; MA.9 examines behavior encouraged by a particular view. OPS.15 supplies operating-account definitions and events. OPS.14 and the relevant financial practice consume the monetary basis their decisions require.

### MA.4:End

## MA.5 - Construct and Update an Operating Forecast

**Type:** Architectural

### MA.5:0 - Use this when

Use this pattern when a coming workload, resource need or monetary consequence must be anticipated and a target or historical average cannot answer the question. Begin with the action the forecast could change and the lead time needed to act.

The pattern governs a conditional operating forecast. It returns the relevant demand, resource and monetary outlook, the assumptions that can change it and the conditions for updating it.

Use an adequate current forecast directly. Additional detail is useful only when it can change the receiving action or its assurance.

### MA.5:1 - Problem frame

An operation needs to anticipate demand, material use, capacity and payment timing. Some inputs can be estimated from current orders; others depend on uncertain demand or intended actions. A future resource threshold can matter even when the central workload estimate fits current capacity.

A forecast expresses what is expected under stated conditions. A target expresses an ambition; an authorized resource amount expresses a decision. Their relationship is useful, but one cannot be substituted for another.

### MA.5:2 - Problem

A forecast built by extending last period's totals can conceal a changed mix, resource threshold or collection delay. A forecast negotiated as a target can conceal expected difficulty.

An elaborate model can still be unhelpful if its horizon is too short to act or its assumptions cannot be revised. Forecast the quantities and conditions that could change the receiving action, with enough detail to show the uncertainty that matters.

### MA.5:3 - Forces

The user needs a timely answer even when the future is uncertain. A single number is convenient, while a range or scenario can better preserve the condition that matters.

Actions taken in response to a forecast can change the outcome. Later evaluation must therefore retain the original conditions and the response rather than treating every numerical miss as the same forecasting failure.

### MA.5:4 - Solution

#### MA.5:4.1 - Choose the receiving use and horizon

State who will use the forecast, what decision or preparation it could change and when that action must occur. Choose a horizon long enough for the relevant response.

Recover the adequate existing account and forecast. Determine whether the missing answer concerns demand, resource conversion, money, timing or uncertainty. Avoid requesting details that the receiving use would not act on.

#### MA.5:4.2 - Connect the consequential assumptions

Build from the relevant demand and work assumptions through resource consumption, supply and money. MA.1–4 supply missing dependencies or account meanings. Preserve changes in mix, yields, rework, prices, supply blocks and settlement timing where they can alter the answer.

Distinguish observed facts, commitments, model estimates and proposed actions. A proposed capacity addition belongs in the scenario in which it occurs, rather than silently becoming available in every forecast.

If a term such as “expected” needs statistical precision, state whether the reported value is a mean, a quantile or another defined estimate. A central planning scenario is not automatically an expected value across possible outcomes.

#### MA.5:4.3 - Retain the uncertainty that changes action

Use a range, scenarios or a supported probabilistic model according to the question and available evidence. Preserve dependencies between uncertain inputs when independently combining favorable values would create an implausible case.

Inspect the conditions that can change feasibility, a payment block or the useful response. A forecast need not specify every contingency to reveal a decisive capacity threshold. If a material input cannot be estimated adequately, state the conditional conclusion or exact unresolved question.

Represent uncertainty in forecast revenue and receipts at the detail needed for their use. Uncertainty does not by itself prohibit forecasting them; it limits the conclusions a particular forecast can support.

#### MA.5:4.4 - Return the forecast and usable response conditions

Supply the quantities, timing and assumptions in a form the recipient can use. Identify the condition that would require a decision, such as workload beyond usable capacity or a payment before available funding.

The forecast does not authorize that response. Use the responsible operating or financial decision method. When payment feasibility is the question, connect the selected flows to the whole timed cash account, including other relevant receipts and obligations.

#### MA.5:4.5 - Update from changed conditions and learn from outcomes

Revise the affected assumptions when new evidence or an actual decision changes them. Preserve the earlier forecast at the level needed to explain the change or learn from it; do not overwrite its premises and then claim it predicted the result.

When comparing with actual outcomes, distinguish changed external conditions, estimation error, bias and actions taken in response. Action taken in response to a forecast can prevent the adverse outcome it describes and explain a numerical difference. This does not by itself prove the forecasting model was accurate. Examine the claim and comparison actually needed.

Choose refresh timing from the pace of relevant change and the receiving action. A rolling window can help; refreshing unchanged detail on a calendar alone can consume effort without improving the result.

### MA.5:5 - Archetypal Grounding

A service forecasts next period's workload using three planning scenarios: 80, 100 or 120 accepted units. These are supplied scenarios without probability weights. The adequate resource model requires ten setup hours plus 0.25 qualified staff-hours per unit. A supplied arrangement provides 38 usable hours for 120 currency units; a feasible extra five-hour block costs 80.

| Workload scenario | Required staff-hours | Relevant supply condition |
| --- | ---: | --- |
| 80 units | 10 + 80 × 0.25 = **30** | Fits the supplied 38 hours. |
| 100 units | 10 + 100 × 0.25 = **35** | Fits the supplied 38 hours. |
| 120 units | 10 + 120 × 0.25 = **40** | Needs an adequate additional arrangement; the supplied five-hour block is one option. |

Materials require 3 per unit, and the service price is 10 per accepted unit. In the 100-unit scenario, materials are 300 and sales are 1,000. The supplied collection assumption places the 1,000 receipt on day 30, while the 300 material and 120 resource payments occur on day 1. A funding use needs the whole cash account.

If new evidence changes the central scenario to 96 units, its resource demand becomes **34 hours**, materials **288** and sales **960**. The existing supply payment remains 120. Updating every amount by four percent would wrongly reduce that unchanged payment.

If the team instead obtains extra capacity in response to the high scenario, the revised forecast includes that decision under its actual terms. Later outcomes are compared with the conditions of each forecast.

### MA.5:6 - Bias-Annotation

People may conceal an adverse outlook when reporting it threatens a target or future resources. Separate the meanings through MA.6 and inspect the incentives through MA.9 when needed.

A modeler can also mistake abundant historical data for stable future behavior. Changed product mix or supply terms can invalidate a precise extrapolation.

### MA.5:7 - Conformance Checklist

Examine whether the forecast has a receiving action and useful horizon; connects adequate demand, resource and monetary assumptions; distinguishes facts, estimates and proposed actions; retains uncertainty that can change the result; and has a warranted update rule.

A constructed scenario demonstrates a conditional consequence. Forecast calibration, actual performance and the success of a response require their corresponding evidence.

### MA.5:8 - Common Anti-Patterns and How to Avoid Them

**Scaling every cost with volume.** Preserve actual supply thresholds and unchanged payments.

**Treating an adverse forecast as a failed promise.** Recover its conditions and the decision it was intended to inform.

**Improving the forecast by rewriting its history.** Retain the earlier premises needed for a valid comparison.

### MA.5:9 - Consequences

The user can prepare for a consequential range and revise the account when evidence changes. The forecast can expose a capacity or funding question early enough for action.

More uncertainty may remain visible than in a negotiated single number. The work also needs maintained assumptions; their detail should be justified by the receiving use.

### MA.5:10 - Architectural Rationale

The forecast is organized around the action it could change because accuracy at an irrelevant horizon has little practical value. Resource and monetary dependencies preserve consequences that total extrapolation can hide.

A stable simple forecast can be adequate for a stable use. Scenarios are useful when different plausible conditions require different responses. A more detailed predictive model is justified by the additional decision-relevant distinction and evidence it can supply.

### MA.5:11 - SoTA-Echoing

The selected line uses Bogsnes's *Implementing Beyond Budgeting*, second edition (2016), printed pp.159–166: forecasts describe expected consequences, should be timely and actionable, and can use scenarios where a point number conceals uncertainty. The current [Beyond Budgeting principles][BB] retain a lean forecasting process distinct from targets and resource allocation.

This changes §§4.1–4.5 by tying horizon and detail to use and preserving responses when learning from outcomes. The pattern qualifies the source's strong external-versus-internal accuracy distinction: intervention changes what comparison is warranted; it does not prohibit evaluating a clearly specified conditional forecast.

At the effort of three resource scenarios, the example reveals a supply threshold that a scaled expense total misses. Reopen the model when the response horizon, dependencies or relevant uncertainty changes.

### MA.5:12 - Relations

MA.1–4 supply resource and account construction. MA.6 separates forecast, target and resource decisions; MA.7 explains differences; MA.8 supplies cohort or product assumptions. OPS and the relevant financial practice use the forecast for their decisions.

### MA.5:End

## MA.6 - Separate Forecasts, Targets and Resource Requests

**Type:** Architectural

### MA.6:0 - Use this when

Use this pattern when one number is expected to predict demand, express ambition and secure resources at the same time. Negotiation can then make the expected outlook hard to see.

The pattern governs the connected meanings and uses of forecasts, targets and requested or authorized resources. It returns distinguishable accounts and the gap or decision they expose.

Keep an adequate existing separation. This method does not require replacing every organizational budgeting arrangement.

### MA.6:1 - Problem frame

A team may expect demand of 100, aspire to serve 120 and seek resources adequate for 130 under a higher-demand scenario. Its approved provision may support only 110. Each number can be legitimate under its own assumptions.

Their differences help people decide whether to change an action, ambition or resource arrangement. Requiring the values to agree before showing them can erase that useful information.

### MA.6:2 - Problem

When a forecast is also a bargaining position, its author has reasons to bias it. A ceiling can then be mistaken for an expectation, or an ambitious target for a feasible operating plan.

The task is to distinguish the meanings and keep their consequential relationships visible.

### MA.6:3 - Forces

Management needs coordination and legitimate resource control. Forecasters need to report an unwelcome expectation without automatically changing a target or losing needed options.

These accounts can use different horizons and revision rules. Their comparison requires an adequate common basis where the difference matters.

### MA.6:4 - Solution

#### MA.6:4.1 - Recover each number's actual use

Ask what the number is meant to do: describe an expectation, set an ambition, request resources or record an authorization. Identify the relevant participant, period, quantity and assumptions.

Use the actual meaning rather than the file's label. A document called “forecast” can contain a negotiated spending envelope; a budget can legitimately contain several distinct accounts.

#### MA.6:4.2 - Give the meanings their own revision and decision rules

Construct the forecast from adequate evidence and assumptions through MA.5. Obtain targets and resource decisions from the responsible management practice. State how each is revised and who can make the relevant decision.

Separate a request from a granted resource amount and from actual usable provision. A forecast revision does not itself authorize spending.

The distinction can be made in one small table.

#### MA.6:4.3 - Explain the consequential gaps

Put comparable quantities on an adequate common basis. Use MA.1–2 when a workload target must be translated into resource capability and payments.

Ask what each gap means. Expected demand below a target can call for a different action or revised ambition. Required capacity above authorized provision can call for a resource decision, changed scope or an explicit adverse scenario. Preserve uncertainty and the conditions under which an apparent gap exists.

Do not close the gap by editing the expectation to equal the authorized number. Change the relevant action or decision, then forecast its warranted consequence.

#### MA.6:4.4 - Return the connected accounts and required decision

Show the expectation, ambition, request and authorization at enough detail to locate the next decision. Preserve the forecast's original assumptions when a later choice changes them.

Observe whether people can now report an unwelcome expectation and whether decisions about resources take that expectation into account. MA.9 examines persistent behavioral effects; the responsible organizational practice supplies a wider change in management arrangements.

### MA.6:5 - Archetypal Grounding

For one period and a supplied service mix, the team expects demand of **100 units** and has an ambition to serve **120**. Its resource request would provide capability for **130**, to meet a possible demand surge to that level within the same period and service mix. The authorized resource arrangement supports **110**, under supplied scheduling and conversion assumptions.

| Account | Meaning | Question exposed |
| --- | --- | --- |
| 100 expected | The present demand outlook. | What action or new evidence could change it? |
| 120 targeted | The intended ambition. | Is the action plan adequate, or should the ambition be reconsidered? |
| Resources for 130 requested | Provision sought for the stated scenario. | Is that protection worth its cost under the applicable decision criteria? |
| Resources for 110 authorized | The current authorized arrangement. | What can be promised and what additional decision is needed? |

The granted 110 does not make demand 110. It also does not establish that the ambition of 120 is feasible. The team returns the resource gap to the competent decision maker while keeping the 100 forecast available.

If a changed market action warrants a new demand expectation of 115, update the forecast and explain its new assumptions. The gap against authorized capability is now five units under the supplied comparison basis. The target remains 120 and authorized capability remains 110 until the responsible people revise them under their applicable rules.

### MA.6:6 - Bias-Annotation

A reformer may assume that removing a budget label removes the incentive to bias numbers. Observe the actual uses and consequences; old bargaining behavior can persist in a newly named forecast.

A controller may interpret separation as loss of control. Distinguishing an expectation from authorization makes the existing control more explicit.

### MA.6:7 - Conformance Checklist

Examine whether each number's use, period and assumptions are clear; forecasts, ambitions, requests and authorizations remain distinguishable; their comparison uses an adequate common basis; revision and authority rules are explicit where needed; and the gap leads to a meaningful decision.

Different labels alone do not establish the separation in practice. Actual use and incentives can combine the meanings.

### MA.6:8 - Common Anti-Patterns and How to Avoid Them

**Making the forecast equal the approved ceiling.** Preserve the expectation and decide what to do about the resource difference.

**Replacing one confused number with disconnected accounts.** Retain the comparison and the decision each gap needs.

**Treating separation as a spending grant.** Obtain the authorization and usable provision required by the actual action.

### MA.6:9 - Consequences

The user can see an adverse expectation, ambitious target and resource constraint together. This can improve the next decision without forcing all quantities to agree.

The change can expose previously hidden conflicts and requires people to use the numbers consistently. A wider management change may be needed if incentives continue to penalize accurate reporting.

### MA.6:10 - Architectural Rationale

The meanings are separated because expectation, aspiration and authorization have different truth and decision conditions. Their relationships show which management or resource decision is needed.

A conventional budget remains usable when it preserves those distinctions for the required work. A broader Beyond Budgeting arrangement can be appropriate when its organizational and management changes address the actual problem; it is not a prerequisite for clarifying four numbers.

### MA.6:11 - SoTA-Echoing

The selected line adopts the purpose separation explained by Bogsnes (2016), printed pp.139–142, and retained in the Beyond Budgeting principles. It changes §§4.1–4.3 by allowing different numbers with connected uses and decision rules.

The pattern adapts the wider organizational proposal to a small first result: a forecast, target and resource account can be distinguished before redesigning the whole management system. At that effort, the 100/120/130/110 case reveals decisions a single negotiated figure conceals. Reopen the arrangement when actual use again merges the meanings or a changed organizational context requires a wider method.

### MA.6:12 - Relations

MA.5 constructs the expectation. MA.1–2 translate workload into adequate resource quantities. MA.9 examines behavioral effects. The responsible management and organizational-change practices establish objectives, authority, resource decisions and any wider implementation.

### MA.6:End

## MA.7 - Explain a Cost or Margin Difference

**Type:** Architectural

### MA.7:0 - Use this when

Use this pattern when a cost, margin or other account differs from a comparison value and the explanation could change a response. Begin with the actual difference before attributing it to performance.

The pattern governs an explanation of an accounting difference. It returns a comparable basis, an adequate decomposition and supported or unresolved explanations of the causes that matter.

Use an adequate existing explanation directly. A small immaterial difference need not trigger a wider investigation unless another obligation requires it.

### MA.7:1 - Problem frame

A period's material cost can rise because more units were produced, the mix changed, more material was consumed per accepted unit or the price changed. A margin can also change because of recognition, shared assignment or capacity use.

An arithmetic decomposition helps locate the difference. It does not by itself establish why the quantities changed or which participant could have acted differently.

### MA.7:2 - Problem

Calling every adverse difference “inefficiency” can direct action at the wrong cause. Comparing unlike periods or definitions can create a variance that has no performance meaning.

A decomposition with many small terms can also hide the consequential explanation. The task is to recover the comparison and investigate the causes that can change the response.

### MA.7:3 - Forces

Management wants an early explanation. A provisional decomposition can be useful before causal evidence is complete, provided its status remains clear.

Several factors can interact, so the amount assigned to each arithmetic component can depend on the decomposition convention. A convenient order is usable for explanation when that convention is visible.

### MA.7:4 - Solution

#### MA.7:4.1 - Restore a comparable account

Identify the two values, their subjects, periods, units and purposes. Recover the definitions, recognition, valuation and allocation rules that produced them. Use MA.4 for a view difference and MA.3 for a changed assignment.

Separate a genuine work or price change from a changed measurement or account boundary. Keep an unresolved comparison problem visible before interpreting a variance as performance.

#### MA.7:4.2 - Decompose the consequential difference

Use an adequate resource and monetary model to separate the effects needed for the question: volume, mix, usage, price, capacity, timing or another relevant factor. State the reference values and order where they affect the calculation.

Reconcile the components to the total, retaining a residual if the present model cannot explain it. Do not force a residual into a preferred cause. A smaller decomposition is sufficient when further terms cannot change the response.

#### MA.7:4.3 - Test the explanation behind the arithmetic

Ask what actually changed each consequential component. Compare operating evidence, terms and relevant conditions. Higher material use per accepted unit might follow a harder product mix, failed attempts, a measurement change or a process defect.

Distinguish association and assigned arithmetic effect from a supported causal explanation. Investigate the rival explanations that would lead to different actions. If adequate evidence is unavailable, return the bounded uncertainty and the next observation or specialist result that could resolve it.

#### MA.7:4.4 - Return the explanation and appropriate response question

Supply the total difference, its adequate decomposition and the supported causes or remaining uncertainty. Keep controllability and responsibility claims at the scope their evidence warrants.

Use the relevant operating, commercial or financial method for the response. MA.5 updates a future outlook when the changed condition is expected to persist; MA.9 examines incentives that may be influencing the account or behavior.

### MA.7:5 - Archetypal Grounding

A constructed material-consumption account planned 100 accepted units, two material units per accepted unit and a price of 3 per material unit. Planned cost was **100 × 2 × 3 = 600**.

The actual comparable account has 120 accepted units, 2.5 material units per accepted unit and a price of 4. Actual cost is **120 × 2.5 × 4 = 1,200**, a difference of **600**.

Using the stated order volume, usage, then price:

| Component | Calculation | Amount |
| --- | --- | ---: |
| Volume at planned usage and price | (120 − 100) × 2 × 3 | **120** |
| Usage at actual volume and planned price | 120 × (2.5 − 2) × 3 | **180** |
| Price at actual volume and usage | 120 × 2.5 × (4 − 3) | **300** |
| Total difference | 120 + 180 + 300 | **600** |

The decomposition is complete arithmetically. It does not establish that the extra 0.5 material units were waste. If the actual workload included a different product mix legitimately requiring more material, the comparison needs that distinction. If the mix is unchanged and adequate records identify failed attempts, the process question becomes more specific. A changed measuring convention would instead require repairing the account.

Another valid decomposition order can assign interaction amounts differently. Retain the chosen convention rather than using a component's exact size as independent evidence of causal responsibility.

### MA.7:6 - Bias-Annotation

A manager can prefer an explanation outside their control; an evaluator can prefer one inside it. Test explanations against actual conditions and evidence.

### MA.7:7 - Conformance Checklist

Examine whether the comparison uses adequate subjects, periods and account rules; consequential components reconcile to the total; the decomposition convention is clear where needed; causal claims have support beyond arithmetic; and unresolved explanations lead to a useful next question.

A zero arithmetic residual establishes numerical closure under the model. It does not establish causal closure.

### MA.7:8 - Common Anti-Patterns and How to Avoid Them

**Calling a usage variance waste before checking mix.** Recover the actual resource requirement and alternative explanations.

**Assigning responsibility from the decomposition order.** Distinguish the arithmetic convention from evidence about cause and control.

**Balancing an unexplained residual into “efficiency”.** Keep the residual visible and investigate the missing relation.

### MA.7:9 - Consequences

The user can respond to a difference with a more specific question and can avoid mistaking account changes for operating performance. A provisional explanation can support useful inquiry.

The result may stop short of a causal conclusion. Its next evidence demand should be proportionate to the decision the explanation can change.

### MA.7:10 - Architectural Rationale

Comparison, decomposition and explanation are separated because each can fail independently. An account can be comparable yet poorly decomposed, or perfectly decomposed yet causally misunderstood.

A routine variance report is sufficient when its definitions and explanations remain adequate. A deeper resource model or inquiry is justified when a plausible alternative would change the response.

### MA.7:11 - SoTA-Echoing

The selected line combines resource-based accounting with explicit numerical decomposition and causal inquiry. Caspari and Caspari's opening fixture case supplies a historical reason to question local performance readings: a changed activity time can have a different consequence at the system constraint. MA.1 supplies the quantitative model; the applicable inquiry method supplies further evidence when a causal question remains.

This changes §§4.1–4.3 by separating comparable accounting values, arithmetic components and supported explanations. At the effort of the three-term example, the analyst locates a usage question without automatically blaming inefficiency. Reopen the explanation when changed mix, definitions or operating evidence defeats its comparison or cause.

### MA.7:12 - Relations

MA.1–4 supply model and account meanings. MA.5 consumes persistent changed assumptions; MA.9 examines behavioral causes. OPS.15 supplies event and observation definitions, and the relevant operating or financial method decides the response. C.11.DUA supports a disputed further-inquiry choice.

### MA.7:End

## MA.8 - Account for Customer and Product Economics Over Time

**Type:** Architectural

### MA.8:0 - Use this when

Use this pattern when a current unit margin hides acquisition, later service, retention, returns or other consequential flows. Begin with the customer cohort or product use and the decision the account must support.

The pattern governs a time-related customer or product account. It returns observed and conditional resource and monetary flows over a stated horizon, with the assumptions needed to interpret acquisition, continuation and scale.

Use an adequate existing account directly. A lifetime valuation or financing decision uses the additional method required by the relevant financial practice.

### MA.8:1 - Problem frame

A service can earn a positive margin from an active customer this month while still failing to recover acquisition spending. Future service demand, retention and collection determine a different part of the account. An established customer's continuation also raises a different question from acquiring a new customer.

Products have their own time structure. Development, production, warranty, support and withdrawal can occur in different periods. A subscription-retention formula does not describe every product's later obligations.

### MA.8:2 - Problem

A single current margin or acquisition ratio compresses the period, population and resource behavior. Extending it across a lifetime can conceal churn, heterogeneous cohorts or an additional supply block.

Counting every historical cost again in a continuation choice produces the opposite error. The task is to preserve the whole account needed for understanding while supplying the future changes relevant to the actual choice.

### MA.8:3 - Forces

The account needs a useful horizon even when long-term behavior is uncertain. Early cohorts provide evidence, but their acquisition conditions and service mix may differ from later expansion.

A detailed lifetime model can look more authoritative than a modest period account. Added precision is useful only when its assumptions and evidence support the receiving conclusion.

### MA.8:4 - Solution

#### MA.8:4.1 - Define the unit, population and decision time

State whether the account concerns a customer, subscription, household, product, cohort or another justified unit. Define membership, the observation date and the horizon. Preserve differences in acquisition channel, tenure or use when they can change the answer.

Distinguish a prospective new customer from an existing one. Recover historical acquisition spending for the account, and identify which future acquisition or service payments the current decision can change.

#### MA.8:4.2 - Connect the relevant flows over time

Recover receipts, refunds, acquisition, service, support and other consequential flows with their timing and account meaning. Use MA.1–4 for missing resource, capacity, shared-cost or reconciliation results.

For a product, include later resource demands and obligations that the receiving use needs. For a cohort, connect expected active or purchasing customers to the relevant service demand and money. Keep observed amounts and modeled future amounts distinguishable.

State whether a reported margin includes allocated costs, resource consumption values or incremental flows. Reuse it only for the use those meanings support.

#### MA.8:4.3 - Establish the continuation and scale assumptions

Use a model appropriate to the actual relationship. A subscription can provide an observable renewal or termination event. A customer who makes no purchase this month may merely be between purchases; treat their future activity with an adequate model for that setting.

Inspect whether behavior changes with tenure, cohort, channel or proposed scale. A constant rate can be a supplied scenario assumption; an aggregate historical rate does not establish that it applies to every customer or future period.

Check how scale changes acquisition and resource supply. A larger audience may cost more to reach, while a new server, service team or warranty obligation can change the cost pattern. Neither falling unit cost nor rising acquisition cost is a universal law.

#### MA.8:4.4 - Build the account and test the consequential alternatives

Calculate the observed and conditional period results on the stated basis. Preserve the acquisition boundary, relevant survival or purchasing assumptions and timing. If a limited horizon is used, state what lies outside it; do not call a three-month total a complete lifetime value.

Test the plausible changes that could alter the decision: retention, service intensity, refunds, collection, acquisition cost or a supply threshold. A valuation use obtains the applicable discounting and risk treatment from the relevant financial method.

For a continuation or expansion choice, supply the future differences to OPS.14 or the responsible financial practice. Historical spending can explain cumulative recovery without becoming an avoidable payment.

### MA.8:5 - Archetypal Grounding

A constructed subscription cohort acquires 100 customers at 20 each, paid initially: **2,000**. The scenario assumes 80% renewal into each next month, and 10 of receipt less relevant service payments per active customer per month. Its three-month account is:

| Month | Active customers under the scenario | Period net service flow |
| --- | ---: | ---: |
| 1 | 100 | **1,000** |
| 2 | 80 | **800** |
| 3 | 64 | **640** |

The three-month service total is **2,440**, leaving **440 after acquisition spending** on this undiscounted basis. These are conditional flows, with no other changing flows under the supplied scenario. This account omits flows after month 3.

Before month 2, the original acquisition payment is already spent. Count the original 2,000 once in the cumulative account. Compare continuation with stopping using the future flows that change and the applicable obligations.

Suppose a proposed new cohort costs 35 per customer to acquire, contributes only 6 per active customer per month and has a supplied 60% monthly renewal scenario. Its corresponding three-month service flow is **600 + 360 + 216 = 1,176** against **3,500** acquisition, leaving **−2,324** on the same limited basis. Copying the earlier cohort's ratio would conceal the changed expansion conditions.

A product can require a different model. Suppose an already sold product carries a supplied obligation to provide a service module in year 2 at an expected resource cost of 400. Include that later requirement even if current unit margin omits it. Stopping new sales does not by itself cancel the supplied obligation; FDM establishes disputed terms or effects.

### MA.8:6 - Bias-Annotation

Successful early cohorts can bias an expansion forecast. Acquisition channel, customer mix and capacity may change as the service grows.

A short account can understate later value or cost. Extending the horizon without supported continuation assumptions can instead overstate what is known. Name the actual horizon and decision use.

### MA.8:7 - Conformance Checklist

Examine whether the unit, cohort and decision time are clear; the horizon and account basis are explicit; acquisition and later flows have adequate meanings and timing; continuation and scale assumptions are warranted or qualified; and historical spending is distinguishable from future changes.

A conditional account supports the stated scenario. Actual retention, causal marketing effects and financial valuation require their corresponding evidence and methods.

### MA.8:8 - Common Anti-Patterns and How to Avoid Them

**Calling a short-period total lifetime value.** State the horizon and retain any material omitted continuation.

**Using non-purchase as proof of departure.** Obtain an activity model appropriate to the relationship.

**Copying an early cohort's economics without checking the expansion conditions.** Examine changed acquisition, mix, retention and resource thresholds.

**Charging sunk acquisition again to the continuation choice.** Preserve the historical account and supply the actual future differences.

### MA.8:9 - Consequences

The user can see why current margin, cumulative recovery and future continuation differ. The account supports a more specific growth, service or product question.

Longer horizons increase dependence on behavioral and resource assumptions. A qualified short account can be more useful than an apparently precise lifetime number with unsupported premises.

### MA.8:10 - Architectural Rationale

The method organizes flows around the population and time of the decision because acquisition and continuation do not concern identical future consequences. Resource modeling reveals when serving more customers changes capacity needs and payments.

A simple cohort table is adequate for a bounded scenario. A richer purchasing, retention or product-life model is justified when its distinctions can change the use and can be supported. The account supplies financial inputs without replacing valuation or financing methods.

### MA.8:11 - SoTA-Echoing

The method connects acquisition, customer and scale questions to explicit period flows. It uses the relevant resource and payment relationships and interprets ROI, ROMI and customer-value ratios under their stated definitions.

Fader and Hardie's [2014 CLV note][CLV] qualifies the lifetime label, customer-age boundary and contractual versus noncontractual setting. Their later [duration-dependence work with colleagues][RETENTION] extends a model based solely on customer heterogeneity, showing why changing aggregate retention does not directly identify changing individual behavior. These contributions require explicit population and continuation assumptions in §§4.1–4.3; the simple worked rates remain supplied scenarios.

At the effort of a three-period table, the pattern exposes unrecovered acquisition and changed expansion economics without claiming a universal CLV formula. Reopen it when the cohort, horizon, resource behavior or supported continuation model changes.

### MA.8:12 - Relations

MA.1–4 supply resource and account meanings, MA.5 the conditional outlook and MA.7 explanations of observed differences. FDM supplies a missing financial position, obligation or flow model. OPS.14 and the relevant financial practice consume the future consequences for their comparisons and valuations.

### MA.8:End

## MA.9 - Examine the Behavioral Effects of an Account

**Type:** Architectural

### MA.9:0 - Use this when

Use this pattern when an accounting measure or its use appears to encourage inventory building, cost transfer, concealed expectations or another behavior that may harm the intended result.

The pattern governs an explanation and possible repair of an account's behavioral effects. It returns a warranted change to the account or its use, or a supported reason to retain it, with consequences that can be observed.

Use an adequate arrangement directly. The existence of a target or allocation alone does not establish harmful behavior.

### MA.9:1 - Problem frame

People act within measurement and decision arrangements. A lower reported unit cost can earn approval while consuming more cash and producing unwanted inventory. A forecast used to negotiate resources can encourage biased expectations.

The account can influence behavior alongside demand, operational constraints, authority and other incentives. A useful repair must establish enough of that connection to change the right thing.

### MA.9:2 - Problem

A metric improvement is often treated as the intended outcome. When the metric omits a consequence, locally rational action can make the wider result worse.

Blaming the account for every undesirable action is equally weak. Changing its formula without understanding its actual use can leave the behavior intact or remove useful information.

### MA.9:3 - Forces

Measures simplify work and make some effects easier to see. A more comprehensive measure may be harder to interpret and can create different incentives.

A repair should address the actual decision arrangement at warranted effort. Adding more targets can increase burden without correcting the reason people acted as they did.

### MA.9:4 - Solution

#### MA.9:4.1 - Recover the account and how people use it

Identify the measured quantity, calculation, participant and decision or reward it affects. Ask the affected people what actions they can take and how the account enters the choice.

Recover the intended result and the relevant resource, monetary and service consequences. MA.1–4 supply missing meanings; MA.6 distinguishes a forecast from a target or resource request.

#### MA.9:4.2 - Work through the behavior the arrangement encourages

Compare plausible actions under the actual measure and its use. Calculate how each affects the reported result and the consequence the organization or participant needs.

Look for a specific divergence: producing more can lower an assigned unit cost while increasing unsold stock; moving a cost can improve one unit's account while leaving the total unchanged. The divergence identifies a hypothesis about behavior, not proof that the measure caused an observed action.

#### MA.9:4.3 - Inspect actual effects and rival explanations

Use records, participant accounts and other adequate evidence to establish what happened and why it may have happened. Examine rivals that would lead to a different repair, such as anticipated demand, a justified reserve, a supply constraint or a changed instruction.

Retain uncertainty about cause. If the contemplated change requires stronger evidence, use the applicable inquiry method. A bounded trial can be useful where it is appropriate and authorized.

#### MA.9:4.4 - Change the account or its use where warranted

Choose the smallest change that addresses the established problem: clarify a denominator, separate meanings, change the performance interpretation or provide a missing consequence alongside the existing figure. Preserve information still needed for legitimate reporting and decisions.

If the repair changes reward or authority arrangements, use [OCE][OCE] to plan the necessary organizational work and have the responsible people make the change effective.

Specify what observable consequence would indicate improvement or a new problem. Revisit the actual use after the change, keeping changes in demand and other conditions available for interpretation.

### MA.9:5 - Archetypal Grounding

An internal production report divides total production cost by units produced. Under supplied conditions, materials cost 2 per unit and the period's resource-supply payment remains 300. Producing 100 units gives **(200 + 300) / 100 = 5 per unit**.

The manager can produce 120 units with the same resource payment. The report then shows **(240 + 300) / 120 = 4.5 per unit**. The metric improves while material payments rise by **40**.

Suppose the period's sales remain 60 units and no supplied evidence supports a need for the extra stock. Unsold quantity rises from **40 to 60**. The account has made additional production look attractive without displaying the changed cash use and inventory burden. MA.4 supplies any needed reconciliation with the actual reporting policy.

The analyst now inspects the action. Was production increased to improve the target, in anticipation of later demand, or for another operating reason? Adequate evidence of a warranted future requirement could justify the extra production despite this period's unchanged sales. The unit-cost calculation alone settles neither explanation.

If the target's use is the supported problem, the responsible manager can stop interpreting lower unit cost alone as improved performance and examine the relevant demand, inventory and resource consequences together. Subsequent observations test whether the changed use reduces unwarranted production without damaging needed provision.

### MA.9:6 - Bias-Annotation

A critic of performance measures can overattribute behavior to the metric; the person who designed it can dismiss inconvenient effects as misuse. Examine the actual arrangement and rival causes.

### MA.9:7 - Conformance Checklist

Examine whether the measure and actual use are clear; the intended result and affected participants are identified; plausible actions expose a consequential divergence; causal claims have adequate support and rival explanations; and the proposed change preserves needed information with observable follow-up consequences.

An arithmetic incentive example establishes a possible mechanism. Actual behavioral improvement needs evidence from the changed arrangement.

### MA.9:8 - Common Anti-Patterns and How to Avoid Them

**Celebrating the ratio while omitting the resource consequence.** Examine the numerator, denominator and actual result together.

**Treating a plausible incentive as proven cause.** Investigate action-changing rival explanations.

**Deleting a required report to repair its managerial misuse.** Preserve the legitimate account and change the use or companion information that caused the problem.

### MA.9:9 - Consequences

The user can identify when an account's use directs effort away from the intended result and can choose a more specific repair. Useful measures and legitimate reports remain available.

The work can reveal an organizational issue beyond accounting. Evidence of the repair's effect may take time and remains conditional on the operating context.

### MA.9:10 - Architectural Rationale

The method examines the account together with its use because a formula alone does not determine behavior. The same unit cost can be useful for one comparison and harmful as a universal performance target.

A clarified interpretation can be sufficient for a bounded misuse. Wider measurement or organizational redesign is justified when the actual decision and incentive arrangement continues to produce the problem.

### MA.9:11 - SoTA-Echoing

The selected line combines the constraint-accounting critique of local cost optimization with Bogsnes's distinction between expectations and negotiated performance numbers. Bragg's inventory discussion and Caspari and Caspari's fixture case supply historical mechanisms by which a local account can conceal a wider consequence.

The adaptation adds explicit examination of actual use and rival causes in §§4.1–4.3. At the effort of comparing two production quantities, the example reveals an incentive that a lower-unit-cost verdict would miss. It does not infer actual causal improvement from the counterexample.

Reopen the repair when observed behavior, decision use or the required information changes, or when the supposed improvement moves burden elsewhere.

### MA.9:12 - Relations

MA.1–4 explain resource and account effects; MA.5–6 clarify forecasts, targets and resources; MA.7 separates arithmetic differences from causal explanations; MA.8 supplies longer-term customer or product consequences. OCE guides wider organizational change; the responsible people decide and make it effective under the applicable rules. C.11.DUA supports an unresolved further-inquiry decision.

### MA.9:End

# References

Copyright © Anatoly Levenchuk. The original framework text and worked examples are licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). The [licensing notice](https://github.com/ailev/FPF/blob/main/LICENSING.md) states the scope and attribution terms. Referenced third-party works retain their own terms.

## Edition record

**MA 1.0** is the first edition of *Management Accounting Principles Framework*, containing MA.1–MA.9. Cite this edition with the pattern and section, for example **MA 1.0, MA.2:5**.

## Source locators


- IMA, *Developing an Effective Managerial Costing Model* (2019): the resource-model construction and use-dependent sophistication discussed in MA.1.
- Steven M. Bragg, *Throughput Accounting: A Guide to Constraint Management* (2007), printed pp.44–47, 84–86 and 111–112: bounded pricing, model assumptions and inventory reconciliation.
- John A. Caspari and Pamela Caspari, *Management Dynamics: Merging Constraints Accounting to Drive Improvement* (2004), printed pp.1–11: the fixture and capacity counterexample.
- Steve Tendon and Daniel Doiron, *Tame your Work Flow* (2020), chapter 7: the capacity and financial-measure arguments qualified in MA.2.
- Bjarte Bogsnes, *Implementing Beyond Budgeting*, second edition (2016), printed pp.139–142 and 159–166: purpose separation and actionable forecasting.
- [IAS 2, IFRS Foundation overview][IAS2]: the inventory-cost and expense-recognition comparator used in MA.4.
- [Beyond Budgeting principles][BB]: the current source for the separate management purposes used in MA.5–6.
- Peter S. Fader and Bruce G. S. Hardie, [What's Wrong With This CLV Formula?][CLV] (2014), and Fader, Hardie, Liu, Davin and Steenburgh, [How to Project Customer Retention Revisited: The Role of Duration Dependence][RETENTION] (preprint page updated 2018): the bounded population, horizon and retention qualifications in MA.8.

[OPS]: OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md
[IMA2019]: https://prodcm.imanet.org/-/media/IMA/Files/Home/Insights-and-Trends/Thought-Leadership/Strategic-Cost-Management/Developing-an-Effective-MC-Model_SMA.ashx
[DUA]: ../FPF-Spec.md#c11dua---decision-useful-advice-and-evidence-demands
[MEAS]: ../FPF-Spec.md#c16---measurement-metrics-characterization-mmchr
[IAS2]: https://www.ifrs.org/issued-standards/list-of-standards/ias-2-inventories/
[BB]: https://bbrt.org/wp-content/uploads/bb_principles.pdf
[OCE]: ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md
[CLV]: https://www.brucehardie.com/notes/033/what_is_wrong_with_this_CLV_formula.pdf
[RETENTION]: https://brucehardie.com/papers/037/
