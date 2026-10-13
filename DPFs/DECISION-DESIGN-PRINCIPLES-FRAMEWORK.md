# Decision Design Principles Framework

**DocID:** `PSDA` within **FPF Library**.

A domain pattern language for constructing problem formulations, decision alternatives and models, and qualifying their interpretation and use in bounded inquiry, including professional participation and advice.

Anatoly Levenchuk, with AI-assisted development. [Working edition, 12 October 2026](#psdasources2---citation-and-limits). Original and adapted framework text: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Third-party sources retain their own terms.

Bring the missing result: a useful formulation, model, alternative, comparison, participation arrangement or qualified return. Use an adequate current answer directly. The Readme gives independent entries; the Architectural Reference explains their connections and limits. Complete patterns carry the operations, cases and source comparisons. One inquiry need not use the whole repertoire.

# Table of Contents

| Public unit | Reader use |
| --- | --- |
| [Readme](#readme) | Recognize a first useful result and its sufficient stop. |
| [Decision Design Principles Framework Architectural Reference](#decision-design-principles-framework-architectural-reference) | Understand the field, connected Methods, professional conditions and alternatives. |
| [PSDA.Reference:1](#psdareference1---the-field-and-its-useful-result) | The field and its useful result |
| [PSDA.Reference:2](#psdareference2---how-the-constructions-connect) | How the constructions connect |
| [PSDA.Reference:2.1](#psdareference21---do-we-need-a-model-an-explanation-research-or-advice) | Do we need a model, an explanation, research or advice? |
| [PSDA.Reference:3](#psdareference3---formulation-professional-support-and-choice) | Formulation, professional support and choice |
| [PSDA.Reference:4](#psdareference4---qualify-the-result-and-its-combination) | Qualify the result and its combination |
| [PSDA.Reference:5](#psdareference5---why-retain-this-connected-language) | Why retain this connected language |
| [PSDA.Reference:5.1](#psdareference51---the-development-direction-profile-and-neighboring-results) | The development-direction profile and neighboring results |
| [PSDA.Reference:5.2](#psdareference52---why-the-source-lines-are-combined) | Why the source lines are combined |
| [PSDA.Reference:5.3](#psdareference53---decision-theory-model-construction-and-engineering-trade-studies) | Decision theory, model construction and engineering trade studies |
| [PSDA.Reference:5.4](#psdareference54---one-bounded-language-and-its-wider-connections) | One bounded language and its wider connections |
| [PSDA.Reference:6](#psdareference6---continue-and-change-the-practice) | Continue and change the practice |
| [PSDA.Reference:7](#psdareference7---whose-conditions-and-evidence-shape-the-answer) | Whose conditions and evidence shape the answer |
| [PSDA.Reference:8](#psdareference8---questions-before-relying-on-a-combined-return) | Questions before relying on a combined return |
| [PSDA.Reference:9](#psdareference9---direct-neighboring-contributions) | Direct neighboring contributions |
| [PSDA.Reference:10](#psdareference10---what-this-framework-covers) | What this framework covers |
| [PSDA.Reference:11](#psdareference11---change-only-what-the-new-basis-changes) | Change only what the new basis changes |
| [PSDA.Reference:12](#psdareference12---obtain-the-result-needed-for-the-developing-subject) | Obtain the result needed for the developing subject |
| [PSDA.Reference:13](#psdareference13---keep-source-changes-and-case-changes-distinct) | Keep source changes and case changes distinct |
| [PSDA.Reference:14](#psdareference14---direct-frameworks-predecessor-sources-and-honest-omissions) | Direct frameworks, predecessor sources, and honest omissions |
| [PSDA.Reference:15](#psdareference15---development-direction-advising-within-a-wider-undertaking) | Development-direction advising within a wider undertaking |
| [PSDA.Sources:1](#psdasources1---source-arguments-and-refresh) | Source arguments and refresh |
| [PSDA.Sources:2](#psdasources2---citation-and-limits) | Citation and limits |
| [PSDA.Sources:3](#psdasources3---source-responsibility-and-references) | Source responsibility and references |
| [PSDA.Sources:4](#psdasources4---source-access-for-the-development-applications) | Source access for the development applications |
| [PSDA.Sources:4.1](#psdasources41---learning-product-source-access) | Learning Product source access |
| [PSDA.Sources:4.2](#psdasources42---foundations-programme-source-access) | Foundations programme source access |
| [PSDA.Sources:4.3](#psdasources43---predecessor-source-account-access) | Predecessor source-account access |
| [PSDA.Sources:4.4](#psdasources44---a-useful-stop-when-access-is-incomplete) | A useful stop when access is incomplete |
| [PSDA.Sources:5](#psdasources5---source-grounds-for-the-development-applications-and-their-suppliers) | Source grounds for the development applications and their suppliers |
| [PSDA.Sources:5.1](#psdasources51---opportunity-characterization-and-retained-possibilities) | Opportunity, characterization, and retained possibilities |
| [PSDA.Sources:5.2](#psdasources52---professional-and-ai-source-qualification) | Professional and AI-source qualification |
| [Development-direction advising](#development-direction-advising) | Follow the conditional profile with its distinct subject and service conditions. |
| [Cross-pattern applications](#cross-pattern-applications) | Follow complete investment, development, inquiry and non-person cases. |
| [Decision Design Principles Framework Sources and Edition Notes](#decision-design-principles-framework-sources-and-edition-notes) | Recover source arguments, specialist returns, citation and changed-use conditions. |

## Pattern index

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| --- | --- | --- | --- | --- |
| 1 | [PSDA.1 - Generate Plural Problem Formulations](#psda1---generate-plural-problem-formulations) | Stable | formulation, framing, rival accounts. Which materially different formulations change what to investigate? | Relevant inquiry inputs; FPF and subject Methods under their conditions; PSDA.12, PSDA.13 for professional participation when needed. |
| 2 | [PSDA.2 - Set and Reopen the Problem Boundary](#psda2---set-and-reopen-the-problem-boundary) | Stable | boundary, scope, exclusions. What must the inquiry include, and what would reopen its cut? | Relevant inquiry inputs; FPF and subject Methods under their conditions; PSDA.12, PSDA.13 for professional participation when needed. |
| 3 | [PSDA.3 - Construct Complementary Situation and Option Models](#psda3---construct-complementary-situation-and-option-models) | Stable | models, claims, assumptions, losses. Which complementary models answer the question without hiding their differences? | Relevant inquiry inputs; FPF and subject Methods under their conditions; PSDA.12, PSDA.13 for professional participation when needed. |
| 4 | [PSDA.4 - Select Problem-Structuring Methods and Combine Them When Needed](#psda4---select-problem-structuring-methods-and-combine-them-when-needed) | Stable | PSM, combination, fit. Which problem-structuring and analytical ways supply the missing result? | Relevant inquiry inputs; FPF and subject Methods under their conditions; PSDA.12, PSDA.13 for professional participation when needed. |
| 5 | [PSDA.5 - Generate Decision Alternatives](#psda5---generate-decision-alternatives) | Stable | alternatives, mechanisms, incumbent. Which complete decision alternatives differ usefully? | Relevant inquiry inputs; FPF and subject Methods under their conditions; PSDA.12, PSDA.13 for professional participation when needed. |
| 6 | [PSDA.6 - Represent Values and Trade-Offs](#psda6---represent-values-and-trade-offs) | Stable | values, objectives, trade-offs. What matters, and what must not be compensated away? | Relevant inquiry inputs; FPF and subject Methods under their conditions; PSDA.12, PSDA.13 for professional participation when needed. |
| 7 | [PSDA.7 - Represent Decision-Relevant Uncertainty and Evidence Limits](#psda7---represent-decision-relevant-uncertainty-and-evidence-limits) | Stable | uncertainty, evidence, scenarios. Which unknown can change the comparison? | Relevant inquiry inputs; FPF and subject Methods under their conditions; PSDA.12, PSDA.13 for professional participation when needed. |
| 8 | [PSDA.8 - Compare Consequences of Decision Alternatives](#psda8---compare-consequences-of-decision-alternatives) | Stable | consequences, comparison, partial order. What follows under the same conditions and declared rule? | Relevant inquiry inputs; FPF and subject Methods under their conditions; PSDA.12, PSDA.13 for professional participation when needed. |
| 9 | [PSDA.9 - Test Robustness and Sensitivity of Decision Alternatives and Their Comparison](#psda9---test-robustness-and-sensitivity-of-decision-alternatives-and-their-comparison) | Stable | robustness, sensitivity, reversal. Where does the conclusion hold or reverse? | Relevant inquiry inputs; FPF and subject Methods under their conditions; PSDA.12, PSDA.13 for professional participation when needed. |
| 10 | [PSDA.11 - Bound the Decision-Support Engagement and Authority Boundary](#psda11---bound-the-decision-support-engagement-and-authority-boundary) | Stable | engagement, authority, recipient. What advice is needed, for whom, and who makes the later choice? | FPF A.15.9, A.10, C.11; PSDA.12, PSDA.1, PSDA.2 when participation, formulations or scope remain live. |
| 11 | [PSDA.12 - Recover Participants, Concerns, and Affected Systems for a Decision-Support Inquiry](#psda12---recover-participants-concerns-and-affected-systems-for-a-decision-support-inquiry) | Stable | participants, concerns, affected Systems. Whose consequential concern or absence could change the inquiry? | Uses the bounded PSDA.11 question; FPF A.1.CSD for consequence-bearer discovery. |
| 12 | [PSDA.13 - Facilitate Decision-Support Inquiry and Preserve Material Dissent](#psda13---facilitate-decision-support-inquiry-and-preserve-material-dissent) | Stable | facilitation, attribution, meaning, dissent. What can participants recognize and what remains materially contested? | PSDA.12, PSDA.1, PSDA.2 when live; FPF A.2.9; specialist truth and authority remain direct returns. |
| 13 | [PSDA.14 - Prepare and Return a Decision-Support Recommendation](#psda14---prepare-and-return-a-decision-support-recommendation) | Stable | recommendation, retained set, request, blocker, abstention. What can responsibly be returned now without taking the choice? | PSDA.11 and the qualified contributing PSDA.5, PSDA.6, PSDA.7, PSDA.8, PSDA.9 results; FPF A.15.9, A.10 and C.11. |
| 14 | [PSDA.15 - Arrange Decision Follow-up or Reassess Advice After a Change](#psda15---arrange-decision-follow-up-or-reassess-advice-after-a-change) | Stable | follow-up, observation, interpretation, change. Which relied-on premise changed, and which advice must be reconsidered? | PSDA.14 when recommendation follow-up is live; FPF A.10 for one known reliance; A.10.1 when a changed source requires discovering and revalidating several uses; G.11 for currentness; direct subject or service guidance for its own question. |
| 15 | [PSDA.16 - Decide Whether and How to Change Problem-Structuring and Decision-Support Methods](#psda16---decide-whether-and-how-to-change-problem-structuring-and-decision-support-methods) | Stable | Method repertoire, fit, evidence, source refresh. Which offering should be retained, changed, tested or retired? | PSDA.4 and actual follow-up evidence; direct Method-engineering and evidence results when required. |
| 16 | [PSDA.17 - Reconcile Simultaneous Problem-Structuring and Decision-Support Work](#psda17---reconcile-simultaneous-problem-structuring-and-decision-support-work) | Stable | simultaneous inquiry, coupling, interference, facilitation. Which arrangement preserves a threatened result at acceptable burden? | PSDA.3, PSDA.4, PSDA.13 where their contributions interact; FPF C.32.MWA for needed several-structure synthesis. |
| 17 | [PSDA.18 - Deliberately Continue and Change Problem-Structuring and Decision-Support Culture](#psda18---deliberately-continue-and-change-problem-structuring-and-decision-support-culture) | Stable | cultural continuation, interpretation, retention, mediation. What changes across practitioners beyond publication or local performance? | PSDA.16 and PSDA.17 when current; FPF C.20 and C.36 for their direct cultural claims. |
| 18 | [PSDA.19 - Bound the Development-Direction Advising Engagement](#psda19---bound-the-development-direction-advising-engagement) | Stable | development advice, recipient, service scope, holder premises, refusal. What can responsibly be recommended for this recipient? | PSDA.11, PSDA.14; qualified PSDA results; actual subject practice and professional service conditions. |

# Readme

## Start with the missing result

Two people can use the same word for different problems; two models can answer different questions despite displaying the same measure. PSDA.1 and PSDA.2 make the formulation and boundary examinable. PSDA.3 constructs complementary model claims. A clear question with adequate models needs none of that work again: it can enter directly at an alternative, value, uncertainty or comparison result.

When familiar proposals cannot obtain a desired consequence, start with [PSDA.5](#psda5---generate-decision-alternatives). Its constructive return through PSDA.6 and PSDA.8 helps build a different combination of means and test it under the same conditions.

If the proposed intervention is already familiar but its value is disputed, PSDA.6 separates attributed concerns, protected conditions and compensating trade-offs. PSDA.8 compares consequences only under a declared rule. PSDA.9 tests where the conclusion holds or reverses. A retained set or bounded conditional comparison can be the complete answer; the authorized chooser makes the later choice.

If a discussion contains reports and opinions but no usable conclusion, B.5.SD constructs the missing inference with competent contributors. Professional facilitation can supply the participation conditions through PSDA.13. It may also supply the subject integration when the facilitator has that competence. A clear direct explanation needs no meeting.

An assisting agent can explain or apply these Methods in ordinary language. Ask for the actual objects, differences, grounds and next useful action, rather than a list of framework names.

## A comparison can be correct and still answer too little

Consider a constructed inquiry about a pumping arrangement. One formulation concerns rated capacity; another concerns access to assistance when roads fail. The second changes the boundary and model question. A capacity model does not establish that people can reach help or that a mobile pump can be deployed. PSDA.1–3 preserve those differences before a comparison is used.

For an illustrative analytical slice, fixed pumps have losses 2 with normal roads and 3 with road access lost, at cost 8. Mobile pumps have corresponding losses 1 and 9, at cost 5. With assumed road-loss probability `p` and cost weight `λ`, lower-is-better scores are `2 + p + 8λ` and `1 + 8p + 5λ`. Fixed pumps score lower when `7p > 1 + 3λ`. At `λ = 0.5`, the mobile score is lower for `p = 0.2`, but the fixed score is lower for `p = 0.6`.

PSDA.6 keeps the assumed trade-off distinct from protected service conditions. PSDA.7 keeps the missing probability basis visible. PSDA.8 supplies the conditional comparison and PSDA.9 exposes its reversal. Neither assumed input is established by this arithmetic. The incumbent and a staged direction may also remain live outside this two-option slice. A whole-investment recommendation therefore requires additional qualified premises or a narrower return.

Now suppose deployment is unavailable in the required window. The mobile branch loses its applicability; inserting a convenient probability cannot repair it. The fixed-option arithmetic remains valid at its stated scope. A professional adviser uses PSDA.14 to return what the recipient can rely on, while the governing decision remains separate. An analyst studying the relation for understanding can instead stop with the bounded model result.

## Practical entries

Bring the question that is blocking useful work. The examples below show how professional support uses intellectual inquiry and returns a qualified answer, and how a changed premise can send that use back. They are not a catalogue or a required sequence. Use the pattern index or search when another question is live; an adequate direct result can finish the task. The [Architectural Reference](#decision-design-principles-framework-architectural-reference) and its [Architectural Rationale](#psdareference5---why-retain-this-connected-language) explain how the contributions fit together. You can ask an assisting agent: “Explain this and give me your comments in ordinary language, without framework jargon.”

If the useful future contribution itself is still unclear, use the general [C.40.OCN opportunity construction (FPF C.40.OCN:1)](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c40ocn1---problem-frame) directly. You can construct an opportunity and stop at its next question without appointing an adviser. When a distinct performer must recommend a development direction to a recipient, use the [advising profile](#development-direction-advising) or the second example below.

### PSDA-CARD-01 — Turn a contested situation into a usable recommendation

- **Situation:** A municipal committee needs advice on a pre-season pumping arrangement. Operations staff emphasize capacity, residents raise unequal protection, and responders question safe access and deployment.
- **Question:** What can the inquiry recommend while preserving those differences and the committee's investment authority?
- **First useful result or blocker:** Attributed formulations and a usable inquiry boundary; then a conditional comparison whose omissions remain visible in the recommendation.
- **Start with:** [PSDA.11](#psda11---bound-the-decision-support-engagement-and-authority-boundary) for the receiving question and authority boundary. If these are adequate, enter at the missing participation, formulation, model or comparison result.
- **Stop or return:** Return the supported advice or its limitation through `PSDA.14`. Reopen the dependent model, alternative, scope or recommendation when a material concern or premise changes. The committee retains the later choice.

The constructed [flood-pump application](#psdaapplication1---app-psd-01--a-flood-pump-calculation-is-not-the-whole-investment-answer) begins with an independent inquiry team preparing a return for the committee. `PSDA.12` discovers affected people and concerns beyond those able to attend. `PSDA.1` preserves different formulations: insufficient capacity, unequal protection, fragile maintenance and unsafe deployment. Their consequences inform the `PSDA.2` boundary: compare the pre-season pumping arrangements while keeping material downstream effects and mobility constraints visible. Long-term relocation remains outside this inquiry.

That boundary changes the modeling question. `PSDA.3` keeps nominal pumping capacity separate from whether people can reach assistance and whether a mobile pump can arrive when roads fail. `PSDA.4` compares a capacity-only calculation with a bounded combination of attributed inquiry and conditional technical analysis. The combination is useful only if its contributions can be obtained and their subjects, conditions and meanings can be joined. `PSDA.13` lets participants correct the claim “the pumps protect the district”: a capacity result does not answer the separate access question. A concern map supplies questions for comparison, not numerical weights.

`PSDA.5` retains the current arrangement, fixed pumps, mobile pumps and a still-incomplete staged direction. The following slice compares only fixed and mobile pumps. Its loss and cost figures are illustrative units, not measured impacts or a complete investment account.

| Alternative | Loss with normal roads | Loss with road access lost | Cost |
| --- | ---: | ---: | ---: |
| Fixed pumps | 2 | 3 | 8 |
| Mobile pumps | 1 | 9 | 5 |

With an assumed road-loss probability `p` and cost weight `λ`, the illustrative lower-is-better scores are `2 + p + 8λ` and `1 + 8p + 5λ`. `PSDA.6` keeps the trade-off premise separate from protected conditions; its §4.5 constructs compatible preferences when the exchange still needs elicitation, with a deterministic worked case in §5.5. `PSDA.7` retains the missing basis for `p` and the uncertainty conditions needed here. `PSDA.8` supplies the comparison, and `PSDA.9` exposes its reversal: fixed pumps score lower when `7p > 1 + 3λ`. At `λ = 0.5`, mobile pumps score lower for `p = 0.2`, but fixed pumps do for `p = 0.6`. Neither input is established for the committee's decision by this calculation.

The `PSDA.14` return therefore retains the conditional comparison while withholding a whole-investment ranking. Access, assistance and protection conditions remain unqualified; the baseline and staged direction were not disposed of by the two-row calculation. A further result is requested through `A.15.9` only if its obtainable contribution warrants the burden. Even resolving road access would not by itself settle the value trade-off.

Suppose the committee authorizes a study, and a qualified source then establishes that mobile deployment is unavailable during the required window. `PSDA.15` returns to the mobile alternative and its consequence premises; this is not a reason to insert a convenient value of `p`. Preserve the earlier conditional calculation as such, but do not use it as the current investment basis. If a newly affected group reveals an omitted consequence, return to the boundary as well. Study authorization still leaves pump procurement to its own decision.

### PSDA-CARD-02 — Recommend a development direction without taking the choice

- **Situation:** A separate advisory team must recommend a ninety-day reliability direction for a service organization: internal development, an external provider or a mixed human–AI arrangement.
- **Question:** Which direction or information-gaining step do the available premises support, and which claims remain conditional?
- **First useful result or blocker:** A retained set with its comparison limit, or a supported direction or bounded probe recommendation when the missing premises become available.
- **Start with:** `PSDA.11` for the engagement; then use `PSDA.5`, `PSDA.6`, `PSDA.7`, `PSDA.8`, `PSDA.9`, `PSDA.14` at the first missing result. The [profile](#development-direction-advising) and [development-direction application](#psdaapplication2---app-psd-02--development-direction-advice-with-unlike-holder-premises) supply the connected account and its other holder cases.
- **Stop or return:** Give the supported advice with its material limits. Use `PSDA.15` for a real changed-premise or follow-up question, preserving independent claims. The authorized chooser decides whether to commit or probe.

In the constructed organization case, the committee has the stated mandate, and the advisory service's competence, confidentiality and conflict conditions are met. Reliability takes priority over throughput; security, critical-service continuity and a bounded probe budget are protected. The operating account identifies the recovery contribution, an interface account describes the current arrangement, and a priority statement supplies the receiving value. These inputs help define the `PSDA.5` alternatives, but none compares all three whole arrangements.

The first `PSDA.14` return retains internal development, the provider and the mixed arrangement, and states that their whole-arrangement comparison is missing for this recovery result and horizon. Inspect an adequate existing specialist result before commissioning another. Through the profile's `A.15.9` return, request the bounded comparison only when its attainable contribution warrants the complete acquisition burden. The supplier chooses how to produce its result; the adviser retains the recommendation question.

Now add qualified arrangement and security results that cover all three directions. They exclude the specified provider because it cannot preserve the security boundary; internal development remains feasible. A separately qualified probe proposal specifies the remaining question, distinguishing observations, feasible resources, exposure and stops. Compared with immediate commitment, it supports obtaining that information at bounded cost. Using the needed value, uncertainty, consequence and robustness results from `PSDA.6`, `PSDA.7`, `PSDA.8`, `PSDA.9`, `PSDA.14` can recommend considering that probe first while retaining internal development. Those additional premises support the stronger return. They establish neither a throughput effect nor permission to perform the probe.

For a later probe of AI configuration A, `PSDA.15` needs a viable arrangement: an owner can report material changes, competent suppliers can interpret them, and the committee can receive the consequence in time. If observations now concern configuration B while the evaluation still covers A, block advice to extend or deploy B pending the premises needed for that use. Keep the earlier advice about A and an independently supported internal-development claim. An observation notice does not itself choose an operational fallback or revoke permission.

The human branch makes a different missing premise visible. An engineer considering evidence review and interface coordination may have permitted access to review material, yet lack a basis for independent capability and transfer; coordination practice and feedback may also be unavailable. Retain the conditional opportunities. Neither course attendance nor the organization's arrangement comparison supplies those human development results.

### PSDA-ENTRY-03 — Find what is wrong when the report is on time

- **Situation:** Weekly reports arrive on time, yet the planner must telephone colleagues to recover identifiers before using them.
- **Question:** Is the difficulty incomplete information, incompatible identifiers, an unsuitable deadline, or a misleading record?
- **First useful result or blocker:** Distinct formulations with an observation that could separate them, or the exact missing fact that prevents stating what is wrong.
- **Start with:** [PSDA.1](#psda1---generate-plural-problem-formulations) to compare the formulations. If the discrepancy is already understood and only a recording correction is needed, make that correction through the responsible practice.
- **Stop or return:** Stop when the formulation and available facts suffice for the current question. Open a causal-model question only when different explanations change the next useful action; return to the formulation if a check changes what was actually wrong.

The [report-handoff application](#psdaapplication3---app-psd-03--an-on-time-report-that-cannot-yet-be-used) follows that conditional continuation: causal alternatives can inform a bounded answer, while missing evidence, a recipient's objection or later observations can change it. A diagnostic check, temporary operational help and research answer different questions and may occur at the same time.

# Decision Design Principles Framework Architectural Reference

A useful answer can be smaller than the question that first brought people together. “Which pump should we buy?” may first need a distinction between a pump's rated capacity and whether assistance can actually reach the affected people. “What should we develop next?” may first need a worthwhile future contribution rather than a training plan or a model upgrade. Decision Design helps a recipient obtain and use those distinctions without claiming that one discussion, model or recommendation settles the whole situation.

The framework serves practitioners and assisting agents who construct formulations and decision models or arrange a professional engagement, obtain suitable inquiry and analysis, preserve participation conditions and return qualified advice. They may be internal analysts, facilitators working with affected groups, or professionals advising another person or organization. A team can investigate a question for its own later decision while keeping the analysis and choice distinct. The development-direction advising profile adds a distinct recommending performer where that service relationship is the question.

This language also supports the maintenance of the Methods and working arrangements that make this work dependable. Its pattern language offers a repertoire for recurring difficulties. The complete Methods address those difficulties; pattern numbers are addresses, and an actual inquiry selects contributions by the results it needs.

## PSDA.Reference:1 - The field and its useful result

Decision Design constructs inspectable formulations and representations of situations, possible actions, values, uncertainty and consequences. Its characteristic work is to make a difficult question investigable, construct possible responses and the models needed to examine them, and build a warranted comparison where the premises permit one. Its result can be an interpretation, model-use account, alternative set, partial comparison, robustness region or connected answer. These results can complete an inquiry for understanding or contribute to a professional engagement. Arranging participation, composing qualified advice and reconsidering it are parts of the same practice when the receiving use needs them; an external adviser or final choice is not required in every inquiry.

The language does not promise every form of thinking. Mathematical proof, physical explanation, causal identification, research, literary interpretation and engineering design retain their subject Methods. PSDA.11–.15 supply professional engagement, participation, advice and follow-up when needed; the owning practice supplies implementation. Leadership develops feasible joint contributions.

A *pattern* describes a recurring difficulty and a useful way to respond. A *Method* is a reusable way of doing the work; a workshop appointment, diagram or software package is not that way merely because it carries a familiar name. Open the pattern that can change the current answer. If an adequate result already exists, use it within its conditions instead of restarting the inquiry.

Some questions are contested. People can disagree about what is wrong, who bears a consequence, what counts as useful service or which evidence should matter. Preserve differences that change action. Making them explicit does not require every position to have equal evidential support, and a shared sentence does not establish unanimous endorsement.

Other questions are already sufficiently formed. They can enter directly at a missing alternative, specialist premise, comparison or recommendation. A person exploring an opportunity can stop even earlier, without asking another performer for advice.

## PSDA.Reference:2 - How the constructions connect

PSDA.1 develops materially different formulations. Their differences identify evidence needs, intervention mechanisms and consequences a single opening story can hide. PSDA.2 selects and reopens a usable boundary. PSDA.3 constructs complementary models whose claims and omissions fit the question. A model can expose a boundary error, and a changed formulation can make an earlier model unnecessary.

PSDA.4 selects the problem-structuring and analytical Methods that supply the missing contributions. It compares a familiar adequate Method with a combination and qualifies the meaning and conditions of the joins. Combination costs preparation and interpretation; a list of respected techniques supplies no whole Method. Professional participation and facilitation remain direct PSDA.12, PSDA.13 contributions where they are needed.

PSDA.5 constructs a live alternative set. PSDA.6 represents values without inferring weights from the frequency of concerns. When the known menu misses a desired consequence, PSDA.6:4.2 distinguishes ends from proposed means, and PSDA.8:4.2.1 can construct a new means combination backward from the desired conditions and test it forward before returning it to PSDA.5. PSDA.7 connects uncertainty to a claim that could change. PSDA.8 compares consequences under the declared rule, and PSDA.9 examines justified variations and reversals. Their results feed back: a robustness gap can require one missing observation; an omitted consequence can reopen the model or alternative without restarting everything.

B.5.SD makes the connection between supplied claims and the receiving answer itself a working object. This Core Method can use the relevant formulation, model, analytical or professional contribution when it is missing. A source-supported explanation, a proposed experiment and a recommendation have different completion conditions. Construct and examine the inference using the relevant subject Methods and grounds.

These are result dependencies and conditional uses, not eighteen compulsory phases. Pattern numbers identify full Methods. The same occasion may enact several Methods, but a claim that they form one composite Method needs explicit whole action, parts, joins and permitted variation under PSDA.4 and FPF B.1.5.

In a professional engagement, formulation and model construction can change which question is worth answering, whose consequences are considered, what counts as the problem and which interventions become plausible. Decision support uses suitably qualified formulations, alternatives, value accounts and evidence to help a receiving decision. A problem formulation can be a complete useful return before a recommendation is possible; a well-formed question can also enter comparison directly.

[PSDA.11](#psda11---bound-the-decision-support-engagement-and-authority-boundary) establishes the receiving use when that use is unclear. [PSDA.12](#psda12---recover-participants-concerns-and-affected-systems-for-a-decision-support-inquiry) supplies attributed concerns and participation limits, while [PSDA.1](#psda1---generate-plural-problem-formulations) shows how rival formulations change evidence needs, boundaries and possible responses. [PSDA.2](#psda2---set-and-reopen-the-problem-boundary) uses the needed engagement and participation results directly, alongside the formulations, to choose a usable inquiry boundary. A formulation alone cannot establish who receives the result or whether an affected person's concern has been represented adequately.

Within that boundary, a model can answer one question and expose another. [PSDA.3](#psda3---construct-complementary-situation-and-option-models) makes the contributions and limits of complementary models usable. [PSDA.4](#psda4---select-problem-structuring-methods-and-combine-them-when-needed) compares the ways of obtaining the needed results and qualifies any combination. [PSDA.13](#psda13---facilitate-decision-support-inquiry-and-preserve-material-dissent) helps participants examine the developing meanings and return shared and contested claims. A corrected concern can therefore change a model or reopen the boundary while independent analysis continues. [PSDA.17](#psda17---reconcile-simultaneous-problem-structuring-and-decision-support-work) becomes useful when the actual interaction between these activities threatens their results.

Formulations and models inform the alternative construction in [PSDA.5](#psda5---generate-decision-alternatives). A consequential difference may then need a value account from [PSDA.6](#psda6---represent-values-and-trade-offs), an uncertainty account from [PSDA.7](#psda7---represent-decision-relevant-uncertainty-and-evidence-limits), a consequence comparison from [PSDA.8](#psda8---compare-consequences-of-decision-alternatives), or the conditions under which a comparison holds or reverses from [PSDA.9](#psda9---test-robustness-and-sensitivity-of-decision-alternatives-and-their-comparison). Obtain only the result that is missing. For example, a sensitivity result can expose a missing road-access premise without requiring another round of alternative generation. A new service concern that the option set cannot address gives a reason to revisit that set or its formulation.

[PSDA.14](#psda14---prepare-and-return-a-decision-support-recommendation) connects the qualified inputs to what the recipient can use now: a direction, a retained set, a conditional comparison, a probe, a request or an abstention with its reason. [PSDA.15](#psda15---arrange-decision-follow-up-or-reassess-advice-after-a-change) connects a material later observation to the advice it can change when follow-up is needed. Neither relation requires performing all preceding patterns. The full [flood-pump application](#psdaapplication1---app-psd-01--a-flood-pump-calculation-is-not-the-whole-investment-answer) shows the connections, including a useful first engagement question and a later whole-investment blocker.

### PSDA.Reference:2.1 - Do we need a model, an explanation, research or advice?

Identify what the recipient lacks. These contributions can be used together, but their completion conditions differ.

| Missing contribution | Useful return and supplying Method |
| --- | --- |
| A representation that makes a relationship inspectable | [PSDA.3](https://github.com/ailev/FPF/blob/main/DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md#psda3---construct-complementary-situation-and-option-models) constructs models for named questions and reconciles only their supported overlaps. A model can expose an unknown without settling it. |
| An answer already available in sources | [RMP.1:4.3](https://github.com/ailev/FPF/blob/main/DPFs/RESEARCH-METHOD-PRACTICE-PRINCIPLES-FRAMEWORK.md#rmp143---answer-from-existing-sources-before-starting-a-study) recovers and interprets the relevant material, compares answer-changing alternatives and returns a sufficient answer or precise remaining question. |
| Grounds for an unresolved knowledge claim | [RMP.1](https://github.com/ailev/FPF/blob/main/DPFs/RESEARCH-METHOD-PRACTICE-PRINCIPLES-FRAMEWORK.md#rmp1--decide-whether-a-question-needs-research-and-when-to-stop) establishes whether the question requires research; [RMP.2](https://github.com/ailev/FPF/blob/main/DPFs/RESEARCH-METHOD-PRACTICE-PRINCIPLES-FRAMEWORK.md#rmp2--choose-a-criticism-bearing-research-design-or-stop) constructs and compares obtainable designs when design selection remains open. |
| A warranted account that the recipient can understand and use | [EXD.1](https://github.com/ailev/FPF/blob/main/DPFs/EXPLANATION-DESIGN-PRINCIPLES-FRAMEWORK.md#exd1---establish-and-revise-what-a-recipient-needs-explained) identifies the missing explanatory connection and obtains its subject basis. A missing scientific or mathematical ground returns to that subject work. |
| Professional help with participation, comparison or advice | [PSDA.11](https://github.com/ailev/FPF/blob/main/DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md#psda11---bound-the-decision-support-engagement-and-authority-boundary) bounds the engagement, recipient and choice authority. [PSDA.11–15](https://github.com/ailev/FPF/blob/main/DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md#psda11---bound-the-decision-support-engagement-and-authority-boundary) develop these professional contributions. |

A simulation produces a result under a model and its inputs. Establish the model's applicability before relying on that result for the present subject. Conversely, research may produce a defensible model or explanation as its useful result; its worth need not depend on an immediate commercial decision. Routine measurement, restoration of a service and acceptance against an established criterion can finish in their own practices without becoming research.

Use a sufficient existing contribution and stop this selection. If two kinds of work are needed, state what one must return to the other.

## PSDA.Reference:3 - Formulation, professional support and choice

A lone analyst can formulate a question and construct a model for their own understanding. A team can compare alternatives for its later decision. A professional adviser can use the same intellectual results within an engagement. Keep that service's recipient, representation, consent, conflict, confidentiality and authority conditions with their actual professional owner.

PSDA.11 supplies a bounded engagement when one is needed; PSDA.12 recovers affected Systems, attributed concerns and representation limits; PSDA.13 makes participation and challenge workable and the return faithful. Those results can change the intellectual inquiry. Their availability does not dictate the formulation or establish a truth claim, and a sound model does not supply the participation conditions in return.

Use the general Core opportunity construction C.40.OCN when a worthwhile contribution is not yet settled. It connects useful problems, possible ways, support and conditional reachability. A sufficiently formed analytical question can enter PSDA directly. Strategy supplies direction and commitments; FPF C.11 and the actual authority govern the later choice. Use RMP when a missing scientific result requires research rather than another representation of current premises.

A concern map can preserve what different participants mean. A hydraulic model can estimate a stated physical consequence. A value account can explain which differences matter to the receiving decision. These accounts can inform one another, but none becomes the represented situation or acquires the other's evidential authority.

Likewise, human capability and transfer, organization arrangements, AI evaluation, legal conditions and safety are different questions. This framework helps specify the result needed from each practice and how its absence affects advice. It does not supply those practices' conclusions. Qualify a source's contribution for the subject and configuration of the advice; similar wording does not establish that its result applies elsewhere.

State what each result supports. A description may explain a proposed arrangement; a claim that its relations already hold needs evidence about that arrangement. A score may inform a choice, which remains with the authorized chooser. Advice for a particular client needs results qualified for that case; an available Method alone does not supply them.

## PSDA.Reference:4 - Qualify the result and its combination

Recognition asks whether a formulation, model or comparison can help the current question. Reliance requires the grounds appropriate to the claim. A participant's corrected paraphrase can establish what they meant; it does not establish that their causal explanation is true. A hydraulic calculation needs its physical assumptions and evidence; a permission claim needs its actual authority. A familiar Method and fluent AI explanation are not substitutes for those grounds.

Keep subject, configuration, time, meaning and source scope compatible across joins. A scenario is not a probability. A concern is not a weight. A model that omits a material consequence cannot supply a whole ranking by adding a disclaimer. Narrow the answer or obtain the missing contribution when it can change the receiving use enough to warrant its complete burden.

The feasibility and shared-evidence conditions below apply to the whole proposed combination; individually adequate contributions can still fail together.

Use the questions in [PSDA.4, Combine contributions through explicit joins](#psda444---combine-contributions-through-explicit-joins) for the combination you actually propose. Each supplying result must be qualified for its own claim, fit the receiving subject, configuration, service meaning and horizon, and meet the conditions of joint use. State any conversion that needs additional work: a concern may suggest an objective, but its frequency of mention supplies no value weight; a scenario can condition analysis, but its presence supplies no probability.

Check shared conditions at the scope where they matter. The needed participants must have usable ways to contribute or correct attribution; specialist evidence must cover the relied-on claim; the Methods must be jointly possible with the available competent effort, data access and time. Include preparation, interpretation and coordination where they consume the same limited resources. Results from one dataset retain that shared evidence dependence. Three compatible pairs establish neither a feasible whole arrangement nor three independent confirmations.

In a constructed budgeting variant of APP-PSD-01, attributed concern recovery needs four team-hours, conditional technical analysis needs six, and preparation of the integrated return needs five. These estimates include their preparation and joining effort, require suitably competent staff, and draw on one twelve-hour budget before the board's deadline. The hours cannot be shared or credited to two activities. Every pair needs at most eleven hours, yet the whole needs fifteen. The proposed combined return therefore needs three more hours, a supported arrangement with lower total effort through adequate reuse or another Method, or a narrower answer or later delivery agreed within the engagement. Omitting a required contribution leaves that whole return unsupported. The individual inquiry or calculation can still be useful at its stated scope. These numbers illustrate a joint condition; a real engagement supplies its own estimates and resource rules.

Evidence effort follows the claim someone will rely on. A sketch may locate a disputed service meaning, and a conditional calculation may identify the assumption worth investigating. A recommendation that relies on physical performance, safety, rights or professional competence needs the relevant practice's qualified result. [PSDA.3, Match assurance to the claim being used](#psda345---match-assurance-to-the-claim-being-used) states that boundary. There is no framework-wide sample size, confidence score or completed-workshop count that can replace it. Ask what possible finding could change the bounded return; acquire evidence for that question and stop collecting when further work cannot improve that return enough to justify its burden. Retain a mandatory domain check whenever the intended reliance requires it.

The common practical tension is between obtaining a timely usable answer and preserving the distinctions that can defeat it. More participation can reveal a missing concern while consuming scarce attention. More models can widen the answer while adding interpretation work. A complete ranking can be easier to communicate while requiring judgements the evidence does not supply. State the accepted cost or narrower result, and return to the affected contribution when its conditions fail.

**Constituent actions in ongoing work.** During a decision-support conversation, distinguishing two meanings of a proposal can constitute part of constructing the problem frame, while that framing is part of supporting the pending decision. If the decision concerns allocation of a shared resource, treating each party's local success as the shared criterion can defeat the whole comparison. The facilitator needs the intermediate ability to elicit and compare these meanings, in addition to subject knowledge and the ability to run the meeting. FPF B.1.5.EW makes that vertical recoverable. The PSDA Methods structure the decision support; the participants, subject expertise, authority and resources needed by the resulting course of action must still be available.

Useful inquiry does not require certainty about everything. It requires knowing what the present answer covers, what it leaves open and what could change it. A partial comparison, a retained pair of alternatives, a narrowly qualified recommendation or an exact request can complete the current question.

Keep protected conditions outside a compensating score when their governing source requires that protection. If the requirement's justification is in question, use [PSDA.6 §4.4](#psda6---represent-values-and-trade-offs) and C.11.DUA: compare its protective contribution with its full burden. State separately what change is justified, whether the requirement remains in force, and how it could be amended.

If plausible variation in the estimates or value judgements used by a comparison or recommendation could change its conclusion, test that variation at proportionate effort through [PSDA.9](#psda9---test-robustness-and-sensitivity-of-decision-alternatives-and-their-comparison). Report whether and under what conditions the conclusion changes. When the response at a central input can hide a consequential nonlinear difference, PSDA.9 section 4.3.1 supplies a small paired-response check. Its constructed equal weights are not actual event probabilities. State when a weight or probability is assumed. A missing premise should block only the claims that need it; independent content can remain useful.

A recommendation belongs to the advising activity. Prepare it for the recipient's intended use; leave the later choice and any authorization to the actors entitled to make them. Plans, performed work and observed effects need their own basis. This separation protects the recipient's agency and makes a later change intelligible: the new evidence may narrow advice without rewriting what was previously chosen or done.

## PSDA.Reference:5 - Why retain this connected language

A general choice rule assumes distinctions this work may still need to construct: what the alternatives are, what their consequences mean and which differences matter. A single established analytical method is sufficient when it answers the actual question with adequate premises. A professional facilitation service is sufficient when it already supplies the needed interpretation and analysis. Retain those adequate alternatives.

This repertoire is useful when the formulation changes the model, the model changes the option set, or the uncertainty and value treatment change what comparison is supportable. Keeping these constructions individually usable avoids both a fixed workshop sequence and an unconnected bag of techniques. A material failure returns to its actual contribution; it need not reopen the entire language.

Problem-structuring traditions contribute rival formulations and contextual boundaries. Decision-analysis traditions contribute alternative construction, preference models, consequences, uncertainty and sensitivity. Their source arguments live in each pattern's SoTA-Echoing section. Older value-focused generation and PSM–MCDA integration anchors remain historical ingredients; later syntheses can refine their limits. Constructed teaching cases explain the Methods and do not establish universal effectiveness.

This language joins engagement, participation and return Methods with problem-structuring and decision-analysis Methods through their results because a technically sound answer can address an inadequate question, and an insightful reframing can leave the recipient with no usable comparison. Keeping the contributions individually addressable lets a practitioner repair the missing connection without repeating adequate work. It also preserves a direct inquiry result when no later recommendation is required.

These serious alternatives explain when the arrangement is worth its cost:

| Alternative | When it is sufficient or preferable | Why the broader PSDA arrangement may be needed |
| --- | --- | --- |
| Use one qualified calculation or decision model for a fixed question. | The relevant alternatives, consequence meanings, value premises and evidence are adequate, and the calculation answers the receiving question. | A contested service meaning, excluded alternative or unqualified premise can invalidate the stronger return while the calculation remains useful. PSDA makes that distinction actionable. |
| Use one familiar problem-structuring method (PSM) or facilitated workshop. | Its actual actions and participation conditions fit the required result at acceptable effort. | A workshop can recover concerns without supplying a technical consequence or qualified preference model. PSDA.4 compares a sufficient single Method with a bounded combination and preserves the missing contribution. |
| Use separate problem-structuring and decision-analysis accounts. | One account closes the question, or competent practitioners can already qualify the joins. | A reader otherwise has to reconstruct how a frame becomes an objective, which uncertainty changes the comparison, and what advice is warranted. The shared explanation exposes those joins while the bodies retain their distinct Methods. |
| Apply a complete fixed process to every case. | A recurring service has an established Method whose dependencies and conditions fit the present engagement. | A formed question may need only one comparison, while a contested question may reopen an earlier boundary. The PSDA repertoire makes both possible and lets actual dependence, rather than publication order, determine the route. |
| Use general FPF guidance and the direct subject practice. | The live question is already covered by a choice rule, a bounded evidence request or a specialist Method. | The integrated repertoire retains separately usable formulation and analytical constructions together with the professional work of obtaining suitable inquiry, organizing participation and facilitation, preserving its limits and returning qualified advice. The general distinctions alone do not perform that work. |

The scope also includes improving and continuing this practice. A better way to elicit concerns, a repair to simultaneous inquiry, and the successful transfer of that way to another team are different achievements. PSDA.16, PSDA.17, PSDA.18 preserve their separate questions and evidence. They become relevant when the repertoire, interaction or continuation is itself at issue; an ordinary comparison need not become a professional-development programme.

### PSDA.Reference:5.1 - The development-direction profile and neighboring results


The [development-direction advising profile](#development-direction-advising) is a bounded use of the shared PSDA contributions. Its difference is consequential: advice concerns a developing subject whose capability, support configuration, horizon and professional relationship can change what is supportable. A sponsor may differ from the person whose private assessment matters; human transfer evidence differs from an organization's arrangement comparison and from an AI configuration's evaluation. The profile's [guidance on evidence about the developing subject](#psdaadvising4---recover-only-the-relevant-holder-premises), [comparison guidance](#psdaadvising7---compare-for-this-receiving-use), [worked uses](#psdaadvising11---worked-uses-and-stopping-points), and [recognition and assurance account](#psdaadvising12---recognition-assurance-and-practical-gain) supply those narrower answers. Its professional source account retains the actual service boundaries; they do not become entry requirements for every PSDA inquiry.

Core C.40.OCN constructs a useful conditional opportunity before the result is settled. Its full opportunity Methods provide inquiry, characterization, search, problem and contribution, directions, joint reachability, retained possibilities and requalification. PSDA.19 governs the distinct advising relationship, including subject-specific premises and an honest refusal or narrower return. An opportunity can supply decision alternatives, while a formed question with adequate inputs needs no prior opportunity-construction pass. The development-direction profile explains the professional connected use without making one supplier's operations the whole service.

The [direct-practice boundary account](#psdareference9---direct-neighboring-contributions) identifies the result needed from human development, organization arrangements, technical evaluation and other practices. Such a result supplies a premise for this inquiry; the supplier retains its Method, evidence and conclusion. For example, an organization's qualified comparison of provider and internal arrangements can support advice, while a publication describing how to make that comparison cannot settle the client's case.

The framework supplies professional and analytical Methods with different completion conditions. An analytical result does not establish a professional relationship or the later decision. A claim that a selected combination is one composite Method needs the whole action, identified part Methods, permitted variations and joins specified in PSDA.4. A Part groups reading material; a profile narrows use; a result dependency states what one contribution needs from another. Those relations do different work. Reconsider the organization of the language when its field boundary, a profile's independently useful result, or a recurring contribution changes.

### PSDA.Reference:5.2 - Why the source lines are combined


Problem-structuring methods give the framework a substantive answer before optimization begins: make rival interpretations and their practical consequences available for inquiry. Smith and Shaw's [2019 characterization](https://doi.org/10.1016/j.ejor.2018.05.003) and Kogetsidis's [2025 application review](https://doi.org/10.1108/IJOA-08-2024-4746) support a diverse continuing practice, with exploratory and published-application limits. The framing comparisons used in PSDA.1 add the need to make contextual changes visible. The formulation Methods use these contributions to construct materially different formulations and stop when they are sufficient for the inquiry or decision they serve. PSDA.1 compares a sponsor's initial brief with formulations whose differences change the next action; neither an unquestioned brief nor endless perspective collection supplies that comparison. The exact comparison and its source limits remain in [PSDA.1, SoTA-Echoing](#psda111---sota-echoing).

The older critical review of combining problem-structuring methods with multiple-criteria decision analysis (MCDA) by [Marttunen, Lienert and Belton (2017)](https://doi.org/10.1016/j.ejor.2017.04.041) makes the interfaces between structuring and analysis part of the problem. The exploratory workshop comparison by [Lami and Tavella (2019)](https://doi.org/10.1016/j.ejor.2018.12.016) provides a bounded counterexample to uniform workshop usefulness. PSDA develops their contributions into the smallest complementary model set and explicit Method joins in PSDA.3, PSDA.4. This costs more interpretation than applying one familiar technique. Retain the cheaper technique when it supplies the same result and conditions; the reviewed applications establish no universal winning combination.

The analytical line supplies ways to build alternatives, express values, compare consequences and identify useful uncertainty questions. The [2025 MCDA synthesis by Greco, Słowiński and Wallenius](https://doi.org/10.1016/j.ejor.2024.07.038) informs matching preference information to the comparison and recommendation form. [Borgonovo and colleagues' 2026 decision-analysis synthesis](https://doi.org/10.1016/j.ejor.2025.05.023) connects alternative construction, uncertainty, sensitivity and information acquisition. PSDA.5, PSDA.6, PSDA.7, PSDA.8, PSDA.9, PSDA.14 adopt these as selective contributions: a justified scalar model remains usable, incomplete preferences can leave a retained set, and one missing branch limits the whole recommendation. The cost of this arrangement is a less decisive-looking return when the premises warrant less decisiveness.

Under unsettled futures, [Lempert and colleagues' 2024 DMDU analysis](https://doi.org/10.3389/fclim.2024.1380054) supports decision-relevant inquiry despite low-confidence knowledge. The older [2019 DAPP account](https://doi.org/10.1007/978-3-030-05252-2_4) contributes pathway timing and failure conditions. PSDA.7, PSDA.9 and PSDA.15 use those distinctions to expose holding regions, reversals and attainable follow-up. They leave probabilities, local thresholds and authority to their actual sources. A qualified probabilistic analysis remains preferable when its premises fit; calling uncertainty difficult is not a reason to discard it.

Professional sources add conditions on the return that a technically correct comparison may leave open. PSDA.14 uses selected ICMCI engagement and conflict clauses within consulting and NCDA provisions within human career services. The [profile source-responsibility account](#psdasources3---source-responsibility-and-references) separately qualifies AI used by an adviser. These bounded normative contributions address competence, intelligible reliance and the service relationship. They supply neither a universal advising protocol nor effectiveness evidence for an intervention. The wider [source map](#psdasources1---source-arguments-and-refresh) returns to the facilitation, follow-up, repertoire and cultural-continuation arguments in their own bodies.

Reconsider the affected arrangement when a simpler Method supplies the same useful return, a shared condition or join fails, a material perspective cannot be preserved, or better evidence changes a source contribution. A local case may need a different Method without defeating the whole language. Repeated failures of the same boundary or profile, or a recurring practical need that the existing contributions do not meet, are reasons to reopen the architectural choice.

### PSDA.Reference:5.3 - Decision theory, model construction and engineering trade studies

A chooser may already have adequate options, a consequence model and an evaluative basis. FPF C.11 supplies the choice-theory construction for that situation, including a partial comparison, rejection of the available set or a worthwhile probe. PSDA addresses work that those premises can still need: constructing formulations and alternatives, eliciting and representing preferences, retaining uncertainty at its supported kind, building consequence accounts, and composing a return for its actual use. Apply a sufficient C.11 result directly when the premises are already adequate. The mathematical choice rule is not developed again in this framework.

The general construction suppliers also retain their own questions. C.38 constructs comparable ways to obtain one result; PSDA.5 can construct alternatives that pursue different results or answer different formulations. C.39 develops a missing obtaining operation or connection. C.40 develops branching search from reusable material, while C.40.OCN connects opportunity inquiry, problems, directions and conditional reachability. A PSDA inquiry supplies the actual formulation, elicitation, modelling and professional operations. A general supplier does not supply a missing subject result merely because its scope includes that question.

C.11.CRC supplies finite configuration-relative contribution comparison when baseline, interactions and the whole change matter. C.11.DUA appraises further advice or evidence work by its attainable receiving value and full burden. C.11.DBR supplies reconsideration after a relied-on decision basis changes. PSDA.8, PSDA.14 and PSDA.15 use these constructions for their respective questions while retaining the professional interpretation, recommendation and observation arrangements. B.5.SD supplies joint substantive answer construction; B.5.RA and B.5.RR retain argument recovery and changed-reasoning operations. A discussion needs only the contribution absent from its present answer.

In engineering, [Decide and Reopen the Engineering Architecture (SYSE.6)](Engineering%20DPF%20Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse6---decide-and-reopen-the-engineering-architecture) binds an architecture decision to the engineered System, selected structures, configurations, operating conditions, qualified engineering evidence and later realization Work. A comparison or recommendation can supply its premises without taking that decision or proving realization. [NASA's decision-analysis account](https://www.nasa.gov/reference/6-8-decision-analysis/) joins criteria, alternatives, evaluation and uncertainty with a recommendation, at rigor proportionate to the decision. [SEBoK Decision Management](https://sebokwiki.org/wiki/Decision_Management) explicitly connects engineering trade studies to decision-analysis mathematics, value-focused alternative generation and the system lifecycle. These connections permit reuse; the engineering Method retains its subject-specific result and conditions.

One professional use of decision analysis includes constructive work. [Phillips's 2025 practitioner treatment](https://pubsonline.informs.org/doi/10.1287/deca.2025.0356) distinguishes the formal ingredients of decision theory from situated model construction with clients, including framing, objectives, alternatives, interpretation and sensitivity. It informs the connected practice here: technical and participation contributions can correct one another while keeping their different grounds. This is an argued practitioner approach and case evidence, not a requirement for a workshop in every use or evidence that confidence in a model establishes its truth.

Machine-learning decision models raise another construction question. For example, [decision-focused learning](https://doi.org/10.1613/jair.1.15320) combines learning with constrained optimization and trains the learned component for the resulting decision quality. A model that contributes to generating an action need not be an analysis of supplied options. The actual learning, optimization and deployment Methods retain their computational and empirical conditions. This framework can help construct their problem, value and consequence premises or interpret a qualified result; its formulation and professional-inquiry Methods do not supply the missing training or deployment procedure. A normative choice rule, a constructed model, a learned action-producing arrangement and the later authorized decision are different contributions.

### PSDA.Reference:5.4 - One bounded language and its wider connections

The shared subject is construction, interpretation and responsible use of problem formulations, decision alternatives and models in a bounded inquiry. **Decision Design** names that constructive practice. Here responsible use means an intelligible return, justified reliance within its conditions, and reassessment when the basis changes. The recipient retains the authorized choice and commitment; their governing practice carries the action. The arrangement is useful when a changed concern alters a formulation, a formulation changes the alternatives or models, or an uncertainty result changes what comparison or recommendation is warranted. Qualified participation is consequential within these constructions; it is not merely preparation for presenting a finished calculation. The language keeps the associated professional Methods and independently usable analytical constructions together so that the reader can obtain and revise these connections.

Its whole-use quality is the adequacy of the return to its receiving question with recoverable and revisable formulation, model, value, evidence and participation grounds. An accurate calculation can still answer an inadequate question, while a faithfully facilitated discussion can still lack a warranted consequence model. The joins described in sections 2–4 expose which missing contribution defeats the stronger answer. No single scalar or demonstrated universal effectiveness is claimed for this quality.

The practice can continue through a different model family, elicitation technique, facilitator, tool or source while those contributions and return relations remain usable. A revised preference method need not invalidate a sound boundary construction, and a changed participation condition need not alter valid arithmetic. PSDA.16–.18 address repertoire, interacting inquiry and continuation when those are the current questions. Replacing the language with arbitrary advice, numerical solving over an unquestioned formulation or the recipient's power to choose would change its subject.

Professional sources indexed under Operational Research connect further contributions. The OR Society's [methods account](https://www.theorsociety.com/ORS/About-OR/OR-Methods.aspx) includes optimization, simulation, stochastic modelling and decision analysis; its [Problem Structuring Methods account](https://www.theorsociety.com/ORS/Community/SIGs-List/Problem-Structuring-Methods.aspx) describes interpretative model-building for contested situations and connections with other MS/OR contributions. This framework covers the formulation, model and professional-inquiry questions developed in its Methods. It supplies no complete optimization, simulation or stochastic-system repertoire. Co-listing those methods neither establishes one disciplinary whole nor makes this framework its constituent, and the practice-development Methods here retain their bounded subject.

This subject is narrower than either a comprehensive science of decisions or the design and operation of an arrangement that repeatedly makes operational decisions. Decision Management can name a lifecycle process, as in the engineering account above, or the construction and maintenance of operational decision systems. [OMG Decision Model and Notation](https://www.omg.org/dmn/) contributes precise business-decision and rule models to the latter setting; such models can be used with process and case models. Their implementation, operation and change require contributions beyond this framework. A qualified formulation or recommendation can supply those practices without replacing them.

Separate problem-structuring and model-construction frameworks could make independent source communities and change boundaries more visible. Here their connected inquiry account remains in one language, while direct entries and source-specific revision conditions preserve useful independence. A broader Suite account becomes useful when a supported disciplinary whole explains additional model/intervention connections that the current user needs, or when separately maintained languages provide a material advantage. The useful formulation, model and professional contributions remain available without first settling that wider arrangement.

The present language can supply qualified formulations, value and uncertainty accounts, comparisons and bounded advice to a wider inquiry. Engineering, management, policy and personal decision work can use those results. Such use establishes the supplying and receiving questions, not membership of the entire field in Engineering or Management. Domain architecture, scientific inference, implementation and the authorized choice retain their own Methods. An adequate specialist result is an available direct entry, not a reason to repeat all eighteen Methods.

## PSDA.Reference:6 - Continue and change the practice

A changed source or receiving condition reopens only the dependent claims until evidence warrants a wider revision. Preserve useful earlier results within their actual scope. A professional organization can use PSDA.16, PSDA.17, PSDA.18 for repertoire, simultaneous service work and cultural continuation; an independent intellectual inquiry can use the general Method-development and cultural-reproduction guidance directly. Neither path is a compulsory tail to one calculation.

The useful change in practice is the ability to reconstruct a consequential distinction, obtain the right model or comparison, and tell what conclusion it actually supports. Successful communication, accepted advice and realized outcomes remain separate results. The next inquiry starts from the changed knowledge and its actual question, not from an obligation to repeat every pattern.

A corrected concern, altered access condition or new model configuration can change the current result. Identify the claims that depend on the change and ask the responsible practitioner to reconsider them. Obtain and interpret the relevant observation before choosing a response; the mere arrival of a notice is not evidence that the new configuration is safe or effective.

A different problem concerns how inquiry itself is conducted. Use [PSDA.16](#psda16---decide-whether-and-how-to-change-problem-structuring-and-decision-support-methods) when the professional repertoire needs a justified change, [PSDA.17](#psda17---reconcile-simultaneous-problem-structuring-and-decision-support-work) when simultaneous inquiry activities interfere, and [PSDA.18](#psda18---deliberately-continue-and-change-problem-structuring-and-decision-support-culture) when a practice must be continued or changed across practitioners. These are conditional uses, not a required tail on every recommendation.

Contemporary source comparisons belong with the pattern claims they support. Earlier traditions remain valuable where their limits are understood. Neither a fashionable school nor an old success is enough to establish the present Method's fit. What changes in practice is the reader's ability to return a useful answer with visible limits—and to change that answer, or the way of obtaining it, when the actual basis changes.

## PSDA.Reference:7 - Whose conditions and evidence shape the answer

The sponsor's first question, the participants who can attend, and the analyst's familiar models all affect what is made visible. Record whose concerns are attributed, which affected people or consequences remain unrepresented, and how a material correction can reach the result. PSDA.12 and PSDA.13 provide that work. More participation does not make all claims equally supported, and a dissenting position has only the practical or institutional effect justified in the case. Domain rules determine a right, duty or protected condition.

The worked applications emphasize institutional investment and development advice. They are constructed teaching cases, and the source studies have their own populations, professional settings and access limits. A practitioner transferring the guidance must qualify local meanings, communication access, evidence and service conditions that can alter use. Method familiarity, fluent AI output, participant confidence and publication visibility can all be mistaken for support of a different claim. The relevant pattern's evidence and bias questions help locate that claim; no single confidence measure qualifies the whole inquiry.

## PSDA.Reference:8 - Questions before relying on a combined return

The opening and direct entries help recognize the first useful action. Assurance asks whether the result is supported for its intended reliance. Use the checklists in the patterns actually selected, and reuse their qualified answers when the subject, content, receiving use and conditions remain the same. For the combination, answer the following questions:

- Can the recipient recover what this return answers, whose later decision or inquiry it serves, and what remains outside it? An early inquiry may end with a formulation or precise question.
- Do material concerns, competing frames and boundary choices survive into the models, alternatives and comparison that depend on them? A supported correction must reach the claim it changes.
- Does each relied-on result cover the needed subject, configuration, meaning and horizon, with its actual evidence limits? Have shared assumptions or sources been counted only for the support they supply?
- Do the selected Methods meet the [joint conditions](#psdareference4---qualify-the-result-and-its-combination), including total effort and required interpretation? Feasibility of each pair does not establish that all the required work can be done together.
- Does the scope of the recommendation match the alternatives and conditions actually examined? In APP-PSD-01, two pump options can be compared conditionally while the whole investment question remains open. In APP-PSD-02, a qualified provider exclusion can close that branch, while an unexamined provider cannot simply disappear.
- Is it clear what information to request, when the inquiry can finish, and which advice must be reconsidered if a premise changes? Does the authorized decision-maker retain the later choice or action? The development profile also needs its stated service conditions and evidence about the developing subject; those qualifications are not inherited merely from generic PSDA use.

These questions address failures shown in the applications: one service phrase hiding unlike concerns, an unjustified conversion of qualitative meaning into a score, and a partial comparison presented as a whole recommendation. Correct the particular meaning, obtain the missing contribution or narrow the return. Answer the questions in the working account the recipient needs; actual performance and later effects require their own evidence.

## PSDA.Reference:9 - Direct neighboring contributions

Within PSDA, engagement, participation, facilitation, recommendation and professional continuation are available through the Methods identified in the pattern index. Leadership supplies contributions and effective commitments. Core C.40.OCN constructs a bounded opportunity and C.40.OD connects knowledge or Method growth to continuing development. Research Method Practice supplies research where a representation of known premises cannot answer the question. Strategy supplies strategic direction, choice and portfolio commitments. Those neighboring contributions retain their own subjects and conditions when a PSDA application needs their results.

Use a direct source when it owns the whole current question. If a chooser already has an adequate option set and needs only their own decision, use [FPF C.11](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11---decision-theory-decsn-cal) or the applicable domain decision rule. If an engagement needs just one missing specialist result, [FPF A.15.9](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a159---use-or-request-a-bounded-result-from-another-practice) gives the bounded inspect, reuse or request entry.

| Needed contribution | What PSDA can do | What it does not supply |
| --- | --- | --- |
| Human capability demand, diagnosis, intervention or transfer | State which person's later Work and which advice premise need a qualified result; use the direct human-practice entry named in the development profile. | A diagnosis, effective curriculum, learning effect, occupational opportunity or demonstrated transfer from a course title or general guidance. |
| Organization, operating or provider arrangement | Specify the result, configuration, use, horizon and acceptance question to compare; retain independent alternatives when one premise fails. | This client's whole-arrangement comparison, implementation capacity or authority from a position description, operating account or published Method. |
| AI/model or other technical evaluation and safety | Identify the configuration and intended use, select a result request when its obtainable decision contribution warrants acquisition, and reconsider only advice that depends on a changed premise. | Evidence for configuration B from A, deployment permission from an evaluation, or practical reachability from novelty or an archive label. |
| Physical, scientific, financial, legal, ethical, safety or governance facts and rules | Expose the premise, its owner, qualification window and effect on the return. | A local threshold, mechanism, permission, professional duty or protected condition by analogy with another field or holder. |
| An evolutionary population or lineage | Recognize the absence of a population-local recipient and choice owner in the represented case. | A development recommendation to that population. A researcher selecting an intervention has a separate question, scientific basis and authority. |

These are boundaries of this guidance, not declarations that the neighboring practices or all their results are unavailable. A published Method may be available while the application-specific result is still missing. Ask for the smallest result that can change the answer; do not wait for every neighboring framework to be packaged, and do not fill a gap with a same-named result from another subject.

A real application must qualify the relied-on content for the stated subject, configuration, receiving use and horizon. [FPF A.10](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a10---evidence-graph-referring-claim-bound-evidence-and-provenance-graph) governs that reliance, while the relevant domain practice governs the claim itself. Discovery, availability, evidence, applicability and authority are different questions.

## PSDA.Reference:10 - What this framework covers

Decision Design serves practitioners and assisting agents constructing and using problem formulations and decision models, including professional help for another's inquiry or decision. Its complete Methods cover formulations, boundaries, complementary models, Method selection and combination, alternatives, values, uncertainty, consequences and robustness, together with engagement, participation and representation, protected facilitation, qualified recommendation, follow-up, repertoire, simultaneous inquiry, cultural continuation and development-direction advice. A recommendation, request, narrowed answer or reasoned abstention can complete that work without taking the recipient's later choice.

Core C.11 supplies the decision-theory construction, C.40.OCN supplies general opportunity construction, and B.5.SD supplies joint substantive answer construction. The practitioner obtains their results when those questions are live and qualifies the joined use. Their availability does not require repeating them as additional PSDA Methods.

PSDA.12 and PSDA.13 remain full professional Methods: participation channels, representation, attributed concerns, facilitator interests, consent, confidentiality, coercion protection and faithful return require their actual relationship and conditions. A correct model does not supply them.

The development-direction profile explains a connected use; PSDA.19 supplies its separately reusable advice Method. The applications preserve the distinction between a useful opportunity, an analytical result, a recommendation, programme choice, learning design and actual performance. They are constructed teaching cases, not implementation or effectiveness evidence. An opportunity inquiry without an adviser can finish at its own result and does not invoke a service merely because it appears in a professional application.

## PSDA.Reference:11 - Change only what the new basis changes

Retain the source and conditions behind each premise that matters to your recommendation. When a source changes, revisit the advice that relied on it and state any revised limit. The [source responsibility and references](#psdasources3---source-responsibility-and-references) below identify the qualified sources and explain which claims to reconsider.

When a source, configuration or receiving condition changes:

1. Identify the claim that used it and whether the new information concerns the same subject and use. A notice is not yet a replacement evaluation.
2. Choose the guidance for the changed premise and the result needed. With an unchanged source but changed actual conditions, use the direct subject guidance. For one already-known bounded source-reliance question, use [FPF A.10](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a10---evidence-graph-referring-claim-bound-evidence-and-provenance-graph); for a materially changed source claim whose receiving uses still need discovery or closure across several uses, use [FPF A.10.1](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a101---revalidate-affected-uses-when-a-relied-on-source-changes); for currentness or a scoped refresh-planning or reporting result, use [FPF G.11](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#g11---decide-whether-and-how-to-refresh-sota-packs-and-related-results-telemetry-and-decay) under its conditions. Keep independent supported content and return material missing premises as limits. Select a further supplier request through A.15.9 and C.11.DUA only when its attainable contribution warrants the whole acquisition burden. A compatible reference repair or sufficient direct answer needs no duplicate common account; a no-impact claim still needs adequate coverage and support.
3. Return the strongest answer still supported: unchanged within scope, narrowed, blocked, returned to its contributor or replaced by later advice. Use PSDA.15 when a decision-support follow-up question is live.
4. Revise the reusable pattern, Method or profile only when its own claim changes. A client-specific result, professional service duty or observed outcome retains its own owner and history.

For example, loss of a mobile pump's access premise reopens that branch, not independent fixed-option arithmetic. Loss of trained reviewers invalidates a staffing-dependent mixed probe, not an unrelated internal option or the tool evaluation within its own scope. A changed professional disclosure condition concerns the applicable service, even when the developing holder is not AI. An unsupported transfer from one learner or model configuration cannot be repaired by broadening the name of the original evidence.

Keep earlier source states recoverable when revising this guidance. An updated description does not rewrite past Work, earlier advice, prior choices or their evidence. Changes that alter a recurring problem, useful result, boundary between practices responsible for a result or claim, or whole-field promise need the corresponding content decision; changed links or presentation alone do not create a new practice or prove improvement.

## PSDA.Reference:12 - Obtain the result needed for the developing subject

| Method or source | Contribution to advising |
| --- | --- |
| [FPF A.3.1](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a31---umethod-reusable-way-of-doing-with-explicit-applicability) and [FPF A.3.2](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a32---umethoddescription-description-episteme-for-a-way-of-doing) | Identify the reusable method and what describes its performance. Evidence of actual performance and effectiveness comes from the application. |
| [FPF A.15.9](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a159---use-or-request-a-bounded-result-from-another-practice), [FPF A.10](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a10---evidence-graph-referring-claim-bound-evidence-and-provenance-graph) and [FPF A.10.1](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a101---revalidate-affected-uses-when-a-relied-on-source-changes) | Obtain a needed specialist result, keep its evidence and limits, and revisit the advice that depends on a changed source. |
| [FPF C.18](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c18---open-ended-search-archive-and-front-stewardship), with C.19 when its search question applies | Support open-ended generation and use of an archive. Obtain results from the relevant domain practice to establish the opportunity's practical reachability and value in the case being considered. |
| HCD.1, HCD.3 and HCD.4 ([complete HCD first edition](Human%20Capability%20Engineering%20DPF%20Suite/HUMAN-CAPABILITY-DEVELOPMENT-PRINCIPLES-FRAMEWORK.md)) | Investigate demand from later human work, a limiting development target and a capability profile. These are the HCD contributions named for this PSDA use; other HCD patterns remain available only under their own working conditions. Further intervention, curriculum and transfer results require their relevant methods and evidence. |
| [OCE.8](Management%20DPF%20Suite/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce8---compare-human-ai-robotic-and-provider-arrangements-for-the-same-organizational-work-result) | Compare whole organizational arrangements once the needed result and its conditions are sufficiently established. Bring the actual organization's comparison back to the advice. |
| The applicable technical or professional practice | Supply the strategy, operating, AI evaluation, safety, authority or other case-specific premise that can change the opportunity or recommendation. |

The sources support the named contributions and their limits. Testing the combined opportunity-construction method, or establishing the effect of an intervention, requires evidence from its actual use.

The [source responsibility and references](#psdasources3---source-responsibility-and-references) retain the qualified professional and historical source grounds; [source and case changes](#psdareference13---keep-source-changes-and-case-changes-distinct) have different receiving consequences.

## PSDA.Reference:13 - Keep source changes and case changes distinct

When a fact about one person, organization, model or provider changes, reconsider the opportunity or advice that depended on it. A changed human career-service condition affects the human engagement, assessment or return that used it; a changed consulting disclosure condition affects the applicable service. Keep the independent evidence for other subjects and conclusions.

Revise the reusable method when new evidence or a better approach changes its search, opportunity construction, dependency reasoning, reachability test or stopping rule. The maintainer of the affected advising or opportunity Method retains the changed claim, its source, the affected contribution and the revised limit. Reopen a wider PSDA contribution when one of its shared inputs or results changes.

A person using advice keeps the relevant subject, configuration, intended use, period and source conditions visible. Actual service relationships determine consent, confidentiality, competence, referral and closure duties. Apply the duties established for that relationship, and obtain a missing professional or technical result before relying on the affected conclusion.

The [source responsibility and references](#psdasources3---source-responsibility-and-references) identify the relied-on sources, while the [subject-specific supplier account](#psdareference12---obtain-the-result-needed-for-the-developing-subject) identifies the contribution whose local use may need to change.

## PSDA.Reference:14 - Direct frameworks, predecessor sources, and honest omissions

This framework supplies formulation, model, value, uncertainty and comparison constructions through [PSDA.1–9](#pattern-index), and professional engagement, participation, facilitation, recommendation and follow-up through [PSDA.11–15](#psda11---bound-the-decision-support-engagement-and-authority-boundary). [Human Capability Development (HCD)](https://github.com/ailev/FPF/blob/main/DPFs/Human%20Capability%20Engineering%20DPF%20Suite/HUMAN-CAPABILITY-DEVELOPMENT-PRINCIPLES-FRAMEWORK.md) supplies personal demand, programme and evidence contributions. [OCE.8](https://github.com/ailev/FPF/blob/main/DPFs/Management%20DPF%20Suite/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce8---compare-human-ai-robotic-and-provider-arrangements-for-the-same-organizational-work-result) supplies whole-arrangement construction and comparison when that same-result question is current. Their use is claim-specific; a bibliography entry is not proof of dependency or client adequacy.

The earlier opportunity-construction description, [advising profile](#development-direction-advising) and [source-responsibility account](#psdasources43---predecessor-source-account-access) remain distinct sources, with their public expressions and access limits identified below. Their construction moves are carried by C.40.OI, C.40.NU, C.40.PC, C.40.DC, C.40.JF, C.40.OP, their actual engagement conditions by PSDA.19, and their affected-opportunity return by C.40.RQ. Use [PSDA.14](#psda14---prepare-and-return-a-decision-support-recommendation) for the qualified recommendation and [PSDA.15](#psda15---arrange-decision-follow-up-or-reassess-advice-after-a-change) for follow-up or reassessment.

The [Foundations programme](#psdasources42---foundations-programme-source-access) and [comparison](#psdasources42---foundations-programme-source-access) illustrate a programme design considered before a particular person's development question. A learner-oriented narrative can arrange explanations and practice for learning; a compact pattern body helps a practitioner select a move for a working difficulty. For a particular person's capability, programme fit or learning result, use the relevant direct practices and observations.

Broader career-design exercises, motivation and learning-science accounts, real-options valuation, specialist investment valuation, complete professional certification, legal/safety compliance and domain implementation are not reproduced here. Their omission is not permission to bypass them when a receiving claim needs them. Return that exact question to its actual current owner.

## PSDA.Reference:15 - Development-direction advising within a wider undertaking

Within a wider development undertaking, this framework's development-direction advising profile supplies bounded problem formulations, alternatives, decision models and recommendations; it does not own the whole development undertaking. [FPF C.40.OD](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c40od---construct-and-continue-open-ended-development) combines the developed Library contributions to problematisation, Method construction, transformation-flow description, capability development and cultural continuation. B.5.PI, C.39, C.40.CD/CU, E.18/E.18.NET, C.32.MWA, E.23.CDI and C.36/C.36.RP retain their precise subjects and conditions. A.12 retains the internal acting/changed-parts explanation where its premises hold. HCD, OCE, the Core Method constructions and the actual target practice retain the operations that make a subject-specific transition attainable. C.40.OD:11 compares the developed joining contribution with direct C.32.MWA.PP/C.40.CU/subject-Method composition, preserves the latter as an adequate cheaper stop, and identifies the exact CIPD and MIT CISR organizational sources and their adaptations. The synthesis supplies the connections and changed-condition construction, not a new universal mechanism for every development subject. In particular, the same-agent explanation in C.40.JD:4.2 connects available capability to a development operation and its receiving use; it neither replaces Reflexive Split nor infers acquisition from the description of a change.

STR.16 uses STR.8/11/14 for contribution and commitment construction, RMP.1/2/8 for independent epistemic purposes and attainable inquiry, MA.1–3/8 for scarce demand and time-related obligations, and OCE.8/9/11 for obtaining and realizing support while current work continues. Its original OECD comparison and transfer limit are stated in STR.16:11. In particular, the mission-portfolio source does not make independent science subordinate to the next commercial release.

The role-community essays cited by C.40.OD contribute overlapping organizational/community relations, participant journeys and competing formal/informal influence. They are conceptual sources from 2024, not evidence that every office disappears or that AI universally replaces human contributions. Their useful source question is how the participant's own purpose, burden and authority changes the proposed provision.

These constructions can be examined through their intermediate results, whole conditions and changed cases. Their worked examples are stipulated explanations, not observations of organizational effectiveness or any provider's actual resources. Reopen a dependent move when subject evidence, a supplier or practical use defeats its connection. An adequate direct Method retains its stopping power.

For source qualifications, citation and edition information, see the [Sources and Edition Notes](#decision-design-principles-framework-sources-and-edition-notes).

## PSDA.Reference:End

# Patterns

## PSDA.1 - Generate Plural Problem Formulations

> **Type:** Method pattern body
> **Status:** Stable
>
> **Primary working result:** a **plural formulation set** for one bounded receiving inquiry: materially different accounts of what warrants intervention, each with its subject, boundary, affected participants or Systems, value tension, evidence need, intervention logic, assumptions, and consequence for the receiving use.


### PSDA.1:1 - Problem frame

Use this pattern when one wording of “the problem” is becoming naturalized even though materially different accounts would change what is included, what evidence matters, which interventions are plausible, whose values are exposed, or what the recipient should do next.

Begin from the bounded inquiry question. A professional engagement can supply it through `PSDA.11`. Use the `PSDA.12` participation and concern account when affected participants, Systems, duties, interests, or dissent are material. Generate formulations that differ in decision-bearing structure, not merely vocabulary, and return them without selecting a winner.

The practical gain is an inspectable choice of frames before modeling, option generation, or comparison locks in the sponsor's first account. Do not use PSDA.1 for a thesaurus exercise, generic creativity session, alternative generation for an already-stable problem (`PSDA.5`), or archive/front stewardship (`C.18`). If one formulation is already adequate and no credible rival could change the receiving use, proceed to the actual missing result.

#### PSDA.1:1.1 - Working Distinctions

| Working term | Meaning in this pattern |
| --- | --- |
| problem formulation | A bounded, source-qualified account of what condition or relation warrants inquiry or intervention for a named receiving use. It proposes a subject, boundary, concern, evidence need, and intervention logic; it is not the situation itself. |
| plural formulation set | Two or more materially different formulations retained together because each can change a downstream boundary, model, alternative family, value treatment, evidence request, or recommendation. |
| material difference | A difference that changes at least one decision-support move. Synonyms, rhetorical emphasis, or unexplained labels are not material plurality. |
| intervention logic | The connection a formulation proposes between the condition treated as problematic and the families of action, inquiry, adaptation, or restraint worth considering. It is a hypothesis, not proof of causation or effectiveness. |
| framing commitment | A supported or provisional inclusion, exclusion, assumption, value emphasis, or causal hypothesis built into one formulation. |

Ill-structured situations do not arrive with one neutral problem object waiting to be described. “Insufficient capacity”, “unequal protection”, “maintenance fragility”, and “unsafe deployment” can concern the same pumping arrangement while selecting different bearers, boundaries, evidence, interventions, and consequences. The formulations may conflict, overlap, or remain jointly useful.

The primary concern is to make those decision-bearing differences recoverable before one model or Method absorbs them. Recognition is cheap: one credible rival intervention logic is enough to test plurality. Assurance remains direct for every factual, causal, evaluative, legal, ethical, safety, authority, or source claim used within a formulation.


### PSDA.1:2 - Problem

The sponsor's first sentence often becomes the model title, data request, option space, and final recommendation. Its assumptions disappear because they are encoded as scope. A second failure produces many “perspectives” that differ only in wording and therefore add ceremony without changing any downstream work. A third treats plurality as permanent indecision and refuses to bound the inquiry.

The needed discipline is neither immediate convergence nor unlimited reframing. It is to construct a small set of materially different formulations, expose what each makes visible and suppresses, and stop when additional formulations no longer change the current receiving use.

### PSDA.1:3 - Forces

| Force | Tension |
| --- | --- |
| Plurality | Rival formulations can prevent premature closure, while decorative variety wastes effort. |
| Usability | Each formulation must guide a next move, while early precision can pretend that contested claims are settled. |
| Participant fidelity | Concerns should shape formulations, while participation does not prove the formulation. |
| Evidence | A formulation reveals what evidence matters, while it must not smuggle unsupported causes or effects into the case. |
| Exploration and stopping | New frames can reveal alternatives, while an unbounded set cannot support a decision. |
| Authority | A recipient may compare formulations, while neither a facilitator nor the set itself owns the later choice. |

### PSDA.1:4 - Solution

Generate a bounded set of problem formulations whose differences are visible in their downstream consequences. Bind every formulation to the same receiving inquiry unless a different receiving question is explicitly separated. Preserve sources, assumptions, uncertainty, and conflicts; then hand the set to boundary, modeling, alternative, and inquiry patterns without declaring a chosen problem.

#### PSDA.1:4.1 - Fix the receiving inquiry, not the problem answer

State the subject, receiving question or Work and horizon. Name a recipient and later choice owner where the use has them; an inquiry for understanding need not appoint an adviser. A professional engagement can supply these premises through PSDA.11. Import a qualified PSDA.12 account only where participants, affected Systems, concerns, duties, interests or dissent can change this inquiry. Other direct sources may supply adequate premises. If the subject or receiving use differs, separate that inquiry rather than merging formulations across identities.

Write the current formulation in one sentence. Mark its source, factual support, assumptions, and important exclusions. This makes the default frame inspectable rather than privileged.

#### PSDA.1:4.2 - Generate structural contrasts

Seek contrasts along the smallest productive set of questions:

- What condition or relation is treated as problematic, for whom or what?
- Which bearer, place, configuration, horizon, or consequence is central?
- Which value, duty, interest, or risk makes intervention worth considering?
- Which mechanism or dependency is hypothesized, and what evidence could challenge it?
- Which action families become plausible, and which disappear?
- Who can prepare, receive, authorize, or implement a response?

Do not require one formulation per question. Combine contrasts into coherent candidate formulations. If two formulations imply the same boundary, evidence, action family, and receiving-use consequence, merge them or state that their difference is rhetorical.

#### PSDA.1:4.3 - Give every formulation a usable face

For each retained formulation, record:

| Position | Required content |
| --- | --- |
| formulation | One ordinary-language account of what warrants inquiry or intervention. |
| subject and bearers | Exact subject, affected participants or Systems, configuration, place, and horizon needed by the claim. |
| boundary and exclusions | What the formulation includes, what it suppresses or defers, and why. |
| value tension | Attributed concern, duty, interest, risk, or desired change that makes the formulation material. |
| evidence need | Current support, uncertainty, contrary evidence, and the smallest question that could reverse or narrow it. |
| intervention logic | Action, inquiry, adaptation, or restraint families made plausible, without claiming effectiveness. |
| receiving-use consequence | Which model, alternative, comparison, scope, recommendation, or decision-support return would change. |

Where a durable formulation is used as a claim-bearing episteme, preserve its source and identity through the direct episteme pattern. Ordinary working sentences need no new root kind.

#### PSDA.1:4.4 - Test material plurality without ranking

Compare each pair only far enough to ask whether the difference changes a downstream move. Preserve incompatibility when one formulation requires evidence, values, boundaries, or interventions that another excludes. Record overlap when formulations can be investigated together.

Do not score, rank, vote, synthesize, or select unless another pattern and authority govern that result. `C.17` may characterize novelty, diversity, or use of an already-generated formulation set when that characterization is material. `C.18` applies only when the project must govern generation records, descriptors, archives, fronts, telemetry, or retained exploration value. Neither pattern supplies the PSM-specific construction of problem formulations.

#### PSDA.1:4.5 - Stop and return the plural formulation set

Stop when every retained formulation changes at least one named downstream move and another credible formulation would not change the current receiving use enough to justify its cost. There is no universal target count. A claim of plurality requires at least two materially different formulations; a case with only one adequate formulation should not manufacture a set.

Return the formulations, their contrasts, shared and disputed premises, evidence gaps, dependent next results, and reopen conditions. If a missing participant, concern, fact, source, or authority relation prevents a responsible formulation, return the exact gap, narrow the claim, request the bounded result, or abstain.

#### PSDA.1:4.6 - Pass plurality forward without creating a workflow

Pass the set to `PSDA.2` when included and excluded scope must be chosen, to `PSDA.3` when different models are needed, to `PSDA.5` when formulations imply different alternative families, and to `PSDA.17` when engagement activities obstruct a material formulation contribution. These branches may be concurrent. Pattern numbering is not a compulsory stage sequence.

Reopen locally when a new participant, concern, affected System, evidence result, value tension, intervention family, horizon, receiving use, or authority fact creates a materially different formulation or defeats one already retained.

#### PSDA.1:4.7 - What changes in practice

The practitioner stops asking participants to agree on one problem sentence before useful work begins. They can show a small set of genuinely different formulations, the evidence and actions each foregrounds, and the exact next result that plurality changes.

### PSDA.1:5 - Archetypal Grounding

#### PSDA.1:5.1 - Four formulations of the flood-pump situation

For the board's pre-season decision, the `PSDA.12` account supports four material formulations:

1. **Capacity shortage:** peak inflow can exceed available pumping capacity; flow, reliability, and deployment evidence matter; permanent or mobile capacity becomes salient.
2. **Unequal protection:** current arrangements shift flood exposure toward particular districts and mobility-constrained residents; distribution, access, and representation evidence matter; allocation and protection rules become salient.
3. **Maintenance fragility:** failures arise from maintenance, spares, staffing, and coordination dependencies rather than nominal pump count; readiness, contracting, and staged maintenance alternatives become salient.
4. **Unsafe deployment:** emergency placement and operation can create worker, resident, traffic, or downstream risks; safe operating envelopes and restraint branches become salient.

These are not synonyms. They imply different scope, evidence, model, alternative, and value work. The team keeps overlaps and conflicts visible and sends the set to `PSDA.2`; it does not vote for “the real problem” or infer that any intervention is effective.

#### PSDA.1:5.2 - Development-direction advice

For an AI-assisted incident-response arrangement, “model accuracy is inadequate”, “operator coordination is fragile”, and “authority escalation is unclear” imply different holders, evidence, intervention families, and safety questions. PSDA.1 retains all three only if each can change the two-quarter development recommendation. Generic slogans such as “improve AI capability” and “make the system better” fail the material-difference test.

#### PSDA.1:5.3 - Cheap non-use

A repair team has a verified broken seal, one affected assembly, one authorized repair decision, and no rival account that changes evidence or action. The live question is which qualified replacement to use. Generating plural problem formulations would add ceremony; proceed directly to comparison or choice.

### PSDA.1:6 - Bias-Annotation

**Scope:** plural problem formulation for one bounded decision-support inquiry. **Lenses:** **Gov** keeps framing influence and later choice authority distinct; **Arch** exposes how formulations change dependent results; **Onto/Epist** separates the situation, formulation, claims, evidence, and causal hypotheses; **Prag** requires material difference and a stopping rule; **Did** provides ordinary-language contrasts before formal models.

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| sponsor-frame bias | The opening brief becomes the only formulation. | Externalize it with sources and exclusions, then seek structural contrasts. |
| vocabulary bias | Synonyms are counted as plurality. | Require a changed boundary, evidence need, intervention family, value, or receiving-use consequence. |
| consensus bias | Participants must agree on one wording before inquiry. | Retain incompatible formulations and name their downstream differences. |
| causality bias | A framing hypothesis is reported as the cause. | State mechanism, support, uncertainty, and falsifying or narrowing evidence. |
| option leakage | Problem formulations become preselected solutions. | State intervention families as consequences of a frame, not proven answers. |
| endless-reframing bias | Every possible perspective stays live. | Stop when added formulations no longer change the named use enough to justify cost. |

### PSDA.1:7 - Conformance Checklist

- [ ] Every formulation concerns the same bounded subject and receiving use, or a different inquiry is explicitly separated; a changed professional engagement returns to `PSDA.11`.
- [ ] Material participants and concerns supplied by `PSDA.12` or other qualified direct sources are used as inputs without being treated as proof or settlement.
- [ ] Each retained formulation changes at least one boundary, evidence need, model, alternative family, value treatment, or receiving-use consequence.
- [ ] Sources, assumptions, exclusions, uncertainty, and intervention logic are visible.
- [ ] Causal, evaluative, legal, ethical, safety, and authority claims retain their direct assurance.
- [ ] The set is not ranked, selected, synthesized, or converted into a decision by this pattern.
- [ ] The stopping rule prevents both decorative plurality and endless reframing.
- [ ] Missing premises produce a gap, narrowed claim, request, blocker, or abstention.
- [ ] The result can feed `PSDA.2`, `PSDA.3`, `PSDA.5`, or `PSDA.17` without imposing a universal traversal order.

### PSDA.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Agree on the problem first.” | Agree on the receiving use; retain materially different problem formulations. |
| “Brainstorm ten frames.” | Keep only formulations that change a named downstream move. |
| “Every stakeholder gets a frame.” | Build coherent formulations from material differences; participation identity does not define one frame each. |
| “The most popular frame is true.” | Popularity establishes neither truth, causal support, value priority, nor authority. |
| “A novel wording is a new problem.” | Use the material-difference test; use `C.17` only if novelty characterization itself matters. |
| “The formulation set is an option archive.” | Use `PSDA.5` for decision alternatives and `C.18` for governed archives or fronts. |

### PSDA.1:9 - Consequences

Later models, boundaries, alternatives, and recommendations inherit visible framing assumptions instead of one hidden sponsor frame. Practitioners can investigate incompatible accounts without forcing premature consensus. The cost is explicit source and contrast work, and some engagements will stop because a framing premise cannot yet be supported.

### PSDA.1:10 - Rationale

Problem formulation is a field-specific generative move: it connects contested descriptions, concerns, values, evidence needs, and intervention logics to a receiving decision-support use. Generic candidate-set patterns can characterize or steward a set after generation, but they do not construct problem formulations. PSDA.1 therefore owns the smallest plural-formulation result while reusing direct FPF patterns for evidence, episteme identity, relations, set characterization, and authority.

### PSDA.1:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How should a practitioner preserve plural framing without losing a usable inquiry? | Treat framing as selection and organization of what matters, externalize materially different formulations, compare their consequences, and revise them as contextual evidence changes. | A fixed sponsor brief is the serious default; unconstrained perspective collection is the opposite default. | The first hides framing commitments and the second cannot stop. **Adapt:** `PSDA.1:4.1`–`4.5` requires structural contrasts, downstream materiality, sources, and a receiving-use stop. | Kelly and Gero's [2022 framing review](https://doi.org/10.1017/dsj.2022.25) supports multiple non-equivalent meanings of design framing; Litster, Cardoso, and Hurst's [2024 study](https://doi.org/10.1017/S089006042400012X) supports observation of changing externalized team framing; Nickel, Hurst, and Duimering's [2024 study](https://doi.org/10.1017/dsj.2024.34) supports contextual trade-offs. These sources establish neither one framing ontology, universal Method, shared team frame, prevalence, causality, nor superiority. | Reopen if later comparative evidence changes the best-known framing line or if contextual evidence materially changes a retained formulation. |
| What remains specifically PSM work after generic candidate handling is subtracted? | PSM practice retains the construction and facilitation of rival problem formulations for ill-structured situations; FPF supplies direct evidence, relation, identity, and later-choice governors around that result. | Treating formulation as generic brainstorming, alternative generation, or archive management is the serious default. | It loses the relation between a formulation and the concerns, boundaries, evidence, and intervention logic of the receiving inquiry. **Adopt:** the formulation face in `PSDA.1:4.3` and the pass-forward boundary in `4.6`. | Smith and Shaw's [2019 review](https://doi.org/10.1016/j.ejor.2018.05.003) and Kogetsidis's [2025 review](https://doi.org/10.1108/IJOA-08-2024-4746) support PSM as a continuing, diverse, facilitated branch for ill-structured situations. Current `C.17` characterizes novelty/diversity/use of a named set; current `C.18` governs open-ended generation, archives, fronts, descriptors, and telemetry. None proves that one PSM, formulation count, facilitation arrangement, or archive policy is universally sufficient or superior. | Reopen if a direct generic pattern acquires the full PSM-specific construction at equal or lower effort, or if PSM evidence changes the material plurality test. |

### PSDA.1:12 - Relations

- For a professional engagement, `PSDA.11` supplies the bounded subject, receiving use, horizon, recipient, and authority boundary. Use `PSDA.12` when material participation, affected Systems, concerns, duties, interests, or dissent need its professional construction; other inquiries can use adequate direct premises.
- `PSDA.2` receives the plural set when the current included/excluded problem boundary must be chosen. `PSDA.3` receives formulation-dependent model needs.
- `PSDA.5` receives formulation-dependent alternative families; it does not retroactively define the problem. `PSDA.17` can use the plural formulation set when deciding how to resolve material interference in the engagement.
- `C.17` may characterize novelty, diversity, or use of the generated set. `C.18` governs archive/front/generation-record stewardship only when those objects are actually needed.
- Direct episteme, evidence, relation, value, causal, legal, ethical, safety, governance, and choice patterns govern their own claims. PSDA.1 neither ranks the set nor authorizes the later choice.

### PSDA.1:End

## PSDA.2 - Set and Reopen the Problem Boundary

> **Type:** Method pattern body
> **Status:** Stable
>
> **Primary working result:** a **usable problem scope and reopen basis** for one bounded receiving inquiry: the formulations, participants, affected Systems, concerns, relations, conditions, horizons, and intervention families included now; material exclusions and unknowns; the basis the recipient needs to judge the cut; and observable conditions for widening, narrowing, or otherwise revising it.


### PSDA.2:1 - Problem frame

Use this pattern when a decision-support inquiry either expands toward everything connected with the situation or excludes a concern, bearer, relation, horizon, or intervention family that could reverse the usefulness of the result. Use it after or alongside `PSDA.1` when plural formulations imply different boundaries.

Choose the smallest boundary that supports the named receiving decision or Work, make consequential exclusions visible, and state how the boundary can reopen. The practical gain is an actionable scope without pretending that what lies outside is false, irrelevant forever, or unaffected.

Do not use PSDA.2 merely to decide whether one exact `U.ContextSlice` belongs to an already-declared `U.Scope`; use `A.2.6` for that claim. Do not use it for generic document scope, organizational jurisdiction, a System boundary owned by a direct engineering practice, or a static project charter when no problem-structuring question remains. Return an unclear receiving question before setting its boundary; use `PSDA.11` when the missing question concerns a professional engagement.

#### PSDA.2:1.1 - Working Distinctions

| Working term | Meaning in this pattern |
| --- | --- |
| engagement boundary | The `PSDA.11` boundary around the decision-support return, recipient, subject, horizon, receiving use, and authority. |
| problem boundary | The provisional cut that determines which formulations, bearers, concerns, relations, conditions, horizons, evidence, and intervention families are treated as material now. |
| material exclusion | An omitted or deferred item that could change the current result and therefore must remain visible with a reason, uncertainty, and reopen condition. |
| usable scope | The smallest current problem boundary adequate for a named next result and its assurance burden. It need not be exhaustive or permanent. |
| reopen basis | An observable change or newly recoverable value that can make the current boundary too narrow, too broad, or otherwise unfit for the receiving use. |
| `U.Scope` | A declared scope for exact `U.ContextSlice` membership, governed by `A.2.6`. An ordinary problem boundary need not be reified as one. |

Every formulation makes a cut. It foregrounds some participants, Systems, concerns, causal or modal paths, operating conditions, time horizons, evidence, and intervention families while leaving others outside. In ill-structured situations those cuts are often contested and revisable rather than simply discovered.

The primary concern is not to find the one true perimeter. It is to choose and expose a boundary adequate for one receiving use while preserving the exclusions and observations that could require revision. Recognition can begin with one plausible boundary reversal. Consequential inclusion, exclusion, relation, harm, authority, legal, ethical, safety, or factual claims retain their direct assurance.


### PSDA.2:2 - Problem

An implicit sponsor boundary hides who and what the inquiry sacrifices. A comprehensive “whole system” map creates the opposite failure: every related condition enters, no stopping rule survives, and the receiving decision disappears. An exact scope declaration can conceal that the underlying inquiry cut remains contestable.

Once models and data collection begin, their available variables make the boundary appear natural. Excluded concerns then vanish rather than remaining explicit deferrals. A later observation is treated as noise instead of evidence that the inquiry should widen, narrow, or change formulation.

### PSDA.2:3 - Forces

| Force | Tension |
| --- | --- |
| Actionability | A current cut is needed to proceed, while premature closure can reverse the result. |
| Completeness | Wider scope can reveal consequences, while unlimited scope destroys affordability and accountability. |
| Explicit exclusion | Material omissions must stay visible, while a boundary register should not become an encyclopedia. |
| Stability and revision | Dependent work needs a current scope, while new evidence can legitimately reopen it. |
| Exact membership | Exact contextual membership sometimes matters, while ordinary problem boundaries need not become `U.Scope` values. |
| Authority | A boundary can inform later work, while it does not authorize the later decision or erase specialist jurisdiction. |

### PSDA.2:4 - Solution

Set the problem boundary relative to one receiving use and one or more current formulations. Name what is included, material exclusions or unknowns, and the observable changes that can reopen the cut. Keep the reason for its adequacy where the recipient needs it to judge or use the scope. Use `A.2.6` only when a receiving claim depends on exact `U.ContextSlice` membership in a declared `U.Scope`.

#### PSDA.2:4.1 - Fix the receiving use and current formulations

Recover the subject, receiving question or Work and horizon from a qualified source for the same inquiry. Name the recipient and later choice owner where the use has them. A current `PSDA.11` engagement question can supply these premises for professional use. Name the `PSDA.1` formulations whose consequences the boundary must preserve. Use one adequate current formulation directly when plural formulations are unnecessary. Keep a materially contested exclusion or boundary reason in the scope where it can change the receiving use.

Use a current `PSDA.12` account where participants, affected Systems, concerns, duties, interests, dissent, representation limits, or possible consequence paths can challenge the cut. Inclusion in that account does not require inclusion in every current model or analysis; exclusion from the boundary does require an honest reason when material. When an input needed for the cut is unavailable, stale, or incompatible, obtain a qualified direct result or return the exact missing premise. A formulation alone does not establish current representation or choice authority.

#### PSDA.2:4.2 - State the boundary through decision-bearing dimensions

Name only dimensions that can change the receiving use:

- subject, configuration, place, population, and operating condition;
- included formulations and affected bearers;
- concerns, duties, interests, relations, dependencies, and consequence paths;
- evidence interval, uncertainty, and time horizon;
- intervention, adaptation, restraint, and no-action families; and
- participating, receiving, implementing, and choice-authority positions where material.

Carry forward the object distinctions recovered with the concerns. If “business trip” names both remote repair and administrative provision, say which work this inquiry concerns and which dependencies it includes. A boundary around expense processing cannot support a conclusion that the remote repair was completed. Several concerns about one identified journey can instead share that object boundary.

State the cut in ordinary language; add an exact `U.Scope` declaration only when the receiving use needs it. A boundary is not justified by drawing a box or using the word “system”.

#### PSDA.2:4.3 - Keep material exclusions and unknowns alive

For every omitted item that could change a downstream result, record the item, exclusion reason, current evidence or uncertainty, consequence of being wrong, and reopen observation. Distinguish:

- outside for this receiving use from irrelevant in general;
- deferred from rejected;
- unknown membership from supported non-membership;
- absent evidence from evidence of absence; and
- a practical stopping decision from a claim that no relation or consequence exists.

Items with no plausible consequence for the current use need not receive a full record. Items that can reverse a high-consequence result require proportionate direct assurance or an explicit stop.

#### PSDA.2:4.4 - Challenge the cut before accepting it

Apply the smallest relevant challenges:

1. **bearer challenge:** could a participant or affected System outside the cut undergo a material change?
2. **formulation challenge:** would another retained formulation include a different mechanism, value, horizon, or intervention family?
3. **action challenge:** does the cut make one alternative appear necessary by excluding feasible restraint, adaptation, or no-action branches?
4. **evidence challenge:** are data availability or model convenience defining the boundary?
5. **authority challenge:** does the cut silently transfer a duty, jurisdiction, implementation burden, or later choice?
6. **reversal challenge:** what smallest observation would make the current result unusable or materially different?

Repair only the affected dimension. A challenge does not require maximal widening.

#### PSDA.2:4.5 - Use exact scope membership only when needed

When a downstream claim depends on whether one exact `U.ContextSlice` belongs to one declared `U.Scope`, use `A.2.6`. Distinguish an evaluation result of true, false, or unknown. Unknown means the available basis cannot decide; obtain the missing input, narrow the attempted use, or abstain instead of asserting exclusion. Changing the extension creates a new scope; a refit that preserves the extension does not.

Do not force every ordinary concern or participant into `U.Scope`. PSDA.2 governs the field-specific judgement that a problem boundary is usable for the current inquiry; `A.2.6` governs exact contextual membership. A `C.2.3` formality threshold concerns how strictly a claim is expressed and is selected separately, only when the receiving use needs it.

#### PSDA.2:4.6 - Return the usable scope and reopen basis

Return the scope in the smallest form that answers the current question. Keep the following content where it changes the recipient's understanding or reliance; a local clarification can finish in the scope itself.

| Result position | Content needed by the recipient |
| --- | --- |
| receiving use | Subject, receiving question or Work and horizon; recipient and retained choice owner where the use has them. |
| formulation basis | Current formulations and the material differences the boundary preserves. |
| included scope | Bearers, concerns, relations, conditions, horizons, evidence, and intervention families included now. |
| exclusions and unknowns | Material omissions or uncertainties, reasons, consequences of error, and direct assurance still needed. |
| adequacy reason, where needed | Why this is the smallest usable scope, when the recipient needs that basis to judge the cut or avoid mistaking an exclusion for a settled fact. |
| dependent uses | Models, facilitation, alternatives, value treatment, comparison, recommendation, or inquiry results that consume the scope. |
| reopen basis | Observable triggers and the dimension to widen, narrow, replace, or re-formulate. |

If no defensible boundary is available, return the exact missing premise, blocker, narrowed claim, or abstention. Do not hide the stop by expanding the map.

#### PSDA.2:4.7 - Reopen locally and state what changed

Reopen when a new participant, affected System, concern, formulation, relation, operating condition, evidence result, value tension, intervention family, horizon, receiving use, or authority fact can change the current result. Name the old boundary, new observation, affected dimension, and dependent result.

Widen, narrow, or replace only that portion. If a declared `U.Scope` or a relied-upon membership result changes, apply `A.2.6`; if the receiving use changes, separate or revise the inquiry, returning a changed professional engagement to `PSDA.11`; if a new formulation is needed, return to `PSDA.1`.

#### PSDA.2:4.8 - What changes in practice

The practitioner stops treating scope as either the sponsor's box or an ever-growing map. They can state a small usable cut, defend why exclusions are tolerable now, and show the precise observation that would reopen each consequential part.

### PSDA.2:5 - Archetypal Grounding

#### PSDA.2:5.1 - Flood-pump boundary

For the board's pre-season decision, the current boundary includes the district pumping arrangement, permanent and mobile capacity, maintenance and staffing dependencies, deployment safety, district access, the next flood season, and material downstream transfer paths. It preserves all four `PSDA.1` formulations rather than reducing the inquiry to pump count.

Long-term watershed redesign and permanent residential relocation are outside the current investment return, but they are not declared irrelevant. Relocation rights and downstream consequences remain material exclusions because they can reverse a recommendation. The boundary records that verified cross-district flood transfer, a safety limit outside the assumed operating envelope, or evidence that no feasible pump branch protects mobility-constrained residents will reopen the relevant dimension.

The result is usable for model and alternative work. It does not authorize funding, assert that every included consequence obtains, or make the emergency board competent to settle legal, ecological, or safety questions.

#### PSDA.2:5.2 - Narrowing after a failed generalization

An incident-response inquiry initially covers all product lines. Evidence shows that the proposed escalation pattern applies only to one regulated line and one staffing configuration. The practitioner narrows the problem boundary and dependent recommendation instead of claiming organization-wide use. Other lines remain explicit unknowns with their own reopen conditions.

#### PSDA.2:5.3 - Cheap non-use

A laboratory test claim already has a declared `U.ClaimScope` with population, configuration, and interval selectors. The live issue is whether one proposed test's `U.ContextSlice` belongs to that scope. Use `A.2.6` directly. PSDA.2 adds no problem-structuring judgement.

#### PSDA.2:5.4 - One adequate formulation and a consequential exclusion

An analyst and a maintenance lead already share the formulation “why are the authorized pump checks late?” Their immediate clarification is whether to examine this week's check queue or expand into redesigning the whole maintenance organization. The available queue and assignment facts support the first cut. The analyst returns: “Examine this week's authorized checks, their staffing and access dependencies, and the late returns.” This scope answers the local question; it needs no new rival-formulation inquiry or separate explanation of why PSDA.1 was not used.

A later board asks whether the same result establishes readiness for the flood season. Now the exclusion of uncompleted seasonal checks can change its decision. The returned scope must retain that those checks were outside the weekly lateness inquiry and that their readiness remains unestablished. The board needs the seasonal check result before relying on a readiness claim. This added limitation serves the new receiving use; it does not undo the supported weekly scope or authorize operation.

### PSDA.2:6 - Bias-Annotation

**Scope:** provisional problem boundaries for a named decision-support use. **Lenses:** **Gov** keeps inclusion, jurisdiction, and choice authority separate; **Arch** exposes dependencies on the cut; **Onto/Epist** distinguishes situation, formulation, ordinary boundary, declared `U.Scope`, and evidence; **Prag** seeks the smallest usable scope; **Did** makes exclusions and reopen cues readable without a specialist notation.

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| sponsor-boundary bias | The brief's perimeter becomes unquestionable. | Challenge it with bearers, formulations, actions, evidence, authority, and reversal. |
| map-completeness bias | More nodes are treated as better scope. | Require each included dimension to change the receiving use. |
| data-availability bias | Available variables define the problem. | Record excluded concerns and evidence gaps independently of the model. |
| box-as-ontology bias | A drawn perimeter is treated as proof of a System boundary or exact scope membership. | State the ordinary decision-support cut; use the direct engineering practice for a System-boundary claim and `A.2.6` for contextual membership when either is needed. |
| exclusion-as-falsehood bias | Outside the current inquiry becomes “does not matter”. | Record material exclusions, uncertainty, consequence, and reopen basis. |
| boundary-freeze bias | Later contrary evidence is absorbed without revising scope. | Reopen the smallest affected dimension and dependent results. |

### PSDA.2:7 - Conformance Checklist

- [ ] The boundary is tied to one receiving use, subject, horizon, and authority boundary.
- [ ] Current formulations and material participation or affected-System inputs are recoverable.
- [ ] Included bearers, concerns, relations, conditions, evidence, horizons, and intervention families are stated only at the needed grain.
- [ ] Material exclusions and unknowns retain reasons, consequences of error, and reopen observations.
- [ ] The bearer, formulation, action, evidence, authority, and reversal challenges were applied proportionately.
- [ ] The result carries the reason for the cut where the receiving use needs it, including any materially contested exclusion.
- [ ] Ordinary problem-boundary judgement is not confused with exact `U.ContextSlice` membership in `U.Scope`.
- [ ] Missing premises produce a gap, narrowed claim, request, blocker, or abstention.
- [ ] Reopening changes the smallest affected dimension and identifies dependent results.
- [ ] The scope neither authorizes the later choice nor displaces direct legal, ethical, safety, scientific, engineering, or governance practices.

### PSDA.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Everything is connected, so include everything.” | Include only what can change the named receiving use; preserve material exclusions and triggers. |
| “Outside scope means irrelevant.” | State outside-for-now, consequence of error, and reopen condition. |
| “The model boundary is the problem boundary.” | Let formulations and concerns challenge available variables and model convenience. |
| “Draw the system boundary.” | Name the problem-structuring cut; establish any System-boundary or exact contextual-membership claim through its direct pattern. |
| “Unknown means excluded.” | Separate true or false membership from an unknown evaluation; unknown does not establish exclusion. |
| “Scope was agreed at kickoff.” | Reopen when the named observation can change the receiving result. |

### PSDA.2:9 - Consequences

The inquiry becomes bounded enough to support models, alternatives, comparison, and recommendation while keeping consequential omissions recoverable. Revision can be local rather than a complete restart. The cost is explicit exclusion work and occasional narrowing, widening, or stopping when a premise cannot be assured.

### PSDA.2:10 - Rationale

Problem boundaries are practical framing commitments. A discovered perimeter or exact membership test alone does not establish that a cut is adequate for a receiving inquiry. PSDA.2 contributes that PSM-specific judgement and preserves the conditions under which the cut must change. `A.2.6` remains the direct owner of exact contextual membership when that stronger claim is needed.

### PSDA.2:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How should a problem boundary remain useful and revisable? | Treat framing as a contextual selection of what matters, compare materially different cuts, state exclusions, and revise the boundary when new evidence changes the receiving use. | A fixed sponsor scope is the serious default; an unbounded whole-situation map is the opposite default. | The first suppresses consequential exclusions and the second cannot stop. **Adapt:** `PSDA.2:4.1`–`4.4` and `4.6` require decision-bearing dimensions, material exclusions, proportionate challenges, and the scope reason needed by the receiving use. | Kelly and Gero's [2022 framing review](https://doi.org/10.1017/dsj.2022.25), Litster, Cardoso, and Hurst's [2024 mapping study](https://doi.org/10.1017/S089006042400012X), and Nickel, Hurst, and Duimering's [2024 contextual trade-off study](https://doi.org/10.1017/dsj.2024.34) support explicit framing, externalized change, and contextual trade-offs. They establish neither one framing ontology, universal Method, shared frame, fixed boundary, prevalence, causality, nor superiority. | Reopen if later field evidence changes the best-known boundary practice or if new contextual evidence changes an included or excluded dimension. |
| When does a receiving use need exact contextual scope membership? | Keep ordinary inquiry cuts in plain language; use current `A.2.6` only when the receiving use must decide whether one exact `U.ContextSlice` belongs to one declared `U.Scope`. | Treating every diagram box or topic perimeter as a declared exact scope is the serious default. | It substitutes apparent precision for boundary judgement and can hide unavailable evaluation. **Adopt:** `PSDA.2:4.5` distinguishes true, false, and unknown evaluation results and routes extension changes to the direct pattern. | Current `A.2.6` supplies exact contextual membership, extension change, and refit discipline. Its applicability axis is independent of `C.2.3` formality. It does not judge which participants, concerns, formulations, intervention families, or exclusions make a PSM boundary usable. Direct engineering, legal, safety, ethical, and governance practices retain their own boundaries and thresholds. | Reopen if the direct scope pattern gains the complete problem-boundary judgement at equal or lower effort, or if a relied-upon scope or membership result changes. |

### PSDA.2:12 - Relations

- `PSDA.11` supplies the identity and authority boundary of a professional engagement when one is involved. `PSDA.12` supplies participation, concern, and affected-System challenges where those professional results are needed. `PSDA.1` supplies the plural formulation set whose differences the boundary must preserve.
- `PSDA.3` and `PSDA.4` receive the scope and formulation basis for modeling and PSM-arrangement questions. `PSDA.17` receives the scope and reopen basis for resolving material interference among simultaneous work contributions in a decision-support engagement.
- `A.2.6` governs exact `U.ContextSlice` membership in a declared `U.Scope` when that claim is needed. `A.1.CSD` supplies consequence-bearer challenges; exact relations remain with their direct governor.
- Direct evidence, legal, ethical, safety, scientific, engineering, governance, assignment, and authority patterns govern their own claims. PSDA.2 neither establishes those results nor authorizes the later choice.

### PSDA.2:End

## PSDA.3 - Construct Complementary Situation and Option Models

> **Type:** Method pattern body
> **Status:** Stable
>
> **Primary working result:** a **multi-model decision account**: the smallest useful set of situation and option models, the questions each answers, their correspondences and limits, and the claims or unresolved questions that a named receiving inquiry may use.

### PSDA.3:1 - Problem frame

**Use this when** one diagram, spreadsheet, simulation, or agreed story is being asked to explain a contested situation, represent everyone's concerns, predict consequences, and identify the best intervention. Also use it when several models exist but their different subjects, assumptions, or meanings make their combined result unclear.

Start with the question that could change the next decision-support move. Choose a model that can answer it, then add another only for a material question the first cannot answer. The gain is a usable account of complementary and conflicting findings, not a larger model collection.

The governed object is that bounded account of model contributions. A model makes selected claims about a subject; a diagram, table, or screen expresses some model content; the people, pumps, service arrangements, and possible changes being considered remain the subjects. The account connects these without making them one object.

**Do not use this pattern** when one already-qualified calculation or model answers the entire receiving question and no material contrast remains. Use the direct modeling, engineering, scientific, or evidence practice for its own validity question. Return to problem formulation or boundary work when the difficulty is that nobody can say what the models should help decide.

### PSDA.3:2 - Problem

A capacity calculation cannot show whose service standard should govern. A rich picture can reveal attributed concerns without estimating a failure probability. A scenario can expose a vulnerable condition without predicting how often it will occur. Treating any one of these as a complete account hides questions it was never built to answer.

Adding models does not automatically repair the loss. Two models may reuse the same data, employ incompatible units or populations, or label different quantities “risk”. Agreement can be duplicated error; disagreement can reflect different questions rather than a defect. A composite dashboard can conceal both.

### PSDA.3:3 - Forces

| Force | Tension |
| --- | --- |
| Discrimination | Each model should change a claim, alternative, or inquiry priority, while exploratory models may first reveal what question matters. |
| Plurality | Material perspectives deserve distinct expression, while collecting every imaginable model makes the engagement unaffordable. |
| Correspondence | Related models need interpretable connections, while forced translation can erase their different meanings. |
| Credibility | Consequential reliance requires qualified evidence, while a preliminary model can still be useful for recognizing a missing premise. |
| Revision | A shared boundary permits comparison, while a model may reveal why that boundary must reopen. |

### PSDA.3:4 - Solution

Build a question-led set of complementary models. For each, state its subject, intended use, assumptions, evidence, and what it omits. Compare only the overlapping claims whose meanings can be aligned, retain material differences, and return the usable claims together with their limits.

#### PSDA.3:4.1 - Recover the questions and current boundary

Use the plural formulation set from `PSDA.1` where its differences identify claims or intervention logics that models must discriminate. A formulation is an interpretation of the problem, not already a validated model of the situation. Use the `PSDA.2` scope and reopen basis for the same subject, receiving decision, operating conditions, and horizon.

These are conditional inputs, not compulsory earlier stages. A qualified direct source may supply the needed formulation or scope. If a needed result is unavailable, stale, outside the present use, or incompatible, return its exact missing premise or narrow the inquiry; do not infer it from the presence of another model.

Turn the live differences into questions, such as “Does this arrangement retain service when road access is lost?” and “Whose loss is omitted by the aggregate service measure?” Keep question, assumed condition, and proposed intervention separate.

#### PSDA.3:4.2 - Choose complementary contributions at the needed grain

Consider what each model can actually contribute before selecting a notation or tool.

| Needed contribution | A possible model | Limit to preserve |
| --- | --- | --- |
| Make different interpretations and concerns discussable. | A rich picture, purposeful-activity model, or attributed cognitive map. | It expresses selected interpretations; agreement with the drawing is not agreement with an intervention or proof of a causal relation. |
| Examine a proposed mechanism or dependency. | A causal, stock-and-flow, network, or dependency model. | An arrow may be a hypothesis or structural assumption. A causal claim requires its direct evidence. |
| Explore changed conditions and intervention responses. | A scenario or conditional simulation. | A scenario is not a probability estimate; a simulated response depends on the model and inputs. |
| Expose objectives and distinguish consequences. | An objectives hierarchy, criteria model, or consequence table. | The arrangement does not supply legitimate weights, commensurability, or permission to trade one concern against another. |
| Test a technical feasibility premise. | A domain calculation or qualified engineering model. | Feasibility holds only within its configuration, operating envelope, evidence, and uncertainty limits. |

Select the smallest set that covers the material questions. A qualitative model may reveal a question worth quantifying; a numerical model may reveal a missing qualitative distinction. Neither direction is a universal order. Drop a model that supplies no distinct contribution unless its independently grounded evidence is needed to challenge another.

A concern map can already complete the task of making participants' concerns discussable. When another material question asks what causes an outcome or what an intervention would change, use an adequate causal model directly. If the causal relations still need to be constructed or compared, `C.28.CM` helps turn the relevant subject knowledge and mechanism accounts into explicit models for that question. Return their assumptions, conditional consequences and unresolved alternatives to the combined account. Keep each existing model for the question it can answer; the constructed causal model still needs the claim-specific assurance in :4.5.

When the question concerns participants' intentions, their dependence on one another and possible alternatives, the Reference's [goals-and-dependencies walkthrough (Engineering.Reference:20)](Engineering%20DPF%20Suite/ENGINEERING-DPF-SUITE-REFERENCE.md#engineeringreference20---explore-a-situation-through-goals-and-dependencies) develops an actors-and-goals model from a service difficulty. It explains how to select what a view reveals, turn a question into analysis assumptions, interpret the answer and return to an omitted assignment when the result exposes a conflict. Use that connected account when these joins need explanation; a sufficient existing model can be used directly.

#### PSDA.3:4.3 - Make each model's use intelligible

A reader should be able to say: “This model concerns this subject, answers this question under these conditions, and supports this limited use.” Supply the assumptions, evidence source and interval, important omissions, and an observation that would invalidate or narrow that use. Identify the exact model content or edition when a changed value could alter the result.

For a mathematical formalism, simulation, or learned representation, apply `C.29` when the choice of mathematical object, mapping, preserved structure, or information loss changes the claim. For example, a road graph can preserve routes and travel-time assumptions while omitting residents' access rights and the reliability of an untested deployment procedure. C.29 does not establish those omitted facts.

Ordinary local meaning needs only the relevant meaning, units, scope, or evidence statement. Use `A.1.1` when the decision needs to establish whether a model applies to a stated subject within a stated claim scope, whether an assignment holder actually uses the model during Work concerning that subject, or whether fixed model and expression contents satisfy a declared coherence criterion under a comparison scheme. Select its broader bounded model-use structure only when the organization of those relations changes the receiving decision. Neither a model collection nor the word “context” supplies that structure.

#### PSDA.3:4.4 - Reconcile overlaps without forcing one model

For each overlap that matters, compare the subject and configuration, population, time horizon, units, definitions, assumptions, and evidence dependencies. Establish whether the models concern the same object or different related objects before treating them as views of one thing. For example, a travel-expense model and a repair-performance model can concern different work commonly called a business trip; matching that label does not equate their completion conditions. State an actual correspondence only as far as the objects and meanings support it. If “service failure” means lost pumping capacity in one model and inability to reach a refuge in another, keep the meanings distinct and ask whether a further relation can be established.

Classify a consequential mismatch before repairing it: different questions, different assumptions, incompatible meanings, contradicted evidence, or a genuine unresolved conflict. Correct a unit or input error locally. Retain alternative assumptions when their truth is not known. When the conflict can reverse the receiving result, compare an obtainable direct investigation with retaining the qualified alternatives or narrower answer through `C.11.DUA`. Use `A.15.9` for a selected outside-practice contribution, including its whole acquisition burden.

Do not average unlike outputs, infer a shared probability from scenario counts, or count models drawing on one dataset as independent confirmation. A combined explanation may show how models inform one another without claiming that they form one unified model.

#### PSDA.3:4.5 - Match assurance to the claim being used

Recognition can begin with a sketch and a plausible contrast. Before consequential reliance, inspect the claims that bear the result: source qualification, implementation or calculation correctness, fitness to the intended use, validation evidence, sensitivity, and extrapolation limits as applicable. The direct domain practice determines what is sufficient; this pattern supplies no universal validation threshold.

Separate confidence in the modeler, internal consistency, empirical adequacy, robustness to assumptions, and authority to decide. A stakeholder's confidence can affect whether a model is used, but cannot substitute for evidence. A model that cannot yet support a recommendation may still support the narrower result “this conclusion depends on an unresolved assumption”. That limit does not itself select a test.

Return a qualified claim, a narrowed use, or an explicit inability to discriminate; include an evidence request when its contribution warrants acquisition. Where an unresolved safety, rights, legal, or technical premise blocks the proposed reliance, retain that stop. A stronger use needs its direct competent result; obtaining it remains a separate feasible and worthwhile continuation.

#### PSDA.3:4.6 - Return the account and its reopen basis

Keep enough content for the recipient to recover:

- the subject, question, receiving use, configuration, and horizon;
- each selected model's distinct contribution, current content, source basis, assumptions, and losses;
- the material correspondences, conflicts, and shared evidence dependencies;
- what the account supports, what remains hypothetical or unknown, and which alternatives or claims it can discriminate; and
- the observation that would reopen a model, its connection to another, the problem formulation, or the boundary.

This can be a short annotated comparison; it need not be a new repository or universal record form. If no model combination answers the question, say so. A missing direct result is more useful than a polished but unsupported combined answer.

The same account may inform Method selection, alternative generation, uncertainty treatment, or conflicts between simultaneous inquiries. Each recipient takes only the current, compatible contribution it needs; the account does not complete those later judgements.

#### PSDA.3:4.7 - What changes in practice

Instead of asking which model is “the right one”, the practitioner asks which claims need a model, what each selected model contributes, and which difference would change the next move. Models can remain usefully plural while their overlaps and limits are explicit.

### PSDA.3:5 - Archetypal Grounding

#### PSDA.3:5.1 - Flood-pump models that answer different questions

In this illustrative continuation of the flood-pump inquiry, the board needs a pre-season decision-support return about permanent pumps, mobile capacity, maintenance, staffing, and access. The current formulations distinguish capacity shortage, deployment reliability, unequal service, and transferred downstream consequences. The scope includes the next flood season and preserves relocation rights and long-term watershed change as material exclusions.

The inquiry team constructs the following bounded account. The values are illustrative case premises, not engineering advice.

| Question and model | Account slice | Consequence for inquiry |
| --- | --- | --- |
| Can nominal capacity meet the assumed inflow? A capacity calculation. | Permanent and mobile branches meet the assumed requirement only with the stated operating units available; no deployment delay is represented. | Nominal capacity alone cannot discriminate reliability or access. |
| Can mobile units reach and serve the district? An access-and-deployment scenario model. | With the main road unavailable, the mobile branch has no supported arrival-time claim. A second route is a hypothesis requiring an operations result. | Keep the mobile branch conditional; arrival time remains unsupported. A route/deployment request is selected only if its obtainable contribution warrants acquisition for this decision. |
| What counts as adequate service, and for whom? An attributed concern map. | The residents' association emphasizes property protection. A separately heard group of mobility-constrained residents requires reachable assistance. Neither statement represents all residents. | Preserve the two service meanings; the hydraulic output does not settle their relation or priority. |

The account returns: “Nominal capacity is not presently the discriminating uncertainty. The mobile branch depends on an unqualified access premise. The service comparison must retain both property protection and reachable assistance.” It does not rank the branches.

If verified access evidence closes the transport gap, only the affected model claim and its dependent uses reopen. If no feasible pump branch supports the service concern, the problem boundary reopens. Repeated use of the same inflow dataset by both technical models supplies one evidence dependency, not two confirmations.

Suppose the board additionally asks whether securing an alternative road would get mobile pumps operating sooner during a main-road closure. Two mechanisms remain plausible: road access delays an otherwise ready crew and pump, or the flood also disables power at the staging site, preventing pump preparation even with another road. Use the causal-construction branch in :4.2 to compare road availability, pump-and-crew readiness and time to operation under the same assumed flood conditions. In the first account a usable alternative road removes the named access delay; in the second, preparation remains a limiting condition. These are conditional consequences of the proposed mechanisms. The scenario provides no evidence to choose between them or assert an arrival time.

Return the narrowed answer: another road could remove the access delay, while pump preparation remains a premise that can change its practical benefit. An operations result about readiness and the alternative route could resolve that distinction; :4.4 governs whether obtaining it is worthwhile. The residents' two service meanings remain as stated in the concern map.

#### PSDA.3:5.2 - Development advice across two holders

An adviser compares a training direction for two service teams. A skills map suggests similar learning needs, but each team's queue model uses its own demand and staffing evidence. The combined account keeps those holders separate: an improvement simulated for Team A supplies no performance claim for Team B.

For Team B, retain the plausible training direction with its unknown demand and performance contribution; Team A's benefit estimate does not transfer. A trial is a further choice whose attainable contribution must warrant its burden. More detailed modeling of Team A would not repair the absent Team B evidence.

#### PSDA.3:5.3 - Cheap non-use

A technician needs one conversion under an already-qualified formula, with agreed units and no material uncertainty about applicability. Use that calculation directly. A rich picture, scenario set, and second model would add no discriminating result.

### PSDA.3:6 - Bias-Annotation

**Scope:** models supporting bounded problem-structuring and decision-support questions. **Lenses:** **Onto/Epist** separates subject, model, expression, and evidence; **Prag** selects useful discrimination; **Arch** exposes model connections; **Gov** preserves later choice and direct authority; **Did** makes different model contributions readable.

Model-prestige bias favors the most technical representation. Agreement bias counts correlated outputs as corroboration. Model-availability bias turns measurable variables into the whole problem. Counter these by naming each model's question, inspecting shared assumptions and evidence, and keeping material unmodeled concerns visible. Plurality itself can become a bias: remove a redundant model when it changes no claim or assurance need.

### PSDA.3:7 - Conformance Checklist

- [ ] The account serves a named subject, question, receiving use, configuration, and horizon.
- [ ] Needed formulation and scope inputs are current and compatible, or their exact gaps are returned.
- [ ] Each model supplies a distinct useful contribution; one sufficient model remains a valid cheaper exit.
- [ ] The subject, model content, expression, evidence, and possible intervention remain distinguishable.
- [ ] Assumptions, important losses, and limits accompany every relied-on output.
- [ ] Material overlaps are compared by meaning, scope, units, and evidence dependency; unresolved differences are not averaged away.
- [ ] Mathematical-lens and actual model-use claims receive their direct treatment only when needed.
- [ ] Recognition, validation, confidence, causal evidence, and authority are not substituted for one another.
- [ ] The returned account identifies usable claims, unresolved discriminating questions, and local reopen conditions.

### PSDA.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “The simulation represents the situation.” | State the exact question, represented conditions, and omitted concerns. |
| “Three models agree, so the evidence is stronger.” | Recover whether their assumptions, data, or implementation errors are shared. |
| “Every perspective needs its own complete model.” | Retain only perspectives whose difference changes a present claim or use; use a smaller expression where sufficient. |
| “The qualitative map supplies the probabilities.” | Keep attributed beliefs separate from calibrated evidence; the missing calibration limits the claim, and acquisition needs its own receiving value. |
| “Consistency means validity.” | Test the relevant model-to-world claim through the direct practice. |
| “C.29 governs every picture.” | Open its mathematical-lens branch only for a real mathematical-lens choice that changes use. |

### PSDA.3:9 - Consequences

The recipient sees which model can answer which question and where the combined account stops. Contradictions can guide inquiry instead of being hidden by one score. The cost is explicit assumptions and correspondence work; limit that work to overlaps that could alter the result. A smaller qualified answer may replace an apparently comprehensive conclusion.

### PSDA.3:10 - Rationale

Complementarity is a relation between useful contributions to a question, not a model count. Purpose-led selection and explicit loss preserve different interpretations while making technical claims inspectable. Separate assurance keeps a useful representation from becoming unearned evidence about the world.

### PSDA.3:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How should models contribute jointly without hiding their different meanings? | Select models by the questions they answer and inspect the joins between problem structuring and analysis. | One comprehensive model is the serious default; an unconstrained collection is the rival expansion. | **Adapt:** `PSDA.3:4.1`–`4.4` choose the smallest complementary set and expose incompatible meanings. Compared with expanding one model, this deliberately accepts some correspondence work to preserve a material concern that the single model omits; it makes no universal claim of lower cost. | Marttunen, Lienert, and Belton's [2017 review of PSM–MCDA combinations](https://doi.org/10.1016/j.ejor.2017.04.041) is a critical synthesis candidate for combination benefits and interface difficulties, including value-tree and weighting issues. Its reviewed applications are not controlled evidence that more models are better or that one combination fits every inquiry. The question-led selection and non-use rule are PSDA adaptations. | Reopen if a simpler model answers the same material questions with equivalent limits, or a new mismatch shows that the chosen combination loses a consequential meaning. |
| What justifies relying on a model-supported claim? | Qualify the intended use, evidence, and losses separately from confidence in the model or its producer. | Technical sophistication, modeler reputation, or participant confidence is treated as sufficient credibility. | **Adapt:** `PSDA.3:4.3`–`4.6` and the flood-pump case retain applicability, evidence dependencies, and unresolved assumptions. The extra assurance effort is accepted only where it can change reliance; sketches remain usable for recognition. | Schwarzburg, Trauer, and Rebentisch's [2024 confidence study](https://doi.org/10.1017/dsj.2024.14) supplies bounded empirical evidence that model-, modeler-, and stakeholder-related factors are associated with confidence and reliance. Its exploratory survey and proposed application model do not validate a particular decision model or establish causal decision quality. Current `C.29` supplies mathematical mapping and loss discipline, not validation, causality, or authority. `A.1.1` supplies the three model relations used above; it applies only when their claims matter to the decision. | Reopen when direct validation contradicts a relied-on claim, the use leaves its qualification window, or a current modeling practice offers the same assurance at materially lower effort. |

### PSDA.3:12 - Relations

- `PSDA.1` supplies formulations only where their differences guide model discrimination. `PSDA.2` supplies the scope and reopen basis for the same subject and decision. Missing needed values require qualified direct sources or an exact gap.
- `PSDA.4`, `PSDA.5`, and `PSDA.17` may use the model account to discriminate their Method, alternative, or simultaneous-inquiry claims. Representation does not make the represented condition obtain.
- `PSDA.7` may use the account's evidence only for the same configuration and horizon; that evidence neither entails its uncertainty judgement nor authorizes action.
- `C.29` governs load-bearing mathematical-lens use. `A.1.1` governs claims about a model's applicability, its actual use in assigned Work, and the coherence of fixed model and expression contents under a declared criterion and comparison scheme. Direct scientific, engineering, causal, and evidence practices retain their own truth and adequacy questions.
- [FPF C.28.CM](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c28cm---construct-and-challenge-a-causal-model) supplies causal construction when the needed relations are missing. Its conditional models join the account at :4.2–4.3; their causal support remains a separate question under `C.28` and :4.5.
- Value treatment and comparison remain separate from constructing models. A model can expose a value conflict without settling it, and the later choice remains with its authorized owner.

### PSDA.3:End

## PSDA.4 - Select Problem-Structuring Methods and Combine Them When Needed

> **Type:** Method pattern body
> **Status:** Stable
>
> **Primary working result:** an **inquiry Method and limits**: the selected reusable way of conducting the bounded inquiry, why its contributions fit the required result, how any combined Methods connect, and the conditions under which the selection must change or stop.

### PSDA.4:1 - Problem frame

**Use this when** a favorite workshop recipe, analytical technique, or problem-structuring method is being proposed before anyone has tested whether it can produce the needed result with these participants, uncertainties, conflicts, and resources. Also use it when several useful Methods are available but their combination has no clear contribution or usable join.

Start by naming the result the inquiry is missing. Compare the simplest sufficient Method with a serious alternative, including a bounded combination when one Method cannot supply the needed contributions. The practical gain is a defensible way of proceeding, with visible limits and a cheaper exit when elaborate facilitation adds no value.

A **Method** (`U.Method`) is a reusable way of doing under stated applicability, participant meanings, preconditions, intended effects, and bounds. The governed question here is which such way fits this problem-structuring or decision-analysis inquiry and whether a proposed combination is coherent. A document describes it, a plan schedules intended work, and people enact it in actual work; none of those is the Method merely by appearance.

**Do not use this pattern** to select software by feature count, establish that a named person is competent or authorized, or schedule an already-selected Method. If one direct calculation or an existing sufficient Method closes the question, use it. If the missing result is the inquiry's purpose or scope, return that question before choosing a workshop.

### PSDA.4:2 - Problem

A popular method can be well described and still be wrong for the current inquiry. It may require participation that cannot be obtained, assume a shared purpose that is disputed, depend on data that do not exist, or produce agreement when the recipient actually needs competing claims and discriminating evidence.

Combining methods creates further risks. A concern map becomes numerical weights without an elicitation basis. A scenario becomes a probability distribution. Two workshops duplicate the same task while an essential technical question remains unanswered. A schedule of activities is called an integrated Method even though no one can explain what connects its results.

### PSDA.4:3 - Forces

| Force | Tension |
| --- | --- |
| Fit | A Method must address the live difficulty, while familiar expertise makes some candidates easier to enact. |
| Participation | Joint inquiry can expose differences, while access, power, time, language, and willingness constrain genuine participation. |
| Complementarity | Several Methods can supply distinct contributions, while more methods add joins, effort, and failure opportunities. |
| Reuse and adaptation | Reusable ways make preparation and learning possible, while a local adaptation may change their identity or assurance needs. |
| Timeliness | The receiving decision has a horizon, while a deadline does not make missing premises true. |

### PSDA.4:4 - Solution

Select by needed contribution and actual applicability, not by a school name or workshop format. Recover what each candidate Method does, compare alternatives at comparable effort, and justify every combination through the meaning of its inputs, outputs, and conditions.

#### PSDA.4:4.1 - State the required result and selection conditions

Use the `PSDA.2` scope for the same subject and receiving decision when it constrains the selection. Use a `PSDA.3` model account only where its models, limits, or conflicts can discriminate candidate Methods. Neither input creates a mandatory sequence.

Recover the current facts that can change Method fit: whether the difficulty concerns interpretation, evidence, interconnected choices, values, or action; who can participate and through which channels; what disagreement must remain visible; the available expertise and data; and the time and resource boundary. Obtain consequential participation, competence, safety, and authority premises from qualified direct sources.

A source is useful only for its named subject, condition, and evidence window. If a required scope, model, or participation premise is missing or incompatible, state the exact gap, select a narrower use if defensible, or stop. Do not treat availability of a MethodDescription as evidence that the Method fits.

#### PSDA.4:4.2 - Recover candidate Methods as ways of doing

For each serious candidate, describe the action in plain language: what participants do, with what accepted inputs, to produce which result under which conditions. When the proposed reusable way is already recoverable, use `A.3.1` to identify it.

Use `A.3.1.MR` only when several grounded occurrences or direct sources create a candidate-recovery question about what reusable way the material may show, and no Method has yet been established. It returns provisional source-traceable candidate accounts, a distinguishing question, or an honest lower result; Method identification remains a separate `A.3.1` question.

If the way is known and only its wording is unclear, clarify the statement; use `E.10` only if an FPF kind or relation question remains. If a prospective recipe lacks a decision about its intended action or applicability, return that missing design question to the person designing the inquiry Method. A missing design choice is not by itself a reason to reconstruct past practice.

For a concrete contrast, three grounded inquiry accounts may leave two explanations plausible: a fixed question sequence with local exceptions, or a reusable rule that changes questions when a concern is challenged. That is a candidate-recovery question for `A.3.1.MR`. A new proposal saying only “interview residents” leaves its intended return and conditions unstated: ask its author to make those design choices, without inventing earlier inquiries. Once the proposed way is sufficiently stated, apply `A.3.1` without requiring such a history.

For example, an attributed-mapping Method elicits a participant's claims, explores their implied connections, checks the rendering with that participant, and retains unresolved differences. A conditional-analysis Method evaluates named alternatives under stated conditions with qualified models and returns consequences and limits. Their labels are insufficient; their actual contributions and applicability make comparison possible.

A source description can explain a Method without demonstrating its effectiveness in this inquiry. Keep instructions, reported applications, direct comparative evidence, and practitioner competence distinct. A document about several Methods is not automatically a `U.MethodDescription` of one composite Method; `A.3.2` governs that membership.

#### PSDA.4:4.3 - Compare the simplest sufficient candidate with a real alternative

Choose the comparison dimensions from the required result. The following questions are often decisive:

- Does the Method reveal the material interpretations, or does it require agreement that is absent?
- Can it use the available evidence without manufacturing precision?
- Can affected participants meaningfully contribute or challenge the result through available channels?
- Does it produce the kind of result the next inquiry needs?
- Can the needed expertise, time, and resources be provided?
- What important limitation or failure would remain?

Compare a single sufficient Method, the plausible incumbent, and a bounded combination only when each is a live alternative. Do not turn every inquiry into a survey of all PSM families. State the trade-off if a richer result costs more preparation or excludes a faster route. Method popularity, a successful workshop elsewhere, and participant satisfaction do not establish comparative fit here.

If the necessary premise cannot be tested before the receiving decision, select a qualified provisional use or return the limitation. A declared gap is not a low score to be averaged away.

#### PSDA.4:4.4 - Combine contributions through explicit joins

Combine only when the second Method contributes something material the first cannot provide at acceptable effort. Name the result or preserved condition passed between them, its meaning, the receiving precondition, and what happens when the join fails.

An attributed concern map can supply candidate objectives for examination. It cannot supply legitimate numerical weights without the separate elicitation and value assumptions those weights require. A qualitative scenario can supply a condition for technical analysis, not its probability. Keep such conversions as explicit additional work or leave the outputs uncombined.

Recover order from dependence. An analysis may need a specific formulation before it can run, while participation inquiry and technical evidence collection can proceed concurrently once their common question is clear. Their later join still needs compatible subject, conditions, meanings, and limits. Document order, calendar order, and simultaneous use do not establish Method composition.

When the inquiry needs one composite `U.Method`, first identify the whole under `A.3.1`, then use `B.1.5` to qualify its independently identified part Methods and whole-forming claims. State the whole action, applicability, accepted inputs, result, required joins, allowed variations, exposed interactions, and failure or stop conditions. A different part, ordering, or interface outside the permitted variations can identify another Method.

If several Methods are merely coordinated without a recoverable whole, return that bounded arrangement honestly. It may be useful interim planning content, but it is not yet the needed inquiry Method. Name the missing whole-action or join question rather than relabeling the activity list.

#### PSDA.4:4.5 - Assess the fragile premise and retain a stop

Examine the assumption most likely to make the selected way unusable: for example, whether a participant can challenge an attributed statement, whether a model accepts the needed scenario, or whether two outputs mean the same thing. Use present support to select a qualified Method or narrow its promised result. When a rehearsal, direct evidence check, or bounded trial could improve that selection, apply `C.11.DUA` to its obtainable contribution and full cost, delay, access, and burden before commissioning it; `A.15.9` governs an outside-practice request.

State what the trial can establish. A successful rehearsal may show that the contribution can be produced under those conditions; it does not demonstrate universal effectiveness or later implementation success. If a required participant, expertise, safeguard, or evidence input is unavailable, adapt the Method within its admitted variation, choose another, narrow the result, or return a blocker.

Continue only while the selected Method can produce its declared result without concealing the unresolved premise. A deadline may justify a narrower return; it does not justify claiming that an omitted contribution was completed.

#### PSDA.4:4.6 - Return the selected Method and limits

| Result position | Content the recipient needs |
| --- | --- |
| Required use | The subject, receiving question, needed result, and current selection conditions. |
| Selected Method | Its reusable action, generic participant meanings, preconditions, intended result, and bounds; enough source content to recover that way of doing. |
| Comparative reason | The serious alternative, the defect or trade-off that changed selection, and the effort accepted. |
| Combination, if needed | Identified part Methods, real dependence or overlap, joins and adapters, whole-level conditions, permitted variation, and failure routes. |
| Reliance limits | What the available source and trial evidence establish, what remains untested, and which direct premises are still required. |
| Reopen basis | A changed result need, participant access, evidence, scope, resource, or failed join that would alter the selection. |

Keep dated assignments and scheduling in the work plan. Record actual enactment and its results separately. A selected Method is neither a commitment by absent participants nor proof that anyone has enacted it.

Supply this result to facilitated inquiry or the reconciliation of simultaneous engagements only where the same situation and qualification window fit. A receiving practitioner still checks the current conditions; Method availability is not fit, enactment, or cultural uptake.

#### PSDA.4:4.7 - What changes in practice

The practitioner can explain why this way of working fits, which simpler alternative was considered, and where the arrangement would fail. Adaptation becomes a reasoned change of action and conditions instead of an unexamined mixture of workshop exercises.

### PSDA.4:5 - Archetypal Grounding

#### PSDA.4:5.1 - Choosing a bounded flood-pump inquiry Method

In this illustrative case, the board needs a pre-season return while service meanings remain contested and the mobile-pump branch depends on unqualified road-access evidence. The current scope and model account make two contributions material: recovering attributed service claims and testing the conditional technical premise.

The author of the engagement design compares three plausible ways:

| Candidate | Contribution and present limit | Selection consequence |
| --- | --- | --- |
| Capacity analysis alone. | Can examine nominal capacity, but cannot recover different service meanings or establish mobile access. | Insufficient for the declared return; retain it only as a bounded technical contribution. |
| A broad facilitated exploration of the whole flood situation. | Can expose more interpretations, but exceeds the pre-season question and available participation time. | Defer the broader inquiry; keep its boundary challenges visible. |
| Attributed mapping joined with conditional access-and-capacity analysis. | Addresses the two discriminating needs, provided attribution can be checked and technical premises have competent sources. | Select the bounded combination with explicit joins and stops. |

The proposed reusable whole is: **for a bounded intervention inquiry with contested service meanings and conditional technical feasibility, contrast attributed service claims with qualified conditional consequences, resolve only the joins needed for the receiving question, and return shared findings and unresolved contrasts without choosing the investment.**

The mapping part elicits, connects, and confirms attributed claims. The analysis part tests named configurations and conditions and reports supported consequences or exact gaps. They can proceed in parallel after the subject and conditions are fixed. Their join accepts only outputs concerning the same intervention, service meaning, and horizon; an unmatched service claim is retained as an unresolved question, not converted to a technical metric.

The whole admits written or spoken elicitation when attribution and challenge remain possible. It does not admit replacing participant confirmation with the sponsor's paraphrase. Its externally usable result is the bounded claim account; internal map-editing steps are not separately promised services. Those action, join, variation, and boundary conditions identify the proposed composite Method for the `A.3.1` and `B.1.5` questions.

For actual use of this combination, participation must permit attribution and challenge. Without qualified access evidence, the return remains a conditional technical claim. A direct access inquiry is worthwhile when an obtainable result can change the pre-season decision enough to warrant its burden; otherwise the conditional claim completes this return. The plan's date and assigned analyst are separate from the reusable Method.

#### PSDA.4:5.2 - A failed join rather than a failed workshop

A team proposes transferring the frequency of concerns mentioned in interviews into numerical criteria weights. The mapping Method yields attributed concerns, not preferences under a weighting model. The join fails even if the interviews were well facilitated.

The practitioner either obtains a separately justified elicitation Method and tests its assumptions or keeps the value contrast qualitative. The failed conversion does not invalidate the interviews or authorize invented weights.

#### PSDA.4:5.3 - Cheap non-use

An operations team has an agreed question, a current qualified calculation Method, sufficient evidence, and no material participation or interpretation conflict. Use that Method. A new multimethod arrangement adds cost without changing the required result.

### PSDA.4:6 - Bias-Annotation

**Scope:** selection and bounded composition of Methods for problem structuring and decision analysis. **Lenses:** **Prag** tests fitness and effort; **Onto/Epist** separates Method, description, plan, enactment, and evidence; **Arch** exposes real joins; **Gov** preserves participation and authority conditions; **Did** makes the reusable action explicit.

Facilitator-familiarity bias favors the method the team can already run. Brand bias mistakes a school name for an identified way of doing. Integration bias treats more techniques as broader competence. Time-pressure bias hides omitted contributions. Counter these with one serious simpler alternative, a result-based contribution comparison, and the exact fragile premise that could reverse selection.

### PSDA.4:7 - Conformance Checklist

- [ ] The selection names the missing result and current subject, scope, conditions, and receiving use.
- [ ] Needed model, participation, expertise, and authority premises are qualified or explicitly missing.
- [ ] Candidate Methods are recoverable reusable ways, not merely titles, descriptions, plans, or reported workshops.
- [ ] A serious simpler alternative and the selected trade-off are explicit.
- [ ] Each additional Method supplies a distinct material contribution.
- [ ] Passed results preserve meaning, scope, and limits; conversions requiring new evidence are not hidden.
- [ ] Real dependence and possible overlap are distinguished from document and calendar order.
- [ ] Any composite-Method claim satisfies the direct whole and part questions; a mere arrangement remains an honest lower result.
- [ ] Fragile premises, allowed variation, failure routes, and local reopen conditions are stated.
- [ ] The result establishes neither actual enactment, participant commitment, effectiveness, nor later choice authority.

### PSDA.4:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “We always run this workshop.” | Recover the required result and compare one serious sufficient alternative. |
| “The agenda is the Method.” | State the reusable action and applicability separately from dated scheduling. |
| “The techniques appear in order, so they compose.” | Test actual dependence, part-Method identity, whole action, and joins. |
| “The qualitative output can be scored numerically.” | Identify the extra elicitation, measurement, or model assumptions; otherwise retain the qualitative result. |
| “The method worked elsewhere.” | Carry the source's subjects, conditions, evidence limits, and actual contribution into this selection. |
| “A shorter deadline removes the need for that input.” | Narrow the declared return or stop; do not mark the missing contribution as completed. |

### PSDA.4:9 - Consequences

Selection becomes inspectable and adaptations become easier to challenge. Methods can contribute together without forcing one universal workflow. The cost is a small comparison and join analysis; a genuinely composite Method may require more identification and assurance work. The pattern can therefore return an existing single Method, a bounded composite, or an explicit incomplete selection.

### PSDA.4:10 - Rationale

Method fit is relational: it depends on what the inquiry needs and what its conditions permit. Complementary labels do not establish complementary results. Recovering reusable actions and their joins explains why the combination can work and what would defeat it, while keeping plans and enacted outcomes separate.

### PSDA.4:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| Which PSM contribution fits the engagement? | Compare assumptions, contributions, conditions, and needed outcomes; retain a simpler sufficient route. | A familiar branded PSM is used as a default regardless of the difficulty. | **Adapt:** `PSDA.4:4.1`–`4.3` compare actual ways of doing and their limits. A short comparison costs more than automatic selection but is justified when a missing contribution can reverse the return; it does not require a full method catalogue. | Smith and Shaw's [2019 PSM characterization](https://doi.org/10.1016/j.ejor.2018.05.003) is a conceptual comparison candidate that makes differences among approaches inspectable; its exploratory family characterization is not a method-ranking algorithm. Lami and Tavella's [2019 workshop comparison](https://doi.org/10.1016/j.ejor.2018.12.016) supplies bounded counterexample evidence to a uniform-usefulness claim: outcomes varied across SCA, SSM, and self-organized workshops in an exploratory MSc-student study. It establishes no universal winner or professional-field effectiveness. | Reopen when the intended outcome or participation conditions change, or better comparative evidence changes the fit of a serious candidate. |
| When does combining Methods improve the result? | Require a distinct contribution and an intelligible join; qualify a composite Method only when its whole action is recovered. | More techniques, a sequence diagram, or an agenda is treated as an integrated Method. | **Adapt:** `PSDA.4:4.4`–`4.6` and the failed-weighting example expose the conversion or missing result. **Adopt:** `A.3.1`, `A.3.2`, and `B.1.5` keep reusable way, description, whole-forming facts, and enactment distinct. Extra join work is accepted only for a material contribution; otherwise the single-Method alternative wins. | Marttunen, Lienert, and Belton's [2017 PSM–MCDA review](https://doi.org/10.1016/j.ejor.2017.04.041) supplies the critical combination line and concrete interface difficulties, not evidence that arbitrary mixtures work. The current FPF patterns supply identity and composition rules, not empirical validation of this engagement Method. | Reopen when a join loses meaning, a part or whole identity changes, a critical precondition fails, or a single Method supplies the same useful result at lower effort. |

### PSDA.4:12 - Relations

- `PSDA.2` supplies the scope/result frame for the same subject and decision. `PSDA.3` supplies model contributions only where they discriminate Method alternatives. Either needed input can be replaced only by a qualified direct result or returned as an exact gap.
- `PSDA.13` and `PSDA.17` may consume the selected Method and limits for the named situation and qualification window. Availability establishes neither fit nor enactment or cultural uptake.
- `A.3.1.MR` supplies provisional accounts only when several grounded occurrences or direct sources create a reusable-way recovery question and no Method is yet established; `A.3.1` identifies a recoverable proposed way without making that recovery compulsory. `A.3.2` governs a description of one identified Method; `B.1.5` governs the composite qualification when needed.
- `A.15.2` governs intended Work and `A.15.1` actual Work and its enactment relation. Direct competence, participation, authority, evidence, and safety practices govern their own premises.
- This selection can request a missing domain result; it cannot manufacture that result by choosing a better workshop format.

### PSDA.4:End

## PSDA.5 - Generate Decision Alternatives

> **Type:** Method pattern body
> **Status:** Stable
>
> **Primary working result:** a finite **candidate set** for one decision-support question, with materially different alternatives, their supported and unresolved premises, and the exact candidate gaps that still matter.

### PSDA.5:1 - Problem frame

**Use this when** an inquiry has clarified what matters but the proposed decision still contains only the incumbent, a sponsor's preferred project, or two labels such as “buy or build”. Also use it when a request for development advice names a course, provider, reorganization, or AI tool before the possible directions have been constructed.

Start by asking what different action could address each live formulation or concern. Change the mechanism, arrangement, combination, timing, or commitment being considered, then state enough of each resulting alternative for a fair consequence comparison. The practical gain is a choice worth examining, including an honest gap when no supported alternative is available.

The governed object is the candidate set, not a selected action. A candidate describes a possible intervention or commitment; its description does not establish feasibility, permission, performed Work, or benefit. Alternatives may address competing formulations rather than obtain exactly the same result. Preserve that difference instead of inventing parity.

**Do not use this pattern** when an adequate finite set already exists and only comparison or an authorized choice remains. Use the direct domain practice when it already owns the complete alternative-generation question. A population or lineage without a population-local recipient or chooser is not a recipient of development advice; an authorized researcher's intervention is a different decision-support case.

### PSDA.5:2 - Problem

An apparently open choice can be closed before analysis begins. A list of pump models omits deployment arrangements; a list of training courses omits changing the Work that prevents capability expression; a list of AI models omits the tool, data, or operating configuration responsible for the failure.

Unrestricted ideation creates the opposite difficulty. Hundreds of names can repeat the same intervention, depend on unsupported capacities, or combine benefits that cannot coexist. Novelty does not make an alternative useful, and an attractive candidate does not become admissible because it survived a workshop.

### PSDA.5:3 - Forces

| Force | Tension |
| --- | --- |
| Breadth and relevance | A different mechanism may expose a better direction, while an unbounded search consumes the decision horizon. |
| Plural formulations | Alternatives should address material interpretations without pretending that every interpretation seeks the same result. |
| Imagination and qualification | A proposal may be worth investigating before feasibility is known, while unsupported proposals cannot be presented as ready commitments. |
| Combination and interaction | Hybrid or staged directions can preserve options, while shared resources, incompatibilities, and delay can remove their apparent advantage. |
| Generation and choice | Early preference helps identify concerns but can suppress candidates before their consequences are known. |

### PSDA.5:4 - Solution

Construct alternatives from the live decision question and useful differences in the inquiry. Make each candidate complete enough for its next use, separate qualification gaps from rejected directions, and stop with a bounded set or a precise missing-alternative result.

#### PSDA.5:4.1 - Recover the receiving question and useful inputs

Name the subject, question, horizon and current arrangement. Recover the protected conditions and resource bounds that can change which alternatives are live. When the inquiry serves a recipient or prepares a commitment, name the recipient, later choice owner and commitment as applicable, and establish the authority boundary required for that use. If the question or a required authority boundary is missing, return that premise rather than inventing a development programme.

Use a `PSDA.1` formulation set only where its differences suggest different interventions. A formulation is not itself an action. Use the `PSDA.3` model account only where a model discriminates candidate mechanisms or exposes an omitted consequence. Use `PSDA.13` inquiry results where a shared or contested claim changes the alternatives; agreement is not required.

These are conditional contributions. Use a qualified direct result when it supplies the same needed premise. If the needed input is absent, stale, or incompatible with this subject and horizon, retain the precise gap. Neither adjacent PatternIDs nor a completed workshop supplies an alternative by itself.

#### PSDA.5:4.2 - Vary the decision-changing contents

Ask what the proposal is meant to achieve, why that result matters, and what other way could address the concern. Generate some ideas independently before group discussion when early advocacy could anchor the whole inquiry. Then use differences and objections to construct additional candidates.

Useful prompts include changing the intervention mechanism, obtaining arrangement, scale, timing, resource allocation, or commitment. Consider combining compatible actions, retaining the present arrangement, declining a proposed change, and obtaining information before a larger commitment. These are prompts, not a mandatory taxonomy or a required number of options.

When the known menu supplies no way to obtain a material desired consequence, use [PSDA.6:4.2](#psda642---distinguish-ends-means-and-repeated-consequences) to distinguish that end from the initially proposed means. Where their relationships need construction, use the backward branch of [PSDA.8:4.2.1](#psda8421---construct-and-question-a-qualitative-consequence-network): trace necessary conditions and possible sufficient routes, propose a combination of means, and test that whole combination forward under the same assumptions. Return the resulting alternative here with its conditions and open transitions. An incompatible combination prompts another construction or a revised formulation; it does not prove that the desired result is impossible. Reuse an adequate direct construction without building another network.

Describe “no new action” against a real baseline. It may still include already authorized maintenance, contractual duties, continuing costs, deterioration, or exposure. It is not a cost-free, consequence-free empty world.

For a staged direction, say what happens first, what later choice remains open, which observation could inform it, and what delay or irreversibility the first commitment introduces. Do not call a probe reversible merely because it is small; obtain the direct feasibility, consent, safety, and recovery premises when they matter.

#### PSDA.5:4.3 - Turn labels into sufficiently complete candidates

For each material alternative, state the proposed change from the current arrangement, affected subjects, intended result, enabling conditions, major burdens, evidence basis, and unresolved premise. Distinguish what is supported now from what is proposed or unknown.

Use `C.38` only when several whole ways are intended to make the same receiving result available and labels still hide their different burdens. If the alternatives seek different results, retain the difference and let the decision-support comparison expose it. Do not force a same-result declaration merely to obtain a neat table.

A combination is another candidate when its interactions can change consequences. Check shared staff, facilities, money, dependencies, sequencing, and incompatible assumptions. Two independently attractive components do not establish an attractive combined arrangement. A provider's advertised capability, a course title, or a benchmark score is not a qualified result for this holder.

#### PSDA.5:4.4 - Distinguish exploration from a live commitment option

Keep a promising but unresolved proposal available for inquiry without presenting it as an admissible commitment. A short annotation is enough: “comparison-ready within these conditions”, “requires this qualification”, or “excluded for this stated reason”. These phrases describe the present use; they create no new universal status system.

Inspect an adequate existing specialist result before requesting more. Preserve useful directions and the exact limit on a stronger claim. A decision-changing cross-practice gap becomes a feasibility, allocation, transfer, security, or other request only when `A.15.9` selects its obtainable contribution against the whole acquisition burden through `C.11.DUA`. A missing result may block one branch while others remain useful.

Use `C.17` when a claim about novelty, diversity, or usefulness of the named candidates needs characterization. Use `C.18` when open-ended generation, archive, or front stewardship is actually needed. Neither characterization nor archive membership chooses the decision alternative. Use `C.19` only for an actual live-pool policy question; thin evidence alone supplies no default exploration policy.

#### PSDA.5:4.5 - Challenge coverage and stop proportionately

Ask whether the set still reflects only one favored formulation, one available technology, or one powerful participant's concern. Check whether a materially different mechanism, genuine no-change case, compatible combination, or bounded probe was omitted without reason. Merge labels that have the same decision-changing contents; retain differences that alter consequences or supported use.

Stop when the set is sufficient for the present comparison: material formulation differences have an addressed candidate or an explicit gap, each retained row is intelligible, protected-condition exclusions are visible, and additional search has no identified benefit worth the remaining effort. This is bounded sufficiency, not proof that all possible alternatives have been found.

If only one lawful direction survives, report that fact and its basis without manufacturing a rival. If none survives, return the missing qualification, infeasible requirement, or need to reopen the problem. A gap is a useful result; a decorative list is not.

#### PSDA.5:4.6 - Return the set without making the choice

Return the question, subject and horizon; the exact candidate contents; their material differences; supported conditions and remaining gaps; excluded branches and reasons; and the observation that would add, remove, or change a candidate. Use the smallest readable form that lets another practitioner reconstruct those distinctions.

`PSDA.8` may use this set as the alternatives for its named consequence comparison. The comparison must still establish its own value, evidence, and scope basis. Use the set as an input to any further ranking or recommendation. The authorized chooser makes the choice. Any later programme or WorkPlan needs its own basis; support claims about performed work and achieved effects with evidence of those occurrences.

### PSDA.5:5 - Archetypal Grounding

#### PSDA.5:5.1 - Flood-pump alternatives beyond a purchase contest

In this illustrative case, the board needs a pre-season return for the next flood season. The inquiry distinguishes nominal capacity, deployment reliability, unequal service, and downstream consequences. The model account says that nominal permanent and mobile capacity can meet the assumed inflow when the stated units are operating, but mobile arrival under road loss is not yet supported. Reachable assistance remains a separate service concern.

The inquiry turns those premises into three candidate descriptions and one unfinished proposal for staging:

| Candidate | Different action being considered | Present use and gap |
| --- | --- | --- |
| N — continue the present arrangement | Keep already authorized operation and maintenance; make no new capacity commitment. | A real baseline for comparison, not an assumption of adequate service or zero cost. |
| F — fixed-capacity change | Add fixed capacity with the necessary operating, staffing, and support arrangement. | A proposed whole change; direct engineering and service results must qualify its consequences. |
| M — mobile-reserve arrangement | Obtain mobile capacity together with its transport, deployment, staffing, and access arrangement. | Retained for inquiry; the road-loss deployment premise prevents an unconditional commitment claim. |
| S — unfinished staged proposal | The proposal would preserve a later capacity choice informed by an access or service inquiry, but its first intervention has not been specified. | Keep the construction question open: what should change first, and how would that permit the later choice? Specify that intervention and qualify its temporary provision, resource overlap, delay and recovery before comparing S as a distinct direction. Adding the benefits of F and M does not answer these questions. |

The property-protection and reachable-assistance concerns remain distinct. They lead the team to ask whether each whole arrangement serves both; they do not establish an approved priority between them. No candidate is dropped because its proponent dissents from the majority.

Return N, F and M with their stated limits, and retain S as an unfinished proposal with a named construction question. The supported comparisons remain usable at their stated scope. If commitment-ready options are needed, identify the missing premise for M and the unfinished construction and qualification of S. Keep those gaps visible without claiming that the usable set exhausts all possibilities.

**A further construction round.** Suppose the recipient now asks for a pumping arrangement that can be deployed on the isolated side when the bridge is closed. PSDA.6 separates that end from the proposed means “deliver the reserve unit by road”. Working backward through PSDA.8:4.2.1 gives another route: put a unit, a competent crew and their required supplies on that side before closure. The first combination borrows the crew of an existing fixed station. Testing it forward exposes an incompatible condition: operating both arrangements during the flood needs that same crew at both sites. This candidate cannot claim both services.

The team constructs L: pre-position a leased unit and supplies at a suitable local site, with a separately available crew and an agreed local activation arrangement. For this teaching continuation, assume that the responsible specialists have established site suitability, equipment and crew availability, the relevant operating permissions, and provision for the named flood duration; the cost fits the stated comparison budget. With those premises, the forward trace no longer depends on the bridge or double-allocates the fixed-station crew. L is a new comparison-ready alternative for the specified deployment result. Its cost, capacity, service distribution and other material consequences still need comparison; it is neither a selected investment nor evidence of actual performance. If the separate crew cannot be obtained, retain that exact gap or reopen the service formulation instead of silently restoring the double allocation.

#### PSDA.5:5.2 - A ninety-day development-direction question

An advisory team is asked which direction a service organization should consider for a ninety-day reliability horizon. “Train, outsource, or use AI” is not yet a set of comparable directions. The adviser resolves the labels into internal development with covered service duties, a qualified provider arrangement, and a mixed human–tool arrangement with specified oversight and fallback. A bounded mixed-arrangement probe is a separate candidate when its information and operating consequences differ from deployment.

Each branch needs its own supplier result. Human capability evidence does not establish transfer to the representative later Work; provider evidence does not establish interface or security fit; model evaluation does not establish reliability of the mixed arrangement. If the organization-allocation comparison is missing, return that exact gap rather than ranking the three labels.

For advice about one person, the same move generates directions only from qualified human and target-Work premises. For an AI arrangement, it distinguishes parameter, data, scaffold, tool, code, and environment changes only where the case makes those objects live. Neither application imports the other's mechanism or evidence.

#### PSDA.5:5.3 - Cheap non-use

A recipient already has two complete, qualified ways of obtaining the same repair result and asks which to choose. Use the existing set and the applicable comparison or `C.11` choice guidance. Another brainstorming exercise adds no candidate-changing result.

### PSDA.5:6 - Bias-Annotation

**Scope:** alternatives for bounded decision inquiries. **Lenses:** **Prag** tests useful differences; **Onto/Epist** separates proposed arrangements from facts; **Arch** exposes combinations and dependencies; **Gov** preserves protected conditions and later authority; **Did** replaces label lists with intelligible candidates.

Incumbency, sponsor anchoring, technology availability, and novelty bias can each shrink or distort the set. Challenge the omitted mechanism and baseline, not merely the number of ideas. Counter the opposite bias toward endless variety by asking what additional candidate could actually change the present comparison.

### PSDA.5:7 - Conformance Checklist

- [ ] The recipient question, holder or subject, current arrangement, horizon, and separate choice boundary are recoverable.
- [ ] Formulations, models, and inquiry claims contribute only where they change the candidates.
- [ ] Alternatives differ in decision-changing contents, not merely names.
- [ ] The no-change case includes its actual continuing obligations and consequences.
- [ ] Combinations and staged directions expose interactions, delay, and unresolved enabling conditions.
- [ ] Supported, proposed, and unknown premises remain distinguishable.
- [ ] Qualification gaps and excluded branches have exact reasons; missing alternatives are not fabricated.
- [ ] The stopping point states bounded sufficiency, not exhaustive search.
- [ ] The returned set permits a later comparison without asserting selection, authority, Work, or benefit.

### PSDA.5:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Score the sponsor's option against “do nothing”. | Recover a real baseline and a materially different mechanism or explain why none is live. |
| Treat buy, provider, AI, and internal as peer kinds. | Describe the proposed whole arrangements and their receiving results. |
| Exclude a proposal because feasibility is unknown. | Keep the inquiry candidate separate from commitment eligibility and name the missing result. |
| Add component benefits to justify a hybrid. | Qualify the combined configuration and its interactions. |
| Treat novelty or archive membership as selection. | Use the characterization or archive result only for its stated function. |
| Generate forever because the set is not exhaustive. | Stop at the bounded comparison need and retain a specific reopen condition. |

### PSDA.5:9 - Consequences

The recipient gets a genuinely wider but finite decision question, with candidate gaps visible before scoring. The cost is some additional construction and qualification effort. Concentrate it on omitted differences that could change the decision; do not describe every possible arrangement in equal detail.

### PSDA.5:10 - Rationale

Structured inquiry becomes useful to choice when its differences change what can be done. Alternative construction preserves those differences while qualification prevents imagination from becoming an unsupported commitment. Keeping generation separate from comparison permits a promising proposal to remain investigable without calling it a winner.

### PSDA.5:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How can an engagement escape the incumbent without producing a decorative idea list? | Use objectives and materially different mechanisms to guide alternative construction. | Unstructured group brainstorming is cheap; a supplied option menu is cheaper still. | **Adapt:** :4.1–:4.3 add concern-led prompts and independent generation where anchoring matters. The deliberate cost is a short construction pass before comparison; an adequate existing set takes the cheap exit. | Borgonovo et al.'s [2026 decision-analysis review](https://doi.org/10.1016/j.ejor.2025.05.023), especially its value-focused-thinking discussion, is a current synthesis candidate. Keeney's [2012 value-focused brainstorming](https://doi.org/10.1287/deca.1120.0251) supplies the specific objective-led and individual-before-group procedure. Its policy example is not universal effectiveness evidence. | Reopen if a simpler elicitation gives the same material breadth or the objectives themselves suppress a live formulation. |
| When is a staged alternative genuinely different? | Preserve options only through explicit dependencies, observations, and feasible later changes. | Compare only fixed end-state projects, or label an underspecified pilot “adaptive”. | **Adapt:** :4.2–:4.4 require a specified and qualified first commitment, later question, and delay or lock-in consequence. The unfinished S example shows why a staging label is insufficient. Additional description is justified only when timing changes the comparison. | The [2019 DAPP chapter](https://doi.org/10.1007/978-3-030-05252-2_4) is the best-known-line candidate for pathway dependencies and failure conditions; its water-policy applications do not supply PSDA's local thresholds, authority, or universal sequence. | Reopen when monitoring, lead time, or reversibility makes the staged direction infeasible or no longer distinct. |
| Does a novelty result already supply the alternatives? | Keep characterization, generation stewardship, and local choice separate. | Read a novelty profile or archive as a ready option set. | **Adopt:** :4.4 uses C.17 and C.18 only for their actual objects; :4.6 retains the PSDA candidate result. This avoids reconstructing machinery when ordinary candidate descriptions suffice. | Current `C.17` characterizes bounded novelty or use; `C.18` governs generation, archive, and front stewardship; `C.38` forms same-result ways. Their exact boundaries defeat the broader reading, but none supplies holder feasibility. | Reopen only if a direct contribution or the receiving candidate question changes. |

### PSDA.5:12 - Relations

- `PSDA.1` supplies formulation differences for candidate formation, not selected actions. `PSDA.3` supplies discriminating model claims, not the obtaining conditions they represent. `PSDA.13` supplies shared and contested inquiry claims only where they change the set; dissent remains explicit.
- `PSDA.6:4.2` distinguishes desired ends from proposed means. When a missing alternative requires a new means combination, `PSDA.8:4.2.1` supplies backward construction and its forward test; return the candidate and its conditions to :4.3. `PSDA.8` may then consume the set for the named consequence comparison. Generation does not select.
- `C.17`, `C.18`, `C.19`, and `C.38` supply characterization, generation stewardship, live-pool policy, and same-result construction only under their own use conditions.
- `A.15.9` supplies bounded use of an outside-practice result and selection of a worthwhile further request. Direct holder and domain practices supply feasibility, mechanisms, protected conditions, and evidence.
- `C.11` governs the later local choice over an adequate option set. A missing or incompatible input returns to its qualified direct source or remains an exact gap; no neighboring body is a compulsory prerequisite.

### PSDA.5:End

## PSDA.6 - Represent Values and Trade-Offs

> **Type:** Method pattern body
> **Status:** Stable
>
> **Primary working result:** a **decision-usable value account**: attributed concerns and objectives, their consequence measures, protected conditions, admitted trade-offs, unresolved disagreements, and limits for one named comparison.

### PSDA.6:1 - Problem frame

**Use this when** a scorecard's criteria came from a template, “importance” weights have no stated meaning, or the same benefit appears under several headings. Also use it when people agree that reliability, development, safety, or fairness matters but mean different consequences for different subjects, or when their consequence comparisons still need to become a justified numerical model.

Begin with one concern: important to whom, about which subject and situation, and why? Trace it to a consequence that could distinguish the live alternatives. Then state how that consequence will be represented and whether it may be traded against another. The gain is a comparison whose value assumptions can be understood and challenged.

The governed object is the value account for that comparison. An objective expresses what is wanted; a measure describes a characteristic; a preference orders consequences; a protected condition limits permissible trade-offs. They can be related without becoming the same thing. Neither an expressed preference nor a numerical weight supplies authority to waive a duty or another person's rights.

**Do not use this pattern** when a current, qualified value account already answers the exact comparison question. Use the direct measurement practice for a missing measurement alone, the appropriate authority or domain practice for a condition's current force, and `C.11.DUA` for a disputed requirement's justification. Use the authorized choice owner for the later decision. This pattern does not determine universally correct values.

### PSDA.6:2 - Problem

Criteria can appear neutral while deciding the result. “Install more pumps” embeds an action in an objective. “Service quality” may count the same avoided outage again under reliability, satisfaction, and reputation. Equal weights may silently favor the concern represented by the largest number of criteria.

Numbers can conceal a second substitution. A budget amount, a probability, an ordinal judgement, and a protected condition become interchangeable entries in a spreadsheet. Normalizing each to zero–one does not establish comparable value. A mean of participants' weights can erase a disagreement about who bears the consequence or what may be traded at all.

### PSDA.6:3 - Forces

| Force | Tension |
| --- | --- |
| Completeness and usability | Material values must remain visible, while an enormous hierarchy burdens elicitation and repeats consequences. |
| Measurement and meaning | Observable measures help comparison, while easily measured proxies can displace the actual concern. |
| Trade-offs and protection | Some sacrifices are legitimate within the question; others require a separate authority or are outside permissible compensation. |
| Individual and collective values | A common comparison is useful, while unlike participants need not share one value function. |
| Precision and honest incompleteness | Explicit scales and preference questions can clarify a choice, while unsupported weights create false precision. |

### PSDA.6:4 - Solution

Recover the values behind the decision, organize them around consequences, and declare only the measurement and trade-off structure that the receiving comparison can support. Keep unresolved preferences and protected conditions visible rather than completing a score by assumption.

#### PSDA.6:4.1 - Recover whose concern changes the comparison

Name the subject, affected people or Systems, configuration, horizon, and receiving question. Use `PSDA.12`'s participation and concern account where it supplies relevant attributed concerns, duties, interests, missing voices, or representation limits. That input is not already a value model or a mandate to aggregate preferences.

For each material concern, ask who expresses or bears it, what consequence matters, and under what conditions. Recover an actual assignment, local system-role classification, or authority relation only where the concern's meaning or governing force depends on it. A title such as resident, manager, or expert does not establish representation or decision rights.

If a needed concern or binding condition is unavailable, use a qualified direct source or return the exact gap. Do not treat non-response as indifference. Distinguish participants' current statements from the analyst's proposed interpretation and from an established obligation.

#### PSDA.6:4.2 - Distinguish ends, means, and repeated consequences

Ask “Why does this matter here?” to identify the consequence sought. Ask “How might it be achieved?” to expose possible means. “Provide training” may be one means; reliable performance in representative later Work may be the relevant end. The distinction is local to the question: a process experience can itself be valued when participants actually care about it.

Organize objectives only as far as the structure helps. For a small decision, a few attributed statements may be enough. A hierarchy or means–ends map is useful when several levels or overlaps would otherwise be lost.

Test apparent duplicates through their meaning and consequence path. Avoid counting one consequence twice under different names. But statistical correlation alone is not duplication: service loss and distribution of that loss can remain different values even when their observed measures covary. Conversely, statistical independence does not prove that a preference model may add the values.

Retain an objective only if it represents a material value, protected condition, or decision-changing distinction. When simplifying, state the lost distinction and check that it cannot reverse the intended comparison. Do not delete a concern merely because it is difficult to measure.

#### PSDA.6:4.3 - Give each measure a usable meaning

For every consequential measure, state the characteristic, subject or participant tuple, scale and unit where applicable, direction of preference, horizon, source, and missingness rule. Distinguish a direct measure from a proxy and say what the proxy cannot establish.

Use `C.16` for measurement and `A.19` when a declared multi-characteristic space or reusable predicate is needed. A.19 supplies coordinate and scale meanings; it does not perform scoring, aggregation, comparison, or selection. A number missing its subject or scope is not repaired by placing it in a common column.

Keep raw consequence descriptions alongside any value transformation that the comparison uses. A performance scale and a value scale answer different questions. If an ordinal judgement is used, preserve its ordering without assuming equal intervals or averaging categories. If a numerical value function is used, state the consequence range, anchors, interpolation or shape, and the elicitation basis that makes the transformation meaningful.

#### PSDA.6:4.4 - Separate conditions from compensable objectives

Identify which conditions are binding, which are aspirations, and which are uncertain claims requiring a competent result. Record the source and use of each condition. A participant's request for a minimum service level is a value claim; a separately established legal or safety requirement has its own governing basis.

Do not compensate for a failed protected condition by adding benefits elsewhere. If its meaning, applicability, or authority is disputed, retain that dispute and ask for the exact interpretation rather than choosing a convenient threshold. A comparison may proceed on an explicitly narrower slice while the whole-decision conclusion remains blocked.

When the live question is whether the requirement itself should be retained or changed, use `C.11.DUA` §4.3 with the competent domain contribution. Identify the protected person or System and interest, unwanted outcome, governed quantity or activity, conditions and horizon. Distinguish background, attributable increment and total exposure where they affect the judgement. Examine the causal and measurement basis, uncertainty, threshold or precision choice, marginal protection, full burden and displaced protective work. Compare retention, tightening, revision, replacement or removal only where they are meaningful alternatives. A safety label does not supply that basis, and expense alone does not defeat a protective requirement.

Return the supported requirement recommendation and the reason or limit the recipient needs, together with its present force, amendment authority and feasible time window. The appraisal can finish even when amendment is unavailable; the currently binding condition still constrains action. State a resulting impasse when no acceptable alternative or timely amendment is feasible. A later correction does not restore an already lost opportunity. Use this return only for the disputed requirement; an adequate ordinary value account needs no new appraisal.

Some thresholds are preference choices rather than prohibitions: an aspiration level, budget preference, or tolerated inconvenience. Say which they are and whose judgement they express. A threshold crossing is not automatically a decision or permission to act.

#### PSDA.6:4.5 - Construct preferences from comparisons of consequences

Ask the value holder to compare concrete consequence profiles, with the same people, horizon and conditions in view. Record whether one profile is **no worse**, **strictly better**, or **indifferent** to another, or whether the holder leaves the comparison open. Retain the profiles and the reason given. An open comparison imposes no equality. Use actual alternatives or understandable hypothetical profiles within the declared ranges; a fictitious combination is useful only if the holder can judge its meaning.

The numerical construction below concerns preferences over known consequences. Preferences over uncertain outcomes also need a suitable account of risk and uncertainty; the deterministic trade-off alone does not supply it. Start with §4.5.1 to choose the form, then use the branch whose conditions the value account supports.

##### PSDA.6:4.5.1 - Choose and challenge the representation

Separate protected conditions under §4.4 before considering compensation. Then ask what the preference must preserve. Choose the least burdensome form that preserves the distinctions needed by the receiving comparison. These are usable alternatives, not stages every decision must pass through:

| Available judgement and intended use | Construction and return |
| --- | --- |
| Only directions of improvement and some pairwise comparisons are justified. | Keep those comparisons and coordinate dominance. Infer further comparisons only through an admitted rule, such as transitivity. Return the resulting partial relation and the pairs still open. |
| A priority or threshold is explicitly noncompensatory. | Write and apply that rule, including its order and tie treatment. For example, prefer every profile with waiting time at most two hours to every profile above two hours, then prefer lower cost within each class. This is a preference rule only if the holder says so; its threshold does not become a duty. |
| Improvements can compensate for one another, with constant value increments and a constant exchange over the stated ranges. | Construct the affine family in §4.5.2. Its coefficients express the admitted exchange, not the importance of criterion names. |
| Compensation is acceptable but marginal values may curve. | Test the additive assumption and use the finite-level construction in §4.5.3 when it fits. Preserve interactions through a suitable non-additive family or explicit rules when addition fails. A qualified outranking Method can instead supply a relation with incomparability; its thresholds and aggregation conditions must be supplied with it. |

For a proposed additive form, compare profiles that differ on a subset of criteria while holding the others equal. Repeat the comparison at materially different common levels of those other criteria. A reversal challenges preferential independence: the preference over that subset depends on its background. Ask also about complementarities, thresholds and refusals to compensate. With two criteria, unchanged directions of preference alone give little support for addition; ask about the exchanges themselves. Statistical independence of measurements answers neither question.

For an affine form, ask the stronger question: does the holder value the same physical increment equally at different positions on each scale, and does the compensating amount remain the same at different starting profiles? Within a one-to-five-hour range, compare reducing two hours to one with reducing five hours to four, and repeat a cost-for-time exchange at a different cost level. A stated constant exchange is a substantive modelling assumption over that range. Finite elicitation can challenge it and check its local fit; it does not prove a universal preference law. Preserve that qualification when the assumption is accepted for use, and return the unresolved form choice when it is not.

Keep materially different holders' accounts separate. Combining them requires a legitimately governed aggregation or reconciliation Method. Neither averaging nor choosing the sponsor's account follows from the construction below.

##### PSDA.6:4.5.2 - Construct a family for a constant exchange

Suppose lower cost `c` and lower waiting time `t` are preferred, both matter, and the holder accepts the affine conditions above on the named ranges. Represent loss by `L(c,t) = a c + b t`, with `a > 0` and `b > 0`; lower loss is preferred. A common constant and positive scale do not change the ordering. Divide by `a` to obtain `L_r(c,t) = c + r t`, where `r = b/a > 0`. The unit of `r` is cost units per hour. It belongs to this holder and use, rather than being a measured market price.

For each statement that profile `(c_x,t_x)` is no worse than `(c_y,t_y)`, write `c_x + r t_x <= c_y + r t_y`. Use equality for stated indifference and a strict inequality for stated strict preference. Keep every statement on the same `r` and intersect its restrictions with `r > 0`. The resulting set `R` describes every admitted exchange in this form. A point selected for a convenient spreadsheet is additional preference information unless the holder actually supplied it.

Ranges still matter when scales are normalized. If the cost range is 20–60 thousand and the waiting range is 1–5 hours, normalized losses are `(c-20)/40` and `(t-1)/4`. A weighted sum with positive weights `w_c + w_t = 1` represents the same exchange only when `r = 10 w_t/w_c`. The weights compare the two whole range changes. A different range changes that correspondence; a change in the holder's marginal values can require a different function as well. Unit conversion alone must leave the represented comparisons unchanged.

##### PSDA.6:4.5.3 - Retain unknown marginal values when linearity is unwarranted

For a finite comparison with an admitted additive form, use the distinct consequence levels appearing in the reference profiles and live alternatives. Order each criterion's levels from least to most preferred. Assign an unknown value contribution `q_i(z)` to each level `z` of criterion `i`. Set the least preferred contribution on each criterion to zero, require the contributions to be nondecreasing along that criterion, and set the sum of the most preferred contributions to one. This normalization requires at least one valued improvement across the represented ranges; it fixes an arbitrary origin and unit without fixing relative criterion values. If the holder is indifferent across every represented profile, return that relation directly. If whether any difference matters is unresolved, retain that gap rather than normalizing it away.

Define `U(x) = sum_i q_i(x_i)`, with higher value preferred. Each no-worse statement `x` versus `y` adds `U(x) >= U(y)`; indifference adds equality; strict preference adds `U(x) > U(y)`. Add elicited bounds or comparisons of value differences only with their own meaning and source. All rows constrain the same contributions. Solving them jointly supplies a family of additive value functions, rather than independently chosen intervals for each criterion. Weak monotonicity permits a flat contribution; require strict increase only where the holder's judgement supports it.

This construction leaves unevaluated levels open. Add a new level with its monotonicity and preference constraints, or use an explicitly justified interpolation. Equal spacing on an ordinal performance scale is not equal spacing in value. A family that is feasible at the represented levels establishes compatibility there; use beyond them needs the stated shape or new elicitation.

The constraints are linear in the unknown contributions. Use direct algebra for a small family or a linear-programming solver for the finite system. When strict comparisons are present, a solver can replace each strict difference by a common positive slack `epsilon` and maximize that slack under the normalization: a feasible result with `epsilon > 0` witnesses joint strictness. A fixed arbitrary margin can exclude compatible models. Preserve weak equalities and numerical error limits when interpreting a computation. `MMP.10` and `MMP.11` supply the general formulation, representation and obtaining-method work; the consequence meanings and preference assumptions supplied here govern this instance.

##### PSDA.6:4.5.4 - Distinguish an open answer from a failed construction

First check whether at least one model satisfies the joint constraints. For a small interval family, exhibit an admitted parameter; for a larger system, obtain a feasible witness or a justified infeasibility result. A solver timeout leaves this question unanswered.

If the family is empty, locate a conflicting subset of the elicited rows and form assumptions. Check transcription, units, profile meanings and attribution with the holder. Two opposite weak comparisons may express indifference; they are not a contradiction. A strict preference for `x` over `y` together with `y` no worse than `x` under the same conditions conflicts with the claimed preference relation. Other failures can arise because the chosen form cannot express otherwise coherent judgements. Do not resolve either failure by silently deleting a row or returning the best fitting weights. Revise a judgement only with its holder, change the form with an explicit basis, or return the unresolved conflict. An approximate fit needs an admitted error interpretation before it can support advice.

For a **nonempty** family, distinguish what all compatible models support from what at least one supports:

- `x` is **necessarily no worse** than `y` when every compatible model gives that weak preference.
- `x` is **possibly no worse** than `y` when at least one compatible model gives it.

Test these claims on the joint family. For the loss family, necessary preference requires `L_r(x) <= L_r(y)` for every `r` in `R`; a possible preference needs one such `r`. A proof over the range establishes necessity; one feasible witness establishes possibility and one contrary witness defeats necessity. Use `MATH.20` for the required whole-domain bound. Separate strict preference from equality at a boundary. An empty family warrants neither kind of recommendation.

If the question asks for a best alternative, keep the quantifiers together. A necessary best is no worse than every rival in every compatible model. A possible best is no worse than every rival in **one and the same** compatible model. Separate pairwise witnesses against different rivals do not establish possible best. Return a common best when supported, the condition-dependent alternatives otherwise, or the precise comparison gap. No probability distribution over the compatible models is implied.

##### PSDA.6:4.5.5 - Reopen only what the changed judgement affects

A further judgement by the same holder on the same profiles adds a constraint to the existing family. Intersect, check nonemptiness again, and recalculate the dependent comparisons. A correction replaces its old row and every restriction derived from it; retaining the superseded row could manufacture a conflict. Preserve consequence measurements, protected conditions and comparisons whose grounds remain valid.

A changed holder, horizon, range, consequence meaning or compensation rule can invalidate the representation itself. Reconsider that premise before intersecting parameters in the old form. State which results depend on it and which remain usable. Stop when the receiving comparison is settled to the needed strength or the missing judgement, form or authority is clear enough to obtain.

#### PSDA.6:4.6 - Return the account and its exact incompleteness

Return the attributed concerns and objectives; consequence meanings and measures; protected conditions and their sources; admitted trade-offs or preference relations; material interactions and dissent; unsupported transformations; and what would change the account. When a requirement's merits were in question, include the bounded appraisal return and the limit imposed by its current force from §4.4.

For a numerical construction, include the chosen form and its assumptions, the profiles and judgements constraining it, the joint compatible family or identified conflict, and the scope of any necessary or possible preference. `PSDA.8` may use it only for the named comparison. The account can support a partial order or leave a comparison unresolved. Missing preference information is not automatically missing empirical evidence: a further experiment may estimate consequences without deciding how they should be valued.

Recognition needs only a material ambiguity, duplication, or unexplained trade-off. Consequential reliance additionally needs qualified measurements, faithful elicitation, a justified aggregation Method when used, direct authority for binding conditions, and the applicable domain assurance. A readable value table satisfies none of those stronger claims by itself.

### PSDA.6:5 - Archetypal Grounding

#### PSDA.6:5.1 - Two meanings of flood service

In the illustrative flood-pump engagement, a residents' association emphasizes property protection, while a separately heard group of mobility-constrained residents emphasizes reachable assistance. The board is the later choice owner, not an assumed representative of every value judgement.

The analyst replaces a generic “service quality” score with this account:

| Concern | Consequence representation | Trade-off or qualification boundary |
| --- | --- | --- |
| Reduce property loss. | A qualified loss estimate for the affected properties and flood conditions. | The estimate is not evidence of reachable assistance; its valuation and uncertainty remain explicit. |
| Keep assistance reachable. | Whether the defined assistance service can reach the named population under the relevant access conditions. | The expressed concern is retained. Any binding access or safety condition needs its direct competent basis; it is not inferred from participation. |
| Maintain pumping service. | Hours of unavailability for the specified pumping service over the season. | This operational measure does not cover all property or human consequences. |
| Limit resource use. | Resources required by each whole arrangement, including continuing obligations and transition. | A cost preference does not permit violation of a separately established protected condition. |

The analyst removes a second “reliability benefit” entry that merely repeats the same pumping-service hours. Reachable assistance stays separate even if failures often occur in the same storms. That is not duplicate value.

If the board adopts a trade-off between operating-service hours and budget units for a narrow analytical slice, the account names that value judgement, range, and limit. It does not present the slice as the residents' common value function. If the association and the other group reject a common trade-off, the return carries separate accounts and a stated disagreement; another hydraulic simulation cannot resolve that disagreement.

#### PSDA.6:5.2 - Development directions do not share a universal improvement score

For the ninety-day service-organization case, a qualified strategy result gives reliability priority over throughput for the current horizon. That premise helps frame the comparison but does not supply numerical weights or a causal effect estimate.

| Proposed holder-specific input | What the value account may use | What it must not infer |
| --- | --- | --- |
| Human capability result for representative later Work. | The supported performance distinction and the person's relevant protected conditions. | Course attendance, assessment performance, retention, and transfer are not one interchangeable development value. |
| Organization result for positions, interfaces, and continuing service. | Contribution and service consequences for the named arrangement. | A local team's gain is not automatically a gain for the organization or another team. |
| AI/model evaluation for a named version and environment. | The qualified performance, resource, oversight, and failure distinctions. | A benchmark percentage is not a person's capability measure or the whole service's reliability. |

The adviser keeps those premises in their own meanings. A common service-level comparison is possible only after qualified domain results connect each direction to that same service and horizon. Without that connection, “human 4, organization 4, AI 4” is not a meaningful equal score. The return requests the missing consequence relation rather than normalizing the three numbers.

#### PSDA.6:5.3 - Cheap non-use

Two qualified replacement parts have the same relevant consequences except for a directly comparable resource cost, and the authorized recipient's cost preference is already explicit. Reuse that account. An objectives hierarchy and a fresh weighting workshop would add no value distinction.

#### PSDA.6:5.4 - Retain a protective restriction or revise a redundant control

These constructed variants concern a service team's proposed use of an external inference provider. In the first, a qualified configuration result shows that the proposed route exposes identifiable confidential incident records to provider staff who have no part in serving those clients. An available internal route meets the current service need within its support budget. The restriction prevents that disclosure; relaxing it for the faster external route would expose those clients without a corresponding needed service gain. The value account therefore supports retaining the restriction and excludes this external route for the current use. It does not infer that all provider configurations are unsuitable.

In the second variant, the configuration and access protection remain adequate. The disputed rule additionally requires three hours of manual transcription of an access log. Assume the competent review has established that the retained, inspectable electronic log covers the same events and that transcription adds no omitted event or distinct check. The same three hours would otherwise test a newly exposed, unreviewed access path to the same protected records. On these facts, retaining the extra transcription displaces more protective work without an identified protective gain. Recommend revising that requirement to use the qualified electronic record while keeping the actual access controls. If a missing event or an independent check is found, that premise changes the recommendation.

The rule owner cannot amend the transcription requirement before this decision. The recommendation is still complete, but it is not an exemption: present options must satisfy the rule or remain deferred. The lost testing opportunity remains a consequence of the present constraint. The contrasted results follow from the stipulated contribution and burden, not from the words security, digital or redundant.

#### PSDA.6:5.5 - Obtain an exchange family and use a new judgement

A service manager supplies one legitimate value account for a four-week arrangement. Known costs are in thousands of resource units, waiting times in hours. The relevant ranges are 20–60 and 1–5. Lower values are preferred. The manager explicitly accepts constant value increments and a constant cost-for-time exchange within these ranges. Those are the form assumptions; the following comparisons constrain its parameters.

| Alternative | Cost `c` | Waiting time `t` | Eligibility for this comparison |
| --- | ---: | ---: | --- |
| A | 60 | 2 | Admissible. |
| B | 30 | 5 | Admissible. |
| C | 45 | 3 | Admissible. |
| D | — | — | Fails a currently binding access condition; no timely amendment is available. |

The manager says that `(60,1)` is no worse than `(20,5)`, and `(20,4)` is no worse than `(60,2)`. Applying §4.5.2 gives:

| Stated judgement | Joint constraint | Consequence for `r` |
| --- | --- | --- |
| `(60,1)` no worse than `(20,5)` | `60 + r <= 20 + 5r` | `r >= 10` |
| `(20,4)` no worse than `(60,2)` | `20 + 4r <= 60 + 2r` | `r <= 20` |

Thus `L_r(c,t) = c + r t` with `10 <= r <= 20` is the compatible family. It is nonempty: both endpoints satisfy both weak comparisons. No interview is available to choose a narrower exchange. In normalized range weights the same family has `1/3 <= w_c <= 1/2`, with `w_t = 1-w_c`; those numbers were derived from the profiles, not assigned to criterion labels.

The receiving `PSDA.8` comparison keeps one shared `r`:

| Difference over the whole family | Consequence |
| --- | --- |
| `L_B - L_C = 2r - 15`, between 5 and 25 | C is strictly preferred to B throughout. |
| `L_B - L_A = 3r - 30`, between 0 and 30 | A is no worse than B throughout, with a tie at `r = 10`. |
| `L_A - L_C = 15 - r`, between -5 and 5 | C is better below 15; A is better above 15; they tie at 15. |

These linear differences establish the signs over the entire interval. At `r = 10`, the losses for A, B and C are 80, 80 and 75; at `r = 20`, they are 100, 130 and 105. Both exchanges satisfy the elicited information but give different best alternatives. The `PSDA.9` sensitivity result is therefore the threshold 15 thousand per hour, and the `PSDA.14` return is the conditional set `{A,C}`. B cannot be best in any compatible model; D remains ineligible. Choosing `r = 15` merely because it is the interval's midpoint would add unsupported indifference.

Later the same manager states that C is no worse than A. Its new row is `45 + 3r <= 60 + 2r`, hence `r <= 15`. Intersecting gives `[10,15]`. Now `L_A-L_C` lies in `[0,5]` and `L_B-L_C` in `[5,15]`: C is no worse than A and strictly better than B for every compatible exchange. C is a necessary best, while `{A,C}` remains the set of possible best alternatives because A ties at 15. Return C as a supported direction with that tie intact. The new judgement changed the value family and its comparison; it changed neither the consequences nor D's access failure. The recommendation still leaves the authorized recipient's later choice distinct.

#### PSDA.6:5.6 - A failed affine form is not automatically contradictory judgement

Consider a different continuation from the original `[10,20]` family. The manager additionally says that `(20,5)` is no worse than `(44,2)`. In the affine form this yields `20 + 5r <= 44 + 2r`, or `r <= 8`. That row and the first original row `r >= 10` cannot hold together. Return this specific conflict; the former comparison no longer has a compatible affine basis.

Ask whether the equal-increment assumption still expresses the manager's values. They may care much more about reducing two hours to one than about reducing five hours to two. For example, a curved time-loss contribution taking values `0,20,28,36,44` at times `1,2,3,4,5`, with loss `c + h(t)`, satisfies all three profile comparisons: `60 <= 64`, `56 <= 80` and `64 <= 64`. This constructed witness proves only that those three judgements need not contradict one another. It is not an elicited curve and supplies no recommendation by itself.

If the manager withdraws constant time increments but retains addition, §4.5.3 constructs the whole compatible monotone family at the relevant levels. If the manager instead states the noncompensatory two-hour rule in §4.5.1, that different value account prefers A to B and C directly. Either change needs its stated basis; neither is a convenient parameter adjustment inside the old affine model. If no clarification is available, retain the attributed comparisons, D's independently established exclusion and the exact failed form. Return the numerical ranking as unresolved.

### PSDA.6:6 - Bias-Annotation

**Scope:** value representation for one bounded comparison. **Lenses:** **Onto/Epist** separates concern, measure, preference, and obligation; **Prag** preserves decision relevance; **Gov** exposes representation and authority; **Did** makes trade-offs concrete.

Template bias imports irrelevant criteria. Proxy bias rewards what is easy to count. Splitting one objective into many criteria can change its apparent importance. Sponsor averaging can conceal who bears a loss. Counter these by returning to attributed consequences, inspecting overlaps, and retaining disagreement and missingness. Do not replace one template with a mandatory elaborate hierarchy.

### PSDA.6:7 - Conformance Checklist

- [ ] Values are attributed to the relevant subjects and receiving comparison, with representation limits intact.
- [ ] Objectives and possible means remain distinct at the grain that changes the decision.
- [ ] Repeated consequences are not counted twice; correlation alone does not justify deletion.
- [ ] Measures retain subject, scale, unit, horizon, evidence, proxy limits, and missingness.
- [ ] Binding conditions, aspirations, and unresolved authority questions are distinguished. A live merits question receives an appraisal of protective contribution and burden, with a supported recommendation and unchanged current force.
- [ ] Value transformations and weights have declared ranges and an elicitation basis; the chosen form is justified separately from fitting its parameters.
- [ ] The numerical family preserves the joint judgements, has a checked feasibility result, and distinguishes incomplete information from contradictory judgements or a failed form.
- [ ] Necessary and possible comparisons retain their quantifiers, ties and dependence on the same compatible model. A changed judgement reopens only dependent results unless it changes the form itself.
- [ ] Interactions and refusals to compensate are preserved.
- [ ] Any collective aggregation has an explicit basis; incompatible accounts remain visible otherwise.
- [ ] The return states partiality, dissent, direct-source gaps, and exact reopen conditions.
- [ ] A supported preference comparison covers only its attributed account and supplied consequences; authorization of the later choice and a claim of effect need their own grounds.

### PSDA.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Everyone agrees safety is important, so give it twenty percent.” | Recover the actual condition, its source, and whether compensation is permitted. |
| “Equal weights are neutral.” | State the consequence ranges and inspect how criterion splitting changes the result. |
| “These two measures correlate, so one is redundant.” | Examine whether they represent the same valued consequence. |
| “Normalize everything to zero–one.” | Establish value meaning and admissible operations before any transformation. |
| “The workshop mean is the public preference.” | Preserve attribution and require an explicit aggregation basis. |
| “Collect more data to resolve the value dispute.” | Identify whether the missing input is evidence, preference, representation, or authority. |

### PSDA.6:9 - Consequences

The comparison becomes open about what it values and what it cannot exchange. Simplifying the account can reduce burden without losing material distinctions. Some decisions remain partially ordered or disputed; that is a truthful result, although it may be less convenient than a single score.

### PSDA.6:10 - Rationale

Value representation makes consequences decision-relevant without confusing description with preference or preference with permission. Concrete trade-off questions expose assumptions hidden by criterion labels. Preserving multiple admissible accounts lets later comparison show where a conclusion is shared and where it depends on a disputed judgement.

### PSDA.6:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How can objectives be concise without omitting what matters? | Inspect means–ends structure, relevance, overlaps, and sensitivity to simplification. | Retain an exhaustive descriptive hierarchy, or delete criteria by correlation alone. | **Adapt:** :4.2–:4.3 keep a small consequence-led account and test any lost distinction. More analyst attention is accepted where it prevents double counting; small clear cases remain short. | Marttunen et al.'s [2019 objectives-hierarchy study](https://doi.org/10.1016/j.ejor.2019.02.039) supplies the comparative methods and retrospective environmental cases. It supports disciplined simplification, not one optimal hierarchy or a statistical license to discard values. | Reopen when a removed distinction can reverse the comparison or a lighter structure preserves the same concerns. |
| Must incomplete preferences become one weighted score? | Construct the preference model from consequence comparisons and use all compatible instances. | Fit one additive score, average weights, or retain a noncompensatory rule when that better expresses the judgement. | **Adapt:** :4.5.1–:4.5.5 develop form selection, joint constraints, feasibility, necessary/possible comparison and local revision; :5.5–:5.6 show a complete use and failure of the affine form. The trade-off is a potentially less decisive answer for less invented precision. | Greco, Słowiński and Wallenius's [2025 MCDA review](https://doi.org/10.1016/j.ejor.2024.07.038), especially §3.1.2 and §7.1 ([accessible author-hosted PDF](https://www.iris.unict.it/retrieve/cb6fc63a-f16d-4c14-a163-46b863c27dc9/1-s2.0-S0377221724005988-main.pdf)), supplies preference assessment and robust ordinal regression. Its rules and non-additive families remain serious alternatives. The two-criterion derivation and service cases here are bounded applications, not its empirical findings or a universal additive-representation theorem. | Reopen when new judgement changes the compatible set, an interaction defeats the form, or the holder, range or governing condition changes. |
| Can common coordinates perform the value judgement? | Declare meanings and scales separately from preference, comparison, and selection. | Treat a dashboard or normalized vector as the decision model. | **Adopt:** :4.3 uses A.19 only for the declared space or predicate and leaves value elicitation here. The distinction adds little effort to an existing table and prevents a false consumer result. | Current `A.19`, `C.16`, and the direct comparison patterns supply the relevant typing and operation boundaries. They do not elicit the engagement's values or authorize a trade-off. | Reopen when the scale, predicate, consequence range, or receiving use changes. |

### PSDA.6:12 - Relations

- `PSDA.12` may supply the participation and concern account that changes the value question. That contribution is not already a weight set or a collective mandate.
- `PSDA.8` consumes the value account and its admitted preference relation for the named comparison; `PSDA.9` tests its dependence on the compatible family, and `PSDA.14` uses the supported direction, conditional set or gap.
- `MMP.10` and `MMP.11` supply general constraint and model-family construction after the value meanings and form conditions in §4.5 are established. `MATH.20` supplies bounds over the admitted domain; none of these suppliers elicits the holder's preferences.
- `C.16` governs measurements; `A.19` supplies a declared characteristic space or predicate when needed. Scoring, aggregation, comparison, and selection remain separate direct operations.
- Direct ethics, law, safety, governance, finance, and holder practices supply the particular conditions and claims they own. `A.15.9` helps obtain a missing qualified contribution without transferring that authority.
- If a required value or source premise is absent, stale, or incompatible, use a qualified direct result or return its exact gap. A completed model, candidate list, or workshop does not fill it by adjacency.

### PSDA.6:End

## PSDA.7 - Represent Decision-Relevant Uncertainty and Evidence Limits

> **Type:** Method pattern body
> **Status:** Stable
>
> **Primary working result:** **bounded decision claims and unresolved discriminating questions**: what the evidence supports about the live alternatives, what could change that comparison, and which uncertainty cannot presently be resolved.

### PSDA.7:1 - Problem frame

**Use this when** a point estimate, “high confidence” label, or model output makes a decision look more settled than its evidence permits. Also use it when a long uncertainty list does not say which unknown could reverse, narrow, defer, or invalidate the decision-support return.

Take one relied-on claim and ask: if this claim were different within its supported limits, what would change about these alternatives or their admissibility? State the supported claim and the remaining question together. The gain is a useful uncertainty account, not the impossible removal of all uncertainty.

The governed object is that decision-linked account. A claim about an uncertain consequence, an attributed belief, a model assumption, missing evidence, and a disputed value are different inputs. Their relevance to one decision does not turn them into one probability or a common confidence score.

**Do not use this pattern** when the only question is a source's provenance or currentness and no decision-support comparison changes; use `A.10` or the direct source practice. If the uncertainty account already supports the present use, reuse it. Direct domain practices retain their own measurement, forecasting, causal, safety, and evidential conclusions.

### PSDA.7:2 - Problem

A numerical estimate can hide the conditions under which it is meaningful. An access model may estimate arrival time only when the road is open; a training study may concern an immediate test rather than later Work; an AI evaluation may concern a previous version or operating distribution. Averaging the results does not repair their missing applicability.

Conversely, a demand for certainty can stop every useful return. Some uncertainty cannot change the ordering, while another can show that all alternatives fail a protected condition. A useful account distinguishes those cases. It also separates a question that better evidence can answer from a disagreement about values or authority that evidence alone cannot settle.

### PSDA.7:3 - Forces

| Force | Tension |
| --- | --- |
| Qualification and action | A decision needs bounded support, not complete knowledge, while an unsupported premise can make action indefensible. |
| Probability and ignorance | Probabilities can represent uncertainty well when justified, while invented distributions hide model disagreement or lack of knowledge. |
| Reduction and relevance | More information may narrow an estimate without changing any available decision. |
| Shared evidence and corroboration | Several sources can provide distinct support or merely repeat the same data and assumptions. |
| Stable comparison and changing conditions | Alternatives need a compatible basis, while source, holder, and environment changes can invalidate that basis. |

### PSDA.7:4 - Solution

Connect each material uncertainty to the exact claim and decision it can change. Use a representation justified by the available knowledge, retain dependencies and limits, and return a bounded claim, discriminating question, narrowed use, or blocker.

#### PSDA.7:4.1 - Start from a comparison that could change

Name the subject, configuration, horizon, receiving question, considered alternatives, and result currently being claimed. Ask which premise could change their consequences, relative standing, eligibility, or the need for a probe. If the alternatives themselves are unclear, return that candidate question.

Use `PSDA.3`'s model account only where its evidence or assumptions bear on this same configuration and horizon. The model can expose an uncertainty without resolving it. A current qualified direct result can supply the same premise without requiring a model-building exercise.

Check both relative and absolute consequences. An uncertainty shared by all alternatives can leave their order unchanged yet show that none meets a required service or safety condition. Do not dismiss it as irrelevant merely because it is not a ranking discriminator.

#### PSDA.7:4.2 - Represent what is unknown at its actual kind

Choose a form that answers the live question without claiming more knowledge than exists.

| Available basis | Useful representation | Limit that must remain visible |
| --- | --- | --- |
| Qualified stochastic model or elicited probabilistic judgement. | A distribution or probability statement tied to its event, population, conditions, and horizon. | Calibration, sampling, elicitation, model assumptions, and applicability still matter. Confidence in the analyst is not the event probability. |
| Supported bounds but no distribution. | An interval or set of admissible values. | An interval is not a uniform distribution; state what supports its endpoints and what lies outside its claim. |
| Several materially different models or future conditions. | Conditional claims under named models or scenarios. | Their count or frequency in an ensemble does not supply real-world likelihood. |
| A decisive absent result or unrepresented mechanism. | The exact missing claim and the comparison it prevents. | A blank cell is neither zero effect nor equal performance. |
| Incompatible interpretations, preferences, or authority claims. | Attributed alternatives and the unresolved interpretation or judgement. | Statistical uncertainty reduction alone cannot reconcile them. |

These are use choices, not a universal taxonomy of uncertainty. Different forms may coexist in one account. Distinguish a physical or behavioral variability claim from uncertainty about its model, data, or applicability whenever the distinction changes the return.

If a probability is useful but unsupported, state the conditional comparison it would enable and identify the needed basis. Do not assign equal probabilities to scenarios simply to make an expected-value calculation run.

#### PSDA.7:4.3 - Qualify the relied-on claims

For each decision-bearing source result, keep the claim, subject, supplying result kind, source edition or effective window, assumptions, evidence, intended use, exclusions, and material dissent recoverable. Use `A.10` for the actual bounded reliance question; its disposition does not establish the source claim's truth or authorize the decision.

Ask whether the evidence concerns the same holder, intervention, environment, and horizon. Separate observed results, forecasts, expert judgements, and unsupported extrapolations. An observation of a benefit is not automatically a causal effect; the direct causal or domain Method supplies that support.

Use an already-qualified result within its limit. If a consequential cross-practice result is still missing, `A.15.9` supports the smallest request or blocker. Do not ask another practice to “remove the uncertainty”; ask for the specific claim, bound, interpretation, or test that could change this comparison.

#### PSDA.7:4.4 - Preserve dependency and model disagreement

Recover shared data, common causes, conditional assumptions, and other dependencies when they affect the consequence comparison. Evidence repeated by several models is not several independent confirmations. Expert or model aggregation needs its own justified Method; the number of voices alone does not determine a probability.

Keep incompatible assumptions separate until a direct result supports their combination. For example, a scenario with a failed access route and a scenario with a functioning route can test different claims; combining their most favorable outcomes produces no realizable case.

Where alternative models disagree, identify the overlapping proposition and what explains the difference: scope, input, representation, mechanism, or unresolved evidence. A new measurement may discriminate the models; sometimes the honest answer is that the present use must retain both. Do not turn disagreement into a narrow average solely because a downstream table expects one number.

#### PSDA.7:4.5 - Form a discriminating question

Write the question in terms of its possible consequences for the current return:

> For this subject and horizon, establish whether this premise lies inside the region supporting alternative A, outside it, or remains unresolved; state the evidence and limits needed for that use.

The requested result may concern eligibility rather than ranking. It may also show that no available alternative works, that a different formulation is needed, or that only a reversible analytical use is supported.

Name a feasible observation, calculation, interpretation, or comparison that might answer the question, its supplying practice, and the relevant time or access limit. If no feasible inquiry can answer before the decision window closes, say so. Do not promise that more data will settle structural ignorance.

This pattern identifies decision-linked questions. `PSDA.9` can later examine reversals and information priorities; `C.11` or the direct choice owner decides whether an actual next probe is worth its cost and authorized. A question with high uncertainty is not automatically the best probe.

#### PSDA.7:4.6 - Return the strongest supported claim and no stronger

A short return states:

- what claim about which alternatives is supported, for which configuration and horizon;
- its uncertainty representation, source limits, and dependencies;
- what different answer could change the comparison, admissibility, or receiving use;
- the exact unanswered question or blocker; and
- what source, observation, candidate, value, or configuration change would reopen the account.

Return “unchanged within the tested bounds” only when those bounds cannot alter the stated result. Return a conditional or narrowed claim when support covers only part of the use. If a required protected-condition premise is unsupported, preserve the direct domain stop rather than compensating with confidence elsewhere.

Recognition may begin with one unexplained estimate. Consequential reliance requires the evidence and assurance demanded by the direct practice, including its independent checks when applicable. This pattern supplies no universal evidence score or acceptable uncertainty threshold.

When a relied-on source actually changes, revalidate the affected use. Use `G.11` for a currentness question and `A.10.1` when the changed claim must be traced through several actual uses. Do not discard unrelated claims merely because they share a source file.

### PSDA.7:5 - Archetypal Grounding

#### PSDA.7:5.1 - Which flood-pump uncertainty matters now?

In the illustrative pre-season inquiry, nominal permanent and mobile capacity meets the assumed inflow only with the stated units operating. The model omits arrival delay. The team cannot turn that conditional result into “mobile service is reliable”.

| Relied-on or proposed claim | Evidence limit | Decision-linked return |
| --- | --- | --- |
| Nominal mobile capacity is adequate. | The capacity calculation assumes operating units on site. | Use for capacity only. It does not discriminate the missing deployment arrangement. |
| Mobile units can serve the district after road loss. | No qualified arrival and deployment result exists for that condition. | Ask for the route-loss deployment result; M remains conditional for the service comparison. |
| The two technical models corroborate the inflow assumption. | They reuse the same inflow dataset. | Retain one shared evidence dependency, not two confirmations. |
| Pumping-service hours represent all affected residents' loss. | Reachable assistance and property protection have different meanings. | Return the missing consequence relation or keep separate accounts; a tighter inflow estimate will not settle the value question. |

If a direct deployment result later supports a bounded arrival range, the account changes only the affected claim and its uses. If the range still spans service failure, the result is a discriminating question for robustness, not an unconditional feasibility claim. If all arrangements share an unsupported power-supply assumption, that common uncertainty can invalidate all of them even while their relative order stays fixed.

#### PSDA.7:5.2 - Development evidence with three different limits

For a ninety-day organization recommendation, suppose the adviser has an immediate human assessment, a queue model for the current team, and an offline AI benchmark. Each can inform a different bounded claim.

The human assessment does not establish retention or transfer to later service Work. The queue model does not establish the performance of a reallocated or mixed arrangement without its staffing and interaction premises. The benchmark does not establish current-version service reliability under the operating distribution and oversight arrangement.

The return names three possible supplier questions at their own grain: representative later-Work capability, changed-arrangement service consequences, and exact-version operating evaluation. Only questions that could change the live recommendation are pursued. Averaging the three “confidence” labels would repair none of these gaps.

#### PSDA.7:5.3 - A bounded input to SensorCo's strategic commitment

SensorCo's illustrative twelve-month question concerns defending devices, offering an integrated service, licensing data, or exiting a segment as generic AI inspection prices fall. The strategy team owns the strategic comparison; the board separately holds commitment authority.

Suppose the integrated-service direction relies on an uncertain repeat-demand claim, while the licensing direction relies on a still-unqualified permission premise. The PSDA return names the repeat-demand conditions that could alter the service comparison and the exact rights interpretation missing for licensing. It supplies neither the strategic facts nor a permission judgement by itself.

Under the decision-linked uncertainty relation, `STR.11` may use the supplied result only for this commitment and compatible horizon. A changed alternative, claim scope, demand question, evidence window, or commitment reopens that use. If the result is unavailable or incompatible, the strategic receiver uses a qualified direct source or keeps the exact gap; a MethodDescription or analogy is no substitute for the result.

#### PSDA.7:5.4 - Cheap non-use

An analyst needs to recover which calibration edition a measurement cites, and no candidate comparison is being made. Use the source and evidence practice directly. A decision-linked uncertainty account would add no current result.

### PSDA.7:6 - Bias-Annotation

**Scope:** uncertainties that can change a bounded decision-support return. **Lenses:** **Epist** separates evidence and belief; **Prag** tests action-changing relevance; **Arch** exposes dependencies; **Gov** preserves direct authority and protected conditions; **Did** makes an unknown into a useful question.

Precision bias favors a number over an honest set or gap. Confidence rhetoric can substitute reputation for evidence. Model averaging can conceal shared errors. Certainty seeking can consume the entire decision window. Counter these with exact conditional claims and an explicit account of what a different answer would change.

### PSDA.7:7 - Conformance Checklist

- [ ] Each material uncertainty is linked to a claim, alternatives, configuration, horizon, and receiving use.
- [ ] The account tests eligibility and shared failure as well as ranking changes.
- [ ] Probabilities, intervals, scenarios, missing results, and disputes retain their different meanings.
- [ ] Every probability or bound has an adequate basis; scenario counts are not probabilities by default.
- [ ] Source, holder, intervention, and environment limits accompany relied-on evidence.
- [ ] Shared evidence, common causes, and incompatible model assumptions remain visible.
- [ ] Each proposed inquiry names a result that could change the return and a feasible limit or honest inability.
- [ ] The disposition is bounded, conditional, narrowed, or blocked as the actual support requires.
- [ ] Direct assurance, permission, and choice are not inferred from an uncertainty account.
- [ ] Changed sources reopen only affected uses, with their own subject judgements.

### PSDA.7:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Confidence is eighty percent.” | Say whose judgement, about which proposition, under what evidence and probability interpretation. |
| Give three scenarios equal probability because three were drawn. | Retain scenario-conditional claims until a distribution is justified. |
| Average incompatible model outputs. | Locate the disputed proposition and keep the alternative assumptions or exact gap. |
| Discard uncertainty common to all candidates. | Check whether it changes absolute admissibility or shows that all fail. |
| Commission more data without a decision question. | State which possible answer could change the comparison or its use. |
| Replace missing holder evidence with another holder's success. | Request the exact transfer or applicability result; retain the blocker if it is unavailable. |

### PSDA.7:9 - Consequences

The recipient can see what is known well enough for this decision and which unknown deserves attention. Some numerical precision is lost, but unsupported certainty is removed. The work can become smaller: once an uncertainty cannot change the bounded return, further refinement needs another justification.

### PSDA.7:10 - Rationale

Uncertainty matters through its effect on a decision claim, not through its size alone. Preserving the source, representation, and dependency of each premise makes that effect inspectable. A bounded unknown can support useful inquiry without pretending to supply the missing fact or the eventual choice.

### PSDA.7:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| When should uncertainty be probabilistic, and when should alternatives remain conditional? | Use qualified probabilistic analysis where its premises hold; retain multiple plausible conditions when decision-relevant probabilities or models are unsettled. | Predict-then-act under one agreed forecast, or reject all probabilistic reasoning whenever uncertainty is difficult. | **Adapt:** :4.1–:4.4 select the representation by the actual basis and test shared failure. Additional scenario work is accepted only when one forecast could conceal a material reversal. | Lempert et al.'s [2024 DMDU/IPCC analysis](https://doi.org/10.3389/fclim.2024.1380054) is the synthesis candidate for decision relevance despite low-confidence knowledge. It does not make scenarios equiprobable or provide a universal uncertainty taxonomy or local risk threshold. | Reopen when a qualified distribution becomes available, model disagreement changes, or an omitted future defeats the claimed bounds. |
| Which missing evidence deserves a question? | Connect elicitation, sensitivity, and information acquisition to the alternatives and consequences they can change. | Rank unknowns by variance or confidence alone. | **Adapt:** :4.5–:4.6 require a discriminating question before further inquiry. The practical trade-off is less general data collection for a more explicit decision boundary. | Borgonovo et al.'s [2026 review](https://doi.org/10.1016/j.ejor.2025.05.023) supplies the current decision-analysis connection among uncertainty, sensitivity, and information value. It is a synthesis, not validation of PSDA's particular evidence or a universal probe rule. `A.10` supplies only bounded reliance; `C.11` retains actual local probe choice. | Reopen if another unknown can change eligibility, a model revision changes the discriminator, or no feasible inquiry fits the decision window. |

### PSDA.7:12 - Relations

- `PSDA.3` may supply model evidence and assumptions for the same configuration and horizon. Representation alone establishes neither the subject condition nor this uncertainty judgement.
- `PSDA.8` may use the bounded claims and questions where they change its consequence comparison. Evidence neither entails that result nor authorizes the later decision.
- `STR.11` may use a supplied decision-linked uncertainty result only where it can change the strategic commitment comparison. The result carries its own scope and horizon; it imports neither the whole PSDA practice nor strategic facts or authority.
- `A.10` governs claim-bound evidence and reliance; `A.15.9` governs a needed outside-practice request or use. `G.11` and, for several actual changed uses, `A.10.1` govern currentness and affected-use revalidation.
- `PSDA.9` owns the distinct robustness and information-priority question. `C.11` or the direct decision owner governs an actual probe or choice. Missing, stale, or incompatible inputs remain exact gaps unless a qualified direct result supplies them.

### PSDA.7:End

## PSDA.8 - Compare Consequences of Decision Alternatives

> **Type:** Method pattern body
> **Status:** Stable
>
> **Primary working result:** an **inspectable consequence comparison** for exact alternatives, affected subjects, conditions, horizon, value accounts, and evidence, including the relations that hold and those that remain unresolved.

### PSDA.8:1 - Problem frame

**Use this when** alternatives have been named or ranked but nobody can reconstruct what each would change, for whom, over what time, and under which assumptions. Also use it when a development direction looks attractive from one component's score while its service, transition, interaction, or protected-condition consequences remain absent.

Begin with one alternative and one consequence that matters. Trace the proposed change through its supported mechanism and conditions to the affected subject, then compare that same consequence for the other alternatives. The gain is a comparison that explains its result and its limits.

The governed object is the consequence comparison, not the future outcome or the authorized choice. A consequence claim may be a forecast, conditional model result, observation, or unsupported hypothesis.

**Do not use this pattern** when a current qualified comparison already covers the exact alternatives and receiving use. Use the direct domain Method for a single missing calculation or effect estimate. If the only remaining question is the authorized choice among adequate options, use `C.11` or the direct decision guidance.

### PSDA.8:2 - Problem

A rank can hide an incomplete causal story. A larger pump does not by itself establish delivered flood service. A better-trained worker does not by itself remove a queue constrained by interfaces. A stronger model benchmark does not establish reliability of the deployed service arrangement.

Even accurate separate estimates can form a false comparison. Alternatives may use different baselines, populations, operating assumptions, or horizons. Shared benefits can be counted twice, losses shifted to excluded people, and an average used to hide a tail or distributional difference. The missing work is a consequence account on a compatible basis, not merely a more sophisticated ranking algorithm.

### PSDA.8:3 - Forces

| Force | Tension |
| --- | --- |
| Common basis and real difference | Alternatives need comparable questions, while their mechanisms and affected subjects can genuinely differ. |
| Detail and affordability | Transition, distribution, and dependencies may reverse a conclusion, while exhaustive modeling can miss the decision window. |
| Multiple values and synthesis | A recipient needs a usable comparison without losing protected conditions or incompatible value accounts. |
| Prediction and evidence | A conditional model can inform a future choice without becoming an observed or causal result. |
| Precision and partiality | Numerical relations can clarify a comparison, while absent or incompatible evidence may leave no defensible total order. |

### PSDA.8:4 - Solution

Build consequence claims for the same receiving question, align only the meanings that can be aligned, apply the declared comparison rule, and return the supported relation together with uncertainty, dissent, and exact gaps.

#### PSDA.8:4.1 - Fix the comparison, not just its column names

Name the recipient question, subject or holder, current configuration, horizon, relevant affected subjects, and exact alternatives. Use `PSDA.5`'s set only as the candidate family; generation supplies no ranking. A proposal missing a decisive premise remains conditional rather than silently joining the eligible set.

Use `PSDA.6`'s value account only for this comparison. Keep its attributed values, protected conditions, scales, and unagreed trade-offs. Use `PSDA.7`'s bounded claims and discriminating questions only where their evidence concerns the same configuration and horizon.

These inputs can come from current qualified direct sources. If one is absent, stale, or incompatible, return the exact missing premise or narrow the comparison. Do not infer a usable value account from a workshop or a qualified forecast from a diagram.

#### PSDA.8:4.2 - Establish consequence paths at the needed grain

For each material alternative, connect the proposed change to intermediate conditions and the consequences that the value account actually uses. Identify who or what bears each consequence, when it appears, whether it persists, and which enabling conditions it needs.

Include transition burdens, delayed effects, and shifted losses when they can alter the comparison. Distinguish the present arrangement from an empty or ideal baseline. Use `C.11.CRC` when the missing input is specifically a finite change's contribution relative to the current configuration; reuse an already adequate contribution claim rather than reconstructing it.

Direct domain models and evidence supply effect estimates and mechanisms. A causal arrow or before–after difference is not sufficient causal support; use the direct causal or field guidance for a causal claim. A qualitative pathway can still identify a missing relationship without estimating its magnitude.

Do not extend a consequence beyond its qualified horizon without a stated model and source. If a short operating horizon excludes a material long-term lock-in or displaced loss, expose the exclusion and reopen the boundary where necessary.

##### PSDA.8:4.2.1 - Construct and question a qualitative consequence network

Use this branch when the important consequences are understandable in ordinary terms but no qualified model yet connects the alternatives to them. It returns conditional consequence profiles and precise questions for investigation. It does not turn an elicited relationship into an established causal law. Reuse a sufficient domain model instead; use a quantitative or dynamic model when timing, magnitude, feedback or joint risk decides the answer.

1. **Recover the participants' reasons.** For each affected party, name the desired state, the proposed action, any required resource and the quality by which that party would judge the result. Ask both “why is this needed?” and “how could it be obtained?” Attribute each answer; a modeler's hypothesis about another person's intention stays a hypothesis. Separate a required result from a prescribed task: two ways may obtain the same result while distributing work and discretion differently.
2. **Construct explicit relationships.** Write each important arrow as a sentence. For an external provision, identify who needs what, why, who could supply it and through which work. For a necessary combination, state which conditions must hold together; for alternative means, state whether either suffices and whether both may coexist. For a quality contribution, explain how an action or intermediate condition supports or impairs that quality. Keep necessity, sufficiency and a merely favorable contribution distinct. Name the conditions and evidence or attributed judgement supporting each sentence. A plausible relationship without support remains an open relationship.
3. **Check the network before using it.** Trace each material consequence to the alternative and to the affected party's criterion. Ask the provider whether the proposed provision is possible and the affected party whether the criterion and stated effect capture their concern. Inspect missing intermediate steps, double-counted paths and contradictory accounts. Do not repair disagreement by deleting one party. If a cycle matters, bound its time steps or obtain an appropriate model; repeatedly circulating a favorable label supplies no additional evidence.
4. **Evaluate one complete alternative at a time.** Hold its configuration and initial assumptions fixed. Carry established or conditional results through necessary combinations and alternative means using their stated meanings. A necessary unfulfilled condition blocks the claimed conjunction; an unknown necessary condition leaves that conjunction unsupported unless another condition already defeats it. One sufficient supported route can establish the stated disjunction even when another route remains unknown. If no route is supported and at least one remains unknown, retain the unresolved result; if every modeled route fails, that modeled disjunction fails. Apply the same discipline to external provision: the receiver's result cannot be established through a provision whose availability is unknown. For contributions, retain the incoming supporting, opposing and unknown grounds together before judging the destination. Do not add signs, count arrows, or promote several weak claims to a strong claim merely because there are several. Distinguish no investigation, an investigated but unknown effect, and opposed grounds.
5. **Ask a question that can settle the disputed transition.** Present the affected person or qualified source with the actual incoming grounds and criterion: would these conditions suffice, only help, obstruct, or leave this outcome unresolved, and why? Record the answer, its scope and dissent. An acceptable judgement may retain a conflict or say that no conclusion is supported. If an unexpectedly favorable or unfavorable result exposes a missing condition, return to the relationship or source rather than adjust the final label to match expectations.
6. **Compare the resulting profiles.** Apply :4.3–:4.5 to the same consequences for all alternatives. Keep a supported trade-off separate from an unknown effect that could reverse it. Return the explanation paths with the profile; a diagram is optional. Mark any judgement on which the comparison depends so that the recipient can challenge it.
7. **Work backward only when the question requires it.** If the recipient asks how several desired conditions could hold together, trace their necessary conditions and candidate sufficient routes backward. Propose a combination of means, ask what incoming conditions would justify each disputed intermediate judgement, then test the whole combination forward under the same assumptions. Set aside a combination with an incompatible condition. Keep a combination with an unsupported decisive transition conditional, naming the missing relationship instead of treating missing evidence as refutation. A failed current combination is not proof that every possible design fails. Do not weaken the recipient's criterion merely to find a solution.
8. **Revise by dependence.** When a source or judgement changes, identify the changed relationship, rerun its downstream consequences for affected alternatives, and recheck the comparison. Reopen the boundary if an omitted party or consequence appears. Preserve independent claims and the earlier result with its earlier conditions.

Use ordinary prose categories appropriate to the subject. If a named language or solver is used, declare its version, propagation rules, treatment of unknown and conflicting evidence, and structural restrictions. A solver's satisfying assignment is a model result, not a commitment by participants or evidence that the arrangement will work.

For an inquiry that also needs to construct and question the underlying actors-and-goals model, the Reference's [goals-and-dependencies walkthrough (Engineering.Reference:20)](Engineering%20DPF%20Suite/ENGINEERING-DPF-SUITE-REFERENCE.md#engineeringreference20---explore-a-situation-through-goals-and-dependencies) connects this branch to the inquiry's purpose, model views, explicit initial assumptions and a return from unexpected results to new source questions. It follows a staffing conflict through a revised allocation and its limited use. The present branch supplies the consequence analysis within that larger inquiry.

#### PSDA.8:4.3 - Construct a consequence account before aggregating

Keep each alternative's material consequence profile visible. For every relied-on entry, show the relevant subject, meaning, unit or category, condition or scenario, time, source, uncertainty, and missingness. A short parallel description can suffice; use a table when it makes repeated comparisons clearer.

Separate physical or service consequences from how they are valued. A budget estimate, hours of service loss, a probability distribution, and a consent condition do not become interchangeable because they occupy adjacent columns. A lower cost can be compared directly under its scale while a disputed value trade-off remains unresolved.

Where there is a distribution, preserve its event definition and dependence on the alternative and conditions. Expected values alone are insufficient when a tail, threshold, reversibility, or distribution across affected subjects can change the decision. Where no distribution is justified, retain conditional scenarios or bounds.

A missing value is unknown, not zero or equal to the competing alternative. A qualified narrower slice remains usable only with its excluded consequences explicit.

#### PSDA.8:4.4 - Check dependencies and shared burdens

Ask whether consequences share a cause, depend on the same resource, overlap in their accounting, or change under combination. A human–tool arrangement needs a whole-arrangement result; adding a worker's effect to a tool's effect can omit coordination loss or count the same resolved case twice.

Use the dependence structure required by the selected model. Do not assume independent failures simply because separate estimates exist. Linearity can justify adding expected contributions without independence, but it does not justify duplicated quantities, unsupported causal contributions, or a joint tail probability.

Inspect whether a claimed dominance survives the common conditions. Different favorable assumptions for different alternatives produce no fair comparison. If a required correspondence or joint model is missing, keep the particular relation unresolved.

#### PSDA.8:4.5 - Apply only an admitted comparison rule

State what “better”, “equivalent”, “dominated”, or “incomparable” means for this use. A coordinatewise comparison may establish that one alternative is no worse on every included coordinate and better on at least one. That conclusion remains limited to those coordinates, conditions, and admissible alternatives; it is not an overall recommendation.

Use the current value account for any compensatory score, priority rule, threshold, or outranking Method. Do not convert ordinal judgements to arithmetic, add a hidden tie-breaker, or adopt a group average to force closure. If several value models remain admissible, show which relations hold throughout them and which depend on the model.

Use `A.19.CPM` when its profile, comparator, admissibility, and evidence conditions obtain. Its set-valued comparison outcome remains distinct from the application and evidence account, a result episteme, selection, or permission. Use the appropriate direct comparison Method otherwise; a table alone does not assert a CPM application.

Distinguish three important outcomes. Two alternatives can be tied under a rule, incomparable because of supported conflicting consequences, or not yet comparable because a necessary input is missing. Preserve the difference. If no candidate meets a protected condition, return that failure rather than ranking the least nonconforming candidate as acceptable.

#### PSDA.8:4.6 - Return the relation and what would change it

State the exact alternatives and question; common basis; consequence profiles and source limits; applied rule; supported relations; material value disagreement; excluded or unresolved comparisons; and the smallest change that could invalidate the result.

`PSDA.9` may use this comparison and its evidence for the same configuration and horizon to test robustness. It does not inherit a robustness claim merely from a clean table. An authorized chooser or recommendation practitioner may use the comparison to inform their own judgement. Establish the basis for a resulting programme or WorkPlan separately, and use evidence of actual performance to support any claim about subsequent Work or its effects.

Recognition begins when a rank lacks a recoverable consequence path. Assurance requires qualified direct models, evidence, source reliance, calculation or implementation checks, and the relevant domain protections. A replayable comparison can still be empirically wrong; independent support of its premises remains necessary.

### PSDA.8:5 - Archetypal Grounding

#### PSDA.8:5.1 - A flood-service comparison with no scenario-free winner

Continue the illustrative next-season case with N, F, M, and S: continue the present arrangement, change fixed capacity, obtain a mobile reserve arrangement, or use a staged combination.

Suppose a later qualified deployment analysis now provides the previously missing conditional operating results for M. A compatible resource estimate and service model provide the following hypothetical analytical slice. Costs are incremental budget units above the common continuing baseline; service loss is hours when the specified pumping service is unavailable. Lower is preferred on both measures for this slice. No scenario probability is supplied.

| Alternative | Incremental budget units | Service-loss hours with normal access | Service-loss hours with road loss |
| --- | --- | --- | --- |
| N — continuing baseline | 0 | 7 | 11 |
| F — fixed-capacity change | 8 | 2 | 3 |
| M — mobile-reserve arrangement | 5 | 1 | 9 |
| S — staged combination | Not yet qualified | Not yet qualified | Not yet qualified |

These figures are invented to demonstrate the comparison; they are not engineering, financial, safety, or investment advice. The current sources do not establish reachable assistance or all property-loss consequences. Those value and protected-condition questions remain outside this numerical slice and can block an overall recommendation.

Under normal access, M costs less and has fewer service-loss hours than F. Under road loss, F loses fewer service hours but costs more. Thus the slice establishes no condition-independent dominance between F and M. N uses fewer incremental resources but loses more service hours; zero incremental cost does not mean that the baseline has no continuing obligations or consequences.

S is not assigned zero or dropped as an inferior candidate. Its missing whole-arrangement result is returned as a gap. The inspector can reproduce the narrower relations while seeing why neither those relations nor the table supports a complete four-candidate recommendation.

#### PSDA.8:5.2 - Compare whole development arrangements, not component scores

In the ninety-day organization case, a course assessment and an AI benchmark cannot be placed directly into one service-reliability ranking. Suppose the adviser obtains a qualified allocation and operations comparison for two whole arrangements: I, internal development with covered service duties, and H, a mixed human–tool arrangement with oversight and fallback.

The hypothetical supplier result gives ninety-day unplanned service-loss bounds of 12–18 hours for I and 8–20 hours for H, on the same service definition and operating conditions. Both retain their separately qualified resource and security conditions. No joint relation between the uncertain losses is supplied.

Those marginal bounds do not establish that H is always better, nor do they establish equality. H permits both a lower and a higher loss than I within the supplied bounds. The comparison returns an unresolved robust service ordering and asks which coordination or operating condition accounts for that difference. A joint model could provide a stronger relation, but it must be supplied rather than inferred from overlapping intervals.

The human capability result, organization-allocation result, and exact-version AI evaluation remain separate premises of that whole-arrangement comparison. No human learning effect is transferred to a model, and no model score stands for the organization's outcome.

#### PSDA.8:5.3 - Cheap non-use

A current qualified comparison already covers two replacement arrangements, their transition costs, service consequences, and the recipient's value rule. Reuse it for the authorized choice. A second consequence table with the same content adds no new result.

#### PSDA.8:5.4 - Two feasible library services with opposed and unknown effects

A library must compare two ways of giving complex reference help during the next four weeks: A, booked consultations with preparation time; B, a walk-in desk with triage. Both have qualified staffing, access and budget arrangements. Neither is excluded for infeasibility. The following observations and judgements are invented to show the method, not findings about libraries.

The reader wants a usable answer; a shift worker also needs a way to seek help without knowing next week's schedule. The librarian wants uninterrupted preparation for difficult questions. The manager needs a service whose answer quality and accessibility can both be defended. These are distinct concerns, not interchangeable satisfaction scores.

The practitioner interviews the roles separately and constructs these relationships:

| Relationship in this case | Ground and limit |
| --- | --- |
| A usable specialist answer needs the reader's question, an accessible relevant collection, and competent librarian work together. | The service definition and a sample of completed requests support this necessary combination. Availability of the collection alone does not produce an answer. |
| The librarian depends on the reader providing enough detail before preparation can start. | The reader supplies the question; the librarian explains which missing details prevent preparation. The booking confirmation itself is not that provision. |
| Booking online or through the staffed telephone can obtain a slot. | Either route suffices for reserving an available slot; they are not mutually exclusive. Neither establishes that the reader can attend. |
| Advance detail and protected preparation help answer quality under A. Walk-in interruptions under B impair preparation for difficult questions. | Librarians can identify the interrupted work in the sample. This supports the direction, not a population-wide effect size. |
| B permits a visit without a prior appointment; A requires attendance at a booked time. | The actual service rules establish this difference. Shift workers explain why the appointment condition can obstruct their access. |
| Reminders under A might improve attendance. | No evidence yet says whether these readers receive a reminder in time or can act on it. The effect is investigated but unknown. |

Now evaluate A. The necessary resources and work arrangement are supported; answer quality has favorable grounds. Telephone booking provides another way to reserve a slot. Shift workers explain that this helps booking but does not establish their ability to attend at the fixed time. The reminder effect remains unknown, so overall accessibility is unresolved.

Evaluate B on the same four-week basis. Unscheduled access is supported, while preparation for complex questions has adverse grounds. Triage may help preparation, but the librarian says it cannot remove interruptions under this staffing arrangement. The comparison consequently contains a supported trade-off plus one unresolved effect:

| Consequence | A — booked consultations | B — walk-in triage |
| --- | --- | --- |
| Preparation for difficult questions | Favorable grounds from advance detail and protected time | Adverse grounds from interruptions, not removed by triage |
| Access without a predictable schedule | Obstructed by fixed attendance; overall access unresolved | Supported by the walk-in rule within desk hours |
| Actual attendance and completed help | Reminder effect unknown | Not inferred merely from an open desk |

There is no supported overall winner. The manager cannot substitute one aggregate satisfaction label for these differences. The return identifies a discriminating question: can the shift-worker group obtain help through A when its schedule changes, and under what continuation?

Work backward from the manager's proposed joint requirement: preserve preparation and provide a route usable after a schedule change. A's telephone booking cannot by itself meet the second condition. B meets that access condition but does not preserve uninterrupted preparation. A possible combination is a booked service with a staffed same-day rescheduling route and protected preparation time. That is a new candidate, not a conclusion that A already meets both conditions. Its staffing interaction and ability to retain preparation must be checked before comparison.

Suppose a bounded trial shows that changed shifts overlap the booked appointments, preventing those readers from attending; reminders arrive after the changes, and appointments cannot be moved during the four-week service. This new ground settles one relationship: reminders do not restore access for the observed shift-worker situations. Rerun A's access branch and the joint-requirement test. Retain A's independently supported preparation advantage and B's existing profile. If access after a schedule change was declared a protected condition, A now fails that condition for this scope; if it was a negotiable value, the result is a clearer trade-off, not automatic exclusion. The trial supports neither a claim about all readers nor the untested combined candidate.

The useful result is the explained comparison, the precise failed route and the next candidate's missing premise. It is more informative than either “both are feasible” or “A scored higher”, and it does not authorize a service change.

### PSDA.8:6 - Bias-Annotation

**Scope:** consequence comparisons for bounded decision-support use. **Lenses:** **Onto/Epist** separates alternative, forecast, observation, and result; **Arch** exposes interaction and distribution; **Prag** fixes the receiving question; **Gov** preserves conditions and authority; **Did** makes the comparison replayable.

Ranking bias prefers closure over partiality. Baseline bias compares change with an empty world. Aggregation bias hides losers and shared burdens. Model precision can conceal missing applicability. Counter these by exposing consequence paths, testing the common basis, and stating the exact relation actually supported.

### PSDA.8:7 - Conformance Checklist

- [ ] Alternatives, subject, configuration, affected subjects, horizon, and receiving use are fixed for the comparison.
- [ ] Candidate, value, and uncertainty inputs are current and compatible or their gaps are returned.
- [ ] Each material consequence has a supported path, subject, timing, and uncertainty account.
- [ ] Where a qualitative network is constructed, relationships have distinct meanings and grounds; opposing and unknown evidence reaches the judgement without arithmetic cancellation.
- [ ] A backward proposal is tested forward as a whole; an unsupported transition or failed combination is not generalized to every possible design.
- [ ] Transition, interaction, shared burdens, and displaced losses are included where they can change the result.
- [ ] Measures, value transformations, protected conditions, and evidence retain their different meanings.
- [ ] Missing entries are not zero, equal, or silently favorable.
- [ ] The comparison rule and admissible operations are explicit.
- [ ] Ties, supported incomparability, and inability to compare are distinguished.
- [ ] The result states supported relations, limits, dissent, and exact reopen conditions.
- [ ] Comparison does not establish robustness, recommendation, authorization, Work, or effect.

### PSDA.8:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Compare a component's score with a whole arrangement's outcome. | Obtain consequence claims for the same receiving subject and use. |
| Use favorable conditions for each alternative. | Hold the comparison basis fixed or show explicit conditional branches. |
| Sum separately advertised benefits. | Recover overlap, interaction, and the qualified whole-arrangement result. |
| Treat overlapping uncertainty intervals as equality. | State what relation the bounds actually support and what joint information is missing. |
| Rank a failed protected condition by compensatory score. | Keep eligibility separate and return the failure. |
| Call an archive front a consequence comparison. | Recover the actual comparator, consequence profiles, conditions, and evidence. |

### PSDA.8:9 - Consequences

A recipient can inspect why an alternative compares favorably and exactly where that conclusion stops. Partial comparisons remain useful, and missing domain results become precise requests. The cost is explicit consequence and dependence work; focus it on distinctions that could reverse the result rather than building a maximal model.

### PSDA.8:10 - Rationale

A consequence comparison connects proposed actions to values through qualified claims about affected subjects. Keeping that chain visible prevents a ranking from silently deciding the model, value system, or protected conditions. Separate comparison and choice allow a well-supported partial answer to remain a valid result.

### PSDA.8:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How should alternatives be connected to consequences? | Use explicit outcome models with the conditions and dependencies needed by the decision. | Rank isolated attributes or tool outputs without a consequence path. | **Adapt:** :4.1–:4.4 reconstruct only decision-changing consequence paths and shared burdens. The added effort is accepted when an omitted interaction could reverse the comparison; a qualified existing account is reused. | Borgonovo et al.'s [2026 decision-analysis review](https://doi.org/10.1016/j.ejor.2025.05.023) supplies the current graphical-model and uncertainty line. It does not validate a local mechanism or establish causal effects from arrows. `C.11.CRC` supplies a missing finite configuration-relative contribution, not field calculations. | Reopen when a changed configuration, mechanism, affected subject, or horizon invalidates a consequence path. |
| What comparison is justified by conflicting or incomplete values? | Use a declared preference model and preserve its partial or model-dependent relations. | Impose one total weighted rank. | **Adapt:** :4.5–:4.6 retain ties, incomparability, and missing-input distinctions. The deliberately accepted trade-off is less rhetorical decisiveness for a truthful relation. | Greco, Słowiński, and Wallenius's [2025 MCDA review](https://doi.org/10.1016/j.ejor.2024.07.038) is a comparison candidate for alternative preference and recommendation forms. Its finite-action methods do not supply local values, probabilities, or decision authority. | Reopen if elicitation or evidence changes the admitted model set or resolves a previously missing comparison. |
| How can early qualitative consequences be constructed and questioned before a complete domain model exists? | Make the intermediate relationships and their grounds explicit, carry each alternative through them, and use attributed domain judgement where evidence does not determine the result. | Draw influence arrows, count favorable signs, or declare a complete model necessary before any useful comparison. | **Adapt:** :4.2.1 and :5.4 supply construction, questioned propagation, conditional backward exploration and local revision; no new notation or solver is required. | Horkoff and Yu's [PoEM 2009 procedure](https://www.cs.toronto.edu/~jenhork/Papers/Horkoff_PoEM_2009l.pdf) and [ER 2010 backward analysis](https://www.cs.toronto.edu/~jenhork/Papers/ER_Horkoff.pdf) are historical method anchors, not current empirical validation or iStar 2.0 semantics. Qualitative support does not establish causal magnitude, participant commitment or realized success. | Reopen when a changed relation, stakeholder judgement or domain model changes a material consequence; use a stronger model when quantitative interaction or feedback decides the answer. |
| Does generic candidate stewardship already compare the consequences? | Keep profile comparison, finite contribution, and archive/front stewardship distinct. | Treat C.18 as a general consequence-ranking Method. | **Adopt:** :4.2 and :4.5 use the exact C.11.CRC and A.19.CPM contributions when needed; the PSDA consequence account retains its field question. No archive machinery is required for a small comparison. | Current `C.18` governs generation, archive, and front objects; `A.19.CPM` governs its admitted set-valued comparison; direct domain Methods supply consequence models. Their different result boundaries defeat the broader attribution. | Reopen when the current question actually becomes archive stewardship or a direct comparison contribution changes. |

### PSDA.8:12 - Relations

- `PSDA.5` supplies the alternative family, `PSDA.6` the value and trade-off account, and `PSDA.7` bounded evidence and uncertainty claims. Each is used only under compatible subject, configuration, horizon, and receiving conditions.
- `PSDA.9` may consume the comparison's evidence to test robustness for that same use. The comparison does not entail the robustness result.
- `C.11.CRC` supplies a missing finite configuration-relative contribution claim. `A.19.CPM` supplies an admitted profile comparison only when its own conditions obtain. `C.18` retains its different archive/front and generation function.
- Direct engineering, operations, human-development, AI/model, financial, scientific, and other practices govern their own consequence and evidence results. `A.10` qualifies reliance; `A.15.9` supports a needed bounded outside contribution.
- `C.11` or the direct decision owner supplies the later choice. An unavailable, stale, or incompatible premise is replaced by a qualified direct result or remains a named gap, never filled by neighboring-pattern presence.

### PSDA.8:End

## PSDA.9 - Test Robustness and Sensitivity of Decision Alternatives and Their Comparison

> **Type:** Method pattern body
> **Status:** Stable
>
> **Primary working result:** **robust regions, reversals, and information priorities** for one decision-support comparison: the conditions under which a claim holds, changes, or cannot be established, and the questions that could usefully change it.

### PSDA.9:1 - Problem frame

**Use this when** a favored alternative depends on a forecast, weight, model, or threshold that might change, or when a precise ranking hides plausible reversals. Also use it when the recipient asks whether further information would improve the decision rather than merely improve the estimate.

Start with one claim: what exactly should remain true, under which changes? Vary the decision-bearing conditions within a justified range and inspect where the claim survives or fails. The gain is a bounded statement of stability and a useful next question, not the adjective “robust” applied to an entire project.

The governed object is that robustness account. **Sensitivity** describes how a result changes with inputs, assumptions, or models. **Robustness** says whether a declared performance, admissibility, or comparison condition continues to hold across specified variation. A sensitive magnitude can leave the preferred set unchanged; an insensitive average can hide a decisive threshold crossing. Section 4.3.1 supplies a small paired-response test when the response at a central input can conceal such a difference.

**Do not use this pattern** when a current robustness result already covers the exact comparison and changes now in question. Use direct model validation for whether a model is adequate in the first place, and the authorized choice owner for the actual decision or probe. Stability inside a model does not validate the model or authorize action.

### PSDA.9:2 - Problem

A one-point ranking can hide a narrow region of support. Small changes in a value trade-off can reverse it; a common-cause failure can defeat every alternative; a different model can change which conditions are even represented.

Sensitivity work can also miss the decision. A tornado chart may rank output variance rather than choice relevance. One-factor-at-a-time tests can miss interactions. Running thousands of similar scenarios can create an appearance of broad coverage, and their frequency can be mistaken for probability. More calculations do not by themselves support a stronger robustness claim.

### PSDA.9:3 - Forces

| Force | Tension |
| --- | --- |
| Coverage and effort | Joint or structural changes can matter, while unrestricted scenario expansion consumes the available time. |
| Stability and truth | Repeated agreement supports only the tested model and region, not the omitted world. |
| Values and evidence | Better information can resolve a fact, while a disputed trade-off needs a value judgement or legitimate collective decision. |
| Flexibility and commitment | Staging can preserve options, while monitoring, lead time, reversibility, and later authority may be unavailable. |
| Information and action | A probe can change a decision, but it also costs time, resources, exposure, and foregone opportunity. |

### PSDA.9:4 - Solution

Declare the claim and variation space, challenge it with the least costly tests that cover the live failure mechanisms, and return supported regions, reversals, and bounded information questions. Keep the actual later decision separate.

#### PSDA.9:4.1 - State what is being tested

Recover the exact alternatives, consequence comparison, value basis, subject, configuration, horizon, and receiving use. Use `PSDA.8`'s comparison and evidence only where they match those conditions. A qualified direct comparison can supply the same input.

Specify the test. It might ask whether one alternative remains no worse under a declared rule, whether every retained alternative meets a service threshold, whether a protected condition is ever violated, or whether the recommendation must remain conditional. Different tests can produce different answers.

Name the robustness criterion before interpreting results. Satisfactory performance across tested conditions, worst-case loss, regret relative to the best available alternative in each condition, and stability across compatible value models answer different questions. Do not change the criterion after seeing which candidate it favors. If the criterion or admissible trade-off is unresolved, return that question rather than presenting a universal winner.

#### PSDA.9:4.2 - Bound the changes by evidence and the decision

Identify the uncertainties or judgement changes that could affect this test: input values, future conditions, model structures, consequence definitions, preference models, evidence qualification, candidate membership, or horizon. State why the selected variations are relevant and what they omit.

Ranges and scenarios need a basis. Distinguish observed bounds, elicited judgements, scientifically or operationally plausible cases, and deliberately extreme stress tests. A stress-test failure can reveal vulnerability without establishing the failure's probability.

Preserve dependencies and feasibility. Joint variations should describe possible or explicitly hypothetical conditions, not arbitrary combinations of incompatible endpoints. Changing a binding legal, safety, consent, or security condition is not an ordinary parameter perturbation. Its meaning, applicability and current force require their own competent result. If the question is whether its protection warrants its measure, threshold or burden, use the bounded `C.11.DUA` §4.3 appraisal through `PSDA.6` §4.4. Return the substantive recommendation and actual amendment authority/window separately; until a revision applies, test present alternatives under the binding condition.

If a needed variation cannot be bounded, retain that coverage gap. “Across all plausible futures” is stronger than “across the three stated futures” and needs stronger support.

#### PSDA.9:4.3 - Test locally, then expand where the failure can hide

Begin with a cheap discriminating test: a boundary value, an alternative value judgement, an omitted condition, or a direct challenge to one decisive assumption. Recompute the same comparison for all affected alternatives under that changed basis.

Use joint or global variation when interactions, nonlinearities, common causes, thresholds, or structural alternatives can change the result. A one-at-a-time test is insufficient for a claim about those combinations. Use the direct modeling and analysis Method to choose suitable tests, sampling, or proofs; this pattern mandates no universal algorithm or scenario count.

Keep empirical variability, model uncertainty, and value disagreement distinguishable. If a model change alters the meaning or comparability of an output, repair the comparison before treating the difference as another numerical sample.

A computational result is limited by the tested region and procedure. An analytical inequality may establish a whole region under its assumptions; a finite sample usually establishes only sampled behavior unless a further guarantee is justified. State that difference.

##### PSDA.9:4.3.1 - Compare a central response with two equally displaced inputs

Use this small test when the response to a varying input may make a central estimate misleading. It needs a response account suitable for the stated comparison, not an assumed probability distribution.

1. Name the input and the response it affects. Fix the arrangement, affected subject, time window, other relevant conditions, response unit and preferred direction. Choose a central input `x` and displacement `h > 0` so that `x-h`, `x` and `x+h` lie within the account's admissible domain. Equal input differences and averaging the responses must be meaningful on their respective scales; numerical labels alone do not suffice.
2. Obtain the three comparable response values from the qualified model or suitable observations. For response `r`, calculate the endpoint mean and its difference from the central response: `D = (r(x-h) + r(x+h))/2 - r(x)`. The equal weights define this constructed test. Calling the mean a real-world expectation requires a separately qualified probability model.
3. Interpret `D` on the declared response coordinate. A positive difference means the endpoint mean exceeds the central response: worse for a loss, better for a benefit whose higher value is preferred. For a target-valued response, use its declared preference rule. Zero means no midpoint gap at these three points; it does not prove linearity or robustness over an interval. Examine each tested response against any independently justified threshold as well.
4. Widen the displacement or test another consequential condition only when it could change the receiving decision and the model's domain permits it. Report the tested values and gaps; do not turn one finite comparison into a regional convexity, derivative or global robustness claim.

If the response account or scale is inadequate, return that specific limit. A clearly conditional calculation or qualitative comparison may remain useful; requesting more observations is a separate worth question, not an automatic next step.

When a harmful response suggests changing exposure, formulate the actual alternative arrangement and compare its whole contribution through `C.11.CRC`. Include the means, carrying burden and displaced work required to maintain a proposed protection. A stated spending limit alone does not enforce a consequence limit. `C.16` governs quantity and scale use; `C.29` governs a needed mathematical-representation correspondence and its transfer limits. The robustness account remains the result here.

#### PSDA.9:4.4 - Map holding regions and reversals


Report which condition holds in each relevant region, where alternatives exchange order, where a threshold is crossed, and where the comparison becomes unsupported. Include boundaries and ties when they can change the return.

Separate a genuine reversal from a different question. A new value rule, candidate, subject, or horizon may define another comparison rather than a parameter change inside the old one. Preserve the original basis so that the reader can see which happened.

Test omissions as well as numbers. A stable two-candidate result can be irrelevant if a material third candidate remains unexamined. A common failure can show that all current alternatives are inadequate. Return that candidate or formulation gap instead of calling the least bad option acceptable.

The result may be a robust retained set, a conditional preference, several non-dominated alternatives, a failure region, an unresolved boundary, or a blocker. No single preferred alternative is required.

#### PSDA.9:4.5 - Connect the remaining uncertainty to information value

Ask what feasible observation, experiment, calculation, or interpretation could move the comparison across a material boundary. Distinguish “this factor changes the output a lot” from “this attainable result could change the decision”.

Where a qualified probabilistic and value model permits information-value analysis, include the possible decisions after the information, the informativeness of the actual probe, and its cost and delay. Perfect-information value can be an upper bound; it is not the value of an imperfect test. Information values from several sources are not automatically additive.

Where probabilities are not defensible, state the discriminating conditions and what a probe could resolve without inventing expected value. Some uncertainty will remain; a broad research programme is not the default response.

Use `C.11` or the direct decision owner for the actual choice of a next probe over the current options, budget, value, and cost. This pattern supplies information priorities and conditions, not probe authorization or a research WorkPlan. A preference or authority dispute may require an explicit judgement rather than more empirical data.

#### PSDA.9:4.6 - Examine adaptive alternatives without assuming free flexibility

When a staged candidate is live, test what it actually preserves. The later observation must arrive early enough, be interpretable, and leave a feasible response within the remaining resources and authority. Include monitoring cost, lead time, temporary exposure, transition burdens, and irreversible loss of options where material.

A policy-failure condition is not automatically an action trigger. The future decision arrangement must determine what observation warrants reconsideration and who can act. If those premises are missing, return the candidate's specific adaptive-capability gap.

Do not favor a pilot solely because uncertainty is high. A probe can be unsafe, too slow, uninformative, or unable to change the relevant commitment. Conversely, a bounded information result can be more useful than a premature direction recommendation when its supported value justifies the delay.

#### PSDA.9:4.7 - Return a bounded robustness account

Return the tested claim and comparison basis; the variation region and omissions; the method and evidence limits; supported holding regions and reversal conditions; unresolved comparisons or candidate gaps; information priorities and feasibility limits; and the observation that reopens the result.

`PSDA.14` may use this evidence for the same configuration and horizon to compose a recommendation. Evidence does not entail that recommendation or the later receiving decision. An unavailable, stale, or incompatible robustness result can be replaced only by a qualified direct result or an explicit gap.

Recognition starts with a plausible reversal. Consequential assurance also requires qualified model and source use, correct analysis, adequate challenge coverage, and the direct domain's protection and independence requirements. Robustness to uncertain parameters does not cure an invalid model or missing safety result.

### PSDA.9:5 - Archetypal Grounding

#### PSDA.9:5.1 - An explicit reversal boundary for the pump comparison

Use the illustrative F and M slice from `PSDA.8`: F costs 8 incremental budget units and loses 2 service hours with normal access or 3 with road loss; M costs 5 and loses 1 or 9 hours. N remains the baseline and S still has an unqualified whole-arrangement result. The following calculation tests only F against M; it does not close the wider candidate comparison.

For an illustrative analytical question, suppose a declared value model minimizes expected service-loss hours plus `lambda` times incremental budget units. Here `lambda` is an explicitly elicited value conversion, in service-hour-equivalent value per budget unit; it is not a measurement conversion or an unspoken public preference. Let `p` be the road-loss probability if a qualified probability model supports one.

Under those assumptions:

- F's value loss is `2 + p + 8*lambda`.
- M's value loss is `1 + 8*p + 5*lambda`.
- F has lower value loss precisely when `7*p > 1 + 3*lambda`; equality is a tie.

For `lambda = 0.5`, the reversal is at `p = 5/14`, approximately 0.357. At `p = 0.2`, F and M give 6.2 and 5.1 respectively, so M is better under this model. At `p = 0.6`, they give 6.6 and 8.3, so F is better. These are invented sensitivity settings, not a forecast.

The source comparison supplied no probability. Therefore the valid return is the conditional boundary, not a claim that either setting is likely. If a probability model cannot be qualified, retain the scenario comparison instead of assigning equal chances.

A different declared test asks whether modeled service loss is at most 4 hours in both stated access conditions. F satisfies that illustrative test; M fails it under road loss. This is a different robustness criterion, not a hidden replacement for the value model. The four-hour cut is an example, not a domain standard. F's result covers only those two modeled conditions.

The account returns the reversal boundary, the limited threshold result, the unresolved probability and value premises, and S's candidate gap. Reachable assistance, wider property consequences, and protected conditions still require their direct results. None of the calculations authorizes a pump investment.

##### PSDA.9:5.1.1 - A separate constructed delay-response question

Keep the preceding probability and value-reversal question separate. For this new illustration, fix a thirty-day service window and one access interruption. A stipulated model supplies the service-loss hours for F and M at three access delays; lower service loss is preferred. Each arrangement and all other modeled conditions stay fixed while delay varies.

| Access delay in days | F: service-loss hours | M: service-loss hours |
| --- | ---: | ---: |
| 0 | 2 | 1 |
| 1 | 2.5 | 3 |
| 2 | 3 | 9 |

With `x = 1` day and `h = 1` day, M's central response is 3 hours, its endpoint mean is `(1 + 9)/2 = 5` hours, and `D = 2` hours. F's central response and endpoint mean are both 2.5 hours, so its `D = 0`. F has no midpoint gap at these three points; this does not establish a linear response between them.

Under the separately declared four-hour service-loss criterion, M's two-day response of 9 hours fails. F satisfies that criterion at the three stated points only. Neither endpoint mean is an expected real loss without a probability basis, and a central response below four hours does not settle the endpoint test.

The useful return is the finite response difference, M's failure condition and the remaining model and coverage limits. F's additional investment and the feasibility of any alternative access protection still need their whole-configuration comparison. If the stipulated model lacks support for real use, retain the calculation as conditional or illustrative; do not report an established pump-performance result. No additional observations or investment are authorized by it.

#### PSDA.9:5.2 - What would change a development recommendation?


In the illustrative ninety-day organization case, I is internal development with covered service duties and H is a mixed human–tool arrangement. The earlier supplier bounds, 12–18 and 8–20 service-loss hours, do not establish a robust ordering.

Suppose a qualified joint operating model now supplies two admissible conditions within those bounds:

| Condition | I: service-loss hours | H: service-loss hours | Supported comparison on this coordinate |
| --- | --- | --- | --- |
| Required handoff coverage is present. | 14 | 10 | H has less service loss. |
| The specified handoff coverage is absent. | 16 | 20 | I has less service loss. |

The robustness result locates a reversal in the whole arrangement's coverage condition. It does not attribute the difference solely to human learning or model quality. The useful next question is the feasibility and persistence of that exact coverage under the proposed allocation, not a generic demand for a higher AI benchmark or another course test.

If that result can be obtained within the decision window, the adviser can return it as an information priority with its cost and limits. If not, the recommendation remains conditional or retains both directions. A service model for another team or model version does not close this holder-specific boundary.

#### PSDA.9:5.3 - Cheap non-use and honest stop

A current analysis already proves the same service comparison throughout the relevant parameter interval, and the only proposed new computation repeats interior points without challenging another assumption. Reuse the result. If the untested issue is instead a missing causal or safety premise, stop the robustness calculation and obtain that direct result; more parameter samples will not supply it.

### PSDA.9:6 - Bias-Annotation

**Scope:** robustness and information questions for bounded decision support. **Lenses:** **Epist** distinguishes model stability from truth; **Prag** tests decision relevance; **Arch** exposes interactions and omitted alternatives; **Gov** preserves protected conditions and future authority; **Did** makes reversals and limits readable.

Winner-protection bias selects narrow ranges or convenient criteria. Scenario-count bias mistakes volume for coverage. Variance bias selects a probe that cannot change the decision. Flexibility bias assumes cost-free adaptation. Counter these by declaring the claim, criterion, region, and real response capability before interpreting the result.

### PSDA.9:7 - Conformance Checklist

- [ ] The exact comparison, subject, configuration, horizon, and robustness claim are stated.
- [ ] The robustness criterion is explicit and not chosen after seeing the preferred winner.
- [ ] Variation ranges, scenarios, dependencies, and exclusions have a recoverable basis.
- [ ] Binding conditions are not silently relaxed as parameters. A disputed requirement's merits return remains separate from its present force and from the robustness result.
- [ ] Tests address relevant interactions, structural differences, and omitted alternatives.
- [ ] Sampled behavior, analytical region claims, and unsupported extrapolation are distinguished.
- [ ] A paired-response test states its admissible inputs, comparable response scale, construction weights, preferred direction and exact finite result; no midpoint gap or constructed mean is overread as global robustness or an actual expectation.
- [ ] Holding regions, ties, reversals, failures, and gaps are reported at their actual scope.
- [ ] Information priorities concern attainable decision-changing results and include cost or feasibility limits.
- [ ] Adaptive claims account for observation, lead time, response feasibility, and later authority.
- [ ] The return supplies evidence for recommendation, not truth, authorization, Work, or effectiveness.

### PSDA.9:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “The winner is robust” after a few small perturbations. | State the claim, variation region, method, and untested failure mechanisms. |
| Count successful scenarios as a success probability. | Supply a qualified probability measure or report conditional coverage only. |
| Change one input at a time despite common-cause failure. | Test the relevant joint conditions under a justified dependence model. |
| Treat the largest output variance as the best information target. | Ask whether attainable information can change a decision or eligibility. |
| Recommend a pilot whenever evidence is thin. | Establish information value, safety, timing, reversibility, and response feasibility. |
| Change the robustness criterion to preserve the preferred option. | Show the different questions and return the criterion disagreement. |

### PSDA.9:9 - Consequences

The recipient learns not only what currently compares favorably but where the conclusion can fail. A retained set or conditional recommendation can be more useful than a fragile winner. The cost is targeted recomparison and explicit coverage limits; stop when further work cannot change the declared return or when a different missing premise governs the next action.

### PSDA.9:10 - Rationale

A decision-support result is strengthened by exposing its reversal conditions, not by defending one point estimate. Separating uncertainty, values, model structure, and response capability prevents robustness from becoming a general assurance label. Decision-linked information priorities keep remaining uncertainty useful without making inquiry endless.

### PSDA.9:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How can a comparison remain useful when future conditions or models are unsettled? | Stress-test declared performance and comparison claims across justified conditions; examine feasible adaptation where it matters. | Optimize one forecast or call an unspecified staged policy robust. | **Adapt:** :4.1–:4.4 and :4.6 return bounded holding and failure regions. Extra scenario and response analysis is accepted when a single forecast or assumed flexibility can conceal failure. | Lempert et al.'s [2024 DMDU analysis](https://doi.org/10.3389/fclim.2024.1380054) supplies the current robust-decision line; the [2019 DAPP chapter](https://doi.org/10.1007/978-3-030-05252-2_4) supplies pathway, timing, and failure-condition distinctions. Their applied domains do not supply universal thresholds, scenario probabilities, or local authority. | Reopen when an omitted condition, implementation lead time, or response constraint defeats the stated region. |
| Which sensitivity result should guide further inquiry? | Link local and joint sensitivity to the decision boundary and the value of attainable information. | Use output variance or a one-factor chart as a universal research priority. | **Adapt:** :4.3–:4.5 distinguish magnitude sensitivity, reversal, and probe value. More computation is justified only when the added question can change the bounded return; actual probe choice remains separate. | Borgonovo et al.'s [2026 review](https://doi.org/10.1016/j.ejor.2025.05.023) is the synthesis candidate for sensitivity and information acquisition. Its formal approaches need their own model assumptions; `C.11` retains the local choice and probe-worthiness result. | Reopen when the feasible probe, decision window, dependency model, or costs change. |
| What can a central-input response conceal? | Compare the central response with a symmetric endpoint mean and test consequential thresholds separately. | Rely on the central response alone or infer a whole-region property from three points. | **Adapt:** :4.3.1 and :5.1.1 make a finite nonlinear-response check usable without inventing probabilities. | Taleb and West's [2023 finite-difference and convexity account, §III-C and Appendix B](https://arxiv.org/html/2209.14631v2), supplies the distinction between a finite comparison and stronger smoothness, regional or probability claims. Its clinical models do not validate a decision-support response model. | Reopen when the response model, scale, supported domain, subject or decision threshold changes. |
| What if the value model, rather than the forecast, is incomplete? | Test relations across the models compatible with the expressed preferences. | Treat one fitted weight vector as uniquely known. | **Adapt:** :4.1–:4.4 retain value-dependent reversals instead of calling preference uncertainty factual noise. The deliberate trade-off is a possibly larger retained set. | Greco, Słowiński, and Wallenius's [2025 MCDA review](https://doi.org/10.1016/j.ejor.2024.07.038) supplies robust ordinal regression as a best-known-line candidate for this question, not a requirement to use one algorithm or to collapse participants' values. | Reopen when elicitation or a legitimately governed value decision changes the compatible model set. |

### PSDA.9:12 - Relations

- `PSDA.8` may supply the consequence comparison and its evidence for the same configuration and horizon. Evidence enables this test but does not establish its result.
- `PSDA.14` may consume robust regions, reversals, and information priorities as evidence for its recommendation. This neither entails the recommendation nor transfers the later choice authority.
- `A.10` governs bounded evidence reliance; direct domain and modeling practices govern the validity of claims, models, ranges, and tests. Changed actual source uses receive their direct revalidation rather than a blanket robustness assertion.
- `C.16` governs quantities, scales and response comparability; `C.29` governs a needed mathematical representation and its correspondence limits. Neither supplies domain validation merely through the calculation.
- `C.11.CRC` compares a proposed finite change to the arrangement, including the feasibility and burden of maintaining a protection. A sensitivity result does not itself change that arrangement.
- `C.11` governs an actual local choice and the worth of another probe. Information priority, probe selection, WorkPlan, performed inquiry, and observed effect remain distinct results.
- Candidate formation, value elicitation, model repair, and follow-up remain their own questions when the test exposes a gap there. Missing or incompatible inputs require a qualified direct result or an exact stop, not an invented prerequisite lifecycle.

### PSDA.9:End

## PSDA.11 - Bound the Decision-Support Engagement and Authority Boundary

> **Type:** DPF pattern body
> **Status:** Stable
>
> **Primary working result:** a **bounded engagement question** that names the decision-support return, its recipient, the holder or subject, the horizon, the receiving decision or Work, the choice owner and authority boundary, the current scope, the smallest missing value, and an observable condition for reopening.

### PSDA.11:0 - Use This When

Use this pattern when someone asks a decision-support performer to “help decide”, “structure the problem”, “recommend what to do”, or “say what should develop next”, but the engagement is not yet bounded well enough to produce a responsible result. The missing value may be the recipient, holder or subject, horizon, receiving decision, receiving Work, choice owner, authority, consequence, or kind of return expected.

Begin with the later decision or use that the decision-support result is meant to inform. Separate the performer who prepares decision support from the person or arrangement that receives it and from the Agent that owns the later choice. Then return one bounded engagement question or the exact value that is still missing.

The practical gain is an affordable start that works both before overt contest and inside a disputed situation. It prevents a workshop, model, score, or recommendation from silently becoming the decision, and it gives later problem-structuring or analytical Work a recoverable subject and stop.

Do not use PSDA.11 merely because a chooser must select among an already-qualified live option set; use `C.11` or the applicable domain choice rule directly. Use one holder-specific practice directly when it owns the whole question and no decision-support composition remains. A scientific, legal, ethical, safety, governance, or other specialist question stays with that practice unless its result must be returned into a separately governed decision-support engagement.

#### PSDA.11:0.1 - Working Distinctions

| Working term | Meaning in this pattern |
| --- | --- |
| decision-support engagement | The bounded situation in which a performer is expected to make a useful result available to a receiving decision or Work. The phrase alone establishes no Method, assignment, authority, WorkPlan, dated Work, service, or product. |
| decision-support performer | The actual or intended person, team, organization, tool-supported arrangement, or other capable System expected to prepare the return. A title, department, model, report, or tool output does not establish this performer or its authority. |
| recipient | The person or arrangement to whom the decision-support return is addressed for a named use. The recipient may or may not own the later choice. |
| holder or subject | The person, organization, System, arrangement, place, policy, capability, or other exact subject whose alternatives or consequences are under consideration. It is not inferred from the recipient's identity. |
| choice owner | The Agent authorized to make, reject, defer, probe, or reroute the later decision. It may coincide with the recipient or performer only when that coincidence and authority are independently supported. |
| receiving decision or Work | The later choice or Work whose next action can change because of the decision-support return. A recommendation is one premise for that use, not the choice or Work itself. |
| bounded engagement question | The smallest decision-support question that makes the intended return, use, participants, scope, authority boundary, and reopen condition usable now. It is a practitioner result, not a universal account schema. |

### PSDA.11:1 - Problem frame

Decision-support practice often begins before there is a stable “problem”. One engagement opens with several participant groups arguing about causes and values. Another opens with a calm request for advice whose recipient, subject, horizon, or later authority is still vague. Both can be prematurely forced into a workshop brief, model boundary, criteria table, or option set.

The primary concern here is the boundary of one decision-support engagement for one receiving use. The first useful result is not a complete problem formulation, alternative set, comparison, recommendation, plan, or decision. It is a question and authority boundary precise enough to say what result can be prepared now, what remains outside, and where a missing value must return.

Recognition is deliberately cheap: one unclear decision-bearing value is enough to open the pattern. Consequential use adds direct evidence for identity, assignment, permission, authority, source reliance, safety, law, ethics, and other claims that the engagement actually consumes. The short opening does not lower those assurance burdens.

### PSDA.11:2 - Problem

An unbounded engagement can expand into every concern, participant, model, consequence, and possible future. The performer gathers material without knowing which later action it can change. A premature boundary creates the opposite failure: the sponsor's wording becomes the only formulation, the visible recipient is treated as the choice owner, or an analytical result is presented as authorization.

These failures compound. A favourite problem-structuring Method can be selected before the decision-support use is known. A list of stakeholders can stand in for affected Systems and material concerns. A model can hide excluded consequences. A recommendation can absorb holder-specific conclusions or take a choice that belongs elsewhere.

The missing discipline is to bind the engagement to one intended return and separately governed later use while keeping the boundary explicitly provisional. Contestation, plural formulations, affected participants, models, alternatives, values, uncertainty, and follow-up open only when they can change that return.

### PSDA.11:3 - Forces

| Force | Tension |
| --- | --- |
| Affordable opening | A practitioner needs a first result quickly, while the most visible request may omit the value that makes any result usable. |
| Useful scope | A boundary is needed to act, while early closure can suppress affected participants, rival formulations, or decisive consequences. |
| Advice and choice | A performer must say something useful, while the later decision and its authority remain separate. |
| Stable use and revisable framing | The engagement needs a current question, while new evidence or participation can legitimately reopen it. |
| Plain roles and exact claims | Recipient, adviser, sponsor, analyst, and decider are useful words, while titles and labels establish no assignment, capability, or authority. |
| Domain ownership | Decision support must combine relevant premises, while holder, legal, ethical, safety, scientific, and governance practices retain their Methods and conclusions. |
| Recognition and assurance | One vague value can justify a cheap clarification, while high-consequence use requires stronger direct evidence and stops. |

### PSDA.11:4 - Solution

Bind the engagement to the smallest receiving decision or Work that can use a decision-support return. Name the distinct participant positions, subject, horizon, expected return, current scope, and authority boundary. Return the bounded engagement question when those values are adequate; otherwise return the exact missing value instead of inventing it.

#### PSDA.11:4.1 - Name the receiving use before the problem statement

Start with one ordinary sentence:

> Make **[kind of decision-support return]** available to **[recipient]** about **[holder or subject]** for **[receiving decision or Work]** within **[horizon]**; **[choice owner]** retains the later choice.

Ask what action can change because of the return and what consequence makes delay, error, or omission material. If no receiving decision or Work can be named, distinguish exploratory inquiry, research, learning, communication, or another direct use rather than manufacturing a decision-support engagement.

The requested return can initially be a bounded question, participant-and-concern account, plural formulation set, model or Method-selection result, alternative gap, comparison, recommendation, blocker, or abstention. Do not require a recommendation when an earlier honest result is more useful.

#### PSDA.11:4.2 - Separate performer, recipient, holder, and choice owner

Name each position separately even when one System may occupy two positions:

1. who is expected to prepare the decision-support return;
2. who will receive it and for what use;
3. which exact holder or subject is under consideration; and
4. who owns the later choice, deferral, probe, or reroute.

State any coincidence explicitly. A manager can receive advice without owning the board's later decision. A team can perform analysis for its own authorized choice, but the analysis Work, recommendation result, and later `ChoiceResult` remain distinct. A tool, document, score, model, department, job title, or meeting creates none of these positions by visibility alone.

Recover assignment, capability, permission, responsibility, conflict, commitment, or authority only to the extent that the current use relies on it. Use their direct patterns for consequential claims. If the required choice owner or authority basis cannot be recovered, return that exact gap.

#### PSDA.11:4.3 - Bound the subject, horizon, receiving Work, and consequence

State the holder or subject at the grain whose alternatives or consequences can change. Add the relevant configuration, place, population, operating condition, and interval only when they change the answer. State the receiving decision or Work and the horizon over which the return is expected to remain useful.

Name at least one consequence of getting the boundary wrong. This is a recognition cue, not a complete consequence analysis. When affected Systems, missing participants, duties, interests, or representation can change the engagement, continue with `PSDA.12`. When several problem formulations imply materially different actions, continue with `PSDA.1`. When included and excluded concerns need a deliberate scope decision, continue with `PSDA.2`.

#### PSDA.11:4.4 - Choose a provisional boundary and the next truthful branch

Record what is inside the engagement now, what remains outside, and what observation would move that boundary. Do not treat package order or the numbering of patterns as a practitioner sequence. Choose the next branch from the missing result:

| Current situation | Next truthful branch |
| --- | --- |
| participants, concerns, consequences, or representation are incomplete | recover the participation and concern account through `PSDA.12` |
| materially different formulations or intervention logics remain hidden | generate plural problem formulations through `PSDA.1` |
| the engagement has no usable included/excluded scope and reopen basis | set and reopen the problem boundary through `PSDA.2` |
| the engagement is bounded but needs a model, a choice or combination of problem-structuring Methods, or facilitation | use `PSDA.3` for the model, `PSDA.4` for Method selection or combination, or `PSDA.13` for facilitated inquiry |
| the engagement is bounded and the live gap is alternatives, uncertainty, comparison, or recommendation | begin with the first missing result in `PSDA.5`, `PSDA.6`, `PSDA.7`, `PSDA.8`, `PSDA.9`, `PSDA.14` |
| another practice owns a premise that can reverse the return | inspect or request the smallest bounded result through `A.15.9` |
| an authorized chooser already has an adequate option set and comparison basis | use `C.11` or the direct domain choice rule; stop treating engagement framing as the live question |

Several branches may be live together. Their results can proceed concurrently when their subjects and returns are clear. Co-occurrence does not turn the table into a workflow or make the engagement one Method.

#### PSDA.11:4.5 - Record the bounded engagement question or exact stop

Use the smallest account that another participant or later use must recover:

| Result position | Required content |
| --- | --- |
| intended return | The smallest decision-support result sought now, including blocker or abstention as valid branches. |
| recipient and use | Who receives the result, which decision or Work can change, and the horizon. |
| holder or subject | The exact subject, configuration, place, population, or interval needed by the current question. |
| participant positions | Decision-support performer and choice owner, plus only the assignments or authority facts the current use needs. |
| current boundary | Included concerns and consequences, important exclusions, and why that cut is usable now. |
| missing value or next branch | The exact participant, formulation, scope, source, alternative, evidence, authority, or other result still needed. |
| reopen condition | The smallest observable change that can alter the question, scope, authority boundary, or next branch. |

A compact result may be one sentence and one stop:

> For **[recipient]** and **[receiving decision]**, prepare **[return]** about **[subject]** within **[horizon]**; **[choice owner]** retains the later choice. The engagement is blocked until **[exact missing value]** is recovered.

Do not add a role register, stage model, workshop plan, evidence pack, or account field merely because a larger case might need it.

#### PSDA.11:4.6 - Reopen locally and preserve the later choice

Name the event that can invalidate the current boundary: a changed recipient, holder, horizon, receiving Work, authority relation, participant or concern, formulation, source, alternative family, evidence condition, consequence, or later decision. Reopen only the affected position and its dependent results.

A returned recommendation may inform the later decision, and follow-up may observe that later decision, but neither retroactively turns the decision-support performer into the choice owner. If the later choice changes the problem structure, use `PSDA.15` to determine which follow-up or reframing question is current.

#### PSDA.11:4.7 - What changes in practice

The practitioner stops accepting “the problem” as a sufficient start. Within the first exchange, they can name the return, recipient, subject, horizon, later use, and choice owner—or return the exact missing value. Method selection, modeling, participation, alternative generation, and recommendation Work begin from that result instead of being used to discover silently what the engagement was supposed to accomplish.

### PSDA.11:5 - Archetypal Grounding

#### PSDA.11:5.1 - Contested flood-pump decision

A municipal resilience office asks a decision-support team to “solve the pump problem” before the next flood season. Operations staff prefer another permanent pump; finance questions capital exposure; residents contest which districts and harms count; and the emergency investment board owns the later funding and deployment decision.

The team does not begin with a pump model or consensus workshop. It first returns this bounded engagement question:

> For the municipal resilience office, prepare a recommendation for the emergency investment board's pre-season funding and deployment decision about the district flood-pumping arrangement over the next flood season. Compare permanent, mobile, staged, and no-new-purchase branches only after affected districts, operating conditions, safety limits, and material dissent are recoverable; the board retains the later choice.

The boundary is useful but incomplete. `PSDA.12` is next because affected residents, operating groups, concerns, and consequence-bearing Systems can change the engagement. `PSDA.1` is also live because “insufficient capacity”, “unequal protection”, “maintenance fragility”, and “unsafe deployment” imply different interventions. The team stops before model or option selection if the board's authority, the decision horizon, or an affected district remains unrecoverable.

#### PSDA.11:5.2 - Development-direction advice without taking the choice

An engineering executive asks an advisory team, “What should we develop next for AI-assisted incident response?” The phrase does not yet say whether the holder is a person, team, organization capability, model, agent arrangement, or operating platform; whether the recipient or an investment committee owns the choice; or whether the horizon is the next release or the next two quarters.

After one clarification, the holder is the organization's AI-assisted incident-response arrangement, the executive is the recipient, the investment committee owns the later portfolio choice, the horizon is two quarters, and the requested return is a source-qualified development-direction recommendation. The first result is:

> For the executive's two-quarter investment proposal, prepare a bounded recommendation about development directions for the AI-assisted incident-response arrangement; the investment committee retains the later choice. Return the exact missing human-capability, organization, operations, model-evaluation, safety, or authority result before using it as a premise.

No contest is assumed. With the engagement bounded, the practitioner may inspect external results through `A.15.9` and begin with the first missing result among `PSDA.5`, `PSDA.6`, `PSDA.7`, `PSDA.8`, `PSDA.9`, `PSDA.14`. PSDA.11 authorizes no training programme, organization change, model modification, purchase, WorkPlan, or choice.

#### PSDA.11:5.3 - Cheap non-use when the choice is already local

A procurement board is the authorized chooser, has three qualified pump options, a current comparison basis, and no unresolved participant, formulation, scope, authority, or outside-practice premise. The live question is which option to select. Use `C.11` or the board's direct choice rule. Repeating PSDA.11 would add no useful boundary.

### PSDA.11:6 - Bias-Annotation

**Scope:** decision-support engagements for a named receiving decision or Work. **Lenses:** **Gov** concerns participation and decision authority; **Arch**, the engagement boundary and dependent contributions; **Onto/Epist**, keeping the subject, claims, recommendation, and later choice distinct; **Prag**, a useful return at proportionate effort; **Did**, plain entry cues that preserve the distinction between cheap recognition and consequential assurance.

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| sponsor-language bias | The sponsor's first wording becomes the problem and scope. | Name the receiving use, affected consequence, exclusions, and reopen condition before accepting the formulation. |
| authority-by-visibility bias | The meeting chair, report author, model owner, or recipient is treated as the choice owner. | Recover the later decision and its authority basis separately. |
| Method-first bias | A familiar PSM, workshop, model, or scoring scheme determines the engagement boundary. | Return the bounded question first; select Methods only for the result that is actually missing. |
| stakeholder-list bias | A visible list is treated as complete participation and concern recovery. | Continue with `PSDA.12` when affected Systems, representation, duties, interests, or dissent can change the return. |
| recommendation-as-choice bias | A confident recommendation, rank, or tool output is presented as authorization. | State the recipient, choice owner, next use, and stop at the recommendation boundary. |
| exhaustive-framing bias | Every possibly related concern is admitted before any useful result can be returned. | Choose the smallest current boundary and one observable reopen condition. |

### PSDA.11:7 - Conformance Checklist

- [ ] The opening names a recognizable receiving decision or Work and the smallest useful decision-support return.
- [ ] Decision-support performer, recipient, holder or subject, and choice owner are separately recoverable.
- [ ] Any coincidence among those positions is explicit and does not transfer authority by wording alone.
- [ ] The holder or subject, horizon, relevant configuration, and at least one consequence of a wrong boundary are visible at the grain needed by the current use.
- [ ] The current included and excluded scope and one observable reopen condition are stated.
- [ ] Contestation opens `PSDA.12`, `PSDA.1`, `PSDA.2` only when participants, formulations, or scope can change the return; it is not a membership requirement for PSDA.11.
- [ ] A bounded direct-advice case can proceed to the first missing `PSDA.5`, `PSDA.6`, `PSDA.7`, `PSDA.8`, `PSDA.9`, `PSDA.14` or external-result branch without a compulsory problem-structuring sequence.
- [ ] Missing authority, subject, horizon, source, or receiving use produces an exact return rather than an invented value.
- [ ] The result does not claim that a recommendation is the later choice, that planned Work occurred, or that an effect obtained.
- [ ] The body supports both a contested-situation entry and development-direction advising without giving either entry a different meaning of engagement or authority.

### PSDA.11:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “First agree what the problem is.” | Preserve materially different formulations and ask which receiving decision each would change. |
| “The client is the decision maker.” | Separate recipient, holder, choice owner, and authority basis; name any supported coincidence. |
| “Run the workshop and the scope will emerge.” | State the intended return and provisional boundary before choosing the workshop Method. |
| “The model says option A, so that is the decision.” | Keep model result, recommendation, authority, and later `ChoiceResult` separate. |
| “We need every stakeholder before we can start.” | Return a bounded current question and use `PSDA.12` to expose which missing participant or concern can change it. |
| “This is only advice, so authority does not matter.” | State who may prepare, receive, rely on, and choose whenever those differences change use or consequences. |
| “Use PSDA.11 as stage one of every engagement.” | Bypass it when the receiving question and authority boundary are already adequate and another result is the live gap. |

### PSDA.11:9 - Consequences

A decision-support engagement gains a usable first result before it gains heavy apparatus. Practitioners can stop on one missing value, route contestation to participation and plural-formulation Work, or proceed directly to alternatives and recommendation when the question is already bounded. Recommendations become easier to inspect because their recipient, subject, horizon, authority boundary, and next use were not reconstructed after the analysis.

The cost is explicit clarification at the start and occasional reopening later. Some requests will stop before analysis because no receiving decision, choice owner, horizon, or subject can be supported. Others will widen after affected participants or rival formulations become visible. Those are useful returns, not failed stages.

### PSDA.11:10 - Rationale

The engagement boundary is the smallest professional decision-support result that can coordinate problem structuring and later analysis without pretending that either has already occurred. Starting from a fixed problem statement is too narrow for contested or revisable framing. Starting from an unlimited situation is too broad to guide a return. Starting from a Method confuses the means with the receiving use.

Generic FPF patterns already govern outside-practice results, evidence, permission, agency, and choice. PSDA.11 does not reproduce them. It contributes the field-specific opening that connects a separately governed later decision to a provisional problem-structuring and decision-support boundary, and it tells the practitioner which exact downstream question is now live.

### PSDA.11:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How should a practitioner open an ill-structured or contested decision-support situation? | The best-known line is to bind inquiry to a named receiving use while keeping framing plural, contextual, and revisable before committing to one PSM, model, or formulation. | A fixed sponsor brief or Method-first workshop is the serious default; an unbounded “include everything” inquiry is the opposite default. | Both defaults hide the decision-support return: one naturalizes the first frame, the other cannot stop. **Adapt:** `PSDA.11:4.1`–`4.4`, the flood-pump case, and the first seven checklist rows require a receiving use, provisional boundary, plural-formulation return, and local reopen before Method choice. | Smith and Shaw's [2019 PSM review](https://doi.org/10.1016/j.ejor.2018.05.003) is a best-known-line candidate for the continuing PSM branch and its differing characteristics; Kogetsidis's [2025 review](https://doi.org/10.1108/IJOA-08-2024-4746) is an application comparator. Kelly and Gero's [2022 framing review](https://doi.org/10.1017/dsj.2022.25), Litster, Cardoso, and Hurst's [2024 systems-mapping study](https://doi.org/10.1017/S089006042400012X), and Nickel, Hurst, and Duimering's [2024 contextual trade-off study](https://doi.org/10.1017/dsj.2024.34) support explicit candidate framing, contextual comparison, and revision. The reviews are non-exhaustive; the studies establish neither one framing ontology, universal Method, shared frame, prevalence, nor superiority. | Reopen if comparative practice shows a lower-effort opening that preserves the same receiving-use, plurality, authority, stop, and revision value, or if a source changes the conditions under which framing must be reopened. |
| How should decision-support advice remain useful without becoming the later choice? | The best-known current FPF line is result-first and authority-bounded: name the receiving decision, reuse or request only the outside-practice result it needs, return the recommendation as a premise, and let the authorized chooser produce the separate `ChoiceResult`. | Expert-report, approval, score, or model-output language treated as the decision is the serious default. | The default transfers authority by format and hides blockers. **Adopt:** `PSDA.11:4.1`, `4.2`, `4.5`, the development-direction case, and the authority checks keep performer, recipient, holder, outside-result owner, and choice owner distinct. | Current `A.15.9` supplies the smallest bounded-result return and supplier/receiver authority split; current `C.11` supplies choice over an already-available option set. Neither pattern bounds a professional problem-structuring and decision-support engagement or selects its next field-specific branch. | Reopen if direct choice or outside-result guidance gains the complete engagement-boundary move at equal or lower effort, or if practitioner use shows that the current separation prevents rather than improves a necessary authorized combined role. |

### PSDA.11:12 - Relations

- `PSDA.12` receives a bounded receiving inquiry when participants, concerns, affected Systems, duties, interests, representation, or dissent can change the return.
- `PSDA.1` receives the case when materially different problem formulations imply different boundaries, evidence, values, or interventions. `PSDA.2` receives the deliberate included/excluded scope and reopen decision.
- `PSDA.3`, `PSDA.4`, `PSDA.13` receive model, PSM-selection, and facilitation questions only when those results are current. `PSDA.5`, `PSDA.6`, `PSDA.7`, `PSDA.8`, `PSDA.9` receive alternatives and comparison questions after the engagement is bounded.
- `PSDA.14` prepares and returns a recommendation without authorizing the later decision. `PSDA.15` relates changed premises and later observations to continuation, adjustment, evidence refresh, or reframing.
- `A.15.9` supplies the inspect-reuse-or-request boundary for one outside-practice result. `A.10` governs any evidence, source, currentness, or bounded reliance claim actually used.
- `C.11` governs the later choice over an already-available option set. `A.13`, assignment, capability, permission, responsibility, and authority patterns govern those actual claims when the engagement relies on them.
- Both `PSDA-CARD-01` and `PSDA-CARD-02` begin from this same engagement and authority meaning. The entries add unlike extended-use examples; they neither redefine PSDA.11 nor impose a traversal order.

### PSDA.11:End

## PSDA.12 - Recover Participants, Concerns, and Affected Systems for a Decision-Support Inquiry

> **Type:** DPF pattern body
> **Status:** Stable
>
> **Primary working result:** an **explicit participation and concern account** for one bounded receiving inquiry: who is participating or represented, which affected Systems and possible consequences remain material, which concerns, duties, interests, and dissent are recoverable, what is missing or uncertain, and what would reopen the account.

### PSDA.12:0 - Use This When

Use this pattern when a bounded decision-support inquiry may be shaped mainly by its loudest, most available, or formally powerful participants, while quieter participants, represented people, consequence-bearing Systems, or material concerns can still change the formulation or return.

Begin from the bounded engagement question in `PSDA.11` when it is current. Recover possible consequence bearers through `A.1.CSD`, then recover the participation conditions and concerns needed by this particular inquiry. Return an explicit account rather than treating attendance, a stakeholder list, or one facilitated conversation as proof of completeness.

The practical gain is a visible basis for whose situations and concerns can change the inquiry without requiring universal inclusion or pretending that participation transfers decision authority. Do not use PSDA.12 for a generic contact list, public-relations audience map, or organization chart. Use `A.1.CSD` directly when the only live question is which Systems may undergo a material change. Use the direct governance, legal, ethical, safety, representation, conflict, or authority practice when that practice owns the whole question.

#### PSDA.12:0.1 - Working Distinctions

| Working term | Meaning in this pattern |
| --- | --- |
| participant | A person or arrangement whose contribution is sought or used in the bounded inquiry. Participation alone proves neither System status, representativeness, agreement, capability, nor authority. |
| affected System | An actual System or intended referent that may undergo a relevant change through a supported direct relation or a stated modal path. Use `A.1.CSD` for this discovery and keep actual and possible relations distinct. |
| concern | A source-attributed matter that a participant, represented person, duty holder, interest holder, or affected-System account makes material to the receiving use. A recorded concern is not thereby true, decisive, or jointly held. |
| representation | A supported basis on which one participant speaks, reports, advocates, or acts for another person or constituency. Presence, title, confidence, or similarity does not establish it. |
| participation condition | An access, timing, language, safety, capability, format, dependency, or other condition that changes whether a contribution can be made or relied upon. |
| participation and concern account | The smallest recoverable account of current and missing participation, affected Systems, concerns, duties, interests, dissent, evidence, uncertainty, and next use for one bounded inquiry. |

### PSDA.12:1 - Problem frame

Contested situations rarely present a neutral list of stakeholders. Sponsors, operators, specialists, residents, customers, regulators, future users, and consequence bearers enter through different channels and with unequal time, language, safety, information, and formal power. Some affected Systems cannot speak; some people speak without a supported representative relation; some participants hold duties or authority without bearing the largest consequences.

The primary concern here is not universal participation. It is whether the current inquiry has enough explicit participation and concern recovery to avoid a materially misleading formulation, model, alternative set, comparison, or recommendation. Recognition can begin with one plausible missing bearer or one silenced concern. Consequential claims about harm, duty, representation, evidence, law, safety, or authority still require their direct assurance.

### PSDA.12:2 - Problem

A stakeholder list collapses several different questions: who attends, who contributes evidence, who may be affected, who holds a duty or interest, who represents whom, and who decides. The most visible contributors then define the concern set. Non-attendance is read as indifference; a representative's statement is generalized beyond its basis; a possible consequence is reported as an observed one; or a facilitator's synthesis becomes false consensus.

The opposite failure is exhaustive participation. Work stops until every possibly related person is present, even when the bounded receiving use needs only the smallest material account and an honest missing-participant stop. PSDA.12 must expose consequential absence without claiming that every inquiry is a deliberative assembly.

### PSDA.12:3 - Forces

| Force | Tension |
| --- | --- |
| Practical inclusion | Missing voices can reverse the inquiry, while universal recruitment is impossible. |
| Consequence discovery | Affected Systems matter even when they cannot participate, while possible impact must not be reported as fact. |
| Participation and authority | Contributions need access and protection, while neither attendance nor facilitation transfers the later choice. |
| Concern fidelity | Duties, interests, experiences, and dissent must remain attributable, while a usable account cannot become a transcript archive. |
| Representation | Some people must rely on representatives, while titles and self-selection do not prove the relation. |
| Recognition and assurance | Cheap cues should expose a gap, while consequential claims need direct sources and specialist checks. |

### PSDA.12:4 - Solution

Recover participants and concerns relative to one bounded inquiry and receiving use. Start from possible consequence bearers, not only invitees. Keep participation, affected-System status, concern attribution, representation, and decision authority as separate claims. Return the smallest account that can change the next problem-structuring or decision-support result.

#### PSDA.12:4.1 - Bind the account to one inquiry

Name the `PSDA.11` bounded engagement question, or state the same subject, recipient, receiving decision or Work, horizon, and authority boundary directly. Do not import a participation account from another decision merely because the organization, place, or topic is similar. If the engagement identity or receiving use is missing, return that gap to `PSDA.11`.

Ask: whose situation, contribution, duty, interest, or possible change could make the current return materially different? This question bounds discovery without assuming that every discovered bearer must attend.

#### PSDA.12:4.2 - Discover affected Systems before equating them with participants

Use the smallest `A.1.CSD` pass that can challenge the current boundary. Name the focus, configuration, scope, horizon, receiver, examined possibilities, actual direct relations, modal paths, bearers, possible changed characteristics, evidence, uncertainty, and reopen trigger at the grain the inquiry needs.

An affected System may be a participant, be represented by a participant, or have no feasible participation channel. Participation can reveal a bearer or path, but it does not prove System construction, a relation occurrence, a consequence, or authority. Use the direct relation pattern for an obtaining claim. Open `A.6.REL` only when later work must distinguish this occurrence from another occurrence of the same relation kind, including another episode with the same participants; a readable current relation assertion is otherwise enough.

#### PSDA.12:4.3 - Recover participation positions and conditions

For each materially distinct contribution, record who contributes, the basis of involvement, what knowledge or experience is being offered, the participation channel, and any condition that limits access or reliance. Name missing or unsafe participation explicitly.

Recover a representative relation only when the current use relies on it. State whom the participant represents, for what question, under which basis, and with what limit. Keep self-report, specialist evidence, advocacy, delegated representation, duty, interest, sponsorship, facilitation, and choice authority distinct.

#### PSDA.12:4.4 - Attribute concerns, duties, interests, and dissent

Record each material concern in ordinary language with its holder or source and the consequence or receiving-use difference it could make.

Establish what the concern is about before joining it to another concern under the same word. Ask what is being done or changed, where that object or work begins and ends, and what would count as the relevant result. Participants saying “the trip is complete” may mean that the remote task is finished, the traveler has returned, or the expense case is closed. Those are different objects with different completion conditions. Recover how they are related and which result each participant needs. In other cases, participants do concern themselves with the same object: duration and cost can describe the same identified journey. Keep that common reference when it fits.

Use this recovery where ambiguity changes the inquiry; ordinary unambiguous concerns need no separate object inventory. Also identify who or what may bear the consequences; that bearer can be the object being discussed or another System. Distinguish:

- reported experience from externally supported evidence;
- duty from preference or interest;
- individual concern from a represented constituency claim;
- disagreement from an unresolved factual question; and
- absence of evidence from evidence of absence.

Keep minority and unresolved positions visible. Facilitation may make contributions usable; it does not establish consensus, truth, priority, permission, or authority.

#### PSDA.12:4.5 - Return the smallest explicit account

| Result position | Required content |
| --- | --- |
| bounded inquiry | Subject, receiving use, horizon, recipient, and retained choice owner. |
| current participation | Participants, contribution bases, channels, and material participation conditions. |
| consequence bearers | Actual Systems or intended referents, supported relations or modal paths, possible changes, evidence, and uncertainty. |
| concerns and positions | Attributed concerns, duties, interests, agreements, dissent, and unresolved questions; the objects and relations needed to understand materially ambiguous terms. |
| representation | Any relied-upon representative relation and its scope; otherwise the explicit gap. |
| material absences | Missing participants, bearers, concerns, channels, or assurance that can change the inquiry. |
| next use and reopen | Which formulation, scope, facilitation, value, or later result consumes the account, and what observation reopens it. |

Stop when the account is adequate for the named next use, not when every possible participant has been contacted. If a missing participant or concern can reverse that use, return the gap, narrow the claim, request the direct result, or abstain.

#### PSDA.12:4.6 - Use the account without making it decide

Pass materially different concerns into `PSDA.1`, boundary challenges into `PSDA.2`, participation conditions into `PSDA.13`, value inputs into `PSDA.6`, and participation-related interference into `PSDA.17` when it obstructs the engagement result. Inclusion in the account does not settle a formulation, priority, model, alternative, recommendation, or later choice.

Reopen locally when a new bearer, consequence path, participant, concern, duty, interest, representation basis, dissent, participation condition, receiving use, horizon, or authority relation can change a dependent result.

#### PSDA.12:4.7 - What changes in practice

The practitioner stops using an invitation list as the social boundary of the problem. They can show who and what may be affected, who contributed under which conditions, whose concerns are attributed rather than generalized, what remains missing, and exactly which next result could change.

### PSDA.12:5 - Archetypal Grounding

#### PSDA.12:5.1 - Flood-pump participation and concern account

For the emergency investment board's pre-season pump decision, the team begins with the `PSDA.11` engagement. Operations and finance staff are available, but district residents, emergency responders, maintenance contractors, downstream ecology staff, and people with limited mobility may bear different consequences.

An `A.1.CSD` pass distinguishes observed basement flooding and pump downtime from possible displacement, access failure, downstream transfer, and ecological change. Resident contributions are attributed by district and channel; one neighborhood association is not assumed to represent every resident. Emergency responders hold operational knowledge and duties but do not thereby own the investment choice. A no-new-purchase concern remains visible beside capacity, equity, maintenance, safety, and environmental concerns.

The returned account names inaccessible evening meetings and missing mobility-service evidence as participation gaps. It is adequate to open `PSDA.1`, because the recovered concerns support materially different formulations. It does not declare consensus or recommend a pump.

#### PSDA.12:5.2 - Affected System without a speaking participant

A service redesign may change response time for a machine-supported monitoring arrangement and for patients who cannot participate directly. The arrangement and patients can enter the affected-System account through supported paths even when no direct participant is available. A clinician, advocate, or family member contributes only under the stated evidence or representation basis. The practitioner returns the unresolved representation or consequence gap rather than inventing a voice.

#### PSDA.12:5.3 - Cheap non-use

A current, low-consequence internal choice has one authorized team, one directly affected workcell, an already-supported consequence account, no representation question, and no material dissent. The live question is comparison among three qualified settings. Repeating PSDA.12 adds no value; use the comparison or choice pattern directly.

#### PSDA.12:5.4 - A completed trip with an unfinished task

A sponsor asks why business trips are failing. An employee has returned from a site visit, and administration has closed the expense case, but the equipment fault the employee was sent to repair remains unresolved. “Trip completed” therefore gives three different answers: journey complete, administrative case complete, remote repair incomplete.

The inquiry identifies the repair work and its intended result, the journey that enabled the visit, and the administrative provision and records. It examines their actual connections: timely travel and site access may enable the repair, while closing an expense case does not settle whether the repair is complete. The first result is a corrected question: what prevents completion of the remote repair, and which travel or administrative conditions contribute to that difficulty? Faster expense processing may be useful, but its completion cannot answer the repair question.

For an unlike case, “access granted” can mean that permission was issued while the account is still unable to open the needed system. Identify the permission, configured access and actual use before deciding what failed. Conversely, an employee and administrator discussing the duration and reimbursable cost of the same identified journey can retain one common object with different concerns. Roles and words alone do not decide object identity.

### PSDA.12:6 - Bias-Annotation

**Scope:** participation and concern recovery for one bounded decision-support inquiry. **Lenses:** **Gov** keeps contribution, representation, duty, and choice authority distinct; **Arch** tracks which participants and concerns can change dependent results; **Onto/Epist** separates Systems, reports, possible paths, and supported relations; **Prag** stops at a sufficient account; **Did** supplies plain recognition cues and an explicit assurance boundary.

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| visibility bias | Available or powerful speakers define the concern set. | Start from possible consequence bearers and record material absences. |
| attendance-as-representation bias | Presence or title is treated as authority to speak for others. | State the representation basis, scope, and limit separately. |
| participation-as-proof bias | A workshop report is treated as proof of Systemhood, consequence, or consensus. | Keep participation, relation, evidence, and agreement claims distinct. |
| stakeholder-exhaustion bias | Work waits for universal participation. | Stop at adequacy for the named use and return exact gaps. |
| harmony bias | Facilitation erases minority or unresolved positions. | Preserve attributed dissent and its consequence for the next result. |
| human-only bias | Non-speaking or non-human consequence bearers disappear. | Use `A.1.CSD` to recover affected Systems and possible changes. |

### PSDA.12:7 - Conformance Checklist

- [ ] The account is bound to one receiving inquiry, subject, horizon, and authority boundary.
- [ ] Participants, affected Systems, represented people, duty or interest holders, and choice owner are not collapsed.
- [ ] Actual relations, modal paths, observed changes, and possible consequences remain distinguishable.
- [ ] Material concerns are attributed; recording them does not imply truth, priority, consensus, or authority.
- [ ] Any relied-upon representation and participation condition is supported and scoped.
- [ ] Missing participants, bearers, concerns, or assurance produce a visible gap, narrowed claim, request, blocker, or abstention.
- [ ] The stopping rule is adequacy for a named next use rather than exhaustive recruitment.
- [ ] Recognition is cheap, while legal, ethical, safety, harm, duty, representation, and authority claims retain their direct assurance.
- [ ] The result can feed plural formulation, boundary, facilitation, value, or inquiry Work without deciding any of them.

### PSDA.12:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “The stakeholder register is complete.” | Ask which plausible consequence bearer or participation condition could change the receiving use. |
| “Everyone agreed in the workshop.” | Preserve who expressed what, under which channel and limits; establish consensus only through its direct basis. |
| “The community representative speaks for residents.” | Recover the constituency, mandate, scope, and dissent or return the representation gap. |
| “Affected means invited.” | Discover consequence bearers independently of participation. |
| “Every concern becomes a criterion.” | Pass concerns to the formulation and value patterns; do not convert them silently. |
| “No one mentioned it, so it is irrelevant.” | Distinguish missing evidence or access from supported non-materiality. |

### PSDA.12:9 - Consequences

Problem formulations and later recommendations gain a recoverable social and consequence basis. Quiet, represented, missing, and non-speaking bearers remain visible without requiring impossible universal participation. The cost is explicit attribution and occasional stopping when representation, access, or consequence evidence is inadequate.

### PSDA.12:10 - Rationale

Problem structuring needs more than generic affected-System discovery and more than a meeting roster. `A.1.CSD` supplies the shared discipline for finding consequence bearers and keeping actual and modal paths honest. PSDA.12 adds the field-specific participation move: recover contribution conditions, concerns, duties, interests, representation, and dissent for a bounded receiving inquiry, then pass rather than decide them. Concern recovery also identifies what each material statement concerns. Otherwise a shared word can make completed support work appear to settle an unfinished task, or turn different objects into apparent disagreement about one object.

### PSDA.12:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How should participation be recovered in an ill-structured decision-support situation? | The continuing PSM branch, including facilitated modeling and multi-method arrangements documented for ill-structured situations. | A sponsor-built stakeholder list or open workshop is the serious default; universal recruitment is the opposite default. | A sponsor's list can hide consequential absence, while universal recruitment supplies no usable stop. **Adapt:** `PSDA.12:4.1`–`4.5` returns a use-bounded participation and concern account whose omissions and dissent remain visible. | Smith and Shaw's [2019 PSM review](https://doi.org/10.1016/j.ejor.2018.05.003) and Kogetsidis's [2025 review](https://doi.org/10.1108/IJOA-08-2024-4746) support the continuing branch, differing Methods, and documented facilitated or multi-method use. They do not establish representativeness, universal facilitation sufficiency, or comparative superiority. PSDA's architecture assigns participation and concern recovery to this pattern; attribution, representation limits, and missing-participant stops are constraints on that account. Current `A.1.CSD` separately supplies consequence-bearer discovery. The resulting combined PSDA rule is an adaptation, not an externally demonstrated best participation protocol. | Reopen if newer comparative evidence changes the conditions under which facilitated participation is adequate, the direct FPF contribution changes, or a material bearer or participation condition is discovered. |
| How should affected Systems enter without turning participation into proof? | Use current `A.1.CSD` to recover actual Systems or intended referents, direct relations or modal paths, possible changed characteristics, evidence, uncertainty, and receiver connection; then use PSDA.12 only for the participation-specific account. | Attendance, complaint volume, or generic impact language is the serious default. | It confuses reports, bearers, paths, changes, and authority. **Adopt:** `PSDA.12:4.2` and the non-speaking-bearer case keep those claims separate. | Current `A.1.CSD` is the direct FPF source for affected-System consequence discovery. Each obtaining claim remains with its direct relation pattern; `A.6.REL` adds occurrence identity only when later use must distinguish occurrences of the same relation kind. These contributions do not recruit participants, establish representation, facilitate inquiry, or rank concerns. Domain safety, legal, ethical, and scientific practices retain their own Methods and thresholds. | Reopen if the direct patterns acquire the full participation-and-concern move at equal or lower effort, or if evidence changes a relied-upon bearer, path, or consequence. |

### PSDA.12:12 - Relations

- `PSDA.11` supplies the bounded subject, receiving decision or Work, horizon, recipient, and authority boundary; absent or stale values return there rather than being inferred.
- `A.1.CSD` supplies affected-System consequence discovery. The relevant direct relation pattern governs each obtaining claim; `A.6.REL` applies only when the receiving use must distinguish occurrences of the same relation kind.
- `PSDA.1` receives materially different participants and concerns as formulation input without treating inclusion as settlement. `PSDA.2` receives boundary challenges.
- `PSDA.13` receives participation conditions for facilitation; `PSDA.6` receives attributed value inputs; `PSDA.17` receives the participants, concerns and work relations needed to resolve material interference in the engagement.
- Direct governance, conflict, representation, legal, ethical, safety, evidence, assignment, and authority patterns govern those claims. PSDA.12 neither replaces them nor authorizes the later choice.

### PSDA.12:End

## PSDA.13 - Facilitate Decision-Support Inquiry and Preserve Material Dissent

> **Type:** DPF pattern body
> **Status:** Stable
>
> **Primary working result:** **shared and contested claims without forced identity**: a bounded inquiry return that distinguishes what participants understand, support, reject, or leave unresolved, with attribution, evidence limits, consequences for the receiving use, and a way to reopen material differences.

### PSDA.13:1 - Problem frame

**Use this when** participants need to work on a decision-support question but disagree about its meaning, evidence, consequences, or acceptable action. Also use it when a smooth workshop is producing an apparently unanimous answer that participants cannot recognize as their own.

Start by making the inquiry's purpose, participation conditions, challenge route, and later choice boundary clear. Help participants state and test claims in terms their holders can recognize. Return useful common ground and material disagreement; agreement is one possible result, not a condition for an honest return.

The governed object is the bounded account of shared and contested claims for the receiving inquiry. Facilitation is the practical work of enabling that inquiry; the account is its result, not the conversation itself or a decision by the group. Shared wording, shared understanding, assent to a claim, consent to an action, and authority to choose remain different.

**Do not use this pattern** merely to circulate one clear qualified fact, record attendance, or administer an already-valid decision rule when no inquiry or interpretation problem remains. Direct mediation, adjudication, safeguarding, or emergency-command work retains its own remit. If the engagement has no recoverable receiving question or choice owner, return that missing premise.

### PSDA.13:2 - Problem

Facilitation can suppress the differences it is meant to make usable. A participant's objection becomes a neutral-looking label, an absent group is treated as represented, and silence is recorded as consent. A model becomes “our view” although participants attach different meanings to it.

The opposite failure is endless disagreement. Every difference reopens the whole discussion, no one distinguishes an evidence gap from a value conflict, and the recipient receives a transcript instead of a result. Productive inquiry needs neither forced consensus nor unlimited debate; it needs a bounded account of what matters and what can be done with it.

### PSDA.13:3 - Forces

| Force | Tension |
| --- | --- |
| Participation | The inquiry needs relevant voices, while access, language, hierarchy, time, and safety can limit meaningful contribution. |
| Common ground | Shared understanding can support joint work, while common wording can conceal opposed claims. |
| Challenge | Claims should be open to examination, while criticism can be socially costly or become personal conflict. |
| Closure | A usable return is needed, while unresolved dissent may materially constrain it. |
| Attribution | Readers need to know whose claim is carried, while confidentiality and representation limits constrain disclosure. |

### PSDA.13:4 - Solution

Create conditions for participants to express, understand, challenge, and revise claims. Distinguish disagreement by what would resolve it, preserve material differences with their consequences, and return only the agreement and support actually established.

#### PSDA.13:4.1 - Recover the inquiry, participation, and Method conditions

Use the current `PSDA.12` participation and concern account only for participants, affected Systems, concerns, representation limits, and missing voices material to this inquiry. Use the `PSDA.4` engagement Method and limits only for the same situation and qualification window. These inputs help establish what to facilitate; their availability does not show that participation is complete or the Method is being enacted.

Recover the receiving question, intended result, and later choice boundary from the current engagement terms or another qualified direct source. Make clear what this interaction can establish and what remains with the decision owner or a direct specialist.

If an input needed for the result is missing, stale, or incompatible, obtain its qualified direct source or name the precise gap. Do not infer consent, representation, permission, or authority from a participant list, a concern map, or a Method description. An affected System need not have a person present who is entitled or able to represent all its concerns.

#### PSDA.13:4.2 - Establish workable participation and challenge conditions

Tell participants what is being asked, how their contribution will be used, how attribution and correction will work, and who will receive the return. Choose channels that permit meaningful contribution and challenge: a joint session, separate conversation, written response, accessible format, or a combination suited to the actual conditions. A workshop is not mandatory.

Make the facilitator's remit and material interests visible. If the facilitator also owns a preferred intervention or controls participants' opportunities, choose safeguards appropriate to that conflict, such as independent handling of a contested claim or a different facilitator. Do not describe the arrangement as neutral merely because the facilitation script is neutral.

Recover any rule governing consent, participation, confidentiality, or later decision from its actual authority. Ask whether the proposed conditions are usable, but do not treat acceptance of the discussion format as assent to its eventual findings. Where credible participation would expose someone to material harm or coercion, use an appropriately protected route, obtain competent support, narrow the claim, or stop that part of the inquiry.

#### PSDA.13:4.3 - Elicit and test meaning before merging claims

Ask for concrete statements: what is happening or might happen, to whom, under which conditions, why it matters, and what would change the speaker's view. Show how a contribution has been represented and invite its holder to correct the meaning. When useful, ask another participant to restate the claim and let its holder identify the remaining difference.

Separate observations, reported experience, causal hypotheses, preferences, duties, proposed actions, and commitments. A participant may agree that a claim was represented accurately while disagreeing that it is true or desirable. Keep those answers distinct.

Use models and shared displays to make questions discussable. A new connection or translation remains a proposal until its meaning and evidence are established. If two participants use “reliable service” differently, retain the two meanings instead of selecting a single label for convenience.

#### PSDA.13:4.4 - Turn material disagreement into a usable inquiry result

A disagreement is material when it can change a formulation, candidate intervention, consequence claim, value treatment, recommendation, implementation condition, or legitimate receiving use. Preserve at least the disputed claim, its attributed positions, why the difference matters, the current basis, and what could change the next move.

| Difference | Useful facilitation move | Honest remaining result |
| --- | --- | --- |
| Different meanings or scopes. | Recover examples and conditions; test a paraphrase or explicit distinction. | A repaired meaning or two still-distinct readings. |
| Different factual or causal claims. | Identify the evidence, assumption, or discriminating observation required. | A qualified claim, unresolved evidence question, or bounded contradiction. |
| Different values, interests, or priorities. | Make the consequence and trade-off explicit without pretending it is a missing measurement. | Attributed value positions for the later value or choice question. |
| Disputed right, duty, representation, or choice authority. | Obtain the direct competent rule or result. | A supported boundary, exact authority gap, or stop on the disputed use. |
| Different willingness to endorse or commit. | Ask what, if anything, each participant actually supports and on what conditions. | Bounded support, dissent, abstention, or a separately established commitment. |

An objection is neither an automatic veto nor something to erase by a majority count. Its effect follows from the actual claim and applicable decision rule. A vote can establish its own result when authorized; it does not settle truth, all participants' consent, or the legitimacy of an unsupported trade-off.

Continue with unresolved differences when the receiving use can honestly preserve them. If a missing premise prevents that use, return the premise or narrow the result. Do not ask participants to manufacture consensus to keep the engagement on schedule.

#### PSDA.13:4.5 - Keep the result faithful without collecting everything

Keep enough attribution and evidence for the recipient to understand and challenge each material claim. Retain the scope of representation: “the association's representatives stated” is different from “residents agreed”. Where a protected contribution cannot be openly attributed, preserve its qualified status and disclosure limit without inventing public endorsement.

A transcript is not normally needed. Reuse a concise claim account, a corrected map, or annotated conclusions. Avoid collecting personal detail that contributes nothing to the receiving question, and do not promise anonymity or confidentiality that the actual arrangements cannot support.

Recognition of a difference needs no formal relation register. If later reliance requires a claim that consent, authorization, representation, or another relation obtains, use that relation's direct pattern and evidence. Use `A.6.REL` only when the receiving use must additionally distinguish occurrences of the same relation kind, including separate episodes with the same participants.

#### PSDA.13:4.6 - Close with shared and contested claims

Read back the proposed return at the grain needed for its use. Invite correction of meaning, attribution, support, conditions, and omissions. Record a correction that arrives after the discussion if it materially changes the return; identify which dependent use must reopen.

The recipient should be able to distinguish:

- shared understanding of a statement from support for that statement;
- supported common claims from conditional claims, unresolved evidence, and dissent;
- participants who responded from absent, unreachable, unrepresented, or declining participants;
- proposed action from commitment or authorization; and
- what the inquiry enables now from the direct result still needed.

Use `A.2.9` when the live question is whether the communication enabled a named recipient to understand or do something and what smallest repair is needed. An acknowledgement or later action is not sufficient proof of understanding, consent, or causal effect. Add exact communicative-Work detail only when that stronger reliance is actually needed.

Return the common claims, material disagreements, evidence gaps, their consequences for the receiving question, and the next discriminating question or reopen condition. The account may inform alternative generation, a recommendation, or reconciliation between simultaneous inquiries. It neither chooses the matter nor requires all participants to become one collective viewpoint.

#### PSDA.13:4.7 - What changes in practice

The facilitator no longer measures success by a smooth meeting or a unanimous closing slide. The useful result is that participants can recognize how their claims were carried and the recipient can see what is shared, disputed, unknown, and still outside the group's authority.

### PSDA.13:5 - Archetypal Grounding

#### PSDA.13:5.1 - A flood-pump return that retains disagreement

In this illustrative inquiry, the board's current engagement terms reserve the investment choice to the board. The participation account distinguishes the residents' association from a separately consulted group of mobility-constrained residents; neither represents all district residents. Operations staff supply their current technical assumptions, while the selected Method calls for attributed service claims and conditional technical analysis.

The facilitator presents three proposed conclusions and obtains these corrections:

| Proposed conclusion | What inquiry establishes | Returned claim |
| --- | --- | --- |
| “The pumps can protect the district.” | The technical calculation concerns nominal capacity under stated inflow and availability assumptions. It does not establish deployment access or every resident's protection. | The conditional capacity claim is shared by the responding participants; the broader protection claim is unsupported. |
| “Residents want the least expensive pumping option.” | Association representatives emphasize property protection and cost. The separately heard group asks how assistance remains reachable when roads fail. No complete cost comparison or district-wide endorsement is available. | Preserve the two attributed service concerns; do not claim a common preference or a chosen option. |
| “The mobile branch is acceptable if capacity is sufficient.” | Operations staff cannot yet support its arrival-time premise under the road-loss condition. The mobility concern remains material even if nominal capacity is adequate. | Keep the branch conditional on access evidence and retain the service disagreement for alternatives and recommendation. |

The result says: “There is a shared conditional reading of nominal capacity, not shared endorsement of an investment. The mobile branch has an unresolved access premise. Property-protection and reachable-assistance concerns remain separately attributed. The board receives these claims and gaps; the inquiry has made no investment commitment.”

The facilitator sends the wording back through the available channels for attribution correction. Missing replies remain missing replies. A later verified access result can close that technical question without resolving the value difference; a participant's corrected service meaning reopens only the affected claim and its downstream use.

#### PSDA.13:5.2 - A manager's summary is not a team's consent

A manager proposes a development direction and asks staff to comment in a meeting where dissent could affect their assignments. Silence is not an adequate basis for “the team supports the plan”.

The facilitator offers an appropriately protected response route or a separately facilitated discussion and states its real disclosure limits. Until usable participation is possible, the return reports the manager's proposal and the limitation on staff input. It does not fabricate agreement, infer hidden opposition, or undertake specialist safeguarding work without its proper support.

#### PSDA.13:5.3 - Cheap non-use

Two analysts agree on a clarified unit conversion and only need the corrected value in their calculation note. Send the qualified correction and confirm the needed understanding. A new facilitated inquiry or dissent register adds no useful result.

### PSDA.13:6 - Bias-Annotation

**Scope:** facilitated inquiry that supports a bounded receiving decision without owning it. **Lenses:** **Gov** separates participation, representation, consent, and choice; **Onto/Epist** separates claim meaning, support, evidence, and occurrence; **Prag** seeks usable closure; **Arch** preserves dependencies on unresolved claims; **Did** makes contested meanings recognizable.

Consensus bias treats a quiet room as a successful outcome. Sponsor bias gives one formulation privileged status. Attribution bias extends one representative's statement to a population. Conflict-avoidance bias weakens an objection until it no longer changes the result. Counter these by checking the exact proposed return with its holders and preserving each material disagreement's practical consequence.

### PSDA.13:7 - Conformance Checklist

- [ ] The inquiry's receiving question, intended result, and later choice boundary are recoverable.
- [ ] Needed participation and Method inputs fit the present situation and qualification window, or their exact gaps are returned.
- [ ] Participation, correction, challenge, attribution, and disclosure conditions are usable rather than merely announced.
- [ ] The facilitator's material interests and limits are visible.
- [ ] Shared meaning, claim support, factual evidence, value preference, consent, and authority remain distinct.
- [ ] Material dissent retains attribution, basis, consequence, and a discriminating question or reopen condition.
- [ ] Absence, silence, abstention, and representation limits do not become agreement.
- [ ] Direct relation claims receive their own assurance; an occurrence register is not compulsory.
- [ ] The return is concise enough to use and precise enough for participants to challenge.
- [ ] Closure neither invents a decision nor conceals a premise that prevents the receiving use.

### PSDA.13:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Everyone agreed with the slide.” | Ask which meaning and claim each response actually supports. |
| “No objection means consent.” | Recover the participation conditions and any applicable consent rule; otherwise report only the observed response. |
| “The representative speaks for everyone affected.” | Carry the actual representation basis and limits. |
| “Keep dissent in the transcript; simplify the recommendation.” | Preserve every disagreement that can change the receiving recommendation or its conditions. |
| “Every objection blocks progress.” | Distinguish its consequence under the actual evidence, authority, and decision rules. |
| “A neutral script makes the facilitator neutral.” | Expose material interests and choose an appropriate safeguard or facilitator. |

### PSDA.13:9 - Consequences

The receiving practitioner obtains usable common ground without losing the disagreements that can reverse a decision-support claim. Evidence questions, value conflicts, and authority gaps can take different next routes. The cost is explicit correction and dissent handling, and sometimes a narrower return when meaningful participation is unavailable.

### PSDA.13:10 - Rationale

Facilitation helps people make claims and differences inspectable; it does not make their meanings, interests, or authority identical. Bounded closure works when the result says what further work can rely on and where reliance must stop. This can preserve disagreement while still enabling a concrete next move.

### PSDA.13:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How can facilitation make different meanings usable? | Attend to the actual interaction: elicit concrete contributions, test formulations with participants, and revisit how the developing model carries their meanings. | Following a workshop script or completing a shared diagram is treated as sufficient evidence of common understanding. | **Adapt:** `PSDA.13:4.2`–`4.3` and `4.6` add targeted meaning and attribution checks within the same interaction. The extra attention is accepted for a material difference, without requiring a full recording or research study. | Franco and Greiffenhagen's [2018 facilitated-modeling analysis](https://doi.org/10.1016/j.ejor.2017.08.016) supplies a bounded empirical account of situated OR practice, not a universal script. Zimmermann and Curran's [2023 microlevel study](https://doi.org/10.1002/sdr.1743) supplies the more specific candidate line on facilitator questions, references to contributions, and recursive development of shared meaning in one heritage-science workshop. Neither establishes universal transfer, consensus, or causal effectiveness for every engagement. | Reopen when participants cannot recognize the returned meaning, the channel suppresses material contributions, or stronger comparative practice supplies the same fidelity with less effort. |
| How should inquiry close when disagreement remains? | Return attributed common claims, material dissent, and the exact missing evidence or authority result. | A unanimous summary is manufactured, or all disagreement postpones every useful return. | **Adapt:** `PSDA.13:4.4`–`4.6` and both substantive cases separate meaning, support, truth, consent, and choice. This accepts a less simple summary in exchange for preserving an action-changing difference; an already-clear factual correction takes the cheap exit. | Current `A.2.9` supplies receiving-use judgement and the distinction between communication, response, achievement, consent, and authority. Current `A.6.REL` supplies occurrence distinction only when needed; direct predicates and evidence establish obtaining relations. Retaining material dissent is the PSDA solution constraint for contested decision support, not an empirical claim that disagreement always improves decisions or grants a veto. | Reopen when a direct rule changes the effect of dissent, new evidence resolves a disputed claim, attribution is corrected, or the receiving use can no longer preserve the unresolved difference honestly. |

### PSDA.13:12 - Relations

- `PSDA.12` supplies the current participation and concern account only where it is material to the inquiry. `PSDA.4` supplies the engagement Method and limits only for the matching situation and qualification window. Needed missing inputs return to qualified direct sources or exact gaps.
- `PSDA.5` may use this inquiry result where it changes the candidate set; agreement is not required and material dissent stays explicit.
- `PSDA.14` and `PSDA.17` may use the participation and dissent account to preserve material agreement and disagreement in a recommendation or simultaneous-inquiry decision. The account grants no choice authority.
- `A.2.9` governs a communication's receiving-use question and any stronger communicative-Work claim. Direct patterns govern actual consent, representation, permission, duty, and authority; `A.6.REL` adds occurrence identity only for a need to distinguish same-kind occurrences.
- Direct evidence, causal, value, legal, safety, safeguarding, and governance practices answer their own substantive questions. Facilitation can expose their missing results but cannot replace them.

### PSDA.13:End

## PSDA.14 - Prepare and Return a Decision-Support Recommendation

> **Type:** Method pattern (DPF)
> **Status:** Stable
>
> **Primary working result:** a **decision-support recommendation account** for a named recipient, subject, horizon and receiving decision: the supported disposition, considered alternatives, reasons, source limits, material dissent, protected conditions, next use and reconsideration basis. The account may be a short return or a larger package; it informs the later decision without authorizing it.

### PSDA.14:1 - Problem frame

**Use this when** analysis is available, or its decisive gap is known, but the recipient still cannot tell what the decision-support performer recommends and on what conditions. A score, workshop agreement or specialist answer is not yet a recommendation for this decision. The same need arises in an ordinary, non-contested request: “Which development direction should we consider over the next four months?”

Start with the receiving question and the strongest answer the available basis permits. Return a supported direction, retained or ranked set, bounded probe, smallest-result request, blocker or abstention. Do not force a single preferred action when the result actually supports a partial order or a missing-premise return.

Problem structuring and decision support is the wider practice. This pattern governs its **recommendation-composition and return branch**: turning qualified premises into advice usable by a particular recipient. It does not govern the recipient's choice, the specialist Methods that produced the premises, implementation, or proof that the advice caused an improvement.

The gain is practical: the recipient can distinguish what is recommended now, why, what remains unresolved, what must not be traded away, and what evidence would change the answer. A complete result can be two sentences when they identify one missing premise and the exact recommendation it prevents.

**Do not use this pattern** merely to reproduce an adequate recommendation, report one specialist result, or make a choice from an already adequate basis. Use the direct communication, supplying-practice or choice guidance instead. An unformed opportunity question needs opportunity construction before advice; an unsettled engagement question returns to `PSDA.11`. Neither case requires a disagreement workshop unless formulation, participation or dissent actually changes the result.

### PSDA.14:2 - Problem

A recommendation often becomes stronger while it travels. “This option performs better in this model” becomes “the best option”; “the group did not object” becomes “stakeholders agreed”; “the report was received” becomes “the decision was approved.” The lost conditions are precisely those the receiving decision needs.

Development advice adds a second failure. A plausible story can combine human learning, organization change and AI evaluation as if they supplied interchangeable evidence. A course catalogue then stands in for transfer into later Work, a position description for a whole-arrangement comparison, or a benchmark score for deployment safety.

The practitioner needs a positive composition rule, not just warnings. Which conclusion follows from these premises for this recipient? Which alternative remains live? Which missing result is worth requesting? When does declining to recommend supply the most useful answer?

### PSDA.14:3 - Forces

| Force | Tension |
| --- | --- |
| Usable direction and warranted strength | The recipient needs an actionable answer; incomplete preferences or evidence may justify only a retained set or bounded question. |
| Synthesis and supplier ownership | Several results must become one account without absorbing their Methods, evidence limits or authority. |
| Clarity and material plurality | A short return is easier to use, but omitted dissent or an omitted alternative can reverse its meaning. |
| Timeliness and protected conditions | Delay has consequences, but urgency does not convert missing permission, consent or safety evidence into an admissible premise. |
| Professional judgement and recipient choice | An adviser should explain a reasoned position without making the recipient's values, mandate or commitment for them. |
| Continuity and changed conditions | An earlier recommendation may remain useful in part even when one configuration, source or assumption changes. |

### PSDA.14:4 - Solution

Compose the recommendation at the strength and scope of its decision-bearing premises, then return it for the agreed use. The following moves express information dependencies, not a compulsory sequence of meetings or documents. Adequate existing results may close several needs at once.

#### PSDA.14:4.1 - Recover the receiving use and the right to provide this advice

State who receives the answer, the exact subject or holder, the horizon, the question and the later decision or other Work that will use it. Recover the actual choice owner separately. A recipient may also be the choice owner when that authority is established; receiving an answer does not establish it.

Use an adequate `PSDA.11` engagement result for the same subject and decision. Otherwise obtain the qualified direct facts or return the exact missing recipient, question, scope or authority premise. Do not infer the engagement from a title, course, department or tool output.

For development-direction advising, distinguish the recommending performer from the recipient at the grain of this application. The client, sponsor, holder, recipient and chooser may coincide in some respects and differ in others; recover only the differences that affect the advice, disclosure or later choice. A larger organization may contain both adviser and recipient. Merely naming two roles of one self-advisory actor does not create the distinct-performer engagement; direct domain and `C.11` guidance remain available.

Establish applicable professional scope, competence, material conflicts and permitted reliance before offering positive advice. For example, management-consultancy engagement and conflict conditions are informed by the [ICMCI competence framework v4.0, C.1.1–2, C.2.1 and E.3.5](https://www.cmc-global.org/sites/default/files/public/icmci_cmc002_competence_framework_version_4.0_1.pdf). Human career-service consent and assessment limits come from the applicable professional source, such as the [NCDA 2024 Code of Ethics, A.2 and E.2](https://www.ncda.org/aws/NCDA/asset_manager/get_file/3395). These are different service conditions, not one universal profession or evidence that a proposed intervention works.

If a material mandate, competence, conflict or admissibility condition cannot be satisfied, return the scoped blocker or appropriate referral. A persuasive presentation cannot repair that condition. Existing emergency, safety or legal response duties retain their own direct authority and must not wait for completion of a PSDA account.

#### PSDA.14:4.2 - Recover what the available premises actually support

For every premise that can change the disposition, recover its claim, exact subject and configuration, source or supplier, applicable window, intended use, uncertainty and reliance limit. Inspect available results first; use `A.15.9` to reuse an adequate result, retain its useful limit, or select a worthwhile obtainable missing contribution, and `A.10` to qualify the actual reliance. This pattern adds no second specialist-acquisition Method.

Read a comparison as a result over particular alternatives under particular values, evidence and assumptions. A `PSDA.9` robustness result contributes only where it can change this recommendation for the same configuration and horizon. It neither entails the whole recommendation nor authorizes the later decision. Preserve the `PSDA.6`, `PSDA.7`, `PSDA.8` comparison basis needed to interpret it.

Keep the live set and the compared subset explicit. A result about internal development and one mixed human–AI arrangement does not dispose of an external provider or a materially different probe. A gap about one candidate can prevent ranking that candidate while leaving an independent comparison usable. Do not narrow the set simply because evidence is easier to obtain for the familiar option.

Preserve material agreement, disagreement and affected-party concerns from `PSDA.13` or a qualified direct account. Distinguish a factual objection, a value conflict, an authority condition and a question about representation; they call for different responses. Give the objection and its consequence enough prominence to survive the return. Attribution and disclosure must respect the applicable protection and confidentiality conditions.

For development opportunities, consume a qualified opportunity result: the problem or promise, dependencies, bounded reachability, uncertainty and next question. A search/archive entry, a fashionable technology or a candidate label supplies none of those by itself. Opportunity construction is a separate Method with an independently useful result; composing advice does not complete missing search, dependency or reachability work.

#### PSDA.14:4.3 - Select the warranted recommendation disposition

Ask what the recipient can responsibly consider **now**, given the question, alternatives, protected conditions, comparison and consequence of delay. Explain the inference from the relied-on premises to the disposition. The six forms below are result branches, not stages to complete.

| Disposition | Positive basis and useful return | Boundary |
| --- | --- | --- |
| Retained or ranked set | Several directions remain live. Return the warranted order, partial order or trade-offs and the unresolved distinction that could narrow it. | A retained set is not consensus; an order valid under one scheme is not a universal ranking. |
| Supported direction | Qualified premises and a declared decision-support rule justify preferring one direction for this use. State the advantage and the conditions under which it holds. | Other candidates need an explicit disposition; protected conditions cannot disappear into a compensating score. |
| Bounded information-gaining probe | A specified uncertainty could change the advice, and a qualified probe is feasible and proportionate to the delay, burden and risk it introduces. Name the question, bounded exposure, useful evidence and stop. | Thin evidence alone does not justify a probe. The probe's authorization, WorkPlan and execution remain separate. |
| Smallest-result request or handoff | A named practice can supply a missing comparison, feasibility, interpretation, or other result whose obtainable contribution warrants the full formulation, qualification, delivery, performance, interpretation, delay, and displaced work for this receiving question. Use A.15.9 and C.11.DUA for that selection. | Request the bounded premise; the supplier keeps its Method and does not take over the recommendation or choice. A missing premise alone can remain a limitation. |
| Blocker | A missing, stale, incompatible, inadmissible or unauthorized premise prevents the requested responsible recommendation. Name the premise, affected use and what would resolve or reroute it. | State any still-usable partial result; do not convert uncertainty into either a confident negative or a positive recommendation. |
| Abstention | The recommendation premise itself fails, or the requested kind of advice cannot responsibly be supplied within the engagement. State the failed premise and the correct receiving account where one exists. | An abstention is not an adverse factual finding about the subject and is not abandonment of any obtaining professional duty. |

A mixed answer can be useful if its scopes are unmistakable: retain two directions and block a stronger ranking, with a comparison request only when selected for its attainable value. Do not present these as contradictory overall statuses.

The strength of each claim stays inside the narrowest material limit of the premises on which **that claim** depends. If one input supports only a particular AI configuration, the recommendation cannot silently extend it to another. If an unused source expires, it does not invalidate unrelated claims merely by appearing in the same bibliography.

When a total order is unwarranted, prefer an explicit partial answer to invented weights or probabilities. When the declared scheme does support one direction, do not conceal that conclusion behind an uninformative list. Explain why a serious remaining alternative loses for this use, and what would reverse that judgement.

#### PSDA.14:4.4 - Make the recommendation account inspectable at the smallest useful size

The account is a claim-bearing result, not a mandatory template or new record kind. A short message may carry it; a consequential institutional matter may need a larger package and protected annex. Keep the following content recoverable wherever it can change reliance.

| Position | Decision-useful content |
| --- | --- |
| Receiving frame | Recipient, recommending performer, holder or subject, question, horizon, choice owner, receiving decision and next Work. |
| Candidate domain | Considered alternatives, compared subset, exclusions with their basis, retained alternatives and any candidate gap. |
| Relied-on premises | Exact results and relevant source editions or dates, configurations, qualification windows, evidence limits and supplying owners. |
| Comparison and inference | Scheme, material trade-offs, protected conditions, robust regions or reversals, and the reasoning that supports the disposition. |
| Unresolved content | Material uncertainty, dissent, evidence losses, unsupported extensions and what each prevents. |
| Return | One or more explicitly scoped dispositions and the next consideration, request, reroute or separately governed choice they support. |
| Reconsideration | The source, observation, configuration, threshold, authority, horizon or candidate change that could alter a specified claim or disposition. |

Put the disposition and its most important limit first. Keep the evidence and reasoning reachable without requiring the recipient to reconstruct the entire analysis. Where a protected annex limits access, the accessible return must still state the resulting reliance restriction; it must not hide that a decisive premise is unavailable to the recipient.

A threshold in this account needs a source and an owner for its meaning. “Reconsider when recovery evidence no longer supports the continuity condition” is useful only if the named evidence, condition and receiving question can be recovered. `PSDA.15` designs how such evidence will be obtained and interpreted. If a positive recommendation depends on ongoing observation, an unassigned or infeasible observation obligation is a material limit now, not an administrative detail to repair after handoff.

#### PSDA.14:4.5 - Return the advice without taking the later choice

Make the result available to the actual recipient in a form suited to the agreed use. For a receiving-use question, apply `A.2.9`: what should the recipient understand or do, what evidence is enough to judge that, and what smallest repair or stop follows? Explaining the conditional nature of a ranking may be necessary; obtaining agreement with it is not the same task.

Keep the communicative Work, recommendation content, carrier, recipient response and later effect distinct. Delivery establishes neither understanding nor reliance, consent, choice, implementation or effectiveness. A recorded acknowledgement may support receipt; it does not establish an authorized decision. A communication can perform an authorization only under its own actual performer, authority and institutional conditions.

The authority-holding System may later choose, reject, retain alternatives, commission a probe or reroute under `C.11` or its direct domain rule. A corporate organ may consume the recommendation and unresolved disagreement through `CGOV.11`; that organ, not this account, performs the authorization Work. Do not require a corporate-governance framework where the actual decision is personal or otherwise outside its subject.

Returning the advice closes this recommendation application, including an honest stop branch. Later premise refresh and a newly composed recommendation are later work. Any promised professional contact, referral or service closure remains governed by the actual relationship; closing this application neither invents nor cancels those duties.

### PSDA.14:5 - Archetypal Grounding

The examples are hypothetical. Assumed specialist results illustrate the pattern; they assert no real public decision, client assessment or intervention effectiveness.

#### PSDA.14:5.1 - A pump comparison that cannot yet choose an investment

An East-District authority asks a separate analysis team for advice on flood-pump investment for the coming season. Its receiving decision is whether and how to commit funds. The live candidates include a baseline `N`, fixed pumping `F`, mobile pumping `M` and staged combination `S`.

The qualified numerical slice concerns pumping-service loss and incremental cost, not the whole public consequence. In the stated model, `F` has loss 2 in normal access and 3 with road loss, at cost 8; `M` has loss 1 and 9, at cost 5. The baseline and staged alternative are not closed by this two-option comparison. Reachable assistance, property consequences and protected conditions still require their direct evidence and value judgements.

A sensitivity result supplies the conditional boundary `7p > 1 + 3λ` for `F` to have the lower weighted loss, where `p` is the assumed road-loss probability and `λ` the declared cost weight in this illustrative model. Neither value has been established for the actual investment question. With `λ = 0.5`, `p = 0.2` favours `M`, while `p = 0.6` favours `F`. This is evidence of a possible reversal, not evidence that either probability obtains.

The team returns:

> Retain fixed and mobile pumping for the current pumping-service/cost comparison. A whole-investment recommendation is blocked by the unqualified road-access basis, unresolved assistance and protection consequences, and the unclosed baseline/staged branches. The current model favours different options under different declared assumptions; it does not justify a preferred investment. Reconsider the affected comparison when those results or the authority's value and protection premises change.

A material objection about reachable assistance remains in the return, not buried below the numerical result. The authority can decide what further evidence to commission under its own mandate. A bounded consequence/access request is a useful continuation when an obtainable result can improve the investment decision enough to warrant its acquisition burden. Neither that request nor the conditional comparison authorizes spending, a public trade-off or an operational response.

#### PSDA.14:5.2 - Development advice with a positive branch and an honest gap

A committee asks a separate advisory team which direction to consider for ninety-day service reliability. The holder is the service organization; the committee is recipient and, by the assumed mandate, choice owner. Internal development, an external provider and a mixed human–AI arrangement are live directions. Critical-service continuity, a security boundary and a bounded budget are protected.

An operations account, position/interface account and strategy priority are available, but none compares the whole obtaining arrangements. The first complete return retains the three directions for consideration and states that their whole-arrangement ranking is unsupported for this horizon and protected conditions. A published Method for obtaining a comparison is not the client-specific result. A comparison request follows only if its attainable contribution warrants the full acquisition burden; the unranked answer need not propose that work.

For a separately stated continuation, suppose qualified allocation and security results now cover all three directions. They support a bounded mixed-arrangement probe, retain internal development, and exclude this provider configuration under the security condition. The probe evidence question, feasibility, exposure and stop are supplied rather than invented. The adviser can then recommend considering that probe first while retaining internal development; throughput remains uncertain and the protected conditions remain binding. These new premises, not a change of wording, permit the stronger answer.

This continuation does not promote an earlier I/H-only comparison into full-set closure. A different provider, a materially different probe, or model configuration B needs its own qualification. If the mixed result covered only configuration A, advice about B retains that qualification gap or a blocker while independently qualified internal-development content can still be returned. The committee's later choice and probe WorkPlan are separate.

A material provider interest must be disclosed and treated under the engagement's conflict conditions before this positive advice is relied on. A sponsor wanting one supplier does not settle the holder's need or the committee's choice.

#### PSDA.14:5.3 - Unlike holders and ordinary non-use

For a person asking a separate adviser about four months of engineering-management development, suppose qualified accounts of current work show useful cross-discipline coordination experience, while an additional individual transfer study would consume much of the available horizon. The adviser can recommend considering a coordination direction within the person's accessible work and support, with uncertainty about the four-month capability gain. This is a substantive direction for consideration, not proof of intervention effect or independent transfer. A course attendance record alone would not support that advice. When current premises support two directions without ordering them, return that retained set and its distinguishing limit; the person's later choice remains theirs.

For an authorized team considering an AI scaffold or human–AI allocation, name the exact changed object, version, environment, evaluation validity, oversight and protected conditions. Use AI/security and, where relevant, organization-allocation results. A human learning study or a ranked recommender-system output does not establish those premises. If a known inadmissible configuration cannot meet the protected boundary, block that recommendation; if the evidence is merely absent, name the gap rather than claiming failure.

For a non-cultural population or lineage with no population-local recipient or chooser, abstain from attributing a recipient-owned development recommendation to it. Return population change to its evolutionary account. A separately authorized research team considering an intervention is a different recipient-owned case with scientific, safety and governance premises; naming that case establishes none of them.

For a chooser who already has an adequate option set and needs only to make their own decision, use direct domain or `C.11` guidance. Neither an adviser nor a PSDA return package needs to be invented.

### PSDA.14:6 - Bias-Annotation

A decisive-sounding answer can conceal uncertainty, but perpetual qualification can also conceal a warranted recommendation. Test both errors: what stronger claim is unsupported, and what useful claim is being withheld despite adequate premises?

Sponsor preference, provider interest and model convenience can shape the candidate domain before the recommendation is written. Inspect exclusions and unclosed branches, not just the displayed winner. Preserve material dissent without implying that every view has equal evidential support or that unanimity is required.

An available numerical score may dominate attention while a consent, continuity or access condition is left in prose. Keep non-compensable conditions visible at the point of disposition. Conversely, do not invent a protected condition from the adviser's personal preference.

### PSDA.14:7 - Conformance Checklist

**Recognition** asks whether recommendation composition is the missing result: a named recipient needs an answer that combines qualified premises, and the account can change their next consideration. A short supported answer with its necessary limit can close a small use; a selected request or exact blocker can also be useful.

**Assurance** asks whether this particular disposition is warranted for its intended reliance. Consequential uses add the direct domain's evidence, competence, independence, consent, safety, security, institutional and validation conditions; the size of the account does not lower them.

| Check | Sufficient answer |
| --- | --- |
| Receiving use | Recipient, subject, horizon, recommending performer, receiving decision/Work and separate choice boundary are recoverable. |
| Premise fit | Every decision-bearing input fits its actual configuration, window and use, or its gap and consequence are explicit. |
| Candidate and comparison coverage | The live set, compared subset, retained alternatives, exclusions, scheme and material reversals are visible. |
| Warrant | The inference supports the stated disposition without inventing preferences, probabilities, authority or supplier results. |
| Conditions and dissent | Material protection, disagreement, evidence loss and professional restrictions survive the return. |
| Use and reconsideration | The recipient can find the next use and exact reason to reconsider; required observation is feasible or named as a limit. |
| Result boundaries | Recommendation, communication, later choice, WorkPlan, implementation and effect have not been substituted for one another. |

If one check fails, repair or narrow the affected claim or return the honest stop. Request a missing result only when its obtainable contribution warrants acquisition. Do not erase independently usable content to make the account look uniform.

### PSDA.14:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Copy the highest score into “we recommend” | Recover the candidate domain, preference/evidence conditions and decision-support inference; retain a partial order when that is all they support. |
| Make a stronger recommendation by omitting an inconvenient branch | State the compared subset and the unclosed alternative or objection, with its effect on the answer. |
| Treat a specialist answer as the whole advice | Preserve supplier scope and compose only the inference that this recipient's question still needs. |
| Use a probe as the default answer to uncertainty | Name the decision-changing question, feasible evidence, exposure, delay and stop before recommending the probe. |
| Turn delivery or agreement into authorization | Obtain the later choice and authority evidence separately; repair understanding without seeking manufactured consent. |
| Offer a universal development prescription | Recover holder-specific premises; return the smallest gap where human, organization and AI evidence differ. |
| Hide a blocker behind a long report | Lead with what cannot yet be responsibly recommended and the exact result that could change it. |

### PSDA.14:9 - Consequences

The recipient gains a bounded answer that can be challenged, declined, acted on through the proper decision, or refreshed without reconstructing the entire engagement. Partial results and honest stops become usable outputs rather than signs that the analyst failed to choose.

The cost is explicit reasoning at the boundary between analysis and advice. Some requests cannot be closed with a single direction, and some attractive probes remain unsupported. This preserves the distinction between useful decision support and a persuasive but unwarranted prescription.

### PSDA.14:10 - Rationale

Recommendation composition has work left after generic evidence, comparison and choice guidance. Evidence can support a claim without determining what to advise; a comparison can leave alternatives unresolved; a choice rule belongs to the later decision. This pattern connects those qualified results to one recipient's question and makes the supported disposition intelligible.

The six return forms avoid two extremes: treating every uncertainty as failure, and treating every engagement as a duty to name a winner. They do not replace domain decision rules. The narrowest-material-premise rule applies claim by claim so that one failed branch neither contaminates unrelated advice nor disappears inside an overall positive answer.

### PSDA.14:11 - SoTA-Echoing

The practice question is **how to return useful advice from qualified analysis without manufacturing a complete order, professional competence or recipient choice**. The selected line combines explicit decision-analysis warrant with a source-bounded professional return. Its additional explanation costs effort; that cost is justified where a lost condition could change the next decision, and is reduced to a short return in a simple case.

| Question and selected move | Serious alternative, defect and changed locus | Source role, limit and reopen condition |
| --- | --- | --- |
| How does comparison become advice? **Adapt** structured preference-to-recommendation reasoning, preserving the actual problem and model conditions. | A single score is economical when a justified model covers the question. It fails when incomplete preferences or an unclosed candidate branch are silently filled in. Sections 4.2–4.4 require the scheme, inference and scope rather than banning scalar comparison. | [Greco, Słowiński and Wallenius (2025), *Fifty years of multiple criteria decision analysis*](https://doi.org/10.1016/j.ejor.2024.07.038), is a best-known-line synthesis of finite-action MCDA and different preference-to-recommendation procedures. It supplies neither this engagement's values nor universal superiority of one procedure. Reopen when a rival gives equally warranted advice with materially lower burden, or the finite-action/model assumptions cease to fit. |
| What must accompany technically supported organizational advice? **Adapt** explicit engagement, client involvement and conflict qualification. | A technically correct memo can suffice for a bounded analytical request. It is insufficient when reliance also depends on mandate or a material provider interest. Sections 4.1 and 5.2 keep those conditions with the advice. | [ICMCI v4.0 (2021), C.1.1–2, C.2.1 and E.3.5](https://www.cmc-global.org/sites/default/files/public/icmci_cmc002_competence_framework_version_4.0_1.pdf), is a substantive professional comparator, not a universal procedure or effectiveness study. Reopen on a changed applicable service rule or evidence that this qualification omits a material relationship condition. |
| What makes a human career return usable? **Adopt within that service** intelligible basis, consent and competent assessment use; retain referral where required. | Generic “best next course” advice is shorter but can conceal the person's receiving question and unsupported assessment. Sections 4.1, 4.5 and 5.3 retain these boundaries while leaving intervention and transfer evidence to their owners. | [NCDA Code of Ethics (2024), A.2, A.10 and E.1–2](https://www.ncda.org/aws/NCDA/asset_manager/get_file/3395), is a profession-specific normative comparator. It proves no learning effect and supplies no AI-holder assessment rule. Reopen when the actual service or applicable professional conditions change. |

### PSDA.14:12 - Relations

- `PSDA.11` supplies the bounded engagement question for the same subject and receiving decision. Its availability does not establish the particular mandate or impose temporal order.
- `PSDA.13` supplies material shared and contested claims. They inform the recommendation without settling the later choice.
- `PSDA.5`, `PSDA.6`, `PSDA.7`, `PSDA.8` supply the candidate, value, uncertainty and comparison results needed to interpret the advice. `PSDA.9` supplies robust regions, reversals and information priorities only where they can change this recommendation for the same configuration and horizon.
- `A.15.9` supplies qualified use and selection of worthwhile acquisition for external results; `A.10` governs their actual reliance. Holder practices retain facts, Methods, protected conditions and conclusion authority.
- `A.2.9` supplies receiving-use judgement and the distinction between communication and its institutional effects. `C.11` or the direct domain rule owns the later choice; WorkPlan, Work and effect remain separate.
- `PSDA.15` uses this recommendation to establish which later decision, consequences, signposts and premise changes matter. It obtains later authorized decision and implementation evidence as distinct results; this recommendation supplies neither.
- `CGOV.11` may use the recommendation and unresolved disagreement for the named corporate matter. Only the authority-holding System supplies the authorization Work.
- Missing, stale, out-of-scope or incompatible contributions call for an adequate qualified direct result or the exact missing-result return. A neighboring pattern, profile or source being available does not supply a performed result or require a complete language traversal.

### PSDA.14:End

## PSDA.15 - Arrange Decision Follow-up or Reassess Advice After a Change

> **Type:** Method pattern (DPF)
> **Status:** Stable
>
> **Primary working result:** a **follow-up arrangement** assigning needed observation and interpretation for a named recommendation or decision premise, or a **qualified current decision-support return** stating what remains usable, must narrow, is blocked, needs a named contributor reopened, or warrants a later recommendation.

### PSDA.15:1 - Problem frame

**Use this when** a recommendation or decision depends on conditions that may change, but nobody can yet say which observations matter, who will interpret them, or what result they should reopen. Also enter directly when a new source, configuration, observation or authority condition may have made existing advice stale.

A project may have a dashboard but no way to connect an alert to a particular assumption. An adviser may have promised to “check back” without establishing access to the receiving decision or its consequences. A revised AI evaluation may concern configuration B while the recommendation still relies on configuration A. In each case, more reporting alone does not close the gap.

Problem structuring and decision support is the wider practice. This pattern governs **follow-up of a structured decision and its supporting recommendation**. The regulated move is to design and use the connection from decision-significant observations to affected support results. Generic source currentness, domain operations, implementation control, strategy choice, professional service management and cultural continuation retain their own Methods.

The practical gain is a timely, bounded return: the advice still holds under stated conditions; a claim must narrow; a premise is missing; one contributor must revise its result; or a new recommendation is needed. The practitioner can preserve unaffected useful content without silently preserving an invalid whole.

**Do not use this pattern** when an existing adequate arrangement already covers the exact follow-up question and has no material change. Use it without redoing earlier framing or facilitation when the decision is already bounded and uncontested. Use the direct operation or emergency rule for an immediate operational response, and the direct currentness rule for a source-maintenance question that has no decision-support consequence.

### PSDA.15:2 - Problem

A recommendation, a later authorized decision, implementation and observed consequences are different results. Yet follow-up often treats the recommendation as evidence of what was chosen and treats a plan as evidence of what was done. A missing report then looks like “no change,” and any later improvement looks like success of the advice.

The reverse failure is indiscriminate reopening. Every source revision, new observation or changed model version causes the whole engagement to restart, even when only one candidate or consequence claim relied on the changed premise. Useful independent results are delayed while the actual gap remains poorly specified.

When future observations are needed, design their collection and interpretation around the claim they can change. When an existing change can already be assessed, return its claim-level effect directly. An observation arrangement needs an interpreting owner, a qualified receiving use, a timely route and an honest answer when access or evidence fails.

### PSDA.15:3 - Forces

| Force | Tension |
| --- | --- |
| Timely warning and observation burden | Frequent data may detect changes sooner, but collection, interpretation and response have costs and can overwhelm the receiving work. |
| Focused learning and unexpected change | A targeted test can resolve a decisive question while overlooking a new concern outside the original model. |
| Continuity and justified revision | Stable advice avoids needless churn; preserving a conclusion after its premise fails creates false confidence. |
| Shared follow-up and differentiated authority | One arrangement connects observers, specialists, advisers and choosers without giving them each other's powers. |
| Trigger clarity and uncertain evidence | An explicit condition helps action, but a noisy measure or an unqualified threshold cannot decide the response. |
| Service continuity and a bounded engagement | Follow-up may require real client contact or referral while the completed recommendation application remains complete. |

### PSDA.15:4 - Solution

Start with the follow-up question. For needed future observations, compare feasible arrangements and establish the necessary observation and interpretation work. For a current change, recover its effect on the affected claim and return the smallest warranted update through §§4.5–4.7. Preparation may begin before recommendation delivery; an already supported update does not require a new observation arrangement.

#### PSDA.15:4.1 - Recover the recommendation, decision and implementation separately

Name the receiving question, subject, horizon, recipient, choice owner, relevant alternatives, protected conditions and the recommendation's current disposition. An adequate `PSDA.14` result supplies what was advised and why. If it is unavailable, stale or outside the present use, recover a qualified direct account or state the exact gap.

Then ask what is actually known about the later decision. Obtain evidence of the authority-holding System's authorized decision from that System or a qualified direct source, under the direct authority and `A.2.9` conditions. Distinguish a choice to commission a study, a choice of an intervention, rejection of the advice, and no established decision. A recommendation or its receipt proves none of them.

Recover implementation and consequence evidence only to the extent the current question needs it. A WorkPlan establishes intended work, not performance. An implementation report must support what was actually done, under which configuration and interval; an observation must identify what was observed and its limits. Whether the advice or action caused an effect requires the direct causal evidence and guidance, not chronology alone.

A useful current return can therefore be: “The recommendation remains conditional; the receiving decision is not yet established; no implementation consequence is claimed.” Unknown decision status must not be silently converted into continuation of a selected action.

#### PSDA.15:4.2 - Name the premises and observations that can change the answer

For each material condition, connect the premise to the recommendation claim, compared alternative, model, protection condition or problem boundary that uses it. State what difference would change the current decision-support result and who can supply or interpret the needed evidence.

The observation may concern an expected consequence, an assumption, a new opportunity, a source's qualification, a participant's material objection, a protection breach or a changed authority condition. It need not be a numeric metric. A new affected group can reopen scope even while existing performance indicators remain favourable.

Use a small relation account such as the following; it is ordinary working content, not a prescribed register.

| Follow-up position | What must be recoverable |
| --- | --- |
| Current premise and receiving use | The exact claim, configuration, horizon and recommendation or decision-support result that relies on it. |
| Observation or source return | What evidence could test or change it, from which observation, supplier, participant or authoritative source. |
| Interpretation | Who can qualify the evidence, under what Method and uncertainty, and who judges its decision significance. |
| Signpost and reconsideration condition | The observable indication, the condition that makes reconsideration necessary, and the source of any threshold or protected limit. |
| Timing and access | When evidence is needed, delay in obtaining and interpreting it, access and disclosure conditions, and the effect of a missed observation. |
| Next result and owner | Which source, model, comparison, formulation or recommendation would change, and who retains the later choice or operational authority. |

A **signpost** is something watched because it can reveal a material change. A **reconsideration condition** states when that information requires a named question to be reopened. Neither is automatically a decision to change action. An operational rule may separately authorize a response to a defined signal; its authority and conditions must be established through that rule.

Choose timing from the consequence of late knowledge, not a universal calendar. If observation plus interpretation and authorized response would arrive after the relevant decision window, move the observation earlier, choose a feasible proxy with its limits, change the arrangement, or return that the promised follow-up is not adequate. Do not invent a threshold to make the table complete.

#### PSDA.15:4.3 - Generate and compare follow-up arrangements

Consider genuinely different ways to obtain a useful return. Possibilities include a recipient-owned scheduled review using existing evidence, a targeted specialist test before a commitment, event-driven notification with qualified interpretation, or a coupled arrangement combining targeted tests with a limited route for unexpected changes. A justified one-off return with no continuing service may be enough for a short, low-consequence use.

Compare coverage of the material questions, detection and interpretation delay, uncertainty, participation, observer independence where required, effort, confidentiality, cost, and the feasible receiving response. Do not maximize the number or frequency of indicators. A technically precise observation is of little use if no authorized or competent receiver can act on its meaning in time.

Targeted monitoring tests a named question; broader observation can reveal unexpected change. Their balance is a design choice for this decision. The distinction is supported by the current environmental decision-support discussion in [Manley, Povak, Reynolds and Hessburg (2026), Discussion / “Change is inevitable, learning is critical”](https://www.frontiersin.org/journals/forests-and-global-change/articles/10.3389/ffgc.2026.1783129/full); it supplies neither a universal monitoring mix nor an effect guarantee for other domains.

Use a `PSDA.17` conflict/facilitation-architecture result only if it constrains this design choice. For example, a material participant correction must reach the analyst before the comparison is used, or an observer cannot also carry an incompatible facilitation burden. The constraint does not choose the follow-up arrangement. Generate and compare alternatives that respect it; return to `PSDA.17` only when the underlying interference itself needs a different decision.

Use `A.22` when the selected organization of independently identified constituents and obtaining relations is itself the subject of a structure claim. A proposed arrangement remains a design description until the required participants, access, assignments and relations are established. A diagram or a filled table does not establish the arrangement, its adequacy or its work.

#### PSDA.15:4.4 - Establish a viable observation and return arrangement

Name who will observe, who will interpret, who receives the qualified result and who owns any resulting decision. Establish the assignments, capability, access, resources, timing and protection needed for those particular contributions. Several functions may be carried by one performer where suitable; distinguish them when competence, independence, workload or authority makes that difference material.

State what happens if the observer cannot obtain the evidence, the source becomes unavailable, the interpreting owner changes, or the evidence arrives too late. A failed observation is not a favourable observation. Return the gap and its effect on current reliance to the named receiver; use any existing authorized escalation or protection rule when it applies.

Where an actual professional service exists, fit contact, confidentiality, referral and closure to that service's conditions. The [NCDA 2024 Code, A.10 and B.1](https://www.ncda.org/aws/NCDA/asset_manager/get_file/3395), for example, constrains continuity and information sharing in career services; it creates no AI-holder duty or universal follow-up contract.

Before relying on the arrangement, test the decisive connection at proportionate cost: can an example material observation be obtained, qualified, delivered and understood as the named reopen question in time? A prospective walkthrough can expose an assignment or interpretation gap; it proves neither later enactment nor empirical effectiveness. Use stronger domain validation when the consequence requires it.

Record whether the result is a proposed arrangement with conditions, an established arrangement ready for its bounded use, or a blocker. Do not promise observation that has no capable performer or permitted source. State the closing or review condition for the arrangement so that a bounded recommendation does not create indefinite unowned monitoring.

#### PSDA.15:4.5 - Interpret actual observations before revising advice

When evidence arrives, first establish its subject, configuration, interval, provenance, Method, uncertainty and allowed use. A current source label alone is insufficient. Use `A.10` for the actual reliance. An adequate existing interpretation may support the answer; a missing one may limit or block it. Select a further specialist result through `A.15.9` and `C.11.DUA` only when its attainable contribution warrants the whole burden within the receiving window.

Compare the qualified evidence with the exact condition it was meant to test. Distinguish a change in the world, a changed source claim, an expired reliance window, a changed value judgement, a revised model and a merely changed representation. A diary review date is not by itself an expired reliance window. When meaning, applicability and access remain compatible, a repaired reference may finish the source update without renewed advice, multi-use search or another result record. A real expired reliance window or missing necessary observation still limits present use.

A source changing from A to B does not establish that advice about A is now valid for B. Preserve the earlier result for its earlier subject and conditions. Return the current use as unqualified when its basis is missing; obtain further qualification only when the needed stronger answer warrants that contribution. Similarly, failure to observe a threshold crossing proves nothing unless the observation coverage and sensitivity support that inference.

Keep the observations and their interpretation distinct from the next decision. If an authorized owner supplies a changed action decision, recover it separately. If the adviser concludes that a different action should be considered, that is renewed advice, not implementation control.

#### PSDA.15:4.6 - Return only the affected decision-support consequence

Trace the changed premise into the particular claim or disposition that relies on it. Preserve inspected independent results for their current conditions. If dependence or coverage remains unresolved, state that gap; do not label an uninspected branch unaffected.

| Current return | When it is warranted | What happens next |
| --- | --- | --- |
| Unchanged within stated conditions | Qualified evidence does not alter the relied-on premise, or the changed claim is outside the inspected use. | Retain that bounded advice and its current conditions. State the next observation only when an actual follow-up use needs it. This is not authority to continue an intervention. |
| Narrowed | A useful portion still has an adequate basis, but the previous scope, configuration, window or strength is no longer supported. | Return the surviving claim and the withdrawn scope explicitly. Do not relabel the narrowed result as the original whole. |
| Blocked for the affected use | A necessary premise, authority condition, observation or interpretation is unavailable or no longer adequate. | State what cannot responsibly be advised or relied on now, the missing basis and the receiver who can resolve or reroute it. Preserve separate usable content. |
| Reopen a named contributor | A needed stronger answer warrants an obtainable source, candidate, value, uncertainty, model, consequence, robustness or scope result, considering the complete acquisition burden. | Request that bounded result through its direct owner. The present qualified limit can close the earlier answer; a pending request is not the refreshed result. |
| Compose a later recommendation | Changed qualified premises require a different disposition or a newly composed answer to the receiving question. | Use `PSDA.14` with the current premises and remaining gaps. Preserve the earlier recommendation occurrence and the separate later choice. |

These are scoped conclusions, not a universal status system or a five-step lifecycle. One event can leave an internal-development claim unchanged, narrow a mixed-arrangement claim to configuration A, block advice about B, and reopen its evaluation supplier. Only the affected combined recommendation needs recomposition.

Keep **continue, adjust, refresh and reframe** precise. Continuing reliance on unchanged advice is a decision-support return. Adjusting a selected action requires the competent owner and its authorized decision, even if the original formulation remains adequate. Refreshing a model or evidence invokes its supplier and does not itself change action. Reframing reopens the problem or boundary through `PSDA.1` or `PSDA.2` when the old question no longer covers the material situation.

For one known reliance question, use `A.10` and the direct subject guidance. If a changed source requires discovering and revalidating several actual receiving uses, use `A.10.1` for its bounded search, coverage, direct-reliance test and subject-result return. That discovery preserves actual dependence and material gaps; equivalent irrelevant mentions can be grouped. The direct decision-support answer can finish without an additional common account unless a receiver needs that overview. Any no-impact claim still requires adequate coverage and support. Citation or adjacency is not dependence. Use `G.11` for currentness, decay and scoped refresh planning/reporting when that is the live result; neither pattern supplies a new domain conclusion or recipient choice.

#### PSDA.15:4.7 - Close the present return and preserve the next useful question

Return the observation, qualification, affected use and material limits needed by the current question. Name a next responsible receiver when further action is actually needed; a sufficient direct return creates no additional completion record. Preserve enough of the prior recommendation, decision and evidence to distinguish a later reassessment from a claim that the earlier Work was different.

Close when this bounded follow-up question has a supported answer or an explicit blocker and its receiving use is clear. Continue an obtaining observation or service arrangement only under its own scope and end condition. A completed recommendation application does not become an indefinitely unfinished application merely because later follow-up exists.

When follow-up evidence can change the decision-support Method repertoire, supply the bounded case, conditions, failure or useful variation to `PSDA.16`. Its owner still compares the repertoire and obtains its own result. One successful delivery, revised diagram or favourable outcome proves neither general Method effectiveness nor cultural continuation.

### PSDA.15:5 - Archetypal Grounding

The examples are hypothetical. Proposed arrangements, assumed authorizations, observations and qualified supplier returns are named separately to make their different effects inspectable.

#### PSDA.15:5.1 - Follow a blocked flood-pump recommendation without inventing a decision

The East-District analysis team has returned a conditional fixed/mobile pumping comparison and blocked a whole-investment recommendation. The road-access basis, reachable assistance and protection consequences, and baseline/staged branches remain unresolved. There is no established investment choice to “monitor.”

The follow-up question is which missing evidence can reach a renewed investment consideration before the coming season. A prior engagement-arrangement decision requires material participant corrections to reach the analyst before any comparison is treated as closed. The follow-up designer uses that constraint, not a prescribed meeting sequence.

Three arrangements are compared. An end-of-season review is inexpensive but too late for the receiving decision. Continuous pump telemetry gives frequent technical data but does not resolve deployment permission, affected residents' access or the unanalysed staged alternative. A bounded pre-decision evidence arrangement obtains targeted logistics and consequence results, admits material participant corrections through the facilitator, and gives the analyst an interpretation window before the authority next considers investment.

The third arrangement is selected in this illustration because the named logistics and consequence suppliers, facilitator and analyst have the required availability and access, and the authority's next consideration date is known. It costs a small additional interpretation meeting. If any decisive supplier cannot return in time, the arrangement reports that limitation and preserves the blocker; it does not quietly move the decision deadline or claim the authority has agreed.

In the continuation, the authority supplies qualified evidence that it has authorized an access study, not a pump purchase. The study's performer then returns evidence that the mobile deployment arrangement assumed in the earlier comparison is unavailable for the required flood-period window. The analyst does not substitute a guessed road-loss probability.

The current return is: preserve the earlier fixed-pump performance claim for its original conditions; narrow the earlier fixed/mobile comparison to the prior deployment basis; block its current investment use; reopen the exact mobile-deployment and consequence inputs. The assistance and staged-alternative gaps remain open. The authority's study decision is recorded separately from the unchanged absence of a qualified investment decision.

The arrangement also preserves a route for a newly identified affected group to raise a material access concern. That concern would reopen the boundary question rather than merely add another performance reading. No favourable pump metric can by itself close that question.

#### PSDA.15:5.2 - One changed AI configuration need not restart all advice

For a ninety-day reliability question, a committee received advice to consider a bounded mixed human–AI probe while retaining internal development. Assume the advice relied on qualified whole-arrangement, security and evaluation results for configuration A. A separate supplied decision shows that the committee authorized only a bounded probe under specified continuity and oversight conditions.

The follow-up designer compares a monthly report, an automated outcome stream without specialist interpretation, and configuration-change notification combined with a targeted probe-evidence review. The monthly option is too slow for the reversible-probe decision window. The stream alone cannot establish that a new scaffold or tool environment is covered by the previous evaluation. The combined option is selected only after the configuration owner, evaluation supplier, adviser and committee have the necessary notification, access, interpretation and receiving arrangements.

Now a configuration-change notice identifies B. That notice is evidence of a changed object, not evidence of B's quality. The probe observation covers B, while the relied-on evaluation still covers A. The response is deliberately split:

| Inspected use | Current consequence |
| --- | --- |
| Internal-development claim whose premises did not use A's evaluation or the changed allocation | Remains usable for its named service and horizon. |
| Earlier mixed-arrangement recommendation for A | Retained as the earlier conditional result; it is not qualification of B. |
| Advice to extend the probe or deploy B | Blocked pending the exact B evaluation, security and allocation premises that can change that advice. |
| Need for renewed comparison | Reopen only the suppliers and comparison claims that actually use the changed configuration; compose a later recommendation when their qualified returns support one. |

The configuration notice does not choose a fallback, stop a service or revoke a permission. If an existing authorized continuity or safety rule governs B, its competent owner applies it separately; otherwise the choice or authority gap is returned promptly. The adviser must not keep an apparently positive recommendation by treating silence from the evaluation supplier as approval.

The same locality works with a human development premise. If an employee's available practice time changes, requalify the affected intervention and transfer claim rather than rewriting unrelated organization or AI evidence. Applicable client-contact conditions may require a conversation, but that conversation does not itself establish transfer or consent to a different intervention.

#### PSDA.15:5.3 - Cheap use, missed observation and proper stop

A recipient has one short, reversible comparison whose evidence remains valid until a named review date. Existing assignments and access already provide the only observation that can change it. Retain that arrangement; no dashboard or recurring workshop is needed.

If the named observation is missed, the current answer is the scoped evidence gap and its effect on reliance, not “unchanged.” If the receiving decision has ended and no continuing evidence, service or protection obligation remains, close this follow-up use with its final qualified return. Do not manufacture ongoing monitoring.

A population without a population-local recipient or choice owner does not acquire either through a follow-up table. Preserve the abstention from that recommendation use. A research team's separately authorized intervention has its own decision, experimental Work and observation conditions.

### PSDA.15:6 - Bias-Annotation

Confirmation bias favours observing only the consequences that made the recommendation attractive. Include the discriminating failure and an affordable route for material unexpected change. Avoid turning this into exhaustive surveillance: the receiving decision and possible loss still bound effort and access.

Automation bias can make an alert look like an interpreted result or authorized command. Separate collection, qualification, judgement and decision even when software assists several of them. A human label alone also proves neither competence nor independence.

Outcome bias can rewrite the earlier advice as obviously correct or wrong after the event. Judge the earlier recommendation against its then-current premises and intended use; judge the later return against the changed evidence. A causal effectiveness claim remains a separate question.

### PSDA.15:7 - Conformance Checklist

**Recognition** asks whether an observation or changed premise can alter current decision support and whether the path to a useful return is missing. One existing adequate result or one clearly scoped gap can close a small case.

**Assurance** asks whether this arrangement can obtain and qualify the needed evidence in time, and whether the actual current return follows from it. Consequential uses require their direct observation, validation, competence, independence, protection and authority conditions. A prospective walkthrough tests design only; it does not replace evidence from enactment.

| Check | Sufficient answer |
| --- | --- |
| Distinct results | Recommendation, later authorized decision, intended work, implementation and observation are separately established or explicitly unknown. |
| Material observation | Each selected observation can change a named premise, claim, alternative, condition or boundary; any threshold has a qualified meaning. |
| Design choice | Feasible arrangements were compared by coverage, delay, burden and receiving use; a PSDA.17 constraint did not preselect the answer. |
| Viability | Observation, interpretation and return have the necessary performers, access, resources, timing, protection and failure route. |
| Current evidence | The actual evidence fits its subject, configuration, interval and intended use; absence or silence is not favourable evidence. |
| Local consequence | Unchanged, narrowed, blocked, reopened-contributor and later-recommendation conclusions name their exact affected scopes and gaps. |
| Authority and closure | Operational change and recipient choice retain their direct authority; the follow-up return has a bounded continuation or end condition. |

### PSDA.15:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Monitor implementation of what was merely recommended | Obtain the later decision and implementation evidence separately; state unknown status when they are absent. |
| Use an indicator list as the whole arrangement | Name its claim, interpreting owner, timing, receiving use and failure return. |
| Trigger an action automatically from a threshold | Establish the direct operational authority and response rule separately; otherwise return the qualified reconsideration question. |
| Rerun the whole engagement after every new version | Inspect changed claim content and actual reliance; preserve independently usable results and reopen only affected contributors. |
| Reuse an A-specific evaluation for configuration B | Retain the historical A result and obtain B's exact qualification. |
| Interpret a missed observation as no change | Return the gap and its consequence for reliance, with the responsible receiver. |
| Call later improvement proof that the advice worked | Obtain the direct causal or effectiveness result; chronology and satisfaction alone do not supply it. |
| Keep follow-up alive without an owner or end condition | Establish the actual service or observation obligation, or close with an honest bounded return. |

### PSDA.15:9 - Consequences

The practitioner can react to a meaningful change without losing every previous result. The recipient sees what remains usable, what is unknown, which contributor should respond and whether a new recommendation is needed. Later decisions and operational responses remain attributable to their real owners.

The arrangement costs observation and interpretation effort and can expose a limitation before action is taken: no feasible way exists to watch a condition on which the advice depends. That is a useful result. A positive recommendation cannot honestly promise protection through follow-up that cannot be performed.

### PSDA.15:10 - Rationale

The decision-support remainder is not generic monitoring or generic source refresh. It connects this recommendation's consequences, assumptions, alternatives, models, authority and problem boundary to a feasible observation-and-interpretation arrangement and a current advice return.

This connection must be designed before it is relied on, but design and use need not form a universal lifecycle. One changed observation can open the pattern directly. A proposal can stop at an infeasible observation condition; a later source can leave the answer unchanged; a changed boundary can require formulation work without first rerunning every calculation.

Locality is semantic rather than file-based. A shared file does not make all claims dependent, and separate documents do not make actually coupled claims independent. The stopping point is the last receiving question whose answer can change.

### PSDA.15:11 - SoTA-Echoing

The practice question is **how to keep decision support useful under change without confusing observation with decision or causing indiscriminate recomputation**. The selected line designs decision-linked evidence and interpretation, combines targeted and unexpected-change coverage where warranted, and returns only the affected question. The trade-off is explicit observation and interpretation effort; lower-burden arrangements remain preferable when they cover the actual use.

| Question and selected move | Serious alternative, defect and changed locus | Source role, limit and reopen condition |
| --- | --- | --- |
| What should cause reconsideration? **Adapt** named signposts and switch/reconsideration conditions tied to the actual decision. | A fixed periodic review is adequate for slowly changing, covered conditions; alone it can miss a consequential change before the next decision. Sections 4.2–4.6 connect evidence, timing and affected result without treating a signal as automatic authority. | [Lynch et al. (2025), *RAD switch points and triggers for adaptation planning*](https://www.usgs.gov/publications/rad-resist-accept-direct-switch-points-and-triggers-adaptation-planning), is a current domain line using three natural-resource cases for iterative reevaluation. It supplies no universal threshold, response or institution. Reopen when a better-supported rival or changed decision window defeats this observation design. |
| Should follow-up only test the predicted outcome? **Adapt** a proportionate combination of targeted questions and observation for unexpected change. | Targeted tests are efficient for a specified uncertainty; broad surveillance can expose unanticipated change but adds burden and weakly identified signals. Sections 4.2–4.3 and 5.1 compare the mix instead of prescribing either alone. | [Manley et al. (2026), *Meeting the moment*, Discussion / “Change is inevitable, learning is critical”](https://www.frontiersin.org/journals/forests-and-global-change/articles/10.3389/ffgc.2026.1783129/full), is a contemporary environmental decision-support perspective distinguishing these monitoring uses, not a comparative effectiveness trial. Reopen on representative evidence that another mix covers the material questions with less burden or delay. |
| Does a returned recommendation end every relationship obligation? **Adapt** bounded service continuation and closure while keeping renewed advice a later application. | Ending all contact at delivery may fit a one-off analytical request but not an obtaining service duty; indefinite monitoring creates the opposite failure. Sections 4.4 and 4.7 require the actual relationship and end condition. | [ICMCI v4.0, C.1.1–2](https://www.cmc-global.org/sites/default/files/public/icmci_cmc002_competence_framework_version_4.0_1.pdf), is a professional comparator for assignment closure. [NCDA 2024, A.10](https://www.ncda.org/aws/NCDA/asset_manager/get_file/3395), governs its own service continuity/referral. Neither establishes a universal contract. Reopen when the actual service or applicable duties change. |

### PSDA.15:12 - Relations

- `PSDA.14` supplies the recommendation's receiving decision, conditions, dissent, gaps and reopen basis. It supplies no evidence that the later decision or implementation occurred.
- `PSDA.17` supplies only a constraint that changes follow-up design. This pattern still generates and compares its own alternatives.
- `PSDA.1`, `PSDA.2` receive a materially changed formulation or boundary question; `PSDA.3` and `PSDA.5`, `PSDA.6`, `PSDA.7`, `PSDA.8`, `PSDA.9` receive only the affected model, candidate, value, uncertainty, consequence or robustness question. Availability does not imply that every contributor must run again.
- `A.10` qualifies one reliance use; `A.15.9` obtains a bounded external result; `A.10.1` discovers and revalidates affected receiving uses of a changed source when its several-use condition holds. `G.11` governs currentness and scoped refresh planning/reporting, not the new domain result.
- `A.22` governs a selected-structure claim when made. It does not establish the proposed arrangement, participant assignment, observation, decision or effectiveness from a representation.
- `A.2.9`, `C.11` and direct domain authority distinguish actual authorization, recipient choice and their records. `A.15.2` and `A.15.1` distinguish intended from performed Work; causal claims retain their direct evidence requirements.
- `PSDA.16` may use this bounded follow-up evidence when it can change a repertoire decision under the relevant conditions. Evidence neither authorizes nor entails the repertoire result.
- Strategy-direction follow-up, domain operations and professional service management retain their direct owners. A `STR.12` result may be considered only when its exact subject, claims, authority, evidence and effective conditions fit; no strategy framework is a blanket prerequisite.
- An unavailable, stale, out-of-scope or incompatible input requires a qualified direct result or the exact missing-result return. A profile, pattern body or available Method is not an actual observation or decision.

### PSDA.15:End

## PSDA.16 - Decide Whether and How to Change Problem-Structuring and Decision-Support Methods

> **Type:** Method pattern (DPF)
> **Status:** Stable
>
> **Primary working result:** a **current decision-support Method repertoire** for named recurring uses, with the ways offered or retained as candidates, their comparative reasons, applicability and evidence limits, cultural lineage, source-to-claim basis, and conditions for refresh or withdrawal from a particular use.

### PSDA.16:1 - Problem frame

**Use this when** a practice needs to decide which problem-structuring and decision-support Methods to retain, change or withdraw from its offering for future engagements. A familiar workshop no longer covers a recurring participation difficulty. A new analytical technique seems promising, but its input assumptions differ from those of the existing repertoire. Follow-up exposes a repeatedly broken join between a material correction and the recommendation that should use it.

Start with the recurring difficulty and the repertoire decision: which way should remain available for which situation, which proposed change deserves a trial, and which use should be narrowed or withdrawn? A better source or a qualified failure can justify a small change; the practice need not redesign its entire repertoire.

Problem structuring and decision support is the wider practice. This pattern governs **development and maintenance of its reusable ways of working**. A repertoire here is a bounded set of Methods and separately identified candidate accounts with usable conditions and reasons, not a catalogue of schools, a software inventory, a training curriculum or an assertion about the whole discipline.

The gain is a practical choice for the next engagement: a practitioner can recover what a Method does, where it fits, what evidence supports that use, what alternative remains, and when to ask for another result. A small repertoire can be better than a comprehensive list that hides unsupported transfers.

**Do not use this pattern** merely to choose an adequate existing Method for one engagement; use `PSDA.4`. Use `PSDA.15` to respond to a changed premise in one current recommendation, and `PSDA.17` for a conflict in the current work arrangement. Enter this pattern only when that evidence can affect the decision to retain or change a reusable Method, applicability claim or repertoire offering. Changing a document, tool, source locator or one local performance does not by itself create a new Method.

### PSDA.16:2 - Problem

Professional repertoires tend to harden around what their practitioners can already teach, facilitate or compute. New situations are then forced into the incumbent's assumptions: unclear values become invented weights, unequal participation becomes apparent agreement, and a dynamic uncertainty problem becomes one fixed scenario.

The opposite failure is uncontrolled combination. Each engagement adds another technique or software assistant, but nobody identifies the reusable action, the meaning of the joins, the evidence that transfers or the conditions that defeat it. The resulting collection is larger without being more useful.

Published applications and local successes can compound the problem. A reported use is evidence of that use, not proof of general superiority. A new edition may improve a description without changing a Method. A promising variant may deserve a trial without inheriting its parent's fit. The practitioner needs a repertoire-development decision that preserves these differences and still supports action.

### PSDA.16:3 - Forces

| Force | Tension |
| --- | --- |
| Professional continuity and change | Familiar ways preserve skill and comparability; an incumbent can also hide a recurring failure. |
| Plurality and usable choice | Several Methods may be warranted, but an undifferentiated list shifts all selection work to the next practitioner. |
| Generality and representative conditions | Reuse needs stable guidance; participation, power, values, evidence and authority vary across engagements. |
| Experiment and protected interests | Trials can improve practice, but participants and receiving decisions must not bear unbounded methodological risk. |
| Method and supporting arrangement | Tools, expertise and organizational conditions affect performance without necessarily changing the reusable way. |
| Lineage and present warrant | Provenance makes a variant recoverable; it does not establish fit, effectiveness or cultural uptake. |

### PSDA.16:4 - Solution

Develop the repertoire around recurring decision-support results and the conditions that make them possible. Recover the actual Methods, compare live alternatives, and retain or change the offering with its source and evidence return. Trial a consequential change only when further evidence can change that decision and its attainable contribution warrants the burden. These are dependencies in reasoning, not a compulsory lifecycle for every engagement.

#### PSDA.16:4.1 - Bound the repertoire question by the work it must serve

Name the practitioner group or service using the repertoire, the recurring situation, the receiving decision-support result, and the horizon over which the offering matters. The starting question might be: “How can our engagements preserve a late but material participant correction without losing the ability to produce a timely qualified recommendation?”

Recover only conditions that can change the answer: disputed or already formed question; participants and power; access to affected parties; values and protected conditions; alternatives; uncertainty; available evidence; technical and facilitation capability; decision authority; receiving Work; and follow-up need.

Use a `PSDA.15` result only when its evidence can change this repertoire decision under the relevant configuration and horizon. A changed mobile-deployment premise may show that the existing follow-up Method worked by returning the correct blocker. It does not by itself demonstrate a defective Method. If a supplied result is missing, stale or incompatible, use a qualified direct account or name the precise gap.

Distinguish a missing input, a failure to enact the stated Method, a support or capability problem, and a defect in the reusable way itself. A practice cannot repair absent stakeholder access simply by adding another modelling technique. Conversely, more training cannot repair a Method rule that systematically excludes the required correction.

Use C.39.RP when the offered repertoire and its missing contributions need construction, C.39.RQ when the situated requirements for a Method need to be made explicit, and C.11.MV when a Method option's worth is the unresolved comparison. Those Core Methods supply their general operations. The professional question here is which formulation, modelling, participation or return contribution can be offered under the actual engagement conditions, with the subject evidence and interpretation limits below.

#### PSDA.16:4.2 - Recover candidate ways of working and their contribution boundaries

State each serious candidate as a way of doing: its entry conditions, participant meanings, actions, input/result commitments, required joins, allowed variation, and stop. Use `A.3.1` for Method identification. Keep an unresolved proposal as a candidate account; an attractive name, complete document or parent Method does not admit it.

When several grounded occurrences or direct sources leave the reusable way genuinely unclear, `A.3.1.MR` can help recover candidate accounts. It is not the route for filling a missing design choice in a prospective recipe. Ask the designer to state the proposed action and its conditions.

Decompose a heavyweight school or package only far enough to compare contributions. The following contrasts are useful starting questions, not an exhaustive taxonomy or automatic assignment rule.

| Recurring difficulty | Contribution to recover | Condition that must not be silently supplied |
| --- | --- | --- |
| Participants formulate different problems | Ways to elicit, represent and challenge attributed interpretations; purposeful-activity or concern-mapping contributions where suitable. | Attendance or a shared map does not establish equal influence, representation or agreement. |
| Related decisions cannot be treated independently | Ways to expose connected choice areas, feasible combinations and commitments. | A diagram of dependencies does not establish feasibility or authorize commitments. |
| Values and trade-offs are incompletely stated | Ways to elicit value judgements and compare alternatives under the admitted preference information. | A preference model cannot create legitimate weights or permission to trade a protected condition. |
| Consequences depend on uncertain conditions | Qualified conditional modelling, uncertainty analysis, scenarios, robustness and information-priority work. | A scenario is not its probability; one robust region does not cover every model or value scheme. |
| Analysis does not become usable advice | Ways to compose and explain a source-bounded recommendation, dissent, limits and next use. | A score or specialist answer is not the whole recommendation or recipient choice. |
| Advice loses its basis after change | Ways to observe decision-significant conditions, interpret evidence and reopen the exact affected result. | A signpost, dashboard or missed observation is neither an authorized response nor evidence of no change. |

Soft Systems Methodology, SODA/cognitive mapping, Strategic Choice, MCDA, scenario and robust-decision approaches can contribute to different rows under their actual source conditions. A software platform may support several such contributions. None supplies a universal Method merely by appearing in the repertoire.

`PSDA.4` supplies the engagement-level comparison and combination discipline. Preserve its joins: an attributed concern may become a candidate objective for examination, not automatically a numerical weight; a scenario may constrain a calculation without supplying a probability. If a proposed whole cannot recover its reusable action and joins, retain the bounded candidate or arrangement description rather than calling co-use a composite Method.

#### PSDA.16:4.3 - Compare the incumbent with a serious alternative before designing a variant

Name the current offering, a plausible competing Method, and a bounded adaptation or combination only where each is live. Compare them against the same recurring result and the actual conditions, at comparable effort where possible.

Ask what each lets participants and practitioners do, what it leaves unresolved, and where it fails. In addition to analytical adequacy, consider meaningful challenge, unequal power, facilitation burden, interpretation skill, source qualification, time to a usable return and cost of maintaining the offering. State a deliberately accepted trade-off when the richer result costs more.

Do not infer that one Method is universally better because it produces a precise score, a satisfying workshop or more alternatives. A single well-qualified Method can remain the best offering for a narrow use. Plural formulations can be necessary elsewhere; a numerical comparison can still be necessary after them.

When a change is needed, state its mechanism: which reusable action, input condition, dependency, decision rule or stop changes, what remains, and why that difference could repair the failure. Distinguish this from a change in wording, display, software, local staffing or performance. The latter may require maintenance or a new fit check without identifying another Method.

For example, replacing a paper map with a digital map while preserving attribution, challenge and unresolved-claim rules may change support and access. Replacing the challenge rule with automatic aggregation of all statements changes the reusable way and can lose dissent. The same interface change can therefore have different repertoire consequences depending on what practitioners actually do.

Use current `A.3.1.MV` guidance when generic variant identity, derivation or non-variant maintenance is the live subquestion and its exact claims fit. The remaining PSDA question is whether that way serves the professional decision-support use: how interpretation, participation, values, uncertainty, authority and follow-up contribute to a usable return. Generic variant maintenance does not answer that field judgement.

#### PSDA.16:4.4 - Build a source-to-claim basis, not a popularity ranking

For every repertoire claim that can change later use, retain the source contribution and its actual limit. An instruction can describe a Method; a reported application can show that it was used; an observed interaction can illuminate a failure mechanism; a comparative study can support a bounded advantage. These are not interchangeable evidence.

A useful basis line says: **this source or qualified experience supports this action or applicability claim for these conditions; this uncertainty remains; this new observation would change the offering**. Include source edition, relevant locus, evidence window and original meaning where they matter. Recover contrary cases and the serious alternative, not only supportive citations.

The [2019 Smith and Shaw review](https://doi.org/10.1016/j.ejor.2018.05.003) provides an exploratory way to compare PSM characteristics; its classification is not an exhaustive admission rule. [Kogetsidis's 2025 application review](https://doi.org/10.1108/IJOA-08-2024-4746) and [2026 online review of Europe and beyond](https://doi.org/10.1108/EMJB-06-2025-0214) provide leads about reported applications. Their journal and search boundaries limit what they establish about practice outside that corpus. Do not rank Methods by the number or location of publications.

A recent decision-analysis synthesis such as [Borgonovo et al. (2026)](https://doi.org/10.1016/j.ejor.2025.05.023) can identify developments in value-focused thinking, graphical modelling, uncertainty, sensitivity and information acquisition. It does not substitute for the source of a particular Method or cover every adjacent decision-support family.

Obtain missing source interpretation, domain evidence or representative evaluation through `A.15.9`, preserving supplier authority, and qualify actual reliance through `A.10`. If the decisive source contribution cannot be recovered, keep that offering conditional or return the source gap. Neither a famous school nor a new source date repairs the missing claim.

#### PSDA.16:4.5 - Trial the claimed improvement in representative engagements

For a selected trial, turn the proposed improvement into a question that can fail. Specify the Method or status-preserved candidate, the situation represented, participant and power conditions, required capability and support, the serious comparator, the expected result, the burden accepted, and the observation that would retain, narrow or reject the proposal.

Select evidence proportionate to the claim. A walkthrough can expose an impossible join. A constructed exercise can test whether practitioners preserve an objection through a calculation. An authorized field trial can test feasibility and use in a real engagement. Broader transfer or causal-effectiveness claims need stronger and appropriately designed evidence. Do not generalize the last two from the first two.

Observe the working mechanism as well as the output: who could contribute or challenge; which material statement entered the model; where meaning changed; what was withheld; how uncertainty and protected conditions reached the recommendation; and whether the receiver could use it. The distinction between technically valid models and what people do with them is central to [Franco et al.'s behavioural OR review (2021)](https://doi.org/10.1016/j.ejor.2020.11.031). It supports attention to intervention configuration and interaction, not one universal trial design.

Preserve competing explanations. Better results may reflect a more skilled facilitator, a different participant group, more time, an easier problem or changed support rather than the Method difference. Where those cannot be separated, report what the trial establishes and what remains unresolved; a useful feasibility result need not pretend to be a causal result.

Do not use a consequential live decision as an uncontrolled Method experiment. Establish the authority, consent, protection, observation and fallback conditions appropriate to the engagement. A prospective candidate can be investigated through a separate trial arrangement without claiming that an unadmitted candidate whole has already been enacted as a `U.Method`.

Retain disconfirming results. A richer Method that cannot run within the actual access or competence conditions may be a poor offering for that use even when its idealized output is better. Conversely, a failed local performance does not disprove the Method when a required condition was absent; it may instead defeat the offered applicability claim.

#### PSDA.16:4.6 - Return a small current repertoire with differentiated dispositions

Decide what the practice can now offer, for which use and with which limits. Useful dispositions include retaining an established offering; narrowing its applicability; adding a separately identified variant for a qualified use; retaining a proposal for a bounded trial; requesting missing evidence; and withdrawing an offering from one use while preserving its history.

Keep identification separate from validation. An independently identified Method may still have unproved practical fit. A candidate account may have useful trial evidence without yet resolving its Method identity. State both rather than using one maturity label for every question.

For each action-changing entry, make the following recoverable in the simplest form that serves its next user.

| Repertoire position | Content needed for use |
| --- | --- |
| Recurring situation and receiving result | Who uses the offering, what difficulty it addresses, which result it provides, and the conditions that matter. |
| Method or candidate | Exact reusable action and status; entry, joins, allowed variation and stop; where the full description can be obtained. |
| Comparative reason | Incumbent or serious alternative, the gained capability or repaired failure, and the accepted effort or other loss. |
| Evidence and source basis | Claim-sized sources and relevant trials, their configurations and limits, defeating evidence and the next unresolved question. |
| Lineage | The actual source way or candidate, preserved and changed semantics, and the evidence for derivation; cultural links only where established. |
| Current offering | What is available for this use, conditional, retained for trial, narrowed or withdrawn; required performer/support conditions and source responsibility. |
| Refresh and exit | Which changed claim, failed condition or receiving need would reopen this entry, and what remains usable elsewhere. |

A repertoire may retain alternatives without ranking them. When the actual question is declaring a selector-facing set result over already identified members, use `G.5` with the exact members, outcome, ordering and basis it requires. Distinguish alternatives retained for later choice from members all included in one named joint use. A Method-family registry or selector declaration supplies neither field fit nor actual enactment and need not be rebuilt for every repertoire update.

Make the next use easy to find: which Method a practitioner should inspect for the named situation, which claim still needs evidence, or which use has been withdrawn. A large source map that gives none of these is not the promised repertoire.

#### PSDA.16:4.7 - Preserve cultural lineage without inventing cultural continuation

Record where a reusable change came from when that relation matters: an identified source Method, a documented adaptation, a changed stopping rule, a taught practice, or another qualified source. Similar names, chronological succession and a shared diagram do not establish derivation.

Keep proposed derivation, observed local enactment, transmission to another practitioner, recognition, selection, retention and loss distinct. A source publication can make a description available without proving that anyone learned or enacted the Method. A successful trial can justify a restricted offering without showing that a professional community adopted it.

Use `C.36` for an actual cultural-evolution question. Supply `PSDA.18` with the repertoire's qualified variant or local evidence only when it matters to that cultural-continuation decision. Name the practitioner population, engagement/community, place and period that the evidence actually covers, and mark the unobserved links. The receiving cultural decision is not entailed or authorized by the repertoire.

This boundary applies equally to new software support and AI-assisted practice. A tool release is not cultural uptake; widespread use of a tool is not evidence that the same Method was enacted by everyone. Teaching, service change and deliberate cultural intervention require their own work and authority.

#### PSDA.16:4.8 - Refresh the affected offering and preserve an honest stop

Maintain a responsible source and use return for the current repertoire. Reopen an entry when new evidence, a source claim, changed Method semantics, participation or authority conditions, support, qualification window or receiving need can change its offering. A new publication date or a file rename alone is not such a change.

For a changed claim, identify its exact repertoire use and the consequence: preserved, narrowed, reopened for a new trial or source result, or withdrawn from that use. Preserve independent entries and the earlier evidence for its original conditions. If applicability remains unresolved, state the uncertainty rather than assigning an unsupported negative or positive status.

A changed service rule might restrict the human career-advising branch without changing organization or AI-domain truth. A new AI configuration may invalidate evidence for a software-assisted offering without changing the manual Method. If the reusable decision-support action itself changes, identify and assess that semantic change rather than hiding it as maintenance.

Use `A.10` for a known bounded reliance, and `A.10.1` when a changed source requires discovering and revalidating several actual receiving uses. Invoke `G.11` for an admitted currentness or refresh-planning/reporting object when its conditions obtain, such as a relied-on evidence or selected set; it does not supply the new repertoire judgement or make every local entry a refresh-orchestration problem.

Close this repertoire question when the relevant offerings, conditions, source/evidence gaps and next uses are clear. Withdraw only the defeated use, not recoverable history or other supported uses. A still-unqualified new proposal can remain visible without being offered as established practice.

### PSDA.16:5 - Archetypal Grounding

The cases are hypothetical. They distinguish source description, proposed Method change, constructed trial, qualified offering and later cultural evidence; they assert no actual practice-wide improvement.

#### PSDA.16:5.1 - A late correction changes an offering, not the whole school

A public decision-support practice serves flood-investment engagements. It maintains an identified one-session inquiry Method: elicit and attribute concerns, compare the admitted alternatives with qualified inputs, record material dissent, and close the session with a bounded return. The Method presumes that all decision-bearing contributions needed for that return are available within the session. The practice has nevertheless offered it as the sole inquiry option for these engagements, including ones in which necessary input can arrive later.

The `PSDA.15` pump follow-up case supplies a changed mobile-deployment premise and the resulting blocker. That alone is not a Method defect: the follow-up correctly prevented an unsupported investment use. The practice retains that evidence at its actual scope.

A separate examination of the one-session offering finds the action-changing mismatch. Engagements in this service can receive a qualified access correction after the meeting, while the reusable closing rule provides no way to bring it into the same pending recommendation. The practice must not advertise that offering as sufficient for such engagements.

Three alternatives are considered. Keep the one-session Method but restrict it to uses with the necessary inputs already available; defer the whole engagement until every possible input arrives; or construct a bounded correction-and-return variant that keeps attribution and conditional analysis, permits a material qualified correction before the receiving recommendation closes, and reopens only the affected comparison.

The third proposal changes a reusable join and closing condition, not merely the calendar. Its candidate account records the parent, retained actions, changed rule, required facilitator/analyst availability and stop when a late contribution cannot be qualified in time. Independent Method identification remains separate from evidence of practical fit.

The practice runs a constructed exercise, not a public investment experiment. Both the incumbent and proposed rule are examined on the same two realistic situations: all required inputs available at the meeting, and a material access correction arriving afterward. Participants' access, analyst time and the receiving deadline are made explicit. The test is whether the correction changes the exact affected comparison while preserving dissent and independent usable claims.

In the illustration, the incumbent gives an adequate bounded return in the first situation but leaves the second correction outside its closed result. The proposed rule preserves the correction and exposes its unresolved consequence in the second situation, at the cost of a further qualified return and analyst/facilitator time. This exercise supports the proposed join's feasibility under those conditions, not superior public decisions or transfer to all engagements.

The repertoire result is deliberately differentiated:

| Offering | Current use and limit |
| --- | --- |
| Existing one-session Method | Retained for the stated input-ready situation. Its broader late-input offering is withdrawn; the Method and other evidence are not erased. |
| Correction-and-return proposal | Retained as a candidate for a protected field trial; its intended join and observed exercise behaviour are recoverable. Any Method identification and field-fit conclusion must be established separately. |
| Wait for every possible input | Not selected for this service's present question because its unbounded delay defeats a timely qualified return; a named indispensable missing input can still require waiting or a blocker. |

No pump is chosen. The staged alternative and assistance/protection questions in the original investment case remain with their direct owners. The repertoire entry does not claim that other practitioners have received, enacted or retained the proposed variant; those cultural links remain unproved.

#### PSDA.16:5.2 - Non-contested development advice and a new software assistant

An advisory service already supports formed development questions without a dispute workshop. Its repertoire includes a source-bounded recommendation Method: recover the recipient, holder and horizon; inspect qualified specialist results; compare only live alternatives under the declared scheme; return a warranted direction, retained set, probe, request, blocker or abstention; and keep the recipient's choice separate.

A new drafting assistant formats the same qualified premises and flags missing fields. If the adviser still performs the same qualification, comparison and return, the changed object is support. The practice checks access, confidentiality, capability and output reliability for that support; it does not create a new Method merely because the model version changed.

A different proposal lets the assistant select a preferred development direction from its own generated ranking and omit unranked candidates. That changes the reusable comparison and stopping rule. The practice cannot import the manual Method's evidence or call the proposal a harmless implementation detail.

The immediate repertoire decision is to retain the manual offering and withhold the stronger automated offering pending an exact candidate account, comparison basis and representative evidence. A useful trial must include an absent whole-arrangement result, an unclosed provider alternative, and an evaluation that covers configuration A while the request concerns B. Success means the return preserves the correct gap and independently useful content, not merely that the text is fluent or shorter.

The trial also has to cover the actual human professional-service conditions where present. Human career-assessment evidence does not establish an AI-holder result, and an organization's allocation evidence does not establish a person's learning transfer. No generic development-direction score bridges those differences.

This is repertoire work, not a recommendation for a particular client, authorization to deploy the assistant, or proof of the full opportunity-construction Method. A human or organizational recipient still makes its own later choice.

#### PSDA.16:5.3 - A source update and a cheap non-use

A new version of a relied-on methodological source changes the conditions under which a comparison procedure may be used. The practice identifies the exact applicability claim in its repertoire. The supported entry for complete input data remains; the incomplete-data branch is narrowed and its source question reopened. Other Methods that do not use that claim remain unchanged.

If the new source only changes layout or a locator while preserving the relied-on claims, update that description or access information under its direct guidance. If one current engagement simply needs an adequate existing Method, stop repertoire development and use `PSDA.4`. Neither situation warrants a new professional Method.

A review reporting more published applications can justify looking for a promising candidate or an unexamined domain. It does not by itself change a local offering's evidence or justify retiring a less frequently published Method.

### PSDA.16:6 - Bias-Annotation

School loyalty and novelty bias pull in opposite directions. Compare the strongest applicable incumbent and the smallest useful new proposal; do not protect either by choosing an easy example. A practice's available expertise is a real constraint, but it is not evidence that other Methods lack value.

Publication and success-reporting bias can hide failed, unpublished or culturally distant uses. Preserve the source search boundary and distinguish reported applications from representative evidence. A corpus dominated by particular journals cannot establish the absence of a practice elsewhere.

Combination bias treats more techniques as richer support. Inspect the meaning and cost of the joins. Automation bias treats a change in software as either automatically new or automatically harmless; recover whether reusable actions and stops actually changed.

### PSDA.16:7 - Conformance Checklist

**Recognition** asks whether the missing result is a reusable repertoire offering rather than an engagement choice, one source update, a support repair or a current follow-up response. One corrected applicability line can be the complete useful result.

**Assurance** asks whether the offered Method or candidate and its claimed use are warranted by the actual source and trial evidence. A description can identify a way without proving fit; a constructed exercise can support feasibility without proving real-world effectiveness or transfer. Consequential trials and offerings retain their direct participant, competence, independence, safety, confidentiality and authority conditions.

| Check | Sufficient answer |
| --- | --- |
| Recurring use | Practitioner, situation, receiving result, material conditions and repertoire decision are bounded. |
| Method recovery | Actual reusable actions, joins and stops are recoverable; Method, candidate, description, support and local Work remain distinct. |
| Comparative development | A serious alternative and the changed mechanism or applicability claim are explicit, with effort and losses. |
| Source and evidence | Each action-changing offering has a claim-sized basis, qualification limits, contrary evidence and an honest gap where needed. |
| Trial claim | The comparator and representative conditions fit the claim; observation, feasibility, fit, causal effect and transfer are not conflated. |
| Current offering | Retained, narrowed, candidate, withheld or withdrawn uses are usable by the next practitioner and do not hide different outcomes. |
| Lineage and refresh | Derivation has a basis; unproved cultural links remain gaps; only affected offerings reopen and recoverable history remains. |

A failed check may narrow one offering or retain a candidate for investigation while other entries stay usable. Do not label the whole repertoire current merely because every row has a source link.

### PSDA.16:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Treat one school as the permanent professional answer | Compare the actual contribution and assumptions against the recurring use and a serious alternative. |
| Turn every successful engagement into a new Method | Separate reusable semantics, one performance, support and applicability evidence. |
| Copy parent evidence to a hybrid | Identify the changed joins and trial the new claim under its own conditions. |
| Count papers, downloads or satisfied participants as general effectiveness | State what was observed and the source boundary; obtain the evidence needed for the stronger claim. |
| Offer a candidate as established because it has a complete description | Keep Method identification, trial status and fit claims separate. |
| Use participant agreement as proof that power and dissent were handled | Examine who could challenge, whose concerns entered the result, and what material disagreement remains. |
| Retire every entry after a source or tool update | Trace the changed claim to its actual offering and preserve independent uses. |
| Treat a repertoire or publication as cultural continuation | Establish transmission, receiving enactment, recognition, selection, retention or loss separately. |

### PSDA.16:9 - Consequences

Future engagements gain a smaller, more discriminating starting point. Practitioners can reuse a Method for a supported situation, select an alternative, ask for a missing input or decline an unsupported extension. Changes become recoverable improvements or bounded experiments rather than accumulating workshop tricks.

The cost is maintaining meaningful applicability and evidence, not just names and editions. Some promising candidates remain unoffered, some broad claims narrow, and some local successes support only the conditions observed. That restraint leaves room for development without presenting uncertainty as established practice.

### PSDA.16:10 - Rationale

The repertoire decision remains after Method identity, generic comparison, variant maintenance and set declaration have done their work. It asks which professional ways can help this practice structure problems and support decisions under actual participation, value, evidence, authority and follow-up conditions.

This is different from choosing a Method once. A future-use offering must preserve enough source, evidence, lineage and limits to survive transfer to another practitioner or engagement. It is also different from changing a culture: making a variant available does not establish the relations through which a community learns, enacts or retains it.

A changed premise can vindicate the incumbent's stop rather than defeat the Method. That is why development starts with the recurring failure or opportunity and the affected claim, not the mere fact that a recommendation changed.

### PSDA.16:11 - SoTA-Echoing

The practice question is **how to develop a usable professional repertoire under heterogeneous situations and uneven evidence without turning either an incumbent school or each new technique into a universal answer**. The selected line is contribution-first comparison, explicit assumptions and joins, representative testing of the claimed change, and local source/evidence refresh. It accepts the cost of maintaining differentiated offerings; a simple established Method remains preferable when it covers the use at lower effort.

| Question and selected move | Serious alternative, defect and changed locus | Source role, limit and reopen condition |
| --- | --- | --- |
| How should unlike problem-structuring approaches enter the repertoire? **Adapt** explicit comparison of assumptions and contributions, with open family boundaries. | A familiar three-school catalogue is cheap to teach but hides differences that change participation and result use. Sections 4.1–4.3 compare the contribution rather than require a fixed membership list. | [Smith and Shaw (2019)](https://doi.org/10.1016/j.ejor.2018.05.003) is an exploratory conceptual comparator; [Kogetsidis (2025)](https://doi.org/10.1108/IJOA-08-2024-4746) is a later published-application line. Neither ranks Methods for this service. Reopen if a stronger account changes a load-bearing boundary or a representative case defeats the assumed fit. |
| Can current uptake evidence decide what to offer? **Reject that inference alone; adapt** reported applications as leads for candidates and source return. | A publication-frequency rule is inexpensive but confounds search coverage and visibility with practitioner use or worth. Sections 4.4, 4.7 and 5.3 preserve those distinctions. | [Kogetsidis (2026 online), Europe and beyond](https://doi.org/10.1108/EMJB-06-2025-0214), examines selected journals over 2010–2024. It is a current corpus-based comparator, not a census of practice or comparative effectiveness test. Reopen when new representative evidence changes the particular offering, not simply when another paper appears. |
| How should analytical advances change the repertoire? **Adapt** the specific value, model, uncertainty, sensitivity or information contribution needed by the use. | Adopting an entire analytical process can preserve coherence when its assumptions hold; importing it wholesale can require missing values, probability or evidence. Sections 4.2–4.4 retain exact inputs and joins. | [Borgonovo et al. (2026), decision analysis in OR](https://doi.org/10.1016/j.ejor.2025.05.023), is a contemporary synthesis of these contributions, explicitly not exhaustive of adjacent fields. It is not a Method-fit result for an engagement. Reopen on a materially better-supported analytical contribution or a failed input/return assumption. |
| What evidence warrants a Method improvement? **Adapt** examination of intervention configuration, interaction and outcomes at the claim's grain. | A technically valid output or favourable post-workshop rating is cheap to obtain but cannot alone identify the changed mechanism, comparative benefit or transfer. Sections 4.5 and 5.1 preserve trial type, comparator and confounding conditions. | [Franco et al. (2021), *Taking stock of behavioural OR*](https://doi.org/10.1016/j.ejor.2020.11.031), synthesizes different intervention-study questions and designs. It supplies no universal causal estimate or trial recipe. Reopen when a stronger representative design or counterexample changes the evidence required for the offering. |

### PSDA.16:12 - Relations

- `PSDA.15` supplies bounded follow-up evidence only when it can change the repertoire decision under the same relevant conditions and horizon. A local observation neither entails nor authorizes the repertoire result.
- `PSDA.4` chooses and combines Methods for an engagement; this pattern develops and maintains the reusable offerings and their limits. It does not require a new repertoire cycle before every selection.
- `PSDA.13`, `PSDA.5`, `PSDA.6`, `PSDA.7`, `PSDA.8`, `PSDA.9`, `PSDA.14`, `PSDA.15` and `PSDA.17` expose participation, alternative, comparison, recommendation, follow-up and arrangement requirements that a Method offering may need to preserve. Their available descriptions are not evidence of this particular Method's enactment or effectiveness.
- `A.3.1` governs Method identification; `A.3.1.MR` supplies candidate recovery only under its actual source/occurrence conditions; `A.3.2` governs a MethodDescription rather than admitting every multi-Method package.
- `A.3.1.MV` can supply qualified generic variant, derivation and non-variant maintenance guidance. Resemblance or shared repertoire vocabulary does not by itself establish a formal Method-specialization relation.
- `A.10` and `A.15.9` qualify and obtain exact source or specialist results. `A.10.1` and `G.11` apply to their respective affected-use and currentness questions, not as substitutes for the field repertoire decision.
- `G.5` declares a selector-facing result when that claim is live over identified members and grounds; it supplies neither a universal Method-family classification nor professional fit.
- `C.36` governs the cultural relation claims. `PSDA.18` uses this repertoire as evidence or a variant for a separately bounded cultural decision; missing generation, transmission, receiving-enactment, recognition, selection, retention and loss links remain unproved.
- An unavailable, stale, out-of-scope or incompatible input calls for a qualified direct source or the exact gap. No sibling DPF, whole-language traversal or unperformed specialist result is implied by adjacency.

### PSDA.16:End

## PSDA.17 - Reconcile Simultaneous Problem-Structuring and Decision-Support Work

> **Type:** Method pattern (DPF)
> **Status:** Stable
>
> **Primary working result:** one **bounded conflict and facilitation-architecture decision**: which arrangement of inquiry, modelling, participation and decision return will be used for the named engagement, why it addresses the material interference, what burden or unresolved conflict remains, and what would reopen it.

### PSDA.17:1 - Problem frame

**Use this when** useful activities in a decision-support engagement obstruct one another. An analyst needs stable assumptions while participants are still correcting the question. A facilitator cannot both handle a consequential objection and rebuild the displayed model. An evidence team qualifies one configuration while the advice recipient changes the configuration to be considered.

Start with the result at risk and the interference: “If we close this comparison now, this still-material contribution cannot enter it.” Recover only the relationships needed to understand that conflict, compare genuinely different arrangements, and decide the smallest warranted change within the applicable remit.

Problem structuring and decision support is the wider practice. This pattern governs a narrower subject: **the arrangement through which a named engagement's different kinds of work contribute to its result**. Here *facilitation architecture* means that arrangement of participation, modelling, inquiry, challenge and return—not a workshop agenda or a new institutional hierarchy. A diagram describes the arrangement; a reusable Method guides action; actual work enacts it.

The gain is a usable local decision without losing the value, evidence, participation or authority condition that made the conflict consequential. The result may retain the present arrangement with a stated limit, change it, or return the exact blocker to a competent owner. “Reconcile” does not require everyone to agree.

**Do not use this pattern** merely because two activities overlap in time. If they have no decision-relevant interference, continue them. Use `PSDA.4` when the question is which Method fits, and `PSDA.13` when a claim needs facilitated inquiry but the arrangement itself remains workable. Routine scheduling, specialist mediation, emergency command and decisions about the affected System retain their own Methods and authority.

### PSDA.17:2 - Problem

A sensible script can conceal an unsound engagement. Its “elicit, model, compare, recommend” order says little about people correcting claims during modelling, technical evidence arriving during discussion, or a sponsor controlling both participation and the receiving decision.

The same display can also carry incompatible readings. A causal sketch supports exploration; a calculation supports a bounded consequence claim; the closing slide appears to authorize action. If their different uses are hidden, completing the slide can look like completing all three results.

Local repairs then export the difficulty. Moving inquiry outside the meeting frees analytical time but adds participation effort and delays correction. Adding a challenger can broaden discussion while reducing facilitation capacity. Freezing a model stabilizes computation while excluding a changed premise. The practitioner needs to expose and decide these consequences, not merely draw a cleaner sequence.

### PSDA.17:3 - Forces

| Force | Tension |
| --- | --- |
| Closure and correction | A recipient needs a timely return, while new evidence or a material concern can invalidate part of it. |
| Analytical focus and participation | Detailed modelling needs concentrated effort; meaningful challenge needs attention when the interpretation is being formed. |
| Joint work and differentiated contributions | Working together can reveal important connections, while facilitation, technical judgement and choice have different conditions. |
| Local gain and transferred burden | Separation or parallelism can improve one contribution while adding delay, support effort or exclusion elsewhere. |
| Adaptation and continuity | The arrangement can change within an adequate Method's allowed variation; a change to its action or joins can instead require Method reselection. |
| Remit and consequence | A facilitator may change discussion conditions without having authority to change participation rights, protection, budgets or the eventual decision. |

### PSDA.17:4 - Solution

Reconcile the engagement around the result and its necessary conditions. Preserve useful order where a real dependency warrants it; preserve overlap where the work actually overlaps. Change the relationship that causes the conflict rather than assuming that all activities must share one structure.

#### PSDA.17:4.1 - Anchor the engagement and the result at risk

For an ongoing engagement, inspect a concrete occurrence: the objection that could not enter the model, the evidence received after a comparison closed, or the attention demand that stopped a participant's contribution. Distinguish an observed failure from a suspected mechanism. For a proposed engagement, use its intended-use case and proposed arrangement; name the later observation that would test it. A prospective design has no performed success to cite.

Recover the receiving question, subject, scope, horizon and decision boundary. Keep only participants, concerns, models and Method conditions that can change the arrangement decision. Existing `PSDA.11`, `PSDA.12`, `PSDA.1`, `PSDA.2`, `PSDA.3`, `PSDA.4`, `PSDA.13` results can supply these inputs under the conditions in section 12; no complete earlier traversal is required.

Ask what a usable return must preserve. Examples include a materially different service concern, an interpretable model assumption, a qualified configuration-specific result, a workable challenge route, or the distinction between a recommendation and the recipient's choice. A deadline is a condition to address, not evidence that these requirements have been met.

If the supposed conflict concerns another subject or receiving decision, establish that separate boundary before joining the work. If an indispensable scope or authority premise is missing, obtain its qualified source or return that precise gap.

#### PSDA.17:4.2 - Separate the structures that matter

Begin with the action whose contribution is unclear: for example, asking a participant to correct the meaning entered in a model. Use `B.1.5.EW` to explain what encompassing inquiry is being performed through that action now, which constituent operations make it possible, and which conditions of the whole change its performance. Follow each connection only as far as it changes this engagement. A missing skill, an unavailable contribution or a misunderstood operation may need a local correction before any rearrangement of the engagement.

When the arrangement decision depends on several different structures, use `C.32.MWA` to relate their accounts. The following distinctions help when they change that decision.

| Account | Example in a decision-support engagement | Distinction to preserve |
| --- | --- | --- |
| Reusable Method and its composition | Attributed inquiry contributes claims to conditional analysis under specified joins. | A Method's parts and necessary order are not the meeting's calendar or every activity performed there. |
| Work, its constituents and its temporal relations | Correcting an attributed statement can be part of recovering a concern within an ongoing inquiry. Separately performed model revision may overlap that inquiry; a calculation can require an earlier result. | Explain the constituent connection and any before-and-after dependence separately. Timing alone establishes neither parthood nor a composite Method. |
| Decision subject and affected Systems | Pumping equipment, access routes, service recipients and later operating arrangements. | A hierarchy among these subjects is not a hierarchy of inquiry Methods or participants. |
| Participation and authority | Residents contribute concerns; specialists qualify premises; a board receives advice and holds the investment choice. | Being present, having expertise, facilitating discussion and having permission to decide are different. |
| Descriptions and models | A concern map, a capacity model and a comparison note describe different claims for different uses. | Document sections and model nodes are not world-side parts, actors or authorizations. |
| Professional-cultural continuation | A community later reuses or rejects the engagement's facilitation variant. | A local choice or visible workshop does not establish transmission, uptake or effectiveness. |

State the correspondence that the current decision uses: for example, which participants can correct which model assumptions, which evidence can qualify which comparison, or which decision owner can change the receiving question. Preserve important losses in the description. A short map may omit timing details that the proposed arrangement now needs.

At a revealing moment, ask how a changed condition of the encompassing inquiry changes the selected action, and how a limitation in that action restricts the inquiry. Recover an unknown operation, obtain a qualified contribution, or practise the combination with its whole conditions still present. Stop the decomposition at an understood operation or sufficient available contribution.

Use the direct FPF pattern when a stronger relation claim matters: `A.3.1` for Method identity, `B.1.5` for Method composition, and the applicable Work or authority pattern for those distinct claims. A Method stack requires explained constituent connections, not a count of activities. If a changed whole no longer supports its old identity, reidentify it rather than preserving a convenient label.

#### PSDA.17:4.3 - Locate the interference and its actual consequence

Describe how one contribution defeats or weakens a condition needed by another. “Modelling and discussion happen together” is not yet a conflict. “The only modeller also controls the discussion, so a contested assumption is entered without its holder being able to correct it” names an interaction that can change the result.

Follow the conflict far enough to identify its receiving consequence. Does it exclude a material alternative, change an attributed value, invalidate evidence use, obscure dissent, prevent meaningful participation, or exceed the engagement's remit? Separate a technical limitation, a value difference, an evidence gap and an authority dispute; they have different returns.

Inspect what is actually shared: a person's attention, a model, a data basis, access to participants, a decision horizon or a rule for closing a claim. Do not solve an evidence gap by voting, or a value dispute by accelerating the model. Use an adequate available specialist result when it answers the question.

When the interaction remains uncertain, compare continuing under that uncertainty, narrowing the return, correcting the arrangement and obtaining further information. Select an observation, rehearsal or outside contribution only when its obtainable result can change the next action enough to warrant its effort, delay and displaced work under `C.11.DUA`; use `A.15.9` for the outside contribution. Existing knowledge may already settle the action. Where a consequential condition is unsupported, lower or stop only the relying claim. Unaffected inquiry can continue when its own conditions remain valid.

#### PSDA.17:4.4 - Construct alternatives that change the relationship

Compare the incumbent with at least one materially different workable arrangement. Select alternatives from the conflict, not from a universal menu.

A local separation can reserve discussion time while calculation pauses. Parallel inquiry and modelling can use explicit exchange points for consequential changes. Separate contribution channels can preserve a protected or unavailable participant's input, provided a usable correction route exists. A simpler provisional model can support discussion while a specialist develops the stronger analysis elsewhere. A different allocation of modelling and facilitation can remove an attention conflict, if the required people and capabilities are available.

State what each arrangement preserves, what it cannot yet produce, and who bears the extra work, delay or loss. A jointly edited model is not always preferable; when inputs and meanings are stable, bounded expert analysis can be sufficient. Nor does fully serial work automatically preserve participation: someone may become unavailable while another contribution is completed.

When the participants share the same relevant perspective and a missing perspective could change the inquiry, consider a prepared content challenger alongside a separate facilitator. Make that contribution explicit and source-supported; allow the group to decline it. It does not confer representation or consent on behalf of absent people. Its preparation and facilitation burden may make another participation route preferable.

Test whether the proposed change stays within the selected Method's permissible variation. A change from spoken to confirmed written inquiry may preserve the Method; replacing participant confirmation with a sponsor's interpretation does not. Return a changed action, result or join to `PSDA.4` rather than calling it a scheduling adjustment.

#### PSDA.17:4.5 - Make the bounded decision and retain the residual

Compare alternatives against the actual result conditions: faithful participation and interpretation, valid model and evidence use, feasible support, timeliness and applicable authority. Keep protected conditions outside compensating trade-offs unless their competent source actually allows that treatment. More output or a shorter meeting does not compensate for unsupported representation or evidence.

Choose within the established facilitation or engagement-design remit. If a proposed change requires another person's resources, changes a participation obligation or alters the authorized receiving decision, obtain the owner's decision. Until then, return a conditional proposal or blocker, not an implemented arrangement. The `C.32.MWA` synthesis informs this choice; it does not supply its authority.

State the selected change, the material reason, the alternative not taken, what remains unchanged, the residual difficulty, and the limit on the next return. Keep an adequate incumbent when another arrangement brings no justified gain. If no available arrangement preserves the necessary conditions, narrow the result or stop its unsupported part.

This decision concerns how decision support is conducted. It does not select the pump, authorize organization change, deploy a model, or establish agreement with the eventual advice.

#### PSDA.17:4.6 - Judge the changed interaction and hand on its conditions

Judge the interaction that justified the change using available observations. Can a corrected concern reach the comparison before it is relied on? Can the modeller identify the evidence version? Can the participant challenge the representation through the chosen channel? Can the separate facilitator sustain the discussion while analysis proceeds? If an unresolved answer could change continuation, select a worthwhile further observation as in 4.3.

A rehearsal supports a prospective arrangement only at its tested scope. For a change used in ongoing work, inspect the resulting contribution and any burden moved elsewhere. A smoother meeting or a completed document alone is not evidence that the material conflict was resolved.

The first result can be a short decision note or spoken return with a recoverable basis. It makes the arrangement, scope, authority, retained conflict, missing result and next observation usable; it need not reproduce every model or conversation.

Carry only consequential constraints into follow-up. For example, a corrected service assumption must reach the named comparison owner; an observation about another configuration does not refresh this result. `PSDA.15` still designs and compares its own follow-up alternatives. Evidence from this local variant may inform `PSDA.18`, but cultural continuation requires its own observations.

Reopen when the receiving question, a material participant or premise, the model use, the arrangement's support, or the permitted decision changes; when the chosen exchange fails; or when a moved burden defeats another necessary condition.

#### PSDA.17:4.7 - What changes in practice

The practitioner can say not only what the engagement does, but why its contributions can coexist without falsifying the return. A necessary sequence remains; a harmful coupling is changed; the unclosed part stays visible. The resulting decision is smaller and more useful than either a master lifecycle or an unbounded redesign of the whole engagement.

### PSDA.17:5 - Archetypal Grounding

#### PSDA.17:5.1 - A flood-pump inquiry cannot freeze away a service concern

This illustrative case continues the bounded attributed-inquiry and conditional-analysis Method. The board retains the investment choice; the engagement lead may arrange inquiry and model work within the agreed participation and resource conditions. The case supplies an available facilitator and analyst, not a general staffing requirement.

The analyst is preparing conditional comparisons; the working list includes fixed, mobile and staged pumping arrangements. The staged candidate still lacks a qualified consequence result. A separately consulted group has not yet corrected the rendering of its reachable-assistance concern. The current plan freezes the comparison before that correction can arrive. The facilitator is also expected to explain the calculations during the only discussion period. A finished comparison could therefore look complete while answering only the property-protection reading.

The relevant structures differ. Attributed inquiry and conditional analysis are Method contributions. Their actual work overlaps. The resident group, analyst and board have different participation and authority relations. A service-concern map and a hydraulic model preserve different claims. Investment implementation is later work, not a final level of the inquiry.

Consider the moment when the facilitator asks a resident to correct an attributed statement. Asking, interpreting the answer and confirming the amended wording are constituents of recovering that service concern; this recovery is part of the problem-structuring engagement now in progress. Suppose the resident means that assistance must reach people when the road is flooded, but the model records only protected property. Accurate transcription is insufficient: the missing connection is the translation of the confirmed concern into the model's question. The facilitator and analyst must preserve that meaning in the comparison or identify the service question it cannot answer. If they cannot make that translation, they need the relevant modelling contribution, not more accurate typing. The active exchange performs part of the inquiry while separate calculation can continue elsewhere.

The lead compares three arrangements:

| Arrangement | What it can preserve | Consequence for this case |
| --- | --- | --- |
| Keep the early freeze and explain the completed model in one session. | Analytical stability and the existing timetable. | Cannot support a claim that the uncorrected service concern was considered. A narrower technical return remains possible. |
| Stop every analysis until every participation response is complete. | Allows those responses to precede analysis. | Delays independent calculations and still cannot promise that every person will respond. |
| Continue bounded analysis while the facilitator maintains inquiry; join material corrections before the affected comparison closes. | Existing qualified calculations, a real correction route and separate attention to discussion. | Requires coordination effort and a clearly limited return if the correction or its technical consequence remains unresolved. |

Under the supplied remit and available support, the lead selects the third arrangement. The facilitator obtains correction of the attributed concern through its agreed channel. The analyst identifies which consequence claims that correction could change and carries unaffected calculations forward. The next return distinguishes qualified calculations, unresolved service claims and the exact access question. If the correction arrives too late for a supported comparison, the brief retains that limitation instead of silently dropping the concern.

A short resulting decision is:

> Keep inquiry and conditional analysis in parallel, with the facilitator handling claim correction and the analyst handling the affected model use. Close each comparison only with its current service meaning and evidence limits visible. Preserve the mobile-access gap and any unanswered contribution in the board's return. The investment choice is unchanged and remains with the board.

The moved burden is explicit: the facilitator and analyst must reconcile the corrected meaning with the consequence account, and the board may receive a narrower answer. A test follows one corrected statement into the draft comparison and checks whether its dependent claim is revised or left explicitly open. That test does not establish road access, district-wide agreement or a superior pump.

If separate analytical support becomes unavailable, the lead must reconsider the arrangement—for example by pausing calculation during the material discussion. The staffing premise cannot be replaced by a role label.

#### PSDA.17:5.2 - A non-contested advice question with a moving evidence basis

A committee asks a separate advisory team for a ninety-day service-development comparison. No disagreement about the question is reported. Internal development and a human–AI support arrangement are live candidates; the organization's allocation and AI evaluation results remain specialist inputs.

During preparation, the system owner changes the proposed AI configuration from A to B. The evaluation already supplied concerns A. Meanwhile, the allocation analysis can still answer an independent question about internal development. The original plan waits for one whole “evidence package” and then issues one complete comparison. Its all-or-nothing join either delays useful work or tempts the adviser to pass A's result into B's claim.

The team considers keeping a historical-A comparison, waiting for every B premise before any return, and separating the returns by their actual dependencies. The first does not answer the committee's now-B question. The second remains possible but withholds the independent allocation result. Within its agreed control of analysis and delivery, the team retains the qualified internal-development contribution and keeps the cross-candidate comparison open wherever B is material. It considers a B qualification only if an obtainable result could change the recommendation within the receiving window and warrants the acquisition burden. Otherwise it returns the useful internal-development result and the unresolved B limitation.

The arrangement names the configuration owner who reports a further change, the specialist result each claim can consume, the person assembling the comparison and the condition for closing it. It does not freeze the operating system, prevent its owner from changing B, or turn the available internal-development result into the recommended direction.

The test substitutes another A-only result at the receiving join. It must remain an A contribution or an unusable input for the B claim, while the independent contribution stays usable. A later adequate B result can close that particular gap. A further change of subject or horizon reopens only the affected use.

This is reconciliation without a disagreement workshop. The decision changes how qualified results can be returned together; it supplies no AI safety, human learning, organizational feasibility or deployment authority.

#### PSDA.17:5.3 - Overlap without an architecture problem

Two analysts examine independent uncertainties for an unchanged question using adequate sources. Neither consumes the other's result, blocks participation or changes a shared condition. Their calendars overlap, but no material interference has been identified. Continue the work; there is no reason to manufacture a common Method, hierarchy or facilitation redesign.

### PSDA.17:6 - Bias-Annotation

**Scope:** arrangements of problem-structuring and decision-support work for a named engagement. The pattern does not govern every concurrent project activity.

Watch for analytical capture: the easiest-to-compute account becomes the whole question. Watch also for participation romanticism: a joint session is credited with representation, expertise or agreement it did not establish. The repair is to trace the actual claim and contribution, including absent or protected participation, rather than treating either the model or the meeting as authoritative.

Architectural tidiness can hide moved burden. Inspect the participant, specialist or recipient who now pays for the proposed improvement. A successful local variant remains local evidence, not proof that a profession has adopted it.

### PSDA.17:7 - Conformance Checklist

| Check | Passing observation |
| --- | --- |
| Recognizable conflict | A specific engagement result and an interaction that can defeat one of its material conditions are identified; concurrency alone is insufficient. |
| Truthful anchor | Observed work and suspected mechanisms are distinguished; a prospective arrangement has a realization and later-test condition. |
| Non-isomorphic structures | Only relevant Method, work, subject, participation/authority, model/description or cultural accounts are used; their important relations and losses remain explicit. |
| Real alternatives | The incumbent and a materially different arrangement are compared for the same receiving use, including support, effort and moved burden. |
| Bounded decision | The chosen change or retained arrangement follows the actual remit; missing authority or specialist evidence remains a conditional return or blocker. |
| Intact Method and source use | Changes outside a Method's permitted variation return to Method selection; a new configuration does not inherit an old premise without qualification. |
| Interaction judgement | Available observations support the claimed change in the join, participation condition or attention arrangement; unresolved limits remain explicit, and further observation is selected by its possible effect and burden. Document completion does not establish success. |
| Usable continuation | The next recipient can recover what changed, what remains open, the consequential follow-up constraint and the smallest reopen condition. |

### PSDA.17:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Better move |
| --- | --- | --- |
| Turn the agenda into the architecture. | A sequence hides actual overlap, shared attention and authority conditions. | Recover the relations that change the current result. |
| Solve the model and declare the engagement complete. | Technical closure can exclude an unanswered interpretation or participation condition. | Qualify the technical return and preserve the missing contribution. |
| Separate everything to remove friction. | Extra handoffs can increase delay, exclusion and inconsistent assumptions. | Compare the moved burden with the conflict actually removed. |
| Add a challenger and claim absent people were represented. | A prepared perspective does not establish their participation or consent. | Keep the source and representation limit; obtain an appropriate direct contribution where needed. |
| Reuse the nearest available evidence package. | Its subject, version or horizon can differ from the current claim. | Qualify each consequential join or return its exact gap. |
| Declare a new culture after one workshop. | Local enactment supplies no observation of later transmission or retention. | Return the local variant and evidence to the distinct cultural question. |

### PSDA.17:9 - Consequences

The engagement can return useful partial results without hiding how its work was arranged. Participants' corrections, specialists' premises and decision owners' authority remain connected but distinct. Necessary order is preserved without forcing all modelling, inquiry and observation into that order.

The cost is explicit coordination and sometimes a narrower or later return. Separate roles require support; separate channels require usable joins. Some conflicts remain with a specialist or authority owner. The gain is not friction-free work, but a defensible arrangement whose remaining limits the recipient can use.

### PSDA.17:10 - Rationale

Method choice and faithful facilitation do not by themselves settle whether their enactment can satisfy several conditions at once. The same adequate inquiry Method may fail under one allocation of attention or one result-closing rule and remain usable under another. Conversely, an apparent scheduling change can replace a Method's essential confirmation or evidence condition.

The pattern therefore starts at one threatened result, recovers selected relationships, and compares arrangements through their consequences. A constituent can perform part of ongoing inquiry while other work overlaps it or supplies a later result. Recovering that vertical connection can locate a missing ability or semantic join that a different timetable would leave unresolved. This distinguishes structural interference from an ordinary claim disagreement and avoids reopening the entire engagement after each correction.

The choice is proportionate. A single sufficient sequence is retained when it works; a coupled arrangement is warranted when the actual interaction changes the answer. The result states what observations support it and what remains unresolved; a proposed arrangement still needs to work under the conditions in which it will be used.

### PSDA.17:11 - SoTA-Echoing

**Practice question:** how should a practitioner alter a decision-support engagement when modelling, participation and result closure constrain one another? The selected line is a situation-qualified arrangement with explicit interactions and local tests. It is compared with a sufficient ordered Method, expert-only analysis and more intensive participatory arrangements; none is universally preferred.

| Question and selected answer | Serious alternative, defect and decision | Source role, limits and changed locus | Reopen condition |
| --- | --- | --- | --- |
| Which order can guide this engagement? Preserve supported dependencies while inspecting the actual model-building and participation interactions. | A fixed sequence is useful when it fits. **Adapt** a multi-structure account where that sequence hides interference; accept the extra coordination cost only for the threatened result. | Franco, Hämäläinen, Rouwette and Leppänen's [2021 behavioural-OR review](https://doi.org/10.1016/j.ejor.2020.11.031), especially §5.2, is a best-known-line synthesis and counterweight to an all-linear or all-nonlinear story: it reports relatively linear engagement paths alongside more complex model-building paths and situated facilitation. Its heterogeneous studies do not validate one arrangement here. This changes 4.1–4.3 and the local test in 4.6. | New comparative evidence or a failed join shows that the selected arrangement loses a consequential result or imposes unnecessary coordination. |
| Must modelling be completed before participants can affect it? Couple the contributions when their interaction changes the model's receiving use; retain expert analysis for a sufficient bounded technical question. | Expert-led production avoids some interaction cost. Fully joint modelling can expose meaning while consuming scarce attention. **Adapt**, rather than universally select, facilitated modelling and inspect consequential interpretations at their joins. | Franco and Montibeller's [2010 review](https://doi.org/10.1016/j.ejor.2009.09.030) supplies the operative expert/facilitated contrast, not a universal superiority claim. Franco and Nielsen's [2018 four-workshop study](https://doi.org/10.1007/s10726-018-9577-7) supplies situated evidence about facilitator formulations shaping interaction, not guaranteed consensus. These comparison contributions change 4.3–4.4 and 5.1. | Actual participation, meaning or support conditions defeat the proposed coupling, or a cheaper direct analysis now closes the use. |
| What if a homogeneous group lacks a material perspective? Consider a prepared challenge with distinct facilitation, not an invented voice for absent people. | Asking the same participants to argue both sides may add no missing information. **Adapt** the conditional challenge arrangement; **reject** its use as substitute participation or a universal staffing rule. | Cunico, Zimmermann and Videira's [2024 study, online 2023](https://doi.org/10.1080/01605682.2023.2263101), §§3 and 7, offers a serious alternative through one exploratory group-model-building application. Preparation, facilitator workload and role ambiguity are explicit trade-offs; effectiveness does not transfer automatically. It bounds 4.4 and the corresponding anti-pattern. | Direct participation becomes feasible, adequate perspective sources are absent, or the changed role damages inquiry or exceeds available support. |
| Is one model, agenda or hierarchy enough to settle the arrangement? Retain different structures through their warranted relationships. | A single view is cheaper when it preserves the needed distinction. **Adopt** the current `C.32.MWA` synthesis when it does not; **reject** layout as proof of a practice relation. | `C.32.MWA` supplies the common obtaining/prospective and several-structure Method. Here the applied decision concerns modelling, participation, challenge and return conditions; the synthesis alone supplies neither professional premises nor decision authority. This governs 4.1–4.2 and 4.5. | A direct relation or domain contribution changes the synthesis, or the conflict no longer needs several structures. |

These comparisons support bounded moves, not a universal workshop design or evidence of institutional effectiveness. Source change reopens the affected move or limit; it does not require every otherwise adequate engagement to restart.

### PSDA.17:12 - Relations

- **`PSDA.11` and `PSDA.2` → `PSDA.17`:** the bounded engagement question and usable scope frame this arrangement decision only for the same subject and receiving decision. They create no temporal order.
- **`PSDA.12` → `PSDA.17`:** the participation and concern account supplies only the participants and concerns material here; inclusion settles neither formulation nor authority.
- **`PSDA.1` → `PSDA.17`:** plural formulations enter where their inquiry changes the candidate arrangements. Agreement is not required and dissent remains explicit.
- **`PSDA.3` → `PSDA.17`:** the multi-model account is used only where it discriminates arrangement alternatives or claims.
- **`PSDA.4` → `PSDA.17`:** the engagement Method and limits apply only to the named situation and qualification window. Availability establishes neither fit, enactment nor cultural uptake.
- **`PSDA.13` → `PSDA.17`:** shared and contested claims preserve material agreement and disagreement in this decision; the account does not make the decision.
- **`PSDA.17` → `PSDA.15`:** the bounded arrangement decision supplies a follow-up design constraint only when it changes that design choice. The receiver still generates and compares its own alternatives.
- **`PSDA.17` → `PSDA.18`:** the local decision may supply evidence or a variant for a named cultural-continuation question. Visibility proves no generation, transmission, enactment, recognition, selection, retention or effectiveness; absent evidence leaves the corresponding link unproved.
- **Direct FPF and specialist returns:** `B.1.5.EW` recovers how an action performs encompassing work and which constituents make it possible; `C.32.MWA` supplies the several-structure synthesis. `C.11.DUA` selects worthwhile further investigation, and `A.15.9` supports reuse or worthwhile acquisition of an outside-practice result. Applicable Method, Work, authority and evidence patterns govern their own claims. If a required input is absent, stale, out of scope or incompatible, use a qualified direct result or retain the exact gap. Pattern adjacency and a MethodDescription supply no performed result.

### PSDA.17:End

## PSDA.18 - Deliberately Continue and Change Problem-Structuring and Decision-Support Culture

> **Type:** Method pattern (DPF)
> **Status:** Stable
>
> **Primary working result:** an **account of the current enacted decision-support culture and one bounded cultural-continuation decision**, with the affected practitioners and variants, authority, retained alternatives, later observations where obtained, and explicit evidence gaps.

### PSDA.18:1 - Problem frame

**Use this when** a decision-support practice needs to decide whether to retain or change how its ways of working are passed on, recognized, chosen or kept alive across practitioners and engagements. A new team copies a recommendation format but loses its uncertainty and dissent. A capable facilitator leaves, and the remaining library does not preserve how to handle a contested contribution. A service rewards decisive-looking recommendations so consistently that honest blockers stop appearing in its examples.

The wider activity is problem structuring and decision support. This pattern governs **deliberate continuation or change of its enacted professional culture**: the relations through which particular Methods, practical judgement, descriptions and norms are generated, transmitted, recognized, selected, remembered, retained or lost. It does not treat a school name, profession, publication or software platform as one thing that acts.

Start with an ordinary sentence: “In our flood-advice service, new facilitators learn from case examples and observation; the examples retain the models but omit why an unresolved service concern limited the recommendation; we are deciding whether to change the receiving practice exercise.”

That sentence identifies a possible intervention, not proof of its cause or success. Recover the actual practitioners, work and sources far enough to decide whether to retain the arrangement, change it, branch to another variant, investigate, or stop. Adequate existing observations and qualified judgement can complete a continuation decision; another hypothesis or intervention is needed only when its contribution can change that decision.

The gain is continuity of usable practice without compulsory uniformity. A receiving practitioner can preserve the important judgement or make a justified adaptation; the service can see what the intervention changed and what it did not.

**Do not use this pattern** merely to select a Method for one engagement (`PSDA.4`), update a repertoire offering (`PSDA.16`), resolve one current work conflict (`PSDA.17`), publish a document, or count participation. Enter the cultural question only when a generation, receiving-enactment, recognition, selection, memory, retention or loss relation matters. A client holder's capability development or a non-cultural population's evolution is not automatically the culture of decision-support practice.

### PSDA.18:2 - Problem

A practice can preserve its visible forms while losing the reasons that made them useful. A concern map becomes a diagram to complete. A conditional comparison becomes an unconditional recommendation. A workshop's apparent agreement becomes a claim that affected people were represented. These changes can travel through teaching, templates, peer imitation, commissioning and recognition even when nobody intends them.

The reverse failure is to resist every variation in the name of fidelity. A receiving team faces different access, values, uncertainty or authority conditions, but is told to reproduce the original format. It may preserve the carrier while making the Method unusable.

Neither a new edition nor one successful engagement settles this problem. The practitioner needs to distinguish what was made available, what reached another person, what was actually done, what was selected and retained, and what consequence followed. A bounded intervention can then be chosen without pretending to control an entire discipline.

### PSDA.18:3 - Forces

| Force | Tension |
| --- | --- |
| Continuity and adaptation | Important judgements must survive transfer, while a receiving situation may justify different actions or support. |
| Recognition and plural practice | Shared standards can make good work visible; one prestigious school or decisive-looking result can suppress warranted alternatives and dissent. |
| Reach and receiving enactment | Publication and digital support can reach many people without showing that they can use the Method. |
| Local authority and distributed culture | A service can change its own arrangements; other practitioners and institutions may choose differently. |
| Useful judgement and incomplete evidence | A bounded, reversible change may be warranted before long-term retention or causation can be established. |
| Memory and protected information | Cases can preserve practical meaning, but source qualification, confidentiality and participant protection can limit what may be shared. |

### PSDA.18:4 - Solution

Begin with the enacted practice and the relation that needs attention. Compare a small set of materially different continuation options, choose only within the actual authority, and observe the receiving practice and decision-support consequences. Keep the intervention decision, its performance and the cultural observations separate.

#### PSDA.18:4.1 - Name the current practice, population and intended consequence

Name the current decision-support Discipline as practiced here, not as a universal school label. Recover the particular Method or variant, the practitioner population, the engagement or community, the place and period, the relevant carriers, and the recurring result at risk.

For example, the relevant practice may be a municipal team's attributed inquiry and conditional comparison, carried through observed facilitation, concern maps, model explanations and bounded recommendation accounts. The question is whether another facilitation team can preserve those contributions in its receiving engagements. “The spread of PSMs” is too broad for that decision.

State the intended professional consequence. It might be that material dissent remains attributable; a missing premise stays visible; a receiving team can distinguish a conditional comparison from a full recommendation; or an unavailable participant contribution is not replaced by an invented consensus. Preserve any cost in time, access, capability or useful analytical independence.

Recover the deciding person or System and the intervention boundary. When a precise Agent claim is needed, `A.13` requires the actual System, a local agential kind and its criterion, evidence of classification, an obtaining assignment, and the relevant scope, situation and window. A team name or collection of practitioners supplies none of these by itself. Authority to change facilitation, training, commissioning or publication is a separate fact; it is not authority to choose the client's investment or to direct another community.

A short recognition account need not become a complete culture inventory. If the target is one receiving exercise, keep unrelated traditions, networks and institutional changes outside. If authority is missing, return the exact decision or permission question. If the cultural relation is not the problem, take the cheaper direct return.

Use C.36 for the cultural claim being made, C.36.RP for sustaining and renewing shared ways, and C.36.MC when the Method-culture contribution itself needs qualification and development. Here the receiving practice is problem structuring and decision analysis: preserving attributed meanings, material dissent, uncertainty and qualified returns in later inquiry. The following professional construction adds those conditions; it does not replace the general cultural Methods or extend this repertoire to every OR practice.

#### PSDA.18:4.2 - Recover what the evidence actually shows

Use `C.36` for the cultural relations and their distinctions. Begin with concrete practice evidence: the changed instruction, observed interaction, qualified account of learning, receiving enactment, selection decision, retained example or demonstrated loss. Label expert estimates and conjectures. A lack of a population study does not prohibit a useful bounded judgement.

The following questions help keep different claims apart. Open only those that can change the current decision.

| Relation at issue | Evidence to recover | What the evidence does not establish alone |
| --- | --- | --- |
| Variant generation | The proposed or actual difference in the reusable way, its source and conditions, or the changed teaching, recognition or memory arrangement. | A new name or file does not identify a new Method; a proposal is not an enacted variant. |
| Transmission | What contribution passed from which source through which carrier or interaction to which receiving practitioner, when and under what interpretation. | Sending or downloading a document does not prove understanding, skill or receiving enactment. |
| Receiving enactment | A bounded actual occurrence in which the receiving practitioner followed the identified Method, with its meaningful conditions and result limits. | Attendance, stated intention or a copied output does not prove that the Method was followed. |
| Recognition and selection | Who recognized which contribution under what criterion, and which practitioner or institution selected which variant for what use. | A local project choice, credential or endorsement does not prove population-wide selection or fitness. |
| Memory | A recoverable description, exemplar, explanation or other carrier that preserves the distinction needed for reuse. | An accessible archive does not show that practitioners retain the ability or habit of using it. |
| Retention or loss | Evidence over the stated interval and relevant opportunities that a contribution continued, changed or ceased to be usable or enacted. | Silence, a missing publication or no opportunity to use the Method does not by itself establish loss. |
| Mediation | The actual tool, platform, community or publication arrangement and the visibility, interpretation, recognition or selection relation it changes. | A prominent display, recommender output or high access count does not establish value, control or cultural success. |

Keep claim scope smaller than or equal to the observed population and period. A workshop account may show one useful adaptation. A review of published applications may reveal cases to inspect. Neither establishes how every practitioner in a country works.

The `PSDA.16` repertoire supplies a variant, lineage or bounded evidence only when it changes this cultural decision. Its offering status is not evidence of transmission. The `PSDA.17` arrangement result can similarly supply a local change or observation; resolution of one interference is not evidence that another team learned it. If either input is absent, stale, out of scope or incompatible, obtain a compatible result that supports the particular cultural link being claimed, or leave that link unproved.

For a claimed performed occurrence, first recover each actual performer's `A.13` basis and independently admit the occurrence through `A.15.1`: performance history, enacted Method, extent and the obtaining containing-System relation. Add `F.6` only when precise assignment-bound attribution is consumed. Missing attribution does not erase independently established Work. A case packet remains evidence or description, not the occurrence.

Do not demand a complete causal history before a small permitted intervention. Use the available basis to decide the present continuation. Leave explanations unresolved where their distinction cannot change that supported decision; select further inquiry through `C.11.DUA` only for an obtainable contribution worth its whole burden. If a new facilitator drops a concern, the cause might be an incomplete example, a changed participation condition, lack of skill, time pressure or the reward for a quick positive answer. Each can require a different change.

#### PSDA.18:4.3 - Compare continuation options at the affected relation

Compare retaining the present arrangement, changing one material relation, maintaining a separate branch, and stopping or reverting the proposed intervention. Treat these as options when they are genuinely live, not as four mandatory forms to complete.

| Option | Useful question | Typical decision-support consequence |
| --- | --- | --- |
| Retain the present arrangement | Is the apparent failure outside its promised use, or is the current way already adequate at lower effort? | Preserve a useful narrow Method and avoid disrupting practiced judgement. |
| Change one arrangement | Would a change to facilitation, teaching, peer discussion, commissioning, recognition or source presentation address the identified mechanism? | Make the missing participation, interpretation or qualified-return move available in receiving practice. |
| Keep a separate branch | Do different access, participant or evidence conditions warrant different supported ways? | Preserve plural practice without pretending that all variants fit the same engagement. |
| Stop or revert | Does the change remove a protected condition, exceed authority, create an unmanageable burden or fail its stated purpose? | Return to a qualified arrangement, narrow the offering, or leave the receiving result explicitly blocked. |

Make the mechanism and trade-off explicit. Replacing a template may improve access but leave tacit facilitation judgement unaddressed. A guided practice exercise may expose that judgement but require an experienced facilitator and protected material. Changing recognition to include a well-grounded blocker can make honest returns visible, but a new checklist can also become another ritual.

A bundle of teaching, exemplar and peer-feedback changes may be one usable arrangement. If it is tried as a bundle, do not later attribute the result to one component without evidence. If the reusable decision-support action itself changes, return that Method or variant question to `PSDA.16`; cultural desirability does not admit a proposed Method.

Keep the receiver's circumstances in the comparison. Translation, remote participation, professional-service conditions, available expertise and the ability to challenge an interpretation can change the required arrangement. Copying the source faithfully is not sufficient if the receiving use cannot enact its essential distinctions.

#### PSDA.18:4.4 - Choose continuation or a bounded intervention

State who can choose, which continuation options are actually available, the intended participation or decision-return consequence, protected conditions, resources and period. If the available evidence supports retaining the present arrangement, record that choice and the conditions under which it applies. For a selected intervention, state what would stop, narrow or redirect the attempt.

Use `C.11` for an already formed bounded choice. Before developing or commissioning a new inquiry, use `C.11.DUA` to compare its attainable contribution with formulation, design, participant and facilitator time, access, interpretation, delay and displaced work. A missing formulation, alternative or probe-design result can remain the limit on a stronger answer; acquire it only when the current question warrants that work.

Keep the choice local. A team may change its own case discussion, mentor arrangement or presentation of examples under its remit. It cannot thereby compel another team to adopt a Method, expose protected client information, certify practitioners, or decide the client's investment. An invitation, a receiving team's agreement and a service-wide rule have different authority and participation consequences.

Use the best qualified judgement proportionate to the decision. A reversible exercise with non-sensitive material may proceed on a stated mechanism hypothesis and modest evidence. A consequential service change may require stronger capability, professional, participant-protection and governance results. Obtain them directly; the cultural account does not invent consent, safety or competence.

Retain any serious alternative and expected loss that matter to the choice. The useful return can be “try one receiving exercise for this cohort, keep the present route for experienced staff, and do not extend the change until an independent receiving use has been observed.” That is a completed bounded decision even though its later effect remains unknown.

#### PSDA.18:4.5 - Perform and observe only the intervention that was chosen

Translate the decision into the actual teaching, facilitation, community, recognition or publication work needed. Keep proposed action and work planning separate from performance. A planned tutorial, a posted file and an actual guided exercise are different facts.

When performance is claimed, use the recovered `A.13` and `A.15.1` basis. An investigation of a proposed decision-support variant may enact an independently identified trial or teaching Method without pretending that the unadmitted candidate whole was already enacted as a `U.Method`.

Observe the receiving use that matters. Ask a receiving practitioner to reconstruct why a concern was retained, which premise limited a comparison, what remained outside the compared set, or why a blocker was the appropriate return. This is a possible intervention design, not a universal teaching recipe. Check whether it is suitable for the population and the professional situation.

Do not make participation in a real consequential decision an uncontrolled training experiment. Preserve the actual access, competence, confidentiality, challenge, source-use and fallback conditions. If sharing the original case would break them, use a qualified redacted or constructed case, or choose another route; acknowledge what that substitute cannot test.

Identify the actual changed object when a change is claimed. An amended example set, an altered display rule and a changed practitioner action are not the same transformation. Use `A.3.4` and the direct effect or Work-to-change predicate when those claims matter. A performed intervention, an observed value and a causal-effect claim remain distinct; a log or temporal succession supplies no missing relation.

#### PSDA.18:4.6 - Test the receiving consequence and competing explanations

Compare the later observation with the intended consequence at the same scope. Preserve the actual result even when the intervention did not work as hoped.

| Professional consequence | A useful observation | An unsupported stronger inference |
| --- | --- | --- |
| Participation and dissent | A material affected concern can enter, be corrected and remain attributable in the receiving inquiry. | More attendees or fewer objections means equal influence or consensus. |
| Uncertainty and evidence | The practitioner preserves the relevant configuration, horizon, qualification and unclosed premise. | A complete model or fluent explanation means every input is adequate. |
| Recommendation return | The account preserves the compared subset, inference, dissent, limits and the appropriate direction, set, probe, request, blocker or abstention. | A signed-off report is necessarily useful advice or an authorized later choice. |
| Receiving use | The named receiver can recover what this result permits and where it must return. | Delivery, access or a positive reaction proves understanding, reliance, implementation or effect. |
| Continuation | The identified contribution appears in an independently observed later use under stated conditions. | One coached performance proves long-term retention or practice-wide adoption. |

Distinguish a useful local outcome from an explanation of why it occurred. An improved return might reflect the exercise, prior experience, a more skilled facilitator, additional time, a different problem, easier evidence or changed authority. Keep those alternatives live where the evidence cannot distinguish them.

When the next question is how this practice may develop, retain credible rivals whose difference can change the answer; do not manufacture a fixed number. Return the supported forecast or continuation with its material uncertainty. Select a new discriminating observation only when it is obtainable and worthwhile for that question. For example, an explanation-rich case library may support later independent use, or its effect may disappear without a mentor. A later uncoached case can inform that distinction; it does not isolate every causal influence.

Use `B.5` and `B.5.2` for hypotheses and testable consequences, `C.28` for an actual causal claim, and `A.3.3` only if a state-space and transition-law claim is needed. An ordinary uncertainty about continuation does not require a mathematical cultural-evolution model.

Ask practitioners and affected participants what was preserved, excluded or made harder. Retain dissent about the intervention itself. Reflective examination of practice can reveal a harmed relationship or lost contribution that a report count misses; it does not replace direct evidence needed for a claimed effect.

#### PSDA.18:4.7 - Return the cultural account and keep its limits usable

Return the smallest account that lets the next user act. It should make the following recoverable without copying the entire history:

- the current practice, Method or variant, population, place, period and carriers;
- the cultural relation that justified attention and the evidence or labelled estimate;
- the bounded decision, actual authority, retained alternative and accepted cost;
- what was proposed, performed or changed, stated separately;
- the available receiving-enactment and decision-support observations, with the limits that affect reliance;
- the unproved transmission, recognition, selection, retention, loss or causal links;
- the supported continuation, responsible return, narrowing or stop, and any separately selected further observation.

A decision can close from the available basis with its relevant uncertainty. If further observation is selected, retain its question and conditions; an unperformed intervention supplies no successful cultural-change claim. Conversely, an observation can establish a receiving use without establishing that this intervention caused it.

Update the `PSDA.16` repertoire only when the cultural evidence changes a Method offering, applicability, lineage or refresh decision. Return a changed current interference to `PSDA.17`, an affected recommendation to `PSDA.14` or `PSDA.15`, and a capability or domain-truth question to its qualified owner. Each return identifies the next question and the pattern or practice that answers it.

Preserve the useful narrow incumbent and the unselected branch. A variant can be inappropriate for one receiving use while remaining valuable elsewhere. A deliberate decision not to continue it in a named setting is different from an unexplained loss across the profession.

#### PSDA.18:4.8 - Refresh the affected relation or stop

Reopen when a consequential carrier, Method, practitioner population, receiving condition, source claim, authority or observation window changes; when the intervention loses its necessary support; or when evidence defeats the expected consequence. Trace the change to the particular cultural and professional claims it can alter.

A departure may remove mentoring capacity without proving that the Method was forgotten. A software update may alter which examples are visible without changing the decision-support Method. A source correction may invalidate one taught inference while leaving the rest usable. State the actual consequence and retain independent claims.

Use `A.10` for the bounded source reliance, `A.10.1` when several actual receiving uses of a changed source must be found and requalified, and `G.11` when its currentness or refresh-planning conditions obtain. Publication and access remain with their direct patterns. Neither source freshness nor carrier availability proves cultural continuation.

Close when the present answer and its material limits are clear; any selected later observation retains its own conditions. Stop or revert the intervention when its protected condition fails, its cost defeats the intended use, or no warranted next action remains. Do not keep generating variants or collecting cultural metrics merely because the entire culture cannot be proved.

### PSDA.18:5 - Archetypal Grounding

The following cases are hypothetical. Observations stated inside them are additional case facts, not claims about actual communities, measured effectiveness, or the enactment of earlier proposed arrangements.

#### PSDA.18:5.1 - Another team must learn the qualified return, not just its format

In a municipal flood-advice service, `DecisionSupportTeam-East` uses the identified attributed-inquiry and conditional-analysis Method. Its practitioners work with residents, finance, operations, ecology and emergency-service participants on the 2027 flood-pump question. Concern maps, model explanations, workshop records and recommendation accounts carry the practice.

The cultural question concerns East's practitioners and the receiving `DecisionSupportTeam-West` in the service's East district and controlled online case environment during March–May 2027. East may change its facilitation and teaching arrangements. West may choose how to prepare for its own permitted engagements. The board retains the investment decision.

The current practice already preserves a qualified fixed/mobile comparison, the unclosed staged alternative, and the reachable-assistance and protection questions. The `PSDA.17` continuation supplies a bounded arrangement and correction route; the `PSDA.16` repertoire supplies its applicability and lineage limits. Neither proves that West received or enacted this practice. The proposed late-correction Method whole retained for trial in `PSDA.16` is still a candidate; this case does not admit or deploy it.

East sends a permitted case packet. West confirms that the file arrived. In a preliminary practice discussion, West's draft turns the conditional fixed/mobile comparison into an overall investment recommendation. The material service concern appears only in an appendix. The packet is available, but the needed interpretation did not survive this use. That observation does not show that West can never learn the Method or that every recipient misunderstood it.

East and West consider the following alternatives.

| Arrangement | Comparative reason |
| --- | --- |
| Keep sending the existing packet | Cheap and adequate for already experienced practitioners; the observed interpretation gap remains for this receiving group. |
| Add one guided qualification exercise using an explanation-rich case packet | West must explain what the comparison supports, what remains unclosed and why. This may address the observed gap, at the cost of experienced facilitator time. |
| Keep separate receiving routes | Experienced staff continue with the compact packet; practitioners needing the explanation use the exercise. This preserves differentiated support but requires clear entry conditions. |
| Stop the transfer attempt for this case | Necessary if source qualification, protected information, receiving capability or facilitation support cannot be secured. |

Within their stated remits, they choose the guided exercise for this receiving group and retain the compact route for experienced staff. The exercise and its packet are tested as one arrangement. No claim is made that the packet alone causes the improvement.

The hypothetical performer and occurrence basis is explicit. Both teams are independently recognized coordinated service Systems with defined boundaries and coordination Methods. The service's local inquiry-steward kind requires goal-directed, condition-sensitive regulation of inquiry and practitioner preparation, including correcting or stopping an unsupported return. Prior evidence establishes that each team meets that criterion. Its directly declared steward-appointment relation has distinct obtaining East and West assignments for the stated service scope and March–May window. These `A.13` facts do not grant investment authority or assert an Agency Grade.

The case separately supplies the performance histories: East's 12 March, 09:00–11:00 inquiry followed the attributed-inquiry and conditional-analysis Method; the two teams' 20 March, 09:00–10:30 exercise followed an independently identified guided-qualification teaching Method; and West's 10 April, 09:00–11:00 receiving inquiry followed the attributed-inquiry and conditional-analysis Method. A locally declared work-within-service relation applies only when the entire occurrence lies inside the service's defined facilitation or practitioner-preparation operations; the supplied boundaries and histories establish it for these three occurrences. They therefore have an `A.15.1` basis independent of the packet or timetable. This case does not need an additional assignment-bound `F.6` attribution claim.

During the exercise, West identifies the exact limit: “The fixed/mobile calculation is usable for its stated assumptions. It does not close the staged alternative or establish reachable assistance. Return those gaps with the qualified calculation; do not name an overall investment choice.” The facilitator challenges a substituted unqualified access premise. West keeps it outside the supported comparison.

In the later April inquiry, an independently observed receiving use preserves a resident's corrected service concern and the same distinction between qualified calculation and missing access evidence. The recommendation account retains the staged alternative as unclosed. No pump purchase, district-wide agreement or improved flood outcome is inferred.

The cultural return is deliberately narrower than “the service adopted the Method”:

| Claim | Supported result or gap in this case |
| --- | --- |
| Generation and memory | A new receiving-exercise arrangement and explanatory packet are recoverable; their source and intended use are explicit. This is not admission of a new decision-support Method. |
| Transmission and receiving enactment | The teaching interaction conveyed the qualified-return distinction, and one later West inquiry enacted the identified Method under stated conditions. File delivery alone did not establish either. |
| Recognition and selection | The exercise feedback recognized preservation of the conditional comparison and honest gaps. West selected that way for the named April engagement; this is not selection by the whole service or profession. |
| Retention and loss | One later receiving use is observed. Continuation beyond that interval, use by other teams and loss elsewhere remain unproved. |
| Intervention consequence | The intended distinction appeared in the receiving return. The evidence does not isolate the contribution of the exercise from prior skill, added attention or other conditions, and supplies no investment-effect claim. |

The evidence supports retaining the receiving arrangement for one further cohort with matching qualification and support conditions. A further uncoached observation is selected only when its attainable contribution to that next use warrants its burden. If mentoring becomes unavailable, the route is reconsidered rather than offered unchanged. East keeps the existing qualified Method and the compact route; the still-unqualified late-correction proposal remains a separate `PSDA.16` candidate.

#### PSDA.18:5.2 - A library of polished advice can hide the honest return

A non-contested development-advising service is considering a change to its case library. The display currently promotes the most-viewed positive recommendations. The service suspects that this makes a decisive-looking answer easier to copy than a warranted request or blocker.

The access records show visibility, not learning or enactment. Two explanations remain live: the display may shape what newcomers imitate, or already familiar cases may simply receive more views. The first useful result is the bounded account of visibility and the unresolved receiving-use question. A claim that the software caused a cultural failure remains unsupported; that limit does not by itself select a new study.

One proposed arrangement pairs a positive example with a qualified non-choice return and asks a receiving practitioner to explain the difference. Retaining the current display is the cheaper alternative; removing the automated promotion rule is a possible fallback. The service must establish its own deciding System, remit, professional conditions and permission before changing the live arrangement; the flood-service authority does not transfer.

The library's constructed client is the Northbank service organization. It needs reliable incident recovery over the next ninety days. Internal development would train its existing recovery team and rehearse revised procedures. The alternatives are an external recovery provider and the existing team assisted by AI configuration B for diagnosis. Critical-service coverage, the customer-data boundary and a capped probe budget remain protected.

For this teaching case, assume a qualified allocation result confirms that two recovery engineers are available for four hours each per week for twelve weeks of training and rehearsal, with the required on-call shifts still fully staffed. This establishes that Northbank has staff time for that internal-development programme under the stated coverage condition. Whether the programme will improve recovery remains unverified.

The available AI evaluation covers configuration A, while B uses different tools; it does not qualify B for this use. The external provider's arrangement has not been assessed. Report the supported staffing finding: Northbank can allocate those two engineers to the programme while maintaining on-call coverage. Retain the separate gaps in recovery effectiveness, B's qualification and the provider assessment, and leave the three-way ranking unresolved. Request the missing evaluation for B through A.15.9 only when its obtainable contribution warrants acquisition.

This exercise tests whether the distinction can be reconstructed from the library arrangement. It establishes neither actual client use nor cultural retention. A later permitted receiving engagement would supply different evidence. If the source gap is in the library's content rather than its display, obtain the missing qualification for configuration B or correct the library's claim about B; rearranging examples cannot qualify B.

The culture at issue is the advisers' way of handling evidence and returns. The human client's learning, an organization's allocation capability, an AI configuration's performance and a population's evolution remain separate subjects. Better teaching of their boundaries supplies none of those domain conclusions.

#### PSDA.18:5.3 - Publication coverage and ordinary non-use

A review finds few published PSM applications in a region. The service may use that observation to look for practitioners or cases, but it cannot conclude that the practice is absent, lost or ineffective. The journal/search boundary is not the boundary of enacted culture. A local continuation decision can use qualified practitioner evidence without first commissioning a global survey.

If the only task is to correct a source locator, use the direct source or publication guidance. If the only question is which available Method fits tomorrow's engagement, use `PSDA.4`. Neither requires a cultural intervention.

A non-cultural population or lineage does not become a deciding Agent because it changes over time. Return that subject question to its direct practice. A researcher may separately choose an authorized intervention with its own scientific and governance basis; that does not turn the observed population into the recipient or chooser of advice.

#### PSDA.18:5.4 - Continue a supported practice

A service lead is deciding whether to retain the compact case packet and ordinary peer discussion for experienced advisers. In four inspected, uncoached returns from two recent cohorts, practitioners preserve the compared subset, uncertainty and material dissent. Qualified local judgement supports continuing this arrangement for the same uses and support conditions. The observations do not isolate the packet's contribution from experience or peer discussion, and establish no profession-wide retention.

A proposed two-hour comparison would displace the only available consultation on a consequential disputed return and would not change this continuation decision. Retain the present practice and those evidence limits. If a later interface hides the qualification or a new receiving group loses it, reopen that affected relation. The actual receiving loss and available teaching support in §5.1 instead warrant its bounded exercise; neither outcome is a universal rule to experiment or to retain.

### PSDA.18:6 - Bias-Annotation

Prestige and publication bias can make visible schools look like the whole field. Preserve the actual population and evidence window, including qualified practitioner accounts and unobserved links.

Intervention bias favors changing something that already works. Keep the narrow incumbent, a cheaper continuation and stopping in the comparison. Fidelity bias pulls the other way: preserving the exact format can destroy the intended use under different receiving conditions.

Consensus and positivity bias reward smooth meetings and decisive recommendations. Inspect whether a dissenting concern, qualified non-choice or refused transfer remains recognizable and usable. Do not punish practitioners merely for exposing a genuine source or authority gap.

Automation and observer bias can make access counts or watched performances look like independent adoption. Distinguish what the tool displayed, what the practitioner understood, what was enacted later, and what the evidence cannot establish.

### PSDA.18:7 - Conformance Checklist

**Recognition** asks whether a relation through which decision-support practice continues or changes is the missing result. One sentence naming the practice, receiving population, affected relation and next choice can be enough.

**Assurance** asks whether the authority, performer, occurrence, source, cultural and effect claims needed by that choice are qualified at their own scope. More elaborate records do not supply missing evidence. A small reversible intervention may use an explicit expert judgement; a broader effect or population claim needs its own basis.

| Check | Sufficient answer |
| --- | --- |
| Current practice | The Method or variant, practitioner population, engagement/community, place, period and carriers are recognizable. |
| Cultural question | The generation, transmission, receiving-enactment, recognition, selection, memory, retention or loss relation that changes action is named. |
| Continuation choice | A real decider and separate authority basis support the bounded choice, with its material alternatives, cost and limits. A supported retention needs no new intervention; a selected inquiry has attainable value, full burden and a stop. |
| Receiving meaning | Participation, dissent, uncertainty, qualified comparison and recommendation-use distinctions survive or their loss is reported. |
| Performance and consequence | Proposal, plan, performed Work, actual change, observation and causal effect are not substituted for one another. |
| Evidence limits | Source coverage, estimates, observed occurrences and unproved population or retention claims remain distinct. |
| Continuation or return | The result names what is retained, changed, narrowed, unproved or stopped and which direct question should reopen. |

A missing link can block a stronger claim while leaving a useful bounded decision intact. The checklist is not a requirement to prove every cultural relation before any professional improvement.

### PSDA.18:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Announce cultural adoption from a new edition or course | Recover actual transmission, receiving enactment and the population/period covered; retain the rest as gaps. |
| Teach only the finished model or recommendation format | Preserve the interpretation, material dissent, qualification and stop that made the result usable. |
| Make every receiving practice copy the source exactly | Compare the necessary meaning with actual access, capability and participation conditions; qualify an adaptation or retain a separate branch. |
| Treat a team title as intervention authority | Recover the deciding System's agency basis and the separate permission or authority for the named change. |
| Call one project choice population selection | State who chose what locally and obtain separate evidence for selection and continuation across practitioners. |
| Infer causation from a better-looking result after training | Preserve rival explanations and the actual scope of the observation; test the stronger claim only when the decision needs it. |
| Use popularity or publication counts as a fitness score | State what the measurement observes and recover the professional consequence that matters. |
| Keep intervening until all cultural links are proved | Close the bounded decision with honest gaps, retained alternatives and a specific next observation or stop. |

### PSDA.18:9 - Consequences

A practice can continue important judgement without freezing one school or format. It can maintain different receiving routes, make a bounded intervention, and recognize that a well-grounded request or blocker can be a successful professional return.

The cost is attending to receiving practice and retaining inconvenient evidence. Some apparent adoption remains visibility, some short-term success remains a local observation, and some changes must be narrowed or stopped. The result is still useful before long-term or population-wide claims are warranted.

### PSDA.18:10 - Rationale

The domain problem remains after the general cultural relations are separated. Decision-support culture must preserve how practitioners handle participation, contested meaning, values, evidence, uncertainty, alternative comparison and the boundary between recommendation and later choice. A generic account of copying or selection does not determine which of those professional contributions is at risk or how to repair its receiving use.

The pattern therefore starts from enacted practice and an intended decision-return consequence. It uses `C.36` for the cultural question and the direct patterns for agency, Work, evidence, choice, change and effect. It adds the professional comparison between facilitation, teaching, community, recognition and source-presentation arrangements.

A small intervention can proceed on qualified judgement without claiming general effectiveness. Keeping that distinction allows practical continuation and honest learning rather than either unbounded cultural control or paralysis until a complete history is known.

### PSDA.18:11 - SoTA-Echoing

The working question is **how to continue useful decision-support judgement across practitioners and engagements without confusing visibility, prescribed practice, local performance and cultural consequence**. The selected line combines a bounded enacted-practice account, attention to receiving interpretation, comparison of actual continuation arrangements and evidence at the grain of the claim. It accepts the cost of observing practice; dissemination alone remains appropriate when availability is the only result needed.

| Question and selected move | Serious alternative, defect and changed locus | Source role, limit and reopen condition |
| --- | --- | --- |
| What can application reviews establish about a current culture? **Adapt** their reported cases as leads while retaining the corpus boundary. | A publication-based diffusion account is cheap to construct but misses unpublished practice and does not distinguish availability, enactment or retention. Sections 4.1–4.2 and 5.3 keep those claims separate. | [Kogetsidis (2025)](https://doi.org/10.1108/IJOA-08-2024-4746) and [Kogetsidis (2026 online)](https://doi.org/10.1108/EMJB-06-2025-0214) are dated application-review comparators, not required inputs to every case. The latter examines selected journals over 2010–2024, not a census or cultural-effectiveness trial. Reopen when better evidence changes the named population, relation or continuation decision. |
| What should a receiving arrangement preserve? **Adapt** a practice-facing account of context, trust, stakeholder engagement, facilitation and reflective professional learning. | A portable recipe or final-output template is useful when its meaning is already shared; alone it can hide practical judgement and ethical consequences. Sections 4.3–4.6 and 5.1 expose those receiving conditions. | Yearworth's [*The Practice of Problem Structuring*](https://doi.org/10.1002/9781119744856.ch6) and [*Evaluation*](https://doi.org/10.1002/9781119744856.ch12), published in 2024, present this practice-facing and evaluation line in their chapter summaries. They do not establish the effectiveness of the exercise proposed here. Reopen if a stronger practice account or receiving observation defeats the assumed mechanism or burden. |
| Does new AI-assisted problem structuring establish a transferable culture? **Retain as a candidate comparison**, separating generated material, human validation and later use. | A large shared output can widen the material considered, but treating that output as shared understanding or enactment loses the receiving problem. Sections 4.2, 4.5 and 5.2 require the exact receiving consequence. | [Voltan and Kells (2026), GOSR](https://doi.org/10.1002/sres.70125), is a contemporary conceptual proposal for facilitation with GenAI-assisted sensemaking. Its limitations include absent participant feedback and further practical testing; it is not evidence of widespread adoption or a universal PSDA Method. Reopen on qualified receiving-use evidence, a changed tool/source condition or a defeated interpretation premise. |
| How might digital mediation change continuation? **Adapt** separate hypotheses about social learning and the mediating arrangement. | Treating a library or recommender as a neutral pipe ignores which variants become visible; importing a model's optimum into a professional service overstates transfer. Sections 4.2, 4.6 and 5.2 keep mechanism hypotheses and observations distinct. | [Czaplicka, Baumann and Rahwan (2025)](https://doi.org/10.1098/rsif.2024.0686) studies a simplified cultural-accumulation model combining network-based learning and algorithmic mediation. It supplies possible mechanisms for investigation, not a PSDA field result or a prescribed mixing ratio. Reopen when an empirical or model result changes the specific mediation hypothesis under its stated conditions. |

### PSDA.18:12 - Relations

- `C.36` supplies the cultural-evolution and intervention distinctions. This pattern retains the professional participation, interpretation, uncertainty and decision-return question. `C.36.P` can restore cultural wording when a label still hides the relied-on subject or relation.
- `PSDA.16` supplies qualified repertoire evidence or a variant only when it changes the cultural-continuation decision. It neither entails nor authorizes that decision; absent or incompatible input leaves the exact link unproved.
- `PSDA.17` supplies qualified local arrangement evidence or a variant under the same condition. A resolved conflict is not proof of transmission, receiving enactment, selection, retention or effect.
- `PSDA.4` retains engagement-level Method selection; `PSDA.13`, `PSDA.5`, `PSDA.6`, `PSDA.7`, `PSDA.8`, `PSDA.9`, `PSDA.14`, `PSDA.15` retain participation, comparison, recommendation and follow-up results. Cultural work returns only a changed question to its direct owner.
- `A.13` and `A.15.1` qualify actual performers and dated Work; `F.6` applies only to a separately needed assignment-bound attribution. `A.3.1` and `A.3.2` distinguish the Method from its description or a candidate.
- `C.11` supplies a formed bounded choice; `B.5`, `B.5.2`, `A.3.3` and `C.28` govern the actual hypothesis, dynamics or causal question when needed. `A.3.4` and the direct Work-to-change or effect relation govern their own claims.
- `A.15.9` obtains an exact missing practice result; `A.10`, `A.10.1` and `G.11` apply to the bounded reliance, affected uses and currentness questions. Missing evidence does not create a whole-language prerequisite.
- Publication, access, archive or selected-set treatment, capability development and holder-specific truth remain with their direct patterns and qualified sources. Neither a cultural account nor a shared carrier supplies those results.

### PSDA.18:End

## PSDA.19 - Bound the Development-Direction Advising Engagement

> **Type:** Method pattern
>
> **Status:** Stable
>
> **Normativity:** Normative unless marked informative.

### PSDA.19:1 - Problem Frame

**Use this when** someone asks a distinct adviser which development direction to consider for a person, organization, or other identified subject, but the terms of that help are not clear enough to support responsible advice. The question may already be well formed. What remains unsettled is who the advice serves, what the adviser can competently provide, what may be disclosed, and who retains the choice.

Begin by naming the recipient, developing subject, intended use, horizon, and the person or arrangement expected to prepare the advice. Then settle the professional conditions that can change whether the service may proceed. The first useful result is an admissible bounded advising question, a narrower service, or an exact blocker or referral.

This pattern is the entry to Development-Direction Advising. It governs the development-advice relationship and its permitted reliance. The shared PSDA formulation, comparison, engagement and recommendation Methods supply their distinct contributions. An admissible engagement question is not yet a warranted recommendation.

**Ordinary non-use boundary.** Self-directed opportunity construction needs no adviser. Enter C.40.OI, C.40.NU, C.40.PC, C.40.DC, C.40.JF, C.40.OP at the missing result when that is the actual question. If a chooser already has adequate premises and needs only their own choice, use C.11 or the direct domain rule. Reuse a current adequate engagement boundary; do not repeat intake merely because another pattern is being used. When one qualified domain practice owns the whole service, use it directly.

### PSDA.19:2 - Problem

An apparently helpful development conversation can serve the wrong recipient. An employer pays for career advice and expects the employee's private assessments. A sponsor's preferred provider becomes the presumed recommendation. A fluent AI-assisted memo conceals an unqualified assessment or unauthorized use of client information.

Another failure makes entry unnecessarily expensive. A formed question is sent through an exhaustive diagnosis, participant-mapping exercise, or workshop before anyone asks what advice is actually needed. The recipient receives either premature prescription or a process that never reaches a useful return.

The adviser needs a bounded relationship in which service competence, participation, confidentiality, conflicts, referral, and choice remain explicit enough to govern the next useful action.

### PSDA.19:3 - Forces

| Force | Tension |
| --- | --- |
| Recipient and sponsor | The person paying may have legitimate interests without being entitled to every assessment or choice. |
| Help and autonomy | An adviser must offer a useful return without taking the recipient's or another authorized participant's decision. |
| Breadth and competence | Development questions cross practices; coordinating their results does not qualify the adviser to perform every assessment. |
| Transparency and confidentiality | The recipient needs intelligible grounds while protected information retains its disclosure limits. |
| Affordable entry | A formed question needs only its missing relationship conditions, not an automatic workshop or complete diagnosis. |
| Delivery and continuing duties | One recommendation can be delivered while actual contact, referral, protection, or closure duties remain. |

### PSDA.19:4 - Solution

Agree the development-advice question and the conditions under which the adviser can responsibly answer it. Keep the boundary proportional to the use and consequence.

#### PSDA.19:4.1 - Identify the actual relationship and receiving use

Use [PSDA.11 — Bound the Decision-Support Engagement and Authority Boundary](#psda11---bound-the-decision-support-engagement-and-authority-boundary) to recover an adequate engagement question or its exact missing value. State whose development is under consideration, what later contribution or decision the advice serves, the horizon, and the return sought now.

Distinguish the recommending performer from the recipient at the grain of this engagement. Naming one self-directing actor twice does not establish the distinct advising relation used here. A recipient may also be the choice owner when that authority is supported. An organizational team can receive advice from a separate internal specialist without appointing an external consultant.

Identify the client, sponsor, developing subject, recipient, and choice owner separately where their differences change service, disclosure, protection, or action. One person may occupy several positions. State the relevant coincidence rather than inferring it from a job title, contract signature, or payment.

A useful question might be: “For Mira's own development choice over four months, help her compare directions for contributing to cross-disciplinary review; her employer's later assignment decision remains separate.” If no recipient or receiving use can be identified, return that gap or the direct inquiry instead of inventing an advice engagement.

#### PSDA.19:4.2 - Bound the service by competence and applicable duties

Agree what assistance is being offered and excluded. Distinguish development-direction advice from assessment, teaching, psychotherapy, recruitment, sales, programme design, and implementation when confusion would change what the client receives. A referral or a smaller service may be the correct result.

Determine the professional and local requirements that actually apply to this service, jurisdiction, and client relationship. Use their competent interpretation when applicability is uncertain. A professional code cited in this pattern establishes neither a licence nor every local duty. Do not assert assessment competence, legal authority, or a client's capacity from an adviser title or a signed form.

Ask what the adviser can judge and which specialist results bear the requested claim. Use A.15.9 for a missing human-development, organizational, technical, safety, legal, financial, or other bounded result; reuse an adequate current one. Retain the advice supported now and its material limit; a missing result becomes a request only when A.15.9 and C.11.DUA select its obtainable contribution against the whole acquisition burden. The supplying practice retains its Method and conclusion. Coordinating a career or organization question does not transfer those competences to the adviser.

For human career services, the applicable professional basis may require informed participation, competent assessment and interpretation, and appropriate referral or closure. [NCDA's 2024 Code of Ethics, A.2, A.10, and E.2](https://www.ncda.org/aws/NCDA/asset_manager/get_file/3395) supplies that bounded line. Apply it within its professional scope; obtain qualified help for consent or capacity questions that the adviser cannot resolve.

#### PSDA.19:4.3 - Agree participation, information use, and disclosure

Make the service and its limits understandable to the person whose participation is required. Establish the applicable consent or other legitimate participation basis, what information will be obtained, its intended use, who may receive it, and relevant confidentiality limits. Keep voluntary participation, mandated service, assent, and authority to act for another person distinct when the case requires them.

Specify what the sponsor receives and what remains within the advising relationship. Do not promise unconditional secrecy where applicable duties require disclosure, or assume that payment permits disclosure. A change in purpose or audience requires its own applicable basis; an earlier agreement does not silently cover every later use.

Use only the information needed for the bounded service. If a decisive premise cannot be disclosed to a recipient, explain the resulting reliance restriction without exposing the protected content. A qualified summary may support a bounded return without releasing raw assessment material. If the permissible explanation cannot support the requested reliance, return the narrower question or blocker; do not ask the recipient to treat an unexplained preference as a warranted recommendation.

When the client declines an optional assessment or service, explain the resulting scope and limits without converting refusal into an adverse factual judgement about capability. Follow any actual professional or legal duties that remain; the declined step is not permission to improvise the missing result.

#### PSDA.19:4.4 - Treat conflicts before relying on the advice

Identify material financial, provider, employment, organizational, or other interests that can distort the requested service. Make their treatment explicit under the applicable relationship: disclosure, changed scope, independent assessment, recusal, referral, or another qualified response.

Disclosure alone may not make an incompatible engagement acceptable. A sponsor's instruction to conceal a material interest or exclude a serious alternative can block the requested independent comparison. Return that service limitation; do not disguise it as a technical inferiority of the excluded direction.

For management consulting, [ICMCI's competence framework v4.0, C.1.1–2, C.2.1, and E.3.5](https://www.cmc-global.org/sites/default/files/public/icmci_cmc002_competence_framework_version_4.0_1.pdf) supplies bounded engagement, client-involvement, and conflict-disclosure guidance. These identified clauses inform the relationship question; the actual applicable professional requirements govern this service.

Preserve an independently qualified domain result within its established scope when a relationship conflict changes who may advise or how the result may be used.

#### PSDA.19:4.5 - Distinguish AI assistance from an AI development subject

If AI assists the adviser, establish the permitted use of client information and the responsible professional's review of the resulting content. Within the [ICMCI AI Code v1.0, May 2026](https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf), sections 1.2, 2.2, 3.1–3.4, 5, and 7, professional responsibility remains with the consultant; material AI use and its limits require appropriate client communication. An unverified generated answer supplies no specialist warrant.

If AI is instead the developing subject, identify the model, scaffold, tools, allocation, or composite arrangement being changed and its receiving environment. The recipient and choice owner are separate questions. A human learning result does not qualify a model change; use the relevant AI, engineering, operating, and governance results through A.15.9.

Both situations can occur in one engagement. Keep the adviser's use of AI, the proposed change to the subject, and the human client's professional protections separate.

#### PSDA.19:4.6 - Enter at the missing substantive result

Once the service boundary is adequate, identify what answer is still needed. Reuse current opportunity, characterization, reachability, and comparison results that cover this subject, configuration, use, and horizon.

If the receiving contribution or direction is unsettled, use the relevant construction pattern. If adequate directions exist, enter the actual PSDA alternatives, comparison, or recommendation question directly. PSDA.12, PSDA.1, PSDA.2, PSDA.3, PSDA.4, PSDA.13 become relevant only when participants, formulations, scope, models, Method choice, or facilitation can change the return; a formed question needs no workshop as an entry fee.

Use C.40.JF for a missing joint-reachability result and A.15.9 for an exact external premise. A service may be admissible while the evidence supports only a conditional set, request, or blocker. Keep the scope local: a missing provider comparison can block ranking all directions while an independent human-development result remains usable.

PSDA.14 supplies the bounded recommendation when that question is current. The later authorized direction choice remains separate. When the selected direction calls for human capability development, HCD.2 programme comparison, an optional programme recommendation, authorized programme choice and Learning Product Guide remain distinct further results. An existing programme-level comparison can be used directly for its programme question.

#### PSDA.19:4.7 - Return the boundary and preserve actual closure duties

Lead with what can be offered now and the most important condition. A two-sentence result can be sufficient:

> We can help Mira compare review-development directions for her own four-month choice; the employer receives only the agreed service summary, not her private assessment material. A recommendation remains conditional on the missing representative-practice and transfer results, while the employer retains its separate assignment decision.

If the relationship cannot responsibly supply the requested service, return the exact mandate, competence, consent, conflict, disclosure, or other blocker and the appropriate next receiver. State what limited independent help remains possible, if any. Do not infer that a service blocker proves the subject has no worthwhile development direction.

Fit the eventual explanation to the recipient's use. PSDA.14 and the applicable receiving-use guidance govern making the recommendation intelligible; persuasion to accept it is a different purpose. Delivery alone establishes neither understanding nor consent, choice, implementation, or effectiveness.

A completed recommendation application does not cancel duties arising from an actual professional relationship. Contact, referral, confidentiality, protection, and service closure continue only as their governing basis requires. If follow-up is needed, use PSDA.15 for a feasible observation and return arrangement; a date in the report creates no staffed service. Reopen the affected engagement condition when the recipient, purpose, competence, conflict, information use, or professional basis changes.

**Recognition and assurance.** The reader can recognize a bounded engagement from the recipient, developing subject, adviser, use, horizon, service limits, and retained choice. Assurance requires the actual competence, participation, protection, reliance, and authority basis relevant to that use. A clear account is not evidence that those conditions obtain.

### PSDA.19:5 - Archetypal Grounding

#### PSDA.19:5.1 - Employer-sponsored advice remains Mira's development question

This is a constructed case. Mira's employer funds four months of career-development advice. Mira asks a separate adviser whether to pursue cross-disciplinary review capability or a specialist engineering direction. The employer also wants information for a later staffing decision.

The adviser first separates the intended uses.

| Participant or use | Bounded position |
| --- | --- |
| Mira | Developing person and recipient for her own development choice. |
| Employer | Sponsor; it retains its separately authorized staffing decision. |
| Adviser | Prepares the development-direction return within the established career-service competence and agreed conditions. |
| Personal assessments | Used only within their qualified purpose and agreed disclosure basis; funding does not settle access. |
| Employer-facing return | An agreed service summary, with no private assessment content unless a separate applicable basis permits it. |

In the case, the adviser's competence for this bounded career service is established; specialist development and transfer assessments remain outside that competence. Mira accepts the bounded service and the employer agrees to the disclosure limit. Existing information identifies the two directions, but no qualified result supports the proposed independent-review transfer. The adviser returns the two-sentence boundary in `:4.7` with the limit on independent-review transfer. A specific HCD request follows only when its attainable contribution warrants acquisition; this service-boundary answer needs no request to be complete. Admitting the service did not make a course recommendation ready.

Now the employer requests raw assessment notes for staffing. That is a changed audience and use, not another copy of the agreed service summary. The adviser withholds that disclosure pending its applicable basis and revisits the affected service terms. Mira's earlier qualified assessment claims retain their established scope; the adviser takes neither her development choice nor the employer's staffing decision.

If the sponsor refuses any service except undisclosed assessment transfer, the current request may end with a scoped blocker or referral under the actual professional conditions. It does not justify an adverse judgement about Mira.

#### PSDA.19:5.2 - A provider interest changes the service, not the engineering facts

In a constructed organization case, a committee asks a consulting team to compare internal development, a provider arrangement, and mixed support for a ninety-day reliability need. The committee is the intended recipient and assumed authorized choice owner.

One consultant has a material payment interest in the named provider. A technical result about internal development is independently qualified, but the requested whole-set recommendation has not been made. The consulting team applies the relevant conflict requirements before offering that recommendation. Disclosure and independent comparison may be sufficient in one relationship; another may require recusal or referral. The pattern does not decide that professional question from the presence of a disclosure note.

If the sponsor demands a concealed provider preference, return the blocker on that service. Keep the independent technical result within its existing scope. Do not recast the conflict as proof that either internal development or the provider is technically infeasible.

#### PSDA.19:5.3 - A model is the subject, not automatically the client

In a constructed AI case, an authorized operations team asks a separate advisory arrangement whether to tune a model, change its retrieval support, or alter human–AI allocation. The team receives the advice; the changed model or composite arrangement is the subject. The advisory service still needs its own scope and qualified technical inputs.

An evaluation covers configuration A, while one proposed direction changes tools and oversight to B. The useful return keeps B's evaluation and safety premises unqualified while retaining the supported scope of A. Select a B-result request only when its obtainable contribution warrants acquisition; neither the limit nor a request supplies a deployment recommendation. The adviser's separate use of a drafting tool changes neither that gap nor the client's information-use restrictions.

For contrast, “tell this unmanaged biological lineage which direction it should choose” supplies no lineage-local recipient or chooser. Return that attribution gap to the evolutionary account. A research team asking about a proposed intervention is a different recipient-owned case requiring its scientific, ethical, safety, and governance basis.

#### PSDA.19:5.4 - Do not create personal advice from an audience description

A provider asks which learning programme to design for future participants. The provider's programme-design decision is the receiving use; the described audience is a design assumption, not a collection of assessed clients. Use PSDA.11 and the learning-product design practice for that question.

If Mira later asks whether that programme fits her own development, her later Work, starting conditions, support, and qualified comparison become relevant. A well-described audience does not supply those personal premises. Conversely, an adequate existing programme comparison can support a programme-level advice question without repeating opportunity construction.

### PSDA.19:6 - Bias-Annotation

Sponsor pressure can displace the recipient's use. Provider incentives can hide behind a technically plausible comparison. Professional confidence can make the adviser cross into an unqualified practice, while automated fluency can obscure that crossing.

Check whose question is being answered, which disclosure is actually permitted, and which competence is carrying the decisive claim. Keep these checks proportional: the absence of a dispute does not remove professional duties, and the existence of several participants does not require a workshop.

### PSDA.19:7 - Conformance Checklist

1. **MUST** identify the distinct recommending performer, recipient, developing subject, receiving use, horizon, and later choice owner at the grain of the engagement.
2. **MUST** separate sponsor, client, recipient, subject, and chooser where the difference changes service, disclosure, protection, or authority.
3. **MUST** bound the offered service, actual competence, applicable professional conditions, exclusions, and referral or closure requirements.
4. **MUST** establish the relevant participation and information-use basis without inferring consent, capacity, or disclosure permission from a title, payment, or form alone.
5. **MUST** address material conflicts before relying on the requested advice; disclosure must not substitute for the treatment actually required.
6. **MUST** distinguish AI assisting the adviser from AI as the developing subject and preserve the respective professional and technical qualification.
7. **MUST** use qualified external results for specialist premises and state the precise scope blocked when a result is missing.
8. **MUST** distinguish an admissible engagement question from a warranted recommendation and each later authorized choice or realization.
9. **MUST** preserve actual professional duties after delivery without inventing an indefinite follow-up service.
10. **SHOULD** reuse an adequate boundary and enter at the first missing result; ordinary self-directed construction needs no advising engagement.

### PSDA.19:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| The sponsor is every recipient | Payment is mistaken for disclosure rights and choice authority. | Name each actual use and its participation, disclosure, and decision basis. |
| Signed means informed | A form substitutes for the required understanding, participation, or capacity. | Establish the applicable condition or obtain qualified assistance. |
| Disclose and proceed regardless | A declaration substitutes for treatment of an incompatible conflict. | Use the actual professional response, including narrowed service or referral. |
| Admit the service, then prescribe | Relationship adequacy is mistaken for substantive evidence. | Return the missing premise and use PSDA for the actual recommendation. |
| AI answered, so the adviser is qualified | Generated content masks missing expertise or prohibited data use. | Keep responsible review and specialist qualification in their actual practices. |
| Every advice question needs a workshop | A formed question is forced through irrelevant intake work. | Use the first missing result and preserve adequate inputs. |
| Delivered means all duties ended | Completion of a return is mistaken for closure of the relationship. | Follow the actual contact, referral, protection, and closure basis. |

### PSDA.19:9 - Consequences

The recipient can understand what help is being offered, whose interests are represented, what may be disclosed, and which decision remains theirs or another participant's. A formed question can proceed without unnecessary construction or facilitation.

The boundary can also expose a genuine limit: a smaller service, an additional qualified supplier, a referral, or no responsible advice under the requested terms. Agreeing these limits costs attention and can frustrate a sponsor, but prevents a fluent answer from concealing the wrong service.

### PSDA.19:10 - Rationale

Development advice combines premises about a subject with a relationship in which someone is expected to help a recipient. Good technical premises cannot repair an unauthorized disclosure or incompatible conflict. Equally, a proper relationship cannot supply a missing development or transfer result.

Separating the two questions makes a useful partial return possible: the service can continue within its supported boundary while one substantive claim remains conditional, or a domain result can survive a change in who may provide the advice.

### PSDA.19:11 - SoTA-Echoing

**Practice question.** How can a formed development-direction question enter responsible advice without collapsing recipient, sponsor, professional service, and later choice?

**Best-known line for this use.** Combine PSDA.11's bounded receiving-use question with the applicable professional relationship conditions. This pattern **adapts** that division in `:4.1`–`:4.4` and `:4.6`–`:4.7`: use the smallest adequate boundary, establish the actual service limits, and return missing premises to their owners.

**Serious alternative and trade-off.** Generic authorization and a technically sound comparison can suffice for an ordinary local choice. They do not settle who receives Mira's assessment or how a provider interest affects the consulting relationship. At comparable intake effort, a question about the intended recipient and disclosure exposes that defect. An exhaustive diagnostic or facilitation engagement can be useful when it is the actual service, but adds burden without resolving a formed question more directly. The selected boundary trades a small amount of explicit agreement for a more usable and contestable service; the constructed cases do not establish measured effectiveness.

**Professional source returns.** NCDA's 2024 Code, A.2, A.10, and E.2, informs the human career-service participation, assessment, and referral limits in `:4.2`–`:4.3`. ICMCI v4.0's identified engagement clauses inform client involvement and conflict treatment in `:4.1` and `:4.4`. These are bounded source contributions, not one universal professional code or a complete current certification standard.

**AI-assisted service.** The ICMCI AI Code v1.0 adds the answer-changing responsibility, content-review, information-use, and material-disclosure conditions in `:4.5`. This pattern **adopts** their professional-scope boundary and **rejects** treating tool availability as warrant. Those conditions do not evaluate the AI development subject.

**Limits and reopen.** Apply the professional sources only where their scope or adoption is established, together with the actual local requirements. Reopen the affected boundary when those requirements, the service purpose, recipient, competence, conflict, or information-use conditions change, or when a less burdensome arrangement preserves the same protections and useful return.

### PSDA.19:12 - Relations

- **Uses PSDA.11:** the generic engagement question, participant positions, receiving use, and authority boundary.
- **Receives from C.40.OI, C.40.NU, C.40.PC, C.40.DC, C.40.JF, C.40.OP or adequate direct sources:** inquiry, characterization, opportunities, directions, reachability, and retained paths when those results are needed.
- **Uses A.15.9 and the relevant holder practices:** qualified specialist premises without taking over their Methods or conclusions.
- **Uses PSDA.5, PSDA.6, PSDA.7, PSDA.8, PSDA.9, PSDA.14:** alternatives, comparison, and recommendation only for the actual missing decision-support result.
- **Returns to the applicable professional relationship:** competence, participation, confidentiality, conflicts, disclosure, referral, and closure.
- **Returns to authorized participants:** the direction choice. When the selected direction calls for human capability development, HCD.2 supplies programme comparison, authorized participants make the programme choice, and Learning Product realizes the later Guide.
- **Uses C.40.RQ:** changed engagement premises and their opportunity-specific effects.
- **Uses PSDA.15:** a genuinely needed follow-up arrangement and affected recommendation return.

### PSDA.19:End

# Development-direction advising

> **Publication use:** a practice-use profile of this framework.
>
> **Practical result:** a development-direction recommendation with its sources and limits, or a statement of what is still needed to prepare one.




## PSDA.Advising:1 - Use this when

Use this profile when a person, organization or AI arrangement is considering what to develop next, a distinct recommending performer must help a named recipient, and the answer depends on several qualified practices. The recipient needs a useful direction, retained set, probe, request, blocker or abstention for a stated horizon. They do not need to be in a dispute.

Development-direction work also has an earlier, independently useful branch: constructing an opportunity when the worthwhile problem or possible contribution is not yet settled. Enter [Construct a Bounded Development Opportunity (FPF C.40.OCN:1)](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c40ocn1---problem-frame) directly for that question. A person can use it to explore future engineering Work without appointing an adviser or asking for a final recommendation. Its result is an opportunity with dependencies and a next question, not advice by another name.

This profile connects opportunity construction, the relevant PSDA contributions and direct supplier results. It is not one compulsory Method with eight stages. The developing holder, opportunity, recommendation and later choice remain different objects. Human development, organization change, strategy, operations, AI engineering, safety and other practices keep their substantive Methods and conclusion authority.

The smallest useful result may be two sentences: “The available comparison covers internal development and configuration A, not the external-provider direction. Obtain the provider comparison for the same result, security boundary and horizon before ranking all three.” That is a complete bounded return.

Do not invent this engagement when a chooser already has adequate alternatives and needs only their own decision rule, or when one qualified domain Method answers the whole question. Use the direct domain or C.11 guidance. A non-cultural population or lineage without a population-local recipient or chooser belongs to its evolutionary account; a separately authorized researcher considering an intervention is a different case.

When the recipient asks which programme to design for future participants, begin with [PSDA.11](#psda11---bound-the-decision-support-engagement-and-authority-boundary) and obtain the needed learning-product design result. Keep the audience description as a design assumption. For personal advice, identify the prospective participant and use the premises about that person's later work, starting performance and support that bear the answer. Missing premises limit the advice; obtain more only when their contribution warrants acquisition. The [programme-design case (Engineering.Reference:11.2)](Engineering%20DPF%20Suite/ENGINEERING-DPF-SUITE-REFERENCE.md#engineeringreference112---recommend-a-programme-before-the-learners-are-known) shows the two uses.




## PSDA.Advising:2 - Enter at the missing result

The entries below are alternatives, not a work order. An adequate result can be reused; a material change can reopen one contribution without reopening the rest.

| Working question | Start here | First useful return |
| --- | --- | --- |
| What useful future contribution could be possible? | [Opportunity-construction Method (FPF C.40.OCN:1)](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c40ocn1---problem-frame) | A candidate opportunity, dependencies, bounded reachability rationale and next question; no adviser is required. |
| Who is asking for what advice, and on what terms? | [Bound the advising engagement](#psdaadvising3---bound-the-advising-engagement), using PSDA.11 | A recipient/holder/horizon question and service boundary, or the missing condition. |
| What facts about this holder could reverse the answer? | [Recover only the relevant holder premises](#psdaadvising4---recover-only-the-relevant-holder-premises) | The holder's current configuration and facts or gaps that can change the decision. |
| Which specialist result is missing? | [Use the direct result-acquisition Method](#psdaadvising5---use-the-direct-result-acquisition-method) | A useful qualified answer and its limit, a worthwhile bounded request, or a blocker. |
| Which directions are actually live, and how do they compare? | [Keep a qualified live candidate set](#psdaadvising6---keep-a-qualified-live-candidate-set) and [Compare for this receiving use](#psdaadvising7---compare-for-this-receiving-use) | A bounded set, comparison, partial order or discriminating question. |
| What can the recipient responsibly consider now? | [Compose the bounded recommendation](#psdaadvising8---compose-the-bounded-recommendation) and [Return it for the agreed use](#psdaadvising9---return-it-for-the-agreed-use) | One or more explicitly scoped recommendation dispositions with basis and limits. |
| Has something changed that affects earlier advice? | [Reconsider only affected advice](#psdaadvising10---reconsider-only-affected-advice) | Retained, narrowed or blocked claims; a request to the practice responsible for an affected result; or a later recommendation. |

A qualified opportunity supplies a candidate basis to PSDA.5; PSDA.6, PSDA.7, PSDA.8, PSDA.9 supply comparison premises to PSDA.14; PSDA.15 handles an actual follow-up question. Each dependency applies only to the same relevant holder, configuration, use and horizon. Neither these links nor their order establishes performed Work, a composite Method, dispatch or authority.




## PSDA.Advising:3 - Bound the advising engagement

Write the question in ordinary terms: “For this recipient, what development direction should this holder consider within this horizon, and for what later use?” Identify the recommending performer separately from the recipient at the grain of this application. The recipient may also be the choice owner when that authority is established. Calling one self-advisory actor by two role names does not establish the distinct-performer relation.

Use [PSDA.11](#psda11---bound-the-decision-support-engagement-and-authority-boundary) for the engagement question and authority boundary. Distinguish client, sponsor, developing holder, recommendation recipient and chooser only where the difference changes the advice, disclosure, protection or decision. An employer paying for a person's career service does not thereby become the recipient of every personal assessment; a sponsor preferring a provider does not settle the committee's choice.

Before positive advice, establish the applicable service scope, competence, conflicts, confidentiality, permitted reliance and referral or closure conditions. These are professional relationship questions in addition to generic permission. The [ICMCI competence framework v4.0, C.1.1–2, C.2.1 and E.3.5](https://www.cmc-global.org/sites/default/files/public/icmci_cmc002_competence_framework_version_4.0_1.pdf) supports agreed engagement content, client involvement and disclosure of material interests in management consulting. It does not authorize every adviser or prove that advice works.

For human career services, apply the actual professional conditions for informed participation, assessment competence, intelligible interpretation and appropriate referral. [NCDA's 2024 Code of Ethics, A.2, A.10 and E.2](https://www.ncda.org/aws/NCDA/asset_manager/get_file/3395) is a bounded professional source, not a universal rule for organizations or AI holders. Determine its applicability and any additional local requirements; do not infer consent or a client's capacity from a signed form alone.

AI assisting an adviser and AI being the developing holder are different cases. Where the [ICMCI AI Code v1.0, §§1.2, 2.2, 3.1–3.4, 5.1–5.4 and 7](https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf) applies, the consultant retains responsibility, checks material AI-assisted content, respects client-data restrictions and explains material AI use and its limits. An unverified generated memo cannot acquire professional warrant from the tool's availability. The actual client relationship governs these duties even when the holder is an organization or a person.

Return the missing mandate, competence, conflict treatment, consent or admissibility condition when it prevents the requested service. A blocker can complete this recommendation application while obtaining professional duties remain in force. Existing safety, legal or emergency duties keep their own direct authority.

Do not require participant mapping, facilitation or a contested-situation workshop merely to admit a formed question. Open PSDA.12, PSDA.1, PSDA.2, PSDA.3, PSDA.4, PSDA.13 only when a participant, boundary, formulation, model, Method choice or disagreement can change this result.




## PSDA.Advising:4 - Recover only the relevant holder premises

Ask which fact, if different, would change a direction, protected condition, comparison or return. Recover that fact for the holder and configuration named in the advice question; do not build an exhaustive diagnosis as an entry fee.

| Developing holder | Premises that can matter | What cannot substitute |
| --- | --- | --- |
| Person | Representative later Work; current capability and evidence; access and expression conditions; target demand; resources; acceptable burden; intervention and transfer premises; consent and choice boundary. | A job title, course attendance, a generic competence inventory or another person's successful transition. |
| Organization | Needed contribution and receiving use; current Work and arrangement; positions and assignments; authority and interfaces; continuity; resources; candidate obtaining arrangements; strategy and protected conditions. | An organization chart, purchased platform, provider promise or one successful employee. |
| AI model, agent or composite arrangement | The changed object and its version; data, scaffold, tools or allocation; environment; evaluation validity; oversight and escalation; safety/security; baseline and protected conditions. | A human learning study, a benchmark from another configuration, a product label or a ranked recommender output. |

Current HCD demand, diagnosis and profile results can identify human premises; they do not, by that fact, establish an intervention's retention or transfer. OCE and Operations results can characterize a contribution or arrangement; they do not automatically compare every way of obtaining it. An AI result qualified for model/scaffold A is not evidence for B merely because both have the same product name.

For every material premise, retain the claim and identify its subject and configuration, the supplier or source, the qualification window, uncertainty and intended use. “Unknown” is useful when it says what cannot yet be inferred. Absence of evidence for one configuration is not evidence that every configuration is infeasible.




## PSDA.Advising:5 - Use the direct result-acquisition Method

Use [FPF A.15.9 - Use or Request a Bounded Result from Another Practice](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a159---use-or-request-a-bounded-result-from-another-practice) for qualified use and selection of worthwhile acquisition, with [FPF A.10](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a10---evidence-graph-referring-claim-bound-evidence-and-provenance-graph) for the actual reliance claim. State the question that the result must answer and identify the conclusion that remains unsupported without that answer. In advising, derive this question from the recipient's need for advice; in independent opportunity construction, derive it from the next unresolved dependency. Keep the useful present answer and its limit. Before formulating a further request, use A.15.9 and C.11.DUA to compare its obtainable contribution with the complete acquisition burden and available continuation; naming the dependency does not select that work.

An available result closes the need only when it covers the same material subject, configuration, use and window. An available MethodDescription says how a result might be obtained; it is not that result. The supplying practice chooses its Method and retains authority for its conclusion.

When acquisition is selected, request “a comparison of internal development, a provider and mixed support for this recovery result, ninety-day horizon, security boundary and continuity condition,” not “an organization-development strategy.” For a person, request the missing representative-Work demand or transfer premise, not “the right course.” For an AI configuration, request the relevant evaluation or safety disposition, not a generic endorsement of AI.

Use an adequate independent result while another branch is unresolved. State whether a missing premise prevents one claim, one candidate's admission, a pairwise comparison or the requested whole-set recommendation. Do not make the whole packet unusable merely because one unrelated source is old.




## PSDA.Advising:6 - Keep a qualified live candidate set

If the useful future contribution itself is unsettled, use the full [opportunity-construction Method (FPF C.40.OCN)](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c40ocn---construct-a-bounded-opportunity). It searches neighboring uses, distinguishes a niche, a proposed provision promise and a worthwhile problem, constructs directions and supports, and exposes dependencies and reachability. A technology label or archive entry cannot fill that result.

Once candidate opportunities or an adequate formed question exist, use [PSDA.5](#psda5---generate-decision-alternatives) to make the advice-relevant alternatives explicit. Keep each direction's status explicit: a feasible direction under stated conditions, a conditional opportunity, a candidate probe or a fragment retained for combination. Keep ruled-out configurations and named gaps visible as such, not as eligible alternatives. Do not let an attractive but conditional opportunity enter a decision-ready set as if its dependencies had obtained.

Keep materially different development, access/support, provider, Method/platform, allocation, staged and no-change directions when they matter. These are generation possibilities, not compulsory options. Several labels for the same intervention provide no real breadth. A different way of supplying the same result is not automatically a different worthwhile problem.

[OCE.8](Management%20DPF%20Suite/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce8---compare-human-ai-robotic-and-provider-arrangements-for-the-same-organizational-work-result) can supply the organizational same-result arrangement comparison after the required result, receiving use, horizon and acceptance premise are stable enough. It returns a changed or unjustified result premise to its owner; it does not supply this profile's whole opportunity search.

Use C.18 only for an actual generation/archive/front question, with its declared generator, operators, descriptors and retention or comparison basis. Use C.19 only for an actual live pool with a current governing policy. Thin evidence creates neither a default exploration posture nor permission to exploit. A probe needs a useful discriminating question and its own feasible, protected and authorized execution basis; otherwise retain the useful direction or limitation without making another request merely to finish.




## PSDA.Advising:7 - Compare for this receiving use

Use PSDA.6, PSDA.7, PSDA.8, PSDA.9 for values, uncertainty, consequences and robustness. State the candidate domain and the subset being compared, the receiving question, characteristics and scales, protected conditions, evidence and uncertainty, and the comparison rule that the result actually uses. Adequate current comparison results can be reused without running all four patterns.

C.16 supplies characterization; C.11.CRC preserves configuration-relative contribution; A.19.CPM supplies a comparison mechanism when its conditions hold. Consume a G.5 selector result only when its candidate domain, eligibility, Method, evidence, result kind and closure are actually established. A ranked list is not proof of that application.

Explain what the comparison can and cannot conclude. Preserve a partial order or non-dominated directions when the basis does not warrant a total ranking. If one direction is supported, explain its advantage over the strongest remaining rival and the conditions that could reverse it. Keep important value disagreement visible instead of manufacturing a shared weight.

Human consent and transfer, organization continuity and AI safety remain unlike premises. A protected condition cannot be compensated away by a favorable total score. When its own justification is disputed, use [PSDA.6 §4.4](#psda6---represent-values-and-trade-offs) and C.11.DUA to compare the protected outcome, causal and measurement basis, threshold, additional protection and full burden. Carry the requirement recommendation and its actual amendment limit in the advice; current force still governs available action. Likewise, a comparison of internal development and one mixed arrangement does not rank an unexamined provider, another model version or a materially different probe.

When evidence is thin, first ask whether the missing distinction could change the answer and whether obtaining it is worth its burden and delay. A small request naming the missing result, a retained set or a blocker may be more useful than another elaborate model. A declared comparison is an input to advice, not the recipient's choice.




## PSDA.Advising:8 - Compose the bounded recommendation

Use [PSDA.14](#psda14---prepare-and-return-a-decision-support-recommendation) to return what the recipient can responsibly consider now. The following development-direction returns are alternative result branches, not a sequence.

| Return | When it is useful | Content that makes it more than a label |
| --- | --- | --- |
| Retained or ranked set | Several directions remain live and the current scheme supports their trade-offs, partial order or order. | The returned set and the comparison scheme, what preserves each direction, what remains unresolved and what could warrant narrowing. |
| Supported direction | Qualified premises justify preferring one direction for the named holder, use and horizon. | Its comparative advantage, the disposition of serious rivals, material limits and reversal conditions. |
| Bounded information-gaining probe | A specified uncertainty could reverse advice and the supplied probe basis supports proportionate information gain. | Question, possible distinguishing observations, exposure, feasibility, protected conditions and stop; choice and execution remain separate. |
| Smallest-result request or handoff | A supplying practice can provide a missing premise whose obtainable contribution warrants its whole acquisition burden for this advice. | The bounded result, subject, configuration and window, affected claim, and what would let advice resume; a useful answer can instead finish with its present limit. |
| Blocker | A missing, stale, inapplicable or unauthorized premise prevents the requested responsible recommendation. | What is missing, which stronger conclusion is blocked and which independent content remains usable. |
| Abstention | The requested recommendation premise fails or the service cannot responsibly supply that kind of advice. | The failed premise and appropriate receiving account or referral, without an invented adverse factual judgment about the holder. |

A mixed return can retain two directions and block a complete ranking, adding a third direction's premise request only when its contribution warrants acquisition. Keep the scopes explicit; do not report mutually inconsistent overall statuses.

For this profile, the recommendation account makes seven things recoverable:

- the recommending performer, recipient, developing holder, question, horizon, choice owner and intended next use;
- the actual candidate domain, compared subset, exclusions and candidate gaps;
- each relied-on specialist result and relevant source edition, configuration, window and reliance limit;
- the declared comparison scheme, material trade-offs, protected conditions and inference to the return;
- uncertainty, dissent, evidence losses and unsupported extensions that can alter reliance;
- the supported disposition and the next consideration, request, reroute or separately governed choice;
- the observation or change in a source, configuration, authority, horizon or policy that would reopen a named claim.

This is content, not a mandatory form. A small blocker needs only the positions that explain its missing premise and receiving use. A consequential positive recommendation may need a protected annex and a fuller claim-to-premise account.

Keep each claim inside the narrowest material limit of the premises on which that claim depends. If evaluation covers configuration A, advice about B remains unsupported. If the internal-development comparison does not depend on that evaluation, it can remain usable. A shared bibliography is neither a dependence relation nor a reason to invalidate everything together.




## PSDA.Advising:9 - Return it for the agreed use

Lead with the disposition and its most important limit. Explain the evidence and reasoning at the recipient's level, including what the result does not authorize. If a decisive premise cannot be disclosed, state the resulting reliance restriction without revealing protected content.

For an actual receiving-use problem, use A.2.9 to ask what the recipient needs to understand or do, what evidence would show that the return serves that use, and what smallest repair is needed. Making a conditional recommendation intelligible is different from persuading the recipient to accept it.

Delivery completes the recommendation application; it proves neither understanding nor reliance, consent, choice, implementation or effectiveness. Acknowledgement is not a ChoiceResult. A programme, course, organization-change plan, assignment, provider commitment or performed Work needs its own content and authority.

The actual professional relationship may require further contact, disclosure, referral or service closure. Those duties do not disappear when this recommendation is delivered, and they do not arise merely because a profile mentions follow-up. Sales persuasion, psychotherapy, teaching and implementation remain different Methods with their own conditions.




## PSDA.Advising:10 - Reconsider only affected advice

Use [PSDA.15](#psda15---arrange-decision-follow-up-or-reassess-advice-after-a-change) when a changed premise can alter advice. Locate the premise and the claims that actually used it; preserve the earlier recommendation as an account of what was returned under its earlier basis.

Choose further guidance by the question it answers. For one already-known bounded source-reliance question, use A.10. When a materially changed source claim requires discovering and revalidating several receiving uses, use A.10.1. When actual conditions change while the source is unchanged, use the direct subject guidance. Use G.11 when the needed result concerns currentness, decay or scoped refresh planning or reporting.

| Changed premise | Bounded response |
| --- | --- |
| Human assessment no longer covers the target Work or current person | Remove that assessment's support from the affected capability or intervention claim; retain the useful advice at its remaining strength. Obtain an assessment for that Work and the person's current conditions only when its contribution warrants the whole burden. Preserve unrelated organization or AI claims. |
| AI model/scaffold A is replaced by B | Requalify B's evaluation, safety and contribution premises. Retain only claims whose basis survives the change. |
| Provider access or security condition changes | Reopen the affected provider or mixed-arrangement claim and any ranking that depended on it. Do not infer that internal development failed. |
| Consulting scope, conflict or disclosure conditions change | Revisit the affected service return and permitted reliance, not the truth of every domain result. |
| An opportunity's useful problem or support dependency changes | Return to the corresponding opportunity claim; reassess any retained stepping stone and dependent advice. |
| A changed observation crosses the advice's stated threshold | Use the qualified observation and interpretation to retain, narrow, block or reopen the affected contribution; compose another recommendation only when needed. |

Observation, interpretation, professional contact and renewed recommendation are distinct Work. If positive advice depends on future observations, establish who can obtain and qualify them, with what access, timing, burden and response opportunity. An infeasible observation obligation is a present limit on advice. “Review in three months” does not by itself make an effective follow-up arrangement.

The source-currentness responsibilities for this profile and its opportunity Method are specified in the [source-responsibility account](#psdareference13---keep-source-changes-and-case-changes-distinct). A change to the generation Method can require revising that Method; a changed fact about one holder normally requires only requalifying the affected application.




## PSDA.Advising:11 - Worked uses and stopping points

The examples below are constructed cases. Assumed specialist results illustrate what a warranted return would require; they are not results about actual clients, performed Work or demonstrated intervention effects.




### PSDA.Advising:11.1 - A ninety-day service-reliability question

A committee asks a separate advisory team which development direction the service organization should consider over ninety days. The committee is recipient and, under the case's assumed mandate, choice owner. The three live directions are internal development, an external provider and a mixed human–AI arrangement. Critical-service continuity, a security boundary and a capped reversible-probe budget are protected. The adviser discloses and resolves a material provider interest under the agreed engagement conditions before offering positive advice.

An operating account identifies the recovery contribution in question. Organization information describes relevant positions and interfaces. A qualified priority statement puts reliability before throughput for this horizon. None of those results compares the whole obtaining arrangements. The current OCE.8 Method is available to guide that comparison, but no adequate result for this client is supplied.

The first complete return is therefore:

> Retain internal development, the provider and the mixed arrangement as directions for consideration. The available basis does not support their whole-arrangement ranking for this ninety-day reliability use and its continuity/security conditions. The operating and position/interface accounts remain useful inputs.

The adviser uses A.15.9 to inspect an existing result for the stated use and protected conditions. If it is adequate, use it. If the gap remains, the unranked answer can finish; a new comparison is selected only when its attainable contribution warrants preparation, supplier effort, interpretation, delay, and displaced work. A selected request goes to the organization-allocation and relevant specialist owners, who choose their Methods.

Now consider a separate hypothetical continuation. A qualified whole-arrangement comparison and security result cover the three named directions. They exclude the specified provider configuration because it cannot preserve the security boundary. Internal development remains feasible but does not resolve the mixed arrangement's key uncertainty: whether permitted AI assistance can reduce the recovery queue without imposing an unacceptable verification burden or weakening fallback.

The supplied probe account covers the mixed configuration being considered, its bounded exposure and resource budget. It makes the distinguishing observations recoverable: representative recovery evidence, verification burden and fallback performance under the protected continuity condition. It supports the probe as proportionate, not as proof of eventual improvement. Compared with committing directly to either development direction, the probe can resolve that specific uncertainty at the bounded cost while preserving internal development as an alternative. The advice can therefore be:

> Consider the bounded mixed-arrangement probe first, retaining internal development. The supplied allocation, probe-feasibility and security results support this information-gaining return for the ninety-day reliability question. Throughput effect is still uncertain. Preserve service continuity, security and the probe budget; reconsider when representative recovery evidence or a relied-on premise changes.

This is not whole-set closure from an internal/mixed-only comparison: the supplied security result explicitly disposes of this provider configuration. A different provider, another mixed configuration or a substantially different probe reopens its own premises. The committee's choice, any authorized probe WorkPlan and later Work remain separate.




### PSDA.Advising:11.2 - A person considering four months of development

An engineer asks a separate career adviser whether to develop cross-functional management capability or pursue a specialist engineering direction over four months. The person is the developing holder and recommendation recipient; their own choice and the employer's separate assignment decisions must not be conflated.

The relevant input is representative later Work, not the management title. A qualified demand account might distinguish coordinating a cross-discipline review from supplying a difficult technical analysis. Current capability, accessible practice, time, consent, assessment limits and target-domain requirements can change which direction is plausible.

If only attendance and a course catalogue are available, return the missing intervention or transfer premise; do not prescribe the course or assert reachability. If qualified premises support both directions but not their order, retain them and name the distinguishing question, such as which representative Work the person can validly try within available support and time. The human branch uses current career information critically, as in [NCDG 2024, CD2 and CD3](https://www.ncda.org/aws/NCDA/pt/sp/ncdg_home_page); it does not infer learning transfer from career-information quality.

Before any separate advice request, the same person may independently use the [opportunity Method's human example (FPF C.40.OCN:5.2)](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c40ocn52---a-person-exploring-future-engineering-work). That entry does not require the distinct adviser assumed here.




### PSDA.Advising:11.3 - An AI or composite holder

An authorized team asks a separate recommending arrangement whether to modify a model, change a scaffold/tool configuration or alter human–AI Work allocation. Identify the object to be changed, its version, the intended environment, evaluation validity, oversight, protected conditions and receiving use. Model tuning, tool access and human–AI allocation are not interchangeable interventions.

Suppose a supplied evaluation supports scaffold A only in a bounded offline environment, while a proposed direction uses B with different tools. State that B's evaluation and safety premises remain unqualified; A's score does not transfer. A separately adequate organization-allocation comparison remains usable within its assumptions. Request B's result only if its obtainable contribution warrants acquisition for this receiving use.

If an applicable safety result excludes one configuration, exclude that configuration for the stated use. If evidence is merely missing, say so. A human course study supplies neither AI adaptation nor deployment safety. A recommender-system ranking can enter only as its separately qualified input; it is not the whole advice Method or deployment authority. Professional duties to human clients still apply where that service relationship actually exists.




### PSDA.Advising:11.4 - A population without a recipient, and an inadmissible engagement

A request to tell an unmanaged lineage which direction it should choose has no population-local recipient or chooser in this account. Abstain from that attribution and return variation, selection, reproduction, persistence and loss to the evolutionary source. Do not redescribe evolutionary change as recipient choice.

A research team may instead ask which authorized experimental intervention to consider. That is a separate recipient-owned question whose scientific, safety, ethical and governance premises must be established; the evolutionary countercase supplies none of them.

Likewise, a sponsor's instruction to conceal a material conflict or to rank a harmful unauthorized option cannot be repaired by a better score. Return the scoped blocker, referral or abstention required by the applicable professional and domain conditions.




## PSDA.Advising:12 - Recognition, assurance and practical gain

Recognition is inexpensive: another performer must help a named recipient make sense of qualified but incomplete development premises. A formed question can enter directly; a not-yet-formed opportunity can enter the independent Method. No institutional dispute, complete diagnosis or global candidate archive is required.

Assurance is use-specific. Check whether the material premises actually cover the holder, configuration and horizon, whether the comparison and recommendation follow from them, and whether service, protection and authority conditions permit the proposed reliance. High-consequence uses require their direct domain validation and independent assurance. A coherent profile, fluent explanation or available source does not establish those results.

In practice, a development request no longer silently becomes a course, staffing choice, organization-change programme or AI deployment. The recipient can see what is supported now, which alternatives remain, which result is missing for the stated question, and what would change the advice. The developer of an opportunity can stop even earlier, with a useful possibility and a discriminating question.

The [source-responsibility account](#psdasources3---source-responsibility-and-references) separates contemporary decision-support and professional sources, historical generation anchors, guidance from the practices supplying a needed premise, and application-specific results. It also states the bounded update responsibility. This profile claims neither universal cross-holder effectiveness nor that publication of a supplying framework has already produced any particular client's evidence.


## PSDA.Advising:End

# Cross-pattern applications

These constructed applications show how several pattern results can serve one working question. Their people, organizations, dates, data and supplied results are illustrative premises, not reports about actual clients or proof of effectiveness. A real use must establish its own facts, authority and evidence. The slices may overlap or reopen one another; their reading order is not a project lifecycle.



## PSDA.Application:1 - APP-PSD-01 — A flood-pump calculation is not the whole investment answer



### PSDA.Application:1.1 - The question and the people who need the answer

In a constructed 2027 case, a municipal resilience office asks a separate inquiry team to help the East-District Infrastructure Committee before the next flood season. The committee, called the board below, owns the later funding decision. The inquiry team may arrange the agreed investigation and return advice; it does not acquire investment or deployment authority.

The broad difficulty could lead to pump renewal, distributed storage, changed demand management or acceptance of a bounded risk. The current pre-season inquiry concentrates on the district pumping arrangement, including permanent and mobile capacity, maintenance, staffing and safe access. That smaller boundary does not reject storage or demand measures, settle relocation rights or declare long-term watershed effects irrelevant.

Using [PSDA.11](#psda11---bound-the-decision-support-engagement-and-authority-boundary), the team first returns:

> Prepare a pre-season recommendation about the district pumping arrangement for the board's funding consideration. Make affected service concerns, operating conditions, protected limits and material dissent visible. Return a narrower comparison or a statement of the missing premise when the basis cannot support the whole investment question; the board retains the choice.

That is already a useful result. A missing recipient, horizon or authority boundary would stop a stronger engagement claim. Here those conditions are supplied by the example, while the problem formulation remains contested.



### PSDA.Application:1.2 - Preserve the differences that can change an intervention

Operations and finance are readily available. Residents, emergency responders, maintenance contractors, downstream ecology staff and mobility-constrained people may experience different consequences. [PSDA.12](#psda12---recover-participants-concerns-and-affected-systems-for-a-decision-support-inquiry) distinguishes supported consequence paths from possible ones and from unknowns. One residents' association is not presumed to speak for every resident. An evening meeting that some people cannot attend is a participation limit, not evidence that they have no concern.

The resulting concerns support four different formulations through [PSDA.1](#psda1---generate-plural-problem-formulations):

| Formulation | What changes in the inquiry |
| --- | --- |
| Capacity shortage | Examine inflow, available pumping capacity and reliability; added capacity becomes a serious direction. |
| Unequal protection | Examine where exposure and access burdens fall, including reachable assistance; an aggregate hydraulic result is insufficient. |
| Maintenance fragility | Examine spares, staffing, contracting and coordination; a maintenance or staged direction may address a different cause from pump count. |
| Unsafe deployment | Examine placement, traffic, worker and downstream conditions; a restraint or differently bounded direction may be necessary. |

The team does not vote for the one “real problem.” [PSDA.2](#psda2---set-and-reopen-the-problem-boundary) keeps the next flood season, material downstream paths and deployment conditions inside the present inquiry. Long-term redesign and permanent relocation remain outside its present investment return, with their decision-bearing consequences visible. Evidence that no feasible pumping branch serves mobility-constrained residents, or that flood burden transfers beyond the assumed area, would reopen the boundary.



### PSDA.Application:1.3 - Join inquiry and analysis without making one speak for the other

A capacity calculation, an access/deployment scenario and an attributed concern map answer different questions. Through [PSDA.3](#psda3---construct-complementary-situation-and-option-models), the team finds that nominal capacity is not yet the deciding uncertainty. The mobile branch has no qualified arrival-time claim when the main road is unavailable; the concern map also distinguishes property protection from reachable assistance.

[PSDA.4](#psda4---select-problem-structuring-methods-and-combine-them-when-needed) compares capacity analysis alone, a broad open-ended investigation and a bounded combination of attributed inquiry with conditional technical analysis. The bounded combination fits the pre-season return only while attribution can be checked and competent sources can qualify the technical premises. Its join requires the same intervention, service meaning and horizon. Counting how often a concern was mentioned does not produce a numerical value weight.

Through [PSDA.13](#psda13---facilitate-decision-support-inquiry-and-preserve-material-dissent), a proposed sentence changes from “the pumps can protect the district” to a qualified nominal-capacity claim. The separately consulted group asks how assistance remains reachable when roads fail. That correction neither proves a pump inadequate nor disappears because the model does not represent it. The return preserves the two attributed service concerns and the unqualified access premise.

The actual inquiry and analysis can overlap. Suppose the proposed timetable freezes the model before a material service correction can reach the analyst. [PSDA.17](#psda17---reconcile-simultaneous-problem-structuring-and-decision-support-work) compares keeping that freeze, stopping every calculation, and allowing bounded analysis while a supported facilitator maintains the correction channel. Under the case's supplied remit and available analyst/facilitator support, the third arrangement preserves independent calculations and permits the affected claim to be revised before it closes. If a correction or its consequence is still unresolved at the deadline, the board receives that limitation. No meeting order substitutes for the missing result.



### PSDA.Application:1.4 - Use a numerical slice at its actual scope

[PSDA.5](#psda5---generate-decision-alternatives) keeps no-new-purchase baseline `N`, fixed pumping `F`, mobile pumping `M` and unfinished staged proposal `S` visible in the present pumping inquiry. S still needs a specified first intervention before its consequences can be compared. Storage and demand-management leads remain outside this narrower set. The supplied numerical slice covers only `F` and `M`, on illustrative pumping-service-loss and incremental-cost scales:

| Direction | Loss with normal access | Loss with road loss | Incremental cost |
| --- | ---: | ---: | ---: |
| Fixed pumping, F | 2 | 3 | 8 |
| Mobile pumping, M | 1 | 9 | 5 |

These are model values, not monetary prices, measured municipal performance or a complete public-consequence account. Baseline, staged, assistance, protection and other material branches remain outside this calculation.

[PSDA.6](#psda6---represent-values-and-trade-offs) keeps the declared value scheme separate from a participant's concern. [PSDA.7](#psda7---represent-decision-relevant-uncertainty-and-evidence-limits) distinguishes an assumed road-loss probability from an established one. [PSDA.8](#psda8---compare-consequences-of-decision-alternatives) can compare the stated consequences, and [PSDA.9](#psda9---test-robustness-and-sensitivity-of-decision-alternatives-and-their-comparison) exposes a possible reversal rather than hiding it.

In this deliberately stated weighted-loss model, let `p` be the assumed road-loss probability and `λ` the declared cost weight. The two totals are `2 + p + 8λ` for F and `1 + 8p + 5λ` for M. F is lower only when `7p > 1 + 3λ`. With `λ = 0.5`, `p = 0.2` favors M; `p = 0.6` favors F. Neither probability nor the weight has been established for the board's decision. When the missing contribution is a trade-off from expressed consequence comparisons, use PSDA.6:4.5 and its worked construction in :5.5. That deterministic value account alone does not supply preferences over uncertain outcomes.

The result therefore identifies a decision-bearing uncertainty and a conditional comparison. It does not prove that a probability obtains, that assistance is reachable, that a protected condition can be traded away, or that F or M should be bought. More decimal places would not close those gaps.



### PSDA.Application:1.5 - Return the useful comparison and the whole-question blocker together

Using [PSDA.14](#psda14---prepare-and-return-a-decision-support-recommendation), the team returns:

> Retain fixed and mobile pumping for the stated service-loss/cost comparison. Their order reverses under the declared assumptions. A whole-investment recommendation remains blocked by the unqualified access basis, unresolved assistance and protection consequences, and unclosed baseline, staged and other material branches. Keep the separately attributed service concern in the board's return; do not replace it with the calculation.

This completes the recommendation at its stated scope. If further inquiry is being considered, use A.15.9 to compare an obtainable access or consequence result with the useful answer already available, a narrower action, deferral or stopping. Select a request only when its contribution to the board's next decision warrants the whole burden of obtaining and using it within the decision horizon. If selected, the team asks the relevant operations/access or consequence practice for the smallest useful result for this configuration and flood-period window. Each supplying practice qualifies its result through its own Method. A qualified source closing access may leave the value disagreement untouched.

The board's decision to commission further inquiry would be another result. Funding an access study is not funding a pump, and receiving the recommendation is neither consent nor execution.



### PSDA.Application:1.6 - A changed premise changes the right claim

The useful follow-up question is what evidence can reach the board before renewed consideration. [PSDA.15](#psda15---arrange-decision-follow-up-or-reassess-advice-after-a-change) compares an end-of-season review, continuous pump telemetry and a bounded pre-decision evidence arrangement. Telemetry alone cannot settle deployment permission, reachable assistance or the staged alternative. The bounded arrangement is selected in this example only after supplier availability, access, interpretation time and the receiving date are supplied.

In a separate hypothetical continuation, the board authorizes an access study, not a pump purchase. A qualified return establishes that the mobile deployment arrangement assumed in the earlier calculation is unavailable during the required flood-period window. The analyst does not insert a guessed new probability.

The fixed-pump performance claim remains usable for its original conditions. The earlier F/M comparison remains an account of its earlier basis, but cannot support the present investment use. The exact mobile-deployment and consequence premises reopen; assistance, staged and other unclosed branches do not vanish. If a newly identified affected group changes the service meaning, the boundary question reopens as well.

The follow-up has returned an actionable distinction without making the board's choice. Missed observation would instead leave a scoped gap; silence would not mean the premise remained valid.



### PSDA.Application:1.7 - Continue the professional practice only when that is the question

The same episode can expose a different need: another inquiry team may copy a recommendation's format while losing its limits. That is not another pumping calculation. [PSDA.16](#psda16---decide-whether-and-how-to-change-problem-structuring-and-decision-support-methods) concerns a justified repertoire change, and [PSDA.18](#psda18---deliberately-continue-and-change-problem-structuring-and-decision-support-culture) concerns continuation across practitioners.

The fuller constructed PSDA.18 case supplies separate East and West teams, their relevant service assignments, the inquiry and teaching Methods, and distinct March–April occurrences. West's receipt of a permitted packet initially produces an overstrong investment recommendation. Under the case's teaching remit and available support, a guided qualification exercise is selected for that receiving group while the compact route remains for experienced practitioners.

In the exercise, West distinguishes the usable F/M calculation from the unclosed staged and assistance questions. One later independently observed West inquiry retains a corrected concern and the comparison's limits. This supports that bounded receiving use, not profession-wide adoption, long-term retention, a causal teaching effect or an improved flood outcome. The separate late-correction Method proposal remains a proposal; the teaching case does not deploy it.

These practice questions open only because the particular interpretation or working arrangement matters. They are not mandatory activities after every recommendation. The immediate practical gain remains simple: the board receives the useful calculation without losing the people, alternatives and conditions that prevent it from being the whole answer.



## PSDA.Application:2 - APP-PSD-02 — Development-direction advice with unlike holder premises



### PSDA.Application:2.1 - Two useful entries, not one compulsory advising process

The [development-direction profile](#development-direction-advising) connects qualified opportunity, holder, comparison and recommendation results. It is useful when a distinct recommending performer must help a named recipient. The developing holder, paying sponsor, recipient and chooser can differ. Their actual relationship determines what may be shared, relied on or decided.

There is also an earlier independent entry. A person or team can use [Construct a Bounded Development Opportunity (FPF C.40.OCN)](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c40ocn---construct-a-bounded-opportunity) to explore useful future work without asking anyone for a recommendation. Its account can end at a conditional opportunity and a discriminating question. Calling that result “advice” would introduce a different performer/recipient relation rather than merely change its title.

When advice is the question, [PSDA.11](#psda11---bound-the-decision-support-engagement-and-authority-boundary) recovers the engagement and authority boundary. Applicable competence, conflict, confidentiality, informed participation and referral conditions remain professional questions, not a generic permission box. AI used by an adviser also differs from AI being developed. An available tool or fluent generated memo gives neither the service relationship nor its content a warrant.



### PSDA.Application:2.2 - Begin before the target contribution is settled

Suppose an engineering-services unit hears that a new model can handle long records. “Adopt the model” is a search lead, not an accepted problem. Within a ninety-day inquiry, the unit explores neighboring uses, technologies and characteristics under confidentiality, independent-acceptance and service-continuity conditions.

The opportunity Method yields two different accounts:

| Candidate opportunity | Worthwhile receiving question | Dependency and first return |
| --- | --- | --- |
| Help an acceptance engineer recover which claims an evidence package supports. | Could a recoverable claim-to-premise account improve the qualification task without implying automatic acceptance? | Representative, permitted record access is not yet qualified. Retain manual indexing and bounded model-assisted retrieval as conditional directions, with representative tool access still unqualified. |
| Help shift staff recover unresolved exceptions and the next permitted handoff. | Could an understandable exception account improve this receiving situation without autonomous dispatch or loss of fallback? | Representative holder capability, workload and review support are not established. Retain a clearer human handoff and a bounded model-assisted direction, with their missing capability/support basis visible. |

The opportunity return is not a ranking or an adoption recommendation. A positive access disposition would open only the permitted inquiry, not prove the model useful. A refusal would close that processing route, while a public-only sample would support only a narrow demonstration. A possible access probe is a candidate stepping stone toward representative evaluation, not permission to perform it.

The two receiving results differ. A same-result arrangement comparison becomes relevant only after one result, use and acceptance premise is stable enough. Forcing both accounts into one such comparison would hide the still-open choice of useful problem. A generation archive is optional and supplies no value, reachability or authority by itself.

The unit may stop here. If a distinct adviser is later asked which direction to recommend, these accounts enter [PSDA.5](#psda5---generate-decision-alternatives) at their actual conditional strength.



### PSDA.Application:2.3 - A person exploring four months of engineering development

An engineer considers technical evidence review and cross-discipline interface coordination. They can first conduct their own opportunity inquiry. The relevant future work is a contribution they might make, not a job title or course name.

In the example, demand statements explain why both contributions could matter. A permitted evidence set is accessible for the review direction, but capability and transfer into representative work remain unknown. The coordination direction lacks a confirmed opportunity to work with the relevant participants and obtain competent feedback. Neither course attendance nor another person's successful transition fills those gaps.

If the person asks a separate adviser for a recommendation, the return is:

> Retain evidence review and coordination as conditional directions. The present evidence does not establish independent review capability or transfer, and access to coordination practice and feedback is unconfirmed. Neither a course prescription nor a four-month transition follows.

The person's own choice remains separate from an employer's assignment decision. Human demand, assessment, intervention and transfer results retain their direct owners. Career information can help compare opportunities but does not establish a learning effect. If practice time later changes, reconsider the dependent intervention or reachability claim; unrelated organization or AI evidence remains as it was.



### PSDA.Application:2.4 - An organization needs a ninety-day reliability recommendation

A committee asks a separate advisory team which direction to consider for a service organization: internal development, an external provider, or a mixed human–AI arrangement. The committee is recipient and, under the example's supplied mandate, later choice owner. Reliability has priority over throughput for this horizon. Critical-service continuity, security and a bounded reversible-probe budget are protected.

An operating account identifies the recovery contribution; a position/interface account explains the current arrangement; a priority statement identifies the receiving value. None compares all three ways of obtaining the required result. The adviser uses the [single A.15.9 import in the profile](#psdaadvising5---use-the-direct-result-acquisition-method) to look for an adequate existing result and retain the supported answer and its limits. A remaining gap becomes a request only when its obtainable contribution warrants the complete acquisition burden.

The first complete return preserves the useful alternatives and the exact comparison limit:

> Retain internal development, the provider and the mixed arrangement as directions for consideration. The operating, interface and priority accounts remain useful, but do not support their whole-arrangement ranking for the ninety-day recovery result and the security/continuity conditions.

The availability of OCE.8 guidance would not change that return. A Method for obtaining a comparison is not the client's comparison, and the supplier chooses how to produce and qualify its own result.

Now take a separate hypothetical continuation. Adequate whole-arrangement and security results cover the three named directions. They exclude the specified provider because it cannot preserve the security boundary. Internal development remains feasible; a bounded mixed-arrangement probe could resolve whether permitted assistance reduces the recovery queue without excessive verification burden or weakened fallback.

The supplied probe result covers the actual question, distinguishing observations, feasibility, exposure, available resources and stop conditions. Compared with immediate commitment, it supports obtaining that information at bounded cost while retaining internal development. A disclosed material provider interest has also been treated under the agreed service conditions. These are additional premises, not improvements in rhetoric.

Using [PSDA.6](#psda6---represent-values-and-trade-offs) through [PSDA.9](#psda9---test-robustness-and-sensitivity-of-decision-alternatives-and-their-comparison) only where their comparison results are needed, the adviser makes the advantage, serious rival, uncertainty and protected conditions recoverable. Through [PSDA.14](#psda14---prepare-and-return-a-decision-support-recommendation), the return is:

> Consider the bounded mixed-arrangement probe first and retain internal development. The supplied arrangement, probe and security results support this information-gaining recommendation for the named reliability use. Throughput effect remains uncertain. Preserve continuity, security and the budget; reconsider when representative recovery evidence or a relied-on premise changes.

This does not close three directions from an internal/mixed-only comparison: the separate security result explicitly disposes of this provider configuration. Another provider or materially different probe would need its own basis. Delivery, committee consideration, a later authorized probe plan, actual work and observed effect remain distinct.



### PSDA.Application:2.5 - An AI configuration changes while independent advice survives

A team considers model modification, a different scaffold/tool configuration and a changed human–AI allocation. The exact changed object matters: a human training result establishes none of the AI evaluation or deployment-safety premises, and an organization-allocation result does not by itself evaluate a model.

Suppose the committee in the reliability example later authorizes only a bounded probe for configuration A under stated continuity and oversight conditions. An appropriate follow-up arrangement exists: the configuration owner can report material changes, specialist suppliers can qualify them, the adviser has interpretation time, and the committee can receive the revised use consequence.

A notice now identifies configuration B. Observation from B arrives, but the relied-on evaluation still concerns A. [PSDA.15](#psda15---arrange-decision-follow-up-or-reassess-advice-after-a-change) produces a split return:

| Dependent use | What follows now |
| --- | --- |
| Internal-development claim independent of A's evaluation and the changed allocation | Retain it within its original service and horizon. |
| Earlier recommendation concerning A | Preserve it as the earlier conditional advice; do not relabel it as evidence for B. |
| Advice to extend the probe or deploy B | Block that stronger return pending the exact B evaluation, safety/security and allocation premises that matter. |
| Observation and operational response | Use the actual competent owner and applicable continuity or safety rule; a notice alone does not choose fallback, stop service or revoke permission. |

If a generator, candidate archive or open-ended search is itself changing, its actual operators, descriptors, retained candidates and governing policy need their direct account. Calling the holder “OEE” or displaying a front does not supply the missing B result, a worthwhile opportunity or deployment authority.

The observation arrangement is not automatic monitoring created by this text. If an expected result is missed, report the resulting reliance gap. If the decision has ended and no continuing service or protection duty remains, close the follow-up rather than inventing another review cycle.



### PSDA.Application:2.6 - A population without a recipient, and a separate research question

A non-cultural population or lineage has no population-local recipient or chooser in this application. Abstain from attributing a development recommendation to it. Variation, reproduction, selection, persistence and loss belong to the evolutionary account; they are not renamed as the population's choice.

A research team may separately ask which experimental intervention to consider. That is a recipient-owned inquiry only when its scientific question, exact subject, authority, safety and other applicable conditions are established. The population countercase supplies none of those premises. The return may therefore identify the scientific or authorization question that must be answered before recommending an intervention.



### PSDA.Application:2.7 - What remains the same across the branches

The useful common result is a qualified opportunity, comparison or recommendation with a stated receiving question and use. What differs is the premise required to support it. Human transfer, organizational obtaining arrangements, AI evaluation and scientific intervention are not one score or one development mechanism.

A supported direction should not be withheld merely because another branch remains uncertain. Equally, fluency, a method publication, a source bibliography or a favorable score cannot promote an unresolved branch. Follow the [profile](#development-direction-advising) for the full engagement and recommendation contract, the [opportunity Method (FPF C.40.OCN)](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c40ocn---construct-a-bounded-opportunity) for the earlier construction, and the direct patterns for their own results. The [source-responsibility account](#psdasources3---source-responsibility-and-references) keeps that profile's bounded source use separate from application-specific follow-up.



## PSDA.Application:3 - APP-PSD-03 — An on-time report that cannot yet be used



### PSDA.Application:3.1 - Recover the difficulty before naming a solution

A team sends its weekly report before the agreed deadline. The timeliness indicator is green. The planner nevertheless spends time calling colleagues to recover identifiers before assigning the reported work. In twenty rows selected for diagnosis, four need clarification. These observations locate work that the indicator misses; they do not estimate the frequency of the difficulty across the organization.

[FPF B.5.PI](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#b5pi---initiate-inquiry-from-ongoing-work) helps notice this mismatch between formal completion and actual use. The question is whether something prevents the receiving work from proceeding under its applicable requirements. A complaint, a blank field and an adverse working condition are different objects. [FPF C.22.2](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c222---problemcard) can express the problem-side account while its factual and criterion premises remain visible.

For this constructed case, the operations manager may authorize a temporary reporting arrangement for the next planning cycle. The inquiry team may return advice; it cannot change another group's deadline or promise extra work on that group's behalf. [PSDA.11](#psda11---bound-the-decision-support-engagement-and-authority-boundary) keeps that boundary. [PSDA.12](#psda12---recover-participants-concerns-and-affected-systems-for-a-decision-support-inquiry) brings in the planner, report preparers and the people who supply the identifiers. Their accounts can differ: the planner needs usable identifiers by planning time, preparers need an unambiguous rule, and upstream staff may not yet have the requested information.

Through [PSDA.1](#psda1---generate-plural-problem-formulations), retain three formulations with different consequences:

| Formulation | What would make it the current difficulty? | First discriminating check |
| --- | --- | --- |
| The handoff omits available information. | Identifiers existed before submission but the receiving material lacks them. | Compare the source information with the material actually sent and received. |
| Sender and receiver use incompatible identifiers. | Both sides have values, but the receiver cannot map them to the intended work. | Follow one affected identifier through the agreed correspondence and actual processing. |
| The deadline precedes information availability. | The identifier is not knowable at the required time under the current arrangement. | Compare the time information becomes available with the receiving work's real need. |

A fourth possibility is that only the recording is wrong: the receiver obtained usable information, but the register presents an empty field. Inspecting the actual sent and received material can settle that limited question. Correcting the register may then be enough; it does not establish an effect of a reporting rule on operational delay. “Install a CRM” is a proposed means, so it does not replace these formulations.

[PSDA.2](#psda2---set-and-reopen-the-problem-boundary) bounds this inquiry to information needed for the next planning cycle and the burdens of obtaining it. If the real difficulty is that the planning deadline itself has no useful justification, return to that requirement and its owner. Improving compliance with an unsuitable deadline can make the working situation worse.



### PSDA.Application:3.2 - Construct alternatives only where their consequences matter

Suppose the recording check leaves a real obstacle to using the information, and the team asks whether restoring the earlier handoff rule would reduce planning delay. [PSDA.3](#psda3---construct-complementary-situation-and-option-models) retains the concern account and the timeline for their own questions. Use an adequate existing causal model directly. When the causal relations are still missing, [FPF C.28.CM](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c28cm---construct-and-challenge-a-causal-model) constructs the needed contribution.

Fix the outcome and horizon before comparing stories. Let X be the rule actually used for a handoff, M whether the receiving information is usable at planning time, Y the delay in assigning that work, and Z the load during the same period. R records what the register says about completeness; S records whether the row was selected for this investigation. Do not replace M with R merely because R is easier to obtain.

One account proposes X→M→Y: the new rule changed the identifier correspondence, which obstructed use and delayed assignment. Load may also have prompted the rule change and delayed work, giving Z→X and Z→Y. The common cause does not erase the proposed mediated path. Under this model, a correctly applied correspondence repair can remove one source of delay while leaving the load-related delay.

A rival account makes load the cause of both information arriving late and assignment delay: Z→M and Z→Y, with Z→X explaining why the rule changed at the same time. It omits X→M. Returning to the earlier rule then leaves those delays unless it changes another mechanism. These accounts may be combined if both mechanisms operate. Their arrows require process knowledge and evidence; the temporal coincidence of a template change and delay selects neither account.

The useful consequence is now explicit: restoring the rule can change M in the first account but does not do so in the second under their stated mechanisms. Trace an affected identifier and the availability times to challenge that difference. If the disagreement is only about how to present known facts, causal construction adds no result. If the necessary process fact is missing, return that fact request instead of completing a graph by intuition.

Selection also matters. If rows enter the investigation because their information is unusable or their assignment is delayed, both M and Y affect S. Restricting attention to S=1 can create dependence between M and Y even without a causal effect between them. Its direction and size do not follow from the three-node shape alone. Use the whole-path rules of C.28.CM for the chosen graph. Address this selection before using those rows to infer a relation across all handoffs.

Separate the start, persistence and amplification of the episode. A correspondence change may start it; a continuing stream of unresolved rows with no correction owner may sustain it; repeated assignment changes may amplify the rework. These are hypotheses about different outcomes and times, not three interchangeable names for one root cause. When delay feeds future load, represent Y(t)→Z(t+1) with the relevant earlier influences. Do not call an unqualified directed cycle a DAG.



### PSDA.Application:3.3 - Match the proposed action and the evidence to the question

Turning a blank field green changes an indication. Correcting and applying the identifier correspondence changes how information is handed over. [FPF C.28.MR](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c28mr---derive-an-intervention-consequence-by-mechanism-replacement) can derive their different consequences once the mechanisms and intervention are specified. [FPF C.28](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c28---causaluse-cal-causal-use-questions-identification-and-realizability) separately asks what supports the resulting causal claim. A calculated consequence does not establish that the chosen mechanism describes this workplace.

A qualitative distinction may suffice. If the decision needs a quantitative causal effect, [MMP.15](https://github.com/ailev/FPF/blob/main/DPFs/Foundational%20Thinking%20DPF%20Suite/MATHEMATICAL-MODELING-PRACTICE-DPF.md#mmp15---identify-an-intervention-effect-from-available-data) asks whether the effect is identified under the model and available information. Its adjustment, front-door and transport examples develop different ways to obtain or limit an answer.

An externally assigned offer of help is not the same variable as help actually used. For an instrumental-variable argument, MMP.15:4.3.1 derives the binary local effect and :5.4 works through the difference between offer, local-use and population effects. Hernán and Robins, [*Causal Inference: What If*, Chapter 16, §§16.1–16.6](https://miguelhernan.org/whatifbook), provide a fuller discussion of the assumptions and limits. Return with the target effect, the proposed instrument, the grounds for its assumptions, the identifying expression or remaining bounds, and the uncertainty relevant to this decision. For a binary offer and binary use, the difference in mean outcomes between offer groups divided by the difference in use rates is the Wald ratio. Relevance, exclusion and instrument exchangeability are necessary for that argument; those conditions alone do not identify the population average effect. With monotonicity and the chapter's consistency and interference conditions, the ratio identifies the average effect among people whose use changes because of the offer. These people are not simply everyone who accepted help, and that local effect need not answer what universal use would achieve. An invitation that teaches the work independently of use breaks exclusion; a weak change in use makes the ratio unstable. Neither an external-looking event nor four clarified rows supplies the required premises or adequate precision. If this conditional result does not answer the decision, return to the target, information or feasible intervention instead of relabelling it as a population effect.

If an unresolved question still warrants research, [RMP.1](RESEARCH-METHOD-PRACTICE-PRINCIPLES-FRAMEWORK.md#rmp1--decide-whether-a-question-needs-research-and-when-to-stop) frames the exact question and current basis. [RMP.2](RESEARCH-METHOD-PRACTICE-PRINCIPLES-FRAMEWORK.md#rmp2--choose-a-criticism-bearing-research-design-or-stop) compares a useful, feasible design with using the evidence already available and selecting no new study. For a rule comparison, the design must address the load, information availability, timing and selection differences that could defeat its inference. A plan for such a comparison establishes no result of performing it.



### PSDA.Application:3.4 - Give a usable answer while uncertainty remains

[PSDA.5](#psda5---generate-decision-alternatives) keeps alternatives connected to the live formulations: repair the correspondence, restore the former rule, offer temporary clarification, change the deadline where authorized, or retain adequate current work. A rule repair addresses a proposed mechanism; temporary clarification may protect the receiving work while its cause remains unresolved. They are different claims of benefit.

[PSDA.6](#psda6---represent-values-and-trade-offs) keeps the value question visible: timeliness matters because of a receiving use, and the receiving group's convenience does not make unlimited upstream calls acceptable. [PSDA.7](#psda7---represent-decision-relevant-uncertainty-and-evidence-limits) and [FPF C.11.DUA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11dua---make-advice-and-evidence-demands-worth-their-burden) ask which remaining uncertainty can change the current choice and whether obtaining the missing result warrants its burden. A disruptive permanent rule change may need evidence that a temporary workaround does not.

Suppose competent staff can perform one authorized cycle of manual clarification within a specified time budget, and current operational evidence supports its ability to make the required information usable. The manager may choose that bounded help while both causal accounts remain live. Its justification rests on the action's expected contribution, feasibility, costs and limits. Agreement among the models on this temporary action does not prove either model.

If the same arrangement transfers intolerable work to another group, or if usable information still cannot exist by the required time, the temporary option loses that basis. Reopen the comparison or deadline question. Through [PSDA.8](#psda8---compare-consequences-of-decision-alternatives) and [PSDA.9](#psda9---test-robustness-and-sensitivity-of-decision-alternatives-and-their-comparison), distinguish a change that matters only under one causal account from an action that remains adequate across the retained accounts. Return a partial comparison when no current basis selects among the permanent alternatives.

[PSDA.14](#psda14---prepare-and-return-a-decision-support-recommendation) can now return: use the justified temporary help for this cycle; correct any established recording defect; keep the permanent rule choice open until the stated mechanism question is answered or the decision no longer needs it. This is conditional advice, not authority or evidence that the plan was executed.

[EXD.4](EXPLANATION-DESIGN-PRINCIPLES-FRAMEWORK.md#exd4---co-construct-and-repair-an-explanation-in-dialogue) helps explain the decisive distinction and use the recipient's response. A preparer's objection, “that identifier does not exist until Friday,” can change the formulation, deadline premise and recommendation. Repeating the original explanation more clearly would not answer it. Agreement is unnecessary for a useful return that locates the disagreement and its consequence.



### PSDA.Application:3.5 - Reconsider the affected claim after action

For the next cycle, the manager names a person with access to the sent material and processing history to report any recurrence before the following planning decision. Suppose that cycle is again delayed. [PSDA.15](#psda15---arrange-decision-follow-up-or-reassess-advice-after-a-change) first distinguishes what was recommended, what was chosen, what people actually did and what the observations measured. Do not infer non-execution from a bad outcome or execution from a green completion flag.

When the follow-up asks about a reusable working method, [FPF A.3.1.WT](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a31wt---design-and-interpret-a-method-work-trial) records the intended task and actual Work for the stated trial question. The resulting evidence can serve [FPF A.3.1.FT](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a31ft---qualify-method-fit-and-transfer) on fit or transfer and [FPF C.11.MV](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11mv---compare-the-worth-of-a-method-option) on practical worth against current alternatives. One successful cycle establishes none of those broader conclusions by itself.

The return depends on the supported distinction:

| What the follow-up establishes | What to reconsider |
| --- | --- |
| The record described a different event or value from the one needed. | Correct or replace the measurement and revise claims that relied on it. |
| Clarification was performed, but the proposed causal difference did not occur under the model's stated conditions. | Challenge that mechanism or its application; inspect live alternatives before strengthening the claim. |
| The action had its predicted effect but cost more or displaced more important work than the comparison allowed. | Reopen the value, burden or option comparison. |
| The chosen action was not performed, or its actual implementation changed the mechanism. | Address the execution or implementation question; the outcome does not test the unperformed action's effect. |
| The action and model conditions held, but an acknowledged uncertain outcome occurred. | Update the evidence and current choice without treating one adverse outcome as proof that every prior decision was wrong. |

Several explanations may hold together, or the evidence may not distinguish them. Return to the particular record, model, comparison, execution arrangement or formulation whose basis changed. “Poor discipline” cannot stand in for that discrimination, and success cannot certify the whole original theory.

Operational work, temporary assistance and research can overlap in time. The causal graph describes proposed influences. The combination of methods describes which contribution another activity needs. The work history describes what actually occurred and when. Changing the labels on the arrows does not turn one of those structures into another.



### PSDA.Application:3.6 - Make a usable aid for your own inquiry

The report case supplies one connected application. To use the reasoning in recurring work, you may need an aid whose questions colleagues can interpret and answer. Start with a narrow receiving use, such as deciding how to make next week's planning input usable. A ready problem account or a short conversation can be sufficient. Make a reusable form only when repeated omissions or misunderstandings warrant its preparation and upkeep.

The following construction adapts the problem-card and intervention exercises in Anatoly Levenchuk's R4 guide to problem-structuring work. The filled cases are constructed teaching material. They show how to produce and change an aid; they do not establish that completing a form improves workplace decisions or that its reader has learned the method.

**Derive questions from the next use.** Write the action the recipient must be able to take after reading the account. For the planning team, this is to choose a justified next response without assuming that a green timeliness indicator means usable information. Work backwards from mistakes that would change that response. Confusing a register with the received report calls for the actual material and its source. Confusing inconvenience with breach of an agreed requirement calls for the receiving work and applicable criterion. Confusing an explanation with an observation calls for separate support and conjecture. [PSDA.1](#psda1---generate-plural-problem-formulations) supplies the formulation content and material contrasts; it does not require a separate form for every perspective.

A first problem aid for this use can have four sections:

| Section and instruction | Filled report example |
| --- | --- |
| **What receiving work is obstructed?** Identify the work, affected people, occasion and requirement. State the undesirable condition without naming a preferred remedy. | The planner cannot assign four reported items without clarification before this week's planning meeting. Sending by the deadline is insufficient: the agreed input must identify the work to be assigned. |
| **What supports that account?** Separate what someone said, what was inspected, and the conclusion. Identify the cases and source; keep missing or contrary information visible. | In twenty rows selected for diagnosis, the planner requested clarification for four. The sent and received material can be inspected. The selection gives no organization-wide failure rate. Whether the identifiers existed before submission is unresolved. |
| **What else could explain or change the difficulty?** Retain alternatives only where they change the next inquiry or response. Do not require a proved cause to describe an actual obstruction. | Available information may have been omitted, sender and receiver may use different identifiers, or the information may become available too late. A recording defect is also possible until actual receipt is checked. |
| **What would count as useful improvement, and what is needed next?** State the receiving result and constraints; name the next consequential question, not every unknown. | The planner can identify and assign the required work in time without unbounded clarification work elsewhere. Inspect one affected handoff's actual information and availability time before attributing the delay to the reporting rule. |

Each section has a consumer. Evidence limits what can be asserted; alternative formulations change what to inspect; the improvement condition later tests whether an option helps. A heading such as “Root cause” would force an early hypothesis into a settled answer. “Proposed software” would prematurely restrict the option set. Remove such requirements rather than asking users to fabricate entries.

An agent's dissatisfaction can itself be a real difficulty. It does not by itself establish a particular defect, cause or remedy. The aid can therefore retain “the planner reports repeated frustration” while the delivery claim remains unresolved. Conversely, a sentence in a completed form creates no empirical fact. Preserve the source and support of each claim.

**Build the intervention account from the problem account.** Copy only the formulation, receiving result and conditions needed to compare responses. Do not copy a suspected cause into a field labelled “established mechanism.” For each candidate, explain what changes, how that change is expected to help, what it depends on and what observation could require revision. Include temporary help, adaptation or continuation when they are serious alternatives. [PSDA.5](#psda5---generate-decision-alternatives) supplies alternative generation; C.28.CM and C.28.MR supply a causal construction and its consequence when that question is live.

For the report case, the intervention aid can carry these genuinely different candidates:

| Candidate | Proposed change and expected contribution | Conditions and comparison that matter |
| --- | --- | --- |
| Apply a corrected identifier correspondence | Change the correspondence used in preparing and receiving the report. If a wrong correspondence is the operative obstacle, this supplies usable identifiers without repeated manual clarification. | Recover the actual correspondence defect, obtain authority to change both uses and check the material produced. Compare usability and processing delay for relevant cases; a successful example alone does not estimate a general causal effect. |
| Provide one cycle of manual clarification | A competent person obtains and conveys the required information for this cycle. This can protect planning while the explanation of the original failure remains open. | Information must exist in time; the helper needs access and a feasible time budget. Observe whether the planner can use the information and how much work is displaced. Stop or revise if the budget or required availability fails. |
| Change the timing or content of the commitment | Where information cannot exist by the current deadline, obtain an authorized agreement about later completion or a usable preliminary report. This changes the obligation rather than making unavailable information appear. | The receiving work must tolerate the changed commitment. Observe its actual delay and burden, not merely whether the revised due date makes the indicator green. |

Keeping current work remains an option when its present consequences are acceptable under the applicable criteria. It is not equivalent to leaving every question unanswered. A combination also needs its own explanation: temporary clarification may accompany a correspondence repair, but the helper's finite time cannot be promised independently to every measure.

Add a final section, **“What will be compared, by whom, and what follows?”** Bind observations to the intended result and the action actually performed. For example: before the next planning decision, the assigned observer checks the received identifiers, clarification time and assignment delay for the agreed cycle. The observer reports whether the chosen measure was performed and under which conditions. A failed receiving result can reopen measurement, implementation, mechanism or value; use the preceding return table to distinguish those claims. Comparing before and after is descriptive unless a suitable design supports causal attribution.

**Try the aid where a causal story is unnecessary.** A workshop coordinator has promised two sessions on Friday, needing three and two hours of the same room. The room is available for four hours. For this exercise, the sessions cannot overlap or be shortened, no preparation time is needed, and these durations and availability are given facts. The difficulty is not an unexplained fall in productivity: the simultaneous commitments cannot be met under these constraints, because 3 + 2 > 4.

The problem account now names both commitments, the shared room and Friday's window as its basis. “Why are people inefficient?” adds an unsupported cause. The useful next question is whether a commitment or a resource condition may change. One intervention moves the two-hour session to a separately available Saturday slot, subject to participants' and the commitment owner's agreement. Another obtains a second suitable room for those two hours, with the required access and cost acceptable to the responsible parties. Retaining both Friday commitments in the original room is infeasible under the stated premises; a preference score cannot repair that fact.

If either option is selected, the receiving check concerns the actual booking and the preserved session requirements. No new causal graph is needed to establish the arithmetic incompatibility. Whether participants will attend on Saturday is a different empirical premise, which the sum does not settle. If the second room is unavailable, retain the incompatibility result and reconsider the options; do not reinterpret an unconfirmed booking as capacity.

This case changes the aid's explanation section to **“What grounds establish or could change this account?”** It permits a constraint argument as well as causal hypotheses. The intervention section still asks what changes and why that supplies the receiving result. A form that requires a hidden root cause and an experiment for every difficulty would fail this use. For a form intended only for report handoffs, keep the narrower terms and state that boundary instead of expanding it into a universal questionnaire.

**Test the aid and correct the transition that fails.** Fill it with two or three actual or constructed cases within its intended scope, including an unresolved claim. Give a filled account to a colleague without supplying an oral explanation of facts absent from the aid. Ask them to explain the difficulty, the basis for the claims and the next justified move. Their request for an omitted availability time can reveal missing content; inability to interpret “complete” can reveal ambiguous wording; disagreement with an authorized criterion may instead expose a substantive conflict. Do not repair every objection by adding a field or by repeating the explanation.

[FPF C.41.TF](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c41tf---construct-a-checklist-template-that-preserves-its-questions) explains how selected questions, answer meanings and references survive a reusable form and its views. Use it when representation is the difficulty. Return a missing or unsuitable question to its substantive owner. Retain an adequate existing aid when the new version adds burden without changing what the recipient can do.

If learning is the purpose, save the first attempt, explain the correction and try a changed case before claiming independent performance. [HCD.9](Human%20Capability%20Engineering%20DPF%20Suite/HUMAN-CAPABILITY-DEVELOPMENT-PRINCIPLES-FRAMEWORK.md#hcd9---perform-deliberate-practice-with-feedback) supplies practice with feedback; [HCD.10](Human%20Capability%20Engineering%20DPF%20Suite/HUMAN-CAPABILITY-DEVELOPMENT-PRINCIPLES-FRAMEWORK.md#hcd10---choose-whether-and-how-to-vary-space-interleave-or-progress-practice) helps vary the missing operation. A completed template, an intelligible description, a justified intervention and demonstrated capability are different results. This construction can finish with a useful aid and a precise unresolved question without establishing the effectiveness of an intervention or a person's later unaided performance.

## PSDA.Application:4 - APP-PSD-04 — Mira's development direction, programme comparison, and Guide


### PSDA.Application:4.1 - The working difficulty and the first bounded return

Mira is an engineer-manager who prepares release-review handovers. She has four months to improve that work. “Learn more patterns” is her initial idea. Her receiving need is more specific: distinguish an already adequate specialist result from a missing result, select a worthwhile further contribution, and avoid carrying a result into a changed configuration without qualification.

For this case, a qualified HCD practitioner has recovered representative later-Work demand and evidence of Mira's present performance under the available checklist and technical reference, using the target practice's qualified correctness criteria. Mira's responses adequately qualified three of five receiving uses; in the two changed-configuration cases they relied on unsupported transfer. The result concerns those tasks and supports. It does not establish unaided performance, a general mastery score, or transfer to every engineering setting.

C.40.OI bounds Mira, that later Work and the four-month horizon. She needs a first direction question by Friday. Two short discussion sessions are available, but the support owner cannot provide a qualified capacity answer this week. The existing HCD result already supports construction of conditional personal-practice and review-support directions. Mira therefore uses that result now and carries the capacity gap; another meeting would not qualify it. Reopen acquisition when an obtainable answer could change the directions or their use.

Development activity must fit within the existing thirty-eight-hour working week; at most three hours a week can be reassigned, with the displaced activity named. Protected conditions include no disclosure of restricted release data and no unsupported technical acceptance. Mira is the recipient and direction chooser; an employer's staffing decision remains a different use.

C.40.OC replaces “become more mature” with the needed readings:

| Coordinate and scale | Current reading in this case | Intended or protected condition |
| --- | --- | --- |
| Adequately qualified handovers, count out of the same five representative tasks; higher is better | 3/5 with the stated checklist and reference | 5/5 under the intended receiving conditions; a target, not an obtained result. |
| Unsupported technical acceptances, count in that task set; lower is better | 2/5 | Protected: zero in the claimed qualified task set. |
| Total work burden, hours per week; lower within the required output is preferable | 38 | Do not exceed 38; development displaces at most three hours of named existing work. |
| Mentor/specialist capacity, hours per week; lower consumption preserves capacity | Extra usable capacity is unknown. | Confirm the capacity before a direction or programme relies on it. |
| Additional work shifted to release colleagues, hours per week; lower is preferable | None from this proposed change, which has not begun. | Qualify who absorbs or stops the displaced work and the resulting burden; spare capacity is not assumed. |
| Information disclosure, permitted/not permitted for each recipient and purpose; prohibited use is inadmissible | The technical reference and anonymized examples are permitted | No raw restricted release data in the learning or advice service. |
| Transfer to unfamiliar configurations, qualified/unqualified/unknown for a stated task family | Unknown | Obtain HCD and target-domain evidence before claiming that transfer. |

Counts, time, permission and qualification readings answer different questions. Do not sum them into one maturity score or code an unknown reading as poor performance.


### PSDA.Application:4.2 - A complete pattern contribution, not “learn A.15.9”

Using C.40.NU, C.40.PC, C.40.DC, Mira constructs two materially different directions. One is intended to develop her recognition and execution of bounded specialist-result use. The other would change the release-review support arrangement so that a qualified technical reviewer supplies more of that contribution. The second may improve the receiving result without demonstrating new personal capability. Both are more precise than competing course brands.

The first direction cites [FPF A.15.9 — Use or Request a Bounded Result from Another Practice](https://raw.githubusercontent.com/ailev/FPF/main/FPF-Spec.md) as a complete contribution. The recurring difficulty is a missing qualified outside contribution. The move is to inspect an existing result, use it at its supported strength, and retain a material limit. A further request is selected only when its obtainable contribution warrants the whole acquisition burden; the return is qualified for the receiving subject, configuration, use and window. The useful result is a qualified contribution or an explicit limitation. A useful narrower answer can also complete the use; a request itself is not the supplied result.

Mira's intended learner action is therefore observable: given a release question and two specialist reports, decide which report can be used and at what strength, retain a genuine use limit, and obtain a further contribution only when it warrants the work. When acquisition is selected, she drafts its bounded request; she withholds the claim that still lacks a suitable result. The PatternID is an address for that guidance, not a development step by itself. Reading the text does not establish that Mira can perform the described move.


### PSDA.Application:4.3 - Finite directions and a conditional later step

Call Mira's actual checklist-and-reference arrangement `S0`. Direction A adds supported practice of that contribution and later task checks; direction B changes the review-service arrangement. They are compared against the same `S0`, task family, horizon and protections. C.40.JF asks HCD for the person-specific challenge, support, practice and transfer basis, and the service owner for real review capacity. Separately plausible components do not establish joint availability.

| Finite candidate | Receiving result and complete burden question | Transition, reversibility, and options | Present conclusion |
| --- | --- | --- | --- |
| A: `S0` plus supported practice, producing prospective `S1` | HCD must qualify expected task closure and transfer; count preparation, attempts, feedback, retries, checks, mentor work, displacement and total weekly burden. Preserve the critical-error and disclosure constraints. | Setup and later checking remain prospective costs. Identify the cost of stopping the segment and restoring displaced work before claiming reversibility. Later unfamiliar-case practice is an option only if its prerequisite is qualified. | Conditional direction, not a qualified improvement or programme. |
| B: `S0` plus a proposed review-service contribution | The service practice must qualify output, response time, capacity, continuing cost, Mira's coordination burden and effects on other supported teams. The same protected errors and disclosure limits apply. | Establish actual provider availability and withdrawal consequences; retained external support is not unaided personal performance. | Conditional support-direction alternative; do not relabel it personal development. |
| Later unfamiliar-case practice after A | For a planned step, use the stated prospective `S1` and keep its result conditional. For an actual transition, use the `S1` actually obtained and reconsider any difference. Qualify the new task, support, time and transfer evidence from that starting configuration. | Keep the first step's incurred costs in history if it occurred. Compare the next increment separately; do not credit the first gain twice or charge hypothetical setup as spent. | Candidate enabling relation; HCD evidence must support the prerequisite and transfer claim. |

C.11.CRC governs any stronger finite comparison. The result, resource, affected-person/team, distributional and protected coordinates above must be complete on one qualified basis, including interactions and evidence limits. No Pareto or aggregate-savings claim follows from these descriptions. C.40.OP may retain A, B and the conditional later step with their missing-result and reconsideration conditions.


### PSDA.Application:4.4 - Advice and the two distinct choices

Suppose Mira asks a distinct career-development adviser for help. Using PSDA.19, the adviser bounds the service on independently established competence, Mira's participation, confidential individual feedback, an employer-facing summary limited to agreed work implications, and appropriate treatment of provider interests. These are supplied conditions of this constructed scene, not consequences of the sponsor's payment. A private assessment does not become an employer record.

PSDA receives the formed direction question and qualified available inputs. While mentor capacity and transfer remain unresolved, its useful return can retain conditional directions with those limits. A request or recommended probe follows only when its obtainable contribution warrants the whole burden; the missing premises do not establish a winner. In a later scene, assume the required capacity and comparison results have arrived and the authorized choice inputs are adequate. Mira explicitly chooses the personal-development direction A under its stated resource and evidence limits. That choice is a new case fact; neither the opportunity table nor the advice made it for her.

[Compose and Compare Human Capability-Development Programmes for Later Work (HCD.2)](https://github.com/ailev/FPF/blob/main/DPFs/Human%20Capability%20Engineering%20DPF%20Suite/HUMAN-CAPABILITY-DEVELOPMENT-PRINCIPLES-FRAMEWORK.md#hcd2---compose-and-compare-human-capability-development-programmes-for-later-work) now receives the selected development stake, compatible profile, later tasks, participation and qualified support. In this constructed continuation, the HCD practitioner supplies a programme-comparison account for two feasible candidates under those conditions:

| Programme candidate | Qualified resource and support position | Expected contribution and limit |
| --- | --- | --- |
| Coached whole-task sequence | Three learner hours and one mentor hour per week, including preparation, attempts, feedback, correction, retries and checks. The provider confirms that one hour is available. | More of the early attempt receives immediate guidance. Later independent and unfamiliar performance remains to be tested. |
| Reference-supported individual sequence with scheduled expert checks | Three learner hours and half an expert hour per week, including the same categories of learner and provider work. The stated references and checking access are available. | More of the attempt occurs before expert feedback. Error correction and changed-condition checking remain necessary; lower expert time is not an effectiveness finding. |

Both fit within the remainder of the original four-month horizon, with inquiry and choice time already allowed for, and preserve Mira's thirty-eight-hour working-week limit. The supplied account identifies an authorized three-hour reallocation from reporting work that can be suspended without moving it to colleagues or losing a required release output. It includes setup, access, assessment, stopping and restoration costs within the reported allocations; performance expectations and transfer uncertainty remain explicit. These are assumed qualified HCD and organizational inputs, not results calculated by the opportunity inquiry from the table. No unqualified practice attempt authorizes live release acceptance. Unequal description detail, missing displacement or an unconfirmed provider hour would reopen the comparison.

If programme advice is wanted, PSDA uses that HCD.2 account to prepare a separate recommendation. In this continuation Mira makes the authorized programme choice of the reference-supported sequence with scheduled expert checks, using the complete comparison and choice inputs. If advice is not wanted and those inputs already exist, the comparison can go directly to the actual chooser. The earlier direction choice did not select this programme.


### PSDA.Application:4.5 - Guide realization, performed attempts, and evidence

Only after the programme choice does Learning Product practice realize its instructional part as a Guide. [LG.02](#psdasources41---learning-product-source-access) places the first distinction, worked use and later varied return at stable addresses. [LG.05](#psdasources41---learning-product-source-access) develops the focal contribution into recognition, explanation, move, result/check, worked case, contrast and practice. [LG.03](#psdasources41---learning-product-source-access) tests the learner's next action rather than the fragment's apparent polish.

A unit can show a completed bounded request and why one existing report is reusable. Its practice case changes the receiving configuration; Mira must decide whether to reuse, narrow or request, produce the stated result, and check the same conditions. The unfamiliar case must require a fresh applicability decision, not recall of the identifier. These are instructional design contributions; the Guide is not the programme, performed practice, or proof that learning occurred.

In a later constructed observation, Mira completes the scheduled attempts and the assessor qualifies all five familiar tasks with the allowed reference, but one unfamiliar configuration still leads to an unsupported transfer. The observation supports the familiar-task result only under its measured conditions. HCD retains diagnosis, transfer and later evidence. C.40.RQ reopens the stronger unfamiliar-work claim and any dependent path; PSDA.15 receives affected advice. Completing those activities and succeeding on the familiar tasks do not prove general transfer or reduced cognitive load.

The result-use sequence in this branch is:

> HCD evidence → Core opportunity/path candidates → PSDA direction advice when requested → authorized direction choice → HCD.2 programme comparison → PSDA programme advice when requested → authorized programme choice → Learning Product Guide → performed attempts → HCD and representative-Work evidence → affected reconsideration.

These are distinct results, not mandatory stages. The inquiry may stop much earlier.


### PSDA.Application:4.6 - A direct programme-level entry

A learning-product author may already have a Foundations-like HCD.2-grounded comparison of programme variants. PSDA can begin with that comparison and the author's actual recommendation question. No earlier personal opportunity path or direction choice is invented. Audience assumptions support a bounded learning-product design return, not individual fit; a named learner still needs compatible later Work, entry evidence, support and participation for personal comparison. The author's authorized programme choice precedes Guide production, and observed learner evidence remains necessary for effectiveness.


## PSDA.Application:5 - APP-PSD-05 — An engineering company's next development opportunities


### PSDA.Application:5.1 - One receiving question, several kinds of direction

Larch Engineering wants to improve a small industrial monitoring service over nine months while preserving current customer operation. Its operations lead is the recipient of the opportunity account. The governing management arrangement owns any later direction commitment; the inquiry team cannot bind the company. C.40.OI sets a return within two weeks and protects confidentiality, safety and continued service. The team has one day of combined engineering and operations effort available, including preparation and interpretation. Existing qualified service and capacity reports can support a first comparison of directions and expose an impossible overlap. Reviewing them is worth that effort; a new platform benchmark cannot qualify the whole support arrangement in this window. The sufficient return is conditional directions and their limiting dependencies, not a purchase recommendation. If the reports cannot support a needed premise, that gap remains in the return.

The initial proposal is “replace the analytics platform.” C.40.OC recovers the real comparison positions: fault-detection usefulness for the stated customer equipment, false-alarm burden, response time, operator and provider effort, total transition and operating resources, service interruption, security, effects on small and large customers, and future maintainability. Each needs its own scale, polarity, evidence and window. Current readings are supplied by engineering and operations; missing readings remain unknown.

C.40.NU varies more than vendors. C.40.PC tests what receiving problem would make each contribution worthwhile. C.40.DC keeps the proposed result and support arrangement together:

| Direction being constructed | Contribution and support question | Exact external result still owned elsewhere |
| --- | --- | --- |
| Market/use | Could the current service solve a different, evidenced customer problem without changing the platform? | Market and domain inquiry must qualify the receiving need, affected customers and acceptance basis; Strategy owns any market commitment. |
| Technology | Could a different detection component improve the named operating result? | Engineering and AI evaluation qualify that component in the actual equipment/data configuration; safety and security retain their constraints. |
| Human capability | Could operators better distinguish a false alarm from an actionable signal? | HCD qualifies later tasks, current performance, supports, transfer and feasible development; a course title is not that result. |
| Organization | Could a revised escalation and review arrangement reduce missed or incomplete handovers? | OCE compares whole arrangements for the same required result, including provider responsibilities and actual capacity. |
| Provider | Could a specialist service supply the missing contribution? | The provider must supply qualified output, availability, response, dependency and withdrawal conditions; purchase intent is not an operating service. |
| Platform/support | Could data provenance, a simpler interface or a maintained reference make current detection usable? | Systems/Platform Engineering supplies architecture and realizability; OPS supplies continuing operating and support conditions. |

When one same-result arrangement comparison is already the whole question, go directly to [OCE.8](https://github.com/ailev/FPF/blob/main/DPFs/Management%20DPF%20Suite/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce8---compare-human-ai-robotic-and-provider-arrangements-for-the-same-organizational-work-result). The broader opportunity search does not become a required preface.


### PSDA.Application:5.2 - Joint limits and a useful return

Assume qualified local results show that, in the compared arrangement, the technology transition and provider transition each require a distinct six-hour contribution from the same specialist per week. Those tasks cannot share the same hours, and the confirmed shared capacity during their overlap is eight hours per week. Each direction can remain individually plausible. Their concurrent combination needs twelve and therefore fails that joint condition. C.40.JF does not erase the individual results or infer that one must be chosen.

A sequential branch may be retained under C.40.OP, but order alone does not establish enablement. Its second step must start from the first step's actual resulting arrangement, or from an explicitly conditional one if the first is only planned. C.11.CRC requires the branch's complete contribution, transition, operating, affected-customer and protected-coordinate comparison. Specialist hours alone establish neither net benefit nor a preferred programme.

The inquiry returns the receiving problem, differentiated directions, the scope of each existing qualification, the ruled-out overlap and the exact missing sequential-transition result. If responsible advice is requested, PSDA.19 establishes its service conditions and PSDA composes the bounded recommendation. Strategy retains the direction commitment and its revision; OCE retains arrangement change, HCD human development, engineering the enabling systems, and OPS continuing operation.

Suppose a later provider notice removes access to one data class. C.40.RQ inspects the actual dependent directions. It may narrow or retire the provider-supported route while preserving an independently qualified operator-practice opportunity. The provider notice does not itself switch the operating system. Actual protection and operational owners apply their existing duties, and PSDA.15 receives affected advice.


## PSDA.Application:6 - APP-PSD-06 — Unlike subjects, exact recipients, and an anti-case

The common opportunity question does not create one development mechanism. Each branch below can enter construction at a missing contribution. Advice additionally needs an actual recipient, distinct advising performer and adequate service terms.


### PSDA.Application:6.1 - Community and governance

A professional maintenance community wants more reliable transfer of incident experience between participating groups. Its named coordination circle receives an inquiry, under its established limited remit. The Core opportunity Methods can construct possibilities such as changed examples, contributor support, review practice or communication arrangements. Cultural and governance practices qualify participation, transmission, variant retention and intervention claims; FPF C.36 supplies its actual cultural question.

One successful workshop or published pattern does not demonstrate changed community practice. A useful first return is a bounded contribution hypothesis with its unestablished practice effect. An observation or coordination request is a further action only when its attainable contribution warrants the whole burden for this inquiry. If nobody is entitled to receive or act on the requested community-wide advice, return that recipient or authority gap. Do not invent community consent from a meeting attendance list.


### PSDA.Application:6.2 - AI/model or composite arrangement

A service team is the recipient of an inquiry about a named AI-assisted review configuration. The development subject is the specified model, data, scaffold, tools, code, oversight and operating arrangement—not an assumed human-like learner. The Core opportunity Methods can contrast parameter, data, scaffold, tool, evaluation, oversight and non-AI support changes.

The first useful result is a contribution-bearing configuration or an exact AI/engineering evaluation gap. The direct practices own performance, safety, security, data access and operational evidence. A result for configuration A does not qualify configuration B because the provider or model family is the same. Human curriculum, motivation, cognitive-load and transfer mechanisms do not transfer by analogy.

The team's authorized operational owner retains deployment or probe choice. AI helping to draft the advice invokes the adviser's own review and information-use obligations; it does not fill the developing subject's evaluation gap.


### PSDA.Application:6.3 - Engineered platform or facility

A laboratory-platform owner asks which change could improve access to a shared instrument without degrading calibration or safety. C.40.OI bounds the facility configuration, receiving experiments, horizon, users, downtime, calibration and resource protections. Directions may involve scheduling, support, interfaces, a component change or a separate provider.

The smallest result may be a qualified support opportunity or a conditional transition. Systems/Platform Engineering supplies architecture and realization; operations, domain measurement and safety practices supply their direct results. A changed interface may make an existing instrument capability more usable; any claimed new measuring capability still needs its own qualification. Fewer support calls do not prove preserved measurement quality. Missing calibration or safety evidence blocks the dependent use, not every independent facility improvement.


### PSDA.Application:6.4 - Research programme or body of knowledge

An actual research lead receives a question about the next contribution to a reproducibility programme. The subject is the specified research arrangement or body of knowledge, and the intended contribution might be a replicated result, corrected claim, discriminating experiment or reusable analysis.

The Core opportunity Methods can construct and retain those opportunities under a stated horizon and burden. Research and evidence practices own the criticism, reproducibility, formalization, empirical result and inference. A sequence of pattern contributions is prospective guidance, not completed research or a capability finding. If an earlier report is corrected, C.40.RQ follows its actual receiving use; A.10.1 applies when several affected receivers must be discovered. Return the precise evidence question or supported epistemic contribution.


### PSDA.Application:6.5 - Non-cultural population or lineage

In this evolutionary research account, the population has no population-local advice recipient or chooser. PSDA.19 abstains from advice to it. Variation, reproduction, selection, persistence and lineage remain the direct subject of the relevant scientific practices, not a human programme in another vocabulary.

A researcher who asks whether to change an experiment or conservation intervention is a different case. The researcher or authorized organization is the recipient; the population remains an affected subject. Its evidence, welfare/protection conditions, governance and intervention authority must be qualified by their actual owners.


### PSDA.Application:6.6 - What the contrast preserves

Across these uses, keep the identified subject, receiving contribution, horizon, protections, source limits and first useful return. Do not transfer a person's mastery reading, a team's authority, an AI benchmark, a facility's calibration or a research claim into another branch without its qualified receiving basis. When the necessary recipient, meaning, permission or evidence is missing, the useful result can be an exact request, narrower claim or abstention.


## PSDA.Application:7 - Choose development support without assuming an office

This is a constructed illustration; its working conditions are stipulated.

Four project teams repeatedly revise commitments after discovering that estimates depended on an unchecked premise. The director proposes a development office. The receiving question is broader: how can the teams improve how they form, test and revise those premises while current delivery continues? The six-week undertaking is meant to improve the estimation Method and the leads' ability to use and further develop it. Training attendance and creation of a department would not establish those results.

An adviser first distinguishes three explanations: missing technical knowledge, insufficient opportunity to question a commitment, and difficulty constructing a useful inquiry from a weak signal. They imply different contributions. Records and participants' corrected accounts can identify which situations occurred. Establishing which mechanism causes the recurring failure may require a further qualified inquiry; the adviser does not claim that a concern map has established it. Use [PSDA.1](https://github.com/ailev/FPF/blob/main/DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md#psda1---generate-plural-problem-formulations) and [PSDA.2](https://github.com/ailev/FPF/blob/main/DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md#psda2---set-and-reopen-the-problem-boundary) to preserve these differences.

[FPF C.40.JD:4.5](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c40jd45---synthesize-the-organization-from-the-work-and-conditions) supplies the organizational construction: retain the needed local work, then obtain the professional help, common means and wider decisions. [FPF C.32.MWA.PP](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c32mwapp---construct-and-compare-method-performance-and-provision-arrangements) compares whole performance and provision arrangements; [OCE.8](https://github.com/ailev/FPF/blob/main/DPFs/Management%20DPF%20Suite/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce8---compare-human-ai-robotic-and-provider-arrangements-for-the-same-organizational-work-result) develops the organizational choice of human, AI and provider contributions. In this case, existing evidence supports the managers' relevant coaching competence, and each has one protected hour per week for the local work. Specialist help remains necessary for the shared subject question. These are premises of the comparison, not consequences of the managers' titles.

Compare two proposed arrangements for the present horizon. Distributed support uses those managers and a shared specialist. A dedicated office would initially use the same specialist and local practice, adding two weekly hours of coordination; no other specialist has been obtained. The relevant recurring specialist demands are:

| Specialist contribution | Managers with distributed help | Proposed office using the same specialist |
| --- | --- | --- |
| Existing commitments | 2 hours | 2 hours |
| One genuinely shared inquiry session | 2 hours | 2 hours |
| Four distinct case reviews, half an hour each | 2 hours | 2 hours |
| Additional office coordination | 0 hours | 2 hours |
| Total against six available hours | 6 hours | 8 hours |

The shared session is common only because the teams need the same distinction and may use the material together. Their local cases remain separate. Protected team time, permitted material, manager authority and the ability to receive the specialist's result are stipulated as available. The table tests one capacity constraint. In this case, the other premises and the six-hour total make the distributed arrangement feasible.

Under those conditions, the adviser recommends distributed support for the six-week undertaking. The proposed office does not fit the present specialist capacity. Concentrated demand, a genuinely reusable service, another qualified provider or changed coordination costs could alter the comparison. An outside provider whose access and availability are unresolved remains a conditional alternative rather than being silently ranked last. [PSDA.9](https://github.com/ailev/FPF/blob/main/DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md#psda9---test-robustness-and-sensitivity-of-decision-alternatives-and-their-comparison) tests those consequential changes; [PSDA.14](https://github.com/ailev/FPF/blob/main/DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md#psda14---prepare-and-return-a-decision-support-recommendation) carries the bounded recommendation to the director's separate choice.

Suppose confidentiality later prevents the common session. Four separate two-hour sessions would require eight hours, plus two hours of case reviews and two existing hours: twelve in total. The distributed arrangement now fails the same six-hour constraint. Reopen its provision or scope, not the already supported technical distinction.

When a feasible arrangement has been chosen and authorized, the teams still have to perform the work. Observe whether a lead can recover a consequential premise, obtain the missing subject answer and form a qualified commitment in an actual contrasting case. That supplies bounded evidence about the intended change. Decide separately what that evidence supports about the revised Method and the leads' capability, and what a next undertaking would need. [PSDA.15](https://github.com/ailev/FPF/blob/main/DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md#psda15---arrange-decision-follow-up-or-reassess-advice-after-a-change) and [FPF C.40.RQ](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c40rq---requalify-changed-opportunities) govern the affected advice and opportunity returns from changed grounds.

## PSDA.Application:End

# Decision Design Principles Framework Sources and Edition Notes

## PSDA.Sources:1 - Source arguments and refresh

Each full pattern preserves its adopted contribution, serious alternatives, trade-offs and source limitations in SoTA-Echoing. Those arguments govern reuse more precisely than a publication year or an author list. The PSM and decision-analysis studies supply their examined claims and settings; professional sources qualify their own relationships; constructed examples supply transparent demonstrations, not effect estimates.

Use a source result only for its actual subject, configuration and question. When a source or condition changes, recover which inference depended on it, preserve independent grounds and obtain the smallest further result that can change the answer. FPF A.10 qualifies a known reliance; A.10.1 revalidates affected uses when a changed source requires their discovery; G.11 governs the selected currentness question. Actual scientific, legal, engineering and professional conclusions remain with their practices.

Each pattern's SoTA-Echoing section owns its substantive comparison: the working question, selected move, serious rival, trade-off, source limits and observation that would reopen it. Use that argument before relying on a citation. The following map is a return aid, not a second source doctrine, a field census or independent confirmation of the sources it condenses.

| Source-informed contribution | Source line used and substantive limit | Return when the answer changes |
| --- | --- | --- |
| Engagement, participation and revisable framing | Smith and Shaw's 2019 PSM characterization and Kogetsidis's 2025 application review inform the continuing diverse PSM branch. Kelly and Gero 2022, Litster and colleagues 2024, and Nickel and colleagues 2024 inform non-equivalent frames and contextual revision. The bounded reviews and studies supply no universal ontology, representation guarantee or superior protocol. | [PSDA.11](#psda11---bound-the-decision-support-engagement-and-authority-boundary), [PSDA.12](#psda12---recover-participants-concerns-and-affected-systems-for-a-decision-support-inquiry), [PSDA.1](#psda1---generate-plural-problem-formulations) and [PSDA.2](#psda2---set-and-reopen-the-problem-boundary): change the affected receiving-use, participation, formulation or boundary claim. |
| Model, Method and facilitation joins | Marttunen, Lienert and Belton 2017 provide the older critical PSM–MCDA combination anchor; Lami and Tavella 2019 supply an exploratory workshop contrast. Schwarzburg and colleagues 2024 distinguish confidence-related factors from validation. Franco and Greiffenhagen 2018 and Zimmermann and Curran 2023 contribute situated interaction evidence, not guaranteed consensus or general transfer. | [PSDA.3](#psda3---construct-complementary-situation-and-option-models), [PSDA.4](#psda4---select-problem-structuring-methods-and-combine-them-when-needed) and [PSDA.13](#psda13---facilitate-decision-support-inquiry-and-preserve-material-dissent): requalify the particular claim, Method contribution, join or attributed meaning. |
| Alternative construction, values and comparison | Borgonovo and colleagues' 2026 decision-analysis synthesis and Greco, Słowiński and Wallenius's 2025 MCDA synthesis inform selective analytical contributions and preference-model fit. Keeney 2012 is a historical generation ingredient; Marttunen and colleagues 2019 inform disciplined objective simplification. These sources do not supply the engagement's values or warrant one total score. | [PSDA.5](#psda5---generate-decision-alternatives), [PSDA.6](#psda6---represent-values-and-trade-offs) and [PSDA.8](#psda8---compare-consequences-of-decision-alternatives): revisit material alternatives, lost value distinctions or the actual comparison relation. |
| Uncertainty, adaptation and robustness | Lempert and colleagues 2024 connect low-confidence knowledge to decision-relevant inquiry. The 2019 DAPP account contributes pathway timing and failure conditions; the 2026 decision-analysis synthesis informs sensitivity and information acquisition. Scenario membership establishes no probability, and a formal method supplies no local threshold or authority. | [PSDA.7](#psda7---represent-decision-relevant-uncertainty-and-evidence-limits) and [PSDA.9](#psda9---test-robustness-and-sensitivity-of-decision-alternatives-and-their-comparison): narrow the stated range, reopen a reversal or qualify a feasible information question. |
| Professional recommendation and development-direction use | PSDA.14 uses NCDA 2024 within its profession and selected ICMCI v4.0 engagement clauses as a bounded older comparator. The profile's separate source account qualifies the used portions on 2 September 2026, including the ICMCI AI Code v1.0 of May 2026 for AI used by an adviser. That code is not AI-holder evaluation, and the older competence clauses are not represented as the complete latest standard. | [PSDA.14](#psda14---prepare-and-return-a-decision-support-recommendation) and the [profile source-responsibility account](#psdasources3---source-responsibility-and-references): revisit the service or source condition on which the advice relied. |
| Opportunity construction before a settled result | Phillips's 2025 practitioner synthesis informs selective future exploration; NCDG 2024 supplies a bounded human information/alternative contribution; historical value-focused generation is one ingredient. Their combination supports a prospective construction Method, not empirical proof that its opportunities are reachable or effective. | The [opportunity Method (FPF C.40.OCN)](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c40ocn---construct-a-bounded-opportunity) and its source-responsibility account: revise the changed search, dependency, reachability or next-question claim. |
| Follow-up under expected and unexpected change | Lynch and colleagues 2025 contribute domain-specific reconsideration triggers; Manley and colleagues 2026 contribute a perspective on targeted and broader observation. Their natural-resource settings do not set every client's monitoring mix, threshold or institutional response. | [PSDA.15](#psda15---arrange-decision-follow-up-or-reassess-advice-after-a-change): reconsider the affected observation, interpretation, service obligation or recommendation use. |
| Professional Method development | PSM comparisons, Borgonovo and colleagues 2026 and Franco and colleagues' 2021 behavioural-OR synthesis inform contribution-specific repertoire and evidence questions. Kogetsidis's 2026 online review covers selected journals in 2010–2024; publication frequency is neither a practice census nor practical worth. | [PSDA.16](#psda16---decide-whether-and-how-to-change-problem-structuring-and-decision-support-methods): change the specific offering, applicability or evidence claim, not the whole repertoire merely because a paper appeared. |
| Simultaneous inquiry | The older expert/facilitated contrast in Franco and Montibeller 2010, Franco and Nielsen's 2018 workshops, Franco and colleagues 2021 and Cunico and colleagues 2024 support bounded comparisons of interaction and challenge arrangements. They do not make one staffing or participation design universally best. | [PSDA.17](#psda17---reconcile-simultaneous-problem-structuring-and-decision-support-work): requalify the actual interaction and local test; use C.32.MWA only when several structures need a joint synthesis. |
| Cultural continuation | Yearworth's 2024 chapter summaries inform a practice-facing account. Voltan and Kells 2026 remain a conceptual GenAI-assisted proposal requiring practical testing; Czaplicka, Baumann and Rahwan 2025 offer a simplified mediation model. Neither publication, generated output nor a modeled mechanism proves professional uptake or cultural effect. | [PSDA.18](#psda18---deliberately-continue-and-change-problem-structuring-and-decision-support-culture): revise the population scope or the affected claim about receiving interpretation, mediation or continuation. |

Publication years identify sources; they do not by themselves identify a qualification window or show that a claim is still reliable. Older anchors remain useful for the particular contribution named above, while later work can repair their limits. Currentness is bounded to the actual inspected claim and intended use. No table here guarantees continuous monitoring or validates a local case.

## PSDA.Sources:2 - Citation and limits

For this working edition, cite Anatoly Levenchuk, *Decision Design Principles Framework*, 12 October 2026, the named PatternID and the actual publication used. This working text contains eighteen complete Methods and the explanations needed to select and combine their contributions. A pattern address identifies a contribution within that publication; its Markdown fragment follows the actual heading. A changed title or source requires checking its maintained return rather than assuming a title-independent URL.

Cite the title, PatternID and edition actually used, with a permanent link or stored copy when the exact wording matters:

```text
Anatoly Levenchuk, with AI-assisted development and review.
Decision Design Principles Framework.
Working edition, 12 October 2026.
GitHub repository: https://github.com/ailev/FPF
```

For a particular pattern, add its PatternID and title, for example: PSDA.14 - Prepare and Return a Decision-Support Recommendation. Retain the release date, and include a permanent link or stored copy when the exact wording matters.

## PSDA.Sources:3 - Source responsibility and references

The development-direction advising profile uses the following sources, including opportunity-construction premises supplied by Core, for the purposes shown. The cited portions were qualified on **2 September 2026**. Apply each source within the stated limits and reconsider a consequential claim when its source or use changes.

| Source and inspected portion | Selected role and affected content | Limit and local reopen |
| --- | --- | --- |
| [Keeney, Value-Focused Brainstorming, 2012](https://pubsonline.informs.org/doi/10.1287/deca.1120.0251), publisher abstract | Historical generation anchor: explicit values inform alternatives; individual generation can precede group anchoring. Opportunity Method §2. | Not a current-prevalence claim or general reachability theory. Reopen if a stronger generation line changes the inquiry's useful action. |
| [Phillips, Decision Analysis for Practitioners, 2025](https://pubsonline.informs.org/doi/full/10.1287/deca.2025.0356), “Requisite Decision Models,” “Decision Conferences and Workshops,” “Decision Models as Transitional Objects,” “Decision Analysis Technology” | Contemporary practitioner synthesis for purpose-dependent future exploration and selective use of analytical ingredients. Opportunity Method's inquiry/choice separation and source-informed design. | Experience-based account, not validation of this cross-holder construction Method or every future outcome. Reopen on a material limitation of that use. |
| [NCDG 2024](https://www.ncda.org/aws/NCDA/pt/sp/ncdg_home_page), CD2/CD3 | Human-branch alternatives, consequences and qualified current career information. Both human examples. | Does not supply intervention, transfer, organization or AI mechanisms. Reopen the human information-use claims when their source or receiving use changes. |
| [NCDA Code of Ethics 2024](https://www.ncda.org/aws/NCDA/asset_manager/get_file/3395), A.2, A.10 and E.2 | Human career-service participation, assessment competence and referral/closure boundaries. Profile engagement and return. | Profession-specific conditions; applicability must be established. No efficacy, legal or AI-holder assessment conclusion follows. Reopen only affected service claims. |
| [ICMCI competence framework v4.0, 2021](https://www.cmc-global.org/sites/default/files/public/icmci_cmc002_competence_framework_version_4.0_1.pdf), C.1.1–2, C.2.1 and E.3.5 | Agreed consulting engagement content, client involvement and material conflict disclosure. Profile engagement/return. | A verified bounded baseline, not a claim that v4.0 is the latest framework. Reopen when an applicable later clause changes the used service condition. |
| [ICMCI AI Code v1.0, May 2026](https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf), §§1.2, 2.2, 3.1–3.4, 5.1–5.4, 7 | Adds a qualified current source for AI used by an adviser: professional responsibility, material-output checking, data restrictions and client disclosure. | Applies within its stated professional/adoption scope. Does not supply AI-holder evaluation or intervention evidence. Reopen the affected service use, not every holder claim. |

The ICMCI [June 2026 release announcement](https://www.cmc-global.org/content/icmci-launches-global-code-responsible-use-ai-management-consulting) supports the AI Code's publication context. Its professional clauses above come from the Code itself, not the announcement. The [2026 competence-framework update presentation](https://www.cmc-global.org/content/icd-2026) is separately discoverable; the present account makes no claim to have inspected or replaced the entire revised certification framework. The older selected engagement clauses are not represented as a complete current standard.

The [subject-specific supplier account](#psdareference12---obtain-the-result-needed-for-the-developing-subject) explains which result each practice supplies. The [source-change and case-change account](#psdareference13---keep-source-changes-and-case-changes-distinct) distinguishes the consequences of a changed source from those of a changed subject or service condition.

## PSDA.Sources:4 - Source access for the development applications

### PSDA.Sources:4.1 - Learning Product source access

The following sources belong to the Learning Product Development LPF. Their complete texts are not included here, and this publication supplies no verified public retrieval address for them.

| Exact source | Contribution used in APP-PSD-04 |
| --- | --- |
| LG.02 - Проектировать длинный учебный маршрут по устойчивым адресам | Place the first distinction, worked use and later varied return along a learning route with stable addresses. |
| LG.03 - Проверять законченный фрагмент руководства по следующему действию учащегося | Check whether a completed Guide fragment supports the learner's next action and identify the bounded repair. |
| LG.05 - Проектировать учебную единицу, которая учит применять паттерн | Develop a pattern-centred unit around recognition, explanation, action, result/check, a worked case and practice. |

Obtain the applicable source from the Learning Product maintainer when its full instruction is needed. LG.05 is marked Candidate in its source LPF; qualify its applicable use before treating it as established instructional guidance. The constructed application explains the requested design contribution, not the admission of that source. Without the full source or a qualified design result, retain the Guide-design question with Learning Product practice. The opportunity and programme results remain separately usable within their conditions.

### PSDA.Sources:4.2 - Foundations programme source access

**ThinkingFoundations + EngineeringFoundations** is the programme source; **Основания выбора и сравнение программ** is its supporting programme-choice and comparison account, with a source-inspection basis of 2 September 2026. They illustrate a programme design considered before a particular person's development question. Their full working texts are not included here and no verified public retrieval route is supplied.

For that illustration's complete design and comparison, request both sources from the programme's responsible designer or maintainer. For an actual person's programme question, obtain the compatible HCD.2 comparison and the person's relevant starting conditions, later tasks, support and participation. The illustration supplies none of those individual premises. A different adequate programme comparison can enter the same advice or choice question directly.

### PSDA.Sources:4.3 - Predecessor source-account access

**Development-direction profile: source responsibility and local refresh** is the full predecessor source account, whose identified qualification window is 2 September 2026. The public PSDA section [Source responsibility and references](#psdasources3---source-responsibility-and-references) supplies a condensed source-responsibility expression, not that complete earlier account.

Use the public section for the contribution it actually states. If a historical qualification or source-use decision depends on omitted detail, obtain the full named account from PSDA profile maintenance. The source roles above and the supplying Core patterns retain their own bounded reliance; neither a condensed expression nor the source's date supplies an uninspected stronger claim.

### PSDA.Sources:4.4 - A useful stop when access is incomplete

A reader should be able to locate the current question, recover its first useful result or gap, and identify the source or practice that can support the stronger claim. If source access fails, keep the missing premise explicit and preserve independent qualified work. The responsible practice may supply an adequate alternative result, a narrower claim or a blocker. Publication, accessible text, recent dates and well-written examples do not supply the client's evidence or authorization.

## PSDA.Sources:5 - Source grounds for the development applications and their suppliers

These source contributions qualify their stated ingredients and uses. The general opportunity and continuing-development Methods have their own Core bodies; the professional advice and applications here retain the source limits on which they rely.

### PSDA.Sources:5.1 - Opportunity, characterization, and retained possibilities

| Source and relied-on contribution | Use in this framework | Limit and smallest reopen |
| --- | --- | --- |
| [ISO 56007:2023](https://www.iso.org/standard/75068.html): opportunity/idea and concept work before solution development and deployment. | **Adapted** in C.40.OI, C.40.NU, C.40.PC, C.40.DC: independent early inquiry, contrastive search, receiving problem/contribution and prospective support configuration. | Reliance is on its public scope, not an inspected full paid standard or effectiveness evidence. Reopen the affected front-end boundary if that scope or a stronger practice changes it. |
| [Phillips, Decision Analysis for Practitioners, 2025](https://pubsonline.informs.org/doi/full/10.1287/deca.2025.0356): requisite modelling, revisable problem framing and exploration sufficient to move forward. | **Adopted and compared** in C.40.OI: a strong alternative when joint modelling and sensitivity analysis serve the question; adapted to a bounded development inquiry with an optional no-adviser entry. | A practitioner account with cases, not comparative effectiveness evidence for these opportunity Methods. Reopen the bounded-entry choice when direct modelling already supplies the needed result. |
| [Keeney, Value-Focused Brainstorming](https://pubsonline.informs.org/doi/10.1287/deca.1120.0251): generate alternatives from explicit values and avoid early group anchoring. | **Adapted historical anchor** in C.40.NU, joined to current bounded inquiry and source-qualified return. | This earlier contribution is not labelled the whole current SoTA or a universal generation Method. A better contrastive approach reopens the affected search move. |
| [ISO 56008:2024](https://www.iso.org/standard/78485.html): measurement and review for innovation management. | **Bounded comparator** for organization/campaign characterization in C.40.OC. | Organization scope does not supply person, AI or facility measures. Reopen its affected measurement comparison, not every holder branch. |
| Current FPF [FPF E.10.DEV](https://raw.githubusercontent.com/ailev/FPF/main/FPF-Spec.md), [FPF C.16](https://raw.githubusercontent.com/ailev/FPF/main/FPF-Spec.md), [FPF C.11.CRC](https://raw.githubusercontent.com/ailev/FPF/main/FPF-Spec.md), [FPF C.11.DUA](https://raw.githubusercontent.com/ailev/FPF/main/FPF-Spec.md), [FPF A.15.9](https://raw.githubusercontent.com/ailev/FPF/main/FPF-Spec.md), [FPF C.18](https://raw.githubusercontent.com/ailev/FPF/main/FPF-Spec.md) and [FPF C.19](https://raw.githubusercontent.com/ailev/FPF/main/FPF-Spec.md). | Their directly defined semantic recovery, measurement, finite comparison, inquiry appraisal, external-result use and acquisition, archive/front and live-pool contributions are **adopted or adapted** at the body loci named in each pattern's SoTA account. | None establishes a particular holder result. C.19 governs actual live-pool treatment, including under unchanged policy; it is not a local probe selector. A changed definition reopens the dependent opportunity claim. |
| [OECD, Proactive portfolio management in mission-oriented innovation policy, 2025](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/03/proactive-portfolio-management-in-mission-oriented-innovation-policy_6bc6df0e/1ee956a5-en.pdf), sections 2–4: complementary activities, stage dependencies, resources, adaptation and termination. | **Adapted** in C.40.OP's retention, stage-specific comparison and reconsideration. | Its mission selection and funding remain external; it supplies no universal horizon count, individual development mechanism or demonstrated option valuation. Reopen the particular retention or specialist-valuation question. |

### PSDA.Sources:5.2 - Professional and AI-source qualification

| Source and qualified reading | Receiving contribution | Scope limit and return |
| --- | --- | --- |
| [NCDA Code of Ethics, 2024](https://www.ncda.org/aws/NCDA/asset_manager/get_file/3395), A.2, A.10 and E.2. | **Adapted** in PSDA.19's career-service participation, assessment-competence, information-use and referral boundaries. | The identified professional scope does not establish local law or the adviser's actual competence. Determine the applicable service and local requirements before relying on those claims. A changed code or use reopens the affected condition. |
| [ICMCI competence framework v4.0, approved October 2021](https://www.cmc-global.org/sites/default/files/public/icmci_cmc002_competence_framework_version_4.0_1.pdf), identified C.1/C.2 engagement and E.3.5 impartiality clauses. | **Bounded clause reliance** for client involvement and material conflict treatment in PSDA.19. | The official [ICD 2026 page](https://www.cmc-global.org/content/icd-2026) lists an update presentation. Its existence does not make this older framework the complete current standard or establish that the full update was inspected. A complete current certification claim remains outside this reliance. |
| [ICMCI Code of Responsible Use of Artificial Intelligence, v1.0, May 2026](https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf), sections 1.2, 2.2, 3.1–3.4, 5 and 7. | **Adopted within professional scope** in PSDA.19: responsibility, human content review, protected information, competence and material-use disclosure. | Routine tool availability is not warrant. Actual adoption, contract and applicable requirements determine the service conditions. The code does not evaluate an AI development subject. |
| [NIST AI RMF Playbook, MAP 1.1 and MAP 4.1](https://airc.nist.gov/airmf-resources/playbook/map/): receiving context, assumptions, third-party components and support risks. | **Adapted** in C.40.JF and C.40.RQ for configuration-specific joint premises and changed-use effects. | These Map contributions do not provide the client's evaluation, causal result or permission. The source describes RMF revision in progress; this is not reliance on a claimed completed replacement edition. Reopen the affected configuration or source claim. |

For a concrete currentness episode, suppose an adviser needs to know whether “ICMCI compliant” establishes all required engagement conditions. The identified v4.0 clauses support the bounded involvement/conflict contribution, and the May 2026 AI Code supplies a separate scoped AI-use contribution. Neither closes the broader complete-current-standard claim. The visible 2026 update cue returns that precise claim to the professional source owner; the adviser can retain the identified qualified contributions while withholding the broader assertion. Local legal and professional applicability still needs its own result. A newer label alone supplies none of these conclusions.

The [Architectural Reference](#decision-design-principles-framework-architectural-reference) explains the connected language and the consequences of these sources for its use.

## PSDA.Sources:End
