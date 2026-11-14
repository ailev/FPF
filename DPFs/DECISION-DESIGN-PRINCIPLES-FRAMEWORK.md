# Decision Design Principles Framework

**DocID:** `PSDA` within **FPF Library**.

Use this framework to formulate problems, construct decision alternatives and models, and determine how their results can be used in a bounded inquiry or professional engagement.

Anatoly Levenchuk, with AI-assisted development. [Working edition, 24 October 2026](#psdasources2---citation-and-limits). Original and adapted framework text: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Third-party sources retain their own terms.

Start with the result the inquiry needs, such as a formulation, model, alternative, comparison, participation arrangement or qualified answer. Reuse an adequate existing result within its conditions. The Readme gives direct entries, the Architectural Reference explains their connections, and the patterns provide instructions, cases and source comparisons.

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
| [Development-direction advising](#development-direction-advising) | Follow the conditional profile to identify the developing subject, advice recipient and service conditions. |
| [Cross-pattern applications](#cross-pattern-applications) | Work through investment, development and inquiry cases, including advice about subjects other than a person. |
| [Decision Design Principles Framework Sources and Edition Notes](#decision-design-principles-framework-sources-and-edition-notes) | Recover source arguments, specialist returns, citation and changed-use conditions. |

## Pattern index

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| --- | --- | --- | --- | --- |
| 1 | [PSDA.1 - Generate Plural Problem Formulations](#psda1---generate-plural-problem-formulations) | Stable | formulation, framing, rival accounts. Which formulations change how we understand the situation, what to investigate or how to respond? | Relevant inquiry inputs; FPF and subject Methods under their conditions; PSDA.12, PSDA.13 for professional participation when needed. |
| 2 | [PSDA.2 - Set and Reopen the Problem Boundary](#psda2---set-and-reopen-the-problem-boundary) | Stable | boundary, scope, exclusions. What must the inquiry include, and what would justify changing that boundary? | Relevant inquiry inputs; FPF and subject Methods under their conditions; PSDA.12, PSDA.13 for professional participation when needed. |
| 3 | [PSDA.3 - Construct Complementary Situation and Option Models](#psda3---construct-complementary-situation-and-option-models) | Stable | models, claims, assumptions, losses. Which models supply the needed claims, and where do their assumptions or conclusions differ? | Relevant inquiry inputs; FPF and subject Methods under their conditions; PSDA.12, PSDA.13 for professional participation when needed. |
| 4 | [PSDA.4 - Select Problem-Structuring Methods and Combine Them When Needed](#psda4---select-problem-structuring-methods-and-combine-them-when-needed) | Stable | PSM, combination, fit. Which method or combination can supply the missing result? | Relevant inquiry inputs; FPF and subject Methods under their conditions; PSDA.12, PSDA.13 for professional participation when needed. |
| 5 | [PSDA.5 - Generate Decision Alternatives](#psda5---generate-decision-alternatives) | Stable | alternatives, mechanisms, incumbent. Which alternatives can we construct or retain, what can each deliver, and which conditions remain open? | Relevant inquiry inputs; FPF and subject Methods under their conditions; PSDA.12, PSDA.13 for professional participation when needed. |
| 6 | [PSDA.6 - Represent Values and Trade-Offs](#psda6---represent-values-and-trade-offs) | Stable | values, objectives, trade-offs. What matters, and what must not be compensated away? | Relevant inquiry inputs; FPF and subject Methods under their conditions; PSDA.12, PSDA.13 for professional participation when needed. |
| 7 | [PSDA.7 - Represent Decision-Relevant Uncertainty and Evidence Limits](#psda7---represent-decision-relevant-uncertainty-and-evidence-limits) | Stable | uncertainty, evidence, scenarios. Which unknown affects a conclusion, its grounds or the comparison? | Relevant inquiry inputs; FPF and subject Methods under their conditions; PSDA.12, PSDA.13 for professional participation when needed. |
| 8 | [PSDA.8 - Compare Consequences of Decision Alternatives](#psda8---compare-consequences-of-decision-alternatives) | Stable | consequences, comparison, partial order. What follows under the same conditions and declared rule? | Relevant inquiry inputs; FPF and subject Methods under their conditions; PSDA.12, PSDA.13 for professional participation when needed. |
| 9 | [PSDA.9 - Test Robustness and Sensitivity of Decision Alternatives and Their Comparison](#psda9---test-robustness-and-sensitivity-of-decision-alternatives-and-their-comparison) | Stable | robustness, sensitivity, reversal. Where does the conclusion hold or reverse? | Relevant inquiry inputs; FPF and subject Methods under their conditions; PSDA.12, PSDA.13 for professional participation when needed. |
| 10 | [PSDA.11 - Bound the Decision-Support Engagement and Authority Boundary](#psda11---bound-the-decision-support-engagement-and-authority-boundary) | Stable | engagement, authority, recipient. What support does the recipient need, and who holds any decision or implementation authority the engagement depends on? | FPF A.15.9, A.10, C.11; PSDA.12, PSDA.1, PSDA.2 when participation, formulations or scope remain live. |
| 11 | [PSDA.12 - Recover Participants, Concerns, and Affected Systems for a Decision-Support Inquiry](#psda12---recover-participants-concerns-and-affected-systems-for-a-decision-support-inquiry) | Stable | participants, concerns, affected Systems. Whose consequential concern or absence could change the inquiry? | A bounded inquiry question, including one obtained through PSDA.11. FPF A.1.CSD can help identify who bears a consequence. |
| 12 | [PSDA.13 - Facilitate Decision-Support Inquiry and Preserve Material Dissent](#psda13---facilitate-decision-support-inquiry-and-preserve-material-dissent) | Stable | facilitation, attribution, meaning, dissent. What can participants recognize and what remains materially contested? | PSDA.12, PSDA.1 or PSDA.2 when needed, and FPF A.2.9. Use competent sources for specialist claims and the applicable holder for an authoritative decision. |
| 13 | [PSDA.14 - Prepare and Return a Decision-Support Recommendation](#psda14---prepare-and-return-a-decision-support-recommendation) | Stable | recommendation, retained set, request, blocker, abstention. What can responsibly be returned now without taking the choice? | The engagement and qualified results it needs, including applicable PSDA.5–PSDA.9 results. PSDA.11 for a missing engagement boundary. FPF A.15.9, A.10 and C.11. |
| 14 | [PSDA.15 - Arrange Decision Follow-up or Reassess Advice After a Change](#psda15---arrange-decision-follow-up-or-reassess-advice-after-a-change) | Stable | follow-up, observation, interpretation, change. What follow-up is needed, or which advice depends on the changed premise? | PSDA.14 when recommendation follow-up is live; FPF A.10 when the source-to-use account remains implicit or a needed reproducible account is missing; A.10.1 when a material source change requires discovery of affected uses or coordinated revalidation of several known uses; G.11 for currentness; direct subject or service guidance for its own question. |
| 15 | [PSDA.16 - Decide Whether and How to Change Problem-Structuring and Decision-Support Methods](#psda16---decide-whether-and-how-to-change-problem-structuring-and-decision-support-methods) | Stable | Method repertoire, fit, evidence, source refresh. Where does an offering fit, and what grounds support retaining, changing, testing or retiring it? | PSDA.4, any applicable evidence from follow-up, and method-design or evidential results when needed. |
| 16 | [PSDA.17 - Reconcile Simultaneous Problem-Structuring and Decision-Support Work](#psda17---reconcile-simultaneous-problem-structuring-and-decision-support-work) | Stable | simultaneous inquiry, coupling, interference, facilitation. Do these activities interfere? If a change is needed, which arrangement preserves the result at an acceptable burden? | PSDA.3, PSDA.4, PSDA.13 where their contributions interact; FPF C.32.MWA for needed several-structure synthesis. |
| 17 | [PSDA.18 - Deliberately Continue and Change Problem-Structuring and Decision-Support Culture](#psda18---deliberately-continue-and-change-problem-structuring-and-decision-support-culture) | Stable | cultural continuation, interpretation, retention, mediation. How did the practice continue or change across practitioners, and what supports that conclusion? | PSDA.16 and PSDA.17 when current; FPF C.20 and C.36 for their direct cultural claims. |
| 18 | [PSDA.19 - Bound the Development-Direction Advising Engagement](#psda19---bound-the-development-direction-advising-engagement) | Stable | development advice, recipient, service scope, holder premises, refusal. What development-advice service can be offered to this recipient under the professional and disclosure conditions? | PSDA.11, PSDA.14; qualified PSDA results; actual subject practice and professional service conditions. |
| 19 | [PSDA.20 - Explore a Situation through Goals and Dependencies](#psda20---explore-a-situation-through-goals-and-dependencies) | Stable | goals, dependencies, provision, model inquiry. What did this work depend on, or what would the proposal require and which question does that reveal? | Relevant participant accounts and domain knowledge; PSDA.8:4.2.1 for qualitative analysis; PSDA.3, PSDA.5 and PSDA.12 when their contributions are needed. |

# Readme

## Start with the missing result

Two people may use the same word for different problems. Two models can display the same measure yet address different questions. PSDA.1 and PSDA.2 help distinguish formulations and scope. PSDA.3 helps construct the model claims the inquiry needs. With a well-formed question and adequate models, go directly to the missing alternative, value, uncertainty or comparison.

When a proposed change depends on a contribution from others, [PSDA.20](#psda20---explore-a-situation-through-goals-and-dependencies) can help establish who needs the contribution, why, and who supplies or could supply it. Trace a completed episode from the evidence of its participants and work. For a proposal, distinguish the arrangements it would need from those already in use. An omitted condition or a new question can be a sufficient result. The car-park case follows a favourable model result back to conflicting assignments.

If the available proposals cannot deliver a desired consequence, use [PSDA.5](#psda5---generate-decision-alternatives). PSDA.6 can help clarify that consequence and PSDA.8 can help work backward to a different combination of means, then test it under the same conditions.

When the value of a familiar intervention is disputed, PSDA.6 distinguishes attributed concerns, protected conditions and permissible trade-offs. PSDA.8 compares consequences under a declared rule. PSDA.9 examines where the conclusion holds or reverses. A retained set or conditional comparison can answer the question. If a choice is required, it belongs to the authorized decision holder.

If a discussion leaves the inference from reports and opinions unresolved, B.5.SD can help construct it with the contributing expertise the question needs. PSDA.13 can help arrange participation and challenge. A facilitator can also integrate the subject results when competent to do that work. Use a sufficient direct explanation where available.

To apply a method or explain it in ordinary language, identify the objects and differences that matter, the grounds for the findings and what the answer enables. Use available evidence or seek a missing contribution from someone or a service able to supply it.

## A comparison can be correct and still answer too little

In a constructed pump inquiry, rated capacity and access to assistance when roads fail pose different questions. A model can establish a pump's rated capacity while leaving open whether affected people can reach help or a mobile pump can be deployed. PSDA.1–PSDA.3 help identify the corresponding formulations, boundaries and model requirements.

Suppose fixed pumps have losses of 2 with normal roads and 3 when road access is lost, at cost 8. Mobile pumps have corresponding losses of 1 and 9, at cost 5. If `p` is the assumed probability of road loss and `λ` the assumed cost weight, lower scores are preferable. The scores are `2 + p + 8λ` and `1 + 8p + 5λ`. Fixed pumps score lower when `7p > 1 + 3λ`. At `λ = 0.5`, mobile pumps score lower for `p = 0.2` and fixed pumps for `p = 0.6`.

PSDA.6 distinguishes the assumed trade-off from protected service requirements. PSDA.7 identifies the missing basis for the road-loss probability. PSDA.8 supplies the conditional comparison and PSDA.9 its reversal. These calculations leave both assumptions open for the investment decision. The incumbent and a staged alternative may also matter. Return the conditional result or obtain the further premises needed for whole-investment advice.

Suppose evidence now establishes that mobile deployment is unavailable in the required window. The mobile alternative cannot be used there. The earlier comparison remains valid under its original condition and the fixed-pump calculation keeps its stated scope. An analyst can finish with that result. An adviser can use PSDA.14 to explain its implications to the recipient. The investment decision remains with its authorized holder.

## Practical entries

The following entries illustrate advice and inquiry with different stopping points. Use the index or search for another question. The [Architectural Reference](#decision-design-principles-framework-architectural-reference) and its [Architectural Rationale](#psdareference5---why-retain-this-connected-language) explain how the contributions fit together. If you ask an agent for help with a passage, ask for an explanation of what it lets you do in ordinary language.

If the useful future contribution is unsettled, the [C.40.OCN opportunity construction (FPF C.40.OCN:1)](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c40ocn1---problem-frame) can help construct a possibility and identify its next question. A person or team can finish that inquiry for its own use. Where a distinct performer is to recommend a direction to a recipient, use the [advising profile](#development-direction-advising) or the second example below.

### PSDA-CARD-01 — Turn a contested situation into a usable recommendation

- **Situation:** A municipal committee needs advice on a pre-season pumping arrangement. Operations staff emphasize capacity, residents raise unequal protection, and responders question safe access and deployment.
- **Question:** What can the inquiry recommend while preserving those differences and the committee's investment authority?
- **First useful result or blocker:** Attributed formulations and a boundary the team can use. For a recommendation, identify what the conditional comparison supports and what its omissions leave open.
- **Start with:** [PSDA.11](#psda11---bound-the-decision-support-engagement-and-authority-boundary) if the receiving question or authority boundary needs clarification. Otherwise start with the missing participation, formulation, model or comparison result.
- **Stop or return:** Return the supported advice or its limit through `PSDA.14`. Reopen the model, alternative, scope or recommendation that a material change actually affects. The committee retains the investment choice.

In the constructed [flood-pump application](#psdaapplication1---app-psd-01--a-flood-pump-calculation-is-not-the-whole-investment-answer), an independent team prepares advice for a committee. Using `PSDA.12`, the team identifies people whose concerns matter, including those unable to attend. `PSDA.1` distinguishes insufficient capacity, unequal protection, fragile maintenance and unsafe deployment. The team uses their consequences to bound the `PSDA.2` inquiry. It will compare pre-season arrangements, including downstream effects and mobility constraints. Long-term relocation remains outside scope.

The team uses `PSDA.3` to distinguish nominal capacity from access to assistance and the conditions for mobile deployment. With `PSDA.4` it compares a capacity calculation with a combination of attributed inquiry and technical analysis. Combining the results requires evidence that their subjects, conditions and service meanings fit and that the work is feasible. Through `PSDA.13`, participants can clarify why rated capacity alone leaves access open. The concern map identifies questions. Numerical weights require separate value judgements.

`PSDA.5` retains the current arrangement, fixed pumps, mobile pumps and an incomplete staged proposal. The table compares the two pump alternatives using illustrative losses and costs.

| Alternative | Loss with normal roads | Loss with road access lost | Cost |
| --- | ---: | ---: | ---: |
| Fixed pumps | 2 | 3 | 8 |
| Mobile pumps | 1 | 9 | 5 |

With road-loss probability `p`, cost weight `λ` and lower scores preferred, the table gives `2 + p + 8λ` for fixed and `1 + 8p + 5λ` for mobile pumps. Fixed pumps score lower when `7p > 1 + 3λ`. With `λ = 0.5`, mobile pumps lead at `p = 0.2` and fixed pumps lead at `p = 0.6`. Both inputs are assumed. `PSDA.6` distinguishes a trade-off from a protection. Its §4.5 constructs compatible preferences where a judgement is still needed, with a deterministic example in §5.5. `PSDA.7` records uncertainty about `p`, `PSDA.8` supplies the comparison, and `PSDA.9` identifies the reversal.

The `PSDA.14` return can give the conditional comparison. Access, assistance and protection remain unresolved, and the two-row calculation leaves the current and staged options unevaluated. These gaps prevent a whole-investment ranking. Request an additional result through `A.15.9` if its attainable contribution warrants the full burden. Establishing road access would still leave the value trade-off to be settled.

Suppose the committee authorizes a study and a qualified source then establishes that mobile deployment is unavailable in the required window. With `PSDA.15`, revise the current advice that relied on the mobile option or its consequences. Retain the earlier conditional calculation with its original conditions. A newly reported material consequence may also require revising the inquiry boundary. Procuring pumps still requires its own decision.

### PSDA-CARD-02 — Recommend a development direction without taking the choice

- **Situation:** A separate advisory team must recommend a ninety-day reliability direction for a service organization: internal development, an external provider or a mixed human–AI arrangement.
- **Question:** Which direction or information-gaining step do the available premises support, and which claims remain conditional?
- **First useful result or blocker:** The alternatives still in consideration and the limit on their comparison. Suitable further premises may support a direction or a recommendation to conduct a bounded probe.
- **Start with:** `PSDA.11` if the engagement needs definition, or the first missing result among `PSDA.5`, `PSDA.6`, `PSDA.7`, `PSDA.8`, `PSDA.9` and `PSDA.14`. The [profile](#development-direction-advising) and the [development-direction application](#psdaapplication2---app-psd-02--development-direction-advice-with-unlike-holder-premises) explain their connections and cases with different developing subjects.
- **Stop or return:** Give the supported advice with its material limits. Use `PSDA.15` for a real changed-premise or follow-up question, preserving independent claims. The authorized chooser decides whether to commit or probe.

In this constructed case the committee has a mandate, and the advisory service meets the competence, confidentiality and conflict conditions. Reliability takes priority over throughput. Security, critical-service continuity and the probe budget are protected. The operating account describes the needed recovery contribution, the interface account describes the arrangement, and the priority statement gives the value at issue. These support construction of the `PSDA.5` alternatives. A comparison of the three whole arrangements is still missing.

The first `PSDA.14` return retains internal development, an external provider and the mixed arrangement. For the recovery result and horizon at issue it identifies the missing whole-arrangement comparison. Use an applicable specialist result if available. Request a further bounded comparison through `A.15.9` when its attainable contribution justifies its full cost. The supplier chooses how to produce the result. The adviser determines what recommendation it supports.

Now suppose qualified arrangement and security results cover all three directions. The specified provider cannot preserve the security boundary, while internal development remains feasible. A qualified proposal identifies the remaining question, observations that could distinguish the answers, available resources, exposure and stopping conditions. On comparison with immediate commitment, the expected information warrants the bounded cost. Using the relevant value, uncertainty, consequence and robustness results from `PSDA.6`–`PSDA.9`, the adviser can use `PSDA.14` to recommend considering the probe first while retaining internal development. A throughput effect and permission to perform the probe remain open.

For later use of advice about probing AI configuration A, a viable `PSDA.15` arrangement identifies who can report a material change, who can interpret it and how the committee can receive its consequence in time. If observations concern configuration B while the evaluation still covers only A, withhold advice to extend or deploy B until the necessary premises are available. Keep the earlier advice about A and the independent internal-development claim. The notice does not decide the operating fallback or revoke a permission.

A human development case needs different evidence. An engineer considering evidence review or interface coordination may have lawful access to review material while evidence of independent capability and transfer remains missing. Coordination practice and feedback may also be unavailable. Keep the opportunities conditional. Course attendance can establish participation, and an organization-level comparison may describe an arrangement. Neither establishes those individual capabilities.

### PSDA-ENTRY-03 — Find what is wrong when the report is on time

- **Situation:** Weekly reports arrive on time, yet the planner must telephone colleagues to recover identifiers before using them.
- **Question:** Is the difficulty incomplete information, incompatible identifiers, an unsuitable deadline, or a misleading record?
- **First useful result or blocker:** Materially different formulations and what distinguishes them on existing evidence or could distinguish them on an attainable observation, or the missing fact that leaves the discrepancy unresolved.
- **Start with:** [PSDA.1](#psda1---generate-plural-problem-formulations) to compare the formulations. If the discrepancy is already understood and only a recording correction is needed, make that correction through the responsible practice.
- **Stop or return:** Stop when the formulations and available facts answer the question. Examine competing causes when the recipient needs a causal answer or a distinction could change the response. Revisit the formulation if evidence changes what the discrepancy was.

The [report-handoff application](#psdaapplication3---app-psd-03--an-on-time-report-that-cannot-yet-be-used) shows how a recipient’s correction or a later observation can change the diagnosis. It separates a qualified causal account, temporary operating support and research. The three kinds of work can proceed concurrently when each is needed.

# Decision Design Principles Framework Architectural Reference

A useful answer can be narrower than the opening question. A pump comparison may need to distinguish rated capacity from the service that can reach the affected people. A development inquiry may first need to establish which future contribution is worthwhile before considering training or a model upgrade. When that requirement is already settled, use it directly. Decision Design helps the practitioner investigate whichever question remains and return the supported result.

Use these methods to formulate a question, construct a decision model or arrange a professional inquiry. Whoever undertakes the analysis needs the relevant competence, access and any authority the work requires. An analyst may investigate a question independently or draw on a facilitator, affected participants or an adviser for a needed contribution. In development-direction advising, the adviser returns a recommendation to a separate recipient.

The pattern language also helps practitioners maintain the methods and working arrangements on which their inquiry depends. Select a method for the contribution the current question needs.

## PSDA.Reference:1 - The field and its useful result

Decision Design constructs inspectable formulations and representations of situations, possible actions, values, uncertainty and consequences. Its characteristic work is to make a difficult question investigable, construct possible responses and the models needed to examine them, and build a warranted comparison where the premises permit one. It can yield an interpretation, an account of how a model applies, a set of alternatives, a partial comparison, a region in which the conclusion holds, or an answer that draws on several of these contributions. These results can complete an inquiry for understanding or contribute to a professional engagement. Arranging participation, composing qualified advice and reconsidering it are parts of the same practice when the receiving use needs them; an external adviser or final choice is not required in every inquiry.

Use the subject methods for mathematical proof, physical explanation, causal identification, research, literary interpretation or engineering design. PSDA.11–.15 support professional engagement, participation, advice and follow-up when the inquiry needs them. When implementation is required, use the responsible practice and its authority. Leadership helps establish feasible joint contributions.

A *pattern* describes a recurring difficulty and a useful way to respond. A *Method* is a reusable way of doing the work. Use an adequate existing result within its conditions. Open a pattern for a contribution or explanation still needed.

In a contested inquiry, people can disagree about what is wrong, who bears a consequence, what counts as useful service or which evidence matters. Preserve differences that affect the answer, its grounds or a resulting action. Attribute positions and assess their evidence. If claiming agreement, use evidence of how the participants responded. Retain material dissent or an unconfirmed position.

For an already formed question, begin with the missing alternative, specialist premise, comparison or recommendation. An independent opportunity inquiry can finish when it has established the opportunity or its limits.

## PSDA.Reference:2 - How the constructions connect

PSDA.1 develops materially different formulations. Their differences identify evidence needs, intervention mechanisms and consequences a single opening story can hide. PSDA.2 selects and reopens a usable boundary. PSDA.3 constructs complementary models whose claims and omissions fit the question. A model can expose a boundary error, and a changed formulation can make an earlier model unnecessary.

PSDA.4 helps select the problem-structuring or analytical methods that can supply the missing results. It can compare one suitable method with a combination, establish what each part contributes and test whether the results fit together. Allow for preparation and interpretation. PSDA.12 and PSDA.13 supply professional participation and facilitation when needed.

PSDA.5 constructs a live alternative set. PSDA.6 represents values without inferring weights from the frequency of concerns. When the known menu misses a desired consequence, PSDA.6:4.2 distinguishes ends from proposed means, and PSDA.8:4.2.1 can construct a new means combination backward from the desired conditions and test it forward before returning it to PSDA.5. PSDA.7 connects uncertainty to a claim that could change. PSDA.8 compares consequences under the declared rule, and PSDA.9 examines justified variations and reversals. A robustness gap can identify a missing observation. An omitted consequence can require a change to the model or alternative that depends on it.

B.5.SD helps construct an answer from supplied claims. Identify the formulation, model, analysis or professional contribution the answer still needs and use the relevant subject methods to justify the inference. A source-supported explanation, proposed experiment and recommendation have different completion conditions.

[PSDA.20](#psda20---explore-a-situation-through-goals-and-dependencies) supplies one separately usable inquiry through participants' goals and dependencies. It connects the working question, required provision, model views, analysis assumptions and the interpreted answer; an unexpected result can reveal a different problem. PSDA.3 and PSDA.8 remain independently usable model and consequence Methods. Use this whole inquiry only when those connections are part of the missing result.

Select these methods by their result dependencies. A single inquiry can use several. To establish that they form one composite Method, identify the whole action, parts, joins and permitted variation using PSDA.4 and FPF B.1.5.

In a professional engagement, formulation and model construction can change which question is worth answering, whose consequences are considered, what counts as the problem and which interventions become plausible. Decision support uses suitably qualified formulations, alternatives, value accounts and evidence to help a receiving decision. A problem formulation can be a complete useful return before a recommendation is possible; a well-formed question can also enter comparison directly.

[PSDA.11](#psda11---bound-the-decision-support-engagement-and-authority-boundary) establishes the receiving use when that use is unclear. [PSDA.12](#psda12---recover-participants-concerns-and-affected-systems-for-a-decision-support-inquiry) supplies attributed concerns and participation limits, while [PSDA.1](#psda1---generate-plural-problem-formulations) shows how rival formulations change evidence needs, boundaries and possible responses. [PSDA.2](#psda2---set-and-reopen-the-problem-boundary) uses the needed engagement and participation results directly, alongside the formulations, to choose a usable inquiry boundary. Establish who will use the result and how an attributed concern was checked when those facts matter to the inquiry.

Within that boundary, a model can answer one question and expose another. [PSDA.3](#psda3---construct-complementary-situation-and-option-models) makes the contributions and limits of complementary models usable. [PSDA.4](#psda4---select-problem-structuring-methods-and-combine-them-when-needed) compares the ways of obtaining the needed results and qualifies any combination. [PSDA.13](#psda13---facilitate-decision-support-inquiry-and-preserve-material-dissent) helps participants examine the developing meanings and return shared and contested claims. A corrected concern can therefore change a model or reopen the boundary while independent analysis continues. [PSDA.17](#psda17---reconcile-simultaneous-problem-structuring-and-decision-support-work) becomes useful when the actual interaction between these activities threatens their results.

Formulations and models inform the alternative construction in [PSDA.5](#psda5---generate-decision-alternatives). A consequential difference may then need a value account from [PSDA.6](#psda6---represent-values-and-trade-offs), an uncertainty account from [PSDA.7](#psda7---represent-decision-relevant-uncertainty-and-evidence-limits), a consequence comparison from [PSDA.8](#psda8---compare-consequences-of-decision-alternatives), or the conditions under which a comparison holds or reverses from [PSDA.9](#psda9---test-robustness-and-sensitivity-of-decision-alternatives-and-their-comparison). Obtain only the result that is missing. For example, a sensitivity result can expose a missing road-access premise without requiring another round of alternative generation. A new service concern that the option set cannot address gives a reason to revisit that set or its formulation.

[PSDA.14](#psda14---prepare-and-return-a-decision-support-recommendation) connects the qualified inputs to a usable recommendation. It can give a direction, retain a set of options, compare them conditionally, propose a probe, request a missing contribution or explain an abstention. [PSDA.15](#psda15---arrange-decision-follow-up-or-reassess-advice-after-a-change) helps reconsider advice when later observations matter. The [flood-pump application](#psdaapplication1---app-psd-01--a-flood-pump-calculation-is-not-the-whole-investment-answer) shows both the first engagement question and a missing premise that limits the investment recommendation.

### PSDA.Reference:2.1 - Do we need a model, an explanation, research or advice?

Identify what the recipient lacks. These contributions can be used together, but their completion conditions differ.

| Missing contribution | Useful return and supplying Method |
| --- | --- |
| A representation that makes a relationship inspectable | [PSDA.3](https://github.com/ailev/FPF/blob/main/DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md#psda3---construct-complementary-situation-and-option-models) constructs models for named questions and reconciles only their supported overlaps. A model can expose an unknown without settling it. |
| An answer already available in sources | [RMP.1:4.3](https://github.com/ailev/FPF/blob/main/DPFs/RESEARCH-METHOD-PRACTICE-PRINCIPLES-FRAMEWORK.md#rmp143---answer-from-existing-sources-before-starting-a-study) recovers and interprets the relevant material, compares answer-changing alternatives and returns a sufficient answer or precise remaining question. |
| Grounds for an unresolved knowledge claim | [RMP.1](https://github.com/ailev/FPF/blob/main/DPFs/RESEARCH-METHOD-PRACTICE-PRINCIPLES-FRAMEWORK.md#rmp1--decide-whether-a-question-needs-research-and-when-to-stop) establishes whether the question requires research; [RMP.2](https://github.com/ailev/FPF/blob/main/DPFs/RESEARCH-METHOD-PRACTICE-PRINCIPLES-FRAMEWORK.md#rmp2--choose-a-criticism-bearing-research-design-or-stop) constructs and compares obtainable designs when design selection remains open. |
| A warranted account that the recipient can understand and use | [EXD.1](https://github.com/ailev/FPF/blob/main/DPFs/EXPLANATION-DESIGN-PRINCIPLES-FRAMEWORK.md#exd1---establish-and-revise-what-a-recipient-needs-explained) identifies the missing explanatory connection and obtains its subject basis. A missing scientific or mathematical ground returns to that subject work. |
| Professional help with participation, comparison or advice | [PSDA.11](https://github.com/ailev/FPF/blob/main/DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md#psda11---bound-the-decision-support-engagement-and-authority-boundary) establishes the scope and recipient of the engagement and identifies any choice authority it depends on. [PSDA.11–15](https://github.com/ailev/FPF/blob/main/DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md#psda11---bound-the-decision-support-engagement-and-authority-boundary) develop these professional contributions. |

A simulation produces a result under a model and its inputs. Establish the model's applicability before relying on that result for the present subject. Research can finish with a defensible model or explanation. Routine measurement, restoration of a service and acceptance against an established criterion can finish in their own practices without becoming research.

Use a sufficient existing contribution and stop this selection. If two kinds of work are needed, state what one must return to the other.

## PSDA.Reference:3 - Formulation, professional support and choice

A lone analyst can formulate a question and construct a model for their own understanding. A team can compare alternatives for its later decision. A professional adviser can use the same intellectual results within an engagement. For professional advice, establish the service recipient, representation, consent, conflicts, confidentiality and applicable authority from the relationship and its governing practice.

PSDA.11 supplies a bounded engagement when one is needed; PSDA.12 recovers affected Systems, attributed concerns and representation limits; PSDA.13 makes participation and challenge workable and the return faithful. Those results can change the intellectual inquiry. Use participants' corrections when they change the inquiry. Establish support for each subject claim and establish the conditions for participation separately.

Use the general Core opportunity construction C.40.OCN when a worthwhile contribution is not yet settled. It connects useful problems, possible ways, support and conditional reachability. A sufficiently formed analytical question can enter PSDA directly. Strategy supplies direction and commitments; FPF C.11 helps the authorized holder make a later choice. Use RMP when a missing scientific result requires research rather than another representation of current premises.

A concern map can preserve what different participants mean. A hydraulic model can estimate a stated physical consequence. A value account can explain which differences matter to the receiving decision. When combining the accounts, retain the evidence and conditions for each claim.

Likewise, human capability and transfer, organization arrangements, AI evaluation, legal conditions and safety are different questions. This framework helps specify the result needed from each practice and how its absence affects advice. Qualify a source's conclusion for the subject and configuration of the advice before relying on it.

State what each result supports. A description can explain a proposal. To establish which relations already hold, use evidence from that arrangement. A score may inform a choice, which remains with the authorized chooser. Advice for a particular client needs results qualified for that case; an available Method alone does not supply them.

## PSDA.Reference:4 - Qualify the result and its combination

To recognize a useful method, ask which formulation, model or comparison the question needs. To rely on a result, examine the evidence for its claim. A participant's corrected paraphrase can establish what they meant. Their causal explanation needs evidence for the mechanism. A hydraulic calculation depends on its physical premises, and permission depends on an applicable grant or rule.

Check that subject, configuration, time, meaning and source scope fit across the combined results. Assign a probability to a scenario or a weight to a concern only on grounds that support that use. An omitted material consequence limits a ranking. Obtain the missing contribution when its expected use warrants the full cost, or return the narrower answer.

The feasibility and shared-evidence conditions below apply to the whole proposed combination; individually adequate contributions can still fail together.

Use the questions in [PSDA.4, Combine contributions through explicit joins](#psda444---combine-contributions-through-explicit-joins) for the combination you propose. Each supplying result must be qualified for its own claim, fit the receiving subject, configuration, service meaning and horizon, and meet the conditions of joint use. State any conversion that needs additional work: a concern may suggest an objective, but its frequency of mention supplies no value weight; a scenario can condition analysis, but its presence supplies no probability.

Check shared conditions at the scale of the proposed work. Use applicable results already obtained. When participants still need to contribute or correct an attribution, establish how they can do so. Specialist evidence must cover the claim that uses it. Check whether the remaining work, including preparation, interpretation and coordination, fits the available competent effort, access and time. Results drawn from one dataset share that evidence dependence.

In a constructed budgeting variant of APP-PSD-01, attributed concern recovery needs four team-hours, conditional technical analysis needs six, and preparation of the integrated return needs five. These estimates include their preparation and joining effort, require suitably competent staff, and draw on one twelve-hour budget before the board's deadline. The hours cannot be shared or credited to two activities. Every pair needs at most eleven hours, yet the whole needs fifteen. To deliver the whole return by the deadline, find three additional competent hours or a supported way to reduce the work, such as reusing an adequate result. Otherwise agree a narrower answer or a later deadline with the engagement holder. Omitting a required contribution leaves that whole return unsupported. The individual inquiry or calculation can still be useful at its stated scope. These numbers illustrate a joint condition; a real engagement supplies its own estimates and resource rules.

Evidence effort follows the claim someone will rely on. A sketch may locate a disputed service meaning, and a conditional calculation may identify the assumption worth investigating. A recommendation that relies on physical performance, safety, rights or professional competence needs the relevant practice's qualified result. [PSDA.3, Match assurance to the claim being used](#psda345---match-assurance-to-the-claim-being-used) states that boundary. Ask whether an attainable finding could improve the answer or its grounds enough to warrant the work. Obtain it when it can, or finish with the supported result and its limits. Retain a mandatory domain check whenever the intended reliance requires it.

The common practical tension is between obtaining a timely usable answer and preserving the distinctions that can defeat it. More participation can reveal a missing concern while consuming scarce attention. More models can widen the answer while adding interpretation work. A complete ranking can be easier to communicate while requiring judgements the evidence does not supply. State the accepted cost or narrower result, and return to the affected contribution when its conditions fail.

**Constituent actions in ongoing work.** During a decision-support conversation, distinguishing two meanings of a proposal can constitute part of constructing the problem frame, while that framing is part of supporting the pending decision. If the decision concerns allocation of a shared resource, treating each party's local success as the shared criterion can defeat the whole comparison. The facilitator needs the intermediate ability to elicit and compare these meanings, in addition to subject knowledge and the ability to run the meeting. FPF B.1.5.EW explains how an action contributes to both the immediate formulation and the encompassing decision support. Carrying out a resulting course requires the relevant participants, expertise, authority and resources.

State what the present answer covers, what remains open and what could change the conclusion. A partial comparison, a retained pair of alternatives, a narrowly qualified recommendation or an exact request can complete the current question.

Keep protected conditions outside a compensating score when their governing source requires that protection. If the requirement's justification is in question, use [PSDA.6 §4.4](#psda6---represent-values-and-trade-offs) and C.11.DUA: compare its protective contribution with its full burden. State separately what change is justified, whether the requirement remains in force, and how it could be amended.

If plausible variation in the estimates or value judgements used by a comparison or recommendation could change its conclusion, test that variation at proportionate effort through [PSDA.9](#psda9---test-robustness-and-sensitivity-of-decision-alternatives-and-their-comparison). Report whether and under what conditions the conclusion changes. When the response at a central input can hide a consequential nonlinear difference, PSDA.9 section 4.3.1 supplies a small paired-response check. Its constructed equal weights are not actual event probabilities. State when a weight or probability is assumed. A missing premise should block only the claims that need it; independent content can remain useful.

Prepare advice for its intended recipient. The authorized holder makes the later choice or commitment. Use evidence of the plan, work performed and observed consequences for the corresponding claims. New evidence may narrow current advice while earlier choices and work remain part of the history.

## PSDA.Reference:5 - Why retain this connected language

A general choice rule assumes distinctions this work may still need to construct: what the alternatives are, what their consequences mean and which differences matter. A single established analytical method is sufficient when it answers the actual question with adequate premises. A professional facilitation service is sufficient when it already supplies the needed interpretation and analysis. Use whichever of these already supplies the result within its conditions.

This repertoire is useful when the formulation changes the model, the model changes the option set, or the uncertainty and value treatment change what comparison is supportable. Use the constructions separately when one is sufficient. When a connection fails, revisit the contributing work and the conclusions that rely on it.

Problem-structuring traditions contribute rival formulations and contextual boundaries. Decision-analysis traditions contribute alternative construction, preference models, consequences, uncertainty and sensitivity. Each pattern's SoTA-Echoing section gives the grounds for using those sources. Older value-focused generation and PSM–MCDA integration anchors remain historical ingredients; later syntheses can refine their limits. Constructed teaching cases explain the Methods and do not establish universal effectiveness.

This language joins engagement, participation and return Methods with problem-structuring and decision-analysis Methods through their results because a technically sound answer can address an inadequate question, and an insightful reframing can leave the recipient with no usable comparison. Keeping the contributions individually addressable lets a practitioner repair the missing connection without repeating adequate work. It also preserves a direct inquiry result when no later recommendation is required.

Compare the available arrangements for the question at hand.

| Alternative | When it is sufficient or preferable | Why the broader PSDA arrangement may be needed |
| --- | --- | --- |
| Use one qualified calculation or decision model for a fixed question. | The relevant alternatives, consequence meanings, value premises and evidence are adequate, and the calculation answers the receiving question. | A contested service meaning, excluded alternative or unqualified premise can invalidate the stronger return while the calculation remains useful. |
| Use one familiar problem-structuring method (PSM) or facilitated workshop. | Its actual actions and participation conditions fit the required result at acceptable effort. | A workshop can recover concerns without supplying a technical consequence or qualified preference model. PSDA.4 can compare a single Method with a combination and identify a contribution that neither can yet supply. |
| Use separate problem-structuring and decision-analysis accounts. | One account closes the question, or competent practitioners can already qualify the joins. | A reader otherwise has to reconstruct how a frame becomes an objective, which uncertainty changes the comparison, and what advice is warranted. The shared explanation exposes those joins while the bodies retain their distinct Methods. |
| Apply a complete fixed process to every case. | A recurring service has an established Method whose dependencies and conditions fit the present engagement. | A formed question may need only one comparison, while a contested question may reopen an earlier boundary. The PSDA repertoire makes both possible and lets the dependencies of the question determine which methods to use. |
| Use general FPF guidance and the direct subject practice. | The live question is already covered by a choice rule, a bounded evidence request or a specialist Method. | The integrated repertoire retains separately usable formulation and analytical constructions together with the professional work of obtaining suitable inquiry, organizing participation and facilitation, preserving its limits and returning qualified advice. The general distinctions alone do not perform that work. |

The scope also includes improving and continuing this practice. A better way to elicit concerns, a repair to simultaneous inquiry, and the successful transfer of that way to another team are different achievements. PSDA.16, PSDA.17, PSDA.18 preserve their separate questions and evidence. Use them when the repertoire, interaction or continuation is itself at issue.

### PSDA.Reference:5.1 - The development-direction profile and neighboring results


The [development-direction advising profile](#development-direction-advising) is a bounded use of the shared PSDA contributions. Its advice depends on the developing subject's capability, available support, time horizon and professional relationship. A sponsor may differ from the person whose private assessment matters; human transfer evidence differs from an organization's arrangement comparison and from an AI configuration's evaluation. The profile's [guidance on evidence about the developing subject](#psdaadvising4---recover-only-the-relevant-holder-premises), [comparison guidance](#psdaadvising7---compare-for-this-receiving-use), [worked uses](#psdaadvising11---worked-uses-and-stopping-points), and [recognition and assurance account](#psdaadvising12---recognition-assurance-and-practical-gain) supply those narrower answers. Its professional source account retains the actual service boundaries; they do not become entry requirements for every PSDA inquiry.

Core C.40.OCN constructs a useful conditional opportunity before the result is settled. Its full opportunity Methods provide inquiry, characterization, search, problem and contribution, directions, joint reachability, retained possibilities and requalification. PSDA.19 governs the distinct advising relationship, including subject-specific premises and an honest refusal or narrower return. An opportunity can supply decision alternatives, while a formed question with adequate inputs needs no prior opportunity-construction pass. The development-direction profile explains how the adviser uses those contributions within the service.

The [direct-practice boundary account](#psdareference9---direct-neighboring-contributions) identifies the result needed from human development, organization arrangements, technical evaluation and other practices. Such a result supplies a premise for this inquiry; the supplier retains its Method, evidence and conclusion. For example, an organization's qualified comparison of provider and internal arrangements can support advice, while a publication describing how to make that comparison cannot settle the client's case.

The framework supplies professional and analytical Methods with different completion conditions. An analytical result does not establish a professional relationship or the later decision. A claim that a selected combination is one composite Method needs the whole action, identified part Methods, permitted variations and joins specified in PSDA.4. A Part groups reading material; a profile narrows use; a result dependency states what one contribution needs from another.  Reconsider the organization of the language when its field boundary, a profile's independently useful result, or a recurring contribution changes.

### PSDA.Reference:5.2 - Why the source lines are combined


Problem-structuring methods give the framework a substantive answer before optimization begins: make rival interpretations and their practical consequences available for inquiry. Smith and Shaw's [2019 characterization](https://doi.org/10.1016/j.ejor.2018.05.003) and Kogetsidis's [2025 application review](https://doi.org/10.1108/IJOA-08-2024-4746) support a diverse continuing practice, with exploratory and published-application limits. The framing comparisons used in PSDA.1 add the need to make contextual changes visible. The formulation Methods use these contributions to construct materially different formulations and stop when they are sufficient for the inquiry or decision they serve. PSDA.1 compares an initial brief with formulations whose differences affect the answer, its grounds or the next action. The exact comparison and its source limits remain in [PSDA.1, SoTA-Echoing](#psda111---sota-echoing).

The older critical review of combining problem-structuring methods with multiple-criteria decision analysis (MCDA) by [Marttunen, Lienert and Belton (2017)](https://doi.org/10.1016/j.ejor.2017.04.041) makes the interfaces between structuring and analysis part of the problem. The exploratory workshop comparison by [Lami and Tavella (2019)](https://doi.org/10.1016/j.ejor.2018.12.016) provides a bounded counterexample to uniform workshop usefulness. PSDA develops their contributions into the smallest complementary model set and explicit Method joins in PSDA.3, PSDA.4. This costs more interpretation than applying one familiar technique. Retain the cheaper technique when it supplies the required result under the applicable conditions. The reviewed studies qualify the combinations they examined.

The analytical line supplies ways to build alternatives, express values, compare consequences and identify useful uncertainty questions. The [2025 MCDA synthesis by Greco, Słowiński and Wallenius](https://doi.org/10.1016/j.ejor.2024.07.038) informs matching preference information to the comparison and recommendation form. [Borgonovo and colleagues' 2026 decision-analysis synthesis](https://doi.org/10.1016/j.ejor.2025.05.023) connects alternative construction, uncertainty, sensitivity and information acquisition. PSDA.5, PSDA.6, PSDA.7, PSDA.8, PSDA.9, PSDA.14 adopt these as selective contributions: a justified scalar model remains usable, incomplete preferences can leave a retained set, and one missing branch limits the whole recommendation. The recipient may therefore have several supported options or a conditional recommendation to use.

Under unsettled futures, [Lempert and colleagues' 2024 DMDU analysis](https://doi.org/10.3389/fclim.2024.1380054) supports decision-relevant inquiry despite low-confidence knowledge. The older [2019 DAPP account](https://doi.org/10.1007/978-3-030-05252-2_4) contributes pathway timing and failure conditions. PSDA.7, PSDA.9 and PSDA.15 use those distinctions to expose holding regions, reversals and attainable follow-up. Establish probabilities and thresholds from applicable evidence or rules and authority from the governing arrangement. Use a probabilistic analysis when its premises and the question warrant it.

Professional sources add conditions on the return that a technically correct comparison may leave open. PSDA.14 uses selected ICMCI engagement and conflict clauses within consulting and NCDA provisions within human career services. The [profile source-responsibility account](#psdasources3---source-responsibility-and-references) separately qualifies AI used by an adviser. These bounded normative contributions address competence, intelligible reliance and the service relationship. They supply neither a universal advising protocol nor effectiveness evidence for an intervention. The wider [source map](#psdasources1---source-arguments-and-refresh) returns to the facilitation, follow-up, repertoire and cultural-continuation arguments in their own bodies.

Reconsider the affected arrangement when a simpler Method supplies the same useful result under the required conditions, a shared condition or connection fails, a material perspective is lost, or better evidence changes a source contribution. A local case may need a different Method without defeating the whole language. Repeated failures of the same boundary or profile, or a recurring practical need that the existing contributions do not meet, are reasons to reopen the architectural choice.

### PSDA.Reference:5.3 - Decision theory, model construction and engineering trade studies

A chooser may already have adequate options, a consequence model and an evaluative basis. FPF C.11 supplies the choice-theory construction for that situation, including a partial comparison, rejection of the available set or a worthwhile probe. PSDA addresses work that those premises can still need: constructing formulations and alternatives, eliciting and representing preferences, retaining uncertainty at its supported kind, building consequence accounts, and composing a return for its actual use. Apply a sufficient C.11 result directly when the premises are already adequate. PSDA.6 develops the preference input where it is missing, including a finite lottery-based construction in :4.5.6; PSDA.8 connects it to the subject's consequence model. C.11 retains the general choice question. For a probabilistic information question, MMP.16 develops the comparison of actions before and after an attainable observation under its possible outcomes, and PSDA.9 applies that result to the engagement.

The general construction suppliers also retain their own questions. C.38 constructs comparable ways to obtain one result; PSDA.5 can construct alternatives that pursue different results or answer different formulations. C.39 develops a missing obtaining operation or connection. C.40 develops branching search from reusable material, while C.40.OCN connects opportunity inquiry, problems, directions and conditional reachability. A PSDA inquiry supplies the actual formulation, elicitation, modelling and professional operations. Use the relevant subject practice for its unresolved premise.

C.11.CRC supplies finite configuration-relative contribution comparison when baseline, interactions and the whole change matter. C.11.DUA appraises further advice or evidence work by its attainable receiving value and full burden. C.11.DBR supplies reconsideration after a relied-on decision basis changes. PSDA.8, PSDA.14 and PSDA.15 use these constructions for their respective questions while retaining the professional interpretation, recommendation and observation arrangements. B.5.SD supplies joint substantive answer construction; B.5.RA and B.5.RR retain argument recovery and changed-reasoning operations. A discussion needs only the contribution absent from its present answer.

In engineering, [Decide and Reopen the Engineering Architecture (SYSE.6)](Engineering%20DPF%20Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md#syse6---decide-and-reopen-the-engineering-architecture) binds an architecture decision to the engineered System, selected structures, configurations, operating conditions, qualified engineering evidence and later realization Work. A comparison or recommendation can supply its premises without taking that decision or proving realization. [NASA's decision-analysis account](https://www.nasa.gov/reference/6-8-decision-analysis/) joins criteria, alternatives, evaluation and uncertainty with a recommendation, at rigor proportionate to the decision. [SEBoK Decision Management](https://sebokwiki.org/wiki/Decision_Management) explicitly connects engineering trade studies to decision-analysis mathematics, value-focused alternative generation and the system lifecycle. These connections permit reuse; the engineering Method retains its subject-specific result and conditions.

[Phillips's 2025 practitioner treatment](https://pubsonline.informs.org/doi/10.1287/deca.2025.0356) distinguishes formal decision-theory ingredients from model construction with clients, including framing, objectives, alternatives, interpretation and sensitivity. The practitioner can use participation to correct the technical model and model results to reopen a framing or interpretation. Phillips offers a practitioner argument and case evidence. Qualify the resulting model against the evidence for its claims.

Machine-learning decision models raise another construction question. For example, [decision-focused learning](https://doi.org/10.1613/jair.1.15320) combines learning with constrained optimization and trains the learned component for the resulting decision quality. A model that contributes to generating an action need not be an analysis of supplied options. Learning, optimization and deployment each depend on their computational and empirical conditions. This framework can help construct their problem, value and consequence premises or interpret a qualified result; its formulation and professional-inquiry Methods do not supply the missing training or deployment procedure. A normative choice rule, a constructed model, a learned action-producing arrangement and the later authorized decision are different contributions.

### PSDA.Reference:5.4 - One bounded language and its wider connections

The shared subject is construction, interpretation and responsible use of problem formulations, decision alternatives and models in a bounded inquiry. **Decision Design** names that constructive practice. Here responsible use means an intelligible return, justified reliance within its conditions, and reassessment when the basis changes. Whoever has the required authority makes the choice or commitment. The responsible practice carries it out when implementation is part of the work. The arrangement is useful when a changed concern alters a formulation, a formulation changes the alternatives or models, or an uncertainty result changes what comparison or recommendation is warranted. Qualified participation is consequential within these constructions; it is not merely preparation for presenting a finished calculation. The language keeps the associated professional Methods and independently usable analytical constructions together so that the reader can obtain and revise these connections.

Judge the combined result by whether it answers the receiving question and whether the recipient can recover and revise the formulation, model, value, evidence and participation grounds it relies on. An accurate calculation can answer an inadequate question. A faithfully facilitated discussion can still lack a warranted consequence model. Sections 2–4 show how to locate a missing contribution.

The practice can continue through a different model family, elicitation technique, facilitator, tool or source while the resulting contributions and the way they inform the answer remain usable. A revised preference method need not invalidate a sound boundary construction, and a changed participation condition need not alter valid arithmetic. PSDA.16–.18 address repertoire, interacting inquiry and continuation when those are the current questions.

Professional sources indexed under Operational Research connect further contributions. The OR Society's [methods account](https://www.theorsociety.com/ORS/About-OR/OR-Methods.aspx) includes optimization, simulation, stochastic modelling and decision analysis; its [Problem Structuring Methods account](https://www.theorsociety.com/ORS/Community/SIGs-List/Problem-Structuring-Methods.aspx) describes interpretative model-building for contested situations and connections with other MS/OR contributions. This framework covers the formulation, model and professional-inquiry questions developed in its Methods. It supplies no complete optimization, simulation or stochastic-system repertoire. Treat a claim of disciplinary membership as a separate question about the relations among these practices. The practice-development methods here concern the bounded inquiry described above.

This subject is narrower than either a comprehensive science of decisions or the design and operation of an arrangement that repeatedly makes operational decisions. Decision Management can name a lifecycle process, as in the engineering account above, or the construction and maintenance of operational decision systems. [OMG Decision Model and Notation](https://www.omg.org/dmn/) contributes precise business-decision and rule models to the latter setting; such models can be used with process and case models. Their implementation, operation and change require contributions beyond this framework. A qualified formulation or recommendation can supply those practices without replacing them.

Separate problem-structuring and model-construction frameworks could make independent source communities and change boundaries more visible. Here their connected inquiry account remains in one language, while direct entries and source-specific revision conditions preserve useful independence. A broader Suite account becomes useful when a supported disciplinary whole explains additional model/intervention connections that the current user needs, or when separately maintained languages provide a material advantage. The useful formulation, model and professional contributions remain available without first settling that wider arrangement.

The present language can supply qualified formulations, value and uncertainty accounts, comparisons and bounded advice to a wider inquiry. Engineering, management, policy and personal decision work can use those results. Such use establishes the supplying and receiving questions, not membership of the entire field in Engineering or Management. Domain architecture, scientific inference, implementation and the authorized choice retain their own Methods. Use an adequate specialist result directly.

## PSDA.Reference:6 - Continue and change the practice

When a source or receiving condition changes, identify the dependent claims and preserve earlier findings for the uses they still support. A corrected concern, altered access or new model configuration may change the answer or its grounds. Use an applicable observation or obtain the missing evidence when needed. A change notice can establish a new configuration. Claims about its safety or effectiveness require the corresponding evidence.

Use [PSDA.16](#psda16---decide-whether-and-how-to-change-problem-structuring-and-decision-support-methods) to assess an offering for recurring work or justify a change, [PSDA.17](#psda17---reconcile-simultaneous-problem-structuring-and-decision-support-work) to establish whether simultaneous activities interfere or to resolve an identified conflict, and [PSDA.18](#psda18---deliberately-continue-and-change-problem-structuring-and-decision-support-culture) to establish how practice was transmitted, used, retained or lost across practitioners, or consider how to continue it. An independent intellectual inquiry can use the general Method-development and cultural-reproduction guidance directly. A sufficient calculation or recommendation can complete its own inquiry.

The useful gain is the ability to reconstruct a consequential distinction, obtain the model or comparison the question needs, and state the conclusion it supports. Successful communication, accepted advice and realized outcomes remain separate results. When the basis changes, use the source that can support the affected claim and retain contributions from earlier work within their limits.

## PSDA.Reference:7 - Whose conditions and evidence shape the answer

The sponsor's first question, the participants who can attend, and the analyst's familiar models all affect what is made visible. Identify the sources of attributed concerns, any affected parties left unrepresented, including those who did not participate, any material consequences omitted, and how a material correction can reach the result. PSDA.12 and PSDA.13 provide that work. More participation does not make all claims equally supported, and a dissenting position has only the practical or institutional effect justified in the case. Domain rules determine a right, duty or protected condition.

The worked applications emphasize institutional investment and development advice. They are constructed teaching cases, and the source studies have their own populations, professional settings and access limits. A practitioner transferring the guidance must qualify local meanings, communication access, evidence and service conditions that can alter use.

## PSDA.Reference:8 - Questions before relying on a combined return

The opening and direct entries help recognize the first useful action. Assurance asks whether the result is supported for its intended reliance. Use the checklists for the selected methods. Reuse their qualified answers when subject, content, receiving use and conditions still fit. Assess the combination against the questions below.

- Can the recipient recover what this return answers, which use it serves, and what remains outside it? An early inquiry may end with a formulation or precise question.
- Do material concerns, competing frames and boundary choices survive into the models, alternatives and comparison that depend on them? A supported correction must reach the claim it changes.
- Does each relied-on result cover the needed subject, configuration, meaning and horizon, with the limits of its evidence? Have shared assumptions or sources been counted only for the support they supply?
- Do the selected Methods meet the [joint conditions](#psdareference4---qualify-the-result-and-its-combination), including total effort and required interpretation? Feasibility of each pair does not establish that all the required work can be done together.
- Does the scope of the recommendation match the alternatives and conditions examined? In APP-PSD-01, two pump options can be compared conditionally while the whole investment question remains open. In APP-PSD-02, a qualified provider exclusion can close that branch, while an unexamined provider cannot simply disappear.
- Is a missing input worth obtaining, and when can this inquiry finish? Can the recipient identify which advice a changed premise would affect? If a later choice or action is needed, who is authorized to take it? In development advising, establish the relevant service conditions and the evidence about the developing subject.

These questions address failures shown in the applications: one service phrase hiding unlike concerns, an unjustified conversion of qualitative meaning into a score, and a partial comparison presented as a whole recommendation. Correct the particular meaning, obtain the missing contribution or narrow the return. Give the recipient the account needed for this use. Establish performance and later effects from evidence of the work or outcomes in question.

## PSDA.Reference:9 - Direct neighboring contributions

Within PSDA, engagement, participation, facilitation, recommendation and professional continuation are available through the Methods identified in the pattern index. Leadership supplies contributions and effective commitments. Core C.40.OCN constructs a bounded opportunity and C.40.OD connects knowledge or Method growth to continuing development. Research Method Practice helps investigate an unresolved knowledge claim when existing premises and evidence cannot answer it. Strategy supplies strategic direction, choice and portfolio commitments. Those neighboring contributions retain their own subjects and conditions when a PSDA application needs their results.

Use a direct source when it owns the whole current question. If a chooser already has an adequate option set and needs only their own decision, use [FPF C.11](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11---decision-theory-decsn-cal) or the applicable domain decision rule. If an engagement needs just one missing specialist result, [FPF A.15.9](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a159---use-or-request-a-bounded-result-from-another-practice) gives the bounded inspect, reuse or request entry.

| Needed contribution | What PSDA can do | What it does not supply |
| --- | --- | --- |
| Human capability demand, diagnosis, intervention or transfer | State which person's later Work and which advice premise need a qualified result; use the direct human-practice entry named in the development profile. | A diagnosis, effective curriculum, learning effect, occupational opportunity or demonstrated transfer from a course title or general guidance. |
| Organization, operating or provider arrangement | Specify the result, configuration, use, horizon and acceptance question to compare; retain independent alternatives when one premise fails. | This client's whole-arrangement comparison, implementation capacity or authority from a position description, operating account or published Method. |
| AI/model or other technical evaluation and safety | Identify the configuration and intended use, select a result request when its attainable contribution to the answer or its grounds warrants the cost, and reconsider only advice that depends on a changed premise. | Evidence for configuration B from A, deployment permission from an evaluation, or practical reachability from novelty or an archive label. |
| Physical, scientific, financial, legal, ethical, safety or governance facts and rules | Identify the premise, its applicable source or decision holder, its period of validity and its effect on the answer. | A local threshold, mechanism, permission, professional duty or protected condition by analogy with another field or holder. |
| An evolutionary population or lineage | Recognize the absence of a population-local recipient and choice owner in the represented case. | A development recommendation to that population. A researcher selecting an intervention has a separate question, scientific basis and authority. |

A published method can explain how to obtain a result while the case-specific evidence is still missing. Use an existing qualified result or establish the premise from the available evidence. Seek a missing contribution when an attainable answer can improve the current conclusion or its grounds enough to justify the work.

A real application must qualify the relied-on content for the stated subject, configuration, receiving use and horizon. [FPF A.10](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a10---evidence-graph-referring-claim-bound-evidence-and-provenance-graph) helps recover an implicit source-to-use account or a needed reproducible account that is missing. Use an adequate explicit account directly. The relevant domain practice governs the claim itself. Discovery, availability, evidence, applicability and authority are different questions.

## PSDA.Reference:10 - What this framework covers

Use Decision Design to formulate problems and construct or interpret decision models, independently or in a professional engagement. Its methods cover boundaries, complementary models, inquiry through goals and dependencies, method selection and combination, alternatives, values, uncertainty, consequences and robustness. They also address engagement, participation and representation, protected facilitation, qualified recommendations, follow-up, repertoire, simultaneous inquiry, cultural continuation and development-direction advice. A recommendation, request, narrower answer or reasoned abstention can complete the inquiry. Any subsequent choice belongs to its authorized holder.

Core C.11 supplies the decision-theory construction, C.40.OCN supplies general opportunity construction, and B.5.SD supplies joint substantive answer construction. The practitioner obtains their results when those questions are live and qualifies the joined use. Reuse an adequate result when it fits the inquiry.

PSDA.12 and PSDA.13 remain full professional Methods: participation channels, representation, attributed concerns, facilitator interests, consent, confidentiality, coercion protection and faithful return require their actual relationship and conditions. A correct model does not supply them.

The development-direction profile explains a connected use; PSDA.19 supplies its separately reusable advice Method. The applications preserve the distinction between a useful opportunity, an analytical result, a recommendation, programme choice, learning design and actual performance. They are constructed teaching cases. Claims about implementation or effects require evidence from the relevant setting. An opportunity inquiry without an adviser can finish at its own result and does not invoke a service merely because it appears in a professional application.

## PSDA.Reference:11 - Change only what the new basis changes

Retain the source and conditions behind each premise that a conclusion or recommendation relies on. When a source changes, revisit the advice that relied on it and state any revised limit. The [source responsibility and references](#psdasources3---source-responsibility-and-references) below identify the qualified sources and explain which claims to reconsider.

When a source, configuration or receiving condition changes:

1. Identify the claim that used it and whether the new information concerns the same subject and use. A change notice can establish what changed. Check whether it also supplies the evidence needed for the new use.
2. If the source is unchanged but the subject conditions have changed, use the relevant subject method. For one known source-reliance question, use [FPF A.10](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a10---evidence-graph-referring-claim-bound-evidence-and-provenance-graph) when the source-to-use account is implicit or a required reproducible account is missing. Use [FPF A.10.1](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a101---revalidate-affected-uses-when-a-relied-on-source-changes) when a materially changed source claim leaves the affected uses to be discovered or requires coordinated revalidation across several uses. Use [FPF G.11](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#g11---decide-whether-and-how-to-refresh-sota-packs-and-related-results-telemetry-and-decay) for currentness, refresh planning or reporting under its conditions. Retain independent supported claims and state which missing premises limit the answer. Seek another supplier result through A.15.9 and C.11.DUA when its attainable contribution warrants the acquisition cost. Use a sufficient direct answer or compatible reference repair. A conclusion that no use is affected needs adequate coverage and evidence.
3. Return the strongest answer still supported: unchanged within scope, narrowed, blocked, returned to its contributor or replaced by later advice. Use PSDA.15 when a decision-support follow-up question is live.
4. Revise the reusable pattern, Method or profile only when its own claim changes. A client-specific result, professional service duty or observed outcome retains its own owner and history.

For example, loss of a mobile pump's access premise reopens that branch, not independent fixed-option arithmetic. Loss of trained reviewers invalidates a staffing-dependent mixed probe, not an unrelated internal option or the tool evaluation within its own scope. A changed professional disclosure condition concerns the applicable service, even when the developing holder is not AI. An unsupported transfer from one learner or model configuration cannot be repaired by broadening the name of the original evidence.

Keep earlier source states recoverable when revising this guidance. An updated description does not rewrite past Work, earlier advice, prior choices or their evidence. Changes that alter a recurring problem, useful result, boundary between practices responsible for a result or claim, or whole-field promise need the corresponding content decision; changed links or presentation alone do not create a new practice or prove improvement.

## PSDA.Reference:12 - Obtain the result needed for the developing subject

| Method or source | Contribution to advising |
| --- | --- |
| [FPF A.3.1](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a31---umethod-reusable-way-of-doing-with-explicit-applicability) and [FPF A.3.2](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a32---umethoddescription-description-episteme-for-a-way-of-doing) | Identify the reusable method and the description of how to perform it. Use evidence of the relevant work to establish performance or effectiveness. |
| [FPF A.15.9](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a159---use-or-request-a-bounded-result-from-another-practice), [FPF A.10](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a10---evidence-graph-referring-claim-bound-evidence-and-provenance-graph) and [FPF A.10.1](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a101---revalidate-affected-uses-when-a-relied-on-source-changes) | Use a suitable specialist result or obtain the missing contribution. Retain its evidence and limits, and revisit advice affected by a source change. |
| [FPF C.18](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c18---open-ended-search-archive-and-front-stewardship), with C.19 when its search question applies | Support open-ended generation and use of an archive. Use evidence from the relevant domain practice to assess whether the opportunity is attainable and worthwhile in this case. |
| HCD.1, HCD.3 and HCD.4 ([complete HCD first edition](Human%20Capability%20Engineering%20DPF%20Suite/HUMAN-CAPABILITY-DEVELOPMENT-PRINCIPLES-FRAMEWORK.md)) | Investigate demand from later human work, a limiting development target and a capability profile. Select other HCD methods for a specific contribution the advice still needs. Further intervention, curriculum and transfer results require their relevant methods and evidence. |
| [OCE.8](Management%20DPF%20Suite/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce8---compare-human-ai-robotic-and-provider-arrangements-for-the-same-organizational-work-result) | Compare whole organizational arrangements once the needed result and its conditions are sufficiently established. Use comparison results that apply to the organization's situation and identify any unresolved condition. |
| The applicable technical or professional practice | Supply the strategy, operating, AI evaluation, safety, authority or other case-specific premise that bears on the opportunity, recommendation or grounds for relying on it. |

The named sources support their respective contributions. To test the combined method or establish an intervention's effect, use evidence about that method or intervention under the conditions the claim covers.

The [source responsibility and references](#psdasources3---source-responsibility-and-references) identify the professional and historical grounds. For a changed premise, see [source and case changes](#psdareference13---keep-source-changes-and-case-changes-distinct).

## PSDA.Reference:13 - Keep source changes and case changes distinct

When a fact about one person, organization, model or provider changes, reconsider the opportunity or advice that depended on it. A changed human career-service condition affects the human engagement, assessment or return that used it; a changed consulting disclosure condition affects the applicable service. Keep the independent evidence for other subjects and conclusions.

Revise the reusable method when new evidence or a better approach changes its search, opportunity construction, dependency reasoning, reachability test or stopping rule. The maintainer of the affected advising or opportunity Method retains the changed claim, its source, the affected contribution and the revised limit. Reopen the wider PSDA contribution if the change affects a shared input or result on which its use depends.

When using advice, establish which subject, configuration, purpose, period and source conditions it covers. The professional relationship determines applicable duties of consent, confidentiality, competence, referral and closure. Apply those duties. Use an existing qualified result or obtain the missing professional or technical evidence before relying on the claim that needs it.

The [source responsibility and references](#psdasources3---source-responsibility-and-references) identify the relied-on sources, while the [subject-specific supplier account](#psdareference12---obtain-the-result-needed-for-the-developing-subject) identifies the contribution whose local use may need to change.

## PSDA.Reference:14 - Direct frameworks, predecessor sources, and honest omissions

This framework supplies formulation, model, value, uncertainty and comparison constructions through [PSDA.1–9](#pattern-index), and professional engagement, participation, facilitation, recommendation and follow-up through [PSDA.11–15](#psda11---bound-the-decision-support-engagement-and-authority-boundary). [Human Capability Development (HCD)](https://github.com/ailev/FPF/blob/main/DPFs/Human%20Capability%20Engineering%20DPF%20Suite/HUMAN-CAPABILITY-DEVELOPMENT-PRINCIPLES-FRAMEWORK.md) supplies personal demand, programme and evidence contributions. [OCE.8](https://github.com/ailev/FPF/blob/main/DPFs/Management%20DPF%20Suite/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce8---compare-human-ai-robotic-and-provider-arrangements-for-the-same-organizational-work-result) supplies whole-arrangement construction and comparison when that same-result question is current. Select the contribution on which the claim depends.

The earlier opportunity-construction description, [advising profile](#development-direction-advising) and [source-responsibility account](#psdasources43---predecessor-source-account-access) remain distinct sources, with their public expressions and access limits identified below. Their construction moves are carried by C.40.OI, C.40.NU, C.40.PC, C.40.DC, C.40.JF, C.40.OP, their engagement conditions by PSDA.19, and their affected-opportunity return by C.40.RQ. Use [PSDA.14](#psda14---prepare-and-return-a-decision-support-recommendation) for the qualified recommendation and [PSDA.15](#psda15---arrange-decision-follow-up-or-reassess-advice-after-a-change) for follow-up or reassessment.

The [Foundations programme](#psdasources42---foundations-programme-source-access) and [comparison](#psdasources42---foundations-programme-source-access) illustrate a programme design considered before a particular person's development question. A learner-oriented narrative can arrange explanations and practice for learning; a compact pattern body helps a practitioner select a move for a working difficulty. For a particular person's capability, programme fit or learning result, use the relevant direct practices and observations.

For a question about career design, motivation and learning science, real-options or specialist investment valuation, professional certification, legal or safety compliance, or implementation, use the applicable practice. If the inquiry needs a contribution that existing evidence cannot supply, seek it from a suitable source or explain how its absence limits the answer.

## PSDA.Reference:15 - Development-direction advising within a wider undertaking

Within a wider development undertaking, this framework's development-direction advising profile supplies bounded problem formulations, alternatives, decision models and recommendations; it does not own the whole development undertaking. [FPF C.40.OD](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c40od---construct-and-continue-open-ended-development) combines the developed Library contributions to problematisation, Method construction, transformation-flow description, capability development and cultural continuation. B.5.PI, C.39, C.40.CD/CU, E.18/E.18.NET, C.32.MWA, E.23.CDI and C.36/C.36.RP retain their precise subjects and conditions. A.12 retains the internal acting/changed-parts explanation where its premises hold. HCD, OCE, the Core Method constructions and the actual target practice retain the operations that make a subject-specific transition attainable. C.40.OD:11 compares these connections with direct use of C.32.MWA.PP, C.40.CU and the subject Method. Use that simpler combination when it supplies the needed result at lower cost. The section also identifies the CIPD and MIT CISR organizational sources and explains how their contributions were adapted. The synthesis helps connect the contributions and revise the construction when conditions change. In particular, the same-agent explanation in C.40.JD:4.2 connects available capability to a development operation and its receiving use; it neither replaces Reflexive Split nor infers acquisition from the description of a change.

STR.16 uses STR.8/11/14 for contribution and commitment construction, RMP.1/2/8 for independent epistemic purposes and attainable inquiry, MA.1–3/8 for scarce demand and time-related obligations, and OCE.8/9/11 for obtaining and realizing support while current work continues. STR.16:11 describes its comparison with the OECD mission-portfolio source and the limits on transfer. An independent scientific inquiry keeps its own purpose and acceptance conditions alongside a commercial release.

The 2024 role-community essays cited by C.40.OD describe overlapping organizational and community relations, participant journeys and competing formal and informal influence. These conceptual sources invite the adviser to ask how participants' own purposes, burdens and authority affect a proposed provision.

Examine these constructions through their intermediate results, combined conditions and changed cases. Their worked examples stipulate those conditions. Use evidence from the relevant setting for claims about organizational effectiveness or a provider's available resources. Reopen a connection when a change in the subject, supply or intended use invalidates it. A direct method can suffice for its question.

For source qualifications, citation and edition information, see the [Sources and Edition Notes](#decision-design-principles-framework-sources-and-edition-notes). For assessment and comparison, see [the earlier PSDA.4:4.3](https://github.com/ailev/FPF/blob/1e57ccda08ebbb9d49b7b2190bc2740b72075a13/DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md#psda443---compare-the-simplest-sufficient-candidate-with-a-real-alternative) and [the current PSDA.4:4.3](#psda443---assess-a-candidate-and-compare-the-available-alternatives). For the result, see [the earlier PSDA.4:4.6](https://github.com/ailev/FPF/blob/1e57ccda08ebbb9d49b7b2190bc2740b72075a13/DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md#psda446---return-the-selected-method-and-limits) and [the current PSDA.4:4.6](#psda446---return-the-assessment-selection-and-limits). For the subject of an uncertainty inquiry, see [the earlier PSDA.7:4.1](https://github.com/ailev/FPF/blob/1e57ccda08ebbb9d49b7b2190bc2740b72075a13/DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md#psda741---start-from-a-comparison-that-could-change) and [the current PSDA.7:4.1](#psda741---identify-the-claim-and-the-comparison-at-issue). For uncertainty representations, see [the earlier PSDA.7:4.2](https://github.com/ailev/FPF/blob/1e57ccda08ebbb9d49b7b2190bc2740b72075a13/DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md#psda742---represent-what-is-unknown-at-its-actual-kind) and [the current PSDA.7:4.2](#psda742---represent-the-kind-of-uncertainty). For qualifying recommendation premises, see [the earlier PSDA.14:4.2](https://github.com/ailev/FPF/blob/1e57ccda08ebbb9d49b7b2190bc2740b72075a13/DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md#psda1442---recover-what-the-available-premises-actually-support) and [the current PSDA.14:4.2](#psda1442---recover-what-the-available-premises-support). For repertoire assessment, see [the earlier PSDA.16:4.3](https://github.com/ailev/FPF/blob/1e57ccda08ebbb9d49b7b2190bc2740b72075a13/DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md#psda1643---compare-the-incumbent-with-a-serious-alternative-before-designing-a-variant) and [the current PSDA.16:4.3](#psda1643---assess-the-current-method-and-compare-alternatives-where-needed). For PSDA.17 on concurrent work, compare [earlier §4.3](https://github.com/ailev/FPF/blob/1e57ccda08ebbb9d49b7b2190bc2740b72075a13/DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md#psda1743---locate-the-interference-and-its-actual-consequence) / [current §4.3](#psda1743---locate-an-interaction-and-its-consequences), [earlier §4.4](https://github.com/ailev/FPF/blob/1e57ccda08ebbb9d49b7b2190bc2740b72075a13/DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md#psda1744---construct-alternatives-that-change-the-relationship) / [current §4.4](#psda1744---assess-the-arrangement-and-construct-alternatives-when-needed), [earlier §4.5](https://github.com/ailev/FPF/blob/1e57ccda08ebbb9d49b7b2190bc2740b72075a13/DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md#psda1745---make-the-bounded-decision-and-retain-the-residual) / [current §4.5](#psda1745---return-the-finding-and-make-any-authorized-choice).

## PSDA.Reference:End

# Patterns

## PSDA.1 - Generate Plural Problem Formulations

> **Type:** Method pattern body
> **Status:** Stable
>
> **Primary working result.** A **plural formulation set** presents materially different accounts of what warrants inquiry or intervention for the same question. Each identifies its subject and boundary, affected participants or Systems, values at stake, evidence needed, assumptions and the inquiry or intervention it makes worth considering.


### PSDA.1:1 - Problem frame

Use this pattern when one wording of “the problem” is becoming naturalized even though materially different accounts would change what is included, what evidence matters, which interventions are plausible, whose values are exposed, or the conclusion or action available to the recipient.

Start with the inquiry question. A professional engagement can supply it through `PSDA.11`. Use `PSDA.12` when participation, affected Systems, duties, interests or dissent call for its work. Construct formulations that change what needs explanation, what evidence would count or what responses merit consideration. Return their differences to the inquiry.

Comparing frames early lets the practitioner see what a familiar brief assumes before building models or alternatives. When one formulation already fits and no credible rival could change the answer or its grounds, use that formulation. For alternatives to a settled problem use `PSDA.5`. For management of an archive or search front use `C.18`.

#### PSDA.1:1.1 - Working Distinctions

| Working term | Meaning in this pattern |
| --- | --- |
| problem formulation | A bounded account of the condition or relation that warrants inquiry or intervention for a stated use. It identifies the subject, its boundary, the concern, the evidence required and the reasoning behind a proposed investigation or intervention. Retain the sources on which it relies. |
| plural formulation set | Two or more materially different formulations retained together because they differ in what they would explain, include, model, value, investigate or recommend. |
| material difference | A difference that changes the answer to the inquiry, its grounds or a possible response. Different words for the same account are insufficient. |
| intervention logic | The connection a formulation proposes between the condition treated as problematic and the families of action, inquiry, adaptation, or restraint worth considering. A formulation may propose a mechanism or an effect. Treat each as a hypothesis until evidence supports that claim. |
| framing commitment | A supported or provisional inclusion, exclusion, assumption, value emphasis, or causal hypothesis built into one formulation. |

Ill-structured situations do not arrive with one neutral problem object waiting to be described. “Insufficient capacity”, “unequal protection”, “maintenance fragility”, and “unsafe deployment” can concern the same pumping arrangement while selecting different bearers, boundaries, evidence, interventions, and consequences. The formulations may conflict, overlap, or remain jointly useful.

Expose the differences before a single model or familiar method hides them. One credible rival account can make comparison worthwhile. Use the appropriate grounds for each factual, causal, evaluative, legal, ethical, safety, authority or source claim on which the inquiry relies.


### PSDA.1:2 - Problem

The sponsor's first sentence often becomes the model title, data request, option space and recommendation. Its assumptions disappear into the scope. Differently worded accounts can also leave the inquiry unchanged if they preserve the same boundary, evidence, values and consequences. A further failure is to treat material differences as grounds for deferring every decision about the scope.

Construct a manageable set of materially different formulations. Show what each includes or leaves out and stop when another plausible account would add too little for the inquiry.

### PSDA.1:3 - Forces

| Force | Tension |
| --- | --- |
| Plurality | Rival formulations can prevent premature closure, while decorative variety wastes effort. |
| Usability | Each formulation should clarify a significant question, inference or next action. Qualify claims that remain contested. |
| Participant fidelity | Concerns should shape formulations, while participation does not prove the formulation. |
| Evidence | A formulation reveals what evidence matters, while it must not smuggle unsupported causes or effects into the case. |
| Exploration and stopping | New frames can reveal alternatives, while an unbounded set cannot support a decision. |
| Authority | A facilitator can help construct or compare formulations. A later choice requires its own authority, which may belong to a participant who also facilitates. |

### PSDA.1:4 - Solution

Construct materially different formulations for one receiving inquiry. Show what each changes about the subject, evidence, conclusions or responses, and retain its sources, assumptions, uncertainties and conflicts. Return the comparison for its intended use. A further boundary, model or alternative is needed only when the inquiry calls for it.

#### PSDA.1:4.1 - Fix the receiving inquiry, not the problem answer

State the subject, receiving question or Work and horizon. Identify any recipient and, where a later choice is involved, its authorized holder. A professional engagement can supply these premises through PSDA.11. Import a qualified PSDA.12 account only where participants, affected Systems, concerns, duties, interests or dissent can change this inquiry. Other direct sources may supply adequate premises. If the subject or receiving use differs, separate that inquiry rather than merging formulations across identities.

Establish the current formulation, its source, factual support, assumptions and material exclusions. A short statement can make the initial frame available for comparison.

#### PSDA.1:4.2 - Generate structural contrasts

Use the questions that can expose a material difference in this inquiry.

- What condition or relation is treated as problematic, for whom or what?
- Which bearer, place, configuration, horizon, or consequence is central?
- Which value, duty, interest, or risk makes this condition worth investigating or treating?
- Which mechanism or dependency is hypothesized, and what evidence could challenge it?
- Which actions, inquiries or reasons to wait become plausible, and which cease to fit?
- Who can prepare, receive, authorize, or implement a response?

Combine relevant contrasts into coherent candidate formulations. If two accounts have the same boundary, evidence, explanatory claims, possible responses and consequences for this use, merge them or identify the remaining difference as one of wording.

#### PSDA.1:4.3 - Give every formulation a usable face

For each retained formulation, identify the information the inquiry needs.

| Position | Required content |
| --- | --- |
| formulation | One ordinary-language account of what warrants inquiry or intervention. |
| subject and bearers | Subject, affected participants or Systems, configuration, place, and horizon needed by the claim. |
| boundary and exclusions | What the formulation includes, what it suppresses or defers, and why. |
| value tension | Attributed concern, duty, interest, risk, or desired change that makes the formulation material. |
| evidence need | Current support, uncertainty, contrary evidence, and any missing observation that could distinguish a rival account, strengthen the grounds, or reverse or narrow the claim. |
| intervention logic | Actions, inquiries, adaptations or reasons for restraint made plausible by the formulation, with their conditions. Effectiveness needs separate evidence. |
| receiving-use consequence | Which interpretation, evidence requirement, scope, model, alternative, comparison, recommendation or action would change. |

Where a durable formulation is used as a claim-bearing episteme, preserve its source and identity through the direct episteme pattern.

#### PSDA.1:4.4 - Test material plurality without ranking

Compare each pair only far enough to ask whether a difference affects the answer, the grounds on which it rests or the work that follows. Preserve incompatibility when one formulation requires evidence, values, boundaries, or interventions that another excludes. Record overlap when formulations can be investigated together.

Return the materially different formulations and their relations. If ranking or selection is also required, use the applicable method and choice authority. `C.17` can characterize the novelty, diversity or use of an existing set. `C.18` supports management of generation records, descriptors, archives, fronts, telemetry and retained exploration value when those are part of the task.

#### PSDA.1:4.5 - Stop and return the plural formulation set

Retain a formulation when it changes a significant conclusion, premise or possible action. Stop when another credible formulation would add too little to warrant the work. A plural set contains at least two materially different accounts. Return a single adequate formulation when that is what the inquiry supports.

Return the formulations, their contrasts, shared and disputed premises, material gaps and any further use or observation that could reopen the question. When a missing concern, fact, source, participant contribution or authority limits a formulation, identify the gap. Use available evidence, obtain an attainable missing contribution when warranted, or narrow the answer or abstain.

#### PSDA.1:4.6 - Pass plurality forward without creating a workflow

Pass the set to `PSDA.2` when included and excluded scope must be chosen, to `PSDA.3` when different models are needed, to `PSDA.5` when a formulation changes a candidate action or its conditions, or opens other alternatives, and to `PSDA.17` when engagement activities obstruct a material formulation contribution. These branches may be concurrent.

Reopen locally when a new participant, concern, affected System, evidence result, value tension, intervention family, horizon, receiving use, or authority fact creates a materially different formulation or defeats one already retained.

#### PSDA.1:4.7 - What changes in practice

The practitioner can compare materially different accounts, including accounts participants do not agree on. Identify which evidence, explanation or practical response each account changes.

### PSDA.1:5 - Archetypal Grounding

#### PSDA.1:5.1 - Four formulations of the flood-pump situation

For the board's pre-season decision, the `PSDA.12` account supports four formulations worth examining.

1. **Capacity shortage:** peak inflow can exceed available pumping capacity; flow, reliability, and deployment evidence matter; permanent or mobile capacity becomes salient.
2. **Unequal protection:** current arrangements shift flood exposure toward particular districts and mobility-constrained residents; distribution, access, and representation evidence matter; allocation and protection rules become salient.
3. **Maintenance fragility:** failures may depend on maintenance, spares, staffing or coordination even when the nominal pump count is adequate; readiness, contracting, and staged maintenance alternatives become salient.
4. **Unsafe deployment:** emergency placement and operation can create worker, resident, traffic, or downstream risks; safe operating envelopes and restraint branches become salient.

The four accounts lead to different boundaries, evidence, models, alternatives and value questions. The team records the overlaps and conflicts and uses `PSDA.2` to choose the scope for the board's question. Qualifying an intervention's effectiveness requires further evidence.

#### PSDA.1:5.2 - Development-direction advice

For an AI-assisted incident-response arrangement, “model accuracy is inadequate”, “operator coordination is fragile”, and “authority escalation is unclear” imply different holders, evidence, intervention families, and safety questions. PSDA.1 retains all three when each can change the two-quarter recommendation or its grounds. Generic slogans such as “improve AI capability” and “make the system better” fail the material-difference test.

#### PSDA.1:5.3 - Cheap non-use

A repair team has a verified broken seal, one affected assembly, one authorized repair decision, and no rival account that changes evidence or action. The live question is which qualified replacement to use. Compare the qualified replacements or use an existing comparison to choose under the repair authority.

### PSDA.1:6 - Bias-Annotation

**Scope.** Compare formulations for one bounded inquiry. Distinguish influence on framing from authority to choose. Establish how the formulation changes dependent work, what evidence supports its claims and which differences warrant attention. Use ordinary language to expose the contrast before formal modelling when that helps the inquiry.

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| sponsor-frame bias | The opening brief becomes the only formulation. | Externalize it with sources and exclusions, then seek structural contrasts. |
| vocabulary bias | Synonyms are counted as plurality. | Require a changed boundary, evidence need, intervention family, value, or receiving-use consequence. |
| consensus bias | Participants must agree on one wording before inquiry. | Retain incompatible formulations and name their downstream differences. |
| causality bias | A framing hypothesis is reported as the cause. | State mechanism, support, uncertainty, and falsifying or narrowing evidence. |
| option leakage | Problem formulations become preselected solutions. | State intervention families as consequences of a frame, not proven answers. |
| endless-reframing bias | Every possible perspective stays live. | Stop when added formulations no longer change the named use enough to justify cost. |

### PSDA.1:7 - Conformance Checklist

- [ ] Every formulation concerns the same bounded subject and receiving use, and identifies a different inquiry separately. Use `PSDA.11` for a changed professional engagement when its terms need clarification.
- [ ] Material participants and concerns supplied by `PSDA.12` or other qualified direct sources inform the formulations. Factual or causal claims attributed to participants are qualified for their intended use.
- [ ] Each retained formulation changes at least one boundary, evidence need, model, alternative family, value treatment, or receiving-use consequence.
- [ ] Sources, assumptions, exclusions, uncertainty, and intervention logic are visible.
- [ ] Causal, evaluative, legal, ethical, safety, and authority claims retain their direct assurance.
- [ ] Any ranking or choice attributed to a participant has its own grounds and, where required, authority.
- [ ] The stopping rule prevents both decorative plurality and endless reframing.
- [ ] Missing premises produce a gap, narrowed claim, request, blocker, or abstention.
- [ ] A needed boundary, model, set of alternatives or interference inquiry can use the formulation result through `PSDA.2`, `PSDA.3`, `PSDA.5` or `PSDA.17`, respectively.

### PSDA.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Agree on the problem first.” | Establish the receiving use. Retain materially different formulations and note any disputed purpose that affects the inquiry. |
| “Brainstorm ten frames.” | Keep only formulations that change a conclusion, its grounds or the work needed. |
| “Every stakeholder gets a frame.” | Build coherent formulations from material differences; participation identity does not define one frame each. |
| “The most popular frame is true.” | A tally of endorsements can establish how many participants expressed support. A count of mentions can include objections. Establish truth, cause, value priority or authority from grounds appropriate to that claim. |
| “A novel wording is a new problem.” | Use the material-difference test; use `C.17` only if novelty characterization itself matters. |
| “The formulation set is an option archive.” | Use `PSDA.5` for decision alternatives and `C.18` for governed archives or fronts. |

### PSDA.1:9 - Consequences

Later models, boundaries, alternatives, and recommendations inherit visible framing assumptions instead of one hidden sponsor frame. Practitioners can investigate incompatible accounts without forcing premature consensus. Comparing sources and contrasts takes time. Where a material premise remains unestablished, a qualified gap may answer the inquiry.

### PSDA.1:10 - Rationale

A problem formulation connects a contested description to concerns, values, evidence needs and possible investigation or intervention. Comparing these accounts can serve understanding or a later decision. Use the relevant FPF guidance for evidence, episteme identity, relations, characterization of an existing set or authority for a subsequent choice.

### PSDA.1:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How should a practitioner preserve plural framing without losing a usable inquiry? | Treat framing as selection and organization of what matters, externalize materially different formulations, compare their consequences, and revise them as contextual evidence changes. | A fixed sponsor brief is the serious default; unconstrained perspective collection is the opposite default. | The first hides framing commitments and the second cannot stop. **Adapt:** `PSDA.1:4.1`–`PSDA.1:4.5` requires structural contrasts, downstream materiality, sources, and a stop when the formulations suffice for their receiving use. | Kelly and Gero's [2022 framing review](https://doi.org/10.1017/dsj.2022.25) supports multiple non-equivalent meanings of design framing; Litster, Cardoso, and Hurst's [2024 study](https://doi.org/10.1017/S089006042400012X) supports observation of changing externalized team framing; Nickel, Hurst, and Duimering's [2024 study](https://doi.org/10.1017/dsj.2024.34) supports contextual trade-offs. These sources establish neither one framing ontology, universal Method, shared team frame, prevalence, causality, nor superiority. | Reopen if later comparative evidence changes the best-known framing line or if contextual evidence materially changes a retained formulation. |
| What remains specifically PSM work after generic candidate handling is subtracted? | PSM practice retains the construction and facilitation of rival problem formulations for ill-structured situations; FPF supplies direct evidence, relation, identity, and later-choice governors around that result. | Treating formulation as generic brainstorming, alternative generation, or archive management is the serious default. | It loses the relation between a formulation and the concerns, boundaries, evidence, and intervention logic of the receiving inquiry. **Adopt:** the formulation face in `PSDA.1:4.3` and the pass-forward boundary in `PSDA.1:4.6`. | Smith and Shaw's [2019 review](https://doi.org/10.1016/j.ejor.2018.05.003) and Kogetsidis's [2025 review](https://doi.org/10.1108/IJOA-08-2024-4746) support PSM as a continuing, diverse, facilitated branch for ill-structured situations. `C.17` characterizes novelty/diversity/use of a named set; current `C.18` governs open-ended generation, archives, fronts, descriptors, and telemetry. None proves that one PSM, formulation count, facilitation arrangement, or archive policy is universally sufficient or superior. | Reopen if a direct generic pattern acquires the full PSM-specific construction at equal or lower effort, or if PSM evidence changes the material plurality test. |

### PSDA.1:12 - Relations

- For a professional engagement, `PSDA.11` supplies the bounded subject, receiving use, horizon, recipient, and authority boundary. Use `PSDA.12` when material participation, affected Systems, concerns, duties, interests, or dissent need its professional construction; other inquiries can use adequate direct premises.
- `PSDA.2` receives the plural set when the current included/excluded problem boundary must be chosen. `PSDA.3` receives formulation-dependent model needs.
- `PSDA.5` receives the possible actions and conditions that depend on a formulation; it does not retroactively define the problem. `PSDA.17` can use the plural formulation set when deciding how to resolve material interference in the engagement.
- `C.17` may characterize novelty, diversity, or use of the generated set. `C.18` governs archive/front/generation-record stewardship only when those objects are needed.
- Direct episteme, evidence, relation, value, causal, legal, ethical, safety, governance, and choice patterns govern their own claims. Use PSDA.1 to construct the set. A later ranking or choice has its own rule and authority.

### PSDA.1:End

## PSDA.2 - Set and Reopen the Problem Boundary

> **Type:** Method pattern body
> **Status:** Stable
>
> **Primary working result.** A **usable problem scope** identifies what this inquiry includes, what it leaves out or uncertain, why that boundary suits the receiving use and what could justify changing it. Include the formulations, affected participants or Systems, concerns, relations, conditions, horizons and possible responses that matter to the question.


### PSDA.2:1 - Problem frame

Use this pattern when an inquiry either expands toward everything connected with the situation or excludes a concern, bearer, relation, horizon, or intervention family that could reverse the usefulness of the result. Use it after or alongside `PSDA.1` when plural formulations imply different boundaries.

Choose the smallest boundary that supports the required result. Identify consequential exclusions and the conditions under which the inquiry would need a different scope. The recipient can use that boundary and see which conclusions it leaves open.

For exact membership of a `U.ContextSlice` in a declared `U.Scope`, use `A.2.6`. Document scope, organizational jurisdiction, an engineering System boundary and a settled project charter have their own questions. If the receiving use remains unclear, establish it from available evidence or report the missing premise. Use `PSDA.11` when the gap concerns a professional engagement.

#### PSDA.2:1.1 - Working Distinctions

| Working term | Meaning in this pattern |
| --- | --- |
| engagement boundary | The `PSDA.11` boundary around the decision-support return, recipient, subject, horizon, receiving use, and authority. |
| problem boundary | The provisional cut that determines which formulations, bearers, concerns, relations, conditions, horizons, evidence, and intervention families are treated as material now. |
| material exclusion | An omitted or deferred item that could change the current result and therefore must remain visible with a reason, uncertainty, and reopen condition. |
| usable scope | The smallest current problem boundary adequate for a named next result and its assurance burden. Reconsider it if that use or its premises change. |
| reopen basis | An observable change or newly recoverable value that can make the current boundary too narrow, too broad, or otherwise unfit for the receiving use. |
| `U.Scope` | A declared scope for exact `U.ContextSlice` membership, governed by `A.2.6`. An ordinary problem boundary need not be reified as one. |

Every formulation makes a cut. It foregrounds some participants, Systems, concerns, causal or modal paths, operating conditions, time horizons, evidence, and intervention families while leaving others outside. In ill-structured situations those cuts are often contested and revisable rather than simply discovered.

Choose or explain the boundary warranted for this use. Identify exclusions or observations that could require revision. One plausible change that would reverse the conclusion can justify examining the boundary. Establish consequential claims about inclusion, relations, harm, authority, law, ethics, safety or facts through the relevant practice.


### PSDA.2:2 - Problem

A sponsor's implicit boundary can hide which participants or concerns the inquiry leaves out. An unbounded map can consume the available effort before producing a usable result. A precise scope declaration can still leave its suitability for the inquiry in dispute.

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

Recover the subject, receiving use and horizon from a source that fits this inquiry. Identify any recipient and any holder of a subsequent choice. A suitable `PSDA.11` engagement account can supply those premises. Use the formulations whose differences matter, including results from `PSDA.1` where relevant. An already adequate single formulation can support the scope. Retain any contested inclusion or exclusion that affects the answer or its grounds.

Use a qualified `PSDA.12` account or other suitable evidence where affected participants, concerns, duties, interests, dissent, representation limits or consequence paths may challenge the cut. Explain material exclusions even when a concern appears in a participation account. If a necessary input is unavailable or incompatible, obtain an applicable result or identify the premise that remains unresolved. Establish current representation and authority from responsible sources where the inquiry relies on them.

#### PSDA.2:4.2 - State the boundary through decision-bearing dimensions

Identify the dimensions that can affect the answer or its grounds.

- subject, configuration, place, population, and operating condition;
- included formulations and affected bearers;
- concerns, duties, interests, relations, dependencies, and consequence paths;
- evidence interval, uncertainty, and time horizon;
- intervention, adaptation, restraint, and no-action families; and
- participating, receiving, implementing, and choice-authority positions where material.

Carry forward the object distinctions recovered with the concerns. If “business trip” names both remote repair and administrative provision, say which work this inquiry concerns and which dependencies it includes. A boundary around expense processing cannot support a conclusion that the remote repair was completed. Several concerns about one identified journey can instead share that object boundary.

State the boundary in ordinary language. Add a declared `U.Scope` when the receiving use requires an exact membership claim.

#### PSDA.2:4.3 - Keep material exclusions and unknowns alive

For a material exclusion, identify what was left out, why, the available evidence, the consequence of an error and what evidence could justify revisiting the cut. Keep the following distinctions where they affect the result.

- outside for this receiving use from irrelevant in general;
- deferred from rejected;
- unknown membership from supported non-membership;
- absent evidence from evidence of absence; and
- a practical stopping decision from a claim that no relation or consequence exists.

Give exclusions the attention their possible consequence warrants. A high-consequence result that could reverse needs appropriate assurance or a stated limit before reliance.

#### PSDA.2:4.4 - Challenge the cut before accepting it

Use the challenges that could expose a consequential error in this cut.

1. **bearer challenge:** could a participant or affected System outside the cut undergo a material change?
2. **formulation challenge:** would another retained formulation include a different mechanism, value, horizon, or intervention family?
3. **action challenge:** does the cut make one alternative appear necessary by excluding feasible restraint, adaptation, or no-action branches?
4. **evidence challenge:** are data availability or model convenience defining the boundary?
5. **authority challenge:** does the cut silently transfer a duty, jurisdiction, implementation burden, or later choice?
6. **reversal challenge:** which observation, if available, could change the conclusion or show that the scope is inadequate?

If the challenge exposes a defect, revise the affected dimension and the conclusions that depend on it.

#### PSDA.2:4.5 - Use exact scope membership only when needed

When a downstream claim depends on whether one exact `U.ContextSlice` belongs to one declared `U.Scope`, use `A.2.6`. Distinguish an evaluation result of true, false, or unknown. An unknown result means the available evidence does not settle membership. Use a suitable existing result, obtain a missing input when warranted, or report the limit or narrower conclusion. Changing the extension creates a new scope; a refit that preserves the extension does not.

PSDA.2 judges whether the problem boundary suits the inquiry. `A.2.6` governs exact contextual membership. A `C.2.3` formality threshold concerns how strictly a claim is expressed and is selected separately, only when the receiving use needs it.

#### PSDA.2:4.6 - Return the usable scope and reopen basis

Return the scope in the smallest form that answers the current question. Use the applicable entries below. A local clarification can finish with the scope itself.

| Result position | Content needed by the recipient |
| --- | --- |
| receiving use | Subject, receiving question or Work and horizon, with any recipient and holder of a subsequent choice. |
| formulation basis | Current formulations and the material differences the boundary preserves. |
| included scope | Bearers, concerns, relations, conditions, horizons, evidence, and intervention families included now. |
| exclusions and unknowns | Material omissions or uncertainties, reasons, consequences of error, and direct assurance still needed. |
| adequacy reason, where needed | Why this is the smallest usable scope, when the recipient needs that basis to judge the cut or avoid mistaking an exclusion for a settled fact. |
| dependent uses | Models, facilitation, alternatives, value treatment, comparison, recommendation, or inquiry results that consume the scope. |
| reopen basis | Conditions that would justify widening, narrowing, replacing or reformulating a dimension, and any observation that could establish them. |

If no defensible boundary is available, identify the premise that prevents a defensible cut and return the narrower supported conclusion or a reason to abstain.

#### PSDA.2:4.7 - Reopen locally and state what changed

Reopen when a new participant, affected System, concern, formulation, relation, operating condition, evidence result, value tension, intervention family, horizon, receiving use, or authority fact can change the current result. Name the old boundary, new observation, affected dimension, and dependent result.

When the new basis warrants revision, widen, narrow or replace the affected portion. Use `A.2.6` if a declared `U.Scope` or relied-on membership result changes. Separate or revise the inquiry when the receiving use changes. Use `PSDA.11` if new engagement terms are needed, and `PSDA.1` if a missing formulation requires its work.

#### PSDA.2:4.8 - What changes in practice

The practitioner can return a boundary that fits the current use, explain consequential exclusions and show how a change in the evidence or question would affect the scope.

### PSDA.2:5 - Archetypal Grounding

#### PSDA.2:5.1 - Flood-pump boundary

For the board's pre-season decision, the current boundary includes the district pumping arrangement, permanent and mobile capacity, maintenance and staffing dependencies, deployment safety, district access, the next flood season, and material downstream transfer paths. It preserves the questions of capacity, unequal protection across districts and affected residents, maintenance and safe deployment from `PSDA.1`.

Long-term watershed redesign and permanent residential relocation are outside the current investment return, for this season. Relocation rights and downstream consequences remain material exclusions because they can reverse a recommendation. The boundary records that verified cross-district flood transfer, a safety limit outside the assumed operating envelope, or evidence that no feasible pump branch protects mobility-constrained residents will reopen the relevant dimension.

The result supports model and alternative work for the stated investment question. Claims that the consequences occur need evidence from the relevant setting. Funding, legal, ecological and safety determinations need the corresponding authority or specialist grounds.

#### PSDA.2:5.2 - Narrowing after a failed generalization

An incident-response inquiry initially covers all product lines. The available evidence supports the proposed escalation pattern for one regulated line and one staffing configuration. The practitioner narrows the problem boundary and dependent recommendation instead of claiming organization-wide use. Other lines remain explicit unknowns with their own reopen conditions.

#### PSDA.2:5.3 - Cheap non-use

A laboratory test claim already has a declared `U.ClaimScope` with population, configuration, and interval selectors. The live issue is whether one proposed test's `U.ContextSlice` belongs to that scope. Use `A.2.6` directly to evaluate that membership.

#### PSDA.2:5.4 - One adequate formulation and a consequential exclusion

An analyst and a maintenance lead already share the formulation “why are the authorized pump checks late?” Their immediate clarification is whether to examine this week's check queue or expand into redesigning the whole maintenance organization. The available queue and assignment facts support the first cut. The analyst describes the scope as “this week's authorized checks, their staffing and access dependencies, and the late returns.” This scope answers the local question.

A later board asks whether the same result establishes readiness for the flood season. Now the exclusion of uncompleted seasonal checks can change its decision. The returned scope must retain that those checks were outside the weekly lateness inquiry and that their readiness remains unestablished. The board needs the seasonal check result before relying on a readiness claim. The weekly scope remains suitable for the lateness inquiry. Establish seasonal readiness and authority to operate from their respective grounds.

### PSDA.2:6 - Bias-Annotation

**Scope.** Judge the boundary chosen for a particular use. Distinguish inclusion from jurisdiction and from authority to choose. Identify the framing commitments, evidence and dependent work that matter to this cut. State exclusions and conditions for revision in language the recipient can use.

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| sponsor-boundary bias | The brief's perimeter becomes unquestionable. | Challenge it with bearers, formulations, actions, evidence, authority, and reversal. |
| map-completeness bias | More nodes are treated as better scope. | Check how each included dimension affects the requested result or the grounds for relying on it. |
| data-availability bias | Available variables define the problem. | Record excluded concerns and evidence gaps independently of the model. |
| box-as-ontology bias | A drawn perimeter is treated as proof of a System boundary or exact scope membership. | State the ordinary decision-support cut; use the direct engineering practice for a System-boundary claim and `A.2.6` for contextual membership when either is needed. |
| exclusion-as-falsehood bias | Outside the current inquiry becomes “does not matter”. | Record material exclusions, uncertainty, consequence, and reopen basis. |
| boundary-freeze bias | Later contrary evidence is absorbed without revising scope. | Reopen the smallest affected dimension and dependent results. |

### PSDA.2:7 - Conformance Checklist

- [ ] The boundary is tied to one receiving use, subject and horizon, with the authority boundary stated where that use has one.
- [ ] Current formulations and material participation or affected-System inputs are recoverable.
- [ ] Included bearers, concerns, relations, conditions, evidence, horizons, and intervention families are stated only at the needed grain.
- [ ] Material exclusions and unknowns retain reasons, consequences of error, and reopen observations.
- [ ] The relevant challenges to bearers, formulations, actions, evidence, authority or reversal were applied in proportion to their consequences.
- [ ] The result carries the reason for the cut where the receiving use needs it, including any materially contested exclusion.
- [ ] A claim about exact `U.ContextSlice` membership in `U.Scope` uses its own evaluation when that claim is required.
- [ ] The scope identifies material missing premises, any supported narrower claim and any missing input worth obtaining.
- [ ] Reopening changes the smallest affected dimension and identifies dependent results.
- [ ] Any attributed choice, authority or specialist judgement has the basis required by its legal, ethical, safety, scientific, engineering or governance practice.

### PSDA.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Everything is connected, so include everything.” | Include only what can change the named receiving use; preserve material exclusions and triggers. |
| “Outside scope means irrelevant.” | State outside-for-now, consequence of error, and reopen condition. |
| “The model boundary is the problem boundary.” | Let formulations and concerns challenge available variables and model convenience. |
| “Draw the system boundary.” | Name the problem-structuring cut; establish any System-boundary or exact contextual-membership claim through its direct pattern. |
| “Unknown means excluded.” | Report true, false or unknown according to the evidence for the declared scope. |
| “Scope was agreed at kickoff.” | Reopen when the named observation can change the receiving result. |

### PSDA.2:9 - Consequences

A usable scope can answer its own inquiry or support further models, alternatives, comparisons and recommendations. Revising a material exclusion takes effort, but the change can often be confined to the conclusions that depend on it. An unsupported premise can require narrowing the answer or stopping.

### PSDA.2:10 - Rationale

A problem boundary expresses which considerations matter to the receiving inquiry and why. Establish its suitability and the conditions that would justify changing it. For a separate claim of exact contextual membership, use `A.2.6`.

### PSDA.2:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How should a problem boundary remain useful and revisable? | Treat framing as a contextual selection of what matters, compare materially different cuts, state exclusions, and revise the boundary when new evidence changes the receiving use. | A fixed sponsor scope is the serious default; an unbounded whole-situation map is the opposite default. | The first suppresses consequential exclusions and the second cannot stop. **Adapt:** `PSDA.2:4.1`–`PSDA.2:4.4` and `PSDA.2:4.6` require decision-bearing dimensions, material exclusions, proportionate challenges, and the scope reason needed by the receiving use. | Kelly and Gero's [2022 framing review](https://doi.org/10.1017/dsj.2022.25), Litster, Cardoso, and Hurst's [2024 mapping study](https://doi.org/10.1017/S089006042400012X), and Nickel, Hurst, and Duimering's [2024 contextual trade-off study](https://doi.org/10.1017/dsj.2024.34) support explicit framing, externalized change, and contextual trade-offs. They establish neither one framing ontology, universal Method, shared frame, fixed boundary, prevalence, causality, nor superiority. | Reopen if later field evidence changes the best-known boundary practice or if new contextual evidence changes an included or excluded dimension. |
| When does a receiving use need exact contextual scope membership? | Keep ordinary inquiry cuts in plain language; use current `A.2.6` only when the receiving use must decide whether one exact `U.ContextSlice` belongs to one declared `U.Scope`. | Treating every diagram box or topic perimeter as a declared exact scope is the serious default. | It substitutes apparent precision for boundary judgement and can hide unavailable evaluation. **Adopt:** `PSDA.2:4.5` distinguishes true, false, and unknown evaluation results and routes extension changes to the direct pattern. | Current `A.2.6` supplies exact contextual membership, extension change, and refit discipline. Its applicability axis is independent of `C.2.3` formality. It does not judge which participants, concerns, formulations, intervention families, or exclusions make a PSM boundary usable. Direct engineering, legal, safety, ethical, and governance practices retain their own boundaries and thresholds. | Reopen if the direct scope pattern gains the complete problem-boundary judgement at equal or lower effort, or if a relied-upon scope or membership result changes. |

### PSDA.2:12 - Relations

- `PSDA.11` supplies the identity and authority boundary of a professional engagement when one is involved. `PSDA.12` supplies participation, concern, and affected-System challenges where those professional results are needed. Use a single adequate formulation or the material differences in a plural set from `PSDA.1` when the scope depends on them.
- `PSDA.3` and `PSDA.4` receive the scope and formulation basis for modeling and PSM-arrangement questions. `PSDA.17` receives the scope and reopen basis for resolving material interference among simultaneous work contributions in a decision-support engagement.
- `A.2.6` governs exact `U.ContextSlice` membership in a declared `U.Scope` when that claim is needed. `A.1.CSD` supplies consequence-bearer challenges; exact relations remain with their direct governor.
- Direct evidence, legal, ethical, safety, scientific, engineering, governance, assignment, and authority patterns govern their own claims. Use their results where the boundary depends on a specialist claim or a later choice.

### PSDA.2:End

## PSDA.3 - Construct Complementary Situation and Option Models

> **Type:** Method pattern body
> **Status:** Stable
>
> **Primary working result:** a **multi-model decision account** that identifies which models answer the receiving questions, where their claims correspond or conflict, and what the evidence supports. One sufficient model may answer the inquiry.

### PSDA.3:1 - Problem frame

**Use this when** one diagram, spreadsheet, simulation, or agreed story is being asked to explain a contested situation, represent everyone's concerns, predict consequences, and identify the best intervention. Also use it when several models exist but their different subjects, assumptions, or meanings make their combined result unclear.

Start with the question the recipient needs to answer. Use a model that can answer the question or supply a needed part of the answer. Add another when it addresses a material omission, supports a needed comparison or provides independent grounds for a claim the recipient will rely on.

The account connects a model’s claims about its subject with the diagram, table or other expression through which the reader can inspect those claims. Identify what the model represents, such as a pump, a service arrangement or a proposed change.

Use an already qualified calculation or model directly when it answers the whole question. Refer a calculation’s validity to the relevant modeling, engineering, scientific or evidence practice if that issue remains open. Revisit formulation or scope if the intended question is still unclear.

### PSDA.3:2 - Problem

A capacity calculation cannot show whose service standard should govern. A rich picture can reveal attributed concerns without estimating a failure probability. A scenario can expose a vulnerable condition without predicting how often it will occur. Treating any one of these as a complete account hides questions it was never built to answer.

Two models may reuse the same data, use incompatible units or populations, or label different quantities “risk”. Check what their agreement or disagreement establishes. If a dashboard combines their results, preserve any difference in meaning or shared dependence on evidence.

### PSDA.3:3 - Forces

| Force | Tension |
| --- | --- |
| Discrimination | A model can answer a question, expose an omission or improve the grounds for retaining a conclusion. Exploratory modeling may bring the question itself into view. |
| Plurality | Material perspectives deserve distinct expression, while collecting every imaginable model makes the engagement unaffordable. |
| Correspondence | Related models need interpretable connections, while forced translation can erase their different meanings. |
| Credibility | Consequential reliance requires qualified evidence, while a preliminary model can still be useful for recognizing a missing premise. |
| Revision | A shared boundary permits comparison, while a model may reveal why that boundary must reopen. |

### PSDA.3:4 - Solution

Choose the models the questions require. For each one, identify its subject, use, assumptions, evidence and relevant omissions. Compare overlapping claims where their meanings can be aligned. Return the supported findings, any consequential disagreement and the limits on use.

#### PSDA.3:4.1 - Recover the questions and current boundary

Where competing formulations identify claims or intervention mechanisms a model must distinguish, use the relevant results of `PSDA.1`. Identify the subject, question, conditions, horizon and grounds for reopening scope. Use a compatible `PSDA.2` result when it supplies them.

A qualified direct source may supply the formulation or scope. If a necessary premise remains unavailable, out of date or incompatible with the intended use, name the gap or answer within the narrower supported scope.

Turn the live differences into questions, such as “Does this arrangement retain service when road access is lost?” and “Whose loss is omitted by the aggregate service measure?” Keep question, assumed condition, and proposed intervention separate.

#### PSDA.3:4.2 - Choose complementary contributions at the needed grain

Identify the contribution a model could make to the question before choosing its notation or tool.

| Needed contribution | A possible model | Limit to preserve |
| --- | --- | --- |
| Make different interpretations and concerns discussable. | A rich picture, purposeful-activity model or attributed cognitive map. | The rendering expresses the interpretations attributed to its contributors. Agreement on the rendering, agreement on an intervention and evidence for a causal relation require different support. |
| Examine a proposed mechanism or dependency. | A causal, stock-and-flow, network or dependency model. | An arrow may represent a hypothesis or structural assumption. A claim about what causes an observed outcome needs evidence for that relation. |
| Explore changed conditions and intervention responses. | A scenario or conditional simulation. | A scenario is not a probability estimate; a simulated response depends on the model and inputs. |
| Expose objectives and distinguish consequences. | An objectives hierarchy, criteria model or consequence table. | To use weights or trade one concern against another, establish the meaning and comparability of the measures and the applicable value and authority premises. |
| Test a technical feasibility premise. | A domain calculation or qualified engineering model. | Feasibility holds only within its configuration, operating envelope, evidence, and uncertainty limits. |

Keep the smallest set that covers the material questions and assurance needs. A qualitative model may expose a question worth quantifying. A numerical model may expose a missing qualitative distinction. Retain a further model when it supplies a distinct contribution, including independently grounded evidence for or against another model’s claim.

A concern map can complete the task of making the participants’ concerns discussable. For a separate question about a cause or the effect of an intervention, use an adequate causal model if one exists. Where the relations still need construction or comparison, use `C.28.CM` to build models from subject knowledge and proposed mechanisms. Return the assumptions, conditional consequences and unresolved alternatives. Qualify causal claims for their intended use under :4.5.

When the question concerns participants' intentions, their dependence on one another and possible alternatives, [PSDA.20](#psda20---explore-a-situation-through-goals-and-dependencies) develops the whole inquiry from a working difficulty. It explains how to construct the actors-and-goals model, select what a view reveals, turn a question into analysis assumptions, interpret the answer and return to an omitted assignment when the result exposes a conflict. Use an adequate existing model directly. Where the needed questions, assumptions or connections remain missing, use that Method to construct them.

#### PSDA.3:4.3 - Make each model's use intelligible

For each model, identify its subject, the question it answers and the conditions of the supported use. Give the assumptions, evidence source and relevant interval, important omissions, and any known observation that would narrow or invalidate reliance. Identify the model content or edition where a changed value could alter the result.

For a mathematical formalism, simulation, or learned representation, apply `C.29` when the choice of mathematical object, mapping, preserved structure, or information loss changes the claim. For example, a road graph can preserve routes and travel-time assumptions while omitting residents' access rights and the reliability of an untested deployment procedure. Use evidence about the residents and the deployment procedure if the question requires those omitted facts.

Use local definitions, units, scope and evidence where they suffice. Use `A.1.1` for a question about whether a model applies to the stated subject and claim, whether an assigned performer used it in work on that subject, or whether fixed model and expression contents meet a stated coherence criterion under a comparison scheme. Use the broader account when the relations among these claims matter to the receiving inquiry.

#### PSDA.3:4.4 - Reconcile overlaps without forcing one model

For a material overlap, compare the subjects, configurations, populations, horizons, units, definitions, assumptions and evidence on which the claims depend. Two models may describe one object or related objects. A travel-expense model and a repair-performance model can concern different work on one business trip. Establish the completion conditions for each. A shared contract could specify the same completion event, while different terms could require distinct evidence. Establish each correspondence from the subjects and meanings. When one model treats service failure as lost pumping capacity and another as inability to reach a refuge, examine the relation that the receiving question needs and retain any unresolved difference.

Locate the source of a material mismatch in the questions, assumptions, meanings or evidence. Correct a unit or input error where it occurs. Retain plausible alternatives where their truth remains open. If investigation could matter to the conclusion or the grounds for relying on it, compare its attainable contribution and cost with returning the qualified alternatives or a narrower answer through `C.11.DUA`. Use `A.15.9` for a selected outside-practice contribution and its acquisition burden.

Keep unlike outputs in their own measures. Scenario counts need a probability basis before they can support a probability estimate. When two models draw on one dataset, identify that shared dependence. The account can explain how the models inform one another while retaining their different subjects or assumptions.

#### PSDA.3:4.5 - Match assurance to the claim being used

A sketch and a plausible contrast may suffice to identify a question. For reliance on an answer, check the claims that carry it. As applicable, examine source qualifications, implementation or calculation, fitness for the intended use, validation, sensitivity and extrapolation. Assess sufficiency through the practice responsible for the claim.

Distinguish confidence in the modeler from internal consistency, fit to the evidence, sensitivity to assumptions and authority to decide. Stakeholder confidence can influence whether a model is used. A model whose recommendation depends on an unresolved premise may already establish which premise matters.

Return the supported claim, its narrower scope or the particular difference the models cannot resolve. An open safety, rights, legal or technical premise can block a proposed use. Seek the competent result for a stronger use when it is attainable and its contribution warrants the effort.

#### PSDA.3:4.6 - Return the account and its reopen basis

Keep enough content for the recipient to recover:

- the subject, question, receiving use, configuration, and horizon;
- each selected model's distinct contribution, current content, source basis, assumptions, and losses;
- the material correspondences, conflicts, and shared evidence dependencies;
- what the account supports, what remains hypothetical or unknown, and which alternatives or claims it can discriminate; and
- an observation or change in conditions that would reopen the model, a connection, the formulation or its boundary, where one is material.

This can be a short annotated comparison. If no model combination answers the question, say so.

The account may inform Method selection, alternative generation, uncertainty treatment or reconciliation of simultaneous inquiries. Supply the current, compatible contribution needed for the receiving question. Make any further judgement under the conditions of that task.

#### PSDA.3:4.7 - What changes in practice

Ask which claims need a model, what each selected model contributes and which differences affect a conclusion or its use. When several models remain useful, explain their overlaps and limits.

### PSDA.3:5 - Archetypal Grounding

#### PSDA.3:5.1 - Flood-pump models that answer different questions

In this illustrative continuation of the flood-pump inquiry, the board needs a pre-season decision-support return about permanent pumps, mobile capacity, maintenance, staffing, and access. The current formulations distinguish capacity shortage, deployment reliability, unequal service, and transferred downstream consequences. The scope includes the next flood season and preserves relocation rights and long-term watershed change as material exclusions.

The team builds the following account from the assumptions of the example.

| Question and model | Account slice | Consequence for inquiry |
| --- | --- | --- |
| Can nominal capacity meet the assumed inflow? A capacity calculation. | Permanent and mobile branches meet the assumed requirement only with the stated operating units available; no deployment delay is represented. | Nominal capacity alone cannot discriminate reliability or access. |
| Can mobile units reach and serve the district? An access-and-deployment scenario model. | With the main road unavailable, the mobile branch has no supported arrival-time claim. A second route is a hypothesis requiring an operations result. | Keep the mobile branch conditional; arrival time remains unsupported. A route/deployment request is selected only if its obtainable contribution warrants acquisition for this decision. |
| What counts as adequate service, and for whom? An attributed concern map. | The residents' association emphasizes property protection. A separately heard group of mobility-constrained residents requires reachable assistance. Neither statement represents all residents. | Preserve the two service meanings; the hydraulic output does not settle their relation or priority. |

The capacity calculation supports both branches under its assumptions. The mobile branch still depends on access. Property protection and reachable assistance remain distinct service requirements. The account identifies these limits and leaves the investment ranking open.

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

- [ ] The reader can identify the subject, question and use, with the configuration and horizon needed to interpret the account.
- [ ] Needed formulation and scope inputs are current and compatible, or their exact gaps are returned.
- [ ] Each model supplies a distinct useful contribution; one sufficient model remains a valid cheaper exit.
- [ ] The subject, model content, expression, evidence, and possible intervention remain distinguishable.
- [ ] Assumptions, important losses, and limits accompany every relied-on output.
- [ ] Material overlaps are compared by meaning, scope, units, and evidence dependency; unresolved differences are not averaged away.
- [ ] Where a claim depends on mathematical mapping, model applicability, performed use or expression coherence, the relevant relation has been established.
- [ ] The grounds fit the claim about recognition, validation, confidence, cause or decision authority.
- [ ] The return identifies supported claims and any unresolved differences or material conditions for reopening them.

### PSDA.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “The simulation represents the situation.” | State the exact question, represented conditions, and omitted concerns. |
| “Three models agree, so the evidence is stronger.” | Recover whether their assumptions, data, or implementation errors are shared. |
| “Every perspective needs its own complete model.” | Retain only perspectives whose difference changes a present claim or use; use a smaller expression where sufficient. |
| “The qualitative map supplies the probabilities.” | Keep attributed beliefs separate from calibrated evidence; the missing calibration limits the claim, and acquisition needs its own receiving value. |
| “Consistency means validity.” | For a claim about the subject, use applicable evidence of the model’s validity or obtain a warranted missing check through the relevant practice. Where the relevant evidence is unavailable, leave that claim open. |
| “C.29 governs every picture.” | Open its mathematical-lens branch only for a real mathematical-lens choice that changes use. |

### PSDA.3:9 - Consequences

The recipient can see which questions each model answers and where the account stops. A contradiction may identify a useful inquiry. Reconciling assumptions and meanings costs effort, so examine the overlaps that matter to a conclusion or its grounds.

### PSDA.3:10 - Rationale

Models are complementary when their contributions jointly answer a question that the simpler account leaves open. Showing what each represents and omits makes the claims inspectable. Assurance concerns the claim about the subject and the use the recipient intends to make of it.

### PSDA.3:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How should models contribute jointly without hiding their different meanings? | Select models by the questions they answer and inspect the joins between problem structuring and analysis. | One comprehensive model is the serious default; an unconstrained collection is the rival expansion. | **Adapt:** `PSDA.3:4.1`–`4.4` choose the smallest complementary set and expose incompatible meanings. Compared with expanding one model, this deliberately accepts some correspondence work to preserve a material concern that the single model omits; it makes no universal claim of lower cost. | Marttunen, Lienert, and Belton's [2017 review of PSM–MCDA combinations](https://doi.org/10.1016/j.ejor.2017.04.041) is a critical synthesis candidate for combination benefits and interface difficulties, including value-tree and weighting issues. The reviewed applications expose possible benefits and difficulties under their own conditions. A comparative advantage in another inquiry requires evidence for that comparison. The question-led selection and non-use rule are PSDA adaptations. | Reopen if a simpler model answers the same material questions with equivalent limits, or a new mismatch shows that the chosen combination loses a consequential meaning. |
| What justifies relying on a model-supported claim? | Qualify the intended use, evidence, and losses separately from confidence in the model or its producer. | Technical sophistication, modeler reputation, or participant confidence is treated as sufficient credibility. | **Adapt:** `PSDA.3:4.3`–`4.6` and the flood-pump case retain applicability, evidence dependencies, and unresolved assumptions. The extra assurance effort is accepted only where it can change reliance; sketches remain usable for recognition. | Schwarzburg, Trauer, and Rebentisch's [2024 confidence study](https://doi.org/10.1017/dsj.2024.14) supplies bounded empirical evidence that model-, modeler-, and stakeholder-related factors are associated with confidence and reliance. Its exploratory survey and proposed application model do not validate a particular decision model or establish causal decision quality. Current `C.29` supplies mathematical mapping and loss discipline, not validation, causality, or authority. `A.1.1` supplies the three model relations used above; it applies when their claims matter to the decision. | Reopen when direct validation contradicts a relied-on claim, the use leaves its qualification window, or a current modeling practice offers the same assurance at materially lower effort. |

### PSDA.3:12 - Relations

- Use `PSDA.1` formulations where their differences guide model discrimination. `PSDA.2` can supply scope and reopening conditions for the same subject and receiving question. A qualified direct source may already supply the premise. Return a specific gap when it remains open.
- `PSDA.4`, `PSDA.5` and `PSDA.17` may use model contributions when they help assess a Method, an alternative or simultaneous inquiries. An inference about the represented situation needs evidence for that situation.
- `PSDA.7` may use the account's evidence only for the same configuration and horizon; that evidence neither entails its uncertainty judgement nor authorizes action.
- `C.29` governs load-bearing mathematical-lens use. `A.1.1` governs claims about a model's applicability, its actual use in assigned Work, and the coherence of fixed model and expression contents under a declared criterion and comparison scheme. Direct scientific, engineering, causal, and evidence practices retain their own truth and adequacy questions.
- [FPF C.28.CM](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c28cm---construct-and-challenge-a-causal-model) supplies causal construction when the needed relations are missing. Its conditional models join the account at :4.2–4.3; their causal support remains a separate question under `C.28` and :4.5.
- A model can expose a value conflict. Address its comparison and treatment on the applicable value grounds. Any subsequent choice belongs to its authorized holder.

### PSDA.3:End

## PSDA.4 - Select Problem-Structuring Methods and Combine Them When Needed

> **Type:** Method pattern body
> **Status:** Stable
>
> **Primary working result:** an **inquiry Method and its limits**, or a finding about whether a proposed way of working fits the bounded inquiry. Explain its contribution, the necessary joins in any combination, and the conditions that limit or reopen its use.

### PSDA.4:1 - Problem frame

**Use this when** you need to establish whether a proposed way of conducting an inquiry can produce its intended result with the available participants, expertise, evidence and resources. Also use it when several Methods could contribute and it is unclear how their results would fit together.

Identify the result the inquiry needs. Assess an existing or proposed Method against its conditions. Where a choice remains open, compare the serious alternatives, including a combination if one Method cannot supply the necessary contributions. Return the supported finding, selection or unresolved condition.

A **Method** (`U.Method`) is a reusable way of doing under stated conditions, with identifiable participants, intended effects and limits. Ask which way fits this inquiry and whether a proposed combination works as a whole. A description sets out the way of working, a plan schedules intended work, and a capable performer enacts it on an occasion that can be evidenced separately.

Use a direct calculation or a known sufficient Method when it answers the question. Establish the inquiry’s purpose or scope first if either is unclear. Tool procurement, a performer’s competence or authority, and scheduling a selected Method have their own criteria.

### PSDA.4:2 - Problem

A popular method can be well described and still be wrong for the current inquiry. It may require participation that cannot be obtained, assume a shared purpose that is disputed, depend on data that do not exist, or produce agreement when the recipient needs competing claims and discriminating evidence.

Combining methods creates further risks. A concern map becomes numerical weights without an elicitation basis. A scenario becomes a probability distribution. Two workshops duplicate the same task while an essential technical question remains unanswered. A schedule of activities is called an integrated Method even though no one can explain what connects its results.

### PSDA.4:3 - Forces

| Force | Tension |
| --- | --- |
| Fit | A Method must address the live difficulty, while familiar expertise makes some candidates easier to enact. |
| Participation | Joint inquiry can expose differences, while access, power, time, language, and willingness constrain genuine participation. |
| Complementarity | Several Methods can supply distinct contributions, while more methods add joins, effort, and failure opportunities. |
| Reuse and adaptation | Reusable ways make preparation and learning possible, while a local adaptation may change their identity or assurance needs. |
| Timeliness | The inquiry has a useful time window. At the deadline, report the limits imposed by any missing premise. |

### PSDA.4:4 - Solution

Assess what the candidate Method could deliver for the requested use and whether its conditions hold. Where there are live alternatives, compare their contributions and costs on common terms. For a combination, establish how its inputs, results and working conditions fit together.

#### PSDA.4:4.1 - State the required result and selection conditions

Use a compatible `PSDA.2` scope when it constrains the assessment. Use a `PSDA.3` model account where a model, its limits or a conflict bears on the fit of a candidate or a comparison.

Establish what affects fit. This can include the kind of question, the people or parties whose contributions or challenge matter, usable channels, disagreement, expertise, data, time and resources. Use applicable evidence for a participation, competence, safety or authority premise. Ask for the missing contribution when it must come from a particular participant or holder.

Check the source against the subject, condition and evidence window. If a required premise remains missing, identify it, narrow the use where that gives an adequate result, or hold the dependent work.

#### PSDA.4:4.2 - Recover candidate Methods as ways of doing

Describe what each candidate would have its performers do, which inputs they need and what result the operations are meant to produce under which conditions. Use `A.3.1` when the reusable way needs identification and these operations are already recoverable.

If evidence of performances leaves the reusable way unidentified, `A.3.1.MR` can recover provisional candidates linked to their sources, a distinguishing question or a bounded account of what remains unknown. Identifying a Method from a sufficiently developed candidate uses `A.3.1`. For documentary guidance, use `A.3.1.DR` where the meaning or status of what the source proposes is unclear.

Clarify an unclear description of a known way. Use `E.10` if an FPF kind or relation remains unresolved. When a proposal lacks a design choice about the action or its conditions, the designer can make it within the task’s authority. Otherwise identify the needed design decision and its holder where known.

For example, three accounts of past inquiries may fit both a fixed sequence with local exceptions and a rule that changes questions when someone challenges a concern. `A.3.1.MR` can investigate which account fits the performances. In a new proposal that says “interview residents”, the design question is what the interviews should return and under what conditions. Specify that if it is yours to decide, or return the missing choice to the designer. Once the proposed way is clear, it can be identified through `A.3.1`.

For example, an attributed-mapping Method elicits a participant's claims, explores their implied connections, checks the rendering with that participant, and retains unresolved differences. A conditional-analysis Method evaluates named alternatives under stated conditions with qualified models and returns consequences and limits. Compare the contributions these ways can provide under the inquiry’s conditions.

A source description can explain a Method without demonstrating its effectiveness in this inquiry. Keep instructions, reported applications, direct comparative evidence, and practitioner competence distinct. A document about several Methods is not automatically a `U.MethodDescription` of one composite Method; `A.3.2` governs that membership.

#### PSDA.4:4.3 - Assess a candidate and compare the available alternatives

Assess the candidate against the required result. When two or more are in contention, compare them on the conditions that matter to that result. For example, ask the following questions.

- Does the Method reveal the material interpretations, or does it require agreement that is absent?
- Can it use the available evidence without manufacturing precision?
- Can the participants whose contribution or challenge is needed use the available channels?
- Does it produce the kind of result the receiving question calls for?
- Can the needed expertise, time, and resources be provided?
- What important limitation or failure would remain?

Include a sufficient single Method, the incumbent or a bounded combination where each is a genuine possibility. State why any difference in result, preparation or time matters to the choice. A workshop’s popularity, reported success elsewhere or participant satisfaction needs a connection to the conditions of this inquiry before it can support the comparison.

If an important premise cannot be established in time, identify the supported provisional use or report the limit. Keep a missing prerequisite explicit in any comparison.

#### PSDA.4:4.4 - Combine contributions through explicit joins

Combine Methods when another contribution is material and one Method cannot provide it at acceptable effort. Identify the content or condition passed between them, its meaning, the receiver’s prerequisites and what happens if the join fails. Reuse a qualified result where it already supplies the required input. Assess the time, expertise and resources for the work that remains together.

An attributed concern map can supply candidate objectives. To turn them into numerical weights, use weights set by the authorized rule or decision where they apply. If the intended weights must express the participants’ preferences, establish the relevant value assumptions and use qualified elicitation evidence. A qualitative scenario supplies an analysis condition. Its probability needs separate grounds. Where a conversion lacks those inputs, keep the results in their original meanings.

Recover the order from the dependencies. One analysis may need a particular formulation before it can start. Participation inquiry and technical evidence collection can run concurrently when the common question is clear and their other prerequisites permit it. At the join, check the subject, conditions, meanings and limits. A calendar may establish the planned order. Establish required sequence from the work’s dependencies, and use evidence of performance for a claim about the order in which it occurred.

When the inquiry needs one composite `U.Method`, first identify the whole under `A.3.1`, then use `B.1.5` to qualify its independently identified part Methods and whole-forming claims. State the whole action, applicability, accepted inputs, result, required joins, allowed variations, exposed interactions, and failure or stop conditions. A different part, ordering, or interface outside the permitted variations can identify another Method.

If several Methods are coordinated and their joint arrangement answers the question, return that arrangement and its limits. If the task requires one composite Method, identify the missing whole action, join or condition before claiming that the arrangement is such a Method.

#### PSDA.4:4.5 - Assess the fragile premise and retain a stop

Examine a premise that could change the assessment. For example, can a participant challenge an attribution, can the model use the proposed scenario, and do the outputs have compatible meanings? Use sufficient existing evidence. If a rehearsal, check or trial could improve the answer, compare its attainable contribution with its full cost, delay and burden through `C.11.DUA`. Use `A.15.9` if obtaining an outside contribution is worthwhile.

Qualify a trial by what happened under its conditions. A successful rehearsal can establish that a contribution was produced in that setting. Broader effectiveness or later implementation needs evidence for those claims. If a required participant, expertise, safeguard or input is unavailable, assess another Method, adapt within the allowed variation, narrow the result or identify the blocker.

Use a Method within the scope its supported premises permit. If a deadline arrives with a required contribution missing, report the narrower result or the outstanding condition.

#### PSDA.4:4.6 - Return the assessment, selection and limits

| Result position | Content the recipient needs |
| --- | --- |
| Required use | The subject, receiving question, needed result, and current selection conditions. |
| Method under consideration | The reusable action, participants, preconditions, intended result and bounds. Identify the selected Method if the task included a choice and one was made. |
| Fit and comparative grounds | What the candidate can supply, what remains open and, where alternatives were compared, the difference in result or cost that matters. |
| Combination, if needed | Identified part Methods, real dependence or overlap, joins and adapters, whole-level conditions, permitted variation, and failure routes. |
| Reliance limits | What the available sources or trials establish and any further premises the intended use requires. |
| Reopen basis | A changed result need, participant access, evidence, scope, resource, or failed join that would alter the selection. |

A work plan identifies intended assignments and times. Establish a participant’s commitment from their agreement or a binding obligation. Permission to participate may already be in force. To report enactment, use evidence of the work. To report a subsequent result, use evidence of that result. Attributing it to the work requires evidence for that connection.

Facilitation or a simultaneous inquiry can use the assessment or selection where it fits the situation and evidence window. Qualify fit, enactment or uptake for the particular conclusion being made.

#### PSDA.4:4.7 - What changes in practice

The practitioner can explain what the candidate would contribute and where it would fail. If alternatives are available, their differences show when adapting a Method or combining Methods would improve the result.

### PSDA.4:5 - Archetypal Grounding

#### PSDA.4:5.1 - Choosing a bounded flood-pump inquiry Method

In this illustrative case, the board needs a pre-season return while service meanings remain contested and the mobile-pump branch depends on unqualified road-access evidence. The current scope and model account make two contributions material: recovering attributed service claims and testing the conditional technical premise.

The engagement designer compares three plausible ways:

| Candidate | Contribution and present limit | Selection consequence |
| --- | --- | --- |
| Capacity analysis alone. | Can examine nominal capacity, but cannot recover different service meanings or establish mobile access. | Insufficient for the declared return; retain it only as a bounded technical contribution. |
| A broad facilitated exploration of the whole flood situation. | Can expose more interpretations, but exceeds the pre-season question and available participation time. | Defer the broader inquiry; keep its boundary challenges visible. |
| Attributed mapping joined with conditional access-and-capacity analysis. | Addresses the two discriminating needs, provided attribution can be checked and technical premises have competent sources. | Select the bounded combination with explicit joins and stops. |

The proposed reusable Method applies as follows. **For a bounded intervention inquiry with contested service meanings and conditional technical feasibility, contrast attributed service claims with qualified conditional consequences, resolve only the joins needed for the receiving question, and return shared findings and unresolved contrasts without choosing the investment.**

The mapping part elicits, connects, and confirms attributed claims. The analysis part tests named configurations and conditions and reports supported consequences or exact gaps. They can proceed in parallel after the subject and conditions are fixed. Their join accepts only outputs concerning the same intervention, service meaning, and horizon; an unmatched service claim is retained as an unresolved question, not converted to a technical metric.

The whole admits written or spoken elicitation when attribution and challenge remain possible. It does not admit replacing participant confirmation with the sponsor's paraphrase. Its externally usable result is the bounded claim account; internal map-editing steps are not separately promised services. Those action, join, variation, and boundary conditions identify the proposed composite Method for the `A.3.1` and `B.1.5` questions.

Using this combination requires participants to be able to check attributions and challenge them. Without qualified access evidence, the return remains a conditional technical claim. An applicable road-access record can qualify the technical claim. Seek further access evidence when its attainable contribution to the assessment or the decision warrants the burden. Where the remaining uncertainty prevents a stronger result, return the conditional claim. The plan's date and assigned analyst are separate from the reusable Method.

#### PSDA.4:5.2 - A failed join rather than a failed workshop

A team proposes transferring the frequency of concerns mentioned in interviews into numerical criteria weights. The mapping Method yields attributed concerns, not preferences under a weighting model. The join fails even if the interviews were well facilitated.

If numerical weights are needed, use weights already fixed by an applicable rule or decision. For weights meant to express preferences, use a qualified elicitation result and its assumptions or obtain one if warranted. The team can retain the qualitative value contrast. The interviews still support the attributed concerns they established.

#### PSDA.4:5.3 - Cheap non-use

An operations team has an agreed question, a current qualified calculation Method, sufficient evidence, and no material participation or interpretation conflict. Use that Method. A new multimethod arrangement adds cost without changing the required result.

### PSDA.4:6 - Bias-Annotation

**Scope:** selection and bounded composition of Methods for problem structuring and decision analysis. **Lenses:** **Prag** tests fitness and effort; **Onto/Epist** separates Method, description, plan, enactment, and evidence; **Arch** exposes real joins; **Gov** preserves participation and authority conditions; **Did** makes the reusable action explicit.

Familiarity, a method’s brand or a tight deadline can obscure what it will deliver. Check its fit and the premise on which it depends. Compare a serious alternative if one is available. For a proposed combination, identify what each part contributes and whether their results can be joined.

### PSDA.4:7 - Conformance Checklist

- [ ] The assessment or selection addresses the requested result under the relevant scope and conditions.
- [ ] Needed model, participation, expertise, and authority premises are qualified or explicitly missing.
- [ ] The reader can recover the reusable actions required to assess the candidate Methods.
- [ ] The finding gives the candidate’s fit and limits. Where there was a choice, it explains the differences that mattered, including any sufficient simpler route.
- [ ] Each additional Method supplies a distinct material contribution.
- [ ] The results passed between Methods preserve their meaning, scope and limits. Any conversion has the additional grounds it requires.
- [ ] Real dependence and possible overlap are distinguished from document and calendar order.
- [ ] A claim about one composite Method identifies the whole and its parts. A coordinated arrangement is described at the scope it supports.
- [ ] Fragile premises, allowed variation, failure routes, and local reopen conditions are stated.
- [ ] Any claim about enactment, participant commitment, effectiveness or authority has grounds for that claim.

### PSDA.4:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “We always run this workshop.” | Check whether the workshop supplies the required result under these conditions. Compare a serious alternative where the choice remains open and an alternative is available. |
| “The agenda is the Method.” | State the reusable action and applicability separately from dated scheduling. |
| “The techniques appear in order, so they compose.” | Establish the dependencies, identities of part Methods, whole action and joins relevant to the composition claim. |
| “The qualitative output can be scored numerically.” | Identify the extra elicitation, measurement, or model assumptions; otherwise retain the qualitative result. |
| “The method worked elsewhere.” | Carry the source's subjects, conditions, evidence limits, and actual contribution into this selection. |
| “A shorter deadline removes the need for that input.” | Narrow the declared return or stop; do not mark the missing contribution as completed. |

### PSDA.4:9 - Consequences

The assessment explains what a candidate can deliver and what could defeat its use. Comparing candidates and qualifying a composite takes time, particularly when a join needs new evidence. The result may be an adequate single Method, a coordinated arrangement, a qualified composite, a supported trade-off or a specific remaining gap.

### PSDA.4:10 - Rationale

A Method fits when its action can supply the inquiry’s result under the available conditions. Recovering the actions and their joins explains whether a combination can work. A plan describes intended work. Evidence of enactment shows what the performers did.

### PSDA.4:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| Which PSM contribution fits the engagement? | Compare assumptions, contributions, conditions, and needed outcomes; retain a simpler sufficient route. | A familiar branded PSM is used as a default regardless of the difficulty. | **Adapt:** `PSDA.4:4.1`–`4.3` assess the ways of working and compare their limits when alternatives are available. A short comparison costs more than automatic selection but is justified when a missing contribution can reverse the return; it does not require a full method catalogue. | Smith and Shaw's [2019 PSM characterization](https://doi.org/10.1016/j.ejor.2018.05.003) is a conceptual comparison candidate that makes differences among approaches inspectable; its exploratory family characterization is not a method-ranking algorithm. Lami and Tavella's [2019 workshop comparison](https://doi.org/10.1016/j.ejor.2018.12.016) supplies bounded counterexample evidence to a uniform-usefulness claim: outcomes varied across SCA, SSM, and self-organized workshops in an exploratory MSc-student study. It establishes no universal winner or professional-field effectiveness. | Reopen when the intended outcome or participation conditions change, or better comparative evidence changes the fit of a serious candidate. |
| When does combining Methods improve the result? | Require a distinct contribution and an intelligible join; qualify a composite Method only when its whole action is recovered. | More techniques, a sequence diagram, or an agenda is treated as an integrated Method. | **Adapt:** `PSDA.4:4.4`–`4.6` and the failed-weighting example expose the conversion or missing result. **Adopt:** `A.3.1`, `A.3.2`, and `B.1.5` keep reusable way, description, whole-forming facts, and enactment distinct. Extra join work is accepted only for a material contribution; otherwise the single-Method alternative wins. | Marttunen, Lienert, and Belton's [2017 PSM–MCDA review](https://doi.org/10.1016/j.ejor.2017.04.041) supplies the critical combination line and concrete interface difficulties, not evidence that arbitrary mixtures work. The current FPF patterns supply identity and composition rules, not empirical validation of this engagement Method. | Reopen when a join loses meaning, a part or whole identity changes, a critical precondition fails, or a single Method supplies the same useful result at lower effort. |

### PSDA.4:12 - Relations

- `PSDA.2` can supply scope and purpose for the present subject. Use a `PSDA.3` model account where it affects the assessment or comparison. Use a qualified direct result for a missing premise or return the gap.
- `PSDA.13` and `PSDA.17` may use the result within the situation and qualification window it covers. Claims about later use or sustained uptake depend on what subsequently happens.
- `A.3.1.MR` recovers provisional candidate accounts from performance evidence; `A.3.1.DR` recovers the source meaning and status of documentary contributions when needed. `A.3.1` identifies a ready candidate way without making either recovery compulsory. `A.3.2` governs a description of one identified Method; `B.1.5` governs the composite qualification when needed.
- `A.15.2` governs intended Work and `A.15.1` actual Work and its enactment relation. Direct competence, participation, authority, evidence, and safety practices govern their own premises.
- Obtain a missing domain result when the intended use needs it and its acquisition is warranted.

### PSDA.4:End

## PSDA.5 - Generate Decision Alternatives

> **Type:** Method pattern body
> **Status:** Stable
>
> **Primary working result:** a finite **candidate set** for the inquiry. Identify the alternatives, the material distinctions among them and the grounds and unresolved conditions for their intended use. If only one direction or none is supported, give that result and its basis.

### PSDA.5:1 - Problem frame

**Use this when** an inquiry has clarified what matters but the proposed decision still contains only the incumbent, a sponsor's preferred project, or two labels such as “buy or build”. Also use it when a request for development advice names a course, provider, reorganization, or AI tool before the possible directions have been constructed.

Identify what action could address each material formulation or concern. Where a useful alternative is missing, vary the mechanism, arrangement, timing, combination or commitment. Describe each resulting candidate in enough detail for its intended comparison. Name any material gap that remains.

A candidate describes a possible intervention or commitment. Establish feasibility, permission, performance and benefit to the extent required for the intended use. Where candidates address different formulations, retain their different consequences in the comparison.

Use an adequate existing set directly for comparison or an authorized choice. Use the relevant domain practice if it already answers the alternative-generation question. A development-advice task needs a recipient or chooser for the subject concerned. For a population with neither, distinguish a researcher’s authorized intervention from advice to the population.

### PSDA.5:2 - Problem

An apparently open choice can be closed before analysis begins. A list of pump models omits deployment arrangements; a list of training courses omits changing the Work that prevents capability expression; a list of AI models omits the tool, data, or operating configuration responsible for the failure.

Unrestricted ideation can repeat the same intervention under hundreds of names, depend on unsupported capacities or combine benefits that cannot coexist. Check the distinguishing consequence and the conditions for using each candidate. A workshop can identify a promising idea while its feasibility remains open.

### PSDA.5:3 - Forces

| Force | Tension |
| --- | --- |
| Breadth and relevance | A different mechanism may expose a better direction, while an unbounded search consumes the decision horizon. |
| Plural formulations | Alternatives should address material interpretations without pretending that every interpretation seeks the same result. |
| Imagination and qualification | A proposal may be worth investigating before feasibility is known, while unsupported proposals cannot be presented as ready commitments. |
| Combination and interaction | Hybrid or staged directions can preserve options, while shared resources, incompatibilities, and delay can remove their apparent advantage. |
| Generation and choice | Early preference helps identify concerns but can suppress candidates before their consequences are known. |

### PSDA.5:4 - Solution

Construct or complete the alternatives the question needs. Give each one enough content for its intended use. Distinguish a missing qualification from an established reason for exclusion. Return the bounded set or the particular alternative that remains missing.

#### PSDA.5:4.1 - Recover the receiving question and useful inputs

Identify the subject, question, horizon and any current arrangement. Establish applicable protections and resource limits. For advice or a proposed commitment, identify the recipient and the holder of the relevant decision or resource right where the task depends on them. Name any missing purpose or authority that limits what can be returned.

Use `PSDA.1` where different formulations suggest different actions. Use a `PSDA.3` model account where it distinguishes mechanisms or exposes a missing consequence. A `PSDA.13` result may contribute an agreed observation or a contested claim that affects candidate construction.

Use a qualified direct result where it supplies the needed premise. If a premise is missing, stale or incompatible with the subject and horizon, identify the specific limit on the candidate.

#### PSDA.5:4.2 - Vary the decision-changing contents

Clarify the desired consequence, why it matters and what else could produce it. If early advocacy could anchor a group, have participants first generate ideas independently. Use relevant differences or objections to complete a candidate or construct a materially different one.

Consider changing the mechanism, obtaining arrangement, scale, timing, resource allocation or commitment. Other possibilities include combining compatible actions, retaining the present arrangement, declining a change or obtaining information before committing. Use the prompts that expose a material alternative.

When the known menu supplies no way to obtain a material desired consequence, use [PSDA.6:4.2](#psda642---distinguish-ends-means-and-repeated-consequences) to distinguish that end from the initially proposed means. Where their relationships need construction, use the backward branch of [PSDA.8:4.2.1](#psda8421---construct-and-question-a-qualitative-consequence-network): trace necessary conditions and possible sufficient routes, propose a combination of means, and test that whole combination forward under the same assumptions. Return the resulting alternative here with its conditions and open transitions. An incompatible combination prompts another construction or a revised formulation; it does not prove that the desired result is impossible. Reuse an adequate direct construction without building another network.

Describe the baseline for “no new action”. It may include authorized maintenance, contractual duties, continuing costs, deterioration or exposure.

For a staged direction, describe the first action, the later choice, evidence that could inform it and any delay or irreversible consequences. Establish the feasibility, consent, safety and recovery conditions needed for a claim about reversibility. A small initial commitment can have lasting effects.

#### PSDA.5:4.3 - Turn labels into sufficiently complete candidates

Give the material change from the baseline, affected subjects, intended result, enabling conditions and substantial burdens for each candidate. Identify the evidence and any unresolved premise the next use needs.

Use `C.38` when several whole ways aim at the same receiving result and their descriptions still hide different burdens. When they aim at different results, preserve that difference in the comparison.

A combination is a distinct candidate where interactions can change its consequences. Check the needed resources, dependencies, sequencing and compatibility of assumptions. For example, each branch may require the same qualified crew at the same time. A provider advertisement, course title or benchmark may suggest a candidate. Its fit for the holder needs evidence for that use.

#### PSDA.5:4.4 - Distinguish exploration from a live commitment option

Keep a promising proposal available for inquiry and identify the conditions for commitment. For example, it may be ready for a bounded comparison, require a stated qualification, or be excluded by an applicable constraint.

Use an adequate specialist result where it exists. If a consequential feasibility, allocation, transfer or security premise remains open, identify the affected candidate. Seek an outside contribution through `A.15.9` if its attainable use warrants the full acquisition burden under `C.11.DUA`. A gap in one branch can leave the others available.

Use `C.17` to characterize a claim about novelty, diversity or usefulness. Use `C.18` for open-ended generation or stewardship of an archive or front. Use `C.19` for a live-pool policy question. Seek each contribution where the task needs it. The decision holder chooses among alternatives on the applicable grounds.

#### PSDA.5:4.5 - Challenge coverage and stop proportionately

Check whether a favoured formulation, a familiar technology or a powerful participant’s concern has obscured another material mechanism, baseline, combination or staged probe. Merge names for the same action and conditions. Retain differences that change consequences, eligibility or the grounds for use.

Stop when the candidates or stated gaps cover the material differences for the requested comparison, each candidate is intelligible and protected-condition exclusions are clear. Continue searching where an attainable additional alternative would warrant the effort.

If only one lawful direction remains, report its conditions and the grounds for its unique eligibility. Give the reasons for excluding other directions if any were considered. If none remains, distinguish a missing qualification, an infeasible requirement and a reason to reopen the formulation.

#### PSDA.5:4.6 - Return the set without making the choice

Return the subject, question, horizon and candidate descriptions. Include their material differences, supported conditions, any gap or exclusion and its grounds. Identify a change that would affect the set where it matters to later use. Choose a form the recipient can use to recover these distinctions.

`PSDA.8` can use the set in a consequence comparison with the appropriate value, evidence and scope basis. Use the result for ranking or recommendation when that work is requested. A choice belongs to its authorized holder. A later programme, work plan, enacted intervention or achieved effect each requires its own grounds.

### PSDA.5:5 - Archetypal Grounding

#### PSDA.5:5.1 - Flood-pump alternatives beyond a purchase contest

In this illustrative case, the board needs a pre-season return for the next flood season. The inquiry distinguishes nominal capacity, deployment reliability, unequal service, and downstream consequences. The model account says that nominal permanent and mobile capacity can meet the assumed inflow when the stated units are operating, but mobile arrival under road loss is not yet supported. Reachable assistance remains a separate service concern.

The inquiry turns those premises into three candidate descriptions and one unfinished proposal for staging:

| Candidate | Different action being considered | Present use and gap |
| --- | --- | --- |
| N — continue the present arrangement | Continue authorized operations and maintenance without a new capacity commitment. | Compare with the ongoing service and costs under N. Its adequacy remains a separate question. |
| F — fixed-capacity change | Add fixed capacity with the necessary operating, staffing, and support arrangement. | A proposed whole change; direct engineering and service results must qualify its consequences. |
| M — mobile-reserve arrangement | Obtain mobile capacity together with its transport, deployment, staffing, and access arrangement. | Retained for inquiry; the road-loss deployment premise prevents an unconditional commitment claim. |
| S — unfinished staged proposal | The proposal would preserve a later capacity choice informed by an access or service inquiry, but its first intervention has not been specified. | Keep the construction question open: what should change first, and how would that permit the later choice? Specify that intervention and qualify its temporary provision, resource overlap, delay and recovery before comparing S as a distinct direction. Adding the benefits of F and M does not answer these questions. |

The property-protection and reachable-assistance concerns remain distinct. They lead the team to ask whether each whole arrangement serves both; they do not establish an approved priority between them. No candidate is dropped because its proponent dissents from the majority.

Return N, F and M within their stated limits. For S, retain the question about the first intervention. A commitment-ready M needs its access premise. S still needs its first intervention to be specified and qualified. The bounded set already supports the comparisons for which the inputs are sufficient.

**A further construction round.** Suppose the recipient now asks for a pumping arrangement that can be deployed on the isolated side when the bridge is closed. PSDA.6 separates that end from the proposed means “deliver the reserve unit by road”. Working backward through PSDA.8:4.2.1 gives another route: put a unit, a competent crew and their required supplies on that side before closure. The first combination borrows the crew of an existing fixed station. Testing it forward exposes an incompatible condition: operating both arrangements during the flood needs that same crew at both sites. This candidate cannot claim both services.

The team constructs L: pre-position a leased unit and supplies at a suitable local site, with a separately available crew and an agreed local activation arrangement. For this teaching continuation, assume that the responsible specialists have established site suitability, equipment and crew availability, the relevant operating permissions, and provision for the named flood duration; the cost fits the stated comparison budget. With those premises, the forward trace no longer depends on the bridge or double-allocates the fixed-station crew. L is a new comparison-ready alternative for the specified deployment result. Its cost, capacity, service distribution and other material consequences still need comparison; investment selection and demonstrated deployment each need their own grounds. If the separate crew cannot be obtained, retain that exact gap or reopen the service formulation instead of silently restoring the double allocation.

#### PSDA.5:5.2 - A ninety-day development-direction question

An advisory team is asked which direction a service organization should consider for a ninety-day reliability horizon. “Train, outsource, or use AI” is not yet a set of comparable directions. The adviser resolves the labels into internal development with covered service duties, a qualified provider arrangement, and a mixed human–tool arrangement with specified oversight and fallback. A bounded mixed-arrangement probe is a separate candidate when its information and operating consequences differ from deployment.

For the internal branch, establish what the available human evidence supports about transfer to the representative work. For the provider, establish interface and security fit. For the mixed arrangement, qualify reliability in the operating configuration. A missing allocation result can limit the comparison. Report the comparisons that remain supported and the missing allocation premise that limits a ranking.

For advice about one person, the same move generates directions only from qualified human and target-Work premises. For an AI arrangement, it distinguishes parameter, data, scaffold, tool, code, and environment changes only where the case makes those objects live. Use evidence for the mechanism and subject underlying the particular direction.

#### PSDA.5:5.3 - Cheap non-use

A recipient already has two complete, qualified ways of obtaining the same repair result and asks which to choose. Use the existing set and the applicable comparison or `C.11` choice guidance. Another brainstorming exercise adds no candidate-changing result.

### PSDA.5:6 - Bias-Annotation

**Scope:** alternatives for bounded decision inquiries. **Lenses:** **Prag** tests useful differences; **Onto/Epist** separates proposed arrangements from facts; **Arch** exposes combinations and dependencies; **Gov** preserves protected conditions and later authority; **Did** replaces label lists with intelligible candidates.

Incumbency, sponsor anchoring, technology availability, and novelty bias can each shrink or distort the set. Challenge the omitted mechanism and baseline, not merely the number of ideas. Counter the opposite bias toward endless variety by asking which attainable candidate could change the comparison or the grounds for it.

### PSDA.5:7 - Conformance Checklist

- [ ] The receiving question, holder or subject, current arrangement and horizon are recoverable; the recipient and separate choice boundary are stated where that use requires them.
- [ ] Any formulation, model or inquiry result used contributes to a candidate, its conditions or its grounds.
- [ ] Distinct alternatives have a material difference in action, conditions, consequences or use.
- [ ] The baseline includes applicable ongoing obligations and consequences.
- [ ] Combinations and staged directions expose interactions, delay, and unresolved enabling conditions.
- [ ] Supported, proposed, and unknown premises remain distinguishable.
- [ ] Material gaps and exclusions are identified with their grounds.
- [ ] The stopping point is justified for the requested use and attainable further search.
- [ ] The return distinguishes the set or identified gap from a later selection, commitment, implementation or benefit.

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

The recipient gets a bounded set of candidates or an explanation of a missing direction. Constructing and qualifying additional candidates costs effort. Concentrate it on omitted differences that matter to the comparison or its use.

### PSDA.5:10 - Rationale

Differences in a formulation matter to choice when they change the available actions, conditions or consequences. An alternative can be worth investigating while its feasibility or authorization remains open.

### PSDA.5:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How can an engagement escape the incumbent without producing a decorative idea list? | Use objectives and materially different mechanisms to guide alternative construction. | Unstructured group brainstorming is cheap; a supplied option menu is cheaper still. | **Adapt:** :4.1–:4.3 add concern-led prompts and independent generation where anchoring matters. The deliberate cost is a short construction pass before comparison; an adequate existing set takes the cheap exit. | Borgonovo et al.'s [2026 decision-analysis review](https://doi.org/10.1016/j.ejor.2025.05.023), especially its value-focused-thinking discussion, is a current synthesis candidate. Keeney's [2012 value-focused brainstorming](https://doi.org/10.1287/deca.1120.0251) supplies the specific objective-led and individual-before-group procedure. Its policy example is not universal effectiveness evidence. | Reopen if a simpler elicitation gives the same material breadth or the objectives themselves suppress a live formulation. |
| When is a staged alternative genuinely different? | Preserve options only through explicit dependencies, observations, and feasible later changes. | Compare only fixed end-state projects, or label an underspecified pilot “adaptive”. | **Adapt:** :4.2–:4.4 require a specified and qualified first commitment, later question, and delay or lock-in consequence. The unfinished S example shows why a staging label is insufficient. Additional description is justified only when timing changes the comparison. | The [2019 DAPP chapter](https://doi.org/10.1007/978-3-030-05252-2_4) is the best-known-line candidate for pathway dependencies and failure conditions; its water-policy applications do not supply PSDA's local thresholds, authority, or universal sequence. | Reopen when monitoring, lead time, or reversibility makes the staged direction infeasible or no longer distinct. |
| Does a novelty result already supply the alternatives? | Keep characterization, generation stewardship, and local choice separate. | Read a novelty profile or archive as a ready option set. | **Adopt:** :4.4 uses C.17 for characterization and C.18 for generation stewardship; :4.6 retains the PSDA candidate result. This avoids reconstructing machinery when ordinary candidate descriptions suffice. | Current `C.17` characterizes bounded novelty or use; `C.18` governs generation, archive, and front stewardship; `C.38` forms same-result ways. Their exact boundaries defeat the broader reading, but none supplies holder feasibility. | Reopen only if a direct contribution or the receiving candidate question changes. |

### PSDA.5:12 - Relations

- `PSDA.1` supplies formulation differences for candidate formation, not selected actions. `PSDA.3` supplies discriminating model claims, not the obtaining conditions they represent. `PSDA.13` supplies shared and contested inquiry claims only where they change the set; dissent remains explicit.
- `PSDA.6:4.2` distinguishes desired ends from proposed means. When a missing alternative requires a new means combination, `PSDA.8:4.2.1` supplies backward construction and its forward test; return the candidate and its conditions to :4.3. `PSDA.8` may then consume the set for the named consequence comparison. Generation does not select.
- `C.17`, `C.18`, `C.19`, and `C.38` supply characterization, generation stewardship, live-pool policy, and same-result construction only under their own use conditions.
- `A.15.9` supplies bounded use of an outside-practice result and selection of a worthwhile further request. Direct holder and domain practices supply feasibility, mechanisms, protected conditions, and evidence.
- Use `C.11` for a later local choice over an adequate option set. Use an applicable source to establish a missing premise or return the specific gap.

### PSDA.5:End

## PSDA.6 - Represent Values and Trade-Offs

> **Type:** Method pattern body
> **Status:** Stable
>
> **Primary working result:** a **decision-usable value account**: attributed concerns and objectives, their consequence measures, protected conditions, admitted trade-offs, unresolved disagreements, and limits for one named comparison.

### PSDA.6:1 - Problem frame

**Use this when** a scorecard's criteria came from a template, “importance” weights have no stated meaning, or the same benefit appears under several headings. Also use it when people agree that reliability, development, safety, or fairness matters but mean different consequences for different subjects, or when their consequence comparisons still need to become a justified numerical model.

For each relevant concern, identify who holds it or bears the consequence, the subject and conditions, and why it matters. Connect it to the consequence that should enter the comparison and state how it is represented. Establish whether trade-offs are permitted and on what grounds.

An objective expresses what is wanted. A measure describes a characteristic. A preference orders consequences, while a protected condition limits the permissible trade-offs. Use the governing basis for a duty and for any affected party’s rights. Establish whether a change or exception is permitted and, if so, who can authorize it. A preference or weight grants no such power.

Use a current, qualified value account directly when it answers the comparison. For a missing measure, use the relevant measurement practice. For a condition’s current force, use the applicable rule, decision or domain evidence. For a disputed requirement’s justification, use `C.11.DUA`. A later choice, if needed, belongs to its authorized holder.

### PSDA.6:2 - Problem

Criteria can appear neutral while deciding the result. “Install more pumps” embeds an action in an objective. “Service quality” may count the same avoided outage again under reliability, satisfaction, and reputation. Equal weights may silently favor the concern represented by the largest number of criteria.

Numbers can conceal a second substitution. A budget amount, a probability, an ordinal judgement, and a protected condition become interchangeable entries in a spreadsheet. Normalizing each to zero–one does not establish comparable value. A mean of participants' weights can erase a disagreement about who bears the consequence or what may be traded at all.

### PSDA.6:3 - Forces

| Force | Tension |
| --- | --- |
| Completeness and usability | Material values must remain visible, while an enormous hierarchy burdens elicitation and repeats consequences. |
| Measurement and meaning | Observable measures help comparison, while easily measured proxies can displace the concern relevant to the comparison. |
| Trade-offs and protection | Some sacrifices are legitimate within the question; others require a separate authority or are outside permissible compensation. |
| Individual and collective values | A common comparison is useful, while unlike participants need not share one value function. |
| Precision and honest incompleteness | Explicit scales and preference questions can clarify a choice, while unsupported weights create false precision. |

### PSDA.6:4 - Solution

Identify the concerns and objectives the comparison is meant to represent. Organize them around consequences. State the measurement and trade-off rules, their grounds and any unresolved preferences or protected conditions. If the task supplies hypothetical parameters, use them for the conditional comparison it asks for.

#### PSDA.6:4.1 - Recover whose concern changes the comparison

Identify the subject, affected people or Systems, configuration, horizon and receiving question. A compatible `PSDA.12` account may establish attributed concerns, duties, interests, missing voices or limits of representation. Establish any value transformation or authority to combine preferences on its own grounds.

For each material concern, establish who expresses it or bears its consequences and under which conditions. Where representation or governing force depends on an assignment, role classification or authority relation, use evidence that the relation holds. A title such as resident, manager or expert identifies a possible contribution without establishing a mandate.

Use a qualified source for a needed concern or binding condition. Where one stays unavailable, state the gap. Distinguish a participant’s statement, the analyst’s interpretation, a stipulated analytical assumption and an established obligation. Non-response leaves the participant’s preference unknown unless other pertinent evidence establishes it.

#### PSDA.6:4.2 - Distinguish ends, means, and repeated consequences

Ask “Why does this matter here?” to identify the consequence sought. Ask “How might it be achieved?” to expose possible means. “Provide training” may be one means; reliable performance in representative later Work may be the relevant end. The distinction is local to the question: a process experience can itself be valued when the participants value it in its own right.

Organize objectives only as far as the structure helps. For a small decision, a few attributed statements may be enough. A hierarchy or means–ends map is useful when several levels or overlaps would otherwise be lost.

Trace apparent duplicates to the consequence represented. Count that consequence once. Service loss and its distribution can be distinct values even when their measures covary. Statistical independence of measures supplies no preference rule for adding their values.

Retain a material value, protected condition or distinction that matters to the requested comparison. Before simplifying, identify what would be lost and examine its effect on the ranking, explanation or ability to detect a protected loss. Difficulty of measurement can leave a value unresolved.

#### PSDA.6:4.3 - Give each measure a usable meaning

For every consequential measure, state the characteristic, subject or participant tuple, scale and unit where applicable, direction of preference, horizon, source, and missingness rule. Distinguish a direct measure from a proxy and say what the proxy cannot establish.

Use `C.16` for measurement and `A.19` where the inquiry needs a declared multi-characteristic space or reusable predicate. `A.19` defines coordinate and scale meanings. Scoring, aggregation and selection need their respective rules.

Keep the raw consequences alongside the value transformation. An ordinal judgement supports ordering. Equal intervals, arithmetic averages and interpolation require additional grounds. For a numerical value function, state the consequence range, anchors, shape or interpolation and the basis for its use. Identify whether it comes from attributed comparisons, an applicable rule or assumptions stipulated for a conditional analysis.

#### PSDA.6:4.4 - Separate conditions from compensable objectives

Distinguish a binding condition from an aspiration and from an unresolved claim about a condition. Identify its subject, scope and source. A requested service minimum may express a value. An existing legal or safety requirement can govern whether compensation is permitted.

Exclude compensation for a failed binding condition. If its meaning or applicability is disputed, use an applicable governing interpretation. Where a new ruling is needed, seek it from the authorized holder or identify the outstanding question. A narrower comparison can remain useful while the whole decision stays blocked.

When the live question is whether the requirement itself should be retained or changed, use `C.11.DUA` §4.3 with the competent domain contribution. Identify the protected person or System and interest, unwanted outcome, governed quantity or activity, conditions and horizon. Distinguish background, attributable increment and total exposure where they affect the judgement. Examine the causal and measurement basis, uncertainty, threshold or precision choice, marginal protection, full burden and displaced protective work. Compare retention, tightening, revision, replacement or removal only where they are meaningful alternatives. A safety label does not supply that basis, and expense alone does not defeat a protective requirement.

For a requirement appraisal, return the conclusion or recommendation the evidence supports and any important limit. Identify the condition’s current force. If amendment is at issue, identify authority and timing. When no acceptable alternative or timely amendment is feasible, state the impasse. A later correction may leave an earlier opportunity lost. An ordinary value account can finish without a separate appraisal.

Some thresholds are preference choices rather than prohibitions: an aspiration level, budget preference, or tolerated inconvenience. Say which they are and whose judgement they express. A threshold crossing is not automatically a decision or permission to act.

#### PSDA.6:4.5 - Construct preferences from comparisons of consequences

For an account of a holder’s preferences, use attributable comparisons of concrete consequence profiles for the same people, horizon and conditions. Obtain a judgement from the holder if the needed comparison is missing and worth obtaining. Preserve whether one profile is **no worse**, **strictly better**, **indifferent**, or the comparison remains open. Keep the profiles and any stated reason. Use alternatives or intelligible hypothetical profiles within the declared ranges. If the task specifies a rule or hypothetical preference instead, report conclusions under that basis.

Sections 4.5.1–4.5.5 treat known consequences. For uncertain outcomes, §4.5.6 uses comparisons of lotteries, preserves the compatible utility functions and relates them to the consequence probabilities. Choose the form for the distinctions the task needs. Deterministic trade-offs alone leave the ranking of some uncertain alternatives open.

##### PSDA.6:4.5.1 - Choose and challenge the representation

Separate protected conditions under §4.4 before considering compensation. Identify what the representation must preserve and use the least burdensome form adequate for the comparison. The following situations call for different forms.

| Available judgement and intended use | Construction and return |
| --- | --- |
| Only directions of improvement and some pairwise comparisons are justified. | Keep those comparisons and coordinate dominance. Infer further comparisons only through an admitted rule, such as transitivity. Return the resulting partial relation and the pairs still open. |
| A priority or threshold is explicitly noncompensatory. | Write and apply that rule, including its order and tie treatment. For example, prefer every profile with waiting time at most two hours to every profile above two hours, then prefer lower cost within each class. Attribute the rule to a holder only on evidence of that judgement. A task can also stipulate it for a conditional comparison. A binding duty needs its own governing basis. |
| Improvements can compensate for one another, with constant value increments and a constant exchange over the stated ranges. | Construct the affine family in §4.5.2. Its coefficients express the admitted exchange, not the importance of criterion names. |
| Compensation is acceptable but marginal values may curve. | Test the additive assumption and use the finite-level construction in §4.5.3 when it fits. Preserve interactions through a suitable non-additive family or explicit rules when addition fails. A qualified outranking Method can instead supply a relation with incomparability; its thresholds and aggregation conditions must be supplied with it. |

For a proposed additive form, compare profiles that differ on a subset of criteria while holding the others equal. Use comparisons at materially different common levels of those other criteria, obtaining further judgements where the available evidence leaves the issue open. A reversal challenges preferential independence: the preference over that subset depends on its background. Ask also about complementarities, thresholds and refusals to compensate. With two criteria, unchanged directions of preference alone give little support for addition; ask about the exchanges themselves. Statistical independence of measurements answers neither question.

For an affine form, ask two further questions. Do equal physical increments have equal value at different positions on each scale? Does the compensating amount stay the same across starting profiles? Within a one-to-five-hour range, compare reducing two hours to one with reducing five hours to four, and repeat a cost-for-time exchange at a different cost level. A stated constant exchange is a substantive modelling assumption over that range. Finite elicitation can challenge it and check its local fit; it does not prove a universal preference law. Preserve that qualification when the assumption is accepted for use, and return the unresolved form choice when it is not.

Keep materially different holders’ accounts separate unless a legitimately governed aggregation or reconciliation Method supplies the joint relation. State that basis when using a collective result.

##### PSDA.6:4.5.2 - Construct a family for a constant exchange

Suppose lower cost `c` and lower waiting time `t` are preferred, both matter, and the holder accepts the affine conditions above on the named ranges. Represent loss by `L(c,t) = a c + b t`, with `a > 0` and `b > 0`; lower loss is preferred. A common constant and positive scale do not change the ordering. Divide by `a` to obtain `L_r(c,t) = c + r t`, where `r = b/a > 0`. The unit of `r` is cost units per hour. Here it represents the holder’s admitted cost-for-time exchange over the stated range. A market price is a different quantity.

For each statement that profile `(c_x,t_x)` is no worse than `(c_y,t_y)`, write `c_x + r t_x <= c_y + r t_y`. Use equality for stated indifference and a strict inequality for stated strict preference. Keep every statement on the same `r` and intersect its restrictions with `r > 0`. The resulting set `R` describes every admitted exchange in this form. A convenient point in that set can be used for a stated scenario. Attributing that particular exchange to the holder needs evidence of their judgement.

Ranges still matter when scales are normalized. If the cost range is 20–60 thousand and the waiting range is 1–5 hours, normalized losses are `(c-20)/40` and `(t-1)/4`. A weighted sum with positive weights `w_c + w_t = 1` represents the same exchange only when `r = 10 w_t/w_c`. The weights compare the two whole range changes. A different range changes that correspondence; a change in the holder's marginal values can require a different function as well. Unit conversion alone must leave the represented comparisons unchanged.

##### PSDA.6:4.5.3 - Retain unknown marginal values when linearity is unwarranted

For a finite comparison with an admitted additive form, use the distinct consequence levels appearing in the reference profiles and live alternatives. Order each criterion's levels from least to most preferred. Assign an unknown value contribution `q_i(z)` to each level `z` of criterion `i`. Set the least preferred contribution on each criterion to zero, require the contributions to be nondecreasing along that criterion, and set the sum of the most preferred contributions to one. This normalization requires at least one valued improvement across the represented ranges; it fixes an arbitrary origin and unit without fixing relative criterion values. If the holder is indifferent across every represented profile, return that relation directly. If the evidence leaves open whether any difference matters, retain that uncertainty.

Define `U(x) = sum_i q_i(x_i)`, with higher value preferred. Each no-worse statement `x` versus `y` adds `U(x) >= U(y)`; indifference adds equality; strict preference adds `U(x) > U(y)`. Add elicited bounds or comparisons of value differences only with their own meaning and source. All rows constrain the same contributions. Solving them jointly supplies a family of additive value functions, rather than independently chosen intervals for each criterion. Weak monotonicity permits a flat contribution; require strict increase only where the holder's judgement supports it.

This construction leaves unevaluated levels open. Add a new level with its monotonicity and preference constraints, or use an explicitly justified interpolation. Equal spacing on an ordinal performance scale is not equal spacing in value. A family that is feasible at the represented levels establishes compatibility there; use beyond them needs an applicable shape assumption or evidence of preferences at the additional levels.

The constraints are linear in the unknown contributions. Use direct algebra for a small family or a linear-programming solver for the finite system. When strict comparisons are present, a solver can replace each strict difference by a common positive slack `epsilon` and maximize that slack under the normalization: a feasible result with `epsilon > 0` witnesses joint strictness. A fixed arbitrary margin can exclude compatible models. Preserve weak equalities and numerical error limits when interpreting a computation. `MMP.10` and `MMP.11` supply the general formulation, representation and obtaining-method work; the consequence meanings and preference assumptions supplied here govern this instance.

##### PSDA.6:4.5.4 - Distinguish an open answer from a failed construction

First check whether at least one model satisfies the joint constraints. For a small interval family, exhibit an admitted parameter; for a larger system, obtain a feasible witness or a justified infeasibility result. A solver timeout leaves this question unanswered.

If the family is empty, locate a conflicting subset of the elicited rows and form assumptions. Check transcription, units, profile meanings and attribution against the available sources. Seek clarification from the holder where the intended judgement remains uncertain. Two opposite weak comparisons may express indifference; they are not a contradiction. A strict preference for `x` over `y` together with `y` no worse than `x` under the same conditions conflicts with the claimed preference relation. Other failures can arise because the chosen form cannot express otherwise coherent judgements. Do not resolve either failure by silently deleting a row or returning the best fitting weights. Revise a judgement only with its holder, change the form with an explicit basis, or return the unresolved conflict. An approximate fit needs an admitted error interpretation before it can support advice.

For a **nonempty** family, distinguish what all compatible models support from what at least one supports:

- `x` is **necessarily no worse** than `y` when every compatible model gives that weak preference.
- `x` is **possibly no worse** than `y` when at least one compatible model gives it.

Test these claims on the joint family. For the loss family, necessary preference requires `L_r(x) <= L_r(y)` for every `r` in `R`; a possible preference needs one such `r`. A proof over the range establishes necessity; one feasible witness establishes possibility and one contrary witness defeats necessity. Use `MATH.20` for the required whole-domain bound. Separate strict preference from equality at a boundary. An empty family warrants neither kind of recommendation.

If the question asks for a best alternative, keep the quantifiers together. A necessary best is no worse than every rival in every compatible model. A possible best is no worse than every rival in **one and the same** compatible model. Separate pairwise witnesses against different rivals do not establish possible best. Return a common best when supported, the condition-dependent alternatives otherwise, or the precise comparison gap. No probability distribution over the compatible models is implied.

##### PSDA.6:4.5.5 - Reopen only what the changed judgement affects

A further judgement by the same holder on the same profiles adds a constraint to the existing family. Intersect, check nonemptiness again, and recalculate the dependent comparisons. A correction replaces its old row and every restriction derived from it; retaining the superseded row could manufacture a conflict. Preserve consequence measurements, protected conditions and comparisons whose grounds remain valid.

A changed holder, horizon, range, consequence meaning or compensation rule can invalidate the representation itself. Reconsider that premise before intersecting parameters in the old form. State which results depend on it and which remain usable. Stop when the receiving comparison is settled to the needed strength or the outstanding judgement, form or authority and its effect on the conclusion are identified.

##### PSDA.6:4.5.6 - Construct preferences over finite uncertain outcomes

Use this branch for a comparison of uncertain consequences under expected utility. A lottery is a probability distribution over specified consequences, which may be complete profiles of cost, delay and service. If a task supplies the utility function, consequence probabilities and their conditions, go directly to **Connect preference to the consequence model** below and report the conditional ranking. To represent a holder’s preferences, establish the applicability of expected utility and use attributable lottery judgements for any missing utility values. Those judgements can concern hypothetical lotteries without exposing anyone to an actual gamble.

**Choose the representation before estimating it.** Expected utility evaluates a lottery `P` by `sum_x P(x) u(x)`. For an attributed account, its utility values represent the holder’s comparisons of lotteries. Stipulated values instead define a conditional analytical account. A function that orders certain outcomes alone does not determine the ranking of lotteries. In particular, any increasing transformation preserves a certain-outcome ordering, but generally changes the ordering of expected values.

Ask whether mixing each of two compared lotteries with the same third lottery, in the same proportions, should preserve the comparison. For example, if L is preferred to M, would the holder retain that preference between a half chance of L plus a half chance of H and a half chance of M plus a half chance of H? Challenge this premise with material cases, including a move from certainty to a chance of failure. Ask whether small changes in probabilities should permit small changes in the comparison, or whether a strict priority or threshold must prevail. These questions make the representation's commitments discussable; finitely many answers cannot validate it for every lottery. If a common-mixture reversal, a noncompensatory rule or a material dependence on how the uncertainty is presented defeats the proposed form, retain the expressed comparisons and use a representation that preserves the feature, or identify the remaining representation gap. A probability-weighting or other non-expected-utility model needs its own construction; changing utility numbers alone cannot repair every failed form.

**Build one joint family.** When constructing a finite utility family from judgements, enumerate the complete consequence profiles appearing in the alternatives and elicitation questions. Obtain two intelligible reference consequences, w and b, that the holder treats as worst and best over this set and strictly distinguishes. Normalize `u(w) = 0` and `u(b) = 1`; require `0 <= u(x) <= 1` for the other represented profiles. This chooses an origin and unit, not the utility of an intermediate consequence. If common anchors lack support, retain the direct comparisons or use a different justified representation. If every consequence is indifferent, return that simpler relation.

Where a utility is still to be established, compare receiving x for certain with a lottery giving b with probability p and w otherwise. Stated indifference gives `u(x) = p`. If x is no worse than the lottery at p, add `u(x) >= p`; if the lottery at q is no worse than x, add `u(x) <= q`. Thus the holder can bound a comparison without identifying one exact probability of indifference. The probabilities in these questions describe the hypothetical lottery. They are not estimates of the real intervention's chance of success.

Retain all answers on the same utility variables. A comparison of two finite lotteries L and M adds `sum_x L(x) u(x) >= sum_x M(x) u(x)` when L is no worse, equality for indifference, or a strict inequality for strict preference. A comparison left open adds no equality. Certain-outcome comparisons are the special case with probability one on one consequence. These are linear constraints in the unknown utilities; use the feasibility and strictness treatment in §4.5.3 and the conflicting-subset diagnosis in §4.5.4. An inconsistent family calls for correcting the question or its interpretation, revisiting a judgement with its holder, or changing the form. It does not justify silently dropping a judgement.

This construction assigns utilities to complete profiles and requires no additive decomposition across their attributes. An additive multiattribute utility can reduce elicitation effort when its additional assumptions fit; the deterministic value model in §4.5.3 alone does not establish those assumptions for lotteries. Keep different holders' families separate unless the receiving work supplies a justified collective rule.

**Connect preference to the consequence model.** For each alternative a, obtain the distribution `P_a(x)` over these same profiles from the subject's probability model. Preserve shared causes, decision-dependent outcomes and the evidence limits described in PSDA.7 and PSDA.8. With one probability model and one utility function, compute `EU(a) = sum_x P_a(x) u(x)`. Comparing expected utility is generally different from applying utility to an average physical consequence.

When probabilities or utilities remain imprecise, retain the set K of compatible complete accounts `(P,u)`. Here P supplies a distribution for every alternative, and u is one utility function used across them. Use all combinations of the probability and utility families only when no joint restriction excludes them. If the meaning of a consequence, a model parameter or an elicited judgement links the two families, carry that restriction in K. Do not mix one alternative's favorable model with another's unfavorable model.

For each pair a and b, compare `D(P,u) = EU(a) - EU(b)` over K. Alternative a is necessarily no worse when every compatible account gives `D >= 0`; it is possibly no worse when at least one does. A contrary account defeats necessity; a feasible witness establishes possibility. The common-witness rule for possible best in §4.5.4 still applies. If K is empty, repair the failed basis before drawing a preference conclusion. No probability distribution over K follows from having retained it.

For fixed probabilities, D is linear in the utilities, so the finite constraint method can find a bound or witness. If both probabilities and utilities vary, their products generally make the problem bilinear; separate interval bounds or one linear-programming call are not automatically an exact solution. Use direct algebra, a complete finite enumeration or an appropriate bounding method under MMP.10 and MATH.20. Report the domain over which the computation establishes the bound. With strict constraints, distinguish an attained witness from an unattained limiting value.

Return the supported preference, conditional alternatives or unresolved comparison, with the consequence meanings, preference evidence or stated assumptions and chosen form. A changed probability estimate revises the assessed distribution of consequences. A new or corrected lottery judgement affects the utility family. Recompute affected relations. If an open preference matters to the requested finding or its use, seek an attributable judgement when warranted or retain the conditional answer. More precise factual measurements can leave the value question open.

#### PSDA.6:4.6 - Return the account and its exact incompleteness

Give the attributed concerns, consequence meanings and measures, applicable protections, preference rules and their grounds. Include any material interaction, dissent, unsupported transformation or condition that would change the result. If the merits of a requirement were at issue, include §4.4’s appraisal and the limit imposed by its current force.

For a numerical construction, include the chosen form and its assumptions, the profiles and judgements constraining it, the joint compatible family or identified conflict, and the scope of any necessary or possible preference. `PSDA.8` may use it only for the named comparison. The account can support a partial order or leave a comparison unresolved. Missing preference information is not automatically missing empirical evidence: a further experiment may estimate consequences without deciding how they should be valued.

A material ambiguity, repeated consequence or unexplained trade-off can identify the need for this work. For consequential reliance, qualify the measurements, elicitation or other value grounds the comparison uses. Justify any aggregation, establish the governing force of binding conditions and apply the relevant domain assurance.

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

The analyst removes a second “reliability benefit” entry that merely repeats the same pumping-service hours. Reachable assistance stays separate even if failures often occur in the same storms.

If the board adopts a trade-off between operating-service hours and budget units for a narrow analytical slice, the account names that value judgement, range, and limit. It does not present the slice as the residents' common value function. If the association and the other group reject a common trade-off, the return carries separate accounts and a stated disagreement; another hydraulic simulation cannot resolve that disagreement.

#### PSDA.6:5.2 - Development directions do not share a universal improvement score

For the ninety-day service-organization case, a qualified strategy result gives reliability priority over throughput for the current horizon. That premise helps frame the comparison but does not supply numerical weights or a causal effect estimate.

| Proposed holder-specific input | What the value account may use | What it must not infer |
| --- | --- | --- |
| Human capability result for representative later Work. | The supported performance distinction and the person's relevant protected conditions. | Course attendance, assessment performance, retention, and transfer are not one interchangeable development value. |
| Organization result for positions, interfaces, and continuing service. | Contribution and service consequences for the named arrangement. | A local team's gain is not automatically a gain for the organization or another team. |
| AI/model evaluation for a named version and environment. | The qualified performance, resource, oversight, and failure distinctions. | A benchmark percentage is not a person's capability measure or the whole service's reliability. |

The adviser keeps those premises in their own meanings. A common service-level comparison is possible only after qualified domain results connect each direction to that same service and horizon. Without that connection, “human 4, organization 4, AI 4” is not a meaningful equal score. Identify the missing link to the service consequence. Seek evidence for that link if its attainable contribution to the intended comparison warrants the cost. Otherwise return the supported account and its limit.

#### PSDA.6:5.3 - Cheap non-use

Two qualified replacement parts have the same relevant consequences except for a directly comparable resource cost, and the authorized recipient's cost preference is already explicit. Reuse that account. An objectives hierarchy and a fresh weighting workshop would add no value distinction.

#### PSDA.6:5.4 - Retain a protective restriction or revise a redundant control

These constructed variants concern a service team's proposed use of an external inference provider. In the first, a qualified configuration result shows that the proposed route exposes identifiable confidential incident records to provider staff who have no part in serving those clients. An available internal route meets the current service need within its support budget. The restriction prevents that disclosure; relaxing it for the faster external route would expose those clients without a corresponding needed service gain. The value account therefore supports retaining the restriction and excludes this external route for the current use. It does not infer that all provider configurations are unsuitable.

In the second variant, the configuration and access protection remain adequate. The disputed rule additionally requires three hours of manual transcription of an access log. Assume the competent review has established that the retained, inspectable electronic log covers the same events and that transcription adds no omitted event or distinct check. The same three hours would otherwise test a newly exposed, unreviewed access path to the same protected records. On these facts, retaining the extra transcription displaces more protective work without an identified protective gain. Recommend revising that requirement to use the qualified electronic record while keeping the actual access controls. If a missing event or an independent check is found, that premise changes the recommendation.

The rule owner cannot amend the transcription requirement before this decision. The recommendation is complete. The current rule still applies to the options under consideration, and an option that cannot satisfy it must wait. The lost testing opportunity remains a consequence of the present constraint. The contrasted results follow from the stipulated contribution and burden.

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

Later the same manager states that C is no worse than A. Its new row is `45 + 3r <= 60 + 2r`, hence `r <= 15`. Intersecting gives `[10,15]`. Now `L_A-L_C` lies in `[0,5]` and `L_B-L_C` in `[5,15]`: C is no worse than A and strictly better than B for every compatible exchange. C is a necessary best, while `{A,C}` remains the set of possible best alternatives because A ties at 15. Return C as a supported direction with that tie intact. The new judgement changed the value family and its comparison; it changed neither the consequences nor D's access failure. The decision holder can use this recommendation within the stated comparison.

#### PSDA.6:5.6 - A failed affine form is not automatically contradictory judgement

Consider a different continuation from the original `[10,20]` family. The manager additionally says that `(20,5)` is no worse than `(44,2)`. In the affine form this yields `20 + 5r <= 44 + 2r`, or `r <= 8`. That row and the first original row `r >= 10` cannot hold together. Return this specific conflict; the former comparison no longer has a compatible affine basis.

Ask whether the equal-increment assumption still expresses the manager's values. They may care much more about reducing two hours to one than about reducing five hours to two. For example, a curved time-loss contribution taking values `0,20,28,36,44` at times `1,2,3,4,5`, with loss `c + h(t)`, satisfies all three profile comparisons: `60 <= 64`, `56 <= 80` and `64 <= 64`. This constructed witness proves only that those three judgements need not contradict one another. It is not an elicited curve and supplies no recommendation by itself.

If the manager withdraws constant time increments but retains addition, §4.5.3 constructs the whole compatible monotone family at the relevant levels. If the manager instead states the noncompensatory two-hour rule in §4.5.1, that different value account prefers A to B and C directly. Either change needs its stated basis; neither is a convenient parameter adjustment inside the old affine model. If no clarification is available, retain the attributed comparisons, D's independently established exclusion and the exact failed form. Return the numerical ranking as unresolved.

#### PSDA.6:5.7 - Separate an uncertain result from its value

A team compares two ways to obtain optional machine time in a ten-hour window. Existing provision covers required service; this comparison concerns additional usable hours, with other material consequences held equal. S supplies four hours for certain. R supplies ten hours if a trial succeeds and zero otherwise. The team prefers more usable hours, but that ordering does not yet compare S with R.

For a success probability of one half, utility `u(x) = x/10` gives `EU(S) = 0.4` and `EU(R) = 0.5`; R is preferred. Utility `u(x) = sqrt(x/10)` preserves the same ordering of certain hours but gives `EU(S) = sqrt(0.4)`, approximately 0.632, and `EU(R) = 0.5`; S is preferred. These two constructed functions show why the certain-outcome ordering is insufficient. Neither is an elicited preference.

The team accepts the expected-utility form for this bounded comparison and uses zero and ten hours as its reference consequences. Let `q = u(4)`, with `u(0) = 0` and `u(10) = 1`. Asked about hypothetical chances, the team says that four certain hours are no worse than a 40 percent chance of ten hours, but a 70 percent chance of ten hours is no worse than four certain hours. Each lottery otherwise gives zero hours. These answers yield `0.4 <= q <= 0.7`; they supply no point estimate.

Separately, engineering evidence bounds R's success probability by `0.45 <= p <= 0.55`. In this constructed case the probability estimate and preference restrictions impose no additional joint constraint. Thus `EU(R) - EU(S) = p - q` ranges from `-0.25` to `0.15`. Neither alternative is necessarily no worse. The accounts `(p,q) = (0.55,0.4)` and `(0.45,0.7)` witness opposite preferences. The two accounts leave the ranking open. Greater precision about success can still leave the team’s valuation unresolved.

The team can answer one further preference question: four certain hours are no worse than a 60 percent chance of ten hours, otherwise zero. Intersecting that answer with the previous family gives `0.6 <= q <= 0.7`. The difference now ranges from `-0.25` to `-0.05`, so S is strictly preferred throughout the joint family. No midpoint utility or invented probability over utility functions was needed.

A changed engineering result can reverse that conclusion without changing the preference account. If a genuinely different trial design raises the supported success range to `0.8 <= p <= 0.9`, while the consequence meanings and other consequences stay the same, the difference ranges from `0.1` to `0.3`: R is now strictly preferred. If the redesign also changes cost, timing or the meaning of usable hours, those omitted consequences must first enter the profiles; the old one-attribute calculation would no longer answer the whole comparison.

The construction concerns one attributed preference account. It neither aggregates conflicting team members' views nor establishes that the trial has the assumed success probability. Those are separate inputs whose absence would leave a different question open.

### PSDA.6:6 - Bias-Annotation

**Scope:** value representation for one bounded comparison. **Lenses:** **Onto/Epist** separates concern, measure, preference, and obligation; **Prag** preserves decision relevance; **Gov** exposes representation and authority; **Did** makes trade-offs concrete.

Template bias imports irrelevant criteria. Proxy bias rewards what is easy to count. Splitting one objective into many criteria can change its apparent importance. Sponsor averaging can conceal who bears a loss. Counter these by returning to attributed consequences, inspecting overlaps, and retaining disagreement and missingness.

### PSDA.6:7 - Conformance Checklist

- [ ] Values are attributed to the relevant subjects and receiving comparison, with representation limits intact.
- [ ] Objectives and means are distinguishable at the level needed for the comparison.
- [ ] Repeated consequences are not counted twice; correlation alone does not justify deletion.
- [ ] Measures retain subject, scale, unit, horizon, evidence, proxy limits, and missingness.
- [ ] Binding conditions, aspirations and unresolved authority questions are distinguished. Where the merits of a requirement were in question, the appraisal identifies protection, burden, the supported conclusion and the requirement’s current force.
- [ ] Value transformations and weights have declared ranges and identifiable grounds, such as attributable preferences, an applicable rule or stated analytical assumptions. The grounds for the chosen form are separate from the fitted parameters.
- [ ] The numerical family preserves the joint judgements, has a checked feasibility result, and distinguishes incomplete information from contradictory judgements or a failed form.
- [ ] Necessary and possible comparisons retain their quantifiers, ties and dependence on the same compatible model. A changed judgement reopens only dependent results unless it changes the form itself.
- [ ] For finite expected utility, the lottery judgements or stipulated assumptions and the representation support the utility account. The probabilities describe the consequences. Compare alternatives under the same compatible account and preserve open preferences.
- [ ] Interactions and refusals to compensate are preserved.
- [ ] Any collective aggregation has an explicit basis; incompatible accounts remain visible otherwise.
- [ ] The return identifies any unresolved comparisons, dissent, missing source grounds and conditions affecting future use.
- [ ] A supported preference comparison covers only its attributed account and supplied consequences; authorization of the later choice and a claim of effect need their own grounds.

### PSDA.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Everyone agrees safety is important, so give it twenty percent.” | Identify the condition, its source, and whether compensation is permitted. |
| “Equal weights are neutral.” | State the consequence ranges and inspect how criterion splitting changes the result. |
| “These two measures correlate, so one is redundant.” | Examine whether they represent the same valued consequence. |
| “Normalize everything to zero–one.” | Establish value meaning and admissible operations before any transformation. |
| “The workshop mean is the public preference.” | Preserve attribution and require an explicit aggregation basis. |
| “Collect more data to resolve the value dispute.” | Identify whether the missing input is evidence, preference, representation, or authority. |

### PSDA.6:9 - Consequences

The comparison shows which consequences are valued, by whom and which trade-offs are permissible. A simpler account may preserve the same distinctions at lower cost. Where the evidence supports only a partial order or separate disputed accounts, return those results.

### PSDA.6:10 - Rationale

Value representation makes consequences decision-relevant without confusing description with preference or preference with permission. Concrete trade-off questions expose assumptions hidden by criterion labels. Preserving multiple admissible accounts lets later comparison show where a conclusion is shared and where it depends on a disputed judgement.

### PSDA.6:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How can objectives be concise without omitting what matters? | Inspect means–ends structure, relevance, overlaps, and sensitivity to simplification. | Retain an exhaustive descriptive hierarchy, or delete criteria by correlation alone. | **Adapt:** :4.2–:4.3 keep a small consequence-led account and test any lost distinction. More analyst attention is accepted where it prevents double counting; small clear cases remain short. | Marttunen et al.'s [2019 objectives-hierarchy study](https://doi.org/10.1016/j.ejor.2019.02.039) supplies the comparative methods and retrospective environmental cases. It supports disciplined simplification, not one optimal hierarchy or a statistical license to discard values. | Reopen when a removed distinction can reverse the comparison or a lighter structure preserves the same concerns. |
| Must incomplete preferences become one weighted score? | Construct the preference model from consequence comparisons and use all compatible instances. | Fit one additive score, average weights, or retain a noncompensatory rule when that better expresses the judgement. | **Adapt:** :4.5.1–:4.5.5 develop form selection, joint constraints, feasibility, necessary/possible comparison and local revision; :5.5–:5.6 show a complete use and failure of the affine form. The trade-off is a potentially less decisive answer for less invented precision. | Greco, Słowiński and Wallenius's [2025 MCDA review](https://doi.org/10.1016/j.ejor.2024.07.038), especially §3.1.2 and §7.1 ([accessible author-hosted PDF](https://www.iris.unict.it/retrieve/cb6fc63a-f16d-4c14-a163-46b863c27dc9/1-s2.0-S0377221724005988-main.pdf)), supplies preference assessment and robust ordinal regression. Its rules and non-additive families remain serious alternatives. The two-criterion derivation and service cases here are bounded applications, not its empirical findings or a universal additive-representation theorem. | Reopen when new judgement changes the compatible set, an interaction defeats the form, or the holder, range or governing condition changes. |
| How can incomplete risk preferences become a usable comparison? | Elicit finite lottery comparisons, construct the compatible utility family and compare expected utilities over compatible probability and utility accounts. | Assume risk neutrality from a certain-outcome score, fit one curve despite open judgements, or retain a different explicit preference rule. | **Adapt:** :4.5.6 supplies the general construction and :5.7 shows elicitation, an open result and a changed comparison. Further elicitation or computation is warranted when its attainable contribution to the requested preference finding or its use justifies the burden. | [Sahlin, Troffaes and Edsman (2021), §§3.3–3.5 and Appendix B](https://arxiv.org/html/2103.04721v1) demonstrate imprecise lottery-based elicitation with imprecise consequence probabilities. Their additive environmental model is not assumed here. [McCarthy, Mikkola and Thomas (2021)](https://arxiv.org/abs/2102.06898) develop the representation question for incomplete mixture preferences; retaining a family does not remove independence and continuity premises. [Breig and Feldman (2026, online 2025)](https://doi.org/10.1007/s11238-025-10089-1) test expected-utility consistency in a specific elicitation design, supporting scrutiny of the form rather than universal use. The finite profile construction and machine-time calculation here are explicit adaptations, not empirical findings from those studies. | Reopen when lottery judgements conflict with the form, a consequence is omitted, the probability model or holder changes, or an unresolved joint restriction changes the comparison. |
| Can common coordinates perform the value judgement? | Declare meanings and scales separately from preference, comparison, and selection. | Treat a dashboard or normalized vector as the decision model. | **Adopt:** :4.3 uses A.19 only for the declared space or predicate and leaves value elicitation here. The declared coordinates allow a reader to interpret the table. Scoring or combining the values requires a rule for that comparison. | Current `A.19`, `C.16`, and the direct comparison patterns supply the relevant typing and operation boundaries. They do not elicit the engagement's values or authorize a trade-off. | Reopen when the scale, predicate, consequence range, or receiving use changes. |

### PSDA.6:12 - Relations

- `PSDA.12` may supply attributable concerns and participation conditions for the value question. Establish numerical weights or a mandate to aggregate from the evidence or rule that provides them.
- `PSDA.8` may use the value account for the named comparison. `PSDA.9` can test its dependence on the compatible family, and `PSDA.14` can use a supported direction, conditional set or gap.
- `MMP.10` and `MMP.11` supply general constraint and model-family construction after the value meanings and form conditions in §4.5 are established. `MATH.20` supplies bounds over the admitted domain; none of these suppliers elicits the holder's preferences.
- `C.16` governs measurements; `A.19` supplies a declared characteristic space or predicate when needed. Scoring, aggregation, comparison, and selection remain separate direct operations.
- Direct ethics, law, safety, governance, finance, and holder practices supply the particular conditions and claims they own. `A.15.9` helps obtain a missing qualified contribution without transferring that authority.
- For a missing, stale or incompatible premise, use an applicable direct result or state the specific limit on the value account.

### PSDA.6:End

## PSDA.7 - Represent Decision-Relevant Uncertainty and Evidence Limits

> **Type:** Method pattern body
> **Status:** Stable
>
> **Primary working result:** a bounded account of the claim, consequences or eligibility the receiving inquiry asks about, the uncertainty that matters to it and any remaining question that could distinguish the possibilities.

### PSDA.7:1 - Problem frame

**Use this when** a point estimate, “high confidence” label, or model output makes a decision look more settled than its evidence permits. Also use it when a long uncertainty list does not say which unknown could reverse, narrow, defer, or invalidate the decision-support return.

Take a claim on which the inquiry relies. Vary its premise within the supported limits. Identify what changes in the consequence, eligibility, ordering or grounds for the conclusion. Report the result and any question the evidence leaves open.

Distinguish an uncertain consequence, an attributed belief, a model assumption, missing evidence and a disputed value. Identify the form and grounds appropriate to each. A common decision question need not give them a common scale.

If the question concerns only a source’s provenance or currentness, use `A.10` or the relevant source practice directly. Use an existing adequate uncertainty account within its scope. Measurement, forecasting, causal attribution and safety each need evidence appropriate to the particular claim.

### PSDA.7:2 - Problem

A numerical estimate can hide the conditions under which it is meaningful. An access model may estimate arrival time only when the road is open; a training study may concern an immediate test rather than later Work; an AI evaluation may concern a previous version or operating distribution. Averaging the results does not repair their missing applicability.

Conversely, a demand for certainty can stop every useful return. Some uncertainty cannot change the ordering, while another can show that all alternatives fail a protected condition. A useful account distinguishes those cases. It also separates a question that better evidence can answer from a disagreement about values or authority that evidence alone cannot settle.

### PSDA.7:3 - Forces

| Force | Tension |
| --- | --- |
| Qualification and action | A decision needs bounded support, not complete knowledge, while an unsupported premise can make action indefensible. |
| Probability and ignorance | Probabilities can represent uncertainty well when justified, while invented distributions hide model disagreement or lack of knowledge. |
| Reduction and relevance | A narrower estimate may strengthen a conclusion or answer a factual question even when the available action stays the same. Further precision can also leave the intended use unchanged. |
| Shared evidence and corroboration | Several sources can provide distinct support or merely repeat the same data and assumptions. |
| Stable comparison and changing conditions | Alternatives need a compatible basis, while source, holder, and environment changes can invalidate that basis. |

### PSDA.7:4 - Solution

Connect each material uncertainty to the claim or decision it can affect. Represent it on the available grounds, preserve dependencies and limits, and return the supported claim, a conditional answer or the specific question still open.

#### PSDA.7:4.1 - Identify the claim and the comparison at issue

Identify the subject, configuration, horizon, receiving question, any relevant alternatives and the claim at issue. Ask which premises affect its consequences, eligibility, relative standing or the strength of its grounds. If an alternative required for the question is unclear, identify the missing candidate information.

Use a `PSDA.3` model account where its evidence or assumptions bear on the configuration and horizon. A model can identify an uncertainty that it cannot resolve. A qualified direct source may already provide the missing premise.

Check absolute consequences where a requirement depends on them. A common uncertainty can leave the ranking fixed while revealing that none of the alternatives meets a required service or safety condition.

#### PSDA.7:4.2 - Represent the kind of uncertainty

Choose a form that answers the live question without claiming more knowledge than exists.

| Available basis | Useful representation | Limit that must remain visible |
| --- | --- | --- |
| Qualified stochastic model or elicited probabilistic judgement. | A distribution or probability statement tied to its event, population, conditions, and horizon. | Calibration, sampling, elicitation, model assumptions, and applicability still matter. Confidence in the analyst is not the event probability. |
| Supported bounds with no distribution. | An interval or set of admissible values. | Give the grounds for the bounds. Values outside the interval may be excluded, while a distribution within it or joint attainability with other quantities needs additional evidence. |
| Several materially different models or future conditions. | Conditional claims under named models or scenarios. | Their count or frequency in an ensemble does not supply real-world likelihood. |
| A decisive absent result or unrepresented mechanism. | The exact missing claim and the comparison it prevents. | A blank cell is neither zero effect nor equal performance. |
| Incompatible interpretations, preferences, or authority claims. | Attributed alternatives and the unresolved interpretation or judgement. | Statistical uncertainty reduction alone cannot reconcile them. |

Several forms may be useful in one account. Distinguish variation in a physical or behavioural process from uncertainty about a model, data or applicability where that difference matters to the finding.

Report what holds under each supported condition when its probability is unknown. If a calculation requires a probability distribution, identify the missing basis or calculate conditionally on explicitly stipulated probabilities. Equal scenario weights can serve a sensitivity calculation. Using them for an expected real-world result requires evidence for that distribution.

#### PSDA.7:4.3 - Qualify the relied-on claims

For a relied-on source result, identify its claim, subject, kind of result, edition or effective window, assumptions, evidence and relevant limits, including any dissent. Use `A.10` when the connection between source and use is unclear or the use requires a reproducible account of that connection and one is missing. Establish the subject claim and authority for any decision on their respective grounds.

Check that the evidence covers the relevant holder, intervention, environment and horizon. Distinguish observations, forecasts, expert judgements and extrapolations. To attribute an observed benefit to the intervention, use evidence that connects them.

Use a qualified result within its limits. If a material premise remains missing, identify the particular claim, bound, interpretation or test it would affect. Use `A.15.9` where an outside contribution is needed and worth obtaining, or return the limit.

#### PSDA.7:4.4 - Preserve dependency and model disagreement

Trace shared data, common causes, assumptions and dependencies where they affect the comparison. Treat repeated use of one dataset as a shared source. To combine independent or dependent judgements, state the aggregation Method, its assumptions and their fit.

Keep incompatible assumptions separate until a direct result supports their combination. For example, a scenario with a failed access route and a scenario with a functioning route can test different claims; combining their most favorable outcomes produces no realizable case.

For disagreeing models, locate the overlapping claim and examine scope, input, representation, mechanism and evidence. Explain a mismatch where its source is established, or retain the distinct supported assumptions or models. A discriminating measurement can be worth obtaining when it would improve the intended result.

#### PSDA.7:4.5 - Form a discriminating question

Formulate an unanswered question where a different supported answer could matter to the current return. For example, a threshold question may take this form.

> For this subject and horizon, establish whether this premise lies inside the region supporting alternative A, outside it, or remains unresolved; state the evidence and limits needed for that use.

The requested result may concern eligibility rather than ranking. It may also show that no available alternative works, that a different formulation is needed, or that only a reversible analytical use is supported.

Identify an observation, calculation, interpretation or comparison that could answer the question, if one is available. Identify who can supply it and the time or access it needs where relevant. If no feasible inquiry can answer within the window, state the remaining limit.

Use `PSDA.9` for reversals and information priorities where that work is needed. For a choice about a probe, compare its attainable contribution and full burden. The authorized decision holder can use `C.11` to choose a feasible next step.

#### PSDA.7:4.6 - Return the strongest supported claim and no stronger

A short return states:

- what claim the evidence supports, for which subject, configuration and horizon, including any alternatives it compares;
- its uncertainty representation, source limits, and dependencies;
- what different answer could change the comparison, admissibility, or receiving use;
- any specific question or obstacle that remains; and
- any change in source, observation, candidate, value or configuration that would affect its intended use.

Return “unchanged within the tested bounds” only when those bounds cannot alter the stated result. Return a conditional or narrowed claim when support covers only part of the use. If a required protected-condition premise is unsupported, preserve the direct domain stop rather than compensating with confidence elsewhere.

An unexplained estimate can reveal the need for this work. For consequential reliance, use the evidence and assurance the relevant domain requires, including independent checks where applicable.

When the basis of a claim changes, revalidate the uses that depend on it. Use `G.11` for currentness and `A.10.1` when affected uses need discovery or a connected return. A known single dependency can be checked directly through `A.10`. Preserve independent claims whose basis still holds.

### PSDA.7:5 - Archetypal Grounding

#### PSDA.7:5.1 - Which flood-pump uncertainty matters now?

In the illustrative pre-season inquiry, nominal permanent and mobile capacity meets the assumed inflow only with the stated units operating. The model omits arrival delay. The team cannot turn that conditional result into “mobile service is reliable”.

| Relied-on or proposed claim | Evidence limit | Decision-linked return |
| --- | --- | --- |
| Nominal mobile capacity is adequate. | The capacity calculation assumes operating units on site. | Use for capacity only. It does not discriminate the missing deployment arrangement. |
| Mobile units can serve the district after road loss. | No qualified arrival and deployment result exists for that condition. | Keep M conditional for service. A qualified route-loss deployment result could close the gap. Seek it if the intended use warrants the effort. |
| The two technical models corroborate the inflow assumption. | Both use the same inflow dataset. | Record the shared evidence dependency. Independent corroboration would require a separate basis. |
| Pumping-service hours represent all affected residents' loss. | Reachable assistance and property protection have different meanings. | Return the missing consequence relation or keep separate accounts; a tighter inflow estimate will not settle the value question. |

A later qualified deployment result can narrow the arrival range and change the claims that depend on it. If the range includes conditions where service fails, identify the condition for robustness rather than asserting unconditional feasibility. A common power-supply uncertainty can leave all arrangements unqualified even where their relative order is fixed. Evidence of a common failure can establish that they all fail.

#### PSDA.7:5.2 - Development evidence with three different limits

For a ninety-day organization recommendation, suppose the adviser has an immediate human assessment, a queue model for the current team, and an offline AI benchmark. Each can inform a different bounded claim.

The human assessment does not establish retention or transfer to later service Work. The queue model does not establish the performance of a reallocated or mixed arrangement without its staffing and interaction premises. The benchmark does not establish current-version service reliability under the operating distribution and oversight arrangement.

Identify the separate questions about representative later work, service in the changed staffing arrangement and the version used under operating conditions. Seek a missing result if its attainable contribution to the recommendation or its grounds warrants the burden. Keep the three evidence limits separate.

#### PSDA.7:5.3 - A bounded input to SensorCo's strategic commitment

SensorCo's illustrative twelve-month question concerns defending devices, offering an integrated service, licensing data, or exiting a segment as generic AI inspection prices fall. The strategy team owns the strategic comparison; the board separately holds commitment authority.

Suppose the integrated-service direction depends on uncertain repeat demand and the licence depends on an unsettled permission question. State the demand conditions that could change the service comparison and identify the missing rights interpretation for licensing. Obtain the corresponding evidence or ruling when the intended use needs it.

`STR.11` can use this uncertainty result for the specified commitment and compatible horizon. Recheck affected uses if the alternative, claim, demand question, evidence window or commitment changes. For an unavailable or incompatible result, use a qualified direct source or report the remaining gap.

#### PSDA.7:5.4 - Cheap non-use

An analyst needs to recover which calibration edition a measurement cites, and no candidate comparison is being made. Use the source and evidence practice directly. A decision-linked uncertainty account would add no current result.

### PSDA.7:6 - Bias-Annotation

**Scope:** uncertainties that can change a bounded decision-support return. **Lenses:** **Epist** separates evidence and belief; **Prag** tests action-changing relevance; **Arch** exposes dependencies; **Gov** preserves direct authority and protected conditions; **Did** makes an unknown into a useful question.

Precision bias favors a number over an honest set or gap. Confidence rhetoric can substitute reputation for evidence. Model averaging can conceal shared errors. Certainty seeking can consume the entire decision window. Counter these with exact conditional claims and an explicit account of what a different answer would change.

### PSDA.7:7 - Conformance Checklist

- [ ] Each material uncertainty is linked to the claim, configuration, horizon and intended use, including the affected alternatives where relevant.
- [ ] The account examines eligibility, shared failure or a ranking change where it affects the claim in question.
- [ ] Probabilities, intervals, scenarios, missing results, and disputes retain their different meanings.
- [ ] Every probability or bound has an adequate basis; scenario counts are not probabilities by default.
- [ ] Source, holder, intervention, and environment limits accompany relied-on evidence.
- [ ] Shared evidence, common causes, and incompatible model assumptions remain visible.
- [ ] A proposed inquiry identifies the result it could supply and its attainable conditions. If no inquiry is feasible in time, the account gives the outstanding limit.
- [ ] The result states the conclusion within its evidential scope or the condition that prevents a conclusion.
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
| Replace missing holder evidence with another holder’s success. | Use evidence of transfer or applicability to the receiving holder. Seek a missing qualified result when warranted, or give the limit. |

### PSDA.7:9 - Consequences

The recipient can see what the evidence supports and which issues remain consequential. A bound or set may convey less numerical precision than a single estimate while identifying what the evidence leaves open. Refine it when the attainable gain for the receiving task warrants the effort.

### PSDA.7:10 - Rationale

Uncertainty matters through its effect on a decision claim, not through its size alone. Preserving the source, representation, and dependency of each premise makes that effect inspectable. A bounded unknown can support useful inquiry without pretending to supply the missing fact or the eventual choice.

### PSDA.7:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| When should uncertainty be probabilistic, and when should alternatives remain conditional? | Use qualified probabilistic analysis where its premises hold; retain multiple plausible conditions when decision-relevant probabilities or models are unsettled. | Predict-then-act under one agreed forecast, or reject all probabilistic reasoning whenever uncertainty is difficult. | **Adapt:** :4.1–:4.4 select a representation from its evidence and test consequential shared failure. Compare further scenarios when a single forecast could conceal a consequential difference in eligibility, exposure or the conclusion requested. | Lempert et al.'s [2024 DMDU/IPCC analysis](https://doi.org/10.3389/fclim.2024.1380054) is the synthesis candidate for decision relevance despite low-confidence knowledge. It does not make scenarios equiprobable or provide a universal uncertainty taxonomy or local risk threshold. | Reopen when a qualified distribution becomes available, model disagreement changes, or an omitted future defeats the claimed bounds. |
| Which missing evidence deserves a question? | Connect elicitation, sensitivity, and information acquisition to the alternatives and consequences they can change. | Rank unknowns by variance or confidence alone. | **Adapt:** :4.5–:4.6 require a discriminating question before further inquiry. The practical trade-off is less general data collection for a more explicit decision boundary. | Borgonovo et al.'s [2026 review](https://doi.org/10.1016/j.ejor.2025.05.023) supplies the current decision-analysis connection among uncertainty, sensitivity, and information value. It is a synthesis, not validation of PSDA's particular evidence or a universal probe rule. `A.10` supplies only bounded reliance; the authorized holder can use `C.11` for a local choice about a probe. | Reopen if another unknown can change eligibility, a model revision changes the discriminator, or no feasible inquiry fits the decision window. |

### PSDA.7:12 - Relations

- `PSDA.3` may supply model evidence and assumptions for the same configuration and horizon. Representation alone establishes neither the subject condition nor this uncertainty judgement.
- `PSDA.8` may use the bounded claims and questions where they change its consequence comparison. Evidence neither entails that result nor authorizes the later decision.
- `STR.11` may use a supplied decision-linked uncertainty result where it informs the strategic commitment comparison or its grounds. The result carries its own scope and horizon; it imports neither the whole PSDA practice nor strategic facts or authority.
- `A.10` addresses reliance on a claim, and `A.15.9` the use of an outside contribution. `G.11` addresses the currentness of a maintained result. Use `A.10.1` where affected uses need discovery or a connected return.
- `PSDA.9` addresses robustness and information priorities. Use `C.11` where the authorized holder needs to choose a probe or another action. Use a qualified source for a missing or incompatible premise, or state the particular gap.

### PSDA.7:End

## PSDA.8 - Compare Consequences of Decision Alternatives

> **Type:** Method pattern body
> **Status:** Stable
>
> **Primary working result:** an **inspectable consequence comparison** for exact alternatives, affected subjects, conditions, horizon, value accounts, and evidence, including the relations that hold and those that remain unresolved.

### PSDA.8:1 - Problem frame

**Use this when** you need to establish what the alternatives would change, for whom, over what period and under which assumptions. A reported rank can leave those conditions unclear. A component score can also omit service, transition, interaction or protected-condition consequences of the whole arrangement.

Start with a material consequence and trace it for one alternative from the proposed change through the mechanism and conditions supported by the evidence. Identify who or what bears it. Compare the same consequence for the other alternatives within the scope the task requires.

Distinguish a forecast, a conditional model result, an observation and an untested hypothesis. The comparison identifies the relations those inputs support. A decision and a later outcome have different grounds.

Use an existing qualified comparison where it covers the alternatives and receiving use. A single missing calculation or effect estimate can be obtained through the relevant domain Method. For a remaining choice over adequate options, the decision holder can use `C.11` or other applicable guidance.

### PSDA.8:2 - Problem

A rank can hide an incomplete causal story. A larger pump does not by itself establish delivered flood service. A better-trained worker does not by itself remove a queue constrained by interfaces. A stronger model benchmark does not establish reliability of the deployed service arrangement.

Even accurate separate estimates can form a false comparison. Alternatives may use different baselines, populations, operating assumptions, or horizons. Shared benefits can be counted twice, losses shifted to excluded people, and an average used to hide a tail or distributional difference. Compare consequence accounts on compatible bases and retain material differences in population, risk and who bears a loss.

### PSDA.8:3 - Forces

| Force | Tension |
| --- | --- |
| Common basis and real difference | Alternatives need comparable questions, while their mechanisms and affected subjects can genuinely differ. |
| Detail and affordability | Transition, distribution, and dependencies may reverse a conclusion, while exhaustive modeling can miss the decision window. |
| Multiple values and synthesis | A recipient needs a usable comparison without losing protected conditions or incompatible value accounts. |
| Prediction and evidence | A conditional model can inform a future choice without becoming an observed or causal result. |
| Precision and partiality | Numerical relations can clarify a comparison, while absent or incompatible evidence may leave no defensible total order. |

### PSDA.8:4 - Solution

Develop consequence claims for the same receiving question. Align meanings that the evidence supports, apply the stated comparison rule and report the resulting relations. Preserve relevant uncertainty, value disagreement and limits on coverage.

#### PSDA.8:4.1 - Fix the comparison, not just its column names

Identify the question, subject or holder, configuration, horizon, affected subjects and alternatives. A compatible `PSDA.5` result can supply the candidate family. Keep a proposal conditional where a missing premise affects eligibility. Use the applicable criterion to determine which comparisons the evidence supports and which remain open.

Use the relevant subject criteria, common measures and binding conditions. When the question depends on values or trade-offs, use a compatible `PSDA.6` account or other qualified basis. Identify whose values it represents or which rule or assumptions supply them, and any trade-offs still open. Use compatible `PSDA.7` results for claims and uncertainty within their configuration, evidence window and horizon.

Use qualified direct sources where they supply these premises. If a necessary premise is missing, outdated or incompatible, name the affected claim and narrow or withhold it.

#### PSDA.8:4.2 - Establish consequence paths at the needed grain

For each material alternative, connect the proposed change to intermediate conditions and the consequences relevant to the question. Where a value account is used, show which consequences enter it. Identify who or what bears each consequence, when it appears, whether it persists, and which enabling conditions it needs.

Include transition burdens, delayed effects, and shifted losses when they can alter the comparison. Distinguish the present arrangement from an empty or ideal baseline. Use `C.11.CRC` when the missing input is specifically a finite change's contribution relative to the current configuration; reuse an already adequate contribution claim rather than reconstructing it.

Use applicable domain models or evidence for a mechanism or effect estimate. A diagram can represent a causal hypothesis. A before-and-after difference can establish an observed change. To attribute that change to an intervention, use evidence for the causal link. A qualitative pathway can identify a missing relation before its magnitude is known.

Do not extend a consequence beyond its qualified horizon without a stated model and source. If a short operating horizon excludes a material long-term lock-in or displaced loss, expose the exclusion and reopen the boundary where necessary.

##### PSDA.8:4.2.1 - Construct and question a qualitative consequence network

Use this branch to connect alternatives to consequences when a sufficient domain model is unavailable. It can supply conditional profiles and identify a missing transition. Use an existing qualified model directly if it answers the question. Timing, magnitude, feedback or joint risk may require a quantitative or dynamic model. Give a causal claim only with its subject-specific grounds.

1. **Recover the participants’ reasons.** Identify the desired state, proposed action, needed resources and criteria of the affected parties. Establish why a result matters to each party and how it could be obtained. Use attributable evidence about their reasons where it exists. Where the account is a modeler’s hypothesis, state it as such. Distinguish a required result from a prescribed task. Two ways can obtain a result while distributing work and discretion differently.
2. **Construct explicit relationships.** Write each important arrow as a sentence. For an external provision, identify who needs what, why, who could supply it and through which work. For a necessary combination, state which conditions must hold together; for alternative means, state whether either suffices and whether both may coexist. For a quality contribution, explain how an action or intermediate condition supports or impairs that quality. Keep necessity, sufficiency and a merely favorable contribution distinct. Name the conditions and evidence or attributed judgement supporting each sentence. Identify a plausible relationship as a hypothesis where its occurrence or strength remains open.
3. **Check the network before using it.** Trace each material consequence to the alternative and the affected party’s criterion. Use applicable records, direct observations or a qualified calculation to establish whether provision is possible. For a claim about what a party values, use their statement or other evidence that supports the attribution. Seek a provider’s commitment or a participant’s account when that contribution remains necessary. Locate missing steps, double counting and disagreement. Where a cycle matters, bound the time steps or use a model that represents feedback. A circulating label adds no evidence.
4. **Evaluate one complete alternative at a time.** Hold its configuration and initial assumptions fixed. Carry established or conditional results through necessary combinations and alternative means using their stated meanings. A necessary unfulfilled condition blocks the claimed conjunction; an unknown necessary condition leaves that conjunction unsupported unless another condition already defeats it. One sufficient supported route can establish the stated disjunction even when another route remains unknown. If no route is supported and at least one remains unknown, retain the unresolved result; if every modeled route fails, that modeled disjunction fails. Apply the same discipline to external provision: the receiver's result cannot be established through a provision whose availability is unknown. For contributions, retain the incoming supporting, opposing and unknown grounds together before judging the destination. Do not add signs, count arrows, or promote several weak claims to a strong claim merely because there are several. Distinguish no investigation, an investigated but unknown effect, and opposed grounds.
5. **Examine a disputed transition.** Compare the grounds and criterion to establish whether the conditions suffice, help, obstruct or leave the outcome unresolved. Use an applicable result or an attainable subject check. Seek the affected participant’s judgement for their concern or the qualified provider’s contribution where it is needed. Retain the scope of the answer, dissent and any unresolved conflict. If an unexpected result exposes a missing premise, revisit the relation or its evidence.
6. **Compare the resulting profiles.** Apply :4.3–:4.5 to the same consequences for all alternatives. Keep a supported trade-off separate from an unknown effect that could reverse it. Return the explanation paths with the profile; use a diagram if it helps the recipient reconstruct the explanation. Mark any judgement on which the comparison depends so that the recipient can challenge it.
7. **Work backward only when the question requires it.** If the recipient asks how several desired conditions could hold together, trace their necessary conditions and candidate sufficient routes backward. Propose a combination of means, ask what incoming conditions would justify each disputed intermediate judgement, then test the whole combination forward under the same assumptions. Set aside a combination with an incompatible condition. Keep a combination with an unsupported decisive transition conditional, naming the missing relationship instead of treating missing evidence as refutation. A failed current combination is not proof that every possible design fails. Do not weaken the recipient's criterion merely to find a solution.
8. **Revise by dependence.** When a source or judgement changes, identify the changed relationship, re-evaluate the consequences and alternatives that depend on it, and recheck the comparison. Reopen the boundary if an omitted party or consequence appears. Preserve independent claims and the earlier result with its earlier conditions.

Use terms appropriate to the subject. If the analysis relies on a formal language or solver, identify the relevant version, propagation rules, treatment of unresolved or conflicting evidence and structural limits. A satisfying assignment establishes a model result. Participant commitment and realized service need evidence from their respective domains.

For an inquiry that also needs to construct and question the underlying actors-and-goals model, [PSDA.20](#psda20---explore-a-situation-through-goals-and-dependencies) connects this branch to the inquiry's purpose, model views, explicit initial assumptions and a return from unexpected results to new source questions. Its car-park case follows a staffing conflict through a revised allocation and its limited use. The present branch supplies the consequence analysis within that larger inquiry.

#### PSDA.8:4.3 - Construct a consequence account before aggregating

Keep each relevant consequence profile visible. For values the comparison uses, identify the subject, meaning, unit or category, condition, time, source and any uncertainty or missing value. Use a brief parallel description or a table suited to the comparison.

Separate physical or service consequences from how they are valued. A budget estimate, hours of service loss, a probability distribution, and a consent condition do not become interchangeable because they occupy adjacent columns. A lower cost can be compared directly under its scale while a disputed value trade-off remains unresolved.

Where there is a distribution, preserve its event definition and dependence on the alternative and conditions. Expected values alone are insufficient when a tail, threshold, reversibility, or distribution across affected subjects can change the decision. If the evidence supports only scenarios or bounds, use those. A calculation under a stated hypothetical distribution remains conditional on that assumption.

Mark a missing value as unknown and identify the comparison it limits. Where a narrower account suffices, name the excluded material consequences.

#### PSDA.8:4.4 - Check dependencies and shared burdens

Check for shared causes, shared resources, overlapping accounts and interactions in a combination. For a human–tool arrangement, establish the consequence of the combined operation. Adding component effects can miss coordination costs or count one resolved case twice.

Use the dependence structure required by the selected model. Do not assume independent failures simply because separate estimates exist. Linearity can justify adding expected contributions without independence, but it does not justify duplicated quantities, unsupported causal contributions, or a joint tail probability.

Check whether a claimed dominance holds across the compatible joint conditions. Keep the conditions for all alternatives within the same scenario. Where the joint relation is missing, state what the known bounds establish and what comparisons remain open.

#### PSDA.8:4.5 - Apply only an admitted comparison rule

State what “better”, “equivalent”, “dominated”, or “incomparable” means for this use. A coordinatewise comparison may establish that one alternative is no worse on every included coordinate and better on at least one. That conclusion remains limited to those coordinates, conditions, and admissible alternatives; an overall recommendation requires the other material values, protections and authority relevant to that task.

Use the applicable priority, threshold, outranking or compensation rule. Give its source, such as attributable preferences, governing terms or assumptions supplied for this calculation. Preserve ordinal scales and stated ties. With several admissible value models, report what holds throughout them and what depends on the model.

Use `A.19.CPM` when the needed profile, comparator, admissibility and evidence conditions hold. Report its set-valued comparison with its application and evidence grounds. Distinguish the comparison outcome, a record expressing it and any subsequent selection or permission. Where those conditions do not hold, use a suitable direct comparison or name the outstanding gap.

Distinguish three important outcomes. Two alternatives can be tied under a rule, incomparable because of supported conflicting consequences, or not yet comparable because a necessary input is missing. Preserve the difference. If no candidate meets a protected condition, return that failure rather than ranking the least nonconforming candidate as acceptable.

For finite uncertain consequences, use an applicable supplied utility account and the probability model to compare expected utilities. If the utility input must be constructed from lottery judgements, **PSDA.6:4.5.6** shows how to construct it and compare over the compatible family. Reuse common consequence meanings and a qualified probability model. Where a scenario or noncompensatory rule already answers the question, use that result directly.

#### PSDA.8:4.6 - Return the relation and what would change it

Identify the alternatives, question, common basis, profiles, source limits and comparison rule. Give the supported relations and any material disagreement, exclusion or unresolved comparison. State which premises matter to later use and what could invalidate a dependent conclusion.

`PSDA.9` can use the comparison and its evidence to assess robustness under the same configuration and horizon. An adviser can use it for a recommendation and a decision holder for a choice. If the work includes a programme or work plan, establish its own basis. A report of subsequent work or its result needs evidence of that occurrence. Attributing an effect to the work needs grounds for the connection.

An unexplained rank can reveal a missing consequence path. For consequential use, establish the necessary model, source, calculation or implementation and relevant protections at the strength required by the domain. Reproducing a calculation checks a different claim from validating its empirical premises.

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

The values are stipulated for this comparison. Reachable assistance and property-loss consequences remain outside the numerical slice. Their values and protected conditions may block an overall recommendation.

Under normal access, M costs less and has fewer service-loss hours than F. Under road loss, F loses fewer service hours but costs more. Thus the slice establishes no condition-independent dominance between F and M. N uses fewer incremental resources but loses more service hours; zero incremental cost does not mean that the baseline has no continuing obligations or consequences.

For S, identify the whole-arrangement result that is still missing. The narrower relations among N, F and M remain usable. They leave the complete four-candidate recommendation open.

#### PSDA.8:5.2 - Compare whole development arrangements, not component scores

In the ninety-day organization case, a course assessment and an AI benchmark cannot be placed directly into one service-reliability ranking. Suppose the adviser obtains a qualified allocation and operations comparison for two whole arrangements: I, internal development with covered service duties, and H, a mixed human–tool arrangement with oversight and fallback.

The hypothetical supplier result gives ninety-day unplanned service-loss bounds of 12–18 hours for I and 8–20 hours for H, on the same service definition and operating conditions. Both retain their separately qualified resource and security conditions. No joint relation between the uncertain losses is supplied.

The marginal bounds alone rule out neither lower nor higher loss for H relative to I. They establish neither a uniform ordering nor equality, and do not show that both orderings occur in feasible joint states. Report the ordering as unresolved. If the intended use needs a stronger relation, investigate how common operating or coordination conditions couple the two losses.

Keep the human capability finding, organizational allocation and version-specific AI evaluation tied to their respective subjects. Use a qualified account of their connection to the whole arrangement for a claim about service loss.

#### PSDA.8:5.3 - Cheap non-use

A current qualified comparison already covers two replacement arrangements, their transition costs, service consequences, and the recipient's value rule. Use that comparison for the requested assessment or the authorized holder’s choice. A second consequence table with the same content adds no new result.

#### PSDA.8:5.4 - Two feasible library services with opposed and unknown effects

A library must compare two ways of giving complex reference help during the next four weeks: A, booked consultations with preparation time; B, a walk-in desk with triage. Both have qualified staffing, access and budget arrangements. Neither is excluded for infeasibility. The following observations and judgements are stipulated for this four-week case.

The reader wants a usable answer; a shift worker also needs a way to seek help without knowing next week's schedule. The librarian wants uninterrupted preparation for difficult questions. The manager needs a service whose answer quality and accessibility can both be defended. These are distinct concerns, not interchangeable satisfaction scores.

The practitioner interviews the participants separately and constructs these relationships:

| Relationship in this case | Ground and limit |
| --- | --- |
| A usable specialist answer needs the reader's question, an accessible relevant collection, and competent librarian work together. | The service definition and a sample of completed requests support this necessary combination. Availability of the collection alone does not produce an answer. |
| The librarian depends on the reader providing enough detail before preparation can start. | The reader supplies the question; the librarian explains which missing details prevent preparation. The booking confirmation itself is not that provision. |
| Booking online or through the staffed telephone can obtain a slot. | Either route suffices for reserving an available slot; they are not mutually exclusive. Neither establishes that the reader can attend. |
| Advance detail and protected preparation help answer quality under A. Walk-in interruptions under B impair preparation for difficult questions. | Librarians can identify the interrupted work in the sample. This supports the direction, not a population-wide effect size. |
| B permits a visit without a prior appointment; A requires attendance at a booked time. | The governing service rules establish this difference. Shift workers explain why the appointment condition can obstruct their access. |
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

The manager receives the explained comparison, the conditions defeating one access route and the missing premise of the new candidate. A service change requires a decision by the responsible holder.

### PSDA.8:6 - Bias-Annotation

**Scope:** consequence comparisons for bounded decision-support use. **Lenses:** **Onto/Epist** separates alternative, forecast, observation, and result; **Arch** exposes interaction and distribution; **Prag** fixes the receiving question; **Gov** preserves conditions and authority; **Did** makes the comparison replayable.

Ranking bias prefers closure over partiality. Baseline bias compares change with an empty world. Aggregation bias hides losers and shared burdens. Model precision can conceal missing applicability. Counter these by exposing consequence paths, testing the common basis, and stating the relation the evidence supports.

### PSDA.8:7 - Conformance Checklist

- [ ] Alternatives, subject, configuration, affected subjects, horizon, and receiving use are fixed for the comparison.
- [ ] Candidate, value, and uncertainty inputs are current and compatible or their gaps are returned.
- [ ] Each material consequence has a stated subject, timing and evidence path, or the account identifies the missing link and its effect on the comparison.
- [ ] Where a qualitative network is constructed, relationships have distinct meanings and grounds; opposing and unknown evidence reaches the judgement without arithmetic cancellation.
- [ ] A backward proposal is tested forward as a whole; an unsupported transition or failed combination is not generalized to every possible design.
- [ ] Transition, interaction, shared burdens, and displaced losses are included where they can change the result.
- [ ] Measures, value transformations, protected conditions, and evidence retain their different meanings.
- [ ] Missing entries are not zero, equal, or silently favorable.
- [ ] The comparison rule and admissible operations are explicit.
- [ ] Ties, supported incomparability, and inability to compare are distinguished.
- [ ] The result states the relations supported under the applied rule, with any limits, dissent or changed premise that matters to its use.
- [ ] Any claim about robustness, recommendation, authority, subsequent work or effect has grounds for the claim being made.

### PSDA.8:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Compare a component's score with a whole arrangement's outcome. | Obtain consequence claims for the same receiving subject and use. |
| Use favorable conditions for each alternative. | Hold the comparison basis fixed or show explicit conditional branches. |
| Sum separately advertised benefits. | Recover overlap, interaction, and the qualified whole-arrangement result. |
| Treat overlapping uncertainty intervals as equality. | State what relation the bounds support and what joint information is missing. |
| Rank a failed protected condition by compensatory score. | Keep eligibility separate and return the failure. |
| Call an archive front a consequence comparison. | Identify the comparator used and the profiles, conditions and evidence to which it applies. |

### PSDA.8:9 - Consequences

The recipient can inspect the basis and scope of each comparison. A missing domain result can leave a precise question or a valid partial answer. Work on dependencies and consequences costs effort. Concentrate it where it could change the conclusion or strengthen the grounds the intended use requires.

### PSDA.8:10 - Rationale

A consequence comparison connects proposed actions to values through qualified claims about affected subjects. Keeping that chain visible prevents a ranking from silently deciding the model, value system, or protected conditions. Separate comparison and choice allow a well-supported partial answer to remain a valid result.

### PSDA.8:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How should alternatives be connected to consequences? | Use explicit outcome models with the conditions and dependencies needed by the decision. | Rank isolated attributes or tool outputs without a consequence path. | **Adapt:** :4.1–:4.4 reconstruct only decision-changing consequence paths and shared burdens. The added effort is accepted when an omitted interaction could reverse the comparison; a qualified existing account is reused. | Borgonovo et al.'s [2026 decision-analysis review](https://doi.org/10.1016/j.ejor.2025.05.023) supplies the current graphical-model and uncertainty line. It does not validate a local mechanism or establish causal effects from arrows. `C.11.CRC` supplies a missing finite configuration-relative contribution, not field calculations. | Reopen when a changed configuration, mechanism, affected subject, or horizon invalidates a consequence path. |
| What comparison is justified by conflicting or incomplete values? | Use a declared preference model and preserve its partial or model-dependent relations. | Impose one total weighted rank. | **Adapt:** :4.5–:4.6 retain ties, incomparability, and missing-input distinctions. A partial relation can preserve a real difference in values even when no total rank follows. | Greco, Słowiński, and Wallenius's [2025 MCDA review](https://doi.org/10.1016/j.ejor.2024.07.038) is a comparison candidate for alternative preference and recommendation forms. Its finite-action methods do not supply local values, probabilities, or decision authority. | Reopen if elicitation or evidence changes the admitted model set or resolves a previously missing comparison. |
| How can early qualitative consequences be constructed and questioned before a complete domain model exists? | Make the intermediate relationships and their grounds explicit, carry each alternative through them, and use attributed domain judgement where evidence does not determine the result. | Draw influence arrows, count favorable signs, or declare a complete model necessary before any useful comparison. | **Adapt:** :4.2.1 and :5.4 supply construction, questioned propagation, conditional backward exploration and local revision; no new notation or solver is required. | Horkoff and Yu's [PoEM 2009 procedure](https://www.cs.toronto.edu/~jenhork/Papers/Horkoff_PoEM_2009l.pdf) and [ER 2010 backward analysis](https://www.cs.toronto.edu/~jenhork/Papers/ER_Horkoff.pdf) are historical method anchors, not current empirical validation or iStar 2.0 semantics. Qualitative support does not establish causal magnitude, participant commitment or realized success. | Reopen when a changed relation, stakeholder judgement or domain model changes a material consequence; use a stronger model when quantitative interaction or feedback decides the answer. |
| Does generic candidate stewardship already compare the consequences? | Keep profile comparison, finite contribution, and archive/front stewardship distinct. | Treat C.18 as a general consequence-ranking Method. | **Adopt:** :4.2 and :4.5 use the exact C.11.CRC and A.19.CPM contributions when needed; the PSDA consequence account retains its field question. No archive machinery is required for a small comparison. | Current `C.18` governs generation, archive, and front objects; `A.19.CPM` governs its admitted set-valued comparison; direct domain Methods supply consequence models. Their different result boundaries defeat the broader attribution. | Reopen when the question concerns archive stewardship or a direct comparison contribution changes. |

### PSDA.8:12 - Relations

- `PSDA.5` supplies the alternative family, `PSDA.6` the value and trade-off account, and `PSDA.7` bounded evidence and uncertainty claims. Each is used only under compatible subject, configuration, horizon, and receiving conditions.
- `PSDA.9` may consume the comparison's evidence to test robustness for that same use. The comparison does not entail the robustness result.
- `C.11.CRC` supplies a missing finite configuration-relative contribution claim. `A.19.CPM` supplies an admitted profile comparison only when its own conditions obtain. `C.18` retains its different archive/front and generation function.
- Direct engineering, operations, human-development, AI/model, financial, scientific, and other practices govern their own consequence and evidence results. `A.10` qualifies reliance; `A.15.9` supports a needed bounded outside contribution.
- For a later choice, the decision holder can use `C.11`. Use an applicable qualified source for a missing or incompatible premise, or state the specific limit.

### PSDA.8:End

## PSDA.9 - Test Robustness and Sensitivity of Decision Alternatives and Their Comparison

> **Type:** Method pattern body
> **Status:** Stable
>
> **Primary working result:** the conditions under which a specified claim holds, reverses or remains open. Identify useful further information when it could change the finding or a decision that relies on it.

### PSDA.9:1 - Problem frame

**Use this when** you need to know how a forecast, weight, model or threshold affects a finding about alternatives. Test whether a ranking reverses, whether a service still meets its limit, or whether obtaining further information would improve the evidence or decision enough to justify its cost.

State the claim and which changes it must withstand. Vary the relevant conditions over a justified range. Report where the claim holds, fails or remains open. If further information could matter, identify the question it could answer.

**Sensitivity** describes how a result changes with inputs, assumptions, or models. **Robustness** says whether a declared performance, admissibility, or comparison condition continues to hold across specified variation. A sensitive magnitude can leave the preferred set unchanged; an insensitive average can hide a decisive threshold crossing. Section 4.3.1 supplies a small paired-response test when the response at a central input can conceal such a difference.

Reuse a current robustness result that covers the claim and the changes in question. Validate the underlying model where the conclusion needs that assurance. The authorized holder chooses or authorizes a decision or probe when one is called for.

### PSDA.9:2 - Problem

A one-point ranking can hide a narrow region of support. Small changes in a value trade-off can reverse it; a common-cause failure can defeat every alternative; a different model can change which conditions are even represented.

Sensitivity work can also miss the decision. A tornado chart may rank output variance rather than choice relevance. One-factor-at-a-time tests can miss interactions. Running thousands of similar scenarios can create an appearance of broad coverage, and their frequency can be mistaken for probability. Check whether the additional calculations cover a relevant untested condition.

### PSDA.9:3 - Forces

| Force | Tension |
| --- | --- |
| Coverage and effort | Joint or structural changes can matter, while unrestricted scenario expansion consumes the available time. |
| Stability and truth | Agreement across tests supports stability within their model and coverage. Extending that finding requires grounds for the larger region. |
| Values and evidence | Better information can resolve a fact, while a disputed trade-off needs a value judgement or legitimate collective decision. |
| Flexibility and commitment | Staging can preserve options, while monitoring, lead time, reversibility, and later authority may be unavailable. |
| Information and action | A probe can improve the finding or change a decision, but it also costs time, resources, exposure, and foregone opportunity. |

### PSDA.9:4 - Solution

State the claim, the variation to be covered and the evidence already available. Choose the least costly adequate tests or proofs for the remaining uncertainty. Report where the claim holds or fails and which information could resolve any consequential gap. A later choice belongs to its authorized holder.

#### PSDA.9:4.1 - State what is being tested

Identify the claim, subject, configuration, horizon and intended use. For a comparison, recover the alternatives, consequences and applicable rule or value basis. Compatible evidence from `PSDA.8` or a direct comparison can supply the input.

Specify the test. It might ask whether one alternative remains no worse under a declared rule, whether every retained alternative meets a service threshold, whether a protected condition is ever violated, or whether the recommendation must remain conditional. Different tests can produce different answers.

Name the robustness criterion before interpreting results. Satisfactory performance across tested conditions, worst-case loss, regret relative to the best available alternative in each condition, and stability across compatible value models answer different questions. Do not change the criterion after seeing which candidate it favors. If the criterion or allowable trade-off remains open, report any conditional results the supported criteria yield and what remains undecided.

#### PSDA.9:4.2 - Bound the changes by evidence and the decision

Identify the uncertainties or judgement changes that could affect this test: input values, future conditions, model structures, consequence definitions, preference models, evidence qualification, candidate membership, or horizon. State why the selected variations are relevant and what they omit.

Ranges and scenarios need a basis. Distinguish observed bounds, elicited judgements, scientifically or operationally plausible cases, and deliberately extreme stress tests. A stress-test failure can reveal vulnerability without establishing the failure's probability.

Preserve dependencies and feasibility. Joint variations should describe possible or explicitly hypothetical conditions, not arbitrary combinations of incompatible endpoints. Changing a binding legal, safety, consent, or security condition is not an ordinary parameter perturbation. Use applicable evidence of its meaning, scope and force, or identify the missing ruling where a decision is required. If the question is whether its protection warrants its measure, threshold or burden, use the bounded `C.11.DUA` §4.3 appraisal through `PSDA.6` §4.4. Return the substantive recommendation and actual amendment authority/window separately; until a revision applies, test present alternatives under the binding condition.

If a needed variation cannot be bounded, identify the claim that the gap limits. “Across all plausible futures” is stronger than “across the three stated futures” and needs stronger support.

#### PSDA.9:4.3 - Test locally, then expand where the failure can hide

Use an existing adequate test or begin with a low-cost discriminating check, such as a boundary value, an alternative value judgement, an omitted condition, or a direct challenge to one decisive assumption. If the basis is changed, recompute the comparison for the affected alternatives or use a result that already covers the change.

Use joint or global variation when interactions, nonlinearities, common causes, thresholds, or structural alternatives can change the result. A one-at-a-time test is insufficient for a claim about those combinations. Choose tests, sampling or proofs appropriate to the model and the claim about the combinations.

Keep empirical variability, model uncertainty, and value disagreement distinguishable. If a model change alters the meaning or comparability of an output, establish comparability before combining numerical outputs. Otherwise report their different meanings and keep the values separate.

A computational result is limited by the tested region and procedure. An analytical inequality may establish a whole region under its assumptions; a finite sample usually establishes only sampled behavior unless a further guarantee is justified. State that difference.

##### PSDA.9:4.3.1 - Compare a central response with two equally displaced inputs

Use this small test when the response to a varying input may make a central estimate misleading. It needs a response account suitable for the stated comparison, not an assumed probability distribution.

1. Name the input and the response it affects. Fix the arrangement, affected subject, time window, other relevant conditions, response unit and preferred direction. Choose a central input `x` and displacement `h > 0` so that `x-h`, `x` and `x+h` lie within the account's admissible domain. Equal input differences and averaging the responses must be meaningful on their respective scales; numerical labels alone do not suffice.
2. Obtain the three comparable response values from the qualified model or suitable observations. For response `r`, calculate the endpoint mean and its difference from the central response: `D = (r(x-h) + r(x+h))/2 - r(x)`. The equal weights define this constructed test. Calling the mean a real-world expectation requires a separately qualified probability model.
3. Interpret `D` on the declared response coordinate. A positive difference means the endpoint mean exceeds the central response: worse for a loss, better for a benefit whose higher value is preferred. For a target-valued response, use its declared preference rule. Zero means no midpoint gap at these three points; it does not prove linearity or robustness over an interval. Examine each tested response against any independently justified threshold as well.
4. Widen the displacement or test another consequential condition when the model supports the altered inputs and the further result could change a needed finding or decision enough to justify the work. Report the tested values and gaps; do not turn one finite comparison into a regional convexity, derivative or global robustness claim.

If the response model or scale is inadequate, identify the resulting limit. Give a conditional calculation or qualitative comparison where its assumptions support one. Assess the value of further observations if they are being considered.

When a change of exposure is under consideration, specify the proposed arrangement and compare its whole contribution through `C.11.CRC`. Include the means, carrying burden and displaced work required to maintain a proposed protection. A stated spending limit alone does not enforce a consequence limit. `C.16` governs quantity and scale use; `C.29` governs a needed mathematical-representation correspondence and its transfer limits. The robustness account remains the result here.

#### PSDA.9:4.4 - Map holding regions and reversals


Report which condition holds in each relevant region, where alternatives exchange order, where a threshold is crossed, and where the comparison becomes unsupported. Include boundaries and ties when they can change the return.

Separate a genuine reversal from a different question. A new value rule, candidate, subject, or horizon may define another comparison rather than a parameter change inside the old one. Preserve the original basis so that the reader can see which happened.

Test omissions as well as numbers. A stable two-candidate result can be irrelevant if a material third candidate remains unexamined. A common failure can show that all current alternatives are inadequate. Return that candidate or formulation gap instead of calling the least bad option acceptable.

The result may be a robust retained set, a conditional preference, several non-dominated alternatives, a failure region, an unresolved boundary, or a blocker.

#### PSDA.9:4.5 - Connect the remaining uncertainty to information value

Identify an attainable observation, calculation or interpretation that could change the requested finding, its grounds, eligibility or the action available. Compare its expected contribution with the cost and delay. A large change in a numerical output may leave the relevant conclusion unchanged.

For an expected-utility comparison, use MMP.16:4.2–4.5 to model the records the proposed observation could produce. For each record, find the highest conditional expected utility among the actions then available. Weight these values by the probabilities of the records, and compare their sum with the best expected utility available without the observation. For a record with a continuous distribution, use the corresponding expectation. Include collection cost, delay, any change to the system and lost opportunities in the consequences of the compared options. Subtract a cost directly from expected utility only if it is additive on that scale and has not already been counted. Use PSDA.6:4.5.6 if a required utility account must be constructed. If several probability and utility accounts are compatible, report the comparisons within each account or the supported range. Averaging accounts needs separate grounds. Perfect information can bound the benefit of information under the same actions and conditions. Several observations may supply overlapping information.

If the probabilities lack support, report the result under the specified conditions and what a feasible observation could resolve. Calculate an expected value on stipulated probabilities only for an explicitly conditional question.

When selecting a further probe, use `C.11` or the applicable decision procedure to compare the attainable options, budget, benefits and costs. Identify the authority required for execution. A dispute about a value or mandate may need a judgement by its holder.

#### PSDA.9:4.6 - Examine adaptive alternatives without assuming free flexibility

When a staged candidate is live, establish which later actions it keeps feasible. The later observation must arrive early enough, be interpretable, and leave a feasible response within the remaining resources and authority. Include monitoring cost, lead time, temporary exposure, transition burdens, and irreversible loss of options where material.

Check the applicable rule for responding to a policy failure. It may trigger a specified protection or require reconsideration by a decision holder. If a necessary route, response or authority is missing, identify that limitation of the staged option.

Before recommending a pilot, check its safety, timing, information value and which response would remain feasible. Report an attainable information result when its value to the question warrants the delay.

#### PSDA.9:4.7 - Return a bounded robustness account

Return the tested claim and criterion, variation and omissions, methods and evidence limits. Report the holding regions, failures, ties or reversals the evidence establishes. Identify any consequential unresolved comparison, missing candidate or useful further information, its feasibility, and the condition under which the result would need reconsideration.

A practitioner preparing a recommendation with `PSDA.14` can use compatible evidence for the same configuration and horizon. If a necessary result is missing, stale or incompatible, use a qualified direct result or state the gap. The decision requires its own authority.

Recognize the need when a relevant variation could alter a finding, a threshold result or its grounds. Consequential assurance also requires qualified model and source use, correct analysis, adequate challenge coverage, and the direct domain's protection and independence requirements. Robustness to uncertain parameters does not cure an invalid model or missing safety result.

### PSDA.9:5 - Archetypal Grounding

#### PSDA.9:5.1 - An explicit reversal boundary for the pump comparison

Use the illustrative F and M slice from `PSDA.8`: F costs 8 incremental budget units and loses 2 service hours with normal access or 3 with road loss; M costs 5 and loses 1 or 9 hours. N remains the baseline and S still has an unqualified whole-arrangement result. The following calculation tests only F against M; it does not close the wider candidate comparison.

For an illustrative analytical question, suppose a declared value model minimizes expected service-loss hours plus `lambda` times incremental budget units. For this illustration suppose `lambda` has been elicited as a trade-off in service-hour-equivalent value per budget unit. The calculation can equally be made conditional on an explicitly stipulated trade-off. Attributing it to the public requires evidence about the public’s values. Let `p` be the road-loss probability if a qualified probability model supports one.

Under those assumptions:

- F's value loss is `2 + p + 8*lambda`.
- M's value loss is `1 + 8*p + 5*lambda`.
- F has lower value loss precisely when `7*p > 1 + 3*lambda`; equality is a tie.

For `lambda = 0.5`, the reversal is at `p = 5/14`, approximately 0.357. At `p = 0.2`, F and M give 6.2 and 5.1 respectively, so M is better under this model. At `p = 0.6`, they give 6.6 and 8.3, so F is better. These are invented sensitivity settings, not a forecast.

The source comparison supplies no road-loss probability. The calculation therefore establishes the conditional boundary. Without a probability basis, report the service loss in each access condition.

A different declared test asks whether modeled service loss is at most 4 hours in both stated access conditions. F satisfies that illustrative test; M fails it under road loss. The four-hour cut is a second criterion stipulated for this illustration. F's result covers only those two modeled conditions.

Return the reversal boundary and the threshold result for F and M under their stipulated conditions. Identify unresolved real-world probability and value premises, the gap for S and any unassessed consequences or protections needed for a wider comparison. The authorized board makes the investment decision.

##### PSDA.9:5.1.1 - A separate constructed delay-response question

For a different question, fix a thirty-day service window and one access interruption. A stipulated model supplies the service-loss hours for F and M at three access delays; lower service loss is preferred. Each arrangement and all other modeled conditions stay fixed while delay varies.

| Access delay in days | F: service-loss hours | M: service-loss hours |
| --- | ---: | ---: |
| 0 | 2 | 1 |
| 1 | 2.5 | 3 |
| 2 | 3 | 9 |

With `x = 1` day and `h = 1` day, M's central response is 3 hours, its endpoint mean is `(1 + 9)/2 = 5` hours, and `D = 2` hours. F's central response and endpoint mean are both 2.5 hours, so its `D = 0`. F has no midpoint gap at the tested points. A claim about values between them requires further grounds.

Under the separately declared four-hour service-loss criterion, M's two-day response of 9 hours fails. F satisfies that criterion at the three stated points only. Neither endpoint mean is an expected real loss without a probability basis, and a central response below four hours does not settle the endpoint test.

Report the finite response difference, the failure at the two-day delay and the model and coverage limits. A question about investing in F or changing access protection requires evidence about the whole arrangement and the relevant authority. Where the model is stipulated, keep the answer conditional on it.

#### PSDA.9:5.2 - What would change a development recommendation?


In the illustrative ninety-day organization case, I is internal development with covered service duties and H is a mixed human–tool arrangement. The suppliers’ separate bounds of 12–18 and 8–20 service-loss hours leave the ordering open.

Suppose a qualified joint operating model now supplies two admissible conditions within those bounds:

| Condition | I: service-loss hours | H: service-loss hours | Supported comparison on this coordinate |
| --- | --- | --- | --- |
| Required handoff coverage is present. | 14 | 10 | H has less service loss. |
| The specified handoff coverage is absent. | 16 | 20 | I has less service loss. |

In this joint model the relative service loss reverses when the handoff coverage changes. The comparison concerns whole arrangements. A choice that relies on this coverage needs evidence of its feasibility and persistence under the proposed allocation. Use applicable evidence or retain the conditional comparison. Attributing the difference to human learning or model quality would require other evidence.

Where evidence about the coverage could be obtained in time and would justify the effort, identify it as an information priority with its cost and limits. Otherwise retain the conditional comparison. A different team or model version needs a basis for transfer to this arrangement.

#### PSDA.9:5.3 - Cheap non-use and honest stop

A current analysis already proves the same service comparison throughout the relevant parameter interval, and the only proposed new computation repeats interior points without challenging another assumption. Reuse the result. If the untested issue is instead a missing causal or safety premise, use an applicable direct result or identify the missing premise and what it prevents; more parameter samples will not supply it.

### PSDA.9:6 - Bias-Annotation

**Scope:** robustness and information questions for bounded decision support. **Lenses:** **Epist** distinguishes model stability from truth; **Prag** tests decision relevance; **Arch** exposes interactions and omitted alternatives; **Gov** preserves protected conditions and future authority; **Did** makes reversals and limits readable.

Winner-protection bias selects narrow ranges or convenient criteria. Scenario-count bias mistakes volume for coverage. Variance bias favors a probe that changes the output but contributes little to the requested finding or choice. Flexibility bias assumes cost-free adaptation. Counter these by declaring the claim, criterion, region, and real response capability before interpreting the result.

### PSDA.9:7 - Conformance Checklist

- [ ] The claim, criterion, subject, configuration and horizon are stated, including the alternatives where they are compared.
- [ ] The robustness criterion is explicit and not chosen after seeing the preferred winner.
- [ ] Variation ranges, scenarios, dependencies, and exclusions have a recoverable basis.
- [ ] Binding conditions are not silently relaxed as parameters. A disputed requirement's merits return remains separate from its present force and from the robustness result.
- [ ] Tests address relevant interactions, structural differences, and omitted alternatives.
- [ ] Sampled behavior, analytical region claims, and unsupported extrapolation are distinguished.
- [ ] A paired-response test states its admissible inputs, comparable response scale, construction weights, preferred direction and exact finite result; no midpoint gap or constructed mean is overread as global robustness or an actual expectation.
- [ ] Holding regions, ties, reversals, failures, and gaps are reported for the conditions the evidence covers.
- [ ] Information priorities concern attainable results that can change a needed finding, its evidence or a decision and include cost or feasibility limits.
- [ ] Adaptive claims account for observation, lead time, response feasibility, and later authority.
- [ ] The conclusion states what the robustness evidence establishes and any further grounds needed for a recommendation, authorized action or claim of effect.

### PSDA.9:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “The winner is robust” after a few small perturbations. | State the claim, variation region, method, and untested failure mechanisms. |
| Count successful scenarios as a success probability. | Supply a qualified probability measure or report conditional coverage only. |
| Change one input at a time despite common-cause failure. | Test the relevant joint conditions under a justified dependence model. |
| Treat the largest output variance as the best information target. | Check whether attainable information could improve the requested finding, establish a condition of eligibility or change the decision. |
| Recommend a pilot whenever evidence is thin. | Establish information value, safety, timing, reversibility, and response feasibility. |
| Change the robustness criterion to preserve the preferred option. | Show the different questions and return the criterion disagreement. |

### PSDA.9:9 - Consequences

The recipient can see the conditions supporting a comparison and where it fails. Recomputing selected cases costs time. Stop when further work would add too little to the requested result or when a different missing premise limits it.

### PSDA.9:10 - Rationale

Stating when the conclusion holds or reverses makes its scope inspectable. Distinguishing the uncertainty, values, model and capacity to respond lets the recipient judge whether a further inquiry could improve the finding or decision.

### PSDA.9:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How can a comparison remain useful when future conditions or models are unsettled? | Stress-test declared performance and comparison claims across justified conditions; examine feasible adaptation where it matters. | Optimize one forecast or call an unspecified staged policy robust. | **Adapt:** :4.1–:4.4 and :4.6 return bounded holding and failure regions. Extra scenario and response analysis is accepted when a single forecast or assumed flexibility can conceal failure. | Lempert et al.'s [2024 DMDU analysis](https://doi.org/10.3389/fclim.2024.1380054) supplies the current robust-decision line; the [2019 DAPP chapter](https://doi.org/10.1007/978-3-030-05252-2_4) supplies pathway, timing, and failure-condition distinctions. Their applied domains do not supply universal thresholds, scenario probabilities, or local authority. | Reopen when an omitted condition, implementation lead time, or response constraint defeats the stated region. |
| Which sensitivity result should guide further inquiry? | Link local and joint sensitivity to the decision boundary and the value of attainable information. | Use output variance or a one-factor chart as a universal research priority. | **Adapt:** :4.3–:4.5 distinguish magnitude sensitivity, reversal, and probe value. More computation is justified only when the added question can change the bounded return; selecting a probe requires its own decision. | Borgonovo et al.'s [2026 review](https://doi.org/10.1016/j.ejor.2025.05.023) is the synthesis candidate for sensitivity and information acquisition. Its formal approaches need their own model assumptions; `C.11` retains the local choice and probe-worthiness result. | Reopen when the feasible probe, decision window, dependency model, or costs change. |
| What can a central-input response conceal? | Compare the central response with a symmetric endpoint mean and test consequential thresholds separately. | Rely on the central response alone or infer a whole-region property from three points. | **Adapt:** :4.3.1 and :5.1.1 make a finite nonlinear-response check usable without inventing probabilities. | Taleb and West's [2023 finite-difference and convexity account, §III-C and Appendix B](https://arxiv.org/html/2209.14631v2), supplies the distinction between a finite comparison and stronger smoothness, regional or probability claims. Its clinical models do not validate a decision-support response model. | Reopen when the response model, scale, supported domain, subject or decision threshold changes. |
| What if the value model, rather than the forecast, is incomplete? | Test relations across the models compatible with the expressed preferences. | Treat one fitted weight vector as uniquely known. | **Adapt:** :4.1–:4.4 retain value-dependent reversals instead of calling preference uncertainty factual noise. The deliberate trade-off is a possibly larger retained set. | Greco, Słowiński, and Wallenius's [2025 MCDA review](https://doi.org/10.1016/j.ejor.2024.07.038) supplies robust ordinal regression as a best-known-line candidate for this question, not a requirement to use one algorithm or to collapse participants' values. | Reopen when elicitation or a legitimately governed value decision changes the compatible model set. |

### PSDA.9:12 - Relations

- `PSDA.8` may supply the consequence comparison and its evidence for the same configuration and horizon. Evidence enables this test but does not establish its result.
- `PSDA.14` may consume robust regions, reversals, and information priorities as evidence for its recommendation. This neither entails the recommendation nor transfers the later choice authority.
- `A.10` governs bounded evidence reliance; direct domain and modeling practices govern the validity of claims, models, ranges, and tests. Revalidate a source-dependent conclusion when the changed use affects its grounds.
- `C.16` governs quantities, scales and response comparability; `C.29` governs a needed mathematical representation and its correspondence limits. Neither supplies domain validation merely through the calculation.
- `C.11.CRC` compares a proposed finite change to the arrangement, including the feasibility and burden of maintaining a protection. A sensitivity result does not itself change that arrangement.
- `C.11` governs a local choice and the worth of another probe. Information priority, probe selection, WorkPlan, performed inquiry, and observed effect remain distinct results.
- Candidate formation, value elicitation, model repair, and follow-up remain their own questions when the test exposes a gap there. For a missing or incompatible input, use a qualified direct result or report precisely what remains open.

### PSDA.9:End

## PSDA.11 - Bound the Decision-Support Engagement and Authority Boundary

> **Type:** DPF pattern body
> **Status:** Stable
>
> **Primary working result:** a bounded engagement question. State what decision support is needed, who can use it, the subject, horizon and present scope. Identify any outstanding condition that limits the work and what would reopen the boundary. For a later decision, identify its holder and authority.

### PSDA.11:0 - Use This When

Use this pattern when the intended use of decision support is unclear. A request such as “help decide” or “what should we develop next?” can leave open the question, subject, horizon, recipient, consequences, authority or the result needed.

Start with the work or decision the result should inform. Identify who prepares the result and who uses it. If a later choice is involved, establish whose decision it is. Return the bounded question or identify what you still need to establish it.

A bounded question gives later analysis a subject and a stopping point, both in a disputed situation and in an ordinary request for advice. A model, score or recommendation can inform the authorized decision.

When the authorized chooser has an adequate option set and comparison, use `C.11` or the applicable choice rule. If a single specialist practice can answer the whole question, use its result directly. Use this engagement boundary when that contribution must inform a separately governed decision-support use.

#### PSDA.11:0.1 - Working Distinctions

| Working term | Meaning in this pattern |
| --- | --- |
| decision-support engagement | The bounded situation in which a performer is expected to make a useful result available to a receiving decision or Work. |
| decision-support performer | The participant expected to prepare the result. Identify the capability and, where required, the authority for the work it will do. |
| recipient | The participant who receives the result for a specified use. Establish separately who holds any later decision. |
| holder or subject | The entity whose alternatives or consequences are being considered, such as a person, an organization, a place or a policy. Establish which entity the question concerns. |
| choice owner | The Agent authorized to make, reject, defer, probe, or reroute the later decision. It may coincide with the recipient or performer only when that coincidence and authority are independently supported. |
| receiving decision or Work | The decision or work that uses the result. The result can inform its conclusion or grounds, even if the action stays the same. |
| bounded engagement question | The smallest decision-support question that makes the intended return, use, participants, scope, authority boundary, and reopen condition usable now. |

### PSDA.11:1 - Problem frame

Decision-support practice often begins before there is a stable “problem”. One engagement opens with several participant groups arguing about causes and values. Another opens with a calm request for advice whose recipient, subject, horizon, or later authority is still vague. Both can be prematurely forced into a workshop brief, model boundary, criteria table, or option set.

Bound one engagement for one receiving use. Identify the question, what result can be prepared now, what lies outside it and what missing fact or authority would affect the answer. Construct a formulation, alternatives, comparison or recommendation only where the receiving work calls for it.

One unclear condition that affects the return is enough to start. For consequential use, establish the identity, capability, assignment, permission, authority, evidence and domain protections on which the result relies.

### PSDA.11:2 - Problem

An unbounded engagement can expand into every concern, participant, model, consequence, and possible future. The performer gathers material without knowing what finding or decision it will inform. A premature boundary creates the opposite failure: the sponsor's wording becomes the only formulation, the visible recipient is treated as the choice owner, or an analytical result is presented as authorization.

These failures compound. A favourite problem-structuring Method can be selected before the decision-support use is known. A list of stakeholders can stand in for affected Systems and material concerns. A model can hide excluded consequences. A recommendation can absorb holder-specific conclusions or take a choice that belongs elsewhere.

Identify the result and its intended use, and keep the boundary open to revision. Examine contested concerns, formulations, affected parties, models, alternatives, values, uncertainty or follow-up where they affect what you can return.

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

Identify the decision or work that can use the result, the subject, horizon, participants, current scope and relevant authority. Return the bounded engagement question when these are sufficiently clear. If something essential is missing, identify it and state the limit it imposes.

#### PSDA.11:4.1 - Name the receiving use before the problem statement

In ordinary language, identify the result, its user, subject, intended use and horizon. For an engagement that informs a later decision, include who holds it. The following engagement illustrates this use.

> Make **[kind of decision-support return]** available to **[recipient]** about **[holder or subject]** for **[receiving decision or Work]** within **[horizon]**; **[choice owner]** retains the later choice.

Determine what finding, evidence or decision the return could affect and what would make an error, delay or omission matter. An exploratory, research, learning or communication task may be a sufficient direct use. If no decision-support result is needed, use the corresponding practice.

The requested return can initially be a bounded question, participant-and-concern account, plural formulation set, model or Method-selection result, alternative gap, comparison, recommendation, blocker, or abstention. Return the result that meets the present use.

#### PSDA.11:4.2 - Separate performer, recipient, holder, and choice owner

Distinguish the positions the intended use requires. The same participant may hold several.

1. who is expected to prepare the decision-support return;
2. who will receive it and for what use;
3. which exact holder or subject is under consideration; and
4. who is authorized to choose, defer, commission a probe or reroute the decision, when such a decision is at issue.

Identify overlapping roles explicitly. A manager may receive advice for a board that holds the investment authority. A team with an appropriate mandate may conduct an analysis and then make its own choice. Its analysis, recommendation and subsequent `ChoiceResult` have separate grounds.

Recover assignment, capability, permission, responsibility, conflict, commitment, or authority only to the extent that the current use relies on it. Use their direct patterns for consequential claims. If the required choice owner or authority basis cannot be recovered, return that exact gap.

#### PSDA.11:4.3 - Bound the subject, horizon, receiving Work, and consequence

State the holder or subject at the grain where the requested conclusions about alternatives or consequences apply. Add the relevant configuration, place, population, operating condition, and interval only when they change the answer. State the receiving decision or Work and the horizon over which the return is expected to remain useful.

Name at least one consequence of getting the boundary wrong. This is a recognition cue, not a complete consequence analysis. When affected Systems, missing participants, duties, interests, or representation can change the engagement, continue with `PSDA.12`. When several formulations would change the findings, their grounds or the indicated actions, continue with `PSDA.1`. When included and excluded concerns need a deliberate scope decision, continue with `PSDA.2`.

#### PSDA.11:4.4 - Choose a provisional boundary and the next truthful branch

Record what is inside the engagement now, what remains outside, and what observation would move that boundary. Use a further method when a needed result is missing.

| Current situation | Further work when needed |
| --- | --- |
| participants, concerns, consequences, or representation are incomplete | recover the participation and concern account through `PSDA.12` |
| materially different formulations or intervention logics remain hidden | develop and compare the relevant formulations through `PSDA.1` |
| the engagement has no usable included/excluded scope and reopen basis | set and reopen the problem boundary through `PSDA.2` |
| the engagement is bounded but needs a model, a choice or combination of problem-structuring Methods, or facilitation | use `PSDA.3` for modeling, `PSDA.4` to qualify a Method or compare or combine Methods, and `PSDA.13` for facilitated inquiry as applicable |
| the engagement is bounded and the live gap is alternatives, uncertainty, comparison, or recommendation | use the relevant method for the missing contribution among `PSDA.5`, `PSDA.6`, `PSDA.7`, `PSDA.8`, `PSDA.9`, `PSDA.14` |
| a premise established by another practice affects the return | inspect or request the smallest bounded result through `A.15.9` |
| an authorized chooser already has an adequate option set and comparison basis | use `C.11` or the direct domain choice rule; stop treating engagement framing as the live question |

Where several contributions are needed, the corresponding work can proceed concurrently if its inputs, resources and authority are available and compatible.

#### PSDA.11:4.5 - Record the bounded engagement question or exact stop

Give enough information for the result to be used within its declared scope.

| Result position | Required content |
| --- | --- |
| intended return | The smallest decision-support result sought now, including blocker or abstention as valid branches. |
| Recipient and use | Who uses the result, the question, decision or work it informs, and the relevant horizon. |
| holder or subject | Name what the question concerns. When the answer depends on a configuration, place, population or interval, give that condition as well. A place or period can itself be the subject when the question concerns it. |
| Participant positions | Who prepares the result. For a decision, who holds it. Include the assignments and authority on which this use depends. |
| current boundary | Included concerns and consequences, important exclusions, and why that cut is usable now. |
| missing value or next branch | Any missing participant, scope, source, evidence, authority or other result, and what remains open because of it. |
| reopen condition | The smallest observable change that can alter the question, scope, authority boundary, or next branch. |

For a decision with an outstanding prerequisite, a short account may suffice.

> Prepare **[result]** about **[subject]** for **[recipient and decision]** over **[horizon]**. **[decision holder]** retains the choice. **[missing fact or authority]** is needed to settle **[specific part of the question]**.



#### PSDA.11:4.6 - Reopen locally and preserve the later choice

Name the event that can invalidate the current boundary: a changed recipient, holder, horizon, receiving Work, authority relation, participant or concern, formulation, source, alternative family, evidence condition, consequence, or later decision. Reopen only the affected position and its dependent results.

A returned recommendation may inform the later decision, and follow-up may observe that later decision, but neither retroactively turns the decision-support performer into the choice owner. If the later choice changes the problem structure and follow-up is needed, use `PSDA.15` to determine which follow-up or reframing question is current.

#### PSDA.11:4.7 - What changes in practice

The practitioner can now state what work the result informs, its recipient, subject, horizon and relevant authority, or explain which condition remains open. Modeling, participation, generating alternatives or preparing a recommendation can then address a specified need.

### PSDA.11:5 - Archetypal Grounding

#### PSDA.11:5.1 - Contested flood-pump decision

A municipal resilience office asks a decision-support team to “solve the pump problem” before the next flood season. Operations staff prefer another permanent pump; finance questions capital exposure; residents contest which districts and harms count; and the emergency investment board owns the later funding and deployment decision.

The team first returns a bounded engagement question.

> For the municipal resilience office, prepare a recommendation for the emergency investment board's pre-season funding and deployment decision about the district flood-pumping arrangement over the next flood season. Compare permanent, mobile, staged, and no-new-purchase branches only after affected districts, operating conditions, safety limits, and material dissent are recoverable; the board retains the later choice.

The boundary is useful but incomplete. `PSDA.12` is next because affected residents, operating groups, concerns, and consequence-bearing Systems can change the engagement. `PSDA.1` is also live because “insufficient capacity”, “unequal protection”, “maintenance fragility”, and “unsafe deployment” imply different interventions. If authority, the horizon or an affected district remains unclear, the team states which comparison, action or recommendation depends on it.

#### PSDA.11:5.2 - Development-direction advice without taking the choice

An engineering executive asks an advisory team, “What should we develop next for AI-assisted incident response?” The phrase does not yet say whether the holder is a person, team, organization capability, model, agent arrangement, or operating platform; whether the recipient or an investment committee owns the choice; or whether the horizon is the next release or the next two quarters.

After one clarification, the holder is the organization's AI-assisted incident-response arrangement, the executive is the recipient, the investment committee owns the later portfolio choice, the horizon is two quarters, and the requested return is a source-qualified development-direction recommendation. The first result is:

> For the executive's two-quarter investment proposal, prepare a bounded recommendation about development directions for the AI-assisted incident-response arrangement; the investment committee retains the later choice. Use relevant existing evidence about capability, organization, operations, the model, safety or authority. Identify any premise still missing and the conclusion it limits.

With the engagement bounded, the practitioner can inspect any needed external results through `A.15.9` and begin with the first missing result among `PSDA.5`, `PSDA.6`, `PSDA.7`, `PSDA.8`, `PSDA.9`, `PSDA.14`. PSDA.11 authorizes no training programme, organization change, model modification, purchase, WorkPlan, or choice.

#### PSDA.11:5.3 - Cheap non-use when the choice is already local

A procurement board is the authorized chooser, has three qualified pump options, a current comparison basis, and no unresolved participant, formulation, scope, authority, or outside-practice premise. The live question is which option to select. Use `C.11` or the board's direct choice rule. Repeating PSDA.11 would add no useful boundary.

### PSDA.11:6 - Bias-Annotation

**Scope:** decision-support engagements for a named receiving decision or Work. **Lenses:** **Gov** concerns participation and decision authority; **Arch**, the engagement boundary and dependent contributions; **Onto/Epist**, keeping the subject, claims, recommendation, and later choice distinct; **Prag**, a useful return at proportionate effort; **Did**, plain entry cues that preserve the distinction between cheap recognition and consequential assurance.

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| sponsor-language bias | The sponsor's first wording becomes the problem and scope. | Name the receiving use, affected consequence, exclusions, and reopen condition before accepting the formulation. |
| authority-by-visibility bias | The meeting chair, report author, model owner, or recipient is treated as the choice owner. | Recover the later decision and its authority basis separately. |
| Method-first bias | A familiar PSM, workshop, model, or scoring scheme determines the engagement boundary. | Return the bounded question first; select Methods only for the result still needed. |
| stakeholder-list bias | A visible list is treated as complete participation and concern recovery. | Continue with `PSDA.12` when affected Systems, representation, duties, interests, or dissent can change the return. |
| recommendation-as-choice bias | A confident recommendation, rank, or tool output is presented as authorization. | Identify the recipient and use of the recommendation. Establish the decision holder, its mandate and any resulting choice separately. |
| exhaustive-framing bias | Every possibly related concern is admitted before any useful result can be returned. | Choose the smallest current boundary and one observable reopen condition. |

### PSDA.11:7 - Conformance Checklist

- [ ] The opening names a recognizable receiving decision or Work and the smallest useful decision-support return.
- [ ] Identify who prepares the result, who receives it and the subject it concerns. Identify the decision holder when a decision is involved.
- [ ] Any coincidence among those positions is explicit and does not transfer authority by wording alone.
- [ ] The holder or subject, horizon, relevant configuration, and at least one consequence of a wrong boundary are visible at the grain needed by the current use.
- [ ] The current included and excluded scope and one observable reopen condition are stated.
- [ ] Contestation opens `PSDA.12`, `PSDA.1`, `PSDA.2` only when participants, formulations, or scope can change the return; it is not a membership requirement for PSDA.11.
- [ ] A bounded direct-advice case can use any needed `PSDA.5`, `PSDA.6`, `PSDA.7`, `PSDA.8`, `PSDA.9`, `PSDA.14` or external-result branch without a compulsory problem-structuring sequence.
- [ ] For a missing authority, subject, horizon, source or intended use, the account states which result the gap limits.
- [ ] Claims about a later decision, performed work or its effects have the evidence appropriate to each claim.
- [ ] The body supports both a contested-situation entry and development-direction advising without giving either entry a different meaning of engagement or authority.

### PSDA.11:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “First agree what the problem is.” | Preserve materially different formulations and examine which findings, evidence needs or decisions would differ. |
| “The client is the decision maker.” | Separate recipient, holder, choice owner, and authority basis; name any supported coincidence. |
| “Run the workshop and the scope will emerge.” | State the intended return and provisional boundary before choosing the workshop Method. |
| “The model says option A, so that is the decision.” | Keep model result, recommendation, authority, and later `ChoiceResult` separate. |
| “We need every stakeholder before we can start.” | Return a bounded current question and use `PSDA.12` to expose which missing participant or concern can change it. |
| “This is only advice, so authority does not matter.” | State who may prepare, receive, rely on, and choose whenever those differences change use or consequences. |
| “Use PSDA.11 as stage one of every engagement.” | Bypass it when the receiving question and authority boundary are already adequate and another result is the live gap. |

### PSDA.11:9 - Consequences

A bounded question lets the practitioner use what is already known, say what remains open and direct further work to the uncertainty that matters. When a recommendation is requested, its recipient, subject, horizon, authority and intended use are available before the analysis.

Clarifying the use and reopening the boundary take time. An unknown subject, horizon or receiving use can prevent further analysis. Unknown decision authority can limit a recommendation or action while leaving a conditional comparison possible. Evidence of newly affected parties or rival formulations may justify widening the inquiry.

### PSDA.11:10 - Rationale

An engagement boundary gives problem structuring and analysis a shared question. It preserves relevant rival formulations, identifies what to leave outside and gives the practitioner a basis for choosing a Method. A working question can be amended when new evidence changes its scope.

Generic FPF patterns already govern outside-practice results, evidence, permission, agency, and choice. PSDA.11 contributes the field-specific opening that connects a receiving decision or work to a provisional problem-structuring and decision-support boundary, and it tells the practitioner which exact downstream question is now live.

### PSDA.11:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How should a practitioner open an ill-structured or contested decision-support situation? | The best-known line is to bind inquiry to a named receiving use while keeping framing plural, contextual, and revisable before committing to one PSM, model, or formulation. | A fixed sponsor brief or Method-first workshop is the serious default; an unbounded “include everything” inquiry is the opposite default. | Both defaults hide the decision-support return: one naturalizes the first frame, the other cannot stop. **Adapt:** `PSDA.11:4.1`–`4.4`, the flood-pump case, and the first seven checklist rows require a receiving use and provisional boundary, with plural-formulation and local reopening branches where they can change Method choice. | Smith and Shaw's [2019 PSM review](https://doi.org/10.1016/j.ejor.2018.05.003) is a best-known-line candidate for the continuing PSM branch and its differing characteristics; Kogetsidis's [2025 review](https://doi.org/10.1108/IJOA-08-2024-4746) is an application comparator. Kelly and Gero's [2022 framing review](https://doi.org/10.1017/dsj.2022.25), Litster, Cardoso, and Hurst's [2024 systems-mapping study](https://doi.org/10.1017/S089006042400012X), and Nickel, Hurst, and Duimering's [2024 contextual trade-off study](https://doi.org/10.1017/dsj.2024.34) support explicit candidate framing, contextual comparison, and revision. The reviews are non-exhaustive; the studies establish neither one framing ontology, universal Method, shared frame, prevalence, nor superiority. | Reopen if comparative practice shows a lower-effort opening that preserves the same receiving-use, plurality, authority, stop, and revision value, or if a source changes the conditions under which framing must be reopened. |
| How should decision-support advice remain useful without becoming the later choice? | The best-known current FPF line is result-first and authority-bounded: name the receiving decision, reuse or request only the outside-practice result it needs, return the recommendation as a premise, and let the authorized chooser produce the separate `ChoiceResult`. | Expert-report, approval, score, or model-output language treated as the decision is the serious default. | The default transfers authority by format and hides blockers. **Adopt:** `PSDA.11:4.1`, `4.2`, `4.5`, the development-direction case, and the authority checks keep performer, recipient, holder, outside-result owner, and choice owner distinct. | Current `A.15.9` supplies the smallest bounded-result return and supplier/receiver authority split; current `C.11` supplies choice over an already-available option set. Neither pattern bounds a professional problem-structuring and decision-support engagement or selects its next field-specific branch. | Reopen if direct choice or outside-result guidance gains the complete engagement-boundary move at equal or lower effort, or if practitioner use shows that the current separation prevents rather than improves a necessary authorized combined role. |

### PSDA.11:12 - Relations

- `PSDA.12` receives a bounded receiving inquiry when participants, concerns, affected Systems, duties, interests, representation, or dissent can change the return.
- Use `PSDA.1` when materially different problem formulations imply different boundaries, evidence, values, or interventions. Use `PSDA.2` when the scope and the conditions for reopening it need a deliberate decision.
- Use `PSDA.3` for modeling, `PSDA.4` for assessing or combining Methods and `PSDA.13` for facilitation where that contribution is needed. `PSDA.5`, `PSDA.6`, `PSDA.7`, `PSDA.8` and `PSDA.9` address bounded questions about alternatives, values, uncertainty, consequences and robustness.
- Use `PSDA.14` to prepare a recommendation for the intended recipient and identify whose decision it will inform. Use `PSDA.15` when changed premises or later observations raise a question about continuation, adjustment, evidence or reframing.
- `A.15.9` supplies the inspect-reuse-or-request boundary for one outside-practice result. Preserve the direct evidence, provenance, currentness and domain grounds of any claim used. Use `A.10` when its source-to-use account remains implicit or a needed reproducible account is missing.
- `C.11` governs the later choice over an already-available option set. `A.13`, assignment, capability, permission, responsibility, and authority patterns supply the grounds for those claims when the engagement relies on them.
- Both `PSDA-CARD-01` and `PSDA-CARD-02` begin from this same engagement and authority meaning. The entries illustrate different extended uses.

### PSDA.11:End

## PSDA.12 - Recover Participants, Concerns, and Affected Systems for a Decision-Support Inquiry

> **Type:** DPF pattern body
> **Status:** Stable
>
> **Primary working result:** an account of participation and material concerns for a bounded inquiry. Identify who contributed, whom any representative speaks for, which Systems could be affected, and which concerns, duties, interests and disagreements matter. State relevant gaps, uncertainty and conditions for reopening.

### PSDA.12:0 - Use This When

Use this pattern when a bounded decision-support inquiry may be shaped mainly by its loudest, most available, or formally powerful participants, while the situations of other affected parties or Systems, represented and unrepresented, can change the formulation or finding.

Use the bounded engagement question or equivalent evidence of the intended use. Identify possible consequence bearers, using `A.1.CSD` when discovery is needed. Determine which participation conditions and concerns affect the answer. A list or a conversation can supply evidence for its own scope.

Use the account to judge whose circumstances and concerns affect the inquiry. If you only need contacts, routine communication or an organization chart, use the appropriate source directly. Use `A.1.CSD` for a question confined to Systems that may undergo change. Where a question is wholly about representation, law, ethics, safety, conflict or authority, use the relevant practice and evidence.

#### PSDA.12:0.1 - Working Distinctions

| Working term | Meaning in this pattern |
| --- | --- |
| participant | A contributor to the inquiry, or a party whose contribution is sought. Distinguish a requested contribution from one received. Establish representation, agreement, capability and authority where a claim depends on them. |
| affected System | A System or prospective referent that may undergo a relevant change. Identify the supported relation or possible path by which the change could reach it. Use `A.1.CSD` when this discovery is needed. |
| concern | A source-attributed matter that a participant, represented person, duty holder, interest holder, or affected-System account makes material to the receiving use. Identify separately the evidence for its substance, priority or support by others when those claims matter. |
| representation | A supported basis on which one participant speaks, reports, advocates, or acts for another person or constituency. Identify the constituency, the basis and limits of the participant’s remit. |
| participation condition | An access, timing, language, safety, capability, format, dependency, or other condition that changes whether a contribution can be made or relied upon. |
| participation and concern account | The smallest recoverable account of current and missing participation, affected Systems, concerns, duties, interests, dissent, evidence, uncertainty, and next use for one bounded inquiry. |

### PSDA.12:1 - Problem frame

Contested situations rarely present a neutral list of stakeholders. Sponsors, operators, specialists, residents, customers, regulators, future users, and consequence bearers enter through different channels and with unequal time, language, safety, information, and formal power. Some affected Systems cannot participate directly. A person who reports their own experience may lack a representative mandate. Duties or authority may belong to someone other than the person who bears the greatest consequence.

Examine participation and concerns far enough to keep the formulation, model, comparison or recommendation from misleading its recipient. One plausible missing bearer or silenced concern can justify the inquiry. Stronger claims about harm, duty, representation or authority require their own evidence.

### PSDA.12:2 - Problem

A stakeholder list collapses several different questions: who attends, who contributes evidence, who may be affected, who holds a duty or interest, who represents whom, and who decides. The most visible contributors then define the concern set. Non-attendance is read as indifference; a representative's statement is generalized beyond its basis; a possible consequence is reported as an observed one; or a facilitator's synthesis becomes false consensus.

Waiting for every potentially affected participant can also prevent a useful result. Give the supported account with its material absences and what those absences limit.

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

Start with the question and the parties or Systems that could bear its consequences. Establish participation, affected-System status, attributed concerns, representation and decision authority on their respective grounds. Return enough information to support the requested finding or later decision-support work.

#### PSDA.12:4.1 - Bind the account to one inquiry

Use a current `PSDA.11` engagement question or identify the subject, recipient, intended use, horizon and relevant authority directly. Check whether an earlier account fits this inquiry. If the use or engagement is still unclear, use `PSDA.11` to bound it or state what remains undetermined.

Identify whose circumstances, contribution, duty, interest or possible change could affect the answer. Distinguish what is already established from a possible effect and identify the evidence or assumptions supporting each. Affected parties need to participate only when their contribution is required.

#### PSDA.12:4.2 - Discover affected Systems before equating them with participants

Use a suitable account of affected Systems. If the boundary needs investigation, apply the relevant `A.1.CSD` discovery to the focus, configuration, scope, horizon and intended use. Distinguish supported direct relations from possible paths. Identify the bearers, possible changes, relevant evidence, uncertainty and what would reopen the result.

An affected System may be a participant, be represented by a participant, or have no feasible participation channel. Participation can reveal a bearer or path, but it does not prove System construction, a relation occurrence, a consequence, or authority. For a claim that a particular relation held, use the applicable relation criteria and evidence. Open `A.6.REL` only when later work must distinguish this occurrence from another occurrence of the same relation kind, including another episode with the same participants; a readable current relation assertion is otherwise enough.

#### PSDA.12:4.3 - Recover participation positions and conditions

For each material contribution, identify who provided it or whose input was sought, the basis for relying on it, and any channel or condition that affected receipt, protection or use. Identify participation that was needed but unavailable or unsafe.

Establish representation when the finding relies on someone speaking or acting for others. State whom the participant represents, for what question, under which basis, and with what limit. Keep self-report, specialist evidence, advocacy, delegated representation, duty, interest, sponsorship, facilitation, and choice authority distinct.

#### PSDA.12:4.4 - Attribute concerns, duties, interests, and dissent

Record each material concern in ordinary language with its holder or source and what it could change in the answer or in which consequences should be examined.

Establish what the concern is about before joining it to another concern under the same word. Ask what is being done or changed, where that object or work begins and ends, and what would count as the relevant result. Participants saying “the trip is complete” may mean that the remote task is finished, the traveler has returned, or the expense case is closed. Those are different objects with different completion conditions. Recover how they are related and which result each participant needs. In other cases, participants do concern themselves with the same object: duration and cost can describe the same identified journey. Keep that common reference when it fits.

Use this recovery where ambiguity changes the inquiry; identify who or what may bear the consequence and how the bearer relates to the object being discussed. Distinguish the following claims.

- what a participant reports experiencing from evidence about an external event;
- duty from preference or interest;
- individual concern from a represented constituency claim;
- disagreement from an unresolved factual question; and
- absence of evidence from evidence of absence.

Keep minority and unresolved positions visible. Facilitation can make a contribution intelligible. Establish any claim of consensus, truth, priority, permission or authority on its own grounds.

#### PSDA.12:4.5 - Return the smallest explicit account

| Result position | Required content |
| --- | --- |
| Bounded inquiry | Subject, receiving use, horizon, recipient and, where a decision is involved, its holder. |
| current participation | Participants, contribution bases, channels, and material participation conditions. |
| consequence bearers | Actual Systems or intended referents, supported relations or modal paths, possible changes, evidence, and uncertainty. |
| concerns and positions | Attributed concerns, duties, interests, agreements, dissent, and unresolved questions; the objects and relations needed to understand materially ambiguous terms. |
| Representation | The grounds and scope of any representative claim on which the account relies. Identify a missing mandate when representation is required. |
| material absences | Missing participants, bearers, concerns, channels, or assurance that can change the inquiry. |
| Use and reopening | What finding, formulation, decision or other work the account supports, and what evidence or change would warrant reconsidering it. |

Finish when the account is adequate for its intended use. If a missing contribution could materially affect the finding, state the gap and its reach. Use an appropriate source, ask for a necessary contribution, narrow the claim or withhold it according to what remains possible.

#### PSDA.12:4.6 - Use the account without making it decide

Use the account where its contents matter. Different concerns can inform `PSDA.1`, scope questions `PSDA.2`, participation conditions `PSDA.13`, value inputs `PSDA.6` and interference between inquiries `PSDA.17`. Developing a formulation, choosing a priority or making a decision requires the relevant further work.

Reopen locally when a new bearer, consequence path, participant, concern, duty, interest, representation basis, dissent, participation condition, receiving use, horizon, or authority relation can change a dependent result.

#### PSDA.12:4.7 - What changes in practice

The practitioner can report who participated, who or what could be affected, which concerns each source supports and what remains unknown. State the consequences of a material absence for the answer or any further work that relies on it.

### PSDA.12:5 - Archetypal Grounding

#### PSDA.12:5.1 - Flood-pump participation and concern account

For the emergency investment board's pre-season pump decision, the team begins with the `PSDA.11` engagement. Operations and finance staff are available, but district residents, emergency responders, maintenance contractors, downstream ecology staff, and people with limited mobility may bear different consequences.

An `A.1.CSD` pass distinguishes observed basement flooding and pump downtime from possible displacement, access failure, downstream transfer, and ecological change. The team attributes each resident contribution by district and channel and checks the scope of the association’s mandate before speaking of wider representation. Emergency responders hold operational knowledge and duties but do not thereby own the investment choice. A no-new-purchase concern remains visible beside capacity, equity, maintenance, safety, and environmental concerns.

The returned account names inaccessible evening meetings and missing mobility-service evidence as participation gaps. It is adequate to open `PSDA.1`, because the recovered concerns support materially different formulations. It does not declare consensus or recommend a pump.

#### PSDA.12:5.2 - Affected System without a speaking participant

A service redesign may change response time for a machine-supported monitoring arrangement and for patients who cannot participate directly. The arrangement and patients can enter the affected-System account through supported paths even when no direct participant is available. A clinician, advocate, or family member contributes only under the stated evidence or representation basis. Identify the evidence that supports each possible effect. Report a representation gap if answering the question requires someone to speak for absent parties and that basis is missing.

#### PSDA.12:5.3 - Cheap non-use

A current, low-consequence internal choice has one authorized team, one directly affected workcell, an already-supported consequence account, no representation question, and no material dissent. The live question is comparison among three qualified settings. Repeating PSDA.12 adds no value; use the comparison or choice pattern directly.

#### PSDA.12:5.4 - A completed trip with an unfinished task

A sponsor asks why business trips are failing. An employee has returned from a site visit, and administration has closed the expense case, but the equipment fault the employee was sent to repair remains unresolved. “Trip completed” therefore gives three different answers: journey complete, administrative case complete, remote repair incomplete.

The inquiry identifies the repair work and its intended result, the journey that enabled the visit, and the administrative provision and records. It examines how those activities connect. Timely travel and site access may enable the repair, while closing an expense case does not settle whether the repair is complete. The first result is a corrected question: what prevents completion of the remote repair, and which travel or administrative conditions contribute to that difficulty? Faster expense processing may be useful, but its completion cannot answer the repair question.

For an unlike case, “access granted” can mean that permission was issued while the account is still unable to open the needed system. Distinguish the issued permission, configured access and ability to use it. To report a completed use or failed attempt, check what happened. Conversely, an employee and administrator discussing the duration and reimbursable cost of the same identified journey can retain one common object with different concerns.

### PSDA.12:6 - Bias-Annotation

**Scope:** participation and concern recovery for one bounded decision-support inquiry. **Lenses:** **Gov** keeps contribution, representation, duty, and choice authority distinct; **Arch** tracks which participants and concerns can change dependent results; **Onto/Epist** separates Systems, reports, possible paths, and supported relations; **Prag** stops at a sufficient account; **Did** supplies plain recognition cues and an explicit assurance boundary.

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| visibility bias | Available or powerful speakers define the concern set. | Start from possible consequence bearers and record material absences. |
| attendance-as-representation bias | Presence or title is treated as authority to speak for others. | For a claim on behalf of others, establish the mandate, constituency and limits. |
| participation-as-proof bias | A workshop report is treated as proof of Systemhood, consequence, or consensus. | Keep participation, relation, evidence, and agreement claims distinct. |
| stakeholder-exhaustion bias | Work waits for universal participation. | Stop at adequacy for the named use and return exact gaps. |
| harmony bias | Facilitation erases minority or unresolved positions. | Preserve attributed dissent and its consequence for the next result. |
| human-only bias | Non-speaking or non-human consequence bearers disappear. | Use `A.1.CSD` to recover affected Systems and possible changes. |

### PSDA.12:7 - Conformance Checklist

- [ ] The account is bound to one receiving inquiry, subject, horizon, and authority boundary.
- [ ] The account distinguishes participants, affected Systems, represented parties, duty or interest holders and any holder of a decision relevant to the inquiry.
- [ ] Actual relations, modal paths, observed changes, and possible consequences remain distinguishable.
- [ ] The account attributes material concerns. Any finding about their substance, priority, agreement or authority has its own grounds.
- [ ] Any relied-upon representation and participation condition is supported and scoped.
- [ ] A material missing contribution or assurance is identified together with the result it limits or the evidence still needed.
- [ ] The stopping rule is adequacy for a named next use rather than exhaustive recruitment.
- [ ] Recognition is cheap, while legal, ethical, safety, harm, duty, representation, and authority claims retain their direct assurance.
- [ ] The account states what work its findings support and the grounds for any further decision.

### PSDA.12:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “The stakeholder register is complete.” | Ask which plausible consequence bearer or participation condition could change the receiving use. |
| “Everyone agreed in the workshop.” | Preserve who expressed what, under which channel and limits; establish consensus only through its direct basis. |
| “The community representative speaks for residents.” | Establish whom the representative can speak for and about what, any material dissent, and any remaining limit. |
| “Affected means invited.” | Discover consequence bearers independently of participation. |
| “Every concern becomes a criterion.” | Establish what each concern bears on. Use the relevant formulation or value method if the task calls for a criterion. |
| “No one mentioned it, so it is irrelevant.” | Distinguish missing evidence or access from supported non-materiality. |

### PSDA.12:9 - Consequences

Problem formulations and later recommendations gain a recoverable social and consequence basis. Quiet, represented, missing, and non-speaking bearers remain visible without requiring impossible universal participation. The cost is explicit attribution and occasional stopping when representation, access, or consequence evidence is inadequate.

### PSDA.12:10 - Rationale

Use `A.1.CSD` to find who or what could be affected, distinguishing a supported relation from a possible path. For the inquiry, establish how contributions were made, what the material statements concern, whose interests or duties they bear on, any mandate for representation and any disagreement. This can distinguish an unfinished repair from a completed trip or show that cost and duration describe the same trip.

### PSDA.12:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How should participation be recovered in an ill-structured decision-support situation? | The continuing PSM branch, including facilitated modeling and multi-method arrangements documented for ill-structured situations. | A sponsor-built stakeholder list or open workshop is the serious default; universal recruitment is the opposite default. | A sponsor's list can hide consequential absence, while universal recruitment supplies no usable stop. **Adapt:** `PSDA.12:4.1`–`4.5` returns a use-bounded participation and concern account whose omissions and dissent remain visible. | Smith and Shaw's [2019 PSM review](https://doi.org/10.1016/j.ejor.2018.05.003) and Kogetsidis's [2025 review](https://doi.org/10.1108/IJOA-08-2024-4746) support the continuing branch, differing Methods, and documented facilitated or multi-method use. They do not establish representativeness, universal facilitation sufficiency, or comparative superiority. Use the evidence for attribution, representation limits and material absences to bound the findings about participation. Current `A.1.CSD` separately supplies consequence-bearer discovery. The resulting combined PSDA rule is an adaptation, not an externally demonstrated best participation protocol. | Reopen if newer comparative evidence changes the conditions under which facilitated participation is adequate, the direct FPF contribution changes, or a material bearer or participation condition is discovered. |
| How should affected Systems enter without turning participation into proof? | Use current `A.1.CSD` to recover actual Systems or intended referents, direct relations or modal paths, possible changed characteristics, evidence, uncertainty, and receiver connection; then use PSDA.12 only for the participation-specific account. | Attendance, complaint volume, or generic impact language is the serious default. | It confuses reports, bearers, paths, changes, and authority. **Adopt:** `PSDA.12:4.2` and the non-speaking-bearer case keep those claims separate. | Current `A.1.CSD` is the direct FPF source for affected-System consequence discovery. Each obtaining claim remains with its direct relation pattern; `A.6.REL` adds occurrence identity only when later use must distinguish occurrences of the same relation kind. These contributions do not recruit participants, establish representation, facilitate inquiry, or rank concerns. Domain safety, legal, ethical, and scientific practices retain their own Methods and thresholds. | Reopen if the direct patterns acquire the full participation-and-concern move at equal or lower effort, or if evidence changes a relied-upon bearer, path, or consequence. |

### PSDA.12:12 - Relations

- A compatible `PSDA.11` result or the established engagement terms can supply the subject, use, horizon, recipient and relevant authority. Clarify a missing or outdated condition when it limits the inquiry.
- `A.1.CSD` supplies affected-System consequence discovery. The relevant direct relation pattern governs each obtaining claim; `A.6.REL` applies only when the receiving use must distinguish occurrences of the same relation kind.
- Material differences among concerns can inform problem formulations under `PSDA.1` or an assessment of scope under `PSDA.2`.
- Use the participation conditions for a facilitation question under `PSDA.13`, attributed values under `PSDA.6`, and evidence about interference between inquiries under `PSDA.17`, where the receiving task needs that contribution.
- Direct governance, conflict, representation, legal, ethical, safety, evidence, assignment, and authority patterns govern those claims. PSDA.12 neither replaces them nor authorizes the later choice.

### PSDA.12:End

## PSDA.13 - Facilitate Decision-Support Inquiry and Preserve Material Dissent

> **Type:** DPF pattern body
> **Status:** Stable
>
> **Primary working result:** an attributed account of what participants understand, support, reject or leave unresolved. State the evidence, the consequences for the receiving question and what would reopen a material difference.

### PSDA.13:1 - Problem frame

**Use this when** participants need to work on a decision-support question but disagree about its meaning, evidence, consequences, or acceptable action. Also use it when a smooth workshop is producing an apparently unanimous answer that participants cannot recognize as their own.

Establish the purpose of the inquiry, the conditions for contributing and challenging, and any boundary on a later choice. Help participants express claims in meanings they recognize. Return the common ground and material disagreement that the evidence supports.

Facilitation enables inquiry. The result is an account of shared or contested claims. Distinguish using the same words, understanding one another, endorsing a claim, consenting to an action and holding authority for a decision.

When no inquiry is needed, circulate the established fact from its qualified source, record who attended using the available evidence, or apply the decision rule within the appropriate mandate. Mediation, adjudication, safeguarding and emergency command require their respective mandates and capabilities. State a missing receiving question or any missing decision authority that limits the intended use.

### PSDA.13:2 - Problem

Facilitation can suppress the differences it is meant to make usable. A participant's objection becomes a neutral-looking label, an absent group is treated as represented, and silence is recorded as consent. A model becomes “our view” although participants attach different meanings to it.

The opposite failure is endless disagreement. Every difference reopens the whole discussion, no one distinguishes an evidence gap from a value conflict, and the recipient receives a transcript instead of a result. Return the differences that matter for the intended use and the limits they place on the answer.

### PSDA.13:3 - Forces

| Force | Tension |
| --- | --- |
| Participation | The inquiry needs relevant voices, while access, language, hierarchy, time, and safety can limit meaningful contribution. |
| Common ground | Shared understanding can support joint work, while common wording can conceal opposed claims. |
| Challenge | Claims should be open to examination, while criticism can be socially costly or become personal conflict. |
| Closure | A usable return is needed, while unresolved dissent may materially constrain it. |
| Attribution | Readers need to know whose claim is carried, while confidentiality and representation limits constrain disclosure. |

### PSDA.13:4 - Solution

Use workable conditions for participants to express, understand, challenge and revise claims, arranging missing conditions where needed. Distinguish what could resolve a factual question, a difference of meaning or a value dispute. Attribute agreement and disagreement to the participants’ expressed positions. Use the relevant evidence for factual claims and identify any remaining uncertainty.

#### PSDA.13:4.1 - Recover the inquiry, participation, and Method conditions

Identify the participants, affected Systems, concerns, representation limits and missing views relevant to this inquiry. A compatible `PSDA.12` account can supply them. Reuse a `PSDA.4` assessment where its Method and limits fit the situation and qualification window.

Recover the receiving question, intended result, and any boundary on a later choice from the current engagement terms or another qualified direct source. Make clear what this interaction can establish and what remains with the decision owner or a direct specialist.

If an input needed for the result is missing, stale, or incompatible, use a qualified source or name the gap and what it prevents. Do not infer consent, representation, permission, or authority from a participant list, a concern map, or a Method description. An affected System need not have a person present who is entitled or able to represent all its concerns.

#### PSDA.13:4.2 - Establish workable participation and challenge conditions

For new participation, tell contributors what is being asked, how their input will be used and attributed, how they can challenge or correct it, and who will receive it. Use channels suitable for the participants, such as a joint session, a written response or a separate conversation. Check that the channel and format are accessible. For a completed exchange, establish what conditions applied.

Make the facilitator's remit and material interests visible. If the facilitator also owns a preferred intervention or controls participants' opportunities, choose safeguards appropriate to that conflict, such as independent handling of a contested claim or a different facilitator. Judge the facilitator’s position from those interests and powers.

Identify the applicable rules for consent, participation, confidentiality and any later decision. Use the governing source and establish what conditions participants can use. Seek a participant’s account where the judgement depends on their experience or response. Acceptance of a format concerns participation; endorsement of a finding requires evidence of that endorsement. If participation creates a material risk of harm or coercion, use a protected route, seek competent support, narrow the claim or stop that part of the inquiry.

#### PSDA.13:4.3 - Elicit and test meaning before merging claims

Recover concrete, attributable claims: what happened or could happen, to whom, under which conditions, why it matters and what might change the position. Use a suitable existing statement or ask the participant where the account is missing or ambiguous. In a new exchange, give the holder a workable opportunity to correct how their claim is represented. Where useful, compare another participant’s restatement with the holder’s response.

Separate observations, reported experience, causal hypotheses, preferences, duties, proposed actions, and commitments. A participant may agree that a claim was represented accurately while disagreeing that it is true or desirable. Keep those answers distinct.

Use a model or shared display when it helps the participants examine a question. A new connection or translation remains a proposal until its meaning and evidence are established. If two participants use “reliable service” differently, retain the two meanings instead of selecting a single label for convenience.

#### PSDA.13:4.4 - Turn material disagreement into a usable inquiry result

A disagreement is material when it can change a formulation, candidate intervention, consequence claim, value treatment, recommendation, implementation condition, or legitimate receiving use. Preserve at least the disputed claim, its attributed positions, why the difference matters, the current basis, and what evidence or changed condition could alter the finding or its use.

| Difference | Useful facilitation move | Honest remaining result |
| --- | --- | --- |
| Different meanings or scopes. | Recover examples and conditions; test a paraphrase or explicit distinction. | A repaired meaning or two still-distinct readings. |
| Different factual or causal claims. | Identify the evidence, assumption, or discriminating observation required. | A qualified claim, unresolved evidence question, or bounded contradiction. |
| Different values, interests, or priorities. | Make the consequence and trade-off explicit without pretending it is a missing measurement. | Attributed value positions for the later value or choice question. |
| Disputed right, duty, representation, or choice authority. | Use the applicable rule or ruling. Seek a decision where required, or state the missing authority. | A supported boundary, exact authority gap, or stop on the disputed use. |
| Different willingness to endorse or commit. | Identify which statement or undertaking each participant supports, on what evidence and conditions. Ask them when a needed position remains unclear. | Bounded support, dissent, abstention, or a separately established commitment. |

An objection is neither an automatic veto nor something to erase by a majority count. Its effect follows from the substance of the claim and applicable decision rule. A vote can establish its own result when authorized; it does not settle truth, all participants' consent, or the legitimacy of an unsupported trade-off.

Return material disagreements with their conditions when the intended use can accommodate them. If a missing premise prevents that use, identify it and narrow the conclusion accordingly.

#### PSDA.13:4.5 - Keep the result faithful without collecting everything

Preserve enough attribution and evidence for the recipient to understand each material claim and how it could be challenged. Retain the scope of representation: “the association's representatives stated” is different from “residents agreed”. Where a protected contribution cannot be openly attributed, preserve its qualified status and disclosure limit without inventing public endorsement.

Use the least detail that supports the inquiry, such as a concise account of claims, a corrected map or annotated conclusions. Collect personal details only when needed for the receiving question and permitted for that use. Describe the confidentiality or anonymity the arrangement can provide.

If later reliance requires a claim that consent, authorization, representation, or another relation obtains, use that relation's direct pattern and evidence. Use `A.6.REL` only when the receiving use must additionally distinguish occurrences of the same relation kind, including separate episodes with the same participants.

#### PSDA.13:4.6 - Close with shared and contested claims

When attribution or the meaning of a proposed return needs confirmation, give the relevant participants an accessible way to inspect and correct it. Use an applicable earlier confirmation when it already covers the wording and conditions. Include a later correction when it materially changes the account and identify affected uses. If confirmation remains unavailable, state the limit on attribution.

The recipient should be able to distinguish:

- shared understanding of a statement from support for that statement;
- supported common claims from conditional claims, unresolved evidence, and dissent;
- participants who responded from absent, unreachable, unrepresented, or declining participants;
- proposed action from commitment or authorization; and
- what the inquiry enables now from the direct result still needed.

Use `A.2.9` when the live question is whether the communication enabled a named recipient to understand or do something and what smallest repair is needed. An acknowledgement or later action is not sufficient proof of understanding, consent, or causal effect. Add exact communicative-Work detail only when that stronger reliance is needed.

Return the supported common claims, material disagreements and evidence gaps, with their consequences for the question. Identify a discriminating question or reopening condition when needed. The account may inform alternative generation, a recommendation or reconciliation between inquiries. A resulting decision has its own authority and evidence.

#### PSDA.13:4.7 - What changes in practice

Participants can see how their claims were represented when the disclosure terms permit it. The recipient can distinguish common ground, disagreement and uncertainty, including the limits of the group’s authority.

### PSDA.13:5 - Archetypal Grounding

#### PSDA.13:5.1 - A flood-pump return that retains disagreement

In this illustrative inquiry, the board's current engagement terms reserve the investment choice to the board. The participation account distinguishes the residents' association from a separately consulted group of mobility-constrained residents; neither represents all district residents. Operations staff supply their current technical assumptions, while the selected Method calls for attributed service claims and conditional technical analysis.

The facilitator presents three proposed conclusions and obtains these corrections:

| Proposed conclusion | What inquiry establishes | Returned claim |
| --- | --- | --- |
| “The pumps can protect the district.” | The technical calculation concerns nominal capacity under stated inflow and availability assumptions. It does not establish deployment access or every resident's protection. | The conditional capacity claim is shared by the responding participants; the broader protection claim is unsupported. |
| “Residents want the least expensive pumping option.” | Association representatives emphasize property protection and cost. The separately heard group asks how assistance remains reachable when roads fail. No complete cost comparison or district-wide endorsement is available. | Preserve the two attributed service concerns; do not claim a common preference or a chosen option. |
| “The mobile branch is acceptable if capacity is sufficient.” | Operations staff cannot yet support its arrival-time premise under the road-loss condition. The mobility concern remains material even if nominal capacity is adequate. | Keep the branch conditional on access evidence and retain the service disagreement for alternatives and recommendation. |

The board receives a shared conditional reading of nominal capacity, the unresolved access premise for the mobile branch, and the separately attributed concerns about property protection and reachable assistance. Endorsement of an investment and the board’s commitment remain separate from these findings.

The facilitator sends the wording back through the available channels for attribution correction. Where no reply is available, leave the requested confirmation open. A later verified access result can close that technical question without resolving the value difference; a participant's corrected service meaning reopens only the affected claim and its downstream use.

#### PSDA.13:5.2 - A manager's summary is not a team's consent

A manager proposes a development direction and asks staff to comment in a meeting where dissent could affect their assignments. The silence establishes neither support nor opposition. Any claim about staff positions needs evidence of those positions.

The facilitator offers a protected response route or a separately facilitated discussion and states its disclosure limits. Include any applicable, appropriately obtained prior statements. If no usable staff contribution is available, report the manager’s proposal and the limit on staff input. Obtain qualified safeguarding support where it is needed.

#### PSDA.13:5.3 - Cheap non-use

Two analysts have agreed on a corrected unit conversion and need the value in their calculation note. Supply the qualified correction for that use. Check receipt or interpretation where the receiving work requires it.

### PSDA.13:6 - Bias-Annotation

**Scope:** facilitated inquiry that supports a bounded receiving inquiry and any subsequent decision. **Lenses:** **Gov** separates participation, representation, consent, and choice; **Onto/Epist** separates claim meaning, support, evidence, and occurrence; **Prag** seeks usable closure; **Arch** preserves dependencies on unresolved claims; **Did** makes contested meanings recognizable.

Consensus bias treats a quiet room as a successful outcome. Sponsor bias gives one formulation privileged status. Attribution bias extends one representative's statement to a population. Conflict-avoidance bias weakens an objection until it no longer changes the result. Counter these by checking what supports each attribution, seeking clarification where it is needed and preserving the consequences of material disagreement.

### PSDA.13:7 - Conformance Checklist

- [ ] The inquiry's receiving question, intended result, and any applicable boundary on later choice are recoverable.
- [ ] Needed participation and Method inputs fit the present situation and qualification window, or their exact gaps are returned.
- [ ] Participation, correction, challenge, attribution, and disclosure conditions are usable rather than merely announced.
- [ ] The facilitator's material interests and limits are visible.
- [ ] Shared meaning, claim support, factual evidence, value preference, consent, and authority remain distinct.
- [ ] Material dissent retains attribution, basis, consequence, and a discriminating question or reopen condition.
- [ ] The account distinguishes absence, silence, abstention, representation limits and an expressed position on the claim.
- [ ] Direct relation claims receive their own assurance; an occurrence register is not compulsory.
- [ ] The return is concise enough to use and precise enough for participants to challenge.
- [ ] Any reported decision has its own basis. A missing premise and the use it limits are stated.

### PSDA.13:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Everyone agreed with the slide.” | Check which meaning and claim each response supports. |
| “No objection means consent.” | Recover the participation conditions and any applicable consent rule; apply that rule to the observed response and state any consent still unestablished. |
| “The representative speaks for everyone affected.” | Carry the representation basis and limits. |
| “Keep dissent in the transcript; simplify the recommendation.” | Preserve every disagreement that can change the requested finding, recommendation or conditions of use. |
| “Every objection blocks progress.” | Distinguish its consequence under the applicable evidence, authority and decision rules. |
| “A neutral script makes the facilitator neutral.” | Expose material interests and choose an appropriate safeguard or facilitator. |

### PSDA.13:9 - Consequences

The receiving practitioner obtains usable common ground without losing material disagreements and what they change in the finding or its use. Evidence questions, value conflicts, and authority gaps can take different next routes. The cost is explicit correction and dissent handling, and sometimes a narrower return when meaningful participation is unavailable.

### PSDA.13:10 - Rationale

Facilitation lets participants examine claims and their differences. Closure is useful when the recipient can see which claims the evidence supports, how unresolved disagreements affect the answer and where relying on it would require another result.

### PSDA.13:11 - SoTA-Echoing

| Practice question | Best-known line | Serious alternative or default | Defect overcome and pattern mutation | Source roles and limits | Reopen condition |
| --- | --- | --- | --- | --- | --- |
| How can facilitation make different meanings usable? | Examine the interaction: elicit concrete contributions, test formulations with participants, and revisit how the developing model carries their meanings. | Following a workshop script or completing a shared diagram is treated as sufficient evidence of common understanding. | **Adapt:** `PSDA.13:4.2`–`4.3` and `4.6` add targeted meaning and attribution checks within the same interaction. The extra attention is accepted for a material difference, without requiring a full recording or research study. | Franco and Greiffenhagen's [2018 facilitated-modeling analysis](https://doi.org/10.1016/j.ejor.2017.08.016) supplies a bounded empirical account of situated OR practice, not a universal script. Zimmermann and Curran's [2023 microlevel study](https://doi.org/10.1002/sdr.1743) supplies the more specific candidate line on facilitator questions, references to contributions, and recursive development of shared meaning in one heritage-science workshop. Neither establishes universal transfer, consensus, or causal effectiveness for every engagement. | Reopen when participants cannot recognize the returned meaning, the channel suppresses material contributions, or stronger comparative practice supplies the same fidelity with less effort. |
| How should inquiry close when disagreement remains? | Return attributed common claims, material dissent, and the exact missing evidence or authority result. | A unanimous summary is manufactured, or all disagreement postpones every useful return. | **Adapt:** `PSDA.13:4.4`–`4.6` and both substantive cases separate meaning, support, truth, consent, and choice. This accepts a less simple summary in exchange for preserving a difference that matters to the finding or its use; an already-clear factual correction takes the cheap exit. | Current `A.2.9` supplies receiving-use judgement and the distinction between communication, response, achievement, consent, and authority. Current `A.6.REL` supplies occurrence distinction only when needed; direct predicates and evidence establish obtaining relations. Retaining material dissent is the PSDA solution constraint for contested decision support, not an empirical claim that disagreement always improves decisions or grants a veto. | Reopen when a direct rule changes the effect of dissent, new evidence resolves a disputed claim, attribution is corrected, or the receiving use can no longer preserve the unresolved difference honestly. |

### PSDA.13:12 - Relations

- A compatible `PSDA.12` account can supply participation and concern findings. `PSDA.4` can supply an assessed Method and its limits under the applicable conditions. Use another qualified source or state the remaining gap where a needed input is missing.
- Use this inquiry result with `PSDA.5` where it changes the candidate set; agreement is not required and material dissent stays explicit.
- Use the participation and dissent account with `PSDA.14` or `PSDA.17`, when needed, to preserve material agreement and disagreement in a recommendation or simultaneous-inquiry decision. The account grants no choice authority.
- `A.2.9` governs a communication's receiving-use question and any stronger communicative-Work claim. Direct patterns govern claims about consent, representation, permission, duty, and authority; `A.6.REL` adds occurrence identity only for a need to distinguish same-kind occurrences.
- Direct evidence, causal, value, legal, safety, safeguarding, and governance practices answer their own substantive questions. Facilitation can expose their missing results but cannot replace them.

### PSDA.13:End

## PSDA.14 - Prepare and Return a Decision-Support Recommendation

> **Type:** Method pattern (DPF)
> **Status:** Stable
>
> **Primary working result:** a recommendation for an identified recipient, subject, horizon and use. Give the supported answer, alternatives considered, reasons, important limits, dissent, protected conditions and grounds for reconsideration. Identify the authority for any later choice.

### PSDA.14:1 - Problem frame

**Use this when** analysis is available, or its decisive gap is known, but the recipient still cannot tell what the decision-support performer recommends and on what conditions. Determine how the score, agreement or specialist result bears on the recipient’s question. If it already supplies adequate advice, use it directly. The same need arises in an ordinary, non-contested request: “Which development direction should we consider over the next four months?”

Start with the receiving question and the strongest answer the available basis permits. Return a supported direction, retained or ranked set, bounded probe, smallest-result request, blocker or abstention. State the partial order or the missing premise when it limits the advice.

Use this branch of problem structuring and decision support to compose advice from qualified premises and return it to the intended recipient. The later choice belongs to its authorized holder. Specialist findings, implementation and any causal effect each require their own grounds.

The recipient can distinguish what is recommended now, why, what remains unresolved, what must not be traded away, and what evidence would change the answer. A complete result can be two sentences when they identify one missing premise and the exact recommendation it prevents.

Reuse an adequate recommendation. For a request confined to one specialist result, provide that result, and for a choice on an adequate basis use the applicable decision procedure. If a development opportunity or the engagement question is unclear, identify what is missing. Construct the opportunity or use `PSDA.11` to clarify the scope where that work is needed. Use facilitation when a material formulation, participation or dissent question calls for it.

### PSDA.14:2 - Problem

A recommendation often becomes stronger while it travels. “This option performs better in this model” becomes “the best option”; “the group did not object” becomes “stakeholders agreed”; “the report was received” becomes “the decision was approved.” The lost conditions are precisely those the receiving decision needs.

Development advice adds a second failure. A plausible story can combine human learning, organization change and AI evaluation as if they supplied interchangeable evidence. A course catalogue then stands in for transfer into later Work, a position description for a whole-arrangement comparison, or a benchmark score for deployment safety.

Determine which conclusion the premises support for this recipient, which alternatives remain live, and whether obtaining missing evidence would be worth its burden. Where the grounds for advice fail, identify the reason for withholding it.

### PSDA.14:3 - Forces

| Force | Tension |
| --- | --- |
| Usable direction and warranted strength | The recipient needs an actionable answer; incomplete preferences or evidence may justify only a retained set or bounded question. |
| Synthesis and supplier ownership | Several results must become one account without absorbing their Methods, evidence limits or authority. |
| Clarity and material plurality | A short return is easier to use, but omitted dissent or an omitted alternative can reverse its meaning. |
| Timeliness and protected conditions | Delay has consequences, but urgency does not convert missing permission, consent or safety evidence into an admissible premise. |
| Professional judgement and recipient choice | An adviser should give reasons for the advice while attributing values and commitments to the parties who supplied or authorized them. |
| Continuity and changed conditions | An earlier recommendation may remain useful in part even when one configuration, source or assumption changes. |

### PSDA.14:4 - Solution

Compose the advice for the agreed use. Check the strength and scope of each premise on which the recommendation depends. Existing results may meet several needs at once.

#### PSDA.14:4.1 - Recover the receiving use and the right to provide this advice

Identify who needs the advice, the subject, horizon and question, and the decision or other work it informs. If a choice is involved, establish its holder and authority. The receiver may hold that authority, give advice to someone else or use the result for other work.

Use an adequate `PSDA.11` engagement result for the same subject and receiving use. Otherwise obtain the qualified direct facts or return the exact missing recipient, question, scope or authority premise.

In a development-direction advising engagement, establish who recommends a course to whom. A single organization may contain both performers. Distinguish a client, sponsor, person or other system whose development is at issue, recipient or chooser when the difference affects the advice, disclosure or decision. A participant conducting its own analysis may also hold the decision. Naming two roles for that participant does not establish that a distinct adviser supplied a recommendation. Use direct domain or `C.11` guidance when the task is to choose.

Establish applicable professional scope, competence, material conflicts and permitted reliance before offering positive advice. For example, management-consultancy engagement and conflict conditions are informed by the [ICMCI competence framework v4.0, C.1.1–2, C.2.1 and E.3.5](https://www.cmc-global.org/sites/default/files/public/icmci_cmc002_competence_framework_version_4.0_1.pdf). Human career-service consent and assessment limits come from the applicable professional source, such as the [NCDA 2024 Code of Ethics, A.2 and E.2](https://www.ncda.org/aws/NCDA/asset_manager/get_file/3395). These are different service conditions, not one universal profession or evidence that a proposed intervention works.

If a material mandate, competence, conflict or admissibility condition cannot be satisfied, return the scoped blocker or appropriate referral. Existing emergency, safety or legal response duties retain their own direct authority and must not wait for completion of a PSDA account.

#### PSDA.14:4.2 - Recover what the available premises support

For every premise that can change the disposition, recover its claim, exact subject and configuration, source or supplier, applicable window, intended use, uncertainty and reliance limit. Inspect available results first. Use `A.15.9` to reuse an adequate result, retain its useful limit, or select a worthwhile obtainable missing contribution; use `A.10` when the source-to-use account remains implicit or a needed reproducible account is missing.

Read a comparison as a result over particular alternatives under particular values, evidence and assumptions. A `PSDA.9` robustness result contributes where it can affect the advice or its grounds for the same configuration and horizon. It neither entails the whole recommendation nor authorizes the later decision. Preserve the `PSDA.6`, `PSDA.7`, `PSDA.8` comparison basis needed to interpret it.

Keep the live set and the compared subset explicit. A result about internal development and one mixed human–AI arrangement does not dispose of an external provider or a materially different probe. A gap about one candidate can prevent ranking that candidate while leaving an independent comparison usable. State any exclusion and the grounds for it.

Preserve material agreement, disagreement and affected-party concerns from `PSDA.13` or a qualified direct account. Distinguish a factual objection, a value conflict, an authority condition and a question about representation; they call for different responses. Give the objection and its consequence enough prominence to survive the return. Attribution and disclosure must respect the applicable protection and confidentiality conditions.

For advice that depends on a development opportunity, use a qualified account of the problem or promise, its dependencies, what is attainable and what remains uncertain. If specification or search for the opportunity remains necessary, obtain that result or state which advice is still open.

#### PSDA.14:4.3 - Select the warranted recommendation disposition

Use the question, the options still under consideration, their established or unresolved feasibility, protected conditions, the comparison and the cost of delay to determine what you can recommend now. Explain the grounds for each part of the advice. The table gives possible returns.

| Disposition | Positive basis and useful return | Boundary |
| --- | --- | --- |
| Retained or ranked set | Several directions remain live. Return the warranted order, partial order or trade-offs and any unresolved distinction that could narrow it. | A retained set is not consensus; an order valid under one scheme is not a universal ranking. |
| Supported direction | Qualified premises and a declared decision-support rule justify preferring one direction for this use. State the advantage and the conditions under which it holds. | Give the disposition of other candidates considered. Protected conditions cannot disappear into a compensating score. |
| Bounded information-gaining probe | A specified uncertainty could change the advice, and a qualified probe is feasible and proportionate to the delay, burden and risk it introduces. Name the question, bounded exposure, useful evidence and stop. | Thin evidence alone does not justify a probe. The probe's authorization, WorkPlan and execution remain separate. |
| Smallest-result request or handoff | A qualified contributor can supply a missing comparison, feasibility, interpretation, or other result whose obtainable contribution warrants the full formulation, qualification, delivery, performance, interpretation, delay, and displaced work for this receiving question. Use A.15.9 and C.11.DUA for that selection. | Request the bounded premise; the supplier keeps its Method and does not take over the recommendation or choice. A missing premise alone can remain a limitation. |
| Blocker | A missing, stale, incompatible, inadmissible or unauthorized premise prevents the requested responsible recommendation. Name the premise, affected use and what would resolve it or where it could be directed, if known. | State any still-usable partial result; do not convert uncertainty into either a confident negative or a positive recommendation. |
| Abstention | The recommendation premise itself fails, or the requested kind of advice cannot responsibly be supplied within the engagement. State the failed premise and the correct receiving account where one exists. | An abstention is not an adverse factual finding about the subject and is not abandonment of any obtaining professional duty. |

A mixed answer can be useful if its scopes are unmistakable: retain two directions and block a stronger ranking, with a comparison request only when selected for its attainable value. State what each part of the answer covers.

The strength of each claim stays inside the narrowest material limit of the premises on which **that claim** depends. If one input supports only a particular AI configuration, the recommendation cannot silently extend it to another. If an unused source expires, it does not invalidate unrelated claims merely by appearing in the same bibliography.

When a total order is unwarranted, prefer an explicit partial answer to invented weights or probabilities. When the declared scheme does support one direction, do not conceal that conclusion behind an uninformative list. Where a serious alternative is less suitable, explain the reason and the conditions that could alter the judgement.

#### PSDA.14:4.4 - Make the recommendation account inspectable at the smallest useful size

Choose a form the recipient can use. A short message may suffice. A protected annex can carry evidence for a consequential institutional matter. Keep the following information recoverable wherever it affects reliance.

| Position | Decision-useful content |
| --- | --- |
| Receiving frame | Recipient, recommending performer, holder or subject, question, horizon, intended use and, for a decision, its holder and authority. |
| Candidate domain | Considered alternatives, compared subset, exclusions with their basis, retained alternatives and any candidate gap. |
| Relied-on premises | Exact results and relevant source editions or dates, configurations, qualification windows, evidence limits and supplying owners. |
| Comparison and inference | Scheme, material trade-offs, protected conditions, robust regions or reversals, and the reasoning that supports the disposition. |
| Unresolved content | Material uncertainty, dissent, evidence losses, unsupported extensions and what each prevents. |
| Return | One or more explicitly scoped dispositions and the next consideration, request, reroute or separately governed choice they support. |
| Reconsideration | The source, observation, configuration, threshold, authority, horizon or candidate change that could alter a specified claim or disposition. |

Put the disposition and its most important limit first. Keep the evidence and reasoning reachable without requiring the recipient to reconstruct the entire analysis. Where a protected annex limits access, the accessible return must still state the resulting reliance restriction; it must not hide that a decisive premise is unavailable to the recipient.

Identify the source and meaning of a threshold. If it governs an action, also establish the applicable rule and authority. “Reconsider when recovery evidence no longer supports the continuity condition” is useful only if the named evidence, condition and receiving question can be recovered. `PSDA.15` designs how such evidence will be obtained and interpreted. If a positive recommendation depends on ongoing observation, an unassigned or infeasible observation obligation is a material limit now, not an administrative detail to repair after handoff.

#### PSDA.14:4.5 - Return the advice without taking the later choice

Make the result available to the intended recipient in a form suited to the agreed use. For a receiving-use question, apply `A.2.9`: what should the recipient understand or do, what evidence is enough to judge that, and what smallest repair or stop follows? Explaining the conditional nature of a ranking may be necessary; obtaining agreement with it is not the same task.

Distinguish sending the recommendation, its content and form, the response and any later effect. An acknowledgement can establish receipt. A claim about understanding, consent, reliance, a decision, implementation or effectiveness needs evidence for that claim. If a communication also authorizes action, identify the issuing actor, its authority and the conditions that make the communication effective.

The authority-holding System may later choose, reject, retain alternatives, commission a probe or reroute under `C.11` or its direct domain rule. When a corporate governance decision is required, the organ with the relevant mandate can use `CGOV.11` to consider the recommendation and any disagreement and decide.

Returning the advice closes this recommendation application, including an honest stop branch. Later premise refresh and a newly composed recommendation are later work. Any promised professional contact, referral or service closure follows the terms of the relationship.

### PSDA.14:5 - Archetypal Grounding

The examples stipulate the specialist findings, authority and protected conditions needed for each recommendation.

#### PSDA.14:5.1 - A pump comparison that cannot yet choose an investment

An East-District authority asks a separate analysis team for advice on flood-pump investment for the coming season. Its receiving decision is whether and how to commit funds. The live candidates include a baseline `N`, fixed pumping `F`, mobile pumping `M` and staged combination `S`.

The qualified numerical slice concerns pumping-service loss and incremental cost, not the whole public consequence. In the stated model, `F` has loss 2 in normal access and 3 with road loss, at cost 8; `M` has loss 1 and 9, at cost 5. The baseline and staged alternative are not closed by this two-option comparison. Reachable assistance, property consequences and protected conditions still require their direct evidence and value judgements.

A sensitivity result supplies the conditional boundary `7p > 1 + 3λ` for `F` to have the lower weighted loss, where `p` is the assumed road-loss probability and `λ` the declared cost weight in this illustrative model. Their values for the investment decision remain open. With `λ = 0.5`, `p = 0.2` favours `M`, while `p = 0.6` favours `F`. This is evidence of a possible reversal, not evidence that either probability obtains.

The team returns:

> Retain fixed and mobile pumping for the current pumping-service/cost comparison. A whole-investment recommendation is blocked by the unqualified road-access basis, unresolved assistance and protection consequences, and the unclosed baseline/staged branches. The current model favours different options under different declared assumptions; it does not justify a preferred investment. Reconsider the affected comparison when those results or the authority's value and protection premises change.

A material objection about reachable assistance qualifies the investment advice alongside the numerical losses. The authority can decide what further evidence to commission under its own mandate. A bounded consequence/access request is a useful continuation when an obtainable result can improve the investment decision enough to warrant its acquisition burden. Neither that request nor the conditional comparison authorizes spending, a public trade-off or an operational response.

#### PSDA.14:5.2 - Development advice with a positive branch and an honest gap

A committee asks a separate advisory team which direction to consider for ninety-day service reliability. The holder is the service organization; the committee is recipient and, by the assumed mandate, choice owner. Internal development, an external provider and a mixed human–AI arrangement are live directions. Critical-service continuity, a security boundary and a bounded budget are protected.

An operations account, position/interface account and strategy priority are available, but none compares the arrangements as a whole. The first complete return retains the three directions for consideration and states that their whole-arrangement ranking is unsupported for this horizon and protected conditions. A published Method for obtaining a comparison is not the client-specific result. A comparison request follows only if its attainable contribution warrants the full acquisition burden; the unranked answer need not propose that work.

For a separately stated continuation, suppose qualified allocation and security results now cover all three directions. They support a bounded mixed-arrangement probe, retain internal development, and exclude this provider configuration under the security condition. The probe evidence question, feasibility, exposure and stop are supplied rather than invented. The adviser can then recommend considering that probe first while retaining internal development; throughput remains uncertain and the protected conditions remain binding. The new allocation and security evidence supports this stronger advice.

This continuation does not promote an earlier I/H-only comparison into full-set closure. A different provider, a materially different probe, or model configuration B needs its own qualification. If the mixed result covered only configuration A, advice about B retains that qualification gap or a blocker while independently qualified internal-development content can still be returned. The committee's later choice and probe WorkPlan are separate.

A material provider interest requires disclosure and treatment under the applicable engagement conditions before this positive advice is relied on. A sponsor wanting one supplier does not settle the holder's need or the committee's choice.

#### PSDA.14:5.3 - Unlike holders and ordinary non-use

For a person asking a separate adviser about four months of engineering-management development, suppose qualified accounts of current work show useful cross-discipline coordination experience, while an additional individual transfer study would consume much of the available horizon. The adviser can recommend considering a coordination direction within the person's accessible work and support, with uncertainty about the four-month capability gain. This is a substantive direction for consideration, not proof of intervention effect or independent transfer. A course attendance record alone would not support that advice. When current premises support two directions without ordering them, return that retained set and its distinguishing limit; the person's later choice remains theirs.

For an authorized team considering an AI scaffold or human–AI allocation, name the exact changed object, version, environment, evaluation validity, oversight and protected conditions. Use applicable evidence about the AI configuration, security and any organization or allocation question that bears on it. A human learning study or a ranked recommender-system output does not establish those premises. If a known inadmissible configuration cannot meet the protected boundary, block that recommendation; if the evidence is merely absent, name the gap rather than claiming failure.

For a non-cultural population or lineage with no population-local recipient or chooser, abstain from attributing a recipient-owned development recommendation to it. Investigate population change using an appropriate evolutionary account if that is the question. A separately authorized research team considering an intervention is a different recipient-owned case with scientific, safety and governance premises.

For a chooser who already has an adequate option set and needs only to make their own decision, use direct domain or `C.11` guidance. Neither an adviser nor a PSDA return package needs to be invented.

### PSDA.14:6 - Bias-Annotation

A decisive-sounding answer can conceal uncertainty, but perpetual qualification can also conceal a warranted recommendation. Test both errors: what stronger claim is unsupported, and what useful claim is being withheld despite adequate premises?

Sponsor preference, provider interest and model convenience can shape the candidate domain before the recommendation is written. Inspect exclusions and unclosed branches, not just the displayed winner. Preserve material dissent without implying that every view has equal evidential support or that unanimity is required.

An available numerical score may dominate attention while a consent, continuity or access condition is left in prose. Keep non-compensable conditions visible at the point of disposition. Conversely, do not invent a protected condition from the adviser's personal preference.

### PSDA.14:7 - Conformance Checklist

**Recognition** asks whether recommendation composition is the missing result: a named recipient needs an answer that combines qualified premises, and the account can support their inquiry, consideration or grounds. A short supported answer with its necessary limit can close a small use; a selected request or exact blocker can also be useful.

**Assurance** asks whether this particular disposition is warranted for its intended reliance. Consequential uses add the direct domain's evidence, competence, independence, consent, safety, security, institutional and validation conditions; the size of the account does not lower them.

| Check | Sufficient answer |
| --- | --- |
| Receiving use | Recipient, subject, horizon, recommending performer, receiving decision or work and any applicable choice authority are recoverable. |
| Premise fit | Every decision-bearing input fits its applicable configuration, window and use, or its gap and consequence are explicit. |
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
| Use a probe as the default answer to uncertainty | Identify the question, how its answer could affect the advice, the attainable evidence, exposure, delay and stopping condition. |
| Turn delivery or agreement into authorization | For a claim about a later choice or authorization, establish who decided, their authority and the act that made it effective. For a communication problem, establish what the intended recipient understood and supply any needed clarification. |
| Offer a universal development prescription | Recover holder-specific premises; return the smallest gap where human, organization and AI evidence differ. |
| Hide a blocker behind a long report | Lead with what cannot yet be responsibly recommended and the exact result that could change it. |

### PSDA.14:9 - Consequences

The recipient can examine the advice, use it under the relevant authority or reconsider it when a premise changes. An unresolved comparison or a specific reason for withholding advice can be sufficient for the intended use.

The cost is explicit reasoning at the boundary between analysis and advice. Some requests cannot be closed with a single direction, and some attractive probes remain unsupported. State what the available evidence and authority permit in that case.

### PSDA.14:10 - Rationale

Recommendation composition has work left after generic evidence, comparison and choice guidance. Evidence can support a claim without determining what to advise; a comparison can leave alternatives unresolved; a later commitment needs a decision under the applicable rule. This pattern connects those qualified results to one recipient's question and makes the supported disposition intelligible.

An adviser can recommend a course, retain several alternatives, propose a bounded inquiry or identify why the requested advice cannot yet be given. Apply each premise’s limits to the claims that depend on it. A gap in one branch may leave another supported.

### PSDA.14:11 - SoTA-Echoing

The practice question is **how to return useful advice from qualified analysis without manufacturing a complete order, professional competence or recipient choice**. The selected line combines explicit decision-analysis warrant with a source-bounded professional return. Its additional explanation costs effort; that cost is justified where a lost condition could change the next decision, and is reduced to a short return in a simple case.

| Question and selected move | Serious alternative, defect and changed locus | Source role, limit and reopen condition |
| --- | --- | --- |
| How does comparison become advice? **Adapt** structured preference-to-recommendation reasoning, preserving the problem and model conditions. | A single score is economical when a justified model covers the question. It fails when incomplete preferences or an unclosed candidate branch are silently filled in. Sections 4.2–4.4 require the scheme, inference and scope rather than banning scalar comparison. | [Greco, Słowiński and Wallenius (2025), *Fifty years of multiple criteria decision analysis*](https://doi.org/10.1016/j.ejor.2024.07.038), is a best-known-line synthesis of finite-action MCDA and different preference-to-recommendation procedures. It supplies neither this engagement's values nor universal superiority of one procedure. Reopen when a rival gives equally warranted advice with materially lower burden, or the finite-action/model assumptions cease to fit. |
| What must accompany technically supported organizational advice? **Adapt** explicit engagement, client involvement and conflict qualification. | A technically correct memo can suffice for a bounded analytical request. It is insufficient when reliance also depends on mandate or a material provider interest. Sections 4.1 and 5.2 keep those conditions with the advice. | [ICMCI v4.0 (2021), C.1.1–2, C.2.1 and E.3.5](https://www.cmc-global.org/sites/default/files/public/icmci_cmc002_competence_framework_version_4.0_1.pdf), is a substantive professional comparator, not a universal procedure or effectiveness study. Reopen on a changed applicable service rule or evidence that this qualification omits a material relationship condition. |
| What makes a human career return usable? **Adopt within that service** intelligible basis, consent and competent assessment use; retain referral where required. | Generic “best next course” advice is shorter but can conceal the person's receiving question and unsupported assessment. Sections 4.1, 4.5 and 5.3 retain these boundaries while leaving intervention and transfer evidence to their owners. | [NCDA Code of Ethics (2024), A.2, A.10 and E.1–2](https://www.ncda.org/aws/NCDA/asset_manager/get_file/3395), is a profession-specific normative comparator. It proves no learning effect and supplies no AI-holder assessment rule. Reopen when the applicable service or applicable professional conditions change. |

### PSDA.14:12 - Relations

- `PSDA.11` supplies the bounded engagement question for the same subject and receiving use. Establish any mandate needed for this recommendation on its own grounds.
- `PSDA.13` supplies material shared and contested claims. They inform the recommendation without settling the later choice.
- `PSDA.5`, `PSDA.6`, `PSDA.7`, `PSDA.8` supply the candidate, value, uncertainty and comparison results needed to interpret the advice. `PSDA.9` supplies robust regions, reversals and information priorities where they can affect the advice or its grounds for the same configuration and horizon.
- `A.15.9` supplies qualified use and selection of worthwhile acquisition for external results; use `A.10` when the connection between a source and its use is unclear or a needed reproducible account is missing. Holder practices retain facts, Methods, protected conditions and conclusion authority.
- Use `A.2.9` to assess what the recipient can use and which institutional effects communication can have. A later choice belongs to the authorized holder under `C.11` or the domain rule. A plan, performed work and its effects have their own conditions.
- Use `PSDA.15` to examine later decisions, consequences, signposts or changed premises where follow-up is needed. For a claim that a decision or implementation occurred, use evidence of that particular act.
- `CGOV.11` may use the recommendation and unresolved disagreement for the named corporate matter. Only the authority-holding System supplies the authorization Work.
- Missing, stale, out-of-scope or incompatible contributions call for an adequate qualified direct result or the exact missing-result return.

### PSDA.14:End

## PSDA.15 - Arrange Decision Follow-up or Reassess Advice After a Change

> **Type:** Method pattern (DPF)
> **Status:** Stable
>
> **Primary working result:** an arrangement for the observation and interpretation a recommendation or decision needs, or an assessment of what a changed premise means for a particular use of the advice. Identify what holds, what must be narrowed or withheld and whether further evidence or a new recommendation is warranted.

### PSDA.15:1 - Problem frame

**Use this when** a recommendation or decision depends on conditions that may change, and the required observation, interpretation or response is unsettled. Also enter directly when a new source, configuration, observation or authority condition may have made existing advice stale.

A project may have a dashboard but no way to connect an alert to a particular assumption. An adviser may have promised to “check back” without establishing access to the receiving decision or its consequences. A revised AI evaluation may concern configuration B while the recommendation still relies on configuration A. In each case, more reporting alone does not close the gap.

This branch of decision support concerns a recommendation or decision whose grounds or consequences need follow-up. Connect a relevant observation to the support result it could change. Use the direct practice for source maintenance, operations, implementation, strategy, professional services or cultural change where that practice owns the whole question.

The practical gain is a timely, bounded return: the advice still holds under stated conditions; a claim must narrow; a premise is missing; a needed premise must be re-established; or a new recommendation is needed. The practitioner can preserve unaffected useful content without silently preserving an invalid whole.

Reuse an arrangement that already covers the follow-up question. A change that affects known advice can be examined directly. For an immediate operational response use the applicable rule and authority. Use the direct source-maintenance method where the change has no effect on decision support.

### PSDA.15:2 - Problem

A recommendation, a later authorized decision, implementation and observed consequences are different results. Yet follow-up often treats the recommendation as evidence of what was chosen and treats a plan as evidence of what was done. A missing report can then be mistaken for unchanged conditions, and an improvement can be wrongly attributed to the advice.

The reverse failure is indiscriminate reopening. Every source revision, new observation or changed model version causes the whole engagement to restart, even when only one candidate or consequence claim relied on the changed premise. Useful independent results are delayed while the specific gap remains poorly specified.

When future observations are needed, design their collection and interpretation around the claim they can change. When an existing change can already be assessed, return its claim-level effect directly. An observation arrangement needs a competent interpreter, a specified receiving use, a timely route and an honest answer when access or evidence fails.

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

Start with the follow-up question. For needed future observations, assess the feasible arrangements and compare material alternatives. Establish the observation and interpretation work when implementation is required. For a current change, recover its effect on the affected claim and return the smallest warranted update through §§4.5–4.7. Preparation may begin before recommendation delivery; an already supported update does not require a new observation arrangement.

#### PSDA.15:4.1 - Recover the recommendation, decision and implementation separately

Name the receiving question, subject, horizon, recipient, any relevant decision holder, alternatives, protected conditions and the recommendation's current disposition. An adequate `PSDA.14` result supplies what was advised and why. If it is unavailable, stale or outside the present use, recover a qualified direct account or state the exact gap.

Establish what is known about a later decision when the question requires it. Use evidence of the decision and the relevant authority, such as an applicable record from the holder or another qualified source. Distinguish authorization of a study, authorization of an intervention, rejection of advice and an unestablished decision. If communication is claimed to have authorized the action, apply the direct authority and `A.2.9` conditions.

Use implementation and consequence evidence where the question needs it. A WorkPlan supports a claim about intended work. For a claim of execution, establish what was done, in which configuration and interval. For a consequence, identify the observation and its limits. Attributing a change to the advice or action requires appropriate causal evidence.

A useful current return can therefore be: “The recommendation remains conditional; the receiving decision is not yet established; no implementation consequence is claimed.” Report a decision of the authorized holder before attributing an action choice to it.

#### PSDA.15:4.2 - Name the premises and observations that can change the answer

For each material condition, connect the premise to the recommendation claim, compared alternative, model, protection condition or problem boundary that uses it. State what difference would change the current decision-support result and what evidence could establish it. Identify the contributor or interpreter when needed.

The observation may concern an expected consequence, an assumption, a new opportunity, a source's qualification, a participant's material objection, a protection breach or a changed authority condition. It need not be a numeric metric. A new affected group can reopen scope even while existing performance indicators remain favourable.

Use the following questions to trace a premise into its intended use.

| Follow-up position | What must be recoverable |
| --- | --- |
| Current premise and receiving use | The exact claim, configuration, horizon and recommendation or decision-support result that relies on it. |
| Observation or source return | What evidence could test or change it, from which observation, supplier, participant or authoritative source. |
| Interpretation | How the evidence can be qualified, who can interpret it and what it would mean for the finding or decision. |
| Signpost and reconsideration condition | The observable indication, the condition that makes reconsideration necessary, and the source of any threshold or protected limit. |
| Timing and access | When evidence is needed, delay in obtaining and interpreting it, access and disclosure conditions, and the effect of a missed observation. |
| Next result and owner | Which source, model, comparison, formulation or recommendation would change, and who holds any decision or operational authority the response requires. |

A **signpost** is an observation that can reveal a material change. A **reconsideration condition** specifies when the observation warrants reopening a particular question. If an operational rule requires a response, establish its applicability, the response and who may carry it out.

Choose timing from the consequence of late knowledge. If collecting and interpreting the observation, and providing any required response, would take longer than the receiving window allows, move the observation earlier, choose a feasible proxy with its limits, change the arrangement, or return that the promised follow-up is not adequate.

#### PSDA.15:4.3 - Generate and compare follow-up arrangements

Use an adequate existing arrangement. When design remains open, compare the viable ways of obtaining and using the evidence the question needs. Possibilities include a recipient-owned scheduled review using existing evidence, a targeted specialist test before a commitment, event-driven notification with qualified interpretation, or a coupled arrangement combining targeted tests with a limited route for unexpected changes. A justified one-off return with no continuing service may be enough for a short, low-consequence use.

Compare coverage of the material questions, detection and interpretation delay, uncertainty, participation, observer independence where required, effort, confidentiality, cost, and the feasible receiving response. Do not maximize the number or frequency of indicators. For a time-critical action, check whether a competent authorized receiver can act before the deadline. A timely observation can also answer a technical question in its own right.

Targeted monitoring tests a named question; broader observation can reveal unexpected change. Their balance is a design choice for this decision. The distinction is supported by the current environmental decision-support discussion in [Manley, Povak, Reynolds and Hessburg (2026), Discussion / “Change is inevitable, learning is critical”](https://www.frontiersin.org/journals/forests-and-global-change/articles/10.3389/ffgc.2026.1783129/full); apply its distinction to the present use and seek separate grounds for transfer of an effect.

Use a `PSDA.17` conflict/facilitation-architecture result only if it constrains this design choice. For example, a material participant correction must reach the analyst before the comparison is used, or an observer cannot also carry an incompatible facilitation burden. The constraint does not choose the follow-up arrangement. Assess arrangements that respect the constraint, comparing alternatives where there are meaningful differences. Return to `PSDA.17` only when the underlying interference itself needs a different decision.

Use `A.22` when the selected organization of independently identified constituents and obtaining relations is itself the subject of a structure claim. A proposed arrangement remains a design description until the required participants, access, assignments and relations are established.

#### PSDA.15:4.4 - Establish a viable observation and return arrangement

For an arrangement to be established, identify who observes, who interprets, who receives the result and who holds any resulting decision. For a proposal, state the corresponding requirements and what is already in place. Establish the assignments, capability, access, resources, timing and protection needed for those particular contributions. Several functions may be carried by one performer where suitable; distinguish them when competence, independence, workload or authority makes that difference material.

State what happens if the observer cannot obtain the evidence, the source becomes unavailable, the interpreting owner changes, or the evidence arrives too late. A failed observation is not a favourable observation. Return the gap and its effect on current reliance to the named receiver; use any existing authorized escalation or protection rule when it applies.

Where a professional service applies, fit contact, confidentiality, referral and closure to that service's conditions. The [NCDA 2024 Code, A.10 and B.1](https://www.ncda.org/aws/NCDA/asset_manager/get_file/3395), for example, constrains continuity and information sharing in career services; it creates no AI-holder duty or universal follow-up contract.

Before relying on the arrangement, establish that a material observation can be obtained, qualified, delivered and interpreted in time for the named use. Reuse sufficient operating evidence, or choose a proportionate test where evidence is missing. A prospective walkthrough can expose an assignment or interpretation gap; it proves neither later enactment nor empirical effectiveness. Use stronger domain validation when the consequence requires it.

State whether the requested result is a proposal with conditions, an arrangement established for its bounded use, a specific limit or a current finding from existing evidence. Do not promise observation that has no capable performer or permitted source. State the closing or review condition for the arrangement so that a bounded recommendation does not create indefinite unowned monitoring.

#### PSDA.15:4.5 - Interpret actual observations before revising advice

When evidence arrives, first establish its subject, configuration, interval, provenance, Method, uncertainty and allowed use. Use `A.10` when the source-to-use account remains implicit or a needed reproducible account is missing. An adequate existing interpretation may support the answer; a missing one may limit or block it. Select a further specialist result through `A.15.9` and `C.11.DUA` only when its attainable contribution warrants the whole burden within the receiving window.

Compare the qualified evidence with the exact condition it was meant to test. Distinguish a change in the world, a changed source claim, an expired reliance window, a changed value judgement, a revised model and a merely changed representation. A diary review date is not by itself an expired reliance window. When meaning, applicability and access remain compatible, a repaired reference may finish the source update without renewed advice, multi-use search or another result record. An expired qualification or missing required observation limits the use that depends on it.

When the source changes from configuration A to B, check which grounds transfer to B. Preserve the earlier result for its earlier subject and conditions. State which conclusion about B the available evidence leaves unsupported. Seek further evidence when its attainable contribution to the question warrants the cost. Similarly, failure to observe a threshold crossing proves nothing unless the observation coverage and sensitivity support that inference.

Keep the observations and their interpretation distinct from the next decision. To report a changed action decision, use evidence of what the authorized holder decided. If the adviser concludes that a different action should be considered, that is renewed advice, not implementation control.

#### PSDA.15:4.6 - Return only the affected decision-support consequence

Trace the changed premise into the particular claim or disposition that relies on it. Preserve an independent result where its conditions of use still hold. If dependence or coverage remains unresolved, state that gap; do not label an uninspected branch unaffected.

| Current return | When it is warranted | What happens next |
| --- | --- | --- |
| Unchanged within stated conditions | Qualified evidence does not alter the relied-on premise, or the changed claim is outside the inspected use. | Retain that bounded advice and its current conditions. State the next observation when a follow-up use needs it. This is not authority to continue an intervention. |
| Narrowed | A useful portion still has an adequate basis, but the previous scope, configuration, window or strength is no longer supported. | Return the surviving claim and the withdrawn scope explicitly. Do not relabel the narrowed result as the original whole. |
| Blocked for the affected use | A necessary premise, authority condition, observation or interpretation is unavailable or no longer adequate. | State what cannot responsibly be advised or relied on now, the missing basis and who can supply the missing result or direct the question where that is known. Preserve separate usable content. |
| Reopen a named contributor | A needed stronger answer warrants an obtainable source, candidate, value, uncertainty, model, consequence, robustness or scope result, considering the complete acquisition burden. | Obtain the bounded result from the appropriate source or request it from a capable contributor when a request is needed. The present qualified limit can close the earlier answer; a pending request is not the refreshed result. |
| Compose a later recommendation | Changed qualified premises require a different disposition or a newly composed answer to the receiving question. | Use `PSDA.14` with the current premises and remaining gaps. Preserve the earlier recommendation occurrence and the separate later choice. |

These are scoped conclusions. One event can leave an internal-development claim unchanged, narrow a mixed-arrangement claim to configuration A, block advice about B, and reopen its evaluation supplier. Only the affected combined recommendation needs recomposition.

Keep **continue, adjust, refresh and reframe** precise. Continuing reliance on unchanged advice is a decision-support return. Adjusting a selected action requires the competent owner and its authorized decision, even if the original formulation remains adequate. To refresh a model or evidence, use an adequate current result, qualify it directly or obtain a needed contribution. An action change has its own grounds and authority. Reframing reopens the problem or boundary through `PSDA.1` or `PSDA.2` when the old question no longer covers the material situation.

For one known reliance question, use the direct subject guidance and any adequate explicit source-use account. Invoke `A.10` when that account remains implicit or a needed reproducible account is missing. Use `A.10.1` when a material change leaves the dependent uses to be discovered or several dependent uses need coordinated revalidation. Set the search scope where needed, establish direct reliance and return the affected subject results and material gaps. Equivalent irrelevant mentions can be grouped. The direct decision-support answer can finish without an additional common account unless a receiver needs that overview. Any no-impact claim still requires adequate coverage and support. Citation or adjacency is not dependence. Use `G.11` for currentness, decay and scoped refresh planning/reporting when that is the live result; neither pattern supplies a new domain conclusion or recipient choice.

#### PSDA.15:4.7 - Close the present return and preserve the next useful question

Return the observation, qualification, affected use and material limits needed by the current question. Name a next responsible receiver when the result requires further action; a sufficient direct return creates no additional completion record. Preserve enough of the prior recommendation, decision and evidence to distinguish a later reassessment from a claim that the earlier Work was different.

Finish when the follow-up question has a supported answer or identified limit and the recipient can use it within that scope. Continue any existing monitoring or professional service under its own mandate and end condition.

When follow-up evidence can change the decision-support Method repertoire, supply the bounded case, conditions, failure or useful variation to `PSDA.16`. Its owner still compares the repertoire and obtains its own result. One successful delivery, revised diagram or favourable outcome proves neither general Method effectiveness nor cultural continuation.

### PSDA.15:5 - Archetypal Grounding

The examples use stipulated arrangements, authorizations, observations and specialist results. Each supports a different part of the follow-up conclusion.

#### PSDA.15:5.1 - Follow a blocked flood-pump recommendation without inventing a decision

The East-District analysis team has returned a conditional fixed/mobile pumping comparison and blocked a whole-investment recommendation. The road-access basis, reachable assistance and protection consequences, and baseline/staged branches remain unresolved. There is no established investment choice to “monitor.”

The follow-up question is which missing evidence can reach a renewed investment consideration before the coming season. A prior engagement-arrangement decision requires material participant corrections to reach the analyst before any comparison is treated as closed. The follow-up designer uses that constraint, not a prescribed meeting sequence.

Three arrangements are compared. An end-of-season review is inexpensive but too late for the receiving decision. Continuous pump telemetry gives frequent technical data but does not resolve deployment permission, affected residents' access or the unanalysed staged alternative. A bounded pre-decision arrangement would obtain targeted logistics and consequence results, admit material participant corrections through the facilitator and give the analyst an interpretation window before the authority next considers investment.

The third arrangement is selected in this illustration because the named logistics and consequence suppliers, facilitator and analyst have the required availability and access, and the authority's next consideration date is known. It costs a small additional interpretation meeting. If any decisive supplier cannot return in time, the arrangement reports that limitation and preserves the blocker; it does not quietly move the decision deadline or claim the authority has agreed.

In the continuation, the authority supplies qualified evidence that it has authorized an access study, not a pump purchase. The study's performer then returns evidence that the mobile deployment arrangement assumed in the earlier comparison is unavailable for the required flood-period window. The analyst does not substitute a guessed road-loss probability.

The current return is: preserve the earlier fixed-pump performance claim for its original conditions; narrow the earlier fixed/mobile comparison to the prior deployment basis; block its current investment use; identify the mobile-deployment and consequence premises an updated investment recommendation would require. The assistance and staged-alternative gaps remain open. The authority's study decision is recorded separately from the unchanged absence of a qualified investment decision.

The arrangement also preserves a route for a newly identified affected group to raise a material access concern. That concern would reopen the boundary question rather than merely add another performance reading. No favourable pump metric can by itself close that question.

#### PSDA.15:5.2 - One changed AI configuration need not restart all advice

For a ninety-day reliability question, a committee received advice to consider a bounded mixed human–AI probe while retaining internal development. Assume the advice relied on qualified whole-arrangement, security and evaluation results for configuration A. A separate supplied decision shows that the committee authorized only a bounded probe under specified continuity and oversight conditions.

The follow-up designer compares a monthly report, an automated outcome stream without specialist interpretation, and configuration-change notification combined with a targeted probe-evidence review. The monthly option is too slow for the reversible-probe decision window. The stream alone cannot establish that a new scaffold or tool environment is covered by the previous evaluation. The combined option is selected only after the configuration owner, evaluation supplier, adviser and committee have the necessary notification, access, interpretation and receiving arrangements.

A configuration-change notice identifies B. B’s operating quality requires applicable evidence. The probe observation covers B, while the relied-on evaluation still covers A. The response is deliberately split:

| Inspected use | Current consequence |
| --- | --- |
| Internal-development claim whose premises did not use A's evaluation or the changed allocation | Remains usable for its named service and horizon. |
| Earlier mixed-arrangement recommendation for A | Retained as the earlier conditional result; it is not qualification of B. |
| Advice to extend the probe or deploy B | Blocked pending the exact B evaluation, security and allocation premises that can change that advice. |
| Need for renewed comparison | Reopen only the suppliers and comparison claims that depend on the changed configuration; compose a later recommendation when their qualified returns support one. |

The configuration notice does not choose a fallback, stop a service or revoke a permission. If an existing authorized continuity or safety rule governs B, its competent owner applies it separately; otherwise the choice or authority gap is returned promptly. The adviser must not keep an apparently positive recommendation by treating silence from the evaluation supplier as approval.

The same locality works with a human development premise. If an employee's available practice time changes, reassess the intervention or transfer claim whose grounds included that time. Preserve unrelated organization or AI evidence. Applicable client-contact conditions may require a conversation, but that conversation does not itself establish transfer or consent to a different intervention.

#### PSDA.15:5.3 - Cheap use, missed observation and proper stop

A recipient has one short, reversible comparison whose evidence remains valid until a named review date. An existing arrangement can obtain the observation that matters within its allowed window. Retain it.

If the named observation is missed, the current answer is the scoped evidence gap and its effect on reliance, not “unchanged.” If the receiving decision has ended and no continuing evidence, service or protection obligation remains, close this follow-up use with its final qualified return.

A population without a population-local recipient or choice owner does not acquire either through a follow-up table. Preserve the abstention from that recommendation use. A research team's separately authorized intervention has its own decision, experimental Work and observation conditions.

### PSDA.15:6 - Bias-Annotation

Confirmation bias favours observing only the consequences that made the recommendation attractive. Include the discriminating failure and an affordable route for material unexpected change. Avoid turning this into exhaustive surveillance: the receiving decision and possible loss still bound effort and access.

Automation bias can make an alert look like an interpreted result or authorized command. Identify what was collected, what interpretation was supported and who or what had authority for any decision. A software service may perform one or more of these operations under its actual capabilities and mandate.

Outcome bias can rewrite the earlier advice as obviously correct or wrong after the event. Judge the earlier recommendation against its then-current premises and intended use; judge the later return against the changed evidence. A causal effectiveness claim remains a separate question.

### PSDA.15:7 - Conformance Checklist

**Recognition** asks whether an observation or changed premise can alter the finding, its grounds or the advice for a particular use and whether the path to a useful return is missing. One existing adequate result or one clearly scoped gap can close a small case.

**Assurance** asks whether this arrangement can obtain and qualify the needed evidence in time, and what the current evidence establishes. Consequential uses require their direct observation, validation, competence, independence, protection and authority conditions. A prospective walkthrough tests design only; it does not replace evidence from enactment.

| Check | Sufficient answer |
| --- | --- |
| Distinct results | Recommendation, later authorized decision, intended work, implementation and observation are distinguished wherever the finding relies on them. A missing fact is reported as a limit on the claim it affects. |
| Material observation | Each selected observation can change a named premise, claim, alternative, condition or boundary; any threshold has a qualified meaning. |
| Design choice | When a follow-up arrangement needs to be designed, the feasible arrangements were assessed for coverage, delay, burden and receiving use. Any comparison respects the relevant PSDA.17 constraints. |
| Viability | Any observation, interpretation and return relied on here have the necessary performers, access, resources, timing, protection and failure route. |
| Current evidence | The evidence fits the subject, configuration, interval and use. A claim based on an event’s absence accounts for observation coverage and sensitivity. |
| Local consequence | Unchanged, narrowed, blocked, reopened-contributor and later-recommendation conclusions name their exact affected scopes and gaps. |
| Authority and closure | Operational change and recipient choice retain their direct authority; the follow-up return has a bounded continuation or end condition. |

### PSDA.15:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Monitor implementation of what was merely recommended | For claims about a later decision or implementation, use evidence of each separately; state unknown status when they are absent. |
| Use an indicator list as the whole arrangement | Name its claim, interpreting owner, timing, receiving use and failure return. |
| Trigger an action automatically from a threshold | Establish the direct operational authority and response rule separately; otherwise return the qualified reconsideration question. |
| Rerun the whole engagement after every new version | Inspect changed claim content and which results rely on it; preserve independently usable results and reopen only affected contributors. |
| Reuse an A-specific evaluation for configuration B | Retain the historical A result and use applicable evidence about B or identify the remaining qualification gap. |
| Interpret a missed observation as no change | Return the gap and its consequence for reliance, with the responsible receiver. |
| Call later improvement proof that the advice worked | Report the observed change. To attribute it to the advice, use an appropriate causal result or state the remaining uncertainty. |
| Keep follow-up alive without an owner or end condition | Establish whether a service or observation duty remains in force, or close with an honest bounded return. |

### PSDA.15:9 - Consequences

The practitioner can react to a meaningful change without losing every previous result. The recipient sees what remains usable, what is unknown, which contributor should respond and whether a new recommendation is needed. Later decisions and operational responses remain attributable to their real owners.

The arrangement costs observation and interpretation effort and can expose a limitation before action is taken: no feasible way exists to watch a condition on which the advice depends. A positive recommendation cannot honestly promise protection through follow-up that cannot be performed.

### PSDA.15:10 - Rationale

Trace each changed consequence, assumption, alternative, model, authority or boundary to the recommendation that depends on it. Decide what can be concluded now and whether a future observation and interpretation arrangement is needed.

Before relying on a future observation, establish that its connection to the receiving question can be used. One changed observation can open the pattern directly. A proposal can stop at an infeasible observation condition; a later source can leave the answer unchanged; a changed boundary can require formulation work without first rerunning every calculation.

Follow dependence between claims. One file can contain independent claims, and claims in separate documents can depend on the same premise. Stop when the remaining receiving questions retain their existing grounds.

### PSDA.15:11 - SoTA-Echoing

The practice question is **how to keep decision support useful under change without confusing observation with decision or causing indiscriminate recomputation**. The selected line designs decision-linked evidence and interpretation, combines targeted and unexpected-change coverage where warranted, and returns only the affected question. The trade-off is explicit observation and interpretation effort; lower-burden arrangements remain preferable when they cover the intended use.

| Question and selected move | Serious alternative, defect and changed locus | Source role, limit and reopen condition |
| --- | --- | --- |
| What should cause reconsideration? **Adapt** named signposts and switch/reconsideration conditions tied to the decision or finding under consideration. | A fixed periodic review is adequate for slowly changing, covered conditions; alone it can miss a consequential change before the next decision. Sections 4.2–4.6 connect evidence, timing and affected result without treating a signal as automatic authority. | [Lynch et al. (2025), *RAD switch points and triggers for adaptation planning*](https://www.usgs.gov/publications/rad-resist-accept-direct-switch-points-and-triggers-adaptation-planning), is a current domain line using three natural-resource cases for iterative reevaluation. It supplies no universal threshold, response or institution. Reopen when a better-supported rival or changed decision window defeats this observation design. |
| Should follow-up only test the predicted outcome? **Adapt** a proportionate combination of targeted questions and observation for unexpected change. | Targeted tests are efficient for a specified uncertainty; broad surveillance can expose unanticipated change but adds burden and weakly identified signals. Sections 4.2–4.3 and 5.1 compare the mix instead of prescribing either alone. | [Manley et al. (2026), *Meeting the moment*, Discussion / “Change is inevitable, learning is critical”](https://www.frontiersin.org/journals/forests-and-global-change/articles/10.3389/ffgc.2026.1783129/full), is a contemporary environmental decision-support perspective distinguishing these monitoring uses, not a comparative effectiveness trial. Reopen on representative evidence that another mix covers the material questions with less burden or delay. |
| Does a returned recommendation end every relationship obligation? **Adapt** bounded service continuation and closure while keeping renewed advice a later application. | Ending all contact at delivery may fit a one-off analytical request but not an obtaining service duty; indefinite monitoring creates the opposite failure. Sections 4.4 and 4.7 use the applicable relationship and end condition. | [ICMCI v4.0, C.1.1–2](https://www.cmc-global.org/sites/default/files/public/icmci_cmc002_competence_framework_version_4.0_1.pdf), is a professional comparator for assignment closure. [NCDA 2024, A.10](https://www.ncda.org/aws/NCDA/asset_manager/get_file/3395), governs its own service continuity/referral. Neither establishes a universal contract. Reopen when the actual service or applicable duties change. |

### PSDA.15:12 - Relations

- `PSDA.14` supplies the recommendation's receiving decision, conditions, dissent, gaps and reopen basis. It supplies no evidence that the later decision or implementation occurred.
- `PSDA.17` can establish a constraint on feasible follow-up arrangements. Use it where it affects the assessment or choice.
- Use `PSDA.1` or `PSDA.2` for a change to the formulation or boundary. Use `PSDA.3` or `PSDA.5`–`PSDA.9` for an affected model, candidate, value, uncertainty, consequence or robustness question.
- Use `A.10` for an implicit source-to-use account or a missing reproducible account needed for the use. Use `A.15.9` for a relevant external result. Use `A.10.1` when a material change leaves the dependent uses to be discovered or several uses need coordinated revalidation. For a currentness or refresh question, apply `G.11` within its scope. Establish the domain conclusion from its own grounds.
- `A.22` governs a selected-structure claim when made. It does not establish the proposed arrangement, participant assignment, observation, decision or effectiveness from a representation.
- `A.2.9`, `C.11` and direct domain authority distinguish authorization, recipient choice and their records. `A.15.2` and `A.15.1` distinguish intended from performed Work; causal claims retain their direct evidence requirements.
- `PSDA.16` may use this bounded follow-up evidence when it can change a repertoire decision under the relevant conditions. Evidence neither authorizes nor entails the repertoire result.
- Strategy-direction follow-up, domain operations and professional service management retain their direct owners. A `STR.12` result may be considered only when its exact subject, claims, authority, evidence and effective conditions fit.
- An unavailable, stale, out-of-scope or incompatible input calls for applicable direct evidence or a statement of which conclusion the gap limits.

### PSDA.15:End

## PSDA.16 - Decide Whether and How to Change Problem-Structuring and Decision-Support Methods

> **Type:** Method pattern (DPF)
> **Status:** Stable
>
> **Primary working result:** the decision-support Methods and candidates available for the recurring work, with the reasons and limits for each offering. An assessment may identify where an existing offering fits, which change or trial is warranted, where its use should be narrowed or withdrawn, or which evidence is missing. Preserve its source basis and any established lineage needed for later use.

### PSDA.16:1 - Problem frame

**Use this when** a practice needs to assess how its problem-structuring and decision-support Methods fit recurring work, or decide which offerings to retain, change or withdraw. A familiar workshop no longer covers a recurring participation difficulty. A new analytical technique seems promising, but its input assumptions differ from those of the existing repertoire. Follow-up exposes a repeatedly broken join between a material correction and the recommendation that should use it.

Start with the recurring difficulty and the result the practice needs. Which way fits which situation? What change could help, what would justify a trial, and where might the current offering need a limit? A better source or evidence of a recurring failure may support one local change.

This method concerns the reusable ways a practice structures problems and supports decisions. Describe each Method and any candidate under consideration, the work it can serve and the grounds and limits for that use. A catalogue of schools, tools or courses does not by itself give a practitioner those grounds.

For a future engagement, the practitioner needs to know what a Method does, where it fits, what supports that use and which conditions remain open. When other ways are available, explain how they differ. A small repertoire with these grounds can serve better than a longer list.

**Do not use this pattern** merely to choose an adequate existing Method for one engagement; use `PSDA.4`. Use `PSDA.15` to respond to a changed premise in one current recommendation, and `PSDA.17` for a conflict in the current work arrangement. Use this pattern when the evidence bears on a reusable Method, an applicability claim or what the practice can offer. Changing a document, tool, source locator or one local performance does not by itself create a new Method.

### PSDA.16:2 - Problem

Professional repertoires tend to harden around what their practitioners can already teach, facilitate or compute. New situations are then forced into the incumbent's assumptions: unclear values become invented weights, unequal participation becomes apparent agreement, and a dynamic uncertainty problem becomes one fixed scenario.

The opposite failure is uncontrolled combination. Each engagement adds another technique or software assistant, but nobody identifies the reusable action, how the contributions can be used together, the evidence that transfers or the conditions that defeat it. The resulting collection is larger without being more useful.

Published applications and local successes can compound the problem. A reported use is evidence of that use, not proof of general superiority. A new edition may improve a description without changing a Method. A promising variant may deserve a trial without inheriting its parent's fit. State which offering the evidence supports and what decision, if any, the practice still needs to make.

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

Start from recurring work and the result the practice needs. Identify the usable Method or candidate, the relevant conditions and evidence, and any viable alternative when comparison matters. Report what the practice can offer, or propose a change and its grounds. Carry out the change when implementation is required and authorized. Trial a proposed change when the attainable evidence could affect the conclusion or choice and warrants the full cost.

#### PSDA.16:4.1 - Bound the repertoire question by the work it must serve

Identify who uses or could use the repertoire, the recurring situation, the receiving decision-support result, and the horizon over which the offering matters. The starting question might be: “How can our engagements preserve a late but material participant correction without losing the ability to produce a timely qualified recommendation?”

Establish the conditions that could change the answer. These may include the question and its maturity, affected parties and access to them, protected interests, input values, alternatives, uncertainty, evidence, capability, decision authority, the work that will use the result and any follow-up.

Use a `PSDA.15` result when its evidence affects the assessment or decision under the relevant configuration and horizon. A changed mobile-deployment premise may show that the existing follow-up Method worked by returning the correct blocker. It does not by itself demonstrate a defective Method. If a supplied result is missing, stale or incompatible, use a qualified direct account or name the precise gap.

Distinguish a missing input, a failure to enact the stated Method, a support or capability problem, and a defect in the reusable way itself. A practice cannot repair absent stakeholder access simply by adding another modelling technique. Conversely, more training cannot repair a Method rule that systematically excludes the required correction.

Use C.39.RP when the offered repertoire and its missing contributions need construction, C.39.RQ when the situated requirements for a Method need to be made explicit, and C.11.MV when a Method option's worth is the unresolved comparison. Use the corresponding general operations for those questions. The professional question here is which formulation, modelling, participation or return contribution can be offered under the actual engagement conditions, with the subject evidence and interpretation limits below.

#### PSDA.16:4.2 - Recover candidate ways of working and their contribution boundaries

State each serious candidate as a way of doing: the conditions and actions, what participants contribute and understand, how the inputs and results connect, what can vary and when to stop. Use `A.3.1` for Method identification. Keep an unresolved proposal as a candidate account.

When performances leave the reusable way unclear, use `A.3.1.MR` to recover candidate accounts. Use `A.3.1.DR` for the meaning or status of a proposed way in documentary guidance. If a design choice is missing, use a qualified existing design where it settles the question. If construction is needed, propose the action and conditions yourself or obtain that contribution from a capable designer. Identify who must authorize any consequential selection. A record of past practice may inform the design but cannot enact that choice.

Decompose a heavyweight school or package only far enough to compare contributions. The table illustrates contributions that can address different difficulties. Use the relevant conditions for the recurring work.

| Recurring difficulty | Contribution to recover | Condition that must not be silently supplied |
| --- | --- | --- |
| Participants formulate different problems | Ways to elicit, represent and challenge attributed interpretations; purposeful-activity or concern-mapping contributions where suitable. | Attendance or a shared map does not establish equal influence, representation or agreement. |
| Related decisions cannot be treated independently | Ways to expose connected choice areas, feasible combinations and commitments. | A diagram of dependencies does not establish feasibility or authorize commitments. |
| Values and trade-offs are incompletely stated | Ways to elicit value judgements and compare alternatives under the admitted preference information. | A preference model cannot create legitimate weights or permission to trade a protected condition. |
| Consequences depend on uncertain conditions | Qualified conditional modelling, uncertainty analysis, scenarios, robustness and information-priority work. | A scenario is not its probability; one robust region does not cover every model or value scheme. |
| Analysis does not become usable advice | Ways to compose and explain a source-bounded recommendation, dissent, limits and next use. | A score or specialist answer may support one part of the advice. A decision needs the appropriate authority. |
| Advice loses its basis after change | Ways to observe decision-significant conditions, interpret evidence and reopen the exact affected result. | A signal can justify investigation or a response under an applicable rule. A missed observation can leave the change unknown. |

Soft Systems Methodology, SODA/cognitive mapping, Strategic Choice, MCDA, scenario and robust-decision approaches can contribute to different rows under the conditions supported by their sources. A software platform may support several such contributions.

For assessment or combination in one engagement, use `PSDA.4`. Preserve the meaning of each contribution. For example, an attributed concern may become a candidate objective for examination, not automatically a numerical weight; a scenario may constrain a calculation without supplying a probability. If a proposed whole cannot recover its reusable action and joins, retain the bounded candidate or arrangement description rather than calling co-use a composite Method.

#### PSDA.16:4.3 - Assess the current Method and compare alternatives where needed

Identify the current or proposed offering, its recurring result and the conditions the work requires. A qualified existing assessment can establish its fit or its limit. When an alternative or adaptation is worth considering, compare it against the same result and conditions, at comparable effort where possible.

Determine what each offering lets practitioners and participants do, which conditions it needs and where the evidence leaves fit open. In addition to analytical adequacy, consider meaningful challenge, unequal power, facilitation burden, interpretation skill, source qualification, time to a usable return and cost of maintaining the offering. State a deliberately accepted trade-off when the richer result costs more.

Judge the promised contribution under the conditions of its intended use. A precise score, a satisfying workshop or a large option set supports only what the evidence establishes. One qualified Method can suffice for a narrow recurring use. Another use may need several formulations followed by numerical comparison.

When a change is needed, state its mechanism: which reusable action, input condition, dependency, decision rule or stop changes, what remains, and why that difference could repair the failure. Distinguish this from a change in wording, display, software, local staffing or performance. The latter may require maintenance or a new fit check without identifying another Method.

For example, replacing a paper map with a digital map while preserving attribution, challenge and unresolved-claim rules may change support and access. Replacing the challenge rule with automatic aggregation of all statements changes the reusable way and can lose dissent. Trace what the new interface allows or requires practitioners to do.

Use current `A.3.1.MV` guidance when the unresolved question concerns variant identity, derivation or maintenance of the same Method. The remaining PSDA question is whether that way serves the professional decision-support use: how interpretation, participation, values, uncertainty, authority and follow-up contribute to a usable return. Generic variant maintenance does not answer that field judgement.

#### PSDA.16:4.4 - Build a source-to-claim basis, not a popularity ranking

For each claim that affects later use, identify the source and the part it supports. An instruction may describe how to work, an application report may establish an instance of use, an observation may reveal a failure, and a comparative study may support an advantage under specified conditions. Use each source for the conclusion it warrants.

Identify the action or applicability claim, the source or qualified experience that supports it, the relevant conditions and any remaining uncertainty. Include edition, passage, evidence window and original meaning where they affect reliance. For an open question, identify evidence that could change the conclusion. Account for relevant contrary cases and plausible alternatives when they exist.

The [2019 Smith and Shaw review](https://doi.org/10.1016/j.ejor.2018.05.003) provides an exploratory way to compare PSM characteristics; its classification is not an exhaustive admission rule. [Kogetsidis's 2025 application review](https://doi.org/10.1108/IJOA-08-2024-4746) and [2026 online review of Europe and beyond](https://doi.org/10.1108/EMJB-06-2025-0214) provide leads about reported applications. Their journal and search boundaries limit what they establish about practice outside that corpus. A count tells you how many publications in the corpus report the use. Several reports may describe the same performance. Ranking the Methods for this practice would require evidence about their uses.

A recent decision-analysis synthesis such as [Borgonovo et al. (2026)](https://doi.org/10.1016/j.ejor.2025.05.023) can identify developments in value-focused thinking, graphical modelling, uncertainty, sensitivity and information acquisition. For a particular Method, consult the source needed for its meaning and scope.

Use a qualified existing interpretation, domain result or representative evaluation when it answers the question. For a missing contribution, use `A.15.9` to assess whether obtaining it is worthwhile and respect the supplier’s authority where applicable. Use `A.10` when the source-to-use account is implicit or a reproducible account needed for this use is missing. If a decisive source remains unavailable, qualify the offering or identify the dependent gap.

#### PSDA.16:4.5 - Trial the claimed improvement in representative engagements

For a selected trial, turn the proposed improvement into a question that can fail. Specify the Method or status-preserved candidate, the situation represented, participant and power conditions, required capability and support, a serious comparator when the claim is comparative, the expected result, the burden accepted, and the observation that would retain, narrow or reject the proposal.

Select evidence proportionate to the claim. A walkthrough can expose an impossible join. A constructed exercise can test whether practitioners preserve an objection through a calculation. An authorized field trial can test feasibility and use in a real engagement. Broader transfer or causal-effectiveness claims need stronger and appropriately designed evidence.

For a claim about how the Method works, examine the relevant actions alongside the output. For example, establish who could contribute or challenge; which material statement entered the model; where meaning changed; what was withheld; how uncertainty and protected conditions reached the recommendation; and whether the receiver could use it. The distinction between technically valid models and what people do with them is central to [Franco et al.'s behavioural OR review (2021)](https://doi.org/10.1016/j.ejor.2020.11.031). It supports attention to intervention configuration and interaction, not one universal trial design.

Preserve competing explanations. Better results may reflect a more skilled facilitator, a different participant group, more time, an easier problem or changed support rather than the Method difference. Where those cannot be separated, report what the trial establishes and what remains unresolved; a feasibility finding can still answer its own question.

Do not use a consequential live decision as an uncontrolled Method experiment. Establish the authority, consent, protection, observation and fallback conditions appropriate to the engagement. A prospective candidate can be investigated through a separate trial arrangement without claiming that an unadmitted candidate whole has already been enacted as a `U.Method`.

Retain disconfirming results. A richer Method that cannot run within the actual access or competence conditions may be a poor offering for that use even when its idealized output is better. Conversely, a failed local performance does not disprove the Method when a required condition was absent; it may show that the offering omitted a necessary condition.

#### PSDA.16:4.6 - Return a small current repertoire with differentiated dispositions

Report what the evidence supports for each use. When a repertoire change is requested, distinguish a proposal from a decision made under the relevant authority. The practice may retain an offering, narrow its use, add a qualified variant, keep a proposal for a bounded trial, seek missing evidence or withdraw an offering from one use while preserving its history.

Keep identification separate from validation. An independently identified Method may still have unproved practical fit. A candidate account may have useful trial evidence without yet resolving its Method identity. State what is known about identity and what the evidence shows about fit.

For each entry that matters to the task, make the relevant conditions and grounds in the table available to its next user.

| Repertoire position | Content needed for use |
| --- | --- |
| Recurring situation and receiving result | Who uses the offering, what difficulty it addresses, which result it provides, and the conditions that matter. |
| Method or candidate | Exact reusable action and status; entry, joins, allowed variation and stop; where the full description can be obtained. |
| Reason for the assessment | Grounds for retaining, limiting or changing the offering. For a comparison, the relevant alternative, gain, effort and other losses. |
| Evidence and source basis | Sources or trials that support the claim, their conditions and limits, any contrary evidence and any question still open. |
| Lineage | The source Method or candidate, preserved and changed semantics, and the evidence for derivation; cultural links only where established. |
| Current offering | What is available for this use, conditional, retained for trial, narrowed or withdrawn; required performer/support conditions and source responsibility. |
| Refresh and exit | Which changed claim, failed condition or receiving need would reopen this entry, and what remains usable elsewhere. |

A repertoire may retain alternatives without ranking them. When the task is to declare a selector-facing set result over already identified members, use `G.5` with the exact members, outcome, ordering and basis it requires. Distinguish alternatives retained for later choice from members all included in one named joint use. A Method-family registry or selector declaration supplies neither field fit nor actual enactment and need not be rebuilt for every repertoire update.

Show where a practitioner can find the Method for the named situation, which applicability claim still needs evidence or which use has been withdrawn.

#### PSDA.16:4.7 - Preserve cultural lineage without inventing cultural continuation

Record where a reusable change came from when that relation matters: an identified source Method, a documented adaptation, a changed stopping rule, a taught practice, or another qualified source. Similar names, chronological succession and a shared diagram do not establish derivation.

Keep proposed derivation, observed local enactment, transmission to another practitioner, recognition, selection, retention and loss distinct. A source publication can make a description available while leaving learning and use unobserved. A successful trial can justify a restricted offering without showing that a professional community adopted it.

Use `C.36` for a cultural-evolution question. A qualified variant or local observation may supply evidence for a question about cultural continuation under `PSDA.18`. Identify the practitioners, engagement or community, place and period covered by the evidence. State which relations remain unobserved. For a proposed cultural intervention, establish what authority or existing decision covers it and whether a further decision is needed.

This boundary applies equally to new software support and AI-assisted practice. A tool release is not cultural uptake; widespread use of a tool is not evidence that the same Method was enacted by everyone. Teaching, service change and deliberate cultural intervention require their own work and authority.

#### PSDA.16:4.8 - Refresh the affected offering and preserve an honest stop

Keep the supporting sources and conditions of use available to practitioners who rely on the repertoire. Reopen an entry when new evidence, a source claim, changed Method semantics, participation or authority conditions, support, qualification window or receiving need can change its offering. A new publication date or a file rename alone is not such a change.

For a changed claim, identify which repertoire entries relied on it. Determine which claims remain supported, which need narrower conditions or further evidence, and which uses should be withdrawn. Preserve independent entries and the earlier evidence for its original conditions. If applicability remains unresolved, state the uncertainty rather than assigning an unsupported negative or positive status.

A changed service rule might restrict the human career-advising branch without changing the corresponding findings about organizations or software. A new AI configuration may invalidate evidence for a software-assisted offering without changing the manual Method. If the reusable decision-support action itself changes, identify and assess that semantic change rather than hiding it as maintenance.

Use `A.10` for a known reliance when the source-to-use account is implicit or a reproducible account needed for this use is missing. Use `A.10.1` when a material source change leaves the affected uses to be discovered or several uses need coordinated revalidation. Use `G.11` when currentness or scoped refresh planning or reporting is itself the task. Establish the new repertoire finding from the relevant subject evidence.

Close this repertoire question when the evidence establishes the requested conclusion or identifies the condition or evidence that still limits it. Withdraw only the defeated use, not recoverable history or other supported uses. A still-unqualified new proposal can remain visible without being offered as established practice.

### PSDA.16:5 - Archetypal Grounding

The following cases illustrate a source description, a proposed change, a constructed trial, a qualified offering and the separate evidence a cultural claim would require.

#### PSDA.16:5.1 - A late correction changes an offering, not the whole school

A public decision-support practice serves flood-investment engagements. It maintains an identified one-session inquiry Method: elicit and attribute concerns, compare the admitted alternatives with qualified inputs, record material dissent, and close the session with a bounded return. The Method presumes that all decision-bearing contributions needed for that return are available within the session. The practice has nevertheless offered it as the sole inquiry option for these engagements, including ones in which necessary input can arrive later.

The `PSDA.15` pump follow-up case supplies a changed mobile-deployment premise and the resulting blocker. That alone is not a Method defect: the follow-up correctly prevented an unsupported investment use. The follow-up therefore supports retaining that stop under the stated conditions.

A separate examination of the one-session offering finds the action-changing mismatch. Engagements in this service can receive a qualified access correction after the meeting, while the reusable closing rule provides no way to bring it into the same pending recommendation. The practice must not advertise that offering as sufficient for such engagements.

Three alternatives are considered. Keep the one-session Method but restrict it to uses with the necessary inputs already available; defer the whole engagement until every possible input arrives; or construct a bounded correction-and-return variant that keeps attribution and conditional analysis, permits a material qualified correction before the receiving recommendation closes, and reopens only the affected comparison.

The third proposal changes a reusable join and closing condition by allowing a relevant qualified late correction before the pending recommendation closes. Its candidate account records the parent, retained actions, changed rule, required facilitator/analyst availability and stop when a late contribution cannot be qualified in time. Independent Method identification remains separate from evidence of practical fit.

In the constructed case, the practice tests the two rules in an exercise. The investment decision remains with its holder. Both the incumbent and proposed rule are examined on the same two realistic situations: all required inputs available at the meeting, and a material access correction arriving afterward. Participants' access, analyst time and the receiving deadline are made explicit. The test is whether the correction changes the exact affected comparison while preserving dissent and independent usable claims.

In the illustration, the incumbent gives an adequate bounded return in the first situation but leaves the second correction outside its closed result. The proposed rule preserves the correction and exposes its unresolved consequence in the second situation, at the cost of a further qualified return and analyst/facilitator time. This exercise supports the proposed join's feasibility under those conditions. A claim about better public decisions or transfer to other engagements would require further evidence.

The practice reaches the following conclusions for this service.

| Offering | Current use and limit |
| --- | --- |
| Existing one-session Method | Retained for the stated input-ready situation. Its broader late-input offering is withdrawn; the Method and other evidence are not erased. |
| Correction-and-return proposal | Retained as a candidate for a protected field trial; its intended join and observed exercise behaviour are recoverable. Any Method identification and field-fit conclusion must be established separately. |
| Wait for every possible input | Not selected for this service's present question because its unbounded delay defeats a timely qualified return; a named indispensable missing input can still require waiting or a blocker. |

The repertoire finding leaves choice of a pump, further investigation of the staged alternative and decisions about assistance or protection with the respective holders. The exercise supplies no observations of other practitioners receiving, using or retaining the proposed rule.

#### PSDA.16:5.2 - Non-contested development advice and a new software assistant

An advisory service already supports formed development questions without a dispute workshop. Its repertoire includes a source-bounded recommendation Method: recover the recipient, holder and horizon; inspect qualified specialist results; compare only live alternatives under the declared scheme; return a warranted direction, retained set, probe, request, blocker or abstention; and identify who has authority to make any later choice.

A new drafting assistant formats the same qualified premises and flags missing fields. If the adviser still performs the same qualification, comparison and return, the changed object is support. The practice checks access, confidentiality, capability and output reliability for that support; it does not create a new Method merely because the model version changed.

A different proposal lets the assistant select a preferred development direction from its own generated ranking and omit unranked candidates. That changes the reusable comparison and stopping rule. The practice cannot import the manual Method's evidence or call the proposal a harmless implementation detail.

The immediate repertoire decision is to retain the manual offering and withhold the stronger automated offering pending an exact candidate account, comparison basis and representative evidence. For the disputed claims in this case, a useful trial includes an absent whole-arrangement result, an unclosed provider alternative, and an evaluation that covers configuration A while the request concerns B. Success means the return preserves the correct gap and independently useful content, not merely that the text is fluent or shorter.

The trial also has to cover the human professional-service conditions that apply to its claimed use. Human career-assessment evidence does not establish an AI-holder result, and an organization's allocation evidence does not establish a person's learning transfer. No generic development-direction score bridges those differences.

The practice has assessed its repertoire. Advice for a particular client, deployment of the assistant and a finding about the whole opportunity-construction Method each need their own grounds. Any later choice belongs to its authorized holder.

#### PSDA.16:5.3 - A source update and a cheap non-use

A revised methodological source changes the conditions for a comparison procedure. The complete-data entry remains supported. The practice restricts incomplete-data use to the revised conditions. If the rule expressly excludes a case, that use is settled. If a material condition is unclear, identify the source question and limit the affected offering. Entries independent of the changed rule retain their grounds.

If the new source only changes layout or a locator while preserving the relied-on claims, update that description or access information under its direct guidance. If one current engagement simply needs an adequate existing Method, use the established assessment directly or use `PSDA.4` when fit for that engagement still needs work. Neither situation warrants a new professional Method.

A review reporting more published applications can justify looking for a promising candidate or an unexamined domain. It does not by itself change a local offering's evidence or justify retiring a less frequently published Method.

### PSDA.16:6 - Bias-Annotation

School loyalty and novelty bias pull in opposite directions. For a comparative claim, test the strongest applicable incumbent and a serious feasible alternative under representative conditions. A practice's available expertise is a real constraint, but it is not evidence that other Methods lack value.

Publication and success-reporting bias can hide failed, unpublished or culturally distant uses. Preserve the source search boundary and distinguish reported applications from representative evidence. A corpus dominated by particular journals cannot establish the absence of a practice elsewhere.

Combination bias treats more techniques as richer support. Inspect the meaning and cost of the joins. Automation bias treats a change in software as either automatically new or automatically harmless; recover whether reusable actions and stops changed.

### PSDA.16:7 - Conformance Checklist

**Recognition** asks whether the question concerns a recurring offering, an engagement-level choice, one source update, a support repair or a current follow-up. A single corrected applicability claim or a finding that the existing claim still holds may complete the repertoire task.

**Assurance** asks whether the offered Method or candidate and its claimed use are warranted by the applicable sources, observations and any relevant trials. A description can identify a way without proving fit; a constructed exercise can support feasibility without proving real-world effectiveness or transfer. Consequential trials and offerings retain their direct participant, competence, independence, safety, confidentiality and authority conditions.

| Check | Sufficient answer |
| --- | --- |
| Recurring use | Practitioner, situation, receiving result, material conditions and the required assessment or choice are established. |
| Method recovery | Actual reusable actions, joins and stops are recoverable; Method, candidate, description, support and local Work remain distinct. |
| Assessment and comparison | The grounds establish the offering’s fit or its remaining limit. If alternatives or a change are being assessed, identify their relevant difference, gain, effort and losses. |
| Source and evidence | Each action-changing offering has a claim-sized basis, qualification limits, relevant contrary evidence and any gap that limits the conclusion. |
| Trial claim | When a trial is used, its conditions and any needed comparator fit the claim. State what it shows about observation, feasibility, fit, causal effect or transfer. |
| Current offering | Retained, narrowed, candidate, withheld or withdrawn uses are usable by the next practitioner and do not hide different outcomes. |
| Lineage and refresh | Derivation has a basis; unproved cultural links remain gaps; only affected offerings reopen and recoverable history remains. |

A failed check may narrow one offering or retain a candidate for investigation while other entries stay usable.

### PSDA.16:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Treat one school as the permanent professional answer | Compare the actual contribution and assumptions against the recurring use and, for a comparative claim, against a serious alternative. |
| Turn every successful engagement into a new Method | Separate reusable semantics, one performance, support and applicability evidence. |
| Copy parent evidence to a hybrid | Identify the changed connections and assess the new claim under its own conditions. Trial it when the missing evidence matters and the trial is justified. |
| Count papers, downloads or satisfied participants as general effectiveness | State what was observed and the source boundary; identify what evidence the stronger claim would need. Seek it when the gain warrants the cost. |
| Offer a candidate as established because it has a complete description | Keep Method identification, trial status and fit claims separate. |
| Use participant agreement as proof that power and dissent were handled | Examine who could challenge, whose concerns entered the result, and what material disagreement remains. |
| Retire every entry after a source or tool update | Trace the changed claim to its actual offering and preserve independent uses. |
| Treat a repertoire or publication as cultural continuation | Use evidence of the relevant transmission, receiving enactment, recognition, selection, retention or loss for the cultural claim being made. |

### PSDA.16:9 - Consequences

Future practitioners gain a repertoire with stated conditions of use. Practitioners can reuse a Method for a supported situation, select an alternative, ask for a missing input or decline an unsupported extension. Changes become recoverable improvements or bounded experiments rather than accumulating workshop tricks.

The cost is maintaining meaningful applicability and evidence. Some promising candidates remain unoffered, some broad claims narrow, and some local successes support only the conditions observed. That restraint leaves room for development without presenting uncertainty as established practice.

### PSDA.16:10 - Rationale

Knowing a Method’s identity, a generic comparison or the members of a declared set may still leave a field question open. Which ways of working fit this practice’s recurring situations under its participation, value, evidence, authority and follow-up conditions? The answer can establish fit or inform a decision about the offering.

This is different from choosing a Method once. A future-use offering must preserve enough source, evidence, lineage and limits to survive transfer to another practitioner or engagement. It is also different from changing a culture: making a variant available does not establish the relations through which a community learns, enacts or retains it.

A changed premise can vindicate the incumbent's stop rather than defeat the Method. Start from the recurring work and the claim the change affects.

### PSDA.16:11 - SoTA-Echoing

The practice question is **how to develop a usable professional repertoire under heterogeneous situations and uneven evidence without turning either an incumbent school or each new technique into a universal answer**. The selected line is contribution-first comparison, explicit assumptions and joins, evidence representative of the claimed change, with further testing when warranted, and local source/evidence refresh. It accepts the cost of maintaining differentiated offerings; a simple established Method remains preferable when it covers the use at lower effort.

| Question and selected move | Serious alternative, defect and changed locus | Source role, limit and reopen condition |
| --- | --- | --- |
| How should unlike problem-structuring approaches enter the repertoire? **Adapt** explicit comparison of assumptions and contributions, with open family boundaries. | A familiar three-school catalogue is cheap to teach but hides differences that change participation and result use. Sections 4.1–4.3 compare the contribution rather than require a fixed membership list. | [Smith and Shaw (2019)](https://doi.org/10.1016/j.ejor.2018.05.003) is an exploratory conceptual comparator; [Kogetsidis (2025)](https://doi.org/10.1108/IJOA-08-2024-4746) is a later published-application line. Neither ranks Methods for this service. Reopen if a stronger account changes a load-bearing boundary or a representative case defeats the assumed fit. |
| Can current uptake evidence decide what to offer? **Reject that inference alone; adapt** reported applications as leads for candidates and source return. | A publication-frequency rule is inexpensive but confounds search coverage and visibility with practitioner use or worth. Sections 4.4, 4.7 and 5.3 preserve those distinctions. | [Kogetsidis (2026 online), Europe and beyond](https://doi.org/10.1108/EMJB-06-2025-0214), examines selected journals over 2010–2024. It is a current corpus-based comparator, not a census of practice or comparative effectiveness test. Reopen when new representative evidence changes the particular offering, not simply when another paper appears. |
| How should analytical advances change the repertoire? **Adapt** the specific value, model, uncertainty, sensitivity or information contribution needed by the use. | Adopting an entire analytical process can preserve coherence when its assumptions hold; importing it wholesale can require missing values, probability or evidence. Sections 4.2–4.4 retain exact inputs and joins. | [Borgonovo et al. (2026), decision analysis in OR](https://doi.org/10.1016/j.ejor.2025.05.023), is a contemporary synthesis of these contributions, explicitly not exhaustive of adjacent fields. It is not a Method-fit result for an engagement. Reopen on a materially better-supported analytical contribution or a failed input/return assumption. |
| What evidence warrants a Method improvement? **Adapt** examination of intervention configuration, interaction and outcomes at the claim's grain. | A technically valid output or favourable post-workshop rating is cheap to obtain but cannot alone identify the changed mechanism, comparative benefit or transfer. Sections 4.5 and 5.1 preserve trial type, comparator and confounding conditions. | [Franco et al. (2021), *Taking stock of behavioural OR*](https://doi.org/10.1016/j.ejor.2020.11.031), synthesizes different intervention-study questions and designs. It supplies no universal causal estimate or trial recipe. Reopen when a stronger representative design or counterexample changes the evidence required for the offering. |

### PSDA.16:12 - Relations

- `PSDA.15` supplies bounded follow-up evidence when it can affect the repertoire assessment or decision under the same relevant conditions and horizon. A local observation neither entails nor authorizes the repertoire result.
- Use `PSDA.4` to assess, choose or combine Methods for a particular engagement. Use `PSDA.16` to assess or change what can be offered across engagements.
- `PSDA.13`, `PSDA.5`, `PSDA.6`, `PSDA.7`, `PSDA.8`, `PSDA.9`, `PSDA.14`, `PSDA.15` and `PSDA.17` expose participation, alternative, comparison, recommendation, follow-up and arrangement requirements that a Method offering may need to preserve.
- `A.3.1` governs Method identification; `A.3.1.DR` recovers documentary contributions when their source meaning or status is unclear; `A.3.1.MR` recovers candidate ways from performance evidence. `A.3.2` governs a MethodDescription rather than admitting every multi-Method package.
- `A.3.1.MV` can supply qualified generic variant, derivation and non-variant maintenance guidance. Resemblance or shared repertoire vocabulary does not by itself establish a formal Method-specialization relation.
- Use `A.15.9` to reuse or, where worthwhile, obtain a qualified source or specialist contribution. Use `A.10` when the source-to-use account remains implicit or a reproducible account needed for this use is missing. Use `A.10.1` for the applicable affected-use question and `G.11` for currentness or refresh. The repertoire judgement uses the subject evidence.
- `G.5` declares a selector-facing result when that claim is live over identified members and grounds; it supplies neither a universal Method-family classification nor professional fit.
- For cultural relations, use `C.36`. A repertoire entry or local observation can supply evidence for `PSDA.18` when the question concerns generation, transmission, receiving enactment, recognition, selection, retention or loss. State what remains unobserved.
- An unavailable, stale, out-of-scope or incompatible input calls for a qualified direct source or the exact gap.

### PSDA.16:End

## PSDA.17 - Reconcile Simultaneous Problem-Structuring and Decision-Support Work

> **Type:** Method pattern (DPF)
> **Status:** Stable
>
> **Primary working result:** a finding about whether activities in the engagement can coexist and what their interaction means for the requested result. Where an arrangement is needed, identify a feasible proposal or authorized choice, its grounds, burden, unresolved conditions and reasons to reopen it.

### PSDA.17:1 - Problem frame

**Use this when** you need to establish whether or how activities in one decision-support engagement interfere, or to change their arrangement. An analyst needs stable assumptions while participants are correcting the question. A facilitator cannot address a consequential objection and rebuild the displayed model at the same moment. The evidence team qualifies one configuration while the service changes the configuration under consideration.

Start with the result and the interaction that could affect it. If a comparison closes before a material correction arrives, what conclusion does it still support? Identify the relationships that determine the answer. If a change is requested, assess feasible arrangements and act within the relevant remit.

Here **facilitation architecture** means how participation, modelling, inquiry, challenge and the return to the recipient work together in one engagement. A diagram describes that arrangement. A reusable Method can guide the work. To report how the arrangement operated on a particular occasion, use evidence of the interaction in question. A meeting record may establish who attended. To establish that a correction reached the model, trace the correction to the model used.

You can report whether the current arrangement preserves the required value, evidence, participation and authority conditions. You can also explain a limit, propose or authorize a change within your remit, or identify a missing result and its supplier where known. A continuing disagreement can itself be a valid finding.

Coinciding dates alone leave interference unestablished. If the work is independent, a report can state that finding and the activities may proceed on their own conditions. Use `PSDA.4` to assess a Method’s fit and `PSDA.13` when a claim needs facilitated inquiry within a workable arrangement. Use the responsible practice and authority for scheduling, specialist mediation, emergency command and decisions about the affected System.

### PSDA.17:2 - Problem

A sensible script can conceal an unsound engagement. Its “elicit, model, compare, recommend” order says little about people correcting claims during modelling, technical evidence arriving during discussion, or a sponsor controlling both participation and the receiving decision.

The same display can also carry incompatible readings. A causal sketch supports exploration; a calculation supports a bounded consequence claim; the closing slide appears to authorize action. If their different uses are hidden, completing the slide can look like completing all three results.

Local repairs then export the difficulty. Moving inquiry outside the meeting frees analytical time but adds participation effort and delays correction. Adding a challenger can broaden discussion while reducing facilitation capacity. Freezing a model stabilizes computation while excluding a changed premise. Trace these effects through to the receiving task. When a change is needed, the practitioner or authorized holder can use the findings to decide.

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

Examine the engagement against the result it requires and the conditions that support it. Distinguish an order that the work requires, actual overlap, and an interaction that defeats the result. If the task calls for a change, address the relationship that causes the conflict.

#### PSDA.17:4.1 - Anchor the engagement and the result at risk

For ongoing or completed work, use evidence of the relevant event and conditions. An objection may have reached the model, arrived after the comparison closed or remained unobserved. Distinguish observed work and a supported explanation from a suspected cause. For a proposal, assess the intended use and identify which observations could qualify any untested claim.

Establish the question, subject, scope, horizon and any relevant authority. Use participants, concerns, models and Method conditions that can affect the assessment or arrangement. Qualified results from `PSDA.11`, `PSDA.12`, `PSDA.1`, `PSDA.2`, `PSDA.3`, `PSDA.4` or `PSDA.13` may already supply these inputs under section 12.

Ask what a usable return must preserve. Examples include a materially different service concern, an interpretable model assumption, a qualified configuration-specific result, a workable challenge route, or the distinction between a recommendation and a choice by its authorized holder. A deadline limits the time available to meet those requirements.

If a suspected conflict concerns a different subject or use, establish that boundary before combining the work. Use available evidence to resolve a missing scope or authority fact. If it remains unknown, state how that limits the result. Seek the missing evidence when its value warrants the effort. If a new decision is required, identify who can make it.

#### PSDA.17:4.2 - Separate the structures that matter

Begin with the action whose contribution is unclear: for example, asking a participant to correct the meaning entered in a model. Use `B.1.5.EW` to explain what encompassing inquiry is being performed through the action in the episode, which constituent operations make it possible, and which conditions of the whole affect its performance. Follow each connection only as far as it changes this engagement. A missing skill, an unavailable contribution or a misunderstood operation may need a local correction without changing the whole engagement.

When several structures matter to the assessment or choice, use `C.32.MWA` to relate their accounts. The table shows examples of distinctions that can affect the conclusion.

| Account | Example in a decision-support engagement | Distinction to preserve |
| --- | --- | --- |
| Reusable Method and its composition | Attributed inquiry contributes claims to conditional analysis under specified joins. | A Method's parts and necessary order are not the meeting's calendar or every activity performed there. |
| Work, its constituents and its temporal relations | Correcting an attributed statement can be part of recovering a concern within an ongoing inquiry. Separately performed model revision may overlap that inquiry; a calculation can require an earlier result. | Explain the constituent connection and any before-and-after dependence separately. Timing alone establishes neither parthood nor a composite Method. |
| Decision subject and affected Systems | Pumping equipment, access routes, service recipients and later operating arrangements. | A hierarchy among these subjects is not a hierarchy of inquiry Methods or participants. |
| Participation and authority | Residents contribute concerns; specialists qualify premises; a board receives advice and holds the investment choice. | Being present, having expertise, facilitating discussion and having permission to decide are different. |
| Descriptions and models | A concern map, a capacity model and a comparison note describe different claims for different uses. | Document sections and model nodes are not world-side parts, actors or authorizations. |
| Professional-cultural continuation | A community later reuses or rejects the engagement's facilitation variant. | A local choice or visible workshop does not establish transmission, uptake or effectiveness. |

State the correspondence the conclusion relies on. For example, establish which participants can correct an assumption, which evidence qualifies a comparison, or who can change the receiving question. Identify any missing timing or attribution detail that limits the account.

Where the interaction is unclear, examine how the conditions of the whole affect the selected action and how the action contributes to the inquiry. Use available evidence of the operation. If a contribution is missing, consider obtaining it or rehearsing the combination under the time, access and cost conditions in §4.3. Stop when the supported finding and its limits answer the question.

Use the direct FPF pattern when a stronger relation claim matters: `A.3.1` for Method identity, `B.1.5` for Method composition, and the applicable Work or authority pattern for those distinct claims. A Method stack requires explained constituent connections, not a count of activities. If a changed whole no longer supports its old identity, reidentify it rather than preserving a convenient label.

#### PSDA.17:4.3 - Locate an interaction and its consequences

Establish whether one contribution weakens a condition another needs. Simultaneous modelling and discussion are compatible with independent work. If the only modeller also controls the meeting, a contested assumption may be recorded before its source can correct it. Check whether that occurred or remains a risk.

Trace an interference to the conclusion or work it affects. It may exclude an alternative, change an attributed value, invalidate evidence use, hide dissent, prevent participation or exceed the remit. Distinguish technical limits, value differences, evidence gaps and authority disputes so that the recipient can use each finding.

Establish what the activities share and whether sharing impairs either contribution. This might be an individual’s attention, a model, source data, access to participants, a decision horizon or a closing rule. A common source may support independent work without either activity consuming the other’s capacity. A practitioner may trace the interaction directly or use an available specialist result that answers the missing question.

If the interaction is uncertain, assess what can be concluded now. When a further answer could change the requested finding, its grounds or a feasible next action, compare its likely contribution with the cost, delay and displaced work under `C.11.DUA`. Use `A.15.9` for a needed external contribution. A qualified existing observation may settle the question. Limit the unsupported claim and preserve independently supported work.

#### PSDA.17:4.4 - Assess the arrangement and construct alternatives when needed

Assess the current or proposed arrangement against the receiving task. If the question is whether a specific interference exists, give the evidence, consequence or remaining limit. When a remedy or comparison is requested, identify feasible ways to change the affected relationship and compare material alternatives where available.

A local separation can reserve discussion time while calculation pauses. Parallel inquiry and modelling can use explicit exchange points for consequential changes. Separate contribution channels can preserve a protected or unavailable participant's input, provided a usable correction route exists. A simpler provisional model can support discussion while a specialist develops the stronger analysis elsewhere. A different allocation of modelling and facilitation can remove an attention conflict, if the required people and capabilities are available.

State what each arrangement preserves, what it can produce and any condition it cannot yet satisfy, and who bears the extra work, delay or loss. A jointly edited model is not always preferable; when inputs and meanings are stable, bounded expert analysis can be sufficient. In fully serial work, someone may become unavailable while another contribution is completed.

When the participants share the same relevant perspective and a missing perspective could change the inquiry, consider a prepared content challenger alongside a separate facilitator. Make that contribution explicit and source-supported; allow the group to decline it. It does not confer representation or consent on behalf of absent people. Its preparation and facilitation burden may make another participation route preferable.

Test whether the proposed change stays within the selected Method's permissible variation. A change from spoken to confirmed written inquiry may preserve the Method; replacing participant confirmation with a sponsor's interpretation does not. When the change leaves the Method’s permissible variation, use `PSDA.4` or an existing qualified assessment to examine the proposed Method and its fit.

#### PSDA.17:4.5 - Return the finding and make any authorized choice

Assess each relevant arrangement against the question it must answer. Check material conditions for participation, interpretation, model and evidence use, support, timing and authority. Treat a protected condition as a requirement unless an applicable rule authorizes a trade-off. More output or a shorter meeting cannot supply missing representation or evidence.

Return a finding or proposal when that meets the assignment. When a choice is needed, apply an existing rule or decide within your remit. For a new commitment of another party’s resources, a changed participation duty or a change to the receiving decision, establish applicable authority and obtain any required decision from its holder. Distinguish a proposal, its authorization and its implementation. The `C.32.MWA` synthesis can inform that choice.

State the result and its grounds. For a selection, explain what the chosen or retained arrangement preserves, what a material alternative would change and what still limits the return. If no arrangement meets the requirements, identify the remaining gap and any independent part that still serves.

Identify who has authority to decide how the inquiry is conducted and the basis for that authority. Choosing a pump, changing organizational rights or deploying a model requires authority for the corresponding action. To report agreement with advice, use evidence of the relevant party’s response.

#### PSDA.17:4.6 - Judge the changed interaction and hand on its conditions

Use available observations to assess the interaction relevant to the question. For example, did a correction reach the comparison on time, could a participant challenge the representation, or did separate facilitation free the analyst’s attention? For a proposed arrangement, state what its conditions support. Consider a further observation under section 4.3 when its attainable answer warrants the cost.

A rehearsal supports a prospective arrangement only at its tested scope. For a change used in ongoing work, inspect the resulting contribution and any burden moved elsewhere. A smoother meeting or a completed document alone is not evidence that the material conflict was resolved.

Return the requested finding, proposal or decision in a form the recipient can use. Explain the arrangement, the grounds and scope of the result, and any unresolved condition. Include the authority, a needed follow-up or an informative observation when the receiving task depends on it.

Carry only consequential constraints into follow-up. For example, a corrected service assumption must reach the named comparison owner; an observation about another configuration does not refresh this result. Use `PSDA.15` if a follow-up question remains. An existing arrangement may already satisfy it. Evidence from this local variant may inform `PSDA.18`, but cultural continuation requires its own observations.

Reopen when the receiving question, a material participant or premise, the model use, the arrangement's support, or the permitted decision changes; when the chosen exchange fails; or when a moved burden defeats another necessary condition.

#### PSDA.17:4.7 - What changes in practice

The practitioner can explain why the contributions can proceed together or which relationship threatens the required result. A necessary sequence can be retained. An unsupported conclusion can be limited. Where change is warranted, the explanation identifies the relationship the change must address.

### PSDA.17:5 - Archetypal Grounding

#### PSDA.17:5.1 - A flood-pump inquiry cannot freeze away a service concern

This illustrative case continues the bounded attributed-inquiry and conditional-analysis Method. The board retains the investment choice; the engagement lead may arrange inquiry and model work within the agreed participation and resource conditions. In this case a facilitator and an analyst are available.

The analyst is preparing conditional comparisons; the working list includes fixed, mobile and staged pumping arrangements. The staged candidate still lacks a qualified consequence result. A separately consulted group has not yet corrected the rendering of its reachable-assistance concern. The current plan freezes the comparison before that correction can arrive. The facilitator is also expected to explain the calculations during the only discussion period. A finished comparison could therefore look complete while answering only the property-protection reading.

The relevant structures differ. Attributed inquiry and conditional analysis are Method contributions. In this case, the work overlaps. The resident group, analyst and board have different participation and authority relations. A service-concern map and a hydraulic model preserve different claims. Investment implementation is later work, not a final level of the inquiry.

Consider the moment when the facilitator asks a resident to correct an attributed statement. Asking, interpreting the answer and confirming the amended wording are constituents of recovering that service concern; this recovery is part of the problem-structuring engagement now in progress. Suppose the resident means that assistance must reach people when the road is flooded, but the model records only protected property. Accurate transcription is insufficient: the missing connection is the translation of the confirmed concern into the model's question. The facilitator and analyst must preserve that meaning in the comparison or identify the service question it cannot answer. If they cannot make that translation, they need the relevant modelling contribution, not more accurate typing. The active exchange performs part of the inquiry while separate calculation can continue elsewhere.

The lead compares three arrangements:

| Arrangement | What it can preserve | Consequence for this case |
| --- | --- | --- |
| Keep the early freeze and explain the completed model in one session. | Analytical stability and the existing timetable. | Cannot support a claim that the uncorrected service concern was considered. A narrower technical return remains possible. |
| Stop every analysis until every participation response is complete. | Allows those responses to precede analysis. | Delays independent calculations and still cannot promise that every person will respond. |
| Continue bounded analysis while the facilitator maintains inquiry; join material corrections before the affected comparison closes. | Existing qualified calculations, a real correction route and separate attention to discussion. | Requires coordination effort and a clearly limited return if the correction or its technical consequence remains unresolved. |

Under the supplied remit and available support, the lead selects the third arrangement. The facilitator obtains correction of the attributed concern through its agreed channel. The analyst identifies which consequence claims that correction could change and carries unaffected calculations forward. The next return distinguishes qualified calculations, unresolved service claims and the exact access question. If the correction arrives too late for a supported comparison, the brief retains that limitation instead of silently dropping the concern.

The lead gives this direction within the agreed remit.

> Keep inquiry and conditional analysis in parallel, with the facilitator handling claim correction and the analyst handling the affected model use. Close each comparison only with its current service meaning and evidence limits visible. Preserve the mobile-access gap and any unanswered contribution in the board's return. Authority for the investment choice remains with the board.

In the chosen arrangement, the facilitator and analyst must reconcile the corrected meaning with the consequence account, and the board may receive a narrower answer. The lead follows one corrected statement into the draft comparison and checks whether the dependent conclusion is retained on adequate grounds, revised or left open. That test does not establish road access, district-wide agreement or a superior pump.

If separate analytical support becomes unavailable, the lead must reconsider the arrangement—for example by pausing calculation during the material discussion.

#### PSDA.17:5.2 - A non-contested advice question with a moving evidence basis

A committee asks a separate advisory team for a ninety-day service-development comparison. No disagreement about the question is reported. Internal development and a human–AI support arrangement are live candidates; the organization's allocation and AI evaluation results remain specialist inputs.

During preparation, the system owner changes the proposed AI configuration from A to B. The evaluation already supplied concerns A. Meanwhile, the allocation analysis can still answer an independent question about internal development. The original plan waits for one whole “evidence package” and then issues one complete comparison. Its all-or-nothing join either delays useful work or tempts the adviser to pass A's result into B's claim.

The team considers keeping a historical-A comparison, waiting for every B premise before any return, and separating the returns by which premises each result needs. The first does not answer the committee's now-B question. The second remains possible but withholds the independent allocation result. Within its agreed control of analysis and delivery, the team retains the qualified internal-development contribution and keeps the cross-candidate comparison open wherever B is material. It considers a B qualification only if an obtainable result could improve the recommendation or its grounds within the receiving window and warrants the acquisition burden. Otherwise it returns the useful internal-development result and the unresolved B limitation.

The arrangement names the configuration owner who reports a further change, the specialist result each claim can consume, the person assembling the comparison and the condition for closing it. It does not freeze the operating system, prevent its owner from changing B, or turn the available internal-development result into the recommended direction.

The test substitutes another A-only result at the receiving join. It supports the relevant A claim. Without grounds for transfer it cannot establish B’s performance, while the independent contribution stays usable. A later adequate B result can close that particular gap. A further change of subject or horizon reopens only the affected use.

Here the participants can keep working results separate by the premises each one needs. Their decision governs the return of that work. Claims about AI performance or safety, human learning or organizational feasibility need their own evidence. Deployment also needs its applicable authority.

#### PSDA.17:5.3 - Overlap without an architecture problem

Two analysts examine different uncertainties for an unchanged question. Both can read the adequate source materials at the same time. Neither consumes the other's result, blocks participation or changes a shared condition. Their calendars overlap, but no material interference has been identified. That finding answers a question about interference. The two studies can proceed under their existing conditions.

### PSDA.17:6 - Bias-Annotation

**Scope:** arrangements of problem-structuring and decision-support work for a named engagement. The pattern does not govern every concurrent project activity.

Watch for analytical capture: the easiest-to-compute account becomes the whole question. Watch also for participation romanticism: a joint session is credited with representation, expertise or agreement it did not establish. Trace the claim to its contributor, evidence and authority. Identify any missing or protected participation that limits it.

Architectural tidiness can hide moved burden. Inspect the participant, specialist or recipient who would bear the cost of a proposed change, or who bore it after implementation. A successful local variant remains local evidence, not proof that a profession has adopted it.

### PSDA.17:7 - Conformance Checklist

| Check | Passing observation |
| --- | --- |
| Interaction | The relevant result and conditions are identified. A claimed conflict has a basis. Evidence may also establish independent work or leave the interaction uncertain. |
| Evidence | Evidence of performed work is distinguished from a suspected mechanism. A proposed arrangement identifies its conditions for use and the evidence needed for any untested claim. |
| Non-isomorphic structures | Only relevant Method, work, subject, participation/authority, model/description or cultural accounts are used; their important relations and losses remain explicit. |
| Alternatives | If a comparison or remedy is needed, assess feasible arrangements for the same use, including support, effort and burden moved elsewhere. A factual account of the interaction can stand on its own. |
| Finding or decision | The conclusion states what the evidence supports. Any selection is made under its applicable authority. A proposed change, missing authorization or evidence limit is identified where relevant. |
| Intact Method and source use | Changes outside a Method's permitted variation return to Method selection; a new configuration does not inherit an old premise without qualification. |
| Interaction judgement | The evidence supports the claimed dependence, interference, change or absence of a material conflict. State remaining limits. For a proposed further observation, weigh its attainable contribution and burden. |
| Usable result | The recipient can recover the result, its grounds and any consequential limits, follow-up or conditions for a later reassessment. |

### PSDA.17:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Better move |
| --- | --- | --- |
| Turn the agenda into the architecture. | A sequence hides actual overlap, shared attention and authority conditions. | Recover the relations that change the current result. |
| Solve the model and declare the engagement complete. | Technical closure can exclude an unanswered interpretation or participation condition. | Qualify the technical return and preserve the missing contribution. |
| Separate everything to remove friction. | Extra handoffs can increase delay, exclusion and inconsistent assumptions. | Compare the moved burden with the interference the separation would avoid, or the interference it did remove. |
| Add a challenger and claim absent people were represented. | A prepared perspective does not establish their participation or consent. | Keep the source and representation limit; use a qualified existing contribution, obtain a needed one where feasible, or state the representation gap. |
| Reuse the nearest available evidence package. | Its subject, version or horizon can differ from the current claim. | Qualify each consequential join or return its exact gap. |
| Declare a new culture after one workshop. | Local enactment supplies no observation of later transmission or retention. | Use the local evidence for a cultural question only to the extent that it supports the relation at issue. |

### PSDA.17:9 - Consequences

The engagement can return useful partial results without hiding how its work was arranged. Participants' corrections, specialists' premises and decision owners' authority remain connected but distinct. Necessary order is preserved without forcing all modelling, inquiry and observation into that order.

Coordination can cost time and can delay or narrow the result. Separate roles need capacity, separate channels need a usable way to pass the work, and a specialist or decision holder may still need to resolve a particular question. State the grounds and limits that the recipient can rely on.

### PSDA.17:10 - Rationale

Method choice and faithful facilitation do not by themselves settle whether their enactment can satisfy several conditions at once. The same adequate inquiry Method may fail under one allocation of attention or one result-closing rule and remain usable under another. Conversely, an apparent scheduling change can replace a Method's essential confirmation or evidence condition.

The pattern therefore starts at one threatened result, recovers selected relationships, and compares arrangements through their consequences. A constituent can perform part of ongoing inquiry while other work overlaps it or supplies a later result. Recovering that vertical connection can locate a missing ability or semantic join that a different timetable would leave unresolved. This distinguishes structural interference from an ordinary claim disagreement and avoids reopening the entire engagement after each correction.

Retain a simple sequence when it preserves the required work. Report a material interaction when it changes the conclusion or the grounds for it. A proposed arrangement can identify how to handle that interaction. To claim it worked, use evidence from the stated operating conditions.

### PSDA.17:11 - SoTA-Echoing

**Practice question.** How can a practitioner establish whether modelling, participation and closing a result constrain one another, and decide how to act when they do? Establish whether an interaction matters in this situation. If a different arrangement is needed, assess the feasible options, which may include an ordered Method, expert analysis or more intensive joint work. Further testing depends on the claim and available evidence.

| Question and selected answer | Serious alternative, defect and decision | Source role, limits and changed locus | Reopen condition |
| --- | --- | --- | --- |
| Which order can guide this engagement? Preserve supported dependencies while inspecting the actual model-building and participation interactions. | A fixed sequence is useful when it fits. **Adapt** a multi-structure account where that sequence hides interference; accept the extra coordination cost only for the threatened result. | Franco, Hämäläinen, Rouwette and Leppänen's [2021 behavioural-OR review](https://doi.org/10.1016/j.ejor.2020.11.031), especially §5.2, is a best-known-line synthesis and counterweight to an all-linear or all-nonlinear story: it reports relatively linear engagement paths alongside more complex model-building paths and situated facilitation. Its heterogeneous studies do not validate one arrangement here. This changes 4.1–4.3 and the local test in 4.6. | New comparative evidence or a failed join shows that the selected arrangement loses a consequential result or imposes unnecessary coordination. |
| Must modelling be completed before participants can affect it? Couple the contributions when their interaction changes the model's receiving use; retain expert analysis for a sufficient bounded technical question. | Expert-led production avoids some interaction cost. Fully joint modelling can expose meaning while consuming scarce attention. **Adapt**, rather than universally select, facilitated modelling and inspect consequential interpretations at their joins. | Franco and Montibeller's [2010 review](https://doi.org/10.1016/j.ejor.2009.09.030) supplies the operative expert/facilitated contrast, not a universal superiority claim. Franco and Nielsen's [2018 four-workshop study](https://doi.org/10.1007/s10726-018-9577-7) supplies situated evidence about facilitator formulations shaping interaction, not guaranteed consensus. These comparison contributions change 4.3–4.4 and 5.1. | Actual participation, meaning or support conditions defeat the proposed coupling, or a cheaper direct analysis now closes the use. |
| What if a homogeneous group lacks a material perspective? Consider a prepared challenge with distinct facilitation, not an invented voice for absent people. | Asking the same participants to argue both sides may add no missing information. **Adapt** the conditional challenge arrangement; **reject** its use as substitute participation or a universal staffing rule. | Cunico, Zimmermann and Videira's [2024 study, online 2023](https://doi.org/10.1080/01605682.2023.2263101), §§3 and 7, offers a serious alternative through one exploratory group-model-building application. Preparation, facilitator workload and role ambiguity are explicit trade-offs; effectiveness does not transfer automatically. It bounds 4.4 and the corresponding anti-pattern. | Direct participation becomes feasible, adequate perspective sources are absent, or the changed role damages inquiry or exceeds available support. |
| Is one model, agenda or hierarchy enough to settle the arrangement? Retain different structures through their warranted relationships. | A single view is cheaper when it preserves the needed distinction. **Adopt** the current `C.32.MWA` synthesis when it does not; **reject** layout as proof of a practice relation. | `C.32.MWA` supplies the common obtaining/prospective and several-structure Method. Here the applied decision concerns modelling, participation, challenge and return conditions; the synthesis alone supplies neither professional premises nor decision authority. This governs 4.1–4.2 and 4.5. | A direct relation or domain contribution changes the synthesis, or the conflict no longer needs several structures. |

These comparisons support bounded moves, not a universal workshop design or evidence of institutional effectiveness. Source change reopens the affected move or limit; it does not require every otherwise adequate engagement to restart.

### PSDA.17:12 - Relations

- **`PSDA.11` and `PSDA.2` → `PSDA.17`.** The engagement question and scope can frame the assessment of this arrangement when they concern the same subject and receiving use. Use them directly if available.
- **`PSDA.12` → `PSDA.17`:** the participation and concern account supplies only the participants and concerns material here; inclusion settles neither formulation nor authority.
- **`PSDA.1` → `PSDA.17`:** plural formulations enter where their inquiry changes the candidate arrangements. Agreement is not required and dissent remains explicit.
- **`PSDA.3` → `PSDA.17`:** the multi-model account is used only where it discriminates arrangement alternatives or claims.
- **`PSDA.4` → `PSDA.17`:** the engagement Method and limits apply only to the named situation and qualification window. Availability establishes neither fit, enactment nor cultural uptake.
- **`PSDA.13` → `PSDA.17`.** Use evidence of agreement or dispute when the participation condition affects the finding. Authority to select an arrangement is a separate question.
- **`PSDA.17` → `PSDA.15`.** Use the arrangement finding as a constraint when it affects a follow-up question. Assess the existing follow-up or compare alternatives if that question still needs work.
- **`PSDA.17` → `PSDA.18`:** the local decision may supply evidence or a variant for a named cultural-continuation question. Visibility proves no generation, transmission, enactment, recognition, selection, retention or effectiveness; absent evidence leaves the corresponding link unproved.
- **Direct FPF and specialist returns:** `B.1.5.EW` recovers how an action performs encompassing work and which constituents make it possible; `C.32.MWA` supplies the several-structure synthesis. `C.11.DUA` selects worthwhile further investigation, and `A.15.9` supports reuse or worthwhile acquisition of an outside-practice result. Applicable Method, Work, authority and evidence patterns govern their own claims. If a required input is absent, stale, out of scope or incompatible, use a qualified direct result or retain the exact gap.

### PSDA.17:End

## PSDA.18 - Deliberately Continue and Change Problem-Structuring and Decision-Support Culture

> **Type:** Method pattern (DPF)
> **Status:** Stable
>
> **Primary working result:** an account of how a specified decision-support practice was passed on, used, retained or lost across practitioners, with its evidence and limits. When continuation is at issue, return the feasible options, any authorized decision and its conditions. Report later observations when available.

### PSDA.18:1 - Problem frame

**Use this when** you need to establish how decision-support practice was passed on, recognized, chosen or retained across practitioners and engagements, or to decide whether and how to continue it. A new team copies a recommendation format but loses its uncertainty and dissent. A capable facilitator leaves, and the remaining library does not preserve how to handle a contested contribution. A service rewards decisive-looking recommendations so consistently that honest blockers stop appearing in its examples.

This method examines how particular decision-support Methods, judgements, descriptions and norms are generated, transmitted, recognized, selected, remembered, retained or lost. Identify the practitioners and arrangements involved in the relation under study.

For example, a service might say, “In our flood-advice service, new facilitators learn from case examples and observation; the examples retain the models but omit why an unresolved service concern limited the recommendation; we are deciding whether to change the receiving practice exercise.”

Use the practitioners’ work and sources to establish the relation the question concerns. Existing observations may show what reached a receiving team and how it used the material. For a continuation decision, consider retaining, changing, branching, investigating or stopping where those options are feasible. Seek more evidence when its attainable contribution warrants the effort.

A receiving practitioner can preserve an important judgement or adapt it to local conditions. A service can compare the intended change with observed practice, including a distinction that failed to survive transfer.

For choosing a Method in one engagement use `PSDA.4`. For a repertoire offering use `PSDA.16`, and for a current conflict use `PSDA.17`. Enter the cultural inquiry when generation, receiving use, recognition, selection, memory, retention or loss across practitioners matters. Publication, attendance, a client’s capability development and the evolution of a non-cultural population each have their own subject.

### PSDA.18:2 - Problem

A practice can preserve its visible forms while losing the reasons that made them useful. A concern map becomes a diagram to complete. A conditional comparison becomes an unconditional recommendation. A workshop's apparent agreement becomes a claim that affected people were represented. These changes can travel through teaching, templates, peer imitation, commissioning and recognition even when nobody intends them.

The reverse failure is to resist every variation in the name of fidelity. A receiving team faces different access, values, uncertainty or authority conditions, but is told to reproduce the original format. It may preserve the carrier while making the Method unusable.

Establish what was available, what reached a receiving practitioner, what they did and what they selected or retained. Examine subsequent consequences when they matter. A publication record can establish that an edition was issued. An observed engagement supports a conclusion about that engagement. A proposed wider change needs grounds at its own scope.

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

Start with the practice and the relation at issue. For an account of past practice, return the supported observation and its limits. If continuation is at issue, assess the feasible arrangements and their consequences. Identify who can choose. Distinguish what was decided, what was carried out and what happened in the receiving practice.

#### PSDA.18:4.1 - Name the current practice, population and intended consequence

Identify the Method or variant as practiced in the engagement or community. Name the practitioner population, place, period, relevant carriers and the professional result whose continuation is in question.

For example, the relevant practice may be a municipal team's attributed inquiry and conditional comparison, carried through observed facilitation, concern maps, model explanations and bounded recommendation accounts. The question is whether another facilitation team can preserve those contributions in its receiving engagements. A count of published PSM applications would leave that receiving use open.

State the professional consequence at issue. Material dissent might remain attributable, a missing premise might stay visible, or a receiving team might preserve the difference between a conditional comparison and an overall recommendation. Assess relevant costs in time, access, capability or analytical independence.

For a proposed intervention, establish who can decide and the scope of their authority. A precise Agent claim under `A.13` needs the System, local agential kind, criterion, evidence of classification, obtaining assignment, scope, situation and window. Authority to change facilitation, training, commissioning or publication applies to the specified work. A client investment or another community’s decision has its own holder.

If the question concerns one receiving exercise, limit the inquiry to the practice and conditions that affect that exercise. When a needed decision or permission is missing, identify it. Use the direct route when the question concerns something else.

Use C.36 for the cultural relation in question, C.36.RP for sustaining and renewing shared ways, and C.36.MC when the Method culture itself needs qualification or development. For decision-support work, examine how later inquiry handles attributed meanings, material dissent, uncertainty and qualified recommendations.

#### PSDA.18:4.2 - Recover what the evidence actually shows

Use `C.36` for the cultural relations and their distinctions. Begin with concrete practice evidence: the changed instruction, observed interaction, qualified account of learning, receiving enactment, selection decision, retained example or demonstrated loss. Label expert estimates and conjectures. A lack of a population study does not prohibit a useful bounded judgement.

Use the questions below for the relation you need to establish.

| Relation at issue | Evidence to recover | What the evidence does not establish alone |
| --- | --- | --- |
| Variant generation | The proposed or actual difference in the reusable way, its source and conditions, or the changed teaching, recognition or memory arrangement. | A name or file can identify a proposal. Use evidence of the changed reusable action and its performance for a claim of enactment. |
| Transmission | What contribution passed from which source through which carrier or interaction to which receiving practitioner, when and under what interpretation. | Sending or downloading a document does not prove understanding, skill or receiving enactment. |
| Receiving enactment | A bounded actual occurrence in which the receiving practitioner followed the identified Method, with its meaningful conditions and result limits. | Attendance, stated intention or a copied output does not prove that the Method was followed. |
| Recognition and selection | Who recognized which contribution under what criterion, and which practitioner or institution selected which variant for what use. | A local project choice, credential or endorsement does not prove population-wide selection or fitness. |
| Memory | A recoverable description, exemplar, explanation or other carrier that preserves the distinction needed for reuse. | An accessible archive does not show that practitioners retain the ability or habit of using it. |
| Retention or loss | Evidence over the stated interval and relevant opportunities that a contribution continued, changed or ceased to be usable or enacted. | If no opportunity arose, non-use leaves loss unresolved. Silence or a missing publication also leaves the state of practice open. |
| Mediation | The actual tool, platform, community or publication arrangement and the visibility, interpretation, recognition or selection relation it changes. | A prominent display, recommender output or high access count does not establish value, control or cultural success. |

Give the population and period each observation covers. A workshop account may support one adaptation. A review of publications may locate relevant cases. A forecast or claim about a wider population needs evidence and uncertainty appropriate to that scope.

Use a qualified `PSDA.16` variant, lineage or finding when it supports the cultural question. An offering can be available to a team without reaching it. `PSDA.17` may establish how a local arrangement changed. To establish that another team learned the change, use evidence of its receiving work. If the available input is missing, stale or incompatible, identify the unsupported link or obtain a suitable input when warranted.

An observation of interaction or receiving use can answer its cultural question directly. To recognize an occurrence as `U.Work`, establish each actual performer’s `A.13` basis and the full `A.15.1` basis for the occurrence. This includes its common constructive components under `A.1:4.2`, performance history, enacted Method, extent and obtaining containing-System relation. For precise assignment-bound attribution use `F.6`. Missing attribution leaves independently established Work available.

A small permitted intervention can be warranted while its cause remains open. If a facilitator drops a concern, possible explanations include an incomplete example, changed participation, lack of skill, time pressure or rewards for a quick positive answer. Test an explanation when it matters to the requested causal finding, its grounds or the choice of change. Use `C.11.DUA` to assess the attainable contribution and full burden of further inquiry.

#### PSDA.18:4.3 - Compare continuation options at the affected relation

When assessing continuation, compare the feasible options that matter to this use. These may include keeping the arrangement, changing a material relation, retaining a separate branch, or stopping or reverting an intervention.

| Option | Useful question | Typical decision-support consequence |
| --- | --- | --- |
| Retain the present arrangement | Is the apparent failure outside its promised use, or is the current way already adequate at lower effort? | Preserve a useful narrow Method and avoid disrupting practiced judgement. |
| Change one arrangement | Would a change to facilitation, teaching, peer discussion, commissioning, recognition or source presentation address the identified mechanism? | Make the missing participation, interpretation or qualified-return move available in receiving practice. |
| Keep a separate branch | Do different access, participant or evidence conditions warrant different supported ways? | Preserve plural practice without pretending that all variants fit the same engagement. |
| Stop or revert | Does the change remove a protected condition, exceed authority, create an unmanageable burden or fail its stated purpose? | Return to a qualified arrangement, narrow the offering, or leave the receiving result explicitly blocked. |

Explain why the proposed change might work and what it would cost. Replacing a template may improve access but leave tacit facilitation judgement unaddressed. A guided practice exercise may expose that judgement but require an experienced facilitator and protected material. Changing recognition to include a well-grounded blocker can make honest returns visible, but a new checklist can also become another ritual.

A bundle of teaching, exemplar and peer-feedback changes may be one usable arrangement. When tried together, record what occurred under the combined arrangement. Attributing the outcome to the combination or to one component requires evidence for the corresponding causal claim. If the reusable decision-support action itself changes, return that Method or variant question to `PSDA.16`; cultural desirability does not admit a proposed Method.

Keep the receiver's circumstances in the comparison. Translation, remote participation, professional-service conditions, available expertise and the ability to challenge an interpretation can change the required arrangement. Check whether the receiving practitioners can use the distinctions the task requires.

#### PSDA.18:4.4 - Choose continuation or a bounded intervention

For a continuation choice, use the feasible options, intended participation or recommendation outcome, protected conditions, resources and period. Identify the holder and any applicable decision already in force. For a new decision, the holder can retain the present arrangement or choose a change within that authority. Give the conditions for retaining, stopping, narrowing or redirecting the chosen course.

Use `C.11` for an already formed bounded choice. Before developing or commissioning a new inquiry, use `C.11.DUA` to compare its attainable contribution with formulation, design, participant and facilitator time, access, interpretation, delay and displaced work. A missing formulation, alternative or probe-design result can remain the limit on a stronger answer; acquire it only when the current question warrants that work.

Keep the choice local. A team may change its own case discussion, mentor arrangement or presentation of examples under its remit. It cannot thereby compel another team to adopt a Method, expose protected client information, certify practitioners, or decide the client's investment. An invitation, a receiving team's agreement and a service-wide rule have different authority and participation consequences.

Match the basis to the decision. A reversible exercise with non-sensitive material may proceed on a stated mechanism hypothesis and modest evidence. A consequential service change may need stronger grounds for capability, professional practice, participant protection and governance. Use applicable existing results. Obtain missing support or state the condition preventing the change.

Retain any serious alternative and expected loss that matter to the choice. The useful return can be “try one receiving exercise for this cohort, keep the present route for experienced staff, and do not extend the change until an independent receiving use has been observed.” That is a completed bounded decision even though its later effect remains unknown.

#### PSDA.18:4.5 - Perform and observe only the intervention that was chosen

When the task includes carrying out a chosen intervention, organize the teaching, facilitation, community, recognition or publication work it requires. Report which actions took place. A planned tutorial, posted file and completed guided exercise each support a different claim.

For a formal `U.Work` claim, use the complete basis in `:4.2`. A trial of a proposed decision-support variant can follow an already identified trial or teaching Method. Evidence of its performance can establish use of that trial or teaching Method on the stated occasion. The proposed variant still needs its own basis for admission as a `U.Method`.

Establish the receiving use from evidence of the work in question. A contemporaneous recommendation can show whether a corrected concern was retained or a comparison stayed within its stated assumptions. For a learning question, one option is to have a practitioner explain the missing premise or justify a qualified return under the relevant conditions. Use the exercise when a response of that kind is needed and suitable for the population and situation.

In a consequential decision, preserve access, competence, confidentiality, opportunities to challenge, source-use rules and fallback arrangements. For practice, choose an authorized original, redacted or constructed case that preserves the relevant distinction. State what the substitute cannot test.

Identify what changed in a claimed intervention, such as the example set, a display rule or practitioner action. For a formal change or effect claim, use `A.3.4` and the applicable direct effect or Work-to-change predicate. Report separately what was carried out, what was observed and what evidence connects the two.

#### PSDA.18:4.6 - Test the receiving consequence and competing explanations

When assessing a consequence, compare the observation with the intended result at the same scope. Report the observed result, including an unsuccessful attempt or an outcome still unknown.

| Professional consequence | A useful observation | An unsupported stronger inference |
| --- | --- | --- |
| Participation and dissent | A material affected concern can enter, be corrected and remain attributable in the receiving inquiry. | More attendees or fewer objections means equal influence or consensus. |
| Uncertainty and evidence | The practitioner preserves the relevant configuration, horizon, qualification and unclosed premise. | A complete model or fluent explanation means every input is adequate. |
| Recommendation return | The account preserves the compared subset, inference, dissent, limits and the appropriate direction, set, probe, request, blocker or abstention. | A signed-off report is necessarily useful advice or an authorized later choice. |
| Receiving use | The named receiver can recover what this result permits and where it must return. | Delivery, access or a positive reaction proves understanding, reliance, implementation or effect. |
| Continuation | Evidence of a later use shows what the receiving practitioners used, under what conditions and with what help. A claim of independent performance or retention across an interval needs evidence under the corresponding assistance, timing and opportunity conditions. | One coached performance proves long-term retention or practice-wide adoption. |

Distinguish a useful local outcome from an explanation of why it occurred. An improved return might reflect the exercise, prior experience, a more skilled facilitator, additional time, a different problem, easier evidence or changed authority. Identify the alternatives the evidence leaves open.

When the next question is how this practice may develop, retain credible rivals whose difference can change the answer; do not manufacture a fixed number. Return the supported forecast or continuation with its material uncertainty. Select a new discriminating observation only when it is obtainable and worthwhile for that question. For example, an explanation-rich case library may support later independent use, or its effect may disappear without a mentor. A later uncoached case can inform that distinction; it does not isolate every causal influence.

Use `B.5` and `B.5.2` for hypotheses and testable consequences, `C.28` for an actual causal claim, and `A.3.3` only if a state-space and transition-law claim is needed. An ordinary uncertainty about continuation does not require a mathematical cultural-evolution model.

Use the sources that can show what was preserved, excluded or made harder. Existing work and records may establish an operational change. For a participant’s experience or disagreement, use their account or seek it where needed and feasible. Preserve material dissent about the intervention and distinguish a reported experience from a claim about its cause.

#### PSDA.18:4.7 - Return the cultural account and keep its limits usable

Return the account needed for the inquiry or decision. Include the following details where they bear on that use.

- the current practice, Method or variant, population, place, period and carriers;
- the cultural relation that justified attention and the evidence or labelled estimate;
- any bounded continuation decision, its holder and authority, alternatives and accepted costs that matter to it;
- what was proposed, performed or changed, stated separately;
- the available receiving-enactment and decision-support observations, with the limits that affect reliance;
- material uncertainty about transmission, recognition, selection, retention, loss or cause;
- the supported finding and, if further work is needed, its scope, recipient or conditions for stopping;

A decision can be supported despite uncertainty about later effects. An observation can establish a receiving use while leaving its cause open. If further observation is selected, state its question and conditions.

Use `PSDA.16` if the cultural evidence changes a question about a Method offering, applicability, lineage or renewal. Use `PSDA.17` for an affected interference question and `PSDA.14` or `PSDA.15` for a changed recommendation or its use. Use applicable domain evidence for a capability or subject question. Identify the needed contribution if it remains unavailable.

Preserve the useful narrow incumbent and the unselected branch. A variant can be inappropriate for one receiving use while remaining valuable elsewhere. A deliberate decision not to continue it in a named setting is different from an unexplained loss across the profession.

#### PSDA.18:4.8 - Refresh the affected relation or stop

Reopen the affected question when a change to a carrier, Method, population, receiving condition, source, authority or observation period alters its grounds. An intervention may also lose necessary support or produce evidence against the expected consequence. Trace the change to the claims it affects.

A departure may remove mentoring capacity without proving that the Method was forgotten. A software update may alter which examples are visible without changing the decision-support Method. A source correction may invalidate one taught inference while leaving the rest usable. State the actual consequence and retain independent claims.

For known reliance on a source, use `A.10` when the connection to the use is implicit or a needed reproducible account is missing. When a material change to a source claim puts earlier uses in question, use `A.10.1` to discover the affected uses or jointly revalidate several known uses. Use `G.11` for currentness or refresh planning under its conditions. Publication and access have their own evidence. To establish continuation, examine the receiving practice.

Close with the supported answer and its material limits. If a later observation has been selected, retain its conditions. If a protected condition fails, costs outweigh the intended contribution or continuation lacks grounds, apply the authorized stop or recovery rule. Where a decision is still needed, return the condition to its holder.

### PSDA.18:5 - Archetypal Grounding

These constructed cases stipulate their observations. They illustrate how to use the method. Claims about an actual community, effective intervention or subsequent enactment require evidence about that subject.

#### PSDA.18:5.1 - Another team must learn the qualified return, not just its format

In a municipal flood-advice service, `DecisionSupportTeam-East` uses the identified attributed-inquiry and conditional-analysis Method. Its practitioners work with residents, finance, operations, ecology and emergency-service participants on the 2027 flood-pump question. Concern maps, model explanations, workshop records and recommendation accounts carry the practice.

The cultural question concerns East's practitioners and the receiving `DecisionSupportTeam-West` in the service's East district and controlled online case environment during March–May 2027. East may change its facilitation and teaching arrangements. West may choose how to prepare for its own permitted engagements. The board retains the investment decision.

The current practice preserves a qualified fixed/mobile comparison, the open staged alternative and the questions about reachable assistance and protection. `PSDA.17` supplies the local arrangement and correction route. `PSDA.16` supplies applicability and lineage limits. To establish receiving use, examine West’s work. The proposed late-correction Method in `PSDA.16` remains a candidate for trial.

East sends a permitted case packet. West confirms that the file arrived. In a preliminary practice discussion, West's draft turns the conditional fixed/mobile comparison into an overall investment recommendation. The material service concern appears only in an appendix. The packet is available, but the needed interpretation did not survive this use. That observation does not show that West can never learn the Method or that every recipient misunderstood it.

East and West consider the following alternatives.

| Arrangement | Comparative reason |
| --- | --- |
| Keep sending the existing packet | Cheap and adequate for already experienced practitioners; the observed interpretation gap remains for this receiving group. |
| Add one guided qualification exercise using an explanation-rich case packet | West must explain what the comparison supports, what remains unclosed and why. This may address the observed gap, at the cost of experienced facilitator time. |
| Keep separate receiving routes | Experienced staff continue with the compact packet; practitioners needing the explanation use the exercise. This preserves differentiated support but requires clear entry conditions. |
| Stop the transfer attempt for this case | Necessary if source qualification, protected information, receiving capability or facilitation support cannot be secured. |

Within their remits, the teams choose the guided exercise for this group and keep the compact route for experienced staff. They test the exercise and packet together. Attributing any improvement to the packet alone would require evidence that distinguishes its contribution.

During March–May the teams’ service remits cover facilitation and practitioner preparation. The board holds the client investment decision.

On 12 March, 09:00–11:00 East used the attributed-inquiry and conditional-analysis Method. On 20 March, 09:00–10:30 both teams used a separately identified guided-qualification teaching Method. On 10 April, 09:00–11:00 West used the attributed-inquiry and conditional-analysis Method. The case places these observed actions within the service’s facilitation or practitioner-preparation operations. They support the inquiry, teaching and receiving-use findings below. The facts given leave the common construction of each occurrence as `U.Work` open. A claim requiring that classification needs the bases in `A.1:4.2` and `A.15.1` set out in §4.2.

During the exercise, West identifies the exact limit: “The fixed/mobile calculation is usable for its stated assumptions. It does not close the staged alternative or establish reachable assistance. Return those gaps with the qualified calculation; do not name an overall investment choice.” The facilitator challenges a substituted unqualified access premise. West keeps it outside the supported comparison.

In the later April inquiry, an independently observed receiving use preserves a resident's corrected service concern and the same distinction between qualified calculation and missing access evidence. The recommendation account retains the staged alternative as unclosed. No pump purchase, district-wide agreement or improved flood outcome is inferred.

The observations support the following claims about the named groups and period.

| Claim | Supported result or gap in this case |
| --- | --- |
| Generation and memory | The new receiving exercise and explanatory packet can be recovered with their source and intended use. Admission of a new decision-support Method remains open. |
| Transmission and receiving use | The teaching interaction conveyed the qualified-return distinction, and West's later observed inquiry followed the attributed-inquiry and conditional-analysis Method under the stated conditions. |
| Recognition and selection | The exercise feedback recognized preservation of the conditional comparison and honest gaps. West selected that way for the named April engagement; this is not selection by the whole service or profession. |
| Retention and loss | One later receiving use is observed. Continuation beyond that interval, use by other teams and loss elsewhere remain unproved. |
| Intervention consequence | The intended distinction appeared in the receiving return. The evidence does not isolate the contribution of the exercise from prior skill, added attention or other conditions, and supplies no investment-effect claim. |

The observations support retaining the receiving arrangement for one further cohort under matching qualification and support conditions. Select a new uncoached observation if its attainable contribution to that use warrants the burden. If mentoring becomes unavailable, reassess the route. East keeps its qualified Method and compact route. The late-correction proposal remains a separate `PSDA.16` candidate.

#### PSDA.18:5.2 - A library of polished advice can hide the honest return

A non-contested development-advising service is considering a change to its case library. The display currently promotes the most-viewed positive recommendations. The service suspects that this makes a decisive-looking answer easier to copy than a warranted request or blocker.

The access records establish which cases were viewed and how often. The display may shape what newcomers imitate, or familiarity may account for the greater number of views. The visibility finding can answer the present question. Receiving use and the display’s effect on it remain open. Select a study if obtaining that answer warrants the work.

One proposed arrangement pairs a positive example with a qualified non-choice return and asks a receiving practitioner to explain the difference. Retaining the current display is the cheaper alternative; removing the automated promotion rule is a possible fallback. The service must establish its own deciding System, remit, professional conditions and permission before changing the live arrangement; the flood-service authority does not transfer.

The library's constructed client is the Northbank service organization. It needs reliable incident recovery over the next ninety days. Internal development would train its existing recovery team and rehearse revised procedures. The alternatives are an external recovery provider and the existing team assisted by AI configuration B for diagnosis. Critical-service coverage, the customer-data boundary and a capped probe budget remain protected.

For this teaching case, assume a qualified allocation result confirms that two recovery engineers are available for four hours each per week for twelve weeks of training and rehearsal, with the required on-call shifts still fully staffed. This establishes that Northbank has staff time for that internal-development programme under the stated coverage condition. Whether the programme will improve recovery remains unverified.

The available AI evaluation covers configuration A, while B uses different tools; it does not qualify B for this use. The external provider's arrangement has not been assessed. Report the supported staffing finding: Northbank can allocate those two engineers to the programme while maintaining on-call coverage. Retain the separate gaps in recovery effectiveness, B's qualification and the provider assessment, and leave the three-way ranking unresolved. Request the missing evaluation for B through A.15.9 only when its obtainable contribution warrants acquisition.

The exercise tests reconstruction of the distinction under its stated conditions. Actual client use or continued practice needs receiving evidence. If the library lacks qualification for configuration B, use a suitable available evaluation, seek it when warranted or correct the library’s claim to reflect the gap. Changing the display would leave B’s qualification open.

The culture at issue is the advisers' way of handling evidence and returns. The human client's learning, an organization's allocation capability, an AI configuration's performance and a population's evolution remain separate subjects. Better teaching of their boundaries supplies none of those domain conclusions.

#### PSDA.18:5.3 - Publication coverage and ordinary non-use

A review finds few published PSM applications in a region. The corpus can help locate practitioners or cases. To establish loss, absence or effectiveness in a practice, examine evidence covering the relevant population and activity. Qualified local evidence may support a local continuation decision without a global survey.

If the only task is to correct a source locator, use the direct source or publication guidance. If the only question is which available Method fits tomorrow's engagement, use `PSDA.4`. Neither requires a cultural intervention.

A non-cultural population or lineage does not become a deciding Agent because it changes over time. Return that subject question to its direct practice. A researcher may separately choose an authorized intervention with its own scientific and governance basis; that does not turn the observed population into the recipient or chooser of advice.

#### PSDA.18:5.4 - Continue a supported practice

A service lead is deciding whether to retain the compact case packet and ordinary peer discussion for experienced advisers. In four inspected, uncoached returns from two recent cohorts, practitioners preserve the compared subset, uncertainty and material dissent. Qualified local judgement supports continuing this arrangement for the same uses and support conditions. The observations do not isolate the packet's contribution from experience or peer discussion, and establish no profession-wide retention.

A proposed two-hour comparison would displace the only available consultation on a consequential disputed return and would not change this continuation decision. Retain the present practice and those evidence limits. If a later interface hides the qualification or a new receiving group loses it, reopen that affected relation. The actual receiving loss and available teaching support in §5.1 instead warrant its bounded exercise; neither outcome is a universal rule to experiment or to retain.

### PSDA.18:6 - Bias-Annotation

Prestige and publication bias can make visible schools look like the whole field. Preserve the actual population and evidence window, including qualified practitioner accounts and unobserved links.

When considering an intervention, include an adequate current arrangement, a less costly way to continue or stopping where feasible. Preserve the meaning the receiving practitioners need when different conditions require a different format.

Consensus and positivity bias reward smooth meetings and decisive recommendations. Inspect whether a dissenting concern, qualified non-choice or refused transfer remains recognizable and usable. Do not punish practitioners merely for exposing a genuine source or authority gap.

Automation and observer bias can make access counts or watched performances look like independent adoption. Distinguish what the tool displayed, what the practitioner understood, what was enacted later, and what the evidence cannot establish.

### PSDA.18:7 - Conformance Checklist

**Recognition** asks which relation in the continuation or change of decision-support practice needs examination. Naming the practice, population, affected relation and question can be enough.

**Assurance** examines the evidence for the cultural claim or decision at its stated scope. Qualify authority, performers, occurrences, sources and effects where the claim uses them. A small reversible intervention may rest on qualified expert judgement. A wider effect or population claim requires grounds for that scope.

| Check | Sufficient answer |
| --- | --- |
| Current practice | The Method or variant, practitioner population, engagement/community, place, period and carriers are recognizable. |
| Cultural question | The relevant generation, transmission, receiving use, recognition, selection, memory, retention or loss is named, with its bearing on the requested conclusion or action. |
| Continuation choice | For a choice, identify who decided, under what authority and on what grounds. Include material alternatives, cost and limits. For selected further inquiry, identify its attainable value, full burden and stop condition. |
| Receiving meaning | Identify which participation, dissent, uncertainty, comparison or recommendation-use distinctions were preserved, lost or left unknown in the stated receiving use. |
| Performance and consequence | Proposal, plan, performed Work, actual change, observation and causal effect are not substituted for one another. |
| Evidence limits | Source coverage, estimates, observed occurrences and unproved population or retention claims remain distinct. |
| Finding or next use | The answer identifies the supported observation, any material open link, and the continuation, change or stopping condition when one is needed. |

An open link can limit a claim about a population or cause while leaving a local observation or continuation decision supported.

### PSDA.18:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| Announce cultural adoption from a new edition or course | Recover actual transmission, receiving enactment and the population/period covered; retain the rest as gaps. |
| Teach only the finished model or recommendation format | Preserve the interpretation, material dissent, qualification and stop that made the result usable. |
| Make every receiving practice copy the source exactly | Compare the necessary meaning with actual access, capability and participation conditions; qualify an adaptation or retain a separate branch. |
| Treat a team title as intervention authority | Establish who may make the named change and the basis for that authority. For a precise Agent claim, use the performer and assignment evidence in §4.1. |
| Call one project choice population selection | State who chose what locally. For a population claim, use evidence covering selection or continuation across the relevant practitioners. |
| Infer causation from a better-looking result after training | Establish what the observation covers and which explanations remain plausible. Test a causal claim when the requested conclusion needs it and the test is worthwhile. |
| Use popularity or publication counts as a fitness score | State what the measurement observes and recover the professional consequence that matters. |
| Keep intervening until all cultural links are proved | Return the bounded finding or decision, material uncertainty and any next observation that has been justified. |

### PSDA.18:9 - Consequences

A practice can continue important judgement without freezing one school or format. It can maintain different receiving routes, make a bounded intervention, and recognize that a well-grounded request or blocker can be a successful professional return.

The cost is attending to receiving practice and retaining inconvenient evidence. Some apparent adoption remains visibility, some short-term success remains a local observation, and some changes must be narrowed or stopped. The result is still useful before long-term or population-wide claims are warranted.

### PSDA.18:10 - Rationale

The domain problem remains after the general cultural relations are separated. Decision-support culture must preserve how practitioners handle participation, contested meaning, values, evidence, uncertainty, alternative comparison and the boundary between recommendation and later choice. A generic account of copying or selection does not determine which of those professional contributions is at risk or how to repair its receiving use.

Start with the practiced activity and the contribution under study. Use `C.36` for the cultural relation and the corresponding methods for agency, Work, evidence, choice, change and effect. When a continuation arrangement is needed, compare feasible ways to support facilitation, teaching, recognition or access to usable examples.

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
- Use `PSDA.16` when repertoire evidence or a variant bears on the cultural conclusion or decision. An offering alone leaves transmission open. If the needed input is missing or incompatible, identify the specific gap.
- Use a relevant `PSDA.17` finding to establish what changed in the local arrangement. Evidence of receiving enactment, selection, retention or effect must address that further claim.
- `PSDA.4` retains engagement-level Method selection; `PSDA.13`, `PSDA.5`, `PSDA.6`, `PSDA.7`, `PSDA.8`, `PSDA.9`, `PSDA.14`, `PSDA.15` retain participation, comparison, recommendation and follow-up results. Return an affected question to the relevant practice when its answer is needed.
- `A.13` and `A.15.1` qualify actual performers and dated Work; `F.6` applies only to a separately needed assignment-bound attribution. `A.3.1` and `A.3.2` distinguish the Method from its description or a candidate.
- `C.11` supplies a formed bounded choice; `B.5`, `B.5.2`, `A.3.3` and `C.28` govern the actual hypothesis, dynamics or causal question when needed. `A.3.4` and the direct Work-to-change or effect relation govern their own claims.
- For a needed external contribution use `A.15.9`. Use `A.10` for bounded reliance under the conditions in §4.8, `A.10.1` to discover uses affected by a material source change or jointly revalidate several known uses, and `G.11` for currentness or refresh planning.
- Publication, access, archive or selected-set treatment, capability development and holder-specific truth remain with their direct patterns and qualified sources. Neither a cultural account nor a shared carrier supplies those results.

### PSDA.18:End

## PSDA.19 - Bound the Development-Direction Advising Engagement

> **Type:** Method pattern
>
> **Status:** Stable
>
> **Normativity:** Normative unless marked informative.

### PSDA.19:1 - Problem Frame

**Use this when** someone asks a distinct adviser which development direction to consider for a person, organization, or other identified subject, but the terms of that help are not clear enough to support responsible advice. The question may already be well formed. Identify the condition still open, such as whose use the advice serves, what the adviser can competently provide, what may be disclosed or who holds a later choice.

Identify the recipient, developing subject, intended use, horizon and adviser. Use the professional and service conditions that govern the requested help. An adequate existing agreement can establish that the service may proceed. Otherwise return a narrower scope, the particular missing condition or a justified referral.

Development-direction advising concerns the relationship between a recommending performer and a recipient and the uses that relationship permits. Use the relevant PSDA methods when formulation, comparison or a recommendation is needed. An adequate relationship permits the bounded service. Supporting the advice itself requires evidence about the subject and directions.

**Ordinary non-use boundary.** For self-directed opportunity construction, use the missing contribution from C.40.OI, C.40.NU, C.40.PC, C.40.DC, C.40.JF or C.40.OP. For the holder’s own choice on adequate premises, use C.11 or the applicable domain rule. Reuse a current service boundary when it covers this engagement. When one qualified practice supplies the whole service, use it directly.

### PSDA.19:2 - Problem

An apparently helpful development conversation can serve the wrong recipient. An employer pays for career advice and expects the employee's private assessments. A sponsor's preferred provider becomes the presumed recommendation. A fluent AI-assisted memo conceals an unqualified assessment or unauthorized use of client information.

Entry becomes costly when a formed question triggers an exhaustive diagnosis, participant map or workshop. Establish which advice is wanted and what condition, if any, prevents the adviser from providing it now.

The adviser needs a bounded relationship in which service competence, participation, confidentiality, conflicts, referral, and choice remain clear enough to establish the service available under the stated conditions.

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

Establish the development-advice question and the conditions under which the adviser can responsibly answer it. Use a sufficient existing agreement. Where a condition needs agreement, establish who can supply it and state any limit that remains. Match the detail to the receiving use and its consequences.

#### PSDA.19:4.1 - Identify the actual relationship and receiving use

Use an adequate existing engagement question, or use [PSDA.11 — Bound the Decision-Support Engagement and Authority Boundary](#psda11---bound-the-decision-support-engagement-and-authority-boundary) to establish the missing part. State whose development is at issue, what contribution or decision the advice serves, the horizon and the return sought now.

Identify who is preparing the advice and who receives it. Development-direction advising here requires a distinct recommending performer. A recipient may also hold the subsequent choice under the applicable authority. A team can receive advice from an internal specialist.

Distinguish client, sponsor, developing subject, recipient and holder of a choice where the difference affects service, disclosure, protection or action. One participant may fill several positions. Establish those positions from the terms and actual circumstances. Payment or a signature may establish one fact while leaving another open.

A useful question might be: “For Mira's own development choice over four months, help her compare directions for contributing to cross-disciplinary review; her employer's later assignment decision remains separate.” If the recipient or intended use is unknown, report the gap. If the task is a direct inquiry, return its result to the relevant use.

#### PSDA.19:4.2 - Bound the service by competence and applicable duties

Establish the agreed scope of assistance or what service could be offered. Distinguish advising from assessment, teaching, psychotherapy, recruitment, sales, programme design or implementation where confusion would change what the client receives. If the requested service exceeds the scope, give the support available or a justified referral.

Apply the professional and local requirements governing this service, jurisdiction and relationship. If their applicability matters and remains uncertain, use a competent interpretation or state the limit. For a claim about licence, duty, assessment competence, legal authority or client capacity, establish the relevant basis. An adviser title or signed form alone may leave it open.

Identify what the adviser is qualified to judge and which specialist premises the advice needs. Reuse applicable results, including those the adviser can competently establish. For missing human-development, organizational, technical, safety, legal, financial or other specialist work, use A.15.9 when its obtainable contribution warrants the acquisition cost under C.11.DUA. For a question about the service boundary, return that boundary. When advice is requested and permitted, give the conclusion supported by current premises and identify any material gap. Attribute a supplied conclusion to its qualified source.

For human career services, [NCDA's 2024 Code of Ethics, A.2, A.10, and E.2](https://www.ncda.org/aws/NCDA/asset_manager/get_file/3395) addresses informed participation, competent assessment and interpretation, and referral or closure. Apply the provisions governing the service in question. If a consent or capacity question exceeds the adviser’s competence, use an applicable qualified result or seek the needed help before relying on that condition.

#### PSDA.19:4.3 - Agree participation, information use, and disclosure

Make the service and its limits intelligible to its required participants. Where a person’s consent or assent is required, establish the applicable basis. For other participants, establish the conditions governing their participation. Identify information required, intended use, permitted recipients and confidentiality limits. Distinguish voluntary participation, mandated service, assent and authority to act for another person when they change what may be done.

Identify which information may go to the sponsor and which remains within the advising relationship. Apply any disclosure duty and any restriction on release. For a different purpose or audience, check whether the applicable basis covers that use. Payment alone establishes funding.

Limit information use to what the bounded service needs. Where a premise is protected, explain how the restriction limits reliance without exposing its content. A permitted qualified summary may support the needed return. If the permitted explanation leaves the advice insufficiently grounded for the recipient, narrow the conclusion or identify the blocked use.

When a client declines an optional assessment or service, state what advice remains available and whether the refusal leaves a material premise open. A refusal supplies evidence of that decision. A claim about capability needs grounds about capability. Continue any duties that apply.

#### PSDA.19:4.4 - Treat conflicts before relying on the advice

Identify material financial, provider, employment, organizational, or other interests that can distort the requested service. Make their treatment explicit under the applicable relationship: disclosure, changed scope, independent assessment, recusal, referral, or another qualified response.

Check whether disclosure resolves the conflict under the applicable relationship. A sponsor’s instruction to conceal a material interest or exclude a serious alternative may prevent an independent comparison. State which service is blocked. The technical properties of the excluded direction need their own evidence.

For management consulting, [ICMCI's competence framework v4.0, C.1.1–2, C.2.1, and E.3.5](https://www.cmc-global.org/sites/default/files/public/icmci_cmc002_competence_framework_version_4.0_1.pdf) addresses engagement scope, client involvement and financial conflicts. Apply the requirements governing the actual consulting relationship.

Preserve an independently qualified domain result within its established scope when a relationship conflict changes who may advise or how the result may be used.

#### PSDA.19:4.5 - Distinguish AI assistance from an AI development subject

When an adviser uses AI assistance, establish the permitted information use and the review required of the responsible professional. Under the [ICMCI AI Code v1.0, May 2026](https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf), sections 1.2, 2.2, 3.1–3.4, 5 and 7, the consultant retains professional responsibility and communicates material AI use and its limits to the client. Qualify specialist claims using evidence and competence relevant to their subject.

When AI is the developing subject, identify the model, scaffold, tools, allocation or composite arrangement being changed and its receiving environment. Establish who receives the advice and who can choose. Qualify the proposed change with applicable AI, engineering, operating and governance evidence. Use A.15.9 for an external result when needed.

Both situations can occur in one engagement. Keep the adviser's use of AI, the proposed change to the subject, and the human client's professional protections separate.

#### PSDA.19:4.6 - Enter at the missing substantive result

If the task was to establish the service boundary, return the supported boundary or limit. For substantive advice, establish what follows from the available premises and identify any contribution still missing. Use opportunity, characterization, reachability and comparison findings that cover the subject, configuration, use and horizon.

If the receiving contribution or direction is unsettled, use the relevant construction method. If adequate directions exist, enter the actual alternatives, comparison or recommendation question. Use PSDA.12, PSDA.1, PSDA.2, PSDA.3, PSDA.4 or PSDA.13 when a result about participants, formulation, scope, models, Method choice or facilitation is needed.

Use C.40.JF for missing joint reachability and A.15.9 for a needed external premise. An admissible service may still have grounds for only a conditional set, request or blocker. A missing provider comparison can leave the whole ranking open while an independently established human-development result remains usable.

PSDA.14 supplies the bounded recommendation when that question is current. The later authorized direction choice remains separate. When the selected direction calls for human capability development, HCD.2 programme comparison, an optional programme recommendation, authorized programme choice and Learning Product Guide remain distinct further results. An existing programme-level comparison can be used directly for its programme question.

#### PSDA.19:4.7 - Return the boundary and preserve actual closure duties

Lead with what can be offered now and the most important condition. For example, the following return establishes the limits for Mira and her employer.

> We can help Mira compare review-development directions for her own four-month choice; the employer receives only the agreed service summary, not her private assessment material. A recommendation remains conditional on the missing representative-practice and transfer results, while the employer retains its separate assignment decision.

If the service is blocked, identify the particular condition, such as mandate, competence, consent, conflict or disclosure. Name any limited help available and a qualified recipient for a referral when one is needed and known. A service blocker leaves the subject’s development possibilities a separate question. If evaluating them is also requested and permitted, use evidence about the subject and directions.

Fit the explanation to the recipient’s use. Use PSDA.14 and the applicable receiving-use guidance when preparing an intelligible recommendation. Establish subsequent understanding, consent, choice, implementation or effect from evidence of each when the task calls for it.

After delivering the return, continue contact, referral, confidentiality, protection and closure duties where the professional relationship requires them. Use PSDA.15 for any needed follow-up. Existing evidence may settle a reassessment. If a new observation is needed, establish a feasible arrangement, including support for its timing. Reopen the affected condition when the recipient, purpose, competence, conflict, information use or professional basis changes in a way that matters.

**Recognition and assurance.** Identify the recipient, subject, adviser, use, horizon and service limits, including the holder of any choice at issue. To rely on the engagement, establish the competence, participation, protection, information-use and authority conditions it requires. A proposal or statement of terms may leave compliance with one of those conditions open.

### PSDA.19:5 - Archetypal Grounding

#### PSDA.19:5.1 - Employer-sponsored advice remains Mira's development question

This is a constructed case. Mira's employer funds four months of career-development advice. Mira asks a separate adviser whether to pursue cross-disciplinary review capability or a specialist engineering direction. The employer also wants information for a later staffing decision.

The adviser first separates the intended uses.

| Participant or use | Bounded position |
| --- | --- |
| Mira | Developing person and recipient for her own development choice. |
| Employer | Sponsor; it retains its separately authorized staffing decision. |
| Adviser | Prepares the development-direction return within the established career-service competence and agreed conditions. |
| Personal assessments | Use within the qualified purpose and permitted disclosure basis. Employer funding leaves access to assessments a separate question. |
| Employer-facing return | An agreed service summary, with no private assessment content unless a separate applicable basis permits it. |

In this case the adviser is competent for the bounded career service. Specialist development and transfer assessments lie outside that competence. Mira accepts the service and the employer agrees to the disclosure limit. Existing information identifies both directions. The proposed transfer to independent review lacks qualified support. The adviser can return the service boundary in `:4.7` with that substantive limit. Seek an HCD result when its attainable contribution warrants the cost. A course recommendation still needs its own grounds.

The employer then requests raw assessment notes for staffing. That use and audience fall outside the agreed summary. The adviser withholds release until an applicable basis permits it and revisits the affected terms. Mira’s earlier assessments retain their established scope. Mira holds her development choice and the employer its staffing decision.

If the sponsor refuses any service except undisclosed assessment transfer, the current request may end with a scoped blocker or referral under the actual professional conditions. It does not justify an adverse judgement about Mira.

#### PSDA.19:5.2 - A provider interest changes the service, not the engineering facts

In a constructed organization case, a committee asks a consulting team to compare internal development, a provider arrangement, and mixed support for a ninety-day reliability need. The committee is the intended recipient and assumed authorized choice owner.

One consultant has a material payment interest in the named provider. There is an independently qualified technical result about internal development. The consulting team has yet to recommend a course across the whole set. Apply the relevant conflict requirements before relying on that advice. Disclosure and independent comparison may suffice under one relationship. Another may require recusal or referral.

If the sponsor demands a concealed provider preference, identify the independent comparison as blocked under those terms. Retain the technical result about internal development. Technical feasibility of any other direction remains a separate question.

#### PSDA.19:5.3 - A model is the subject, not automatically the client

In a constructed AI case, an authorized operations team asks a separate advisory arrangement whether to tune a model, change its retrieval support, or alter human–AI allocation. The team receives the advice; the changed model or composite arrangement is the subject. The advisory service still needs its own scope and qualified technical inputs.

The evaluation covers configuration A. The proposed configuration B changes tools and oversight. Return the supported result for A and identify the evaluation and safety conditions still unverified for B. Seek B-specific evidence when its attainable contribution warrants the cost. A deployment recommendation needs grounds for that configuration. The adviser’s drafting tool leaves the client’s information-use restrictions in force.

For contrast, “tell this unmanaged biological lineage which direction it should choose” supplies no lineage-local recipient or chooser. Return that attribution gap to the evolutionary account. A research team asking about a proposed intervention is a different recipient-owned case requiring its scientific, ethical, safety, and governance basis.

#### PSDA.19:5.4 - Do not create personal advice from an audience description

A provider asks which learning programme to design for future participants. The provider's programme-design decision is the receiving use; the described audience is a design assumption, not a collection of assessed clients. Use PSDA.11 and the learning-product design practice for that question.

If Mira later asks whether that programme fits her own development, her later Work, starting conditions, support, and qualified comparison become relevant. A well-described audience does not supply those personal premises. Conversely, an adequate existing programme comparison can support a programme-level advice question without repeating opportunity construction.

### PSDA.19:6 - Bias-Annotation

Sponsor pressure can displace the recipient's use. Provider incentives can hide behind a technically plausible comparison. Professional confidence can make the adviser cross into an unqualified practice, while automated fluency can obscure that crossing.

Identify whose question the advice serves, what disclosure is permitted and what competence supports a decisive claim. Apply the duties of the actual relationship. Involve participants where their contribution or agreement is needed.

### PSDA.19:7 - Conformance Checklist

1. **MUST** identify the distinct recommending performer, recipient, developing subject, receiving use and horizon. Identify the authority for a later choice when that choice matters, or state the limit if its holder is still unknown.
2. **MUST** separate sponsor, client, recipient, subject, and chooser where the difference changes service, disclosure, protection, or authority.
3. **MUST** bound the offered service, actual competence, applicable professional conditions, exclusions, and referral or closure requirements.
4. **MUST** establish the relevant participation and information-use basis without inferring consent, capacity, or disclosure permission from a title, payment, or form alone.
5. **MUST** address a material conflict under the rule governing the relationship before relying on the requested advice. Disclosure is sufficient where that rule and the circumstances make it so.
6. When AI assists a performer, **MUST** identify the applicable professional and information-use conditions. When an AI configuration is the development subject, **MUST** qualify the technical claim about that configuration. Both questions can arise together.
7. **MUST** support specialist premises with suitably qualified work and identify which claim a missing premise limits. Where a stronger conclusion needs work beyond the adviser’s competence, use a qualified external result or report the limit if it is unavailable.
8. **MUST** distinguish an admissible engagement question from a warranted recommendation and each later authorized choice or realization.
9. **MUST** meet the professional contact, referral, protection and closure duties that continue after delivery for this relationship.
10. **SHOULD** reuse an adequate boundary. If further work is needed, enter at the missing result. For an ordinary self-directed inquiry, use the corresponding opportunity or choice method directly.

### PSDA.19:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| The sponsor is every recipient | Payment is mistaken for disclosure rights and choice authority. | Name each actual use and its participation, disclosure, and decision basis. |
| Signed means informed | A form substitutes for the required understanding, participation, or capacity. | Establish the applicable condition or obtain qualified assistance. |
| Disclose and proceed regardless | A declaration substitutes for treatment of an incompatible conflict. | Use the actual professional response, including narrowed service or referral. |
| Admit the service, then prescribe | A suitable relationship permits a service. A recommendation depends on the available substantive evidence. | Use available premises to support the advice, or return the narrower finding or missing premise. Use PSDA.14 when a recommendation is needed. |
| AI answered, so the adviser is qualified | Generated content masks missing expertise or prohibited data use. | Keep responsible review and specialist qualification in their actual practices. |
| Every advice question needs a workshop | A formed question is forced through irrelevant intake work. | Use the first missing result and preserve adequate inputs. |
| Delivered means all duties ended | Completion of a return is mistaken for closure of the relationship. | Follow the actual contact, referral, protection, and closure basis. |

### PSDA.19:9 - Consequences

The recipient can understand what help is being offered, whose interests are represented, what may be disclosed, and which decision remains theirs or another participant's. A formed question can proceed without unnecessary construction or facilitation.

The boundary may support a smaller service, identify a needed qualified supplier, justify referral or show that the requested terms preclude responsible advice. Agreeing terms requires attention from the participants. It can expose a sponsor’s expectation that the agreed service cannot meet.

### PSDA.19:10 - Rationale

Development advice combines premises about a subject with a relationship in which someone is expected to help a recipient. Good technical premises cannot repair an unauthorized disclosure or incompatible conflict. Equally, a proper relationship cannot supply a missing development or transfer result.

A service may proceed within its supported scope while one substantive claim remains conditional. A qualified domain result can also remain usable when a conflict changes who may provide the advice.

### PSDA.19:11 - SoTA-Echoing

**Practice question.** How can a formed development-direction question enter responsible advice without collapsing recipient, sponsor, professional service, and later choice?

Use PSDA.11’s receiving-use question with the professional conditions governing this relationship. Sections 4.1–4.4 and 4.6–4.7 adapt that division. Identify the minimum adequate service boundary, the evidence already available and the supplier of any missing premise when needed.

**Serious alternative and trade-off.** Generic authorization and a technically sound comparison can suffice for an ordinary local choice. They do not settle who receives Mira's assessment or how a provider interest affects the consulting relationship. At comparable intake effort, a question about the intended recipient and disclosure exposes that defect. An exhaustive diagnostic or facilitation engagement can be useful when it is the actual service, but adds burden without resolving a formed question more directly. The selected boundary trades a small amount of explicit agreement for a more usable and contestable service; the constructed cases do not establish measured effectiveness.

**Professional source returns.** NCDA's 2024 Code, A.2, A.10, and E.2, informs the human career-service participation, assessment, and referral limits in `:4.2`–`:4.3`. ICMCI v4.0's identified engagement clauses inform client involvement and conflict treatment in `:4.1` and `:4.4`. These are bounded source contributions, not one universal professional code or a complete current certification standard.

Section 4.5 of this method draws on the ICMCI AI Code v1.0 for the consultant’s responsibility, content review, information use and communication of material AI assistance. Apply those conditions in their professional scope. An evaluation of the developing AI configuration requires evidence about that configuration in its intended use.

**Limits and reopen.** Apply the professional sources only where their scope or adoption is established, together with the actual local requirements. Reopen the affected boundary when those requirements, the service purpose, recipient, competence, conflict, or information-use conditions change, or when a less burdensome arrangement preserves the same protections and useful return.

### PSDA.19:12 - Relations

- **Uses PSDA.11:** the generic engagement question, participant positions, receiving use, and authority boundary.
- **Receives from C.40.OI, C.40.NU, C.40.PC, C.40.DC, C.40.JF, C.40.OP or adequate direct sources:** inquiry, characterization, opportunities, directions, reachability, and retained paths when those results are needed.
- Use suitably qualified specialist work for its own premise. For a needed external contribution, use A.15.9 where acquisition is warranted and feasible. If it remains unavailable, identify the conclusion it limits.
- **Uses PSDA.5, PSDA.6, PSDA.7, PSDA.8, PSDA.9, PSDA.14:** alternatives, comparison, and recommendation only for the actual missing decision-support result.
- **Returns to the applicable professional relationship:** competence, participation, confidentiality, conflicts, disclosure, referral, and closure.
- A direction choice belongs to the authorized holder. If the selected direction calls for human development, use HCD.2 for a needed programme comparison. A programme recommendation, authorized programme choice and later Learning Product Guide are distinct results.
- **Uses C.40.RQ:** changed engagement premises and their opportunity-specific effects.
- **Uses PSDA.15:** a genuinely needed follow-up arrangement and affected recommendation return.

### PSDA.19:End

## PSDA.20 - Explore a Situation through Goals and Dependencies

> **Type:** Method pattern body
> **Status:** Stable
>
> **Primary working result:** a supported answer about the proposed change or observed situation, an explanation of a newly identified difficulty, or a precise unresolved question. Connect the result to the relevant purposes, provision, assumptions and limits.

### PSDA.20:1 - Problem frame

**Use this when** a change appears helpful from one participant’s position and you need to know what it would require or change for others. You can also trace a reported outcome to the provision it depended on. The inquiry may yield a comparison, a newly identified difficulty or a question for investigation. Use a diagram when it makes the relevant relationships easier to inspect.

Start with a particular episode or proposal. Identify the needed answer and the difference that matters to its conclusion, grounds or use. Trace a provision on which the result depends. An omitted contributor or an unsupported condition can be the first useful finding.

Use an adequate existing model or qualified answer directly. For a settled technical calculation, use the relevant technical method. Use PSDA.8 for a missing consequence comparison or PSDA.3 for contributions from several models that need to be reconciled. A choice or work allocation requires the appropriate authority.

The performer can conduct this inquiry independently or with others when they have the necessary access and competence to interpret the relationships. Use participants’ accounts and qualified specialist evidence where the question needs them. If an intention or specialist relation remains unknown, identify that limit. A separate adviser, workshop, formal notation or solver can help when its expected benefit, such as a better-grounded answer or time saved, warrants its cost.

### PSDA.20:2 - Problem

A proposal can improve one visible result while relying on work that nobody has provided. A replacement sensor may improve a count without settling who keeps the service operating during installation. A diagram can make the dependency visible yet still conceal its purpose, timing or competing assignment. Evaluating the diagram as if those conditions already held produces an answer to a different question.

An unexpected result can expose an incomplete question. The immediate difficulty may be staffing two services together. Trace the answer to its premises, revise the affected question and retain earlier conclusions whose grounds still hold.

### PSDA.20:3 - Forces

| Force | Tension |
| --- | --- |
| Local reasons and joint work | A change can help one participant while its provision or burden prevents another necessary contribution. |
| Useful simplification and omitted conditions | A small model can expose the next question, but hiding a provider or assignment can make an unavailable arrangement look adequate. |
| Exploration and reliance | Conditional analysis can be useful before every input is known; a stronger claim needs the corresponding evidence and actual conditions. |
| Required results and freedom of means | Naming the needed provision leaves room for another method; prescribing a task can narrow that freedom deliberately or accidentally. |
| Revision and continuity | A discovered conflict can change the problem, while independent relationships and earlier conditional answers remain usable. |

### PSDA.20:4 - Solution

Connect the question to the relevant purposes and provision. Use the model to infer what follows from its relationships and stated premises, then interpret that result in the working situation. If an omitted condition affects the answer, revise the relevant model or question. Close with the finding, limit or next inquiry the receiving work needs.

The connected contributions are [PSDA.12](#psda12---recover-participants-concerns-and-affected-systems-for-a-decision-support-inquiry) for whose concerns enter, [PSDA.3](#psda3---construct-complementary-situation-and-option-models) for what the model can answer, [PSDA.5](#psda5---generate-decision-alternatives) for alternatives, and [PSDA.8:4.2.1](#psda8421---construct-and-question-a-qualitative-consequence-network) for qualitative analysis. Enter at the unresolved question and retain usable answers. If a current direct calculation or an already qualified comparison settles it, use that result.

The car-park case follows the inquiry through a staffing conflict and a revised allocation. Enter the general method at the part the question needs. An existing model may supply the relationships, a precise question may be ready for analysis, and an unexpected result may identify one missing premise. The exhibition case in §5 examines permissions and supply.

#### PSDA.20:4.1 - Let the question determine what to model

Identify what the inquiry needs to explain or support. Use existing records, relevant accounts and observations that establish the operating conditions. For a participant’s intention or experienced burden, use an attributable account or ask when needed and feasible. State any material gap. Participation in building the model may help correct it. To report agreement with a proposal, use evidence of the relevant response.

Consider a car park whose unreliable sensors sometimes send drivers towards occupied floors. Attendants walk the floors and correct the displayed counts. Management proposes replacing the entire system, since the sensors cannot simply be exchanged in the current design. The inquiry asks, **Does replacement address the service difficulty better than continuing manual correction?** This is an adaptation of the parking exercise in the [iStar tutorial, slide 57](https://zenodo.org/records/10637477/files/iStar-tutorial-online.pdf?download=1). The following participants, conditions and judgements are constructed for this walkthrough.

Include drivers because the guidance affects finding a place; attendants because correction requires their work; the operations manager because staffing and service arrangements are theirs to decide; and the technical supplier because replacement feasibility and installation depend on its contribution. Management cares about operating cost and reputation. Drivers care about usable guidance and protection of their cars. An attendant's account of an assignment is evidence about that work, not a statement of every driver's preferences.

Keep the questions distinct. What would make the displayed count trustworthy? Can the work supply it when needed? How would the alternatives affect cost and the concerns behind reputation? A model of intentions can expose these questions before it has the technical estimates needed to answer all of them.

#### PSDA.20:4.2 - Connect provision to the reasons on both sides

Distinguish a desired state, action, required entity and quality. Current guidance is a desired result. Walking the floors and entering a corrected count prescribes work. The supplied count is information used in the display. Accuracy concerns how well it represents available and occupied spaces for the intended guidance. Evidence of a completed round needs a further connection to support a claim about accuracy.

For a material dependency, identify who needs the contribution, why, and what must be supplied. Establish who could or did supply it and how, insofar as the question needs those facts. Keep an unknown provider or an unsettled means open. For example, an agreed assignment might read as follows.

> The operations manager needs a checked floor count from the attendant so that the service can issue current guidance; the attendant obtains the count by inspecting the floor and entering the result before the next update.

Distinguish the checking task, supplied count and manager’s need. State any missing method, deadline or condition that limits the result. To claim availability, acceptance or completed work, use evidence for the particular claim.

Requiring a count with stated fitness conditions leaves room to choose its production method. Requiring a specified inspection task restricts that choice. State which relationship the work needs. Similarly, two recipients needing information called “the floor count” may need different intervals or accuracy; matching names do not establish interchangeable provision.

For this service, a suitable count and a working display are both needed. A recent manual inspection or supported automatic sensing might supply the count. Check the operating conditions for the means under consideration. Manual correction needs staff time and access. Replacement needs an applicable design, installation and operation. Investigate a proposed external delivery as a supplier contribution.

Give each relationship its intended meaning, such as necessity, sufficiency under stated conditions, a favorable or adverse contribution or a quality of a provision. The manager considers accuracy helpful to reputation and also values protection of parked cars. Evidence of protection is still needed to count it as provided.

#### PSDA.20:4.3 - Show the part of the model needed for the current question



A view showing only participants and external provision helps locate a missing supplier. Opening the manager's and attendant's internal reasons exposes why the count is needed and what work supports it. Opening the supplier's proposed arrangement becomes useful when installation or later maintenance can change the answer.

In iStar the strategic dependency view, strategic rationale view and their selective combinations expose different parts of one model. Use the view that answers the question. Preserve the identified dependency across views. Check underlying conditions when the display omits a detail that matters.

For this car park, an overview can show “attendant supplies count”. To examine availability during a shift, open the checking task and its staffing conditions. For a whole-cost comparison, use an applicable cost account, calculate it from qualified inputs or state the cost still unknown. The [iStar 2.0 Guide, §§2–8](https://arxiv.org/html/1605.07767v3) supplies the notation, distinctions and integrity rules when an actual iStar model is wanted. This prose walkthrough uses those distinctions without claiming to be a solver-ready model.

#### PSDA.20:4.4 - Turn a working question into an analysis, then recover its meaning



For each alternative the question concerns, identify which work or assumptions differ from the current arrangement. Alternative A retains the existing displays and uses manual correction. Alternative B installs the proposed replacement and uses its automatic counts. For the initial comparison, suppose staffing for A is available and the supplier has described a technically plausible B, while B's installation interval and whole cost remain unknown. Do not compare A in its troublesome current state with B in an unexplained ideal state.

In this question, label each initial value as an observation or a stipulated assumption. To examine B if installed and operating as proposed, assume installation and the specified sensing performance. Keep installation and whole cost open for any investment decision. The conditional service comparison can proceed on its stated inputs.

Omitting manual rounds from B defines the proposal. It supplies no evidence about the attendants’ capability to inspect a floor. Use any independent evidence available for that question. Distinguish an unexamined element, an examined effect for which evidence is insufficient, a negative observation and conflicting grounds.

Follow the relevant relationships for each alternative. Use [PSDA.8:4.2.1](#psda8421---construct-and-question-a-qualitative-consequence-network) for a needed qualitative analysis. Keep the initial assumptions and intermediate judgements with its result. For A, a sufficiently recent and correctly performed round supports a corrected count; publication still needs the working display. For B, the stipulated sensing performance supports the count conditionally; it does not establish the installation date or remove all future maintenance work.

Use the source that can support an unresolved contribution, such as a relevant participant’s stated judgement, an operating record or a specialist assessment. Here management judges that fewer misleading indications would help reputation. That supports a favorable contribution from guidance. The overall judgement about reputation remains open while protection is unresolved. Manual inspection can improve counts and increase staff burden at the same time. Assess those effects on their own grounds.

Return the conditional comparison in the terms of the car-park inquiry.

| Question | A: retained system with manual correction | B: proposed replacement |
| --- | --- | --- |
| Can it provide useful counts? | Supported only while the stated inspection, freshness, staffing and publication conditions hold. | Supported conditionally on the proposed installation and sensing performance. |
| What happens to work and cost? | Inspection remains a recurring demand. | Some inspection may be displaced, but acquisition, transition and operating costs remain to be established. |
| Does it meet the concerns behind reputation? | Better count information addresses one concern; protection of cars needs its own grounds. | The same limit applies; a better sensor is not evidence of protection. |

The comparison identifies a possible service improvement under its assumptions. Installation timing and total cost remain open, so it leaves the investment decision unresolved. Return the conditional comparison if that answers the question. Seek the missing facts when their attainable contribution warrants the work.

#### PSDA.20:4.5 - Use surprising results to discover a different problem

Trace a surprising answer to the relationships, premises and analysis rules that produced it. Check whether the model misrepresents the work or the original question omitted a consequential condition. Correct an established error and reconsider the affected conclusions. Use the corrected model if it answers the original inquiry.

When the original question omits a necessary contribution, state the required joint result and the conditions that make it possible. Explain how the dependency changes the question for the intended use. A supported account of that dependency can finish an inquiry about the original proposal.

If the task needs another arrangement, work backward from the joint requirement. Look for feasible changes to the provider, means, timing or support. Use PSDA.5 when generating alternatives needs further work. A proposed relaxation of the requirement needs the applicable authority and the conditions of the recipient’s use.

Test each candidate combination under the same conditions, including competing assignments and shared resources. When a premise changes, revise the dependent conclusions and keep those still supported. Return the resulting candidate, supported rejection or open condition with the reason it matters.


Suppose the first model gave A an unqualified favorable result because it represented the round but omitted other assignments. Ask what must be true for that result to hold. Inspecting the rota now reveals that the same attendant must be at the security desk from 10:00 to 10:15, while the modeled correction requires leaving it for a round from 10:00 to 10:10. No substitute is assigned. These stipulated facts defeat the simultaneous arrangement.

The discovery changes the model and the problem. Add the required desk coverage and its relation to the attendant's available work; then revise A's count availability for this interval. The earlier claim that a completed, timely inspection can supply a count still holds. B's separate technical hypothesis also survives. What fails is the premise that A's work can coexist with the retained service obligations.

If the manager needs a remedy, the next question is **how can the service provide current guidance and cover the desk during this interval?** A different allocation or contributor would need to meet both requirements. The manager holds assignment authority. Use [OCE.11](Management%20DPF%20Suite/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce11---coordinate-organization-change-work-with-continuing-service) when the proposed change competes with continuing service.

Current guidance requires an adequate count and publication. Desk coverage requires someone at the desk. A competent relief checker could perform the round while the attendant remains at the desk. Establish whether the checker could obtain and publish the count in time with the required access and without leaving another necessary assignment. Until then the proposed allocation is conditional.

For a bounded continuation, suppose the manager assigns a competent relief worker for this interval, verifies that no other required assignment overlaps, and provides the permitted access and existing checking procedure. In the stipulated trial the relief worker obtains and publishes a count meeting the agreed freshness and accuracy conditions, while the attendant remains at the desk. Both required contributions are supplied in this interval. The added staffing cost belongs in A's cost account. If relief is available only today, retain today's result and reopen the staffing question before promising tomorrow's service; the earlier investment question remains open.

A different candidate might change the update interval or the information promised to drivers. That changes the service requirement, so return to whether the altered guidance remains useful and acceptable. Do not weaken the criterion silently to make the diagram succeed. An incompatible candidate can be rejected without proving that all possible arrangements fail; an unsupported candidate stays conditional.

Retain the failed combination and its reason where another decision or attempt depends on it. In formal backward analysis, identify which premises or judgements produce the incompatibility. A proof of incompatibility establishes it within the encoding, premises and restrictions. A search that exhausted its allowance without finding a solution leaves compatibility unresolved. An organizational claim about all remedies needs evidence covering those remedies.

#### PSDA.20:4.6 - Stop with a usable answer and preserve the right return

In the stipulated interval the original assignments conflicted and the revised allocation supplied both services. The initial conditional comparison leaves the replacement investment open. A repaired rota can settle allocation for the interval. A cost comparison contributes to an investment question, while assignment of a checker needs a separate authorized act.

Close when the result answers the receiving question at the required strength. Return the supported comparison, explained incompatibility, fact about provision or precise missing information with the conditions needed to use it.

When a new fact matters, trace it to the affected premise, relationship and dependent conclusions. Keep independent results. For a needed technical result such as an accuracy bound or failure probability, use suitable existing evidence or an appropriate model. If the input or model is unavailable, identify the remaining limit.

If the analysis is difficult to interpret, try a small question whose expected answer can be traced through the relationships. Check for omitted providers or intentions relevant to the claimed coverage. The researchers also suggest extreme hypothetical settings and realistic alternatives for examining a model. Their usefulness for diagnosis and their feasibility as actual plans are separate questions. If the chosen language is unfamiliar, seek or provide the preparation the task needs.

### PSDA.20:5 - Archetypal Grounding

#### PSDA.20:5.1 - A searchable exhibition whose material cannot simply be published

A community archive proposes automatic transcription for a public website so that visitors can search thirty oral-history stories in either of two languages before an exhibition opens. The access rules, source states and capacities below are stipulated for this constructed example.

The curator needs visitors to find the relevant approved story. Speakers have agreed to public use of approved excerpts; the raw recordings remain restricted. The proposed service requires an approved excerpt in both languages for each of the thirty stories. The permitted use protects the speakers’ conditions for sharing. Coverage in both languages for all thirty stories defines the proposed service. Faster search cannot authorize release. Would transcribing and publishing the recordings supply what the curator needs?

Recover the provision before choosing software. The curator needs approved bilingual excerpts from an editorial contributor. That contributor needs permitted access to source material, a usable translation and the approval required for that use. The archive custodian can supply permitted material, while the speakers supply approval under the stipulated arrangement. A transcription tool can propose text; it does not supply permission, translation competence or the speakers' approval.

An overview showing “archive supplies stories” hides these differences. Open the editorial contribution only as far as the current question needs. Distinguish producing a transcript, producing a translation and obtaining approval. Examine fidelity to the speaker’s account, intelligibility for visitors and permission to use the excerpt. Readability establishes at most one part of that assessment.

Now examine two proposed arrangements. Publishing searchable raw transcripts conflicts with the stated access rule even if the transcripts are accurate. Publishing an index of approved bilingual excerpts could meet the rule, but only if the needed excerpts can be supplied. This comparison neither rejects automatic transcription as an internal aid nor silently relaxes the required public use.

Suppose the first model gave the second arrangement a favorable result because it represented an editor as available. On asking what that assumption includes, the curator finds that approved bilingual excerpts exist for ten stories and the available editorial work can complete five more before opening. No supplier is yet identified for the remaining fifteen. The model had combined “some editorial help is available” with “all thirty contributions will be supplied.” The latter claim is unsupported. The ten existing excerpts and their publication permission remain usable. Completion of the next five remains conditional on the planned editorial work.

The next question becomes: can the remaining approved bilingual material be obtained within the opening conditions? Work backward from that joint requirement. An existing approved translation held by a contributor is one candidate provision; a newly commissioned translation with the necessary review is another. Test any candidate forward for source fitness, access, permitted publication, capacity and timely approval. Reducing the collection changes the promised scope and needs an authorized decision. The existing ten excerpts retain their qualified uses.

Suppose a contributor supplies suitable translations for the fifteen stories but permits exhibition use only. The translations retain their qualified content. The permission leaves online publication unavailable. An on-site search route would change the proposal. The curator can ask whether it serves the intended audience and seek any needed decision. The access finding can complete the present inquiry before either service is implemented.

The car-park trial records that timely guidance and desk coverage were both supplied in the stipulated interval. In the exhibition case, the analysis locates an unresolved provision and a restriction on public use. Each supplies an answer under its conditions. A change to the promised language coverage or access would need a separate decision.

#### PSDA.20:5.2 - A sufficient direct answer

The archive already has a current, qualified answer covering the exact approved excerpts, languages, access route and opening period. The remaining task is to apply the settled publication instruction. Use that answer and the responsible publishing practice. The existing answer supplies the necessary basis for that action.

### PSDA.20:6 - Bias-Annotation

**Scope:** Inquiry into participants’ intentions and dependencies. **Lenses:** **Onto/Epist** distinguishes participants, work, model content and evidence. **Prag** relates the finding to the receiving question. **Arch** identifies necessary provision and competing assignments. **Gov** examines permission and allocation. **Did** distinguishes an intelligible account from evidence of modelling capability.

Proposal bias treats the suggested technology as the problem's boundary. Agreement bias mistakes participants' recognition of a diagram for acceptance or feasibility of the work. Favorable-label bias hides unknown provision or offsets a protected condition against another benefit. Ask what each relied-on relationship means and which actual condition supports it; keep a contrary account or missing premise visible.

### PSDA.20:7 - Conformance Checklist

- Identify the needed answer, its receiving use and what the evidence must establish.
- Identify the recipient, purpose and needed provision. Establish the provider, means, acceptance and availability to the extent the conclusion uses them. Name any consequential gaps.
- A view preserves the modeled relationships relevant to the question; omitted display detail is not treated as an absent condition.
- Initial analysis assumptions remain distinguishable from observations, model relationships and unknown or conflicting grounds.
- The analysis result is interpreted in the original working terms, with its limited use and any newly discovered problem stated.
- For a candidate derived from a joint requirement, examine the whole combination under those requirements. For each combination at issue, state what the grounds establish about its feasibility or which condition remains unresolved.
- Changed assumptions or evidence reopen their dependent answers while independent results remain available. A sufficient result permits stopping.
- When a notation or solver is chosen, its language and analysis rules are compatible and its restrictions are preserved. Actual allocation, performance, permission and empirical effects retain their own grounds.

### PSDA.20:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Why it fails and what to do instead |
| --- | --- |
| Start by drawing every actor and goal. | A large picture can still miss the consequential question. Begin with the receiving use and add a relationship when it can change the answer. |
| Count favorable arrows or satisfied goals. | Counts hide the meaning and strength of the grounds, necessary combinations and protected conditions. Use the qualified consequence analysis and explain the returned profile. |
| Treat a supplier name as delivered work. | A named provider may lack access, time, competence or an accepted assignment. Use evidence of delivery to claim that work was supplied. To assess a proposal, establish its needed conditions or state the gap. |
| Interpret an assumption as a result. | “If installed” cannot establish an installation date. Retain the assumption with the conditional answer and return the missing investment or operating premise. |
| Repair a failed model by weakening the recipient's criterion. | This changes the problem without the required decision. Compare another means or make the proposed requirement change explicit. |
| Rebuild everything after one change. | Independent results can remain valid. Follow the changed relation and its downstream reliance, reopening the boundary only when the new question requires it. |

### PSDA.20:9 - Consequences

The inquiry may explain an incompatibility, establish what was provided, compare options within known limits or identify a question for a particular source. A newly discovered dependency can change the problem while leaving earlier conditional conclusions usable.

The cost is obtaining and interpreting the relevant accounts and relationships. Large or technical questions can exceed a manual model's useful reach. Reuse a suitable domain result, obtain competent help or narrow the present claim when that is the better way to answer the question.

### PSDA.20:10 - Architectural Rationale

Participants' intentions matter here because the same supplied entity can serve different purposes and require different conditions. Connecting provision to reasons on both sides explains why substituting a task, supplier or output can change the inquiry. Include the distinctions that affect the requested conclusion or its grounds.

Forward analysis establishes what follows under stated relationships and premises. Backward inquiry identifies possible means for a joint requirement. Interpret the result in the working situation. For a proposed combination, examine the joint conditions. An unexpected result can reveal an omitted question and change the candidate response.

Use PSDA.3 when several model contributions must be reconciled and PSDA.8 when consequence comparison is needed, including its qualitative branch. Here the model of purposes and dependencies helps interpret the situation and refine the question. Use a sufficient existing model or a settled comparison directly.

### PSDA.20:11 - SoTA-Echoing

The iStar Guide defines a language; the [PoEM 2009 treatment](https://www.cs.toronto.edu/~jenhork/Papers/Horkoff_PoEM_2009l.pdf) develops interactive modeling and forward evaluation. The [ER 2010 procedure](https://www.cs.toronto.edu/~jenhork/Papers/ER_Horkoff.pdf) adds formal backward search with human judgements and backtracking under stated structural restrictions. The manual backward question used here is an adaptation, not an implementation of that algorithm. If a named solver is used, select compatible language and analysis versions and preserve their restrictions, rather than applying older propagation tables to iStar 2.0 without a justified mapping.

The [subsequent systematic-versus-ad-hoc study](https://www.cs.toronto.edu/pub/eric/PoEM10-JH.pdf) gives reasons to attend to interpretation, coverage and training. It does not establish that a systematic procedure uniquely produces better understanding or more useful new questions. Use the model for the relationships and inferences it supports. Reliance on an operating fact or authorized decision requires evidence for that fact or decision.

These comparisons concern manual inquiry guided by a working question. A formal-analysis claim or claim about consulting effectiveness needs its own basis.

| Source contribution or alternative | Adoption and limit for this Method |
| --- | --- |
| iStar 2.0 language and its dependency/rationale views | Use the distinctions and integrity rules when that notation is chosen. The inquiry can also use prose; language conformance does not supply the domain facts. |
| Interactive forward evaluation and human judgement | Adapt the connection between a working question, stated initial values, relationships and an interpreted answer. Unresolved or conflicting grounds remain possible results. |
| Formal backward search | Retain the useful backward question and whole-candidate forward test. Do not claim an implementation or transfer old formal rules to a different language version without a justified mapping. |
| A sufficient technical model or qualified comparison | Use it directly for the question it answers. More intentional modeling is not a substitute for missing dynamics, accuracy bounds, probabilities or actual operating evidence. |

The car park and exhibition are constructed applications. Their allocations, capacities and permissions are stipulated. Use them to trace the reasoning. Evidence about actual service outcomes or solver performance must come from the corresponding work.

### PSDA.20:12 - Relations

- [PSDA.12](#psda12---recover-participants-concerns-and-affected-systems-for-a-decision-support-inquiry) supplies participant and affected-subject recovery when those contributions are missing. [PSDA.13](#psda13---facilitate-decision-support-inquiry-and-preserve-material-dissent) supplies professional facilitation where its conditions obtain.
- [PSDA.1](#psda1---generate-plural-problem-formulations) and [PSDA.2](#psda2---set-and-reopen-the-problem-boundary) support a changed formulation or boundary. A source-supported local question need not repeat those Methods.
- [PSDA.3](#psda3---construct-complementary-situation-and-option-models) makes several model contributions and their limits usable. [PSDA.5](#psda5---generate-decision-alternatives) receives a newly constructed candidate without inheriting feasibility or ranking.
- [PSDA.8:4.2.1](#psda8421---construct-and-question-a-qualitative-consequence-network) supplies the qualitative forward and backward analysis used here. The whole inquiry retains its purpose, initial assumptions, interpretation and return to the source situation.
- FPF C.40.CD develops the general relation between a changed problem and a changed way. FPF B.5.SD supplies substantive discussion when constructing the answer with others is the missing contribution.
- [OCE.11](Management%20DPF%20Suite/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce11---coordinate-organization-change-work-with-continuing-service) supplies organizational coordination when change work competes with continuing service. An allocation requires the applicable authority and an effective assignment.
- [PSDA.14](#psda14---prepare-and-return-a-decision-support-recommendation) can use the qualified result for a recommendation. A decision needs its authority, performed work its evidence, and a claim of effect grounds for the causal connection.

### PSDA.20:End

# Development-direction advising

> **Publication use:** a practice-use profile of this framework.
>
> **Practical result:** a supported recommendation, comparison or service boundary for a development-direction question, with its sources and limits, or a statement of the missing premise.




## PSDA.Advising:1 - Use this when

Use this profile when a distinct adviser helps a recipient consider what a specified person, organization or technical arrangement could develop. Identify the contribution the recipient needs, the horizon and the premises that bear on it. A useful return may be a direction, a set of alternatives, a proposed probe, a well-grounded request or a limit on advice.

Development-direction work also has an earlier, independently useful branch: constructing an opportunity when the worthwhile problem or possible contribution is not yet settled. Enter [Construct a Bounded Development Opportunity (FPF C.40.OCN:1)](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c40ocn1---problem-frame) directly for that question. A practitioner can use it independently to explore future engineering Work. It can return an opportunity, its dependencies and the question that remains open. A separate advising relationship has its own participants and purpose.

Enter this profile at the contribution the question needs. An opportunity under consideration, the subject that could develop, a recommendation and the subsequent choice each have different evidence. Use qualified work in human development, organization change, strategy, operations, AI engineering, safety or another relevant practice for its own conclusion.

A two-sentence return may suffice. “The available comparison covers internal development and configuration A. Ranking the external provider as well would require evidence about that provider under the same result, security boundary and horizon.” The recipient can use the bounded comparison now.

For a chooser with adequate alternatives and a settled decision question, use C.11 or the direct domain rule. Use a single qualified domain method when it answers the whole question. An unmanaged population or lineage without a local recipient or chooser is a subject for evolutionary inquiry. A research team considering an intervention has its own question, authority and required evidence.

When the recipient asks which programme to design for future participants, identify the design question. Use [PSDA.11](#psda11---bound-the-decision-support-engagement-and-authority-boundary) where the engagement boundary is unresolved and the learning-product design practice where a design result is needed. Keep the audience description as a design assumption. For personal advice, identify the prospective participant and use the premises about that person's later work, starting performance and support that bear the answer. Missing premises limit the advice; obtain more only when their contribution warrants acquisition. The [programme-design case (Engineering.Reference:11.2)](Engineering%20DPF%20Suite/ENGINEERING-DPF-SUITE-REFERENCE.md#engineeringreference112---recommend-a-programme-before-the-learners-are-known) shows the two uses.




## PSDA.Advising:2 - Enter at the missing result

Select the entry that answers the current question. Reuse adequate results. When a premise changes, reopen the contributions that depend on it.

| Working question | Start here | First useful return |
| --- | --- | --- |
| What useful future contribution could be possible? | [Opportunity-construction Method (FPF C.40.OCN:1)](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c40ocn1---problem-frame) | A candidate opportunity, dependencies, bounded reachability rationale and next question; no adviser is required. |
| Who is asking for what advice, and on what terms? | [Bound the advising engagement](#psdaadvising3---bound-the-advising-engagement), using PSDA.11 | A recipient/holder/horizon question and service boundary, or the missing condition. |
| Which facts about the developing subject affect the answer or its grounds? | [Recover only the relevant holder premises](#psdaadvising4---recover-only-the-relevant-holder-premises) | The holder's current configuration and facts or gaps that affect the requested conclusion. |
| Which specialist result is missing? | [Use the direct result-acquisition Method](#psdaadvising5---use-the-direct-result-acquisition-method) | A useful qualified answer and its limit, a worthwhile bounded request, or a blocker. |
| Which directions are actually live, and how do they compare? | [Keep a qualified live candidate set](#psdaadvising6---keep-a-qualified-live-candidate-set) and [Compare for this receiving use](#psdaadvising7---compare-for-this-receiving-use) | A bounded set, comparison, partial order or discriminating question. |
| What can the recipient responsibly consider now? | [Compose the bounded recommendation](#psdaadvising8---compose-the-bounded-recommendation) and [Return it for the agreed use](#psdaadvising9---return-it-for-the-agreed-use) | One or more explicitly scoped recommendation dispositions with basis and limits. |
| Has something changed that affects earlier advice? | [Reconsider only affected advice](#psdaadvising10---reconsider-only-affected-advice) | Retained, narrowed or blocked claims; a request to the practice responsible for an affected result; or a later recommendation. |

Use a qualified opportunity as a candidate basis for PSDA.5. PSDA.6, PSDA.7, PSDA.8 and PSDA.9 can supply premises for PSDA.14. Use PSDA.15 when follow-up or reassessment is needed. For each result, check that its scope covers the relevant developing subject, configuration, use and horizon. A link between methods identifies a possible contribution. A claim about completed work or authority needs evidence for it.




## PSDA.Advising:3 - Bound the advising engagement

Identify the recipient, the subject whose development is in question, the horizon and the intended use. Establish who will prepare the advice and who, if anyone, holds the choice it serves. Here the adviser is distinct from the recipient. In a self-directed inquiry, identify the contribution needed for the practitioner’s own work.

If the engagement question or authority boundary needs work, use [PSDA.11](#psda11---bound-the-decision-support-engagement-and-authority-boundary). Distinguish client, sponsor, developing holder, recommendation recipient and chooser only where the difference changes the advice, disclosure, protection or decision. An employer paying for a person's career service does not thereby become the recipient of every personal assessment; a sponsor preferring a provider does not settle the committee's choice.

For advice within the service, establish the applicable service scope, competence, conflicts, confidentiality, permitted reliance and referral or closure conditions. These are professional relationship questions in addition to generic permission. The [ICMCI competence framework v4.0, C.1.1–2, C.2.1 and E.3.5](https://www.cmc-global.org/sites/default/files/public/icmci_cmc002_competence_framework_version_4.0_1.pdf) supports agreed engagement content, client involvement and disclosure of material interests in management consulting. It does not authorize every adviser or prove that advice works.

For human career services, apply the actual professional conditions for informed participation, assessment competence, intelligible interpretation and appropriate referral. [NCDA's 2024 Code of Ethics, A.2, A.10 and E.2](https://www.ncda.org/aws/NCDA/asset_manager/get_file/3395) is a bounded professional source, not a universal rule for organizations or AI holders. Determine its applicability and any additional local requirements; do not infer consent or a client's capacity from a signed form alone.

AI assisting an adviser and AI being the developing holder are different cases. Where the [ICMCI AI Code v1.0, §§1.2, 2.2, 3.1–3.4, 5.1–5.4 and 7](https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf) applies, the consultant retains responsibility, checks material AI-assisted content, respects client-data restrictions and explains material AI use and its limits. The professional relationship governs those duties. A specialist premise in generated advice still needs evidence and competence for its subject.

When a missing mandate, competence, conflict treatment, consent or other condition prevents the service, identify that condition and the available narrower result. A scoped blocker can complete the request. Continue the safety, legal, emergency and other professional duties that apply to the actual relationship.

Open PSDA.12, PSDA.1, PSDA.2, PSDA.3, PSDA.4, PSDA.13 only when a participant, boundary, formulation, model, Method choice or disagreement affects the result or the grounds for relying on it.




## PSDA.Advising:4 - Recover only the relevant holder premises

Identify which facts about the developing subject and configuration affect a direction, protected condition, comparison or return. Use established facts and label assumptions. If a needed fact remains unknown, identify the conclusion it limits. Seek further evidence when its expected value warrants the burden.

| Developing holder | Premises that can matter | What cannot substitute |
| --- | --- | --- |
| Person | Representative later Work; current capability and evidence; access and expression conditions; target demand; resources; acceptable burden; intervention and transfer premises; consent and choice boundary. | A job title, course attendance, a generic competence inventory or another person's successful transition. |
| Organization | Needed contribution and receiving use; current Work and arrangement; positions and assignments; authority and interfaces; continuity; resources; candidate obtaining arrangements; strategy and protected conditions. | An organization chart, purchased platform, provider promise or one successful employee. |
| AI model, agent or composite arrangement | The changed object and its version; data, scaffold, tools or allocation; environment; evaluation validity; oversight and escalation; safety/security; baseline and protected conditions. | A human learning study, a benchmark from another configuration, a product label or a ranked recommender output. |

Human Capability Development demand, diagnosis and profile results can characterize a person and work. Retention or transfer needs evidence under the corresponding conditions. OCE and Operations results can describe an arrangement or contribution. A comparison of ways to obtain it needs evidence about those ways. For an AI configuration, establish that the evaluation covers the version and use at issue.

For each material premise, identify its subject, configuration, source, relevant time, uncertainty and intended use. For an unknown premise, say what remains unsupported. A finding about one configuration may leave others open.




## PSDA.Advising:5 - Use the direct result-acquisition Method

Use [FPF A.15.9 - Use or Request a Bounded Result from Another Practice](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a159---use-or-request-a-bounded-result-from-another-practice) for a needed external contribution and [FPF A.10](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a10---evidence-graph-referring-claim-bound-evidence-and-provenance-graph) when the source-to-use account is implicit or a needed reproducible account is missing. Derive the question from the recipient’s use when preparing advice, or from the unresolved dependency when exploring an opportunity independently. Establish what the available evidence supports as an answer. Before requesting more work, compare its attainable contribution, full cost and delay with the available continuation under A.15.9 and C.11.DUA.

To rely on an existing result, check what the qualified source established about the relevant subject, configuration, use and period. A MethodDescription can guide the work. The performer or practice qualified to assess the subject establishes the substantive result. The adviser assesses whether its grounds support the present use.

When an external result is worth obtaining, specify the missing contribution and its conditions. For the reliability case, request a comparison of internal development, a provider and mixed support for the ninety-day horizon, security boundary and continuity requirement. For personal development, identify the needed representative-work or transfer premise. For an AI configuration, specify the evaluation or safety judgement the question requires.

Retain a qualified result while another branch remains open. Identify whether the missing premise affects one claim, one candidate’s eligibility, a pairwise comparison or the whole-set recommendation. Trace dependence before applying a source change to other results.




## PSDA.Advising:6 - Keep a qualified live candidate set

If the useful future contribution itself is unsettled, use an adequate available opportunity or develop the missing contribution with the [opportunity-construction Method (FPF C.40.OCN)](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c40ocn---construct-a-bounded-opportunity). It searches neighboring uses, distinguishes a niche, a proposed provision promise and a worthwhile problem, constructs directions and supports, and exposes dependencies and reachability.

If the candidate directions are not sufficiently specified, use [PSDA.5](#psda5---generate-decision-alternatives) to make the advice-relevant alternatives explicit. Keep each direction's status explicit: a feasible direction under stated conditions, a conditional opportunity, a candidate probe or a fragment retained for combination. Keep ruled-out configurations and named gaps visible as such, not as eligible alternatives. Do not let an attractive but conditional opportunity enter a decision-ready set as if its dependencies had obtained.

Retain materially different ways to develop, obtain support, allocate effort, stage a change or continue the present arrangement when they bear on the question. Distinguish different means of supplying the same result from different worthwhile problems.

[OCE.8](Management%20DPF%20Suite/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce8---compare-human-ai-robotic-and-provider-arrangements-for-the-same-organizational-work-result) can supply the organizational same-result arrangement comparison after the required result, receiving use, horizon and acceptance premise are stable enough. It returns a changed or unjustified result premise to its owner; it does not supply this profile's whole opportunity search.

Use C.18 for a question about generation, an archive or a frontier under declared operators, descriptors and a retention or comparison rule. Use C.19 for a live pool governed by its current policy. To recommend a probe, identify what it could distinguish, its feasible exposure and protected conditions. To carry it out, establish the applicable authorization and operating conditions. Return a supported direction or limit when a probe is unavailable or would add too little.




## PSDA.Advising:7 - Compare for this receiving use

Use existing qualified comparisons. When work is missing, use PSDA.6 for values, PSDA.7 for uncertainty, PSDA.8 for consequences or PSDA.9 for robustness as needed. Name the actual candidate domain, compared subset and the characteristics, scales, protection, evidence, uncertainty and rule the comparison uses.

Use C.16 for characterization, C.11.CRC for a contribution relative to configuration and A.19.CPM for an applicable comparison mechanism. To rely on a G.5 selection, establish its candidate domain, eligibility, Method, evidence, result kind and closure. A ranked list alone reports an order.

Return the ordering the evidence supports, including an unresolved or partial order, a tie or several non-dominated directions. For a supported preference, state its advantage over relevant rivals and any conditions that could reverse it. If one direction alone is eligible, state the grounds for that result. Attribute material value differences and leave a shared weighting open unless its basis is established.

Human consent and transfer, organization continuity and AI safety remain unlike premises. A protected condition cannot be compensated away by a favorable total score. When its own justification is disputed, use [PSDA.6 §4.4](#psda6---represent-values-and-trade-offs) and C.11.DUA to compare the protected outcome, causal and measurement basis, threshold, additional protection and full burden. Carry the requirement recommendation and its actual amendment limit in the advice; current force still governs available action. Likewise, a comparison of internal development and one mixed arrangement does not rank an unexamined provider, another model version or a materially different probe.

When evidence is thin, first ask whether the missing distinction could change the advice or the grounds for it and whether obtaining it is worth its burden and delay. A small request naming the missing result, a retained set or a blocker may be more useful than another elaborate model. Use the comparison as evidence for the advice. A choice requires an act by its authorized holder.




## PSDA.Advising:8 - Compose the bounded recommendation

Use [PSDA.14](#psda14---prepare-and-return-a-decision-support-recommendation) to return what the recipient can responsibly consider now. Choose the form of return that fits the evidence and the recipient’s use.

| Return | When it is useful | Content that makes it more than a label |
| --- | --- | --- |
| Retained or ranked set | Several directions remain live and the current scheme supports their trade-offs, partial order or order. | The returned set and the comparison scheme, what preserves each direction, what remains unresolved and what could warrant narrowing. |
| Supported direction | Qualified premises justify preferring one direction for the named holder, use and horizon. | Its comparative advantage, the disposition of serious rivals, material limits and reversal conditions. |
| Bounded information-gaining probe | Resolving a specified uncertainty would matter to the advice or its grounds and the supplied probe basis supports proportionate information gain. | Question, possible distinguishing observations, exposure, feasibility, protected conditions and stop condition. Report selection and execution on their own grounds. |
| Smallest-result request or handoff | A supplying practice can provide a missing premise whose obtainable contribution warrants its whole acquisition burden for this advice. | The bounded result, subject, configuration and window, affected claim, and what would let advice resume; a useful answer can instead finish with its present limit. |
| Blocker | A missing, stale, inapplicable or unauthorized premise prevents the requested responsible recommendation. | What is missing, which stronger conclusion is blocked and which independent content remains usable. |
| Abstention | The requested recommendation premise fails or the service cannot responsibly supply that kind of advice. | The failed premise and appropriate receiving account or referral, without an invented adverse factual judgment about the holder. |

A mixed return may retain two directions and leave their complete ranking open. Add a request about a third direction only when the expected contribution warrants obtaining it. Name the subset and the conclusion each part supports.

Include the information the recipient needs to understand and use the particular recommendation or limit.

- the adviser, recipient, developing subject, question, horizon and intended use, including who holds a choice when that matters;
- the actual candidate domain, compared subset, exclusions and candidate gaps;
- each relied-on specialist result and relevant source edition, configuration, window and reliance limit;
- the declared comparison scheme, material trade-offs, protected conditions and inference to the return;
- uncertainty, dissent, evidence losses and unsupported extensions that can alter reliance;
- the supported conclusion and any further consideration, request, referral or separately authorized choice it calls for;
- the change in conditions or evidence that would reopen a claim where the receiving use depends on its continued applicability.

A short blocker can name the missing premise, the conclusion it prevents and who needs that result. A consequential recommendation may need a protected annex and a fuller account of its premises.

Keep each claim inside the narrowest material limit of the premises on which that claim depends. An evaluation confined to configuration A supplies no basis for B on its own. Independent evidence for B, or a supported transfer of the evaluation to B, can qualify the relevant conclusion. If the internal-development comparison does not depend on that evaluation, it can remain usable.




## PSDA.Advising:9 - Return it for the agreed use

Lead with the conclusion and its most important limit. Give the grounds at the level the recipient’s use requires. Identify the scope of any authority involved. When a decisive premise is protected, explain its effect on reliance without disclosing the protected content.

For an actual receiving-use problem, use A.2.9 to ask what the recipient needs to understand or do, what evidence would show that the return serves that use, and what smallest repair is needed. Making a conditional recommendation intelligible is different from persuading the recipient to accept it.

Delivery can complete an assignment to return the recommendation. To claim understanding, reliance, consent, choice, implementation or effectiveness, use evidence of the corresponding fact. Acknowledgement can establish receipt. A programme, course, organization-change plan, assignment, provider commitment or performed Work requires its own content and conditions, including authority where applicable.

After delivery, continue any contact, disclosure, referral, protection or closure duties governing the actual professional relationship. Sales, psychotherapy, teaching and implementation have their own scope and conditions.




## PSDA.Advising:10 - Reconsider only affected advice

Use [PSDA.15](#psda15---arrange-decision-follow-up-or-reassess-advice-after-a-change) when a changed premise can alter the advice, its grounds or the scope of reliance. Locate the premise and the claims that relied on it; preserve the earlier recommendation as an account of what was returned under its earlier basis.

For a known source-to-use relation, use A.10 when it remains implicit or a needed reproducible account is missing. When a material source change puts earlier uses in question, use A.10.1 if affected uses have to be discovered or several known uses need coordinated revalidation. Use direct subject evidence when the conditions change with the source unchanged. Use G.11 for currentness, decay and scoped refresh planning or reporting.

| Changed premise | Bounded response |
| --- | --- |
| Human assessment no longer covers the target Work or current person | Remove that assessment's support from the affected capability or intervention claim; retain the useful advice at its remaining strength. Obtain an assessment for that Work and the person's current conditions only when its contribution warrants the whole burden. Preserve unrelated organization or AI claims. |
| AI model/scaffold A is replaced by B | Check which evaluation, safety and contribution premises cover B. Use applicable evidence, or state which claims about B remain open. Retain independently supported conclusions. |
| Provider access or security condition changes | Reopen the affected provider or mixed-arrangement claim and any ranking that depended on it. Do not infer that internal development failed. |
| Consulting scope, conflict or disclosure conditions change | Revisit the affected service boundary and permitted use. Keep independently grounded domain conclusions within their scope. |
| An opportunity's useful problem or support dependency changes | Return to the corresponding opportunity claim; reassess any retained stepping stone and dependent advice. |
| A changed observation crosses the advice's stated threshold | Use the qualified observation and interpretation to retain, narrow, block or reopen the affected contribution; compose another recommendation only when needed. |

An existing observation, policy or decision may settle a follow-up. Where new observation, interpretation, professional contact or renewed advice is needed, establish the corresponding access, timing, burden and opportunity for response. An unavailable observation limits the advice that would depend on it.

The source-currentness responsibilities for this profile and its opportunity Method are specified in the [source-responsibility account](#psdareference13---keep-source-changes-and-case-changes-distinct). A change to the generation Method can require revising that Method; a changed fact about one holder normally requires only requalifying the affected application.




## PSDA.Advising:11 - Worked uses and stopping points

The examples below are constructed cases. Assumed specialist results illustrate what a warranted return would require; they are not results about actual clients, performed Work or demonstrated intervention effects.




### PSDA.Advising:11.1 - A ninety-day service-reliability question

A committee asks a separate advisory team which development direction the service organization should consider over ninety days. The committee is recipient and, under the case's assumed mandate, choice owner. The three live directions are internal development, an external provider and a mixed human–AI arrangement. Critical-service continuity, a security boundary and a capped reversible-probe budget are protected. The adviser discloses and resolves a material provider interest under the agreed engagement conditions before offering positive advice.

An operating account identifies the recovery contribution in question. Organization information describes relevant positions and interfaces. A qualified priority statement puts reliability before throughput for this horizon. None of those results compares the whole obtaining arrangements. The current OCE.8 Method is available to guide that comparison, but no adequate result for this client is supplied.

The adviser can return the following bounded result.

> Retain internal development, the provider and the mixed arrangement as directions for consideration. The available basis does not support their whole-arrangement ranking for this ninety-day reliability use and its continuity/security conditions. The operating and position/interface accounts remain useful inputs.

Use any current result that covers the stated use and protected conditions. If the comparison remains unavailable, the unranked answer can complete the inquiry. Select a further comparison only when its attainable contribution warrants preparation, supplier effort, interpretation, delay and displaced work. Use A.15.9 when external contributions are needed and identify their subjects and conditions.

Now consider a separate hypothetical continuation. A qualified whole-arrangement comparison and security result cover the three named directions. They exclude the specified provider configuration because it cannot preserve the security boundary. Internal development remains feasible but does not resolve the mixed arrangement's key uncertainty: whether permitted AI assistance can reduce the recovery queue without imposing an unacceptable verification burden or weakening fallback.

The supplied probe account covers the mixed configuration being considered, its bounded exposure and resource budget. It makes the distinguishing observations recoverable: representative recovery evidence, verification burden and fallback performance under the protected continuity condition. These conditions support proposing the probe. Its effect on recovery remains open. Compared with committing directly to either development direction, the probe can resolve that specific uncertainty at the bounded cost while preserving internal development as an alternative. The advice can therefore be:

> Consider the bounded mixed-arrangement probe first, retaining internal development. The supplied allocation, probe-feasibility and security results support this information-gaining return for the ninety-day reliability question. Throughput effect is still uncertain. Preserve service continuity, security and the probe budget; reconsider when representative recovery evidence or a relied-on premise changes.

The security finding excludes this provider configuration. The whole-set return draws on that finding as well as the internal/mixed comparison. A different provider, mixed configuration or probe needs its own applicable premises. Distinguish the committee’s choice, an authorized WorkPlan and performed Work.




### PSDA.Advising:11.2 - A person considering four months of development

An engineer asks a separate career adviser whether to develop cross-functional management capability or pursue a specialist engineering direction over four months. The person is the developing subject and recipient and holds their own development choice. The employer holds a separate assignment decision.

Establish what the representative later Work would involve. A qualified demand account might distinguish coordinating a cross-discipline review from supplying a difficult technical analysis. Current capability, accessible practice, time, consent, assessment limits and target-domain requirements can change which direction is plausible.

If only attendance and a course catalogue are available, return the missing intervention or transfer premise; do not prescribe the course or assert reachability. If qualified premises support both directions but not their order, retain them and name the distinguishing question, such as which representative Work the person can validly try within available support and time. The human branch uses current career information critically, as in [NCDG 2024, CD2 and CD3](https://www.ncda.org/aws/NCDA/pt/sp/ncdg_home_page); it does not infer learning transfer from career-information quality.

Before any separate advice request, the same person may independently use the [opportunity Method's human example (FPF C.40.OCN:5.2)](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c40ocn52---a-person-exploring-future-engineering-work). That entry does not require the distinct adviser assumed here.




### PSDA.Advising:11.3 - An AI or composite holder

An authorized team asks a separate recommending arrangement whether to modify a model, change a scaffold/tool configuration or alter human–AI Work allocation. Identify the object to be changed, its version, the intended environment, evaluation validity, oversight, protected conditions and receiving use. Model tuning, tool access and human–AI allocation are not interchangeable interventions.

Suppose a supplied evaluation supports scaffold A only in a bounded offline environment, while a proposed direction uses B with different tools. Identify B’s evaluation and safety premises still unsupported for that use. A’s score applies in its assessed offline configuration. A separately adequate organization-allocation comparison remains usable within its assumptions. Request B's result only if its obtainable contribution warrants acquisition for this receiving use.

If an applicable safety result excludes one configuration, exclude that configuration for the stated use. If evidence is merely missing, say so. A human course study supplies neither AI adaptation nor deployment safety. A recommender-system ranking can enter only as its separately qualified input; it is not the whole advice Method or deployment authority. Professional duties to human clients still apply where that service relationship actually exists.




### PSDA.Advising:11.4 - A population without a recipient, and an inadmissible engagement

An unmanaged lineage supplies no recipient or chooser for advice about which direction it should take. State that limit. Address variation, selection, reproduction, persistence and loss in the evolutionary inquiry.

A research team may instead ask which authorized experimental intervention to consider. That is a separate recipient-owned question whose scientific, safety, ethical and governance premises must be established; the evolutionary countercase supplies none of them.

Likewise, a sponsor's instruction to conceal a material conflict or to rank a harmful unauthorized option cannot be repaired by a better score. State what prevents the requested advice, what limited work remains permissible and any referral the applicable conditions require.




## PSDA.Advising:12 - Recognition, assurance and practical gain

Recognize this advising question when a distinct performer helps a recipient interpret development premises. A formed question can enter directly. For an opportunity still to be constructed, use the independent opportunity method. Current evidence or a known scope limit can supply a complete first answer.

Assurance is use-specific. Check whether the material premises cover the developing subject, configuration and horizon, whether the comparison and recommendation follow from them, and whether service, protection and authority conditions permit the proposed reliance. Apply the domain validation and independent assurance required by the claim, its consequences and the applicable scientific, professional or service conditions.

The recipient can see which direction or limit is supported, which alternatives remain and what could change the advice. A course, staffing decision, organization-change programme or AI deployment needs its own evidence and authority. A practitioner exploring opportunities independently may finish with a useful possibility and a question that distinguishes its conditions.

The [source-responsibility account](#psdasources3---source-responsibility-and-references) separates contemporary decision-support and professional sources, historical generation anchors, guidance from the practices supplying a needed premise, and application-specific results. It also states the bounded update responsibility.


## PSDA.Advising:End

# Cross-pattern applications

These constructed applications show how several pattern results can answer one working question. Each case supplies its own illustrative facts, permissions and results. Establish those premises for a real client and use evidence from the relevant work for a claim of effectiveness. A practitioner can combine, revisit or stop after the parts that answer the question.



## PSDA.Application:1 - APP-PSD-01 — A flood-pump calculation is not the whole investment answer



### PSDA.Application:1.1 - The question and the people who need the answer

In this constructed 2027 case, a municipal resilience office asks a separate inquiry team to advise the East-District Infrastructure Committee before the next flood season. The committee, called the board below, holds the funding decision. The team may arrange the agreed investigation and return advice. Funding and deployment require the authority for those acts.

Possible responses include pump renewal, distributed storage, changed demand management and acceptance of a bounded risk. The pre-season inquiry covers permanent and mobile pumping capacity, maintenance, staffing and safe access. Storage, demand measures and permanent relocation remain open beyond this comparison. Include downstream or long-term consequences that bear on the investment now under consideration.

With [PSDA.11](#psda11---bound-the-decision-support-engagement-and-authority-boundary), the team defines its assignment.

> Prepare a pre-season recommendation about the district pumping arrangement for the board's funding consideration. Make affected service concerns, operating conditions, protected limits and material dissent visible. Return a narrower comparison or a statement of the missing premise when the basis cannot support the whole investment question; the board retains the choice.

The team now has a recipient, a horizon and a limit on its authority. The competing formulations still matter to the advice.



### PSDA.Application:1.2 - Preserve the differences that can change an intervention

The team can readily consult operations and finance. Residents, emergency responders, maintenance contractors, downstream ecology staff and people with limited mobility may bear different consequences. With [PSDA.12](#psda12---recover-participants-concerns-and-affected-systems-for-a-decision-support-inquiry), the team traces supported consequences, identifies possible ones and records what it cannot establish. It checks whom the residents’ association represents. People unable to attend an evening meeting may have concerns the inquiry has yet to hear.

The resulting concerns support four different formulations through [PSDA.1](#psda1---generate-plural-problem-formulations):

| Formulation | What changes in the inquiry |
| --- | --- |
| Capacity shortage | Examine inflow, available pumping capacity and reliability; added capacity becomes a serious direction. |
| Unequal protection | Examine where exposure and access burdens fall, including reachable assistance; an aggregate hydraulic result is insufficient. |
| Maintenance fragility | Examine spares, staffing, contracting and coordination; a maintenance or staged direction may address a different cause from pump count. |
| Unsafe deployment | Examine placement, traffic, worker and downstream conditions; a restraint or differently bounded direction may be necessary. |

Using [PSDA.2](#psda2---set-and-reopen-the-problem-boundary), the team keeps the next flood season, material downstream effects and deployment conditions inside the inquiry. It records how long-term redesign and permanent relocation could affect the investment decision while leaving those choices open. Evidence that no feasible pumping option serves residents with limited mobility, or that flooding shifts outside the assumed area, would reopen the boundary.



### PSDA.Application:1.3 - Join inquiry and analysis without making one speak for the other

The team compares its capacity calculation, deployment scenario and map of attributed concerns using [PSDA.3](#psda3---construct-complementary-situation-and-option-models). Nominal capacity is still useful. The team cannot establish the mobile pump’s arrival time if the main road is unavailable. The concern map also distinguishes protecting property from providing reachable assistance.

Using [PSDA.4](#psda4---select-problem-structuring-methods-and-combine-them-when-needed), the team compares capacity analysis alone, an open-ended investigation and a bounded inquiry combining attributed concerns with technical analysis. The combination fits the pre-season remit if the team can check attribution and obtain qualified technical premises. To combine the results, the team checks that they refer to the same intervention, service and horizon. Frequency of mention measures mentions. A numerical preference weight needs its own basis.

Through [PSDA.13](#psda13---facilitate-decision-support-inquiry-and-preserve-material-dissent), the team replaces “the pumps can protect the district” with the nominal capacity its calculation supports. A separately consulted group asks whether assistance will remain reachable when roads fail. The board receives both attributed service concerns and the unresolved access condition. Establishing pump performance or reachable assistance requires evidence of that subject.

Inquiry and analysis can overlap. Suppose the proposed timetable freezes the model before a material service correction can reach the analyst. Using [PSDA.17](#psda17---reconcile-simultaneous-problem-structuring-and-decision-support-work), the team compares keeping that freeze, stopping all calculations and continuing independent calculations while a facilitator keeps the correction channel open. The case supplies a remit, an analyst and facilitator support for the third option. The analyst can revise the affected claim before it closes. At the deadline the board receives any correction or consequence still unresolved.



### PSDA.Application:1.4 - Use a numerical slice at its actual scope

With [PSDA.5](#psda5---generate-decision-alternatives), the team retains the no-new-purchase baseline `N`, fixed pumping `F`, mobile pumping `M` and the unfinished staged proposal `S`. To compare S, it still needs a specified first intervention. Storage and demand management are outside this pumping inquiry. The two-option calculation uses the following illustrative losses of pumping service and incremental costs.

| Direction | Loss with normal access | Loss with road loss | Incremental cost |
| --- | ---: | ---: | ---: |
| Fixed pumping, F | 2 | 3 | 8 |
| Mobile pumping, M | 1 | 9 | 5 |

The table gives model values. Baseline and staged options, reachable assistance and the distribution of protection need their own evidence. A monetary or measured-performance interpretation would require a basis for those units and observations.

The team uses [PSDA.6](#psda6---represent-values-and-trade-offs) for the stated trade-off and [PSDA.7](#psda7---represent-decision-relevant-uncertainty-and-evidence-limits) for the assumed probability of road loss. It compares consequences under [PSDA.8](#psda8---compare-consequences-of-decision-alternatives) and tests where the order changes with [PSDA.9](#psda9---test-robustness-and-sensitivity-of-decision-alternatives-and-their-comparison). The declared assumptions support a conditional answer. To attribute the trade-off to a participant, the team would need evidence of that participant’s judgement.

Let `p` be the assumed probability of road loss and `λ` the declared cost weight. Weighted loss is `2 + p + 8λ` for F and `1 + 8p + 5λ` for M. F has lower loss when `7p > 1 + 3λ`. At `λ = 0.5`, M has lower loss at `p = 0.2`, F at `p = 0.6`, and they tie at `p = 5/14`. For the board’s investment decision, the probability and trade-off remain unestablished. If the question is to derive a trade-off from expressed consequence comparisons, use PSDA.6:4.5 and :5.5. For an expected-utility calculation, use qualified or explicitly stipulated utilities and probabilities. PSDA.6:4.5.6 gives the additional operation for deriving utilities from a holder’s lottery comparisons.

The team can report the conditional ordering and the assumption at which it changes. Reachable assistance and the applicable protected conditions still need their own grounds before anyone could use the comparison to recommend a purchase.



### PSDA.Application:1.5 - Return the useful comparison and the whole-question blocker together

The team uses [PSDA.14](#psda14---prepare-and-return-a-decision-support-recommendation) to return the following recommendation.

> Retain fixed and mobile pumping for the stated comparison of service loss and cost. Their order changes with the declared assumptions. Access when the road fails, reachable assistance, the distribution of protection and the baseline, staged and other material options still limit a whole-investment recommendation. Include the separately attributed service concern in the board’s return.

This answers the question at the stated scope. If further inquiry is under consideration, use A.15.9 to compare an obtainable access or consequence result with proceeding on the available answer, narrowing the action, deferring or stopping. Request the result if its expected contribution before the board’s deadline warrants the work of obtaining and using it. The supplying practice qualifies its result for the named configuration and flood period. Establishing access can leave the value disagreement open.

The board could separately commission an access study. Receiving the recommendation, authorizing the study, funding a pump and deploying it are different events.



### PSDA.Application:1.6 - A changed premise changes the right claim

The board needs to know which evidence could reach it before renewed consideration. With [PSDA.15](#psda15---arrange-decision-follow-up-or-reassess-advice-after-a-change), the team compares an end-of-season review, continuous pump telemetry and a bounded pre-decision inquiry. Deployment permission, reachable assistance and the staged alternative require sources beyond telemetry. The last arrangement is selected here on the supplied availability of those sources, access, interpretation time and receiving date.

In a separate hypothetical continuation, the board authorizes the access study. The qualified result establishes that the specified mobile deployment is unavailable during the required flood period. This changes the feasibility premise of the earlier comparison.

The fixed-pump performance claim still applies to its original conditions. The earlier F/M comparison can explain the earlier advice. For a present investment recommendation, revisit the mobile deployment and its consequences. Assistance, staging and other unresolved questions retain their status. A newly identified affected group could change the service under consideration and require the team to reopen the boundary.

The follow-up identifies the consequence for the board’s decision. If the planned observation had been missed, the team could report what remained unknown about access during the flood window.



### PSDA.Application:1.7 - Continue the professional practice only when that is the question

Another inquiry team might copy the recommendation’s format and lose its limits. Use [PSDA.16](#psda16---decide-whether-and-how-to-change-problem-structuring-and-decision-support-methods) to examine whether its existing methods fit that work and what change, if any, is warranted. Use [PSDA.18](#psda18---deliberately-continue-and-change-problem-structuring-and-decision-support-culture) to examine how the practice continues across teams.

The constructed PSDA.18 case specifies the service assignments of the East and West teams, the inquiry and teaching methods, and separate March and April events. West receives a permitted packet and drafts an investment recommendation stronger than the packet supports. The teaching remit and available help support a guided qualification exercise for West. Experienced practitioners can continue with the compact route.

During the exercise, West distinguishes the usable F/M calculation from the unresolved staging and assistance questions. An independent observer later sees West carry a corrected concern and the limits of the comparison into one inquiry. This establishes that later use under its observed conditions. Long-term retention, profession-wide adoption, teaching effectiveness and flood outcomes each need evidence at the scope claimed. The late-correction method remains a proposal.

The board can use the calculation now, with an account of the affected groups, their service requirements, the other options and the operating conditions the calculation omits. How another team uses the advice is a separate practice question when that use matters.



## PSDA.Application:2 - APP-PSD-02 — Development-direction advice with unlike holder premises



### PSDA.Application:2.1 - Two useful entries, not one compulsory advising process

Use the [development-direction profile](#development-direction-advising) when one party must recommend a development direction to another. Identify the developing person or system and the recipient of the advice. Where a sponsor or later chooser matters, establish the relevant role and authority. Use the actual relationships and permissions to determine what may be shared, relied on or decided.

Use [Construct a Bounded Development Opportunity (FPF C.40.OCN)](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c40ocn---construct-a-bounded-opportunity) to explore worthwhile future work for your own inquiry. A conditional opportunity and the question that would distinguish its uses can complete that task. Advice becomes a separate result when a performer makes a recommendation for another recipient.

For advice, use the engagement and authority already established for the service. Use [PSDA.11](#psda11---bound-the-decision-support-engagement-and-authority-boundary) to clarify an unresolved assignment or authority boundary. Apply the competence, conflict, confidentiality, informed-participation and referral conditions relevant to that service. Distinguish AI used to prepare advice from an AI system whose development is being considered. Establish the basis and permitted use of any generated memo on which the advice relies.



### PSDA.Application:2.2 - Begin before the target contribution is settled

An engineering-services unit hears that a new model can handle long records. It treats adoption as a possibility to investigate. The unit has ninety days to explore related uses, technologies and characteristics within its confidentiality, independent-acceptance and service-continuity requirements.

The unit develops two possible opportunities.

| Candidate opportunity | Worthwhile receiving question | Dependency and first return |
| --- | --- | --- |
| Help an acceptance engineer identify which claims an evidence package supports. | Would tracing each claim to its premises improve qualification while keeping acceptance with the responsible engineer? | Retain manual indexing and bounded model-assisted retrieval. The unit still needs to establish permitted access to representative records for the relevant comparison. |
| Help shift staff identify unresolved exceptions and the next permitted handoff. | Would a clearer account improve the next handoff while preserving dispatch authority and fallback? | Retain a clearer human handoff and bounded model assistance. Capability for the representative work, workload and available review support remain unestablished. |

The unit can return both opportunities. Permission to inspect representative records would open the permitted inquiry. A refusal would close that processing route. A public sample can support a limited demonstration. A proposed access check still needs the authority to perform it and evidence of usefulness would come from the relevant evaluation.

Each opportunity addresses a different result. If the inquiry later asks how to obtain one result, its intended use and acceptance conditions provide a basis for comparing arrangements. At this stage the choice of which problem to pursue remains open. A candidate archive can help recover alternatives when needed.

The opportunity inquiry may finish here. If the unit later requests advice from another performer, use the established directions at their conditional strength. Use [PSDA.5](#psda5---generate-decision-alternatives) when the alternative set still needs construction.



### PSDA.Application:2.3 - A person exploring four months of engineering development

An engineer explores technical evidence review and coordination across disciplines. They can examine their own opportunity to make either contribution before asking for advice. A job title or course name alone leaves the future work unspecified.

In this case, statements of demand explain why both contributions might matter. For review, the engineer can access a permitted evidence set. Their capability and transfer to representative work remain unknown. For coordination, access to the relevant participants and competent feedback has yet to be confirmed. Course attendance and another person’s successful transition do not establish those conditions.

If the person asks a separate adviser for a recommendation, the return is:

> Retain evidence review and coordination as conditional directions. The present evidence does not establish independent review capability or transfer, and access to coordination practice and feedback is unconfirmed. Neither a course prescription nor a four-month transition follows.

The engineer can make their own choice. Their employer holds its assignment decision. Use the appropriate sources for the work demand, personal assessment, intervention and transfer. Career information can help compare opportunities. Evidence about learning must concern the relevant intervention and learner. If practice time changes, reassess the intervention or route that depended on it.



### PSDA.Application:2.4 - An organization needs a ninety-day reliability recommendation

A committee asks an advisory team to compare internal development, an external provider and a mixed human–AI arrangement for a service organization. The committee receives the advice and holds the later decision under its mandate. Over ninety days it gives reliability priority over throughput and protects critical-service continuity, security and the approved budget for a reversible probe.

An operating account identifies the recovery work. A separate account explains existing positions and interfaces, and the priority statement establishes what matters to the committee. These sources leave the whole-arrangement comparison open. The adviser uses [the profile’s guidance on obtaining a needed result](#psdaadvising5---use-the-direct-result-acquisition-method) to apply an adequate existing result or return the supported conclusion and its limits. Seek a further contribution where feasible and worth its full acquisition cost.

The adviser can already return the following comparison limit.

> Retain internal development, the provider and the mixed arrangement as directions for consideration. The operating, interface and priority accounts remain useful, but do not support their whole-arrangement ranking for the ninety-day recovery result and the security/continuity conditions.

The committee can use this account of the remaining directions and the comparison still missing. To rank them, the adviser needs a qualified comparison of the named options. Use an available result or obtain one when justified. OCE.8 can guide the work. A supplier performing it chooses and qualifies its method under the applicable conditions.

In a separate hypothetical continuation, qualified arrangement and security results cover the three directions. They exclude the specified provider because it cannot preserve the security boundary. Internal development is feasible. A bounded trial of the mixed arrangement could show whether permitted assistance reduces the recovery queue without excessive checking or a weaker fallback.

The case also supplies the trial question, the observations that could distinguish the alternatives, resources, exposure and stop conditions. Compared with committing now, a feasible trial can obtain the needed information at acceptable cost while internal development remains available. The team has addressed a disclosed provider interest under the service agreement.

The adviser draws on [PSDA.6](#psda6---represent-values-and-trade-offs) through [PSDA.9](#psda9---test-robustness-and-sensitivity-of-decision-alternatives-and-their-comparison) for the comparisons needed here. With [PSDA.14](#psda14---prepare-and-return-a-decision-support-recommendation), the adviser explains the advantage, the feasible rival, the uncertainty and the protected conditions.

> Consider the bounded mixed-arrangement probe first and retain internal development. The supplied arrangement, probe and security results support this information-gaining recommendation for the named reliability use. Throughput effect remains uncertain. Preserve continuity, security and the budget; reconsider when representative recovery evidence or a relied-on premise changes.

The separate security result excludes this provider. The internal/mixed comparison covers the two remaining directions for this use. Another provider or a materially different trial needs its own basis. The committee can receive the advice before considering or authorizing a probe. Evidence that the probe ran and produced an effect would concern later work.



### PSDA.Application:2.5 - An AI configuration changes while independent advice survives

A team considers changing a model, its scaffold or tools, or the allocation of work between people and AI. Each calls for evidence about the object and use being changed. A human training result concerns the participants. An organizational allocation may establish who does the work. AI performance and deployment safety need evidence for the relevant configuration.

Suppose the committee authorizes a bounded probe for configuration A, with specified continuity and oversight. The configuration owner can report material changes, specialist providers can qualify their effect on the premises, the adviser has time to interpret them and the committee can receive the revised advice in time.

A notice identifies configuration B. An observation from B is available, while the evaluation used for the original advice concerns A. Using [PSDA.15](#psda15---arrange-decision-follow-up-or-reassess-advice-after-a-change), the adviser determines which uses still have adequate grounds.

| Dependent use | What follows now |
| --- | --- |
| Internal-development claim independent of A's evaluation and the changed allocation | Retain it within its original service and horizon. |
| Earlier recommendation concerning A | Preserve the advice for A under its earlier conditions. To use the result for B, establish its applicability there or use independent evidence about B. |
| Advice to extend the probe or deploy B | State which evaluation, safety, security or allocation condition is still unsupported for B. Use the evidence for each stronger recommendation when it applies. |
| Observation and operational response | Apply the governing continuity or safety rule within the applicable authority. Obtain a decision from the responsible party if one is needed. A change notice identifies the configuration. |

If the candidate generator, its archive or its open-ended search changes, establish what changed in its operators, descriptors, retained candidates or governing policy and which use depends on it.

If an expected observation is missed, report which use now lacks evidence. Close the follow-up when the decision has ended and there is no continuing service or protection duty.



### PSDA.Application:2.6 - A population without a recipient, and a separate research question

In this example, the non-cultural population has no recipient or chooser for advice. Use the evolutionary account for variation, reproduction, selection, persistence and loss. Attributing a recommendation to the population would require a decision relation the example does not supply.

A research team can ask its own question about the population or compare possible experiments. Establish the subject and scientific question for that inquiry. To recommend or carry out an intervention, establish the applicable safety and authority conditions for that use. An evidence or authority gap can limit the recommendation while leaving a scientific finding available.



### PSDA.Application:2.7 - What remains the same across the branches

Across these cases the practitioner can return an opportunity, comparison or recommendation for an identifiable use. The evidence needed for human transfer, an organizational arrangement, an AI evaluation or a scientific intervention depends on the particular claim.

Return a supported direction with its conditions and identify the unresolved branches. Use the [profile](#development-direction-advising) for the advisory engagement and recommendation, the [opportunity Method (FPF C.40.OCN)](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c40ocn---construct-a-bounded-opportunity) for constructing an opportunity, and the relevant direct patterns for subject results. The [source-responsibility account](#psdasources3---source-responsibility-and-references) explains the contributions the profile takes from those sources.



## PSDA.Application:3 - APP-PSD-03 — An on-time report that cannot yet be used



### PSDA.Application:3.1 - Recover the difficulty before naming a solution

A team sends its weekly report before the agreed deadline. The timeliness indicator is green, but the planner must call colleagues to recover identifiers before assigning the work. Four of twenty rows selected for diagnosis need clarification. That observation identifies a difficulty in the selected cases. An estimate of its frequency across the organization needs a suitable sampling basis.

With [FPF B.5.PI](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#b5pi---initiate-inquiry-from-work), ask what prevents the planner from using the report under the agreed conditions. A complaint is evidence of what someone reports. A blank field is a property of a record. To establish an obstruction, connect the receiving work, the applicable requirement and what occurred. Use [FPF C.22.2](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c222---problemcard) to describe that problem and its outstanding factual or criterion premises.

In this constructed case the operations manager can authorize a temporary arrangement for the next planning cycle. The inquiry team can give advice. Separate authority would be needed to change another group’s deadline or commit its resources. Use [PSDA.11](#psda11---bound-the-decision-support-engagement-and-authority-boundary) for the remit and [PSDA.12](#psda12---recover-participants-concerns-and-affected-systems-for-a-decision-support-inquiry) to include the planner, preparers and identifier suppliers. The planner needs usable identifiers in time, preparers need a clear rule, and upstream staff may not yet have the requested information.

Using [PSDA.1](#psda1---generate-plural-problem-formulations), the team identifies three formulations that would lead it to inspect different evidence.

| Formulation | What would make it the current difficulty? | First discriminating check |
| --- | --- | --- |
| The handoff omits available information. | Identifiers existed before submission but the receiving material lacks them. | Compare the source information with the material actually sent and received. |
| Sender and receiver use incompatible identifiers. | Both sides have values, but the receiver cannot map them to the intended work. | Follow one affected identifier through the agreed correspondence and actual processing. |
| The deadline precedes information availability. | The identifier is not knowable at the required time under the current arrangement. | Compare the time information becomes available with the receiving work's real need. |

A fourth possibility is a recording defect. The receiver may have had usable information while the register displayed an empty field. Use a qualified comparison of the material sent and received, or inspect the relevant material when that evidence is missing. Its contents may settle the question, and correcting the register may complete a repair. Attributing assignment delay to the reporting rule needs evidence about that effect. A CRM is one possible intervention once the difficulty is clear.

With [PSDA.2](#psda2---set-and-reopen-the-problem-boundary), the team bounds this inquiry to the next planning cycle and the burden of obtaining the needed information. If the deadline itself obstructs the work, establish its grounds and who can change it. Improving compliance with an unsuitable deadline may worsen the problem.



### PSDA.Application:3.2 - Construct alternatives only where their consequences matter

Suppose the recording check reveals an obstacle to actual use. The team asks whether restoring the earlier handoff rule would reduce delay. It uses [PSDA.3](#psda3---construct-complementary-situation-and-option-models) to retain the concern account and timeline for the questions they answer. Use an adequate causal model if available. Where the relevant relations remain unspecified, use [FPF C.28.CM](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c28cm---construct-and-challenge-a-causal-model) to construct and assess them.

Specify the outcome and horizon. Let X be the handoff rule used, M whether the planner had usable information in time, Y the delay in assigning the work, and Z the load in the same period. R records the register’s completeness entry. S records selection of a row for diagnosis. Evidence about R can stand for M only on a qualified relation between the register and what reached the planner.

One account proposes X→M→Y: the new rule changed the identifier correspondence, which obstructed use and delayed assignment. Load may also have prompted the rule change and delayed work, giving Z→X and Z→Y. The common cause does not erase the proposed mediated path. Under this model, a correctly applied correspondence repair can remove one source of delay while leaving the load-related delay.

A rival account has Z→M and Z→Y, with Z→X explaining why the rule changed at the same time. It omits X→M. Under those mechanisms, restoring the earlier rule leaves the load-related delay. Both mechanisms could operate together. Test the proposed relations against process knowledge and evidence. The shared timing of a template change and a delay leaves their causal relation open.

Restoring the rule could change M in the first model. In the second there is no such path. An affected identifier and the times at which its information was available can help distinguish them. A disagreement about presentation of known facts may need no causal model. If a necessary process fact is missing, establish it from a suitable source if feasible and warranted, or report how its absence limits the causal answer.

Selection also matters. If rows enter the investigation because their information is unusable or their assignment is delayed, both M and Y affect S. Restricting attention to S=1 can create dependence between M and Y even without a causal effect between them. Its direction and size do not follow from the three-node shape alone. Use the whole-path rules of C.28.CM for the chosen graph. Address this selection before using those rows to infer a relation across all handoffs.

Distinguish what may have started, sustained or amplified the difficulty. A change in correspondence could start it. A continuing stream of unresolved rows with nobody assigned to correct them could sustain it. Repeated assignment changes could amplify the rework. Each hypothesis has its own outcome and period. To represent delay feeding later load, use Y(t)→Z(t+1) and the relevant earlier influences. A directed acyclic graph requires this time structure to be free of directed cycles.



### PSDA.Application:3.3 - Match the proposed action and the evidence to the question

Turning a blank field green changes the recorded indication. Applying a corrected identifier correspondence changes the handoff. Using [FPF C.28.MR](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c28mr---derive-an-intervention-consequence-by-mechanism-replacement), derive what each intervention implies under the specified mechanisms. Use [FPF C.28](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c28---causaluse-cal-causal-use-questions-identification-and-realizability) to examine the evidence connecting those mechanisms to this workplace.

A qualitative distinction may answer the question. For a quantitative causal effect, use [MMP.15](https://github.com/ailev/FPF/blob/main/DPFs/Foundational%20Thinking%20DPF%20Suite/MATHEMATICAL-MODELING-PRACTICE-DPF.md#mmp15---identify-an-intervention-effect-from-available-data) to determine what the model and available information identify. Choose adjustment, front-door, transport or another suitable argument according to its actual assumptions.

For an instrumental-variable argument, distinguish the assigned offer of help from the help used. With binary offer and use, the Wald ratio divides the difference in mean outcomes between offer groups by their difference in use rates. Give the grounds for relevance, exclusion and instrument exchangeability. With monotonicity and the applicable consistency and interference conditions, the ratio identifies the average effect among those whose use changes with the offer. That group need not include everyone who accepted, and its effect need not equal the effect of universal use. An invitation that teaches the work independently of use breaks exclusion. A small difference in use rates makes the ratio unstable. MMP.15:4.3.1 derives the local effect, :5.4 distinguishes offer, local-use and population effects, and Hernán and Robins give the assumptions in [*Causal Inference: What If*, Chapter 16, §§16.1–16.6](https://miguelhernan.org/whatifbook). Return the target effect, instrument, supported expression or remaining bounds and relevant uncertainty. If the identified effect differs from the requested one, state the difference and what further information or intervention could resolve it.

For an unresolved question that warrants research, use [RMP.1](RESEARCH-METHOD-PRACTICE-PRINCIPLES-FRAMEWORK.md#rmp1--decide-whether-a-question-needs-research-and-when-to-stop) to define it and the available basis. With [RMP.2](RESEARCH-METHOD-PRACTICE-PRINCIPLES-FRAMEWORK.md#rmp2--choose-a-criticism-bearing-research-design-or-stop), compare a feasible study with answering on existing evidence or commissioning no study. A rule comparison must address differences in load, information availability, timing and selection that could defeat the inference. A proposal establishes the study design. To report its execution or findings, establish what work was done and what follows from the evidence, including suitable archival observations where applicable.



### PSDA.Application:3.4 - Give a usable answer while uncertainty remains

With [PSDA.5](#psda5---generate-decision-alternatives), consider options for the live problems, including repairing the correspondence, restoring the former rule, providing temporary clarification, changing the deadline within its authority, or keeping adequate current work. A rule repair may address a proposed cause. Temporary clarification can protect the planner’s work while that cause remains open.

Use [PSDA.6](#psda6---represent-values-and-trade-offs) to establish what timeliness serves and whose work the upstream calls consume. With [PSDA.7](#psda7---represent-decision-relevant-uncertainty-and-evidence-limits) and [FPF C.11.DUA](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11dua---make-advice-and-evidence-demands-worth-their-burden), identify which uncertainty matters to the requested finding, its grounds or the choice at hand. Weigh the expected contribution of obtainable evidence against the full burden. A permanent rule change may require stronger evidence than a one-cycle workaround.

Suppose qualified staff have access, authority and enough time for one cycle of manual clarification. Operational evidence supports its ability to supply usable information. The manager can choose it for this cycle on its expected contribution, costs and limits while both causal models remain plausible. Agreement about the temporary response still leaves the original causal question open.

If clarification would impose an unacceptable burden on another group, or the identifiers cannot exist by the deadline, reconsider the temporary option or the deadline. With [PSDA.8](#psda8---compare-consequences-of-decision-alternatives) and [PSDA.9](#psda9---test-robustness-and-sensitivity-of-decision-alternatives-and-their-comparison), distinguish an option that works across the retained accounts from one that depends on a particular mechanism. Report the supported comparison even when the permanent alternatives cannot yet be ordered.

Using [PSDA.14](#psda14---prepare-and-return-a-decision-support-recommendation), the team can recommend one justified cycle of temporary help, correction of any established recording defect and deferral of the permanent rule choice while the mechanism remains material and unresolved. The manager holds the applicable decision. To report execution, establish what the participants did.

With [EXD.4](EXPLANATION-DESIGN-PRINCIPLES-FRAMEWORK.md#exd4---co-construct-and-repair-an-explanation-in-dialogue), explain why available information and the deadline matter and use the recipient’s response. A preparer’s statement that the identifier does not exist until Friday can change the formulation and recommendation when supported. If views still differ, return the disagreement, its grounds and its consequence.



### PSDA.Application:3.5 - Reconsider the affected claim after action

For the next cycle the manager assigns an observer with access to the sent material and processing history. The observer will report any recurrence before the following decision. Suppose the cycle is delayed again. Through [PSDA.15](#psda15---arrange-decision-follow-up-or-reassess-advice-after-a-change), distinguish the recommendation, choice, work performed and measurements. Establish execution from suitable evidence of the work. To use a completion flag for that conclusion, check what event the flag records and how it relates to the claimed action.

If the question concerns a trial of a reusable method, use [FPF A.3.1.WT](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a31wt---design-and-interpret-a-method-work-trial) to connect the intended task with the work and conditions of the occurrence. That can answer what was done in this cycle. For a further question of fit or transfer, use [FPF A.3.1.FT](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#a31ft---qualify-method-fit-and-transfer). For practical worth against feasible alternatives, use [FPF C.11.MV](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c11mv---compare-the-worth-of-a-method-option). Each stronger use needs the corresponding grounds.

The return depends on the supported distinction:

| What the follow-up establishes | What to reconsider |
| --- | --- |
| The record described a different event or value from the one needed. | Correct or replace the measurement and revise claims that relied on it. |
| Clarification was performed, but the proposed causal difference did not occur under the model's stated conditions. | Challenge that mechanism or its application; inspect live alternatives before strengthening the claim. |
| The action had its predicted effect but cost more or displaced more important work than the comparison allowed. | Reopen the value, burden or option comparison. |
| The chosen action was not performed, or its actual implementation changed the mechanism. | Address the execution or implementation question; the outcome does not test the unperformed action's effect. |
| The action and model conditions held, and one of the possible adverse outcomes occurred. | Update the evidence and any judgement that depends on it. One event under uncertainty need not invalidate the earlier decision. |

Several explanations can hold together. The evidence may also leave them unresolved. Revisit the particular record, model, comparison, work arrangement or formulation whose basis changed and return the supported finding or limit.

Operational work, temporary help and research can overlap. A causal graph represents proposed influences. A method combination identifies contributions that different activities need. A work history identifies the events that occurred and their order.



### PSDA.Application:3.6 - Make a usable aid for your own inquiry

For recurring work, start with what the recipient needs, such as usable input for next week’s planning. A ready account or short conversation can suffice. Consider building or revising an aid if repeated omissions or misunderstandings justify the work of preparing and maintaining it.

This construction adapts the problem-card and intervention exercises in Anatoly Levenchuk’s R4 guide. The filled cases illustrate how to build and revise an aid. Claims that a form improves decisions or that someone learned the method need evidence of the corresponding work and effect.

**Derive the questions from the intended use.** Identify the conclusion or action the recipient needs. Here the planner must choose a justified response when a green timeliness indicator coexists with unusable information. Work backwards from errors that could change that result. Distinguishing the register from the received report takes the material and its source. Distinguishing inconvenience from breach of a requirement takes the receiving work and the applicable criterion. Separate observations from proposed explanations. [PSDA.1](#psda1---generate-plural-problem-formulations) helps construct the formulations and contrasts that matter.

A first problem aid for this use can have four sections:

| Section and instruction | Filled report example |
| --- | --- |
| **What receiving work is obstructed?** Identify the work, affected people, occasion and requirement. State the undesirable condition without naming a preferred remedy. | The planner cannot assign four reported items without clarification before this week's planning meeting. Sending by the deadline is insufficient: the agreed input must identify the work to be assigned. |
| **What supports that account?** Distinguish testimony, inspected material and conclusions. Identify the cases, their sources and any missing or contrary evidence. | In twenty rows selected for diagnosis, the planner requested clarification for four. The sent and received material is available for inspection. Whether the identifiers existed before submission remains unknown. The selection does not establish an organization-wide failure rate. |
| **What else could explain or change the difficulty?** Keep alternatives that affect the requested explanation, its grounds, the next inquiry or the response. Describe an observed obstruction even when its cause is open. | Available information may have been omitted, the identifiers may differ, or the information may have arrived too late. A recording defect remains possible until the receipt is checked. |
| **What would count as useful improvement, and what is needed next?** State the receiving result and constraints; name the next consequential question, not every unknown. | The planner can identify and assign the required work in time without unbounded clarification work elsewhere. Inspect one affected handoff's actual information and availability time before attributing the delay to the reporting rule. |

The evidence section qualifies what can be asserted. Alternative formulations guide inspection. An improvement criterion can later test whether a response helps. Requiring a “Root cause” before it is known invites a guess. Requiring “Proposed software” excludes viable responses. Keep the entry that serves the recipient and allow an unknown to remain open.

A participant’s reported dissatisfaction can itself be the difficulty under inquiry. Record the planner’s repeated frustration on the basis of that report. Whether delivery failed, why and what would remedy it remain separate questions to investigate if needed.

**When an intervention account is needed, build it from the problem.** Carry forward the formulation, receiving outcome and relevant conditions. Identify hypotheses as such. For each live candidate, describe what it would change, how that could help, what it depends on and what evidence could alter the conclusion. Include temporary help, adaptation or continuation when viable. Use [PSDA.5](#psda5---generate-decision-alternatives) to construct alternatives and C.28.CM and C.28.MR for a needed causal account and its consequences.

For this report, the intervention aid can distinguish the following responses.

| Candidate | Proposed change and expected contribution | Conditions and comparison that matter |
| --- | --- | --- |
| Apply a corrected identifier correspondence | Change the correspondence used in preparing and receiving the report. If a wrong correspondence is the operative obstacle, this supplies usable identifiers without repeated manual clarification. | Recover the actual correspondence defect, obtain authority to change both uses and check the material produced. Compare usability and processing delay for relevant cases; a successful example alone does not estimate a general causal effect. |
| Provide one cycle of manual clarification | A qualified provider obtains and conveys the required information for this cycle. The planner may use that result while the original cause remains open. | The information must exist in time and the provider needs access and sufficient time. To assess performance, establish what arrived, whether it was usable and what work was displaced. Review or stop under the applicable mandate if the budget or availability fails. |
| Change the timing or content of the commitment | Where information cannot exist by the current deadline, obtain an authorized agreement about later completion or a usable preliminary report. This changes the obligation rather than making unavailable information appear. | The receiving work must tolerate the changed commitment. Observe its actual delay and burden, not merely whether the revised due date makes the indicator green. |

Keeping the current arrangement remains an option when its consequences meet the applicable criteria. A combination needs its own feasibility assessment. Temporary clarification can accompany a correspondence repair if the helper’s available time covers the combined demand and the other relevant conditions hold.

When follow-up is needed, specify **what will be examined, by whom and for which use**. Before the planning decision, for example, the assigned observer can check the received identifiers, clarification time and assignment delay for the agreed cycle. Establish what work occurred under which conditions. A failure may concern measurement, implementation, mechanism or value. Use the preceding table to locate the affected conclusion. Before-and-after observations can describe change. Attribution to the intervention needs suitable causal grounds.

**Apply the aid to a constraint question.** Two promised Friday sessions require three and two hours of the same room. The exercise gives a four-hour window, no preparation time and no option to overlap or shorten the sessions. Since 3 + 2 > 4, the two commitments cannot be met as stated. That calculation answers the feasibility question.

For the feasibility finding, give the two commitments, the room and the available window. If the coordinator must make the sessions possible, examine which conditions can change. Moving the two-hour session to Saturday needs a suitable slot and the relevant agreements. A second room needs suitable access for two hours at an acceptable cost. Under the original Friday constraints, a preference score cannot create the missing room-hour.

For a chosen alternative, establish the booking and the session requirements it must preserve. The arithmetic already establishes the original incompatibility. Saturday attendance requires its own evidence. If the second room is unavailable, retain the Friday finding and reconsider alternatives when the task needs a remedy.

A general aid can ask **“What grounds establish or could change this account?”** It can then accept a constraint argument or causal hypothesis. A section about interventions can still ask what each change would supply. For an aid limited to report handoffs, keep the narrower terms and state that scope.

**Test the aid where its use remains uncertain.** Choose cases that distinguish the uses in scope, including an unresolved claim where that matters. Existing suitable tests can provide evidence. For a new test of independent reading, let an intended user read a filled account without first supplying a missing explanation. Examine the difficulty, basis and warranted next result they recover. A request for the omitted availability time can expose missing content. An ambiguous use of “complete” may require a wording change. Disagreement with a criterion can be substantive. Repair the element that failed when a repair is needed.

Use [FPF C.41.TF](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c41tf---construct-a-checklist-template-that-preserves-its-questions) when the representation must preserve selected questions, answer meanings and references across views. Address a missing substantive question through the relevant practice. Preserve an adequate aid when a proposed revision adds work without improving the recipient’s use.

For a learning task, preserve an interpretable first attempt before giving a decisive cue. Offer feedback or another case when the learner’s work calls for it. To establish independent performance, examine the learner’s action and permitted support under the relevant conditions. [HCD.9](Human%20Capability%20Engineering%20DPF%20Suite/HUMAN-CAPABILITY-DEVELOPMENT-PRINCIPLES-FRAMEWORK.md#hcd9---perform-deliberate-practice-with-feedback) supports practice with feedback and [HCD.10](Human%20Capability%20Engineering%20DPF%20Suite/HUMAN-CAPABILITY-DEVELOPMENT-PRINCIPLES-FRAMEWORK.md#hcd10---choose-whether-and-how-to-vary-space-interleave-or-progress-practice) helps vary the practice. A useful aid, a justified intervention, evidence of learning and evidence of an intervention’s effectiveness can answer different requests.

## PSDA.Application:4 - APP-PSD-04 — Mira's development direction, programme comparison, and Guide


### PSDA.Application:4.1 - The working difficulty and the first bounded return

Mira prepares release-review handovers and has four months to improve that work. Her first idea is to learn more patterns. The needed contribution is to recognize when a specialist result already answers the question, identify a worthwhile missing result and check applicability before using a result for a changed configuration.

For this case, an HCD practitioner establishes the later-work demand and examines Mira’s representative performance with her checklist and technical reference, using qualified criteria from the target practice. She adequately qualifies three of five uses. In the two changed configurations she relies on unsupported transfer. These observations describe those tasks with those supports. Independent performance elsewhere needs its own evidence.

With C.40.OI, Mira defines the later work, four-month horizon and first direction question due Friday. Two short discussions are available, but the support provider cannot establish capacity this week. The existing HCD result already supports conditional personal-practice and review-support directions. Mira can return these now and identify capacity as unresolved. Seek further evidence when an attainable answer would justify the work for the intended use.

Mira’s current working week is 38 hours. At most three hours per week may be reassigned to development, with the displaced work identified. Restricted release data must stay protected, and technical acceptance still needs adequate grounds. Mira receives the advice and holds the direction choice. Her employer holds staffing authority.

Using C.40.OC, Mira specifies the following readings and conditions for assessing a direction.

| Coordinate and scale | Current reading in this case | Intended or protected condition |
| --- | --- | --- |
| Adequately qualified handovers, count out of the same five representative tasks; higher is better | 3/5 with the stated checklist and reference | 5/5 under the intended receiving conditions; a target, not an obtained result. |
| Unsupported technical acceptances, count in that task set; lower is better | 2/5 | Protected: zero in the claimed qualified task set. |
| Total work burden, hours per week; lower within the required output is preferable | 38 | Do not exceed 38; development displaces at most three hours of named existing work. |
| Mentor/specialist capacity, hours per week; lower consumption preserves capacity | Extra usable capacity is unknown. | Confirm the capacity before a direction or programme relies on it. |
| Additional work shifted to release colleagues, hours per week; lower is preferable | None from this proposed change, which has not begun. | Qualify who absorbs or stops the displaced work and the resulting burden; spare capacity is not assumed. |
| Information disclosure, permitted/not permitted for each recipient and purpose; prohibited use is inadmissible | The technical reference and anonymized examples are permitted | No raw restricted release data in the learning or advice service. |
| Transfer to unfamiliar configurations, qualified/unqualified/unknown for a stated task family | Unknown | Obtain HCD and target-domain evidence before claiming that transfer. |

Use each reading for the question it answers. Keep unknown performance, measured error, weekly burden and disclosure permission distinguishable. A combined maturity score would hide these constraints.


### PSDA.Application:4.2 - A complete pattern contribution, not “learn A.15.9”

With C.40.NU, C.40.PC and C.40.DC, Mira constructs two directions. In one she would learn to recognize and use the limits of specialist results. In the other a qualified technical reviewer would supply more of that contribution in the release service. Both could improve the handover. To attribute a new capability to Mira, examine what she can do.

The first direction uses [FPF A.15.9 — Use or Request a Bounded Result from Another Practice](https://raw.githubusercontent.com/ailev/FPF/main/FPF-Spec.md). Inspect an existing specialist result for its subject, configuration, use and window. Use the part that answers the question and identify any material limit. If a further contribution is attainable and worth the full burden of getting it, obtain it and qualify what returns. A narrower supported answer or a precise missing premise may complete the current task.

Given a release question and two specialist reports, Mira must determine which results are usable, under what conditions and at what strength. If a further contribution is worth obtaining, she drafts a bounded request. Where an adequate result is unavailable, she identifies the unsupported claim and returns whatever narrower finding the evidence permits.


### PSDA.Application:4.3 - Finite directions and a conditional later step

Mira’s existing checklist and reference make up `S0`. Direction A adds supported practice and later checks, with a prospective `S1`. B changes the review service. Compare both on the same starting condition, task family, horizon and protections. With C.40.JF, use qualified HCD evidence about Mira’s challenge, practice, support and transfer, and service evidence about review capacity. Check the joint availability of the contributions each direction needs.

| Finite candidate | Receiving result and complete burden question | Transition, reversibility, and options | Present conclusion |
| --- | --- | --- | --- |
| A: `S0` plus supported practice, producing prospective `S1` | HCD must qualify expected task closure and transfer; count preparation, attempts, feedback, retries, checks, mentor work, displacement and total weekly burden. Preserve the critical-error and disclosure constraints. | Setup and later checking remain prospective costs. Identify the cost of stopping the segment and restoring displaced work before claiming reversibility. Later unfamiliar-case practice is an option only if its prerequisite is qualified. | Conditional direction, not a qualified improvement or programme. |
| B: `S0` plus a proposed review-service contribution | The service practice must qualify output, response time, capacity, continuing cost, Mira's coordination burden and effects on other supported teams. The same protected errors and disclosure limits apply. | Establish actual provider availability and withdrawal consequences; retained external support is not unaided personal performance. | Conditional support-direction alternative; do not relabel it personal development. |
| Later unfamiliar-case practice after A | For a planned step, use the stated prospective `S1` and keep its result conditional. For an actual transition, use the `S1` actually obtained and reconsider any difference. Qualify the new task, support, time and transfer evidence from that starting configuration. | Keep the first step's incurred costs in history if it occurred. Compare the next increment separately; do not credit the first gain twice or charge hypothetical setup as spent. | Candidate enabling relation; HCD evidence must support the prerequisite and transfer claim. |

For a stronger finite comparison under C.11.CRC, use a common basis covering results, resources, affected people and teams, distribution, protected conditions, interactions and evidence limits. The descriptions alone leave a Pareto or aggregate-savings claim open. With C.40.OP, Mira can retain A, B and the conditional later step and specify what would justify reconsidering them.


### PSDA.Application:4.4 - Advice and the two distinct choices

Suppose Mira asks a separate career-development adviser for help. Using PSDA.19, the adviser relies on established competence, Mira’s participation, confidential individual feedback, an employer summary restricted to agreed work implications and the applicable treatment of provider interests. The case supplies those service conditions. Sponsor payment alone would not authorize transfer of Mira’s private assessment to the employer.

The adviser can use the established direction question and the available results. While mentor capacity and transfer remain unresolved, both directions are conditional. Recommend another inquiry or trial if its attainable contribution warrants its full burden. In a later scene the required capacity, comparison and authorization are available. Mira chooses personal-development direction A within those resource and evidential limits. Her choice is a further event.

For the selected direction, the HCD practitioner uses [Compose and Compare Human Capability-Development Programmes for Later Work (HCD.2)](https://github.com/ailev/FPF/blob/main/DPFs/Human%20Capability%20Engineering%20DPF%20Suite/HUMAN-CAPABILITY-DEVELOPMENT-PRINCIPLES-FRAMEWORK.md#hcd2---compose-and-compare-human-capability-development-programmes-for-later-work) with Mira’s profile, later tasks, participation and qualified support. This constructed continuation supplies two feasible programme candidates.

| Programme candidate | Qualified resource and support position | Expected contribution and limit |
| --- | --- | --- |
| Coached whole-task sequence | Three learner hours and one mentor hour per week, including preparation, attempts, feedback, correction, retries and checks. The provider confirms that one hour is available. | More of the early attempt receives immediate guidance. Later independent and unfamiliar performance remains to be tested. |
| Reference-supported individual sequence with scheduled expert checks | Three learner hours and half an expert hour per week, including the same categories of learner and provider work. The references and checking access are available. | More of the attempt occurs before expert feedback. Check a changed condition and address errors that occur. Lower expert time leaves comparative effectiveness open. |

Both proposals fit the remaining four-month horizon after time for inquiry and choice. The case supplies an authorized reassignment of three weekly hours from reporting that can be suspended without shifting work to colleagues or losing a required release output. The 38-hour limit is preserved. The allocations include setup, access, assessment, stopping and restoration. Expected performance and transfer remain uncertain. Live release acceptance requires its own grounds and authority. Missing displaced work, unequal coverage of costs or an unconfirmed provider hour would limit this comparison.

If Mira requests programme advice, the adviser can use the HCD.2 comparison. With its qualified choice inputs, Mira selects the reference-supported sequence with scheduled expert checks. A chooser who already has the needed comparison can decide directly. Choosing the earlier development direction left this programme choice open.


### PSDA.Application:4.5 - Guide realization, performed attempts, and evidence

For Mira’s selected programme, the author uses Learning Product practice to prepare the instructional Guide. With [LG.02](#psdasources41---learning-product-source-access), the author places the initial distinction, worked use and later variation at stable addresses. [LG.05](#psdasources41---learning-product-source-access) develops recognition, explanation, action, result, checking and practice around a worked contrast. With [LG.03](#psdasources41---learning-product-source-access), the author checks what the fragment enables the learner to do next.

A unit shows a completed bounded request and why one existing report applies. The practice case changes the receiving configuration. Mira must decide whether to reuse a result, narrow it or request another, produce the supported answer and check the relevant conditions. An unfamiliar case must make applicability matter to the answer. This specifies Guide content. Programme performance and learning require evidence of what happened.

In a later constructed observation, Mira uses the allowed reference and qualifies all five familiar tasks. In one unfamiliar configuration she still makes an unsupported transfer. Report the familiar-task result under the observed conditions. Use HCD for diagnosis and transfer, C.40.RQ for the stronger unfamiliar-work claim and any dependent path, and PSDA.15 for advice relying on that claim. A claim about reduced cognitive load needs its own evidence.

The following sequence traces the results used in Mira’s branch.

> HCD evidence → Core opportunity/path candidates → PSDA direction advice when requested → authorized direction choice → HCD.2 programme comparison → PSDA programme advice when requested → authorized programme choice → Learning Product Guide → performed attempts → HCD and representative-Work evidence → affected reconsideration.

A reader may enter at an existing result or finish when the requested finding, proposal or choice is supported.


### PSDA.Application:4.6 - A direct programme-level entry

A learning-product author may already have a comparison of programme variants, as in the Foundations example. Use that comparison directly if it covers the author’s question, the intended audience and the proposed conditions. Audience assumptions can support a design before an individual is known. A personal programme comparison requires the learner’s later work, starting evidence, participation and support. Use the author’s applicable authority when selecting a programme for production. Claims about actual learning or effectiveness require evidence for those claims.


## PSDA.Application:5 - APP-PSD-05 — An engineering company's next development opportunities


### PSDA.Application:5.1 - One receiving question, several kinds of direction

Larch Engineering wants to improve a monitoring service over nine months while current customers can continue using it. Its operations lead receives the inquiry. The authorized management body retains any later commitment. With C.40.OI, the team sets a two-week return, protecting confidentiality, safety and service continuity. One day of combined engineering and operations effort, including preparation and interpretation, is available. Reviewing existing qualified reports can give a first comparison and expose a resource clash. A new platform benchmark would leave the wider support arrangement unresolved in this window. Return the conditional directions and any missing premise.

The initial proposal is to replace the analytics platform. Using C.40.OC, the team identifies what would make a direction useful, including detection on the customer equipment, false alarms, response time, operator and provider effort, transition and operating resources, interruptions, security, effects on customer groups and maintainability. Establish the relevant scale, direction, period and evidence for each. Use engineering and operating readings where available and identify the unknowns.

With C.40.NU the team varies the kind of change as well as the vendor. It uses C.40.PC for the receiving problem and C.40.DC to connect each proposed contribution to its support.

| Direction | Possible contribution and support question | Source needed for the stronger claim |
| --- | --- | --- |
| Market/use | Could the current service address a different evidenced customer need on the existing platform? | Use qualified market and domain evidence about the need, affected customers and acceptance. A market commitment requires the responsible strategy authority. |
| Technology | Could a different detection component improve the named operating result? | Engineering and AI evaluation qualify that component in the actual equipment/data configuration; safety and security retain their constraints. |
| Human capability | Could operators better distinguish a false alarm from an actionable signal? | HCD qualifies later tasks, current performance, supports, transfer and feasible development. |
| Organization | Could a revised escalation and review arrangement reduce missed or incomplete handovers? | OCE compares whole arrangements for the same required result, including provider responsibilities and actual capacity. |
| Provider | Could a specialist service supply the missing contribution? | Establish what it can deliver, availability, response times, dependency and withdrawal conditions. For a claim about operating provision, use evidence of the actual service. |
| Platform/support | Could data provenance, a simpler interface or a maintained reference make current detection usable? | Systems/Platform Engineering supplies architecture and realizability; OPS supplies continuing operating and support conditions. |

For a question about ways to obtain one already defined result, use an adequate comparison or go directly to [OCE.8](https://github.com/ailev/FPF/blob/main/DPFs/Management%20DPF%20Suite/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce8---compare-human-ai-robotic-and-provider-arrangements-for-the-same-organizational-work-result) to develop one.


### PSDA.Application:5.2 - Joint limits and a useful return

Suppose the technology transition and the provider transition each require six distinct hours per week from the same specialist. Only eight hours are available during their overlap. Each direction may still be feasible alone. Together they require twelve hours and cannot meet that shared condition. With C.40.JF the team can establish this incompatibility while leaving the choice between the directions open.

A sequential branch under C.40.OP can remain conditional. For the second step, distinguish the proposed result of an unperformed first step from the result it has delivered. A full C.11.CRC comparison also needs the contributions, transition and operating work, effects on customers and protected conditions. Specialist hours suffice for the overlap finding.

The team reports the receiving problem, qualified directions, scope of available evidence, incompatible overlap and missing basis for a sequential transition. If advice is requested, use existing applicable service terms or PSDA.19 to establish them. The adviser can then return the bounded recommendation. Strategy authority governs commitments. Use the relevant organization, human-development, engineering and operations practices for their own work.

Suppose a provider later removes access to one data class. Using C.40.RQ, identify the directions that used it. The provider-supported route may need narrowing or withdrawal, while a separately supported operator-practice opportunity can remain viable. The responsible parties apply existing protection and operating duties. Use PSDA.15 for any advice that relied on the lost access.


## PSDA.Application:6 - APP-PSD-06 — Unlike subjects, exact recipients, and an anti-case

Each branch can start with the contribution its inquiry still needs. The shared opportunity question does not imply a common development mechanism. For advice by one party to another, also establish the recipient, the adviser’s role and the applicable service terms.


### PSDA.Application:6.1 - Community and governance

A professional maintenance community wants participating groups to share incident experience more reliably. Its coordination circle receives the inquiry within a limited remit. Consider changes in examples, contributor support, review or communications. Use cultural and governance evidence for participation, transmission, retention of variants and proposed intervention, with FPF C.36 for a question about professional culture.

A workshop record can establish what happened in that session. To claim a change in community practice, follow the relevant later uses. An opportunity hypothesis with its untested effect can answer the first inquiry. Seek more evidence or coordination when its attainable contribution warrants the full burden. If no entitled recipient is established for community-wide advice, report that limit. Give the supported recommendation to its intended recipient. If carrying it out requires a decision or permission, state who holds that authority when known and whether it has been exercised. Attendance by itself leaves consent open.


### PSDA.Application:6.2 - AI/model or composite arrangement

A service team receives the inquiry about an AI-assisted review configuration. Specify the model, data, scaffold, tools, code, oversight and operating arrangements that matter to the use. With the Core opportunity methods, consider changes to parameters, data, tools, evaluation or oversight alongside support that does not use AI.

The team can return a proposed configuration and its possible contribution, a qualified result or a precise evaluation gap. Use engineering and AI evidence for performance, safety, security, data access and operation. To transfer a result from A to B, establish applicability to the relevant differences. A shared provider or model family alone leaves that question open. Claims about a human learner require their own subject and evidence.

The designated holder has authority over deployment or a trial. If the adviser uses AI to draft advice, apply the service’s information-use and review obligations. Evaluation of the proposed configuration remains a separate contribution.


### PSDA.Application:6.3 - Engineered platform or facility

A laboratory-platform owner asks which change could improve access to a shared instrument while preserving calibration and safety. With C.40.OI, specify the facility configuration, receiving experiments, users, horizon, downtime, resources and protected conditions. Consider changes to scheduling, support, interfaces, a component or a provider.

A qualified support opportunity or conditional transition may answer the inquiry. Use systems or platform engineering for architecture and realization, and operating, measurement and safety evidence for their corresponding claims. A changed interface can make an existing measurement capability accessible. Establish any claimed new capability for the measurement and conditions in question. Fewer support calls alone leave calibration open. Other independently supported improvements can still proceed within their authority.


### PSDA.Application:6.4 - Research programme or body of knowledge

A research lead receives a question about the next contribution to a reproducibility programme. Identify the research arrangement or body of knowledge and the contribution sought, such as a replicated result, a corrected claim, a discriminating experiment or a reusable analysis.

Use the Core opportunity methods to construct and retain worthwhile possibilities under the stated horizon and burden. Use the relevant research methods and evidence for criticism, reproducibility, formalization and empirical inference. A proposed research sequence can guide work. To report a finding, establish what the work and evidence support. If a source claim changes materially, use C.40.RQ to examine dependent conclusions. Use A.10.1 when affected uses must be discovered or several known uses need coordinated revalidation. For a known, explicit reliance, reassess it directly where the grounds suffice. Return the supported finding or precise open question.


### PSDA.Application:6.5 - Non-cultural population or lineage

In this evolutionary example the population has no recipient or chooser for advice. Use the scientific account for variation, reproduction, selection, persistence and lineage. Under PSDA.19, a recommendation to the population would require a service relation absent here.

If a researcher asks whether to change an experiment or conservation intervention, the researcher or designated organization receives that answer. The population remains the affected subject. Establish the scientific evidence, welfare and protection conditions, applicable governance and authority relevant to the proposed intervention.


### PSDA.Application:6.6 - What the contrast preserves

In each branch identify the subject, requested contribution, horizon, protections and source limits. To use a mastery assessment, mandate, benchmark, calibration or research finding in another branch, establish what makes it applicable there. If a premise is missing, return the narrower supported claim, request an attainable missing result if warranted, or explain why the requested advice cannot be given.


## PSDA.Application:7 - Choose development support without assuming an office

The following example supplies the staffing, permissions and time available for the comparison.

Four project teams repeatedly revise commitments after discovering an unchecked premise in the estimates. The director proposes a development office. The six-week undertaking has two aims, improving the estimation method and helping the leads apply and develop it while delivery continues. The teams need to form, test and revise the premises behind their estimates.

Using [PSDA.1](https://github.com/ailev/FPF/blob/main/DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md#psda1---generate-plural-problem-formulations) and [PSDA.2](https://github.com/ailev/FPF/blob/main/DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md#psda2---set-and-reopen-the-problem-boundary), the adviser distinguishes missing technical knowledge, too little opportunity to challenge a commitment, and difficulty turning a weak signal into a useful inquiry. Each points to a different possible need. Records or a participant’s correction can establish what occurred. Attributing the repeated failure to one mechanism needs evidence for that causal claim.

With [FPF C.40.JD:4.5](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c40jd45---synthesize-the-organization-from-the-work-and-conditions), identify the work the teams need to retain locally and the specialist help, common resources and wider decisions they require. Use [FPF C.32.MWA.PP](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c32mwapp---construct-and-compare-method-performance-and-provision-arrangements) and [OCE.8](https://github.com/ailev/FPF/blob/main/DPFs/Management%20DPF%20Suite/ORGANIZATION-CHANGE-ENGINEERING-PRINCIPLES-FRAMEWORK.md#oce8---compare-human-ai-robotic-and-provider-arrangements-for-the-same-organizational-work-result) to compare proposed ways to perform and supply the whole result, testing their feasibility. Here the evidence supports the managers’ coaching competence, and each has one protected hour per week for local work. The common subject question still requires specialist help.

Compare two arrangements for six weeks. Distributed support uses the existing managers and a shared specialist. The proposed office initially uses the same specialist and local practice and adds two weekly coordination hours. No additional specialist capacity has been secured. The table gives the recurring specialist work.

| Specialist contribution | Managers with distributed help | Proposed office using the same specialist |
| --- | --- | --- |
| Existing commitments | 2 hours | 2 hours |
| One genuinely shared inquiry session | 2 hours | 2 hours |
| Four distinct case reviews, half an hour each | 2 hours | 2 hours |
| Additional office coordination | 0 hours | 2 hours |
| Total against six available hours | 6 hours | 8 hours |

A single session can serve all four teams because they need the same distinction and may share the material. The local reviews remain separate. This case supplies protected team time, permitted material, management authority and the ability to receive the result. Given those other conditions, the six-hour total fits the specialist’s available time.

The adviser recommends distributed support for the six weeks. The proposed office needs eight specialist-hours against six available. Concentrated demand, a reusable service, another qualified provider or a different coordination cost could change the comparison. An external provider whose access and availability are unknown remains conditional. With [PSDA.9](https://github.com/ailev/FPF/blob/main/DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md#psda9---test-robustness-and-sensitivity-of-decision-alternatives-and-their-comparison), test consequential changes when needed. Use [PSDA.14](https://github.com/ailev/FPF/blob/main/DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md#psda14---prepare-and-return-a-decision-support-recommendation) to return the recommendation to the director for the separate choice.

If confidentiality later prevents a common session, four separate two-hour sessions require eight hours. With two hours for case reviews and two already committed, the total is twelve against six available. The distributed proposal no longer fits. Revisit its provision or scope. The previously established technical distinction is still available.

When the chosen arrangement is authorized for use, assess its performance from the work carried out. In a contrasting case, examine how a lead identifies a consequential premise, obtains the missing subject answer and forms a justified commitment. This may support a conclusion about that lead’s contribution under the observed conditions. Evaluate the revised method and any stronger capability claim on their respective grounds. Use [PSDA.15](https://github.com/ailev/FPF/blob/main/DPFs/DECISION-DESIGN-PRINCIPLES-FRAMEWORK.md#psda15---arrange-decision-follow-up-or-reassess-advice-after-a-change) and [FPF C.40.RQ](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c40rq---requalify-changed-opportunities) to revisit advice or opportunities that depended on a changed premise.

## PSDA.Application:End

# Decision Design Principles Framework Sources and Edition Notes

## PSDA.Sources:1 - Source arguments and refresh

Each pattern’s SoTA-Echoing section explains the question its sources address, the contribution used, alternatives, trade-offs, limits and grounds for reconsideration. The table locates those arguments. Consult the relevant one when a claim relies on that source use.

Use PSM and decision-analysis studies for the claims and settings they investigate. Professional sources can qualify conditions within their remit. The constructed cases illustrate reasoning with their supplied premises. Use observations of the local outcome to report what happened. To attribute that outcome to an intervention, establish the causal link. For an effect estimate from another setting, establish that its causal grounds apply to the receiving use.

Use a source result for the subject, configuration and question its grounds cover. When an input changes, identify dependent inferences and preserve independently supported conclusions. Seek a further result if its attainable contribution warrants the full cost of obtaining and using it. FPF A.10 addresses a known reliance when the source-to-use relation is implicit or a needed reproducible account is missing. Use A.10.1 after a material source-claim change when affected uses must be discovered or several known uses need coordinated revalidation. Use G.11 for a question about currentness. Base scientific, legal, engineering and professional conclusions on their applicable evidence and competent authority.

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

A publication year helps identify the source. For a currentness claim, establish which portion was inspected, when and for what use. An older result can still answer its original question. Later evidence may change a particular conclusion or its applicability.

## PSDA.Sources:2 - Citation and limits

Cite the edition used. The following citation identifies this working edition.

```text
Anatoly Levenchuk, with AI-assisted development and review.
Decision Design Principles Framework.
Working edition, 24 October 2026.
GitHub repository: https://github.com/ailev/FPF
```

For a specific contribution, add its PatternID and title, for example PSDA.14 - Prepare and Return a Decision-Support Recommendation. Include the edition date and a permanent link or stored copy when the wording matters.

The framework contains nineteen methods and guidance on selecting and combining them. Markdown section links use the published headings. Check the maintained destination if a title or source changes.

## PSDA.Sources:3 - Source responsibility and references

The table identifies the source portions used for development-direction advice, including opportunity construction supplied by Core. Their stated qualification date is **2 September 2026**. Use the relevant contribution within its scope and reassess a consequential reliance when its source or use changes.

| Source and inspected portion | Selected role and affected content | Limit and local reopen |
| --- | --- | --- |
| [Keeney, Value-Focused Brainstorming, 2012](https://pubsonline.informs.org/doi/10.1287/deca.1120.0251), publisher abstract | Historical generation anchor: explicit values inform alternatives; individual generation can precede group anchoring. Opportunity Method §2. | Not a current-prevalence claim or general reachability theory. Reopen if a stronger generation line changes the inquiry's useful action. |
| [Phillips, Decision Analysis for Practitioners, 2025](https://pubsonline.informs.org/doi/full/10.1287/deca.2025.0356), “Requisite Decision Models,” “Decision Conferences and Workshops,” “Decision Models as Transitional Objects,” “Decision Analysis Technology” | Contemporary practitioner synthesis for purpose-dependent future exploration and selective use of analytical ingredients. Opportunity Method's inquiry/choice separation and source-informed design. | Experience-based account, not validation of this cross-holder construction Method or every future outcome. Reopen on a material limitation of that use. |
| [NCDG 2024](https://www.ncda.org/aws/NCDA/pt/sp/ncdg_home_page), CD2/CD3 | Human-branch alternatives, consequences and qualified current career information. Both human examples. | Does not supply intervention, transfer, organization or AI mechanisms. Reopen the human information-use claims when their source or receiving use changes. |
| [NCDA Code of Ethics 2024](https://www.ncda.org/aws/NCDA/asset_manager/get_file/3395), A.2, A.10 and E.2 | Human career-service participation, assessment competence and referral/closure boundaries. Profile engagement and return. | Profession-specific conditions; applicability must be established. No efficacy, legal or AI-holder assessment conclusion follows. Reopen only affected service claims. |
| [ICMCI competence framework v4.0, 2021](https://www.cmc-global.org/sites/default/files/public/icmci_cmc002_competence_framework_version_4.0_1.pdf), C.1.1–2, C.2.1 and E.3.5 | Agreed consulting engagement content, client involvement and material conflict disclosure. Profile engagement/return. | A verified bounded baseline, not a claim that v4.0 is the latest framework. Reopen when an applicable later clause changes the used service condition. |
| [ICMCI AI Code v1.0, May 2026](https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf), §§1.2, 2.2, 3.1–3.4, 5.1–5.4, 7 | Adds a qualified current source for AI used by an adviser: professional responsibility, material-output checking, data restrictions and client disclosure. | Applies within its stated professional/adoption scope. Does not supply AI-holder evaluation or intervention evidence. Reopen the affected service use, not every holder claim. |

ICMCI’s [June 2026 release announcement](https://www.cmc-global.org/content/icmci-launches-global-code-responsible-use-ai-management-consulting) documents the publication of the AI Code. The professional clauses cited here come from the Code. A [2026 competence-framework update presentation](https://www.cmc-global.org/content/icd-2026) is also available. For a conclusion about the complete revised certification framework, examine the applicable framework. The selected earlier engagement clauses support their named uses.

The [subject-specific supplier account](#psdareference12---obtain-the-result-needed-for-the-developing-subject) identifies the result each practice can supply. Use the [source-change and case-change account](#psdareference13---keep-source-changes-and-case-changes-distinct) to distinguish a source-claim change from a change in the developing subject or advisory service.

## PSDA.Sources:4 - Source access for the development applications

### PSDA.Sources:4.1 - Learning Product source access

The following Learning Product Development LPF sources supply the contributions used in APP-PSD-04. This publication identifies them and summarizes their role. It does not include their full instructions or a verified public address for retrieving them.

| Exact source | Contribution used in APP-PSD-04 |
| --- | --- |
| LG.02 - Design a Long Learning Route with Stable Addresses | Place the first distinction, worked use and later varied return along a learning route with stable addresses. |
| LG.03 - Check a Completed Guide Passage against the Learner’s Next Action | Check whether a completed Guide fragment supports the learner's next action and identify the bounded repair. |
| LG.05 - Design a Learning Unit That Teaches How to Apply a Pattern | Develop a pattern-centred unit around recognition, explanation, action, result/check, a worked case and practice. |

When the question concerns the full instructions, use an available authorized copy or obtain the applicable text from Learning Product maintenance. Its LPF marks LG.05 as Candidate. Qualify the proposed use before relying on it as established guidance. For a Guide-design question, an adequate existing design result can suffice. If neither suitable source guidance nor a qualified result supplies the needed design contribution, identify what remains missing. Other opportunity and programme results retain their supported uses.

### PSDA.Sources:4.2 - Foundations programme source access

**ThinkingFoundations + EngineeringFoundations** is the programme source. **Grounds for Choosing and Comparing Programmes** is its supporting account of programme choice and comparison, inspected on 2 September 2026. They illustrate design before any one learner’s development question is known. This publication gives their role and does not provide the full working texts or a verified public route to them.

For the full design and comparison in this example, consult both sources where available or obtain them from the responsible designer or maintainer. For an individual programme assessment, use a compatible HCD.2 result and evidence of the person’s starting conditions, later tasks, access, support and participation. Another qualified comparison can serve the advice or choice directly.

### PSDA.Sources:4.3 - Predecessor source-account access

**Development-direction profile: source responsibility and local refresh** is the earlier source account, with a qualification window of 2 September 2026. The public [Source responsibility and references](#psdasources3---source-responsibility-and-references) gives a condensed account of the contributions used.

Use the public account for the contribution it states. If a historical source-use decision turns on an omitted detail, consult an accessible copy of the earlier account or obtain it from profile maintenance. Preserve any independently qualified contributions from the sources and Core patterns.

### PSDA.Sources:4.4 - A useful stop when access is incomplete

If a source is inaccessible, state which claim lacks support and keep any narrower answer whose grounds remain available. A qualified alternative result may answer the question. Seek stronger evidence when it can make the needed difference at a justified cost.

## PSDA.Sources:5 - Source grounds for the development applications and their suppliers

Use the following sources for the contributions and limits given in the table. The Core bodies develop the general opportunity and continuing-development methods. Advice and applications here rely on those methods for the uses identified.

### PSDA.Sources:5.1 - Opportunity, characterization, and retained possibilities

| Source and relied-on contribution | Use in this framework | Limit and smallest reopen |
| --- | --- | --- |
| [ISO 56007:2023](https://www.iso.org/standard/75068.html): opportunity/idea and concept work before solution development and deployment. | **Adapted** in C.40.OI, C.40.NU, C.40.PC, C.40.DC: independent early inquiry, contrastive search, receiving problem/contribution and prospective support configuration. | Reliance is on its public scope, not an inspected full paid standard or effectiveness evidence. Reopen the affected front-end boundary if that scope or a stronger practice changes it. |
| [Phillips, Decision Analysis for Practitioners, 2025](https://pubsonline.informs.org/doi/full/10.1287/deca.2025.0356): requisite modelling, revisable problem framing and exploration sufficient to move forward. | **Adopted and compared** in C.40.OI: a strong alternative when joint modelling and sensitivity analysis serve the question; adapted to a bounded development inquiry with an optional no-adviser entry. | A practitioner account with cases, not comparative effectiveness evidence for these opportunity Methods. Reopen the bounded-entry choice when direct modelling already supplies the needed result. |
| [Keeney, Value-Focused Brainstorming](https://pubsonline.informs.org/doi/10.1287/deca.1120.0251): generate alternatives from explicit values and avoid early group anchoring. | **Adapted historical anchor** in C.40.NU, joined to current bounded inquiry and source-qualified return. | This earlier contribution is not labelled the whole current SoTA or a universal generation Method. A better contrastive approach reopens the affected search move. |
| [ISO 56008:2024](https://www.iso.org/standard/78485.html): measurement and review for innovation management. | **Bounded comparator** for organization/campaign characterization in C.40.OC. | Organization scope does not supply person, AI or facility measures. Reopen its affected measurement comparison, not every holder branch. |
| [FPF E.10.DEV](https://raw.githubusercontent.com/ailev/FPF/main/FPF-Spec.md), [FPF C.16](https://raw.githubusercontent.com/ailev/FPF/main/FPF-Spec.md), [FPF C.11.CRC](https://raw.githubusercontent.com/ailev/FPF/main/FPF-Spec.md), [FPF C.11.DUA](https://raw.githubusercontent.com/ailev/FPF/main/FPF-Spec.md), [FPF A.15.9](https://raw.githubusercontent.com/ailev/FPF/main/FPF-Spec.md), [FPF C.18](https://raw.githubusercontent.com/ailev/FPF/main/FPF-Spec.md) and [FPF C.19](https://raw.githubusercontent.com/ailev/FPF/main/FPF-Spec.md). | Their directly defined semantic recovery, measurement, finite comparison, inquiry appraisal, external-result use and acquisition, archive/front and live-pool contributions are **adopted or adapted** at the body loci named in each pattern's SoTA account. | None establishes a particular holder result. C.19 governs actual live-pool treatment, including under unchanged policy; it is not a local probe selector. A changed definition reopens the dependent opportunity claim. |
| [OECD, Proactive portfolio management in mission-oriented innovation policy, 2025](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/03/proactive-portfolio-management-in-mission-oriented-innovation-policy_6bc6df0e/1ee956a5-en.pdf), sections 2–4: complementary activities, stage dependencies, resources, adaptation and termination. | **Adapted** in C.40.OP's retention, stage-specific comparison and reconsideration. | Its mission selection and funding remain external; it supplies no universal horizon count, individual development mechanism or demonstrated option valuation. Reopen the particular retention or specialist-valuation question. |

### PSDA.Sources:5.2 - Professional and AI-source qualification

| Source and qualified reading | Receiving contribution | Scope limit and return |
| --- | --- | --- |
| [NCDA Code of Ethics, 2024](https://www.ncda.org/aws/NCDA/asset_manager/get_file/3395), A.2, A.10 and E.2. | **Adapted** in PSDA.19's career-service participation, assessment-competence, information-use and referral boundaries. | The identified professional scope does not establish local law or the adviser's actual competence. Determine the applicable service and local requirements before relying on those claims. A changed code or use reopens the affected condition. |
| [ICMCI competence framework v4.0, approved October 2021](https://www.cmc-global.org/sites/default/files/public/icmci_cmc002_competence_framework_version_4.0_1.pdf), identified C.1/C.2 engagement and E.3.5 impartiality clauses. | **Bounded clause reliance** for client involvement and material conflict treatment in PSDA.19. | The official [ICD 2026 page](https://www.cmc-global.org/content/icd-2026) lists an update presentation. Its existence does not make this older framework the complete current standard or establish that the full update was inspected. A complete current certification claim remains outside this reliance. |
| [ICMCI Code of Responsible Use of Artificial Intelligence, v1.0, May 2026](https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf), sections 1.2, 2.2, 3.1–3.4, 5 and 7. | **Adopted within professional scope** in PSDA.19: responsibility, human content review, protected information, competence and material-use disclosure. | Routine tool availability is not warrant. Actual adoption, contract and applicable requirements determine the service conditions. The code does not evaluate an AI development subject. |
| [NIST AI RMF Playbook, MAP 1.1 and MAP 4.1](https://airc.nist.gov/airmf-resources/playbook/map/): receiving context, assumptions, third-party components and support risks. | **Adapted** in C.40.JF and C.40.RQ for configuration-specific joint premises and changed-use effects. | These Map contributions do not provide the client's evaluation, causal result or permission. The source describes RMF revision in progress; this is not reliance on a claimed completed replacement edition. Reopen the affected configuration or source claim. |

Suppose an adviser needs to know what “ICMCI compliant” establishes for an engagement. The inspected v4.0 clauses support the specified client-involvement and conflict conditions. The May 2026 AI Code contributes conditions for AI use in its stated scope. A claim about compliance with the complete current framework requires the applicable full standard and evidence for the engagement. The 2026 update notice identifies a reason to check that claim. Keep the bounded earlier contributions where they still apply and establish the relevant local professional and legal conditions separately.

The [Architectural Reference](#decision-design-principles-framework-architectural-reference) explains the connected language and the consequences of these sources for its use.

## PSDA.Sources:End
