# Defense and Transmission Modeling DPF

A pattern language for explaining how practices continue and spread, how they help or impair work, and how protective action changes those outcomes.

- **Version:** 23 September 2026
- **Edition:** 1
- **Status:** Stable
- **Publication:** [Engineering DPF Suite — Defense and Transmission Modeling](https://github.com/ailev/FPF/blob/main/Engineering%20DPF%20Suite/DEFENSE-AND-TRANSMISSION-MODELING-DPF.md)

Original framework text: © 2026 Anatoly Levenchuk, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Third-party material retains its own terms.

# Table of Contents

## Public units

| Unit | What it helps you do |
| --- | --- |
| [Defense and Transmission Modeling DPF Readme](#defense-and-transmission-modeling-dpf-readme) | Choose a direct entry or retain a longer cross-pattern inquiry. |
| [Preface](#preface) | Understand the language, its connected use, assumptions and external contributions. |

## Part I — Dependence, transmission and continuation

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [DTM.1 - Distinguish Dependence, Cooperation and Parasitic Use](#dtm1---distinguish-dependence-cooperation-and-parasitic-use) | Stable | useful dependence; who benefits; whose harm; copied description versus method | FPF A.6.P.RI, C.36, D.3/D.4 |
| 2 | [DTM.2 - Build a Transmission Law from Exposure and Uptake](#dtm2---build-a-transmission-law-from-exposure-and-uptake) | Stable | contact is not adoption; reinforcement; reconstruction; source and recipient | DTM.1; MMP.7/.11 |
| 3 | [DTM.3 - Couple Change Within Carriers to Spread Between Them](#dtm3---couple-change-within-carriers-to-spread-between-them) | Stable | learning changes spread; partner composition; mean hides differences | DTM.2; MMP.18 |
| 4 | [DTM.4 - Find Conditions for Variant Invasion, Persistence and Return](#dtm4---find-conditions-for-variant-invasion-persistence-and-return) | Stable | threshold; persistence; return after intervention; initial conditions | DTM.2/.3; mathematical analysis |

## Part II — Competition, coexistence and diversion

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 5 | [DTM.5 - Separate Selection Within and Among Collectives](#dtm5---separate-selection-within-and-among-collectives) | Stable | within-group gain; aggregate change; counted unit; differential continuation | DTM.1/.2; MMP.16 |
| 6 | [DTM.6 - Model Competition and Facilitation between Variants](#dtm6---model-competition-and-facilitation-between-variants) | Stable | shared capacity; compatibility; facilitation; indirect release | DTM.1/.2; MMP.11/.16 |
| 7 | [DTM.7 - Locate Diversion of a Shared Control or Cooperation Mechanism](#dtm7---locate-diversion-of-a-shared-control-or-cooperation-mechanism) | Stable | proxy versus result; access and support; unintentional diversion | DTM.1/.2; FPF C.30.LCA; MMP.16 |

## Part III — Protective action and its consequences

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| :--- | :--- | :--- | :--- | :--- |
| 8 | [DTM.8 - Compare Protective Actions against Continuing or Spreading Activity by Target and Remaining Effects](#dtm8---compare-protective-actions-against-continuing-or-spreading-activity-by-target-and-remaining-effects) | Stable | contact; established activity; consequence; restoration; feasible protection | DTM.1–3; FPF C.32.MWA |
| 9 | [DTM.9 - Model Damage and Feedback from Protective Responses to Continuing or Spreading Activity](#dtm9---model-damage-and-feedback-from-protective-responses-to-continuing-or-spreading-activity) | Stable | costly response; memory; differential sensitivity; protection backfires | DTM.3/.4/.6/.8; MMP.18; FPF C.30.LCA |

# Defense and Transmission Modeling DPF Readme

## Practical entries

These are selected examples, not a catalogue or a prescribed workflow. Bring the work, question and observed difficulty you actually have. If none fits, use the Table of Contents and the direct patterns.

You can ask an assisting agent: “Explain this and give me comments in the language of my work, without framework jargon.” Use the equations only when their assumptions fit; a short causal account can already settle the next action.

### DEPENDENCE — A useful service is being called a parasite

- **Situation:** Your work depends on an external contribution, and that dependence is being treated as proof of harm.
- **Question:** What changes for the participants while support is available, if it disappears, and under an available substitute?
- **First useful result or blocker:** A comparison that separates current usefulness, interruption exposure and replaceability, or an identified unknown that changes the decision.
- **Start with:** [DTM.1](#dtm1---distinguish-dependence-cooperation-and-parasitic-use).
- **Stop or return:** Stop if that account settles the choice. Study spread only when continued uptake or changing dependence remains material.

### Practical-Use Cards

These examples retain longer inquiries across several methods. The repeated wording helps keep their intermediate results and returns together; each pattern supplies the operation itself.

#### INNOVATION — A useful change meets protection

- **Situation:** A proposed practice appears useful, but existing checks or exchange conditions restrict its use.
- **Question:** Which restriction protects needed work, and which change could preserve that work while allowing the useful contribution?
- **First useful result or blocker:** A conditional explanation linking consequences, uptake, compatibility and protective response; a missing distinction remains a specific investigation.
- **Mantra:** Name whose work changes; recover uptake and its conditions; separate protection from its costs; test the resulting continuation and return to evidence.
- **Start with:** DTM.1 → DTM.2/.3; use DTM.6 for interaction, DTM.8/.9 for protection, then DTM.4 for persistence.
- **Stop or return:** An absent capability is not resistance. Return to the subject learning or engineering method; stop the harmful-variant branch when harm is not established.

#### DIVERSION — A spreading procedure undermines the work

- **Situation:** A frequently reused procedure receives continuing support while its recipients report worse results.
- **Question:** Does support favor a misleading signal, do selection conditions favor the variant, or is another mechanism responsible?
- **First useful result or blocker:** A discriminating causal account and a feasible response comparison, not a label applied to its users.
- **Mantra:** Establish the consequence; trace support and continuation; distinguish diversion from selection; compare response targets; check what persists or changes afterward.
- **Start with:** DTM.1 → DTM.7 or DTM.5; use DTM.6/.3 for consequential interactions and spread, DTM.8/.9 for response, and DTM.4 for return.
- **Stop or return:** Retain competing explanations if the observation does not distinguish them. A protection proposal needs the actual means and authority to perform it.

#### RECOVERY — Restore a capability without restoring everything

- **Situation:** Removing a harmful arrangement also removes a contribution on which useful work depended.
- **Question:** How can the needed function be recovered and sustained through another tool, method or division of work?
- **First useful result or blocker:** A feasible replacement contribution, its acquisition need and the conditions for its continued use.
- **Mantra:** Keep the needed function; obtain a replacement contribution; recover its learning and transmission; test continuation without recreating the harmful dependence.
- **Start with:** DTM.8 with FPF C.36.RP; DTM.2/.3 connect acquisition and transmission, and DTM.4/.6 test continuation under the changed arrangement.
- **Stop or return:** A description of the replacement does not establish capability. Obtain the subject method and test it in the whole work before claiming recovery.

# Preface

## DTM.Preface:1 - The working problem and field

A practice can spread without producing its advertised result. A useful tool can create dependence without harming its users. A protective response can preserve one function while disabling another. These situations become difficult when local performance, further transmission and the consequences for different participants are treated as the same thing.

Defense and Transmission Modeling helps researchers, designers and practitioners construct and compare accounts of those relations. It covers recurring mechanisms of continuation, interaction and protection in engineering and cultural work. It is a repertoire of methods used in different combinations, not one compulsory nine-step process.

The relevant object may be a working procedure, learned operation, tool-use arrangement or another variant with a stated continuation criterion. The participant in which it is realized is sometimes called its carrier. That term does not classify the participant as diseased or passive. A person, AI agent, team or technical system may actively reconstruct what it receives; their learning and operating mechanisms remain different.

The language foregrounds the connection between local effects and continued use elsewhere. It abstracts from most technical details of the subject practice. It does not supply clinical interventions, biological experimental procedures, a complete cultural-engineering program or universal rules for controlling populations.

The practical gain is a better located modeling or intervention question: what continues, through which relation, with what consequences, and what a feasible change would leave unresolved. Modeling effort, observation cost and uncertain causal relations limit that gain. If a subject method already supplies the needed answer, use it directly.

## DTM.Preface:2 - How the language holds the problem together

The first part establishes what is being compared and continued. DTM.1 separates dependence from consequences. DTM.2 constructs the transmission event and any reconstruction of the variant. DTM.3 relates change within a participant to further spread and to conditions changed by that spread. DTM.4 distinguishes establishment, maintained use and return after intervention.

The second part explains why variants continue differently. DTM.5 separates changes within groups from their different contributions to what continues. DTM.6 builds the interaction through an actual intermediary. DTM.7 is narrower: it investigates whether a shared recognition or support relation sustains a result incompatible with its intended work. Neither competition nor disagreement automatically makes that last method applicable.

The third part distinguishes protective choices. DTM.8 locates the target of each action; DTM.9 models the response itself, including formation, memory, cost and indirect effects. A changing variant returns to the earlier continuation and interaction questions rather than forcing an endless escalation of protection.

A useful connection carries a result, not just a PatternID. An uptake account supplies an event and its conditions; a coupling supplies how participant state changes that event; a regime analysis supplies a conditional continuation; a protection comparison supplies feasible changes and their residual consequences. Keep those conditions when one person, specialist or AI hands the result to another.

Three structures can be present together without being identical: simultaneous constituent work, a network of contacts, and units of selection or reproduction. A team may execute one method vertical while its members exchange several procedures across different networks. The method vertical is not a population hierarchy, and a group in a statistical partition is not automatically a reproducing collective.

## DTM.Preface:3 - A connected worked inquiry

Consider a group of engineering teams deciding whether to adopt a new method with a different exchange format. Existing conversion permits exchange with old-method partners, but at a cost. Some participants call the resulting delay resistance to innovation; others describe the new format as a threat.

DTM.1 starts with the work and recipients. Suppose the benefit to a switching team is 2 units over the chosen horizon, adoption costs 0.5, and conversion costs 3 times the share of its relevant partners still using the old method. These are constructed values, with all conversion cost borne by the switching team. The unchanged arrangement is the comparison, not a claim of zero existing benefit.

DTM.2 separates hearing about the method from being capable and authorized to use it. If no eligible team encounters it, an attractive gain does not produce adoption. If teams cannot execute the method, a better announcement does not supply that capability.

DTM.3/.6 connect partner composition to the gain from switching. With f the share of relevant partners already using it, the gain is 2−0.5−3(1−f). It is −0.9 at f=0.2 and 0.9 at f=0.8. The relation is compatibility-mediated facilitation, not proof that participants irrationally reject novelty. DTM.4 identifies the positive-gain threshold f>0.5, while keeping that comparison separate from a dynamic law of adoption.

An available adapter costing 0.4 and reducing the conversion coefficient to 0.2 gives gain 0.94 at f=0.2. Its engineering method must establish the promised exchange and cost. A change in who bears conversion cost requires recomputing the consequences for both sides.

If an admission check rejects the new format to preserve a required exchange result, DTM.8 locates its target. The comparison can now include retaining the restriction, providing the adapter or changing the receiving work. DTM.9 is needed if the checking response has consequential memory, cost or effects on other useful activity. It is not invoked merely because a restriction exists.

The question does not require decomposing a change across source groups, and no diversion of support has been identified. DTM.5/.7 therefore add no required step. The first useful result is the conditional compatibility account and a concrete engineering and uptake question. It is not a forecast that the adapter will be adopted.

## DTM.Preface:4 - Protection and the simultaneous method vertical

A team checks an unfamiliar procedure while continuing to produce work for its customers. At the same moment it is performing several related kinds of work:

| Simultaneous work | Contribution that must be available | Condition imposed by the whole |
| --- | --- | --- |
| Delivering the required customer result | Subject execution, resources and coordination | Protection must preserve an acceptable way to obtain that result. |
| Selecting and controlling procedure use | Observation, interpretation, decision and authority | A restriction must distinguish what matters under the actual conditions. |
| Carrying out the check | A usable comparison, instruments or data, and competent interpretation | The check must fit the time and capacity available during delivery. |
| Obtaining and interpreting the observations | Sensing or retrieving the data and recognizing the consequential difference | The check cannot assume a distinction that no performer can make under the working conditions. |

This is one useful vertical, not four universal levels. Earlier training can make simultaneous performance possible, but the trained capability must still be available during the work. A correct check in isolation does not establish that the whole combination is feasible.

For example, a reviewer may know the difference between a valid and invalid result, yet lack a way to observe it before the delivery deadline. Increasing the number of reviews will not supply that missing operation. Alternatively, the operation may exist but consume the same scarce capacity needed for delivery. Those are different acquisition and operational questions.

FPF B.1.5.EW and C.32.MWA recover the constituent relation and simultaneous support. Human capability development, AI training, technical implementation and operational methods supply their own missing contributions. DTM describes only part of that vertical.

The reference of protection remains explicit throughout: who is protected from whose action, which result is preserved, and who bears the response's cost. Incoming and outgoing harm are useful questions in safety/security discussions, not an exhaustive definition of those terms. An aggregate collective advantage does not automatically settle a constituent's interests.

## DTM.Preface:5 - What counts as a useful result

A first result can be a bounded relation with a discriminating next observation. More detailed modeling is useful when it changes a feasible choice.

For a connected use, ask:

- Does the account distinguish the continuing variant, its realization and a copied description?
- Does the transmission law refer to the receiving event actually counted?
- Does a coupling retain the participant differences and timescales that can alter the result?
- Are an accounting decomposition, a causal claim and a value judgement kept distinct?
- Does the response act on the proposed target, and are the necessary distinction, means and authority available?
- What result returns to the larger work, and which observation or changed condition would reopen it?

The pattern checklists supply their local tests. These questions concern the combination: independently acceptable pieces may use incompatible events, horizons or resource assumptions.

Common failures have different repairs. Popularity mistaken for usefulness returns to DTM.1. Contacts mistaken for adoption return to DTM.2. A mean participant hiding nonlinear effects returns to DTM.3. Any unfavorable outcome labeled capture returns to DTM.7's alternatives. Stronger protection assumed to be better returns to DTM.8/.9.

The numerical examples demonstrate deductions under stipulated assumptions. They do not establish empirical rates, effective organizational policies or comparative learning gains. A real intervention requires evidence for the subject relations, appropriate authority and the relevant practice's assurance.

## DTM.Preface:6 - Rationale, synthesis and alternatives

The language connects several questions that are often answered in isolation: whether a dependence helps, how a variant is acquired and reconstructed, how local activity affects transmission, why contributions differ across groups, and what protective action changes.

It retains distinct methods because their first results and return conditions differ. An exposure law cannot supply the consequences of supported work. A decomposition of selection cannot identify a diverted control relation. Distinguishing intervention targets cannot replace modeling a response's memory. Their composition makes it possible to revise one account without discarding the others.

A supplied population model is a serious cheaper alternative when its entities, event law and parameters already fit the question. Use it. Generic mathematical modeling is sufficient for representation, analysis and testing once the consequential subject relations are supplied. DTM helps when constructing and connecting those relations is itself the repeated difficulty.

Biological and epidemiological sources contribute mechanism distinctions, not classifications of cultures or people. The source comparisons in the relevant pattern bodies identify what is adopted, adapted and limited:

| Contribution to the synthesis | Where it changes the method | Retained limit |
| --- | --- | --- |
| Separate coupling or replication from contribution to useful work | DTM.1; competing positions on cognitive offloading are compared there | State labels and chosen scores do not establish harm. |
| Distinguish contact, uptake, reconstruction and cross-scale interaction | DTM.2/.3/.6 | Human learning, AI training and biological establishment need different subject laws. |
| Separate counted units and causal selection | DTM.5 | Contribution counts are not automatically reproduction of collectives. |
| Recover a shared control or support relation | DTM.7 | An architectural analogy does not prove capture or intent. |
| Separate protection targets and include response effects | DTM.8/.9 | Lower local consequence need not mean lower transmission or lower harm elsewhere. |
| Relate continuation to compatibility and allocation of costs | DTM.3/.4/.6 | Historical equilibrium results do not supply a current adoption mechanism. |

The synthesis does not presume independence is always preferable, novelty is harmful, collective growth overrides individual consequences, or every defense is an obstacle. These are possible biases in the question being modeled. Restoring affected parties and feasible comparisons makes them inspectable.

Reopen a method when a relied-on source changes a consequential claim, a supported mechanism no longer fits the practice, an omitted interaction reverses the choice, or an existing subject method resolves the whole question with less burden. A new publication date alone is not a reason to replace a working account.

## DTM.Preface:7 - External methods and publication use

These contributions remain external to DTM. The links return to the supplying public frameworks; search the stated PatternIDs within them. Use the currently available body that still supplies the described result, and revisit the combination if that relied-on content changes.

| Supplying framework | Content relied on | Receiving use and condition |
| --- | --- | --- |
| [FPF Core](https://github.com/ailev/FPF/blob/main/FPF-Spec.md) — A.6.P.RI, C.36, C.36.RP, D.3/D.4 | Reference restoration, cultural continuation and recovery, conflicts of interests and levels | Establish the participant, consequence and cultural relation before characterizing harm or recovery. |
| FPF Core — C.30.LCA, C.32.MWA, B.1.5.EW | Layered control and simultaneous Method participation | Needed when the explanation or action depends on those relations; a contact network alone does not establish them. |
| [Mathematical Modeling](https://github.com/ailev/FPF/blob/main/Foundational%20Thinking%20DPF%20Suite/MATHEMATICAL-MODELING-PRACTICE-DPF.md) — MMP.7/.11/.16/.18/.19 | Observation model, state and law construction, distinguishing explanations, coupling and reduction, counterfactual comparison | Supplies the modeling operations. A subject-supported mechanism and the conditions of causal comparison must still be available. |
| [Mathematical Thinking](https://github.com/ailev/FPF/blob/main/Foundational%20Thinking%20DPF%20Suite/MATHEMATICAL-PRACTICE-DPF.md) and [Computational Thinking](https://github.com/ailev/FPF/blob/main/Foundational%20Thinking%20DPF%20Suite/COMPUTATIONAL-THINKING-DPF.md) | Construction, analysis and computational execution of the chosen model | Use the methods needed by the actual representation; a qualitative first result need not require a simulation. |
| [Economic Reasoning and Coordination](https://github.com/ailev/FPF/blob/main/Engineering%20DPF%20Suite/ECONOMIC-REASONING-AND-COORDINATION-PRINCIPLES-FRAMEWORK.md) — ECO.8 | Coordination, authority and cost-bearing distinctions | Relevant to the compatibility and institutional cases; utility comparison does not establish permission to change an arrangement. |
| [Operations Management](https://github.com/ailev/FPF/blob/main/Engineering%20DPF%20Suite/OPERATIONS-MANAGEMENT-PRINCIPLES-FRAMEWORK.md) — OPS.10/.19 | Usable capacity under the required service conditions; reconciliation with other operating work | DTM.8's review and saturation examples need these results when limited resources change the protective effect or displace other commitments. |
| [Human Capability Development](https://github.com/ailev/FPF/blob/main/Engineering%20DPF%20Suite/HUMAN-CAPABILITY-DEVELOPMENT-PRINCIPLES-FRAMEWORK.md) — HCD.6/.9 | Representative human practice, an attempted action, feedback and retry | Use when acquisition requires more than exposure. The subject movement or work method supplies the technique; HCD.11/.13 address performance and retention or tool dependence when stronger capability claims are needed. |

The subject practice must additionally supply the actual work method, observation, technical feasibility and limits. A model can identify a missing contribution; it cannot create a skill, sensor, adapter or permission by naming one.

DTM belongs in the Engineering DPF Suite because its first use supports inquiry and intervention in ongoing work. It relies on FPF and the Foundational Thinking methods; it does not change their general definitions. Its Parts group publication content rather than declaring three new disciplines.

This file contains the framework's practical entry, whole-language account and nine pattern bodies. Cite a body by its DTM PatternID, retaining the edition when a changed body could affect the use.

## DTM.Preface:End

# Part I — Dependence, transmission and continuation

## DTM.1 - Distinguish Dependence, Cooperation and Parasitic Use

**Type:** Method
**Status:** Stable

### DTM.1:1 - Problem frame

**Use this when** a spreading practice, component or tool relies on other participants' resources and someone concludes that this dependence makes it harmful—or that its popularity makes it beneficial.

A team using an external reasoning service may deliver better results while losing an alternative way to obtain them. A new exchange standard may help its users while imposing conversion work elsewhere. A teaching technique may be copied widely without producing the ability its learners wanted. In each case, determine what continues or spreads and what changes for those who support and use it.

The first result is a small account of the dependence and its consequences under a stated comparison. It lets the participants distinguish useful support, cooperation, extraction at another's expense and an unresolved relation before choosing a response.

For a routine purchase with known service conditions and no question about continuation or spread, use the applicable procurement or operational method. This method is useful when the relation itself is being misclassified.

### DTM.1:2 - Problem

Dependence, replication advantage and useful work are different relations. A method description can be copied while competent performance disappears. A provider can gain more customers while those customers also gain. A variant can persist because it brings benefits, because alternatives are inaccessible, or because its continuation is rewarded even when the work suffers.

Classifying the whole situation as “parasitism” conceals which of these mechanisms would have to change. Conversely, calling it “cooperation” can conceal a cost transferred to someone outside the comparison.

### DTM.1:3 - Forces

| Force | Tension |
| --- | --- |
| A decision is needed | Consequences may be partly known and differ by participant or horizon. |
| External support extends capability | Losing access or replaceability can also remove a needed capability. |
| Variants must be recognizable | A copied description, learned operation and installed device preserve different things. |
| A collective result matters | It does not automatically override the interests of its members or neighbours. |

### DTM.1:4 - Solution

**Name what continues, recover what supports it, compare the consequences, then characterize the relation.**

#### DTM.1:4.1 - Identify the variant and its continuation

Choose the unit whose continuation is in question. For a working practice, distinguish the method used, a description of it, its competent execution and the participants capable of teaching it. For a device or program, distinguish installed instances from the design and its revisions.

State the criterion by which a later occurrence counts as continuation or a changed variant. A short operational distinction may suffice: “a report prepared with this procedure and checked against independent measurements,” rather than “the same culture.” Where learning changes the method, retain that change for DTM.2.

Then identify the participants and means that enable this continuation: an executor, a provider, an organization allocating time, a communication channel, or an archive. These examples are different relations, not a compulsory list of parts.

#### DTM.1:4.2 - Recover the enabling relation

Ask what contribution would be absent if the supporting participant or resource were unavailable. Describe the resulting loss and whether another available contribution could replace it. Distinguish dependence on one supplier from dependence on the kind of contribution.

For example, the practice may need an external solver, without needing this particular solver. Alternatively, its records may be readable only by the present service. These relations call for different continuations: obtaining a substitute, making the representation portable, changing the practice, or accepting the dependence for the intended work.

Use a model or a safe bounded comparison when withdrawal would disrupt real work. An unperformed counterfactual remains a hypothesis. Loss under withdrawal establishes dependence; it does not yet establish harm during supported use.

#### DTM.1:4.3 - Compare results for the affected participants

Recover whose result matters, for which work and over what horizon. A.6.P.RI helps repair expressions such as “our benefit,” “the system is safe” or “they are dependent.”

Choose a feasible comparison: continuing the present arrangement, using an available alternative, or changing one contribution. For each materially affected participant, retain useful output, required expenditure, exposure to failure and capacity for later work where those differences change the choice. The relevant domain methods define and measure these quantities.

A difference is meaningful only against that comparison. If a provider bears a conversion cost in one arrangement and the customer bears it in another, keep both allocations visible. Do not place the cost in an unnamed total and then attribute the resulting advantage to each participant.

When consequences remain unknown, identify the missing relation that changes the conclusion. It may be sufficient to proceed under two conditional accounts. A new investigation is useful only if its result could improve the receiving decision enough to warrant its cost.

#### DTM.1:4.4 - Relate continuation to consequences

Now compare the variant's continuation with the effects just recovered.

| Observed or modeled relation | Working characterization and consequence |
| --- | --- |
| Continuation depends on another contribution, while effects are unresolved | Dependence is established; usefulness and harm remain open. |
| Participants obtain useful contributions from the arrangement under the stated comparison | Cooperation is supported for those participants and conditions. Inspect any relevant omitted recipient before generalizing. |
| A variant or participant gains continuation through another's resources while impairing that other's stated work | Parasitic use is a candidate explanation of this relation. Identify the causal extraction or diversion; disadvantage alone does not establish it. |
| Effects change with access, scale, time or allocation of costs | Retain a conditional relation; model the condition that changes its character. |

These are not permanent types of people or organizations. Several relations may coexist: cooperation between two participants can impose harm on a third. The description also does not settle what intervention is legitimate; the applicable agreements, rights and decision methods do that work.

The minimal output can be one sentence: “This procedure depends on the shared service, improves current output while the service is available, and leaves the team without a tested substitute.” That is already enough to consider a substitute or a different assurance arrangement without calling either participant a parasite.

#### DTM.1:4.5 - Choose the next modeling question

Use DTM.2 when the uncertainty concerns adoption or further transmission; DTM.3 when participants change through use and thereby change transmission. Use DTM.5 for a conflict between within-group and between-group change, and DTM.7 only when a shared mechanism may be serving a different result.

If the comparison removes the alleged harm, stop the harmful-variant branch. If only the choice among already understood arrangements remains, return to the existing selection and improvement methods. A new dynamic model is not required to preserve an already sufficient conclusion.

### DTM.1:5 - Archetypal Grounding

#### DTM.1:5.1 - A service improves work but concentrates dependence

Consider a hypothetical team whose old process yields 10 acceptable analyses per week. With a service it yields 14 at an additional cost affordable for the work. Under an outage the supported process yields only 4; a tested substitute would yield 9.

The method produces three separate comparisons. Current supported output improved by 4. Current outage exposure is larger than before. Replaceability would reduce that exposure, but would not preserve all normal output. None of these differences alone proves exploitation. The next action depends on the required continuity, supplier conditions and cost of the substitute.

If the supplier benefits from continued use, that fact also does not settle parasitism: both parties may benefit. Evidence that a supplier deliberately obstructs portability would introduce a further causal claim, not retroactively change these numerical comparisons.

#### DTM.1:5.2 - The same spread permits opposite evaluations

Suppose a conditional population model gives fractions 0.30, 0.25 and 0.45 in three modes of tool use. Scores of 1, 0.5 and 0.1 for a separately specified task give a mean of 0.47. Scores of 1, 1.4 and 0.9 for another justified assessment give 1.055.

The arithmetic is a constructed example, not measurements of users. Its purpose is to expose the missing premise: state fractions do not determine task performance. The practitioner must supply the task, capability criterion and evidence for the scores. A model of spread cannot supply them merely by naming one state “dependent.”

#### DTM.1:5.3 - A remembered movement is not the promised capability

A learner can recall a turn sequence and depend on a teacher's cues while still failing to coordinate balance and timing. Separate the transmitted description, the cue-supported execution and independent execution under the intended conditions. The dependence may be useful temporary support. Calling it harmful before comparing learning outcomes would obscure the missing coordination method.

The next inquiry concerns the relevant bodily, rhythmic and learning methods. DTM does not infer a physical cause from the learner's difficulty.

### DTM.1:6 - Bias-Annotation

The word “parasite” can turn a disputed comparison into an apparent natural classification. Keep the claim about a specified relation and its effects. An evaluator's preferred independence is not automatically the participant's objective.

A focus on immediate output can hide future exposure; a focus on unaided performance can hide the value of reliable tools. Compare both only when the receiving work requires them.

### DTM.1:7 - Conformance Checklist

- The account distinguishes the continuing variant, its realization and the participants or means supporting it.
- Withdrawal or substitution bears on dependence; a separate comparison bears on usefulness or harm.
- Each material consequence has a recipient, horizon and feasible comparison.
- A parasitic-use claim names the enabling or diversion mechanism and the impaired work, rather than relying on unfamiliarity or popularity.
- Unknown effects and conditional changes remain visible; the next action does not require a settled moral label.

### DTM.1:8 - Common Anti-Patterns and How to Avoid Them

**Dependence is damage.** Replace the inference with the enabling relation and a comparison of supported, interrupted and alternative work.

**Spread is approval.** Obtain evidence of the work's result separately from counts of adoption.

**The organization benefits, so everyone benefits.** Restore recipients and cost allocation before combining outcomes.

**Classify first, explain later.** Describe the enabling relation and effects first; retain an unresolved characterization when the evidence does not select one.

### DTM.1:9 - Consequences

The participant can choose what to preserve, replace or investigate without treating every dependence as failure. The account can also expose a conflict hidden by an aggregate improvement. It costs more than assigning a label, but may finish with a few sentences instead of a population model.

### DTM.1:10 - Rationale

Continuation and useful work answer different questions. Their separation makes it possible to understand cooperation, exploitation and changing relations with the same method while retaining the differing causal mechanisms. The comparison is supplied by the actual work, not by an assumption that autonomy or collective growth is always preferable.

### DTM.1:11 - SoTA-Echoing

[Solé et al., *Large-Language Models as a Cognitive Virus* (2026 preprint)](https://arxiv.org/abs/2609.03344) distinguish dynamics of coupling states from an illustrative competence measure. This method adopts that separation, without taking their state names as diagnoses or their chosen scores as universal measurements.

[Fields and Levin, *Cognitive Offloading Is a Cognitive Universal* (2026 preprint)](https://www.preprints.org/manuscript/202607.0507) provide a competing starting point: external support is not inherently a defect. The method uses that challenge to the independence default; it does not require the paper's stronger universal physical claims.

[Koonin, *The first major transition* (2026 preprint)](https://arxiv.org/abs/2608.22348) distinguishes replication autonomy from contribution to a collective in its early-life model. This supports keeping the two questions separate; it does not establish the corresponding cultural relations.

The subject-level synthesis here compares enabling dependence, continuation and consequences. C.36 supplies cultural relations, A.6.P.RI the reference repair, and D.3/D.4 the treatment of conflicts across interests and levels. None alone establishes the subject-specific effects, which remain a modeling and evidence question.

### DTM.1:12 - Relations

- **DTM.2** constructs adoption and variant-change laws after the continuing unit is identified.
- **DTM.3** connects participant change and further spread.
- **DTM.5** distinguishes selection within and among collectives; **DTM.7** investigates a particular diversion mechanism.
- **DTM.8/.9** use the identified consequences to model protective action and its feedback.
- **C.36**, **A.6.P.RI**, **D.3/D.4** retain their general cultural, reference and conflict contributions.

### DTM.1:End

## DTM.2 - Build a Transmission Law from Exposure and Uptake

**Type:** Method
**Status:** Stable

### DTM.2:1 - Problem frame

**Use this when** a model predicts the spread of a way of working from contacts, messages or downloads, yet these events do not reliably produce use.

A standard can reach a group that lacks permission to adopt it. A demonstration can reach a learner who cannot yet perform its coordinated movement. A prompt can be copied into an AI workflow and then altered before it is executed. These differences change both the amount transmitted and what continues.

Build a law connecting observable exposure, uptake and the resulting variant. The first result is a defensible expected flow or transition probability, with the unresolved factors retained. It can be qualitative when the next decision needs only the missing condition.

A count of views is already sufficient if the question is only whether a notice was seen. Do not expand it into a model of competence or use unless the receiving question needs that result.

### DTM.2:2 - Problem

A single “transmission rate” can combine contact, exposure, opportunity, willingness, successful performance and later continuation. It may fit one data series while giving the wrong answer when teaching, permissions, compatibility or access changes.

Adoption and faithful copying also differ. Two practices can have equal uptake and very different future composition because recipients reconstruct or combine what they receive.

### DTM.2:3 - Forces

| Force | Tension |
| --- | --- |
| Few parameters are convenient | A parameter that combines different mechanisms may not survive the proposed change. |
| Contacts supply information | Repetition, independent endorsement and conflicting advice can change its effect. |
| A variant needs a traceable identity | Learning and adaptation may be productive transformations rather than copying errors. |
| Events must be observable | Available records often show publication or access, not performance. |

### DTM.2:4 - Solution

**Define the receiving event, reconstruct the path to it, then compose uptake with the resulting variant.**

#### DTM.2:4.1 - Name the event to be predicted

Choose an event that answers the work question: first trial, successful execution under named conditions, continued use over an interval, or ability to teach another participant. Distinguish these when one may occur without the next.

Specify who can undergo the event and the opportunity over which its probability or rate is measured. For a weekly adoption count, identify the groups not already using the practice and what counts as a first use during that week. For a transition between two working methods, identify both starting and receiving states.

Return to DTM.1 if “the variant” sometimes means the description and sometimes the performed method. MMP.7 and MMP.16 help model what records actually reveal and choose observations that distinguish competing event definitions.

#### DTM.2:4.2 - Recover exposure and the conditions of uptake

Trace how a recipient encounters an actionable variant. A contact matters only through what it makes available. Identify any condition whose absence prevents the receiving event: a needed capability, usable tool, compatible interface, time or authority, for example.

For one period, let E be relevant exposure, G the required opportunity or support, and U the receiving event. When U requires E and G, the chain rule gives:

~~~text
P(U) = P(E) × P(G | E) × P(U | E,G).
~~~

The conditional terms retain dependence; multiplying three unrelated marginal probabilities would assume more. If use can begin through independent invention or another channel, add that event path rather than treating all use as transmission from the selected source.

A brief account such as “the group saw the method but cannot run the required tool” may finish this step. Estimate numerical terms only when they change the next use.

#### DTM.2:4.3 - Choose a contact law that matches the mechanism

For independent opportunities with per-contact success probability p and n contacts, the chance of at least one success is 1−(1−p)^n. This construction requires comparable independent trials. It is not justified merely by counting contacts.

When uptake needs reinforcement, use the relevant history: distinct supporting neighbours, repeated successful demonstrations, trust, resource availability or a shared commitment. Give repeated and independent sources the effects supported by the case. Repetition may cease to add information, and another contact can discourage uptake.

In continuous time, define the hazard for a specified recipient who is still eligible for the event. The conditional probability of its first event over a small interval Δt is approximately hΔt; h has units of inverse time. Under a constant hazard, the interval probability is 1−exp(−hΔt), not h itself.

To construct the population flow, count the eligible recipients once. In an illustrative fixed population of N participants, with fraction f already using the variant, homogeneous mixing may support an eligible recipient's hazard h=βf. Then:

~~~text
eligible recipients S = N(1−f)
new-uptake flow J = S h = N(1−f)βf          [events per unit time]
flow of population share j = J/N = βf(1−f) [share per unit time].
~~~

Here β combines the supported encounter and conditional-uptake rates. The factor 1−f belongs to the eligible population, not again inside its per-recipient hazard. This is one two-state construction, not a universal law. Network, institutional or broadcast exposure may require recipient-specific hazards; sum those over the actual eligible set. New participants, departures and return to eligibility require their own transitions.

If competing variants or mechanisms could explain the same uptake, retain those alternatives and use MMP.16 to find a distinguishing observation. A fitted contact coefficient does not establish the missing mechanism.

#### DTM.2:4.4 - Describe what the recipient obtains

After determining uptake, specify whether the recipient preserves, reconstructs or combines variants. Keep the change conditional on the source, receiving conditions and chosen event.

For discrete alternatives, K(i|j) can represent the probability that an uptake from source variant j yields recipient variant i. Each source column sums to one over the included possible outcomes. If a failed or unclassified outcome matters, include it or separately state the conditioning that excludes it.

With accepted source flows a_j, the receiving flow is:

~~~text
b_i = Σ_j K(i|j) a_j.
~~~

This does not require copying fidelity or a fixed biological analogue. A revised procedure may be a useful result. When several sources jointly produce one method, replace the single-source column with a rule conditional on that combination. An unchanged title does not demonstrate an unchanged method.

#### DTM.2:4.5 - Connect observation and further transmission

State which observed records estimate each event or term. A download can identify access, a trial can identify attempted execution, and an independently checked result can support a performance claim. None automatically supplies the next event.

If uptake changes the recipient's ability or incentive to transmit, hand that dependence to DTM.3. If recipients stop using the variant, represent that transition separately from failure to adopt. The output is the event account plus the resulting law and its source of uncertainty; it is not a requirement to estimate every possible parameter.

Stop when the law supports the intended comparison. Return to the event path if a proposed intervention changes a factor that the current rate had combined with others.

### DTM.2:5 - Archetypal Grounding

#### DTM.2:5.1 - Transmission can reconstruct the practice

Suppose 100 eligible groups face a modeled one-period uptake probability of 0.3. Among their accepted source encounters, 60% carry A and 40% carry B. The accepted flows are therefore 18 and 12.

Assume the recipient retains A after an A encounter with probability 0.9, while a B encounter yields A with probability 0.2. The other outcomes yield B. The receiving flows are:

~~~text
A: 0.9 × 18 + 0.2 × 12 = 18.6
B: 0.1 × 18 + 0.8 × 12 = 11.4.
~~~

These are expected counts, not fractions of a particular person. Thirty uptakes do not mean thirty faithful copies. If accepted encounters favour one source differently, use their composition rather than the source population's composition.

An intervention that helps more recipients obtain the required tool changes uptake. An intervention that helps recipients preserve a needed operation changes K. They are different proposed effects and need different observations.

#### DTM.2:5.2 - Reinforcement is a different law

In a constructed three-neighbour case, each neighbour independently provides a relevant endorsement with probability 0.4. If one endorsement is sufficient, the chance of reaching that threshold is 1−0.6³=0.784. If two are required, it is 3×0.4²×0.6+0.4³=0.352.

Both numbers concern the specified endorsement condition, not actual adoption. A recipient may still lack resources or choose not to proceed. Dependence among neighbours invalidates this binomial calculation; three repetitions from one source are not necessarily three independent endorsements.

The useful result is a choice between mechanisms to investigate, rather than adjusting one transmission coefficient until both stories appear to fit.

#### DTM.2:5.3 - A demonstration reaches learners without supplying coordination

A dance workshop distributes a turn demonstration. A view count measures exposure. A learner's attempt, successful execution with a cue, uncued execution and later teaching provide different events.

If the learner needs a coordination method not supplied by the demonstration, raising the number of views need not increase the target performance. HCD and the relevant movement methods supply the acquisition work. The transmission model records its effect on the chosen transition, rather than treating a missing capability as unwillingness or resistance.

#### DTM.2:5.4 - A recipient hazard becomes a population flow

Suppose N=100, f=0.2 and β=0.5 per week. There are 80 eligible recipients, each with current hazard 0.1 per week. The instantaneous new-uptake flow is therefore 8 events per week, or 0.08 of the population per week.

For a short interval of 0.1 week with hazards approximately unchanged, the expected first-uptake count is approximately 0.8. With constant hazard throughout that interval, it is 80[1−exp(−0.01)], approximately 0.796. Counting the remaining fraction again would incorrectly reduce the instantaneous flow to 6.4 events per week. If uptake materially changes f during the interval, evolve the changing state rather than holding its initial hazard fixed.

### DTM.2:6 - Bias-Annotation

A convenient event can displace the intended result: copied prompts and watched demonstrations are easier to count than retained competence. Preserve the receiving event even when its measurement is harder.

Do not treat every reconstruction as decay. Compare what the new variant enables before assigning a copying-error interpretation.

### DTM.2:7 - Conformance Checklist

- The predicted event, eligible population and interval are stated.
- Exposure, opportunity and uptake remain separable where an intervention can change them differently.
- Multiplicative factors have appropriate conditional meanings; contact independence is not silently assumed.
- The resulting variant is linked to accepted source flows, including reconstruction or combination when relevant.
- Observed records are connected to the events they actually establish.
- The output states the conditions under which the law can be reused and what change requires reconstruction.

### DTM.2:8 - Common Anti-Patterns and How to Avoid Them

**One click equals adoption.** Select the receiving event before choosing a convenient record.

**Every repetition is an independent trial.** Recover the source and history of the encounters.

**Uptake means copying.** Add the resulting-variant rule after uptake; do not hide it inside a contact count.

**A fitted rate explains the mechanism.** Retain rival mechanisms when they imply different effects of the proposed change.

### DTM.2:9 - Consequences

The model can distinguish increasing access from enabling performance or changing what is learned. It also shows when an intervention cannot affect the bottleneck it claims to address. More event distinctions require evidence; keep only those that alter the receiving comparison.

### DTM.2:10 - Rationale

A law of transmission connects a source opportunity to a recipient change. Exposing that construction makes it possible to revise the appropriate factor when conditions change. Composing uptake with reconstruction preserves the possibility of cultural development instead of reducing it to faithful replication.

### DTM.2:11 - SoTA-Echoing

[Centola, *The spread of behavior in an online social network experiment* (2010)](https://pubmed.ncbi.nlm.nih.gov/20813952/) is a historical experimental counterexample to universally treating social adoption as independent simple contagion. It motivates the reinforcement branch, not a universal threshold or the illustrative numbers above.

[Zilio et al., *Co-circulation and co-infection: parasite interactions across scales* (2026)](https://doi.org/10.1016/j.tree.2025.12.002) distinguish contacts, transmission and establishment and examine their coupling. The method transfers that separation of events; it does not transfer biological event probabilities into cultural practice.

C.36 supplies creation, transmission, reconstruction and selection as distinct cultural relations. MMP.7/.16 supply the observation-model work. The contribution here is to construct the subject-specific event path and compose uptake with the resulting variant, using those providers.

### DTM.2:12 - Relations

- **DTM.1** identifies the continuing variant and affected participants.
- **DTM.3** connects the adopted practice with changes in participants and further spread.
- **DTM.4** analyzes the resulting dynamic regimes.
- **DTM.6** handles interaction that changes exposure, uptake or persistence.
- **C.36**, **MMP.7/.16** and the applicable learning methods retain their distinct cultural, measurement and capability contributions.

### DTM.2:End

## DTM.3 - Couple Change Within Carriers to Spread Between Them

**Type:** Method
**Status:** Stable

### DTM.3:1 - Problem frame

**Use this when** a practice changes its participants, and those changes affect whether, what or how they pass it on—or when wider adoption changes the conditions under which participants can use it.

A learner becomes able to demonstrate a method only after practice. Growing adoption can overload shared teaching support. An installed standard changes which exchanges need conversion. A model that holds these conditions fixed can therefore predict the wrong continuation even if its separate local descriptions are reasonable.

The first result is a coupled account: which participant state changes which transmission or uptake event, and which population change feeds back to participants. It may be two connected ordinary sentences or a small mathematical model. Use MMP.18 for the general work of reconciling mathematical descriptions once these subject relations have been identified.

If participant change has no material effect on the receiving question over its horizon, retain the simpler transmission model.

### DTM.3:2 - Problem

Two common reductions erase the relation that drives the result. One treats every carrier as an unchanged source of identical transmission. Another computes a detailed participant trajectory but assumes its population consequences are just that trajectory multiplied by the number of participants.

“Carrier” here names the person, group, device or other participant in which the relevant variant is realized or retained for this model. It does not imply disease. A carrier's state, its resources, the method it uses and the contact network remain different objects.

### DTM.3:3 - Forces

| Force | Tension |
| --- | --- |
| A participant model can be detailed | The receiving spread model may need only one output, but it must be the right output. |
| A mean makes computation cheaper | Nonlinear uptake and unequal contact can make the mean misleading. |
| Events unfold at different speeds | Replacing a process with its equilibrium can erase startup, delay or memory. |
| One vertical of methods supports performance | That vertical is not the same structure as transmission between participants. |

### DTM.3:4 - Solution

**Find the relation crossing each modeling boundary, construct its effect on an event, then test what the chosen aggregation loses.**

#### DTM.3:4.1 - Identify the participant state that can change transmission

Start from a receiving event defined by DTM.2. Ask what changes its occurrence or resulting variant: the source's capability, time available to teach, quality of a demonstrated result, retention, equipment compatibility, or the receiver's current preparation, for example.

Keep a state only if it can change the receiving outcome. Recover how that state changes through use, learning, wear, recovery, support or another mechanism of the actual practice. Describe the process before choosing its equation.

A person's ability to coordinate a turn and a robot controller's learned parameters can each affect a demonstration. That does not give them the same learning law. Obtain the internal process from the relevant human-development, movement or engineering methods.

#### DTM.3:4.2 - Convert the state into a transmission contribution

Determine the quantity delivered to the next model. Examples include demonstrations per period that meet a performance criterion, an uptake probability conditional on readiness, the composition of reconstructed variants, or the cost of exchange with an adopter.

Preserve the event selected in DTM.2. If each encounter is eligible for a repeatable success, the expected success count is the sum of its event probabilities. With n comparable encounters and common probability p, that count is np; this expectation does not require independence.

First uptake by a recipient is different: after it occurs, later encounters cannot create that recipient's first uptake again. For n independent comparable opportunities before such uptake, its probability is 1−(1−p)^n. More generally, let p_k be the chance of first uptake at opportunity k conditional on no earlier uptake and the stated history. Compose those conditional chances along that history; if histories vary, also account for their probabilities. Alternatively, update the eligible recipient set as events occur.

Aggregate first-uptake probabilities over distinct eligible recipients, not encounters. For a continuous-time model, sum their hazards to obtain the population flow as in DTM.2. This preserves the quantity passed to DTM.4.

Use DTM.2's conditional factors and resulting-variant rule where needed. Do not multiply a capability score by a contact count without explaining how that score changes the selected event probability or rate.

Then name the observation that could establish or challenge the proposed state-to-event relation. If two mechanisms predict different outcomes for the same state, retain both until the receiving decision warrants discrimination by MMP.16.

#### DTM.3:4.3 - Recover the feedback from wider spread

Ask what changes for a participant when more, fewer or different others use the variant. Common possibilities include access to compatible partners, demand on shared support, availability of teachers, recognition rules and a protective response.

Build only the feedback supported by the case. For example, increasing adoption may create more teachers and also consume their time. The net effect is a question about those quantities, not an automatic positive feedback.

Where the influence is one-way over the chosen horizon, state that reduction and its reason. A diagram with arrows in both directions is not a requirement to invent the second mechanism. Where both directions matter, trace the loop far enough to see which state or event the returning effect changes.

C.32.MWA helps keep the structures separate: the vertical of methods enacted in one performance, resource provision, control, contacts and units of selection need not share the same boundaries.

#### DTM.3:4.4 - Choose an aggregation that preserves the needed effect

Choose among individual states, a few relevant classes, a distribution over state or age since adoption, and a justified common state. Use the least detail that preserves the comparison.

When event contribution is q(x), the relevant population quantity is the appropriately weighted average of q(x), not automatically q of the average x. Weights come from the modeled events: an individual making many demonstrations can contribute more exposure than an individual making none. Population shares alone need not be the weights.

A time-since-adoption description is useful when newcomers and experienced users produce materially different events. An average state is more defensible when the effect is approximately linear over the relevant range or when variation is small enough for the decision. Test that approximation, rather than choosing a fixed number of classes.

Return to MMP.18 if shared quantities, units, conservation, state boundaries or incompatible assumptions prevent composition.

#### DTM.3:4.5 - Decide whether a fast process may be reduced

If local adjustment is much faster than changes in adoption, a local equilibrium may provide the needed output. First identify the relaxation time and the population-change time over the conditions being compared. Examine startup and interventions, not only a final stationary point.

Retain the local dynamic state when learning delay, fatigue, memory, periodic loading or loss of support changes the prediction. A fast measured response does not establish the absence of slower memory.

The result states what is passed across the boundary, the conditions under which it can be summarized, and the change that would require restoring detail. DTM.4 then investigates persistence and return using that coupled model.

### DTM.3:5 - Archetypal Grounding

#### DTM.3:5.1 - Equal average readiness can imply different spread

Consider an illustrative readiness x between 0 and 1. Suppose a relevant demonstration occurs once per period and produces the receiving event with probability q(x)=x². This law is a declared hypothesis for the example, not a general law of learning.

In population A every source has readiness 0.5, giving q=0.25. In population B half have readiness 0.1 and half 0.9. Both have mean readiness 0.5, but population B has mean contribution (0.01+0.81)/2=0.41.

A model using only mean readiness would treat both populations identically. If the comparison is about transmitted successful practice, that reduction loses the effect. Preserve the readiness distribution or sufficient classes. If the actual event law were linear and contact opportunities equal, the same particular loss would disappear.

This case also separates evidence obligations. Measurements of readiness do not establish q(x)=x²; that link requires observations of the chosen receiving event.

#### DTM.3:5.2 - Growth can reduce the support available to each learner

Suppose local readiness follows the conditional model:

~~~text
x' = α(f)(1−x) − δx
α(f) = α₀/(1+kf).
~~~

Here f is the fraction adopting, α is the effective support rate per learner, δ a loss rate, and k specifies how adoption loads the support arrangement. The signs and functional form express the assumed sharing mechanism; they would have to change if adoption added support faster than demand.

For α₀=1, δ=0.25 and k=3 in the chosen time unit, the stationary readiness is α/(α+δ). It is about 0.714 at f=0.2 and 0.541 at f=0.8. If q=x² remains the receiving-event law, the corresponding contributions are about 0.510 and 0.292.

The loop is now visible: adoption changes support per participant, readiness changes the receiving-event rate, and that rate changes adoption. These stationary substitutions are useful only when readiness adjusts fast enough. Immediately after a large influx of beginners, replacing their states with these equilibria can be wrong.

A trial to increase adoption might therefore need additional teaching support. The equation does not prove that such support exists or how to teach the missing operation; those are provider questions.

#### DTM.3:5.3 - Spread changes compatibility without changing a learner

Consider a group comparing two exchange standards. Let f be the share of its relevant partners on the new standard. Over the same horizon, the group compares switching with continuing. Suppose it pays conversion costs while its old-standard partners keep their process unchanged. Its gain from switching is b−c−l(1−f): improvement b, switching cost c and conversion cost l for the remaining old-standard partner share.

Here the feedback is through compatible exchanges. No readiness state or training equation is needed. DTM.2 constructs the actual adoption event; the resulting adoption changes f and thus the gain available to later groups. A broadcast announcement is not the same as an authorized, affordable transition.

Use ECO.8 to retain the coordination and cost-bearing relations. Use the engineering compatibility method to establish that an adapter actually works. The spread model couples those supplied results rather than replacing them.

#### DTM.3:5.4 - Repeated opportunities do not create repeated first uptake

For one initially eligible recipient, suppose two independent comparable opportunities each succeed with probability 0.8. The probability of first uptake during those opportunities is 1−0.2²=0.96. It can also be obtained as 0.8+0.2×0.8: the second term includes only the recipients still eligible after the first opportunity.

The product 2×0.8=1.6 instead gives the expected number of successes when both attempts are actually performed and success is repeatable. It is not a first-uptake probability. Either quantity can be useful, but they feed different receiving models. The participant-state coupling must preserve that distinction even when the same internal readiness supplies both probabilities.

### DTM.3:6 - Bias-Annotation

A biological source can make “within” suggest a single organism and “between” a population of organisms. Recover the actual participant boundaries instead. A shared provider or a network may cross organizational boundaries.

A detailed internal model can also attract attention away from the only output the receiving question needs. Detail is justified by a changed prediction or decision, not by anatomical or organizational completeness.

### DTM.3:7 - Conformance Checklist

- The account names the event whose law changes and the participant state that changes it.
- Each boundary-crossing quantity has a subject interpretation, units where relevant, and an identified receiving use.
- Any feedback from spread is a stated mechanism; an omitted feedback has a bounded reason.
- Event-weighted contributions are distinguished from unweighted participant averages.
- A stationary reduction has a timescale and startup boundary; material delay or memory remains represented.
- A change in aggregation or participant boundary returns to the relevant modeling provider.

### DTM.3:8 - Common Anti-Patterns and How to Avoid Them

**Everyone transmits like the average participant.** Average the event contributions under the relevant contact weights and compare with the proposed reduction.

**A vertical of methods is a contact hierarchy.** Separate the simultaneously enacted operations from the network through which another participant encounters the practice.

**Fast equilibrium from the first moment.** Check newcomers and changed conditions before discarding internal time.

**Always draw two arrows.** Keep one-way coupling where justified; construct reverse influence only from an actual mechanism.

### DTM.3:9 - Consequences

The model can explain why a locally successful method fails to spread, or why its spread changes the conditions that made it successful. The cost is additional state or data when simple aggregation fails. Some cases become simpler after the correct interface quantity is identified.

### DTM.3:10 - Rationale

Cross-level modeling becomes useful when one process supplies a quantity that another process changes in return. The subject method must identify those quantities; general mathematical composition cannot choose them from a shared vocabulary alone. Explicit aggregation and time assumptions make the connection revisable.

### DTM.3:11 - SoTA-Echoing

[Zilio et al. (2026)](https://doi.org/10.1016/j.tree.2025.12.002) motivate separating within-carrier interaction from co-circulation and the feedback through transmission conditions. Their biological mechanisms are not used as universal cultural laws. The readiness and compatibility examples above are separate conditional constructions.

The historical [Katz–Shapiro model of compatibility and network effects (1985)](https://idv.sinica.edu.tw/kongpin/teaching/io/KatzShapiro1.pdf) supplies a contrasting mechanism in which others' adoption changes a user's outcome. Its equilibrium approach does not by itself provide the adoption or learning dynamics used here.

MMP.18 provides general coupling and reduction methods. C.32.MWA preserves distinctions between structures. DTM adds the construction connecting participant state, transmission contribution and conditions changed by spread.

### DTM.3:12 - Relations

- **DTM.2** identifies receiving events and variant changes; **DTM.4** examines the resulting regimes.
- **DTM.6** supplies interaction mechanisms that can change local or population conditions.
- **DTM.8/.9** add protective interventions and response dynamics where they matter.
- **MMP.18**, **MMP.16** and **C.32.MWA** supply mathematical composition, distinguishing observations and structural correspondence.
- **HCD**, relevant movement methods and engineering methods supply their own acquisition or physical mechanisms; DTM does not replace them.

### DTM.3:End

## DTM.4 - Find Conditions for Variant Invasion, Persistence and Return

**Type:** Method
**Status:** Stable

### DTM.4:1 - Problem frame

**Use this when** early growth, a fitted trend or a single threshold is being used to claim that a practice will establish itself, disappear, or return after an intervention.

A method may decline when few groups use it yet persist once compatible partners or supporting capabilities become common. A brief reduction can be followed by return to the same regime. A favorable gain from switching may still produce no uptake when no capable, authorized recipient receives the proposal.

The first result is a conditional account of possible continuation: whether a rare variant grows in a specified environment, what can maintain it, and what would change the reachable regime. Use the relevant mathematical methods to establish the properties of the chosen model; this pattern selects and connects the questions that a spread claim must answer.

For an immediate one-off choice with no reliance on persistence or later return, a comparison of the available actions may be sufficient.

### DTM.4:2 - Problem

“Increases now,” “can establish,” “persists under present conditions” and “cannot be reversed” are different claims. Local growth does not settle long-term coexistence. A stable regime need not attract every admissible initial condition. A mathematical equilibrium at zero remains possible even when a nonzero introduction would grow.

A threshold without its governing event law, surrounding state and admissible initial conditions can therefore support the wrong intervention.

### DTM.4:3 - Forces

| Force | Tension |
| --- | --- |
| A decision needs a useful prediction | The available model may establish only a conditional possibility. |
| A rare-variant test is inexpensive | Reinforcement or several interacting variants can require a finite introduction. |
| Local stability summarizes nearby behavior | Large changes and delayed feedback can cross its boundary. |
| A response changes current prevalence | It may also change the environment in which another variant can establish. |

### DTM.4:4 - Solution

**Specify the surrounding regime, test growth from rarity, find maintained regimes, then examine reachable change and return.**

#### DTM.4:4.1 - Preserve the law and the surrounding conditions

Recover the transmission and uptake construction from DTM.2 and the relevant feedback from DTM.3. Identify the variables being varied and those held fixed, the feasible state region, units of time and the environmental conditions. Keep the counted event and eligible population unchanged across that handoff. A per-recipient probability or hazard, a repeatable-event count and a population flow are different inputs; convert them using the stated receiving event before analyzing regimes.

State the practical question before solving: establishment from a small introduction, persistence of an existing variant, coexistence, reduction to a desired range, or return after a temporary change. “What happens?” is too broad when those questions depend on different initial conditions.

If a capability, permission or resource required for uptake is absent, preserve that absence in the law. A favorable comparison is not itself an event.

#### DTM.4:4.2 - Test a rare variant in a specified resident regime

Place the proposed variant at a small positive amount in an otherwise specified regime. Determine its initial growth from the modeled receiving events and losses.

For one rare quantity y, a local form y'=r y plus smaller terms gives growth when r>0 and decline when r<0. r concerns this surrounding regime and these assumptions. If r=0 or the neglected terms can dominate at the relevant scale, the first-order test does not decide.

With several linked rare states, use the appropriate coupled linearization or generation-to-generation operator supplied by the mathematical modeling method. Do not assign one scalar “reproduction number” until its construction and threshold apply to that model.

A zero initial amount can remain zero in a deterministic model with no external introduction. The rare-variant test asks about a small positive amount; it does not predict that an introduction will occur.

#### DTM.4:4.3 - Find what can maintain the variant

Find admissible stationary or recurring regimes and determine their relevant stability. Retain coexistence, oscillation or continued replacement if the model supports those forms; persistence need not mean a constant population share.

Where reinforcement or compatibility matters, examine finite initial amounts as well as rarity. A rare variant can decline while a sufficiently established variant persists. In that case, identify what separates the continuations and whether the proposed action can cross that boundary.

Use analytical reasoning, validated numerical calculation or a justified qualitative argument at the formality needed by the decision. A solver's last point alone is not evidence of an attracting regime; check the event law, feasible region and behavior under relevant nearby conditions.

#### DTM.4:4.4 - Distinguish a temporary displacement from a changed law

Model what the contemplated action changes. A one-time alteration of current use changes an initial condition. Continuing support, a compatibility adapter or a revised recognition rule can change a rate or a dependence. A newly available variant changes the candidate set.

Follow the trajectory during the action and after its removal. Ask whether the post-action state remains in the same region of attraction, enters another one, or encounters a different law because capabilities, resources or variants have changed.

For an intended return, identify the route and means needed to realize it. Lowering a parameter is insufficient if a necessary alternative has been lost or an endpoint is invariant under the model. Use C.36.RP and the relevant domain method to obtain an unavailable contribution; do not invent it as a free change in the state variable.

#### DTM.4:4.5 - Express the result as conditional continuations

Give the conditions and their consequences together:

- the surrounding regime in which a rare variant grows or declines;
- the maintained regimes relevant to the question;
- initial conditions or interventions that distinguish reachable continuations;
- the observations or changed assumptions that would defeat the account.

Use the existing comparison and portfolio methods when several actions remain viable. DTM.1 preserves whose consequences are being compared. DTM.6/.9 reopen the law when another variant or protective response changes the surrounding regime.

Stop with the weakest supported claim that answers the practical question. A useful conditional threshold need not become an unconditional prediction, and a qualitative return may be enough to reject an ineffective intervention.

### DTM.4:5 - Archetypal Grounding

#### DTM.4:5.1 - Rare growth and persistence give different answers

Consider a constructed reversible uptake model for the share f using a practice. The modeled adoption flow is s f²(1−f): encounters must provide the reinforcement represented by f². The modeled abandonment flow is s θ f(1−f): access to alternative users contributes to departure. Thus:

~~~text
f' = s f(1−f)(f−θ),    0≤f≤1,    s>0,    0<θ<1.
~~~

The two flows are nonnegative on the stated region. Their forms are hypotheses for this example, not universal properties of social learning. With θ=0.4 and s=1 per chosen time unit, the fixed points are 0, 0.4 and 1.

For 0<f<0.4 the derivative is negative; for 0.4<f<1 it is positive. The endpoint regimes attract interior states on their respective sides, while 0.4 separates them. At f=0.2 the rate is −0.032; at f=0.6 it is +0.048.

The rare-variant test reports decline near zero. It does not establish that an existing majority will disappear. The model instead gives persistence from the higher initial range. The first useful result is this distinction, before any choice of intervention.

#### DTM.4:5.2 - A temporary reduction can be followed by return

In the same model, suppose an admissible action temporarily changes f from 0.8 to 0.5. When the action ends and the old law resumes, f increases again because 0.5 remains above 0.4. A displacement to 0.3 would instead place the trajectory in the lower range.

These statements do not establish an available or legitimate way to change f. They tell the project what a claimed temporary intervention would need to achieve under the model. Changing ongoing support would require a revised law, not a fictitious one-time jump.

The endpoints in this model are invariant: departure is absent at f=1 and uptake absent at f=0. If the actual practice permits independent departure, outside introduction or invention, add those processes before using the endpoint predictions. A change in the underlying event account may remove the threshold or replace the two regimes.

#### DTM.4:5.3 - Compatibility changes a threshold but does not guarantee uptake

Suppose a switching group bears conversion costs while old-standard partners keep their process unchanged. Over one horizon, its gain relative to continuing is g(f)=2−0.5−3(1−f), where f is the adopter share. Assume equally weighted encounters in a homogeneous population, so f also gives the group's relevant partner share on the new standard. The gain is positive only above f=0.5.

An available adapter costing 0.4 and reducing the conversion coefficient to 0.2 gives gₐ(f)=2−0.5−0.4−0.2(1−f). At f=0.2, g=−0.9 while gₐ=0.94.

This is a threshold of the group's comparison, not yet a population stability result. Add the explicit event rule that a fraction e of the remaining groups receive a feasible, authorized offer and adopt when the gain is positive. Then one step gives:

~~~text
f_next = f + (1−f)e × indicator(g>0).
~~~

For f=0.2 and e=0.25, the share remains 0.2 without the adapter and becomes 0.4 with it. For e=0, neither positive gain nor a favorable threshold produces uptake.

This constructed rule omits departure, unequal partners and changing expectations. To conclude persistence or reversibility, supply those mechanisms where they matter and repeat the corresponding question. ECO.8 retains the coordination and allocation of costs; the engineering method establishes compatibility.

### DTM.4:6 - Bias-Annotation

The term “invasion” denotes growth from a small positive presence in a specified model. It assigns neither moral value nor an instruction to spread something.

An attractive tipping-point narrative can encourage modelers to choose reinforcement in advance. Compare a simpler uptake law when the evidence does not establish it, and preserve the resulting difference in continuation.

### DTM.4:7 - Conformance Checklist

- The practical question distinguishes establishment, persistence and return.
- The resident state, feasible region and event law are identifiable.
- A rare-variant result is conditional on a specified surrounding regime and a nonzero introduction.
- Maintained regimes are distinguished from a trajectory's transient values; finite-introduction effects are examined where relevant.
- The proposed action changes an initial condition, law, resource or variant set explicitly.
- The result after action removal and any unavailable return contribution remain visible.
- A comparison threshold is not presented as proof of uptake, stability or authority.

### DTM.4:8 - Common Anti-Patterns and How to Avoid Them

**A positive trend proves inevitability.** Recover the surrounding regime and test the continuation that the claim actually needs.

**Rare decline proves eventual disappearance.** Examine persistence from established states when reinforcement or compatibility supplies a different regime.

**One successful reduction proves durable change.** Follow the post-action law and reachable state.

**A profitable transition occurs automatically.** Include exposure, means and authority in the event rule.

### DTM.4:9 - Consequences

The result can reject an intervention that only displaces the state temporarily, or reveal that a failed small introduction does not rule out persistence under different conditions. Its value depends on the event law and feasible actions; precise calculation cannot repair a missing mechanism.

### DTM.4:10 - Rationale

Establishment, persistence and return are related questions on one dynamic account, but they use different evidence. Keeping them together prevents a local calculation from answering a more expansive question by implication. Mathematical methods supply the analysis; the subject method keeps its conditions connected to the intended change in practice.

### DTM.4:11 - SoTA-Echoing

[Solé et al. (2026 preprint)](https://arxiv.org/abs/2609.03344) provide a current example of reinforcement producing multiple stable coupling regimes. This motivates examining establishment and persistence separately; the one-variable construction above is a different illustrative model, not a reduction or empirical validation of that paper.

The historical [Katz–Shapiro compatibility analysis (1985)](https://idv.sinica.edu.tw/kongpin/teaching/io/KatzShapiro1.pdf) shows why outcomes may depend on other adopters. A gain comparison does not supply an adoption process. The worked adapter construction adds its own explicit event rule and leaves stronger dynamic claims open.

The pattern uses existing mathematical stability and continuation methods. Its contribution is the linked subject inquiry from rare growth through maintained regimes to feasible return.

### DTM.4:12 - Relations

- **DTM.1** preserves the participants and consequence comparison.
- **DTM.2/.3** supply the event law, internal change and feedback.
- **DTM.5/.6** can change the resident composition or selection conditions.
- **DTM.8/.9** supply protective actions and their dynamic effects.
- **MMP**, relevant mathematical and computational methods perform the selected analysis; **C.36.RP** helps recover a contribution needed for an otherwise unavailable return.

### DTM.4:End

# Part II — Competition, coexistence and diversion

## DTM.5 - Separate Selection Within and Among Collectives

**Type:** Method
**Status:** Stable

### DTM.5:1 - Problem frame

**Use this when** a variant becomes more common within each participating group, yet its overall prevalence changes differently—or when a claimed advantage of a collective is being used to explain which variants continue.

A shortcut can gain users inside every team while teams that use it less contribute more of the next period's procedures. Conversely, a practice can be costly to a current member while supporting a group's continued operation. These situations require distinguishing units of continuation and the processes that change their weights.

The first result is a decomposition of the observed or modeled change, followed by an account of which parts have a supported selection mechanism. The decomposition alone does not establish causation or justify privileging a higher level.

For comparing the current performance of two organizations without a question about differential continuation, use the existing evaluation and choice methods.

### DTM.5:2 - Problem

An overall mean mixes changes within groups with changes in the groups' contributions to what continues. Calling either component “group success” leaves its unit unclear: more copied methods, more learners, survival of the same organization, or more successor organizations.

The same arithmetic can also arise without selection. Reconstruction, unequal exposure, recruitment or a changed measurement can alter the mean. A useful account must therefore distinguish the bookkeeping identity from the causal explanation.

### DTM.5:3 - Forces

| Force | Tension |
| --- | --- |
| Groups influence continuation | A chosen grouping can create an apparent group effect without a group-level cause. |
| Aggregate change is observable | Its contributing events may have different sources or mixed parentage. |
| Within-group advantage matters | It may conflict with what makes a collective continue or contribute. |
| Selection language is compact | It can conceal changes of counted unit and normative recipient. |

### DTM.5:4 - Solution

**Choose the unit of continuation, trace its sources, separate the changes, then investigate the mechanisms behind them.**

#### DTM.5:4.1 - Decide what the next population counts

Name the earlier population, the receiving population and the interval or transition connecting them. Specify the continuing unit: an executed method variant, a learner retaining it, a transmitted procedure instance, or a collective with an identified successor relation.

A group can contribute many transmitted instances without producing a new group. Use the first kind of count for variant continuation and the second for collective reproduction. Survival, revenue or an externally assigned quality score does not automatically measure either.

C.36 supplies the cultural relations; DTM.1 identifies the variant and affected work. Return to DTM.2 if the available record shows only copies of descriptions while the claim concerns continued execution.

#### DTM.5:4.2 - Recover contribution weights and within-group change

For each source group, identify how much of the receiving population derives from it and how the relevant property changes along that contribution. Use the actual source relation, rather than assuming that every present member contributes equally.

When multiple groups contribute to one resulting method, choose an allocation supported by the receiving question or retain unresolved source shares. A convenient attribution convention is not evidence of biological or cultural inheritance.

Account for every receiving unit once. Mark the part attributed to the identified source groups and any external or unresolved part; shared source attribution must not count the same unit twice. If the record covers only part of the receiving population, retain that coverage in the result.

Keep differences due to reconstruction, recruitment and observation visible. For example, a transmitted procedure may omit a check during reconstruction even if no recipient deliberately selected the unchecked variant.

#### DTM.5:4.3 - Decompose the aggregate change

For a scalar property, let π_g be the source population's weight in group g, z_g its initial mean, w_g its contribution per source unit to the covered part of the receiving population, and Δz_g the change in the corresponding transmitted mean. Weights π_g sum to one; the mean contribution w̄ is positive. The source-attributed contributions must cover that part without omission or double counting.

The covered mean and its difference from the initial mean satisfy:

~~~text
z_cov = Σ_g π_g w_g (z_g + Δz_g) / w̄
z_cov − z_old
  = Cov_π(w,z) / w̄ + Σ_g π_g w_g Δz_g / w̄.
~~~

The first term expresses the effect of different contribution weights associated with the earlier property. The second expresses changes along those contributions. If those contributions cover the whole receiving population, z_new = z_cov.

Otherwise let c be the covered fraction of the receiving population and z_ext the mean property in the rest, using the same counted unit and weighting convention. Include that contribution:

~~~text
z_new = c z_cov + (1−c) z_ext
z_new − z_old = c (z_cov − z_old) + (1−c)(z_ext − z_old).
~~~

An unknown external composition remains unknown; it is not zero. For a binary variant share and known c, the possible new share lies between c z_cov and c z_cov + 1−c until the external composition is constrained. When no receiving unit derives from the identified sources, omit their decomposition and calculate from the other contribution. MMP and the relevant mathematical methods supply the calculation.

This identity does not tell why w or Δz has the observed value. Call them between-source and within-contribution changes until the causal interpretation is established. If the units are collectives, redefine z and w for collective continuation; do not carry over a particle count while silently changing the claim.

For a question needing no scalar aggregate, retain the corresponding source and change table. Do not invent a total score solely to use the formula.

#### DTM.5:4.4 - Test the proposed selection mechanisms

For within-group selection, identify the process by which variants contribute differently under the group's conditions. For a between-group explanation, identify what group property changes survival, contribution, recruitment or successor formation.

Consider an alternative that could reproduce the same decomposition: groups may encounter different audiences, receive unequal support, have different ages, or be observed with different completeness. Choose the distinguishing observation or comparison with MMP.16 and the applicable research method.

The response to a change must follow the mechanism. If a group's larger contribution comes from privileged broadcast access, altering an internal learning method may leave that advantage unchanged. If the advantage comes from reliable results that others adopt, changing access alone can hide the relevant production difference.

#### DTM.5:4.5 - Return the decomposition to the work question

State the units, contribution relation, covered population and any external contribution, distinct components of change, supported causes and consequential unknowns. If coverage or external composition is unresolved, return the supported range or restrict the claim to the covered part. Then ask which feasible change addresses the problematic relation.

A practice favored within teams but associated with lower total contribution can persist locally. A collective's growth can also coexist with costs to its members. D.3/D.4 and the existing decision methods retain those conflicts; no arithmetic term grants moral priority to its level.

Use DTM.3/.4 to examine dynamic continuation and DTM.6 when another variant changes the contribution mechanism. Stop with the descriptive decomposition when causality remains unresolved and that description is sufficient for the receiving use.

### DTM.5:5 - Archetypal Grounding

#### DTM.5:5.1 - Within-group increase is canceled by changing contribution weights

Take two equally weighted source groups. Their initial shares of variant B are 0.2 and 0.8. Along each group's transmitted contribution the B share increases by 0.1. The groups supply relative transmitted-instance counts of 2 and 1.

The initial overall B share is 0.5. The receiving share is:

~~~text
(2 × 0.3 + 1 × 0.9) / 3 = 0.5.
~~~

The contribution-weight change is −0.1; the within-contribution change is +0.1. They cancel. An unchanged aggregate would therefore conceal two material changes.

The weights count transmitted instances, not new organizations and not usefulness. The result does not establish why the low-B group supplied twice as much. Better results, broader access or a sampling difference are possible explanations requiring different follow-up.

If the two groups instead supply equal counts, the new B share becomes 0.6. This changed condition shows which contribution the aggregate depended on.

#### DTM.5:5.2 - A copied method can change without being selected

Suppose every teaching group sends one equally weighted procedure, but recipients reconstruct it with a different timing convention. A change in the receiving mean belongs to the within-contribution term. There is no differential contribution in this stipulated case.

The next action is to study reconstruction with DTM.2 and the relevant learning or notation method. Calling the change selection would direct attention away from how the recipient obtained the new variant.

#### DTM.5:5.3 - Counting successor collectives answers another question

A project network may form successor teams with different arrangements. If the question is which arrangement becomes common among successor teams, count those teams and recover their formation relations. If the question is which procedure most workers later use, count the corresponding use and contribution relations.

One prolific source team can dominate the latter count without dominating the former. The choice of unit is part of the question, not a defect to remove by finding one universal fitness number.

#### DTM.5:5.4 - External arrival changes the receiving mean

One procedure instance A continues from the identified source, with B-share z_old = z_cov = 0. One instance B arrives from outside that source set. The receiving population has two instances, so c=1/2 and z_ext=1. Its B-share is (1/2)×0 + (1/2)×1 = 1/2. A source-only calculation would return zero because it answers only for the covered part.

If the external instance's variant is unknown, the whole-population B-share lies between 0 and 1/2. Additional source tracing is needed only if that uncertainty changes the receiving decision. Neither result attributes the external arrival to selection within the original source.

### DTM.5:6 - Bias-Annotation

Grouping by a striking label can make an accounting effect look like a collective cause. Recover the source relations and plausible alternatives before asserting that causal level.

The phrase “higher-level success” also invites a value judgement. Name what continues and who benefits separately.

### DTM.5:7 - Conformance Checklist

- The earlier and receiving populations, interval and counted unit are identified.
- Group contribution is not confused with reproduction of the group itself.
- Source weights and changes along contributions can be reconstructed or their uncertainty is stated.
- The receiving population is covered without omission or double counting; external contributions enter the mean, or the result is explicitly bounded to the covered part.
- The decomposition uses consistent units and does not serve as its own causal explanation.
- Reconstruction and differential exposure remain alternatives where they could change the answer.
- The practical conclusion retains conflicts among affected participants instead of assigning automatic priority to a level.

### DTM.5:8 - Common Anti-Patterns and How to Avoid Them

**The aggregate did not change, so nothing happened.** Recover both components and their possible cancellation.

**A profitable team has higher reproductive success.** Establish the continuation unit and contribution relation; profit may explain one, but does not define it.

**A covariance proves group selection.** Investigate the mechanism and a consequential competing explanation.

**Every inherited change is selection.** Keep reconstruction and transformation distinct from differential continuation.

### DTM.5:9 - Consequences

The method exposes conflicts hidden in a population mean and prevents intervention at the wrong mechanism. It also limits overclaiming: a valid decomposition may leave the causal question open. Source attribution and comparable observations can be costly; their required precision follows the receiving decision.

### DTM.5:10 - Rationale

Multilevel change is not simply the same selection calculation repeated at larger scales. The objects counted, their contribution relations and the causal mechanisms can differ. An explicit decomposition makes those differences inspectable.

### DTM.5:11 - SoTA-Echoing

[Bourrat, *Multilevel selection 1, multilevel selection 2, and the Price equation: a reappraisal* (2023)](https://doi.org/10.1007/s11229-023-04285-1) sharpens the distinction between contributions of particles from collectives and reproduction of collectives. This method adopts the unit distinction without resolving the paper's broader interpretation of multilevel selection.

Compared with following only aggregate prevalence, the decomposition can reveal offsetting changes at modest additional calculation cost. Compared with treating every group association as causal selection, it requires the source and causal relation that would change intervention. Existing mathematical and research methods supply those tests; DTM retains the units and continuation question.

### DTM.5:12 - Relations

- **DTM.1/.2** supply the variant, consequences, uptake and reconstruction distinctions.
- **DTM.3/.4** investigate coupled continuation and persistence.
- **DTM.6** models interactions that can change contribution weights.
- **C.36**, **MMP.16**, **D.3/D.4** retain cultural relations, discrimination of explanations and conflicts between interests.

### DTM.5:End

## DTM.6 - Model Competition and Facilitation between Variants

**Type:** Method
**Status:** Stable

### DTM.6:1 - Problem frame

**Use this when** a method spreads, persists or works differently in the presence of another variant, and treating the two independently would change the decision.

Two procedures may draw on the same limited capacity. One practice may teach a notation needed by another. A shared response to both may restrict them unequally. These are different mechanisms; identifying the connection comes before choosing an equation.

The first useful result is a dependence of one variant's execution, continuation or transmission on the other, through a named relation that can be investigated. The result includes the independent-action comparison and an observation that could distinguish the explanations.

If the question concerns only two interacting components, with no continuation or transmission of variants, ordinary subject modeling is sufficient.

### DTM.6:2 - Problem

Correlation between variants does not establish competition or facilitation. They may share favorable conditions, reach the same audiences or be counted differently. Conversely, fitting each variant separately can miss a real interaction and recommend a change that releases the other.

A useful model must show what one variant changes for the other. It must also distinguish an immediate effect, a later feedback and the effect of changing the intervention itself.

### DTM.6:3 - Forces

| Force | Tension |
| --- | --- |
| Simple separate models are tractable | Their independence can remove the relation that controls the outcome. |
| A familiar interaction model is available | Its resource, response or contact assumptions may not hold here. |
| Co-occurrence supplies evidence | Shared conditions can produce it without interaction. |
| Intervention changes one variant | It may also change the intermediary and the other variant's conditions. |

### DTM.6:4 - Solution

**Identify the affected result, recover the connecting relation, construct its effect and compare joint with independent action.**

#### DTM.6:4.1 - Name the variants, result and comparison

Use DTM.1/.2 to identify what continues and how a transmitted instance is recognized. State whether the current result is successful execution, persistence in a participant, uptake elsewhere or a consequence for an affected party.

Choose the comparison at comparable conditions: what would change if the other variant were absent, held fixed or prevented from changing the suspected intermediary? These are different comparisons. A feasible observation or intervention must support the one used.

Do not call one variant a competitor merely because its name occupies a neighboring category. Two differently named methods can draw on different resources; two instances of the same named method can compete for a limited one.

#### DTM.6:4.2 - Recover the intermediary

Ask what the first variant changes that the second uses or encounters. Possibilities include a resource, a shared response, compatibility with partners, prerequisite capability or the contact network.

For the selected relation, identify the changing quantity or condition, its effect on the second variant and any return effect. Use observations of that relation where possible. Retain independent action or common external cause when the connection remains unresolved.

Distinguish an indirect effect from a direct interaction. A practice can alter the audience available to another without ever being executed by the same participant.

#### DTM.6:4.3 - Build the dependence from the relation

The construction follows the intermediary:

- **Shared limited capacity:** account for available capacity and the amount each variant occupies or consumes. Derive each variant's feasible execution or growth from what remains. A replacement assumption is needed if one unit displaces another.
- **Shared response:** relate each variant to formation of the response, then relate that response to each variant's continuation. Unequal sensitivity matters. DTM.9 develops response dynamics, costs and memory.
- **Compatibility:** relate partner composition and conversion arrangements to successful exchange, its cost and the consequences of adopting the variant. Existing incompatibility need not make exchange impossible.
- **Prerequisite capability:** relate execution or transmission to the capability supplied by another practice. Separate acquiring the prerequisite from encountering a description of it.

MMP supplies the representation and admissible operations for the dependence. Do not infer any of these mechanisms from the word “competition.”

#### DTM.6:4.4 - Compare independent and coupled results

Evaluate the same result under the independent account and the account containing the proposed relation. Keep other relevant conditions comparable. Examine a range of plausible conditions when the effect's sign or size changes with them.

A negative immediate effect can coexist with a positive later effect. For example, training consumes current execution time but may enlarge later capability. Give the horizon; do not compress the two into an unexplained positive or negative coefficient.

For establishment of a rare variant, evaluate its continuation in the environment maintained by the resident variants. That invasion calculation belongs to DTM.4 and is needed only when establishment is the question. Coexistence, switching order and transient disruption can require different analyses.

#### DTM.6:4.5 - Choose a distinguishing observation and pass the result on

Use MMP.16 to identify an observation or permissible comparison that differs between the coupled account and its serious alternative. If removing one variant also changes resources, staffing and audience, the result alone does not isolate the proposed mechanism.

Return the conditional dependence, comparison and unresolved alternatives. DTM.3 links the effect to transmission between participants; DTM.4 investigates persistence. Use DTM.7 only if a shared mechanism is actually diverted from its intended result. Ordinary resource competition does not establish diversion or intent.

### DTM.6:5 - Archetypal Grounding

#### DTM.6:5.1 - Restricting both variants can favor the less sensitive one

Consider a hypothetical community sharing procedures. A and B denote normalized execution activity inside one group, with A+B no greater than one. Remaining capacity is R=1−A−B. A yields useful results in this case; B produces specified errors. These are descriptions of practices and outcomes, not classes of people.

Suppose a shared checking response a affects them differently:

~~~text
A' = A(2R − 0.2 − a)
B' = B(R − 0.3 − 0.2a).
~~~

These illustrative coefficients are stipulated, not measured. Two connections are now visible: both use R, and a restricts A more strongly. Holding activity fixed, an increase in a lowers both instantaneous growth rates. Over time, loss of A also releases capacity for B. The sign of B's eventual change cannot be read from its direct response term alone.

DTM.9 completes this example by modeling how a is formed and calculating the later outcome. If a real procedure catalogue does not have the assumed capacity competition or differential checking effect, this model is not its explanation. A distinguishing investigation must recover those relations.

#### DTM.6:5.2 - Compatible partners can make an unfamiliar method worth adopting

Suppose the proposed method gives a group a benefit of 2 units over a fixed horizon and costs 0.5 to adopt. Exchange with a partner using the old method remains possible through manual conversion. The switching group bears conversion cost 3 per unit share of old-method partners.

If f is the share of its relevant partners already using the proposed method, its gain relative to continuing is:

~~~text
g(f) = 2 − 0.5 − 3(1−f).
~~~

An independent estimate that omits partner conversion gives 2−0.5=1.5. The coupled estimate instead gives −0.9 at f=0.2 and 0.9 at f=0.8. At the lower share, ignoring compatibility therefore reverses the sign of the choice. Here other adopters facilitate adoption by reducing conversion work. No shared defensive response is needed.

An available adapter costing 0.4 over the same horizon and reducing the conversion coefficient to 0.2 changes the gain to 2−0.5−0.4−0.2(1−f), or 0.94 at f=0.2. The participants, cost allocation and horizon are unchanged. If costs instead shift to old-method partners, both parties' consequences must be recomputed.

A comparison that records conversion work and partner composition can distinguish this account from an unrelated reluctance to adopt. Adoption still requires opportunity, capability and authority; a positive gain is not a transmission event. DTM.2/.4 supply those further questions.

#### DTM.6:5.3 - A notation practice can facilitate another method's transmission

A group encounters a useful construction but cannot reconstruct its diagrammatic operations. A notation-learning practice may change that capability. The proposed connection is therefore capability → reconstruction of the transmitted method, not contact → uptake alone.

Compare subsequent reconstruction on suitable tasks, while retaining differences in prior knowledge and exposure. If only familiarity with the example increases, the evidence does not establish general facilitation. Human learning and AI training use their respective subject methods; this pattern does not prescribe one learning algorithm.

### DTM.6:6 - Bias-Annotation

Resource competition is an attractive default because it readily yields equations. The intermediary may instead be compatibility, capability or audience structure.

A second bias is to treat observed dominance as intrinsic superiority. A variant can dominate because another practice changed its conditions, while producing worse results for a specified recipient.

### DTM.6:7 - Conformance Checklist

- The affected result concerns execution, continuation or transmission of identified variants.
- The comparison states what is absent, held fixed or changed.
- A connecting relation supports the dependence, or competing explanations remain explicit.
- Independent action is compared with the coupled account under stated conditions.
- Immediate effects, later feedback and the relevant horizon remain distinguishable.
- A selected observation can discriminate a consequential alternative.
- The model does not turn ordinary interaction into evidence of capture, harm or intent.

### DTM.6:8 - Common Anti-Patterns and How to Avoid Them

**Co-occurrence proves facilitation.** Check shared exposure and other common causes.

**Everything competes for one resource.** Identify what is actually limiting and how use changes availability.

**Restricting both must reduce both.** Follow indirect effects through the intermediary and later state.

**The positive gain explains adoption.** Recover the encounter, feasible execution and choice relation separately.

### DTM.6:9 - Consequences

The method reveals when separate estimates would give a wrong intervention direction. It can also justify retaining separate models when no consequential coupling is supported. The cost is identifying and observing the intermediary; a more elaborate coupled model is not automatically more informative.

### DTM.6:10 - Rationale

Transmission and continuation change the environment in which variants act. Modeling the actual relation preserves this feedback without treating every interaction as biological competition. The same operation accommodates limiting and enabling relations while leaving their subject laws to the relevant practice.

### DTM.6:11 - SoTA-Echoing

[Zilio et al., *Co-circulation and co-infection: parasite interactions across scales* (2026)](https://doi.org/10.1016/j.tree.2025.12.002) distinguish interaction routes that can operate within and between carriers. The adopted lesson is to recover the route; biological observations do not validate a cultural dependence.

[Ramesh and Hall (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12203456/) provide a current biological treatment of competition involving shared resources and response. The illustrative activity equations here are our construction, not a reproduction or fitted application of that model.

[Katz and Shapiro, *Network Externalities, Competition, and Compatibility* (1985)](https://idv.sinica.edu.tw/kongpin/teaching/io/KatzShapiro1.pdf) are a historical source for compatibility-dependent benefit and differing incentives. Their equilibrium analysis does not supply the uptake law used by a current engineering case.

Compared with using an interaction coefficient alone, recovering the intermediary costs more but identifies what an intervention could change. When a verified subject model already supplies that dependence, reuse it.

### DTM.6:12 - Relations

- **DTM.1/.2** identify variants, affected results and transmission events.
- **DTM.3/.4** connect local interaction to spread and persistence.
- **DTM.5** separates contribution changes across groups without assuming interaction.
- **DTM.7/.9** develop diversion and response feedback when those mechanisms are present.
- **MMP.11/.16/.18** supply model construction, discrimination and justified coupling.
- **ECO.8** helps retain coordination, authority and cost-bearing relations in compatibility changes.

### DTM.6:End

## DTM.7 - Locate Diversion of a Shared Control or Cooperation Mechanism

**Type:** Method
**Status:** Stable

### DTM.7:1 - Problem frame

**Use this when** a shared arrangement keeps granting access, attention, resources or further use, yet the resulting activity fails the work it was meant to support—and this relation may help the activity continue.

A procedure catalogue can recommend a method because its description resembles a trusted entry, while the method does not produce the required result. A coordination arrangement can keep rewarding a measured output after the connection between that output and the intended work has broken.

Start by tracing one grant of support from its recognition signal to its actual consequence. The first useful result is the possible diversion point, a supported alternative explanation and a check that could distinguish them.

If two variants simply compete for a resource under the arrangement's intended rules, use DTM.5/.6. Difference of interests, dependence or local failure alone does not establish diversion.

### DTM.7:2 - Problem

Calling an arrangement “captured” can replace the causal account with a presumed adversary. Conversely, checking each component against its local specification can miss that a successful sequence now supports another result.

The practical question is which relation converts a signal into support, how that support changes the relevant outcome, and whether the resulting activity feeds its own continuation. Intention is a separate claim.

### DTM.7:3 - Forces

| Force | Tension |
| --- | --- |
| Shared arrangements reduce coordination cost | One weak recognition relation can affect many uses. |
| Proxies make decisions affordable | Their relation to the intended result can fail or change. |
| Local participants may follow their instructions | Their combined activity can sustain an unwanted result. |
| Defensive change can stop diversion | It can also block legitimate use or move costs to others. |

### DTM.7:4 - Solution

**Trace the intended work, the support-granting relation and the resulting continuation; locate and test the mismatch before choosing a defensive change.**

#### DTM.7:4.1 - Recover the intended result and affected parties

Name the shared arrangement and what its participating parties are entitled to expect from it. Separate the provider, the performer, the recipient of the work result and parties affected indirectly. A.6.P.RI helps restore the standpoint of each claim.

Use an applicable agreement, objective or established function to identify the intended result. A preferred outcome asserted by one observer does not by itself define misuse by everyone else.

DTM.1 supplies the consequences and dependence account. If a practice is merely unfamiliar and no relevant adverse effect or violation has been established, stop the diversion claim.

#### DTM.7:4.2 - Follow one grant of support

Recover the relation in ordinary terms:

~~~text
observed signal → recognition or decision
                → granted operation or resource
                → work actually performed
                → result for the named parties.
~~~

The signal may be a description, measured output, recommendation or observed behavior. The grant may be admission to a catalogue, execution by an agent, access to a shared resource or repeated recommendation.

For each arrow, ask what makes it operate. Distinguish an automatic controller from a person's judgement and from a standing allocation rule. C.30.LCA supplies the control description when layered feedback matters; do not invent a controller where a simple institutional rule explains the relation.

#### DTM.7:4.3 - Locate the mismatch and the continuation feedback

Compare what the recognition signal warrants with what the granted operation produces. A mismatch can lie in an unreliable signal, an inappropriate interpretation, the decision rule, the available action, or the subject model connecting action to result.

Ask why the signal and result have separated. Selection on a noisy measure can favor unusually overestimated cases; unfamiliar operating conditions can invalidate a formerly useful relation; changing the measured variable or the participant's response to the rule can alter that relation. These explanations call for different corrections and do not all imply diversion.

Then recover how the grant affects continuation of the variant: more encounters, successful executions, source visibility, resources for further use or inheritance by a later procedure. DTM.2/.3 construct that continuation relation.

Keep three possibilities separate:

- the shared arrangement is diverted toward an incompatible result;
- the arrangement is functioning as specified but its objective or allocation is contested;
- ordinary implementation error or model error causes poor performance without a self-supporting continuation mechanism.

Only the first warrants the diversion account as stated. The others can still require action through their own methods.

#### DTM.7:4.4 - Compare a causal change with a serious alternative

Choose a feasible comparison that changes the suspected relation while preserving enough of the work to interpret the result. Examples include checking the work result independently of the familiar description or testing whether recommendations still differ when subject performance is comparable.

Observe the activity in conditions where the signal actually governs support, and check the work result independently. If a separate test removes the relevant incentive or opportunity, good performance there does not by itself establish that the ordinary support relation is sound. Retain that difference in the comparison instead of inferring a permanent disposition of the agent.

The comparison must not assume the distinction it is meant to establish. If the only reason a method is labeled unreliable is that it is unfamiliar, filtering that label cannot validate the diagnosis.

Consider an alternative such as unequal resources, unsuitable tasks, changed operating conditions or a conflict over the intended objective. Use MMP.16 and the subject research method to distinguish it. A single sequence of events can locate a hypothesis without confirming its cause.

#### DTM.7:4.5 - Design the smallest consequential correction

Once the relation is supported, consider changing the signal, its interpretation, the grant rule, the available operation or feedback from the actual result. Recover the required authority and practical means separately.

DTM.8 compares these actions with reducing consequences or restoring the function. DTM.9 examines their costs, false restrictions and feedback on other variants. Test whether the correction still admits legitimate use and whether another route would reproduce the same mismatch.

Return the mechanism and conditions, not a permanent classification of an agent as a parasite. Evidence of deliberate manipulation may matter to the receiving practice, but is not needed to model an unintentional diversion and cannot be inferred from benefit alone.

### DTM.7:5 - Archetypal Grounding

#### DTM.7:5.1 - A catalogue recommends descriptions instead of usable methods

In a hypothetical catalogue, a familiar-looking description increases the chance that a method is recommended. Recommendation produces trial use, and trial-use counts increase its later visibility. Suppose a method B resembles a trusted method A in description but omits an operation necessary for the advertised result.

The candidate loop is:

~~~text
description similarity → recommendation → trial use
                       → visibility → more recommendation.
~~~

The intended contribution—helping users obtain the advertised work result—is absent from the loop. This is a diversion hypothesis, not yet a finding about a real catalogue.

A discriminating comparison examines the recommendation relation and tests the methods on suitable tasks with the necessary prerequisites. If descriptions do not affect access, the proposed first link is false. If B succeeds under its stated conditions, poor outcomes may instead reflect unsuitable use. If result failure is established but recommendations do not feed continuation, the recurrence mechanism needs another explanation.

One possible correction is to connect recommendation to demonstrated result under recoverable conditions. Its cost, errors and effect on new useful methods remain questions for DTM.8/.9. It is not enough to replace one unexplained reputation score with another.

#### DTM.7:5.2 - A completion count can sustain incomplete work

Suppose a team receives support for the number of completed cases, while downstream users need resolved cases. Closing a record is necessary for the administrative measure but does not establish resolution. A procedure that closes records early can raise the measured output and therefore receive more support.

First recover whether support really depends on that count and whether unresolved cases impose the stated downstream cost. If both links hold, the candidate diversion lies in treating record closure as evidence of resolution. It does not require anyone to intend harm: all participants may be following their assigned criteria.

A sampled follow-up on outcomes can distinguish premature closure from a real improvement in resolution speed. Changing the measure without ensuring that resolution can be observed would leave the original difficulty intact.

#### DTM.7:5.3 - Resource competition is not necessarily diversion

Two valid methods may both need a limited specialist. The allocation rule may grant more time to one, reducing the other's use. If the rule, signal and resulting work retain their intended relation, this is competition or a disputed priority.

DTM.6 models the resource dependence; the relevant coordination and decision methods address the priority. Searching for an imitated signal or concealed attacker would not improve that account.

### DTM.7:6 - Bias-Annotation

A biological metaphor can turn disagreement into presumed infection. Restrict the claim to the identified practice, relation and consequence.

Another bias is to presume that a local beneficiary designed the failure. The causal account of support and continuation does not establish intention, responsibility or authority to intervene.

### DTM.7:7 - Conformance Checklist

- The shared arrangement, intended result and relevant parties are recoverable.
- The signal, decision, granted support and actual consequence remain distinct.
- A specific mismatch and its role in continuation are supported or labeled as hypotheses.
- Contested objectives, ordinary competition and implementation error have not been silently reclassified as diversion.
- A feasible comparison can distinguish a consequential alternative.
- Proposed corrections retain legitimate use, costs, authority and possible feedback.
- The conclusion concerns a mechanism rather than a permanent kind of person or group.

### DTM.7:8 - Common Anti-Patterns and How to Avoid Them

**Someone benefits, therefore the mechanism was captured.** Recover the mismatch and continuation relation.

**Every component passed, therefore the work succeeded.** Follow the combined result to its intended recipient.

**Unfamiliar means harmful.** Test the work result and conditions, not conformity of appearance.

**A new score fixes a bad score.** Establish how the new observation supports the receiving decision and what its errors change.

### DTM.7:9 - Consequences

The method turns a broad accusation into a testable account and identifies several possible correction points. It can also reject the diversion hypothesis while preserving a real resource or objective conflict. Tracing outcomes can cost more than reading a proxy; the gain depends on whether that relation changes a consequential decision.

### DTM.7:10 - Rationale

A shared arrangement can amplify a small mismatch because many participants reuse the same recognition and allocation relation. Recovering that relation explains continuation without requiring an adversary or a biological reproduction model. The protection question then becomes how to restore the work while retaining the benefits of sharing.

### DTM.7:11 - SoTA-Echoing

[Manheim and Garrabrant, *Categorizing Variants of Goodhart's Law* (2018, revised 2019)](https://arxiv.org/abs/1803.04585) distinguish proxy failure through selection on noise, use outside familiar conditions, changed causal relations and other agents' responses. This historical distinction informs :4.3: poor results under a high score need not have one cause. Correcting measurement, reconsidering the operating range and changing a support rule answer different failures.

[Qi et al., *Training a Misaligned Reward Seeker* (2026)](https://alignment.anthropic.com/2026/reward-seeker/) report that reward-hacking training produced harmful reward-seeking behavior in some evaluation contexts, while tests without a clear grading opportunity did not reveal that behavior. The relevant contribution to :4.4 is context-sensitive diagnosis: inspect the relation where support is actually granted. This experiment concerns one training setup; it does not establish a universal trait of AI agents, human intention or a general cultural law.

The synthesis uses a mechanism-specific account of proxy failure and checks it in the support-granting context. Compared with auditing each component or tightening a score threshold, the additional work can distinguish a bad measurement from a changed incentive or causal relation. Compared with assuming an attacker, it retains unintended reinforcement and failures without a continuation loop. If measurement correction alone restores the required result and there is no consequential continuation question, stop with that simpler repair.

Use an established subject fault-analysis or control method when it already resolves the whole relation. DTM adds the connection to differential continuation or transmission only when that connection matters. Reopen the explanation if the proposed support link is absent, another mechanism fits the observations better, or behavior changes when the support conditions change.

### DTM.7:12 - Relations

- **DTM.1** establishes dependence and consequences without presuming exploitation.
- **DTM.2/.3** explain how granted support changes continuation.
- **DTM.5/.6** supply selection and interaction alternatives to diversion.
- **DTM.8/.9** compare corrections and their response feedback.
- **A.6.P.RI** restores the standpoint of claims; **C.30.LCA** supplies layered control distinctions when applicable.
- **MMP.16** supports the discriminating comparison; existing coordination methods retain authority and resource assignment.

### DTM.7:End

# Part III — Protective action and its consequences

## DTM.8 - Compare Protective Actions against Continuing or Spreading Activity by Target and Remaining Effects

**Type:** Method
**Status:** Stable

### DTM.8:1 - Problem frame

**Use this when** several proposed protective actions promise a similar improvement but act on different parts of a continuing or spreading practice.

Reducing exposure does not necessarily stop an already established activity. Reducing its consequences does not necessarily stop its further transmission. Restoring a useful function does not necessarily restore the old arrangement. These differences determine what the action can accomplish and what must accompany it.

Start with the function and affected party to be protected, then locate what each feasible action changes. The first result is a comparison of intervention targets, their direct effects, important remaining effects and implementation conditions.

For an already understood isolated hazard with no continuation or transmission question, use the relevant subject protection method. This pattern does not supply clinical, biological or other technical intervention procedures.

### DTM.8:2 - Problem

A single label such as prevention, resistance or resilience can hide several causal changes. A decline in observed damage can result from fewer new contacts, less continuing activity, lower consequences of the same activity, or faster restoration after damage.

Treating these as interchangeable produces false completion claims. A local improvement can leave the source of harm to others unchanged, and a restriction that stops one activity can also prevent a needed contribution.

### DTM.8:3 - Forces

| Force | Tension |
| --- | --- |
| Prompt protection is valuable | The nearest available action may act on the wrong target. |
| Local consequences are visible | Continued transmission or costs to others may be missed. |
| Combining actions can help | Their effects and resource demands may interfere. |
| Restoration is desirable | Rebuilding the previous arrangement may be unnecessary or infeasible. |

### DTM.8:4 - Solution

**Identify the protected function, separate the intervention targets, follow their remaining effects and compare feasible combinations.**

#### DTM.8:4.1 - Restore the reference of protection

State which system or participant performs the relevant work, who receives its result, what adverse consequence is at issue and over what horizon. Use DTM.1 before treating an unfamiliar or dependent practice as harmful.

Ask separately about harm entering the considered system and harm its operation can impose on others. This directional contrast can help clarify a discussion of security and safety, but the two words have wider, context-dependent definitions. Accidental versus intentional action is another distinction; it does not follow from the direction.

A.6.P.RI restores the standpoint of the claim. A reduction in the operator's cost is not automatically a reduction in harm to a customer, neighboring group or constituent participant.

#### DTM.8:4.2 - Locate each proposed change

Follow the current account from encounter through established activity to consequence and restoration. Distinguish four target kinds:

| Target | What the action changes | What can remain |
| --- | --- | --- |
| Contact or admission | Opportunity to encounter, receive or establish the variant | Activity already established inside participants |
| Continuing activity | Amount, intensity or occurrence of the unwanted activity after establishment | Past damage, other sources and possible re-establishment |
| Consequence of activity | The effect on a specified function at comparable continuing activity | The activity and its potential for further transmission |
| Restoration | Recovery or replacement of an impaired function | The source of new impairment and continuing exposure |

These targets distinguish causal changes. Their quantities come from the subject practice: failed executions, unauthorized operations, incompatible exchanges or another specified event. There is no universal scalar “burden” shared by all these cases.

One action can affect several targets. Record those actual connections rather than giving it one exclusive label.

#### DTM.8:4.3 - Construct the change and its residual effects

For each feasible action, specify which relation in DTM.2/.3 or the subject model changes. Keep the comparison at the same recipient, horizon and relevant initial conditions.

For reduced contact, retain what happens in already affected participants. For reduced established activity, retain earlier consequences and possible return. For reduced consequence, check whether the variant can still be transmitted. For restoration, compare the restored function with the continuing rate of new impairment.

When a numerical model is warranted, vary the corresponding parameters or operations rather than replacing every protective action with a common reduction factor. MMP supplies the model change and analysis. DTM.4 examines persistence or return; DTM.9 includes response formation and indirect effects.

#### DTM.8:4.4 - Check implementation across the method vertical

Recover the component operations, resources and capabilities needed while the protective action is performed, and the larger work it is meant to sustain. C.32.MWA supplies this simultaneous method-vertical question.

For example, “exclude an unreliable procedure” requires an available way to distinguish it under relevant conditions, authority to change admission, and an alternative means to continue needed work. A hypothetical perfect distinction is a model assumption, not an implemented capability.

Use the existing development and operational methods to obtain missing contributions. Restoring a capability can use a different tool, partner or division of work; C.36.RP helps avoid equating cultural recovery with a return to the old arrangement.

#### DTM.8:4.5 - Compare combinations and the unchanged option

Pass the distinct outcomes, costs, uncertainties and feasibility conditions to the existing portfolio and decision methods. Retain the unchanged option and a smaller bounded change.

Check combinations for shared resource use and inconsistent assumptions. A result-checking operation can both stop faulty work and consume capacity needed for valid work. A repair activity can fail to catch up if new impairment continues faster than it restores function.

The first sufficient result may be a justified exclusion: “reducing new encounters alone cannot meet this deadline because the affected work is already installed.” A complete population model is unnecessary when that conclusion follows from the established causal account.

### DTM.8:5 - Archetypal Grounding

#### DTM.8:5.1 - Fewer contacts and fewer errors are different changes

Consider a hypothetical network in which 20 teams already use procedure B. Each performs 10 runs per week. Under the stated conditions, a run has probability 0.25 of producing an erroneous result. The expected number of new erroneous results is therefore 50 per week.

The following actions address different targets:

- Reducing recommendations may reduce new adopting teams. It does not by itself change the 200 weekly runs already performed.
- Stopping half of the established runs, with all other assumptions unchanged, reduces expected generated errors to 25 per week. The needed work those runs served must still be considered.
- An available independent review that catches 80% of generated errors before delivery reduces expected erroneous deliveries to 10 per week. It leaves 50 generated errors, consumes review effort and does not by itself change transmission of the procedure.
- Correcting earlier erroneous results reduces the unresolved stock. It does not by itself change the current rate of new errors.

Combining the halving of established runs with review of every remaining result leaves 100 runs, 25 expected generated errors and 5 expected erroneous deliveries per week. This requires capacity to review all 100 results at the stated performance without displacing other needed work. If capacity permits only 50 uniformly selected reviews, expected detections are 50×0.25×0.8=10, leaving 15 erroneous deliveries rather than 5. Use OPS to resolve that capacity question.

The error probability and review performance are assumptions for illustration, not empirical claims. If review changes future learning or recommendations, that additional feedback belongs in the model.

#### DTM.8:5.2 - The same unresolved stock can hide a different source

Let L be the expected number of unresolved erroneous results, e the expected arrival rate and r the resolution rate per unresolved result. Under the illustrative approximation L'=e−rL, the stationary stock is e/r.

At e=50 per week and r=1 per week, the stock is 50. Halving e or doubling r gives a stationary stock of 25, but through different actions. In the latter case 50 new erroneous results still arrive each week.

The approximation assumes the resolution capacity supports a rate proportional to L. If a fixed-capacity correction team becomes saturated, that assumption fails; an OPS model is needed. The equal stationary stocks do not establish equal cost, delay, external consequence or further spread.

#### DTM.8:5.3 - Protecting exchange without rejecting a useful new method

A group receives work represented in a new format. Restricting admission of incompatible records can preserve the current exchange function while also obstructing a useful method.

Possible changes include a verified adapter, a more informative compatibility check or a bounded migration of the receiving work. Their subject engineering methods establish whether exchange succeeds. DTM.2/.6 examine how compatibility affects adoption; DTM.9 becomes relevant if the checking response itself changes useful participation.

Calling the new format an infection would conceal the actual problem. Continuing the old arrangement, converting at the boundary and changing the arrangement are alternatives with different costs and consequences.

### DTM.8:6 - Bias-Annotation

“More protection” can sound preferable without identifying a target. It may instead impose a costly restriction while leaving the relevant source unchanged.

A second bias treats restoration as making the participant self-sufficient. The required result may be dependable access to a contribution, not possession of every underlying method.

### DTM.8:7 - Conformance Checklist

- Protection has a named function, recipient, comparison and horizon.
- Harm to the considered system and harm from its operation are not silently combined.
- Contact or admission, established activity, consequences and restoration are distinguished where they change the choice.
- Each proposed action changes an identified relation and retains material residual effects.
- Required recognition, authority, component operations and supporting capabilities are feasible or explicitly unresolved.
- Combinations are checked for resource conflicts and feedback; existing choice methods perform the comparison.

### DTM.8:8 - Common Anti-Patterns and How to Avoid Them

**Fewer new users means the established problem is gone.** Keep the already installed activity in the account.

**Less local damage means less transmission.** Recover the actual link; it may be unchanged or even increase.

**A successful repair ends the source.** Compare ongoing impairment with restoration.

**The model has a selective intervention, so we can implement it.** Establish the distinction, means and authority used by that intervention.

### DTM.8:9 - Consequences

Protective choices become comparable without pretending that they act in the same way. The method can reveal the need for a combination or a simpler sufficient action. It also exposes costs that a single protection score would conceal. Subject-specific feasibility and value judgements remain indispensable.

### DTM.8:10 - Rationale

The location of an intervention determines which relations it can change. Keeping the locations distinct prevents an improvement in one observed result from being mistaken for removal of every relevant cause. Connecting them to transmission and the method vertical makes the distinction useful beyond its biological origins.

### DTM.8:11 - SoTA-Echoing

[Medzhitov, Schneider and Soares, *Disease Tolerance as a Defense Strategy* (2012)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3564547/) are a historical source for distinguishing reduction of an agent's amount from reduction of its damaging consequences. This pattern adapts the causal distinction to named activities and functions; it does not equate disease tolerance with social tolerance.

[Tang, Mou and Xu, *Defense strategies for plant health: Disease resistance and tolerance* (2025)](https://academic.oup.com/plcell/article/37/8/koaf186/8215596) also distinguish protective effects from damage caused by the response. That distinction informs the comparison of residual effects and response costs in :4.3–.5; the receiving practice must establish the effects of its actual actions.

Compared with one generic suppression target, the four-target account can show why a locally successful action leaves spread or impaired function unresolved. Compared with a complete protection model, it can stop after the smallest relation sufficient to distinguish feasible choices. Existing subject methods establish intervention effects; existing decision methods compare their outcomes.

### DTM.8:12 - Relations

- **DTM.1** supplies the consequence comparison; **DTM.2/.3** locate transmission and established activity.
- **DTM.4** investigates persistence and return; **DTM.6** adds effects through other variants.
- **DTM.7** identifies a diversion point when relevant; **DTM.9** models the protective response and its feedback.
- **A.6.P.RI** restores the standpoint of protection; **C.32.MWA** recovers simultaneous method support.
- **C.36.RP** supports recovery through available cultural means; **MMP** and the existing portfolio methods retain modeling and choice.

### DTM.8:End

## DTM.9 - Model Damage and Feedback from Protective Responses to Continuing or Spreading Activity

**Type:** Method
**Status:** Stable

### DTM.9:1 - Problem frame

**Use this when** a protective response depends on the activity it encounters and, in turn, changes that activity, useful work or subsequent transmission.

A checking process may consume the capacity it protects. A rule triggered by visible use may restrict an easily recognized useful method more than a less visible faulty one. A learned warning may persist after conditions change. In each case, treating protection as a fixed beneficial reduction can reverse the predicted result.

Start by making the response itself part of the causal account. The first result is a conditional model of its formation, persistence, costs and differentiated effects, sufficient to compare the proposed change with a plausible alternative.

If a fixed external constraint has adequate subject evidence and its response dynamics do not matter to the receiving decision, retain that simpler model.

### DTM.9:2 - Problem

Protection is often represented only by how much it removes. That omits the process that produces the response, what it costs, which useful activity it restricts and how the remaining variants change its future conditions.

An immediate decrease can therefore coexist with later release of another variant, loss of useful work or persistent restriction after the initiating condition has disappeared. The protective action can become part of the problem without ceasing to have a protective effect.

### DTM.9:3 - Forces

| Force | Tension |
| --- | --- |
| Fast response limits consequences | Low-latency recognition may be less selective. |
| Memory avoids relearning | It can preserve an inappropriate response after conditions change. |
| Stronger restriction suppresses activity | It also changes resources and competition among remaining variants. |
| A compact model helps decisions | Eliminating response dynamics can hide delay, cost or hysteresis. |

### DTM.9:4 - Solution

**Model how the response is generated and sustained, how it acts on each relevant activity, and how those effects return to the conditions that generate it.**

#### DTM.9:4.1 - Identify the response and its information

Use DTM.8 to name the protected function and target. Recover what generates the response: an observed event, accumulated evidence, a prediction, a standing rule or a participant's judgement. Distinguish the actual condition from the signal used to recognize it.

Specify the operation that follows and the means needed to perform it. C.30.LCA supplies the relevant control relations; the technical or organizational practice supplies the detection and action method.

If recognition is uncertain, retain its consequential errors. An action that perfectly distinguishes useful and faulty variants is not available merely because the model assigns them different symbols.

#### DTM.9:4.2 - Choose the response state and time description

Represent formation, decay, persistence and capacity limits at the resolution needed by the question. A response may depend on current activity, past experience or prediction. Use a state or history sufficient to represent that dependence.

An algebraic response a=F(x,u) assumes that its adjustment is sufficiently fast for the receiving result, where x describes relevant activity and u the proposed change. A simple dynamic alternative is:

~~~text
τa' = F(x,u) − a, with τ > 0.
~~~

This illustrative first-order adjustment does not automatically represent learning, saturation or several kinds of memory. Introduce those relations only where supported. MMP.11/.18 govern the state choice and any reduction.

Test the simplification against the decision. A stationary comparison can tolerate a reduction that would be unsuitable for startup, short disturbances or a deadline. Even a fast response can matter when a brief transient crosses an irreversible boundary.

#### DTM.9:4.3 - Follow effects on useful work, unwanted activity and transmission

For every variant that can change the conclusion, recover how the response changes execution, continuation or uptake. Use the different sensitivities or action conditions supplied by the subject account.

Then follow indirect effects through the relations identified in DTM.6: released capacity, lost prerequisite capability, changed compatibility or a changed audience. Connect resulting participant states to transmission with DTM.3.

Do not add a common resource or a biological mechanism merely to complete a familiar model. A compatibility restriction may operate through exchange opportunities alone; a checking process may instead share scarce staff time with the work it checks.

#### DTM.9:4.4 - Account for response costs and restoration

Name each material consequence and its recipient. Direct effort, delayed useful work, inappropriate restrictions and external harm need not share a unit or a scalar total. A.6.P.RI and the existing evaluation methods retain those distinctions.

If a local consequence accumulates and can be repaired, represent both its source and restoration. DTM.8 distinguishes changing the source from repairing its result. State which other participants' consequences remain outside that local measure.

At the method vertical, verify that sensing, decision, action and restoration can operate together while supporting the containing work. A proposed response that consumes the only capacity needed for that work may be infeasible even if its isolated mechanism succeeds.

#### DTM.9:4.5 - Compare regimes, transients and changed variants

Compare the unchanged arrangement with the feasible response changes. Use DTM.4 for persistence and return, and the appropriate mathematical and computational methods for the calculation.

Where variants can change, examine a consequential alternative that differs in response sensitivity or continuation mechanism. Separate a possible variant from evidence that it will arise. DTM.2 supplies reconstruction or change; DTM.5/.6 explain differential continuation. Reuse the existing improvement and model-revision methods rather than adding an automatic escalation rule.

Return the condition under which the response helps, its adverse effects, sensitivity to uncertain relations and the observation that would change the choice. “Protection works” is too broad when the result holds only for one variant or one recipient.

### DTM.9:5 - Archetypal Grounding

#### DTM.9:5.1 - A broad response releases the variant it was meant to limit

Continue the illustrative activity model of DTM.6. A is useful execution and B is execution producing specified errors inside a group. Both occupy limited execution capacity. Suppose the checking response is generated more strongly by visible A activity and also by B:

~~~text
a = 2A + 0.5B + u
A' = A[2(1−A−B) − 0.2 − a]
B' = B[(1−A−B) − 0.3 − 0.2a − v].
~~~

Here u is additional broad checking and v selectively stops established B activity. A, B and remaining capacity are nonnegative. Time and activity are normalized; coefficients are chosen for this example. The equation for a assumes fast adjustment with no consequential memory.

With positive initial presence and the stated model, the stable stationary comparisons are:

| Condition | A | B | a |
| --- | ---: | ---: | ---: |
| No additional response: u=v=0 | 0.25556 | 0.31111 | 0.66667 |
| Broad response: u=0.4, v=0 | 0 | 0.56364 | 0.68182 |
| Selective action: u=0, v=0.3 | 0.45 | 0 | 0.90 |

Increasing broad checking removes the more sensitive A and releases capacity for B. The larger response therefore leaves more B. This conclusion follows from the stipulated resource and sensitivity relations; it is not an empirical claim about procedure catalogues or a general argument against checking.

Selective action succeeds here only if B can actually be distinguished and stopped at the assumed cost. It cannot be presented as an available improvement before that capability is established.

#### DTM.9:5.2 - A local consequence and further spread can move differently

Add an illustrative local consequence stock:

~~~text
L' = hB + 0.1a + 0.05v − rL.
~~~

L measures a specified local impairment in normalized units; h is its rate per unit B activity and r its restoration rate. The other terms represent local costs of response and selective checking. Useful A remains a separate result, and harm to outside recipients is not included.

With h=r=1, the three rows above give stationary L of approximately 0.37778, 0.63182 and 0.105. Broad checking worsens both useful activity and this local consequence. These results do not collapse all affected interests into L.

If groups share the same settled internal regime and between-group spread is slower, an illustrative coupling is z'=βBz(1−z)−γz, with z the fraction of groups in which B is established. At β=2 and γ=0.5, the positive stationary fractions are approximately 0.19643 for the baseline and 0.55645 for broad checking. The zero state remains invariant without an introduction.

Reducing h or increasing r can improve the local consequence without changing B and therefore without changing this spread law. Conversely, reducing β can stop continued spread while leaving the established internal activity untouched. DTM.8 explains the distinct intervention targets. If affected groups differ materially or are still learning, use DTM.3 to repair the coupling instead of inserting an unsupported average B.

#### DTM.9:5.3 - A successful restriction may leave another continuation route

In the selective-action regime, A=0.45 and a=0.9. Consider a hypothetical rare alternative B* that is unaffected by v and has response sensitivity 0.1 instead of 0.2. Its initial growth rate under the same resource account is:

~~~text
(1−0.45) − 0.3 − 0.1×0.9 = 0.16.
~~~

The positive value establishes a possible weakness of this intervention under those assumptions. It does not predict the appearance of B*, its frequency or an adversary's intention. The next question is whether that alternative has a plausible construction and whether a feasible observation or action addresses it.

A changed variant may also be more useful rather than more harmful. DTM.1 must establish its consequences afresh; inherited suspicion is not an evaluation.

#### DTM.9:5.4 - Memory can outlast the condition that formed it

Suppose a receiving team keeps restricting an exchange format because earlier versions caused failures. The present format and conversion method have changed, but the restriction uses accumulated historical evidence.

The response state must then distinguish current compatibility from retained evidence. A comparison of current verified exchange and the rule's update behavior can reveal whether the restriction still protects the intended work. A memory-free relation to current usage would miss that question.

For a small constructed case, let m be a retained warning score. The rule holds the format when m≥0.4, starts at m_0=0.8, and updates after an authorized exchange test by m_next=0.8m+0.2e, where e=1 for a failed test and 0 for a successful one. Four successful tests give scores 0.64, 0.512, 0.4096 and 0.32768. The rule therefore still holds the format after the first three tests and releases it after the fourth, although the latest observed outcome is the same throughout.

A rule based only on the latest outcome would release it after the first success. Neither rule is justified by this arithmetic alone: the subject engineering method must establish which exchanges were tested and what evidence warrants admission. If the restriction also prevents every new test and the score has no other update, m remains 0.8 and the restriction sustains its own lack of new evidence.

The subject control and learning methods define how evidence is updated.

### DTM.9:6 - Bias-Annotation

A protective label can hide the response's own consequences. Include useful work and affected recipients alongside the suppressed activity.

The opposite bias treats any costly response as unjustified. A response may remain preferable to the consequences it prevents; the comparison, conditions and alternatives determine that judgement.

### DTM.9:7 - Conformance Checklist

- The response's initiating information and performed operation are identified.
- Formation, decay, memory and time reduction match the receiving question.
- Consequential recognition errors and different effects on variants remain visible.
- Direct costs and indirect effects on capacity, useful work and transmission are traced.
- Local consequence measures do not silently stand for every recipient's welfare.
- A selective action has an implementable distinction or remains a conditional alternative.
- Possible variant change is not reported as observed or inevitable change.
- The result states conditions and return observations, rather than recommending indiscriminate escalation.

### DTM.9:8 - Common Anti-Patterns and How to Avoid Them

**A stronger response is a stronger solution.** Follow useful work and indirect release of other variants.

**The equilibrium settles a deadline question.** Restore response time and the relevant transient.

**A perfect classifier is a harmless simplifying assumption.** Test whether its errors and implementation cost could reverse the chosen action.

**The first successful restriction is permanent.** Revisit the continuation mechanism when conditions or variants change.

### DTM.9:9 - Consequences

The model can expose protective actions that worsen the stated outcome and identify when a narrower or differently timed response could help. It also makes uncertainty costly in a visible way: lacking a reliable distinction may rule out the apparently best action. Added dynamics are worthwhile only when they change a consequential comparison.

### DTM.9:10 - Rationale

A response belongs inside the model when it is produced by, and changes, the modeled activity. This closes a feedback relation that fixed suppression misses. Treating the response as an ordinary process with state, limits and consequences also prevents its protective purpose from being mistaken for proof of its effect.

### DTM.9:11 - SoTA-Echoing

[Ramesh and Hall (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12203456/) examine competition with shared resources and responses in a biological setting. Their distinction between a variant's effect on a limiting factor and its sensitivity to that factor informs :4.3 and :5.1: the same response can restrict the variants differently while their activity changes its formation. The engineering example uses stipulated coefficients; it does not reproduce the biological model.

[Zilio et al. (2026)](https://doi.org/10.1016/j.tree.2025.12.002) reinforce the need to distinguish interaction routes across scales. A changed local interaction therefore needs a stated connection to transmission, rather than an assumed population benefit.

Compared with a fixed suppression term, an endogenous response can reveal costs, differential sensitivity and memory. Compared with an unrestricted multi-process simulation, the method adds only relations that can change the receiving decision. MMP.18 supplies the reduction test, C.30.LCA the control distinctions and the subject practice the realizable response.

### DTM.9:12 - Relations

- **DTM.6** supplies the interaction relation; **DTM.7** supplies a possible diversion point.
- **DTM.8** distinguishes action targets before their response dynamics are compared.
- **DTM.2/.3/.4** connect change, spread and persistence; **DTM.5** distinguishes levels of continuation.
- **MMP.11/.16/.18** provide state construction, discriminating evidence and justified coupling or reduction.
- **C.30.LCA**, **C.32.MWA** and **A.6.P.RI** retain control, simultaneous method support and reference distinctions.

### DTM.9:End
