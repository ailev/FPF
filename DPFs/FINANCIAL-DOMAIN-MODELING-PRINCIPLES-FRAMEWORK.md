# Financial Domain Modeling Principles Framework

**DocID:** `FDM` within **FPF Library**.

**Edition:** [FDM 1.0](#fdmsources1---edition-record)

**Author:** Anatoly Levenchuk, with AI-assisted development and review

Use Financial Domain Modeling to establish whose financial position a model describes, which events can change it or how a service contributes to a participant’s result. Its five methods connect parties and their rights or obligations with contractual flows, actual events and the use of a service.

# Table of Contents

**Reader entry**

| § | Publication unit | Use |
| --- | --- | --- |
| R | [Financial Domain Modeling Readme](#financial-domain-modeling-readme) | Connect service use, financial positions, conditional events and actual effects. |
| P | [Financial Domain Modeling Principles Framework Architectural Reference](#financial-domain-modeling-principles-framework-architectural-reference) | Understand the connected methods, alternatives and limits. |
| FDM.Reference:1 | [The working problem](#fdmreference1---the-working-problem) |  |
| FDM.Reference:2 | [How the methods connect](#fdmreference2---how-the-methods-connect) |  |
| FDM.Reference:3 | [Connect models by the financial question](#fdmreference3---connect-models-by-the-financial-question) |  |
| FDM.Reference:4 | [Parties, resources and several useful structures](#fdmreference4---parties-resources-and-several-useful-structures) |  |
| FDM.Reference:5 | [Practical gain, cost and evidence](#fdmreference5---practical-gain-cost-and-evidence) |  |
| FDM.Reference:6 | [Source choices and alternatives](#fdmreference6---source-choices-and-alternatives) |  |
| FDM.Reference:7 | [Using the connected account correctly](#fdmreference7---using-the-connected-account-correctly) |  |
| FDM.Sources:1 | [Edition record](#fdmsources1---edition-record) |  |
| FDM.Sources:2 | [Source locators](#fdmsources2---source-locators) |  |
| FDM.Sources | [Financial Domain Modeling Principles Framework Sources and Edition Notes](#financial-domain-modeling-principles-framework-sources-and-edition-notes) |  |

**Patterns**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| --- | --- | --- | --- | --- |
| 1 | [FDM.1 - Recover the Financial Position Behind a Record](#fdm1---recover-the-financial-position-behind-a-record) | Stable | Right, duty and record; score; loan position | A.2.8 and A.2.8.PER; FDM.2 for a disputed party. |
| 2 | [FDM.2 - Choose Party and Group Boundaries for Financial Modeling](#fdm2---choose-party-and-group-boundaries-for-financial-modeling) | Stable | Debtor; entity; fund; founder group; guarantee; usable cash | FDM.1 for positions; SIE.5–6 for identity and composition. |
| 3 | [FDM.3 - Derive Events and Conditional Flows from Financial Contract Terms](#fdm3---derive-events-and-conditional-flows-from-financial-contract-terms) | Stable | Principal; accrued interest; payment allocation; calendar; guarantee trigger; conditional and actual flow | FDM.1–2 for terms and parties. Use FDM.4 to establish actual effects. |
| 4 | [FDM.4 - Establish What a Financial Action Changed](#fdm4---establish-what-a-financial-action-changed) | Stable | Approval; instruction; posting; payment; effect; residual obligation | Relevant positions, parties and terms from FDM.1–3 or existing sources. Applicable institutional rules and evidence for the event in question. |
| 5 | [FDM.5 - Trace a Financial Service to a Participant's Result](#fdm5---trace-a-financial-service-to-a-participants-result) | Stable | Score use; admission; financial benefit; service output | FDM.1–4 when financial meaning or effect is missing; relevant decision practice. |

# Financial Domain Modeling Readme

## Practical entries

Start with the financial question and the results already established. To explain what a service contributed, you may need an account of a position or event. A newly established payment may require revising an earlier claim about what funds were available. Use the Table of Contents to go directly to a method. The cases below show how to combine them.

**FDM** is the reference code for this framework. FDM.3:4.2 identifies section 4.2 of pattern 3. You can apply the methods yourself or ask an agent to model the case or explain it in the language of your work. The examples stipulate their terms and facts. For an actual arrangement, use the applicable financial and institutional interpretation.

### FDM-E1 — A score is presented as a financial benefit

- **Situation:** A better score is reported as a benefit to a borrower, but the financial change is unclear.
- **Question:** What did the service change for this participant, and what remains unresolved?
- **First useful result or blocker:** A supported contribution to the participant's result, an unchanged financial outcome, or a missing term or event.
- **Start with:** FDM.5 to examine how the service was used. Use a position or event method if the claimed change depends on a question still open.
- **Stop or return:** Report the established contribution and any material limit. Reconsider a term, occurrence or link to the participant’s outcome when the conclusion depends on it.

A scoring team improves the accuracy of its output and wants to explain the benefit to a borrower. Use [FDM.5](#fdm5---trace-a-financial-service-to-a-participants-result) to identify how the score affects the decision. If the applicable rule gives this borrower the same decision and terms at both scores, the gain in accuracy produces no difference through that route. That can answer the question. A claim that the borrower spent less time supplying information requires its own comparison.

Suppose an authorized decision maker uses the new score and changes a lending decision. Use [FDM.1](#fdm1---recover-the-financial-position-behind-a-record) to identify any rights and obligations created under the applicable terms. If the lender’s or borrower’s identity is disputed, use [FDM.2](#fdm2---choose-party-and-group-boundaries-for-financial-modeling) to resolve it. The agreement’s formation conditions determine which duties already exist before funding. To establish whether the funds are usable, follow the funding event.

In this example a valid agreement provides that successful funding of 100 creates a position with 105 due on day 30. Use [FDM.3](#fdm3---derive-events-and-conditional-flows-from-financial-contract-terms) to derive the contractual flows for each party and [FDM.4](#fdm4---establish-what-a-financial-action-changed) to determine what occurred and what it changed. Suppose 60 was paid and applied in full to the amount due, with no further interest or fees. The remaining obligation is 45. Reconcile a record showing 105 unpaid with that effect. The original contractual amount remains 105. If the evidence establishes only an instruction to pay 60, the payment and its effect remain open.

Use FDM.5 to explain what the financial service supplied. Funding may make the agreed proceeds usable even if the equipment bought with them never arrives. Report the funding and the failed delivery in their respective scopes. A later business benefit requires evidence that the financed work produced it.

For unclear terms, use FDM.1 or FDM.3. For a disputed occurrence, use FDM.4. For a gap between the service output and the participant’s result, use FDM.5. In each case, apply a sufficient existing result directly.

### FDM-E2 — A group's cash is used to justify one entity's payment

- **Situation:** A group's cash balance is used to claim that one member can pay a debt.
- **Question:** Which funds can this entity actually use by the due date?
- **First useful result or blocker:** The resources available to the entity by the due date and any shortfall, or the particular support term or receipt that remains uncertain.
- **Start with:** FDM.2 for the payment boundary, then FDM.1 and FDM.3 for support terms and FDM.4 for what occurred.
- **Stop or return:** Report what the entity could use by the due date. Revisit a conclusion about availability or support if a relevant event or term changes.

X owes 100 on day 7 and has 20 of unrestricted cash available then, after all its other receipts and obligations. Y has 150. X and Y share a founder. Use [FDM.2](#fdm2---choose-party-and-group-boundaries-for-financial-modeling) to distinguish exposure to the founder group from X’s ability to pay. On the supplied facts X is short of 80. Adding the two balances establishes no right or means for X to use Y’s cash.

Suppose Y undertakes to transfer 80 to X before day 7. Use FDM.1 to establish the obligation and its parties and FDM.3 to derive the conditions and timing of the transfer. A guarantee payable to the creditor after X fails and a valid demand is made gives the creditor a conditional recovery route. Performance of that guarantee would pay the creditor. It would not give X cash to make the original day-7 payment. If the terms leave the timing of support open, report that limit.

Use FDM.4 to examine the event that would make the funds usable. A support commitment, transfer permission or sent payment instruction can precede receipt. Suppose Y transfers 60 under its support obligation and X can use it before day 7, with nothing else in the cash account changed. X now has 80 and is short of 20. Y has performed 60 of its commitment of 80. Update X’s payment account with the confirmed receipt. If the deadline is still ahead, receiving the remaining 20 in time remains a conditional scenario until its outcome is established. Revise any conclusion inconsistent with the established events.

The question can end with the amount available or with a precise limit if receipt is unknown. When a financing or payment choice is needed, the responsible party can use that result to compare its options. For portfolio risk, common dependence on the founder may matter even when X cannot use Y’s funds. Keep the group exposure distinct from the cash available to X.

# Financial Domain Modeling Principles Framework Architectural Reference

## FDM.Reference:1 - The working problem

Financial work connects institutional relations with resources, records and possible future events. A borrower can have an obligation before a reporting system displays it. A displayed receivable can be disputed or already discharged. Money in a related company's account can be relevant to an exposure analysis while remaining unavailable for the borrower's next payment.

Establish the parties, meanings, event conditions and effects that a financial question, service or connected model needs. A table, diagram or software model can express the answer. Its claims depend on the applicable terms, events and their evidence.

Consider a loan with an advance of 100 and a contractual payment of 105 on day 30. A scoring method, the calculator implementing it and the score in this case are different objects. An authorized decision maker can use the score. An agreement creates rights and obligations under its formation conditions, funding can make proceeds available, and a later payment may discharge part of what is due. Trace the relevant steps to identify the score’s contribution or where it fell short.

## FDM.Reference:2 - How the methods connect

Use FDM.1 to recover the financial position described by a record and FDM.2 to establish the parties or grouping the question requires. Either result can suffice. A lender asking who owes an amount may already have all the information needed once the entity is identified.

With sufficient terms and party identities, use FDM.3 to derive what the contract requires when its conditions hold. Scenario assumptions can support conditional flows. Expected flows also require a basis for the expectations. For actual performance, use FDM.4 to establish an occurrence and its effect, such as a remaining obligation. An unresolved institutional condition can limit the finding.

When a flow must be derived, use FDM.1:4.2 to establish the operative terms and interpretations that matter. In FDM.3:4.2–4.3, connect each condition to its consequence, identify the relevant state and dates, then derive the amount and next state. The partial-payment and guarantee cases show how to adapt the construction. For a settled fixed payment, the two-row account in FDM.3:5.1 can suffice.

Use FDM.5 to trace a service output through its use to a participant’s financial result. If the connection depends on the meaning of a position or the effect of an event, establish that contribution. In the other direction, a known financial change may raise a question about whom it served. Follow the connection needed for the task.

Interpreting a payment under a contract can be part of deriving the remaining obligation and thus of explaining the borrower’s position. Use [FPF B.1.5.EW — Recover How Constituent Actions Enact Encompassing Work][EW] when you need to establish how those actions contribute to the present modeling work or which capability is missing. FDM.4:5.2 shows why correct subtraction may leave the position unresolved. The bank transfer itself is an occurrence the modeler can observe, even while building the account.

## FDM.Reference:3 - Connect models by the financial question

Suppose a lending model stores “loan amount = 100” for the principal, while a payment model requires the amount payable at maturity. Equal-looking field names do not establish an adequate correspondence.

Use FDM.1 and FDM.2 to check that both models refer to the same lender, borrower and contract. The terms used with FDM.3 give principal of 100 and a payment of 105 in the stated currency on day 30. With [SIE.4][SIE], connect the principal field to the principal input and derive the maturity value from the terms. Copying 100 into the maturity field would understate the amount due by 5.

Use [SIE.5][SIE] to preserve the party and contract identities and [SIE.6][SIE] to combine statements with their meanings, currency and time. Use [SIE.3][SIE] to assess whether the models answer the receiving question or need an extension.

For this example, assume the advance of 100 has occurred and sufficient evidence establishes it. Under the supplied terms, funding creates an obligation to pay 105 on day 30.

| Receiving question | Financial statement needed | Meaning that a connection must preserve |
| --- | --- | --- |
| How much was advanced? | Principal advance of 100 under the supplied terms. | The amount advanced. |
| What is contractually due at maturity? | Payment of 105 on day 30. | The contractual amount and event conditions. |
| What was actually paid? | An adequately established payment of 60. | The actual occurrence, with its relevant dates. |
| What remains due after that payment? | 45 under the supplied application rule, with no further fees or interest. | The effect of payment on the obligation. |

Use FDM.4 to establish the advance, the payment and what remains due. Keep the original contractual schedule alongside the observed performance when reporting or modeling risk needs both. The connection is adequate when it answers the receiving question or shows precisely which premise remains unresolved.

[FIBO][FIBO] describes financial concepts and their relations. [ACTUS][ACTUS] supplies logic for deriving scheduled contractual events from terms. A model may need either or both. To implement a correspondence, inspect the definitions, terms, encoding and outputs on which it relies.

## FDM.Reference:4 - Parties, resources and several useful structures

A founder-group account, legal-entity account and portfolio-risk account can all be useful. They answer different questions. A common founder can matter to correlated exposures, governance or expected support; the relation alone does not identify another entity as the debtor or make its funds available.

Give the criterion and use for each grouping. To sum balances, check the parties, dates, currencies, restrictions and relations the aggregate depends on. One organizational tree may suffice for a report and omit a relation another question needs. Use [SIE.5 through SIE.6][SIE] to resolve identity or composition where necessary.

The same discipline applies within a loan. The lender's right, the borrower's duty, a bank-account record, usable proceeds and equipment acquired with those proceeds are different subjects. Their relationships explain the financial service.

## FDM.Reference:5 - Practical gain, cost and evidence

The first gain is a smaller, better defined question. A payment report may need only a corrected party reference or a distinction between due and paid. A service design may need to locate who actually uses a score. A disputed obligation may require the applicable institutional rule and evidence of the event it recognizes.

Detailed models take time to build and maintain. Begin with what existing accounts establish. Add detail when a plausible difference matters to the requested finding or action. The result can be a supported position or model, a finding that nothing changed, or a precise limit on what is known.

A score presented as a benefit or a group balance presented as available cash gives reason to examine the claim. To establish a financial effect, use evidence for the parties, terms, event and consequence on which it depends. For a quantitative benefit, support the comparison and qualify its uncertainty. The numerical cases in this book stipulate their terms.

## FDM.Reference:6 - Source choices and alternatives

The loan and group-funding cases connect a description to the financial relation it concerns and to what using it changes for a participant. A tool supplier can deliver information to a different decision maker. An authorized automated service can itself act on the information. Establish a duty or permission from the applicable institutional conditions and distinguish it from its description. When assessing increased admissions, consider suitability, legitimate refusals and the purposes of the participants under those conditions.

Use [FPF A.2.8][DUTY] for duties, [FPF A.2.8.PER][PER] for permissions and [FPF A.2.9][ACT] for communicative work. Use ADM for the administrative question in the case. These distinctions matter when a financial term or record leaves the actual right, duty, permission or act unclear.

A data dictionary may answer a question about a term. To derive behavior from terms, use an event model. To establish how a service output was used and what it contributed, examine its role in the work of the participant concerned. Combine these accounts where the question connects them. Reconsider an affected conclusion when terms, institutional conditions, observed behavior or intended use change its basis.

## FDM.Reference:7 - Using the connected account correctly

Where two models join, check that they refer to compatible parties, positions, terms and times. Preserve the conditions for any projected event. For a claim about use or effect, examine whether the evidence supports that particular occurrence and consequence. Reuse adequate results while their conditions hold.

If an amount field is substituted for the amount due, recover the contractual meaning. If group cash is treated as available to one member, check that member’s access. If a service output is credited as a participant’s outcome, trace its actual use and contribution. Preserve unrelated conclusions that still have adequate grounds.

For source qualifications, citation and edition information, see the [Sources and Edition Notes](#financial-domain-modeling-principles-framework-sources-and-edition-notes).

## FDM.Reference:End

## FDM.1 - Recover the Financial Position Behind a Record

**Type:** Architectural

**Status:** Stable


### FDM.1:0 - Use this when

Use this pattern when a balance, agreement, score or label leaves unclear whose financial position it concerns or which terms apply. Identify the party and the question the record is being used to answer.

Establish the relevant right, obligation or other financial interest of the identified party under the conditions and at the time in question. Explain how the records and resources bear on that position.

Use an adequate account directly. If only the report layout has changed and the position is still established, the existing interpretation can suffice.

### FDM.1:1 - Problem frame

In financial records, “claim” can name an assertion in a report or a creditor’s right to receive something. A report may assert that a lender has such a right. Whether the right exists under the applicable terms is a separate question.

A loan agreement, a funded position, an account entry and proceeds available to the borrower can concern the same loan. Determine which of these the question requires you to establish.

### FDM.1:2 - Problem

A record's label and amount can make its financial interpretation appear settled. If the party, terms or time are wrong, a correctly copied number can still answer the wrong question. Treating the record as the position also prevents the practitioner from explaining a stale entry, disputed obligation or valid agreement that has not yet been funded.

### FDM.1:3 - Forces

Start with a sufficient existing account. If a field’s meaning, party or date is disputed and matters to the answer, recover that particular basis.

A right to future payment can be established while the payment itself remains uncertain. Qualify the account accordingly.

### FDM.1:4 - Solution

#### FDM.1:4.1 - State the financial question and relevant party

Identify what the record is meant to establish. It might concern who owes or may receive an amount, who bears a loss or what resources are available. Name the party whose position matters and any counterparty needed to interpret it. Use the stated question directly or obtain clarification where its meaning is unresolved.

If the answer depends on a disputed identity or group boundary, use FDM.2 or [SIE.5][SIE]. A trading name, group identifier or database key can locate records. Check the entity it identifies before relying on it to resolve the dispute.

#### FDM.1:4.2 - Recover the position from its applicable basis

Use the terms and institutional basis applicable to this question. Establish what right, duty or interest exists, who holds it, against whom when relevant, and with what content, conditions and timing. If its existence is disputed, state what the available basis establishes.

For a position governed by an agreement, identify the operative agreement for the parties and time in question. Include definitions, elections and amendments that affect the answer. Follow an incorporated reference when it contains a needed interest convention, guarantee notice procedure or other term. A proposal may carry the same commercial label as a concluded agreement. Check which document and status the claim relies on.

For a provision requiring or permitting action, establish who must act or may choose, what the action or election is, which condition activates it, and when it applies. Read the relevant definitions and exceptions. Preserve the provision’s location when a later user must inspect the derived rule. A few operative sentences can suffice for a simple agreement.

Where interpretation could change the result, identify the particular question. Does the weekend adjustment move the payment date alone or also the end of ordinary interest accrual for this installment? Apply an existing supported interpretation for the parties, date and use in question. If a new interpretation is needed, supply the operative text, parties, competing readings, date and intended use to a qualified interpreter, or interpret the provision within your own competence and authority. Use the supported result in the calculation. Where the reading remains open, retain the conditional results. Readings that give the same amount today can diverge at a later date.

An enforceable term can create a conditional obligation before money moves. Identify that obligation separately from the amount advanced, current principal and payments already due. Use the established position with FDM.3 when a flow question follows.

A document can provide evidence. Its execution or another recognized act can also institute a relation under the applicable rule. Establish the rule and event when the claim depends on them. A missing or stale database entry can leave an existing obligation unreported. A recording can itself have legal effect where the rule gives it that effect.

Use [FPF A.2.8][DUTY] to establish whether a particular duty exists. Use [FPF A.2.8.PER][PER] for a permission.

#### FDM.1:4.3 - Relate descriptions and resources to the position

Identify what each source describes, the time it concerns and any limitation affecting reliance. A contract description, a servicing record and a customer's statement can refer to the same loan while differing in date, purpose or evidential support.

Establish separately which resources the relevant party can use. A borrower may still owe repayment after spending all the proceeds. A lender may have a right to payment even though the borrower cannot pay now. A displayed balance can be evidence when its account meaning, date and availability conditions support the claim.

Describe a prospective position under its conditions. A score or offer can inform a decision. A valid agreement can create duties at formation before disbursement. To establish a particular position, use the conditions that actually apply to it.

#### FDM.1:4.4 - Return what is warranted for this use

Report whose financial relation is at issue, what it provides, the conditions under which it holds and the time to which the finding applies. Relate the material records to the finding and identify any discrepancy or premise the available evidence leaves open.

Use FDM.3 when the question needs conditional events and flows. Use FDM.4 when it asks whether an actual action changed the position. An established position can itself answer a report or decision question.

### FDM.1:5 - Archetypal Grounding

Suppose a lender considers advancing 100 to a borrower. The example stipulates currency, valid agreement formation and terms under which successful funding creates a position with 105 due on day 30. Identify the lender’s right, the borrower’s duty and the proceeds made available on funding.

The lender has a score of 0.72 produced by a scoring method. To interpret it as a probability, establish the meaning and scale the method assigns to it. Establish a lending decision or repayment obligation from the relevant decision and formation evidence.

Suppose the signed arrangement also obliges the lender to advance funds once a specified condition is met. This is a separate pre-funding duty under the stipulated terms. It can matter before any disbursement. If formation or the term is disputed in an actual case, report what the uncertainty leaves open.

Now suppose the advance of 100 has occurred and 105 is due on day 30. A payment of 60 is established. If all 60 applies to that obligation and no further interest or fees arise, 45 remains due. Use FDM.4 to establish that effect. The original contractual payment is still 105. Investigate a servicing record showing all 105 as unpaid when the discrepancy matters to the requested result.

### FDM.1:6 - Bias-Annotation

System designers may prefer facts represented in their own application; a contract specialist may emphasize the agreement while overlooking settlement or usable resources. Compare the accounts around the receiving financial question.

For an ownership interest or a conditional instrument, establish the relation and terms governing that interest. The lender–borrower example grounds a debt case.

### FDM.1:7 - Conformance Checklist

Check whether the proposed interpretation meets these criteria.

1. The actual party and financial question are identifiable.
2. The right, obligation or other interest has an adequate basis, content, conditions and time.
3. Assertions and records about the position remain distinguishable from the position itself.
4. Claims about available resources or expected future performance have the grounds they require in addition to the established position.
5. The result supplies an adequate answer or names the particular identity, term, rule or evidence still missing.

### FDM.1:8 - Common Anti-Patterns and How to Avoid Them

**Treating “claim” as one unambiguous object.** State whether the sentence concerns an assertion or a creditor's right. Then relate them where the report is evidence about the right.

**Making the database constitutive by default.** Establish what rule, if any, gives the relevant recording act that effect. A stale or missing entry otherwise remains a recording question.

**Deferring every duty until funds move.** Inspect the actual formation and conditional-performance terms. A valid unfunded arrangement can already have consequences.

### FDM.1:9 - Consequences

The recipient can use an amount with its financial meaning and can distinguish uncertainty about a position from uncertainty about payment. The model also makes a disagreement between records intelligible.

Recovering terms and relations concealed by a label takes work. An adequate existing account reduces that cost. An unresolved institutional interpretation limits the conclusion the model can supply.

### FDM.1:10 - Architectural Rationale

The financial position is the central subject because it is what the record is commonly used to infer. Beginning with the receiving question limits the reconstruction to distinctions that matter.

A dictionary can settle a shared term when that is the question. To establish a particular party’s right or duty, use the applicable terms and facts. Trace a financial service only when the receiving question also needs its contribution.

### FDM.1:11 - SoTA-Echoing

To interpret a financial record, distinguish what an institution establishes from what the record asserts. Apply that distinction in §§4.2–4.3 by identifying the applicable relation and connecting the relevant descriptions and resources to it.

Use FIBO to clarify a financial concept or relation obscured by a local label. Evidence that a particular party holds a right comes from its institutional basis. Recovering that basis can reveal a missing formation condition or date that renaming the field would leave open.

FINOS CDM’s [Legal Agreements model][CDM-LEGAL] distinguishes agreement identification, elections, amendments and related agreements. These distinctions help locate terms hidden by a single agreement field. For their effect in the particular case, use a supported interpretation under §4.2.

Revisit an interpretation when a change in terms, party identity or evidence could affect the account of the position. Distinguish a change in what is known from a change in the position itself.

### FDM.1:12 - Relations

FDM.2 resolves the party or group boundary; FDM.3 derives contractual behavior; FDM.4 establishes actual changes. FDM.5 uses an adequate position model when tracing a service's contribution.

Use A.2.8 for an individual duty, A.2.8.PER for permission and A.2.9 for communicative work when its occurrence matters. Use [ADM.2 through ADM.4][ADM] for the corresponding administrative participant, effectivity and account questions. SIE supplies general identity and correspondence methods. Use the applicable financial terms for the financial interpretation.

### FDM.1:End

## FDM.2 - Choose Party and Group Boundaries for Financial Modeling

**Type:** Architectural

**Status:** Stable


### FDM.2:0 - Use this when

Use this pattern when the boundary between companies, accounts, funds or groups could change the answer to a financial question. A founder’s portfolio and a reporting group can have different members. For a payment question, identify the party that must pay.

Identify the parties and underlying positions relevant to the question. Establish the grouping criterion, aggregate or support relation the use requires.

Use an adequate established boundary directly. A different display arrangement alone need not reopen an undisputed debtor or reporting subject.

### FDM.2:1 - Problem frame

One fund tracks investments by legal entity. Another groups startups that share founders. Both views can be useful. A common founder establishes that grouping but leaves each entity’s debts and accounts subject to its own terms.

Choose the relation for the question. To assess payment, establish the debtor’s timely usable resources. For portfolio risk, shared exposure can matter even where no entity supports another. For a consolidated report, apply its inclusion and elimination rules. Connect these views when the intended use needs more than one.

### FDM.2:2 - Problem

A convenient group key is often used as if it settled control, liability, support and resource availability together. Adding the members' balances then conceals the very restriction that changes the financial answer.

Separate-entity accounts can miss correlated exposure or an actual support arrangement. Choose a boundary that preserves the relation relevant to this question, and enough of the underlying positions to interpret the aggregate.

### FDM.2:3 - Forces

An aggregate simplifies comparison when it retains the distinctions that affect the conclusion. Check membership and support at the time the question concerns.

A relation can establish a duty or power, or support an expectation of voluntary action. State which applies. An expected transfer can inform a scenario. A claim of committed funding also needs evidence of the commitment.

### FDM.2:4 - Solution

#### FDM.2:4.1 - Start with the financial consequence being examined

Identify whose payment, position, exposure, control or report is at issue and the relevant time. Use the underlying entities and accounts to interpret the group label.

For a payment, identify the obligor and the funds it can use by the due date. For a portfolio question, identify the investments or exposures and what their aggregation means for risk. For a report, identify the framework adopted or required for the entity and period. Use its purpose and applicable authority to select the rules. Use [SIE.5][SIE] if entity identity or continuity is disputed.

#### FDM.2:4.2 - State why these members belong together

Choose the grouping criterion for the question. It may be a common founder, control, contractual support or inclusion under the applicable consolidation rule. Establish which parties meet the criterion at the relevant time. Retain the underlying positions needed to interpret a group result.

Different criteria can produce overlapping groups. Keep them connected when the receiving use needs them. A single hierarchy need not carry every financial relation.

#### FDM.2:4.3 - Recover what connects the positions

For a claim about support or resource availability, establish the relation that would justify it. A guarantee, committed facility, transfer permission, control relation and expected voluntary payment confer different rights or support different expectations.

Establish the parties, content, limits, conditions and timing that matter. A guarantee can give the creditor a conditional claim payable after default. It can leave the debtor without cash for the original due date. A permission allows a transfer. A commitment creates an undertaking to transfer under its terms. An actual timely transfer needs evidence of performance. Control may coexist with restrictions on the use of funds.

When a transfer is expected, state the reason for the expectation and its role in the scenario. A risk assessment can use that expectation. To include support in cash already available, establish that the debtor can use it by the relevant time.

#### FDM.2:4.4 - Build the warranted aggregate

Combine only amounts whose meaning, time, currency and inclusion rule are adequate for the receiving use. Preserve restrictions and conditional relations that can change the result.

For a reporting result, use the provisions governing consolidation, recognition, measurement or elimination, including material exceptions, or a responsible accountant’s supported treatment. If control determines a disputed boundary, establish the relevant ownership and decision rights. Apply an available qualified determination or seek one for the entity and period if the result requires it. Until then, identify which aggregate remains unresolved.

Use an established reporting boundary and treatment to identify included entities, align their accounting bases and make required adjustments. If amounts remain incompatible, explain why they have to stay separate. Use [MA.4][MA4] for account construction and reconciliation. A valuation, conversion or netting operation needs its own applicable rule.

For a disputed treatment, identify the rule or judgement that determines the operation, the parties and period it covers, and conditions that could change it. Apply a sufficient existing treatment. Establish a missing jurisdiction or reporting basis from the available authority, or obtain a determination if one is still needed.

For a payment question, derive the debtor’s usable funds at the due time after other relevant receipts and obligations. Count support from another entity according to its terms and established availability under §4.3. For a risk question, retain shared exposures and dependencies relevant to the scenarios. An exposure aggregate and a payment balance require their own meanings.

#### FDM.2:4.5 - Return the boundary and its financial meaning

Return the relevant parties and the boundary, aggregate or support conclusion they justify for this question. Identify any missing identity, term, restriction, time or aggregation rule that materially limits use.

Use [SIE.6][SIE] to combine claims once their financial meanings are established. The combined account may retain several claims, a conflict, non-comparability or an unresolved premise. Use FDM.3 to derive conditional support flows and FDM.4 to establish the effect of an actual transfer when the question requires them. An established boundary may suffice on its own.

### FDM.2:5 - Archetypal Grounding

#### FDM.2:5.1 - A founder group and one debtor

Suppose X must pay 100 on day 7. It has 20 in unrestricted cash available on that date after all other receipts and obligations, before this payment. Y holds 150 in its own account. X and Y share a founder.

The founder group includes both entities and their respective balances. On the supplied facts X is **80 short** of what it must pay. To count Y’s money towards that payment, establish how and when it becomes usable by X.

Suppose an effective arrangement requires Y to transfer 80 to X before day 7. That establishes a support obligation. Timely performance would close the gap. To count the full 80 of support in addition to X’s own 20, establish receipt or another effective means for X to use that support by the due date.

Suppose instead the guarantee can be called only after X fails to pay. Under those terms the creditor may have a further recovery route, while X still lacks cash for day 7. Use FDM.3 for the trigger, timing and beneficiary of the guarantee.

If Y has no support commitment but the founder is expected to arrange a voluntary transfer, keep that event in the scenario that assumes it. For a portfolio-risk question, common dependence on that founder or on the same market can justify examining the members together even when no transfer is possible.

#### FDM.2:5.2 - A reporting group and an internal amount

Suppose the reporting practitioner has established the reporting basis and period and determined that P and S are consolidated for that report. Their aligned standalone accounts include P's receivable of 40 from S and S's corresponding payable of 40. The supplied consolidation treatment eliminates that internal pair in the group view.

Keep P’s right to receive 40 and S’s obligation to pay 40 available for a question about S’s payment. Eliminating the internal amount from a consolidated report does not discharge S’s debt. If the reporting boundary is unresolved, use an existing determination or establish it from the applicable basis. Seek a qualified decision when one is required. A common founder alone does not establish the elimination.


### FDM.2:6 - Bias-Annotation

An investor may track shared founders while a reporting system uses a legal identifier. Test the chosen grouping against the financial consequence the question concerns.

Evidence of past voluntary support can inform an expectation. It does not by itself establish a present obligation or remove the possibility that support will arrive too late.

### FDM.2:7 - Conformance Checklist

Check the following for the stated use of the boundary.

1. The financial question, relevant time and underlying parties are clear.
2. Group membership follows an identified criterion adequate for that question.
3. Liability, control, support, permission and expected behavior remain distinct where their differences matter.
4. An aggregate retains the necessary time, currency, restrictions and applicable composition rule.
5. A claim of available funding has adequate support for timely usability, and unresolved premises remain visible.

### FDM.2:8 - Common Anti-Patterns and How to Avoid Them

**Funding X by summing X and Y.** Identify any relation and event that would make Y’s funds available to X. If none is established, keep their balances separate for X’s payment question.

**Reading a guarantee as cash in advance.** Use the actual trigger, beneficiary and payment conditions. The guarantee may answer a recovery question while leaving the immediate funding question open.

**Rejecting a useful risk group because its members are separate debtors.** Keep the debtor accounts and model the shared exposure for the risk use that needs it.

### FDM.2:9 - Consequences

Different group views can reveal shared exposure while preserving which party owes an amount and whether support is available in time. A single grouping can suffice for one of those questions.

Maintain several structures when their different uses justify the work, such as a consolidated report and a separate-entity payment account.

### FDM.2:10 - Architectural Rationale

The method begins with the consequence because there is no single group boundary that settles every financial question. It retains underlying positions so that aggregation can be interpreted and revised.

A single reporting tree is adequate when its rule and the receiving use match. Separate-entity accounts suffice for an isolated debtor question. Several connected views become useful when support, exposure and reporting differ. Their connection uses SIE's existing identity and composition methods, with the financial relations supplied here.

### FDM.2:11 - SoTA-Echoing

C.32.MWA explains how several useful structures can coexist. In a financial model, membership by founder, control or support can differ. Use SIE.5–6 when identifying the entities or composing their claims requires further work.

In §§4.1–4.4, select the boundary for the financial question, preserve the members’ positions and examine support separately. Identifying the debtor and any support relation can expose a shortfall hidden by the founder-group total. Extend the model when another material relation is needed.

[AASB 10 §19 and B86–B88][AASB10] illustrate the reporting operation. Consolidated statements on that basis require consistent accounting policies and adjustments eliminating intragroup balances. Apply the provisions that govern the report once its boundary is established. A different reporting basis calls for its own treatment.

In the X–Y example, common group membership and an obligation to provide support produce different financial conclusions. Revisit an affected conclusion when membership, support terms, restrictions, reporting basis or the receiving question changes.

### FDM.2:12 - Relations

FDM.1 supplies positions, FDM.3 their conditional flows and FDM.4 actual changes. FDM.5 uses the relevant participant boundary when examining a service result.

Use SIE.5 for an unresolved identity and SIE.6 to compose claims. Use [FPF C.32.MWA][MWA] for a financial-practice architecture question involving several structures, starting from representative performed work or a prospective case. For a disputed reporting, liability or aggregation rule, obtain the applicable accounting, legal or financial interpretation.

### FDM.2:End

## FDM.3 - Derive Events and Conditional Flows from Financial Contract Terms

**Type:** Architectural

**Status:** Stable


### FDM.3:0 - Use this when

Use this pattern when an amount or due-date field leaves unclear what an instrument requires under its terms. A payment date, draw condition, prepayment or guarantee can change the flows that the parties must arrange.

Establish the contractual events and flows relevant to the question. For a scenario, add the applicable assumptions. For a question about performance, relate the contractual or conditional account to evidence of what occurred.

Use ordinary financial arithmetic with the operative agreement or a competent interpretation of it. For an unclear term, use FDM.1:4.2 to identify which rule, date or calculation is unresolved. Obtain a supported interpretation if the result needs it, or give the conditional outcomes the available terms allow.

Use an existing schedule directly when its terms, state and assumptions match the question.

### FDM.3:1 - Problem frame

“Loan amount 100” does not say whether 100 is the advance, current principal or payment due. A repayment amount may depend on elapsed time, a reference value, an option or prior events. Its date may depend on a calendar rule rather than a number typed into a report.

What is due and what has been paid are different results. To forecast receipts from a schedule, give the assumptions about payment. To report actual receipts, use evidence of performance.

### FDM.3:2 - Problem

A flat list of amounts and dates can conceal the conditions that produce them. Treating the resulting schedule as an unconditional cash forecast then imports an unsupported performance assumption.

Recover the contractual rules and conditional outcomes that matter to the present use. A model of every contingency can cost more than the information it would supply for that question.

### FDM.3:3 - Forces

Contract terms can be precise while required inputs remain uncertain. An amount linked to a future reference value may be contractually well defined without being numerically known today.

Simplification is useful when it preserves the receiving answer. It becomes misleading when it erases an exercise condition, timing rule or priority of events that changes the amount or obligation.

### FDM.3:4 - Solution

#### FDM.3:4.1 - Recover the arrangement and intended question

Identify the relevant parties, instrument or arrangement, version of the terms and time from which the model starts. Use FDM.1 or FDM.2 for missing positions or boundaries.

Specify the requested result, such as the contractual schedule, an adverse funding scenario or the consequence of an option. To find the borrower’s next required payment, establish its obligation and the applicable event conditions. To find what it has already discharged, use evidence of performance. For its ability to pay, establish usable funds by the due date. Reuse adequate terms and schedules under their stated assumptions.

#### FDM.3:4.2 - Construct the event rules from the operative terms

Use the operative terms and supported interpretations. FDM.1 can supply them when needed. For an event relevant to the question, identify the actor or payer, any recipient, the quantity and currency where applicable, and the relevant time.

Read each material clause as a condition with a consequence. An installment can fall due on a date even though the obligation already exists. An election clause specifies an available action and the effect of a valid exercise. A floating-rate clause specifies the observation setting the rate and when it applies. An allocation clause determines how an actual or assumed receipt changes principal and interest.

Establish how to recognize the condition, calculate the consequence and carry the resulting state forward. If payments first satisfy accrued interest, calculate interest to the receipt’s effective boundary, allocate the receipt and carry the remaining principal into the next accrual interval. A field showing “payment = 1,000” leaves that allocation open.

##### FDM.3:4.2.1 - Match or adapt an available model

Assess a suitable available model against the operative rules. Choose a contract family by its behavior. Principal payable only at maturity, fixed principal installments and equal total installments require different calculations. An optional prepayment is another distinct event. Use the actual terms to determine which the loan requires or permits.

Check whether the model’s definitions and event rules express the required allocation, calendar and exercise conditions. Use a fit directly, extend a separable missing behavior when the rest remains valid, or report what the model cannot support. A software default can support a conditional scenario if stated. Use the agreement to establish its actual terms. [SIE.3][SIE] helps decide whether the model suffices and SIE.4 helps connect different representations.

For an [ACTUS][ACTUS] implementation, inspect the selected contract type’s schedule, state initialization, payoff and transition rules, together with the dictionary and implementation edition. Supply the operative terms, supported starting state and any external inputs the model needs. Compare its events with the agreement-based derivation in this case. A successful sample run establishes what that sample executed. Applying the model to another contract needs a correspondence for that contract.

##### FDM.3:4.2.2 - Construct enough state and preserve the different dates

Work back from the next calculation to identify the required state. Simple interest on unpaid principal needs that principal, the rate and the start of the interval still to accrue. Carry any accrued unpaid interest separately. An exercised option may change which events remain possible. Other instruments can require other state.

Initialize the state at the requested starting time from supported history or an adequate opening account. After a repayment, the original principal may give a wrong forecast. After a rate change, today’s rate may give a wrong amount for an earlier interval. Use the intervening event or an adequate opening value. If neither is available, identify the later quantities that remain conditional.

Generate recurring dates from the specified anchor, interval and end condition. Preserve a short final period or end-of-month rule where the agreement requires it. Then determine which dates the business-day convention changes. The date used to calculate interest, the date on which payment is due and the date on which a transfer actually settles can differ. Notice and observation dates can add further relevant boundaries.

When a rate or principal changes, split the accrual interval at the effective boundary and apply each value during its interval. If events coincide, use the order supported by the terms or a qualified interpretation. Calculate each event from the state its rule requires. A spreadsheet row order needs a financial basis before it can determine the result.

#### FDM.3:4.3 - Derive and inspect contractual behavior

Work through the relevant events in their applicable order. Keep the operative terms, supplied input values and derived amounts distinguishable enough to inspect.

For a simple-interest interval with constant principal **P** and annual rate **r**, the constructed case below uses **P × r × d / 365**, where **d** is its specified actual-day count. Other conventions require their own supplied calculation. Keep the rule that selects the dates beside the arithmetic.

At an event, bring any required accrual to the applicable boundary. Determine the amount payable or noncash consequence, then apply the rule for the next state. For a receipt **C** allocated to interest first, compute payable interest **I**, apply the smaller of **C** and **I** to it and apply any permitted remainder to principal. If **C < I**, carry unpaid interest forward as the terms require. Use the arrangement’s rules for rounding, excess receipts and other allocations. Where capitalization is specified, add the eligible interest to principal without a cash payment.

At the due date, derive what is payable. A forecast may assume that the borrower pays it. To report an actual discharge, use FDM.4 with evidence of the event the terms recognize. Keep outstanding principal and interest until discharge or another effective change is established. A forecasting engine that clears its balance at scheduled maturity establishes only the state of that forecast.

Give the receiving user the starting position, operative rule, event condition, dates, amount and next state needed to reconstruct the result. A short table can suffice. An executable model can help with repeated or interacting calculations. Where users must inspect its result, show how a representative event answers their financial question.

Check derived flows and state changes against the terms under conditions representative of the claimed use. Examine a relevant boundary when the date, event order, exercise or allocation can change the result. Correct arithmetic still depends on the party, meaning of the amount and starting state. Use a simple two-row account for a fixed-payment loan when it suffices. Add branches or an executable model for behavior the question needs.

#### FDM.3:4.4 - Add scenarios and performance without replacing the contract

For a scenario, state the assumptions that affect the result, such as market values, option exercise, default or recovery. Derive the conditional flows. A probability or expectation needs a basis appropriate to the claim, including explicitly supplied weights for a conditional calculation.

Preserve contractual flows alongside scenarios or expectations when the receiving use needs those different amounts. Expected receipts combine possible outcomes under a model. Actual receipts require evidence of performance. Use FDM.4 to establish their effect on the remaining position.

For a financing choice, valuation or funding question, supply the qualified flows to the method that needs them. Use [FIN.10][FIN10] to compare financing terms and [FIN.2][FIN2] to relate dated amounts to usable funds. Discounting, risk treatment and rules for choosing an alternative require their respective grounds.

#### FDM.3:4.5 - Return and adapt the model for its receiving use

Return the contractual or conditional flows with the parties, timing rules and assumptions the question needs. An unknown future market value can leave a usable formula. Competing readings of a term may give different formulas or dates. When no single value is established, give the supported range, conditional branches or precise unresolved amount.

Distinguish an observation, exercise of an existing right, an amendment and correction of a record. A new market fixing gives an input to an existing rule. An effective amendment may change the rule. A late bank confirmation can establish a receipt that occurred earlier. Update the state, rule or evidence that actually changed.

For a valid prospective amendment, preserve established history and apply the revised rule from its effective boundary. Recompute dependent later events. If effectivity or treatment of prior accrual is unresolved, qualify the affected amount and obtain an interpretation when it is needed. Use [ADM.3 and ADM.10][ADM] for the temporal or performance question.

Revisit the affected calculation when the relevant state, scenario premise or intended use changes. Use FDM.4 for the established effects needed to update actual state. Use FDM.5 for a question about how the model contributed to a service result. Preserve the basis of an opening value or changed rule when a later user needs it.

### FDM.3:5 - Archetypal Grounding

#### FDM.3:5.1 - A fixed payment, expected receipt and actual payment

Suppose a lender advances 100 and the borrower owes one payment of 105 on day 30. The case stipulates valid formation, currency and fixed payment terms. The two parties’ cash flows under the schedule are shown below.

| Event | Lender's cash flow under the stated schedule | Borrower's cash flow under the same schedule |
| --- | ---: | ---: |
| Successful advance | −100 | +100 |
| Contractual payment on day 30 | +105 | −105 |

The signs follow each party’s viewpoint. The second row states what is due under the contract. An actual receipt requires a payment under the applicable conditions.

Suppose a performance model assigns an 80% probability to receipt of 105 and a 20% probability to receipt of 60 on day 30. Its conditional expected receipt is **0.8 × 105 + 0.2 × 60 = 96**. The probabilities are stipulated. Interpreting an unexplained score as a probability would require a separate basis. The contractual amount is 105, and no discounting enters this calculation.

If the actual payment is 60, report that receipt separately. Under the example’s allocation rule, all 60 applies to the obligation. With no additional fees or interest, 45 remains due. The original contractual payment remains 105. Use FDM.4 to establish the actual effect.

Suppose an arrangement specifies support of 80 for X’s debt after a stated failure and valid demand. Identify the beneficiary and payment date from the provisions governing them. If the creditor receives the payment after default, it supplies no cash to X for the original day-7 payment. If the terms leave the recipient or timing open, report the resulting limit.

#### FDM.3:5.2 - Constructing a partial payment and a shifted due date

What must B arrange to pay on the next due date after lender L receives an early payment of 1,000? Both parties use USD. The example stipulates an effective agreement, identified parties and the following terms governing these events.

| Supplied term | Modeling consequence to derive |
| --- | --- |
| L advances 3,650 to B on 2 April 2026. | The advance creates principal of 3,650 when it occurs; it is a cash inflow for B and outflow for L. |
| Ordinary interest is simple, 10% annually on unpaid principal, actual days divided by 365. An interval includes its first date and excludes its last. Interest itself bears no interest. | Split an interval when principal changes. Carry accrued interest separately until paid; no capitalization. |
| Remaining principal and ordinary interest are payable on 2 May. A nonbusiness payment date moves to the following business day without extending ordinary interest accrual. In this example Monday–Friday are business days and there are no holidays. | Accrual ends on 2 May. Payment is due on 4 May under the stipulated calendar. |
| B may make an early payment on a business day after valid notice received at least one business day earlier. An effective receipt first pays all interest accrued to that date, rounded to cents, then principal. There is no early-payment fee. | A notice enables the action but changes no amount by itself. Accrue first, allocate the receipt, then use the reduced principal. |
| Payment takes effect on irrevocable credit to L’s designated account. All effective dates here are treated as the beginning of that date. | A submitted instruction establishes submission. Principal changes on the recognized effective receipt under the allocation terms. |
| No other payment, fee, rate change or capitalization affects this calculation. Round interest to the nearest cent, halves upward, when it is paid; final interest is rounded once at maturity payment. | The example's arithmetic needs no guessed charges or daily rounding. Questions about later default charges require their separate terms. |

The history establishes the 2 April advance, valid notice on 16 April and irrevocable credit of 1,000 on 17 April. For these confirmed transfers, both parties' corresponding cash movements occurred on the stated dates. The account is prepared just after the 17 April receipt. The future path assumes full payment on 4 May, with B's debit and L's irrevocable credit both on that date.

The 1,000 receipt includes interest and principal. Fifteen days of interest on 3,650 at 10% per year using actual/365 give 15.00. Apply 15.00 to interest and the remaining 985.00 to principal. Principal becomes 2,665.00 and unpaid accrued interest becomes zero.

| Event or boundary | Cash for B | Derived state or required payment |
| --- | --- | --- |
| Confirmed advance, 2 April | +3,650.00 | Principal 3,650.00; interest starts accruing. |
| Accrual to 17 April, before receipt allocation | 0 | Interest 3,650 × 0.10 × 15 / 365 = 15.00. |
| Confirmed receipt, 17 April | −1,000.00 | Pay interest 15.00 and principal 985.00; principal 2,665.00, unpaid interest zero. |
| Ordinary accrual endpoint, 2 May | 0 | Another 15 days produce unrounded interest 10.95205479… . |
| Payment due, 4 May | −2,675.95 if fully performed | Principal 2,665.00 plus rounded interest 10.95. Actual discharge still depends on the receipt condition. |

The amount due comprises the principal and interest being demanded. Adding it to those balances would count them twice. The transfer signs reverse for L. Use the terms to identify how the corresponding bank movements affected the obligation.

The first interval accrues on the 3,650 then outstanding. The next accrues on 2,665. Payment moves to Monday while ordinary accrual stops on Saturday. Subtracting the full 1,000 from principal would omit the interest allocation. Applying 2,665 to the first interval would use a principal that arose later.

Suppose instead that ordinary interest runs to the adjusted payment date. Keep the established first receipt and its allocation. The later interval increases from 15 to 17 days. Its interest is 12.41232877… and 2,677.41 falls due. B’s provision of 2,676 covers the original amount and falls short by 1.41 under the changed term. If the operative text leaves the end date open, report both conditional amounts and the unresolved interpretation.

Return to the original terms, with ordinary accrual ending on 2 May. Now suppose the 17 April record establishes only a submitted instruction and its effect is unknown. Keep the confirmed advance. To determine actual principal, use qualified evidence of whether and when that attempt produced irrevocable credit, or seek the provider’s result if needed. Principal of 2,665 is conditional on credit on 17 April. If the attempt failed and no other receipt occurred, principal is 3,650. Ordinary interest through 2 May is 30.00 and 3,680.00 is due on 4 May. A credit on a different date requires splitting accrual at that date. If its outcome remains unknown, return the affected possibilities.

If the confirmed 1,000 instead belongs to a refundable collateral arrangement, use FDM.4 to establish its effect. The same transfer amount and date can create a collateral position and leave the loan principal unchanged. FDM.4:5.2 develops that distinction.

For a funding question, use [FIN.2][FIN2] with the qualified amount, due date and B’s usable funds. Use [FIN.10][FIN10] to compare financing arrangements when needed. Use FDM.5 to establish whether a treasury service used the model, arranged the required payment and produced a claimed contribution. The calculation itself can answer the question about how much is due.

#### FDM.3:5.3 - Constructing the payment conditions of a guarantee

Suppose G separately guarantees L up to 2,000 of B’s unpaid principal on the loan in §5.2. Payment requires the principal due date to have passed, two following business days to have elapsed without cure, and G to have received a valid demand. It falls due two following business days after that demand. Use the same weekday-only calendar. Can this guarantee give B funds for the payment on 4 May?

Construct the condition as a conjunction. A principal shortfall alone supplies only one part. Keep the outstanding covered principal from the loan, the end of the cure interval and the demand's validity and receipt as distinct inputs. When all activation conditions hold, the amount is the lesser of covered unpaid principal and 2,000; the recipient is L. A scenario assumption about default cannot substitute for an actual valid demand.

Suppose B makes no maturity payment and no intervening event reduces principal. The two following business days are 5 and 6 May. A valid demand received on 7 May makes payment due on 11 May, with 8 and 11 May the two following business days. Covered principal is 2,665, so 2,000 of the guarantee is due to L on this branch.

The guarantee provides B with no funds for 4 May. It may protect L against part of a later loss or affect a separate offer of financing. For an actual guarantee payment, use FDM.4 to establish its effect on L’s claim and any claim G acquires against B. A payment of 2,000 to L can change the holder of a claim without reducing B’s total obligations by the same amount.

Derive the trigger, qualifying action, beneficiary and due date together. Entering the guarantee limit as a loan payment omits the conditions that produce the event. If demand validity is unresolved, give the conditional event. Use a qualified determination of validity if the question needs a definite outcome. Other established loan amounts remain available.

### FDM.3:6 - Bias-Annotation

A precise formula can attract more confidence than its inputs deserve. Keep the source and uncertainty of performance assumptions visible, especially when a score has been converted into a probability.

A familiar simple loan can also bias the interpretation of another instrument. Use its actual terms; a repeated software field name does not establish the same event behavior.

### FDM.3:7 - Conformance Checklist

Check the following for the intended use of the flows.

1. The arrangement, parties, relevant terms and initial state are identified.
2. Event conditions, amounts, currencies, timing and state updates follow the applicable terms or explicit assumptions.
3. The representation retains the branches and ordering that can change the answer.
4. Contractual, scenario, expected and actual flows remain distinguishable.
5. Missing terms and uncertain inputs are exposed where they affect the result.
6. A valuation or decision claim uses the further method and evidence it requires.

### FDM.3:8 - Common Anti-Patterns and How to Avoid Them

**Using principal as the maturity payment.** Recover the amount's contractual meaning and derive the payment from the terms.

**Treating a schedule as a receipt forecast.** State the performance assumptions and retain the contractual obligation separately.

**Applying an undocumented default.** Establish whether the chosen convention belongs to the actual arrangement. If it is only a scenario assumption, say so where it changes the flow.

### FDM.3:9 - Consequences

The user can explain where an amount or date comes from and can compare contractual requirements with conditional and actual outcomes. The result can feed funding, risk, reporting or service work.

An amount that previously appeared definite may depend on an unresolved term or unknown input. A conditional amount or formula can still be usable. More complex instruments usually require more work to construct and maintain the model.

### FDM.3:10 - Architectural Rationale

An instrument’s behavior follows from how terms and events change its state over time. An amount-and-date record can suffice for a fixed obligation. Extend it when the question depends on conditions that change the result.

Separating contractual behavior from performance keeps both interpretable. A single blended “forecast cash flow” can be useful to its intended decision, but its construction must retain the contractual and scenario meanings needed to explain or revise it.

### FDM.3:11 - SoTA-Echoing

ACTUS supplies event schedules, state initialization, payoff calculations and state transitions. Its [technical specification v1.1][ACTUS-SPEC] (2020) gives a historical example in the PAM prepayment rule, which brings accrual to the event before reducing principal. The [terms dictionary][ACTUS-TERMS] v1.4 (8 December 2023) distinguishes shifting a calculation date from shifting a payment date under the applicable business-day convention. These distinctions inform §§4.2–4.3. To use an ACTUS implementation for the loan above, check how its date and event rules map to that loan’s agreed treatment, including the maturity date.

The [ACTUS analytics account][ACTUS-ANALYTICS] relates contract inputs and external risk factors to analytical uses. Its [Quick Start][ACTUS-QUICKSTART] gives an implementation entry. A spreadsheet can suffice for an inspectable small calculation. Repeated or interacting events may justify an event engine and its mapping and maintenance costs. Use the selected edition’s specification and dictionary to map the operative terms and check the resulting behavior.

FINOS CDM’s [Event Model, version 7.0.0][CDM-EVENT] describes trade state and changes. An amendment, an observed reset and a transfer have different effects. Use this distinction in §4.5 to separate rule changes, new inputs and evidence of performance. The state-and-event representation serves lifecycle integration. To derive contractual amounts, use the applicable payoff logic and establish the correspondence if both models are needed.

The examples derive events from their stipulated agreements. When assessing an ACTUS or CDM implementation, compare its conventions and outputs with that derivation. Use [SIE.3 through SIE.4][SIE] for reuse and correspondence, and FDM.4 for actual effects. Revisit a mapping if changes in terms, state, event behavior or implementation edition affect its use.

### FDM.3:12 - Relations

FDM.1–2 supply adequate positions and party boundaries. FDM.4 establishes actual events and their effects; FDM.5 uses the flows relevant to a participant's service result.

Use SIE.3–6 to construct and connect models. Use [Management Accounting (MA.4)][MA4] to reconcile operating, reporting and cash accounts and [MA.5][MA5] for a forecast using the applicable conditional flows. Use [FIN.10][FIN10] to design or compare financing terms and [FIN.2][FIN2] to compare dated requirements with usable funds. For a valuation or choice, use the method and evidence appropriate to that financial task.

### FDM.3:End

## FDM.4 - Establish What a Financial Action Changed

**Type:** Architectural

**Status:** Stable


### FDM.4:0 - Use this when

Use this pattern when a financial action is reported as complete and you need to establish what, if anything, changed. Approval, sending an instruction, posting an entry and settlement can each support a different claim.

Establish the effect of the action or event on the relevant financial position. Give the supported change, the supported absence of that change or the particular effect still unresolved. Include the remaining position when the question needs it.

Use an established account of the effect when it supplies the evidence the present question needs.

### FDM.4:1 - Problem frame

A lending decision can authorize a next step without funding a borrower. An agreement can create a duty before funding. A payment instruction can be accepted for processing while the recipient still lacks usable funds. A payment can discharge only part of an obligation.

To establish an actual financial effect, identify the applicable rule and the event it recognizes. Check whether the evidence establishes the rule’s conditions.

### FDM.4:2 - Problem

A local completion label can be used to infer a wider result. That inference can leave a debt overstated, a payment falsely treated as available or a proposed agreement treated as effective.

Waiver, valid modification or another recognized act can change a position before any cash moves. Determine the mechanism from the applicable arrangement and the event that occurred.

### FDM.4:3 - Forces

Operational systems need timely completion signals. Their signals have scopes and can arrive before or after the effect relevant to another participant. Several dates may therefore be useful.

Records can disagree about time, party, meaning or whether an action succeeded. Examine the differences that matter to the requested effect. A routine account can be used directly when it already resolves them.

### FDM.4:4 - Solution

#### FDM.4:4.1 - Name the claimed change and prior position

Identify the claimed change, party, arrangement and relevant time. Establish the previous position as far as needed to explain the effect. Use FDM.1 for a missing position and FDM.2 for a party boundary that still matters.

Distinguish a change in permission, duty, usable resources, recorded information or business outcome. For a message marked “approved,” establish what decision the message reports and who issued that approval before relying on it for another claimed result.

#### FDM.4:4.2 - Recover the rule that gives the event its effect

Use the applicable terms or institutional rule to identify the recognized act or event, any required actor or authority, the conditions and the effective time. Some changes require communication. Others depend on performance or another occurrence.

Use [FPF A.2.8][DUTY] for duties, [FPF A.2.8.PER][PER] for permissions and [FPF A.2.9][ACT] for communicative work. For a disputed local term, use a qualified interpretation or obtain the specialist judgement the case still needs. A recording act can create an effect where the applicable rule gives it that force.

#### FDM.4:4.3 - Establish what actually occurred

Inspect the evidence relevant to that rule and effect. Match the parties, arrangement, amount and occurrence. Distinguish an instruction from its execution and a provider's local result from the recipient's result where those differences matter.

Use the dates that matter to the question. The occurrence, effective date, posting and actual availability can differ. Evidence that the provider received an instruction can answer that question while leaving the recipient’s access to funds unresolved.

If sources disagree, compare their subjects, dates and meanings. Investigate a remaining factual discrepancy when the requested conclusion needs it and the inquiry can resolve it at justifiable cost. Otherwise report the supported result and limit. Use a source for the claim it can establish.

#### FDM.4:4.4 - Derive the effect and remaining position

Apply the rule to the established occurrence and identify any change and its effective time. For a partial payment, use the applicable allocation rule to calculate which amounts were discharged and what remains. Include other interest, fees or conditions only where the arrangement makes them relevant.

A forecast can clear its modeled balance at maturity. To establish actual discharge, use evidence of the receipt or other event recognized by the terms. FDM.3:5.2 shows how a confirmed receipt updates principal and interest, and why an instruction of unknown effect leaves several states possible.

Relate the calculation to its financial meaning. When the arithmetic is possible but the position it would establish is unclear, use [FPF B.1.5.EW][EW] to locate the missing operation. A contractual interpretation may be supplied by a qualified colleague or another adequate source. An incorrect computation calls for a computational correction.

If evidence establishes that the recognized event did not occur, report that the claimed change did not arise through that event. A different waiver, payment or recognized act can still matter. If either the rule or occurrence remains unresolved, identify the missing premise and the effect that remains open.

Relate the records to the supported position. If an account must be corrected, use its responsible process and preserve the relevant history. For a comparison of participants’ accounts, use [ADM.4][ADM].

#### FDM.4:4.5 - Return the result needed by the next user

Return the supported effect, time, remaining position and material limits the user needs. If a missing rule, occurrence or necessary account correction blocks further use, identify the question and who can resolve it when that is known.

FDM.3 uses the resulting state for later events. FDM.5 uses the effect when examining a participant's service result. A demonstrated financial change can be useful even when its longer-term benefit is not yet known.

### FDM.4:5 - Archetypal Grounding

#### FDM.4:5.1 - A payment, an instruction and a modification

Suppose 105 is due on day 30 and the borrower pays 60 to the lender. Evidence establishes the payment. Under the supplied rule all 60 applies to this obligation and no additional fees or interest arise. The remaining amount is **45**.

A servicing report showing all 105 unpaid disagrees with the established position. Report the remaining 45 and the discrepancy. Retain the original contractual payment of 105 and the actual payment of 60 in their respective accounts.

Suppose the evidence instead shows only that the borrower sent an instruction for 60. That establishes submission. It leaves the payment event and reduction to 45 unresolved. To establish the residual position, determine whether the event recognized by the terms occurred.

In a separate case, suppose the competent parties validly modify a lender’s conditional advance obligation before funding. The supplied terms give that modification its effect. Report the changed undertaking from the effective event even though no money has yet moved.

The results depend on the stipulated formation, modification and payment-allocation terms. Use the terms governing the particular instrument to establish its effects.

#### FDM.4:5.2 - Deriving the position through an interpreted calculation

Suppose the lender receives 60 under terms classifying it as refundable cash collateral. The loan obligation of 105 remains outstanding. Subtracting 60 from 105 gives 45 arithmetically. Here the appropriate account retains **105** due on the loan and identifies the separate collateral position.

By interpreting the receipt under the contract, the modeler derives its financial effect and constructs the position account. The repayment terms permit subtraction from the debt. The collateral terms require a separate collateral position. The bank receipt is the financial event interpreted in that work.

If the modeller can calculate but lacks the required interpretation, use an adequate existing interpretation or obtain one from a qualified source. Develop the modeller’s own interpretive capability if the work also requires that ability. With the terms established, use the existing evidence of receipt. If collateral can later be applied to the debt, establish the relevant event and its effect before updating the obligation.

### FDM.4:6 - Bias-Annotation

A service team may judge success from its own processing, while a financial report emphasizes the latest posting. Check what each observation establishes under the rule giving the event its effect.

When the available sources cannot establish whether the event occurred, retain that uncertainty.

### FDM.4:7 - Conformance Checklist

Check these criteria for the particular effect claimed.

1. The affected party, prior position, claimed change and relevant time are clear.
2. The applicable rule and its action, authority or occurrence conditions are established where required.
3. Evidence supports the actual event at the scope claimed.
4. The derived effect and any residual obligation follow the applicable terms.
5. Records, effective relations and resource availability remain distinct where their differences matter.
6. The result distinguishes supported change, supported non-change and unresolved effect.

### FDM.4:8 - Common Anti-Patterns and How to Avoid Them

**Closing the obligation from a sent instruction.** Establish the event the applicable arrangement recognizes as performance.

**Treating all postings as either constitutive or merely descriptive.** Recover the actual rule and the role of the recording act in that arrangement.

**Using one date for every consequence.** Retain distinct occurrence, effect or availability dates when they change the receiving answer.

### FDM.4:9 - Consequences

A practitioner can explain what the financial action changed, what remains and which part the local completion signal establishes.

The account may establish that a required event did not occur, or that the available evidence leaves its occurrence unknown. An unresolved rule or a record requiring correction can also limit further work. Use a qualified source or the responsible participant when that work is needed.

### FDM.4:10 - Architectural Rationale

A financial effect depends on an operative rule and the occurrence satisfying its conditions. A term can establish what would happen. Evidence of an occurrence can establish which branch applies and when.

A transaction log is sufficient when it already supplies adequate evidence for a settled effect rule. A broad business-outcome inquiry is unnecessary for a narrow residual-balance question. The wider inquiry becomes useful when someone claims the financial change itself established the participant's benefit.

### FDM.4:11 - SoTA-Echoing

For an actual financial change, apply FPF’s distinctions among duties, permissions and communicative acts. Use ADM.3 and ADM.9–10 when the case turns on effectivity, usable provision or fulfillment. These distinctions help determine what a decision, message or record can establish.

In §§4.2–4.4, identify the rule, establish the recognized occurrence and derive the position. This distinguishes “60 instructed” from “60 paid” even when a local display says “complete.” Investigate further if a remaining premise matters to the requested finding or downstream use and the inquiry is worthwhile.

Actual local rules and event evidence govern an actual result. Reopen the account when either changes or when a later use requires a broader effect claim.

### FDM.4:12 - Relations

Use FDM.1–2 for missing positions or identities. Use FDM.3 to derive contractual event conditions and update its actual state with the effect established here. Use FDM.5 when that effect contributes to a claim about service use.

ADM.3, ADM.7–10 and the relevant financial practice supply effectivity, evidence, permission, usable provision and fulfillment questions at their own scope. A.2.8, A.2.8.PER and A.2.9 govern the underlying institutional distinctions.

### FDM.4:End

## FDM.5 - Trace a Financial Service to a Participant's Result

**Type:** Architectural

**Status:** Stable


### FDM.5:0 - Use this when

Use this pattern when the contribution of a score, report, advice, interface or transaction service to a participant’s financial result needs explanation. Start with the participant and the result at issue. The question may concern a service already delivered or a proposed use.

Identify the service output, the work in which it is or would be used and the financial effect or participant result being claimed. Give the basis for each part the question requires and any material uncertainty.

Use an adequate existing account of the contribution directly. A routine service can be described from its established result.

### FDM.5:1 - Problem frame

A scoring team can improve predictive accuracy while leaving lending decisions unchanged. An admission tool can produce accurate client information while a separate arrangement determines permission to use a service. A payment provider can complete its own processing while the recipient still lacks usable funds.

Identify whose work uses the result and what financial contribution is actual or proposed. A supplier can properly finish its work by delivering information. The output supplier, decision maker, service provider and beneficiary may coincide or be different participants.

### FDM.5:2 - Problem

A good output can remain unused, a decision can remain open, and a promised provision can fail. A consequence for one participant may also impose a loss on another. Examine the links needed for the claim being made.

Follow the connection far enough to explain the service’s contribution and its limits for the question at hand. Extending the boundary to every later business outcome can assign the provider responsibility for conditions outside its work or authority.

### FDM.5:3 - Forces

A service needs a recognizable useful result. Different participants can want different results, and a throughput measure may not express their shared interest. A legitimate refusal can be preferable to another admission.

A longer-term outcome may depend on conditions outside the service provider’s control. Establish the part the service contributed and identify conditions whose effect is still uncertain.

### FDM.5:4 - Solution

#### FDM.5:4.1 - Name the participant and intended result

Identify the participant and the result at issue. Examples include usable funds, a justified lending decision, timely payment or better understood exposure. Establish the time horizon. For an improvement claim, identify the comparison it requires.

Where several participants matter, preserve their different objectives and consequences. The lender and borrower can seek different results. If a disputed objective or choice criterion affects the answer, use the governing financial or management basis or obtain a decision from its holder where needed. Report distinct supported views if the question asks for those.

#### FDM.5:4.2 - Locate the output and its actual receiver

Identify the service output and its intended or actual use. Distinguish the scoring method, implemented calculator, calculation performed in the case and resulting score where the conclusion depends on the difference.

Trace how the output enters the receiving work. Use suitable records, observations or the receiver’s account. If the service applies its own result under an existing mandate, establish that action directly. For delivery, establish what reached the recipient. For a claim that the output influenced an action, establish the use and the link to that action.

A supplier asked to provide information can complete its assignment by delivering a usable result to the intended recipient. To credit it with a further financial outcome, establish the connection through the relevant use and effect.

#### FDM.5:4.3 - Follow the use through the financial effect

Identify the decision or action the output supports and the financial position or resource that could change through its use. To explain a factual contribution, establish which part occurred. Use FDM.1–4 where a missing position, term or effect is material.

For a proposed contribution, explain the mechanism and assumptions. For an actual contribution, establish the parts claimed, such as delivery, use or the resulting financial effect. A service already delivered can also have a prospective benefit whose conditions remain open.

Follow the connection as far as the participant’s question requires. Funding can make proceeds usable. The equipment bought with them may never arrive, or changed demand may defeat the hoped-for business return. Report the established funding contribution in its own scope and qualify any later outcome separately.

#### FDM.5:4.4 - Examine the contribution and its failure points

For a claim about what the service improved, compare the relevant alternative. Would the same decision follow without this output? Did another source already provide the information? Identify funding, authority, timing, delivery or use conditions that could prevent the proposed gain.

Examine the alternatives that affect the conclusion. To attribute an improved financial outcome to the service, use a suitable comparison and evidence of the causal connection, with uncertainty qualified to the claim. Accuracy of the output establishes a narrower result. Use the evaluation or inquiry method needed for a stronger claim.

Preserve a supported narrower result. A service can improve the information available for a decision even if the effect on the outcome is unmeasured. It can also supply usable funds while a later necessary condition remains outside the provider’s control. State which contribution is established and where the remaining question begins.

#### FDM.5:4.5 - Return a qualified contribution and next action

Explain the contribution in enough detail for its intended use. Identify the participant, output, receiving work and any financial effect, intended result or condition that the claim depends on. A connected paragraph may suffice.

Report the supported result. If a stronger conclusion still needs evidence or a decision, identify the missing contribution. An account may already answer the current question before a loan matures or a longer-term causal study finishes.

### FDM.5:5 - Archetypal Grounding

Suppose a scoring team gives a lender a score concerning a proposed borrower. The method gives the score’s meaning and validation conditions. The lender considers an advance of 100 under terms that would make 105 due on day 30.

Suppose the lending rule produces the same decision and terms at the old and new scores. Better score accuracy leaves that route to the borrower’s financial outcome unchanged. A different benefit, such as a reduction in the effort required to obtain information, can be assessed by its own comparison.

Suppose an authorized decision maker uses the score and reaches a different decision under its applicable rule. Use FDM.4 to establish the effects of any decision, agreement formation or funding that actually occurs. Under the supplied terms, successful funding makes proceeds usable by the borrower and establishes the funded positions.

The borrower wants to acquire equipment. Usable equipment delivered to the borrower can satisfy the next condition. If delivery fails, report that failure alongside the established financial effect of the loan. To establish a later return from the financed work, use business evidence of the result and the basis for attributing it.

In FDM.3:5.2 a treasury model shows whether 2,676 covers the amount due under each accrual rule. The shortfall under extended accrual is 1.41. The finding is useful before any action is chosen. If treasury uses it to arrange payment, use FDM.4 to establish what the actual action changed. A claim of avoided loss also needs a comparison supporting that difference.

For a client-admission service, follow the parts relevant to the claim. To establish information delivery, identify what reached the recipient. To report an access decision, determine whether the authorized arrangement granted or refused access. To establish provision, examine what service the client actually received. More admissions need not meet the client’s objective or the provider’s obligations. A justified refusal can be the appropriate result.

### FDM.5:6 - Bias-Annotation

Tool metrics may show a genuine improvement in the output. A sponsor interested in the eventual benefit also needs a basis for the receiving use and the link to that benefit. Identify the participant doing each part under the arrangement being examined.

### FDM.5:7 - Conformance Checklist

Check the following for the service contribution claimed.

1. The relevant participant, intended result and horizon are identifiable.
2. The service output and receiving use have adequate meanings and boundaries.
3. When a financial effect is claimed, the account connects it through the applicable decision, action and terms, with its actual or proposed status clear.
4. Output quality, actual use, financial effect and later participant outcome retain their different evidence and uncertainty.
5. Material alternatives and failure points have been examined where they can change the conclusion.
6. The result states the supported contribution and any specific next evidence or decision needed.

### FDM.5:8 - Common Anti-Patterns and How to Avoid Them

**Calling score accuracy a financial return.** Establish the receiving use, relevant comparison and financial consequence.

**Requiring the tool supplier to be the final decision maker.** Locate the actual receiver and the supplier's contribution to that receiver's work.

**Making every service responsible for the participant's whole future.** Retain the material connection and its conditions while distinguishing the service result from later outcomes.

### FDM.5:9 - Consequences

The result can explain an established service contribution, identify an unused output or locate a failed connection. When a change is called for, it also helps choose the scope of a further investigation or service improvement.

A narrower benefit may be established even when a sponsor’s wider claim is unresolved. Looking only at the final business outcome can also conceal an earlier useful contribution. A stronger causal claim needs a comparison and evidence appropriate to its greater scope.

### FDM.5:10 - Architectural Rationale

The participant’s intended result determines which part of the service to examine. Identify the supplied output and the receiving work. This makes it possible to establish a provider’s own contribution even when a different party supplies the final business result.

A technical specification can answer an interface question once the required meanings are settled. A question about financial value also needs a basis for the service’s financial contribution. If locating a missing use or effect answers the question, report that finding.

### FDM.5:11 - SoTA-Echoing

Trace the part of the service contribution at issue. Delivery of usable information can itself meet the request. For a claim about a decision or a further financial effect, establish the corresponding use and result. An authorized service can act on a score. A justified refusal can serve a participant better than admission, so a count of admissions alone cannot determine the benefit.

In §§4.1–4.4, identify what the service proposes to supply and under what conditions, or establish what the supplier delivered in the case examined. For a claim about later use or a financial consequence, trace the relevant steps. An accuracy report can miss that the decision maker never used a score. To attribute a benefit to its use, compare the applicable alternative. Consider a wider outcome study when a stronger finding or decision needs it and the attainable benefit justifies the work.

Use FDM.1–4, ADM and the relevant decision practice for the financial, administrative and choice questions that arise. Reconsider the affected contribution claim if its receiver, decision arrangement, terms or intended result changes.

### FDM.5:12 - Relations

Use FDM.1–4 for missing financial positions, boundaries, contractual events or actual effects. Use [ADM.7 through ADM.10][ADM] when the claim depends on evidence, permission, usable provision or fulfillment.

SIE supplies the general model connection. The relevant financial, operating or management practice supplies decision criteria and comparisons. When service design or provider choice is the unresolved task, use the relevant service-design or provider-selection method.

### FDM.5:End

# Financial Domain Modeling Principles Framework Sources and Edition Notes

Copyright © Anatoly Levenchuk. The original framework text and worked examples are licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). The [licensing notice (Licensing FPF and its DPF publications)](https://github.com/ailev/FPF/blob/main/LICENSING.md) states the scope and attribution terms. Referenced third-party works retain their own terms.



## FDM.Sources:1 - Edition record

**FDM 1.0** is the first edition of *Financial Domain Modeling Principles Framework*, containing FDM.1–FDM.5. Cite this edition with the pattern and section, for example **FDM 1.0, FDM.1:5**.

## FDM.Sources:2 - Source locators


- [FIBO, EDM Council][FIBO]: reusable financial concepts and their relations.
- [ACTUS technical-specification entry][ACTUS], [v1.1 specification][ACTUS-SPEC] and [terms dictionary][ACTUS-TERMS]: schedules, state, calculations and event transitions, with the edition boundaries discussed in FDM.3:11.
- [ACTUS analytics account][ACTUS-ANALYTICS] and [Quick Start][ACTUS-QUICKSTART]: the connection to analytical uses and an implementation entry.
- FINOS CDM 7.0.0, [Event Model][CDM-EVENT] and [Legal Agreements model][CDM-LEGAL]: agreement content and lifecycle-state distinctions.
- [AASB 10 §19 and B86–B88][AASB10]: a specific reporting basis for the policy-alignment and consolidation comparison in FDM.2:11.
- FPF A.2.8, A.2.8.PER and A.2.9: actual duty, permission and communicative-work distinctions.
- [Semantic Integration Engineering (SIE)][SIE], SIE.3–6: model construction, correspondence, identity and composition.
- [Organization Administration (ADM)][ADM], ADM.2–4 and ADM.7–10: applied participant, effectivity, account, evidence, permission, provision and fulfillment questions.

[SIE]: Engineering%20DPF%20Suite/SEMANTIC-INTEGRATION-ENGINEERING-PRINCIPLES-FRAMEWORK.md
[MA4]: Management%20DPF%20Suite/MANAGEMENT-ACCOUNTING-PRINCIPLES-FRAMEWORK.md#ma4---reconcile-operating-reporting-and-cash-accounts
[MA5]: Management%20DPF%20Suite/MANAGEMENT-ACCOUNTING-PRINCIPLES-FRAMEWORK.md#ma5---construct-and-update-an-operating-forecast
[EW]: ../FPF-Spec.md#b15ew---recover-how-constituent-actions-enact-encompassing-work
[ADM]: Management%20DPF%20Suite/ORGANIZATION-ADMINISTRATION-PRINCIPLES-FRAMEWORK.md
[DUTY]: ../FPF-Spec.md#a28---ucommitment--individual-duties-to-act-or-refrain
[PER]: ../FPF-Spec.md#a28per---granted-permission-exercise-and-non-prohibition
[ACT]: ../FPF-Spec.md#a29--uspeechact--communicative-work-and-its-intended-use
[MWA]: ../FPF-Spec.md#c32mwa---synthesize-an-architecture-account-of-methods-and-their-use
[FIBO]: https://spec.edmcouncil.org/fibo/index.html
[ACTUS]: https://www.actusfrf.org/techspecs
[ACTUS-SPEC]: https://raw.githubusercontent.com/actusfrf/actus-techspecs/master/actus-techspecs.tex
[ACTUS-TERMS]: https://raw.githubusercontent.com/actusfrf/actus-dictionary/master/actus-dictionary-terms.json
[ACTUS-ANALYTICS]: https://documentation.actusfrf.org/docs/Introduction/Model-for-analytics
[ACTUS-QUICKSTART]: https://documentation.actusfrf.org/docs/quickstart
[CDM-EVENT]: https://cdm.finos.org/docs/event-model/
[CDM-LEGAL]: https://cdm.finos.org/docs/legal-agreements/
[AASB10]: https://standards.aasb.gov.au/sites/default/files/2026-03/AASB10_07-15_ACOMPnov24_01-26.pdf
[FIN2]: Management%20DPF%20Suite/CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin2---assess-liquidity-and-funding-needs-by-date
[FIN10]: Management%20DPF%20Suite/CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin10---design-financing-instruments-and-terms

The [Architectural Reference](#financial-domain-modeling-principles-framework-architectural-reference) explains how to connect these sources when a financial question needs their different contributions.

## FDM.Sources:End
