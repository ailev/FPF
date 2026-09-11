# Corporate Finance Principles Framework

**Edition:** [FIN 1.0](#edition-record)\
**Author:** Anatoly Levenchuk, with AI-assisted development and review

Methods for valuing investments, arranging finance, preserving liquidity, managing financial exposure and making corporate-finance decisions.

# Table of Contents

**Reader entry**

| § | Publication unit | Use |
| --- | --- | --- |
| — | [Corporate Finance Readme](#corporate-finance-readme) | Enter through a financial question. |
| — | [Preface](#preface) | Understand the language and how its methods connect. |
| — | [References](#references) | Find supplying editions, source guidance and citation information. |

**Part A - Cash and decision accounts**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [FIN.1 - Frame the Corporate Finance Decision, Corporation, Jurisdiction, and Time](#fin1---frame-the-corporate-finance-decision-corporation-jurisdiction-and-time) | | financial question; corporation; jurisdiction; horizon | FDM and C.11.DUA when needed |
| 2 | [FIN.2 - Recover Cash, Liquidity, and Commitments](#fin2---recover-cash-liquidity-and-commitments) | | cash gap; liquidity; cash forecast; drawable facility | FIN.4; FDM when needed |
| 3 | [FIN.3 - Manage Working Capital and Cash Conversion](#fin3---manage-working-capital-and-cash-conversion) | | working capital; inventory; customer advance; cash conversion | FIN.2; MA and OPS when needed |
| 4 | [FIN.4 - Prepare Accounts and Forecasts for the Finance Decision](#fin4---prepare-accounts-and-forecasts-for-the-finance-decision) | | profit to cash; finance projection; pro forma; forecast | MA and FDM when needed |

**Part B - Investment and value**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 5 | [FIN.5 - Estimate Cost of Capital and Financing Constraints](#fin5---estimate-cost-of-capital-and-financing-constraints) | | discount rate; WACC; equity return; financing constraints | FIN.4; FIN.10 when needed |
| 6 | [FIN.6 - Value Capital Projects](#fin6---value-capital-projects) | | capital project; NPV; opportunity cost; payback | FIN.4–5; FIN.8 when needed |
| 7 | [FIN.7 - Value Assets and the Corporation](#fin7---value-assets-and-the-corporation) | | enterprise value; equity value; DCF; comparables | FIN.4–5; FIN.8 when needed |
| 8 | [FIN.8 - Value Options under Uncertainty](#fin8---value-options-under-uncertainty) | | real option; defer; expand; abandon; binomial | FIN.5; FDM when needed |
| 9 | [FIN.9 - Compare Capital Investments and Allocations](#fin9---compare-capital-investments-and-allocations) | | capital rationing; acquisition; divestment; synergy; price | FIN.6–8; FIN.10–12 and FIN.21 when needed |

**Part C - Financing, distributions and recovery**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 10 | [FIN.10 - Design Financing Instruments and Terms](#fin10---design-financing-instruments-and-terms) | | loan; issue fee; maturity; financing terms | FIN.2; FDM when needed |
| 11 | [FIN.11 - Select Capital Structure](#fin11---select-capital-structure) | | debt equity mix; debt capacity; capital structure | FIN.5; FIN.10–12 when needed |
| 12 | [FIN.12 - Preserve Covenant Headroom and Financing Flexibility](#fin12---preserve-covenant-headroom-and-financing-flexibility) | | covenant; headroom; waiver; refinancing | FIN.2; FIN.10 when needed |
| 13 | [FIN.21 - Decide How Much Capital to Retain or Return](#fin21---decide-how-much-capital-to-retain-or-return) | | dividend; buyback; retain capital; payout | FIN.2; FIN.7, FIN.9 and FIN.11–12 when needed |
| 14 | [FIN.22 - Compare Financial Restructuring and Recovery Routes](#fin22---compare-financial-restructuring-and-recovery-routes) | | financial distress; restructuring; recovery; interim finance | FIN.2; FIN.7 and FIN.10–12 when needed |

**Part D - Exposure and treasury action**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 15 | [FIN.13 - Identify and Measure Financial Exposures](#fin13---identify-and-measure-financial-exposures) | | currency; rates; credit; counterparty; financial exposure | FIN.4; FDM when needed |
| 16 | [FIN.14 - Design Hedges and Financial Risk Transfer](#fin14---design-hedges-and-financial-risk-transfer) | | hedge; forward; swap; partial receipt; residual risk | FIN.13; FIN.2 and FIN.8 when needed |
| 17 | [FIN.15 - Execute Treasury and Liquidity Decisions](#fin15---execute-treasury-and-liquidity-decisions) | | treasury execution; payment; short-term investment; settlement | Selected financial decision; FDM when needed |

**Part E - Advice, renewal and continuing practice**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 18 | [FIN.16 - Prepare a Finance Recommendation and Return It for a Decision](#fin16---prepare-a-finance-recommendation-and-return-it-for-a-decision) | | recommendation; conditional advice; evidence demand | Selected FIN results; C.11.DUA when needed |
| 19 | [FIN.17 - Refresh Financial Models and Data](#fin17---refresh-financial-models-and-data) | | model refresh; changed data; revised forecast | The affected FIN result |
| 20 | [FIN.18 - Develop and Refresh Corporate-Finance Methods](#fin18---develop-and-refresh-corporate-finance-methods) | | method choice; forecast comparison; trial; model improvement | The direct financial method; C.11.DUA when needed |
| 21 | [FIN.19 - Reconcile Simultaneous Corporate-Finance Work Across Claims and Horizons](#fin19---reconcile-simultaneous-corporate-finance-work-across-claims-and-horizons) | | concurrent finance work; shared cash; multiple horizons | C.32.MWA; direct FIN methods when needed |
| 22 | [FIN.20 - Deliberately Continue and Change Corporate-Finance Culture](#fin20---deliberately-continue-and-change-corporate-finance-culture) | | finance culture; forecast use; practice retention | C.36; MA.9 and C.11.DUA when needed |

# Corporate Finance Readme

## Practical entries

These are selected examples, not a catalogue or a coverage boundary. Bring the actual financial question. If no example fits, use the Table of Contents or enter a direct pattern. The patterns are a repertoire: their numbering and Parts do not prescribe an execution sequence.

### FIN-E1 - A profitable order leaves a day-7 cash gap

- **Situation:** An operating account establishes that an order is feasible and brings 1,200 on day 28 against incremental payments of 440 on day 0 and 100 on day 7. The whole-business baseline, after all other flows, has cash of 500 at each relevant date.
- **Question:** Which available arrangement funds the order while preserving the required cash?
- **First useful result or blocker:** The liquidity calculation finds a day-7 gap of 40 before any positive reserve. A response is usable only if its money arrives in time and its later payments remain fundable.
- **Start with:** FIN.2 for the dated cash account, then FIN.3 for the customer-advance alternative or FIN.10 for financing terms. Use FIN.15 for the selected permitted action.
- **Stop or return:** Complete the comparison with a supported choice of an arrangement whose receipts are available in time and whose repayments are fundable, or identify the specific missing condition. Return when collection, reserve, fees, draw access or repayment changes.

The order requires 26–29 rig-hours. The supplied operating plan has 20 usable hours plus an available ten-hour block costing 240. Materials cost 200 and supplier service costs 100. Materials and the block require 440 on day 0; the supplier's 100 is due on day 7. Those adequate operating and accounting results give the 540 of incremental payments and a favorable contribution of 660. Finance can use them directly.

After paying 440, cash is 60. The day-7 payment of 100 creates the gap of 40. A committed facility can supply up to 80 before that payment; it withholds a fee of 3 and requires principal plus interest of 2 on day 28. A gross draw of 43 supplies net cash 40. Alternatively, the customer has agreed to pay 96 on day 6 against 100 of the invoice, leaving 1,100 on day 28.

| Available arrangement | Cash after day-7 payment | Cash after day-28 flows | Incremental gain over the 500 baseline |
| --- | ---: | ---: | ---: |
| Draw 43, then repay 45 | 0 | 1,155 | 655 |
| Receive the agreed advance of 96 | 56 | 1,156 | 656 |

On these conditions, the advance provides one more unit of gain and a larger buffer. Without the customer's agreement, the proposed advance is not available to pay the day-7 obligation. If a positive reserve is required, the zero-cash facility row must change. If collection moves to day 40 but the loan remains due on day 28, its 45 repayment becomes a new gap. A positive total contribution does not establish an extension.

### FIN-E2 - Value a project before arranging its funding

- **Situation:** A project pays 1,000 now and returns 600 at the end of each of two years. These are complete incremental after-tax operating cash flows, with no terminal value.
- **Question:** Does the project add financial value at a matching annual required return of 10%?
- **First useful result or blocker:** FIN.6 gives NPV 41.32 on these grounds. This completes the stated value calculation; it does not provide the initial 1,000.
- **Start with:** FIN.6. Use FIN.5 if the required return is unresolved and FIN.2 if the next question is payment capacity.
- **Stop or return:** Return when cash, timing, risk basis or a competing capital use changes the answer.

### FIN-E3 - A currency hedge meets a partial customer payment

- **Situation:** A customer owes 100 foreign units on day 30. A physical forward requires delivery of 100 foreign units for 90 home units that day, but the customer pays only 60.
- **Question:** What does the hedge protect, and what must treasury now fund?
- **First useful result or blocker:** At spot 0.95 home per foreign unit, buying the missing 40 costs 38 home units. If funded and settled, current net home cash is 52 and the unpaid customer claim of 40 foreign units remains. Unavailable purchase funding is an execution problem.
- **Start with:** FIN.14 for combined exposure and protection, then FIN.15 for the permitted purchase and settlement.
- **Stop or return:** Reassess the remaining claim and future protection after actual performance; a derivative settlement does not settle the customer's separate obligation.

# Preface

## FIN.Preface:1 - Problem frame

Use this language when a corporate-finance analyst, treasurer, CFO or manager must answer a financial question about the corporation's investments, funding, liquidity, exposures, distributions or recovery. It assumes ordinary familiarity with financial statements, amounts, percentages and dates. Additional mathematical, market or institutional knowledge is stated with the methods that need it. It supplies procedures and worked cases for making financial consequences usable in decisions.

The governed field is corporate finance. Investor portfolio selection, prudential banking, a complete legal or accounting manual and the broader economics of exchange are outside this edition. A formal valuation, tax conclusion, regulated action or legal process uses the actual applicable professional requirements when that claim is needed.

## FIN.Preface:2 - Problem

A corporation can be profitable and unable to pay, buy a valuable business at a destructive price, hedge a currency while retaining collection risk, or improve one financial model while creating incompatible commitments elsewhere. The difficulty is often the connection between valid local calculations and the actual choice they are meant to support.

The language addresses those connections without reducing finance to generic advice about “making better decisions”. Practitioners use the analytical methods to calculate dated cash positions and values, compare financing terms, assess exposures, design protection and prepare recommendations. Treasury methods guide permitted financial actions and verification of their effects.

## FIN.Preface:3 - Forces

Financial work balances value, payment continuity, risk, flexibility, control, evidence and limited attention. It must use actual institutional conditions while remaining small enough for a routine decision. A more complete model can be useful, but only when its distinctions can change action or warranted reliance. Uncertainty can justify a range or conditional recommendation without making every question a new research project.

## FIN.Preface:4 - Solution

Enter through the missing useful result. Cash and account methods are FIN.1–4; value and allocation are FIN.5–9; financing is FIN.10–12; retention and recovery are FIN.21–22; exposure and execution are FIN.13–15; advice and continuing practice are FIN.16–20. The Parts group these contributions for reading. A pattern can be used in several combinations.

When combining results, preserve their material common conditions: corporation and claimant perspective, financial positions, baseline, currency and units, valuation and payment dates, tax and risk treatment, and access to the same money or capacity. Do not count one receipt, benefit or available facility twice. A valid set of local calculations may still fail this joint condition.

The acquisition and divestment profile is a bounded use of FIN.9. FIN.7 supplies the interest's standalone value; FIN.9 adds price, combination or separation effects and the remaining business; FIN.10–12 supply financing conditions where needed. This is a financial transaction comparison, not the whole acquisition process.

An adequate supplied result can be used directly. A finance analyst need not reconstruct operating capacity, create a new semantic model or visit every related pattern before calculating. FIN.16 connects completed results to a receiving decision when a direct result is not already enough.

## FIN.Preface:5 - Archetypal Grounding

FIN-E1 supplies the whole first-use case. The operating plan and incremental account are already adequate. FIN.2 exposes the gap hidden by the positive contribution; FIN.3 compares an agreed advance with the available loan; the treasurer uses FIN.15 to perform the selected permitted action. When collection moves to day 40, repayment on day 28 becomes unfunded. FIN.17 helps the analyst reconsider the financing recommendation while retaining unaffected operating grounds.

The language also reaches a different result when the financial question changes. FIN.6 calculates positive project NPV without claiming funding. FIN.9's acquisition has equity value 80, additional benefits 30 and costs 15: a price of 100 gives buyer value −5, while 90 gives +5. FIN.22 compares the same expected recovery at different dates. These constructed cases establish how to apply the methods, not evidence of organizational adoption or measured financial improvement.

## FIN.Preface:6 - Bias-Annotation

The corporation is the usual receiving perspective, but its owners, creditors, employees, customers and providers can bear different consequences. Name those interests and applicable constraints when they change the question. Public-company market evidence may not transfer to a private firm; consolidated accounts may not establish local access to cash; one jurisdiction's financing rule may not apply elsewhere.

All numerical cases are constructed and use the expressly stated terms. They are not quotations of current market offers. Use actual current facts for the corporation's real decision.

## FIN.Preface:7 - Conformance Checklist

Can the practitioner identify the receiving action, corporation and claim perspective? Does each method supply its promised financial result on stated grounds? Do combined results preserve the joint conditions in FIN.Preface:4, including payment timing and shared resources? Are institutional facts sufficient for the claimed action, and are unresolved ones specific? Can another practitioner replay the decisive case and identify a condition that changes it? Are recommendation, decision and execution distinguished where the result crosses those boundaries?

Use each pattern's checklist to examine its narrower claim. A completed direct use does not require evidence for every other pattern.

## FIN.Preface:8 - Common Anti-Patterns and How to Avoid Them

Treating profit as cash hides the first-use gap; use FIN.2. Treating enterprise value as an equity purchase price hides claims and consideration; use FIN.7 and FIN.9. Treating a hedge as a customer guarantee hides the partial-receipt branch; use FIN.14. Treating a new template as improved practice hides actual use; use FIN.20.

Another failure is to turn these corrections into a compulsory chain. Start with an adequate existing question and account, and obtain only the missing contribution.

## FIN.Preface:9 - Consequences

The financial result becomes usable at the place where it can change a decision: the dated shortage, value threshold, price, financing condition, residual exposure or actual settlement. The language also permits a supported continuation or a bounded unresolved condition.

The cost is explicit attention to assumptions, dates and effects that a familiar summary can omit. Preserve that detail when it matters; a routine direct result should remain routine.

## FIN.Preface:10 - Architectural Rationale

The language retains domain procedures because a general choice method cannot calculate cash conversion, discount a project or reconcile an instrument's proceeds by itself. It reuses Management Accounting, Financial Domain Modeling and Operations Management for their independently useful results instead of making them three sections of a larger finance prerequisite.

Separate patterns distinguish value, allocation, funding and execution because the same case can obtain one result and fail another. In acquisition and divestment comparisons, FIN.9 combines supplied valuations with the price, transaction effects and financing conditions. Distributions and distress retain their own questions about claims and feasible capital routes.

## FIN.Preface:11 - SoTA-Echoing

The current professional line used here combines corporate investment and valuation, treasury practice, explicit financial positions and decision-specific accounts. The [CFA 2026 readings][CFA-CAPITAL] contribute finance methods and their comparison limits; [AFP's treasury specification][AFP] contributes the breadth of cash, provider, funding and control responsibilities. A syllabus or task list establishes a professional concern, not proof that one implementation is effective.

[OpenStax's 2026 second edition][OS-STRUCTURE] provides accessible capital-structure and cost-of-capital explanations. The [IVSC overview][IVSC] identifies valuation concerns without supplying the full requirements of a particular engagement. The [World Bank's 2022 workout toolkit][WB-WORKOUT] is a substantive recovery-method source; current local law and actual agreements still determine available routes.

The language adopts these financial contributions and connects them through actual dates, claims, feasible choices and receiving use. It rejects both a finance-only sequence that silently rebuilds all accounting and a generic decision vocabulary that leaves the financial calculation unspecified. Changed professional knowledge, institutional conditions or a case exposing a consequential omission reopens the affected method.

## FIN.Preface:12 - Relations

| Supplying language or method | Contribution used here | When to obtain it |
| --- | --- | --- |
| [Management Accounting, MA 1.0][MA] | Resource and cost accounts, capacity and assignment meanings, reporting–cash reconciliation, purpose-qualified forecasts and account use. | A required accounting result is missing or its meaning is disputed; primarily FIN.3–4, with reuse elsewhere. |
| [Financial Domain Modeling, FDM 1.0][FDM] | Parties, financial positions, conditional instruments, descriptions and actual event effects. | A financial object's meaning or effect is unresolved; particularly FIN.1–2, FIN.8, FIN.10 and FIN.13–16. |
| [Operations Management, 5 September 2026 publication][OPS] | Feasible operating plans, capacity and service consequences. | A financial alternative's operating feasibility is unresolved. |
| [FPF C.11][CHOICE] and [C.11.DUA][DUA] | Choice among available alternatives; appraisal of advice and evidence demands by receiving use. | The local choice or the value of advice or demanded inquiry needs that general method. |
| [FPF C.32.MWA][MWA] and [C.36][CULT] | Several interacting structures of practice; cultural continuation and deliberate change. | FIN.19 or FIN.20 needs the corresponding reusable method. |

These are contribution relations, not a mandatory reading order. Reopen a dependency when its supplying result or the receiving use changes materially; unchanged adequate results remain usable.

# Part A - Cash and decision accounts

## FIN.1 - Frame the Corporate Finance Decision, Corporation, Jurisdiction, and Time

**Type:** Method

### FIN.1:0 - Use this when

A request such as “can we afford this?” or “is this good for the group?” admits several financial answers. Recover the actual choice, paying or benefiting corporation, horizon and constraints before choosing a calculation. If these are already sufficient, enter the needed financial method directly.

### FIN.1:1 - Problem frame

Corporate finance includes value, financing, liquidity, risk and distributions. This pattern governs the financial question being answered within that field: whose choice and consequences are being assessed, at what date, for what use. It does not determine a corporation's legal identity or replace its authority arrangements.

### FIN.1:2 - Problem

An analyst may value an enterprise when the question concerns the price of an equity interest, use group cash for a subsidiary payment, or present an attractive recommendation as if someone had authorized it. Correct arithmetic then answers the wrong question.

### FIN.1:3 - Forces

Keep the first question usable and small while retaining party, time and institutional differences that can change the answer. Respect several affected interests without hiding their conflicts in an unspecified “company benefit”.

### FIN.1:4 - Solution

1. Restate the intended action in ordinary words: for example, pay a supplier on Friday, propose a project, buy a specified interest, refinance a maturity or distribute an amount to owners. Name the receiving decision and the consequence that would make the answer useful.
2. Identify the relevant corporation or entities, affected claims and claimant perspective. The borrower, operating company, seller and shareholder may be different parties. Use [FDM.1–2][FDM] only where the existing account leaves these identities or boundaries unresolved.
3. Fix the comparison baseline, decision and valuation dates, currencies, planning horizon and treatment of inflation and tax. Different horizons can coexist: an eighteen-month investment can be constrained by a six-month covenant.
4. Recover the existing jurisdictional, contractual and authority conditions needed by this action. Use a supplied qualified interpretation when sufficient. If a particular rule or consent is missing, state the dependent uncertainty rather than infer a universal rule.
5. Route the financial work by its missing result: FIN.2 for dated liquidity; FIN.5–9 for value and allocation; FIN.10–12 for financing; FIN.13–15 for exposure and action; FIN.21–22 for payout or recovery. These are selectable contributions, not a compulsory itinerary.
6. State the result's use and limit. An analyst can complete a comparison and prepare a conditional recommendation. The authorized party can decide, and the permitted performer can execute; routine delegated authority may already cover the action.

Stop once the needed method has a usable question and sufficient grounds. Return through FIN.16 when several results or conditions must be combined for the receiver.

### FIN.1:5 - Archetypal Grounding

A subsidiary owes 70 tomorrow and has 40 usable cash. Its parent has 100. The question “does the group have enough cash?” can be answered yes on aggregate, yet the subsidiary is short 30. FIN.2 must assess an actual permitted transfer, including timing and any restrictions. If a valid transfer of 30 is available before the cutoff, the payment path becomes fundable; an ownership chart alone does not establish it. The result concerns tomorrow's subsidiary payment, not the group's enterprise value.

### FIN.1:6 - Bias-Annotation

A shareholder-value question can omit effects on creditors, employees or counterparties. Name material constraints and affected interests explicitly; use the corporation's actual decision basis instead of assuming every financial question has the same objective.

### FIN.1:7 - Conformance Checklist

Can a second practitioner identify the proposed action, receiver, entities, claim perspective, dates, currency, baseline and binding conditions? Is the unanswered institutional question specific enough to obtain a useful answer? Does the conclusion preserve the difference between advice, decision and performance?

### FIN.1:8 - Common Anti-Patterns and How to Avoid Them

Starting with the most familiar model invites a precise answer to a different question; name the action first. Calling all entities “the business” can make unavailable money appear spendable; recover the paying entity. Requiring a complete new ontology for an adequate routine account adds work without changing the decision; use that account.

### FIN.1:9 - Consequences

The practitioner selects the calculation that can change the receiving choice and can explain a bounded limit when a fact is missing. Some initially combined questions become separate, connected analyses.

### FIN.1:10 - Architectural Rationale

Framing is a short correction of subject and use, not a new approval layer. It keeps direct use possible while preventing incompatible financial meanings from being silently combined.

### FIN.1:11 - SoTA-Echoing

[FDM][FDM] supplies the party, position and event distinctions; [C.11.DUA][DUA] connects advice to its receiving question. This pattern applies those contributions before selecting a corporate-finance method. Compared with treating a headline request as a complete specification, it makes the action-changing ambiguity explicit; a changed entity or use reopens the frame.

### FIN.1:12 - Relations

FIN.2–22 supply the selected financial answers. [C.11][CHOICE] helps choose among available alternatives when that comparison is the current question. [C.11.DUA][DUA] helps appraise advice or an evidence demand. Existing authority and specialist legal or tax results remain external inputs.

### FIN.1:End

## FIN.2 - Recover Cash, Liquidity, and Commitments

**Type:** Method

### FIN.2:0 - Use this when

A payment is approaching and a bank balance, profit figure or unused credit limit does not yet tell you whether the corporation can pay. Start with the money and commitments at the relevant dates; obtain a dated funding requirement before selecting a response. A sufficient existing cash forecast can be used directly.

### FIN.2:1 - Problem frame

The treasurer or analyst is preparing a liquidity account for a named paying entity, currency and horizon. A spreadsheet or dashboard describes that account; neither creates cash nor changes the entity's rights. This method recovers usable balances and timed flows. It does not itself choose a capital structure, obtain a lender's consent or execute a payment.

### FIN.2:2 - Problem

A corporation can have valuable assets and positive projected earnings while missing tomorrow's payment. Totals hide timing; consolidation can hide restrictions between entities; a facility's headline limit can hide a condition that prevents drawing it.

### FIN.2:3 - Forces

Protect payment continuity without keeping unnecessary idle cash. Retain decision-changing detail without forecasting every immaterial transaction. Separate a contractual amount, an expected receipt and an available balance, while using a common timeline to see their combined effect.

### FIN.2:4 - Solution

1. Choose the paying entity, currencies, payment dates and minimum usable cash required at each date. Include the whole baseline of other receipts and payments. Use daily or intraday intervals around tight dates, even when the remaining horizon is monthly.
2. Reconcile opening bank and cash balances to the usable amount: remove restricted, pledged, trapped or unsettled amounts as the actual arrangements require. Identify an intercompany transfer by its source, permitted route, cost and earliest usable time; common ownership alone supplies none of these.
3. Place material operating payments, collections, taxes, debt service, investments and distributions on the timeline. Distinguish agreed dates from expectations. Keep alternative collection or draw assumptions as scenarios; do not add a hoped-for receipt to a committed one.
4. For each facility, establish the remaining commitment, borrower, currency, expiry, draw conditions, notice period, cutoff, collateral and fees. Count a draw as available only on the scenario whose conditions support it. A revocable indicative line contributes a possible funding alternative, not current cash.
5. Calculate each closing balance as opening usable cash plus usable inflows minus payments. For a required reserve, funding need at a date is the positive amount by which the pre-funding balance falls below that reserve. Solve for the gross draw when fees are withheld; include later interest and repayment.
6. Recalculate the whole timeline with the proposed response. A draw that cures today's gap can create a larger maturity gap. Return the amounts, dates, conditions and affected commitments. Use FIN.3 for working-capital alternatives, FIN.10 for financing terms, or FIN.15 for a selected permitted treasury action.

Stop when the receiving decision can distinguish a funded path from its unresolved conditions. If the right to money or the contract's event behavior is unclear, obtain that specific account through [FDM.1–3][FDM]. If profit and cash disagree materially, use FIN.4 and the applicable [MA.4][MA] reconciliation.

### FIN.2:5 - Archetypal Grounding

A constructed order brings 1,200 on day 28 and requires payments of 440 on day 0 and 100 on day 7. The otherwise unchanged whole-business baseline has cash of 500 at each relevant date after all other flows. The operating account already establishes a favorable incremental contribution of 660 and feasible capacity.

| Event | Cash without financing |
| --- | ---: |
| Opening, day 0 | 500 |
| After paying 440, day 0 | 60 |
| After paying 100, day 7 | −40 |
| After receiving 1,200, day 28 | 1,160 |

A committed facility can provide up to 80 before the day-7 payment. Its fee of 3 is withheld on drawing, and interest of 2 is paid with principal on day 28. A gross draw of 43 supplies the missing 40; day-7 cash becomes zero. Repayment of 45 leaves day-28 cash at 1,155. With a required reserve of 10, draw 53 instead; a draw of 43 no longer suffices. Assume the same stated fee and interest for these illustrative amounts.

If collection moves to day 40 while repayment stays on day 28, the first financing path leaves a gap of 45 on day 28. An actual extension or replacement is needed. Neither the unused limit nor the order's positive contribution establishes that extension.

### FIN.2:6 - Bias-Annotation

The forecast follows the selected corporation's ability to pay. A group total can conceal a subsidiary's shortage, and a base-case collection date can understate customer risk. Choose adverse cases because their consequences matter, without representing unspecified probabilities as measured likelihoods.

### FIN.2:7 - Conformance Checklist

Can another treasurer recover the usable opening amount, all material dated flows, reserve, draw conditions and gross-to-net proceeds? Does every proposed cure remain funded through its repayment? Are cash in another entity and unfulfilled conditions excluded from the asserted available amount?

### FIN.2:8 - Common Anti-Patterns and How to Avoid Them

Using profit as payment capacity hides noncash items and timing; recover the cash account. Using the portal limit as draw evidence ignores the contract; inspect the remaining conditions. Adding the same customer receipt to both baseline and incremental forecast double-counts money; reconcile the two before calculating need.

### FIN.2:9 - Consequences

The result identifies the amount and date that a response must cover and the conditions under which it works. Finer timing and conditional flows add forecasting effort, so retain only detail that can change payment, reserve or funding advice.

### FIN.2:10 - Architectural Rationale

A dated cash account makes the decisive constraint visible before financing is ranked. Ratios can summarize liquidity but cannot demonstrate that a particular payment is fundable at its cutoff.

### FIN.2:11 - SoTA-Echoing

The [CFA working-capital reading][CFA-WC] supplies the connection between liquidity and the cash-conversion mechanisms. This method adapts that connection to the actual payer and payment date. Compared with relying on aggregate liquidity ratios, the dated account exposes a temporary shortage; changed contractual access or payment timing reopens the conclusion.

### FIN.2:12 - Relations

FIN.1 supplies a missing decision boundary; FIN.4 supplies a missing cash projection. FIN.3 and FIN.10 compare responses, FIN.12 examines covenant access, and FIN.15 carries out the permitted action. [FDM][FDM] resolves financial positions when needed; it does not replace the liquidity calculation.

### FIN.2:End

## FIN.3 - Manage Working Capital and Cash Conversion

**Type:** Method

### FIN.3:0 - Use this when

A profitable order or a growing business consumes cash before customers pay, or inventory and payment terms tie up more money than the operation needs. Compare a concrete change in stock, customer credit, collections or supplier terms with its operating and commercial consequences. For a sufficient existing arrangement, continue it without redesign.

### FIN.3:1 - Problem frame

The working object is an arrangement governing inventory and trade-related receipts and payments. The finance practitioner compares changes to that arrangement with the same business baseline, using operating quantities and feasible service consequences supplied by the relevant teams.

### FIN.3:2 - Problem

A shorter cash-conversion cycle can release money while reducing sales, interrupting supply or moving cost to a weaker counterparty. A favorable margin can coexist with an unfinanceable timing gap.

### FIN.3:3 - Forces

Balance liquidity, contribution, reliability and commercial relationships. Distinguish a one-time cash release from a recurring profit improvement. Improve collection or inventory without assuming every customer, supplier or stage has the same behavior.

### FIN.3:4 - Solution

1. Identify the mechanism: order quantity and safety stock, customer credit and collection, supplier payment, or a combination. State what can actually change, whose consent is needed and when it takes effect.
2. Recover the relevant volumes, prices, variable resource consumption, holding and shortage consequences, expected credit losses and timed payments. Use an adequate [MA][MA] account and [OPS][OPS] feasibility result directly.
3. Build the no-change and changed dated cash accounts. Include discounts, financing, collection effort, supplier-price changes, lost contribution, taxes where applicable and the transitional stock or receivable change. Separate recurring operating effects from cash released by reducing a balance.
4. Use cash-conversion measures to explain the mechanism where the business and denominators fit. For a period of N days, inventory days approximate average relevant inventory divided by that period's cost of goods sold, times N; receivable days use average trade receivables divided by credit sales, times N; payable days use average trade payables divided by credit purchases, times N. Cost of goods sold is a purchases proxy only when its adequacy is established. On consistent period and scope grounds, cash-conversion days equal inventory days plus receivable days minus payable days. Investigate cohort, seasonal or overdue-account differences that an average conceals.
5. Compare feasible alternatives on the same horizon. Preserve service and capacity requirements. A discount offered to a customer is available only when the necessary agreement exists; a supplier extension is not obtained by changing a forecast date.
6. Select a policy or return conditional advice with the operational consequence, cash effect and revisit condition. Use FIN.2 to verify reserves across dates and FIN.15 to perform an authorized action.

For a discount offered in exchange for earlier cash, compare its actual cash cost with the available funding alternative over the same interval. Annualizing a short-period discount can help comparison, but retain its day count, compounding assumption and the actual amount needed; a large annualized percentage alone does not settle the order decision.

### FIN.3:5 - Archetypal Grounding

Continue FIN.2's order, with a day-7 gap of 40 and no required positive reserve. The customer has agreed to pay 96 on day 6 against 100 of the gross invoice, leaving 1,100 on day 28. All other terms are unchanged.

| Feasible response | Day-7 cash | Day-28 cash | Incremental gain over the 500 baseline |
| --- | ---: | ---: | ---: |
| Draw 43, fee 3, interest 2 | 0 | 1,155 | 655 |
| Receive the agreed advance with discount 4 | 56 | 1,156 | 656 |

On these grounds the advance adds one more unit of gain and leaves a buffer. This supports the advance for this question, assuming the stated customer agreement. If the customer has merely been asked, the proposed advance remains conditional and is not available for the day-7 payment.

The supplied operating case requires 26–29 rig-hours for 100 units. Twenty hours are usable and a ten-hour block costs 240. Materials cost 200 and supplier service costs 100. Materials and the block require 440 on day 0; the supplier's 100 is due on day 7. These give the incremental payments of 540. Cutting the ten-hour block to improve a cash ratio removes needed capacity, so it is not the same feasible order alternative.

For a separate 365-day illustration, average inventory 100 with cost of goods sold 500 gives 73 inventory days; average trade receivables 120 with credit sales 730 gives 60 receivable days; average trade payables 50 with credit purchases 365 gives 50 payable days. The cash-conversion cycle is 73 + 60 − 50 = 83 days on these comparable definitions. Shortening that summary still needs the operating and financial comparison above.

### FIN.3:6 - Bias-Annotation

A customer- or supplier-average view can hide a concentration, credit-quality change or unequal burden. A reduction in inventory is beneficial only with the service and replenishment conditions assumed in the comparison.

### FIN.3:7 - Conformance Checklist

Do both alternatives share the same baseline and quantities? Are discounts, losses, transitional cash and operating consequences included once? Is each changed payment arrangement agreed or clearly conditional? Can the reader distinguish released cash from recurring earnings?

### FIN.3:8 - Common Anti-Patterns and How to Avoid Them

Extending every supplier term can destroy supply continuity; compare affected suppliers and available agreements. Reducing all stock proportionally can remove protection at a constraint; use the operating consequence. Treating a smaller receivable balance as additional sales counts the same benefit twice; distinguish the stock of claims from income.

### FIN.3:9 - Consequences

A working-capital decision becomes a joint cash and operating comparison. It can favor a slightly cheaper arrangement with a larger buffer, or retain more inventory when reliability is worth its cost.

### FIN.3:10 - Architectural Rationale

The financial gain comes from a changed arrangement and its consequences, not from a ratio target by itself. Keeping the operating account external lets finance compare real feasible changes without rebuilding capacity analysis.

### FIN.3:11 - SoTA-Echoing

The [CFA working-capital reading][CFA-WC] supplies the inventory–receivable–payable mechanism. [MA][MA] and [OPS][OPS] supply resource and operating consequences. The adopted choice is to compare their combined cash effects rather than optimize cycle length alone. A changed service requirement, credit quality or feasible financing offer can reverse that choice.

### FIN.3:12 - Relations

FIN.2 tests the resulting cash timeline; FIN.4 prepares a missing projection, FIN.10 supplies financing alternatives, and FIN.16 returns material policy advice. [MA][MA] and [OPS][OPS] answer only the unresolved accounting or operating questions.

### FIN.3:End

## FIN.4 - Prepare Accounts and Forecasts for the Finance Decision

**Type:** Method

### FIN.4:0 - Use this when

Available accounts do not yet show the cash, earnings or claims needed for a financial choice, or two reports appear to contradict one another. Prepare the required view and reconcile material differences. Do not rebuild a supplied account that already answers the question.

### FIN.4:1 - Problem frame

The analyst prepares a decision-specific financial projection from reporting, operating and financial-position inputs. The projection is a description of expected or conditional consequences. Its purpose, date and assumptions determine its use; updating it does not amend a contract or create a deposit.

### FIN.4:2 - Problem

Reported profit, contribution, cash movement and a forward-looking valuation are different quantities. Mixing them can turn depreciation into a payment, allocated cost into an avoidable expense, or a negotiated target into an expected receipt.

### FIN.4:3 - Forces

Connect financial views without pretending that their quantities are interchangeable. Obtain enough detail to explain the decision while avoiding a second accounting system. Retain uncertainty where different operating assumptions change the result.

### FIN.4:4 - Solution

1. State the output needed: a dated cash forecast, project cash flows, a pro forma income and balance-sheet account, or a bridge between views. Choose its entity, horizon, units and baseline through FIN.1 when necessary.
2. Reuse sufficient source accounts. For unresolved resource consumption, capacity, attribution or cohort questions, obtain the appropriate [MA.1–8][MA] contribution. For disputed financial positions or conditional instruments, obtain [FDM][FDM]. For feasibility, use the actual operating result.
3. Build the projection through its economic drivers. Connect quantity and price to receipts; resources and terms to payments; investment and disposal to asset changes; inventory, receivables and payables to working capital; financing terms to their separate flows.
4. Reconcile material differences with the starting accounts. Explain timing, recognition, noncash items, scope and the decision baseline. Use a balance-sheet roll-forward when that is the intended view, but do not force every direct cash decision through a complete set of statements.
5. Separate forecasts, targets and authorized resource allocations. A changed forecast can update an expected consequence without changing what management wants or what someone is allowed to spend.
6. Examine the assumptions capable of reversing the financial answer. Return the projection with its purpose, key grounds, units, timing and conditions. Use FIN.17 for later changes to relied-on data; use FIN.18 when the forecasting method itself needs selection.

### FIN.4:5 - Archetypal Grounding

A one-period constructed operating account reports revenue 200, cash operating expense 120 and depreciation 20: operating profit is 60. Customers actually pay 150, suppliers are paid 120, and capital expenditure is 30. With no tax, debt flow or other working-capital change in this example, operating cash flow for the period is 30 and net cash flow after capital expenditure is zero. The bridge is profit 60 + depreciation 20 − increase in receivables 50 − capital expenditure 30 = 0. The 50 receivable remains a claim; it is not cash already received. If customers pay the remaining 50 next period, place that receipt there once. To assess a further payment, use FIN.2 with the opening usable balance and the dates of receipts and payments.

### FIN.4:6 - Bias-Annotation

Financial inputs can carry incentive-driven optimism, recognition choices and averages that hide cohorts. A reconciled historical account does not establish the future operating assumptions. Preserve the distinction between an observed amount and a forecast.

### FIN.4:7 - Conformance Checklist

Is every result labelled by view, purpose, entity and period? Can a reader replay the material bridge and identify the operating assumptions? Are noncash items, working-capital movements and financing flows included only in the views where they belong?

### FIN.4:8 - Common Anti-Patterns and How to Avoid Them

Copying profit into a cash forecast hides collection and payment timing; construct the bridge. Removing all allocated costs as irrelevant can also remove a truly incremental commitment; recover the resource consequence. Adjusting the forecast to a target removes its predictive use; retain the two purposes.

### FIN.4:9 - Consequences

Finance obtains a coherent input for liquidity or valuation and can explain why it differs from a report. Reconciliation takes effort, but the method limits that effort to differences that affect reliance or the decision.

### FIN.4:10 - Architectural Rationale

This pattern assembles a financial view from adequate domain accounts. Detailed accounting construction stays with MA, while the finance practitioner retains responsibility for the projection used in the financial answer.

### FIN.4:11 - SoTA-Echoing

The [MA 1.0 language][MA] separates operating, reporting and cash accounts and distinguishes forecast from target and allocation. FIN.4 adopts those results instead of treating ledger figures as universal decision inputs. Its additional contribution is the finance projection and material bridge; changed source meanings or receiving use reopen it.

### FIN.4:12 - Relations

FIN.2 uses dated cash; FIN.5–9 use matching valuation inputs; FIN.10–12 use debt-service and covenant projections. FIN.17 updates the relied-on projection. [MA][MA] and [FDM][FDM] provide specific missing accounts without becoming mandatory first steps.

### FIN.4:End

# Part B - Investment and value

## FIN.5 - Estimate Cost of Capital and Financing Constraints

**Type:** Method

### FIN.5:0 - Use this when

A valuation needs a discount rate, or an attractive financing rate is being used as if it were the required return on the whole investment. Match the return estimate to the cash flows and claims being valued. A sufficient externally supplied rate with the right grounds can be used directly.

### FIN.5:1 - Problem frame

Estimating required returns uses knowledge of investment returns, risk and present value. The calculation also needs market evidence appropriate to the claim; a sufficient supplied rate can be used on its stated grounds.


The analyst estimates the return capital providers require for the claim being valued and identifies relevant financing constraints. Management separately chooses the minimum return it will accept for a project. An obtainable borrowing offer states financing terms; an authorized financing decision permits a specified action.

### FIN.5:2 - Problem

Using a cheap loan rate for risky operating cash flows overvalues the project. Using a corporate average for a materially different project hides risk. Nominal, real, pre-tax and after-tax quantities can be combined into a number with no coherent meaning.

### FIN.5:3 - Forces

Use a tractable estimate while respecting uncertainty in market evidence, risk and future financing. Maintain comparability without asserting that all projects or claims have the same cost of capital.

### FIN.5:4 - Solution

1. Identify the cash flow to discount: operating cash available to all capital providers, cash available to common equity, or another specified claim. Fix currency, valuation date, timing, inflation and tax basis.
2. Estimate required returns from relevant market evidence and a suitable model. For equity, a CAPM estimate takes the form risk-free return plus beta times the market equity premium; explain the currency and horizon, comparable risk, estimation period and leverage assumptions. Do not make a historical estimate an observed future return.
3. Estimate debt cost from the relevant current borrowing risk and terms, including the distinction between a quoted yield and the total proceeds and fees of an actual issue. FIN.10 compares those offers.
4. When the operating cash flow and financing assumptions support it, use market-value capital weights for weighted average cost of capital. With debt and equity only: WACC = E/(D+E) × required equity return + D/(D+E) × debt return × (1−usable marginal tax rate). The debt-tax adjustment requires the applicable deductibility and ability to use it. Other claims require their own treatment.
5. Test material changes in required returns, weights and tax use. If financing changes substantially over time, use an appropriate changing-rate or separate-financing-effects valuation rather than impose a constant WACC.
6. Return the estimated rate or range, its grounds, material constraints and the cash-flow use it supports. Distinguish the estimated return required by capital providers from management's chosen minimum for accepting a project. Keep the rate quoted in an actual borrowing offer as a separate financing input.

### FIN.5:5 - Archetypal Grounding

For a hypothetical matched operating valuation, the market value of equity is 60 and the market value of debt is 40. Equity return is estimated at 9% from a 3% risk-free rate, beta 1.2 and equity premium 5%. Debt return is 6%; all of the assumed 25% debt tax benefit is usable. WACC is 0.6×9% + 0.4×6%×0.75 = 7.2%. Without that usable tax benefit it is 7.8%. These are constructed assumptions, not market quotations. A project with materially different operating risk needs a new match; the corporation's ability to borrow at 6% does not establish either project rate.

### FIN.5:6 - Bias-Annotation

Quoted market data may be stale, incomparable or unavailable for a private corporation. A model can conceal judgment in its beta, premium or target leverage. Expose action-changing uncertainty instead of reporting extra decimal places.

### FIN.5:7 - Conformance Checklist

Do the claim, currency, inflation, tax and timing bases match? Are weights and risk estimates justified for this use? Is the tax benefit usable under the assumed conditions? Can the reader distinguish the estimated return required by capital providers, management's chosen project-acceptance minimum and the terms of a borrowing offer?

### FIN.5:8 - Common Anti-Patterns and How to Avoid Them

Using book weights merely because they are easy to find can misstate the relevant financing mix; recover suitable values or qualify the estimate. Adding a risk premium after already making the same risk adjustment to cash flows double-counts it; identify where each effect enters.

### FIN.5:9 - Consequences

The valuation has an interpretable rate and sensitivity range. A rate range can support a robust choice or identify the uncertainty on which the choice turns; it cannot guarantee financing access.

### FIN.5:10 - Architectural Rationale

The method keeps discounting and financing connected through actual assumptions while retaining their different questions. A single fixed rate is useful only within the conditions that make it a reasonable approximation.

### FIN.5:11 - SoTA-Echoing

[OpenStax's WACC treatment][OS-WACC] supplies the weighted-rate calculation and the need to examine equity-model assumptions. This pattern retains those conditions and connects them to the actual financial claim. It rejects automatic use of a reported corporate rate for every project; a changed risk or financing basis reopens the estimate.

### FIN.5:12 - Relations

FIN.4 supplies cash flows; FIN.6–8 use matching rates. FIN.10 supplies actual financing terms, FIN.11 compares financing mixes, and FIN.12 tests access constraints. FIN.18 handles a material change in rate-estimation method.

### FIN.5:End

## FIN.6 - Value Capital Projects

**Type:** Method

### FIN.6:0 - Use this when

The corporation can invest in a project and needs to know what it adds relative to the relevant alternative. Estimate incremental project cash and value it on matching grounds. If the issue is competition for scarce capital among several projects, use the result in FIN.9.

### FIN.6:1 - Problem frame

Calculating discounted project value requires familiarity with compounding and present value. The cash-flow construction and matching-rate conditions below govern their use for this project.


The analyst values a specified project alternative against a baseline. The result is a financial assessment of incremental consequences, not proof of operating feasibility, available funding or authorization.

### FIN.6:2 - Problem

Accounting return, payback and gross revenue can favor a project whose incremental value is negative. Sunk costs and allocated expenses can displace the relevant opportunity cost, while working capital or terminal obligations disappear from the calculation.

### FIN.6:3 - Forces

Capture consequential cash effects without building an unnecessarily detailed model. Compare value over time while exposing uncertainty, strategic dependencies and limited funding.

### FIN.6:4 - Solution

1. Specify the project and the feasible baseline: continue, replace, defer, stop or another actual alternative. Obtain adequate operating quantities, capacity and service consequences; a technically impossible plan has no actionable investment value.
2. Estimate incremental after-tax operating cash at its expected dates. Include changes to existing business, opportunity cost of resources, investment, working capital, taxes, disposal and closure consequences. Exclude expenditure already irrecoverably incurred, while including any future consequence that the current choice can still change.
3. For an unlevered project valuation, calculate operating cash before financing flows and discount using a matching required return from FIN.5. Do not then subtract the new loan's interest and principal from the same cash flow. A separate equity valuation uses cash and a return appropriate to equity.
4. Calculate NPV by multiplying each incremental cash flow by the factor that brings it to the valuation date. With a constant annual rate r and cash flow CF at year t, each present value is CF/(1+r)^t; include the initial outlay at t = 0. Use date-specific discount factors when irregular timing matters. Include a terminal value only for a real remaining asset or continuing activity, with its assumptions stated.
5. Find thresholds and adverse cases that can change the sign or the comparison. A sensitivity changes one assumption; a scenario combines mutually consistent changes. Use probabilities only when their grounds support the intended expected-value claim.
6. Use IRR, payback or accounting measures for the questions they answer. IRR can misrank mutually exclusive projects of different scale or timing and can be multiple or absent for unusual cash-flow signs. Payback describes recovery timing while omitting later value unless explicitly extended.
7. Include valuable exercisable flexibility through FIN.8 and interactions or capital rationing through FIN.9 when material. Return value, conditions and the decision-changing threshold. FIN.2 separately tests funding.

### FIN.6:5 - Archetypal Grounding

A constructed project pays 1,000 now and receives 600 at the end of each of the next two years. These are complete incremental after-tax operating cash flows; no terminal value remains. At a matching annual rate of 10%, NPV = −1,000 + 600/1.10 + 600/1.10² = 41.32. Equal annual receipts of 576.19 would give zero NPV. At a required return of 15%, the same 600 receipts give −24.57. Thus the result supports the project on the stated 10% basis, and the relevant return assumption can reverse it. The 41.32 is a value estimate; it does not supply the initial 1,000.

### FIN.6:6 - Bias-Annotation

Sponsor forecasts may overstate demand or understate implementation loss. An apparently conservative sensitivity can still omit a correlated adverse scenario. Keep operating evidence and the selected baseline visible.

### FIN.6:7 - Conformance Checklist

Can the reader rebuild incremental cash from the alternative and baseline? Are opportunity cost, working capital, tax and terminal effects handled once? Does the discount basis match? Is any claimed flexibility feasible, and is funding distinguished from positive NPV?

### FIN.6:8 - Common Anti-Patterns and How to Avoid Them

Charging an unchanged allocated overhead as incremental cost can reject a useful project; recover the resource effect. Ignoring cannibalized contribution can overvalue it; include the lost alternative cash. Choosing by highest IRR alone can discard more valuable feasible capital uses; compare their NPV and constraints.

### FIN.6:9 - Consequences

The result shows whether the project adds financial value on stated grounds and what changes the answer. The analyst can complete this valuation while funding for the initial investment or the project's operating feasibility remains unresolved.

### FIN.6:10 - Architectural Rationale

Incremental cash and matching discount factors provide a common value basis. Additional measures remain useful as complementary answers, so a fast payback need not be mistaken for the greatest value.

### FIN.6:11 - SoTA-Echoing

The [CFA capital-investment reading][CFA-CAPITAL] emphasizes incremental analysis and the limits of common allocation rules. This pattern adopts NPV for the value question while preserving timing and uncertainty questions. Compared with accepting a hurdle-based accounting return alone, it exposes displaced cash and residual obligations; a changed baseline or realizable option reopens the result.

### FIN.6:12 - Relations

FIN.4 provides the required projection and FIN.5 the matching return. FIN.8 values flexibility; FIN.9 compares interacting uses. [MA][MA] and [OPS][OPS] supply missing resource and feasibility results. FIN.16 returns the financial recommendation.

### FIN.6:End

## FIN.7 - Value Assets and the Corporation

**Type:** Method

### FIN.7:0 - Use this when

A decision needs the value of an asset, operating enterprise or ownership interest at a stated date. Identify exactly what is being valued and choose methods that answer that purpose. A qualified supplied valuation can be used without recreating it.

### FIN.7:1 - Problem frame

An income valuation requires familiarity with present value and required returns; market and asset approaches require comparable or asset-value evidence and the relevant adjustments. Obtain the additional expertise for the approach actually used, or use an adequate supplied valuation.


The object is a value estimate for an identified interest under a stated premise and purpose. Operating enterprise value, equity value, transaction price and book amount can concern related objects while answering different questions.

### FIN.7:2 - Problem

An enterprise value can be quoted as the amount payable to shareholders without treating debt and other claims. A multiple from an unlike company or a perpetual-growth assumption can drive an apparently precise result with little support.

### FIN.7:3 - Forces

Use available market and operating evidence while retaining differences in rights, risk, control, liquidity and growth. Reconcile methods without mechanically averaging incompatible estimates.

### FIN.7:4 - Solution

1. Identify the asset or interest, ownership rights, valuation purpose and date. State the premise, such as continued operation or disposal, and the relevant information and scope limits. Use the actual engagement and applicable standards when a formal valuation conclusion is required.
2. Select the income, market or asset approach that fits the subject and evidence. An income approach values expected cash; a market approach uses sufficiently comparable prices or multiples; an asset approach values the relevant assets and liabilities. Explain why a method contributes to this question.
3. For an operating income valuation, forecast cash available to capital providers and discount it on matching grounds. A common FCFF construction is after-tax operating profit plus noncash depreciation, minus capital investment and the increase in operating working capital. In a simple debt-and-common-equity case, FCFE is net income after interest and tax, plus noncash depreciation, minus capital investment and the increase in operating working capital, plus new borrowing minus principal repaid. Other prior claims require their appropriate cash treatment. Discount equity cash flow at the required equity return.
4. Explain continuing-value assumptions separately. A constant-growth terminal value at the end of year n uses next year's sustainable cash divided by the discount rate minus growth, with growth below that rate and reinvestment compatible with growth. Discount that value to the valuation date.
5. Reconcile operating enterprise value to the specified equity interest by adding the nonoperating assets actually included and subtracting the debt and other prior claims treated in the transaction or valuation. Match market values, ownership shares and claim treatment; avoid counting cash or a liability twice.
6. For comparables, align the numerator and financial measure, date and definitions. Examine growth, margins, risk and accounting differences; an adjustment needs a reason. For asset values, include the liabilities and costs relevant to the stated premise.
7. Reconcile differences between approaches by their assumptions and evidential strength. Return a supported value or range, its use, and the condition that would require a new estimate.

### FIN.7:5 - Archetypal Grounding

Suppose two years of FCFF are 10 each, the matching WACC is 10%, and continuing year-3 FCFF is sustainably 10 with zero growth. Terminal value at year 2 is 100. Operating enterprise value is 10/1.1 + (10+100)/1.1² = 100. If debt with a market value of 30 remains outstanding in the acquired company and the company includes excess cash of 10 that is freely transferable after closing, with no other claim adjustment, standalone equity value is 80. FIN.9 compares that interest's value with the price. A price of 100 for the equity is not made reasonable by calling the operating business worth 100.

### FIN.7:6 - Bias-Annotation

Market comparables can privilege listed companies and recent transactions while omitting private-company conditions. A terminal value can dominate the estimate. State whose interest is valued and what can actually be transferred.

### FIN.7:7 - Conformance Checklist

Is the interest, date, purpose and premise clear? Do cash flows, rates and terminal assumptions agree? Can the enterprise-to-equity bridge be replayed? Are comparable definitions and meaningful differences examined? Is a formal standards claim supported by the applicable requirements?

### FIN.7:8 - Common Anti-Patterns and How to Avoid Them

Averaging an equity multiple with an enterprise multiple does not reconcile them; align claims first. Treating all cash as excess can remove operating reserves; recover its use. Adding a terminal growth rate without funding reinvestment creates unsupported value; make growth and cash generation compatible.

### FIN.7:9 - Consequences

The receiving transaction or allocation decision obtains a value for the actual interest and can see its sensitive assumptions. Different purposes may properly yield different estimates.

### FIN.7:10 - Architectural Rationale

The method starts from the valued interest because no technique can repair a mistaken object. Several approaches provide useful challenges to assumptions; they do not automatically form a single average.

### FIN.7:11 - SoTA-Echoing

The [CFA free-cash-flow reading][CFA-FCF] supplies the FCFF/FCFE distinction and matching discount bases. The [IVSC public standards overview][IVSC] identifies scope, basis, data, model and reporting as distinct concerns; it does not supply the full engagement requirements. FIN.7 adopts both contributions and rejects an unexplained blend of price, book amount and value.

### FIN.7:12 - Relations

FIN.5 supplies required returns and FIN.4 relevant projections. FIN.8 assesses embedded flexibility; FIN.9 uses standalone and transaction values. FIN.22 uses a valuation adapted to the actual recovery route and claimant treatment.

### FIN.7:End

## FIN.8 - Value Options under Uncertainty

**Type:** Method

### FIN.8:0 - Use this when

The corporation can wait, expand, switch or abandon after new information arrives, and this flexibility may change an investment or financing comparison. Identify the actual right or operational ability before valuing it. An uncertain future alone does not establish an exercisable option.

### FIN.8:1 - Problem frame

The valuation requires familiarity with present value and payoffs that depend on later events or choices. Using the replication model also requires understanding its trading and borrowing assumptions, stated in the procedure below.


The object is a contingent choice available to a named party within an exercise window and constraints. Financial options derive their rights from an instrument; real flexibility also requires capacity, access and the ability to act. This method assesses their value or a useful bound.

### FIN.8:2 - Problem

A fixed cash-flow forecast can omit valuable flexibility. Conversely, applying an option formula to a project with no feasible exercise path creates value that the corporation cannot obtain.

### FIN.8:3 - Forces

Represent contingent decisions without claiming that every business risk is tradable or that risk-neutral weights are observed probabilities. Balance modeling detail with the choice it can change.

### FIN.8:4 - Solution

1. Name the holder, underlying asset or activity, available exercise actions, timing, costs and constraints. Recover a disputed financial right through [FDM][FDM]; obtain operating feasibility for a real option.
2. Build the relevant states and decision points. At each point include only actions available with information then obtainable. Retain the costs of preserving the option, such as a reservation payment, pilot or capacity commitment.
3. For tradable contingent claims with justified replication assumptions, use an appropriate no-arbitrage model. In a one-period binomial model with no intermediate underlying payout, underlying value S, up/down factors u and d, and accessible risk-free borrowing and lending at gross growth R between d and u, the risk-neutral up weight is (R−d)/(u−d). Discount the weighted state payoffs by R. For several periods work backward; compare immediate exercise with continuation only where early exercise is permitted.
4. For nontraded projects, test whether replication or a defensible risk adjustment actually supports that pricing claim. Otherwise compare contingent strategies under explicit scenarios, probabilities where justified, and consistent discounting. Report a range or limit when a unique price lacks grounds.
5. Compare the flexible strategy with the same project under the relevant commitment alternative. Avoid adding an “option premium” to cash flows that already implement the same contingent strategy.
6. Return the supported value, choice or bound with its exercise and financing conditions. Reopen when rights, exercise cost, timing or information availability changes.

### FIN.8:5 - Archetypal Grounding

A constructed European call has exercise price 100. Its tradable underlying is worth 100 now and can be worth 120 or 80 in one period, with no interim payout. Risk-free growth is 1.05; the stated idealized model permits replication without transaction frictions. Payoffs are 20 and zero. The risk-neutral up weight is (1.05−0.8)/(1.2−0.8) = 0.625, so option value is 0.625×20/1.05 = 11.90. The weight is a pricing device under these assumptions, not a forecast that the up state occurs with probability 62.5%.

For a different, nontraded expansion, suppose the decision date has two stated scenarios: an expansion costing 60 then produces value 90 in the favorable case and 40 in the adverse case. If the corporation may choose at that date, net exercise values are 30 and zero, instead of 30 and −20 under an unavoidable commitment. That shows the consequential branch. A price today additionally needs the cost of preserving the choice and justified timing and risk grounds; the two scenario numbers alone do not establish it.

### FIN.8:6 - Bias-Annotation

Model convenience can conceal nonmarket risk, illiquidity or a loss of operational freedom. Scenario selection can overstate how much information will be available before exercise.

### FIN.8:7 - Conformance Checklist

Can the named party actually take each exercise action at the modeled time? Are preservation and exercise costs included? Are pricing weights distinguished from factual probabilities? Does the comparison count flexibility once and identify the grounds for any reported price?

### FIN.8:8 - Common Anti-Patterns and How to Avoid Them

Calling a forecast range an option omits an action; identify the exercisable choice. Using traded-option assumptions for an unreplicable project without explanation overstates precision; return conditional scenarios or a supported bound. Assuming exercise finance will exist can turn a valuable right into an unusable plan; state the funding condition.

### FIN.8:9 - Consequences

The result can justify preserving flexibility or show that its cost exceeds its useful value. The analyst can compare the two expansion scenarios while leaving today's price unresolved until the cost of preserving the choice and its timing and risk grounds are known.

### FIN.8:10 - Architectural Rationale

Working backward from actual contingent actions makes the source of flexibility value explicit. Separate treatment of market replication and project scenarios keeps a convenient formula from silently changing the claim.

### FIN.8:11 - SoTA-Echoing

The [CFA contingent-claims reading][CFA-OPTIONS] supplies no-arbitrage valuation, backward induction and their market assumptions. FIN.8 applies them where supported and uses explicit scenario comparisons elsewhere. Compared with a fixed commitment forecast, the method preserves later choice; losing the exercise path or replication grounds changes the valuation.

### FIN.8:12 - Relations

FIN.6 and FIN.7 use option assessments when material; FIN.9 compares the resulting alternatives. FIN.10 supplies embedded financing terms, and FIN.14 may use option protection. [FDM][FDM] establishes the right when unresolved.

### FIN.8:End

## FIN.9 - Compare Capital Investments and Allocations

**Type:** Method

### FIN.9:0 - Use this when

Several uses of capital compete, interact or displace one another, or the corporation is considering an acquisition or divestment. Compare feasible combinations and their incremental value. Use FIN.6 directly for a sufficient standalone project question.

### FIN.9:1 - Problem frame

The object is a capital-use choice or combination for a named corporation. Acquisition and divestment are transaction uses of this comparison: they add a specified interest, consideration and combination or separation effects. Legal closing and operational execution require their applicable professional methods.

### FIN.9:2 - Problem

Choosing the largest standalone NPV can exclude a better combination. Adding an attractive business to the corporation can destroy buyer value at the offered price. Divestment proceeds can look beneficial while the remaining business loses shared services or customers.

### FIN.9:3 - Forces

Compare value, limited capital, operating dependencies and risk concentration on compatible grounds. Preserve indivisibilities and institutional feasibility without hiding judgments in an unexplained weighted score.

### FIN.9:4 - Solution

1. Specify the feasible alternatives and combinations, including continuation or deferral where available. Recover the capital, capacity, time, financing and authority constraints. If alternatives are still missing, develop them before claiming to rank the available set.
2. Obtain matching values from FIN.6–8 and relevant cash requirements from FIN.2. Align valuation date, currency, baseline, tax and risk treatment. Identify shared costs, mutually exclusive projects and dependencies; do not sum contributions that assume the same scarce resource twice.
3. Compare whole feasible combinations. For a few indivisible projects, enumerating them can be enough. For larger sets, use an appropriate constrained model and inspect the meaning of its variables and constraints. Stress shared demand, input-price and funding shocks across the combination to expose coincident losses or funding needs. A profitability index can help a suitable divisible-capital question but does not solve arbitrary indivisible combinations.
4. For an acquisition, identify the interest and included claims. Compare its standalone value, incremental buyer-specific benefits, integration and other incremental costs, and total consideration. Include the conditions required to obtain benefits and the effect on the buyer's remaining business. Reconcile debt, cash and other claims through FIN.7 before comparing equity value with an equity price.
5. For a divestment, compare net disposal proceeds plus the value and obligations of the remaining business with the no-sale alternative. Include taxes, transaction costs, lost contribution, retained liabilities and changes to shared operations. Do not count both sale proceeds and continued ownership of what is sold.
6. Use FIN.10–12 for material financing conditions and FIN.21 for the retain-or-return alternative. Separate a favorable financial comparison from the availability of funds and transaction consents.
7. State the recommendation, robust alternatives, constraints and facts that can reverse it. [C.11][CHOICE] supplies the general choice contribution over these available alternatives; this pattern supplies their financial consequences and feasible combinations.

### FIN.9:5 - Archetypal Grounding

With a capital limit of 100, indivisible projects A, B and C cost 100, 60 and 40 and have NPVs 25, 18 and 12 on compatible grounds. Assuming no interaction, B+C costs 100 and yields 30, exceeding A's 25. Ranking standalone NPV would select A and miss five of value. If B and C require the same unavailable capacity, their combination is infeasible and the result changes.

In a constructed acquisition at one valuation date and currency, standalone operating enterprise value is 100. Debt with a market value of 30 remains outstanding in the acquired company, and included excess cash of 10 is freely transferable after closing. With no other claim adjustment, standalone equity value is 80. Buyer-specific incremental benefits have present value 30; integration and other incremental costs have present value 15, on compatible after-tax grounds.

| Equity price | Buyer value after price |
| --- | ---: |
| 100 | 80 + 30 − 15 − 100 = −5 |
| 90 | 80 + 30 − 15 − 90 = +5 |

Positive combination benefits therefore do not justify the price of 100. A price of 90 changes the financial answer on unchanged grounds. A new financing effect must enter the appropriate valuation once; it cannot be both capitalized in the rate and subtracted again as the same cost. The included 10 is not available to pay the seller before closing. Actual funding, consent and the ability to realize benefits can still block the transaction.

For a divestment, suppose the whole business is worth 150 before sale. Net sale proceeds are 45 and the remaining business, after all lost synergies and retained obligations, is worth 100. The comparable total is 145, five below retaining the business. A headline offer of 50 would not establish a gain without the net-proceeds and residual-business calculation.

### FIN.9:6 - Bias-Annotation

Synergies and strategic benefits often receive the sponsor's most optimistic assumptions. A corporation-level total can hide the burden on particular operations or claimants. Preserve those constraints and the uncertainty that matters to the recommendation.

### FIN.9:7 - Conformance Checklist

Are all combinations feasible, and do their values share a comparison basis? Are shared resources and effects counted once? For a transaction, can the reader recover the interest, claim bridge, price, incremental effects and residual business? Are financial preference and closing conditions distinct?

### FIN.9:8 - Common Anti-Patterns and How to Avoid Them

Ranking by standalone return can miss dependencies; compare combinations. Treating synergy as permission to pay any premium omits price; calculate buyer value after consideration. Calling disposal proceeds profit can ignore the asset and continuing obligations surrendered; compare the complete alternatives.

### FIN.9:9 - Consequences

The corporation obtains a conditional allocation or transaction recommendation that explains why a combination or price changes the result. A useful financial answer may still require operating, financing or authority action before implementation.

### FIN.9:10 - Architectural Rationale

A transaction changes more than the cash paid or received. Buying a business changes both the buyer's claims and its operations; selling can leave costs and obligations with the remaining business. Comparing these whole alternatives on matching grounds prevents a purchase's attractive standalone value or a sale's headline proceeds from being mistaken for a gain to the corporation.

### FIN.9:11 - SoTA-Echoing

The [CFA capital-allocation reading][CFA-CAPITAL] supplies investment-comparison concerns; its [corporate-restructuring reading][CFA-RESTRUCT] supplies transaction and pro forma concerns. FIN.9 adapts these to the corporation's net gain and remaining business. Compared with a standalone-value ranking, it includes price and interaction; changed transaction scope or feasibility reopens the comparison.

### FIN.9:12 - Relations

FIN.6–8 supply values; FIN.2 supplies timed funding needs; FIN.10–12 supply financing conditions; FIN.21 supplies retention or payout alternatives. FIN.16 prepares the receiving advice. [C.11][CHOICE] supports the local choice once these financial alternatives exist.

### FIN.9:End

# Part C - Financing, distributions and recovery

## FIN.10 - Design Financing Instruments and Terms

**Type:** Method

### FIN.10:0 - Use this when

The corporation needs funds and must compare an issue, loan, lease, committed line or other feasible arrangement. Model the terms that determine proceeds, future cash and rights. Use an already adequate committed arrangement directly when the task is only its permitted execution.

### FIN.10:1 - Problem frame

Calculating an effective financing rate requires familiarity with compounding and discounting timed payments. Comparing adequate supplied proceeds and payment amounts can be sufficient without solving for that rate.


The object is a proposed financing arrangement and its financial consequences for the corporation. Instrument design includes amount, maturity, repayment, priority, collateral, currency, options and control terms. It does not itself secure investor acceptance or establish a disputed legal interpretation.

### FIN.10:2 - Problem

The lowest headline rate can produce the highest effective cost, insufficient net proceeds or a maturity the corporation cannot meet. An indicative term sheet can be mistaken for committed funding.

### FIN.10:3 - Forces

Balance cost, access, timing, flexibility, control and repayment risk. Retain contractual detail that can change the choice while keeping genuinely comparable alternatives visible.

### FIN.10:4 - Solution

1. Recover the net amount and dates needed, currencies and expected repayment capacity. Include the effect of fees withheld at issue. Use FIN.2 where the funding requirement is unresolved.
2. Construct obtainable alternatives with their actual potential providers. Specify who supplies funds, who owes what, repayment and draw conditions, ranking, security, restrictions, conversion or exercise rights and required consents. Use [FDM][FDM] for an unresolved position or conditional event.
3. Project proceeds and every material payment under each alternative: interest or distribution terms, principal, issue and commitment fees, collateral or margin cash, tax consequences where supported, and contingent payments. Use the stated rate conventions, day counts, resets and settlement dates.
4. Compare the same funding requirement over the same horizon. Where meaningful, solve for the rate equating net proceeds with the discounted payments; retain any option or contingent risk that a single effective rate cannot represent.
5. Test refinancing and adverse states, collateral and covenant constraints, currency mismatch and control effects. Compare a long maturity with a rollover plan only if the latter includes its actual access uncertainty.
6. Obtain specific legal, tax, accounting or provider facts where they change the offer or its use. Distinguish proposed, offered, accepted, committed and currently drawable terms by what has actually occurred.
7. Return the preferred terms or conditional alternatives, total cash consequences and the unresolved condition. FIN.11 handles the larger financing mix and FIN.15 executes an authorized transaction.

### FIN.10:5 - Archetypal Grounding

Two constructed one-year offers finance a net need of 100. A charges 8% interest on face value and withholds an issue fee of 2% of face value. B charges 9% and no fee. Assume no other cost, tax difference or contingent term and that A permits the necessary larger face amount. A must issue 100/0.98 = 102.04 and repay 102.04×1.08 = 110.20; its effective cost is 1.08/0.98−1 = 10.20%. B provides 100 and repays 109, so B is cheaper for this need despite its higher headline rate. If A is capped at face value 100, its net proceeds of 98 do not meet the need at all.

### FIN.10:6 - Bias-Annotation

Provider quotations can omit conditions or vary in availability. A rate comparison can understate collateral, control, refinancing and concentrated-provider risks.

### FIN.10:7 - Conformance Checklist

Does each alternative supply the required net cash at the required time? Are fees, repayment and contingent terms recoverable? Are comparable dates and conventions used? Is each commitment and consent claim supported, and is the residual funding need visible?

### FIN.10:8 - Common Anti-Patterns and How to Avoid Them

Comparing coupons alone ignores issue economics; compare net proceeds and payments. Assuming a revolving facility will renew hides refinancing risk; show the expiry and available alternatives. Translating foreign debt at one spot rate can conceal future payment exposure; use FIN.13.

### FIN.10:9 - Consequences

The comparison helps the corporation choose more useful terms or shows that a seemingly cheap offer cannot finance the requirement. It retains meaningful non-rate consequences for the receiving decision.

### FIN.10:10 - Architectural Rationale

A cash-and-rights comparison connects instrument design to the corporation's actual need. A single cost measure remains a useful projection, while conditions that change availability or control remain explicit.

### FIN.10:11 - SoTA-Echoing

The [AFP treasury task specification][AFP] includes funding arrangements, provider relations and financial risk as connected professional responsibilities. [FDM][FDM] supplies conditional instrument behavior. FIN.10 turns those concerns into comparable cash terms rather than treating a product label or quote as sufficient; changed conditions or net need reopen it.

### FIN.10:12 - Relations

FIN.2 supplies funding need; FIN.5 distinguishes required return from financing cost; FIN.11 compares the mix and FIN.12 its restrictions. FIN.13–14 assess financial exposure and protection. FIN.15 carries out the permitted financing action.

### FIN.10:End

## FIN.11 - Select Capital Structure

**Type:** Method

### FIN.11:0 - Use this when

The corporation must choose or reconsider its mix of debt, equity and other financing, rather than just select one instrument. Compare the mix under actual cash, tax, control, access and distress conditions. An analytical target is a proposal unless the relevant authority has decided it.

### FIN.11:1 - Problem frame

The object is a financing mix for the corporation or a specified financing need. Its usefulness depends on the operating assets, obligations and adverse states it must support. This method does not establish a universal optimal debt ratio.

### FIN.11:2 - Problem

Debt can lower a simple weighted financing cost while making the corporation unable to survive a cash downturn or obtain future funds. An all-equity alternative can preserve payment flexibility while imposing issuance cost or an unacceptable change in control.

### FIN.11:3 - Forces

Balance financing cost, tax benefits, control, distress exposure and flexibility. Distinguish expected profitability from debt-service capacity, and a long-term target from the next feasible transaction.

### FIN.11:4 - Solution

1. State the financing need, existing claims, operating cash generation and required liquidity. Separate the current mix, proposed transaction and longer-term analytical target.
2. Form materially different feasible mixes. Recover instrument terms through FIN.10 only where missing. Include continuation if it remains available.
3. Project each mix's cash service and residual claims over the relevant horizon and adverse states. Examine maturities, refinancing concentrations, currency mismatches and contingent obligations.
4. Assess the usable tax benefits and the costs or constraints of distress, issuance, information, control and future access. Use current institution-specific facts; do not transfer a tax or insolvency assumption between jurisdictions without grounds.
5. Estimate value or required-return implications with matching FIN.5 grounds where they can change the decision. Avoid holding equity and debt costs fixed while making a material leverage change unless that approximation is justified.
6. Compare the alternatives against the corporation's objectives and constraints. A mix with attractive expected value can be excluded by a required liquidity or access condition. Use FIN.12 for covenant and flexibility consequences.
7. Return a structure proposal, bounded target range or supported continuation, with the implementation conditions. Authorization and the actual financing remain separate decisions and actions.

### FIN.11:5 - Archetypal Grounding

A constructed corporation needs 100 for the same assets. Mix A provides debt 80 and equity 20 with annual debt service 35; mix B provides debt 40 and equity 60 with service 15. Assume these are obtainable terms without other cash cost. Cash available before debt service is 60 in the base state and 25 in the adverse state, and the corporation requires at least 5 remaining cash. A leaves 25 in the base state but −10 in the adverse state. B leaves 45 and 10. B satisfies the stated cash requirement in both states; A does not. This establishes a capacity constraint, not that B is universally optimal: the additional equity's price, control effects and other feasible terms remain part of the choice.

### FIN.11:6 - Bias-Annotation

A shareholder perspective can understate harm shifted to creditors or the operating business. Historical cash stability can fail during a regime change. Explicit adverse states avoid treating average service coverage as a guarantee.

### FIN.11:7 - Conformance Checklist

Do the mixes fund the same need and preserve the assumed operating plan? Are debt service, tax use, adverse cash and refinancing conditions included? Are changing required returns and control effects examined where material? Is the conclusion clearly target, proposal, continuation or authorized change?

### FIN.11:8 - Common Anti-Patterns and How to Avoid Them

Selecting the lowest WACC from fixed rates can ignore the cost of increased leverage; recalculate the relevant risk. Treating an unused debt limit as spare cash ignores draw conditions; use FIN.2. Calling a target ratio a financing action confuses analysis with execution; state the next authorized move.

### FIN.11:9 - Consequences

The comparison connects the proposed financing mix to the corporation's ability to make the stated payments, retain the required cash balance and obtain future financing. It can support a range or incremental transition when a precise ratio would overstate the evidence.

### FIN.11:10 - Architectural Rationale

Capital structure concerns the joint effects of claims on the corporation. Instrument-by-instrument selection alone can miss concentrated maturities and distress exposure, while a universal ratio discards the conditions that determine their importance.

### FIN.11:11 - SoTA-Echoing

[OpenStax's capital-structure account][OS-STRUCTURE] supplies the debt/equity mix and cost-of-capital connection. FIN.11 combines it with FIN.2's dated service capacity and FIN.12's actual access conditions. The method rejects cost minimization under frozen risk assumptions as a complete answer; changed operating risk or financing access reopens the mix.

### FIN.11:12 - Relations

FIN.5 supplies matching return estimates, FIN.10 feasible terms and FIN.12 access constraints. FIN.21 connects retention and payout to funding; FIN.22 handles a broader recovery problem when ordinary financing alternatives no longer suffice.

### FIN.11:End

## FIN.12 - Preserve Covenant Headroom and Financing Flexibility

**Type:** Method

### FIN.12:0 - Use this when

A financial plan approaches a covenant, borrowing limit or refinancing date, or a change may remove access to funds. Recover the actual test and available response before relying on headroom. A sufficient current covenant calculation can be used without rebuilding the contract analysis.

### FIN.12:1 - Problem frame

The object is the corporation's compliance and usable financing capacity under specified terms and dates. A covenant ratio, a cash balance, a rating and a facility commitment are different grounds for access; this method connects the ones that matter to the proposed action.

### FIN.12:2 - Problem

A forecast may pass an internally defined ratio while failing the agreement's definition, or show nominal headroom that disappears after a distribution. A possible waiver can be treated as if it had already amended the terms.

### FIN.12:3 - Forces

Preserve access and flexibility while avoiding unnecessary idle capacity or expensive amendments. Act early enough for a remedy to be available without manufacturing certainty about another party's consent.

### FIN.12:4 - Solution

1. Recover the applicable agreement, borrower, tested quantities, accounting definitions, exclusions, currency conversion, test dates and reporting or certification requirements. Obtain qualified interpretation for an ambiguity that affects reliance.
2. Calculate current and projected tests using those definitions. State headroom in an interpretable form: distance to a ratio threshold, amount of additional debt permitted, or deterioration in the denominator before breach. Inspect both numerator and denominator behavior.
3. Connect the tests to the cash plan, proposed borrowing, acquisitions, distributions and collateral use. Test the adverse states and timing that can remove access before the nominal maturity. Where ratings or collateral valuations affect terms or access, examine those effects separately; passing the covenant does not by itself preserve that access.
4. Recover the actual consequences, notice requirements and available cure rights or consent procedures. Do not assume that a breach universally accelerates debt or that every agreement permits an equity cure.
5. Compare obtainable actions: modify the operating or funding plan, repay or refinance, preserve collateral, request waiver or amendment, or invoke an available cure. Include cost, delay, restrictions and the risk of non-consent.
6. Return the action or conditional advice with its latest useful date. A waiver under discussion is an alternative dependent on consent. If ordinary responses cannot restore a viable financing path, use FIN.22.

### FIN.12:5 - Archetypal Grounding

A constructed facility tests debt/EBITDA at quarter end with a maximum of 3.0, using the agreement's supplied definitions. Tested debt is 240 and EBITDA 100: the ratio is 2.4 and permitted additional debt at unchanged EBITDA is 60. If EBITDA falls to 80, the same debt reaches 3.0 and that headroom disappears. A proposed debt-funded payment of 20 produces 260/80 = 3.25. This plan cannot rely on the original headroom under that scenario. A repayment of 20, different permitted financing or an actual amendment can change the result; a hoped-for waiver cannot.

### FIN.12:6 - Bias-Annotation

A single ratio can conceal minimum liquidity, collateral or reporting conditions. Management's EBITDA forecast may be optimistic, and contract definitions can differ from management reporting.

### FIN.12:7 - Conformance Checklist

Are definitions and dates taken from the applicable terms? Can the current and changed headroom be replayed? Are all action-changing restrictions and actual remedy conditions included? Does the plan distinguish requested consent from obtained consent?

### FIN.12:8 - Common Anti-Patterns and How to Avoid Them

Using an analyst's EBITDA instead of the tested definition answers a different question; reconcile the definitions. Reporting “20% headroom” without its denominator obscures the stress; state the ratio or permitted amount. Counting a waiver as available finance before agreement hides a remaining choice by the lender.

### FIN.12:9 - Consequences

The result identifies the move and time needed to preserve financing access or makes the unresolved consent problem explicit. It can justify reducing an otherwise attractive investment or payout.

### FIN.12:10 - Architectural Rationale

Headroom has meaning relative to an actual test and a changed plan. Retaining the contract's event and timing conditions makes it a usable financing result rather than an isolated dashboard number.

### FIN.12:11 - SoTA-Echoing

[FDM][FDM] supplies conditional financial obligations and event effects; the [World Bank workout toolkit][WB-WORKOUT] addresses consent and finance constraints when ordinary arrangements become inadequate. FIN.12 applies those distinctions to an actual covenant calculation, instead of equating a ratio forecast with continuing access. Changed terms or tested inputs reopen it.

### FIN.12:12 - Relations

FIN.2 supplies liquidity and FIN.10–11 financing alternatives. FIN.9 and FIN.21 use access constraints before recommending investment or payout. FIN.22 compares broader recovery routes. FIN.17 updates an affected relied-on calculation.

### FIN.12:End

## FIN.21 - Decide How Much Capital to Retain or Return

**Type:** Method

### FIN.21:0 - Use this when

The corporation has apparent surplus capital and must decide whether to retain it, pay a dividend or repurchase ownership interests. Establish what is distributable and useful to retain before selecting an amount and form. A routine payment under a sufficient existing decision can go directly to FIN.15.

### FIN.21:1 - Problem frame

The object is a retention or distribution choice for a named corporation and ownership interests. Cash availability, legal distributability, financial value and payment authority are different conditions of that choice.

### FIN.21:2 - Problem

All bank cash can be labelled surplus despite forthcoming payments and investment needs. A buyback can improve per-share accounting measures while transferring value away from remaining owners at an excessive price.

### FIN.21:3 - Forces

Balance current owner returns, valuable investment, liquidity, financing flexibility and ownership effects. Distinguish a sustainable recurring commitment from a one-time return.

### FIN.21:4 - Solution

1. Recover usable cash, existing payment and funding commitments, reserves and restrictions through adequate FIN.2 and FIN.12 results. Obtain the applicable distributability, solvency, tax and authority facts where they affect the action.
2. Compare retention for actual investment, liquidity or financing needs with return to owners. Use FIN.9 for competing capital uses and FIN.11 for financing consequences. A vague future opportunity is not the same as a selected project, but preserving access can still have supported value.
3. Set the amount and timing that the corporation can support under the relevant adverse states. Separate a recurring dividend policy from a special distribution; include the consequences of establishing or changing expectations where they matter.
4. Compare the forms. The corporation pays a dividend to eligible holders according to the rights attached to their interests. A repurchase exchanges company cash for specified interests at a price, changing ownership quantities and potentially their distribution. Include actual tax, transaction, liquidity, control and legal conditions.
5. Compare a repurchase price with the value of the interests on matching grounds; do not use an increase in earnings per share alone as proof of value creation.
6. Return a retention decision or conditional payout recommendation with its amount, form, timing and constraints. Obtain the actual decision and execute through FIN.15 when required.

### FIN.21:5 - Archetypal Grounding

Usable cash is 100, unavoidable forthcoming payments are 70 and minimum reserve is 20. Only 10 remains before any further investment or distribution. If a selected feasible investment needs 6, at most 4 remains on these cash grounds. Paying 20 based on the original bank balance would exceed the 4 available for distribution after the selected investment.

In a separate simplified comparison, a company worth 200 has ten identical shares and no other claims. Repurchasing two shares at 25 costs 50 and leaves value 150 across eight shares: 18.75 each. Under the stated unchanged value grounds, the initial value per share was 20, so overpaying harms remaining owners. With the same 50 paid as a proportional dividend, a holder receives 5 for each original share and keeps that share, now worth 15, totaling 20 per share before any tax or transaction effects. All ten shares remain outstanding after the dividend. The examples isolate the price effect; actual forms require their own conditions.

### FIN.21:6 - Bias-Annotation

A controlling owner's preference may differ from other owners' cash, tax or control interests. Market price and estimated value can differ for a reason; a repurchase conclusion inherits that valuation uncertainty.

### FIN.21:7 - Conformance Checklist

Is the amount supported by dated cash and applicable restrictions? Are retained uses and adverse states considered? Are the actual interests, price, timing and ownership effects clear? Does the advice distinguish a recurring policy from one payment and an approved action from a proposal?

### FIN.21:8 - Common Anti-Patterns and How to Avoid Them

Distributing the entire cash balance ignores commitments; calculate the available amount. Treating EPS accretion as value creation ignores the purchase price; compare interests and value. Assuming unused borrowing capacity makes a payout harmless omits future access and service risk; use FIN.11–12.

### FIN.21:9 - Consequences

The result can justify a smaller payout, retention or a different form. It gives owners and decision makers a financial explanation while retaining the institutional conditions of execution.

### FIN.21:10 - Architectural Rationale

Retention and distribution are competing capital uses with distinct ownership consequences. They deserve an explicit choice instead of becoming an unexplained residual of the investment budget.

### FIN.21:11 - SoTA-Echoing

The [CFA dividend and repurchase reading][CFA-PAYOUT] supplies payout form, policy and constraint distinctions. FIN.21 adopts their joint comparison and makes the cash limit and repurchase price replayable. Compared with an automatic payout of reported surplus, it preserves funded commitments and owner-value effects; changed investment or restriction grounds reopen it.

### FIN.21:12 - Relations

FIN.2 supplies liquidity, FIN.7 the needed interest value, FIN.9 investment alternatives and FIN.11–12 financing conditions. FIN.16 returns advice and FIN.15 performs an authorized distribution.

### FIN.21:End

## FIN.22 - Compare Financial Restructuring and Recovery Routes

**Type:** Method

### FIN.22:0 - Use this when

Ordinary financing or repayment is no longer adequate, and the corporation must compare an extension, amended claims, new funding, asset sale, broader restructuring or exit. Compare viable routes and the actual recoveries of affected claimants. A narrow covenant remedy that already suffices remains in FIN.12.

### FIN.22:1 - Problem frame

Discounting recoveries to a common date requires familiarity with present value and risk-adjusted required returns. A qualified supplied recovery valuation can be used directly on its stated grounds.


The finance practitioner compares routes through financial distress for the debtor's stated receiving question. The object is each route's financed operating and claim-treatment consequences over time. Negotiation, formal proceedings and legal priority require the applicable institutional methods and authority.

### FIN.22:2 - Problem

A larger nominal recovery can be worse when it arrives much later or depends on unfunded continuation. Aggregate enterprise value can hide who receives it, new financing claims, continuing losses and consent requirements.

### FIN.22:3 - Forces

Preserve viable value while respecting time, cash urgency, claimant differences and consent. Use uncertain recovery estimates without treating a debtor's preferred plan as an agreement.

### FIN.22:4 - Solution

1. State the debtor's question, current cash runway and obligations, affected claimants and the latest dates at which choices remain available. Obtain the applicable legal and contractual facts for any route whose availability depends on them.
2. Form credible alternatives: consensual amendment or extension, operational and financial restructuring, new capital, asset or business sale, and available formal or exit routes. Identify the operating changes required to make a continuation viable.
3. Project each route's timed operating and realization cash, process and disposal costs, taxes, collateral effects and interim finance. Establish who can actually provide interim money and under what consent, security and repayment conditions.
4. Apply the actual proposed or applicable treatment of claims. Calculate what each materially affected class or claimant receives, when, in which form and with what risk. A distribution to one claimant is not the same as value available to all.
5. Compare recoveries on a common valuation date and matching currency, timing and risk grounds. Use ranges or scenarios for uncertain realization and timing. Keep contractual claim amount, expected payment and present value distinct.
6. Examine whether the required consents, implementation capacity and interim funding make the route feasible. A financially preferable offer may still be rejected; report whose agreement is needed without asserting that financial superiority grants authority.
7. Return the route comparison, conditional proposal or reason no supported route remains. Identify the immediate funded action or specialist question that changes survival or feasibility. Keep any applicable notice or filing obligation with its actual institutional source.

### FIN.22:5 - Archetypal Grounding

A constructed debtor CFO asks whether to propose an extension giving a lender a better financial recovery. That lender is owed 100; no other claimant shares the net recoveries in this illustration. Exit yields 65 now. Restructuring yields an expected 80 after one year. Both figures are net of the applicable operating, tax, restructuring or exit costs and interim-finance repayment. All amounts share a currency and valuation date; a matching lender valuation rate of 10% is supplied.

| Route | Expected net lender payment | Present value |
| --- | ---: | ---: |
| Exit | 65 now | 65.00 |
| Extension | 80 in one year | 72.73 |
| Slower extension variant | 80 in three years | 60.11 |

The one-year extension supports a conditional proposal on these financial grounds. Moving the same 80 to year three reverses that preference. Neither comparison establishes actual lender consent or interim funding. If continuation needs money that no available arrangement supplies, exclude that route from the actionable set or state the specific funding condition.

With several creditors, repeat the payment treatment for their actual claims and priorities. Do not distribute these single-lender amounts pro rata by assumption; a different security interest or consent rule can change both recoveries and feasible routes.

### FIN.22:6 - Bias-Annotation

Debtors, secured creditors, unsecured creditors and owners can value timing and outcomes differently. Recovery estimates can be strategically optimistic or pessimistic. A selected discount rate does not remove uncertainty about realizable proceeds.

### FIN.22:7 - Conformance Checklist

Can the reader identify whose recovery is compared and replay net payments at their dates? Are operating viability, process costs and interim-finance repayment included? Are claim treatment and required consents grounded in the actual route? Is the feasible set distinct from financially attractive but unsupported proposals?

### FIN.22:8 - Common Anti-Patterns and How to Avoid Them

Comparing 80 later with 65 now as simple amounts ignores time and risk; use a matching valuation. Treating group value as every creditor's recovery omits claim treatment; allocate by the actual arrangement. Counting interim funds as free value ignores their repayment and priority; include the complete financing consequence.

### FIN.22:9 - Consequences

The corporation receives a financially interpretable restructuring proposal or a precise reason a route cannot be relied on. It can support negotiation while remaining distinct from an accepted plan or successful recovery.

### FIN.22:10 - Architectural Rationale

Distress changes both the feasible choices and the treatment of claims. The method connects operating value, interim cash and claimant recoveries so that a higher aggregate number cannot hide an unfinanceable plan.

### FIN.22:11 - SoTA-Echoing

The [World Bank's 2022 workout toolkit][WB-WORKOUT] supplies viability, recovery, consent and interim-finance concerns. FIN.22 adapts them to an explicit common-date claimant comparison and the debtor's receiving question. It rejects nominal aggregate recovery as a sufficient ranking; a changed jurisdictional route, claim treatment or financing condition requires a new comparison.

### FIN.22:12 - Relations

FIN.2 establishes cash urgency, FIN.7 supports route-specific values, FIN.10–12 supply financing and covenant facts, and FIN.16 returns conditional advice. [FDM][FDM] resolves disputed parties, positions or event consequences. Specialist restructuring and legal methods carry the actual negotiation or proceeding.

### FIN.22:End

# Part D - Exposure and treasury action

## FIN.13 - Identify and Measure Financial Exposures

**Type:** Method

### FIN.13:0 - Use this when

A change in rates, exchange prices, commodity prices, payment behavior or funding access could affect the corporation. Trace the exposure to actual claims and operations, then measure the consequence relevant to the decision. A reported notional amount alone does not identify the risk.

### FIN.13:1 - Problem frame

The object is the sensitivity of specified corporate value, cash or claims to financial changes over a chosen horizon. Transaction, operating, valuation, counterparty and liquidity effects may coexist, but their measurements answer different questions.

### FIN.13:2 - Problem

Netting different entities or payment dates can hide a funding requirement. A large notional can have a small sensitivity, while an option or collateral requirement can create a large nonlinear or liquidity consequence.

### FIN.13:3 - Forces

Make material risks visible without measuring everything in one generic score. Use simple sensitivities where adequate and more detailed scenarios where timing, correlation or nonlinearity can change the answer.

### FIN.13:4 - Solution

1. Name the exposed corporation, position or activity, decision horizon and outcome of concern: cash needed, earnings variation, value loss or inability to perform. Use [FDM][FDM] for unresolved positions and FIN.4 for the required projection.
2. Trace rate resets, currency receipts and payments, commodity-linked operating cash, customer and counterparty payments, collateral and funding commitments. Distinguish a contractual amount from expected collection and from settled cash.
3. Group or offset exposures only where the decision permits it. Economic offset does not establish legal netting or intraday payment capacity; retain entity, currency and date differences that affect use.
4. Apply suitable measures. For a fixed foreign-currency net receipt, multiply the amount by exchange-rate changes. For rate-sensitive cash, use the actual reset, notional and accrual conventions. For nonlinear instruments, revalue material scenarios rather than extrapolate one small-change sensitivity.
5. Examine concentrations and combined adverse conditions. A customer delay can coincide with an exchange move, collateral call or loss of funding. If a statistical loss measure is used, state its outcome, horizon, probability model and limitations; it does not give a maximum possible loss.
6. Return the exposures and scenarios that can change action, existing protection and residual uncertainty. Use FIN.14 to compare protection, FIN.2 to assess resulting cash needs, or FIN.15 for an execution exception.

### FIN.13:5 - Archetypal Grounding

A constructed corporation expects 100 foreign units from a customer and owes 60 foreign units to a supplier on the same day. If both pay in full, the net economic receipt is 40. A home-per-foreign exchange rate moving from 0.90 to 0.80 changes its home value from 36 to 32, a loss of 4. If the customer instead pays only 30 before the supplier's cutoff, the corporation must obtain 30 foreign units to pay the supplier then. The original net receipt of 40 did not establish payment capacity. If the remaining customer claim of 70 persists under the agreement, retain it separately from that immediate shortage.

### FIN.13:6 - Bias-Annotation

Historical correlations may fail when liquidity is most scarce. An aggregate group view can omit local access constraints. A favorable expected receipt can conceal a concentrated counterparty obligation.

### FIN.13:7 - Conformance Checklist

Is the measured outcome, entity, horizon and unit clear? Can the sensitivity be traced to actual terms or operations? Are offsets usable for the claimed purpose? Do material timing, credit and nonlinear scenarios survive the aggregation?

### FIN.13:8 - Common Anti-Patterns and How to Avoid Them

Treating a notional as value at risk conflates amount and sensitivity; calculate the consequence. Netting across dates can remove an actual cash gap; retain the payment timeline. Calling a quantile a worst-case bound overstates its claim; keep the modeled tail limitation.

### FIN.13:9 - Consequences

The corporation can decide which exposure needs protection, funding or acceptance. The account may show that a liquidity or credit action matters more than reducing a headline market-risk number.

### FIN.13:10 - Architectural Rationale

Exposure begins with what changes for the corporation. Separating sensitivity, collection and settlement makes measures useful for action without demanding a universal risk model.

### FIN.13:11 - SoTA-Echoing

The [AFP treasury specification][AFP] includes market, credit, counterparty and liquidity risk within treasury practice. The [CFA contingent-claims reading][CFA-OPTIONS] explains the limits of local option sensitivities. FIN.13 combines those concerns with actual payment conditions rather than accepting notional or aggregate net exposure as a complete answer.

### FIN.13:12 - Relations

FIN.2 assesses cash consequences, FIN.14 compares protection and FIN.15 handles actual performance. FIN.4 and [FDM][FDM] supply missing projections and position meanings. FIN.17 updates exposures whose grounds have changed.

### FIN.13:End

## FIN.14 - Design Hedges and Financial Risk Transfer

**Type:** Method

### FIN.14:0 - Use this when

A financial exposure matters enough to consider changing, offsetting or transferring it. Compare the protection obtained with cost, residual risk and cash demands. An existing adequate hedge can remain in use within its conditions.

### FIN.14:1 - Problem frame

The object is a protection arrangement for a specified exposure. It can change the underlying activity, use a natural offset, or introduce a derivative, insurance or other applicable transfer. Designing it does not establish that a contract is executed or that the underlying customer will pay.

### FIN.14:2 - Problem

A hedge can reduce price uncertainty while adding volume, basis, margin, credit or funding risk. Matching only the headline notional can leave the corporation with an obligation it cannot settle.

### FIN.14:3 - Forces

Reduce consequential downside while retaining useful flexibility and affordable cash requirements. Compare risk reduction with its price and the conditions under which protection actually works.

### FIN.14:4 - Solution

1. Start from the outcome and exposure in FIN.13. State which change the protection should limit, over what period and for which entity; distinguish cash protection from accounting presentation.
2. Form feasible alternatives: change currency or pricing terms, alter timing or activity, use a reliable natural offset, purchase optional protection, or enter a forward, swap or other appropriate arrangement. Include acceptance of the exposure where allowed.
3. Match amount, underlying reference, currency, reset and settlement dates, exercise conditions and remaining flexibility. Use FIN.8 for a needed option value and [FDM][FDM] for disputed contractual behavior.
4. Project the combined underlying and protection cash in the material scenarios. Include partial or late underlying performance, basis changes, margin or collateral, counterparty failure and termination where these affect the choice. A price hedge is not a guarantee of underlying volume or credit.
5. Compare costs, residual exposures and peak funding needs. Obtain actual legal enforceability and accounting treatment when the proposed use relies on them; a cash-protection comparison can be complete without claiming a reporting qualification.
6. Return the selected design or conditional recommendation, expected protection, exposure left open and what would require resizing, closing or replacing it. FIN.15 executes within authority and verifies settlement.

### FIN.14:5 - Archetypal Grounding

The corporation expects a customer to pay 100 foreign units on day 30. A physical forward obliges it to deliver 100 foreign units and receive 90 home units that day. Assume the customer pays only 60, the unpaid claim of 40 remains, and the forward still requires delivery of 100. At spot 0.95 home per foreign unit, buying the missing 40 costs 38 home units.

If the corporation obtains that money and buys the currency in time, it delivers 100 and receives 90: current net home cash from the purchase and forward is 90−38 = 52, with the customer claim of 40 foreign units still outstanding. If it cannot fund or purchase the missing currency, there is an execution problem. The forward did not eliminate credit or volume risk.

For a separate rate example, debt pays a floating reference plus 2%, and a swap on the same notional and dates receives exactly that floating reference and pays fixed 4%. The matched net rate is 6% before other costs. A different reference, reset or floor breaks that simple cancellation and must be modeled.

### FIN.14:6 - Bias-Annotation

A low premium or zero initial payment can conceal later collateral and termination costs. A reported hedge ratio can hide uncertainty in the exposure volume. The chosen protection may transfer risk to a counterparty with correlated weakness.

### FIN.14:7 - Conformance Checklist

Can the reader replay combined cash under normal and consequential adverse performance? Do notional, reference and dates match the claimed offset? Are margin, funding and counterparty effects included where material? Is any accounting or enforceability conclusion supported by its applicable facts?

### FIN.14:8 - Common Anti-Patterns and How to Avoid Them

Declaring the exposure “fully hedged” from matching notional hides partial collection; model the event. Treating a zero-cost contract as free ignores contingent payments and collateral. Removing an unpaid customer claim after settling the derivative confuses two positions; retain their separate effects.

### FIN.14:9 - Consequences

The result specifies what the corporation is protected against and what it must still fund or bear. The comparison can support choosing more expensive optional protection when volume uncertainty makes a fixed delivery obligation unsuitable.

### FIN.14:10 - Architectural Rationale

Comparing the combined activity and instrument reveals the protection's actual result. Separating design, execution and remaining claims prevents a desired risk reduction from being reported as an accomplished financial effect.

### FIN.14:11 - SoTA-Echoing

[FDM][FDM] supplies the conditional instrument and event distinctions; [CFA's option treatment][CFA-OPTIONS] supplies optional-payoff reasoning. FIN.14 uses both within a combined cash comparison, rather than treating instrument name or notional equality as protection. Changed underlying performance or settlement terms reopen the design.

### FIN.14:12 - Relations

FIN.13 supplies exposure, FIN.8 option value, FIN.2 funding consequences and FIN.15 execution. FIN.16 returns a material hedge recommendation. A legal or accounting qualification remains with its applicable specialist method.

### FIN.14:End

## FIN.15 - Execute Treasury and Liquidity Decisions

**Type:** Method

### FIN.15:0 - Use this when

A permitted cash payment, borrowing, short-term investment, distribution or hedge action must now be carried out. Select the actual available execution and verify its effect. A material change in the decision's conditions returns to the relevant comparison instead of being silently absorbed into execution.

### FIN.15:1 - Problem frame

The object is a treasury action and the resulting financial position at its effective time. An authorized decision, submitted instruction, provider confirmation and completed settlement are different facts. Existing delegated limits can permit routine action without a new approval.

### FIN.15:2 - Problem

A payment can be submitted but miss the cutoff; a borrowing can be booked without usable proceeds; a liquid-looking investment can mature after the money is needed. A changed beneficiary or false instruction can divert the intended action.

### FIN.15:3 - Forces

Complete the action in time while preserving authorization, account and settlement controls. Compare provider access, service, fees and concentration without repeating a finished financing or investment decision.

### FIN.15:4 - Solution

1. Recover the selected action, permitted performer, account and limits, required amount and date, and material conditions. Use the current authorized arrangement directly when adequate.
2. Confirm funds, drawable capacity or deliverable assets and the actual provider's timing. Where provider choice matters, compare access, service reliability and cutoff times, fees and concentration across available providers. For short-term investment, derive the amount and latest useful return date from the cash plan; compare preservation of principal, liquidity, credit concentration, custody, fees and return within the permitted mandate.
3. Apply the controls relevant to the transaction: validated counterparty and beneficiary, trusted change verification, separation of initiation and approval where required, secure access and applicable account or signatory limits. A provider message alone does not amend those controls.
4. Execute through the permitted route with the actual price, amount, currency, settlement date and reference terms. If terms leave the authorized bounds or remove the financial rationale, return the changed choice before committing.
5. Inspect provider confirmations and the actual resulting balances, positions or settlement evidence. Reconcile amount, fees, date and counterparty; prevent duplication when an instruction is pending or its outcome is uncertain.
6. Resolve a failed or partial execution through the provider's supported recovery and the relevant decision authority. State what changed, what remains owed and the next funded action. Use [FDM.4][FDM] where the effect of a posting or settlement is disputed.

### FIN.15:5 - Archetypal Grounding

A constructed treasury plan has usable cash 160, a payment of 100 on day 7 and a required reserve of 20 throughout a 30-day horizon, with no other flows. At most 40 can be placed in an investment locked until day 30 on these grounds. Investing 60 would leave zero after day-7 payment and breach the reserve. A quoted higher yield does not correct that timing failure. The treasurer also needs acceptable provider and instrument terms before placing the 40.

For FIN.14's partial-receipt hedge, the required foreign-currency purchase costs 38 home units. If only 20 is usable, execution has an 18-unit funding need. A submitted purchase order is not proof that 40 foreign units were delivered. After actual purchase and forward settlement, reconcile the home payments and receipt and retain the unpaid customer claim.

### FIN.15:6 - Bias-Annotation

Operational convenience can concentrate balances or authority with one provider or person. A familiar instrument label can conceal changed liquidity terms. The intended action can differ from the effect of a processed instruction.

### FIN.15:7 - Conformance Checklist

Was the action within actual authority and limits? Were funds or assets available by the required cutoff? Were relevant beneficiary and account controls applied? Does observed settlement support the claimed resulting position, and is any pending or partial state explicit?

### FIN.15:8 - Common Anti-Patterns and How to Avoid Them

Retrying an uncertain payment can pay twice; recover its status through the provider first. Selecting a term investment solely by yield ignores the cash return date; use the timeline. Treating a confirmation as the same fact as final settlement can conceal an exception; verify the effect required by the decision.

### FIN.15:9 - Consequences

Treasury can state the completed action and resulting position or identify a specific remaining obligation and recovery need. Execution evidence supports this transaction, not a general claim that the chosen policy is effective.

### FIN.15:10 - Architectural Rationale

The method ends in the financial effect needed by the corporation. Keeping instructions, confirmations and settlement distinct makes recovery possible without changing the intended decision by assumption.

### FIN.15:11 - SoTA-Echoing

The [AFP treasury task specification][AFP] supplies execution, provider, cash and control responsibilities. [FDM.4][FDM] supplies the distinction between instructions and actual financial effects. FIN.15 combines them around the required settlement result; it rejects submission as sufficient evidence of payment and reopens when actual terms exceed the permitted choice.

### FIN.15:12 - Relations

FIN.2 supplies cash constraints; FIN.10 supplies financing terms; FIN.14 supplies hedge design and FIN.21 the distribution choice. FIN.16 handles a changed decision request; FIN.17 refreshes affected forecasts after actual events.

### FIN.15:End

# Part E - Advice, renewal and continuing practice

## FIN.16 - Prepare a Finance Recommendation and Return It for a Decision

**Type:** Method

### FIN.16:0 - Use this when

Financial work must become advice that another person can use to choose or act. Combine the results that matter to that question and state the recommended move, reasons and conditions. A complete direct calculation need not become a formal report when its receiver can use it as it stands.

### FIN.16:1 - Problem frame

The object is a financial recommendation for a specified receiving decision. A memo, conversation or dashboard can carry it. The recommendation describes an action and its grounds; it is distinct from the receiver's decision, an authorization and the later financial effect.

### FIN.16:2 - Problem

A report can contain accurate calculations without saying what choice they support. A conditional financial preference can be read as unconditional permission, or an evidence request can add work that cannot change the decision.

### FIN.16:3 - Forces

Make advice concise without hiding decisive assumptions, disagreement or constraints. Obtain more information when its attainable value warrants the work and delay, while allowing a supported conditional recommendation now.

### FIN.16:4 - Solution

1. Recover the receiver's actual question and available choices. Use FIN.1 or [C.11.DUA][DUA] if the intended use of advice is unclear.
2. Select the material completed financial results and reconcile their shared conditions. Include the recommended action, expected consequence, relevant alternative and the constraint that could change the preference.
3. Distinguish established facts, model assumptions and unresolved conditions. Retain disagreement when a different value or perspective changes the choice. Do not present an average of incompatible conclusions as consensus.
4. State a specific information need only when its answer can change the receiving action or warranted reliance. Compare the whole burden, delay and displaced work with the obtainable gain; a supported conditional recommendation may be enough.
5. Identify the deciding party when a decision or authorization is requested. A routine action under existing authority can proceed through its ordinary method; the advice does not create a new approval requirement.
6. Return the recommendation in the smallest usable form. Name the next action and the trigger for reconsideration. If the grounds do not support a recommendation, state the precise missing choice-changing fact and what remains usable.

### FIN.16:5 - Archetypal Grounding

For FIN.2–3's order, a concise recommendation is: “Use the customer's agreed advance of 96 on day 6 against 100 of the invoice. It leaves 56 on day 7 and produces incremental gain 656, compared with zero cash and gain 655 under the available draw of 43. This preference uses the supplied operating plan and agreement. If the advance is not agreed, use the drawable-facility comparison; if collection moves beyond day 28, obtain a funded repayment path before relying on that facility.” The analyst has completed the comparison and prepared usable advice. The appropriate authorized person still chooses or performs the action under the existing arrangement.

### FIN.16:6 - Bias-Annotation

The receiver may prefer a simple affirmative answer, and the adviser may suppress a condition to make the recommendation persuasive. Material disagreement and the interests excluded from the chosen question need to remain visible.

### FIN.16:7 - Conformance Checklist

Can the receiver identify the recommended action, reason, relevant alternative and condition that changes it? Do the financial results share compatible grounds? Is any new evidence request tied to a possible changed action? Are advice, decision and execution kept distinct?

### FIN.16:8 - Common Anti-Patterns and How to Avoid Them

Ending with “more analysis is needed” without a choice-changing question leaves no next useful move; name the required answer. Reporting only NPV hides funding conditions; state the material ones. Treating a recommendation as authorized action claims an effect it does not supply.

### FIN.16:9 - Consequences

The receiver can act on a supported result or pursue a bounded missing fact. The work can finish as conditional advice even when another party's consent remains unresolved.

### FIN.16:10 - Architectural Rationale

Advice becomes useful through its relation to a receiving choice. Its form and length follow that use, rather than a universal reporting package.

### FIN.16:11 - SoTA-Echoing

[C.11.DUA][DUA] supplies the appraisal of advice and demanded evidence by their receiving value. FIN.16 applies it to connected financial results, including funding and valuation conditions. It replaces a collection of correct but unconnected calculations with actionable conditional advice; a changed receiver or choice reopens the recommendation.

### FIN.16:12 - Relations

The selected FIN methods supply the substantive financial results. [C.11][CHOICE] compares available alternatives when necessary. FIN.15 performs permitted treasury actions and FIN.17 refreshes a recommendation whose relied-on grounds change.

### FIN.16:End

## FIN.17 - Refresh Financial Models and Data

**Type:** Method

### FIN.17:0 - Use this when

A new receipt date, price, contract, accounting input or operating fact may change a financial model or conclusion currently being used. Update the affected result and its conditions. If the change cannot affect that use, a supported no-update conclusion is sufficient.

### FIN.17:1 - Problem frame

The object is a financial model, projection or conclusion together with the grounds on which someone relies on it. A source-data change is distinct from a change in the described contract or actual position.

### FIN.17:2 - Problem

Updating an input file can leave the receiving recommendation stale. Rebuilding every model after any change wastes effort, while treating every assumption change as a new method choice creates unnecessary work.

### FIN.17:3 - Forces

Keep live reliance current without redoing unaffected calculations. Preserve enough connection between grounds and conclusions to identify which change matters, without maintaining an exhaustive registry of every model cell.

### FIN.17:4 - Solution

1. Identify the changed fact or source and the financial use that may depend on it. Recover the previously supported result and its relevant assumptions.
2. Trace the consequence through affected cash dates, amounts, values, ratios, constraints and advice. Distinguish correction of a description, a new expectation, an amended agreement and an actual event.
3. Revise the affected model or projection with the new grounds and recompute the dependent result. Retain unchanged accounts and current supported comparisons. When the changed assumption requires a different method, return that specific choice to FIN.18.
4. Examine the condition most likely to change the action: funding at a due date, sign of value, covenant access, hedge amount or recommendation. Correct any inconsistency introduced by the update.
5. Return the updated model, projection or financial conclusion with its conditions for use. If the needed fact is missing, state the specific reliance limit and what remains usable.
6. Arrange ongoing observation only for an actual continuing use, with a source and trigger that can change action. A one-time calculation does not by itself require continuous monitoring.

### FIN.17:5 - Archetypal Grounding

FIN.2's order was expected to collect 1,200 on day 28. Its draw of 43 supplied net cash 40 and was due with interest, totaling 45, on day 28. A new supported expectation moves collection to day 40; it does not amend the loan. The updated cash projection shows a day-28 gap of 45. The operating contribution before financing remains 660 if all other operating grounds are unchanged. The analyst must reconsider the financing recommendation because repayment on day 28 is now unfunded; the previous net gain of 655 cannot be retained without accounting for a feasible repayment arrangement and its cost. FIN.10 supplies that comparison. By contrast, correcting a customer display name while retaining the same debtor, claim, dates and use may support no financial-model update.

### FIN.17:6 - Bias-Annotation

A convenient new datum can be adopted before its meaning or reliability is understood. Conversely, a model owner can protect an earlier recommendation by treating a consequential change as cosmetic.

### FIN.17:7 - Conformance Checklist

Is the changed fact distinguished from the financial event or agreement it describes? Are all action-changing dependent results updated, and unaffected results retained? Does the return name the actual updated object or a specific no-update reason? Is any ongoing observation justified by continuing use?

### FIN.17:8 - Common Anti-Patterns and How to Avoid Them

Changing an input without recomputing the dependent financial results and reconsidering the advice that uses them can leave the recommendation based on obsolete assumptions; carry the change through to that receiving use. Rebuilding unrelated models increases work without repairing the current answer. Treating a revised forecast as lender consent changes the wrong object; recover actual agreement.

### FIN.17:9 - Consequences

The practitioner returns a current financial result or an explicit reliance limit. This can reopen a financing decision while preserving the supported operating account.

### FIN.17:10 - Architectural Rationale

Refresh follows the connection between a changed ground and its use. It is smaller than redesigning the method and broader than editing a number in a data source.

### FIN.17:11 - SoTA-Echoing

[MA][MA] supplies purpose-qualified forecasts and account differences; [FDM][FDM] distinguishes descriptions from financial positions and events. FIN.17 adopts these distinctions to update relied-on finance conclusions. Compared with blanket refresh or input-only replacement, it follows the action-changing consequence; a changed method basis invokes FIN.18.

### FIN.17:12 - Relations

Every relied-on FIN result can be refreshed through this method. FIN.18 handles a needed method choice, while FIN.16 returns changed advice. The appropriate MA or FDM method supplies a newly unresolved source account.

### FIN.17:End

## FIN.18 - Develop and Refresh Corporate-Finance Methods

**Type:** Method

### FIN.18:0 - Use this when

The present valuation, forecasting, exposure or treasury method fails on a recurring financial difficulty, or a new method may improve the result enough to justify changing practice. Compare the method variants on that question. A changed input value within an adequate method belongs in FIN.17.

### FIN.18:1 - Problem frame

The object is the choice or improvement of a corporate-finance method for a stated use. A new spreadsheet, model implementation or training session can support that method, but adopting the tool does not establish better decisions.

### FIN.18:2 - Problem

A more sophisticated method can improve an average error while missing the cash shortages that matter. A familiar method can persist after its assumptions no longer fit the business. A broad research programme can displace a useful bounded repair.

### FIN.18:3 - Forces

Improve decision quality while accounting for data, skills, explanation, operating cost and delay. Use relevant current knowledge without equating novelty, complexity or source prestige with demonstrated improvement.

### FIN.18:4 - Solution

1. Name the financial difficulty, intended gain and current method's observed or otherwise supported limit. State what result or action would change if the proposed method helped.
2. Compare genuinely different variants, including continued use or a smaller repair. Recover the relevant current professional or research contribution and its conditions; a task syllabus establishes repertoire, not method effectiveness.
3. Choose a comparison appropriate to the claim. For forecasting, use information available at the forecast date and periods withheld from method selection when estimating predictive performance. Include the errors that change cash or action, not only an aggregate fit measure. For valuation or exposure, compare assumptions, limiting cases and decision reversals on the relevant objects.
4. Include implementation, data, explanation, review, runtime and participant burdens. If a further trial could change the choice, compare its attainable value with its whole cost and delay using [C.11.DUA][DUA] as needed.
5. Select the method, qualify its narrower use, propose a bounded trial or continue the supported method. Preserve unresolved claims instead of calling the new method universally superior.
6. Make the selected change usable in the actual finance procedure and explain when to reopen it. FIN.17 updates the affected models; FIN.20 addresses transmission and continued use when those become the problem.

### FIN.18:5 - Archetypal Grounding

In a constructed comparison, a cash forecast triggers action when predicted closing cash is below a reserve of 5. Four withheld periods have actual closing cash 20, 2, −8 and 15. Method A predicts 18, 12, 4 and 16; method B predicts 16, 3, −3 and 13 using only information available at each forecast date. A flags the third shortage but misses the second; B flags both. The comparison identifies a useful difference for liquidity action. Four illustrative cases do not establish general superiority. If B requires a costly new daily data collection, a bounded trial must compare avoided funding failures and unnecessary actions with that burden; the action-changing question is specific enough to decide whether the trial is worth doing.

### FIN.18:6 - Bias-Annotation

A method developer can select favorable cases, leak future information or optimize a convenient metric. Evidence from one corporation or market condition may not support another use.

### FIN.18:7 - Conformance Checklist

Is the difficulty and changed action explicit? Are alternatives genuinely different and compared on relevant cases and information? Does the evaluation include consequential errors and total burden? Is the claimed improvement no broader than the evidence, with a usable continuation or trial outcome?

### FIN.18:8 - Common Anti-Patterns and How to Avoid Them

Choosing by training fit rewards knowledge of the answer; preserve the information boundary. Equating a new tool with a changed financial method hides what actually improves. Requiring another study without a possible changed decision turns uncertainty into unbounded work.

### FIN.18:9 - Consequences

The finance practice gains a qualified method choice, useful repair or bounded trial proposal. It can reject an attractive but costly innovation while retaining a supported simple method.

### FIN.18:10 - Architectural Rationale

Method development is governed by the financial problem and the result it must improve. Keeping it separate from data refresh makes actual methodological assumptions open to comparison without turning routine updates into research.

### FIN.18:11 - SoTA-Echoing

[MA's forecasting contributions][MA] make purpose and consequential differences central; [C.11.DUA][DUA] relates demanded inquiry to its receiving value. FIN.18 applies these ideas to current finance methods and relevant professional sources. It rejects novelty or fit alone as a selection rule; a new failure or materially better attainable method reopens the choice.

### FIN.18:12 - Relations

FIN.17 applies the selected method to relied-on models, FIN.19 reconciles cross-practice effects and FIN.20 addresses continuing use. The direct FIN method and its current domain sources supply the substantive calculation being improved.

### FIN.18:End

## FIN.19 - Reconcile Simultaneous Corporate-Finance Work Across Claims and Horizons

**Type:** Method

### FIN.19:0 - Use this when

Investment, treasury, financing and distribution work each appears reasonable, but their combined commitments conflict or their models describe different situations. Reconcile the actual work and constraints, then compare changes to how the practice is organized. A single disputed cash figure can go directly to FIN.2 or FIN.4.

### FIN.19:1 - Problem frame

The object is the organization of simultaneous corporate-finance practice around actual claims, decisions and horizons. Work overlap, ownership of money, model use, provider dependence and authority are different relations. This method recovers their consequential conflict; it does not turn a reporting hierarchy into a description of all financial work.

### FIN.19:2 - Problem

Two teams can allocate the same available cash while each model passes its local test. Centralizing every decision can remove that conflict at the cost of delay, while merely drawing more views leaves the competing commitments intact.

### FIN.19:3 - Forces

Preserve useful local expertise and speed while making joint constraints effective. Repair a real conflict without moving an unseen burden to operations, counterparties or another time horizon.

### FIN.19:4 - Solution

1. Anchor the question in a representative actual occurrence, or label a future arrangement as prospective. State the financial result at stake and the participants; do not infer performed work from a process diagram.
2. Recover the relations needed to explain the conflict. Distinguish which work overlaps, which entity owns or owes the money, which model describes it for which use, which decisions constrain another, and which provider or capability makes action possible.
3. Reconcile the material dates, baselines and claim meanings. Several copies can describe the same financial position and preserve the same subject and use. A monthly plan and daily cash forecast can instead preserve different detail; explain the loss when one is used in place of the other.
4. Form genuinely different organizations of the work: for example, centralize a limited allocation decision, retain local decisions with a shared dated constraint, change the sequence of commitments, or alter the financing arrangement. Include the cost and limits of each.
5. Compare the conflict and burden under each alternative. Use FIN.9 for capital combinations, FIN.2 for payment timing, FIN.12 for access and FIN.16 for the resulting advice as needed. Examine moved delay, risk, reporting effort, authority burden and loss of useful local information.
6. Select or propose the bounded reconfiguration under the actual authority. State what each participant now needs to know or do and the result that would show the conflict is resolved. Stop adding views when they cannot change the decision.
7. Reopen when a new entity, horizon, commitment, provider or observed occurrence changes the conflict. Use FIN.20 only when transmission or continued use of the arrangement becomes the question.

### FIN.19:5 - Archetypal Grounding

In a constructed prospective case, the corporation has 100 usable cash next week. Operating payments need 60 and the agreed reserve is 20, leaving 20 for additional commitments. An investment team proposes an immediate project outlay of 30, while treasury plans a distribution of 20. The investment team's local view subtracts operating payments but omits the reserve, showing 40 available. Treasury includes the reserve and sees 20 for distribution. Each proposal appears affordable in its team's view; together they require 50 where only 20 is available.

The alternatives differ in practice. Central approval of every payment would enforce one cash decision but add delay to routine payments. A shared dated commitment account can retain routine delegated execution while making the investment and distribution compete for the same 20. A third alternative funds an additional 30 through an obtainable financing arrangement, with its cost and later payment obligation included.

For this case, the corporation can retain routine payment authority and bring the two exceptional capital uses to one allocation comparison. FIN.9 then compares reducing, deferring or funding them on their financial merits. The joint account resolves the incompatible available-cash assumptions; it does not by itself decide which capital use is best. If those proposals occur in different legal entities, actual transfer conditions must also be recovered.

### FIN.19:6 - Bias-Annotation

A central finance view can erase operational knowledge and local restrictions. A collection of descriptions can be mistaken for the practice itself. A tidy organizational chart is not evidence that its work interfaces are effective.

### FIN.19:7 - Conformance Checklist

Is the anchor actual or explicitly prospective? Are work, claims, models, authority and provider relations distinguished where they matter? Do the alternatives change the conflict in different ways? Are moved burdens and the next financial decision explicit?

### FIN.19:8 - Common Anti-Patterns and How to Avoid Them

Forcing every view into one hierarchy hides cross-cutting relations; recover the relation actually used. Calling two spreadsheets two financial positions confuses description with subject; reconcile their meaning. Fixing a treasury conflict by delaying all operating payments moves the failure; compare that consequence.

### FIN.19:9 - Consequences

The practitioner obtains a usable reconfiguration proposal or a selected arrangement, with the remaining financial choice visible. Coordination changes when the participants carry out the selected arrangement. That arrangement can preserve direct local work while making a shared constraint operative.

### FIN.19:10 - Architectural Rationale

A conflict across claims and horizons cannot always be repaired inside one financial model. Comparing the organization of the work exposes alternatives that a larger consolidated spreadsheet alone would hide.

### FIN.19:11 - SoTA-Echoing

[C.32.MWA][MWA] supplies synthesis from several actual relations, the practice–description distinction and comparison of moved burdens. FIN.19 applies that contribution to concurrent corporate-finance commitments. It rejects visual tidiness as the selection criterion; a new representative conflict or material horizon changes the synthesis.

### FIN.19:12 - Relations

FIN.2, FIN.9, FIN.12 and FIN.16 answer the specific financial conflicts. [FDM][FDM] resolves parties and positions. [C.32.MWA][MWA] supplies the architecture method; FIN.20 addresses subsequent transmission and retention when needed.

### FIN.19:End

## FIN.20 - Deliberately Continue and Change Corporate-Finance Culture

**Type:** Method

### FIN.20:0 - Use this when

A useful finance method is not being used, a harmful routine persists, or a valued practice risks being lost. Examine how people learn, recognize, select and retain the actual practice before deciding whether to continue or change it. A numerical model correction belongs in FIN.17.

### FIN.20:1 - Problem frame

The object is the continuation or change of finance practices across a named population and period. A template, training event or policy can influence practice, but producing it does not establish that people use the method or obtain its intended result.

### FIN.20:2 - Problem

Publishing a forecast template can be reported as a forecasting improvement while meetings still negotiate targets and conceal expected cash. Conversely, a working local practice can be displaced by a broad vocabulary or tool programme that adds little practical value.

### FIN.20:3 - Forces

Preserve useful knowledge while improving consequential habits. Distinguish deliberate intervention from distributed uptake, incentives and loss. Obtain enough evidence for the current continuation decision without imposing a study on every small practice.

### FIN.20:4 - Solution

1. Name the population, practice variants and useful financial result. Use actual observations for an obtaining practice, or clearly label a proposed future arrangement.
2. Recover how variants are generated, taught or copied, recognized as legitimate, selected or discouraged, and retained or lost. A repository retains a document; people using its method in decisions is a separate fact.
3. Examine incentives, meeting routines, provider tools and familiar language that mediate use. Distinguish a forecast of expected outcomes, a target and a resource-allocation decision when these meanings affect behavior. People can use a sound distinction in ordinary terms without a company-wide terminology programme.
4. Compare continuing the supported practice, a bounded change and a materially different intervention. Include keeping different local variants or stopping the practice when the population's conditions make those alternatives relevant. State the relation each would change and the expected financial-use consequence. For example, changing how a forecast is discussed differs from distributing a new spreadsheet.
5. Select observation or trial only when its attainable answer can improve the receiving use enough to warrant its full cost and participant burden. Preserve supported current conclusions when a stronger causal explanation remains unresolved.
6. Carry out an authorized intervention through its actual performers when selected. Keep the proposal, performed action, changed practice and financial effect distinct; claim each only on its own evidence.
7. Return a supported continuation, bounded change or stop, with what would reopen it. Preserve useful materials and practices without equating their availability with uptake.

### FIN.20:5 - Archetypal Grounding

In a constructed case, a finance team has a forecast spreadsheet, but six weekly meetings replace the expected collection dates with the dates needed to meet the target. The treasurer therefore receives an optimistic cash view. The proposed repair retains the familiar spreadsheet and changes the meeting: discuss the best-supported collection expectation separately from the target, then decide resource action. A second proposal replaces the whole planning platform. The smaller intervention directly addresses the observed use problem with less transition effort. Its performance would be established by the changed meeting work; continued use by subsequent forecasts retaining genuine expectations; a financial benefit would require evidence of changed cash decisions or outcomes. A published instruction alone establishes none of those later claims.

### FIN.20:6 - Bias-Annotation

Managers may hear agreement while staff continue a different routine. Observed adoption can reflect coercion or temporary attention rather than a retained method. A practice useful to central finance can impose an unrecognized burden on other participants.

### FIN.20:7 - Conformance Checklist

Are population, period and actual or prospective basis explicit? Are transmission, selection, retention and financial effect distinguished? Does the proposed action change the relation responsible for the difficulty? Is continued use supported separately from publication or training attendance?

### FIN.20:8 - Common Anti-Patterns and How to Avoid Them

Counting downloaded templates as improved finance confuses access with use; inspect the decision practice. Requiring everyone to adopt new terminology can displace the useful distinction; use familiar language when sufficient. Attributing a cash improvement to training without examining other changes overstates causality.

### FIN.20:9 - Consequences

The corporation can continue a useful practice or make a bounded intervention with a meaningful return condition. It avoids replacing functioning local knowledge merely because a newer tool or vocabulary is available.

### FIN.20:10 - Architectural Rationale

Finance practice persists through people, incentives and repeated use as well as documents. Keeping deliberate actions and distributed continuation distinct makes both improvement and preservation assessable.

### FIN.20:11 - SoTA-Echoing

[C.36][CULT] supplies the distinctions among cultural variation, transmission, selection, retention and deliberate intervention. [MA.9][MA] connects account use with behavior; its budgeting sources provide a historical anchor for separating forecast, target and allocation. FIN.20 adopts the practical distinction while withholding unsupported adoption and effect claims.

### FIN.20:12 - Relations

FIN.18 supplies a selected method change, FIN.17 its model update and FIN.19 a practice reconfiguration when needed. [C.36][CULT] supplies the cultural method and [C.11.DUA][DUA] the appraisal of a demanded inquiry. Existing authority governs any actual intervention.

### FIN.20:End

# References

Copyright © Anatoly Levenchuk. The original framework text and worked examples are licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). The [licensing notice](https://github.com/ailev/FPF/blob/main/LICENSING.md) states scope and attribution terms. Referenced third-party works retain their own terms.

## Edition record

**Framework and edition:** Corporate Finance Principles Framework, FIN 1.0.\
**Language:** English.\
**Edition date:** 11 September 2026.\
**Boundary:** The twenty-two FIN patterns, practical entries, Preface and reference material in this publication.

For a precise citation, name the framework, FIN 1.0 and the pattern or section, for example: “Anatoly Levenchuk, Corporate Finance Principles Framework, FIN 1.0, FIN.9 — Compare Capital Investments and Allocations.” Mark adaptations and retain the applicable attribution.

Use current market, operating and institutional facts for a real decision. FIN.17 refreshes relied-on financial results; FIN.18 reconsiders their method. Revisit a cited supplying edition when its contribution changes the receiving use. A copied publication preserves its edition's text, not continuing accuracy of the user's data or continuing access to every external source.

## Source guidance

The pattern bodies state the adopted contribution and comparison. These locators let a reader examine the sources or obtain greater professional depth. They do not claim full access to restricted curricula or compliance with an unread standard.

| Source | Contribution and reading scope |
| --- | --- |
| [CFA Institute, Working Capital and Liquidity, 2026][CFA-WC] | Public introduction and learning outcomes for liquidity and the cash-conversion mechanism. |
| [CFA Institute, Capital Investments and Capital Allocation, 2026][CFA-CAPITAL] | Public treatment of incremental investment analysis and comparison limits. |
| [CFA Institute, Free Cash Flow Valuation, 2026][CFA-FCF] | Public FCFF/FCFE and matching discount-basis explanation, including continuing-value concerns. |
| [CFA Institute, Valuation of Contingent Claims, 2026][CFA-OPTIONS] | Public introduction, outcomes and summary of replication assumptions, option valuation and sensitivities. |
| [CFA Institute, Analysis of Dividends and Share Repurchases, 2026][CFA-PAYOUT] | Public payout-form and policy discussion. |
| [CFA Institute, Corporate Restructuring, 2026][CFA-RESTRUCT] | Public transaction and pro forma concerns, adapted here to the corporation's receiving question. |
| [Association for Financial Professionals, CTP Test Specifications][AFP] | Published treasury task domains. These establish professional coverage, not efficacy of a particular method. |
| Julie Dahlquist and Rainford Knight, OpenStax, Principles of Finance 2e, 24 June 2026: [17.1][OS-STRUCTURE] and [17.3][OS-WACC] | Capital mix, opportunity cost, weighted capital cost and estimation assumptions. These are the identified sections used, not a claim to have synthesized the whole textbook. |
| [International Valuation Standards Council, standards overview][IVSC] | Public overview of scope, basis, approaches, data, models and reporting. Full engagement requirements must be obtained for an actual standards claim. |
| [World Bank, A Toolkit for Corporate Workouts, 2022][WB-WORKOUT], sections 2.3 and 2.6–2.9 | Viability and recovery, negotiation and consent, and interim finance. The toolkit does not establish current law for every jurisdiction. |
| [MA 1.0][MA] and [FDM 1.0][FDM] | The supplied accounting and financial-modeling methods and their qualified source contributions. MA's Bragg, Caspari and Bogsnes sources are historical anchors used for particular distinctions, not labels for the latest line in all finance. |
| [FPF][FPF], especially [C.11][CHOICE], [C.11.DUA][DUA], [C.32.MWA][MWA] and [C.36][CULT] | General methods reused for the specific relations explained in the Preface and FIN bodies. |

[MA]: MANAGEMENT-ACCOUNTING-PRINCIPLES-FRAMEWORK.md
[FDM]: FINANCIAL-DOMAIN-MODELING-PRINCIPLES-FRAMEWORK.md
[OPS]: OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md
[CHOICE]: ../FPF-Spec.md#c11---decision-theory-decsn-cal
[DUA]: ../FPF-Spec.md#c11dua---decision-useful-advice-and-evidence-demands
[MWA]: ../FPF-Spec.md#c32mwa---practice-architecture-synthesis-from-several-structures
[CULT]: ../FPF-Spec.md#c36---cultural-evolution-and-cultural-evolution-engineering
[FPF]: https://github.com/ailev/FPF
[CFA-WC]: https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/working-capital-and-liquidity
[CFA-CAPITAL]: https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/capital-investments-and-capital-allocation
[CFA-FCF]: https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/free-cash-flow-valuation
[CFA-OPTIONS]: https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/valuation-contingent-claims
[CFA-PAYOUT]: https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/analysis-of-dividends-and-share-repurchases
[CFA-RESTRUCT]: https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/corporate-restructuring
[AFP]: https://ctpcert.financialprofessionals.org/overview/ctp-test-specifications
[OS-STRUCTURE]: https://openstax.org/books/principles-finance-2e/pages/17-1-the-concept-of-capital-structure
[OS-WACC]: https://openstax.org/books/principles-finance-2e/pages/17-3-calculating-the-weighted-average-cost-of-capital
[IVSC]: https://ivsc.org/standards/
[WB-WORKOUT]: https://documents1.worldbank.org/curated/en/982181642007438817/pdf/A-Toolkit-for-Corporate-Workouts.pdf
