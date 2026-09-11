# Organization Administration Principles Framework

**Author:** Anatoly Levenchuk, with AI-assisted development and review\
**Release date:** 11 September 2026\
**Status:** Eternal alpha — an evolving framework, revised as methods and evidence improve.

ADM helps administrators examine administrative requests, give justified refusals and provide usable results under the organization's rules. Its fifteen patterns also help improve the arrangements supporting this work by connecting organizational rules, participants, permissions, work and records. Establish any permission required for the action being taken; specialist decisions remain with the people authorized to make them.

[First edition and source basis](#first-edition)

# Table of Contents

**Reader entry**

| § | Publication unit | Use |
| --- | --- | --- |
| R | [Organization Administration Readme](#organization-administration-readme) | Choose a first question and obtain a usable result. |
| P | [Preface](#preface) | Understand the administrative field, its connected methods and their limits. |

**Part A - Identify the Work and the Organizational Condition**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| A.1 | [ADM.1 - Frame the Work Being Enabled](#adm1---frame-the-work-being-enabled) | Stable | What is this request for?; trip complete; business result; service boundary | [OPS.3][OPS] and [C.32.MWA][MWA] for a disputed work or structure boundary. |
| A.2 | [ADM.2 - Establish the Relevant Participants and Relations](#adm2---establish-the-relevant-participants-and-relations) | Stable | Who receives?; who decides?; assignment; counterparty; authority | [A.6.REL][REL]; an adequate assignment may come from [OCE.6][OCE]. |
| A.3 | [ADM.3 - Determine What Changed and When It Takes Effect](#adm3---determine-what-changed-and-when-it-takes-effect) | Stable | Effective date; future appointment; suspension; record correction | [A.6.REL][REL]; ADM.2 when the relevant relation is unclear. |
| A.4 | [ADM.4 - Reconcile Participant-Relative Accounts](#adm4---reconcile-participant-relative-accounts) | Stable | Payer and recipient; same transfer; different records; conflicting claims | [SIE.4–6][SIE] for unresolved cross-source meaning or identity; ADM.3 when effectivity matters. |

**Part B - Design the Repeated Case, Resolve Exceptions and Supply the Result**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| B.1 | [ADM.5 - Design the Reusable Administrative Case](#adm5---design-the-reusable-administrative-case) | Stable | Repeated request; service instruction; approval and provision; ordinary correction | ADM.1–3 for unsettled inputs; ADM.6–10 for the needed handling actions; [OPS.5–6][OPS]. |
| B.2 | [ADM.6 - Resolve an Administrative Exception](#adm6---resolve-an-administrative-exception) | Stable | Opaque refusal; missing authority; conflicting requirement; competent return | ADM.7–9 for the missing claim, permission or provision; [OPS.6][OPS] for situated continuation. |
| B.3 | [ADM.7 - Check the Claim Needed for This Decision](#adm7---check-the-claim-needed-for-this-decision) | Stable | Evidence reuse; wrong test; insufficient evidence; unavailable checker | [A.10][A10] for source-to-use recovery; [SYSE.28][SYSE] when check placement needs design. |
| B.4 | [ADM.8 - Establish and Exercise the Required Permission](#adm8---establish-and-exercise-the-required-permission) | Stable | Standing grant; spending authority; read versus download; conflicting restriction | [A.2.8.PER][PER]; ADM.2–3 for participant or effective-time questions. |
| B.5 | [ADM.9 - Provide a Usable Administrative Result](#adm9---provide-a-usable-administrative-result) | Stable | Approved but unusable; failed access; partial effect; safe recovery | ADM.8 for an unresolved permission; [SYSE.26][SYSE] when supported interaction or recovery needs design. |
| B.6 | [ADM.10 - Reconcile What Was Owed, Performed and Recorded](#adm10---reconcile-what-was-owed-performed-and-recorded) | Stable | Unconfirmed payment; obligation; fulfillment; record correction; gross and net | ADM.3–4 for time and correspondence; ADM.7–9 for a needed check, permission or provision; [OPS.15][OPS]. |

**Part C - Engineer the Administrative Arrangement**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| C.1 | [ADM.11 - Join Providers Around the Administrative Result](#adm11---join-providers-around-the-administrative-result) | Stable | Provider handoff; local completion; receiving prerequisites; failed join | [SYSE.8][SYSE] and [OPS.8][OPS]; ADM.2–3 and ADM.8 for institutional inputs; [SYSE.24][SYSE] for a complete obtaining choice. |
| C.2 | [ADM.13 - Keep Administrative Records Fit for Their Uses](#adm13---keep-administrative-records-fit-for-their-uses) | Stable | Earlier decision; correction history; retention; disposal; authorized retrieval | ADM.3–4; [A.10][A10] and [SIE.4–6][SIE] for source, meaning and identity questions. |
| C.3 | [ADM.14 - Connect a Control to Its Purpose and Competent Decision](#adm14---connect-a-control-to-its-purpose-and-competent-decision) | Stable | Control purpose; rule owner; wrong proxy; qualified check; remedy | [SYSE.9][SYSE] and [SYSE.28][SYSE]; ADM.6–8 for case use; ADM.15 for consequences. |

**Part D - Assess and Change the Arrangement**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| D.1 | [ADM.15 - Judge Administrative Consequences](#adm15---judge-administrative-consequences) | Stable | Usable result; mistaken refusal; pre-entry failure; T+N; shifted effort | ADM.1 and ADM.7–10; [OPS.12–15][OPS] and [OCE.13][OCE] for the relevant consequence question. |
| D.2 | [ADM.16 - Change an Administrative Arrangement Without Losing Open Cases](#adm16---change-an-administrative-arrangement-without-losing-open-cases) | Stable | Old and new terms; transition authority; open claim; retention; independent handling | ADM.13–15; [SYSE.29][SYSE] for technical transition; [ME.15][ME] for method variants; [ME.17][ME] for Method Engineering culture. |

**Source return**

| § | Publication unit | Use |
| --- | --- | --- |
| S | [Sources and direct returns](#sources-and-direct-returns) | Recover the applied instructions, source arguments and their limits. |

# Organization Administration Readme

## Practical entries

ADM-E1–ADM-E7 are ordinary practical entries. They are selected examples, not a catalogue or a coverage boundary. Bring the actual question; if no example fits, use the Table of Contents or the opening of the relevant pattern.

**ADM** is the reference code for this framework. In `ADM.15:4.3`, `15` identifies the pattern and `4.3` identifies its section. The ToC's Part and `§` position show publication order; they prescribe no order of use.

### ADM-E1 — The trip is marked complete, but the work failed

- **Situation:** Transport, accommodation and expenses were arranged, but the visit produced no agreement.
- **Question:** Which result is complete, and who takes the next action?
- **First useful result or honest blocker:** A separate account of the travel condition supplied and the unsuccessful negotiating work. A missing travel condition remains an administrative question; the next negotiating decision belongs to the person responsible for that work.
- **Start with:** [ADM.1](#adm1---frame-the-work-being-enabled).
- **Stop or return:** Stop when the needed condition, recipient, provider and time are clear. Return the business decision to its responsible person; use the applicable service instruction for unfinished administrative provision.

### ADM-E2 — A future appointment is being used for today's access request

- **Situation:** A request for 25 September relies on an appointment effective on 1 October.
- **Question:** Does the supplied appointment satisfy the request's eligibility condition at the intended time?
- **First useful result or honest blocker:** This appointment does not meet the effective-appointment condition on 25 September. That established negative result answers the time question for the supplied appointment.
- **Start with:** [ADM.3](#adm3---determine-what-changed-and-when-it-takes-effect); use [ADM.2](#adm2---establish-the-relevant-participants-and-relations) if the relevant participant or grant is unclear.
- **Stop or return:** Use the negative result under the applicable service rule for its required response. If a different appointment or other applicable basis is actually claimed and remains unresolved, send that specific question to its competent source or decision maker. A later-date request still needs its applicable permission and usable provision.

### ADM-E3 — One party says “payment” and the other says “receipt”

- **Situation:** The payer's outgoing payment record and the recipient's incoming receipt record may concern the same transfer.
- **Question:** Are these compatible accounts, different events, or a real disagreement?
- **First useful result or honest blocker:** A supported correspondence preserving each participant's meaning, or the exact identity, amount, timing or authority question that prevents combining the accounts.
- **Start with:** [ADM.4](#adm4---reconcile-participant-relative-accounts).
- **Stop or return:** Keep both correct accounts when they describe one event from different participants' positions. Obtain missing effect evidence before treating a payment as settled or issuing a potentially duplicate payment.

### ADM-E4 — A new service has a form but no usable handling instruction

- **Situation:** A service owner has a reimbursement policy and prospective providers, but handlers cannot follow a request through to actual payment.
- **Question:** What reusable instruction connects the request, necessary evidence, competent decision and usable result?
- **First useful result or honest blocker:** A bounded handling instruction that includes ordinary correction, refusal, completion evidence and genuine exception returns; or the exact missing policy, authority or provider contribution.
- **Start with:** [ADM.5](#adm5---design-the-reusable-administrative-case).
- **Stop or return:** Exercise the instruction with the intended participants and return the design and its limits. Individual requests then use that instruction; a completed design does not itself approve or pay a claim.

### ADM-E5 — Access is approved, but the recipient still cannot use it

- **Situation:** An effective read grant and required identity result are available, but the recipient's attempt to open the promised document fails.
- **Question:** What provider action will supply the authorized usable condition?
- **First useful result or honest blocker:** Working access within the grant, with adequate effect evidence, or a precise provider failure and accountable recovery action.
- **Start with:** [ADM.9](#adm9---provide-a-usable-administrative-result).
- **Stop or return:** Use an adequate permitted recovery route. Return to [ADM.8](#adm8---establish-and-exercise-the-required-permission) when the proposed action or effective conditions change; recover an unknown earlier effect before any potentially duplicate provision.

### ADM-E6 — Closed requests conceal the service's actual outcome

- **Situation:** A portal reports 70 closed requests out of 80, while some refusals were mistaken and other applicants never reached registration.
- **Question:** What did the service actually supply, and which consequence should change the next decision?
- **First useful result or honest blocker:** A bounded account separating usable provision, correct and mistaken refusal, unfinished requests and relevant entry failures, with the evidence or uncertainty that matters.
- **Start with:** [ADM.15](#adm15---judge-administrative-consequences).
- **Stop or return:** Use established defects for their applicable correction. Return a control, provider or transition question to its competent owner; obtain further observations only when their answer can change a live decision or required claim.

### ADM-E7 — A new policy starts while earlier cases remain open

- **Situation:** A service owner is introducing an allowance while receipt-based journeys, unsettled payments and disputed claims remain.
- **Question:** Which conditions govern each affected use, and how will its legitimate result remain available?
- **First useful result or honest blocker:** The competent transition decision and executable case dispositions, or the precise missing authority, provider or evidence result.
- **Start with:** [ADM.16](#adm16---change-an-administrative-arrangement-without-losing-open-cases).
- **Stop or return:** Apply the actual cohort rule and preserve required recovery and records. A changed form does not decide which old terms end; adequate current evidence may instead support retaining the arrangement.

# Preface

## ADM.Preface:1 - The working problem

Organization Administration concerns the institutional conditions and services through which people can do organizational work. A researcher needs legitimate access to an archive. A traveller needs an approved journey and usable accommodation. A supplier needs the agreed payment to arrive. The administrator's useful result is the particular condition supplied to the relevant participant under the applicable rules.

The work enabled can have a different outcome. A correctly administered journey can end in unsuccessful negotiations. Conversely, someone may complete the business task despite a failed administrative service by spending personal time or obtaining an improvised workaround. Judging only the business result conceals the service failure; judging only closed requests conceals the burden on the person trying to work.

The practical difficulty is often smaller than “redesign administration”. A handler may need to establish which person is entitled to receive a result, whether an appointment is effective yet, or whether two records describe the same event. A service owner may instead need to design a repeatable handling instruction or coordinate several providers. Selecting the actual question keeps each inquiry proportionate.

## ADM.Preface:2 - How the contributions connect

The four patterns in Part A provide different first results. ADM.1 identifies the administrative condition needed for particular work. ADM.2 identifies the participants and organizational relations that determine who may receive, decide or perform an action. ADM.3 determines the relevant change and its effective time. ADM.4 establishes how participant accounts correspond and which disagreements remain.

Part B connects those results to design and actual handling. ADM.5 produces a reusable case instruction when one is missing. A handler uses ADM.6 for a genuine obstacle, ADM.7 for a needed claim check and ADM.8 for the particular permission. ADM.9 connects authorized performance to the beneficiary's usable condition. ADM.10 reconciles an obligation, its actual fulfillment and the participant records. These are different entry questions; an ordinary case with adequate inputs and an existing instruction can proceed directly.

Part C concerns the arrangement that supplies those cases. ADM.11 joins provider contributions around the recipient's result and the actual undertakings that support it. ADM.13 keeps records fit for their legitimate current and historical uses. ADM.14 connects a reusable control to its purpose, qualified check, competent decision and remedy. Use these questions when an existing arrangement is insufficient; a routine handler can apply adequate provider and control instructions directly.

Part D supports retention and change. ADM.15 examines provision, correctness, restrictions, recovery and burden for the population the decision concerns. ADM.16 uses the relevant evidence to retain the arrangement or obtain and implement its competent transition decision. Open cases, active permissions, obligations and record uses retain the conditions that actually govern them until those conditions are validly changed.

Use a result when the next question needs it. An existing, adequate appointment can be used directly; a handler does not repeat an organizational investigation for every request. An unexplained effective date calls for ADM.3. An amount mismatch between records may start at ADM.4. The publication order is a finding aid; these questions do not require four stages for every case.

For example, a researcher asks for archive access on 25 September to prepare an experiment. ADM.1 identifies the needed condition as usable access by that date. ADM.2 finds that the supplied access rule requires an effective appointment and a distinct read grant. ADM.3 establishes that the offered appointment begins on 1 October, so it does not satisfy the appointment condition on 25 September. That negative result settles the time question for the supplied basis. The handler applies the service rule to that result; a further eligibility inquiry is not needed merely because the result is negative.

If the researcher separately claims an earlier appointment whose decision and scope are unavailable, that is a different unresolved basis. The issuing appointment office receives the specific question of whether that appointment covers the researcher, relevant work and September date. For a request on 2 October, an effective appointment and valid read grant may already be supplied; if login fails, the next task is to repair provision under that grant.

These results also supply administrative inputs to wider work. ADM.5 helps a service owner design a repeatable instruction for receiving, checking, deciding, providing and recording requests. Its result is the instruction; it neither decides a particular request nor performs its provision. During actual handling, OPS.5–6 can resolve admission or situated continuation questions. When a project must choose how to obtain replacement provision, SYSE.24 compares the complete arrangements using adequate administrative permissions, responsibilities and provider conditions. A routine request through an established provider can use its existing instruction directly.

The same distinction matters when a record says “paid” but an earlier payment's effect is unknown. ADM.7 identifies the missing effect claim, ADM.9 recovers the provider attempt, and ADM.10 applies the actual fulfillment rule to the evidenced credit. These are connected questions in that case, not compulsory stages for every payment. A confirmed adequate result can be reused. A sent instruction or a corrected record cannot create a missing credit.

A service owner can then use the recurring evidence at a different scale. Repeated lost payment responses may reveal a provider join to repair through ADM.11, a claim check to reconsider through ADM.14 or a consequence account to examine through ADM.15. ADM.13 preserves the grounds needed to recover those events. If a changed arrangement is selected, ADM.16 keeps the old cases and unresolved effects connected to their applicable conditions. One adequately resolved case does not automatically establish a service-wide improvement.

## ADM.Preface:3 - Different things, different accounts and different structures

First establish what each statement concerns. “The trip” may mean a journey, negotiating work or the administrative handling that enabled both. Those are related subjects with different completion conditions. By contrast, the payer's disbursement and the recipient's receipt can be correct accounts of one transfer. A useful common account preserves the correspondence between them.

An organizational relation also differs from a claim about it. An appointment can already be effective although a directory has not been updated. A future appointment can already be recorded although it is not effective today. Some rules make registration part of constitution; in those cases the record-related act matters because the rule makes it matter. The practitioner determines which situation applies from the supplied rule and facts.

Several arrangements can concern the same people without becoming one hierarchy. One service may support several projects; one administrative case may require several specialist decisions and providers. A shared record can help the participants coordinate while their responsibilities remain distinct. Use the actual enabling, provision, assignment and evidence relations. When a decision depends on comparing several structures, C.32.MWA supplies that comparison; the common label or shared people do not establish parthood.

Consider two projects whose researchers need archive access during the same morning. In this constructed case, each request has an adequate appointment, identity result and valid grant, but each still needs an account mapping before the archive provider can configure usable access. That mapping is a prerequisite of configuration; it is not a prerequisite of the identity check that has already supplied its result.

Both requests are ready for mapping. The same qualified specialist has one two-hour window, and each mapping requires two hours of that specialist's work under the supplied method. Each request fits alone; together they require four hours. The responsible service parties must resolve priorities, timing or qualified additional provision under their actual commitments before promising both in that window. ADM.11 identifies the shared contribution and its receiving inputs. ADM.9 establishes the usable access after provision, and ADM.15 accounts for the recipients' waiting and any displaced work.

The projects, requests, providers and grants therefore have different boundaries. The appointment and grant results can remain adequate while the combined provider promise is unsupported. A larger window or qualified additional capacity changes that promise question; reuse earlier results only within their scope and effective time. If the revised use exceeds those conditions, return to ADM.3 or ADM.8 for the relevant time or permission question. Use C.32.MWA when the decision needs a fuller comparison of such structures.

## ADM.Preface:4 - Correct use and its cost

The first pass can fit in an ordinary request or note: name the action or condition, the participants it concerns, the governing rule when one matters, the relevant time, the available grounds and the next action. Add a timeline, comparison table or explicit event identity only when the receiving decision requires it. A service-level inquiry also names its population and the consequence that could change the decision.

For a consequential use, examine whether the result distinguishes the requested condition from its evidence, identifies who may resolve a missing condition, and preserves any limitation that changes the next action. A claim of completed provision needs the promised usable effect. A supported relation claim needs the applicable rule and facts. A common event account needs enough correspondence to distinguish it from another event. These are different questions, and an adequate answer to one can be reused without pretending that it answers the others.

Elapsed delay, labor and money also answer different questions. The laboratory's T+N shorthand needs an explicit starting event and administrative result; reducing that delay can still worsen correctness or shift effort to the applicant. Include relevant unfinished and pre-entry cases before treating a portal indicator as the service outcome. A bounded observed defect may support a correction while a general effectiveness or causal claim remains unresolved.

This approach can reduce repeated checking, opaque refusals and unnecessary reconciliation. It also requires access to people and evidence that a portal may hide. A participant's account can remain unresolved when a needed source or qualified decision is unavailable. State the missing result and who can supply it; useful administrative framing can finish with that actionable gap.

## ADM.Preface:5 - Why use this language

General operations methods already organize cases and current work; semantic-integration methods already align meanings and identities. The recurring administrative difficulty is connecting those results to institutional eligibility, authority, effectivity and the condition owed to a participant. Keeping those questions together helps a handler choose the next action without replacing the specialist's rules.

A complete legal, tax, financial, employment or security determination remains with the qualified source and competent decision maker for that question. These patterns explain how to identify, request and use such a result. They do not supply a jurisdiction's substantive rule merely by naming its subject.

A single portal or ledger is a possible implementation. It can reduce duplicate entry but can also conceal distinct meanings, authorities or unresolved provider effects. A whole-problem service boundary is useful when it follows the participant's needed result; it becomes costly when it expands into every related organizational problem. Choose the smallest arrangement that retains the needed relations and practical returns.

## ADM.Preface:6 - Sources, evidence and changed conditions

The administrative laboratory discussions contribute concrete failures and distinctions: an enabling service versus the enabled work, an organizational relation versus a record, and an opaque refusal versus an actionable condition. The framework connects the service to the participant's work and examines the burden of obtaining it. Its proposed methods and constructed cases explain how to address these questions; assess a particular service's performance from its actual use.

The Readme selects a few first questions from this field; the Preface connects institutional conditions, case handling, provider contributions and participant accounts. These entries shorten the full pattern instructions and omit case-specific rule details and specialist tests. Return to the relevant Solution before applying a branch whose conditions matter. The pattern bodies retain ordinary correction, established refusal, unresolved evidence and failure recovery as different outcomes.

The source discussions also contain broader accounting ontologies, technology proposals and particular reported incidents. This publication keeps the distinctions needed for administrative decisions and the resulting actions; it does not reproduce those complete source structures. Use the direct sources below when an interpretation, assumption or proposed extension depends on material that the pattern's stated use leaves outside. A local legal, financial, employment or security decision still requires its competent rule and evidence.

The strongest useful synthesis here combines those distinctions with the actual relation, permission, operations and semantic-integration instructions named in the patterns. The Partridge accounting and agentology arguments support preserving participant-relative meanings after event identity is established. Their full ontology and one-database proposals are not needed for that result. NIST's digital-identity guidance contributes a bounded distinction between identity processes and other eligibility or permission questions; its institutional authority does not determine a local entitlement.

The worked cases below are constructed. They state the policy and facts needed to reason through the next action. A successful construction shows how the instruction applies under those conditions. A walkthrough of a proposed transition, actual receiving use and later independent handling support different claims. Current adequate evidence can justify retaining the arrangement; an additional observation is selected for the decision it can change. Demonstrating organizational effectiveness requires observations of the actual service and affected participants, including failures, unfinished cases and displaced effort.

Revisit the affected result when the requested action, participant, rule, effective time, source meaning or evidence changes. Reuse unaffected results within their conditions. A corrected directory entry can justify a new account without creating another appointment; a valid policy change can alter later handling even if the old form remains unchanged.

# Part A - Identify the Work and the Organizational Condition

## ADM.1 - Frame the Work Being Enabled

**Type:** Architectural\
**Status:** Stable

### ADM.1:0 - Use this when

Use this pattern when an administrative request is hard to interpret, several providers call their part “done”, or one word such as “trip” hides different results. Begin with the person trying to do something and the condition the administration is expected to supply.

The pattern governs the relation between the work intended and its needed administrative condition. Its first result is a bounded enabling question: what condition is needed, for whom, from whom and by when. This lets the handler select the relevant service instruction or return a business question to the person responsible for that work.

If those facts are already clear and an adequate instruction covers the request, apply that instruction. A complete map of the organization adds nothing to a straightforward request.

### ADM.1:1 - Problem frame

A participant asks for travel, access, reimbursement, an appointment or another administrative result because it makes some work possible. The request may name a form or portal operation instead of the needed condition: “close the ticket”, “create an account”, or “approve the trip”. A local provider can perform that operation while the participant still cannot do the intended work.

The relevant participants may belong to different units or organizations. A research group requests access, an archive owner decides eligibility, and a technical provider provisions a credential. The administrative question connects their contributions to the needed condition across those unit or organizational boundaries.

### ADM.1:2 - Problem

How can a handler establish what administration is expected to supply, and recognize its completion, without confusing that result with the outcome of the work it enables?

A vague completion label has practical costs. It can send a failed negotiation to a travel desk, close an unusable access request, or make a service owner claim that administrative success guarantees a business outcome.

### ADM.1:3 - Forces

The handler needs enough context to identify the real result, but asking for the whole business plan can delay a simple service. Providers need precise boundaries for their commitments, while the participant needs a condition that works across those boundaries. An early answer should enable action, yet a superficially complete record can hide a missing permission or a failed provision.

These pressures favour a small explicit question. Expand it only where a missing distinction could change the provider, the applicable rule, the expected result or the next action.

### ADM.1:4 - Solution

#### ADM.1:4.1 - Recover the needed condition from the request

Ask what the participant intends to do and what administrative condition is missing. Use the participant's ordinary description first. “I need to examine the archive before the experiment” is more useful than beginning with the account-creation form.

Then name the condition that would make the administrative part usable. For archive work this may be permitted read access for the named researcher during the necessary interval. For a journey it may be authorized travel with usable transport and accommodation. Keep additional conditions only when they change the requested use.

Distinguish the condition from its usual evidence. A booking confirmation supports a claim about accommodation; the traveller still needs accommodation that can actually be used. Once the authorized decision maker approves the stated journey and expenditure under the travel rule, that authorization is established. The providers still have to supply usable transport and accommodation.

#### ADM.1:4.2 - Separate the subjects hidden by the label

For each completion or failure statement, ask what happened to what. “The trip succeeded” could concern the journey, the negotiating work, the administrative case or the records supporting expense settlement. State the relevant subject and its result before combining the statements.

Use a short comparison when several meanings are active. Different subjects may have an enabling relation, a contribution relation or some other connection. Determine that connection from the actual work. If the statements instead concern one event from different participants' positions, use ADM.4 to preserve their correct correspondence.

When an operations account is genuinely unclear about cases, work, resources or descriptions, OPS.3 supplies those distinctions. When several selected structures change the decision, use C.32.MWA. A routine enabling question does not require either inquiry to be repeated.

#### ADM.1:4.3 - Bound the administrative promise

Name the participant who needs the condition, the provider or providers expected to supply it, the relevant time and the supplied conditions for its use. Recover the applicable authority or eligibility through ADM.2 only when it is unresolved. Use ADM.3 when timing or change affects the answer.

Write a first result in ordinary language, for example:

> The archive service needs to provide Mara with usable, permitted read access to collection R by 25 September so that she can prepare experiment E. The archive owner decides eligibility; the access provider supplies the technical means. The experiment's outcome remains with the research team.

That statement is sufficient to locate the next service or eligibility question. It need not become a new form. If the provider is unknown, the first useful result can identify the missing responsibility and the service owner who must establish it.

#### ADM.1:4.4 - Choose the next action and stop

When the requested condition, recipient, provider and needed time are identified, and the applicable service instruction's prerequisites for the next handling action are established, the handler uses that instruction to obtain or verify provision. Reuse adequate supplied facts and decisions. If a required fact or decision is unresolved, the handler sends the specific question to someone able to resolve it: the deciding authority, specialist, provider or person responsible for the substantive work.

For a missing administrative condition, state what the participant still cannot use and why the local “done” evidence is insufficient. For a failed business result after the administrative condition was supplied, return the next business decision to the responsible person. An administrative provider can still examine its own contribution if new evidence connects it to that failure.

Framing finishes when the receiving person can act on the bounded question or identified gap. It does not have to wait for all the enabled work to finish.

#### ADM.1:4.5 - What changes in practice

The request becomes about a usable condition and a responsible next action. The handler can distinguish an incomplete service from an unsuccessful business task, and providers can see which joins matter to the participant's use. An already adequate request proceeds directly.

### ADM.1:5 - Archetypal Grounding

#### ADM.1:5.1 - A completed journey and an unsuccessful negotiation

In this constructed case, an employee travels to negotiate a supply agreement. The supplied travel rule requires an eligible traveller, authorized expenditure, usable transport and accommodation, and settlement of the required expenses. Those conditions are satisfied. The parties nevertheless fail to reach the intended agreement.

| Subject | Stipulated result | Next action |
| --- | --- | --- |
| Journey and stay | The employee travelled and used the accommodation. | Retain the relevant provision evidence for its intended administrative use. |
| Negotiating work | The parties reached no agreement. | The person responsible for the negotiating work decides whether to revise the offer, continue negotiations or stop. |
| Administrative handling | The stated travel conditions and required expense settlement were satisfied. | The handler may report that administrative result complete under the supplied rule. |

The first useful account names these results separately. It does not repair a failed negotiation by reopening a completed hotel booking. If the accommodation had been unusable and the employee had arranged a replacement personally, the administrative account would instead retain that failure and the displaced effort even if the negotiations later succeeded.

#### ADM.1:5.2 - An ordinary request that needs no reframing

A requester identifies the eligible traveller, destination, permitted dates and existing booking instruction. The provider and completion condition are clear. The handler uses that instruction. Asking for another description of the organizational architecture would add effort without changing the next action.

### ADM.1:6 - Bias-Annotation

An internal service view can privilege the provider's queue over the participant's actual work. Ask the participant what condition is usable and include a justified failed or abandoned request when it changes the service account. The business owner can also misattribute every failed outcome to administration; keep the claimed causal contribution separate from the observed service failure.

A participant may be unable to disclose the full business purpose. Request only enough permitted context to determine the needed condition and applicable rule.

### ADM.1:7 - Conformance Checklist

For the actual enabling question, examine whether:

1. The participant's intended work and the administrative condition are identifiable in ordinary language.
2. Each completion or failure claim refers to the relevant subject.
3. The recipient, provider, needed time and action-changing use conditions are supplied or named as unresolved.
4. Evidence such as an approval or provider message is interpreted against the promised condition.
5. The next action reaches someone able to resolve the remaining question, and an adequate ordinary request can proceed without a wider investigation.

These questions assess the framing. Whether the service was actually supplied requires evidence of that result under its applicable conditions.

### ADM.1:8 - Common Anti-Patterns and How to Avoid Them

**Closing the form while the condition is absent.** An account-creation ticket says “done”, but the person cannot read the authorized material. Return the usable-access question to the provider with the actual failed use and applicable grant.

**Treating one label as one subject.** A report counts “completed trips” without distinguishing journeys, business results and administrative cases. State which result is counted and retain any correspondence needed for the decision.

**Expanding every request into service redesign.** A handler sends an eligible ordinary request into a discovery workshop. Use the adequate existing instruction; reserve redesign for a repeated or unresolved arrangement problem.

### ADM.1:9 - Consequences

The handler gains a clearer service boundary and a smaller next task. This can make hidden provider failures and participant burden visible. It also prevents a service result from being used as evidence of an unrelated business success.

The result is limited by the available service conditions and context. If an organization has not assigned responsibility for the needed condition, identifying that gap is useful but does not supply the missing provider commitment.

### ADM.1:10 - Architectural Rationale

The enabled work is the starting point because it explains why the administrative condition matters. The administrative result remains separate because it has its own applicability, provider and completion evidence. This separation supports both a simple direct request and a service spanning several providers.

A department-first boundary can be adequate when one provider already supplies the entire needed condition. It becomes inadequate when a local completion leaves the participant unable to work. A whole-business boundary has the opposite cost: it can make administration responsible for results it neither decides nor supplies. The bounded enabling relation retains the useful connection without either expansion.

### ADM.1:11 - SoTA-Echoing

The practice question is how to define an administrative result at enough scope to help the participant without absorbing the whole business task. Keep the enabling administrative service distinct from the participant's business work, and use OPS.3 to distinguish cases, work and descriptions. Use C.32.MWA when competing structures change the answer.

The serious default is a department or catalogue item whose completion defines success. GOV.UK's whole-problem service guidance is a useful comparator because it expands attention to the user's needed outcome while cautioning against an oversized service. Here that contribution changes §§4.1–4.3: start from the needed condition, follow the relevant provider joins, and keep the business outcome separate. At the same first-pass effort, one condition sentence can expose a missing result that a ticket label conceals; a wider service inquiry is accepted only when that distinction changes action.

The July laboratory, especially 11:56–14:59 and 20:37–30:49, supplies reported situations and conceptual distinctions used in this synthesis. The GOV.UK guidance supplies a service-design comparison. The organization's rules determine local administrative authority; observations of the service are needed to judge an improvement claim.

Reconsider this selection if actual cases show that the stated condition fails to distinguish administrative completion from the enabled result, or if a smaller existing service instruction gives the same needed boundary more reliably.

### ADM.1:12 - Relations

ADM.2 supplies participants and organizational relations when those facts determine the request. ADM.3 resolves effectivity or change; ADM.4 compares accounts after their subjects are identified. These are conditional result uses, not steps required for every case.

OPS.3 supplies the general case/work/description distinction. C.32.MWA supplies a comparison of several structures when their non-matching boundaries affect the decision. The administrative handler uses the applicable service instruction for the next administrative action on the bounded question. The person responsible for the substantive work receives a business question.

### ADM.1:End

## ADM.2 - Establish the Relevant Participants and Relations

**Type:** Architectural\
**Status:** Stable

### ADM.2:0 - Use this when

Use this pattern when an administrative action depends on who the people or organizations are to one another: who may receive a service, who is responsible for it, who may decide, or who may perform the resulting action. Typical signals are “the employee is in the directory”, “management approved”, or “the administrator can do it” without the relation needed for this request.

The subject is the organizational relation that changes the administrative action. The first result names its participants, applicable conditions and grounds, or the exact missing relation that a competent person must resolve.

Reuse an adequate supplied assignment, entitlement or grant. If the only problem is a failed technical action under already established conditions, pass that problem to the provider using the existing instruction.

### ADM.2:1 - Problem frame

An administrator works with people in several capacities. The requester can act for a beneficiary. An organization's policy owner can define service conditions while another person decides an individual request. A technical operator can implement that decision. The relevant relations may connect people, organizations, resources and particular actions.

A role title is a useful clue to the source of those relations. It is insufficient when the intended action depends on a particular appointment, delegation, permission or obligation. A person can also fill several functions, each under its own conditions. The inquiry concerns the relation required for the action, rather than a count of departments or job titles.

### ADM.2:2 - Problem

How can a handler identify the participants and organizational standing that actually determine an administrative action?

If the handler substitutes an authenticated identity or a familiar role label for the relevant relation, the service may be provided to an ineligible recipient or refused to someone whose valid relation is missing from the convenient record. If decision authority and technical capability are conflated, an implementation action can silently replace a required decision.

### ADM.2:3 - Forces

Ordinary handling should reuse reliable facts and familiar responsibilities. A consequential action may nevertheless depend on a narrower grant or a different effective interval. An organizational chart makes people findable, but it may not show the counterparty, covered action or authority that this case needs.

The handler also needs a usable return when a relation cannot be established. Collecting more identity documents will not resolve every missing delegation or eligibility condition.

### ADM.2:4 - Solution

#### ADM.2:4.1 - Name the action and the participants it requires

Start with the proposed administrative action or needed condition. Identify the participant who would receive it and the person or organization expected to supply it. Distinguish the requester from the beneficiary when that difference affects the rule.

Then identify who may decide the unresolved question and who may perform the decided action. Keep only participants that change the result. A direct request with one authorized provider may require only a short sentence; a delegated payment may require the principal, delegate, payee and responsible treasury performer.

If a name, identifier or account may select the wrong person or organization, resolve that identity question before attaching organizational standing to it. SIE.5 supplies cross-source identity work when ordinary supplied evidence is inadequate.

#### ADM.2:4.2 - Recover the relation needed for this use

State the relation in ordinary language with its participants: “Mara holds the appointment covered by the archive eligibility rule”, “the archive custodian may grant read access to collection R”, or “Lee may configure the access that the custodian has granted”.

Recover the applicable source and conditions. Ask what establishes the relation, what action or resource it covers, when it applies, and what relevant restriction or ending condition can change the present use. A supplied current assignment can answer this inquiry directly. OCE.6 provides assignment results for an organizational-change question; reuse one only for the participants and responsibilities it actually establishes.

A.6.REL governs the underlying distinction between a relation obtaining and someone asserting or recording that it obtains. Its ordinary branch permits a readable relation statement. Add an occurrence identifier or a full relation model only when later work needs to distinguish another occurrence of that relation, including a later episode with the same participants.

#### ADM.2:4.3 - Keep eligibility, decision authority and performance distinct

For the intended action, ask which relation supplies each necessary condition. An effective appointment can make a person eligible to request access. A valid grant can permit a particular read action. A separate assignment and permission can allow a technical operator to configure the resource.

These facts can be supplied together in a well-designed service instruction. Keep them separately recoverable when a failure, restriction or later use depends on the difference. A.2.8.PER supplies the distinctions between granted permission, actual exercise and a finding of non-prohibition. A finding that no prohibition was located cannot fill a missing grant where the applicable rule requires one.

When a grant and another governing requirement imply incompatible conclusions for the same participant's action, identify the conflicting claims and their overlapping scope and time. First apply an existing precedence rule when its stated conditions select which claim governs that use. If the rule does not settle the conflict, reuse an adequate existing authorized decision or ask the person whose authority covers this conflict to decide which claim governs the specified action, scope and interval. Until a rule or such a decision settles it, return that question as unresolved. Do not infer precedence from record recency, seniority or technical capability.

#### ADM.2:4.4 - Return the usable participant account or the specific gap

The first result can be a short statement attached to the request. Name the relevant participants, the relation needed for each action, its effective conditions and the grounds that the receiving decision needs. Keep an unsupported relation claim explicit as a claim requiring resolution.

For example, “the supplied appointment establishes eligibility from 1 October; a read grant is still needed from the archive custodian” is actionable. “More approvals required” conceals the missing result and the person who can supply it.

A missing fact goes to a source or checker able to establish it. A missing grant or disputed rule application goes to the competent decision maker. If a valid condition is already met and provision failed, send the provider the authorized action and actual failure. Identification of a gap does not itself resolve it.

#### ADM.2:4.5 - What changes in practice

The handler asks the right person for the particular missing result and reuses adequate relations already supplied. Identity checking, eligibility, authority and technical performance no longer substitute for one another. The request can proceed as soon as its actual conditions are established.

### ADM.2:5 - Archetypal Grounding

#### ADM.2:5.1 - One access request, three different grounds

This constructed case concerns Mara reading collection R on 2 October for experiment E. The supplied archive rule makes an effective research appointment an eligibility condition. It authorizes the archive custodian to grant access and assigns technical configuration of an approved grant to Lee. The following case facts are supplied:

| Relevant relation | Supplied fact | Administrative consequence |
| --- | --- | --- |
| Research appointment | Mara's appointment is effective from 1 October and covers experiment E. | The appointment satisfies this case's stated appointment condition on 2 October. |
| Read grant | The custodian's valid grant permits Mara to read collection R during October. It excludes downloading. | The permitted action is reading within that scope and interval. |
| Configuration responsibility and permission | Lee is assigned and permitted to configure the granted access. | Lee can perform that configuration; a different access decision remains with the custodian. |

The handler can now ask Lee to repair Mara's failed login under the read grant. The result of this pattern is the participant and relation account that makes that request legitimate and precise. Whether Mara can actually read the collection still depends on successful provision.

A download request is a different action. The handler can state that it falls outside the supplied grant and return it through the archive's applicable decision route. The read grant is not widened by the technical availability of a download button.

#### ADM.2:5.2 - A familiar name identifies the wrong person

A directory contains two people named Mara. The appointment refers to one and the account request to the other. The handler first establishes the participant identity using the relevant sources. The appointment cannot be applied to the second person merely because the name matches.

If the identity and appointment were already unambiguous in an adequate request, the handler would reuse them. This pattern does not impose duplicate identity checking on every case.

#### ADM.2:5.3 - An applicable rule and an unresolved conflict

In both branches of this constructed case, Mara has the valid October read grant for collection R. A current security restriction prohibits reading that collection from 09:00 to 11:00 local time on 2 October. Her intended read is at 09:30. The grant and restriction therefore give incompatible conclusions about the same participant, action, collection and interval. The supplied authority account names the archive policy owner as the person authorized to resolve this kind of conflict.

In the first branch, an applicable policy explicitly gives that temporary security restriction precedence over read grants during the stated interval. The handler applies the rule and returns its result: the restriction governs Mara's 09:30 read, so that action cannot proceed under the grant. No further discretionary decision is needed to settle this inquiry. The result concerns the stated overlap; it does not rewrite the October grant.

In the second branch, the same grant, restriction, intended action and decision authority are supplied, but no applicable precedence rule or existing resolving decision is available. The handler returns the particular unresolved question to the archive policy owner: which claim governs Mara's read of R at 09:30 within the 09:00–11:00 restriction? Naming that person does not supply the answer. The handler does not authorize the disputed read from these inputs.

### ADM.2:6 - Bias-Annotation

Organizational charts and provider tools tend to foreground staff and ignore claimants, contractors, external counterparties or people represented by someone else. Include a participant when their relation changes the requested action, even if the convenient tool has no field for it.

Visible seniority can also bias a handler toward assuming authority. Recover the action-specific basis when it matters; expertise, employment, ownership and permission can have different implications under the supplied rule.

### ADM.2:7 - Conformance Checklist

For the named action, examine whether:

1. The requester, beneficiary, provider and decision maker are distinguished where their difference matters.
2. The needed relation is stated with its participants and applicable rule or adequate supplied result.
3. Its action, resource, interval and relevant restriction fit this use.
4. A role title, authenticated identity or technical capability has not replaced a missing institutional condition.
5. The result distinguishes an established relation, an unresolved claim and a missing decision.
6. The next request names both the missing result and someone competent to supply it.

The participant account supports the receiving action only within those conditions. It does not establish that the action was performed.

### ADM.2:8 - Common Anti-Patterns and How to Avoid Them

**Using the organizational chart as a universal permission table.** A person's department is known, but the requested expenditure exceeds the supplied delegation. Recover the delegation for that action and return the uncovered decision to its competent holder.

**Asking the technical operator to decide entitlement.** A provisioning team receives “please make it work” although eligibility is unresolved. Obtain that decision first, then give the operator the resulting action and scope.

**Repeating the wrong check.** Another identity check is requested when the actual missing fact is whether an appointment is effective. Reuse adequate identity evidence and resolve the relation or time question.

### ADM.2:9 - Consequences

A precise participant account can reduce misdirected questions and make delegated actions intelligible. It also exposes places where an organization has no clear deciding or provision responsibility.

The account may require qualified interpretation of a policy or relation. That can limit the dependent action. A supported eligibility result can remain useful while a distinct permission question is unresolved.

### ADM.2:10 - Architectural Rationale

The pattern begins with the action because that determines which relations matter. Starting from every relation a person has would make an ordinary service request unnecessarily large. Starting from a job title alone would lose the conditions that justify the action.

General relation and permission instructions remain with their FPF suppliers. The administrative contribution is the use-specific join: whose institutional standing supplies the requested condition, whose decision is needed, and which provider can act on it. That join can remain a readable sentence when the inputs are adequate.

### ADM.2:11 - SoTA-Echoing

The practice question is how to use organizational standing without confusing identity, eligibility, decision authority and provision. The selected line adopts A.6.REL's obtaining-versus-assertion distinction and A.2.8.PER's granted-permission distinctions, and adapts the laboratory's rule-owner, handler and provider separation to the administrative request.

The serious default is to infer entitlement from a directory identity, organizational title or technical account. NIST SP 800-63-4 is a bounded comparator: its identity-proofing, authentication and federation model helps identify what a digital-identity result actually establishes. It does not decide this archive's eligibility or read grant. That comparison changes §§4.1–4.3 and the access case: retain the supplied identity result and obtain only the different relation that remains missing. The extra explicitness is justified when that difference changes the action; adequate combined inputs can still be reused directly.

The May and June laboratory discussions provide failure examples and the specialist/handler distinction. OCE.6 supplies an actual assignment method for its own organizational-change question. Neither a reported incident nor an identity standard proves that a local authority relation obtains; the supplied rule and case facts do that work.

Reconsider how the handler establishes participant standing and authority for the intended action if a different institutional regime changes who can decide, if a grant's beneficiary or scope cannot be resolved by these instructions, or if a simpler available method preserves the same action-changing relations more reliably.

### ADM.2:12 - Relations

ADM.1 supplies the needed administrative condition when the action is unclear. ADM.3 determines the relevant effective time or relation change. ADM.4 handles incompatible or differently organized accounts of the participant or relation.

A.6.REL supplies relation obtaining and conditional occurrence identity. A.2.8.PER supplies the permission distinctions. OCE.6 can supply an adequate effective assignment; SIE.5 supplies identity resolution when sources do not select the participant reliably. The case's existing service instruction uses the resulting facts for its own decision and provision.

### ADM.2:End

## ADM.3 - Determine What Changed and When It Takes Effect

**Type:** Architectural\
**Status:** Stable

### ADM.3:0 - Use this when

Use this pattern when an administrative decision depends on whether an appointment, grant, obligation or other organizational condition has begun, continues, is suspended or has ended. It also applies when a changed record is being treated as a changed relation.

The subject is the particular organizational relation or condition at the time relevant to the action. The first result states what changed, when the change matters and what that permits the handler to conclude. A missing rule or fact remains an explicit question to the person able to resolve it.

If an adequate supplied result already establishes the condition for the intended time, use it. Reconstruct a history only when another date, episode or disputed change can alter the decision.

### ADM.3:1 - Problem frame

An organization can approve an appointment before it takes effect. A directory can be updated before or after that date. A handler can learn about the appointment later still. These moments matter to different claims.

The same issue occurs with payment, delegation, cancellation and suspension. A payment instruction can exist before its effect is known. A corrected amount in a report can change what the organization claims without changing the earlier transfer. Some governing rules, however, make a particular registration or notice part of the act that changes the relation. The handler must recover that rule rather than assume that records are always constitutive or always merely descriptive.

### ADM.3:2 - Problem

How can a handler determine the organizational condition applicable to one action without turning a record date, a later discovery or an intended future change into a present fact?

The wrong time can cause premature access, an incorrect refusal or a claim that a later correction retrospectively supplied missing authority. A useful answer identifies both the relevant state and the next action warranted by the available basis.

### ADM.3:3 - Forces

Current handling needs a quick usable answer. Historical disputes may require a more precise account of what was effective and what participants could then know. A convenient latest record reduces search but can conceal future applicability or a gap between two episodes.

Time detail also has a cost. Dates, time zones and interval boundaries matter only as finely as the receiving decision requires. The governing rule determines the relevant precision; adding timestamps without identifying the changed relation creates false exactness.

### ADM.3:4 - Solution

#### ADM.3:4.1 - Fix the relation and the time of the intended use

State the condition the administrative action depends on. If the relation or participants are unclear, use ADM.2. Name the time being asked about: eligibility for a request on 25 September, a grant during a session, or an outstanding obligation after a particular payment.

Keep the time of the intended action separate from the time at which someone now examines the case. Later evidence may improve a historical account. It does not by itself change which rule or relation applied at the earlier moment.

#### ADM.3:4.2 - Recover what can make the condition change

Use the applicable rule to identify the relevant act or event and its conditions. The rule may make an authorized decision effective on a stated date, require another participant's acceptance, require a registration, or give a cancellation effect only after notice. Obtain the qualified interpretation when that requirement is unresolved.

Recover the actual case facts needed by that rule. An appointment document may be adequate evidence of its stated decision and effective date. A future plan supplies an intended change, not a completed change. An unconfirmed event remains unresolved for any conclusion that depends on it.

A.6.REL supplies the distinction between relation change and assertion or description change. Apply the direct relation's obtaining and continuity conditions; the record's location or revision date does not replace them.

#### ADM.3:4.3 - Separate the relevant times

Distinguish these times when their difference can change the next action:

| Time question | What it identifies |
| --- | --- |
| When did the relevant act or event happen? | The decision, notice, transfer or other occurrence relied on. |
| When does the relation or condition begin, change or end? | The effective boundary under the applicable rule. |
| When was the event observed or learned about? | The evidence or participant knowledge available at that moment. |
| When was the record created or corrected? | The history of the assertion or description used to represent the condition. |

This is a set of different questions, not a requirement to create four database fields. If the same supplied fact answers several of them and no distinction changes the use, say so simply. Where a deadline crosses time zones or a suspension begins within a day, recover the rule's actual time basis before judging the boundary.

#### ADM.3:4.4 - Determine whether the condition holds at the requested time

Apply the rule to the facts for the requested time. State whether the relevant condition holds, does not hold, or remains unresolved on the available basis. A supported negative result settles that condition for the stated participants, basis and time. Do not relabel it as unresolved merely because the requested action cannot proceed on that basis. Conversely, an unresolved claim is not a positive or negative finding about the relation merely because the form requires one status value.

For a later history that must distinguish episodes, use the direct same-versus-new-occurrence rule under A.6.REL. The same person and role can participate again after an earlier appointment ended. A new record alone does not establish another episode; a reused identifier alone does not establish continuity.

When only the description was corrected, update the account and retain the correction history needed for its use. A claimed cancellation, suspension or new grant requires the corresponding governing act and conditions.

#### ADM.3:4.5 - Return the effect on the actual request

Give the handler the conclusion for the relevant action and time, its decisive basis and any remaining condition. A small timeline is useful when the ordering itself explains the answer.

Return the established positive or negative result to the handler, who applies the service rule for the response or case decision it actually requires. If another basis, a disputed interpretation or an exception is a live unresolved question, name that question and the source or authorized person able to resolve it. The negative result alone does not create such a question. Correcting the account and deciding whether any earlier handling needs a remedy are separate tasks; the appropriate policy owner or decision maker supplies a remedy when the applicable conditions call for one.

This inquiry can finish with an established positive or negative result, or a precisely bounded unresolved claim. A later eligibility or transition decision is a distinct result when the actual service or change question requires one.

#### ADM.3:4.6 - What changes in practice

The handler can use a future appointment for the interval it actually covers, preserve a valid relation despite delayed recording, and distinguish a corrected report from a changed institutional condition. The next question concerns the missing rule, event or effective boundary instead of an undirected request for more documents.

### ADM.3:5 - Archetypal Grounding

#### ADM.3:5.1 - An appointment recorded before it is effective

In this constructed case, the supplied appointment rule makes an authorized appointment effective on the date stated in the decision; entry in the directory reports it. The archive's eligibility rule requires an effective appointment. The case supplies these facts:

| Local date | Fact | Consequence for the access question |
| --- | --- | --- |
| 20 September | The competent person makes Mara's appointment decision, stating an effective date of 1 October. | The decision exists; its stated appointment condition concerns the later interval. |
| 22 September | The directory is updated with that appointment and effective date. | The record is available; updating it has not advanced the stated effective date. |
| 25 September | Mara requests access for that day. | The supplied appointment does not satisfy the effective-appointment condition for this date. |
| 1 October | The appointment becomes effective under the supplied rule and facts. | It can supply the appointment condition for a later request within its scope. |

The handler returns: “This appointment begins on 1 October and does not meet the effective-appointment condition for 25 September.” With only the supplied appointment and rule, that negative result completes the temporal inquiry. The handler uses the applicable service instruction for the required response to the request. The appointment's effective date is not an unresolved question, and the temporal result does not itself replace any separately required service decision.

Now add a different fact: Mara claims a second appointment, said to begin on 20 September, but its issuing decision and scope are unavailable. The October appointment's negative result remains established. The handler asks the issuing appointment office to confirm whether the separately claimed appointment covers Mara, the relevant work and 25 September. This request concerns the missing alternative basis; it is not a mandatory further inquiry in the first case.

For a request on 2 October, the appointment condition can be adequate. A separate valid read grant and actual usable access still matter to that action. If both institutional inputs are already supplied and login fails, the provider receives the technical provision problem.

#### ADM.3:5.2 - A late record and a constitutive registration are different cases

Suppose the same appointment rule applies, but the directory is not updated until 3 October. The authorized decision and its 1 October effective date are adequately evidenced. The handler can establish the appointment condition for 2 October and correct the directory's account. The delay in recording does not move the appointment's effective date under this rule.

Now consider a different, explicitly supplied rule for a resource reservation: the reservation becomes effective only when the authorized allocation is entered into the designated registry. The case supplies an approved allocation at 12:00 and the required registration at 13:00, with all other conditions met. Before 13:00 the rule's constitutive condition is incomplete; afterward it is complete. Here registration matters because the rule assigns it that role.

The handler therefore asks what the actual rule makes effective. “The record is missing” alone cannot distinguish absent evidence, incomplete constitution and a reporting defect.

#### ADM.3:5.3 - The same participants after a gap

A history query asks whether Mara was appointed continuously through November. The supplied rule and records establish an appointment ending on 31 October and a later appointment beginning on 1 December. The same person, organization and role do not fill the November gap. The handler retains the separate intervals needed for the historical decision and obtains any different claimed basis for November instead of inferring continuity from the matching name.

### ADM.3:6 - Bias-Annotation

The latest convenient record can dominate the account even when it describes a future state or was corrected late. Conversely, a participant's recollection can be treated as decisive without the applicable rule. Keep both the facts needed to determine the relation and the evidence limits needed to rely on the account.

A retrospective reader has knowledge that the original handler may not have had. Distinguish the relation that applied then from the information available then when judging the earlier action.

### ADM.3:7 - Conformance Checklist

For the requested time, examine whether:

1. The relation or condition and its participants are clear.
2. The applicable rule identifies what makes it begin, change, continue or end.
3. The relevant act or event and its effective boundary are supported or explicitly unresolved.
4. Observation and record times remain separate where they change interpretation.
5. A later correction, repeated name or reused identifier has not supplied an unsupported continuity or historical-authority claim.
6. The return states the consequence for the actual request and identifies any missing result and competent resolver.

The same result can be reused while the relation, time, governing conditions and relied-on facts remain adequate.

### ADM.3:8 - Common Anti-Patterns and How to Avoid Them

**Treating future registration as present eligibility.** A directory shows next month's appointment. Apply the effective date to the intended action.

**Assuming that every record merely reports.** A reservation rule expressly requires entry in a designated registry before the reservation is effective. Inspect that constitutive condition rather than copying an appointment example's different rule.

**Repairing history by overwriting the latest row.** A corrected report makes an earlier decision appear authorized without identifying any valid earlier basis. Preserve the difference between correcting the account and establishing what actually applied.

**Inferring continuity from the same participants.** A later appointment repeats the same person and role after a gap. Apply the relation's episode rule for the history being asked about.

### ADM.3:9 - Consequences

A time-specific answer can prevent premature action and avoid refusing a valid current relation merely because its usual record lags. It makes historical disagreement more precise: a dispute can concern the effective event, the evidence available then or a later description.

The cost is recovering the rule and enough history for the receiving decision. When that basis is missing, a precise unresolved condition is the truthful result. The pattern does not create the authority to change or retrospectively validate the relation.

### ADM.3:10 - Architectural Rationale

The relation and requested time come first because they select which events and records matter. A full chronology would otherwise collect details that cannot change the action. Separate time questions become useful only when their answers differ consequentially.

Using the latest status alone is adequate when it reliably states the condition for the relevant interval and no live contrary fact remains. It is inadequate for future changes, delayed reporting or contested episodes. The additional timeline is a response to those difficulties, not a universal administrative data model.

### ADM.3:11 - SoTA-Echoing

The practice question is how to distinguish an effective organizational change from a change in what participants know or record. The selected line adopts A.6.REL's direct obtaining and continuity rules, and adapts the laboratories' relation/record distinction to administrative applicability.

The serious default is “use the latest row as the current state”. Its advantage is low handling effort. Its defect appears when that row contains a future appointment, when recording lags, or when registration is itself constitutive. Sections 4.2–4.4 and the paired registration cases retain the rule that determines which interpretation applies. The practitioner can still use an adequate latest account directly; a timeline is added only when it resolves an action-changing difference.

The May laboratory's relation/record discussion and the later ADM source pack's effective-condition distinctions supply failure reasoning and synthesis inputs. A.6.REL supplies the general method for relation change and optional occurrence identity. This is a selected practical comparison, not empirical proof that one temporal database design is best.

Reconsider the instruction when a governing relation uses an additional constitutive condition, when repeated episodes cannot be distinguished for the required history, or when a new record arrangement changes what evidence a handler can obtain.

### ADM.3:12 - Relations

ADM.2 supplies the relevant participants and relation when those are not already established. ADM.4 receives a source-account disagreement that remains after the time questions are explicit. ADM.1 supplies the intended administrative condition and deadline when they are unclear.

A.6.REL supplies the relation's obtaining, continuity and conditional occurrence-identity discipline. The qualified policy or relation source supplies the actual constitutive and effective conditions. The existing service instruction receives the result for the requested time; a competent decision maker receives any unresolved eligibility or remedy question.

### ADM.3:End

## ADM.4 - Reconcile Participant-Relative Accounts

**Type:** Architectural\
**Status:** Stable

### ADM.4:0 - Use this when

Use this pattern when participants describe an administrative event or condition differently and that difference affects what someone should do. “We paid”, “we received”, “the account is active” and “the case is closed” can each be correct within one purpose while leaving another participant's question unanswered.

The subject is the administrative event or relation being described, together with the participant accounts needed for the receiving action. The first result is a usable correspondence that preserves each correct meaning, or a precise unresolved claim and its next resolver.

If the records already concern an unambiguous subject and supply adequate compatible facts for the action, use them directly. Reconciling accounts does not require a common database or a redesign of every source schema.

### ADM.4:1 - Problem frame

Several participants can be involved in one transfer, appointment or provision. Each keeps records for its own decisions. A payer records an outgoing payment; a recipient records an incoming receipt. An appointment owner records an effective assignment; a service provider records technical access. The first pair may describe one event differently, while the second pair may describe different related conditions.

A shared label, identifier or screen can conceal that distinction. A useful account identifies the subject, the claim made about it, the participant's position, the relevant time and the action for which the claim is used.

### ADM.4:2 - Problem

How can participants use their accounts together without erasing a correct difference or inventing agreement about an unresolved fact?

Forcing every record into one meaning can remove the creditor's claim or the specialist's qualification. Preserving every wording difference without examining its subject can leave an ordinary administrative action blocked. The practitioner needs a bounded correspondence, not either extreme.

### ADM.4:3 - Forces

A common event account helps coordination and reduces contradictory copying. Local accounts retain purposes, authority and distinctions that the shared representation may omit. The practitioner needs to proceed with an adequate subset of facts while preserving any uncertainty that can change the decision.

The comparison must also separate representation from effect. A consistent set of records does not itself transfer money, grant access or establish a relation. Conversely, different entry times need not mean that participants describe different events.

### ADM.4:4 - Solution

#### ADM.4:4.1 - Start from the receiving action

State what each relevant participant needs to decide or perform. A payer may need to establish whether an obligation is discharged; a recipient may need to allocate a receipt to an invoice. The administrative correspondence serves those actions.

Recover each source statement in its own terms. Ask what the participant means by “paid”: an instruction was issued, a transfer settled, or a particular obligation was discharged under an applicable rule. Retain the author, source, intended use and time when those facts affect interpretation. The exact authority of a source matters to the claim for which it is used.

Do not demand a universal vocabulary before an ordinary action can proceed. If a supplied statement is already clear and adequate, use it.

#### ADM.4:4.2 - Identify the subjects before comparing the claims

Determine whether the statements concern one subject, different subjects, or subjects whose identity remains unresolved. Use the information appropriate to the actual event or relation: participant identities, the relevant action, source reference and its issuer, amount and currency where applicable, effective time and supporting evidence.

A matching local identifier is evidence to interpret within its source scheme. It does not alone prove event identity. Repeated participants can also take part in another event. Use SIE.5 when the cross-source identity question cannot be resolved from adequate supplied facts; SIE.4 and SIE.6 supply the needed alignment and claim-composition methods for a substantive meaning problem.

For a relation history, use ADM.3 and the direct A.6.REL identity rule only as far as the receiving use needs. A different edition of a claim can still describe the same relation.

#### ADM.4:4.3 - Choose the correct comparison result

Distinguish three situations:

| Situation | Result and next move |
| --- | --- |
| Correct participant-relative accounts of one subject | Preserve each account's meaning and state the correspondence needed for the participant actions. An outgoing payment and an incoming receipt can both describe the same transfer. |
| Different or related subjects | State the relation between them and use the appropriate facts for each question. A payment instruction, the resulting transfer and an obligation are different subjects; a label such as “payment” can refer to any of them. |
| Incompatible claims or an unresolved fact about the relevant subject | Preserve the exact claim and uncertainty. Obtain the evidence, qualified interpretation or authorized correction that can resolve it before relying on that disputed conclusion. |

These situations are distinguished by the case facts and meanings, not by a preference for agreement. Several can occur in one case: the parties can identify the same transfer and still disagree about the fee or its effect on an obligation.

#### ADM.4:4.4 - Retain only the correspondence needed for use

State the common subject and how each local account refers to it. Keep the local purpose, participant-relative meaning, effective time and authority or evidence qualification that changes the receiving action. A short joined explanation can be enough.

For the payer/recipient case, retain that A17 calls transfer T a disbursement by P and B82 calls T a receipt by Q. The shared event description can say that 300 moved from P to Q at the evidenced time. P and Q then apply their supplied conditions to their different administrative decisions.

Correct a source record only through the source's appropriate authority and procedure. A useful cross-source explanation does not authorize overwriting a participant's account or silently replacing its rule.

#### ADM.4:4.5 - Return the remaining question and stop

If the correspondence and supplied facts answer the receiving question, let the participant act under the applicable instruction. Record the useful correspondence where that action needs it.

If an amount, time or effect remains unknown, state the exact missing fact and request it from a source or checker able to establish it. If institutional applicability is disputed, return it to the competent decision maker. A technical retry is appropriate only after the state and applicable recovery rule are adequate; a missing settlement confirmation is not a reason to issue a potentially duplicate payment.

The reconciliation can finish with a correspondence plus one bounded unresolved claim. It need not make every source identical or settle questions outside the receiving use.

#### ADM.4:4.6 - What changes in practice

Participants can retain different correct descriptions and still coordinate. A handler can also distinguish a meaning problem from an unknown effect, a wrong identity or a rule question and request the right next result. Consistent wording becomes a means of understanding the event, rather than a substitute for establishing it.

### ADM.4:5 - Archetypal Grounding

#### ADM.4:5.1 - One transfer, two correct administrative accounts

In this constructed case, organization P makes one authorized transfer T of 300 currency units to hotel Q for invoice I. The case supplies bank evidence that the full amount was credited to Q at 13:00 on 10 September, with no fee deducted. The supplied invoice terms make the full 300 credit to this destination discharge P's 300 obligation. Q's supplied allocation rule applies a matching identified receipt to I. These conditions, including the authority for the payment and record actions, are inputs to the example.

P enters record A17 at 13:05 and calls T an outgoing payment or disbursement. Q enters B82 at 15:20 and calls T an incoming payment or receipt. The local record-entry events differ. Both records describe the same settled transfer at 13:00.

The handler establishes the correspondence using the bank reference with its issuer, the payer and recipient, destination, amount, currency, effective time and settlement evidence. The result is:

| Account retained | Correspondence | Action it supports |
| --- | --- | --- |
| P's A17: disbursement of 300 to Q for I | A17 describes transfer T from the payer's position. | P's responsible handler records the outgoing payment and, under the supplied invoice conditions, records the 300 obligation as discharged. |
| Q's B82: receipt of 300 from P for I | B82 describes T from the recipient's position. | Q's responsible handler allocates the receipt to I and updates the outstanding receivable under Q's supplied conditions. |

Both descriptions survive because their different directions are correct relative to different participants. The common event description supplies neither spending authority nor the rule for discharge or allocation; those are explicit inputs in this case. The participants can use this correspondence without replacing their ledgers or local record identifiers.

#### ADM.4:5.2 - The amount differs

Now suppose P's account concerns 300 and Q reports a credit of 290. The handler first asks what each amount measures. A fee, a gross-versus-net distinction, another transfer or a genuinely incorrect claim could change the answer.

If evidence establishes a 300 gross transfer and a 10 fee, those quantities can be compatible descriptions. Whether the payer's obligation is discharged still depends on the applicable payment conditions. If the evidence is unavailable, the handler preserves the unresolved credit or fee claim and obtains the needed source result. Neither a shared reference nor a familiar payment status settles it.

#### ADM.4:5.3 - The same label names different subjects

A traveller says “the trip was unsuccessful”; the travel desk says “the trip is complete”. The traveller means the negotiations produced no agreement. The desk means the travel conditions were supplied and the expense handling completed. ADM.1 separates those subjects and their connection. Treating them as two conflicting measurements of one result would send the next action to the wrong person.

In another case, two records both show “reference 17”, but the numbers belong to different issuing systems. The handler cannot combine them until identity is established. The shared numeral is insufficient correspondence.

### ADM.4:6 - Bias-Annotation

A common representation often adopts the vocabulary of the party that owns the tool. That party's purpose and authority can then appear universal. Ask whose decision each claim supports and which local qualification would be lost by the proposed common wording.

Access can also be asymmetric. One participant may have settlement evidence that another cannot inspect. Preserve the resulting reliance limit and request an adequate permitted source return; apparent silence or lack of access is not itself proof that the event failed.

### ADM.4:7 - Conformance Checklist

For the receiving administrative use, examine whether:

1. The participant actions and the subjects of the source statements are identifiable.
2. A claimed common identity is supported beyond an ambiguous shared label or reference.
3. The comparison distinguishes compatible participant-relative meanings, different subjects and incompatible or unresolved claims.
4. Relevant quantities, times, source meanings and institutional qualifications survive the correspondence.
5. Each participant can identify what the result supports and what it leaves unresolved.
6. A needed correction, evidence request or qualified decision reaches the appropriate source or responsible person.

These questions assess the usable correspondence. A separate claim that an obligation was discharged or an action was permitted still uses its governing conditions.

### ADM.4:8 - Common Anti-Patterns and How to Avoid Them

**Forcing correct directions to agree.** A common ledger replaces both “disbursement” and “receipt” with one participant's term. Preserve the common transfer and each participant's relation to it.

**Making the identifier do every job.** A matching reference is used as proof of identity, amount, settlement and authority. Establish the correspondence, then retain the separate facts each conclusion requires.

**Resolving missing effect by copying a status.** A payer's “sent” field is copied as “received” in another account. Obtain evidence of the relevant effect and preserve uncertainty until that evidence or the applicable recovery decision is adequate.

**Reconciling different subjects as contradictory views.** Negotiating work and travel administration are treated as one result. Identify their subjects and use the appropriate next action for each.

### ADM.4:9 - Consequences

A bounded correspondence can make participant accounts jointly usable while retaining their correct differences. It can reduce unnecessary schema redesign and make the unresolved question easier to route.

The result may remain partial because some meaning, evidence or institutional condition is unavailable. That limitation is useful when it isolates the exact conclusion that cannot yet be relied on. It does not require withholding every independently supported fact.

### ADM.4:10 - Architectural Rationale

The receiving action comes first because it determines which correspondence matters. Subject identity precedes comparison of participant meanings because a viewpoint label cannot establish that two statements concern the same thing. Institutional consequence follows separately because a common event description cannot determine a rule it does not contain.

The serious alternatives are full normalization into one account and leaving every source separate. Normalization can be economical when meanings and authority already match. It loses useful content when participant-relative meanings or decision conditions differ. Separate sources can remain adequate when one action needs only one account; a bounded correspondence is worthwhile when the participants must act together.

### ADM.4:11 - SoTA-Echoing

The practice question is how to preserve correct participant-relative accounts while producing an administrative result the parties can use. The selected line adopts SIE.4–6 for real alignment, identity and claim-composition work, and adapts the Partridge accounting and agentology comparison after the administrative subject is established.

The serious rival is one normalized representation whose terminology replaces all local accounts. The Partridge papers distinguish organizing an account around a participant from describing the common represented event, and separately examine how direction is represented. That contribution changes §§4.2–4.4 and the payer/recipient case: establish the common event, retain how each participant describes it, and keep the next institutional action under its supplied rule. The full BORO ontology and one-database infrastructure are not selected for this bounded result.

Thoroughly Modern Accounting, especially PDF pp. 9–10 and 13–14, and Ontology then Agentology, PDF pp. 5–8, supply conceptual arguments and worked representations. They do not establish the facts of a particular transfer or empirical superiority in every administrative setting. The July laboratory and later source pack supply the distinction between different subjects and different accounts of one subject. Both contributions are needed to avoid treating every disagreement as a viewpoint difference.

At comparable handling effort, a small explicit correspondence retains action-changing meaning without a full schema merger. Maintaining it has a cost when source meanings change. Reconsider the selected correspondence when a new participant, source scheme, quantity, effective-time rule or institutional decision makes the retained distinctions insufficient, or when an existing integrated account already supplies them adequately.

### ADM.4:12 - Relations

ADM.1 separates the enabled work and administrative result when a broad label hides different subjects. ADM.2 supplies participant standing and authority; ADM.3 supplies effective conditions and relation history. Use their results only when the receiving comparison needs them.

SIE.4–6 supply alignment, identity and claim composition for unresolved semantic integration. OPS.4 supplies usable current claims for ongoing handling. A.6.REL governs a relation occurrence and its distinction from revised descriptions when that history matters.

The responsible handler uses the correspondence with the applicable service or specialist instruction. In the transfer case, P's handler applies the supplied obligation-discharge condition and Q's handler applies the receipt-allocation rule. If a payment or other provision is still needed, the assigned and authorized provider follows the applicable instruction for that action. The provider performs it only when that instruction's prerequisites are met. The handler sends an unresolved substantive question to the specialist or decision maker competent to answer it.

### ADM.4:End

# Part B - Design the Repeated Case, Resolve Exceptions and Supply the Result

## ADM.5 - Design the Reusable Administrative Case

**Type:** Architectural

**Status:** Stable

### ADM.5:0 - Use this when

Use this pattern when a service owner has an administrative result to supply repeatedly and the applicable policy, but handlers lack a usable instruction for receiving, checking, deciding, providing and closing individual requests. A new reimbursement service, for example, needs more than a form and a list of approvers.

The first useful result is an instruction that a handler and the relevant specialists can apply to an ordinary request, including the action to take when a needed condition fails. Start with one representative request and the condition promised to its recipient. Follow it far enough to identify the decision, actual provision and evidence of completion.

Use an adequate existing instruction directly. This pattern is unnecessary for each later request and does not itself approve a request, appoint a provider or authorize an exception. A missing substantive policy belongs to the person competent to supply it; a form designer cannot fill that gap by choosing convenient fields.

### ADM.5:1 - Problem frame

The designer is working on how a class of administrative requests will be handled. The enabled work and requested condition are already sufficiently clear, or ADM.1 can establish them. The supplied policy determines such matters as eligibility, permitted amounts, deciding authority and any mandatory evidence. Actual service participants supply the remaining operational constraints.

The reusable instruction and an individual case have different results. The instruction describes what the handler, decision maker and provider do under stated conditions. In a particular case, those people apply it to actual facts, make any required decision and perform the provision. A completed design cannot establish that any claimant has received a result.

The relevant scope may be small: reimbursing one category of travel expense for one employee population. Add a variant only when it changes the needed input, authority, action or result. A single instruction need not absorb every service that happens to share a portal.

### ADM.5:2 - Problem

A service often begins with an application form. Each department adds fields and approvals, yet nobody establishes how the approved request produces a usable result. Handlers then improvise missing evidence rules; applicants repeat information; providers close requests after issuing instructions whose effects remain unknown.

The opposite response leaves all handling discretionary. Skilled staff may resolve familiar cases, but a new handler cannot tell which decisions are already settled by policy, which require a qualified person and which information is actually needed.

### ADM.5:3 - Forces

| Force | Tension |
| --- | --- |
| Repeatability | An instruction should support consistent handling while retaining legitimate variations and exception conditions. |
| Minimum burden | Reuse known facts and decisions while obtaining the evidence the actual decision needs. |
| Institutional authority | A designer can describe a decision and its recipient without possessing the authority to make or delegate it. |
| Usable completion | A provider's intermediate activity is easy to record; the promised effect may require a different observation. |
| Practical size | One short instruction can be sufficient, while a diagram that omits refusal, uncertainty or recovery is incomplete for those cases. |

### ADM.5:4 - Solution

#### ADM.5:4.1 - Fix the supported result and governing inputs

Name the condition to be supplied, its recipient, applicable time and supported request class. Recover the actual policy and the people authorized to decide, perform and correct the relevant actions. Distinguish a supplied rule from an assumption that still needs its competent source.

Keep the work enabled separate. A travel reimbursement service supplies an authorized reimbursement; it does not determine whether the traveller's negotiations succeeded. If the policy makes a particular business condition relevant, include that condition and the person or evidence that can establish it.

An unavailable policy, unassigned payment provider or missing qualified test is a design gap. State the exact missing contribution and who can supply it before promising the affected result.

#### ADM.5:4.2 - Work backwards to the minimum request

For each action-changing condition, identify the fact, evidence or existing result that the handler needs. Reuse a sufficiently current assignment, permission or prior check within its actual scope. Ask the applicant only for information that cannot adequately be recovered and that matters to handling.

Specify how the handler relates the evidence to the actual claimant and request. A receipt must concern this expense; an assignment must cover the relevant person and time. “Upload documents” leaves these questions unanswered. ADM.7 supplies the case check when the correspondence or support is disputed.

Specify where the request enters, how the applicant can correct an ordinary omission, and what the handler returns when the request is outside the supported class. Collect and expose personal information only for the stated handling need under the applicable information rules.

#### ADM.5:4.3 - Identify the actual decisions and actions

For each consequential branch, name who applies the rule or makes the decision, the conditions used, and what the next participant receives. A direct policy rule may already determine the required response. A case-specific approval remains a decision when the policy requires an authorized person to make it.

Keep the handler's preparation, a specialist's judgment, the competent person's authorization and the provider's performance distinct. Completing a checklist neither transfers approval authority nor performs payment. ADM.8 resolves a permission question; OPS.5–6 can supply admission or situated continuation when actual handling needs one.

State which independent action may proceed while another condition is pending. An instruction for obtaining a price quote need not inherit the spending authorization required for a later booking unless the applicable rule makes that authorization a condition of the inquiry.

#### ADM.5:4.4 - Connect authorization to provision and completion

Identify the provider who will perform the authorized action and the input that provider needs. Define completion from the recipient's promised use: access that works under the grant, accommodation that can be occupied, or funds credited under the applicable payment terms.

Choose evidence adequate for that effect. An issued instruction may establish that the provider was asked to act; it may leave performance unknown. ADM.9 supplies the needed provision and recovery inquiry. ADM.10 reconciles a discrepancy among the obligation, performance and records.

Specify the record returned to each participant: the relevant decision, actual result, effective conditions and any unresolved next action. Use an existing case record where it suffices. Participants need enough correspondence to recover the same case; they need not adopt one universal description of every event.

#### ADM.5:4.5 - Describe ordinary correction and genuine exceptions

Give the handler the existing response for a correctable omission or an established negative condition. A missing receipt may receive the policy's correction request. A clearly excluded expense may receive its reasoned refusal and applicable challenge route. Neither outcome requires inventing another discretionary decision.

Use ADM.6 when an actual gap prevents ordinary handling: conflicting facts, an inapplicable rule, unresolved authority, incompatible requirements or provision whose effect cannot be established. Name the competent destination and the bounded question. A transfer to “support” without anyone assigned to resolve it is still a gap.

For potentially duplicate actions, include recovery of the earlier attempt before repetition. The instruction should state what remains permitted while the uncertain effect is investigated, rather than calling the entire service complete or restarting it blindly.

#### ADM.5:4.6 - Exercise and publish the usable instruction

Walk through a representative supported request with its prospective handler, deciding person, provider and result consumer. Add variations that exercise the actual branches: a correctable omission, a decisive negative condition, an authority gap and an uncertain provider effect.

Ask each participant to recover their next action from the instruction. Repair missing joins and unnecessary requests. A desk walkthrough establishes that the described handling is intelligible under the supplied facts; a trial of actual provision is needed to establish that the provider can deliver the promised condition.

Return the instruction with its supported class, applicable policy, effective conditions and known gaps. Use the organization's existing place for such instructions. The first real request then uses the applicable instruction; it does not reopen the design without a changed condition or observed defect.

### ADM.5:5 - Archetypal Grounding

#### ADM.5:5.1 - A reimbursement instruction

Suppose policy P permits reimbursement of documented business-travel expenses up to 500 units for employees with an effective relevant assignment. P requires a named finance approver's case decision; treasury is authorized to pay approved claims. The payment terms define the promised effect as the approved amount credited to the claimant's designated account. These are supplied conditions for this example, not universal reimbursement rules.

The service owner and participants develop this instruction:

| Question | Instruction for the supported class |
| --- | --- |
| What enters? | Receive the claimant's identity, expense, amount, business purpose, receipt and relevant assignment reference. Recover adequate information already held. |
| What is checked? | The handler establishes claimant/assignment/expense correspondence, the applicable category and amount, and whether this expense has already been reimbursed. A disputed claim uses ADM.7. |
| What ordinary correction applies? | Return a missing receipt for the correction P allows. Apply P's response to an established excluded category, including the available challenge route. |
| Who decides? | The finance approver applies P and makes the required decision for the exact claim and amount. The handler's completed preparation supplies input to that person. |
| Who performs? | Treasury receives the approved claim and the account information through the authorized channel, then issues the permitted payment. |
| When is provision complete? | Adequate provider evidence establishes the approved credit to the intended account. An instruction acknowledgement alone leaves the effect to be established. |
| What is returned? | The claimant receives the decision and actual provision result or precise remaining condition. Finance and treasury retain the corresponding evidence needed for their duties. |
| What requires resolution? | Conflicting assignment evidence, unclear approving authority or an unknown earlier payment effect goes to its competent resolver through ADM.6. Recover the earlier effect before a possible duplicate payment. |

Later an employee claims 200 units. The supplied assignment and receipt support eligibility, and adequate records establish no earlier reimbursement. The handler prepares the case, the finance approver approves it, and treasury performs payment. Evidence of the credit supports completion and the returned record. The existing instruction has been enacted; it has not been redesigned.

#### ADM.5:5.2 - A variant outside the supplied policy

A contractor submits an otherwise identical receipt. P covers employees, and no contractor rule is supplied. The handler follows the instruction's outside-scope response and identifies the missing contractor-policy question to its competent source. The service owner cannot extend P by adding a contractor checkbox. If another applicable instruction already covers contractors, the request can use it.

### ADM.5:6 - Bias-Annotation

Designers tend to optimize the fields and handoffs they can see, while applicants bear repeated entry, waiting and inaccessible channels. Exercise the instruction from the recipient's attempt to obtain the condition as well as from each provider's task.

The example assumes an explicit policy and identifiable decision makers. An informal service may use a short agreed instruction, but informality does not create missing authority. The pattern also assumes that the substantive policy is supplied; it offers no independent judgment that the policy is lawful or desirable.

### ADM.5:7 - Conformance Checklist

**Recognition.** The result is a reusable instruction for a bounded class. It connects entry and evidence to actual deciding and performing participants, a usable completion condition, the returned account and meaningful failure branches.

**Assurance for reliance.** Trace a supported request and a relevant failing variation. Can the participants recover their own next action without inventing authority, supplying a needless fact or mistaking an intermediate acknowledgement for completion? Check any consequential dependency against its actual policy, source or provider capability. Describe a walkthrough and an operational trial according to what each establishes.

### ADM.5:8 - Common Anti-Patterns and How to Avoid Them

A **form presented as a service** specifies inputs but leaves the decision and actual provision unassigned. Follow one request through to the recipient's usable condition.

**Design on every request** repeats the architecture inquiry despite an adequate instruction. Apply the existing instruction; reopen only the defective or changed condition.

**Every refusal becomes an escalation** sends settled cases to another decider. Retain the policy's ordinary response and challenge route; reserve exception resolution for the actual unresolved question.

### ADM.5:9 - Consequences

Handlers can begin ordinary cases with less improvisation, while specialists receive specific questions and providers receive actionable decisions. Applicants can distinguish a correction request, a reasoned refusal and unfinished provision.

Design costs become visible: someone must obtain missing policy, test correspondence and agree how to observe completion. More detailed documentation is useful only while it changes handling. The instruction's successful construction does not establish service effectiveness; that requires evidence from actual cases and participants.

### ADM.5:10 - Architectural Rationale

The reusable object is the handling instruction. Authority remains with the actual participants, and successful provision remains an effect of their work. Keeping these distinct lets the service reuse its design without treating a model, approval or record as the beneficiary's result.

Conditional connections are sufficient. A settled case need not visit every specialist; an uncertain effect does need its qualified recovery. This preserves both efficient ordinary handling and accountable exceptional handling.

### ADM.5:11 - SoTA-Echoing

The working question is how to make an administrative service repeatable while keeping institutional decisions and actual provision connected. The June laboratory and ADM source pack distinguish developing a service from using it. Part of this question is how the service supports the participant's intended work and what effort it requires from them. The laboratory material supplies reported situations; assess service effectiveness from its actual use.

The selected synthesis uses the actual [OPS.5–6][OPS] instructions for admission and continuation during handling, with ADM's explicit evidence, authority and usable-result joins. [CMMN 1.1][CMMN], §§4.1–4.3, supplies a serious case-model alternative: work toward an outcome can use evolving information and discretionary planning. Its model does not supply the local eligibility policy, appoint the decider or establish real provision.

An adequate existing service instruction is the strongest low-cost alternative and should be used directly. A process diagram or case model is also sufficient when it already carries the needed conditions and returns. Sections 4.2–4.5 become necessary where the representation omits those joins; no particular notation or CMMN conformance is required.

Reopen the affected design when policy, supported population, deciding authority, provider capability or a demonstrated handling failure changes it. A new form or software feature alone is not a new administrative result.

### ADM.5:12 - Relations

ADM.1 supplies the condition the service enables; ADM.2–3 supply participants and effective relations when those are unsettled. The handler uses ADM.7 for a needed claim check, ADM.8 for permission, ADM.9 for usable provision and ADM.10 for reconciliation. A genuine obstacle returns through ADM.6 to the person able to resolve it.

[OPS.5–6][OPS] supply decisions during actual handling. [SYSE.26][SYSE] supplies the design of a supported interaction and its failure recovery when that engineering question is live. Neither return is a mandatory preliminary to using an adequate administrative instruction.

### ADM.5:End

## ADM.6 - Resolve an Administrative Exception

**Type:** Architectural

**Status:** Stable

### ADM.6:0 - Use this when

Use this pattern when a real obstacle prevents the applicable administrative instruction from producing its ordinary result: a needed fact is disputed, the rule does not cover the case, requirements conflict, authority is unresolved or provision has failed in a way the ordinary recovery cannot resolve.

The first useful move is to state the exact condition preventing the next action and identify the person or source able to resolve it. The result is a resolved condition and usable continuation, or a reasoned disposition with the applicable correction or challenge route. A request for resolution is an intermediate result when the answer is still unavailable.

Apply a sufficient existing rule or recovery instruction directly. An ordinary missing-field correction or a negative condition already settled by policy is not automatically an exception. This pattern grants no authority to waive a requirement, invent evidence or extend a permission.

### ADM.6:1 - Problem frame

A handler is working on a particular request for an administrative condition. The relevant action, participant and intended time are known well enough to locate what is blocked. The handler may have a service instruction, prior decisions and evidence from the provider.

The obstacle belongs to a particular question. A missing identity result, an unresolved eligibility rule, an unavailable authorized decider and an unknown payment effect call for different work. They can occur in one case without becoming interchangeable reasons to “escalate”.

Resolution also has several possible stopping points. Finding the competent source creates an actionable request; receiving its answer may settle the condition; an authorized provider must still perform any resulting provision. The handler states which result is actually available.

### ADM.6:2 - Problem

An opaque refusal leaves the participant unable to correct the case. Repeated transfers between departments can move the request without moving the unresolved question. A handler may compensate by improvising a waiver, treating technical access as permission, or repeating a payment whose earlier effect remains unknown.

At the other extreme, every negative answer is sent to a discretionary decision maker. This delays cases whose governing rule already supplies the response and obscures the genuinely unresolved alternatives that do need judgment.

### ADM.6:3 - Forces

| Force | Tension |
| --- | --- |
| Continuity | The participant needs a next move, while some missing results require qualified work that the handler cannot perform. |
| Competence | A reachable person is useful only if they can supply the needed fact, interpretation, decision or provision. |
| Direct resolution | A matching rule or prior result may settle the question without a new choice. |
| Legitimate alternatives | A permitted alternative can restore use; convenience cannot create permission to bypass a restriction. |
| Accurate progress | A sent request, received decision and usable effect must remain distinguishable. |

### ADM.6:4 - Solution

#### ADM.6:4.1 - Recover the blocked action and the actual obstacle

State the intended action, its participant, applicable time and the condition that is not established. Use the existing case facts; reopen ADM.1–3 only when the requested result, relevant relation or effective time is itself unclear.

Separate what is known from what is missing. “No appointment is effective on this date under the supplied decision” is an established result. “An earlier appointment is claimed but its decision cannot be recovered” is a separate unresolved basis. A provider's failure message may establish that a login attempt failed while leaving institutional permission intact.

If the applicable rule already determines the response, apply it. A policy-defined refusal can finish that bounded inquiry and still expose the available correction or challenge route. The existence of that route does not make a challenge mandatory.

#### ADM.6:4.2 - Identify the smallest resolution task

Locate the missing contribution before choosing a recipient.

| Actual obstacle | Needed contribution |
| --- | --- |
| A material claim is unsupported or disputed | Evidence or a competent check of that exact claim; ADM.7 helps specify it. |
| The rule's application or scope is unresolved | Interpretation from the source or person authorized to settle that question. |
| Requirements yield incompatible conclusions | A matching precedence rule or adequate resolving decision; ADM.8 keeps the permission question bounded. |
| A required authority is absent or unclear | A decision or assignment by the person permitted to provide it, if the governing arrangement allows one. |
| Authorized provision failed or its effect is unknown | Investigation and recovery by the provider able to establish or change that effect; ADM.9 applies. |

A named department is not yet a resolution mechanism. Identify an actual receiving function or person and the result they can supply. If no such assignment exists, return that gap to the person authorized to arrange it. Do not fabricate a specialist answer to keep the case moving.

#### ADM.6:4.3 - Reuse what already resolves the question

First apply a matching rule, adequate evidence or existing authorized decision within its conditions. Confirm the relevant subject, scope and time; a nearby case's answer may concern a different person or action.

When more than one legitimate continuation remains, use the applicable decision method to select among them. [OPS.6][OPS] supplies the situated continuation: direct rule or recognition first, a real choice only when alternatives remain, and a bounded probe only if its answer can change the action.

An authorized exception can permit a bounded action under its actual conditions. It does not make a failed factual claim true. Record or communicate the condition that was waived or varied separately from the evidence that remains absent or negative.

#### ADM.6:4.4 - Send an answerable question and preserve permitted work

Give the resolver the question, relevant facts, actual conflict or gap, intended use of the answer, and any time condition that changes its usefulness. Use existing evidence references and protect information according to the applicable rules. Avoid forwarding an entire personal file when a narrower account suffices.

State who will consume the result and perform the next action. Obtain a usable return arrangement through the existing service channel; do not assume that sending a message appointed the recipient or established a response commitment.

Continue independent permitted work when its own prerequisites hold. A spending-approval question can block booking while a permitted price inquiry proceeds. An unresolved earlier payment effect blocks a potentially duplicate payment, but may leave an evidence inquiry fully permitted.

#### ADM.6:4.5 - Apply the actual answer or issue the reasoned disposition

On return, check that the answer concerns this subject, action, scope and time. Apply a settled condition under the service instruction. A new authorization supplies a permission result; the provider still needs to perform the authorized provision.

For a refusal, explain the action-changing reason and the correction, alternative or challenge route that the applicable arrangement actually provides. A competent refusal may be the correct case disposition while the requested condition remains unprovided. Do not report the beneficiary's service as supplied merely because the administrative inquiry ended.

If the answer or effect is still unavailable, preserve the specific uncertainty, the responsible next action and any applicable time or stop condition. The useful completed result may be an actionable resolution request, with the dependent provision still unfinished.

### ADM.6:5 - Archetypal Grounding

#### ADM.6:5.1 - A valid read grant and a failed identity route

A visiting researcher has an effective appointment and a valid archive read grant for 2 October. The supplied access policy additionally requires an accepted identity result for the person using the service. The portal's device credential succeeds, but its identity service cannot complete the required person check.

The handler establishes three facts: the grant is valid, the requested use is within it, and the person-check result is unavailable. The device result cannot answer the missing person question. The handler has no authority to remove that requirement.

The supplied support instruction permits the identity support officer to perform a qualified attended check through a protected channel. The handler sends that officer the specific failed attempt and needed identity question. This is a resolution request; the researcher does not yet have usable archive access.

The officer performs the prescribed check and returns an accepted result for this person and attempt. The archive provider then completes the authorized access setup. The researcher successfully opens the permitted archive material, supplying evidence of usable provision through ADM.9. These are three distinct results: the check, its use in handling, and access that actually works.

If the attended route is unavailable too, the handler reports the unavailable check and the existing support or challenge route. The valid grant is preserved; it does not supply missing identity evidence. A different service that does not depend on that check may proceed under its own conditions.

#### ADM.6:5.2 - A settled negative and a genuine alternative basis

A request for 25 September cites only an appointment effective on 1 October. The service rule requires an effective appointment at use and prescribes a response explaining the failed condition. ADM.3 supplies the negative temporal result; the handler issues that response. No further eligibility decision is needed for the supplied appointment.

The requester then identifies a different appointment said to begin on 1 September, but the relevant decision and scope are unavailable. The new question goes to its issuing office: does that appointment cover this person, work and requested date? If an adequate existing decision is recovered, use it. If it is not recovered, preserve the gap. The later descriptive record of a valid September appointment would not itself make that appointment begin later.

### ADM.6:6 - Bias-Annotation

Handlers often classify an unusual participant as an invalid request or assume that every exception deserves special permission. First distinguish a valid unsupported case, a settled negative condition and a genuine uncertainty.

A digital route can conceal barriers experienced by people who cannot use that channel. The pattern requires an actual permitted support or redress arrangement when one is supplied; it does not presume universal availability or let the handler invent it.

### ADM.6:7 - Conformance Checklist

**Recognition.** The handler can name the blocked action, exact obstacle, needed contribution and competent destination. A settled result is applied; an unresolved question remains explicit.

**Assurance for reliance.** Trace the actual response back to its authority or evidence and forward to the next action. Verify that an alternative preserves the relevant conditions, that independent permitted work is not blocked by association, and that a request for resolution has not been reported as the received answer or completed provision.

### ADM.6:8 - Common Anti-Patterns and How to Avoid Them

**Escalation by forwarding** moves the case but supplies no question or capable recipient. Identify the smallest missing contribution and who can return it.

**A negative answer treated as uncertainty** repeats a decision already supplied by the rule. Apply its ordinary response; investigate only a separately live alternative or challenge.

**An exception that rewrites the facts** describes absent evidence as a passed check. Keep the authorized variation and the unresolved or negative fact distinct.

### ADM.6:9 - Consequences

Participants receive an intelligible next action instead of an unexplained transfer. Handlers can use existing rules and answers more quickly while reserving specialist attention for unresolved questions.

Some cases remain blocked because the competent contribution is unavailable. Making that condition explicit is useful, but it does not provide the requested service. Evidence from actual handling is needed to establish whether resolution reduces delay or displaced effort.

### ADM.6:10 - Architectural Rationale

The unit of resolution is the action-changing question. That unit connects the case to the source or participant able to answer it without making the handler a universal authority. Separating the answer from its later execution preserves accountability when several people contribute to one administrative result.

### ADM.6:11 - SoTA-Echoing

The working question is how to restore legitimate continuation when ordinary administrative handling cannot supply its result. The May and June laboratories expose opaque refusal, specialist judgment and execution gaps. The selected method joins those domain distinctions to the actual direct-rule, recognition and continuation instructions in [OPS.6][OPS].

[NIST SP 800-63-4][NIST]'s redress treatment supplies a bounded comparison for digital-identity failures: accessible issue handling, review, correction and human support. It does not determine a local appointment or entitlement. That limit shapes §§4.2 and 5.1: a qualified identity result is requested from its proper source and then used by the service.

[CMMN 1.1][CMMN] provides a serious alternative for adaptive case planning. Its information and discretionary-work constructs can carry the handling arrangement, but do not by themselves settle institutional authority. An adequate ordinary instruction is the cheaper alternative and remains sufficient when it already resolves the condition.

Reopen the affected instruction when repeated exceptions reveal a missing ordinary branch, an unavailable competent provider or a changed governing rule. Repetition alone does not justify waiving the condition.

### ADM.6:12 - Relations

ADM.1–3 establish the needed condition and relevant effective relations when those are unclear. ADM.7 specifies the needed factual check; ADM.8 resolves permission within the applicable rule. The handler uses the returned result in continuing the case, while the authorized provider performs provision under ADM.9. ADM.10 supplies reconciliation when an obligation or recorded effect remains disputed.

ADM.5 is used when the recurring instruction itself needs repair. [OPS.6][OPS] supplies a current continuation decision without requiring redesign of that instruction for every exception.

### ADM.6:End

## ADM.7 - Check the Claim Needed for This Decision

**Type:** Architectural

**Status:** Stable

### ADM.7:0 - Use this when

Use this pattern when an administrative action depends on a particular claim and the handler needs to establish whether available evidence adequately supports that claim for this use. Examples include an effective assignment, an expense's eligibility, the identity of the person requesting access or the effect of an earlier payment.

Start by writing the claim and the action that depends on it. The first useful result is a supported answer, a supported negative answer, or the exact missing evidence or competent check. Reuse a sufficient existing result within its conditions.

Do not run an additional check merely because a form has a field for it. A settled decision whose applicable rule requires no further check can use its established basis. This pattern applies an existing qualified check to a case; redesigning a control or inventing a specialist test is a separate task.

### ADM.7:1 - Problem frame

A handler, deciding person or provider is about to rely on a claim. The claim concerns an identified participant, event, relation, amount or condition at a relevant time. The governing service rule supplies the criterion where one is needed.

A check can establish different things: that a document came from its stated issuer, that a receipt concerns this expense, that a condition holds under a policy, or that a provider effect occurred. A successful check of one thing cannot silently answer another. An authentic assignment record can describe a future appointment; a successful credential operation can leave the person's eligibility unestablished.

The handler specifies and uses the needed result. The person or mechanism competent to perform the check supplies its evidence or judgment. Administrative responsibility for the case does not confer every specialist competence.

### ADM.7:2 - Problem

Administrative checks often follow available documents instead of the decision. Staff confirm that a file exists, a signature is valid or an automated service returned green, then treat that observation as proof of entitlement or completion.

Repeating all checks can also be harmful. It imposes burden without improving the answer, particularly when an adequate result already exists or when the checked fact cannot change the decision. Meanwhile, a consequential missing claim can remain hidden behind several successful but irrelevant checks.

### ADM.7:3 - Forces

| Force | Tension |
| --- | --- |
| Claim precision | A broad label such as “verified” is convenient but conceals what was actually established. |
| Proportionate effort | A wrong answer can matter greatly, while unnecessary checking delays legitimate work and collects avoidable information. |
| Reuse | A prior result may remain adequate, or may concern a different subject, rule, condition or time. |
| Competence | A general evidence account can expose a gap without supplying the qualified domain test. |
| Distinct outcomes | False, unsupported, inapplicable and unavailable can require different next actions. |

### ADM.7:4 - Solution

#### ADM.7:4.1 - State the claim and receiving action

Specify what needs to be true, for whom or what, under which relevant rule and time, and which action depends on the answer. Split a compound claim only when its components need different sources or can lead to different actions.

Ask what a wrong positive or negative answer would change. That consequence helps identify the applicable evidence requirement and any needed specialist contribution; it does not authorize the handler to invent a numerical confidence threshold.

For example, proving that a claimant has an effective assignment does not prove that a particular expense falls under it. Checking the expense's category does not establish that it has not already been reimbursed. Select only the claims actually required for the receiving action.

#### ADM.7:4.2 - Match available evidence to the claim

Recover an existing result before commissioning another check. Identify the actual subject, source, criterion, relevant time and stated limitations. Establish enough correspondence to know that the result concerns this person, expense, grant or provider attempt.

Distinguish the source's identity from the truth of its content. A signed record can support an origin claim while leaving scope, effective date or substantive correctness disputed. [A.10][A10] supplies source recovery and bounded reliance when that account needs to remain inspectable; it does not perform the domain check.

Use ADM.3 for a live effective-time question and ADM.4 when participant accounts or cross-source identity prevent the match. Do not build a larger evidence record when the ordinary source and its conditions already answer the question.

#### ADM.7:4.3 - Reuse the result or perform the smallest competent check

Reuse a result while its subject, criterion and action-changing conditions match the current use. Name the specific change that would defeat reuse: a different person, a revised policy, a revoked grant, an altered subject or a later time outside the result's scope.

When evidence is insufficient, select the qualified procedure or competent person that can answer the remaining question. A records custodian may recover a decision; the authorized specialist may interpret a rule; the payment provider may establish an attempt's effect. A new generic document request cannot replace any of these.

If a domain method is missing, return that method gap through ADM.6. If a separately required assurance claim is current, [B.3][B3] supplies the argument about that exact claim and use. Consequence alone does not require constructing such an assurance claim.

#### ADM.7:4.4 - Preserve each action-changing outcome

Return the substantive result in ordinary language and retain distinctions the next action needs.

| Outcome | Meaning and continuation |
| --- | --- |
| The claim is supported for the stated use | The deciding person or handler may use that result under the applicable rule; the check itself does not grant permission or perform provision. |
| Evidence supports the negative condition | Apply the service rule's response to that established negative result. |
| The evidence is insufficient or conflicting | Preserve the unresolved claim and request the particular additional evidence or judgment needed. |
| The chosen check is inapplicable | Choose the check that actually answers the claim, or return the missing method; an irrelevant test supplies no positive or negative answer. |
| The check cannot currently be performed | Use an adequate existing result or separately permitted alternative if available; otherwise report the unavailable check and dependent action. |

An unavailable mechanism is a fact about checking, not a negative answer about the claimant. A policy may prescribe refusal or deferral when evidence is missing, but that disposition still differs from proof that the claim is false.

#### ADM.7:4.5 - Bind the result to the actual use

Return the claim, its answer, the material basis and any limitation that changes action. Add enough identity and timing to prevent substitution between check and use. If a payment instruction can change after approval, verify that the provider receives the approved amount and destination under the applicable procedure.

A historical observation cannot establish an indefinitely changing condition. [SYSE.28][SYSE] supplies the engineering question of where a check or enforcement mechanism must act when later changes can defeat it. Use an adequate existing control directly in a case; do not redesign its placement merely because a request arrived.

The consuming person then applies the governing rule or makes the required decision. Keep that decision and subsequent performance separate from the check. Reopen only a result affected by a material changed condition.

### ADM.7:5 - Archetypal Grounding

#### ADM.7:5.1 - An eligible expense, with one missing answer

Use the reimbursement policy P from ADM.5. Elena claims 200 units for travel on 10 September. P requires an effective relevant assignment, a receipt corresponding to an eligible business-travel expense, and no earlier reimbursement of the same expense. In this constructed case, P accepts the assigned manager's confirmation of business purpose.

The existing appointment decision covers Elena and the trip date. The handler reuses that temporal result. The receipt identifies Elena's actual journey and amount; the accepted manager confirmation supplies its business purpose. Those results support the corresponding eligibility claims without another appointment inquiry or purpose interview.

The payment log contains an earlier instruction for the same expense, but its effect is unknown. The missing claim is now precise: was that expense already reimbursed by this attempt? A bank or payment-provider effect inquiry can answer it. Another receipt upload cannot.

The provider confirms that the earlier instruction failed before any credit. That result supports the negative answer to “already reimbursed by this attempt”; the handler still checks the actual policy's required coverage of any other possible reimbursement. Suppose the adequate case records establish none. The finance approver can now make the required decision. The provider then performs any authorized payment. The check neither approved the claim nor paid it.

If the earlier effect remains unknown, the handler preserves that uncertainty. A potentially duplicate payment waits for recovery under ADM.9–10.

#### ADM.7:5.2 - The wrong test and an unavailable test

An archive requires an accepted person-identity result and a valid read grant. A device credential succeeds. That observation supports the device operation it actually checked; the handler cannot use it as the required person result or read grant.

If the person checker is unavailable, the outcome is unavailable checking. The existing approved alternative may supply a qualified person check through ADM.6. If the person check instead establishes that the person is different from the grant beneficiary, that is a substantive negative correspondence result, and the applicable service rule supplies the response.

These cases require different next actions despite each sometimes being displayed as “verification failed”.

### ADM.7:6 - Bias-Annotation

Available data and automated scores can dominate the question even when they concern convenient proxies. Start with the actual claim and inspect what the selected check can establish.

The pattern assumes access to applicable criteria and qualified sources. It cannot infer those from institutional prestige, a familiar interface or an applicant's ability to produce more documents. Additional collection should have an action-changing purpose and follow the actual information rules.

### ADM.7:7 - Conformance Checklist

**Recognition.** A reader can recover the exact claim, dependent action, applicable criterion, subject correspondence and substantive outcome. Existing adequate evidence has an explicit scope of reuse.

**Assurance for reliance.** Examine the actual source and check for this claim. Try a relevant subject substitution, changed effective time or unavailable-check case. Confirm that each produces the correct limitation or next action under the rule. Use the qualified domain procedure for consequential correctness; a well-filled evidence table alone cannot establish it.

### ADM.7:8 - Common Anti-Patterns and How to Avoid Them

**Green means eligible** substitutes a successful technical operation for the required institutional claim. State the property actually checked and recover the missing result.

**Unknown means false** turns unavailable evidence into an accusation or an incorrect case account. Preserve uncertainty while applying the policy's actual response to missing evidence.

**Check everything again** ignores adequate existing results. Recheck only a claim whose receiving use or relevant condition has changed.

### ADM.7:9 - Consequences

The handler can reduce irrelevant requests and direct missing-evidence work to the source that can answer it. Decisions receive more precise inputs, and a refusal can distinguish a failed condition from an unavailable check.

This may expose a previously hidden method or evidence gap. More precise uncertainty is not a successful check, but it prevents unsupported permission, denial or duplicate action. Actual service observations are needed to establish the effect on errors and participant burden.

### ADM.7:10 - Architectural Rationale

The organizing relation is between one claim, its evidence and its receiving use. That relation allows a source result to be reused where it remains adequate and limited where it does not. Institutional decisions and provider actions retain their own conditions instead of being collapsed into a generic “verified” status.

### ADM.7:11 - SoTA-Echoing

The working question is how to check the administrative claim that matters to a particular decision without replacing it by an available proxy. The May laboratory's control-purpose problem supplies the domain failure. [A.10][A10], especially §§4.1–4.2 and 4.5–4.6, supplies source and bounded-use recovery; [B.3][B3] is retained only for an actual separately named assurance question.

The selected synthesis applies that evidence discipline with [SYSE.28][SYSE]'s actual reuse, outcome and change-before-use instructions. A generic checklist is the serious low-cost alternative: it suffices when its items already match the case claims and preserve consequential outcomes. It fails when one “pass/fail” field hides an inapplicable or unavailable check, which motivates §§4.1 and 4.4.

[NIST SP 800-63-4][NIST]'s separation of digital-identity functions supports the bounded identity example. It does not supply an expense rule or a universal permission test. The cases are constructed applications, not estimates of checking accuracy.

Reopen a result when its relevant subject, rule, evidence or use changes. Reopen the reusable checking design when actual failures show that the test cannot answer the claimed question or cannot protect the interval before reliance.

### ADM.7:12 - Relations

ADM.2–4 supply participant, relation, time and account correspondence when needed. The handler uses the check result in the actual permission or case decision; ADM.8 governs the permission question, and ADM.9 governs provision. An unavailable competent check returns through ADM.6.

ADM.10 uses effect evidence to reconcile an obligation and performance. [A.10][A10] retains the source-to-use account; [B.3][B3] addresses an actual assurance claim; [SYSE.28][SYSE] designs or repairs a check's placement when that separate question is live.

### ADM.7:End

## ADM.8 - Establish and Exercise the Required Permission

**Type:** Architectural

**Status:** Stable

### ADM.8:0 - Use this when

Use this pattern when an intended administrative action needs a permission and the performer must establish the applicable grant, its conditions or a material conflict before acting. Examples include approving expenditure, booking a journey, reading an archive or instructing a payment.

Start with the actual performer and intended action, including the resource, extent and time that matter. The first useful result is the applicable permission and its conditions, an established lack of the required permission, or the precise unresolved authority question. When the current work includes performance, the performer then acts within the established bounds.

Use an adequate standing grant directly. The pattern does not require a fresh approval for every exercise. Technical ability, an appointment or an absence of known prohibition can be relevant inputs; each supplies only the condition it actually establishes.

### ADM.8:1 - Problem frame

A person or organization proposes an action for which the applicable institutional arrangement requires authority. The beneficiary of a grant may perform the action or may act through another participant whose own authority must be established. Approval of expenditure, delegation to an agent, access to a technical system and actual performance can therefore concern different actions.

The permission question is bounded. Permission to ask for a quote may already exist while permission to incur expenditure is still missing. Permission to read a collection does not necessarily cover downloading or disclosing it.

The local policy, agreement or competent decision supplies the substantive grant and conflict rules. This pattern establishes and uses their application to the case; it does not invent the institution's authority structure.

### ADM.8:2 - Problem

Administrative handling often treats all successful preparatory steps as “approval”. A directory entry, supervisor endorsement or enabled button is then used as if it granted the exact action. Conversely, staff repeatedly seek approval already supplied by a standing grant.

Conflicts create a further error. A handler may assume that a permit overrides a prohibition, or ask another decider despite an applicable precedence rule already settling the case. Both responses lose the actual authority and scope of the decision.

### ADM.8:3 - Forces

| Force | Tension |
| --- | --- |
| Usable authority | A performer needs an actionable answer, while broad labels conceal resource, purpose, amount and time limits. |
| Reuse | Standing grants reduce repeated decisions, but cannot cover changed actions or expired conditions. |
| Conflict | An applicable rule can settle incompatible conclusions; unresolved cases require a competent result. |
| Technical enforcement | A mechanism can block or enable an action without constituting institutional permission. |
| Performance | Permission supports an action but does not establish that the action occurred or its promised result was supplied. |

### ADM.8:4 - Solution

#### ADM.8:4.1 - Name the action and actual participants

Specify who intends to do what, to which resource or recipient, for what relevant purpose, extent and time. Identify whose grant is being used and whether the performer acts for another participant. Add a delegation question only when the action depends on one.

Separate neighboring actions when their permission conditions differ. A manager's authorization to approve a travel expense does not automatically authorize the travel handler to approve it; the handler may instead be authorized to prepare the claim or issue a booking after that approval.

Use ADM.2 for an unclear participant or relation and ADM.3 for uncertain effectivity. Use already adequate results without rebuilding the organizational account.

#### ADM.8:4.2 - Recover the required positive basis and conditions

Obtain the applicable grant or rule-derived permission and the source that establishes it. Match the beneficiary, action, resource, extent and effective conditions to the proposed exercise. Check a relevant revocation, suspension or unmet prerequisite when it can alter this use.

Establish separately any eligibility condition required by the grant. A valid appointment can meet an appointment condition while leaving the required read grant absent. A technical credential can support authentication without supplying spending authority.

If the governing arrangement requires a positive grant, a non-prohibition finding alone is insufficient. If the rule itself permits the action under specified conditions, apply that rule; do not manufacture a separate approval requirement.

#### ADM.8:4.3 - Resolve only the conflict that actually applies

Determine whether the apparently competing conclusions concern the same beneficiary and action with overlapping scope and time. A download restriction may leave a permitted read untouched. A restriction from 09:00 to 11:00 does not by itself govern an action at noon.

For an actual conflict, follow [A.2.8.PER][PER]'s distinction. First apply a matching current precedence rule when it selects the applicable conclusion. Otherwise reuse an adequate authorized resolving decision for this scope and time. Only a remaining unresolved conflict calls for the competent person to decide the exact question.

The title of an office, the presence of two records or the handler's preferred outcome supplies no precedence. Preserve the unresolved condition if the authorized answer is unavailable. An authorized variation does not retroactively make a failed factual prerequisite true.

#### ADM.8:4.4 - Return the bounded permission result

State which action by which performer is permitted, under what action-changing conditions, or why the required basis is absent or unresolved. Include the relevant source or decision reference where the recipient needs it to rely on the result.

Apply the ordinary service response to an established negative condition. If a distinct alternative basis is actually claimed, investigate that question. A missing grant, conflicting evidence and a settled prohibition need not receive the same response.

Keep a request for permission separate from the received grant. Use ADM.6 to obtain a missing competent answer or resolve an unavailable authority arrangement. The handler does not acquire the authority by documenting the gap.

#### ADM.8:4.5 - Exercise within the established bounds

If the present task is only to answer the permission question, stop with that answer and its conditions. When the task includes the action, the authorized performer carries it out under those conditions and obtains the evidence of actual performance needed by its consumer.

Before a delayed exercise, revisit only facts that can change the permission: expiration, revocation, changed amount, resource, purpose or performer. A permission for one date does not extend because provision was late. A different permitted action may proceed while a separate grant remains pending.

Technical enforcement implements its specified rule. A successful operation supplies evidence about the operation and effect it actually achieved. Use ADM.9 when the beneficiary's promised condition still needs to be provided or established; use ADM.10 when performance and records disagree.

### ADM.8:5 - Archetypal Grounding

#### ADM.8:5.1 - A quote and a booking have different prerequisites

A travel handler is permitted by the supplied service policy to request nonbinding prices. The same policy permits booking only after a named budget holder authorizes the expenditure. A traveller supplies a destination and date, but the budget authorization is pending.

The intended first action is a nonbinding price inquiry. The standing permission covers the handler, inquiry and relevant provider; the stipulated other conditions hold. The handler can obtain a quote now. That action does not create the budget holder's approval or commit the organization to the booking.

After the budget holder authorizes a specified booking up to 300 units for the named trip, the handler receives a 280-unit offer within those conditions. The existing booking instruction and grant permit the handler to book it. An otherwise similar 340-unit offer is outside the supplied amount condition and needs its applicable response or a new competent decision.

The budget holder's decision, handler's booking action and traveller's usable travel arrangements remain separately recoverable.

#### ADM.8:5.2 - A grant, a temporary restriction and an unresolved variant

A researcher has a valid read grant for collection R on 2 October. A security instruction restricts that same read action from 09:00 to 11:00. The supplied policy explicitly gives this temporary security restriction precedence during that interval. At 09:30 the handler applies that rule: the read action is restricted, and no additional discretionary decision is needed.

At noon the temporary restriction no longer covers the requested action. Suppose the grant and all its other conditions still hold and no other applicable restriction is present. The researcher can exercise the read permission. The earlier conflict does not create an all-day ban.

Now change the case: both conclusions apply at 09:30, but no matching precedence rule or adequate resolving decision is available. The handler returns the exact conflict to the authorized security/access decision maker and preserves the unresolved permission question. Naming that person is not the resolving decision.

#### ADM.8:5.3 - Permission survives a provider failure within its conditions

For a permitted read at noon, the portal fails to open collection R. The grant is still valid. The provider investigates the failed use under ADM.9, using any permitted existing recovery route.

The provider may not silently give download access when the grant covers reading only. If recovery is delayed beyond the grant's effective day, the permission question reopens for the later use. Repairing software neither broadens the action nor extends its time.

### ADM.8:6 - Bias-Annotation

Organizational status, familiarity and a powerful interface can be mistaken for authority. Examine the actual grant and action instead of the participant's prestige or technical capability.

A permission account can also become needlessly restrictive by carrying every neighboring action's prerequisites into the present one. Keep the bounded action visible, including ordinary permitted inquiry and correction.

### ADM.8:7 - Conformance Checklist

**Recognition.** The result identifies the action, performer, positive basis where required, material conditions and any applicable conflict. It distinguishes the grant, its exercise and a non-prohibition finding.

**Assurance for reliance.** Compare the actual grant and rule to a changed amount, action or time that could alter the answer. For a conflict, establish the scope overlap and the rule or authorized result that settles it. For performance, obtain evidence of what the performer actually did; a permission record alone cannot supply that evidence.

### ADM.8:8 - Common Anti-Patterns and How to Avoid Them

**The button grants authority** treats technical capability as institutional permission. Recover the rule or grant required for the action.

**Approval everywhere** repeats a standing authorization or blocks inquiry behind an unrelated spending prerequisite. Match the condition to the particular action.

**Permit always wins** invents conflict precedence. Apply the actual matching rule or adequate resolving decision; return only the unresolved question.

**A repair enlarges the grant** supplies an excluded action or later use as a convenient workaround. Recover permission for the changed action before relying on it.

### ADM.8:9 - Consequences

The performer can use established authority without needless reapproval, while material limits remain explicit. Handlers can give a precise response to absent permission and keep technical repair separate from institutional decision.

This requires access to the operative grant and conflict rules. Some actions remain unresolved when those sources or decisions are unavailable. An intelligible permission account improves the basis for action; it does not prove that the later provision succeeded.

### ADM.8:10 - Architectural Rationale

A permission is a relation under particular conditions, its exercise is an action, and the provider's usable result may be a further effect. Preserving those distinctions lets the handler reuse a grant, identify a real conflict and repair a failed provision without accidentally changing institutional authority.

### ADM.8:11 - SoTA-Echoing

The working question is how to make an administrative action legitimate and executable without confusing grant, eligibility, enforcement and performance. The selected instruction follows the actual [A.2.8.PER][PER] grant, exercise, non-prohibition and conflict distinctions, especially §4.6. The laboratories supply the administrative cases in which device permission, institutional conditions and usable access diverge.

[OASIS XACML 3.0][XACML], terminology and §7.2, supplies a serious policy-decision/enforcement comparison. Its architecture separates information, decisions and enforcement; it requires defined handling of inapplicable or indeterminate outcomes. Sections 4.2–4.5 retain that separation without prescribing XML or importing an XACML enforcement operation as a general legal obligation.

A direct standing rule is the strongest simpler alternative and is sufficient when its conditions settle the action. A universal approval workflow adds cost and can misclassify independent actions; an allow/deny interface alone can conceal the missing institutional basis. The constructed cases test these distinctions under supplied rules, not the legality of an actual organization.

Reopen the affected permission when its beneficiary, action, scope, rule or effective conditions change. Changes to a technical implementation require reconsidering permission only where they change those conditions or the action being performed.

### ADM.8:12 - Relations

ADM.2–3 establish the relevant participants and effective relations; ADM.7 checks a needed claim without granting permission. ADM.6 supplies a competent return for a genuine unresolved question. The authorized performer uses the applicable permission in acting, and ADM.9 establishes the promised usable condition when provision is the next task.

[A.2.8.PER][PER] governs the grant/exercise/non-prohibition distinction. [OPS.6][OPS] supplies situated continuation when a legitimate next action still needs to be selected.

### ADM.8:End

## ADM.9 - Provide a Usable Administrative Result

**Type:** Architectural

**Status:** Stable

### ADM.9:0 - Use this when

Use this pattern when a participant needs an authorized administrative condition to become usable, or when an approval or completion message does not establish that the promised result is available. Typical cases are access that still fails, accommodation that cannot be occupied or a payment instruction whose effect is unknown.

Start with what the recipient must be able to do and the provider action expected to make that possible. The first useful result is the promised usable condition with adequate evidence, or the exact remaining provision failure and accountable next action.

Use an adequate existing provision and recovery instruction directly. A request only for a permission answer can finish under ADM.8; a service whose promised result is a booking can finish with a usable booking. The completion criterion follows the actual promise, not a universal demand to prove all later business outcomes.

### ADM.9:1 - Problem frame

A beneficiary, relevant permission and intended administrative condition are known sufficiently to act, or the outstanding prerequisite is explicit. A provider has the ability and assignment to perform the needed action. The handler connects that provider's work to the condition the participant will use.

Several results may occur on the way: a request is accepted, a decision is issued, work is scheduled, a provider acts and an effect becomes usable. Each may be valuable for its own purpose. The handler must determine which one satisfies the particular service promise.

Provision can be synchronous and simple. A participant may immediately receive the required document through an authorized channel. Delayed or externally effected provision may instead require enough attempt identity and observation to recover a failure without duplicating work.

### ADM.9:2 - Problem

A service reports completion when its internal task ends. The recipient then discovers that access still fails, the reservation is unusable or funds have not been confirmed. The unresolved work moves to the recipient, while the service's record appears successful.

A blind retry can make matters worse. An unobserved payment may already have occurred; an interrupted account change may be partly applied. Repeating the instruction without knowing its effect can produce duplication or contradictory conditions.

### ADM.9:3 - Forces

| Force | Tension |
| --- | --- |
| Recipient use | The beneficiary needs a practical condition, while provider systems expose intermediate activity more readily. |
| Permission | The authorized action may be clear even when provision fails; a workaround may change its scope. |
| Recovery | Fast retries can help reversible operations but can duplicate uncertain external effects. |
| Evidence | Adequate confirmation should support the promised use without demanding an unnecessary ceremony from every recipient. |
| Continuity | An honest partial or unknown result needs a next action, not merely an accurate failure label. |

### ADM.9:4 - Solution

#### ADM.9:4.1 - Recover the promised usable condition

Name the recipient, condition, relevant time and intended use. Recover the applicable authorization and provider assignment from existing results. Use ADM.1 or ADM.8 only for an actual unresolved framing or permission question.

Describe completion so the handler and recipient can distinguish it from a preparatory step. “The researcher can retrieve the permitted document on the intended day” is different from “the administrator entered an access rule”. Conversely, when the requested result is a reservation that can later be used, occupied accommodation is not the immediate completion criterion.

State any prerequisite whose absence still prevents provision. An approved service plan does not establish that a provider has been assigned or can deliver it.

#### ADM.9:4.2 - Give the capable provider an executable request

Use the existing supported channel and instruction. Supply the authorized action, actual recipient, relevant resource or destination, effective conditions and information needed to perform it. Preserve sensitive information through the applicable protected mechanism.

For a simple immediate action, the ordinary request and result may suffice. When delay, cancellation or uncertain external effects matter, preserve an identifier and evidence that allow the provider and handler to recover the same attempt. Do not create a separate job-tracking scheme for every trivial request.

Identify who can investigate or repair the effect. A generic support link is insufficient if no provider is actually assigned to answer the relevant question. ADM.6 can obtain the missing contribution.

#### ADM.9:4.3 - Establish the effect needed for this use

The provider performs the authorized action. The handler then uses evidence adequate for the promised effect: a recipient's successful use, a qualified provider confirmation or another observation accepted by the applicable arrangement.

Match that evidence to this beneficiary, resource, amount, configuration and time where those distinctions matter. A successful test with an administrator's account cannot automatically establish the beneficiary's access. One document successfully opened establishes only the scope that the observation and supporting conditions carry.

Keep the result proportionate. An ordinary confirmed delivery need not provoke a new independent test unless the promise or actual uncertainty requires it. An “instruction accepted” response cannot establish a downstream effect that the provider has not yet observed.

#### ADM.9:4.4 - Distinguish failure, partial effect and unknown effect

Locate what actually happened before choosing recovery.

| Observed situation | Next provision question |
| --- | --- |
| No effect occurred and the cause is established | Can the provider correct that cause and retry under the existing authorization and recovery instruction? |
| Part of the effect occurred | What remains needed, what must be preserved, and would another action duplicate or contradict the completed part? |
| The effect may have occurred but cannot yet be established | How can the provider recover the earlier attempt's actual state before a potentially duplicate action? |
| The promised condition is usable | Does the available evidence support the requested completion statement within its scope? |

A failed response channel does not prove that the provider action failed. Look up or investigate the same attempt when possible. If the provider cannot establish its effect, preserve that uncertainty and restrict the dependent repeat action according to the applicable recovery rule.

For a payment, ADM.10 connects the recovered effect to the obligation and records. Technical data or software recovery stays with its qualified engineering method; this pattern does not invent a rollback procedure.

#### ADM.9:4.5 - Recover a permitted path and return the actual result

Apply an adequate existing recovery instruction or permitted alternative. Confirm that it supplies the promised condition within the same relevant authorization. An alternative read channel can be sufficient; sending a downloadable copy may be outside the read grant.

If the action, amount, recipient, resource or effective time changes materially, obtain the required permission result through ADM.8. An expired grant cannot be extended by treating the later use as completion of an earlier support ticket.

Return the usable result and relevant limitations, or the remaining condition, competent next action and applicable time or stop condition. Distinguish successful provision, a partial usable result and an unresolved effect. Ending an investigation with a reasoned refusal is a possible case disposition, but it does not mean the requested condition was supplied.

Use [SYSE.26][SYSE] when the supported interaction or failure recovery itself needs design. A single failed request with an adequate recovery path needs that path applied, not a new portal.

### ADM.9:5 - Archetypal Grounding

#### ADM.9:5.1 - The read grant is valid and the service still fails

A researcher has an effective appointment, an accepted identity result and a valid grant to read document D from archive R on 2 October. The provider has been assigned to supply that access. These prerequisites are stipulated as adequate for the example.

An administrator installs the expected access rule and marks the request complete. The researcher attempts to open D under their actual account and receives an access error. The installation is an observed provider action; the promised condition is still unavailable.

The existing support instruction lets the archive provider inspect the account/resource mapping for that attempt. The provider finds that the rule was associated with a different account identifier. It corrects the mapping under its assigned authority. The researcher then opens D through the permitted channel, and the evidence supports completion for the named document and time.

If the service promise instead covered a larger collection, this single opening would need the applicable additional evidence of that scope. The handler does not promote a narrow observation into a whole-collection result.

If the ordinary channel remains unavailable, a supplied authorized attended-reading route may provide the same permitted use. A downloadable copy is not a substitute when the grant excludes downloading. If the usable access cannot be supplied until 4 October, the grant for 2 October does not cover that later use; the permission question reopens.

#### ADM.9:5.2 - A payment response disappeared

Treasury is authorized to transfer 400 units to a specified recipient. The payment provider receives an instruction, but the response connection fails. The available observation is “the response was lost”; it does not establish whether funds were credited.

The handler preserves the original attempt reference and requests its effect through the provider's authorized inquiry channel. The provider confirms credit to the intended account. Under the supplied payment terms, that evidence establishes the promised effect; no second payment is needed.

If the provider instead confirms failure before any credit, treasury can use its applicable authorized retry instruction. If the effect remains unknown, the handler returns that uncertainty and the effect-recovery task. ADM.10 determines what can then be said about the obligation and records.

### ADM.9:6 - Bias-Annotation

Provider dashboards favor events inside the provider's control. Recipients may experience a failure after every internal task has succeeded. Observe the condition relevant to the recipient's use without assuming that one person's feedback represents every user or future attempt.

The pattern also resists a universal requirement that every recipient perform a ceremonial acceptance test. Use the evidence adequate for the actual promise, uncertainty and receiving decision.

### ADM.9:7 - Conformance Checklist

**Recognition.** The result names the beneficiary's promised usable condition, actual provider action and evidence of effect. A partial or unknown result identifies what remains and who can act.

**Assurance for reliance.** Compare the evidence with the actual recipient, resource and effective conditions. Exercise an uncertain-effect or partial-effect case where repetition could cause harm, using the existing qualified recovery method. Establish that the alternative or retry stays within its permission and does not silently duplicate completed provision.

### ADM.9:8 - Common Anti-Patterns and How to Avoid Them

**Closed means supplied** equates an internal record with the beneficiary's condition. Recover the actual promised effect and its evidence.

**Retry to discover what happened** uses another consequential action as a diagnostic for the first. Recover the earlier effect through a suitable observation or qualified recovery.

**Any workaround is equivalent** ignores scope or permission changes. Compare the alternative's actual use with the promise and grant.

### ADM.9:9 - Consequences

Completion becomes meaningful to the participant who needs to work. Failed provision can retain its valid authorization and receive focused provider recovery, while unknown effects are less likely to trigger duplicate actions.

The cost is access to evidence beyond the provider's immediate task status and, sometimes, cooperation across providers. A bounded successful use establishes that result under its conditions; service-wide reliability requires broader observations.

### ADM.9:10 - Architectural Rationale

Authorization, provider action and beneficiary effect are connected but distinct. The first allows an action, the second occurs through performance, and the third determines whether the promised condition was supplied. This separation makes recovery local: repair the failed contribution without inventing another permission or erasing an already completed effect.

### ADM.9:11 - SoTA-Echoing

The working question is how administrative handling reaches the participant's usable condition, including recovery after ambiguous provider effects. The May and July laboratories supply the access and enabling-service failures. Include the participant's effort in obtaining the service when judging whether provision is usable.

The selected instruction uses [SYSE.26][SYSE], §§4.1–4.5: begin with the user's undertaking, distinguish progress from result and uncertainty, recover the same attempt before a consequential replay, and keep support connected to failed use. ADM adds the explicit institutional grant, promised condition and beneficiary correspondence.

A provider completion response is the serious simpler alternative. It is sufficient when its actual semantics and evidence establish the promised effect; it is insufficient when it only acknowledges receipt of an instruction. This comparison determines §§4.3–4.4. No particular portal, persistent job model or universal recipient test is selected.

Reopen the affected provision or recovery instruction when the promised use, authorization, provider capability or effect evidence changes, or an actual failure reveals an unsupported transition. The constructed cases establish an intelligible application, not measured service reliability.

### ADM.9:12 - Relations

ADM.1 supplies the enabled condition and ADM.8 the relevant permission when either is unresolved. ADM.7 checks a needed effect claim; ADM.6 obtains a missing competent contribution. ADM.10 connects the actual effect to an obligation and participant records.

The handler applies an existing service instruction from ADM.5 where one is needed. [SYSE.26][SYSE] supplies supported-interaction and recovery design for a genuine engineering question; engineering realization itself remains with its qualified provider and method.

### ADM.9:End

## ADM.10 - Reconcile What Was Owed, Performed and Recorded

**Type:** Architectural

**Status:** Stable

### ADM.10:0 - Use this when

Use this pattern when participants need to determine whether an administrative obligation was fulfilled, yet the obligation, actual performance and records do not line up clearly. A payment record may be closed while part of the credit remains unconfirmed; an access obligation may be recorded as fulfilled while the recipient could not use the permitted resource.

Start with the particular obligation and its applicable fulfillment rule, then compare the performance evidence and records for that same subject and time. The first useful result is a supported reconciliation, or the exact remaining discrepancy and competent next action.

Use a sufficient existing reconciliation directly. An isolated spelling correction with no effect on meaning does not require this inquiry. The pattern does not supply statutory accounting, tax, valuation, treasury or legal discharge rules; use the rule actually governing the obligation and obtain a qualified interpretation when that rule is unresolved.

### ADM.10:1 - Problem frame

The handler is comparing what one participant owed another, what actually happened and what the participants recorded. Those may be three different claims about related subjects. A record may describe an instruction, debit, credit, allocation or case closure; each can have a different effective or recording time.

The obligation's fulfillment condition must be known. Issuing an instruction, crediting a recipient, accepting a deliverable and making a resource usable can be different conditions. The handler cannot infer which condition discharges an obligation from the most convenient system status.

Participant-relative descriptions remain legitimate. A payer's outgoing payment and a recipient's incoming receipt can concern the same transfer. ADM.4 supplies their correspondence when needed; this pattern then determines what that event establishes about the particular obligation.

### ADM.10:2 - Problem

A handler compares two totals or status fields without establishing their meaning, scope or time. Apparent equality is then reported as settlement, or a harmless difference in recording time is treated as failed performance.

A more serious error turns missing evidence into another payment. The record says 400 remains, so someone instructs 400 again, although the earlier instruction may already have credited the recipient. Correcting the account requires recovering the event before changing the world.

### ADM.10:3 - Forces

| Force | Tension |
| --- | --- |
| Comparable claims | Common amounts and labels can conceal different events, quantities, purposes or periods. |
| Institutional effect | Actual performance matters under a supplied fulfillment rule; the handler cannot invent that rule. |
| Honest uncertainty | Unconfirmed effect differs from known nonperformance and may prevent a safe repeat action. |
| Participant accounts | Several correct records can coexist while their correspondence needs to remain recoverable. |
| Corrective authority | A record correction, additional provision and change to an obligation can require different authority. |

### ADM.10:4 - Solution

#### ADM.10:4.1 - Fix the obligation and the question being answered

Identify who owes what to whom, for which subject, quantity or usable condition, purpose and relevant time. Recover the operative agreement, decision or rule and its actual fulfillment condition. Include a change, suspension, allocation or permitted offset only when it matters to this obligation.

State the receiving question: whether the obligation was fulfilled by a particular date, what is still established as outstanding, why two accounts differ, or which corrective action is now needed. A historical statement and a present payment decision may require different evidence.

If the fulfillment rule is unavailable or disputed, obtain its competent interpretation. A ledger label cannot supply the missing rule. Use ADM.3 for a material effective-time question.

#### ADM.10:4.2 - Align the claims before comparing them

Recover what each record asserts and what evidence supports actual performance. Establish event identity and participant correspondence through ADM.4 when needed. Use [SIE.4–6][SIE] for a genuine unresolved source-meaning or identity question.

Match quantities, units, direction, gross or net basis, allocation, observation time and coverage where those distinctions can change the conclusion. A debit from the payer and a credit to the recipient may be different observations of a transfer. Two identical amounts may instead belong to two different transfers.

[OPS.15][OPS] supplies comparison of observations for matching subjects and bases when that operational comparison is needed. It does not determine the obligation's fulfillment rule. Once the claims are adequately aligned, compare them directly without constructing an unnecessary shared database.

#### ADM.10:4.3 - Apply the fulfillment rule to established performance

Determine which evidenced effects satisfy which part of the obligation under the supplied rule. Keep the actual event, evidence of it and institutional consequence distinct. A later report can improve knowledge of an earlier credit without making the credit occur on the report date.

Distinguish at least the differences that change the next action:

| Difference | What must be resolved |
| --- | --- |
| Meaning or identity | Whether the records concern comparable claims about the same subject or event. |
| Time or coverage | Whether one account is earlier, later or covers a different interval or subset. |
| Quantity or condition | Whether established performance meets the amount or usable condition actually owed. |
| Authority or allocation | Whether the governing decision permits the claimed change, correction, offset or application. |
| Unknown effect | Whether an earlier action actually supplied any of the condition; missing evidence is not proof of nonperformance. |

A known fulfilled part and an uncertain remainder can coexist. Report each with its basis. Do not infer that a whole obligation is settled merely because the case record is closed, or that an uncertain remainder is definitely unpaid.

#### ADM.10:4.4 - Select the correction that matches the discrepancy

For a recording defect with adequate performance evidence, obtain the authorized correction and retain the needed connection to the original event and prior account. Correcting a description does not undo or repeat the historical action. If the governing rule gives a recording act a constitutive effect, apply that rule explicitly.

For established missing performance, identify the provider action and permission actually required to complete it. ADM.8 supplies a live permission inquiry; ADM.9 supplies provision. A handler authorized to edit a case record is not thereby authorized to issue payment or amend the obligation.

For an unknown earlier effect, first recover the same attempt through its competent provider. If the effect occurred, reconcile and correct the account. If it did not occur, use the applicable authorized continuation. If it remains unknown, preserve that uncertainty and the next recovery action before any repetition that could duplicate performance.

A real dispute about the obligation or its interpretation returns through ADM.6 to its competent decision maker. The reconciliation cannot settle that dispute by choosing one participant's preferred record.

#### ADM.10:4.5 - Return the reconciled account and remaining action

Give the participants the bounded conclusion, material basis and any unresolved difference. Retain each participant's correct account and explain its correspondence where a common event is used.

A small case may finish with a short note: the named obligation was fulfilled by the confirmed effect at the relevant time, and the record has been corrected by the authorized handler. An unresolved case needs the precise missing claim, its competent recipient and the action that depends on it.

Reopen only the affected conclusion when new evidence, a corrected meaning, a valid changed obligation or a relevant effective-time fact arrives. Do not reopen unrelated reconciled cases merely because the same provider supplied the new information.

### ADM.10:5 - Archetypal Grounding

#### ADM.10:5.1 - One thousand owed, six hundred confirmed, four hundred unknown

Organization P owes supplier Q 1,000 units for invoice I. The supplied terms say that amounts credited to Q's designated account discharge the corresponding portion of this obligation. For this example there are no fees, offsets, other credits or changes to I.

Evidence confirms a 600-unit credit to that account. A second instruction for 400 units was issued, but its effect is unknown. The case record says “paid 1,000” because both instructions were sent.

The handler establishes that the confirmed 600 discharges that portion under the supplied terms. The second instruction establishes an attempted payment, not its credit. The remaining 400 has an unresolved effect; the available evidence does not establish whether the actual outstanding amount is now 400 or zero. The record's closed status cannot settle the question.

The handler uses the original second-attempt reference to ask the payment provider whether and when Q's account was credited. The possible returns have different consequences:

| Provider result | Reconciliation and next action |
| --- | --- |
| The 400 was credited to Q's designated account | The supplied terms establish full fulfillment. The authorized handler corrects the account or evidence linkage as needed; there is no remaining payment to issue. |
| The attempt failed without a credit | The available evidence establishes 400 still outstanding under the stated assumptions. The competent participants arrange the properly authorized remaining provision. |
| The effect still cannot be established | Retain the confirmed 600 and the 400-unit uncertainty. Continue the assigned effect inquiry before any potentially duplicate payment. |

Suppose the confirmed second credit occurred on 10 September but the provider's report arrived on 12 September. The event time remains 10 September. A report made on 11 September with only the earlier evidence should have stated uncertainty. The later evidence supports a better historical account, not a new credit on 12 September.

#### ADM.10:5.2 - Compare debit, credit and fee before deciding fulfillment

In a different case, P's account shows a 1,000-unit debit, while Q's account shows a 990-unit credit and a separate fee claim. Before inferring an unpaid balance, the handler establishes the event correspondence, quantity bases and actual fee allocation.

If the supplied terms require a net 1,000 credit to Q, the 990 credit alone does not establish full performance of that condition. If a different applicable term assigns the fee differently, its competent interpretation determines the institutional consequence. The two record totals cannot choose the term.

Likewise, a 1,000-unit receipt allocated to another invoice cannot automatically close I. The handler needs the actual allocation basis and authority before applying the receipt to this obligation.

### ADM.10:6 - Bias-Annotation

The most accessible ledger can appear to be the truth for every question. Inspect whether it records instructions, effects, obligations or a participant's classification before relying on it.

Financial examples make quantities visible, but administrative fulfillment can concern usable access or another condition. Do not force every such condition into a monetary balance. The pattern also does not equate one common event account with one mandatory database.

### ADM.10:7 - Conformance Checklist

**Recognition.** The result distinguishes the obligation, its fulfillment rule, evidenced performance and records. It states what is established, what remains uncertain and which correction or provision is actually needed.

**Assurance for reliance.** Trace the conclusion through actual event correspondence, comparable quantities and times, and the governing rule. Examine a missing-effect, changed-allocation or delayed-evidence case that could alter the next action. Verify that a record correction and any new provision use their own authority, and that uncertainty has not become an invented settlement or duplicate action.

### ADM.10:8 - Common Anti-Patterns and How to Avoid Them

**The ledger is closed, therefore the obligation is discharged** substitutes record status for the applicable fulfillment condition. Apply the rule to evidenced performance.

**The totals match, therefore the accounts agree** ignores gross/net basis, identity, allocation or time. Align the claims before comparing amounts.

**Unconfirmed means unpaid** turns missing evidence into an instruction to repeat. Recover the earlier effect and retain uncertainty until the result supports a continuation.

**Correcting history by changing the event** treats a revised account as another payment or a retroactive obligation change. Distinguish authorized description correction from actual provision and constitutive acts.

### ADM.10:9 - Consequences

Participants can see which portion of a claim is established, why apparently different accounts may both be correct and what work remains. Reconciliation can avoid duplicate provision and direct corrections to the person with the right authority.

The process depends on adequate event evidence and an applicable fulfillment rule. A precise unresolved account may be the only supportable result. Broader accounting correctness and operational effectiveness require their own qualified evidence.

### ADM.10:10 - Architectural Rationale

The obligation, performance and record have different change conditions. Their connection is established through event correspondence and the operative institutional rule. Keeping those conditions separate permits a later correction of knowledge without changing the event, and a legitimate additional action without treating every discrepancy as missing performance.

### ADM.10:11 - SoTA-Echoing

The working question is how to determine fulfillment across participant accounts without confusing instructions, effects and records. The July laboratory supplies the administrative problem. Use an account suited to the decision while preserving accounts needed for other purposes. Partridge and colleagues' [accounting][PARTRIDGE-A] and [agentology][PARTRIDGE-B] arguments support preserving participant-relative meanings around an established common subject.

The selected synthesis combines that representational contribution with [OPS.15][OPS]'s comparable-observation question, [SIE.4–6][SIE]'s meaning and identity work, and [SYSE.26][SYSE]'s recovery of uncertain provider effects. The substantive fulfillment rule remains an explicit local input.

Direct matching of two records is the serious simpler alternative and suffices when their semantics, coverage and evidence already support the requested conclusion. A universal ledger or wholesale ontology replacement adds no needed result to the worked cases. Sections 4.1–4.4 instead make the institutional rule and unresolved effect visible while retaining adequate existing records.

The 2018 representation arguments are conceptual sources, not current evidence that a particular accounting system is superior. Reopen the affected reconciliation when the obligation, source meaning, allocation, evidence or effective-time basis changes. A broader financial or accounting claim needs its qualified method and evidence.

### ADM.10:12 - Relations

ADM.3 supplies material effectivity distinctions; ADM.4 establishes participant-relative correspondence before this pattern determines what performance fulfills. ADM.7 supplies a missing claim check. ADM.8 establishes any needed permission, and the provider performs remaining provision through ADM.9. ADM.6 returns an unresolved substantive question to its competent source.

[SIE.4–6][SIE] and [OPS.15][OPS] supply meaning, identity and observation comparison within their scopes. The handler uses those results under the actual fulfillment rule; none of those methods creates the obligation or authorizes payment merely by describing it.

### ADM.10:End

# Part C - Engineer the Administrative Arrangement

## ADM.11 - Join Providers Around the Administrative Result

**Type:** Architectural

**Status:** Stable

### ADM.11:0 - Use this when

Use this pattern when several providers contribute to an administrative condition and their local completions do not yet give the recipient a usable result. A new colleague may have an appointment, identity confirmation and an access approval while still being unable to use the required archive.

Start at one consequential join: what does the receiving provider need for its next action, what is actually available, and who can supply the missing contribution? The first useful result is a workable connection between the contributions, including the responsibility and recovery arrangements needed to fulfill the service promise.

Use adequate existing joins directly. A routine case does not require remapping the whole service. If the open question is which complete arrangement a project should use to obtain provision, use SYSE.24 with the relevant administrative conditions; this pattern supplies those conditions and identifies gaps.

### ADM.11:1 - Problem frame

The practitioner is arranging contributions to a particular administrative result or a bounded class of such results. Relevant participants include the recipient, specialist decision makers, providers who perform provision, and whoever has undertaken to arrange the combined result.

The contributions can have different subjects and authorities. An appointment decision, identity result, permission grant, technical configuration and successful use remain distinct even when they concern one researcher. A service catalogue groups descriptions; it does not establish the authority, commitments or working connections among the providers.

The service owner needs enough of the arrangement to explain how the recipient's condition will be supplied, who handles a failed join and which uncertainty prevents a promise. The account can be a short instruction or a few entries in an existing service description.

### ADM.11:2 - Problem

Each provider reports completion against its local criterion. The next provider receives the wrong identifier, an expired result or a decision that does not authorize the required action. The recipient then becomes the investigator and coordinator of a service that was presented as one result.

Centralizing the form does not necessarily repair these joins. It can hide the distinct decisions or move unresolved work into another queue. Conversely, duplicating every specialist function inside one service can be costly and may exceed the service owner's authority.

### ADM.11:3 - Forces

| Force | Tension |
| --- | --- |
| Recipient result | One usable condition may require several separately governed contributions. |
| Local competence | Each provider must retain its qualified judgment while returning something another participant can use. |
| Readiness | Prerequisites belong to the next action; a later result must not be demanded before the action that produces it. |
| Responsibility | Coordination, performance, ownership, permission and commitment can belong to different participants. |
| Proportion | One failed join may need one correction; a genuinely different obtaining arrangement requires a wider comparison. |

### ADM.11:4 - Solution

#### ADM.11:4.1 - Recover the promised condition and actual undertakings

Name the recipient's condition, scope, time and completion evidence. Recover who has undertaken to supply or arrange it and under which terms. Keep a desired target, a forecast and an actual commitment distinct; OPS.13 supplies a live promise question.

Identify only the provider contributions that can change this result. Use existing assignments, permissions and adequate decisions from ADM.2–3 and ADM.8. An unassigned future provider is a proposal, not available capacity or a current undertaking.

When nobody is responsible for resolving a combined-service failure, return that assignment or commitment question to the person authorized to settle it. Naming a coordinator in a diagram does not create the missing responsibility.

#### ADM.11:4.2 - Inspect what each receiving action needs

At a consequential join, state the receiving action and the input it can use. Match the input to the actual person, case, resource, configuration and effective conditions where those distinctions matter.

Use [OPS.8][OPS]'s next-action readiness rule. An identity check can begin when its required information, capable checker and permission are available; the identity result is an output of that action. The later grant decision may need that result. Requiring the final grant before the check would create a false circular dependency.

A local completion label is useful only through what it establishes. Determine whether the receiver has the evidence, decision, resource or actual condition needed next. Retain legitimate participant descriptions and use ADM.4 or SIE when their correspondence is unresolved.

#### ADM.11:4.3 - Make the consequential joins executable

For each unresolved join, obtain the missing agreement or qualified contribution. State who supplies what, who receives and uses it, the conditions of use, and how a mismatch returns to someone able to resolve it.

Use the existing channel when it carries the needed result. A new portal or common record is an implementation choice. Providers may retain separate records if the receiving correspondence is adequate and the required information remains accessible under its applicable restrictions.

Distinguish transferred work from transferred responsibility. A provider may finish an assigned check while another participant retains the obligation to arrange usable access. A change to that obligation requires its actual authorized basis; forwarding the request does not supply one.

#### ADM.11:4.4 - Arrange continuity and recovery where failure matters

Identify the failure that can defeat the combined result: a missing specialist answer, invalid scope, delayed provider, lost correspondence or uncertain earlier effect. Assign the resolution task to the participant capable and authorized to supply it, with the return needed by the next action.

Preserve independent permitted work. A ready price inquiry may proceed while booking authority is pending. Preserve completed contributions within their supported conditions instead of restarting every provider after a local failure.

For overlapping cases, inspect relevant resource windows, priorities, repeated work and existing commitments. OPS.8 supplies operational joins and protection; OPS.12–13 supply material burden and promise questions. A shared specialist already committed elsewhere is not additional simultaneous capacity.

Unknown external effects require the provider recovery in ADM.9–10 before a potentially duplicate action. The combined service retains a precise unfinished condition even when every internal queue would prefer to close its own item.

#### ADM.11:4.5 - Exercise the join and choose the next arrangement decision

Walk one supported case through the actual contributions and a material failing join. Ask the receiving provider to recover its next action from the supplied result, and ask the recipient whether the promised condition has been established.

A description walkthrough tests the arrangement's intelligibility. A bounded operational trial can establish actual transfer, performance and use under its observed conditions. Neither establishes every future provider's reliability.

Return the usable join, its governing undertakings and limitations, or the exact missing provider result. If the existing arrangement cannot supply the condition and a complete obtaining choice is now live, pass these administrative facts to [SYSE.24][SYSE]. That comparison may retain, adapt or replace the arrangement; the join diagnosis does not predetermine centralization or outsourcing.

### ADM.11:5 - Archetypal Grounding

#### ADM.11:5.1 - Three completed contributions and a missing account correspondence

An organization undertakes to arrange Mira's access to document D by 10:00 on 2 October. The service coordinator has the supplied assignment to resolve cross-provider gaps until that condition is established. The appointment office, identity service, authorized grant maker and archive provider retain their distinct responsibilities.

The appointment office supplies a decision effective on 1 October. The identity service returns the accepted person result for institutional identifier M. The grant maker issues a valid read grant for M and D on 2 October. The archive provider requires the corresponding account identifier to configure access.

The first three contributions are adequate within their stated conditions. The missing input is the correspondence between M and the account that will actually read D. “Identity complete” does not establish that correspondence. The coordinator sends the bounded mapping question to the assigned access provider, which can recover the account binding through its authorized directory procedure.

After establishing that binding, the archive provider configures the permitted account. Mira opens D, and the available evidence supports the promised condition. The service did not need another appointment decision, identity interview or grant merely because the mapping was missing.

| Join | What the receiver actually uses |
| --- | --- |
| Appointment to grant decision | The relevant person, effective assignment and scope required by the supplied access rule. |
| Identity result to grant decision | The accepted person result for that beneficiary under the rule's conditions. |
| Grant to archive provision | The permitted action and resource, effective time, beneficiary and supported account correspondence. |
| Archive provision to service completion | Evidence that the intended recipient can use D within the grant. |

If the provider cannot recover the mapping, the service retains that precise gap and the accountable recovery action. The coordinator's assignment does not authorize inventing a mapping or broadening the grant.

#### ADM.11:5.2 - Shared provision does not establish shared capacity

Two services rely on the same specialist during a two-hour window. Each local plan assumes that the specialist is available for its full two-hour job. The assignments reveal an overlap; a common catalogue has not doubled capacity.

The responsible parties use the actual service priorities and commitments to resolve the resource question. They may change timing or obtain qualified additional provision where authorized. The administrative join account supplies the affected cases, needed specialist results and obligations. A claim that a new shared-service arrangement will solve the problem remains conditional until its actual capability and timing are established.

### ADM.11:6 - Bias-Annotation

The service owner can overvalue the part visible inside their own department. Follow the recipient's failed use and the receiving provider's actual prerequisites.

The pattern can also overfit a single coordinator. Coordination is needed where an unresolved join requires it; an adequate direct provider arrangement may operate without another intermediary. No fixed departmental structure is implied.

### ADM.11:7 - Conformance Checklist

**Recognition.** The account connects the promised condition to consequential provider contributions, actual receiving prerequisites and capable failure returns. It distinguishes coordination from the authority and commitments of the participants.

**Assurance for reliance.** Exercise a normal join and a relevant mismatch or unavailable-contribution case. Establish that the next action receives the right subject and effective result, completed work is preserved within its conditions, and someone has the actual undertaking to resolve the remaining service failure. Qualify wider reliability or capacity claims through their proper methods.

### ADM.11:8 - Common Anti-Patterns and How to Avoid Them

**Every department is done** reports local completions while the recipient still lacks the result. Inspect the missing receiving input or usable effect.

**The future output is an entry condition** prevents a check from starting because its result is demanded first. Recover the prerequisites of the actual next action.

**A common catalogue creates one provider** substitutes publication grouping for capability and responsibility. Identify the actual contributions and obtaining relations.

### ADM.11:9 - Consequences

The recipient can obtain coordinated provision with fewer unexplained returns, and providers receive narrower, usable requests. Existing specialist results can remain useful through a local failure.

The arrangement requires access to real commitments, resource conditions and recovery capabilities. It may reveal that a promised result is unsupported. That finding enables an honest service or obtaining decision; it is not itself the missing provision.

### ADM.11:10 - Architectural Rationale

The administrative result is connected through contribution, evidence, permission, performance and responsibility relations. Those relations need not form one hierarchy or one composite method. Identifying them at the consequential joins preserves specialist authority while making the undertakings that support the beneficiary's result explicit.

### ADM.11:11 - SoTA-Echoing

The working question is how separate providers supply one administrative condition without losing the institutional decisions and failure responsibilities between them. The June laboratory distinguishes developing this service arrangement from using it. Judge the arrangement also by the effort it requires from the participant.

The selected synthesis uses the actual [SYSE.8][SYSE] provider-arrangement distinctions, [OPS.8][OPS]'s receiving-action readiness and [OPS.13][OPS]'s separation of forecasts, objectives and commitments. [GOV.UK Service Standard point 2][GOVUK] contributes a whole-user-problem comparison by analogy; it supplies no local authority or provider commitment.

An adequate direct arrangement is the strongest simpler alternative and remains sufficient. A central portal can improve entry but does not necessarily repair result correspondence or failure responsibility. Sections 4.2–4.4 retain those joins; a whole obtaining comparison stays with SYSE.24 rather than being inferred from a preference for centralization.

Reopen an affected join when a provider, required input, permission, commitment, capability or recipient use changes. The constructed cases explain the method under supplied arrangements and make no general cost-saving claim.

### ADM.11:12 - Relations

ADM.1 supplies the administrative condition; ADM.2–4 supply participants, effectivity and correspondence when unsettled. ADM.5 carries reusable handling, and ADM.6 returns a genuine provider gap to its competent resolver. The authorized providers use ADM.7–10 for needed checks, permission, provision and reconciliation.

[SYSE.8][SYSE] develops provider concepts, [OPS.8][OPS] supplies operational joins, and [SYSE.24][SYSE] selects a complete obtaining arrangement when that question is live. ADM.15 examines the resulting consequences; ADM.16 governs an actual institutional transition.

### ADM.11:End

## ADM.13 - Keep Administrative Records Fit for Their Uses

**Type:** Architectural

**Status:** Stable

### ADM.13:0 - Use this when

Use this pattern when someone must later establish an administrative relation, decision or provision, and the retained records may not support that use. A handler may need to explain an earlier refusal, recover the terms that governed an open claim, correct a mistaken account or decide what can be disclosed or disposed of.

Start with the later question and its legitimate reader. The first useful result is the smallest adequate record arrangement for that use, including its interpretation, access, correction and retention conditions, or the exact missing source or competent decision.

Use an adequate record directly. Do not reconstruct every historical event for an ordinary request that already has a sufficient basis. This pattern supplies no universal retention period, disclosure right or legal priority; apply the governing rule and obtain the qualified answer when its application is unresolved.

### ADM.13:1 - Problem frame

The practitioner is maintaining records used in administration. A record may contain a request, rule edition, decision, grant, provider instruction, observed effect or participant account. It may be stored in one system or recovered from several adequate sources.

What is recorded and what occurred have different conditions. An appointment may already be effective before a directory is updated. A rule may instead make a particular registration act part of constitution. The handler must preserve the distinction applicable to the actual case.

Future readers also differ. A recipient needs an intelligible response; a dispute resolver needs the relevant grounds; a provider may need only the current authorized instruction. Fit for one use does not imply unrestricted access or fitness for every other use.

### ADM.13:2 - Problem

A current status overwrites the earlier decision and its grounds. Later staff cannot explain why an action was taken, which terms applied or whether a payment was actually made. Alternatively, an organization keeps every document indefinitely while losing the interpretation or access route needed to use it.

Correction, restricted use and disposal are often treated as one operation. Someone deletes an old account to fix a current display, or keeps exposing information because another legitimate purpose requires retaining it. Both errors substitute a storage action for the actual institutional question.

### ADM.13:3 - Forces

| Force | Tension |
| --- | --- |
| Future use | Enough grounds must remain recoverable without collecting every available fact. |
| Historical accuracy | A corrected account should improve the answer while retaining material earlier decisions and their basis. |
| Access | A record needed for one authorized use may contain information unnecessary for another reader. |
| Retention | Continuing obligations or disputes can require records while other information has reached its disposal condition. |
| Representation | Several correct participant accounts can coexist; a common storage location does not make their meanings identical. |

### ADM.13:4 - Solution

#### ADM.13:4.1 - Name the uses the record must support

Identify who must establish what, for which subject, purpose and time. Include only uses that the applicable service, authority, obligation, recovery or record rule actually requires.

For an earlier refusal, the needed answer may be the request assessed, the applicable rule, the grounds then used and the response given. For a current provider action, the necessary record may be much smaller: an adequate current authorization and its relevant conditions.

Distinguish a required future use from speculative convenience. If an existing source can reliably supply the needed grounds within its authorized access and retention conditions, a second full copy may add no useful result.

#### ADM.13:4.2 - Retain the content and correspondence needed by those uses

Keep the relevant source, decision or event identity, meaning, effective time and recording time where those distinctions change the answer. Identify the material rule or instruction edition used in an earlier decision.

Separate what the source asserts, what the handler established and what action occurred. A provider instruction record does not establish its effect. A copied decision retains only the scope its actual authority and conditions support.

Use [A.10][A10] when the source-to-use account must remain recoverable and contestable. Use ADM.3–4 or SIE for a material temporal or cross-source correspondence question. An ordinary case reference and relevant source can suffice; a complete provenance graph is not a prerequisite for every record.

#### ADM.13:4.3 - Make authorized retrieval and interpretation workable

Arrange a usable return to the record for each required reader. Confirm that the reader can recover the content and understand its meaning under the relevant conditions, rather than merely finding an export filename.

Apply the actual access and disclosure rules. Give a participant the information needed for the legitimate use through an appropriate protected channel. Separate the ability to retain a record from permission to disclose all of its contents.

Where an old format or system is being retired, identify the reading capability, context and identity that must survive. A conversion that preserves visible words but loses the relation between decision, beneficiary and effective date may defeat the needed use. Technical conversion and restoration use their qualified methods.

#### ADM.13:4.4 - Correct the right thing

Determine whether the defect concerns a description, an absent evidential link, an actual institutional act or missing provision. Select the corresponding authorized correction.

For a mistaken description, preserve enough of the original and correction to support the required historical use. State what was corrected and the effective facts the new account describes. A spelling correction does not constitute another appointment or move its effective date.

If the governing rule makes a registration act constitutive, apply that rule to the actual act and its timing. Editing a descriptive field cannot silently perform the required registration. If payment was not performed, a corrected “paid” field cannot supply it; use ADM.9–10.

A later source may change what can now be established about an earlier event. Preserve both the earlier decision's actual grounds and the later qualified account. The competent case procedure determines any resulting revision or remedy.

#### ADM.13:4.5 - Separate new use, disclosure, retention and disposal

For a proposed change, identify which action is being considered. Stopping new requests through an old form, restricting access, correcting a record, ending reliance on an obsolete rule and disposing of retained data are different actions.

Recover the applicable retention and disposal conditions, including a live dispute or hold when one exists. Match them to the actual record class and use. Obtain a qualified interpretation when restrictions conflict; do not invent precedence from the oldest or most convenient instruction.

Apply authorized disposal only to the eligible scope. Retention for one continuing purpose does not authorize unrelated new use or unrestricted disclosure. Conversely, stopping ordinary use does not establish that every required historical record can be deleted.

#### ADM.13:4.6 - Exercise the needed retrieval and return the arrangement

Try the question that made the record necessary: recover the earlier grounds, identify the effect of a correction, or supply the permitted extract. Include a relevant adverse case such as a changed identifier, unavailable old reader or disputed source.

Return the record arrangement and its applicable limits, or the exact missing capability, source or decision. A representative retrieval establishes that use under its conditions; it does not establish every legal or historical claim concerning the repository.

Reopen the affected arrangement when a required use, rule, reader, record meaning, dispute or provider capability changes.

### ADM.13:5 - Archetypal Grounding

#### ADM.13:5.1 - Explaining the earlier access response

On 25 September a researcher requests archive access using an appointment effective on 1 October. Policy P requires an effective appointment at the requested time. The handler establishes that the supplied appointment does not meet that condition and gives P's prescribed response.

For a later explanation, the relevant record retains the assessed request and date, appointment decision and effective date, policy P, the negative temporal result and the actual response. The record does not state that every possible earlier appointment was disproved, or that a separate read grant was checked, when neither inquiry occurred.

A later directory correction fixes the spelling of the researcher's name while preserving identity and the appointment's effective date. The authorized record maintainer corrects the current display. The historical account still explains the September response, and no new appointment or retrospective date is invented.

Now suppose the researcher presents a different, earlier appointment decision. That new source may change the current eligibility account. The handler retains the earlier assessment's actual basis and sends the new source through the applicable case procedure. ADM.3 establishes the temporal claim; ADM.8 supplies any still-required read-permission question. The record of the earlier response is not silently replaced by a fiction that the new source was used at the time.

#### ADM.13:5.2 - A dispute hold and an obsolete service form

Suppose the organization's supplied record rule requires the decision and material grounds for a disputed claim to remain available to the authorized resolver until the hold is released. A separate instruction ends new requests through an old form on 1 November. The old system also contains routine diagnostic records with their own disposal conditions.

The service owner can stop new use of the form under that instruction. The active dispute's decision and grounds still need their permitted retrieval route. The resolver receives the relevant protected account; other readers do not receive unrestricted access merely because retention continues.

Before withdrawing the old reader, the provider demonstrates that the retained decision, source meaning and correction history can be recovered through the authorized replacement. The service owner applies the separate disposal conditions to eligible diagnostic material. If the scope of a restriction or hold is unclear, its competent source receives that question.

Neither keeping the entire old system forever nor deleting it at form closure follows from the supplied rules.

### ADM.13:6 - Bias-Annotation

Current-system designers tend to privilege present fields over historical explanation. Future-use advocates can make the opposite error and retain everything without a defined legitimate purpose. Begin with the concrete uses and rules.

Records also reflect the perspective of their producer. Preserve participant correspondence and material disagreement instead of assuming the most centralized account is correct for every question.

### ADM.13:7 - Conformance Checklist

**Recognition.** The record arrangement names the required use and reader, necessary content and meaning, applicable access, and the distinct correction and retention conditions. It separates a description from any constituting act or actual provision.

**Assurance for reliance.** Recover the actual answer through the intended reader and channel. Check a relevant correction, changed identifier, retention hold or system-withdrawal case. Establish that the needed grounds remain interpretable and that disclosure or disposal follows its own applicable authority. A successful export job alone cannot establish those claims.

### ADM.13:8 - Common Anti-Patterns and How to Avoid Them

**Current status replaces the past** destroys the grounds for an earlier decision. Preserve the material earlier account and the correction needed by later uses.

**The record creates the event** treats an edited field as appointment, authorization or payment. Identify whether the actual rule makes a recording act constitutive and whether that act occurred.

**Retain means disclose** extends a legitimate retention purpose into unrestricted access. Apply the disclosure rule to the reader's particular use.

### ADM.13:9 - Consequences

Participants can explain decisions, recover obligations and correct descriptions without inventing events. Service changes can preserve necessary history while allowing eligible obsolete material to be removed.

The cost is maintaining the access and interpretation needed by actual uses, not merely storage. An unresolved restriction or unavailable historical source can still limit a conclusion. The pattern makes that gap actionable without claiming universal record compliance.

### ADM.13:10 - Architectural Rationale

Records connect participants to claims about relations, decisions and performance. Their usefulness depends on recoverable meaning, legitimate access and the time at which the claim matters. Distinguishing these uses from storage operations prevents correction, cessation and disposal from becoming one accidental action.

### ADM.13:11 - SoTA-Echoing

The working question is how administrative records remain usable for current and historical institutional questions. The May and June laboratories and the qualified ADM source pack supply the relation/record, correction and execution distinctions. [A.10][A10] and [SIE.4–6][SIE] supply bounded source recovery and meaning correspondence.

[ISO 15489-1:2016][ISO]'s public abstract connects records, metadata, responsibilities, business context and controls. That conceptual scope informs §§4.1–4.5. The full paid standard and its clauses are not used here; no retention period or compliance conclusion is derived from the abstract.

A current case database with adequate history and retrieval is the serious simpler alternative and should be used directly. A universal immutable archive or one shared ontology does not by itself answer authorized access, correction or disposal. The selected method follows the actual institutional use and its rule rather than choosing one storage architecture.

Reopen the affected arrangement when its legitimate use, governing restriction, source interpretation or recovery capability changes. The worked examples are stipulated record situations, not jurisdictional advice or measured evidence of a particular system's superiority.

### ADM.13:12 - Relations

ADM.2–4 establish the relevant relation, time and participant account; ADM.7 supplies a needed evidence check. ADM.9–10 distinguish actual provision from the recorded account. ADM.6 returns an unresolved restriction or authority question to its competent source.

ADM.5 specifies what an ordinary case returns, and ADM.16 preserves required records during transition. [A.10][A10] supplies source-to-use recovery; [SIE.4–6][SIE] supplies unresolved meaning or identity work; [SYSE.29][SYSE] supplies the technical provision-retirement question.

### ADM.13:End

## ADM.14 - Connect a Control to Its Purpose and Competent Decision

**Type:** Architectural

**Status:** Stable

### ADM.14:0 - Use this when

Use this pattern when an administrative check or restriction is disputed, ineffective or burdensome, and its purpose, governing requirement, competent owner or remedy is unclear. A mandatory field may reject legitimate requests while failing to prevent the problem it was meant to address.

Start with the action the control checks or prevents and the condition that justifies doing so. The first useful result is a defensible connection from the institutional requirement to the needed claim, qualified check, deciding authority and usable failure response, or an exact missing contribution.

Apply an adequate existing control directly in a case through ADM.7–8. Do not redesign it for every request. A costly or inconvenient control is not thereby invalid, and discovering a questionable requirement does not authorize the handler to suspend it.

### ADM.14:1 - Problem frame

The practitioner is examining a reusable control arrangement. Its purpose may be to prevent unauthorized expenditure, establish eligibility, avoid duplicate provision or protect a required access condition. The actual rule and affected participants determine which interest or obligation is at stake.

The requirement, test, observation, administrative decision and enforcing mechanism can be different objects. A policy owner can require an eligible expense to be paid once; a competent checker establishes the expense and prior effect; treasury uses the result in a payment decision; software may enforce a corresponding restriction.

The service owner needs to know whether these contributions actually connect. A committee decision or a green technical test cannot stand in for every one of them.

### ADM.14:2 - Problem

A control survives because the form or system requires it. Its original purpose is lost, the responsible owner cannot be found and the only available response is “the system will not allow it”. Staff add workarounds or more approvals while the underlying risk remains.

Another failure removes the control to reduce delay without establishing what it protected. The service becomes faster by losing a valid restriction, shifting the check to the applicant or making later recovery impossible.

### ADM.14:3 - Forces

| Force | Tension |
| --- | --- |
| Purpose | A control needs an actual institutional reason, while its technical form may outlive that reason. |
| Competence | The rule owner, qualified tester, case decider and software provider can be different participants. |
| Burden | Checking can prevent loss while also excluding valid cases or creating unnecessary effort. |
| Evidence | A test must answer the relevant claim for the actual subject at the point of reliance. |
| Revision | A better design can be proposed before it has been authorized or implemented. |

### ADM.14:4 - Solution

#### ADM.14:4.1 - Recover the requirement and its competent owner

Name the controlled action, affected participant and condition to be checked or preserved. Recover the actual policy, commitment or other governing source, its scope and effective time, and who is responsible for maintaining or authorizing a change to it.

Ask what failure the requirement addresses and whose interest or obligation that failure affects. Retain an unavailable purpose or disputed applicability as an explicit question. A form field's presence does not establish the requirement; an observer's inability to explain it does not establish that it has no valid use.

Apply a matching rule or adequate existing interpretation directly. If the rule itself is disputed or incomplete, ADM.6 supplies the bounded return to the competent owner. Continue independent work under its own established conditions.

#### ADM.14:4.2 - State the claim and decision the control must serve

Translate the requirement into the actual case question: whether this beneficiary is eligible at use, whether this action has the necessary authority, or whether this expense has already been reimbursed.

Distinguish the factual result from the decision made with it. An unavailable identity check is not proof of ineligibility. An authorized exception can permit a bounded action while the failed or absent factual result remains as it was.

Identify who needs the result and how it changes action. If the existing test answers another claim, name the gap. Do not choose a convenient measurement merely because the system can produce it.

#### ADM.14:4.3 - Obtain the needed qualified method and placement

Reuse an adequate qualified procedure or specialist result within its conditions. [SYSE.9][SYSE] supplies the acquisition question when a missing expert contribution can change the design: specify the needed answer, its use and the attainable work rather than requesting generic approval.

Use [SYSE.28][SYSE] when the test's placement or enforcement needs design. Determine where the checked property can change, where another subject can be substituted, and where the result can still prevent the prohibited reliance. An earlier successful check may remain sufficient through controlled steps that cannot defeat it.

Keep test qualification, implementation and authority distinct. A software provider can implement a supplied rule without being competent to define its legal or security criterion. A specialist result can qualify a test without appointing the person authorized to waive the requirement.

#### ADM.14:4.4 - Provide an intelligible response for each consequential outcome

Specify what the handler or mechanism returns when the condition is satisfied, contradicted, unsupported, inapplicable or currently uncheckable. Use only the distinctions that change action, but preserve those distinctions through the actual interface.

For each failure or uncertainty, name the permitted correction, competent review, existing alternative or reasoned refusal. A technical block should affect the dependent action; it need not cancel an unrelated permitted inquiry or evidence-recovery request.

Connect the returned reason to the source and condition the participant can act on. “Rejected by validation” is insufficient when the participant needs to correct a specific mismatch or challenge the relevant rule. ADM.6–8 supply the case-level resolution, check and permission uses.

#### ADM.14:4.5 - Compare and authorize a change to the right contribution

Compare retaining the current arrangement with the material feasible alternative: clarify a response, reuse an adequate result, change the qualified test or its placement, repair implementation, or ask the authorized rule owner to revise the requirement.

Keep protected conditions visible before weighing optional speed or cost. Include false rejection, missed violations, unavailable checking, displaced work and recovery where they can alter the choice. ADM.15 supplies the consequence comparison.

Choose the smallest supported change. A correct policy with a defective implementation may need technical repair; a genuinely obsolete policy needs its authorized revision. A proposal or committee discussion does not establish adoption. A case handler uses the current applicable rule or an actual authorized exception while that decision remains open.

#### ADM.14:4.6 - Exercise the changed control in its receiving use

For a selected change, exercise a supported case, a known violating case and the relevant uncertainty or unavailable-check branch. Include a changed subject or post-check change when it can defeat reliance. Use the qualified domain procedure for the actual assurance claim.

Confirm that the intended decision receives the correct result and that the failure response reaches someone able to act. A desk comparison supports the design account; a trial of the real implementation supports only the behavior actually observed.

Return the retained or changed control arrangement, its governing basis, actual evidence and remaining gaps. Use ADM.5 for an affected reusable handling instruction and ADM.16 when the authorized change alters open cases, grants or records.

### ADM.14:5 - Archetypal Grounding

#### ADM.14:5.1 - Duplicate expense control checks the wrong identity

Policy P requires eligible expenses to be reimbursed once. The qualified case procedure establishes the actual expense and checks its earlier reimbursement effects. A portal has implemented a shortcut that compares only uploaded image hashes.

A claimant uploads a new photograph of an expense whose reimbursement is already confirmed. The image hash differs, so the shortcut does not identify the earlier payment. The controlling claim is “this expense has already been reimbursed”, not “this file has previously been uploaded”.

The service owner recovers P and the adequate existing expense-correspondence procedure. For the actual case, the handler uses the qualified source and effect evidence to establish the earlier reimbursement and applies P's response. That bounded result can be used immediately; it does not depend on completing a new platform design.

For the reusable repair, the assigned provider implements the supplied correspondence and effect check where the payment decision uses it. The design retains the actual expense identity and evidence needed by the qualified procedure. It does not prescribe an arbitrary universal key or treat equal amounts as one expense.

The exercise includes the same expense with a different photograph, two distinct expenses with equal amounts, and an unavailable prior-payment source. The first must retain the earlier reimbursement result; the second must preserve the distinct expenses; the third must return the missing effect evidence rather than pass the check. These are stated completion conditions for the design and trial, not claims that an implementation has already passed them.

#### ADM.14:5.2 - A paper requirement and an existing policy answer

A service form requests an original paper receipt. The operative policy explicitly permits a qualified electronic receipt for the same expense class, and an adequate existing interpretation covers the submitted receipt. The handler can apply that supplied policy result; another policy decision is unnecessary. The service owner sends the inconsistent form or implementation to its authorized maintainer for repair.

Change the situation: the operative policy actually requires the original for this class and its purpose is disputed. The handler cannot remove the condition by editing the form. The competent owner receives the requirement question and the evidence about burden and alternatives. An existing permitted exception may be used within its scope; otherwise the current rule supplies the case response until it is validly changed.

### ADM.14:6 - Bias-Annotation

Control advocates can interpret every delay as the price of protection, while service-improvement advocates can interpret every restriction as waste. Neither view supplies the actual requirement or evidence of effectiveness.

Digital implementations favor conditions that are easy to count. Inspect whether the convenient property is the one the institutional decision needs, and include the participant who bears a mistaken rejection or extra collection task.

### ADM.14:7 - Conformance Checklist

**Recognition.** The control account identifies its purpose and governing source, the competent rule owner, needed claim, qualified checking contribution, consuming decision and failure response.

**Assurance for reliance.** Use the qualified procedure to examine a valid, violating and relevant unavailable or changed-subject case at the point of use. Establish that the proposed repair changes the intended contribution under actual authority, preserves protected conditions and gives the participant an actionable return. A policy signature and a technical test remain evidence for different claims.

### ADM.14:8 - Common Anti-Patterns and How to Avoid Them

**The form is the policy** treats a mandatory field as sufficient authority. Recover the operative requirement and its actual scope.

**The proxy is the protected condition** substitutes an image hash or document presence for the decision's claim. Identify and test the actual correspondence.

**Faster means better** removes checking without examining its consequence. Compare the permitted alternatives and retained protection.

### ADM.14:9 - Consequences

Handlers can apply settled rules directly, participants receive more intelligible responses and recurring control defects reach the contribution that can be repaired. A valid restriction can remain effective while unnecessary implementation burden is removed.

The inquiry may expose a missing qualified test or unavailable rule owner. Those gaps can prevent a particular change without invalidating every current control or requiring a general redesign.

### ADM.14:10 - Architectural Rationale

The institutional requirement, factual check, administrative decision and enforcing mechanism each have their own conditions and responsible participants. Connecting them explicitly lets a repair stay local and prevents a successful result in one place from acquiring the authority or meaning of another.

### ADM.14:11 - SoTA-Echoing

The working question is how a control remains justified and usable as the administrative situation changes. The May and June laboratories supply the purpose, competent-owner and opaque-refusal failures. The selected synthesis uses [SYSE.9][SYSE] for a worthwhile missing specialist contribution and [SYSE.28][SYSE] for meaningful placement, reuse and consequential outcomes.

[OASIS XACML 3.0][XACML]'s decision/enforcement distinction is a bounded technical comparison. It helps keep an unresolved or inapplicable outcome separate from the policy that governs the response; it does not determine a local requirement or turn an enforcement operation into an institutional duty.

An adequate existing rule and qualified check are the strongest simpler alternative and should be applied. Adding another approval or a more elaborate technical block fails when the actual defect is wrong claim correspondence or missing remedy. Sections 4.1–4.5 therefore locate the governed contribution before choosing a repair.

Reopen the affected arrangement when the protected condition, rule, capable source, test applicability, implementation or observed consequences change. The constructed cases demonstrate the distinctions; they do not establish an empirical false-acceptance rate.

### ADM.14:12 - Relations

ADM.7 applies the established check to a case, ADM.8 supplies its actual permission question and ADM.6 returns a genuine unresolved condition. ADM.13 retains the grounds needed for explanation and correction.

[SYSE.9][SYSE] qualifies a needed specialist contribution and [SYSE.28][SYSE] places a supplied control. ADM.15 supplies the administrative consequence question, ADM.5 updates the affected handling instruction, and ADM.16 governs an authorized transition.

### ADM.14:End

# Part D - Assess and Change the Arrangement

## ADM.15 - Judge Administrative Consequences

**Type:** Architectural

**Status:** Stable

### ADM.15:0 - Use this when

Use this pattern when a decision about an administrative service depends on its actual consequences: whether to retain a promise, repair a control, change a provider arrangement or investigate a reported burden. A high closure rate or shorter provider handling time may conceal unusable results, mistaken refusals or work shifted to applicants.

Start with the decision and the consequence that could change it. The first useful result is a bounded account of provision, correctness, restrictions, recovery and participant effort relevant to that decision, or the exact missing observation.

Use adequate current evidence directly. A known protection breach or supported case defect can justify its applicable response without waiting for a new dashboard. This pattern does not make one speed, cost or satisfaction measure the universal objective of administration.

### ADM.15:1 - Problem frame

The practitioner is assessing a service or proposed change for an identified population, arrangement and period. Relevant participants include recipients, handlers, specialist providers, people who recover failures and others whose work is displaced.

The service's result is institutionally defined. A legitimate refusal can be a correct disposition while the requested condition remains unprovided. A technically successful action can still be unauthorized or unusable. The enabled business work has its own outcome, as ADM.1 establishes.

The receiving decision determines the evidence needed. Describing this week's observed cases, forecasting a future service level and claiming that a redesign caused improvement are different questions.

### ADM.15:2 - Problem

Service reports often count completed tickets and average their duration. Requests abandoned before registration, unresolved cases and participants who supplied unrecorded effort disappear from the account. A local gain is then presented as a whole-service improvement.

Financial and time claims can drift too. Freed staff minutes are reported as cash savings even when no payment changes, or a faster administrative service is credited with the success of the business activity it enabled. These claims can lead the decision maker to retain the wrong arrangement.

### ADM.15:3 - Forces

| Force | Tension |
| --- | --- |
| Decision relevance | Evidence should change a real choice without becoming a permanent collection burden. |
| Population | Completed cases are easy to observe, while excluded, abandoned and unfinished needs may reveal the decisive loss. |
| Several consequences | Speed, correctness, protection, effort and money can move in different directions. |
| Claim strength | A descriptive contrast can be useful while causal and population-wide claims need stronger support. |
| Authority | An observer can reveal a trade-off without having authority to relax a protected condition or change the service. |

### ADM.15:4 - Solution

#### ADM.15:4.1 - Fix the decision, service result and affected population

Name who needs to decide what and when the answer can still change action. Recover the applicable service promise, eligibility and permission conditions, protected interests and actual condition the recipient needs.

Define the cases or attempts relevant to that use. Include unfinished and abandoned cases, repeated attempts and pre-entry failures where omitting them changes the conclusion. Distinguish these subjects rather than adding every log row to one denominator.

Ask affected participants what the visible service record omits. An account of repeated form failure may identify a missing population even before its size is established. Preserve that limited observation while deciding which further evidence matters.

#### ADM.15:4.2 - Choose the observations that can alter the decision

Use existing [OPS.12–15][OPS] and [OCE.13][OCE] results when they match the administrative question. Select only the relevant consequences; the following are discovery questions rather than compulsory metrics.

| Question | Necessary distinction |
| --- | --- |
| Was the condition supplied? | Promised usable effect versus approval, instruction or local closure. |
| Was the handling correct? | Legitimate refusal, mistaken refusal, unsupported approval and unresolved condition. |
| Was a restriction preserved? | Authorized use versus a successful action outside its permission or required protection. |
| What happened after failure? | Recovery, repeated work, unknown effect, abandonment and work shifted to another participant. |
| What time and effort changed? | Elapsed delay, each participant's work, interruptions and displaced work. |
| What financial consequence matters? | Actual or conditional payment, released capacity and the receiving use of that capacity. |

Use the qualified domain result for a substantive correctness or protection claim. A satisfaction answer can report the participant's experience; it cannot alone establish that the decision followed the governing rule.

#### ADM.15:4.3 - Make timing, counts and comparisons interpretable

For each chosen quantity, recover the subject, unit or category, observation period, inclusion rule and source. Ratios need a numerator and denominator; durations need a start, end and treatment of unfinished cases. OPS.15 supplies this observation discipline.

For the laboratory shorthand `T+N`, choose the start T for the receiving question. A recipient's need-to-result delay begins at that person's observed or reported onset of need; registered handling begins when the identified request enters the service's register. Name the selected event, its source and its supported time or interval. Keep the time of a report separate from the onset it reports. If the question instead concerns delay after a request became eligible or an action became permitted, identify the applicable rule, relevant facts and event that met its condition. A reported need alone does not establish that condition.

Define the usable ending condition and the evidence for its time. State the time unit and calendar; retain a missing time as unknown or as a supported bound. For an unprovided result, report elapsed time to a stated observation cutoff with its unfinished status. N measures elapsed time, not the sum of provider and recipient labor.

For a constructed access example, the owner wants to see how much delay a registered-handling report leaves outside its scope. Use elapsed hours on a 24-hour calendar; all dates are in October 2026 and all times are UTC+03:00. In an interview at 16:00 on 5 October, Noor reports that the need for document D began between 09:00 and 10:00 that day. The portal log records registration at 09:00 on 6 October. The selected usable end is the first confirmed successful read under Noor's valid grant: a test with Noor and the archive log establish it at 12:00 on 7 October.

| Duration question | Selected start and source | Elapsed time to that usable end |
| --- | --- | --- |
| Need-to-result | Noor's reported onset, 5 October 09:00–10:00, retained separately from the interview's 16:00 timestamp. | 50–51 hours, conditional on that reported onset interval. |
| Registered handling | Portal registration, 6 October 09:00, from the request log. | 27 hours; the 23–24 hours from reported need to registration are outside this clock. |

If this request's earlier need time were unavailable, the account would retain 27 registered hours and an unknown need-to-result duration; it would not turn unobserved earlier time into zero. If the access test instead established that provision was still unfinished at the 7 October 12:00 cutoff, the account would show 50–51 hours since the reported need and 27 hours since registration, both to that cutoff. Neither would be reported as a completed-result duration.

A shorter N is useful only alongside the relevant correctness, protection, recovery and effort conditions. Moving waiting outside the portal's clock is not evidence of shorter whole-service delay. The aspiration of immediate provision does not establish that zero delay is feasible or preferable for every service.

Align definitions and conditions before comparing arrangements or periods. Preserve material differences in case mix, eligibility, staffing, concurrent changes and missing observations. Recalculate on a common basis when the source permits; otherwise state the narrower comparison.

#### ADM.15:4.4 - Obtain or reuse proportionate evidence

Begin with existing case records, provider effects, qualified checks and participant observations. Match their scope and time to the current question. A recent report can contain old data; two records can repeat the same omission.

Obtain a missing observation only when its attainable answer can change the decision or a required claim enough to warrant collection and participant burden. Use permitted sources and avoid exposing identities unnecessarily.

Keep a walkthrough estimate, observed count, participant report, forecast and causal explanation distinct. [OCE.13][OCE] supplies the corresponding consequence comparison. A causal claim requires its actual causal method and domain evidence; a before/after display or plausible story does not supply that result.

#### ADM.15:4.5 - Compare the consequences and return an actionable conclusion

State what improved, worsened, stayed unchanged or remains unknown for the affected participants. Preserve valid restrictions and obligations before comparing optional gains. A shorter queue does not compensate for a protected condition by arithmetic.

For a financial choice, use [OPS.14][OPS] with the actual alternatives and horizon. Freed capacity has a financial consequence only through the relevant avoided payment, supported additional use or other qualified receiving account. A revised forecast does not grant spending authority.

Return the supported comparison and its limits to the authorized decision maker. A precise defect may justify a bounded repair while a broader effectiveness claim remains unresolved. Use ADM.14 for a control question, ADM.11 for a provider join or ADM.16 for a warranted transition.

Stop collection when unresolved detail cannot change this use and no other actual decision, assurance or recovery use requires it. Reopen only the affected claim when the population, rule, promise, evidence or arrangement changes.

### ADM.15:5 - Archetypal Grounding

#### ADM.15:5.1 - The portal reports closure and misses twenty requests

For a constructed weekly account, a service owner identifies 100 distinct access requests from the portal, help channel and a bounded requester follow-up. Repeated attempts are linked to their original request. The account's cutoff is the requested-use date for this cohort.

Eighty requests reached the portal. Sixty received the promised usable access. Ten received refusals; a qualified case review under policy P establishes that six followed P and four were mistaken. Ten entered requests remained unprovided at the cutoff. Twenty additional requests encountered entry failure and never reached the portal; their eligibility and possible eventual outcomes are not established by that failure.

| Observed group | What the account supports |
| --- | --- |
| 60 with usable access | Confirmed provision for those requests under the examined conditions. |
| 6 refusals consistent with P | Correct negative dispositions; the requested access was not supplied. |
| 4 refusals contrary to P | Specific handling defects with their applicable correction or remedy. |
| 10 entered but still unprovided | Open outcomes requiring their own timing, reason and next-action account. |
| 20 entry failures | A material omitted population; failed entry does not itself prove ineligibility. |

A report of 70 closed portal requests out of 80 is arithmetically consistent with the local closure convention. It does not establish 70 usable results or whole-population success. The broader evidence supports 60 confirmed provisions and six correct refusals as different result kinds.

The service owner can act on the four established mistaken refusals through the applicable case procedure and investigate the entry failure affecting the omitted group. A new general cost study is unnecessary for those bounded responses. The evidence still does not establish that the portal caused every failure or that the next cohort will have the same proportions.

#### ADM.15:5.2 - Freed provider time and additional applicant work

A walkthrough compares two feasible handling arrangements for the same stated expense class. Its scoped estimates are 10 provider minutes and 3 applicant minutes per case in the current arrangement, versus 6 provider minutes and 9 applicant minutes in the proposed self-service arrangement.

Under that estimation basis, provider effort falls by 4 minutes while applicant effort rises by 6. The estimated combined labor rises from 13 to 15 person-minutes. This sum is meaningful only for the declared labor boundary and compatible units; it is not elapsed service time or a financial net benefit.

Suppose no staffing payment changes within the decision horizon. The freed provider time may still be useful for another supported service, but it is not automatically a cash saving. OPS.14 asks what actual payment or displaced use changes. The authorized owner compares that consequence with applicant burden and the service's required conditions.

These are walkthrough estimates, not observations of an implemented change. If a material uncertainty remains and a feasible observation could change the decision, the owner selects that inquiry. Adequate existing evidence can instead justify retaining the current arrangement.

### ADM.15:6 - Bias-Annotation

The provider's boundary and successful cases tend to dominate reporting. Include relevant non-entry, refusal, unfinished work and recovery before treating a local indicator as the service's result.

The observer can also collect excessive detail or convert every uncertainty into a study. Bound collection by the actual decision and retain supported local action even when a wider claim remains unknown.

### ADM.15:7 - Conformance Checklist

**Recognition.** The account names the decision, institutionally defined result, observed population and material consequences for affected participants. It distinguishes usable provision, correct refusal, uncertainty, elapsed time, labor and financial effect.

**Assurance for reliance.** Trace a decision-bearing count or duration to its actual population and source, including a consequential omitted or unfinished case. Check comparability and the qualified basis of correctness claims. Obtain stronger domain, forecasting or causal evidence only for the stronger claim actually being made.

### ADM.15:8 - Common Anti-Patterns and How to Avoid Them

**Closed requests define success** erases unusable provision and legitimate versus mistaken refusal. Report the result kinds the decision needs.

**The clock starts when the queue sees it** hides earlier service waiting. Use the receiving boundary and state excluded time explicitly.

**Minutes saved are money saved** skips the actual payment or use consequence. Apply the financial comparison for the real horizon and alternative.

### ADM.15:9 - Consequences

The decision maker can retain an observed benefit, correct a specific loss and limit an unsupported claim without treating the whole service as one success or failure. Participant effort and unresolved outcomes become visible where they affect the choice.

The cost is reconstructing a sufficient observation boundary and, sometimes, obtaining qualified correctness evidence. The result can remain partial. A truthful bounded comparison is more useful than a precise aggregate that answers another question.

### ADM.15:10 - Architectural Rationale

Administrative consequences attach to different subjects: the recipient's condition, a decision's correctness, a restriction, a person's work and a financial account. Their correspondence supports comparison, but it does not make their measures interchangeable. Keeping those subjects and the receiving decision explicit prevents one convenient indicator from deciding the service's worth.

### ADM.15:11 - SoTA-Echoing

The working question is whether an administrative arrangement supplies its institutional result with acceptable consequences for the affected participants. The May laboratory's T+N discussion and the dependent ADM source pack contribute the delay question and its reliability and burden conditions. [OPS.15:4.2–4.3][OPS] supplies the operational start, end, source and uncertainty discipline used in §4.3. Compare delay, reliability and participant burden for the work the service enables. The historical aspiration of immediate administration is not adopted as a universal objective.

The selected method uses [OPS.12–15][OPS] for burden, commitments, financial comparison and observation, together with [OCE.13][OCE] for bounded consequence claims and actual causal-use limits. The TameFlow sources contribute through those qualified operational instructions rather than a universal profit or single-metric rule.

A dashboard of completed requests is the serious cheaper alternative and can answer a completed-request question. It fails for the broader service when entry failures, mistaken refusals or shifted effort change the decision. Sections 4.1–4.5 therefore preserve the actual population and unlike consequences. The [2025 shared-service cost review's author-institution abstract][SSC] also cautions against a general cost-reduction conclusion from weak or unclear company-wide baselines; its full article is not used here.

Reopen only the affected comparison when the rule, population, service boundary, evidence or receiving decision changes. The constructed counts and estimates demonstrate interpretation; they do not establish organizational effectiveness.

### ADM.15:12 - Relations

ADM.1 distinguishes the enabled work and administrative condition. ADM.7–10 supply relevant correctness, permission, effect and reconciliation results, while ADM.13 keeps needed grounds recoverable.

[OPS.12–15][OPS] and [OCE.13][OCE] supply the actual consequence and measurement instructions. The authorized owner uses the resulting evidence to repair a control through ADM.14, a provider join through ADM.11 or a selected arrangement through ADM.16.

### ADM.15:End

## ADM.16 - Change an Administrative Arrangement Without Losing Open Cases

**Type:** Architectural

**Status:** Stable

### ADM.16:0 - Use this when

Use this pattern when evidence supports a decision about retaining or changing an administrative arrangement, and existing cases, grants, obligations or records could be affected. A new allowance policy, provider or portal can leave earlier requests governed by different conditions.

Start with the actual decision and one affected case whose treatment could change. The first useful result is a warranted retention decision, an authorized transition with usable case dispositions, or a bounded proposal and the missing competent decision. A proposed change is not an adopted rule or completed migration.

Use the current arrangement directly when adequate evidence supports continuation under its applicable authority. A new trial is unnecessary for that conclusion. This pattern is not needed to process an ordinary request under an adequate existing instruction.

### ADM.16:1 - Problem frame

The practitioner is considering or implementing a change to a policy, control, provider arrangement, handling instruction or supporting system. These objects can change separately. A revised form does not necessarily change the institutional rule; a rule change may require changes in several providers and records.

Open work can depend on several effective regimes. The relevant grouping may follow the date of an authorization, the date an obligation arose, a participant's valid election or another condition supplied by the transition decision. Submission date and software version are not universal cohort rules.

The policy owner or other competent participant decides the institutional change. The service owner and providers arrange its actual application and recovery. Preparing the proposal, authorizing it, performing the change and establishing later usable provision remain different results.

### ADM.16:2 - Problem

A service switches to a new form or rule and treats every visible request as new. Earlier promises, valid grants, pending effects and disputes lose their governing conditions. Alternatively, the old arrangement is retained indefinitely because nobody identifies which remaining uses actually need it.

Training and publication can create a further illusion. Staff have received the new instruction, but later handling does not distinguish an ordinary case, a legitimate old-regime variant and an erroneous workaround. A successful rehearsal is then reported as established independent retention.

### ADM.16:3 - Forces

| Force | Tension |
| --- | --- |
| Improvement | A proposed gain can justify change, while adequate current practice may be the better continuation. |
| Institutional continuity | Existing cases can retain different conditions until an authorized decision actually changes them. |
| Operational feasibility | A valid policy needs capable providers, usable instructions and supported coexistence or recovery. |
| Historical use | Stopping new requests differs from ending obligations or disposing of records. |
| Learning | Publication and coached success can support change without establishing later independent use or its cause. |

### ADM.16:4 - Solution

#### ADM.16:4.1 - State what could change the continuation decision

Recover the current arrangement, observed consequences, relevant commitments and protected conditions. Use ADM.14–15 results when they answer the live control or consequence question.

Compare retention with the material feasible change. If the current arrangement already meets the relevant conditions and the proposed gain does not warrant its burden, the authorized decision maker can retain it on adequate existing evidence. Do not commission a new trial merely to justify continuing what is already supported.

For a change proposal, identify the actual object and intended difference: rule, control, provider, instruction, record or software. Use [ME.15][ME] only when maintaining an actual method variant or repertoire is the question. Changed wording, technical support or institutional authority does not by itself establish a new method.

#### ADM.16:4.2 - Recover affected uses and institutional conditions

Identify the materially different open and foreseeable case groups, active grants, obligations, unresolved effects, disputes and required historical uses. Use actual dependency evidence as well as current traffic; a quiet week does not establish absence of infrequent use.

For each action-changing group, recover the old conditions, intended new result, relevant authority and the fact that will determine its treatment. Preserve an unknown cohort classification when that determining fact is unavailable.

Use ADM.2–3 for a live relation or effectivity question and ADM.13 for required record use. An inventory label is not evidence that a grant expired, an obligation ended or a disputed claim was resolved.

#### ADM.16:4.3 - Obtain the competent transition decision

The authorized owner decides whether to adopt the institutional change and which conditions apply to which cases. Obtain the qualified legal, tax, contractual, security or other contribution only where that substantive question matters and is not already adequately answered.

State the actual effective conditions and any permitted election, exception, coexistence or termination. Neither automatic retroactivity nor universal preservation of old terms is assumed. Apply the supplied transition rule to the actual case facts.

Keep a proposal, received decision and implementation distinct. Until a valid decision changes an existing condition, the handler continues to apply the condition that governs that case. An internal forecast or deployment date does not revise a participant's right or obligation.

#### ADM.16:4.4 - Make one authorized next increment executable

The service owner arranges the providers, supported instructions and records needed for the selected transition. Name the source and receiving conditions, affected participants, actual action, required permission, completion evidence and recovery boundary.

Use [SYSE.29][SYSE] when technical provision changes or is retired. Retaining an old path, restoring an executable, restoring data and repairing forward have different conditions. A rollback option is usable only if it preserves the relevant state and obligations.

Explain the change where participants act. Give the applicable instruction, the fact that selects it and the competent support return. A notice or training invitation does not supply the new provider capability.

Preserve independent unaffected work. For an uncertain payment or other consequential effect, recover what already occurred through ADM.9–10 before repeating, converting or discarding the attempt.

#### ADM.16:4.5 - Establish the receiving use and its important failure branch

For an actual transition into changed provision, perform the bounded trial or clearly labelled rehearsal required by its governing method before widening reliance. Include the relevant old state, new ordinary case, legitimate variant and partial or unresolved effect.

The receiving participant must obtain the promised condition; a successful conversion job alone is insufficient. Identify the observation that would stop expansion or require repair, and who can authorize the corresponding continuation.

When the remaining question concerns staff handling the administrative cases independently or retaining that ability later, name the handling practice, staff, applicable rule and interval. State the behavior the evidence must establish: correct ordinary disposition, recognition of the relevant legitimate exception, and return of a genuine unresolved condition to its competent owner.

Reuse adequate existing observations within their scope. Select a new observation only when its attainable result could change the decision or warranted claim enough to justify the work and burden. Publication, attendance and coached performance retain their actual evidence value; they do not automatically establish independent later handling or a causal improvement.

Here the named population and interval, independent-use evidence, supported continuation and selective inquiry are an administrative adaptation of [ME.17][ME] §§4.1 and 4.4. ME.17 itself governs Method Engineering practice. Use it directly when the question concerns how method engineers transmit or retain their practice of constructing, checking or revising methods; apply the administrative instruction above to staff handling the cases.

#### ADM.16:4.6 - Complete the selected scope and retain honest residual work

Apply the authorized disposition to each materially different remaining use: continued bounded support, qualified transfer, an adequate outside result or an authorized end with its consequences understood.

Separate cessation of new requests, withdrawal of a served interface, ending an undertaking, restricting access and disposing of records. ADM.13 supplies the record-use question. A disabled button or quiet queue does not establish that every obligation and historical use has ended.

Return the actual completed change, supported continued uses, unresolved cases and next responsible action. Reopen the smallest affected condition when later evidence defeats the transition basis. A remaining local gap need not invalidate unaffected provision, but it must not be reported as completed migration.

### ADM.16:5 - Archetypal Grounding

#### ADM.16:5.1 - An allowance begins while earlier journeys remain open

A service owner proposes replacing receipt-by-receipt handling with a travel allowance. The authorized expense-policy owner, using the needed qualified inputs, adopts the following transition for this constructed case:

- Journeys authorized before 1 November retain the earlier receipt-based terms.
- Journeys authorized from 1 November use the specified allowance.
- A pre-November journey may use the allowance only through a recorded election before disbursement, with the confirmation required by the adopted transition rule.
- Existing unresolved payment effects and disputed claims retain their applicable recovery and record conditions.

The proposal alone supplied none of these permissions; the stated owner decision does. The service owner must now arrange actual handling.

| Case | Applicable continuation under the supplied decision |
| --- | --- |
| Journey authorized on 28 October, performed on 3 November, claim submitted on 6 November | Use the earlier terms unless the permitted election is actually established. The submission date does not select the new regime. |
| Journey authorized on 2 November | Use the allowance instruction with its actual eligibility and payment conditions. |
| Earlier journey with a valid recorded election and required confirmation before disbursement | Apply that authorized variant; it is not an erroneous workaround merely because the ordinary earlier terms differ. |
| Authorization date or election basis cannot be established | Recover the specific missing decision or fact through the competent source. Do not infer it from the form's version. |
| Payment instruction already issued, effect unknown | Recover that attempt's effect before another payment or a conversion that could duplicate it. |

The provider's initial proposal disables the receipt route on 1 November. The case comparison shows that the route still serves an authorized population. The responsible parties arrange bounded old-regime support or a qualified replacement that preserves its required inputs, decisions and recovery. They do not infer indefinite retention of the whole old platform.

A receiving-use trial exercises one old-regime claim, one new-regime claim and the relevant election or unknown-effect branch. The trial's actual observations qualify those uses; they are not replaced by a green data-import status. Historical grounds and active disputes remain retrievable under ADM.13.

#### ADM.16:5.2 - Retention is supported, while a new staff claim needs evidence

Suppose adequate current observations show that two handlers apply the adopted authorization-date rule, recognize its permitted election and return an unknown decision to the issuing office without the instruction's author choosing the answer. For continuation with those handlers under the same conditions, the responsible owner can use that evidence and retain the arrangement.

Now a different receiving use requires a new relief handler to work independently. Existing attendance at a presentation does not answer that question. A bounded practice exercise is feasible before the assignment, and its result can change the supported work the handler receives. The maintainer selects an equivalent case that preserves the old/new-regime distinction and the applicable return, and observes the handler's unaided disposition.

A correct result supports that observed application with the available instruction and prior preparation. It does not isolate the cause of success or establish long-term retention. An error selecting by submission date calls for a focused correction to the instruction, support or learning contribution that actually failed. A legitimate election under the transition rule must remain distinguishable from that error.

If the present decision only concerned the two already supported handlers, the new exercise would not be required merely to populate a training report.

### ADM.16:6 - Bias-Annotation

Change advocates can privilege the new arrangement's visible users and overlook old cases, disputes or infrequent recovery. Defenders of the old arrangement can treat every reference to it as a live dependency. Recover the actual use and its governing condition.

The pattern also guards against treating staff compliance or repeated use as proof of independent understanding. Name the behavior, population and interval the evidence actually covers.

### ADM.16:7 - Conformance Checklist

**Recognition.** The result identifies retention or the actual changed object, the competent decision, affected case conditions, executable provider actions and residual uses. It distinguishes proposal, authorization, performance and later evidence.

**Assurance for reliance.** Apply the transition to the relevant old, new, permitted-variant and unresolved-effect cases. Establish actual receiving use and the recovery boundary required by the selected change. For an independent-handling or retention claim, use observations that test that claim in the named population and interval; reuse adequate current evidence without manufacturing another experiment.

### ADM.16:8 - Common Anti-Patterns and How to Avoid Them

**New form, new terms for everyone** changes institutional conditions through a software date. Apply the actual authorized cohort rule.

**The old queue is empty, so everything can be deleted** confuses present traffic with remaining obligations and record uses. Give those uses their own supported disposition.

**Training happened, so the practice is retained** substitutes an event for later independent behavior. State and test only the claim the receiving decision needs.

### ADM.16:9 - Consequences

An organization can improve an arrangement while keeping open cases, effective permissions and historical grounds intelligible. Adequate current practice can also continue without unnecessary trial work.

The cost is temporary coexistence, qualified recovery or additional support where the transition actually needs it. Some uses can remain unresolved. The result states their real disposition instead of declaring universal migration success.

### ADM.16:10 - Architectural Rationale

Changes to rules, instructions, providers, records and technical systems have different effects on current work. An authorized transition connects those changes through the conditions governing actual cases. Separating continuation evidence from change performance also prevents a sound decision to retain practice from becoming an invented intervention.

### ADM.16:11 - SoTA-Echoing

The working question is how an administrative arrangement changes without losing the conditions that govern open work. The laboratories and ADM source pack distinguish changes to rules, service instructions and performed work. Evaluate the changed service by the work it enables and the burden it places on participants.

The selected synthesis uses [SYSE.29][SYSE]'s actual-use, coexistence, receiving-result and retirement instructions, with ADM's explicit grants, obligations, case cohorts and competent transition decision. [ME.15][ME] preserves the distinction between a method variant and changes to description, support or other governed objects.

[ME.17][ME] supplies source distinctions about a bounded population and interval, independent-use evidence, sufficient continuation and worthwhile inquiry. Section 4.5 adapts them to administrative case handling under the governing rule; ME.17's full method remains a direct return for a Method Engineering practice question. The adaptation preserves the limits on claims of later retention or causal improvement.

A retained arrangement with adequate current evidence is the strongest simpler alternative. A one-date cutover can also suffice when its actual conditions cover every affected use. It fails when authorization dates, valid elections, unresolved effects or record duties still distinguish cases; §§4.2–4.6 preserve those differences.

The historical TameFlow contributions are reused through qualified operations instructions, including revisable readiness and commitments. No universal meeting rule, irreversible commitment or untested cultural effect is adopted. Reopen the affected decision when the rule, population, evidence, capability or actual transition consequence changes.

### ADM.16:12 - Relations

ADM.14–15 supply control and consequence questions; ADM.2–3 establish relevant participants and effectivity. ADM.5 carries the changed reusable instruction, ADM.11 connects providers, and ADM.13 preserves required record uses. ADM.6–10 continue individual cases under their actual conditions.

[SYSE.29][SYSE] governs technical transition and retirement; [SYSE.24][SYSE] answers a still-open complete obtaining choice. [ME.15][ME] supplies the actual method-variant question. Section 4.5 adapts selected [ME.17][ME] distinctions to administrative independent handling; direct ME.17 use concerns Method Engineering practice. These contributions leave the institutional transition decision with its competent owner.

### ADM.16:End

# Sources and direct returns

## First edition

This is the first edition of the **Organization Administration Principles Framework**, with reference code **ADM** and fifteen patterns: ADM.1–11 and ADM.13–16. It offers prospective practitioner guidance for administrative conditions, cases and arrangements under the actual rules of the organization. Its constructed cases explain the instructions; claims about a particular service's effectiveness require that service's evidence.

Cite the framework name, release date and PatternID when the wording or source basis matters. A pattern address continues across editions only while its practical answer continues. The ToC's Part and position locate the current presentation.

Copyright © Anatoly Levenchuk. The original framework text and worked examples are licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). The [licensing notice](https://github.com/ailev/FPF/blob/main/LICENSING.md) states the scope and attribution terms. Referenced third-party works retain their own terms.

### External source states and refresh

Use the following source states when checking a source change or reconstructing this edition's basis. The applied-instruction table and source arguments below name the exact sections, contributions and limits used. The hashes identify the source texts used.

ADM relies on the cited FPF relation, permission, evidence and structure distinctions and on the named OPS, OCE, SIE, SYSE and ME instructions for their stated receiving uses. Those texts remain external to ADM. Removing a needed contribution or changing its meaning can invalidate the corresponding ADM instruction or return; it reopens that use.

| External source text | SHA-256 of the relied-on source state |
| --- | --- |
| [FPF A.6.REL][REL] | `7cc6e809db555cfda2f2d9373614810fff7f4cd411218f94b5a1e3a1315bf89f` |
| [FPF A.2.8.PER][PER] | `c940642c546f44de1e4ec1a139a78fe6757f377ba2a7762d688074f2deaf6bc7` |
| [FPF C.32.MWA][MWA] | `4cc2acb560b37dff68a9f6607b1957d373f4ee3968940d77309d59c032aab4be` |
| [FPF A.10][A10] | `376994b9f2837d55724e83cc9c1b6d798c6f139abbd6adbe01a614c1f3bcfea4` |
| [FPF B.3][B3] | `d9b76ef38ce2f46339fe7bd10bf88a3d77ba499a1497f54ea19009496786748b` |
| [Operations Management][OPS] | `3db33a91206c05eb21b83b51a613e1cbfb73a5925338b95fd968a4e64d548bbe` |
| [Organization Change Engineering][OCE] | `768881ebd8655e9736f49c5d01c53816d22cfb897b8f728c2a6928203b8c9bf4` |
| [Semantic Integration Engineering][SIE] | `24caed612eaec96e21b59062bf6c8e6df081b75485b4a3eea00c8756c4845a31` |
| [Systems Engineering][SYSE] | `d82c411414e50a001fa9f018b1b8c1039e701435e8cf1b6d8242b229ffed7b87` |
| [Method Engineering][ME] | `c7f791f9f6f7ef9899f287335204a2727e35a4bf4a54b611e174c9f79dd5076c` |

A changed source file calls for comparison of the relied-on sections. Unchanged contributions remain usable within their conditions. If a needed external instruction or its source cannot be recovered, retain the exact missing contribution and continue only the questions that do not depend on it. A citation supplies neither the organization's rule nor permission to act.

Revisit an affected pattern when a real use exposes an unclear action, a missed case, unsupported evidence or an excessive burden. Revisit the connected explanation when an individual result no longer supports the next question it promises to answer. A changed source meaning, organizational rule, population or operating condition reopens only the claims that depend on it. The relevant pattern's source return and stopping conditions identify the first place to work.

## Applied framework instructions

The cited methods retain their own scope. Use the named contribution when it answers a live question; the citation is not a requirement to read every framework before handling a request.

| Source | Contribution used here |
| --- | --- |
| [FPF A.6.REL — Relation Obtaining and Individuated Relation Occurrences][REL], §§4.2–4.7 | Readable relation use; obtaining versus assertion; occurrence identity only for a receiving use that needs to distinguish episodes; relation change versus description change. ADM.2–4 apply these distinctions to the actual administrative rule and facts. |
| [FPF A.2.8.PER — Granted Permission, Exercise and Non-Prohibition][PER], §§4.1 and 4.3–4.6 | Keep a grant, its exercise and a non-prohibition finding distinct; apply a matching conflict rule or adequate resolving decision before returning a genuine gap. ADM.2 and ADM.8 apply these distinctions to the named administrative action. |
| [Operations Management][OPS], OPS.3–6, OPS.8 and OPS.12–15 | OPS.3–4 distinguish operating subjects and usable claims; OPS.5–6 supply admission and continuation. OPS.8 supplies receiving-action readiness and operational joins. OPS.12–15 supply burden, promises, financial comparison and observations for the actual decision. Administrative eligibility, authority and fulfillment rules remain explicit inputs. |
| [FPF A.10 — Evidence Graph Referring][A10], §§4.1–4.2 and 4.5–4.6; [B.3 — Trust and Assurance Calculus][B3], §§4.1–4.2 | A.10 recovers the exact claim, source and bounded reliance without supplying the domain result. B.3 is used only for an actual named assurance claim; consequence alone does not create one. ADM.7 retains these limits. |
| [Organization Change Engineering][OCE], OCE.6 and OCE.13 | OCE.6 supplies an effective assignment for its organizational-change question. OCE.13 supplies bounded consequence comparison, population and evidence distinctions, and the limits of a descriptive or causal claim. Adequate results are reused within their actual scope. |
| [Semantic Integration Engineering][SIE], SIE.4–6 | Supplies alignment, cross-source identity and claim composition when the administrative accounts cannot be combined directly. |
| [FPF C.32.MWA — Practice-Architecture Synthesis from Several Structures][MWA] | Compares several structures when their differing boundaries or relations change the practice decision. |
| [Systems Engineering][SYSE], SYSE.24 §§4.1–4.9 | Compares complete obtaining arrangements for a project result. Adequate administrative permissions, responsibilities and provider conditions are inputs; the choice does not itself perform the later provision. |
| [Systems Engineering][SYSE], SYSE.26 §§4.1–4.5 and SYSE.28 §§4.1–4.5 | SYSE.26 supplies supported interaction, usable result and recovery of uncertain effects. SYSE.28 supplies check placement, condition-bound reuse and distinct outcomes. ADM.7 and ADM.9 use these results without requiring control or platform redesign for each case. |
| [Systems Engineering][SYSE], SYSE.8–9 and SYSE.29 | SYSE.8 develops provider arrangements with distinct contributions and undertakings; SYSE.9 uses adequate expert results or qualifies worthwhile missing contributions. SYSE.29 supplies actual-use transition, coexistence, recovery and retirement. ADM.11, ADM.14 and ADM.16 connect these results to institutional conditions. |
| [Method Engineering][ME], ME.15 and ME.17 §§0, 4.1 and 4.4 | ME.15 distinguishes actual method variants from changed descriptions, support or other governed objects. ME.17 governs Method Engineering practice. ADM.16:4.5 adapts its population, interval, independent-use, supported-continuation and selective-inquiry distinctions to administrative case handling, retaining their evidence limits. Direct ME.17 use concerns a Method Engineering culture question. |

## Administrative and representation sources

The following source arguments shaped the working distinctions. The constructed cases in this publication are applications of those distinctions with supplied facts; they are not reports of observed ADM deployments.

### Administration laboratories and synthesis

The dated laboratory transcripts and ADM-Lab synthesis are working source materials with no public full-text return supplied in this edition. The following accounts give their selected contributions, original locators and limits; the receiving ADM instructions are available in this publication.

- **Administration laboratory, 1 July 2023.** The transcript, especially 11:56–14:59 and 20:37–30:49, distinguishes the journey, work at the destination and administrative case; 30:52–42:21 develops participant and payment descriptions. ADM.1 and ADM.4 retain the subject and participant distinctions; ADM.9–10 connect them to usable provision and reconciliation. Reported situations and proposed ontologies do not establish universal administrative laws.
- **Administration laboratory, 27 May 2023.** The transcript, especially 14:53–19:40, 49:40–64:24 and 69:14–77:50, connects controls to their purpose, distinguishes relation state from records, and examines usable provision. ADM.2–3 retain the action-changing rule and record distinctions; ADM.6–9 apply the competent-check, permission and usable-provision questions. The T+N discussion at 69:14–77:50 supplies ADM.15's qualified elapsed-delay question.
- **Administration laboratory, 17 June 2023.** The transcript, especially 44:18–56:43 and 62:15–78:22, separates developing a service from using it and connects substantive judgments, execution and exception resolution. This supports the Preface's design/handling distinction, ADM.2's competent return and ADM.5–6's reusable instruction and exception resolution. ADM.11 and ADM.13–16 extend the corresponding provider, record, control and transition questions.
- **ADM-Lab source pack v0.1, 15 July 2026.** The synthesis, especially §§13–21 and 23–27, qualifies the earlier discussions. Section 15 supports the same-subject/participant-account comparison; §§20.1–20.2 propose the T+N delay question and qualify speed by reliability and participant burden. ADM.15 uses OPS.15:4.2–4.3 to make the selected start, usable end, source and time uncertainty recoverable. This is a dependent synthesis and authorial clarification, not independent corroboration.

### Enabling provision and decision accounts

The administrative contribution is to make the organizational condition support the participant's intended work and to examine the burden of obtaining that support. The accounting contribution is to choose an account that answers the operating decision while retaining accounts required for other purposes. ADM.1, ADM.9 and ADM.15 make the enabling result and participant burden explicit; [OPS.14–15][OPS] supply the financial comparison and observation methods used here.

### Accounting representations and TameFlow

- **Partridge and colleagues, Thoroughly Modern Accounting: Shifting to a de re Conceptual Pattern for Debits and Credits, 2018.** Published in *Advances in Conceptual Modeling, ER 2018*, LNCS 11158, pp. 134–148; [public bibliographic record and abstract][PARTRIDGE-A], DOI 10.1007/978-3-030-01391-2_20. The consulted preprint, PDF pp. 9–10 and 13–14, figures 7–8, supports the comparison of participant-relative and common representations and transaction direction. ADM.4 and ADM.10 adapt the representational contribution after event identity is established, while fulfillment remains governed by the actual obligation. The record identifies the work; its full-text download is restricted.
- **Partridge and colleagues, Ontology then Agentology, 2018.** The [paper][PARTRIDGE-B], especially PDF pp. 5–8, table 2 and figures 2–4, distinguishes the common represented subject from an actor's position and meaning. ADM.2 and ADM.4 retain the useful correspondence. The conceptual examples do not establish empirical superiority of one database or require adopting the complete source ontology.
- **Tendon and Doiron, Tame your Work Flow, 2020; Tendon, The Book of TameFlow, version 17 January 2022.** The consulted 2020 book, chapters 6–8 and 21, and the consulted 2022 book, chapters 15–16 and chapter 17 pp. 267–276, supply historical operating arguments about readiness, commitment, financial contribution and recurring problems. ADM.11 and ADM.15–16 use the qualified OPS instructions rather than universal single-metric, fixed-cost or cultural-effect claims. [OPS.14–15][OPS] supply the financial comparison and observation methods used here. Public returns are the publisher's [Tame your Work Flow catalogue page](https://leanpub.com/workflow) and [The Book of TameFlow page](https://leanpub.com/tameflow). The first is retired from sale; the second presents the continuing edition. These pages identify the works; the chapter and page locators above refer to the consulted editions.

### Using operational accounts

Use an account suited to the operating decision, relate workload and capacity to financial consequences, and refresh assumptions when the decision changes. Preserve other accounts for their respective purposes. [OPS.14–15][OPS] describe the corresponding comparison and observation methods.

For ADM.15, use the relevant receipts, payments, time and participant burdens on the declared comparison basis. This qualified reuse supplies no universal monetary objective, no rule that all allocated cost is useless, and no general equivalence between ROI or ROMI and a customer-value-to-acquisition-cost ratio. A cash comparison uses its declared incremental receipts and payments; a broader investment or customer-value claim requires the applicable finance or accounting method.

## Bounded current comparisons

[GOV.UK's Service Standard, point 2][GOVUK] supplies the whole-problem service comparison used in ADM.1 and ADM.11. Its user-problem boundary is useful here; it does not establish the authority, applicability or outcome of a local administrative service.

[NIST SP 800-63-4, Digital Identity Guidelines, July 2025][NIST], particularly its digital-identity model and Redress section, distinguishes identity proofing, authentication and federation and supplies bounded issue-handling and correction guidance. ADM.2 and ADM.6–7 retain the distinction between the needed identity result and a separate eligibility or permission condition. The federal digital-identity scope does not determine local entitlement.

[OMG CMMN 1.1, 2016][CMMN], §§4.1–4.3, supplies the case-outcome, information and model/execution comparison used in ADM.5–6. It does not supply institutional authority or imply CMMN conformance here.

[OASIS XACML 3.0, 2013][XACML], terminology and §7.2, supplies the policy-decision/enforcement comparison in ADM.8 and ADM.14. Its enforcement obligations are operations within that architecture; they are not imported as general legal duties.

[ISO 15489-1:2016][ISO]'s public abstract supplies the records, metadata, responsibilities, business-context and controls comparison in ADM.13. The full paid standard and its individual clauses were not inspected; the abstract supplies no local retention period or compliance conclusion.

[Goth, Catala-Perez and Hedderich's 2025 shared-service cost review][SSC] is used through its author-institution abstract. Its qualified concern about weak or unclear company-wide financial baselines limits a general administrative-cost-reduction claim in ADM.15. The full article was not read; the finding does not establish that shared services never save cost.

[REL]: ../FPF-Spec.md#a6rel---relation-obtaining-and-individuated-relation-occurrences
[PER]: ../FPF-Spec.md#a28per---granted-permission-exercise-and-non-prohibition
[MWA]: ../FPF-Spec.md#c32mwa---practice-architecture-synthesis-from-several-structures
[OPS]: OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md
[OCE]: ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md
[SIE]: SEMANTIC-INTEGRATION-ENGINEERING-PRINCIPLES-FRAMEWORK.md
[SYSE]: SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md
[PARTRIDGE-A]: https://biblio.ugent.be/publication/8577441
[PARTRIDGE-B]: https://www.scitepress.org/papers/2018/66063/66063.pdf
[GOVUK]: https://www.gov.uk/service-manual/service-standard/point-2-solve-a-whole-problem
[NIST]: https://pages.nist.gov/800-63-4/sp800-63.html
[A10]: ../FPF-Spec.md#a10---evidence-graph-referring-claim-bound-evidence-and-provenance-graph
[B3]: ../FPF-Spec.md#b3---trust-and-assurance-calculus
[CMMN]: https://www.omg.org/spec/CMMN/1.1/PDF
[XACML]: https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html
[ME]: METHOD-ENGINEERING-PRINCIPLES-FRAMEWORK.md
[ISO]: https://www.iso.org/standard/62542.html
[SSC]: https://forschung.hs-ansbach.de/de/publikationen/1447-shared-service-centers-sscs-and-administrative-cost-reduction-a-systematic-review-and-research-agenda
