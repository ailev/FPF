# Financial Domain Modeling Principles Framework

**Edition:** [FDM 1.0](#fdmreference1---edition-record)

**Author:** Anatoly Levenchuk, with AI-assisted development and review

Financial Domain Modeling helps a financial practitioner, business modeler or service designer establish whose financial position a model describes, what events can change it and how a service contributes to a participant's result. Its five methods connect parties, rights and obligations, contractual flows, actual effects and service use.

# Table of Contents

**Reader entry**

| § | Publication unit | Use |
| --- | --- | --- |
| R | [Financial Domain Modeling Readme](#financial-domain-modeling-readme) | Connect service use, financial positions, conditional events and actual effects. |
| P | [Preface](#preface) | Understand the connected methods, alternatives and limits. |

**Patterns**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| --- | --- | --- | --- | --- |
| 1 | [FDM.1 - Recover the Financial Position Behind a Record](#fdm1---recover-the-financial-position-behind-a-record) | Stable | Right, duty and record; score; loan position | A.2.8 and A.2.8.PER; FDM.2 for a disputed party. |
| 2 | [FDM.2 - Choose Party and Group Boundaries for Financial Modeling](#fdm2---choose-party-and-group-boundaries-for-financial-modeling) | Stable | Debtor; entity; fund; founder group; guarantee; usable cash | FDM.1 for positions; SIE.5–6 for identity and composition. |
| 3 | [FDM.3 - Derive Events and Conditional Flows from Financial Contract Terms](#fdm3---derive-events-and-conditional-flows-from-financial-contract-terms) | Stable | Principal; accrued interest; payment allocation; calendar; guarantee trigger; conditional and actual flow | FDM.1–2 for terms and parties; actual effects use FDM.4. |
| 4 | [FDM.4 - Establish What a Financial Action Changed](#fdm4---establish-what-a-financial-action-changed) | Stable | Approval; instruction; posting; payment; effect; residual obligation | FDM.1–3; applicable institutional rule and event evidence. |
| 5 | [FDM.5 - Trace a Financial Service to a Participant's Result](#fdm5---trace-a-financial-service-to-a-participants-result) | Stable | Score use; admission; financial benefit; service output | FDM.1–4 when financial meaning or effect is missing; relevant decision practice. |

# Financial Domain Modeling Readme

## Practical entries

The examples below show how the five methods connect a financial question to a usable answer. A service question may need a position or event model; a changed payment may require revising an earlier availability claim. Enter with the results already established and obtain only the missing contribution. Use the Table of Contents for a direct pattern question or a different application.

**FDM** is the reference code for this framework. In FDM.3:4.2, 3 identifies the pattern and 4.2 its section. You can ask an assisting agent to explain or apply the methods in the language of your work, without framework jargon. The cases use supplied terms and facts; actual arrangements require their applicable financial and institutional interpretation.

### FDM-E1 — A score is presented as a financial benefit

- **Situation:** A better score is reported as a benefit to a borrower, but the financial change is unclear.
- **Question:** What did the service change for this participant, and what remains unresolved?
- **First useful result or blocker:** A supported contribution to the participant's result, an unchanged financial outcome, or a missing term or event.
- **Start with:** FDM.5 for the service's use, then the position and event methods needed to establish the claimed change.
- **Stop or return:** Finish with the supported contribution. Return to the terms, event or outcome connection when its premise fails.

A scoring team has improved its output and wants to describe the benefit to a borrower. [FDM.5](#fdm5---trace-a-financial-service-to-a-participants-result) locates the decision that uses the score. If an established rule gives the same decision and terms for the old and new score, improved accuracy alone establishes no change in this borrower's financial outcome. That answer can finish the question. A different proposed benefit, such as less information-gathering effort, needs its own comparison.

Suppose instead that an adequately authorized decision arrangement uses the score to change a lending decision. [FDM.1](#fdm1---recover-the-financial-position-behind-a-record) identifies the resulting rights and obligations under the supplied terms; [FDM.2](#fdm2---choose-party-and-group-boundaries-for-financial-modeling) resolves a disputed lender or borrower identity if necessary. The score, agreement and usable funds answer different questions about the service. An actual agreement's formation conditions determine which duties exist before funding.

The constructed loan supplies valid formation and terms under which successful funding of 100 creates a funded position with 105 due on day 30. [FDM.3](#fdm3---derive-events-and-conditional-flows-from-financial-contract-terms) derives the contractual flows for each party. [FDM.4](#fdm4---establish-what-a-financial-action-changed) determines what actually occurred and changed. If a payment of 60 is established, all 60 applies to the due amount, and no further interest or fees arise, 45 remains due. A record still showing 105 unpaid must be reconciled with that effect; the original contractual amount remains 105. If the evidence establishes only an instruction to pay 60, the reduction remains unresolved. Correct subtraction cannot settle whether payment occurred.

FDM.5 uses these effect results to explain what the service supplied. Funding can make the agreed proceeds usable even if the equipment bought with them later fails to arrive. The contribution account then identifies the failed delivery step without erasing the funding result. Whether the financed work produces a later business benefit is a further question. A wider outcome claim can therefore be narrowed while the supported service contribution is retained.

The return depends on the failure: ambiguous terms return to FDM.1 or FDM.3, a disputed occurrence to FDM.4, and an unsupported connection to the participant's result to FDM.5. An adequate existing answer can be reused at any of these points.

### FDM-E2 — A group's cash is used to justify one entity's payment

- **Situation:** A group's cash balance is used to claim that one member can pay a debt.
- **Question:** Which funds can this entity actually use by the due date?
- **First useful result or blocker:** An availability and shortfall account for the entity, or an unresolved support condition or receipt.
- **Start with:** FDM.2 for the payment boundary, then FDM.1 and FDM.3 for support terms and FDM.4 for what occurred.
- **Stop or return:** Finish when the payment question is answered; revise affected availability or support assumptions when an event or term changes.

X owes 100 on day 7 and has 20 of unrestricted cash available then, after all other receipts and obligations. Y holds 150, and the two entities share a founder. [FDM.2](#fdm2---choose-party-and-group-boundaries-for-financial-modeling) distinguishes the founder-group view from X's payment question. Under these supplied facts, X has an 80 shortfall; adding the two balances does not make Y's funds available to X.

Now suppose a support arrangement requires Y to transfer 80 before day 7. FDM.1 establishes the relevant obligation and its parties; FDM.3 derives the conditions and timing that would make the support useful. If the arrangement instead guarantees payment only after X's failure and a valid demand, that is a different conditional route. It cannot be counted as an already available day-7 transfer. If the timing terms are insufficient, the model returns that unresolved condition.

FDM.4 then examines the event that would make the funds usable. A support commitment, transfer permission or sent payment instruction does not establish timely receipt. Suppose a later, adequately established transfer makes 60 usable by X before day 7 and nothing else in the supplied cash account changes. X now has 80 available and a remaining shortfall of 20. This actual result updates FDM.2's payment account and any FDM.3 scenario that assumed full support. The earlier 80 commitment and the 60 performance remain distinct.

The model can finish with that availability answer, or with the unresolved event when receipt is unknown. The responsible financial practice uses it to compare financing or payment actions. For a different portfolio-risk question, common dependence on the founder may still make the group view useful even when transfer is unavailable. Preserving that view alongside the payment account avoids replacing one question's answer with another's aggregate.

# Preface

## FDM.Preface:1 - The working problem

Financial work connects institutional relations with resources, records and possible future events. A borrower can have an obligation before a reporting system displays it. A displayed receivable can be disputed or already discharged. Money in a related company's account can be relevant to an exposure analysis while remaining unavailable for the borrower's next payment.

The language helps the practitioner recover these relations for a particular use. It does not attempt to replace every financial discipline. Its branch is financial domain modeling: establish the financial subjects, meanings, event conditions and effect claims that a decision, service or connected model needs. The resulting account can be a small table, a diagram or a software model; the carrier does not determine whether its claims are warranted.

Consider a loan with an advance of 100 and one contractual payment of 105 on day 30. A scoring method, its implemented calculator and one produced score are distinct. An applicable decision arrangement can use the score; an agreement can create rights and obligations under its actual formation conditions; funding can make proceeds available; later performance can satisfy only part of what is due. Following those differences explains what a score might contribute and where that contribution could fail.

## FDM.Preface:2 - How the methods connect

FDM.1 recovers a financial position and distinguishes it from its descriptions. FDM.2 chooses the parties and grouping needed by the question. Either can provide an already sufficient answer. A lender explaining which entity owes an amount does not have to model an entire service.

FDM.3 uses adequate parties and terms to derive contractual events. A schedule describes what those terms require under their conditions. Scenario assumptions can produce an expected or conditional flow account; actual occurrences produce a performance account. FDM.4 establishes the effect of an actual event or action and can return a remaining obligation, a discrepancy or an unresolved institutional question.

To obtain the event model, use FDM.1:4.2 for the operative terms and any interpretation that changes the answer. FDM.3:4.2–4.3 then connects each condition to its consequence, constructs the needed state and dates, and derives the amount and next state. Its partial-payment and guarantee cases show how to adapt that construction. A settled fixed payment can still use the short two-row account in FDM.3:5.1.

FDM.5 follows a service output through its use to the participant's intended financial result. It requests a position or effect model when that connection is unclear. Conversely, an accurately modeled financial change can raise the question of whose result it serves. These connections select the next needed result; they do not require all five methods for every use.

There is also a connection within the modeler's present work. While interpreting a payment under contractual terms, the modeler can be deriving a remaining obligation and thereby constructing an account of the borrower's position. Use [B.1.5.EW — Recover How Constituent Actions Enact Encompassing Work][EW] when it is unclear how the present operation performs the encompassing work or which capability is missing. FDM.4:5.2 shows why correct subtraction can leave that work undone. A banking transfer being modeled is a separate occurrence, even when the modeler observes it while working.

## FDM.Preface:3 - Connect models by the financial question

Suppose a lending model stores “loan amount = 100” for the principal, while a payment model requires the amount payable at maturity. Equal-looking field names do not establish an adequate correspondence.

FDM.1 and FDM.2 identify the same lender, borrower and contract. FDM.3 supplies the terms: principal 100, contractual maturity payment 105 in the stated currency on day 30. [SIE.4][SIE] can now establish a qualified correspondence: the principal field supplies the principal input; the maturity amount follows from the applicable terms. Replacing the maturity value by 100 would lose the contractual difference of 5.

[SIE.5][SIE] preserves the relevant party and contract identities. [SIE.6][SIE] combines the statements with their meanings, currency and time. [SIE.3][SIE] asks whether the available models are sufficient for the receiving question and directs a necessary extension. The financial distinction and the general integration method have separate contributions.

For this constructed example, assume that the advance of 100 has actually occurred and is adequately established, creating the obligation to pay 105 on day 30 under the supplied terms.

| Receiving question | Financial statement needed | Meaning that a connection must preserve |
| --- | --- | --- |
| How much was advanced? | Principal advance of 100 under the supplied terms. | The amount advanced. |
| What is contractually due at maturity? | Payment of 105 on day 30. | The contractual amount and event conditions. |
| What was actually paid? | An adequately established payment of 60. | The actual occurrence, with its relevant dates. |
| What remains due after that payment? | 45 under the supplied application rule, with no further fees or interest. | The effect of payment on the obligation. |

FDM.4 supplies the answers about the actual advance, payment and remaining obligation; it does not rewrite the original contractual schedule as if only 60 had been due. A reporting or risk model can retain both the schedule and the observed outcome with their distinct meanings. The connection is complete when it answers the intended question adequately, including any material unresolved premise.

[FIBO][FIBO] supplies a reusable account of financial concepts and their relationships. [ACTUS][ACTUS] supplies a different contribution: logic relating contract terms to scheduled contractual events. A system may need either or both. The example above explains their possible roles; implementing a particular correspondence requires inspecting the chosen definitions, terms, encoding and results.

## FDM.Preface:4 - Parties, resources and several useful structures

A founder-group account, legal-entity account and portfolio-risk account can all be useful. They answer different questions. A common founder can matter to correlated exposures, governance or expected support; the relation alone does not identify another entity as the debtor or make its funds available.

Keep each grouping's criterion and use explicit. Before summing balances, preserve the parties, dates, currencies, restrictions and any relation needed for the intended aggregate. A single organizational tree can be adequate for one report and inadequate for another question. [SIE.5–6][SIE] supply unresolved identity and composition work.

The same discipline applies within a loan. The lender's right, the borrower's duty, a bank-account record, usable proceeds and equipment acquired with those proceeds are different subjects. Their relationships explain the financial service.

## FDM.Preface:5 - Practical gain, cost and evidence

The first gain is a smaller, better defined question. A payment report may need only a corrected party reference or a distinction between due and paid. A service design may need to locate who actually uses a score. A disputed obligation may require the applicable institutional rule and evidence of the event it recognizes.

A detailed model costs time to build and maintain. Begin with an adequate existing account and deepen it where a plausible alternative changes interpretation or action. A qualified model, demonstrated non-change or precisely located unknown can be the first useful result.

Recognition and assurance have different jobs. A score presented as a benefit or an aggregate presented as available cash is a reason to examine the account. An actual financial-effect claim needs adequate support for the parties, applicable terms, occurrence and consequence it asserts. A quantitative benefit claim also needs evidence for its comparison and uncertainty. The numerical cases here are constructed under supplied terms.

## FDM.Preface:6 - Source choices and alternatives

The score-and-loan and group-funding cases join two questions: which financial relation a description concerns, and what using the description can change for a participant. A tool supplier can properly deliver information while another participant makes the decision. An authorized automated arrangement can act without a mandatory intermediate change in a human's expectation. A duty or permission is an actual institutional relation under its applicable conditions, distinguishable from descriptions of it. More client admissions are not by themselves a better outcome: suitability, legitimate refusal, participant objectives and the governing conditions can change that conclusion.

[A.2.8][DUTY], [A.2.8.PER][PER] and [A.2.9][ACT] supply the respective duty, permission and communicative-work distinctions. ADM supplies the applied administrative questions. These sources retain results that a vocabulary-only financial model could erase.

A data dictionary is a good first result when the missing answer is a term's meaning. An event model is needed when terms must determine behavior; a service explanation is needed when the use and contribution remain unclear. Combining them is justified by the receiving question. Reconsider a model when actual terms, institutional conditions, observed behavior or a changed use defeats a relied-on distinction.

## FDM.Preface:7 - Using the connected account correctly

For a connected use, establish that the parties, positions, terms and times agree where the models join; that a conditional event remains conditional; and that the evidence supports the particular use or effect being asserted. Use the relevant pattern's substantive questions for its result. An adequate supplied result can be reused while its conditions hold.

The examples expose three consequential mistakes: an amount field substituted for its financial meaning, a group aggregate substituted for available resources and a service output substituted for the participant's outcome. Recover the missing relation rather than adding another label. When only one such question is unresolved, the other adequate accounts remain usable.

## FDM.Preface:End

## FDM.1 - Recover the Financial Position Behind a Record

**Type:** Architectural

**Status:** Stable


### FDM.1:0 - Use this when

Use this pattern when someone relies on a balance, agreement, score or financial label without being able to say whose position it describes and under which terms. Begin with the party and the financial question the record is being used to answer.

The pattern governs an account of a financial position: the relevant right, obligation or other financial interest of an identified party under stated conditions and at a relevant time. It returns the warranted position and its relation to the records and resources involved.

Use an already adequate account directly. A cosmetic change to a report does not require recovering an undisputed position from the beginning.

### FDM.1:1 - Problem frame

Financial systems hold statements about parties and their positions. The word “claim” can refer either to an assertion in a report or to a creditor's right to receive something. Those meanings have different consequences. A report can assert that a lender has a right; the assertion and that right remain distinguishable.

Similarly, a loan agreement, a funded loan position, an account entry and the proceeds available to the borrower are connected without being the same subject. The receiving use determines which of these must be established.

### FDM.1:2 - Problem

A record's label and amount can make its financial interpretation appear settled. If the party, terms or time are wrong, a correctly copied number can still answer the wrong question. Treating the record as the position also prevents the practitioner from explaining a stale entry, disputed obligation or valid agreement that has not yet been funded.

### FDM.1:3 - Forces

A practitioner needs an answer quickly enough to support work. Reconstructing every institution and document is excessive when an adequate established account is available. Yet a material gap cannot be supplied merely by trusting a familiar field name.

The position can be clear while its future performance is uncertain. The model must retain that difference: a right to a future payment is not an assurance that the payment will occur.

### FDM.1:4 - Solution

#### FDM.1:4.1 - State the financial question and relevant party

Ask what someone intends to conclude from the record: who owes, who may receive, who bears a loss, what is available or another specific result. Identify the actual party whose position matters and the counterparty or other participant required to interpret it.

Resolve a material identity or grouping uncertainty through FDM.2 or [SIE.5][SIE]. A common trading name, group identifier or database key can help locate the party but cannot settle a disputed entity boundary.

#### FDM.1:4.2 - Recover the position from its applicable basis

Obtain the terms and institutional basis adequate for this question. Establish what right, duty or financial interest they provide, to whom, against whom where relevant, with what content, conditions and time.

For a position governed by an agreement, locate the operative agreement for the identified parties and time, together with the incorporated definitions, elections and amendments that can change the answer. Follow a reference when the referring clause leaves a needed operation elsewhere: a loan schedule may name an interest convention defined in another document, or a guarantee may use a notice procedure in a master agreement. A proposal and a concluded agreement can have the same commercial label while supporting different claims.

When a provision requires or permits an action, recover the party that must act or may choose, what it must do or can elect, the condition that activates that consequence, and the time at which the consequence applies. Read the provision together with its definitions and exceptions. Keep its location beside a derived rule when a later user must be able to inspect why that rule was selected. Keep the reconstruction to provisions that can affect the answer; a small adequate agreement may need only a few sentences.

When interpretation is unresolved, formulate the question at the point where it changes the model. Instead of “please confirm the contract,” ask, for example: “Does the weekend adjustment move only the payment date, or also the end of ordinary interest accrual for this installment?” Give the interpreter the parties, operative text, proposed alternatives, relevant date and intended use. Obtain the supported interpretation and its applicable conditions. Use it to complete the affected calculation, or retain the alternative results while the question remains open. Keep different readings distinct when a later date would distinguish their effects, even if they give the same amount today.

A term can already create a conditional obligation before money moves. Separate that relation from the amount advanced, current principal and payments already due. The resulting position supplies the starting basis for FDM.3.

A document can provide evidence and, under an applicable rule, its execution or another recognized act may help institute a relation. Recover that rule and event when they matter. Do not infer the existence or absence of an obligation solely from whether a database entry is present.

[A.2.8][DUTY] supplies the question whether an individual duty actually obtains. A permission uses [A.2.8.PER][PER].

#### FDM.1:4.3 - Relate descriptions and resources to the position

Identify what each source describes, the time it concerns and any limitation affecting reliance. A contract description, a servicing record and a customer's statement can refer to the same loan while differing in date, purpose or evidential support.

Distinguish the position from resources actually available. A borrower can owe repayment while proceeds have already been spent. A lender can have a funded right to payment while the borrower cannot currently pay. A displayed balance can be evidence about these facts, but its interpretation still needs the relevant account and availability conditions.

Retain a prospective position as prospective. A score or offer can inform a decision without establishing an agreement. Conversely, applicable terms can establish duties at valid formation before disbursement. Examine the actual conditions rather than imposing one universal sequence.

#### FDM.1:4.4 - Return what is warranted for this use

Return the party, financial relation, content, conditions and time at enough detail to answer the question. Relate the material records to that account and name any discrepancy or missing premise.

Use FDM.3 when the receiving question needs the event and flow consequences. Use FDM.4 when an actual action may have changed the position. If the position is already sufficient for a routine report or decision, supply it without expanding the model.

### FDM.1:5 - Archetypal Grounding

A lender considers advancing 100 to a borrower. In this constructed arrangement, valid formation, currency and the applicable terms are supplied: successful funding creates the stated funded position, with 105 contractually due on day 30. The model distinguishes the lender and borrower, their respective right and duty, and the proceeds made available on funding.

An earlier score of 0.72 is a produced assertion under its scoring method. Its scale and meaning must be known before it is interpreted even as a probability. The score alone establishes neither a lending decision nor the borrower's repayment obligation.

Suppose the signed arrangement also obliges the lender, before funding, to advance the amount once a specified condition is met. That supplied term gives the practitioner a separate pre-funding duty to examine. Waiting for disbursement before recognizing every obligation would lose it. If the actual formation or term is disputed, the model returns that exact uncertainty.

Now assume that the advance of 100 has occurred and the resulting obligation to pay 105 is established. After an adequately established payment of 60, the original agreement still describes the contractual payment of 105. FDM.4 can establish the remaining 45 under the example's application rule and absence of further fees or interest. A servicing record that still shows an unpaid 105 is now a discrepancy to investigate, not proof that the payment had no effect.

### FDM.1:6 - Bias-Annotation

System designers may prefer facts represented in their own application; a contract specialist may emphasize the agreement while overlooking settlement or usable resources. Compare the accounts around the receiving financial question.

The loan is a debt example. Other financial interests require their actual relation and governing terms; do not force an ownership interest or conditional instrument into a simple lender–borrower account merely because that example is familiar.

### FDM.1:7 - Conformance Checklist

For the proposed interpretation, examine whether:

1. The actual party and financial question are identifiable.
2. The right, obligation or other interest has an adequate basis, content, conditions and time.
3. Assertions and records about the position remain distinguishable from the position itself.
4. Actual resources and expected future performance are not inferred from a position alone.
5. The result supplies an adequate answer or names the particular identity, term, rule or evidence still missing.

An adequate description supports its stated interpretation. Its existence alone does not prove formation, funding or performance.

### FDM.1:8 - Common Anti-Patterns and How to Avoid Them

**Treating “claim” as one unambiguous object.** State whether the sentence concerns an assertion or a creditor's right. Then relate them where the report is evidence about the right.

**Making the database constitutive by default.** Establish what rule, if any, gives the relevant recording act that effect. A stale or missing entry otherwise remains a recording question.

**Deferring every duty until funds move.** Inspect the actual formation and conditional-performance terms. A valid unfunded arrangement can already have consequences.

### FDM.1:9 - Consequences

The recipient can use an amount with its financial meaning and can distinguish uncertainty about a position from uncertainty about payment. The model also makes a disagreement between records intelligible.

The cost is recovering material terms and relations that a label had concealed. Adequate existing accounts reduce that cost; unresolved institutional interpretation limits the conclusion the model can supply.

### FDM.1:10 - Architectural Rationale

The financial position is the central subject because it is what the record is commonly used to infer. Beginning with the receiving question limits the reconstruction to distinctions that matter.

A dictionary-only account is sufficient when the issue is a shared term and the actual position is already known. It is inadequate when an individual party's right or duty remains unsettled. Starting instead with the complete financial-service chain can impose unnecessary work on a narrow position question.

### FDM.1:11 - SoTA-Echoing

The practice question is how to give a financial record a warranted interpretation. The method uses FPF's distinction between an actual institutional relation and claims about it to interpret financial records. This changes §§4.2–4.3: establish the applicable relation and then connect the descriptions and resources.

FIBO is useful for financial concepts and relations that a local label obscures. It supplies reusable meaning rather than evidence that this particular party has this particular right. At the effort of clarifying one disputed label, a position account can expose a missing formation or time premise that a field renaming would retain.

FINOS CDM's [Legal Agreements model][CDM-LEGAL] offers an implementation comparison: it separates an agreement's identification, elections, amendments and related agreements. This helps locate terms that a single agreement field hides. It does not determine their legal effect; §4.2 obtains that interpretation for the actual question.

Reopen the interpretation when actual terms, party identity or event evidence changes the position being described.

### FDM.1:12 - Relations

FDM.2 resolves the party or group boundary; FDM.3 derives contractual behavior; FDM.4 establishes actual changes. FDM.5 uses an adequate position model when tracing a service's contribution.

A.2.8 governs the individual-duty question, A.2.8.PER the permission question and A.2.9 communicative work where its occurrence matters. [ADM.2–4][ADM] supply the corresponding administrative participant, effectivity and account questions. SIE supplies general identity and correspondence methods without replacing the financial terms.

### FDM.1:End

## FDM.2 - Choose Party and Group Boundaries for Financial Modeling

**Type:** Architectural

**Status:** Stable


### FDM.2:0 - Use this when

Use this pattern when a financial question crosses companies, accounts, funds or groups and the chosen boundary could change the answer. A founder's portfolio and a reporting group can include different entities; identify separately which party must make the payment.

The pattern governs the party and grouping account used for a financial question. It returns identified underlying parties and positions, a grouping criterion and the aggregation or support relations warranted for that use.

Use an adequate established boundary directly. A different display arrangement alone need not reopen an undisputed debtor or reporting subject.

### FDM.2:1 - Problem frame

One fund tracks investments by individual legal entity. Another groups startups associated with the same founders. Both views can support useful work, yet a shared founder does not automatically combine their obligations or accounts.

The question determines the relevant relation. Payment feasibility concerns the debtor's timely usable resources. A portfolio analysis can concern shared exposures without any support between entities. A reporting aggregate follows its applicable inclusion and elimination rules. The model must retain these differences while allowing the useful views to connect.

### FDM.2:2 - Problem

A convenient group key is often used as if it settled control, liability, support and resource availability together. Adding the members' balances then conceals the very restriction that changes the financial answer.

Forcing every question into separate-entity accounts has a different cost: it can miss correlated exposure or an actual support arrangement. The practitioner needs the boundary warranted by this question, with enough underlying structure to prevent an aggregate from acquiring another meaning.

### FDM.2:3 - Forces

An aggregate makes comparison manageable. Its simplicity is useful only while the omitted distinctions do not change the intended conclusion. The relevant membership and support conditions can also change over time.

Some relations establish a duty or power; others support a prediction of voluntary action. Both may matter, but treating an expectation as committed funding gives the prediction an unwarranted institutional effect.

### FDM.2:4 - Solution

#### FDM.2:4.1 - Start with the financial consequence being examined

State whose payment, position, exposure, control or report is at issue and the relevant time. Identify the actual entities and accounts involved before selecting a group label.

For a payment, find the party that bears the obligation and the funds it can use by the due time. For a portfolio question, identify the investments or exposures being compared and the risk meaning of their aggregation. For a reporting result, establish the reporting framework adopted for the entity and period. The report's purpose and applicable authority select the rule family; a shared owner does not. Use [SIE.5][SIE] when the entities themselves or their continuity are disputed.

#### FDM.2:4.2 - State why these members belong together

State the question the grouping serves and its inclusion criterion. The criterion may concern a common founder, control, contractual support or inclusion in the consolidated accounts under the applicable reporting rule. Establish membership at the time relevant to that question. Preserve the underlying positions when a group view is produced.

Different criteria can produce overlapping groups. Keep them connected when the receiving use needs them. A single hierarchy need not carry every financial relation.

#### FDM.2:4.3 - Recover what connects the positions

For a proposed support or resource-availability conclusion, inspect the actual connecting relation. A guarantee, committed facility, permitted transfer, control relationship and expected voluntary payment answer different questions.

Establish the relevant parties, content, limits, conditions and timing. A guarantee can give the creditor a further conditional claim without placing cash in the primary debtor's account now. Permission to transfer does not establish a transfer obligation. A support commitment does not establish timely performance. Control can matter while restrictions still prevent a particular use of funds.

When support is merely expected, preserve it as a scenario assumption with the reason for that expectation. A risk account may reasonably consider it; an account of cash already available needs the stronger fact it claims.

#### FDM.2:4.4 - Build the warranted aggregate

Combine only amounts whose meaning, time, currency and inclusion rule are adequate for the receiving use. Preserve restrictions and conditional relations that can change the result.

For a reporting result, retrieve the relevant provisions for consolidation, recognition, measurement or elimination, with their scope and exceptions, or obtain the responsible accountant's supported treatment. If the boundary depends on an unresolved control determination, provide the ownership and decision-right facts needed for it and ask which entities enter this reporting boundary for this period. A request for a consolidated number cannot supply that missing conclusion.

Use the returned boundary and treatment to identify included entities, align the relevant accounting bases and perform required adjustments. Explain an unresolved difference rather than combining incompatible values. [MA.4][MA4] supplies the account-construction and reconciliation work once the responsible treatment is adequate. A valuation, conversion or netting operation likewise needs the rule appropriate to its actual use; the group label does not supply one.

A useful specialist return supplies the decisive treatment, the parties and period to which it applies, the conditions that change it and the resulting model operation. If only the applicable jurisdiction or reporting basis is missing, ask for that selection. Apply an already adequate treatment directly.

For a payment question, derive the debtor's usable funds at the payment time after other relevant receipts and obligations. Include another entity's support through the arrangement and conditions established in §4.3. For a risk question, retain the exposures and dependencies needed to understand adverse scenarios. Do not silently use the risk aggregate as the payment-feasibility balance.

#### FDM.2:4.5 - Return the boundary and its financial meaning

Return the relevant parties, membership rule, positions and justified aggregate or support conclusion. State what remains unresolved where it affects use: an entity identity, support condition, restriction, payment time or aggregation rule.

Use [SIE.6][SIE] to combine the relevant claims into a qualified answer once their financial meanings are established. Its result can retain several claims or report conflict, non-comparability or an unresolved premise. FDM.3 develops conditional support flows; FDM.4 establishes the effects of an actual transfer. A sufficient ordinary boundary can be used without constructing every other group view.

### FDM.2:5 - Archetypal Grounding

#### FDM.2:5.1 - A founder group and one debtor

X must pay 100 on day 7. Its unrestricted cash available on that date, after all other receipts and obligations but before this payment, is 20. Y holds 150 in its own account. They share a founder. These are supplied facts of a constructed case.

The founder-group view can show both members and their balances. It does not settle X's ability to pay. X has an **80 shortfall** under the stated cash premise.

Suppose a duly established support arrangement requires Y to transfer 80 to X, with conditions that make it due before day 7. The model now contains a support obligation whose timely performance could close the gap. Until adequate evidence establishes the transfer or another means of timely availability, “support committed” remains different from “funds available”.

If the arrangement instead provides only a guarantee exercisable after X fails to pay, the creditor may have a further route under those supplied terms. X still lacks day-7 cash in the facts given. FDM.3 models the guarantee's actual trigger and timing; the model must not describe it as an earlier transfer.

If Y has no support commitment but the founder is expected to arrange a voluntary transfer, keep that event in the scenario that assumes it. For a portfolio-risk question, common dependence on that founder or on the same market can justify examining the members together even when no transfer is possible.

#### FDM.2:5.2 - A reporting group and an internal amount

Suppose the reporting practitioner has established the reporting basis and period and determined that P and S are consolidated for that report. Their aligned standalone accounts include P's receivable of 40 from S and S's corresponding payable of 40. The supplied consolidation treatment eliminates that internal pair in the group view.

Preserve the two entities' own claims for a separate question about S's payment. The reporting adjustment does not discharge S's obligation. If the reporting boundary has not been determined, ask for the missing determination; do not infer the same elimination merely because P and S share a founder.


### FDM.2:6 - Bias-Annotation

An investor may view a founder group as one economic story; a reporting system may prefer one legal identifier. Test both against the actual consequence being claimed.

Evidence of past voluntary support can inform an expectation. It does not by itself establish a present obligation or remove the possibility that support will arrive too late.

### FDM.2:7 - Conformance Checklist

For the boundary's stated use, examine whether:

1. The financial question, relevant time and underlying parties are clear.
2. Group membership follows an identified criterion adequate for that question.
3. Liability, control, support, permission and expected behavior remain distinct where their differences matter.
4. An aggregate retains the necessary time, currency, restrictions and applicable composition rule.
5. A claim of available funding has adequate support for timely usability, and unresolved premises remain visible.

A correct membership list establishes the group under its criterion. It does not establish every financial conclusion someone might draw from that group.

### FDM.2:8 - Common Anti-Patterns and How to Avoid Them

**Funding X by summing X and Y.** Recover the relation and event that make Y's resources usable for X's payment.

**Reading a guarantee as cash in advance.** Use the actual trigger, beneficiary and payment conditions. The guarantee may answer a recovery question while leaving the immediate funding question open.

**Rejecting a useful risk group because its members are separate debtors.** Keep the debtor accounts and model the shared exposure for the risk use that needs it.

### FDM.2:9 - Consequences

The user can compare group views without erasing the party that bears an obligation or the conditions of support. This exposes both false funding comfort and overlooked shared exposure.

The model can require more than one structure. Maintaining those structures is justified by their uses; unused groupings add cost without improving the financial answer.

### FDM.2:10 - Architectural Rationale

The method begins with the consequence because there is no single group boundary that settles every financial question. It retains underlying positions so that aggregation can be interpreted and revised.

A single reporting tree is adequate when its rule and the receiving use match. Separate-entity accounts suffice for an isolated debtor question. Several connected views become useful when support, exposure and reporting differ. Their connection uses SIE's existing identity and composition methods, with the financial relations supplied here.

### FDM.2:11 - SoTA-Echoing

The practice question is which party and group account makes a financial consequence intelligible. For financial groupings, the method adapts C.32.MWA's idea that several useful structures need not coincide. SIE.5–6 supply identity and composition methods.

This changes §§4.1–4.4: choose the boundary by the consequence, retain the members' positions and examine support separately. At the effort of naming the debtor and the support relation, it can expose a payment shortfall that a founder-group total hides. A larger organizational model is useful only when another material relation needs it.

[AASB 10 §19 and B86–B88][AASB10] illustrate that reporting choice: preparing consolidated statements involves consistent accounting policies and adjustments that eliminate intragroup balances. They give a practitioner using that basis rules for §4.4 once the reporting boundary is established. If the report uses another basis, retrieve its treatment instead.

The X–Y example demonstrates the difference between grouping entities and establishing support under its supplied conditions. Reopen the boundary when actual membership, support terms, restrictions, reporting basis or the receiving financial question changes.

### FDM.2:12 - Relations

FDM.1 supplies positions, FDM.3 their conditional flows and FDM.4 actual changes. FDM.5 uses the relevant participant boundary when examining a service result.

SIE.5 supplies unresolved identity work and SIE.6 composition. Use [C.32.MWA][MWA] when a financial-practice architecture question spans several structures, starting from representative performed work or a prospective use case. The relevant accounting, legal or financial practice supplies a disputed reporting, liability or aggregation rule.

### FDM.2:End

## FDM.3 - Derive Events and Conditional Flows from Financial Contract Terms

**Type:** Architectural

**Status:** Stable


### FDM.3:0 - Use this when

Use this pattern when a financial instrument's amount or due-date field cannot answer what happens under its terms. The question may concern payment timing, a conditional draw, repayment, a guarantee or another event that changes the required flows.

The pattern governs an event and flow model of the relevant arrangement. It returns contractual events under stated terms, any scenarios needed for the question and their relation to observed performance.

The construction assumes ordinary financial arithmetic and access to the agreement or a competent interpretation of it. It explains how to obtain and adapt the event model from that basis. An unresolved legal term returns to the precise interpretation request in FDM.1:4.2.

Use an adequate existing schedule directly when its conditions match the question. A new diagram is unnecessary if the contractual behavior is already clear.

### FDM.3:1 - Problem frame

“Loan amount 100” does not say whether 100 is the advance, current principal or payment due. A repayment amount may depend on elapsed time, a reference value, an option or prior events. Its date may depend on a calendar rule rather than a number typed into a report.

Contractual behavior and actual performance also differ. An amount due can remain unpaid. A forecast of receipts requires assumptions about performance even when the contractual schedule is certain.

### FDM.3:2 - Problem

A flat list of amounts and dates can conceal the conditions that produce them. Treating the resulting schedule as an unconditional cash forecast then imports an unsupported performance assumption.

A model of every possible contingency would be costly and often impossible. The working problem is to recover the contractual logic and the conditional outcomes that can change the present use.

### FDM.3:3 - Forces

Contract terms can be precise while required inputs remain uncertain. An amount linked to a future reference value may be contractually well defined without being numerically known today.

Simplification is useful when it preserves the receiving answer. It becomes misleading when it erases an exercise condition, timing rule or priority of events that changes the amount or obligation.

### FDM.3:4 - Solution

#### FDM.3:4.1 - Recover the arrangement and intended question

Identify the relevant parties, instrument or arrangement, version of the terms and time from which the model starts. Use FDM.1 or FDM.2 for missing positions or boundaries.

State the needed answer: the contractual schedule, an adverse funding scenario, the consequence of an option or another specific question. To determine what a borrower must pay next, obtain its obligation and conditional payment account. Determining what it has already discharged needs established performance; assessing whether it can fund the next payment also needs an account of usable money. Reuse existing terms and schedules to the extent that their scope and assumptions match.

#### FDM.3:4.2 - Construct the event rules from the operative terms

Use the operative terms and supported interpretations obtained through FDM.1. For each event that can change the answer, establish who acts or pays, to whom, what amount or quantity is determined, in which currency and at what time.

Read a consequential clause as a connection between a condition and a consequence. An installment clause determines an amount that becomes due on the specified date; the obligation to make that payment may already exist. An election clause creates an available action and specifies when a valid exercise changes the arrangement. A floating-rate clause specifies which observation sets the rate and when it applies. A payment-allocation clause determines how an actual or assumed receipt changes interest and principal.

For each such connection, explain how to decide that its condition holds, calculate its consequence and carry forward what has changed. For example, “payments first satisfy accrued interest” requires calculating the interest up to the payment's effective boundary before applying the remaining receipt to principal. The closing principal then supplies the next accrual interval. Simply extracting “payment = 1,000” omits that operation.

##### FDM.3:4.2.1 - Match or adapt an available model

Try an available model against these rules before constructing a new one. Select a contract family by behavior: scheduled principal repayment only at maturity, specified principal installments and equal total installments imply different future calculations. The marketing label “loan” does not decide among them. An optional prepayment is also different from a mandatory amortization installment.

Inspect the chosen model's definitions, assumptions and event behavior. Check that it can express the actual allocation, calendar and exercise rules. Use it directly when it fits, extend a separable missing behavior when the other meanings remain valid, or retain the unsupported part explicitly. A software default can be used as an explicit assumption; it does not determine the agreement's meaning. [SIE.3][SIE] supplies this reuse decision; SIE.4 supplies a qualified correspondence when two representations use different meanings.

For an [ACTUS][ACTUS] implementation, the useful return is to the chosen contract type's schedule, state initialization, payoff calculations and state transitions, together with the selected dictionary and implementation edition. Supply the operative terms, a supported starting state and any external observations or scenarios that the model needs. Compare its produced events with the agreement-based construction. A successful sample request establishes execution of that sample; it does not establish the mapping for another contract.

##### FDM.3:4.2.2 - Construct enough state and preserve the different dates

Work backward from the next calculation to determine what must be carried forward. Simple interest on unpaid principal needs that principal, the rate and the beginning of the unaccrued interval. Interest already accrued but not paid needs its own amount. An exercised option may change which later events are possible. A more complex instrument can require other state; an unused field need not be invented.

Initialize those values for the requested starting time from supported history or a qualified existing account. Starting halfway through a loan with its original principal can produce a wrong forecast after a repayment. Estimating prior interest from today's principal or rate can also be wrong after a change. Recover the intervening event or the adequate opening value. If it is unavailable, identify which later quantities remain conditional.

Generate recurring dates from the specified anchor, interval and end condition. Preserve a short final period or end-of-month rule where the agreement requires it. Then determine which dates the business-day convention changes. The date used to calculate interest, the date on which payment is due and the date on which a transfer actually settles can differ. Notice and observation dates can add further relevant boundaries.

At a rate or principal change, split the accrual interval at the effective boundary and apply each value only to its interval. When events coincide, obtain the order from the terms or their qualified interpretation. Calculate on the state that the event's rule actually consumes. A convenient spreadsheet row order supplies no financial reason for that choice.

#### FDM.3:4.3 - Derive and inspect contractual behavior

Work through the relevant events in their applicable order. Keep the operative terms, supplied input values and derived amounts distinguishable enough to inspect.

For a simple-interest interval with constant principal **P** and annual rate **r**, the constructed case below uses **P × r × d / 365**, where **d** is its specified actual-day count. Other conventions require their own supplied calculation. Keep the rule that selects the dates beside the arithmetic.

At an event, first bring any needed accrual to its applicable boundary. Determine the amount payable or the noncash consequence. Then apply the event's rule to obtain the next state. For a receipt **C** allocated to interest first, calculate the payable interest **I**, apply the smaller of **C** and **I** to interest, and apply any permitted remainder to principal. Carry unpaid interest forward when **C < I**. Rounding, excess receipts and other allocations follow the arrangement's rules. Capitalization instead adds the eligible interest to principal with no cash payment.

At a due date, the terms determine the amount now payable. A payment event under an assumed performance path can settle it in a forecast. For an account of actual performance, FDM.4 supplies whether the required effect occurred. Keep principal and unpaid interest until their discharge or other change is established. If a forecasting engine clears balances at a scheduled maturity event, that transition cannot by itself establish that the real borrower paid.

The resulting account should let the next user recover the starting position, operative rule, event condition, calculation dates, conditional amount and subsequent state. A short table may be enough. Use an executable model when repetition or interacting conditions make that necessary, while keeping an inspectable example of how its events answer the financial question.

Check the flows and state changes against the terms under representative conditions. Inspect a boundary where a date, event order, exercise or allocation can change the result. A calculation can be mechanically correct while using the wrong meaning for “amount”, the wrong party or an inappropriate initial state. A simple fixed-payment loan can still be modeled in two rows; add branches or execution only where the needed behavior justifies them.

#### FDM.3:4.4 - Add scenarios and performance without replacing the contract

For a scenario, state the additional assumptions: market values, exercise, default, recovery or another condition relevant to the use. Derive the resulting conditional flows. If a probability or expectation is needed, obtain an adequate basis for it and retain its conditions.

Keep the contractual schedule available alongside expected or scenario flows. An expectation is an account across possible outcomes under a model; it is not another amount that every counterparty must pay. Likewise, an observed payment belongs to the actual-performance account. FDM.4 establishes its effect on remaining positions.

A financial choice or valuation may need discounting, risk treatment or comparison with alternatives. [FIN.10][FIN10] consumes the contractual behavior when comparing financing terms; [FIN.2][FIN2] uses the amounts and dates with usable funds. Supply the qualified flows to the method answering the financial question. The event model alone does not select its decision rules.

#### FDM.3:4.5 - Return and adapt the model for its receiving use

Return the contractual or conditional flows, relevant parties, time rules and assumptions at the detail the receiving use needs. Name a missing term or uncertain input where it changes the answer. A missing future market value can leave a usable formula; a missing interpretation can leave different formulas or dates. Return a range, conditional branches or an unresolved amount when the available basis does not determine one value.

Separate a new observation, an exercised existing right, a change to the agreement and correction of an earlier record. A new market fixing supplies a value to an existing rule; an effective amendment can change the rule. A late bank confirmation can establish an earlier receipt. Each calls for a different update.

For a valid prospective amendment, preserve the history already established and apply the changed rule from its effective boundary. Recompute dependent later events. If the amendment's effectivity or treatment of earlier accrual is unclear, obtain that interpretation before rewriting the prior account. [ADM.3 and ADM.10][ADM] supply the temporal and performance inquiries.

Reopen only the dependent parts when the relevant state, a relied-on scenario premise or the receiving use changes. FDM.4 supplies established effects for updating actual state; FDM.5 examines how using the model contributes to the participant's result. Preserve the source of an opening value or changed rule when later users need it to understand that update.

### FDM.3:5 - Archetypal Grounding

#### FDM.3:5.1 - A fixed payment, expected receipt and actual payment

In the constructed loan, a lender advances 100 and the borrower owes one payment of 105 on day 30. Valid formation, currency and the fixed payment terms are supplied. The model can begin with:

| Event | Lender's cash flow under the stated schedule | Borrower's cash flow under the same schedule |
| --- | ---: | ---: |
| Successful advance | −100 | +100 |
| Contractual payment on day 30 | +105 | −105 |

The signs describe each party's perspective. The second row is contractual; actual receipt still requires performance.

For illustration, suppose a separate performance model assumes an 80% probability of payment of 105 and a 20% probability of payment of only 60, both on day 30. Its expected receipt is **0.8 × 105 + 0.2 × 60 = 96**. These probabilities are supplied assumptions, not an interpretation of an unexplained score. The expected amount is neither the contractual amount nor a discounted value.

If the actual payment is 60, retain that observation separately. Under the example's supplied application rule and absence of additional fees or interest, FDM.4 can establish 45 remaining due. The contractual schedule does not become “60 due” merely because only 60 was paid.

Now consider a conditional support arrangement for X. The terms require a payment of 80 only after a specified failure and valid demand. Its event model must preserve those conditions and the actual payment timing rule. It cannot supply 80 of unconditional day-7 funding merely because that amount appears in the document. If the rule does not establish when funds can arrive, the timing result remains unresolved.

#### FDM.3:5.2 - Constructing a partial payment and a shifted due date

The question is what B must arrange to pay at the next due date after a 1,000-unit early receipt by lender L. Both parties use USD. The case supplies an effective agreement, valid party identities and the following complete terms for the events considered; their legal effect is a premise of the example.

| Supplied term | Modeling consequence to derive |
| --- | --- |
| L advances 3,650 to B on 2 April 2026. | The advance creates principal of 3,650 when it occurs; it is a cash inflow for B and outflow for L. |
| Ordinary interest is simple, 10% annually on unpaid principal, actual days divided by 365. An interval includes its first date and excludes its last. Interest itself bears no interest. | Split an interval when principal changes. Carry accrued interest separately until paid; no capitalization. |
| Remaining principal and ordinary interest are payable on 2 May. A nonbusiness payment date moves to the following business day without extending ordinary interest accrual. For this example only, every Monday–Friday is a business day and there are no holidays. | The accrual endpoint is 2 May; the payment due date is 4 May. This is a stipulated calendar, not a jurisdiction's calendar. |
| B may make an early payment on a business day after valid notice received at least one business day earlier. An effective receipt first pays all interest accrued to that date, rounded to cents, then principal. There is no early-payment fee. | A notice enables the action but changes no amount by itself. Accrue first, allocate the receipt, then use the reduced principal. |
| Payment takes effect only upon irrevocable credit to L's designated account. All effective dates here are treated as the beginning of that date. | A submitted instruction alone cannot establish the receipt or the principal reduction. |
| No other payment, fee, rate change or capitalization affects this calculation. Round interest to the nearest cent, halves upward, when it is paid; final interest is rounded once at maturity payment. | The example's arithmetic needs no guessed charges or daily rounding. Questions about later default charges require their separate terms. |

The history establishes the 2 April advance, valid notice on 16 April and irrevocable credit of 1,000 on 17 April. For these confirmed transfers, both parties' corresponding cash movements occurred on the stated dates. The account is prepared just after the 17 April receipt. The future path assumes full payment on 4 May, with B's debit and L's irrevocable credit both on that date.

The decisive interpretation occurs before subtraction. The 1,000 is a total receipt, not a principal-only reduction. Fifteen days of interest on 3,650 at 10%/365 equal 15.00. The receipt therefore pays 15.00 of interest and 985.00 of principal. Principal becomes 2,665.00; accrued unpaid interest becomes zero.

| Event or boundary | Cash for B | Derived state or required payment |
| --- | --- | --- |
| Confirmed advance, 2 April | +3,650.00 | Principal 3,650.00; interest starts accruing. |
| Accrual to 17 April, before receipt allocation | 0 | Interest 3,650 × 0.10 × 15 / 365 = 15.00. |
| Confirmed receipt, 17 April | −1,000.00 | Pay interest 15.00 and principal 985.00; principal 2,665.00, unpaid interest zero. |
| Ordinary accrual endpoint, 2 May | 0 | Another 15 days produce unrounded interest 10.95205479… . |
| Payment due, 4 May | −2,675.95 if fully performed | Principal 2,665.00 plus rounded interest 10.95. Actual discharge still depends on the receipt condition. |

The due amount is a view of the principal and interest being demanded, not a third balance to add to them. Signs reverse for L's account of the same transfers. Neither those signs nor the matching bank amounts establish the institutional allocation without the terms.

Accrue the first interval on the principal that was outstanding during it. The next interval uses 2,665, and the payment moves to Monday while ordinary accrual still stops on Saturday. A model that subtracts the entire 1,000 from principal has omitted allocation; a model that uses 2,665 for the first interval has rewritten the past.

Now change one term: ordinary interest runs to the adjusted payment date. The first receipt and its allocation remain established. Only the later accrual interval changes from 15 to 17 days. Its interest becomes 12.41232877… and the due amount becomes 2,677.41. B's provision of 2,676 would cover the original obligation and fall short by 1.41 under the changed term. Reuse the first interval instead of rebuilding it. If the operative text does not settle which accrual rule applies, return these conditional results and the precise interpretation question.

Change the evidence instead of the term: the 17 April record proves only an instruction and its effect is unknown. Keep the confirmed advance. Ask the payment provider whether and when the same attempt produced the required credit. The 2,665 principal is then conditional on credit on 17 April; it is not an established actual balance. A proved failure with no other receipt leaves principal 3,650 and ordinary interest 30.00 through 2 May, giving 3,680.00 due on 4 May. A credit on a different date requires splitting at that date and recalculating. Missing evidence does not establish any one of these paths.

If the confirmed 1,000 instead belongs to a refundable collateral arrangement, recover that arrangement's effect under FDM.4. A transfer with the same amount and date can create a collateral position while leaving the loan principal unchanged. FDM.4:5.2 develops this distinction between refundable collateral and repayment.

For the model's use, [FIN.2][FIN2] consumes the qualified amount and due date together with B's usable funds; [FIN.10][FIN10] can compare a different financing arrangement. FDM.5 asks whether the treasury service used the model to arrange a sufficient payment and what effect followed. The next action and any claimed benefit depend on that receiving use.

#### FDM.3:5.3 - Constructing the payment conditions of a guarantee

For the loan in §5.2, suppose G separately guarantees L up to 2,000 of B's unpaid principal. The supplied terms activate payment only after the principal due date has passed, two following business days have elapsed without cure, and G has received a valid demand. Payment is due two following business days after that demand. The same stipulated weekday-only calendar applies. The question is whether this guarantee can supply B with money for the 4 May payment.

Construct the condition as a conjunction. A principal shortfall alone supplies only one part. Keep the outstanding covered principal from the loan, the end of the cure interval and the demand's validity and receipt as distinct inputs. When all activation conditions hold, the amount is the lesser of covered unpaid principal and 2,000; the recipient is L. A scenario assumption about default cannot substitute for an actual valid demand.

On the branch where B makes no maturity payment and no intervening event reduces principal, the two following business days are 5 and 6 May. A valid demand received on 7 May makes payment due on 11 May, after 8 May and 11 May as the two following business days. Covered principal is 2,665, so the guarantee payment is 2,000 on that branch.

This construction supplies no funds to B before 4 May. It can protect L against part of the later loss, and its existence could affect a separately offered financing decision. Those are different uses. To account for a later guarantee payment, FDM.4 also needs its effect on L's claim and any resulting claim by G against B. The guarantee amount alone cannot establish that B's total obligations fell by 2,000.

The transferable move is to derive the trigger, qualifying action, beneficiary and resulting date together. Loan-style arithmetic with a guarantee limit inserted as a payment would miss the work that produces the event. If demand validity is unresolved, return the affected conditional event and obtain the responsible interpretation; unrelated known loan amounts remain usable.

### FDM.3:6 - Bias-Annotation

A precise formula can attract more confidence than its inputs deserve. Keep the source and uncertainty of performance assumptions visible, especially when a score has been converted into a probability.

A familiar simple loan can also bias the interpretation of another instrument. Use its actual terms; a repeated software field name does not establish the same event behavior.

### FDM.3:7 - Conformance Checklist

For the intended flow use, examine whether:

1. The arrangement, parties, relevant terms and initial state are identified.
2. Event conditions, amounts, currencies, timing and state updates follow the applicable terms or explicit assumptions.
3. The representation retains the branches and ordering that can change the answer.
4. Contractual, scenario, expected and actual flows remain distinguishable.
5. Missing terms and uncertain inputs are exposed where they affect the result.
6. A valuation or decision claim uses the further method and evidence it requires.

A generated schedule demonstrates the calculation under its inputs. It does not establish valid formation, future performance or financial suitability.

### FDM.3:8 - Common Anti-Patterns and How to Avoid Them

**Using principal as the maturity payment.** Recover the amount's contractual meaning and derive the payment from the terms.

**Treating a schedule as a receipt forecast.** State the performance assumptions and retain the contractual obligation separately.

**Applying an undocumented default.** Establish whether the chosen convention belongs to the actual arrangement. If it is only a scenario assumption, say so where it changes the flow.

### FDM.3:9 - Consequences

The user can explain where an amount or date comes from and can compare contractual requirements with conditional and actual outcomes. The result can feed funding, risk, reporting or service work.

The model may reveal that a previously definite number depends on an unresolved term or uncertain input. That limits reliance while giving the recipient a precise next question. Greater instrument complexity increases construction and maintenance effort.

### FDM.3:10 - Architectural Rationale

Events and their conditions are central because an instrument's financial behavior depends on how the arrangement responds over time. A flat amount-and-date record can be sufficient for a simple fixed obligation; it needs extension when conditions alter that obligation.

Separating contractual behavior from performance keeps both interpretable. A single blended “forecast cash flow” can be useful to its intended decision, but its construction must retain the contractual and scenario meanings needed to explain or revise it.

### FDM.3:11 - SoTA-Echoing

The practice question is how to obtain an event model from terms and use it through changing conditions. ACTUS offers an algorithmic supplier: schedules, initialized state, event payoffs and transitions. Its [technical specification v1.1][ACTUS-SPEC], released in 2020, is a historical reference for those rules. For example, its PAM prepayment rule brings accrual to the event before reducing principal. The [terms dictionary][ACTUS-TERMS], version 1.4 dated 2023-12-08, distinguishes changing a calculation date from shifting the payment date. Those distinctions inform §§4.2–4.3; the agreement determines which behavior is applicable.

The current [ACTUS analytics account][ACTUS-ANALYTICS] connects contract inputs and external risk factors to analytical uses. Its [Quick Start][ACTUS-QUICKSTART] supplies an implementation entry. A spreadsheet is adequate for an inspectable small construction; an event engine becomes useful when repeated or interacting calculations justify the mapping and maintenance effort. Use the selected implementation's specification and dictionary when constructing that mapping. Neither a familiar contract-type name nor successful execution of a sample establishes agreement-specific behavior.

FINOS CDM's [Event Model, version 7.0.0][CDM-EVENT] provides a complementary model of trade state and changes. Terms amendments, observed resets and transfers with different statuses supply different updates. It informs the distinction in §4.5 between changing a rule, obtaining an input and establishing performance. Such a state-and-event representation is useful for lifecycle integration, while contractual payoff logic is useful for deriving amounts. A project can need both; their outputs require a qualified correspondence.

The worked cases use their stated agreement terms. To assess an ACTUS or CDM implementation, compare its result and conventions with that agreement-based model. [SIE.3–4][SIE] supply the general reuse and correspondence methods, and FDM.4 supplies actual-effect reasoning. Reopen a relied-on mapping when its terms, state, event behavior or implementation edition changes.

### FDM.3:12 - Relations

FDM.1–2 supply adequate positions and party boundaries. FDM.4 establishes actual events and their effects; FDM.5 uses the flows relevant to a participant's service result.

SIE.3–6 supply general model construction and connection. [Management Accounting, MA.4][MA4] reconciles operating, reporting and cash accounts; [MA.5][MA5] uses the relevant conditional flows in its forecast. [FIN.10][FIN10] uses contractual event behavior to design and compare financing instruments and terms; [FIN.2][FIN2] compares dated requirements with usable funds. The responsible financial practice supplies any additional valuation or choice method.

### FDM.3:End

## FDM.4 - Establish What a Financial Action Changed

**Type:** Architectural

**Status:** Stable


### FDM.4:0 - Use this when

Use this pattern when someone says a financial action is complete but the resulting position is uncertain. Approval, a sent instruction, a system posting and settlement can support different claims.

The pattern governs an account of an actual action or event's financial effect. It returns a supported change, supported non-change or a specific unresolved effect, including the remaining position where that matters.

Use an adequate established effect account directly. Reconstructing an uncontested payment from every source adds no value when the receiving use already has sufficient evidence.

### FDM.4:1 - Problem frame

A lending decision can authorize a next step without funding a borrower. An agreement can create a duty before funding. A payment instruction can be accepted for processing while the recipient still lacks usable funds. A payment can discharge only part of an obligation.

The financial question concerns the effect that actually obtains under the applicable arrangement. Its answer needs both the relevant institutional or contractual rule and adequate evidence of the event that satisfies its conditions.

### FDM.4:2 - Problem

A local completion label can be used to infer a wider result. That inference can leave a debt overstated, a payment falsely treated as available or a proposed agreement treated as effective.

The opposite error is to require physical cash movement for every financial change. Waiver, valid modification or another recognized act can change a position under its applicable rule. The method must recover the actual effect mechanism rather than select it from the action's label.

### FDM.4:3 - Forces

Operational systems need timely completion signals. Their signals have scopes and can arrive before or after the effect relevant to another participant. Several dates may therefore be useful.

Evidence can disagree because of timing, identity or meaning as well as an actual failed action. Resolving the discrepancy requires enough context to distinguish those explanations, without turning every routine completion into a full investigation.

### FDM.4:4 - Solution

#### FDM.4:4.1 - Name the claimed change and prior position

State what is supposed to have changed, for which party, under which arrangement and at what relevant time. Recover the prior position to the extent needed to explain the effect. FDM.1 supplies a missing position account; FDM.2 resolves an uncertain party boundary.

Distinguish a changed permission, duty, usable resource, recorded statement and business outcome. If a message says only “approved”, establish what its sender actually approved before treating it as evidence of another result.

#### FDM.4:4.2 - Recover the rule that gives the event its effect

Obtain the applicable terms or institutional rule. Identify the event or action the rule recognizes, the actor and authority where required, the conditions and the effective time. Some effects require a communicative act; others depend on performance or another recognized occurrence.

[A.2.8][DUTY], [A.2.8.PER][PER] and [A.2.9][ACT] supply the respective duty, permission and communicative-work questions. Use the relevant specialist for disputed local terms. A record can be constitutive if the applicable rule gives the recording act that role.

#### FDM.4:4.3 - Establish what actually occurred

Inspect the evidence relevant to that rule and effect. Match the parties, arrangement, amount and occurrence. Distinguish an instruction from its execution and a provider's local result from the recipient's result where those differences matter.

Retain the dates needed to interpret the action: occurrence, effective date, posting or actual availability can differ. Obtain only the dates that can change the present answer. Evidence sufficient for “instruction received” may be insufficient for “recipient can use the funds”.

If sources disagree, first compare their subjects, dates and meanings. Then investigate the remaining factual discrepancy. Do not select a source as decisive merely because its application is the most familiar one.

#### FDM.4:4.4 - Derive the effect and remaining position

Apply the recovered rule to the established occurrence. State what changed and when. For a partial payment, use the applicable allocation rule to determine which amounts are satisfied and what remains. Preserve other interest, fees or conditions only where the actual arrangement requires them.

A scheduled transition that clears a forecast balance does not establish actual discharge. Use the receipt or other event recognized by the terms. FDM.3:5.2 shows how an established receipt updates principal and interest for the next calculation, while an instruction with unknown effect leaves alternative states.

Keep the calculation answerable to that interpretation. If you can perform the arithmetic but cannot explain how it establishes the financial position, use [B.1.5.EW][EW] to locate the missing operation in the encompassing work. An unresolved contractual interpretation may need a qualified colleague's contribution; a computational correction addresses a different failure.

When the evidence establishes that the required event did not occur, return the supported non-change for that effect. When the rule or occurrence is unresolved, return the exact missing premise. An unresolved result is not proof of either performance or failure.

Relate the records to the resulting position. A necessary correction belongs in the appropriate account through its responsible process; do not silently rewrite history to make sources appear consistent. Use [ADM.4][ADM] when the participants' accounts require a broader comparison.

#### FDM.4:4.5 - Return the result needed by the next user

Supply the supported effect, time, remaining position and limits. Name the next responsible question when a rule, occurrence or correction still needs resolution.

FDM.3 uses the resulting state for later events. FDM.5 uses the effect when examining a participant's service result. A demonstrated financial change can be useful even when its longer-term benefit is not yet known.

### FDM.4:5 - Archetypal Grounding

#### FDM.4:5.1 - A payment, an instruction and a modification

In the constructed loan, 105 is due on day 30. Adequate evidence establishes a payment of 60 by the borrower to the lender. The supplied application rule applies all 60 to that due amount; there are no additional fees or interest. The resulting unpaid amount is **45**.

A servicing report still showing 105 unpaid disagrees with that established effect. The model returns the 45 position and the report discrepancy. It retains the original 105 contractual schedule and the actual 60 payment as distinct statements, rather than editing either into the other.

Now suppose the available evidence instead establishes only that the borrower sent a payment instruction for 60. The evidence does not yet establish the event that the supplied terms recognize as payment. The claimed reduction to 45 remains unresolved. The next question is whether that event occurred, not whether subtraction was performed correctly.

A separate pre-funding example has different effect conditions. A valid modification, made by the competent parties under supplied terms, changes a lender's conditional advance obligation before any money moves. The model follows that rule and its actual occurrence. It does not wait for disbursement to recognize every change.

These examples demonstrate reasoning under their supplied premises. Another instrument's payment-allocation, formation or modification rule can produce a different result.

#### FDM.4:5.2 - Deriving the position through an interpreted calculation

Consider a variant in which receipt of 60 is established, but the supplied terms classify it as refundable cash collateral. The terms leave the borrower's loan obligation of 105 unchanged. Subtracting 60 from 105 still produces 45 arithmetically, but does not describe the remaining loan obligation under these terms. The account instead retains the obligation of **105** and the separate collateral position.

While applying the contractual classification, the modeler is deriving the financial effect and constructing the position account. What the larger account must explain determines what the local calculation may claim. The earlier repayment example permits the subtraction; this collateral example does not. The banking receipt supplies an occurrence to interpret, rather than becoming part of the modeler's act of interpretation.

Someone who can calculate but cannot interpret the collateral terms needs to learn to interpret them or obtain an adequate interpretation from an appropriate specialist. Once the interpretation is adequate, the account can proceed without a fresh investigation of the already established receipt. If the terms later provide that collateral is applied to the debt, establish the event and effect under that changed condition before updating the obligation.

### FDM.4:6 - Bias-Annotation

A service team may equate its own successful step with the recipient's result. A financial reporter may give the latest posting more authority than its evidential meaning supports. Recover the effect and its rule before judging either account.

When the available sources cannot establish whether the event occurred, retain that uncertainty.

### FDM.4:7 - Conformance Checklist

For the effect being asserted, examine whether:

1. The affected party, prior position, claimed change and relevant time are clear.
2. The applicable rule and its action, authority or occurrence conditions are established where required.
3. Evidence supports the actual event at the scope claimed.
4. The derived effect and any residual obligation follow the applicable terms.
5. Records, effective relations and resource availability remain distinct where their differences matter.
6. The result distinguishes supported change, supported non-change and unresolved effect.

A calculation can verify the consequence of supplied premises. It cannot establish the missing event or institutional rule.

### FDM.4:8 - Common Anti-Patterns and How to Avoid Them

**Closing the obligation from a sent instruction.** Establish the event the applicable arrangement recognizes as performance.

**Treating all postings as either constitutive or merely descriptive.** Recover the actual rule and the role of the recording act in that arrangement.

**Using one date for every consequence.** Retain distinct occurrence, effect or availability dates when they change the receiving answer.

### FDM.4:9 - Consequences

The practitioner can explain what a financial action actually changed and what remains. Local system success no longer automatically becomes a broader completion claim.

The work can expose a missing rule, uncertain event or account correction. Resolving it may require another participant or specialist.

### FDM.4:10 - Architectural Rationale

The method joins a governing rule with an actual occurrence because neither alone establishes the particular effect. A generic term describes what would happen; an event description becomes financially meaningful through the applicable conditions.

A transaction log is sufficient when it already supplies adequate evidence for a settled effect rule. A broad business-outcome inquiry is unnecessary for a narrow residual-balance question. The wider inquiry becomes useful when someone claims the financial change itself established the participant's benefit.

### FDM.4:11 - SoTA-Echoing

The practice question is how to distinguish an actual financial effect from a decision, message or record. The method applies FPF's duty, permission and communicative-work distinctions to financial actions, with ADM.3 and ADM.9–10 supplying effectivity, usable provision and fulfillment questions.

This changes §§4.2–4.4: recover the effect rule, establish the occurrence and derive the remaining position. At the effort of examining one completion claim, it can distinguish “60 instructed” from “60 paid”, which a status-only reading conflates. More extensive investigation is justified when the unresolved premise changes the receiving use.

Actual local rules and event evidence govern an actual result. Reopen the account when either changes or when a later use requires a broader effect claim.

### FDM.4:12 - Relations

FDM.1–2 supply positions and parties. FDM.3 supplies contractual event logic and consumes the resulting actual state. FDM.5 uses the supported effect in a service-contribution account.

ADM.3, ADM.7–10 and the relevant financial practice supply effectivity, evidence, permission, usable provision and fulfillment questions at their own scope. A.2.8, A.2.8.PER and A.2.9 govern the underlying institutional distinctions.

### FDM.4:End

## FDM.5 - Trace a Financial Service to a Participant's Result

**Type:** Architectural

**Status:** Stable


### FDM.5:0 - Use this when

Use this pattern when a score, report, advice, interface or transaction service is called a financial benefit without explaining the receiving use. Begin with the participant and the result the service is supposed to help them obtain.

The pattern governs an explanation of a financial service's contribution. It returns the relevant output, use, financial effect and participant result, with the support and uncertainty appropriate to the claim being made.

Use an adequate existing contribution account directly. A routine service need not be redesigned merely to describe its established result.

### FDM.5:1 - Problem frame

A scoring team can improve predictive accuracy while leaving lending decisions unchanged. An admission tool can produce accurate client information while a separate arrangement determines permission to use a service. A payment provider can complete its own processing while the recipient still lacks usable funds.

Each output can be useful. Its contribution depends on a receiving participant, an actual or proposed use and the financial result that use can affect. The tool developer, decision maker, service provider and beneficiary need not be the same participant.

### FDM.5:2 - Problem

Output quality is often used as evidence of an entire financial result. This hides an unused output, missing decision, failed provision or adverse consequence for another participant.

Expanding the service boundary to every eventual business outcome is also unhelpful. It can make a provider responsible for results it neither decides nor supplies. The working problem is to explain the relevant contribution and its limits at enough scope to support the current decision.

### FDM.5:3 - Forces

A service needs a recognizable useful result. Different participants can want different results, and a throughput measure may not express their shared interest. A legitimate refusal can be preferable to another admission.

Longer-term outcomes depend on more conditions than the service controls. A useful model can name those conditions without claiming either sole causation or complete ignorance about the service's contribution.

### FDM.5:4 - Solution

#### FDM.5:4.1 - Name the participant and intended result

Identify the participant whose result is at issue and what would improve for them: access to usable funds, a warranted lending decision, timely payment, a better understood exposure or another concrete gain. Establish the horizon and comparison the present question needs.

When several participants matter, retain their differing objectives and consequences. A lender's result and a borrower's result need not be identical. Use the responsible financial or management practice to settle a disputed objective or choice criterion.

#### FDM.5:4.2 - Locate the output and its actual receiver

Identify the service output and who uses it. Separate the method, its implementation, one performed use and the produced result where their differences affect the account. A score is one output of a scoring arrangement; it is not the arrangement itself.

Ask the receiving participant how the output enters their work. A human or an authorized automated arrangement can use it. There is no mandatory intermediate change in a human's private expectation. Conversely, delivering data to an application does not establish that it influenced the relevant action.

A supplier can properly deliver information to another actor. Give that supplier's contribution its actual scope instead of redefining every upstream tool as if it directly provided the final financial outcome.

#### FDM.5:4.3 - Follow the use through the financial effect

Identify the decision or action the output can change and the financial relation or resource consequence that action can establish. Use FDM.1–4 where the position, terms or actual effect is unclear.

For a proposed service, explain the mechanism and assumptions under which the contribution is expected. For an actual service, obtain evidence of the receiving use and effect at the scope claimed. These can have different truth status within the same explanation.

Follow the connection far enough to answer the participant's question. A loan can provide usable proceeds; an equipment purchase can fail to deliver a working asset; changed demand can defeat the expected return from that asset. The financial service can have supplied its promised result while a later business outcome fails.

#### FDM.5:4.4 - Examine the contribution and its failure points

Ask what would happen without this output or with the relevant alternative. Is the decision unchanged? Does another source already supply the same information? Can funding, authority, timing, delivery or subsequent use defeat the proposed gain?

Inspect the explanations that can change the present conclusion. A claim about improved financial outcomes may need a suitable comparison, uncertainty account and evidence of causes. An output-accuracy measure alone cannot supply them. Use the relevant evaluation or inquiry method when that further claim is required.

Preserve justified narrower claims. The service may improve the available decision information while its outcome effect remains unmeasured. It may supply a usable financial result under conditions outside its control. Locate the unanswered question rather than collapsing all evidence into either “benefit proved” or “no value”.

#### FDM.5:4.5 - Return a qualified contribution and next action

Return an explanation that a receiver can use: the participant, service output, receiving use, relevant financial effect, intended result and material conditions. A simple connected paragraph can be enough.

State the supported result and the next missing evidence or decision. A contribution model can be complete for its current use before the loan matures or a long-term causal study finishes. A wider promise requires the further evidence appropriate to that promise.

### FDM.5:5 - Archetypal Grounding

A scoring team supplies a lender with a score about a proposed borrower. The score's meaning and validation conditions are given by its method. In the constructed loan, the lender considers advancing 100 with 105 contractually due on day 30.

First locate the receiving decision arrangement. Suppose it uses an established rule under which both the earlier and new score lead to the same decision and terms. Improved score accuracy alone does not establish a changed financial outcome in this case. The team can still investigate another useful effect, such as a reduction in warranted information-gathering effort, without attributing an unobserved lending gain to the score.

In another case, the adequately authorized arrangement uses the score to change a decision under its applicable method. FDM.4 establishes what the decision, formation and funding actually change. Successful funding makes the stipulated proceeds usable by the borrower and establishes the funded positions under the supplied terms.

The borrower intends to acquire equipment. If the equipment is delivered and usable, that can supply the next intended condition. If delivery fails, the loan's financial effect and the failed equipment result remain distinguishable. The service account explains where the connection broke. Whether the financed work later earns the hoped-for return requires its own business evidence.

A treasury modeling service supplies another use. In FDM.3:5.2, changing the accrual rule changes whether provision of 2,676 is enough. The model gives treasury a qualified requirement that it can use to choose a funding or payment action. FDM.4 establishes the effect of the action actually taken. Locating the shortfall is a useful output even before an action is chosen, while a claim of avoided loss needs evidence that the action and comparison support it.

The same construction applies to a client-admission service. An information supplier provides facts; the applicable arrangement grants or refuses access; actual service provision follows under its conditions. More admitted clients is not by itself an adequate objective. Legitimate refusal, the client's intended use and the provider's obligations can make a different result preferable.

### FDM.5:6 - Bias-Annotation

A developer may overvalue improvements visible in the tool's own metrics. A business sponsor may prefer the final benefit and omit the intervening assumptions. Recover both the actual output and the receiving use.

A reported source case can also tempt the modeler to require one organization or human role arrangement everywhere. Preserve the relevant functions and actual authority while allowing different competent human and automated arrangements.

### FDM.5:7 - Conformance Checklist

For the contribution being claimed, examine whether:

1. The relevant participant, intended result and horizon are identifiable.
2. The service output and receiving use have adequate meanings and boundaries.
3. The proposed or actual financial effect is connected through the applicable decision, action and terms.
4. Output quality, actual use, financial effect and later participant outcome retain their different evidence and uncertainty.
5. Material alternatives and failure points have been examined where they can change the conclusion.
6. The result states the supported contribution and any specific next evidence or decision needed.

A coherent contribution model supports understanding and inquiry. An observed improvement or causal benefit needs the evidence its stronger claim requires.

### FDM.5:8 - Common Anti-Patterns and How to Avoid Them

**Calling score accuracy a financial return.** Establish the receiving use, relevant comparison and financial consequence.

**Requiring the tool supplier to be the final decision maker.** Locate the actual receiver and the supplier's contribution to that receiver's work.

**Making every service responsible for the participant's whole future.** Retain the material connection and its conditions while distinguishing the service result from later outcomes.

### FDM.5:9 - Consequences

The team can explain what its financial service contributes and can locate an unused output or failed connection. This can change the next investigation, service boundary or improvement effort.

The account may support a narrower benefit than a sponsor initially claimed. It can also reveal a useful contribution that a final-outcome-only measure concealed. A wider causal conclusion increases the evidence and comparison burden.

### FDM.5:10 - Architectural Rationale

The participant's intended result provides the reason to follow the service connection. The output and actual receiving use keep that connection grounded. Together they permit a modest upstream contribution without making the whole business outcome the provider's direct product.

A technical output specification is sufficient for a settled supplier interface. It becomes inadequate when the disputed question is financial value. A complete business redesign is unnecessary when locating one missing use or effect answers that question.

### FDM.5:11 - SoTA-Echoing

The practice question is how to relate a financial tool or service to a participant's useful result. The method follows the actual receiver and effect of a service output. An automated arrangement can act on a score, and a warranted refusal can serve the participant's objective better than admission; the model therefore follows the particular decision and result.

This changes §§4.1–4.4: distinguish the supplier's output, the receiving decision and the participant's financial consequence, then examine the alternative that could defeat the claimed contribution. At the effort of one connected use account, it can expose an unused score that an accuracy report misses. A wider outcome study becomes useful when the stronger benefit claim could change a decision.

FDM.1–4, ADM and the relevant decision practice supply the distinctions used in this account. Reopen the contribution account when the receiver, decision arrangement, financial terms or intended result changes.

### FDM.5:12 - Relations

FDM.1–4 supply the financial positions, boundaries, events and actual effects needed by this service question. [ADM.7–10][ADM] supply evidence, permission, usable provision and fulfillment where those administrative questions arise.

SIE supplies the general model connection. The relevant financial, operating or management practice supplies decision criteria and comparisons. When service design or provider choice is the unresolved task, use the relevant service-design or provider-selection method.

### FDM.5:End

# References

Copyright © Anatoly Levenchuk. The original framework text and worked examples are licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). The [licensing notice](https://github.com/ailev/FPF/blob/main/LICENSING.md) states the scope and attribution terms. Referenced third-party works retain their own terms.

<a id="edition-record"></a>

## FDM.Reference:1 - Edition record

**FDM 1.0** is the first edition of *Financial Domain Modeling Principles Framework*, containing FDM.1–FDM.5. Cite this edition with the pattern and section, for example **FDM 1.0, FDM.1:5**.

<a id="source-locators"></a>

## FDM.Reference:2 - Source locators


- [FIBO, EDM Council][FIBO]: reusable financial concepts and their relations.
- [ACTUS technical-specification entry][ACTUS], [v1.1 specification][ACTUS-SPEC] and [terms dictionary][ACTUS-TERMS]: schedules, state, calculations and event transitions, with the edition boundaries discussed in FDM.3:11.
- [ACTUS analytics account][ACTUS-ANALYTICS] and [Quick Start][ACTUS-QUICKSTART]: the connection to analytical uses and an implementation entry.
- FINOS CDM 7.0.0, [Event Model][CDM-EVENT] and [Legal Agreements model][CDM-LEGAL]: agreement content and lifecycle-state distinctions.
- [AASB 10 §19 and B86–B88][AASB10]: a specific reporting basis for the policy-alignment and consolidation comparison in FDM.2:11.
- FPF A.2.8, A.2.8.PER and A.2.9: actual duty, permission and communicative-work distinctions.
- [Semantic Integration Engineering][SIE], SIE.3–6: model construction, correspondence, identity and composition.
- [Organization Administration][ADM], ADM.2–4 and ADM.7–10: applied participant, effectivity, account, evidence, permission, provision and fulfillment questions.

[SIE]: SEMANTIC-INTEGRATION-ENGINEERING-PRINCIPLES-FRAMEWORK.md
[MA4]: MANAGEMENT-ACCOUNTING-PRINCIPLES-FRAMEWORK.md#ma4---reconcile-operating-reporting-and-cash-accounts
[MA5]: MANAGEMENT-ACCOUNTING-PRINCIPLES-FRAMEWORK.md#ma5---construct-and-update-an-operating-forecast
[EW]: ../FPF-Spec.md#b15ew---recover-how-constituent-actions-enact-encompassing-work
[ADM]: ORGANIZATION-ADMINISTRATION-PRINCIPLES-FRAMEWORK.md
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
[FIN2]: CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin2---assess-liquidity-and-funding-needs-by-date
[FIN10]: CORPORATE-FINANCE-PRINCIPLES-FRAMEWORK.md#fin10---design-financing-instruments-and-terms

## FDM.Reference:End
