# Explanation Design Principles Framework

**DocID:** `EXD` within **FPF Library**.

Develop or use a warranted explanation of the connection a recipient needs. Choose the question, account, expression and any assistance the intended use requires.

Anatoly Levenchuk, with AI-assisted development and review.

Edition dated 23 October 2026.

**License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) for original framework content; third-party material retains its own terms.


# Table of Contents

Use the public units for orientation and source access. The pattern index below lists six methods by the question each helps answer. The EXD numbers are stable addresses for the methods. Enter where the task needs an explanation, example, expression, exchange or comparison.

## Public units

| Unit | Reader use |
| :--- | :--- |
| [Readme](#readme) | Follow an explanation through a changed question, a learner's retry and a comparison that separates content repair from a change of form. |
| [Explanation Design Principles Framework Architectural Reference](#explanation-design-principles-framework-architectural-reference) | Find the grounds for an explanation, identify what its recipient can reconstruct and, when a reply is available, use it to decide what the exchange needs. |
| [EXD.Reference:1](#exdreference1---the-practice-and-the-problem-it-solves) | The practice and the problem it solves |
| [EXD.Reference:2](#exdreference2---the-distinctions-that-change-the-work) | The distinctions that change the work |
| [EXD.Reference:3](#exdreference3---obtain-and-carry-the-subject-explanation) | Obtain and Carry the Subject Explanation |
| [EXD.Reference:4](#exdreference4---a-worked-exchange-and-its-consequential-returns) | A worked exchange and its consequential returns |
| [EXD.Reference:5](#exdreference5---why-these-methods-form-a-useful-language) | Why these Methods form a useful language |
| [EXD.Reference:6](#exdreference6---assurance-limits-and-practical-consequences) | Assurance, limits and practical consequences |
| [EXD.Reference:7](#exdreference7---framework-and-subject-suppliers) | Framework and subject suppliers |
| [EXD.Sources:1](#exdsources1---relied-on-contributions-and-their-limits) | Relied-on contributions and their limits |
| [EXD.Profiles - Use profiles](#use-profiles) | Adapt the Methods to instructional, technical/advisory and human–AI explanation. |
| [Explanation Design Principles Framework Sources and Edition Notes](#explanation-design-principles-framework-sources-and-edition-notes) | Recover relied-on research contributions, their limits and conditions for reconsideration. |
| [EXD.Edition - Name and citation](#name-and-citation) | Cite the framework and recover its local naming settlement. |

**Patterns by working question**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [EXD.1 - Establish and Revise What a Recipient Needs Explained](#exd1---establish-and-revise-what-a-recipient-needs-explained) |  Stable  | question, purpose, contrast, changed condition. Which question needs explaining? Did the question change, or was the inference wrong? Establish or revise the question and identify a missing premise or policy choice if it matters. | FPF A.2.9; EXD.4 |
| 2 | [EXD.2 - Build and Bound an Explanatory Example](#exd2---build-and-bound-an-explanatory-example) |  Stable  | worked example, correspondence, analogy, counterexample. How does the instance illustrate the rule, and where does that correspondence end? Assess an existing example or construct one that shows the required distinction. | EXD.1; HCD.6 |
| 3 | [EXD.3 - Coordinate the Expression of an Explanation](#exd3---coordinate-the-expression-of-an-explanation) |  Stable  | prose, table, diagram, demonstration, access, cognitive load. Is the missing contribution a relation, a usable form or help? Which form would help the recipient recover the relation? A single form may suffice. Use complementary forms when their different contributions matter. | EXD.1; FPF C.37, C.2.8 |
| 4 | [EXD.4 - Co-Construct and Repair an Explanation in Dialogue](#exd4---co-construct-and-repair-an-explanation-in-dialogue) |  Stable  | dialogue, feedback, changed question, diagnosis, close. What does the recipient’s contribution establish or change? Interpret the reply. That finding can answer a question about the exchange or guide a clarification, correction or close. | EXD.1; FPF A.2.9 |
| 5 | [EXD.5 - Guide a Recipient's Own Explanation](#exd5---guide-a-recipients-own-explanation) |  Stable  | learner explanation, self-explanation, feedback, assistance, retry. Which relation did the recipient use, and with what help? Interpret their explanation. If learning calls for correction, offer relevant feedback and another opportunity. | EXD.1, EXD.2; HCD.9, HCD.10 |
| 6 | [EXD.6 - Compare Explanations for the Recipient's Use and Decide Whether a Repair Is Worthwhile](#exd6---compare-explanations-for-the-recipients-use-and-decide-whether-a-repair-is-worthwhile) |  Stable  | structural recovery, reader, effort, comparison, repair. What can the recipient reconstruct under these conditions? Keep an adequate explanation, identify what remains unknown or compare the gain from a change with its burden. | EXD.1; FPF C.2.8, C.11.CRC, C.11; C.37.CF, HCD.19 |

# Readme

## Practical entries

Explanation Design connects a recipient’s question with a warranted account in a form they can use. An example can show the required relation. A reply may expose a missing step, change the question or show that the current explanation is sufficient. Select the method that addresses the difficulty you have.

The two cases below illustrate different uses of the six methods in the Table of Contents. See [Obtain and Carry the Subject Explanation](#exdreference3---obtain-and-carry-the-subject-explanation) for the mathematical, causal, technical or advisory basis of an explanation. A missing derivation or recommendation premise needs grounds appropriate to that claim.

Use these methods in the language of the work. A practitioner or service can produce the explanation or use the account directly. An assisting agent can explain or apply a method in the language and terminology the recipient uses. Keep the distinctions needed to answer the question.

### EXD-CHANGE — Distinguish a changed question from a mistaken inference

**Situation:** A recipient rejects an answer or offers another result. It is unclear whether they have changed the question, missed a relation or disputed a premise.

**Question:** What should the next explanation answer, and which part of the existing account can it reuse?

**Possible result:** the answer to the revised question, a justified correction under the original question, or an account of the disputed premise, including any grounds still needed.

**Start with** [EXD.4 - Co-Construct and Repair an Explanation in Dialogue](#exd4---co-construct-and-repair-an-explanation-in-dialogue) when an actual reply is available. Use [EXD.1 - Establish and Revise What a Recipient Needs Explained](#exd1---establish-and-revise-what-a-recipient-needs-explained) if the reply changes what the account must explain.

**Stop or return** when the requested explanatory work is complete. Evidence of the recipient using the relation can settle a question about their understanding. A recipient who understands a recommendation may decline it. If the remaining issue is what to choose, identify who may make that choice.

1. **Recover the relation the question needs.** In the [worked exchange](#exdreference4---a-worked-exchange-and-its-consequential-returns), two values have mean 3 and six values have mean 8. Their total is `2 × 3 + 6 × 8 = 54`. Dividing by the eight individual observations gives 6.75. If each branch instead receives equal weight, the mean of 3 and 8 is 5.5.
2. **Show that correspondence.** Use [EXD.2 - Build and Bound an Explanatory Example](#exd2---build-and-bound-an-explanatory-example) to connect each count and mean to its group sum. Use [EXD.3 - Coordinate the Expression of an Explanation](#exd3---coordinate-the-expression-of-an-explanation) when a table showing these quantities and the weighting condition would help. A single clear form suffices. Adding the missing relationship between count, mean and sum changes the content.
3. **Use the reply.** If the recipient says “Each branch should have equal influence regardless of size,” EXD.1 helps establish the revised target. The answer is 5.5. The result 6.75 still answers the individual-weighting question. If the target remains equal weight per individual but the recipient divides the sum of two branch means by two, EXD.4 helps locate the error. Explain how each group mean and count give its sum, then divide the total of those sums by the number of individuals. If the issue is which policy should govern the report, use the applicable policy or seek a choice from its holder when necessary.
4. **Use the learner’s own explanation when that is the purpose.** With [EXD.5 - Guide a Recipient's Own Explanation](#exd5---guide-a-recipients-own-explanation), retain the learner’s initial answer and the help they received. If the distinction needs practice, give feedback on groups versus individuals and offer a changed case. Three values with mean 4 and nine with mean 8 give `(12 + 72)/12 = 7`. Equal branch weights give 6. An immediate correction shows performance under those conditions. Independent performance after a delay needs evidence from that condition.

In advising, “Why does this assignment fit my present strengths?” and “Why would it develop a missing capability?” call for different grounds. A change to the second question requires the rationale for expected development. If the recipient understands that rationale and prefers another setting, respect their preference and identify its bearing on the choice they actually face.

### EXD-REPAIR — Repair what the recipient cannot use without rewriting everything

**Situation:** An explanation fails in use, and plausible repairs include more subject content, another form or additional help. These changes would contribute different things.

**Question:** Which repair addresses the actual difficulty, and is it worth its burden compared with the available explanation?

**Possible result:** a justified repair, an adequate explanation to retain, or the subject or reader evidence missing for the particular comparison.

**Start with** [EXD.6 - Compare Explanations for the Recipient's Use and Decide Whether a Repair Is Worthwhile](#exd6---compare-explanations-for-the-recipients-use-and-decide-whether-a-repair-is-worthwhile). Identify the relation the recipient needs and the criterion for its use.

**Stop or return.** Keep an explanation that satisfies the intended use. A supported subject result can justify correcting an explicit false claim. For a mathematical error, the definitions may suffice. For a question about what a reader can recover, use suitable existing evidence or obtain an observation if its attainable contribution warrants the effort.

1. **Identify the required relation.** Consider a proposed explanation of active effort on one person’s task. The accounting rule counts time spent working on that task. The draft instead uses the elapsed time from start to handoff. On an uninterrupted task they agree, so that case cannot distinguish the rules.
2. **Choose an example that distinguishes the rules.** Work from 09:00 to 10:00 and again from 11:00 to 12:00 gives two hours of active effort and three hours elapsed, provided the person does no task work in the intervening hour. Use EXD.2 to explain why the rules differ. If a table helps, use EXD.3 to show the intervals and label the two quantities. Correct the rule itself wherever it equates effort with elapsed time.
3. **Identify any remaining difficulty.** If a recipient still counts the interruption, use EXD.4 to find out what their answer means. If they need practice, ask them to explain how each interval enters the calculation. Use EXD.5 to give feedback on that explanation and offer a changed case when useful. Keep any initial answer and the help received. A knowledgeable reader may have corrected the draft from prior knowledge. A later correct answer may depend on the help.
4. **Choose the conclusion the evidence supports.** The accounting rule justifies correcting the draft. Faster reading or better learning with the table requires evidence about those outcomes. If accurate prose already serves the task, retain it. Repeated comparison of corresponding intervals might justify another form. When comparing forms, keep the claims and the available help comparable.

If the task changes to concurrent work by several people, establish what total is wanted and how each person’s effort counts. The one-person example does not determine the answer. Use HCD.18 or HCD.19 to assess an instructional material and the relevant HCD method for claims about later human performance, transfer or retention. A correction to the explanation may already finish the present task.

## Using the repertoire

Enter where the required inputs are available. A clear question and a sufficient account may call for an adjustment to expression or no change. Use subject evidence for a missing premise. Use dialogue when the recipient’s contribution can inform the answer. In a one-way explanation, state the consequential conditions and give the intended reader access to the fuller account when their use requires it.

The [Architectural Reference](#explanation-design-principles-framework-architectural-reference) develops the distinctions used above. The [use profiles](#use-profiles) adapt them to instruction, technical and advisory work, and human–AI interaction.

# Explanation Design Principles Framework Architectural Reference

## EXD.Reference:1 - The practice and the problem it solves

Use Explanation Design to explain a connection a recipient needs: how a calculation follows, why an outcome occurred, how something works, why a recommendation follows from its grounds or how an arrangement addresses a problem. Prepare an account or work with the recipient’s contribution in an exchange. The result can be a usable explanation, a finding about what a previous explanation established, or a specific connection that the available subject evidence leaves open.

A well-supported account may be hard for a particular recipient to reconstruct. A fluent account may make an unsupported inference easy to follow. Examine the grounds for the connection and what the recipient can recover under the conditions of use.

Explanation Design draws on the subject methods that justify an account and on evidence about how recipients can use it. Identify which question is open. It may concern a missing premise, an expression, access, preparation, attention, help or possible later learning.

A recipient may use an already understood fact or a complete account directly. Use the relevant subject methods for a scientific finding, the applicable authority for policy choice, a participant’s response for agreement and suitable learning evidence for a claim about human development. An exchange may supply evidence for a particular one of these claims.

## EXD.Reference:2 - The distinctions that change the work

The **subject** is what the explanation concerns. The **question** identifies the connection sought and the **purpose** explains why it matters. The **account** supplies claims, relations and conditions relevant to that connection. Its **expression** might be prose, a formula, a table, a diagram, a demonstration or a combination. The **recipient** interprets the expression under particular conditions of preparation, access, help and effort, and may contribute to the explanation.

When explaining a Method, distinguish the reusable way of working, an actual or stipulated performance and the material used. An explainer who wants to show how to construct an example can choose two groups with different sizes and different means, so that equal-group and equal-individual weighting give different answers. The arithmetic is the material. Selecting the contrasting instance illustrates a design operation. A correct sum and an account from which the recipient can learn that operation have different criteria.
These distinctions support concrete diagnoses:

| What changes | Example | Consequence for the explanation |
| --- | --- | --- |
| Question or purpose | Equal influence per group replaces equal weight per individual observation. | Use the corresponding calculation and label. Keep the result for the original question. |
| Subject account | The relation between a group mean, its count and its sum is missing. | Supply that relation and its mathematical basis. |
| Expression | The same claims about counts, means and sums are placed in a table. | Assess the form under the intended reading conditions. A claim about improved recovery needs suitable evidence for the forms compared. |
| Assistance | A hint directs attention to the unit counted by the denominator. | When attributing the answer to the recipient, identify what help they received and what they supplied. |
| Required outcome | The task changes from following today’s calculation to doing a new one next week. | Use evidence from the required later condition, with the permitted assistance. Identify any consequential performance that remains unobserved. |

[FPF C.2.8](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c28---extractablestructuralinformation--structure-this-reader-can-recover) relates a particular expression and the structure it contains to what an observer can recover under specified conditions. Identify the required relations, what counts as correct reconstruction and the relevant preparation, access, help, allowed operations and effort. An assessment can identify which relations the recipient could recover under those conditions. An observed response can establish which they did recover and what they omitted. A numerical comparison requires a justified scale and comparable conditions.

An expert and a novice may recover different connections from the same text with the same effort. Repetition may support access or retention without adding a new relation to the account. Familiar relations count when the task asks what is recoverable. For human recipients, include attention and memory when they affect the conditions or outcome at issue.

Formal computational epiplexity has a specified model and computational bound. Applying such a result to human understanding requires a justified correspondence. For a practical task under C.2.8, a qualitative account of the relations recoverable under the specified conditions can suffice. Describe an actual recovery when the response establishes it. Subject warrant, effort, retention, transfer, usefulness and agreement each require evidence for the particular claim.

## EXD.Reference:3 - Obtain and Carry the Subject Explanation

Recover the account that supports the connection the recipient needs. It may be a mathematical definition and derivation, a causal finding, a Method account or a recommendation's rationale. Select its relevant claims while preserving answer-changing conditions, alternatives and limits. The minimum useful account can be very short.

For a nonempty finite list, its mean is the sum divided by the count. Group A contains 2 and 4, with sum 6 and mean 3. Group B contains six 8s, with sum 48 and mean 8. Equal weight per individual gives `(6 + 48)/8 = 6.75`. Equal weight per group gives `(3 + 8)/2 = 5.5`. The intended weighting determines which result answers the question.

If a consequential connection lacks grounds, identify the missing premise, derivation or other subject contribution. A causal explanation requires suitable evidence about the cause. A recommendation needs the premises and conditions supporting it, including any alternatives material to its rationale. A mathematical step may follow from a definition or a derivation already available. Use a qualified existing result when it supplies the connection. Otherwise state the conditional answer or the limit and seek further subject work when the task warrants it.

When checking a proposed explanation, follow its conclusion back to the premises and operations and then forward from them to the answer. At the first consequential gap, identify whether an input is absent, an operation unexplained, an inference unsupported or the connection to the question missing. Select any needed subject work accordingly. A change of expression alone cannot establish a missing premise.

For an account of a Method, use A.3.2.DE:4.1 to recover who or what acts on which input, what the operation yields and why it is justified. Use C.39:4.2–4.5 to develop a needed operation or connection, working back from the receiving result and forward through the proposed steps. For a language of Methods, E.8.ML:4.1–4.4 explains how independently useful results fit together and why the Methods have their stated boundaries. Carry the applicable contribution and its conditions into the explanation.

Use the method appropriate to a gap in the subject account. RMP.2:4.4 helps construct an investigation that could distinguish proposed answers. PSDA.14:4.2–4.4 helps justify a recommendation from its premises, alternatives and comparison, and PSDA.19 addresses conditions of the advising engagement. When a person needs to learn the relation, HCD.6, HCD.9 and HCD.10 guide representative tasks, feedback and assistance. Use A.6.3.NAR when a narrative expression helps connect supplied source relations.

For a research question, a puzzling observation may lead to competing explanations, criticism of those explanations against the available evidence before an experiment, and an initial report of what can already be established. An adequate source may already answer the question. If it remains open, weigh the evidence an attainable study could provide against the burden of obtaining it. Use RMP to qualify the question, select a strategy or a justified stopping point and revise the claims affected by the results.

Use the warranted subject account as the basis for the explanation. The six methods below address questions about the recipient, example, expression, dialogue, learning and comparison. Enter where the remaining task requires a contribution.

## EXD.Reference:4 - A worked exchange and its consequential returns

An analyst asks why the report rejected 5.5, the equal-weighted average of two branch means. The branches contain the eight observations above. The report initially requires the mean across individuals. That requirement determines the weighting rule. Use EXD.1 if the intended question still needs clarification.

The analyst can add and divide but asks why branch counts matter. Use EXD.2 to show how each branch count multiplied by its mean gives its sum. Add those sums and divide by the total count. The answer is `54/8 = 6.75`. If a table helps the analyst locate the values, use EXD.3 to place count, mean and sum together. A usable prose calculation can also explain the relation.

The analyst now says, “I want each branch to have equal influence regardless of its size.” Use EXD.4 to recognize a changed question and EXD.1 to establish the revised target. Equal branch weights give 5.5. Individual weights still give 6.75. The explanation can close with both answers and their weighting rules. If the question is which policy governs the report, use the relevant existing policy or refer the choice to its holder.

If the target remains equal weight per individual, dividing the sum of the two branch means by two reveals a different problem. Explain why the numerator must include each branch’s total and the denominator all individuals. For an instructional task, use EXD.5 to examine the learner’s own explanation and give relevant feedback or a changed case as needed. Without dialogue, the written account can state both rules and the condition for using each. A settled weighting rule can be applied directly.

Use EXD.6 to compare a proposed repair with the present explanation. Adding the missing relation among each group’s count, mean and sum changes the account. Rearranging those claims changes the form. Supplying a hint changes assistance. If the analyst can already use the distinction, the current explanation may suffice. The constructed case demonstrates the arithmetic and the design choices. Claims about human attention, learning or a population effect need evidence of those outcomes.

## EXD.Reference:5 - Why these Methods form a useful language

Use EXD.1 to establish what needs explaining, including when preparing an account for a recipient who is unavailable to respond. Use EXD.4 to interpret an actual contribution and determine whether the exchange needs a clarification, correction or close. These are different tasks and have distinct direct entries.

Use EXD.2 to show how an instance illustrates a claim and where that correspondence ends. Use EXD.3 to choose one adequate expression or coordinate complementary forms. With EXD.5, examine the recipient’s own explanation against the task criterion and guide correction or retry when appropriate. Use EXD.6 to compare possible changes with the value and burden for the intended use.

An example may disclose ambiguity in the question, a diagram may reveal a missing premise, and a learner’s answer may change the exchange. Follow the consequence that matters. A comparison can identify a small change of expression or give grounds for keeping the current explanation.

Narrativization and Narrative Studies supplies ways to connect source reasoning, evidence about cognition and the craft of expression. Use the contributions that fit the explanation. A derivation can show how a result follows. A narrative can make a connection memorable. Its subject warrant and its effect on memory require evidence for each claim.

## EXD.Reference:6 - Assurance, limits and practical consequences

An explicit question, a needed connection and clear conditions of use can be enough to recognize a promising explanation. To justify a particular result, apply the criterion for that claim. Check the derivation for a mathematical inference, the recipient’s reconstruction for a claim about understanding, or the applicable premises for a recommendation. A claim about later independent performance requires evidence of that performer’s work after the relevant interval and with the support the claim permits.

A correct number, an approving response or a fluent paraphrase may leave the inference the recipient used uncertain. Look for the part of the answer that shows how they related the facts. A recipient may understand a recommendation and decline it. Preserve what they actually said or did and the help they received. Keep an observed response distinct from a stipulated example or an expected benefit.

Weigh the detail required against the recipient’s effort, guidance against the independent contribution sought, and the value of another question against its interruption. When a change is needed, prefer the smallest change that addresses the difficulty, weighing its gain and burden against the available explanation. Keep a sufficient explanation.

The examples emphasize explicit relations and short exchanges. Tacit, affective, embodied or culturally situated understanding may call for other forms and criteria. Account for unfamiliar terminology and access requirements before drawing a conclusion about the recipient’s capability. The human–AI profile explains what a system’s output can establish under the stated conditions.

According to the task, an explanation designer can return a warranted connection, an illustrative example, a usable form, an interpretation of a reply, guidance for a learner or a comparison of possible repairs. If the answer depends on an unestablished subject premise, a choice of policy or stronger evidence of learning, identify the subject work, applicable policy or authorized decision, or learning evidence that could answer the remaining question. Preserve the conclusion already supported.

## EXD.Reference:7 - Framework and subject suppliers

Use an adequate result from the relevant framework or subject practice directly. If an input is missing, the table identifies where to find the operation or evidence that could supply it. The six EXD methods handle the explanatory work.

| Supplying contribution | What it supplies here | Reconsider the affected use when |
| --- | --- | --- |
| C.2.8 | A relation between expressed structure and what a particular recipient can recover under stated conditions, used in this Reference, EXD.3 and EXD.6. | The recipient, recovery criterion, assistance or comparison conditions change. |
| C.37 and C.37.CF | Selection and comparison of representations for the same receiving action in EXD.3 and EXD.6. | A form changes the supplied content, available operations or effort. |
| A.2.9 | The communicative act, its participants and intended use, distinct from the resulting account and expression. | A claim relies on a changed act or an inference about a participant. |
| A.6.3.NAR | Selection and connection of source relations when narrative rendering serves the explanation. | The source relation, connective claim or narrative purpose changes. |
| A.3.2.DE:4.1, C.39:4.2–4.5 and E.8.ML:4.1–4.4 | Recovery of a Method's actions and reasons, construction of a missing operation or join, and explanation of the relations within a pattern language. | The proposed action, missing connection or reason for keeping Methods together changes. |
| F.0.2.MA, A.3.1.CC and F.0.2.RC | In the technical profile, use F.0.2.MA to identify which source supplies each contribution, A.3.1.CC to compare a maintained claim with its basis and correct it when needed, and F.0.2.RC to check whether the promised contribution can be recovered. | The source is unavailable or does not support the particular claim to be used. |
| C.11.CRC, C.11 and C.11.DUA | Compare an explanatory change with the existing account and weigh the attainable gain from another step against its burden. | The available explanation, proposed change, intended use or burden changes materially. |
| HCD.6:4.2–4.5, HCD.9:4.4–4.6, HCD.10:4.6–4.7 and HCD.19:4.1–4.5 | For human learning, construct representative tasks, offer feedback and another attempt when needed, choose assistance and evaluate the promised route through a learning material. | The required performance, preparation, help or claimed learning result changes. |
| PSDA.14:4.2–4.4 and PSDA.19 | Recommendation grounds and alternatives, together with the conditions of the advising engagement. | A relied-on premise, preference, alternative, resource or authority condition changes. |
| RMP.1, RMP.2:4.4 and RMP.8 | Qualify a research question, develop a way to distinguish proposed answers when needed and establish what evidence warrants retaining or revising a research claim. | The subject question, rival explanation, observations or intended use changes. |
| NSTD Framework Architectural Reference, NSTD.6 and NSTD.8 | Connections among source reasoning, cognition and production craft, and the choice of a narrative form when it serves the explanation. | The needed contribution or narrative use changes. |

Reconsider the particular conclusion when its premise or evidence changes, when source access affects the proposed use or when a stronger result is requested. Keep independently supported and conditional conclusions within their established conditions.

For the external research sources and their roles, see the [Sources and Edition Notes](#explanation-design-principles-framework-sources-and-edition-notes).

## EXD.Reference:End


# Patterns

## EXD.1 - Establish and Revise What a Recipient Needs Explained

> **Status:** Stable


### EXD.1:1 - Problem frame

Use this method to establish what a recipient needs explained. The required connection, comparison or purpose may be unclear, or a later reply may change it. A teacher, technical specialist, adviser or service can use an existing request or exchange to establish the question.

Begin with the request and the use the explanation must serve. If the request or other evidence already distinguishes the plausible questions, use it. If a consequential ambiguity remains, ask a focused question when feasible or state the conditional alternatives. Return the question, the intended use and any subject input or operation still needed.

A request such as “Show how the total of these eight values gives their mean” can lead straight to the calculation. Seek clarification only when the answer could affect what needs explaining or how the recipient can use it.

### EXD.1:2 - Problem

“Why is this wrong?” can hide several questions. The recipient may have made a calculation error, used a different aggregation rule, questioned a premise or asked whether the result serves a decision. Answering the first interpretation that comes to mind can produce a valid account whose decisive relation is irrelevant to the recipient.

A course title, professional role or fluent acknowledgement may leave it unclear whether a recipient can use a particular relation. Examine the available evidence of preparation when that distinction matters to the explanation. A simple request for an already known result can be answered directly.

### EXD.1:3 - Forces

| Force | Practical tension |
| --- | --- |
| A quick answer and a consequential ambiguity | A short request may already be clear; a small clarification can also prevent a long explanation of the wrong question. |
| The subject and the recipient's purpose | The subject constrains which answers are warranted. The recipient's purpose selects which of those answers is useful. |
| Available knowledge and added burden | An existing attempt may reveal the relation a recipient used. Asking for a new demonstration takes effort and may be unnecessary for a simple request. |
| Continuity and revision | Earlier explanation can remain correct while a changed purpose makes another question current. |

### EXD.1:4 - Solution

#### EXD.1:4.1 - Recover the requested connection and its use

Start from the question as expressed in the available request, material or exchange. Identify what the answer should let the recipient infer, distinguish, predict, calculate or do. “What is the average across these people?” calls for a statistic. “I need a fair comparison of branches” identifies a purpose. Use any applicable weighting rule or identify what remains to be decided.

If different interpretations would change the answer, use relevant existing instructions or evidence of the recipient’s purpose. If the distinction remains open, ask a brief question or give conditional answers. For an average, determine whether each individual or each group should count equally. For advice, distinguish a request for the recommendation’s existing grounds from a question about evidence of expected development.

Use a clear reply or an adequately supported interpretation. If the weighting target remains open, state the consequences. Equal group weights and equal individual weights call for different calculations. Identify the outstanding policy choice only when the task requires choosing between them.

#### EXD.1:4.2 - Locate usable preparation at the needed grain

Use a question, attempted calculation, annotation, objection or other contribution already available. If a relevant prerequisite remains uncertain and the distinction matters, ask for a small inference where that is feasible. For example, “What total does a group of six with mean eight contribute?” examines the link from count and mean to sum. A useful conditional explanation may still be possible without a reply.

Interpret a response under the conditions in which it occurred. If you showed how to multiply count by mean before the reply, the recipient had that step available. Establish what they supplied before claiming independent use. In advising, explaining a disputed premise may already answer the request.

If dialogue is unavailable, work from the intended audience, the task and any relevant prior replies. State assumptions that matter and give conditional conclusions when the evidence leaves more than one interpretation open. A reader can use an explicit branch directly. When the short account omits a connection needed for that use, make the fuller account accessible.

#### EXD.1:4.3 - Form the question that the subject can answer

State the connection to explain, its consequential conditions and the answer sought. For example, “For these eight values, why does equal weight per individual require weighting the group means by their counts?” Use [Obtain and Carry the Subject Explanation](#exdreference3---obtain-and-carry-the-subject-explanation) for its subject basis, including a suitable existing derivation.

If the subject basis is incomplete, identify what the requested explanation depends on. A causal claim needs evidence of the proposed connection, a recommendation its decisive premises, and a mathematical step its definition or derivation. Use an existing qualified result where it answers the question. Otherwise give a conditional answer or state the limit. Further inquiry can supply a missing result when feasible and worth the effort.

#### EXD.1:4.4 - Revise when a contribution changes the target

Compare a new contribution with the current question. Does it change the intended use or a relevant condition, challenge a premise, reveal an error under the same question or confirm that the existing account suffices? State the consequence for the explanation or for the account of the exchange.

For a changed target, state the revised question and retain the earlier answer within its conditions. For an error under the same target, explain the affected inference. For a disputed premise, establish what the evidence supports or state the limit. In dialogue, use [EXD.4](#exd4---co-construct-and-repair-an-explanation-in-dialogue) to interpret the recipient’s contribution and decide whether a further response is needed.

Finish when the question and its conditions are clear enough for the requested use, or identify the precise ambiguity or missing contribution that the available evidence cannot settle and where that contribution could come from. Record it in a separate form only if the work needs one.

### EXD.1:5 - Archetypal Grounding

Suppose a learner asks why averaging two group means gave the wrong result. Group A contains 2 and 4, and group B six values of 8. The task explicitly calls for the mean across all eight individuals. The learner can add and divide but has calculated `(3 + 8)/2 = 5.5`.

The question is why group sizes matter when every individual receives equal weight. Multiplying each count by its mean recovers its group sum: `2 × 3 = 6` and `6 × 8 = 48`. Both sums belong in the numerator, and both counts in the denominator. The pooled mean is `(6 + 48)/(2 + 6) = 6.75`. Explain this connection when it is what the recipient lacks.

The recipient then says, “For my report, I want each branch to count equally, regardless of how many people it has.” This explicitly selects a different aggregation rule, so the explainer can answer the revised question directly.

Under the revised rule, `(3 + 8)/2 = 5.5` is the mean of the two equally weighted branch means. The answer 6.75 still applies to the individuals. These labels and conditions can finish the explanation. If the report requires a choice of policy, use the applicable rule or refer the remaining choice to its holder.

The case stipulates the exchange. The calculation gives the answer criteria for the two questions. A claim about what a learner actually learned requires evidence of that learning.

An adviser has explained why an assignment fits Mira’s demonstrated strengths and available protected time. If Mira asks why it would teach a missing capability, explain the expected learning on its own grounds or state what remains unknown. Evidence of present strengths may already justify the original answer. If Mira understands the advice and prefers a course’s social setting, her reply establishes a preference relevant to the advice.

### EXD.1:6 - Bias-Annotation

Expert familiarity may make one interpretation look inevitable. Check the requested use and a materially different question where one is plausible. A prepared question bank can prompt alternatives. When interacting with recipients, leave room for their own question and reason.

The instructional case makes a correct answer easy to compute. In technical or advisory work, disagreement about the basis can remain unresolved even after the question is clear.

### EXD.1:7 - Conformance Checklist

Recognize a question-setting task when an ambiguity, changed purpose or relevant prerequisite matters. Use a sufficiently stated question directly.

To assess the question and the grounds for interpreting it, check the applicable points below.

- the question and the purpose can be distinguished;
- The relation to explain and conditions that could change the answer are clear enough to select the subject account.
- A statement about preparation identifies its task-relevant evidence or is identified as an assumption.
- When a new contribution is available, interpret it in context. Revise the question, premise, help or interpretation where warranted and retain what the contribution leaves adequate.
- The resulting question can be used, or the account identifies the remaining ambiguity, assumption or missing subject result and, where known, how to resolve it.

These checks concern the question and its use. Retention and transfer need their corresponding evidence.

### EXD.1:8 - Common Anti-Patterns and How to Avoid Them

| Failure visible in use | Repair |
| --- | --- |
| Repeating why 5.5 is wrong after the recipient selects equal branch weight | Restate the changed aggregation question and answer it under its own rule. |
| Taking “I understand” or a qualification as evidence of the needed inference | Use an already available response or one relevant inference when that distinction can change assistance. |
| Treating an elicited list as a complete account of a recipient’s need | Consider what the explanation must support. Use available evidence of the recipient’s purpose and invite other contributions if clarification is needed. |
| Reopening a clear request with an elaborate interview | Use the sufficient question and return to clarification only when a consequential uncertainty appears. |

### EXD.1:9 - Consequences

The question identifies the connection an explanation should address. A changed purpose may call for another account, while the earlier account remains valid within its original conditions. A finding about the change can be the complete result.

Clarifying the question takes attention and can reveal a source gap or a choice outside the explainer’s authority. State that limit and retain independently supported or conditional answers.

### EXD.1:10 - Architectural Rationale

Use EXD.1 to establish the question before preparing a text or to interpret a changed request during an exchange. EXD.4 interprets an actual contribution and can guide the size and content of the next reply, feedback or repair. It can also establish why an earlier exchange ended.

The purpose selects a relevant question. Arithmetic establishes the result under a specified weighting rule. Evidence about what the recipient supplied and what help they received establishes the scope of an independent-use claim. These distinctions determine which part of a proposed explanation, if any, needs to change.

### EXD.1:11 - SoTA-Echoing

[Liao et al., 2021](https://arxiv.org/pdf/2104.03483) connect elicited questions about concrete tasks with their purposes and possible explanatory responses. Apply this relation to the inference the recipient needs. A question bank can suggest alternatives. A single focused question may distinguish them.

[Schmude et al., 2025](https://doi.org/10.1016/j.ijhcs.2024.103380) studied free questions, a question bank and clarification in two algorithmic-decision scenarios with 24 participants. Their exploratory results support allowing recipients to express what matters to them and go beyond prepared categories. Those two scenarios and the 24 participants did not establish that the bank was complete or that it improved comprehension in general.

[Galbraith and Khalifa, 2026, §§2 and 5](https://link.springer.com/article/10.1007/s11098-025-02477-8) propose an interrogative account of understanding and leave some epistemic conditions open. Use the distinction among questions here. Establish the grounds for the subject connection in the applicable domain.

In the worked case, “Which unit receives equal weight?” distinguishes the two rules more directly than “Why is 5.5 wrong?” Both questions are brief. This comparison concerns what they identify. Measuring conversation time would require timed exchanges. Reconsider the question-setting approach if actual use reveals a consequential distinction it cannot express.

### EXD.1:12 - Relations

Use [EXD.4](#exd4---co-construct-and-repair-an-explanation-in-dialogue) for a recipient’s actual contribution to an exchange. [The supplied-account entry](#exdreference3---obtain-and-carry-the-subject-explanation) helps establish the subject relations and conditions the answer depends on.

[FPF A.2.9](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a29--uspeechact--communicative-work-and-its-intended-use) helps identify the communicative act and intended use where that distinction matters. [FPF C.2.8](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c28---extractablestructuralinformation--structure-this-reader-can-recover) helps establish what a particular observer can recover from an expressed account under specified conditions. Identify the purpose from the task or the recipient’s grounds for seeking the explanation.

### EXD.1:End

## EXD.2 - Build and Bound an Explanatory Example

> **Status:** Stable


### EXD.2:1 - Problem frame

Use this method when a particular instance could help a recipient see how a principle, definition or claim applies. A calculation, comparison, analogy or counterexample can expose a connection that the general statement leaves hard to use. The task may be to assess an existing example or to construct one.

Name the relation the instance must show. When a competing rule matters, choose conditions under which its consequences differ from those of the intended rule. Return the worked correspondence and its conditions, or identify what the available example leaves undetermined.

Use an adequate direct explanation when another example would add no needed relation. To present an instance as evidence, establish what the instance and its grounds support. An example can also show why a claim remains open or illustrate what follows under a stated assumption.

### EXD.2:2 - Problem

An attractive example can make a statement memorable while hiding why it applies. A recipient may copy the numbers or surface features, infer a rule from one convenient success, or carry an analogy beyond its justified correspondence.

Show how the instance relates to the claim and, where a plausible alternative would change the use, which feature distinguishes them. A correct final number can be shared by two rules. Inspect the operation that produced it when that distinction matters.

### EXD.2:3 - Forces

| Force | Practical tension |
| --- | --- |
| Simplicity and discrimination | Easy values reduce calculation burden but may make different rules produce the same number. |
| Familiarity and correspondence | A familiar setting can support the mapping or draw attention to irrelevant similarities. |
| Guidance and independent contribution | A worked relation may supply the whole answer. A learner’s own attempt can show what help is needed or what they can already do under the available conditions. |
| A useful boundary and excess detail | One changed condition can expose the limit, while an exhaustive catalogue can obscure the first connection. |

### EXD.2:4 - Solution

#### EXD.2:4.1 - Select the relation and a discriminating instance

Use [EXD.1](#exd1---establish-and-revise-what-a-recipient-needs-explained) if the current question needs clarification. For a definition, derivation, causal account or recommendation premise, see the [supplied-account entry](#exdreference3---obtain-and-carry-the-subject-explanation). Use the available subject basis directly when sufficient.

Identify the correspondence to show. In a pooled mean, multiplying each group mean by its count gives the group sum. Add group sums and group counts separately. For two groups, choose unequal counts and unequal means if the example must distinguish equal weighting per individual from equal weighting per group.

Use an observed or documented case when its evidence and complexity suit the explanation. A constructed case can make the assumptions and answer criterion explicit. State which kind of example supplies the result.

Choose the example for its role in the whole explanation. Derive the relevant variation from the subject, the grounds available and the recipient’s task. A case may reveal a distinction that belongs in the general account. Retain a sufficient direct explanation when a story adds no needed connection. If the account is missing, look for its subject basis or state the limit rather than expanding the illustration.

#### EXD.2:4.2 - Work the correspondence, not only the answer

Show the quantities, operations, relations and conditions needed for the result. Identify which feature of the instance corresponds to which part of the claim and why each consequential inference follows. When explaining how to design an example, show the explainer’s choice and the reason for it. Choosing unequal counts and unequal means distinguishes the two weighting rules. Multiplying count by mean is the mathematical operation used within that example.

For a calculation, name the units and what each numerator or denominator counts. For a causal example, separate the observations and the inferred mechanism. For an analogy, identify the relation that carries over and a consequential condition or difference that limits it. Two things can look alike while the relation needed for this inference differs.

When the task turns on what a recipient can supply, use any adequate initial answer with its assistance conditions. For a new diagnostic attempt, ask for a small mapping before supplying the step to be assessed, for example how to recover the total represented by a group mean. Then offer guidance where needed. When the purpose is to explain the relation to a beginner, showing the worked relation first may be appropriate.

#### EXD.2:4.3 - Vary the condition that matters

If a changed case is needed, vary a condition that distinguishes the relevant rules or reveals a boundary. Identify what should stay the same, what should change and why. Avoid incidental complexity that would obscure this relation.

Compare the rule as well as the number. With equal group counts, the mean of the two group means agrees with the pooled mean. With equal group means, the two results coincide even when counts differ. The intended unit of weighting still determines which rule answers the question.

Use [EXD.5](#exd5---guide-a-recipients-own-explanation) when the learner’s own account, guidance or correction is the teaching task. Use [EXD.4](#exd4---co-construct-and-repair-an-explanation-in-dialogue) to establish what a reply shows and whether the question, a premise or the next explanatory contribution needs to change.

When the promised explanation covers several kinds of ground or use, choose examples that reveal those differences and what remains common. A mathematical derivation, a conditional causal account and advice under competing preferences each require their own grounds. Include ordinary cases as well as informative contrasts. For human learning across a family of regularities, HCD.6.1:4.2.2 guides the selection of qualified encounters, contextual variation and focused returns. The learner can recognize members of the family without articulating one verbal rule for them all.

A worked instance can reveal a missing condition or suggest a wider explanation. Establish the basis for generalization. It may follow from a definition or argument, have observational support or remain a proposal. Bring that result and its conditions into the explanation. Keep the particular instance’s evidential scope clear.

#### EXD.2:4.4 - Bound the example and stop at its useful result

State the relation the example preserves and where a claimed correspondence ends. In one aggregation a branch is the equally weighted unit. In another, the individuals within each branch receive equal weight. The same data can therefore answer two different questions.

Use enough examples to make the required relation and its material variation understandable. One case or a pair may suffice for a local distinction. A broad account should include the different conditions on which its conclusion depends. Remove details that add no needed relation.

Continue a worked case when its earlier result or conditions help explain the next relation. Identify what the case contributes at each use. Change or end the case if it hides a consequential alternative, condition or kind of application. An explanation can remain connected through its question and reasoning while its examples change. Changing a number in the same story can test a calculation without testing the wider range of a claimed Method.

Assess the example against the recipient’s task. Does it supply the relation, its reason and the conditions that could change its use? For a claim about what the recipient actually recovered, examine their contribution. Recalling a story or giving the right number can establish a narrower result. Correct missing subject content when repair is part of the task, and distinguish the worked example from evidence that someone learned from it.

### EXD.2:5 - Archetypal Grounding

A recipient can average a list but combines group means without considering counts. The question is the mean across all individuals.

| Group | Count | Mean | Reconstructed sum |
| --- | ---: | ---: | ---: |
| A: values 2 and 4 | 2 | 3 | 2 × 3 = 6 |
| B: six values of 8 | 6 | 8 | 6 × 8 = 48 |
| Combined individuals | 8 | 6.75 | 54 |

For each group, count multiplied by mean gives its sum. The sums add to 54 and the counts to eight, so the mean across individuals is 6.75. Assigning equal weights to the two branches instead gives `(3 + 8)/2 = 5.5`.

Now reduce B to two values of 8. Each branch contains two observations. The combined sum is 22, the count is four and the mean is 5.5. Here equal group influence gives equal individual influence, so the shortcut agrees. A teaching task may ask the learner to explain that correspondence.

Now keep the unequal counts and give both groups mean 3. Both summaries equal 3 because the weighted terms share the same mean. Equal results for this data do not establish that the weighting rules are identical or that unequal counts always give different answers.

Together, the cases show which rule answers the stated question and why the shortcut sometimes agrees numerically. They are constructed mathematical instances. Evidence about how people learned would be needed for a claim that the examples improved learning.

In a constructed example, a manual prices a batch of twelve parts at 30 currency units. A guide promises a cost-per-part calculation that its reader can recover without the manual. It repeats the price and omits the batch size. The price agrees with the source, but the guide alone lacks the denominator. Including it gives `30/12 = 2.50` per part. A second guide shows `36/12 = 3` and attributes that price to the same manual. This calculation is recoverable, but its price contradicts the source. If both defects occur, assess both promised recovery and agreement with the source.

#### EXD.2:5.1 - Keep the explanatory Method visible across different subject grounds

In the averaging example, the explainer chooses conditions that distinguish two rules, works the correspondence and varies an important condition. The mathematical definition supplies the answer criterion. To explain that design operation beyond arithmetic, vary the subject and the kind of evidence that warrants its answer.

Suppose two pumps share a power supply. A recipient asks why the second pump cannot provide pumping when that supply fails. A sketch can show both connections and the consequence of the stipulated loss. As a contrast, suppose the second pump has a supply that remains available under the same failure. The explainer’s choice is to make the power dependency visible and follow the change through it. Whether an actual installation has an independent usable supply is an engineering question.

Suppose a software revision is followed by fewer recorded failures while traffic and logging also change. One explanation is that the revision prevented failures. Fewer opportunities for failure or less complete recording could also account for the lower count. The given evidence establishes the fall in recorded failures and leaves its cause open. Use an adequate existing comparison or further subject inquiry if a causal answer is needed and the work is justified. The contrast illustrates which connection the explanation would have to establish.

In the technical and advisory profile, the recommendation assumes the protected time the coordination assignment requires. Withdrawing that time defeats this premise unless equivalent time is available. A recipient who understands the rationale and prefers a course’s social setting has supplied a different preference. Its effect on the recommendation or choice depends on the decision criteria and other grounds. Explain the change that actually follows.

The examples illustrate the same design operation across different grounds. In each, the explainer selects a consequential correspondence, works its implications and states the scope of the result. The numerical answer, causal limit and recommendation therefore play different roles. Their stipulated outcomes do not measure learning or effectiveness.

### EXD.2:6 - Bias-Annotation

Expert familiarity can hide an intermediate relation a recipient needs. Check the mapping at the level of the actual task. A familiar story can also suggest a cause or norm the subject account does not support. Explain the correspondence that has grounds.

### EXD.2:7 - Conformance Checklist

Recognition asks whether a particular instance or comparison can make the needed connection usable.

To assess an example, inspect its subject basis, correspondence, worked result and consequential conditions. If the explanation promises a range of uses, check that its examples cover that range and show the common relation. In an illustration of an explanatory Method, distinguish the explainer’s choice from the subject operation shown. When interpreting a response, distinguish which help was available from what the recipient used and supplied. A correct number reached by the wrong rule can identify a gap in the explanation or in the recipient’s inference.

### EXD.2:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| Using only equal-sized groups to teach why counts matter | Add an unequal-count, unequal-mean case that distinguishes the competing rules. |
| Treating one correct number as evidence of the correct relation | Look for the mapping in the answer or its working. If the available work leaves the rule uncertain, report that limit. Use a changed case when the distinction matters and a further comparison can supply it. |
| Asking for an independent explanation when the task omits a required input | Identify the missing input and what the existing answer can establish. For a task that requires the missing component, supply it or a worked correspondence when feasible. If the recipient then uses it, interpret the response with that help. |
| Extending an analogy through surface resemblance | State the supported relation and the consequential non-correspondence. |

### EXD.2:9 - Consequences

A worked example can show how the claim applies and, when relevant, where a plausible alternative diverges. Consider the effort of preparing and using additional examples. A different recipient or a broader subject may need another form or condition of support.

### EXD.2:10 - Architectural Rationale

An instance and its bounded correspondence can be a complete design result. Use representation work to express that correspondence when needed. In a learning task, the recipient can try using it. If difficulty is observed, check what the evidence establishes about the subject account, its expression, the support and the recipient's contribution. A cause can remain open.

### EXD.2:11 - SoTA-Echoing

The [2023 relational-mapping study](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1241873/full) examined principle–example and example–example mapping in probability topics, including free mapping followed by guided mapping of components. The procedure suggests how to expose a correspondence or guide a learner where help is needed. The comparison supports using component guidance in its tested conditions. A choice for different learners or tasks needs grounds for that use; this study does not establish a format that is generally superior.

When a person needs to learn the reasoning, use representative tasks from Human Capability Development and vary the conditions that affect the inference. [Fiorella, 2023](https://link.springer.com/article/10.1007/s10648-023-09769-7) distinguishes the contributions and guidance needs of generated explanations, visualizations and enactments.

With comparable calculation effort, unequal counts and unequal means distinguish the two weighting rules. With equal counts the two rules give the same number. Use the examples that make the needed distinction visible, or use its derivation where that suffices. Revise the construction if a needed application exposes a different plausible rule, a missing component or an unsupported analogy.

### EXD.2:12 - Relations

Use [EXD.1](#exd1---establish-and-revise-what-a-recipient-needs-explained) to clarify the target question where needed, and [EXD.3](#exd3---coordinate-the-expression-of-an-explanation) to express the worked correspondence. Use [EXD.5](#exd5---guide-a-recipients-own-explanation) to interpret a learner’s own explanation, including any guidance used, or to guide a further attempt when the learning task needs one. Use [EXD.6](#exd6---compare-explanations-for-the-recipients-use-and-decide-whether-a-repair-is-worthwhile) to assess a possible change or an already adequate example.

See the [instructional profile](#exdprofiles1---instructional-explanation) when the example is used for a learning task, feedback or assistance. The [supplied-account entry](#exdreference3---obtain-and-carry-the-subject-explanation) addresses the grounds for the subject connection.

### EXD.2:End

## EXD.3 - Coordinate the Expression of an Explanation

> **Status:** Stable


### EXD.3:1 - Problem frame

Use this pattern to express a supported connection in a form the intended recipient can follow, to coordinate several representations, or to examine how an existing expression presents the connection. The available medium may be words, notation, a diagram, a demonstration or a combination.

Select the relation the recipient needs and examine what each representation contributes. When preparing an explanation, make the correspondences clear at the point of use. When assessing an existing explanation, identify which correspondences it makes available. One form may already be sufficient. For a proposed or existing arrangement, identify the conditions under which its relations are accessible and any consequential loss.

If an expression exposes a missing premise or derivation, establish that subject contribution where the claim depends on it. State what the existing grounds support while the premise remains open.

### EXD.3:2 - Problem

Working across representations can take time. A formula and table may use different labels, a diagram may omit a condition, or the reader may have to reconstruct an unstated correspondence. Shortening the account can remove the condition that makes its conclusion true.

Judge an expression by whether the recipient can recover the selected relation and its subject meaning under the intended conditions. Brevity, visual layout and interaction can contribute when they serve that use.

### EXD.3:3 - Forces

| Force | Practical tension |
| --- | --- |
| Complementary views and translation burden | Another representation can expose a relation while requiring extra cross-reference work. |
| Economy and completeness | Removing words can reduce reading burden or erase a decisive condition. |
| Guidance and usable preparation | Signals and worked transitions may help one recipient and interrupt another's sufficient reading. |
| Pacing and coherence | A manageable segment needs enough connection to support its inference. |

### EXD.3:4 - Solution

#### EXD.3:4.1 - Select each contribution

Identify the question and the claims on which its answer depends. Use FPF C.37 when deciding how to express them or combine forms. Specify what the recipient needs to locate, compare, connect or do.

Use one representation when it suffices. Add another when its contribution justifies the extra work, for example when a table makes the correspondence between group count, mean and sum easier to follow beside a formula. Identify which claims and conditions each form supplies and what they leave the recipient to recover across forms.

Distinguish changes to content, expression and help. Adding the relation between group count, mean and sum supplies explanatory content. Displaying that same relation in a table changes its expression. A prompt supplied during the calculation changes the help available. Attribute a result to the change the comparison can isolate.

#### EXD.3:4.2 - Make the correspondence available where it is used

Use consistent names, units and referents. Put a label beside the quantity or feature it names, or give an unambiguous cross-reference when the medium prevents proximity. Make a line, arrow or spatial arrangement's meaning explicit when it could denote different relations.

For human instruction, choose a signal, layout, division into steps or preparation of a concept that addresses the actual difficulty. Direct attention to the needed relation, keep each inference intelligible within its step and allow a return to earlier steps where the medium permits it.

When forms are used simultaneously, make their contributions usable together. Words can explain a relation shown in a diagram. Reading a duplicate passage while listening and watching an animation can compete for attention. Retain text when the recipient needs it for access or later reference.

#### EXD.3:4.3 - Preserve a usable reading path

Make the question, relation, answer and decisive conditions reachable in the chosen form. A short answer may suffice. Where the recipient will need a fuller derivation, indicate when it applies and how to reach it.

Use labels and correspondences available through the recipient’s channel. When an important distinction is conveyed by color, provide another cue for a reader who cannot use that color. If a static diagram obscures timing, use a sequence or an accompanying explanation that preserves the temporal relation. When a reader cannot use one channel, make any needed contribution available in a channel they can use.

#### EXD.3:4.4 - Inspect the specific gain and loss

Check how the specified inference or comparison can be made under the intended conditions. An existing expression, qualified assessment or observation may answer the question. Use [EXD.6](#exd6---compare-explanations-for-the-recipients-use-and-decide-whether-a-repair-is-worthwhile) to choose a further comparison when its possible results could change the choice or resolve a question about use.

Identify changes in content, expression and help. A warranted design comparison can justify a choice under the stated conditions. Identify any uncertainty that makes the choice provisional. A claim of observed advantage needs evidence of the relevant comparison. Identify a missing condition or check the subject source when the representation suggests a different claim. Restore the condition when preparing or repairing the explanation. Stop adding forms when the arrangement suffices.

### EXD.3:5 - Archetypal Grounding

The account explains the mean across all eight individuals in two groups. Its prose form states:

“Group A has two values with mean three, so their sum is six. Group B has six values with mean eight, so their sum is forty-eight. Across the two groups the sum is fifty-four and the count is eight. Dividing the combined sum, fifty-four, by the combined count, eight, gives 6.75. Averaging the two group means gives each group equal influence and yields 5.5.”

A table candidate arranges those same claims:

| Group | Count | Mean | Sum = count × mean |
| --- | ---: | ---: | ---: |
| A | 2 | 3 | 6 |
| B | 6 | 8 | 48 |
| Combined individuals | 2 + 6 = 8 | 54 / 8 = 6.75 | 6 + 48 = 54 |

Beside the table, state the corresponding condition and result in prose. “Averaging the two group means gives each group equal influence and yields 5.5.” The labels then connect counts, means and sums, and both forms distinguish equal influence per group from equal weight per individual.

The table presents the selected claims in a different form. Removing its sentence about equal group influence would change what it explains. Supplying a derivation omitted from the formula changes the explanatory content. Adding the corresponding verbal account also changes the presentation.

When a recipient needs help with the mean-to-sum relation, point to one group’s count and mean and work the step. To interpret a response, identify what the recipient did before any hint and what they did after it, where known. A correct calculation after the hint establishes performance with that help.

In a technical explanation, a box around three checks may suggest they are parts of one method. If the box means “available checks,” say so and identify which question each check answers. A list may convey that information with less effort.

### EXD.3:6 - Bias-Annotation

Check the recipient’s access and the operations the task requires. A visual or terse form familiar to its author may be difficult for that recipient. Findings from human multimedia instruction apply within their studied conditions. Claims about an AI system’s use of the same material need evidence for that system.

### EXD.3:7 - Conformance Checklist

Use the method when the ability to recover a relation from its expression or the coordination of representations matters to the question.

For an assessment, identify what each representation contributes, how the labels and correspondences support the needed inference, and whether decisive conditions are present. State any change in content, expression or help. Credit an observed gain only to the difference the comparison supports. For a claim about what a recipient actually recovered, give the supporting observation and the conditions of that response.

### EXD.3:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| Adding arrows whose meaning is ambiguous | State the relation shown and identify what each relevant label and arrow refers to. |
| Calling added explanatory grounds a layout improvement | Identify the new claims before comparing the forms. |
| Removing the weighting condition to shorten the mean explanation | Restore the condition at the point where the two answers diverge. |
| Crediting the original form with an inference supplied by later assistance | Identify the available evidence of the initial response, the assistance and the subsequent response. |
| Adding another medium because more media are assumed to help | Keep a representation when it makes a useful contribution under the recipient’s actual conditions. |

### EXD.3:9 - Consequences

The design can make the needed connections easier to locate. To claim lower effort in use, examine the relevant comparison. When coordinated forms are maintained, update each affected expression of a changed value or condition.

### EXD.3:10 - Architectural Rationale

For an explanation, coordinate the representations around the particular connection the recipient needs. An example can supply an instance and show its limits. Layout, signals and pacing can make those claims accessible. If preparing a form reveals a missing subject premise, establish it on its own grounds.

### EXD.3:11 - SoTA-Echoing

[Mayer, 2024](https://link.springer.com/article/10.1007/s10648-023-09842-1) describes human multimedia instruction, including placing corresponding words and graphics together, signaling, segmentation and preparation of needed concepts. Choose the operation that addresses the difficulty under the relevant learner, task and presentation conditions.

[Cromley and Chen, 2025](https://doi.org/10.1016/j.edurev.2025.100730) synthesize 181 studies from 92 articles in Mayer’s 1990–2022 research corpus and examine factors that moderate the findings. Use its findings where the learner, task and presentation conditions apply. A general ranking of prose, tables, diagrams or their combinations requires evidence for that wider comparison.

FPF C.37 and C.37.CF help select representations and compare content and form. Here the prose and table carry the same selected relations. The table makes a correspondence spatially explicit. Establishing an advantage in use requires the corresponding comparison. Reconsider the choice if the medium, preparation, access or content changes.

### EXD.3:12 - Relations

Use [EXD.2](#exd2---build-and-bound-an-explanatory-example) when a worked example would clarify the relation or its limits. Use [EXD.4](#exd4---co-construct-and-repair-an-explanation-in-dialogue) to interpret a recipient’s contribution in an exchange, and [EXD.6](#exd6---compare-explanations-for-the-recipients-use-and-decide-whether-a-repair-is-worthwhile) when assessing recoverability or comparing a proposed repair with the present explanation.

Use [FPF C.37](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c37---select-and-use-representations-for-one-action) to choose or combine representations and [FPF C.2.8](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c28---extractablestructuralinformation--structure-this-reader-can-recover) to assess which relations an observer can recover under the stated conditions. For claims about human learning or assistance, use the [instructional profile](#exdprofiles1---instructional-explanation).

### EXD.3:End

## EXD.4 - Co-Construct and Repair an Explanation in Dialogue

> **Status:** Stable


### EXD.4:1 - Problem frame

Use this pattern to prepare, conduct or examine an explanatory exchange when a participant’s contribution bears on the question, the account, the help needed or a further inference. A teacher, technical specialist, adviser or assisting agent may take part. Either participant can offer a relevant relation or a correction.

In a live exchange, offer a contribution that addresses the current question at a level the recipient can use and allow a response to change the explanation or complete it. In an existing exchange, identify what the response established under the conditions then available. The result may be a recovered relation, a revised question, a disagreement or an identified gap in the subject account.

A short message can answer a clear lookup. Seek a diagnostic exchange when the question is still open, its possible answers would distinguish explanations or diagnoses that matter, and the exchange is worth obtaining. An earlier exchange can already settle the question.

### EXD.4:2 - Problem

An exchange can contain many turns while leaving the explanation unchanged or the recipient's question unanswered. For example, an acknowledgement can confirm that a message arrived, an objection can show that the recipient understood and disagreed, and a changed question can make the original derivation irrelevant.

Use what the recipient contributed to decide whether a new explanation, a correction or a conclusion is warranted. A completed exchange can establish what was understood with the help given, even when the participants disagree.

### EXD.4:3 - Forces

| Force | Practical tension |
| --- | --- |
| A coherent contribution and timely correction | Enough connected content is needed for an inference, while a long uninterrupted account can hide the point at which the participants diverge. |
| Feedback and its interpretation | A response may concern contact, perception, understanding or attitude. Its content and the circumstances determine which conclusion it supports. |
| Adaptation and subject warrant | Either participant may correct the account, while an appealing contribution still needs its subject basis. |
| Helpful diagnosis and unnecessary burden | A small question may locate the difficulty; repeated checks can obstruct an already sufficient answer. |

### EXD.4:4 - Solution

#### EXD.4:4.1 - Offer a contribution tied to the current question

Use the question and subject grounds already available. If the target remains uncertain, use [EXD.1](#exd1---establish-and-revise-what-a-recipient-needs-explained) to identify the distinction that matters. Use [Obtain and Carry the Subject Explanation](#exdreference3---obtain-and-carry-the-subject-explanation) when the proposed connection needs a derivation, causal account or other subject basis.

For a new contribution, offer the claim with the ground, condition or correspondence needed for the inference. Match its detail to the task and the recipient’s preparation. A short derivation may suffice. A demonstration may need an intermediate step that the recipient can identify. In an existing exchange, identify what the participants supplied and whether its detail allowed the intended inference.

Make the explanation accessible through an available channel. A pause, an editable example or access to the underlying account can help the recipient contribute. If a live exchange is unavailable, a one-way explanation can still supply the warranted account and its conditions. Give access to the fuller grounds when the recipient needs them.

#### EXD.4:4.2 - Interpret the recipient's contribution in context

Attend to what the contribution changes. “I could not hear the number,” “I do not see why you multiplied,” “I want a different average,” and “I understand, but I reject that policy” invite different responses.

Address the point the recipient raised. If a number was inaudible, restore access to it. If a step in the derivation is unclear, inspect the relation and how it was expressed. Examine a challenged premise against its subject grounds. If the intended use has changed, reconsider the question. Distinguish agreement or willingness to act from a response that shows understanding.

When a recipient says their concern was misrepresented, use their correction if it is clear. If a consequential ambiguity remains, restate what you understood and invite correction. Identify what you agree on and what remains disputed or uncertain. Express genuine uncertainty without weakening a warranted claim merely to sound receptive. If the exchange is itself the obstacle, a different time or channel, a pause or closure can serve the explanatory purpose.

If plausible readings would lead to different repairs, seek a distinguishing clue in the exchange or ask a focused question. “Which quantity should receive equal influence here?” can reveal a change of weighting target. “What sum does this group mean represent?” can reveal a missing mean-to-sum relation. If the available answer leaves the diagnosis open, state what remains uncertain.

#### EXD.4:4.3 - Change the part that prevents the next useful move

Choose a further contribution when the exchange reveals a need for one.

| What the exchange has revealed | Construct the next contribution |
| --- | --- |
| A needed term, label or signal was inaccessible | Supply the same contribution through an accessible channel when it is still needed. Check the affected inference if that bears on the conclusion. |
| A relation is missing or the recipient cannot follow it | Identify whether a subject ground is absent, a correspondence is unclear, or the expression is inaccessible. Report what the evidence establishes. Where a further explanation is needed, supply the missing contribution when available, or identify the open premise and retain its conditions. |
| The recipient uses a wrong relation under the same question | Show the specific mismatch, give targeted support and invite the affected inference again when the use warrants it. |
| A condition or the intended question changed | State the revised question and answer it using its own subject basis. Retain the earlier answer at its original scope. |
| A subject claim is disputed or unsupported | Use available subject evidence, or identify what the supplying practice would still need to establish. Limit or withdraw a claim whose grounds prove insufficient. |
| The recipient understands the grounds and disagrees with the choice | Identify the disputed preference, trade-off or decision. If a decision is required, the participant authorized to decide can make it or another participant can seek their decision. |

When help affects interpretation, identify what was available, what was supplied or used, and what the recipient contributed at each response. If the recipient repeats a step the explainer supplied, that shows what happened with the step available. To claim later independent use, examine performance under the corresponding conditions.

Either participant can supply a missing relation or correct a claim. Check the correction against the subject evidence and use it where warranted.

#### EXD.4:4.4 - Close with the result the exchange supports

State what the exchange supports about the question and the conditions of that conclusion. Give access to the relevant source passage where needed. Identify any unresolved choice or missing connection. Use another inference or action when the evidence is insufficient, its outcome could distinguish the live possibilities and obtaining it is feasible and worthwhile.

Close the exchange when the receiving question is answered, including when the recipient understands the grounds and disagrees. For a learning task, select practice or a later independent case when the specific learning question and available evidence warrant it.

If the exchange ends with a gap, report the established part and the missing input. For example, “Both calculations are available. The report still needs a choice of which unit receives equal weight.”

### EXD.4:5 - Archetypal Grounding

In this constructed exchange, group A contains 2 and 4, so its mean is 3. Group B contains six values of 8, so its mean is 8. The initial task asks for the mean across all eight individuals.

| Contribution | What it changes or establishes |
| --- | --- |
| Recipient: “Why is my average of 3 and 8 wrong?” | The live question concerns the difference between averaging two means and averaging all individuals. |
| Explainer: “For the average across all eight people, reconstruct the totals: 2 × 3 = 6 and 6 × 8 = 48. Then 54 / 8 = 6.75. Averaging the two means gives each group half the influence.” | Supplies the mathematical connection and the condition under which the stated answer applies. |
| Recipient: “But for my branch report I want each branch to count equally, regardless of its number of people.” | Introduces a purpose and weighting rule that differ from the initial task. |
| Explainer: “Then the mean of the branch means is (3 + 8) / 2 = 5.5. Label it as giving each branch equal weight. The 6.75 figure is the mean across individuals.” | Answers the revised question and retains the earlier result with its own condition. |
| Recipient: “I will label 5.5 as the equally weighted branch-mean summary.” | The recipient identifies the statistic and the use intended for the report. Choosing the best policy for a management decision would also require its criteria and authority. |

The recipient changed the weighting target. The result is 5.5 for equal influence per branch and 6.75 for equal weight per individual. Further detail on the pooled mean would answer the earlier question.

A different recipient says, “I still need the average across individuals, but I do not see why multiplying the count by the mean gives the total.” Use the definition of the mean to show why six values with mean eight sum to 48. If the learning question calls for a further attempt, ask for the total of four values with mean five. A response of 20 gives the correct total under the conditions of that exchange. The learner's working and the help used show which part of the calculation they supplied. For a claim about subsequent independent use, use evidence from that later condition.

In advisory work, a recipient might say, “I understand why the assignment fits my present strengths. I prefer the course because I value its social setting.” The response identifies a different value that may affect the decision. If the request was to explain the recommendation, that explanation can end here.

#### EXD.4:5.1 - Recover the concern before adding another explanation

An engineer explains that a proposed service reduces response time from eight minutes to five. A colleague replies: “You keep treating my objection as resistance to speed. I need somebody available throughout the night.” The comparison of response times does not answer that staffing concern.

Use the correction the colleague supplied. “You need continuous coverage. The five-minute figure applies only while an operator is present.” If the question is whether overnight coverage exists, use available staffing evidence or identify what is still unknown. If the question is why the response takes five minutes, give the derivation under its conditions.

### EXD.4:6 - Bias-Annotation

Interpret a response by its content and the conditions of the encounter. An acknowledgement may confirm reception while leaving an inference unexamined. An objection may show that the recipient understood and has a reason to prefer an alternative.

Take a correction from either participant seriously enough to examine its subject basis. Use it when that basis supports the change.

### EXD.4:7 - Conformance Checklist

Identify the question and the contribution whose meaning affects the explanation. In a completed exchange, inspect the content of the relevant turns.

To assess a performed exchange, examine the contribution and response on which the conclusion depends.

- Identify which question the offered account addresses and whether it answers the question then being asked.
- Interpret feedback at the level its content supports.
- A consequential ambiguity is resolved from the available evidence, examined by a distinguishing question or reported as unresolved.
- Any further explanatory move addresses the identified difficulty or revised question.
- Distinguish what the recipient supplied from any added help when the conclusion depends on it.
- State what the exchange supports, its conditions and any consequential gap. If the original exchange ended without a closing account, report what the available turns establish.

These criteria support conclusions about the exchange. Retention, transfer and an independent capability require evidence of performance under their respective conditions.

### EXD.4:8 - Common Anti-Patterns and How to Avoid Them

| Failure visible in the exchange | Repair |
| --- | --- |
| Repeating the original derivation after the recipient changes the statistic | Use the new weighting rule if it is clear, or clarify it where needed. Supply the result for that rule. |
| Treating “yes” as proof of an inference the reply does not show | Use an existing response that shows the inference, or ask a focused question when its answer can change the conclusion. |
| Correcting a recipient who understands the account but rejects its policy | Recover the decision or preference disagreement and return it to the appropriate work. |
| Making an unsupported AI explanation more fluent | Check the facts or mechanism against a qualified source. Give the supported account and identify any unresolved premise. |
| Continuing until the recipient agrees | Close the supported explanatory result and distinguish agreement from that result. |

### EXD.4:9 - Consequences

The explanation can change while the difficulty is still local to a contribution. The participants can revise the target, preserve a useful earlier account and stop with a result whose limits they can name.

A participant may understand an explanation and still disagree. Dialogue takes participants’ attention and may require access to the subject basis. It can identify what remains disputed or what would resolve it. Whether dialogue improved understanding requires evidence of the change and its basis.

### EXD.4:10 - Architectural Rationale

The method connects an explanatory contribution, the recipient’s response and what that response warrants. A prepared account or example may be sufficient. When participants identify a new question or a missing premise, they can change the order and content of the exchange.

Identify the question before or during the exchange as needed. Check a proposed change in the account against the subject grounds. A change of audience, help or intended use may call for a different explanation even when those grounds still hold.

### EXD.4:11 - SoTA-Echoing

The *Social Explainable AI* chapters on [Practices, §5.3](https://link.springer.com/chapter/10.1007/978-981-96-5290-7_5), [Incremental Communication, §§12.3.1–12.3.3](https://link.springer.com/chapter/10.1007/978-981-96-5290-7_12) and [Adaptation, §§13.2–13.3](https://link.springer.com/chapter/10.1007/978-981-96-5290-7_13) describe explaining through situated contributions that the participants can adjust together. §§4.1–4.4 apply this account to the question, each response and any needed repair. Claims about learning require evidence for the recipients and conditions at issue.

[Fisher et al., 2022](https://link.springer.com/article/10.1007/s13218-022-00787-1) analyzed eleven natural consultations. They observed phases alternating and both sides contributing to how the exchange was organized. The observed variation rules out treating one fixed phase order as necessary across these exchanges. A preferred schedule for other consultations requires a separate comparison. Determining whether that organization improves understanding would require evidence of its effect.

[Axelsson, Buschmeier and Skantze, 2022, §2](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2022.744574/full) distinguish feedback about contact, perception, understanding and attitude. In §4.2 the context and content of the response help identify what an acknowledgement supports.

[Fichtel et al., 2025, §§5–6](https://aclanthology.org/2025.sigdial-1.1/) found more co-constructive behavior with enhanced prompting in their Llama 3.1 70B study. The study found no statistically significant difference in mean objective understanding. The behavioral change and the understanding measure answer different questions about that interaction.

[Yeomans et al., 2020](https://www.mikeyeomans.info/papers/receptiveness.pdf), Study 4 and §6.2, examined how acknowledgement and engagement in written messages affected perceived receptiveness, persuasiveness and intentions to collaborate. §4.2 uses a participant’s correction to identify the particular concern before adding a rebuttal. State genuine agreement, disagreement and uncertainty. The correctness of the account, the recipient’s understanding and later cooperation have their own grounds. Reconsider the response when the participant’s concern is still misrepresented.

In the worked exchange, repeating the pooled-mean derivation would answer the original question. Using the recipient’s new weighting rule gives the branch-mean answer and retains the pooled result under its original condition. Reconsider the move if another response points to a different difficulty.

### EXD.4:12 - Relations

Use [EXD.1](#exd1---establish-and-revise-what-a-recipient-needs-explained) when the question needs to be established or revised. Use [the supplied-account entry](#exdreference3---obtain-and-carry-the-subject-explanation) when the subject basis requires attention.

[FPF C.2.8](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c28---extractablestructuralinformation--structure-this-reader-can-recover) qualifies what an observer can recover from an account and its expression under stated conditions. Identify any change of help when interpreting a later response. When a person is learning, Human Capability Development can supply suitable assistance, feedback and a further attempt when needed.

### EXD.4:End

## EXD.5 - Guide a Recipient's Own Explanation

> **Status:** Stable


### EXD.5:1 - Problem frame

Use this pattern when a learner needs to explain a relation or when the task is to establish what the learner contributed to an earlier explanation. A learner might connect a worked step to a principle, explain an error, map a diagram or show how an operation follows. Use the verbal, visual or enacted response that bears on the question.

Identify the relation and what would count as showing it. Examine an existing response with the help available, supplied and used. To develop the learner’s explanation, give a focused prompt with appropriate assistance. The result can be the learner’s own account, what they explained with assistance, a supported correction or a limit on what the available response establishes.

Someone who needs a fact or the grounds for advice can use a sufficient answer directly. When the recipient’s own contribution matters, use a sufficient existing response or ask for an explanation appropriate to the task.

### EXD.5:2 - Problem

“Explain it in your own words” may elicit a paraphrase that leaves the relation unclear. An answer can reflect a wrong inference, a copied step or a missing prerequisite. When the learner replies after receiving a correction, identify what the correction supplied and which relation the learner then explained.

Specify what the learner’s response should show. Keep the initial response when one exists. If the task calls for correction, connect the feedback to the affected relation and check a further attempt when it can establish the intended use.

### EXD.5:3 - Forces

| Force | Practical tension |
| --- | --- |
| Productive effort and unavailable knowledge | Constructing a relation can support learning; demanding it without the required basis can produce confusion. |
| Diagnosis and assistance | An unassisted response can show what the learner did under that condition. A worked step may help the learner use the same relation or prepare them to tackle a different one. |
| Focus and expressive freedom | A precise prompt identifies the relation. Several forms of response can meet the same subject criterion. |
| Immediate correction and later use | A response after feedback can settle what happened in that episode. Later independent use requires evidence from the relevant task, delay and assistance conditions. |

### EXD.5:4 - Solution

#### EXD.5:4.1 - Select the target and the product

Identify the question, learning purpose where relevant, and warranted subject relation. Choose or inspect a product that could show it, such as an explanation of one step, a labeled diagram, a worked correspondence or a demonstration that shows what its actions represent.

State a criterion for the relation. For the pooled mean, the learner needs to show what the denominator counts and how to reconstruct each group’s sum. Accept any expression that establishes those two connections.

Use [EXD.2](#exd2---build-and-bound-an-explanatory-example) when the instance and contrast need construction. Keep legitimate tools available when the intended performance allows them.

#### EXD.5:4.2 - Give a focused prompt and preserve the first response

For a teaching task, select help in light of the learner’s preparation and the relation they need to use. For an earlier attempt, establish what help was available and used from the evidence of that attempt. A worked example, partial diagram, cue or open prompt can each serve a purpose. If an unassisted response is needed to distinguish starting points, use an existing qualified response or seek one before giving the decisive step.

In a new attempt, ask for the relation the learner needs to show. When examining an earlier response, identify which relation its prompt asked the learner to show. “What does your denominator count, and what should it count for this question?” locates a possible error more precisely than “Explain the answer.” In a new attempt, let the learner choose a suitable way to express the relation.

If the learner needs a component that the task does not supply, provide it where feasible and identify the help given. An initial worked step may be appropriate. When a person is learning, use Human Capability Development for broader questions about the task, assistance or progression.

#### EXD.5:4.3 - Locate the error and support its correction

Compare the response with the criterion for the question actually asked. A wrong relation, an unavailable prerequisite, an unclear expression and a changed question can produce similar answers. Equal influence per branch calls for the mean of branch means. Use [EXD.1](#exd1---establish-and-revise-what-a-recipient-needs-explained) or [EXD.4](#exd4---co-construct-and-repair-an-explanation-in-dialogue) when a change of question or a response in the exchange needs interpretation.

When correction is the learning task, help the learner identify the wrong relation, explain why it fails in this case, construct the corrected relation and explain how to use it. Give feedback tied to the criterion. For example, “Your denominator counts two groups, but this question asks about eight individuals.” If the learner also needs the mean-to-sum relation, supply the necessary ground.

Retain the original response if available and identify what the correction supplied. State what the learner explained under those conditions and identify any contribution that remains unclear.

#### EXD.5:4.4 - Ask for the affected use again

When the learning purpose calls for a further attempt, choose one that can show whether the learner can use the corrected relation. Vary values or a consequential condition and state the help available. A completed earlier attempt can already supply the needed evidence. For a historical question, report what the available evidence of the response establishes and any limit on attribution.

If a difficulty persists and the learning task continues, reconsider its cause and the help needed. Stop immediate correction when the learner’s response meets the criterion. Use HCD and suitable evidence for a separate question about later retrieval, reduced help or transfer.

### EXD.5:5 - Archetypal Grounding

The fixed task asks for the mean across all individuals. Group A has two values with mean 3; group B has six values with mean 8. The learner's first product is “(3 + 8) / 2 = 5.5, because there are two averages.”

Keep the first response. Ask, “Which things receive equal weight in this calculation?” In this example the learner answers, “The two groups.” Ask which things the question weights equally. If the learner identifies the individuals, show how the denominator of two reflects the grouping while the task concerns eight people.

One adequate explanation is “Each group mean summarizes a different number of people. Multiply each mean by its count to obtain the group sums, 2 × 3 = 6 and 6 × 8 = 48. Divide their combined sum of 54 by the number of people, 2 + 6 = 8. The mean is 6.75.” If the learner needs help recovering the group sums, supply the relation between a mean, count and sum and record that help.

For a further attempt, use three values with mean 4 and nine with mean 8. Ask for the pooled mean and the meaning of its denominator. Here (3 × 4 + 9 × 8) / 12 = 7. A response that uses the total count and reconstructs both sums meets the criterion under the assistance available. Establish independent use after a delay from a performance under those conditions.

For equal influence of the two group means, the answer is (4 + 8) / 2 = 6. Ask the learner to explain the change of target when distinguishing the weighting rules is part of the task.

The prompts and criteria are constructed. Use the evidence of a particular learner’s response and conditions when deciding what assistance or further practice is warranted.

### EXD.5:6 - Bias-Annotation

Judge the response by how it shows the required relation. A brief diagram or demonstration may meet the criterion. Require particular terminology only if using those terms matters to the task. A diagram or different wording can express the same consequential distinction.

### EXD.5:7 - Conformance Checklist

Use a learner’s response when it can show how the learner understands or uses a relation, or when constructing the response can help them develop that understanding.

Check the relation, answer criterion and conditions of the response being assessed. Identify the learner’s own contribution and any help supplied or used. For instruction, judge the fit of the prompt and correction to the difficulty and use a further attempt when needed. Qualify immediate supported performance, independent use and retention by the evidence for each.

### EXD.5:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| A generic request produces a fluent paraphrase | Ask for the decisive correspondence, ground, contrast or error. |
| An answer is marked wrong after the question changes | Apply the criterion for the question actually asked. Clarify it before giving corrective feedback if it is uncertain. |
| A repeated solution supplied by the teacher is credited as independent use | Report the demonstrated response and the help given. For an independent-use claim, seek relevant evidence under the required conditions. |
| A learning exercise is assigned to someone who needs only a qualified answer | Supply that answer when it serves the request. Use the learner’s own explanation when the outcome depends on their contribution. |
| A failed retry receives the same prompt indefinitely | Revisit the missing component, representation or diagnosis. |

### EXD.5:9 - Consequences

A learner’s explanation can give evidence for a limited finding about that attempt and for choosing targeted support. Producing another response costs time. Seek it when the learning or assessment task warrants it. A supported correction can complete the present task even when retention or transfer has yet to be established.

### EXD.5:10 - Architectural Rationale

For instruction, choose a prompt and product for the relation to be explained. A historical assessment can use the prompt and product from the earlier work. For human learning, Human Capability Development can supply task design, feedback, assistance and progression. The learner’s product may already meet the subject criterion. An observed discrepancy can guide subsequent work on that relation.

### EXD.5:11 - SoTA-Echoing

[Fiorella, 2023](https://link.springer.com/article/10.1007/s10648-023-09769-7) distinguishes explaining, visualizing and enacting as sense-making activities with different guidance needs. Select prompts, partial support or feedback for the relation and task. A learning claim requires evidence of what changed in the learner’s performance.

[Zhang and Fiorella, 2024](https://doi.org/10.1016/j.cedpsych.2024.102326) examined guidance for learners to identify a wrong relation, explain the error and explain how to use the corrected relation. Experiment 2 analyzed 73 students who had made errors. The evidence supported correction and near transfer in that study. A far-transfer advantage was not established.

[Tetzlaff et al., 2025](https://doi.org/10.1016/j.learninstruc.2025.102142) examine how prior knowledge and conditions affect the usefulness of assistance. Use the learner’s task and preparation to decide whether to retain, change or fade support. In this example, a prompt about what the denominator counts targets the identified error more closely than a general invitation to explain. Change the support when the learner’s response shows a different difficulty.

### EXD.5:12 - Relations

Use [EXD.2](#exd2---build-and-bound-an-explanatory-example) when an example or its boundary needs development, [EXD.3](#exd3---coordinate-the-expression-of-an-explanation) to coordinate a visual or symbolic product, and [EXD.4](#exd4---co-construct-and-repair-an-explanation-in-dialogue) to establish what a response shows, including a change of question, a need for help or grounds to end the exchange. [EXD.6](#exd6---compare-explanations-for-the-recipients-use-and-decide-whether-a-repair-is-worthwhile) supports assessment or comparison of a possible change.

The [instructional profile](#exdprofiles1---instructional-explanation) connects this method to HCD for task design, feedback, assistance, material evaluation and evidence of later human learning.

### EXD.5:End

## EXD.6 - Compare Explanations for the Recipient's Use and Decide Whether a Repair Is Worthwhile

> **Status:** Stable


### EXD.6:1 - Problem frame

Use this pattern to assess what an explanation could make recoverable under specified conditions, establish what a recipient recovered in an episode, or compare a proposed improvement with an available explanation. Identify the question the assessment should answer. A missing relation, costly reconstruction or unsuitable help can justify a repair.

Identify the inference or action needed, the conditions of use and the explanation available. For a comparison, select the smallest difference that could affect the result. The answer may be a qualified assessment, an observed finding, a justified repair, a provisional choice or the specific subject contribution still missing.

Keep an explanation that suffices for the intended use unless an alternative offers a worthwhile contribution.

### EXD.6:2 - Problem

A longer explanation may add unneeded information and a shorter one may omit a decisive condition. A new diagram may also introduce new grounds. If an answer improves after a hint, determine which evidence bears on the text, the hint and the recipient’s contribution.

Identify the result in question. Correctness, recoverability, what was actually recovered, effort, retention, transfer and usefulness require different grounds. In a comparison, state what changed.

### EXD.6:3 - Forces

| Force | Practical tension |
| --- | --- |
| A possible improvement and its burden | Additional structure or support may help the use while increasing authoring, reading or maintenance cost. |
| Comparable conditions and realistic use | Holding other conditions steady helps attribute a difference. A practical repair may change content, expression and help together. |
| Immediate evidence and later outcomes | A response can show what the recipient inferred at the time. Independent later use requires evidence from that later condition. |
| Value of further checking | An omitted claim, a wrong calculation, a sufficient existing explanation or an adequate previous observation can settle a question. A new observation is worthwhile when its attainable findings matter enough to the remaining use. |

### EXD.6:4 - Solution

#### EXD.6:4.1 - Fix the receiving question and its criterion

Identify what this recipient needs to recover or do and the applicable subject criterion. Examine the explanation in question. If a choice is needed, identify an available explanation that can serve as the comparison. A mathematical result depends on its derivation, and advice on its grounds and conditions.

For a structural assessment under FPF C.2.8, identify the account, expression, observer and selected relations. Specify the relevant criterion, preparation, operations, access, assistance and budget. Distinguish what can be recovered under those conditions from what a particular recipient has shown. A qualitative account may suffice. A numerical value needs a declared scale and the applicable unit or denominator.

An account can express an intelligible relation whose underlying claim lacks support. If the recipient needs a warranted account, assess both the recoverability of the relation and its subject grounds.

#### EXD.6:4.2 - Identify the smallest material change

If a change is needed, address the identified difficulty. Clarify the question, establish a missing ground, build a distinguishing example, coordinate the expression or guide a learner’s response as appropriate. State what changed in the target, content, expression, preparation or help.

When comparing forms, keep the selected claims and receiving conditions comparable. If the practical repair changes several things at once, compare the combined change and limit attribution to what the evidence distinguishes. An inventory can identify shared claims. What the reader could recover and what they actually recovered need further grounds.

FPF C.11.CRC helps compare the contributions of alternative arrangements, and C.11 helps decide whether the marginal change is worthwhile. For descriptions of methods, use the comparison offered by C.37.CF when relevant. For material intended for human learning, HCD.19 assesses what the material supplies. Inspect its content and conditions or use suitable learner work when the claim depends on a response. Use a suitable existing result directly.

#### EXD.6:4.3 - Obtain only the evidence that can change the choice

Inspect the subject grounds, the claims expressed and any contradiction that bears on the question. This can establish a missing relation or justify a repair before a new reader attempt. Use a qualified existing response or assessment within its scope. Seek a new reading or application probe when its possible results could resolve a consequential question and justify the work.

When a comparison depends on what the recipient could do before corrective help, preserve or recover that initial response where possible. Identify which help was available, delivered or used and what the recipient contributed. A recipient who supplies a missing premise or corrects a false instruction can give a sound answer that the expression alone did not provide.

Prior exposure or practice can affect a second response from the same person. Use a comparison suited to the conclusion or report the resulting attribution limit. A local observation can settle a question about one episode or justify a targeted repair for that use. A general or causal effect needs evidence for that stronger claim.

If a needed observation is unavailable, report what can be established from the content and the stated access or assistance conditions. For a decision, retain a sufficient explanation or make a justified provisional choice that can be reversed, stating its intended gain as an expectation.

#### EXD.6:4.4 - Choose the result and its stopping condition

For a repair decision, weigh the demonstrated or reasonably expected gain against its cost in the intended use. Retain a sufficient explanation when the alternative offers no worthwhile improvement. If a change is warranted, address the specific missing relation or difficulty. Qualify a subject claim whose grounds are missing and seek those grounds when the task requires them.

Specify which result the evidence supports. A recipient might recover more relations within the same budget, or the same relations with less effort. A response in one episode, retention across a delay and transfer to another task have different conditions. Understanding the grounds for advice, agreeing with it, expressing willingness to act, and an actual choice or action are separate outcomes.

Give the supported finding at its stated conditions. If choosing an explanation or repair, identify the choice, its grounds and any change that would make reconsideration worthwhile.

### EXD.6:5 - Archetypal Grounding

For this comparison, take the complete prose account of the pooled mean and the table expression in [EXD.3](#exd3---coordinate-the-expression-of-an-explanation). Both carry five selected relations.

- count multiplied by group mean reconstructs group sum;
- group sums combine into total sum;
- group counts combine into the total number of individuals;
- total sum divided by total individual count gives the pooled mean;
- averaging group means equally answers a different weighting question.

Equal individual weighting gives 6.75 and equal group weighting gives 5.5. The table aligns counts, means and sums already present in the prose. Its proposed benefit is easier correspondence under the recipient’s preparation and budget. That benefit can be distinguished from adding a new mathematical premise.

A response may show that the recipient did not use the mean-to-sum relation. If the explainer then supplies the step and the recipient answers correctly, identify both responses and the help actually given. The episode can justify attention to that step. Determining whether the table itself works better than the prose requires a comparison that distinguishes their contributions.

If the recipient already recovers all five relations from the prose and uses the required statistic, the prose suffices for that task. For repeated lookup of counts and sums, the table may be chosen on a stated design ground. Report a reduction in reading time only when evidence supports it.

If the report calls for equal branch influence, use that condition to judge the responses. The answer is 5.5. The same account yields 6.75 for equal individual weighting.

These cases use stipulated conditions. To report what a particular reader recovered, identify the observed response, task and help. A qualified estimate of what the reader could recover depends on their access, preparation and conditions.

In advising, a person may understand the premises for a recommendation and prefer another option. Their response can finish the explanatory question. If a decision is required, identify how the preference bears on the choice. A claim of persuasion requires its own purpose and evidence.

### EXD.6:6 - Bias-Annotation

A new explanation can receive undue credit for the effort invested in it, and a fluent response can receive undue credit because it echoes the author’s words. Judge the relation, its subject criterion and the recipient’s actual conditions. For a repair decision, include the available explanation at its established scope and retain it when it suffices.

For a human learning claim, use evidence from the relevant human task and learning conditions. For an AI system, identify its version, inputs, available operations and assistance. Use the returned result to establish what it recovered on a run. A bounded analysis can instead establish what it could recover under stated conditions.

### EXD.6:7 - Conformance Checklist

Use these criteria for an assessment of recoverability, a finding about actual use, or a decision about retaining or repairing an explanation.

Identify the question, subject criterion and relevant conditions, including preparation, access and help. For a claim about actual use, examine what the recipient did. For a comparison, identify the alternatives, their differences and what the observations or design grounds establish. Relate any repair decision to the gain and burden it entails.

State when an observation is missing. Leave the claim that depends on it open unless other evidence establishes it. A numerical value for extractable structural information or effort requires its own measurement basis.

### EXD.6:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| Crediting added grounds to layout alone | Separate content and expression, or bound the conclusion to the combined repair. |
| Crediting an assisted answer to an unassisted explanation | Identify the observed response, the help supplied and what the recipient contributed. Use an existing first response when it bears on the conclusion. |
| Measuring words, arrows or messages as recovered structure | Select subject relations and a correctness criterion under C.2.8. |
| Treating a revised question as a failed answer to the old one | Reset the target and preserve both conditional results. |
| Seeking further improvement when both explanations suffice and no choice remains | Use the adequate explanation already available. |
| Reporting learning or persuasion from a fluent reconstruction | Identify what the response shows. A stronger claim needs evidence of the relevant learning or persuasive effect. |

### EXD.6:9 - Consequences

An assessment can establish a supported use, identify a missing subject input or leave a precise uncertainty about the recipient’s conditions. When a choice is needed, the participant responsible for the choice can retain the existing explanation or choose a repair whose contribution justifies its cost. Generalization requires grounds for the wider use.

### EXD.6:10 - Architectural Rationale

Assess contributions by connecting content, expression and help to the recipient’s intended use. A sufficient explanation can close the work. For a consequential difficulty, use the evidence to identify what needs attention in the account, access, expression, help or receiving work. If its cause cannot be established, report that limit.

### EXD.6:11 - SoTA-Echoing

Use FPF C.2.8 to characterize recoverability, C.11.CRC to compare contributions relative to the arrangement, and C.11 to decide whether a marginal change is worthwhile. C.37.CF addresses representations of method descriptions. HCD.19 assesses material intended for human learning through inspection or suitable evidence of representative learner work. Use the operation and criterion appropriate to the question.

[Mengelkamp et al., 2025](https://doi.org/10.1002/acp.70036) distinguish comprehension from judgements about one’s own comprehension for informative narrative and expository texts under different reading goals. Their results varied by condition. [Fichtel et al. (2025)](https://aclanthology.org/2025.sigdial-1.1/) found more co-constructive behavior under enhanced prompting without establishing a significant mean advantage in objective understanding.

In the worked case, identifying whether an apparent gain came from a new premise, another expression or a supplied step can change which repair is justified. A fluent, extensive or attractive version can still omit the relation the reader needs. The already sufficient explanation can be retained when a proposed change adds no worthwhile contribution. Reconsider the choice if the task, subject grounds, recipient, help, budget or evidence changes.

### EXD.6:12 - Relations

Use [EXD.1](#exd1---establish-and-revise-what-a-recipient-needs-explained) when the receiving question needs clarification. [EXD.2](#exd2---build-and-bound-an-explanatory-example), [EXD.3](#exd3---coordinate-the-expression-of-an-explanation) and [EXD.5](#exd5---guide-a-recipients-own-explanation) can help develop a suitable example, expression or guided learner contribution. Use [EXD.4](#exd4---co-construct-and-repair-an-explanation-in-dialogue) to interpret an actual response in an exchange.

Use [FPF C.2.8](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c28---extractablestructuralinformation--structure-this-reader-can-recover) for a question about structural recovery, [FPF C.11.CRC](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11crc---configuration-relative-contribution-comparison) for contributions relative to a configuration, and [FPF C.11](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11---decision-theory-decsn-cal) for the marginal choice. The [source and dependency account](#explanation-design-principles-framework-architectural-reference) identifies Core’s method-development contributions and the uses of HCD for instructional tasks, feedback and assistance.

### EXD.6:End

# Use profiles

These profiles apply the distinctions among subject, account, expression, recipient and evidence to instruction, technical or advisory work, and human–AI interaction. Start from the intended use and select the methods that supply a contribution it needs.



## EXD.Profiles:1 - Instructional explanation

Use this profile to help a human learner reconstruct and use a relation, or to assess an earlier explanation by that learner. Start with the task, its criterion and the help permitted. An accurate imitation may leave the underlying relation unexamined. An existing performance can supply the answer, and someone seeking an immediate answer or its grounds can use an adequate explanation directly.

For human instruction, use the HCD contribution the task needs. HCD.6 helps design a practice task, HCD.9 connects feedback to its criterion and a further attempt when needed, and HCD.10 helps decide whether and how to change assistance. HCD.19 can assess the instructional material itself. Use Explanation Design to choose or make the account, example, expression or prompt the task needs, and to interpret the learner’s own contribution. A judgement about a capability gap or durable learning needs evidence under the relevant conditions.

In the pooled-mean task, the learner can add and divide and first writes “(3 + 8)/2 = 5.5, because there are two averages.” The question gives equal weight to each individual. EXD.1 helps recover that target when necessary. EXD.2 can show why multiplying each group’s count by its mean recovers its sum. EXD.3 can place count, mean and sum together while preserving the same mathematical claims.

For a teaching attempt, use EXD.5 to ask what the denominator counts for the stated target and retain the initial explanation. For an earlier attempt, identify the question, response and help from the available evidence. If the learner needs help, point to the eight observations and ask how to reconstruct the total sum and count. The pooled mean is 54/8 = 6.75. Identify what the learner supplied, what help they received and what part of it they used where this matters. If a further attempt is needed, use three observations with mean 4 and nine with mean 8. Their pooled mean is (12 + 72)/12 = 7. The reasoning needs to connect the group sums and counts to the individual mean. The number alone leaves open how it was obtained.

If the question changes to equal influence per group, the two means in the further example give (4 + 8)/2 = 6. Use EXD.4 when the learner’s contribution changes the question. Address the group-weighted result on its own terms. The instructor can use the original individual-weighting task again if the learning objective still requires it.

A learner’s product can identify a needed connection, demonstrate a successful use or leave a particular inference open. State what the person did under the documented help conditions. Performance on a meaningfully changed task may show transfer to that task under its actual help conditions. A qualified later observation of the same contribution can show what the learner retained over the interval. Generalizing about learners or attributing a learning effect needs evidence appropriate to the wider claim.

Guidance can reduce the work of finding a connection while supplying a step the learner might otherwise have to construct. Choose the task and assistance from the purpose and preparation. Seeking an unassisted first response costs effort and may tell little if the learner still needs a component supplied. If initial independent performance is at issue, use an existing observation or seek a response before giving the decisive step. Where the learner needs the component supplied, it can be provided directly.

Fiorella’s work on explaining, visualizing and enacting, the relational-mapping study, Zhang and Fiorella’s error-focused feedback, and Tetzlaff and colleagues’ synthesis inform choices of examples and support in EXD.2 and EXD.5. Mayer’s multimedia principles and Cromley and Chen’s synthesis inform EXD.3 under their learner and presentation conditions. Use EXD.6 or HCD.19 when the task calls for assessing or repairing the explanation or instructional material. Use the content and conditions of access to assess what the lesson supplies. Use evidence of the learner’s work and help to establish what happened in a particular attempt. A supported finding may leave the material as it is or call for a change in the task or support.



## EXD.Profiles:2 - Technical and advisory explanation

Use this profile when a practitioner or advice recipient needs to understand a technical arrangement or a recommendation, assess its conditions or establish which rationale was used earlier. Identify the question and the premises already available. An omitted relation, unfamiliar expression, changed premise or disagreement can call for different responses. If the recipient also needs permission to act, establish who can decide.

Use the qualifications supplied by the applicable technical or advising practice. Core A.3.2.DE and E.8.ML address a method description and the rationale for a connected set of methods. C.37.CF helps compare their representations. Use Decision Design PSDA.14 for the grounds and alternatives of a recommendation, PSDA.15 when earlier advice needs re-examination, and PSDA.19 when its engagement, authority or feasibility conditions matter.

An engineer asks why source allocation, coherence checking and reconstruction have separate entries and proposes combining them. Distinguish the architecture question from the performance of one check. F.0.2.MA asks which source contributions are carried and why. A.3.1.CC tests a maintained method claim against its basis. F.0.2.RC examines whether the promised source contribution can be reconstructed for its stated use. Its result may confirm coverage, identify an omission or leave the basis open. E.8.ML explains how the distinct questions, results and returns can justify separate entries. A diagram can group them for navigation without prescribing a sequence.

For the question whether one maintained claim agrees with the available source, A.3.1.CC can suffice. If a needed source disappears, identify the conclusion that depends on it and retain independently supported findings. EXD.3 helps express these relations. The existing E.8.ML account can suffice. Use EXD.6 to assess a proposed change when the comparison matters. Authorization to publish requires its own basis.

In a stipulated advising case, Mira asks why a bounded coordination assignment is recommended before enrolment in a management course. She recently succeeded at coordination tasks, a sponsor offers four months of protected time, and the available evidence does not establish that a credential is required. These are the grounds offered for comparing the two options.

Mira may understand the rationale and still prefer the course for its social setting or decline the recommendation. Her earlier question can be answered by explaining the grounds on which the advice was given. If she wants advice for the current choice, consider that preference under the applicable criteria. If the sponsor has withdrawn the protected time, reassess feasibility, including any equivalent time available. The recommendation may change, remain supported for other reasons, or become conditional.

Check the rationale against its sources and conditions. For the engineer’s architecture question, explain how the three methods supply distinct results and why their relations justify the entries. For a particular check, identify which method answers that narrower question. In Mira’s case, show which premise depends on protected time. To establish what a recipient understood, examine their response with its help conditions. Agreement, consent, resources and decision authority each have their own grounds.

Use a clear question directly. Further elicitation or justification costs the recipient time when their purpose and the rationale are already known. An unfamiliar request or disagreement can reflect a different intended use or preference. Before inferring a difficulty in the recipient’s understanding, examine what their response establishes. Fisher’s eleven consultations illustrate how both participants can shape the exchange. Axelsson and colleagues distinguish feedback on contact, perception, understanding and attitude. These sources inform dialogue in the examples. Assess any effect on understanding separately. Use the instructional profile when learning is a further purpose.



## EXD.Profiles:3 - Human–AI explanation

Use this profile when a person and an AI system prepare, discuss or revise an explanation, or when an AI system is itself the subject of the explanation. The question might concern its design or how a deployed version produced a particular result. Identify which subject is being explained. An account of a deployed system’s output may need evidence about its version, inputs and operation.

Use the relevant subject grounds and identify the contributions in the exchange. A person can propose a question, correction, constraint or preference, and an AI system may supply a calculation or source. To explain a deployed system’s behavior, use evidence bearing on its actual operation. A fluent self-description or expressed confidence can be reported as an output. Its causal interpretation needs further grounds.

An AI assistant can use the definition of the mean to recover the total sum and count and give 6.75 for equal individual weighting. If the user changes to equal branch influence, report 5.5 for equal branch weighting. Keep 6.75 as the answer to the earlier individual-weighting question. Use EXD.1 or EXD.4 when the intended question needs clarification. The established calculation can answer a direct request.

If the user asks why a deployed predictor returned a particular value, identify the model, input and diagnostic or other subject evidence that bears on that output. When evidence is incomplete, give the warranted explanation, identify the evidence still needed for an unresolved causal claim and state the limit. The earlier arithmetic example establishes the averaging relation for its own inputs.

For human instruction, an AI assistant can prompt for the learner’s reasoning and preserve the response, any help given and a further attempt when the question needs one. The person’s explanation gives evidence of what they did under those conditions. A result the assistant produces itself can help inspect public instructions or construct a candidate answer. Claims about either performer’s capabilities or mechanisms need evidence about that performer.

For an exchange, identify the current question, its subject grounds and what the participants contributed. For an observed result, specify the system or person, version where relevant, access and assistance. Distinguish interaction behavior, performance on the immediate task against its criterion, confidence, later retention and decision quality when interpreting evidence.

Social XAI work examines joint question formation, incremental explanation and adaptation. Liao and colleagues and Schmude and colleagues examine ways to recover a user’s task beyond a prepared question bank. Fichtel and colleagues’ 2025 study found more co-constructive behavior under its prompting conditions. It did not find a significant mean advantage on its objective understanding measure.

Adaptation may help with a changed purpose and may also add turns, reading effort or unsupported claims. Use a correction or existing response to identify what now matters. Give the warranted answer, the repair needed or the open subject question with its conditions. EXD.6 helps assess a worthwhile local change. Use the instructional or technical and advisory profile where a stronger claim depends on its evidence.

## EXD.Profiles:End


# Explanation Design Principles Framework Sources and Edition Notes

## EXD.Sources:1 - Relied-on contributions and their limits

The sources below connect research on explanation, learning and interaction to the stated practitioner use. The worked examples use constructed conditions unless the text identifies an observation from a study.

| Source and access | Contribution adopted or adapted here | Limit on reliance |
| --- | --- | --- |
| [Galbraith and Khalifa, 2026](https://link.springer.com/article/10.1007/s11098-025-02477-8) (especially §§2 and 5) | Their account of how questions shape understanding informs selection and revision of a question in EXD.1 and EXD.4. | The account addresses selected epistemic questions. Assessing whether the explanation is correct, whether a particular recipient grasped it or whether an intervention helped requires grounds for the claim being made. |
| [Fisher, 2022](https://link.springer.com/article/10.1007/s13218-022-00787-1) | In eleven natural consultations, phases alternated and both participants contributed to how the explanation unfolded. EXD.4 uses those observations when interpreting dialogue. | The variation in the observed consultations rules out a necessary fixed order across them. A general or causal benefit for understanding would require separate evidence. |
| [Axelsson, Buschmeier and Skantze, 2022, §2](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2022.744574/full) | Feedback can concern contact, perception, understanding or attitude. | Interpret a signal using its content and context. If several recipient states still fit, report the observed signal and the limit on what can be inferred. |
| [Social Explainable AI, 2026, ch. 5](https://link.springer.com/chapter/10.1007/978-981-96-5290-7_5), [ch. 12](https://link.springer.com/chapter/10.1007/978-981-96-5290-7_12), [ch. 13](https://link.springer.com/chapter/10.1007/978-981-96-5290-7_13) | Explaining practices (§5.3), incremental explanation (§§12.3.1–3) and adaptation (§§13.2–3) inform work on contributions from both participants. | Use these AI-oriented accounts for the roles and subject at issue. A learning benefit needs appropriate evidence of learning. |
| [Liao and colleagues, 2021](https://arxiv.org/pdf/2104.03483) and [Schmude and colleagues, 2025](https://doi.org/10.1016/j.ijhcs.2024.103380) | When the user’s purpose is unclear, a question bank or clarification can help identify the needed explanatory support. | The latter study involved 24 participants in two contexts. A prepared list can miss a question material to a different recipient or task. |
| [Fichtel and colleagues, 2025](https://aclanthology.org/2025.sigdial-1.1/) | The study examines co-constructive interaction and objective understanding as separate outcomes. | Two prompting conditions with Llama 3.1 70B covered three topics and 277 retained participants. No significant mean advantage on the objective understanding measure was found. An estimate for other conditions needs further grounds. |
| [Relational-mapping study, 2023](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1241873/full) | Comparisons between a principle and an example and between two examples, with free and component-guided mapping, inform EXD.2. | Apply the result within its probability-learning conditions. An unassisted first attempt or a preference for one format in another task needs its own reason. |
| [Fiorella, 2023](https://link.springer.com/article/10.1007/s10648-023-09769-7) | Explaining, visualizing and enacting can make different contributions. Modeled, focused and partial guidance inform EXD.2 and EXD.5. | For human learning, choose learner-generated explanation when constructing or revealing the learner’s own reasoning serves the task. |
| [Mayer, 2024](https://link.springer.com/article/10.1007/s10648-023-09842-1) and [Cromley and Chen, 2025](https://doi.org/10.1016/j.edurev.2025.100730) | Proximity, signaling, segmentation and preparation inform EXD.3’s choices for human instruction. | The synthesis covers 181 studies from 92 Mayer articles from 1990–2022. Use its findings under the applicable learner, task and presentation conditions. The best format or the contribution of repeating information can vary with those conditions. |
| [Zhang and Fiorella, 2024](https://doi.org/10.1016/j.cedpsych.2024.102326) | Guidance to explain a specific error and its correction informs EXD.5. | Experiment 2 examined 73 learners who had made errors. The study found benefits for correction and near transfer. A far-transfer advantage was not established. |
| [Tetzlaff and colleagues, 2025](https://doi.org/10.1016/j.learninstruc.2025.102142) and [biochemistry study, 2025](https://link.springer.com/article/10.1007/s10648-025-09993-3) | Task-specific prior knowledge and assistance conditions affect choices of instructional sequence. | The synthesis covers sixty experiments. Decide whether to retain, change or fade help from the particular learner and task. The biochemistry study’s near-transfer results depended on the population. Identify the relevant prior knowledge rather than inferring it from course experience, and seek separate evidence for far transfer. |
| [Mar and colleagues, 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8219577/) and [Mengelkamp and colleagues, 2025](https://doi.org/10.1002/acp.70036) | Narrative and expository contrasts and the distinction between comprehension and metacomprehension inform choices of expression and assessment. | Compare genre, content, reading goal and measurement under relevant conditions. Memorability can be an outcome. Subject warrant and an appropriate choice of form have additional grounds. |

Publisher descriptions and contents of books by Brown and Wragg (2001), LeFever (2012), Khalifa (2017) and McCain (2022) identify historical lines of instructional practice, explanatory craft and philosophical inquiry. The sources and limits in the table identify the grounds used for the specific methods.

Use the [Architectural Reference](#explanation-design-principles-framework-architectural-reference) for an explanation of how these source contributions enter the connected practice.

## EXD.Sources:End


# Name and citation



## EXD.Edition:1 - Citation

Anatoly Levenchuk. *Explanation Design Principles Framework*. Cite the edition date. For one method, add its EXD address and title. To identify the wording you used, give a permanent link to the file at the commit you used or to an accessible archived copy. The public framework is available through the [FPF publication repository](https://github.com/ailev/FPF).



## EXD.Edition:2 - Naming settlement

This name applies to the six-pattern Domain Principle Framework and its three use profiles. [FPF E.4.DPF](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#e4dpf---domain-and-local-principle-frameworks-whether-and-how-to-author-and-publish) defines its kind. [FPF F.18](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#f18---local-first-unification-naming-protocol) and [FPF F.17](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#f17---make-a-settled-naming-decision-recoverable-for-reuse-unified-term-sheet) supply the naming methods.

**NameCard EXD-NAME-01.** The governed value is the Explanation Design DPF specified by this edition's Architectural Reference, six EXD Methods and Use profiles. Its kind is Domain Principle Framework as constrained by E.4.DPF. Its Tech designation is **Explanation Design Principles Framework**; its Plain designation is **Explanation Design**. **EXD** is the local pattern-address prefix.

The local reference scheme identifies the practice of constructing and adapting explanations for a recipient’s use, including explanatory interaction. It distinguishes the subject, question, purpose, supported account, expression, recipient, contributions and conditions of use. The methods that establish the subject grounds and their results come from the corresponding subject practice. “Explanation Design” names this DPF for that practice.

“Explanation Practice” includes performance but leaves the constructive repertoire less visible. “Explanation and Understanding” names both sides of the relation but suggests a wider subject. The opening scope and dialogue method establish how the chosen name covers both preparation and interaction. Existing FPF and supplying-DPF designations retain their own referents. This is the initial local naming settlement.

Reconsider the name if actual use systematically obscures performed interaction, the governed practice changes or a naming collision makes citations ambiguous. A new citation alone leaves the identity unchanged. If a changed source contribution alters the practice, reconsider the name on those grounds.



## EXD.Edition:3 - Public term row

The [FPF F.17](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#f17---make-a-settled-naming-decision-recoverable-for-reuse-unified-term-sheet) public row gives the designation and prefix needed to cite the framework. Its six method titles retain their ordinary action names. The row states identity, sense, basis, use and currentness claims. The row and the naming settlement are distinct epistemes about the same framework.

| Row field | Value |
| --- | --- |
| UTSRowId; UnificationThreadId | EXD-TERM-01; EXD-NAMING-01, stable local designators. |
| GovernedValueRef; GovernedValueKindRef | This edition's Explanation Design DPF as specified in the Architectural Reference, EXD.1–EXD.6 and Use profiles; Domain Principle Framework under E.4.DPF. |
| SubjectPatternLocator | FPF E.4.DPF. |
| ReferenceScheme | By value: the governed practice constructs and adapts explanations for a recipient's use; subject, question, purpose, warranted account, expression, recipient, contribution and use conditions remain distinct; subject-supplying Methods remain external. |
| UnifiedTechName; UnifiedPlainName | Explanation Design Principles Framework; Explanation Design. |
| NameCardRef | EXD-NAME-01 in Naming settlement, this edition. |
| SenseCellRefs | EXD-SENSE-01: the local scheme above, the expression “Explanation Design”, and the local sense “this Domain Principle Framework for constructing and adapting explanations for recipient use, including performed interaction”. |
| LocalSenseBasisRelation | EXD-SENSE-BASIS-01 relates this edition's account in the Architectural Reference, six Methods and Use profiles to EXD-SENSE-01: that account specifies the named practice, repertoire and boundary. This edition is the basis episteme; its section titles locate the supporting content. |
| RowRationale | The designation supports stable public citation. Its stated scope includes preparation and performed interaction. |
| AdmissibleUse | Refer to this framework and its EXD pattern addresses at this edition and stated scope. |
| RowEditionId | EXD-TERM-01@2026-09-09, an edition designator. |
| CurrentnessCondition | Use the designation while the value and local sense still match the citation. Reconsider an affected use if the practice or repertoire changes or a naming collision prevents identification. Availability of the publication and adequacy of its methods have separate grounds. |

## EXD.Edition:End
